Integrating this over the volume occupied by the fluid, we find that the first term gives rise to

$$
\frac { d } { d t } \int \rho ^ { * } \Big ( \frac { 1 } { 2 } v ^ { 2 } + \Pi \Big ) d ^ { 3 } x
$$

after taking the total time derivative outside the integral. By virtue of Eq. (8.120d) we find that the second term contributes

$$
\frac { d } { d t } \int \rho ^ { * } \Big ( - \frac { 1 } { 2 } U \Big ) d ^ { 3 } x ,
$$

and the third term vanishes (by Gauss’s theorem) after integration. Writing

$$
E = \mathcal { T } + \Omega + E _ { \mathrm { i n t } } + O ( c ^ { - 2 } )
$$

with

$$
\begin{array} { r c l } { \displaystyle \mathcal { T } : = \frac { 1 } { 2 } \int \rho ^ { * } v ^ { 2 } d ^ { 3 } x , } \\ { \displaystyle \Omega : = - \frac { 1 } { 2 } \int \rho ^ { * } U d ^ { 3 } x , } \\ { \displaystyle E _ { \mathrm { i n t } } : = \int \rho ^ { * } \Pi d ^ { 3 } x , } \end{array}
$$

we have shown that $d E / d t = 0$ . We recognize in $\tau$ the total kinetic energy of the fluid, $\Omega$ is the total gravitational potential energy, and $E _ { \mathrm { i n t } }$ is the total internal energy; these add up to the conserved energy $E$ .

The total mass-energy $M$ of the fluid system is defined by $M : = m + E / c ^ { 2 }$ . Combining Eqs. (8.132) and (8.134), this is

$$
M : = \int \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \Bigr ) \biggr ] d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) ,
$$

and we have that $d M / d t = 0$ . We have encountered the expression of Eq. (8.136) before, back in Sec. 7.3.2, in the context of the post-Minkowskian approximation. In Chapter 7 the total mass-energy was defined by $M : = c ^ { - 2 } \int ( - g ) ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } ) d ^ { 3 } x$ , in terms of the fluid’s energy-momentum tensor and the Landau–Lifshitz pseudotensor. In the present context, our expression for $M$ was obtained by manipulating the fluid equations, and it is reassuring that we have complete consistency between the two approaches.

# 8.4.6 Conservation of momentum

More work is required to identify the total momentum $P ^ { j }$ and show that ${ d P ^ { j } } / { d t } = 0$ . We return to Eq. (8.112) and examine the second group of post-Newtonian terms. We see that the terms involving the Newtonian potential can be grouped into

$$
2 \rho ^ { * } v _ { j } \frac { d U } { d t } = 2 \rho ^ { * } \frac { d } { d t } ( U v _ { j } ) - 2 \rho ^ { * } U \frac { d v _ { j } } { d t } ,
$$

$$
2 \rho ^ { * } v _ { j } \frac { d U } { d t } = 2 \rho ^ { * } \frac { d } { d t } ( U v _ { j } ) + 2 U \partial _ { j } p - 2 \rho ^ { * } U \partial _ { j } U + O ( c ^ { - 2 } )
$$

after inserting the Newtonian version of Euler’s equation. The terms involving the vector potential can similarly be expressed as $- 4 \rho ^ { * } ( d U _ { j } / d t - v ^ { k } \partial _ { j } U _ { k } )$ , and we find that the local statement of momentum conservation becomes

$$
\begin{array} { l } { { \displaystyle 0 = \partial _ { t } ( \mu \rho ^ { * } v ^ { j } ) + \partial _ { k } ( \mu \rho ^ { * } v ^ { j } v ^ { k } ) + \partial _ { j } p - \rho ^ { * } \partial _ { j } U + \frac { 2 } { { c } ^ { 2 } } U \partial _ { j } p } } \\ { { \displaystyle \quad - \frac { 1 } { { c } ^ { 2 } } \rho ^ { * } \bigg ( \frac { 3 } { 2 } v ^ { 2 } - U + \Pi + p / \rho ^ { * } \bigg ) \partial _ { j } U + \frac { 2 } { { c } ^ { 2 } } \rho ^ { * } \frac { d } { d t } \Big ( U v _ { j } - 2 U _ { j } \Big ) } } \\ { { \displaystyle \quad + \frac { 4 } { { c } ^ { 2 } } \rho ^ { * } v ^ { k } \partial _ { j } U _ { k } - \frac { 1 } { { c } ^ { 2 } } \rho ^ { * } \partial _ { j } \Psi + { \cal O } ( { c } ^ { - 4 } ) , } } \end{array}
$$

with $\mu$ defined by Eq. (8.113).

We next integrate this equation over the volume occupied by the fluid. Examining each term in turn, we find that the integral of the first term contributes

$$
\frac { d } { d t } \int \mu \rho ^ { * } v ^ { j } d ^ { 3 } x ,
$$

but that the integrals of the second, third, and fourth terms vanish by virtue of Gauss’s theorem and the identity of Eq. (8.120a). For the fifth term we get $\begin{array} { r } { - 2 c ^ { - 2 } \int p \partial _ { j } U d ^ { 3 } x } \end{array}$ after integration by parts. Leaving the sixth term alone for the time being, we note that the seventh term becomes

$$
\frac { 2 } { c ^ { 2 } } \frac { d } { d t } \int \rho ^ { * } ( U v _ { j } - 2 U _ { j } ) d ^ { 3 } x = - \frac { 2 } { c ^ { 2 } } \frac { d } { d t } \int \rho ^ { * } U v _ { j } d ^ { 3 } x
$$

after involvement of Eq. (8.120b). And finally, we obtain

$$
\begin{array} { l } { { \displaystyle 0 = \frac { d } { d t } \int \mu \rho ^ { * } v ^ { j } d ^ { 3 } x - \frac { 2 } { c ^ { 2 } } \frac { d } { d t } \int \rho ^ { * } U v _ { j } d ^ { 3 } x } } \\ { { \displaystyle ~ - \frac { 1 } { c ^ { 2 } } \int \rho ^ { * } \biggl ( \frac { 3 } { 2 } v ^ { 2 } - U + \Pi + 3 p / \rho ^ { * } \biggr ) \partial _ { j } U d ^ { 3 } x + \frac { 4 } { c ^ { 2 } } \int \rho ^ { * } v ^ { k } \partial _ { j } U _ { k } d ^ { 3 } x } } \\ { { \displaystyle ~ - \frac { 1 } { c ^ { 2 } } \int \rho ^ { * } \partial _ { j } \psi d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int \rho ^ { * } \partial _ { t t j } X d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) } } \end{array}
$$

after inserting $\begin{array} { r } { \Psi = \psi + \frac { 1 } { 2 } \partial _ { t t } { \boldsymbol { X } } } \end{array}$ within the last term. This simplifies to

$$
0 = \frac { d } { d t } \int \mu \rho ^ { * } v ^ { j } d ^ { 3 } x - \frac { 2 } { c ^ { 2 } } \frac { d } { d t } \int \rho ^ { * } U v _ { j } d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int \rho ^ { * } \partial _ { t t j } X d ^ { 3 } x + O ( c ^ { - 4 } )
$$

when we invoke the identities of Eqs. (8.120c) and (8.120e).

We must now work on the term involving the superpotential. We write

$$
\rho ^ { * } \partial _ { t t j } X = \rho ^ { * } \frac { d } { d t } \big ( \partial _ { t j } X \big ) - \rho ^ { * } v ^ { k } \partial _ { t j k } X
$$

and integrate. We obtain

$$
\int \rho ^ { * } \partial _ { t t j } X d ^ { 3 } x = - \frac { d } { d t } \int \rho ^ { * } U _ { j } d ^ { 3 } x + \frac { d } { d t } \int \rho ^ { * } \Phi _ { j } d ^ { 3 } x
$$

after using Eqs. (8.10) and (8.122), and we note that by virtue of Eq. (8.120b), the first integral on the right-hand side can also be expressed as $\int \rho ^ { * } U v _ { j } d ^ { 3 } x$ .

Collecting results, we have obtained the conservation statement ${ d P ^ { j } } / { d t } = 0$ , with the total momentum $P ^ { j }$ identified as

$$
P ^ { j } : = \int \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi + p / \rho ^ { * } \Bigr ) \biggr ] d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int \rho ^ { * } \Phi ^ { j } d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) .
$$

We recall that the potential $\Phi ^ { j }$ was defined by Eq. (8.8). In Chapter 7 the total momentum was defined as $P ^ { j } : = c ^ { - 1 } \int ( - g ) ( T ^ { 0 j } + t _ { \mathrm { L L } } ^ { 0 j } ) d ^ { 3 } x$ , and this led to the expression displayed in Eq. (7.65). A glance at Eq. $( 8 . 1 2 0 \mathrm { g } )$ confirms that the two expressions are equivalent.

The total momentum of a post-Newtonian spacetime can always be made to vanish by performing a post-Galilean transformation of the type described in Sec. 8.3.6. The transformation is characterized by the velocity vector $V ^ { j } = P ^ { j } / M$ .

# 8.4.7 Center-of-mass

Inspection of Eq. (8.132) suggests that a plausible expression for the position of the centerof-mass might be

$$
R ^ { j } : = \frac { 1 } { M } \int \rho ^ { * } x ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \Bigr ) \biggr ] d ^ { 3 } x + O ( c ^ { - 4 } ) .
$$

This matches the result obtained back in Sec. 7.3.2 on the basis of the post-Minkowskian definition $R ^ { j } : = ( M c ^ { 2 } ) ^ { - 1 } \textstyle \int ( - g ) ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } ) x ^ { j } d ^ { 3 } x$ . We confirm this result by proving that with Eq. (8.146), we can produce the expected center-of-mass relation

$$
M \dot { R } ^ { j } = P ^ { j } + O ( c ^ { - 4 } ) .
$$

Once $P ^ { j }$ has been set equal to zero by performing a post-Galilean transformation, the position of the center-of-mass is fixed in space, and a constant translation of the spatial coordinates allows us to set $R ^ { j } = 0$ . The conditions $P ^ { j } = 0$ and $R ^ { j } = 0$ define the centerof-mass frame of the fluid system.

We express Eq. (8.146) as $\begin{array} { r } { M R ^ { j } = \int { \nu \rho ^ { * } x ^ { j } d ^ { 3 } x } + O ( c ^ { - 4 } ) } \end{array}$ , with $\nu = 1 + c ^ { - 2 } ( { \textstyle { \frac { 1 } { 2 } } } v ^ { 2 } -$ ${ \frac { 1 } { 2 } } U + \Pi )$ . Differentiation with respect to time produces

$$
M \dot { R } ^ { j } = \int \nu \rho ^ { * } v ^ { j } d ^ { 3 } x + \int \rho ^ { * } x ^ { j } \frac { d \nu } { d t } d ^ { 3 } x ,
$$

and this can be written in the form

$$
M \dot { R } ^ { j } = R ^ { j } - \frac { 1 } { c ^ { 2 } } \int p v ^ { j } d ^ { 3 } x + \frac { 1 } { 2 c ^ { 2 } } \int \rho ^ { * } \Phi ^ { j } d ^ { 3 } x + \int \rho ^ { * } x ^ { j } \frac { d \nu } { d t } d ^ { 3 } x
$$

after incorporating Eq. (8.145). The derivative of $\nu$ can be evaluated with the help of Euler’s equation (8.104) and the first law of thermodynamics, Eq. (8.105). We obtain

$$
\rho ^ { * } x ^ { j } \frac { d \nu } { d t } = - \frac 1 { c ^ { 2 } } x ^ { j } \partial _ { k } ( p v ^ { k } ) - \frac 1 { 2 c ^ { 2 } } \rho ^ { * } x ^ { j } \big ( \partial _ { t } U - v ^ { k } \partial _ { k } U \big ) + { \cal O } ( c ^ { - 4 } ) ,
$$

and integration yields

$$
\int \rho ^ { * } x ^ { j } { \frac { d \nu } { d t } } d ^ { 3 } x = { \frac { 1 } { c ^ { 2 } } } \int p v ^ { j } d ^ { 3 } x - { \frac { 1 } { 2 c ^ { 2 } } } \int \rho ^ { * } \Phi ^ { j } d ^ { 3 } x + O ( c ^ { - 4 } ) ;
$$

we integrated the first term by parts and made use of Eq. $( 8 . 1 2 0 \mathrm { g } )$ for the second term.   
Making the substitution into Eq. (8.149), we see that Eq. (8.147) is indeed satisfied.

# 8.5 Bibliographical notes

The Maxwell-like formulation of the equations of post-Newtonian theory, as reviewed in $\mathrm { B o x } ~ 8 . 1$ , has received a number of presentations in the literature. One of the earliest incarnations was provided by Braginskii, Caves, and Thorne (1977).

The classic approach to post-Newtonian theory can be traced to the earliest days of general relativity. Representative works are Lorentz and Droste (1917), Eddington and Clark (1938), Einstein, Infeld, and Hoffmann (1938), and the treatise by Fock (1959). The work was invigorated by Chandrasekhar in the nineteen sixties, through a series of papers written with students and collaborators: Chandrasekhar and Contopoulos (1967), Chandrasekhar (1965 and 1969), Chandrasekhar and Nutku (1969), and Chandrasekhar and Esposito (1970).

The theory of post-Newtonian coordinate transformations developed in Sec. 8.3 was first initiated by Damour, Soffel, and Xu (1991); our treatment follows Racine and Flanagan (2005). The post-Galilean subclass of transformations was first investigated in Chandrasekhar and Contopoulos (1967). The rotating coordinates of $\mathrm { B o x } ~ 8 . 3$ and the darned disk are described in some detail in Robertson and Noonan (1968).

The post-Newtonian theory of fluid dynamics was first developed in Chandrasekhar (1965 and 1969). Our treatment in Sec. 8.4 follows the master’s work quite closely.

# 8.6 Exercises

8.1 Show that the inverse to the metric of Eqs. (8.20) is given by

$$
\begin{array} { l } { { g ^ { 0 0 } = - 1 - \displaystyle \frac { 2 } { c ^ { 2 } } { \cal U } - \displaystyle \frac { 2 } { c ^ { 4 } } \big ( \Psi + { \cal U } ^ { 2 } \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle g ^ { 0 j } = - \displaystyle \frac { 4 } { c ^ { 3 } } { \cal U } ^ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g ^ { j k } = \bigg ( 1 - \displaystyle \frac { 2 } { c ^ { 2 } } { \cal U } \bigg ) \delta ^ { j k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where $U ^ { j } : = \delta ^ { j k } U _ { k }$ . Show that the metric determinant is $\sqrt { - g } = 1 + 2 U / c ^ { 2 } +$ $O ( c ^ { - 4 } )$ . Verify Eqs. (8.15) for the Christoffel symbols.

8.2 Show that the post-Newtonian version of the geodesic equation $D u ^ { \alpha } / d \tau = 0$ can be presented in the form

$$
\frac { d ( g _ { s } \gamma v ) } { d t } = \gamma \Big ( E _ { \mathrm { g } } + v \times B _ { \mathrm { g } } + v ^ { 2 } \nabla g _ { s } \Big ) + O ( c ^ { - 4 } ) ,
$$

where $E _ { \mathrm { g } }$ and $B _ { \mathrm { g } }$ are the gravitational fields defined in $\operatorname { B o x } 8 . 1 , \gamma : = d t / d \tau$ , and $g _ { s } = 1 + 2 c ^ { - 2 } U$ is the coefficient of the spatial part of the metric.

8.3 (a) Show that the coordinate transformation

$$
t = \bar { t } , \qquad x ^ { j } = \bar { x } ^ { j } + \frac { \lambda } { c ^ { 2 } } \partial ^ { \bar { \jmath } } \bar { X } ,
$$

in which $\lambda$ is a constant, produces a new post-Newtonian metric given by

$$
\begin{array} { l } { { \displaystyle \bar { g } _ { 0 0 } = g _ { 0 0 } - \frac { 2 \lambda } { c ^ { 4 } } ( \bar { U } ^ { 2 } - \bar { \Phi } _ { 2 } + \bar { \Phi } _ { W } ) , } } \\ { { \displaystyle } } \\ { { \bar { g } _ { 0 j } = g _ { 0 j } + \frac { \lambda } { c ^ { 3 } } \partial _ { \bar { t } \bar { \jmath } } \bar { X } , } } \\ { { \displaystyle } } \\ { { \bar { g } _ { j k } = g _ { j k } + \frac { 2 \lambda } { c ^ { 2 } } \partial _ { \bar { \jmath } \bar { k } } \bar { X } , } } \end{array}
$$

where $g _ { \alpha \beta }$ denotes the original post-Newtonian metric, with all potentials defined in terms of $\bar { x } ^ { \alpha }$ , and where $\bar { \Phi } _ { W }$ is an auxiliary potential (known as the Whitehead potential) defined by

$$
\bar { \Phi } _ { W } : = G ^ { 2 } \int \bar { \rho } ^ { * \prime } \bar { \rho } ^ { * \prime \prime } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) _ { j } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } \left[ \frac { ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } } { | \bar { x } - \bar { x } ^ { \prime \prime } | } - \frac { ( \bar { x } - \bar { x } ^ { \prime \prime } ) ^ { j } } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | } \right] d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } ^ { \prime \prime } .
$$

(b) Consider a static system with a “point mass” at the origin. This assumption allows us to ignore the potentials $\bar { \psi } , \bar { \Phi } _ { 2 }$ , and $\bar { \Phi } _ { W }$ , and to set all time derivatives to zero. Find the value of $\lambda$ for which the metric is linear in $\bar { U }$ to post-Newtonian order. Show that the line element in spherical polar coordinates can be expressed to post-Newtonian order as

$$
d s ^ { 2 } = - ( 1 - { \cal R } / \bar { r } ) ( c d \bar { t } ) ^ { 2 } + ( 1 - { \cal R } / \bar { r } ) ^ { - 1 } d \bar { r } ^ { 2 } + \bar { r } ^ { 2 } \bigl ( d \bar { \theta } ^ { 2 } + \sin ^ { 2 } \bar { \theta } d \bar { \phi } ^ { 2 } \bigr ) ,
$$

where $\begin{array} { r } { R = ( 2 G / c ^ { 2 } ) \int \rho ^ { * } d ^ { 3 } x = 2 G m / c ^ { 2 } } \end{array}$ . What is this metric?

8.4 (a) Using the expressions for the Landau–Lifshitz pseudotensor given in Eqs. (7.48) and (7.49), together with the post-Newtonian expression for the potentials $h _ { 2 } ^ { \alpha \beta }$ from Box 7.5, show that the components of the effective energy-momentum pseudotensor $\tau ^ { 0 j }$ and $\tau ^ { j k }$ are given to post-Newtonian order by

$$
\begin{array} { l } { { \displaystyle c ^ { - 1 } \tau ^ { 0 j } = \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac 1 2 v ^ { 2 } + 3 U + \Pi + p / \rho ^ { * } \biggr ) \biggr ] } } \\ { { \displaystyle ~ + \frac { 1 } { 4 \pi G c ^ { 2 } } \biggl [ 3 \partial _ { t } U \partial ^ { j } U + 4 \bigl ( \partial ^ { j } U ^ { k } - \partial ^ { k } U ^ { j } \bigr ) \partial _ { k } U \biggr ] + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle \tau ^ { j k } = \rho ^ { * } \nu ^ { j } \nu ^ { k } \bigg [ 1 + \frac { 1 } { c ^ { 2 } } \Big ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi + p / \rho ^ { * } \Big ) \bigg ] + p \bigg ( 1 + \frac { 2 } { c ^ { 2 } } U \bigg ) \delta ^ { j k } } } \\ { { \displaystyle \qquad + \frac { 1 } { 4 \pi G } \Big ( \partial ^ { j } U \partial ^ { k } U - \frac { 1 } { 2 } \delta ^ { j k } \partial _ { n } U \partial ^ { n } U \Big ) } } \\ { { \displaystyle \qquad \frac { 1 } { 4 \pi G c ^ { 2 } } \bigg \{ 2 \partial ^ { ( j ) } U \partial ^ { k } \Psi - 1 6 \partial ^ { [ j } U ^ { n ] } \partial ^ { [ k } U ^ { n ] } + 8 \partial ^ { ( j } U \partial _ { t } U ^ { k ) } } } \\ { { \displaystyle \qquad - \delta ^ { j k } \Big [ \partial ^ { n } U \partial ^ { n } \Psi - 4 \partial ^ { [ m } U ^ { n ] } \partial ^ { [ m } U ^ { n ] } + 4 \partial ^ { n } U \partial _ { t } U ^ { n } + \frac { 3 } { 2 } ( \partial _ { t } U ) ^ { 2 } \Big ] \bigg \} } } \\ { { \displaystyle \qquad + O ( c ^ { - 4 } ) , } } \end{array}
$$

where $\begin{array} { r } { \Psi = \psi + \frac { 1 } { 2 } \partial _ { t t } X } \end{array}$ .

(b) Show that the conservation statement $\partial _ { \beta } \tau ^ { j \beta } = 0$ yields the post-Newtonian version of Euler’s equation, as displayed in Eq. (8.119). You may make use of the continuity equation for $\rho ^ { * }$ , the first law of thermodynamics, and the Poisson equations satisfied by the various potentials.

8.5 In this problem we consider the equilibrium structure of a spherical body in post-Newtonian theory, thereby generalizing the Newtonian discussion of Sec. 2.2. We assume that the matter distribution is static and spherically symmetric, so that all variables depend on $r$ only. Show that under these conditions, the gravitational potentials are determined by the set of equations

$$
\frac { d U } { d r } = - \frac { G m } { r ^ { 2 } } , \qquad \frac { d m } { d r } = 4 \pi r ^ { 2 } \rho ^ { * } ,
$$

$$
\frac { d \Psi } { d r } = - \frac { G n } { r ^ { 2 } } , \qquad \frac { d n } { d r } = 4 \pi r ^ { 2 } \rho ^ { * } ( - U + \Pi + 3 p / \rho ^ { * } ) ,
$$

where $n$ is a post-Newtonian auxiliary variable analogous to the Newtonian mass function $m$ . Show also that the equation of hydrostatic equilibrium becomes

$$
\frac { d p } { d r } = - \frac { G \rho ^ { * } } { r ^ { 2 } } \Bigg \{ m + \frac { 1 } { c ^ { 2 } } \Big [ ( - 3 U + \Pi + p / \rho ^ { * } ) m + n \Big ] \Bigg \} + { \cal O } ( c ^ { - 4 } ) .
$$

These equations are to be supplemented by an equation of state $p = p ( \rho ^ { * } )$ and the first law of thermodynamics, $d \Pi = ( p / \rho ^ { * 2 } ) d \rho ^ { * } + { \cal O } ( c ^ { - 2 } )$ .

8.6 The equations derived in the preceding problem should agree with the exact formulation of the structure equations, as presented in Sec. 5.6.5, when these are expressed as a post-Newtonian expansion. The comparison, however, is not entirely straightforward, because the formulations use different variables and coordinates.

(a) By comparing the metric of Eq. (5.156) with the post-Newtonian metric of Eq. (8.2), relate the radial coordinate $\bar { r }$ of Sec. 5.6.5 (perversely denoted $r$ there) to the harmonic radial coordinate $r$ employed in this chapter.   
(b) Show that the metric functions are related by $\Phi = U + \Psi / c ^ { 2 } + O ( c ^ { - 4 } )$ and $\bar { m } = m + O ( c ^ { - 2 } )$ , where $\bar { m }$ is the mass function defined by Eq. (5.158) (and denoted $m$ there).

(c) Prove that when Eqs. (5.215), (5.216), and (5.218) are expanded through order $c ^ { - 2 }$ in a post-Newtonian expansion, they agree with the equations derived in the preceding problem.

(d) Show that the comparison relies on the identification

$$
\bar { m } = m + \frac { 1 } { c ^ { 2 } } \big ( n + m U - G m ^ { 2 } / r - 4 \pi r ^ { 3 } p \big ) + O ( c ^ { - 4 } )
$$

for the relativistic mass function.

8.7 Using the Newtonian Euler equation and the first law of thermodynamics, verify the energy conservation equation (8.110).

8.8 Show that the conserved angular momentum tensor for an isolated system is given to post-Newtonian order by

$$
\begin{array} { c } { { J ^ { j k } = 2 \displaystyle \int \rho ^ { * } x ^ { [ j } \{ v ^ { k ] } + \frac { v ^ { k ] } } { c ^ { 2 } } ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi + p / \rho ^ { * } ) } } \\ { { - \displaystyle \frac { 1 } { c ^ { 2 } } \biggl ( 4 U ^ { k ] } - \frac { 1 } { 2 } \partial _ { t } ^ { k ] } X \biggr ) \Bigg \} d ^ { 3 } x . } } \end{array}
$$

8.9 Verify the integral identities of Eqs. (8.120e) and (8.120f).

In this chapter we apply the results of Chapter 8 to situations in which a fluid distribution breaks up into a collection of separated bodies. Our aim is to go from a fine-grained description involving the fluid variables $\{ \rho ^ { * } , p , \Pi , \pmb { v } \}$ to a coarse-grained description involving a small number of center-of-mass variables for each body. We accomplish this reduction in Sec. 9.1, and in Sec. 9.2 we apply it to a calculation of the spacetime metric in the empty region between bodies; the metric is thus expressed in terms of the mass-energy $M _ { A }$ , position $\pmb { r } _ { A } ( t )$ , and velocity ${ \pmb v } _ { A } ( t )$ of each body. In Sec. 9.3 we derive post-Newtonian equations of motion for the center-of-mass positions, and in Sec. 9.4 we show that the same equations apply to compact bodies with strong internal gravity. In Sec. 9.5 we allow the bodies to rotate, and we calculate the influence of the spins on the metric and equations of motion; we also derive evolution equations for the spin vectors. We conclude in Sec. 9.6 with a discussion of how point particles can be usefully incorporated within post-Newtonian theory, in spite of their infinite densities and diverging gravitational potentials.

# 9.1 From fluid configurations to isolated bodies

We consider a situation in which a distribution of perfect fluid breaks up into a number $N$ of separated components. We call each component a “body,” and label each body with the index $A = 1 , 2 , \dotsc , N$ . Mathematically, this means that we can express the fluid density as

$$
\rho ^ { * } = \sum _ { A } \rho _ { A } ^ { * } ;
$$

the sum extends over each body, and $\rho _ { A } ^ { * }$ is zero everywhere except within the volume occupied by body $A$ . In this situation we forbid the presence of matter between the bodies; for example, there is no mass transfer between any members of the $N$ -body system.

# 9.1.1 Center-of-mass variables

The material mass of body $A$ is

$$
m _ { A } : = \int _ { A } \rho ^ { * } d ^ { 3 } x .
$$

The domain of integration $V _ { A }$ is a time-independent region of three-dimensional space that extends beyond the volume occupied by the body. It is sufficiently large that in a time interval $d t$ , the body will not cross the domain’s boundary $S _ { A }$ ; but it is sufficiently small that $V _ { A }$ does not include nor intersect another body within the system. We could have inserted $\rho _ { A } ^ { * }$ in place of $\rho ^ { * }$ inside the integral, but since $\rho ^ { * } = \rho _ { A } ^ { * }$ within $V _ { A }$ , this distinction is not necessary. By virtue of Eq. (1) in Box 8.4, we have that $d m _ { A } / d t = 0$ .

We define the position of the center-of-mass of body $A$ by

$$
\pmb { r } _ { A } ( t ) : = \frac { 1 } { m _ { A } } \int _ { A } \pmb { \rho } ^ { * } \pmb { x } d ^ { 3 } \pmb { x } .
$$

This definition is largely arbitrary (as we have observed before in Box 1.7), but it proves convenient for our purposes: It produces simple expressions for the gravitational potentials, and the equations of motion for each body take a simple form when expressed in terms of $r _ { A }$ . We next introduce

$$
{ \pmb v } _ { A } ( t ) : = \frac { d { \pmb r } _ { A } } { d t } = \frac { 1 } { m _ { A } } \int _ { A } \rho ^ { * } { \pmb v } d ^ { 3 } x
$$

as the velocity of the body taken as a whole, and the body’s acceleration is

$$
{ \pmb a } _ { A } ( t ) : = \frac { d { \pmb v } _ { A } } { d t } = \frac { 1 } { m _ { A } } \int _ { A } \rho ^ { * } \frac { d { \pmb v } } { d t } d ^ { 3 } { \pmb x } .
$$

We evaluate this in Sec. 9.3 by inserting the post-Newtonian Euler equation within the integral.

# 9.1.2 Relative variables; reflection symmetry

To carry out the integrations over the domain $V _ { A }$ it is convenient to introduce the relative variables

$$
\bar { \pmb { x } } : = \pmb { x } - \pmb { r } _ { A } ( t ) , \qquad \bar { \pmb { v } } : = \pmb { v } - \pmb { v } _ { A } ( t ) ;
$$

the vector $\bar { x }$ gives the position of a fluid element relative to the center-of-mass $\pmb { r } _ { A } ( t )$ , while $\bar { v }$ measures the velocity of this fluid element relative to the body velocity ${ \pmb v } _ { A } ( t )$ . Under this transformation the domain $V _ { A }$ is translated by $- \pmb { r } _ { A } ( t )$ and becomes a neighborhood of the origin, and the volume element becomes $d ^ { 3 } { \bar { x } } = d ^ { 3 } x$ .

For technical reasons it will be useful to assume that each body is reflection-symmetric about its center-of-mass. Mathematically, this means that we shall impose the property

$$
\rho ^ { * } ( t , \pmb { r } _ { A } - \bar { \pmb { x } } ) = \rho ^ { * } ( t , \pmb { r } _ { A } + \bar { \pmb { x } } ) ,
$$

and subject the fluid pressure $p$ and the specific internal energy density $\Pi$ to the same symmetry. There is nothing particularly deep about this assumption, which is far less restrictive, for example, than demanding that each body be spherically symmetric. A generic body will not satisfy this symmetry requirement, but computations carried out for this generic body will involve a lot of additional details that can be avoided if we impose Eq. (9.7). In particular, the symmetry implies that any body integral that involves the product of an odd number of internal vectors, such as $\bar { x }$ or $\bar { \pmb { v } }$ , will vanish identically.

For example, the integral $\begin{array} { r } { \int _ { A } \rho ^ { * } ( \pmb { r } _ { A } + \pmb { \bar { x } } ) \bar { x } ^ { j } \bar { x } ^ { k } \bar { v } ^ { n } d ^ { 3 } \bar { x } } \end{array}$ becomes $\begin{array} { r } { - \int _ { A } \rho ^ { * } ( \pmb { r } _ { A } - \pmb { \bar { x } } ) \bar { x } ^ { j } \bar { x } ^ { k } \bar { v } ^ { n } d ^ { 3 } \bar { x } } \end{array}$ under a reflection across the center-of-mass, and Eq. (9.7) implies that the integral must vanish. In the following we frequently exploit this observation and eliminate many such odd integrals; and this is, ultimately, the sole reason for introducing the symmetry requirement of Eq. (9.7). In the course of our development we will accumulate a lot of evidence to support the claim that the gravitational field outside the bodies, and the motion of these bodies, are largely insensitive to details of internal structure. We might as well, therefore, impose the reflection symmetry and benefit from its great convenience, feeling sure that the longer computations required for a generic body would lead to the same answers.

# 9.1.3 Structure integrals; equilibrium conditions

As we shall see, the internal structure of each body is characterized by a number of structure integrals, which we introduce here. We first have the scalar quantities

