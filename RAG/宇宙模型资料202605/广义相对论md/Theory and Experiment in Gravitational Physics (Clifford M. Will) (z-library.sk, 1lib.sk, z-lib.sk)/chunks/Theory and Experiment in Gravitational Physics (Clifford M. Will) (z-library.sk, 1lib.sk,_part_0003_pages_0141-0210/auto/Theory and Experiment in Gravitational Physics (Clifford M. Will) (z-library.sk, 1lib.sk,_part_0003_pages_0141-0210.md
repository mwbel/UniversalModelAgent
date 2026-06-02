These parameters express the mismatch between the flat metric $\eta _ { \mu \nu }$ and the asymptotic form of the physical metric $g _ { \mu \nu } ^ { ( 0 ) }$ determined by the cosmological model. Depending on the cosmological model, it was generally possible to choose $c _ { 0 }$ and $c _ { 1 }$ so as to make $\alpha _ { 2 }$ small enough to conform to solar system bounds (see Section 8.4).

Death to Rosen’s bimetric theory came with the Hulse-Taylor binary pulsar. Despite the ability to agree with general relativity at post-Newtonian order, the theory predicted violations of the Strong Equivalence Principle in the presence of strongly gravitating neutron stars (Will and Eardley, 1977), and also predicted significant differences from general relativity for gravitational radiation. In particular, for the binary pulsar, it predicted dipole gravitational radiation with a negative energy flux (Will, 1977; Will and Eardley, 1977), leading to a predicted increase in the binary pulsar’s orbital period, in strong contradiction with the observed decrease.

# 5.8.3 Other theories

In the years prior to general relativity, Nordstrom (1913), toyed with a conformally flat ¨ theory of gravity, in which the metric has the form ${ \pmb g } \equiv f ( \phi ) \eta$ , where $\eta$ is the Minkowski metric, and $\phi$ is a scalar field. Irrespective of the field equations for $\phi$ , the conformal flatness and a proper Newtonian limit require that $g _ { i j } = - \delta _ { i j } g _ { 0 0 } = \delta _ { i j } ( 1 - 2 U )$ . Therefore $\gamma = - 1$ , in strong disagreement with observation. This result can also be deduced from the conformal invariance of Maxwell’s equations (i.e., invariance under the transformation $g _ { \mu \nu }  \phi g _ { \mu \nu } ,$ ), which implies that propagation of light rays in the metric $f ( \phi ) \eta$ is identical to propagation in the flat spacetime metric $\eta$ , namely, straight-line propagation at constant speed.

Another class of alternative theories asserted that, in a certain coordinate system, the metric should always have the form $d s ^ { 2 } = - A ( \phi ) d t ^ { 2 } + B ( \phi ) ( d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } )$ , independent of the nature of the source, with $\phi$ determined by some field equations. Such theories can actually be made generally covariant by introducing a nondynamical background Minkowski metric $\eta$ , and a nondynamical scalar field $T$ with the properties $T _ { \vert \mu \nu } = 0$ and $T _ { , \mu } T _ { , \nu } \eta ^ { \mu \nu } = - 1 { } _ { \ L }$ . This scalar field acts like a cosmic time coordinate, selecting preferred spatial sections or “strata” that are orthogonal to $\mathbf { v } T .$ . With these definitions, the metric in these “stratified theories with time-orthogonal space slices” takes the covariant form ${ \pmb g } =$ $( B - A ) \mathbf { d } T \otimes \mathbf { d } T + B \pmb { \eta }$ . Since the metric is diagonal in a coordinate system in which $T _ { \mu } = \delta _ { \mu } ^ { 0 }$ (the preferred cosmic rest frame), independently of the nature of the source, then in the post-Newtonian limit and in the standard PPN gauge, we must have that $g _ { 0 j } = - \epsilon X _ { , 0 j }$ for some $\epsilon$ . From Box 4.1, we then conclude that $\alpha _ { 1 } = - 4 ( \gamma + 1 )$ in gross violation of observation. Some “straw-man” generalizations of this class of theories circumvented this problem by introducing auxiliary dynamical vector and tensor fields, in addition to the scalar field (Lee et al., 1974; Ni, 1973). It turned out however, that when the parameters were adjusted to conform to solar-system experiments, most of these theories predicted negative gravitational energy flux, in strong disagreement with binary pulsar data (Will, 1977).

One of the consequences of the fundamental postulates of metric theories of gravity is that matter and nongravitational fields couple only to the metric, in a manner dictated by EEP. The resulting equations of motion include

$$
\begin{array} { r l r l } & { T ^ { \mu \nu } { } _ { ; \nu } = 0 } & { } & { \left[ \mathrm { h y d r o d y n a m i c s ~ a n d ~ n o n g r a v i t a t i o n a l ~ f i e l d s } \right] , } \\ & { u ^ { \nu } u ^ { \mu } { } _ { ; \nu } = 0 } & { } & { \left[ \mathrm { n e u t r a l ~ t e s t ~ b o d y : ~ g e o d e s i c s } \right] , } \\ & { F ^ { \mu \nu } { } _ { ; \nu } = 4 \pi J ^ { \mu } } & { } & { \left[ \mathrm { M a x w e l l ' s ~ e q u a t i o n s } \right] , } \\ & { k ^ { \nu } k ^ { \mu } { } _ { ; \nu } = 0 } & { } & { \left[ \mathrm { l i g h t ~ r a y s : ~ g e o d e s i c s } \right] , } \end{array}
$$

(see Section 3.2 for discussion). In Chapter 4, we developed the general spacetime metric through post-Newtonian order as a functional of matter variables and as a function of ten PPN parameters. If this metric is substituted into these equations of motion, we obtain coupled sets of equations of motion for matter and nongravitational field variables in terms of other matter and nongravitational field variables. For specific problems, these equations can be solved using standard techniques to obtain predictions for the behavior of matter in terms of the PPN parameters. These predictions can then be compared with experiment. It is the purpose of this chapter to cast the above equations of motion into a form that can be applied to specific situations and experiments. That application will be made in Chapters 7, 8 and 9. In Section 6.1, we carry out this procedure for light rays. Section 6.2 lays out the equations of hydrodynamics in the PPN framework, and Section 6.3 deals with massive, self-gravitating bodies and presents appropriate $N .$ -body equations of motion. Section 6.5 specializes to semiconservative theories of gravity and presents an $N$ -body Lagrangian and Hamilton from which the semiconservative $N .$ -body equations of motion can be derived. In Section 6.6, we derive the relative acceleration between two bodies, including the effects of nearby gravitating bodies and of motion with respect to the universe rest frame, and put it into a form from which one can identify a “locally measured” Newtonian gravitational constant. In Section 6.7, we derive post-Newtonian equations of motion for spinning bodies.

# 6.1 Equations of Motion for Photons

We begin with the geodesic equation obtained from Maxwell’s equations in the geometrical-optics limit, Eq. (6.1):

$$
k ^ { \nu } k ^ { \mu } { } _ { ; \nu } = 0 ,
$$

where $k ^ { \mu }$ is the wave vector tangent to the “photon” trajectory, with

$$
k ^ { \mu } k _ { \mu } = 0 .
$$

Substituting $k ^ { \mu } = d x ^ { \mu } / d \sigma$ where $\sigma$ is an “affine” parameter measured along the trajectory, we obtain

$$
{ \frac { d ^ { 2 } x ^ { \mu } } { d \sigma ^ { 2 } } } + \Gamma _ { \nu \lambda } ^ { \mu } { \frac { d x ^ { \nu } } { d \sigma } } { \frac { d x ^ { \lambda } } { d \sigma } } = 0 .
$$

As it stands, this equation is not particularly useful, since we have no experimental access to the parameter $\sigma$ . On the other hand, we do have access to coordinate time $t$ . For example, the arrival of photons at Earth can be recorded in terms of atomic time $t _ { \mathrm { a t o m i c } }$ on Earth; this time can be directly related to PPN coordinate time $t = x ^ { 0 }$ by well known transformations (see, e.g., PW, chapter 10). We can rewrite Eq. (6.4) using $t$ rather than $\sigma$ by noticing that

$$
{ \frac { d ^ { 2 } t } { d \sigma ^ { 2 } } } + \Gamma _ { \nu \lambda } ^ { 0 } { \frac { d x ^ { \nu } } { d \sigma } } { \frac { d x ^ { \lambda } } { d \sigma } } = 0 .
$$

Then the spatial components of Eq. (6.4) can be rewritten in the form

$$
{ \frac { d ^ { 2 } x ^ { j } } { d t ^ { 2 } } } + \left( \Gamma _ { \nu \lambda } ^ { j } - \Gamma _ { \nu \lambda } ^ { 0 } { \frac { d x ^ { j } } { d t } } \right) { \frac { d x ^ { \nu } } { d t } } { \frac { d x ^ { \lambda } } { d t } } = 0 .
$$

Eq. (6.3) can be written

$$
g _ { \mu \nu } { \frac { d x ^ { \mu } } { d t } } { \frac { d x ^ { \nu } } { d t } } = 0 .
$$

To post-Newtonian accuracy, Eqs. (6.6) and (6.7) take the form (see Box 6.1 for expressions for the Christoffel symbols $\Gamma _ { \nu \lambda } ^ { \mu }$ )

$$
\begin{array} { r l r } {  { \frac { d \pmb { \nu } } { d t } = \pmb { \nabla } U \big ( 1 + \gamma \pmb { \nu } ^ { 2 } \big ) - 2 ( 1 + \gamma ) \pmb { \nu } \big ( \pmb { \nu } \cdot \pmb { \nabla } U \big ) , } } \\ & { { } } & { 0 = 1 - 2 U - \nu ^ { 2 } \big ( 1 + 2 \gamma U \big ) , } \end{array}
$$

where $\pmb { \nu } = d \pmb { x } / d t$ , with $| \nu | \sim 1$ . Eq. (6.8b) implies that $\nu$ can be written as

$$
\pmb { \nu } = \left[ 1 - ( 1 + \gamma ) U \right] \pmb { n } ,
$$

where $\pmb { n }$ is a unit vector, satisfying $\pmb { n } \cdot \pmb { n } = 1$ . Substituting Eq. (6.9) back into (6.8a) yields an equation for the unit vector $_ { n }$ ,

$$
\frac { d n ^ { j } } { d t } = ( 1 + \gamma ) ( \delta ^ { j k } - n ^ { j } n ^ { k } ) U _ { , k } .
$$

Notice that the right-hand-side of Eq. (6.10) is orthogonal to $\pmb { n }$ , so that $\pmb { n }$ remains a unit vector; only its direction changes.

Eqs. (6.9) and (6.10), can be solved in a straightforward way. Consider a light signal emitted at PPN coordinate time $t _ { e }$ at a point $x _ { e }$ in an initial direction described by the unit vector $\pmb { k }$ , where $\pmb { k } \cdot \pmb { k } = 1$ . The zeroth-order solution to Eq. (6.10) is $\pmb { n } = \pmb { k }$ , so that the light trajectory is given to zeroth order by

$$
\begin{array} { r } { \pmb { x } ( t ) = \pmb { x } _ { e } + \pmb { k } ( t - t _ { e } ) , } \end{array}
$$

where $x _ { e } = x ( t _ { e } )$ . At the first PN order, we define

$$
\pmb { n } = \pmb { k } + \pmb { \alpha } ,
$$

where to post-Newtonian order, $_ \alpha$ satisfies

$$
\frac { d \alpha ^ { j } } { d t } = ( 1 + \gamma ) ( \delta ^ { j k } - k ^ { j } k ^ { k } ) U _ { , k } ,
$$

with the initial condition $\alpha ( t _ { e } ) = 0$ , where $U _ { , k }$ is to be evaluated at $x ( t )$ , and $U$ is given by Eq. (6.11),

$$
U ( { \bf x } ( t ) ) = \int \frac { { \rho } ^ { * } { } ^ { \prime } } { s } d ^ { 3 } x ^ { \prime } ,
$$

where $\mathbf { } s = \mathbf { } x ( t ) - x ^ { \prime }$ and $s = | s |$ . This gives

$$
\frac { d \alpha } { d t } = - ( 1 + \gamma ) \int \rho ^ { * \prime } \frac { b } { s ^ { 3 } } d ^ { 3 } x ^ { \prime } ,
$$

where

$$
\pmb { b } \equiv \pmb { s } _ { e } - ( \pmb { s } _ { e } \cdot \pmb { k } ) \pmb { k } , \quad \pmb { s } _ { e } \equiv \pmb { x } _ { e } - \pmb { x } ^ { \prime } .
$$

The vector $\pmb { b }$ is directed from a point $ { \boldsymbol { { x } } } ^ { \prime }$ within the source to the point of closest approach of the light ray relative to that point. To post-Newtonian order, the velocity $\nu$ of the light ray is now given by

$$
\begin{array} { r } { \pmb { \nu } = \left[ 1 - ( 1 + \gamma ) U \right] \pmb { k } + \pmb { \alpha } . } \end{array}
$$

To solve for $_ { \alpha }$ and to integrate Eq. (6.17) to obtain the trajectory, we employ the useful identities, valid to lowest PN order:

$$
\begin{array} { c } { \displaystyle \frac { d s } { d t } = \frac { { s \cdot k } } { s } , } \\ { \displaystyle \frac { d } { d t } \left( \frac { s \cdot k } { s } \right) = \frac { b ^ { 2 } } { s ^ { 3 } } , } \\ { \displaystyle \frac { d } { d t } \ln ( s + s \cdot k ) = \frac { 1 } { s } . } \end{array}
$$

We can then use the identity (6.18b) to express $d \alpha / d t$ as

$$
\frac { d { \pmb \alpha } } { d t } = - ( 1 + \gamma ) \frac { d } { d t } \int \rho ^ { * \prime } \frac { { \pmb b } } { b ^ { 2 } } \frac { { \pmb s } \cdot { \pmb k } } { s } d ^ { 3 } x ^ { \prime } ,
$$

which can be integrated to yield

$$
\alpha ( t ) = - ( 1 + \gamma ) \int \rho ^ { * \prime } \frac { b } { b ^ { 2 } } \biggl ( \frac { s \cdot k } { s } - \frac { s _ { e } \cdot k } { s _ { e } } \biggr ) d ^ { 3 } x ^ { \prime } .
$$

Integrating Eq. (6.17) making use of the identities (6.18a) and (6.18c), we find the photon’s trajectory in the form

$$
\pmb { x } ( t ) = \pmb { x } _ { e } + \pmb { k } ( t - t _ { e } ) + \pmb { k } \delta x _ { \parallel } ( t ) + \delta \pmb { x } _ { \perp } ( t ) ,
$$

where

$$
\begin{array} { l } { { \delta x _ { \parallel } ( t ) = - ( 1 + \gamma ) \int \rho ^ { * \prime } \ln \biggl [ \frac { ( s + s \cdot k ) ( s _ { e } - s _ { e } \cdot k ) } { b ^ { 2 } } \biggr ] d ^ { 3 } x ^ { \prime } , } } \\ { { \delta x _ { \perp } ( t ) = - ( 1 + \gamma ) \int \rho ^ { * \prime } \frac { b } { b ^ { 2 } } \biggl ( s - \frac { s \cdot s _ { e } } { s _ { e } } \biggr ) d ^ { 3 } x ^ { \prime } , } } \end{array}
$$

assuming the initial conditions $\begin{array} { r } { \delta x _ { \parallel } ( t _ { e } ) = \delta x _ { \perp } ( t _ { e } ) = 0 . } \end{array}$ In the expression for $\delta \boldsymbol { x } _ { \parallel }$ , we have made use of the identity $b ^ { 2 } = ( s _ { e } - { \pmb s } _ { e } \cdot { \pmb k } ) ( s _ { e } + { \pmb s } _ { e } \cdot { \pmb k } )$ . Equations (6.21) and (6.22) give a complete post-Newtonian solution for the trajectory of light around any mass distribution.

# 6.2 PPN Hydrodynamics

The PPN equations of hydrodynamics can be obtained by substituting the Christoffel symbols, displayed to the appropriate order in $\mathrm { B o x } 6 . 1$ , into the equation of motion $T _ { ; \nu } ^ { \mu \nu } = 0$ , using the post-Newtonian form of $T ^ { \mu \nu }$ given in Box 4.1. Using coordinate time $t$

# Box 6.1

To the post-Newtonian order sufficient for use in the equations of hydrodynamics or the geodesic equation for test bodies, the Christoffel symbols are given by

$$
\begin{array} { r l } & { \Gamma _ { \mathrm { e } } ^ { \prime } = - U _ { 0 } , } \\ & { \Gamma _ { \mathrm { s } } ^ { \prime } = - U _ { i } , } \\ & { \Gamma _ { \mathrm { s } } ^ { \prime } = - \gamma _ { i } \partial _ { i } U _ { i } + \frac { 1 } { 2 } \big ( 4 \gamma + 4 + \alpha _ { 1 } \big ) U _ { i , 0 , i } + \frac { 1 } { 2 } \big ( 1 + \alpha _ { 2 } - \zeta _ { 1 } + 2 \xi \big ) U _ { i , 0 } } \\ & { \quad + \frac { 1 } { 2 } \alpha _ { 1 } \alpha _ { 2 } \big \langle \partial _ { i } U _ { i , 0 } , } \\ & { \qquad + \frac { 1 } { 2 } \alpha _ { 1 } \alpha _ { 2 } \big ( \beta + \gamma \big ) ( B _ { i } - \alpha _ { 1 } \psi ) \mathcal { H } _ { i , 0 } , } \\ & { \Gamma _ { \mathrm { e } } ^ { \prime } = - U _ { i } + 2 \big ( \beta + \gamma \big ) ( B _ { i } - \psi _ { i } ) - \frac { 1 } { 2 } \big ( \delta _ { 7 } + 4 + \alpha _ { 1 } \big ) V _ { i , 0 } } \\ & { \qquad - \frac { 1 } { 2 } \big ( 1 + \alpha _ { 2 } - \zeta _ { 1 } + 2 \xi \big ) \zeta _ { 2 , 0 } + \frac { 1 } { 2 } \big ( \alpha _ { 1 } - \alpha _ { 3 } \big ) \alpha ^ { 2 } b _ { i } - \frac { 1 } { 2 } \alpha _ { 1 } \beta ^ { 3 } b _ { i } ^ { \prime } \mathcal { H } _ { i , 0 } } \\ & { \qquad - \frac { 1 } { 2 } \alpha _ { 1 } \alpha _ { 2 } b _ { i } ^ { \prime } b _ { i } + \frac { 1 } { 2 } \big ( \alpha _ { 1 } - 2 \alpha _ { 3 } \big ) \alpha ^ { 2 } b _ { i } ^ { \prime } b _ { i } + \alpha _ { 3 } \beta ^ { 3 } b _ { i } ^ { \prime } b _ { i } , } \\ & { \Gamma _ { \mathrm { s } } ^ { \prime } = \gamma _ { 0 } ^ { \mathrm { s } } b _ { i } ^ { \prime } - \frac { 1 } { 2 } \big ( 4 \gamma + 4 + \alpha _ { 1 } \big ) ( b _ { i } \psi _ { i } ) - \frac { 1 } { 2 } \alpha _ { 1 } \gamma _ { 0 } b _ { i } ^ { \prime } b _ { i } ^ { \prime } } \\ &  \qquad \ \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle { \psi = \frac { 1 } { 2 } ( 2 \gamma + 1 + \alpha _ { 3 } + \zeta _ { 1 } - 2 \xi ) \Phi _ { 1 } - ( 2 \beta - 1 - \zeta _ { 2 } - \xi ) \Phi _ { 2 } } } \\ { \displaystyle { \quad \quad + ( 1 + \zeta _ { 3 } ) \Phi _ { 3 } + ( 3 \gamma + 3 \zeta _ { 4 } - 2 \xi ) \Phi _ { 4 } - \frac { 1 } { 2 } ( \zeta _ { 1 } - 2 \xi ) \Phi _ { 6 } - \xi \Phi _ { W } . } } \end{array}
$$

to parametrize the time evolution, and organizing terms to put the resulting equation into a form that matches the Euler equation (4.3) in the Newtonian limit, we obtain

$$
\begin{array} { r l r } {  { \rho ^ { * } \frac { d \nu ^ { j } } { d t } = \rho ^ { * } U _ { j } - p _ { , j } } } \\ & { } & { + [ \frac { 1 } { 2 } \nu ^ { 2 } + ( 2 - \gamma ) U + \Pi + \frac { p } { \rho ^ { * } } ] p _ { , j } - \nu ^ { j } p _ { 0 } } \\ & { } & { + \rho ^ { * } \Bigg \{ [ \gamma \nu ^ { 2 } - 2 ( \gamma + \beta ) U ] U _ { , j } + \psi _ { , j } - \nu ^ { j } [ ( 2 \gamma + 1 ) U _ { , 0 } + 2 ( \gamma + 1 ) \nu ^ { k } U _ { , k } ] } \\ & { } & { +  \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) [ V _ { , 0 } + \nu ^ { k } \big ( V _ { , j , k } - V _ { , k , j } \big ) ] + \frac { 1 } { 2 } \big ( 1 + \alpha _ { 2 } - \zeta _ { 1 } + 2 \xi \big ) X _ { , 0 , 0 } \Bigg \} } \\ & { } & { + \rho ^ { * } [ \frac { 1 } { 2 } \Phi _ { , j } ^ { \mathrm { P r } } - \Phi _ { j , 0 } ^ { \mathrm { P r } } - \nu ^ { k } \big ( \Phi _ { , j , k } ^ { \mathrm { P r } } - \Phi _ { k , j } ^ { \mathrm { P r } } ) ] , \qquad \quad ( 6 . 2 5 ) } \end{array}
$$

where $\psi , \Phi ^ { \mathrm { P F } }$ and $\Phi _ { j } ^ { \mathrm { P F } }$ are displayed in Box 4.1.

# 6.3 Equations of Motion for Massive Bodies

One method of obtaining equations of motion for massive bodies is to assume that each body moves on a test-body geodesic in a spacetime whose PPN metric is produced by the other bodies in the system as well as by the body itself (with proper care taken of infinite self-field terms). However, the resulting equations of motion cannot be applied to massive self-gravitating bodies, such as planets, stars, or the Sun (except in general relativity, as it turns out), because such bodies do not necessarily follow geodesics of any PPN metric. Instead, their motion may depend upon their internal structure (a violation of GWEP). This was first demonstrated by Nordtvedt (1968b). Therefore, one must treat each body realistically, as a finite, self-gravitating “ball” of matter and solve the hydrodynamic equations of motion (6.25) to obtain equations of motion for a suitably chosen center of mass of each body. For the purposes of solar-system and stellar-system experiments, it is adequate to treat the matter composing each body as perfect fluid.

In Newtonian gravitation theory, this program is straightforward. By defining an inertial mass and a center of mass for body $a$ according to

$$
\begin{array} { l } { { \displaystyle m _ { a } \equiv \int _ { a } \rho d ^ { 3 } x , } } \\ { { \displaystyle x _ { a } \equiv m _ { a } ^ { - 1 } \int _ { a } \rho x d ^ { 3 } x , } } \end{array}
$$

one can show, using the Newtonian equation of continuity (4.3), that

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \frac { d m _ { a } } { d t } = 0 , } } \\ { { } } & { { } } & { { \displaystyle \nu _ { a } \equiv \frac { d { \bf x } _ { a } } { d t } = m _ { a } ^ { - 1 } \int _ { a } \rho \nu d ^ { 3 } x , \ } } \\ { { } } & { { } } & { { \displaystyle { a _ { a } \equiv \frac { d \nu _ { a } } { d t } = m _ { a } ^ { - 1 } \int _ { a } \rho \frac { d \nu } { d t } d ^ { 3 } x , } } } \end{array}
$$

as long as there is no flux of matter from the body, such as a stellar wind, or mass ejection. Inserting the Newtonian Euler equation (4.3), we obtain the equation of motion for body $a$

$$
\begin{array} { r } { { \pmb { a } } _ { a } = { \pmb { \nabla } } \mathfrak { U } , } \end{array}
$$

where

$$
\mathfrak { U } = \sum _ { b \ne a } \left[ \frac { m _ { b } } { r _ { a b } } + \frac { 1 } { 2 } \left( I _ { b } ^ { \langle i j \rangle } + \frac { m _ { b } } { m _ { a } } I _ { a } ^ { \langle i j \rangle } \right) \nabla _ { a i } \nabla _ { a j } \frac { 1 } { r _ { a b } } + O ( r _ { a b } ^ { - 4 } ) \right] ,
$$

where $m _ { b }$ is the inertial mass of the $b$ th body, $I _ { b } ^ { \langle i j \rangle }$ is its symmetric, tracefree quadrupole moment tensor, given by

$$
I _ { b } ^ { \langle i j \rangle } \equiv \int _ { b } \rho \left( \bar { x } ^ { i } \bar { x } ^ { j } - \frac 1 3 | \bar { x } | ^ { 2 } \delta ^ { i j } \right) d ^ { 3 } x , \quad \bar { x } \equiv x - x _ { b } ,
$$

with analogous expressions for body $a$ , and $x _ { a b }$ and $r _ { a b }$ are given by

$$
{ \pmb x } _ { a b } \equiv { \pmb x } _ { a } - { \pmb x } _ { b } , \quad r _ { a b } \equiv \left| { \pmb x } _ { a b } \right| .
$$

Here we display the leading finite-size effects on the motion, proportional to the quadrupole moment of each body; a complete expression including all multipole moments may be found in PW, section 1.6.5. Because the gravitational potential is not uniform, the distribution of mass within a finite-size body can affect its own motion and that of other bodies in the system. These effects can have real-world consequences, such as tidal locking, orbital perturbations and the precession of the Earth’s angular momentum. In the limit in which the bodies are small compared to their separations, such effects decrease as $( R / r _ { a b } ) ^ { \ell }$ , with $\ell \geq 2$ , where $R$ is a characteristic size of a body.

We now wish to generalize these equations to the post-Newtonian approximation, using the PPN formalism. We will ignore all finite-size effects that vanish in the limit of small bodies, such as the multipole moment terms we just described. Because there are many different “mass densities” in the post-Newtonian limit – locally measured rest-mass $\rho$ , mass-energy density $\rho ( 1 + \Pi )$ , conserved density $\rho ^ { * }$ , and so on – there is a variety of possible definitions for inertial mass and center of mass. The main requirements for a sensible definition of center of mass are that it be located somewhere inside the body (it should not wander too far off), that it be useful and convenient, and that it be used consistently in all developments. Once these requirements are satisfied, the freedom of choice is unlimited, and ultimately the most important requirement is one of convenience. Since fluid bodies in nature tend to be spherically symmetric to a high degree, except under extreme conditions such as tidal disruption, any reasonable definition of the center of mass will place it close to the geometrical center of the body.

The choice we will make here has the advantage that the final equations of motion are simple (although “simple” is clearly a subjective statement). We define the inertial mass and the center of mass of the ath body to be

