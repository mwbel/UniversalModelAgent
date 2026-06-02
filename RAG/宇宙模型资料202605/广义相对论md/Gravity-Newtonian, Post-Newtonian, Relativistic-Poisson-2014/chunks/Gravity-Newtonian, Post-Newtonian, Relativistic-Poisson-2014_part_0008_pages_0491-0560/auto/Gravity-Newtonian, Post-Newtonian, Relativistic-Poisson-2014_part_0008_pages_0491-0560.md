# 9.6.1 Energy-momentum tensor

The description of a point particle moving in a curved spacetime was developed in Sec. 5.3.4. The particle has a mass $m$ , it moves on a world line described by the parametric relations $r ^ { \alpha } ( \tau )$ , and its velocity four-vector is $u ^ { \alpha } = d r ^ { \alpha } / d \tau ; \tau$ $\tau$ is proper time on the particle’s world line. Its energy-momentum tensor was displayed in Eq. (5.108); it is

$$
T ^ { \alpha \beta } = m c \int u ^ { \alpha } u ^ { \beta } { \frac { \delta { \bigl ( } x ^ { \mu } - r ^ { \mu } ( \tau ) { \bigr ) } } { \sqrt { - g } } } d \tau .
$$

This expression can be simplified if we change the variable of integration from $\tau$ to $r ^ { 0 } ( \tau )$ . This permits an integration over the delta function $\delta ( x ^ { 0 } - r ^ { 0 } )$ , and we obtain

$$
T ^ { \alpha \beta } = \frac { m u ^ { \alpha } u ^ { \beta } } { \gamma \sqrt { - g } } \delta \bigl ( { \pmb x } - { \pmb r } ( t ) \bigr ) ,
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

where $\rho ^ { * }$ stands for $\rho ^ { * } ( t , \boldsymbol { x } )$ , while $\rho ^ { * \prime }$ stands for $\rho ^ { * } ( t , x ^ { \prime } )$ . The integral involves a product of delta functions, and its value is mathematically ill-defined. It is not clear, therefore, that $\Omega _ { A }$ can be set equal to zero. To explore this we substitute $m _ { A } \delta ( { \pmb x } - { \pmb r } _ { A } )$ for $\rho ^ { * }$ , $m _ { A } \delta ( { \pmb x } ^ { \prime } - { \pmb r } _ { A } )$ for $\rho ^ { * \prime }$ , and we integrate with respect to $d ^ { 3 } x ^ { \prime }$ ; the result is

$$
\Omega _ { A } = - \frac 1 2 G m _ { A } ^ { 2 } \int _ { A } \frac { \delta ( { \pmb x } - { \pmb r } _ { A } ) } { | { \pmb x } - { \pmb r } _ { A } | } d ^ { 3 } x ,
$$

and we see why the integral is ill-defined: the quantity $\delta ( \pmb { x } - \pmb { r } _ { A } ) / | \pmb { x } - \pmb { r } _ { A } |$ is not defined as a distribution, and a blind evaluation would return $1 / 0$ . This mathematical difficulty illustrates rather well the spectacular failure of the point particle to provide a sensible model for an extended body in general relativity; the non-linearity of the field equations simply won’t allow it.

All is not lost, however. We can reconcile the diverging values for $\Omega _ { A }$ if we introduce the seemingly nonsensical regularization prescription

$$
\frac { \delta ( \pmb { x } - \pmb { r } _ { A } ) } { | \pmb { x } - \pmb { r } _ { A } | } \equiv 0 .
$$

With this rule the integral becomes well-defined, and we arrive at the desired result, $\Omega _ { \cal A } = 0$ . As we shall see, the regularization prescription is the only additional rule that is required to make sense of all the ill-defined integrals that we shall encounter; and with this prescription we shall be able to recover the metric of Eq. (9.81) on the basis of the point-particle model.

The regularization prescription of Eq. (9.264) is a special case of a more powerful method known as Hadamard regularization, which was used to great benefit by our friends Luc Blanchet and Thibault Damour in their work (along with their collaborators) on high-order post-Newtonian theory. The method works as follows.

Let $F ( x ; r )$ be a function of $\boldsymbol { x }$ that diverges when $\boldsymbol { x }$ approaches the point $r$ . Specifically, assume that its behavior near $x = r$ is given by the Laurent series

$$
F ( \pmb { x } ; \pmb { r } ) = \sum _ { n = 0 } ^ { n _ { \operatorname* { m a x } } } s ^ { - n } f _ { n } ( \pmb { n } ; \pmb { r } ) + O ( s ) ,
$$

where $s : = x - r , s : = | x - r |$ , and $\pmb { n } : = \pmb { s } / s$ . The function therefore diverges as $s ^ { - n _ { \operatorname* { m a x } } }$ when $x  r$ , and it clearly does not have a well-defined value at $x = r$ . We regularize it by extracting its partie finie at the singular point $x = r$ . This is defined by

$$
\lfloor F \rfloor ( \pmb { r } ) : = \frac { 1 } { 4 \pi } \int f _ { 0 } ( \pmb { n } ; \pmb { r } ) d \Omega ( \pmb { n } ) ,
$$

in which $d \Omega ( n )$ is an element of solid angle in the direction of the unit vector $\pmb { n }$ . Thus, the partie finie of $F$ is the angular average of the zeroth term $f _ { 0 } ( \pmb { n } ; \pmb { r } )$ in its Laurent series. The partie finie can be used to make sense of the product of $F$ with the delta function $\delta ( x - r )$ : We declare that

$$
F ( { \pmb x } ; { \pmb r } ) \delta ( { \pmb x } - { \pmb r } ) \equiv \lfloor F \rfloor ( { \pmb r } ) \delta ( { \pmb x } - { \pmb r } ) .
$$

It follows immediately from this rule that $\begin{array} { r } { \int F ( { \pmb x } ; { \pmb r } ) \delta ( { \pmb x } - { \pmb r } ) d ^ { 3 } x = \lfloor F \rfloor ( { \pmb r } ) . } \end{array}$

We now see that Eq. (9.264) is indeed a special case of Hadamard regularization. In this case $\boldsymbol { F } = | \boldsymbol { x } - \boldsymbol { r } | ^ { - 1 }$ , and its partie finie vanishes; Eq. (9.267) then implies $\delta ( x - r ) / | x -$ $r | \equiv 0$ . Hadamard regularization even allows us to generalize the rule to $\delta ( x - r ) / | x -$ $r | ^ { n } \equiv 0$ for any positive integer $n$ .

# 9.6.3 Potentials

The gravitational potentials are computed by substituting Eqs. (9.260) and (9.261) into the Poisson integrals of Eqs. (8.4). We immediately obtain

$$
\begin{array} { l } { { \displaystyle U = \sum _ { A } \frac { G M _ { A } } { s _ { A } } , } } \\ { { \displaystyle U ^ { j } = \sum _ { A } \frac { G M _ { A } v _ { A } ^ { j } } { s _ { A } } , } } \\ { { \displaystyle X = \sum _ { A } G M _ { A } s _ { A } , } } \end{array}
$$

where $s _ { A }$ is the length of the vector $\mathbf { \delta } _ { S _ { A } } : = \mathbf { \delta } _ { \mathbf { X } } - \mathbf { \delta } \mathbf { \vec { r } } _ { A } ( t )$ , and we have used the fact that since $\mathcal { T } _ { A } = \Omega _ { A } = E _ { A } ^ { \mathrm { i n t } } = 0$ , the total mass-energy $M _ { A }$ of a point particle is equal to its material mass $m _ { A }$ .

The potential $\psi$ requires more work. The starting point is

$$
\psi = G \int { \frac { \rho ^ { * \prime } { \bigl ( } { \frac { 3 } { 2 } } v ^ { \prime 2 } - U ^ { \prime } { \bigr ) } } { | \mathbf { x } - \mathbf { x } ^ { \prime } | } } d ^ { 3 } x ^ { \prime } ,
$$

and we decompose the Newtonian potential as $U ^ { \prime } = U _ { A } ^ { \prime } + U _ { \lnot A } ^ { \prime }$ , where $U _ { A } ^ { \prime } = G M _ { A } / s _ { A } ^ { \prime }$ and $\begin{array} { r } { U _ { \neg A } ^ { \prime } = \sum _ { B \not = A } G M _ { B } / s _ { B } ^ { \prime } } \end{array}$ , with $s _ { A } ^ { \prime } : = | \pmb { x } ^ { \prime } - \pmb { r } _ { A } ( t ) |$ . The integral involving $U _ { A } ^ { \prime }$ is

$$
- \sum _ { A } G ^ { 2 } M _ { A } ^ { 2 } \int { \frac { \delta ( { \pmb x } ^ { \prime } - { \pmb r } _ { A } ) } { | { \pmb x } ^ { \prime } - { \pmb r } _ { A } | } } { \frac { 1 } { | { \pmb x } - { \pmb x } ^ { \prime } | } } d ^ { 3 } x ^ { \prime } ,
$$

and this is ill-defined. The regularization prescription of Eq. (9.264), however, dictates that the integral vanishes. The remaining piece of $\psi$ is

$$
\sum _ { A } \frac { G M _ { A } } { s _ { A } } \biggl [ \frac { 3 } { 2 } v _ { A } ^ { 2 } - U _ { \lnot A } ( \pmb { r } _ { A } ) \biggr ] ,
$$

and we arrive at

$$
\psi = \frac { 3 } { 2 } \sum _ { A } \frac { G M _ { A } v _ { A } ^ { 2 } } { s _ { A } } - \sum _ { A } \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { s _ { A } r _ { A B } } ,
$$

where $r _ { A B }$ is the length of the vector $\pmb { r } _ { A B } : = \pmb { r } _ { A } ( t ) - \pmb { r } _ { B } ( t )$ .

According to Eq. (8.3), the post-Newtonian potential is $\begin{array} { r } { \Psi = \psi + \frac 1 2 \partial _ { t t } { X } . } \end{array}$ . Differentiation of the superpotential yields

$$
\partial _ { t t } X = \sum _ { A } \frac { G M _ { A } } { s _ { A } } \Big [ v _ { A } ^ { 2 } - ( \pmb { n } _ { A } \cdot \pmb { v } _ { A } ) ^ { 2 } \Big ] - \sum _ { A } G M _ { A } \pmb { n } _ { A } \cdot \pmb { a } _ { A } ,
$$

where $\pmb { n } _ { A } : = \pmb { s } _ { A } / s _ { A }$ . To evaluate this fully we need an expression for $\pmb { a } _ { A }$ , the acceleration of particle $A$ . For our purposes here it suffices to use the Newtonian expression $\textstyle - \sum _ { B \neq A } G M _ { B } { \pmb { n } } _ { A B } / r _ { A B } ^ { 2 }$ , where $\pmb { n } _ { A B } : = \pmb { r } _ { A B } / r _ { A B } .$ . This yields

$$
\partial _ { t t } X = \sum _ { A } \frac { G M _ { A } } { s _ { A } } \Big [ v _ { A } ^ { 2 } - ( \pmb { n } _ { A } \cdot \pmb { v } _ { A } ) ^ { 2 } \Big ] + \sum _ { A } \sum _ { B \neq A } \frac { G ^ { 2 } M _ { A } M _ { B } ( \pmb { n } _ { A B } \cdot \pmb { n } _ { A } ) } { r _ { A B } ^ { 2 } } .
$$

Collecting results, the post-Newtonian potential is

$$
\Psi = \sum _ { A } \frac { G M _ { A } } { s _ { A } } \biggl [ 2 v _ { A } ^ { 2 } - \frac { 1 } { 2 } ( \pmb { n } _ { A } \cdot \pmb { v } _ { A } ) ^ { 2 } \biggr ] - \sum _ { A } \sum _ { B \neq A } \frac { G ^ { 2 } M _ { A } M _ { B } } { r _ { A B } s _ { A } } \biggl ( 1 - \frac { \pmb { n } _ { A B } \cdot \pmb { s } _ { A } } { 2 r _ { A B } } \biggr ) .
$$

Our expressions for $U , U ^ { j }$ , and $\Psi$ agree with Eqs. (9.55), (9.58), and (9.80), respectively, and we recover the inter-body metric of Eqs. (9.81). It should be evident that the computations carried out here were far less tedious than those presented in Sec. 9.2. The point-particle model, in spite of its mathematical difficulties and the need to regularize divergent integrals, has clear merits.

# 9.7 Bibliographical notes

The post-Newtonian equations of motion derived in Sec. 9.3 were first obtained by Lorentz and Droste (1917). A version of the equations, containing an error, was obtained independently by de Sitter (1916); the mistake was eventually corrected by Eddington and Clark (1938). A definitive treatment of the problem of motion was provided by Einstein, Infeld, and Hoffmann (1938), and the history of this fascinating episode in the development of general relativity is related in Havas (1989). Another fine survey of the “problem of motion” in Einstein’s theory is Damour (1987). The method of derivation adopted in Sec. 9.3 is adapted from Will (1993).

The alternative method employed in Sec. 9.4 to derive equations of motion for compact bodies originates in the work of Demianski and Grishchuk (1974), D’Eath (1975), and Damour (1983). The method was developed systematically in Damour, Soffel, and Xu (1992), and generalized to bodies of arbitrary shape and composition by Racine and Flanagan (2005). The particular approach adopted in Sec. 9.4 is adapted from Taylor and Poisson (2008).

The motion of spinning bodies in curved spacetime has a long history, which is also summarized in Havas (1989). The equations of motion were first derived on the basis of point-particle models by Mathisson (1937) and Papapetrou (1951), and the importance of imposing a “spin supplementary condition” was stressed by Barker and O’Connell (1974). Derivations making use of extended bodies were provided later, and our methods in Sec. 9.5 are based on Kidder (1995) and Will (2005). An elegant alternative method was devised by Damour, Soffel, and Xu (1993).

The mathematical theory of Hadamard regularization, touched upon very briefly in Sec. 9.6, is developed fully in Sellier (1994) and Blanchet and Faye (2000).

# 9.8 Exercises

9.1 Verify all the results listed in Eqs. (9.91).

9.2 Verify all the results listed in Eqs. (9.103).

9.3 Show that the post-Newtonian equations of motion for a system of $N$ bodies can be derived from the Lagrangian

$$
\begin{array} { l } { { \displaystyle { { \cal L } = - \sum _ { A } M _ { A } c ^ { 2 } \biggl [ 1 - \frac { 1 } { 2 } ( v _ { A } / c ) ^ { 2 } - \frac { 1 } { 8 } ( v _ { A } / c ) ^ { 4 } \biggr ] + \frac { 1 } { 2 } \sum _ { A , B \ne A } \frac { G M _ { A } M _ { B } } { r _ { A B } } } } } \\ { { \displaystyle ~ \times \left\{ 1 + \frac { 1 } { c ^ { 2 } } \biggl [ 3 v _ { A } ^ { 2 } - \frac { 7 } { 2 } v _ { A } \cdot v _ { B } - \frac { 1 } { 2 } ( \pmb { n } _ { A B } \cdot \pmb { v } _ { A } ) ( \pmb { n } _ { A B } \cdot \pmb { v } _ { B } ) - \sum _ { C \ne A } \frac { G M _ { C } } { r _ { A C } } \biggr ] \right\} . } } \end{array}
$$

Find the canonical momentum $P _ { A }$ for this Lagrangian, and show that $\sum _ { A } { P _ { A } }$ equals the conserved total momentum of Eq. (9.132b).

9.4 Verify Eq. (9.141).

9.5 Verify all the results listed in Eqs. (9.205).

9.6 To conclude the exploration of the one-parameter family of representative world lines in Sec. 9.5.8, calculate the changes in the barycenter position $\pmb { R }$ and total momentum $P$ induced by the transformation of Eq. (9.239).

9.7 We saw in Sec. 9.6 that the gravitational potentials of a spinless body can be computed efficiently by modeling the body as a point mass with density $m _ { A } \delta ( { \pmb x } - { \pmb r } _ { A } )$ . Here we wish to show that the body’s spin can be accommodated by making the substitution

$$
v ^ { j }  v _ { A } ^ { j } + \frac { 1 } { 2 m _ { A } } S _ { A } ^ { j k } \partial _ { k }
$$

in the potentials. Here the derivative operator attached to the spin tensor is meant to act on the delta function supplied by the density. The prescription is valid to first order in the spin tensor, and terms quadratic in the spin must be neglected. Use the prescription to compute the potentials $U ^ { j } , \Phi _ { 1 }$ , and $\Phi _ { 6 }$ , and compare your results to those displayed in Sec. 9.5.3.

In November 1915, Einstein completed a calculation whose result so agitated him that he worried that he might be having a heart attack. He later wrote to a friend that “for several days I was beside myself in joyous excitement.” What Einstein calculated was the contribution to the advance of the perihelion of Mercury from the first post-Newtonian corrections to Newtonian gravity provided by his newly completed theory of general relativity. This had been a notorious and unsolved problem in astronomy, ever since Le Verrier pointed out in 1859 that there was a discrepancy of approximately 43 arcseconds per century in the rate of advance between what was observed and what could be accounted for in Newtonian theory from planetary perturbations, refer to Secs. 3.1 and 3.4. Many earlier attempts to devise relativistic theories of gravity, including Einstein’s own “Entwurf ” (outline) theory of 1913 with Marcel Grossmann, had failed to give the correct answer. Now armed with the correct field equations, Einstein found an approximate vacuum solution that could be applied to the geodesic motion of Mercury around the Sun. He found that the orbit was almost Keplerian, but with a periastron that advances at a rate that matched Le Verrier’s observations.

For Einstein, this success with Mercury was the first concrete evidence that his theory, over which he had struggled so mightily for the past four years, might actually be correct. His prediction for the deflection of light by the Sun, completed that same month, and which doubled the value that he had derived in 1907 using just the principle of equivalence, would not be confirmed until 1919.

For the next 60 years, until the discovery of the first binary pulsar by Hulse and Taylor, the main testing-ground for general relativity would be the solar system, where gravitational fields are weak and motions are slow, so that the conditions for the post-Newtonian approximation are valid. In this chapter we take the formal development of post-Newtonian theory, presented in Chapters 8 and 9, and apply it to the real world of solar-system dynamics, solar-system experiments, and the dynamics of binary star (and binary black-hole) systems. We will encounter some of the famous experimental tests of general relativity, and will see how the precision of modern tools such as atomic clocks, satellite navigation systems, radio interferometry, and laser ranging make it necessary to take relativistic effects into account in a number of practical applications.

We begin in Sec. 10.1 with a description of the post-Newtonian motion of two selfgravitating bodies; it is in this section that we emulate Einstein with his calculation of the perihelion advance of Mercury. In Section 10.2 we examine the motion of light in weak gravitational fields, and describe such phenomena as the deflection of a light ray by a massive body, gravitational lenses, and the Shapiro time delay. The practically important issue of clock synchronization in the presence of gravitation is the topic of Sec. 10.3. We conclude the chapter in Sec. 10.4 with a discussion of the motion of a binary system of spinning bodies.

# 10.1 Post-Newtonian two-body problem

We begin our exploration of post-Newtonian dynamics with an examination of the twobody problem, the relativistic generalization of the Kepler problem reviewed in Sec. 3.2. The foundations of the post-Newtonian problem were presented in Chapter 9, and the equations that govern the motion of binary systems were derived in Sec. 9.3.7. While the method of derivation employed in most of Chapter 9 was restricted to bodies with weak internal gravity, we saw back in Sec. 9.4 that in fact the equations of motion apply just as well to compact bodies such as neutron stars and black holes; the internal gravity of each body can be arbitrarily strong, but if the mutual gravity is weak, the equations apply.

The equations of motion can be applied to any binary-star system, but they can also be applied to the solar system, in spite of the fact that the number of bodies exceeds two. The reason is that the Sun dominates the mass of the solar system by a factor of 1000, so that from the point of view of relativistic effects, which scale as $G M / ( c ^ { 2 } r )$ , the Sun is the elephant in the room, making the other planets largely irrelevant. Consider, for example, the perihelion advance of Mercury, which is produced in part by relativistic effects, and in part by perturbations generated by other planets (mostly Jupiter). As we shall see below, the relativistic part of the advance per orbit is of order $G M _ { \odot } / ( c ^ { 2 } a ) \sim 3 \times 1 0 ^ { - 8 }$ radians, where $a$ is Mercury’s semi-major axis. On the other hand, we recall from Sec. 3.4.1, refer to Eq. (3.83), that the advance produced by a perturbing planet scales as $( m _ { p } / M _ { \odot } ) ( a / R ) ^ { 3 }$ , where $m _ { p }$ and $R$ are the mass and semi-major axis of the perturbing planet; this is of order $4 \times 1 0 ^ { - 7 }$ radians per orbit when Jupiter is the perturbing planet, and is therefore comparable to the relativistic contribution. We can expect the post-Newtonian corrections to Newtonian third-body perturbations, as well as third-body contributions to the post-Newtonian perturbation, to be of the same order of magnitude as the product of these two small factors, and thus to be unmeasurably small. It follows that for most solar-system applications, we can safely calculate post-Newtonian two-body effects and Newtonian $N .$ - body effects separately, and simply add them together. The conclusion of this discussion is that the relativistic two-body problem provides an adequate foundation to describe most relativistic effects in the solar system.

An important exception to this rule occurs in the Earth–Moon system, for which there is a measurable post-Newtonian three-body effect produced by the Sun, a contribution to the precession of the lunar orbital plane. This effect is often called de Sitter precession, because it was predicted in 1916 by the Dutch astronomer Willem de Sitter, on the basis of his post-Newtonian equations of motion. We shall conclude this section with a description of the de Sitter precession.

# 10.1.1 Equations of motion

The equations that govern the motion of a two-body system were obtained back in Sec. 9.3.7, where they were cast in the form of an effective one-body problem. We work in terms of the separation $r : = r _ { 1 } - r _ { 2 }$ , relative velocity $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ , relative acceleration ${ \textbf { \em a } } : =$ ${ \pmb a } _ { 1 } - { \pmb a } _ { 2 }$ , and involve the mass parameters $m : = M _ { 1 } + M _ { 2 }$ , $\eta : = { M _ { 1 } M _ { 2 } } / ( M _ { 1 } + M _ { 2 } ) ^ { 2 }$ , and $\Delta : = ( M _ { 1 } - M _ { 2 } ) / ( M _ { 1 } + M _ { 2 } )$ . The relative acceleration is given by Eq. (9.142),

$$
\begin{array} { c } { \displaystyle { \pmb { a } = - \frac { G m } { r ^ { 2 } } \pmb { n } - \frac { G m } { c ^ { 2 } r ^ { 2 } } \bigg \{ \bigg [ ( 1 + 3 \eta ) v ^ { 2 } - \frac { 3 } { 2 } \eta \dot { r } ^ { 2 } - 2 ( 2 + \eta ) \frac { G m } { r } \bigg ] \pmb { n } } } \\ { \displaystyle { - 2 ( 2 - \eta ) \dot { \star } \pmb { v } \bigg \} + O ( c ^ { - 4 } ) , } } \end{array}
$$

where $r : = | r |$ is the inter-body distance, ${ \pmb n } : = { \pmb r } / r$ a unit vector that points from body 2 to body 1, and ${ \dot { r } } : = v \cdot n$ the radial component of the velocity vector. Equation (10.1) is a second-order differential equation for $\mathbf { } r ( t )$ , and its solution determines the position of each body. This information is provided by Eq. (9.141),

$$
\begin{array} { l } { { \displaystyle r _ { 1 } = \frac { M _ { 2 } } { m } r + \frac { \eta \Delta } { 2 c ^ { 2 } } \Big ( v ^ { 2 } - \frac { G m } { r } \Big ) r + O ( c ^ { - 4 } ) , } } \\ { { \displaystyle r _ { 2 } = - \frac { M _ { 1 } } { m } r + \frac { \eta \Delta } { 2 c ^ { 2 } } \Big ( v ^ { 2 } - \frac { G m } { r } \Big ) r + O ( c ^ { - 4 } ) . } } \end{array}
$$

These equations imply that $\pmb { v } _ { 1 } = ( M _ { 2 } / m ) \pmb { v } + O ( c ^ { - 2 } )$ and $\pmb { v } _ { 2 } = - ( M _ { 1 } / m ) \pmb { v } + O ( c ^ { - 2 } )$ .

We saw back in Sec. 3.2 that the Newtonian two-body problem admits constants of the motion, the orbital energy $E = \mu \varepsilon$ and the orbital angular momentum $L = \mu h$ , in which $\mu : = M _ { 1 } M _ { 2 } / ( M _ { 1 } + M _ { 2 } ) = \eta m$ is the system’s reduced mass. The post-Newtonian problem also admits a conserved energy and a conserved angular-momentum vector, and it is not difficult to deduce their expressions. We know that at the Newtonian level, the conserved energy is given by $\begin{array} { r } { \varepsilon = { \frac { 1 } { 2 } } v ^ { 2 } - G m / r } \end{array}$ , and we also know that post-Newtonian corrections come with a multiplicative factor of $c ^ { - 2 }$ . Possible contributions must then be proportional to $v ^ { 4 } , \dot { r } ^ { 2 } v ^ { 2 } , \dot { r } ^ { 4 } , v ^ { 2 } G m / r , \dot { r } ^ { 2 } G m / r$ , and $( G m / r ) ^ { 2 }$ , and the correct combination of such terms can be identified by including them all (with unknown coefficients) in a trial expression for $\varepsilon$ , and demanding that $d \varepsilon / d t = 0$ by virtue of the post-Newtonian dynamics of Eq. (10.1). The end result of this simple exercise is the expression

$$
\varepsilon : = \frac { 1 } { 2 } v ^ { 2 } - \frac { G m } { r } + \frac { 1 } { c ^ { 2 } } \Bigg \{ \frac { 3 } { 8 } ( 1 - 3 \eta ) v ^ { 4 } + \frac { G m } { 2 r } \bigg [ ( 3 + \eta ) v ^ { 2 } + \eta \dot { r } ^ { 2 } + \frac { G m } { r } \bigg ] \Bigg \} + { \cal O } ( c ^ { - 4 } )
$$

for the post-Newtonian energy of the two-body system. In a similar way we can show that

$$
h : = \bigg \{ 1 + \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 1 } { 2 } ( 1 - 3 \eta ) v ^ { 2 } + ( 3 + \eta ) \frac { G m } { r } \bigg ] \bigg \} ( r \times v ) + { \cal O } ( c ^ { - 4 } )
$$

is the post-Newtonian angular momentum.

<table><tr><td>10.1</td><td>Ambiguities in energy and angular momentum</td></tr><tr><td></td><td>The expressons of Eqs. (10.3)and (10.4) are actually not unique. For example, six arbitrary coeficients are needed when constructinga post-Newtonian trial expression for ε,and six conditions are found when dε/dt is required to vanish after involving the post-Newtonian equations of motion.Two ofthe conditions, however, turn out tobe redundant,and asa result,one coeficient cannot be determined.It is easy to show thatthe free coeficient represents the freedom to add to the expresion for ε an arbitrary amount ofa post-Newtonian contribution c-2(v2 - 2Gm/r)2.This is constant by virtue of the Newtonian equations of motion,and so theconstancy ofε through O(c-2)stillholds.This freedom reflects the fact thatthe zeroof energy is not fixed in classical mechanics. To arrve at Eq. (10.3) we fixed the free coefficient so that the v4 term in ε has thefactor shown.With this choice,thelimit Gm /r -→ Oofε matches the Newtonian and post-Newtonian terms in the expansion ofthe special relativisticenergyoftwo bodies, given by γ1m1c² + Y2m2c², where YA = (1 - v /c2)-1/2.Similar considerations applyto the conserved angular momentum h.</td></tr></table>

It is interesting to note that although $\pmb { h }$ is conserved in the post-Newtonian dynamics, the vector $r \times v$ is not; this is a point of departure from the Newtonian situation. But while $r \times v$ is no longer constant in magnitude, it is still constant in direction, and this is sufficient to establish that the orbital motion proceeds within a fixed orbital plane, just as in the Newtonian situation. As in Sec. 3.2, we may simplify the mathematical description of the post-Newtonian motion by taking the orbital plane to coincide with the $x - y$ plane of the coordinate system, and by introducing the vectorial basis $\pmb { n } : = [ \cos \phi , \sin \phi , 0 ]$ , $\lambda : = [ - \sin \phi , \cos \phi , 0 ]$ , and $\pmb { e } _ { z } : = [ 0 , 0 , 1 ]$ , in which $\phi$ is the orbital angle. In terms of the orbital basis we have $\boldsymbol { r } = \boldsymbol { r } \boldsymbol { n }$ , $\pmb { v } = \dot { r } \pmb { n } + r \dot { \phi } \pmb { \lambda }$ ,

$$
\pmb { a } = \left( \ddot { r } - r \dot { \phi } ^ { 2 } \right) \pmb { n } + \frac { 1 } { r } \frac { d } { d t } ( r ^ { 2 } \dot { \phi } ) \pmb { \lambda } ,
$$

and $\pmb { r } \times \pmb { v } = ( r ^ { 2 } \dot { \phi } ) \pmb { e } _ { z }$ . The equations of motion become