$$
\begin{array} { r l } & { T _ { A } : = \cfrac { 1 } { 2 } \int _ { a } \rho ^ { * } \bar { v } ^ { 2 } d ^ { 3 } \bar { x } , } \\ & { \Omega _ { A } : = - \cfrac { 1 } { 2 } G \int _ { 4 } \frac { \rho ^ { * } \rho ^ { * } } { | \bar { x } - \bar { x } ^ { * } | } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } , } \\ & { P _ { A } : = \cint _ { A } p d ^ { 3 } \bar { x } , } \\ & { E _ { A } ^ { \mathrm { i n } } : = \cint _ { A } \rho ^ { * } \Pi ^ { d ^ { 3 } } \bar { x } , } \\ & { H _ { A } : = G \int _ { a } \rho ^ { * } \rho ^ { * } \frac { \bar { v } _ { j } ^ { \prime } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { | \bar { x } - \bar { x } ^ { * } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } , } \end{array}
$$

which are all functions of time $t$ . Here $\rho ^ { * } , p , \Pi$ , and $\bar { \pmb { v } }$ are all expressed as functions of $t$ and position $\pmb { r } _ { A } ( t ) + \pmb { \bar { x } }$ , and $\rho ^ { * \prime }$ stands for $\rho ^ { * } ( t , r _ { A } + \bar { x } ^ { \prime } )$ . We have encountered some of these quantities before: $\mathcal { T } _ { A }$ is recognized as the total kinetic energy of body $A$ (as measured in $A$ ’s comoving frame), $\Omega _ { A }$ is the total gravitational potential energy, $P _ { A }$ is the integrated pressure, and $E _ { A } ^ { \mathrm { i n t } }$ is the total internal energy; $H _ { A }$ is a new quantity.

We also have the tensorial quantities

$$
\begin{array} { l } { { { \cal I } _ { { \cal A } } ^ { j k } : = \displaystyle \int _ { \cal A } \rho ^ { * } \bar { x } ^ { j } \bar { x } ^ { k } d ^ { 3 } \bar { x } , } } \\ { { \displaystyle S _ { { \cal A } } ^ { j k } : = \displaystyle \int _ { \cal A } \rho ^ { * } \left( \bar { x } ^ { j } \bar { \nu } ^ { k } - \bar { x } ^ { k } \bar { \nu } ^ { j } \right) d ^ { 3 } \bar { x } , } } \\ { { \displaystyle T _ { { \cal A } } ^ { j k } : = \displaystyle \frac { 1 } { 2 } \int _ { \cal A } \rho ^ { * } \bar { \nu } ^ { j } \bar { \nu } ^ { k } d ^ { 3 } \bar { x } , } } \\ { { \displaystyle L _ { { \cal A } } ^ { j k } : = \displaystyle \int _ { { \cal A } } \bar { \nu } ^ { j } \partial _ { k } p d ^ { 3 } \bar { x } , } } \\ { { \displaystyle \Omega _ { { \cal A } } ^ { j k } : = - \displaystyle \frac { 1 } { 2 } G \displaystyle \int _ { \cal A } \rho ^ { * } \rho ^ { * } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } d ^ { 3 } \bar { x } , } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { l } { { \displaystyle H _ { A } ^ { j k } : = G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \frac { \bar { v } ^ { \prime } { } ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { \vert \bar { \bar { x } } - \bar { x } ^ { \prime } \vert ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } , } } \\ { { \displaystyle K _ { A } ^ { j k } : = G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \frac { \bar { v } _ { n } ^ { \prime } ( \bar { { \bar { x } } } - \bar { x } ^ { \prime } ) ^ { n } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { \vert \bar { x } - \bar { x } ^ { \prime } \vert ^ { 5 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } , } } \end{array}
$$

where $\bar { v } ^ { \prime j }$ is the relative velocity field at position $\pm \bar { x } ^ { \prime } + \bar { x } ^ { \prime }$ . Some of these structure integrals, like the quadrupole moment $\dot { I } _ { A } ^ { j k }$ , the angular-momentum tensor $S _ { A } ^ { j k }$ , the kinetic-energy tensor $\mathcal { T } _ { A } ^ { j k }$ , and the potential-energy tensor $\Omega _ { A } ^ { j k }$ , were encountered before; note that $\mathcal { T } _ { A } =$ T A and The others, A， , and , are new; note that $\delta _ { j k } \mathcal { T } _ { A } ^ { j k }$ $\Omega _ { A } = \delta _ { j k } \Omega _ { A } ^ { j k } .$ $H _ { A } ^ { j k } , K _ { A } ^ { j k }$ $L _ { A } ^ { j k }$ $H _ { A } = \delta _ { j k } H _ { A } ^ { j k }$

As an additional assumption concerning the bodies, we shall take them to be in dynamical equilibrium. By this we mean that each body has had time, under its own internal dynamics, to relax to a steady state in which its structure properties do not depend on time. This means, in particular, that the structure integrals listed in Eqs. (9.8) and (9.9) can all be taken to be time-independent. And as we show below in Sec. 9.1.7, the assumption also implies the validity of the equilibrium conditions

$$
2 { \cal T } _ { A } ^ { j k } + \Omega _ { A } ^ { j k } + \delta ^ { j k } { \cal P } _ { A } = { \cal O } ( c ^ { - 2 } )
$$

and

$$
4 H _ { A } ^ { ( j k ) } - 3 K _ { A } ^ { j k } + \delta ^ { j k } \dot { P } _ { A } - 2 L _ { A } ^ { ( j k ) } = { \cal O } ( c ^ { - 2 } ) .
$$

We also record the trace of Eq. (9.10),

$$
2 T _ { A } + \Omega _ { A } + 3 P _ { A } = { \cal O } ( c ^ { - 2 } ) .
$$

It is important to understand that the equilibrium conditions are valid only approximately. We have insisted that each body should reach an equilibrium state under its own internal dynamics, which involves hydrodynamical processes and the body’s own gravitational field. Each body, however, is also subjected to the gravitational influence of the remaining bodies, and this external dynamics comes in two different guises. The first effect, and by far the most important one, is the motion of the body’s center-of-mass in the field of the external bodies; this will be considered in Sec. 9.3, and the key point here is that the motion of the body as a whole does not prevent it from reaching an internal equilibrium state. The second effect, however, produces a small deviation from equilibrium; this is the tidal interaction between the body and its companions, produced by inhomogeneities in the external gravitational field across the volume occupied by the body. This effect, however, is small when the bodies are widely separated (we shall quantify this in the following subsection), and we shall ignore it in this and the following sections. Our conclusion is that while the equilibrium conditions are approximate, they hold to a large degree of accuracy, and this degree is quite sufficient for our purposes.

# 9.1.4 Multipole structure

In principle the mass distribution of each body is characterized by an infinite number of mass multipole moments $I _ { A } ^ { L } ( t )$ , and the fluid motions within each body are characterized by an infinite number of current multipole moments $J _ { A } ^ { j L } ( t )$ ; here $L : = k _ { 1 } k _ { 2 } \cdot \cdot \cdot k _ { \ell }$ is a multi-index that contains a number $l$ of individual indices. The most important moments have already been introduced: we have the mass monopole moment $m _ { A }$ , the quadrupole moment $I _ { A } ^ { j k }$ , and the angular-momentum tensor $S _ { A } ^ { j k }$ . We shall first simplify this description by demanding that the bodies be well separated.

This condition can be formulated as follows. Let $R _ { A }$ be a length scale associated with the volume occupied by body $A$ , and let $s _ { A } : = | \pmb { x } - \pmb { r } _ { A } |$ be the distance from $A$ ’s center-of-mass. We assume that in most applications that will interest us,

$$
R _ { A } \ll s _ { A } .
$$

This implies that when, for example, we evaluate the gravitational potentials outside each body, we are allowed to ignore all terms generated by the quadrupole moment $I _ { A } ^ { j k }$ and its higher-order analogues. To see this, recall that relative to the monopole term in the Newtonian potential, the quadrupole term scales as $I _ { A } ^ { j k } / ( m _ { A } s _ { A } ^ { 2 } )$ , or $( R _ { A } / s _ { A } ) ^ { 2 }$ , which is small by virtue of Eq. (9.13). The suppression is even more dramatic when the body is intrinsically spherical, and deformed ever so slightly by its tidal coupling with the other bodies; in this case $I _ { A } ^ { j k }$ scales as $m _ { A } R _ { A } ^ { 5 } / r _ { A B } ^ { 3 }$ instead of $m _ { A } R _ { A } ^ { 2 }$ , where $r _ { A B } : = | \pmb { r } _ { A } - \pmb { r } _ { B } |$ is the inter-body distance, and the quadrupole term is smaller than the monopole term by a factor of order $R _ { A } ^ { 5 } / ( r _ { A B } ^ { 3 } s _ { A } ^ { 2 } ) \ll 1 .$ . On the other hand, the condition of Eq. (9.13) is obviously invalid when we examine the internal structure of each body.

In our initial treatment of the $N$ -body system, we shall also simplify the multipole description by taking each body to be non-rotating. We shall therefore set

$$
S _ { A } ^ { j k } = 0 ,
$$

and maintain this assumption until Sec. 9.5, in which we finally incorporate the spinning motion of each body into the metric and equations of motion.

# 9.1.5 Internal and external potentials

In the following computations we shall have to distinguish between the gravitational potentials produced by body $A$ and those produced by the remaining bodies in the system. To accomplish this we proceed as in Sec. 1.6.3 and introduce a decomposition of each potential into internal and external pieces. For example, the Newtonian potential $U$ is decomposed as

$$
U = U _ { A } + U _ { \lnot A } ,
$$

with

$$
U _ { A } ( t , { \pmb x } ) = G \int _ { A } \frac { \rho ^ { * } ( t , { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } d ^ { 3 } x ^ { \prime }
$$

denoting the internal piece, and

$$
U _ { \neg { A } } ( t , { \pmb x } ) = \sum _ { B \not = A } G \int _ { B } \frac { \rho ^ { * } ( t , { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } d ^ { 3 } x ^ { \prime }
$$

denoting the external piece.

As another example we examine the auxiliary potential $\Phi _ { 2 }$ introduced in Eq. (8.8). Its decomposition is

$$
\Phi _ { 2 } = \Phi _ { 2 , A } + \Phi _ { 2 , \lnot A } ,
$$

with

$$
\Phi _ { 2 , A } = G \int _ { A } { \frac { \rho ^ { * \prime } U ^ { \prime } } { | { \boldsymbol { x } } - { \boldsymbol { x } } ^ { \prime } | } } d ^ { 3 } x ^ { \prime }
$$

and

$$
\Phi _ { 2 , - , \ldots } = \sum _ { B \neq { \cal A } } G \int _ { B } \frac { \rho ^ { * \prime } U ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

But these expressions involve the Newtonian potential, and this should also be decomposed into internal and external pieces. For $\Phi _ { 2 , A }$ we express $U ^ { \prime }$ as in Eq. (9.15) and get

$$
\Phi _ { 2 , A } = G \int _ { A } { \frac { \rho ^ { * \prime } U _ { A } ^ { \prime } } { | { \boldsymbol x } - { \boldsymbol x } ^ { \prime } | } } d ^ { 3 } { \boldsymbol x } ^ { \prime } + G \int _ { A } { \frac { \rho ^ { * \prime } U _ { - A } ^ { \prime } } { | { \boldsymbol x } - { \boldsymbol x } ^ { \prime } | } } d ^ { 3 } { \boldsymbol x } ^ { \prime } .
$$

For $\Phi _ { 2 , \lnot A }$ we must be more careful, because the internal-external decomposition should now refer to each body $B$ instead of body $A$ . In fact, to be fully clear we should refine our decomposition and write $U ^ { \prime } = U _ { A } ^ { \prime } + U _ { B } ^ { \prime } + U _ { \neg A B } ^ { \prime }$ , with $\begin{array} { r } { U _ { \neg A B } ^ { \prime } : = \sum _ { C \neq A , B } \int _ { C } \rho ^ { * \prime \prime } | \pmb { x } ^ { \prime } - } \end{array}$ $\boldsymbol { x } ^ { \prime \prime } | ^ { - 1 } d ^ { 3 } \boldsymbol { x } ^ { \prime \prime }$ now excluding bodies $A$ and $B$ . Then Eq. (9.20) becomes

$$
\Phi _ { 2 , - A } = \sum _ { B \neq A } \Biggl \{ G \int _ { B } \frac { \rho ^ { \ast \prime } U _ { A } ^ { \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } + G \int _ { B } \frac { \rho ^ { \ast \prime } U _ { B } ^ { \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } + G \int _ { B } \frac { \rho ^ { \ast \prime } U _ { - A B } ^ { \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } \Biggr \} .
$$

Subtleties like these arise also in the decomposition of the potential $\Phi _ { 5 }$ ; they are, of course, a consequence of the non-linear nature of the field equations.

# 9.1.6 Total mass-energy

The total mass-energy of body $A$ is $M _ { A } : = m _ { A } + ( \mathcal { T } _ { A } + \Omega _ { A } + E _ { A } ^ { \mathrm { i n t } } ) / c ^ { 2 } + O ( c ^ { - 4 } )$ , or

$$
M _ { A } : = \int _ { A } \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } { \bar { v } } ^ { 2 } - \frac { 1 } { 2 } U _ { A } + \Pi \biggr ) \biggr ] d ^ { 3 } x + O ( c ^ { - 4 } )
$$

in view of Eqs. (9.8) and (9.16). In Sec. 8.4.5 we learned that the total mass-energy $M$ of the entire fluid system is a conserved quantity, $d M / d t = 0$ . The manipulations that led to this conclusion involved the integration of the fluid equations over the volume occupied by the entire fluid. The integrations, however, can be limited to the volume occupied by body $A$ , and it is easy to see that the same manipulations would now reveal that each $M _ { A }$ is conserved when the time dependence of external multipole moments can be ignored:

$$
\frac { d M _ { A } } { d t } = 0 .
$$

The relation between $M$ and the sum $\textstyle \sum _ { A } M _ { A }$ is elucidated below in Sec. 9.3.6; the gravitational interaction between bodies prevents these quantities from being equal to each other.

We shall see below that it is only the combination $M _ { A }$ that appears in the metric of an $N$ - body system; the components $m _ { A }$ , $\mathcal { T } _ { A }$ , $\Omega _ { A }$ , or $E _ { A } ^ { \mathrm { i n t } }$ do not make individual appearances. We shall see also that only $M _ { A }$ appears in the equations of motion. The spacetime of an $N$ -body system therefore depends only on the total mass-energy of each body, and the decomposition of this mass-energy into material mass, kinetic energy, gravitational potential energy, and internal energy is of no consequence; two bodies with vastly different internal compositions but the same mass-energy will produce the same spacetime and move in identical manners. This is a statement of the strong equivalence principle in post-Newtonian theory. (Refer to Sec. 5.1 for a discussion of the weak, strong, and Einstein versions of the principle of equivalence.)

The important physical role of the total mass-energy $M _ { A }$ suggests that we might refine our notion of center-of-mass and adopt

$$
\pmb { R } _ { \cal A } : = \frac { 1 } { M _ { \cal A } } \int _ { \cal A } \rho ^ { \ast } \pmb { x } \bigg [ 1 + \frac { 1 } { c ^ { 2 } } \bigg ( \frac { 1 } { 2 } \bar { v } ^ { 2 } - \frac { 1 } { 2 } U _ { \cal A } + \Pi \bigg ) \bigg ] d ^ { 3 } x + O ( c ^ { - 4 } )
$$

instead of Eq. (9.3) as a proper definition of center-of-mass position. Fortunately, the definitions are equivalent under the symmetry assumption of Eq. (9.7):

$$
\pmb { R } _ { A } = \pmb { r } _ { A } + O ( c ^ { - 4 } ) .
$$

To prove this we insert $\pmb { x } = \pmb { r } _ { A } + \pmb { \bar { x } }$ inside the integral, and see immediately that $\pmb { R } _ { A }$ differs from $r _ { A }$ by the integral

$$
\frac { 1 } { M _ { A } c ^ { 2 } } \int _ { A } \rho ^ { * } \bar { { \bf x } } \bigg ( \frac { 1 } { 2 } \bar { v } ^ { 2 } - \frac { 1 } { 2 } U _ { A } + \Pi \bigg ) d ^ { 3 } \bar { x } .
$$

The first and third terms vanish after integration, because the integrals involve an odd number of internal vectors. The second term also leads to a vanishing integral, because

$$
\int _ { \cal A } \rho ^ { * } { \bar { \bf x } } U _ { \cal A } d ^ { 3 } { \bar { x } } = G \int _ { \cal A } \rho ^ { * } \rho ^ { * \prime } \frac { { \bar { x } } } { | { \bar { x } } - { \bar { x } } ^ { \prime } | } d ^ { 3 } { \bar { x } } ^ { \prime } d ^ { 3 } { \bar { x } }
$$

is odd under a reflection across the center-of-mass. The integral vanishes, and we have established the equality of $\pmb { R } _ { A }$ and $r _ { A }$ . There is no need to modify our definition for the center-of-mass position.

# 9.1.7 Virial identities

In this subsection we derive the virial identities that give rise to the equilibrium conditions of Eqs. (9.10) and (9.11). They are

$$
\begin{array} { l } { { \displaystyle { \frac { 1 } { 2 } \dot { I } _ { ^ { A } } ^ { j k } = \frac { 1 } { 2 } S _ { ^ { A } } ^ { j k } + \int _ { A } \rho ^ { * } \bar { v } ^ { j } \bar { x } ^ { k } d ^ { 3 } \bar { x } , } } } \\ { { \displaystyle { \frac { 1 } { 2 } \ddot { I } _ { ^ A } ^ { j k } = 2 \mathcal { T } _ { _ A } ^ { j k } + \Omega _ { _ A } ^ { j k } + \delta ^ { j k } P _ { _ A } + \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \partial ^ { k ) } U _ { - , 4 } d ^ { 3 } \bar { x } + O ( c ^ { - 2 } ) , } } } \\ { { \displaystyle { \frac { 1 } { 2 } \dddot { I } _ { _ A } ^ { j k } = 4 H _ { _ A } ^ { ( j k ) } - 3 K _ { _ A } ^ { j k } + \delta ^ { j k } \dot { P } _ { _ A } - 2 L _ { _ A } ^ { ( j k ) } + \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \frac { d } { d t } \partial ^ { k ) } U _ { - , 4 } d ^ { 3 } \bar { x } } } } \\ { { \displaystyle ~ + 3 \int _ { A } \rho ^ { * } \bar { v } ^ { ( j } \partial ^ { k ) } U _ { - , 4 } d ^ { 3 } \bar { x } + O ( c ^ { - 2 } ) . } } \end{array}
$$

The identities are generated by repeated differentiation of $\begin{array} { r } { I _ { A } ^ { j k } = \int _ { A } \rho ^ { * } \bar { x } ^ { j } \bar { x } ^ { k } d ^ { 3 } \bar { x } } \end{array}$ with respect to time. Equation (9.28a) follows easily from a first differentiation and the definition of the angular-momentum tensor; when the body is non-spinning and in dynamical equilibrium, the identity reveals that

$$
\int _ { A } \rho ^ { * } { \bar { v } } ^ { j } { \bar { x } } ^ { k } d ^ { 3 } { \bar { x } } = 0 .
$$

Equation (9.28b) features an integral involving the external Newtonian potential in addition to the structure integrals introduced in Eq. (9.9); under the condition of Eq. (9.13) the external term is suppressed by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 } \ll 1$ with respect to $\Omega _ { A } ^ { j k }$ , and it can be neglected. At equilibrium the identity gives rise to Eq. (9.10). And similarly, the external terms can be neglected in Eq. (9.28c), and we recover Eq. (9.11) when the body is in dynamical equilibrium.

We now proceed with the derivation of Eq. (9.28b). Taking two derivatives of the quadrupole-moment tensor produces

$$
\frac { 1 } { 2 } \ddot { I } _ { A } ^ { j k } = \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \bar { a } ^ { k ) } d ^ { 3 } \bar { x } + \int _ { A } \rho ^ { * } \bar { v } ^ { j } \bar { v } ^ { k } d ^ { 3 } \bar { x } ,
$$

where $\bar { a } ^ { k } = d v ^ { k } / d t - a _ { A } ^ { j }$ is the acceleration of a fluid element relative to $a _ { A } ^ { j } : = d v _ { A } ^ { j } / d t$ , the acceleration of the center-of-mass. The second integral is $2 \mathcal { T } _ { A } ^ { j k }$ , and to evaluate the first we substitute the Newtonian version of Euler’s equation, $\rho ^ { * } d v ^ { k } / d t = - \partial _ { k } p + \rho ^ { * } \partial _ { k } U +$ $O ( c ^ { - 2 } )$ . We obtain

$$
\frac { 1 } { 2 } \ddot { I } _ { A } ^ { j k } = 2 \mathcal { T } _ { A } ^ { j k } - \int _ { A } \bar { x } ^ { ( j } \partial ^ { k ) } p d ^ { 3 } \bar { x } + \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \partial ^ { k ) } U d ^ { 3 } \bar { x } + O ( c ^ { - 2 } )
$$

after noting that the terms involving $\pmb { a } _ { A }$ vanish identically. We next integrate the pressure term by parts and decompose the potential term into internal and external pieces; this yields

$$
\frac { 1 } { 2 } \ddot { I } _ { A } ^ { j k } = 2 { \cal T } _ { A } ^ { j k } + \delta ^ { j k } { \cal P } _ { A } + \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \partial ^ { k ) } U _ { A } d ^ { 3 } \bar { x } + \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \partial ^ { k ) } U _ { - A } d ^ { 3 } \bar { x } + { \cal O } ( c ^ { - 2 } ) .
$$

The integral involving $U _ { A }$ is

$$
- G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \frac { \bar { x } ^ { ( j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k ) } } { \vert \bar { x } - \bar { x } ^ { \prime } \vert ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } ,
$$

and by switching the identity of the integration variables we can also write it as

$$
+ G \int _ { A } \rho ^ { * \prime } \rho ^ { * } \frac { \bar { x } ^ { \prime ( j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k ) } } { \vert \bar { \bf x } - \bar { { \bf x } } ^ { \prime } \vert ^ { 3 } } d ^ { 3 } \bar { x } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

or as

$$
- \frac { 1 } { 2 } G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } ,
$$

which we recognize as $\Omega _ { A } ^ { j k }$ . Making the substitution in Eq. (9.32) gives us Eq. (9.28b).

Moving on to Eq. (9.28c), we return to Eq. (9.32) and differentiate it with respect to time. We get

$$
\begin{array} { r } { \frac 1 2 \dddot { I } _ { A } ^ { j k } = 2 \dot { \bar { \gamma } } _ { A } ^ { j k } + \delta ^ { j k } \dot { \bar { P } } _ { A } + \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \frac { d } { d t } \partial ^ { k ) } U _ { A } d ^ { 3 } \bar { x } + \int _ { A } \rho ^ { * } \bar { v } ^ { ( j } \partial ^ { k ) } U _ { A } d ^ { 3 } \bar { x } } \\ { + \displaystyle \int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \frac { d } { d t } \partial ^ { k ) } U _ { - A } d ^ { 3 } \bar { x } + \int _ { A } \rho ^ { * } \bar { v } ^ { ( j } \partial ^ { k ) } U _ { - A } d ^ { 3 } \bar { x } + O ( c ^ { - 2 } ) . } \end{array}
$$

The derivative of the kinetic-energy tensor is $\begin{array} { r } { \dot { \mathcal T } _ { A } ^ { j k } = \int _ { A } \rho ^ { * } \bar { v } ^ { ( j } \bar { a } ^ { k ) } d ^ { 3 } \bar { x } } \end{array}$ , and this becomes

$$
\dot { \mathcal { T } } _ { A } ^ { j k } = - \int _ { \mathcal { A } } \bar { v } ^ { ( j } \partial ^ { k ) } p d ^ { 3 } \bar { x } + \int _ { \mathcal { A } } \rho ^ { \ast } \bar { v } ^ { ( j } \partial ^ { k ) } U _ { A } d ^ { 3 } \bar { x } + \int _ { \mathcal { A } } \rho ^ { \ast } \bar { v } ^ { ( j } \partial ^ { k ) } U _ { - , 4 } d ^ { 3 } \bar { x } + O ( c ^ { - 2 } )
$$

after invoking Euler’s equation and decomposing $U$ into internal and external pieces. The pressure integral is $\hat { L } _ { A } ^ { ( j k ) }$ , and we note that the integral involving $U _ { A }$ also appears in Eq. (9.36); it is given by

$$
- G \int _ { A } \rho ^ { * } \rho ^ { * \prime } { \frac { { \bar { v } } ^ { ( j } ( { \bar { x } } - { \bar { x } } ^ { \prime } ) ^ { k ) } } { | { \bar { x } } - { \bar { x } } ^ { \prime } | ^ { 3 } } } d ^ { 3 } { \bar { x } } ^ { \prime } d ^ { 3 } { \bar { x } } = + G \int _ { A } \rho ^ { * \prime } \rho ^ { * } { \frac { { \bar { v } } ^ { \prime ( j } ( { \bar { x } } - { \bar { x } } ^ { \prime } ) ^ { k ) } } { | { \bar { x } } - { \bar { x } } ^ { \prime } | ^ { 3 } } } d ^ { 3 } { \bar { x } } d ^ { 3 } { \bar { x } } ^ { \prime } ,
$$

which is recognized as $H _ { A } ^ { ( j k ) }$ . We therefore have

$$
\dot { \mathcal { T } } _ { \mathcal { A } } ^ { j k } = H _ { \mathcal { A } } ^ { ( j k ) } - L _ { \mathcal { A } } ^ { ( j k ) } + \int _ { \mathcal { A } } \rho ^ { * } \bar { v } ^ { ( j } \partial ^ { k ) } U _ { - \mathcal { A } } d ^ { 3 } \bar { x } + O ( c ^ { - 2 } ) ,
$$

and this can be inserted within Eq. (9.36).

We next work on the integral involving $d ( \partial ^ { k } U _ { A } ) / d t$ in Eq. (9.36). We have

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \partial ^ { k } U _ { A } = \partial _ { t } \partial ^ { k } U _ { A } + v ^ { n } \partial _ { n } \partial ^ { k } U _ { A } } \\ { \displaystyle \qquad = - G \int _ { A } \rho ^ { \ast \prime } v ^ { \prime n } \partial _ { n ^ { \prime } } \frac { ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } - G \int _ { A } \rho ^ { \ast \prime } v ^ { n } \partial _ { n } \frac { ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } , } \end{array}
$$

and evaluation of the partial derivatives yields

$$
\frac { d } { d t } \partial ^ { k } U _ { A } = - G \int _ { A } \rho ^ { \ast \prime } \frac { ( v - v ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } + 3 G \int _ { A } \rho ^ { \ast \prime } \frac { ( v - v ^ { \prime } ) _ { n } ( x - x ^ { \prime } ) ^ { n } ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 5 } } d ^ { 3 } x ^ { \prime } .
$$

Now