$$
\begin{array} { r c l } { { } } & { { } } & { { m _ { a } \equiv \displaystyle \int _ { a } \rho ^ { * } \left( 1 + \frac { 1 } { 2 } \bar { \nu } ^ { 2 } - \frac { 1 } { 2 } \bar { U } + \Pi \right) d ^ { 3 } x , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } &  { { \displaystyle x _ { a } \equiv \frac { 1 } { m _ { a } } \displaystyle \int _ { a } \rho ^ { * } \left( 1 + \frac { 1 } { 2 } \bar { \nu } ^ { 2 } - \frac { 1 } { 2 } \bar { U } + \Pi \right) x d ^ { 3 } x , } } \end{array}
$$

where $\overline { { \nu } } \equiv \nu - \nu _ { a ( 0 ) }$ , where, to lowest order,

$$
\nu _ { a ( 0 ) } \equiv \frac { 1 } { m _ { a } } \int _ { a } ^ { } \rho ^ { * } \nu d ^ { 3 } x ,
$$

and where

$$
\bar { U } \equiv \int _ { a } \frac { \rho ^ { * / } } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

In many post-Newtonian expressions, it will also be useful to define $\pmb { \bar { x } } \equiv \pmb { x } - \pmb { x } _ { a ( 0 ) }$ , where, to lowest order,

$$
{ \pmb x } _ { a ( 0 ) } \equiv \frac { 1 } { m _ { a } } \int _ { a } { \boldsymbol \rho } ^ { * } { \pmb x } d ^ { 3 } { \boldsymbol \chi } .
$$

Note that, roughly speaking, $m _ { a }$ is the total mass-energy of the body – rest mass of particles plus kinetic, gravitational, and internal energies – as measured in a local, comoving, nearly inertial frame surrounding the body. As long as we ignore tidal forces on the ath body, which would be proportional to its finite size, then according to our discussion of conservation laws in the PPN formalism (Section 3.2.4), $m _ { a }$ is conserved to post-Newtonian accuracy, that is,

$$
\frac { d m _ { a } } { d t } = 0 .
$$

Making use of the equation of continuity for $\rho ^ { * }$ , and using Newtonian equations of motion in any post-Newtonian terms, we obtain

$$
\nu _ { a } \equiv \frac { d x _ { a } } { d t } = \frac { 1 } { m _ { a } } \int _ { a } \left[ \rho ^ { * } \left( 1 - \frac { 1 } { 2 } \bar { \nu } ^ { 2 } - \frac { 1 } { 2 } \bar { U } + \Pi \right) \nu + p \bar { \nu } - \frac { 1 } { 2 } \rho ^ { * } \bar { W } _ { a } \right] d ^ { 3 } x ,
$$

where here and for future use we define

$$
\begin{array} { l } { { \displaystyle \bar { V } _ { a } \equiv \int _ { a } \rho ^ { * \prime } \frac { \bar { \nu } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \\ { { \displaystyle \bar { W } _ { a } \equiv \int _ { a } \rho ^ { * \prime } \frac { \bar { \nu } ^ { \prime } \cdot ( x - x ^ { \prime } ) ( x - x ^ { \prime } ) } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } . } } \end{array}
$$

The acceleration $\mathbf { \delta } _ { \pmb { a } }$ is then given by

$$
\begin{array} { l } { { \displaystyle { \vphantom { \bigg | } } { \vphantom { \bigg | } } { a _ { a } } \equiv \frac { d \nu _ { a } } { d t } } } \\ { { \displaystyle { \vphantom { \bigg | } } = \frac { 1 } { m _ { a } } \bigg \{ \int _ { a } \rho ^ { * } \bigg ( 1 - \frac { 1 } { 2 } \bar { \nu } ^ { 2 } - \frac { 1 } { 2 } \bar { U } + \Pi \bigg ) \frac { d \nu } { d t } d ^ { 3 } x + \int _ { a } ( \nu _ { a } \cdot \nabla p ) \bar { \nu } d ^ { 3 } x } \ ~ } \\ { { \displaystyle ~ + \int _ { a } \bigg ( p , 0 \bar { \nu } - \frac { p } { \rho ^ { * } } \nabla p \bigg ) d ^ { 3 } x - \frac { 1 } { 2 } \frac { d } { d t } \int _ { a } \rho ^ { * } \bar { W } _ { a } d ^ { 3 } x + \frac { 1 } { 2 } \mathcal { T } _ { a } - \frac { 1 } { 2 } \mathcal { T } _ { a } ^ { * } + \mathcal { P } _ { a } \bigg \} , } } \end{array}
$$

where $\mathcal { T } _ { a } , \mathcal { T } _ { a } ^ { * }$ and $\mathcal { P } _ { a }$ are determined purely by the internal structure of the ath body. Formulae for these and other “internal” terms are given in $\mathrm { B o x } 6 . 2$ . Notice that the acceleration of our chosen center of mass is more than just the weighted average of the accelerations of individual fluid elements, as it is in Newtonian theory. We now evaluate the first integral in Eq. (6.39) using the PPN equations of hydrodynamics (6.25). We make use of the Newtonian equations of motion where necessary to simplify post-Newtonian terms. For more details on how individual terms are evaluated, see PW, section 9.3.

Scalar integrals

$$
\begin{array} { l } { { I _ { a } \equiv \displaystyle \int _ { a } \rho ^ { * } | \vec { x } ^ { 2 } d ^ { 3 } \vec { x } , } } \\ { { \ } } \\ { { \mathcal { T } _ { a } \equiv \displaystyle \frac { 1 } { 2 } \int _ { a } \rho ^ { * } \vec { v } ^ { 2 } d ^ { 3 } \vec { x } , } } \\ { { \ } } \\ { { \Omega _ { a } \equiv - \displaystyle \frac { 1 } { 2 } \int _ { a } \frac { \rho ^ { * } \vec { v } ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } d ^ { 3 } \vec { x } ^ { \prime } d ^ { 3 } \vec { x } , } } \\ { { \ } } \\ { { \ P _ { a } \equiv \displaystyle \int _ { a } p d ^ { 3 } \vec { x } , } } \\ { { \ } } \\  { \ell _ { a } \equiv \displaystyle \int _ { a } \rho ^ { * } \Pi { \} ^ { a } \vec { x } . } } \end{array}
$$

Tensor integrals

$$
\begin{array} { r l } & { I _ { \xi } ^ { k } = \displaystyle \int _ { 0 } p ^ { - 1 / 2 } \hat { \mathcal { K } } ^ { \beta } \mathcal { K } , } \\ & { S _ { \xi } ^ { k } = \displaystyle \int _ { 0 } p ^ { - 1 / 2 } \hat { \mathcal { K } } ^ { \beta } \hat { \mathcal { K } } ^ { \beta } , } \\ & { T _ { \xi } ^ { k } = \displaystyle \int _ { 0 } p ^ { - 1 / 2 } \hat { \mathcal { K } } ^ { \beta } \hat { \mathcal { K } } ^ { \beta } \mathcal { K } , } \\ & { \bar { L } _ { \xi } ^ { k } = \displaystyle \int _ { 0 } ^ { 1 } \hat { \mathcal { C } } ^ { \beta } \hat { \mathcal { K } } \hat { \mathcal { P } } ^ { \beta } \hat { \mathcal { K } } , } \\ & { \bar { L } _ { \xi } ^ { k } = \displaystyle - \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { \rho } \hat { \mathcal { L } } ^ { \beta } \hat { \mathcal { K } } ^ { \beta } , } \\ & { \bar { \mathcal { O } } _ { \xi } ^ { k } = - \displaystyle \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } p ^ { - \rho } \frac { \gamma ^ { \prime } ( \mathcal { K } - \mathcal { K } ^ { \prime } ) ^ { \beta } ( \mathcal { K } - \mathcal { K } ^ { \prime } ) ^ { \beta } } { | \mathcal { K } - \mathcal { K } ^ { \prime } | ^ { \beta } } \hat { \mathcal { H } } _ { \gamma } ^ { \gamma } \hat { \mathcal { H } } _ { \gamma } ^ { \beta } , } \\ & { \bar { H } _ { \xi } ^ { k } = \displaystyle \int _ { 0 } ^ { 1 } p ^ { - \rho } \frac { \gamma ^ { \prime } ( \mathcal { K } - \mathcal { K } ^ { \prime } ) ^ { \beta } } { | \mathcal { K } - \mathcal { K } ^ { \prime } | ^ { \beta } } \delta ^ { \prime } \hat { \mathcal { H } } _ { \gamma } ^ { \beta } , } \\ &  \mathcal { K } _ { \xi } ^ { k } = \displaystyle \int _ { 0 } ^ { 1 } \hat { \mathcal { C } } ^ { \beta } \varphi ^ { \prime } \frac  \gamma ^ { \prime } ( \mathcal { K } - \mathcal { K } ^ { \prime } ) ( \mathcal { K } - \mathcal { K } ^ { \prime } ) ^ { \beta } ( \mathcal { K } - \mathcal { K } ^ { \prime } \ \end{array}
$$

Vector integrals

$$
\begin{array} { l } { { t _ { a } ^ { j } = \displaystyle \int _ { 0 } ^ { t } \rho ^ { * } \rho ^ { * } \frac { \tilde { V } ^ { j ^ { 2 } } \left( X - X ^ { ' } \right) ^ { j } } { | X - X ^ { ' } | ^ { 3 } } d ^ { 3 } x ^ { ' } d ^ { 3 } X } , }  \\ { { \ } } \\ { { T _ { a } ^ { j } = \displaystyle \int _ { 0 } ^ { t } \rho ^ { * } \rho ^ { * } \frac { \tilde { V } ^ { j ^ { * } } \left| \tilde { V } ^ { j ^ { * } } \left( x - X ^ { ' } \right) \right. } { | x - x ^ { ' } | ^ { 3 } } d ^ { 3 } x ^ { ' } d ^ { 3 } x , } } \\ { { \ } } \\ { { T _ { a } ^ { ' i } = \displaystyle \int _ { 0 } ^ { t } \rho ^ { * } \rho ^ { * } \frac { \tilde { V } ^ { j ^ { * } j ^ { * } } \left( x - x ^ { ' } \right) } { | X - x ^ { ' } | ^ { 3 } } d ^ { 3 } x ^ { ' } d ^ { 3 } X , } } \\ { { \ } } \\ { { T _ { a } ^ { * * j } = \displaystyle \int _ { a } ^ { t } \rho ^ { * } \rho ^ { * } \frac { \left[ \tilde { V } ^ { j ^ { * } } \cdot \left( x - x ^ { ' } \right) \right] ^ { j } \left( x - x ^ { ' } \right) ^ { j } } { | x - x ^ { ' } | ^ { 5 } } d ^ { 3 } x ^ { ' } d ^ { 3 } X , } } \\ { { \ } } \\ { { \Omega _ { a } ^ { j } \equiv \displaystyle \int _ { 0 } ^ { t } \rho ^ { * } \rho ^ { * } \rho ^ { * \prime } \frac { \left( x - x ^ { ' } \right) ^ { j } } { | x ^ { ' } - x ^ { ' } | ^ { 3 } } d ^ { 3 } x ^ { ' } d ^ { 3 } x ^ { ' } d ^ { 3 } x , } } \end{array}
$$

$$
\begin{array} { l } { { \Omega _ { a } ^ { * j } \equiv \displaystyle \int _ { a } \rho ^ { * } \rho ^ { * \prime } \rho ^ { * \prime \prime } \frac { \left( x ^ { \prime } - x ^ { \prime \prime } \right) \cdot \left( x - x ^ { \prime } \right) \left( x - x ^ { \prime } \right) ^ { j } } { \left| x ^ { \prime } - x ^ { \prime \prime } \right| ^ { 3 } \left| x - x ^ { \prime } \right| ^ { 3 } } d ^ { 3 } x ^ { \prime \prime } d ^ { 3 } x ^ { \prime } d ^ { 3 } x , } } \\ { { \displaystyle \mathcal { P } _ { a } ^ { j } \equiv \displaystyle \int _ { a } \rho ^ { * } p ^ { * \prime } \frac { \left( x - x ^ { \prime } \right) ^ { j } } { \left| x - x ^ { \prime } \right| ^ { 3 } } d ^ { 3 } x ^ { \prime } d ^ { 3 } x , } } \\ { { \displaystyle \mathcal { E } _ { a } ^ { j } \equiv \displaystyle \int _ { a } \rho ^ { * } \rho ^ { * \prime } \Pi ^ { \prime } \frac { \left( x - x ^ { \prime } \right) ^ { j } } { \left| x - x ^ { \prime } \right| ^ { 3 } } d ^ { 3 } x ^ { \prime } d ^ { 3 } x . } } \end{array}
$$

Considerable simplification of the equations results if we make use of virial identities that connect a number of integrals in Box 6.2. These identities are given, to Newtonian order, by

$$
\begin{array} { l } { { \displaystyle \frac 1 2 \frac { d } { d t } I _ { a } ^ { j k } = \frac 1 2 S _ { a } ^ { j k } + \int _ { a } \rho ^ { * } \bar { \nu } ^ { j } \bar { x } ^ { k } d ^ { 3 } x , } } \\ { { \displaystyle \frac 1 2 \frac { d ^ { 2 } } { d t ^ { 2 } } I _ { a } ^ { j k } = 2 \mathcal { T } _ { a } ^ { j k } + \Omega _ { a } ^ { j k } + \delta ^ { j k } P _ { a } , } } \\ { { \displaystyle \frac 1 2 \frac { d ^ { 3 } } { d t ^ { 3 } } I _ { a } ^ { j k } = 4 H _ { a } ^ { ( j k ) } - 3 K _ { a } ^ { j k } + \delta ^ { j k } \dot { P } _ { a } - 2 L _ { a } ^ { ( j k ) } . } } \end{array}
$$

Two vectorial identities are given by

$$
\begin{array} { r l } & { \displaystyle \frac { d } { d t } \int _ { a } \rho ^ { * } \bar { V } _ { a } ^ { j } d ^ { 3 } x = \mathcal { T } _ { a } ^ { j } + \mathcal { T } _ { a } ^ { * j } + \Omega _ { a } ^ { j } + \mathcal { P } _ { a } ^ { j } , } \\ & { \displaystyle \frac { d } { d t } \int _ { a } \rho ^ { * } \bar { W } _ { a } ^ { j } d ^ { 3 } x = - t _ { a } ^ { j } - \mathcal { T } _ { a } ^ { j } + \mathcal { T } _ { a } ^ { * j } + 3 \mathcal { T } _ { a } ^ { * * j } - \Omega _ { a } ^ { * j } - \mathcal { P } _ { a } ^ { j } , } \end{array}
$$

where we have discarded post-Newtonian corrections as well as terms that arise from external gravitational potentials, that can be shown to vary as $O ( R _ { a } ^ { 2 } / r _ { a b } ^ { 2 } )$ , where $R _ { a }$ is the characteristic size of the ath body.

We now assume that each body is in dynamical equilibrium. By this we mean that each body has had time, under its own internal dynamics, to relax to a steady state in which its internal structure does not depend on time. This means, in particular, that the structure integrals listed in Box 6.2 can all be taken to be time-independent. Then we can set equal to zero any total time derivatives of purely internal quantities, such as the left-hand-sides of Eqs. (6.43) and (6.44). This is a reasonable approximation for systems with well separated bodies, since any secular changes in the structure of the bodies that would prevent the vanishing of such averaged time derivatives occur over timescales much longer than an orbital timescale.

The final form of the equations of motion is

$$
{ \pmb a } _ { a } = ( { \pmb a } _ { a } ) _ { \mathrm { s e l f } } + ( { \pmb a } _ { a } ) _ { \mathrm { N e w t } } + ( { \pmb a } _ { a } ) _ { \mathrm { N b o d y } } ,
$$

where

$$
\begin{array} { c } { { ( a _ { a } ^ { j } ) _ { \mathrm { s e l f } } = \displaystyle - \frac 1 { m _ { a } } \left[ \frac 1 2 ( \alpha _ { 3 } + \zeta _ { 1 } ) t _ { a } ^ { j } + \frac 1 2 \zeta _ { 1 } ( 2 T _ { a } ^ { j } - 3 T _ { a } ^ { * * j } ) + \zeta _ { 2 } \Omega _ { a } ^ { j } + \zeta _ { 3 } \mathcal { E } _ { a } ^ { j } + 3 \zeta _ { 4 } P _ { a } ^ { j } \right] } } \\ { { { } } } \\ { { - \displaystyle \frac 1 { m _ { a } } \alpha _ { 3 } ( w + \nu _ { a } ) ^ { k } H _ { a } ^ { k j } , ~ } } \\ { { { } } } \end{array}
$$

$$
\begin{array} { r l } {  \mathbf { x }  _ { \mathbf { x } ^ { \prime } } = } & { - \displaystyle \sum _ { j = 0 } ^ { \infty } \frac { \sin x _ { i } } { \cos ^ { 2 } } [ \sum _ { k = 1 } ^ { n - \infty } ( \frac { \sin x _ { i } } { 2 } ( \sin ( \theta - \phi _ { i } ) + \sin ( \phi _ { i } - 1 ) \phi _ { j } )   } \\ & {   - \frac { \sin x _ { i } } { 2 } ( \sin ( \phi - \phi _ { i } ) ) \phi _ { i } ) \phi _ { i } ] } \\ & { - \displaystyle \sum _ { j = 0 } ^ { \infty } ( \frac { \sin x _ { i } } { 2 } ( \sin ( \phi - \phi _ { i } ) ) \phi _ { j } ) \phi _ { i } ( \cos ( \phi _ { i } ) \cos ( \phi _ { j } ) ) } \\ & {   \int _ { 0 } ^ { \mathcal { R } } \alpha _ { 0 } ( 1 + \sin x _ { i } ) ( \sin x _ { i } ) ( \frac { \sin x _ { i } } { 2 } ( \phi _ { i } ) - \sin ( \phi _ { i } ) ) \phi _ { i } ( \cos ( \phi _ { i } ) ) ) ] } \\ & { - \displaystyle \sum _ { j = 1 } ^ { n - \infty } \frac { \sin x _ { i } } { 2 } [ \sin ( \phi - \phi _ { i } ) ] \phi _ { i } ( \cos ( \phi _ { j } ) - \phi _ { i } ) } \\ & { - \displaystyle \sum _ { j = 0 } ^ { \infty } \frac { \sin x _ { i } } { 2 } [ \sin ( \phi + \sin x _ { i } ) ( \frac { \sin x _ { j } } { 2 } ( \phi _ { i } - \phi _ { j } ) ) \phi _ { i } ] } \\ & { - \displaystyle \sum _ { k = 1 } ^ { n - \infty } \frac { \sin x _ { i } } { 2 } [ \sin ( \phi + \sin x _ { i } ) ( \frac { \sin x _ { i } } { 2 } ( \phi - \phi _ { i } ) ) \phi _ { i } ( \cos ( \phi _ { i } ) + \sin ( \phi _ { i } ) )  } \\ &   \sum _ { k = 2 } ^ { n - \infty } \frac { \sin x _ { i } } { \sin ( \phi _ { i } ) } [ \sin ( \phi - \phi _ { i } ) + \sin ( \phi _  i  \end{array}
$$

where ${ \pmb n } _ { a b } = { \pmb x } _ { a b } / r _ { a b }$

The terms within square brackets in $\left( \pmb { a } _ { a } \right) _ { \mathrm { s e l f } } .$ , Eq. (6.46a), depend only on the internal structure of the ath body, and thus represent “self-accelerations” of the body’s center of mass. Such self-accelerations are associated with breakdowns in conservation of total momentum, since they depend on the PPN conservation-law parameters $\alpha _ { 3 }$ $, \zeta _ { 1 } , \zeta _ { 2 } ,$ $\zeta _ { 3 }$ , and $\zeta _ { 4 }$ . In any semiconservative theory of gravity

$$
\alpha _ { 3 } = \zeta _ { 1 } = \zeta _ { 2 } = \zeta _ { 3 } = \zeta _ { 4 } = 0 ,
$$

and these self-accelerations are absent. Also note that spherically symmetric bodies, or bodies with reflection symmetry about the origin (as assumed in PW) suffer no acceleration regardless of the theory of gravity, since for them the terms $t _ { a } ^ { j }$ , $\mathcal { T } _ { a } ^ { j }$ , ${ \mathcal { T } } _ { a } ^ { * * j }$ , $\Omega _ { a } ^ { j }$ , $\mathcal { E } _ { a } ^ { j }$ and $\mathcal { P } _ { a } ^ { j }$ are identically zero. The same is true for a composite massive body made up of two bodies in a nearly circular orbit, when the self-acceleration is averaged over an orbital period. Thus, there is little hope of testing the existence of these terms in the solar system because of the high degree of symmetry of the bodies and the high circularity of their orbits. However, in binary pulsars, where orbital eccentricities can be large, this effect has been tested, leading to a tight bound on $\zeta _ { 2 }$ (see Section 9.3).

The final term in Eq. (6.46a), $- m _ { a } ^ { - 1 } \alpha _ { 3 } ( w + \nu _ { a } ) ^ { k } H _ { a } ^ { k j }$ , is a self-acceleration which involves the massive body’s motion relative to the universe rest frame. It depends on the conservation-law/preferred-frame parameter $\alpha _ { 3 }$ , which is zero in any semiconservative theory of gravity. For any static body, $\bar { \nu } = 0$ , thus $H _ { a } ^ { k j }$ is zero, but for a body that rotates uniformly with angular velocity $\omega _ { a }$ , $\overline { { { \nu } } } = \omega _ { a } \times \overline { { { x } } }$ , and thus

$$
\begin{array} { c } { { H _ { a } ^ { k j } = \epsilon ^ { k \ell m } \omega _ { a } ^ { \ell } \displaystyle \int _ { a } \rho ^ { * } \rho ^ { * \prime } \frac { \bar { x } ^ { \prime m } ( x - x ^ { \prime } ) ^ { j } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } d ^ { 3 } x } } \\ { { = \epsilon ^ { k \ell m } \omega _ { a } ^ { \ell } \Omega _ { a } ^ { j m } . } } \end{array}
$$

For a nearly spherical body, the isotropic part of $\Omega _ { a } ^ { j m }$ makes the dominant contribution to Eq. (6.48), that is,

$$
\Omega _ { a } ^ { j m } \simeq \frac { 1 } { 3 } \Omega _ { a } \delta ^ { j m } , \quad H _ { a } ^ { k j } \simeq \frac { 1 } { 3 } \epsilon ^ { k \ell j } \omega _ { a } ^ { \ell } \Omega _ { a } .
$$

Then the final acceleration term in Eq. (6.46a) becomes

$$
- \frac { 1 } { 3 } \alpha _ { 3 } \frac { \Omega _ { a } } { m _ { a } } ( \pmb { w } + \pmb { \nu } _ { a } ) \times \pmb { \omega } _ { a } .
$$

In Section 8.4 we will see that this term can produce strikingly large accelerations in spinning pulsars, leading to very strong bounds on $\alpha _ { 3 }$ .

The next term, $( \pmb { a } _ { a } ) _ { \mathrm { N e w t } }$ in Eq. (6.45), is the quasi-Newtonian acceleration of the body, but it contains post-Newtonian corrections that depend on the internal structure of both body $a$ and the other bodies in the system. These corrections can be grouped together so as to appear as corrections to the “passive gravitational mass” of body $a$ and to the “active gravitational mass” of the other bodies $b$ . In fact, the passive mass turns out to be tensorial, given by

$$
\begin{array} { c } { { ( m _ { \mathrm { P } } ) _ { a } ^ { j k } = m _ { a } \bigg \{ \delta ^ { j k } \bigg [ 1 + ( 4 \beta - \gamma - 3 - 3 \xi - \alpha _ { 1 } + \alpha _ { 2 } - \zeta _ { 1 } ) \frac { \Omega _ { a } } { m _ { a } } - 3 \xi n _ { a b } ^ { \ell } n _ { a b } ^ { m } \frac { \Omega _ { a } ^ { \ell n } } { m _ { a } } \bigg ] } } \\ { { + ( 2 \xi - \alpha _ { 2 } + \zeta _ { 1 } - \zeta _ { 2 } ) \frac { \Omega _ { a } ^ { j k } } { m _ { a } } \bigg \} . } } \end{array}
$$

The quasi-Newtonian potential $\mathfrak { U } ( \pmb { x } _ { a } )$ has the form

$$
\mathfrak { U } ( { \pmb x } _ { a } ) = \sum _ { b \not = a } \frac { [ m _ { \mathrm { A } } ( { \pmb n } _ { a b } ) ] _ { b } } { r _ { a b } } ,
$$

where the active gravitational mass of the $b$ th body is given by

$$
\begin{array} { c } { { { [ m _ { \mathrm { A } } ( n _ { a b } ) ] _ { b } = m _ { b } \bigg \{ 1 + \left( 4 \beta - \gamma - 3 - 3 \xi - \frac { 1 } { 2 } \alpha _ { 3 } - \frac { 1 } { 2 } \zeta _ { 1 } - 2 \zeta _ { 2 } \right) \frac { \Omega _ { b } } { m _ { b } } + \zeta _ { 3 } \frac { E _ { b } } { m _ { b } } } } } \\ { { + \left( 3 \zeta _ { 4 } - \zeta _ { 1 } - \frac { 3 } { 2 } \alpha _ { 3 } \right) \frac { P _ { b } } { m _ { b } } + \frac { 1 } { 2 } ( \zeta _ { 1 } - 2 \xi ) n _ { a b } ^ { j } n _ { a b } ^ { k } \frac { \Omega _ { b } ^ { j k } } { m _ { b } } \bigg \} . } } \end{array}
$$

Note that the active and passive gravitational mass tensors may be functions of direction ${ \pmb n } _ { a b }$ . An alternative form of the quasi-Newtonian acceleration involves inertial, active and passive mass tensors that are independent of position, at the expense of having a complicated tensorial gravitational potential, as follows:

$$
\begin{array} { r } { { ( \tilde { m } _ { \mathrm { I } } ) _ { a } ^ { j k } ( a _ { a } ^ { k } ) _ { \mathrm { N e w t } } = ( \tilde { m } _ { \mathrm { P } } ) _ { a } ^ { \ell m } \dag \downarrow _ { , j } ^ { \ell m } , \qquad } } \\ { { \mathfrak { U } ^ { \ell m } \equiv \displaystyle \sum _ { b \ne a } ( \tilde { m } _ { \mathrm { A } } ) _ { b } ^ { m q } \frac { n _ { a b } ^ { q } n _ { a b } ^ { \ell } } { r _ { a b } } , \qquad } } \end{array}
$$

where the inertial, passive, and active mass tensors are given by

$$
\begin{array} { l } { { \displaystyle ( \tilde { m } _ { \mathrm { I } } ) _ { a } ^ { j k } \equiv m _ { a } \{ \delta ^ { j k } [ 1 + ( \alpha _ { 1 } - \alpha _ { 2 } + \zeta _ { 1 } ) \frac { \Omega _ { a } } { m _ { a } } ] + ( \alpha _ { 2 } - \zeta _ { 1 } + \zeta _ { 2 } ) \frac { \Omega _ { a } ^ { j k } } { m _ { a } } \} , } } \\ { { \displaystyle ( \tilde { m } _ { \mathrm { P } } ) _ { a } ^ { \ell m } \equiv m _ { a } \{ \delta ^ { \ell m } [ 1 + ( 4 \beta - \gamma - 3 - 3 \xi ) \frac { \Omega _ { a } } { m _ { a } } ] - \xi \frac { \Omega _ { a } ^ { \ell m } } { m _ { a } } \} , } } \\ { { \displaystyle ( \tilde { m } _ { \mathrm { A } } ) _ { b } ^ { m q } \equiv m _ { b } \{ \delta ^ { m q } [ 1 + ( 4 \beta - \gamma - 3 - 3 \xi - \frac { 1 } { 2 } \alpha _ { 3 } - \frac { 1 } { 2 } \zeta _ { 1 } - 2 \zeta _ { 2 } ) \frac { \Omega _ { b } } { m _ { b } }   } }  \\ { { \displaystyle  \qquad + \zeta _ { 3 } \frac { E _ { b } } { m _ { b } } + ( 3 \zeta _ { 4 } - \zeta _ { 1 } - \frac { 3 } { 2 } \alpha _ { 3 } ) \frac { P _ { b } } { m _ { b } } ] + \frac { 1 } { 2 } ( \zeta _ { 1 } - 2 \xi ) \frac { \Omega _ { b } ^ { m q } } { m _ { b } } \} . } } \end{array}
$$

In Newtonian theory, the active gravitational mass, the passive gravitational mass, and the inertial mass are the same, hence each massive body’s acceleration is independent of its mass or structure, in accord with the Newtonian equivalence principle. However, according to Eq. (6.55), passive gravitational mass need not be equal to inertial mass in a given metric theory of gravity, and in fact both may be anisotropic; their difference depends on several PPN parameters, and on the gravitational self-energy $\Omega$ and $\Omega ^ { j k }$ ) of the body. This is a breakdown in the gravitational Weak Equivalence Principle (GWEP) (see Section 3.3), also called the “Nordtvedt effect” after its discoverer (Nordtvedt, 1968a,b). The possibility of such an effect was first noticed by Dicke (1964) (see also Dicke (1969) and Will (1971c)). The observable consequences of the Nordtvedt effect will be discussed in Chapter 8. Its existence does not violate EEP or the Eotv ¨ os experiment (Chapter 2), ¨ because the laboratory-sized bodies considered in those situations have negligible self gravity, that is, $( \Omega / m ) _ { \mathrm { l a b ~ b o d i e s } } < 1 0 ^ { - 3 9 }$ .

According to Eq. (6.55), the active gravitational mass for massive bodies may also differ from inertial mass and from passive gravitational mass. In Newtonian gravitation theory, the conservation of momentum of an isolated system is a result of the law “action equals reaction,” that is, of the law “active gravitational mass equals passive gravitational mass.” In the PPN formalism, one can still use such Newtonian language to describe the quasi-Newtonian acceleration $( \pmb { a } _ { a } ) _ { \mathrm { N e w t } }$ . From Section 4.4, we know that momentum conservation is a property of semiconservative theories of gravity, whose parameters satisfy $\alpha _ { 3 } = \zeta _ { k } =$ 0. By substituting these values into Eq. (6.55), we find that for semiconservative theories, the active and passive mass tensors are indeed equal, and are given by

$$
( \tilde { m } _ { \mathrm { P } } ) _ { a } ^ { j k } = ( \tilde { m } _ { \mathrm { A } } ) _ { a } ^ { j k } = m _ { a } \left\{ \delta ^ { j k } \left[ 1 + ( 4 \beta - \gamma - 3 - 3 \xi ) \frac { \Omega _ { a } } { m _ { a } } \right] - \xi \frac { \Omega _ { a } ^ { j k } } { m _ { a } } \right\} .
$$

Equivalently, we can write $( \pmb { a } _ { a } ) _ { \mathrm { N e w t } }$ to post-Newtonian order in the form

$$
\begin{array} { r } { ( \tilde { m } _ { \mathrm { I } } ) _ { a } ^ { j k } ( a _ { a } ^ { k } ) _ { \mathrm { N e w t } } = \displaystyle \sum _ { b \neq a } m _ { a } m _ { b } \bigg \{ \bigg [ 1 + ( 4 \beta - \gamma - 3 - 3 \xi ) \left( \frac { \Omega _ { a } } { m _ { a } } + \frac { \Omega _ { b } } { m _ { b } } \right) \bigg ] \frac { n _ { a b } ^ { j } } { r _ { a b } ^ { 2 } } } \\ { + \xi \left( \frac { \Omega _ { a } ^ { k \ell } } { m _ { a } } + \frac { \Omega _ { b } ^ { k \ell } } { m _ { b } } \right) \frac { n _ { a b } ^ { \ell } } { r _ { a b } ^ { 2 } } \left( 2 \delta ^ { j k } - 3 n _ { a b } ^ { j } n _ { a b } ^ { k } \right) \bigg \} . } \end{array}
$$

The term in braces is manifestly antisymmetric under interchange of $a$ and $b$ , hence action equals reaction, and $\begin{array} { r } { \sum _ { a } ( \tilde { m } _ { \mathrm { I } } ) _ { a } ^ { j k } ( a _ { a } ^ { k } ) _ { \mathrm { N e w t } } = 0 } \end{array}$ .

Note that in general relativity, the mass tensors of Eq. (6.55) are isotropic and equal to the inertial mass, that is, dropping the Kronecker deltas,

$$
\left( \tilde { m } _ { \mathrm { I } } \right) = \left( \tilde { m } _ { \mathrm { P } } \right) = \left( \tilde { m } _ { \mathrm { A } } \right) = m _ { a } \quad [ \mathrm { g e n e r a l ~ r e l a t i v i t y } ] .
$$

There is no Nordtvedt effect in general relativity. However, in scalar-tensor theories, for example, the Nordtvedt effect is present; in those theories $\tilde { m } _ { \mathrm { I } } = m _ { a }$ , but

$$
\tilde { m } _ { \mathrm { P } } = \tilde { m } _ { \mathrm { A } } = m _ { a } \left[ 1 + \frac { 1 + 2 \lambda } { 2 + \omega } \frac { \Omega _ { a } } { m _ { a } } \right] .
$$

For most practical situations, we may assume that the bodies in question are spherically symmetric, then using the approximation $\Omega _ { a } ^ { j k } \simeq \textstyle { \frac { 1 } { 3 } } \delta ^ { j k } \Omega _ { a }$ to simplify the mass tensors, we may write

$$
( a _ { a } ^ { j } ) _ { \mathrm { N e w t } } = \frac { ( m _ { \mathrm { P } } ) _ { a } } { m _ { a } } \mathfrak { U } _ { , j } , \qquad \mathfrak { U } \equiv \sum _ { b \ne a } \frac { ( m _ { \mathrm { A } } ) _ { b } } { r _ { a b } } ,
$$

where we combine $( \tilde { m } _ { \mathrm { I } } ^ { j k } ) ^ { - 1 }$ and $( \tilde { m } _ { \mathrm { P } } ^ { l m } )$ into a single quantity $m _ { \mathrm { P } }$ to obtain

$$
\begin{array} { r l } & { \displaystyle \frac { ( m _ { \mathrm { P } } ) _ { a } } { m _ { a } } = 1 + \left( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } \right) \frac { \Omega _ { a } } { m _ { a } } , } \\ & { \displaystyle \frac { ( m _ { \mathrm { A } } ) _ { b } } { m _ { b } } = 1 + \left( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \frac { 1 } { 2 } \alpha _ { 3 } - \frac { 1 } { 3 } \zeta _ { 1 } - 2 \zeta _ { 2 } \right) \frac { \Omega _ { b } } { m _ { b } } } \\ & { \quad \quad \quad + \zeta _ { 3 } \frac { E _ { b } } { m _ { b } } + \left( 3 \zeta _ { 4 } - \zeta _ { 1 } - \frac { 3 } { 2 } \alpha _ { 3 } \right) \frac { P _ { b } } { m _ { b } } . } \end{array}
$$

The remaining term $( a _ { a } ^ { j } ) _ { \mathrm { N b o d y } }$ , in Eq. (6.45) is called the $N _ { ☉ }$ -body term. It contains the post-Newtonian corrections to the Newtonian equations of motion which would result from treating each body as a “point mass” moving along a geodesic of the PPN metric produced by all the other bodies, assumed to be point masses, taking account of certain post-Newtonian terms generated by the gravitational field of the body itself. It is the $N .$ -body acceleration which produces the “classical” perihelion shift of the planets, as well as a host of other effects, to be examined in Chapters 8 and 9. For the case of general relativity, the $N .$ - body terms in Eq. (6.46c) are in agreement with the equations first obtained by Lorentz and Droste (1917), and later by de Sitter (1916) (once a crucial error in de Sitter’s work has been corrected), Einstein, Infeld, and Hoffmann (1938), Levi-Civita (1965), and Fock (1964).

# 6.4 Two-Body Systems

# 6.4.1 Effective one-body equation of motion

We now truncate the PPN $N .$ -body equations of motion (6.45) and (6.46) to $N = 2$ . We consider a system of two bodies of inertial masses $m _ { 1 }$ and $m _ { 2 }$ and self-gravitational energies $\Omega _ { 1 }$ and $\Omega _ { 2 }$ . Both bodies will be assumed to be reflection symmetric about their centers of mass, so that the self-terms in Eq. (6.46a) can be dropped, but we will let the second body have a small quadrupole moment I 
ij2 a s defined in Eq. (6.30). We assume that the entire system is at rest with respect to the universe rest frame $( w = 0$ ) and that there are no other gravitating bodies near the system. In Chapter 8 we will return to the effects of motion of the system and of distant bodies (preferred-frame and preferred-location effects) on the two-body problem. For the moment we ignore them. We work in a PPN coordinate system in which the center of mass of the system is at rest at the origin. Making use of the fact that each body is nearly spherical, $\Omega _ { a } ^ { j k } \simeq \textstyle { \frac { 1 } { 3 } } \delta ^ { j k } \Omega _ { a }$ , we obtain from Eqs. (6.45) and (6.46) the acceleration of each body

$$
\begin{array} { l } { \displaystyle a _ { 1 } = \frac { ( m _ { \mathrm { P } } ) _ { 1 } } { m _ { 1 } } \nabla \mathfrak { L } _ { 1 } + \frac { m _ { 2 } n } { r ^ { 2 } } \bigg [ ( 2 \gamma + 2 \beta ) \frac { m _ { 2 } } { r } + ( 2 \gamma + 2 \beta + 1 + \frac { 1 } { 2 } \alpha _ { 1 } - \zeta _ { 2 } ) \frac { m _ { 1 } } { r } - \gamma \nu _ { 1 } ^ { 2 } } \\ { \displaystyle \quad \quad + \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) ( \nu _ { 1 } \cdot \nu _ { 2 } ) - \frac { 1 } { 2 } ( 2 \gamma + 2 + \alpha _ { 2 } + \alpha _ { 3 } ) \nu _ { 2 } ^ { 2 } + \frac { 3 } { 2 } ( 1 + \alpha _ { 2 } ) ( n \cdot \nu _ { 2 } ) ^ { 2 } \bigg ] } \\ { \displaystyle \quad \quad + \frac { m _ { 2 } n } { r ^ { 2 } } \cdot [ ( 2 \gamma + 2 ) \nu _ { 1 } - ( 2 \gamma + 1 ) \nu _ { 2 } ] \nu _ { 1 } } \\ { \displaystyle \quad \quad - \frac { 1 } { 2 } \frac { m _ { 2 } n } { r ^ { 2 } } \cdot [ ( 4 \gamma + 4 + \alpha _ { 1 } ) \nu _ { 1 } - ( 4 \gamma + 2 + \alpha _ { 1 } - 2 \alpha _ { 2 } ) \nu _ { 2 } ] \nu _ { 2 } , } \\ { \displaystyle a _ { 2 } = \{ 1  = 2 ; n  - n \} , } \end{array}
$$

where $\textbf { \em x } \equiv \textbf { \em x } _ { 1 2 }$ , $\textbf { \textit { n } } = \textbf { \textit { x } } / r$ , and $m _ { \mathrm { P } }$ is given by Eq. (6.61a). Including the Newtonian contribution of the quadrupole moment in the quasi-Newtonian potential produced by body 2 as shown in Eq. (6.29), we have

$$
\begin{array} { r l } & { ( \mathfrak { U } _ { j } ) _ { 1 } = - ( m _ { \mathrm { A } } ) _ { 2 } \displaystyle \frac { n ^ { j } } { r ^ { 2 } } - \frac { 1 5 } { 2 } I _ { 2 } ^ { \langle k \ell \rangle } \displaystyle \frac { n ^ { \langle j k \ell \rangle } } { r ^ { 4 } } , } \\ & { ( \mathfrak { U } _ { j } ) _ { 2 } = ( m _ { \mathrm { A } } ) _ { 1 } \displaystyle \frac { n ^ { j } } { r ^ { 2 } } + \frac { 1 5 } { 2 } \displaystyle \frac { ( m _ { \mathrm { A } } ) _ { 1 } } { ( m _ { \mathrm { A } } ) _ { 2 } } I _ { 2 } ^ { \langle k \ell \rangle } \displaystyle \frac { n ^ { \langle j k \ell \rangle } } { r ^ { 4 } } , } \end{array}
$$

where $m _ { \mathrm { A } }$ is given by Eq. (6.61b), and $n ^ { \langle j k \ell \rangle }$ is the symmetric tracefree combination of unit vectors, given by

$$
n ^ { \langle j k \ell \rangle } \equiv n ^ { j } n ^ { k } n ^ { \ell } - \frac { 1 } { 5 } \left( n ^ { j } \delta ^ { k \ell } + n ^ { k } \delta ^ { j \ell } + n ^ { \ell } \delta ^ { j k } \right) .
$$

In Eq. (6.63), we have ignored the difference between the inertial and active masses in the quadrupole contributions, and used active masses throughout. Even though the quadrupole terms are of Newtonian order, they are generally very small, and thus this is a reasonable approximation. For a body which is axially symmetric about an axis with direction $e$ , it can be shown that

$$
I _ { 2 } ^ { \langle k n \rangle } = - ( m _ { \mathrm { A } } ) _ { 2 } R _ { 2 } ^ { 2 } J _ { 2 ( 2 ) } \left( e ^ { k } e ^ { n } - \frac { 1 } { 3 } \delta ^ { k n } \right) ,
$$

where $R _ { 2 }$ is the mean radius of body 2, and ${ \cal J } _ { 2 ( 2 ) }$ is its dimensionless quadrupole moment ( $\ell = 2$ ), given for general axisymmetric bodies by

$$
J _ { 2 } = \frac { C - A } { m R ^ { 2 } } ,
$$

where $C$ and $A$ are the moments of inertia about the symmetry axis and about an axis in the equatorial plane, respectively.

Since the center of mass is at rest at the origin, we may replace $\nu _ { 1 }$ and $\nu _ { 2 }$ in the post-Newtonian terms in Eqs. (6.62) by

$$
\pmb { \nu } _ { 1 } = \frac { m _ { 2 } } { m } \pmb { \nu } , \quad \pmb { \nu } _ { 2 } = - \frac { m _ { 1 } } { m } \pmb { \nu } ,
$$

where

$$
\pmb { \nu } \equiv \pmb { \nu } _ { 1 } - \pmb { \nu } _ { 2 } , \quad m \equiv m _ { 1 } + m _ { 2 } .
$$

We also define the dimensionless reduced mass parameter

$$
\eta \equiv \frac { m _ { 1 } m _ { 2 } } { ( m _ { 1 } + m _ { 2 } ) ^ { 2 } } .
$$

Then the relative acceleration $\pmb { a } \equiv \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ takes the form of an effective one-body equation of motion,

$$
\begin{array} { l } { { a = - \displaystyle \frac { m ^ { * } n } { r ^ { 2 } } + \frac { 3 } { 2 } \displaystyle \frac { m R _ { 2 } ^ { 2 } J _ { 2 ( 2 ) } } { r ^ { 4 } } \left[ 5 n ( e \cdot n ) ^ { 2 } - 2 ( e \cdot n ) e - n \right] } } \\ { { { } ~ + \displaystyle \frac { m n } { r ^ { 2 } } \Bigg \{ \left[ 2 \gamma + 2 \beta + \eta ( 2 + \alpha _ { 1 } - 2 \zeta _ { 2 } ) \right] \displaystyle \frac { m } { r } } } \\ { { { } ~ - \displaystyle \frac { 1 } { 2 } \left[ 2 \gamma + \eta ( 6 + \alpha _ { 1 } + \alpha _ { 2 } + \alpha _ { 3 } ) \right] \nu ^ { 2 } + \displaystyle \frac { 3 } { 2 } \eta ( 1 + \alpha _ { 2 } ) ( \nu \cdot n ) ^ { 2 } \Bigg \} } } \\ { { { } ~ + \displaystyle \frac { m \nu ( n \cdot \nu ) } { r ^ { 2 } } \left[ 2 \gamma + 2 - \eta ( 2 - \alpha _ { 1 } + \alpha _ { 2 } ) \right] , } } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle m ^ { * } \equiv \frac { ( m _ { \mathrm { P } } ) _ { 2 } } { m _ { 2 } } ( m _ { \mathrm { A } } ) _ { 1 } + \frac { ( m _ { \mathrm { P } } ) _ { 1 } } { m _ { 1 } } ( m _ { \mathrm { A } } ) _ { 2 } } } \\ { { \displaystyle ~ = m + [ \mathrm { s e l f ~ \ e n e r g y ~ t e r m s ~ \ f o r ~ \ b o d i e s ~ \ 1 ~ \ a n d ~ \ 2 } ] . } } \end{array}
$$

The self-energy terms from Eqs. (6.61b) and (6.61a) that appear in the above expression are constant if the bodies are in quasistationary equilibrium. Furthermore, observations of a binary system can only measure the mass $m ^ { * }$ , via Kepler’s third law, for example, and thus the self-energy corrections are unmeasurable. Henceforth, we will simply drop the $( ^ { * } )$ in Eq. (6.70).

# 6.4.2 Perturbed two-body orbits and the Lagrange planetary equations

Here we provide a brief review of standard orbital perturbation theory, used to compute deviations from Keplerian two-body motion induced by perturbing forces, described by the equation of motion

$$
\pmb { a } = - \frac { m { \pmb { n } } } { r ^ { 2 } } + \delta \pmb { a } ,
$$

where $\delta \pmb { a }$ is a perturbing acceleration. For a general orbit described by $_ x$ and $\pmb { \nu } = d \pmb { x } / d t$ , we define the “osculating” Keplerian orbit using a set of orbit elements: the semilatus rectum $p$ , eccentricity $e$ , inclination $\iota$ , nodal angle $\Omega$ and pericenter angle $\omega$ , defined by the following set of equations (see Figure 6.1):

![](images/86773021c8f9e606ca7df4729591cba727d857633617d4e532172d39707e03c1.jpg)

Fig. 6.1 Elements of a general relative two-body orbit.

$$
{ \begin{array} { r l } & { x = r n , } \\ & { r \equiv p / \left( 1 + e \cos f \right) , } \\ & { n \equiv \left( \cos \Omega \cos \phi - \cos \iota \sin \Omega \sin \phi \right) e _ { X } } \\ & { \qquad + \left( \sin \Omega \cos \phi + \cos \iota \cos \Omega \sin \phi \right) e _ { Y } } \\ & { \qquad + \sin \iota \sin \phi e _ { Z } , } \\ & { \lambda \equiv \partial n / \partial \phi , \quad { \hat { h } } = n \times \lambda , } \\ & { h \equiv x \times \nu \equiv { \sqrt { m p } } { \hat { h } } , } \end{array} }
$$

where $f \equiv \phi - \omega$ is the true anomaly, $\phi$ is the orbital phase measured from the ascending node, and $e _ { A }$ are chosen reference basis vectors. From the given definitions, we see that $\pmb { \nu } = \dot { r } \pmb { n } + ( h / r ) \pmb { \lambda }$ and $\begin{array} { r } { \dot { r } = ( h e / p ) \sin f . } \end{array}$ The semilatus rectum $p$ is related to the semimajor axis $a$ by $p = a ( 1 - e ^ { 2 } )$ . One then introduces the radial $\mathcal { R }$ , cross-track $\boldsymbol { s }$ and out-of-plane $\mathcal { W }$ components of the perturbing acceleration $\delta \pmb { a }$ , defined, respectively, by $\mathcal { R } \equiv \pmb { n } \cdot \delta \pmb { a }$ , $\boldsymbol { S } \equiv \boldsymbol { \lambda } \cdot \boldsymbol { \delta a }$ and $\mathcal { W } \equiv \hat { \pmb { h } } \cdot \delta \pmb { a }$ , and writes down the “Lagrange planetary equations” for the evolution of the orbit elements,

$$
\begin{array} { r l } & { \frac { d p } { d t } = 2 \sqrt { \displaystyle \frac { p ^ { 3 } } { m } } \frac { \delta } { 1 + e \cos f } , } \\ & { \frac { d e } { d t } = \sqrt { \displaystyle \frac { p } { m } } \left[ \sin f \aleph + \frac { 2 \cos f + e + e \cos ^ { 2 } f } { 1 + e \cos f } \delta \right] , } \\ & { \frac { d \omega } { d t } = \frac { 1 } { e } \sqrt { \displaystyle \frac { p } { m } } \left[ - \cos f \aleph + \frac { 2 + e \cos f } { 1 + e \cos f } \sin f \delta - e \coth \frac { \sin ( \omega + f ) } { 1 + e \cos f } \delta \right] , } \\ & { \frac { d \dot { a } } { d t } = \sqrt { \displaystyle \frac { p } { m } } \mathcal { W } \left( \frac { r } { p } \right) \cos \phi , } \\ & { \frac { d \Omega } { d t } = \sqrt { \displaystyle \frac { p } { m } } \mathcal { W } \left( \frac { r } { p } \right) \frac { \sin \phi } { \sin \alpha } . } \end{array}
$$

(see PW, section 3.3 for further discussion.) We have not listed a sixth equation for the variation of $T _ { \ast }$ the “time of pericenter passage”; the six elements $p , e , \omega , \iota$ , and $\Omega$ and $T$ provide a complete characterization of the six orbital variables $x ( t )$ and $\mathbf { \boldsymbol { \nu } } ( t )$ . The element $T$ is relevant if the evolution of the orbit with time is the main focus. But for many applications, the evolution with orbital phase $f$ or $\phi$ is the focus. In the latter case we use Eq. (6.74) and close the system by providing equations that connect f or $\phi$ with $t$ , given by

$$
\begin{array} { l } { \displaystyle \frac { d f } { d t } = \frac { h } { r ^ { 2 } } - \frac { d \omega } { d t } - \cos \iota \frac { d \Omega } { d t } , } \\ { \displaystyle \frac { d \phi } { d t } = \frac { h } { r ^ { 2 } } - \cos \iota \frac { d \Omega } { d t } . } \end{array}
$$

These equations are exact: they are simply a reformulation of Eq. (6.72) in terms of new variables. However, they are particularly useful when the perturbations are small, so that solutions can be obtained by a process of iteration. At lowest order (no perturbations), the elements $p$ , e, $\omega$ , $\Omega$ , and $\iota$ are constant, and $d f / d t = \sqrt { m p } / r ^ { 2 }$ ; those solutions can then be plugged into the right-hand side and the equations integrated to find corrections, and so on. The corrections to the orbit elements tend to be of two classes: periodic corrections, which vary on an orbital timescale, and secular corrections, which vary on a longer timescale, depending upon the nature of the perturbations.

In many applications, such as planetary orbits in the solar system, the orbital inclinations are very small, and it is difficult to separate the variation of $\omega$ and of $\Omega$ , instead one measures variations in the pericenter direction within the orbital plane, relative to the $X$ reference axis (the equinox direction, in the case of the solar system). The variable that describes this variation is

$$
\begin{array} { l } { \displaystyle \frac { d \varpi } { d t } \equiv \frac { d \omega } { d t } + \cos \iota \frac { d \Omega } { d t } } \\ { \displaystyle = \frac { 1 } { e } \sqrt { \frac { p } { m } } \left[ - \cos f \mathcal { R } + \frac { 2 + e \cos f } { 1 + e \cos f } \mathrm { s i n } f S \right] . } \end{array}
$$

We are mainly interested in “secular” variations of the orbital elements induced by the perturbations shown in Eq. (6.70). The components of the perturbations are given by

$$
\begin{array} { l } { { \displaystyle { \mathcal R } = \frac { 3 } { 2 } \frac { m R ^ { 2 } J _ { 2 } } { r ^ { 4 } } \left[ 3 ( e \cdot n ) ^ { 2 } - 1 \right] + \frac { m } { r ^ { 2 } } \left\{ \left[ 2 \gamma + 2 \beta + \eta ( 2 + \alpha _ { 1 } - 2 \zeta _ { 2 } ) \right] \frac { m } { r } \right. } } \\ { { \displaystyle \quad \left. - \frac { 1 } { 2 } \left[ 2 \gamma + \eta ( 6 + \alpha _ { 1 } + \alpha _ { 2 } + \alpha _ { 3 } ) \right] \nu ^ { 2 } + \frac { 1 } { 2 } \left[ 4 \gamma + 4 - \eta ( 1 - 2 \alpha _ { 1 } - \alpha _ { 2 } ) \right] ( \nu \cdot n ) ^ { 2 } \right\} } } \\ { { \displaystyle \quad \mathcal S = - 3 \frac { m R ^ { 2 } J _ { 2 } } { r ^ { 4 } } ( e \cdot n ) ( e \cdot \lambda ) + \frac { m } { r ^ { 2 } } ( \nu \cdot n ) ( \nu \cdot \lambda ) \left[ 2 \gamma + 2 - \eta ( 2 - \alpha _ { 1 } + \alpha _ { 2 } ) \right] , } } \\ { { \displaystyle { \mathcal W } = - 3 \frac { m R ^ { 2 } J _ { 2 } } { r ^ { 4 } } ( e \cdot n ) ( e \cdot \hat { h } ) , \qquad } } & { { ( 6 \cdot 7 - \alpha _ { 1 } ) ( e \cdot n ) ( e \cdot n ) ^ { 2 } } } \end{array}
$$

where we have dropped the subscript “2” from $R$ and $J _ { 2 }$ . We will assume that the $X - Y - Z$ reference basis is chosen so that the symmetry axis of the body with the quadrupole moment is in the $Z .$ -direction. To calculate the changes in the orbit elements to first order in the perturbations, we substitute Eq. (6.73) into (6.77) and substitute $\mathcal { R }$ , $\boldsymbol { \mathcal { S } }$ and $\mathcal { W }$ into Eq. (6.74). We convert the equations from $d / d t$ to $d / d f$ using $d f / d t = h / r ^ { 2 }$ , and integrate over $f$ from 0 to $2 \pi$ . The resulting secular changes in the elements per orbit are given by

$$
\begin{array} { r l } & { \Delta p = 0 , } \\ & { \Delta e = 0 , } \\ & { \Delta t = 0 , } \\ & { \Delta \omega = \frac { 6 \pi m } { p } \left[ \frac { 1 } { 3 } \left( 2 + 2 \gamma - \beta \right) + \frac { 1 } { 6 } \left( 2 \alpha _ { 1 } - \alpha _ { 2 } + \alpha _ { 3 } + 2 \zeta _ { 2 } \right) \right] } \\ & { \qquad + \theta \pi J _ { 2 } \left( \frac { R } { p } \right) ^ { 2 } \left( 1 - \frac { 5 } { 4 } \sin ^ { 2 } \iota \right) , } \\ & { \Delta \Omega = - 3 \pi J _ { 2 } \left( \frac { R } { p } \right) ^ { 2 } \cos \iota . } \end{array}
$$

We will make use of the rate of pericenter advance when we turn to the orbit of Mercury in Chapter 7. We will employ the Lagrange planetary equations in Chapter 8 when we discuss orbital perturbations induced by the Nordtvedt effect and by preferred-frame and preferred-location effects, in Chapter 9 when we discuss orbital perturbations due to spin effects and in Chapters 10 and 12 when we discuss orbits involving compact bodies, such as binary pulsar systems and bodies orbiting supermassive black holes.

# 6.5 Semiconservative Theories and N-body Lagrangians

The overwhelming majority of modern alternative theories of gravity are based on an invariant action principle, and so they automatically generate a post-Newtonian limit that is semiconservative. It is therefore appropriate to re-express the post-Newtonian $N .$ -body equations of motion with the constraints $\alpha _ { 3 } = \zeta _ { k } = 0$ . In a PPN coordinate frame at rest with respect to the universe rest frame, the resulting equations consist of the standard Newtonian acceleration (here we ignore the GWEP violating effects on the inertial, passive and active masses) plus the post-Newtonian $N .$ -body acceleration $\pmb { a } _ { \mathrm { N b o d y } }$ , Eq. (6.46c) with $w = 0$ and with semiconservative PPN parameters,

$$
\begin{array} { r l } { \langle a _ { k } \rangle _ { \mathrm { b o t } } = } & { - \displaystyle \sum _ { \tilde { \phi } \neq \infty } \frac { m A _ { k } \rho _ { k } ^ { 2 } } { \nu _ { \phi } ^ { 2 } } \bigg \{ 1 + \gamma _ { \phi } ^ { 2 } - ( 2 \gamma _ { \tilde { \phi } } + 2 ) ( \nu _ { \phi } \cdot \nu _ { \phi } ) + ( \gamma + 1 ) \gamma _ { \phi } ^ { 2 } - \frac { 3 } { 2 } ( \alpha _ { k } \cdot \nu _ { \phi } ) ^ { 2 } } \\ & { + \displaystyle \frac { 1 } { 2 } ( \kappa _ { \phi } + \nu _ { \phi } ) ^ { 2 } - \frac { 1 } { 2 } \alpha _ { k } ( \kappa + \nu _ { \phi } ) \cdot ( \nu + \nu _ { \phi } ) - \frac { 3 } { 2 } \alpha _ { \tilde { \phi } } \rho _ { k } \rho _ { k } \cdot ( \kappa + \nu _ { \phi } ) \bigg \} } \\ & { - \left( 2 \gamma + 2 \delta + 1 + \frac { 1 } { 2 } \alpha _ { k } ^ { 2 } \right) \rho _ { k \phi } ^ { 2 } - \langle \gamma + 2 \rangle ^ { 2 } \rho _ { k \phi } ^ { 2 } \bigg \} } \\ & { + \displaystyle \sum _ { \tilde { \phi } \neq \infty } \frac { m _ { \tilde { \phi } } } { \nu _ { \phi } } \alpha _ { k } \cdot [ ( 2 \gamma - 2 ) \nu _ { \phi } - ( 2 \gamma + 1 ) \nu _ { \phi } ] ( \nu _ { \phi } - \nu _ { \phi } ) } \\ & { - \displaystyle \sum _ { \tilde { \phi } \neq \infty } \frac { m _ { \tilde { \phi } } } { \nu _ { \phi } } \alpha _ { k } \cdot [ \sigma _ { \phi } ( \nu _ { \phi } + \nu _ { \phi } ) + \frac { 1 } { 2 } \alpha _ { 1 } ( \alpha _ { k } \cdot \nu _ { \phi } ) ] ( \nu _ { \phi } + \nu _ { \phi } ) } \\ & { + \displaystyle \sum _ { \tilde { \phi } \neq \infty } \sum _ { \phi \neq \infty } \frac { m _ { \tilde { \phi } } \rho _ { k } } { \nu _ { \phi } } \alpha _ { \tilde { \phi } } \bigg [ ( 2 \gamma + 2 \delta - 2 ) \frac { 1 } { \nu _ { \phi } } + ( 2 \beta - 1 - 2 \xi ) \frac { 1 } { \alpha _ { k } } } \\ &  - \displaystyle \frac { 1 } { 2 } ( 1 + 2 \xi  \end{array}
$$

$$
\begin{array} { l } { \displaystyle - \frac { 1 } { 2 } \big ( 4 \gamma + 3 - 2 \xi + \alpha _ { 1 } - \alpha _ { 2 } \big ) \sum _ { b \ne a } \sum _ { c \ne a , b } \frac { m _ { b } m _ { c } } { r _ { a b } r _ { b c } ^ { 2 } } { \pmb { n } } _ { b c } } \\ { \displaystyle - \xi \sum _ { b \ne a } \sum _ { c \ne a , b } \frac { m _ { b } m _ { c } } { r _ { a b } ^ { 3 } } \bigg [ \big ( { \pmb { n } } _ { a c } - { \pmb { n } } _ { b c } \big ) - 3 { \pmb { n } } _ { a b } \cdot \big ( { \pmb { n } } _ { a c } - { \pmb { n } } _ { b c } \big ) { \pmb { n } } _ { a b } \bigg ] . } \end{array}
$$

Remarkably, these equations of motion can be derived from the Euler-Lagrange equations obtained by varying the trajectory $x _ { q } ( t ) , \nu _ { q } ( t )$ of the $q$ th particle in the action

$$
I _ { \mathrm { N b o d y } } = \int L d t ,
$$

where

$$
\begin{array} { l } { { L = - \displaystyle \sum _ { a } m _ { a } \left( 1 - \frac { 1 } { 2 } \nu _ { a } ^ { 2 } - \frac { 1 } { 8 } \nu _ { a } ^ { 4 } \right) } } \\ { { \ ~ + \displaystyle \frac { 1 } { 2 } \sum _ { a } \sum _ { b \neq a } \frac { m _ { a } m _ { b } } { r _ { a b } } \biggl [ 1 - \frac { 1 } { 2 } \nu _ { a } ^ { 2 } - \frac { 1 } { 4 } ( 4 \gamma + 3 ) | \nu _ { a } - \nu _ { b } | ^ { 2 } - \frac { 1 } { 2 } \bigl ( \nu _ { a } \cdot n _ { a b } \bigr ) \bigl ( \nu _ { b } \cdot n _ { a b } \bigr ) \biggr ] ~ } } \\ { { \ ~ - \displaystyle \frac { 1 } { 2 } ( \alpha _ { 1 } - \alpha _ { 2 } ) \bigl ( w + \nu _ { a } \bigr ) \cdot ( w + \nu _ { b } ) - \frac { 1 } { 2 } \alpha _ { 2 } \bigl ( w + \nu _ { a } \bigr ) \cdot n _ { a b } \bigl ( w + \nu _ { b } \bigr ) \cdot n _ { a b } } } \\ { { \ ~ - \left( 2 \beta - 1 \right) \sum _ { c \neq a } \frac { m _ { c } } { r _ { a c } } - \xi \frac { x _ { a b } } { r _ { a b } ^ { 2 } } \cdot \sum _ { c \neq a b } ^ { 2 } m _ { c } \left( \frac { x _ { b c } } { r _ { a c } } - \frac { x _ { a c } } { r _ { b c } } \right) \biggr ] . } } \end{array}
$$

A Hamiltonian $H$ can then be constructed from $L$ in the usual way by defining $p _ { a } ^ { j } \equiv \partial L / \partial \nu _ { a } ^ { j }$ and $\begin{array} { r } { H { = } \sum _ { a } { p _ { a } \cdot \nu _ { a } - L } } \end{array}$ , with the result

$$
\begin{array} { c } { { H = \displaystyle \sum _ { a } \left( m _ { a } + \frac { p _ { a } ^ { a } } { 2 m _ { a } } - \frac { p _ { a } ^ { 4 } } { 8 m _ { a } ^ { 3 } } \right) } } \\ { { - \displaystyle \frac { 1 } { 2 } \sum _ { a } \displaystyle \sum _ { b \neq a } \frac { m _ { a } m _ { b } } { r _ { a b } } \biggl [ 1 + ( 2 \gamma + 1 ) \frac { p _ { a } ^ { 2 } } { m _ { a } ^ { 2 } } - \frac { 1 } { 2 } ( 4 \gamma + 3 + \alpha _ { 1 } - \alpha _ { 2 } ) \frac { p _ { a } \cdot p _ { b } } { m _ { a } m _ { b } } } } \\ { { - \displaystyle \frac { 1 } { 2 } ( 1 + \alpha _ { 2 } ) \frac { ( p _ { a } \cdot n _ { a b } ) ( p _ { b } \cdot n _ { a b } ) } { m _ { a } m _ { b } } - ( 2 \beta - 1 ) \sum _ { c \neq a } \frac { m _ { c } } { r _ { a c } } } } \\ { { - \xi \frac { x _ { a b } } { r _ { a b } ^ { 2 } } \cdot \displaystyle \sum _ { c \neq a } m _ { c } \left( \frac { x _ { b c } } { r _ { a c } } - \frac { x _ { a c } } { r _ { b c } } \right) \biggr ] , } } \end{array}
$$

where we have set $w = 0$ , for simplicity. A Hamiltonian formulation of the equations of motion is useful for analyzing the dynamics of many-body systems.

# 6.6 The Locally Measured Gravitational Constant

Here, we derive an equation which is not really an equation of motion, but is nevertheless a fundamental result within the PPN formalism. In the previous section, we found that some metric theories of gravity could predict a violation of GWEP (Nordtvedt effect). Such effects represent violations of the Strong Equivalence Principle (SEP). As discussed in Section 3.3, the existence of preferred-frame and preferred-location effects in local gravitational experiments would also represent violations of SEP. One such local gravitational experiment is a measurement of Newton’s constant $G$ , usually called the Cavendish experiment, in honor of the experiments carried out by Henry Cavendish in the late 1700s. In an idealized version of this experiment one measures the relative acceleration of two bodies as a function of their masses and of the distance between them. Distances and times are measured by means of physical rods and atomic clocks at rest in the laboratory. The gravitational constant G is then identified as that number with dimensions $\mathrm { c m } ^ { 3 } \mathrm { g } ^ { - 1 } \mathrm { s } ^ { - 2 }$ which appears in Newton’s law of gravitation for the two bodies. This quantity is called the locally measured gravitational constant $G _ { \mathrm { L } }$ .

The analysis of this experiment proceeds as follows: a body of mass $m _ { 1 }$ (source) falls freely through spacetime. A test body with negligible mass moves through spacetime, maintained at a constant proper distance $r _ { p }$ from the source by a four-acceleration A provided by some nongravitational force. The line joining the pair of masses is nonrotating relative to asymptotically flat inertial space. An invariant “radial” unit four-vector $\mathsf { E } _ { r }$ , points from the test mass toward the source. Then according to Newton’s law of gravitation the radial component of the four-acceleration of the test mass is given by

$$
\mathsf { A } \cdot \mathsf { E } _ { r } \equiv - G _ { \mathrm { L } } \frac { m _ { 1 } } { r _ { p } ^ { 2 } } ,
$$

for $r _ { p }$ small compared to the scale of inhomogeneities in the external gravitational fields. Since the quantity $\mathsf { A } \cdot \mathsf { E } _ { r }$ is invariant, we can calculate it in a suitably chosen PPN coordinate system, then use Eq. (6.83) to read off the locally measured $G _ { \mathrm { L } }$ .

Before carrying out the computation, however, it is instructive to ask what might be expected for the form of $\mathsf { A } \cdot \mathsf { E } _ { r }$ to post-Newtonian order. We imagine that the source and the test body are moving with respect to the universe with velocity $w _ { 1 }$ and are in the presence of some external sources, idealized as point masses of mass $m _ { a }$ at location $x _ { a }$ . It is simplest to do the calculation in a PPN coordinate system in which the source is momentarily at rest. Then we would expect $\mathtt { A } \cdot \mathtt { E } _ { r }$ to contain post-Newtonian corrections to the equation $\mathtt { A } \cdot \mathtt { E } _ { r } = m _ { 1 } / r _ { p } ^ { 2 }$ of the form

$$
\mathsf { A } \cdot \mathsf { E } _ { r } : \quad \frac { m _ { 1 } } { r _ { p } ^ { 2 } } \frac { m _ { 1 } } { r _ { p } } , \quad \frac { m _ { 1 } } { r _ { p } ^ { 2 } } \frac { m _ { a } } { r _ { 1 a } } , \quad \frac { m _ { 1 } } { r _ { p } } \frac { m _ { a } } { r _ { 1 a } ^ { 2 } } , \quad \frac { m _ { 1 } } { r _ { p } ^ { 2 } } \big ( w _ { 1 } ^ { 2 } \big ) ,
$$

where $r _ { 1 a } = | { \pmb x } _ { 1 } - { \pmb x } _ { a } |$ . In obtaining these possible corrections, we have neglected the variation of the external gravitational potentials across the separation $r _ { p }$ . Such a variation will produce the standard Newtonian tidal gravitational force, which is of the form

$$
\big ( \mathsf { A } \cdot \mathsf { E } _ { r } \big ) _ { \mathrm { t i d a l } } : \qquad \frac { m _ { a } } { r _ { 1 a } ^ { 3 } } r _ { p } ,
$$

and post-Newtonian corrections to this force. We will neglect such forces throughout. The first term in Eq. (6.84) represents post-Newtonian modifications in the two-body motion of the test body about the source; these can be understood and analyzed separately from a discussion of $G _ { \mathrm { L } }$ . The third term represents effects due to the gradients of the external fields; however, if we fit $\mathsf { A } \cdot \mathsf { E } _ { r }$ to an $r _ { p } ^ { - 2 }$ curve in order to determine $G _ { \mathrm { L } }$ , these terms will have no effect (in most practical situations, they are smaller than the terms we are interested in by factors of $r _ { p } / r _ { 1 a }$ ). We will drop both types of terms throughout the analysis. Thus, we retain only terms of the form $( m _ { 1 } / r _ { p } ^ { 2 } ) ( m _ { a } / r _ { 1 a } )$ or $( m _ { 1 } / r _ { p } ^ { 2 } ) w _ { 1 } ^ { 2 }$ .

The form of the PPN metric that we will use is given by the expression in $\mathrm { B o x } 4 . 1$ , where now the velocity $\pmb { w }$ is the source’s velocity relative to the mean rest frame of the universe, denoted $w _ { 1 }$ . We label the test body by $a = 0$ , the source by $a = 1$ and the remaining bodies by $a = 2$ , 3, . . . . lnitially, both the source and test body are at rest, that is,

$$
\pmb { \nu } _ { 1 } ( t = 0 ) = \pmb { \nu } _ { 0 } ( t = 0 ) = 0 .
$$

We separate the Newtonian gravitational potential $U _ { 1 }$ due to the source from that due to the other bodies in the system:

$$
U ( { \pmb x } ) = U _ { 1 } ( r _ { 1 } ) + \sum _ { a \neq 1 } { \frac { m _ { a } } { r _ { a } } } ,
$$

where $r _ { 1 } = | { \pmb x } - { \pmb x } _ { 1 } |$ , $r _ { a } = | { \pmb x } - { \pmb x } _ { a } |$ , and $U _ { 1 }$ is assumed for simplicity to be spherically symmetric.

The proper distance between the test body and the source is given by applying Eq. (3.48), with the result

$$
\begin{array} { l } { { r _ { p } = \displaystyle \int _ { x _ { 0 } } ^ { x _ { 1 } } \left[ 1 + \gamma U ( { \pmb x } ) + O ( \epsilon ^ { 2 } ) \right] d | { \pmb x } | } } \\ { { = r _ { 0 1 } \left( 1 + \gamma \displaystyle \sum _ { a \neq 1 } \frac { m _ { a } } { r _ { 1 a } } \right) , } } \end{array}
$$

where, in line with our starting assumptions, we have neglected the variation of the external gravitational potential across the separation $r _ { 0 1 }$ and we have dropped the term arising from the integral of $U _ { 1 }$ from $x _ { 0 }$ to $x _ { 1 }$ because it leads to effects only in the two-body motion of the test body about the source. The proper distance $r _ { p }$ is to be kept constant by the four-acceleration $A$ , thus

$$
\frac { d r _ { p } } { d t } = \frac { d ^ { 2 } r _ { p } } { d t ^ { 2 } } = 0 .
$$

Recalling that $\pmb { \nu } _ { 1 } = \pmb { \nu } _ { 0 } = 0$ at $t = 0$ , it is simple to show that this implies that

$$
{ \pmb n } _ { 0 1 } \cdot \left( \frac { d { \pmb \nu } _ { 0 } } { d t } - \frac { d { \pmb \nu } _ { 1 } } { d t } \right) = 0 ,
$$

where ${ \pmb n } _ { 0 1 } \equiv { \pmb x } _ { 0 1 } / r _ { 0 1 }$

We now assume that the source follows a geodesic of spacetime, but that the test body undergoes a four-acceleration $A$ , so that

$$
\begin{array} { r } { u _ { \mathrm { s o u r c e } } ^ { \nu } u _ { \mathrm { s o u r c e } ; \nu } ^ { \mu } = 0 , \quad } \\ { u _ { \mathrm { t e s t } } ^ { \nu } u _ { \mathrm { t e s t } ; \nu } ^ { \mu } = A ^ { \mu } , } \end{array}
$$

with $u _ { \mathrm { t e s t } } ^ { \mu } A _ { \mu } = 0$ . In PPN coordinates, with $\pmb { \nu } _ { 1 } = \pmb { \nu } _ { 0 } = 0$ , this may expressed at $t = 0$ as

$$
\begin{array} { l } { { \displaystyle { \frac { d { \nu } _ { 1 } ^ { j } } { d t } } + \Gamma _ { 0 0 } ^ { j } ( { \pmb x } _ { 1 } ) = 0 } , \ ~ } \\ { { \displaystyle { \frac { d { \nu } _ { 0 } ^ { j } } { d t } } + \Gamma _ { 0 0 } ^ { j } ( { \pmb x } _ { 0 } ) = \left( \displaystyle { \frac { d \tau } { d t } } \right) ^ { 2 } A ^ { j } } , } \end{array}
$$

with $A ^ { 0 } = 0$ , where, for the test body,

$$
\left( \frac { d \tau } { d t } \right) ^ { 2 } = 1 - 2 \sum _ { a \ne 1 } \frac { m _ { a } } { r _ { 1 a } } + O ( \epsilon ^ { 2 } ) ,
$$

where we again ignore spatial variations in external potentials and drop the contribution of the source potential. We use the PPN Christoffel symbol $\Gamma _ { 0 0 } ^ { j }$ from $\mathrm { B o x } 6 . 1$ , and retain only the terms discussed earlier. Substituting Eq. (6.92) into Eq. (6.90), and including the Newtonian tidal force for illustration, we obtain

$$
\begin{array} { l } { { \displaystyle \mathbb { A } \cdot e = - 3 r _ { 1 0 } e ^ { j } e ^ { k } \sum _ { a \neq 1 } \frac { m _ { a } n _ { 1 a } ^ { \prime } } { r _ { 1 a } ^ { 3 } } } } \\ { { \displaystyle \qquad - e \cdot \nabla U _ { 1 } \bigg [ 1 - ( 4 \beta + 2 \gamma - 3 - \zeta _ { 2 } - 4 \xi ) \sum _ { a \neq 1 } \frac { m _ { a } } { r _ { 1 a } } - \frac { 1 } { 2 } ( \alpha _ { 1 } - \alpha _ { 3 } ) w _ { 1 } ^ { 2 } \bigg ] } } \\ { { \displaystyle \qquad - e \cdot \nabla X _ { 1 , j k } \left[ \frac { 1 } { 2 } \alpha _ { 2 } w _ { 1 } ^ { j } w _ { 1 } ^ { k } - \xi \sum _ { a \neq 1 } \frac { m _ { a } n _ { 1 a } ^ { j } n _ { 1 a } ^ { k } } { r _ { 1 a } } \right] , } } \end{array}
$$

where $e \equiv n _ { 0 1 }$ , and

$$
n _ { 1 a } ^ { \langle j k \rangle } = n _ { 1 a } ^ { j } n _ { 1 a } ^ { k } - \frac { 1 } { 3 } \delta ^ { j k } .
$$

For a spherically symmetric body, the potential $U _ { 1 }$ and superpotential $X _ { 1 }$ are given by

$$
U _ { 1 } = \frac { m _ { 1 } } { r _ { 0 1 } } , \qquad X _ { 1 } = m _ { 1 } r _ { 0 1 } + \frac { 1 } { 3 } \frac { I _ { 1 } } { r _ { 0 1 } } ,
$$

where $I _ { 1 }$ is the source’s spherical moment of inertia, given by

$$
I _ { 1 } = \int _ { 1 } \rho ^ { * } r ^ { 2 } d ^ { 3 } x .
$$

The radial unit four-vector $\mathsf { E } _ { r }$ is proportional to the coordinate unit vector, $E _ { r } ^ { j } = - \alpha n _ { 0 1 } ^ { j }$ , with $E _ { r } ^ { 0 } = 0$ . Imposing the normalization $g _ { \mu \nu } E _ { r } ^ { \mu } E _ { r } ^ { \nu } = 1$ , and including in the metric only external potentials, we obtain

$$
E _ { r } ^ { j } = - n _ { 0 1 } ^ { j } \left( 1 - \gamma \sum _ { a \neq 1 } \frac { m _ { a } } { r _ { 1 a } } \right) .
$$

The final result for the invariant radial component of the four-acceleration $A$ is

$$
\begin{array} { r l r } {  { \mathrm { A } \cdot \mathrm { E } _ { r } = \sum _ { a \not = 1 } ^ { m _ { a } r _ { p } } [ 3 ( n _ { 1 a } \cdot e ) ^ { 2 } - 1 ] } } \\ & { } & { + \frac { m _ { 1 } } { r _ { | a } ^ { 2 } } \{ 1 - ( 4 \beta - \gamma - 3 - \zeta _ { 2 } - 3 \xi ) \sum _ { a \not = 1 } \frac { m _ { a } } { r _ { | a } } - \frac { 1 } { 2 } ( \alpha _ { 1 } - \alpha _ { 2 } - \alpha _ { 3 } ) w _ { 1 } ^ { 2 }  } \\ & { } & {  - \frac { 1 } { 2 } \alpha _ { 2 } ( w _ { 1 } \cdot e ) ^ { 2 } + \xi \sum _ { a \not = 1 } \frac { m _ { a } } { r _ { | a } } ( n _ { 1 a } \cdot e ) ^ { 2 }  } \\ & { } & { +  \frac { I _ { 1 } } { m _ { 1 } r _ { p } ^ { 2 } } ( 3 e ^ { j } e ^ { k } - \delta ^ { j k } ) [ \frac { 1 } { 2 } \alpha _ { 2 } w _ { 1 } ^ { j } w _ { 1 } ^ { k } - \xi \sum _ { a \not = 1 } \frac { m _ { a } } { r _ { 1 a } } n _ { 1 a } ^ { j } n _ { 1 a } ^ { k } ] \} . } \end{array}
$$

The first term in Eq. (6.99) is simply the Newtonian tidal acceleration; minimizing these accelerations is a significant challenge in real-life Cavendish experiments. From the second term, we can read off the locally measured gravitational constant,

$$
\begin{array} { c } { { G _ { \mathrm { L } } = 1 - \left[ 4 \beta - \gamma - 3 - \zeta _ { 2 } - \xi \left( 3 + \chi \right) \right] U _ { \mathrm { e x t } } - \displaystyle \frac 1 2 \left[ \alpha _ { 1 } - \alpha _ { 3 } - \alpha _ { 2 } \left( 1 - \chi \right) \right] w _ { 1 } ^ { 2 } } } \\ { { - \displaystyle \frac 1 2 \alpha _ { 2 } \left( 1 - 3 \chi \right) \left( w _ { 1 } \cdot e \right) ^ { 2 } + \xi \left( 1 - 3 \chi \right) U _ { \mathrm { e x t } } ^ { j k } e ^ { j } e ^ { k } , } } \end{array}
$$

where

$$
U _ { \mathrm { e x t } } \equiv { \frac { m _ { a } } { r _ { 1 a } } } , \quad U _ { \mathrm { e x t } } ^ { j k } \equiv { \frac { m _ { a } } { r _ { 1 a } } } n _ { 1 a } ^ { j } n _ { 1 a } ^ { k } ,
$$

and

$$
\chi \equiv \frac { I _ { 1 } } { m _ { 1 } r _ { p } ^ { 2 } } .
$$

Here, we see a direct example of the possibility of violations of the Strong Equivalence Principle, via preferred-frame or preferred-location effects in local Cavendish experiments. The preferred-frame effects depend upon the velocity $w _ { 1 }$ of the source relative to the universe rest frame, and are present unless the PPN preferred-frame parameters $\alpha _ { 1 } , \alpha _ { 2 }$ , and $\alpha _ { 3 }$ all vanish. The preferred-location effects depend upon the gravitational potentials $U _ { \mathrm { e x t } }$ and $U _ { \mathrm { e x t } } ^ { j k }$ of nearby bodies, and are present in general unless the PPN parameters satisfy $4 \beta - \gamma - 3 - \zeta _ { 2 } = \xi = 0$ . We note that general relativity predicts that $G _ { \mathrm { { L } } } = 1$ .

For an alternative derivation of $G _ { \mathrm { L } }$ that involves transforming the PPN metric to a locally comoving quasi-inertial frame of a chosen massive body and examining the effective “Newtonian” potential of that body in the presence of motion relative to the preferred frame and of external matter, see PW section 13.2.6.

# 6.7 Equations of Motion for Spinning Bodies

In Section 6.3 we ignored the finite extent of each body, except insofar as it would permit internal kinetic, gravitational and other forms of energy. We ignored any finite-size effects that would lead to tidal interactions and their post-Newtonian corrections, for example. But this meant that we also ignored the effects of rotation or spin of the bodies. But rotation is everywhere, and it is important to incorporate it in a description of the motion of an $N .$ -body system. In gravitational physics, it is becoming increasingly clear that spin effects play a central role in such phenomena as binary black-hole inspirals, gravitational collapse, accretion onto compact objects, and the emission of gravitational radiation. In addition, several key experimental tests of general relativity have involved the effects of spin. By spin, we mean the macroscopic rotation of an extended body, and not the quantummechanical spin of an elementary particle.

The motion of spinning bodies in curved spacetime has been a subject of considerable research for many years. This research has been aimed at discovering (i) how a body’s spin alters its trajectory (deviations from geodesic motion) and (ii) how a body’s motion in curved spacetime alters its spin. No rigorous solution is available for these problems because of the difficulties in defining a center of mass of a spinning body in curved spacetime. The extensive literature on this subject includes work by Mathisson (1937), Papapetrou (1951), Corinaldesi and Papapetrou (1951), Barker and O’Connell (1974), and Dixon (1979). For a review of this history, see Havas (1989).

However, in the post-Newtonian approximation, it is relatively straightforward to incorporate spin. In this section we sketch the method for obtaining both the equations of motion for the center-of-mass of each spinning body, and the evolution equations for the spin of each body. More details can be found in PW, chapters 9 and 13.

The starting point is a simple and natural definition of the spin tensor (see Box 6.2),

$$
S _ { a } ^ { j k } \equiv \int _ { a } \rho ^ { * } \left( \bar { x } ^ { j } \bar { \nu } ^ { k } - \bar { x } ^ { k } \bar { \nu } ^ { j } \right) d ^ { 3 } x ,
$$

where $\bar { \pmb { x } } \equiv \pmb { x } - \pmb { x } _ { a ( 0 ) }$ and $\overline { { \pmb { \nu } } } \equiv \pmb { \nu } - \pmb { \nu } _ { a ( 0 ) }$ are the position and velocity of a fluid element relative to the body’s baryonic center of mass, defined by Eq. (6.35). We also introduce a vectorial version of the spin angular momentum, defined by

$$
\pmb { S } _ { a } \equiv \int _ { a } \rho ^ { * } \pmb { \overline { { x } } } \times \pmb { \overline { { \nu } } } d ^ { 3 } x .
$$

It is easy to show that the tensor and vector are related by

$$
S _ { a } ^ { j } = \frac 1 2 \epsilon ^ { j p q } S _ { a } ^ { p q } , \qquad S _ { a } ^ { j k } = \epsilon ^ { j k p } S _ { a } ^ { p } .
$$

# Box 6.3

# World lines for spinning bodies

For spinning bodies, there is a basic ambiguity in the definition of the world line $x _ { a }$ of the body. To understand this, we define a four-tensor spin quantity for body $a$ by the equation

$$
J _ { a } ^ { \mu \nu } \equiv 2 \int _ { a } \rho ^ { * } ( \boldsymbol { x } ^ { [ \mu } - \tilde { \chi } _ { a } ^ { [ \mu } ) \boldsymbol { v } ^ { \nu ] } d ^ { 3 } x ,
$$

a form modeled after Eq. (4.69), with the center of the coordinate system there being replaced with the variable ${ \widetilde { X } } _ { a } ^ { \mu }$ which denotes the “representative world line”of the body. Here $x ^ { 0 } = \tilde { x } _ { a } ^ { 0 } = t , \mathsf { a n d } v ^ { 0 } = 1 .$ Then it is straightforward to show that

$$
\begin{array} { l } { { J _ { a } ^ { 0 j } = - m _ { a } ( x _ { a } ^ { j } - \tilde { x } _ { a } ^ { j } ) , } } \\ { { J _ { a } ^ { j k } = \varsigma _ { a } ^ { j k } + 2 m _ { a } ( x _ { a } ^ { [ j } - \tilde { x } _ { a } ^ { [ j } ) v _ { a } ^ { k ] } . } } \end{array}
$$

To relate the baryonic center of mass $\chi _ { a } ^ { j }$ to the world-line $\widetilde { \chi } _ { a } ^ { j }$ we must constrain $J _ { a } ^ { 0 j }$ . One possibility is to require ${ \cal J } _ { a } ^ { 0 j } = 0 , { \sf s o }$ that $\begin{array} { r } { \chi _ { a } ^ { j } = \widetilde { \chi } _ { a } ^ { j } , } \end{array}$ and the spin tensor $J _ { a } ^ { \mu \nu }$ is purely spatial in the PPN coordinate frame. But another possibility is to impose the “covariant” condition

$$
{ \cal J } _ { a } ^ { \mu \nu } u _ { a \nu } = 0 ,
$$

where $u _ { a } ^ { \mu }$ is the body’s four-velocity. This condition asserts that the spin tensor $J _ { a } ^ { \mu \nu }$ is purely spatial in the body’s rest-frame. To lowest PN order, it can be expressed in the form

$$
{ \cal J } _ { a } ^ { 0 j } = - { \cal J } _ { a } ^ { j k } { \cal V } _ { a } ^ { k } .
$$

One can interpolate between the two conditions using a parameter $\lambda ,$ with $J _ { a } ^ { 0 j } = - \lambda J _ { a } ^ { j k } v _ { a } ^ { k } ,$ leading to a relation between the center of mass and the world-line given to lowest PN order by

$$
x _ { a } ^ { j } = \tilde { x } _ { a } ^ { j } + \lambda m _ { a } ^ { - 1 } S _ { a } ^ { j k } v _ { a } ^ { k } .
$$

Note that the difference between these world line definitions is of post-Newtonian order. The condition that fixes the representative world line of a spinning body is often called a “spin supplementary condition”(Barker and O’Connell, 1974). This is another example of the ambiguity inherent in defining the center of mass or the world line of an extended body. The important thing is to make a choice and to maintain that choice throughout all calculations.

It is then relatively straightforward to return to Section 6.3 and redo the calculation of the equations of motion for a system of bodies, but now including specific finite-size terms in which the combination $\bar { \nu } ^ { j } \bar { x } ^ { k }$ is integrated over a body, leading to a term proportional to $S _ { a } ^ { j k }$ . Only terms linear in the extent ${ \bar { x } } ^ { k }$ for any given body are kept, with the result that only terms linear in spins, or involving the product of spins of two different bodies are kept. It turns out that one of the virial relations of Eq. (6.43) is modified by a term involving spin:

$$
\frac 1 2 \frac { d ^ { 3 } } { d t ^ { 3 } } J _ { a } ^ { j k } = 4 H _ { a } ^ { ( j k ) } - 3 K _ { a } ^ { j k } + \delta ^ { j k } \dot { P } _ { a } - 2 L _ { a } ^ { ( j k ) } + 3 S _ { a } ^ { p ( j } \sum _ { b } \frac { m _ { b } } { r _ { a b } ^ { 3 } } { ( n _ { a b } ^ { k ) } } n _ { a b } ^ { p } - \frac 1 3 \delta ^ { k ) p } ) .
$$

We also transform from the center of mass to the representative world line $ { \widetilde { x } } _ { a } ^ { j }$ using Eq. (6.110) in both the acceleration $d a _ { a } ^ { j } / d t$ and the Newtonian term $\sum _ { b } m _ { b } x _ { a b } ^ { j } / r _ { a b } ^ { 3 }$ , to obtain the additional spin contributions to the equations of motion (dropping the tildes):

$$
\delta { \pmb a } _ { a } = { \pmb a } _ { a } [ \mathrm { s o } ] + { \pmb a } _ { a } [ \mathrm { s s } ] ,
$$

where SO and SS denote spin-orbit and spin-spin terms, given by

$$
\begin{array} { r l } {  { a _ { d } ^ { j } [ \mathrm { S o l } ] = \frac { 3 } { 2 } \sum _ { b } \frac { m _ { b } } { b _ { d b } ^ { 3 } } \{ \eta _ { a b } ^ { i j k } [ v _ { b } ^ { i j } ( ( 2 \gamma + 1 + \lambda ) \widehat { S } _ { a } ^ { i j } + ( 2 \gamma + 2 ) \widehat { S } _ { b } ^ { i j } )   } } \\ & { -  v _ { b } ^ { i j } ( ( 2 \gamma + 1 + \lambda ) \widehat { S } _ { b } ^ { i j } + ( 2 \gamma + 2 ) \widehat { S } _ { a } ^ { i j } ) ] } \\ & { +  \eta _ { a b } ^ { i j k } ( v _ { a } - v _ { b } ) ^ { i j } ( ( 2 \gamma + 1 - \lambda ) \widehat { S } _ { a } ^ { i j } + ( 2 \gamma + 2 ) \widehat { S } _ { b } ^ { i j } )  } \\ & { +  \frac { 1 } { 2 } \mathrm { c } _ { 1 } n _ { a b } ^ { i j k } [ ( w + v _ { a } ) ^ { p } \widehat { S } _ { b } ^ { i j } - ( w + v _ { b } ) ^ { p } \widehat { S } _ { a } ^ { i j } ] } \\ & { +  \frac { 1 } { 2 } \mathrm { c } _ { 1 } n _ { a b } ^ { i j k } ( v _ { a } - v _ { b } ) ^ { p } \widehat { S } _ { b } ^ { i k } - \omega _ { a } n _ { a b } ^ { i j } ( w + v _ { b } ) ^ { p } \widehat { S } _ { b } ^ { i k } \} , } \\ & {  a _ { d } ^ { j } [ \mathrm { S s } ] = - \frac { 1 } { 8 } ( 4 \gamma + 4 + \alpha _ { 1 } ) \sum _ { b \in \omega } \frac { m _ { b } } { r _ { a } } \widehat { S } _ { b } ^ { i j } \frac { \partial } { \partial s _ { b } ^ { i j } } n _ { a b } ^ { i j k } ) , } \end{array}
$$

where ˆS jka ≡ S jka /ma and where n 
jkab and n 
jpqab denote the symmetric tracefree combinations

$$
\begin{array} { l } {{ { n _ { a b } ^ { \langle j k \rangle } } \equiv n _ { a b } ^ { j } n _ { a b } ^ { k } - \displaystyle \frac { 1 } { 3 } \delta ^ { j k } , } } \\ { { { \cal n } _ { a b } ^ { \langle j p q \rangle } \equiv n _ { a b } ^ { j } n _ { a b } ^ { p } n _ { a b } ^ { q } - \displaystyle \frac { 1 } { 5 } \left( n _ { a b } ^ { j } \delta ^ { p q } + n _ { a b } ^ { p } \delta ^ { j q } + n _ { a b } ^ { q } \delta ^ { j p } \right) . } } \end{array}
$$

It is useful to note that, when $\lambda = 1$ , corresponding to the covariant spin condition, all reference to the velocity of the PPN coordinate system disappears. All terms depend on relative positions $x _ { a b }$ , and on either relative velocities $\nu _ { a } - \nu _ { b }$ or the velocity of a given body relative to the universe rest frame, $w + \nu _ { a }$ or $w + \nu _ { b }$ .

To obtain the equations of motion for the spin vector, we simply insert the PPN equations of hydrodynamics into the expression

$$
\frac { d S _ { a } ^ { j } } { d t } = \frac 1 2 \epsilon ^ { j p q } \frac { d S _ { a } ^ { p q } } { d t } = \epsilon ^ { j p q } \int _ { a } \rho ^ { * } \bar { x } ^ { p } \frac { d \bar { \nu } ^ { q } } { d t } d ^ { 3 } x .
$$

We again expand the potentials keeping only terms linear in the variable $\bar { x } ^ { j }$ . We absorb back into the definition of $S _ { a } ^ { j }$ a set of PN terms that involve only the internal variables of body $a$ and that can be expressed as a total time derivative. Finally, we define a PN-corrected spin called the “proper” spin, $\bar { \pmb S } _ { a }$ according to

$$
\bar { \bf S } _ { a } \equiv { \bf S } _ { a } + \biggl [ \nu _ { a } ^ { 2 } + ( 2 \gamma + 1 ) \sum _ { b } \frac { m _ { b } } { r _ { a b } } \biggr ] { \bf S } _ { a } - \frac { 1 } { 2 } ( { \bf \nu } _ { { a } } \cdot { \bf S } _ { a } ) { \bf \nu } _ { { { a } } } .
$$

This turns out to be the spin as measured in a quasi-Lorentz frame momentarily comoving with body $a$ (see PW, section 9.5.7). The result is a spin evolution equation given by

$$
\frac { d \bar { \bar { \bf S } } _ { a } } { d t } = \left( \frac { d \bar { \bf S } _ { a } } { d t } \right) _ { \mathrm { s e l f } } + \left( \frac { d \bar { \bf S } _ { a } } { d t } \right) _ { \Omega _ { a } } + \left( \frac { d \bar { \bf S } _ { a } } { d t } \right) _ { \mathrm { p r e c } } ,
$$

where the first two terms depend on the internal structure of the body:

$$
\begin{array} { l } { { \displaystyle \left( \frac { d S _ { a } ^ { j } } { d t } \right) _ { \mathrm { s e l f } } = \epsilon ^ { j p q } \int _ { a } \rho ^ { \ast } \bar { x } ^ { p } \biggl [ \frac { 1 } { 2 } ( \alpha _ { 3 } + \zeta _ { 1 } ) \bar { \Phi } _ { 1 , q } + \zeta _ { 2 } \bar { \Phi } _ { 2 , q } + \zeta _ { 3 } \bar { \Phi } _ { 3 , q } } } \\ { { { } } } \\ { { { } + 3 \zeta _ { 4 } \bar { \Phi } _ { 4 , q } - \displaystyle \frac { 1 } { 2 } \zeta _ { 1 } \left( \bar { \Phi } _ { 6 , q } + \bar { X } _ { , 0 0 \ell } \right) \biggr ] d ^ { 3 } x , } } \\ { { { } } } \\ { { \displaystyle \left( \frac { d S _ { a } ^ { j } } { d t } \right) _ { \Omega _ { a } } = \epsilon ^ { j p q } \Omega _ { a } ^ { p n } \biggl [ \alpha _ { 2 } ( w + \nu _ { a } ) ^ { q } ( w + \nu _ { a } ) ^ { n } - 2 \xi \sum _ { b } \frac { m _ { b } } { r _ { a b } } n _ { a b } ^ { q } n _ { a b } ^ { n } \biggr ] , } } \end{array}
$$

where the barred potentials are generated only by internal variables of the body. The “self” terms are present only in non-conservative theories. For a body that is spherically symmetric to a good approximation, the integrals will all be proportional to $\delta ^ { p q }$ , which is killed by the contraction with $\epsilon ^ { j p q }$ . For a stationary axisymmetric body, the only quantities available to construct a two-index tensor are $\delta ^ { p q }$ and $e ^ { p } e ^ { q }$ , where $e$ is a unit vector in the direction of the symmetry axis, and these also are killed by a contraction with $\epsilon ^ { j p q }$ . The strange nonconservative precessions are therefore relevant only for rather oddly shaped bodies. The $\Omega _ { a }$ term depends on the velocity of body $a$ relative to the preferred frame, and on the distribution of distant matter via the Whitehead potential. For a spherically symmetric body, both terms are killed by the contraction with $\epsilon ^ { j p q }$ . In addition, for laboratory-sized spinning bodies, such as the gyroscopes of Gravity Probe B, these terms are utterly negligible.

The final term in Eq. (6.117) is the PPN equation of spin precession,

$$
\left( \frac { d \bar { \bf S } _ { a } } { d t } \right) _ { \mathrm { p r e c } } = \Omega _ { a } \times \bar { \bf S } _ { a } ,
$$

where $\Omega _ { a }$ contains spin-orbit, spin-spin and preferred-frame contributions, given by

$$
\Omega _ { a } = \Omega _ { a } [ \mathrm { s o } ] + \Omega _ { a } [ \mathrm { s s } ] + \Omega _ { a } [ \mathrm { P F } ] ,
$$

where

$$
\begin{array} { l } { { \Omega _ { a } [ \mathrm { s o } ] = \displaystyle \frac 1 2 \sum _ { b } \frac { m _ { b } } { r _ { a b } ^ { 2 } } n _ { a b } \times \left[ ( 2 \gamma + 1 ) \nu _ { a } - ( 2 \gamma + 2 ) \nu _ { b } \right] , } } \\ { { \Omega _ { a } [ \mathrm { s s } ] = \displaystyle \frac 1 8 ( 4 \gamma + 4 + \alpha _ { 1 } ) \sum _ { b } \frac { 1 } { r _ { a b } ^ { 3 } } \big [ 3 n _ { a b } ( n _ { a b } \cdot \bar { S } _ { b } ) - \bar { S } _ { b } \big ] , } } \\ { { \Omega _ { a } [ \mathrm { P F } ] = - \displaystyle \frac 1 4 \alpha _ { 1 } \sum _ { b } \frac { m _ { b } } { r _ { a b } ^ { 2 } } n _ { a b } \times ( { \pmb w } + { \pmb \nu } _ { b } ) . } } \end{array}
$$

The use of the proper spin ensures that this is a pure precession, in other words, the magnitude of the spin does not change as a result of its interaction with the other bodies in the system. The equations for spin evolution are independent of the parameter $\lambda$ .

It is useful to note that $\Omega _ { a }$ can be expressed in the alternative form

$$
\Omega _ { a } = \frac { 1 } { 2 } ( 2 \gamma + 1 ) \pmb { \nu } _ { a } \times \pmb { \nabla } U - \frac { 1 } { 2 } \pmb { \nabla } \times \pmb { g } ,
$$

where $\begin{array} { r } { U = \sum _ { b } ( m _ { b } / r _ { a b } ) } \end{array}$ and $g ^ { j } = g _ { 0 j }$ , where $g _ { 0 j }$ may be read off from the PPN metric in $\mathrm { B o x } 4 . 1$ , noting that, for a system of spinning bodies, the vector potential $V _ { j }$ has the form

$$
V = \sum _ { b } \left[ \frac { m _ { b } \pmb { v _ { b } } } { r _ { a b } } - \frac { 1 } { 2 } \frac { { \pmb { n _ { a b } } \times \pmb { S _ { b } } } } { r _ { a b } ^ { 2 } } + O ( R _ { b } ^ { 2 } / r _ { a b } ^ { 3 } ) \right] .
$$

Equation (6.119) gives the precession of the proper spin relative to the PPN coordinate frame, whose axes are non-rotating relative to distant matter. We will discuss the observable consequences of this precession in Chapter 9.

With the PPN formalism and its associated equations of motion in hand, we are now ready to confront the gravitation theories discussed in Chapter 5 with the results of experiments. In this chapter, we focus on the three “classical” tests of relativistic gravity, consisting of (i) the deflection of light, (ii) the time delay of light, and (iii) the perihelion advance of Mercury.

This usage of the term “classical” is a break with tradition. Traditionally, the term “classical tests” referred to the gravitational redshift experiment, the deflection of light, and the perihelion advance of Mercury. The reason is largely historical. These were the first observable effects of general relativity to be computed by Einstein, and he regarded these three as crucial tests of his theory. However, in Chapter 2 we saw that the gravitational redshift experiment is really not a test of general relativity, rather it is a test of the Einstein Equivalence Principle, upon which general relativity and every other metric theory of gravity are founded. Put differently, every metric theory of gravity automatically predicts the same redshift. For this reason, the the redshift effect has been dropped as a ”classical” test (that is not to deny its importance, of course, as our discussion in Chapter 2 points out).

We can immediately replace it with an experiment that is as important as the other two, the Shapiro time delay of light. This effect is closely related to the deflection of light, as one might expect, since any physical mechanism in Maxwell’s equations (refraction, dispersion, gravity) that bends light can also be expected to delay it. In fact, it is a mystery why Einstein did not discover this effect. It was discovered as a prediction of Einstein’s theory in l964, by radio astronomer Irwin Shapiro. The simplest explanation seems to be that Shapiro had the benefit of knowing that the space technology of the 1960s and 1970s would make feasible a measurement of a delay of the expected size $2 0 0 ~ \mu \mathrm { s }$ for a round trip signal to Mars). No such technology was known to Einstein. He was aware only of the known problem of Mercury’s excess perihelion advance of 43 arcseconds per century, and of the potential ability to measure the deflection of starlight. But the lack of available technology may not be the whole story. After all, Einstein derived the gravitational redshift at a time when the hopes of measuring it were marginal at best (a reliable measurement was not performed until 1960), and other workers such as Lense and Thirring and de Sitter derived effects of general relativity, with little or no hope of seeing them measured using the technology of the day. Why then, did no one at the time take the step from deflection to time delay, if only as a matter of principle?

Nevertheless, despite its late arrival, the time delay deserves a place in the triumvirate of “classical” tests, not the least because it has given one of the most precise tests of general relativity to date!

We begin this chapter with measurements of the deflection of light, Section 7.1, then turn to the Shapiro time delay, Section 7.2, and in Section 7.3, we discuss the perihelion advance of Mercury.

# 7.1 Deflection of Light

Eq. (6.21) indicates that the path of a light ray is deflected by a distribution of mass, but it does not tells us how to measure the effect. We can measure the direction of an incoming photon from some source, but we have no information about the initial direction. In order to make this a testable effect we must use only quantities that can be observed directly. The key quantity is the angle between two sources. Then, if we can measure that angle at a time when the mass distribution is sufficiently far from the sources as seen on the sky that we can ignore any deflection, and then measure the angle when the mass is close by, we can measure the differential deflection.

We can give this angle a coordinate-invariant expression. Consider an observer at rest in the PPN coordinate system, with four velocity $u ^ { \mu }$ , who receives a signal from a target source and a reference source, whose trajectories are $x ^ { \mu } ( t )$ and $x _ { r } ^ { \mu } ( t )$ , respectively. The spatial directions of the incoming signals are given by projecting the tangent four-vectors $\nu ^ { \mu } \equiv$ $d x ^ { \mu } / d t$ and $\nu _ { r } ^ { \mu } \equiv d x _ { r } ^ { \mu } / d t$ of the rays onto the hypersurface orthogonal to the observer’s four-velocity, using the projection operator $P _ { \mu } ^ { \nu } = \delta _ { \mu } ^ { \nu } + u ^ { \nu } u _ { \mu } .$ The inner product between the resulting vectors is related to the cosine of the angle $\theta$ between the incoming directions by

$$
\cos \theta \equiv \frac { \nu ^ { \lambda } P _ { \lambda } ^ { \mu } \nu _ { r } ^ { \nu } P _ { \nu \mu } } { | \nu ^ { \lambda } P _ { \lambda } ^ { \mu } | | \nu _ { r } ^ { \nu } P _ { \nu \mu } | } = 1 + \frac { \nu \cdot \nu _ { r } } { ( \nu \cdot u ) ( \nu _ { r } \cdot u ) } .
$$

If we ignore the velocity of the observer, which only produces effects such as aberration, which can be readily accounted for if necessary, then Eq. (7.1) simplifies to

$$
\cos \theta = 1 - ( g _ { 0 0 } ) ^ { - 1 } g _ { \mu \nu } \nu ^ { \mu } \nu _ { r } ^ { \nu } .
$$

By substituting Eq. (6.17) into Eq. (7.2), we obtain, to post-Newtonian accuracy,

$$
\cos \theta = \boldsymbol { k } \cdot \boldsymbol { k } _ { r } + \boldsymbol { k } \cdot \boldsymbol { \alpha } _ { r } + \boldsymbol { k } _ { r } \cdot \boldsymbol { \alpha } .
$$

We now consider the simple case where the source is a spherical body at the origin of the PPN coordinate system. Assuming that the ray is always outside the body, then in Eq. (6.13), $U _ { , k } = - m x ^ { k } ( t ) / r ( t ) ^ { 3 }$ , and Eq. (6.15) becomes $d { \pmb { \alpha } } / d t = - ( 1 + \gamma ) m { \pmb { b } } / r ( t ) ^ { 3 }$ , where now $\pmb { b } \equiv \pmb { x } _ { e } - ( \pmb { x } _ { e } \cdot \pmb { k } ) \pmb { k } .$ . Employing the identity (6.18b) with $s = x ( t )$ and integrating with respect to $t$ , we obtain

$$
\pmb { \alpha } ( t ) = - ( 1 + \gamma ) m \frac { \pmb { b } } { b ^ { 2 } } \bigg ( \frac { \pmb { x } \cdot \pmb { k } } { r } - \frac { \pmb { x } _ { e } \cdot \pmb { k } } { r _ { e } } \bigg ) .
$$

Substituting Eq. (7.4) into Eq. (7.3) we obtain, to post-Newtonian order,

$$
\begin{array} { c } { \cos \theta = k \cdot k _ { r } - ( 1 + \gamma ) m \left\{ \displaystyle \frac { b \cdot k _ { r } } { b ^ { 2 } } \left( \displaystyle \frac { { \boldsymbol { x } } _ { O } \cdot { \boldsymbol { k } } } { r _ { O } } - \displaystyle \frac { { \boldsymbol { x } } _ { e } \cdot { \boldsymbol { k } } } { r _ { e } } \right) \right. } \\ { \displaystyle \left. + \frac { b _ { r } \cdot k } { b _ { r } ^ { 2 } } \left( \displaystyle \frac { { \boldsymbol { x } } _ { O } \cdot k _ { r } } { r _ { O } } - \displaystyle \frac { { \boldsymbol { x } } _ { r } \cdot k _ { r } } { r _ { r } } \right) \right\} , } \end{array}
$$

where $x _ { O }$ is the location of the observer, and the subscript $r$ denotes the reference source. It is useful to note, to the post-Newtonian accuracy needed in Eq. (7.5), that

$$
\pmb { b } = \pmb { x } _ { O } - ( \pmb { x } _ { O } \cdot \pmb { k } ) \pmb { k } , \quad \pmb { b } _ { r } = \pmb { x } _ { O } - ( \pmb { x } _ { O } \cdot \pmb { k } _ { r } ) \pmb { k } _ { r } .
$$

We now define the angle $\theta _ { 0 }$ to be the angle between the unperturbed paths of the photons from the source and from the reference source, i.e.,

$$
\cos \theta _ { 0 } \equiv \pmb { k } \cdot \pmb { k } _ { r } ,
$$

and we define the “deflection” of the measured angle from the unperturbed angle to be

$$
\delta \theta \equiv \theta - \theta _ { 0 } .
$$

There are two interesting cases to consider. This first is an idealized situation that leads to a simple formula. We suppose that the Sun itself is both the massive source and the reference source. Then the second term inside the braces never appears (since $\pmb { b } = 0 \ \boldsymbol { a }$ priori), $b \cdot k _ { r } / b = \sin \theta _ { 0 }$ , and

$$
\delta \theta = \left( \frac { 1 + \gamma } { 2 } \right) \frac { 2 m } { b } \left( \frac { \pmb { x } _ { \oplus } \cdot \pmb { k } } { r _ { \oplus } } - \frac { \pmb { x } _ { e } \cdot \pmb { k } } { r _ { e } } \right) .
$$

For a photon emitted from a distant star or galaxy, $r _ { e } \gg r _ { \oplus } , \pmb { x } _ { e } { \cdot } \pmb { k } / r _ { e } \simeq - 1$ , and ${ \pmb x } _ { \oplus } { \pmb \cdot } { \pmb k } / r _ { \oplus } \simeq$ cos $\theta _ { 0 }$ , and we obtain (Shapiro 1967; Ward 1970),

$$
\delta \theta = \left( \frac { 1 + \gamma } { 2 } \right) \frac { 4 m } { b } \left( \frac { 1 + \cos \theta _ { 0 } } { 2 } \right) .
$$

The deflection is a maximum for a ray which just grazes the Sun. For $\theta _ { 0 } \simeq 0$ , $b \simeq R _ { \odot } \simeq$ $6 . 9 6 \times 1 0 ^ { 5 } \mathrm { k m }$ , $m = m _ { \odot } = 1 . 4 7 6 \mathrm { k m }$ , we obtain

$$
\delta \theta _ { \mathrm { m a x } } = 1 . 7 5 0 4 \left( \frac { 1 + \gamma } { 2 } \right) \mathrm { a r c s e c } .
$$

For rays coming from arbitrary directions, we use the fact that $b \simeq r _ { \oplus } \sin \theta _ { 0 }$ to express the deflection in the form

$$
\begin{array} { r } { \delta \theta = \left( \frac { 1 + \gamma } { 2 } \right) \frac { 2 m } { r _ { \oplus } } \left( \frac { 1 + \cos \theta _ { 0 } } { \sin \theta _ { 0 } } \right) } \\ { = 4 . 0 7 2 \left( \frac { 1 + \gamma } { 2 } \right) \cot \frac { \theta _ { 0 } } { 2 } \operatorname* { m a s } . } \end{array}
$$

At $9 0 ^ { \circ }$ from the direction of the Sun, the deflection is about 4 mas.

The second case to consider is more closely related to the actual method of measuring the deflection of light using the techniques of radio or optical interferometry. In these techniques, one chooses a reference source near the observed source and monitors changes $\delta \theta$ in their angular separation. If we define $\Phi$ and $\Phi _ { r }$ to be the angular separation between the Earth-Sun direction and the unperturbed direction of photons from the two sources, as in Figure 7.1, then

$$
\cos \Phi = \frac { { \bf x } _ { \oplus } \cdot \pmb { k } } { r _ { \oplus } } \quad \cos \Phi _ { r } = \frac { { \bf x } _ { \oplus } \cdot \pmb { k } _ { r } } { r _ { \oplus } } .
$$

![](images/ddd0a38a374a61699d4f3a8c73d15f6093ddf02f7260550bf3fb6a1e17102862.jpg)  
Fig. 7.1 Geometry of light deflection measurements.

Assuming again that the two sources are very distant and using the fact that $b = r _ { \oplus } \sin \Phi$ and $b _ { r } = r _ { \oplus } \sin \Phi _ { r }$ , we obtain an expression purely in terms of measured angles on the sky:

$$
\delta \theta = \left( \frac { 1 + \gamma } { 2 } \right) \frac { 2 m } { r _ { \oplus } } \left[ \frac { \cos \Phi _ { r } - \cos \Phi \cos \theta _ { 0 } } { ( 1 - \cos \Phi ) \sin \theta _ { 0 } } + \frac { \cos \Phi - \cos \Phi _ { r } \cos \theta _ { 0 } } { ( 1 - \cos \Phi _ { r } ) \sin \theta _ { 0 } } \right] .
$$

Note that the angle $\theta _ { 0 }$ is related to the angle $\chi$ between the Sun-source and Sun-reference directions projected on the plane of the sky (Figure 7.1) by the formula from spherical geometry

$$
\cos \theta _ { 0 } = \cos \Phi _ { r } \cos \Phi + \sin \Phi _ { r } \sin \Phi \cos \chi .
$$

If the observed source direction passes very near the Sun, while the reference source remains a decent angular distance away, we can approximate $\Phi \ll \Phi _ { r }$ , and thus

$$
\theta _ { 0 } \simeq \Phi _ { r } - \Phi \cos \chi + \frac { \cos \Phi _ { r } \sin ^ { 2 } \chi } { 2 \sin \Phi _ { 2 } } \Phi ^ { 2 } + O ( \Phi ^ { 3 } ) .
$$

The resulting deflection is

$$
\delta \theta = \left( \frac { 1 + \gamma } { 2 } \right) \frac { 4 m } { b } \biggl [ - \cos \chi + \frac { 1 + \left( 1 + 2 \sin ^ { 2 } \chi \right) \cos \theta _ { 0 } } { 2 \sin \theta _ { 0 } } \Phi + O ( \Phi ^ { 2 } ) \biggr ] .
$$

This result shows quite clearly how the relative angular separation between two distant sources may vary as the lines of sight of one of them passes near the Sun $( b \sim R _ { \odot } , \chi$ varying).

# 7.1.1 Tests of the deflection of light

The first successful measurement of the bending of light by the Sun was carried out by Eddington and his colleagues during the total solar eclipse of May 29, 1919. The principle

# Box 7.1

Why 1 (1 + γ)? The deflection of light can be viewed as arising from two effects. The first, corresponding to the $" 1 / 2 "$ part of the coefficient, is commonly called the “Newtonian” deflection. One way to derive this is to assume that light behaves as a particle, to recall that the trajectory of a particle is independent of its mass (Weak Equivalence Principle), and to calculate the deflection of its trajectory in the limit in which the particle’s speed approaches the speed of light. Such an approach would have made sense in Newton’s day, when light was really viewed as a “corpuscle,”and, indeed, Newton himself speculated on the possible effect of gravity on light. The English physicist Henry Cavendish may have been the first person to calculate the bending explicitly, possibly as early as 1784, although evidence for this was not discovered until around 1914, during an effort to compile and publish his entire body of work – publication having never been high on Cavendish’s list of priorities. In fact, all that was found was a scrap of paper in Cavendish’s handwriting stating that he had done the calculation, and giving the answer. Independently of Cavendish, the Bavarian astronomer Johann von Soldner did publish in 1803 a detailed calculation of the Newtonian bending in a German astronomical journal. Strangely, von Soldner’s calculation was largely forgotten until it was resurrected in 1921 by Phillip Lenard as part of a campaign to discredit the “Jewish” relativity of Einstein by publicizing the earlier work of the “Aryan” von Soldner. Apparently, Lenard was not deterred by the fact that the 1919 measurements by Eddington actually favored general relativity over the Newtonian deflection.

Unaware of the earlier work, Einstein himself derived the “Newtonian” deflection in 1911. He argued that the principle of equivalence requires the replacement of the Minkowski metric of flat spacetime by the metric

$$
d s ^ { 2 } = - ( 1 - 2 U ) d t ^ { 2 } + d x ^ { 2 } + d y ^ { 2 } + d z ^ { 2 } .
$$

Geodesic motion for a test particle in this spacetime reproduces Newtonian gravity, and geodesic motion for a photon gives the Newtonian deflection. Another derivation using only the equivalence principle imagines a sequence of freely falling frames through which a light ray passes as it travels near a gravitating body. Each frame is momentarily at rest at the moment the light ray enters it. Although the path of the ray is a straight line within each frame, the frame picks up a downward velocity during the ray’s traversal, because of the body’s gravitational attraction. When the adjacent, momentarily stationary frame receives the light ray, the ray is deflected toward the body because the downward motion of the previous frame induces aberration on the received ray. By adding up all the tiny aberrations over a sequence of frames, one arrives at the Newtonian deflection.

But a relativistic metric theory of gravity introduces an additional effect, because the spatial part of the metric now comes with the multiplying factor $( 1 + 2 \gamma U )$ . This represents spatial curvature, which could not be taken into account either by Newtonian gravity or by the principle of equivalence. So the total deflection can be viewed as a sum of a Newtonian deflection relative to locally straight lines, plus the bending of locally straight lines relative to straight lines at infinity. Thus in the coefficient $( 1 + \gamma ) / 2 ,$ the $" 1 / 2 "$ holds in any metric theory, while the $" \gamma / 2 "$ varies from theory to theory.

of the experiment was to make differential measurements. Photographs of the stars near the Sun taken during the eclipse were to be compared with photographs of the same stars taken at night some months earlier or later, and the displacement of each star compared to the reference photograph was to be carefully measured. But on the day of the eclipse at Eddington’s site, a rainstorm started, and as the morning wore on, he began to lose all hope. But at the last moment, the weather began to change for the better, and when the partial eclipse was well advanced, the astronomers began to get a glimpse of the Sun. Of the sixteen photographs taken through the remaining cloud cover, only two had reliable images, totaling only about five stars. Nevertheless, comparison of the two eclipse plates with a comparison plate taken at the Oxford University telescope before the expedition yielded results in agreement with general relativity, corresponding to a deflection at the limb of the Sun (grazing ray) of $1 . 6 0 \pm 0 . 3 1$ arcseconds, corresponding to $0 . 9 1 \pm 0 . 1 8$ for $( 1 + \gamma ) / 2$ . The Sobral expedition, blessed with better weather, managed to obtain eight usable plates showing at least seven stars each. The nineteen plates taken on a second telescope were deemed worthless because the telescope apparently changed its focal length just before totality of the eclipse, possibly as a result of heating by the Sun. Analysis of the good plates yielded a grazing deflection of $1 . 9 8 \pm 0 . 1 2$ arcseconds, or $1 . 1 3 \pm 0 . 0 7$ for $( 1 + \gamma ) / 2$ (Dyson et al., 1920). These results are indicated by the point and the arrow (off the chart) to the far left of Figure 7.2. Eddington’s announcement in November 1919 that

# Fig. 7.2

![](images/5a5907c2104e0a4598b030c649cfadffb0ef9033c6f25ac76a70cbfea340bd8c.jpg)  
Measurements of the coefficient $( 1 + \gamma ) / 2$ from light deflection and time delay measurements. Its GR value is unity. The arrows at the top denote anomalously large values from early eclipse expeditions. The Shapiro time-delay measurements using the Cassini spacecraft yielded an agreement with GR to $1 0 ^ { - 3 }$ percent, and VLBI light deflection measurements have reached 0.01 percent. Hipparcos denotes the optical astrometry satellite, which reached 0.2 percent.

the bending measurements were in agreement with general relativity helped make Einstein an international celebrity.

Questions were raised, however, about the results of Eddington’s measurements. Given the poor quality of the data, did they really support Einstein or not? Was it proper for Eddington to discard the data from the second telescope at the Sobral site? More recently, some (Earman and Glymour, 1980) have wondered whether Eddington’s enthusiasm for the theory of general relativity caused him to select or massage the data to get the desired result. Numerous reanalyses between 1923 and 1956 of the plates used by Eddington yielded the same results within 10 percent. In 1979, on the occasion of the centenary of Einstein’s birth, astronomers at the Royal Greenwich Observatory reanalysed both sets of Sobral plates using a modern tool called the Zeiss Ascorecord and its data reduction software (Harvey, 1979). The plates from the first telescope yielded virtually the same deflection as that obtained by Eddington’s team with the errors reduced by 40 percent. Despite the scale changes in the second set of Sobral plates, the analysis still gave a result $1 . 5 5 \pm 0 . 3 4$ arcseconds at the limb, consistent with general relativity, albeit with much larger errors. Looking back on Eddington’s treatment of the data, Kennefick (2009) has argued that there is no credible evidence of bias on his part.

The publicity surrounding Eddington’s famous announcement has left the impression that his was the only test of the deflection using eclipse measurements, successful or otherwise. But the history is much richer (Crelinsten, 2006). William Campbell and Heber Curtis of the Lick Observatory analyzed plates from a 1900 eclipse in Georgia and a 1918 eclipse in Washington state in the United States and found no deflection; ironically they reported this negative result at the Royal Society of London meeting in July 1919 in the midst of Eddington’s data analysis (at the meeting, rumors were already going around that Eddington would report a positive result). Following up on Eddington’s success, seven teams tried the measurement during a 1922 eclipse in Australia, although only three succeeded. Campbell and Robert Trumpler of the Lick team reported a result for the deflection at the limb of $1 . 7 2 \pm 0 . 1 1$ arcseconds, while a Canadian team and an England/Australian team reported values between 1.2 and 2.3 arcseconds. Later eclipse measurements continued to give mild support to general relativity: one in 1929, two in 1936, one each in 1947 and 1952, and one in 1973 (light grey points and arrows in Figure 7.2). Surprisingly, there was very little improvement in accuracy, with different measurements giving values anywhere between three-quarters and one and one-third times the general relativistic prediction. On the other hand, there was little doubt that the Newtonian deflection was wrong [for reviews, see von Kl¨uber (1960) and Bertotti et al. (1962)].

The 1973 expedition is a case in point. Organized by the University of Texas and Princeton University, the observation took place in June at Chinguetti Oasis in Mauritania.1 The observers had the benefit of 1970s technology: modern photographic emulsions, a temperature-controlled telescope shed, sophisticated motor drives to control the direction of the telescope accurately, and computerized analysis of the photographs. Unfortunately, they couldn’t control the weather any better than Eddington. Eclipse morning brought high winds, drifting sand, and dust too thick to see the Sun. But as totality of the eclipse approached, the winds died down, the dust began to settle, and the astronomers took a sequence of photographs during what they have described as the shortest six minutes of their lives. They had hoped to gather over 1000 star images, but the dust cut the visibility to less than 20 percent and only a disappointing 150 were obtained. After a follow-up expedition to the site in November to take comparison plates, the photographs were analyzed using the GALAXY Measuring Engine at the Greenwich Observatory, with a result $0 . 9 5 \pm 0 . 1 1$ times the general relativity prediction, essentially no improvement in accuracy over previous eclipse measurements (Brune et al., 1976; Jones, 1976).

During the 2017 solar eclipse that passed over the United States, a number of amateur and professional astronomers endeavored to improve upon these results by exploiting new technologies such as CCD cameras, together with precise reference locations of stars provided by space astrometry telescopes, such as GAIA. Bruns (2018) achieved a three percent result in agreement with general relativity.

The development of radio interferometry, and later of very-long-baseline radio interferometry (VLBI), produced greatly improved determinations of the deflection of light. These techniques now have the capability of measuring angular separations and changes in angles to accuracies better than 100 microarcseconds. Early measurements took advantage of the fact that groups of strong quasars annually pass very close to the Sun (as seen from the Earth), such as the group 3C273, 3C279 and 3C48. As the Earth moves in its orbit, changing the lines of sight of the quasars relative to the Sun, the angular separation between pairs of quasars varies according to Eq. (7.17). A number of measurements of this kind over the period 1969 – 1975 yielded determinations of the coefficient $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ , or equivalently of $\gamma - 1$ , reaching levels of a percent. A 1995 VLBI measurement using 3C273 and 3C279 yielded $\gamma - 1 = ( - 8 \pm 3 4 ) \times 1 0 ^ { - 4 }$ (Lebach et al., 1995), while a 2009 measurement using the VLBA targeting the same two quasars plus two other nearby radio sources yielded $\gamma - 1 = ( - 2 \pm 3 ) \times 1 0 ^ { - 4 }$ (Fomalont et al., 2009).

In recent years, transcontinental and intercontinental VLBI observations of quasars and radio galaxies have been made partly to monitor the Earth’s rotation and partly to establish a “reference frame” for precision astrometry (“VLBI” in Figure 7.2). These measurements are sensitive to the milliarcsecond level deflections of light over almost the entire celestial sphere. A 2004 analysis of almost 2 million VLBI observations of 541 radio sources, made by 87 VLBI sites yielded $\gamma - 1 = ( - 1 . 7 \pm 4 . 5 ) \times 1 0 ^ { - 4 }$ (Shapiro et al., 2004). Analyses that incorporated data through 2010 yielded $\gamma - 1 = ( - 0 . 8 \pm 1 . 2 ) \times 1 0 ^ { - 4 }$ (Lambert and Le Poncin-Lafitte, 2009, 2011).

To reach high precision at optical wavelengths requires observations from space. The Hipparcos optical astrometry satellite making global measurements of the deflection yielded a result for $( 1 + \gamma ) / 2$ at the level of 0.2 percent (Froeschle et al., 1997). ´ GAIA, a high-precision astrometric orbiting telescope launched by ESA in 2013 (Gaia Collaboration et al., 2016) possesses astrometric capability ranging from 10 to a few hundred microarcseconds, plus the ability to measure the locations of a billion stars down to the 20th magnitude; it could eventually measure the light-deflection and $\gamma$ to the $1 0 ^ { - 6 }$ level (Mignard and Klioner, 2010).

# 7.1.2 Gravitational lenses

In 1979, astronomers Dennis Walsh, Robert Carswell, and Ray Weymann discovered the “double quasar” $Q 0 9 5 7 + 5 6 1$ , which consisted of two quasar images about 6 arcseconds apart, with almost the same redshift $( z ~ = ~ 1 . 4 1$ ) and very similar spectra (Walsh et al., 1979). It was immediately realized that there was just one quasar, but that intervening matter in the form of a galaxy or a cluster of galaxies was bending the light from the quasar and producing two separate images.

Since then, the “gravitational lens” has become an important tool for astronomers. The phenomenon has been exploited to map the distribution of mass around galaxies and clusters, and to search for dark matter, dark energy, compact objects, and extrasolar planets. Many subtopics of gravitational lensing have been developed to cover different astronomical realms: microlensing for the search for dim compact objects and extrasolar planets, the use of luminous arcs to map the distribution of mass and dark matter, and weak lensing to measure the properties of dark energy. Lensing has to be taken into account in interpreting certain aspects of the cosmic microwave background radiation, and in extracting information from gravitational waves emitted by sources at cosmological distances.

Gravitational lensing has also yielded a remarkable measurement of $( 1 + \gamma ) / 2$ on galactic scales (Bolton et al., 2006). It used data on gravitational lensing by 15 elliptical galaxies, collected by the Sloan Digital Sky Survey. The mass distribution of each lensing galaxy (including the contribution from dark matter) was derived from the observed velocity dispersion of stars within the galaxy. Comparing the observed lensing with the lensing predicted by the deflection formula (6.20) provided a five percent bound on $( 1 + \gamma ) / 2$ , in agreement with general relativity. Although the accuracy was only comparable to that of Eddington’s 1919 measurements, this test of Einstein’s light deflection was obtained on a galactic, rather than a solar-system scale.

# 7.2 The Shapiro Time Delay

Eqs. (6.17) or (6.21) reveal that, in addition to being deflected in the gravitational field of a massive body, a photon is also retarded in its motion. Its coordinate speed is less than unity (nevertheless, the speed measured by a local freely falling observer as the photon passes her is always unity). We consider the simple case of a light ray passing by a spherical body of mass $m$ . Solving Eq. (6.21) for $t - t _ { e }$ , and recalling that $\pmb { k } \cdot \delta \pmb { x } _ { \bot } = 0$ , we obtain

$$
t - t _ { e } = | \pmb { x } ( t ) - \pmb { x } _ { e } | + ( 1 + \gamma ) m \ln \biggl [ \frac { ( r ( t ) + \pmb { x } ( t ) \cdot \pmb { k } ) ( r _ { e } - \pmb { x } _ { e } \cdot \pmb { k } ) } { b ^ { 2 } } \biggr ] ,
$$

where $\pmb { b } \equiv \pmb { x } _ { e } - ( \pmb { x } _ { e } \cdot \pmb { k } ) \pmb { k }$ . For a signal emitted from the Earth, received at a planet or spacecraft at $\boldsymbol { x } _ { p }$ and returned to Earth, the roundtrip travel time $\Delta t$ is given by

$$
\Delta t = 2 | \pmb { x } _ { \oplus } - \pmb { x } _ { p } | + 2 ( 1 + \gamma ) m \ln \biggl [ \frac { \left( \boldsymbol { r } _ { \oplus } + \pmb { x } _ { \oplus } \cdot \pmb { k } \right) ( \boldsymbol { r } _ { p } - \pmb { x } _ { p } \cdot \pmb { k } ) } { b ^ { 2 } } \biggr ] ,
$$

where $\pmb { k }$ is the direction of the photon on its return flight. Here we have ignored the motion of the Earth during the round trip of the signal. To be completely correct, the round trip travel time should be expressed in terms of the proper time elapsed during the round trip, as measured by an atomic clock on Earth; but this introduces no new effects so we will not do so here (in actual measurements of the delay, these effects are routinely taken into account). The additional delay $\delta t$ produced by the second term in Eq. (7.19) is a maximum when the planet is on the far side of the Sun from the Earth (superior conjunction), that is, when

$$
\begin{array} { r } { { \pmb x } _ { \oplus } \cdot { \pmb k } \simeq r _ { \oplus } , \quad { \pmb x } _ { p } \cdot { \pmb k } \simeq - r _ { p } , \quad { b } \simeq R _ { \odot } , } \end{array}
$$

then

$$
\begin{array} { l } { \displaystyle \delta t = 2 ( 1 + \gamma ) m \ln \left( \frac { 4 r _ { \oplus } r _ { p } } { b ^ { 2 } } \right) } \\ { = \left( \frac { 1 + \gamma } { 2 } \right) \left\{ 2 3 8 . 5 \mu \mathrm { s } - 1 9 . 7 \mu \mathrm { s } \ln \left[ \left( \frac { b } { R _ { \odot } } \right) ^ { 2 } \frac { a } { r _ { p } } \right] \right\} , } \end{array}
$$

where $R _ { \odot }$ is the radius of the Sun, and $a = 1 . 4 9 6 \times 1 0 ^ { 8 } { \mathrm { k m } }$ is the astronomical unit.

Soon after radio astronomer Irwin Shapiro discovered this effect as a theoretical prediction of general relativity, a program of measurements began, using radar ranging to targets passing through superior conjunction. The first of these was carried out by Shapiro’s team (Shapiro et al., 1968, 1971) using radar signals bouncing off the surface of Mercury and Venus. Since one does not have access to a “Newtonian” signal against which to compare the round trip travel time of the observed signal, it is again necessary to do a differential measurement of the variations in round trip travel times as the target passes through superior conjunction, and to look for the characteristic logarithmic behavior of the delay. To achieve this accurately however, one must take into account the variations in $| \pmb { x } _ { \oplus } - \pmb { x } _ { p } |$ due to the orbital motion of the target relative to the Earth. This is done by using radar-ranging (and possibly other) data on the target taken when it is far from superior conjunction (i.e., when the time-delay term is negligible) to determine an accurate orbit for the target, using the orbit to predict the PPN coordinate trajectory $\boldsymbol { x } _ { p }$ near superior conjunction, then combining that information with the trajectory of the Earth $\scriptstyle { \boldsymbol { x } } _ { \oplus }$ to determine all the relevant quantities in Eq. (7.19). The resulting predicted round trip travel times in terms of the unknown coefficient $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ are then fit to the measured travel times using the method of least squares, and an estimate obtained $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ . This is an oversimplification, of course.

The targets employed included planets, such as Mercury or Venus, used as passive reflectors of the radar signals, and artificial satellites, such as Mariners 6 and 7, Voyager 2, the Viking Mars landers and orbiters, and the Cassini spacecraft to Saturn, used as active retransmitters of the radar signals.

The results for the coefficient $\textstyle { \frac { 1 } { 2 } } ( 1 + \gamma )$ of all radar time-delay measurements performed to date are shown in the bottom half of Figure 7.2. The 1976 Viking experiment resulted in a 0.1 percent measurement (Reasenberg et al., 1979).

A significant improvement was reported in 2003 from Doppler tracking of the Cassini spacecraft while it was on its way to Saturn (Bertotti et al., 2003), with a result $\gamma - 1 =$ $( 2 . 1 \pm 2 . 3 ) \times 1 0 ^ { - 5 }$ . This was made possible by the ability to do Doppler measurements using both X-band $( 7 1 7 5 ~ \mathrm { M H z } )$ and Ka-band $( 3 4 3 1 6 ~ \mathrm { M H z } )$ radar, thereby significantly reducing the dispersive effects of the solar corona. Note that with Doppler measurements, one is essentially measuring the time derivative of the Shapiro delay. In addition, the 2002 superior conjunction of Cassini was particularly favorable: with the spacecraft at 8.43 astronomical units from the Sun, the distance of closest approach of the radar signals to the Sun was only $1 . 6 R _ { \odot }$ . For scalar-tensor theories, the Cassini bound places a limit $\omega _ { 0 } ~ > ~ 4 0 , 0 0 0$ or $\alpha _ { 0 } < 3 . 5 \times 1 0 ^ { - 3 }$ . For the case of massive scalar fields, Alsing et al. (2012) displayed the bounds as a function of the mass. Improved measurements of the Shapiro delay, down to the level of parts per million, may be possible using data from the cruise phase of the joint European-Japanese BepiColombo project to place two orbiters around Mercury (Benkhoff et al., 2010), scheduled for launch in late 2018 (Imperi and Iess, 2017).

The Shapiro delay has been measured and plays an important role in analyzing binary pulsar data, most notably from the “double pulsar” J0737-3039 and even, recently, from the original Hulse-Taylor binary pulsar $\mathrm { B } 1 9 1 3 + 1 6$ (see Chapter 12). In combination with the geometric delay caused by light deflection, the Shapiro delay also plays a role in efforts to measure the Hubble constant using time delays between images in gravitational lenses (see Meylan et al. (2006) for recent reviews).

# 7.3 The Perihelion Advance of Mercury

The explanation of the anomalous perihelion shift of Mercury’s orbit was an early triumph of GR. Since Le Verrier’s 1859 announcement of an unexplained advance in the perihelion of Mercury after the perturbing effects of the other planets had been accounted for, no credible explanation had been found, despite numerous attempts. The modern value for this discrepancy is about 43 arcseconds per century (see Table 7.1). General relativity accounted for the anomalous shift in a natural way without disturbing the agreement with other planetary observations.

<table><tr><td>Table7.1 Planetary contributions to Mercury&#x27;s perihelion advance (in arcseconds per century).</td></tr><tr><td>Planet Advance</td></tr><tr><td>Venus 277.8</td></tr><tr><td>Earth 90.0</td></tr><tr><td>Mars 2.5</td></tr><tr><td>Jupiter 153.6</td></tr><tr><td>Saturn 7.3</td></tr><tr><td>Total 531.2</td></tr><tr><td>Observed 574.1</td></tr><tr><td>Discrepancy 42.9</td></tr></table>

In Chapter 6, Eq. (6.78) we obtained the secular changes in the orbit elements of a two-body system in the PPN framework, including the effects of a Newtonian quadrupole moment for one of the bodies (but ignoring preferred-frame or preferred location effects for the moment). Since the orbit of Mercury is inclined by only $7 ^ { \circ }$ relative to the ecliptic plane of the solar system, and since changes in its perihelion are measured relative to the fixed reference system of the ecliptic plane, the relevant observable quantity is $\Delta \boldsymbol { \varpi } = \Delta \boldsymbol { \omega } + \cos \iota \Delta \boldsymbol { \Omega }$ . From Eq. (6.78), with $\iota \simeq 0$ , we obtain

$$
\Delta \varpi = \frac { 6 \pi m } { p } \left[ \frac { 1 } { 3 } \left( 2 + 2 \gamma - \beta \right) + \frac { 1 } { 6 } \eta \left( 2 \alpha _ { 1 } - \alpha _ { 2 } + \alpha _ { 3 } + 2 \zeta _ { 2 } \right) \right] + \frac { 3 \pi } { 2 } J _ { 2 } \left( \frac { R } { p } \right) ^ { 2 } ,
$$

where now J2 and R are the quadrupole moment and radius of the Sun, and m = m + m . We have ignored a small additional quadrupole contribution caused by the fact that the Sun’s rotation axis is inclined relative to the ecliptic by $\theta \sim 7 ^ { \circ }$ ; this adds a correction to the quadrupole term that is too small to be measurable at present.

The first term in Eq. (7.22) is the “classical” perihelion shift, which depends upon the PPN parameters $\gamma$ and $\beta$ . The second term depends upon the dimensionless reduced mass of the two bodies; it is zero in any fully conservative theory of gravity $\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } =$ $\zeta _ { 2 } = 0$ ); it is also negligible for Mercury, since $\eta \simeq m _ { \breve { \updownarrow } } / m _ { \odot } \simeq 2 \times 1 0 ^ { - 7 }$ . We will drop this term henceforth. The third term depends upon the solar quadrupole moment $J _ { 2 }$ . For a Sun that rotates uniformly with its observed surface angular velocity, so that the quadrupole moment is produced by centrifugal flattening, one may estimate $J _ { 2 } \simeq 1 0 ^ { - 7 }$ . This actually agrees reasonably well with values inferred from rotating solar models that are in accord with observations of the normal modes of solar oscillations (helioseismology); the latest inversions of helioseismology data give $J _ { 2 } = ( 2 . 2 \pm 0 . 1 ) \times 1 0 ^ { - 7 }$ (Mecheri et al., 2004; Antia et al., 2008); for a review of measurements of the solar quadrupole moment, see (Rozelot and Damiani, 2011). Substituting standard orbital elements and physical constants for Mercury and the Sun we obtain the rate of perihelion shift $d \varpi / d t$ , in seconds of arc per century,

$$
\frac { d \varpi } { d t } = 4 2 . 9 8 0 \left[ \frac { 1 } { 3 } \left( 2 + 2 \gamma - \beta \right) + 6 . 5 \times 1 0 ^ { - 4 } \left( \frac { J _ { 2 } } { 2 . 2 \times 1 0 ^ { - 7 } } \right) \right] .
$$

(see Nobili and Will (1986) for a discussion of how the precise numerical value of the GR prediction is obtained).

In the current method of testing gravitational theories using the dynamics of Mercury, the actual value of the predicted advance is somewhat irrelevant. Instead, the equations of motion used in all ephemeris computer codes to predict the orbits of Mercury and of all the planets are the $\mathrm { P P N } N .$ -body equations (6.46c). Those equations contain all the effects needed to determine the total advance of the perihelion of Mercury, including both the effects of the other planets and post-Newtonian effects. The modeling of the orbits depends on a host of parameters. These include masses and orbit elements at a chosen epoch of all the planets, of the Moon and many of the other moons of the planets, and of many asteroids. The effects of solar wind and radiation pressure on spacecraft must be modeled. Parameters associated

# Box 7.2

The solar oblateness controversy During the 1960s, Robert Dicke and Mark Goldenberg attempted to determine $J _ { 2 }$ by measuring the Sun’s visual shape. Because the surface of the Sun is an equipotential, its shape is affected by $J _ { 2 }$ in a way that can be directly related to the deformation of the external gravitational field. The shape was measured by inserting a circular, opaque disk in front of a telescopic image of the Sun, leaving only a thin visible ring at the edge of the Sun, and measuring the difference in brightness of the visible ring between the equator and pole of the Sun. If the Sun were oblate, the ring at the equator should extend further beyond the occulting disk, and should therefore be brighter. But many factors had to be corrected for, including the effects of atmospheric distortion on the observed shape of the Sun, and the effects of possible temperature differences between the polar and equatorial regions of the Sun, which would lead to brightness differences not associated with the shape. Dicke and Goldenberg claimed to have measured a $J _ { 2 }$ of the order of $2 . 5 \times 1 0 ^ { - 5 }$ , over 100 times larger than the currently accepted value. Dicke postulated that such a large oblateness would occur if the core of the Sun were rotating much faster than its outer layers, thereby generating more centrifugal flattening than would be expected on the basis of the observed surface rotation alone (see Dicke and Goldenberg (1974) for a review).

A value of $J _ { 2 }$ this large would mean that solar oblateness contributes as much as 4 arcseconds per century to Mercury’s perihelion advance, which would destroy the agreement of the measured advance with the prediction of general relativity. But it would have supported the Brans-Dicke theory of gravity if $\omega _ { \mathrm { B D } }$ were chosen to be around 5, a value favored by Dicke for other reasons. Later observations of the visible shape of the Sun by Henry Hill and others, along with observations to try to better understand the temperature differences, did not fully resolve this controversy.

The resolution came with the advance of helioseismology. This was the discovery that the Sun vibrates in a superposition of thousands of normal modes with an array of frequencies, as could be observed by measuring the frequency spectrum of Doppler-shifted solar spectral lines. The specific pattern of frequencies depends on the Sun’s angular-velocity profile. Through a systematic program of ground-based and spacebased observations of the Sun, it became possible to determine the Sun’s rotational profile over much of its interior. The conclusion was that the core does not rotate much faster than the surface, and solar models consistent with this information produced the currently accepted value of $J _ { 2 } = 2 . 2 \times 1 0 ^ { - 7 } ;$ this is approximately what one would infer from a Sun that rotates uniformly at its observed surface rate.

with the effects of the interplanetary plasma and the Earth’s atmosphere on the propagation of the tracking signals, and with variations in locations of radar tracking stations caused by Earth rotation changes and tidal effects are included. Finally, the PPN parameters are included. The relevant data include centuries of optical observations of planetary motions on the sky, radar measurements of planets and spacecraft, and laser ranging to the Moon. Predicted orbits are compared with the data, and the parameters are adjusted to obtain a best fit in the least-squares sense. The results include an estimate for the PPN parameter combination $( 2 + 2 \gamma - \beta ) / 3$ , along with an associated error. Some data sets are particularly sensitive to the Shapiro time delay, and these provide accurate estimates of $( 1 + \gamma ) / 2$ . Lunar laser ranging data are sensitive to the Nordtvedt effect (to be discussed in Chapter 8), and improve the parameters of the Earth’s orbit about the Earth–Moon barycenter. As the data improve, either from more accurate range or Doppler measurements, or from new satellite missions, particularly planetary flyby and orbiter missions, the estimates for many parameters may change and the errors may decrease.

By the end of the 1970s, measurements of the factor $( 2 + 2 \gamma - \beta ) / 3$ had attained precisions of roughly 0.5 percent, through analyses of three centuries of optical observations of Mercury’s orbit, and of radar measurements since the middle 1960s both to Mercury’s surface and to the Mariner 10 spacecraft, which had close encounters with Mercury in 1974 and 1975. These estimates continued to improve somewhat during the 1980s and 1990s through the steady accumulation of data. However, a major advance in measuring the perihelion advance was made by exploiting Mercury MESSENGER. In 2011, MESSENGER became the first spacecraft to orbit Mercury, and range and Doppler measurements of the orbiter were made until the spacecraft ended its mission in 2015 with a controlled crash on the surface of Mercury. By 2013, MESSENGER data had already led to dramatically improved knowledge of Mercury’s orbit. One analysis of all the available data yielded bounds on $\gamma$ and $\beta$ given by $\gamma - 1 = ( - 0 . 3 \pm 2 . 5 ) \times 1 0 ^ { - 5 }$ and $\beta - 1 = ( 0 . 2 \pm 2 . 5 ) \times 1 0 ^ { - 5 }$ (Fienga et al., 2011; Verma et al., 2014; Fienga et al., 2015). The bound on $\gamma$ is consistent with that obtained from the dedicated test of the Shapiro time delay using Cassini (Section 7.2). The analysis also yielded an estimate $J _ { 2 } = ( 2 . 4 \pm 0 . 2 ) \times 1 0 ^ { - 7 }$ , consistent with the results from helioseismology. Taking into account the errors in $\gamma$ and $\beta$ at the level of $2 . 5 \times 1 0 ^ { - 5 }$ , this corresponds to an effective measurement of the relativistic perihelion advance of Mercury at $4 2 . 9 8 0 \pm 0 . 0 0 1$ arcseconds per century. This precision could be improved using future data from BepiColombo (Milani et al., 2002; Ashby et al., 2007).

A slightly weaker bound $\beta - 1 = ( 0 . 4 \pm 2 . 4 ) \times 1 0 ^ { - 4 }$ from the perihelion advance of Mars (adopting the Cassini bound on $\gamma$ a priori) was obtained by exploiting data from the Mars Reconnaissance Orbiter (Konopliv et al., 2011). Laser tracking of the Earthorbiting satellite LAGEOS II led to a measurement of its relativistic perigee precession (3.3 arcseconds per year) in agreement with general relativity to 2 percent (Lucchesi and Peron, 2010, 2014).

The next class of experiments that test relativistic gravitational effects may be called tests of the Strong Equivalence Principle (SEP). That principle states that (i) WEP is valid for self-gravitating bodies as well as for test bodies (GWEP), (ii) the outcome of any local test experiment, gravitational or nongravitational, is independent of the velocity of the freely falling apparatus, and (iii) the outcome of any local test experiment is independent of where and when in the universe it is performed. In Section 3.3, we pointed out that many metric theories of gravity (perhaps all except general relativity) can be expected to violate one or more aspects of SEP. In Chapter 6, working within the PPN framework, we saw explicit evidence of some of these violations: violations of GWEP in the equations of motion for massive self-gravitating bodies, Eq. (6.46b); preferred-frame effects in the $N .$ - body equations of motion, Eq. (6.46c); and preferred-frame and preferred-location effects in the locally measured gravitational constant, Eq. (6.100).

This chapter is devoted to the study of some of the observable consequences of such violations of SEP, and to the experiments that test for them. In Section 8.1, we consider violations of GWEP (the Nordtvedt effect), and its primary experimental test via Lunar laser ranging. Section 8.2 focuses on preferred-frame and preferred-location effects on the orbital motions of planets and binary systems, while Section 8.3 analyzes such effects on the structure of self-gravitating bodies. Another violation of SEP would be the variation with time of the gravitational constant $G$ as a result of cosmic evolution. Tests of such a variation are described in Section 8.5.

# 8.1 The Nordtvedt Effect

The breakdown in the Weak Equivalence Principle for massive, self-gravitating bodies (GWEP), which many metric theories predict, has a variety of observable consequences. In Chapter 6, we saw that this violation could be expressed in quasi-Newtonian language by attributing to each massive body inertial and passive gravitational mass tensors $\tilde { m } _ { \mathrm { I } } ^ { j k }$ and $\tilde { m } _ { \mathrm { P } } ^ { j k }$ I , which may differ from each other. The quasi-Newtonian part of the body’s acceleration may then be written [see Eq. (6.54)]

$$
( \tilde { m } _ { \mathrm { I } } ) _ { a } ^ { j k } ( a _ { a } ^ { k } ) _ { \mathrm { N e w t } } = ( \tilde { m } _ { \mathrm { P } } ) _ { a } ^ { l m } \Omega _ { , j } ^ { l m } ,
$$

where $\mathfrak { U } ^ { l m }$ is a quasi-Newtonian gravitational potential, and the inertial and passive mass tensors, $\tilde { m } _ { \mathrm { I } } ^ { j k }$ and $\tilde { m } _ { \mathrm { P } } ^ { j k }$ , are given by

$$
\begin{array} { l } { { ( \tilde { m } _ { \mathrm { I } } ) _ { a } ^ { j k } \equiv m _ { a } \left\{ \delta ^ { j k } \left[ 1 + ( \alpha _ { 1 } - \alpha _ { 2 } + \zeta _ { 1 } ) \displaystyle \frac { \Omega _ { a } } { m _ { a } } \right] + ( \alpha _ { 2 } - \zeta _ { 1 } + \zeta _ { 2 } ) \displaystyle \frac { \Omega _ { a } ^ { j k } } { m _ { a } } \right\} , } } \\ { { ( \tilde { m } _ { \mathrm { P } } ) _ { a } ^ { l m } \equiv m _ { a } \left\{ \delta ^ { l m } \left[ 1 + ( 4 \beta - \gamma - 3 - 3 \xi ) \displaystyle \frac { \Omega _ { a } } { m _ { a } } \right] - \xi \displaystyle \frac { \Omega _ { a } ^ { l m } } { m _ { a } } \right\} , } } \end{array}
$$

where $\Omega _ { a }$ and $\Omega _ { a } ^ { j k }$ are the body’s internal gravitational energy and gravitational energy tensor (see Box 6.2 for definitions), and $m _ { a }$ is the total mass energy of the body. Most self-gravitating bodies (planets, stars) are very nearly spherically symmetric, so we may approximate

$$
\Omega _ { a } ^ { j k } \simeq \frac 1 3 \Omega _ { a } \delta ^ { j k } .
$$

With these approximations, we write the quasi-Newtonian equation (8.1) in the form

$$
{ \pmb a } _ { a } = \left( \frac { m _ { \mathrm { P } } } { m } \right) _ { a } \nabla \mathfrak { U } ,
$$

where

$$
\begin{array} { l } { \displaystyle ( \frac { m _ { \mathrm { P } } } { m } ) _ { a } = 1 + ( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } ) \frac { \Omega _ { a } } { m _ { a } } , } \\ { \displaystyle   \mathrm { A } = \sum _ { b \neq a } \frac { ( m _ { \mathrm { A } } ) _ { b } } { r _ { a b } } .  } \end{array}
$$