$$
\begin{array} { c c } { { \displaystyle { \ddot { r } = r \dot { \phi } ^ { 2 } - \frac { G m } { r ^ { 2 } } + \frac { G m } { c ^ { 2 } r ^ { 2 } } \left[ \frac { 1 } { 2 } ( 6 - 7 \eta ) \dot { r } ^ { 2 } - ( 1 + 3 \eta ) ( r \dot { \phi } ) ^ { 2 } + 2 ( 2 + \eta ) \frac { G m } { r } \right] + O ( c ^ { - 4 } ) , } } } & { { \mathrm { ~ i ~ f ~ } } } \\ { { \mathrm { } } } & { { \mathrm { } } } \\ { { \displaystyle { \ddot { r } = r \dot { \phi } ^ { 2 } - \frac { G m } { r ^ { 2 } } \dot { r } \dot { \phi } + O ( c ^ { - 4 } ) , } } } & { { \mathrm { ~ } } } \\ { { \displaystyle { \vphantom { \Biggl ( } } } } & { { \mathrm { ~ \ o } 1 0 . 6 \mathrm { b } \dot { \phi } ^ { 2 } - 1 . } } \end{array}
$$

when they are expressed in terms of the dynamical variables $\boldsymbol { r } ( t )$ and $\phi ( t )$ .

The integration of Eqs. (10.6) is greatly facilitated by the existence of $\varepsilon$ and $h : = | h |$ as constants of the motion. In fact, the conserved quantities can be used to express $\dot { r } ^ { 2 }$ and $\dot { \phi }$ as simple polynomials in $1 / r$ . A simple computation reveals that

$$
\begin{array} { c } { { \dot { r } ^ { 2 } = 2 \varepsilon \bigg [ 1 - \frac 3 2 ( 1 - 3 \eta ) \frac { \varepsilon } { c ^ { 2 } } \bigg ] + 2 \frac { G m } { r } \bigg [ 1 - ( 6 - 7 \eta ) \frac { \varepsilon } { c ^ { 2 } } \bigg ] - \frac { h ^ { 2 } } { r ^ { 2 } } \bigg [ 1 - 2 ( 1 - 3 \eta ) \frac { \varepsilon } { c ^ { 2 } } \bigg ] } } \\ { { - 5 ( 2 - \eta ) \frac { ( G m ) ^ { 2 } } { c ^ { 2 } r ^ { 2 } } + ( 8 - 3 \eta ) \frac { G m h ^ { 2 } } { c ^ { 2 } r ^ { 3 } } + { \cal O } ( c ^ { - 4 } ) } } \end{array}
$$

and

$$
\dot { \phi } = \frac { h } { r ^ { 2 } } \bigg [ 1 - ( 1 - 3 \eta ) \frac { \varepsilon } { c ^ { 2 } } \bigg ] - 2 ( 2 - \eta ) \frac { G m h } { c ^ { 2 } r ^ { 3 } } .
$$

These equations can be compared with their Keplerian version displayed in Eqs. (3.10) and (3.13).

# 10.1.2 Circular orbits

Our next task is integration of the post-Newtonian equations of motion. We begin with the simple case of a circular orbit of radius $r$ . Setting $\dot { r } = 0$ in Eq. (10.6b) reveals that the orbital angular velocity $\dot { \phi }$ is a constant that we denote $\Omega$ . Setting $\ddot { r } = 0$ in Eq. (10.6a) allows us to relate $\Omega$ to $r$ , and we obtain

$$
\Omega ^ { 2 } = \frac { G m } { r ^ { 3 } } \biggl [ 1 - ( 3 - \eta ) \frac { G m } { c ^ { 2 } r } + { \cal O } ( c ^ { - 4 } ) \biggr ] ,
$$

the relativistic version of the familiar Keplerian relation $\Omega ^ { 2 } = G m / r ^ { 3 }$ . The orbital velocity is then given by

$$
v ^ { 2 } = ( r \Omega ) ^ { 2 } = \frac { G m } { r } \biggl [ 1 - ( 3 - \eta ) \frac { G m } { c ^ { 2 } r } + { \cal O } ( c ^ { - 4 } ) \biggr ] ,
$$

and the constants of the motion reduce to

$$
\varepsilon = - { \frac { G m } { 2 r } } \biggl [ 1 - { \frac { 1 } { 4 } } ( 7 - \eta ) { \frac { G m } { c ^ { 2 } r } } + { \cal O } ( c ^ { - 4 } ) \biggr ]
$$

and

$$
h = \sqrt { { G m r } } { \left[ { 1 + 2 \frac { { { G m } } } { { { c ^ { 2 } } r } } + { \cal O } ( { c ^ { - 4 } } ) } \right] } .
$$

# 10.1.3 Perturbed Keplerian orbits

A possible way of integrating the equations of motion is to treat the post-Newtonian terms in Eq. (10.1) as a perturbing force $f$ in the perturbed Kepler problem described in Sec. 3.3. (Recall our admonition from Chapter 3, that even though $f$ is an acceleration, we nevertheless use the conventional term “force” to describe it.) We exploit the method of osculating orbital elements, in which the perturbed motion is represented by a Keplerian orbit with time-dependent orbital elements, which vary in response to the perturbing force. The components of the perturbing force in the orbital basis $( n , \lambda , e _ { z } )$ are

$$
\begin{array} { l } { \displaystyle \mathcal { R } = \frac { G m } { c ^ { 2 } r ^ { 2 } } \biggl [ - ( 1 + 3 \eta ) v ^ { 2 } + \frac { 1 } { 2 } ( 8 - \eta ) \dot { r } ^ { 2 } + 2 ( 2 + \eta ) \frac { G m } { r } \biggr ] , } \\ { \displaystyle \mathcal { S } = \frac { G m } { c ^ { 2 } r ^ { 2 } } \biggl [ 2 ( 2 - \eta ) \dot { r } ( r \dot { \phi } ) \biggr ] , } \\ { \displaystyle \mathcal { W } = 0 , } \end{array}
$$

in which we insert the Keplerian relations $r = p / ( 1 + e \cos f ) , \dot { r } = \sqrt { G m / p } e \sin f , r \dot { \phi } =$ $\sqrt { G m / p } ( 1 + e \cos f )$ , where $p$ is the Keplerian semi-latus rectum, $e$ is the Keplerian eccentricity, and $f : = \phi - \omega$ is the true anomaly, with $\omega$ denoting the Keplerian longitude of pericenter. Substituting the force components within Eqs. (3.69) produces

$$
\begin{array} { l } { \displaystyle \frac { d p } { d f } = 4 ( 2 - \eta ) \frac { G m } { c ^ { 2 } } e \sin f , \eqno ( 3 . 4 ) } \\ { \displaystyle \frac { d e } { d f } = \frac { G m } { c ^ { 2 } p } \left\{ \left[ 3 - \eta + \frac { 1 } { 8 } ( 5 6 - 4 7 \eta ) e ^ { 2 } \right] \sin f + ( 5 - 4 \eta ) e \sin 2 f - \frac { 3 } { 8 } \eta e ^ { 2 } \sin 3 f \right\} , } \end{array}
$$

$$
\frac { l \omega } { l f } = \frac { 1 } { e } \frac { G m } { c ^ { 2 } p } \left\{ 3 e - \left[ 3 - \eta - \frac { 1 } { 8 } ( 8 + 2 1 \eta ) e ^ { 2 } \right] \cos { f } - ( 5 - 4 \eta ) e \cos { 2 f } + \frac { 3 } { 8 } \eta e ^ { 2 } \cos { 3 f } \right\} .
$$

The vanishing of ${ \mathcal W } : = \boldsymbol { f } \cdot \boldsymbol { e } _ { z }$ implies that the inclination angle $\iota$ and longitude of ascending node $\Omega$ are not affected by the perturbing force; this is a consequence of the fact that the post-Newtonian motion proceeds in a fixed orbital plane.

The perturbing force $f$ is of first post-Newtonian order, and working consistently at this order, it is appropriate to integrate Eqs. (10.14) while keeping the orbital elements constant on the right-hand side of the equations. In this way we obtain

$$
p ( f ) = p _ { 0 } \biggl [ 1 + 4 ( 2 - \eta ) { \frac { G m } { c ^ { 2 } p _ { 0 } } } ( 1 - \cos f ) \biggr ]
$$

and more complicated expressions for $e ( f )$ and $\omega ( f )$ ; here $p _ { 0 } : = p ( f = 0 )$ . These expressions can then be inserted within the original Keplerian relations to obtain the complete solutions for $r ( f )$ and ${ \pmb v } ( f )$ . The post-Newtonian motion is thus parameterized by the true anomaly $f$ , and its description in terms of time $t$ can be obtained by integrating Eq. (3.70).

# 10.1.4 Pericenter advance

The description of the post-Newtonian motion in terms of osculating Keplerian orbits is perfectly adequate from a mathematical point of view, but it is fairly awkward to use and not well suited to practical implementations. An illustration of this is the curious fact that the circular orbit of radius $r$ examined in Sec. 10.1.2 is one with Keplerian orbital parameters $e = ( 3 - \eta ) G m / ( c ^ { 2 } r )$ and $p = r [ 1 - ( 3 - \eta ) G m / ( c ^ { 2 } r ) ]$ , and also this orbit has a constant true anomaly given by $f = \pi$ , so that the pericenter advances at the same rate as the body itself. We shall give the motion a much better description in the next subsection, but let’s not give up just yet on the osculating formulation.

In the applications of the method of osculating orbital elements examined in Sec. 3.4, we saw that the method’s most powerful insights are delivered when it is asked to reveal the secular changes in the orbital elements, and allowed to discard any information about the periodic changes that average out after each orbital cycle. We shall adopt this wisdom here, and calculate the secular changes in $p , e$ , and $\omega$ produced by the post-Newtonian perturbation of Eqs. (10.13). They are obtained by integrating Eqs. (10.14) over a complete orbital period (from $f = 0$ to $f = 2 \pi$ ), and the equations produce $\Delta p = 0$ , $\Delta e = 0$ , as

well as

$$
\Delta \omega = 6 \pi { \frac { G m } { c ^ { 2 } p } } .
$$

The fact that $p$ undergoes no secular change is a consequence of angular-momentum conservation, and the absence of a secular change in $e$ (and therefore in the Keplerian semimajor axis $a$ ) is a consequence of energy conservation. The only parameter that undergoes a secular evolution is the longitude of periastron $\omega$ , and Eq. (10.16) describes the pericenter advance that was so famously calculated by Einstein.

Einstein’s method of derivation was very different. He did not have access to the post-Newtonian metric of an $N$ -body system, and he did not have access to the $N$ -body equations of motion. What he did was to obtain the post-Newtonian metric of a single body (the Sun), and to calculate the motion of a second body (Mercury) under the assumption that it is a test mass that moves on a geodesic of the spacetime. This is a sensible assumption, given that the Mercury–Sun mass ratio is approximately one to 6 million. Einstein obtained the result of Eq. (10.16), but with the total mass $m : = { M } _ { 1 } + { M } _ { 2 }$ well approximated by $M _ { 1 }$ , the mass of the Sun. Our result is more general, and it applies to a much broader range of situations.

The advance per orbit can be converted to a rate of advance by dividing by the orbital period. We can also eliminate the semi-major axis appearing in $p = a ( 1 - e ^ { 2 } )$ by using Kepler’s third law, $a = ( G M ) ^ { 1 / 3 } ( P / 2 \pi ) ^ { 2 / 3 }$ , where $P$ is the orbital period; in principle the relation should be modified by a post-Newtonian correction, but the modification is irrelevant because $\Delta \omega$ is already of first post-Newtonian order. The result is

$$
\begin{array} { r } { \left( \frac { d \omega } { d t } \right) _ { \mathrm { s e c } } = \displaystyle \frac { 3 } { 1 - e ^ { 2 } } \frac { ( G M / c ^ { 3 } ) ^ { 2 / 3 } } { ( P / 2 \pi ) ^ { 5 / 3 } } \qquad } \\ { = 7 1 6 . 2 5 \frac { 1 } { 1 - e ^ { 2 } } \bigg ( \frac { M } { M _ { \odot } } \bigg ) ^ { 2 / 3 } \bigg ( \frac { P } { 1 \mathrm { d a y } } \bigg ) ^ { - 5 / 3 } \mathrm { a s } / \mathrm { y r } . } \end{array}
$$

Substituting the values for Mercury, $e = 0 . 2 0 5 6$ and $P = 8 7 . 9 7$ days, we obtain 42.98 arcseconds per century. As we saw back in Table 3.1, the modern difference between the measured advance and the one predicted by Newtonian $N$ -body perturbations is $4 2 . 9 8 \pm$ 0.04 arcseconds per century, in $0 . 1 \%$ agreement with the relativistic prediction.

The discovery of binary-pulsar systems with total masses of 2 to 3 solar masses, and with orbital periods as small as fractions of a day, resulted in the observation of periastron advances of several degrees per year. The relativistic periastron advance plays an interesting role in these systems. In the solar system, $G M$ for the Sun is known to high precision from the measured orbital period and orbital radius of the Earth, combined with Kepler’s third law. By contrast, the masses of the neutron stars are not known, apart from the general expectation that they should be around the Chandrasekhar limit of $1 . 4 M _ { \odot }$ , based on models of how such systems might have formed. In the famous Hulse–Taylor binary pulsar, the first such system to be discovered, it was possible to measure the orbital eccentricity, the orbital period, and the pericenter advance very accurately; the current values are $e = 0 . 6 1 7 1 3 3 8 ( 4 )$ , $P = 0 . 3 2 2 9 9 7 4 4 8 9 3 0 ( 4 )$ day, and $\dot { \omega } = 4 . 2 2 6 5 9 5 ( 5 ) \mathrm { d e g / y r } ,$ , in which the number in parentheses denotes the error in the final digit. Assuming that there is no other source of periastron advance, we can turn Eq. (10.17) around and use it to measure the total mass of the system. The result is $M = 2 . 8 2 8 2 9 6 ( 5 ) M _ { \odot }$ . The recently discovered double pulsar J0737-3039A/B, in which both stars are observed as pulsars, has $e = 0 . 0 8 7 7 7 7 5 ( \mathfrak { L }$ 9), $P = 0 . 1 0 2 2 5 1 5 6 2 4 8 ( 5$ ) day, and $\dot { \omega } = 1 6 . 8 9 9 5 ( 7 ) \mathrm { d e g / y r }$ , giving a total mass of $2 . 5 8 7 1 ( 2 ) M _ { \odot }$ . These are remarkably accurate measurements of an astrophysical quantity, and as we can see, general relativity plays a central role in the analysis.

# 10.1.5 Integration of the equations of motion

To integrate the post-Newtonian equations of motion listed in Sec. 10.1.1, we adopt the approach followed by Damour and Deruelle in their seminal 1985 paper. Our starting point is the observation that the transformation

$$
r = \bar { r } - \frac 1 2 ( 8 - 3 \eta ) \frac { G m } { c ^ { 2 } } + { \cal O } ( c ^ { - 4 } )
$$

turns Eq. (10.7) into the simpler polynomial

$$
\dot { \bar { r } } ^ { 2 } = 2 \varepsilon _ { \mathrm { K } } + 2 \frac { G m _ { \mathrm { K } } } { \bar { r } } - \frac { h _ { \mathrm { K } } ^ { 2 } } { \bar { r } ^ { 2 } } ,
$$

in which

$$
\begin{array} { r l } & { \varepsilon _ { \mathrm { K } } : = \varepsilon \bigg [ 1 - \frac 3 2 ( 1 - 3 \eta ) \frac \varepsilon { c ^ { 2 } } + O ( c ^ { - 4 } ) \bigg ] , } \\ & { m _ { \mathrm { K } } : = m \bigg [ 1 - ( 6 - 7 \eta ) \frac \varepsilon { c ^ { 2 } } + O ( c ^ { - 4 } ) \bigg ] , } \\ & { h _ { \mathrm { K } } ^ { 2 } : = h ^ { 2 } \bigg [ 1 - 2 ( 1 - 3 \eta ) \frac \varepsilon { c ^ { 2 } } + 2 ( 1 - \eta ) \frac { ( G m ) ^ { 2 } } { c ^ { 2 } h ^ { 2 } } + O ( c ^ { - 4 } ) \bigg ] . } \end{array}
$$

The radial equation is an exact replica of the Keplerian equation displayed in Eq. (3.13), and it therefore admits the same solution. We adopt a representation in terms of an eccentric anomaly $u$ , according to which $\bar { r } = \bar { a } ( 1 - \bar { e } \cos u )$ and $t - T = \sqrt { \bar { a } ^ { 3 } / ( G m _ { \mathrm { K } } ) } ( u - \bar { e } \sin u )$ , in which $\bar { a }$ is a post-Newtonian semi-major axis and $\bar { e }$ a post-Newtonian eccentricity, defined in the same way as in the Keplerian problem: $\varepsilon _ { \mathrm { K } } = - G m _ { \mathrm { K } } / ( 2 \bar { a } )$ and $h _ { \mathrm { K } } ^ { 2 } = G m _ { \mathrm { K } } \bar { a } ( 1 - \bar { e } ^ { 2 } )$ .

With the solution for $\bar { r }$ thus obtained, we apply the transformation of Eq. (10.18) to express the motion directly in terms of $r$ . Simple manipulations produce

$$
r = a ( 1 - e \cos u ) ,
$$

in which $\begin{array} { r } { a : = \bar { a } [ 1 - \frac { 1 } { 2 } ( 8 - 3 \eta ) G m / ( c ^ { 2 } \bar { a } ) ] } \end{array}$ and $e = \bar { e } [ 1 + { \textstyle \frac { 1 } { 2 } } ( 8 - 3 \eta ) G m / ( c ^ { 2 } \bar { a } ) ]$ are new post-Newtonian orbital elements. Adopting these as the primary elements, it is a simple matter to express the conserved energy $\varepsilon$ and conserved angular momentum $h$ in terms of $a$ and $e$ ; we obtain

$$
\varepsilon = - { \frac { G m } { 2 a } } \biggl [ 1 - { \frac { 1 } { 4 } } ( 7 - \eta ) { \frac { G m } { c ^ { 2 } a } } + { \cal O } ( c ^ { - 4 } ) \biggr ]
$$

and

$$
h ^ { 2 } = G m a ( 1 - e ^ { 2 } ) \biggl [ 1 + \frac { 4 + ( 2 - \eta ) e ^ { 2 } } { 1 - e ^ { 2 } } \frac { G m } { c ^ { 2 } a } + { \cal O } ( c ^ { - 4 } ) \biggr ] .
$$

The time function can then be expressed as

$$
t - T = { \frac { P } { 2 \pi } } { \big ( } u - e _ { t } \sin u { \big ) } ,
$$

in which

$$
e _ { t } : = e \biggl [ 1 - \frac { 1 } { 2 } ( 8 - 3 \eta ) \frac { G m } { c ^ { 2 } a } + { \cal O } ( c ^ { - 4 } ) \biggr ]
$$

is a second eccentricity parameter (which differs from $e$ by a post-Newtonian correction), and

$$
P : = 2 \pi \sqrt { \frac { a ^ { 3 } } { G m } } \bigg [ 1 + \frac { 1 } { 2 } ( 9 - \eta ) \frac { G m } { c ^ { 2 } a } + { \cal O } ( c ^ { - 4 } ) \bigg ]
$$

is the post-Newtonian period.

To obtain $\phi$ as a function of $u$ we begin with the transformation

$$
r = \tilde { r } - ( 2 - \eta ) \frac { G m } { c ^ { 2 } } + { \cal O } ( c ^ { - 4 } ) ,
$$

which turns Eq. (10.8) into

$$
\dot { \phi } = \frac { \tilde { h } } { \tilde { r } ^ { 2 } } ,
$$

where

$$
\tilde { h } : = \sqrt { G m a ( 1 - e ^ { 2 } ) } \biggl [ 1 + \frac { 3 ( 1 - \eta ) + ( 1 + 2 \eta ) e ^ { 2 } } { 2 ( 1 - e ^ { 2 } ) } \frac { G m } { c ^ { 2 } a } + O ( c ^ { - 4 } ) \biggr ] .
$$

We next use Eq. (10.21) to write $\tilde { r } = \tilde { a } ( 1 - \tilde { e } \cos u )$ , in which $\tilde { a } = a [ 1 + ( 2 - \eta ) G m / ( c ^ { 2 } a ) ]$ and $\tilde { e } = e [ 1 - ( 2 - \eta ) G m / ( c ^ { 2 } a ) ]$ , and Eq. (10.24) to obtain

$$
\frac { d \phi } { d u } = \frac { P } { 2 \pi } \frac { \tilde { h } } { \tilde { a } ^ { 2 } } \frac { 1 - e _ { t } \cos u } { ( 1 - \tilde { e } \cos u ) ^ { 2 } } + O ( c ^ { - 4 } ) ,
$$

which can be integrated to yield the orbital angle $\phi$ in terms of eccentric anomaly $u$ . This equation can be compared with the Keplerian version of Eq. (3.33), and here we see a substantial difference in the form of the equations. In addition to the multiplicative factor that appears on the right-hand side, we see that the post-Newtonian expression involves $( 1 - e _ { t } \cos u ) / ( 1 - \tilde { e } \cos u ) ^ { 2 }$ while the Keplerian version features the simpler factor of $( 1 - e \cos u ) ^ { - 1 }$ . The forms, however, can be reconciled with a simple trick. We first observe that $e _ { t }$ differs from $\tilde { e }$ by a post-Newtonian correction that we denote $\epsilon$ . We next define a third eccentricity parameter by $e _ { \phi } : = \tilde { e } - \epsilon$ , and factorize $( 1 - \tilde { e } \cos u ) ^ { 2 }$ as

$$
\begin{array} { c } { { ( 1 - \tilde { e } \cos u ) ^ { 2 } = \big [ 1 - ( \tilde { e } + \epsilon ) \cos u \big ] \big [ 1 - ( \tilde { e } - \epsilon ) \cos u \big ] + O ( c ^ { - 4 } ) } } \\ { { = ( 1 - e _ { t } \cos u ) ( 1 - e _ { \phi } \cos u ) + O ( c ^ { - 4 } ) . } } \end{array}
$$

This allows us to re-express $d \phi / d u$ as

$$
\frac { d \phi } { d u } = ( 1 + k ) \frac { ( 1 - e _ { \phi } ^ { 2 } ) ^ { 1 / 2 } } { 1 - e _ { \phi } \cos u } + { \cal O } ( c ^ { - 4 } ) ,
$$

which now looks identical to Eq. (3.33), except for the factor $1 + k : = ( P / 2 \pi ) ( \tilde { h } / \tilde { a } ^ { 2 } ) ( 1 -$ $e _ { \phi } ^ { 2 } ) ^ { - 1 / 2 }$ .

The solution to this equation can be expressed as in Eqs. (3.30) and (3.32). We have that

$$
\cos \left( \frac { \phi } { 1 + k } \right) = \frac { \cos u - e _ { \phi } } { 1 - e _ { \phi } \cos u } , \qquad \sin \left( \frac { \phi } { 1 + k } \right) = \frac { ( 1 - e _ { \phi } ^ { 2 } ) ^ { 1 / 2 } \sin u } { 1 - e _ { \phi } \cos u } ,
$$

or that

$$
\mathrm { t a n } \biggl [ { \frac { \phi } { 2 ( 1 + k ) } } \biggr ] = \sqrt { \frac { 1 + e _ { \phi } } { 1 - e _ { \phi } } } \tan { \frac { u } { 2 } } .
$$

Simple algebra confirms that

$$
e _ { \phi } = e \biggl [ 1 + \frac { 1 } { 2 } \eta \frac { G m } { c ^ { 2 } a } + { \cal O } ( c ^ { - 4 } ) \biggr ]
$$

and

$$
k = { \frac { 3 } { 1 - e ^ { 2 } } } { \frac { G m } { c ^ { 2 } a } } + { \cal O } ( c ^ { - 4 } ) .
$$

The meaning of this last quantity is easy to extract from Eqs. (10.33) and (10.34). These relations inform us that in the course of a complete radial cycle, as $u$ runs from 0 to $2 \pi$ , the orbital angle $\phi$ runs from 0 to $2 \pi ( 1 + k )$ . The excess angle,

$$
2 \pi k = 6 \pi \frac { G m } { c ^ { 2 } a ( 1 - e ^ { 2 } ) } + { \cal O } ( c ^ { - 4 } ) ,
$$

is the pericenter advance of Eq. (10.16).

It is a remarkable fact that the two-body equations of motion of post-Newtonian theory can be integrated in the same manner as the Keplerian equations, with only the small cost of introducing two additional eccentricity parameters ${ \bf \nabla } _ { { e _ { t } } }$ and $e _ { \phi }$ , which differ from $e$ by post-Newtonian corrections), and a pericenter-advance parameter $k : = \Delta \omega / ( 2 \pi )$ . This implies that the post-Newtonian motion can be computed with great ease, by exploiting the tried and true methods of celestial mechanics.

The individual motion of each body can be obtained from Eq. (10.2). It is easy to show that

$$
r _ { 1 } : = | \pmb { r } _ { 1 } | = a _ { 1 } ( 1 - e _ { 1 } \cos u ) ,
$$

in which $a _ { 1 } : = ( M _ { 2 } / m ) a$ is the semi-major axis of the first body, while

$$
e _ { 1 } = e \bigg [ 1 - \frac { M _ { 1 } ( M _ { 1 } - M _ { 2 } ) } { 2 m ^ { 2 } } \frac { G m } { c ^ { 2 } a } \bigg ]
$$

is its eccentricity. The corresponding results for the second body are obtained by a suitable exchange of labels.

# 10.1.6 de Sitter precession

The de Sitter precession of the lunar orbit is a relativistic three-body effect that involves the Moon, the Earth, and the Sun; it is a secular advance of the line of nodes of the lunar orbital plane. You will recall from our discussion in Chapter 3 that the motion of the Moon is a notoriously difficult problem in Newtonian gravity, mainly because the strong perturbations caused by the Sun lead to a poorly convergent sequence of corrections. Special formulations of the perturbation theory, such as the Hill–Brown theory, were required for high precision, and today the equations of motion are solved directly using computers. With the motion of the Moon in Newtonian gravity now under control, discrepancies between the predicted and observed motions can be attributed to relativistic effects.

Relativistic three-body effects can be investigated on the basis of the $N$ -body equations listed in Sec. 9.3.5 – refer to Eq. (9.127). As in Sec. 3.4.1, in which we considered third-body effects in Newtonian theory, we focus our attention on a two-body system (the Earth and the Moon) and examine the perturbations produced by a third body (the Sun). We let the Moon be the first body (mass $M _ { 1 }$ , position $r _ { 1 }$ ), the Earth be the second body (mass $M _ { 2 }$ , position $r _ { 2 }$ ), and the Sun be the third body (mass $M _ { 3 }$ , position $r _ { 3 }$ ). We let $r : = r _ { 1 } - r _ { 2 }$ be the separation between the Moon and the Earth, and $\pmb { R } : = \pmb { r } _ { 2 } - \pmb { r } _ { 3 }$ be the separation between the Earth and the Sun. Similarly, we let $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ be the Moon’s velocity relative to Earth’s, and $V : = { \pmb v } _ { 2 } - { \pmb v } _ { 3 }$ be the Earth’s velocity relative to the Sun. For simplicity we imagine that the Sun is at rest at the spatial origin of the coordinate system, so that $\pmb { r } _ { 3 } = \mathbf { 0 } = \pmb { v } _ { 3 }$ .

The relativistic three-body equations lead to effects of various sizes on the two-body system. We wish to focus our attention on the dominant effects, and to allow ourselves to neglect the smaller ones, or to ignore relativistic effects that would be masked by much larger Newtonian effects. To seek guidance in the identification of which terms must be kept in the equations of motion, and which terms can be neglected, we first examine the various scales of the problem.

Our first observation is that $M _ { 1 }$ , the mass of the Moon, is much smaller than both $M _ { 2 }$ and $M _ { 3 }$ , and we shall therefore neglect all terms in the equations of motion that involve $M _ { 1 }$ . Our second observation is that the acceleration of the Earth–Moon system toward the Sun is approximately twice the acceleration of the Moon toward the Earth, $G M _ { 3 } / R ^ { 2 } \sim 2 G M _ { 2 } / r ^ { 2 }$ ; this comes about because $r / R \sim 2 \times 1 0 ^ { - 3 }$ , which counteracts the large value of $M _ { 3 } / M _ { 2 }$ . Our third observation is that the post-Newtonian corrections scale as $G M _ { 3 } / ( c ^ { 2 } R ) \sim 1 0 ^ { - 8 }$ for the Earth–Moon system moving around the Sun, so that $V / c \sim$ $1 0 ^ { - 4 }$ , and as $G M _ { 2 } / ( c ^ { 2 } r ) \sim 1 0 ^ { - 1 1 }$ for the Moon moving around the Earth, so that $v / c \sim$ $3 \times 1 0 ^ { - 6 }$ ; the motion around the Sun is more relativistic than the motion around the Earth. We rely on this observation to neglect $G M _ { 2 } / ( c ^ { 2 } r )$ compared to $G M _ { 3 } / ( c ^ { 2 } R )$ in the equations of motion, and to neglect $( v / c ) ^ { 2 }$ compared to $( V / c ) ^ { 2 }$ . Another source of simplification is the previously noted smallness of $r / R$ , which allows us to ignore the inhomogeneity of the Sun’s gravitational field across the Earth–Moon orbit; this means that ${ \pmb r } _ { 1 3 } = { \pmb R } + { \pmb r }$ can be safely approximated by $\pmb { R }$ in the equations of motion.

With these simplifications, it is a straightforward exercise to apply Eq. (9.127) to the Earth–Moon system perturbed by the Sun. We find that the post-Newtonian term in the

Moon’s acceleration reduces to

$$
\begin{array} { l } { { \displaystyle { \boldsymbol a } _ { 1 } [ \mathrm { P N } ] = \frac { G M _ { 2 } } { c ^ { 2 } r ^ { 2 } } \bigg [ { \boldsymbol V } ^ { 2 } + 2 { \boldsymbol V } \cdot { \boldsymbol v } + \frac 3 2 ( \boldsymbol n \cdot { \boldsymbol V } ) ^ { 2 } + \frac { 5 G M _ { 3 } } { R } \bigg ] \boldsymbol n + \frac { G M _ { 2 } } { c ^ { 2 } r ^ { 2 } } ( \boldsymbol n \cdot { \boldsymbol V } ) { \boldsymbol v } } } \\ { ~ - ~ \frac { G M _ { 3 } } { c ^ { 2 } R ^ { 2 } } \bigg [ { \boldsymbol V } ^ { 2 } + 2 { \boldsymbol V } \cdot { \boldsymbol v } - \frac { 4 G M _ { 3 } } { R } \bigg ] { \boldsymbol N } } \\ { ~ + ~ \frac { 4 G M _ { 3 } } { c ^ { 2 } R ^ { 2 } } \bigg [ ( { \boldsymbol N } \cdot { \boldsymbol V } ) { \boldsymbol V } + ( { \boldsymbol N } \cdot { \boldsymbol V } ) { \boldsymbol v } + ( { \boldsymbol N } \cdot { \boldsymbol v } ) { \boldsymbol V } \bigg ] , } \end{array}
$$

in which ${ \pmb n } : = { \pmb r } / r$ and $N : = R / R$ , and that the Earth’s post-Newtonian acceleration becomes

$$
{ \pmb a } _ { 2 } [ \mathrm { P N } ] = - \frac { G M _ { 3 } } { c ^ { 2 } R ^ { 2 } } \bigg ( V ^ { 2 } - \frac { 4 G M _ { 3 } } { R } \bigg ) { \pmb N } + \frac { 4 G M _ { 3 } } { c ^ { 2 } R ^ { 2 } } ( { \pmb N } \cdot { \pmb V } ) { \pmb V } .
$$

The relative acceleration ${ \pmb a } [ \mathrm { P N } ] : = { \pmb a } _ { 1 } [ \mathrm { P N } ] - { \pmb a } _ { 2 } [ \mathrm { P N } ]$ is then

$$
\begin{array} { l } { { \displaystyle { a [ \mathrm { P N } ] = \frac { G M _ { 2 } } { c ^ { 2 } r ^ { 2 } } \bigg [ V ^ { 2 } + \frac { 3 } { 2 } ( \pmb { n } \cdot { V } ) ^ { 2 } + \frac { 5 G M _ { 3 } } { R } \bigg ] \pmb { n } } } } \\ { { \displaystyle ~ + \frac { 2 G M _ { 3 } } { c ^ { 2 } R ^ { 2 } } \bigg [ 2 ( { \pmb { N } \cdot { V } } ) \pmb { v } + 2 ( { \pmb { N } \cdot { v } } ) { \pmb { V } } - ( { \pmb { V } \cdot { v } } ) { \pmb { N } } \bigg ] } , }  \end{array}
$$

in which we have neglected $2 V \cdot v$ compared to $V ^ { 2 }$ in the first group of terms. This can be treated as a perturbing force $f$ on the Keplerian system formed by the Earth and the Moon, and it can be used in a perturbative evolution of the orbital elements along the lines developed in Sec. 3.4.

The motion of the Moon around the Earth is described by an osculating Keplerian orbit of elements $( p , e , \omega , \iota , \Omega )$ perturbed by the external force of Eq. (10.42). To simplify the description of the evolution of the orbital elements, we follow the approach of Sec. 3.4.1 and place the Earth on a circular orbit of radius $R$ , angular velocity $\Omega _ { \mathrm { o r b } }$ , and orbital phase $F = \Omega _ { \mathrm { o r b } } t$ around the Sun; the orbit is situated in the fundamental $X – Y$ plane. It is then a straightforward task to calculate the components $( \mathcal { R } , { S } , \mathcal { W } )$ of the perturbing force, to insert these into the osculating equations (3.69), to obtain the total changes $( \Delta p , \Delta e , \Delta \omega , \Delta \iota , \Delta \Omega )$ over a complete lunar orbit, and finally, to average these over the motion of the Earth around the Sun. Our final results are that $\langle \Delta p \rangle = \langle \Delta e \rangle = \langle \Delta \iota \rangle =$ $\langle \Delta \omega \rangle = 0$ , but that

