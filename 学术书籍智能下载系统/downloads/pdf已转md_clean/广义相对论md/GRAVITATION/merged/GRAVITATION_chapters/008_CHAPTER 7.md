CHAPTER 7

# INCOMPATIBILITY OF GRAVITY AND SPECIAL RELATIVITY

# $\$ 7.1$ .ATTEMPTS TO INCORPORATE GRAVITY INTO SPECIAL RELATIVITY

The discussion of special relativity so far has consistently assumed an absence of gravitational fields. Why must gravity be ignored in special relativity? This chapter describes the difficulties that gravitational fields cause in the foundations of special relativity.After meeting these difficulties,one can appreciate fully the curved-spacetime methods that Einstein introduced to overcome them.

Start, then,with what one already knows about gravity, Newton's formulation of its laws:

$$
\begin{array} { c } { { d ^ { 2 } x ^ { i } / d t ^ { 2 } = - \partial \pmb { \phi } / \partial x ^ { i } , } } \\ { { \nabla ^ { 2 } \pmb { \phi } = 4 \pi G \rho . } } \end{array}
$$

This chapter is entirely Track 2.

It depends on no preceding Track-2 material.

It is not needed as preparation for any later chapter,but will be helpful in Chapter 18 (weak gravitational fields),and in Chapters 38 and 39 (experimental tests and other theories of gravity).

These equations cannot be incorporated as they stand into special relativity. The equation of motion (7.1) for a particle is in three-dimensional rather than four-dimensional form; it requires modification into a four-dimensional vector equation for $d ^ { 2 } x ^ { \mu } / d \tau ^ { 2 }$ .Likewise, the field equation (7.2) is not Lorentz-invariant, since the appearance of a three-dimensional Laplacian operator instead of a four-dimensional d'Alembertian operator means that the potential $\pmb { \phi }$ responds instantaneously to changes in the density $\rho$ at arbitrarily large distances away. In brief, Newtonian gravitational fields propagate with infinite velocity.

Newton's gravitational laws must be modified into four-dimensional, geometric form

One's first reaction to these problems might be to think that they are relatively straightforward to correct. Exercises at the end of this section study some relatively straightforward generalizations of these equations,in which the gravitational potential $\pmb { \phi }$ is taken to be first a scalar, then a vector,and finally a symmetric tensor field. Each of these theories has significant shortcomings,and all fail to agree with observations.The best of them is the tensor theory (exercise 7.3,Box 7.1). which, however,

All straightforward modifications are unsatisfactory

Best modification (tensor theory in flat spacetime)is internally inconsistent:when repaired,it becomes general relativity.

is internally inconsistent and admits no exact solutions. This difficulty has been attacked in recent times by Gupta (1954,1957,1962), Kraichnan (1955), Thirring (1961),Feynman (l963),Weinberg (l965),Deser (l970). They show how the flatspace tensof theory may be modified within the spirit of present-day relativistic field theory to overcome these inconsistencies.By this field-theory route (part 5 of Box 17.2), they arrive uniquely at standard l915 general relativity. Only at this end point does one finally recognize, from the mathematical form of the equations, that what Ostensibly started out as a flat-space theory of gravity is really Einstein's theory, with gravitation being a manifestation of the curvature of spacetime.This book follows Einstein's line of reasoning because it keeps the physics to the fore.

# EXERCISES

# EXERCISES ON FLAT-SPACETIME THEORIES OF GRAVITY

The following three exercises provide a solid challenge. Happily,all three require similar techniques,and a solution to the most difficult one (exercise 7.3) is presented in Box 7.1. Therefore,it is reasonable to proceed as follows.(a) Work either exercise 7.1 (scalar theory of gravity) or 7.2 (vector theory of gravity),skimming exercise 7.3 and Box 7.1 (tensor theory of gravity) for outline and method, not for detail,whenever difficulties arise.(b) Become familiar with the results of the other exercise (7.2 or 7.l) by discussing it with someone who has worked it in detail.(c) Read in detail the solution to exercise 7.3 as presented in Box 7.1,and compare with the computed results for the other two theories. (d) Develop computational power by checking some detailed computations from Box 7.1.

# Exercise 7.1. SCALAR GRAVITATIONAL FIELD, $\pmb { \phi }$

A.Consider the variational principle $\delta I = 0$ ,where

$$
I = - m \int e ^ { \phi } \left( - \eta _ { \alpha \beta } \frac { d z ^ { \alpha } } { d \lambda } \frac { d z ^ { \beta } } { d \lambda } \right) ^ { 1 / 2 } d \lambda ,
$$

Here $m = ( { \tt r e s t \ m a s s } )$ and $z ^ { \alpha } ( \lambda ) =$ (parametrized world line) for a test particle in the scalar gravitational field $\pmb { \phi }$ . By varying the particle's world line,derive differential equations governing the particle's motion.Write them using the particle's proper time as the path parameter,

$$
d \tau = \Big ( - \eta _ { \alpha \beta } \frac { d z ^ { \alpha } } { d \lambda } \frac { d z ^ { \beta } } { d \lambda } \Big ) ^ { 1 / 2 } d \lambda ,
$$

so that $u ^ { \alpha } = d z ^ { \alpha } / d \tau$ satisfies $u ^ { \alpha } u ^ { \beta } \eta _ { \alpha \beta } = - 1$

B.Obtain the field equation for ${ \pmb \phi } ( { \pmb x } )$ implied by the variational principle $\delta I = 0$ ,where $\begin{array} { r } { I = \int \mathcal { L } \ d ^ { 4 } x } \end{array}$ and

$$
\mathcal E = - \frac { 1 } { 8 \pi G } \eta ^ { \alpha \beta } \frac { \partial \phi } { \partial x ^ { \alpha } } \frac { \partial \phi } { \partial x ^ { \beta } } - \int m e ^ { \phi } \hat { \delta } ^ { 4 } [ \pmb { x } - \pmb { z } ( \tau ) ] d \tau .
$$

Show that the second term here gives the same integral as that studied in part A (equation 7.3).

Discussion: The field equations obtained describe how a single particle of mass m generates the scalar field.If many particles are present, one includes in $\mathcal { E }$ a term $- \int m e ^ { \phi } \hat { \delta } ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] d \tau$ for each particle.

C. Solve the field equation of part B,assuming a single source particle at rest. Also assume that $e ^ { \phi } = 1$ is an adequate approximation in the neighborhood of the particle. Then check this assumption from your solution;i.e., what value does it assgn to $e ^ { \phi }$ at the surface of the earth?(Units with $c = 1$ are used throughout; one may also set $G = 1$ ,if one wishes.)

D. Now treat the static, spherically symmetric field $\pmb { \phi }$ from part C as the field of the sun acting as a given external field in the variational principle of part A, and study the motion of a planet determined by this variational principle. Constants of motion are available from the spherical symmetry and time-independence of the integrand.Use spherical coordinates and assume motion in a plane. Derive a formula for the perihelion precession of a planet.