The most important consequence of the Nordtvedt effect is a polarization of the orbit of a binary system in the presence of a third body. If the self-gravitational energy per unit mass of one member of the binary is larger than that of its companion, then the two bodies may fall toward the distant third body with slightly different accelerations, leading to the orbital polarization. The most notable example is that of the Earth–Moon orbit in the presence of the Sun (Nordtvedt, 1968c). Other examples include binary systems (especially binary pulsars) in the presence of the galaxy, and the recently discovered pulsar in a triple system, consisting of a neutron star and two white-dwarf companions.

Even in pure Newtonian gravity, the three-body problem is notoriously difficult. However, if the system is “hierarchical,” meaning that the average separation of one pair of bodies is small compared to the distance between that pair and the third body, then the problem is amenable to an expansion in terms of the small parameter $r / R$ where $r$ and $R$ are the two separations (in some situations, a better expansion parameter is the ratio of the period of the inner binary to that of the third body, $P _ { b } / P _ { 3 }$ ). In hierarchical triple systems, the inner binary can be treated as a Keplerian two-body orbit to lowest order, with the third body producing small perturbations.

Using our quasi-Newtonian equation of motion (8.4), we obtain, for a two-body system in the presence of a third body

$$
\begin{array} { r l } & { { \pmb a } _ { 1 } = - \left( \frac { m _ { \mathrm { P } } } { m } \right) _ { 1 } \left[ ( m _ { \mathrm { A } } ) _ { 2 } \frac { { \pmb x } _ { 1 2 } } { r _ { 1 2 } ^ { 3 } } + ( m _ { \mathrm { A } } ) _ { 3 } \frac { { \pmb x } _ { 1 3 } } { r _ { 1 3 } ^ { 3 } } \right] , } \\ & { { \pmb a } _ { 2 } = \left( \frac { m _ { \mathrm { P } } } { m } \right) _ { 2 } \left[ ( m _ { \mathrm { A } } ) _ { 1 } \frac { { \pmb x } _ { 1 2 } } { r _ { 1 2 } ^ { 3 } } - ( m _ { \mathrm { A } } ) _ { 3 } \frac { { \pmb x } _ { 2 3 } } { r _ { 2 3 } ^ { 3 } } \right] . } \end{array}
$$