$$
\langle \Delta \Omega \rangle = \frac { 3 \pi G } { c ^ { 2 } } \frac { M _ { \odot } ^ { 3 / 2 } p ^ { 3 / 2 } } { M _ { \oplus } ^ { 1 / 2 } R ^ { 5 / 2 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } ,
$$

in which we have substituted the standard symbols $M _ { \odot }$ and $M _ { \oplus }$ for the mass of the Sun and the Earth, respectively. Thus, the only long-term impact of relativistic three-body effects on the lunar orbit is a precession of the line of nodes, whose longitude $\Omega$ advances at the averaged rate

$$
\left( \frac { d \Omega } { d t } \right) _ { \mathrm { s e c } } = \frac { 3 } { 2 } \sqrt { \frac { G M _ { \odot } } { R ^ { 3 } } } \frac { G M _ { \odot } } { c ^ { 2 } R } ,
$$

obtained by dividing $\langle \Delta \Omega \rangle$ by the Moon’s orbital period.

According to Eq. (10.44), the line of nodes of the lunar orbit advances at an averaged rate of 19.1 arcseconds per century. The effect was first predicted in 1916 by de Sitter, but at the time it was far too small to be detected on top of the 19.3 degrees of advance per year produced by the Sun’s Newtonian perturbations. It is a remarkable feat of modern precision instrumentation that thanks to lunar laser ranging (a technique described in some detail in Box 13.2), the de Sitter precession has been measured to a precision of better than one percent.

# 10.2 Motion of light in post-Newtonian gravity

Most of the information about astrophysical objects comes in the form of electromagnetic signals, and confrontation between theory and observations must account for the curved path of a light ray in a gravitational field. Indeed, electromagnetic waves are deflected and delayed by a massive body, and these measurable effects must be taken into account in high-accuracy astronomical observations.

# 10.2.1 Motion of a photon

In the geometric-optics approximation of electromagnetism (refer to Box 5.6), light rays behave as massless particles – photons – that move on null geodesics of a curved spacetime; the geodesic equation for a photon in a post-Newtonian spacetime was obtained in Sec. 8.1.4. The particle moves on a trajectory $\mathbf { } r ( t )$ with a velocity ${ \pmb v } = d { \pmb r } / d t$ that can be expressed as

$$
\pmb { v } = c \bigg ( 1 - \frac { 2 } { c ^ { 2 } } U \bigg ) \pmb { n } + ( c ^ { - 3 } ) ,
$$

in terms of a unit vector $\pmb { n }$ that specifies the direction of propagation. This satisfies the differential equation

$$
\frac { d n ^ { j } } { d t } = \frac { 2 } { c } \big ( \delta ^ { j k } - n ^ { j } n ^ { k } \big ) \partial _ { k } U + O ( c ^ { - 3 } ) ,
$$

in which $U$ is the Newtonian potential evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ . It should be noted that in this section, $\mathbf { } r ( t )$ stands for the photon’s trajectory and not the interbody separation of a two-body system, and $\pmb { n }$ denotes the direction of propagation and not the vector $r / r$ .

The leading-order solution to Eq. (10.46) is $\pmb { n } = \pmb { k } + O ( c ^ { - 2 } )$ , in which $\pmb { k }$ is a constant vector. At this order, the photon’s trajectory is described by the straight path

$$
\pmb { r } ( t ) = \pmb { r } _ { e } + c \pmb { k } ( t - t _ { e } ) + O ( c ^ { - 2 } ) ,
$$

in which $r _ { e } = r ( t = t _ { e } )$ is the position of the source, and $t _ { e }$ is the emission time. At the next order we have

$$
\pmb { n } = \pmb { k } + \pmb { \alpha } + O ( c ^ { - 4 } ) ,
$$

in which the deflection vector $\pmb { \alpha }$ satisfies

$$
\frac { d \alpha ^ { j } } { d t } = \frac { 2 } { c } \big ( \delta ^ { j k } - k ^ { j } k ^ { k } \big ) \partial _ { k } U ,
$$

with $\partial _ { k } U$ evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } ( t )$ , as given by Eq. (10.47). We integrate Eq. (10.49) with the initial conditions

$$
\begin{array} { r } { \pmb { \alpha } ( t = t _ { e } ) = \mathbf { 0 } , } \end{array}
$$

so that $\pmb { n } ( t = t _ { e } )$ , the initial direction of propagation, coincides with the vector $\pmb { k }$ .

Inserting Eq. (10.48) within Eq. (10.45), we find that

$$
\pmb { v } = c \bigg ( 1 - \frac { 2 } { c ^ { 2 } } U \bigg ) \pmb { k } + c \pmb { \alpha } + O ( c ^ { - 3 } ) .
$$

Note that $\pmb { \alpha }$ is necessarily orthogonal to $\pmb { k }$ , so that the second term in Eq. (10.51) describes a transverse deflection of the photon; the longitudinal aspects of the correction are captured by the first term.

To integrate Eq. (10.49) we substitute $\begin{array} { r } { \partial _ { k } U = - G \int \rho ^ { \prime } s ^ { - 3 } s ^ { k } d ^ { 3 } x ^ { \prime } } \end{array}$ on the right-hand side, where $\rho ^ { \prime } : = \rho ( t , \boldsymbol { x } ^ { \prime } )$ is the mass density of the matter distribution, $s : = r ( t ) - x ^ { \prime }$ , and $s : = | \pmb { s } |$ . This gives

$$
\frac { d \pmb { \alpha } } { d t } = - \frac { 2 G } { c } \int \rho ^ { \prime } \frac { \pmb { b } } { s ^ { 3 } } d ^ { 3 } x ^ { \prime } ,
$$

in which

$$
b : = s _ { e } - \left( s _ { e } \cdot k \right) \pmb { k } , \qquad s _ { e } : = { \pmb { r } } _ { e } - { \pmb x } ^ { \prime } ;
$$

the vector $\pmb { b }$ points from $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ to the point of closest approach reached by a photon emitted from a position $r _ { e }$ in a direction $\pmb { k }$ . We next invoke the easily established identity

$$
{ \frac { 1 } { c } } { \frac { d } { d t } } \biggl ( { \frac { s \cdot k } { s } } \biggr ) = { \frac { b ^ { 2 } } { s ^ { 3 } } }
$$

to express $d \pmb { \alpha } / d t$ as

$$
\frac { d \alpha } { d t } = - \frac { 2 G } { c ^ { 2 } } \int \rho ^ { \prime } \frac { b } { b ^ { 2 } } \frac { d } { d t } \bigg ( \frac { s \cdot k } { s } \bigg ) d ^ { 3 } x ^ { \prime } = - \frac { 2 G } { c ^ { 2 } } \frac { d } { d t } \int \rho ^ { \prime } \frac { b } { b ^ { 2 } } \frac { s \cdot k } { s } d ^ { 3 } x ^ { \prime } .
$$

Integration of this equation is immediate.

Taking into account Eq. (10.50), we find that the deflection vector is given by

$$
\pmb { \alpha } ( t ) = - \frac { 2 G } { c ^ { 2 } } \int \rho ( t , \pmb { x } ^ { \prime } ) \frac { \pmb { b } } { b ^ { 2 } } \bigg ( \frac { \pmb { s } \cdot \pmb { k } } { \pmb { s } } - \frac { \pmb { s } _ { e } \cdot \pmb { k } } { \pmb { s _ { e } } } \bigg ) d ^ { 3 } x ^ { \prime }
$$

for any matter distribution. Further progress on evaluating the deflection vector requires specification of the mass density.

With the photon’s velocity $\pmb { v }$ given by Eqs. (10.51) and (10.56), we may now determine the photon’s trajectory $\mathbf { } r ( t )$ . We express the solution to $d r / d t = { \pmb v }$ as

$$
\begin{array} { r } { \pmb { r } ( t ) = \pmb { r } _ { e } + c \pmb { k } ( t - t _ { e } ) + \pmb { k } \delta \pmb { r } _ { \parallel } ( t ) + \delta \pmb { r } _ { \perp } ( t ) + O ( c ^ { - 4 } ) , } \end{array}
$$

in which $\delta r _ { \parallel } ( t )$ is the longitudinal displacement determined by $d ( \delta r _ { \parallel } ) / d t = - 2 U / c$ , and $\delta r _ { \perp } ( t )$ is the transverse displacement determined by $d ( \delta r _ { \perp } ) / d t = c \pmb { \alpha }$ . The longitudinal term in Eq. (10.57) does not alter the path of the photon with respect to its unperturbed description, but it affects the relationship between position and time. The transverse term represents a deviation from the path, in response to the deflection vector $\pmb { \alpha }$ .

To calculate the longitudinal displacement we insert the usual expression for the Newtonian potential and get $\begin{array} { r } { d ( \delta r _ { \parallel } ) / d t = - ( 2 G / c ) \int \rho ^ { \prime } s ^ { - 1 } d ^ { 3 } x ^ { \prime } } \end{array}$ . The identity

$$
{ \frac { 1 } { c } } { \frac { d } { d t } } \ln ( s + s \cdot k ) = { \frac { 1 } { s } }
$$

permits an immediate integration, and we obtain

$$
\delta r _ { \parallel } ( t ) = - \frac { 2 G } { c ^ { 2 } } \int \rho ( t , x ^ { \prime } ) \ln \biggl ( \frac { s + s \cdot k } { s _ { e } + s _ { e } \cdot k } \biggr ) d ^ { 3 } x ^ { \prime } ,
$$

which reflects the initial condition $\delta r _ { \parallel } ( t = 0 ) = 0$ . The factorization $b ^ { 2 } = ( s _ { e } - { s _ { e } } \cdot { \pmb k } ) ( s _ { e } +$ $s _ { e } \cdot k )$ allows us to write this in the alternative form

$$
\delta r _ { \parallel } ( t ) = - \frac { 2 G } { c ^ { 2 } } \int \rho ( t , x ^ { \prime } ) \ln \biggl [ \frac { ( s + s \cdot k ) ( s _ { e } - s _ { e } \cdot k ) } { b ^ { 2 } } \biggr ] d ^ { 3 } x ^ { \prime }
$$

involving the vector $\pmb { b }$

To obtain the transverse displacement we invoke Eq. (10.56) and get

$$
\frac { d } { d t } \delta \pmb { r } _ { \perp } = - \frac { 2 G } { c } \int \rho ( t , \pmb { x } ^ { \prime } ) \frac { \pmb { b } } { b ^ { 2 } } \bigg ( \frac { \pmb { s } \cdot \pmb { k } } { s } - \frac { \pmb { s } _ { e } \cdot \pmb { k } } { s _ { e } } \bigg ) d ^ { 3 } x ^ { \prime } .
$$

Once more integration is immediate thanks to the identity $c ^ { - 1 } d s / d t = s \cdot \pmb { k } / s$ and the fact that the second term within brackets is constant in time. We arrive at

$$
\delta \pmb { r } _ { \perp } ( t ) = - \frac { 2 G } { c ^ { 2 } } \int \rho ( t , \pmb { x } ^ { \prime } ) \frac { \pmb { b } } { b ^ { 2 } } \bigg ( s - \frac { \pmb { s } \cdot \pmb { s } _ { e } } { s _ { e } } \bigg ) d ^ { 3 } x ^ { \prime } ,
$$

which also reflects the initial condition $\delta { \pmb r } _ { \perp } ( t = 0 ) = { \bf 0 }$ . The motion of the photon in the post-Newtonian spacetime is now completely determined.

# 10.2.2 Deflection by a spherical body

The simplest application of light deflection involves a single spherically-symmetric body of mass $M$ , which we place at the spatial origin of the coordinate system. Because the photon must travel outside the body to be observable, the gravitational potential $U$ can be equated to its external expression $G M / | x |$ , and Eq. (10.49) can be integrated for this special case. Alternatively, and more simply, we can insert $\rho ( { \pmb x } ^ { \prime } ) = M \delta ( { \pmb x } ^ { \prime } )$ within Eq. (10.56) and get

$$
\pmb { \alpha } ( t ) = - \frac { 2 G M } { c ^ { 2 } } \frac { \pmb { b } } { b ^ { 2 } } \bigg [ \frac { \pmb { r } ( t ) \cdot \pmb { k } } { r ( t ) } - \frac { \pmb { r } _ { e } \cdot \pmb { k } } { r _ { e } } \bigg ] ,
$$

in which $\pmb { r } ( t ) : = \pmb { r } _ { e } + c \pmb { k } ( t - t _ { e } ) + O ( c ^ { - 2 } )$ , and

$$
\pmb { b } : = \pmb { r } _ { e } - ( \pmb { r } _ { e } \cdot \pmb { k } ) \pmb { k }
$$

![](images/868bfd6f90e5b665418fa51bb109fb4ac59e517607bea5862c3e43bce66f64d1.jpg)

Fig. 10.1 Deflection of light by a spherical body.

is now a constant vector that points from the body’s center-of-mass to the photon’s point of closest approach (see Fig. 10.1); $b : = | \pmb { b } |$ is the impact parameter. Note that the deflection vector always points in the direction of $\mathbf { - } \pmb { b }$ , corresponding to a deflection toward the massive body, and varies in magnitude in response to the change in the photon’s position.

The deflection vector can also be expressed as

$$
\pmb { \alpha } ( t ) = - \frac { 2 G M } { c ^ { 2 } } \frac { \pmb { b } } { b ^ { 2 } } \Big [ \cos \Phi ( t ) + \sqrt { 1 - ( b / r _ { e } ) ^ { 2 } } \Big ] ,
$$

in which cos $\Phi ( t ) : = ( \boldsymbol { r } \cdot \boldsymbol { k } ) / r$ , so that $\Phi ( t )$ is the angle between the photon’s current position $\mathbf { } r ( t )$ and its initial direction $\pmb { k }$ (see Fig. 10.1), and the square root is an alternative expression for $- ( r _ { e } \cdot k ) / r _ { e }$ . If we specialize to a situation in which the distance of closest approach $b$ is very much smaller than the distance to the source $r _ { e }$ , then the deflection vector simplifies to

$$
\pmb { \alpha } ( t ) = - \frac { 4 G M } { c ^ { 2 } } \frac { \pmb { b } } { b ^ { 2 } } \frac { 1 + \cos \Phi ( t ) } { 2 } .
$$

Evaluating this as $t \to \infty$ , long after the photon has passed the point of closest approach, we find that $\mathbf { } r ( t )$ becomes increasingly aligned with $\pmb { k }$ , so that cos $\Phi ( t  \infty )  1$ and

$$
\pmb { \alpha } ( t  \infty ) = - \frac { 4 G M } { c ^ { 2 } } \frac { \pmb { b } } { b ^ { 2 } } .
$$

From Fig. 10.1 it is easy to see that the photon’s total angle of deflection $\alpha$ is given by $\alpha \simeq \tan \alpha = | \pmb { n } \cdot \pmb { b } / b | / ( \pmb { n } \cdot \pmb { k } )$ , in which $\pmb { n } = \pmb { k } + \pmb { \alpha } + O ( c ^ { - 4 } )$ is evaluated at late times. This gives $\alpha = | { \pmb \alpha } \cdot { \pmb b } | / b = | { \pmb \alpha } |$ , and we find that

$$
\alpha = { \frac { 4 G M } { c ^ { 2 } b } } .
$$

This is the famous deflection angle of a light ray passing near a spherical body, as first calculated by Einstein in 1915.

# 10.2.3 Measurement of light deflection

The preceding results indicate that light is indeed deflected by a massive body, but they do not yet offer a means to put the prediction to a test. The reason is that while the final direction of propagation $k + \pmb { \alpha }$ of a photon can easily be measured by a telescope, the initial direction $\pmb { k }$ is unknown, and the extraction of $\pmb { \alpha }$ from the observations is impossible. To perform a test it is necessary to manipulate the equations to produce a relationship between quantities that can be measured directly. The way to proceed is to involve two sources of light, the first a reference source and the second a target source, which represents the emitter of interest. The angle $\theta$ between the two light rays, when they are received simultaneously at a telescope or a radio interferometer, is a measurable quantity. It can be given a precise mathematical expression independent of any coordinate system, and it is this relationship that can be tested by observations.

In the following we assume that all measurements are carried out by an observer at rest in the post-Newtonian spacetime. In reality, of course, observations would be performed by an astronomer on the moving Earth, and her motion would have to be incorporated in the analysis of the measurement; we ignore such effects here. The observer has a spacetime velocity vector $u ^ { \alpha }$ , and her reference frame is spanned by the spatial unit vectors $e _ { ( j ) } ^ { \alpha }$ first introduced in Sec. 4.1.5; the label $( j )$ runs from (1) to (3). The vectors are mutually orthogonal, they are also orthogonal to $u ^ { \alpha }$ , and they satisfy the identity

$$
P ^ { \alpha \beta } : = g ^ { \alpha \beta } + u ^ { \alpha } u ^ { \beta } / c ^ { 2 } = e _ { ( 1 ) } ^ { \alpha } e _ { ( 1 ) } ^ { \beta } + e _ { ( 2 ) } ^ { \alpha } e _ { ( 2 ) } ^ { \beta } + e _ { ( 3 ) } ^ { \alpha } e _ { ( 3 ) } ^ { \beta } .
$$

The tensor $P _ { \beta } ^ { \alpha }$ projects any vector $A ^ { \beta }$ in the directions orthogonal to $u ^ { \alpha }$ , which define the observer’s reference frame; it was first introduced in Sec. 4.1.5 in the context of flat spacetime, and this is its incarnation in a curved spacetime with metric $g _ { \alpha \beta }$ .

Let the target source emit a photon with velocity vector $\boldsymbol { v } ^ { \alpha } = ( c , \pmb { v } )$ , as given by Eq. (10.51), and let the reference source emit another photon with velocity vector $v ^ { \prime \alpha } = ( c , \pmb { v } ^ { \prime } )$ . With no loss of generality we orient the vectorial basis $e _ { ( j ) } ^ { \alpha }$ in such a way that both photons move in the $x - y$ plane of the observer’s reference frame. As shown back in Sec. 4.1.6, see Eq. (4.28), the angle $\phi$ made by the target photon with respect to the observer’s $x$ -axis is determined by

$$
\cos \phi = c \frac { v _ { \alpha } e _ { ( 1 ) } ^ { \alpha } } { - v _ { \beta } u ^ { \beta } } , \qquad \sin \phi = c \frac { v _ { \alpha } e _ { ( 2 ) } ^ { \alpha } } { - v _ { \beta } u ^ { \beta } } .
$$

Similarly, the angle $\phi ^ { \prime }$ made by the reference photon is given by

$$
\cos \phi ^ { \prime } = c \frac { v _ { \alpha } ^ { \prime } e _ { ( 1 ) } ^ { \alpha } } { - v _ { \beta } ^ { \prime } u ^ { \beta } } , \qquad \sin \phi ^ { \prime } = c \frac { v _ { \alpha } ^ { \prime } e _ { ( 2 ) } ^ { \alpha } } { - v _ { \beta } ^ { \prime } u ^ { \beta } } .
$$

The angle between the two photons is $\theta : = \phi - \phi ^ { \prime }$ , and this is given by

$$
\cos \theta = \cos \phi \cos \phi ^ { \prime } + \sin \phi \sin \phi ^ { \prime } = { \frac { v _ { \alpha } v _ { \beta } ^ { \prime } \big ( e _ { ( 1 ) } ^ { \alpha } e _ { ( 1 ) } ^ { \beta } + e _ { ( 2 ) } ^ { \alpha } e _ { ( 2 ) } ^ { \beta } \big ) } { v _ { \mu } v _ { \nu } ^ { \prime } ( u ^ { \mu } u ^ { \nu } / c ^ { 2 } ) } } .
$$

Because $v _ { \alpha } e _ { ( 3 ) } ^ { \alpha } = 0 = v _ { \alpha } ^ { \prime } e _ { ( 3 ) } ^ { \alpha }$ , the quantity within brackets can be replaced by the projector of Eq. (10.69), and we arrive at

$$
\cos \theta = 1 + \frac { g _ { \alpha \beta } v ^ { \alpha } v ^ { \prime \beta } } { v ^ { \mu } v ^ { \prime \nu } ( u _ { \mu } u _ { \nu } / c ^ { 2 } ) } ,
$$

![](images/2ba3bd0d586df35870910e01195874ff7b757af9ddef7577252973ddc7e52665.jpg)  
Fig. 10.2 Geometry of light deflection measurements.

our final expression for the relative angle. Note that the right-hand side of Eq. (10.73) is a spacetime invariant that can be evaluated in any coordinate system; this guarantees that $\theta$ is a precisely defined, observable quantity.

Our next task is to evaluate Eq. (10.73) for our situation, which involves the post-Newtonian spacetime, the observer at rest, and the target and reference photons. The relevant components of the metric tensor are $g _ { 0 0 } = - ( 1 - 2 U / c ^ { 2 } ) + O ( c ^ { - 4 } )$ , $g _ { j k } = ( 1 + 2 U / c ^ { 2 } ) \delta _ { j k } + O ( c ^ { - 4 } )$ , the only non-vanishing component of the observer’s velocity vector is $u ^ { 0 } = c ( 1 + U / c ^ { 2 } ) + O ( c ^ { - 3 } )$ , and the photon’s velocities are given by $\pmb { v } = c ( 1 - 2 U / c ^ { 2 } ) \pmb { k } + c \pmb { \alpha } + O ( c ^ { - 3 } )$ and $\pmb { v } ^ { \prime } = c ( 1 - 2 U / c ^ { 2 } ) \pmb { k } ^ { \prime } + c \pmb { \alpha } ^ { \prime } + O ( c ^ { - 3 } )$ . Inserting all this within Eq. (10.73) gives

$$
\cos \theta = k \cdot k ^ { \prime } + k ^ { \prime } \cdot \alpha + k \cdot \alpha ^ { \prime } + { \cal O } ( c ^ { - 4 } ) .
$$

The relative angle is thus given a simple expression in terms of $\pmb { k }$ and $\pmb { \alpha }$ , the initial direction and deflection of the target photon, as well as $\pmb { k } ^ { \prime }$ and ${ \pmb { \alpha } } ^ { \prime }$ , the initial direction and deflection of the reference photon.

We next insert Eq. (10.66) within Eq. (10.74) and obtain

$$
\cos \theta = \cos \theta _ { 0 } - \frac { 4 M G } { c ^ { 2 } } \frac { k ^ { \prime } \cdot b _ { e } } { b _ { e } ^ { 2 } } \frac { 1 + \cos \Phi _ { e } } { 2 } - \frac { 4 M G } { c ^ { 2 } } \frac { k \cdot b _ { r } } { b _ { r } ^ { 2 } } \frac { 1 + \cos \Phi _ { r } } { 2 } ,
$$

in which $\cos \theta _ { 0 } : = \pmb { k } \cdot \pmb { k } ^ { \prime }$ , so that $\theta _ { 0 }$ is the relative angle in the absence of deflection, cos $\Phi _ { e } : = { r } _ { \mathrm { { o b s } } } \cdot { k } / { r } _ { \mathrm { { o b s } } }$ , so that $\Phi _ { e }$ is the angle between the observer’s position $r _ { \mathrm { o b s } }$ and the direction $\pmb { k }$ of the target photon, and $\cos \Phi _ { r } : = \boldsymbol { r } _ { \mathrm { { o b s } } } \cdot \boldsymbol { k } ^ { \prime } / r _ { \mathrm { { o b s } } }$ , so that $\Phi _ { r }$ is the angle between the observer’s position and the direction of the reference photon (see Fig. 10.2); we also have $\pmb { b } _ { e } : = \pmb { r } _ { e } - ( \pmb { r } _ { e } \cdot \pmb { k } ) \pmb { k }$ , where $r _ { e }$ is the position of the target source (the emitter), and $\pmb { b } _ { r } : = \pmb { r } _ { r } - ( \pmb { r } _ { r } \cdot \pmb { k } ^ { \prime } ) \pmb { k } ^ { \prime }$ , where $r _ { r }$ is the position of the reference source.

Our expression for $\cos \theta$ can be cleaned up if we express $\pmb { k } ^ { \prime } \cdot \pmb { b } _ { e }$ and $\pmb { k } \cdot \pmb { b } _ { r }$ in terms of the angles $\Phi _ { e } , \Phi _ { r }$ , and $\theta _ { 0 }$ . To accomplish this we note that since the vector $r _ { \mathrm { { o b s } } } - r _ { e }$ is directed along $\pmb { k }$ (apart from the small correction from $\alpha$ ), we can write $b _ { e } = r _ { \mathrm { o b s } } - ( r _ { \mathrm { o b s } } \cdot$ $\pmb { k } ) \pmb { k }$ ; similarly we have that $\pmb { b } _ { r } = \pmb { r } _ { \mathrm { o b s } } - ( \pmb { r } _ { \mathrm { o b s } } \cdot \pmb { k } ^ { \prime } ) \pmb { k } ^ { \prime }$ . These expressions imply $\pmb { k } ^ { \prime } \cdot \pmb { b } _ { e } =$ $r _ { \mathrm { o b s } } ( \cos \Phi _ { r } - \cos \Phi _ { e } \cos \theta _ { 0 } )$ and $\pmb { k } \cdot \pmb { b _ { r } } = r _ { \mathrm { o b s } } ( \cos \Phi _ { e } - \cos \Phi _ { r } \cos \theta _ { 0 } )$ . Noting in addition that sin $\Phi _ { e } = b _ { e } / r _ { \mathrm { o b s } }$ and sin $\Phi _ { r } = b _ { r } / r _ { \mathrm { { o b s } } }$ , as can be gleaned from Fig. 10.2, we arrive at

$$
\begin{array} { c } { { \cos \theta = \cos \theta _ { 0 } - \frac { 4 M G } { c ^ { 2 } b _ { e } } \left( \frac { \cos \Phi _ { r } - \cos \Phi _ { e } \cos \theta _ { 0 } } { \sin \Phi _ { e } } \right) \frac { 1 + \cos \Phi _ { e } } { 2 } } } \\ { { - \frac { 4 M G } { c ^ { 2 } b _ { r } } \left( \frac { \cos \Phi _ { e } - \cos \Phi _ { r } \cos \theta _ { 0 } } { \sin \Phi _ { r } } \right) \frac { 1 + \cos \Phi _ { r } } { 2 } . } } \end{array}
$$

The difference between the unperturbed angle $\theta _ { 0 }$ and the measured angle $\theta$ is denoted $\delta \theta$ , and since cos $\theta = \cos ( \theta _ { 0 } + \delta \theta ) = \cos \theta _ { 0 } - \sin \theta _ { 0 } \delta \theta$ , we find that

$$
\begin{array} { c } { \delta \theta = \displaystyle \frac { 4 M G } { c ^ { 2 } b _ { e } } \left( \frac { \cos \Phi _ { r } - \cos \Phi _ { e } \cos \theta _ { 0 } } { \sin \Phi _ { e } \sin \theta _ { 0 } } \right) \frac { 1 + \cos \Phi _ { e } } { 2 } } \\ { \displaystyle + \frac { 4 M G } { c ^ { 2 } b _ { r } } \left( \frac { \cos \Phi _ { e } - \cos \Phi _ { r } \cos \theta _ { 0 } } { \sin \Phi _ { r } \sin \theta _ { 0 } } \right) \frac { 1 + \cos \Phi _ { r } } { 2 } . } \end{array}
$$

We recall that $\theta _ { 0 }$ is the angle subtended by the target and reference sources, that $\Phi _ { e }$ is the angle subtended by the target source and the deflecting body, and that $\Phi _ { r }$ is the angle subtended by the reference source and the deflecting body. In our discussion so far, these angles have been defined by the unperturbed, straight motion of the light rays in flat spacetime, as depicted in Fig. 10.2. But since the angles occur within a post-Newtonian expression, and the difference between the perturbed and unperturbed angles is itself of post-Newtonian order, we can actually interpret $\theta _ { 0 }$ , $\Phi _ { e }$ , and $\Phi _ { r }$ in Eq. (10.77) as if they were the observed angles on the sky; the difference manifests itself at second post-Newtonian order only, and is negligible.

# Box 10.2

# Spherical trigonometry

Angular measurements in astronomy are performed on the celestial sphere, a fictitious sphere of large radius centered at the position of the observer, on which all astronomical bodies are imagined to be situated. Relationships between angles are then clarified with the rules of spherical trigonometry.

For the angles shown in Fig. 10.3, we have the relations

$$
\cos \theta _ { 0 } = \cos \Phi _ { r } \cos \Phi _ { e } + \sin \Phi _ { r } \sin \Phi _ { e } \cos \chi ,
$$

$$
\Phi _ { e } = \cos \theta _ { 0 } \cos \Phi _ { r } + \sin \theta _ { 0 } \sin \Phi _ { r } \cos A ,
$$

and

$$
{ \frac { \sin \Phi _ { e } } { \sin A } } = { \frac { \sin \Phi _ { r } } { \sin B } } = { \frac { \sin \theta _ { 0 } } { \sin \chi } } .
$$

With these we find that Eq. (10.77) simplifies to

$$
\delta \theta = \frac { 4 M G } { c ^ { 2 } b _ { e } } \cos B \frac { 1 + \cos \Phi _ { e } } { 2 } + \frac { 4 M G } { c ^ { 2 } b _ { r } } \cos A \frac { 1 + \cos \Phi _ { r } } { 2 } .
$$

![](images/81bb905607c25bb884ccd90e43529d9467e7d232bd2c4c60398eb5656e7a9fc0.jpg)

Angles of sources on the celestial sphere as seen from the Earth. When the Sun is behind the Earth, the point labelled “Sun” becomes the extension of the Sun–Earth line into the sky, and the angles $\Phi _ { r }$ and $\Phi _ { e }$ become $\pi - \Phi _ { r }$ and $\pi - \Phi _ { e } ,$ respectively.

This equation states that the change in angular separation between the target and reference sources is just the sum of the apparent displacement of each image away from the deflecting body, projected along the line joining the reference and target sources.

Equation (10.77) is what we need to put the prediction of light deflection to a test, except for the fact that while we can always measure $\theta$ for the target and reference sources, we still do not have access to $\theta _ { 0 }$ , its unperturbed value. To get around this, all measurements of the light deflection are carried out differentially. In this method, the angle between the target and reference stars is measured at different times, first when the Sun is nowhere in the vicinity of the stars, and again when the light from the target star passes near the Sun. The first measurement yields the unperturbed angle, which does not change with time unless the stars have significant proper motion. The second measurement yields the deflected angle $\theta$ , and a measurement of $\delta \theta = \theta - \theta _ { 0 }$ can finally be compared with Eq. (10.77).

Equation (10.77) simplifies a little when the target source is very close to the Sun as seen from Earth, so that $\Phi _ { e } \ll 1 .$ An expansion of cos $\theta _ { 0 } = \cos \Phi _ { r }$ cos $\Phi _ { e } + \sin \Phi _ { r }$ sin $\Phi _ { e } \cos \chi$ , see Box 10.2, in powers of $\Phi _ { e }$ reveals that

$$
\theta _ { 0 } = \Phi _ { r } - \cos \chi \ \Phi _ { e } + \frac { \cos \Phi _ { r } \sin ^ { 2 } \chi } { 2 \sin \Phi _ { r } } \Phi _ { e } ^ { 2 } + O ( \Phi _ { e } ^ { 3 } ) ,
$$

and substitution within Eq. (10.77) produces

$$
\delta \theta = \frac { 4 G M } { c ^ { 3 } b _ { e } } \biggl [ - \cos \chi + \frac { 1 + ( 1 + 2 \sin ^ { 2 } \chi ) \cos \theta _ { 0 } } { 2 \sin \theta _ { 0 } } \Phi _ { e } + O ( \Phi _ { e } ^ { 2 } ) \biggr ] ,
$$

in which $\chi$ is the angle subtended by the reference and target sources as seen from the Sun (as shown in Fig. 10.3). This expression reveals clearly how the angular separation between the target and reference sources changes with time as the Sun moves across the sky, causing $\chi$ and $\Phi _ { e }$ to vary with time. Inserting $b _ { e } = r _ { \mathrm { o b s } } \sin \Phi _ { e } = r _ { \mathrm { o b s } } \Phi _ { e } + O ( \Phi _ { e } ^ { 3 } )$ reveals also that the theoretical prediction can be expressed entirely in terms of observable quantities.

The first successful measurement of the bending of light by the Sun was carried out by British astronomer Arthur Stanley Eddington and his colleagues during the total solar eclipse of May 29, 1919. Two expeditions were sent out to measure the eclipse, one to Brazil, the other to the small island of Principe, off the west coast of Africa. In both cases it was a differential measurement: Photographs of the stars near the Sun taken during the eclipse were compared with photographs of the same stars taken at night from the same locations later in the year, and the changes in angles between pairs of stars were carefully measured. Eddington’s announcement in November 1919 that the bending measurements were in agreement with general relativity helped make Einstein an international celebrity. The observations, however, had an accuracy of approximately 30 percent, and succeeding eclipse measurements were not much better. The results were scattered between one half and twice the Einstein prediction, but in spite of such limited success, Einstein was declared victorious.

