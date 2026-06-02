Collecting results, we find that the total energy of a system of isolated bodies is given by

$$
\begin{array} { l } { { \displaystyle { E = \sum _ { A } E _ { A } + \sum _ { A } \frac { 1 } { 2 } m _ { A } v _ { A } ^ { 2 } - \frac { 1 } { 2 } \sum _ { A } \sum _ { B \ne A } \frac { G m _ { A } m _ { B } } { r _ { A B } } } } } \\ { { \displaystyle { ~ - \frac { 1 } { 2 } \sum _ { A } \sum _ { B \ne A } \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \Big [ ( - 1 ) ^ { \ell } G m _ { A } I _ { B } ^ { \{ L \} } + G m _ { B } I _ { A } ^ { \{ L \} } \Big ] \partial _ { L } ^ { A } \Big ( \frac { 1 } { r _ { A B } } \Big ) } } } \\ { { \displaystyle { ~ - \frac { 1 } { 2 } \sum _ { A } \sum _ { B \ne A } \sum _ { \ell = 2 } ^ { \infty } \sum _ { \ell = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell ^ { \prime } } } { \ell ! \ell ^ { \prime } ! } G I _ { A } ^ { \{ L \} } I _ { B } ^ { \{ L ^ { \prime } \} } \partial _ { L L } ^ { A } \Bigg ( \frac { 1 } { r _ { A B } } \Bigg ) , } } } \end{array}
$$

where $E _ { A } : = T _ { A } + \Omega _ { A } + E _ { A } ^ { \mathrm { i n t } }$ is the self-energy of body $A$ . The manipulations following Eq. (1.67) can immediately be adapted to each body, and the conclusion is that each selfenergy is individually conserved. Because the term $\sum _ { A } E _ { A }$ merely contributes an irrelevant constant to $E$ , it can be safely removed from a conventional accounting of total energy, which holds that the energy should vanish when $v _ { A } \to 0$ and $r _ { A B }  \infty$ . In the final analysis we shall retain only the center-of-mass kinetic energies and the mutual interaction energies in Eq. (1.213).

When the bodies are spherical, so that $I _ { A } ^ { \langle L \rangle } = 0$ for $\ell \neq 0$ , the total energy reduces to

$$
E = \sum _ { A } { \frac { 1 } { 2 } } m _ { A } v _ { A } ^ { 2 } - { \frac { 1 } { 2 } } \sum _ { A } \sum _ { B \neq A } { \frac { G m _ { A } m _ { B } } { r _ { A B } } } ,
$$

the familiar expression for a system of point masses.

# 1.6.7 Equations of motion for binary systems

We next specialize the general discussion of this section to a system of two bodies. Our binary system consists of a first body of mass $m _ { 1 }$ and multipole moments $I _ { 1 } ^ { \langle L \rangle }$ at a position $r _ { 1 }$ , and a second body of mass $m _ { 2 }$ and multipole moments $I _ { 2 } ^ { \langle L \rangle }$ at a position $r _ { 2 }$ . The total mass of the binary system is $m : = m _ { 1 } + m _ { 2 }$ . In place of $r _ { 1 }$ and $r _ { 2 }$ it is useful to work with the barycenter position

$$
\pmb { R } : = \frac { m _ { 1 } } { m } \pmb { r } _ { 1 } + \frac { m _ { 2 } } { m } \pmb { r } _ { 2 } ,
$$

and the relative separation

$$
r : = r _ { 1 } - r _ { 2 } .
$$

This vector was denoted $r _ { 1 2 }$ in preceding subsections, and we simplify other notations in a similar way by defining

$$
r : = | r | , \qquad n : = r / r .
$$

It is useful to note that $r _ { 2 1 } = - r$ , ${ \pmb n } _ { 2 1 } = - { \pmb n }$ , and that $r _ { 2 1 } = r$ . In addition to the relative separation we also introduce the relative velocity $\pmb { v } : = d \pmb { r } / d t = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ and the relative acceleration

$$
\pmb { a } : = \frac { d ^ { 2 } \pmb { r } } { d t ^ { 2 } } = \pmb { a } _ { 1 } - \pmb { a } _ { 2 } .
$$

Solving for $r _ { 1 }$ and $r _ { 2 }$ , we find that

$$
r _ { 1 } = R + { \frac { m _ { 2 } } { m } } r , \qquad r _ { 2 } = R - { \frac { m _ { 1 } } { m } } r .
$$

The motion of the binary system is determined when $\pmb { R } ( t )$ and $\mathbf { } r ( t )$ are both known as functions of time. The motion of the barycenter is uniform: as we saw at the end of Sec. 1.6.2, it is described by $\pmb { R } ( t ) = \pmb { R } ( 0 ) + \pmb { V } t$ , where $V : = P / m$ is a constant velocity vector. The relative motion is governed by

$$
\begin{array} { c } { { \displaystyle { a ^ { j } = - \frac { G m } { r ^ { 2 } } n ^ { j } + G m \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \Bigg [ \frac { I _ { 1 } ^ { \langle L \rangle } } { m _ { 1 } } + ( - 1 ) ^ { \ell } \frac { I _ { 2 } ^ { \langle L \rangle } } { m _ { 2 } } \Bigg ] \partial _ { j L } \bigg ( \frac { 1 } { r } \bigg ) } } } \\ { { + G m \sum _ { \ell = 2 } ^ { \infty } \sum _ { \ell ^ { \prime } = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell ^ { \prime } } } { \ell ! \ell ^ { \prime } ! } \frac { I _ { 1 } ^ { \langle L \rangle } } { m _ { 1 } } \frac { I _ { 2 } ^ { \langle L ^ { \prime } \rangle } } { m _ { 2 } } \partial _ { j L L ^ { \prime } } \bigg ( \frac { 1 } { r } \bigg ) , } } \end{array}
$$

an effective one-body equation that can easily be obtained from Eq. (1.201). The derivation relies on the fact that $\partial _ { j } ^ { 2 } r _ { 2 1 } ^ { - 1 } = - \partial _ { j } ^ { 1 } r _ { 1 2 } ^ { - 1 } : = - \partial _ { j } r ^ { - 1 }$ ; in this notation $\partial _ { j }$ indicates partial differentiation with respect to the Cartesian coordinate $r ^ { j }$ associated with the relative separation $r$ . From Eq. (1.213) we find that the total energy (excluding self-energies) of a two-body system is given by

$$
\begin{array} { l } { E = \displaystyle \frac { 1 } { 2 } m V ^ { 2 } + \frac { 1 } { 2 } \mu v ^ { 2 } - \frac { G \mu m } { r } } \\ { \displaystyle - G \mu m \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \Bigg [ \frac { I _ { 1 } ^ { ( L ) } } { m _ { 1 } } + ( - 1 ) ^ { \ell } \frac { I _ { 2 } ^ { ( L ) } } { m _ { 2 } } \Bigg ] \partial _ { L } \bigg ( \frac { 1 } { r } \bigg ) } \\ { \displaystyle - G \mu m \sum _ { \ell = 2 } ^ { \infty } \sum _ { \ell ^ { \prime } = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell ^ { \prime } } } { \ell ! \ell ^ { \prime } ! } \frac { I _ { 1 } ^ { ( L ) } } { m _ { 1 } } \frac { I _ { 2 } ^ { ( L ^ { \prime } ) } } { m _ { 2 } } \partial _ { L L ^ { \prime } } \bigg ( \frac { 1 } { r } \bigg ) , } \end{array}
$$

in which $\mu : = m _ { 1 } m _ { 2 } / m$ is the system’s reduced mass.

As a specialization of these equations we assume that the multipole moments of one of the bodies, say body 1, are negligible. This simplification would apply, for example, to a planet orbiting the Sun (the planet has negligible moments), to a satellite orbiting the Earth (the satellite has negligible moments), or to a non-rotating black hole or neutron star orbiting a normal star (the compact object has negligible moments). In this case we find that the relative acceleration simplifies to

$$
a ^ { j } = - \frac { G m } { r ^ { 2 } } n ^ { j } + G m \sum _ { \ell = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \frac { I _ { 2 } ^ { \langle L \rangle } } { m _ { 2 } } \partial _ { j L } \left( \frac { 1 } { r } \right) ,
$$

and the total energy becomes

$$
E = \frac { 1 } { 2 } m V ^ { 2 } + \frac { 1 } { 2 } \mu v ^ { 2 } - \frac { G \mu m } { r } - G \mu m \sum _ { \ell = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \frac { I _ { 2 } ^ { \langle L \rangle } } { m _ { 2 } } \partial _ { L } \left( \frac { 1 } { r } \right) .
$$

For a planet orbiting the Sun, or a spacecraft orbiting the Earth, $m _ { 1 }$ is much smaller than $m _ { 2 }$ , and $m / m _ { 2 } \simeq 1$ . In this case the equations describe the motion of a spherical body in the multipole field of a heavy, central object. In situations involving comparable masses, however, such as a black hole or neutron star orbiting a normal star, the ratio $m / m _ { 2 }$ could be substantially larger than unity, reflecting the fact that the motion of both bodies can be strongly affected by the multipole moments of body 2.

Specializing even further, we now take body 2 to be symmetric about an axis aligned with the unit vector $\pmb { e }$ . The symmetry requires the body’s multipole moments $I ^ { \langle L \rangle }$ to be proportional to the STF tensor $e ^ { \langle L \rangle }$ , so that $I ^ { \langle L \rangle } = \alpha _ { \ell } e ^ { \langle L \rangle }$ for some coefficient $\alpha _ { \ell }$ . We wish to relate this to the dimensionless multipole moments $J _ { \ell }$ introduced in Eq. (1.143). To achieve this we align the $z$ -direction with the vector $\pmb { e }$ and invoke Eqs. (1.112), (1.167), and (1.168). After some algebra we obtain $\alpha _ { \ell } = - m R ^ { \ell } J _ { \ell }$ , so that

$$
I _ { 2 } ^ { \langle L \rangle } = - m _ { 2 } R _ { 2 } ^ { \ell } ( J _ { \ell } ) _ { 2 } e _ { 2 } ^ { \langle L \rangle } ;
$$

Equation (1.222) can then be written as

$$
a ^ { j } = - \frac { G m } { r ^ { 2 } } \left[ n ^ { j } - \sum _ { \ell = 2 } ^ { \infty } \frac { ( 2 \ell + 1 ) ! ! } { \ell ! } ( J _ { \ell } ) _ { 2 } \left( \frac { R _ { 2 } } { r } \right) ^ { \ell } e _ { 2 } ^ { \langle L \rangle } n _ { \langle j L \rangle } \right] ,
$$

after making use of Eq. (1.156) to express the derivatives of $r ^ { - 1 }$ in terms of STF products of the vector $\pmb { n }$ ; the product $e _ { 2 } ^ { \langle L \rangle } n _ { \langle j L \rangle }$ could be further simplified by invoking Eq. (1.160b). With similar manipulations we can show that the total energy becomes

$$
E = { \frac { 1 } { 2 } } m V ^ { 2 } + { \frac { 1 } { 2 } } \mu v ^ { 2 } - { \frac { G \mu m } { r } } \biggl [ 1 - \sum _ { \ell = 2 } ^ { \infty } ( J _ { \ell } ) _ { 2 } \biggl ( { \frac { R _ { 2 } } { r } } \biggr ) ^ { \ell } P _ { \ell } ( e _ { 2 } \cdot n ) \biggr ] ;
$$

to arrive at this result we have made use of Eq. (1.159a) to express $e _ { 2 } ^ { \langle L \rangle } n _ { \langle L \rangle }$ in terms of Legendre polynomials.

For modestly deformed bodies, and for sufficiently large separations, the $\ell = 2$ term dominates in both Eq. (1.225) and Eq. (1.226). In this case the relative acceleration becomes

$$
{ \pmb a } = - \frac { G m } { r ^ { 2 } } \left[ { \pmb n } - \frac 3 2 ( J _ { 2 } ) _ { 2 } \bigg ( \frac { R _ { 2 } } { r } \bigg ) ^ { 2 } \bigg \{ \big [ 5 ( { \pmb e } _ { 2 } \cdot { \pmb n } ) ^ { 2 } - 1 \big ] { \pmb n } - 2 ( { \pmb e } _ { 2 } \cdot { \pmb n } ) { \pmb e } _ { 2 } \bigg \} \right] ;
$$

the expression involves the total mass $m : = m _ { 1 } + m _ { 2 }$ , and it applies to a binary system of arbitrary mass ratio. This equation, the specialization of Eq. (1.220) to a spherical body moving in the monopole and quadrupole field of an axisymmetric body, is the foundation for the study of a number of important phenomena, including the effect of the solar quadrupole moment on the orbit of Mercury, and the precession of the planes of Earth-orbiting satellites. We shall return to these applications in Chapter 3.

# 1.6.8 Spin dynamics

As we saw back in Eq. (1.205), the spin angular momentum of body $A$ is defined by

$$
{ \bf \cal S } _ { { \cal A } } ( t ) : = \int _ { \cal A } \rho ( t , x ) ( x - r _ { { \cal A } } ) \times ( \pmb { v } - \pmb { v } _ { { \cal A } } ) d ^ { 3 } x ,
$$

and it refers to its center-of-mass position $r _ { A }$ and velocity ${ \pmb v } _ { A }$ . In terms of components we use the permutation symbol $\epsilon ^ { j p q }$ to describe the vectorial product, and we write

$$
S _ { A } ^ { j } ( t ) : = \epsilon ^ { j p q } \int _ { A } \rho ( x - r _ { A } ) ^ { p } ( v - v _ { A } ) ^ { q } d ^ { 3 } x .
$$

We wish to find an equation of motion for ${ \pmb S } _ { A } ( t )$ , and we shall proceed by following the general method outlined in Secs. 1.6.2, 1.6.3, and 1.6.4.

We begin by differentiating Eq. (1.229) with respect to $t$ . Exploiting once again the techniques developed in Sec. 1.4.3, we find that

$$
\begin{array} { c } { { \displaystyle \frac { d S _ { { \cal A } } ^ { j } } { d t } = \epsilon ^ { j p q } \displaystyle \int _ { { \cal A } } \rho ( v - v _ { { \cal A } } ) ^ { p } ( v - v _ { { \cal A } } ) ^ { q } d ^ { 3 } x + \epsilon ^ { j p q } \displaystyle \int _ { { \cal A } } \rho ( x - r _ { { \cal A } } ) ^ { p } ( d v / d t - a _ { { \cal A } } ) ^ { q } d ^ { 3 } x } } \\ { { { } } } \\ { { = \epsilon ^ { j p q } \displaystyle \int _ { { \cal A } } \rho ( x - r _ { { \cal A } } ) ^ { p } \displaystyle \frac { d v ^ { q } } { d t } d ^ { 3 } x , ~ ( 1 . 2 ) ~ } } \end{array}
$$

where we have used the fact that $\begin{array} { r } { \int _ { A } \rho ( x - r _ { A } ) ^ { p } d ^ { 3 } x = 0 } \end{array}$ by virtue of the definition of the center-of-mass position. In this we insert Euler’s equation (1.23) and obtain

$$
{ \frac { d S _ { A } ^ { j } } { d t } } = \epsilon ^ { j p q } \int _ { A } \rho ( x - r _ { A } ) ^ { p } \partial _ { q } U d ^ { 3 } x - \epsilon ^ { j p q } \int _ { A } ( x - r _ { A } ) ^ { p } \partial _ { q } p d ^ { 3 } x .
$$

The second term, involving the pressure $p$ , can be integrated by parts; after discarding the boundary term we are left with $\epsilon ^ { j p q } \delta _ { p q } \int _ { A } p d ^ { 3 } x$ , which vanishes identically. We have obtained

$$
\frac { d S _ { A } ^ { j } } { d t } = \epsilon ^ { j p q } \int _ { A } \rho ( x - r _ { A } ) ^ { p } \partial _ { q } U d ^ { 3 } x \ ,
$$

and in this we insert the decomposition of the gravitational potential in terms of internal and external pieces, as in Eq. (1.184). It is easy to show that the contribution from the internal potential,

$$
\epsilon ^ { j p q } \int _ { A } \rho x ^ { p } \partial _ { q } U _ { A } d ^ { 3 } x - \epsilon ^ { j p q } r _ { A } ^ { p } \int _ { A } \rho \partial _ { q } U _ { A } d ^ { 3 } x ,
$$

is in fact zero. The first term vanishes by virtue of Eq. (1.80) (applied to body $A$ instead of the entire $N$ -body system), and the second term vanishes thanks to Eq. (1.187). The evolution of the spin is therefore governed by

$$
\frac { d S _ { A } ^ { j } } { d t } = \epsilon ^ { j p q } \int _ { A } \rho ( x - r _ { A } ) ^ { p } \partial _ { q } U _ { \neg { A } } d ^ { 3 } x ,
$$

which involves the gravitational potential $U _ { \neg { A } } ( t , \pmb { x } )$ produced by the bodies external to $A$ . At this stage we import Eq. (1.193), which provides an expression for $\partial _ { q } U _ { \neg A } ( t , \pmb { x } )$ as a Taylor expansion in powers of $\mathbf { \boldsymbol { x } } - \mathbf { \boldsymbol { r } } _ { A }$ . Inserting this within Eq. (1.233), we obtain

$$
\begin{array} { c } { { \displaystyle { \frac { d S _ { \cal A } ^ { j } } { d t } } = \epsilon ^ { j p q } \sum _ { \ell = 0 } ^ { \infty } \frac { 1 } { \ell ! } I _ { \cal A } ^ { p L } \partial _ { q L } U _ { { \scriptscriptstyle - A } } ( t , { \bf r } _ { \cal A } ) } } \\ { { = \epsilon ^ { j p q } \sum _ { \ell = 0 } ^ { \infty } \frac { 1 } { \ell ! } I _ { \cal A } ^ { \langle p L \rangle } \partial _ { q L } U _ { { \scriptscriptstyle - A } } ( t , { \bf r } _ { \cal A } ) . } } \end{array}
$$

In the second line we allowed ourselves to enclose the indices $p L$ within angular brackets, recognizing that the difference between $I _ { A } ^ { \langle p L \rangle }$ and $I _ { A } ^ { p L }$ involves a number of Kronecker deltas that either (i) force indices contained in $\partial _ { q L }$ to be equal, giving zero when acting on $U _ { \neg A }$ , or (ii) force the derivative operator to be of the form $\partial _ { p q L - 1 }$ , which vanishes when multiplied by $\epsilon ^ { j p q }$ . We next import Eq. (1.199) and obtain

$$
{ \frac { d S _ { A } ^ { j } } { d t } } = G \epsilon ^ { j p q } \sum _ { B \ne A } \sum _ { \ell = 0 } ^ { \infty } \sum _ { \ell ^ { \prime } = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { \ell ^ { \prime } } } { \ell ! \ell ^ { \prime } ! } } I _ { A } ^ { \langle p L \rangle } I _ { B } ^ { \langle L ^ { \prime } \rangle } \partial _ { \langle q L L ^ { \prime } \rangle } ^ { A } \left( { \frac { 1 } { r _ { A B } } } \right) .
$$

To write this in a friendlier form we observe that the terms with $\ell = 0$ make no contributions (because the dipole moment of body $A$ vanishes), that the terms with $\ell ^ { \prime } = 0$ involve $m _ { B }$ only, and that the terms with $\ell ^ { \prime } = 1$ also make no contributions. We can therefore split the sum into two pieces, one linear in the moments of body $A$ , and the other involving products of moments. We have

$$
\begin{array} { l } { \displaystyle \frac { d S _ { A } ^ { j } } { d t } = G \epsilon ^ { j p q } \sum _ { B \neq A } \sum _ { \ell = 1 } ^ { \infty } \frac { 1 } { \ell ! } m _ { B } I _ { A } ^ { \langle p L \rangle } \partial _ { \langle q L \rangle } ^ { A } \left( \frac { 1 } { r _ { A B } } \right) } \\ { \displaystyle \qquad + G \epsilon ^ { j p q } \sum _ { B \neq A } \sum _ { \ell = 1 } ^ { \infty } \sum _ { \ell ^ { \prime } = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell ^ { \prime } } } { \ell ! \ell ^ { \prime } ! } I _ { A } ^ { \langle p L \rangle } I _ { B } ^ { \langle L ^ { \prime } \rangle } \partial _ { \langle q L L ^ { \prime } \rangle } ^ { A } \left( \frac { 1 } { r _ { A B } } \right) , } \end{array}
$$

and this equation determines the behavior of each spin once the multipole moments and the center-of-mass motion of each body are specified.

We next specialize the discussion to an $N$ -body system that consists of a spinning body $A$ with non-vanishing multipole moments, and external bodies $B$ with negligible multipole moments. In addition, we assume that body $A$ is symmetric about an axis aligned with the unit vector $e _ { A }$ . Under these conditions we have that

$$
S _ { \cal A } = S _ { \cal A } e _ { \cal A } , \qquad S _ { \cal A } : = | S _ { \cal A } | ,
$$

and Eq. (1.224) implies that the body’s multipole moments are given by

$$
I _ { A } ^ { \langle L \rangle } = - m _ { A } R _ { A } ^ { \ell } ( J _ { \ell } ) _ { A } e _ { A } ^ { \langle L \rangle } .
$$

This relation is inserted within Eq. (1.236), along with Eq. (1.156), and after some algebra we obtain

$$
\frac { d S _ { A } ^ { j } } { d t } = - \epsilon ^ { j p q } \sum _ { B \neq A } \frac { G m _ { A } m _ { B } } { r _ { A B } } \sum _ { \ell = 1 } ^ { \infty } ( - 1 ) ^ { \ell + 1 } \frac { ( 2 \ell + 1 ) ! ! } { \ell ! } ( J _ { \ell + 1 } ) _ { A } \bigg ( \frac { R _ { A } } { r _ { A B } } \bigg ) ^ { \ell + 1 } e _ { A } ^ { \langle p L \rangle } n _ { A B } ^ { \langle q L \rangle } .
$$

This is simplified with the help of Eq. (1.160b), and we express the final result as

$$
\frac { d \pmb { S } _ { A } } { d t } = - \sum _ { B \neq A } \frac { G m _ { A } m _ { B } } { r _ { A B } } ( \pmb { e } _ { A } \times \pmb { n } _ { A B } ) \sum _ { \ell = 2 } ^ { \infty } ( - 1 ) ^ { \ell } ( J _ { \ell } ) _ { A } \left( \frac { R _ { A } } { r _ { A B } } \right) ^ { \ell } \frac { d P _ { \ell } } { d \mu _ { A B } } ,
$$

in which $P _ { \ell } ( \mu _ { A B } )$ is a Legendre polynomial, and $\mu _ { A B } : = e _ { A } \cdot \pmb { n } _ { A B } .$ . This equation implies that the magnitude of the spin vector stays constant, because according to Eq. (1.237), $d S _ { A } / d t = e _ { A } \cdot d S _ { A } / d t = 0$ . And indeed, we observe that each term in the sum over $B$ would give rise to a precession of $e _ { A }$ in the direction of ${ \pmb n } _ { A B }$ ; after summation the precession is seen to take place in a direction given by a weighted average of all the vectors ${ \pmb n } _ { A B }$ .

As we shall see in Chapter 3, one notable consequence of Eq. (1.240) is the disturbance of the Earth’s axis caused by the coupling of its equatorial bulge with the gravitational fields of the Sun and Moon. This leads to the famous precession of the equinoxes, with its cycle of approximately 26 000 years.

# 1.7 Bibliographical notes

The presentation of the basic equations of Newtonian gravity in Sec. 1.2 follows the standard treatment found in many undergraduate texts, including the venerable Newtonian Mechanics by French (1971). The theory, of course, was created in Newton’s own Principia, which can be accessed in the superb English edition with extensive commentary by Cohen, Whitman, and Budenz (1999). The Eot-Wash torsion balance experiment is described in ¨ Su et al. (1994) and Baessler et al. (1999).

The theory of Green’s functions touched upon in Secs. 1.3 and 1.5 is developed systematically in many textbooks on mathematical methods, including the excellent Mathematical Methods for Physicists by Arfken, Weber, and Harris (2012).

The discussion of Sec. 1.4 relies on elements of fluid mechanics, thermodynamics, and statistical physics. Those are covered in many textbooks. An elegant and sophisticated development of fluid mechanics can be found in the classic Fluid Mechanics by Landau and Lifshitz (1987), and another useful resource is Kundu, Cohen, and Dowling (2011). A comprehensive presentation of thermodynamics and statistical physics can be found in Reif’s Fundamentals of Statistical and Thermal Physics, now available in a new 2008 edition.

The development of multipole expansions to integrate Poisson’s equation in Sec. 1.5 relies on the theory of spherical harmonics, a topic covered in most textbooks on mathematical methods. These developments are virtually identical to those related to the electrostatic potential, which are described in most textbooks on electromagnetism; the most comprehensive is the classic Classical Electromagnetism by Jackson (1998). The use of symmetric-tracefree tensors as substitutes for spherical harmonics was pioneered by Sachs (1961) and Pirani (1964); a systematic treatment can be found in Thorne (1980), and another useful resource is Damour and Iyer (1991). The citation from the Principia is taken from the Cohen, Whitman, and Budenz edition. The book Allen’s Astrophysical Quantities is edited by Cox (2001).

An overview of the GRACE geodesy project, mentioned in Sec. 1.6, can be found at www.csr.utexas.edu/grace/gravity/geodesy.html.

# 1.8 Exercises

1.1 Show explicitly that for a function $f ( t , \pmb { x } , \pmb { x } ^ { \prime } )$ ,

$$
\frac { \partial ^ { 2 } } { \partial t ^ { 2 } } \int \rho ^ { \prime } f d ^ { 3 } x ^ { \prime } = \int \rho ^ { \prime } \bigg ( \frac { \partial ^ { 2 } f } { \partial t ^ { 2 } } + 2 { \pmb v } ^ { \prime } \cdot \nabla ^ { \prime } \frac { \partial f } { \partial t } + \frac { d { \pmb v } ^ { \prime } } { d t } \cdot \nabla ^ { \prime } f + { \pmb v } ^ { \prime } { \pmb v } ^ { \prime } \partial _ { j } \partial _ { k } f \bigg ) d ^ { 3 } x ^ { \prime } .
$$

1.2 Given the Newtonian potential $U ( t , { \boldsymbol { x } } )$ , one can define a superpotential $X ( t , x )$ , a superduperpotential $Y ( t , x )$ , and another superlative potential $Z ( t , x )$ that satisfy the equations

$$
\nabla ^ { 2 } X = 2 U , \qquad \nabla ^ { 2 } Y = 1 2 X , \qquad \nabla ^ { 2 } Z = 3 0 Y .
$$

Find explicit expressions for $X , Y$ , and $Z$ as integrals over the mass density $\rho ( t ,  { \boldsymbol { x } } ^ { \prime } )$ , assuming that $\rho$ vanishes outside some finite region of space.

1.3 Using the expression for the superpotential $X$ obtained in the preceding problem, show that

$$
\begin{array} { l } { \displaystyle \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } X ( t , \pmb { x } ) = - \int \rho ^ { \prime } \frac { d \pmb { v } ^ { \prime } } { d t } \cdot \frac { ( \pmb { x } - \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } \pmb { x } ^ { \prime } } \\ { \displaystyle + \int \frac { \rho ^ { \prime } } { | \pmb { x } - \pmb { x } ^ { \prime } | } \left\{ { v } ^ { \prime 2 } - \frac { [ \pmb { v } ^ { \prime } \cdot ( \pmb { x } - \pmb { x } ^ { \prime } ) ] ^ { 2 } } { | \pmb { x } - \pmb { x } ^ { \prime } | ^ { 2 } } \right\} d ^ { 3 } \pmb { x } ^ { \prime } . } \end{array}
$$

1.4 Prove that

$$
\int \rho ( t , \boldsymbol { x } ) x ^ { j } v ^ { k } d ^ { 3 } \boldsymbol { x } = \frac { 1 } { 2 } \frac { d I ^ { j k } } { d t } + \frac { 1 } { 2 } \epsilon ^ { j k p } J ^ { p } ,
$$

where $I ^ { j k }$ is the quadrupole moment tensor of the mass distribution, and $J ^ { p }$ is the total angular momentum.

1.5 Assuming that $T ^ { \alpha \beta } = 0$ far away from the system, use the equations of hydrodynamics in the form of $\partial _ { \beta } T ^ { \alpha \beta } = 0$ to verify explicitly that the total mass $M$ , momentum $P$ , and angular momentum $\pmb { J }$ of an isolated system are all constant.

1.6 With the same assumptions as in the preceding problem, prove that a statement of the tensorial virial theorem is

$$
\frac { d ^ { 2 } I ^ { j k } } { d t ^ { 2 } } = \int T ^ { j k } d ^ { 3 } x ,
$$

where $\begin{array} { r } { I ^ { j k } : = \int T ^ { t t } x ^ { j } x ^ { k } d ^ { 3 } x . } \end{array}$ . Then show that with $T ^ { j k }$ given by Eq. (1.96), the virial theorem takes the explicit form of Eq. (1.88).

1.7 Use the spherical-harmonic expansion of $| x - x ^ { \prime } | ^ { - 1 }$ to verify that

$$
U ( t , r ) = \frac { G m ( t , r ) } { r } + 4 \pi G \int _ { r } ^ { R } \rho ( t , r ^ { \prime } ) r ^ { \prime } d r ^ { \prime }
$$

for a spherical matter distribution.

1.8 Show explicitly that $\partial _ { j k n p } r ^ { - 1 } = 1 0 5 n ^ { \langle j k n p \rangle } / r ^ { 5 }$ .

1.9 Show that the forms of $n ^ { \langle j k \rangle }$ , $n ^ { \langle j k n \rangle }$ , $n ^ { \langle j k n p \rangle }$ given by Eq. (1.153) satisfy the general formula of Eq. (1.155).

1.10 Find $n ^ { \langle j k n p q \rangle }$ by explicit construction.

1.11 Show that the internal gravitational potential of Eq. (1.129) can be expressed as

$$
U = G \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \bigg [ q ^ { \langle L \rangle } ( t , r ) \partial _ { L } r ^ { - 1 } + p ^ { \langle L \rangle } ( t , r ) x ^ { \langle L \rangle } \bigg ] ,
$$

where