We denote the barycenter position of the two-body system by

$$
{ \pmb x } _ { c } \equiv \frac { m _ { 1 } } { m } { \pmb x } _ { 1 } + \frac { m _ { 2 } } { m } { \pmb x } _ { 2 } ,
$$

where $m \equiv m _ { 1 } + m _ { 2 }$ . Assuming that $r _ { 1 2 } \ll r _ { 2 3 }$ , we expand

$$
\frac { x _ { 1 3 } ^ { j } } { r _ { 1 3 } ^ { 3 } } = \frac { x _ { c 3 } ^ { j } } { r _ { c 3 } ^ { 3 } } - x _ { 1 c } ^ { k } \left( \frac { 1 } { r _ { c 3 } } \right) _ { , j k } - \frac { 1 } { 2 } x _ { 1 c } ^ { k } x _ { 1 c } ^ { m } \left( \frac { 1 } { r _ { c 3 } } \right) _ { , j k m } + O ( r _ { 1 c } ^ { 3 } / r _ { c 3 } ^ { 5 } ) ,
$$

where ${ \pmb x } _ { c 3 } \equiv { \pmb x } _ { c } - { \pmb x } _ { 3 }$ and ${ \pmb x } _ { 1 c } \equiv { \pmb x } _ { 1 } - { \pmb x } _ { c }$ ; we expand $x _ { 2 3 } ^ { j } / r _ { 2 3 } ^ { 3 }$ in a similar fashion. We define $R \equiv r _ { c 3 } = | \pmb { x } _ { c 3 } | , N \equiv { \bf x } _ { c 3 } / r _ { c 3 }$ , ${ \pmb n } _ { 1 c } \equiv { \pmb x } _ { 1 c } / r _ { 1 c }$ , ${ \pmb n } _ { 2 c } \equiv { \pmb x } _ { 2 c } / r _ { 2 c }$ , and notice that