The subsequent development of long-baseline radio interferometry greatly improved the measurement of the light deflection. These techniques now have the capability of measuring angular separations and changes in angles to accuracies of tens of micro-arcseconds. Early measurements took advantage of the fact that a few quasistellar radio sources – quasars – pass very close to the Sun as seen from the Earth. As the Earth moves in its orbit, changing the lines of sight of the quasars relative to the Sun, the angular separation $\delta \theta$ between pairs of quasars varies. The time evolution of $\chi$ and $\Phi _ { e }$ in Eq. (10.79) is determined using an accurate ephemeris for the Earth and initial directions for the quasars, and the resulting prediction for $\delta \theta$ as a function of time is compared with the measured values. A number of measurements of this kind over the period 1969–1975 yielded results in agreement with general relativity to a few parts in $1 0 ^ { 3 }$ . In recent years, transcontinental and intercontinental VLBI observations of quasars and radio galaxies have been made primarily to monitor the Earth’s rotation and to establish a highly accurate reference frame for astronomy and navigation. These measurements are sensitive to the deflection of light over almost the entire celestial sphere. For example, the deflection of a ray approaching the Earth from a direction $9 0 ^ { \circ }$ away from the Sun is 4 milli-arcseconds, easily measurable by modern VLBI techniques. A 2004 analysis of nearly 2 million VLBI observations of 541 radio sources, made by 87 VLBI sites over a 20-year period, verified Einstein’s prediction to a few parts in $1 0 ^ { 4 }$ . Analysis of observations made by the Hipparcos optical astrometry satellite yielded a test at the level of 0.3 percent, and a future orbiting observatory named GAIA will have the capability of testing the deflection to parts per million.

<table><tr><td>Box 10.3</td><td>The &quot;Newtonian&quot; deflection of light</td></tr><tr><td></td><td>At the time of Eddington&#x27;s atempt to measure the deflection of light, people envisioned three possible out- comes for the experiment: no deflection,the Einsteinian deflection,or one half of Einstein&#x27;s prediction, com-</td></tr><tr><td></td><td>monly called the&quot;Newtonian&quot; deflection.The Newtonian deflection can be derived in a variety of ways. One</td></tr><tr><td></td><td> way is to assume that light behaves as a particle, to recall that the trajectory of a particle is independent of</td></tr><tr><td></td><td>its mass (weak equivalence principle),and to calculate the deflection of its trajectory in the limit in which the particle&#x27;s speed approaches the speed of light. Such an approach would have made sense in Newton&#x27;s day,</td></tr></table>

when light was really viewed as a “corpuscle,” and indeed, Newton himself speculated on the possible effect of gravity on light.

The English physicist Henry Cavendish may have been the first person to calculate the bending explicitly, possibly as early as 1784, although evidence for this was not discovered until around 1914, during an effort to compile and publish his entire body of work – publication never being high on Cavendish’s list of priorities. In fact, all that was found was a scrap of paper in Cavendish’s handwriting stating that he had done the calculation, and giving the answer.

Independently of Cavendish, the Bavarian astronomer Johann von Soldner did publish in 1803 a detailed calculation of the Newtonian bending in a German astronomical journal. Strangely, von Soldner’s calculation was largely forgotten until it was resurrected in 1921 by Phillip Lenard as part of a campaign to discredit the “Jewish” relativity of Einstein by publicizing the earlier work of the “Aryan” von Soldner. Apparently, Lenard was not deterred by the fact that the 1919 observations actually favored general relativity over the Newtonian deflection.

Unaware of the earlier work, Einstein himself derived the “Newtonian” deflection in 1911. He argued, as we have back in Sec. 5.1.3, that gravity requires replacement of the Minkowski metric of flat spacetime by the Newtonian metric of Eq. (5.12),

$$
d s ^ { 2 } = - ( 1 - 2 U / c ^ { 2 } ) d ( c t ) ^ { 2 } + d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } .
$$

Geodesic motion for a test particle in this spacetime reproduces Newtonian gravity, and geodesic motion for a photon gives the Newtonian deflection. Another derivation using only the equivalence principle imagines a sequence of freely falling frames through which a light ray passes as it travels near a gravitating body. Each frame is momentarily at rest at the moment the light ray enters it. Although the path of the ray is a straight line within each frame, the frame picks up a downward velocity during the ray’s traversal, because of the body’s gravitational attraction. When the adjacent frame receives the light ray, it is deflected toward the body because the downward motion of the previous frame induces aberration on the received ray. By adding up all the tiny aberrations over a sequence of frames, one arrives at the Newtonian deflection.

But the full theory of general relativity doubles the deflection, because the spatial part of the metric now comes with the multiplying factor $( 1 + 2 U / c ^ { 2 } )$ . This represents spatial curvature, which could not be taken into account either by Newtonian gravity or by the principle of equivalence. So the total deflection can be viewed as a sum of a Newtonian deflection relative to locally straight lines, plus the bending of locally straight lines relative to straight lines at infinity; each effect contributes exactly half the total deflection.

# 10.2.4 Gravitational lenses

The deflection of light has become a cornerstone of the empirical edifice that supports general relativity. But in 1979 the phenomenon became much more than that. That year, astronomers Dennis Walsh, Robert Carswell and Ray Weymann discovered the “double quasar” $\mathrm { Q 0 9 5 7 + 5 6 1 }$ , which consisted of two quasar images about 6 arcseconds apart, with almost the same redshift $( z = 1 . 4 1 )$ ) and very similar spectra. Given that quasars are thought to be among the most distant objects in the universe, the probability of finding two so close together was low. It was soon realized that there was in fact just one quasar, but that intervening matter in the form of a galaxy or a cluster of galaxies was bending the light from the quasar and producing two separate images.

Since then, over 60 lensed quasars have been discovered. But more importantly, gravitational lensing has become a major tool in efforts to map the distribution of mass around galaxies and clusters, and in searches for dark matter, dark energy, compact objects, and extrasolar planets. Many subtopics of gravitational lensing have been developed to cover different astronomical realms: microlensing for the search for dim compact objects and extra-solar planets, the use of luminous arcs to map the distribution of mass and dark matter, and weak lensing to measure the properties of dark energy. Lensing has to be taken into account in interpreting certain aspects of the cosmic microwave background radiation, and in extracting information from gravitational waves emitted by sources at cosmological distances. These topics are beyond the scope of this book, but we can extend our discussion of the deflection of light to provide many of the basic concepts and results.

# Deflection vector

We consider light rays emitted by a remote source like a quasar to be observed by an astronomer on Earth. The rays pass through a distribution of matter – the gravitational lens – on their way to the observer, and undergo a deflection described by the vector $\pmb { \alpha }$ of Eq. (10.56). In this situation the source is almost directly behind the lens, so that $s _ { e } \cdot k / s _ { e } \simeq - 1$ , the observer is almost directly in front of the lens, so that $s _ { \mathrm { 0 b s } } \cdot k / s _ { \mathrm { 0 b s } } \simeq 1$ , and the deflection vector can be simplified to

$$
\pmb { \alpha } = - \frac { 4 G } { c ^ { 2 } } \int \rho ( \pmb { x } ^ { \prime } ) \frac { \pmb { b } } { b ^ { 2 } } d ^ { 3 } \pmb { x } ^ { \prime } ,
$$

in which $\pmb { b } : = \pmb { s } _ { e } - ( \pmb { s } _ { e } \cdot \pmb { k } ) \pmb { k }$ , where $\pmb { s } _ { e } : = \pmb { r } _ { e } - \pmb { x } ^ { \prime }$ ; here $r _ { e }$ is the position of the source relative to the center-of-mass of the matter distribution, and $\pmb { k }$ is the ray’s initial direction; its final direction as measured by the observer is $\pm \pmb { \alpha }$ . We have assumed that the distribution of matter is time independent, so that $\rho$ depends on the spatial variables $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ only.

To express the deflection vector in a more convenient form we introduce the vectors

$$
\pmb { \xi } : = \pmb { r _ { e } } - ( \pmb { r _ { e } } \cdot \pmb { k } ) \pmb { k } , \qquad \pmb { \xi } ^ { \prime } : = \pmb { x } ^ { \prime } - ( \pmb { x } ^ { \prime } \cdot \pmb { k } ) \pmb { k } ,
$$

so that $\pmb { \xi }$ is the projection of the source’s position $r _ { e }$ in the lens plane, defined as the plane perpendicular to the direction of propagation $\pmb { k }$ $\pmb { \xi }$ is also the photon’s point of closest approach to the center-of-mass of the matter distribution), and similarly, $\pmb { \xi } ^ { \prime }$ is the projection of $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ in the lens plane. In terms of these vectors we have that $\pmb { b } = \pmb { \xi } - \pmb { \xi } ^ { \prime }$ , and the deflection vector becomes

$$
\pmb { \alpha } = - \frac { 4 G } { c ^ { 2 } } \int \rho ( \pmb { x } ^ { \prime } ) \frac { \pmb { \xi } - \pmb { \xi } ^ { \prime } } { \vert \pmb { \xi } - \pmb { \xi } ^ { \prime } \vert ^ { 2 } } d ^ { 3 } x ^ { \prime } .
$$

To simplify this further we implement a coordinate transformation from the old system $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ to a new system $( \pmb { \xi } ^ { \prime } , \ell ^ { \prime } )$ , in which $\ell ^ { \prime } : = x ^ { \prime } \cdot k$ is the distance along the line of sight,

perpendicular to the lens plane. Integration over $d { \boldsymbol { \ell } } ^ { \prime }$ involves $\rho ( \pmb { \xi } ^ { \prime } , \ell ^ { \prime } )$ only, and it gives rise to

$$
\Sigma ( \pmb { \xi } ^ { \prime } ) : = \int \rho ( \pmb { \xi } ^ { \prime } , \ell ^ { \prime } ) d \ell ^ { \prime } ,
$$

the projected, two-dimensional mass density (per unit area) of the matter distribution. Our final expression for the deflection vector is

$$
\pmb { \alpha } ( \pmb { \xi } ) = - \frac { 4 G } { c ^ { 2 } } \int \ d \Sigma ( \pmb { \xi } ^ { \prime } ) \frac { \pmb { \xi } - \pmb { \xi } ^ { \prime } } { \vert \pmb { \xi } - \pmb { \xi } ^ { \prime } \vert ^ { 2 } } d ^ { 2 } \pmb { \xi } ^ { \prime } ;
$$

it reveals that $\pmb { \alpha }$ is a function of $\pmb { \xi }$ only, and that it lies within the lens plane. Alternative expressions for the deflection vector are formulated in Exercise 10.5.

The deflection vector acquires a particularly simple form when the matter distribution is axially symmetric, so that the surface density $\Sigma$ depends only on the magnitude $\xi ^ { \prime }$ of the vector $\pmb { \xi } ^ { \prime }$ . In this case we can adopt a system of polar coordinates $( \xi ^ { \prime } , \phi ^ { \prime } )$ in the lens plane, and carry our the integration over the angle $\phi ^ { \prime }$ . The result is

$$
\pmb { \alpha } ( \pmb { \xi } ) = - \frac { 4 G } { c ^ { 2 } } \frac { m ( \pmb { \xi } ) } { \pmb { \xi } ^ { 2 } } \pmb { \xi } ,
$$

in which

$$
m ( \xi ) : = 2 \pi \int _ { 0 } ^ { \xi } \Sigma ( \xi ^ { \prime } ) \xi ^ { \prime } d \xi ^ { \prime }
$$

is the mass inside a circle of radius $\xi$ in the lens plane. In this case the deflection vector necessarily points in the direction opposite to $\pmb { \xi }$ .

# Lens equation

We now consider the situation depicted in Fig. 10.4. We have a source at a distance $D _ { \mathrm { { S } } }$ from the observer, and a lens between the source and observer, at a distance $D _ { \mathrm { { L } } }$ from the observer; $D _ { \mathrm { L S } } : = D _ { \mathrm { S } } - D _ { \mathrm { L } }$ is the distance between the lens and the source. The figure displays the lens plane, which is perpendicular to the initial direction of propagation of the light rays, and a source plane that contains the source, which is parallel to the lens plane. The figure also shows the optical axis, which passes through the observer and the center-of-mass of the lens; the optical axis is not necessarily perpendicular to the planes. The vector $\pmb { \eta }$ gives the position of the source in the source plane, relative to the optical axis, and $\boldsymbol { \zeta }$ is the position of the image relative to the source; as usual $\pmb { \xi }$ is the point of closest approach in the lens plane. We introduce the vector $\beta : = \eta / D _ { \mathrm { S } }$ , whose magnitude $\beta$ is the angle between the source and the optical axis. We introduce also the vector $\pmb { \theta } : = ( \pmb { \eta } + \pmb { \zeta } ) / D _ { \mathrm { S } }$ , whose magnitude $\theta$ is the angle between the image and the optical axis.

Our main goal is to determine $\pmb \theta$ for a given $\beta$ , and the key step is to recognize from Fig. 10.4 that the deflection vector $\boldsymbol { \zeta }$ can be expressed as $- \pmb { \alpha } D _ { \mathrm { L S } }$ , where the negative sign accounts for the fact that $\pmb { \alpha }$ points in the direction opposite to $\pmb { \xi }$ . The definition of $\pmb \theta$ then

![](images/ce4ca694da2a02c9b33f193bcdf7f93c6cfafd258b231f1455aba51eb10fa343.jpg)  
Fig. 10.4 Geometry of a gravitational lens. The observer is labeled O, the source S, and the image I.

implies $\pmb { \theta } = ( D _ { \mathrm { S } } \pmb { \beta } - D _ { \mathrm { L S } } \pmb { \alpha } ) / D _ { \mathrm { S } }$ , or

$$
\pmb \theta + \frac { D _ { \mathrm { L S } } } { D _ { \mathrm { S } } } \pmb \alpha = \pmb \beta .
$$

This lens equation can be solved for $\pmb \theta$ once we insert the deflection vector of Eq. (10.84), in which we substitute $\pmb { \xi } = D _ { \mathrm { { L } } } \pmb { \theta }$ , another relation that can be inferred from Fig. 10.4. Because the deflection vector is a non-linear function of its argument, the lens equation typically admits more than one solution for a given source position $\beta$ . To obtain these solutions it is necessary to know ${ \pmb { \alpha } } ( { \pmb { \xi } } )$ , and this requires an evaluation of the integral in Eq. (10.84). This can be accomplished when the density profile of the lens is known, but this information is usually not available in an astronomical context. The power of gravitational lensing in astronomy resides in the fact that the lens equation can be turned around: the measured positions of the multiple images of a given source can be used, through the deflection vector $\pmb { \alpha }$ , to deduce some features of the mass distribution.

# Schwarzschild lens

The simplest instance of a gravitational lens is one created by a single, sphericallysymmetric body of mass $M$ . In this case the deflection vector is given by Eq. (10.67), or is obtained by letting $m ( \xi ) = M$ in Eq. (10.85). We have

$$
\pmb { \alpha } ( \pmb { \xi } ) = - \frac { 4 G M } { c ^ { 2 } } \frac { \pmb { \xi } } { \pmb { \xi } ^ { 2 } } ,
$$

and substitution within Eq. (10.87) gives rise to

$$
\theta - \frac { \theta _ { \mathrm { E } } ^ { 2 } } { \theta } = \beta ,
$$

in which

$$
\theta _ { \mathrm { E } } ^ { 2 } : = { \frac { 4 G M } { c ^ { 2 } } } { \frac { D _ { \mathrm { L S } } } { D _ { \mathrm { S } } D _ { \mathrm { L } } } } .
$$

In this case the lens equation reduces to a scalar equation, because by virtue of the axial symmetry of the lens (which follows from its spherical symmetry), all vectors point in the same direction. The parameter $\theta _ { \mathrm { E } }$ is known as the Einstein angle, and the corresponding length scale

$$
\xi _ { \mathrm { E } } : = D _ { \mathrm { L } } \theta _ { \mathrm { E } } = { \sqrt { { \frac { 4 G M } { c ^ { 2 } } } { \frac { D _ { \mathrm { L S } } D _ { \mathrm { L } } } { D _ { \mathrm { S } } } } } }
$$

is the Einstein radius. The Einstein angle gives the characteristic scale of the deflection. For lenses of galactic scales with $M \sim 1 0 ^ { 1 2 } M _ { \odot }$ , $\theta _ { \mathrm { E } } \simeq 1 . 8$ as, while for solar-mass lenses, $\theta _ { \mathrm { E } } \simeq 0 . 5$ mas. The lens equation is consistent whenever $\xi \gg 4 G M / c ^ { 2 }$ , so that higher post-Newtonian corrections are not required, and this condition implies that $\theta$ must be much larger than $( D _ { \mathrm { S } } / D _ { \mathrm { L S } } ) \theta _ { \mathrm { E } } ^ { 2 }$ .

The solutions to the lens equations are

$$
\theta _ { \pm } = \frac { 1 } { 2 } \bigg ( \beta \pm \sqrt { \beta ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } } \bigg ) ,
$$

and we see that the lens produces two images of the source. For large angles $\beta \gg \theta _ { \mathrm { E } }$ the solutions reduce to $\theta _ { + } = \beta + \theta _ { \mathrm { E } } ^ { 2 } / \beta + \cdot \cdot \cdot$ and $\theta _ { - } = - \theta _ { \mathrm { E } } ^ { 2 } / \beta + \cdot \cdot \cdot$ , which indicates that one image is displaced beyond the source, while the second image occurs below the optical axis and is closer to the lens than is the source itself. When $\beta$ increases beyond unity, the second solution becomes smaller than $\theta _ { \mathrm { E } } ^ { 2 }$ and enters a regime in which the lens equation is no longer consistent, because for this solution $\xi = D _ { \mathrm { L } } \theta = - D _ { \mathrm { L } } \theta _ { \mathrm { E } } ^ { 2 } / \beta \sim$ $( 4 G M / c ^ { 2 } ) ( D _ { \mathrm { L S } } / D _ { \mathrm { S } } ) / \beta$ , which violates the condition $\xi \gg 4 G M / c ^ { 2 }$ . For small angles $\beta \ll$ $\theta _ { \mathrm { E } }$ the solutions reduce to $\begin{array} { r } { \theta _ { + } = \theta _ { \mathrm { E } } + \frac { 1 } { 2 } \beta + \cdot \cdot \cdot } \end{array}$ and $\begin{array} { r } { \theta _ { - } = - \theta _ { \mathrm { E } } + \frac { 1 } { 2 } \beta + \cdot \cdot \cdot } \end{array}$ , which indicates that the images are at an angle approximately equal to $\theta _ { \mathrm { E } }$ above and below the optical axis. When $\beta = 0$ , that is, when the source is directly behind the lens, the deflection angle is precisely equal to $\pm \theta _ { \mathrm { E } }$ , and the axial symmetry of the situation forces the image to take the shape of a ring – known as an Einstein ring – around the optical axis.

When the source has a non-zero angular size, the lens continues to displace its images, but there is also a distortion of its shape. Points on opposite sides of the source perpendicular to the optical axis are displaced by an angle $\theta$ , and are therefore stretched by a corresponding factor, while points on either side parallel to the optical axis are stretched only by the difference in $\theta$ . When the source is circular, and in the limit where its angular size $\delta \beta$ is small compared to $\beta$ , the image is an ellipse with an axis ratio $a / b = \beta / \sqrt { \beta ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } }$ , with $a$ denoting the semi-axis in the direction of the lens, and $b$ the semi-axis in the perpendicular direction. For sources of larger angular size, the image can actually be distorted into an arc with a convex side; this occurs when

$$
\delta \beta < \beta \quad \mathrm { a n d } \quad \theta _ { \mathrm { E } } \geq \frac { \beta - \delta \beta } { 2 \delta \beta } \sqrt { \beta ^ { 2 } - \delta \beta ^ { 2 } } .
$$

The orientation and shapes of such luminous arcs have been used to deduce the mass distribution of the galaxies or clusters that act as lenses, a procedure sometimes dubbed gravitational tomography. Even when the lens produces elliptical distortions that are too small to be measured individually, there is a systematic effect, averaged over large collections of images, that is sensitive to the evolution of the universe over an epoch when dark energy began to be important; this is the realm of weak gravitational lensing.

Because the number of photons emitted per unit area and unit time is constant for a steady source, the brightness of the image is proportional to its observed area, which for small angles is proportional to $\int \theta d \theta d \phi$ . And because the intrinsic area of the source is proportional to $\int \beta d \beta d \phi$ , we find that each image is magnified by a factor

$$
\mu _ { \pm } = \frac { \theta _ { \pm } d \theta _ { \pm } } { \beta d \beta } = \pm \frac { 1 } { 4 } \Bigg ( \frac { \beta } { \sqrt { \beta ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } } } + \frac { \sqrt { \beta ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } } } { \beta } \pm 2 \Bigg ) .
$$

The term in parentheses is always greater than zero, and we see that $\mu _ { + }$ is positive, while $\mu _ { - }$ is negative, indicating that the image is inverted relative to the source. In addition, we see that $\mu _ { + }$ is always greater than unity, but that $| \mu _ { - } |$ is smaller than unity, indicating that the second image is actually demagnified by the lens.

In microlensing situations the images are too close together to be resolved individually by the observer, and in such cases the total magnification is measured by

$$
| \mu _ { + } | + | \mu _ { - } | = \frac { 1 } { 2 } \biggl ( \frac { \beta } { \sqrt { \beta ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } } } + \frac { \sqrt { \beta ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } } } { \beta } \biggr ) ,
$$

which is always greater than unity. The technique of monitoring the variable brightness of lensing images was used in a series of experiments to search for “massive compact halo objects” (MACHOs) in our galaxy. If the galaxy contained a population of dark objects (black holes, neutron stars, brown dwarf stars, or other exotic objects) with masses comparable to $M _ { \odot }$ , then the brightness of a star transiting behind such an object should behave in a way consistent with Eq. (10.95). This effect can be distinguished from the star’s own variability, or from the absorption of starlight by intervening matter, because these tend to depend on wavelength, while the lensing is independent of wavelength. Searches for dark objects passing in front of the dense field of stars in the Large Magellanic Cloud and in the galactic center were carried out between 1993 and 2007, placing a stringent upper limit on the amount of halo mass that could be made up of such objects. This strengthened the conclusion that the vast majority of the halo mass must be made of non-baryonic dark matter.

In 2003, an extra-solar planetary system was discovered by microlensing. The combined lensing of a distant source by a Jupiter-scale companion and its host star was measured and could be deconvolved to determine the mass ratio and the approximate distance between the planet and the star. Additional systems were discovered subsequently, and gravitational lensing is proving to be a key tool in the search for exoplanets.

# 10.2.5 Shapiro time delay

Our discussion of the motion of light in a gravitational field has so far emphasized the transverse aspects of the motion – the deflection of a light ray with respect to its unperturbed, straight path. The longitudinal aspects – the changed relationship between position and time – are also important, and we conclude this section with an examination of the delay suffered by a photon as it travels across a gravitational potential well. We consider a light source situated at $r _ { e }$ relative to the center-of-mass of a spherical body of mass $M$ , and an observer situated at $r _ { \mathrm { o b s } }$ . We imagine that the body is situated between the source and the observer, near the line of sight, and that the photon is at a distance $b$ from the body when it reaches its point of closest approach. We wish to calculate the light-travel time between the source and observer.

The information is contained in Eq. (10.57),

$$
\begin{array} { r } { \pmb { r } ( t ) = \pmb { r } _ { e } + c \pmb { k } ( t - t _ { e } ) + \pmb { k } \delta r _ { \parallel } ( t ) + \delta \pmb { r } _ { \perp } ( t ) + O ( c ^ { - 4 } ) , } \end{array}
$$

in which we may insert Eq. (10.60) for the longitudinal displacement $\delta \boldsymbol { r } _ { \parallel }$ , and Eq. (10.62) for the transverse displacement $\delta r _ { \perp }$ . The equation is evaluated at $t = t _ { \mathrm { o b s } }$ so that $r ( t =$ $t _ { \mathrm { 0 b s } } ) = r _ { \mathrm { 0 b s } }$ , and the displacements must be specialized to the case at hand, for which the mass density can be expressed as $\rho ( t , \pmb { x } ^ { \prime } ) = M \delta ( \pmb { x } ^ { \prime } )$ . We do not need an explicit expression for $\delta \boldsymbol { r } _ { \perp }$ , but we find that the longitudinal displacement becomes

$$
\delta \boldsymbol { r } _ { \parallel } = - \frac { 2 G M } { c ^ { 2 } } \ln \biggl [ \frac { ( \boldsymbol { r } _ { \mathrm { { o b s } } } + \boldsymbol { r } _ { \mathrm { o b s } } \cdot \boldsymbol { k } ) ( \boldsymbol { r } _ { e } - \boldsymbol { r } _ { e } \cdot \boldsymbol { k } ) } { b ^ { 2 } } \biggr ] .
$$

The travel time $t _ { \mathrm { o b s } } - t _ { e }$ is computed by squaring Eq. (10.96), which yields

$$
\begin{array} { r } { | r _ { \mathrm { \small 0 b s } } - r _ { e } | ^ { 2 } = c ^ { 2 } ( t _ { \mathrm { \small 0 b s } } - t _ { e } ) ^ { 2 } + 2 c ( t _ { \mathrm { \small 0 b s } } - t _ { e } ) \delta r _ { \parallel } + O ( c ^ { - 4 } ) , } \end{array}
$$

or

$$
c ( t _ { \mathrm { { o b s } } } - t _ { e } ) = | { \boldsymbol { r } } _ { \mathrm { { o b s } } } - { \boldsymbol { r } } _ { e } | - \delta r _ { \parallel } + O ( c ^ { - 4 } ) .
$$

Inserting our expression for $\delta r _ { \parallel }$ , we arrive at

$$
t _ { \mathsf { o b s } } - t _ { e } = { \frac { 1 } { c } } | r _ { \mathsf { o b s } } - r _ { e } | + { \frac { 2 G M } { c ^ { 3 } } } \ln \left[ { \frac { ( r _ { \mathsf { o b s } } + r _ { \mathsf { o b s } } \cdot k ) ( r _ { e } - r _ { e } \cdot k ) } { b ^ { 2 } } } \right] + { \cal O } ( c ^ { - 5 } ) .
$$

The first term is obviously the time required to travel a distance $| r _ { \mathrm { { o b s } } } - r _ { e } |$ in the absence of gravity, while the second term is the delay produced by the massive body. With the source assumed to be at a large distance behind the body, and the observer at a large distance in front of the body, we have that $r _ { e } \cdot k / r _ { e } \simeq - 1$ and $r _ { \mathrm { 0 b s } } \cdot k / r _ { \mathrm { 0 b s } } \simeq 1$ , and Eq. (10.100) simplifies to

$$
t _ { \mathrm { o b s } } - t _ { e } = { \frac { 1 } { c } } | r _ { \mathrm { o b s } } - r _ { e } | + { \frac { 2 G M } { c ^ { 3 } } } \ln { \frac { 4 r _ { \mathrm { o b s } } r _ { e } } { b ^ { 2 } } } + { \cal O } ( c ^ { - 5 } ) .
$$

This will be our final expression for the light-travel time.

The situation examined thus far does not yet give rise to a means to measure the time delay, because the time of emission $t _ { e }$ is typically not known. A slight variation on the theme, however, gives us what we need. Imagine that the light source at $r _ { e }$ is replaced by a

reflector, and that the observer at $r _ { \mathrm { o b s } }$ sends a pulse of light to the reflector at a time $t _ { 0 }$ , to receive it back at a later time $t _ { 1 }$ . The light-travel time during the return trip is twice what was calculated previously, and we find that

$$
t _ { 1 } - t _ { 0 } = { \frac { 2 } { c } } | \boldsymbol { r } _ { \mathrm { { o b s } } } - \boldsymbol { r } _ { e } | + { \frac { 4 G M } { c ^ { 3 } } } \ln { \frac { 4 { r } _ { \mathrm { { o b s } } } r _ { e } } { b ^ { 2 } } } + { \cal O } ( c ^ { - 5 } ) .
$$

The last term is the famous Shapiro time delay. For solar-system situations it can be expressed as

$$
\Delta t _ { \mathrm { S h a p i r o } } = \frac { M } { M _ { \odot } } \bigg \{ 2 4 0 - 2 0 \ln \bigg [ \bigg ( \frac { b } { R _ { \odot } } \bigg ) ^ { 2 } \bigg ( \frac { \mathrm { A U } ^ { 2 } } { r _ { \mathrm { o b s } } r _ { e } } \bigg ) \bigg ] \bigg \} \mu \mathrm { s } ,
$$

in which $r _ { \mathrm { o b s } }$ and $r _ { e }$ are measured in astronomical units, the distance between the Earth and the Sun; the Shapiro time delay is measured in hundreds of microseconds.

While we are now closer to a measurement protocol, we are not there yet. For one thing, our expression for the time delay, Eq. (10.102), is given in terms of coordinate time and distances, and it should be converted to an expression that involves observable quantities only. For another, we do not have access to the unperturbed, Euclidean distance $| r _ { \mathrm { { o b s } } } - r _ { e } |$ in order to separate out the relativistic effect. Just as in the case of the deflection of light reviewed in Sec. 10.2.3, it is essential to do a differential measurement of the variations in round-trip travel times during many repetitions of the experiment. Particularly important are “superior conjunction” configurations in which the reflector transits behind the Sun as viewed from Earth, leading to a strong modulation of the travel times by the logarithmic term in Eq. (10.102) as $^ b$ changes with time. In order to do this accurately, however, one must take into account the variations in travel times that are due to the orbital motion of the reflector. This is done by accumulating radar-ranging data on the reflector when it is far from superior conjunction (so that the time-delay term is negligible) to determine its orbit, using the computed orbit to predict its coordinate trajectory $r _ { e } ( t )$ near superior conjunction, and then combining this with the trajectory of the Earth $\mathbf { } r _ { \oplus } ( t )$ to determine the Newtonian round-trip time and the logarithmic term in Eq. (10.102). The prediction made on this basis can then be compared with the actual measurements obtained during superior conjunction.

It was radio astronomer Irwin I. Shapiro who first discovered, in 1964, that the time delay was a prediction of general relativity. (It was independently discovered by Jet Propulsion Laboratory scientists Duane Muhleman and Paul Reichley.) He called it the “fourth” test of general relativity, after the three classical tests – the periastron advance of Mercury, the light deflection, and the redshift of light as it climbs up a gravitational field. Shapiro and his colleagues carried out the first measurement of the time delay in 1967, by bouncing radar signals off the surface of Mercury. Later experiments involved radar echos from Venus and the tracking of the Mars exploration spacecraft, Mariners 6, 7 and 9, as well as the 1976 Viking landers and orbiters.

The most recent measurement of the Shapiro time delay exploited the Cassini spacecraft while it was on its way to Saturn. Several circumstances made this mission particularly favorable. One was the ability to do tracking measurements using both X-band $( 7 1 7 5 \mathrm { M H z } )$ and Ka-band $( 3 4 3 1 6 \mathrm { M H z } )$ ) radar, thereby significantly reducing the dispersive effects of the solar corona. Another was that the distance of closest approach of the radar signals to the

Sun was only $1 . 6 R _ { \odot }$ during Cassini’s 2002 superior conjunction, when the spacecraft was at $8 . 4 3 { \mathrm { ~ } } _ { \mathrm { A U } }$ from the Sun. Because the tracking involved Doppler measurements only, and not time delays, it was the rate of change of the Shapiro delay that was actually measured. The result was in agreement with general relativity to two parts in $1 0 ^ { 5 }$ .

The Shapiro delay now figures in a wide range of astrophysical phenomena. In its one-way incarnation, it has been measured in a number of binary-pulsar systems, most notably in the double pulsar J0737-3039A/B, where the orbit is seen almost edge-on, and the pulsed radio signals from each pulsar pass close to the other pulsar once per orbit. It is also relevant in analyses of the spectra and time variations of X-ray emissions from accretion disks around black holes; in this case the modeling must be performed in full general relativity, because the post-Newtonian approximation breaks down near black holes.

# 10.3 Post-Newtonian gravity in timekeeping and navigation

In our development of the foundations of special and general relativity, we have emphasized that only physically measurable quantities are relevant, and that the selection of coordinates is completely arbitrary, devoid of physical meaning. On the other hand, to calculate such things as equations of motion or the Shapiro time delay, it is essential to have a suitable coordinate system. No one should consider doing such calculations using a proper time variable or using physically-measured lengths, because this would introduce unnecessary complications into the calculations. In this section we explore the relationship between the coordinates employed to chart a spacetime and the physical measurements carried out by observers moving in the spacetime.

# 10.3.1 “A brief history of time”

[The title of this section is obviously borrowed from Stephen Hawking’s bestseller. We could not resist.]

Most of the calculations presented in this book employ a coordinate system $x ^ { \alpha }$ defined so that, far from any gravitating system, the coordinate $x ^ { 0 } / c : = t$ represents proper time as measured by an inertial observer at rest with respect to the coordinate system, and $x ^ { j }$ represent spatial coordinates whose scale is measured by rigid rulers also at rest. But we rarely have access to those ideal observers, and we make our measurements using instruments that reside in the gravitational field of the Earth, which is itself moving in the gravitational environment of the solar system.