E.Pass to the limit of a zero rest-mass particle in the equations of motion of part A. Do this by using a parameter $\lambda$ different from proper time,so chosen that $k ^ { \mu } = \mathcal { \bar { d } } x ^ { \mu } / d \lambda$ is the energy-momentum vector,and by taking the limit $m \longrightarrow 0$ with $k ^ { 0 } = \gamma m = E$ remaining finite (so $u ^ { 0 } = \gamma \longrightarrow \infty )$ .Use these equations to show that the quantities $q ^ { \mu } = k ^ { \mu } e ^ { \phi }$ are Constants of motion,and from this deduce that there is no bending of light by the sun in this scalar theory.

# Exercise 7.2. VECTOR GRAVITATIONAL FIELD, $\boldsymbol { \phi } _ { \mu }$

A. Verify that the variational principle $\delta I = 0$ gives Maxwell's equations by varying $A _ { \mu }$ and the Lorentz force law by varying $z ^ { \mu } ( \tau )$ ，when

$$
I = \frac { - 1 } { 1 6 \pi } \int F _ { \mu \nu } F ^ { \mu \nu } d ^ { 4 } x + \frac { 1 } { 2 } m \int \frac { d z ^ { \mu } } { d \tau } \frac { d z _ { \mu } } { d \tau } d \tau + e \int \frac { d z ^ { \mu } } { d \tau } A _ { \mu } ( z ) d \tau .
$$

Here $F _ { \mu \nu }$ is an abbreviation for $A _ { \nu , \mu } - A _ { \mu , \nu }$ Hint: to vary $\pmb { A } _ { \pmb { \mu } } ( \pmb { x } )$ ，rewrite the last term as a spacetime integral by introducing a delta function $\delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ]$ as in exercise 7.1,parts A and B.

B.Define,byalogytotheaboveavectorgraviatialfd $\Phi _ { \mu }$ with $G _ { \mu \nu } \equiv \phi _ { \nu , \mu } - \phi _ { \mu , \nu }$ using a variational principle with

$$
I = + \frac { 1 } { 1 6 \pi G } \int G _ { \mu \nu } G ^ { \mu \nu } d ^ { 4 } x + \frac { 1 } { 2 } m \int \frac { d z ^ { \mu } } { d \tau } \frac { d z _ { \mu } } { d \tau } d \tau + m \int \phi _ { \mu } \frac { d z ^ { \mu } } { d \tau } d \tau .
$$

(Note: if many particles are present, one must augment $I$ by terms $\bar { { \bf 2 } } m \int ( d z ^ { \mu } / d \tau ) ( d z _ { \mu } / d \tau ) d \tau +$ $m \int \phi _ { \mu } ( d z ^ { \mu } / d \tau ) \ d \tau$ for each particle.) Find the“Coulomb”law in this theory,and verify that the coefficients of the terms in the variational principle have been chosen reasonably.

C. Compute the perihelion precession in this theory. D.Compute the bending of light in this theory (i.e.，scatering of a highly relativistic particle $u ^ { 0 } = \gamma \longrightarrow \infty ;$ ,as it passes by the sun,because of the sun's $\boldsymbol { \phi } _ { \mu }$ field.

E. Obtain a formula for the total field energy corresponding to the Lagrangian implicit in part B.Use the standard method of Hamiltonian mechanics,with

$$
I _ { \mathrm { { t i e l d } } } = { \frac { 1 } { 1 6 \pi G } } \int G _ { \mu \nu } G ^ { \mu \nu } d ^ { 4 } x \equiv \int { \mathcal { L } } d ^ { 4 } x ;
$$

$\mathcal { L }$ is the Lagrangian density and $\begin{array} { r } { L \equiv \int \vec { \mathfrak { L } } \ d ^ { 3 } x } \end{array}$ is the Lagrangian. The corresponding Hamiltonian density $\circledequiv$ energy density) is

$$
\mathcal { H } ^ { \cdot } = \sum _ { \mu } \phi _ { _ { \mu , 0 } } \frac { \partial \mathcal { L } ^ { \cdot } } { \partial \phi _ { _ { \mu , 0 } } } - \mathcal { L } ^ { \cdot } .
$$

Show that vector gravitational waves carry negative energy.

Exercise 7.3. SYMMETRIC TENSOR GRAVITATIONAL FIELD, $h _ { \mu , r } = h _ { { \nu } \mu }$ Here the action principle is, as for the vector field, $\delta I = 0$ ，with $I = I _ { \mathrm { f i e l d } } + I _ { \mathrm { p a r t i c l e } } +$ Iinteraction·Iparticle is the same as for the vector field:

$$
I _ { \mathrm { p a r t i c l e } } = { \frac { 1 } { 2 } } m \int { \frac { d z ^ { \mu } } { d \tau } } { \frac { d z _ { \mu } } { d \tau } } d \tau .
$$

However, $I _ { \mathrm { f i e l d } }$ and $I _ { \mathrm { i n t e r a c t i o n } }$ are different:

$$
\begin{array} { r l } & { I _ { \mathrm { f i e l d } } = \displaystyle \int \mathcal { E } _ { f } d ^ { 4 } x , } \\ & { \mathcal { E } _ { f } = \frac { - 1 } { 3 2 \pi G } \left( \frac { 1 } { 2 } h _ { \nu \beta , \alpha } \overline { { h } } ^ { \nu \beta , \alpha } - \overline { { h } } _ { \mu \alpha } \overline { { h } } ^ { \nu \beta , \beta } , \beta \right) \qquad \left\lceil \mathrm { o n e ~ } h \mathrm { ~ h e r e } \atop \mathrm { i s ~ n o t ~ a n ~ } \overline { { h } } ^ { \mathrm { } } \right\rceil , } \end{array}
$$

with

$$
\begin{array} { r l r } & { } & { \overline { { h } } _ { \mu \nu } \equiv h _ { \mu \nu } - \frac { 1 } { 2 } \eta _ { \mu \nu } h ^ { \sigma } { } _ { \sigma } ; } \\ & { } & { } \\ & { } & { I _ { \mathrm { i n t e r a c t i o n } } = \displaystyle \frac { 1 } { 2 } \int h _ { \mu \nu } T ^ { \mu \nu } d ^ { 4 } x . } \end{array}
$$

Here $T ^ { \mu \nu }$ is the stress-energy tensor for all nongravitational fields and matter present. For a system of point particles (used throughout this exercise),

$$
T ^ { \mu \nu } ( { \pmb x } ) = \int m \frac { d z ^ { \mu } } { d \tau } \frac { d z ^ { \nu } } { d \tau } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] d \tau .
$$