$$
r _ { 1 c } = ( m _ { 2 } / m ) r , \qquad r _ { 2 c } = ( m _ { 1 } / m ) r , \qquad n _ { 1 c } = - n _ { 2 c } = n ,
$$

where $r \equiv \left| \boldsymbol { r } _ { 1 2 } \right|$ and ${ \pmb n } \equiv { \pmb x } _ { 1 2 } / r _ { 1 2 }$ . With this notation we find that the relative acceleration $\pmb { a } \equiv \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ is given by

$$
\begin{array} { c } { { \displaystyle { \pmb a } = - \frac { m ^ { * } } { r ^ { 2 } } { \pmb n } - \delta \frac { m _ { 3 } } { R ^ { 2 } } { \pmb N } + \alpha ^ { * } \frac { m _ { 3 } r } { R ^ { 3 } } \big [ 3 { \pmb N } ( { \pmb N } \cdot { \pmb n } ) - { \pmb n } \big ] } } \\ { { - \frac { 3 } { 2 } \Delta ^ { * } \frac { m _ { 3 } r ^ { 2 } } { R ^ { 4 } } \big [ 5 { \pmb N } ( { \pmb N } \cdot { \pmb n } ) ^ { 2 } - 2 { \pmb n } ( { \pmb N } \cdot { \pmb n } ) - { \pmb N } \big ] , } } \end{array}
$$

where $m ^ { * }$ is defined by Eq. (6.71), we have dropped the A subscript on $m _ { 3 }$ , and we have defined

$$
\begin{array} { l } { { \alpha ^ { * } \equiv \alpha + \displaystyle \frac { 1 } { 2 } \delta \Delta , } } \\ { { \Delta ^ { * } \equiv \Delta \alpha + \displaystyle \frac { 1 } { 2 } \delta ( 1 - 2 \eta ) , } } \end{array}
$$

where