$$
q ^ { \langle L \rangle } ( t , r ) : = \int _ { 0 } ^ { r } \rho ( t , x ^ { \prime } ) x ^ { \prime \langle L \rangle } d ^ { 3 } x ^ { \prime } , \qquad p ^ { \langle L \rangle } ( t , r ) : = \int _ { r } ^ { R } \rho ( t , x ^ { \prime } ) \partial _ { L } r ^ { \prime - 1 } d ^ { 3 } x ^ { \prime } .
$$

In the integral defining $\boldsymbol { q } ^ { \langle L \rangle } ( t , \boldsymbol { r } )$ , the domain of integration is the region of space bounded by a sphere of radius $r : = | { \boldsymbol { x } } |$ . In the integral defining $p ^ { \langle L \rangle } ( t , r )$ , the domain of integration is the region of space bounded inwardly by a sphere of radius $r$ , and outwardly by a sphere of arbitrary radius $R$ that lies outside the distribution of matter.

1.12 For $\ell = 2$ , 3, and 4, show explicitly that $n ^ { \prime } ^ { \langle L \rangle } n ^ { \langle L \rangle } = [ \ell ! / ( 2 \ell - 1 ) ! ! ] P _ { \ell } ( \mu )$ , where ${ \boldsymbol { \mu } } : = { \boldsymbol { n } } ^ { \prime } \cdot { \boldsymbol { n } }$ .

1.13 Fill in all the steps that are required to establish the STF identities of Eqs. (1.159) and (1.160).

1.14 If $_ e$ and $\pmb { n }$ are unit vectors, show that

$$
\begin{array} { c } { { e ^ { \langle q L \rangle } n ^ { \langle p L \rangle } = \displaystyle \frac { \ell ! } { ( 2 \ell + 1 ) ( 2 \ell + 1 ) ! ! } \Biggl [ \delta ^ { p q } \displaystyle \frac { d P _ { \ell } } { d \mu } - \bigl ( e ^ { p } e ^ { q } + n ^ { p } n ^ { q } \bigr ) \displaystyle \frac { d ^ { 2 } P _ { \ell + 1 } } { d \mu ^ { 2 } } } } \\ { { + e ^ { ( p } n ^ { q ) } \biggl ( 2 \displaystyle \frac { d ^ { 2 } P _ { \ell } } { d \mu ^ { 2 } } + ( 2 \ell + 1 ) \displaystyle \frac { d P _ { \ell + 1 } } { d \mu } \biggr ) + ( 2 \ell + 1 ) e ^ { [ p } n ^ { q ] } \displaystyle \frac { d P _ { \ell + 1 } } { d \mu } \Biggr ] , } } \end{array}
$$

where $\mu = e \cdot \pmb { n }$ , and use this to verify Eq. (1.240). Hint: exploit the fact that $e ^ { \left. q L \right. } \propto$ $\partial _ { q L } ( 1 / R )$ and $n ^ { \langle p L \rangle } \partial _ { p L } ( 1 / r )$ , where $R$ and $r$ are independent distance variables.

1.15 Determine the STF tensors $\mathcal { V } _ { \ell m } ^ { \langle L \rangle }$ for $\ell = 1$ , $\ell = 2$ , and $\ell = 3$ , and thereby verify the results listed in Box 1.5.

1.16 Using the general equation of motion (1.201), show explicitly that $\sum _ { A } m _ { A } \pmb { a } _ { A } = \pmb { 0 }$ .

In Chapter 1 we introduced the foundations of Newtonian gravity, and presented the equations that govern the gravitational potential of spherical and nearly spherical bodies. We also examined the center-of-mass motion of extended bodies, and witnessed the remarkable near-decoupling of the external dynamics – the motion of each body as a whole – from the internal dynamics – the internal fluid motions within each body. As we saw in Chapter 1, the details of internal structure, encapsulated in multipole moments of the mass distribution, have a limited influence on the motion of the body as a whole. In this chapter we take the focus away from the external dynamics and examine the internal structure and dynamics of extended, self-gravitating bodies. We shall return to the theme of the near-decoupling of the external and internal dynamics, and reveal the limited influence of the center-of-mass motion and the external bodies on the structure of a selected body.

We begin in Sec. 2.1 with a review of the equations of fluid mechanics that are relevant to the internal dynamics; these are best formulated in the moving reference frame of a selected body $A$ in an $N$ -body system. In Sec. 2.2 we examine the simplest models of internal structure, involving spherical symmetry, assuming that the body is non-rotating and not influenced by external bodies. The simplicity permits a gentle acquisition of much insight into the structure of realistic bodies, and we shall introduce models of increasing complexity: incompressible fluids, polytropes, isothermal spheres, and degenerate fermion gases as models of white dwarfs. Rotation can only be ignored for so long, however, and in Sec. 2.3 we examine the physics of rotating, self-gravitating bodies; we first present elements of a general theory, and then construct models of incompressible, rigidly rotating bodies in hydrostatic equilibrium – the famous Maclaurin spheroids and Jacobi ellipsoids.

While our discussion in Sec. 2.3 is not restricted to slow rotations and small deviations away from spherical symmetry, it is severely limited by the assumption that the fluid is incompressible. In Sec. 2.4 we relax this assumption and formulate a general theory of deformed bodies that accommodates an arbitrary equation of state. Though limited to small deformations, the theory is sufficiently powerful that it can handle any perturbation that causes a deformation from spherical symmetry, including rotation and tidal fields created by external bodies. The theory, therefore, allows us to return to the main theme introduced previously – the near-decoupling of the external and internal dynamics – and to calculate the effects of a tidal field on the body’s structure. The tidal dynamics of extended bodies is examined in some detail in Sec. 2.5, both in the context of static tides (which occur slowly, on a time scale that is long compared with the internal dynamical time scale) and dynamical tides (which occur rapidly).

# 2.1 Equations of internal structure

Our main goal in this chapter is to describe the internal structure of a body $A$ in a system of $N$ bodies, making some assumptions regarding its composition, and accounting for the influence of the external bodies. The motion of the body’s center-of-mass position $\pmb { r } _ { A } ( t )$ was examined in Sec. 1.6, and there we observed that this motion is largely (but not completely) insensitive to the details of internal structure, which are encapsulated in a number of multipole moments $I _ { A } ^ { \langle L \rangle } ( t )$ . In this section we shall find that the internal structure is largely (though not completely) insensitive to the details of the center-of-mass motion and the presence of external bodies.

The foundations of our analysis are the same as in Chapter 1. We take the body to consist of a perfect fluid of mass density $\rho ( t , \boldsymbol { x } )$ , pressure $p ( t , \boldsymbol { x } )$ , and velocity field ${ \pmb v } ( t , { \pmb x } )$ . These quantities are governed by Euler’s equation

$$
\rho \frac { d \pmb { v } } { d t } = \rho \pmb { \nabla } U - \pmb { \nabla } p
$$

and the continuity equation

$$
\frac { \partial \rho } { \partial t } + \nabla \cdot ( \rho \pmb { v } ) = 0 .
$$

The gravitational potential $U ( t , x )$ is produced by all the bodies in the system, and it is governed by Poisson’s equation

$$
\nabla ^ { 2 } U = - 4 \pi G \rho .
$$

The center-of-mass variables of body $A$ were introduced back in Sec. 1.6.2. They comprise the body’s total mass $m _ { A }$ , center-of-mass position $r _ { A }$ , velocity ${ \pmb v } _ { A }$ , acceleration $\pmb { a } _ { A }$ , and multipole moments $I _ { A } ^ { \langle L \rangle }$ . In Sec. 1.6.3 the gravitational potential was decomposed as $U = U _ { A } + U _ { \lnot A }$ , in terms of a piece $U _ { A }$ produced by body $A$ alone – the internal potential – and a piece $U _ { \neg A }$ produced by the remaining bodies – the external potential. In Sec. 1.6 we showed that the acceleration of body $A$ is caused by the external potential, and its general expression was displayed in Eq. (1.200).

To determine the internal motions of body $A$ we focus on the position $\bar { \pmb { x } } : = \pmb { x } - \pmb { r } _ { A }$ of a fluid element relative to the center-of-mass position, and on its relative velocity $\pmb { \bar { v } } : = \pmb { v } - \pmb { v } _ { A }$ . The equation that governs the behavior of the relative velocity is easily obtained from Euler’s equation, and we write it in the form

$$
\rho \frac { d \bar { \bf { v } } } { d t } = \rho \bar { \bf { \nabla } } U _ { A } - \bar { \bf { \nabla } } p + \rho \bar { \bf { \nabla } } \left( U _ { - A } - { \bf { a } } _ { A } \cdot \bar { \bf { x } } \right) ,
$$

in which $\bar { \nabla }$ is the gradient operator in the relative coordinates $\bar { x }$ . The first two terms on the right-hand side account for the purely internal aspects of the body’s dynamics, and the remaining terms account for the influence of the external bodies; the last term, involving the body’s acceleration, is a fictitious force that arises because the body’s center-of-mass frame is not inertial.

We recall from Sec. 1.6.3 that the internal potential is given explicitly by

$$
U _ { A } ( t , { \bar { \mathbf { x } } } ) = G \int _ { A } \frac { \rho ( t , { \bar { \mathbf { x } } } ^ { \prime } ) } { | { \bar { \mathbf { x } } } - { \bar { \mathbf { x } } } ^ { \prime } | } d ^ { 3 } { \bar { x } } ^ { \prime } .
$$

For the external potential we follow the strategy of Sec. 1.6.4 and express it as a Taylor expansion about the body’s center-of-mass. From Eq. (1.192) we get