$$
\begin{array} { l } { { \displaystyle \int _ { \mathcal { A } } \rho ^ { * } \bar { x } ^ { j } \frac { d } { d t } \partial ^ { k } U _ { \mathcal { A } } d ^ { 3 } \bar { x } = - G \int _ { \mathcal { A } } \rho ^ { * } \rho ^ { * \prime } \frac { \bar { x } ^ { j } ( \bar { v } - \bar { v } ^ { \prime } ) ^ { k } } { \vert \bar { x } - \bar { x } ^ { \prime } \vert ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } } } \\ { { \displaystyle \qquad + 3 G \int _ { \mathcal { A } } \rho ^ { * } \rho ^ { * \prime } \frac { ( \bar { v } - \bar { v } ^ { \prime } ) _ { n } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { n } \bar { x } ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { \vert \bar { x } - \bar { x } ^ { \prime } \vert ^ { 5 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } , } } \end{array}
$$

and we see that by playing with the identities of the integration variables – our old “switch trick” $\bar { \mathbf { x } }  \bar { \mathbf { x } } ^ { \prime } - \mathrm { w e }$ can bring the first integral to the form of $H _ { A } ^ { k j }$ , while the second integral is recognized as $- K _ { A } ^ { j k }$ . Our final expression is therefore

$$
\int _ { A } \rho ^ { * } \bar { x } ^ { ( j } \frac { d } { d t } \partial ^ { k ) } U _ { A } d ^ { 3 } \bar { x } = H _ { A } ^ { ( j k ) } - 3 K _ { A } ^ { j k } .
$$

Collecting the results displayed in Eqs. (9.36), (9.39), and (9.43), we finally obtain the virial identity of Eq. (9.28c).

# 9.2 Inter-body metric

# 9.2.1 Introduction

The post-Newtonian metric was first written down in Eq. (8.2); it is

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U + \displaystyle \frac { 2 } { c ^ { 4 } } \big ( \Psi - U ^ { 2 } \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \displaystyle \frac { 4 } { c ^ { 3 } } U _ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \bigg ( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U \bigg ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

and the gravitational potentials were expressed in terms of fluid variables in Eqs. (8.4). The Newtonian and vector potentials are

$$
\begin{array} { r } { U = G \displaystyle \int \frac { \rho ^ { * \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ { U ^ { j } = G \displaystyle \int \frac { \rho ^ { * \prime } v ^ { \prime j } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \end{array}
$$

in which $\rho ^ { * \prime }$ and $v ^ { \prime j }$ are respectively the density and velocity field expressed as functions of time $t$ and position $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ . The post-Newtonian potential can be written as

$$
\Psi = 2 \Phi _ { 1 } - \Phi _ { 2 } + \Phi _ { 3 } + 4 \Phi _ { 4 } - \frac { 1 } { 2 } \Phi _ { 5 } - \frac { 1 } { 2 } \Phi _ { 6 } ,
$$

in terms of the auxiliary potentials introduced in Eq. (8.8):

$$
\begin{array} { r l } & { \Phi _ { 1 } = G \int \frac { \rho ^ { \star } v ^ { \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 2 } = G \int \frac { \rho ^ { \star } v ^ { \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 3 } = G \int \frac { \rho ^ { \star } v ^ { \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 4 } = G \int \frac { \rho ^ { \star } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 5 } = G \int \rho ^ { \star } \partial _ { J } \psi _ { \ \ } \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 6 } = G \int \rho ^ { \star } v _ { \gamma } ^ { \prime } \rho _ { \nu } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } . } \end{array}
$$

Our task in this section is to coarse-grain this fluid description and evaluate the potentials for a system of $N$ separated bodies. We shall do this at a fair distance from each body, and exploit the condition $s _ { A } \gg R _ { A }$ of Eq. (9.13); here $s _ { A }$ is the distance to $A$ ’s center-of-mass, and $R _ { A }$ is the body radius, a length scale associated with the volume occupied by body $A$ .

In the course of our calculations we will use all the tricks reviewed in Sec. 9.1, and our results will be expressed in terms of the structure integrals of Eqs. (9.8) and (9.9). To simplify the notation it is convenient to introduce

$$
s _ { \scriptscriptstyle A } : = x - r _ { \scriptscriptstyle A } ( t ) , \qquad s _ { \scriptscriptstyle A } : = | x - r _ { \scriptscriptstyle A } ( t ) | , \qquad n _ { \scriptscriptstyle A } : = \frac { s _ { \scriptscriptstyle A } } { s _ { \scriptscriptstyle A } } ,
$$

as well as

$$
\pmb { r } _ { A B } : = \pmb { r } _ { A } ( t ) - \pmb { r } _ { B } ( t ) , \qquad \pmb { r } _ { A B } : = | \pmb { r } _ { A } ( t ) - \pmb { r } _ { B } ( t ) | , \qquad \pmb { n } _ { A B } : = \frac { \pmb { r } _ { A B } } { \pmb { r } _ { A B } } .
$$

We also need the identities

$$
\begin{array} { c } { { \partial _ { j } s _ { A } = n _ { A } ^ { j } , } } \\ { { \partial _ { j k } s _ { A } = \displaystyle \frac { 1 } { s _ { A } } \big ( \delta ^ { j k } - n _ { A } ^ { j } n _ { A } ^ { k } \big ) , } } \\ { { \partial _ { j k n } s _ { A } = \displaystyle - \frac { 1 } { s _ { A } ^ { 2 } } \big ( \delta ^ { j k } n _ { A } ^ { n } + \delta ^ { j n } n _ { A } ^ { k } + \delta ^ { k n } n _ { A } ^ { j } - 3 n _ { A } ^ { j } n _ { A } ^ { k } n _ { A } ^ { n } \big ) , } } \end{array}
$$

which are established by straightforward computations.

# 9.2.2 Potentials

# Newtonian potential $U$

To evaluate the Newtonian potential we begin with Eq. (9.45a), introduce the sum over bodies, and change the integration variables to the relative position $\bar { \pmb x } ^ { \prime } : = { \pmb x } ^ { \prime } - { \pmb r } _ { A }$ . This gives

$$
U ( t , { \pmb x } ) = \sum _ { A } G \int _ { A } \frac { \rho ^ { * } ( t , { \pmb r } _ { A } + \bar { { \pmb x } } ^ { \prime } ) } { | { \pmb s } _ { A } - \bar { { \pmb x } } ^ { \prime } | } d ^ { 3 } \bar { { \boldsymbol x } } ^ { \prime } ,
$$

where $\pmb { s } _ { A } : = \pmb { x } - \pmb { r } _ { A }$ was introduced in Eq. (9.48). In the next step we invoke the condition $R _ { A } \ll s _ { A }$ and express $| \pmb { s } _ { A } - \pmb { \bar { x } } ^ { \prime } | ^ { - 1 }$ as a Taylor expansion in powers of $\bar { x } ^ { \prime j }$ ,

$$
\frac { 1 } { | s _ { { \scriptscriptstyle A } } - \bar { x } ^ { \prime } | } = \frac { 1 } { s _ { { \scriptscriptstyle A } } } - \bar { x } ^ { \prime j } \partial _ { j } \frac { 1 } { s _ { { \scriptscriptstyle A } } } + \frac { 1 } { 2 } \bar { x } ^ { \prime j } \bar { x } ^ { \prime k } \partial _ { j k } \frac { 1 } { s _ { { \scriptscriptstyle A } } } + \cdot \cdot \cdot .
$$

Substitution within each integral produces

$$
\begin{array} { r l r } {  { \int _ { \mathcal { A } } \frac { \rho ^ { * \prime } } { | s _ { A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } = \frac { 1 } { s _ { A } } \int _ { A } \rho ^ { * \prime } d ^ { 3 } \bar { x } ^ { \prime } - \Big ( \partial _ { j } \frac { 1 } { s _ { A } } \Big ) \int _ { A } \rho ^ { * \prime } \bar { x } ^ { \prime j } d ^ { 3 } \bar { x } ^ { \prime } } } \\ & { } & { + \frac { 1 } { 2 } \Big ( \partial _ { j k } \frac { 1 } { s _ { A } } \Big ) \int _ { A } \rho ^ { * \prime } \bar { x } ^ { \prime j } \bar { x } ^ { \prime j } d ^ { 3 } \bar { x } ^ { \prime } + \cdots . } \end{array}
$$

The first integral gives $m _ { A }$ , the material mass of body $A$ . The second integral vanishes by virtue of the definition of $r _ { A }$ given by Eq. (9.3). The third integral gives $I _ { A } ^ { j k }$ , the quadrupole

moment of the mass distribution. Our expression for $U$ is therefore

$$
U = \sum _ { A } \biggl ( \frac { G m _ { A } } { s _ { A } } + \frac { 1 } { 2 } I _ { A } ^ { j k } \partial _ { j k } \frac { 1 } { s _ { A } } + \cdots \biggr ) ,
$$

and we shall truncate this to

$$
U = \sum _ { A } \frac { G m _ { A } } { s _ { A } } + \cdot \cdot \cdot ,
$$

noting that the quadrupole term is smaller than the monopole term by a factor of order $( R _ { A } / s _ { A } ) ^ { 2 } \ll 1$ . This degree of accuracy is maintained in all following calculations.

$$
\mathsf { V e c t o r p o t e n t i a l U } ^ { j }
$$

The steps involved in evaluation of the vector potential are very similar. We begin with Eq. (9.45b), introduce the sum over bodies, and make the substitutions $\pmb { x } ^ { \prime } = \pmb { r } _ { A } + \pmb { \bar { x } } ^ { \prime }$ and $\pmb { v } ^ { \prime } = \pmb { v } _ { A } + \pmb { \bar { v } } ^ { \prime }$ within the integrals. We get

$$
U ^ { j } = \sum _ { A } \Biggl ( v _ { A } ^ { j } G \int _ { A } { \frac { \rho ^ { * \prime } } { | s _ { A } - { \bar { x } } ^ { \prime } | } } d ^ { 3 } { \bar { x } } ^ { \prime } + G \int _ { A } { \frac { \rho ^ { * \prime } { \bar { v } } ^ { \prime j } } { | s _ { A } - { \bar { x } } ^ { \prime } | } } d ^ { 3 } { \bar { x } } ^ { \prime } \Biggr ) .
$$

The Taylor expansion of $| s _ { A } - \bar { x } ^ { \prime } | ^ { - 1 }$ gives rise to $G m _ { A } v _ { A } ^ { j } / s _ { A } + \cdot \cdot .$ for the first integral, where we again neglect the quadrupole term. For the second integral we have

$$
\begin{array} { l } { { \displaystyle \int _ { \cal A } \frac { \rho ^ { * \prime } \bar { v } ^ { \prime } { } ^ { j } } { | { \bf s } _ { \cal A } - \bar { \bf x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } = \displaystyle \frac { 1 } { s _ { \cal A } } \int _ { \cal A } \rho ^ { * \prime } \bar { v } ^ { \prime } { } ^ { j } d ^ { 3 } \bar { x } ^ { \prime } - \left( \partial _ { \cal k } \frac { 1 } { s _ { \cal A } } \right) \int _ { \cal A } \rho ^ { * \prime } \bar { v } ^ { \prime } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } ^ { \prime } } } \\ { { \displaystyle \qquad + \frac { 1 } { 2 } \Big ( \partial _ { k n } \frac { 1 } { s _ { \cal A } } \Big ) \int _ { \cal A } \rho ^ { * \prime } \bar { v } ^ { \prime } \bar { x } ^ { \prime } \bar { x } ^ { \prime } n d ^ { 3 } \bar { x } ^ { \prime } + \cdot \cdot \cdot . } } \end{array}
$$

The first integral vanishes by virtue of the definition of ${ \pmb v } _ { A }$ given by Eq. (9.4). The second integral is the same one that appears in Eq. (9.29), and it vanishes for non-spinning bodies in equilibrium. And the third integral vanishes for bodies that are reflection-symmetric about the center-of-mass, as was discussed in Sec. 9.1.2. The neglected terms are suppressed by a factor of order $( R _ { A } / s _ { A } ) ^ { 3 }$ relative to the leading term, and we conclude that

$$
U ^ { j } = \sum _ { A } \frac { G m _ { A } v _ { A } ^ { j } } { s _ { A } } + \cdot \cdot \cdot ,
$$

up to neglected terms of fractional order $( R _ { A } / s _ { A } ) ^ { 2 }$ .

# Auxiliary potential $\Phi _ { 1 }$

Following the same steps we obtain

$$
\begin{array} { l } { \Phi _ { 1 } = \displaystyle \sum _ { A } \Biggl ( v _ { A } ^ { 2 } G \int _ { A } \frac { \rho ^ { * \prime } } { | s _ { A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } + 2 v _ { A } ^ { j } G \int _ { A } \frac { \rho ^ { * \prime } \bar { v } _ { j } ^ { \prime } } { | s _ { A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } } \\ { + G \int _ { A } \frac { \rho ^ { * \prime } \bar { v } ^ { \prime 2 } } { | s _ { A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } \Biggr ) } \end{array}
$$

from Eq. (9.47a). The first two terms are handled just as before, and the third integral is

$$
\begin{array} { l } { \displaystyle { \int _ { \cal A } \frac { \rho ^ { * \prime } \bar { v } ^ { \prime 2 } } { | s _ { \cal A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } = \displaystyle \frac { 1 } { s _ { \cal A } } \int _ { \cal A } \rho ^ { * \prime } \bar { v } ^ { \prime 2 } d ^ { 3 } \bar { x } ^ { \prime } - \left( \partial _ { j } \frac { 1 } { s _ { \cal A } } \right) \int _ { \cal A } \rho ^ { * \prime } \bar { v } ^ { \prime 2 } \bar { x } ^ { \prime j } d ^ { 3 } \bar { x } ^ { \prime } } } \\ { \displaystyle { + \frac { 1 } { 2 } \Big ( \partial _ { j k } \frac { 1 } { s _ { \cal A } } \Big ) \int _ { \cal A } \rho ^ { * \prime } \bar { v } ^ { \prime 2 } \bar { x } ^ { \prime j } \bar { x } ^ { \prime k } d ^ { 3 } \bar { x } ^ { \prime } + \cdots . } } \end{array}
$$

The first integral is $2 \mathcal { T } _ { A }$ , the second vanishes for reflection-symmetric bodies, and the third term is suppressed by a factor of order $( R _ { A } / s _ { A } ) ^ { 2 }$ relative to the first. Collecting results, we have obtained

$$
\Phi _ { 1 } = 2 \sum _ { A } \frac { G \mathcal { T } _ { A } } { s _ { A } } + \sum _ { A } \frac { G m _ { A } v _ { A } ^ { 2 } } { s _ { A } } + \cdot \cdot \cdot .
$$

# Auxiliary potential $\Phi _ { 2 }$

This computation requires a little more care, because the Newtonian potential $U ^ { \prime }$ appears inside the Poisson integral that defines $\Phi _ { 2 }$ . Decomposing this as $U _ { A } ^ { \prime } + U _ { \lnot A } ^ { \prime }$ , Eq. (9.47b) becomes

$$
\Phi _ { 2 } = \sum _ { A } G \int _ { A } { \frac { \rho ^ { * } U _ { A } ^ { \prime } } { | { \pmb x } - { \pmb x } ^ { \prime } | } } d ^ { 3 } x ^ { \prime } + \sum _ { A } G \int _ { A } { \frac { \rho ^ { * } U _ { \neg A } ^ { \prime } } { | { \pmb x } - { \pmb x } ^ { \prime } | } } d ^ { 3 } x ^ { \prime } .
$$

In the first group of terms in Eq. (9.62) we insert $\begin{array} { r } { U _ { A } ^ { \prime } = G \int _ { A } \rho ^ { * \prime \prime } | { \bf x } ^ { \prime } - { \bf x } ^ { \prime \prime } | ^ { - 1 } d ^ { 3 } x ^ { \prime \prime } } \end{array}$ , as well as $\pmb { x } ^ { \prime } = \pmb { r } _ { A } + \pmb { \bar { x } } ^ { \prime }$ and $\pmb { x } ^ { \prime \prime } = \pmb { r } _ { A } + \pmb { \bar { x } } ^ { \prime \prime }$ . We obtain a sum of terms of the form

$$
G ^ { 2 } \int _ { A } \frac { \rho ^ { * \prime } \rho ^ { * \prime \prime } } { | \bar { \bar { \mathbf { x } } } ^ { \prime } - \bar { \bar { \mathbf { x } } } ^ { \prime \prime } | | s _ { A } - \bar { \bar { \mathbf { x } } } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } .
$$

We next express $| s _ { A } - \bar { x } ^ { \prime } | ^ { - 1 }$ as a Taylor expansion in powers of $\bar { x } ^ { \prime j }$ . The leading term gives rise to the contribution

$$
\frac { G ^ { 2 } } { s _ { A } } \int _ { A } \int _ { A } \frac { \rho ^ { * \prime } \rho ^ { * \prime \prime } } { | \bar { { \bf x } } ^ { \prime } - \bar { { \bf x } } ^ { \prime \prime } | } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

and we recognize this as $- 2 G \Omega _ { A } / s _ { A }$ . The linear term produces an odd integral that vanishes, and the quadratic term gives rise to a negligible contribution of fractional order $( R _ { A } / s _ { A } ) ^ { 2 }$ . We therefore obtain $\textstyle - 2 \sum _ { A } G \Omega _ { A } / s _ { A }$ for the first group of terms in Eq. (9.62).

In the second group of terms we insert $\begin{array} { r } { U _ { \neg A } ^ { \prime } = \sum _ { B \not = A } G \int _ { B } \rho ^ { * \prime \prime } | { \pmb x } ^ { \prime } - { \pmb x } ^ { \prime \prime } | ^ { - 1 } d ^ { 3 } x ^ { \prime \prime } } \end{array}$ , as well as $\pmb { x } ^ { \prime } = \pmb { r } _ { A } + \pmb { \bar { x } } ^ { \prime }$ and $\pmb { x } ^ { \prime \prime } = \pmb { r } _ { B } + \pmb { \bar { x } } ^ { \prime \prime }$ . We obtain a double sum over bodies $A$ and $B$ of terms of the form

$$
G ^ { 2 } \int _ { A } \int _ { B } \frac { \rho ^ { * \prime } \rho ^ { * \prime \prime } } { | \boldsymbol { r } _ { A B } + \bar { \boldsymbol { x } } ^ { \prime } - \bar { \boldsymbol { x } } ^ { \prime \prime } | | \boldsymbol { s } _ { A } - \bar { \boldsymbol { x } } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } .
$$

To evaluate this we express $| s _ { A } - \bar { x } ^ { \prime } | ^ { - 1 }$ as a Taylor expansion in powers of $\bar { x } ^ { \prime j }$ , and we simultaneously expand $| \pmb { r } _ { A B } + \pmb { \bar { x } } ^ { \prime } - \pmb { \bar { x } } ^ { \prime \prime } | ^ { - 1 }$ in powers of $( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j }$ . Making the substitution, we find that as before, the integral is dominated by the leading term in the expansion, that

the linear terms do not contribute at all, and that the quadratic terms can be neglected. We arrive at the expression $\textstyle \sum _ { A } \sum _ { B \neq A } G ^ { 2 } m _ { A } m _ { B } / ( r _ { A B } s _ { A } )$ for the second group of terms in Eq. (9.62).

Collecting results, we find that our final expression for $\Phi _ { 2 }$ is

$$
\Phi _ { 2 } = - 2 \sum _ { A } { \frac { G \Omega _ { A } } { s _ { A } } } + \sum _ { A } \sum _ { B \neq A } { \frac { G ^ { 2 } m _ { A } m _ { B } } { r _ { A B } s _ { A } } } + \cdot \cdot \cdot .
$$

# Auxiliary potentials $\Phi _ { 3 } , \Phi _ { 4 }$ , and $\Phi _ { 5 }$

The potentials $\Phi _ { 3 }$ and $\Phi _ { 4 }$ are computed exactly as the Newtonian potential $U$ . We immediately obtain

$$
\Phi _ { 3 } = \sum _ { A } { \frac { G E _ { A } ^ { \mathrm { i n t } } } { s _ { A } } } + \cdot \cdot \cdot
$$

and

$$
\Phi _ { 4 } = \sum _ { A } { \frac { G P _ { A } } { s _ { A } } } + \cdot \cdot \cdot
$$

The computation of $\Phi _ { 5 }$ resembles that of $\Phi _ { 2 }$ . We write Eq. (9.47e) in the form

$$
\Phi _ { 5 } = \sum _ { A } G \int _ { A } \rho ^ { \ast \prime } \partial _ { j ^ { \prime } } U _ { A } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } + \sum _ { A } G \int _ { A } \rho ^ { \ast \prime } \partial _ { j ^ { \prime } } U _ { - A } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

and work on each group of terms separately.

The first group is a sum of terms of the form

$$
- G ^ { 2 } \int _ { A } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } ( s _ { A } - \bar { x } ^ { \prime } ) _ { j } } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } | s _ { A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

and to evaluate this we expand $( s _ { A } - \bar { x } ^ { \prime } ) _ { j } / | s _ { A } - \bar { x } ^ { \prime } | = \partial _ { j } | s _ { A } - x ^ { \prime } |$ in powers of $\bar { x } ^ { \prime k }$ . We obtain

$$
\begin{array} { r l r } { \displaystyle \int _ { A } \rho ^ { * \prime } \partial _ { j ^ { \prime } } U _ { A } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | } \ d ^ { 3 } x ^ { \prime } = - G \big ( \partial _ { j } s _ { A } \big ) \int _ { A } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } } & { } & \\ { \displaystyle } & { \qquad + G \big ( \partial _ { j k } s _ { A } \big ) \int _ { A } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } \bar { x } ^ { \prime } k } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } } & { } & \\ { \displaystyle } & { \qquad - G \big ( \partial _ { j k n } s _ { A } \big ) \int _ { A } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } \bar { x } ^ { \prime } k \bar { x } ^ { \prime n } } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } } & { } & \\ { \displaystyle } & { \qquad + \ \cdots } & { \qquad ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { n } } \end{array}
$$

The first and third integrals are odd in the number of internal vectors and therefore vanish. The second integral can be written as

$$
\frac { 1 } { 2 } \int _ { A } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { k } } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

which we recognize as $- \Omega _ { A } ^ { j k } / G$ . The neglected terms are of fractional order $( R _ { A } / s _ { A } ) ^ { 2 }$ , and A we conclude that the first group of terms in Eq. (9.69) equals $\textstyle - \sum _ { A } G \Omega _ { A } ^ { j k } \partial _ { j k } s _ { A }$ .

The second group is a double sum of terms

$$
- G ^ { 2 } \int _ { A } \int _ { B } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { ( r _ { A B } + \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } ( s _ { A } - \bar { x } ^ { \prime } ) _ { j } } { | \bar { r } _ { A B } + \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } | s _ { A } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

and the integrals can be evaluated by expanding the factor multiplying $\rho ^ { * } { } ^ { \prime } \rho ^ { * \prime \prime }$ in a double Taylor series in powers of $( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { k }$ and ${ \bar { x } } ^ { \prime n }$ . Once more the dominant contribution comes from the zeroth-order term, and we find that the second group of terms in Eq. (9.69) can be approximated by $\begin{array} { r l } { \phantom { } } & { { } - \sum _ { A } \sum _ { B \neq A } G ^ { 2 } m _ { A } m _ { B } ( \pmb { r } _ { A B } \cdot \pmb { s } _ { A } ) / ( r _ { A B } ^ { 3 } s _ { A } ) } \end{array}$ .

Collecting results, we have that $\Phi _ { 5 }$ is given by

$$
\Phi _ { 5 } = - \sum _ { A } G \Omega _ { A } ^ { j k } \partial _ { j k } s _ { A } - \sum _ { A } \sum _ { B \ne A } G ^ { 2 } m _ { A } m _ { B } \frac { { \pmb r } _ { A B } \cdot { \pmb s } _ { A } } { r _ { A B } ^ { 3 } s _ { A } } + \cdots ,
$$

or

$$
\Phi _ { 5 } = - \sum _ { A } { \frac { G \Omega _ { A } } { s _ { A } } } + \sum _ { A } G \Omega _ { A } ^ { j k } { \frac { n _ { A j } n _ { A k } } { s _ { A } } } - \sum _ { A } \sum _ { B \neq A } G ^ { 2 } m _ { A } m _ { B } { \frac { { n _ { A B } } \cdot { n _ { A } } } { r _ { A B } ^ { 2 } } } + \cdot \cdot \cdot
$$

after using Eq. (9.50) to evaluate $\partial _ { j k } { s _ { A } }$

# Auxiliary potential $\Phi _ { 6 }$

Equation (9.47f) becomes

$$
\begin{array} { l } { { \Phi _ { 6 } = \displaystyle \sum _ { A } G \biggl [ v _ { A } ^ { j } v _ { A } ^ { k } \int _ { A } \rho ^ { * \prime } \frac { ( s _ { A } - \bar { x } ^ { \prime } ) _ { j } ( s _ { A } - \bar { x } ^ { \prime } ) _ { k } } { | s _ { A } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } } } \\ { { \mathrm { } + 2 v _ { A } ^ { j } \displaystyle \int _ { A } \rho ^ { * \prime } \bar { v } ^ { \prime k } \frac { ( s _ { A } - \bar { x } ^ { \prime } ) _ { j } ( s _ { A } - \bar { x } ^ { \prime } ) _ { k } } { | s _ { A } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } } } \\ { { \mathrm { } + \displaystyle \int _ { A } \rho ^ { * \prime } \bar { v } ^ { \prime j } \bar { v } ^ { \prime k } \frac { ( s _ { A } - \bar { x } ^ { \prime } ) _ { j } ( s _ { A } - \bar { x } ^ { \prime } ) _ { k } } { | s _ { A } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } \biggr ] } } \end{array}
$$

after making the substitutions $\pmb { x } ^ { \prime } = \pmb { r } _ { A } + \pmb { \bar { x } } ^ { \prime }$ and $\pmb { v } ^ { \prime } = \pmb { v } _ { A } + \pmb { \bar { v } } ^ { \prime }$ . In each integral we perform the usual trick of expanding $( s _ { A } - \bar { x } ^ { \prime } ) _ { j } ( s _ { A } - \bar { x } ^ { \prime } ) _ { k } \vert s _ { A } - \bar { x } ^ { \prime } \vert ^ { - 3 }$ in powers of ${ \bar { x } } ^ { \prime n }$ . For the first integral we find that the zeroth-order term gives the dominant contribution, that the linear terms give rise to a vanishing integral, and that the quadratic terms can be neglected. For the second integral we find that the zeroth-order term vanishes (because the integral is odd in the number of internal vectors), that the first-order term vanishes by virtue of the non-spinning condition of Eq. (9.29), and that the second-order term also vanishes (another odd integral). And finally, the third integral is evaluated just as the first, and we retain only the zeroth-order contribution.

The end result is

$$
\Phi _ { 6 } = 2 \sum _ { A } G \mathcal { T } _ { A } ^ { j k } \frac { n _ { A j } n _ { A k } } { s _ { A } } + \sum _ { A } G m _ { A } \frac { ( \pmb { n } _ { A } \cdot \pmb { v } _ { A } ) ^ { 2 } } { s _ { A } } + \cdots .
$$

# Post-Newtonian potential #

Combining Eqs. (9.46), (9.61), (9.66), (9.67), (9.68), (9.75), and (9.77) we arrive at the following expression for the post-Newtonian potential:

$$
\begin{array} { l } { { \Psi = \displaystyle \sum _ { A } \frac { G } { s _ { A } } \bigg ( 4 \mathcal { T } _ { A } + \frac { 5 } { 2 } \Omega _ { A } + E _ { A } ^ { \mathrm { i n } } + \frac { 9 } { 2 } P _ { A } \bigg ) } } \\ { { - \displaystyle \frac { 1 } { 2 } \sum _ { A } \frac { G } { s _ { A } } \Big ( 2 T _ { A } ^ { j k } + \Omega _ { A } ^ { j k } + \delta ^ { j k } P _ { A } \Big ) n _ { A j } n _ { A k } } } \\ { { + \displaystyle \sum _ { A } \frac { G m _ { A } } { s _ { A } } \bigg [ 2 v _ { A } ^ { 2 } - \frac { 1 } { 2 } ( n _ { A } \cdot v _ { A } ) ^ { 2 } \bigg ] } } \\ { { - \displaystyle \sum _ { A } \sum _ { B \ne A } \frac { G ^ { 2 } m _ { A } m _ { B } } { r _ { A B } s _ { A } } \bigg ( 1 - \frac { n _ { A B } \cdot s _ { A } } { 2 r _ { A B } } \bigg ) . } } \end{array}
$$

This can be simplified. We note first that the second group of terms, involving the structure tensors $\mathcal { T } _ { A } ^ { j k } , \Omega _ { A } ^ { j \bar { k } }$ , and $\delta ^ { j k } P _ { A }$ , vanishes by virtue of the equilibrium condition of Eq. (9.10). On the other hand, according to Eq. (9.12) the first group of terms can be altered at will by the insertion of any multiple of $2 \mathcal { T } _ { A } + \Omega _ { A } + 3 P _ { A } = 0$ ; we exploit this freedom to eliminate the $P _ { A }$ term in the first sum. And finally, we use the identity

$$
{ \pmb { n } } _ { A B } \cdot { \boldsymbol { s } } _ { A } = \frac { s _ { B } ^ { 2 } - s _ { A } ^ { 2 } - r _ { A B } ^ { 2 } } { 2 r _ { A B } }
$$

to alter the appearance of the double sum.

After implementing these changes, our final expression for $\Psi$ is

$$
\begin{array} { l } { \displaystyle \Psi = \sum _ { A } \frac { G } { s _ { A } } \Big ( \mathcal { T } _ { A } + \Omega _ { A } + E _ { A } ^ { \mathrm { i n t } } \Big ) + \sum _ { A } \frac { G m _ { A } } { s _ { A } } \bigg [ 2 v _ { A } ^ { 2 } - \frac { 1 } { 2 } \big ( \pmb { n } _ { A } \cdot \pmb { v } _ { A } \big ) ^ { 2 } \bigg ] } \\ { \displaystyle - \sum _ { A } \sum _ { B \neq A } \frac { G ^ { 2 } m _ { A } m _ { B } } { r _ { A B } s _ { A } } \frac { 5 r _ { A B } ^ { 2 } + s _ { A } ^ { 2 } - s _ { B } ^ { 2 } } { 4 r _ { A B } ^ { 2 } } . } \end{array}
$$

Note that the first sum, which features the only remaining terms that involve the structure integrals, depends on the combination $E _ { A } : = T _ { A } + \Omega _ { A } + E _ { A } ^ { \mathrm { i n t } }$ ; this is the total energy of body $A$ , the sum of kinetic, gravitational, and internal energies.

# 9.2.3 At long last, the metric

We insert Eq. (9.55), (9.58), and (9.80) within the post-Newtonian metric of Eqs. (9.44). The first group of terms in the post-Newtonian potential $\Psi$ combines with the Newtonian potential $U$ , and the combination gives rise to a contribution

$$
{ \frac { 2 } { c ^ { 2 } } } \sum _ { A } { \frac { G ( m _ { A } + E _ { A } / c ^ { 2 } ) } { s _ { A } } }
$$

to $g _ { 0 0 }$ . This result implies that the Newtonian piece of the metric is naturally expressed in terms of $M _ { A } : = m _ { A } + E _ { A } / c ^ { 2 }$ , the total mass-energy of each body, as defined by Eq. (9.23). Furthermore, the post-Newtonian terms also can be expressed in terms of $M _ { A }$ , because the difference between this and $m _ { A }$ is of order $c ^ { - 2 }$ and can be transferred to the (neglected) 2pn terms. The conclusion is that the metric involves $M _ { A }$ only, and is completely insensitive to its decomposition in terms of material mass $m _ { A }$ , kinetic energy $\mathcal { T } _ { A }$ , gravitational potential energy $\Omega _ { A }$ , and internal energy $E _ { A } ^ { \mathrm { i n t } }$ . This conclusion was anticipated in Sec. 9.1.6: the 1pn metric does indeed satisfy the strong formulation of the principle of equivalence.

Our final expression for the metric is

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } \sum _ { { \lambda } } \frac { G M _ { { \lambda } } } { s _ { { \lambda } } } + \frac { 1 } { c ^ { 4 } } \sum _ { { \lambda } } \frac { G M _ { { \lambda } } } { s _ { { \lambda } } } \biggl [ 4 v _ { { \lambda } } ^ { 2 } - ( n _ { { \lambda } } \cdot v _ { { \lambda } } ) ^ { 2 } - 2 \frac { G M _ { { \lambda } } } { s _ { { \lambda } } } \biggr ] } } \\ { ~ - \frac { 1 } { c ^ { 4 } } \sum _ { { \lambda } } \sum _ { { \delta } \neq { \lambda } } \frac { G ^ { 2 } M _ { { \lambda } } M _ { { \lambda } } } { s _ { { \lambda } } } \biggl ( \frac { 2 } { s _ { { \lambda } } } + \frac { 5 } { 2 r _ { A B } } + \frac { s _ { { \lambda } } ^ { 2 } - s _ { B } ^ { 2 } } { 2 r _ { A B } ^ { 3 } } \biggr ) + { \cal O } ( c ^ { - 6 } ) , }  \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } \sum _ { { \lambda } } \frac { G M _ { { \lambda } } v _ { { \lambda } } ^ { j } } { s _ { { \lambda } } } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \biggl ( 1 + \frac { 2 } { c ^ { 2 } } \sum _ { { \lambda } } \frac { G M _ { { \lambda } } } { s _ { { \lambda } } } \biggr ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

We recall the notation

$$
\pmb { s } _ { { \scriptscriptstyle A } } : = \pmb { x } - \pmb { r } _ { { \scriptscriptstyle A } } ( t ) , \qquad \pmb { s } _ { { \scriptscriptstyle A } } : = \vert \pmb { x } - \pmb { r } _ { { \scriptscriptstyle A } } ( t ) \vert , \qquad \pmb { n } _ { { \scriptscriptstyle A } } : = \frac { \pmb { s } _ { { \scriptscriptstyle A } } } { \pmb { s } _ { { \scriptscriptstyle A } } } ,
$$

as well as

$$
r _ { A B } : = | \pmb { r } _ { A } ( t ) - \pmb { r } _ { B } ( t ) | .
$$

And we recall that the mass-energy parameter $M _ { A }$ was introduced in Eq. (9.23):

$$
M _ { \cal A } : = \int _ { \cal A } \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } { \bar { v } } ^ { 2 } - \frac { 1 } { 2 } U _ { \cal A } + \Pi \biggr ) \biggr ] d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) ,
$$

where $\pmb { \bar { v } } : = \pmb { v } - \pmb { v } _ { A }$ is the velocity field in the comoving frame of body $A$ , and $U _ { A }$ is the internal gravitational potential. The mass-energy $M _ { A }$ is a constant of the post-Newtonian motion.

The metric of Eqs. (9.81) is valid outside each body, at a distance $s _ { A }$ that is much larger than each body radius $R _ { A }$ . Only the leading terms are displayed, and our expressions leave out terms that are suppressed by factors of order $( R _ { A } / s _ { A } ) ^ { 2 } \ll 1$ . They also leave out terms that are contributed by the spin of each body, which was assumed to vanish; these will be incorporated in Sec. 9.5. The metric is expressed in terms of the center-of-mass position $\pmb { r } _ { A } ( t )$ and velocity ${ \pmb v } _ { A } ( t ) = d { \pmb r } _ { A } / d t$ of each body. These have not yet been determined, and this shall be our task in the following section.

# 9.3 Motion of isolated bodies

# 9.3.1 Strategy

To find equations of motion for the center-of-mass positions $\pmb { r } _ { A } ( t )$ , we return to Eq. (9.5), which we copy as

$$
m _ { A } \pmb { a } _ { A } = \int _ { A } \rho ^ { * } \frac { d \pmb { v } } { d t } d ^ { 3 } \pmb { x } .
$$

Here $\begin{array} { r } { m _ { A } : = \int _ { A } \rho ^ { \ast } d ^ { 3 } x } \end{array}$ is the material mass of body $A$ , $\pmb { a } _ { A } : = d ^ { 2 } \pmb { r } _ { A } / d t ^ { 2 }$ is the coordinate acceleration of its center-of-mass, and $\pmb { v }$ is the fluid’s velocity field. The domain of integration $V _ { A }$ is a time-independent region of three-dimensional space that extends beyond the volume occupied by the body. As stated previously, it is sufficiently large that in a time interval $d t$ , the body will not cross the domain’s boundary $S _ { A }$ ; but it is sufficiently small that $V _ { A }$ does not include nor intersect another body within the system.

In this equation we insert the post-Newtonian Euler equation (8.119), which is derived in Sec. 8.4.3. Taking into account Eq. (8.12), this gives rise to

$$
m _ { A } a _ { A } ^ { j } = F _ { 0 } ^ { j } + \sum _ { n = 1 } ^ { 1 8 } F _ { n } ^ { j } + O ( c ^ { - 4 } ) ,
$$

where

$$
F _ { 0 } ^ { j } : = \int _ { A } \left( - \partial _ { j } p + \rho ^ { * } \partial _ { j } U \right) d ^ { 3 } x
$$

is the Newtonian contribution to the force acting on body $A$ , while the eighteen terms that make up the post-Newtonian contribution are

$$
\begin{array} { r l } & { F _ { 1 } ^ { \prime } = \frac { 1 } { 2 \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } \beta ^ { 2 } \lambda _ { x } } , } \\ & { F _ { 2 } ^ { \prime } = - \frac { 1 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } \beta ^ { 2 } \lambda _ { x } } , } \\ & { F _ { 3 } ^ { \prime } = \frac { 1 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } \beta ^ { 2 } \lambda _ { y } } } \\ & { F _ { 4 } ^ { \prime } = - \frac { 1 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } \beta ^ { 2 } \lambda _ { y } } d y ^ { \prime } \varepsilon ^ { \prime } , } \\ & { F _ { 5 } ^ { \prime } = - \frac { 1 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } \beta ^ { 2 } \lambda _ { y } } d y ^ { \prime } \varepsilon ^ { \prime } , } \\ & { F _ { 6 } ^ { \prime } = - \frac { 1 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } ^ { 2 } \lambda _ { y } } d y ^ { \prime } \varepsilon ^ { \prime } , } \\ & { F _ { 7 } ^ { \prime } = - \frac { 4 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } ^ { 2 } \lambda _ { y } } d y ^ { \prime } \varepsilon ^ { \prime } , } \\ & { F _ { 9 } ^ { \prime } = - \frac { 4 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } ^ { 2 } \lambda _ { y } } d y ^ { \prime } \varepsilon ^ { \prime } d \lambda _ { x } ^ { \prime } , } \\ & { F _ { 9 } ^ { \prime } = - \frac { 3 } { \alpha ^ { 2 } } \int _ { \varepsilon } ^ { \varepsilon ^ { \prime } \partial _ { \beta } ^ { 2 } \lambda _ { y } } d y ^ { \prime } \varepsilon ^ { \prime } . } \end{array}
$$

(continued overleaf)

$$
\begin{array} { r l } & { E _ { \mu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \mu \nu } d x _ { \mu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \mu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = e ^ { \lambda _ { 2 } ^ { 2 } } \int _ { x } ^ { x } \hat { \sigma } ^ { \mu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = e ^ { \lambda _ { 2 } ^ { 2 } } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ & { F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d x _ { \nu } ^ { \nu } } \\ &  F _ { \nu } ^ { ( k ) } = - \frac { \lambda _ { 2 } ^ { 2 } } { \mu } \int _ { x } ^ { x } \hat { \sigma } ^ { \nu \nu } d \end{array}
$$

The auxiliary potentials $\Phi _ { n }$ were introduced in Eqs. (8.8).

To evaluate the force integrals we rely on the techniques introduced in Sec. 9.1. We assume that each body is reflection-symmetric about the center-of-mass (Sec. 9.1.2), so that each variable (such as $\rho ^ { * } , p$ , and $\Pi$ ) that specifies its internal structure can be taken to be invariant under the reflection $\bar { x } \to - \bar { x }$ , where $\bar { \pmb { x } } : = \pmb { x } - \pmb { r } _ { A } ( t )$ is the position of a fluid element relative to the center-of-mass; this property allows us to eliminate all body integrals that contain an odd number of internal vectors (such as $\bar { x }$ , $\pmb { \bar { v } } : = \pmb { v } - \pmb { v } _ { A }$ , or $\nabla p$ ). We express our results in terms of the structure integrals introduced in Sec. 9.1.3, and assume that the bodies are in dynamical equilibrium, so that Eqs. (9.10), (9.11), and (9.12) are satisfied. We continue to assume that each body is non-spinning (Sec. 9.1.4), so that its angular-momentum tensor $S _ { A } ^ { j k }$ vanishes. We rely on the decomposition of all gravitational potentials into internal and external pieces, as explained in Sec. 9.1.5. And finally, we assume that the bodies are well separated (Sec. 9.1.4) and allow ourselves to neglect terms that are suppressed by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 }$ relative to the leading-order contribution to each force integral; here $R _ { A }$ is the typical body radius and $r _ { A B } : = | \pmb { r } _ { A } - \pmb { r } _ { B } |$ the typical inter-body distance.

We exploit the condition $R _ { A } \ll r _ { A B }$ to simplify expressions involving the external potentials. The wide separation between bodies implies that when (say) the external potential $U _ { \neg A }$ is evaluated within body $A$ , it can be usefully expressed as the Taylor expansion

$$
U _ { \neg { A } } ( t , { \pmb x } ) = U _ { \neg { A } } ( t , { \pmb r } _ { A } ) + \bar { x } ^ { j } \partial _ { j } U _ { \neg { A } } ( t , { \pmb r } _ { A } ) + \frac 1 2 \bar { x } ^ { j } \bar { x } ^ { k } \partial _ { j k } U _ { \neg { A } } ( t , { \pmb r } _ { A } ) + \cdots ,
$$

where $\bar { \pmb { x } } : = \pmb { x } - \pmb { r } _ { A }$ . With respect to the leading term $U _ { \neg A } ( t , \pmb { r } _ { A } )$ , the linear term in Eq. (9.89) is suppressed by a factor of order $R _ { A } / r _ { A B }$ , while the quadratic term is smaller by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 }$ ; according to the rules spelled out previously, this last term can be discarded.

# 9.3.2 Results and sample computations

It would be exhausting (both for the reader and the authors) to present a detailed calculation of each one of the nineteen force integrals $F _ { n } ^ { j }$ . We shall instead state the results, and present a small (but representative) sample of the calculations that are required to obtain these results.

The individual contributions to the gravitational force are

$$
F _ { 0 } ^ { j } = m _ { A } \partial _ { j } U _ { \neg A } ( t , \pmb { r } _ { A } )
$$

and

$$
\begin{array} { r l } & { \mathcal { L } ^ { \mathcal { L } ^ { L } } ( \gamma ) = \frac { \partial \xi _ { 1 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 1 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - 2 \frac { \partial \xi _ { 1 } ^ { L } } { \partial \tau ^ { L } } , \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 1 } ^ { L } } { \partial \tau ^ { L } } , \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - 2 \frac { \partial \xi _ { 1 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - 3 \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 2 } ^ { L } } { \partial \tau ^ { L } } , } \\ & { \mathcal { L } ^ { \mathcal { L } } ( \gamma ) = - \frac { \partial \xi _ { 1 } ^ { L } } { \partial \tau ^ { L } } , } \\ &  \mathcal { L } ^ { \mathcal { L } } ( \ \end{array}
$$

Here $U _ { \neg A }$ is a shorthand notation for $U _ { \neg A } ( t , \pmb { x } = \pmb { r } _ { A } )$ , with the rule extending to all other external potentials. These are differentiated with respect to $t$ and $x ^ { j }$ before being evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ .

To illustrate the method of derivation we begin with the simplest case, the result of Eq. (9.90), which is obtained from Eq. (9.87); these calculations were also presented back in Sec. 1.6. The integral of $\partial _ { j } p$ over the three-dimensional domain $V _ { A }$ can be expressed as the surface integral $\oint _ { S _ { A } } p d S _ { j }$ , and this vanishes because the boundary surface $S _ { A }$ lies outside of body $A$ . The integral of $\partial _ { j } U$ is handled by decomposing the Newtonian potential as $U = U _ { A } + U _ { \lnot A }$ . The first contribution to $F _ { 0 } ^ { j }$ is the self-interaction term $\int _ { A } \rho ^ { * } \partial _ { j } U _ { A } d ^ { 3 } x$ , which vanishes; this is the statement of Eq. (8.120a), adapted to the current situation in which the integration extends over the volume occupied by body $A$ . The sole contribution to the Newtonian force is therefore $\begin{array} { r } { F _ { 0 } ^ { j } = \int _ { A } \rho ^ { * } \partial _ { j } U _ { \lnot A } d ^ { 3 } x } \end{array}$ . In this we insert the Taylor expansion of Eq. (9.89). The first term gives rise to Eq. (9.90). The second term vanishes, because $\begin{array} { r } { \int _ { A } \rho ^ { * } \bar { x } ^ { j } d ^ { 3 } x = 0 } \end{array}$ by virtue of the definition of the center-of-mass position $r _ { A }$ . The third term gives rise to a contribution $\scriptstyle { \frac { 1 } { 2 } } I _ { A } ^ { k n } \partial _ { j k n } U _ { \lnot A } ( t , \pmb { r } _ { A } )$ to the Newtonian force, and this is smaller than the leading term by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 }$ ; we discard this as well as all higher-order terms. Our final result is Eq. (9.90).

We next examine a more complicated example, the computation of $F _ { 6 } ^ { j }$ . Here again we write $U = U _ { A } + U _ { \lnot A }$ , and in addition we express the velocity field $\pmb { v }$ as ${ \pmb v } _ { A } + \bar { \pmb v }$ . This gives rise to a sum of six terms,

$$
\begin{array} { l } { { \displaystyle c ^ { 2 } F _ { 6 } ^ { j } = v _ { A } ^ { 2 } \int _ { A } \rho ^ { * } \partial _ { j } U _ { A } d ^ { 3 } x + 2 v _ { A } ^ { k } \int _ { A } \rho ^ { * } \bar { v } _ { k } \partial _ { j } U _ { A } d ^ { 3 } x + \int _ { A } \rho ^ { * } \bar { v } ^ { 2 } \partial _ { j } U _ { A } d ^ { 3 } x } } \\ { { \displaystyle \qquad + v _ { A } ^ { 2 } \int _ { A } \rho ^ { * } \partial _ { j } U _ { - A } d ^ { 3 } x + 2 v _ { A } ^ { k } \int _ { A } \rho ^ { * } \bar { v } _ { k } \partial _ { j } U _ { - A } d ^ { 3 } x + \int _ { A } \rho ^ { * } \bar { v } ^ { 2 } \partial _ { j } U _ { - A } d ^ { 3 } x . } } \end{array}
$$

The first integral vanishes, as was observed previously. In the second integral we insert $\begin{array} { r } { U _ { A } = G \int _ { A } \rho ^ { * \prime } | { \pmb x } - { \pmb x } ^ { \prime } | ^ { - 1 } d ^ { 3 } x ^ { \prime } } \end{array}$ which we differentiate with respect to $x ^ { j }$ . The result is

$$
- G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \bar { v } _ { k } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { \vert \bar { x } - \bar { x } ^ { \prime } \vert ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x }
$$

after changing the variables of integration from $_ x$ and $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ to $\pmb { \bar { x } } : = \pmb { x } - \pmb { r } _ { A }$ and $\bar { \pmb x } ^ { \prime } : = { \pmb x } ^ { \prime } - { \pmb r } _ { A }$ This can be written as

$$
+ G \int _ { A } \rho ^ { * \prime } \rho ^ { * } { \bar { v } _ { k } ^ { \prime } } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { \vert \bar { x } - \bar { x } ^ { \prime } \vert ^ { 3 } } d ^ { 3 } \bar { x } d ^ { 3 } \bar { x } ^ { \prime }
$$

by switching the identities of the integration variables (the old “switch trick”). This is recognized as the structure integral $H _ { A } ^ { k j }$ , and the second contribution to $c ^ { 2 } F _ { A } ^ { j }$ is $2 H _ { A } ^ { k j } v _ { A } ^ { k }$ . The third integral vanishes, because it contains an odd number of internal vectors $\bar { x } , \bar { x } ^ { \prime }$ , and $\bar { \pmb { v } }$ . In the fourth integral we insert the Taylor expansion of the external potential and retain the leading term only; the fourth contribution to $c ^ { 2 } F _ { 6 } ^ { j }$ is $m _ { A } v _ { A } ^ { 2 } \partial _ { j } U _ { \lnot A } ( t , \pmb { r } _ { A } )$ , plus terms that are smaller than this by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 }$ . In the fifth integral the Taylor expansion gives rise to a leading term proportional to $\int _ { A } \rho ^ { * } \bar { v } _ { k } d ^ { 3 } \bar { x }$ , which vanishes by virtue of Eq. (9.4). The second term is proportional to $\textstyle \int _ { A } \rho ^ { * } { \bar { v } } _ { k } { \bar { x } } ^ { n } d ^ { 3 } { \bar { x } }$ , which vanishes by virtue of Eq. (9.29). We neglect the third term and conclude that the fifth contribution to $c ^ { 2 } F _ { 6 } ^ { j }$ is negligible. And finally, the sixth integral produces the final contribution $2 \mathcal { T } _ { A } \partial _ { j } U _ { \neg A } ( t , \pmb { r } _ { A } )$ to $c ^ { 2 } F _ { 6 } ^ { j }$ . Collecting results, we obtain the expression displayed in Eq. (9.91f).

As our final example we go through the computations that lead to Eq. (9.91n). After decomposing $\Phi _ { 2 }$ into internal and external pieces, we have that

$$
c ^ { 2 } F _ { 1 4 } ^ { j } = - \int _ { A } \rho ^ { * } \partial _ { j } \Phi _ { 2 , A } d ^ { 3 } x - \int _ { A } \rho ^ { * } \partial _ { j } \Phi _ { 2 , - A } d ^ { 3 } x .
$$

In the second integral we substitute the Taylor expansion for $\Phi _ { 2 , \lnot A }$ , and this gives rise to a contribution $- m _ { A } \partial _ { j } \Phi _ { 2 , - A } ( t , \pmb { r } _ { A } )$ to $c ^ { 2 } F _ { 1 4 } ^ { j }$ . Working now on the first integral, we invoke the definition of $\Phi _ { 2 }$ from Eqs. (8.8) on page 374, decompose $U ^ { \prime }$ into internal and external pieces, and write

$$
\partial _ { j } \Phi _ { 2 , A } = - G \int _ { A } \rho ^ { * \prime } U _ { A } ^ { \prime } { \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | ^ { 3 } } } d ^ { 3 } x ^ { \prime } - G \int _ { A } \rho ^ { * \prime } U _ { - A } ^ { \prime } { \frac { ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | ^ { 3 } } } d ^ { 3 } x ^ { \prime } .
$$

Making the substitution, we find that the first term produces a contribution

$$
G \int _ { A } \rho ^ { * } \rho ^ { * \prime } U _ { A } ^ { \prime } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x }
$$

to $c ^ { 2 } F _ { 1 4 } ^ { j }$ ; this integral vanishes because it contains an odd number of internal vectors. The second term produces

$$
G \int _ { A } \rho ^ { * } \rho ^ { * \prime } U _ { \neg A } ^ { \prime } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } ,
$$

and in this we substitute the Taylor expansion for the external Newtonian potential. The leading term gives rise to an odd integral, and the next term produces a contribution

$$
\partial _ { k } U _ { \neg { A } } ( t , \boldsymbol { r } _ { A } ) G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \frac { \bar { x } ^ { \prime k } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x }
$$

to $c ^ { 2 } F _ { 1 4 } ^ { j }$ . By making use of the switch trick we re-express this as

$$
- \partial _ { k } U _ { - A } ( t , \pmb { r } _ { A } ) G \int _ { A } \rho ^ { * \prime } \rho ^ { * } \frac { \bar { x } ^ { k } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

and averaging the results produces the final expression

$$
- \frac { 1 } { 2 } \partial _ { k } U _ { \neg { A } } ( t , \boldsymbol { r } _ { A } ) G \int _ { \cal A } \rho ^ { * } \rho ^ { * \prime } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } ;
$$

this is equal to $\Omega _ { A } ^ { j k } \partial _ { k } U _ { \neg A } ( t , \pmb { r } _ { A } )$ . The higher-order terms in the Taylor expansion can be neglected, and collecting results, we have established Eq. (9.91n).

# 9.3.3 Equations of motion (in terms of external potentials)

Substitution of Eqs. (9.90) and (9.91) into Eq. (9.86) returns