$$
{ \begin{array} { r l } & { \alpha \equiv { \frac { 1 } { 2 } } \left[ \left( { \frac { m _ { \mathrm { P } } } { m } } \right) _ { 1 } + \left( { \frac { m _ { \mathrm { P } } } { m } } \right) _ { 2 } \right] , } \\ & { \delta \equiv \left( { \frac { m _ { \mathrm { P } } } { m } } \right) _ { 1 } - \left( { \frac { m _ { \mathrm { P } } } { m } } \right) _ { 2 } , } \\ & { \Delta \equiv { \frac { m _ { 2 } - m _ { 1 } } { m _ { 1 } + m _ { 2 } } } . } \end{array} }
$$

The first term in Eq. (8.10) is the standard Newtonian acceleration; since $m ^ { * }$ represents the Kepler-measured mass of the two-body system we will replace it by $m$ . The second term is a relative acceleration that stretches or shrinks the orbit along a line directed toward the third body—this is the Nordtvedt effect. From Eq. (8.5) we have that

$$
\delta = \left( 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } \right) \left( \frac { \Omega _ { 1 } } { m _ { 1 } } - \frac { \Omega _ { 2 } } { m _ { 2 } } \right) .
$$

The third and fourth terms originate from the Newtonian tidal interactions with the third body, and they typically give rise to orbital perturbations that are substantially larger than the nominal size of the Nordtvedt effect.

We now consider a simplified situation in which the inner and outer orbits lie in the same plane (for the Earth–Moon-Sun system, their actual relative inclination is about $5 ^ { \circ }$ ), the inner orbit is approximately circular (the eccentricity of the Moon-Earth orbit is 0.055)

and the outer orbit is circular (the eccentricity of the Earth-Sun orbit is 0.017). We calculate the first-order perturbations of the inner orbit created by the last three terms in Eq. (8.10). In the limit of small eccentricity, we can write for the inner binary $d \phi / d t = \omega _ { b } \approx$ constant, and for the outer binary, $d \phi / d t = \omega _ { 3 } =$ constant, so that

$$
\begin{array} { r l } & { r = a ( 1 - e \cos f ) + O ( e ^ { 2 } ) , } \\ & { f = \phi - \omega = \omega _ { b } t - \omega + O ( e ) , } \\ & { n = e _ { X } \cos \left( \omega _ { b } t \right) + e _ { Y } \sin \left( \omega _ { b } t \right) + O ( e ) , } \\ & { \lambda = - e _ { X } \sin \left( \omega _ { b } t \right) + e _ { Y } \cos \left( \omega _ { b } t \right) + O ( e ) , } \\ & { N = e _ { X } \cos \left( \omega _ { 3 } t - \Phi \right) + e _ { Y } \sin \left( \omega _ { 3 } t - \Phi \right) , } \end{array}
$$

where $e$ is the eccentricity of the inner orbit, and $\Phi$ is the initial phase of the third body. Note that

$$
\begin{array} { c } { { { \pmb { n } } \cdot { \cal N } = \cos \left( \Lambda t + \Phi \right) , } } \\ { { \lambda \cdot { \cal N } = - \sin \left( \Lambda t + \Phi \right) , } } \end{array}
$$

where $\Lambda \equiv \omega _ { b } - \omega _ { 3 }$

We now use the Lagrange planetary equations reviewed in Section 6.4.2. This must be done with some care, because the orbital eccentricity is small, and $\omega$ loses its meaning when $e \to 0$ . In such cases it is best to use the alternative variables $A \equiv e \cos \omega$ and $B \equiv e \sin \omega$ , and to reexpress the Lagrange planetary in terms of $A$ and $B$ . We therefore write

$$
r = a \big [ 1 - A \cos \left( \omega _ { b } t \right) - B \sin \left( \omega _ { b } t \right) \big ] + O ( e ^ { 2 } ) ,
$$

and convert Eqs. (6.74) to the form

$$
\begin{array} { l } { \displaystyle \frac { d a } { d t } = \frac { 2 } { \omega _ { b } } S + O ( e ) , } \\ { \displaystyle \frac { d A } { d t } = \frac { 1 } { \omega _ { b } p } \Big [ \mathcal { R } \sin \left( \omega _ { b } t \right) + 2 S \cos \left( \omega _ { b } t \right) \Big ] + O ( e ) , } \\ { \displaystyle \frac { d B } { d t } = \frac { 1 } { \omega _ { b } p } \Big [ - \mathcal { R } \cos \left( \omega _ { b } t \right) + 2 S \sin \left( \omega _ { b } t \right) \Big ] + O ( e ) , } \end{array}
$$

where $\mathcal { R }$ and $\boldsymbol { \mathcal { S } }$ are the radial and tangential components of the perturbing acceleration, and we have used the fact that $( p / m ) ^ { 1 / 2 } = ( \omega _ { b } p ) ^ { - 1 } + O ( e ^ { 2 } )$ . To lowest order in $e$ , $\mathcal { R }$ and $\boldsymbol { \mathcal { S } }$ are given by