$$
\begin{array} { l } { { \displaystyle U _ { \scriptscriptstyle { \scriptstyle \{ - { \cal A } } } } ( t , \bar { \boldsymbol { x } } ) = \sum _ { \ell = 0 } ^ { \infty } \frac { 1 } { \ell ! } \partial _ { L } U _ { \scriptscriptstyle { \scriptstyle - { \cal A } } } ( t , { \bf 0 } ) \bar { \boldsymbol { x } } ^ { L } } \ ~  \\ { { \displaystyle ~ = U _ { \scriptscriptstyle { \scriptstyle \{ - { \cal A } } } } ( t , { \bf 0 } ) + g _ { j } ( t ) \bar { x } ^ { j } - \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \mathcal { E } _ { L } ( t ) \bar { x } ^ { L } } ,  \end{array}
$$

where

$$
\begin{array} { r } { g _ { j } ( t ) : = \partial _ { j } U _ { \neg { A } } ( t , \mathbf { 0 } ) , \qquad \mathscr { E } _ { L } ( t ) : = - \partial _ { L } U _ { \neg { A } } ( t , \mathbf { 0 } ) ; } \end{array}
$$

the derivatives of the external potential are evaluated at the center-of-mass $\bar { \boldsymbol { x } } = \mathbf { 0 }$ . The multiindex notation, in which $L$ stands for a collection of $\ell$ individual indices, was introduced back in Sec. 1.5.3. We observe that since the external potential satisfies Laplace’s equation $\nabla ^ { 2 } { U } _ { \neg { A } } = 0$ within the volume occupied by the body, the tensors $\mathcal { E } _ { L }$ are symmetric and tracefree (STF). We observe also that the term $\ell = 0$ in Eq. (2.6) is spatially constant, and that it plays no role whatever in Eq. (2.4); we may therefore remove it from the expansion. The body’s acceleration can also be expressed in terms of the expanded external potential. From Eq. (1.194) we obtain

$$
\begin{array} { r l r } {  { a _ { \cal A } ^ { j } = \sum _ { \ell = 0 } ^ { \infty } \frac { 1 } { \ell ! } \frac { I _ { \cal A } ^ { \langle L \rangle } ( t ) } { m _ { \cal A } } \partial _ { j L } U _ { \neg { \cal A } } ( t , { \bf 0 } ) } } \\ & { } & { = g _ { j } - \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \frac { I _ { \cal A } ^ { \langle L \rangle } ( t ) } { m _ { \cal A } } \mathcal { E } _ { j L } ( t ) ; } \end{array}
$$

the term with $\ell = 1$ vanishes because $I _ { A } ^ { j } = 0$ by virtue of the definition of the center-ofmass.

With Eqs (2.6) and (2.8) we find that the external terms in Euler’s equation combine to give

$$
U _ {  A } ^ { \mathrm { e f f } } : = U _ {  A } - \pmb { a } _ { A } \cdot \bar { \pmb { x } } = - \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \bigg [ \mathcal { E } _ { L } ( t ) \bar { \pmb { x } } ^ { L } - \frac { I _ { A } ^ { \langle L \rangle } ( t ) } { m _ { A } } \mathcal { E } _ { j L } ( t ) \bar { \pmb { x } } ^ { j } \bigg ] .
$$

The cancellation of $g _ { j }$ in this expression implies that the external terms in Eq. (2.4) are much smaller than the internal terms; this is the near-decoupling of the external dynamics from the internal dynamics. With $\bar { r } _ { c }$ denoting a characteristic length scale within the body, we have that the internal potential scales as $U _ { A } \sim G m _ { A } / \bar { r } _ { c }$ . The (effective) external potential is dominated by the $\ell = 2$ term, and this scales as $G m _ { B } \bar { r } _ { c } ^ { 2 } / r _ { A B } ^ { 3 }$ , with $r _ { A B }$ denoting a typical inter-body distance. The ratio of external and internal influences is therefore given by

$$
\frac { U _ { \neg A } ^ { \mathrm { e f f } } } { U _ { A } } \sim \frac { m _ { B } } { m _ { A } } \biggl ( \frac { \bar { r } _ { c } } { r _ { A B } } \biggr ) ^ { 3 } ,
$$

and this is indeed much smaller than unity when the bodies are well separated $( \bar { r } _ { c } \ll r _ { A B } )$

When the body is spherical, or when its deviations from spherical symmetry are sufficiently small to be neglected, the coupling between the higher multipole moments $I _ { A } ^ { \langle L \rangle }$ and $\mathcal { E } _ { j L }$ can be neglected in the acceleration. In such circumstances the effective external potential simplifies to

$$
U _ { \neg A } ^ { \mathrm { e f f } } = - \sum _ { \ell = 2 } ^ { \infty } { \frac { 1 } { \ell ! } } { \mathcal E } _ { L } ( t ) \bar { x } ^ { L } .
$$

We shall return to this expression later on in the chapter.

In the next two sections we shall neglect the external terms and examine the equilibrium states of a completely isolated body. We shall incorporate the external terms in Secs. 2.4 and 2.5, and see how they affect the body’s internal structure.

# 2.2 Equilibrium structure of a spherical body

We begin our exploration of the equilibrium structure of an isolated body with the simplest conceivable model, that of a non-rotating and spherically symmetric object.

# 2.2.1 Equations of body structure

# Hydrostatic equilibrium

The equations that govern the equilibrium structure of an isolated body were already identified back in Sec. 1.5, and they can be recovered from Eq. (2.4) by setting $\bar { v } ^ { j } = 0$ and omitting the external terms. In spherical symmetry the equation of hydrostatic equilibrium is

$$
\frac { d p } { d r } = \rho \frac { d U } { d r } ,
$$

in which we drop the bar over the radial variable and the label $A$ on the gravitational potential to simplify the notation. Poisson’s equation can be integrated to give

$$
\frac { d U } { d r } = - \frac { G m ( r ) } { r ^ { 2 } } ,
$$

in which $m ( r )$ is the mass contained within a sphere of radius $r$ ; this is related to the density by

$$
{ \frac { d m } { d r } } = 4 \pi r ^ { 2 } \rho .
$$

We recall from Sec. 1.5 that according to Eq. (2.13), the potential inside the body can be expressed as

$$
U _ { \mathrm { i n } } = \frac { G m ( r ) } { r } + 4 \pi G \int _ { r } ^ { R } \rho ( r ^ { \prime } ) r ^ { \prime } d r ^ { \prime } ,
$$

in which $R$ is the body’s radius, at which $p = 0$ . The potential outside the body is

$$
U _ { \mathrm { o u t } } = { \frac { G M } { r } } ,
$$

in which $M : = m ( r = R )$ is the body’s total mass. Again we adjust the notation employed in Sec. 2.1 and denote the total mass $M$ instead of $m _ { A }$ ; this switch of notation was also made in Chapter 1.

# Equation of state; energy production and transport

These equations must be supplemented by an equation of state

$$
p = p ( \rho , T ; X )
$$

that relates the pressure to the density $\rho$ , temperature $T$ , and chemical composition $X$ of the matter making up the body. In addition, equations must be provided to account for energy production and transport within the body. One such equation was already considered back in Sec. 1.4.2, where it was shown that in conditions of thermal equilibrium, the heat-flux vector $\pmb { H }$ and the rate of energy production per unit mass $q$ are related by the conservation equation $\nabla \cdot H = \rho q$ . In spherical symmetry this reduces to

$$
\frac { 1 } { r ^ { 2 } } \frac { d } { d r } ( r ^ { 2 } H ) = \rho q ,
$$

where $H$ is the radial component of $\pmb { H }$ . This equation, in turn, must be supplemented by a relation $q = q ( \rho , T ; X )$ that links the rate of energy production to the local conditions within the fluid. Once $H ( r )$ is known, the temperature profile is determined by the equation of radiative transport,

$$
\frac { d T } { d r } = - \frac { 3 } { 4 a c } \kappa \rho \frac { H } { T ^ { 3 } } ,
$$

where $\kappa$ is the mean opacity, which also depends on the local conditions within the fluid, and $a$ is the radiation constant.

This set of equations is overly simplistic; realistic stellar models (like the standard solar model that describes the structure of our Sun) are far more complicated. Among many simplifying assumptions, we have taken the composition $X$ to be uniform throughout the body; this assumption is violated in a highly evolved star, in which nuclear reactions have produced a large radial variation in the abundances of heavy elements. It is also violated for planets that might have a mantle or crust that cannot be modeled as a perfect fluid. We have also assumed that radiation is the only relevant mechanism of energy transport; this is violated in most main-sequence stars, which harbor large convection zones.

In our simplified picture, a stellar model is constructed by simultaneously integrating Eqs. (2.12), (2.13), (2.14), (2.18), and (2.19). The relevant boundary conditions at $r = 0$ are that $p = p _ { c }$ (the central pressure), $m = 0$ , $H = 0$ , and $T = T _ { c }$ (the central temperature). At the boundary $r = R$ we find that $p = 0$ , $m = M$ , $H = L / ( 4 \pi R ^ { 2 } )$ with $L$ denoting the stellar luminosity, and $T$ achieves its surface value $T ( R )$ . This is a formidable set of equations; $q$ and $\kappa$ are typically provided in tabular form, and the equations must be integrated numerically.

# Virial theorem and other integral properties

The equilibrium configuration must satisfy the virial theorem of Eq. (1.90), which we write in the restricted form

$$
\Omega + 3 P = 0 ,
$$

in which $\begin{array} { r } { \Omega = - \frac { 1 } { 2 } \int \rho U d ^ { 3 } x } \end{array}$ is the body’s gravitational potential energy, and $\textstyle P = \int p d ^ { 3 } x$ is the integrated pressure. We have left the kinetic-energy term out of Eq. (2.20) because we are applying the theorem to a static configuration that has no kinetic energy.

The integrated pressure is $\begin{array} { r } { P = 4 \pi \int _ { 0 } ^ { R } p r ^ { 2 } d r } \end{array}$ for a spherical body, and integration by parts brings this to the form

$$
P = - \frac { 4 \pi } { 3 } \int _ { 0 } ^ { R } \frac { d p } { d r } r ^ { 3 } d r .
$$

Substitution of Eqs. (2.12) and (2.13) produces

$$
3 P = 4 \pi G \int _ { 0 } ^ { R } \rho ( r ) m ( r ) r d r ,
$$

and we wish to show that the right-hand side is an expression for $- \Omega$ . One way to establish this is to insert Eq. (2.15) within the definition of $\Omega$ ; this yields

$$
\Omega = - 2 \pi G \int _ { 0 } ^ { R } \rho m r d r - 8 \pi ^ { 2 } G \int _ { 0 } ^ { R } d r \rho ( r ) r ^ { 2 } \int _ { r } ^ { R } d r ^ { \prime } \rho ( r ^ { \prime } ) r ^ { \prime } ,
$$

which we re-express as

$$
\Omega = - 2 \pi G \int _ { 0 } ^ { R } \rho m r d r - 8 \pi ^ { 2 } G \int _ { 0 } ^ { R } d r ^ { \prime } \rho ( r ^ { \prime } ) r ^ { \prime } \int _ { 0 } ^ { r ^ { \prime } } d r \rho ( r ) r ^ { 2 }
$$

by altering the order of integration in the second term. The right-most integral is recognized as $m ( r ^ { \prime } ) / ( 4 \pi )$ , and the second term becomes $\begin{array} { r } { - 2 \pi G \int _ { 0 } ^ { R } \rho ( r ^ { \prime } ) m ( r ^ { \prime } ) d r ^ { \prime } } \end{array}$ , the same as the first term. Our final expression for $\Omega$ is therefore

$$
\Omega = - 4 \pi G \int _ { 0 } ^ { R } \rho ( r ) m ( r ) r d r ,
$$

and we confirm the validity of Eq. (2.20).

Other integral properties of the equilibrium configuration can be obtained in a similar way. Integration of $d p / d r$ from $r = 0$ to $r = R$ produces $- p _ { c }$ , and substitution of Eqs. (2.12) and (2.13) within the integral reveals that

$$
p _ { c } = G \int _ { 0 } ^ { R } \frac { \rho ( r ) m ( r ) } { r ^ { 2 } } d r .
$$

We next integrate $p r ^ { 3 }$ from the center to the surface. Exploiting integration by parts as we did before, we find that

$$
\int _ { 0 } ^ { R } p r ^ { 3 } d r = { \frac { 1 } { 4 } } G \int _ { 0 } ^ { R } \rho m r ^ { 2 } d r .
$$

But $\rho r ^ { 2 } = ( 4 \pi ) ^ { - 1 } d m / d r$ , and the integrand can be expressed as the total derivative $( 8 \pi ) ^ { - 1 } d m ^ { 2 } / d r$ . Integration produces

$$
M ^ { 2 } = \frac { 3 2 \pi } { G } \int _ { 0 } ^ { R } p ( r ) r ^ { 3 } d r .
$$

# When pressure depends only on density

When the pressure depends only on density, and does not depend on temperature, the main equations of hydrostatic equilibrium decouple from the energy equations, and they can be handled separately. These can be given either as a set of first-order differential equations,

$$
\frac { d p } { d r } = - \rho \frac { G m } { r ^ { 2 } } , \qquad \frac { d m } { d r } = 4 \pi r ^ { 2 } \rho ,
$$

or they can be combined into a single second-order differential equation for the pressure,

$$
{ \frac { 1 } { r ^ { 2 } } } { \frac { d } { d r } } \biggl ( { \frac { r ^ { 2 } } { \rho } } { \frac { d p } { d r } } \biggr ) = - 4 \pi G \rho ;
$$

in both cases it is assumed that $\rho$ is given as a function of the pressure. In most applications, especially those involving computational methods, the formulation of Eq. (2.29) is a more practical one. In some applications, however, Eq. (2.30) can be advantageous, as it sometimes leads to a differential equation that can be solved in closed form.

<table><tr><td>Box 2.1</td><td>Newtonian gravity, neutrinos,and the Sun</td></tr><tr><td></td><td>One of the most surprising successes ofthe standard solar model, with its foundation grounded in Newtonian gravity, was the role it played in the discovery of neutrino oscilltions.The chain of nuclear reactions that converthydrogen to heliumin the Sun produces neutrinos asa by-product.In 1964, Raymond Davis Jr.and John Bahcallproposed an experiment to measure the flux of high-energy neutrinos from the decay of 8B produced in a side chain of the solar nuclear reactions. These neutrinos are able to convert 37Cl to radioactive 37Ar. The experiment involved a swimming-pool sized container of ordinary cleaning fluid (CCl4),from which Davis could extract minute amounts of37Ar (a few atoms per month) using speciallydesigned chemical techniques. Beginning in 1968,Davis reported that the flux of neutrinos was about one third of what was expected from standard solar models. While there was initial skepticism of his result, the &quot;solar neutrino problem&quot;survived</td></tr></table>

Suspicion fell on the solar models used to predict the neutrino flux. To construct a solar model is an exceedngly complicated task. In addition to Newtonian gravity, one must provide the initial elemental abundances from which the Sun was formed, input all the relevant nuclear reactions with their measured rates, incorporate the correct heat transfer from core to surface (involving both radiative transport and convection), and evolve the Sun for 4.5 billion years. The resulting model must match the current solar luminosity and the surface elemental abundances. The reaction rates in the solar core are extremely sensitive to temperature; a $1 \%$ change in temperature can induce a $3 0 \%$ change in the neutrino flux from $^ { 8 } { \sf B } .$ Decades of reanalyses and refinements of the solar models failed to resolve the solar neutrino problem.

Meanwhile, developments in particle physics opened the possibility that neutrinos might not be strictly massless. As a consequence, they could undergo “neutrino oscillations,” whereby an electron neutrino transmutes into a muon neutrino (and to a smaller extent into a tau neutrino) and back. Mikheev, Smirnov and Wolfenstein showed that this effect, while operative in vacuum, could be enhanced during passage through matter, such as the solar interior. The experimental results could be explained if a sufficient number of the initial $^ { 8 } { \sf B }$ electron neutrinos had converted to muon or tau neutrinos, because the conversion of $^ { 3 7 } \mathrm { { C } }$ to $^ { 3 7 } \mathsf { A r }$ is induced only by electron neutrinos.

The solution to the solar neutrino problem was provided by new solar neutrino experiments, notably Kamiokande and super-Kamiokande in Japan, GALLEX in Germany, SAGE in Russia, and SNO in Canada. All the experiments confirmed the deficit of solar electron neutrinos. But the Japanese and Canadian experiments were sensitive to all three types of neutrinos, and SNO could actually distinguish between the different varieties of neutrinos; they ultimately verified that the total flux of neutrinos agreed completely with the predictions of the solar models based on Newtonian gravity.

# 2.2.2 Incompressible fluid

The simplest equilibrium structure is obtained when one assumes that the fluid is incompressible, that is, that the mass density is uniform throughout the body. We express this mathematically as

$$
\rho ( r ) = \left\{ \begin{array} { l l } { \rho _ { 0 } } & { r \le R } \\ { 0 } & { r > R } \end{array} \right. ,
$$

where $\rho _ { 0 }$ is a constant. Another way of expressing this is $\rho ( r ) = \rho _ { 0 } \Theta ( R - r )$ , with $\Theta$ denoting the Heaviside step function. The pressure of an incompressible fluid is unrelated to the density, and it must be determined by integrating the equation of hydrostatic equilibrium. The incompressible fluid is an exceedingly crude and entirely unphysical model – it leads, for example, to a formally infinite speed of sound within the body. Nevertheless, its simplicity makes it an attractive starting point for a study of equilibrium structures, and we shall have many occasions to return to it in this chapter.

From Eq. (2.14) we find that the mass function within the body is given by

$$
m ( r ) = \frac { 4 \pi } { 3 } \rho _ { 0 } r ^ { 3 } = M ( r / R ) ^ { 3 } ,
$$

with

$$
M = \frac { 4 \pi } { 3 } \rho _ { 0 } R ^ { 3 }
$$

denoting the total mass. From Eqs. (2.12) and (2.13) we find that the pressure profile is given by

$$
p ( r ) = p _ { c } ( 1 - r ^ { 2 } / R ^ { 2 } ) ,
$$

with

$$
p _ { c } = { \frac { 2 \pi } { 3 } } G \rho _ { 0 } ^ { 2 } R ^ { 2 } = { \frac { 3 } { 8 \pi } } { \frac { G M ^ { 2 } } { R ^ { 4 } } }
$$

denoting the central pressure $p ( r = 0 )$ ; the constant of integration was chosen so that $p ( r )$ properly vanishes at the boundary $r = R$ . And from Eq. (2.15) we find that the gravitational potential inside the body is given by

$$
U _ { \mathrm { i n } } = { \frac { G M } { 2 R } } \big ( 3 - r ^ { 2 } / R ^ { 2 } \big ) ;
$$

outside the body it takes the usual form $U _ { \mathrm { o u t } } = G M / r$ , and the potential is continuous (though not differentiable) at $r = R$ .

Evaluation of Eq. (2.25) reveals that the gravitational potential energy of an incompressible body is

$$
\Omega = - \frac { 3 } { 5 } \frac { G M ^ { 2 } } { R } ,
$$

and by virtue of the virial theorem, the integrated pressure is $\begin{array} { r } { P = - \frac { 1 } { 3 } \Omega = \frac { 1 } { 5 } G M ^ { 2 } / R } \end{array}$

# 2.2.3 Polytropes and the Lane–Emden equation

# Polytropic equation of state and polytropes

A polytrope is a body in hydrostatic equilibrium for which the matter satisfies the polytropic equation of state

$$
p = K \rho ^ { \Gamma } , \Gamma : = 1 + 1 / n ,
$$

where $K$ and $\Gamma$ are constants; the related constant $n$ is called the polytropic index. We first encountered this equation of state near the end of Sec. 1.4.2, where it was shown to result from thermal equilibrium when the energy density $\epsilon$ of a fluid element is related to the pressure $p$ by $\epsilon = n p$ (note that $n$ was denoted $\eta$ in Sec. 1.4.2). Equation (2.38) is an example of an equation of state that is independent of temperature, which implies that an equilibrium configuration can be constructed without having to consider the equations of energy production and transport.

Polytropes have the advantage of being more physical than models involving an incompressible fluid, but they are still a far cry from representing a realistic stellar structure. Nevertheless, they were studied extensively in the 19th and early $2 0 \mathrm { { t h } }$ century in an effort to gain insight into stellar astrophysics at a time when almost nothing was known about how stars actually operate; the simplicity of Eq. (2.38) encouraged the development of a rich body of work that may not be directly applicable to real stars (although we shall see the connection with white dwarfs later in this section), but is nevertheless beautiful and worthy of study. This effort was initiated by Lord Kelvin, who noted that Eq. (2.38) should apply to a star in convective equilibrium. The study of stellar structure based on the polytropic equation of state was taken up by Lane and developed systematically by Ritter. The work, as it stood in 1907, was summarized in a treatise by Emden, and it was passed on (with further developments) to later generations by Chandrasekhar (1958) in his classic text $A n$ introduction to the study of stellar structure.

# Scales

Our goal is to integrate the equations of hydrostatic equilibrium, either Eqs. (2.29) or Eq. (2.30), for a fluid with a polytropic equation of state. Before getting started with this task it is helpful to introduce a number of scaling quantities that are relevant to this problem. We have

$$
\begin{array} { r l } & { \rho _ { c } : = \mathrm { c e n t r a l ~ d e n s i t y } , } \\ & { p _ { c } : = \mathrm { c e n t r a l ~ p r e s s u r e } , } \\ & {  { \boldsymbol } _ { r _ { 0 } } : = \mathrm { l e n g t h ~ s c a l e } , } \\ & {  { \boldsymbol } _ { m _ { 0 } } : = \mathrm { m a s s ~ s c a l e } . } \end{array}
$$

While $\rho _ { c }$ and $p _ { c }$ provide their own definitions, with the equation of state giving $\mathit { p _ { c } } =$ Kρ 1+1/n c , r and $m _ { 0 }$ must still be determined. To define $m _ { 0 }$ we simply note that it must scale as $\rho _ { c } r _ { 0 } ^ { 3 }$ and insert a convenient numerical factor; we set

$$
m _ { 0 } : = 4 \pi \rho _ { c } r _ { 0 } ^ { 3 } .
$$

To define $r _ { 0 }$ we appeal to the equation of hydrostatic equilibrium, $d p / d r = - G \rho m / r ^ { 2 }$ , and note that the left-hand side scales as $p _ { c } / r _ { 0 }$ while the right-hand side scales as $G \rho _ { c } m _ { 0 } / r _ { 0 } ^ { 2 }$ ; inserting a convenient numerical factor, we set

$$
r _ { 0 } ^ { 2 } : = \frac { ( n + 1 ) p _ { c } } { 4 \pi G \rho _ { c } ^ { 2 } } = \frac { ( n + 1 ) K } { 4 \pi G } \rho _ { c } ^ { ( 1 - n ) / n } .
$$

Combining this with Eq. (2.40), we find that the mass scale takes the explicit form

$$
m _ { 0 } = \frac { ( n + 1 ) ^ { 3 / 2 } K ^ { 3 / 2 } } { ( 4 \pi ) ^ { 1 / 2 } G ^ { 3 / 2 } } \rho _ { c } ^ { ( 3 - n ) / ( 2 n ) } .
$$

From Eqs. (2.40) and (2.41) we also get $G m _ { 0 } / r _ { 0 } = ( n + 1 ) p _ { c } / \rho _ { c }$ , a useful relation among the various scales. Other relations are

$$
p _ { c } = \frac { ( 4 \pi ) ^ { 1 / 3 } G } { n + 1 } \rho _ { c } ^ { 4 / 3 } m _ { 0 } ^ { 2 / 3 }
$$

and

$$
\frac { m _ { 0 } ^ { n - 1 } } { r _ { 0 } ^ { n - 3 } } = \frac { 1 } { 4 \pi } \biggl [ \frac { ( n + 1 ) K } { G } \biggr ] ^ { n } ,
$$

which reveals that $m _ { 0 } ^ { n - 1 } / r _ { 0 } ^ { n - 3 }$ is actually independent of the central density $\rho _ { c }$

# Dimensionless variables and Lane–Emden equation

Having introduced the relevant scales, the next step is to express the equations of hydrostatic equilibrium in dimensionless and scale-free form. We introduce

$$
\xi : = r / r _ { 0 }
$$

as a dimensionless radial variable, and

$$
\mu : = m / m _ { 0 }
$$

as a dimensionless mass function. We also write

$$
\rho : = \rho _ { c } \theta ^ { n } ,
$$

and adopt $\theta$ as a dimensionless substitute for the density function. For the pressure we then have

$$
p = p _ { c } \theta ^ { n + 1 } ,
$$

in accordance with the equation of state of Eq. (2.38).

With these variables Eqs. (2.29) become

$$
\frac { d \theta } { d \xi } = - \frac { \mu } { \xi ^ { 2 } } , \frac { d \mu } { d \xi } = \xi ^ { 2 } \theta ^ { n } .
$$

These equations are integrated outward from $\xi = 0$ , where the boundary conditions

$$
\theta ( \xi = 0 ) = 1 , \qquad \mu ( \xi = 0 ) = 0
$$

are imposed. Integration proceeds until $\theta = 0$ at $\xi = \xi _ { 1 }$ , which marks the body’s boundary, where both the pressure and density vanish. The body’s total mass is then

$$
M = m _ { 0 } \mu _ { 1 } ,
$$

with $\mu _ { 1 } : = \mu ( \xi = \xi _ { 1 } )$ , while the body’s radius is

$$
R = r _ { 0 } \xi _ { 1 } .
$$

From Eqs. (2.40), (2.51), and (2.52) it is easy to see that the mean density of a polytrope is given by

$$
\bar { \rho } : = \frac { 3 M } { 4 \pi R ^ { 3 } } = \rho _ { c } \bigg ( \frac { 3 \mu _ { 1 } } { \xi _ { 1 } ^ { 3 } } \bigg ) .
$$

It is useful to note that according to Eq. (2.49), $\mu _ { 1 } = - \xi _ { 1 } ^ { 2 } \theta ^ { \prime } ( \xi _ { 1 } )$ , in which a prime indicates differentiation with respect to $\xi$ .

As in Eq. (2.30), the equations displayed in Eq. (2.49) can be combined into a single, second-order differential equation for the density variable $\theta$ . This equation,

$$
\frac 1 { \xi ^ { 2 } } \frac d { d \xi } \biggl ( \xi ^ { 2 } \frac { d \theta } { d \xi } \biggr ) = - \theta ^ { n } ,
$$

<table><tr><td colspan="3">Table 2.1 Numerical integration of the Lane-Emden equation for various polytropes.The first column lists the polytropic index n,and the second column lists Γ = 1+1/n.The third column lists1,the value of the radial variable at which θ = 0.The fourth column lists μ1, the value of the dimensionless mass function at  = $1.</td></tr><tr><td>n r</td><td>m1</td><td>μ1</td></tr><tr><td>1/2 3</td><td>2.752698054</td><td>3.788651185</td></tr><tr><td>2/3</td><td>5/2 2.871323871</td><td>3.538747902</td></tr><tr><td>1</td><td>2 3.141592654</td><td>3.141592654</td></tr><tr><td>3/2</td><td>5/3 3.653753736</td><td>2.714055120</td></tr><tr><td>2</td><td>3/2 4.352874596</td><td>2.411046012</td></tr><tr><td>3</td><td>4/3 6.896848619</td><td>2.018235951</td></tr><tr><td>4</td><td>5/4 14.97154635</td><td>1.797229914</td></tr></table>

is the famous Lane–Emden equation. For most applications the first-order formulation of Eq. (2.49) is more practical, but as we shall see below, for selected values of $n$ Eq. (2.54) leads to a simple differential equation that can be integrated exactly.

# Properties of polytropes

Because Eqs. (2.49) and (2.54) are independent of $K$ and $\rho _ { c }$ , they can be integrated once and for all for any selected value of $n$ ; the solutions are scale-free and independent of both $K$ and $\rho _ { c }$ . For a given $n$ and $K$ (that is, for a given equation of state), the solution gives rise to an entire family of stellar models parameterized by the central density $\rho _ { c }$ . As Eq. (2.42) reveals, the mass $M = m _ { 0 } \mu _ { 1 }$ increases with $\rho _ { c }$ when $n < 3$ , but it decreases with increasing density when $n > 3$ . From Eq. (2.41) we observe that the radius $R = r _ { 0 } \xi _ { 1 }$ increases with $\rho _ { c }$ when $n < 1$ , but that it decreases with increasing density when $n > 1$ . Combining these statements, we find that the mass increases with the radius when $n < 1$ and $n > 3$ , while it decreases with increasing radius when $1 < n < 3$ . Note that when $n = 3$ (or $\Gamma = 4 / 3$ ), the mass turns out to be independent of the central density; we shall come back to this observation in our study of white dwarfs. Note also that when $n = 1$ (or $\Gamma = 2$ ), it is the radius that becomes independent of the central density.

In Box 2.2 we describe how the Lane–Emden equations can be integrated numerically, and in Table 2.1 we display the results of such numerical integrations. In Fig. 2.1 we present plots of the density as a function of radius. The figure shows that as $n$ increases and $\Gamma$ decreases, so that the equation of state becomes increasingly soft, the polytropes become centrally dense, with a density profile that falls off increasingly rapidly away from $r = 0$ . For stiffer equations of state (for $n$ small and $\Gamma$ large), the density becomes increasingly uniform.

![](images/c6735919be54472ceebc91fa73eb3b10bd84ecd4769a54573401464bfe1e6279.jpg)

# Fig. 2.1

Density versus radius for various polytropes. The density is normalized to the central density $\rho _ { c } ,$ and the radius is normalized to the body radius $R$

# Box 2.2

Equations (2.49) must be integrated outward from $\xi = 0$ , and the boundary conditions are $\theta ( 0 ) = 1$ and $\mu ( 0 ) = 0 . \mathtt { A }$ difficulty is immediately encountered with $d \theta / d \xi$ , which evaluates to 0/0 at $\xi = 0$ ; since $\mu { \mathfrak { g } } { \mathfrak { o e s } }$ to zero as $\scriptstyle { \frac { 1 } { 3 } } \xi ^ { 3 }$ , the equation is actually well-behaved at the center, but this formulation of the equations is ill suited to a direct numerical integration.

To avoid this difficulty it is helpful to adopt

$$
\nu : = \frac { \mu } { \xi ^ { 3 } }
$$

as a substitute variable. The differential equations become

$$
\frac { d \theta } { d \xi } = - \xi \nu , \qquad \frac { d \nu } { d \xi } = \frac { 1 } { \xi } ( \theta ^ { n } - 3 \nu ) ,
$$

and the equation for $\theta$ is now better behaved near $\xi = 0$ . The boundary conditions are now $\theta ( 0 ) = 1$ and $\begin{array} { r } { \nu ( 0 ) = \frac { 1 } { 3 } } \end{array}$ . The equation for $\nu$ is still presenting a problem at $\xi = 0$ . To take care of this we perform the transformation

$$
x : = \ln \xi
$$

and adopt $x \ \mathtt { a s a }$ new independent variable. The differential equations become

$$
\frac { d \theta } { d x } = - e ^ { 2 x } \nu , \qquad \frac { d \nu } { d x } = \theta ^ { n } - 3 \nu ,
$$

and they are now well conditioned for numerical integration, except for the fact that integration must proceed from $x = - \infty$ .

The solution to this last difficulty is to start the integration from $x = x _ { \mathrm { i n i t } } ,$ where $x _ { \mathrm { i n i t } }$ is large and negative. Starting values for the dependent variables can then be obtained by expanding $\theta$ and $\nu$ in powers of $\xi$ , with coefficients determined by substituting the approximations within the differential equations. In this way we obtain

$$
\theta = 1 - \frac { 1 } { 6 } \xi ^ { 2 } + \frac { n } { 1 2 0 } \xi ^ { 4 } + O ( \xi ^ { 6 } )
$$

and

$$
\nu = \frac { 1 } { 3 } - \frac { n } { 3 0 } \xi ^ { 2 } + \frac { n ( 8 n - 5 ) } { 2 5 2 0 } \xi ^ { 4 } + { \cal O } ( \xi ^ { 6 } ) .
$$

By choosing $\xi = e ^ { x _ { \mathrm { i n i t } } }$ sufficiently small, the errors can be adjusted to be below a chosen tolerance, and numerical integration of the equations can be attempted with standard methods such as the fourth-order Runge-Kutta algorithm.

Integration proceeds until $x = x _ { 1 } = \ln \xi _ { 1 } ,$ , which marks the first point at which $\theta$ changes sign. To determine the precise location requires finding the root of the equation $\theta ( x ) = 0$ . The simplest way to achieve this is to perform a bisection search: One first identifies an $x _ { 0 }$ such that $\theta ( x _ { 0 } ) > 0$ and an $x _ { 2 }$ such that $\theta ( x _ { 2 } ) < 0 , 5 0$ that $x _ { 1 }$ must be between $x _ { 0 }$ and $x _ { 2 }$ . One next evaluates $\theta ( x )$ at the half-way point. If the sign is positive, then $x _ { 0 }$ is moved to this new position while $x _ { 2 }$ is left where it was; if the sign is negative, then $x _ { 0 }$ is left alone while $x _ { 2 }$ is brought to the new position. The cycle repeats until the interval containing $x _ { 1 }$ has shrunk to a sufficiently small size. At this stage $x _ { 1 }$ is known to sufficient numerical accuracy, and $\mu _ { 1 } = \nu ( x _ { 1 } ) e ^ { 3 x _ { 1 } }$ can be evaluated with the same degree of accuracy.

# Gravitational potential energy

We wish to show that the gravitational potential energy of a polytrope is given by

$$
\Omega = - \frac { 3 } { 5 - n } \frac { G M ^ { 2 } } { R } .
$$

This result and the virial theorem imply that the integrated pressure is

$$
P = - \frac { 1 } { 3 } \Omega = \frac { 1 } { 5 - n } \frac { G M ^ { 2 } } { R } .
$$

These results indicate that models with $n \geq 5$ are peculiar; we shall examine the special case $n = 5$ below, and see what happens when $n > 5$ .

Our starting point is Eq. (2.25), in which we substitute Eqs. (2.45), (2.46), and (2.47). After taking into account Eq. (2.40), we obtain

$$
\Omega = - \frac { G m _ { 0 } ^ { 2 } } { r _ { 0 } } \int _ { 0 } ^ { \xi _ { 1 } } \mu \theta ^ { n } \xi d \xi .
$$

This integral can be written in a number of equivalent forms. We first use Eq. (2.49) to eliminate $\mu$ in favor of $- \xi ^ { 2 } \theta ^ { \prime }$ , in which a prime indicates differentiation with respect to $\xi$ ; after integration by parts we arrive at

$$
\Omega = - \frac { G m _ { 0 } ^ { 2 } } { r _ { 0 } } \frac { 3 } { n + 1 } \int _ { 0 } ^ { \xi _ { 1 } } \xi ^ { 2 } \theta ^ { n + 1 } d \xi .
$$

Proceeding from this expression, we next eliminate $\theta ^ { n }$ in favor of $\mu ^ { \prime } / \xi ^ { 2 }$ and write the integrand as $\theta \mu ^ { \prime }$ ; integration by parts yields

$$
\Omega = - \frac { G m _ { 0 } ^ { 2 } } { r _ { 0 } } \frac { 3 } { n + 1 } \int _ { 0 } ^ { \xi _ { 1 } } \frac { \mu ^ { 2 } } { \xi ^ { 2 } } d \xi ,
$$

after expressing $\theta ^ { \prime }$ as $- \mu / \xi ^ { 2 }$ . If we next return to Eq. (2.57) and eliminate $\theta ^ { n }$ in the same way, we obtain the integrand $\mu \mu ^ { \prime } / \xi$ ; integration by parts produces

$$
\Omega = - \frac { G m _ { 0 } ^ { 2 } } { r _ { 0 } } \biggl [ \frac { \mu _ { 1 } ^ { 2 } } { 2 \xi _ { 1 } } + \frac { 1 } { 2 } \int _ { 0 } ^ { \xi _ { 1 } } \frac { \mu ^ { 2 } } { \xi ^ { 2 } } { d \xi } \biggr ] .
$$

The second term matches the expression displayed in Eq. (2.59), and combining these expressions, we finally arrive at

$$
\Omega = - \frac { 3 } { 5 - n } \frac { G m _ { 0 } ^ { 2 } \mu _ { 1 } ^ { 2 } } { r _ { 0 } \xi _ { 1 } } ,
$$

which is the same statement as Eq. (2.55).

# Special cases with exact solutions

The Lane–Emden equation can be integrated exactly for special values of $n$ . The first such case is $n = 0$ , which is actually a singular limit of the formalism. While Eq. (2.54) is perfectly well behaved when $n = 0$ , the polytropic equation of state is singular, and the density becomes unrelated to the pressure. Accordingly, the definition of $\theta$ provided by Eq. (2.47) breaks down, but we observe that Eq. (2.48) remains meaningful when $n = 0$ ; it becomes $p = p _ { c } \theta$ , and this relation supplies $\theta$ with a new definition. To keep the remaining equations meaningful, we introduce a new density scale $\rho _ { 0 }$ , a new length scale $r _ { 0 }$ , and a new mass scale $m _ { 0 }$ defined by

$$
r _ { 0 } ^ { 2 } = \frac { p _ { c } } { 4 \pi G \rho _ { 0 } ^ { 2 } } , \qquad m _ { 0 } = 4 \pi \rho _ { 0 } r _ { 0 } ^ { 3 } ;
$$

these definitions replace Eqs. (2.40) and (2.41), and the density scale $\rho _ { 0 }$ is unrelated to the central pressure $p _ { c }$ . The dimensionless variables then refer to the new scales: $\xi = r / r _ { 0 }$ , $\theta = p / p _ { c }$ , and $\mu = m / m _ { 0 }$ .

With these changes we find that Eqs. (2.49) or (2.54) apply just as well to the case $n = 0$ . Integration is straightforward, and we find that the solutions are

$$
\theta = 1 - \frac { 1 } { 6 } \xi ^ { 2 } , \qquad \mu = \frac { 1 } { 3 } \xi ^ { 3 } .
$$

These results imply that the pressure vanishes at $\xi = \xi _ { 1 } = \sqrt { 6 }$ , and that the body’s dimensionless mass is $\mu _ { 1 } = 2 \sqrt { 6 }$ Incorporating the scales, we have found that

$$
R = \sqrt { 6 } r _ { 0 } , \qquad M = 2 \sqrt { 6 } m _ { 0 } .
$$

The fact that the mass function is exactly proportional to $r ^ { 3 }$ implies that the density is uniform within the body: at any radius $r$ we have that $\rho = \rho _ { 0 }$ . The $n = 0$ limit of a polytrope, therefore, corresponds to an incompressible body, and the results obtained here are fully compatible with those described in Sec. 2.2.2. Note, in particular, that Eq. (2.55) reduces to Eq. (2.37) when $n = 0$ .

Another case that admits an exact solution is $n = 1$ , corresponding to $\Gamma = 2$ . The general solution to Eq. (2.54) is $\theta = ( c _ { 1 } \sin \xi + c _ { 2 } \cos \xi ) / \xi$ , where $c _ { 1 }$ and $c _ { 2 }$ are integration constants, and imposing the boundary conditions yields

$$
\theta = \frac { \sin \xi } { \xi } , \qquad \mu = \sin \xi - \xi \cos \xi .
$$

These results imply that the boundary is at $\xi = \xi _ { 1 } = \pi$ , and the body’s dimensionless mass is $\mu _ { 1 } = \pi$ . Incorporating the scales of Eqs. (2.41) and (2.42), we find that

$$
R = \sqrt { \frac { \pi K } { 2 G } } , \qquad M = \sqrt { \frac { 2 \pi K } { G } } \rho _ { c } .
$$

We note that $R$ is independent of the central density, while $M$ increases linearly with $\rho _ { c }$ .

A final case that gives rise to an exact solution is $n = 5$ . To find this solution it is helpful to change the dependent variable from $\theta$ to $f : = \theta ^ { - 2 }$ . The Lane–Emden equation becomes

$$
\frac { 1 } { 2 } f f ^ { \prime \prime } - \frac { 3 } { 4 } ( f ^ { \prime } ) ^ { 2 } + \frac { 1 } { \xi } f f ^ { \prime } = 1 ,
$$

in which a prime indicates differentiation with respect to $\xi$ . This is a non-linear differential equation, but a solution can be found by substituting a trial solution of the form $f =$ $\textstyle 1 + \sum _ { p = 1 } ^ { \infty } a _ { p } \xi ^ { 2 p }$ . This reveals that the exact solution is $\textstyle f = 1 + { \frac { 1 } { 3 } } \xi ^ { 2 }$ . In terms of the original variables, we have

$$
\theta = \bigl ( 1 + { \textstyle \frac 1 3 } \xi ^ { 2 } \bigr ) ^ { - 1 / 2 } , \qquad \mu = { \textstyle \frac 1 3 } \xi ^ { 3 } \bigl ( 1 + { \textstyle \frac 1 3 } \xi ^ { 2 } \bigr ) ^ { - 3 / 2 } .
$$

These results imply that the body does not have a well-defined surface: $\theta$ vanishes at $\xi = \xi _ { 1 } = \infty$ . Nevertheless, the total mass is finite and equal to $\mu _ { 1 } = \sqrt { 3 }$ . In this case Eq. (2.42) produces

$$
M = \frac { 1 8 \sqrt { 2 } K ^ { 3 / 2 } } { ( 4 \pi ) ^ { 1 / 2 } G ^ { 3 / 2 } } \frac { 1 } { \rho _ { c } ^ { 1 / 5 } } ,
$$

and we see that $M$ decreases very slowly with an increasing central density $\rho _ { c }$ . We observed previously that Eq. (2.55) for the gravitational potential energy does not apply when $n = 5$ ;

in fact, the equation is meaningless when $n = 5$ and $R = \infty$ , but it is nevertheless true that $\Omega$ is finite in this case. It can also be shown that all polytropes with $n \geq 5$ have an infinite radius.

# 2.2.4 Isothermal spheres

Another equation of state that leads to simple equilibrium configurations is

$$
{ p } = { \frac { \rho k T } { \mu m _ { \mathrm { H } } } } + { \frac { 1 } { 3 } } a T ^ { 4 } ,
$$

in which the temperature $T$ is assumed to be uniform; $\mu$ is the mean atomic number (which is not to be confused with the dimensionless mass function), $m _ { \mathrm { H } }$ is the atomic mass unit, and $a$ is the radiation constant. The first term in the equation of state is the pressure exerted by an ideal gas, and the second term is the radiative pressure. This equation of state is relevant when convection brings large portions of the body into thermal equilibrium at a constant temperature; this is in contrast to radiative equilibrium, where the temperature varies because of radiation transport. The equation of state (without the radiation term) is also adopted in simple models of star clusters, where two-body scattering processes bring the stars into an approximate Maxwellian distribution of velocities, with a common “temperature” related to the velocity dispersion in the cluster.

Because $T$ is constant, the radiation term does not give rise to a pressure gradient, and therefore it does not participate in the hydrostatic equilibrium. So for a given $T$ , the effective equation of state is

$$
p = K \rho ,
$$

where $K : = k T / ( \mu m _ { \mathrm { H } } )$ ; this is a special case of a polytropic equation of state with $\Gamma = 1$ and $n = \infty$ . This limit is too singular to be handled by the Lane–Emden equation, and we must give it a separate treatment.

As usual we introduce the relevant scaling quantities: we have the central density $\rho _ { c }$ , the central pressure $p _ { c } = K \rho _ { c }$ , and we introduce a length scale $r _ { 0 }$ and a mass scale $m _ { 0 }$ with the relations

$$
r _ { 0 } ^ { 2 } : = \frac { p _ { c } } { 4 \pi G \rho _ { c } ^ { 2 } } = \frac { K } { 4 \pi G \rho _ { c } }
$$

and

$$
\begin{array} { r } { m _ { 0 } = 4 \pi \rho _ { c } r _ { 0 } ^ { 3 } . } \end{array}
$$

A useful relation among these quantities is $G m _ { 0 } / r _ { 0 } = p _ { c } / \rho _ { c } = K$ . The scale-free, dimensionless variables are

$$
\xi : = r / r _ { 0 } , \qquad e ^ { - \psi } : = \rho / \rho _ { c } = p / p _ { c } , \qquad \mu : = m / m _ { 0 } .
$$

With these substitutions it is easy to show that the equations of hydrostatic equilibrium, displayed in Eq. (2.29), take the form of

$$
\frac { d \psi } { d \xi } = \frac { \mu } { \xi ^ { 2 } } , \qquad \frac { d \mu } { d \xi } = \xi ^ { 2 } e ^ { - \psi } .
$$

![](images/1b4d58897d45f4f56c53063fbb8540bd3a04ec7a510db24ac198d19659b3e324.jpg)

Plots of the dimensionless density $e ^ { - \psi }$ and rescaled mass $\mu / ( 2 \xi )$ as functions of the dimensionless radius $\xi$ . While the density decreases monotonically with increasing $\xi$ , it does so too slowly for the mass $\mu$ to converge to a finite limit; the figure reveals that $\mu / ( 2 \xi )$ converges, but that the mass increases without bound. For reasons explained in the text, the inset shows a plot of $( \frac { 1 } { 2 } \xi ^ { 2 } e ^ { - \psi } - 1 ) \xi ^ { 1 / 2 }$ as a function of $\mathsf { i o g } \xi$ .

These can be combined into a single, second-order differential equation for $\psi$

$$
{ \frac { 1 } { \xi ^ { 2 } } } { \frac { d } { d \xi } } \biggl ( \xi ^ { 2 } { \frac { d \psi } { d \xi } } \biggr ) = e ^ { - \psi } .
$$

The equations are integrated outward from $\xi = 0$ , with boundary conditions $\psi ( 0 ) = 0$ (so that $e ^ { - \psi } = 1$ at the center) and $\mu ( 0 ) = 0$ ; integration proceeds until $e ^ { - \psi } = 0$ . The equations can be integrated once and for all for any $K$ and central density $\rho _ { c }$ , and the solution describes an entire family of equilibrium structures parameterized by $\rho _ { c }$ . Numerical integration of the equations is facilitated by the tricks described in Box 2.2; it is useful to note that for $\xi \ll 1$ , the functions are well approximated by the expansions $\begin{array} { r } { \psi = \frac 1 6 \xi ^ { 2 } - \frac { 1 } { 1 2 0 } \xi ^ { 4 } + \frac { 1 } { 1 8 9 0 } \xi ^ { 6 } + O ( \xi ^ { 8 } ) } \end{array}$ and $\textstyle \nu : = \mu / \xi ^ { 3 } = \frac { 1 } { 3 } - \frac { 1 } { 3 0 } \xi ^ { 2 } + \frac { 1 } { 3 1 5 } \xi ^ { 4 } + O ( \xi ^ { 6 } )$ .

In Fig. 2.2 we display the results of a numerical integration of Eqs. (2.75). The most important observation is that while the density decreases monotonically with increasing radius, it does so too slowly to give rise to a well-defined surface and a finite mass for the body. In fact, it can be shown that when $\xi \gg 1$ , $e ^ { - \psi }$ behaves as

$$
e ^ { - \psi } = \frac { 2 } { \xi ^ { 2 } } \biggl [ 1 + \frac { \cal { A } } { \xi ^ { 1 / 2 } } \cos \biggl ( \frac { \sqrt { 7 } } { 2 } \ln \xi + \delta \biggr ) + { \cal { O } } ( \xi ^ { - 1 } ) \biggr ] ,
$$

where $A$ and $\delta$ are constants that must be matched to the numerical results. The asymptotic behavior $e ^ { - \psi } \sim 2 / \xi ^ { 2 }$ implies that the mass increases as $\mu \sim 2 \xi$ , and this is confirmed by the numerical results. The figure’s inset shows a plot of $( { \textstyle \frac { 1 } { 2 } } \xi ^ { 2 } e ^ { - \psi } - 1 ) \xi ^ { 1 / 2 } \sim A \cos ( { \textstyle \frac { \sqrt { 7 } } { 2 } } \ln \xi +$ δ), and the plot confirms the existence of logarithmic oscillations of constant amplitude.

These results make it clear that the isothermal equation of state cannot describe a complete star or star cluster. Nevertheless, it is often adopted to model the core of a star or star cluster, where the conditions are approximately isothermal. The model is cut off at some appropriate radius, and the solution is matched to another solution for the outer region of the body, where a different equation of state takes over.

# 2.2.5 White dwarfs

A white dwarf is a low-mass star that has come to the end state of its stellar evolution, following a long life on the main sequence. It is a dead star that is no longer able to support itself with radiative pressure produced by thermonuclear reactions in the core, because these have ceased after virtually all the hydrogen and helium have been converted to heavier elements. As the star starts to shrink (after it has ejected its outer layers), the density increases sufficiently for the electrons to become degenerate, and it is the degeneracy pressure of the electrons that will continue to support the star against further gravitational collapse. White dwarfs have masses typically ranging between $0 . 5 M _ { \odot }$ and $0 . 7 M _ { \odot }$ , with the majority of them tightly clustered around $0 . 6 M _ { \odot }$ ; masses as low as $0 . 2 M _ { \odot }$ and as high as $1 . 3 M _ { \odot }$ have been observed. The typical radius of a white dwarf is of the order of $9 \times 1 0 ^ { 3 } ~ \mathrm { k m }$ , somewhat larger than the Earth; the typical density is of the order of $4 \times 1 0 ^ { 8 } ~ \mathrm { k g } / \mathrm { m } ^ { 3 }$ . A typical white dwarf has a composition dominated by $^ { 1 2 } \mathrm { C }$ and $^ { 1 6 } \mathrm { O }$ . In this section we construct the equation of state for a degenerate electron gas, and we integrate the equations of hydrostatic equilibrium to uncover the internal structure of a white dwarf.

# Conditions for degeneracy and relativity

Electron degeneracy was reviewed briefly in Sec. 1.4.2, where it was shown to result when the temperature $T$ becomes smaller than the Fermi temperature

$$
T _ { \mathrm { F } } = \frac { \hbar ^ { 2 } } { 2 m _ { e } k } \big ( 3 \pi ^ { 2 } n _ { e } \big ) ^ { 2 / 3 } ,
$$

which was first introduced in Eq. (1.42); here $m _ { e }$ is the electron’s mass, and $n _ { e }$ is its number density. This equation reveals that the Fermi temperature is high when the density is high, and these are the conditions that prevail inside a white dwarf.

To turn the criterion $T < T _ { \mathrm { F } }$ into something more useful, we estimate the temperature of a white dwarf by relating it to its pressure and mass density; taking the ideal-gas equation of state as a rough guide, we have $k T \sim p / n _ { e }$ , where $p$ is the pressure within the star. Because the matter is electrically neutral, and because most of the mass is contained in the ions (instead of the electrons), we write $n _ { e } \sim \rho / m _ { \mathrm { H } }$ , in which $\rho$ is the total mass density. With $p \sim G M ^ { 2 } / R ^ { 4 }$ and $\rho \sim M / R ^ { 3 }$ , we find that $k T \sim G m _ { \mathrm { H } } M / R$ . The Fermi temperature, on the other hand, is given by $k T _ { \mathrm { F } } = \hbar ^ { 2 } M ^ { 2 / 3 } / ( m _ { e } m _ { \mathrm { H } } ^ { 2 / 3 } R ^ { 2 } )$ , and the criterion for degeneracy is

$$
M ^ { 1 / 3 } R < \frac { \hbar ^ { 2 } } { G m _ { e } m _ { \mathrm { H } } ^ { 5 / 2 } } ,
$$

or

$$
\left( \frac { M } { M _ { \odot } } \right) ^ { 1 / 3 } \left( \frac { R } { R _ { \odot } } \right) < 1 0 ^ { - 2 }
$$

after inserting the relevant numbers. For the typical white dwarf described previously, the left-hand side evaluates to 0.01, and the criterion is (marginally) satisfied.

The electrons are not only degenerate, they are also relativistic. (We are speaking of special relativity, not general relativity; as Table 1.1 indicates, the gravitational potential is still too modest for general relativity to play a significant role in the structure of white dwarfs.) To estimate the size of the relativistic corrections we examine the quantity $x : =$ $| \pmb { p } | / ( m _ { e } c )$ , the ratio of an electron’s momentum to $m _ { e } c$ ; relativistic effects are important when $x > 1$ . For a degenerate gas the momentum is given by the Fermi momentum, which is linked to the density by the relation (derived below) $n _ { e } = x ^ { 3 } / ( 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } )$ , in which $\lambda _ { e } : = \hbar / ( m _ { e } c )$ is the Compton wavelength of the electron. With this we find that

$$
x \sim { \frac { \lambda _ { e } \rho ^ { 1 / 3 } } { m _ { \mathrm { H } } ^ { 1 / 3 } } } \sim { \frac { \lambda _ { e } } { m _ { \mathrm { H } } ^ { 1 / 3 } } } { \frac { M ^ { 1 / 3 } } { R } } ,
$$

or

$$
x \sim 1 0 ^ { - 2 } \bigg ( \frac { M } { M _ { \odot } } \bigg ) ^ { 1 / 3 } \bigg ( \frac { R _ { \odot } } { R } \bigg )
$$

after inserting the relevant numbers. For the typical white dwarf described previously, we have that $x \sim 1$ , which indicates that relativistic effects are indeed important.

# Equation of state

We wish to construct the equation of state of a degenerate, and relativistic, electron gas. To do this we rely on techniques borrowed from the kinetic theory of gases, which features the distribution function $f ( { \boldsymbol { x } } , { \boldsymbol { p } } )$ as a starting point of most calculations. This is defined so that

$$
\frac { g } { ( 2 \pi \hbar ) ^ { 3 } } f ( { \pmb x } , { \pmb p } ) d ^ { 3 } x d ^ { 3 } { \pmb p }
$$

is the number of particles in a phase-space cell of volume $d ^ { 3 } x d ^ { 3 } p$ at position $_ x$ and momentum $\pmb { p }$ . The factor $g$ is the number of internal states associated with a particle of given momentum, and in the case of an electron (a spin- $\cdot \frac { 1 } { 2 }$ particle), this is equal to 2. It can be shown that the distribution function is a relativistic invariant, so that $_ x$ and $\pmb { p }$ can refer to any Lorentz frame.

The distribution function gives rise to the number density

$$
n _ { e } = \frac { 2 } { ( 2 \pi \hbar ) ^ { 3 } } \int f ( { \pmb x } , { \pmb p } ) d ^ { 3 } { \boldsymbol p } ,
$$

the energy density

$$
\epsilon = \frac { 2 } { ( 2 \pi \hbar ) ^ { 3 } } \int { \cal E } f ( { \bf x } , { \bf p } ) d ^ { 3 } p ,
$$

and the pressure

$$
p = \frac { 1 } { 3 } \frac { 2 } { ( 2 \pi \hbar ) ^ { 3 } } \int | p | v f ( { \pmb x } , { \pmb p } ) d ^ { 3 } p ,
$$

where $E = \sqrt { | { \pmb p } | ^ { 2 } c ^ { 2 } + m _ { e } ^ { 2 } c ^ { 4 } }$ is the relativistic energy, and $v = | p | c ^ { 2 } / E$ the relativistic speed, of a particle with momentum $\pmb { p }$ . The equation for the pressure expresses the fact that pressure is a flux of momentum, and the factor of $\frac 1 3$ reflects the isotropy of the gas. Note that we must be cautious to distinguish the pressure $p$ from the magnitude $| p |$ of the momentum vector.

We are interested in the relation between the pressure $p$ and the number density $n _ { e }$ . To work this out we need an expression for $f$ , and in our case this is given by the famous Fermi–Dirac distribution. To simplify we assume that $T \ll T _ { \mathrm { F } }$ , and adopt the limiting form that applies at zero temperature. This is simple: $f = 1$ when $| p |$ is smaller than the Fermi momentum $p _ { \mathrm { F } }$ , and $f = 0$ when $| p | > p _ { \mathrm { F } }$ . Then the expression for the number density gives rise to $\begin{array} { r } { n _ { e } = 2 ( 2 \pi \hbar ) ^ { - 3 } \int _ { 0 } ^ { p _ { \mathrm { F } } } 4 \pi | \pmb { p } | ^ { 2 } d | \pmb { p } | } \end{array}$ , which integrates to

$$
n _ { e } = \frac { x ^ { 3 } } { 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } } ,
$$

where $x : = p _ { \mathrm { F } } / ( m _ { e } c )$ is a dimensionless version of the Fermi momentum, and $\lambda _ { e } : =$ $\hbar / ( m _ { e } c )$ is the electron’s Compton wavelength. The electron gas is relativistic when $x > 1$ , and Eq. (2.86) indicates that the average inter-particle distance n−1/3 e is then smaller than the Compton wavelength.

The integral for the pressure produces

$$
p = \frac { m _ { e } c ^ { 2 } } { 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } } \phi ( x ) ,
$$