$$
\begin{array} { c } { { \displaystyle { a _ { \cal A } ^ { j } = \frac { 1 } { m _ { \cal A } c ^ { 2 } } \biggl [ \bigl ( 2 { \cal L } _ { \cal A } ^ { ( j k ) } - 4 { \cal H } _ { \cal A } ^ { ( j k ) } + 3 { \cal K } _ { \cal A } ^ { j k } - \delta ^ { j k } { \dot { { \cal F } } } _ { \cal A } \bigr ) v _ { \cal A } ^ { k } } } } \\ { { - 4 \bigl ( 2 { \cal T } _ { \cal A } ^ { j k } + \Omega _ { \cal A } ^ { j k } + \delta ^ { j k } { \cal P } _ { \cal A } \bigr ) \partial _ { k } U _ { - \cal A } + \bigl ( 2 { \cal T } _ { \cal A } + \Omega _ { \cal A } + 3 { \cal P } _ { \cal A } \bigr ) \partial _ { j } U _ { - \cal A } \biggr ] } } \\ { { + \partial _ { j } U _ { - \cal A } + \frac { 1 } { c ^ { 2 } } \biggl [ \bigl ( v _ { \cal A } ^ { 2 } - 4 U _ { - \cal A } \bigr ) \partial _ { j } U _ { - \cal A } - v _ { \cal A } ^ { j } \bigl ( 4 v _ { \cal A } ^ { k } \partial _ { k } U _ { - \cal A } + 3 \partial _ { t } U _ { - \cal A } \bigr ) } } \\ { { - 4 v _ { \cal A } ^ { k } \bigl ( \partial _ { j } U _ { - \cal A } ^ { k } - \partial _ { k } U _ { - \cal A } ^ { j } \bigr ) + 4 \partial _ { t } U _ { - \cal A } ^ { j } + \partial _ { j } \Psi _ { - \cal A } \biggr ] + { \cal O } ( c ^ { - 4 } ) } } \end{array}
$$

after some algebra and simplification. The self-interaction terms can all be eliminated by taking into account the equilibrium conditions of Eqs. (9.10), (9.11), and (9.12), as well as setting ${ \dot { P } } _ { A } = 0$ . The equations of motion for body $A$ reduce to

$$
\begin{array} { c } { { \displaystyle { a _ { \cal A } ^ { j } = \partial _ { j } U _ { - \cal A } + \frac { 1 } { c ^ { 2 } } \bigg [ \big ( v _ { \cal A } ^ { 2 } - 4 U _ { - \cal A } \big ) \partial _ { j } U _ { - \cal A } - v _ { \cal A } ^ { j } \big ( 4 v _ { \cal A } ^ { k } \partial _ { k } U _ { - \cal A } + 3 \partial _ { t } U _ { - \cal A } \big ) } } } \\ { { - 4 v _ { \cal A } ^ { k } \big ( \partial _ { j } U _ { - \cal A } ^ { k } - \partial _ { k } U _ { - \cal A } ^ { j } \big ) + 4 \partial _ { t } U _ { - \cal A } ^ { j } + \partial _ { j } \Psi _ { - \cal A } \bigg ] + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

The acceleration vector is currently expressed in terms of the external piece of the Newtonian potential $U$ , the vector potential $U ^ { j }$ , and the post-Newtonian potential $\Psi$ ; these are evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A } ( t )$ after differentiation. The external post-Newtonian potential is given by

$$
\Psi _ { \neg A } = 2 \Phi _ { 1 , \ - \ - \mathcal { A } } - \Phi _ { 2 , \ - \not { \ l } , \ + } + \Phi _ { 3 , \ - \ - \mathcal { A } } + 4 \Phi _ { 4 , \ -  \mathcal { A } } - \frac { 1 } { 2 } \Phi _ { 5 , \ -  \mathcal { A } } - \frac { 1 } { 2 } \Phi _ { 6 , \ -  \mathcal { A } }
$$

in terms of the auxiliary external potentials $\Phi _ { n , \lnot A }$ . Our next task is to evaluate the external potentials, and find their expressions as explicit functions of the positions $r _ { A }$ and velocities ${ \pmb v } _ { A }$ .

Before we proceed it is interesting to compare Eq. (9.101), which governs the motion of body $A$ among a system of $N$ gravitating bodies, with the geodesic equation (8.16), which determines the motion of a test mass in a pre-determined spacetime with gravitational potentials $U , U ^ { j }$ , and $\Psi$ . The equations are formally identical, and this allows us to conclude that body $A$ moves as if it were on a geodesic in a spacetime with gravitational potentials $U _ { \neg A }$ , $U _ { \neg A } ^ { j }$ , and $\Psi _ { \neg A }$ . This conclusion rests on our assumptions that each body is non-spinning and well separated from any other body, so that the effects of the higherorder multipole moments (such as the quadrupole moment $I _ { A } ^ { j k }$ and the angular-momentum tensor $S _ { A } ^ { j k }$ ) can be neglected in the equations of motion; inclusion of these effects would produce deviations from geodesic motion. The conclusion must also be formulated with care, because the external potentials are not truly independent of body $A$ ; as we shall see, the non-linear nature of the field equations implies that $\partial _ { t } U _ { \neg A } ^ { j }$ and $\partial _ { j } \Phi _ { 2 , \lnot A }$ depend on $m _ { A }$ in addition to all other, external masses.

# 9.3.4 Evaluation of the external potentials

Once again we shall state our results and go through the details of only a small subset of computations. After evaluation at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A } ( t )$ we find that the derivatives of the external potentials are given by

$$
\begin{array} { l } { { \displaystyle \partial _ { j } U _ { - \boldsymbol { A } } = - \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } } \frac { G m _ { \boldsymbol { \beta } } n _ { \boldsymbol { A } } ^ { \boldsymbol { A } } \mu _ { \boldsymbol { A } } } { r _ { \boldsymbol { A } \boldsymbol { A } } ^ { 2 } } , } } \\ { { \ } } \\ { { \displaystyle \partial _ { i } U _ { - \boldsymbol { A } } = \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } } \frac { G m _ { \boldsymbol { \beta } } ( n _ { \boldsymbol { A } } \cdot \boldsymbol { \nu } _ { \boldsymbol { B } } ) } { r _ { \boldsymbol { A } } ^ { 2 } } , } } \\ { { \ } } \\ { { \displaystyle \partial _ { i } U _ { - \boldsymbol { A } } ^ { j } = - \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } } \frac { G m _ { \boldsymbol { \beta } } n _ { \boldsymbol { A } } ^ { \boldsymbol { B } } \mu _ { \boldsymbol { A } } ^ { \boldsymbol { A } } } { r _ { \boldsymbol { A } \boldsymbol { B } } ^ { 2 } } , } } \\ { { \ } } \\ { { \displaystyle \partial _ { i } U _ { - \boldsymbol { A } } ^ { j } = \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } } ( ( \mathcal { T } _ { \boldsymbol { B } } ^ { j k } + \mathcal { D } _ { \boldsymbol { B } } ^ { j k } + \delta ^ { j k } P _ { \boldsymbol { A } } ) \frac { n _ { \boldsymbol { A } } ^ { \boldsymbol { A } } \mu } { r _ { \boldsymbol { A } \boldsymbol { B } } ^ { 2 } } + \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } } \frac { G m _ { \boldsymbol { \beta } } ( n _ { \boldsymbol { A } } \cdot \boldsymbol { \nu } _ { \boldsymbol { B } } ) \nu _ { \boldsymbol { B } } ^ { j } } { r _ { \boldsymbol { A } \boldsymbol { B } } ^ { 2 } }  } } \\ { { \ } } \\   \displaystyle  + \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } } \frac { G ^ { 2 } m _ { \boldsymbol { A } } m _ { \boldsymbol { B } } n _ { \boldsymbol { A } } ^ { \boldsymbol { A } } \mu _ { \boldsymbol { B } } } { r _ { \boldsymbol { A } \boldsymbol { B } } ^ { 2 } } - \sum _ { \boldsymbol { \beta } \neq \boldsymbol { A } \in \mathcal { A } _ { \boldsymbol { A } } ^ { \boldsymbol { A } } \neq \boldsymbol { B } } \frac  G ^ { 2 } m _ { \boldsymbol { B } } m _ { \boldsymbol { A } } ^ { \boldsymbol { A } }  \end{array}
$$

$$
\begin{array} { r l } { \gamma _ { 1 } \psi _ { 2 } ^ { \ell } , \ldots - \sum _ { y , z } \frac { \bigcirc ( X _ { \ell } + \ell _ { 1 } ^ { \ell } \xi _ { 2 } ^ { \ell } \big ) \xi _ { 2 } } { \xi _ { 1 } ^ { \ell } } , } \\ { \lambda ^ { \ell } , \ldots , \ldots , } \\ { \lambda ^ { \ell } , \ldots , \frac { \bigcirc ( X _ { \ell } + \ell _ { 2 } ^ { \ell } ) ^ { \ell } ( 1 \ell _ { 1 } ^ { \ell } \lambda _ { 2 } ^ { \ell } ) } { \xi _ { 1 } ^ { \ell } } , \ldots , } \\ { \lambda ^ { \ell } , \ldots , \frac { \bigcirc ( X _ { \ell } + \ell _ { 1 } ^ { \ell } ) ^ { \ell } ( 1 \ell _ { 1 } ^ { \ell } \lambda _ { 2 } ^ { \ell } ) } { \xi _ { 1 } ^ { \ell } } , \ldots , \frac { \bigcirc ( X _ { \ell } + \ell _ { 2 } ^ { \ell } ) ^ { \ell } ( 1 \ell _ { 2 } ^ { \ell } \lambda _ { 1 } ^ { \ell } ) } { \xi _ { 1 } ^ { \ell } } , \ldots , \frac { \bigcirc ( X _ { \ell } + \ell _ { 1 } ^ { \ell } ) ^ { \ell } ( 1 \ell _ { 2 } ^ { \ell } \lambda _ { 2 } ^ { \ell } ) } { \xi _ { 1 } ^ { \ell } } , } \\ { + \frac { 1 } { 2 } \frac { \sqrt { \xi _ { 2 } \lambda _ { 2 } \lambda _ { 3 } \ell _ { 3 } ^ { \ell } } } { \xi _ { 1 } ^ { \ell } } , \ldots , \frac { \bigcirc ( X _ { \ell } + \ell _ { 2 } ^ { \ell } ) ^ { \ell } ( 1 \ell _ { 2 } ^ { \ell } \lambda _ { 3 } ^ { \ell } ) } { \xi _ { 1 } ^ { \ell } } , \ldots , } \\  \lambda ^ { \ell _ { 3 } } , \ldots , \ldots , \frac { \sqrt { \xi _ { 2 } ^ { \ell } ( X _ { \ell } + \ell _ { 1 } ^ { \ell } ) ^ { \ell } ( 1 \ell _ { 2 } ^ { \ell } \lambda _ { 1 } ^ { \ell } ) } { \xi _ { 1 } ^ { \ell } } , \ldots , } \\  \lambda ^ { \ell _ { 4 } } , \ldots , \frac  \sqrt { \xi _ { 2 } ^ { \ell } ( X _ { \ell } + \ell _ { 1 } ^ { \ell } ) }  \xi _ { 1 } ^   \end{array}
$$

(continued overleaf)

$$
\begin{array} { c } { { \displaystyle \partial _ { j } \Phi _ { 6 , \neg { A } } = - \sum _ { B \not = A } 2 G \mathcal { T } _ { B } ^ { k n } \partial _ { j k n } r _ { A B } - \sum _ { B \not = A } \frac { 2 G \mathcal { T } _ { B } n _ { A B } ^ { j } } { r _ { A B } ^ { 2 } } } } \\ { { + \sum _ { B \not = A } \frac { G m _ { B } ( \pmb { n } _ { A B } \cdot \pmb { v } _ { B } ) } { r _ { A B } ^ { 2 } } \biggl [ 2 v _ { B } ^ { j } - 3 ( \pmb { n } _ { A B } \cdot \pmb { v } _ { B } ) n _ { A B } ^ { j } \biggr ] . } } \end{array}
$$

Once more we have assumed that the bodies are well separated, and terms that are suppressed by factors of order $( R _ { A } / r _ { A B } ) ^ { 2 }$ relative to the leading contributions have been freely discarded. We make use of the notation introduced in Eq. (9.49),

$$
r _ { A B } : = r _ { A } - r _ { B } , \qquad r _ { A B } : = | { \boldsymbol r } _ { A } - { \boldsymbol r } _ { B } | , \qquad n _ { A B } : = \frac { r _ { A B } } { r _ { A B } } ,
$$

and $\partial _ { j k n } r _ { A B }$ stands for the third derivative of the inter-body distance $r _ { A B }$ with respect to the vector $r _ { A B }$ .

To illustrate how these results are obtained we begin with the simplest case, the evaluation of $\partial _ { j } U _ { \neg A }$ . Introducing the notation $s : = | \pmb { x } - \pmb { x } ^ { \prime } |$ , we recall first that the Newtonian potential is given by $\begin{array} { r } { U = G \int \rho ^ { * \prime } s ^ { - 1 } d ^ { 3 } x ^ { \prime } } \end{array}$ , so that $\begin{array} { r } { \partial _ { j } U = G \int \rho ^ { * \prime } \partial _ { j } s ^ { - 1 } d ^ { 3 } x ^ { \prime } } \end{array}$ ; the external piece of this is

$$
\partial _ { j } U _ { \neg { A } } = \sum _ { B \ne A } G \int _ { B } \rho ^ { * \prime } \partial _ { j } s ^ { - 1 } d ^ { 3 } x ^ { \prime } .
$$

In this we substitute $\pmb { x } ^ { \prime } = \pmb { r } _ { B } ( t ) + \pmb { \bar { x } } ^ { \prime }$ , so that $s$ becomes $s = | \pmb { x } - \pmb { r } _ { B } - \pmb { \bar { x } } ^ { \prime } |$ . We next expand $\partial _ { j } s ^ { - 1 }$ in powers of $\bar { x } ^ { \prime k }$ :

$$
\partial _ { j } s ^ { - 1 } = \partial _ { j } s _ { B } ^ { - 1 } - { \bar { x } } ^ { \prime k } \partial _ { j k } s _ { B } ^ { - 1 } + \frac { 1 } { 2 } { \bar { x } } ^ { \prime k } { \bar { x } } ^ { \prime n } \partial _ { j k n } s _ { B } ^ { - 1 } + \cdot \cdot \cdot ,
$$

where $s _ { B } : = | { \pmb x } - { \pmb r } _ { B } |$ . Making the substitution in $\partial _ { j } U _ { \neg A }$ , we find that it becomes

$$
\partial _ { j } U _ { \neg { A } } = \sum _ { B \not = A } \biggl ( G m _ { B } \partial _ { j } s _ { B } ^ { - 1 } + \frac { 1 } { 2 } G I _ { B } ^ { k n } \partial _ { j k n } s _ { B } ^ { - 1 } + \cdot \cdot \cdot \biggr ) .
$$

The term involving $\partial _ { j k } s _ { B } ^ { - 1 }$ vanishes, because $\begin{array} { r } { \int _ { B } \rho ^ { * \prime } \bar { x } ^ { \prime k } d ^ { 3 } x ^ { \prime } = 0 } \end{array}$ by virtue of the definition of the center-of-mass position $r _ { B } ^ { k }$ . The term involving the quadrupole moment tensor is smaller than the leading term by a factor of order $( R _ { B } / s _ { B } ) ^ { 2 }$ , and we discard it. After evaluation of $\partial _ { j } s _ { B } ^ { - 1 }$ using Eqs. (9.50), we set $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A } ( t )$ and arrive at Eq. (9.103a).

We next tackle a more complicated case, the evaluation of $\partial _ { t } U _ { \neg A } ^ { j }$ . The vector potential is $\begin{array} { r } { U ^ { j } = G \int \rho ^ { * \prime } v ^ { \prime } { } ^ { j } s ^ { - 1 } d ^ { 3 } x ^ { \prime } } \end{array}$ , and using the rules spelled out in $\mathrm { B o x } 8 . 4$ , we find that its time derivative is given by $\begin{array} { r } { \partial _ { t } U ^ { j } = G \int \rho ^ { * \prime } ( d v ^ { \prime j } / d t + v ^ { \prime j } v ^ { \prime k } \partial _ { k ^ { \prime } } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } } \end{array}$ . In this we substitute the Newtonian version of Euler’s equation, Eq. (8.104), and obtain

$$
\partial _ { t } U ^ { j } = - G \int ( \partial _ { j ^ { \prime } } p ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } + G \int \rho ^ { * \prime } ( \partial _ { j ^ { \prime } } U ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } - G \int \rho ^ { * \prime } v ^ { \prime \prime } v ^ { \prime k } \partial _ { k } s ^ { - 1 } d ^ { 3 } x ^ { \prime } ;
$$

in the last term we have made use of the identity $\partial _ { k ^ { \prime } } s ^ { - 1 } = - \partial _ { k } s ^ { - 1 }$ , and our expression for $\partial _ { t } U ^ { j }$ is accurate up to terms of order $c ^ { - 2 }$ . The external piece of this is

$$
\begin{array} { l } { { \partial _ { t } U _ { \mathrm { - } A } ^ { j } = \displaystyle - \sum _ { B \neq A } G \int _ { B } ( \partial _ { j ^ { \prime } } p ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } + \sum _ { B \neq A } G \int _ { B } \rho ^ { \ast \prime } ( \partial _ { j ^ { \prime } } U ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } } } \\ { { - \sum _ { B \neq A } G \int _ { B } \rho ^ { \ast \prime } v ^ { \prime \ j } v ^ { \prime k } \partial _ { k } s ^ { - 1 } d ^ { 3 } x ^ { \prime } . } } \end{array}
$$

We initially examine the first group of terms. We substitute $\pmb { x } ^ { \prime } = \pmb { r } _ { B } ( t ) + \pmb { \bar { x } } ^ { \prime }$ inside the integral and expand $s ^ { - 1 }$ in powers of $\bar { x } ^ { \prime k }$ ; it becomes

$$
s _ { B } ^ { - 1 } \int _ { B } \partial _ { j ^ { \prime } } p ^ { \prime } d ^ { 3 } \bar { x } ^ { \prime } - \partial _ { k } s _ { B } ^ { - 1 } \int _ { B } \bar { x } ^ { \prime k } \partial _ { j ^ { \prime } } p ^ { \prime } d ^ { 3 } \bar { x } ^ { \prime } + \frac { 1 } { 2 } \partial _ { k n } s _ { B } ^ { - 1 } \int _ { B } \bar { x } ^ { \prime k } \bar { x } ^ { \prime n } \partial _ { j ^ { \prime } } p ^ { \prime } d ^ { 3 } \bar { x } ^ { \prime } + \cdot \cdot \cdot
$$

The first integral vanishes automatically, the third vanishes because it contains an odd number of internal vectors, and after integration by parts the second integral returns $- \delta ^ { j k } P _ { B }$ . The first group of terms in Eq. (9.109) is therefore

$$
- \sum _ { B \ne A } G \int _ { B } ( \partial _ { j ^ { \prime } } p ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } = \sum _ { B \ne A } G P _ { B } \partial _ { j } s _ { B } ^ { - 1 } ,
$$

after discarding contributions that are smaller by a factor of order $( R _ { B } / s _ { B } ) ^ { 2 }$ .

We turn next to the second group of terms in Eq. (9.109), in which we insert $\partial _ { j ^ { \prime } } U ^ { \prime } =$ $\begin{array} { r } { \partial _ { j ^ { \prime } } U _ { A } ^ { \prime } + \partial _ { j ^ { \prime } } U _ { B } ^ { \prime } + \sum _ { C \neq A , B } \partial _ { j ^ { \prime } } U _ { C } ^ { \prime } } \end{array}$ . The integral that involves $\begin{array} { r } { \partial _ { j ^ { \prime } } U _ { A } ^ { \prime } = G \int _ { A } \rho ^ { * \prime \prime } \partial _ { j ^ { \prime } } s ^ { \prime - 1 } d ^ { 3 } x ^ { \prime \prime } } \end{array}$ is

$$
G \int _ { B } \int _ { A } { \rho ^ { * \prime } } { \rho ^ { * \prime \prime } } s ^ { - 1 } \partial _ { j ^ { \prime } } s ^ { \prime - 1 } d ^ { 3 } x ^ { \prime \prime } d ^ { 3 } x ^ { \prime } ,
$$

where $s ^ { \prime } : = | \pmb { x } ^ { \prime } - \pmb { x } ^ { \prime \prime } |$ . In this we substitute $\pmb { x } ^ { \prime } = \pmb { r } _ { B } + \pmb { \bar { x } } ^ { \prime }$ , $\pmb { x } ^ { \prime \prime } = \pmb { r } _ { A } + \pmb { \bar { x } } ^ { \prime \prime }$ and express $s ^ { - 1 } \partial _ { j ^ { \prime } } s ^ { \prime - 1 }$ as a double Taylor expansion in powers of $\bar { x } ^ { \prime k }$ and ${ \bar { x } } ^ { \prime \prime n }$ . Only the leading term is required, and we arrive at

$$
G \int _ { B } \rho ^ { * \prime } ( \partial _ { j ^ { \prime } } U _ { A } ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } = G ^ { 2 } m _ { A } m _ { B } s _ { B } ^ { - 1 } \partial _ { j ^ { \prime } } r _ { A B } ^ { - 1 } ,
$$

in which $\partial _ { j ^ { \prime } }$ is interpreted as a partial derivative with respect to $r _ { B } ^ { j }$ . The integral that involves $\partial _ { j ^ { \prime } } U _ { C } ^ { \prime }$ is evaluated in the same way, and we get

$$
G \int _ { B } \rho ^ { * \prime } ( \partial _ { j ^ { \prime } } U _ { C } ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } = G ^ { 2 } m _ { B } m _ { C } s _ { B } ^ { - 1 } \partial _ { j ^ { \prime } } r _ { B C } ^ { - 1 } .
$$

The integral that involves $\partial _ { j ^ { \prime } } U _ { B } ^ { \prime }$ is

$$
- G \int _ { B } \rho ^ { * \prime } \rho ^ { * \prime \prime } s ^ { - 1 } \frac { ( x ^ { \prime } - x ^ { \prime \prime } ) ^ { j } } { \vert x ^ { \prime } - x ^ { \prime \prime } \vert ^ { 3 } } d ^ { 3 } x ^ { \prime \prime } d ^ { 3 } x ^ { \prime } ,
$$

and in this we substitute $\pmb { x } ^ { \prime } = \pmb { r } _ { B } + \pmb { \bar { x } } ^ { \prime }$ and $\pmb { x } ^ { \prime \prime } = \pmb { r } _ { B } + \pmb { \bar { x } } ^ { \prime \prime }$ . We expand $s = | \pmb { x } - \pmb { r } _ { B } - \pmb { \bar { x } } ^ { \prime } |$ in powers of $\bar { x } ^ { \prime k }$ , eliminate all odd integrals, and get

$$
G \partial _ { k } s _ { B } ^ { - 1 } \int _ { B } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { \bar { x } ^ { \prime k } ( \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } ) ^ { j } } { | \bar { x } ^ { \prime } - \bar { x } ^ { \prime \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime \prime } d ^ { 3 } \bar { x } ^ { \prime } .
$$

After symmetrization in the primed and double-primed variables, we arrive at

$$
G \int _ { B } \rho ^ { * \prime } ( \partial _ { j ^ { \prime } } U _ { B } ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } = - G \Omega _ { B } ^ { j k } \partial _ { k } s _ { B } ^ { - 1 } .
$$

Collecting results, we find that the second group of terms in Eq. (9.109) is

$$
\begin{array} { l } { { \displaystyle \sum _ { B \ne A } G \int _ { B } \rho ^ { * \prime } ( \partial _ { j ^ { \prime } } U ^ { \prime } ) s ^ { - 1 } d ^ { 3 } x ^ { \prime } = - \sum _ { B \ne A } G \Omega _ { B } ^ { j k } \partial _ { k } s _ { B } ^ { - 1 } + \sum _ { B \ne A } G ^ { 2 } m _ { A } m _ { B } s _ { B } ^ { - 1 } \partial _ { j ^ { \prime } } r _ { A B } ^ { - 1 } } } \\ { { \displaystyle \qquad + \sum _ { B \ne A } \sum _ { C \ne A , B } G ^ { 2 } m _ { B } m _ { C } s _ { B } ^ { - 1 } \partial _ { j ^ { \prime } } r _ { B C } ^ { - 1 } . \qquad ( \mathrm { ~ o ~ r ~ } \qquad \rho ^ { \mathrm { ~ T ~ } } ) } } \end{array}
$$

We recall that in the second and third sums, $\partial _ { j ^ { \prime } }$ is interpreted as a partial derivative with respect to $r _ { B } ^ { j }$ .

We finally examine the third group of terms in Eq. (9.109). Here the manipulations are simple: we insert $\pmb { x } ^ { \prime } = \pmb { r } _ { B } + \pmb { \bar { x } } ^ { \prime }$ , $\pmb { v } ^ { \prime } = \pmb { v } _ { B } + \pmb { \bar { v } } ^ { \prime }$ and expand $\partial _ { k } s ^ { - 1 }$ in powers of ${ \bar { x } } ^ { \prime n }$ . We quickly arrive at

$$
- \sum _ { B \neq A } G \int _ { B } \rho ^ { \ast \prime } v ^ { \prime \prime } v ^ { \prime k } \partial _ { k } s ^ { - 1 } d ^ { 3 } x ^ { \prime } = - \sum _ { B \neq A } 2 G T _ { B } ^ { j k } \partial _ { k } s _ { B } ^ { - 1 } - \sum _ { B \neq A } G m _ { B } v _ { B } ^ { j } v _ { B } ^ { k } \partial _ { k } s _ { B } ^ { - 1 } .
$$

Substitution of Eqs. (9.111), (9.118), and (9.119) into Eq. (9.109) returns Eq. (9.103d), after computation of the derivatives of $s _ { B }$ , $r _ { A B }$ , and $r _ { B C }$ and evaluation of all expressions at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A } ( t )$ .

# 9.3.5 Equations of motion (final form)

When Eqs. (9.103) are inserted within Eqs. (9.101) and (9.102), we finally obtain an explicit expression for $a _ { A } ^ { j }$ , the coordinate acceleration of body $A$ . It can be decomposed as

$$
{ \bf \delta } { \bf { a } } _ { \scriptscriptstyle A } = { \bf { a } } _ { \scriptscriptstyle A } [ 0 \mathrm { p N } ] + { \bf { a } } _ { \scriptscriptstyle A } [ 1 \mathrm { p N } ] + { \bf { a } } _ { \scriptscriptstyle A } [ \mathrm { s T R } ] + O ( c ^ { - 4 } ) ,
$$

where

$$
{ \pmb a } _ { A } [ 0 \mathrm { P N } ] = - \sum _ { B \neq A } \frac { G m _ { B } } { r _ { A B } ^ { 2 } } { \pmb n } _ { A B }
$$

is the Newtonian acceleration, while

$$
\begin{array} { r l } { c ^ { 2 } a _ { 4 } [ \mathrm { I N N } ] = - { \displaystyle \sum _ { \scriptscriptstyle { R \nearrow } \scriptscriptstyle { \mathscr { R } } } } \frac { G m _ { \scriptscriptstyle { R } } } { r _ { A B } ^ { 2 } } \bigg [ v _ { A } ^ { 2 } - 4 ( v _ { A } \cdot v _ { B } ) + 2 v _ { B } ^ { 2 } - \frac { 3 } { 2 } ( n _ { A B } \cdot v _ { B } ) ^ { 2 } \bigg . } \\ & { \left. \qquad - \frac { 5 G m _ { \scriptscriptstyle { A } } } { r _ { A B } } - \frac { 4 G m _ { \scriptscriptstyle { B } } } { r _ { A B } } \right] n _ { A B } } \\ { \displaystyle } & { + { \displaystyle \sum _ { \scriptscriptstyle { B \ne A } } } \frac { G m _ { \scriptscriptstyle { B } } } { r _ { A B } ^ { 2 } } \Big [ n _ { A B } \cdot ( 4 v _ { A } - 3 v _ { B } ) \Big ] ( v _ { A } - v _ { B } ) } \\ { \displaystyle } & { + { \displaystyle \sum _ { \scriptscriptstyle { B \ne A } } \sum _ { \scriptscriptstyle { C \ne A } \scriptscriptstyle { \mathscr { D } } } } \frac { G ^ { 2 } m _ { \scriptscriptstyle { B } } m _ { \scriptscriptstyle { C } } } { r _ { A B } ^ { 2 } } \bigg [ \frac { 4 } { r _ { A C } } + \frac { 1 } { r _ { B C } } - \frac { T _ { A B } } { 2 r _ { B C } ^ { 2 } } ( n _ { A B } \cdot n _ { B C } ) \bigg ] n _ { A B } } \\ { \displaystyle } & { - \frac { 7 } { 2 } \sum _ { \scriptscriptstyle { R \ne A } \scriptscriptstyle { C \ne A } , \scriptscriptstyle { \mathscr { R } } } \frac { G ^ { 2 } m _ { \scriptscriptstyle { B } } m _ { \scriptscriptstyle { C } } } { r _ { A B } r _ { B C } ^ { 2 } } n _ { B C } ( 9 ) } \end{array}
$$

is the post-Newtonian piece of the acceleration vector.

The third contribution $\pmb { a } _ { A } [ \mathbf { S } \mathbf { T } \mathbf { R } ]$ is generated by the structure-integral terms that are scattered throughout Eqs. (9.103); it is given by

$$
\begin{array} { l } { { \displaystyle c ^ { 2 } a _ { _ A } ^ { j } [ \mathrm { S T R } ] = \sum _ { B \not = A } \biggl [ 4 G \bigl ( 2 { \cal T } _ { B } ^ { j k } + \Omega _ { B } ^ { j k } + \delta ^ { j k } { \cal P } _ { B } \bigr ) { \frac { n _ { A B } ^ { k } } { r _ { A B } ^ { 2 } } } } } \\ { ~ + { \frac { 1 } { 2 } } G \bigl ( 2 { \cal T } _ { B } ^ { k n } + \Omega _ { B } ^ { k n } + \delta ^ { k n } { \cal P } _ { B } \bigr ) \partial _ { j k n } r _ { A B } }  \\ { ~ - { G } \bigl ( 2 { \cal T } _ { B } + \Omega _ { B } + 3 { \cal P } _ { B } \bigr ) { \frac { n _ { A B } ^ { j } } { r _ { A B } ^ { 2 } } } - { \frac { G E _ { B } } { r _ { A B } ^ { 2 } } } n _ { A B } ^ { j } \biggr ] , }  \end{array}
$$

where $E _ { B } : = T _ { B } + \Omega _ { B } + E _ { B } ^ { \mathrm { i n t } }$ is the total energy contained in body $B$ , the sum of kinetic, gravitational, and internal energies. To obtain this expression we added ${ \textstyle \frac { 1 } { 2 } } G \delta ^ { k n } P _ { B } \partial _ { j k n } r _ { A B }$ to the second group of terms and subtracted the same thing, $\textstyle { \frac { 1 } { 2 } } G P _ { B } \partial _ { j k k } r _ { A B } = - P _ { B } n _ { A B } ^ { j } / r _ { A B } ^ { 2 }$ , from the third group. Most of $a _ { A } ^ { j } [ \mathrm { S T R } ]$ vanishes after imposing the equilibrium conditions of Eqs. (9.10) and (9.12); what survives is

$$
{ \pmb a } _ { \cal A } [ \mathrm { S T R } ] = - \sum _ { B \neq A } \frac { G ( E _ { B } / c ^ { 2 } ) } { r _ { A B } ^ { 2 } } { \pmb n } _ { A B } ,
$$

and this makes a contribution to the acceleration at 1pn order.

We observe that $\pmb { a } [ 0 \mathrm { \bf P N } ]$ and $\pmb { a }$ [str] combine nicely to give

$$
{ \pmb a } [ 0 \mathrm { P N } ] + { \pmb a } [ \mathrm { S T R } ] = - \sum _ { B \not = A } { \frac { G M _ { B } } { r _ { A B } ^ { 2 } } } { \pmb n } _ { A B } ,
$$

where

$$
M _ { B } : = m _ { B } + E _ { B } / c ^ { 2 } + O ( c ^ { - 4 } )
$$

is the total mass-energy of body $B$ . And we observe that the substitution $m _ { B } = M _ { B } +$ $O ( c ^ { - 2 } )$ can be made in $\pmb { a } _ { \mathcal { A } } [ 1 \mathrm { P N } ]$ without altering the form of the equations of motion at 1pn order. Our conclusion is that the equations of motion, like the inter-body metric of Eqs. (9.81), depend on the total mass-energy parameters $M _ { B }$ only, and not on their decomposition in terms of material mass $m _ { B }$ , kinetic energy $\mathcal { T } _ { B }$ , gravitational potential energy $\Omega _ { B }$ , and internal energy $E _ { B } ^ { \mathrm { i n t } }$ . The equations of motion, like the inter-body metric, are compatible with the strong formulation of the principle of equivalence.

Our final expression for the equations of motion is

$$
\begin{array} { c } { { \displaystyle { a _ { \cal A } = - \sum _ { B \not = A } \frac { G { \cal M } _ { B } } { r _ { A B } ^ { 2 } } { \pmb { n } } _ { A B } } } } \\ { { \displaystyle { + \frac { 1 } { c ^ { 2 } } \left[ - \sum _ { B \not = A } \frac { G { \cal M } _ { B } } { r _ { A B } ^ { 2 } } \biggl [ v _ { A } ^ { 2 } - 4 ( v _ { A } \cdot v _ { B } ) + 2 v _ { B } ^ { 2 } - \frac { 3 } { 2 } ( { \pmb { n } } _ { A B } \cdot { \pmb v } _ { B } ) ^ { 2 } \right. } } } \\ { { \displaystyle { \qquad \left. - \frac { 5 G { \cal M } _ { A } } { r _ { A B } } - \frac { 4 G { \cal M } _ { B } } { r _ { A B } } \right] { \pmb { n } } _ { A B } } } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { l } { { \displaystyle + \sum _ { B \not = A } \frac { G M _ { B } } { r _ { d B } ^ { 2 } } \Big [ n _ { A B } \cdot ( 4 v _ { A } - 3 v _ { B } ) \Big ] ( v _ { A } - v _ { B } ) } } \\ { { \displaystyle + \sum _ { B \not = A } \sum _ { C \not = A , B } \frac { G ^ { 2 } M _ { B } M _ { C } } { r _ { d B } ^ { 2 } } \Big [ \frac { 4 } { r _ { A C } } + \frac { 1 } { r _ { B C } } - \frac { r _ { A B } } { 2 r _ { B C } ^ { 2 } } ( n _ { A B } \cdot n _ { B C } ) \Big ] n _ { A B } } } \\ { { \displaystyle - \frac { 7 } { 2 } \sum _ { B \not = A } \sum _ { C \not = A , B } \frac { G ^ { 2 } M _ { B } M _ { C } } { r _ { A B } r _ { B C } ^ { 2 } } n _ { B C } \Bigg ] + O ( c ^ { - 4 } ) . } } \end{array}
$$

We recall our notation: $\pmb { r } _ { A } ( t )$ is the position of body $A$ in harmonic coordinates, ${ \pmb v } _ { A } ( t ) : =$ $d r _ { A } / d t$ is its velocity, and $\pmb { a } _ { A } : = d \pmb { v } _ { A } / d t$ is the coordinate acceleration. The vector $r _ { A B } : =$ $r _ { A } - r _ { B }$ points from body $B$ to body $A$ ; its length $r _ { A B } : = | \pmb { r } _ { A } - \pmb { r } _ { B } |$ is the inter-body distance, and $\pmb { n } _ { A B } : = \pmb { r } _ { A B } / r _ { A B }$ .

The equations of motion (9.127) apply to each body $A$ within the $N$ -body system. The bodies are assumed to be non-spinning and sufficiently well separated that the effects of higher-order multipole moments can be ignored. These equations have a rich history that was well summarized by Peter Havas in a 1989 essay. The equations were first formulated in 1917 by Lorentz and Droste, who published their results in Dutch in a communication to the Dutch Academy; their breakthrough remained unnoticed by the few researchers involved in the early development of general relativity. The equations of motion were also obtained at about the same time by de Sitter, who made use of the post-Newtonian metric previously derived by Droste, and postulated that the bodies should move on geodesics of the external metric; because of a calculational error, de Sitter’s equations differed from the correct post-Newtonian equations by one term, and led to the wrong prediction that the system’s barycenter should undergo a secular acceleration. The error was discovered and corrected in 1938 by Eddington and Clark (the twenty-year delay indicating the low level of activity in general relativity at the time), and in the same year a new derivation of the equations of motion was produced by Einstein, Infeld, and Hoffmann. In spite of the much earlier work of Lorentz and Droste, which eventually came to light thanks to an English translation published in 1937, the equations became known as the EIH equations of motion.

# 9.3.6 Conserved quantities

In Secs. 8.4.5, 8.4.6, and 8.4.7 we established the existence of conserved quantities associated with the dynamics of a perfect fluid in a post-Newtonian spacetime. We identified

$$
M : = \int \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \Bigr ) \biggr ] d ^ { 3 } x + O ( c ^ { - 4 } )
$$

as the total mass-energy of the fluid system,

$$
P ^ { j } : = \int \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi + p / \rho ^ { * } \Bigr ) \biggr ] d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int \rho ^ { * } \Phi ^ { j } d ^ { 3 } x + { \cal O } ( c ^ { - 4 } )
$$

as the total momentum, with $\Phi ^ { j }$ defined by

