CHAPTER 23

# S23.1. PROLOG

Preview of the rest of this book

Beautiful though gravitation theory may be,it is a sterile subject until it touches thereal physical world. Only the hard reality of experiments and of astronomical observations can bring gravitation theory to life. And only by building theoretical models of stars (Part V),of the universe (Part VI), of stellar collapse and black holes (Part VII), of gravitational waves and their sources (Part VII),and of gravitational experiments (Part IX),can one understand clearly the contacts between gravitation theory and reality.

The model-building in this book will follow the tradition of theoretical physics. Each Part (stars,universe,collapse,...） will begin with the most oversimplified model conceivable,and will subsequently add only those additional touches of realism necessary to make contact with the least complex of actual physical systems. The result will be a tested intellectual framework, ready to support and organize the additional complexities demanded by greater realism. Greater realism will not be attempted in this book.But the reader seeking it could start in no better place than the two-volume treatise on Relativistic Astrophysics by Zel'dovich and Novikov (1971,1974).

Begin,now,with models for relativistic stars.As a major simplification,insist (initially) that all stars studied be static. Thereby exclude not only exploding and pulsating stars,but even quiescent ones with stationary rotational motions. From the static assumption, plus a demand that the star be made of “perfect fluid" (no shear stresses allowed!), plus Einstein's field equations, it probably follows that the star is spherically symmetric. However,nobody has yet given a proof.[For proofs under more restricted assumptions,see Avez (l964) and Kunzle (l971).] In the absence of a proof,assume the result: insist that all stars studied be spherical as well as static.

Static stars must be spherical

# S23.2. COORDINATES AND METRIC FOR A STATIC. SPHERICAL SYSTEM

Metric for any static, spherical system:

To deduce the gravitational field for a static spherical star-or for any other static. spherical system--begin with the metric of special relativity (no gravity) in the spherically symmetric form

$$
d s ^ { 2 } = - d t ^ { 2 } + d r ^ { 2 } + r ^ { 2 } d \varOmega ^ { 2 } ,
$$

where

$$
d \Omega ^ { 2 } = d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } .
$$