Most measurements involve time. We determine the orbit of a planet by measuring the time at which it passes in front of a star or transits across the Sun. We determine the orbit of a spacecraft by measuring either the round-trip travel time of a radar signal (radar ranging) or the change in frequency of the return signal compared to the emitted signal (Doppler tracking). We determine the position of a quasar by measuring the difference in arrival time of a given radio wave front at two radio telescopes separated by a known baseline. We navigate around the countryside by measuring the times of arrival of coded signals from four or more GPS satellites orbiting the Earth. So a question is: what is the relationship between time as measured on Earth and the coordinate time t that we use to calculate the motion of planets and satellites or the trajectories of light rays?

Before about 1950, this question did not have much practical importance. Time was determined initially by the regular rotation of the Earth, so that the second was defined to be 1/86 400 of a day. But as measurements of the orbits of the Earth and planets improved, it was realized that the length of the day fluctuates seasonally because of largescale atmospheric motions, and it increases with time because of tidal dissipation, making it ill suited as a standard of time for precision measurements. The standard of time was then replaced by ephemeris time, for which the second is defined to be a fraction of the period of the Earth’s orbit around the Sun. But even the Earth’s orbital period is not precisely constant, because of planetary perturbations, and a better time standard had to be identified.

The development of atomic clocks during the period 1949–1955 made it possible to envision a standard of time based on fundamental physics instead of astronomy, with a potential for unprecedented accuracy. Today the second is defined to be the time elapsed during 9192 631 770 cycles of the hyperfine transition in the ground state of cesium-133. In addition, the speed of light has now been defined to be exactly equal to $2 9 9 7 9 2 4 5 8 \mathrm { m } / \mathrm { s }$ , so that the meter is now defined in terms of the second, and is no longer tied to the length of a certain platinum rod in Paris.

During the 1960s and early 1970s, two developments signaled that general relativity would have to be incorporated into the practical definition of time. One was the development of numerical methods to integrate the equations of motion for bodies in the solar system, which replaced the largely analytic perturbative methods reviewed in Chapter 3. These techniques made it straightforward to include post-Newtonian corrections in the equations of motion, so that ephemeris time could be regarded as akin to the coordinate time $t$ that appears in the post-Newtonian metric. The second development was the ongoing improvement in the accuracy and stability of atomic clocks, in particular those based on cesium-133, rubidium-87, and the $_ { 2 1 - \mathrm { c m } }$ hyperfine transition of hydrogen. With stabilities better than a few parts in $1 0 ^ { 1 3 }$ , these new standards were sensitive to the effects of gravity on time. For example, two clocks on the surface of the Earth differ in their rates by one part in $1 0 ^ { 1 3 }$ for every kilometer in height difference, and this effect is easily measured by the latest clocks. The rate difference between the surface of the Earth and interplanetary space is a few parts in $1 0 ^ { 1 0 }$ , so that the effect of gravity on time is very important in the determination of planetary orbits.

As a result, in 1976 the International Astronomical Union, one of whose functions is to establish the world-wide agreements and conventions for the establishment and dissemination of precise time, resolved to establish atomic time as the primary international standard, known as Temps Atomique International (tai), for which the second is defined by a cesium-133 clock at rest on the Earth’s geoid (see below). They also established the relationship between tai and the time coordinate $t$ involved in the post-Newtonian metric and in calculations of orbital motion. In 1991 the IAU endeavored to make these definitions as rigorous as possible from a relativistic point of view, and established working groups to monitor the definitions and their accuracy in the face of improving technology and more exacting requirements by users. This is a great example of the practical importance of general relativity.

The resolutions of the IAU are framed in the context of the post-Newtonian metric and equations of motion, and it has not yet proved necessary to extend these considerations to second post-Newtonian order. This is because the maximum size of the 2pn corrections is of order $( U / c ^ { 2 } ) ^ { 2 } \sim 1 0 ^ { - 1 6 }$ , which is just below the accuracy of the best current clocks (here the gravitational potential is dominated by the Sun, and it is evaluated at the Earth’s orbit). One can well imagine, however, that the next generation of atomic clocks, based on phenomena like cold atom fountains, Bose-Einstein condensates, or atom interferometers, will be so accurate that 2pn corrections will be needed.

# 10.3.2 Reference frames

We begin our exploration of the measurement of time on, or near, a moving and rotating Earth with the specification of three reference frames. The first is the barycentric frame $( t _ { \mathrm { b a r y } } , x _ { \mathrm { b a r y } } )$ , which is attached to the barycenter of the entire solar system; this is the frame in which the motion of planets would be calculated. The second is the non-rotating geocentric frame $( { \bar { t } } , { \bar { { \boldsymbol { x } } } } )$ , which is attached to the moving Earth, but is non-rotating with respect to the barycentric frame; this is the frame in which the motion of satellites around the Earth would be calculated, and the behavior of their clocks analyzed. And the third is the rotating geocentric frame $( t , \boldsymbol { x } )$ , which is also attached to the moving Earth, but rotating rigidly with Earth’s angular velocity; this is the frame in which the behavior of clocks on the surface of the Earth would be analyzed.

The transformation between the barycentric and non-rotating geocentric frames is a special case of the class of post-Newtonian transformations developed in Sec. 8.3. This case was examined in Sec. 8.3.5, where it was shown that

$$
\begin{array} { l } { { t _ { \mathrm { b a r y } } = \displaystyle \bar { t } + \frac { 1 } { c ^ { 2 } } ( A + { \pmb v } _ { \oplus } \cdot \bar { \pmb x } ) + O ( c ^ { - 4 } ) , } } \\ { { \pmb x } _ { \mathrm { b a r y } } = \bar { \pmb x } + { \pmb r } _ { \oplus } + O ( c ^ { - 2 } ) , } \end{array}
$$

in which $\pmb { r } _ { \oplus } ( \bar { t } )$ is the Earth’s position in the barycentric frame, expressed as a function of geocentric time $\bar { t }$ , ${ \pmb v } _ { \oplus } ( \bar { t } )$ its velocity, and $A ( \bar { t } )$ is determined by

$$
{ \frac { d A } { d \bar { t } } } = { \frac { 1 } { 2 } } v _ { \oplus } ^ { 2 } + U _ { \mathrm { e x t } } ,
$$

with $U _ { \mathrm { e x t } } ( { \bar { t } } , \pmb { r } _ { \oplus } )$ denoting the piece of the Newtonian potential produced by the bodies external to the Earth, including the Moon, Sun, and other solar-system bodies, evaluated at the Earth’s position.

The discussion of Sec. 8.3.5 implies that in the non-rotating geocentric frame, the metric is given by

$$
d s ^ { 2 } = - \biggl [ 1 - \frac { 2 } { c ^ { 2 } } U + O ( c ^ { - 4 } ) \biggr ] d ( c \bar { t } ) ^ { 2 } + \Bigl [ 1 + O ( c ^ { - 2 } ) \Bigr ] \bigl ( d \bar { x } ^ { 2 } + d \bar { y } ^ { 2 } + d \bar { z } ^ { 2 } \bigr ) ,
$$

in which $U$ (which should be properly denoted $\bar { U }$ ) is the Earth’s gravitational potential augmented by the tidal potential produced by the external bodies. For reasons that will be clarified shortly, we have neglected the post-Newtonian terms in the metric, and retained only the Newtonian term in $\bar { g } _ { 0 0 }$ .

We wish to use the metric of Eq. (10.106) to calculate the interval of proper time $d \tau$ measured by a clock moving with a velocity $\bar { v }$ in the non-rotating geocentric frame. Because $d \tau$ is related to $d s ^ { 2 }$ by $c ^ { 2 } d \tau ^ { 2 } = - d s ^ { 2 }$ , and because $d { \bar { x } } = { \bar { v } } d { \bar { t } }$ as we follow the clock’s world line, we find that

$$
d \tau = \left[ 1 - { \frac { 1 } { c ^ { 2 } } } { \left( { \frac { 1 } { 2 } } \bar { v } ^ { 2 } + U \right) } + { \cal O } ( c ^ { - 4 } ) \right] d \bar { t } .
$$

This is a key equation that allows us to relate $d \tau$ , a quantity measured by an actual clock, to $d { \bar { t } } _ { \bar { } }$ , an interval of coordinate time that is measured by no one, but could be employed in many calculations. The relation involves the clock’s speed $\bar { v } - \mathbf { a }$ special relativistic effect – and the gravitational potential $U - \mathbf { a }$ general relativistic effect. The neglect of post-Newtonian terms in the metric can now be justified: they would lead to corrections of order $c ^ { - 4 }$ in $d \tau$ , which are negligible in the present context. We shall also neglect the tidal terms in $U$ , because $U _ { \mathrm { t i d a l } } / c ^ { 2 } \sim 1 0 ^ { - 1 7 }$ is too small to be of practical significance, at least for today’s technological state of the art.

The transformation between the rotating and non-rotating geocentric frames involves a rigid rotation of the coordinates around the Earth’s rotation axis (which we choose to align with the $z$ -direction), at the Earth’s angular velocity $\omega$ . The transformation is described in great detail in Sec. 2.3.1, where we show that the velocities transform as $v ^ { \bar { a } } = \Lambda _ { \ j } ^ { \bar { a } } ( v ^ { j } + \epsilon _ { \ k n } ^ { j } \omega ^ { k } x ^ { n } )$ , in which $\bar { \pmb { v } }$ is the clock’s velocity in the non-rotating frame, $\pmb { v }$ its velocity in the rotating frame, $\omega = [ 0 , 0 , \omega ]$ is the angular-velocity vector, and $\Lambda$ is the transformation matrix. The relation implies

$$
\bar { v } ^ { 2 } = v ^ { 2 } + 2 v \cdot ( \omega \times x ) + \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) ,
$$

and substitution within Eq. (10.107) returns

$$
d \tau = \left[ 1 - \frac { 1 } { c ^ { 2 } } \left( \frac { 1 } { 2 } \boldsymbol { v } ^ { 2 } + \boldsymbol { v } \cdot ( \boldsymbol { \omega } \times \boldsymbol { x } ) + \Phi \right) + O ( c ^ { - 4 } ) \right] d t ,
$$

in which

$$
\Phi = U + \Phi _ { \mathrm { C } }
$$

is the Newtonian potential augmented by the centrifugal potential $\Phi _ { \mathrm { C } } : = \textstyle { \frac { 1 } { 2 } } \omega ^ { 2 } ( x ^ { 2 } + y ^ { 2 } )$ . It should be noted that the time coordinate employed in the rotating frame is the same as in the non-rotating frame: $t : = \bar { t }$ . We can rely on Eq. (10.109) to relate a clock time interval $d \tau$ to the coordinate time interval $d t$ .

# 10.3.3 Geoid

We now focus our attention on a clock situated on Earth’s surface, or at a low elevation above the surface; the clock may be at rest or moving with a velocity $\pmb { v }$ . We shall perform our calculations in the rotating geocentric frame $( t , \boldsymbol { x } )$ , and therefore work with Eq. (10.109).

Our first item of business is to specify a reference surface from which all elevations will be measured. Because of the important role that the generalized potential $\Phi$ plays in Eq. (10.109), it is wise to choose a surface $\Phi =$ constant as our reference, which is then known as the geoid. From Sec. 2.3.1 we know that surfaces of constant $\rho , p$ , and $\Phi$ all coincide for a fluid body, and since the body’s boundary is situated at $p = 0$ , the reference surface can be made to coincide with the boundary. The Earth is not quite a fluid body, but most of its surface is covered by oceans which do behave as perfect fluids. For the Earth, therefore, the geoid is chosen to coincide with the mean ocean surface extended through the continents.

To model the gravitational field of the Earth we take into account its rotational deformation, but neglect all other deformations produced by inhomogeneities in its mass density; this is a gross oversimplification of the actual situation. We assume that the deformation is axially symmetric, and express the gravitational potential as in Eq. (1.144),

$$
U ( r , \theta ) = \frac { G M } { r } \biggl [ 1 - J _ { 2 } \biggl ( \frac { R } { r } \biggr ) ^ { 2 } P _ { 2 } ( \cos \theta ) \biggr ] ,
$$

in which the multipole expansion was truncated to $\ell = 2$ ; here $M$ is the mass of the Earth, $R$ its equatorial radius, and $J _ { 2 }$ its dimensionless quadrupole moment. The centrifugal potential is

$$
\Phi _ { \mathrm { C } } = { \frac { 1 } { 2 } } \omega ^ { 2 } r ^ { 2 } \sin ^ { 2 } \theta ,
$$

and according to our discussion in Sec. 2.4.5, $J _ { 2 } = k _ { 2 } \zeta$ , in which $k _ { 2 }$ is the Earth’s gravitational Love number, and

$$
\zeta : = \frac { 2 \omega ^ { 2 } R ^ { 3 } } { 3 G M }
$$

provides the fractional scale of the rotational deformation. We shall assume that $\zeta \ll 1$ .

Constructing $\Phi = U + \Phi _ { \mathrm { C } }$ , it is easy to show that the geoid $\Phi ( r , \theta ) = \Phi _ { \mathrm { g e o i d } } =$ constant is situated on the surface $r = R _ { \mathrm { g e o i d } } ( \theta )$ , where

$$
R _ { \operatorname { g e o i d } } ( \theta ) = R ( 1 - f \cos ^ { 2 } \theta )
$$

with

$$
f = { \frac { 3 } { 2 } } J _ { 2 } + { \frac { \omega ^ { 2 } R ^ { 3 } } { 2 G M } } = { \frac { 3 } { 4 } } ( 1 + 2 k _ { 2 } ) \zeta .
$$

The expression implies that $f = 1 - R ( 0 ) / R ( \textstyle { \frac { \pi } { 2 } } )$ , and the condition $\zeta \ll 1$ implies that $f$ is small.

Another description of the geoid is given by the Cartesian form $x ^ { 2 } + y ^ { 2 } + ( 1 +$ $2 f ) z ^ { 2 } = R ^ { 2 }$ , and the unit normal $\pmb { n }$ to the geoid is easily shown to have the components $n _ { x } = ( 1 - 2 f \cos ^ { 2 } \theta ) \sin \theta \cos \phi , n _ { y } = ( 1 - 2 f \cos ^ { 2 } \theta ) \sin \theta \sin \phi$ , and $n _ { z } = ( 1 +$ $2 f \sin ^ { 2 } \theta ) \cos \theta .$ . The geographical latitude $\psi$ of a point on the geoid is the angle between $\pmb { n }$ and the equatorial plane, so that sin $\psi = n _ { z }$ . The relation implies

$$
\cos \theta = ( 1 - 2 f \cos ^ { 2 } \psi ) \sin \psi .
$$

In terms of the geographical latitude we have that $R _ { \mathrm { g e o i d } } = R ( 1 - f \sin ^ { 2 } \psi )$ .

For future reference we wish to find an approximate expression for the potential $\Phi$ for a point $\boldsymbol { x }$ at a height $h \ll R$ just above (or below) the geoid; the displacement is in the direction of the normal vector $\pmb { n }$ , at a constant geographical latitude $\psi$ . Expressing $\Phi$ in terms of $r$ and $\psi$ , setting $r = R _ { \mathrm { g e o i d } } + h$ , and expanding in powers of $h$ , we find that

$$
\Phi = \Phi _ { \mathrm { g e o i d } } - h g ( \psi ) + O ( h ^ { 2 } ) ,
$$

where $g ( \psi ) : = - \partial \Phi / \partial r$ , given by

$$
\begin{array} { l } { { \displaystyle g ( \psi ) = \frac { G M } { R ^ { 2 } } \biggl [ 1 + \frac { 3 } { 2 } J _ { 2 } - \frac { \omega ^ { 2 } R ^ { 3 } } { G M } + \left( \frac { 2 \omega ^ { 2 } R ^ { 3 } } { G M } - \frac { 3 } { 2 } J _ { 2 } \right) \sin ^ { 2 } \psi \biggr ] } } \\ { { \displaystyle ~ = \frac { G M } { R ^ { 2 } } \biggl [ 1 - \frac { 3 } { 2 } ( 1 - k _ { 2 } ) \zeta + \frac { 3 } { 2 } ( 2 - k _ { 2 } ) \zeta ~ \sin ^ { 2 } \psi \biggr ] , } } \end{array}
$$

is the local acceleration of gravity. For the Earth this evaluates to $g = ( 9 . 7 8 0 3 +$ $0 . 0 5 1 9 \sin ^ { 2 } \psi ) \mathrm { m } / \mathrm { s } ^ { 2 }$ .

# 10.3.4 Temps Atomique International

By definition, tai is the time measured by an atomic clock at rest on the geoid. By virtue of Eq. (10.109), in which we insert ${ \pmb v } = { \bf 0 }$ , we have that the relationship between tai and coordinate time $t$ is given by

$$
d ( \mathrm { T A I } ) = ( 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } ) d t ,
$$

and constancy of $\Phi$ on the geoid guarantees that clocks at rest on the geoid mark time at exactly the same rate.

Actual atomic clocks are typically not situated on the geoid. Instead they tend to be housed in more convenient places at a range of altitudes above sea level, such as Boulder, Colorado (NIST), Washington, DC (USNO), Paris, France (BIPM), and so on. These clocks, therefore, do not keep time at the rate specified by tai, and a correction must be introduced to account for their different placement in the Earth’s potential. To calculate this we return to Eq. (10.109), insert Eq. (10.117), and get

$$
d \tau = \left[ 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } + h g ( \psi ) / c ^ { 2 } \right] d t
$$

for the time $\tau$ measured by a clock at rest at a geographical latitude $\psi$ and elevation $h$ above the geoid. Combining this with Eq. (10.119) produces

$$
d ( \mathrm { T A I } ) = \left[ 1 - h g ( \psi ) / c ^ { 2 } \right] d \tau ,
$$

an equation that relates the measured time $\tau$ to the time standard tai. The correction evaluates to $g / c ^ { 2 } = ( 1 . 0 8 8 2 + 0 . 0 0 5 7 7 \sin ^ { 2 } \psi ) \times 1 0 ^ { - 1 6 } ~ \mathrm { m } ^ { - 1 }$ . Thus, any atomic clock at rest on Earth can have its rate linked directly to tai by a simple correction factor. In practice, tai is defined by an average measurement over an ensemble of the best atomic clocks at different locations around the world, suitably corrected via Eq. (10.121).

The establishment of tai as a precise time standard relies on measurements made by atomic clocks at multiple locations. How are these clocks synchronized? We shall not delve into the practical aspects of this matter, but wish to raise an important question of principle: How can clocks be synchronized in a rotating reference frame?

Suppose that we have a clock at position $B$ that we wish to synchronize with another clock at position $A$ . For simplicity we ignore effects associated with elevation, and assume that both locations are on the geoid. Each clock marks time at the rate indicated by Eq. (10.119), and integration yields $\tau [ A ] = ( 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } ) t$ and $\tau [ B ] = ( 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } ) t + \Delta \tau$ , in which $\Delta \tau$ is an integration constant. The synchronization procedure is meant to achieve $\Delta \tau = 0$ , so that $\tau [ B ] = \tau [ A ]$ .

A possible way of establishing synchronization would be to rely on a portable clock that is transported slowly from $A$ to $B$ . This clock is initially synchronized with the $A$ -clock, and during its trip to $B$ it marks time at a rate $d \tau ^ { * }$ given by Eq. (10.109),

$$
d \tau ^ { * } = \left[ 1 - { \frac { 1 } { c ^ { 2 } } } { \Big ( } \boldsymbol { v } \cdot ( \boldsymbol { \omega } \times \boldsymbol { r } ) + \Phi _ { \mathrm { g e o i d } } { \Big ) } \right] d t ,
$$

in which $\mathbf { } r ( t )$ is the path of the portable clock; we have neglected the ${ \scriptstyle { \frac { 1 } { 2 } } } v ^ { 2 }$ term under the assumption that the transport is slow. Integrating this for the whole trip, which begins at time $t _ { 1 }$ and ends at time $t _ { 2 }$ , we find that

$$
\tau _ { 2 } ^ { * } - \tau _ { 1 } ^ { * } = \big [ 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } \big ] ( t _ { 2 } - t _ { 1 } ) - \frac { 1 } { c ^ { 2 } } \int _ { A } ^ { B } ( \pmb { \omega } \times \pmb { r } ) \cdot d \pmb { r } .
$$

Because the clock is synchronized with the $A$ -clock at the beginning of the trip, we have that $\tau _ { 1 } ^ { * } = \tau _ { 1 } [ A ] = ( 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } ) t _ { 1 }$ , in which $\tau _ { 1 } [ A ]$ is the time recorded by the $A$ -clock at departure. Expressing $t _ { 2 }$ in terms of $\tau _ { 2 } [ B ]$ , the time recorded by the $B$ -clock at the arrival of the portable clock, and solving for $\tau _ { 2 } ^ { * }$ , we find that

$$
\tau _ { 2 } ^ { * } = \tau _ { 2 } [ B ] - \Delta \tau - \frac { 1 } { c ^ { 2 } } \int _ { A } ^ { B } ( \pmb { \omega } \times \pmb { r } ) \cdot d \pmb { r } .
$$

We see that the path integral prevents us from achieving synchronization ( $\Delta \tau = 0$ ) by doing the obvious, setting the $B$ -clock so that $\tau _ { 2 } [ B ] = \tau _ { 2 } ^ { * }$ . Instead, we must synchronize the $B$ -clock by setting

$$
\tau _ { 2 } [ B ] = \tau _ { 2 } ^ { * } + \frac { 1 } { c ^ { 2 } } \int _ { A } ^ { B } ( \pmb { \omega } \times \pmb { r } ) \cdot d \pmb { r } ;
$$

a correction must be applied to reflect the transport of the clock in the rotating frame of the Earth. Note that the path integral is independent of $\pmb { v }$ ; the effect survives even in the limit of a quasi-static transport.

This failure of simple-minded synchronization, known as the Sagnac effect after the French physicist Georges Sagnac (1869–1926), is a consequence of the Earth’s rotation. For a path $r$ confined to the geoid, is it is easy to show that

$$
{ \frac { 1 } { c ^ { 2 } } } \int _ { A } ^ { B } ( \omega \times r ) \cdot d r = { \frac { \omega R ^ { 2 } } { c ^ { 2 } } } \int _ { A } ^ { B } \sin ^ { 2 } \theta d \phi ,
$$

and the integral (multiplied by $R ^ { 2 }$ ) is twice the area swept out by a line joining the center of the Earth to a projection of the path onto the equatorial plane. For a closed path around the equator, the Sagnac term amounts to 207 ns, and the effect is very noticeable. Note that the Sagnac effect disappears when the clock is transported along a meridian, so that $d \phi = 0$ .

Clock synchronization on a rotating Earth can nevertheless be achieved provided that one applies the Sagnac correction, which requires one to keep careful track of the path taken by the portable clock. As a result, all clocks on the geoid can be consistently synchronized to a single master clock, which could be situated in Washington DC, Greenwich UK, Beijing China, or at the North Pole (the latter being the most politically neutral). This method now forms the basis for all terrestrial timekeeping.

# 10.3.5 Orbiting clocks

Atomic clocks orbiting the Earth have become an important part of our lives thanks to the Global Positioning System (GPS; see Box 10.4), which would fail utterly if it did not account for relativistic effects in timekeeping. To analyze the behavior of orbiting clocks we put ourselves in the non-rotating geocentric frame $( { \bar { t } } , { \bar { { \boldsymbol { x } } } } )$ and use Eq. (10.107),

$$
d \tau [ \mathrm { o r b i t } ] = \bigg [ 1 - \frac { 1 } { c ^ { 2 } } \bigg ( \frac { 1 } { 2 } \bar { \upsilon } ^ { 2 } + U \bigg ) \bigg ] d \bar { t } ,
$$

to relate the clock’s proper time $\tau$ [orbit] to the coordinate time $\bar { t }$ ; here $\bar { \pmb { v } }$ is the satellite’s orbital velocity and $U$ is the Earth’s gravitational potential. In this case we may ignore the multipolar deformations, which are small at the high altitudes considered here $( r \simeq 4 R _ { \oplus }$ for GPS satellites), and set $U = G M / r$ .

Each satellite moves on a Keplerian orbit around the Earth, and we may rely on the orbital equations derived in Sec. 3.2.4 to integrate Eq. (10.127). It is convenient to employ a representation of the motion in terms of the eccentric anomaly $u$ , as displayed in Eqs. (3.34) and (3.35). We have that $\bar { r } = a ( 1 - e \cos u )$ and $\bar { v } ^ { 2 } = ( G M / a ) ( 1 + e \cos u ) / ( 1 - e \cos u ) ,$ where $a$ and $e$ are the semi-major axis and eccentricity, respectively, and the eccentric anomaly is related to $\bar { t }$ by Kepler’s equation

$$
\bar { t } - T = \sqrt { \frac { a ^ { 3 } } { G M } } ( u - e \sin u ) ,
$$

in which $T$ is the time of perigee passage. It follows that

$$
\frac { 1 } { 2 } \bar { v } ^ { 2 } + \frac { G M } { r } = \frac { 3 } { 2 } \frac { G M } { a } + \frac { 2 G M } { a } \frac { e \cos u } { 1 - e \cos u } ,
$$

and substitution within Eq. (10.127) yields

$$
\tau \mathrm { [ o r b i t ] } = \biggl ( 1 - { \frac { 3 } { 2 } } { \frac { G M } { c ^ { 2 } a } } \biggr ) \bar { t } - { \frac { 2 G M } { c ^ { 2 } a } } \sqrt { \frac { a ^ { 3 } } { G M } } e \sin u + \tau _ { 0 } ,
$$

where $\tau _ { 0 }$ is a constant of integration set by synchronization of the orbiting clock.

The time marked by the orbiting clock is expressed in terms of the coordinate time $\bar { t }$ . To complete the description we should relate it to the time measured by a clock at rest (or moving slowly inside a car) at a geographical latitude $\psi$ and elevation $h$ on the surface of

the Earth. The translation is provided by Eq. (10.120), which integrates to

$$
\tau [ \mathrm { g r o u n d } ] = \big [ 1 - \Phi _ { \mathrm { g e o i d } } / c ^ { 2 } + h g ( \psi ) / c ^ { 2 } \big ] \bar { t } + \tau _ { 1 } ,
$$

with $\tau _ { 1 }$ another constant of integration. Making the substitution in Eq. (10.130), we find that

$$
\begin{array} { l } { { \displaystyle \tau [ \mathrm { o r b i t } ] = \left\{ 1 - \frac { 1 } { c ^ { 2 } } \bigg [ \frac { 3 } { 2 } \frac { G M } { a } - \Phi _ { \mathrm { g e o i d } } + h g ( \psi ) \bigg ] \right\} \tau [ \mathrm { g r o u n d } ] } } \\ { { \displaystyle ~ - \frac { 2 G M } { c ^ { 2 } a } \sqrt { \frac { a ^ { 3 } } { G M } } e \sin u + \tau _ { 2 } , } } \end{array}
$$

in which $u$ is now expressed implicitly as a function of $\tau$ [ground].

Equation (10.132) relates the time measured by a clock on board a satellite to the time measured by a clock on the ground. The first group of terms describes a constant difference between the clock rates. The first correction term $- 3 G M / ( 2 c ^ { 2 } a )$ comes with a negative sign, and represents a time-dilation effect produced by the orbital motion. The second term $+ \Phi _ { \mathrm { g e o i d } } / c ^ { 2 }$ comes with a positive sign, and represents a gravitational blueshift associated with the transfer of the time signal from high to low altitude. The third term $- h g ( \psi ) / c ^ { 2 }$ is an elevation-dependent correction, and its sign depends on the sign of $h$ . The second group of terms is a time-dependent modulation of $\tau$ [orbit] associated with the orbital eccentricity; this effect is usually very small, because the GPS satellites are in highly circular orbits $( e \sim 0 . 0 1 )$ . A typical orbit has a period of 12 hours, corresponding to $a = 2 6$ , $6 3 0 \mathrm { k m }$ , or about $4 . 2 R _ { \oplus }$ , and this implies that the geoid term dominates the orbital term in the constant rate factor. This means that the gravitational blueshift dominates time dilation, so that GPS clocks tick faster than clocks on the geoid by a factor of $4 . 4 6 7 \times 1 0 ^ { - 1 0 }$ , or by about 38.6 microseconds per day. Note that the geoid and satellite terms cancel each other at an orbital radius of about $1 . 5 R _ { \oplus }$ , and that time dilation would dominate for a lower orbit.

<table><tr><td>Box 10.4</td><td>Global Positioning System</td></tr><tr><td></td><td>The Global Positioning System(GPS)has becomeaubiquitous fixtureofourdailylives,being foundin many smartphones and helping us navigate our cars in unfamiliar neighborhoods.The GPS consists of 24 satellites orbiting the Earth,with groups offour satellites on six distinct orbital planes oriented at 55 degrees relative to Earth&#x27;s equatorial plane.The system operates in such a way that at least four satelites are visible above the horizon at any given time.Each satelite harbours a very acurate atomicclock; the accumulated time lapse of a given clock overa fullday is measured in nanoseconds. The system is operated by the United States Department of Defense; it was deployed for military purposes before it was made available to civilians.</td></tr></table>

Each GPS satellite emits a sequence of radio pulses that contain information about the satellite’s position and the time of emission. This information is used by a receiving unit on Earth to determine its own position. The receiver acquires the position $r _ { A }$ and time of emission $t _ { A }$ from each of the four visible satellites. Ignoring the relativistic effects described in the main text, the receiver determines its own position $r$ and time $t$ by solving the system of equations

$$
c ^ { 2 } ( t - t _ { A } ) ^ { 2 } = | { \boldsymbol { r } } - { \boldsymbol { r } } _ { A } | ^ { 2 } ;
$$

solving for t is necessary because the clock inside the receiver is not nearly as accurate as the atomic clocks, and because this clock has not been synchronized with sufficient precision. In this way the receiving unit can determine its position on Earth with an accuracy of a few meters and local time with an accuracy of 30 nanoseconds.

As explained in the main text, relativistic effects such as time dilation and gravitational blueshift must be taken into account for the successful operation of the GPS. For example, according to Eq. (10.132), the size of the constant rate difference between $\tau$ [orbit] and $\tau$ [ground] is given by

$$
{ \frac { 3 } { 2 } } { \frac { G M } { c ^ { 2 } a } } - { \frac { \Phi _ { \mathrm { g e o i d } } } { c ^ { 2 } } } = - 4 . 4 6 4 7 \times 1 0 ^ { - 1 0 } .
$$

This may seem like a small number, but in the course of a full day it builds up to a time difference of $3 8 . 6 \mu s$ . This is much, much larger than the intrinsic accuracy of the atomic clocks, and translates (after multiplication by c) to a distance error of $1 2 \mathrm { k m }$ . Think of Einstein the next time your GPS saves you from an unfortunate detour in downtown Los Angeles.

# 10.3.6 Timing of binary pulsars

As a final application of timekeeping in general relativity, we examine binary pulsars, those important astrophysical systems that have been so fruitful in delivering tests of our favorite theory. A binary pulsar is a two-body system, of which at least one is an active pulsar that emits radio pulses at very regular intervals. The pulses are received on Earth by a radio telescope, and a careful timing allows the astronomer to extract detailed information about the orbital motion of the binary pulsar, including its post-Newtonian aspects. The companion star is generally assumed to be a compact object as well, either a neutron star or a white dwarf (both types of system have been observed) or a black hole (no evidence so far).

We wish to relate the proper time of emission $\tau _ { e }$ of a radio pulse, as measured by a clock attached to the pulsar, to its arrival time $t _ { a }$ , as measured by a remote observer. Our timing model will include all the relevant relativistic effects, but for simplicity we shall neglect a number of effects that are also important to the radio astronomer. These include the motion of the observer relative to the barycenter of the binary system, the aberration associated with the rotational motion of the pulsar, and the dispersion of the radio pulses in the interstellar medium.

We consider a binary system consisting of a pulsar of mass $M _ { 1 }$ and position $r _ { 1 }$ , and a companion of mass $M _ { 2 }$ and position $r _ { 2 }$ . The motion of the binary is described in the system’s barycentric frame, and the observer is situated at a remote position $r _ { \mathrm { o b s } }$ relative to the barycenter; the observer is imagined to be at rest at that position, and her clock measures coordinate time $t$ . As usual we let $r : = r _ { 1 } - r _ { 2 }$ denote the orbital separation, and $r : = | r |$ .