$$
\Phi ^ { j } : = G \int \rho ^ { * \prime } v _ { k } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { j } ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } ,
$$

and

$$
R ^ { j } : = \frac { 1 } { M } \int \rho ^ { * } x ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \Bigr ) \biggr ] d ^ { 3 } x + O ( c ^ { - 4 } )
$$

as the position of the center-of-mass for the entire fluid system. The total mass-energy and momentum are constants of the fluid’s motion; the position of the center-of-mass satisfies $M { \dot { R } } ^ { j } = P ^ { j }$ .

The conserved quantities keep their usefulness when the fluid distribution is broken up into a collection of $N$ separated bodies. In this case the integrals of Eqs. (9.128), (9.129), and (9.131) become a sum of $N$ individual integrals, and the conserved quantities become

$$
\begin{array} { r l } & { M = \displaystyle \sum _ { A } M _ { A } + \frac { 1 } { c ^ { 2 } } \sum _ { A } \frac { 1 } { 2 } M _ { A } v _ { A } ^ { 2 } - \frac { 1 } { c ^ { 2 } } \sum _ { A } \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { 2 r _ { A B } } + O ( c ^ { - 4 } ) , } \\ & { P = \displaystyle \sum _ { A } M _ { A } v _ { A } + \frac { 1 } { c ^ { 2 } } \sum _ { A } \frac { 1 } { 2 } M _ { A } v _ { A } ^ { 2 } v _ { A } } \\ & { \qquad - \frac { 1 } { c ^ { 2 } } \sum _ { A } \displaystyle \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { 2 r _ { A B } } \Big [ v _ { A } + ( n _ { A B } \cdot v _ { A } ) n _ { A B } \Big ] + O ( c ^ { - 4 } ) , } \\ & { M R = \displaystyle \sum _ { A } M _ { A } r _ { A } + \frac { 1 } { c ^ { 2 } } \sum _ { A } \frac { 1 } { 2 } M _ { A } v _ { A } ^ { 2 } r _ { A } - \frac { 1 } { c ^ { 2 } } \sum _ { A } \displaystyle \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { 2 r _ { A B } } r _ { A } + O ( c ^ { - 4 } ) . } \end{array}
$$

As usual the expressions of Eqs. (9.132) apply to bodies that are well separated; terms of fractional order $( R _ { A } / r _ { A B } ) ^ { 2 }$ have been neglected. It is straightforward (though tedious) to show directly that $d M / d t = 0$ , ${ d } P / { d t } = 0$ , and $M d R / d t = P$ by virtue of the post-Newtonian equations of motion. The expression for $M$ reveals that the total mass-energy of the $N$ -body system consists of a sum of mass-energies from each body, plus the total kinetic energy of the system (divided by $c ^ { 2 }$ ), plus the total gravitational potential energy of the system (also divided by $c ^ { 2 }$ ).

To derive these results we rely on the techniques introduced in the preceding subsections. Starting from Eq. (9.128) we find that the total mass-energy is given by

$$
\begin{array} { l } { { \displaystyle { \cal M } = \sum _ { A } \biggl ( \int _ { A } \rho ^ { * } d ^ { 3 } x + \frac { 1 } { 2 c ^ { 2 } } \int _ { A } \rho ^ { * } v ^ { 2 } d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int _ { A } \rho ^ { * } U d ^ { 3 } x + \frac { 1 } { c ^ { 2 } } \int _ { A } \rho ^ { * } \Pi d ^ { 3 } x \biggr ) } } \\ { { \displaystyle ~ + ~ { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

The $\rho ^ { * }$ integral gives $m _ { A }$ , the $\rho ^ { * } v ^ { 2 }$ integral produces $m _ { A } v _ { A } ^ { 2 } + 2 \mathcal { T } _ { A }$ after expressing $\pmb { v }$ as ${ \pmb v } _ { A } + { \bar { \pmb v } }$ , and the $\rho ^ { * } \Pi$ integral gives $E _ { A } ^ { \mathrm { i n t } }$ . In the $\rho ^ { * } U$ integral we write $U = U _ { A } + U _ { \lnot A }$ and observe that the first term produces $- 2 \Omega _ { A }$ , while the second term gives $m _ { \mathit { A } } U _ { \neg { \mathit { A } } } ( t , \pmb { r } _ { \mathit { A } } )$ after substitution of the Taylor expansion for the external potential; it is here that terms of fractional order $( R _ { A } / r _ { A B } ) ^ { 2 }$ are discarded. Collecting results, and noting that $m _ { A } + ( T _ { A } + \Omega _ { A } + E _ { A } ^ { \mathrm { i n t } } ) / c ^ { 2 } = M _ { A }$ , we arrive at Eq. (9.132a) after making the substitution $m _ { A } = M _ { A } + O ( c ^ { - 2 } )$ in the post-Newtonian terms. The derivation of Eq. (9.132c) proceeds in exactly the same way, and there is no need to go through the details here.

Equation (9.129) implies that the total momentum of the $N$ -body system is given by

$$
\begin{array} { l } { { \displaystyle P ^ { j } = \sum _ { A } \biggl ( \int _ { A } \rho ^ { * } v ^ { j } d ^ { 3 } x + \frac { 1 } { 2 c ^ { 2 } } \int _ { A } \rho ^ { * } v ^ { 2 } v ^ { j } d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int _ { A } \rho ^ { * } U v ^ { j } d ^ { 3 } x } } \\ { { \displaystyle \qquad + \frac { 1 } { c ^ { 2 } } \int _ { A } \rho ^ { * } \Pi v ^ { j } d ^ { 3 } x + \frac { 1 } { c ^ { 2 } } \int _ { A } p v ^ { j } d ^ { 3 } x - \frac { 1 } { 2 c ^ { 2 } } \int _ { A } \rho ^ { * } \Phi ^ { j } d ^ { 3 } x \biggr ) } } \\ { { \displaystyle \qquad + O ( c ^ { - 4 } ) . } } \end{array}
$$

The first four integrals are evaluated as we did previously, and the fifth integral produces $P _ { A } v _ { A } ^ { j }$ . In the sixth and final integral we decompose $\Phi ^ { j }$ as $\Phi _ { A } ^ { j } + \Phi _ { \lnot A } ^ { j }$ . The internal piece produces $- 2 \Omega _ { A } ^ { j k } v _ { A } ^ { k }$ , and the external piece gives $m _ { A } \Phi _ { \neg A } ^ { j } ( t , \stackrel {  } { r } _ { A } )$ after Taylor expansion of the external potential. From Eq. (9.130) we get

$$
\Phi _ { - A } ^ { j } : = \sum _ { B \neq A } G \int _ { B } \rho ^ { \ast \prime } v _ { k } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { j } ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } ,
$$

and in this we substitute $\pmb { x } ^ { \prime } = \pmb { r } _ { B } + \pmb { \bar { x } } ^ { \prime }$ and $\pmb { v } ^ { \prime } = \pmb { v } _ { B } + \pmb { \bar { v } } ^ { \prime }$ . To leading order in an expansion in powers of $\bar { x } ^ { \prime j }$ , we find that $\begin{array} { r } { \Phi _ { \neg A } ^ { j } ( t , \pmb { r } _ { A } ) = \sum _ { B \not = A } G m _ { B } ( \pmb { n } _ { A B } \cdot \pmb { v } _ { B } ) n _ { A B } ^ { j } / r _ { A B } } \end{array}$ . Collecting results, we have that

$$
\begin{array} { l l } { { \displaystyle { P ^ { j } = \sum _ { A } \biggl [ m _ { A } + \frac { 1 } { c ^ { 2 } } \bigl ( \mathcal T _ { A } + \Omega _ { A } + E _ { A } ^ { \mathrm { i n t } } \bigr ) \biggr ] v _ { A } ^ { j } + \frac { 1 } { c ^ { 2 } } \sum _ { A } \bigl ( 2 T _ { A } ^ { j k } + \Omega _ { A } ^ { j k } + \delta ^ { j k } P _ { A } \bigr ) v _ { A } ^ { k } } } } \\ { { \displaystyle { \quad + \frac { 1 } { c ^ { 2 } } \sum _ { A } \frac { 1 } { 2 } m _ { A } v _ { A } ^ { 2 } v _ { A } ^ { j } - \frac { 1 } { c ^ { 2 } } \sum _ { A } \sum _ { B \ne A } \frac { G m _ { A } m _ { B } } { 2 r _ { A B } } \biggl [ v _ { A } ^ { j } + ( n _ { A B } \cdot v _ { B } ) n _ { A B } ^ { j } \biggr ] } } } \\ { { \displaystyle { \quad + O ( c ^ { - 4 } ) . } } } & { { \displaystyle { ( 9 } } } \end{array}
$$

In the first group of terms we recognize $m _ { A } + E _ { A } / c ^ { 2 } = M _ { A }$ , and we eliminate the second group by invoking the equilibrium condition of Eq. (9.10). In the remaining groups we insert $m _ { A } = M _ { A } + O ( c ^ { - 2 } )$ , and in the last step we rearrange the double sum that gives rise to the last group: We switch the identities of bodies $A$ and $B$ and re-express the sums as

$$
\sum _ { B } \sum _ { A \neq B } \frac { G M _ { B } M _ { A } } { 2 r _ { B A } } ( \pmb { n } _ { B A } \cdot \pmb { v } _ { A } ) n _ { B A } ^ { j } ;
$$

because $\pmb { n } _ { B A } = - \pmb { n } _ { A B }$ and $r _ { B A } = r _ { A B }$ , this is

$$
\sum _ { A } \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { 2 r _ { A B } } ( \pmb { n } _ { A B } \cdot \pmb { v } _ { A } ) \pmb { n } _ { A B } ^ { j } ,
$$

and we have arrived at Eq. (9.132b).

# 9.3.7 Binary systems

The equations obtained in the preceding subsections apply to any number of well-separated bodies. To conclude this section we examine the special case $N = 2$ , that is, the case of a binary system. In the Newtonian context reviewed in Sec. 1.6.7, we saw that the description of the motion simplified when the origin of the coordinate system was attached to the barycenter $\pmb { R }$ , and that the position of each body could be determined in terms of the separation vector. The same simplification occurs in the post-Newtonian context.

The binary system consists of a first body of mass-energy $M _ { 1 }$ , position $r _ { 1 }$ , and velocity ${ \pmb v } _ { 1 }$ , and a second body of mass-energy $M _ { 2 }$ , position $r _ { 2 }$ , and velocity ${ \pmb v } _ { 2 }$ . To simplify the notation we introduce the mass parameters

$$
m : = M _ { 1 } + M _ { 2 } , \qquad \eta : = \frac { M _ { 1 } M _ { 2 } } { ( M _ { 1 } + M _ { 2 } ) ^ { 2 } } , \qquad \Delta : = \frac { M _ { 1 } - M _ { 2 } } { M _ { 1 } + M _ { 2 } } ,
$$

so that $m$ is a kind of total mass, $\eta$ a symmetric mass ratio, and $\Delta$ a dimensionless measure of the mass difference; it should be noted that $m$ differs from the total mass-energy $M$ introduced in Eq. (9.132) by terms of order $c ^ { - 2 }$ . We introduce also the separation $r : =$ $r _ { 1 } - r _ { 2 }$ , the relative velocity $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ , and we shall set $r : = | r | = r _ { 1 2 } , n : = r / r = { \pmb n } _ { 1 2 }$ , and $v : = | v |$ .

According to Eq. (9.132), the position of the system’s barycenter is given by

$$
M R = M _ { 1 } \bigg [ 1 + \frac { 1 } { 2 c ^ { 2 } } \bigg ( v _ { 1 } ^ { 2 } - \frac { G M _ { 2 } } { r } \bigg ) \bigg ] r _ { 1 } + M _ { 2 } \bigg [ 1 + \frac { 1 } { 2 c ^ { 2 } } \bigg ( v _ { 2 } ^ { 2 } - \frac { G M _ { 1 } } { r } \bigg ) \bigg ] r _ { 2 } ,
$$

and we wish to impose the condition $\pmb { R = 0 }$ . This allows us to solve for $r _ { 1 }$ and $r _ { 2 }$ in terms of $r$ , and the result is

$$
\begin{array} { l } { { \displaystyle r _ { 1 } = \frac { M _ { 2 } } { m } r + \frac { \eta \Delta } { 2 c ^ { 2 } } \Big ( v ^ { 2 } - \frac { G m } { r } \Big ) r , } } \\ { { \displaystyle r _ { 2 } = - \frac { M _ { 1 } } { m } r + \frac { \eta \Delta } { 2 c ^ { 2 } } \Big ( v ^ { 2 } - \frac { G m } { r } \Big ) r . } } \end{array}
$$

These equations imply that $\pmb { v } _ { 1 } = ( M _ { 2 } / m ) \pmb { v } + O ( c ^ { - 2 } )$ and $\pmb { v } _ { 2 } = - ( M _ { 1 } / m ) \pmb { v } + O ( c ^ { - 2 } )$

An equation of motion for $r$ can be obtained by computing the relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ from Eq. (9.127). Taking into account that ${ \pmb n } _ { 2 1 } = - { \pmb n } _ { 1 2 } = - { \pmb n }$ , the final result after simplification is

$$
\begin{array} { c } { { { \displaystyle a = - \frac { G m } { r ^ { 2 } } n - \frac { G m } { c ^ { 2 } r ^ { 2 } } \bigg \{ \bigg [ ( 1 + 3 \eta ) v ^ { 2 } - \frac { 3 } { 2 } \eta ( n \cdot v ) ^ { 2 } - 2 ( 2 + \eta ) \frac { G m } { r } \bigg ] n } } } \\ { { - 2 ( 2 - \eta ) ( n \cdot v ) v \bigg \} + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

This is a second-order differential equation for $\mathbf { } r ( t )$ , and its solution provides, through $r _ { 1 }$ and $r _ { 2 }$ , complete information regarding the motion of the binary system.

# 9.4 Motion of compact bodies

The post-Newtonian equations of motion (9.127) apply to fluid bodies that are well separated from one another, so that their mutual gravitational interaction is weak. The method of derivation relied on the post-Newtonian fluid equations, and these rest on an assumption that the self-gravity of each body is also weak. In this context, therefore, the gravitational field is assumed to be weak everywhere. In this section we examine a different context in which we retain the weakness of the mutual gravity between bodies, but allow each body to be strongly self-gravitating. We demonstrate that Eq. (9.127) continues to apply in these situations.

In the new context the bodies can be arbitrarily compact, and can possess an arbitrarily strong internal gravitational field. The bodies are not necessarily built from a perfect fluid, and indeed, we shall have no interest in their internal constitution. The only assumption concerning them shall be that they are spherically symmetric – a restrictive assumption that was not made in the fluid case. Each body may thus be a neutron star, a black hole, or any other object with strong internal gravity; it may still be, of course, a diffuse perfect-fluid body with weak internal gravity. We maintain, however, the requirement that the bodies be well separated, so that gravity is allowed to be weak between the bodies; it is in these inter-body regions that the post-Newtonian metric provides a good approximation to the true gravitational field.

We shall focus our attention on the vacuum region external to one of the compact bodies, and our new derivation of its equations of motion will be based entirely on solving the Einstein field equations in this region. Matter variables never enter this discussion. Our strategy is based instead on the transformation between the inertial frame of the post-Newtonian spacetime and the moving frame of the compact body. To describe this we rely on the theory of post-Newtonian coordinate transformations that was developed back in Sec. 8.3; please refer to the summary provided in Box 8.2. We follow the treatment provided in the 2008 article by Taylor and Poisson; the paper offers additional details that are not covered in this briefer treatment.

# 9.4.1 Zones and matching strategy

We select one of the compact bodies as our reference body, and we henceforth refer to it as “the body.” We introduce three distinct zones in spacetime (see Fig. 9.1). The first is the body zone, the body’s immediate neighborhood; in the body zone the gravitational field is dominated by the body’s own field, and the contribution from external bodies is small. If $\bar { r }$ is the distance from the body’s center-of-mass, then the body zone is defined by $\bar { r } < r _ { \operatorname* { m a x } }$ , with $r _ { \mathrm { m a x } } \ll r _ { A B }$ marking the zone’s boundary; $r _ { A B }$ is the inter-body distance, and the condition $\hat { r } \ll r _ { A B }$ ensures that the external gravity is indeed small. The second zone is the post-Newtonian zone, in which gravity is weak everywhere. The outer boundary of the post-Newtonian zone coincides with the boundary of the near zone, as was discussed in Sec. 8.1. The inner boundary is a sphere of radius $\bar { r } = r _ { \operatorname* { m i n } }$ , within which the body’s gravity becomes strong; we demand that $r _ { \operatorname* { m i n } } \gg G M / c ^ { 2 }$ , where $M$ is the body’s mass. When the bodies are well separated we have that $G M / c ^ { 2 } \ll r _ { A B }$ , and we can ensure that $r _ { \mathrm { m i n } } < r _ { \mathrm { m a x } }$ . The region $r _ { \mathrm { m i n } } < \bar { r } < r _ { \mathrm { m a x } }$ is the overlap zone, the intersection between the body and post-Newtonian zones.

Our strategy behind the new derivation of the equations of motion is based on the following key idea: We construct independently two solutions to the vacuum field equations

![](images/8196ef0da270b688d3a591c688d40605821da17eeae5d1dc8ab7b0f9b0c5eabb.jpg)  
Body, post-Newtonian, and overlap zones. The compact body is shown in black. The body zone is shown in wavy texture, and is restricted by $\bar { r } < r _ { \mathsf { m a x } } \ll r _ { A B r }$ where $\bar { \boldsymbol { r } }$ is the distance to the body. The post-Newtonian zone is tinted, and is restricted by $\bar { r } > r _ { \mathsf { m i n } } \gg G M / c ^ { 2 }$ . The overlap zone is shown in both wavy texture and tint, and is restricted by $r _ { \operatorname* { m i n } } < \bar { r } < r _ { \operatorname* { m a x } }$ .

# Fig. 9.1

in two overlapping regions of spacetime, and we match these solutions in the overlap; the equations of motion follow as an outcome of the matching procedure. The first solution is constructed in the body zone, in the body’s comoving frame, and the metric is presented in harmonic coordinates $( c \bar { t } , \bar { x } ^ { j } )$ that are attached to the body’s center-of-mass. The second solution is constructed in the post-Newtonian zone, in the global inertial frame, and the metric is presented in a different set of harmonic coordinates $( c t , x ^ { j } )$ that are attached to the center-of-mass of the entire $N$ -body system. To match the solutions in the overlap zone we must first reconcile the coordinate systems, and we therefore transform the post-Newtonian metric from the global coordinates $( c t , x ^ { j } )$ to the body coordinates $( c \bar { t } , \bar { x } ^ { j } )$ . We next compare the post-Newtonian metric to the body metric, and demand that they agree. The matching procedure determines (i) unknown functions within each metric, (ii) unknown functions within the coordinate transformation, and finally, (iii) the body’s equations of motion.

# 9.4.2 Body metric

We wish to find the metric of a spherical body placed in the presence of remote external bodies. The metric will be presented in harmonic coordinates $( c \bar { t } , \bar { x } ^ { j } )$ , in the body’s own moving frame, and it will be valid in the body zone, in which $\hat { r } \ll r _ { A B }$ . We do not need the metric inside the body, and indeed, the details of internal structure are entirely irrelevant for our purposes. If the body were in complete isolation, its external metric would be given by the Schwarzschild solution of Eq. (5.171) – refer to Sec. 5.6. What we need here, however, is a perturbed version of this metric that accounts for the weak gravity created by the external bodies. We state without proof that the time–time component of this perturbed metric is given by

$$
g _ { \bar { 0 } \bar { 0 } } = - \frac { 1 - R / 2 \bar { r } } { 1 + R / 2 \bar { r } } - \frac { 1 } { c ^ { 2 } } ( 1 - R / 2 \bar { r } ) ^ { 2 } \mathcal { E } _ { j k } \bar { x } ^ { j } \bar { x } ^ { k } ,
$$

where $R : = 2 G M / c ^ { 2 }$ is the Schwarzschild radius associated with the body mass $M$ , and $\mathcal { E } _ { j k } ( \overline { { t } } )$ is an arbitrary STF tensor that cannot be determined by solving the vacuum field equations in the body zone only. This metric is valid in the interval $R _ { \mathrm { b o d y } } < \bar { r } < r _ { \mathrm { m a x } }$ , where $R _ { \mathrm { b o d y } }$ is the body’s radius.

The perturbation terms in Eq. (9.143) have a quadrupolar structure, and they grow as $\bar { r } ^ { 2 }$ when $\bar { r } \gg R$ ; this is precisely the behavior that we expect from a tidal field. This can be seen most easily by evaluating the metric in the overlap zone $( G M / c ^ { 2 } \ll \bar { r } \ll r _ { A B } )$ , in which it can be expanded in powers of $c ^ { - 2 }$ . The Newtonian piece of the body metric is given by

$$
\bar { U } = \frac { G M } { \bar { r } } - \frac { 1 } { 2 } \mathcal { E } _ { j k } \bar { x } ^ { j } \bar { x } ^ { k } ,
$$

and we may compare this with Eq. (2.261) or with Eq. (8.73). The comparison reveals that $\begin{array} { r } { \mathcal { E } _ { j k } ( \bar { t } ) = - \partial _ { j k } U _ { \mathrm { e x t } } ( \bar { t } , \boldsymbol { r } ) } \end{array}$ , with $r ( \bar { t } )$ denoting the body’s position, and that the second term in Eq. (9.144) is the leading term in an expansion of the external potential in powers of $\bar { x } ^ { j }$ . The tensor $\mathcal { E } _ { j k } ( \overline { { t } } )$ therefore characterizes the body’s tidal environment, and Eq. (9.143) neglects higher-order terms in the expansion of the tidal potential.

The metric neglects other terms as well. A spherical body subjected to tidal forces normally suffers a deformation, but this effect was not included in Eq. (9.143). As we learned back in Sec. 2.5.1, the deformation is measured by the quadrupole-moment tensor $I _ { \langle j k \rangle }$ , and dimensional analysis requires a relationship of the form $\begin{array} { r } { G I _ { \langle j k \rangle } = - \frac { 2 } { 3 } k _ { 2 } R _ { \mathrm { b o d y } } ^ { 5 } \mathcal { E } _ { j k } } \end{array}$ , in which $k _ { 2 }$ is the body’s gravitational Love number, which depends on the details of its internal structure. The quadrupole-moment term in $\bar { U }$ would decay as $\bar { r } ^ { - 3 }$ , and would be of fractional order $( R _ { \mathrm { b o d y } } / \bar { r } ) ^ { 5 }$ relative to the tidal term; we choose to neglect it in $\bar { U }$ , and choose to neglect it in $g _ { \bar { 0 0 } } ^ { - - }$ also, recalling that our accuracy requirements were more modest in the preceding sections.

We shall not be interested in tidal effects in the following considerations, and for our purposes it is sufficient to know that in the overlap zone, the Newtonian piece of the body metric is given by $\bar { U } = G M / \bar { r } + O ( \bar { r } ^ { 2 } )$ . Similarly, we need to know that the post-Newtonian piece obtained from Eq. (9.143) is given by $\bar { \Psi } - \bar { U } ^ { 2 } = - G ^ { 2 } M ^ { 2 } / \bar { r } ^ { 2 } + { \cal O } ( \bar { r } ^ { 2 } )$ , so that

$$
\bar { \Psi } = { \cal O } ( \bar { r } ^ { 2 } ) .
$$

We shall not require the time–space components of the metric, apart from the knowledge that they contain tidal terms only; from this we infer that

$$
{ \bar { U } } ^ { j } = O ( { \bar { r } } ^ { 2 } ) .
$$

And we shall not need the space–space components of the metric; for our purposes they provide only redundant information.

Our derivation of the equations of motion relies on the expression of Eq. (9.143) for the body metric, and we present it here without a derivation. The result is based on a straightforward application of gravitational perturbation theory applied to spherical bodies, but to go through the details of its construction would take us too far afield. Some key points, however, are worth a mention. The unperturbed metric is given by the Schwarzschild solution, and its spherical symmetry guarantees that once a (linear) perturbation field is decomposed into spherical harmonics, each mode decouples from any other mode. The metric perturbation of Eq. (9.143) is a pure quadrupole field $( \ell = 2 )$ ), as can be seen from the fact that it is generated by a second-rank STF tensor $\mathcal { E } _ { j k } ( \bar { t } )$ . It can be shown that there is no non-trivial monopole field $( \ell = 0$ ) in vacuum (a trivial field would correspond to a meaningless shift in the mass parameter), and the statement that the dipole field $\ell = 1$ ) vanishes amounts to making a specific choice of center-of-mass position for the body. It is therefore the quadrupole field that describes the leading-order tidal effects, and higher-order multipole fields correspond to higher-order terms in the Taylor expansion of the external Newtonian potential; we neglect these additional terms.

We make a final remark before moving on: The Newtonian potential of Eq. (9.144) is expressed in terms of $M$ , the mass parameter of the Schwarzschild metric. This is the body’s total mass-energy, which in principle could be expressed in exact relativistic form in terms of the material mass and all relevant forms of energy. Our current convention for the Newtonian potential is therefore different from our previous usage, in which $U$ accounted for the material mass $m$ only, while $\Psi$ accounted for the body’s energy $E$ . Here we let the Newtonian potential account for the body’s total mass-energy, and as a result, the expected energy terms do not appear within the post-Newtonian potential of Eq. (9.145).

# 9.4.3 Post-Newtonian metric

Gravity is weak everywhere in the post-Newtonian zone, and here we may express the metric as the post-Newtonian expansion

$$
g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } ( \Psi - U ^ { 2 } ) + { \cal O } ( c ^ { - 4 } ) .
$$

The metric is presented in the global inertial frame, in harmonic coordinates $( c t , x ^ { j } )$ attached to the center-of-mass of the entire $N$ -body system. The post-Newtonian zone coincides with the near zone, but it excludes a sphere of radius $\bar { r } = r _ { \operatorname* { m i n } }$ centered on the body; $r _ { \mathrm { m i n } }$ is chosen to be much larger than $G M / c ^ { 2 }$ to ensure that gravity does not get too strong as we approach the body.

In the overlap zone $( G M / c ^ { 2 } \ll r _ { \operatorname* { m i n } } < \bar { r } < r _ { \operatorname* { m a x } } \ll r _ { A B } )$ the post-Newtonian metric must satisfy the vacuum field equations. According to Eqs. (8.24), the gravitational potentials must be solutions to $\nabla ^ { 2 } U = 0$ , $\nabla ^ { 2 } U ^ { j } = 0$ , $\nabla ^ { 2 } \psi = 0$ , and $\nabla ^ { 2 } X = 2 U$ ; the post-Newtonian potential is $\begin{array} { r } { \Psi = \psi + \frac { 1 } { 2 } \partial _ { t t } { \boldsymbol { X } } } \end{array}$ . The solutions must contain the information that a compact body is situated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ , and that external bodies are to be found outside the overlap zone. We model the body as a post-Newtonian monopole (an assumption that is justified by the matching procedure to be carried out later), and we write

$$
\begin{array} { l } { { U = \displaystyle \frac { G M } { s } + U _ { \mathrm { e x t } } , } } \\ { { U ^ { j } = \displaystyle \frac { G M v ^ { j } } { s } + U _ { \mathrm { e x t } } ^ { j } , } } \\ { { \psi = \displaystyle \frac { G M \mu } { s } + \psi _ { \mathrm { e x t } } , } } \\ { { X = G M s + X _ { \mathrm { e x t } } , } } \end{array}
$$

where $s : = | \pmb { x } - \pmb { r } ( t ) |$ is the length of the vector $s : = x - r ( t )$ . We have introduced ${ \pmb v } ( t ) : = d { \pmb r } / d t$ as the body’s velocity, and its presence in the vector potential is required by the harmonic gauge condition, $\partial _ { t } U + \partial _ { j } U ^ { j } = 0$ . The quantity $\mu ( t )$ is a post-Newtonian correction to the mass parameter $M$ , and this cannot be determined by solving the field equations in the post-Newtonian zone only. The external potentials separately satisfy the vacuum field equations. From Eq. (9.148) we get

$$
\Psi = \frac { G M } { s } \Big [ \mu + { \frac { 1 } { 2 } } { v } ^ { 2 } - { \frac { 1 } { 2 } } ( \pmb { n } \cdot \pmb { v } ) ^ { 2 } \Big ] - { \frac { 1 } { 2 } } G M \pmb { n } \cdot \pmb { a } + \Psi _ { \mathrm { e x t } } ,
$$

where $\pmb { n } : = \pmb { s } / s$ and $\Psi _ { \mathrm { e x t } } = \psi _ { \mathrm { e x t } } - { \textstyle \frac { 1 } { 2 } } \partial _ { t t } X _ { \mathrm { e x t } }$ . We have also introduced $\pmb { a } ( t ) : = d \pmb { v } / d t$ as the body’s acceleration, and this is the quantity that we wish to determine.

Notice that the body potentials are all singular at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ ; this is to be expected from a monopole field. The singularity, however, is not physical – the body is not a point mass, but a fully extended object. The singularity is also only apparent, because the point $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ lies outside the post-Newtonian zone; the potentials are valid for $s \gg G M / c ^ { 2 }$ only.

# 9.4.4 Transformation to the comoving frame

The coordinate transformation from the inertial system $( c t , x ^ { j } )$ to the comoving system $( c \bar { t } , \bar { x } ^ { j } )$ is described in $\mathrm { B o x } ~ 8 . 2$ . It is characterized by a number of free functions that must be determined in the course of the matching procedure. The most important piece of information is the vector $r ( \bar { t } )$ , which determines the position of the body. The transformation also involves $A ( \bar { t } ) , H ^ { j } ( \bar { t } ) , R ^ { j } ( \bar { t } )$ , and the harmonic function $\gamma ( \bar { t } , \bar { x } ^ { j } )$ .

The first step is to construct the “hatted potentials,” the original gravitational potentials evaluated at time $t = \bar { t }$ and position $\pmb { x } = \pmb { \bar { x } } + \pmb { r } ( \bar { t } )$ . From Eqs. (9.148) and (9.149) we get

$$
\begin{array} { l } { \displaystyle \hat { U } = \frac { G M } { \bar { r } } + \hat { U } _ { \mathrm { e x t } } , } \\ { \displaystyle \hat { U } ^ { j } = \frac { G M v ^ { j } } { \bar { r } } + \hat { U } _ { \mathrm { e x t } } ^ { j } , } \\ { \displaystyle \hat { \Psi } = \frac { G M } { \bar { r } } \Big [ \mu + \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } ( \bar { n } \cdot v ) ^ { 2 } \Big ] - \frac { 1 } { 2 } G M \bar { n } \cdot a + \hat { \Psi } _ { \mathrm { e x t } } , } \end{array}
$$

where $v , \mu$ , and $\pmb { a }$ are now functions of $\bar { t }$ , and $\bar { \pmb { n } } : = \bar { \pmb { x } } / \bar { r }$ .

The transformed potentials $\bar { U } , \bar { U } ^ { j }$ , and $\bar { \Psi }$ will contain terms that are singular in the formal limit $\bar { r }  0$ , and terms that are well-behaved in this limit. The external potentials

contribute non-singular terms, and as usual it is convenient to express them as Taylor expansions in powers of $\bar { x } ^ { j }$ . We write, for example,

$$
{ \hat { U } } _ { \mathrm { e x t } } ( { \bar { t } } , { \bar { x } } ) = { \hat { U } } _ { \mathrm { e x t } } ( { \bar { t } } , \mathbf { 0 } ) + { \bar { x } } ^ { j } \partial _ { j } { \hat { U } } _ { \mathrm { e x t } } ( { \bar { t } } , \mathbf { 0 } ) + { \frac { 1 } { 2 } } { \bar { x } } ^ { j } { \bar { x } } ^ { k } \partial _ { j k } { \hat { U } } _ { \mathrm { e x t } } ( { \bar { t } } , \mathbf { 0 } ) + \cdots .
$$

The harmonic function $\gamma$ also contributes non-singular terms, and we also express it as a Taylor expansion:

$$
\gamma ( \bar { t } , \bar { x } ) = C ( \bar { t } ) + \gamma _ { j } ( \bar { t } ) \bar { x } ^ { j } + \frac { 1 } { 2 } \gamma _ { j k } ( \bar { t } ) \bar { x } ^ { j } \bar { x } ^ { k } + \cdot \cdot \cdot ;
$$

here $C ( \bar { t } )$ and $\gamma _ { j } ( \bar { t } )$ are arbitrary functions of time $\bar { t }$ , and $\gamma _ { j k } ( \bar { t } )$ is an arbitrary STF tensor (so that $\gamma$ can be a solution to Laplace’s equation).

For our purposes here it is useful to refine the notation of $\operatorname { B o x } 8 . 2$ and decompose the acceleration vector $\pmb { a } ( \bar { t } )$ into Newtonian and post-Newtonian pieces. We write

$$
\begin{array} { r } { \pmb { a } = \pmb { a } [ 0 \mathrm { p N } ] + \pmb { a } [ 1 \mathrm { p N } ] + O ( c ^ { - 4 } ) , \qquad \pmb { a } [ 1 \mathrm { p N } ] = : c ^ { - 2 } \pmb { \alpha } , } \end{array}
$$

and re-express the transformation of the Newtonian potential as

$$
\bar { U } = \hat { U } - \dot { A } + \frac { 1 } { 2 } v ^ { 2 } - a _ { j } [ 0 \mathrm { p v } ] \bar { x } ^ { j } .
$$

The missing piece involving ${ \pmb a } [ 1 \mathrm { P N } ]$ is transferred to the post-Newtonian potential $\bar { \Psi }$ . This has the effect of altering the expression of $G _ { j }$ by an additional term $- \alpha _ { j }$ .

A lengthy computation reveals that the transformed potentials are given by

$$
\begin{array} { l } { { \displaystyle \bar { U } = \frac { G M } { \bar { r } } + { } _ { 0 } U + { } _ { 1 } U _ { j } \bar { x } ^ { j } + \cdots , } } \\ { { \displaystyle \bar { U } ^ { j } = { } _ { 0 } U ^ { j } + { } _ { 1 } U _ { \phantom { j } k } ^ { j } \bar { x } ^ { k } + \cdots , } } \\ { { \displaystyle \bar { \Psi } = - \frac { G M } { \bar { r } ^ { 3 } } \big ( H _ { j } - A { } \upsilon _ { j } \big ) \bar { x } ^ { j } + \frac { G M } { \bar { r } } \big ( \mu + \dot { A } - 2 { } \upsilon ^ { 2 } \big ) + { } _ { 0 } \Psi + { } _ { 1 } \Psi _ { j } \bar { x } ^ { j } + \cdots , } } \end{array}
$$

with

$$
\begin{array} { l } { { \ _ { a } U = \frac { 1 } { 2 } v ^ { 2 } - \mathcal { \bar { A } } + \hat { U } _ { \mathrm { e x t } } , } } \\ { { \ } } \\ { { \ _ { \perp } U _ { j } = - a _ { j } [ 0 \mathrm { e n } ] + \partial _ { j } \hat { U } _ { \mathrm { e x t } } , } } \\ { { \ } } \\ { { \_ { \omega } U ^ { j } = \hat { V } _ { \mathrm { e x t } } ^ { j } - \nu ^ { j } \hat { U } _ { \mathrm { e x t } } + \frac { 1 } { 4 } ( 2 \mathcal { \bar { A } } - v ^ { 2 } ) v ^ { j } - \frac { 1 } { 4 } \hat { H } ^ { j } + \frac { 1 } { 4 } c _ { p q } ^ { j } \nu ^ { p } R ^ { q } + \frac { 1 } { 4 } \gamma ^ { j } , } } \\ { { \ } } \\ { { \ _ { U _ { k } ^ { j } } \hat { U } _ { \mathrm { e x t } } ^ { j } = \hat { p } _ { k } \hat { U } _ { \mathrm { e x t } } ^ { j } - \nu ^ { j } \partial _ { k } \hat { U } _ { \mathrm { e x t } } + \frac { 3 } { 8 } v ^ { j } \alpha _ { k } [ 0 \mathrm { e n } ] + \frac { 1 } { 8 } \alpha ^ { j } [ 0 \mathrm { e n } ] v _ { k } } } \\ { { \ } } \\ { { \ \ } } \\ { { \ + \frac { 1 } { 4 } \delta _ { k } ^ { j } \hat { k } \big ( \frac { 4 } { 3 } \mathcal { \bar { A } } - 2 v ^ { \alpha } n _ { \mathrm { e } } [ 0 \mathrm { e n } ] \big ) - \frac { 1 } { 4 } \epsilon _ { k } ^ { j } \hat { k } ^ { p } + \frac { 1 } { 4 } \gamma _ { k } ^ { j } , } } \\ { { \ } } \\  { \ _ { \mathrm { s p } } \hat { \nu } = \hat { V } _ { \mathrm { e x t } } - 4 v _ { 0 } \hat { V } _ { \mathrm { e x t } } ^ { j } + 2 v ^ { 2 } \hat { U } _ { \mathrm { e x t } } + 4 \beta _ { i } \hat { V } _ { \mathrm { e x t } } + ( H ^ { j } - A v ^ { j } ) \partial _ { j } \hat { U } _ { \mathrm { e x t } } } \\ { { \ } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { r l } & { \mathrm { i } { \Psi } _ { j } = \partial _ { \bar { j } } \hat { \Psi } _ { \mathrm { e x t } } - 4 v _ { k } \partial _ { \bar { j } } \hat { U } _ { \mathrm { e x t } } ^ { k } + \Bigl ( \frac { 5 } { 2 } v ^ { 2 } - \dot { A } \Bigr ) \partial _ { \bar { j } } \hat { U } _ { \mathrm { e x t } } - \frac { 1 } { 2 } v _ { j } v ^ { k } \partial _ { \bar { k } } \hat { U } _ { \mathrm { e x t } } + v _ { j } \partial _ { \bar { t } } \hat { U } _ { \mathrm { e x t } } } \\ & { \qquad + A \partial _ { \bar { t } \bar { j } } \hat { U } _ { \mathrm { e x t } } + ( H ^ { k } - A v ^ { k } ) \partial _ { \bar { j } \bar { k } } \hat { U } _ { \mathrm { e x t } } - \alpha _ { j } + \Bigl ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } \Bigr ) a _ { j } [ 0 \mathrm { p N } ] } \\ & { \qquad - \Bigl ( \ddot { A } - \frac { 3 } { 2 } v ^ { n } a _ { n } [ 0 \mathrm { p N } ] \Bigr ) v _ { j } - \epsilon _ { j p q } \bigl ( \partial ^ { \bar { p } } \hat { U } _ { \mathrm { e x t } } R ^ { q } + v ^ { p } \dot { A } ^ { q } \bigr ) - \dot { \gamma } _ { j } . } \end{array}
$$