where

$$
\phi ( x ) : = \int _ { 0 } ^ { x } { \frac { y ^ { 4 } d y } { \sqrt { 1 + y ^ { 2 } } } } = { \frac { 3 } { 8 } } \biggl [ x \left( { \textstyle { \frac { 2 } { 3 } } } x ^ { 2 } - 1 \right) \sqrt { 1 + x ^ { 2 } } + \ln \Bigl ( x + \sqrt { 1 + x ^ { 2 } } \Bigr ) \biggr ] .
$$

The function $\phi ( x )$ admits the approximations

$$
\phi ( x ) = \frac { 1 } { 5 } x ^ { 5 } - \frac { 1 } { 1 4 } x ^ { 7 } + { \cal O } ( x ^ { 9 } ) ,
$$

when $x \ll 1$ , and

$$
\phi ( x ) = \frac { 1 } { 4 } x ^ { 4 } - \frac { 1 } { 4 } x ^ { 2 } + O ( 1 ) ,
$$

when $x \gg 1$ . The equation of state is obtained by combining Eq. (2.86) for $n _ { e } ( x )$ with Eq. (2.87) for $p ( x )$ ; in its exact formulation the equation of state is expressed in parametric form.

For our purposes we must relate the pressure to the mass density $\rho$ instead of the number density $n _ { e }$ . To achieve this we return to the discussion of Sec. 1.4.2, and re-introduce the atomic mass unit $m _ { \mathrm { H } }$ and the mean molecular weight per electron $\mu _ { e }$ ; this, we recall, is defined by the relation $\textstyle \mu _ { e } ^ { - 1 } : = \sum _ { i } Z _ { i } X _ { i } / \mathcal { A } _ { i }$ , in which $Z _ { i }$ is the atomic number of an ion of type $i$ , $X _ { i }$ is the mass fraction of this ion, and $\mathbf { \mathcal { A } } _ { i }$ is its atomic mass number. In terms of these quantities we have that $\rho = \mu _ { e } m _ { \mathrm { H } } n _ { e }$ . Combining this with our previous results, we find that the equation of state of a white dwarf is given by

$$
\rho = \frac { \mu _ { e } m _ { \mathrm { H } } } { 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } } x ^ { 3 } , \qquad p = \frac { m _ { e } c ^ { 2 } } { 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } } \phi ( x ) ,
$$

with $\phi ( x )$ given by Eq. (2.88). For a typical white dwarf containing mostly $^ { 1 2 } \mathrm { C }$ $Z = 6$ , $A = 1 2$ ) and $^ { 1 6 } \mathrm { O } \left( Z = 8 , \mathcal { A } = 1 6 \right)$ , the mean molecular weight is $\mu _ { e } = 2$ .

In the non-relativistic regime $x \ll 1$ the approximation of Eq. (2.89) can be exploited, and the equation of state simplifies to

$$
p = K \rho ^ { 5 / 3 } , \qquad K = \frac { ( 3 \pi ^ { 2 } ) ^ { 2 / 3 } \hbar ^ { 2 } } { 5 \mu _ { e } ^ { 5 / 3 } m _ { e } m _ { \mathrm { H } } ^ { 5 / 3 } } ;
$$

this is a polytropic equation of state with $\begin{array} { r } { \Gamma = \frac { 5 } { 3 } } \end{array}$ . In the extreme relativistic regime $x \gg 1$ the approximation of Eq. (2.89) takes over, and the equation of state simplifies to

$$
p = K ^ { \prime } \rho ^ { 4 / 3 } , \qquad K ^ { \prime } = \frac { ( 3 \pi ^ { 2 } ) ^ { 1 / 3 } \hbar c } { 4 \mu _ { e } ^ { 4 / 3 } m _ { \mathrm { H } } ^ { 4 / 3 } } ;
$$

this is another polytropic equation of state with $\textstyle \Gamma = { \frac { 4 } { 3 } }$

# Equations of structure

The scaling quantities relevant to a white-dwarf equilibrium are defined by

$$
\begin{array} { r l } & { p _ { 0 } : = \frac { m _ { e } c ^ { 2 } } { 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } } , } \\ & { \rho _ { 0 } : = \frac { \mu _ { e } m _ { \mathrm { H } } } { 3 \pi ^ { 2 } \lambda _ { e } ^ { 3 } } , } \\ & { r _ { 0 } ^ { 2 } : = \frac { 1 } { f _ { c } ^ { 2 } } \frac { p _ { 0 } } { 4 \pi G \rho _ { 0 } ^ { 2 } } , } \\ & { m _ { 0 } : = 4 \pi f _ { c } ^ { 3 } \rho _ { 0 } r _ { 0 } ^ { 3 } , } \end{array}
$$

where the numerical factor $f _ { c }$ , which is defined precisely below, is introduced for convenience. A useful relation among these quantities is $G m _ { 0 } / r _ { 0 } = f _ { c } p _ { 0 } / \rho _ { 0 }$ . The length scale can be expressed as

$$
r _ { 0 } = \frac { \sqrt { 3 \pi } } { 2 f _ { c } \mu _ { e } } \frac { m _ { \mathrm { P l } } } { m _ { \mathrm { H } } } \lambda _ { e } = 3 . 8 8 4 6 6 \times 1 0 ^ { 6 } \frac { 1 } { f _ { c } } \bigg ( \frac { 2 } { \mu _ { e } } \bigg ) \mathrm { m } ,
$$

where $m _ { \mathrm { P l } } : = { \sqrt { \hbar c / G } }$ is the Planck mass, and the mass scale can be expressed as

$$
m _ { 0 } = \frac { \sqrt { 3 \pi } } { 2 \mu _ { e } ^ { 2 } } \frac { m _ { \mathrm { P l } } ^ { 3 } } { m _ { \mathrm { H } } ^ { 2 } } = 0 . 7 2 1 4 5 9 \left( \frac { 2 } { \mu _ { e } } \right) ^ { 2 } M _ { \odot } .
$$

The numerical value of the density scale is $\rho _ { 0 } = 1 . 9 4 7 8 7 \times 1 0 ^ { 9 } ( \mu _ { e } / 2 ) \mathrm { k g / m } ^ { 3 } .$

The scale-free, dimensionless variables are

$$
\xi : = r / r _ { 0 } , \qquad x ^ { 3 } : = \rho / \rho _ { 0 } , \qquad \phi ( x ) : = p / p _ { 0 } , \qquad \mu : = m / m _ { 0 } ,
$$

where $\phi ( x )$ is the function defined in Eq. (2.88). In terms of these variables, the equations of hydrostatic equilibrium, Eqs. (2.29), become

$$
\frac { d x } { d \xi } = - f _ { c } \frac { \sqrt { 1 + x ^ { 2 } } } { x } \frac { \mu } { \xi ^ { 2 } } , \qquad \frac { d \mu } { d \xi } = \frac { 1 } { f _ { c } ^ { 3 } } \xi ^ { 2 } x ^ { 3 } .
$$

The equations are integrated outward from $\xi = 0$ , with boundary conditions $x ( 0 ) = x _ { c }$ (related to the central density) and $\mu ( 0 ) = 0$ . Integration proceeds until $x = 0$ at the stellar boundary $\xi = \xi _ { 1 }$ .

In place of $x$ it is convenient to adopt a variable $\theta$ that is similar to the Lane–Emden variable introduced in Sec. 2.2.3. This is defined by

$$
1 + f _ { c } \theta : = \sqrt { 1 + x ^ { 2 } } ,
$$

where

$$
f _ { c } : = \sqrt { 1 + x _ { c } ^ { 2 } } - 1
$$

is the precise definition for the numerical factor introduced previously. The new density variable $\theta$ begins at 1 when $\xi = 0$ and $x = x _ { c }$ , and it drops to zero when $\xi = \xi _ { 1 }$ and $x = 0$ . With $\theta$ substituting for $x$ , the structure equations become

$$
\frac { d \theta } { d \xi } = - \frac { \mu } { \xi ^ { 2 } } , \qquad \frac { d \mu } { d \xi } = \xi ^ { 2 } \theta ^ { 3 / 2 } \big ( \theta + 2 / f _ { c } \big ) ^ { 3 / 2 } .
$$

As usual the equations can be combined into a single, second-order differential equation for $\theta$ :

$$
\frac { 1 } { \xi ^ { 2 } } \frac { d } { d \xi } \biggl ( \xi ^ { 2 } \frac { d \theta } { d \xi } \biggr ) = - \theta ^ { 3 / 2 } \bigl ( \theta + 2 / f _ { c } \bigr ) ^ { 3 / 2 } .
$$

The equations of white-dwarf structure bear a striking resemblance to the polytropic equations displayed in Eqs. (2.49) and (2.54). There is, however, a major difference: in the case of polytropes the structure equations were completely universal and independent of $\rho _ { c }$ ; here the equations feature a direct dependence upon $f _ { c }$ , which is tied to the central density. For a selected value of $f _ { c }$ , a solution to Eqs. (2.101) or (2.102) yields a unique white-dwarf model with a radius and mass given by

$$
R = \xi _ { 1 } r _ { 0 } , \qquad M = \mu _ { 1 } m _ { 0 } ;
$$

here $\mu _ { 1 } : = \mu ( \xi _ { 1 } )$ is the dimensionless mass function evaluated at the stellar boundary.

![](images/e5331743e8be50e3576af3d1861fb2844e4a5d66453b6e1d16fe8df4912d7685.jpg)

Mass of a white dwarf, in units of the solar mass, as a function of the central-density parameter $f _ { c }$ . Models with $f _ { c } \ll 1$ are non-relativistic, while models with $f _ { c } \gg 1$ are extremely relativistic. The mass increases with $f _ { c } ,$ and it asymptotes to the Chandrasekhar limit as $f _ { c } \to \infty$ .

# Properties of white dwarfs

In Figs. 2.3 and 2.4 we display the results of a numerical integration of Eqs. (2.101) for many selected values of $f _ { c }$ . Models with $f _ { c } \ll 1$ are non-relativistic, while models with $f _ { c } \gg 1$ are extremely relativistic. In all cases the mean molecular weight per electron is set equal to $\mu _ { e } = 2$ . The main features revealed by the plots are that the mass increases with $f _ { c }$ , but never beyond a limit of approximately $1 . 4 6 M _ { \odot }$ , and that the radius decreases with increasing mass.

In the non-relativistic regime $f _ { c } \ll 1$ , Eqs. (2.101) simplify to $d \theta / d \xi = - \mu / \xi ^ { 2 }$ and $d \mu / d \xi = ( 2 / f _ { c } ) ^ { 3 / 2 } \xi ^ { 2 } \theta ^ { 3 / 2 }$ . With the rescalings

$$
\begin{array} { r } { \xi = \left( { \textstyle { \frac { 1 } { 2 } } } f _ { c } \right) ^ { 3 / 4 } \bar { \xi } , \qquad \theta = \bar { \theta } , \qquad \mu = \left( { \textstyle { \frac { 1 } { 2 } } } f _ { c } \right) ^ { 3 / 4 } \bar { \mu } , } \end{array}
$$

the equations become $d \bar { \theta } / d \bar { \xi } = - \bar { \mu } / \bar { \xi } ^ { 2 }$ and $d \bar { \mu } / d \bar { \xi } = \bar { \xi } ^ { 2 } \bar { \theta } ^ { 3 / 2 }$ , and these are precisely the equations that govern the hydrostatic equilibrium of a polytrope with $\begin{array} { r } { n = \frac { 3 } { 2 } } \end{array}$ . The essential properties of the solution are displayed in Table 2.1, which reveals that $\bar { \xi } _ { 1 } = 3 . 6 5 3 7 5 3 7 4$ and $\bar { \mu } _ { 1 } = 2 . 7 1 4 0 5 5 1 2$ . These results, together with the approximation $\begin{array} { r } { f _ { c } = \frac { 1 } { 2 } x _ { c } ^ { 2 } = \frac { 1 } { 2 } ( \rho _ { c } / \rho _ { 0 } ) ^ { 2 / 3 } } \end{array}$ , imply that the mass and radius of a white dwarf are given by

$$
M = 0 . 4 9 6 0 2 8 \left( \frac { 2 } { \mu _ { e } } \right) ^ { 5 / 2 } \left( \frac { \rho _ { c } } { 1 0 ^ { 9 } \mathrm { k g / m } ^ { 3 } } \right) ^ { 1 / 2 } M _ { \odot }
$$

![](images/27dacc1c76e76107b639d76805fafe8286ce85b60282d905a25c5c47fbd4a31f.jpg)

Radius of a white dwarf, in units of $1 0 ^ { 6 } \mathsf { k m }$ , as a function of its mass, in units of the solar mass. The radius decreases with increasing mass, and goes to zero as the mass reaches the Chandrasekhar limit.

and

$$
{ R = 1 . 1 2 1 6 0 \times 1 0 ^ { 7 } \left( \frac { 2 } { \mu _ { e } } \right) ^ { 5 / 6 } \left( \frac { 1 0 ^ { 9 } \mathrm { { k g / m ^ { 3 } } } } { \rho _ { c } } \right) ^ { 1 / 6 } \mathrm { { m } } }
$$

in the non-relativistic regime. These results reveal that $M$ increases with the central density as $\rho _ { c } ^ { 1 / 2 }$ , while $R$ decreases as $\rho _ { c } ^ { - 1 / 6 }$ .

In the extreme relativistic regime $f _ { c } \gg 1$ , Eqs. (2.101) simplify to $d \theta / d \xi = - \mu / \xi ^ { 2 }$ and $d \mu / d \xi = \xi ^ { 2 } \theta ^ { 3 }$ ; in this limit the white dwarf is a polytrope with $n = 3$ . In this case Table 2.1 reveals that $\xi _ { 1 } = 6 . 8 9 6 8 4 8 6 2$ and $\mu _ { 1 } = 2 . 0 1 8 2 3 5 9 5$ . Together with the approximation $f _ { c } = x _ { c } = ( \rho _ { c } / \rho ) ^ { 1 / 3 }$ , these results imply that the mass and radius of a white dwarf are given by

$$
M _ { \mathrm { C h a n d r a } } = 1 . 4 5 6 0 7 \left( { \frac { 2 } { \mu _ { e } } } \right) ^ { 2 } M _ { \odot }
$$

and

$$
{ R = 3 . 3 4 5 9 8 \times 1 0 ^ { 7 } \left( \frac { 2 } { \mu _ { e } } \right) ^ { 2 / 3 } \left( \frac { 1 0 ^ { 9 } \mathrm { { k g / m ^ { 3 } } } } { \rho _ { c } } \right) ^ { 1 / 3 } \mathrm { { m } } }
$$

in the extreme relativistic regime. These expressions reveal that $R$ decreases as $\rho _ { c } ^ { - 1 / 3 }$ with increasing central density, but that the mass is independent of the central density. The numerical results show that Eq. (2.107) is the maximum mass realized on the sequence of white-dwarf models; it is the famous Chandrasekhar limit, which was first discovered in 1930.

For a typical white dwarf of mass $M = 0 . 6 M _ { \odot }$ , the numerical results imply that the central-density parameter is $f _ { c } = 0 . 5 4 6$ , revealing that the conditions are only mildly relativistic. The central density is $\rho _ { c } = 3 . 1 9 \times 1 0 ^ { 9 } ~ \mathrm { k g / m } ^ { 3 }$ , and the radius of such a white dwarf is $R = 8 . 8 5 \times 1 0 ^ { 6 }$ km. From these values we can infer that the mean density $\bar { \rho } = 3 M / ( 4 \pi R ^ { 3 } )$ is 0.129 times the central density.

# Chandrasekhar mass: balance between Fermi and gravitational energies

We have found that in the extreme relativistic regime, the white-dwarf mass is equal to a universal factor multiplying the mass scale $m _ { 0 }$ , which, according to Eq. (2.96), is itself proportional to $m _ { \mathrm { P l } } ^ { 3 } / m _ { \mathrm { H } } ^ { 2 }$ . Thus, $M _ { \mathrm { C h a n d r a } } \propto m _ { \mathrm { P l } } ^ { 3 } / m _ { \mathrm { H } } ^ { 2 }$ , and this dependence can be understood on the basis of a simple argument that originates with Landau. The argument works for any system of degenerate fermions, and we can apply it to neutron stars as well as white dwarfs.

In the extreme relativistic regime, the Fermi energy of a fermion is given by $p _ { \mathrm { F } } c$ , which, by the uncertainty principle, is comparable to $\hbar c / \Delta x \sim \hbar c n ^ { 1 / 3 } \sim \hbar c N ^ { 1 / 3 } / R$ , where $N$ is the total number of fermions in the body. On the other hand, the gravitational energy per fermion is approximately $- G M m _ { \mathrm { H } } / R$ , with $M \sim N m _ { \mathrm { H } }$ . (When the argument is applied to neutrons, the gravitational energy is dominated by the neutrons, and $m _ { \mathrm { H } }$ is approximately the neutron’s mass. When the argument is applied to electrons, the gravitational energy is dominated by the ions, and a factor of $\mu _ { e }$ should be inserted to relate the number of fermions to the mass. In both cases the relevant mass is the atomic mass unit $m _ { \mathrm { H } }$ .) Collecting results, we find that the total energy of the system may be expressed as

$$
E \sim \frac { \hbar c N ^ { 4 / 3 } } { R } - \frac { G N ^ { 2 } m _ { \mathrm { H } } ^ { 2 } } { R } .
$$

The key point is that each term is inversely proportional to $R$ . Now, the stability of the configuration is dictated by the overall sign of the total energy. When $E$ is positive, a decrease in $R$ produces an increase in energy, and this behavior indicates stability with respect to gravitational collapse. When $E$ is negative, a decrease in $R$ produces a decrease in energy, and this points to an instability.

Stability under gravitational collapse therefore places an upper limit on the number of fermions that can be relativistically degenerate. This limit is given by $\hbar c N ^ { 4 / 3 } > G N ^ { 2 } m _ { \mathrm { H } } ^ { 2 }$ , or $N ^ { 2 / 3 } < ( m _ { \mathrm { P l } } / m _ { \mathrm { H } } ) ^ { 2 }$ , recalling that $m _ { \mathrm { P l } } : = { \sqrt { \hbar c / G } }$ is the Planck mass. We then find that the body’s maximum mass is given by

$$
M _ { \mathrm { m a x } } \sim N _ { \mathrm { m a x } } m _ { \mathrm { H } } \sim \frac { m _ { \mathrm { P l } } ^ { 3 } } { m _ { \mathrm { H } } ^ { 2 } } ,
$$

which is the same scaling as $m _ { 0 }$ , as defined by Eq. (2.96).

The value of the maximum mass does not depend on the identity of the degenerate fermion; apart from numerical factors, the result should be the same for electrons and for neutrons. So, if neutron stars were subjected to Newtonian gravity, and if their equation of state were indeed that of an ideal gas of degenerate fermions, then they would have a maximum mass also given by Eq. (2.107), but with $\mu _ { e }$ replaced by $\mu _ { n }$ , whose value depends on the ratio of free neutrons to neutrons still bound in nuclei. The catch, of course, is that neutron stars are not subjected to Newtonian gravity: because $\varepsilon \sim G M / ( c ^ { 2 } R ) \sim 0 . 2$ for neutron stars, the gravitational fields are too strong for a Newtonian treatment, and they must be described by general relativity. The other catch is that neutron stars are not actually made up of an ideal gas of degenerate neutrons: the densities are so high (of the order of $1 0 ^ { 1 7 } \mathrm { k g / m } ^ { 3 }$ ) that the neutrons are subjected to short-range strong interactions, beta decay and inverse beta decay, and the possible conversion to exotic particles such as pion condensates and strange hadrons. The neutrons are not free, and their interactions at such high densities are poorly understood; as a consequence, the maximum mass of neutron stars is somewhat uncertain, lying between about 2 and 3 solar masses.

# 2.3 Rotating self-gravitating bodies

The equilibrium structures examined in Sec. 2.2 were all spherically symmetric and nonrotating. Rotation, however, is everywhere: planets rotate, the Sun rotates, stars and galaxies rotate. Neutron stars observed as pulsars rotate; one of the fastest, PSR J1748-2446ad, spins at a rate of 716 times per second. Black holes are expected to have substantial rotation. Because astronomical objects are formed by gravitational collapse, the slightest amount of angular momentum in the progenitor material results in a rotational angular velocity that is magnified by the collapse, limited only by the shedding of material when the centrifugal forces exceed the gravitational forces.

Our previous models of non-rotating, spherically-symmetric, self-gravitating bodies allowed us to explore many basic properties of stars and planets, but the idealization is not realistic when applied to real astronomical bodies. We must consider rotation, and the related complication that rotating bodies are not spherical. And when we do so, the number of basic questions increases greatly, and their answers depend on the detailed nature of the body.

Do bodies rotate rigidly? That is, do they rotate with an angular velocity that is independent of position within the body? It turns out that this is impossible under some conditions, and the body must then undergo differential rotation, or must develop meridional currents, fluid flows in a direction parallel to the rotation axis. The Sun rotates differentially; the angular velocity in the polar regions is about $2 / 3$ that at the equator, and the angular velocity at the center could be as much as 10 times higher than that at the surface.

What is the shape of a rotating fluid body? In a general situation the shape cannot be fixed a priori, and must be determined along with the rest of the body’s structure. To keep the problem tractable, however, it is helpful to adopt a specific class of shapes for the body, and then determine whether these shapes are compatible with the equations of stellar structure. For example, the simplest shape one might expect for a rotating body is one for which one or more of the three cross sections has the form of an ellipse. If one of the cross sections is circular while the other two are elliptical, the shape is known as a spheroid;

if all three cross sections are elliptical, the shape is an ellipsoid. We shall see below that in the special case of a rigidly rotating body of uniform density, the equations of stellar structure are compatible with a spheroidal or ellipsoidal shape, provided that the angular velocity does not exceed a certain limit; beyond this maximum value, differential rotation is required to support the body. In the limit of slow rotation, for general density distributions and equations of state, we show in Sec. 2.4 that the shape is spheroidal to the first order of approximation. In general, however, the shape of a rotating body is neither a spheroid nor an ellipsoid, and it must be determined by solving the equations of stellar structure with no built-in assumptions – a most difficult task.

Are rotating bodies axially symmetric? Not necessarily: a rotating body can be in hydrostatic equilibrium and assume a shape that is not symmetric about the axis of rotation. In fact, we shall see that one can construct an equilibrium model of a rotating body that has two equally valid solutions, one an axisymmetric spheroid, and the other a non-axisymmetric ellipsoid; and one can show that some of the spheroids are subjected to instabilities that convert them into ellipsoids.

In this section we take advantage of simple models to address several of these questions.

# 2.3.1 Foundations of the theory of rotating bodies

# Rotating frame

We again consider an isolated body, governed by Eq. (2.4), in which we continue to ignore the external terms. But now we assume that $\bar { v }$ , the velocity of a fluid element relative to the body’s center-of-mass, can be decomposed as

$$
\pmb { \bar { v } } = \pmb { \omega } \times \pmb { \bar { x } } + \pmb { u } .
$$

The first term is a rotational velocity, which refers to a local frame of reference that rotates with an instantaneous angular velocity $\omega ( t , x )$ with respect to the center-of-mass frame; the angular velocity may in general depend on time and spatial position, but we assume that its direction is along a fixed axis described by the unit vector $_ e$ . The second term is the intrinsic velocity of the fluid element in the rotating frame of reference.

The acceleration of the fluid element is then given by

$$
\begin{array} { l } { \displaystyle \frac { d \bar { \pmb { v } } } { d t } = \pmb { \omega } \times \bar { \pmb { v } } + \frac { d \pmb { \omega } } { d t } \times \bar { \pmb { x } } + \frac { d \pmb { u } } { d t } } \\ { \displaystyle = \pmb { \omega } \times ( \pmb { \omega } \times \bar { \pmb { x } } ) + \pmb { \omega } \times \pmb { u } + \frac { d \pmb { \omega } } { d t } \times \bar { \pmb { x } } + \frac { d \pmb { u } } { d t } } \\ { \displaystyle = - \omega ^ { 2 } \pmb { \varrho } + 2 \pmb { \omega } \times \pmb { u } + \frac { d \pmb { \omega } } { d t } \times \bar { \pmb { x } } + \pmb { a } , } \end{array}
$$

where we have used the fact that $d { \pmb u } / d t = { \pmb \omega } \times { \pmb u } + { \pmb a }$ , with $\pmb { a }$ denoting the acceleration in the rotating frame, and where

$$
\varrho : = \bar { x } - e ( e \cdot \bar { x } )
$$

is the projection of the position vector to the plane perpendicular to the rotation axis. If we align the $\bar { z }$ -direction with $_ e$ , then $\varrho = [ \bar { x } , \bar { y } , 0 ]$ and $\varrho : = | \varrho | = ( \bar { x } ^ { 2 } + \bar { y } ^ { 2 } ) ^ { 1 / 2 }$ is the usual cylindrical radial coordinate of a $( \varrho , \bar { z } , \bar { \phi } )$ coordinate system. The first term in Eq. (2.112) is the centrifugal acceleration, the second is the Coriolis acceleration, present if the fluid has intrinsic motion in the rotating frame; the third term is a rotational acceleration effect, and the final term is the intrinsic acceleration of the element in the rotating frame.