Our first task is to relate the pulsar’s proper time $\tau$ to the coordinate time $t$ . Working to the leading, Newtonian order, the relation is provided by Eq. (10.107), which we evaluate at the position of the pulsar. Removing the overbars, which are no longer required, we have

that

$$
d \tau = \left[ 1 - \frac { 1 } { c ^ { 2 } } \bigg ( \frac { 1 } { 2 } v _ { 1 } ^ { 2 } + U \bigg ) + { \cal O } ( c ^ { - 4 } ) \right] d t ,
$$

in which ${ \pmb v } _ { 1 }$ is the pulsar’s velocity and $U$ is the binary’s gravitational potential, consisting of the pulsar’s own constant potential $U _ { 1 }$ and the companion’s potential $G M _ { 2 } / r$ . To integrate this we once again make use of the Keplerian relations obtained in Sec. 3.2.4. After some algebra we find that

$$
\frac { 1 } { 2 } v _ { 1 } ^ { 2 } + \frac { G M _ { 2 } } { r } = \frac { G M _ { 2 } } { a } \bigg ( \frac { 2 M _ { 1 } + 3 M _ { 2 } } { 2 m } + \frac { M _ { 1 } + 2 M _ { 2 } } { m } \frac { e \cos u } { 1 - e \cos u } \bigg ) ,
$$

in which $m : = M _ { 1 } + M _ { 2 }$ is the total mass, $a$ is the binary’s semi-major axis, $e$ its eccentricity, and $u$ is the eccentric anomaly, which is related to $t$ by Kepler’s equation. Making the substitution and integrating, we find that

$$
\tau = \bigg ( 1 - \frac { 2 M _ { 1 } + 3 M _ { 2 } } { 2 m } \frac { G M _ { 2 } } { c ^ { 2 } a } - \frac { U _ { 1 } } { c ^ { 2 } } \bigg ) t - \frac { M _ { 1 } + 2 M _ { 2 } } { m } \sqrt { \frac { a ^ { 3 } } { G m } } \frac { G M _ { 2 } } { c ^ { 2 } a } e \sin u + \tau _ { 0 } ,
$$

in which $\tau _ { 0 }$ is a constant of integration. In practical applications $\tau _ { 0 }$ is unobservable, and so is the constant factor in front of $t$ , which can be absorbed into a re-definition of the pulsar’s intrinsic frequency, which is unknown; the key information is contained in the time-dependent term, which is proportional to the binary’s eccentricity.

Equation (10.135) allows us to relate the proper time of emission $\tau _ { e }$ to the coordinate time $t _ { e }$ . We must now obtain the relation between $t _ { e }$ and the time of arrival $t _ { a }$ , by calculating the time required by an electromagnetic signal to travel from the pulsar at $r _ { 1 }$ to the observer at $r _ { \mathrm { o b s } }$ . The work was already carried out in Sec. 10.2.5, and Eq. (10.100) informs us that

$$
c ( t _ { a } - t _ { e } ) = | { \boldsymbol { r } } _ { \mathrm { { o b s } } } - { \boldsymbol { r } } _ { 1 } | + \frac { 2 G M _ { 2 } } { c ^ { 2 } } \ln \biggl [ \frac { | { \boldsymbol { r } } _ { \mathrm { { o b s } } } - { \boldsymbol { r } } _ { 2 } | + ( { \boldsymbol { r } } _ { \mathrm { { o b s } } } - { \boldsymbol { r } } _ { 2 } ) \cdot { \boldsymbol { k } } } { r + r \cdot { \boldsymbol { k } } } \biggr ] + { \cal O } ( c ^ { - 4 } ) ,
$$

where

$$
k : = \frac { r _ { \mathrm { o b s } } - r _ { 1 } } { | r _ { \mathrm { o b s } } - r _ { 1 } | }
$$

is the direction of propagation. Some work was required to go from Eq. (10.100) to Eq. (10.136). First, the version here accounts for the fact that the delay is produced by the companion at $r _ { 2 }$ instead of a body situated at the spatial origin of the coordinate system. And second, the factor $b ^ { 2 }$ in Eq. (10.100) was factorized as $b ^ { 2 } = ( r - r \cdot k ) ( r + r \cdot k )$ , a relation that follows directly from the definition $\pmb { b } : = \pmb { r } - ( \pmb { r } \cdot \pmb { k } ) \pmb { k }$ . Our result can be simplified if we recognize that the observer is situated at a large distance from the binary system. With $r _ { \mathrm { { o b s } } } / r _ { 1 } \gg 1$ and $r _ { \mathrm { { o b s } } } / r _ { 2 } \gg 1$ , we find that Eq. (10.136) reduces to

$$
c ( t _ { a } - t _ { e } ) = { r _ { \mathrm { 0 b s } } } - { n _ { \mathrm { 0 b s } } } \cdot { r _ { 1 } } - \frac { 2 G M _ { 2 } } { c ^ { 2 } } \ln \biggl [ \frac { ( 1 + { n _ { \mathrm { 0 b s } } } \cdot { n } ) r } { 2 r _ { \mathrm { 0 b s } } } \biggr ] + { \cal O } ( c ^ { - 4 } ) ,
$$

in which ${ \pmb n } : = { \pmb r } / r$ and $\pmb { n } _ { \mathrm { o b s } } : = { r } _ { \mathrm { o b s } } / r _ { \mathrm { o b s } } .$ . It is understood that $r$ and $r _ { 1 }$ are evaluated at time $t = t _ { e }$ .

We now wish to put Eq. (10.138) in a more concrete form. We adopt the point of view of the astronomer, who looks up at the binary system and assigns to it the orbital parameters $( a , e , \iota , \Omega , \omega )$ , in which $\iota$ is the orbital inclination, $\Omega$ the longitude of the ascending node, and $\omega$ the longitude of pericenter. She erects a fundamental $( X , Y , Z )$ frame and aligns it in such a way that the $Z$ -axis points toward the binary. In this description we have that $n _ { \mathrm { o b s } } =$ $- e _ { Z }$ , and $\pmb { n }$ is given by Eq. (3.42); with this it follows that ${ \pmb n } _ { \mathrm { o b s } } \cdot { \pmb n } = - \sin \iota \sin ( \omega + f )$ , in which $f$ is the orbit’s true anomaly.

In the term ${ \pmb n } _ { 0 } \mathrm { \ldots } \mathrm { \pmb r } _ { 1 }$ on the right-hand side of Eq. (10.138) we insert the post-Newtonian description of the orbital motion given by Eq. (10.21). In the logarithmic term we may insert the usual Keplerian relations. Making the substitutions, we arrive at