It is understood that in these expressions, the external potentials are all evaluated at $\bar { \boldsymbol { x } } = \mathbf { 0 }$ after differentiation.

For later convenience it is useful to decompose $\phantom { } _ { 1 } U _ { j k }$ into its trace, symmetric-tracefree, and antisymmetric parts. We have

$$
\mathbf { \nabla } _ { 1 } U _ { j k } = \frac { 1 } { 3 } \delta _ { j k } \mathbf { \nabla } _ { 1 } U + \mathbf { \nabla } _ { 1 } U _ { \langle j k \rangle } + \mathbf { \nabla } _ { 1 } U _ { [ j k ] }
$$

with

$$
\begin{array} { l } { { \displaystyle { } _ { 1 } U = \ddot { \cal A } - \partial _ { \bar { t } } \hat { U } _ { \mathrm { e x t } } - v ^ { j } a _ { j } [ 0 \mathrm { p N } ] , } } \\ { { \displaystyle { } _ { 1 } U _ { \langle j k \rangle } = \partial _ { \langle \bar { J } } \hat { U } _ { k \rangle } ^ { \mathrm { e x t } } - v _ { \langle j } \partial _ { \bar { k } \rangle } \hat { U } _ { \mathrm { e x t } } + \frac { 1 } { 2 } v _ { \langle j } a _ { k \rangle } [ 0 \mathrm { p N } ] + \frac { 1 } { 4 } \gamma _ { j k } , } } \\ { { \displaystyle { } _ { 1 } U _ { [ j k ] } = - \partial _ { [ \bar { J } } \hat { U } _ { k ] } ^ { \mathrm { e x t } } - v _ { [ j } \partial _ { \bar { k } ] } \hat { U } _ { \mathrm { e x t } } + \frac { 1 } { 4 } v _ { [ j } a _ { k ] } [ 0 \mathrm { p N } ] - \frac { 1 } { 4 } \epsilon _ { j k p } \dot { R } ^ { p } } . }  \end{array}
$$

# 9.4.5 Matching

Comparison of Eqs. (9.144), (9.145), and (9.146) with Eqs. (9.155) reveals that agreement is achieved if and only if the matching conditions

$$
\phantom { } _ { 0 } U = { } _ { 1 } U _ { j } = { } _ { 0 } U ^ { j } = { } _ { 1 } U _ { j k } = \phantom { } _ { 0 } \Psi = { } _ { 1 } \Psi _ { j } = 0 ,
$$

and

$$
H ^ { j } = A v ^ { j } , \qquad \mu = 2 v ^ { 2 } - \dot { A } ,
$$

are satisfied. By virtue of Eq. (9.157), the condition ${ \cal U } _ { j k } = 0$ implies the independent conditions $\mathrm { \Upsilon } _ { 1 } U = \mathrm { \Gamma } _ { 1 } U _ { \langle j k \rangle } = \mathrm { \Gamma } _ { 1 } U _ { [ j k ] } = 0$ . We now proceed to extract the information contained in these equations.

The condition $\phantom { } _ { 0 } U = 0$ implies that $\begin{array} { r } { \dot { A } = \frac { 1 } { 2 } v ^ { 2 } + \hat { U } _ { \mathrm { e x t } } } \end{array}$ . This, together with Eq. (9.160), tells us that the metric function $\mu$ is given by

$$
\mu = \frac { 3 } { 2 } v ^ { 2 } - \hat { U } _ { \mathrm { e x t } } ( \bar { t } , \mathbf { 0 } ) .
$$

The condition ${ } _ { 1 } U _ { j } = 0$ implies that

$$
a _ { j } [ 0 \mathrm { P N } ] = \partial _ { \bar { \jmath } } \hat { U } _ { \mathrm { e x t } } ( \bar { t } , \mathbf { 0 } ) ,
$$

and we have established the fact that to leading order in a post-Newtonian expansion of the mutual gravitational interaction, the compact body moves just as any Newtonian body.

The condition ${ } _ { 0 } U _ { j } = 0$ reveals that $\gamma _ { j } = - 4 \hat { U } _ { j } ^ { \mathrm { e x t } } + ( \textstyle { \frac { 1 } { 2 } } v ^ { 2 } + 3 \hat { U } _ { \mathrm { e x t } } ) v _ { j } + A \partial _ { \bar { j } } \hat { U } _ { \mathrm { e x t } } -$ $\epsilon _ { j p q } v ^ { p } R ^ { q }$ . The condition $\phantom { } _ { 1 } U = 0$ is automatically satisfied, and ${ \cal U } _ { \langle j k \rangle } = 0$ determines $\gamma _ { j k }$ , but this quantity is not required in the derivation of the equations of motion. The condition ${ \cal U } _ { [ j k ] } = 0$ reveals that $\epsilon _ { j k p } \dot { R } ^ { p } = - 4 \partial _ { [ \bar { \jmath } } \hat { U } _ { k ] } ^ { \mathrm { e x t } } - 3 v _ { [ j } \partial _ { \bar { k } ] } \hat { U } _ { \mathrm { e x t } }$ , and this equation determines the vector $R ^ { j }$ . The condition $\Psi = 0$ determines $\dot { C }$ , but this quantity also is not required. And finally, ${ \Psi } _ { j } = 0$ determines the post-Newtonian piece of the acceleration vector; after some algebra and simplification, we arrive at

$$
\begin{array} { r l } & { \alpha _ { j } = \left( v ^ { 2 } - 4 \hat { U } _ { \mathrm { e x t } } \right) \partial _ { \bar { \jmath } } \hat { U } _ { \mathrm { e x t } } - v _ { j } \left( v ^ { k } \partial _ { k } \hat { U } _ { \mathrm { e x t } } + 3 \partial _ { \bar { t } } \hat { U } _ { \mathrm { e x t } } \right) } \\ & { \qquad - 4 v _ { k } \partial _ { \bar { \jmath } } \hat { U } _ { \mathrm { e x t } } ^ { k } + 4 \partial _ { \bar { t } } \hat { U } _ { \mathrm { e x t } } ^ { j } + \partial _ { \bar { \jmath } } \hat { \Psi } _ { \mathrm { e x t } } . } \end{array}
$$

As before it is understood that the external potentials are evaluated at $\bar { \boldsymbol { x } } = \mathbf { 0 }$ after differentiation.

The matching conditions have determined the unknown pieces of the coordinate transformation, the functions $A , H ^ { j } , R ^ { j } , C , \gamma _ { j } , \gamma _ { j k }$ , and the all-important vector $r ( \bar { t } )$ , which is recovered by solving the equations of motion ${ \ddot { r } } = { \pmb a } [ 0 \mathrm { P N } ] + c ^ { - 2 } { \pmb \alpha } + O ( c ^ { - 4 } )$ . In addition, the matching conditions have determined the unknown metric function $\mu$ , and further analysis would also produce the tidal moments $\mathcal { E } _ { j k }$ . The problem, therefore, is solved completely: we have the metric, the coordinate transformation, and the equations of motion.

# 9.4.6 Equations of motion

The final form of the equations of motion is obtained by inserting Eqs. (9.162) and (9.163) within Eq. (9.153). We evaluate each quantity at time $\bar { t } = t$ and replace the hatted potentials by their original version in Eqs. (9.148) and (9.149). After paying careful attention to the rules of partial differentiation, which are spelled out at the end of $\mathrm { B o x } 8 . 2$ , we arrive at

$$
\begin{array} { c } { { a ^ { j } = \partial _ { j } U _ { \mathrm { e x t } } + { \displaystyle { \frac { 1 } { c ^ { 2 } } } } \Big [ \big ( v ^ { 2 } - 4 U _ { \mathrm { e x t } } \big ) \partial _ { j } U _ { \mathrm { e x t } } - v ^ { j } \big ( 4 v ^ { k } \partial _ { k } U _ { \mathrm { e x t } } + 3 \partial _ { t } U _ { \mathrm { e x t } } \big ) } } \\ { { - 4 v _ { k } \big ( \partial _ { j } U _ { \mathrm { e x t } } ^ { k } - \partial _ { k } U _ { \mathrm { e x t } } ^ { j } \big ) + 4 \partial _ { t } U _ { \mathrm { e x t } } ^ { j } + \partial _ { j } \Psi _ { \mathrm { e x t } } \Big ] + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

The acceleration vector $\pmb { a }$ now stands for $d ^ { 2 } r / d t ^ { 2 }$ , and the equations of motion are expressed in the global inertial frame. These should be compared with Eq. (9.101), which determines the motion of a fluid body. The equations are identical, and we have established the important statement that the compact body moves in exactly the same way as a weakly self-gravitating body. This is a nice confirmation of the fact that general relativity is compatible with the strong formulation of the principle of equivalence.

In principle the calculation should be completed with the determination of the external potentials and the conversion of Eq. (9.164) to an explicit system of differential equations for the position vectors $\pmb { r } _ { A } ( t )$ . There is no need to go through these details here; it is clear that the computation would lead back to Eq. (9.127).

A few comments, however, may be helpful. The decompositions of Eqs. (9.148) and (9.149) distinguish between “the body” and the external objects. To recover the expressions of Eqs. (9.55), (9.58), and (9.80), we must adapt our notation and assign the label $A = 1$ (say) to our reference body. The internal term $G M / s$ in $U$ then becomes $G M _ { 1 } / s _ { 1 }$ . Because the Newtonian potential satisfies a linear field equation $\nabla ^ { 2 } U = 0 )$ ), the external piece can be written as a sum of similar terms, so that $\begin{array} { r } { U _ { \mathrm { e x t } } = \sum _ { A \ne 1 } G M _ { A } / s _ { A } } \end{array}$ . This reproduces the expression of Eq. (9.55), and the same procedure also gives rise to Eq. (9.58).

The procedure works also for $\Psi$ , which also satisfies a linear field equation. In the new notation, and with $\mu _ { 1 }$ given by Eq. (9.161), the internal piece of $\Psi$ is

$$
\Psi _ { 1 } = \frac { G M _ { 1 } } { s _ { 1 } } \Big [ 2 v _ { 1 } ^ { 2 } - \frac { 1 } { 2 } ( \pmb { n } _ { 1 } \cdot \pmb { v } _ { 1 } ) ^ { 2 } - U _ { \mathrm { e x t } } \Big ] - \frac { 1 } { 2 } G M _ { 1 } \pmb { n } _ { 1 } \cdot \pmb { a } _ { 1 } .
$$

With $\begin{array} { r } { U _ { \mathrm { e x t } } = \sum _ { B \neq 1 } G M _ { B } / r _ { 1 B } } \end{array}$ and $\pmb { a } _ { 1 } = \pmb { \nabla } U _ { \mathrm { e x t } } + O ( c ^ { - 2 } )$ , this is

$$
\Psi _ { 1 } = \frac { G M _ { 1 } } { s _ { 1 } } \Big [ 2 v _ { 1 } ^ { 2 } - \frac { 1 } { 2 } ( \pmb { n } _ { 1 } \cdot \pmb { v } _ { 1 } ) ^ { 2 } \Big ] - \sum _ { B \neq 1 } \frac { G ^ { 2 } M _ { 1 } M _ { B } } { r _ { 1 B } s _ { 1 } } \bigg ( 1 - \frac { \pmb { n } _ { 1 B } \cdot \pmb { s } _ { 1 } } { 2 r _ { 1 B } } \bigg ) .
$$

Taking $\Psi _ { \mathrm { e x t } }$ to be a sum of similar terms, we have reproduced Eq. (9.80), except for a noticeable difference: the sum $\sum _ { A } G E _ { A } / s _ { A }$ is present in the original expression, but it is absent here. The reason for this discrepancy was explained at the end of Sec. 9.4.2: here the energy terms have been incorporated within the Newtonian potential, which is expressed in terms of $M _ { A }$ instead of $m _ { A }$ ; they must therefore be removed from the post-Newtonian potential.

# 9.5 Motion of spinning bodies

Back in Sec. 9.1.4 we imposed the important restriction that each body should have a vanishing angular-momentum tensor, and subsequent developments relied heavily on this assumption. But rotation is everywhere, and it is crucially important to incorporate it in a description of the motion of an $N$ -body system. In fact, non-rotating bodies are about as rare as a relativist at a biophysics convention, and failure to account for rotation would be a significant shortcoming. In atomic, nuclear, and particle physics, the effects of quantum-mechanical spin are known to be of central importance. In gravitational physics, it is becoming increasingly clear that spin effects play a similarly central role in such phenomena as binary black-hole inspirals, gravitational collapse, accretion onto compact objects, and the emission of gravitational radiation. In addition, several key experimental tests of general relativity have involved the effects of spin. By spin, of course, we mean the macroscopic rotation of an extended body, and not the quantum-mechanical spin of an elementary particle. We will use the term “spin” to describe the intrinsic (as opposed to orbital) angular momentum of a rotating body, and will refer to spin–orbit and spin–spin effects in the orbital motion of an $N$ -body system; these effects are purely classical, but they have direct analogues in quantum physics.

In this section we compute the inter-body metric of a system of spinning bodies, obtain the equations of motion for the center-of-mass positions of each body, derive evolution equations for the intrinsic angular momentum of each body, and examine issues associated with the choice of center-of-mass.

# 9.5.1 Definitions of spin

The intrinsic angular-momentum tensor (or spin tensor) of a rotating body was defined back in Eq. (9.9b),

$$
S _ { A } ^ { j k } : = \int _ { A } \rho ^ { * } \big ( \bar { x } ^ { j } \bar { v } ^ { k } - \bar { x } ^ { k } \bar { v } ^ { j } \big ) d ^ { 3 } \bar { x } ,
$$

in which $\bar { \pmb { x } } : = \pmb { x } - \pmb { r } _ { A }$ is the position of a fluid element relative to the body’s center-of-mass, and $\pmb { \bar { v } } : = \pmb { v } - \pmb { v } _ { A }$ is its relative velocity. We may also introduce a vectorial version of the spin angular momentum, defined by

$$
\pmb { S } _ { A } : = \int _ { A } \rho ^ { * } \pmb { \bar { x } } \times \pmb { \bar { v } } d ^ { 3 } \tau
$$

It is easy to show that the tensor and vector are related by

$$
S _ { A } ^ { j } = \frac 1 2 \epsilon ^ { j p q } S _ { A } ^ { p q } , \qquad S _ { A } ^ { j k } = \epsilon ^ { j k p } S _ { A } ^ { p } .
$$

In the rest of the section we frequently go back and forth between the vectorial and tensorial notions of intrinsic angular momentum.

We continue to assume that our bodies are in dynamical equilibrium, and the virial identity of Eq. (9.28a) implies that the spin tensor can also be expressed as

$$
{ S _ { A } ^ { j k } = 2 \int _ { A } \rho ^ { * } \bar { x } ^ { j } \bar { v } ^ { k } d ^ { 3 } \bar { x } } .
$$

It is important to understand that this relation holds in dynamical equilibrium only; the definition of Eq. (9.167) is completely general.

We shall have occasion, below, to refine the definition of the spin vector by the inclusion of post-Newtonian terms at order $c ^ { - 2 }$ . Our final definition of the spin vector is

$$
\bar { S } _ { A } ^ { j } = S _ { A } ^ { j } + \Delta _ { \mathrm { i n t } } S _ { A } ^ { j } + \Delta _ { \mathrm { e x t } } S _ { A } ^ { j } ,
$$

in which

$$
\begin{array} { c } { { \Delta _ { \mathrm { i n t } } S _ { A } ^ { j } : = \displaystyle \frac { 1 } { c ^ { 2 } } \epsilon ^ { j p q } \biggl [ \int _ { A } \rho ^ { * } \bar { x } ^ { p } \bar { v } ^ { q } \left( \frac { 1 } { 2 } \bar { v } ^ { 2 } + 3 U _ { A } + \Pi + \frac { p } { \rho ^ { * } } \right) d ^ { 3 } \bar { x } } } \\ { { - \displaystyle \int _ { A } \rho ^ { * } \bar { x } ^ { p } \left( 4 U _ { A } ^ { q } + \frac { 1 } { 2 } \partial _ { t q } X _ { A } \right) d ^ { 3 } \bar { x } \biggr ] } } \end{array}
$$

is a post-Newtonian correction that originates from the body’s internal motion and gravitational potentials, and

$$
\Delta _ { \mathrm { e x t } } S _ { A } ^ { j } : = \frac { 1 } { c ^ { 2 } } \bigg [ \big ( v _ { A } ^ { 2 } + 3 U _ { \neg A } \big ) S _ { A } ^ { j } - \frac { 1 } { 2 } ( \pmb { v } _ { A } \cdot \pmb { S } _ { A } ) v _ { A } ^ { j } \bigg ]
$$

is another correction that originates from the orbital motion and external Newtonian potential. We shall motivate these post-Newtonian additions below, but for the time being we proceed with the original definition of Eqs. (9.167) and (9.168).

# 9.5.2 Equilibrium conditions

To prepare the way for our subsequent computations, we revisit the equilibrium conditions of Sec. 9.1.3 to see how they must be amended to account for spin. It is easy to see that the only affected condition is Eq. (9.11), which becomes

$$
4 H _ { A } ^ { ( j k ) } - 3 K _ { A } ^ { j k } + \delta ^ { j k } \dot { P } _ { A } - 2 L _ { A } ^ { ( j k ) } + S _ { A } ^ { p ( j } \partial _ { p } ^ { k ) } U _ { - A } ( \pmb { r } _ { A } ) = O ( c ^ { - 2 } )
$$

in the presence of spin.

To establish this generalized form of the equilibrium condition, we return to the virial identity of Eq. (9.28c), which is exact and requires no modification to account for spin. In the no-spin context of Sec. 9.1.3, the terms involving the external Newtonian potential $U _ { \neg A }$ could be neglected, as they give rise to contributions of fractional order $( R _ { A } / r _ { A B } ) ^ { 2 } \ll 1$ to the equilibrium condition. In our current context, however, these terms contain spin contributions that must be identified and included in the equilibrium condition.

The first term to examine is

$$
A ^ { j k } : = \int _ { A } \rho ^ { * } \bar { x } ^ { j } \frac { d } { d t } \partial _ { k } U _ { \ l \ l \ l \ l } d ^ { 3 } \bar { x } .
$$

We follow the familiar method of expressing the external potential as a Taylor expansion about $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ , inserting the expansion inside the integral, evaluating the result, and discarding terms that are suppressed by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 }$ . In the current case we have

$$
\frac { d } { d t } \partial _ { k } U _ { \mathrm { - } A } ( { \pmb x } ) = \frac { d } { d t } \partial _ { k } U _ { \mathrm { - } A } ( { \pmb r } _ { A } ) + \bar { \nu } ^ { p } \partial _ { p k } U _ { \mathrm { - } A } ( { \pmb r } _ { A } ) + \bar { \nu } ^ { p } \frac { d } { d t } \partial _ { p k } U _ { \mathrm { - } A } ( { \pmb r } _ { A } ) + \cdots ,
$$

in which $d / d t$ on the right-hand side is to be interpreted as $\partial _ { t } + v _ { A } ^ { q } \partial _ { q }$ , and the spatial derivatives act on the variables $r _ { A }$ . Only the second term contributes to $A ^ { j k }$ , and making use of Eq. (9.170), we find that

$$
A ^ { j k } = - \frac 1 2 S _ { A } ^ { p j } \partial _ { p k } U _ { \neg A } ( \pmb { r } _ { A } ) .
$$

The second term to examine is

$$
B ^ { j k } : = 3 \int _ { A } \bar { v } ^ { j } \partial _ { k } U _ { \neg A } d ^ { 3 } \bar { x } ,
$$

and its evaluation proceeds along similar lines. In this case we find

$$
B ^ { j k } = \frac { 3 } { 2 } S _ { A } ^ { p j } \partial _ { p k } U _ { \neg A } ( \pmb { r } _ { A } ) ,
$$

and inclusion of these terms in Eq. (9.28c) gives rise to the modified equilibrium condition of Eq. (9.174).

# 9.5.3 Inter-body metric of spinning bodies

Our first task is to re-calculate the inter-body metric of an $N$ -body system to account for the spin of the bodies. We follow the general methods introduced in Sec. 9.2, but now retain the terms that used to vanish under the no-spin condition. The idea is to expand the gravitational potentials about the center-of-mass of each body, and to find the terms that combine an $\bar { x } ^ { j }$ with a $\bar { v } ^ { k }$ so as to give rise to a spin tensor $S _ { A } ^ { j k }$ under Eq. (9.170). Terms of higher order in $\bar { x } ^ { j }$ , such as $\bar { v } ^ { j } \bar { x } ^ { k } \bar { x } ^ { m } \bar { x } ^ { n }$ or $\bar { v } ^ { j } \bar { v } ^ { k } \bar { x } ^ { m } \bar { x } ^ { n }$ , are discarded, because they give rise to negligible contributions of fractional order $( R _ { A } / s _ { A } ) ^ { 2 } \ll 1$ to the potentials. In this spirit, we also neglect terms in the potentials that are quadratic in the body spins.

Going over the computations of Sec. 9.2, we see that spin terms will appear in the post-Newtonian potentials $U ^ { j } , \Phi _ { 1 }$ , and $\Phi _ { 6 }$ , but that the remaining potentials are not affected. Straightforward computations reveal that the additional spin terms are given by

$$
\begin{array} { l } { { \displaystyle \Delta U ^ { j } = - \frac { 1 } { 2 } \sum _ { \cal A } \frac { G S _ { \cal A } ^ { j k } n _ { \cal A } ^ { k } } { s _ { \cal A } ^ { 2 } } , } } \\ { { \displaystyle \Delta \Phi _ { 1 } = - \sum _ { \cal A } \frac { G v _ { \cal A } ^ { j } S _ { \cal A } ^ { j k } n _ { \cal A } ^ { k } } { s _ { \cal A } ^ { 2 } } , } } \\ { { \displaystyle \Delta \Phi _ { 6 } = - \sum _ { \cal A } \frac { G v _ { \cal A } ^ { j } S _ { \cal A } ^ { j k } n _ { \cal A } ^ { k } } { s _ { \cal A } ^ { 2 } } , } } \end{array}
$$

in which $\pmb { s } _ { A } : = \pmb { x } - \pmb { r } _ { A }$ , $s _ { A } : = | \pmb { s } _ { A } |$ , and $\pmb { n } _ { A } : = \pmb { s } _ { A } / s _ { A }$ . These results imply that the main post-Newtonian potential $\Psi$ is changed by

$$
\Delta \Psi = - \frac { 3 } { 2 } \sum _ { A } \frac { G v _ { A } ^ { j } S _ { A } ^ { j k } n _ { A } ^ { k } } { s _ { A } ^ { 2 } } .
$$

These results are expressed in terms of the spin tensor. Transforming to the spin vector, we have that $S _ { A } ^ { j k } n _ { A } ^ { k } = ( \pmb { n } _ { A } \times \pmb { S } _ { A } ) ^ { j }$ and $v _ { A } ^ { j } S _ { A } ^ { j k } n _ { A } ^ { \bar { k } } = - ( \pmb { n } _ { A } \times \pmb { v } _ { A } ) \cdot \pmb { S } _ { A }$ .

Inserting the potentials within the metric of Eq. (9.44), we find that the changes to the inter-body metric are given by

$$
\begin{array} { l } { \Delta g _ { 0 0 } = \displaystyle \frac { 3 } { c ^ { 4 } } \sum _ { A } \frac { G ( \pmb { n } _ { A } \times \pmb { v } _ { A } ) \cdot \pmb { S } _ { A } } { s _ { A } ^ { 2 } } + O ( c ^ { - 6 } ) , } \\ { \Delta g _ { 0 j } = \displaystyle \frac { 2 } { c ^ { 3 } } \sum _ { A } \frac { G ( \pmb { n } _ { A } \times \pmb { S } _ { A } ) ^ { j } } { s _ { A } ^ { 2 } } + O ( c ^ { - 5 } ) , } \\ { \Delta g _ { j k } = O ( c ^ { - 4 } ) . } \end{array}
$$

These additional terms affect the motion of test masses around each body, and we shall see that spin effects also modify the center-of-mass motion of each body within the system.

To illustrate the gravitational influence of spin on a test mass, we specialize the metric to a single body. We place the body at $\pmb { r } _ { A } = \pmb { 0 }$ , set $\pmb { v } _ { A } = \pmb { 0 }$ , and import the additional terms