# Steady rotation; equilibrium configuration

We now introduce some simplifying assumptions. First, the rotation is taken to be steady, in the sense that $\omega$ is independent of time. Second, the fluid motion is taken to be purely rotational, in the sense that ${ \pmb u } = 0$ . Third, the system is taken to be stationary when viewed by a non-rotating observer, so that $\partial \rho / \partial t = 0$ . And fourth, the density is also taken to be constant when viewed by an observer following the fluid, so that $d \rho / d t = 0$ .

The last two assumptions, combined with the equation of continuity, $\partial \rho / \partial t + \nabla \cdot ( \rho \bar { \pmb { v } } ) =$ 0 or $d \rho / d t + \rho \nabla \cdot \bar { \pmb { v } } = 0$ , imply that

$$
\bar { \pmb { \nu } } \cdot \nabla \rho = 0 \quad \mathrm { a n d } \quad \nabla \cdot \bar { \pmb { \nu } } = 0 .
$$

The second assumption implies that $\pmb { \bar { v } } = \pmb { \omega } \times \pmb { \bar { x } }$ , and it follows that

$$
\begin{array} { r l } & { 0 = ( \omega \times \bar { x } ) \cdot \nabla \rho } \\ & { \quad = \omega \cdot ( \bar { x } \times \nabla ) \rho } \\ & { \quad = \omega \frac { \partial \rho } { \partial \bar { \phi } } \cdot } \end{array}
$$

This is the statement that the mass density of a rotating body must be axially symmetric, independent of the azimuthal angle $\bar { \phi }$ . We also have

$$
{ \begin{array} { r l } & { 0 = \nabla \cdot { \bar { \boldsymbol { v } } } } \\ & { \quad = \nabla \cdot \left( \omega \times { \bar { x } } \right) } \\ & { \quad = \left( { \bar { \boldsymbol { x } } } \times \nabla \right) \cdot \omega } \\ & { \quad = { \cfrac { \partial \omega } { \partial { \bar { \phi } } } } , } \end{array} }
$$

the statement that the angular velocity also must be independent of $\bar { \phi }$ .

With these assumptions, Euler’s equation, Eq. (2.4), reduces to

$$
\frac { 1 } { \rho } \nabla p = \nabla U + \omega ( \bar { \mathbf { x } } ) ^ { 2 } \pmb { \varrho } .
$$

This equation, together with Poisson’s equation for the gravitational potential $U$ , governs the equilibrium structure of our stationary rotating body.

# Stratification

As we saw in Sec. 2.2, a feature of spherical bodies is that the surfaces of constant $\rho$ , constant $p$ , and constant $U$ all coincide, because these surfaces are all spherical. In the case of a rotating body, is it still true that these level surfaces coincide? We wish to show that under some conditions on the angular velocity, surfaces of constant $\rho$ and constant $p$ continue to coincide, and there also exists a generalized potential $\Phi$ with coincident level surfaces. We shall find, however, that the surfaces of constant $U$ do not in general coincide with the other level surfaces.

To explore this, we take the curl of Eq. (2.117) and obtain

$$
- \frac { 1 } { \rho ^ { 2 } } \nabla \rho \times \nabla p = 2 \omega \nabla \omega \times \pmb { \varrho } .
$$

Now, surfaces of constant $\rho$ and constant $p$ will coincide when $\nabla \rho \times \nabla p = \mathbf { 0 }$ , which implies (assuming that $\omega \neq 0$ ) that $\nabla \omega \times \varrho = \mathbf { 0 }$ . Since we already know that $\partial \omega / \partial \bar { \phi } = 0$ , this implies that $\partial \omega / \partial \bar { z } = 0$ and we conclude that $\omega = \omega ( \varrho )$ . We have found that when the body rotates uniformly ( $\omega =$ constant), or when its angular velocity depends on $\varrho$ only, then the surfaces of constant $\rho$ and constant $p$ coincide.

When $\omega$ is either constant or a function of $\varrho$ only, we can further show that there exists a centrifugal potential $\Phi _ { \mathrm { { C } } }$ associated with the centrifugal acceleration term in Eq. (2.117). This follows because the centrifugal acceleration has a vanishing curl,

$$
\nabla \times ( \omega ^ { 2 } \pmb { \varrho } ) = 2 \omega \nabla \omega \times \pmb { \varrho } = \pmb { 0 } ,
$$

and is therefore given by the gradient of a scalar function. The potential is given by

$$
\Phi _ { \mathrm { C } } ( \varrho ) : = \int ^ { \varrho } \omega ( \varrho ^ { \prime } ) ^ { 2 } \varrho ^ { \prime } d \varrho ^ { \prime } ,
$$

and a generalized potential

$$
\Phi : = U + \Phi _ { \mathrm { C } }
$$

can be introduced to simplify the form of the structure equations, which become

$$
\nabla p = \rho \nabla \Phi .
$$

Taking the curl of this equation, we conclude finally that with the stated assumptions, the surfaces of constant $p$ , constant $\rho$ , and constant $\Phi$ all coincide. Notice that this statement does not imply that surfaces of constant $U$ and constant $\Phi _ { \mathrm { { C } } }$ coincide with each other, nor with the level surfaces of the total potential $\Phi$ .

# Global properties

Back in Sec. 1.4.3 we established the virial theorem of stationary fluid configurations,

$$
2 \mathcal { T } + \Omega + 3 P = 0 ,
$$

where $\tau$ is the total kinetic energy, $\Omega$ the gravitational potential energy, and $P$ the integrated pressure; these quantities are defined by Eqs. (1.64), (1.65), and (1.85), and the virial theorem was first stated in Eq. (1.90). Since $P \ge 0$ and $\Omega$ is negative, we can immediately derive a bound on the ratio of kinetic to potential energy for a rotating body:

$$
\tau : = \frac { \mathcal T } { | \Omega | } \leq \frac 1 2 .
$$

For a rotating body with $\bar { \pmb { v } } = \pmb { \omega } \times \bar { \pmb { x } }$ , the kinetic energy is given by

$$
\begin{array} { l } { { \displaystyle { \mathcal T } = \frac { 1 } { 2 } \int \rho \bar { v } ^ { 2 } d ^ { 3 } \bar { x } } } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \int \rho \omega ^ { 2 } \big [ \bar { r } ^ { 2 } - ( e \cdot \bar { x } ) ^ { 2 } \big ] d ^ { 3 } \bar { x } } } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \int \rho \omega ^ { 2 } \varrho ^ { 2 } d ^ { 3 } \bar { x } . } } \end{array}
$$

The angular momentum is given by

$$
\begin{array} { l } { J = \displaystyle \int \rho \bar { \boldsymbol { x } } \times ( \boldsymbol { \omega } \times \bar { \boldsymbol { x } } ) d ^ { 3 } \bar { \boldsymbol { x } } } \\ { \displaystyle = \int \rho \omega \big [ e \bar { r } ^ { 2 } - \bar { x } ( e \cdot \bar { x } ) \big ] d ^ { 3 } \bar { x } } \\ { \displaystyle = e \int \rho \omega \varrho ^ { 2 } d ^ { 3 } \bar { x } , } \end{array}
$$

where we use the axisymmetry of $\rho$ and $\omega$ to obtain the final result. When the rotation is uniform, so that $\omega =$ constant, these equations simplify to

$$
\boldsymbol { \mathcal { T } } = \frac { 1 } { 2 } \omega ^ { 2 } \boldsymbol { I } , \qquad \boldsymbol { J } = \omega \boldsymbol { I } \boldsymbol { e } ,
$$

where

$$
I : = \int \rho \varrho ^ { 2 } d ^ { 3 } \bar { x }
$$

is the body’s moment of inertia about the axis of rotation.

We continue to assume that the rotation is uniform. In this case the centrifugal potential simplifies to

$$
\Phi _ { \mathrm { C } } = { \frac { 1 } { 2 } } \omega ^ { 2 } \varrho ^ { 2 } ,
$$

and from this we find that $\nabla ^ { 2 } \Phi _ { \mathrm { C } } = 2 \omega ^ { 2 }$ . For the total potential of Eq. (2.121) we then get $\nabla ^ { 2 } \Phi = - 4 \pi G \rho + 2 \omega ^ { 2 }$ . Integrating this equation over the body and using Gauss’s theorem, we find that

$$
\oint { \nabla } \Phi \cdot { \pmb { n } } d S = - 4 \pi G M + 2 \omega ^ { 2 } V ,
$$

where $M$ and $V$ are the mass and volume of the body, respectively, and $\pmb { n }$ is an outwardpointing unit vector on the body’s surface. But Eq. (2.122) implies that $\nabla \Phi \cdot \pmb { n } = \rho ^ { - 1 } \nabla p .$ $\pmb { n }$ , which must be negative everywhere on the surface, because $p$ vanishes there and is positive everywhere inside. As a result, we obtain the Poincare inequality ´

$$
\omega ^ { 2 } < 2 \pi G \bar { \rho } ,
$$

where ${ \bar { \rho } } = M / V$ is the body’s mean density. Recall that the angular velocity required for a particle to be on a circular orbit at the body’s equator is given approximately by $( d \bar { \phi } / d t ) ^ { 2 } \sim G M / r _ { \mathrm { e q } } ^ { 3 } \sim G \bar { \rho }$ , with $r _ { \mathrm { e q } }$ denoting the equatorial radius. The condition $\omega ^ { 2 } \sim G \bar { \rho }$ marks the mass-shedding limit, because a body rotating faster than this will shed matter from its equatorial regions. The inequality of Eq. (2.131) is therefore the statement that a rotating body in equilibrium cannot exceed the mass-shedding limit. The Poincare´ inequality provides a rather generous upper bound on a body’s angular velocity, and we shall find that actual bounds are much tighter; the numerical coefficient on the right-hand side of Eq. (2.131) can be reduced by a factor approximately equal to 4.

# Transformation to the rotating frame

We have developed the structure equations of a rotating body by referring to the rotating frame to measure the velocity $\pmb { u }$ and acceleration $\pmb { a }$ of a fluid element. We have, however, continued to measure the position $\bar { x }$ relative to the non-rotating frame, and to conclude this section we wish to complete the transformation to the rotating frame. We shall now relax most of the assumptions introduced previously, except for the rather restrictive one that $\omega$ is taken to be a constant (independent of time and spatial position).

The original frame $\pmb { \bar { x } } = ( \bar { x } , \bar { y } , \bar { z } )$ is attached to the body’s center-of-mass, and is nonrotating. The new frame $\pmb { x } = ( x , y , z )$ that we introduce here is also attached to the centerof-mass, but is rotating rigidly with an angular velocity $\omega$ . We align the $\bar { z }$ -direction with the rotation axis, and the transformation between the two frames is given by

$$
\bar { x } = x \cos ( \omega t ) - y \sin ( \omega t ) , \qquad \bar { y } = x \sin ( \omega t ) + y \cos ( \omega t ) , \qquad \bar { z } = z .
$$

The inverse transformation is obtained simply by reversing the sign of $\omega$ . For our developments it is useful to employ an index language in which $\bar { x }$ is represented by the coordinates $x ^ { \bar { a } }$ while $\boldsymbol { x }$ is represented by $x ^ { j }$ . The transformation can then be expressed as

$$
x ^ { \bar { a } } = \Lambda _ { ~ j } ^ { \bar { a } } ( t ) x ^ { j } ,
$$

in which $\Lambda _ { ~ j } ^ { \bar { a } } ( t )$ are the elements of the rotation matrix. The inverse transformation is

$$
x ^ { j } = \Lambda _ { \bar { a } } ^ { j } ( t ) x ^ { \bar { a } } ,
$$

with $\Lambda _ { \bar { a } } ^ { j } ( t )$ denoting the elements of the inverse matrix. The identities

$$
\Lambda _ { \ j } ^ { \bar { a } } \Lambda _ { \ \bar { b } } ^ { \ j } = \delta _ { \ \bar { b } } ^ { \bar { a } } , \qquad \Lambda _ { \ \bar { a } } ^ { j } \Lambda _ { \ k } ^ { \bar { a } } = \delta _ { \ k } ^ { j }
$$

express the fact that a transformation followed by its inverse is an identity transformation.

Suppose that we follow the motion of a fluid element. In the non-rotating frame the motion is described by $x ^ { \bar { a } } ( t )$ , while it is described by $x ^ { j } ( t )$ in the rotating frame. The velocity of the fluid element is $v ^ { \bar { a } } = d x ^ { \bar { a } } / d t$ in the non-rotating frame, and $u ^ { j } = d x ^ { j } / d t$ in the rotating frame. The relation is provided by differentiating Eq. (2.133) with respect to time, and we obtain

$$
v ^ { \bar { a } } = \Lambda _ { ~ j } ^ { \bar { a } } \big ( u ^ { j } + \omega _ { ~ k } ^ { j } x ^ { k } \big ) ,
$$

where

$$
\omega _ { \mathrm { \tiny ~ \it k } } ^ { j } : = \Lambda _ { \bar { a } } ^ { j } \dot { \Lambda } _ { \mathrm { \tiny ~ \it k } } ^ { \bar { a } }
$$

is the angular-velocity tensor (the overdot on the right-hand side indicates differentiation with respect to time). A simple calculation reveals that

$$
\omega _ { j k } = - \epsilon _ { j k n } \omega ^ { n } ,
$$

where $\epsilon _ { j k n }$ is the permutation symbol and $\omega ^ { n } = \omega e ^ { n }$ are the components of the angularvelocity vector. Because $\omega _ { \boldsymbol { k } } ^ { j } \boldsymbol { x } ^ { k } = ( \boldsymbol { \omega } \times \boldsymbol { x } ) ^ { j }$ , we see that Eq. (2.136) is essentially the same statement as Eq. (2.111). Differentiation of Eq. (2.136) then produces

$$
\frac { d v ^ { \bar { a } } } { d t } = \Lambda ^ { \bar { a } } { } _ { j } \big ( a ^ { j } + 2 \omega ^ { j } { } _ { k } u ^ { k } - C _ { \ k } ^ { j } x ^ { k } \big ) ,
$$

in which $a ^ { j } : = d u ^ { j } / d t$ is the acceleration of the fluid element in the rotating frame, and

$$
C _ { j k } : = - \omega _ { j n } \omega _ { k } ^ { n } = \omega ^ { 2 } \big ( \delta _ { j k } - e _ { j } e _ { k } \big )
$$

is the centrifugal tensor. The second term on the right-hand side of Eq. (2.139) is recognized as the Coriolis acceleration, while the third term is the centrifugal acceleration. Equation (2.139) is essentially the same statement as Eq. (2.112) when the angular velocity is restricted to be a constant.

We now wish to formulate the equations of fluid dynamics in the rotating frame. A subtle issue concerns the meaning of partial derivatives, because differentiating with respect to $t$ while keeping $\bar { x }$ constant (for a non-rotating observer) is very different from performing the operation while keeping $_ x$ constant (for a rotating observer). The relation can be uncovered by expressing a function $f$ of the variables $( t , x ^ { \bar { a } } )$ as $f ( t , { \Lambda ^ { \bar { a } } } _ { j } x ^ { j } )$ and performing the differentiations. We obtain

$$
\begin{array} { l } { { \displaystyle \left( \frac { \partial f } { \partial t } \right) _ { x ^ { \bar { a } } } = \left( \frac { \partial f } { \partial t } \right) _ { x ^ { j } } - \left( \frac { \partial f } { \partial x ^ { j } } \right) \omega _ { \ k } ^ { j } x ^ { k } \mathrm { , } } } \\ { { \displaystyle \left( \frac { \partial f } { \partial x ^ { \bar { a } } } \right) = \left( \frac { \partial f } { \partial x ^ { j } } \right) \Lambda _ { \ \bar { a } } ^ { j } \mathrm { , } } } \end{array}
$$

in which the subscript on the time derivative indicates which variable is kept fixed.

With these rules it is easy to show that the continuity equation keeps its usual form in the rotating frame,

$$
\left( \frac { \partial \rho } { \partial t } \right) _ { x ^ { j } } + \frac { \partial } { \partial x ^ { j } } \big ( \rho u ^ { j } \big ) = 0 ,
$$

that Euler’s equation becomes

$$
\frac { d u ^ { j } } { d t } = \partial _ { j } U - \frac { 1 } { \rho } \partial _ { j } p - 2 \omega _ { \ k } ^ { j } u ^ { k } + C _ { \ k } ^ { j } x ^ { k } ,
$$

and that Poisson’s equation also keeps its usual form,

$$
\nabla ^ { 2 } U = - 4 \pi G \rho ,
$$

in which the Laplacian operator refers to the rotating frame $x ^ { j }$ .

When the configuration is stationary in the rotating frame $( u ^ { j } = 0$ ), Euler’s equation reduces to

$$
\frac { 1 } { \rho } \partial _ { j } p = \partial _ { j } \Phi ,
$$

where $\Phi = U + \Phi _ { \mathrm { C } }$ is the total potential introduced previously, with

$$
\Phi _ { \mathrm { { C } } } = { \frac { 1 } { 2 } } C _ { j k } x ^ { j } x ^ { k } = { \frac { 1 } { 2 } } \omega ^ { 2 } \big ( x ^ { 2 } + y ^ { 2 } \big )
$$

the centrifugal potential of Eq. (2.129), now written in terms of the rotating-frame coordinates $x ^ { j }$ .

# 2.3.2 Rotating bodies of uniform density

Back in Sec. 2.2.2 we found that the mathematics of spherical bodies of uniform density were particularly simple, though physically unrealistic. In a similar way, rigidly rotating bodies of uniform density admit a relatively simple treatment in Newtonian theory, and the results can be expressed in terms of simple integrals that, unfortunately, cannot in general be evaluated in closed form. Even though the assumption of uniform density is no more realistic here than it was in the case of a spherical body, the resulting models capture many important properties of realistic rotating bodies. Because the mathematics are relatively simple, these models attracted the attention of many of the great mathematical physicists of the 18th and 19th centuries, and many of the resulting models bear their names: the spheroids of Maclaurin, the ellipsoids of Jacobi, Dirichlet, Dedekind, and Riemann. Although incomplete, this body of work was not much pursued in the 20th century; as Chandrasekhar famously expressed it, “the subject quietly went into a coma.” It was, however, vigorously revived by Lebovitz and Chandrasekhar in the nineteen sixties, and the entire subject came to a beautiful close in Chandra’s monumental Ellipsoidal figures of equilibrium.

In this section we assume that the figure of a rigidly rotating body of uniform density is an ellipsoid, and seek to determine the conditions that ensure consistency with the equations of hydrostatic equilibrium.

# Gravitational potential inside an ellipsoid

The hardest part of the task ahead is to calculate the gravitational potential inside a body of uniform density, under the assumption that its surface is described by the equation

$$
\frac { x ^ { 2 } } { a _ { 1 } ^ { 2 } } + \frac { y ^ { 2 } } { a _ { 2 } ^ { 2 } } + \frac { z ^ { 2 } } { a _ { 3 } ^ { 2 } } = 1 ,
$$

in which the constants $a _ { 1 } , a _ { 2 }$ , and $a _ { 3 }$ are the ellipsoid’s semi-axes in the three principal directions. The description is given in the body’s rotating frame, which is assumed to rotate rigidly about the $z$ -direction with an angular velocity $\omega$ . When $a _ { 1 } = a _ { 2 }$ the body is axially symmetric about the $z$ -direction, and the surface is a spheroid.

We state the answer before getting on with the work:

$$
U = \pi G \rho \big ( A _ { 0 } - A _ { 1 } x ^ { 2 } - A _ { 2 } y ^ { 2 } - A _ { 3 } z ^ { 2 } \big ) ,
$$

where

$$
{ \cal A } _ { 0 } : = a _ { 1 } a _ { 2 } a _ { 3 } \int _ { 0 } ^ { \infty } \frac { d u } { \Delta } ,
$$

and

$$
A _ { i } : = a _ { 1 } a _ { 2 } a _ { 3 } \int _ { 0 } ^ { \infty } \frac { d u } { \Delta \left( a _ { i } ^ { 2 } + u \right) } ,
$$

with

$$
\Delta ^ { 2 } : = \big ( a _ { 1 } ^ { 2 } + u \big ) \big ( a _ { 2 } ^ { 2 } + u \big ) \big ( a _ { 3 } ^ { 2 } + u \big ) .
$$

The integrals must be evaluated numerically when $a _ { 1 } \neq a _ { 2 }$ , but they admit closed-form expressions when the body is axisymmetric; these will be revealed below. The quadratic form of Eq. (2.148) is remarkably simple, and it is easy to show that $U$ satisfies Poisson’s equation (for a constant density) for any set of $A _ { i } \mathbf { s }$ that satisfies the constraint $A _ { 1 } + A _ { 2 } +$ $A _ { 3 } = 2$ ; as we shall see, the set of Eq. (2.150) does indeed possess this property.

To calculate $U$ we follow the general strategy devised by Moulton in his classic text on celestial mechanics. We let $\pmb { x } = ( x , y , z )$ be the point at which $U$ is evaluated (which is interior to the ellipsoid), and we let $\pmb { x } ^ { \prime } = ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ be a source point within the ellipsoid. To locate $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ we employ spherical coordinates $( \tilde { r } , \tilde { \theta } , \tilde { \phi } )$ centered upon $\boldsymbol { x }$ , so that

$$
x ^ { \prime } = x + \tilde { r } \sin \tilde { \theta } \cos \tilde { \phi } , \qquad y ^ { \prime } = y + \tilde { r } \sin \tilde { \theta } \sin \tilde { \phi } , \qquad z ^ { \prime } = z + \tilde { r } \cos \tilde { \theta } .
$$

The distance between the two points is evidently $\tilde { r }$ . The source point is on the surface when $x ^ { \prime } = x _ { \mathrm { s } } , y ^ { \prime } = y _ { \mathrm { s } } , z ^ { \prime } = z _ { \mathrm { s } }$ , with $( x _ { \mathrm { s } } , y _ { \mathrm { s } } , z _ { \mathrm { s } } )$ a solution to Eq. (2.147). In terms of the spherical coordinates, the surface is described by the equation $\tilde { r } = r _ { \mathrm { s } } ( \tilde { \theta } , \tilde { \phi } )$ , and the function $r _ { \mathrm { s } }$ is determined by inserting Eqs. (2.152) within Eq. (2.147). This gives rise to the quadratic equation

$$
\alpha r _ { \mathrm { s } } ^ { 2 } + 2 \beta r _ { \mathrm { s } } + \gamma = 0 ,
$$

with

$$
\begin{array} { r l } & { \alpha : = \frac { \sin ^ { 2 } \tilde { \theta } \cos ^ { 2 } \tilde { \phi } } { a _ { 1 } ^ { 2 } } + \frac { \sin ^ { 2 } \tilde { \theta } \sin ^ { 2 } \tilde { \phi } } { a _ { 2 } ^ { 2 } } + \frac { \cos ^ { 2 } \tilde { \theta } } { a _ { 3 } ^ { 2 } } , } \\ & { \beta : = \frac { x \sin \tilde { \theta } \cos \tilde { \phi } } { a _ { 1 } ^ { 2 } } + \frac { y \sin \tilde { \theta } \sin \tilde { \phi } } { a _ { 2 } ^ { 2 } } + \frac { z \cos \tilde { \theta } } { a _ { 3 } ^ { 2 } } , } \\ & { \gamma : = \frac { x ^ { 2 } } { a _ { 1 } ^ { 2 } } + \frac { y ^ { 2 } } { a _ { 2 } ^ { 2 } } + \frac { z ^ { 2 } } { a _ { 3 } ^ { 2 } } - 1 . } \end{array}
$$

We see that $\alpha > 0$ , and since $\boldsymbol { x }$ is an interior point, we have that $\gamma < 0$ ; the sign of $\beta$ depends on $\tilde { \theta }$ and $\tilde { \phi }$ . We note that while $\alpha$ and $\gamma$ are preserved under a reflection $( \tilde { \theta } , \tilde { \phi } )  ( \pi - \tilde { \theta } , \tilde { \phi } + \pi )$ across the origin at $x , \beta$ changes sign under the reflection. The

appropriate solution to the quadratic equation is

$$
r _ { \mathrm { s } } = { \frac { - \beta + { \sqrt { \beta ^ { 2 } - \alpha \gamma } } } { \alpha } } ;
$$

the other solution would produce a negative radius.

The gravitational potential is given by

$$
U ( { \pmb x } ) = G \int \frac { \rho ( { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } d ^ { 3 } { \pmb x } ^ { \prime } = G \rho \int \tilde { r } d \tilde { r } d \tilde { \Omega } ,
$$

where we make use of the fact that $d ^ { 3 } x ^ { \prime } = \tilde { r } ^ { 2 } d \tilde { r } d \tilde { \Omega }$ , with $d \tilde { \Omega } : = \sin \tilde { \theta } d \tilde { \theta } d \tilde { \phi }$ . Integration with respect to the radial variable yields

$$
U = \frac { 1 } { 2 } G \rho \int r _ { \mathrm { { s } } } ^ { 2 } ( \tilde { \theta } , \tilde { \phi } ) d \tilde { \Omega } ,
$$

and the remaining integration is over the usual range of the angular coordinates. Insertion of Eq. (2.155) gives

$$
U = \frac { 1 } { 2 } G \rho \Bigg [ \int \frac { 2 \beta ^ { 2 } - \alpha \gamma } { \alpha ^ { 2 } } d \tilde { \Omega } - 2 \int \frac { \beta \sqrt { \beta ^ { 2 } - \alpha \gamma } } { \alpha ^ { 2 } } d \tilde { \Omega } \Bigg ] ,
$$

and with the stated properties of $\alpha , \beta$ , and $\gamma$ under a reflection across $\boldsymbol { x }$ , we see that the second integral vanishes because contributions from one hemisphere cancel out the contributions from the opposite hemisphere. The potential simplifies to

$$
U = \frac { 1 } { 2 } G \rho \int \frac { 2 \beta ^ { 2 } - \alpha \gamma } { \alpha ^ { 2 } } d \tilde { \Omega } .
$$

When we expand $2 \beta ^ { 2 } - \alpha \gamma$ in full, we find that it is a quadratic form that involves diagonal terms proportional to $x ^ { 2 }$ , $y ^ { 2 }$ , and $z ^ { 2 }$ , and non-diagonal terms proportional to $x y , x z$ , and $y z$ ; each term is multiplied by a specific function of $\tilde { \theta }$ and $\tilde { \phi }$ . Examining the non-diagonal terms closely, we find that once again the integrals vanish by symmetry. What is left over is the expression of Eq. (2.148), with

$$
\begin{array} { r l } & { { \cal A } _ { 0 } = \displaystyle \frac { 1 } { 2 \pi } \int \frac { d \tilde { \Omega } } { \alpha } \ : , } \\ & { { \cal A } _ { 1 } = \displaystyle \frac { 1 } { 2 \pi a _ { 1 } ^ { 2 } } \int \left( 1 - \frac { 2 \sin ^ { 2 } \tilde { \theta } \cos ^ { 2 } \tilde { \phi } } { a _ { 1 } ^ { 2 } \alpha } \right) \frac { d \tilde { \Omega } } { \alpha } \ : , } \\ & { { \cal A } _ { 2 } = \displaystyle \frac { 1 } { 2 \pi a _ { 2 } ^ { 2 } } \int \left( 1 - \frac { 2 \sin ^ { 2 } \tilde { \theta } \sin ^ { 2 } \tilde { \phi } } { a _ { 2 } ^ { 2 } \alpha } \right) \frac { d \tilde { \Omega } } { \alpha } \ : , } \\ & { { \cal A } _ { 3 } = \displaystyle \frac { 1 } { 2 \pi a _ { 3 } ^ { 2 } } \int \left( 1 - \frac { 2 \cos ^ { 2 } \tilde { \theta } } { a _ { 3 } ^ { 2 } \alpha } \right) \frac { d \tilde { \Omega } } { \alpha } \ : , } \end{array}
$$

where $\alpha$ continues to be given by Eq. (2.154).

The remaining task is to evaluate the integrals and bring them to the standard form displayed in Eqs. (2.149) and (2.150). The good news is that only $A _ { 0 }$ requires evaluation,

because all other integrals can be obtained by exploiting the identity

$$
A _ { i } = \frac { 1 } { a _ { i } ^ { 2 } } \biggl ( 1 - a _ { i } \frac { \partial } { \partial a _ { i } } \biggr ) A _ { 0 } ,
$$

which is easily established from the previous expressions; there is no summation over the index $i$ in the second term. To evaluate $A _ { 0 }$ we note first that the symmetries of the integrand allow us to restrict the range of integration to $\begin{array} { r } { 0 < \tilde { \phi } < \frac { \pi } { 2 } } \end{array}$ , at the cost of introducing a factor of 4; and in this range it is helpful to switch integration variables to $t : = \tan { \tilde { \phi } }$ , which varies from 0 to $\infty$ . In terms of the new variable we have that $\alpha = ( p + q t ^ { 2 } ) / ( 1 + t ^ { 2 } )$ with

$$
p : = \frac { \sin ^ { 2 } \tilde { \theta } } { a _ { 1 } ^ { 2 } } + \frac { \cos ^ { 2 } \tilde { \theta } } { a _ { 3 } ^ { 2 } } , \qquad q : = \frac { \sin ^ { 2 } \tilde { \theta } } { a _ { 2 } ^ { 2 } } + \frac { \cos ^ { 2 } \tilde { \theta } } { a _ { 3 } ^ { 2 } } .
$$

With $d \tilde { \phi } = d t / ( 1 + t ^ { 2 } )$ the integration is immediate, and we obtain

$$
A _ { 0 } = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } \sin { \tilde { \theta } } d { \tilde { \theta } } \int _ { 0 } ^ { \infty } { \frac { d t } { p + q t ^ { 2 } } } = \int _ { 0 } ^ { \pi } { \frac { \sin { \tilde { \theta } } d { \tilde { \theta } } } { \sqrt { p q } } } .
$$

To evaluate the remaining integral we note that the range of integration can be restricted to $\begin{array} { r } { 0 < \tilde { \theta } < \frac { \pi } { 2 } } \end{array}$ (introducing a factor of 2), and in this range it is helpful to adopt $u : = a _ { 3 } ^ { 2 } \tan ^ { 2 } \tilde { \theta }$ as a new integration variable, which varies from 0 to $\infty$ . In terms of the new variable we have that

$$
p = \frac { 1 } { a _ { 1 } ^ { 2 } } \frac { a _ { 1 } ^ { 2 } + u } { a _ { 3 } ^ { 2 } + u } , \qquad q = \frac { 1 } { a _ { 2 } ^ { 2 } } \frac { a _ { 2 } ^ { 2 } + u } { a _ { 3 } ^ { 2 } + u } ,
$$

and with $\begin{array} { r } { \sin { \tilde { \theta } } d \tilde { \theta } = \frac { 1 } { 2 } a _ { 3 } ( a _ { 3 } ^ { 2 } + u ) ^ { - 3 / 2 } d u } \end{array}$ , we find that the integral for $A _ { 0 }$ assumes the form originally given in Eq. (2.149). The expression for $A _ { i }$ is then recovered by exploiting the identity of Eq. (2.161).

The proof that $A _ { 1 } + A _ { 2 } + A _ { 3 } = 2$ begins with

$$
A _ { 1 } + A _ { 2 } + A _ { 3 } = a _ { 1 } a _ { 2 } a _ { 3 } \int _ { 0 } ^ { \infty } \frac { d u } { \Delta } \left( \frac { 1 } { a _ { 1 } ^ { 2 } + u } + \frac { 1 } { a _ { 2 } ^ { 2 } + u } + \frac { 1 } { a _ { 3 } ^ { 2 } + u } \right) ,
$$

and proceeds by recognizing that the expression within brackets is $2 \Delta ^ { - 1 } d \Delta / d u$ . Integration can then be carried out, and since $\Delta ^ { - 1 } = 0$ at the upper limit while $\Delta ^ { - 1 } = ( a _ { 1 } a _ { 2 } a _ { 3 } ) ^ { - 1 }$ at the lower limit, the result follows immediately.

# Equilibrium conditions

The equilibrium conditions for a rigidly rotating ellipsoid of uniform density are derived from Eq. (2.145). When $\rho$ is a constant the equation implies that $p / \rho = U + \Phi _ { \mathrm { C } } +$ constant, with $U$ given by Eq. (2.148) and $\begin{array} { r } { \Phi _ { \mathrm { { C } } } = \frac { 1 } { 2 } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) } \end{array}$ . Making the substitutions, we find that the pressure is given by