A. Obtain the equations of motion of a particle by varying $z ^ { \mu } ( \tau )$ in $\delta ( I _ { \mathrm { p a r t i c l e } } +$ $I _ { \mathrm { i n t e r a c t i o n } } ) = 0$ .Express your result in terms of the“gravitational force field”

$$
\displaystyle { \cal T } _ { \nu \alpha \beta } = \frac { 1 } { 2 } ( h _ { \nu \alpha , \beta } + h _ { \nu \beta , \alpha } - h _ { \alpha \beta , \nu } )
$$

derived fromthe tensor gravitational potentials $h _ { \mu \nu } = h _ { \nu \mu }$

B. Obtain the field equations from $\delta ( I _ { \mathrm { f i e l d } } + I _ { \mathrm { i n t e r a c t i o n } } ) = 0$ ; express them in terms of

$$
- H ^ { \mu \alpha \nu \beta } \equiv \bar { h } ^ { \mu \nu } \eta ^ { \alpha \beta } + \bar { h } ^ { \alpha \beta } \eta ^ { \mu \nu } - \overline { { { h } } } ^ { \alpha \nu } \eta ^ { \mu \beta } - \overline { { { h } } } ^ { \mu \beta } \eta ^ { \alpha \nu } .
$$

Discuss gauge invariance,and the condition $\widetilde { h } ^ { \mu \alpha } { } _ { , \alpha } = 0$

C.Find the tensor gravitational potentials $h _ { \mu \nu }$ due to the sun (treated as a point mass). D. Compute the perihelion precession.   
E.Compute the bending of light.   
F. Consider a gravitational wave

$$
\widetilde { h } ^ { \mu \nu } = A ^ { \mu \nu } \exp ( i k _ { \alpha } x ^ { \alpha } ) .
$$

What conditions are imposed by the field equations? By the gauge condition

$$
{ \bar { h } } ^ { \mu \alpha } { } _ { , \alpha } = 0 ?
$$

Show that, by further gauge transformations

$$
h _ { \mu \nu } \longrightarrow h _ { \mu \nu } + \xi _ { \mu , \nu } + \xi _ { \nu , \mu }
$$

that preserve the $\widetilde { h } ^ { \mu \alpha } { } _ { , \alpha } = 0$ restrictions,further conditions

$$
u _ { \alpha } \overline { { { h } } } { } ^ { \alpha \mu } = 0 , \qquad \overline { { { h } } } { } ^ { \alpha } { } _ { \alpha } = 0
$$

can be imposed, where $u ^ { \alpha }$ is a fixed,timelike vector.It is sufficient to consider the case, obtained by a suitable choice of reference frame, where $u ^ { \alpha } = ( 1 ; 0 , 0 , 0 )$ and $k ^ { \alpha } = ( \omega ; 0 , 0 , \omega )$ G.From the Hamiltonian density

$$
\mathcal { H } \equiv \dot { h } _ { \ \mu \nu } ( \partial \mathcal { E } / \partial \dot { h } _ { \mu \nu } ) \ - \ \mathcal { E }
$$

for the field, show that the energy density of the waves considered in part $\mathbf { F }$ is positive. H. Compute $T ^ { \mu \nu }$ for the stress-energy tensor of particles $T ^ { \mu \nu }$ that appears in the action integral $I$ Does $T ^ { \mu \nu } { } _ { , { } ^ { \nu } }$ vanish (e.g.,for the earth in orbit around the sun)? Why? Show that the coupled equations for fields and particles obtained from $\delta I = 0$ have no solutions.

(continued on page 187)

# Box 7.1 AN ATTEMPT TO DESCRIBE GRAVITY BY A SYMMETRIC TENSOR FIELD IN FLAT SPACETIME [Solution to exercise 7.3]