(1）generalized from flat spacetime

Try to modify this metric to allow for curvature due to the gravitational influence of the star,while preserving spherical symmetry. The simplest and most obvious guess is to allow those metric components that are already non-zero in equation (23.1) to assume different values:

$$
d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + R ^ { 2 } d \Omega ^ { 2 } ,
$$

where $\Phi , \ A ,$ and $R$ are functions of $\pmb { r }$ only.(The static assumption demands $\partial g _ { \mu \nu } / \partial t = 0 .$ To verify that this guess is good,use it in constructing stellar models, and check that the resulting models have the same generality (same set of quantities freely specifiable) as in Newtonian theory and as expected from general physical considerations. An apparently more general metric

$$
d s ^ { 2 } = { } - a ^ { 2 } d t ^ { 2 } - 2 a b d r d t + c ^ { 2 } d r ^ { 2 } + R ^ { 2 } d \Omega ^ { 2 }
$$

actually is not more general in any physical sense. One can perform a coordinate transformation to a new time coordinate $t ^ { \prime }$ defined by

$$
e ^ { \phi } d t ^ { \prime } = a d t + b d r .
$$

By inserting this in equation (23.4),and by defining $e ^ { 2 A } \equiv b ^ { 2 } + c ^ { 2 }$ ,one obtains the postulated line element (23.3), apart from a prime on the t.\*

The necessity to allow for arbitrary coordinates in general relativity may appear burdensome when one is formulating the theory; but it gives an added flexibility, something one should always try to turn to one's advantage when formulating and solving problems. The $g _ { r t } = 0$ simplification (called a coordinate condition) in equation (23.3) results from an advantageous choice of the $t$ coordinate. The $r$ coordinate, however, is also at one's disposal (as long as one chooses it in a way that respects spherical symmetry; thus not $r ^ { \prime } = r + \cos \theta$ ).One can turn this freedom to advantage by introducing a new coordinate $r ^ { \prime } ( r )$ defined by

$$
r ^ { \prime } = R ( r ) .
$$

With this choice of the radial coordinate, and with the primes dropped, equation (23.3） reduces to

$$
d s ^ { 2 } = { } - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + r ^ { 2 } d \Omega ^ { 2 } ,
$$

a line element with just two unknown functions, $\pmb { \phi } ( \pmb { r } )$ and $\boldsymbol { A } ( \boldsymbol { r } )$ .This coordinate system and metric have been used in most theoretical models for relativistic stars since the pioneering work of Schwarzschild (l916b),Tolman (1939),and Oppenheimer and Volkoff (1939). These particular coordinates are sometimes called “curvature coordinates”and sometimes “Schwarzschild coordinates.”The central idea of these coordinates, in a nutshell, is (Schwarzschild $\pmb { r }$ -coordinate) $=$ (proper circumference)/ $n \pi$

For a more rigorous proof that in any static spherical system Schwarzschild coordinates can be introduced, bringing the metric into the simple form (23.7), see Box 23.3 at the end of this chapter.

(3) derived more rigorously

# Exercise 23.1. ISOTROPIC COORDINATES AND NEWTONIAN LIMIT

# EXERCISE

An alternative set of coordinates sometimes used for static,spherical systems is the “isotropic coordinate system” $( t , \widetilde { r } , \theta , \phi )$ . The metric in isotropic coordinates has the form

$$
d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 \mu } [ d \overline { { { r } } } ^ { 2 } + \overline { { { r } } } ^ { 2 } d \Omega ^ { 2 } ] ,
$$

with $\pmb { \phi }$ and $\mu$ being functions of $\widetilde { \pmb { r } } .$

(a)Exhibit the coordinate transformation connecting the Schwarzschild coordinates (23.7) to the isotropic coordinates (23.8).

(b) From equation (l6.2a) [or equivalently (18.15c)],show that, in the Newtonian limit, the metric coefficient $\pmb { \phi }$ of the isotropic line element becomes the Newtonian potential;and $\mu$ becomes equal to $- \tilde { \phi }$ 、By combining with part (a),discover that $\Lambda = r d \tilde { \phi } / d r$ in the Newtonian limit.

# $\$ 23.3$ .PHYSICAL INTERPRETATION OF SCHWARZSCHILD COORDINATES

In general relativity, because the use of arbitrary coordinates is permitted,the physical significance of statements about tensor or vector components and other quantities is not always obvious.There are, however, some situations where the interpretation is almost as straightforward as in special relativity. The most obvious example is the center point of a local inertial coordinate system,where the principle of equivalence allows one to treat all local quantities (quantities not involving spacetime curvature） exactly as in special relativity. Schwarzschild coordinates for a spherical system turn out to be a second example.

One's first reaction when meeting a new metric should be to examine it,not in order to learn about the gravitational field,for which the curvature tensor is more

The form of any metric can reveal the nature of the coordinates being used

directly informative, but to learn about the coordinates. (Are they,for instance, locally inertial at some point?)

Geometric significance of the Schwarzschild coordinates:

(1) $\theta , \phi$ are angles on sphere

The names given to the coordinates have no intrinsic significance.A coordinate transformation $t ^ { \prime } = \theta , r ^ { \prime } = \phi , \theta ^ { \prime } = r , \phi ^ { \prime } = t$ is perfectly permissible,and has no influence on the physics or the mathematics of a relativistic problem. The only thing it affects is easy communication between the investigator who adopts it and his colleagues. Thus the names $t r \theta \phi$ for the Schwarzschild coordinates (23.7） provide a mnemonic device pointing out the geometric content of the coordinates.\* In particular,the names $\theta , \phi$ are justified by the fact that on each two-dimensional surface of constant $r$ and $t$ ，the distance between two nearby events is given by $d s ^ { 2 } = r ^ { 2 } d \varOmega ^ { 2 }$ ,as befits standard $\theta , \phi$ coordinates on a sphere of radius $\boldsymbol { r } ,$ The area of this two-dimensional sphere is clearly

$$
A = \int ( r d \theta ) ( r \sin \theta d \phi ) = 4 \pi r ^ { 2 } ;
$$

(2)r measures surface area of sphere

hence,the metric (23.7) tels how to measure the $r$ coordinate that it employs. One can merely measure (in proper length units) the area $\pmb { A }$ of the sphere, composed of all points rotationally equivalent to the point $\mathcal { P }$ for which the value $r ( \mathcal { P } )$ is desired; and one can then calculate

$$
r ( \mathcal { P } ) = \binom { \mathrm { p r o p e r ~ a r e a ~ o f ~ s p h e r e } } { \mathrm { t h r o u g h ~ p o i n t } ~ \mathcal { P } } 4 \pi \bigg ) ^ { 1 / 2 } .
$$

(3) t has 3 special geometric properties

The Schwarzschild coordinates have been picked for convenience,and not for the ease with which one could build a coordinate-measuring machine. This makes it more difficult to design a machine to measure $t$ than machines to measure $r , \theta , \phi$

The geometric properties of $t$ on which a measuring device can be based are: (l） the time-independent distances $( \partial g _ { \alpha \beta } / \partial t = 0 )$ ）between world lines of constant $r , \theta , \phi ^ { \prime }$ （2）the orthogonality $( g _ { t \tau } = g _ { t \theta } = g _ { t \phi } = 0 )$ of these world lines to the $t =$ constant hypersurfaces；and (3)a labeling of these hypersurfaces by Minkowski (special relativistic) coordinate time at spatial infinity,where spacetime becomes flat. This labeling produces a constraint

$$
\bar { \pmb { \phi } } ( \infty ) = 0
$$

(4) description of a "machine" to measure t

in the metric (23.7).[Mathematically,this constraint is imposed by a simple rescaling transformation $t ^ { \prime } = e ^ { \phi ( \infty ) } t$ ,and by then dropping the prime.]

One“machine” design which constructs (mentally) such a t coordinate, and in the process measures it, is the following. Observers using radar sets arrange to move along the coordinate lines $r , \theta , \phi = \mathrm { c o n s t }$ They do this by adjusting their velocities until each finds that the radar echos from his neighbors,or from“benchmark” reference points in the asymptotically flat space, require the same round-trip time at each repetition. Equivalently, each returning echo must show zero doppler shift;

it must return with the same frequency at which it was sent out. Next a master clock is set up near spatial infinity (far from the star). It is constructed to measure proper time-which, for it, is Minkowski time “at infinity”-and to emit a standard one-Hertz signal. Each observer adjusts the rate of his“coordinate clock”to beat in time with the signals he receives from the master clock.To set the zero of his“coordinate clock,”now that its rate is correct, he synchronizes with the master clock, taking account of the coordinate time At required for radar signals to travel from the master to him.[To compute the transit time, he assumes that for radar signals (treflection - $t _ { \mathrm { e m i s s i o n } } ) = ( t _ { \mathrm { r e t u r n } } - t _ { \mathrm { r e f l e c t i o n } } ) = \varDelta t _ { \mathrm { : } }$ ,so that the echo is obtained by time-inversion about the reflection event. This time-reversal invariance distinguishes the time $t$ in the metric (23.7) from the more general $t$ coordinates allowed by equation (23.4).] Each observer moving along a coordinate line $( r , \theta , \phi =$ const.) now has a clock that measures coordinate time $t$ in his neighborhood.

The above discussion identifies the Schwarzschild coordinates of equation (23.7) by their intrinsic geometric properties. Not only are $r$ and $t$ radial and time variables, respectively (in that $\partial / \partial r$ and $\partial / \partial t$ are spacelike and timelike, respectively, and are orthogonal also to the spheres defined by rotational symmetry), but they have particular properties $\scriptstyle \left[ 4 \pi r ^ { 2 } \right. =$ surface area; $\partial g _ { \mu \nu } / \partial t = 0$ ； $\partial / \partial r \cdot \partial / \partial t = g _ { r t } = 0$ $\partial / \partial t \cdot \partial / \partial t = g _ { t t } = - 1$ at $r = \infty ]$ that distinguish them from other possible coordinate choices $[ r ^ { \prime } = f ( r )$ ， $t ^ { \prime } = t + F ( r ) \}$ . No claim is made that these are the only coordinates that might reasonably be called $r$ and $t$ ；for an alternative choice ("isotropic coordinates"),see exercise 23.1. However,they provide a choice that is reasonable,unambiguous,useful,and often used.

Other coordinates are possible，but Schwarzschild are particularly simple

# \$23.4. DESCRIPTION OF THE MATTER INSIDE A STAR

To high precision, the matter inside any star is a perfect fluid. (Shear stresses are negligible, and energy transport is negligible on a“hydrodynamic time scale.") Thus, it is reasonable in model building to describe the matter by perfect-fluid parameters:

$$
\begin{array} { r l } & { \rho = \rho ( r ) = \mathrm { d e n s i t y ~ o f ~ m a s s - e n e r g y ~ i n ~ r e s t - f r a m e ~ o f ~ f l u i d } ; } \\ & { p = p ( r ) = \mathrm { i s o t r o p i c ~ p r e s s u r e ~ i n ~ r e s t - f r a m e ~ o f ~ f l u i d } ; } \\ & { n = n ( r ) = \mathrm { n u , b e r ~ d e n s i t y ~ o f ~ b a r y o n s ~ i n ~ r e s t - f r a m e ~ o f ~ f l u i d } ; } \end{array}
$$

$u ^ { \mu } = u ^ { \mu } ( r ) = 4$ -velocity of fluid;

$$
T ^ { \mu \nu } = ( \rho + p ) u ^ { \mu } u ^ { \nu } + p g ^ { \mu \nu } = { \mathrm { s t r e s s - e n e r g y ~ t e n s o r ~ o f ~ f l u i d } } .
$$

(For Track-1 discussion,see Box 5.1; for greater Track-2 detail, see $\ S 8 2 2 . 2$ and 22.3.) In order that the star be static, each element of fluid must remain always at rest in the static coordinate system; i.e., each element must move along a world line of constant $r , \theta , \phi$ ； i.e., each element must have 4-velocity components

$$
u ^ { \tau } = d r / d \tau = 0 , \quad \quad u ^ { \theta } = d \theta / d \tau = 0 , \quad \quad u ^ { \phi } = d \phi / d \tau = 0 .
$$

Material inside star to be idealized as perfect fluid

Parameters describing perfect fluid:

(1) $\rho , p , n$

The normalization of 4-velocity,

$$
- 1 = \pmb { u } \cdot \pmb { u } = g _ { \mu \nu } u ^ { \mu } u ^ { \nu } = g _ { t t } u ^ { t } u ^ { t } = - e ^ { 2 \phi } u ^ { t } u ^ { t } ,
$$

then determines $u ^ { t }$

$$
u ^ { t } = d t / d \tau = e ^ { - \phi } , ~ \pmb { \upsilon } = e ^ { - \phi } \partial / \partial t ;
$$

and this, together with the general form (23.12) of the stress-energy tensor and the form (23.7) of the metric, determines $T ^ { \mu \nu }$ ：

$$
\begin{array} { c c c } { { T ^ { 0 0 } = \rho e ^ { - 2 \phi } , } } & { { T ^ { r r } = p e ^ { - 2 A } , } } & { { T ^ { \theta \theta } = p r ^ { - 2 } , } } \\ { { } } & { { } } & { { T ^ { \alpha \beta } = 0 \mathrm { i f } \alpha \not = \beta . } } \end{array} \quad T ^ { \phi \phi } = p r ^ { - 2 } \sin ^ { - 2 } \theta ,
$$

Although these components of the stress-energy tensor in Schwarzschild coordinates are useful for calculations, the normalization factors $e ^ { - 2 \phi } , e ^ { - 2 A } , r ^ { - 2 } , r ^ { - 2 } \sin ^ { - 2 } \theta$ make them inconvenient for physical interpretations. More convenient are components on orthonormal tetrads carried by the fluid elements ("proper reference frames"; see $\ S 1 3 . 6 )$ ：

Proper reference frame of fluid

$$
\pmb { e } _ { \hat { \imath } } \equiv \frac { d } { d \tau } = \frac { 1 } { e ^ { \phi } } \frac { \partial } { \partial t } , \pmb { e } _ { \hat { \imath } } = \frac { 1 } { e ^ { A } } \frac { \partial } { \partial r } , \pmb { e } _ { \hat { \imath } } = \frac { 1 } { r } \frac { \partial } { \partial \theta } , \pmb { e } _ { \hat { \imath } } = \frac { 1 } { r \sin \theta } \frac { \partial } { \partial \phi } ;
$$

$$
\begin{array} { r } { \omega ^ { \hat { t } } = e ^ { \phi } d t , \qquad \omega ^ { \hat { r } } = e ^ { A } d r , \qquad \omega ^ { \hat { \theta } } = r d \theta , \qquad \omega ^ { \hat { \phi } } = r \sin \theta d \phi ; } \end{array}
$$

Components of $\pmb { u }$ and $\pmb { \tau }$ in proper reference frame

$$
\begin{array} { l l l } { { \pmb { u } = \pmb { e } _ { \hat { t } } ; } } & { { ~ \pmb { u } ^ { \hat { t } } = 1 , } } & { { ~ \pmb { u } ^ { \hat { \tau } } = u ^ { \hat { \theta } } = u ^ { \hat { \phi } } = 0 ; } } \end{array}
$$

$$
T _ { \hat { t } \hat { t } } \equiv T _ { \hat { 0 } \hat { 0 } } = \rho , \qquad T _ { \hat { r } \hat { r } } = T _ { \hat { \theta } \hat { \theta } } = T _ { \hat { \phi } \hat { \phi } } = p , \qquad T _ { \hat { \alpha } \hat { \beta } } = 0 \mathrm { ~ i f ~ } \alpha \neq \beta .
$$

See exercise 23.2 below.

The structure of a star--i.e., the set of functions ${ \Phi ( \boldsymbol { r } ) } , \ A ( \boldsymbol { r } ) , \ \rho ( \boldsymbol { r } ) , \ p ( \boldsymbol { r } ) , \ n ( \boldsymbol { r } )$ -is determined in part by the Einstein field equations, $G ^ { \mu \nu } = 8 \pi T ^ { \mu \nu }$ ,and in part by the law of local conservation of energy-momentum in the fluid, $T ^ { \mu \nu } { } _ { ; \nu } = 0$ .However, these are not sufficient to fix the structure uniquely. Also necessary is the functional dependence of pressure $p$ and density $\pmb { \rho }$ on number density of baryons $\pmb { n }$ ：

$$
p = p ( n ) , \qquad \rho = \rho ( n ) .
$$

Equation of state: (1)in general

Normally one cannot deduce $p$ and $\pmb { \rho }$ from a knowledge solely of $\pmb { n }$ . One must know, in addition, the temperature $T$ or the entropy per baryon $\pmb { s }$ ；then the laws of thermodynamics plus equations of state will determine all remaining thermodynamic variables:

$$
p = p ( n , s ) , \rho = \rho ( n , s ) , . . . . .
$$

(2) idealized to "one-parameter form" $p = p ( n ) , \rho = \rho ( n )$ ，

(See $\ S 2 2 . 2$ and $\mathbf { B o x } 2 2 . 1$ for full Track-2 discussions.) To pass from the given thermodynamic knowledge, $p ( n , s )$ and $\rho ( n , s )$ ,to the desired knowledge, $p ( n )$ and $\rho ( n )$ ,one needs information about the star's thermal properties,and especially about the way in which energy-generation plus heat flow have conspired to distribute the entropy, $s = s ( n )$ ：

$$
p ( n ) = p [ n , s ( n ) ] , \qquad \rho ( n ) = \rho [ n , s ( n ) ] .
$$

There exist three important applications of the theory of relativistic stars: neutron stars,white dwarfs,and supermassive stars (stars with $M \gtrsim 1 0 ^ { 3 } M _ { \odot }$ ，which may exist according to theory, but the existence of which has never yet been confirmed by observation). In all three cases, happily, the passage from $\begin{array} { r } { p = p ( n , s ) , \rho ( n , s ) , } \end{array}$ to $p = p ( n )$ ， $\rho = \rho ( n )$ ，is trivial.

Justification for idealized equation of state:

Consider first a neutron star. Though hot by ordinary standards,a neutron star is so cold by any nuclear-matter scale of temperatures that essentially all its thermal degrees of freedom are frozen out ("degenerate gas";“quantum fluid"). It is not important that a detailed treatment of the substance of a neutron star is beyond the capability of present theory (allowance for the interaction between baryon and baryon; production at sufficiently high pressures of hyperons and mesons). The simple fact is that one is dealing with matter at densities comparable to the density of matter in an atomic nucleus $( 2 \times 1 0 ^ { 1 4 } \mathrm { g } / \mathrm { c m } ^ { 3 } )$ and higher. Everything one knows about nuclear matter [see,for example, Bohr and Mottelson (1969)] tells one that it is degenerate, and that one can estimate in order of magnitude its degeneracy temperature by treating it as though it were an ideal Fermi neutron gas. (In a normal atomic nucleus,a little more than 5O per cent of all baryons are neutrons, the rest are protons; in a neutron star, as many as 99 per cent are neutrons.) When approximating the neutron-star matter as an ideal Fermi neutron gas,one considers the neutrons to occupy free-particle quantum states, with two particles of opposite spin in each occupied state, and a sharp drop from lOo per cent occupancy of quantum states to empty states when the particle energy rises to the level of the“Fermi energy” [for more on such an ideal Fermi gas, see Kittel, Section 19 (l958); or at an introductory level, see Sears, Section l6-5 (1953)]. In matter at nuclear density, the Fermi energy is of the order

(1) in neutron stars

$$
E _ { \mathrm { F e r m i } } \sim 3 0 ~ \mathrm { M e V ~ o r } ~ 3 \times 1 0 ^ { 1 1 } \mathrm { K } ;
$$

and at higher density the temperature required to unfreeze the degeneracy is even greater. In other words, for matter at and above nuclear densities, already at zero temperature the kinetic energy of the particles (governed by the Pauli exclusion principle and by their Fermi energy) is a primary source of pressure. Nuclear forces make a large correction to this pressure, but for $T \lesssim 3 0 ~ \mathrm { M e V } = 3 \times 1 0 ^ { 1 1 } \mathrm { K } .$ energies of thermal agitation do not.

A star, in collapsing from a normal state to a neutron-star state (see Chapter 24), emits a huge flux of neutrinos at temperatures $\gtrsim 1 0 ^ { 1 0 } \mathrm { K }$ ，and thereby cools to $T \ll 3 \times 1 0 ^ { 1 1 } \mathrm { K }$ within a few seconds after formation. Consequently, in all neutron stars older than a few seconds one can neglect thermal contributions to the pressure and density; i.e.,one can set

$$
p ( n , s ) = p ( n , s = 0 ) = p ( n ) , \qquad \rho ( n , s ) = \rho ( n , s = 0 ) = \rho ( n ) .
$$

A white dwarf is similar, except that here electrons rather than neutrons are the (2) in white dwarfs source of Fermi gas pressure and degeneracy. Typical white-dwarf temperatures satisfy

$$
k T \leqslant E _ { \mathrm { F e r m i e l e c t r o n s } } ;
$$

the Fermi kinetic energy (Pauli exclusion principle),and not random $k T$ energy, is primarily responsible for the pressure and energy density; and one can set

$$
p ( n , s ) = p ( n , s = 0 ) = p ( n ) , \qquad \varrho ( n , s ) = \rho ( n , s = 0 ) = \rho ( n ) .
$$

(3) in supermassive stars

In a supermassive star (see Chapter 24), the situation is quite different. There temperature and entropy are almost the whole story,so far as pressure and energy density are concerned. However, convection keeps the star stirred up and produces a uniform entropy distribution

so one can write

$$
\begin{array} { r l } & { p ( n , s ) = p _ { s } ( n ) , \qquad \quad \rho ( n , s ) = \rho _ { s } ( n ) . } \\ & { \qquad \quad  \begin{array} { l } { \mathrm { f u n c t i o n s ~ d e p e n d i n g ~ o n } } \\ { \mathrm { u n i f o r m ~ e n t r o p y ~ p e r ~ b a r y o n } , } \\ { s , \mathrm { i n ~ t h e ~ s t a r } } \end{array}  } \end{array}  ^ { \mathrm { ~ \tiny ~ \cdot ~ } }
$$

In all three cases-neutron stars,white dwarfs,supermassive stars-one regards the relations $p ( n )$ and ${ \pmb \rho } ( n )$ as “equations of state";and having specified them, one can calculate the star's structure without further reference to its thermal properties.

# EXERCISE

# Exercise 23.2. PROPER REFERENCE FRAMES OF FLUID ELEMENTS

(a) Verify that equations (23.15a,b)define an orthonormal tetrad and its dual basis of1-forms,   
at each event in spacetime. (b) Verify that the components of the fluid 4-velocity relative to these tetrads are given   
by equations (23.15c). Why do these components guarantee that the tetrads form“proper   
reference frames” for the fluid elements? (c) Verify equations (23.15d) for the components of the stress-energy tensor.

# $\$ 23.5$ .EQUATIONS OF STRUCTURE

Five equations needed to determine 5 stellar-structure functions: $\pmb { \phi }$ A $p$ p.n

The structure of a relativistic star is determined by five functions of radius $r$ the metric functions $\varPhi ( r ) , A ( r )$ ，the pressure $p ( r ) .$ ，the density of mass-energy $\rho ( r )$ and the number density of baryons, $n ( r )$ 、Hence,to determine the structure uniquely, one needs five equations of structure, plus boundary conditions. Two equations of structure, the equations of state $p ( n )$ and $\rho ( n )$ ,are already in hand.The remaining three must be the essential content of the Einstein field equations and of the law of local energy-momentum conservation, $T ^ { \mu \nu } { } _ { ; \nu } = 0$

One knows that the law of local energy-momentum conservation for the fluid follows as an identity from the Einstein field equations.Without loss of information, one can therefore impose all ten field equations and ignore local energy-momentum conservation. But that is an inefficient way to proceed. Almost always the equations $T ^ { \mu \nu } { } _ { ; \nu } = 0$ can be reduced to usable form more easily than can the field equations. Hence, the most efficient procedure is to: (l) evaluate the four equations $T ^ { \mu \nu } { } _ { ; \nu } = 0$ (2) evaluate enough field equations (six) to obtain a complete set $( 6 + 4 = 1 0 )$ ； and (3） evaluate the remaining four field equations as checks of the results of (1) and (2).

The Track-2 reader has learned (S22.3) that the equations $T ^ { \mu \nu } { } _ { ; \nu } = 0$ for a perfect fluid take on an especially simple form when projected (l) on the 4-velocity ${ \pmb u }$ of the fluid itself,and (2) orthogonal to u. Projection along u $( u _ { \mu } { T ^ { \mu \nu } } _ { ; \nu } = 0 )$ gives the local law of energy conservation (22.1la),

The most efficient procedure for solving Einstein equations

$$
\frac { d \rho } { d \tau } = - ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } = \frac { \rho + p } { n } \frac { d n } { d \tau } ,
$$

where $\pmb { \upsilon } = d / d \tau$ ;i.e., $\tau$ is proper time along the world line of any chosen element of the fluid.For a static star, or for any other static system, both sides of this equation must vanish identically (no fluid element ever sees any change in its own density).

Projection of $T ^ { \mu \nu } { } _ { ; \nu } = 0$ orthogonal to $\pmb { u }$ gives the reasonable equation

Equation of hydrostatic equilibrium derived

$$
{ \begin{array} { r l } & { { \mathrm { ( i n e r t i a l ~ m a s s } } } \\ & { { \mathrm { \backslash p e r ~ u n i t ~ v o l u m e } } } \end{array} } ) \cdot { \mathrm { ( 4 - a c c e l e r a t i o n ) } } = \ - ( { \begin{array} { l } { { \mathrm { p r e s s u r e ~ g r a d i e n t , ~ p r o j e c t e d } } } \\ { { \mathrm { p e r p e n d i c u l a r ~ t o ~ } } u } \end{array} } )
$$

i.e.,

$$
( \rho + p ) \pmb { \nabla } _ { \pmb { u } } \pmb { u } = - [ \pmb { \nabla } p + ( \pmb { \nabla } _ { \pmb { u } } p ) \pmb { u } ] .
$$

[see equation (22.13)]. When applied to a static star, this equation tells how much pressure gradient is needed to prevent a fluid element from falling. Only the radial component of this equation has content, since the pressure depends only on $r$ The radial component in.the Schwarzschild coordinate system says [see the line element (23.7) and the 4-velocity components (23.13)],

$$
\begin{array} { c } { { ( \rho + p ) u _ { r ; \nu } u ^ { \nu } = - ( \rho + p ) { \cal T } ^ { \alpha } { } _ { r \nu } u _ { \alpha } u ^ { \nu } = - ( \rho + p ) { \cal T } ^ { 0 } { } _ { r 0 } u _ { 0 } u ^ { 0 } } } \\ { { = ( \rho + p ) \varPhi _ { , r } = - p { } _ { , r } . } } \end{array}
$$

(Track-l readers can derive this from scratch at the end of the section, exercise 23.3.) In the Newtonian limit,Φ becomes the Newtonian potential (since goo = -e2+ = -1 - 2Φ), and the pressure becomes much smaller than the mass-energy density; consequently equation (23.17) becomes

$$
\rho \tilde { \phi } _ { , \tau } = - p _ { , \tau } .
$$

This is the Newtonian version of the equation describing the balance between gravitational force and pressure gradient.

The pressure gradient that prevents a fluid element from falling appears in Einstein's theory as the source of an acceleration. This acceleration, by keeping the fluid element at a fixed $r$ value, causes it to depart from geodesic motion (from “fiducial world line"; from motion of free fall into the center of the star). Newtonian

Comparison of Newton and Einstein views of hydrostatic equilibrium

theory,on the other hand,views as the fducial world line the one that stays at a fixed $r$ value. It regards the “gravitational force” as trying (without success, because balanced by the pressure gradient) to pull a particle from a fixed- $\cdot r$ world line onto a geodesic world line. In the two theories the magnitudes of the acceleration, whether “actually taking place” (Einstein theory） or “trying to take place”(Newtonian theory),are the same to lowest order (but opposite in direction); so it is no surprise that (23.17) and (23.17N) differ only in detail.

Turn next to the Einstein field equation. Here,as is often the case, the components of the field equation in the fuid's orthonormal frame [equations (23.15a,b)] are simpler than the components in the coordinate basis. One already knows the stressenergy tensor $T _ { \hat { \alpha } \hat { \beta } }$ in the orthonormal frame [equation (23.15d)]; and Track-2 readers have already calculated the Einstein tensor $G _ { \hat { \alpha } \hat { \beta } }$ (exercise 14.13; Track-1 readers will face the task at the end of this section, exercise 23.4). All that remains is to equate $G _ { \hat { \alpha } \hat { \beta } }$ t0 $8 \pi T _ { \hat { \alpha } \hat { \beta } }$ . Examine first the O0 component of the field equations:

$$
\begin{array} { r l } & { G _ { \hat { 0 } \hat { 0 } } = r ^ { - 2 } - r ^ { - 2 } e ^ { - 2 A } - r ^ { - 1 } ( d / d r ) ( e ^ { - 2 A } ) } \\ & { \qquad = r ^ { - 2 } ( d / d r ) [ r ( 1 - e ^ { - 2 A } ) ] = 8 \pi T _ { \hat { 0 } \hat { 0 } } = 8 \pi \rho . } \end{array}
$$

This equation becomes easy to solve as soon as one notices that it is a differential equation linear in the quantity $e ^ { - 2 A }$ ； a bit of tidying up then focuses attention on the quantity $r ( 1 - e ^ { - 2 A } )$ . Give this quantity the name $2 m ( r )$ (so far only a name!); thus,

$$
2 m \equiv r ( 1 - e ^ { - 2 A } ) ; ~ e ^ { 2 A } = ( 1 - 2 m / r ) ^ { - 1 } .
$$

In this notation the O0 component of the Einstein tensor becomes

$$
G _ { \hat { 0 } \hat { 0 } } = \frac { 2 } { r ^ { 2 } } \frac { d m ( r ) } { d r } = 8 \pi \rho .
$$

Integrate and find

$$
m ( r ) = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \rho d r + m ( 0 ) .
$$

For the constant of integration $m ( 0 )$ ,a zero value means a space geometry smooth at the origin (physically acceptable); a non-zero value means a geometry with a singularity at the origin (physically unacceptable: no local Lorentz frame at $r = 0$ ：

$$
\begin{array} { r l r } { d s ^ { 2 } = [ 1 - 2 m ( 0 ) / r ] ^ { - 1 } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) } \\ { } & { } & { \approx - [ r / 2 m ( 0 ) ] d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ~ \mathrm { a t } r \approx 0 \mathrm { i f } m ( 0 ) \ne 0 ; } \\ { } & { } & { d s ^ { 2 } = [ 1 - ( 8 \pi / 3 ) \rho _ { c } r ^ { 2 } ] ^ { - 1 } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) } \\ { } & { } & { \approx d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ~ \mathrm { a t } r \approx 0 \mathrm { i f } m ( 0 ) = 0 . } \end{array}
$$

The quantity $m ( r )$ ，defined by equation (23.18) and calculated from equation (23.19) with $m ( 0 ) = 0$ ,is a relativistic analog of the“mass-energy inside radius $r$ ” Box 23.1 spells out the analogy in detail.

# Box 23.1 MASS-ENERGY INSIDE RADIUS r

The total mass-energy $M$ of an isolated star is well-defined (Chapter l9). But not well-defined,in general, is the distribution of that mass-energy from point to point inside the star and in its gravitational field (no unique “gravitational stress-energy tensor"). This was the crucial message of $\ S 2 0 . 4$ (Track 2).

The message is true-in general.But for the case of a spherical star-and only for that case-the message loses its bite. Spherical symmetry allows one to select a distribution of the total mass-energy that is physically reasonable.In Schwarzschild coordinates, it is defined by

$$
{ } ^ { \mathrm { * } } \mathrm { t o t a l ~ m a s s - e n e r g y ~ i n s i d e ~ r a d i u s ~ } r ^ { \prime } \equiv m ( r ) = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \rho ~ d r .
$$

The fully convincing argument for this definition is found only by considering a generalization of it to time-dependent spherically symmetric stars (pulsating, collapsing,or exploding stars; see Chapters 26 and 32,and especially exercise 32.7). For them one finds that the mass-energy m associated with a given ball of matter (fixed baryon number) can change in time only to the extent that locally measurable energy fluxes can be detected at the boundary of the ball.[Such energy fluxes could be the power expended by pressure forces against the moving boundary surface, or heat fluxes,or radiation (photon or neutrino) fluxes.But since spherically symmetric gravitational waves do not exist (Chapters 35 and 36), neither physical intuition nor Einstein's equations require that problems oflocalizing gravitational-wave energy be faced.] Thus the energy m is localized, not by a mathematical convention, but by the circumstance that transfer of energy (with this definition of $m$ ）is detectable by local measurements.[For the mathematical details of $m ( r , t )$ in the time-dependent case,see Misner and Sharp (1964), Misner (l965),and exercise 32.7.]

In addition to the critical “local energy flux” property of $m ( r )$ described above, there are three further properties that verify its identification as mass-energy. They are:(l） Everywhere outside the star

$$
m ( r ) = M \equiv { \binom { \mathrm { t o t a l ~ m a s s - e n e r g y ~ o f ~ s t a r ~ a s ~ m e a s u r e d ~ f r o m } } { \mathrm { K e p l e r ' s ~ t h i r d ~ l a w ~ f o r ~ d i s t a n t ~ p l a n e t s } } } ;
$$

see $\ S 2 3 . 6$ for proof. (2) For a Newtonian star, where “mass inside radius $r ^ { , , }$ has a unique meaning, $m ( r )$ is that mass.(3) For a relativistic star, $m ( r )$ splits nicely into “rest mass-energy" $m _ { 0 } ( r )$ plus “internal energy” $U ( r )$ plus “gravitational potential energy” $\varOmega ( r )$

To recognize and appreciate the split

$$
m ( r ) = m _ { 0 } ( r ) + U ( r ) + \varOmega ( r ) ,
$$

proceed as follows. First split the total density of mass-energy, $\pmb { \rho }$ , into a part $\mu _ { 0 } n$ due to rest mass--where $\mu _ { 0 }$ is the average rest mass of the baryonic species pres-


<!-- chunk 0010: pages 631-700 -->
# Box 23.1 (continued)

ent-and a part ρ - μon due to internal thermal energy,compressional energy, etc. Next notice that the proper volume of a shell of thickness $d r$ is

$$
d \mathcal { V } = 4 \pi r ^ { 2 } ( e ^ { \cal A } d r ) = 4 \pi r ^ { 2 } ( 1 - 2 m / r ) ^ { - 1 / 2 } d r ,
$$

not $4 \pi r ^ { 2 } d r$ .Consequently,the total rest mass inside radius $r$ is

$$
m _ { 0 } = \int _ { 0 } ^ { r } \mu _ { 0 } n d \mathcal { V } = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } ( 1 - 2 m / r ) ^ { - 1 / 2 } \mu _ { 0 } n d r ,
$$

and the total internal energy is

$$
U = \int _ { 0 } ^ { r } { \left( \rho - \mu _ { 0 } n \right) d \mathcal { V } } = \int _ { 0 } ^ { r } { 4 \pi r ^ { 2 } ( 1 - 2 m / r ) ^ { - 1 / 2 } ( \rho - \mu _ { 0 } n ) d r } .
$$

Subtract these from the total mass-energy, $m$ ; the quantity that is left must be the gravitational potential energy,

$$
\begin{array} { r l r } {  { \mathcal { Q } = - \int _ { 0 } ^ { \tau } \rho [ ( 1 - 2 m / r ) ^ { - 1 / 2 } - 1 ] 4 \pi r ^ { 2 } d r } } \\ & { } & \\ & { \approx - \int _ { 0 } ^ { \tau } ( \rho m / r ) 4 \pi r ^ { 2 } d r . } \\ & { } & { \hat { \big \downarrow } _ { [ \mathrm { N e w t o n i a n \ l i m i t } , m / r \ll 1 ] } . } \end{array}
$$

(See exercise 23.7.)

Turn next to the $\hat { r } \hat { r }$ component of the field equations:

$$
\begin{array} { r l } & { G _ { \hat { r } \hat { r } } = - r ^ { - 2 } + r ^ { - 2 } e ^ { - 2 A } + 2 r ^ { - 1 } e ^ { - 2 A } d \varPhi / d r } \\ & { \qquad = 8 \pi T _ { \hat { r } \hat { r } } = 8 \pi p . } \end{array}
$$

Solving this equation for the derivative of $\pmb { \phi }$ ,and replacing $e ^ { - 2 A }$ by $1 - 2 m / r .$ one obtains an expression for the gradient of the potential $\pmb { \phi }$ ：

$$
\frac { d \phi } { d r } = \frac { m + 4 \pi r ^ { 3 } p } { r ( r - 2 m ) } .
$$

This expression reduces to the familiar formula

$$
d \Phi / d r = m / r ^ { 2 }
$$

in the Newtonian limit.

In most studies of stellar structure,one replaces equation (23.17) by the equivalent equation obtained with the help of (23.21),

$$
\frac { d p } { d r } = - \frac { ( \rho + p ) ( m + 4 \pi r ^ { 3 } p ) } { r ( r - 2 m ) } .
$$

Equation of hydrostatic equilibrium rewritten in "ov" form

This is called the Oppenheimer-Volkoff (OV) equation of hydrostatic equilibrium. Its Newtonian limit,

$$
d p / d r = - \rho m / r ^ { 2 } ,
$$

is familiar.

Compare two stellar models,one relativistic and the other Newtonian. Suppose that at a given radius $r$ [determined in both cases by (proper area) $\mathbf { \varepsilon } = 4 \pi r ^ { 2 } ]$ ,the two configurations have the same values of $\pmb \rho , p _ { \mathrm { : } }$ and $m$ .Then in the relativistic model the pressure gradient is

$$
{ \begin{array} { r l } { { \frac { d p } { d ( { \mathrm { p r o p e r ~ r a d i a l ~ d i s t a n c e } } ) } } = { \frac { d p } { e ^ { A } d r } } } \\ & { = - { \frac { ( \rho + p ) ( m + 4 \pi r ^ { 3 } p ) } { r ^ { 2 } ( 1 - 2 m / r ) ^ { 1 / 2 } } } . } \end{array} }
$$

In contrast, Newtonian theory gives for the pressure gradient

$$
{ \frac { d p } { d ( { \mathrm { p r o p e r ~ r a d i a l ~ d i s t a n c e } } ) } } = { \frac { d p } { d r } } = - { \frac { \rho m } { r ^ { 2 } } } .
$$

The relativistic expression for the gradient is larger than the Newtonian expresion (l） because the numerator is larger (added pressure term in both factors） and (2) because the denominator is smaller [shrinkage factor $( 1 - 2 m / r ) ^ { 1 / 2 } ]$ . Therefore, as one proceeds deeper into the star, one finds pressure rising faster than Newtonian gravitation theory would predict. Moreover,this rise in pressure is in a certain sense “self-regenerative."The more the pressure goes up, the larger the pressure-correction terms become in the numerator of (23.23);and the larger these terms become, the faster is the further rise of the pressure as one probes still deeper into the star. The geometric factor $[ 1 - 2 m ( r ) / r ] ^ { 1 / 2 }$ in the denominator of (23.23) further augments this regenerative rise of pressure towards the center. It is appropriate to summarize the situation in short-hand terms by saying that general relativity predicts stronger gravitational forces in a stationary body than does Newtonian theory. These forces, among their other important effects, can pull certain white-dwarf stars and supermassive stars into gravitational collapse under circumstances (see Chapter 24) where Newtonian theory would have predicted stable hydrostatic equilibrium. As the most elementary indication that a new factor has surfaced in the analysis of stability,note that no star in hydrostatic equilibrium can ever have $2 m ( r ) / r \geq 1$ (see Box 23.2 for one illustration and $\ S 2 3 . 8$ for discussion),a phenomenon alien to Newtonian theory.

Comparison of pressure gradients in Newtonian and relativistic stars

Now in hand are five equations of structure [two equations of state (23.16); equation (23.19), expressing $m ( r ) = { \frac { 1 } { 2 } } r ( 1 - e ^ { - 2 A } )$ as a volume integral of $\pmb { \rho }$ ; the source

# Equations of stellar structure summarized

equation (23.21) for $\pmb { \phi }$ ; and the OV equation of hydrostatic equilibrium (23.22)] for the five structure functions $\qquad \rho , p , n , \phi , A .$ If the theory of relativistic stars as outlined above is well posed, then each of the remaining eight Einstein field equations $G _ { \hat { \alpha } \hat { \beta } } = 8 \pi T _ { \hat { \alpha } \hat { \beta } }$ must be either vacuous $( ^ { 6 4 } 0 = 0 ^ { 9 9 } ,$ ，or must be a consequence of the five equations of structure.This is,indeed,the case, as one can verify by straightforward but tedious computations.

To construct a stellar model, one needs boundary conditions as well as structure equations. To facilitate the presentation of boundary conditions,the next section will examine the star's external gravitational feld.

# EXERCISES

# Exercise 23.3. LAW OF LOCAL ENERGY-MOMENTUM CONSERVATION (for readers who have not studied Chapter 22)

$T ^ { \alpha \beta } { } _ { ; \beta } = 0$ 3.149 $T ^ { \prime \beta } { } _ { ; \beta } = 0$ a nonvacuous result; it gives equation (23.17).]

# Exercise 23.4. EINSTEIN CURVATURE TENSOR (for readers who have not studied Chapter 14)

Calculate the components of the Einstein curvature tensor, $G _ { \alpha \beta }$ ,in Schwarzschild coordinates. Then perform a transformation to obtain $G _ { \hat { \alpha } \hat { \beta } }$ ,the components in the orthonormal frame of equations (23.15a,b). [See Box 8.6,or Box 14.2 and equation (14.7).]

# Exercise 23.5. TOTAL NUMBER OF BARYONS IN A STAR

Show that, if $r = R$ is the location of the surface of a static star, then the total number of baryons inside the star is

$$
A = \int _ { \eta } ^ { R } 4 \pi r ^ { 2 } n e ^ { \varLambda } d r .
$$

[Hint: See the discussion of m in Box 23.1.]

# Exercise 23.6. BUOYANT FORCE IN A STAR

Anobserver at rest at some point inside a relativistic star measures the radial pressure-buoyant force, $F _ { \mathrm { b u o y } }$ , on a small fluid element of volume $V .$ Let him use the usual laboratory techniques.Do not confuse him by telling him he is in a relativistic star.What value will he find for $F _ { \mathrm { b u o y } } \mathrm { ; }$ in terms of $\rho , p , m , V ,$ and $d p / d r ?$ If he equates this buoyant force to an equal and opposite gravitational force, $F _ { \mathrm { g r a v } } ,$ what will $F _ { \mathrm { g r a v } }$ be in terms of $\rho , p , m , V ,$ and $r ?$ (Use equation 23.22.) How do these results differ from the corresponding Newtonian results?

# ExerciSe 23.7. GRAVITATIONAL ENERGY OF A NEWTONIAN STAR

Calculate in Newtonian theory the energy one would gain from gravity if one were to construct a star by adding one spherical shell of matter on top of another,working from the inside outward. Use Laplace's equation $( r ^ { 2 } \Phi _ { , r } ) _ { , r } = 4 \pi r ^ { 2 } \rho$ and the equation of hydrostatic equilibrium $p _ { , \mathsf { r } } = - \rho \Phi _ { , \mathsf { r } }$ to put the answer in the following equivalent forms:

$$
\begin{array} { l } { { \displaystyle = \int _ { 0 } ^ { R } ( \rho r \dot { \phi } _ { , \ast } ) 4 \pi r ^ { 2 } d r = \int _ { 0 } ^ { R } ( \rho m / r ) 4 \pi r ^ { 2 } d r } } \\ { { \displaystyle = - \frac { 1 } { 2 } \int _ { 0 } ^ { R } ( \rho \phi ) 4 \pi r ^ { 2 } d r = \frac { 1 } { 8 \pi } \int _ { 0 } ^ { \infty } ( \dot { \phi } _ { , r } ) ^ { 2 } 4 \pi r ^ { 2 } d r } } \\ { { \displaystyle = 3 \int _ { 0 } ^ { R } 4 \pi r ^ { 2 } p d r . } } \end{array}
$$

# $\$ 23.6$ .EXTERNAL GRAVITATIONAL FIELD

Outside a star the density and pressure vanish,so only the metric parameters $\pmb { \phi }$ and $\begin{array} { r } { A = - { \frac { 1 } { 2 } } \ln \left( 1 - 2 m / r \right) } \end{array}$ need be considered.From equation (23.l9) one sees that “the mass inside radius $r ; m ( r )$ ,stays constant for values of $r$ greater than $R$ (outside the star). Its constant value is denoted by $M$ ：

$$
m ( r ) = M \qquad \mathrm { f o r } \ r > K \ ( \mathrm { i . e . , \ o u t s i d e \ t h e \ s t a r } ) .
$$

By integrating equation (23.21） with $p = 0$ and $m = M$ ，and by imposing the boundary condition (23.10） on $\pmb { \phi }$ at $r = \infty$ ("normalization of scale of time at $r = \infty "$ ,one finds

$$
\phi ( r ) = \frac 1 2 \ln ( 1 - 2 M / r ) \qquad \mathrm { f o r } \ r > R .
$$

Consequently, outside the star the spacetime geometry (23.7) becomes

$$
d s ^ { 2 } = - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { ( 1 - 2 M / r ) } } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

This is called the “Schwarzschild geometry” or“Schwarzschild gratitational field” or “Schwarzschild line element,” because Karl Schwarzschild (1916a) discovered it as an exact solution to Einstein's field equations a few months after Einstein formulated general relativity theory.

In that region of spacetime, $r \gg 2 M$ ,where the geometry is nearly flat, Newton's theory of gravity is valid,and the Newtonian potential is

$$
{ \phi } = - M / r \qquad \mathrm { f o r } \ r > R , r \gg 2 M .
$$

Spacetime outside star possesses ''Schwarzschild" geometry

Consequently, $M$ is the mass that governs the Keplerian motions of planets in the distant, Newtonian gravitational field-i.e., it is the star's “total mass-energy" (see Chapters 19 and 20). Since the metric (23.27) far outside the star is precisely diagonal $( g _ { t j } \equiv 0 )$ ,the star's total angular momentum must vanish. This result accords with the absence of internal fluid motions.

Total mass-energy of star

# $\$ 23.7$ . HOW TO CONSTRUCT A STELLAR MODEL

The equations of stellar structure (23.16),(23.19),(23.21),(23.22),and associated boundary conditions (to be discussed below),all gathered together along with the line element, read as follows.

# Line Element

$$
\begin{array} { l } { { d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + \frac { d r ^ { 2 } } { 1 - 2 m / r } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) } } \\ { { \mathrm { ~ } = - \left( 1 - \frac { 2 M } { r } \right) d t ^ { 2 } + \frac { d r ^ { 2 } } { 1 - 2 M / r } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) \mathrm { ~ f o r ~ } r > R . } } \end{array}
$$

# Mass Equation

$$
m = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \rho \ d r , \mathrm { w i t h } \ m ( r = 0 ) = 0 .
$$

# OV Equation of Hydrostatic Equilibrium

$$
\frac { d p } { d r } = - \frac { ( \rho + p ) ( m + 4 \pi r ^ { 3 } p ) } { r ( r - 2 m ) } , \mathrm { w i t h } p ( r = 0 ) = p _ { c } = \mathrm { c e n t r a l ~ p r e s s u r e } .
$$

Equations of State

$$
\begin{array} { r } { p = p ( n ) , } \\ { \rho = \rho ( n ) . } \end{array}
$$

# Source Equation for $\pmb { \phi }$

$$
\frac { d \phi } { d r } = \frac { ( m + 4 \pi r ^ { 3 } p ) } { r ( r - 2 m ) } , \qquad \mathrm { w i t h } \ \phi ( r = R ) = \frac 1 2 \ln { ( 1 - 2 M / R ) } .
$$

How to solve the equations of stellar structure

To construct a stellar model one can proceed as follows.First specify the equations of state (23.28c,d) and a value of the central pressure, $p _ { c }$ Also specify an arbitrary (later to be renormalized) value, $\pmb { \phi } _ { 0 }$ for ${ \pmb \phi } ( r = 0 )$ . The boundary conditions $p ( r = 0 ) = p _ { c } , \varPhi ( r = 0 ) = \varPhi _ { 0 } , m ( r = 0 ) = 0$ are sufficient to determine uniquely the solution to the coupled equations (23.28). Integrate these coupled equations outward from $r = 0$ until the pressure vanishes.[The OV equation,(23.28b),guarantees that the pressure will decrease monotonically so long as the equations of state obey the reasonable restriction ${ \pmb \rho } \ge 0$ for all $p \geq 0$ ] The point at which the pressure reaches zero is the star's surface;the value of $r$ there is the star's radius, $R$ ; and the value of $m$ there is the star's total mass-energy, $M .$ Having reached the surface,renormalize $\pmb { \phi }$ by adding a constant to it everywhere, so that it obeys the boundary condition (23.28e). The result is a relativistic stellar model whose structure functions $\delta , m ,$ $\rho , p$ ， $\pmb { n }$ satisfy the equations of structure.

Notice that for any fixed choice of the equations of state $p = p ( n )$ ， $\rho = \rho { \left( n \right) }$ ,the stellar models form a one-parameter sequence (parameter $p _ { c } )$ .Once the central pressure has been specified,the model is determined uniquely.

The next chapter describes a variety of realistic stellar models constructed numer-ically by the above prescription. For an idealized stellar model constructed analytically,see Box 23.2.

# Exercise 23.8. NEWTONIAN STARS OF UNIFORM DENSITY

# EXERCISE

Calculate the structures of uniform-density configurations in Newtonian theory. Show that the relativistic configurations of $\mathtt { B o x } 2 3 . 2$ become identical to the Newtonian configurations in the weak-gravity limit. Also show that there are no mass or radius limits in Newtonian theory.

(continued on page 612)

# Box 23.2 RELATIVISTIC MODEL STAR OF UNIFORM DENSITY

For realistic equations of state (see next chapter), the equations of stellar structure (23.28) cannot be integrated analytically; numerical integration is necessary.However,analytic solutions exist for various idealized and ad hoc equations of state. One of the most useful analytic solutions [Karl Schwarzschild (19i6b)] describes a star of uniform density,

$$
\rho = \rho _ { 0 } = { \mathrm { c o n s t a n t ~ f o r ~ a l l } } \ p .
$$

It is not necessary to indulge in the fiction of “an incompressible fluid” to accept this model as interesting. Incompressibility would imply a speed of sound, $v = ( d p / d \rho ) ^ { 1 / 2 }$ ,of unlimited magnitude, therefore in excess of the speed of light, and therefore in contradiction with a central principle of special relativity("principle of causality") that no physical effect can be propagated at a speed $v > 1$ (If a source could cause an effect so quickly in one local Lorentz frame,then there would exist another local Lorentz frame in which the effect would occur before the source had acted!) However, that the part of the fluid in the region of high pressure has the same density as the part of the fluid in the region of low pressure is an idea easy to admit, if only one thinks of the fluid having a composition that varies from one r value to another ("hand-tailored"). Whether one thinks along this line,or simply has in mind a globe of water limited in size to a small fraction of the dimensions of the earth, one has in Schwarzschild's model an instructive example of hydrostatics done in the framework of Einstein's theory.

The mass equation (23.28a) gives immediately

$$
m = \left\{ { \begin{array} { l l } { ( 4 \pi / 3 ) \rho _ { 0 } r ^ { 3 } \quad } & { \mathrm { f o r } r < R } \\ { M = ( 4 \pi / 3 ) \rho _ { 0 } R ^ { 3 } \quad } & { \mathrm { f o r } r > R } \end{array} } \right\} ,
$$

from which follows the length-correction factor in the metric

$$
{ \frac { d ( \mathrm { p r o p e r ~ d i s t a n c e } ) } { d r } } = e ^ { A } = [ 1 - 2 m ( r ) / r ] ^ { - 1 / 2 } .
$$

When for ease of visualization the space geometry $( r , \phi )$ of an equatorial slice through the star is viewed as embedded in a Euclidean 3-geometry $( z , r , \phi )$ [see $\ S 2 3 . 8 ]$ ,the “lift” out of the plane $z = 0$ is

$$
\begin{array}{c} z ( r ) = \{ ( R ^ { 3 } / 2 M ) ^ { 1 / 2 } [ 1 - ( 1 - 2 M r ^ { 2 } / R ^ { 3 } ) ^ { 1 / 2 } ] \quad \mathrm { ~ f o r ~ } r \leq R ,  \qquad \\ { ( R ^ { 3 } / 2 M ) ^ { 1 / 2 } [ 1 - ( 1 - 2 M / R ) ^ { 1 / 2 } ] + [ 8 M ( r - 2 M ) ] ^ { 1 / 2 } - [ 8 M ( R - 2 M ) ] ^ { 1 / 2 } + { \cal O } ( R ^ { 3 } ) , } \\ { \qquad \quad \mathrm { ~ f o r ~ } r \geq R . \qquad } \end{array} 
$$

The knowledge of $m ( r )$ from (2） allows the equation of hydrostatic equilibrium (23.28b) to be integrated to give the pressure:

$$
p = \rho _ { 0 } \bigg \{ \frac { ( 1 - 2 M r ^ { 2 } / R ^ { 3 } ) ^ { 1 / 2 } - ( 1 - 2 M / R ) ^ { 1 / 2 } } { 3 ( 1 - 2 M / R ) ^ { 1 / 2 } - ( 1 - 2 M r ^ { 2 } / R ^ { 3 } ) ^ { 1 / 2 } } \bigg \} \mathrm { ~ f o r ~ } r < R .
$$

The pressure in turn leads via (23.28e) to the time-correction factor in the metric.

$$
\frac { d ( \mathrm { p r o p e r ~ t i m e } ) } { d t } = e ^ { \phi } = \left\{ \begin{array} { l l } { \displaystyle \frac { 3 } { 2 } \bigg ( 1 - \frac { 2 M } { R } \bigg ) ^ { 1 / 2 } - \frac { 1 } { 2 } \bigg ( 1 - \frac { 2 M r ^ { 2 } } { R ^ { 3 } } \bigg ) ^ { 1 / 2 } } & { \mathrm { f o r ~ } r < R } \\ { \displaystyle ( 1 - 2 M / r ) ^ { 1 / 2 } } & { \mathrm { f o r ~ } r > R } \end{array} \right\} .
$$

Several features of these uniform-density configurations are noteworthy. (l) For fixed energy density, $\rho _ { 0 } .$ ， the central pressure

$$
p _ { c } = \rho _ { 0 } \bigg \{ \frac { 1 - ( 1 - 2 M / R ) ^ { 1 / 2 } } { 3 ( 1 - 2 M / R ) ^ { 1 / 2 } - 1 } \bigg \} ,
$$

increases monotonically as the radius, $R$ ,increases-and, hence,also as the mass, $M = ( 4 \pi / 3 ) \rho _ { 0 } R ^ { 3 }$ , and the ratio ("strength of gravity")

$$
2 M / R = ( 8 \pi / 3 ) \rho _ { 0 } R ^ { 2 }
$$

increase. This is natural, since,as more and more matter is added to the star,a greater and greater pressure is required to support it. (2) The central pressure becomes infinite when $M , R ,$ and $2 M / R$ reach the limiting values

$$
\begin{array} { c } { { R _ { \mathrm { { l i m } } } = ( 9 / 4 ) M _ { \mathrm { { l i m } } } = ( 3 \pi \rho _ { 0 } ) ^ { - 1 / 2 } , } } \\ { { ( 2 M / R ) _ { \mathrm { { l i m } } } = 8 / 9 . } } \end{array}
$$

No star of uniform density can have a mass and radius exceeding these limits. These limits are purely relativistic phenomena; no such limits occur in Newtonian theory. (3) Inside the star the space geometry (geometry of a hypersurface t= constant) is that of a three-dimensional spherical surface with radius of curvature

$$
a = ( 3 / 8 \pi \rho _ { 0 } ) ^ { 1 / 2 } .
$$

[See equation (4), above.] Outside the star the (Schwarzschild) space geometry is that of a three-dimensional paraboloid of revolution. The interior and exterior geometries join together smoothly. Allthese details are shown in the following three diagrams. There allquantities are given in the following geometric units (to convert mass in g or density in g/cm³ into mass in cm or density in cm-²,multiply by $0 . 7 4 2 \times 1 0 ^ { - 2 8 } \mathrm { c m / g ) }$ : lengths, in units $( 3 / 8 \pi \rho _ { 0 } ) ^ { 1 / 2 }$ ; pressure, in units $\pmb { \rho _ { 0 } }$ mass,in units $( 3 / 3 2 \pi \rho _ { 0 } ) ^ { 1 / 2 }$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0010_pages_0631-0700/auto/images/c1f75bf85ed24c13e05c32c24c0d93dcb77679e5a6846471e2a6cc7962e017c6.jpg)

# Box 23.2 (continued)

The mass“after assembly” is what is called $M .$ The mass of the same fluid, dispersed in droplets at infinite separation,is called $M _ { \mathrm { b e f o r e } }$ in the following table.

<table><tr><td>Mbefore</td><td>small</td><td>0.0882</td><td>0.894</td><td>1.0913</td><td>1.374</td></tr><tr><td>1</td><td>small</td><td>0.0828</td><td>0.636</td><td>0.729</td><td>0.838 （critical）</td></tr><tr><td>Difference (binding):</td><td>M3/3</td><td>0.0054</td><td>0.258</td><td>0.362</td><td>0.536</td></tr></table>

Surface area of spheres, $4 \pi r ^ { 2 }$ ：

(1）increases monotonically from center of star outward

# \$23.8. THE SPACETIME GEOMETRY FOR A STATIC STAR

For a highly relativistic star,the spacetime geometry departs strongly from Euclid-Lorentz flatness. Consequently, there is no a priori reason to expect that the surface area ${ \pmb q } _ { \pi r ^ { 2 } }$ ，and hence also the radial coordinate $r _ { \mathrm { { ; } } }$ ，will increase monotonically as one moves from the center of the star outward. Fortunately,the equations of stellar structure guarantee that r will increase monotonically from O at the star's center to o at an infinite distance away from the star, so long as $\rho \geq 0$ and so long as the star is static (equilibrium).

The monotonicity of $r$ can be seen as follows. Introduce as a new radial coordinate proper distance, $\ell$ ,from the center of the star.By virtue of expression (23.27') for the metric,l and $r$ are related by

$$
d r = \pm ( 1 - 2 m / r ) ^ { 1 / 2 } d \ell .
$$

Note that $r$ is zero at the center of the star (where $m \propto r ^ { 3 } .$ ,and note that $r$ is always nonnegative by definition. Therefore $r$ must at first increase with $\ell$ as one moves outward from $\ell = 0$ ； $r ( \ell )$ can later reach a maximum and start decreasing only at a point where $2 m / r$ becomes unity [see equation (23.29)]. Such a behavior can and does happen in a closed model universe,a 3-sphere of uniform density and radius $^ a$ ,where

$$
r ( \ell ) = a \sin \left( \ell / a \right)
$$

[see Chapter 27; especially the embedding diagram of Box 27.2(A)]. However, the field equations demand that such a system be dynamic. Here,on the contrary, attention is limited to a system where conditions are static.In such a system, the condition of hydrostatic equilibrium (23.28b) applies. Then the pressure gradient is given by an expression with the factor $[ 1 - 2 m ( r ) / r ]$ in its denominator. If $2 m / r$ approaches unity with increasing l in some region of the star, the pressure gradient there becomes so large that one comes to the point $p = 0$ (surface of the star) before one comes to any point where $2 m ( r ) / r$ might attain unit value. Moreover,after the surface of the star is passed, $m$ remains constant, $m ( r ) = M ,$ and $2 m ( r ) / r$ decreases. Consequently, $2 m / r$ is always less than unity; and $r ( \ell )$ cannot have a maximum, Q.E.D. (Details of the proof are left to the reader as exercise 23.9.)

Although the radii of curvature, $\boldsymbol { r }$ ,and corresponding spherical surface areas, ${ \pmb q } _ { \pi r ^ { 2 } }$ ， increase monotonically from the center of a star outward, they do not increase at the same rate as they would in flat spacetime.In flat spacetime the rate of increase is given by $d r / d ($ proper radial distance) $= d r / d \ell = 1$ .In a star it is given by $d r / d \ell = ( 1 - 2 m / r ) ^ { 1 / 2 } < 1$ 、Consequently,if one were to climb a long ladder outward from the center of a relativistic star, measuring for each successive spherical shell its Schwarzschild $\boldsymbol { r }$ value ("proper circumference" $2 \pi$ )，one would find these $r$ values to increase surprisingly slowly.

(2) but increases more slowly than in flat spacetime

This strange behavior is most easily visualized by means of an “embedding diagram.” It would be too much for any easy visualization if one were to attempt to embed the whole curved four-dimensional manifold in some higher-dimensional flat space.[See, however,Fronsdal (1959) and Clarke (1970) for a global embedding in $5 + 1$ dimensions,and Kasner(1921b) for a local embedding in $4 + 2$ dimensions. One can never embed a non-fiat, vacuum metric $( G _ { \mu \nu } = 0 )$ in a fiat space of 5 dimensions (Kasner,192lc).] Therefore seek a simpler picture (Flamm l9i6). Space at one time in the context of a static system has the same 3-geometry as space at another time. Therefore, depict 3-space only as it is at one time, $t = c o n s t a n t$ Moreover, at any one time the space itself has spherical symmetry. Consequently, one slice through the center, $r = 0$ ,that divides the space symmetrically into two halves (for example, the equatorial slice, $\theta = \pi / 2$ )has the same 2-geometry as any other such slice (any selected angle of tilt, at any azimuth) through the center. Therefore limit attntion to the 2-geometry of the equatorial slice. The geometry on this slice is described by the line element

# Embedding of spacetime in a flat space of higher dimensionality

$$
d s ^ { 2 } = [ 1 - 2 m ( r ) / r ] ^ { - 1 } d r ^ { 2 } + r ^ { 2 } d \phi ^ { 2 } .
$$

Now one may embed this two-dimensional curved-space geometry in the flat geometry of a Euclidean three-dimensional manifold.

If the curvature of the two-dimensional slice is zero or negligible,the embedding is trivial. In this event, identify the 2-geometry with the slice $z = 0$ of the Euclidean 3-space. Moreover, introduce into that 3-space the familiar cylindrical coordinates $z , r , \phi ,$ ，that one employs for any problem with axial symmetry (see Fig. 23.1 and $\mathbf { B o x } 2 3 . 2$ for more detail). Then one recognizes the flat two-dimensional slice as the set of points of the Euclidean-space with $z = 0$ with $\phi$ running from O to $2 \pi$ and $r$ from 0 to $\infty$ . One has identified the $r$ and $\phi$ of the slice with the $r$ and $\phi$ of the Euclidean 3-space.

If the 2-geometry is curved,as it is when the equatorial section is taken through a real star, then maintain the identification between the $r , \phi ,$ ，of the slice and the $r , \phi ,$ ,of the Euclidean 3-geometry,but bend up the slice out of the plane $z = 0$ (except at the origin, $r = 0 \AA$ ).At the same time,insist that the bending be axially symmetric. In other words,require that the amount of the “lift”above the plane $z = 0$ shall

Construction of "embedding diagram"for equatorial slice through star

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0010_pages_0631-0700/auto/images/11ad181bd99409885f69a27afd33eed9bc9a2ac442a3be97efa1698036671d86.jpg)  
Figure 23.1. Geometry within(grey) and around (white) a star of radius $R = 2 . 6 6 M ,$ 、schematically displayed.The star is in hydrostatic equilibrium and has zero angular momentum (spherical symmetry). The twodimensionai geometry

$$
d s ^ { 2 } = \{ 1 - 2 m ( r ) / r \} ^ { - 1 } d r ^ { 2 } + r ^ { 2 } d \phi ^ { 2 }
$$

of an equatorial slice through the star $( \pmb \theta = \pi / 2$ ， $t =$ constant) is represented as embedded in Euclidean 3-space,in such a way that distances between any two nearby points $( r , \phi )$ and $( r + d r , \phi + d \phi )$ are correctly reproduced.Distances measured off the curved surface have no physical meaning; points off that surface have no physical meaning;and the Euclidean 3-space itself has no physical meaning. Only the curved 2-geometry has meaning. A circle of Schwarzschild coordinate radius $\boldsymbol { r }$ has proper circumference $_ { 2 \pi r }$ (attention limited to equatorial plane of star, $\theta = \pi / 2$ ).Replace this circle by a sphere of proper area $4 \pi r ^ { 2 }$ ,similarly for allthe other circles,in order to visualize_the entire 3-geometry in and around the star at any chosen moment of Schwarzschild coordinate time $t ,$ The factor $\lbrace 1 - 2 m ( r ) / r \rbrace ^ { - 1 }$ develops no singularity as $\dot { \boldsymbol { r } }$ decreases within $r = 2 M$ because $m ( r )$ decreases sufficiently fast with decreasing $\boldsymbol { r }$

be independent of $\phi$ ,whatever may be its dependence on $r .$ Thus the whole storyof the embedding is summarized by the single function,the lift,

$$
z = z ( r ) ( \mathrm { ' e m b e d d i n g ~ f o r m u l a " } ) .
$$

The geometry on this curved two-dimensional locus in Euclidean space (a made-up 3-space; it has nothing whatever to do with the real world) is to be identical with the geometry of the two-dimensional equatorial slice through the actual star; in other words,the line elements in the two cases are to be identical. To work out this requirement in mathematical terms,write the line element in three-dimensional Euclidean space in the form

$$
d s ^ { 2 } = d z ^ { 2 } + d r ^ { 2 } + r ^ { 2 } d \phi ^ { 2 } .
$$

Restrict to the chosen locus ("lifted surface") by writing $z = z ( r )$ or $d z = ( d z / d r ) d r$ Thus have

$$
d s ^ { 2 } = \left[ 1 + \left( \frac { d z ( r ) } { d r } \right) ^ { 2 } \right] d r ^ { 2 } + r ^ { 2 } d \phi ^ { 2 }
$$

on the two-dimensional locus in the 3-geometry,to be identified with

$$
d s ^ { 2 } = [ 1 - 2 m ( r ) / r ] ^ { - 1 } d r ^ { 2 } + r ^ { 2 } d \phi ^ { 2 }
$$

in the actual star. Compare and conclude

$$
\left( \frac { d z ( r ) } { d r } \right) ^ { 2 } + 1 = [ 1 - 2 m ( r ) / r ] ^ { - 1 } .
$$

This equation is information enough to find the lift as a function of $\boldsymbol { r }$ thus,

$$
z ( r ) = \int _ { 0 } ^ { r } \frac { d r } { \left[ \frac { r } { 2 m ( r ) } - 1 \right] ^ { 1 / 2 } }
$$

$$
z ( r ) = [ 8 M ( r - 2 M ) ] ^ { 1 / 2 } + \mathrm { c o n s t a n t }
$$

Outside the star this embedded surface is a segment of a paraboloid of revolution. Its form inside the star depends on how the mass, $m$ ,varies as a function of $r$ Recall that $m ( r )$ varies as $( 4 \pi / 3 ) \rho _ { c } r ^ { 3 }$ near the center of the star.Conclude that the embedded surface there looks like a segment of a sphere of radius $a = ( 3 / 8 \pi \rho _ { c } ) ^ { 1 / 2 }$ ; thus,

$$
[ a - z ( r ) ] ^ { 2 } + r ^ { 2 } = a ^ { 2 } \qquad { \mathrm { f o r ~ } } r \ll a = ( 3 / 8 \pi \rho _ { c } ) ^ { 1 / 2 } .
$$

In the special case of a star with uniform density $( \mathbf { B o x } 2 3 . 2 )$ , the entire interior is of the spherical form (23.34c); in the general case it is not. In all cases, because $r > 2 m ( r ) ,$ ，equation (23.34a) produces a surface with $z$ and $r$ as monotonically increasing functions of each other. This means that the embedded surface always opens upward and outward like a bowl; it always looks qualitatively like Figure 23.1; it never has a neck,and it never flatens out except asymptotically at $r = \infty$ At the star's surface,even though the density may drop discontinuously to zero ( $\mathbf { \nabla } _ { \pmb { \rho } }$ finite inside when $p = 0$ ； $\pmb { \rho }$ zero outside), the interior and exterior geometries will join together smoothly $\{ d z / d r ,$ ,as given by equation (23.33),is continuous].

It must be emphasized that only points lying on the embedded 2-surface have physical significance so far as the stellar geometry is concerned: the three-dimensional regions inside and outside the bowl of Figure 23.l are physically meaningless. So is the Euclidean embedding space. It merely permits one to visualize the geometry of space around the star in a convenient manner.

Description of embedded surface

# Exercise 23.9. GOOD BEHAVIOR OF r

# EXERCISES

Carry out explicitly the full details of the proof,at the beginning of this section, that $2 m / r$ is always less than unity and $r$ is a monotonic function of l.

# ExerciSe 23.1O. CENTER OF STAR OCCUPIED BY IDEAL FERMI GAS AT EXTREME RELATIVISTIC LIMIT

Opposite to the idealization of a star built from an incompressible fluid is the idealization in which it is built from an ideal Fermi gas [ideal neutron star;see Oppenheimer and Volkoff (1939)]at zero temperature,so highly compressed that the particles have relativistic energies,

in comparison with which any rest mass they possess is negligible. In this limit, with two particles per occupied cell of volume $h ^ { . 3 }$ in phase space, one has

$$
\binom { \mathrm { n u m b e r ~ d e n s i t y } } { \mathrm { o f ~ f e r m i o n s } } = n = ( 2 / h ^ { 3 } ) 4 \div \int _ { 0 } ^ { p _ { \mathrm { F } } } p ^ { 2 } \ d p = 8 \pi { p _ { \mathrm { F } } } ^ { 3 } / 3 h ^ { 3 } ,
$$

$$
\binom { \mathrm { d e n s i t y ~ o f ~ } } { \mathrm { m a s s - e n e r g y } } = \rho = ( 2 / h ^ { 3 } ) 4 \pi \int _ { 0 } ^ { p _ { \mathrm { F } } } c p \cdot p ^ { 2 } d p = 2 \pi c p _ { \mathrm { F } } ^ { ~ 4 } / h ^ { 3 } ,
$$

and finally

$$
p = - \frac { d \binom { \mathrm { e n e r g y } } { \mathrm { p e r ~ p a r t i c l e } } } { d \binom { \mathrm { v o l u m e } } { \mathrm { p e r ~ p a r t i c l e } } } = - \frac { d ( \rho / n ) } { d ( 1 / n ) } = 2 \pi c p _ { \mathrm { F } } { } ^ { 4 } / 3 h ^ { 3 } = \rho / 3 ,
$$

as if one were dealing with radiation instead of particles ( $p _ { F } =$ Fermi momentum;momentum of highest occupied state).

# Box 23.3 RIGOROUS DERIVATION OF THE SPHERICALLY SYMMETRIC LINE ELEMENT

Section 23.2 gave a heuristic derivation of the general spherically symmetric line element (23.7). This box attempts a more rigorous derivation, applicable to nonstatic systems,as well as static ones.

Begin with a manifold $M ^ { 4 }$ on which a metric $d s ^ { 2 }$ of Lorentz signature is defined. Assume $M ^ { 4 }$ to be spherically symmetric in the sense that to any $3 \times 3$ rotation matrix $\pmb { A }$ there corresponds a mapping (rotation） of $M ^ { 4 }$ ，also called A $( A { : } M ^ { 4 }$ $\longrightarrow M ^ { 4 } { : } \mathcal { P } \longrightarrow A \mathcal { P } )$ ,that preserves the lengths of all curves.Further assumptions and constructions will be numbered (i),(ii),etc., so one can see what specializations are needed to get to the line element (23.7). Daggers $( \dagger )$ indicate assumptions that are found inapplicable to some other physically interesting situations.

For any point ${ \mathcal P }$ ，form the set $\begin{array} { r } { s = \mathcal { S } ( \mathcal { P } ) = } \end{array}$ $\{ A \mathcal { P } \in M ^ { \bar { 4 } } | A \stackrel { - } { \in } S O ( 3 ) \}$ of all points equivalent to $\mathcal { P }$ under rotations. Assume $( \mathrm { i } ) \dagger$ that $\pmb { s }$ is a two-dimensional surface (except for center points, where $\pmb { s }$ is zero-dimensional),and (ii) that the metric on $\pmb { s }$ is that of a standard 2-sphere. Then on $\pmb { s }$ one will have

$$
( d s ^ { 2 } ) _ { s } = R ^ { 2 } ( s ) d \varOmega ^ { 2 } ,
$$

where $d \Omega ^ { 2 }$ is the standard metric of a unit sphere $( d \Omega ^ { 2 } = d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 }$ for some $\theta , \phi .$ defined on $s )$ ,and where $2 \pi R$ is the circumference of $\pmb { S } .$ If $M ^ { 2 }$ is the set of all such surfaces $\pmb { S } ,$ then $\mathcal { S } { : } M ^ { 4 } \longrightarrow$

$M ^ { 2 } { : } \mathcal { P } \longrightarrow s = \mathcal { S } ( \mathcal { P } )$ allows one to obtain, from $R { \mathrel { : } } M ^ { 2 } \longrightarrow { \mathcal { R } } { \mathrel { : } } s \longrightarrow R ( s )$ [the“circumference” function on $M ^ { 2 }$ as defined by equation (l)],a correspondingfunction $R : M ^ { 4 } \longrightarrow \mathcal { R } : \mathcal { O } \longrightarrow$ $R ( { \mathcal { S } } ( { \mathcal { P } } ) )$ on $M ^ { 4 }$ which in some cases can eventually be used as a coordinate on $M ^ { 4 }$ . (Note: $\mathcal { R }$ denotes here the real numbers.)

Now assume (ii) $\dagger$ there is a spherically symmetric 4-velocity field $\pmb { u }$ defined so that if $\bar { \boldsymbol { \mathcal { P } } } = \boldsymbol { \mathcal { C } } ( \tau )$ is one trajectory of $\pmb { u }$ with $\pmb { \upsilon } = d / d \tau$ ，then each curve $\mathcal { P } = A \mathcal { C } ( \tau )$ obtained by a rotation must also be a trajectory of ${ \pmb u } .$ .The orthogonal projection of $\pmb { u }$ onto any sphere $\pmb { s }$ must then vanish,as there are no rotation invariant non-zero vector fields on 2-spheres. Thus $\pmb { u }$ is orthogonal to each s. Also, if two trajectories of $\pmb { u }$ start on some same sphere s, so $\mathcal { C } _ { 1 } ( 0 ) = A \mathcal { C } _ { 2 } ( 0 )$ ,then the same rotation $\pmb { A }$ will always relate them, $\mathcal { C } _ { 1 } ( \tau ) = A \mathcal { C } _ { 2 } ( \tau ) ,$ since trajectories are uniquely defined by any one point on them. Then $\mathcal { S } ( \mathcal { C } _ { \mathfrak { r } } ( \tau ) )$ and $\mathcal { S } ( \mathcal { C } _ { 2 } ( \tau ) )$ are both the same curve in $M ^ { 2 }$ ，whose tangent $d / d \tau$ one can call also $\pmb { u }$ ；in this way one obtains a vector field ${ \pmb u }$ on $M ^ { 2 }$ . Give each trajectory of ${ \pmb u }$ on $M ^ { 2 }$ a different label $r$ to define a function $r ( s )$ on $M ^ { 2 }$ . Denote by $r = r ( \mathcal { S } ( \mathcal { P } ) )$ a corresponding function $r$ on $M ^ { 4 }$ with $d r / d \tau = 0$ . Since functions and their gradients on $M ^ { 4 }$ define corresponding quantities on $M ^ { 2 }$ ， inner products such as $d f \cdot d g$ can be defined on $M ^ { 2 }$ by their values on $M ^ { 4 }$ ； thus,from the metric on $M ^ { 4 }$ one obtains a metric on $M ^ { 2 }$ . Then by equa-

(a) Write out the relativistic equation of hydrostatic equilibrium for a substance satisfying the equation of state $\pmb { p } = \pmb { \rho } / 3$ (b) Show that there exists a well-defined analytic solution for the limiting case of infinite central density,in which $m ( r ) / r$ has the value $3 / 1 4$ · (c）Find $\rho ( r ) , p ( r )$ and $n ( r )$ (d) Show that the number of particles out to any finite $r$ -value is finite,despite the fact that $n ( r )$ is infinite at the origin. (e） Show that the 3-geometry has a “conical singularity”at $\boldsymbol r = 0$ (f） Make an “embedding diagram” for this 3-geometry [lift” $z ( r )$ as a function of $\boldsymbol { r }$ from (23.34)]. (Note that the conical singularity at $\boldsymbol r = 0$ ,otherwise physically unreasonable,arises because the density of mass-energy goes to infinity at that point. Note also that the calculated mass of the system diverges to infinity as $r \longrightarrow \infty$ . In actuality with decreasing density the Fermi momentum fals from relativistic to nonrelativistic values,the equation of state changes its mathematical form,and the total mass $M$ converges to a finite value).

tion (23.5） or equivalently by drawing curves in $M ^ { 2 }$ orthogonal to the $r =$ const. lines, and giving each a different label $t$ ,one obtains coordinates with $g ^ { \varkappa } \equiv d r \cdot d t = 0$ .Both $r$ and $t$ labels were assigned arbitrarily on the corresponding curves, so it is clear that transformations $t ^ { \prime } = t ^ { \prime } ( t )$ and $r ^ { \prime } = r ^ { \prime } ( r )$ are not excluded.

On one 2-sphere $\pmb { s }$ in $M ^ { 4 }$ ,on the $t = 0$ hypersurface, choose a set of $\theta , \phi$ coordinates by picking the pole $( \theta = 0 )$ and the prime meridian $( \phi = 0 )$ arbitrarily. Then extend the definition of $\theta , \phi$ over the $t = 0$ hypersurface by requiring $\pmb \theta$ and $\phi$ to be constant on curves orthogonal to each 2-sphere $\pmb { s }$ i.e., by demanding that $( \bar { \partial } / \partial r ) _ { \theta \phi }$ be orthogonal to each $\pmb { s }$ at $t = 0$ .Extend the definition of $\pmb \theta$ and $\phi$ to $t \neq 0$ by requiring them to be constant on curves with tangent $\pmb { u }$ so $( \partial / \partial t ) _ { r \theta \phi } \propto \pmb { \mu }$ But each $\pmb { s }$ is a surface of constant $r$ and $t$ so $( \partial / \partial \pmb { \theta } ) _ { \pmb { r } \pmb { \phi } }$ and $( \partial / \partial \phi ) _ { \varkappa \theta }$ are tangent to $\pmb { s }$ ，while $\pmb { \mathscr { u } } \propto ( \hat { \partial } / \dot { \partial } t )$ is orthogonal to each ${ \pmb S } .$ Consequently,

and

$$
\begin{array} { l l } { { g _ { t \theta } = ( \partial / \partial t ) \cdot ( \partial / \partial \theta ) = 0 } } \\ { { \ } } \\ { { g _ { t \phi } = ( \partial / \partial t ) \cdot ( \partial / \partial \phi ) = 0 } } \end{array}
$$

in the $t r \theta \phi$ coordinate system just constructed. The vector $( \partial / \partial r ) _ { t \theta \phi }$ does not depend on the arbitrary directions introduced in the original choice of $\theta , \phi$ coordinates on one sphere $\pmb { \mathscr { s } }$ ；it is invariant under transformations $\theta = \theta ( \theta ^ { \prime } , \phi ^ { \prime } )$ ， $\phi = \phi ( \theta ^ { \prime } , \phi ^ { \prime } )$ But nothing except $\pmb \theta$ and $\phi$ introduced nonrotationally invariant elements into the discussion; so(a/ar)te must be a rotationally invariant vector field (unlike, say, $\hat { \partial } / \hat { \partial } \phi \dot { } \mathrm { ~  ~ }$ ; so it is,like $\pmb { u }$ ,orthogonal to each 2-sphere $\pmb { s }$ This invariance then gives

$$
g _ { \tau \theta } = ( \partial / \partial r ) \cdot ( \partial / \partial \theta ) = 0 ,
$$

$$
g _ { \tau \phi } = ( \partial / \partial r ) \cdot ( \partial / \partial \phi ) = 0 ,
$$

which, with $g ^ { t r } = 0$ as previously established, gives $g _ { t r } = 0$ . The result is a line element of the form (23.3). Further specialization,a change of radial and time coordinates to $\pmb R$ and $T ,$ where $R$ is defined by(l）above and

$$
\begin{array} { l } { d T = e ^ { \displaystyle \psi } \biggl [ \frac { 1 } { g _ { \pi } } \frac { \partial R } { \partial r } d t - \frac { 1 } { g _ { t t } } \frac { \partial R } { \partial t } d r \biggr ] , } \\ { e ^ { \displaystyle \psi } = \biggl ( \mathrm { i n t e g r a t i n g } \biggr ) , } \end{array}
$$

followed by a change of notation， leads to Schwarzschild coordinates and the line element (23.7)—-though such a transformation is possible (i.e.,nonsingular) only where $d R \wedge d T \not \equiv 0$ ：

$$
( \pmb { \nabla } R ) ^ { 2 } = \frac { ( \partial R / \partial t ) ^ { 2 } } { g _ { t t } } + \frac { ( \partial R / \partial r ) ^ { 2 } } { g _ { \pi } } \neq 0 .
$$

f $( \mathrm { i } \mathbf { v } ) \dag$ spacetime is asymptotically flat， so $r \longrightarrow \infty$ is a region where the metric can take on its special relativity values, then the arbitrariness in the $t$ coordinate, $t ^ { \prime } = t ^ { \prime } ( t )$ , can be eliminated by requiring $g _ { t t } = - 1 \mathsf { a s } r \longrightarrow \infty$ . Then $( \partial / \partial t ) _ { r \theta \phi }$ is uniquely determined by natural requirements (independent of the arbitrary $\theta , \phi$ ，choices)，and whenever it is desired to make the further physical assumption $( \mathbf { v } ) \dagger$ of a time-independent geometry, this can be appropriately restated as $\partial g _ { \mu \nu } / \partial t = 0$