$$
{ \frac { p } { \pi G \rho } } = \mathrm { c o n s t a n t } - \bigg ( A _ { 1 } - { \frac { \omega ^ { 2 } } { 2 \pi G \rho } } \bigg ) x ^ { 2 } - \bigg ( A _ { 2 } - { \frac { \omega ^ { 2 } } { 2 \pi G \rho } } \bigg ) y ^ { 2 } - A _ { 3 } z ^ { 2 } .
$$

This, in particular, must apply to the surface of the ellipsoid (where $p = 0$ ), and because the surface is also described by Eq. (2.147), we find that the coefficients of the quadratic

forms must be related by the constraints

$$
a _ { 1 } ^ { 2 } \bigg ( A _ { 1 } - { \frac { \omega ^ { 2 } } { 2 \pi G \rho } } \bigg ) = a _ { 2 } ^ { 2 } \bigg ( A _ { 2 } - { \frac { \omega ^ { 2 } } { 2 \pi G \rho } } \bigg ) = a _ { 3 } ^ { 2 } A _ { 3 } .
$$

These equations give rise to the equilibrium conditions satisfied by the rotating ellipsoid.

The equations can be solved for the angular velocity, and the solution can be expressed in a number of ways:

$$
\begin{array} { r l r } & { } & { \frac { \omega ^ { 2 } } { 2 \pi G \rho } = \frac { a _ { 1 } ^ { 2 } A _ { 1 } - a _ { 3 } ^ { 2 } A _ { 3 } } { a _ { 1 } ^ { 2 } } } \\ & { } & \\ & { } & { = \frac { a _ { 2 } ^ { 2 } A _ { 2 } - a _ { 3 } ^ { 2 } A _ { 3 } } { a _ { 2 } ^ { 2 } } } \\ & { } & { = \frac { a _ { 1 } ^ { 2 } A _ { 1 } - a _ { 2 } ^ { 2 } A _ { 2 } } { a _ { 1 } ^ { 2 } - a _ { 2 } ^ { 2 } } . } \end{array}
$$

Only two of these relations are independent, and they are mutually compatible when

$$
a _ { 1 } ^ { 2 } a _ { 2 } ^ { 2 } ( A _ { 1 } - A _ { 2 } ) + \left( a _ { 1 } ^ { 2 } - a _ { 2 } ^ { 2 } \right) a _ { 3 } ^ { 2 } A _ { 3 } = 0 .
$$

Inserting the integral expressions for $A _ { i }$ displayed in Eq. (2.150), we find that the angular velocity is given by

$$
\begin{array} { c } { { \displaystyle \frac { \omega ^ { 2 } } { 2 \pi G \rho } = \frac { a _ { 1 } a _ { 3 } } { a _ { 2 } } \left( a _ { 2 } ^ { 2 } - a _ { 3 } ^ { 2 } \right) \int _ { 0 } ^ { \infty } \frac { { u } } { \left( a _ { 2 } ^ { 2 } + u \right) \left( a _ { 3 } ^ { 2 } + u \right) } \frac { d u } { \Delta } } } \\ { { { } ~ = \frac { a _ { 2 } a _ { 3 } } { a _ { 1 } } \left( a _ { 1 } ^ { 2 } - a _ { 3 } ^ { 2 } \right) \int _ { 0 } ^ { \infty } \frac { { u } } { \left( a _ { 1 } ^ { 2 } + u \right) \left( a _ { 3 } ^ { 2 } + u \right) } \frac { d u } { \Delta } } } \\ { { { } ~ = a _ { 1 } a _ { 2 } a _ { 3 } \int _ { 0 } ^ { \infty } \frac { u } { \left( a _ { 1 } ^ { 2 } + u \right) \left( a _ { 2 } ^ { 2 } + u \right) } \frac { d u } { \Delta } , } } \end{array}
$$

and that the compatibility condition becomes

$$
\left( a _ { 1 } ^ { 2 } - a _ { 2 } ^ { 2 } \right) \left[ a _ { 1 } ^ { 2 } a _ { 2 } ^ { 2 } \int _ { 0 } ^ { \infty } \frac { 1 } { \left( a _ { 1 } ^ { 2 } + u \right) \left( a _ { 2 } ^ { 2 } + u \right) } \frac { d u } { \Delta } - a _ { 3 } ^ { 2 } \int _ { 0 } ^ { \infty } \frac { 1 } { \left( a _ { 3 } ^ { 2 } + u \right) } \frac { d u } { \Delta } \right] = 0 .
$$

The first two expressions for $\omega ^ { 2 }$ imply that the principal axes of a rotating ellipsoid must be constrained by $a _ { 1 } > a _ { 3 }$ and $a _ { 2 } > a _ { 3 }$ : the shortest axis must be the rotation axis, and the figure is oblate, not prolate. The compatibility condition implies either one of two statements: either $a _ { 1 } = a _ { 2 }$ and the ellipsoid is axially symmetric, $o r$ the three axes must be adjusted to ensure that the integral constraint

$$
a _ { 1 } ^ { 2 } a _ { 2 } ^ { 2 } \int _ { 0 } ^ { \infty } \frac { 1 } { \left( a _ { 1 } ^ { 2 } + u \right) \left( a _ { 2 } ^ { 2 } + u \right) } \frac { d u } { \Delta } = a _ { 3 } ^ { 2 } \int _ { 0 } ^ { \infty } \frac { 1 } { \left( a _ { 3 } ^ { 2 } + u \right) } \frac { d u } { \Delta }
$$

is satisfied; for selected values of $a _ { 1 }$ and $a _ { 2 }$ , this equation can be solved for $a _ { 3 }$ . The axisymmetric branch defines the Maclaurin spheroids, which will be described in detail below. The non-axisymmetric branch constrained by Eq. (2.172) defines the Jacobi ellipsoids, to which we turn next.

Table 2.2 Solutions to the equilibrium conditions for Jacobi ellipsoids. The first entry of the table, for a1 = a2, is the point of bifurcation from the Maclaurin sequence.   

<table><tr><td>a2/a1</td><td>a3/a1</td><td>ω²/(2π Gp)</td></tr><tr><td>1.00</td><td>0.5827241662</td><td>0.1871148374</td></tr><tr><td>0.95</td><td>0.5677381338</td><td>0.1869173572</td></tr><tr><td>0.90</td><td>0.5518726119</td><td>0.1862832772</td></tr><tr><td>0.85</td><td>0.5350575095</td><td>0.1851433886</td></tr><tr><td>0.80</td><td>0.5172160586</td><td>0.1834185183</td></tr><tr><td>0.75</td><td>0.4982641698</td><td>0.1810182506</td></tr><tr><td>0.70</td><td>0.4781097616</td><td>0.1778396039</td></tr><tr><td>0.65</td><td>0.4566520785</td><td>0.1737657518</td></tr><tr><td>0.60</td><td>0.4337810349</td><td>0.1686649517</td></tr><tr><td>0.55</td><td>0.4093766373</td><td>0.1623899695</td></tr><tr><td>0.50</td><td>0.3833085784</td><td>0.1547785068</td></tr><tr><td>0.45</td><td>0.3554361455</td><td>0.1456555096</td></tr><tr><td>0.40</td><td>0.3256086868</td><td>0.1348388928</td></tr><tr><td>0.35</td><td>0.2936670362</td><td>0.1221514037</td></tr><tr><td>0.30</td><td>0.2594465778</td><td>0.1074435407</td></tr><tr><td>0.25</td><td>0.2227831754</td><td>0.0906367278</td></tr><tr><td>0.20</td><td>0.1835242862</td><td>0.0718047786</td></tr><tr><td>0.15</td><td>0.1415500250</td><td>0.0513316734</td></tr><tr><td>0.10</td><td>0.09681524257</td><td>0.0302360801</td></tr><tr><td>0.05</td><td>0.04944350586</td><td>0.0109330058</td></tr></table>

Returning to Eq. (2.166), we insert the relations of Eq. (2.167) to simplify the expression for the pressure, and we adjust the constant to ensure that $p = 0$ on the surface of the ellipsoid. The end result of this exercise is

$$
p = p _ { c } \bigg ( 1 - \frac { x ^ { 2 } } { a _ { 1 } ^ { 2 } } - \frac { y ^ { 2 } } { a _ { 2 } ^ { 2 } } - \frac { z ^ { 2 } } { a _ { 3 } ^ { 2 } } \bigg ) ,
$$

where $p _ { c } : = \pi G \rho ^ { 2 } a _ { 3 } ^ { 2 } A _ { 3 }$ is the central pressure.

# Jacobi ellipsoids

Solutions to the compatibility condition of Eq. (2.172) are presented in Table 2.2, which also lists the corresponding values of $\omega ^ { 2 }$ calculated according to Eq. (2.170c). Because $a _ { 1 }$ can be adopted as the fundamental length scale of the rotating body, the values of $a _ { 2 }$ and $a _ { 3 }$ are given in units of $a _ { 1 }$ . The table is constructed by choosing $a _ { 2 } / a _ { 1 }$ and solving the compatibility condition for $a _ { 3 } / a _ { 1 }$ ; without loss of generality we take $a _ { 2 }$ to be smaller than $a _ { 1 }$ . Two main observations can be made regarding the numerical results. The first is that as we proceed along the Jacobi sequence, with $a _ { 2 } / a _ { 1 }$ decreasing from unity, we find that $a _ { 3 } / a _ { 1 }$ decreases, giving rise to an increasingly elongated and flattened figure. The second is that the angular velocity decreases along the sequence, so that the most deformed figure is the one with the least angular velocity; the maximum value of $\omega ^ { 2 }$ on the sequence is a factor of 0.187 smaller than the Poincare bound of Eq. ( ´ 2.131).

The mass of a Jacobi ellipsoid is given by

$$
M = \int \rho d ^ { 3 } x = \frac { 4 \pi } { 3 } \rho a _ { 1 } a _ { 2 } a _ { 3 } ,
$$

its angular momentum is

$$
J = \omega \int \rho ( x ^ { 2 } + y ^ { 2 } ) d ^ { 3 } x = \frac { 1 } { 5 } M \omega \big ( a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } \big ) ,
$$

and its total kinetic energy is

$$
\mathcal { T } = \frac { 1 } { 2 } \omega J = \frac { 1 } { 1 0 } M \omega ^ { 2 } \big ( a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } \big ) .
$$

To perform these integrals it is helpful to adopt a system of ellipsoidal coordinates $( s , \theta , \phi )$ related to the original system $( x , y , z )$ by $x = a _ { 1 } s \sin \theta \cos \phi$ , $y = a _ { 2 } s \sin \theta \sin \phi$ , and $z =$ $a _ { 3 } s \cos \theta$ ; the volume integral covers the interval $0 < s < 1$ and the usual range of the angular variables. From the results displayed in the table it is possible to show that $J$ , when measured in units of $\sqrt { G M ^ { 3 } \bar { a } }$ with $\bar { a } : = ( a _ { 1 } a _ { 2 } a _ { 3 } ) ^ { 1 / 3 }$ , increases along the Jacobi sequence.

# Maclaurin spheroids

When $a _ { 1 } = a _ { 2 }$ the rigidly rotating body becomes a Maclaurin spheroid. In this case $A _ { 0 } , A _ { i }$ , and $\omega$ can all be expressed as simple functions of the eccentricity

$$
e : = \sqrt { 1 - ( a _ { 3 } / a ) ^ { 2 } } ,
$$

in which we have set $a : = a _ { 1 } = a _ { 2 }$ . Inserting $a _ { 3 } = a { \sqrt { 1 - e ^ { 2 } } }$ within Eqs. (2.149) and (2.150), we find that the integrals evaluate to

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { 0 } = 2 a ^ { 2 } \frac { \sqrt { 1 - e ^ { 2 } } } { e } \arcsin e , } } \\ { { \displaystyle { \cal A } _ { 1 } = { \cal A } _ { 2 } = \frac { \sqrt { 1 - e ^ { 2 } } } { e ^ { 3 } } \arcsin e - \frac { 1 - e ^ { 2 } } { e ^ { 2 } } , } } \\ { { \displaystyle { \cal A } _ { 3 } = - 2 \frac { \sqrt { 1 - e ^ { 2 } } } { e ^ { 3 } } \arcsin e + \frac { 2 } { e ^ { 2 } } . } } \end{array}
$$

On the other hand, the relation $\omega ^ { 2 } / ( 2 \pi G \rho ) = A _ { 1 } - ( a _ { 3 } / a ) ^ { 2 } A _ { 3 }$ produces

$$
\frac { \omega ^ { 2 } } { 2 \pi G \rho } = \frac { \sqrt { 1 - e ^ { 2 } } } { e ^ { 3 } } ( 3 - 2 e ^ { 2 } ) \mathrm { a r c s i n } e - 3 \frac { 1 - e ^ { 2 } } { e ^ { 2 } } .
$$

This expression for the angular velocity is plotted in Fig. 2.5. The figure reveals that the angular velocity first increases with the eccentricity, but that it reaches a maximum of $\omega ^ { 2 } / ( 2 \pi G \rho ) = 0 . 2 2 4 6 6 6$ when $e = 0 . 9 2 9 9 5 6$ . It then decreases to zero as the eccentricity increases toward unity; in this limit we have an infinitely thin disk rotating with negligible angular velocity.

It is known, however, that the sequence of Maclaurin spheroids never comes close to these extremes. There exists on the sequence a point of bifurcation at which a Maclaurin spheroid and a Jacobi ellipsoid with $a _ { 1 } = a _ { 2 }$ are both valid solutions to the equilibrium equations; this point occurs at $e = 0 . 8 1 2 6 7 0$ , where $\omega ^ { 2 } / ( 2 \pi G \rho ) = 0 . 1 8 7 1 1 5$ . Going beyond the bifurcation point, it is observed that for a given eccentricity, the Jacobi ellipsoid has a smaller total energy than the corresponding Maclaurin spheroid, and this suggests that in the presence of a dissipative mechanism, such as viscosity or gravitational radiation damping, the Maclaurin spheroid is unstable to perturbations that eventually convert it to a Jacobi ellipsoid. This conclusion is confirmed by a stability analysis: the bifurcation point marks the onset of a secular instability that drives a Maclaurin spheroid toward a Jacobi ellipsoid. There is also, further along the sequence beyond $e = 0 . 9 5 2 8 8 7$ , a regime of dynamical instability that, even in the absence of dissipation, converts a Maclaurin spheroid to a Jacobi ellipsoid.

![](images/a55ccb3f96cf5c550c7e8d6eabf1c5ab862ea7f25c303fc7526383245eb7fc00.jpg)  
Squared angular velocity $\omega ^ { 2 } / ( 2 \pi G \rho )$ as a function of eccentricity e for Maclaurin spheroids. The plot reveals an ascending branch, along which the angular velocity increases with eccentricity, and a descending branch, along which the angular velocity decreases. The figure also shows the Jacobi sequence, which bifurcates from the Maclaurin sequence when $e = 0 . 8 1 2 6 7 0$ .

From the results obtained previously in the case of Jacobi ellipsoids, we find that the mass, angular momentum, and kinetic energy of a Maclaurin spheroid are given by

$$
\begin{array} { l } { { { \cal M } = \displaystyle \frac { 4 \pi } { 3 } \rho a ^ { 3 } \sqrt { 1 - e ^ { 2 } } , } } \\ { { { \cal J } = \displaystyle \frac { 2 } { 5 } { \cal M } \omega a ^ { 2 } , } } \\ { { { \cal T } = \displaystyle \frac { 1 } { 5 } { \cal M } \omega ^ { 2 } a ^ { 2 } . } } \end{array}
$$

In addition to these results, a computation of the gravitational potential energy – refer to Exercise 2.3 – reveals that

$$
\Omega = - \frac { 3 } { 5 } \frac { G M ^ { 2 } } { a } \frac { \arcsin e } { e } ,
$$

so that

$$
\tau : = \frac { \mathcal { T } } { | \Omega | } = \frac { 3 } { 2 e ^ { 2 } } \bigg ( 1 - \frac { e \sqrt { 1 - e ^ { 2 } } } { \arcsin e } \bigg ) - 1 .
$$

This relation implies that as $e$ increases from 0 to $1 , \tau$ increases monotonically from 0 to $\frac { 1 } { 2 }$ . The maximum angular velocity is reached when $\tau = 0 . 2 3 7 9 0 2$ , and the point of bifurcation occurs at $\tau = 0 . 1 3 7 5 2 8$ .

The gravitational potential inside a Maclaurin spheroid is given by Eq. (2.148) with $A _ { 1 } = A _ { 2 }$ , and the quadratic form implies that it contains multipoles of order $\ell = 0$ and $\ell = 2$ only. The external potential, on the other hand, is more complicated, and must be expressed as an infinite multipole expansion

$$
U _ { \mathrm { e x t } } = \frac { G M } { r } \left[ 1 - \sum _ { \ell = 2 } ^ { \infty } J _ { \ell } \left( \frac { a } { r } \right) ^ { \ell } P _ { \ell } ( \cos \theta ) \right] ,
$$

where cos $\theta : = z / r$ , and where the dimensionless multipole moments

$$
J _ { \ell } : = - \frac { 1 } { M a ^ { \ell } } \int \rho r ^ { \ell } P _ { \ell } ( \cos \theta ) d ^ { 3 } x
$$

were first introduced in Sec. 1.5.2 – refer to Eq. (1.143). The existence of an infinite number of multipole moments has to do with the fact that the internal and external potentials must match across a spheroidal surface; in this context, a simple internal potential can give rise to a complicated external potential. After performing the radial integration we find that the multipole moments become

$$
J _ { \ell } = - \frac { 2 \pi \rho } { ( \ell + 3 ) M a ^ { \ell } } \int R ^ { \ell + 3 } ( \theta ) P _ { \ell } ( \cos \theta ) d \cos \theta ,
$$

where $R ( \theta )$ , given explicitly by

$$
\frac { 1 } { R ^ { 2 } } = \frac { \sin ^ { 2 } \theta } { a ^ { 2 } } + \frac { \cos ^ { 2 } \theta } { a _ { 3 } ^ { 2 } } ,
$$

is the description of the spheroidal surface in the spherical coordinates $( r , \theta , \phi )$ . Mercifully these integrals can be evaluated, and after a short computation we obtain

$$
J _ { \ell } = \frac { 3 ( - 1 ) ^ { \ell / 2 + 1 } } { ( \ell + 1 ) ( \ell + 3 ) } e ^ { \ell }
$$

for the multipole moments of a Maclaurin spheroid. You will be asked to go through the steps of this calculation in Exercise 2.4.

When the eccentricity is small, the various functions encountered previously can be expanded in powers of $e$ , and they become

$$
\begin{array} { r l } & { { \mathcal A } _ { 0 } = 2 a ^ { 2 } \Bigg [ 1 - \frac { 1 } { 3 } e ^ { 2 } - \frac { 2 } { 1 5 } e ^ { 4 } + O ( e ^ { 6 } ) \Bigg ] , } \\ & { { \mathcal A } _ { 1 } = { \mathcal A } _ { 2 } = \frac { 2 } { 3 } \Bigg [ 1 - \frac { 1 } { 5 } e ^ { 2 } - \frac { 4 } { 3 5 } e ^ { 4 } + O ( e ^ { 6 } ) \Bigg ] , } \\ & { { \mathcal A } _ { 5 } = \frac { 2 } { 3 } \Bigg [ 1 + \frac { 2 } { 5 } e ^ { 2 } + \frac { 8 } { 3 5 } e ^ { 4 } + O ( e ^ { 6 } ) \Bigg ] , } \\ & { \frac { \omega ^ { 2 } } { 2 \pi G \rho } = \frac { 4 } { 1 5 } e ^ { 2 } \Bigg [ 1 + \frac { 1 } { 7 } e ^ { 2 } - \frac { 8 } { 2 3 1 } e ^ { 4 } + O ( e ^ { 6 } ) \Bigg ] , } \\ & { { \mathcal D } = - \frac { 3 } { 5 } \frac { G M ^ { 2 } } { a u } \Bigg [ 1 + \frac { 1 } { 6 } e ^ { 2 } + \frac { 3 } { 4 0 } e ^ { 4 } + O ( e ^ { 6 } ) \Bigg ] } \\ & { \quad \quad \quad \tau = \frac { 2 } { 1 5 } e ^ { 2 } \Bigg [ 1 + \frac { 1 0 } { 2 1 } e ^ { 2 } + \frac { 9 2 } { 3 1 5 } e ^ { 4 } + O ( e ^ { 6 } ) \Bigg ] . } \end{array}
$$

# 2.4 General theory of deformed bodies

When we relax the assumption of uniform density, the problem of finding the structure of a general rotating body becomes much more involved, even when we retain the assumption of rigid rotation. On the other hand, most planets and stars rotate sufficiently slowly that they deviate only slightly from spherically symmetry. For example, the Earth’s dimensionless quadrupole moment $J _ { 2 }$ is approximately $1 0 ^ { - 3 }$ , and the higher $J _ { \ell } \mathbf { s }$ are a thousand times smaller; for the Sun, $J _ { 2 } \simeq 2 \times 1 0 ^ { - 7 }$ . For these slowly-rotating bodies it is appropriate to take an approach in which the deviations from spherical symmetry are assumed to be small. This is the standard fare of perturbation theory, in which one starts with an unperturbed, spherical configuration and deforms it so slightly that all equations can be linearized with respect to the deviations from spherical symmetry.

The perturbative approach to deformed bodies is sufficiently general that we can consider bodies with arbitrary equations of state, and deformations that result not only from rotation, but also from tidal fields produced by external bodies. Our goal in this section is to develop this framework. We shall continue to restrict our attention to equilibrium configurations, but in Sec. 2.5.3 we will relax this assumption and consider fully dynamical perturbations of spherical bodies.

# 2.4.1 Fluid equations

We return to Eq. (2.4), the statement of Euler’s equation in the moving (but non-rotating) frame of a given body $A$ in a system of $N$ separated bodies. We now keep the external terms associated with the remote bodies, and adopt the simplified form of Eq. (2.11), which neglects the influence of $A$ ’s higher multipole moments on its motion in the external gravitational field – these vanish in spherical symmetry, and produce second-order corrections in perturbation theory. Assuming that $A$ is rotating rigidly with angular velocity $\omega$ , we subject Euler’s equation to a transformation to the rotating frame, in the way described near the end of Sec. 2.3.1 – refer to Eq. (2.139).

Collecting results, we find that Euler’s equation takes the form of

$$
\frac { d u ^ { j } } { d t } = - \frac 1 \rho \partial _ { j } p - 2 \epsilon _ { j k n } \omega ^ { k } u ^ { n } + \partial _ { j } \Phi ,
$$

where $\pmb { u }$ is the velocity vector in the rotating frame, $\omega : = [ 0 , 0 , \omega ]$ is the angular-velocity vector, and

$$
\Phi : = U + \Phi _ { \mathrm { { C } } } + U _ { \mathrm { { t i d a l } } }
$$

is a generalized potential that includes the body’s gravitational potential $U$ (previously denoted $U _ { A }$ ), the centrifugal potential

$$
\Phi _ { \mathrm { C } } = { \frac { 1 } { 2 } } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) ,
$$

and the tidal potential

$$
U _ { \mathrm { t i d a l } } = - \sum _ { \ell = 2 } ^ { \infty } { \frac { 1 } { \ell ! } } \mathcal { E } _ { L } ( t ) x ^ { L } ,
$$

which was previously denoted $U _ { \neg A } ^ { \mathrm { e f f } }$ . The STF tensors $\mathcal { E } _ { L } ( t ) : = - \partial _ { L } U _ { \neg A } ( t , \mathbf { 0 } )$ are the tidal moments associated with the external potential; they are obtained by differentiating $U _ { \neg A }$ with respect to $x ^ { j }$ and evaluating the result at the body’s center-of-mass $\mathbf { \nabla } _ { \mathbf { \boldsymbol { x } } } = \mathbf { \boldsymbol { 0 } }$ . In our treatment the tidal moments are taken to be known functions of time; their specification depends on the particular application.

As usual the Euler equation must be supplemented by the continuity equation $\partial _ { t } \rho +$ $\partial _ { j } ( \rho u ^ { j } ) = 0$ and Poisson’s equation $\nabla ^ { 2 } U = - 4 \pi G \rho$ for the body’s potential; the expression of Eq. (2.192) implies that the tidal potential satisfies Laplace’s equation $\nabla ^ { 2 } U _ { \mathrm { t i d a l } } = 0$ , and we also have that $\nabla ^ { 2 } \Phi _ { \mathrm { C } } = 2 \omega ^ { 2 }$ .

For our developments below it is useful to decompose the centrifugal potential $\Phi _ { \mathrm { { C } } }$ into monopole and quadrupole pieces, according to

$$
\Phi _ { \mathrm { C } } = \Phi _ { \mathrm { C } } ^ { \ell = 0 } + \Phi _ { \mathrm { C } } ^ { \ell = 2 } ,
$$

with

$$
\Phi _ { \mathrm { C } } ^ { \ell = 0 } = { \frac { 1 } { 3 } } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) = { \frac { 1 } { 3 } } \omega ^ { 2 } r ^ { 2 }
$$

and

$$
\Phi _ { \mathrm { C } } ^ { \ell = 2 } = \frac { 1 } { 6 } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } - 2 z ^ { 2 } ) = - \frac { 1 } { 3 } \omega ^ { 2 } r ^ { 2 } P _ { 2 } ( \cos \theta ) .
$$

The monopole piece satisfies $\nabla ^ { 2 } \Phi _ { \mathrm { C } } ^ { \ell = 0 } = 2 \omega ^ { 2 }$ , while $\nabla ^ { 2 } \Phi _ { \mathrm { C } } ^ { \ell = 2 } = 0$

The tidal potential depends on time through the tidal moments, which contain all the relevant information about the changing positions of the external bodies. This time dependence implies that there is an inherent contradiction between Euler’s equation and the goal of finding equilibrium configurations. The contradiction would indeed be severe if the external bodies were in $A$ ’s immediate vicinity, and in such circumstances no equilibrium solutions could ever be found. (We shall consider this situation in Sec. 2.5.3.) But the contradiction is very mild when the external bodies are remote and move on an orbital time scale $T _ { \mathrm { o r b } } \sim \sqrt { r _ { A B } ^ { 3 } / G M }$ that is much longer than the internal, hydrodynamical time scale $T _ { \mathrm { i n t } } \sim ( G \rho ) ^ { - 1 / 2 } \sim \sqrt { R ^ { 3 } / G M }$ ; here $r _ { A B }$ is a typical inter-body separation, $R$ is the body’s radius, and the time scales are indeed well separated when $r _ { A B } \gg R$ . In such circumstances, the time dependence contained in $\mathcal { E } _ { L } ( t )$ is too slow to take the body out of equilibrium; the solutions will still carry a dependence upon $t$ inherited from the tidal moments, but this reflects a parametric dependence instead of a genuine dynamical dependence.

# 2.4.2 Unperturbed configuration

The unperturbed configuration of the fluid is spherically symmetric and in equilibrium; it corresponds to the absence of external bodies and rotational effects. The equations that govern such a configuration were presented in Sec. 2.2: we have the equation of hydrostatic equilibrium,

$$
\frac { d p } { d r } = \rho \frac { d } { d r } \big ( U + \Phi _ { \mathrm { C } } ^ { \ell = 0 } \big ) ,
$$

and Poisson’s equation

$$
{ \frac { 1 } { r ^ { 2 } } } { \frac { d } { d r } } \biggl ( r ^ { 2 } { \frac { d U } { d r } } \biggr ) = - 4 \pi G \rho
$$

for the body potential. It is assumed that the density $\rho$ and pressure $p$ are related by an equation of state. For convenience we choose to insert the monopole piece of $\Phi _ { \mathrm { { C } } }$ in the equation of hydrostatic equilibrium, in spite of the fact that it is part of the perturbation. This choice is motivated by the fact that unlike all other terms in the perturbing potential, $\Phi _ { \mathrm { C } } ^ { \ell = 0 }$ is spherically symmetric, and thus naturally included as part of the unperturbed configuration.

To solve the unperturbed equations we introduce an effective potential

$$
\tilde { U } : = U + \Phi _ { \mathrm { C } } ^ { \ell = 0 }
$$

associated with an effective mass density

$$
\tilde { \rho } : = \rho - \frac { \omega ^ { 2 } } { 2 \pi G } ,
$$