Attempts to describe gravity within the framework of special relativity would naturally begin by considering the gravitational field to be a scalar (exercise 7.l） as it is in Newtonian theory,or a vector (exercise 7.2） by analogy to electromagnetism. Only after these are found to be deficient (e.g., no bending of light in either theory; negative-energy waves in the vector theory） would one face the computational complexities of a symmetric tensor gravitational potential $h _ { \mu \nu } = h _ { \nu \mu } ,$ which has more indices.

The foundations of the most satisfactory of all tensor theories of gravity in flat spacetime are laid out at the beginning of exercise 7.3. The choice of the Lagrangian made there (equations 7.8) is dictated by the demand that $h _ { \mu \nu }$ be a“Lorentz covariant, massless, spin-two field.” The meaning of this demand,and the techniques of special relativity required to translate it into a set of field equations,are customarily found in books on elementary particle physics or quantum feld theory; see, e.g., Wentzel (1949), Feynman (l963),or Gasiorowicz (l966).Fierz and Pauli (1939) were the first to write down this Lagrangian and investigate the resulting theory. The conclusions of the theory are spelled out here in the form of a solution to exercise 7.3.

# A. Equation of Motion for a Test Particle (exercise 7.3A)

Carry out the integration in equation (7.9), using the particle stress-energy tensor of equation (7.10), to find

$$
I _ { p + i } \equiv I _ { \mathrm { p a r t i c l e } } + I _ { \mathrm { i n t e r a c t i o n } } = { \frac { 1 } { 2 } } m \int ( \eta _ { \mu \nu } + h _ { \mu \nu } ) \dot { z } ^ { \mu } \dot { z } ^ { \nu } d \tau ,
$$

where

$$
\dot { z } ^ { \mu } \equiv d z ^ { \mu } / d \tau .
$$

Then compute $\delta I _ { p + i }$ ,and find that the coefficient of the arbitrary variation in path $\delta z ^ { \mu }$ vanishes if and only if

$$
( d / d \tau ) [ ( \eta _ { \mu \nu } + h _ { \mu \nu } ) \dot { z } ^ { \nu } ] - \frac { 1 } { 2 } h _ { \alpha \beta , \mu } \dot { z } ^ { \alpha } \dot { z } ^ { \beta } = 0 .
$$

Rewrite this equation of motion in the form

$$
( \eta _ { \mu \nu } + h _ { \mu \nu } ) \ddot { z } ^ { \nu } + { \cal { r } } _ { \mu \alpha \beta } \dot { z } ^ { \alpha } \dot { z } ^ { \beta } = 0 ,
$$

where $\Gamma _ { \mu \alpha \beta }$ is defined in equation (7.11).

# $\mathsf { B } _ { \mathbf { 1 } }$ .Field Equations (exercise 7.3B)

Use $I _ { \mathrm { f i e l d } }$ and $I _ { \mathrm { i n t e r a c t i o n } }$ in the forms given in equations (7.8) and (7.9); but for the quickest and least messy derivation, do not use the standard Euler-Lagrange equations. Instead,compute directly the first-order change $\delta \mathcal { L } _ { f }$ produced by a small

Box 7.1 (continued)

variation $\delta h _ { \alpha \beta }$ of the field. For the second term of $\vec { c ^ { \prime } } _ { f }$ ,i is clear(byrelabeling dummy indices as needed) that varying each factor gives the same result, so the two terms from the product rule combine:

$$
\delta ( \widetilde { h } _ { \mu \alpha } , ^ { \alpha } \ : \overline { { { h } } } ^ { \mu \beta } { } _ { , \beta } ) = 2 \overline { { { h } } } ^ { \mu \beta } { } _ { , \beta } \ : \delta \overline { { { h } } } _ { \mu \alpha } , ^ { \alpha } .
$$

A similar result holds for the first term of $\mathcal { L } _ { f } ^ { \flat } ,$ in view of the identity $a _ { \mu \nu } \overline { { { b } } } ^ { \mu \nu } = \overline { { { a } } } _ { \mu \nu } b ^ { \mu \nu } { } _ { ; }$ which holds for the “bar” operation of equations (7.8); each side here is just $a _ { \mu } { } _ { \nu } b ^ { \mu \nu }$ $- \ : _ { 2 } ^ { 1 } a ^ { \mu } { } _ { \mu } b ^ { \nu } { } _ { \nu } .$ Consequently,

$$
- ( 3 2 \pi G ) \delta \mathcal { E } _ { f } = \overline { { h } } ^ { \nu \beta , \alpha } \delta h _ { \nu \beta , \alpha } - 2 \overline { { h } } ^ { \mu \beta } { } _ { , \beta } \delta \overline { { h } } _ { \mu \alpha } { } ^ { , \alpha } .
$$

Next use this expression in $\delta I _ { \mathrm { f i e l d } }$ ； and,by an integration by parts,remove the derivatives from Shu giving

$$
\delta I _ { \mathrm { { f i e l d } } } = ( 3 2 \pi G ) ^ { - 1 } { \int { [ \overline { { h } } ^ { \nu \beta , \alpha } , \delta h _ { \beta } - 2 \overline { { h } } ^ { \mu \beta } { } _ { , \beta } { } ^ { , \alpha } \delta \overline { { h } } _ { \mu \alpha } ] d ^ { 4 } x } } .
$$

To find the coefficient of $\delta h _ { \mu \nu }$ in this expression, write (from equation 7.8c)

$$
\delta \widetilde { h } _ { \alpha \beta } = ( \delta ^ { \mu } { } _ { \alpha } \delta _ { \nu \beta } - \frac { 1 } { 2 } \eta _ { \alpha \beta } \eta ^ { \mu \nu } ) \delta h _ { \mu \nu } ;
$$

and then rearrange and relabel dummy (summation) indices to obtain

$$
\delta I _ { \mathrm { { f i e l d } } } = ( 3 2 \pi G ) ^ { - 1 } \int { [ \overline { { h } } ^ { \mu \beta , \alpha } , \alpha \delta h _ { \nu \beta } - 2 \overline { { h } } ^ { \mu \beta } { } _ { , \beta } { } ^ { , \alpha } \delta \overline { { h } } _ { \mu \alpha } ] d ^ { 4 } x }  .
$$

By combining this with $\begin{array} { r } { \delta I _ { \mathrm { i n t e r a c t i o n } } = \frac { 1 } { 2 } T ^ { \mu \nu } \delta h _ { \mu \nu } d ^ { 4 } x , } \end{array}$ and by using the symmetry $\delta h _ { \mu \nu } = \delta h _ { \nu \mu } ,$ obtain

$$
- \overline { { h } } { ^ \mu \nu } _ { , \alpha } { ^ \alpha } - \eta { ^ { \mu \nu } } \overline { { h } } { ^ { \alpha \beta } } _ { , \alpha \beta } + \overline { { h } } { ^ { \mu \alpha } } _ { , \alpha } { ^ \nu } + \overline { { h } } { ^ { \nu \alpha } } _ { , \alpha } { ^ { \mu } } = 1 6 \pi G T ^ { \mu \nu } .
$$

The definition made in equation (7.12) allows this to be rewritten as

$$
H ^ { \mu \alpha \nu \beta } { } _ { , \alpha \beta } = 1 6 \pi G T ^ { \mu \nu } .
$$

# $\mathsf { B } _ { \mathbf { 2 } }$ Gauge Invariance (exercise 7.3B, continued)

The symmetries,

$$
H ^ { \mu \alpha \nu \beta } = H ^ { \left[ \mu \alpha \right] \left[ \nu \beta \right] } = H ^ { \nu \beta \mu \alpha } ,
$$

of $H ^ { \mu \alpha \nu \beta }$ imply an identity

$$
{ H ^ { \mu \alpha \nu \beta } } _ { , \alpha \beta \nu } = H ^ { \mu \alpha \{ \nu \beta \} } { } _ { , \alpha \mid \beta \nu ) } \equiv 0
$$

analogous to $F ^ { \mu \nu } { } _ { , \nu \mu } \equiv 0$ in electromagnetism.

Thus $T ^ { \mu \nu } { } _ { , \nu } = 0$ is required of the sources, just as is $J ^ { \mu } { } _ { , \mu } = 0$ in electromagnetism (exercise 3.i6). These identities make the feld equations (4') too weak to fix hup

completely. In particular,by direct substitution in equations (4), one verifies that to any solution one can add a gauge field

$$
\begin{array} { r l } & { h _ { \mu \nu } ^ { \mathrm { \tiny ~ ( g a u g e ) } } = \xi _ { \mu , \nu } + \xi _ { \nu , \mu } , } \\ & { \overline { { h } } _ { \mu \nu } ^ { \mathrm { \tiny ~ ( g a u g e ) } } = \xi _ { \mu , \nu } + \xi _ { \nu , \mu } - \eta _ { \mu \nu } \xi ^ { \alpha } { } _ { , \alpha } , } \end{array}
$$

without changing $T ^ { \mu \nu }$ ·

Let $\xi _ { \mu }$ vanish outside some finite spacetime volume, but be otherwise arbitrary. Then $h _ { \mu \nu }$ and $h _ { \mu \nu } = h _ { \mu \nu } + h _ { \mu \nu } ^ { \quad ( \mathrm { g a u g e ) } }$ both satisfy the source equation (4) for the same source $T ^ { \mu \nu }$ and the same boundary conditions at infinity. We therefore expect them to be physically equivalent.

By a specialization of the gauge analogous to the“Lorentz” specialization $A ^ { \alpha } { } _ { , \alpha } = 0$ of electromagnetism (equation 3.58a; exercise 3.17), one imposes the condition

$$
{ \overline { { h } } } { \mu \alpha } _ { , \alpha } = 0 .
$$

This reduces the field equations (4) to the simple d'Alembertian form

$$
\square \overline { { { h } } } { } ^ { \mu \nu } \equiv \widetilde { h } { } ^ { \mu \nu } { } _ { , \alpha } { } ^ { \alpha } = - 1 6 \pi T ^ { \mu \nu }
$$

(see exercise 18.2). Here and henceforth we set $G = 1$ ("geometrized units").

# C.Field of a Point Mass (exercise 7.3C)

For a static source, the wave equation (7) reduces to a Laplace equation

$$
\nabla ^ { 2 } \widetilde { h } _ { \mu \nu } = - 1 6 \pi T _ { \mu \nu } .
$$

The stress-energy tensor for a static point mass (equation 7.10) is $T ^ { 0 0 } = M \delta ^ { 3 } ( x )$ and $T ^ { \mu k } = 0$ .Put this into the Laplace equation,solve for $\overline { { h } } _ { \mu \nu }$ ,and use equation (7.8c) to obtain $h _ { \mu \nu }$ . The result is:

$$
h _ { 0 0 } = 2 M / r ; \qquad h _ { 0 k } = 0 ; \qquad h _ { i k } = \delta _ { i k } ( 2 M / r )
$$

(see equation 18.15a).

# D． Perihelion Precession (exercise 7.3D)

Direct substitution of the potential (8) into the equations of motion (2) is tedious and not very instructive.Variational principles are popular in mechanics because they simplify such calculations. Return to the basic variational principle $\delta I _ { p + i } = 0$ (equation l),and insert the potential (8) for the sun. Convert to spherical coordinates so oriented that the orbit lies in the equatorial $( \theta = \pi / 2$ ）plane:

$$
\begin{array} { l } { { I _ { p + i } = \displaystyle \int L d \tau ; } } \\ { { L = \displaystyle \frac { 1 } { 2 } m [ - ( 1 - 2 M r ^ { - 1 } ) \dot { t } ^ { 2 } + ( 1 + 2 M r ^ { - 1 } ) ( \dot { r } ^ { 2 } + r ^ { 2 } \phi ^ { 2 } ) ] . } } \end{array}
$$


<!-- chunk 0004: pages 211-280 -->
Box 7.1 (continued)

From the absence of explicit $t \cdot , \phi \cdot ,$ and $\pmb { \tau }$ -dependence in $L$ ,infer three constants of motion: the canonical momenta

$$
P _ { t } \equiv - m \gamma = \partial L / \partial i
$$

(this defines Y） and

$$
P _ { \phi } \equiv m \alpha = \partial L / \partial \dot { \phi }
$$

(this defines $\pmb { \alpha }$ )；and the Hamiltonian

$$
H = \dot { x } ^ { \mu } ( \partial L / \partial \dot { x } ^ { \mu } ) - L ,
$$

which can be set equal to $- { \frac { 1 } { 2 } } m$ by appropriate normalization of the path parameter $\tau .$ .From these constants of the motion, derive an orbit equation as follows: (l) calculate $H = - \frac { 1 } { 2 } m$ in terms of $r , \dot { r } , \dot { \phi } .$ and $i _ { \downarrow }$ (2)eliminate $i$ and $\dot { \phi }$ in favor of the constants $\boldsymbol { \mathsf { \tt T } }$ and $\pmb { \alpha }$ ；(3)as in Newtonian orbit problems, define $u = M / r$ and write

$$
\frac { d u } { d \phi } = \frac { \dot { u } } { \dot { \phi } } = - \frac { M \dot { r } } { r ^ { 2 } \dot { \phi } } = - \frac { M } { \alpha } ( 1 + 2 u ) \dot { r } ;
$$

(4)in $H _ { : }$ eliminate $\dot { r }$ in favor of $d u / d \phi$ via the above equation,and eliminate $r$ in favor of $\pmb { u }$ ；(5) solve for $d u / d \phi$ . The result is

$$
\left( { \frac { d u } { d \phi } } \right) ^ { 2 } + u ^ { 2 } = ( \gamma ^ { 2 } - 1 + 2 u ) { \frac { M ^ { 2 } } { \alpha ^ { 2 } } } \biggl [ { \frac { 1 + 2 u } { 1 - 2 u } } \biggr ] .
$$

Neglecting cubic and higher powers of $u = G M / c ^ { 2 } r \sim ( 1 - \gamma ^ { 2 } )$ in this equation, derive the perihelion shift. (For details of method, see exercise 40.4,with the $\boldsymbol { \gamma }$ and $\pmb { \alpha }$ of this box renamed $\widetilde { E }$ and $\widetilde { L }$ and with the $\boldsymbol { \gamma }$ and $\beta$ of that exercise set equal to l and O.) The resulting shift per orbit is

$$
\begin{array} { r } { \Delta \phi = 8 \pi M / r _ { 0 } + O ( [ M / r _ { 0 } ] ^ { 2 } ) . } \end{array}
$$

This is $\textstyle { \frac { 4 } { 3 } }$ the prediction of general relativity; and it disagrees with the observations On Mercury (see Box 40.3).

# E.Bending of Light (exercise 7.3E)

The deflection angle for light passing the sun is, on dimensional grounds,a smal quantity, $\begin{array} { r } { \varDelta \phi \sim M _ { \odot } / R _ { \odot } \sim 1 0 ^ { - 6 } . } \end{array}$ ； from the outset, one makes approximations based On this smallness. A diagram of the photon trajectory, set in the $x , z \cdot$ plane, shows that, for initial motion parallel to the $z \cdot$ -axis, the deflection angle can be expressed in terms of the final momentum as $\varDelta \phi = p _ { z } / p _ { z }$ .Compute the final $\pmb { p _ { x } }$ by an integral along the trajectory,

$$
p _ { x } = \int _ { - \infty } ^ { + \infty } ( d p _ { x } / d z ) d z ,
$$

![](../chunks/GRAVITATION_part_0004_pages_0211-0280/auto/images/8b0e11cdfccab66a5aec2dc79d9ccda3cd8d2c46eae6df5c39f298f20b75282a.jpg)

treating $\pmb { p _ { z } }$ as essentially constant. This computation requires generalization of the equation of motion (2) to the case of zero rest mass.To handle the limit $m \longrightarrow 0$ ， introduce a new parameter $\lambda = \tau / m$ ；then $p ^ { \mu } = m ( d z ^ { \mu } / d \tau ) = d z ^ { \mu } / d \lambda$ Also define $p _ { \mu } = ( \eta _ { \mu \nu } + h _ { \mu \nu } ) p ^ { \nu }$ , since this quantity appears simply in equation (2) and agrees with $p _ { \mu }$ in the limit $r \longrightarrow \infty$ , where one will need to evaluate it. Then equation (2) reads, for any $m$ ,including $m = 0$ ，

$$
\frac { d P _ { \mu } } { d \lambda } = \frac { 1 } { 2 } h _ { \alpha \beta , \mu } p ^ { \alpha } p ^ { \beta } .
$$

On the righthand side here, since $h _ { \alpha \beta , \mu }$ is small, a crude approximation to $p ^ { \mu }$ suffices; $p ^ { 1 } = p ^ { 2 } = 0 , p ^ { 0 } = p ^ { 3 } = d z / d \lambda = \stackrel { \cdot } { \omega } =$ constant. Thus,

$$
\frac { d P _ { 1 } } { d \lambda } = \frac { 1 } { 2 } ( h _ { 0 0 } + 2 h _ { 0 3 } + h _ { 3 3 } ) _ { , 1 } \omega ^ { 2 }
$$

and

$$
\quad \frac { 1 } { p _ { 3 } } \frac { d P _ { 1 } } { d z } = \frac { 1 } { 2 } ( h _ { 0 0 } + 2 h _ { 0 3 } + h _ { 3 3 } ) _ { , 1 } .
$$

For the sun, $h _ { 0 0 } = h _ { 3 3 } = 2 M / r$ ,and $h _ { 0 3 } = 0$ (equation 8), so

$$
A \phi = - \left( { \frac { p _ { 1 } } { p _ { 3 } } } \right) _ { \mathrm { f i n a l } } = - \left( { \frac { P _ { 1 } } { p _ { 3 } } } \right) _ { \mathrm { f i n a l } } = \int _ { - \infty } ^ { \infty } { \frac { 2 M t d z } { ( \lambda ^ { 2 } + z ^ { 2 } ) ^ { 3 / 2 } } } { \stackrel { . . . } { = } } { \frac { 2 M } { \lambda } } \int _ { - \infty } ^ { \infty } { \frac { d \xi } { ( 1 + \xi ^ { 2 } ) ^ { 3 / 2 } } } = { \frac { 4 M } { t } } .
$$

For light grazing the sun, $\ell = R _ { \odot } ,$ this gives $\pmb { \mathcal { \Delta } } \phi = 4 M _ { \odot } / R _ { \odot }$ radians $= 1 ^ { \prime \prime } . 7 5$ ,which is also the prediction of general relativity,and is consistent with the observations (see Box 40.1).

# F. Gravitational Waves (exercise 7.3F)

The field equations (4) and gauge properties (5) of the present flat-spacetime theory are identical to those of Einstein's “linearized theory.”Thus,the treatment of gravitational waves using linearized theory,which is presented in $\ S \ S 1 8 . 2 , 3 5 . 3$ ,and 35.4, applies here.

# G. Positive Energy of the Waves (exercise 7.3G)

Computing a general formula for $\mathcal { H }$ from equation (7.17)is tedious, but it is sufficient to consider only the special case of a plane wave (equation 7.l3)-or better still,

a plane wave with only $h _ { 1 2 } = h _ { 2 1 } = f ( z - t )$ . Any gravitational wave can be constructed as a superposition of such plane waves. First compute the Langrangian for this case. According to equation (7.8), it reads

$$
\mathcal { L } _ { f } = ( 3 2 \pi ) ^ { - 1 } [ ( h _ { 1 2 , 0 } ) ^ { 2 } - ( h _ { 1 2 , 3 } ) ^ { 2 } ] .
$$

Now the full content of the formula (7.l7) defining $\mathcal { H }$ is precisely the following: start from the Lagrangian; keep all terms that are quadratic in time derivatives; omit all terms that are linear in time derivatives; and reverse the sign of terms that contain no time derivatives.The result is

$$
\mathcal { K } = ( 3 2 \pi ) ^ { - 1 } [ ( h _ { 1 2 , 0 } ) ^ { 2 } + ( h _ { 1 2 , 3 } ) ^ { 2 } ] ,
$$

which is positive.

# H. Self-Inconsistency of the Theory (exercise 7.3H)

From equation (7.10), find

$$
T ^ { \mu \nu } { } _ { , \nu } = m \int { \frac { d z ^ { \mu } } { d \tau } } { \frac { d z ^ { \nu } } { d \tau } } { \frac { \hat { \nabla } } { \hat { \partial } x ^ { \nu } } } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] d \tau .
$$

But $\delta ^ { 4 } ( { \pmb x } - { \pmb z } )$ depends only on the difference $x ^ { \mu } - z ^ { \mu }$ ， ${ \bf s } 0 - \partial / \partial z ^ { \nu }$ can replace $\hat { \boldsymbol { d } } / \hat { \boldsymbol { d } } \boldsymbol { x } ^ { \nu }$ when acting on the $\delta$ -function. Noting that

$$
\frac { d z ^ { \nu } } { d \tau } \frac { \partial } { \partial z ^ { \nu } } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] = \frac { d } { d \tau } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] ,
$$

rewrite $T ^ { \mu \nu } { } _ { , \nu }$ as

$$
\dot { T } ^ { \mu \nu } { } _ { , \nu } = - m \int \dot { z } ^ { \mu } ( d / d \tau ) \delta ^ { 4 } [ x - z ( \tau ) ] d \tau = + m \int \ddot { z } ^ { \mu } \delta ^ { 4 } [ x - z ( \tau ) ] d \tau .
$$

(The last step is obtained by an integration by parts.) Thus $T ^ { \mu \nu } { } _ { , \nu } = 0$ holds if and only if $\tilde { z } ^ { \mu } = 0$ . But $\tilde { z } ^ { \mu } = 0$ means that the gravitational fields have no effect on the motion of the particle. But this contradicts the equation of motion (2), which follows from the theory's variational principle. Thus, this tensor theory of gravity is inconsistent. [Stated briefly,equation (4) requires $T ^ { \mu \nu } { } _ { , \nu } = 0$ ,while equation (2) excludes it.]

The fact that, in this theory,gravitating bodies cannot be affected by gravity,also holds for bodies made of arbitrary stress-energy (e.g., rubber balls or the Earth). Since all bodies gravitate, since the field equations imply $T ^ { \mu \nu } { } _ { , \nu } = 0$ , and since this “equation of motion for stress-energy” implies conservation of a body's total 4-momentum $P ^ { \mu } = \mathcal { J } T ^ { \mu 0 } d ^ { 3 } x$ ，no body can be accelerated by gravity. The Earth cannot be attracted by the sun; it must fly off into interstellar space!

Straightforward steps to repair this inconsistency in the theory lead inexorably to general relativity (see Box l7.2 part 5). Having adopted general relativity as the theory of gravity, one can then use the present flat-spacetime theory as an approximation to it (“Linearized general relativity"; treated in Chapters 18,l9,and 35; see especially discussion at end of $\ S 1 8 . 3 \AA$ 0.

# $\ S 7 . 2$ . GRAVITATIONAL RED SHIFT DERIVED FROM ENERGY CONSERVATION

Einstein argued against the existence of any ideal,straight-line reference system such as is assumed in Newtonian theory.He emphasized that nothing in a natural state of motion, not even a photon, could ever give evidence for the existence or location of such ideal straight lines.

That a photon must be affected by a gravitational field Einstein (l9ll) showed from the law of conservation of energy,applied in the context of Newtonian gravitation theory. Let a particle of rest mass m start from rest in a gravitational field $g$ at point $\mathcal { Q }$ and fall freely for a distance $h$ to point $\mathcal { B }$ . It gains kinetic energy mgh. Its total energy,including rest mass, becomes

Gravitational redshift derived from energy considerations

$$
m + m g h .
$$

Now let the particle undergo an annihilation at $\mathcal { B }$ ，converting its total rest mass plus kinetic energy into a photon of the same total energy. Let this photon travel upward in the gravitational field to $\mathcal { Q }$ . If it does not interact with gravity, it will have its original energy on arrival at $\boldsymbol { \mathcal { Q } }$ .At this point it could be converted by a suitable apparatus into another particle of rest mass m (which could then repeat the whole process) plus an excess energy mgh that costs nothing to produce.To avoid this contradiction of the principal of conservation of energy,which can also be stated in purely classical terms,Einstein saw that the photon must suffer a red shift. The energy of the photon must decrease just as that of a particle does when it climbs out of the gravitational field. The photon energy at the top and the bottom of its path through the gravitational feld must therefore be related by

$$
E _ { \mathrm { b o t t o m } } = E _ { \mathrm { t o p } } ( 1 ~ + ~ g h ) = E _ { \mathrm { t o p } } ( 1 ~ + ~ g _ { \mathrm { c o n v } } h / c ^ { 2 } ) .
$$

The drop in energy because of work done against gravitation implies a drop in frequency and an increase in wavelength (red shift; traditionally stated in terms of a red shift parameter, $z = \varDelta \lambda / \lambda$ )； thus,

$$
1 + z = \frac { \lambda _ { \mathrm { t o p } } } { \lambda _ { \mathrm { b o t t o m } } } = \frac { h \nu _ { \mathrm { b o t t o m } } } { h \nu _ { \mathrm { t o p } } } = \frac { E _ { \mathrm { b o t t o m } } } { E _ { \mathrm { t o p } } } = 1 + g h .
$$

The redshift predicted by this formula has been verified to l percent by Pound and Snider (l964,l965),refining an experiment by Pound and Rebka (1960).

# $\$ 7.3$ .GRAVITATIONAL REDSHIFT IMPLIES SPACETIME IS CURVED

An argument by Schild (1960,1962,1967） yields an important conclusion: the existence of the gravitational redshift shows that a consistent theory ofgravity cannot be constructed within the framework of special relativity.

![](../chunks/GRAVITATION_part_0004_pages_0211-0280/auto/images/6f2ac1ad29d7ec4d267dd7540ae4c921cf9e1f37085b92426e37e2001d6a56b9.jpg)  
Figure 7.1. Successive pulses of light rising from height $z _ { 1 }$ to height $z _ { 2 } = z _ { 1 } + h$ against the gravitational feld of the earth.The paths $\gamma _ { 1 }$ ,and $\gamma _ { 2 }$ must be exactly congruent, whether sloped at $4 5 ^ { \circ }$ (left)or having variable slope (right).

Assume gravity is described by an (unspecified) field in flat spacetime..

Whereas Einstein's argument (last section) was formulated in Newtonian theory, Schild's is formulated in special relativity.It analyzes gravitational redshift experiments in the field of the Earth,using a global Lorentz frame tied to the Earth's center.It makes no demand that free particles initially at rest remain at rest in this global Lorentz frame (except far from the Earth,where gravity is negligible). On the contrary,it demands that free particles be accelerated relative to the Lorentz frame by the Earth's gravitational field.It is indifferent to the mathematical nature of that field (scalar, vector,tensor,...),but it does insist that the gravitational accelerations agree with experiment. And, of course, it demands that proper lengths and times be governed by the metric of special relativity.

Schild's argument proceeds as follows.Consider one observer at rest on the Earth's surface at height $z _ { 1 } ,$ ,and a second above the Earth's surface at height $z _ { 2 } = z _ { 1 } + h$ (Figure 7.1). The observers may verify that they are at rest relative to each other and relative to the Earth's Lorentz frame by,for instance,radar ranging to free particles that are at rest in the Earth's frame far outside its gravitational field.The bottom experimenter then emits an electromagnetic signal of a fixed standard frequency $\omega _ { b }$ which is received by the observer on top.For definiteness,let the signal be a pulse exactly $N$ cycles long. Then the interval of time\* $\delta \tau _ { \mathsf { b o t } }$ required for the emission of the pulse is given by $2 \pi N = \omega _ { b } \delta \tau _ { \mathrm { b o t } } .$ The observer at the top is then to receive these same $N$ cycles of the electromagnetic wave pulse and measure the time interval\* $\delta \tau _ { \mathsf { t o p } }$ required. By the definition of “frequency,” it satisfies $2 \pi N =$ $\omega _ { t } \delta \tau _ { \mathsf { t o p } }$ .The redshift effect, established by experiment (for us) or by energy conservation (for Einstein), shows $\omega _ { t } < \omega _ { b }$ ； consequently the time intervals are different, $\delta \tau _ { \mathrm { t o p } } > \delta \tau _ { \mathrm { b o t } } .$ Transfer this information to the special-relativity spacetime diagram of the experiment (Figure 7.l). The waves are light rays; so one might show them as traveling along $4 5 ^ { \circ }$ null lines in the spacetime diagram (Figure 7.1,A). In this simplified but slightly inadequate form of the argument,one reaches a contradiction by noticing that here one has drawn a parallelogram in Minkowski spacetime in which two of the sides are unequal, $\tau _ { \mathrm { { t o p } } } > \tau _ { \mathrm { { b o t } } }$ ，whereas a parallelogram in flat Minkowski spacetime cannot have opposite sides unequal. One concludes that special relativity cannot be valid over any sufficiently extended region. Globally,spacetime, as probed by the tracks of light rays and test particles, departs from flatness("curvature"; Parts III and IV of this book),despite the fine fit that Lorentz-Minkowski flatness gives to physics locally.

Figure 7.1,B, repairs an oversimplification in this argument by recognizing that the propagation of light will be influenced by the gravitational field. Therefore photons might not follow straight lines in the diagram. Consequently,the world lines $\gamma _ { 1 }$ and $\gamma _ { 2 }$ of successive pulses are curves.However, the gravitational field is static and the experimenters do not move. Therefore nothing in the experimental setup changes with time. Whatever the path $\gamma _ { 1 }$ ，the path $\gamma _ { 2 }$ must be a congruent path of exactly the same shape,merely translated in time.On the basis of this congruence and the fact that the observers are moving on parallel world lines, one would again conclude,if flat Minkowski geometry were valid, that $\tau _ { \mathrm { b o t } } = \tau _ { \mathrm { t o p } } ,$ ， thus contradicting the observed redshift experiment. The experimenters do not need to understand the propagation of light in a gravitational field.They need only use their radar apparatus to verify the fact that they are at rest relative to each other and relative to the source of the gravitational field. They know that, whatever influence the gravitational feld has on their radar apparatus,it will not be a time-dependent influence. Moreover, they do not have to know how to compute their separation in order to verify that the separation remains constant. They only need to verify that the round-trip time required for radar pulses to go out to each other and back is the same every time they measure it.

Schild's redshift argument does not reveal what kind of curvature must exist, or whether the curvature exists in the neighborhood of the observational equipment or Some distance away from it. It does say, however, quite unambigously, that the flat spacetime of special relativity is inadequate to describe the_situation,and it should therefore motivate one to undertake the mathematical analysis of curvature in Part III.

This assumption is incompatible with gravitational redshift

Conclusion:spacetime is curved

# $\ S 7 . 4$ .GRAVITATIONAL REDSHIFT AS EVIDENCE FOR THE PRINCIPLE OF EQUIVALENCE

Einstein (l9o8,1911) elevated the idea of the universality of gravitational interactions to the status of a fundamental principle of equivalence, that all effects of a uniform gravitational field are identical to the effects of a uniform acceleration of the coordinate system.This principle generalized a result of Newtonian gravitation theory,in which a uniform acceleration of the coordinate system in equation (7.l） gives rises to a

Principle of equivalence:a uniform gravitational field is indistinguishable from a uniform acceleration of a reference frame

supplementary uniform gravitational field. However, the Newtonian theory only gives this result for particle mechanics.Einstein's principle of equivalence asserts that a similar correspondence willhold for all the laws of physics, including Maxwell's equations for the electromagnetic feld.

The rules of the game--the“scientific method"-require that experimental support be sought for any new theory or principle,and Einstein could treat the gravitational redshift as the equivalent of experimental confirmation of his principle of equivalence.There are two steps in such a confirmation: first, the theory or principle must predict an effect (the next paragraph describes how the equivalence principle implies the redshift); second, the predicted effect must be observed.With the Pound-Rebka-Snider experiments,one is in much better shape today than Einstein was for this second step. Einstein himself had to rely on the experiments supporting the general Concept of energy conservation, plus the necesity of aredshift to preserve energy conservation,as a substitute for direct experimental confirmation.

Gravitational redshift derived from equivalence principle

The existence of the gravitational redshift can be deduced from the equivalence principle by considering two experimenters in a rocket ship that maintains a constant acceleration $g$ .Let the distance between the two observers be $h$ in the direction of the acceleration. Suppose for definiteness that the rocket ship was at rest in some inertial coordinate system when the bottom observer sent off a photon. It will require time $t = h$ for the photon to reach the upper observer.In that time the top observer acquires a velocity $v = g t = g h$ .He will therefore detect the photon and observe a Doppler redshift $z = v = g h$ . The results here are therefore identical to equation (7.20).The principle of equivalence of course requires that,if this redshift is observed in an experiment performed under conditions of uniform acceleration in the absence of gravitational fields, then the same redshift must be observed by an experiment performed under conditions where there is a uniform gravitational field, but no acceleration. Consequently,by the principle of equivalence, one can derive equation (7.20)as applied to the gravitational situation.

# $\$ 7.5$ ． LOCAL FLATNESS，GLOBAL CURVATURE

The equivalence principle helps one to discern the nature of the spacetime curvature, whose existence was inferred from Schild's argument.Physics is the same in an accelerated frame as it is in a laboratory tied to the Earth's surface. Thus,an Earth-bound lab can be regarded as accelerating upward, with acceleration $g$ relative to the Lorentz frames in its neighborhood.\* Equivalently,relative to the lab and the Earth's surface, all Lorentz frames must accelerate downward.But the downward (radial) direction is different at different latitudes and longitudes.Hence,local Lorentz frames,initially at rest with respect to each other but on opposite sides of the Earth, subsequently fall toward the center and go flying through each other. Clearly they cannot be meshed to form the single global Lorentz frame, tied to the

Earth, that was assumed in Schild's argument. This nonmeshing of local Lorentz frames, like the nonmeshing of local Cartesian coordinates on a curved 2-surface, is a clear manifestation of spacetime curvature.

Geographers have similar problems when mapping the surface of the earth. Over small areas,a township or a county,it is easy to use a standard rectangular coordinate system. However, when two fairly large regions are mapped,each with one coordinate axis pointing north, then one finds that the edges of the maps overlap each other best if placed at a slight angle (spacetime analog: relative velocity of two local Lorentz frames meeting at center of Earth). It is much easier to start from a picture of a spherical globe,and then talk about how small flat maps might be used as good approximations to parts of it, than to start with a huge collection of small maps and try to piece them together to build up a picture of the globe. The exposition of the geometry of spacetime in this book will therefore take the first approach. Now that one recognizes that the problem is to fit together local, flat spacetime descriptions of physics into an over-all view of the universe,one should be happy to jump,in the next chapter, into a broadscale study of geometry.From this more advantageous viewpoint,one can then face the problem of discussng the relationship between the local inertial coordinate systems appropriate to two nearby regions that have slightly different gravitational fields.

# Nonmeshing of local Lorentz frames motivates study of geometry

Two types of geometry relevant to spacetime:

There are actually two distinguishable ways in which geometry enters the theory of general relativity. One is the geometry of lengths and angles in four-dimensional spacetime,which is inherited from the metric structure $d s ^ { 2 }$ of special relativity. Schild's argument already shows (without a direct appeal to the equivalence principle) that the special-relativistic ideas of length and angle must be modified. The modified ideas of metric structure lead to Riemannian geometry,which will be treated in Chapters 8 and l3. However, geometry also enters general relativity because of the equivalence principle.An equivalence principle can already be stated within Newtonian gravitational theory,in which no concepts of a spacetime metric enter,but only the Euclidean metric structure of three-dimensional space. The equivalence-principle view of Newtonian theory again insists that the local standard of reference be the freely falling particles. This requirement leads to the study of a spacetime geometry in which the curved world lines of freely falling particles are defined to be locally straight. They play the role in a curved spacetime geometry that straight lines play in flat spacetime. This “affine geometry” will be studied in Chapters lO--12. It leads to a quantitative formulation of the ideas of“covariant derivative” and “curvature” and even “curvature of Newtonian spacetime"!

Riemannian geometry (lengths and angles)

Affine geometry （"'straight lines"and curvature)

# PART 三

# THE MATHEMATICS OF CURVED SPACETIME

Wherein the reader is exposed to the charms of a new temptress-Modern Differential Geometry-and makes a decision: to embrace her for eight full chapters:or, having drunk his fill, to escape after one.