from Eq. (9.81). The metric becomes

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 } { c ^ { 2 } } \displaystyle \frac { G M } { r } - \displaystyle \frac { 2 } { c ^ { 4 } } \biggl ( \displaystyle \frac { G M } { r } \biggr ) ^ { 2 } + { \cal O } ( c ^ { - 6 } ) , } } \\ { { g _ { 0 j } = \displaystyle \frac { 2 } { c ^ { 3 } } \displaystyle \frac { G ( { \bf x } \times { \bf S } ) ^ { j } } { r ^ { 3 } } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { g _ { j k } = \biggl ( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } \displaystyle \frac { G M } { r } \biggr ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

in which $M$ is the body’s mass, $s$ its spin vector, and $r : = | { \boldsymbol { x } } |$ . We examine the geodesic motion of a test particle in this spacetime. We describe the motion in terms of the position vector $\mathbf { } r ( t )$ , and we recall from Sec. 5.2.3 (see Eq. (5.52)) that the motion follows from the Lagrangian ${ \cal L } = - m c \sqrt { - g _ { \alpha \beta } v ^ { \alpha } v ^ { \beta } }$ , in which $m$ is the particle’s mass and $\boldsymbol { v } ^ { \alpha } = ( c , \pmb { v } )$ with ${ \pmb v } = d { \pmb r } / d t$ . Making the substitutions, and keeping only the Newtonian and spin terms in the Lagrangian, we find that it is given approximately by

$$
L = - m c ^ { 2 } + { \frac { 1 } { 2 } } m v ^ { 2 } + { \frac { G m M } { r } } - { \frac { 2 G m ( { \pmb x } \times { \pmb v } ) \cdot { \pmb S } } { c ^ { 2 } r ^ { 3 } } } .
$$

Aligning the spin direction with the $z$ -axis, and expressing the Lagrangian in spherical polar coordinates, we obtain our final expression

$$
L = - m c ^ { 2 } + { \frac { 1 } { 2 } } m { \left( { \dot { r } } ^ { 2 } + r ^ { 2 } { \dot { \theta } } ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta { \dot { \phi } } ^ { 2 } \right) } + { \frac { G m M } { r } } - { \frac { 2 G m S \sin ^ { 2 } \theta { \dot { \phi } } } { c ^ { 2 } r } } ,
$$

in which an overdot indicates differentiation with respect to $t$ .

The Lagrangian implies the existence of a conserved angular momentum,

$$
h : = \frac { 1 } { m } \frac { \partial L } { \partial \dot { \phi } } = r ^ { 2 } \sin ^ { 2 } \theta \bigg ( \dot { \phi } - \frac { 2 G S } { c ^ { 2 } r ^ { 3 } } \bigg ) ,
$$

and this equation captures the essential features of motion around a spinning body. Consider a particle released from rest at infinity. The particle has no angular momentum, $h = 0$ , but when it reaches a position $r$ , it has nevertheless acquired an angular velocity $2 G S / ( c ^ { 2 } r ^ { 3 } )$ . A particle with no angular momentum is therefore compelled to rotate in the same direction as the spinning body, as if it were dragged along by the rotational motion of the central body. Conversely, a test particle with a vanishing angular velocity at a position $r$ has a negative angular momentum, $h = - 2 G S \sin ^ { 2 } \theta / ( c ^ { 2 } r )$ , as if it were counter-rotating relative to the local spacetime. In the spacetime of a rotating body, therefore, zero angular momentum does not imply zero angular velocity, and zero angular velocity does not imply zero angular momentum. The phrase dragging of inertial frames is often attached to these phenomena. We return to the observable consequences of frame dragging in Chapter 10.

# 9.5.4 Spin–orbit and spin–spin accelerations

We next turn to the task of calculating the center-of-mass acceleration ${ \pmb a } _ { A }$ of a spinning body. Our strategy here is identical to the one adopted in Sec. 9.3. First, we insert the

post-Newtonian Euler equation within the definition

$$
m _ { A } \pmb { a } _ { A } = \int _ { A } \rho ^ { * } \frac { d \pmb { v } } { d t } d ^ { 3 } \pmb { x }
$$

and evaluate the resulting integrals, as listed in Eqs. (9.88). Second, we invoke the equilibrium conditions of Secs. 9.1.3 and 9.5.2 to eliminate all terms that depend on the body’s internal structure. And third, we evaluate the external potentials and their derivatives at the position of each body. As we shall show below, the final result of this computation is the expression

$$
{ \bf \delta } a _ { \scriptscriptstyle A } = { \bf \delta } a _ { \scriptscriptstyle A } [ 0 \mathrm { p N } ] + { \bf \delta } a _ { \scriptscriptstyle A } [ 1 \mathrm { p N } ] + { \bf \delta } a _ { \scriptscriptstyle A } [ \mathrm { s o } ] + { \bf \delta } a _ { \scriptscriptstyle A } [ \mathrm { s s } ] + O ( c ^ { - 4 } ) ,
$$

in which the Newtonian and post-Newtonian terms are given by Eq. (9.127),

$$
\begin{array} { c } { { a _ { \cal A } ^ { j } [ { \sf s o } ] = \displaystyle \frac { 3 } { 2 c ^ { 2 } } \sum _ { B \not = { \cal A } } \frac { G M _ { B } } { r _ { A B } ^ { 3 } } \Biggl \{ n _ { A B } ^ { \langle j k \rangle } \biggl [ v _ { A } ^ { p } \bigl ( 3 \hat { S } _ { A } ^ { k p } + 4 \hat { S } _ { B } ^ { k p } \bigr ) - v _ { B } ^ { p } \bigl ( 3 \hat { S } _ { B } ^ { k p } + 4 \hat { S } _ { A } ^ { k p } \bigr ) \biggr ] } } \\ { { { } } } \\ { { + n _ { A B } ^ { \langle k p \rangle } ( v _ { A } - v _ { B } ) ^ { p } \bigl ( 3 \hat { S } _ { A } ^ { j k } + 4 \hat { S } _ { B } ^ { j k } \bigr ) \Biggr \} } } \end{array}
$$

is the spin–orbit acceleration, which is linear in each spin tensor, and

$$
a _ { \scriptscriptstyle A } ^ { j } [ \mathrm { s s } ] = - \frac { 1 5 } { c ^ { 2 } } \sum _ { B \not = A } \frac { G M _ { B } } { r _ { \scriptscriptstyle A B } ^ { 4 } } \hat { S } _ { A } ^ { k p } \hat { S } _ { B } ^ { k q } n _ { \scriptscriptstyle A B } ^ { \langle j p q \rangle }
$$

is the spin–spin acceleration, bilinear in the spins. We recall the symbols $r _ { A B } : = r _ { A } - r _ { B }$ , $r _ { A B } : = | \pmb { r } _ { A B } | , \pmb { n } _ { A B } : = { \pmb { r } _ { A B } } / { r _ { A B } }$ , that angular brackets such as $\langle j p q \rangle$ indicate a symmetrictracefree combination, and we have introduced

$$
\hat { S } _ { A } ^ { j k } : = \frac { 1 } { M _ { A } } S _ { A } ^ { j k }
$$

to denote the spin tensor divided by the body’s total mass-energy $M _ { A }$ .

To arrive at Eq. (9.188) we return to the listing of partial forces in Eqs. (9.88) and identify the ones that produce a dependence upon spin. It is easy to see that $F _ { 6 } ^ { j }$ $, F _ { 8 } ^ { j } , F _ { 9 } ^ { j } , F _ { 1 1 } ^ { j }$ , and $F _ { 1 2 } ^ { j }$ all contain terms proportional to $S _ { A } ^ { j k }$ , and that $F _ { 1 0 } ^ { j } , \dot { F _ { 1 1 } ^ { j } } , F _ { 1 2 } ^ { j } , F _ { 1 3 } ^ { j }$ 6 , and $F _ { 1 8 } ^ { j }$ 9 11contain terms proportional to $S _ { B } ^ { j k }$ contributed by the external potentials $U _ { \neg A } ^ { j }$ , $\Phi _ { 1 , \lnot A }$ , and $\Phi _ { 6 , \lnot A }$ .

Making use of the calculational tools developed in Sec. 9.3.2, we find that the first group of terms evaluates to

$$
\begin{array} { r l } & { c ^ { 2 } \Delta F _ { 6 } ^ { j } = - v _ { A } ^ { k } S _ { A } ^ { k p } \partial _ { p j } U _ { - , 4 } , } \\ & { c ^ { 2 } \Delta F _ { 8 } ^ { j } = \frac { 3 } { 2 } S _ { A } ^ { j p } \partial _ { t p } U _ { - , 4 } , } \\ & { c ^ { 2 } \Delta F _ { 9 } ^ { j } = 2 v _ { A } ^ { k } S _ { A } ^ { j p } \partial _ { k p } U _ { - , 4 } , } \\ & { c ^ { 2 } \Delta F _ { 1 1 } ^ { j } = 0 , } \\ & { c ^ { 2 } \Delta F _ { 1 2 } ^ { j } = 2 S _ { A } ^ { k p } \partial _ { j p } U _ { - , 4 } ^ { k } , } \end{array}
$$

in which the external potentials are evaluated at $r _ { A }$ after differentiation. The second group of terms is

$$
\begin{array} { l } { { { c ^ { 2 } \Delta F _ { 1 0 } ^ { j } = 4 m _ { _ { A } } \Delta \partial _ { t } U _ { - , d } ^ { j } , } } } \\ { { { c ^ { 2 } \Delta F _ { 1 1 } ^ { j } = 4 m _ { _ { A } } v _ { _ A } ^ { k } \Delta \partial _ { k } U _ { - , d } ^ { j } , } } } \\ { { { c ^ { 2 } \Delta F _ { 1 2 } ^ { j } = - 4 m _ { _ { A } } v _ { _ A } ^ { k } \Delta \partial _ { j } U _ { - , d } ^ { k } , } } } \\ { { { c ^ { 2 } \Delta F _ { 1 3 } ^ { j } = 2 m _ { _ { A } } \Delta \partial _ { j } \Phi _ { 1 , - , d } , } } } \\ { { { c ^ { 2 } \Delta F _ { 1 8 } ^ { j } = - { \frac { 1 } { 2 } } m _ { _ { A } } \Delta \partial _ { j } \Phi _ { 6 , - , d } , } } } \end{array}
$$

in which, for example, $\Delta \partial _ { k } U _ { \lnot A } ^ { j }$ denotes the spin-dependent terms in the gradient of the external vector potential. In addition to these contributions we must also account for the spin-dependent term in the equilibrium condition of Eq. (9.174), which, according to Eq. (9.100), gives rise to the shift

$$
c ^ { 2 } \Delta F ^ { j } = \Delta \big ( 2 L _ { A } ^ { ( j k ) } - 4 H _ { A } ^ { ( j k ) } + 3 K _ { A } ^ { j k } - \delta ^ { j k } \dot { P } _ { A } \big ) v _ { A } ^ { k } = v _ { A } ^ { k } S _ { A } ^ { p ( k } \partial _ { p } ^ { j ) } U _ { \neg A } .
$$

In the next step we employ the methods described in Sec. 9.3.4 to evaluate the derivatives of external potentials that occur in Eqs. (9.192), (9.193), and (9.194). We have

$$
\begin{array} { r l } & { \lambda _ { x } \mu _ { x + 1 } ^ { \mathrm { r e q } } = \lambda _ { x } \frac { \cosh \cosh \cosh \cosh \cosh } { \cosh \cosh \cosh } , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

Making the substitutions and adding up the partial forces, we finally obtain the spin–orbit and spin–spin accelerations of Eqs. (9.189) and (9.190). In the last step we make the replacement $m _ { A }  M _ { A } + O ( c ^ { - 2 } )$ in the accelerations, so as to express them in terms of the total mass-energy $M _ { A }$ instead of the material mass $m _ { A }$ .

# 9.5.5 Conserved quantities

The conserved quantities of Sec. 9.3.6 also acquire spin-dependent terms. While it is easy to see that the total mass-energy $M$ is spin-independent, a close examination of Eqs. (9.129) and (9.131) reveals that the center-of-mass position $\pmb { R }$ and total momentum $P$ contain spin terms. In the case of the center-of-mass position, these contributions originate from the term $\scriptstyle { \frac { 1 } { 2 } } \rho ^ { * } x ^ { j } v ^ { 2 }$ inside the integral. In the case of the total momentum, they arise from $\rho ^ { * } v ^ { j } U$ and $\rho ^ { * } \Phi ^ { j }$ .

We calculate the spin-dependent terms by following the approach detailed in Sec. 9.3.6, and obtain

$$
\Delta ( M R ^ { j } ) = \frac { 1 } { 2 c ^ { 2 } } \sum _ { A } S _ { A } ^ { j k } v _ { A } ^ { k } = \frac { 1 } { 2 c ^ { 2 } } \sum _ { A } \bigl ( \pmb { v } _ { A } \times \pmb { S } _ { A } \bigr ) ^ { j }
$$

for the change in the barycenter position, and

$$
\Delta P ^ { j } = - { \frac { 1 } { 2 c ^ { 2 } } } \sum _ { A } \sum _ { B \neq A } { \frac { G M _ { B } } { r _ { A B } ^ { 2 } } } S _ { A } ^ { j k } n _ { A B } ^ { k } = - { \frac { 1 } { 2 c ^ { 2 } } } \sum _ { A } \sum _ { B \neq A } { \frac { G M _ { B } } { r _ { A B } ^ { 2 } } } { \left( n _ { A B } \times S _ { A } \right) } ^ { j }
$$

for the change in the total momentum. It is easy to show that $d \Delta ( M R ) / d t = \Delta P + O ( c ^ { - 4 } )$ and $d \Delta P / d t = { \cal O } ( c ^ { - 4 } )$ provided that $d S _ { A } ^ { j k } / \dot { d t } = O ( c ^ { - 2 } )$ .

# 9.5.6 Spin precession

Our next task in this survey of spinning bodies is to derive an evolution equation for each spin vector $\pmb { S } _ { A }$ . This question was first considered back in Sec. 1.6.8 in the context of Newtonian gravity, where we showed that $\pmb { S } _ { A }$ changes as a result of a coupling between the body’s multipole moments $I _ { A } ^ { L }$ and inhomogeneities in the external Newtonian potential $U _ { \neg A }$ . We have so far neglected all effects associated with multipole moments, and we shall continue to do so in our treatment of spin evolution. As a result, we shall find that the changes in $\pmb { S } _ { A }$ occur at post-Newtonian order, and result from a coupling between the body’s spin and gradients of the external potentials.

Our final expression of the spin evolution equation involves the refined spin vector of Eq. (9.171). It takes the form of the precession equation

$$
\frac { d \bar { \pmb { S } } _ { A } } { d t } = \pmb { \Omega } _ { A } \times \bar { \pmb { S } } _ { A } + O ( c ^ { - 4 } ) ,
$$

in which the precessional angular velocity is given by

$$
\Omega _ { \cal A } = \Omega _ { \cal A } [ \mathrm { s o } ] + \Omega _ { \cal A } [ \mathrm { s s } ] ,
$$

with

$$
\Omega _ { \scriptscriptstyle A } [ \mathrm { s o } ] = \frac { 1 } { 2 c ^ { 2 } } \sum _ { B \not = A } \frac { G M _ { B } } { r _ { \scriptscriptstyle A B } ^ { 2 } } { \pmb { n } } _ { A B } \times \bigl ( 3 { \pmb { v } } _ { A } - 4 { \pmb { v } } _ { B } \bigr ) ,
$$

$$
\Omega _ { \cal A } [ \mathrm { s s } ] = \frac { 1 } { c ^ { 2 } } \sum _ { B \neq { \cal A } } \frac { G } { r _ { A B } ^ { 3 } } \biggl [ 3 \bigl ( \bar { \bf S } _ { B } \cdot { \pmb n } _ { A B } \bigr ) { \pmb n } _ { A B } - \bar { \bf S } _ { B } \biggr ] .
$$

The first term describes a spin–orbit interaction, and the second a spin–spin interaction. Equation (9.198) implies that the magnitude $| \bar { \pmb S } _ { A } |$ of the spin vector is a constant of the motion; the equation describes a precession of the spin around the time-dependent angularvelocity vector $\pmb { \Omega } _ { A }$ .

The spin-precession equation involves the refined spin vector $\bar { \pmb S } _ { A }$ instead of the original vector $\pmb { S } _ { A }$ , but the inter-body metric and equations of motion were previously written in terms of the original spin. There is no obstacle, however, in expressing all previous results in terms of the refined spin. Because ${ \pmb S } _ { A } = \bar { \pmb S } _ { A } + O ( c ^ { - 2 } )$ , and because all spin terms occur at post-Newtonian order in the metric and equations of motion, the substitution affects only the neglected terms at $2 \mathrm { P N }$ order. The final expression of our results, therefore, involves only the refined spin vector.

# Partial torques

The derivation of Eq. (9.198) begins with

$$
\frac { d S _ { A } ^ { j } } { d t } = \epsilon ^ { j p q } \int _ { A } \rho ^ { * } \bar { x } ^ { p } \frac { d v ^ { q } } { d t } d ^ { 3 } \bar { x } ,
$$

which is obtained by straightforward differentiation of Eq. (9.168); the integral initially features $d \bar { v } ^ { p } / d t = d v ^ { p } / d t - a _ { A } ^ { j }$ , but the center-of-mass condition $\textstyle \int _ { A } \rho ^ { * } { \bar { x } } ^ { p } d ^ { 3 } { \bar { x } } = 0$ implies that the second term leads to a vanishing contribution to the torque. In this we insert the post-Newtonian version of Euler’s equation and end up with a sum of terms that bears a close resemblance to Eq. (9.86). For our purposes here it is helpful to write the Euler equation – refer to Eq. (8.119) – in the alternative form

$$
\begin{array} { c c } { \rho ^ { \ast } \displaystyle \frac { d v ^ { j } } { d t } = - \partial _ { j } p + \rho ^ { \ast } \partial _ { j } U + \displaystyle \frac { 1 } { c ^ { 2 } } \Bigg \lbrace \Bigg ( \displaystyle \frac { 1 } { 2 } v ^ { 2 } + U + \Pi + \displaystyle \frac { p } { \rho ^ { \ast } } \Bigg ) \partial _ { j } p - v ^ { j } \partial _ { t } p } \\ { + \rho ^ { \ast } \bigg [ ( v ^ { 2 } - 4 U ) \partial _ { j } U - 3 v ^ { j } \displaystyle \frac { d U } { d t } - v ^ { j } v ^ { k } \partial _ { k } U + 4 \displaystyle \frac { d U ^ { j } } { d t } - 4 v ^ { k } \partial _ { j } U ^ { k } + \partial _ { j } \Psi \bigg ] \Bigg \rbrace } \\ { + O ( c ^ { - 4 } ) , } & { ( 9 . 2 0 . } \end{array}
$$

in which $\begin{array} { r } { \Psi = \psi + \frac { 1 } { 2 } \partial _ { t t } \boldsymbol { X } } \end{array}$ and $\begin{array} { r } { \psi = \frac { 3 } { 2 } \Phi _ { 1 } - \Phi _ { 2 } + \Phi _ { 3 } + 3 \Phi _ { 4 } } \end{array}$ – refer to Eq. (8.3) and Eq. (8.9). Inserting this within Eq. (9.201), we have that

$$
\frac { d S _ { A } ^ { j } } { d t } = \frac { 1 } { c ^ { 2 } } \epsilon ^ { j p q } \sum _ { n = 1 } ^ { 9 } G _ { n } ^ { p q } + { \cal O } ( c ^ { - 4 } ) ,
$$

where

$$
\begin{array} { l } { { G _ { 1 } ^ { j k } : = \displaystyle \int _ { A } \bar { x } ^ { j } \left( \frac { 1 } { 2 } v ^ { 2 } + U + \Pi + \frac { p } { \rho ^ { * } } \right) \partial _ { k } p d ^ { 3 } \bar { x } , } } \\ { { \ } } \\ { { G _ { 2 } ^ { j k } : = - \displaystyle \int _ { A } \bar { x } ^ { j } v ^ { k } \partial _ { t } p d ^ { 3 } \bar { x } , } } \\ { { \ } } \\ { { G _ { 3 } ^ { j k } : = \displaystyle \int _ { A } \rho ^ { * } \bar { x } ^ { j } ( v ^ { 2 } - 4 U ) \partial _ { k } U d ^ { 3 } \bar { x } , } } \end{array}
$$

$$
\begin{array} { r l } & { G _ { 4 } ^ { j k } : = - 3 \displaystyle \int _ { 4 } \rho ^ { * } \bar { x } ^ { j } \nu ^ { k } \frac { d U } { d t } d ^ { 3 } \bar { x } , } \\ & { G _ { 5 } ^ { j k } : = - \displaystyle \int _ { 4 } \rho ^ { * } \bar { x } ^ { j } \nu ^ { k } \nu ^ { p } \partial _ { P } U d ^ { 3 } \bar { x } , } \\ & { G _ { 6 } ^ { j k } : = 4 \displaystyle \int _ { 4 } \rho ^ { * } \bar { x } ^ { j } \frac { d U ^ { k } } { d t } d ^ { 3 } \bar { x } , } \\ & { G _ { 7 } ^ { j k } : = - 4 \displaystyle \int _ { 4 } \rho ^ { * } \bar { x } ^ { j } \nu ^ { p } \partial _ { k } U ^ { p } d ^ { 3 } \bar { x } , } \\ & { G _ { 8 } ^ { j k } : = \displaystyle \int _ { 4 } \rho ^ { * } \bar { x } ^ { j } \partial _ { k } \psi d ^ { 3 } \bar { x } , } \\ & { G _ { 9 } ^ { j k } : = \frac { 1 } { 2 } \displaystyle \int _ { 4 } \rho ^ { * } \bar { x } ^ { j } \partial _ { k \bar { x } } X d ^ { 3 } \bar { x } , } \end{array}
$$

are the partial torques. As motivated previously, we have discarded the Newtonian terms in Eq. (9.203), and factorized the overall factor of $c ^ { - 2 }$ .

The remaining computations are lengthy, but they proceed along the same lines as the evaluation of the partial forces in Sec. 9.3.2. For example, the velocity vector is decomposed as $\pmb { v } = \pmb { v } _ { A } + \pmb { \bar { v } }$ , the potentials are decomposed into internal and external pieces, the external potentials are expressed as Taylor expansions about $r _ { A }$ , integrals featuring an odd number of internal vectors are set to zero, and terms of fractional order $( R _ { A } / r _ { A B } ) ^ { 2 } \ll 1$ are neglected. In addition, double volume integrals are symmetrized with respect to the integration variables $\bar { x }$ and $\bar { x } ^ { \prime }$ , and all terms in $\bar { G } _ { n } ^ { j k }$ that are symmetric in $j k$ are discarded, because they do not survive the antisymmetrization operation contained in Eq. (9.203). Skipping over these computational details, we obtain

$$
\begin{array} { r l } & { G _ { 1 } ^ { ( k ) } = \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } G _ { 2 } ^ { ( k ) } \dag , \hat { \psi } _ { 1 } ^ { ( k ) } d x , } \\ & { G _ { 2 } ^ { ( k ) } = - \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } G _ { 2 } ^ { ( k ) } \dag , \hat { \psi } _ { 1 } ^ { ( k ) } d x , } \\ & { G _ { 3 } ^ { ( k ) } = \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } G _ { 3 } ^ { ( k ) } G _ { 2 } ^ { ( k ) } \dag , \hat { \psi } _ { 2 } ^ { ( k ) } d x + \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } G _ { 2 } ^ { ( k ) } d x , } \\ & { G _ { 4 } ^ { ( k ) } = - \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } G _ { 2 } ^ { ( k ) } d x , \quad \hat { \psi } _ { 2 } ^ { ( k ) } d x - \frac { 2 } { x ^ { 3 } } \frac { \hat { \psi } _ { 2 } ^ { ( k ) } d x } { \hat { \psi } _ { 1 } } , } \\ &  G _ { 5 } ^ { ( k ) } = - \frac { 3 } { x ^ { 4 } } \frac { 2 } { x ^ { 3 } } \frac { 2 } { x ^ { 5 } } G _ { 2 } ^ { ( k ) } \dag , \hat { \psi } _ { 2 } ^ { ( k ) } d x + \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } \left( \sqrt { \frac { 1 } { x ^ { 3 } } - \frac { 2 } { x ^ { 3 } } } \right) \frac { \hat { \psi } _ { 2 } ^ { ( k ) } ( x , x ) }  \end{array}
$$

in which the external potentials are evaluated at $r _ { A }$ after differentiation. The partial torques involve some external pieces that depend on the spin tensor $S _ { A } ^ { j k }$ , and some internal integrals that are not directly featured in the final result displayed in Eq. (9.198). Many of these integrals actually cancel out, as can be seen for the terms involving the potential energy tensor $\Omega _ { A } ^ { j k }$ .

Other cancellations are produced once we express $G _ { 1 } ^ { j k }$ in a different form. We eliminate $\partial _ { k } p$ from the integral by making use of the Newtonian version of Euler’s equation, which we write in the approximate form $\rho ^ { * } d \bar { v } ^ { k } / d t = - \partial _ { k } p + \rho ^ { * } \partial _ { k } U _ { A }$ , having equated $d v _ { A } ^ { k } / d t$ with $\partial _ { k } U _ { \neg A } ( \pmb { r } _ { A } )$ . The partial torque becomes

$$
\begin{array} { l } { { G _ { 1 } ^ { j k } = \displaystyle - \int _ { A } \rho ^ { * } \bar { x } ^ { j } \left( \displaystyle \frac { 1 } { 2 } \bar { v } ^ { 2 } + 3 U _ { A } + \Pi + \frac { p } { \rho ^ { * } } \right) \displaystyle \frac { d \bar { v } ^ { k } } { d t } d ^ { 3 } \bar { x } + 2 \int _ { A } \rho ^ { * } \bar { x } ^ { j } U _ { A } \displaystyle \frac { d \bar { v } ^ { k } } { d t } d ^ { 3 } \bar { x } } } \\ { { \displaystyle ~ + \int _ { A } \rho ^ { * } \bar { x } ^ { j } \left( \displaystyle \frac { 1 } { 2 } \bar { v } ^ { 2 } + U _ { A } + \Pi + \frac { p } { \rho ^ { * } } \right) \partial _ { k } U _ { A } d ^ { 3 } \bar { x } . } } \end{array}
$$

The integrand of the first term is $\rho ^ { * } \bar { x } ^ { j } A d \bar { v } ^ { k } / d t$ with $\begin{array} { r } { A : = \frac { 1 } { 2 } \bar { v } ^ { 2 } + 3 U _ { A } + \Pi + p / \rho ^ { * } } \end{array}$ , and we express it as

$$
\rho ^ { * } \frac { d } { d t } \big ( \bar { x } ^ { j } \bar { v } ^ { k } A \big ) - \rho ^ { * } \bar { v } ^ { j } \bar { v } ^ { k } A - \rho ^ { * } \bar { x } ^ { j } \bar { v } ^ { k } \frac { d A } { d t } ,
$$

with $d A / d t = ( \partial _ { t } p + v _ { A } ^ { n } \partial _ { n } p ) / \rho ^ { * } + { \bar { v } } ^ { n } \partial _ { n } U _ { A } + 3 d U _ { A } / d t$ ; to arrive at this result we have invoked Euler’s equation once more, and made use of $d \Pi / d t = ( p / \rho ^ { * 2 } ) d \rho ^ { * } / d t$ , the statement of the first law of thermodynamics. We make the substitutions within the first integral in $G _ { A } ^ { j k }$ , and for the second integral we make use of Euler’s equation to express $\bar { x } ^ { j } U _ { A } \partial _ { k } p$ as

$$
\partial _ { k } \big ( \bar { x } ^ { j } p U _ { A } \big ) - \delta ^ { j k } p U _ { A } - \bar { x } ^ { j } p \partial _ { k } U _ { A } ,
$$

with the first term producing a vanishing surface integral. Collecting results, we obtain

$$
\begin{array} { l } { { G _ { 1 } ^ { j k } = \displaystyle - \frac { d } { d t } \int _ { A } \rho ^ { * } \bar { x } ^ { j } \bar { v } ^ { k } \biggl ( \frac { 1 } { 2 } \bar { v } ^ { 2 } + 3 U _ { A } + \Pi + \frac { p } { \rho ^ { * } } \biggr ) d ^ { 3 } \bar { x } + \int _ { A } \bar { x } ^ { j } \bar { v } ^ { k } \partial _ { t } p d ^ { 3 } \bar { x } ~ } } \\ { { \displaystyle ~ + \int _ { A } \rho ^ { * } \bar { x } ^ { j } \bar { v } ^ { k } \bar { v } ^ { p } \partial _ { p } U _ { A } d ^ { 3 } \bar { x } + 3 \int _ { A } \rho ^ { * } \bar { x } ^ { j } \bar { v } ^ { k } \frac { d U _ { A } } { d t } d ^ { 3 } \bar { x } } } \\ { { \displaystyle ~ + \int _ { A } \rho ^ { * } \bar { x } ^ { j } \biggl ( \frac { 1 } { 2 } \bar { v } ^ { 2 } + 3 U _ { A } + \Pi + 3 \frac { p } { \rho ^ { * } } \biggr ) \partial _ { k } U _ { A } d ^ { 3 } \bar { x } , } } \end{array}
$$

and recognize some of the internal integrals that were encountered previously.

# Internal and external torques

Summing over the partial torques, we find that the internal pieces collect themselves into

$$
\begin{array} { c } { { G _ { \mathrm { i n t } } ^ { j k } = \displaystyle - \frac { d } { d t } \biggl [ \int _ { \cal A } \rho ^ { \ast } \bar { x } ^ { j } \bar { v } ^ { k } \biggl ( \frac { 1 } { 2 } \bar { v } ^ { 2 } + 3 U _ { A } + \Pi + \frac { p } { \rho ^ { \ast } } \biggr ) d ^ { 3 } \bar { x } } } \\ { { - \displaystyle \int _ { \cal A } \rho ^ { \ast } \bar { x } ^ { j } \biggl ( 4 U _ { A } ^ { k } + \frac { 1 } { 2 } \partial _ { t k } X _ { A } \biggr ) d ^ { 3 } \bar { x } \biggr ] } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { l } { { \displaystyle - G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \bar { x } ^ { j } \left( \frac { 3 } { 2 } \bar { v } ^ { 2 } - U _ { A } + \Pi + 3 \frac { p } { \rho ^ { * } } \right) \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } } }  \\ { { \displaystyle - G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \bar { x } ^ { j } \left( \frac { 3 } { 2 } \bar { v } ^ { \prime 2 } - U _ { A } ^ { \prime } + \Pi ^ { \prime } + 3 \frac { p ^ { \prime } } { \rho ^ { * \prime } } \right) \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x } . } }  \end{array}
$$

The last term can be re-expressed as

$$
+ G \int _ { A } \rho ^ { * } \rho ^ { * \prime } \bar { x } ^ { \prime } { } ^ { j } \Bigg ( \frac 3 2 \bar { v } ^ { 2 } - U _ { A } + \Pi + 3 \frac { p } { \rho ^ { * } } \Bigg ) \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } d ^ { 3 } \bar { x }
$$

and combined with the previous integral to give something symmetric in $j k$ . Discarding this, we find that the internal pieces give rise to a total time derivative that can be moved to the left-hand side of Eq. (9.203) and absorbed into a re-definition of the spin vector. This is the origin of the term $\Delta _ { \mathrm { i n t } } S _ { A } ^ { j }$ in Eq. (9.171).

With the redefinition $\bar { S } _ { A } ^ { j } : = S _ { A } ^ { j } + \Delta _ { \mathrm { i n t } } S _ { A } ^ { j }$ , which for the moment excludes the external shift also present in Eq. (9.171), we find that the spin-evolution equation becomes

$$
{ \frac { d \bar { S } _ { A } ^ { j } } { d t } } = { \frac { 1 } { c ^ { 2 } } } \epsilon ^ { j p q } G _ { \mathrm { e x t } } ^ { p q } + { \cal O } ( c ^ { - 4 } )
$$

with

$$
\begin{array} { l } { { G _ { \mathrm { e x t } } ^ { j k } : = \bar { S } _ { A } ^ { j p } v _ { A } ^ { p } \partial _ { k } U _ { - A } - 2 \bar { S } _ { A } ^ { j p } v _ { A } ^ { k } \partial _ { p } U _ { - A } - \displaystyle { \frac { 1 } { 2 } } \bar { S } _ { A } ^ { j k } v _ { A } ^ { p } \partial _ { p } U _ { - A } - \frac { 3 } { 2 } \bar { S } _ { A } ^ { j k } \frac { d U _ { - A } } { d t } } } \\ { { \qquad + 2 \bar { S } _ { A } ^ { j p } \big ( \partial _ { p } U _ { - A } ^ { k } - \partial _ { k } U _ { - A } ^ { p } \big ) , } } \end{array}
$$

in which the original spin tensor $S _ { A } ^ { j k }$ has been replaced by its refinement $\bar { S } _ { A } ^ { j k } = S _ { A } ^ { j k } +$ $O ( c ^ { - 2 } )$ . Our expression for $G _ { \mathrm { e x t } } ^ { j k }$ A A A is not unique, because we may again collect some of its terms in a total time derivative that can be moved to the left-hand side of the spin-evolution equation. We can use this freedom judiciously to ensure that the resulting equation takes the form of a precession equation, as we have it in Eq. (9.198). In these manipulations we use the fact that $d \bar { S } _ { A } ^ { j k } / d t = O ( c ^ { - 2 } )$ , as well as the Newtonian equations of motion $d v _ { A } ^ { j } / d t = \partial _ { j } U _ { \neg { A } } ( \pmb { r } _ { A } ) + \stackrel {  } { O } ( c ^ { - 2 } )$ . For example, the $v _ { A } ^ { p } \partial _ { p } U _ { \lnot A }$ factor in the third term of Eq. (9.210) can be written as

$$
v _ { A } ^ { p } \partial _ { p } U _ { \lnot A } = v _ { A } ^ { p } \frac { d v _ { A } ^ { p } } { d t } = \frac { 1 } { 2 } \frac { d } { d t } \big ( v _ { A } ^ { 2 } \big ) ,
$$

and this term can indeed be expressed as a total time derivative. As another example, we have

$$
v _ { A } ^ { k } \partial _ { p } U _ { \lnot A } = \frac { d } { d t } \big ( v _ { A } ^ { k } v _ { A } ^ { p } \big ) - v _ { A } ^ { p } \partial _ { k } U _ { \lnot A } ,
$$

and the substitution can be made in the second term of Eq. (9.210). After simplification we find that our new expression for $G _ { \mathrm { e x t } } ^ { j k }$ becomes

$$
\begin{array} { l } { { \displaystyle G _ { \mathrm { e x t } } ^ { j k } = - \frac { d } { d t } \bigg ( \frac { 1 } { 2 } \bar { S } _ { A } ^ { j p } v _ { A } ^ { k } v _ { A } ^ { p } + \frac { 1 } { 4 } \bar { S } _ { A } ^ { j k } v _ { A } ^ { 2 } + \frac { 3 } { 2 } \bar { S } _ { A } ^ { j k } U _ { - A } \bigg ) } } \\ { { \displaystyle \qquad + \frac { 3 } { 2 } \bar { S } _ { A } ^ { j p } \big ( v _ { A } ^ { p } \partial _ { k } U _ { - A } - v _ { A } ^ { k } \partial _ { p } U _ { - A } \big ) - 2 \bar { S } _ { A } ^ { j p } \big ( \partial _ { k } U _ { - A } ^ { p } - \partial _ { p } U _ { - A } ^ { k } \big ) . } } \end{array}
$$

Moving the time derivative to the left-hand side of Eq. (9.203), we see that the extra terms give rise to the additional shift $\Delta _ { \mathrm { { e x t } } } S _ { A } ^ { j }$ in Eq. (9.171); we have arrived at our final version of the spin vector, $\bar { S } _ { A } ^ { j } = S _ { A } ^ { j } + \Delta _ { \mathrm { i n t } } S _ { A } ^ { j } + \Delta _ { \mathrm { e x t } } S _ { A } ^ { j } = S _ { A } ^ { j } + O ( c ^ { - 2 } )$ .

In the final step we evaluate the derivatives of the external potentials, taking into account the spin terms in the vector potential – refer to Eq. (9.195d) – and make the substitutions in Eq. (9.213). Excluding now the total time derivative, we have that

$$
G _ { \mathrm { e x t } } ^ { j k } = G ^ { j k } [ \mathrm { s o } ] + G ^ { j k } [ \mathrm { s s } ] ,
$$

with

$$
G ^ { j k } [ { \mathsf { s o } } ] = - { \frac { 1 } { 2 } } { \bar { S } } _ { A } ^ { j p } \sum _ { B \neq A } { \frac { G m _ { B } } { r _ { A B } ^ { 2 } } } { \bigg [ } ( 3 v _ { A } - 4 v _ { B } ) ^ { p } n _ { A B } ^ { k } - ( 3 v _ { A } - 4 v _ { B } ) ^ { k } n _ { A B } ^ { p } { \bigg ] }
$$

and

$$
G ^ { j k } [ \mathrm { s s } ] = \bar { S } _ { A } ^ { j p } \sum _ { B \neq A } \frac { G } { r _ { A B } ^ { 3 } } \bigg [ 3 n _ { A B } ^ { p } \bar { S } _ { B } ^ { k q } n _ { A B } ^ { q } - 3 n _ { A B } ^ { k } \bar { S } _ { B } ^ { p q } n _ { A B } ^ { q } + 2 \bar { S } _ { B } ^ { p k } \bigg ] .
$$

Inserting this within Eq. (9.203), expressing the spin tensor in terms of the spin vector $\bar { S } _ { A } ^ { j }$ , and simplifying, we finally arrive at the spin-precession equation of Eq. (9.198).

# 9.5.7 Comoving frame and proper spin

The partial redefinition $S _ { A }  S _ { A } + \Delta _ { \mathrm { i n t } } S _ { A }$ of the spin vector was performed to eliminate the total time derivative from the right-hand side of Eq. (9.208), and this operation was unique. The further shift of the spin vector by $\Delta _ { \mathrm { e x t } } \pmb { S } _ { A }$ was introduced specifically to cast the spin evolution equation in the form of a precession equation, and this operation reflected a choice on our part; the equation could have been left in its original form, or manipulated into yet a different form, in spite of the fact that these alternative versions would have been less compelling than Eq. (9.198). In this section we provide additional motivation for the external shift. We shall show that

$$
\bar { \bf S } _ { \cal A } : = { \bf S } _ { \cal A } + \Delta _ { \mathrm { e x t } } { \bf S } _ { \cal A } = S _ { \cal A } + \frac { 1 } { c ^ { 2 } } \bigg [ \big ( v _ { \cal A } ^ { 2 } + 3 U _ { - \cal A } \big ) S _ { \cal A } - \frac { 1 } { 2 } ( v _ { \cal A } \cdot S _ { \cal A } ) v _ { \cal A } \bigg ]
$$

is the spin vector as measured in a non-inertial frame that is at all times moving with the body; we call it the proper spin, or comoving spin. Our considerations here exclude the internal shift contributed by the internal motions and potentials.

The transformation from the original, inertial frame $( t , x ^ { j } )$ to the non-inertial, comoving frame $( \bar { t } , \bar { x } ^ { j } )$ is described by the class of post-Newtonian transformations presented in Sec. 8.3 – refer to $\mathrm { B o x } 8 . 2$ . The transformation is given by

$$
\begin{array} { c } { { t = \bar { t } + c ^ { - 2 } \alpha ( \bar { t } , \bar { x } ^ { j } ) + { \cal O } ( c ^ { - 4 } ) , } } \\ { { { } } } \\ { { x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( t ) + c ^ { - 2 } h ^ { j } ( \bar { t } , \bar { x } ^ { j } ) + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

in which

$$
\begin{array} { l } { { \alpha = { \cal A } ( \bar { t } ) + { \dot { r } } _ { p } \bar { x } ^ { p } , } } \\ { { { } } } \\ { { h ^ { j } = H ^ { j } ( \bar { t } ) + H _ { _ p } ^ { j } ( \bar { t } ) \bar { x } ^ { p } + { \cfrac { 1 } { 2 } } H _ { _ { p q } } ^ { j } ( \bar { t } ) \bar { x } ^ { p } \bar { x } ^ { q } , } } \end{array}
$$

with

$$
\begin{array} { c } { { H _ { j p } = \displaystyle \frac { 1 } { 2 } \dot { r } _ { j } \dot { r } _ { p } - \delta _ { j p } \bigg ( \dot { A } - \frac { 1 } { 2 } \dot { r } ^ { 2 } \bigg ) , } } \\ { { H _ { j p q } = - \delta _ { j p } \ddot { r } _ { q } - \delta _ { j q } \ddot { r } _ { p } + \delta _ { p q } \ddot { r } _ { j } ; } } \end{array}
$$

the functions $r ^ { j } ( \bar { t } ) , A ( \bar { t } )$ , and $H ^ { j } ( \bar { t } )$ are for now arbitrary, overdots indicate differentiation with respect to $\bar { t }$ , and $\dot { r } ^ { 2 } : = \delta _ { p q } \dot { r } ^ { p } \dot { r } ^ { q }$ . The terms of order $c ^ { - 4 }$ in the time transformation are not required here, and the functions $R ^ { j } ( \bar { t } )$ that would normally appear in $H _ { j p }$ were set equal to zero.

The starting point of our discussion of proper spin is the selection of a representative world line $\mathit { z } _ { A } ( t )$ within body $A$ , which is meant to track the motion of its “center-of-mass.” An issue that we shall have to address is the precise meaning of this phrase. In our previous considerations, the center-of-mass was always defined in the inertial frame, but here we have the option of defining the center-of-mass in the body’s comoving frame; these definitions are not equivalent when the body is spinning, and we shall have to decide which centerof-mass the representative world line is supposed to track. We leave it arbitrary for the time being, and think of it as the world line of an arbitrarily-selected fluid element within the body. The frame $( \bar { t } , \bar { x } ^ { j } )$ is attached to the representative world line, so that $\bar { x } ^ { j } = 0$ on the representative world line.

Our spin vector shall now be defined with respect to the representative world line. We have

$$
\pmb { S } _ { A } : = \int _ { A } \rho ^ { * } ( \pmb { x } - \pmb { z } _ { A } ) \times ( \pmb { \nu } - \pmb { w } _ { A } ) d ^ { 3 } x
$$

in the inertial frame, in which $\pmb { w } _ { A } : = d \pmb { z } _ { A } / d t$ and the integral is evaluated on a surface $t = 0$ constant in spacetime (so that all the sampled points $_ { x }$ are simultaneous with $z _ { A }$ in the inertial frame), and

$$
\bar { \pmb { S } } _ { A } : = \int _ { A } \bar { \rho } ^ { * } \bar { \pmb { x } } \times \bar { \pmb { v } } d ^ { 3 } \bar { x }
$$

in the comoving frame, in which the integral is evaluated on a surface $\bar { t } =$ constant (all the sampled points $\bar { x }$ are simultaneous in the comoving frame). We wish to express $\pmb { S } _ { A }$ in terms of $\bar { \pmb S } _ { A }$ , and for this we must relate $\mathbf { x } - \mathbf { z } _ { A }$ to $\bar { x }$ , and ${ \pmb v } - { \pmb w } _ { A }$ to $\bar { \pmb { v } }$ , and take into account the fact that $d m : = \rho ^ { \ast } d ^ { 3 } x = \bar { \rho } ^ { \ast } d ^ { 3 } \bar { x }$ is an invariant – recall the discussion around Eq. (8.92).

To achieve this we examine the world line of an arbitrary fluid element that passes through a spacetime point $P$ within the body, to which we assign the coordinates $( t , x ^ { j } )$ in the inertial frame, and the coordinates $( \bar { t } , \bar { x } ^ { j } )$ in the comoving frame; the transformation is given by Eq. (9.218). Together with this world line we consider the body’s representative world line, and on it we select the spacetime point $Q$ that is simultaneous with $P$ in the inertial frame; its coordinates are $( t , z _ { A } ^ { j } )$ in the inertial frame, $( \bar { t } _ { A } , 0 )$ in the comoving frame,

and the transformation is given by

$$
t = \bar { t } _ { A } + c ^ { - 2 } A ( \bar { t } _ { A } ) + O ( c ^ { - 4 } ) , \qquad z _ { A } ^ { j } = r ^ { j } ( \bar { t } _ { A } ) + c ^ { - 2 } H ^ { j } ( \bar { t } _ { A } ) + O ( c ^ { - 4 } ) .
$$

From Eqs. (9.218) and (9.223) we find that

$$
\bar { t } = \bar { t } _ { A } - c ^ { - 2 } \dot { r } _ { p } ( \bar { t } _ { A } ) \bar { x } ^ { p } + O ( c ^ { - 4 } )
$$

and $( x - z _ { A } ) ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } ) - r ^ { j } ( \bar { t } _ { A } ) + c ^ { - 2 } [ h ^ { j } ( \bar { t } , \bar { x } ^ { j } ) - H ^ { j } ( \bar { t } _ { A } ) ] + O ( c ^ { - 4 } ) .$ The last equation appears to give us what we need, but it requires additional work because the various terms on the right-hand side refer to different times; what we want instead is for all the terms to be simultaneous in the comoving frame. In particular, $\bar { x } ^ { j }$ refers to $P$ , which is not simultaneous, and we wish to express this in terms of the coordinates of the point $P ^ { \prime }$ on the fluid element’s world line that is simultaneous with $Q$ . If the functions $\bar { x } ^ { j } ( \bar { t } )$ describe the world line in the comoving frame, then $\bar { x } ^ { j } ( \bar { t } )$ refers to $P$ , while $\bar { x } ^ { j } ( \bar { t } _ { A } )$ refers to $P ^ { \prime }$ , and the relation $\bar { x } ^ { j } = \bar { x } ^ { j } ( \bar { t } _ { A } ) - c ^ { - 2 } \bar { v } ^ { j } \dot { r } _ { p } \bar { x } ^ { p } + O ( c ^ { - 4 } )$ follows by simple Taylor expansion; $\bar { v } ^ { j }$ is the fluid’s velocity field in the comoving frame. Proceeding similarly with $r ^ { j } ( \bar { t } )$ , we find that

$$
( x - z _ { A } ) ^ { j } = \bar { x } ^ { j } + c ^ { - 2 } \biggl [ \bigl ( H _ { { p } } ^ { j } - \dot { r } ^ { j } \dot { r } _ { p } - \bar { v } ^ { j } \dot { r } _ { p } \bigr ) \bar { x } ^ { p } + \frac { 1 } { 2 } H _ { { p q } } ^ { j } \bar { x } ^ { p } \bar { x } ^ { q } \biggr ] + O ( c ^ { - 4 } ) ,
$$

in which all terms on the right-hand side refer to $P ^ { \prime }$ and are evaluated at comoving time $\overline { { t } } _ { A }$

The left-hand side of Eq. (9.225) can be differentiated with respect to $t$ , the right-hand side can be differentiated with respect to $\bar { t } _ { A }$ , and Eq. (9.223) can be used to relate the time differentials. The end result is

$$
\begin{array} { r l } & { ( v - w _ { \mathit { A } } ) ^ { j } = \bar { v } ^ { j } + c ^ { - 2 } \bigg [ \big ( \dot { H } _ { p } ^ { j } - \dot { r } ^ { j } \ddot { r } _ { p } - \bar { v } ^ { j } \ddot { r } _ { p } - \ddot { r } ^ { j } \dot { r } _ { p } - \bar { a } ^ { j } \dot { r } _ { p } \big ) \bar { x } ^ { p } - \dot { A } \bar { v } ^ { j } } \\ & { \qquad + \big ( H _ { p } ^ { j } - \dot { r } ^ { j } \dot { r } _ { p } - \bar { v } ^ { j } \dot { r } _ { p } \big ) \bar { v } ^ { p } + \frac { 1 } { 2 } \dot { H } _ { p q } ^ { j } \bar { x } ^ { p } \bar { x } ^ { q } + H _ { p q } ^ { j } \bar { x } ^ { p } \bar { v } ^ { q } \bigg ] , } \end{array}
$$

in which all terms on the right-hand side continue to be evaluated at comoving time $\bar { t } _ { A }$ .