so that $\nabla ^ { 2 } \tilde { U } = - 4 \pi G \tilde { \rho }$ . If we also introduce an effective mass function $\tilde { m } ( r )$ defined by

$$
\frac { d \tilde { m } } { d r } = 4 \pi r ^ { 2 } \tilde { \rho } ,
$$

then $d \tilde { U } / d r = - G \tilde { m } / r ^ { 2 }$ and the equation of hydrostatic equilibrium becomes

$$
\frac { d p } { d r } = - \rho \frac { G \tilde { m } } { r ^ { 2 } } .
$$

Note that this equation involves the actual mass density $\rho$ together with the effective mass function $\tilde { m }$ . We assume that these equations can be solved for a selected equation of state, and that $\rho ( \boldsymbol { r } ) , p ( \boldsymbol { r } ) , \tilde { m } ( \boldsymbol { r } )$ , and $\tilde { U } ( \boldsymbol { r } )$ are known for the unperturbed configuration. The stellar radius $R$ is such that $p ( r = R ) = 0$ , and the total mass is $M = \tilde { m } ( r = R ) + \omega ^ { 2 } R ^ { 3 } / ( 6 \pi G )$ .

# 2.4.3 Fluid perturbations

The introduction of $U _ { \mathrm { t i d a l } }$ and $\Phi _ { \mathrm { C } } ^ { \ell = 2 }$ in Euler’s equation creates a perturbation of the fluid configuration. The density changes from $\rho$ to $\rho + \delta \rho$ , the pressure from $p$ to $p + \delta p$ , the body potential from $U$ to $U + \delta U$ , and the fluid velocity $u ^ { j }$ is no longer zero if the equilibrium is disturbed. We suppose that the perturbation is small, and we work consistently to first order in all perturbation variables.

The perturbation of any fluid quantity $Q$ can be described either in terms of its Eulerian perturbation $\delta Q$ (as was done previously), or its Lagrangian perturbation $\Delta Q$ . The Eulerian point of view is macroscopic: $Q$ is compared to its unperturbed value $Q _ { 0 }$ at the same position in space, and

$$
\delta Q : = Q ( t , \pmb { x } ) - Q _ { 0 } ( t , \pmb { x } ) .
$$

The Lagrangian point of view is microscopic: $Q$ is compared at the same fluid element, which is displaced by the vector $\pmb { \xi } ( t , \pmb { x } )$ relative to its position $\boldsymbol { x }$ in the unperturbed configuration. The Lagrangian perturbation is

$$
\begin{array} { r } { \Delta Q : = Q ( t , { \boldsymbol { x } } + { \boldsymbol { \xi } } ) - Q _ { 0 } ( t , { \boldsymbol { x } } ) = \delta Q + \xi ^ { j } \partial _ { j } Q _ { 0 } . } \end{array}
$$

From the definition of the displacement vector it is obvious that

$$
\Delta { \pmb u } = \frac { d { \pmb \xi } } { d t } ,
$$

where $d / d t$ is the Lagrangian time derivative, which refers to the unperturbed flow. When the unperturbed fluid is in equilibrium, $d / d t = \partial / \partial t$ .

The commutation rules,

$$
\begin{array} { l } { \displaystyle \delta \partial _ { t } = \partial _ { t } \delta , } \\ { \displaystyle \delta \partial _ { j } = \partial _ { j } \delta , } \\ { \displaystyle \Delta \partial _ { t } = \partial _ { t } \Delta - ( \partial _ { t } \xi ^ { j } ) \partial _ { j } , } \\ { \displaystyle \Delta \partial _ { j } = \partial _ { j } \Delta - ( \partial _ { j } \xi ^ { k } ) \partial _ { k } , } \\ { \displaystyle \Delta \frac { d } { d t } = \frac { d } { d t } \Delta , } \end{array}
$$

are easy to establish, and they permit an efficient manipulation of the perturbed Euler equation. For example, $\delta ( \partial _ { j } Q ) = \partial _ { j } Q - \partial _ { j } Q _ { 0 }$ while $\partial _ { j } ( \delta Q ) = \partial _ { j } ( Q - Q _ { 0 } ) = \partial _ { j } Q - \partial _ { j } Q _ { 0 }$ , and we see that the operations commute. As another example, $\Delta ( \partial _ { j } Q ) =$ $\delta ( \partial _ { j } Q ) + \xi ^ { k } \partial _ { k j } Q _ { 0 } = \partial _ { j } ( \delta Q ) + \xi ^ { k } \partial _ { j k } Q _ { 0 }$ while $\begin{array} { r } { \partial _ { j } ( \Delta Q ) = \partial _ { j } ( \delta Q ) + \partial _ { j } ( \xi ^ { k } \partial _ { k } Q _ { 0 } ) = } \end{array}$ $\partial _ { j } ( \delta Q ) + ( \partial _ { j } \xi ^ { k } ) ( \partial _ { k } Q _ { 0 } ) + \xi ^ { k } \partial _ { j k } Q _ { 0 }$ , and we see that these operations do not commute.

The mass of a selected portion of the fluid stays constant during a perturbation. In the unperturbed configuration the portion of the fluid occupies the volume $V$ ; in the perturbed configuration it occupies the volume $V + \Delta V$ . The mass of the unperturbed configuration is $\textstyle \int _ { V } \rho d ^ { 3 } x$ , the mass of the perturbed configuration is $\begin{array} { r } { \int _ { V + \Delta V } ( \rho + \delta \rho ) d ^ { 3 } x } \end{array}$ , and we insist that the two integrals must produce the same number. The first integral for the mass of the perturbed configuration can be expressed as $\begin{array} { r } { \int _ { V } \rho d ^ { 3 } x + \oint _ { S } \rho \pmb { \xi } \cdot d S } \end{array}$ , where $S$ is the closed surface bounding $V$ , and $d \pmb { S }$ is its (outward-directed) surface element. After converting the surface integral to a volume integral, we find that the statement of mass conservation is $\int _ { V } [ \delta \rho +$ $\partial _ { j } ( \rho \xi ^ { j } ) ] d ^ { 3 } x = 0$ . Because this statement must hold for any piece of the fluid, we have

$$
\delta \rho = - { \partial } _ { j } ( \rho \xi ^ { j } ) ,
$$

or

$$
\Delta \rho = - \rho \partial _ { j } \xi ^ { j } .
$$

These are time-integrated forms of the perturbed continuity equation.

By virtue of the equation of state satisfied by the fluid, the perturbation of the pressure is directly linked to the density perturbation. The link is provided by the quantity $\Gamma _ { 1 }$ , which is defined by the (Lagrangian) statement

$$
\frac { \Delta p } { p } = \Gamma _ { 1 } \frac { \Delta \rho } { \rho } .
$$

In general $\Gamma _ { 1 }$ is a function of time and position within the fluid; for adiabatic changes it is given by $c _ { P } / c _ { V }$ , the ratio of specific heats. According to this equation, the Eulerian perturbation of the pressure is given by

$$
\delta p = - \Gamma _ { 1 } p \partial _ { j } \xi ^ { j } - \xi ^ { j } \partial _ { j } p .
$$

The perturbation of Euler’s equation can be formulated in either the Eulerian picture or the Lagrangian picture. We begin with the Lagrangian picture, and submit Eq. (2.189) to the operator $\Delta$ and use the commutation rules to simplify the results. For example, the perturbation of the left-hand side is $\Delta ( d u ^ { j } / d t )$ , which can be written as $d ( \Delta u ^ { j } ) / d t$ by virtue of the commutation rules; invoking now Eq. (2.204), we write this in its final form of $d ^ { 2 } \xi ^ { j } / d t ^ { 2 }$ . Proceeding in a similar way with the remaining terms, we find that the perturbed Euler equation can be expressed as

$$
\frac { d ^ { 2 } \xi ^ { j } } { d t ^ { 2 } } = \frac { \Delta \rho } { \rho ^ { 2 } } \partial _ { j } p - \frac { 1 } { \rho } \partial _ { j } \Delta p - 2 \epsilon _ { j k n } \omega ^ { k } \frac { d \xi ^ { n } } { d t } + \partial _ { j } \Delta \Phi + \left( \partial _ { j } \xi ^ { k } \right) \left( \frac { 1 } { \rho } \partial _ { k } p - \partial _ { k } \Phi \right) .
$$

When the unperturbed state is an equilibrium configuration, the unperturbed velocity field vanishes, the factor multiplying $\partial _ { j } \xi ^ { k }$ vanishes, and the equation simplifies to

$$
\frac { \partial ^ { 2 } \xi ^ { j } } { \partial t ^ { 2 } } = \frac { \Delta \rho } { \rho ^ { 2 } } \partial _ { j } p - \frac { 1 } { \rho } \partial _ { j } \Delta p - 2 \epsilon _ { j k n } \omega ^ { k } \frac { \partial \xi ^ { n } } { \partial t } + \partial _ { j } \Delta \Phi .
$$

When the perturbed state is also an equilibrium configuration, $\partial \xi ^ { j } / \partial t = 0$ and the equation simplifies further.

Moving next to the Eulerian picture, we now submit Eq. (2.189) to the operator δ and use the commutation rules to simplify the result. For example, the perturbation of the first term on the right-hand side is $\delta ( \rho ^ { - 1 } \partial _ { j } p ) = - \rho ^ { - 2 } ( \delta \rho ) \partial _ { j } p + \rho ^ { - 1 } \delta ( \partial _ { j } p ) = - \rho ^ { - 2 } ( \delta \rho ) \partial _ { j } p +$ $\rho ^ { - 1 } \partial _ { j } \delta p$ . Proceeding in a similar way with the other terms, and assuming once more that the unperturbed state is an equilibrium configuration, we find that the perturbed Euler equation can also be expressed as

$$
\frac { \partial ^ { 2 } \xi ^ { j } } { \partial t ^ { 2 } } = \frac { \delta \rho } { \rho ^ { 2 } } \partial _ { j } p - \frac { 1 } { \rho } \partial _ { j } \delta p - 2 \epsilon _ { j k n } \omega ^ { k } \frac { \partial \xi ^ { n } } { \partial t } + \partial _ { j } \delta \Phi .
$$

The equation simplifies further when the perturbed configuration is also in equilibrium.

The perturbed Euler equation, either Eq. (2.211) or Eq. (2.212), can be solved once we incorporate the expressions obtained previously for $\delta \rho$ (or $\Delta \rho$ ) and $\delta p$ (or $\Delta p$ ). A missing ingredient is the perturbation of the body’s gravitational potential, which is best calculated in the Eulerian picture. It satisfies Poisson’s equation

$$
\nabla ^ { 2 } \delta U = - 4 \pi G \delta \rho ,
$$

and the solution can be fed into Euler’s equation.

# 2.4.4 Perturbed equilibrium

# Perturbation equations

When the perturbed fluid is also in equilibrium, $\partial \xi ^ { j } / \partial t = 0$ and Eq. (2.212) simplifies to

$$
\frac { \delta \rho } { \rho ^ { 2 } } \partial _ { j } p - \frac { 1 } { \rho } \partial _ { j } \delta p + \partial _ { j } \delta \Phi = 0 .
$$

The perturbation of the generalized potential is decomposed as

$$
\delta \Phi = \delta U + V ,
$$

where

$$
V : = U _ { \mathrm { t i d a l } } + \Phi _ { \mathrm { C } } ^ { \ell = 2 }
$$

is the potential driving the perturbation; we recall that $U _ { \mathrm { t i d a l } }$ is given by Eq. (2.192), and that $\Phi _ { \mathrm { C } } ^ { \ell = 2 }$ is defined by Eq. (2.195).

Our task is to solve Eq. (2.214), assuming that $V$ is specified. To achieve this we choose $\xi ^ { j }$ to describe the displacement of a fluid element on a spherical surface $\rho =$ constant in the unperturbed configuration to the deformed surface $\rho =$ constant in the perturbed configuration (the mass density is numerically the same on both surfaces). This ensures that $\Delta \rho \equiv 0$ , and Eq. (2.208) further ensures that $\Delta p = 0$ . These results imply that

$$
\partial _ { j } \xi ^ { j } = 0
$$

and

$$
\delta \rho = - \xi ^ { j } \partial _ { j } \rho , \qquad \delta p = - \xi ^ { j } \partial _ { j } p .
$$

Because the unperturbed density $\rho$ and pressure $p$ depend on $r$ only, these equations involve only $\xi ^ { r }$ , the radial component of the displacement vector; we shall not need to solve for the angular components, which are constrained by the divergence-free condition.

# Spherical-harmonic decomposition

To proceed it is helpful to decompose all perturbation quantities in spherical harmonics:

$$
\begin{array} { l } { { \displaystyle { \xi ^ { r } = \sum _ { \ell m } r f _ { \ell m } ( \ell , \phi ) , } } } \\ { { \displaystyle { \delta \rho = \sum _ { \ell m } \rho _ { \ell m } ( r ) Y _ { \ell m } ( \theta , \phi ) , } } } \\ { { \displaystyle { \delta p = \sum _ { \ell m } \rho _ { \ell m } ( r ) Y _ { \ell m } ( \theta , \phi ) , } } } \\ { { \displaystyle { \delta U = \sum _ { \ell m } U _ { \ell m } ( r ) Y _ { \ell m } ( \theta , \phi ) , } } } \\ { { \displaystyle { V = \sum _ { \ell m } V _ { \ell m } ( r ) Y _ { \ell m } ( \theta , \phi ) , } } } \end{array}
$$

in which $( r , \theta , \phi )$ are spherical polar coordinates associated with the rotating frame $x ^ { j }$ ; note that a factor $r$ has been inserted in the relation between $\xi ^ { r }$ and its (dimensionless) coefficients $f _ { \ell m }$ . By virtue of Eqs. (2.192) and (2.195), the spherical-harmonic decompositions begin at $\ell = 2$ , with $m$ running from $- \ell$ to $\ell$ .

The equations for $\delta \rho$ and $\delta p$ imply that

$$
\rho _ { \ell m } = - r \rho ^ { \prime } f _ { \ell m }
$$

and

$$
p _ { \ell m } = - r p ^ { \prime } f _ { \ell m } = \frac { \rho G m } { r } f _ { \ell m } ,
$$

where a prime indicates differentiation with respect to $r$ . We invoked Eq. (2.201) to replace $p ^ { \prime }$ in the last equation. We no longer distinguish between the effective mass function $\tilde { m } ( r )$ and the actual mass function $m ( r )$ , because the difference is of first order in the perturbation, and would therefore be of second order after multiplication by $f _ { \ell m }$ .

The spherical-harmonic components of $\delta U$ have already been introduced and examined in Sec. 1.5.2 – refer to the discussion following Eq. (1.122). By virtue of Poisson’s equation they satisfy the differential equation

$$
r ^ { 2 } U _ { \ell m } ^ { \prime \prime } + 2 r U _ { \ell m } ^ { \prime } - \ell ( \ell + 1 ) U _ { \ell m } = - 4 \pi G r ^ { 2 } \rho _ { \ell m }
$$

in the body’s interior. Outside the body they are given by

$$
U _ { \ell m } ^ { \mathrm { o u t } } ( r ) = \frac { 4 \pi G } { 2 \ell + 1 } \frac { I _ { \ell m } } { r ^ { \ell + 1 } } ,
$$

where $I _ { \ell m }$ are the body’s multipole moments.

Because $\nabla ^ { 2 } V = 0$ , the spherical-harmonic components of the driving potential satisfy the homogeneous version of Eq. (2.222),

$$
r ^ { 2 } V _ { \ell m } ^ { \prime \prime } + 2 r V _ { \ell m } ^ { \prime } - \ell ( \ell + 1 ) V _ { \ell m } = 0 .
$$

This equation is satisfied both inside and outside the body, and the only admissible solution is

$$
V _ { \ell m } ( r ) = \frac { 4 \pi } { 2 \ell + 1 } d _ { \ell m } r ^ { \ell } ,
$$

where $d _ { \ell m }$ are the moments of the driving potential; these are readily computed once $V$ is specified.

We now insert the spherical-harmonic decompositions within Eq. (2.214). It is easy to see that the radial component of the equation produces

$$
p _ { \ell m } ^ { \prime } = - \frac { G m } { r ^ { 2 } } \rho _ { \ell m } + \rho ( U _ { \ell m } ^ { \prime } + V _ { \ell m } ^ { \prime } ) ,
$$

where we have used Eq. (2.201) to eliminate $p ^ { \prime }$ . The angular components imply

$$
p _ { \ell m } = \rho \bigl ( U _ { \ell m } + V _ { \ell m } \bigr ) .
$$

When we differentiate this with respect to $r$ and substitute back in the previous equation, we obtain

$$
\frac { G m } { r ^ { 2 } } \rho _ { \ell m } = - \rho ^ { \prime } \big ( U _ { \ell m } + V _ { \ell m } \big ) .
$$

When combined with Eqs. (2.220) and (2.221), the last two equations yield

$$
{ \frac { G m } { r } } f _ { \ell m } = U _ { \ell m } + V _ { \ell m } .
$$

This last equation summarizes the entire content of Euler’s equation for a perturbed equilibrium.

It has become clear that the functions $f _ { \ell m } ( r ) - \mathrm { o r }$ , as we shall see below, their substitutes $\eta _ { \ell } ( r ) -$ determine the entire set of unknowns $\rho _ { \ell m } , p _ { \ell m }$ , and $U _ { \ell m }$ . Our main goal, therefore, is to calculate them for a specified driving potential $V$ . And from $f _ { \ell m } ( r )$ we wish to extract useful information about the deformation, such as the geometrical shape of the deformed surface, and the multipole moments $I _ { \ell m }$ of the deformed mass distribution. Before we explain how $f _ { \ell m }$ is computed and this information extracted, we summarize the results in Box 2.3.

<table><tr><td>Box 2.3</td><td>Clairaut-Radau equation and Love numbers</td></tr><tr><td></td><td>The potential driving the body to a perturbed equilibrium state from an unperturbed equilibrium is 4π V = Utidal + Φ=2 demreYem(0,Φ), = 2l+1</td></tr><tr><td> multipole expansion begins at l = 2.</td><td>lm where the tidal potential is given by Eq. (2.192),and the quadrupole piece of the centrifugal potential is defined by Eq. (2.195).It is assumed that the unperturbed configuration is spherically symmetric,and the</td></tr></table>

The gravitational potential of the deformed body is

$$
U = - \frac { G M } { r } + \sum _ { \ell m } \frac { 4 \pi } { 2 \ell + 1 } \frac { G I _ { \ell m } } { r ^ { \ell + 1 } } Y _ { \ell m } ( \theta , \phi ) ,
$$

where $M$ is the body’s total mass and $I _ { \ell m }$ the multipole moments of the mass distribution. By virtue of the perturbation equations, these are related to the coefficients $d _ { \ell m }$ of the driving potential by

$$
G I _ { \ell m } = 2 k _ { \ell } R ^ { 2 \ell + 1 } d _ { \ell m } ,
$$

where $k _ { \ell }$ are the gravitational Love numbers, which depend on the details of the unperturbed configuration.

The shape of the deformed boundary is described by $r = R + \delta R$ , with

$$
\delta R = \sum _ { \ell m } \frac { 4 \pi } { 2 \ell + 1 } R _ { \ell m } Y _ { \ell m } ( \theta , \phi ) ,
$$

and the perturbation equations imply that the coefficients $R _ { \ell m }$ are related to $d _ { \ell m }$ by

$$
R _ { \ell m } = h _ { \ell } \frac { R ^ { \ell + 2 } } { G M } d _ { \ell m } ,
$$

where $h _ { \ell }$ are the surficial Love numbers, which also depend on the details of the unperturbed configuration.

The compute the Love numbers we require a solution to the Clairaut–Radau equation,

$$
r \eta _ { \ell } ^ { \prime } + \eta _ { \ell } ( \eta _ { \ell } - 1 ) + 6 \mathcal { D } ( \eta _ { \ell } + 1 ) - \ell ( \ell + 1 ) = 0 ,
$$

where a prime indicates differentiation with respect to $r$ , and

$$
\mathcal { D } : = \frac { 4 \pi \rho ( r ) r ^ { 3 } } { 3 m ( r ) }
$$

encodes the relevant information regarding the body’s structure. The differential equation is integrated outward from $r = 0$ , with the boundary condition $\eta _ { \ell } ( r = 0 ) = \ell - 2$ . It proceeds to $r = R$ , and $\eta _ { \ell } ( r = R )$ is computed. The Love numbers are then given by

$$
k _ { \ell } = \frac { \ell + 1 - \eta _ { \ell } ( R ) } { 2 \big [ \ell + \eta _ { \ell } ( R ) \big ] } , \qquad h _ { \ell } = 1 + 2 k _ { \ell } .
$$

# Clairaut’s equation

To determine $f _ { \ell m } ( r )$ we rely on Eq. (2.229), which we insert within Eq. (2.222), taking into account Eq. (2.224). We simplify the expression by making use of Eq. (2.220) and the equation $m ^ { \prime } = 4 \pi r ^ { 2 } \rho$ for the unperturbed mass function. The end result is the second-order differential equation

$$
r ^ { 2 } f _ { \ell m } ^ { \prime \prime } + 6 \mathcal { D } \big ( r f _ { \ell m } ^ { \prime } + f _ { \ell m } \big ) - \ell ( \ell + 1 ) f _ { \ell m } = 0 ,
$$

where

$$
\mathcal { D } ( r ) : = \frac { 4 \pi \rho ( r ) r ^ { 3 } } { 3 m ( r ) } = \frac { \rho ( r ) } { \bar { \rho } ( r ) }
$$

is a function that encodes the relevant details of the unperturbed configuration, contained in $\rho ( r )$ and $m ( r )$ ; ${ \bar { \rho } } : = 3 m ( r ) / ( 4 \pi r ^ { 3 } )$ is the mean density inside a sphere of radius $r$ . This is Clairaut’s equation, named after the French mathematician Alexis Clairaut (1713–1765). The equation is integrated outward from $r = 0$ , and the boundary conditions can be determined by a local analysis near $r = 0$ : because $\mathcal { D } \sim 1$ in the limit, we find that $f _ { \ell m } \sim a _ { \ell m } r ^ { \ell - 2 }$ with $a _ { \ell m }$ an arbitrary constant, and from this it follows that $f _ { \ell m } ^ { \prime } \sim ( \ell - 2 ) a _ { \ell m } r ^ { \ell - 3 }$ . These behaviors indicate that the Clairaut equation is ill-conditioned for numerical integration, and we cast it in a more practical form below. It should be noted that $f _ { \ell m } ( r )$ is determined up to a multiplicative factor $a _ { \ell m }$ , which is fixed by the junction conditions at $r = R$ .

To extract useful information from $f _ { \ell m } ( r )$ we assume specifically that the unperturbed density $\rho ( r )$ goes smoothly to zero at the boundary. We exclude discontinuities to ensure that $\rho _ { \ell m } ( r )$ is non-singular at $r = R$ – refer to Eq. (2.220) – and to ensure that $U _ { \ell m }$ and its first derivative are continuous at $r = R$ – refer to Eq. (2.222). While discontinuities could be accommodated in a more complete treatment of the perturbation equations, we choose to exclude such complications from our discussion; we shall, however, examine the special case of an incompressible fluid below.

We first wish to relate the multipole moments $I _ { \ell m }$ of the deformed mass distribution to the coefficients $d _ { \ell m }$ of the driving potential; we expect a linear relationship mediated by the functions $f _ { \ell m }$ . To find this relation we evaluate Eq. (2.229) at $r = R$ and exploit the continuity of $U _ { \ell m }$ at the boundary to equate it to its external expression of Eq. (2.223). This gives

$$
\frac { G M } { R } f _ { \ell m } ( R ) = \frac { 4 \pi } { 2 \ell + 1 } \bigg [ \frac { G I _ { \ell m } } { R ^ { \ell + 1 } } + d _ { \ell m } R ^ { \ell } \bigg ] .
$$

Repeating the procedure with the first derivative of Eq. (2.229), we also obtain

$$
\frac { G M } { R } \Bigl [ R f _ { \ell m } ^ { \prime } ( R ) - f _ { \ell m } ( R ) \Bigr ] = \frac { 4 \pi } { 2 \ell + 1 } \biggl [ - ( \ell + 1 ) \frac { G I _ { \ell m } } { R ^ { \ell + 1 } } + \ell d _ { \ell m } R ^ { \ell } \biggr ] .
$$

These equations can be solved for $d _ { \ell m }$ and $I _ { \ell m }$ , and we get

$$
d _ { \ell m } = { \frac { G M } { 4 \pi R ^ { \ell + 1 } } } \Big [ R f _ { \ell m } ^ { \prime } ( R ) + \ell f _ { \ell m } ( R ) \Big ]
$$

and

$$
G I _ { \ell m } = - \frac { G M } { 4 \pi } R ^ { \ell } \Bigl [ R f _ { \ell m } ^ { \prime } ( R ) - ( \ell + 1 ) f _ { \ell m } ( R ) \Bigr ] .
$$

These equations provide the desired relationship between $I _ { \ell m }$ and $d _ { \ell m }$ . This is recast in a simpler form below.

We next determine the geometrical figure of the deformed boundary, at which the perturbed pressure $p + \delta p$ goes to zero. The deformed boundary is described mathematically by $r = R + \delta R ( \theta , \phi )$ , and the definition of the displacement vector $\xi ^ { j }$ makes it clear that

$\delta R = \xi ^ { r }$ . From this we find that

$$
\delta R = \sum _ { \ell m } \frac { 4 \pi } { 2 \ell + 1 } R _ { \ell m } Y _ { \ell m } ( \theta , \phi ) ,
$$

with $4 \pi ( 2 \ell + 1 ) ^ { - 1 } R _ { \ell m } : = R f _ { \ell m } ( R )$ . We may express this in terms of $I _ { \ell m }$ and $d _ { \ell m }$ with the help of Eq. (2.232), and because $I _ { \ell m }$ is linearly related to $d _ { \ell m }$ , we conclude that $R _ { \ell m }$ is proportional to $d _ { \ell m }$ , with a coefficient that depends on $f _ { \ell m }$ and its first derivative. This relation is given explicitly below.

# Radau’s equation and Love numbers

Clairaut’s equation (2.230) is independent of the azimuthal number $m$ , and the dependence of the solutions on $m$ must be inherited from the junction conditions at $r = R$ . And indeed, we have seen that $f _ { \ell m } ( r )$ is determined up to a multiplicative factor $a _ { \ell m }$ , and the dependence on $m$ must be contained in this number. These considerations imply that the function

$$
\eta _ { \ell } : = \frac { r f _ { \ell m } ^ { \prime } } { f _ { \ell m } } = \frac { d \ln f _ { \ell m } } { d \ln r } ,
$$

known as Radau’s function, must be independent of $m$ . And as it turns out, this combination of $f _ { \ell m }$ and $f _ { \ell m } ^ { \prime }$ is precisely what is involved in the relation between $I _ { \ell m }$ and $d _ { \ell m }$ . Returning to our previous expressions, we see that the relationship can be expressed as

$$
G I _ { \ell m } = 2 k _ { \ell } R ^ { 2 \ell + 1 } d _ { \ell m } ,
$$

where $k _ { \ell }$ is a dimensionless quantity given by

$$
k _ { \ell } : = { \frac { \ell + 1 - \eta _ { \ell } ( R ) } { 2 \bigl [ \ell + \eta _ { \ell } ( R ) \bigr ] } } .
$$

The key point is that $k _ { \ell }$ is independent of $m$ , and determined by the Radau function, which is itself determined by Eq. (2.230). We see that the relation of Eq. (2.238) is valid for any perturbed equilibrium driven by a potential $V$ characterized by its spherical-harmonic coefficients $d _ { \ell m }$ , and that the details of the body’s composition are encapsulated in the constants $k _ { \ell }$ . These all-important numbers are known as gravitational Love numbers, and they are named after the British geophysicist A.E.H. Love (1863–1940), who introduced them early in the $2 0 \mathrm { { t h } }$ century. The numbers are also known in the astronomical and celestial mechanics literature as “apsidal constants,” because they control the size of tidal and rotational deformations of stars in close binary systems, which lead to observable perturbations in the “line of apsides” (also known as the longitude of pericenter); we describe these perturbations in Sec. 3.4.4. The reader should be warned that our definition of $k _ { \ell }$ is the one adopted by astronomers; geophysicists also use Love numbers to describe gravimeter measurements made on the surface of the Earth, but their definition of $k _ { \ell }$ includes an additional factor of two.

<table><tr><td colspan="8">Table2.3 Gravitational Lovenumbers keforvariouspolytropes characterized bythepolytropic indexnandT=1+1/n. The notation e-pat the end of each number stands for × 10-p.</td></tr><tr><td>l</td><td>n = 1/2</td><td>n = 2/3</td><td>n=1</td><td>n = 3/2</td><td>n=2</td><td>n=3</td><td>n =4</td></tr><tr><td>2</td><td>Γ=3 4.49154e-1</td><td>Γ = 5/2</td><td>Γ=2 2.59909e-1</td><td>Γ = 5/3 1.43279e-1</td><td>Γ = 3/2 7.39384e-2</td><td>Γ = 4/3</td><td>Γ = 5/4</td></tr><tr><td>3</td><td>2.03384e-1</td><td>3.75966e-1 1.64696e-1</td><td>1.06454e-1</td><td>5.28485e-2</td><td>2.43940e-2</td><td>1.44430e-2 3.69989e-3</td><td>1.19488e-3 2.23093e-4</td></tr><tr><td>4</td><td>1.25063e-1</td><td>9.85460e-2</td><td>6.02413e-2</td><td>2.73931e-2</td><td>1.15077e-2</td><td>1.40970e-3</td><td>6.55706e-5</td></tr><tr><td>5</td><td>8.75838e-2</td><td>6.74240e-2</td><td>3.92925e-2</td><td>1.65688e-2</td><td>6.41997e-3</td><td>6.56211e-4</td><td>2.46927e-5</td></tr><tr><td>6</td><td>6.60100e-2</td><td>4.97911e-2</td><td>2.78270e-2</td><td>1.09837e-2</td><td>3.96610e-3</td><td>3.46899e-4</td><td>1.09340e-5</td></tr><tr><td>7</td><td>5.21751e-2</td><td>3.86488e-2</td><td>2.08099e-2</td><td>7.74547e-3</td><td>2.62762e-3</td><td>2.00562e-4</td><td>5.43272e-6</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The relation between $R _ { \ell m }$ and $d _ { \ell m }$ can also be expressed in a similar form. From our previous results it is easy to see that