$$
\begin{array} { c c } { { \displaystyle \mathcal { R } = \omega _ { 3 } ^ { 2 } a \Bigg \{ \alpha ^ { * } \big [ 3 \cos ^ { 2 } ( \Lambda t + \Phi ) - 1 \big ] - \frac { 3 } { 2 } \frac { a } { R } \Delta ^ { * } \cos \left( \Lambda t + \Phi \right) \big [ 5 \cos ^ { 2 } ( \Lambda t + \Phi ) - 3 \big ] } } \\ { { \displaystyle \qquad - \frac { R } { a } \delta \cos \left( \Lambda t + \Phi \right) \Bigg \} , } } & { { \mathrm { ( 8 . 2 0 ~ } \mathrm { R e ~  { \alpha } ~ , } } } \\ { { \displaystyle \mathcal { S } = \omega _ { 3 } ^ { 2 } a \Bigg \{ - 3 \alpha ^ { * } \sin \left( \Lambda t + \Phi \right) \cos \left( \Lambda t + \Phi \right) + \frac { 3 } { 2 } \frac { a } { R } \Delta ^ { * } \sin \left( \Lambda t + \Phi \right) \big [ 5 \cos ^ { 2 } ( \Lambda t + \Phi ) - 1 \big ] } } \\ { { \displaystyle \qquad + \frac { R } { a } \delta \sin \left( \Lambda t + \Phi \right) \Bigg \} , } } & { { \mathrm { ( 8 . 2 1 ~ } \mathrm { R e ~  { \alpha } ~ , } } } \end{array}
$$

where $\omega _ { 3 } ^ { 2 } ~ \equiv ~ m _ { 3 } / R ^ { 3 }$ . Because the orbital planes are taken to coincide, there are no perturbations of the inclination $\iota$ or line of nodes $\Omega$ .

Substituting Eq. (8.21) into Eq. (8.19), integrating subject to the boundary conditions $a = a _ { 0 } , A = A _ { 0 } , B = B _ { 0 }$ at $t = 0$ , and inserting the results into Eq. (8.16), we obtain

$$
\begin{array} { r l } { \delta r ( t ) = a ^ { \prime } \left[ 1 - A ^ { \prime } \cos \left( \omega _ { b } t \right) - B ^ { \prime } \sin \left( \omega _ { b } t \right) \right] } & { } \\ { + a _ { 0 } \left( \frac { \omega _ { 3 } } { \omega _ { b } } \right) ^ { 2 } \Bigg \{ \frac { 3 } { 2 } \alpha ^ { * } \frac { \omega _ { b } ^ { 2 } \left( 1 + \omega _ { b } / \Lambda \right) } { \omega _ { b } ^ { 2 } - 4 \Lambda ^ { 2 } } \cos 2 ( \Lambda t + \Phi ) } & { } \\ { - \frac { 1 } { 8 } \frac { a _ { 0 } } { R } \Delta ^ { * } \Bigg [ \frac { 3 \omega _ { b } ^ { 2 } \left( 3 + 2 \omega _ { b } / \Lambda \right) } { \omega _ { b } ^ { 2 } - \Lambda ^ { 2 } } \cos \left( \Lambda t + \Phi \right) } & { } \\ { + \frac { 5 \omega _ { b } ^ { 2 } \left( 3 + 2 \omega _ { b } / \Lambda \right) } { \omega _ { b } ^ { 2 } - 9 \Lambda ^ { 2 } } \cos 3 ( \Lambda t + \Phi ) \Bigg ] } & { } \\ { - \delta \frac { R } { a _ { 0 } } \frac { \omega _ { b } ^ { 2 } \left( 1 + 2 \omega _ { b } / \Lambda \right) } { \omega _ { b } ^ { 2 } - \Lambda ^ { 2 } } \cos \left( \Lambda t + \Phi \right) . \Bigg \} , } \end{array}
$$

where $a ^ { \prime } , \ A ^ { \prime }$ and $B ^ { \prime }$ differ from $a _ { 0 } , \ A _ { 0 }$ and $B _ { 0 }$ by small corrections induced by the perturbations, and represent unobservable constant shifts in the orbit elements. The remaining terms depend on the difference $\Lambda = \omega _ { b } - \omega _ { 3 }$ , and thus have a very different time dependence from that of the eccentric orbit. Notice that, because we have a sinusoidal driving force acting on a sinusoidal oscillator, the solutions take the form of a resonant response, with denominators of the form $1 / ( \omega _ { b } ^ { 2 } - N ^ { 2 } \Lambda ^ { 2 } )$ , with $N$ representing the harmonic degree. If $N = 1$ , then, if $\omega _ { 3 } ~ \ll ~ \omega _ { b }$ , the resonant factor becomes $\omega _ { b } ^ { 2 } / ( \omega _ { b } ^ { 2 } \mathrm { ~ - ~ } \Lambda ^ { 2 } ) \ \approx$ $\omega _ { b } / 2 \omega _ { 3 } \gg 1$ , leading to an enhanced amplitude.

We first apply these results to the Earth–Moon system, with the Sun making up the third body. We set $m _ { 2 } = m _ { \oplus }$ $, m _ { 1 } = m _ { \mathbb { Q } } = m _ { \oplus } / 8 1 . 3$ , $m _ { 3 } = m _ { \odot }$ , $\omega _ { b } = \omega _ { \mathbb { Q } }$ , the angular velocity of the Moon around the Earth, and $\omega _ { 3 } = \omega _ { \oplus }$ , the angular velocity of the Earth around the Sun, with $\omega _ { \mathbb { Q } } \approx 1 3 . 3 7 \omega _ { \oplus } = 2 . 6 6 \times 1 0 ^ { - 6 } \mathrm { s } ^ { - 1 }$ . In the Earth–Moon system, $\Lambda$ is known as the synodic frequency, the angular frequency of the lunar orbit relative to the Sun. This is to be distinguished from the sidereal frequency $\omega _ { \mathbb { ( } }$ , which refers to the global coordinate frame. We also have

$$
\frac { \Omega _ { \oplus } } { m _ { \oplus } } = - 4 . 6 \times 1 0 ^ { - 1 0 } , \quad \frac { \Omega _ { \ ? } } { m _ { \ ? } } = - 0 . 2 \times 1 0 ^ { - 1 0 } ,
$$

and $R / a _ { 0 } ~ \approx ~ 3 9 0$ . Inserting the relevant numbers for the Earth–Moon system, setting $\delta \simeq 4 . 4 \times 1 0 ^ { - 1 0 }$ , and taking into account the fact that $a _ { 0 } \approx 3 . 8 4 \times 1 0 ^ { 5 } { \mathrm { ~ k m } }$ , we see that the three tidal perturbations and the Nordtvedt effect have approximate amplitudes of $2 7 7 0 \ \mathrm { k m } \ ( 2 \Lambda ) , \ 3 \ \mathrm { k m } \ ( 3 \Lambda ) , \ 7 3 \ \mathrm { k m } \ ( $ , and 8 meters $( \Lambda )$ , respectively. Two of the tidal perturbations occur at twice and three times the synodic frequency, whereas the Nordtvedt effect occurs at the synodic frequency; the tidal perturbations are much larger, but they can be cleanly separated from the Nordtvedt effect by observing many lunar orbits. The third tidal perturbation contributes at frequency $\Lambda$ with an amplitude of $7 3 \mathrm { k m }$ . However, because this perturbation depends on parameters $( \omega _ { \oplus } , \omega _ { \mathbb { Q } } , R , a _ { 0 } , \Delta )$ that are very accurately measured by other means, it can be predicted in advance to an accuracy well below the amplitude of the Nordtvedt effect.

In fact, an accurate calculation of the relevant amplitudes would require us to go beyond the first-order perturbation analysis carried out here. The perturbations induced by each term affect the behavior of the other terms, and so it is necessary to go to higher order in the orbital perturbation equations, and to include higher values of the multipole index $\ell$ . The problem is that the solar perturbation of the lunar orbit is so large, as seen by the $2 7 7 0 \mathrm { k m }$ leading tidal amplitude, that one must employ more sophisticated techniques, such as the Hill-Brown lunar theory, in order to find a sequence of perturbations that converges in a reasonable way. The final conclusion of such calculations is that the effective amplitude of the Nordtvedt term is increased from the amplitude shown in Eq. (8.22) by a factor approximately equal to $1 + 2 \omega _ { \oplus } / \omega _ { \mathbb { Q } } \ \simeq \ 1 . 1 5$ , leading to an amplitude of 9.2 meters. Similarly, the amplitude of the competing synodic term is increased from $7 3 ~ \mathrm { k m }$ to 110 km, but it can still be predicted accurately enough to be subtracted from the data.

The resulting prediction for the Nordtvedt effect is

$$
\delta r ( t ) \simeq 9 . 2 \eta _ { N } \cos { ( \Lambda t + \Phi ) } \mathrm { m } ,
$$

where $\eta _ { N }$ is the Nordtvedt parameter

$$
\eta _ { N } \equiv 4 \beta - \gamma - 3 - \frac { 1 0 } { 3 } \xi - \alpha _ { 1 } + \frac { 2 } { 3 } \alpha _ { 2 } - \frac { 2 } { 3 } \zeta _ { 1 } - \frac { 1 } { 3 } \zeta _ { 2 } .
$$

As we explain in $\mathrm { B o x } 8 . 1$ , long-term monitoring of the lunar orbit has revealed no sign of a Nordtvedt effect, and $\eta _ { N }$ is currently constrained to be smaller than about $4 \times 1 0 ^ { - 4 }$ .

Tests of the Nordtvedt effect for neutron stars have also been carried out using a class of systems known as “wide-orbit binary millisecond pulsars” (WBMSP). These are pulsarwhite-dwarf binaries with orbital periods ranging from 5 to 800 days, and eccentricities ranging from $1 0 ^ { - 3 }$ to $1 0 ^ { - 5 }$ . In the gravitational field of the galaxy, a non-zero Nordtvedt effect can induce an anomalous eccentricity pointed toward the galactic center (Damour and Schaefer, 1991). This can be bounded using statistical methods, given a sufficient number of WBMSPs. The current bound is $| \eta _ { N } ( \Omega / m ) _ { \mathrm { N S } } | < 4 . 6 \times 1 0 ^ { - 3 }$ , from data on more than 20 WBMSPs, including some highly circular systems (Stairs et al., 2005; Gonzalez et al., 2011). Because $( \Omega / m ) _ { \mathrm { N S } } \sim 0 . 1$ for typical neutron stars, this bound on $\eta _ { N }$ does not compete with the bound from LLR; on the other hand, the presence of neutron stars implies that these systems test the Strong Equivalence Principle in the strong-field regime. Freire et al. (2012) discuss ways to carry out this test in WBMSP systems without relying on statistical averages over many systems.

The remarkable pulsar in a triple system $J 0 3 3 7 \substack { + 1 7 1 5 }$ , reported by Ransom et al. (2014), may provide a test of the Nordtvedt effect that supercedes that from LLR. The system consists of a millisecond pulsar in a 1.6 day orbit with a white-dwarf companion of $0 . 2 M _ { \odot }$ , with a more distant $0 . 4 M _ { \odot }$ white dwarf in a 327 day orbit around the pair. The two orbits are almost perfectly coplanar and highly circular. The key parameters of the system are shown in Table 8.1. Inserting those parameters into Eq. (8.22), we find that the three tidal perturbations have amplitudes $2 . 2 \times 1 0 ^ { 5 } \mathrm { k m } ( 2 \Lambda ) , 2 \times 1 0 ^ { 3 } \mathrm { k m } ( 3 \Lambda )$ and $1 . 1 \times 1 0 ^ { 4 } \mathrm { k m } \left( \Lambda \right)$ , while the Nordtvedt effect $( \Lambda )$ has the amplitude

$$
\delta r _ { N } \sim 3 5 4 \mathrm { k m } \left( \frac { \eta _ { N } } { 1 0 ^ { - 4 } } \right) \left( \frac { \Omega _ { 1 } / m _ { 1 } - \Omega _ { 2 } / m _ { 2 } } { 0 . 1 } \right) ,
$$

# Box 8.1

# Lunar laser ranging and the Nordtvedt effect

In the late 1950s, Dicke wondered whether one could measure a variation with time of Newton’s constant G, a feature that he would soon incorporate into Brans-Dicke theory. By the early 1960s, the development of pulsed ruby lasers and the rapid build-up of the lunar space program led him and others to propose making very accurate measurements of the Earth–Moon distance by bouncing laser pulses off specially designed reflectors, to be placed on the lunar surface by either unmanned or manned landers. Such measurements would provide tests of general relativity, but they would also have other important scientific benefits, such as improving our understanding of the Earth–Moon orbit, the librations of the Moon, and even the motions of the Earth-bound laser sources resulting from tidal motions and continental drift.

The first retroreflector was deployed on the Moon by US Apollo 11 astronaut Neil Armstrong on July 21, 1969, and within a month, the first successful acquisition was made of a reflected laser signal. Two other US and two French-built reflectors were subsequently placed on the Moon by US astronauts and Soviet unmanned landers. Strangely, the French reflectors were never detected via laser bounces, until just recently.

Since that time a worldwide network of observatories has made regular measurements of the round-trip travel time to the three US lunar retroreflectors, with accuracies that are routinely at the 50 ps (1 cm) level, and that are approaching 5 ps (1 mm). These measurements are fit using the method of least-squares to a theoretical model for the lunar motion that takes into account perturbations created by the Sun and the other planets, tidal interactions, and post-Newtonian gravitational effects. The predicted round-trip travel times between retroreflector and telescope also take into account the librations of the Moon, the orientation of the Earth, the location of the observatories, and atmospheric effects on the signal propagation. The Nordtvedt parameter is then estimated in the least-squares fit, along with several other important parameters of the model.

From the first published analyses of lunar laser ranging (LLR) data in 1976 to the present, there has been absolutely no evidence, within experimental uncertainty, for the Nordtvedt effect. The residual orbital perturbation is $\delta r ( t ) = ( 2 . 8 \pm 4 . 1 ) \mathrm { m m } \cos { ( \Lambda t + \Phi ) }$ .

At this level of precision, however, we can’t regard the results of LLR as a completely “clean” test of the Nordtvedt effect until we consider the possibility of a compensating violation of the Weak Equivalence Principle for the Earth and Moon. This is because the chemical compositions of the Earth and Moon differ: the Earth is richer in the iron group elements, while the Moon is richer in silicates. To address this issue, the Eöt-Wash group at the University of Washington in Seattle carried out a novel torsion-balance test of WEP by fabricating laboratory bodies whose chemical compositions mimic that of the Earth and Moon. They found that the mini-Earth and mini-Moon fell with the same acceleration to 1.4 parts in $1 0 ^ { 1 3 }$ (Baeßler et al., 1999; Adelberger, 2001). Combining this limit with the results for $\delta r ( t )$ led to a bound on the Nordtvedt parameter

$$
\eta _ { N } = ( 4 . 4 \pm 4 . 5 ) \times 1 0 ^ { - 4 } .
$$

This represents a limit on a possible violation of the Strong Equivalence Principle of about 2 parts in $1 0 ^ { 1 3 }$ (Williams et al., 2004b, 2009; Hofmann et al., 2010).

The Apache Point Observatory for Lunar Laser ranging Operation (APOLLO) project, a joint effort by researchers from the University of Washington, Seattle, and the University of California, San Diego, is using enhanced laser and telescope technology, together with a good, high-altitude site in New Mexico, hoping to improve the LLR bound by as much as an order of magnitude (Murphy et al., 2012). Strangely, the current limitation is not the laser ranging itself (which routinely reaches millimeter levels of precision) but the fact that many of the large ephemeris codes used to analyze the data have not kept pace with the improved data on solar-system dynamics. This effort will be aided by the fortuitous 2010 discovery by the Lunar Reconnaissance Orbiter of the precise landing site of the Soviet Lunokhod I rover, which deployed a French retroreflector in 1970. Its uncertain location made it effectively lost to lunar laser ranging for almost 40 years. Its location on the lunar surface will make it useful in improving models of the lunar libration (Murphy et al., 2011).

Lunar laser ranging also yielded important bounds on the PPN parameters $\alpha _ { 1 }$ and $\alpha _ { 2 }$ and on a time variation of G (see Sections 8.4 and 8.5).

<table><tr><td colspan="2">Table 8.1 Parameters of the pulsar J0337+1715 triple system. Numbers in parentheses denote errors in the last digit.</td></tr><tr><td>Parameter</td><td> Value</td></tr><tr><td>Pulsar mass Inner companion mass Outer companion mass</td><td>1.438(1)Mo 0.1975(2)Mo 0.4101(3)Mo</td></tr><tr><td>Inner orbit Semimajor axis Orbital period</td><td>1.9242(4) 1s 1.629401788(5) d</td></tr><tr><td>Eccentricity Inclination</td><td>6.9178(2) × 10-4 39.25(1)°</td></tr><tr><td>Outer orbit</td><td></td></tr><tr><td></td><td></td></tr><tr><td>Semimajor axis</td><td>118.04(3) 1s</td></tr><tr><td>Orbital period</td><td>327.257541(7) d</td></tr><tr><td></td><td></td></tr><tr><td>Eccentricity Inclination</td><td>3.5356196(2) × 10-2 39.24(1)°</td></tr></table>

where we have scaled $\eta _ { N }$ by the approximate current bound from LLR, and the selfgravitational energy difference by 0.1, a typical value for neutron stars in general relativity (compare with the parts in $1 0 ^ { 1 0 }$ for the Earth–Moon system and parts in $1 0 ^ { 4 }$ for the companion white dwarf). With timing residuals for the pulsar at the level of a microsecond, corresponding to errors in $\delta r$ of order $0 . 3 \ \mathrm { k m }$ , the bound on $\eta _ { N }$ could potentially be improved by three orders of magnitude. This estimate is consistent with results of a simulation by Shao (2016).1

However, because neutron stars involve strong gravity, post-Newtonian theory does not necessarily give a good approximation to the consequences of SEP violations, so this discussion of WBMSPs and the pulsar triple system should be regarded as only qualitative. In Chapter 10, we will introduce a framework for treating the post-Newtonian motion of systems containing compact bodies (neutron stars and and black holes).

# 8.2 Preferred Frames and Locations: Orbits

There are a number of observable effects of a preferred-frame and preferred-location type in the orbital motions of bodies governed by the PPN $N .$ -body equation of motion (6.45). To determine these effects, we consider a two-body system whose barycenter moves relative to the universe rest frame with velocity $\pmb { w }$ , and that resides in the gravitational potential $U _ { \mathrm { e x t } }$ of a distant body (the galaxy will prove to be the dominant such body). In the $N .$ - body equations of motion (6.45), we will ignore all the self-acceleration terms except the term in Eq. (6.46a) that depends on $\alpha _ { 3 }$ and $\pmb { w }$ . We will also ignore the Newtonian acceleration, the Nordtvedt terms, and all the post-Newtonian terms that were included in the classical perihelion-shift calculation. Thus, from Eqs. (6.46a), (6.46c), and (6.50) we have the additional accelerations

$$
\begin{array} { l } { { \displaystyle \delta a _ { 1 } = - \frac { 1 } { 3 } \alpha _ { 3 } \frac { \Omega _ { 1 } } { m _ { 1 } } ( w + \nu _ { 1 } ) \times \omega _ { 1 } + \frac { m _ { 2 } n } { r ^ { 2 } } \bigg [ \big ( 4 \beta + 2 \gamma - 1 - \zeta _ { 2 } - 3 \xi \big ) \frac { m _ { G } } { r _ { G } } } } \\ { { \displaystyle \quad \quad + \frac { 1 } { 2 } ( \alpha _ { 1 } - \alpha _ { 2 } - \alpha _ { 3 } ) w ^ { 2 } + \frac { 1 } { 2 } \alpha _ { 1 } w \cdot \nu _ { 1 } + \frac { 1 } { 2 } ( \alpha _ { 1 } - 2 \alpha _ { 2 } - 2 \alpha _ { 3 } ) w \cdot \nu _ { 2 } } } \\ { { \displaystyle \quad \quad + \frac { 3 } { 2 } \alpha _ { 2 } ( w \cdot n ) ^ { 2 } + 3 \alpha _ { 2 } ( w \cdot n ) ( \nu _ { 2 } \cdot n ) \bigg ] } } \\ { { \displaystyle \quad \quad + \xi \frac { m _ { 2 } } { r ^ { 2 } } \frac { m _ { G } } { r _ { G } } \big [ 2 n _ { G } ( n _ { G } \cdot n ) - 3 n ( n _ { G } \cdot n ) ^ { 2 } \big ] - \alpha _ { 2 } \frac { m _ { 2 } } { r ^ { 2 } } ( n \cdot w ) \nu _ { 2 } } } \\ { { \displaystyle \quad \quad - \frac { 1 } { 2 } \frac { m _ { 2 } } { r ^ { 2 } } n \cdot [ \alpha _ { 1 } \nu _ { 1 } - ( \alpha _ { 1 } - 2 \alpha _ { 2 } ) \nu _ { 2 } + 2 \alpha _ { 2 } w ] w } , } \\ { { \displaystyle a _ { 2 } = \{ 1 \ + 2 ; n \cdot \nu - n \} , } } \end{array}
$$

where ${ \pmb n } \equiv { \pmb x } _ { 1 2 } / r$ , $r _ { G } ~ \equiv ~ | { \pmb x } _ { 1 G } |$ , and ${ \pmb { n } } _ { G } ~ \equiv ~ { \pmb { x } } _ { 1 G } / r _ { 1 G }$ . In obtaining Eq. (8.27), we have ignored terms of order $m _ { G } r / r _ { G } ^ { 2 }$ , $m _ { G } r ^ { 2 } / r _ { G } ^ { 3 }$ , and so on. The first two terms inside the braces in Eq. (8.27) are constant, therefore they can simply be absorbed into the Newtonian acceleration by redefining the gravitational constant (they are related to the constant corrections to $G _ { \mathrm { L } }$ in Eq. (6.100)).

We will defer a discussion of the term proportional to $\alpha _ { 3 } \Omega _ { 1 } / m _ { 1 } ( \pmb { w } + \pmb { v } _ { 1 } ) \times \pmb { \omega } _ { 1 }$ to later in this section.

The relative acceleration $\pmb { a } \equiv \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ is given by

$$
\begin{array}{c} \begin{array}{c} \begin{array} { l } { { \displaystyle { \vphantom { \bigg ( } } } } \\ { { \displaystyle { \vphantom { \bigg ( } } } } \\ { { \displaystyle { \vphantom { \bigg [ } } } } \\ { { \displaystyle { \vphantom { \bigg [ } } } } \\ { { \displaystyle { \vphantom { \bigg [ } } } } \end{array}   \\ { { \quad \mathrm {  ~ \Gamma ~ } } } \\ { { \displaystyle { \vphantom { \bigg [ } } } } \\ { { \mathrm {  { \quad \Gamma ~ } } } } \end{array} \left[ \frac { 1 } { 2 } \alpha _ { 1 } \Delta w \cdot \nu + \frac { 3 } { 2 } \alpha _ { 2 } ( \pmb { w } \cdot \pmb { n } ) ^ { 2 } \right] - \frac { m x } { r ^ { 3 } } \cdot \left[ \frac { 1 } { 2 } \alpha _ { 1 } \Delta \pmb { \nu } + \alpha _ { 2 } \pmb { w } \right] w  \\ { { \mathrm {  ~ \Gamma ~ } } } \\ { { \displaystyle { \vphantom { \bigg [ } } } } \\ { { \displaystyle { \vphantom { \bigg [ } } } } \end{array}
$$

where we have made use of Eqs. (6.67) and (6.68).

Following the method outlined in Section 6.4.2, we calculate the secular changes in the orbit elements resulting from these perturbations. Using Eq. (6.73), we define

$$
\begin{array} { r l } & { { \pmb e } _ { \mathrm { P } } \equiv { \pmb n } | _ { \phi = \omega } = { \pmb e } _ { \Omega } \cos \omega + { \pmb e } _ { \perp } \sin \omega , } \\ & { { \pmb e } _ { \mathrm { Q } } \equiv { \pmb \lambda } | _ { \phi = \omega } = - { \pmb e } _ { \Omega } \sin \omega + { \pmb e } _ { \perp } \cos \omega , } \\ & { \hat { \pmb h } \equiv { \pmb e } _ { \mathrm { P } } \times { \pmb e } _ { \mathrm { Q } } = { \pmb e } _ { \Omega } \times { \pmb e } _ { \perp } , } \end{array}
$$

where $e _ { \mathrm { P } }$ is a unit vector pointing toward the pericenter (it is the Runge-Lenz vector divided by the orbital eccentricity) and ${ \pmb e } _ { \mathrm { Q } } = \hat { \pmb h } \times { \pmb e } _ { \mathrm { P } }$ ; $e _ { \Omega }$ is a unit vector pointing along the ascending node (see Figure 6.1), and $\pmb { e } _ { \perp } = \hat { \pmb { h } } \times \pmb { e } _ { \Omega }$ . For any vector $\pmb { A }$ , we then define components $A _ { \mathrm { P } }$ , $A _ { \mathrm { Q } } , A _ { \mathrm { h } } , A _ { \Omega }$ , and $A _ { \perp }$ accordingly.

The secular changes in the orbit elements are then given by

$$
\begin{array} { r l } & { \Delta = - 0 , } \\ & { \quad \Delta = - \omega _ { 0 , 1 } } \\ & { \quad - \omega _ { 0 , 2 } \Delta \Bigg ( \frac { m } { \omega _ { 0 } } \Bigg ) ^ { 1 / 2 } \quad \omega _ { 0 } \Bigg \{ 1 - \omega _ { 0 } ^ { 2 } \Bigg \} \epsilon ( \epsilon ) + 2 \omega _ { 0 , 2 } \omega _ { 0 , 0 } \epsilon \frac { P ( \epsilon ) } { \sqrt { 1 - \epsilon } } - \omega _ { 0 } ^ { 2 } \kappa ( \epsilon ) } \\ & { \quad \quad \quad - 4 \epsilon \frac { m \epsilon } { P _ { 0 } \omega _ { 0 } } \epsilon \omega _ { 0 } \omega _ { 0 } \omega _ { 1 } - \omega _ { 0 } ^ { 2 } \kappa ( \epsilon ) P _ { 1 } ^ { 2 } , } \\ & { \quad \quad \quad \Delta = - \omega _ { 1 } \Delta \Bigg ( \frac { m } { P _ { 0 } } \Bigg ) ^ { 1 / 2 } \quad \eta _ { 0 } \Bigg \{ 1 - \frac { \omega _ { 0 } ^ { 2 } } { \epsilon } \Bigg \} \epsilon \frac { \partial ^ { 2 } \kappa ( P ) } { \partial x _ { 0 } } , } \\ & { \quad \quad \quad \quad - \tau \alpha _ { 1 } \Delta \Bigg ( \frac { m } { P _ { 0 } } \Bigg ) ^ { 1 / 2 } \quad \eta _ { 0 } \Bigg \{ 1 - \frac { \omega _ { 0 } ^ { 2 } } { \epsilon } \Bigg \} \epsilon \frac { \partial ^ { 2 } \kappa ( P ) } { \partial x _ { 0 } } , } \\ & { \quad \quad \quad \quad - 2 \epsilon \frac { m \epsilon } { P _ { 0 } \omega _ { 0 } } \epsilon \frac { \partial ^ { 2 } \kappa ( P ) } { \partial x _ { 0 } } , } \\ & { \quad \quad \quad \quad \quad - \Delta \epsilon - \omega _ { 1 } \Delta \Bigg ( \frac { m } { P _ { 0 } } \Bigg ) ^ { 1 / 2 } \omega _ { 0 , 0 } \Delta ( \epsilon ) P _ { 0 } ^ { 2 } \epsilon - 2 \omega _ { 0 } \omega _ { 2 } \omega _ { 1 } \eta _ { 0 } \frac { P _ { 0 } ( \epsilon ) } { \sqrt { 1 - \epsilon } } } \\ & { \quad \quad \quad - 4 \epsilon \frac { m \epsilon } { P _ { 0 } \omega _ { 0 } } \epsilon \frac { \partial ^ { 2 } \kappa ( P ) } { \partial x _ { 0 } } , } \\ &  \quad \quad \quad \quad - 4 \epsilon \frac { m \epsilon } { P _ { 0 } \omega _ { 0 } } \epsilon \frac  \partial ^ { 2 } \end{array}
$$

where

$$
F ( e ) \equiv { \frac { 1 } { 1 + \sqrt { 1 - e ^ { 2 } } } } ,
$$

and for any vector $\pmb { A }$ ,

$$
\begin{array} { r } { A _ { \mathrm { R } } \equiv A _ { \mathrm { P } } \cos { \left( \omega \right) } - A _ { \mathrm { Q } } \sin { \left( \omega \right) } \sqrt { 1 - e ^ { 2 } } , } \\ { A _ { \mathrm { S } } \equiv A _ { \mathrm { P } } \sin { \left( \omega \right) } + A _ { \mathrm { Q } } \cos { \left( \omega \right) } \sqrt { 1 - e ^ { 2 } } . } \end{array}
$$

In the small-eccentricity limit, to first order in $e$ , these results simplify to

$$
\begin{array} { l } { \Delta a = 0 , } \\ { \Delta e = - \displaystyle \frac { \pi } { 2 } \alpha _ { 1 } \Delta \left( \displaystyle \frac { m } { a } \right) ^ { 1 / 2 } w _ { \mathrm { P } } + \displaystyle \frac { \pi } { 2 } \alpha _ { 2 } w _ { \mathrm { P } } w _ { \mathrm { Q } } e - \pi \xi \displaystyle \frac { m _ { G } } { r _ { G } } n _ { G \mathrm { P } } n _ { G \mathrm { Q } } e , } \\ { \Delta \varpi = - \displaystyle \frac { \pi } { 2 } \alpha _ { 1 } \Delta \left( \displaystyle \frac { m } { a } \right) ^ { 1 / 2 } \displaystyle \frac { w _ { \mathrm { Q } } } { e } - \displaystyle \frac { \pi } { 4 } \alpha _ { 2 } \left( w _ { \mathrm { P } } ^ { 2 } - w _ { \mathrm { Q } } ^ { 2 } \right) + \displaystyle \frac { \pi } { 2 } \xi \displaystyle \frac { m _ { G } } { r _ { G } } \left( n _ { G \mathrm { P } } ^ { 2 } - n _ { G \mathrm { Q } } ^ { 2 } \right) , } \end{array}
$$

$$
\begin{array} { c } { { \displaystyle \Delta \iota = \frac { \pi } { 2 } \alpha _ { 1 } \Delta \left( \frac { m } { a } \right) ^ { 1 / 2 } w _ { \mathrm { h } } e \sin \left( \omega \right) - \pi \alpha _ { 2 } w _ { \mathrm { h } } w _ { \Omega } + 2 \pi \xi \frac { m _ { G } } { r _ { G } } n _ { G \mathrm { h } } n _ { G \mathrm { \tiny ~ , } } } } \\ { { \displaystyle \sin \iota \Delta \Omega = - \frac { \pi } { 2 } \alpha _ { 1 } \Delta \left( \frac { m } { a } \right) ^ { 1 / 2 } w _ { \mathrm { h } } e \cos \left( \omega \right) - \pi \alpha _ { 2 } w _ { \mathrm { h } } w _ { \bot } + 2 \pi \xi \frac { m _ { G } } { r _ { G } } n _ { G \mathrm { h } } n _ { G \bot } \mathrm { , } } } \end{array}
$$

where, for $e = 0$ , Eq. (8.32) implies that $A _ { \mathrm { R } } = A _ { \Omega }$ , and $A _ { \mathrm { S } } = A _ { \perp }$ .

It is tempting to interpret these secular changes as implying linearly growing values of the orbital elements. However, the expressions in Eq. (8.33) depend on $\omega$ , both from explicit $\omega$ dependence, and via the $\mathrm { P }$ and Q components of $\pmb { w }$ and ${ \pmb { n } } _ { G }$ . The pericenter angle is actually advancing at an average rate $d \omega / d \phi \equiv \omega ^ { \prime } \simeq 3 m / p$ (see Eq. (6.78)), which we anticipate is much larger than the preferred-frame effects shown in Eq. (8.33c) – the goal is to set strong upper bounds on such effects. Thus the variations in the orbit elements will be modulated on a pericenter precession timescale and could even change sign. So in order to find the proper long-term evolution of the elements, we define, for a given element $X _ { a }$ , $d X _ { a } / d \phi \equiv \Delta X _ { a } / 2 \pi$ , insert $\omega = \omega _ { 0 } + \omega ^ { \prime } \phi$ in the right-hand sides (including in the $\mathrm { P }$ and Q components of various vectors) and integrate with respect to $\phi$ . Inserting the resulting integrals for $e$ and $\varpi$ , into the expression

$$
r = a [ 1 - e \cos \left( \phi - \omega \right) + O ( e ^ { 2 } ) ] ,
$$

and expanding to first order in the preferred-frame perturbations, we obtain

$$
\begin{array} { r } { \frac { r } { a } = 1 - e _ { 0 } \cos \left( \phi - \omega _ { 0 } - \omega ^ { \prime } \phi \right) - \frac { 1 } { 4 } \alpha _ { 1 } \Delta \left( \frac { m } { a } \right) ^ { 1 / 2 } \frac { w } { \omega ^ { \prime } } \left( \hat { w } _ { \perp } \cos \phi - \hat { w } _ { \Omega } \sin \phi \right) } \\ { + \frac { e _ { 0 } } { 4 } \alpha _ { 2 } w ^ { 2 } \frac { \sin \omega ^ { \prime } \phi } { \omega ^ { \prime } } \left[ 2 \hat { w } _ { \Omega } \hat { w } _ { \perp } \cos \left( \phi + \omega _ { 0 } \right) + \left( \hat { w } _ { \perp } ^ { 2 } - \hat { w } _ { \Omega } ^ { 2 } \right) \sin \left( \phi + \omega _ { 0 } \right) \right] } \\ { + \frac { e _ { 0 } } { 4 } \xi \frac { m _ { G } } { r _ { G } } \frac { \sin \omega ^ { \prime } \phi } { \omega ^ { \prime } } \left[ 2 n _ { G \Omega } n _ { G \perp } \cos \left( \phi + \omega _ { 0 } \right) + \left( n _ { G \perp } ^ { 2 } - n _ { G \Omega } ^ { 2 } \right) \sin \left( \phi + \omega _ { 0 } \right) \right] . } \end{array}
$$

The first term in Eq. (8.35) is the normal contribution to $r / a$ resulting from the small eccentricity, with the pericenter advancing at a rate $\omega ^ { \prime }$ . The second term is a forced eccentricity of the orbit, with an amplitude proportional to $( \hat { w } _ { \bot } ^ { 2 } + \hat { w } _ { \Omega } ^ { 2 } ) ^ { 1 / 2 } = ( 1 - \hat { w } _ { h } ^ { 2 } ) ^ { 1 / 2 } \equiv$ $\sin \psi$ , where $\psi$ is the angle between the orbital angular momentum $\hat { \pmb h }$ and the velocity $\mathbfcal { w }$ relative to the preferred frame, and a phase given by $\tan ^ { - 1 } \left( - \hat { w } _ { \Omega } / \hat { w } _ { \perp } \right)$ (Damour and Esposito-Farese, 1992b). This effect is present even in the limit \` $e _ { 0 } \to 0$ . The final terms are also polarizations of the orbit, proportional to $e _ { 0 }$ , with an amplitude modulated by the factor $\sin \omega ^ { \prime } \phi / \omega ^ { \prime }$ . However, they vanish in the limit $e _ { 0 } \to 0$ .

The other important effect of the preferred-frame perturbations is to cause the orbital angular momentum to precess. Since $\begin{array} { r } { \hat { \boldsymbol h } = \sin \iota \big ( \sin \Omega \boldsymbol e _ { X } - \cos \Omega \boldsymbol e _ { Y } \big ) + \cos \iota e _ { Z } , } \end{array}$ , variations in $\hat { h }$ are given by

$$
\Delta \hat { \pmb { h } } = \sin \iota \Delta \Omega \pmb { e } _ { \Omega } - \Delta \iota \pmb { e } _ { \perp } .
$$

Inserting Eqs. (8.33d) and (8.33e), and noting that $e _ { \Omega } \cos \omega + e _ { \perp } \sin \omega = e _ { \mathrm { P } }$ and that $A _ { \perp } \pm e _ { \Omega } - A _ { \Omega } e _ { \perp } = A \times \hat { h }$ , we obtain

$$
\Delta \hat { h } = - \frac { \pi } { 2 } \alpha _ { 1 } \Delta \left( \frac { m } { a } \right) ^ { 1 / 2 } w _ { \mathrm { h } } e e _ { \mathrm { P } } - \pi \alpha _ { 2 } w _ { h } ( \pmb { w } \times \hat { \pmb { h } } ) + 2 \pi \xi \frac { m _ { G } } { r _ { G } } n _ { G \mathrm { h } } ( \pmb { n } _ { G } \times \hat { \pmb { h } } ) ,
$$

leading to a precession of the angular momentum vector $\pmb { h }$ . Because of the variation of $e$ in Eq. (8.33b), the magnitude of the angular momentum $h = { \sqrt { m a ( 1 - e ^ { 2 } ) } }$ will also change. The first two terms, dependent on the preferred-frame parameters $\alpha _ { 1 }$ and $\alpha _ { 2 }$ do not come as a surprise. We saw in Section 4.4 that, in semi-conservative theories of gravity, a system’s total angular momentum is conserved only if the system is at rest in the preferred frame; for moving systems, angular momentum need not be conserved. The third term may seem surprising, since $\xi$ can be non-zero even in a fully conservative theory, where total angular momentum is conserved. In this case, because of the distant mass $m _ { G }$ , the binary system is not a truly isolated system, and presumably there is a compensating change in the angular momentum of the orbit of the binary around the distant mass that conserves the total angular momentum. Changes in the angular momentum of a binary system induced by tidal interactions with a third body are well-known (Kozai-Lidov effects); here the effect is induced by a post-Newtonian violation of SEP.

We turn finally to the self-acceleration term in Eq. (8.27) proportional to $\alpha _ { 3 }$ . We assume that only body 1 possesses enough self-gravitational binding energy and spin to generate such a term, so that the relative acceleration is given by

$$
\pmb { a } = - \frac 1 3 \alpha _ { 3 } \frac { \Omega _ { 1 } } { m _ { 1 } } \pmb { w } \times \omega _ { 1 } ,
$$

where we drop the contribution from the orbital velocity $\nu _ { 1 }$ . Calculating the secular changes in the orbit elements, we obtain

$$
\begin{array} { r l } & { \Delta a = 0 , } \\ & { \Delta e = - \pi \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { m } B _ { 0 } , } \\ & { \Delta \varpi = \pi \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { e m } B _ { \mathrm { P } } , } \\ & { \Delta t = \pi \frac { a ^ { 2 } e } { m \sqrt { 1 - e ^ { 2 } } } B _ { \mathrm { h } } \cos \omega , } \\ & { \sin \iota \Delta \Omega = \pi \frac { a ^ { 2 } e } { m \sqrt { 1 - e ^ { 2 } } } B _ { \mathrm { h } } \sin \omega , } \end{array}
$$

where ${ \pmb B } \equiv \alpha _ { 3 } ( \Omega _ { 1 } / m _ { 1 } ) ( { \pmb w } \times { \pmb \omega } _ { 1 } )$ . As before, we integrate with respect to $\phi$ including the dominant pericenter precession proportional to $\omega ^ { \prime }$ , assume that $e$ is small, and substitute the results for $e$ and $\varpi$ into Eq. (8.34) to obtain

$$
\begin{array} { l } { \displaystyle \frac { r } { a } = 1 - e _ { 0 } \cos { ( \phi - \omega _ { 0 } - \omega ^ { \prime } \phi ) } } \\ { \displaystyle \qquad + \frac { 1 } { 2 } \alpha _ { 3 } \frac { a ^ { 2 } } { m \omega ^ { \prime } } \frac { \Omega _ { 1 } } { m _ { 1 } } [ ( \pmb { w } \times \omega _ { 1 } ) \cdot \pmb { e } _ { \perp } \sin \phi + ( \pmb { w } \times \omega _ { 1 } ) \cdot \pmb { e } _ { \Omega } \cos \phi ) ] . } \end{array}
$$

Again we recognize a forced eccentricity, with amplitude proportional to ${ \big | } w \times \omega _ { 1 } { \big | } \sin \psi$ where $\psi$ is the angle between $\hat { h }$ and $w \times \omega _ { 1 }$ . If the body’s spin vector $\omega _ { 1 }$ is perpendicular to the orbital plane, then $\psi = 9 0 ^ { \circ }$ .

# 8.3 Preferred Frames and Locations: Structure of Massive Bodies

# 8.3.1 GL and distortions of massive bodies

In Section 6.6, we found that some metric theories of gravity predict preferred-frame and preferred-location effects in the locally measured gravitational constant $G _ { \mathrm { L } }$ as measured by means of a Cavendish experiment:

$$
\begin{array} { c } { { G _ { \mathrm { L } } = 1 - \left[ 4 \beta - \gamma - 3 - \zeta _ { 2 } - \xi \left( 3 + \chi \right) \right] \displaystyle \frac { m _ { G } } { r _ { G } } - \frac 1 2 \left[ \alpha _ { 1 } - \alpha _ { 3 } - \alpha _ { 2 } \left( 1 - \chi \right) \right] w ^ { 2 } } } \\ { { - \displaystyle \frac 1 2 \alpha _ { 2 } \left( 1 - 3 \chi \right) \left( \pmb { w } \cdot \pmb { n } \right) ^ { 2 } + \xi \left( 1 - 3 \chi \right) \displaystyle \frac { m _ { G } } { r _ { G } } ( \pmb { n } _ { G } \cdot \pmb { n } ) ^ { 2 } , } } \end{array}
$$

where $\pmb { w }$ is the velocity of the body relative to the preferred frame, $m _ { G } , r _ { G }$ and ${ \pmb { n } } _ { G }$ are the mass, distance, and unit vector for the external body (summed over all external masses, if necessary), and

$$
\chi \equiv { \frac { I } { m r ^ { 2 } } } ,
$$

where $m$ and $I$ are the mass and spherical moment of inertia of the source body, and $r$ and $\pmb { n }$ are the distance and unit vector between the two masses being used to measure $G _ { \mathrm { L } }$ .

These effects represent violations of SEP. Unfortunately, present-day laboratory measurements of $G$ are only accurate to parts in $1 0 ^ { 4 }$ (Mohr and Taylor, 2005), and so are unlikely to shed light on the post-Newtonian corrections to $G _ { \mathrm { L } }$ shown in Eq. (8.41), which are at levels of $1 0 ^ { - 6 }$ and smaller in the solar system. However, such variations and anisotropies in $G _ { \mathrm { L } }$ should affect the structure of self-gravitating bodies such as the Earth, in a manner that is analogous to the tidal effects of the Sun and Moon.

The tidal forces caused an external body induce variations in the local acceleration of gravity $g$ on the surface of a chosen body. The measured variations are affected not only by the direct tidal accelerations, but also by the displacement of the surface relative to the center of the body and by the redistribution of mass inside the body. One can show that the variations in $g$ are then related to the external driving variations by a numerical factor, a combination of so-called “Love numbers,” which depend on the detailed structure of the body (see section 2.4 of PW for a pedagogical discussion). For the Earth, the numerical factor turns out to be approximately 1.16. These solid Earth tides are to be distinguished from ocean tides, which are much more complex.

On the Earth, variations in $g$ are measured routinely and to very high precision by global arrays of gravimeters, as a means to learn about the structure of the Earth via measurement of the Love numbers. We wish to use such measurements to set limits on the PPN parameters that appear in Eq. (8.41). We will assume that, for the Earth, we can approximate

$$
\frac { \Delta g } { g } = 1 . 1 6 \frac { \Delta G _ { \mathrm { L } } } { G _ { \mathrm { L } } } .
$$

A more accurate calculation of $\Delta g / g$ would consider the PPN equation of hydrostatic equilibrium obtained from the static limit of the PPN equation of hydrodynamics (6.25), with perturbations induced by the various preferred-frame and preferred-location terms, and then would proceed with the same kind of perturbation calculation that is done for tidal perturbations, as detailed in PW, section 2.4. In the Earth’s interior the perturbing force generated by the variations in $G _ { \mathrm { L } }$ is proportional to $\rho ^ { * } \nabla U$ , whereas the tidal perturbing force is proportional to the distance from the center of the Earth. If the Earth’s density were uniform, then $\rho ^ { * } \boldsymbol { \nabla } U$ would be proportional to $r$ , and the Love numbers would be the same as in the Newtonian tidal case. However, in Newtonian tidal theory, the Love number factor for gravimeter measurements (1.16), is not very sensitive $\pm 5$ percent) to variations in the model for the Earth, thus we do not expect it to be sensitive to a different disturbing force law.

Consider the first post-Newtonian term in Eq. (8.41). Because of the Earth’s eccentric orbital motion, the external potential produced by the Sun varies yearly on Earth by only a part in $1 0 ^ { 1 0 }$ , too small to be detected with confidence by Earth-bound gravimeters. The time-varying effects of other bodies (planets, the galaxy) are even smaller. The second term is proportional to $w ^ { 2 } = w _ { 0 } ^ { 2 } + 2 w _ { 0 } \cdot \nu + \nu ^ { 2 }$ , where $w _ { 0 } \simeq 1 0 ^ { - 3 }$ is the velocity of the solar-system barycenter relative to the preferred frame and $\nu \simeq 1 0 ^ { - 4 }$ is the Earth’s orbital velocity. The first term is constant and the third varies by only a part in $1 0 ^ { 1 0 }$ , but the middle term varies with the full amplitude $\propto ~ w _ { 0 } \nu$ because of the orbital motion of the Earth. Because of the rotation of the Earth (varying $\pmb { n }$ ) the two anisotropic terms in Eq. (8.41) will generate variations in $g$ at various harmonics of the Earth’s rotation rate. In addition, $( w \cdot n ) ^ { 2 }$ will vary because of the orbital contribution to $\pmb { w }$ . Finally, the preferred-location term should include all gravitating matter that is not part of the cosmological background used to establish the asymptotically flat PPN coordinate system. Therefore, it should include the Sun, planets, stars, the Galaxy, and so on, at least out to scales where the matter distribution is sufficiently isotropic so as to wash out the variation with changing $\pmb { n }$ . In this case, the factor $m _ { G } / r _ { G }$ is dominated by our galaxy $( \sim 5 \times 1 0 ^ { - 7 } )$ followed by the Sun $( \sim 1 0 ^ { - 8 } )$ .

In order to illustrate how the variations in $G _ { \mathrm { L } }$ would appear in practice in a time series of gravimeter readings, we will select the variations with largest amplitude in Eq. (8.41), and write

$$
\begin{array} { l } { \displaystyle \frac { \Delta G _ { \mathrm { L } } } { G _ { \mathrm { L } } } = - \left( \alpha _ { 1 } - \alpha _ { 3 } - \frac 1 2 \alpha _ { 1 } \right) { \pmb w _ { 0 } \cdot \pmb \nu } } \\ { \displaystyle \qquad + \frac 1 4 \alpha _ { 2 } ( { \pmb w _ { 0 } \cdot \pmb n } ) ^ { 2 } - \frac 1 2 \xi \frac { m _ { G } } { r _ { G } } ( { \pmb n } _ { G } \cdot { \pmb n } ) ^ { 2 } , } \end{array}
$$

where we have used the fact that $\chi \simeq 1 / 2$ for the Earth, and where here the subscript $G$ refers to the galaxy. We work in geocentric ecliptic coordinates, and assume a circular Earth orbit, with the Earth at vernal equinox at $t = 0$ . Then

$$
\begin{array} { r } { \begin{array} { r } { \pmb { \nu } = \nu \left( \sin \omega t \pmb { e } _ { x } - \cos \omega t \pmb { e } _ { y } \right) , } \\ { \hat { \pmb { w } } _ { 0 } = \cos \beta _ { w } \left( \cos \lambda _ { w } \pmb { e } _ { x } + \sin \lambda _ { w } \pmb { e } _ { y } \right) + \sin \beta _ { w } \pmb { e } _ { z } , } \\ { \pmb { n } _ { G } = \cos \beta _ { G } \left( \cos \lambda _ { G } \pmb { e } _ { x } + \sin \lambda _ { G } \pmb { e } _ { y } \right) + \sin \beta _ { G } \pmb { e } _ { z } . } \end{array} } \end{array}
$$

The latter two equations define the ecliptic coordinates $\left( \lambda _ { w } , \beta _ { w } \right)$ and $\left( \lambda _ { G } , \beta _ { G } \right)$ of the solar system’s velocity and of the galactic center, respectively. For a gravimeter stationed at Earth latitude $L$ ,

$$
\begin{array} { r } { n = \cos L \cos \left( \Omega t - \epsilon \right) e _ { x } + \left[ \cos L \sin \left( \Omega t - \epsilon \right) \cos \theta + \sin L \sin \theta \right] e _ { y } } \\ { - \left[ \cos L \sin \left( \Omega t - \epsilon \right) \sin \theta - \sin L \cos \theta \right] e _ { z } , } \end{array}
$$

where $\epsilon$ is related to the longitude of the gravimeter on Earth, and $\theta$ is the “tilt” $( 2 3 . 5 ^ { \circ } )$ of the Earth relative to the ecliptic plane. Then the three amplitudes in Eq. (8.44) can be expressed as

$$
\begin{array} { c } { { w _ { 0 } \cdot \nu = w _ { 0 } \nu \cos \beta _ { w } \sin \left( \omega t - \lambda _ { w } \right) , } } \\ { { \ } } \\ { { \displaystyle \left( w _ { 0 } \cdot n \right) ^ { 2 } = \displaystyle \frac { 1 } { 2 } w _ { 0 } ^ { 2 } \Big [ \cos ^ { 2 } \delta _ { w } \cos ^ { 2 } L + 2 \sin ^ { 2 } \delta _ { w } \sin ^ { 2 } L + \sin 2 \delta _ { w } \sin 2 L \cos \left( \Omega t - \epsilon - \alpha _ { w } \right) } } \\ { { \displaystyle \qquad + \cos ^ { 2 } \delta _ { w } \cos ^ { 2 } L \cos 2 \left( \Omega t - \epsilon - \alpha _ { w } \right) \Big ] , } } \\ { { \displaystyle \left( n _ { G } \cdot n \right) ^ { 2 } = \displaystyle \frac { 1 } { 2 } \Big [ \cos ^ { 2 } \delta _ { G } \cos ^ { 2 } L + 2 \sin ^ { 2 } \delta _ { G } \sin ^ { 2 } L + \sin 2 \delta _ { G } \sin 2 L \cos \left( \Omega t - \epsilon - \alpha _ { G } \right) } } \\ { { \displaystyle \qquad + \cos ^ { 2 } \delta _ { G } \cos ^ { 2 } L \cos 2 \left( \Omega t - \epsilon - \alpha _ { G } \right) \Big ] , } } \end{array}
$$

where $( \alpha _ { w } , \delta _ { w } )$ and $( \alpha _ { G } , \delta _ { G } )$ are the Earth-oriented equatorial coordinates. The ecliptic and equatorial coordinates are related by

$$
\begin{array} { c } { \sin \delta = \sin \beta \cos \theta + \cos \beta \sin \theta \sin \lambda , } \\ { \cos \delta \cos \alpha = \cos \beta \cos \lambda , } \\ { \cos \delta \sin \alpha = - \sin \beta \sin \theta + \cos \beta \cos \theta \sin \lambda . } \end{array}
$$

The two anisotropic terms produce variations in $\Delta g / g$ at frequencies $2 \Omega$ and $\Omega$ , corresponding to periods of half a sidereal day (“semidiurnal”) and a sidereal day (“diurnal”), respectively. The dominant Newtonian tides occur at frequencies $2 ( \Omega - \omega _ { \mathbb { C } } { \mathrm { ~ ) ~ } }$ and $2 ( \Omega - \omega _ { \oplus } )$ , corresponding to half a lunar and solar day respectively. In fact, because of factors such as the tilt of the lunar orbit relative to the ecliptic, there are numerous sidebands of the diurnal and semidiurnal tides at $\pm \omega _ { \oplus }$ , $\pm 2 \omega _ { \oplus } , \pm \omega _ { \mathbb { Q } }$ and $\pm 2 \omega _ { \mathbb { ( } }$ . Similarly, if we had included the orbital contributions to $( w \cdot n ) ^ { 2 }$ and the solar contribution to the preferred-location term, there would be a corresponding array of sidebands in the PPN signal. Thus by analyzing gravimeter data taken over long periods of time, and incorporating Earth models that predict the Newtonian tidal amplitude to relatively high accuracy, one can endeavor to place bounds on $\alpha _ { 2 }$ and $\xi$ . We will discuss specific experiments and the bounds they provide in Section 8.4.

The $w _ { 0 } \cdot \nu$ term produces an annual variation in the size of $G _ { \mathrm { L } }$ . Such variations would cause the Earth to expand and shrink slightly, changing its moment of inertia, and thereby changing its rotation rate on an annual basis. In Section 8.4, we will discuss the bounds placed by comparing such variations with the observations.

# 8.3.2 Precession of the spin axis of massive bodies

Another effect induced by preferred-frame and preferred-location violations of SEP is an apparent failure of conservation of angular momentum, leading to a precession of the axis of a rotating massive body. We have already seen an example of this in the precession of the angular momentum of a binary system in Section 8.2, Eq. (8.37). Here we will derive the analogous effect for a rotating, self-gravitating body at rest in the PPN coordinate frame. In the PPN equation of hydrodynamics (6.25), we split the various potentials $U , \Phi _ { 2 } , \Phi _ { W }$ , and so on into an internal part and a part due to an external body, keeping only terms proportional to $m _ { G } / r _ { G }$ . We also include the preferred-frame terms. Keeping only such terms along with the Newtonian Euler equation, we obtain

$$
\begin{array} { r l } & { \rho ^ { * } \cfrac { d \nu ^ { j } } { d t } = \rho ^ { * } U _ { j } \bigg [ 1 - \frac { m _ { G } } { r _ { G } } \left( 4 \beta + 2 \gamma - 1 - \zeta _ { 2 } - 4 \xi \right) + \frac { 1 } { 2 } ( \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { 2 } \bigg ] } \\ & { \quad \quad \quad - \left[ 1 + ( 2 - \gamma ) \frac { m _ { G } } { r _ { G } } \right] p _ { j } - \rho ^ { * } X _ { j k m } \left[ \xi \frac { m _ { G } } { r _ { G } } n _ { G } ^ { k } n _ { G } ^ { m } - \frac { 1 } { 2 } \alpha _ { 2 } w ^ { k } w ^ { m } \right] } \\ & { \quad \quad \quad + \frac { 1 } { 2 } ( 2 \alpha _ { 3 } - \alpha _ { 1 } ) w ^ { k } V _ { k j } + \frac { 1 } { 2 } \alpha _ { 1 } \left[ w ^ { j } U _ { 0 } + 2 \hat { \nu } ^ { k } w ^ { [ j } U ^ { k ] } \right] - \alpha _ { 2 } w ^ { k } X _ { , 0 j k } , } \end{array}
$$

where $U , X ,$ and $V _ { k }$ are potentials generated by the rotating body, with $V _ { k }$ dependent on $\bar { \nu } ^ { k }$ , the velocity of the fluid relative to the center of mass. The coefficient of $m _ { G } / r _ { G }$ in the first line of this expression differs slightly from the corresponding term in Eq. (8.41) because here we work in PPN coordinates, whereas $G _ { \mathrm { L } }$ in Eq. (8.41) was defined using proper distances and times. We now wish to calculate the rate of change of the angular momentum tensor, $\begin{array} { r } { d J ^ { i j } / d t \equiv 2 \int \rho ^ { * } x ^ { [ i } ( d \nu ^ { j ] } / d t ) d ^ { 3 } x } \end{array}$ . We use the fact that terms such as $\int \rho ^ { * } x ^ { [ i } U ^ { j ] } d ^ { 3 } x$ or $f x ^ { [ i } p ^ { j ] } d ^ { 3 } x$ are already known to vanish in establishing the Newtonian conservation of angular momentum, and that quantities such as $\begin{array} { r l } { \int \rho ^ { * } x ^ { i } V _ { k } ^ { j } d ^ { 3 } x , \int \rho ^ { * } x ^ { i } \nu _ { k } U ^ { j } d ^ { 3 } x } \end{array}$ or $\int \rho ^ { * } x ^ { i } \dot { U } d ^ { 3 } x$ vanish because they contain odd numbers of spatial indices, and we make our standard assumption of reflection symmetric bodies. The only terms that survive are

$$
{ \frac { d J ^ { i j } } { d t } } = - \int \rho ^ { * } x ^ { [ i } X ^ { j ] k m } d ^ { 3 } x \left[ 2 \xi { \frac { m _ { G } } { r _ { G } } } n _ { G } ^ { k } n _ { G } ^ { m } - \alpha _ { 2 } w ^ { k } w ^ { m } \right] .
$$

Recalling that $\begin{array} { r } { X = \int \rho ^ { * } | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } } \end{array}$ , it is straightforward to show that

$$
\int \rho ^ { * } x ^ { [ i } X ^ { j ] k m } d ^ { 3 } x = \Omega ^ { k [ i } \delta ^ { j ] m } + \Omega ^ { m [ i } \delta ^ { j ] k } ,
$$

where $\Omega ^ { i j }$ is the self-gravitational energy tensor for the body. It satisfies the virial relation $2 { \cal T } ^ { i j } + \Omega ^ { i j } + { \cal P } \delta ^ { i j } = 0$ , where $P$ is the integral of the pressure, and $\mathcal { T } ^ { i j }$ is the kinetic energy tensor, given for a uniformly rotating body by

$$
{ \cal T } ^ { i j } = \frac { 1 } { 2 } \int \rho ^ { * } \nu ^ { i } \nu ^ { j } d ^ { 3 } x = \frac { 1 } { 2 } \epsilon ^ { i k m } \epsilon ^ { j p q } \omega ^ { k } \omega ^ { p } \int \rho ^ { * } x ^ { m } x ^ { q } d ^ { 3 } x .
$$

For a nearly spherical body, $\begin{array} { r } { \int \rho ^ { * } x ^ { m } x ^ { q } d ^ { 3 } x \simeq \frac { 1 } { 2 } \delta ^ { p q } I _ { e } } \end{array}$ , where $\begin{array} { r } { I _ { e } = \int \rho ^ { * } r ^ { 2 } \sin ^ { 2 } \theta d ^ { 3 } x } \end{array}$ is the moment of inertia about the rotation axis $e$ , and thus

$$
\mathcal { T } ^ { i j } = \frac { 1 } { 4 } I _ { e } \omega ^ { 2 } \left( \delta ^ { i j } - e ^ { i } e ^ { j } \right) .
$$

Pulling everything together and recalling that the angular momentum vector is given by $\begin{array} { r } { J ^ { k } = \frac { 1 } { 2 } \epsilon ^ { k i j } J ^ { i j } } \end{array}$ we find that the torque on the body is given by

$$
\frac { d \boldsymbol J } { d t } = - \frac { 1 } { 2 } I _ { e } \omega ^ { 2 } \left[ 2 \xi \frac { m _ { G } } { r _ { G } } \boldsymbol e \cdot \boldsymbol n _ { G } ( \boldsymbol e \times \boldsymbol n _ { G } ) - \alpha _ { 2 } \boldsymbol e \cdot \boldsymbol w ( \boldsymbol e \times \boldsymbol w ) \right] .
$$

This is completely equivalent to the change in orbital angular momentum shown in Eq. (8.37). There is no $\alpha _ { 1 }$ term in Eq. (8.54) because of our assumption of reflection symmetry for the body; this is equivalent to setting $e = 0$ (circular orbit) in Eq. (8.37).

# 8.4 Preferred Frames and Locations: Bounds on the PPN Parameters

Here we review the bounds that have been placed on the preferred-frame parameters $\alpha _ { 1 }$ , $\alpha _ { 2 }$ and $\alpha _ { 3 }$ and on the preferred-location or Whitehead parameter $\xi$ by observational searches for the effects described in Sections 8.2 and 8.3.

To be concrete, we must employ values for the velocity of the preferred frame and the galactic potential and their associated directions. In any theory of gravity with a preferred frame, it is natural to assume that the preferred frame is the rest frame of the overall mass distribution of the universe, as represented by the frame in which the cosmic microwave background (CMB) is isotropic. From the measured dipole anisotropy of the CMB, we know that the solar-system is moving with a speed $w _ { 0 } \simeq 3 7 0 \mathrm { k m } \mathrm { ~ s } ^ { - 1 } \simeq 1 . 2 \times 1 0 ^ { - 3 }$ . Table 8.2 shows the precise value along with the direction in galactic, ecliptic, and equatorial coordinates.

The galactic potential $m _ { G } / r _ { G }$ is less precise, but we can estimate it within a factor of a few. The solar system’s velocity within the galaxy is $2 3 0 \mathrm { k m / s }$ ; assuming that $\nu ^ { 2 } \sim m _ { G } / r _ { G }$ we can estimate $m _ { G } / r _ { G } \sim 5 \times 1 0 ^ { - 7 }$ . This assumes that the mass of the galaxy is more or less concentrated at the center, whereas we know that the bulk of the mass of the galaxy is in a roughly spherical halo of stars and dark matter, substantially larger in size than the visible Milky Way.

However it can be shown using a simple density model for the galaxy that the rough estimate we have adopted holds up within a factor of a few. First, we note that the important quantity $( m _ { G } / r _ { G } ) n _ { G } ^ { i } n _ { G } ^ { j }$ is a single-mass version of the potential tensor $U ^ { j } = \delta ^ { i j } U - X ^ { , i j }$ . For a spherically symmetric distribution of matter, $X$ is given by

$$
X = r m ( r ) + \frac { 4 \pi } { 3 r } \int _ { 0 } ^ { r } \rho ^ { \prime } r ^ { \prime 4 } d r ^ { \prime } + \frac { 4 \pi } { 3 } \int _ { r } ^ { \infty } \rho ^ { \prime } r ^ { \prime } ( r ^ { 2 } + 3 r ^ { \prime 2 } ) d r ^ { \prime } ,
$$

where $\rho$ is the mass density and $m ( r )$ is the mass inside radius $r$ . Then, for spherical symmetry,

$$
\begin{array} { l } { { \displaystyle X ^ { i j } = n ^ { i } n ^ { j } \frac { d ^ { 2 } X } { d r ^ { 2 } } - \frac { 1 } { r } \left( \delta ^ { i j } - n ^ { i } n ^ { j } \right) \frac { d X } { d r } } } \\ { { \displaystyle \quad = - n ^ { i } n ^ { j } \left[ \frac { m ( r ) } { r } - \frac { I ( r ) } { r ^ { 3 } } \right] + \delta ^ { i j } \left[ \frac { m ( r ) } { r } - \frac { I ( r ) } { 3 r ^ { 3 } } + \frac { 8 \pi r } { 3 } \int _ { r } ^ { \infty } \rho ^ { \prime } r ^ { \prime } d r ^ { \prime } \right] } , }  \end{array}
$$

where $I ( r )$ is the spherical moment of inertia inside radius $r$ . Since we are only interested in anisotropic effects, we will drop all terms proportional to $\delta ^ { i j }$ .

To compare with our rough estimate we consider a specific density distribution given by $4 \pi \rho = \alpha / r _ { c } ^ { 2 }$ , for $r < r _ { c }$ , and $4 \pi \rho = \alpha / r ^ { 2 }$ , for $r > r _ { c }$ , where $r _ { c }$ is a core radius meant to represent the mass of the inner part of the galaxy, and $\alpha$ is a parameter. The $1 / r ^ { 2 }$ density distribution is meant to model the dark matter halo, and to yield a flat rotation curve for the outer reaches of the Milky Way, in rough agreement with observations. By noting that a circular orbit in a spherical potential satisfies, $\nu ^ { 2 } / r = a _ { r } = m ( r ) / r ^ { 2 }$ , and considering the case $r > r _ { c }$ , we can fit $\alpha = \nu ^ { 2 } / ( 1 - 2 q / 3 )$ , where $q = r _ { c } / r$ , and find that

<table><tr><td colspan="3">Table 8.2 Parameters of the preferred frame velocity wo and the galactic potential at the solar system.</td></tr><tr><td>Galactic (l, b)</td><td>Ecliptic (入， β)</td><td>Equatorial (α, δ)</td></tr><tr><td>Velocity,368± 2 km s−1 (1.23 × 10-3)</td><td></td><td></td></tr><tr><td>Longitude 263°.85</td><td>171°.55</td><td>167°.85</td></tr><tr><td>Latitude 48°.25</td><td>-11°.13</td><td>-6°.88</td></tr><tr><td>Galactic potential ~ 5 × 10-7</td><td></td><td></td></tr><tr><td>Longitude 0°</td><td>266°.84</td><td>266° .41</td></tr><tr><td>Latitude 0°</td><td>-5°.54</td><td>-28°.94</td></tr></table>

$$
U _ { G } ^ { i j } = \frac { 2 } { 3 } \nu ^ { 2 } n _ { G } ^ { i } n _ { G } ^ { j } \frac { 1 - q + q ^ { 3 } / 5 } { 1 - 2 q / 3 } .
$$

For the case $r < r _ { c }$ , a similar calculation gives

$$
{ U } _ { G } ^ { i j } = { \frac { 2 } { 5 } } \nu ^ { 2 } n _ { G } ^ { i } n _ { G } ^ { j } ,
$$

independent of $q$ . Thus for $\nu \sim 2 3 0 ~ \mathrm { k m / s }$ , we find an amplitude $2 - 4 \times 1 0 ^ { - 7 }$ . Note from Eq. (8.56) that only the matter inside our radius has an effect on the anisotropy. Even though the galaxy and its halo are not strictly spherically symmetric, this is unlikely to alter the estimate significantly. Table 8.2 shows our adopted value for the galactic potential along with the directions to the galactic center in various coordinates.

The anisotropies in $G _ { \mathrm { L } }$ in Eq. (8.44) provided the first bounds on PPN preferred-frame and preferred-location parameters. Surveying the geophysical literature of the time, Will (1971a) pointed out that data on the semidurnal tides of the Sun and Moon agreed with Newtonian predictions to the level corresponding to amplitudes of $1 0 ^ { - 9 }$ , resulting in the bounds $\left| \alpha _ { 2 } \right| < 3 \times 1 0 ^ { - 2 }$ and $\left| \xi \right| < 5 \times 1 0 ^ { - 3 }$ . An explicit experimental test was performed by Warburton and Goodkind (1976), who used an array of superconducting gravimeters at a site in southern California to take an 18-month record of tidal amplitudes and phases. They included the full array of PPN variations, not just the ones shown in Eq. (8.44), and carefully accounted for the disturbing effects of tides of the nearby Pacific Ocean. The result was the pair of bounds $| \alpha _ { 2 } | < 4 \times 1 0 ^ { - 4 }$ and $\vert \xi \vert < 1 0 ^ { - 3 }$ . Nordtvedt and Will (1972) placed modest bounds on various combinations of the parameters using perhelion advance information and limits on any anomalous annual variation in the rotation rate of the Earth, the latter induced by the $w _ { 0 } \cdot \nu$ term in Eq. (8.44).

A tighter bound on $\alpha _ { 2 }$ was set by Nordtvedt (1987), by considering the spin precession effect of Eq. (8.54) acting on the Sun. Focusing on the preferred-frame term, the precession takes the form $d { \pmb J } / d t = { \pmb \Omega } \times { \pmb J }$ , where $J = I _ { e } \omega e$ and $\begin{array} { r } { \Omega = - { \frac { 1 } { 2 } } \alpha _ { 2 } \omega ( \pmb { e } \cdot \pmb { w } ) \pmb { w } } \end{array}$ , where $\omega$ is the rotation angular velocity of the Sun. Over a time $T .$ the change in direction of the spin axis would be of order

$$
\frac { \Delta J } { J } \sim \frac { \omega T } { 2 } \alpha _ { 2 } w ^ { 2 } \sin \beta _ { w } \cos \beta _ { w } .
$$

Inserting $\omega \simeq 2 . 8 \times 1 0 ^ { - 6 } \mathrm { s } ^ { - 1 }$ , $T = 4 \times 1 0 ^ { 9 }$ years, and requiring that the change be no larger than the known $7 ^ { \circ }$ tilt of the Sun’s axis relative to the ecliptic, we obtain $\left| \alpha _ { 2 } \right| < 2 \times 1 0 ^ { - 6 }$ .

Lunar laser ranging yielded the bounds $\alpha _ { 1 } = ( - 0 . 7 \pm 1 . 8 ) \times 1 0 ^ { - 4 }$ and $\alpha _ { 2 } = ( 1 . 8 \pm$ $5 . 0 ) \times 1 0 ^ { - 5 }$ from the absence of any induced eccentricity (Eq. (8.35)) in the lunar orbit (M¨uller et al., 1996, 2008).

Substantial improvements in bounds on these parameters came from analyzing timing data from a variety of isolated and binary pulsars.

In TEGP, we pointed out that, for an isolated spinning body moving relative to the preferred frame, the term proportional to $\alpha _ { 3 }$ in Eq. (8.27) produces a self-acceleration (recall that $\alpha _ { 3 }$ is also a conservation law parameter). If the body were a pulsar, this would induce a change in the observed pulse period $P _ { p }$ at a rate $d P _ { p } / d t \simeq 2 \times 1 0 ^ { - 4 } \alpha _ { 3 }$ , for $\Omega / m \simeq 0 . 1$ and $w \simeq 3 0 0 \mathrm { k m / s }$ . Given that half of the observed pulsars have $d P _ { p } / d t$ lying between $1 0 ^ { - 1 4 }$ and $1 0 ^ { - 1 5 }$ , we inferred the upper bound $\left| \alpha _ { 3 } \right| < 1 0 ^ { - 1 0 }$ . This bound was improved dramatically using data on $\sim 2 1$ WBMSPs. Searches for the induced eccentricity of Eq. (8.40), combined with statistical arguments to mitigate the effects of unknown orbital orientations of the observed population of WBMSPs led to the impressive bound $\left| \alpha _ { 3 } \right| < 4 \times 1 0 ^ { - 2 0 }$ (Bell and Damour, 1996; Stairs et al., 2005).

Similar searches for eccentricities induced by the $\alpha _ { 1 }$ term in Eq. (8.35) resulted in bounds on $\alpha _ { 1 }$ as small as a few parts in $1 0 ^ { 5 }$ (Wex, 2000; Shao and Wex, 2012). The tightest bound used a specific binary pulsar $J 1 7 3 8 \substack { + 0 3 3 3 }$ , whose orbit around its whitedwarf companion has an eccentricity $3 . 4 \times 1 0 ^ { - 7 }$ . The analysis was helped by the fact that the white dwarf is bright enough to be observed spectroscopically, leading to accurate determinations of the key orbital parameters. Furthermore, because the pericenter advances at a rate of about $1 . 6 \mathrm { d e g ~ \ y r } ^ { - 1 }$ , the decade-long data span made it possible to partially separate any induced eccentricity, whose direction is fixed by the direction of $\boldsymbol { w }$ , from the natural eccentricity, which rotates with the pericenter. For this system the result was $\vert \alpha _ { 1 } \vert < 3 . 4 \times 1 0 ^ { - 5 }$ (Shao and Wex, 2012).

Limits on $\alpha _ { 2 }$ and $\xi$ were obtained by looking for the precession of the orbital plane of a binary system [see Eq. (8.37)]. Such a precession would lead to a variation in the “projected semimajor axis” of the pulsar, $a _ { p } \sin \iota$ , a quantity that is measured very accurately in binary pulsar timing (see Section 12.1). Combining data from the two WBMSP systems $J 1 7 3 8 \substack { + 0 3 3 3 }$ and $J 1 0 1 2 + 5 3 0 7$ , Shao and Wex (2012, 2013) obtained the bounds $| \alpha _ { 2 } | \ <$ $1 . 8 \times 1 0 ^ { - 4 }$ and $\vert \xi \vert < 3 . 1 \times 1 0 ^ { - 4 }$ .

These bounds were improved substantially by searching for the precession of the spin of isolated pulsars (see Eq. (8.54)), the analogue of the precession effect studied by Nordtvedt (1987) in the solar context. If the spin of the pulsar precesses, then the pulse profile should change as the line of site to the pulsar slices different parts of the emission region. Using 15

In this chapter, we have used a number of observations of binary and isolated pulsars to place bounds on preferred-frame and preferred-location parameters. And observations of the pulsar in a triple system may soon place a bound on the Nordtvedt parameter.

However, the PPN framework does not strictly apply to such systems, because the neutron stars are compact, strong-field objects, in the sense that the post-Newtonian expansion parameter $\epsilon$ can be of order $0 . 1 - 0 . 3$ near and inside these objects. And in theories of gravity with spontaneous scalarization effects, the effective internal values of $\epsilon$ can be much larger than unity.

Accordingly, one should treat bounds on the PPN parameters inferred from such systems with some caution. In some alternative theories, the effect of the compact body could be to rescale the relevant PPN parameter by a factor $1 + \epsilon ,$ where $\epsilon \sim m / r ,$ where $m$ and r are the mass and radius of the neutron star. Since the bounds on many of these parameters are very small, such corrections of order tens of percent will be insignificant. On the other hand, in some theories, additional parameters may be present for systems containing compact objects, and the relation between these paramaters and the true PPN parameters may be more complicated than a simple rescaling of the PPN parameter. This will be addressed in Section 10.3.1, where we will introduce a “modified EIH formalism $, \ Y ,$ parametrization of the Lagrangian for systems of compact bodies, rather than of the spacetime post-Newtonian metric. These parameters will depend on the theory of gravity and on the internal structure of the compact bodies in the system. In the limit where there are no compact bodies, these parameters will have specific limits in terms of the PPN parameters for semiconservative theories. For example, using the modified EIH formalism, we will derive an equation for the preferred-frame perturbations of a binary system of compact bodies that generalizes the preferred-frame terms in Eq. (8.28).

In the literature on tests of SEP using neutron stars, it is conventional to designate the relevant parameters using “hats,” for example $\hat { \alpha } _ { 1 } , \hat { \alpha } _ { 2 } , 0 \mathsf { r } \hat { \xi } ,$ to emphasize that the parameters may not be quite the same as the corresponding PPN parameters.

years of observations of $\mathrm { B } 1 9 3 7 + 2 1$ and J1744-1134, two isolated millisecond pulsars with very stable pulse profiles, Shao et al. (2013) and Shao and Wex (2013) found no evidence of pulse profile changes, and thereby established the strong bounds $\left| \alpha _ { 2 } \right| \mathrm { ~ < ~ } 1 . 6 \times 1 0 ^ { - 9 }$ and $\vert \xi \vert < 3 . 9 \times 1 0 ^ { - 9 }$ . The use of isolated pulsars rather than binary pulsars was crucial, in order to avoid any complication from the well-known geodetic precession of spins that occurs in binary pulsar systems (see Section 12.1.2).

# 8.5 Constancy of Newton’s Gravitational Constant

Most theories of gravity that violate SEP predict that the locally measured Newtonian gravitational constant may vary with time as the universe evolves. For the theories discussed in Chapter 5, the predictions for $\dot { G } / G$ can generally be written in terms of time derivatives of the asymptotic dynamical fields or of the asymptotic matching parameters.

Other, more heuristic proposals for a changing gravitational constant, such as those due to Dirac, cannot be written this way. Dyson (1972) gives a detailed discussion of these earlier proposals. Where $G$ does change with cosmic evolution, its rate of variation should be of the order of the expansion rate of the universe, that is

$$
\frac { \dot { G } } { G } \simeq \sigma H _ { 0 } ,
$$

where $H _ { 0 }$ is the Hubble expansion parameter whose value is

$$
H _ { 0 } = 7 0 \pm 2 \mathrm { k m ~ s } ^ { - 1 } \mathrm { M p c } ^ { - 1 } \simeq 7 \times 1 0 ^ { - 1 1 } \mathrm { y r } ^ { - 1 } ,
$$

(Bennett et al., 2013; Planck Collaboration et al., 2014; Grieb et al., 2017), and $\sigma$ is a dimensionless parameter whose value depends upon the theory of gravity under study and upon the detailed cosmological model assumed.

For general relativity, of course, $G$ is precisely constant $( \sigma = 0$ ). For Brans-Dicke theory in a spatially flat Friedmann-Robertson-Walker (FRW) cosmology, $\sigma \simeq - ( 2 + \omega ) ^ { - 1 }$ [see, e.g., Section 16.4 of Weinberg (1972)]. In Einstein-Æther and Khronometric theory, $G$ is constant, basically because the auxiliary vector field is constrained to have unit norm.

However, several observational constraints can be placed on ${ \dot { G } } / G$ , one kind coming from bounding the present rate of variation, another from bounding a difference between the present value and a past value. The first type of bound typically comes from LLR measurements, planetary radar-ranging measurements, and pulsar timing data. The second type comes from studies of the evolution of the Sun, stars and the Earth, Big-Bang nucleosynthesis, and analyses of ancient eclipse data. Given the present uncertainties in laboratory measurements of $G$ (together with significant disagreements among measurements that are larger than the individual errors), it is unlikely that laboratory tests of $\dot { G }$ will contribute interesting bounds for the foreseeable future. For a time during the 1970s, van Flandern (1975) and others argued for a nonzero $\dot { G }$ , based on observations of the recession of the Moon from the Earth. Today those claims are given little credence, particularly in the face of much more precise, independent bounds on ${ \dot { G } } / G$ .

The best limits on a current $\dot { G } / G$ come from improvements in the ephemeris of Mars using range and Doppler data from the Mars Global Surveyor (1998 – 2006), Mars Odyssey $( 2 0 0 2 - 2 0 0 8 )$ , and Mars Reconnaissance Orbiter $( 2 0 0 6 - 2 0 0 8 )$ , together with improved data and modeling of the effects of the asteroid belt (Pitjeva, 2005; Konopliv et al., 2011; Pitjeva and Pitjev, 2013). Since the bound is actually on variations of $G M _ { \odot }$ , any future improvements in $\dot { G } / G$ beyond a part in $1 0 ^ { 1 3 }$ per year will have to take into account models of the actual mass loss from the Sun, due to radiation of photons and neutrinos $( \sim 0 . 7 \times 1 0 ^ { - 1 3 } \mathrm { y r } ^ { - 1 } )$ and due to the solar wind $( \sim 0 . 6 \times 1 0 ^ { - 1 3 } \mathrm { y r } ^ { - 1 } )$ . Another bound comes from LLR measurements (Williams et al., 2004b). For earlier results see Dickey et al. (1994),Williams et al. (1996) and M¨uller et al. (1999). This precision could be improved by the future BepiColombo mission to Mercury, scheduled for launch in late 2018 (Milani et al., 2002; Ashby et al., 2007).

Although bounds on $\dot { G } / G$ from solar-system measurements can be correctly obtained in a phenomenological manner through the simple expedient of replacing $G$ by $G _ { 0 } + \dot { G } ( t - t _ { 0 } )$ in Newton’s equations of motion, the same does not hold true for pulsar and binary pulsar timing measurements. The reason is that, in theories of gravity that violate SEP, such as scalar-tensor theories, the “mass” and moment of inertia of a gravitationally bound body may vary with $G$ . Because neutron stars are highly relativistic, the fractional variation in these quantities can be comparable to $\dot { G } / G$ , the precise variation depending both on the equation of state of neutron star matter and on the theory of gravity in the strong-field regime. The variation in the moment of inertia affects the spin rate of the pulsar, while the variation in the mass can affect the orbital period of a binary in a manner that can subtract from the direct effect of a variation in $G$ , given by $\dot { P } _ { b } / P _ { b } = - 2 \dot { G } / G$ (Nordtvedt, 1990). Thus, the bounds quoted in Table 8.3 for binary and millisecond pulsars are theorydependent and must be treated as merely suggestive.

<table><tr><td colspan="3">Table 8.3 Tests of the constancy of G.</td></tr><tr><td>Method</td><td>G/G (10-13 yr-1)</td><td>Reference</td></tr><tr><td> Mars ephemeris</td><td>0.1 ± 1.6 -0.6 ± 0.4</td><td>Konopliv et al. (2011) Pitjeva and Pitjev (2013)</td></tr><tr><td> Lunar laser ranging</td><td>4±9</td><td>Williams et al. (2004b)</td></tr><tr><td rowspan="2">Binary and millisecond pulsars</td><td>0.7 ±3.8</td><td>Hofmann et al. (2010)</td></tr><tr><td>-7±33</td><td>Deller et al. (2008)</td></tr><tr><td></td><td></td><td>Lazaridis et al. (2009)</td></tr><tr><td>Helioseismology</td><td>0±16</td><td>Guenther et al. (1998)</td></tr><tr><td>Big-bang nucleosynthesis</td><td>0±4</td><td>Copi et al. (2004)</td></tr><tr><td></td><td></td><td>Bambi et al. (2005)</td></tr></table>

Bounds from helioseismology and Big-Bang nucleosynthesis (BBN) assume a model for the evolution of $G$ over the multi-billion-year time spans involved. For example, the concordance of predictions for light elements produced around 3 minutes after the Big Bang with the abundances observed in the present universe indicate that $G$ then was within 20 percent of $G$ today. Assuming a power-law variation of $G \sim t ^ { - \alpha }$ then yields the bound on $\dot { G } / G$ today shown in Table 8.3.

A number of tests of post-Newtonian gravitational effects do not fit into either of the two categories, classical tests or tests of SEP. These include the search for relativistic effects involving spinning bodies (Section 9.1), the de Sitter precession (Section 9.2), and tests of post-Newtonian conservation laws (Section 9.3). Some of these experiments provide limits on PPN parameters, in particular the conservation-law parameters $\zeta _ { 1 }$ , $\zeta _ { 2 }$ , $\zeta _ { 3 }$ , and $\zeta _ { 4 }$ , that were not constrained (or that were constrained only indirectly) by the classical tests and by tests of SEP. Such experiments provide new information about the nature of post-Newtonian gravity. Others, such as measurements of spin effects, constrain values for PPN parameters that are already better constrained by the experiments discussed in Chapters 7 and 8. Nevertheless, such experiments are important, for the following reasons:

(i) They may provide independent checks of the values of the PPN parameters, and thereby independent tests of gravitation theory. They are independent in the sense that the physical mechanism responsible for the effect being measured may be rather different than the mechanism that led to the prior limit on the PPN parameters. An example is the Lense-Thirring effect, the dragging of inertial frames produced by the rotation of a body. It is not a preferred-frame effect, yet it depends upon the parameter $\alpha _ { 1 }$ . So while a bound on $\alpha _ { 1 }$ achieved by measuring the Lense-Thirring effect may not beat the strong bounds we saw in Chapter 8, it comes from rather different physical effects.

(ii) The structure of the PPN formalism is an assumption about the nature of gravity, one that, while seemingly compelling, could be incorrect or incomplete. According to this viewpoint, one should not prejudice the design, performance, and interpretation of an experiment by viewing it within any single theoretical framework. Thus, the $\gamma$ parameters measured by light-deflection and time-delay experiments could in principle be different, while according to the PPN formalism they must be identical. We agree with this viewpoint because, although theoretical frameworks such as the PPN formalism have proven to be very powerful tools for analyzing both theory and experiment, they should not be used in a prejudicial way to reduce the importance of experiments that have independent, compelling justifications for their performance.

(iii) Any result in disagreement with general relativity would be of extreme interest.

# 9.1 Testing the Effects of Spin

Post-Newtonian gravity introduces an entirely new class of phenomena that are not present in Newtonian gravity – the effects of spin or rotation. These effects occur because, at post-Newtonian order, the velocity of matter becomes important, and consequently the internal velocity of a rotating body, even if it is at rest, can affect the gravitational field it generates, and can influence how it responds to an external field. These effects, known in various contexts as spin-orbit and spin-spin coupling, frame-dragging, Lense-Thirring effects, gravitomagnetism, and so on, are fundamentally relativistic. This is also true in quantum mechanics, where spin effects arise only when special relativity is merged with quantum theory to produce the Dirac equation. In post-Newtonian theory, the term “spin” refers only to the rotation of a finite-size, massive body. It does not refer to quantum mechanical spin, although there are numerous parallels between effects in the two realms.

There are precessions of spins in Newtonian gravity, but the nature of the effects is completely different. For example, the “precession of the equinoxes” is caused by the precession of the Earth’s rotation axis with a period of about 26,000 years. However this is the result of the interaction between the Earth’s quadrupole moment (which is caused by the centrifugal forces associated with its rotation) and the gravitational fields of the Sun and Moon. It is a nonrelativistic, quadrupole interaction involving nonspherical mass distributions. By contrast, the relativistic effects of spin are dipole in nature.

# 9.1.1 Effects of spin in two-body systems

In Section 6.7 we derived the post-Newtonian effects of the spin of a body on its motion, and the effects of its motion in a gravitational field on its spin. We found that a spinning body experiences spin-orbit and spin-spin accelerations [Eq. (6.113)] produced by both its own spin and the spins of other bodies in the system. At the same time, its own spin experiences a precession, caused by spin-orbit, spin-spin and preferred-frame couplings. The key equations, (6.113), and (6.119)–(6.121), were derived for a general $N .$ -body system of spinning masses. Here we specialize to two bodies and derive results that will allow us to discuss several important tests of the effects of spin, including Gravity Probe B, LAGEOS tracking, and precessions in binary pulsars.

We consider a binary system of bodies with masses $m _ { 1 }$ and $m _ { 2 }$ and spins $\pmb { S } _ { 1 }$ and $\pmb { S } _ { 2 }$ , in an elliptical orbit with elements $p , e , \iota , \Omega$ , and $\omega$ . We will first work out the precession of the spin of body 1, averaged over an orbit. Using Eqs. (6.119) and (6.121) restricted to two bodies, along with the fact that $\pmb { \nu } _ { 1 } = ( m _ { 2 } / m ) \pmb { \nu }$ and $\pmb { \nu } _ { 2 } = - ( m _ { 1 } / m ) \pmb { \nu }$ , we obtain

$$
\begin{array} { c } { \displaystyle { \frac { d { \bf S } _ { 1 } } { d t } = \frac { 1 } { 2 } \left( 2 \gamma + 1 + \frac { m _ { 1 } } { m } \right) \frac { m _ { 2 } } { r ^ { 3 } } { \boldsymbol { h } } \times { \bf S } _ { 1 } } } \\ { \displaystyle { + \frac { 1 } { 8 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \frac { 1 } { r ^ { 3 } } \left[ 3 { \boldsymbol { n } } ( { \boldsymbol { n } } \cdot { \bf S } _ { 2 } ) - { \bf S } _ { 2 } \right] \times { \bf S } _ { 1 } , } } \end{array}
$$

where $r \equiv \left| \boldsymbol { x } _ { 1 2 } \right|$ , ${ \pmb n } \equiv { \pmb x } _ { 1 2 } / r$ , and $\pmb { h } \equiv \pmb { x } \times \pmb { \nu }$ . By suitably interchanging labels $1  2$ , we can write down the corresponding equation for spin 2. Using our Keplerian orbit formulae of Eq. (6.73), and setting both spins to be constant on the right-hand-side, we can integrate over one orbit to find the change $\Delta \pmb { S } _ { 1 }$ . We make use of the fact that, when integrated over one period,

$$
\int \frac { 1 } { r ^ { 3 } } d t = \frac { 2 \pi } { h p } { , } \quad \int \frac { n ^ { i } n ^ { j } } { r ^ { 3 } } d t = \frac { \pi } { h p } \left( \delta ^ { i j } - { \hat { h } } ^ { i } { \hat { h } } ^ { j } \right) { , }
$$

where $h = { \sqrt { m p } }$ and $p = a ( 1 - e ^ { 2 } )$ . The change in $\pmb { S } _ { 1 }$ over one orbit is then given by

$$
\begin{array} { l } { \displaystyle \Delta \pmb { S } _ { 1 } = \pi \left( 2 \gamma + 1 + \frac { m _ { 1 } } { m } \right) \frac { m _ { 2 } } { p } \hat { \pmb { h } } \times \pmb { S } _ { 1 } } \\ { \displaystyle + \frac { \pi } { 8 h p } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \left[ \pmb { S } _ { 2 } - 3 \hat { \pmb { h } } ( \hat { \pmb { h } } \cdot \pmb { S } _ { 2 } ) \right] \times \pmb { S } _ { 1 } . } \end{array}
$$

The first term is frequently called the geodetic precession; it is a spin-orbit effect, as it involves the interaction between the spin $\pmb { S } _ { 1 }$ and the orbital angular momentum $\pmb { h }$ . For the geodetic effect, the change in $\pmb { S } _ { 1 }$ is always confined to the orbital plane (orthogonal to $\pmb { h }$ ); it vanishes if the spin is parallel to $\pmb { h }$ and is maximized if the spin lies in the orbital plane. Geometrically, the effect is partially linked to the fact that the parallel transport of a vector around a closed path in a curved spacetime causes a change in the direction of the vector related to the spatial curvature and the area enclosed by the path; the $^ { \bullet \bullet } 2 \gamma ^ { \bullet \bullet }$ part of the coefficient is related to this spatial curvature effect. The remaining piece of the coefficient is related to the special relativistic Thomas precession of a spin moving in a curved orbit.

The second term, a spin-spin interaction, is referred to in many ways: Lense-Thirring precession, dragging of inertial frames and “Schiff” precession. If the companion’s spin is fixed, $\pmb { S } _ { 1 }$ undergoes a precession about a fixed vector that is a combination of the spin of the companion and the orbital angular momentum.

To find the spin-orbit and spin-spin contributions to the relative equation of motion for a binary system, $\pmb { a } \equiv \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ , we take Eq. (6.113), set $w = 0$ and $\alpha _ { 3 } = 0$ , and obtain

$$
\begin{array} { l } { { \displaystyle a [ \mathrm { S O } ] = \frac { 3 } { 2 r ^ { 3 } } \bigg \{ n ( n \times \nu ) \cdot \left[ ( 2 \gamma + 1 + \lambda ) \sigma + \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) S \right] } }  \\ { { \displaystyle ~ + ~ ( n \cdot \nu ) n \times \left[ ( 2 \gamma + 1 - \lambda ) \sigma + \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) S \right] } } \\ { { \displaystyle ~ - \frac { 2 } { 3 } \nu \times \left[ ( 2 \gamma + 1 ) \sigma + \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) S \right] \bigg \} , } } \\ { { \displaystyle a [ \mathrm { S S } ] = \frac { 3 } { 8 } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \frac { m } { r ^ { 4 } } \left[ 5 n ( n \cdot \hat { S } _ { 1 } ) ( n \cdot \hat { S } _ { 2 } ) - n \hat { S } _ { 1 } \cdot \hat { S } _ { 2 } - 2 \hat { S } _ { ( 1 } ( n \cdot \hat { S } _ { 2 ) } ) \right] , } } \end{array}
$$

where

$$
\begin{array} { l } { { \displaystyle \sigma \equiv \frac { m _ { 2 } } { m _ { 1 } } S _ { 1 } + \frac { m _ { 1 } } { m _ { 2 } } S _ { 2 } , } } \\ { { \displaystyle S \equiv S _ { 1 } + S _ { 2 } , } } \\ { { \displaystyle \hat { S } _ { i } \equiv \frac { S _ { i } } { m _ { i } } . } } \end{array}
$$

Calculating the radial, cross-track and out-of-plane components of these perturbing accelerations, substituting into Eq. (6.74), and integrating over one orbit assuming that the spins are constant over an orbital timescale, we obtain the secular changes in the orbit elements. For the spin-orbit terms we find

$$
\begin{array} { l } { \Delta a = 0 , } \\ { \Delta e = 0 , } \\ { \Delta i = \displaystyle \frac { \pi } { h p } \left( C _ { \mathrm { P } } \cos \omega - C _ { \mathrm { Q } } \sin \omega \right) = \frac { \pi } { h p } C _ { \Omega } , } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \sin \imath \Delta \Omega = \frac { \pi } { h p } \left( C _ { \mathrm { P } } \sin \omega + C _ { \mathrm { Q } } \cos \omega \right) = \frac { \pi } { h p } C _ { \perp } , } } \\ { { \displaystyle \Delta \varpi = - \frac { 2 \pi } { h p } C _ { \mathrm { h } } , } } \end{array}
$$

where

$$
\pmb { C } = ( 2 \gamma + 1 ) \pmb { \sigma } + \frac { 1 } { 2 } ( 4 \gamma + 4 + \alpha _ { 1 } ) \pmb { S } ,
$$

and the subscripts P, Q and h denote components along the pericenter direction, the direction in the orbital plane given by ${ \pmb e } _ { \mathrm { Q } } = { \hat { \pmb h } } \times { \pmb e } _ { \mathrm { P } }$ , and the direction $\hat { h }$ normal to the orbital plane, respectively, while the subscripts $\Omega$ and $\perp$ denote components along the line of nodes and along the direction given by $\pmb { e } _ { \perp } = \hat { \pmb { h } } \times \pmb { e } _ { \Omega }$ . Note that the arbitrary parameter $\lambda$ , related to the choice of world line of the spinning body $\left( \mathrm { B o x } 6 . 3 \right)$ drops out.

Although the inclination of the orbit relative to the reference system changes, the inclination relative to the vector $c$ does not. The rate of change of $\hat { h }$ is given by $\Delta \hat { \pmb h } =$ $\Delta \Omega \sin \iota e _ { \Omega } - \Delta \iota e _ { \perp } = ( \pi / 2 h p ) ( C _ { \perp } e _ { \Omega } - C _ { \Omega } e _ { \perp } )$ , which is perpendicular to $C .$ . Thus the orbital angular momentum vector precesses around $c$ with ${ \hat { \pmb { h } } } \cdot { \pmb { C } } =$ constant.

For the spin-spin contributions we obtain

$$
\begin{array} { c } { { \Delta a = 0 , } } \\ { { \Delta e = 0 , } } \\ { { \Delta i = - \displaystyle \frac { 3 \pi } { 8 p ^ { 2 } } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \left[ ( S _ { 1 } ) _ { \mathrm { h } } ( S _ { 2 } ) _ { \Omega } + ( S _ { 2 } ) _ { \mathrm { h } } ( S _ { 1 } ) _ { \Omega } \right] , } } \\ { { } } \\ { { \sin \iota \Delta \Omega = - \displaystyle \frac { 3 \pi } { 8 p ^ { 2 } } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \left[ ( S _ { 1 } ) _ { \mathrm { h } } ( S _ { 2 } ) _ { \perp } + ( S _ { 2 } ) _ { \mathrm { h } } ( S _ { 1 } ) _ { \perp } \right] , } } \\ { { } } \\ { { \Delta \varpi = - \displaystyle \frac { 3 \pi } { 8 p ^ { 2 } } \left( 4 \gamma + 4 + \alpha _ { 1 } \right) \left[ S _ { 1 } \cdot S _ { 2 } - 3 ( S _ { 1 } ) _ { \mathrm { h } } ( S _ { 2 } ) _ { \mathrm { h } } \right] . } } \end{array}
$$

# 9.1.2 Tests of spin precession

In 2011 the Relativity Gyroscope Experiment (Gravity Probe B or GPB) carried out by Stanford University, NASA, and Lockheed Martin Corporation, finally brought to a conclusion a space mission to detect the frame-dragging and geodetic precessions of an array of gyroscopes orbiting the Earth (Everitt et al., 2011; Everitt et al., 2015). The story of GPB is told in Box 9.1.

To analyze the experiment, we use Eq. (9.3), with the mass of the gyroscope $m _ { 1 }$ set equal to zero; $m _ { 2 }$ and $\pmb { S } _ { 2 }$ are the mass and spin of the Earth, and $p$ is the orbital semilatus rectum. To maximize the geodetic precession, it is useful to orient the spin of the gyroscope to be perpendicular to $\hat { h }$ , in other words to lie in the orbital plane. Then the spin will precess within the orbital plane, in the same sense as the orbital motion. To maximize the framedragging precession, one should maximize $| S _ { 2 } - 3 \hat { \pmb { h } } ( \hat { \pmb { h } } \cdot { \pmb { S } } _ { 2 } ) | = ( S _ { 2 } ^ { 2 } + 3 ( \hat { \pmb { h } } \cdot { \pmb { S } } _ { 2 } ) ^ { 2 } ) ^ { 1 / 2 }$ , which means putting the orbit on the equatorial plane so that $\hat { h }$ and $\pmb { S } _ { 2 }$ are parallel, and orienting the spin to be in the orbital plane so that $\pmb { S } _ { 1 }$ is orthogonal to both $\hat { h }$ and $\pmb { S } _ { 2 }$ . However the resulting precession of the spin will also be in the orbital plane, adding to or subtracting from the geodetic term. This makes it impossible to separate the two effects. An alternative

# Box 9.1

# Gravity Probe B

Gravity Probe B will very likely go down in the history of science as one of the most ambitious, difficult, expensive, and controversial relativity experiments ever performed. It was almost 50 years from inception to completion and US\$ 750 million in the making, although only about half of the total time was spent as a full-fledged, approved space flight program.

The origin of GPB dates back to around 1960, when Leonard Schiff at Stanford calculated the geodetic and Lense-Thirring precessions of a gyroscope and suggested the possibility of measuring them. Independently of Schiff, George Pugh at the Weapons Systems Evaluation Group of the US military had performed the same calculations a few months earlier. Pugh was assessing the use of high-performance gyroscopes in missile and aircraft guidance. He wondered how large the relativistic effects would be, and what it would take for a space experiment to measure them. Pugh’s classified work could not be published in the open literature, and so Schiff was initially given credit for the idea; only later was Pugh’s work discovered and recognized. It is worth noting that all this occurred in the very early days of space exploration, only two years after the launch by the Soviet Union of Sputnik, the world’s first artificial satellite.

GPB started officially in late 1963 when NASA funded the initial R&D work at Stanford to identify the new technologies needed to make such a difficult measurement possible. Francis Everitt became Principal Investigator of GPB in 1981, and the project moved to the mission design phase in 1984. At that time, plans called for a preliminary flight on board the Space Shuttle to test key technologies to be used in GPB (similar in intent to the LISA Pathfinder mission of 2015), followed by full launch from the Shuttle a few years later. Unfortunately the 1986 Space Shuttle Challenger catastrophe forced a cancellation of the technology test, and a complete redesign of the spacecraft for a launch from a Delta rocket. The additional costs and delays arising from this engendered increasing criticism of the project, and NASA asked the National Academy of Sciences to conduct a thorough review of the project in 1994. Following the endorsement of that committee, GPB was approved for flight development, and began to collaborate with Lockheed-Martin and NASA’s Marshall Space Flight Center. The satellite finally was launched on April 20, 2004 for a 16-month mission, but another five years of data analysis were needed to tease out the effects of relativity from a background of other disturbances of the gyros.

There were four gyroscopes aboard GPB. Each gyroscope was a fused silica rotor, about four centimeters in diameter, machined to be spherical and homogeneous to better than a part per million, and coated with a thin film of niobium. The gyroscope assembly, which sat in a dewar of 2440 liters of liquid helium, was held at 1.8 degrees Kelvin. At this temperature, niobium is a superconductor, and the supercurrents in the niobium of each spinning rotor produce a “London” magnetic moment parallel to its spin axis. Extremely sensitive magnetometers (superconducting quantum interference detectors, or ${ } ^ { \prime \prime } \mathsf { S } 0 \mathsf { U } | | \mathsf { D } \mathsf { S } ^ { \prime \prime } )$ attached to the wall of the spherical chamber housing each rotor were capable of detecting minute changes in the orientation of the rotor’s magnetic moment and hence the precession of its rotation axis.

After the spacecraft reached its orbit, the four gyros were aligned to spin along the symmetry axis of the spacecraft. This axis was also the optical axis of a telescope directly mounted on the end of the structure housing the rotors. Spacecraft thrusters oriented the telescope to point precisely toward IM Pegasi (except when the Earth intervened, once per orbit). In order to average out numerous unwanted nonrelativistic torques on the gyros, the spacecraft rotated about its axis once every 78 seconds. The satellite was placed in an almost perfectly circular polar orbit with an altitude of 642 kilometers above the Earth’s surface.

Almost every aspect of the spacecraft, its subsystems, and the science instrumentation performed extremely well, some far better than expected. Still, the success of such a complex and delicate experiment boils down to figuring out the sources of error. In particular, having an accurate calibration of the electronic readout from the SQUID magnetometers with respect to the tilt of the gyros was essential. The plan for calibrating the SQUIDs was to exploit the aberration of starlight, which causes a precisely calculable misalignment between the rotors and the telescope as the latter shifts its pointing toward the guide star by up to 20 arcseconds to compensate for the orbital motion of the spacecraft and of the Earth. However, three important, but unexpected, phenomena were discovered during the experiment that affected the accuracy of the results.

First, because each rotor is not exactly spherical, its principal axis rotates around its spin axis with a period of several hours, with a fixed angle between the two axes. This is the familiar “polhode”motion of a spinning top. In fact this polhoding was essential in the calibration process because it led to modulations of the SQUID output via the residual trapped magnetic flux on each rotor (about 1 percent of the London moment). The polhode period and angle of each rotor were expected to remain constant throughout the mission, leading to accurate calibrations, but instead these quantities actually decreased monotonically with time, implying the presence of some damping mechanism, and this significantly complicated the calibration analysis. In addition, each rotor was found to make occasional, seemingly random “jumps” in its orientation—some as large as 100 milliarcseconds. Some rotors displayed more frequent jumps than others. Without being able to continuously monitor the rotors’ orientation, the GPB team could not fully exploit the calibrating effect of the stellar aberration in their analysis. Finally, during a planned 40-day, end-of-mission calibration phase, the team discovered that when the spacecraft was deliberately pointed away from the guide star by a large angle, the misalignment induced much larger torques on the rotors than expected. From this, they inferred that even the very small misalignments that occurred during the science phase of the mission had induced torques that were probably several hundred times larger than the designers had estimated.

What ensued during the data analysis phase following the mission was worthy of a detective novel. The critical clue came from the calibration tests. Here, they took advantage of the residual trapped magnetic flux on the gyroscope. Superconducting lead shielding was used to suppress stray magnetic fields before the niobium coated gyroscopes were cooled, but no shielding is ever perfect. This flux adds a periodic modulation to the SQUID output, which the team used to plot the phase and polhode angle of each rotor throughout the mission. This helped them to discover that interactions between random patches of electrostatic potential fixed to the surface of each rotor, and similar patches on the inner surface of its spherical housing, were causing the extraneous torques. In principle, the rolling spacecraft should have suppressed these effects via averaging, but they were larger than expected.

Fortunately, the patches are fixed on the various surfaces, and so it was possible to build a parametrized model of the patches on both surfaces using multipole expansions, and to calculate the torques induced by those interactions when the spin and spacecraft axes are misaligned, as a function of the parameters. One prediction of the model was that the induced torque should be perpendicular to the plane formed by the two axes, and this was clearly seen in the data. Another prediction was that, when the slowly decreasing polhode period crosses an integer multiple of the spacecraft roll period, the torques fail to average over the roll period, whereupon the spin axis precesses about its initial direction in an opening Cornu spiral, then migrates to a new direction along a closing Cornu spiral. This is known as a loxodromic path, familiar to navigators as a path of