$$
\begin{array} { l } { { c ( t _ { a } - t _ { e } ) = r _ { \mathrm { o b s } } + \sin \iota \sin ( \omega + f _ { e } ) a _ { 1 } ( 1 - e _ { 1 } \cos u _ { e } ) } } \\ { { \displaystyle ~ - ~ \frac { 2 G M _ { 2 } } { c ^ { 2 } } \ln \Bigl \{ \bigl [ 1 - \sin \iota \sin ( \omega + f _ { e } ) \bigr ] ( 1 - e \cos u _ { e } ) \Bigr \} + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

in which $a _ { 1 }$ and $e _ { 1 }$ are the pulsar’s post-Newtonian orbital parameters, as defined in Eq. (10.38), $f _ { e }$ is the true anomaly at the time of emission, and $u _ { e }$ is the eccentric anomaly. The relation between $f _ { e }$ and $u _ { e }$ is given by Eq. (10.34), and the relation between $u _ { e }$ and $t _ { e }$ is expressed by Eq. (10.24).

Our task is completed. With Eq. (10.135) we relate the proper time of emission $\tau _ { e }$ of a radio pulse to the coordinate time $t _ { e }$ , and with Eq. (10.139) we relate $t _ { e }$ to the arrival time $t _ { a }$ . Combining these expressions, we obtain the desired relation between $t _ { a }$ and $\tau _ { e }$ . The relation is provided in a rather implicit form, but the building blocks are all sufficiently simple that it can easily be turned into a practical timing tool.

In Sec. 10.1.4 we pointed out that the measurement of the pericenter advance in a binarypulsar system yields a very accurate determination of the system’s total mass. The timing formulae of Eqs. (10.135) and (10.139) provide additional information. The time-dependent term in Eq. (10.135) involves a different combination of $M _ { 1 }$ and $M _ { 2 }$ , and combining this measurement with a pericenter-advance measurement returns values for each mass. When the Shapiro delay is significant (which requires a nearly edge-on orbit), the amplitude of the delay reveals the companion mass $M _ { 2 }$ straight away, while its detailed shape depends on sin ι. Such independent measurements of the masses in many binary pulsars turn out to give consistent results to high precision, affirming the correctness of the general relativistic description of the physics. In Chapter 12 we uncover yet another way to measure the masses, via the effect of gravitational radiation damping.

# 10.4 Spinning bodies

As relativistic effects go, those associated with a body’s spin tend to be suppressed compared to the effects reviewed in Sec. 10.1. For example, in the spin–orbit contributions to the equations of motion, Eqs. (9.189) or Eq. (9.245), a relativistic factor $v _ { A } ^ { 2 } / c ^ { 2 }$ has been replaced by $S _ { A } v _ { A } / ( M _ { A } c ^ { 2 } r _ { A B } )$ , which is smaller by a factor of order $( V _ { A } / v _ { A } ) ( R _ { A } / r _ { A B } )$ 、 where $V _ { A }$ is the equatorial rotation velocity of the spinning body and $R _ { A }$ is its radius. The rotation velocity for a body is limited by the Keplerian velocity $( G M _ { A } / R _ { A } ) ^ { 1 / 2 }$ , at which matter on the equator is no longer bound to the body, and the orbital velocity is itself comparable to $( G M _ { A } / r _ { A B } ) ^ { 1 / 2 }$ , so that one would expect a spin–orbit effect to be smaller than an orbital post-Newtonian effect by a factor of order $( R _ { A } / r _ { A B } ) ^ { 1 / 2 }$ . In the context of the theory of motion developed in Chapter 9, in which each body was assumed to be small compared with the inter-body separation, this is necessarily a small number. Furthermore, most bodies do not rotate at anything close to the Keplerian limit. For example, the Earth’s equatorial rotational velocity is approximately $0 . 5 \mathrm { k m / s }$ , which is 16 times smaller than the Keplerian limit. Even the most rapidly spinning pulsar rotates at less than half its Keplerian limit. The sole exception to this rule is a rapidly rotating black hole, for which the effective $V _ { A }$ can be comparable to the speed of light.

So it would seem that to detect the effects of spin in the solar system would be hopeless, unless we could relax the constraint that $R _ { A } \ll r _ { A B }$ , which means putting one body close to the surface of the rotating body. We can do this and retain the validity of the equations of motion obtained in Chapter 9 by demanding that the first body have a negligible mass. This is the context of Gravity Probe B, in which gyroscopes are placed on a low Earth orbit with $r _ { A B } = R _ { A } + 6 5 0 ~ \mathrm { k m }$ , and of the LAGEOS experiment, which tracked satellites on near-Earth orbits with $r _ { A B } \approx 2 R _ { A }$ . On the other hand, by virtue of the remarkable accuracy afforded by pulsar timing, relativistic spin–orbit effects have been measured in a number of binary pulsar systems.

# 10.4.1 Frame dragging and Gravity Probe B

Gravity Probe B will very likely go down in the history of science as one of the most ambitious, difficult, expensive, and controversial relativity experiments ever performed.1 In fact, the list of superlatives associated with the project is formidable: it fabricated the world’s most perfect spheres, it achieved the lowest magnetic fields, it built the best dragfree control, and so on. All these achievements and more were essential to the successful measurement of the minute precession of a spinning body as it orbits the Earth.

# Precession of a gyroscope

We consider a binary system that consists of the Earth, with mass $M _ { \oplus }$ and spin $\pmb { S } _ { \oplus }$ , and a gyroscope of negligible mass and spin $s$ . The gyroscope orbits the Earth, and its spin precesses. The relevant equation was listed in Sec. 9.5.6. According to Eq. (9.198), we have that $d { \pmb S } / d t = { \pmb \Omega } \times { \pmb S }$ , where $\pmb { \Omega } = \pmb { \Omega } [ \mathrm { s o } ] + \pmb { \Omega } [ \mathrm { s s } ]$ is the precessional angular velocity decomposed in spin–orbit and spin–spin contributions, with

$$
\begin{array} { l } { { \displaystyle \Omega [ \mathrm { s o } ] = \frac { 3 } { 2 } \frac { G M _ { \oplus } } { c ^ { 2 } r ^ { 2 } } n \times v } , } \\ { { \displaystyle \Omega [ \mathrm { s s } ] = \frac { G } { c ^ { 2 } r ^ { 3 } } \Big [ 3 ( S _ { \oplus } \cdot n ) n - S _ { \oplus } \Big ] , } } \end{array}
$$

in which $r = r n$ is the gyroscope’s orbital position, and $\pmb { v }$ its orbital velocity.

We describe the orbital motion in the fundamental $( X , Y , Z )$ frame introduced in Sec. 3.2.5. The frame is oriented in such a way that the $X – Y$ plane coincides with the Earth’s equatorial plane, and $\pmb { S } _ { \oplus }$ points in the $Z$ -direction. We place the gyroscope on a circular orbit of radius $a$ , inclination $\iota$ , and longitude of ascending node $\Omega$ . The direction to the gyroscope is given by Eq. (3.42),

$$
\begin{array} { r l } & { \pmb { n } = \left[ \cos \Omega \cos ( \omega + f ) - \cos \iota \sin \Omega \sin ( \omega + f ) \right] \pmb { e } _ { X } } \\ & { \quad ~ + \left[ \sin \Omega \cos ( \omega + f ) + \cos \iota \cos \Omega \sin ( \omega + f ) \right] \pmb { e } _ { Y } } \\ & { \quad ~ + \sin \iota \sin ( \omega + f ) \pmb { e } _ { Z } , } \end{array}
$$

in which $f = 2 \pi t / P$ is the orbital phase; $P = 2 \pi a ^ { 3 / 2 } ( G M _ { \oplus } ) ^ { - 1 / 2 }$ is the orbital period.

It is convenient to introduce a vectorial basis $( e _ { p } , e _ { q } , e _ { z } )$ adapted to the gyroscope’s orbital plane. The normal to the plane is given by Eq. (3.45),

$$
\pmb { e } _ { z } = \sin \iota \sin \Omega \pmb { e } _ { X } - \sin \iota \cos \Omega \pmb { e } _ { Y } + \cos \iota \pmb { e } _ { Z } .
$$

As a second basis vector we select

$$
\begin{array} { r } { \pmb { e } _ { p } = \cos \Omega \pmb { e } _ { X } + \sin \Omega \pmb { e } _ { Y } , } \end{array}
$$

which lies in the plane and points toward the ascending node. And as a third vector, orthogonal to the first two, we get

$$
\pmb { e } _ { q } = - \cos \iota \sin \Omega \pmb { e } _ { X } + \cos \iota \cos \Omega \pmb { e } _ { Y } + \sin \iota \pmb { e } _ { Z } .
$$

In terms of the orbital basis we have that ${ \pmb { n } } = \cos f e _ { p } + \sin f e _ { q }$ , $\pmb { e } _ { Z } = \sin \iota \pmb { e } _ { q } + \cos \iota \pmb { e } _ { z }$ , and $\pmb { n } \times \pmb { v } = \sqrt { G M _ { \oplus } / a } \pmb { e } _ { z }$ .

We insert the foregoing relations within the precessional angular velocities, obtaining

$$
\begin{array} { r l } & { \Omega [ \mathrm { s o } ] = \displaystyle \frac { 3 } { 2 c ^ { 2 } a } \left( \frac { G M _ { \oplus } } { a } \right) ^ { 3 / 2 } e _ { z } , } \\ & { \Omega [ \mathrm { s s } ] = \displaystyle \frac { G S _ { \oplus } } { c ^ { 2 } a ^ { 3 } } \left[ \frac { 3 } { 2 } \sin \iota \sin 2 f e _ { p } + \frac { 1 } { 2 } \sin \iota ( 1 - 3 \cos 2 f ) e _ { q } - \cos \iota e _ { z } \right] , } \end{array}
$$

and substitute these into the precession equation. Because the changes in the gyroscope spin $s$ are small, we may insert its initial value $\pmb { S } _ { 0 }$ on the right-hand side of the equation. And because we are interested only in the secular evolution of the spin, we average the precession equation over a complete cycle of the orbital motion. We arrive at

$$
\begin{array} { l } { \displaystyle \left. \frac { d \boldsymbol { S } } { d t } \right. _ { \mathrm { s o } } = \frac { 3 } { 2 c ^ { 2 } a } \left( \frac { G M _ { \oplus } } { a } \right) ^ { 3 / 2 } \boldsymbol { e } _ { z } \times \boldsymbol { S } _ { 0 } , } \\ { \displaystyle \left. \frac { d \boldsymbol { S } } { d t } \right. _ { \mathrm { s s } } = \frac { G S _ { \oplus } } { c ^ { 2 } a ^ { 3 } } \left( \frac { 1 } { 2 } \sin \iota e _ { q } - \cos \iota e _ { z } \right) \times \boldsymbol { S } _ { 0 } . } \end{array}
$$

Inserting the appropriate numerical values for the Earth, the equations reveal that the precessional angular velocities are given by

$$
\begin{array} { l } { { \displaystyle \langle \Omega [ \mathrm { s o } ] \rangle = \frac { 3 } { 2 c ^ { 2 } a } \bigg ( \frac { G M _ { \oplus } } { a } \bigg ) ^ { 3 / 2 } = 8 . 4 3 \bigg ( \frac { R _ { \oplus } } { a } \bigg ) ^ { 5 / 2 } \mathrm { a s / y r } , } } \\ { { \displaystyle \langle \Omega [ \mathrm { s s } ] \rangle = \frac { G S _ { \oplus } } { c ^ { 2 } a ^ { 3 } } = 0 . 1 0 9 \bigg ( \frac { R _ { \oplus } } { a } \bigg ) ^ { 3 } \mathrm { a s / y r } ; } } \end{array}
$$

we see that the spin–orbit precession amounts to in a few arcseconds per year, while the spin–spin precession is smaller by almost two orders of magnitude.

# Geodetic precession; Schiff precession

The spin–orbit precession is frequently called the “geodetic precession” of a spin vector. Its underlying origin is the fact that spacetime is curved in the vicinity of the Earth, and that parallel transport of a vector around a closed path returns a vector that points in a direction that differs from the initial direction. The change is given by the product of components of the curvature tensor with the vector itself, multiplied by the area enclosed by the orbit. In order of magnitude we have that $\delta S \sim ( \mathrm { R i e m a n n } ) ( \mathrm { a r e a } ) S _ { 0 }$ , and with Riemann $\sim G M _ { \oplus } / ( c ^ { 2 } a ^ { 3 } )$ , area $\sim a ^ { 2 }$ , $P \sim \sqrt { a ^ { 3 } / ( G M _ { \oplus } ) }$ , we find that

$$
\left. \frac { d S } { d t } \right. _ { \mathrm { s o } } \sim \frac { \delta S } { P } \sim \frac { 1 } { c ^ { 2 } a } \biggl ( \frac { G M _ { \oplus } } { a } \biggr ) ^ { 3 / 2 } S _ { 0 } ,
$$

in agreement with the more detailed calculation. The geodetic precession is independent of the orientation of the orbit, but is maximized when the spin $\pmb { S } _ { 0 }$ lies within the orbital plane; it vanishes when the spin is parallel to $e _ { z }$ .

The spin–spin precession is also called the “Schiff precession” of a spin vector. In 1960, Leonard Schiff calculated the spin–orbit and spin–spin precessions of a gyroscope and suggested the possibility of measuring them. Unbeknownst to Schiff, a researcher at the US Pentagon named George Pugh had performed the same calculations a few months earlier. Pugh was working for the Weapons Systems Evaluation Group, assessing the use of high-performance gyroscopes in missile and aircraft guidance. He wondered how large the relativistic effects would be, and what it would take of a space experiment to measure them. Pugh’s classified work could not be published in the open literature, and so Schiff was initially given credit for the idea; only later was Pugh’s work discovered and recognized. It is worth noting that all this occurred in the very early days of space exploration, only two years after the launch of Sputnik.

The phrases “frame dragging” and “Lense–Thirring effects” are sometimes attached to the spin–spin precession of a spin vector. Lense and Thirring were the first, in 1918, to examine the metric of a rotating body in the weak-field limit, and to work out the effects of rotation on the orbits of bodies, a topic to which we return in the next subsection. They did not consider the motion of gyroscopes explicitly, but the basic phenomenon of frame dragging applies to them just as well: an inertial frame with axes defined by an array of perpendicularly oriented gyroscopes will precess about the axis defined by $\pmb { \Omega }$ [ss] relative to an inertial frame at infinity. This phenomenon is directly linked to the dragging of a particle moving on a geodesic near a rotating body, as discussed back in Sec. 9.5.3.

The Maxwell-like formulation of post-Newtonian theory summarized in Box. 8.1 provides additional insight into the phenomenon of spin–spin precession. We recall that a rotating body produces a gravitomagnetic field $\pmb { { B } } _ { g } = \pmb { { \nabla } } \times \pmb { { A } } _ { g }$ , in which $A _ { g } = - 4 U / c ^ { 2 }$ is a rescaled version of the post-Newtonian vector potential. For a spinning Earth at the spatial origin of the coordinate system, we have that

$$
A _ { g } = \frac { 2 G } { c ^ { 2 } } \frac { \pmb { x } \times \pmb { S } _ { \oplus } } { | \pmb { x } | ^ { 3 } } ,
$$

and this produces a dipolar gravitomagnetic field given by

$$
B _ { g } = - \frac { 2 G } { c ^ { 2 } | { \pmb x } | ^ { 3 } } \bigg [ \frac { 3 ( { \pmb S } _ { \oplus } \cdot { \pmb x } ) { \pmb x } } { | { \pmb x } | ^ { 2 } } - { \pmb S } _ { \oplus } \bigg ] .
$$

Comparing this with Eq. (10.140), we see that $\begin{array} { r } { \pmb { \Omega } [ \mathrm { s s } ] = - \frac { 1 } { 2 } \pmb { B } _ { g } ( \pmb { x } = \pmb { r } ) } \end{array}$ . In electrodynamics, the torque exerted by a magnetic field on a magnetic dipole moment $\pmb { m }$ is ${ \pmb { \tau } } = { \pmb { m } } \times { \pmb { B } }$ . In gravity we would expect that the torque exerted by a gravitomagnetic field on a gravitomagnetic dipole moment $\begin{array} { r } { \pmb { m } _ { g } : = \frac { 1 } { 2 } \pmb { S } } \end{array}$ is given by

$$
\pmb { \tau } = \pmb { m } _ { g } \times \pmb { B } _ { g } = \left( \frac { 1 } { 2 } \pmb { S } \right) \times \left( - 2 \pmb { \Omega } [ \mathrm { s s } ] \right) = \pmb { \Omega } [ \mathrm { s s } ] \times \pmb { S } ,
$$

in agreement with the precession equation.

# Gravity Probe B

We now return to the description of the Gravity Probe B experiment. In order to maximize the spin–orbit precession, we align the gyroscope so that it points in the orbital plane. We write

$$
{ \pmb S } _ { 0 } = S _ { 0 } ( \cos \psi e _ { p } + \sin \psi e _ { q } ) ,
$$

with $\psi$ denoting the angle between $\pmb { S } _ { 0 }$ and the line of nodes. It is then easy to show that

$$
\begin{array} { c } { { \displaystyle \left. \frac { d { \pmb S } } { d t } \right. _ { \mathrm { s s } } \propto \left( \frac 1 2 \sin \iota e _ { q } - \cos \iota e _ { z } \right) \times \pmb S _ { 0 } } } \\ { { \displaystyle \propto \cos \iota \sin \psi e _ { p } - \cos \iota \cos \psi e _ { q } - \frac 1 2 \sin \iota \cos \psi e _ { z } , } } \end{array}
$$

and that the length of this vector is proportional to $\begin{array} { r } { [ 1 - \sin ^ { 2 } \iota ( 1 - \frac { 1 } { 4 } \cos ^ { 2 } \psi ) ] ^ { 1 / 2 } } \end{array}$ It becomes clear that the effect is maximized by setting $\iota = 0$ and therefore placing the orbit in the Earth’s equatorial plane. This, however, is not the optimal choice for the operations of Gravity Probe B, because in this case $\langle d S / d t \rangle _ { \mathrm { S O } }$ and $\langle d S / d t \rangle _ { \mathrm { S S } }$ are both aligned in the direction of $\boldsymbol { e } _ { z } \times \boldsymbol { S } _ { 0 }$ . In this orientation the spin–spin precession would be very difficult to distinguish from the dominant spin–orbit precession, and the configuration does not permit a clean measurement of each effect separately. A much better strategy is to select an orbit that produces spin–orbit and spin–spin precessions that are perpendicular to each other. It is easy to show that the inner product between $\langle d S / d t \rangle _ { \mathrm { S O } }$ and $\langle d S / d t \rangle _ { \mathrm { S S } }$ is proportional to cos $\iota$ , and setting $\begin{array} { r } { \iota = \frac { \pi } { 2 } } \end{array}$ forces this to be zero. The optimal orbit, therefore, is a polar orbit. With these specifications the spin-precession equations become

$$
\begin{array} { l } { { \displaystyle { \bigg \langle \frac { d S } { d t } \bigg \rangle _ { \mathrm { s o } } = \frac { 3 } { 2 c ^ { 2 } a } \bigg ( \frac { G M _ { \oplus } } { a } \bigg ) ^ { 3 / 2 } \Big ( - \sin \psi e _ { p } + \cos \psi e _ { q } \Big ) } , } } \\ { { \displaystyle { \bigg \langle \frac { d S } { d t } \bigg \rangle _ { \mathrm { s s } } = - \frac { G S _ { \oplus } } { 2 c ^ { 2 } a ^ { 3 } } \cos \psi e _ { z } } . } } \end{array}
$$

In this geometry the spin–orbit precession is in the orbital plane, and the spin–spin precession is normal to the plane.

The Gravity Probe B spacecraft was launched into an almost perfectly circular polar orbit at an altitude of $6 4 2 \mathrm { k m }$ , with the orbital plane parallel to the direction of a guide star known as IM Pegasi. The spacecraft contained four spheres made of fuzed quartz, all spinning about the same axis (two were spun in the opposite direction), which was oriented to be in the orbital plane, pointing toward the guide star. An onboard telescope pointed continuously at the guide star, and the direction of each spin was compared with the direction to the star, which was at a declination of $1 6 ^ { \circ }$ relative to the Earth’s equatorial plane. With $\psi$ chosen such that the angle between $e _ { q }$ (now parallel to the Earth’s rotation axis) and the spins is equal to $7 4 ^ { \circ }$ , we obtain a value of 6630 mas/yr for the spin–orbit precession, and of $3 8 \mathrm { \ m a s / y r }$ for the spin–spin precession, the first in the orbital plane (in the north-south direction) and the second perpendicular to it (in the east-west direction).

In order to reduce the non-relativistic torques on the rotors to an acceptable level, the rotors were fabricated to be both spherical and homogenous to better than a few parts in 10 million. Each rotor was coated with a thin film of niobium, and the experiment was conducted at cryogenic temperatures inside a dewar containing 2200 litres of superfluid liquid helium. As the niobium film becomes a superconductor, each rotor develops a magnetic moment parallel to its spin axis. Variations in the direction of the magnetic moment relative to the spacecraft were then measured using current loops surrounding each rotor. As the spacecraft orbits the Earth, the aberration of light from the guide star causes an artificial but predictable change in direction between the rotors and the onboard telescope; this was an essential tool for calibrating the conversion between the voltages read by the current loops and the actual angle between the rotors and the guide star.

The spacecraft was launched on April 20, 2004, and the mission ended in September 2005, as scheduled, when the remaining liquid helium boiled off. Although all subsystems of the spacecraft and the apparatus performed extremely well, they were not perfect. Calibration measurements carried out during the mission, both before and after the science phase, revealed unexpectedly large torques on the rotors, believed to be caused by electrostatic interactions between surface imperfections on the niobium films and the spherical housings surrounding each rotor. These effects and other anomalies greatly contaminated the data and complicated its analysis, but finally, in October 2010, the Gravity Probe B team announced that the experiment had successfully measured both the geodetic and frame-dragging precessions. The outcome was in agreement with general relativity, with a precision of $0 . 3 \%$ for the spin–orbit precession, and $20 \%$ for the spin–spin precession.

# 10.4.2 Frame dragging and LAGEOS satellites

We next consider the influence of the Earth’s spin on the orbital motion of a satellite, which we take to have a negligible mass and spin. The spin–orbit contribution to the relative acceleration between the satellite and the Earth is given by Eq. (9.252), and with our assumptions we find that it becomes

$$
a [ \mathrm { s o } ] = \frac { 2 G } { c ^ { 2 } r ^ { 3 } } \bigg [ 3 ( \pmb { n } \times \pmb { v } ) \cdot \pmb { S } _ { \oplus } \pmb { n } + 3 ( \pmb { n } \cdot \pmb { v } ) \pmb { n } \times \pmb { S } _ { \oplus } - 2 \pmb { v } \times \pmb { S } _ { \oplus } \bigg ] ,
$$

in which $r$ is the satellite’s position relative to Earth, $\pmb { v }$ its velocity, and as usual ${ \pmb n } : = { \pmb r } / r$ . Recalling that $\pmb { h } : = \pmb { r } \times \pmb { v } = h \pmb { e } _ { z }$ is the conserved angular momentum (per unit reduced mass) of the Keplerian motion, and writing $\pmb { S } _ { \oplus } = S _ { \oplus } \pmb { e } _ { Z }$ , the spin–orbit acceleration becomes

$$
\begin{array} { l } { \displaystyle { \boldsymbol { a } [ \mathrm { s o } ] = - \frac { 2 G S _ { \oplus } } { c ^ { 2 } r ^ { 3 } } \bigg [ 2 { \boldsymbol { v } } \times { \boldsymbol { e } } _ { Z } - 3 \dot { { \boldsymbol { r } } } { \boldsymbol { n } } \times { \boldsymbol { e } } _ { Z } - \frac { 3 h } { r } ( { \boldsymbol { e } } _ { z } \cdot { \boldsymbol { e } } _ { Z } ) { \boldsymbol { n } } \bigg ] , } } \end{array}
$$

with ${ \dot { r } } : = n \cdot v$ denoting the radial component of the velocity vector.

We take the spin–orbit acceleration as a perturbing force $f$ to be inserted in the formalism of osculating Keplerian orbits reviewed in Sec. 3.3.2. A short computation using $v =$ $\dot { r } { \pmb n } + ( h / r ) { \pmb \lambda }$ reveals that the components of $f$ in the orbital basis $( n , \lambda , e _ { z } )$ introduced in Sec. 3.2.2 are

$$
\begin{array} { r l } & { \mathcal { R } = \displaystyle \frac { 2 G S _ { \oplus } } { c ^ { 2 } r ^ { 3 } } \frac { h } { r } e _ { z } \cdot e _ { Z } , } \\ & { \mathcal { S } = \displaystyle - \frac { 2 G S _ { \oplus } } { c ^ { 2 } r ^ { 3 } } \dot { r } e _ { z } \cdot e _ { Z } , } \\ & { \mathcal { W } = \displaystyle \frac { 2 G S _ { \oplus } } { c ^ { 2 } r ^ { 3 } } \bigg ( \dot { r } \lambda \cdot e _ { Z } + \frac { 2 h } { r } n \cdot e _ { Z } \bigg ) . } \end{array}
$$

In this we insert the Keplerian relations $h = \sqrt { G m p } , ~ r = p / ( 1 + e \cos f ) , ~ \dot { r } =$ $\sqrt { G m / p } e \sin f$ , in which $m \simeq M _ { \oplus }$ is the total mass, $p$ the semi-latus rectum, $e$ the eccentricity, and $f$ is the true anomaly. We also insert the vectorial relations listed in Sec. 3.2.5, according to which $e _ { z } \cdot e _ { Z } = \cos \iota , \lambda \cdot e _ { Z } = \sin \iota \cos ( \omega + f )$ , and $\pmb { n } \cdot \pmb { e } _ { Z } = \sin \iota \sin ( \omega + f )$ ， in which $\iota$ is the orbit’s inclination relative to Earth’s equatorial plane, and $\omega$ is the longitude of perigee. Finally, we insert the components of the perturbing force in the osculating equations listed in Sec. 3.3.2, refer to Eqs. (3.69), and integrate over a complete orbital cycle to obtain the secular changes in the Keplerian orbital elements.

The final outcome of this sequence of steps is the statement that $\Delta p = \Delta e = \Delta \iota = 0$ , but that

$$
\begin{array} { r l } & { \Delta \omega = - 1 2 \pi \frac { G S _ { \oplus } } { \sqrt { G M _ { \oplus } p ^ { 3 } } c ^ { 2 } } \cos \iota , } \\ & { \Delta \Omega = 4 \pi \frac { G S _ { \oplus } } { \sqrt { G M _ { \oplus } p ^ { 3 } } c ^ { 2 } } . } \end{array}
$$

These results can be combined to give

$$
\Delta \omega + \cos \iota \Delta \Omega = - 8 \pi \frac { G S _ { \oplus } } { \sqrt { G M _ { \oplus } p ^ { 3 } } c ^ { 2 } } \cos \iota ,
$$

Table 10.1 Orbital elements of laser-ranged satellites.   

<table><tr><td> Satellite</td><td>Semi-major axis (km)</td><td>Orbital period (min)</td><td>Eccentricity</td><td>Inclination to equator (°)</td><td>Mass (kg)</td></tr><tr><td>LAGEOSI</td><td>12,257</td><td>225</td><td>0.0045</td><td>109.84</td><td>407</td></tr><tr><td>LAGEOS II</td><td>12,168</td><td>223</td><td>0.0135</td><td>52.64</td><td>405</td></tr><tr><td> LARES</td><td>7,821</td><td>115</td><td>0.0007</td><td>69.5</td><td>387</td></tr></table>

which describes the secular advance of the perigee relative to a fixed reference direction – the $X$ -axis – in the fundamental plane. The nodal advance $\Delta \Omega$ over a complete orbit can be converted to an averaged rate of advance by dividing by the orbital period, and inserting numerical values appropriate for an Earth-orbiting satellite, we obtain

$$
\left( \frac { d \Omega } { d t } \right) _ { \mathrm { s e c } } = 0 . 2 1 8 8 { \left( \frac { R _ { \oplus } } { a } \right) } ^ { 3 } ( 1 - e ^ { 2 } ) ^ { - 3 / 2 } \mathrm { a s } / \mathrm { y r } .
$$

This very small effect on the satellite’s motion, measured in fractions of arcseconds per year, is not beyond the reach of modern spacecraft tracking using lasers. In particular, a pair of “Laser Geodynamics Satellites” (LAGEOS) are ideal for this purpose. Launched in 1976 and 1992, the satellites are massive spheres, $6 0 \ \mathrm { c m }$ in diameter and weighing about $4 0 0 ~ \mathrm { k g }$ , placed in nearly circular orbits with semi-major axes approximately equal to $2 R _ { \oplus }$ (the precise orbital elements are listed in Table 10.1). The spheres are covered with laser retroreflectors, conical mirrors designed to reflect a laser beam back to the same direction from which it came. Because of their large mass-to-area ratio, the spheres are less affected by atmospheric drag than other satellites at similar altitudes. This, combined with the high precision of laser ranging (which routinely achieves millimeter-level precision), means that their orbits can be determined extremely precisely. The LAGEOS satellites were launched primarily to carry out studies in geodesy and geodynamics, but it was soon recognized that they were potentially capable of measuring the relativistic nodal advance, which under the stated conditions amounts to approximately 32 mas/yr.

A significant challenge in performing the experiment comes from the fact that the deformed figure of the Earth produces a huge contribution to the nodal advance. The effect of oblateness on orbital motion was examined back in Sec. 3.4.3, and an application of these results to the LAGEOS orbits reveals that the Newtonian perturbation produces an advance of approximately 120 degrees per year, more than 10 million times larger than the relativistic advance. To measure the relativistic contribution to $1 0 \%$ accuracy requires a very precise subtraction of the Newtonian effect, which requires knowledge of the Earth’s quadrupole moment $\mathit { J } _ { 2 } \sim 1 0 ^ { - 3 }$ ) to better than a part in $1 0 ^ { 5 }$ . The higher multipole moments $J _ { 4 } , J _ { 6 } ,$ , and so on, also contribute substantially to the nodal advance. The Earth’s multipole moments were not known sufficiently well at the time of the launch of the first LAGEOS satellite to permit a clean measurement of the relativistic contribution.

After the launch of LAGEOS I in 1976, it was recognized by Italian physicist Ignazio Ciufolini and others, building on an earlier idea by Stanford physicists Richard van Patten and Francis Everitt, that the Newtonian and relativistic contributions to $\Delta \Omega$ could actually be distinguished from one another. The key observation is that the Newtonian contribution is proportional to cos $\iota$ , while the relativistic contribution is independent of inclination. If a second LAGEOS satellite were to have an inclination supplementary to that of LAGEOS I, so that $\iota _ { 2 } = 1 8 0 ^ { \circ } - \iota _ { 1 }$ , then the Newtonian advance would be equal and opposite for the two satellites. (This turns out to be true for the contributions of all even- multipole moments; see Exercise 3.5.) This means that if one measured the nodal advance of both satellites simultaneously and added them together, the large Newtonian effect would cancel out exactly, leaving the relativistic effect in full view.

Ciufolini and other relativists campaigned vigorously to have LAGEOS II launched with $\iota _ { 2 } = 7 0 . 1 6 ^ { \circ }$ , but other considerations prevailed in the end. LAGEOS II was launched with $\iota _ { 2 } = 5 2 . 6 4 ^ { \circ }$ , mainly to optimize coverage by the world’s network of laser tracking stations, which was important for geophysics and geodynamics research. The fall-back option was then to combine the data from the two satellites as they were. One could still eliminate the largest Newtonian contribution coming from $J _ { 2 }$ with a suitable linear combination of the two measured nodal advances, thereby revealing the relativistic contribution and those coming from higher-order multipole moments, whose uncertainties would contribute to the error made in measuring the relativistic effect. For a time, Ciufolini and collaborators tried to include a third piece of data, the perigee advance of LAGEOS II (which has a small eccentricity), as a way to also eliminate $J _ { 4 }$ , but this turned out to be plagued with systematic errors that were large and hard to control.

But then along came CHAMP and GRACE. Europe’s CHAMP (Challenging Minisatellite Payload) and NASA’s GRACE (Gravity Recovery and Climate Experiment) missions, launched in 2000 and 2002, respectively, use precision tracking of spacecraft to measure variations in the Earth’s gravity on scales as small as several hundred kilometers, with unprecedented accuracies. GRACE consists of a pair of satellites flying in close formation (200 kilometers apart) on polar orbits. Each satellite carries an on-board accelerometer to measure non-gravitational perturbations, a satellite to satellite K-band radar to measure variations in the Earth’s gravity gradient on short scales, and a GPS tracking unit to measure larger scale variations. With the dramatic improvements on $J _ { \ell }$ obtained by CHAMP and GRACE, Ciufolini and his colleagues could now treat $J _ { 4 }$ and higher multipole moments as known, and use the two LAGEOS nodal advances to determine $J _ { 2 }$ and the relativistic contribution. The final outcome was a successful test of the relativistic prediction at the level of $10 \%$ accuracy, which was later confirmed by independent analyses of the LAGEOS/GRACE/CHAMP data.

On February 13, 2012, a third laser-ranged satellite, known as LARES (Laser Relativity Satellite) was launched by the Italian Space Agency. Its inclination was $6 9 . 5 ^ { \circ }$ , very close to the required supplementary angle relative to LAGEOS I, and its eccentricity was very nearly zero (see Table 10.1). Combining data from all three satellites with continually improving Earth data from GRACE, the LARES team led by Ciufolini hopes to achieve a test of frame-dragging at the $1 \%$ level.

# 10.4.3 Binary systems of spinning bodies

In our final exploration of the influence of spin in post-Newtonian gravity, we examine the motion of a binary system of spinning bodies.

# Equations of motion and conserved quantities

The equations of motion for the relative orbit and spin vectors of a binary system were derived back in Sec. 9.5.9. The relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ is expressed as ${ \pmb a } =$ $\pmb { a } [ 0 \mathrm { P N } ] + \pmb { a } [ 1 \mathrm { P N } ] + \pmb { a } [ \mathrm { s o } ] + \pmb { a } [ \mathrm { s s } ] + O ( c ^ { - 4 } ) ,$ , with the two first terms given by Eq. (10.1), the spin–orbit contribution given by

$$
\begin{array} { c } { { a [ \mathrm { s o } ] = \displaystyle \frac { G } { c ^ { 2 } r ^ { 3 } } \bigg \{ \displaystyle \frac { 3 } { 2 } ( n \times v ) \cdot ( 3 \sigma + 4 S ) n + \displaystyle \frac { 3 } { 2 } ( n \cdot v ) n \times ( 3 \sigma + 4 S ) } } \\ { { - v \times ( 3 \sigma + 4 S ) + \displaystyle \frac { 3 \lambda } { 2 } \Big [ n ( n \times v ) \cdot \sigma - ( n \cdot v ) n \times \sigma \Big ] \bigg \} , } } \end{array}
$$

and the spin–spin contribution given by

$$
a [ s s ] = - \frac { 3 G } { \mu c ^ { 2 } r ^ { 4 } } \Big [ ( S _ { 1 } \cdot S _ { 2 } ) n - 5 ( S _ { 1 } \cdot n ) ( S _ { 2 } \cdot n ) n + ( S _ { 1 } \cdot n ) S _ { 2 } + ( S _ { 2 } \cdot n ) S _ { 1 } \Big ] .
$$

The accelerations are expressed in terms of the combinations $\pmb { \sigma } : = ( M _ { 2 } / M _ { 1 } ) \pmb { S } _ { 1 } +$ $( M _ { 1 } / M _ { 2 } ) S _ { 2 }$ and $\pmb { S } : = \pmb { S } _ { 1 } + \pmb { S } _ { 2 }$ of the spin vectors, and the arbitrary parameter $\lambda$ was introduced back in Sec. 9.5.8 to characterize the choice of representative world line within each body; $m : = { M } _ { 1 } + { M } _ { 2 }$ and $\mu : = M _ { 1 } M _ { 2 } / ( M _ { 1 } + M _ { 2 } )$ are respectively the total and reduced masses of the binary system.

The spin-precession equation for the first body is $d { \pmb S } _ { 1 } / d t = { \pmb \Omega } _ { 1 } \times { \pmb S } _ { 1 }$ with $\pmb { \Omega } _ { 1 } =$ ${ \pmb { \Omega } } _ { 1 } [ \mathrm { s o } ] + { \pmb { \Omega } } _ { 1 } [ \mathrm { s s } ]$ , where

$$
\begin{array} { l } { { \displaystyle \Omega _ { 1 } [ \mathrm { s o } ] = \frac { 2 G \mu } { c ^ { 2 } r ^ { 2 } } \biggl ( 1 + \frac { 3 M _ { 2 } } { 4 M _ { 1 } } \biggr ) n \times v , } } \\ { { \displaystyle \Omega _ { 1 } [ \mathrm { s s } ] = \frac { G } { c ^ { 2 } r ^ { 3 } } \bigl [ 3 ( S _ { 2 } \cdot n ) n - S _ { 2 } \bigr ] , } } \end{array}
$$

are the precessional angular velocities. The equations for the second body are obtained by a simple exchange of labels $1  2$ .

Back in Sec. 10.1.1 we established that the equations of motion $\pmb { a } = \pmb { a } [ 0 \mathrm { P N } ] + \pmb { a } [ 1 \mathrm { P N } ] +$ $O ( c ^ { - 4 } )$ admit a conserved energy $E = \mu \varepsilon$ given by Eq. (10.3), and a conserved angular momentum $L = \mu h$ given by Eq. (10.4). It is possible to extend these results and show that the equations of motion with spin–orbit and spin–spin terms included also admit a conserved energy and a conserved angular momentum. The modified energy (per unit reduced mass) takes the form of $\varepsilon = \varepsilon [ \mathrm { 0 P N } ] + \varepsilon [ \mathrm { 1 P N } ] + \varepsilon [ \mathrm { s o } ] + \varepsilon [ \mathrm { s s } ] + O ( c ^ { - 4 } )$ , with the first two terms as listed previously, the spin–orbit term given by

$$
\varepsilon [ \mathrm { s o } ] = \lambda \frac { G } { c ^ { 2 } r ^ { 2 } } ( \pmb { n } \times \pmb { v } ) \cdot \pmb { \sigma } ,
$$

and the spin–spin term given by

$$
\varepsilon [ \mathrm { s s } ] = - \frac { G } { \mu c ^ { 2 } r ^ { 3 } } \bigg [ { \pmb S } _ { 1 } \cdot { \pmb S } _ { 2 } - 3 ( { \pmb n } \cdot { \pmb S } _ { 1 } ) ( { \pmb n } \cdot { \pmb S } _ { 2 } ) \bigg ] .
$$

Note that the spin–orbit contribution to the conserved energy vanishes when $\lambda = 0$ , that is, when the representative world line is chosen to track the body’s center-of-mass in the barycentric frame (as opposed to the moving frame of each body). The modified total

angular momentum takes the form

$$
\pmb { J } = \pmb { L } + \pmb { S } + O ( c ^ { - 4 } )
$$

with ${ \cal L } = { \cal L } [ 0 \mathrm { P N } ] + { \cal L } [ 1 \mathrm { P N } ] + { \cal L } [ \mathrm { s o } ]$ , where the Newtonian and post-Newtonian terms were given by Eq. (10.4), and the spin–orbit term is given by

$$
\begin{array} { c } { \displaystyle { \pmb { L } [ \mathrm { s o } ] = \frac { G \mu } { 2 c ^ { 2 } r } \pmb { n } \times \left[ \pmb { n } \times ( 3 \pmb { \sigma } + 4 \pmb { S } ) \right] } } \\ { \displaystyle { - \frac { \lambda } { 2 c ^ { 2 } } \bigg [ \frac { G \mu } { r } \pmb { n } \times ( \pmb { n } \times \pmb { \sigma } ) + \frac { \mu } { m } \pmb { v } \times ( \pmb { v } \times \pmb { \sigma } ) \bigg ] ; } } \end{array}
$$

there is no spin–spin contribution to the total angular momentum. The facts that $d \varepsilon / d t = 0$ and $d J / d t = \mathbf { 0 }$ by virtue of the post-Newtonian dynamics can be verified with a straightforward computation involving the complete set of equations of motion; for this purpose it is convenient to also make use of the evolution equation

$$
\frac { d \pmb { S } } { d t } = \frac { G \mu } { 2 c ^ { 2 } r ^ { 2 } } ( \pmb { n } \times \pmb { v } ) \times ( 3 \pmb { \sigma } + 4 \pmb { S } ) + \frac { 3 G } { c ^ { 2 } r ^ { 3 } } \Big [ ( \pmb { S } _ { 1 } \cdot \pmb { n } ) \pmb { n } \times \pmb { S } _ { 2 } + ( \pmb { S } _ { 2 } \cdot \pmb { n } ) \pmb { n } \times \pmb { S } _ { 1 } \Big ]
$$

for the total spin vector.

# Simple precession

To explore the effects produced by the spin–orbit coupling in the equations of motion of a binary system, we examine first the case in which only one of the bodies has spin; this is sometimes called the “simple precession” case. Taking the first body to have spin, and setting $\pmb { S } _ { 2 } = \pmb { 0 }$ , the precession equation for $\pmb { S } = \pmb { S } _ { 1 }$ can be expressed as

$$
\frac { d \boldsymbol { S } } { d t } = \frac { 2 G } { c ^ { 2 } r ^ { 3 } } \bigg ( 1 + \frac { 3 M _ { 2 } } { 4 M _ { 1 } } \bigg ) \boldsymbol { L } [ \boldsymbol { 0 } \boldsymbol { \mathrm { P N } } ] \times \boldsymbol { S } ,
$$

where $L [ 0 \mathrm { P N } ] = \mu r \times v$ is the Newtonian expression for the orbital angular momentum. Expressing $1 + 3 M _ { 2 } / ( 4 M _ { 1 } )$ as ${ \frac { 1 } { 4 } } ( 1 + 3 m / M _ { 1 } )$ , and $\pmb { L } [ \mathrm { 0 P N } ]$ as $J - S + O ( c ^ { - 2 } )$ , we find that the equation becomes

$$
\frac { d \pmb S } { d t } = \frac { G } { 2 c ^ { 2 } r ^ { 3 } } \bigg ( 1 + \frac { 3 m } { M _ { 1 } } \bigg ) \pmb J \times \pmb S ,
$$

in which corrections of order $c ^ { - 4 }$ are neglected. Because $\pmb { J } = \pmb { L } + \pmb { S }$ is conserved, this equation implies that $d { \cal L } / d t = - d { \cal S } / d t$ and is therefore proportional to $\mathbf { \nabla } J \times \mathbf { \nabla } S$ . Replacing $s$ by ${ \pmb J } - { \pmb L }$ in this expression, we arrive at

$$
\frac { d \boldsymbol { L } } { d t } = \frac { \boldsymbol { G } } { 2 c ^ { 2 } r ^ { 3 } } \bigg ( 1 + \frac { 3 m } { M _ { 1 } } \bigg ) \boldsymbol { J } \times \boldsymbol { L }
$$

for the rate of change of the orbital angular momentum. These equations reveal that both $s$ and $\pmb { L }$ precess about a fixed $\pmb { J }$ at a common angular frequency

$$
\Omega _ { \mathrm { p r e c } } = { \frac { G J } { 2 c ^ { 2 } r ^ { 3 } } } \bigg ( 1 + { \frac { 3 m } { M _ { 1 } } } \bigg ) ;
$$

![](images/02e14f9253edfba43e9bdcbbcc1bf62f3c091d5a7d75eca02337ecacb534b04b.jpg)  
Fig. 10.5 Simple precession of L and S about a fixed total angular momentum J.

the precession preserves the angle $\theta _ { L }$ between $\pmb { L }$ and $\pmb { J }$ , and the angle $\theta _ { S }$ between $s$ and $\pmb { J }$ (see Fig. 10.5). The precession of $\pmb { L }$ about $\pmb { J }$ implies that the binary’s orbital plane no longer has a fixed orientation in space, as it does in the Newtonian and spinless post-Newtonian dynamics. The normal to the orbital plane is aligned with $L [ 0 \mathrm { P N } ] = \mu r \times v$ , and because this deviates from $\pmb { L }$ by terms of order $c ^ { - 2 }$ , we see that the orbital plane does not quite follow the precessional motion; there is an extra wobble produced by the spin–orbit contribution to the orbital angular momentum. On average, however, the motion of the orbital plane is described by a steady precession, and this phenomenon has already been encountered in our discussion of the LAGEOS satellites. It is easy to show that the precession angle integrated over a complete orbit corresponds precisely to the nodal advance given by Eq. (10.158).

Simple precession can also occur when both bodies are spinning, but in this case the orbital angular momentum is required to be much larger than the spin angular momenta, and the masses are required to be equal. The demand for a large $\pmb { L }$ is to ensure that the spin–spin coupling continues to be negligible compared to the spin–orbit coupling, and the demand for equal masses is to ensure equality of the precessional angular velocities, which are proportional to $( 1 + 3 m / M _ { 1 } )$ and $( 1 + 3 m / M _ { 2 } )$ , respectively. In such circumstances the precession equations become

$$
\frac { d \pmb { S } _ { 1 } } { d t } \simeq \frac { 7 G } { 2 c ^ { 2 } r ^ { 3 } } L [ 0 \mathrm { p N } ] \times \pmb { S } _ { 1 } , \qquad \frac { d \pmb { S } _ { 2 } } { d t } \simeq \frac { 7 G } { 2 c ^ { 2 } r ^ { 3 } } L [ 0 \mathrm { p N } ] \times \pmb { S } _ { 2 } .
$$

These equations can be combined to give a precession equation for the total spin ${ \pmb S } = { \pmb S } _ { 1 } +$ $\pmb { S } _ { 2 }$ , and the $\pmb { L } [ \mathrm { 0 P N } ]$ factor on the right-hand side can again be expressed as $J - S + O ( c ^ { - 2 } )$ . The result can then be used to derive a precession equation for $\pmb { L }$ , and we arrive at

$$
\frac { d \pmb { S } } { d t } \simeq \frac { 7 G } { 2 c ^ { 2 } r ^ { 3 } } \pmb { J } \times \pmb { S } , \qquad \frac { d \pmb { L } } { d t } \simeq \frac { 7 G } { 2 c ^ { 2 } r ^ { 3 } } \pmb { J } \times \pmb { L } .
$$

These equations imply that $s$ and $\pmb { L }$ both precess around $\pmb { J }$ with a common angular velocity $\Omega _ { \mathrm { p r e c } } = 7 G J / ( 2 c ^ { 2 } r ^ { 3 } )$ .

![](images/60b2bd1a9ca6a8bcecc9e9661ae9c2e9cf023eedd98d8c463156bf7415555f17.jpg)  
Precession of L about a fixed J for two bodies with $M _ { 1 } = 2 M _ { 2 } ,$ , with spins of equal magnitudes whose projections perpendicular to J are initially at right angles.

The precessions remain reasonably simple even when the masses are unequal, provided that we maintain the condition that $\pmb { L }$ is much larger than both $\pmb { S } _ { 1 }$ and $\pmb { S } _ { 2 }$ . In this case the factor ${ \cal L } [ 0 \mathrm { P N } ] \times { \cal S } _ { 1 }$ in $d S _ { 1 } / d t$ can be expressed as $[ J - S _ { 1 } - S _ { 2 } + O ( c ^ { - 2 } ) ] \times S _ { 1 }$ , and since $\pmb { J }$ is dominated by orbital angular momentum, this can be approximated by $J \times \pmb { S } _ { 1 }$ . The resulting equations are

$$
\begin{array} { r l r } & { } & { \displaystyle \frac { d { \pmb S } _ { 1 } } { d t } \simeq \frac { G } { 2 c ^ { 2 } r ^ { 3 } } \bigg ( 1 + \frac { 3 m } { M _ { 1 } } \bigg ) { \pmb J } \times { \pmb S } _ { 1 } , } \\ & { } & { \displaystyle \frac { d { \pmb S } _ { 2 } } { d t } \simeq \frac { G } { 2 c ^ { 2 } r ^ { 3 } } \bigg ( 1 + \frac { 3 m } { M _ { 2 } } \bigg ) { \pmb J } \times { \pmb S } _ { 2 } , } \end{array}
$$

and the spins precess with different angular velocities. The motion of $L = J - S _ { 1 } -$ $\pmb { S _ { 2 } }$ incorporates both precessions, and this leads to a complicated trajectory of the type displayed in Fig. 10.6.

# Spin–spin coupling

Thus far we have considered situations in which the spin–spin aspects of the orbital dynamics could be neglected. To conclude our survey of the dynamics of a binary system of spinning bodies, we examine the conditions under which the spin–spin aspects of the dynamics can become important.

The importance of the spin–spin coupling on body 1 (say) can be measured by the ratio

$$
\frac { \mathrm { s s } } { \mathrm { s o } } : = \frac { \Omega _ { 1 } [ \mathrm { s s } ] } { \Omega _ { 1 } [ \mathrm { s o } ] } ,
$$

in which $\Omega _ { 1 } [ \mathrm { s s } ]$ is the magnitude of the spin–spin precessional angular velocity vector, and $\Omega _ { 1 } [ \mathrm { s o } ]$ the magnitude of the spin–orbit angular velocity. In order of magnitude we have

that $\Omega _ { 1 } [ \mathrm { s o } ] = G L ( 1 + 3 m / M _ { 1 } ) / ( 2 c ^ { 2 } r ^ { 3 } )$ and $\Omega _ { 1 } [ \mathrm { s s } ] = { 2 G S _ { 2 } } / { ( c ^ { 2 } r ^ { 3 } ) }$ , so that

$$
\frac { \mathrm { s s } } { \mathrm { s o } } = \frac { 4 } { 1 + 3 m / M _ { 1 } } \frac { S _ { 2 } } { L } .
$$

To estimate this we take body 2 to have a radius $R _ { 2 }$ and a rotational frequency $\omega _ { 2 }$ , so that $S _ { 2 } \sim M _ { 2 } R _ { 2 } ^ { 2 } \omega _ { 2 }$ . We also let $L \sim \mu r ^ { 2 } \Omega _ { \mathrm { K } }$ , in which $\Omega _ { \mathrm { K } } = \sqrt { G m / r ^ { 3 } }$ is the Keplerian angular velocity of the orbital motion. Making the substitutions, we obtain

$$
\frac { \mathrm { s s } } { \mathrm { s o } } = \frac { 4 m } { 3 m + M _ { 1 } } \biggl ( \frac { R _ { 2 } } { r } \biggr ) ^ { 2 } \frac { \omega _ { 2 } } { \Omega _ { \mathrm { K } } } .
$$

A useful bound on this is obtained by recalling that $\omega _ { 2 }$ is limited by the Keplerian angular velocity at the body’s surface, so that $\omega _ { 2 } < \sqrt { G M _ { 2 } / R _ { 2 } ^ { 3 } }$ . This gives

$$
\frac { \mathrm { s s } } { \mathrm { s o } } < \frac { 4 m } { 3 m + M _ { 1 } } \biggl ( \frac { M _ { 2 } } { m } \biggr ) ^ { 1 / 2 } \biggl ( \frac { R _ { 2 } } { r } \biggr ) ^ { 1 / 2 } .
$$

This bound, together with our usual requirement that $R _ { 2 } \ll r$ , implies that $\mathrm { s s } / \mathrm { s o } \ll 1$ , and that the spin–spin aspects of the dynamics are typically small.

An exception to this rule arises when body 1 is very small (in both size and mass), so that it can approach body 2 without suffering from tidal disruption. In such circumstances Eq. (10.178) simplifies to $\mathrm { s s } / \mathrm { s o } \simeq ( 4 / 3 ) ( \omega _ { 2 } / \Omega _ { \mathrm { K } } )$ , which can be large whenever $\omega _ { 2 }$ is comparable to $\Omega _ { \mathrm { K } }$ . This is precisely the situation for Gravity Probe B: plugging in the angular velocities for the Earth and for a low Earth orbit, we find that ss/so is comparable to the ratio identified in Sec. 10.4.1 between the 43 mas frame-dragging precession and the 6600 mas geodetic precession.

Another exception to the general rule arises in the case of a compact object, a neutron star or a black hole, for which the rotational velocity can approach the speed of light, producing a very large spin. The spin of a compact object scales as

$$
S _ { 2 } = \chi \frac { G M _ { 2 } ^ { 2 } } { c } ,
$$

in which $\chi$ is a dimensionless parameter that ranges between 0 and approximately 0.6 for a neutron star, and between 0 and 1 for a Kerr black hole. Inserting this and $L \sim \mu \sqrt { G m r }$ within Eq. (10.177), we find that

$$
{ \frac { \mathrm { s s } } { \mathrm { s o } } } = { \frac { 4 M _ { 2 } } { 4 M _ { 1 } + 3 M _ { 2 } } } \chi { \sqrt { \frac { G m } { c ^ { 2 } r } } }
$$

for a binary system involving compact objects. For a very tight binary at the natural endpoint of its orbital evolution under gravitational radiation reaction (refer to Chapter 12 below), the spin–spin aspects of the dynamics become important when $r$ drops below approximately $1 0 G m / c ^ { 2 }$ . This is especially true when one of the spins becomes aligned with $\pmb { L }$ so that the spin–orbit term passes through zero. The system then loses its gyroscopic bearing, and $\mathbf { \delta } _ { L , S _ { 1 } }$ , and $\pmb { S } _ { 2 }$ can all precess wildly. The orbital angular momentum can even change sign, so that an initially clockwise orbit flips over and becomes counter-clockwise. These strange gyrations, however, occur in a strong-field regime where post-Newtonian theory is gradually breaking down, and it is only with the advent of numerical relativity that the rich dynamical behavior of spinning binaries could be explored to the fullest extent.

# 10.5 Bibliographical notes

Post-Newtonian celestial mechanics provides a vast field of study that we have sampled only sparsely in this chapter. For a more comprehensive survey the reader is invited to consult the treatises by Soffel (1989) and Brumberg (1991).

The methods introduced in Sec. 10.1.5 to integrate the post-Newtonian equations of motion of a two-body system originate from Damour and Deruelle (1985). The relativistic precession of the line of nodes of the lunar orbit, reviewed in Sec. 10.1.6, was first predicted by de Sitter (1916), and the effect was first measured by Shapiro et al. (1988).

The story of the 1919 eclipse expedition to measure the relativistic deflection of light, mentioned in Sec. 10.2.3, is engagingly told in the book Einstein’s Jury by Jeffrey Crelinsten (2006), and in Daniel Kennefick’s Physics Today article from 2009. The official report on the expedition is published as Dyson, Eddington, and Davidson (1920). The results of lightdeflection measurements carried out by the VLBI between 1979 and 1999 are compiled in Shapiro et al. (2004), and the Hipparcos measurements are reported in Froeschle, Mignard, ´ and Arenou (1997). The “Newtonian” calculation described in Box 10.3, which originates in the independent work of Cavendish and von Soldner, is described in more detail in Will (1988).

The theory of gravitational lenses, touched upon in Sec. 10.2.4, is developed systematically in the excellent monograph by Schneider, Ehlers, and Falco (1992). The discovery of the first lens, in the form of the double quasar $\mathrm { Q 0 9 5 7 + 5 6 1 }$ , was reported by Walsh, Carswell, and Weymann (1979). Results of the MACHO experiment are recorded in Alcock et al. (2000), and the first discovery of an exoplanet via gravitational lensing is described in Bond et al. (2004).

The calculation of the Shapiro time delay (Sec. 10.2.5) was first published in Shapiro (1964), and the results of the first measurement were reported in Shapiro et al. (1968). The improved experiment involving the Cassini spacecraft is described in Bertotti, Iess, and Tortora (2003).

The relativistic aspects of the Global Positioning System, described in Sec. 10.3.5 and Box 10.4, are treated systematically in Neil Ashby’s excellent Living Reviews article from 2003. Our discussion of the timing of binary pulsars in Sec. 10.3.6 borrows heavily from Blandford and Teukolsky (1976) and Damour and Deruelle (1986).

The final results of the Gravity Probe B experiment, described in Sec. 10.4.1, were reported in Everitt et al. (2011). The dragging of inertial frames was first studied by Thirring and Lense (1918), and the calculation of the spin–spin precession was first presented in the open literature in Schiff (1960). The independent classified calculation by Pugh (1959) was later reprinted in 2003. The successful measurement, of the dragging of inertial frames on the orbital motion of the LAGEOS satellites, as described in Sec. 10.4.2, were reported in Ciufolini and Pavlis (2004).

# 10.6 Exercises

10.1 Show that the post-Newtonian energy of Eq. (10.3) and the post-Newtonian angular momentum of Eq. (10.4) are conserved under the two-body dynamics reviewed in Sec. 10.1.1.

10.2 In the formulation of the post-Newtonian two-body problem in Sec. 10.1.3, express the post-Newtonian energy $\varepsilon$ and post-Newtonian angular momentum $\pmb { h }$ explicitly in terms of the osculating orbital elements. Using Eq. (10.14), show that $\varepsilon$ and $\pmb { h }$ are constant at 1pn order.

10.3 Consider the osculating equations (10.14) in the limit of small eccentricity. Show that a circular orbit (an orbit with $r$ constant) does not correspond to $e = 0$ . Find a solution for $p , e _ { : }$ , and $\omega$ that corresponds to a circular post-Newtonian orbit, and give an interpretation of the orbit in the language of osculating Keplerian orbits.

10.4 Calculate the “Newtonian deflection of light” according to the prescription of Box 10.3. Show that the result is half the deflection predicted by general relativity.

10.5 In this problem we formulate alternative expressions for the deflection vector of a gravitational lens.

(a) Show that ${ \pmb { \alpha } } ( { \pmb { \xi } } ) = { \pmb { \nabla } } _ { \pmb { \xi } } \psi$ , in which $\nabla _ { \pmb { \xi } }$ is the gradient operator associated with the vector $\pmb { \xi }$ , and

$$
\psi ( { \pmb \xi } ) = - \frac { 4 G } { c ^ { 2 } } \int \Sigma ( { \pmb \xi } ^ { \prime } ) \ln | { \pmb \xi } - { \pmb \xi } ^ { \prime } | d ^ { 2 } { \pmb \xi } ^ { \prime }
$$

is a deflection potential.

(b) Show that the deflection angle can also be expressed as

$$
\pmb { \alpha } ( \pmb { \xi } ) = \frac { 2 } { c ^ { 2 } } \int \nabla _ { \pmb { \xi } } U d \ell ,
$$

in which $U$ is the Newtonian potential expressed in terms of the coordinates $( \pmb \xi , \ell )$ introduced in Sec. 10.2.4.

10.6 Show that the magnification of the images of a Schwarzschild gravitational lens can be written in the form

$$
\mu _ { \pm } = \frac { 1 } { 1 - ( \theta _ { \mathrm { E } } / \theta _ { \pm } ) ^ { 4 } } ,
$$

in which $\theta _ { \mathrm { E } }$ is the Einstein angle and $\theta _ { \pm }$ are the two solutions to the lens equation.

10.7 Consider a Schwarzschild gravitational lens, and a circularly symmetric source whose center is at an undeflected angle $\beta _ { 0 }$ from the lens in the $x$ direction. Assume that the source has an angular diameter $2 \chi$ , with $\chi < \beta _ { 0 }$ , and model any point on the edge of the source as being on a circle described by $\beta ( \phi ) = ( \beta _ { 0 } + \chi \cos \phi ) \pmb { e } _ { x } +$ $\chi \sin \phi e _ { y }$ , with $\phi$ ranging from 0 to $2 \pi$ .

(a) In the limit $\chi \ll \beta _ { 0 }$ , show that the image is distorted into an ellipse, with a minor axis parallel to the direction of the image displacement, and with the ratio of minor to major axes given by $\beta _ { 0 } / \sqrt { \beta _ { 0 } ^ { 2 } + 4 \theta _ { \mathrm { E } } ^ { 2 } }$ .

(b) As $\chi$ increases for fixed $\beta _ { 0 }$ , show that the ellipse becomes concave, i.e. becomes an arc, when

$$
\frac { \chi } { ( \beta _ { 0 } - \chi ) \sqrt { \beta _ { 0 } ^ { 2 } - \chi ^ { 2 } } } \geq \frac { 1 } { 2 \theta _ { \mathrm { E } } } .
$$

10.8 The Schwarzschild lens is a rather poor model of a gravitational lens produced by a galaxy, and a better approximation of a galactic mass distribution is provided by the Plummer expression

$$
m ( \xi ) = M \frac { ( \xi / \xi _ { c } ) ^ { 2 } } { 1 + ( \xi / \xi _ { c } ) ^ { 2 } } ,
$$

in which $M$ is the total mass of the galaxy, and $\xi _ { c }$ is a “core radius” inside which most of the mass density resides.

(a) Calculate the mass density $\Sigma ( \xi )$ and plot it as a function of $\xi / \xi _ { c }$ .

(b) Show that the lens equation for a Plummer lens is given by

$$
\theta - \bigg ( \frac { \theta _ { \mathrm { E } } } { \theta _ { c } } \bigg ) ^ { 2 } \frac { \theta } { 1 + ( \theta / \theta _ { c } ) ^ { 2 } } = \beta ,
$$

in which $\theta _ { \mathrm { E } }$ is the Einstein angle of Eq. (10.90), and $\theta _ { c } : = \xi _ { c } / D _ { \mathrm { L } }$ (c) The lens equation is now a cubic equation for $\theta$ , and the number of solutions will depend on the sign of the discriminant $\Delta$ : the lens produces three images when $\Delta > 0$ , and a single image when $\Delta < 0$ . Show that the discriminant is given by

$$
\Delta = - 4 \beta ^ { 4 } - \left( 8 + 2 0 \theta _ { \mathrm { E } } ^ { 2 } - \theta _ { \mathrm { E } } ^ { 4 } \right) \beta ^ { 2 } + 4 \left( \theta _ { \mathrm { E } } ^ { 2 } - 1 \right) ^ { 3 } ,
$$

in which $\beta$ and $\theta _ { \mathrm { E } }$ are now expressed in units of $\theta _ { c }$ .

(d) Show that the sign of $\Delta$ is dictated by the parameter $\beta _ { * }$ defined by

$$
\beta _ { * } ^ { 2 } = - 1 - \frac { 5 } { 2 } \theta _ { \mathrm { E } } ^ { 2 } + \frac { 1 } { 8 } \theta _ { \mathrm { E } } ^ { 4 } + \frac { 1 } { 8 } \theta _ { \mathrm { E } } \big ( \theta _ { \mathrm { E } } ^ { 2 } + 8 \big ) ^ { 3 / 2 } ,
$$

so that $\Delta > 0$ when $\beta < \beta _ { * }$ , while $\Delta < 0$ when $\beta > \beta _ { * }$

The Plummer lens therefore produces three images when $\beta$ is smaller than the critical value $\beta _ { * }$ . It is known that the production of an odd number of images is typical in axially symmetric lenses with an extended distribution of mass.

10.9 A rocket is launched from the surface of a body of mass $M$ and radius $R$ on a radial orbit, reaching a maximum distance $r _ { \mathrm { m a x } }$ before returning to the planet. The rocket carries an atomic clock, while an identical clock remains on the body’s surface. During the flight, the clock on the ground emits a signal with a frequency $f _ { 0 }$ , and this signal is received by the rocket with a frequency $f ^ { \prime }$ as measured onboard the rocket. A signal of that same frequency is then generated and returned to the ground (the device that achieves this is called a transponder); there it is measured to have a frequency $f _ { 1 }$ . This is the method used for Doppler tracking. At the same moment as the tracking signal is transponded back, the rocket emits its own signal of frequency $f _ { 0 }$ as measured onboard. This signal is received on the ground, and the frequency is measured to be $f _ { 2 }$ .

(a) Show that

$$
\begin{array} { l } { \displaystyle \frac { f _ { 1 } } { f _ { 0 } } = \frac { 1 - \dot { r } / c } { 1 + \dot { r } / c } + O ( c ^ { - 3 } ) , } \\ { \displaystyle \frac { f _ { 2 } } { f _ { 0 } } = 1 - \frac { \dot { r } } { c } + \frac { G M } { c ^ { 2 } } \left( \frac { 1 } { R } - \frac { 1 } { r _ { \mathrm { m a x } } } \right) + O ( c ^ { - 3 } ) , } \end{array}
$$

where $\dot { r }$ is the radial velocity of the rocket.

(b) Define the combination of frequency ratios $\Delta : = ( f _ { 2 } / f _ { 0 } ) - ( f _ { 1 } / 2 f _ { 0 } ) - 1 / 2$ . Show that this combination eliminates the first-order Doppler effect and is given by

$$
\Delta = \frac { G M } { c ^ { 2 } } \left( \frac { 1 } { R } - \frac { 2 } { r } + \frac { 1 } { r _ { \mathrm { m a x } } } \right) + { \cal O } ( c ^ { - 3 } ) .
$$

Discuss the qualitative behavior of the frequency shift during the experiment.

(c) For the Earth, and for a rocket reaching a maximum altitude of $1 0 0 0 0 { \mathrm { k m } }$ , determine the maximum value of $\Delta$ . This was the basis for the 1976 Gravity Probe A experiment of Robert Vessot and colleagues, using hydrogen maser clocks and a Scout rocket launched from Wallops Island, Virginia. The experiment verified the prediction for $\Delta$ to about 70 parts per million.

10.10 Using the recipe concocted in Sec. 10.3.6, write a computer code that calculates $t _ { a }$ , the time of arrival of a radio pulse emitted by a binary pulsar, as a function of $\tau _ { e }$ , the proper time of emission. The code should have the pulsar’s intrinsic frequency $\omega$ , the masses $M _ { 1 }$ and $M _ { 2 }$ , the post-Newtonian orbital elements $a$ and $e$ , and the positional elements $\iota$ and $\omega$ as input parameters. You have complete latitude over the design and implementation of the algorithm. Be clever!

10.11 This exercise approaches the de Sitter precession of the lunar orbit from a different viewpoint.

(a) Treat the Earth–Moon system as a giant gyroscope with spin $\pmb { S } = \mu \pmb { r } \times \pmb { v }$ , where $\mu$ is the reduced mass. Imagine that this gyroscope is on a circular orbit around the Sun. Show that the spin–orbit precession of $s$ produces the de Sitter precession as given by Eq. (10.44).

(b) Using Eq. (10.42), show that the rate of change of the Moon’s angularmomentum vector $\pmb { h } = \pmb { r } \times \pmb { v }$ can be expressed as

$$
\frac { d \pmb { h } } { d t } = \frac { 3 } { 2 } \frac { G M _ { 3 } } { c ^ { 2 } R ^ { 2 } } \left( \pmb { N } \times \pmb { V } \right) \times \pmb { h } ,
$$

where $M _ { 3 }$ is the mass of the Sun, $R$ the Earth–Sun distance, $N$ a unit vector pointing from the Sun to the Earth, and $V$ the Earth’s velocity. Assume that the orbit of the Earth around the Sun is circular. Compare this result with your simple model in the first part of this exercise. Hint: Any post-Newtonian expression that can be converted to total time derivatives can be absorbed into the definition of $\pmb { h }$ ; be careful to stay within the approximations used to construct Eq. (10.42), which amount to keeping only terms linear in $\pmb { v }$ , the Moon’s velocity relative to Earth.

10.12 The gravitomagnetic viewpoint elaborated in $\mathrm { B o x } 8 . 1 $ provides useful insights into a number of post-Newtonian effects, most notably the behavior of a gyroscope around a rotating body. Review this material and then provide qualitative answers to the following questions, using only “right-hand-rule” techniques and lessons learned from electromagnetism. To keep everything simple, model both the Earth and a gyroscope as loops of matter rotating about an axis perpendicular to the plane of the loop.

(a) Show that the gravitomagnetic field of the Earth has the same dipole form as the magnetic field of a loop of positive charge rotating in the same direction, but with the field lines emanating from the south pole and returning to the north pole.   
(b) A gyroscope (loop) sits in a gravitomagnetic field that is perpendicular to the plane of the loop. Show that the torque on the gyroscope vanishes.   
(c) A gyroscope sits in a gravitomagnetic field that lies in the plane of the loop. Show that the torque $d S / d t$ on the gyroscope is in the direction of $\pmb { S } \times \pmb { B } _ { g }$ , where $s$ is the spin vector of the gyroscope.   
(d) Show that a gyroscope at the Earth’s equator, with its spin axis parallel to the equator, precesses in a direction opposite to the Earth’s rotation. Show that a similar gyroscope at the pole precesses in the same direction as the Earth’s rotation. How do these qualitative conclusions compare with the corresponding precessions derived from Eq. (10.140b)?

10.13 In the formulation of the dynamics of spinning binaries provided in Sec. 10.4.3, show that the energy per unit reduced mass $\varepsilon$ and the total angular momentum $\pmb { J }$ are conserved quantities.

In the preceding three chapters we stayed safely in the near zone and ignored all radiative aspects of the motion of bodies subjected to a mutual gravitational interaction. In this chapter we move to the wave zone and determine the gravitational waves produced by the moving bodies. To achieve this goal we must return to the post-Minkowskian approximation developed in Chapters 6 and 7, because the post-Newtonian techniques of Chapter 8 are necessarily restricted to the near zone.

We begin in Sec. 11.1 by reviewing the notion of far-away wave zone, in which the gravitational-wave field can be extracted from the (larger set of) gravitational potentials $h ^ { \alpha \beta }$ ; we explain how to perform this extraction and obtain the gravitational-wave polarizations $h _ { + }$ and $h _ { \times }$ . In Sec. 11.2 we derive the famous quadrupole formula, the leading term in an expansion of the gravitational-wave field in powers of $v _ { c } / c$ (with $v _ { c }$ denoting a characteristic velocity of the moving bodies); we flesh out this discussion by examining a number of applications of the formula. Section 11.3 is a very long excursion into a computation of the gravitational-wave field beyond the quadrupole formula, in which we add corrections of fractional order $( v _ { c } / c )$ , $( v _ { c } / c ) ^ { 2 }$ , and $( v _ { c } / c ) ^ { 3 }$ to the leading-order expression. The calculations are carried out for a system of $N$ bodies, and they reveal a very interesting physical phenomenon: the fact that the waves propagate not in the fictitious flat spacetime of post-Minkowskian theory, but in a physical spacetime which is curved by the total mass-energy contained in the $N$ -body system. The true waves are delayed with respect to the fictitious waves because they climb out of a gravitational potential well as they travel from the near zone to the wave zone. In Sec. 11.4 we convert the general formalism of the preceding section into concrete expressions for $h _ { + }$ and $h _ { \times }$ by restricting the number of bodies to two; we first derive general expressions for arbitrary (eccentric) motion, and next specialize our results to circular orbits. We conclude the chapter with Sec. 11.5, where we show how to relate the polarizations $h _ { + }$ and $h _ { \times }$ to the output channel of a laser interferometric gravitational-wave detector.

The radiative themes explored in this chapter are developed further in Chapter 12, in which we determine the effects of radiative losses on the motion of an $N$ -body system. This is the phenomenon of radiation reaction, which reveals a direct link between the near zone and the wave zone.

# 11.1 Gravitational-wave field and polarizations

# 11.1.1 Far-away wave zone

The notion of wave zone was first introduced back in Sec. 6.3.2; this is the region of three-dimensional space in which $R : = | { \boldsymbol { x } } |$ is larger than $\lambda _ { c }$ , the characteristic wavelength of the gravitational-wave field. (In previous chapters the length of the position vector was denoted $r$ instead of $R$ ; for our purposes in this chapter we adapt the notation and keep $r$ available for a later assignment.) By far-away wave zone we mean the farthest reaches of the wave zone, a neighborhood of spatial infinity in which the $R ^ { - 1 }$ part of the gravitational potentials $h ^ { \alpha \beta }$ dominates over the parts that fall off as $R ^ { - 2 }$ and faster.

To illustrate these notions, and the distinctions between behavior in the near zone and behavior in the wave zone, we return to the scalar dipole field of Box 6.6,

$$
\psi ( t , \pmb { x } ) = ( \pmb { p } \cdot \pmb { N } ) \bigg ( \frac { \cos \omega \tau } { R ^ { 2 } } - \frac { \omega } { c } \frac { \sin \omega \tau } { R } \bigg ) ,
$$

which is an exact solution to the wave equation $\square \psi = 0$ outside a region of radius $r _ { c }$ that contains the source. The potential has the dimension of an inverse length, and $\pmb { p }$ is a constant vector of order $r _ { c } ; \omega$ is the frequency of oscillation of the dipole, and the characteristic wavelength is $\lambda _ { c } = 2 \pi c / \omega$ . We have re-introduced the retarded-time variable

$$
\tau : = t - R / c
$$

and the unit vector

$$
N : = x / R ,
$$

which points in the direction of the field point $_ x$ . (In previous chapters the unit vector was denoted $\pmb { n }$ instead of $N$ ; here we change the notation and keep $\pmb { n }$ available for a later assignment.) We assume that the dipole is subjected to a slow-motion condition (refer to Sec. 6.3.2), so that $r _ { c } \ll \lambda _ { c }$ . With $t _ { c } = \omega ^ { - 1 }$ denoting a characteristic time scale and $v _ { c } = r _ { c } / t _ { c }$ a characteristic velocity, we have that $r _ { c } / \lambda _ { c } \sim v _ { c } / c \ll 1$ .

The near zone is defined to be the region of space where $R < \lambda _ { c } = 2 \pi c / \omega$ . In the near zone the potential behaves as

$$
\boldsymbol { \psi } = ( \pmb { p } \cdot \pmb { N } ) \frac { \cos \omega t } { R ^ { 2 } } \bigg [ 1 + \frac { 1 } { 2 } \bigg ( \frac { \omega R } { c } \bigg ) ^ { 2 } + \cdot \cdot \cdot \bigg ] ,
$$

and we see that when $R \sim r _ { c }$ , the leading term is corrected by an expression of fractional order $( r _ { c } / \lambda _ { c } ) ^ { 2 } \sim ( v _ { c } / c ) ^ { 2 }$ . We may say that the correction is of 1pn order, and this is the same near-zone behavior that was identified for the gravitational potentials of post-Newtonian theory.

The wave zone is defined to be the region of space where $R > \lambda _ { c } = 2 \pi c / \omega$ . In the wave zone the potential behaves as

$$
\psi = - { \frac { \omega } { c R } } ( { \pmb p } \cdot { \pmb N } ) \bigg ( \sin \omega \tau - { \frac { c } { \omega R } } \cos \omega \tau \bigg ) ,
$$

and we see that the leading term is corrected by an expression of fractional order $\lambda _ { c } / R$ . This correction becomes increasingly irrelevant as $R$ increases beyond $\lambda _ { c }$ , and it is completely negligible in the far-away wave zone, our adopted vantage point in this chapter.

The gravitational-wave field is obtained by evaluating the gravitational potentials $h ^ { \alpha \beta }$ in the far-away wave zone, where we neglect corrections of order $\lambda _ { c } / R \ll 1$ . How good is this approximation? For a source of gravitational waves with a frequency of $1 0 0 \mathrm { H z } \left( \lambda _ { c } \sim \right.$ $3 0 0 0 \mathrm { k m } ,$ ) at a distance of $1 0 0 \mathrm { M p c }$ $( 3 \times 1 0 ^ { 2 1 } ~ \mathrm { k m } )$ , the neglected terms are of order $1 0 ^ { - 1 8 }$ , making this an excellent approximation indeed. Only a subset of the potentials is actually involved: as we shall see below, the gravitational-wave field is the transverse-tracefree (TT) piece of the complete set of potentials, and this is what we aim to calculate in this chapter. We assume that the source of the gravitational field is a bounded distribution of matter subjected to a slow-motion condition, so that it lies well within the near zone.

# 11.1.2 Gravitational potentials in the far-away wave zone

In Chapter 7 we obtained expressions for the gravitational potentials $h ^ { \alpha \beta }$ that are applicable in the wave zone. These expressions were accurate in the second post-Minkowskian approximation of general relativity. From the summary provided in $\mathrm { B o x } 7 . 7$ , we gather that their behavior in the far-away wave zone is given by

$$
\begin{array} { l } { { { h ^ { 0 0 } = \displaystyle \frac { 4 G M } { c ^ { 2 } R } + \frac { G } { c ^ { 4 } R } C ( \tau , N ) , } } } \\ { { { } } } \\ { { { h ^ { 0 j } = \displaystyle \frac { G } { c ^ { 4 } R } D ^ { j } ( \tau , N ) , } } } \\ { { { } } } \\ { { { h ^ { j k } = \displaystyle \frac { G } { c ^ { 4 } R } A ^ { j k } ( \tau , N ) . } } } \end{array}
$$

Here, $M$ is the total gravitational mass, as defined by Eq. (7.63) in the case of a fluid system, or by Eq. (9.132) in the case of an $N$ -body system. The functions $C , D ^ { j }$ , and $A ^ { j k }$ depend on the retarded-time variable $\tau : = t - R / c$ and the unit vector $N : = x / R$ . We shall not need their precise forms just yet. In fact, the validity of Eqs. (11.6) extends beyond the post-Minkowskian domain of Sec. 7.1.4. It is easy to show that these equations provide solutions to the wave equations $\Pi h ^ { \alpha \beta } = 1 6 \pi G \tau ^ { \alpha \beta } / c ^ { 4 }$ provided only that $\tau ^ { \alpha \beta }$ , the effective energy-momentum pseudotensor, falls off at least as fast as $R ^ { - 2 }$ . The impact of the harmonic gauge conditions $\partial _ { \beta } h ^ { \alpha \beta } = 0$ on the solutions is examined below.

Before we proceed we introduce a useful differentiation rule that applies in the far-away far zone:

$$
\partial _ { j } h ^ { \alpha \beta } = - \frac { 1 } { c } N _ { j } \partial _ { \tau } h ^ { \alpha \beta } .
$$

The rule follows from the fact that the potentials depend on the spatial coordinates $x ^ { j }$ through the overall factor of $R ^ { - 1 }$ , and through the dependence of the functions $C , D ^ { j }$ , and $A ^ { j k }$ on $\tau$ and $N$ . Because $\partial _ { j } R ^ { - 1 } = O ( R ^ { - 2 } )$ and $\partial _ { j } N _ { k } = O ( R ^ { - 1 } )$ , the only dependence that matters is in $\tau$ , and we have that $\partial _ { j } \tau = - c ^ { - 1 } \partial _ { j } R = - c ^ { - 1 } N _ { j }$ . This, finally, leads to Eq. (11.7), in which a correction term of order $R ^ { - 2 }$ is omitted.

# 11.1.3 Decomposition into irreducible components

Before we examine the impact of the gauge conditions $\partial _ { \beta } h ^ { \alpha \beta } = 0$ on the gravitational potentials, it is useful to decompose the vector $D ^ { j }$ and the tensor $A ^ { j k }$ into longitudinal and transverse components. The longitudinal direction is identified with $N$ , and the machinery to achieve the decomposition was developed back in Sec. 5.5; it is summarized in $\mathrm { B o x } 5 . 7$ . The decomposition is simplified by the differential rule of Eq. (11.7).

We write

$$
D ^ { j } = D N ^ { j } + D _ { \mathrm { T } } ^ { j } ,
$$

with $D N ^ { j }$ representing the longitudinal part of $D ^ { j }$ , and $D _ { \mathrm { T } } ^ { j }$ its transverse part; the latter is required to satisfy

$$
N _ { j } D _ { \mathrm { T } } ^ { j } = 0 .
$$

The three components of $D ^ { j }$ are therefore partitioned into one longitudinal component $D$ , and two transverse components contained in $D _ { \mathrm { T } } ^ { j }$ ; these are functions of $\tau$ and $N$ . Similarly, we write

$$
A ^ { j k } = \frac 1 3 \delta ^ { j k } { \cal A } + \left( N ^ { j } N ^ { k } - \frac 1 3 \delta ^ { j k } \right) B + N ^ { j } { \cal A } _ { \mathrm { T } } ^ { k } + N ^ { k } { \cal A } _ { \mathrm { T } } ^ { j } + { \cal A } _ { \mathrm { T T } } ^ { j k } ,
$$

which is a decomposition of $A ^ { j k }$ into a trace part $\textstyle { \frac { 1 } { 3 } } \delta ^ { j k } A$ , a longitudinal-tracefree part $( N ^ { j } N ^ { k } - { \textstyle \frac { 1 } { 3 } } \delta ^ { j k } ) B$ , a longitudinal-transverse part $N ^ { j } A _ { \mathrm { T } } ^ { k } + N ^ { k } A _ { \mathrm { T } } ^ { j }$ , and a transverse-tracefree part $A _ { \mathrm { T T } } ^ { j k }$ . We impose the constraints

$$
N _ { j } A _ { \mathrm { T } } ^ { j } = 0
$$

and

$$
N _ { j } A _ { \mathrm { T T } } ^ { j k } = 0 = \delta _ { j k } A _ { \mathrm { T T } } ^ { j k } ,
$$

so that the six independent components of $A ^ { j k }$ are contained in two scalars $A$ and $B$ , two components of a transverse vector $A _ { \mathrm { T } } ^ { j }$ , and two components of a transverse-tracefree tensor $A _ { \mathrm { T T } } ^ { j k }$ . The last term in Eq. (11.10) is called the transverse-tracefree part, or TT part, of $A ^ { j k }$ . As we shall see, the radiative parts of the gravitational potentials are contained entirely within $A _ { \mathrm { T T } } ^ { j k }$ .

# 11.1.4 Harmonic gauge conditions

The harmonic gauge conditions are $c ^ { - 1 } \partial _ { \tau } h ^ { 0 0 } + \partial _ { k } h ^ { 0 k } = 0$ and $c ^ { - 1 } \partial _ { \tau } h ^ { 0 j } + \partial _ { k } h ^ { j k } = 0$ . In the far-away wave zone they simplify to

$$
\partial _ { \tau } \bigl ( h ^ { 0 0 } - h ^ { 0 k } N _ { k } \bigr ) = 0 , \qquad \partial _ { \tau } \bigl ( h ^ { 0 j } - h ^ { j k } N _ { k } \bigr ) = 0 ,
$$

thanks to the differentiation rule of Eq. (11.7). After substituting Eqs. (11.8) and (11.10) into Eqs. (11.6), and these into Eqs. (11.13), we find that the harmonic gauge conditions

$$
\begin{array} { l } { { \displaystyle { C = D } , } } \\ { { \displaystyle { D = \frac { 1 } { 3 } A + \frac { 2 } { 3 } B } , } } \\ { { \displaystyle { D _ { \mathrm { T } } ^ { j } = A _ { \mathrm { T } } ^ { j } } . } } \end{array}
$$

We have set the constants of integration to zero, because an eventual $\tau$ -independent term in $C$ would correspond to an unphysical shift in the total gravitational mass $M$ , while a $\tau$ -independent term in $D ^ { j }$ would be incompatible with the fact that the time-independent part of $h ^ { 0 j }$ is associated with the total angular momentum, and must fall off as $R ^ { - 2 }$ instead of $R ^ { - 1 }$ .

Incorporating these constraints, the gravitational potentials become

$$
\begin{array} { l } { { \displaystyle h ^ { 0 0 } = \frac { 4 G M } { c ^ { 2 } R } + \frac { G } { c ^ { 4 } R } \frac 1 3 \big ( A + 2 B \big ) , } } \\ { { \displaystyle h ^ { 0 j } = \frac { G } { c ^ { 4 } R } \biggl [ \frac 1 3 ( A + 2 B ) N ^ { j } + A _ { \mathrm { T } } ^ { j } \biggr ] , } } \\ { { \displaystyle h ^ { j k } = \frac { G } { c ^ { 4 } R } \biggl [ \frac 1 3 \delta ^ { j k } A + \left( N ^ { j } N ^ { k } - \frac 1 3 \delta ^ { j k } \right) B + N ^ { j } A _ { \mathrm { T } } ^ { k } + N ^ { k } A _ { \mathrm { T } } ^ { j } + A _ { \mathrm { T } } ^ { j k } \biggr ] , } } \end{array}
$$

in which $A , B , A _ { \mathrm { T } } ^ { j }$ , and $A _ { \mathrm { T T } } ^ { j k }$ are functions of $\tau$ and $N$ . We now have a total of six independent quantities: one in $A$ , another in $B$ , two in $A _ { \mathrm { T } } ^ { j }$ , and two more in $A _ { \mathrm { T T } } ^ { j k }$ . The gauge conditions have eliminated four redundant quantities.

# 11.1.5 Transformation to the TT gauge

It is possible, in the far-away wave zone, to specialize the harmonic gauge even further, and to eliminate four additional redundant quantities. We wish to implement a gauge transformation generated by a four-vector field $\zeta ^ { \alpha } ( x ^ { \beta } )$ chosen so as to preserve the harmonic-gauge conditions, $\partial _ { \beta } h ^ { \alpha \beta } = 0$ . We first figure out how such a transformation affects the gravitational potentials $h ^ { \alpha \beta }$ .

We saw back in Sec. 5.5 that when the spacetime metric is expressed as $g _ { \alpha \beta } = \eta _ { \alpha \beta } + p _ { \alpha \beta }$ where $\eta _ { \alpha \beta }$ is the Minkowski metric and $p _ { \alpha \beta }$ is a perturbation, a gauge transformation produces the change

$$
p _ { \alpha \beta }  p _ { \alpha \beta } - \partial _ { \alpha } \zeta _ { \beta } - \partial _ { \beta } \zeta _ { \alpha }
$$

to first order in the small quantities $p _ { \alpha \beta }$ and $\partial _ { \alpha } \zeta _ { \beta }$ , where $\zeta _ { \alpha } : = \eta _ { \alpha \beta } \zeta ^ { \beta }$ ; this is Eq. (5.122). To relate $p _ { \alpha \beta }$ to the gravitational potentials we appeal to Eqs. (7.20), which states that

$$
g _ { \alpha \beta } = \eta _ { \alpha \beta } + h _ { \alpha \beta } - \frac { 1 } { 2 } h \eta _ { \alpha \beta } + O ( h ^ { 2 } ) ,
$$

where $h _ { \alpha \beta } = \eta _ { \alpha \mu } \eta _ { \beta \nu } h ^ { \mu \nu }$ and $h = \eta _ { \mu \nu } h ^ { \mu \nu }$ ; in the far-away wave zone we can neglect the terms quadratic in $h ^ { \alpha \beta }$ , because they fall off as $R ^ { - 2 }$ . We find that

$$
h _ { \alpha \beta } = p _ { \alpha \beta } - \frac { 1 } { 2 } p \eta _ { \alpha \beta } ,
$$

where $p = \eta ^ { \mu \nu } p _ { \mu \nu }$ . It follows that the gauge transformation produces the change

$$
h ^ { \alpha \beta } \to h ^ { \alpha \beta } - \partial ^ { \alpha } \zeta ^ { \beta } - \partial ^ { \beta } \zeta ^ { \alpha } + \left( \partial _ { \mu } \zeta ^ { \mu } \right) \eta ^ { \alpha \beta }
$$

in the gravitational potentials. We next find that $\partial _ { \beta } h ^ { \alpha \beta }  \partial _ { \beta } h ^ { \alpha \beta } - \sqcup \zeta ^ { \alpha }$ and conclude that the harmonic gauge conditions will be preserved whenever the vector field satisfies the wave equation

$$
\begin{array} { r }  \boxed { \begin{array} { r } { \boxed { \begin{array} { r } { \alpha } = 0 . } \end{array} } } \end{array} \end{array}
$$

We wish to preserve the harmonic gauge, and we construct a solution to the wave equation by writing

$$
\begin{array} { l } { { \displaystyle { \xi ^ { 0 } = \frac { G } { c ^ { 3 } R } \alpha ( \tau , N ) + O ( R ^ { - 2 } ) } , } } \\ { { \displaystyle { \xi ^ { j } = \frac { G } { c ^ { 3 } R } \beta ^ { j } ( \tau , N ) + O ( R ^ { - 2 } ) } , } } \end{array}
$$

where $\alpha$ and $\beta ^ { j }$ are arbitrary functions of their arguments, and the factors of $G / c ^ { 3 }$ were inserted for convenience. As before we decompose the vector in terms of its irreducible components,

$$
\beta ^ { j } = \beta N ^ { j } + \beta _ { \mathrm { T } } ^ { j } , \qquad N _ { j } \beta _ { \mathrm { T } } ^ { j } = 0 .
$$

We differentiate $\xi ^ { 0 }$ and $\xi ^ { j }$ using the differentiation rule of Eq. (11.7), and insert the results within Eq. (11.19). After also involving Eqs. (11.15), we eventually deduce that the gauge transformation produces the changes

$$
\begin{array} { l } { { A  A + 3 \partial _ { \tau } \alpha - \partial _ { \tau } \beta , } } \\ { { \ } } \\ { { B  B + 2 \partial _ { \tau } \beta , } } \\ { { \ } } \\ { { A _ { \mathrm { T } } ^ { j }  A _ { \mathrm { T } } ^ { j } + \partial _ { \tau } \beta _ { \mathrm { T } } ^ { j } , } } \\ { { \ } } \\ { { A _ { \mathrm { T T } } ^ { j k }  A _ { \mathrm { T T } } ^ { j k } } } \end{array}
$$

in the irreducible pieces of the gravitational potentials.

We see that the transverse-tracefree part of $A ^ { j k }$ is invariant under the gauge transformation. We see also that $\alpha , \beta$ , and $\beta _ { \mathrm { T } } ^ { j }$ can be chosen so as to set $A , B$ , and $A _ { \mathrm { T } } ^ { j }$ all equal to zero. Implementing this gauge transformation, we arrive at the simplest expression for the gravitational potentials in the far-away wave zone:

$$
\begin{array} { l } { { { h ^ { 0 0 } = \displaystyle \frac { 4 G M } { c ^ { 2 } R } , } } } \\ { { { h ^ { 0 j } = 0 , } } } \\ { { { h ^ { j k } = \displaystyle \frac { G } { c ^ { 4 } R } A _ { \mathrm { T T } } ^ { j k } ( \tau , N ) . } } } \end{array}
$$