$$
R _ { \ell m } = h _ { \ell } \frac { R ^ { \ell + 2 } } { G M } d _ { \ell m } ,
$$

where $h _ { \ell }$ is another dimensionless quantity given by

$$
h _ { \ell } = 1 + 2 k _ { \ell } .
$$

These numbers also are independent of $m$ and determined by the Radau function; they are known as surficial Love numbers, and are mostly of interest to geophysicists.

In principle the Radau function can be obtained from $f _ { \ell m }$ after integrating Eq. (2.230). It is more practical, however, to formulate a differential equation directly for $\eta _ { \ell }$ . By inserting Eq. (2.237) within Eq. (2.230) it is easy to see that the equation becomes

$$
r \eta _ { \ell } ^ { \prime } + \eta _ { \ell } ( \eta _ { \ell } - 1 ) + 6 \mathcal { D } ( \eta _ { \ell } + 1 ) - \ell ( \ell + 1 ) = 0 ,
$$

which is known as Radau’s equation. This is a first-order differential equation, but unlike Eq. (2.230) it is non-linear in the dependent variable. Radau’s equation is integrated outward from $r = 0$ with the boundary condition

$$
\eta _ { \ell } ( r = 0 ) = \ell - 2 ,
$$

and the integration proceeds to the boundary, where $\eta _ { \ell } ( r = R )$ is obtained. The computation produces the Love numbers $k _ { \ell }$ and $h _ { \ell }$ , and the deformed equilibrium of the body is completely determined. The function $\eta _ { \ell } ( r )$ and its differential equation are named after the Prussian-French astronomer and mathematician Rodolphe Radau (1835–1911).

In Table 2.3 we present the results of a computation for deformed polytropes. (Refer to Exercise 2.7 for helpful computational details.) We observe that $k _ { \ell }$ decreases as $n$ increases ( $\Gamma$ decreases, so that the equation of state becomes softer), and that this behavior is more pronounced as $\ell$ increases. This reflects the body’s internal structure: when $n$ is large and the equation of state is soft, the body is centrally dense with most of its mass confined to the core, where the factor $r ^ { \ell }$ involved in the definition of the multipole moments is small and getting smaller with increasing . Mathematically, this behavior comes about because $\mathcal { D }$ decreases rapidly to zero when $n$ is large; with $\mathcal { D }$ negligible near the surface, Eq. (2.230) implies that $f _ { \ell m } ( r ) \propto r ^ { \ell + 1 }$ and $\eta _ { \ell } \simeq \ell + 1$ , which produces $k _ { \ell } \simeq 0$ .

We note that when $n = 1$ and $\rho = \rho _ { c } \sin ( \xi ) / \xi$ , where $\xi$ is the dimensionless radial variable introduced in Sec. 2.2.3, Clairaut’s equation can be integrated exactly to give

$$
f _ { \ell m } = \frac { \xi j _ { \ell } ( \xi ) } { \xi \cos \xi - \sin \xi } \qquad ( n = 1 ) ,
$$

where $j _ { \ell }$ is a spherical Bessel function. This analytical result can be used as a check on the numerical computations.

It can be shown, see Exercise 2.9, that the magnitude of the gravitational acceleration of a test mass (for example a gravimeter) on the surface of a deformed body is perturbed from the nominal value $G M / R ^ { 2 }$ by a factor proportional to $[ \ell + 2 h _ { \ell } - 2 ( \ell + 1 ) k _ { \ell } ] d _ { \ell m } .$ The first term is the direct perturbation caused by the perturbing force, the second results from the displacement of the surface from its unperturbed location, and the third comes from the redistribution of the matter and the resulting perturbation of the body’s gravitational field. Similarly, one can calculate the “tilt” of a gravimeter, the angle between the gravitational acceleration and a normal to the body’s surface; this is controlled by the factor $( 1 - h _ { \ell } +$ $2 k _ { \ell } ) d _ { \ell m }$ . For perfect-fluid bodies, the relation $h _ { \ell } = 1 + 2 k _ { \ell }$ implies that the tilt vanishes – the surface is always perpendicular to a plumb line. But for a heterogeneous body like the Earth, with both solid and liquid components, the Love numbers are no longer linked, and gravimeter and tilt measurements can be used to shed light on the nature of the Earth’s interior.

# Uniform density

Our previous developments did not allow for a discontinuity of the unperturbed density $\rho$ at the unperturbed boundary $r = R$ . As an example of a model involving a discontinuous density and requiring a separate treatment, we examine the simplest case of a homogeneous body with density $\rho ( r ) = \rho _ { 0 } \Theta ( R - r )$ , in which $\rho _ { 0 }$ is a constant and $\Theta ( R - r )$ is the Heaviside step function. The body comes with a mass function $m ( r ) = ( 4 \pi / 3 ) \rho _ { 0 } r ^ { 3 }$ and a total mass $M = ( 4 \pi / 3 ) \rho _ { 0 } R ^ { 3 }$ .

From Eq. (2.220) we find that

$$
\rho _ { \ell m } = \rho _ { 0 } R f _ { \ell m } ( R ) \delta ( r - R ) ,
$$

indicating that the density perturbation is supported at the boundary only. The presence of a $\delta$ -function in $\rho _ { \ell m }$ implies that the first derivative of $U _ { \ell m }$ is discontinuous at the boundary, which invalidates many of the manipulations carried out previously. From Eq. (2.222) we indeed find that the junction conditions at $r = R$ are now given by

$$
\left[ U _ { \ell m } \right] = 0 , \qquad \left[ U _ { \ell m } ^ { \prime } \right] = - \frac { 3 G M } { R ^ { 2 } } f _ { \ell m } ( R ) ,
$$

where $[ \psi ] : = \psi ( r = R + \epsilon ) - \psi ( r = R - \epsilon )$ denotes the jump of a function $\psi$ across $r = R$ ( $\epsilon$ is a small, positive constant). Because $\rho _ { \ell m }$ vanishes inside the body, the internal solution to Eq. (2.222) is $4 \pi ( 2 \ell + 1 ) ^ { - 1 } c _ { \ell m } r ^ { \ell }$ for some constants $c _ { \ell m }$ , and the external solution continues to be $4 \pi ( 2 \ell + 1 ) ^ { - 1 } G I _ { \ell m } r ^ { - \ell - 1 }$ . Continuity of $U _ { \ell m }$ at $r = R$ implies that $c _ { \ell m } = G I _ { \ell m } R ^ { - 2 \ell - 1 }$ , and the remaining junction condition yields

$$
G I _ { \ell m } = { \frac { 3 } { 4 \pi } } G M R ^ { \ell } f _ { \ell m } ( R ) ,
$$

which replaces Eq. (2.235).

The link to $d _ { \ell m }$ is provided by Eq. (2.229), which requires no modification in this context because both $U _ { \ell m }$ and $V _ { \ell m }$ are continuous at the boundary. We find that

$$
d _ { \ell m } = \frac { 2 ( \ell - 1 ) } { 3 } \frac { G I _ { \ell m } } { R ^ { 2 \ell + 1 } } ,
$$

and collecting results, we finally obtain the Love numbers of an incompressible fluid:

$$
k _ { \ell } = { \frac { 3 } { 4 ( \ell - 1 ) } } , \qquad h _ { \ell } = { \frac { 2 \ell + 1 } { 2 ( \ell - 1 ) } } .
$$

It is amusing to note that these results can be recovered on the basis of the recipe presented in $\mathrm { B o x } 2 . 3$ , in spite of the fact that the discontinuity at $r = R$ invalidates its usage. Indeed, the uniform-density model implies that $\mathcal { D } = 1$ throughout the body, and in this case the solution to Clairaut’s equation is $f _ { \ell m } \propto r ^ { \ell - 2 }$ , leading to $\eta _ { \ell } = \ell - 2$ . The Love numbers can then be computed by applying the general relations, and the results agree with our previous answers.

# 2.4.5 Rotational deformations

As a first application of the general theory we consider an isolated body subjected to a rigid rotation of angular velocity $\omega$ . We therefore leave $U _ { \mathrm { t i d a l } }$ out of the perturbing potential $V$ , but we include $\Phi _ { \mathrm { C } } ^ { \ell = 2 }$ and seek to determine its effect on a body of arbitrary composition. In Sec. 2.5 we shall apply the general theory to a body subjected to tidal forces.

The perturbing potential is obtained from Eq. (2.195), which we write as

$$
V = \Phi _ { \mathrm { C } } ^ { \ell = 2 } = \frac { 1 } { 6 } \omega ^ { 2 } r ^ { 2 } ( 1 - 3 \cos ^ { 2 } \theta ) = - \frac { 1 } { 3 } \sqrt { \frac { 4 \pi } { 3 } } \omega ^ { 2 } r ^ { 2 } Y _ { 2 0 } ( \theta ) .
$$

The potential is characterized by the single non-vanishing coefficient

$$
d _ { 2 0 } = - \frac 1 3 \sqrt { \frac { 5 } { 4 \pi } } \omega ^ { 2 } ,
$$

and the perturbation is a pure axisymmetric quadrupole. To express our results below it is helpful to introduce a mean density $\bar { \rho }$ defined by $\begin{array} { r } { M : = \frac { 4 \pi } { 3 } \bar { \rho } R ^ { 3 } } \end{array}$ , as well as the parameter

$$
\zeta : = \frac { 2 \omega ^ { 2 } R ^ { 3 } } { 3 G M } = \frac { \omega ^ { 2 } } { 2 \pi G \bar { \rho } } ,
$$

which is a dimensionless measure of the rotational deformation.

According to Eq. (2.238), the quadrupole moment of the rotating body is

$$
G I _ { 2 0 } = - \frac { 2 } { 3 } \sqrt { \frac { 5 } { 4 \pi } } k _ { 2 } \omega ^ { 2 } R ^ { 5 } ,
$$

and this leads to a dimensionless quadrupole moment $J _ { 2 } : = - \sqrt { 4 \pi / 5 } I _ { 2 0 } / ( M R ^ { 2 } )$ given by

$$
J _ { 2 } = k _ { 2 } \zeta .
$$

According now to Eqs. (2.236) and (2.240), the deformation of the boundary is described by $\delta R = ( 4 \pi / 5 ) h _ { 2 } ( R ^ { 4 } / G M ) d _ { 2 0 } Y _ { 2 0 }$ , or

$$
\delta R = \frac { 1 } { 4 } h _ { 2 } \zeta R ( 1 - 3 \cos ^ { 2 } \theta ) .
$$

This allows us to define an equatorial radius

$$
\begin{array} { r } { a : = R + \delta R \left( \theta = \frac { \pi } { 2 } \right) = R \left( 1 + \frac { 1 } { 4 } h _ { 2 } \zeta \right) , } \end{array}
$$

and a polar radius

$$
a _ { 3 } : = R + \delta R ( \theta = 0 ) = R \left( 1 - \frac { 1 } { 2 } h _ { 2 } \zeta \right) ,
$$

and to express the equation describing the surface, to first order in $\zeta$ , as

$$
\frac { 1 } { ( R + \delta R ) ^ { 2 } } = \frac { \sin ^ { 2 } \theta } { a ^ { 2 } } + \frac { \cos ^ { 2 } \theta } { a _ { 3 } ^ { 2 } } \cdot
$$

Comparing with Eq. (2.186), we see that this is the equation of a spheroid. We conclude that to first order in perturbation theory, any rotationally deformed body assumes the shape of a spheroid.

The equatorial and polar radii give rise to an eccentricity given by

$$
e ^ { 2 } : = 1 - \frac { a _ { 3 } ^ { 2 } } { a ^ { 2 } } = \frac { 3 } { 2 } h _ { 2 } \zeta ,
$$

and the relation between the quadrupole moment and the eccentricity is then

$$
J _ { 2 } = \frac { 2 k _ { 2 } } { 3 h _ { 2 } } e ^ { 2 } .
$$

For a body of uniform density, $\begin{array} { r } { k _ { 2 } = \frac { 3 } { 4 } } \end{array}$ and $\begin{array} { r } { h _ { 2 } = \frac { 5 } { 2 } } \end{array}$ , and these relations become $\textstyle \zeta = { \frac { 4 } { 1 5 } } e ^ { 2 }$ and $\begin{array} { r } { J _ { 2 } = \frac { 1 } { 5 } e ^ { 2 } } \end{array}$ . Comparing with Eqs. (2.187) and (2.188d), we see that these results agree with those obtained previously for a Maclaurin spheroid of small eccentricity.

# 2.5 Tidally deformed bodies

Anybody who has spent time at the sea shore has experienced tides. In some parts of the world, such as the Bay of Fundy in Canada or the mouth of the River Severn in England, they are spectacular. In other areas the tides are barely noticeable. Tides are caused by inhomogeneities in the gravitational attraction of the Moon and Sun on the Earth. To lowest order, all parts of the Earth fall toward the Moon with the same acceleration; but the acceleration of a point on the side closest to the Moon is larger than that of a point at the center of the Earth, and this acceleration is itself larger than that of a point on the surface opposite to the Moon. Furthermore, points on the sides of the Earth perpendicular to the direction to the Moon have a small component of their acceleration toward the center of the Earth. As a result the tidal deformation has a characteristic quadrupolar shape, leading to the twice-per-day phenomenon of ocean tides. The solar tide is a little less than half as strong as the lunar tide. Depending on the relative position of the Sun and Moon in the sky, the tidal amplitudes vary from the large “spring tide” to the smaller “neap tide.”

The ocean tides are very complex, because they depend not only on the gravitational attraction of the Sun and Moon, but also on the interaction between the water and the continental shelf where we landlubbers observe them. Less noticeable in daily life, but equally important, are the “solid” Earth tides, the tidal deformations of the full Earth. These are measured and analyzed to high precision using gravimeters, which measure time variations of $g$ , the acceleration at the surface of the Earth. Measurements such as these are used to determine the Earth’s gravitational Love numbers $k _ { \ell }$ , which reveal information regarding its internal structure.

Tidal interactions are also important in many close binary-star systems. The modification to each star’s gravitational potential caused by the tidal deformation leads to observable perturbations in the orbital motion, to be described in Chapter 3. These can be exploited to learn something about the stellar interiors through the inferred values of $k _ { \ell }$ .

Tidal deformations can lead to heating and dissipation of angular momentum. In the Jovian system, tidal heating is responsible for the spectacular volcanic activity observed on Io’s surface, which far exceeds in intensity the activity seen on Earth. In the Earth–Moon system, tidal torquing is responsible for the facts that the Moon is receding from the Earth and that the length of the day is slowly increasing. Interestingly, it was Immanuel Kant (1724–1804) who first suggested that this might be the case, long before the effect could be measured. He reasoned that the Moon presents the same face to the Earth because its rotation has slowed down by virtue of tidal dissipation, and that therefore the same must be happening to the Earth. Eventually, the two bodies will become tidally locked, rotating and revolving with the same angular velocity, and with the same side facing each other in perpetuity. If the Earth is still populated with sentient beings when this occurs, then half of them will never have the privilege of observing the clair de lune.

In this section we explore the physics of tides on a fluid body. We first examine static tides in Sec. 2.5.1, in which the external tidal field varies so slowly that it never takes the body out of hydrostatic equilibrium. The tools required to describe such tides were fashioned in Sec. 2.4, and this will be our second application of the general theory of deformed bodies. In Sec. 2.5.2 we incorporate viscous dissipation in our discussion of static tides, and reveal some of its most important consequences. We conclude with an exploration of dynamical tides in Sec. 2.5.3; here the tidal field varies so rapidly that it forces the body out of its equilibrium state. This is a vast domain of study, and our discussion will be limited to a very simplified model involving a body of uniform density.

# 2.5.1 Static tides

As a second application of the general theory of deformed bodies developed in Sec. 2.4, we consider a rotating or non-rotating body subjected to a tidal field created by one or more external bodies. We ignore the body’s rotational deformation, which was treated separately in Sec. 2.4.5, and focus on the tidal deformation. We therefore leave $\Phi _ { \mathrm { C } } ^ { \ell = 2 }$ out of the perturbing potential $V$ , include $U _ { \mathrm { t i d a l } }$ , and seek to determine its effect on a body of arbitrary composition.

The tidal potential was first introduced in Sec. 2.1, where it was denoted $U _ { \neg A } ^ { \mathrm { e f f } }$ , and a simplified expression valid for a body with small multipole moments $I _ { A } ^ { \langle L \rangle }$ was first written down in Eq. (2.11) on page 66. Working in the body’s rotating frame, we copy this here as

$$
V = U _ { \mathrm { t i d a l } } = - \sum _ { \ell = 2 } ^ { \infty } { \frac { 1 } { \ell ! } } \mathcal { E } _ { L } ( t ) x ^ { L } ,
$$

in which the tidal moments $\mathcal { E } _ { L } ( t )$ are time-dependent STF tensors that serve to specify the tidal environment. They are defined by

$$
\mathcal { E } _ { L } ( t ) : = - \partial _ { L } U _ { \neg A } ( t , \mathbf { 0 } ) ,
$$

in which the gravitational potential $U _ { \neg A }$ created by the external bodies is differentiated $\ell$ times with respect to $x ^ { j }$ and the result evaluated at the body’s center-of-mass $\mathbf { \nabla } _ { \mathbf { \boldsymbol { x } } } = \mathbf { \boldsymbol { 0 } }$ . The tidal moments depend on time, but as was discussed near the end of Sec. 2.4.1, this dependence is assumed to be sufficiently slow that the tidal field is never able to the take the body out of hydrostatic equilibrium. This assumption will be relaxed in Sec. 2.5.3.

The tidal potential is naturally expressed as an expansion in STF tensors, but the general theory of Sec. 2.4 relies on an expansion in spherical harmonics. The translational tools were developed in Sec. 1.5.3, where we showed that the STF product $n ^ { \langle L \rangle }$ , with ${ \pmb n } : = { \pmb x } / r$ denoting a unit vector in the direction of $\boldsymbol { x }$ , can be expressed as

$$
n ^ { \langle L \rangle } = \frac { 4 \pi \ell ! } { ( 2 \ell + 1 ) ! ! } \sum _ { m = - \ell } ^ { \ell } \mathcal { I } _ { \ell m } ^ { \langle L \rangle } \mathcal { Y } _ { \ell m } ( \theta , \phi )
$$

in terms of spherical harmonics, with $\mathcal { V } _ { \ell m } ^ { \langle L \rangle }$ the constant STF tensor defined by

$$
\mathcal { V } _ { \ell m } ( \theta , \phi ) = \mathcal { V } _ { \ell m } ^ { * { ( L ) } } n _ { \langle L \rangle } ,
$$

an expansion of the spherical-harmonic functions in STF tensors; the asterisk indicates complex conjugation. Inserting $x ^ { L } = r ^ { \ell } n ^ { L }$ within Eq. (2.261) and making use of the sphericalharmonic decomposition of $n ^ { \langle L \rangle }$ , we quickly find that the coefficients $d _ { \ell m }$ involved in the decomposition of the perturbing potential, as defined by Eq. (2.225), are given by

$$
d _ { \ell m } = - \frac { 1 } { ( 2 \ell - 1 ) ! ! } \mathcal { Y } _ { \ell m } ^ { \langle L \rangle } \mathcal { E } _ { L } .
$$

A few steps of algebra next reveal that

$$
\mathcal { E } _ { L } = - \frac { 4 \pi \ell ! } { 2 \ell + 1 } \sum _ { m = - \ell } ^ { \ell } d _ { \ell m } \mathcal { Y } _ { \ell m } ^ { * \langle L \rangle }
$$

is the inverse relation.

According to Eq. (2.238), the tidal field deforms the body so as to create the multipole moments $G I _ { \ell m } = 2 k _ { \ell } R ^ { 2 \ell + 1 } d _ { \ell m }$ . We wish to express this in STF form, and the required

translation was worked out in Sec. 1.5.3 – refer to Eq. (1.168). Collecting results, we find that the STF multipole moments of a body deformed by an external tidal field are given by

$$
G I _ { \langle L \rangle } = - { \frac { 2 k _ { \ell } } { ( 2 \ell - 1 ) ! ! } } R ^ { 2 \ell + 1 } { \mathcal E } _ { L } ,
$$

in which $k _ { \ell }$ are the body’s gravitational Love numbers. This expression can be inserted within the general multipole expansion of the body’s potential, which is displayed in Eq. (1.157). We find

$$
U = { \frac { G M } { r } } - \sum _ { \ell = 2 } ^ { \infty } { \frac { 2 k _ { \ell } } { \ell ! } } { \frac { R ^ { 2 \ell + 1 } } { r ^ { \ell + 1 } } } { \mathcal { E } } _ { L } n ^ { L } ,
$$

and the total gravitational potential is

$$
U + U _ { \mathrm { t i d a l } } = \frac { G M } { r } - \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } \Big [ 1 + 2 k _ { \ell } \big ( R / r \big ) ^ { 2 \ell + 1 } \Big ] \mathcal { E } _ { L } x ^ { L } .
$$

This expression leaves out a term $g _ { j } x ^ { j }$ , where $g _ { j } : = \partial _ { j } U _ { \neg A } ( \mathbf { 0 } )$ is the body’s acceleration in the field of the external bodies; as we saw back in Sec. 2.1, this term plays no role because it is cancelled out by a fictional force originating from the translation to the body’s moving frame. Focusing on the tidal terms, we see that the total perturbation at $r = R$ is given by a contribution proportional to $( 1 + 2 k _ { \ell } ) \mathcal { E } _ { L } n ^ { L }$ from each tidal moment; the first unit of $\mathcal { E } _ { L } n ^ { L }$ is the direct contribution from the tidal field, and the remaining $2 k _ { \ell }$ units come from the body’s response to the applied tidal field.

The body’s deformed surface is described by Eq. (2.236), in which we insert Eqs. (2.240) and (2.265). After conversion to an expansion in STF tensors, we find that the surface of a body deformed by tidal forces is described by $r = R + \delta R$ with

$$
\delta R = - \sum _ { \ell = 2 } ^ { \infty } \frac { 1 } { \ell ! } h _ { \ell } \frac { R ^ { \ell + 2 } } { G M } { \mathcal E } _ { L } n ^ { L } ,
$$

where $h _ { \ell }$ are the surficial Love numbers.

In many circumstances it is sufficient to keep only the leading, quadrupole term in the expansions of Eqs. (2.268) and (2.270). Truncating all expressions at $\ell = 2$ , we find that the tidal potential simplifies to

$$
U _ { \mathrm { t i d a l } } = - \frac { 1 } { 2 } \mathcal { E } _ { j k } ( t ) x ^ { j } x ^ { k } ,
$$

in which $\mathcal { E } _ { j k } ( t )$ is the tidal quadrupole moment. The body’s quadrupole moment is then

$$
G I _ { \langle j k \rangle } = - \frac { 2 } { 3 } k _ { 2 } R ^ { 5 } { \mathcal E } _ { j k } ,
$$

and its potential simplifies to

$$
U = { \frac { G M } { r } } - k _ { 2 } { \frac { R ^ { 5 } } { r ^ { 3 } } } { \mathcal E } _ { j k } n ^ { j } n ^ { k } .
$$

In this truncated description the surface deformation becomes

$$
\delta R = - \frac { 1 } { 2 } h _ { 2 } \frac { R ^ { 4 } } { G M } \mathcal { E } _ { j k } n ^ { j } n ^ { k } .
$$

When the body is a member of an $N$ -body system, the tidal field is supplied by the remaining $N - 1$ bodies, and in this case the tidal quadrupole moment is given by

$$
\begin{array} { l } { { \displaystyle \mathcal E _ { j k } = - \sum _ { B \neq A } G m _ { B } \partial _ { j k } ^ { A } \frac { 1 } { r _ { A B } } } } \\ { { \displaystyle \quad = - 3 \sum _ { B \neq A } \frac { G m _ { B } } { r _ { A B } ^ { 3 } } n _ { A B } ^ { \langle j k \rangle } } } \\ { { \displaystyle \quad = - \sum _ { B \neq A } \frac { G m _ { B } } { r _ { A B } ^ { 3 } } \left( 3 n _ { A B } ^ { j } n _ { A B } ^ { k } - \delta ^ { j k } \right) , } } \end{array}
$$

in which $r _ { A B } : = | \pmb { r } _ { A B } | = | \pmb { r } _ { A } - \pmb { r } _ { B } |$ is the distance between body $A$ and body $B$ , and $\pmb { n } _ { A B } : = \pmb { r } _ { A B } / r _ { A B }$ is a unit vector pointing from body $B$ to body $A$ . To arrive at this expression for $\mathcal { E } _ { j k }$ we assume that the multipole moments $I _ { B } ^ { \langle L \rangle }$ of the external bodies are small, so that they need not be included in the expression for the external potential. We have reverted to the notation of Sec. 1.6, in which the mass of body $B$ is denoted $m _ { B }$ instead of $M _ { B }$ . Similarly, the mass of body $A$ will be denoted $m _ { A }$ instead of $M _ { A }$ .

As a concrete example, imagine that our body is non-rotating, and that it is the first member of a two-body system on a circular orbit of radius $r : = r _ { 1 2 }$ and angular velocity $\Omega =$ $\sqrt { G m / r ^ { 3 } }$ , in which $m = m _ { 1 } + m _ { 2 }$ . Taking the $x - y$ plane to coincide with the orbital plane, we have that $\pmb { n } _ { 1 2 } = [ \cos \Omega t , \sin \Omega t , 0 ]$ , and we write $\pmb { n } = [ \sin \theta \cos \phi$ , sin θ sin φ, cos θ ]. With this we find that

$$
\mathscr { E } _ { j k } n ^ { j } n ^ { k } = - 3 \frac { G m _ { 2 } } { r ^ { 3 } } \bigg [ \sin ^ { 2 } \theta \cos ^ { 2 } ( \phi - \Omega t ) - \frac { 1 } { 3 } \bigg ] .
$$

We see that the tidal field is proportional to $G m _ { 2 } / r ^ { 3 }$ , and by virtue of its dependence on $\begin{array} { r } { \cos ^ { 2 } ( \phi - \Omega t ) = \frac { 1 } { 2 } + \frac { 1 } { 2 } \cos 2 ( \phi - \Omega t ) } \end{array}$ , we see that it oscillates at twice the orbital frequency $\Omega$ . The peak position of the tidal bulge is obtained when the argument of the cosine function vanishes, and we find that $\phi _ { \mathrm { b u l g e } } = \Omega t$ ; the bulge is at all times aligned with the orbiting body.

# 2.5.2 Tidal dissipation

Our discussion of static tides was based on an assumption that the body is adequately modeled as a perfect fluid of mass density $\rho$ and pressure $p$ . For many applications this model is indeed adequate, but in some aspects it is deficient, and the deficiency is somewhat severe in the context of tidal dynamics. What is missing from a perfect-fluid model is a mechanism to dissipate energy, and in this section we attempt to incorporate this important effect in the physics of tides.

The simplest way to include a dissipative mechanism in fluid mechanics is to let the fluid be a viscous fluid, and to add the (kinematic) viscosity $\nu$ to the list of fluid variables, along with $\rho$ and $p$ . This is defined in such a way that the frictional force on a fluid element is given by the kinematic viscosity multiplied by the mass density multiplied by the element’s cross-sectional area multiplied by the velocity gradient across the fluid element; the unit of $\nu$ is then $\mathrm { m } ^ { 2 } / \mathrm { s }$ . The inclusion of viscosity in the fluid dynamics requires a modification of Euler’s equation, which is generalized to the famous Navier–Stokes equation. It would take us much too far afield to formulate a perturbation theory based on the Navier–Stokes equation, and to find solutions that describe a tidally deformed body. Such developments are beyond the scope of this book, and we shall instead be satisfied with displaying the final outcome of this analysis. We provide no proof, but attempt to motivate the answer by appealing to an analogous physical system (see Box 2.4).

# Box 2.4

# Driven harmonic oscillator

s we shall see in Sec. 2.5.3, the physics of tidal deformations is closely analogous to the physics of a simple armonic oscillator driven by an external force. In this analogy, the oscillator’s position $x$ from equilibrium lays the role of the tidal deformation (as measured by the mass quadrupole moment $I _ { \langle j k \rangle }$ ), and the external rce $f$ plays the role of the applied tidal field (as measured by the tidal quadrupole moment $\mathcal { E } _ { j k } \mathrm { . }$ ).

In the absence of damping, the oscillator’s response to the external force is governed by

$$
\ddot { x } + \omega ^ { 2 } x = f ,
$$

in which an overdot indicates differentiation with respect to $t$ , and $\omega$ is the oscillator’s natural frequency. We assume that the internal time scale $T _ { \mathrm { i n t } } : = \omega ^ { - 1 }$ is very short compared with the external time scale $T _ { \mathrm { e x t } }$ associated with the behavior of the external force. The general solution to this equation is

$$
x ( t ) = x ( 0 ) \cos \omega t + { \frac { 1 } { \omega } } { \dot { x } } ( 0 ) \sin \omega t + { \frac { 1 } { \omega } } \int _ { 0 } ^ { t } f ( t ^ { \prime } ) \sin \omega ( t - t ^ { \prime } ) d t ^ { \prime } ,
$$

and repeated integration by parts turns this expression into

$$
\begin{array} { l } { { \displaystyle x ( t ) = \biggl [ x ( 0 ) - \frac { 1 } { \omega ^ { 2 } } f ( 0 ) + \cdot \cdot \cdot \biggr ] \cos \omega t + \frac { 1 } { \omega } \biggl [ \dot { x } ( 0 ) - \frac { 1 } { \omega ^ { 2 } } \dot { f } ( 0 ) + \cdot \cdot \cdot \biggr ] \sin \omega t } } \\ { { \displaystyle ~ + \frac { 1 } { \omega ^ { 2 } } \bigl [ f ( t ) + \cdot \cdot \cdot \bigr ] , } } \end{array}
$$

in which the neglected terms are smaller than the leading terms by a factor of order $( T _ { \mathrm { i n t } } / T _ { \mathrm { e x t } } ) ^ { 2 } \ll 1$ . Averaging over the oscillations to keep track of the long-term motion, we arrive at

$$
\langle x ( t ) \rangle = \frac { 1 } { \omega ^ { 2 } } \big [ f ( t ) + \cdot \cdot \cdot \big ] ,
$$

and this result is analogous to Eq. (2.272).

We next incorporate dissipation in the oscillator’s response by inserting a damping term in the differential equation, which now reads

$$
\begin{array} { r } { \ddot { x } + 2 \zeta \omega \dot { x } + \omega ^ { 2 } x = f , } \end{array}
$$