We next insert Eqs. (9.225) and (9.226) within Eq. (9.221) and evaluate the integral. We implement our usual simplification rules by discarding all terms that involve an odd number of internal vectors, and neglecting all terms that scale as $R _ { A } ^ { 2 }$ . We insert the previously displayed expression for $H _ { j k }$ , simplify the result, and arrive at

$$
{ \pmb S } _ { { \cal A } } = \bar { \pmb S } _ { { \cal A } } + \frac { 1 } { c ^ { 2 } } \bigg [ \bigg ( \frac { 1 } { 2 } \dot { r } ^ { 2 } - 3 \dot { \cal A } \bigg ) \bar { \pmb S } _ { { \cal A } } + \frac { 1 } { 2 } ( \dot { r } \cdot \bar { \pmb S } _ { { \cal A } } ) \dot { \pmb r } \bigg ] + O ( c ^ { - 4 } ) ,
$$

which can be inverted to give

$$
\bar { \bf S } _ { \scriptscriptstyle A } = { \bf S } _ { \scriptscriptstyle A } + \frac { 1 } { c ^ { 2 } } \bigg [ \bigg ( 3 \dot { A } - \frac { 1 } { 2 } \dot { r } ^ { 2 } \bigg ) { \bf S } _ { \scriptscriptstyle A } - \frac { 1 } { 2 } ( \dot { r } \cdot { \bf S } _ { \scriptscriptstyle A } ) \dot { r } \bigg ] + O ( c ^ { - 4 } ) .
$$

This equation looks vaguely like Eq. (9.217), but we must justify the identification ${ \dot { \pmb { r } } } = { \pmb { v } } _ { A }$ and determine the arbitrary function $A ( \bar { t } )$ .

In fact, our discussion thus far has left many quantities undetermined. We have yet to specify the functions $r ^ { j } ( \bar { t } ) , \ A ( \bar { t } )$ , and $H ^ { j } ( \bar { t } )$ , and we have yet to make a choice of representative world line. We first tackle the determination of $r ^ { j }$ and $H ^ { j }$ , and to achieve

this we return to Eq. (9.223), which we write as $\bar { t } _ { A } = t - c ^ { - 2 } A ( \bar { t } _ { A } ) + O ( c ^ { - 4 } )$ and

$$
z _ { A } ^ { j } ( t ) = r ^ { j } ( \bar { t } _ { A } ) + c ^ { - 2 } H ^ { j } ( \bar { t } _ { A } ) + O ( c ^ { - 4 } ) .
$$

If we express the functions on the right-hand side in terms of $t$ , we have that

$$
z _ { A } ^ { j } ( t ) = r ^ { j } ( t ) + c ^ { - 2 } \big [ H ^ { j } ( t ) - A ( t ) \dot { r } ^ { j } ( t ) \big ] + O ( c ^ { - 4 } ) .
$$

This equation becomes $z _ { A _ { . } } ^ { j } { = } r ^ { j } + { \cal O } ( c ^ { - 4 } )$ when we set $H ^ { j } = A \dot { r } ^ { j }$ , and we may then identify $r ^ { j } ( \bar { t } )$ with the position $z _ { A } ^ { j }$ of the representative world line evaluated at the time $t = \bar { t }$ . In this manner we identity $r$ with $z _ { A }$ , and $\dot { \boldsymbol { r } }$ with ${ \pmb { w } } _ { A }$ .

We next tackle determination of the representative world line. As a guide, we insert Eq. (9.225) within $\textstyle \int _ { A } \rho ^ { * } ( x - z _ { A } ) ^ { j } d ^ { 3 } x$ , evaluate the integral, and get

$$
\begin{array} { l } { { ( r _ { \cal A } - z _ { \cal A } ) ^ { j } = \displaystyle \biggl [ 1 - \frac { 1 } { c ^ { 2 } } \Bigl ( { \dot { \cal A } } - \frac { 1 } { 2 } w _ { \cal A } ^ { 2 } \Bigr ) \biggr ] { \bar { r } } _ { \cal A } ^ { j } - \frac { 1 } { 2 c ^ { 2 } } ( { \pmb w } _ { \cal A } \cdot { \bar { \pmb r } } _ { \cal A } ) w _ { \cal A } ^ { j } } } \\ { { ~ + \frac { 1 } { 2 m _ { \cal A } c ^ { 2 } } { \bar { \cal S } } _ { \cal A } ^ { j k } w _ { \cal A } ^ { k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

in which

$$
\pmb { r } _ { A } : = \frac { 1 } { m _ { A } } \int _ { A } \pmb { \rho } ^ { * } \pmb { x } d ^ { 3 } \pmb { x }
$$

is the center-of-mass position in the inertial frame,

$$
\bar { \pmb { r } } _ { A } : = \frac { 1 } { m _ { A } } \int _ { A } \bar { \rho } ^ { * } \bar { \pmb { x } } d ^ { 3 } \bar { x }
$$

is the center-of-mass position in the comoving frame, and

$$
{ { \bar { S } } _ { A } ^ { j k } } : = \int _ { A } { \bar { \rho } ^ { \ast } } \left( { { \bar { x } } ^ { j } } { { \bar { v } } ^ { k } } - { { \bar { x } } ^ { k } } { { \bar { v } } ^ { j } } \right) { { d } ^ { 3 } } \bar { x }
$$

is the comoving spin tensor.

There are two obvious ways of selecting a representative world line. The first is to declare that it will track the body’s center-of-mass as defined in the inertial frame. To effect this choice we set $z _ { A } = r _ { A }$ , and Eq. (9.231) informs us that the position of the comoving center-of-mass is given by

$$
\bar { r } _ { A } ^ { j } = - \frac { 1 } { 2 m _ { A } c ^ { 2 } } \bar { S } _ { A } ^ { j k } v _ { A } ^ { k } + O ( c ^ { - 4 } ) .
$$

With this choice of representative world line, we find that the spatial origin of the comoving frame $( \bar { t } , \bar { x } ^ { j } )$ does not coincide with the comoving center-of-mass, which is offset by the vector ${ \bar { \boldsymbol { r } } } _ { A }$ . This situation invites us to make a distinction between the comoving spin $\bar { \pmb S } _ { A }$ , defined relative to the origin of the comoving frame, and a proper spin defined relative to the comoving center-of-mass. The proper spin would be defined by

$$
\int _ { A } \bar { \rho } ^ { * } ( \bar { \pmb { x } } - \bar { \pmb { r } } _ { A } ) \times ( \bar { \pmb { v } } - \bar { \pmb { v } } _ { A } ) d ^ { 3 } \bar { x } ,
$$

but it is easy to show that since $\bar { \pmb r } _ { A } = O ( c ^ { - 2 } )$ and $\bar { \pmb { v } } _ { A } = O ( c ^ { - 2 } )$ , this is equal to the comoving spin $\bar { \pmb S } _ { A }$ up to terms of order $c ^ { - 4 }$ . So while the distinction is important as a

matter of principle, it has no practical implications at the level of accuracy maintained in our discussion of spinning bodies.

The second way of selecting a representative world line is to declare that it will track the body’s center-of-mass as defined in the comoving frame. In this case we set $\bar { r } _ { A } = \mathbf { 0 }$ , and Eq. (9.231) implies that

$$
z _ { A } ^ { j } = r _ { A } ^ { j } - \frac { 1 } { 2 m _ { A } c ^ { 2 } } S _ { A } ^ { j k } v _ { A } ^ { k } + O ( c ^ { - 4 } ) .
$$

This equation states that the representative world line is offset from the inertial-frame center-of-mass by the vector $S _ { A } ^ { j k } v _ { A } ^ { k } / ( 2 m _ { A } c ^ { 2 } )$ . In this case there is no distinction to be made between comoving spin and proper spin, and the distinction between the inertial spin of Eq. (9.221) and the usual spin vector $\begin{array} { r } { \int _ { A } \rho ^ { * } ( { \pmb x } - { \pmb r } _ { A } ) \times ( { \pmb v } - { \pmb v } _ { A } ) d ^ { 3 } x } \end{array}$ occurs only at order $c ^ { - 4 }$ and is therefore unimportant.

Either way of selecting the representative world line leads to the identifications $r = z _ { A } =$ $\pmb { r } _ { A } + O ( c ^ { - 2 } )$ and $\pmb { \dot { r } } = \pmb { w } _ { A } = \pmb { v } _ { A } + O ( c ^ { - 2 } )$ , and Eq. (9.228) becomes

$$
\bar { \bar { \bf S } } _ { \cal A } = { \bf S } _ { \cal A } + \frac { 1 } { c ^ { 2 } } \biggl [ \Bigl ( 3 \dot { A } - \frac { 1 } { 2 } v _ { A } ^ { 2 } \Bigr ) { \bf S } _ { \cal A } - \frac { 1 } { 2 } ( { \pmb v } _ { A } \cdot { \bf S } _ { \cal A } ) { \pmb v } _ { A } \biggr ] + O ( c ^ { - 4 } ) .
$$

Our only remaining task is to determine the function $A ( \bar { t } )$ that appears in the transformation between the internal and comoving frames. Here we take our guidance from Sec. 8.3.5, in which we first examined the post-Newtonian transformation between a global, inertial frame to a local, comoving frame. There it was shown that in order to account for the special-relativistic and gravitational effects of time dilation, the function $A ( \bar { t } )$ must be a solution to

$$
\dot { A } = \frac { 1 } { 2 } v _ { A } ^ { 2 } + U _ { \ l \ l \ l \ l , A } ,
$$

in which the external potential is evaluated on the representative world line. Making the substitution in Eq. (9.237), we arrive at Eq. (9.217), and our justification of the external shift $\Delta _ { \mathrm { e x t } } \pmb { S } _ { A }$ is complete.

# 9.5.8 Choice of representative world line

The discussion of the previous subsection revealed an ambiguity in the choice of representative world line when the body is spinning. We considered two canonical choices, one in which the representative world line tracks the body’s center-of-mass as defined in the global, inertial frame, and another in which it tracks the center-of-mass as defined in the local, comoving frame. While these choices lead to the same notion of proper spin, they lead to different representations of the center-of-mass motion.

To explore the impact of this ambiguity on the equations of motion, we enlarge our freedom of choice and examine a one-parameter family of representative world lines described by

$$
\tilde { r } _ { A } ^ { j } = r _ { A } ^ { j } - \frac { \lambda } { 2 m _ { A } c ^ { 2 } } S _ { A } ^ { j k } v _ { A } ^ { k } + O ( c ^ { - 4 } ) ,
$$

in which $r _ { A }$ is the center-of-mass position in the inertial frame, $S _ { A } ^ { j k }$ is the spin tensor of Eq. (9.167), and $\lambda$ is a dimensionless parameter. (In this subsection we prefer to use the notation ${ \tilde { r } } _ { A }$ for the representative world line, instead of $z _ { A }$ as we did in the preceding subsection.) The assignment $\lambda = 0$ makes the representative world line track the inertial center-of-mass, $\lambda = 1$ makes it track the comoving center-of-mass, and it is easy to show that Eq. (9.239) gives rise to the comoving spin vector of Eq. (9.217) for any choice of $\lambda$ .

Because the difference between ${ \pmb { \tilde { r } } } _ { A }$ and $r _ { A }$ is of order $c ^ { - 2 }$ , the transformation has no impact on the spin-precession equations (9.198). It also has no direct impact on the post-Newtonian terms in the center-of-mass accelerations of Eq. (9.188). There is, however, an indirect impact, because the Newtonian acceleration will undergo a change of order $c ^ { - 2 }$ , and this change can be transferred to the post-Newtonian terms; because the transformation is linear in the spin, the transfer affects the form of the spin–orbit acceleration. In addition, we can see that the transformation will have no direct impact on the post-Newtonian potentials within the metric, but that the Newtonian potential will be changed by a term of order $c ^ { - 2 }$ that can be transferred to the post-Newtonian potentials.

We begin with a computation of the transformed Newtonian potential, which is given by $\begin{array} { r } { U = \sum _ { A } G m _ { A } / s _ { A } } \end{array}$ with $s _ { A } : = | \pmb { x } - \pmb { r } _ { A } |$ when it is evaluated far away from each body. This expression refers to the inertial center-of-mass of each body, and our goal here is to shift the reference to the representative world line. We write $\pmb { r } _ { A } = \pmb { \tilde { r } } _ { A } + \delta \pmb { r } _ { A }$ , with $\delta r _ { A }$ given by (minus) the second term in Eq. (9.239), and we express $s _ { A }$ as $\lvert \tilde { s } _ { A } - \delta r _ { A } \rvert$ , with $\tilde { \mathbf { s } } _ { A } : = \mathbf { x } - \tilde { { \boldsymbol { r } } } _ { A }$ denoting the separation between the field point $_ { x }$ and the representative world line. Performing a Taylor expansion in powers of $\delta r _ { A }$ , we quickly arrive at

$$
U = \tilde { U } + \frac { \lambda } { 2 c ^ { 2 } } \sum _ { A } \frac { G ( \tilde { \pmb { n } } _ { A } \times \tilde { \pmb { v } } _ { A } ) \cdot \pmb { S } _ { A } } { \tilde { s } _ { A } ^ { 2 } } + O ( c ^ { - 4 } ) ,
$$

in which $\begin{array} { r } { \tilde { U } : = \sum _ { A } G m _ { A } / \tilde { s } _ { A } } \end{array}$ is the shifted potential, $\tilde { s } _ { A } : = | \tilde { \pmb { s } } _ { A } |$ , $\pmb { \tilde { n } } _ { A } : = \pmb { \tilde { s } } _ { A } / \pmb { \tilde { s } } _ { A }$ , and $\widetilde { \pmb { v } } _ { A } : =$ $d \tilde { r } _ { A } / d t$ is the velocity of the representative world line. The transformation of the Newtonian potential creates a spin contribution to $g _ { 0 0 }$ that must be added to the one already listed in Eq. (9.182). We find that

$$
\Delta g _ { 0 0 } = \frac { 3 + \lambda } { c ^ { 4 } } \sum _ { A } \frac { G ( \tilde { n } _ { A } \times \tilde { v } _ { A } ) \cdot S _ { A } } { \tilde { s } _ { A } ^ { 2 } } + { \cal O } ( c ^ { - 6 } )
$$

is the spin term under the new description of the body’s motion. There are no additional changes to $g _ { 0 j }$ and $g _ { j k }$ .

We next consider the changes in the equations of motion. The first source of change is the difference implied by Eq. (9.239) between the acceleration $\tilde { \pmb { a } } _ { A }$ of the representative world line and the acceleration $\pmb { a } _ { A }$ of the inertial center-of-mass. To calculate this difference we first differentiate Eq. (9.239) with respect to time and obtain $\tilde { \pmb { v } } _ { A }$ in terms of ${ \pmb v } _ { A }$ . The term involving $d S _ { A } ^ { j k } / d t = O ( c ^ { - 2 } )$ can be neglected, and the term involving $a _ { A } ^ { k }$ can be written in terms of the Newtonian acceleration. The end result is

$$
\tilde { v } _ { A } ^ { j } = v _ { A } ^ { j } + \frac { \lambda } { 2 m _ { A } c ^ { 2 } } \sum _ { B \neq A } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } S _ { A } ^ { j k } n _ { A B } ^ { k } .
$$

Another differentiation with respect to $t$ produces

$$
\tilde { a } _ { \cal A } ^ { j } = a _ { \cal A } ^ { j } - \frac { 3 \lambda } { 2 c ^ { 2 } } \sum _ { B \not = { \cal A } } \frac { G M _ { B } } { r _ { A B } ^ { 3 } } n _ { A B } ^ { \langle k p \rangle } ( v _ { A } - v _ { B } ) ^ { p } \hat { S } _ { A } ^ { j k } ,
$$

in which $\hat { S } _ { A } ^ { j k } : = S _ { A } ^ { j k } / m _ { A } = S _ { A } ^ { j k } / M _ { A } + O ( c ^ { - 2 } )$

The second source of change is the shift of the Newtonian acceleration $\pmb { a } _ { \mathcal { A } } [ 0 \mathrm { \bf p N } ]$ that occurs when the acceleration is made to refer to the representative world line instead of the inertial center-of-mass. This shift is analogous to the one calculated previously for the Newtonian potential, and indeed, it can be computed in the same way, by expanding the acceleration in powers of $\delta r _ { A }$ . The outcome of this computation is

$$
a _ { A } ^ { j } [ 0 \mathrm { P N } ] = - \sum _ { B \neq A } \frac { G M _ { B } } { \tilde { r } _ { A B } ^ { 2 } } \tilde { n } _ { A B } ^ { j } + \frac { 3 \lambda } { 2 c ^ { 2 } } \sum _ { B \neq A } \frac { G M _ { B } } { \tilde { r } _ { A B } ^ { 3 } } \tilde { n } _ { A B } ^ { \langle j k \rangle } \big ( \hat { S } _ { A } ^ { k p } \tilde { v } _ { A } ^ { p } - \hat { S } _ { B } ^ { k p } \tilde { v } _ { B } ^ { p } \big ) ,
$$

in which $\tilde { { \pmb r } } _ { A B } : = \tilde { { \pmb r } } _ { A } - \tilde { { \pmb r } } _ { B } , \tilde { { \pmb r } } _ { A B } : = | \tilde { { \pmb r } } _ { A B } |$ , and $\pmb { \tilde { n } } _ { A B } : = \pmb { \tilde { r } } _ { A B } / \tilde { r } _ { A B }$ .

Collecting results, we find that the changes to the acceleration are all linear in the spin tensors, and that they contribute to a shift in the spin–orbit acceleration of Eq. (9.189). The shifted expression is

$$
\begin{array} { c } { { \tilde { a } _ { \mathcal { A } } ^ { j } [ \mathrm { s o } ] : = \displaystyle \frac { 3 } { 2 c ^ { 2 } } \sum _ { B \neq \mathcal { A } } \frac { G M _ { B } } { \tilde { r } _ { A B } ^ { 3 } } \Bigg \{ \tilde { n } _ { \mathcal { A } B } ^ { \langle j k \rangle } \bigg [ \tilde { v } _ { \mathcal { A } } ^ { p } \bigg ( ( 3 + \lambda ) \hat { S } _ { \mathcal { A } } ^ { k p } + 4 \hat { S } _ { B } ^ { k p } \bigg ) - \tilde { v } _ { B } ^ { p } \bigg ( ( 3 + \lambda ) \hat { S } _ { B } ^ { k p } + 4 \hat { S } _ { \mathcal { A } } ^ { k p } \bigg ) \bigg ] } } \\ { { { } } } \\ { { { } + \tilde { n } _ { \mathcal { A } B } ^ { \langle k p \rangle } ( \tilde { v } _ { \mathcal { A } } - \tilde { v } _ { B } ) ^ { p } \bigg ( ( 3 - \lambda ) \hat { S } _ { \mathcal { A } } ^ { j k } + 4 \hat { S } _ { B } ^ { j k } \bigg ) \Bigg \} , } } \end{array}
$$

and there are no additional changes to the post-Newtonian and spin–spin accelerations.

Ambiguities tend to make one feel uncomfortable. Things ought to be well defined, one feels, and there ought to be a “correct” value of $\lambda$ . There is no such thing, however, and one must learn to accept the freedom associated with the choice of representative world line. In a way, the freedom to shift the world line is analogous to the inherent freedom in general relativity to shift the coordinate system. The coordinate freedom is complete, and one knows that a coordinate transformation will produce a change in the metric, and a change in the equations of motion. One learns to live with this freedom, and to eliminate the coordinate ambiguity by formulating well-posed questions that have coordinate-independent answers. The situation is similar in the case of the representative world line. Here also the freedom is complete (even though we have restricted it to a one-parameter family in this discussion), and here also a shift in world line produces a change in the metric and the equations of motion. One must learn to live with the freedom, and to eliminate the ambiguity by formulating meaningful questions with precise answers.

In the literature the spin–orbit acceleration has traditionally been presented in two canonical forms corresponding to $\lambda = 0$ and $\lambda = 1$ , respectively, and the choice of $\lambda$ is often described as “imposing a spin supplementary condition;” for example, the choice $\lambda = 1$ i s described as the “covariant spin supplementary condition,” for reasons that we won’t care to go into here. Each form is acceptable, but one must be sure to implement the choice of $\lambda$ consistently in the equations of motion, the metric, and any other quantity computed from these ingredients.

# 9.5.9 Binary systems

To conclude our discussion of spinning bodies, we specialize our results to the case of a binary system involving a first body of mass-energy $M _ { 1 }$ , position $r _ { 1 }$ , velocity ${ \pmb v } _ { 1 }$ , and spin $\pmb { S } _ { 1 }$ , and a second body of mass-energy $M _ { 2 }$ , position $r _ { 2 }$ , velocity ${ \pmb v } _ { 2 }$ , and spin $\pmb { S } _ { 2 }$ . We adopt the one-parameter family of representative world lines introduced in the preceding subsection, but omit the tildes on the position and velocity vectors to keep the notation uncluttered.

Returning to the discussion of Sec. 9.3.7 but incorporating the changes coming from the spins, we find that the system’s barycenter is now situated at

$$
\begin{array} { l } { { \displaystyle M R = M _ { 1 } \bigg [ 1 + \frac { 1 } { 2 c ^ { 2 } } \bigg ( v _ { 1 } ^ { 2 } - \frac { G M _ { 2 } } { r } \bigg ) \bigg ] r _ { 1 } + M _ { 2 } \bigg [ 1 + \frac { 1 } { 2 c ^ { 2 } } \bigg ( v _ { 2 } ^ { 2 } - \frac { G M _ { 1 } } { r } \bigg ) \bigg ] r _ { 2 } } } \\ { { \displaystyle ~ + \frac { 1 + \lambda } { 2 c ^ { 2 } } \bigg ( v _ { 1 } \times S _ { 1 } + v _ { 2 } \times S _ { 2 } \bigg ) + O ( c ^ { - 4 } ) . } } \end{array}
$$

Imposing the barycentric condition $\pmb { R } = \pmb { 0 }$ allows us to express $r _ { 1 }$ and $r _ { 2 }$ in terms of the separation $r : = r _ { 1 } - r _ { 2 }$ and relative velocity $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ . We find that $r _ { 1 } = ( M _ { 2 } / m ) r +$ $P$ and $r _ { 2 } = - ( M _ { 1 } / m ) r + P$ , with

$$
P : = \frac { \eta \Delta } { 2 c ^ { 2 } } \Big ( v ^ { 2 } - \frac { G m } { r } \Big ) r - \frac { 1 + \lambda } { 2 m c ^ { 2 } } \pmb { v } \times \big ( M _ { 2 } \pmb { S } _ { 1 } - M _ { 1 } \pmb { S } _ { 2 } \big ) + O ( c ^ { - 4 } ) ,
$$

in which $m : = M _ { 1 } + M _ { 2 }$ , $\eta : = { M _ { 1 } M _ { 2 } } / ( M _ { 1 } + M _ { 2 } ) ^ { 2 }$ , and $\Delta : = ( M _ { 1 } - M _ { 2 } ) / ( M _ { 1 } + M _ { 2 } )$ .   
These equations imply that $\pmb { v } _ { 1 } = ( M _ { 2 } / m ) \pmb { v } + O ( c ^ { - 2 } )$ and $\pmb { v } _ { 2 } = - ( M _ { 1 } / m ) \pmb { v } + O ( c ^ { - 2 } )$ .

The relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ can be expressed as

$$
\pmb { a } = \pmb { a } [ 0 \mathrm { P N } ] + \pmb { a } [ 1 \mathrm { P N } ] + \pmb { a } [ \mathrm { s o } ] + \pmb { a } [ \mathrm { s s } ] + O ( c ^ { - 4 } ) ,
$$

with ${ \pmb a } [ 0 \mathrm { \bf P N } ]$ and ${ \pmb a } [ 1 \mathrm { P N } ]$ given by Eq. (9.142), and the spin–orbit and spin–spin accelerations given by

$$
a ^ { j } [ { \mathsf { s o } } ] = { \frac { 3 G } { 2 c ^ { 2 } r ^ { 3 } } } \bigg \{ n ^ { \langle j k \rangle } v ^ { p } \big [ ( 3 + \lambda ) \sigma ^ { k p } + 4 S ^ { k p } \big ] + n ^ { \langle k p \rangle } v ^ { p } \big [ ( 3 - \lambda ) \sigma ^ { j k } + 4 S ^ { j k } \big ] \bigg \}
$$

and

$$
a ^ { j } [ \mathrm { s s } ] = - \frac { 1 5 G m } { c ^ { 2 } r ^ { 4 } } \hat { S } _ { 1 } ^ { k p } \hat { S } _ { 2 } ^ { k q } n ^ { \langle j q p \rangle } ,
$$

respectively, in which $r : = | r | , n : = r / r$ , and

$$
\sigma ^ { j k } : = \frac { M _ { 2 } } { M _ { 1 } } S _ { 1 } ^ { j k } + \frac { M _ { 1 } } { M _ { 2 } } S _ { 2 } ^ { j k } , \qquad S ^ { j k } : = S _ { 1 } ^ { j k } + S _ { 2 } ^ { j k } .
$$

These become

$$
\begin{array} { c } { { a [ \mathrm { s o } ] = \displaystyle \frac { G } { c ^ { 2 } r ^ { 3 } } \Bigg \{ \displaystyle \frac { 3 } { 2 } ( n \times v ) \cdot \big [ ( 3 + \lambda ) \sigma + 4 S \big ] n + \displaystyle \frac { 3 } { 2 } ( n \cdot v ) n \times \big [ ( 3 - \lambda ) \sigma + 4 S \big ] } } \\ { { - v \times ( 3 \sigma + 4 S ) \Bigg \} } } \end{array}
$$

and

$$
a [ \mathrm { s s } ] = - \frac { 3 G m } { c ^ { 2 } r ^ { 4 } } \Big [ ( \hat { S } _ { 1 } \cdot \hat { S } _ { 2 } ) n - 5 ( \hat { S } _ { 1 } \cdot n ) ( \hat { S } _ { 2 } \cdot n ) n + ( \hat { S } _ { 1 } \cdot n ) \hat { S } _ { 2 } + ( \hat { S } _ { 2 } \cdot n ) \hat { S } _ { 1 } \Big ] ,
$$

when we express the accelerations in terms of the spin vectors; here we have that $\pmb { \sigma } : =$ $( M _ { 2 } / M _ { 1 } ) \pmb { S } _ { 1 } + ( M _ { 1 } / M _ { 2 } ) \pmb { S } _ { 2 } , \pmb { S } : = \pmb { S } _ { 1 } + \pmb { S } _ { 2 } , \hat { \pmb { S } } _ { 1 } : = \pmb { S } _ { 1 } / M _ { 1 } ,$ and $\hat { \pmb { S } } _ { 2 } : = \pmb { S } _ { 2 } / M _ { 2 }$ .

The spin-precession equations become

$$
\frac { d \bar { \pmb { S } } _ { 1 } } { d t } = { \pmb { \Omega } } _ { 1 } \times \bar { \pmb { S } } _ { 1 } ,
$$

in which $\bar { \pmb { S } } _ { 1 }$ is the proper spin of the first body, and

$$
\pmb { \Omega } _ { 1 } = \pmb { \Omega } _ { 1 } [ \mathrm { s o } ] + \pmb { \Omega } _ { 1 } [ \mathrm { s s } ] ,
$$

with

$$
\begin{array} { l } { { \displaystyle \mathfrak { Q } _ { 1 } [ \mathrm { s o } ] = \frac { 2 \eta G m } { c ^ { 2 } r ^ { 2 } } \biggl ( 1 + \frac { 3 M _ { 2 } } { 4 M _ { 1 } } \biggr ) \pmb { n } \times \pmb { v } , } } \\ { { \displaystyle \mathfrak { Q } _ { 1 } [ \mathrm { s s } ] = \frac { G } { c ^ { 2 } r ^ { 3 } } \bigl [ 3 ( \bar { \mathbf { S } } _ { 2 } \cdot \pmb { n } ) \pmb { n } - \bar { \mathbf { S } } _ { 2 } \bigr ] , } } \end{array}
$$

the precessional angular velocity. The equations for the second body are obtained by a simple exchange of labels $1  2$ .

# 9.6 Point particles

The calculations that led to the inter-body metric of Eq. (9.81) were laborious, and most of this labor was spent on the computation of terms that depend on the internal structure of each body. These terms, however, all cancel out after invoking the equilibrium conditions, and they do not appear in the final expression for the metric. This effort is not entirely wasted, because it generates considerable evidence that general relativity satisfies the strong formulation of the principle of equivalence, but one wonders whether a shortcut to the final result might not exist.

In this final section of Chapter 9 we examine the shortcut that results when the bodies are modeled as point particles. We show that the road to the metric is made much shorter indeed, but that this efficiency comes at a high price: the need to regularize divergent integrals. The origin of the problem is easy to identify: a point particle possesses an infinite mass density $\rho ^ { * }$ and produces a Newtonian potential $U$ that diverges at the particle’s position; because the product $\rho ^ { * } U$ acts as a source for the post-Newtonian potential $\Psi$ , the mathematical existence of this object becomes questionable. We shall show, however, that a simple and well-motivated regularization prescription allows us to make sense of the divergent integrals, and the method reproduces the results displayed in Eq. (9.81).

We use the shortcut extensively in Chapter 11, when we calculate the gravitational waves produced by the motion of an $N$ -body system. Throughout this section we take the bodies to have no spin, so that $S _ { A } ^ { j k } = 0$ .

# 9.6.1 Energy-momentum tensor

The description of a point particle moving in a curved spacetime was developed in Sec. 5.3.4. The particle has a mass $m$ , it moves on a world line described by the parametric relations $r ^ { \alpha } ( \tau )$ , and its velocity four-vector is $u ^ { \alpha } = d r ^ { \alpha } / d \tau ;$ $\tau$ is proper time on the particle’s world line. Its energy-momentum tensor was displayed in Eq. (5.108); it is

$$
T ^ { \alpha \beta } = m c \int u ^ { \alpha } u ^ { \beta } { \frac { \delta { \bigl ( } x ^ { \mu } - r ^ { \mu } ( \tau ) { \bigr ) } } { \sqrt { - g } } } d \tau .
$$

This expression can be simplified if we change the variable of integration from $\tau$ to $r ^ { 0 } ( \tau )$ . This permits an integration over the delta function $\delta ( x ^ { 0 } - r ^ { 0 } )$ , and we obtain

$$
T ^ { \alpha \beta } = \frac { m u ^ { \alpha } u ^ { \beta } } { \gamma \sqrt { - g } } \delta \bigl ( \pmb { x } - \pmb { r } ( t ) \bigr ) ,
$$

where $\gamma : = u ^ { 0 } / c$ . The particle’s world line is now described by the relations $\mathbf { } r ( t )$ with $t : = x ^ { 0 } / c$ , and the velocity four-vector is decomposed as $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ with $\pmb { v } : = d \pmb { r } / d t$ .

Equation (9.258) can be compared with Eq. (5.91), which gives the energy-momentum tensor of a perfect fluid. The comparison reveals that the point particle is a limiting case of a perfect fluid, with a proper energy density given by $\mu = m c ^ { 2 } \gamma ^ { - 1 } ( - g ) ^ { - 1 / 2 } \delta ( { \bf x } - r )$ , and a vanishing pressure $p$ . Since $\mu = \rho c ^ { 2 } + \epsilon$ , where $\rho$ is the proper mass density and $\epsilon$ is the proper density of internal energy, we see that we can effectively set $\epsilon = 0$ , or equivalently set the internal energy per unit mass $\Pi$ to zero. The conserved mass density is

$$
\rho ^ { * } = m \delta \bigl ( \mathbf { x } - \boldsymbol { r } ( t ) \bigr ) .
$$

The fluid’s velocity field, in this case, reduces to the particle’s velocity $\pmb { v } ( t )$ .

The preceding description applies to a single particle. For a system of $N$ particles we add the contributions from each particle, and the conserved mass density becomes

$$
\rho ^ { * } = \sum _ { A } m _ { A } \delta \big ( \pmb { x } - \pmb { r } _ { A } ( t ) \big ) ,
$$

with $m _ { A }$ denoting the mass of each particle, and $\pmb { r } _ { A } ( t )$ the individual trajectories. For the system we still have

$$
\Pi = p = 0 ,
$$

and the velocity field reduces to the individual velocities ${ \pmb v } _ { A } ( t )$ .

# 9.6.2 Regularization

Equation (9.261) implies that each “body” can be assigned a zero integrated pressure $P _ { A }$ and a zero internal energy $E _ { A } ^ { \mathrm { i n t } }$ . The internal kinetic energy $\mathcal { T } _ { A }$ vanishes also, and the equilibrium condition of Eq. (9.12) indicates that the gravitational potential energy $\Omega _ { A }$ must also be assigned a value of zero. This sensible conclusion, however, creates a mathematical inconsistency.

Going back to the definition of Eq. (9.8), the potential-energy integral is

$$
\Omega _ { A } = - \frac { 1 } { 2 } G \int _ { A } \frac { \rho ^ { * } \rho ^ { * \prime } } { | { \boldsymbol x } - { \boldsymbol x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } d ^ { 3 } x ,
$$

where $\rho ^ { * }$ stands for $\rho ^ { * } ( t , \boldsymbol { x } )$ , while $\rho ^ { * \prime }$ stands for $\rho ^ { * } ( t , \boldsymbol { x } ^ { \prime } )$ . The integral involves a product of delta functions, and its value is mathematically ill-defined. It is not clear, therefore, that $\Omega _ { A }$ can be set equal to zero. To explore this we substitute $m _ { A } \delta ( { \pmb x } - { \pmb r } _ { A } )$ for $\rho ^ { * }$ , $m _ { A } \delta ( { \pmb x } ^ { \prime } - { \pmb r } _ { A } )$ for $\rho ^ { * \prime }$ , and we integrate with respect to $d ^ { 3 } x ^ { \prime }$ ; the result is

$$
\Omega _ { A } = - \frac 1 2 G m _ { A } ^ { 2 } \int _ { A } \frac { \delta ( \pmb x - \pmb r _ { A } ) } { | \pmb x - \pmb r _ { A } | } d ^ { 3 } \pmb x ,
$$

and we see why the integral is ill-defined: the quantity $\delta ( \pmb { x } - \pmb { r } _ { A } ) / | \pmb { x } - \pmb { r } _ { A } |$ is not defined as a distribution, and a blind evaluation would return $1 / 0$ . This mathematical difficulty illustrates rather well the spectacular failure of the point particle to provide a sensible model for an extended body in general relativity; the non-linearity of the field equations simply won’t allow it.

All is not lost, however. We can reconcile the diverging values for $\Omega _ { A }$ if we introduce the seemingly nonsensical regularization prescription

$$
\frac { \delta ( \pmb { x } - \pmb { r } _ { A } ) } { | \pmb { x } - \pmb { r } _ { A } | } \equiv 0 .
$$

With this rule the integral becomes well-defined, and we arrive at the desired result, $\Omega _ { \cal A } = 0$ . As we shall see, the regularization prescription is the only additional rule that is required to make sense of all the ill-defined integrals that we shall encounter; and with this prescription we shall be able to recover the metric of Eq. (9.81) on the basis of the point-particle model.

The regularization prescription of Eq. (9.264) is a special case of a more powerful method known as Hadamard regularization, which was used to great benefit by our friends Luc Blanchet and Thibault Damour in their work (along with their collaborators) on high-order post-Newtonian theory. The method works as follows.

Let $F ( x ; r )$ be a function of $_ x$ that diverges when $_ x$ approaches the point $r$ . Specifically, assume that its behavior near $x = r$ is given by the Laurent series

$$
F ( \pmb { x } ; \pmb { r } ) = \sum _ { n = 0 } ^ { n _ { \operatorname* { m a x } } } s ^ { - n } f _ { n } ( \pmb { n } ; \pmb { r } ) + O ( s ) ,
$$

where $\pmb { s } : = \pmb { x } - \pmb { r }$ , $s : = | \pmb { x } - \pmb { r } |$ , and $\pmb { n } : = \pmb { s } / s$ . The function therefore diverges as $s ^ { - n _ { \operatorname* { m a x } } }$ when $x  r$ , and it clearly does not have a well-defined value at $x = r$ . We regularize it by extracting its partie finie at the singular point $x = r$ . This is defined by

$$
\lfloor F \rfloor ( \pmb { r } ) : = \frac { 1 } { 4 \pi } \int f _ { 0 } ( \pmb { n } ; \pmb { r } ) d \Omega ( \pmb { n } ) ,
$$

in which $d \Omega ( n )$ is an element of solid angle in the direction of the unit vector $\pmb { n }$ . Thus, the partie finie of $F$ is the angular average of the zeroth term $f _ { 0 } ( \pmb { n } ; \pmb { r } )$ in its Laurent series. The partie finie can be used to make sense of the product of $F$ with the delta function $\delta ( x - r )$ : We declare that

$$
F ( { \pmb x } ; { \pmb r } ) \delta ( { \pmb x } - { \pmb r } ) \equiv \lfloor F \rfloor ( { \pmb r } ) \delta ( { \pmb x } - { \pmb r } ) .
$$

It follows immediately from this rule that $\begin{array} { r } { \int F ( { \pmb x } ; { \pmb r } ) \delta ( { \pmb x } - { \pmb r } ) d ^ { 3 } x = \lfloor F \rfloor ( { \pmb r } ) . } \end{array}$