CHAPTER 22

# THERMODYNAMICS,HYDRODYNAMICS, ELECTRODYNAMICS，GEOMETRIC OPTICS,AND KINETIC THEORY

# \$22.1. THE WHY OF THIS CHAPTER

Astrophysical applications of gravitation theory are the focus of the rest of this book, except for Chapters 41-44. Each application-stars,star clusters,cosmology,collapse, black holes,gravitational waves,solar-system experiments-can be pursued by itself at an elementary level,-without reference to the material in this chapter. But deep understanding of the applications requires a prior grasp of thermodynamics, hydrodynamics, electrodynamics,geometric optics,and kinetic theory,all in the context of curved spacetime. Hence, most Track-2 readers will want to probe these subjects at this point.

This chapter is entirely Track 2. No earlier Track-2 material is needed as preparation for it. but Chapter 5 (stress-energy tensor) will be helpful.

$\$ 22.5$ (geometric optics) is needed as preparation for Chapter 34 (singularities and global methods). The rest of the chapter is not needed as preparation for any later chapter;but it will be extremely helpful in most applications of gravitation theory (Chapters 23-40).

# \$22.2. THERMODYNAMICS IN CURVED SPACETIME\*

Consider, for concreteness and simplicity,the equilibrium thermodynamics of a perfect fluid with fixed chemical composition ("simple perfect fuid")-for example, the gaseous interior of a collapsing supermassive star. The thermodynamic state of a fluid element, as it passes through an event ${ \mathcal { P } } _ { 0 }$ ,can be characterized by various thermodynamic potentials, such as $n , \ \rho , \ p , \ T , \ s , \ \mu$ ，The numerical value of each potential at $\mathcal { P } _ { 0 }$ is measured in the proper reference frame $( \ S 1 3 . 6 )$ of an observer who moves with the fluid element-i..,in the fluid element's“rest frame.” Despite

Thermodynamic potentials are defined in rest frame of fluid

this use of rest frame to measure the potentials. the potentials are frame-independent functions (scalar fields). At the chosen event $\boldsymbol { \mathfrak { P } } _ { 0 }$ ,a given potential (e.g., n) has a unique value $n ( \mathfrak { s } \mathfrak { P } _ { 0 } )$ ：so $\pmb { n }$ is a perfectly good frame-independent function.

The values of $n , \rho , p , T , s , \mu$ measure the following quantities in the rest frame of the fluid element:

# Definitions of thermodynamic potentials

$\pmb { n }$ ，baryon number density: i.e., number of baryons per unit three-dimensional volume of rest frame, with antibaryons (if any) counted negatively.   
$\pmb { \rho }$ ，density of total mass-energy; i.e., total mass-energy (including rest mass, thermal energy,compressional energy,etc.) contained in a unit three-dimensional volume of the rest frame.   
$\boldsymbol { p }$ ，isotropic pressure in rest frame.   
$T ,$ temperature in rest frame.   
$s$ ， entropy per baryon in rest frame. (The entropy per unit volume is ns.)   
$\mu$ ,chemical potential of baryons in rest frame [see equation (22.8) below].

Definition of “simple fluid'

The chemical composition of the fluid (number density of hydrogen molecules, number density of hydrogen atoms, number density of free protons and electrons, number density of photons,number density of $^ { 2 3 8 } \mathrm { U }$ nuclei, number density of $\pmb { A }$ hyperons ..)is assumed to be fixed uniquely by two thermodynamic variables-e.g, by the total number density of baryons $\pmb { n }$ and the entropy per baryon s. In this sense the fluid is a“simple fuid.” Simple fluids occur whenever the chemical abundances are“frozen” (reaction rates too slow to be important on the time scales of interest; for example, in a supermassive star except during explosive burning and except at temperatures high enough for $e ^ { - } - e ^ { + }$ pair production).Simple fluids also occur in the opposite extreme of complete chemical equilibrium (reaction rates fast enough to maintain equilibrium despite changing density and entropy; for example, in neutron stars,where high pressures speed up all reactions). When one examines nuclear burning in a nonconvecting star, or explosive nuclear burning,or pair production and neutrino energy losses at high temperatures, one must usually treat the fluid as “multicomponent.” Then one introduces a number density $n _ { J }$ and a chemical potential $\mu _ { J }$ for each chemical species with abundance not fixed by $\pmb { n }$ and s.For further details see, e.g., Zel'dovich and Novikov (1971).

The most fundamental law of thermodynamics-even more fundamental than the “first”and “second” laws-is baryon conservation.Consider a fluid element whose moving wals are attached to the fluid so that no baryons flow in or out.As the fluid element moves through spacetime,deforming along the way,its volume $V$ changes. But the number of baryons in it must remain fixed,so

$$
\frac { d } { d \tau } \left( n V \right) = 0 .
$$

The changes in volume are produced by the flow of neighboring bits of fluid away from or toward each other-explicitly (exercise 22.1)

$$
d V / d \tau = ( \nabla \cdot \pmb { u } ) V ,
$$

where $\pmb { \mu } = \pmb { d } / d \tau$ is the 4-velocity of the fluid. Consequently, baryon conservation [equation (22.1)] can be reexpressed as

$$
0 = \frac { d n } { d \tau } + \frac { n } { V } \frac { d V } { d \tau } = \nabla _ { u } n + n ( \nabla \cdot u ) = u \cdot \nabla n + n ( \nabla \cdot u ) = \nabla \cdot ( n u ) ;
$$

i.e.,

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { s } = 0 , } \end{array}
$$

(see $\ S 5 . 4$ and exercise 5.3.) Moreover,this abstract geometric version of the law must be just as valid in curved spacetime as in flat (equivalence principle).

Note the analogy with the law of charge conservation, $\pmb { \nabla } \cdot \pmb { J } = 0$ ,in electrodynamics (exercise 3.16) and with the local law of energy-momentum conservation, $\pmb { \bigtriangledown } \cdot \pmb { \cal T } = 0$ $\mathfrak { S } \mathfrak { S } \mathfrak { S } . 9$ and 16.2). In a very deep sense,the forms of these three laws are dictated by the theorem of Gauss (S5.9,and Boxes 5.3,5.4).

The second law of thermodynamics states that, in flat spacetime or in curved, entropy can be generated but not destroyed. Apply this law to a fluid element of volume $V$ containing a fixed number of baryons $N .$ The entropy it contains is

Second law of thermodynamics

$$
S = N s = n s V .
$$

Entropy may flow in and out across the faces of the fuid element ("heat flow” between neighboring fluid elements); but for simplicity assume it does not; or if it does,assume that it flows too slowly to have any significance for the problem at hand. Then the entropy in the fluid element can only increase:

$$
d ( n s V ) / d \tau \geq 0
$$

i.e. [combine with equation (2.1)]

$$
d s / d \tau \geq 0 \ ( \mathrm { n o \ e n t r o p y \ e x c h a n g e } ) .
$$

Shock waves and heat flow

So long as the fluid element remains in thermodynamic equilibrium, its entropy will actually be conserved $[ ^ { 6 6 } = "$ in equation (22.5)]; but at a shock wave,where equilibrium is momentarily broken, the entropy will increase (conversion of "relative kinetic energy”of neighboring fluid elements into heat). [For discussions of heat flow in special and general relativity, see Exercise 22.7.For discussion of shock waves, see Taub (1948),de Hoffman and Teller (1950), Israel (1960),May and White (1967), Zel'dovich and Rayzer (1967),Lichnerowicz (1967,1971),and Thorne (1973a).]

The first law of thermodynamics, in the proper reference frame of a fuid element, is identical to the first law in flat spacetime ("principle of equivalence"); and in flat spacetime the first law is merely the law of energy conservation:

First law of thermodynamics

$$
d { \binom { \mathrm { e n e r g y ~ i n ~ a ~ v o l u m e ~ e l e m e n t ~ c o n t a i n i n g } } { \mathrm { a ~ f u x e d ~ n u m b e r } , ~ \mathcal { A } , ~ \mathrm { o f ~ b a r y o n s } } } = - p d ( \mathrm { v o l u m e } ) ~ + ~ T d ( \mathrm { e n t r o p y } ) ;
$$

$$
d ( \rho A / n ) = - p d ( A / n ) + T d ( A s ) ;
$$

i.e.,

$$
d \rho = \frac { \rho + p } { n } d n + n T d s .
$$

Query: what kind of a $" d "$ appears here? For a simple fluid, the values of two potentials, e.g., $\pmb { n }$ and $\pmb { S }$ ,fix all the others uniquely; so any change in $\rho$ must be determined uniquely by the changes in $\pmb { n }$ and ${ \pmb S } .$ . It matters not whether the changes are measured along the world line of a given fluid element, or in some other direction. Thus, the $" d "$ in the frst law can'be interpreted as an exterior derivative

$$
{ \pmb d } \rho = \frac { \rho + p } { n } { \pmb d } n + n T { \pmb d } s ;
$$

and the changes along a given direction in the fuid (along a given tangent vector $\pmb { \nu }$ ）can be written

$$
\begin{array} { c l } { \displaystyle \pmb { \nabla } _ { \pmb { v } } \rho \equiv \langle \pmb { d } \rho , \pmb { v } \rangle = \frac { \rho + p } { n } \langle \pmb { d } n , \pmb { v } \rangle + n T \langle \pmb { d } s , \pmb { v } \rangle } \\ { \displaystyle = \frac { \rho + p } { n } \pmb { \nabla } _ { \pmb { v } } n + n T \pmb { \nabla } _ { \pmb { v } } s . } \end{array}
$$

Pressure and temperature calculated from $\rho ( n , s )$

Equation (22.6) lends itself to interpretation in two opposite senses: as a way to deduce the density of mass-energy of the medium from information about pressure (as a function of $\pmb { n }$ and $s \mathrm { \ i }$ )and temperature (as a function of $\pmb { n }$ and s); and conversely, as a way to deduce the two functions $p ( n , s )$ and $T ( n , s )$ from the one function $\rho ( n , s )$ It is natural to look at the second approach first; who does not like a strategy that makes an intellectual profit? Regarding $\pmb { \rho }$ as a known (or calculable) function of $\pmb { n }$ and $s$ ,one deduces from (22.6)

$$
\begin{array} { c } { \displaystyle \frac { \rho + p } { n } = \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } n } \right) _ { s } , } \\ { \displaystyle n T = \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } s } \right) _ { n } , } \end{array}
$$

and thence pressure and temperature individually,

$$
\begin{array} { c } { { p ( n , s ) = n \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } n } \right) _ { s } - \rho , } } \\ { { { } } } \\ { { T ( n , s ) = \displaystyle \frac { 1 } { n } \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } s } \right) _ { n } } } \end{array}
$$

("two equations of state from one"). The analysis simplifies stil further when the fluid,already assumed to be everywhere of the same composition,is also everywhere endowed with the same entropy per baryon, s,and is in a state of adiabatic flow (no shocks or heat conduction). Then the density $\rho = \rho ( n , s )$ reduces to a function of one variable out of which one derives everything $( \pmb \rho , p , \mu )$ needed for the hydrodynamics and the gravitation physics of the system (next chapter). Other choices of the “primary thermodynamic potential” are appropriate under other circumstances (see Box 22.1).

If differentiation leads from $\rho ( n , s )$ to $p ( n , s )$ and $T ( n , s )$ ,it does not follow that one can take any two functions $p ( n , s )$ and $T ( n , s )$ and proceed “backwards" (by integration） to the“primary function”, $\rho ( n , s )$ . To be compatible with the first law of thermodynamics (22.6),the two functions must satisfy the consistency requirement ["Maxwell relation”; equality of second partial derivatives of $\pmb { \rho } ]$

$$
( \hat { \sigma } p / \hat { \sigma } s ) _ { n } = n ^ { 2 } ( \hat { \sigma } T / \hat { \sigma } n ) _ { s } .
$$

# Box 22.1 PRINCIPAL ALTERNATIVES FOR "PRIMARY THERMODYNAMIC POTENTIAL" TO DESCRIBE A FLUID

Primary thermodynamic potential and quantities on which it is most appropriately envisaged to depend

“Secondary” thermodynamic quantities obtained by differentiation of primary with or without use of

Conditions under which convenient, appropriate,and relevant

$$
d \bigg ( \frac { \rho } { n } \bigg ) + p d \bigg ( \frac { 1 } { n } \bigg ) - T d s = 0
$$

"Density"; total amount of masenergy (rest $^ +$ thermal $+ \cdot \cdot \cdot )$ per unit volume

$$
\rho = \rho ( n , s )
$$

$$
{ \begin{array} { l } { p ( n , s ) \equiv n { \Big ( } { \frac { \partial \rho } { \partial n } } { \Big ) } _ { s } - \rho } \\ { T ( n , s ) = { \frac { 1 } { n } } { \Big ( } { \frac { \partial \rho } { \partial s } } { \Big ) } _ { n } } \\ { \mu ( n , s ) = { \frac { p + \rho } { n } } = { \Big ( } { \frac { \partial \rho } { \partial n } } { \Big ) } _ { s } } \end{array} }
$$

Conditions of adiabatic flow (no shocks or heat conduction),so'that $\pmb { \mathscr { s } }$ stays constant along streamline

"Physical free energy"

$$
a ( n , T ) = { \frac { \rho } { n } } - T s
$$

$$
\begin{array} { l } { { \displaystyle p ( n , T ) = n ^ { 2 } \bigg ( \frac { \partial a } { \partial n } \bigg ) _ { T } } } \\ { { \displaystyle s ( n , T ) = - \bigg ( \frac { \partial a } { \partial T } \bigg ) _ { n } } } \\ { { \displaystyle \rho ( n , T ) = - n T ^ { 2 } \bigg [ \frac { \partial ( a / T ) } { \partial T } \bigg ] _ { n } } } \end{array}
$$

Know or can calculate a (or the “sum over states”of statistical mechanics) for conditions of specified volume per baryon and temperature "Chemical free energy”

$$
f ( p , T ) = { \frac { \rho + p } { n } } - T s
$$

Relevant for determining equilibrium when pressure and temperature are specified

“Chemical potential"("energy to inject”expressed on a“per baryon" basis)

$$
\mu ( p , s ) = { \frac { p + \rho } { n } } 
$$

$$
\rho ( p , s ) = { \frac { \mu } { ( \partial \mu / \hat { \sigma } p ) _ { s } } } - p
$$

When injection energy $\{ =$ Fermi energy for an ideal Fermi gas,relativistic or not; see exercise 22.3j is the center of attention

Chemical potential equals "injection energy"at fixed entropy per baryon and total volume

The chemical potential $\mu$ is also a unique function of $\pmb { n }$ and s. It is defined as follows. (l) Take a sample of the simple fluid in a fixed thermodynamic state (fixed $\pmb { n }$ and $s ^ { \cdot }$ ).(2)Take, separately,a much smaller sample of the same fluid, containing $\delta A$ baryons in the same thermodynamic state as the large sample (same $\pmb { n }$ and s). (3) Inject the smaller sample into the larger one, holding the volume of the large sample fixed during the injection process. (4) The total mass-energy injected,

$$
\delta M _ { \mathrm { i n j e c t e d } } = \rho \times ( \mathrm { v o l u m e ~ o f ~ i n j e c t e d ~ f l u i d } ) = \rho ( \delta A / n ) ,
$$

plus the work required to perform the injection

$$
\begin{array} { r } { \delta W _ { \mathrm { i n j e c t i o n } } = \Big ( \mathrm { w o r k ~ d o n e ~ \mathsf { a g a i n s t } ~ p r e s s u r e ~ o f ~ l a r g e ~ s a m p l e } \Big ) } \\ { \mathsf { \ t i o ~ o p e n ~ \mathsf { u p ~ s p a c e ~ i n ~ i t ~ f o r ~ t h e ~ i n j e c t e d ~ f l u i d } } } \\ { = p ( \mathrm { v o l u m e ~ o f ~ i n j e c t e d ~ f l u i d } ) = p ( \delta A / n ) , \qquad } \end{array}
$$

is equal to $\mu \delta A$ ：

$$
\mu \delta A = \delta M _ { \mathrm { i n j e c t e d } } + \delta W _ { \mathrm { i n j e c t i o n } } = \frac { \rho + p } { n } \delta A .
$$

Stated more briefly:“

$$
\begin{array} { r l } & { \mu = \left( \begin{array} { l } { \mathrm { t o t a l ~ m a s s - e n e r g y ~ r e q u i r e d , ~ p e r ~ b a r y o n , ~ t o ~ \hat { \mu } ^ { * } c r e a t e ' s ~ a n d } } \\ { \mathrm { i n j e c t ~ a ~ s m a l l ~ a d d i t i o n a l ~ a m o u n t ~ o f ~ f u i d ~ i n i d ~ i n t o ~ a ~ g i v e n } } \\ { \mathrm { s a m p l e , ~ w i t h o u t ~ c h a n g i n g ~ \hat { \mu } s ~ o r ~ v o l u m e ~ o f ~ t h e ~ s a m p l e } } \end{array} \right) } \\ & { \quad = \frac { \rho + p } { n } = \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } n } \right) _ { s } . } \\ & { \qquad \quad \begin{array} { r } { \mathrm { L } _ { [ b y ~ f i r s t ~ l a w ~ o f ~ t h e r m o d y n a m i c s ~ ( 2 2 . 6 ) ] } } \end{array} } \end{array}
$$

All the above laws and equations of thermodynamics are the same in curved spacetime as in flat spacetime; and the same in (relativistic) flat spacetime as in classical nonrelativistic thermodynamics-except for the inclusion of rest mass, together with all other forms of mass-energy,in $\pmb { \rho }$ and $\mu$ .The reason is simple: the laws are all formulated as scalar equations linking thermodynamic variables that one measures in the rest frame of the fluid.

# $\$ 22.3$ . HYDRODYNAMICS IN CURVED SPACETIME\*

Laws of hydrodynamics for simple fluid without heat flow or viscosity:

A simple perfect fluid flows through spacetime.It might be the Earth's atmosphere circulating in the Earth's gravitational field. It might be the gaseous interior of the Sun at rest in its own gravitational feld. It might be interstellar gas accreting onto a black hole.But whatever and wherever the fluid may be, its motion will be governed by the curved-spacetime laws of thermodynamics $( \ S 2 2 . 2 )$ plus the local

(1） Origins of laws

law of energy-momentum conservation, ${ \pmb { \nabla } } \cdot { \pmb { \vec { r } } } = 0$ .The chief objective of this section is to reduce the equation $\pmb { \bigtriangledown } \cdot \pmb { \cal T } = 0$ to usable form. The reduction will be performed in the text using abstract notation; the reader is encouraged to repeat the reduction using index notation.

The stress-energy tensor for a perfect fluid,in curved spacetime as in flat (equivalence principle!), is

$$
\pmb { \tau } = ( \rho + p ) \pmb { \mu } \otimes \pmb { \mu } + p \pmb { g } .
$$

(See $\ S 5 . 5 . )$ Its divergence is readily calculated using the chain rule; using the “com-patibility relation between $\pmb { \mathscr { g } }$ and $\because \pmb { \nabla } \pmb { g } = 0$ ； using the identity $( { \pmb { \nabla } } p ) \cdot { \pmb { g } } = { \pmb { \nabla } } p$ (which one readily verifies in index notation); and using

$$
\begin{array} { r l r } {  { 0 = \nabla \cdot \pmb { T } = [ \nabla ( \rho + p ) \cdot \pmb { u } ] \pmb { u } + [ ( \rho + p ) \nabla \cdot \pmb { u } ] \pmb { u } + [ ( \rho + p ) \pmb { u } ] \cdot \pmb { \nabla } \pmb { u } + ( \pmb { \nabla } p ) \cdot \pmb { g } } } \\ & { \overset { \mathrm { . } } { \mathrm { L } } _ { [ \mathrm { d i v e r g e n c e ~ o n ~ f i r s t ~ s l o t } ] } } \\ & { = [ \pmb { \nabla } _ { \pmb { u } } \rho + \pmb { \nabla } _ { \pmb { u } } p + ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } ] \pmb { u } + ( \rho + p ) \pmb { \nabla } _ { \pmb { u } } \pmb { u } + \pmb { \nabla } p . } & { ( 2 2 . 1 6 \pmb { \nabla } \pmb { u } ) } \end{array}
$$

The component of this equation along the 4-velocity is especially simple (recall that $\begin{array} { r } { \pmb { u } \cdot \pmb { \nabla _ { u } } \pmb { u } = \frac { 1 } { 2 } \pmb { \nabla _ { u } } \pmb { u } ^ { 2 } = 0 } \end{array}$ because $\pmb { u } ^ { 2 } \equiv - 1$ ）：

$$
\begin{array} { r l } & { 0 = u \cdot ( \pmb { \nabla } \cdot \pmb { T } ) = - [ \pmb { \nabla } _ { u } \rho + \pmb { \nabla } _ { u } p + ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } ] + \pmb { \nabla } _ { u } p } \\ & { \quad = - \pmb { \nabla } _ { u } \rho - ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } . } \end{array}
$$

Combine this with the equation of baryon conservation (22.3); the result is

$$
- \quad - \qquad { \frac { d \rho } { d \tau } } = { \frac { ( \rho + p ) } { n } } { \frac { d n } { d \tau } } .
$$

(2) Local energy   
conservation:adiabaticity of   
flow

Notice that this is identical to the first law of thermodynamics (22.6) applied along a fow line, plus the assumption that the entropy per baryon is conserved along a flow line

$$
d s / d \tau = 0 .
$$

There is no reason for surprise at this result.To insist on thermodynamic equilibrium and to demand that the entropy remain constant is to require zero exchange of heat between one element of the fluid and another. But the stress-energy tensor (22.9) recognizes that heat exchange is absent. Any heat exchange would show up as an energy flux term in $\pmb { \tau } ( \mathbf { E x } . 2 2 . 7 )$ ； but no such term is present. Consequently, when one studies local energy conservation by evaluating ${ \pmb u } \cdot \hat { ( } \dot { \pmb { v } } \cdot \pmb { r } ) = 0$ ,the stress-energy tensor reports that no heat flow is occurring--i.e. that $d s / d \tau = 0$

Three components of ${ \pmb { \bigtriangledown } } \cdot { \pmb { \cal T } } = 0$ remain: the components orthogonal to the fluid's 4-velocity. One can pluck them out of ${ \pmb { \bigtriangledown } } \cdot { \pmb { \cal T } } = 0$ ,leaving behind the component along $\pmb { u }$ ,by use of the “projection tensor”

$$
{ \pmb { P } } \equiv { \pmb { g } } + { \pmb { u } } \otimes { \pmb { u } } .
$$

# A.Ten Quantities Characterize the Fluid

Thermodynamic potentials all measured in rest frame

$_ { n }$ ,baryon number density   
$\pmb { \rho }$ ,density of total mass-energy   
$\boldsymbol { p }$ pressure   
$T ,$ temperature   
$s ,$ ,entropy per baryon   
$\mu$ ,chemical potential per baryon

Four components of the fuid 4-velocity

# B. Ten Equations Govern the Fluid's Motion

Two equations of state

$$
p = p ( n , s ) , \quad \quad T = T ( n , s )
$$

subject to the compatibility constraint ("Maxwell relation,”which follows from first law of thermodynamics)

$$
( \hat { \sigma } p / \hat { \sigma } s ) _ { n } = n ^ { 2 } ( \hat { \sigma } T / \hat { \sigma } n ) _ { s } .
$$

First law of thermodynamics

$$
{ \pmb d } \rho = \frac { \rho + p } { n } { \pmb d } n + n T { \pmb d } s ,
$$

which can be integrated to give $\rho ( n , s )$

Equation for chemical potential

$$
\begin{array} { r } { \mu = ( \rho + p ) / n , } \end{array}
$$

which can be combined with $\rho ( n , s )$ and $p ( n , s )$ to give $\mu ( n , s )$

Law of baryon conseruation

$$
d n / d \tau \equiv \pmb { \nabla } _ { \pmb { u } } n = - n \ \pmb { \nabla } \cdot \pmb { u } .
$$

Conservation of energy along flow lines, which (assuming no energy exchange between adjacent fluid elements) means “adiabatic flow”

[Shock waves are not treated in this book; see Taub (l948),de Hoffman and Teller (1950), Israel (1960), May and White (1967), Zel'dovich and Rayzer(l967)； Lichnerowicz (1967,1971); and Thorne (1973a).]

Euler equations

$$
\left( \rho + p \right) \nabla _ { u } u = - ( { \pmb g } + { \pmb u } \otimes { \pmb u } ) \cdot \nabla p ,
$$

which determine the flow lines to which $\pmb { u }$ is tangent.

Normalization of 4-velocity

$$
{ \pmb u } \cdot { \pmb u } = - 1 .
$$

(See exercise 22.4.) Contracting $\pmb { P }$ with $\pmb { \bigtriangledown } \cdot \pmb { \cal T } = 0$ [equation (22.10)] gives

(3) Euler equation

$$
\left( \rho + p \right) \nabla _ { u } u = - P \cdot \left( \nabla p \right) \equiv - [ \nabla p + ( \nabla _ { u } p ) u ] .
$$

This is the “Euler equation”of relativistic hydrodynamics.It has precisely the same form as the corresponding flat-spacetime Euler equation:

$$
{ \begin{array} { r l } & { { \left( \begin{array} { l } { { \mathrm { i n e r t i a l ~ m a s s } } } \\ { { \mathrm { p e r ~ u n i t ~ v o l u m e } } } \\ { [ { \mathrm { e x e r c i s e ~ } } 5 . 4 ] } \end{array} \right) } \times { \left( \begin{array} { l } { 4 { \mathrm { - a c c e l e r a t i o n } } } \\ { { \mathrm { o f ~ f l u i d } } } \end{array} \right) } = - { \left( \begin{array} { l } { { \mathrm { p r e s s u r e ~ g r a d i e n t } } } \\ { { \mathrm { i n ~ t h e ~ } } 3 { \mathrm { - s u r f a c e } } } \\ { { \mathrm { o r t h o g o n a l ~ t o ~ } } 4 { \mathrm { - v e l o c i t y } } } \end{array} \right) } . } \end{array} }
$$

The pressure gradient, not “gravity,” is responsible for all deviation of fow lines from geodesics.

Box 22.2 reorganizes and summarizes the above laws of thermodynamics and hydrodynamics.

# Exercise 22.1. DIVERGENCE OF FLOW LINES PRODUCES VOLUME CHANGES

Derive the equation $d V / d \tau = ( \pmb { \nabla } \cdot \pmb { u } ) V$ [equation (22.2)] for the rate of change of volume of a fluid element. [Hint: Pick an event $\varphi _ { \mathfrak { d } } ^ { }$ and calculate in a local Lorentz frame at $\scriptstyle { \mathcal { P } } _ { 0 }$ which momentarily moves with the fluid ("rest frame at ${ \vec { \pmb { \mathscr { P } } } } _ { 0 } ^ { \pmb { \mathscr { P } } } .$ .] [Solution: At events near $\pmb { \mathcal { P } _ { 0 } }$ the fluid has a very small ordinary velocity $v ^ { j } = d x ^ { j } / d t$ .Consequently a cube of fluid at ${ \pmb \mathcal { P } } _ { \bf 0 }$ with edges $\Delta x = \Delta y = \Delta z = L$ changes its edges,after time $\delta t .$ ,by the amounts

$$
\begin{array} { r l } & { \delta ( \varDelta x ) = [ ( d x / d t ) \delta t ] _ { \mathrm { a t } ^ { * } \mathrm { t r o n t f a c e } ^ { * } } - [ ( d x / d t ) \delta t ] _ { \mathrm { a t } ^ { * } \mathrm { b a c k } \mathrm { t a c e } ^ { * } } } \\ & { \qquad = ( \partial v ^ { x } / \partial x ) L \delta t , } \\ & { \delta ( \varDelta y ) = ( \partial v ^ { y } / \partial y ) L \delta t , } \\ & { \delta ( \varDelta z ) = ( \partial v ^ { z } / \partial z ) L \delta t . } \end{array}
$$

The corresponding change in volume is

$$
\delta ( \varDelta x \varDelta y \varDelta z ) = ( \partial v ^ { j } / \partial x ^ { j } ) L ^ { 3 } \delta t ;
$$

so the rate of change of volume is

$$
\partial V / \partial t = V ( \partial v ^ { j } / \partial x ^ { j } ) .
$$

But in the local Lorentz rest frame at and near ${ \pmb \mathcal { S } } _ { \bf 0 }$ (where $x ^ { \alpha } = 0$ ），the metric coefficientsare $g _ { \mu \nu } = \eta _ { \mu \nu } + 0 ( | x ^ { \alpha } | ^ { 2 } ) ~$ ,and the ordinary velocity is $v ^ { j } = 0 ( | x ^ { \alpha } | )$ ； so

$$
\begin{array} { c } { { u ^ { 0 } = \displaystyle \frac { d t } { d \tau } = \displaystyle \frac { d t } { ( - g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } } = \mathrm { 1 } + 0 ( | x ^ { \alpha } | ^ { 2 } ) , } } \\ { { u ^ { j } = \displaystyle \frac { d x ^ { j } } { d \tau } = v ^ { j } + 0 ( | x ^ { \alpha } | ^ { 3 } ) . } } \end{array}
$$

Thus, the derivatives $\partial V / \partial t$ and $V ( \partial v ^ { j } / \partial x ^ { j } )$ at $\scriptstyle { \mathcal { P } } _ { 0 }$ are

$$
\begin{array} { r l } & { \partial V / \partial t = u ^ { \alpha } \partial V / \partial x ^ { \alpha } = u ^ { \alpha } V _ { , \alpha } = d V / d \tau } \\ & { \qquad = V ( \partial v ^ { j } / \partial x ^ { j } ) = V ( \partial u ^ { \alpha } / \partial x ^ { \alpha } ) = V { u ^ { \alpha } } _ { ; \alpha } = V ( \pmb { \nabla } \pmb { \cdot } \pmb { u } ) . } \end{array}
$$

[Note that by working in flat spacetime, one could have inferred more easily that $\partial V / \partial t =$ $d V / d \tau$ and $\partial v ^ { j } / \partial x ^ { j } = \mathbf { \nabla \mathbf { \nabla } \cdot } \pmb { u }$ ；one would then have concluded $d V / d \tau = ( \pmb { \nabla } \cdot \pmb { u } ) V$ and one could have invoked the equivalence principle to move this law into curved spacetime.]

# Exercise 22.2. EQUATION OF CONTINUITY

Show that in the nonrelativistic limit in flat spacetime the equation of baryon conservation (22.3) becomes the “equation of continuity”

$$
\frac { \partial n } { \partial t } + \frac { \partial } { \partial x ^ { j } } ( n v ^ { j } ) = 0 .
$$

# Exercise 22.3. CHEMICAL POTENTIAL FOR IDEAL FERMI GAS

Show that the chemical potential of an ideal Fermi gas, nonrelativistic or relativistic,is (at zero temperature) equal to the Fermi energy (energy of highest occupied momentum state) of that gas.

# Exercise 22.4. PROJECTION TENSORS

Show that contraction of a tangent vector $\pmb { B }$ with the “projection tensor” $\pmb { P } \equiv \pmb { g } + \pmb { u } \otimes \pmb { u }$ projects $\pmb { B }$ into the 3-surface orthogonal to the 4-velocity vector $\pmb { u }$ [Hint: perform the calculation in an orthonormal frame with $\pmb { e } _ { \hat { \imath } } = \pmb { \mu }$ and write $\pmb { { \cal B } } = { \cal B } ^ { \alpha } \pmb { e } _ { \alpha }$ ：then show that ${ \pmb P } \cdot { \pmb B } = B ^ { \dagger } { \pmb e } _ { \hat { \jmath } } . ]$ If $\pmb { n }$ is a unit spacelike vector, show that ${ \pmb { P } } \equiv { \pmb { g } } - { \pmb { n } } \otimes { \pmb { i } }$ n is the corresponding projection operator. Note: There is no unique concept of “the projection orthogonal to a null vector."Why? [Hint: draw pictures in flat spacetime suppressing one spatial dimension.]

# ExerciSe 22.5. PRESSURE GRADIENT IN STATIONARY GRAVITATIONAL FIELD

A perfect fuid is at rest (flow lines have $x ^ { j } =$ constant） in a stationary gravitational field (metric coefficients are independent of $x ^ { 0 }$ ). Show that the pressure gradient required to “support the fluid against gravity” (i.e., to make its flow lines be $x ^ { j } =$ constant instead of geodesics) is

$$
\frac { \partial p } { \partial x ^ { 0 } } = 0 , \frac { \partial p } { \partial x ^ { j } } = - ( \rho + p ) \frac { \partial \ln \sqrt { - g _ { 0 0 } } } { \partial x ^ { j } } .
$$

Evaluate this pressure gradient in the Newtonian limit, using the coordinate system and metric coeficients of equation (18.15c).

# Exercise 22.6. EXPANSION，ROTATION，AND SHEAR

Let a field of fluid 4-velocities ${ \pmb u } ( { \pmb \mathcal { G } } )$ be given.

(a) Show that $\yen 4$ can be decomposed in the following manner:

$$
u _ { \alpha ; \beta } = \omega _ { \alpha \beta } + \sigma _ { \alpha \beta } + \frac { 1 } { 3 } \theta P _ { \alpha \beta } - a _ { \alpha } u _ { \beta } ,
$$

where a is the ${ \pmb { 4 } } .$ acceleration of the fluid

$$
a _ { \alpha } \equiv u _ { \alpha ; \beta } u ^ { \beta } ,
$$

$\pmb \theta$ is the “expansion”of the fuid world lines

$$
\begin{array} { r } { \pmb { \theta } \equiv \pmb { \nabla } { \cdot } \pmb { u } = \pmb { u } ^ { \alpha } { } _ { ; \alpha } , } \end{array}
$$

$P _ { \alpha \beta }$ is the projection tensor

$$
P _ { \alpha \beta } \equiv g _ { \alpha \beta } + u _ { \alpha } u _ { \beta } ,
$$

$\sigma _ { \alpha \beta }$ is the shear tensor of the fluid

$$
\sigma _ { \alpha \beta } \equiv \frac { 1 } { 2 } ( u _ { \alpha ; \mu } { P ^ { \mu } } _ { \beta } + u _ { \beta ; \mu } { P ^ { \mu } } _ { \alpha } ) - \frac { 1 } { 3 } \theta P _ { \alpha \beta } ,
$$

and $\omega _ { \alpha \beta }$ is the rotation 2-form of the fuid

$$
\omega _ { \alpha \beta } \equiv \frac { 1 } { 2 } ( u _ { \alpha ; \mu } { P ^ { \mu } } _ { \beta } - u _ { \beta ; \mu } { P ^ { \mu } } _ { \alpha } ) .
$$

(b) Each of the component parts of this decomposition has a simple physical interpretation in the local rest frames of the fluid.The interpretation of the 4-acceleration $\pmb { a }$ in terms of accelerometer readings should be familiar. Exercise 22.l showed that the expansion $\pmb { \theta } = \pmb { \nabla } \cdot \pmb { u }$ describes the rate of increase of the volume of a fuid element,

$$
\theta = ( 1 / V ) ( d V / d \tau ) .
$$

Exercise 22.4 explored the meaning and use of the projection tensor $\pmb { P } .$ Verify that in a local Lorentz frame $\dot { ( } g _ { \hat { \alpha } \beta } = \eta _ { \alpha \beta } , \Gamma ^ { \hat { \alpha } } { } _ { \beta \hat { \gamma } } \stackrel { \smile } { = } 0 )$ momentarily moving with the fluid $\dot { ( u ^ { \alpha } } = \delta ^ { \alpha } { } _ { 0 } )$ ， $\sigma _ { \hat { \alpha } \beta }$ and $\omega _ { \hat { \alpha } \hat { \beta } }$ reduce to the classical (nonrelativistic) shear and rotation of the fluid.[See, e.g, $\ S 8 2 . 4$ and 2.5of Ellis (197l） for both classical and relativistic descriptions of shear and rotation.]

# Exercise 22.7. HYDRODYNAMICS WITH VISCOSITY AND HEAT FLOW.\*

(a)In $\ S 1 S$ of Landau and Lifshitz (l959),one finds an analysis of viscous stresses for'a classical (nonrelativistic) fluid.By carrying that analysis over directly to the local Lorentz rest frame of a relativistic fluid, and by then generalizing to frame-independent language, show that the contribution of viscosity to the stress-energy tensor is

$$
\begin{array} { r } { \pmb { T } ^ { \mathrm { ( v i s c ) } } = - 2 \eta \pmb { \sigma } - \zeta \pmb { \theta } \pmb { P } , } \end{array}
$$

where $\eta \geq 0$ is the“coefficientofdynamic viscosity"; $\zeta \geq 0$ is the“coefficient ofbulk viscosity";   
and $\sigma , \theta , P$ are the shear, expansion,and projection tensor of the fluid.

(b) An idealized description of heat flow in a fluid introduces the heat-flux 4-vector q with components in the local rest-frame of the fluid,

$$
q _ { \cdot } ^ { \widehat { \boldsymbol { \mathfrak { \mathfrak { \varphi } } } } } = 0 , \qquad q ^ { \widehat { \boldsymbol { \mathfrak { \mathfrak { j } } } } } = \left( \operatorname * { e n e r g y } _ { \mathrm { s u r f a c e \ p e r \ u n i t \ t i m e \ c r o s s i n g \ u n i t } } \right) .
$$

By generalizing from the fluid rest frame to frame-independent language,show that the contribution of heat flux to the stress-energy tensor is

$$
\pmb { T } ^ { ( \mathrm { b e a t } ) } = \pmb { u } \otimes \pmb { q } + \pmb { q } \otimes \pmb { u } .
$$

Thereby conclude that, in this idealized picture,the stress-energy tensor for a viscous fluid with heat conduction is

$$
T ^ { \alpha \beta } = \rho u ^ { \alpha } u ^ { \beta } + ( p - \xi \theta ) { \cal P } ^ { \alpha \beta } - 2 \eta \sigma ^ { \alpha \beta } + q ^ { \alpha } u ^ { \beta } + u ^ { \alpha } q ^ { \beta } .
$$

(c) Define the entropy 4-vector $\pmb { s }$ by

$$
{ \pmb s } \equiv n s { \pmb u } + { \pmb q } / T .
$$

By calculations in the local rest-frame of the fluid, show that

$$
\begin{array} { r l } & { { \pmb \nabla } \cdot { \pmb s } = \left( \mathrm { \mathop { r a t e ~ o f ~ i n c r e a s e ~ o f ~ e n t r o p y } } \right) - \left( \mathrm { r a t e ~ a t ~ w h i c h ~ h e a t ~ a n d ~ f u i d } \right. } \\ & { \left. \qquad \mathrm { ( c a r r y ~ e n t r o ~ a ~ u n i t ~ v o l u m e ) } \right. } \\ & { \qquad = \left( \mathrm { r a t e ~ a t ~ w h i c h ~ e n t r o p y ~ i s ~ b e i n g } \right) . } \\ & { \qquad \left. ( 2 \mathrm { e n e r a t e d ~ i n ~ a ~ u n i t ~ v o l u m e } \right. } \end{array}
$$

Thereby arrive at the following form of the second law of thermodynamics:

$$
{ \pmb { \nabla } } \cdot { \pmb { s } } \geq 0 .
$$

(d) Calculate the law of local energy conservation, $\pmb { \mu } \cdot \pmb { \nabla } \pmb { \cdot } \pmb { \tau } = 0$ ,for a viscous fluid with heat flow. Combine with the first law of thermodynamics and with the law of baryon conservation to obtain

$$
T \Psi \cdot s = \xi \theta ^ { 2 } + 2 \eta \sigma _ { \alpha \beta } \sigma ^ { \alpha \beta } - q ^ { \alpha } ( T _ { , \alpha } / T + a _ { \alpha } ) .
$$

Interpret each term of this equation as a contribution to entropy generation (example: $2 \eta \sigma _ { \alpha \beta } \sigma ^ { \alpha \beta }$ describes entropy generation by viscous heating). [Note: The term $q ^ { \alpha } a _ { \alpha }$ is relativistic in origin.It is associated with the inertia of the flowing heat.]

(e) When one takes account of the inertia of the flowing heat, one obtains the following generalization of the classical law of heat conduction:

$$
q ^ { \alpha } = - \kappa P ^ { \alpha \beta } ( T _ { , \beta } + T a _ { \beta } )
$$

(Eckart 1940). Here $\kappa$ is the coefficient of thermal conductivity. Use this equation to show that,for a fuid at rest in a-stationary gravitational field (Exercise 22.5),

$$
q _ { 0 } = 0 , \qquad q _ { j } = - \frac { \kappa } { \sqrt { - g _ { 0 0 } } } ( T \sqrt { - g _ { 0 0 } } ) _ { , j } .
$$

[Thus,thermal equilibrium corresponds not to constant temperature,but to the redshifted temperature distribution ${ \cal T } \sqrt { - g _ { 0 0 } } =$ constant; Tolman (1934a), p.313.] Also,use the idealized law of heat conduction (22.16i) to reexpress the rate of entropy generation as

$$
\begin{array} { r l } & { T \mathbf { \nabla } \cdot \mathbf { s } = \xi \theta ^ { 2 } + 2 \eta \sigma _ { \alpha \beta } \sigma ^ { \alpha \beta } + ( \kappa / T ) P ^ { \alpha \beta } ( T _ { , \alpha } + T a _ { \alpha } ) ( T _ { , \beta } + T a _ { \beta } ) } \\ & { \quad \quad \geq 0 . } \end{array}
$$

[For further details about heat flow and for discussions of the limitations of the above idealized description,see e.g., $\ S 4 . 1 8$ of Ehlers (1971)； also Marle (1969),Anderson (1970), Stewart (197l),and papers cited therein.]

Electric and magnetic fields

# \$22.4. ELECTRODYNAMICS IN CURVED SPACETIME

In a local Lorentz frame in the presence of gravity, an observer can measure the electric and magnetic fields $\pmb { \cal E }$ and $\pmb { B }$ using the usual Lorentz force law for charged particles. As in special relativity, he can regard $\pmb { \cal E }$ and $\pmb { B }$ as components of an electromagnetic field tensor,

$$
F ^ { \hat { 0 } \hat { \dagger } } = - F ^ { \hat { j } \hat { 0 } } = E ^ { \hat { j } } , \qquad F ^ { \hat { j } \hat { k } } = \epsilon ^ { \hat { j } \hat { k } \hat { l } } B ^ { \hat { l } } ; \cdots
$$

he can regard the charge and current densities as components of a 4-vector $J ^ { \hat { \alpha } }$ and he can write Maxwell's equations and the Lorentz force equation in the special relativistic form,

$$
F ^ { \hat { \alpha } \hat { \beta } } { } _ { , \hat { \beta } } = 4 \pi J ^ { \hat { \alpha } } , \qquad F _ { \hat { \alpha } \hat { \beta } , \hat { \gamma } } + F _ { \hat { \beta } \hat { \gamma } , \hat { \alpha } } + F _ { \hat { \gamma } \hat { \alpha } , \hat { \beta } } = 0 ,
$$

$$
m a ^ { \hat { \alpha } } \doteq F ^ { \hat { \alpha } \hat { \beta } } q u _ { \hat { \beta } } \qquad \left( { m = { \mathrm { m a s s ~ o f ~ p a r t i c l e } } , q = { \mathrm { c h a r g e } } , \atop { u ^ { \hat { \alpha } } = 4 \mathrm { - v e l o c i t y } , a ^ { \hat { \alpha } } = 4 \mathrm { - a c c e l e r a t i o n } } } \right) .
$$

Maxwell equations and Lorentz force law

In any other frame these equations will have the same form, but with commas replaced by semicolons

$$
\begin{array} { c } { { F ^ { \alpha \beta } { } _ { ; \beta } = 4 \pi J ^ { \alpha } , } } \\ { { { } } } \\ { { F _ { \alpha \beta ; \gamma } + F _ { \beta \gamma ; \alpha } + F _ { \gamma \alpha ; \beta } = 0 , } } \\ { { { } } } \\ { { m a ^ { \alpha } = F ^ { \alpha \beta } q \dot { u } _ { \beta } . } } \end{array}
$$

These are the basic equations of electrodynamics in the presence of gravity. From them follws everything else. For example,as in special relativity, so also here (exercise 22.9), they imply the equation of charge conservation

$$
J ^ { \alpha } { } _ { ; \alpha } = 0 ;
$$

and for an electromagnetic field interacting with charged matter (exercise 22.10) they imply vanishing divergence for the sum of the stress-energy tensors

$$
( T ^ { ( \mathrm { E M } ) \alpha \beta } + T ^ { ( \mathrm { M A T T E R } ) \alpha \beta } ) _ { ; \beta } = 0 .
$$

Local conservation of energy-momentum

As in special relativity, so also here, one can introduce a vector potential $A ^ { \mu }$ Replacing commas by semicolons in the usual special-relativistic expression for $F ^ { \mu \nu }$ in terms of $A ^ { \mu }$ ，one obtains

Vector potential

$$
F _ { \mu \nu } = A _ { \nu ; \mu } - A _ { \mu ; \nu } .
$$

If allis well, this equation should guarantee (as in special relativity) that the Maxwell equations (22.17b) are satisfied.Indeed, it does,as one sees in exercise 22.8.To derive the wave equation that governs the vector potential, insert expression (22.l9a) into the remaining Maxwell equations (22.17a), obtaining

$$
- { A ^ { \alpha ; \beta } } _ { \beta } + { A ^ { \beta ; \alpha } } _ { \beta } = 4 \pi J ^ { \alpha } ;
$$

then commute covariant derivatives in the first term using the identity (l6.6c), to obtain

$$
- { A ^ { \alpha ; \mu } } _ { \mu } + { A ^ { \mu } } _ { ; \mu } { } ^ { ; \alpha } + { R ^ { \alpha } } _ { \mu } A ^ { \mu } = 4 \pi J ^ { \alpha } .
$$

Finally, adopting the standard approach of special relativity, impose the Lorentz gauge condition

$$
{ A ^ { \mu } } _ { ; \mu } = 0 ,
$$

Lorentz gauge condition

thereby bringing the wave equation (2.19b) into the form

$$
( { \cal { A } } _ { d R } { \cal { A } } ) ^ { \alpha } \equiv - { \cal { A } } ^ { \alpha ; \beta } { } _ { \beta } + R ^ { \alpha } { } _ { \beta } { \cal { A } } ^ { \beta } = 4 \pi J ^ { \alpha } .
$$

Wave equation for vector potential

The “de Rham vector wave operator” A which appears here is, apart from sign, a generalized d'Alambertian for vectors in curved spacetime.Mathematically it is more powerful han $- A ^ { \alpha ; \beta } { } _ { ; \beta }$ andthananyotheroperatorthatreducesto(minus) the d'Alambertian in special relativity.[For a discussion, see de Rham (1955).]

Although the electrodynamic equations (22.17a)-(22.19b) are all obtained from special relativity by the comma-goes-to-semicolon rule, the wave equation (22.19d) for the vector potential is not ("curvature coupling"; see Box l6.1). Nevertheless, .when spacetime is flat (so $R ^ { \alpha } { } _ { \beta } = 0 \rangle$ ,(22.19d) does reduce to the usual wave equation of special relativity.

# Exercise 22.8. THE VECTOR POTENTIAL FOR ELECTRODYNAMICS

Show that in any coordinate frame the connection coefficients cancel out of both equations (22.19a) and (22.17b),so they can be written

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 .
$$

$$
F _ { \mu \nu } = A _ { \nu , \mu } - A _ { \mu , \nu } ,
$$

# EXERCISES

(ln the language of differential forms these equations are ${ \pmb F } = \pmb { d A }$ ， $\begin{array} { r } { \pmb { d } \pmb { F } = 0 . } \end{array}$ ）Then use this form of the equations to show that equation (2.19a) implies equation (22.17b), as asserted in the text.

# ExerciSe 22.9. CHARGE CONSERVATION·IN THE PRESENCE OF GRAVITY

Show that Maxwel's equations (22.17a,b) imply the equation of charge conservation (22.18a) when gravity is present, just as they do in special relativity theory.[Hints: Use the antisymmetry of $F ^ { \alpha \beta }$ ； and beware of the noncommutation of the covariant derivatives, which must be handled using equations (16.6). Alternatively,show that in coordinate frames,equation (22.17a) can be written as

$$
\frac { 1 } { \sqrt { | g | } } \frac { \partial } { \partial x ^ { \beta } } ( \sqrt { | g | } F ^ { \alpha \beta } ) = 4 \pi J ^ { \alpha }
$$

and (22.18a) as

$$
{ J ^ { \alpha } } _ { ; \alpha } \equiv \frac { 1 } { \sqrt { | g | } } \frac { \partial } { \partial x ^ { \alpha } } \left( \sqrt { | g | } J ^ { \alpha } \right) = 0 ,
$$

and carry out the demonstration in a coordinate frame.]

# ExerCise 22.1O. INTERACTING ELECTROMAGNETIC FIELDAND CHARGED MATTER

As in special relativity， so also in the presence of gravity (equivalence principle"),the stress-energy tensor for an electromagnetic field is

$$
T ^ { \mathrm { ( E M ) } } { } _ { \alpha \beta } = \frac { 1 } { 4 \pi } \bigg ( F _ { \alpha \mu } F _ { \beta } { } ^ { \mu } - \frac { 1 } { 4 } F _ { \mu \nu } F ^ { \mu \nu } g _ { \alpha \beta } \bigg ) .
$$

Use Maxwell's equations (22.17a,b) in the presence of gravity to show that

$$
T ^ { ( \mathrm { E M } ) \alpha \beta } { } _ { ; \beta } = - F ^ { \alpha \beta } J _ { \beta } .
$$

But $F ^ { \alpha \beta } J _ { \beta }$ is just the Lorentz 4-force per unit volume with which the electromagnetic field acts on the charged mater [see the Lorentz force equation (22.l7c)； also equation (5.43)}; i.e.,it is T(MATTER)aβ. ;B Consequently,the above equation can be rewritten in the form (22.18b) cited in the text.

# \$22.5. GEOMETRIC OPTICS IN CURVED SPACETIME\*

Radio waves from the quasar 3C279 pass near the sun and get deflected by its gravitational field. Light rays emitted by newborn galaxies long ago and far away propagate through the cosmologically curved spacetime of the universe,and get focused (and redshifted) producing curvature-enlarged (but dim) images of the galaxies on the Earth's sky.

These and most other instances of the propagation of light and radio waves are subject to the laws of geometric optics. This section derives those laws, in curved spacetime, from Maxwell's equations.

The fundamental laws of geometric optics are: (1) light rays are null geodesics; (2) the polarization vector is perpendicular to the rays and is parallel-propagated along the rays; and (3) the amplitude is governed by an adiabatic invariant which, in quantum language, states that the number of photons is conserved.

The conditions under which these laws hold are defined by conditions on three lengths: (l) the typical reduced wavelength of the waves,

$$
\lambda \equiv \frac { \lambda } { 2 \pi } = \binom { \mathrm { { * c l a s s i c a l ~ d i s t a n c e ~ o f ~ c l o s e s t ~ a p p r o a c h ~ f o r } } } { a \ p h o t o n \ w i t h \ o n e \ u n i t \ o f \ a n g u l a r \ m o m e n t u m ^ { \prime } } \Big ) ,
$$

as measured in a typical local Lorentz frame (e.g., a frame at rest relative to nearby galaxies)； (2) the typical length $\mathcal { L }$ over which the amplitude, polarization,and wavelength of the waves vary, e.g., the radius of curvature of a wave front, or the length of a wave packet produced by a sudden outburst in a quasar; (3) the typical radius of curvature $\mathcal { R }$ of the spacetime through which the waves propagate,

$$
\mathcal { R } \equiv \left| \operatorname * { t y p i c a l \ c o m p o n e n t \ o f } \ R i e m a n n \mathrm { \ a s \ m e a s u r e d } \right| ^ { - 1 / 2 } .
$$

Overview of geometric optics

Conditions for validity of geometric optics

Geometric optics is valid whenever the reduced wavelength is very short compared to each of the other scales present,

$$
\lambda \ll \mathcal { L } \mathrm { a n d } \lambda \ll \mathcal { R } ,
$$

so that the waves can be regarded locally as plane waves propagating through spacetime of negligible curvature.

Mathematically one exploits the geometric-optics assumption, $\lambda \ll \mathcal { L }$ and $\lambda \ll \mathcal { R }$ ， as follows. Focus attention on waves that are highly monochromatic over regions $\lesssim \mathcal { L } .$ .(More complex spectra can be analyzed by superposition, i.e.,by Fourier analysis.)Split the vector potential of electromagnetic theory into a rapidly changing, real phase,

The "'two-length-scale" expansion underlying geometric optics

$$
\theta \sim ( \mathrm { d i s t a n c e } \ p r o p a g a t e d ) / \lambda ,
$$

and a slowly changing,complex amplitude(i.e. one with real and imaginary parts),

$$
\pmb { A } = \mathrm { R e a l ~ p a r t ~ o f } \{ \mathrm { a m p l i t u d e } \times e ^ { i \theta } \} \equiv \Re \{ \mathrm { a m p l i t u d e } \times e ^ { i \theta } \} .
$$

Imagine holding fixed the scale of the amplitude variation, $\mathcal { E }$ ,and the scale of the spacetime curvature, $\mathscr { R }$ ,while making the reduced wavelength, $\pmb { \lambda }$ ,shorter and shorter. The phase will get larger and larger $( \theta \propto 1 / \lambda )$ at any fixed event in spacetime, but the amplitude as a function oflocation in spacetime can remain virtually unchanged,

This circumstance allows one to expand the amplitude in powers of :\*

$$
\begin{array} { l } { { \mathrm { \bf ~ \Gamma ~ \ a m p u u u c = } \atop { \mathrm { \bf ~ \Gamma ~ } } } } \\ { { \mathrm { \bf ~ \Gamma ~ \ i n d e p e n d e n t { \bf \Gamma } } } } \\ { { \mathrm { \bf ~ \Gamma ~ \ o f ~ } \lambda } } \end{array} \nonumber
$$

The vector potential in geometric optics

[Actually, the expansion proceeds in powers of the dimensionless number

$$
\lambda / ( \mathrm { m i n i m u m ~ o f } \ \mathcal { L } \ \mathrm { ~ a n d ~ } \ \mathcal { R } ) \equiv \lambda / L .
$$

Applied mathematicians call this a “two-length-scale expansion”；see,e.g., Cole (1968). The basic short-wavelength approximation here has a long history; see,e.g., Liouville (1837), Rayleigh (1912). Following a suggestion of Debye, it was applied to Max well's equations by Sommerfeld and Runge (l911). It is familiar as the WKB approximation in quantum mechanics,and has many other applications as indicated by the bibliography in Keller,Lewis,and Seckler (1956). The contribution of higher order terms is considered by Kline (l954) and Lewis (l958). See especially the book of Froman and Froman (1965).]

It is useful to introduce a parameter ε that keeps track of how rapidly various terms approach zero (or infinity) as $\pmb { \lambda } / L$ approaches zero:

$$
A _ { \mu } = \mathfrak { R } \{ ( a _ { \mu } + \varepsilon b _ { \mu } + \varepsilon ^ { 2 } c _ { \mu } + \cdot \cdot \cdot ) e ^ { { \mathrm { i } } \theta / { \varepsilon } } \} .
$$

Any term with a factor $\varepsilon ^ { n }$ in front of it varies as $( { \pmb { \chi } } / L ) ^ { n }$ in the limit of very small wavelengths $[ \theta \propto ( \pmb { \lambda } / L ) ^ { - 1 }$ ； $c _ { \mu } \propto ( \dot { x } / L ) ^ { 2 }$ ; etc.].By convention,ε is a dummy expan-sion parameter with eventual value unity; so it can be dropped from the calculations when it ceases to be useful. And by convention, all “post-geometric-optics correc-tions" are put into the amplitude terms b, c,...； none are put into $\pmb \theta$

Note that,while the phase $\pmb \theta$ is a real function of position in spacetime, the amplitude and hence the vectors $\pmb { a }$ ,b, c,...are complex. For example, to describe monochromatic waves with righthand circular polarization,propagating in the $_ { z }$ direction, one could set $\theta = \omega ( z - t )$ and $a = \dot { 1 / \sqrt { 2 } } a ( { \pmb e } _ { x } + \dot { i \pmb e } _ { y } )$ with $\pmb { a }$ real; so‘

$$
A = \Re \left\{ { \frac { 1 } { \sqrt { 2 } } } a ( e _ { x } + i e _ { y } ) e ^ { i \omega ( z - t ) } \right\} = { \frac { 1 } { \sqrt { 2 } } } a \{ \cos \left[ \omega ( z - t ) \right] e _ { x } - \sin \left[ \omega ( z - t ) \right] e _ { y } \}
$$

The assumed form (22.25) for the vector potential is the mathematical foundation of geometric optics. All the key equations of geometric optics result from inserting this vector potential into the source-free wave equation $\pmb { \mathscr { A } } = 0$ [equation (22.19d)] and into the Lorentz gauge condition $\pmb { \nabla } \cdot \pmb { A } = 0$ [equation (22.19c)]. The resulting equations (derived below) take their simplest form only when expressed in terms of the following:

Basic concepts of geometric optics:

"polarization vector,” ${ \pmb f } \equiv { \pmb a } / a =$ "unit complex vector along a".

(Here ā is the complex conjugate of $\pmb { a }$ ) Light rays are defined to be the curves $\mathcal { P } ( \lambda )$ normal to surfaces of constant phase $\pmb \theta$ Since $\pmb { k } \equiv \pmb { \nabla } \theta$ is the normal to these surfaces, the differential equation for a light ray is

(4) light rays

$$
{ \frac { d x ^ { \mu } } { d \lambda } } = k ^ { \mu } ( x ) = g ^ { \mu \nu } ( x ) \theta _ { , \nu } ( x ) .
$$

Box 22.3,appropriate for study at this point, shows the polarization vector, wave vector, surfaces of constant phase,and light rays for a propagating wave; the scalar amplitude, not shown there, merely tells the length of the vector amplitude a.Insight into the complex polarization vector, if not familiar from electrodynamics,can be developed later in Exercise 22.12.

So much for the foundations. Now for the calculations. First insert the geometricoptics vector potential (22.25) into the Lorentz gauge condition:

Derivation of laws of geometric optics

$$
0 = { A ^ { \mu } } _ { ; \mu } = \Re \left\{ \left[ { \frac { i } { \varepsilon } } k _ { \mu } ( a ^ { \mu } + \varepsilon b ^ { \mu } + \cdot \cdot \cdot ) + ( a ^ { \mu } + \varepsilon b ^ { \mu } + \cdot \cdot \cdot ) _ { ; \mu } \right] e ^ { \mathrm { i } \theta / \varepsilon } \right\} .
$$

The leading term (order $1 / \varepsilon$ says

$$
{ \bf { k \cdot a } } = 0 ~ ( a m p l i t u d e ~ i s ~ p e r p e n d i c u l a r ~ t o ~ w a v e ~ v e c t o r ) ;
$$

or, equivalently

$$
{ \pmb k } \cdot { \pmb f } = 0 ~ ( p o l a r i z a t i o n ~ i s ~ p e r p e n d i c u l a r ~ t o ~ w a v e ~ v e c t o r ) .
$$

The post-geometric-optics breakdown in this orthogonality condition is governed by the higher-order terms $[ 0 ( 1 ) , \ 0 ( \varepsilon ) , \ 0 ( \varepsilon ^ { 2 } ) , \ldots ]$ in the gauge condition (22.27)；for example, the O(l) terms say

$$
\pmb { k } \cdot \pmb { b } = i \pmb { \nabla } \cdot \pmb { a } .
$$

Next insert the vector potential (22.25) into the source-free wave equation (22.19d):

$$
\begin{array} { r l } & { 0 = ( { \cal A } _ { d R } { \cal A } ) ^ { \alpha } = - { \cal A } ^ { \alpha ; \beta } { } _ { \beta } + { \cal R } ^ { \alpha } { } _ { \beta } { \cal A } ^ { \beta } } \\ { } & { ~ = \Re \left\{ \left[ \frac { 1 } { \varepsilon ^ { 2 } } k ^ { \beta } k _ { \beta } ( a ^ { \alpha } + \varepsilon b ^ { \alpha } + \varepsilon ^ { 2 } c ^ { \alpha } + \cdot \cdot \cdot ) - 2 \frac { i } { \varepsilon } k ^ { \beta } ( a ^ { \alpha } + \varepsilon b ^ { \alpha } + \cdot \cdot \cdot ) _ { ; \beta } \right. \right. } \\ { } & { \qquad \left. \left. - \frac { i } { \varepsilon } k ^ { \beta } { } _ { ; \beta } ( a ^ { \alpha } + \varepsilon b ^ { \alpha } + \cdot \cdot \cdot ) - ( a ^ { \alpha } + \cdot \cdot \cdot ) ^ { ; \beta } { } _ { \beta } + { \cal R } ^ { \alpha } { } _ { \beta } ( a ^ { \beta } + \cdot \cdot \cdot ) \right] e ^ { \mathrm { i } \theta / \varepsilon } \right\} . } \end{array}
$$

Collect terms of order $1 / \varepsilon ^ { 2 }$ and $1 / \varepsilon$ (terms of order higher than $1 / \varepsilon$ govern postgeometric-optics corrections):

(continued on page 576)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/794db3806a7d0feda19d06b47ed12076f074c8ff9d8ddec1a0960382f721f4dd.jpg)  
Box 22.3 GEOMETRY OF AN ELECTROMAGNETIC WAVE TRAIN   
one wavelength, $2 \pi \lambda$ ， as seen in local Lorentz frame

direction of propagation as seen in local Lorentz frame

The drawing shows surfaces of constant phase, $\theta =$ constant, emerging through the “surface of simultaneity", $t = 0$ , of a local Lorentz frame. The surfaces shown are alternately “crests” $( \theta = 1 7 6 4 \pi$ ， $\theta = 1 7 6 6 \pi , \ldots .$ and“troughs” $( \theta = 1 7 6 5 \pi _ { ; }$ $\theta =$ $1 7 6 7 \pi , \ldots )$ of the wave train. These surfaces make up a 1-form, $\widetilde { \pmb { k } } = \pmb { d } \pmb { \theta }$ The "corresponding vector” $\pmb { k } = \pmb { \nabla } \theta$ is the “wave vector." The wave vector is null, $\pmb { k } \cdot \pmb { k } = 0$ ,according to Maxwell's equations [equation (22.30). Therefore it lies in a surface of constant phase:

$$
{ \binom { \mathrm { n u m b e r ~ o f ~ s u r f a c e s } } { \mathrm { p i e r c e d ~ b y ~ } k } } = \langle d \theta , k \rangle = \langle \widetilde { k } , k \rangle = { k \cdot k } = 0 .
$$

But not only does it lie in a surface of constant phase; it is also perpendicular to that surface! Any vector $\pmb { \nu }$ in that surface must satisfy $\pmb { k } \cdot \pmb { v } = \langle \widetilde { \pmb { k } } , \pmb { v } \rangle \doteq \langle \pmb { d } \theta , \pmb { v } \rangle = 0$ because it pierces no surfaces.

Geometric optics assumes that the reduced wavelength $\pmb { \lambda }$ ,as measured in a typical local Lorentz frame, is small compared to the scale $\mathcal { L }$ of inhomogeneities in the wave train and small compared to the radius of curvature of spacetime, $\mathcal { R }$ Thus, over regions much larger than $\pmb { \lambda }$ but smaller than $\mathcal { L }$ or $\mathcal { R }$ , the waves are plane-fronted and monochromatic,and there exist Lorentz reference frames (Riemann normal coordinates). In one of these “extended" local Lorentz frames, the phase must be

$$
\theta = k _ { \alpha } x ^ { \alpha } + \mathrm { c o n s t a n t } ;
$$

no other expression will yield ${ \overline { { \mathbf { \nabla } } } } \pmb { \nabla } \theta = \pmb { k } .$ . The corresponding vector potential [equation (22.25)] will be

$$
{ \cal A } ^ { \mu } = \Re \left\{ a ^ { \mu } \exp [ i ( k \cdot x - k ^ { 0 } t ) ] \right\} + ( { } ^ { \mathrm { * * } } \mathrm { p o s t . } \mathrm { g e o m e t r i c \mathrm { - } o p t i c s ~ c o r r e c t i o n s " } ) ;
$$

hence,

$$
\begin{array} { c } { k ^ { 0 } = 2 \pi / ( \mathrm { p e r i o d ~ o f ~ w a v e } ) = 2 \pi \nu = \omega \equiv ( \mathrm { a n g u l a r ~ f r e q } } \\ { \left| k \right| = 2 \pi / ( \mathrm { w a v e l e n g t h ~ o f ~ w a v e } ) = 1 / \lambda = \omega , } \end{array}
$$

At each event in spacetime there is a wave vector; and these wave vectors, tacked end-on-end, form a family of curves-the “light rays”or simply “rays”-whose tangent vector is $\pmb { k }$ .The rays,like their tangent vector,lie both in and perpendicular to the surfaces of constant phase.

The affine parameter $\lambda$ of a ray (not to be confused with wavelength $= 2 \pi \lambda$ satisfies $\pmb { k } = \bar { d } / d \lambda$ ; therefore it is given by

$$
\lambda = t / k ^ { 0 } + \mathrm { c o n s t a n t } = t / \omega + \mathrm { c o n s t a n t } ,
$$

where $t$ is proper time along the ray as measured, not by the ray itself (its proper time is zero!), but by the local Lorentz observer who sees angular frequency $\omega .$ Thus, while $\pmb { \omega }$ is a frame-dependent quantity and $t$ is also a frame-dependent quantity, their quotient $t / \omega$ when measured along the ray (not off the ray) is the frame-independent affine parameter. For a particle it is possible and natural to identify the affine parameter $\lambda$ with proper time $\tau$ .For a light ray this identification is unnatural and impossible. The lapse of proper time along the ray is identically zero. The springing up of $\lambda$ to take the place of the vanished $\pmb { \tau }$ gives one a tool to do what one might not have suspected to be possible. Given a light ray shot out at event $\boldsymbol { \mathcal { Q } }$ and passing through event $\mathcal { B }$ , one can give a third event $\mathcal { C }$ along the same null world line that is twice as“far” from $\boldsymbol { \mathcal { Q } }$ as $\mathcal { B }$ is “far,” in a new sense of“far” that has nothing whatever directly to do with proper time (zero!), but is defined by equal increments of the affine parameter $( \lambda _ { \mathfrak { c } } - \lambda _ { \mathfrak { r } } = \lambda _ { \mathfrak { s } } - \lambda _ { \mathfrak { c } } )$ .The “affine parameter” has a meaning for any null geodesic analyzed even in isolation. In this respect, it is to be distinguished from the so-called “luminosity distance”which is sometimes introduced in dealing with the propagation of radiation through curved spacetime, and which is defined by the spreading apart of two or more light rays coming from a common source.

Maxwell's equations as explored in the text [equation (22.28')] guarantee that the complex polarization vector $\pmb { \mathscr { f } }$ is perpendicular to the wave vector $\pmb { k }$ and that, therefore, it lies in a surface of constant phase (see drawing). Intuition into the polarization vector is developed in exercise 22.12.

$$
\scriptstyle 0 \left( { \frac { 1 } { \varepsilon ^ { 2 } } } \right) :
$$

$$
k ^ { \beta } k _ { \beta } a ^ { \alpha } = 0
$$

$\implies \boldsymbol { k } \cdot \boldsymbol { k } = 0$ (wave vector is null);

$$
\scriptstyle 0 \left( { \frac { 1 } { \varepsilon } } \right) ;
$$

$$
\begin{array} { r l } & { \frac { 1 } { \varepsilon } \bigg ) : \qquad \underbrace { k ^ { \beta } k _ { \beta } b ^ { \alpha } - 2 i \Big ( k ^ { \beta } a ^ { \alpha } { } _ { ; \beta } + \frac { 1 } { 2 } k ^ { \beta } { } _ { ; \beta } a ^ { \alpha } \Big ) } _ { \dot { \mathbb { L } } \left[ = \ 0 \right] } = 0 } \\ & { \implies \Psi _ { k } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a \ ( p r o p a g a t i o n \ e q u a t i o n \ f o r \ v e c t o r \ a m p l i t u d e ) . } \end{array}
$$

These equations (22.30,22.31） together with equation (22.28) are the basis from which all subsequent results will follow. As a first consequence,one can obtain the geodesic law from equation (22.30). Form the gradient of $\pmb { k } \cdot \pmb { k } = 0$ ，

$$
0 = ( k ^ { \beta } k _ { \beta } ) _ { ; \alpha } = 2 k ^ { \beta } k _ { \beta ; \alpha } ,
$$

and use the fact that $k _ { \beta } \equiv \theta _ { , \beta }$ is the gradient of a scalar to interchange indices, $\theta _ { ; \beta \alpha } = \theta _ { ; \alpha \beta }$ 0r

$$
0 = k ^ { \beta } k _ { \beta ; \alpha } = k ^ { \beta } k _ { \alpha ; \beta } .
$$

The main laws of geometric optics:

The result is

$$
\Psi _ { k } k = 0 ~ ( p r o p a g a t i o n ~ e q u a t i o n ~ f o r ~ w a v e ~ v e c t o r ) .
$$

(1） Light rays are null geodesics

Notice that this is the geodesic equation! Combined with equation (22.30),it is the statement, derived from Maxwel's equations in curved spacetime, that light rays are null geodesics, the first main result of geometric optics.

Turn now from the propagation vector $\pmb { k } = \pmb { \nabla } \theta$ to the wave amplitude $a = a f ,$ and obtain separate equations for the magnitude $^ { a }$ and polarization f. Use equation (22.31) to compute

$$
\begin{array} { l } { { 2 a \widehat { \circ } _ { \pmb { \partial } _ { k } a } = 2 a \pmb { \nabla } _ { k } a = \pmb { \nabla } _ { k } a ^ { 2 } = \pmb { \nabla } _ { k } ( a \cdot \overrightarrow { a } ) = \overline { { a } } \cdot \pmb { \nabla } _ { k } a + a \cdot \pmb { \nabla } _ { k } \overrightarrow { a } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = - \displaystyle \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) ( \overline { { a } } \cdot \pmb { a } + a \cdot \overrightarrow { a } ) = - a ^ { 2 } \pmb { \nabla } \cdot \pmb { k } ; } } \end{array}
$$

so

$$
\hat { v } _ { k } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a ( p r o p a g a t i o n ~ e q u a t i o n ~ f o r ~ s c a l a r ~ a m p l i t u d e ) ,
$$

Next write $\bullet = a \bullet$ in equation (22.31) to obtain

$$
0 = \boldsymbol { \nabla } _ { k } ( a t ) + \frac { 1 } { 2 } \left( \boldsymbol { \nabla } \cdot \boldsymbol { k } \right) a t = a \boldsymbol { \nabla } _ { k } t + \frac { 1 } { t } \left[ \boldsymbol { \nabla } _ { k } a + \frac { 1 } { 2 } \left( \boldsymbol { \nabla } \cdot \boldsymbol { k } \right) a \right] = a \boldsymbol { \nabla } _ { k } t
$$

$$
\pmb { \nabla } _ { k } \pmb { f } = 0 \ ( p r o p a g a t i o n \ e q u a t i o n \ f o r \ p o l a r i z a t i o n \ v e c t o r ) .
$$

This together with equation (22.28), constitutes the second main result of geometric optics,that the polarization vector is perpendicular to the rays and is parallel-propagated along the rays. It is now possible to see that these results,derived from equations (22.30) and (22.31) are consistent with the gauge condition (22.28). The vectors $\pmb { k }$ and $\pmb { \mathscr { f } } ,$ specifed at one point, are fixed along the entire ray by their propagation equations. But because both propagation equations are parallel-transport laws,the conditions $\pmb { k } \cdot \pmb { k } = 0$ ， ${ \pmb f } \cdot { \pmb { \bar { f } } } = 1$ ,and $\pmb { k } \cdot \pmb { f } = 0$ , once imposed on the vectors at one point, willbe satisfied along the entire ray.

The equation (22.33) for the scalar amplitude can be reformulated as a conservation law. Since $\partial _ { \pmb { k } } \equiv ( \pmb { k } \cdot \pmb { \nabla } )$ ,one rewrites the equation as $( \pmb { k } \cdot \pmb { \nabla } ) a ^ { 2 } + a ^ { 2 } \pmb { \nabla } \cdot \pmb { k } = 0$ ， or

(2)polarization vector is perpendicular to ray and is parallel propagated along ray

$$
\pmb { \nabla } \cdot ( a ^ { 2 } \pmb { k } ) = 0 .
$$

(3) conservation of \`photon number"

Consequently the vector $a ^ { 2 } \pmb { k }$ is a “conserved current,” and the integral $\displaystyle \int a ^ { 2 } k ^ { \mu } d ^ { 3 } { \textstyle \sum _ { \mu } }$ has a fixed, unchanging value for each 3-volume cutting a given tube formed of light rays. (The tube must be so formed of rays that an integral of $a ^ { 2 } k$ over the walls of the tube will give zero.) What is conserved? To remain purely classical, one could say it is the “number of light rays” and call $a ^ { 2 } k ^ { 0 }$ the“density of light rays” on an $x ^ { 0 } =$ constant hypersurface. But the proper correspondence and more concrete physical interpretation make one prefer to call equation (22.35) the law of conservation of photon number. It is the third main result of geometric optics.Photon number, of course, is not always conserved; it is an adiabatic invariant, a quantity that is not changed by influences (e.g., spacetime curvature, ${ \sim } 1 / \mathcal { R } ^ { 2 } )$ which change slowly $( { \mathcal { R } } \gg { \mathcal { X } } )$ compared to the photon frequency.

Box 22.4 summarizes the above equations of geometric optics,along with others derived in the exercises,

Exercise 22.11. ELECTROMAGNETIC FIELD AND STRESS ENERG Derive the equations given in part $\mathbf { D }$ of Box 22.4 for $\pmb { F } , \pmb { E } , \pmb { B }$ and $\pmb { \tau } .$

# Exercise 22.12. POLARIZATION

At an event ${ \mathfrak { P } } _ { 0 }$ through which geometric-optics waves are passing, introduce a local Lorentz frame with $\bar { \cdot }$ -axis along the direction of propagation. Then $\pmb { k } = \omega ( \pmb { e } _ { 0 } + \pmb { e } _ { z } )$ . Since the polarization vector is orthogonal to $\pmb { k }$ 、itis $\pmb { f } = f ^ { 0 } ( \pmb { e } _ { 0 } + \pmb { e } _ { z } ) + f ^ { 1 } \pmb { e } _ { z } + f ^ { 2 } \pmb { e } _ { y }$ and since $\dot { \pmb { f } } \cdot \pmb { \bar { f } } = 1$ it has $| f ^ { 1 } | ^ { 2 } + | f ^ { 2 } | ^ { 2 } = 1$

(a） Show that the component $f ^ { 0 }$ of the polarization vector has no influence on the electric and magnetic fields measured in the given frame;i.e., show that one can add a multiple of $\pmb { k }$ to $\pmb { \mathscr { f } }$ without affecting any physical measurements.

(continued on page 581)

# Box 22.4 GEOMETRIC OPTICS IN CURVED SPACETIME (Summary of Results Derived in Text and Exercises)

# A. Geometric Optics Assumption

Electromagnetic waves propagating in a source-free region of spacetime are locally plane-fronted and monochromatic (reduced wavelength $\lambda \ll$ scale $\mathcal { E }$ over which amplitude,wavelength, or polarization vary; and $\lambda \ll \Re =$ mean radius of curvature of spacetime).

# B. Rays, Phase,and Wave Vector (see Box 22.3)

Everything (amplitude, polarization, energy, etc.） is transported along rays; and the quantities on one ray do not influence the quantities on any other ray.

The rays are null geodesics of curved spacetime, with tangent vectors ("wave vectors")k:

$$
\pmb { \nabla } _ { \pmb { k } } \pmb { k } = 0 .
$$

The rays both lie in and are perpendicular to surfaces of constant phase, $\theta =$ const.;and their tangent vectors are the gradient of $\pmb \theta$ ：

$$
\pmb { k } = \pmb { \nabla } \pmb { \theta } .
$$

In a local Lorentz frame, $k ^ { 0 }$ is the“angular frequency" and $k ^ { 0 } / 2 \pi$ is the ordinary frequency of the waves, and

$$
{ \pmb n } = { \pmb k } / k ^ { 0 }
$$

is a unit 3-vector pointing along their direction of propagation.

# C. Amplitude and Polarization Vector

The waves are characterized by a real amplitude $_ { a }$ and a complex polarization vector $\pmb { \mathscr { f } }$ of unit length, $\pmb { \mathscr { f } } \cdot \bar { \pmb { f } } = 1$ .(Of the fundamental quantities $\theta , \kappa , a , \tilde { \prime } ,$ all are real except f. See exercise 22.12 for deeper understanding of $\pmb { \mathscr { f } } .$ ）

The polarization vector is everywhere orthogonal to the rays, $\pmb { k } \cdot \pmb { f } = 0$ ； and is parallel-transported along them, $\pmb { \nabla } _ { \pmb { k } } \pmb { f } = 0$

The propagation law for the amplitude is

$$
\partial _ { \pmb { k } } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a .
$$

This propagation law is equivalent to a law of conseruation of photons (classically: of rays)； $a ^ { 2 } k$ is the"“conserved current” satisfying $\pmb { \nabla } \pmb { \cdot } ( a ^ { 2 } \pmb { k } ) = 0$ ；and $( 8 \pi \hbar ) ^ { - 1 } \int a ^ { 2 } k ^ { 0 } \sqrt { | g | } d ^ { 3 } x$ is the number of photons (rays) in the 3-volume of integration on any $x ^ { 0 } =$ constant hypersurface,and is constant as this volume is carried along the rays.

The propagation law holds separately on each hypersurface of constant phase. There it can be interpreted as conservation of a $a ^ { 2 } { \mathcal { Q } }$ where $\boldsymbol { \mathscr { a } }$ is a two-dimensional cross-sectional area of a pulse of photons or rays. See exercise 22.13.

# D. Vector Potential, Electromagnetic Field, and Stress-Energy-Momentum

At any event the vector potential in Lorentz gauge is

$$
A = \Re \{ a e ^ { \mathsf { i } \theta } \pmb { \mathscr { f } } \} ,
$$

where R denotes the real part.

The electromagnetic field tensor is orthogonal to the rays, $\pmb { F } \cdot \pmb { k } = 0$ , and is given by

$$
{ \pmb F } = \Re \{ i a e ^ { i \theta } { \pmb k } \wedge { \pmb f } \} , \quad \_
$$

The corresponding electric and magnetic felds in any local Lorentz frame are

$$
\begin{array} { c } { { E = \Re \{ i a k ^ { 0 } e ^ { \mathrm { { i } } \theta } ( \mathrm { p r o j e c t i o n \ o f \ } f \mathrm { \ p e r p e n d i c u l a r \ t o \ } k ) \} , } } \\ { { B = n \times E , \mathrm { w h e r e \ } n \equiv k / k ^ { 0 } . } } \end{array}
$$

The stress-energy tensor, averaged over a wavelength, is

$$
\dot { \pmb { \tau } } = ( 1 \bar { / } 8 \bar { \pmb { \pi } } ) a ^ { 2 } \pmb { k } \otimes \pmb { k } ,
$$

corresponding to an energy density in a local Lorentz frame of

$$
T ^ { 0 0 } = ( 1 / 8 \pi ) ( a k ^ { 0 } ) ^ { 2 }
$$

and an energy flux of

$$
T ^ { 0 j } = T ^ { 0 0 } n ^ { j } , \ldots \ldots \ -
$$

that-cnergy flows along the rays (in ${ \pmb n } = { \pmb k } / k ^ { 0 }$ direction) with the speed of :ht. This is identical with the stress-energy tensor that would be produced by beam of photons with 4-momenta $\pmb { p } = \hbar \pmb { k }$

Conservation of energy-momentum $\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla  \end{array}$ follows from the ray conservation law $\pmb { \nabla } \pmb { \cdot } ( a ^ { 2 } \pmb { k } ) = 0$ and the geodesic law $\pmb { \nabla } _ { \pmb { k } } \pmb { k } \equiv ( \pmb { k } \cdot \pmb { \nabla } ) \pmb { k } = 0$ ：

$$
8 \pi \ \Psi \cdot T = \Psi \cdot ( a ^ { 2 } \pmb { k } \otimes \pmb { k } ) = [ \pmb { \nabla } \cdot ( a ^ { 2 } \pmb { k } ) ] \pmb { k } + a ^ { 2 } ( \pmb { k } \cdot \pmb { \nabla } ) \pmb { k } = 0 .
$$

The adiabatic(geometric optics) invariant“ray number" $a ^ { 2 } k ^ { 0 }$ or"photon number" $( 8 \pi \hbar ) ^ { - 1 } a ^ { 2 } k ^ { 0 }$ in a unit volume is proportional to the energy, $( 8 \pi ) ^ { - 1 } a ^ { 2 } ( k ^ { 0 } ) ^ { 2 }$ ， divided by the frequency, $k ^ { 0 }$ --corresponding exactly to the harmonic oscillator adiabatic invariant $E / \omega$ [Einstein (19i2),Ehrenfest (19l6),Landau and Lifshitz (1960)].

# E. Photon Reinterpretation of Geometric Optics

The laws of geometric optics can be reinterpreted as follows. This reinterpretation becomes a foundation of the standard quantum theory of the electromagnetic field (see,e.g.,Chapters 1 and I3 of Baym (l969)]; and the classical limit of that quantum theory is standard Maxwell electrodynamics.

Photons are particles of zero rest mass that move along nul geodesics of spacetime (the null rays).

The 4-momentum of a photon is related to the tangent vector of the nul ray (wave vector) by $\pmb { p } = \hbar \pmb { k }$ .A renormalization of the afine parameter,

$$
( \mathrm { n e w ~ p a r a m e t e r } ) = ( 1 / \hbar ) \times ( \mathrm { o l d ~ p a r a m e t e r } ) ,
$$

makes $\pmb { \rho }$ the tangent vector to the ray.

Each photon possesses a polarization vector, $\pmb { \mathscr { f } } ,$ which is orthogonal to its 4-momentum ( $\mathbf { \nabla } \cdot \mathbf { \vec { r } } = 0 ,$ ,and which it parallel-transports along its geodesic world line $( \pmb { \nabla _ { p } } \pmb { f } = 0 )$ .

A swarm of photons, all with nearly the same 4-momentum $\pmb { p }$ and polarization vector $\pmb { \mathscr { f } }$ (as compared by parallel transport), make up a classical electromagnetic wave.The scalar amplitude $^ { a }$ of the wave is determined by equating the stress-energy tensor of the wave-

$$
\pmb { \tau } = \frac { 1 } { 8 \pi } a ^ { 2 } \pmb { k } \otimes \pmb { k } = \frac { 1 } { 8 \pi } \bigg ( \frac { a } { \hbar } \bigg ) ^ { 2 } \pmb { p } \otimes \pmb { p }
$$

to the stress-energy tensor of a swarm of photons with number-flux vector S,

$$
{ \pmb { \tau } } = { \pmb { \rho } } \otimes { \pmb { s } }
$$

[see equation (5.18). The result:

$$
{ \pmb S } = \frac { 1 } { 8 \pi } \bigg ( \frac { a } { \hbar } \bigg ) ^ { 2 } { \pmb \rho } = \frac { 1 } { 8 \pi \hbar } a ^ { 2 } { \pmb k }
$$

or, in any local Lorentz frame,

$$
a = ( 8 \pi \hbar ^ { 2 } S ^ { 0 } / p ^ { 0 } ) ^ { 1 / 2 } = ( 8 \pi ) ^ { 1 / 2 } \hbar \left( { \frac { \mathrm { n u m b e r ~ d e n s i t y ~ o f ~ p h o t o n s } } { \mathrm { e n e r g y ~ o f ~ o n e ~ p h o t o n } } } \right) ^ { 1 / 2 } .
$$

(b) Show that the following polarization vectors correspond to the types of polarization listed:

(c) Show that the type of polarization (linear; circular; elliptical with given eccentricity of ellipse) is the same as viewed in any local Lorentz frame at any event along a given ray. [Hint:Use pictures and abstract calculations rather than Lorentz transformations and component calculations.]

# Exercise 22.13. THE AREA OF A BUNDLE OF RAYS

Write equation (22.31) in a coordinate system in which one of the coordinates is chosen to be $\scriptstyle x ^ { 0 } = \theta$ ,the phase (a retarded time coordinate).

(a) Show that $g ^ { 0 0 } = 0$ and that no derivatives $\partial / \partial \pmb \theta$ appear in equation (22.33); so propagation of a can be described within a single $\theta =$ constant hypersurface.

(b) Perform the following construction (see Figure 22.1). Pick a ray $\mathcal { C } _ { 0 }$ along which $\pmb { a }$ is to be propagated.Pick a bundle of rays,with two-dimensional cross section,that (i） all lie in the same constant-phase surface as $\mathcal { C } _ { 0 } ,$ and (ii） surround $\mathcal { C } _ { 0 }$ (The surface is three-di-("conseruation of photon fux").(3) $\boldsymbol { \mathcal { Q } }$ obeys the “propagation equation" (22.36).

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/2fef0e6d2c7950b0bf76f342d3bd9d4e56d6b73bb27477f142c7a10fb25410fb.jpg)  
Figure 22.1. Geometric optics fora bundle of rays with two-dimensional cross section,all lying in a surface of constant phase, $\theta = \mathsf { c o n s t }$ ，Sketch (a) shows the bundle, surrounding a central ray $c _ { \mathbf { 0 } } ^ { \prime } .$ in a spacetime diagram with one spatial dimension suppressed.Sketch (b) shows the bundle as viewed on a slice of simultaneity in a local Lorentz frame at the event $\mathcal { P } _ { \mathbf { 0 } }$ Slicing the bundle turns each ray into a“photon”；so the bundle becomes a two-dimensional surface filled with photons.The area $\boldsymbol { \mathcal { Q } }$ of this photon-filled surface obeys the following laws (see exercises 22.13 and 22.14):(l) $\boldsymbol { \mathcal { Q } }$ is independent of the choice of Lorentz frame;it depends only on location $\vartheta _ { \mathbf { 0 } }$ along the ray $\scriptstyle { \mathcal { C } } _ { 0 }$ .(2）The amplitude $^ { a }$ of the waves satisfies

mensional,soany bundle filing it hasa two-dimensional cross section.)At any event $\mathcal { P } _ { 0 } .$ in any local Lorentz frame there,on a “slice of simultaneity” $x ^ { 0 } =$ constant, measure the cross-sectional area $\pmb { \mathcal { a } }$ of the bundle.(Note: the area being measured is perpendicular to $\pmb { k }$ in the three-dimensional Euclidean sense; it can be thought of as the region occupied momentarily by a group of photons propagating along,side by side,in the $\pmb { k }$ direction.） Show that the area $\pmb { \mathcal { a } }$ is the same, at a given event $\boldsymbol { \mathfrak { P } } _ { 0 } ,$ regardless of what Lorentz frame is used to measure it; but the area changes from point to point along the ray $\mathcal { C } _ { 0 }$ as a result of the rays' divergence away from each other or convergence toward each other:

$$
\begin{array} { r } { \hat { v } _ { \pmb { k } } \pmb { \mathcal { a } } = ( \pmb { \nabla } \pmb { \cdot } \pmb { k } ) \pmb { \mathcal { a } } . } \end{array}
$$

Then show that $\scriptstyle { \mathcal { a } } a ^ { 2 }$ is a constant everywhere along the ray $\mathcal { E } _ { 0 }$ ("conservation of photon flux"). [Hints: (i) Any vector $\pmb { \xi }$ connecting adjacent rays in the bundle is perpendicular to $\pmb { k }$ ，because $\pmb { \xi }$ lies in a surface of constant $\pmb \theta$ and $\pmb { k } \cdot \pmb { \xi } \overset { \cdot } { = } \langle \widetilde { \pmb { k } } , \pmb { \xi } \rangle = \langle \pmb { d } \theta , \pmb { \xi } \rangle \overset { \cdot } { = } \overset$ (change in $\pmb \theta$ along $\xi ) = 0$ .(ii） Consider,for simplicity,a bundle with rectangular cross section as seen in a specific local Lorentz frame at a specific event $\mathcal { P } _ { 0 }$ [edge vectors $\pmb { v }$ and $\boldsymbol { \mathsf { w } }$ with ${ \pmb v } \cdot { \pmb w } = 0$ (edges perpendicular） and $\pmb { v } \cdot \pmb { e } _ { 0 } = \pmb { w } \cdot \pmb { e } _ { 0 } = 0$ (edges in surface of constant time） and $\pmb { v } \cdot \pmb { k } = \pmb { w } \cdot \pmb { k } = 0$ (since edge vectors connect adjacent rays of the bundle)]. Show pictorially that in any other Lorentz frame at $\mathcal { P } _ { 0 }$ ,the edge vectors are ${ \pmb v } ^ { \prime } = { \pmb v } + \alpha { \pmb k }$ and $w ^ { \prime } = w + \beta k$ for some $\pmb { \alpha }$ and $\beta$ .Conclude that in all Lorentz frames at $\mathcal { P } _ { 0 }$ the cross section has identical shape and identical area,and is spatially perpendicular to the direction of propagation $( \pmb { k } \cdot \pmb { v } = \pmb { k } \cdot \pmb { w } = 0 )$ .(iii) By a calculation in a local Lorentz frame show that $\partial _ { \pmb { k } } \pmb { \mathcal { a } } = ( \pmb { \nabla } \pmb { \cdot } \pmb { k } ) \pmb { \mathcal { a } }$ (iv) Conclude from $\hat { \partial } _ { \pmb { k } } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a$ that $\hat { v } _ { \star } ( \mathcal { a } a ^ { 2 } ) = 0 . ]$

# Exercise 22.14. FOCUSING THEOREM

The cross-sectional area $\boldsymbol { \mathscr { a } }$ of a bundle of rays all lying in the same surface of constant phase changes along the central ray of the bundle at the rate (22.36) (see Figure 22.1).

(a) Derive the following equation (“focusing equation") for the second derivative of $\pmb { \mathcal { Q } } ^ { 1 / 2 }$

$$
\frac { d ^ { 2 } \mathcal { Q } ^ { 1 / 2 } } { d \lambda ^ { 2 } } = - \bigg ( | \sigma | ^ { 2 } + \frac { 1 } { 2 } R _ { \alpha \beta } k ^ { \alpha } k ^ { \beta } \bigg ) \mathcal { Q } ^ { 1 / 2 } ,
$$

where $\lambda$ is affine parameter along the central ray $( \pmb { \mathscr { k } } = d / d \lambda )$ ,and the“magnitude of the shear of the rays”, $| \pmb { \sigma } |$ ,is defined by the equation

$$
\vert \sigma \vert ^ { 2 } \equiv { \frac { 1 } { 2 } } k _ { \alpha ; \beta } k ^ { \alpha ; \beta } - { \frac { 1 } { 4 } } ( k ^ { \mu } { } _ { ; \mu } ) ^ { 2 } .
$$

[Hint: This is a vigorous exercise in index manipulations. The key equations needed in the manipulations are $\mathcal { a } _ { , \alpha } k ^ { \alpha } = ( k ^ { \alpha } { } _ { ; \alpha } ) \mathcal { a }$ [equation (22.36)}; $k ^ { \alpha } { } _ { ; \beta } k ^ { \beta } = 0$ [geodesic equation (22.32) for rays]; $k _ { \alpha ; \beta } = k _ { \beta ; \alpha }$ [which follows from $k _ { \alpha } \equiv \theta _ { , \alpha } ] ;$ and the rule (16.6c) for interchanging covariant derivatives of a vector.]

(b) Show that, in a local Lorentz frame where $\pmb { k } = \omega ( \pmb { e } _ { t } + \pmb { e } _ { z } )$ at the origin,

$$
| \sigma | ^ { 2 } = \frac { 1 } { 4 } ( k _ { x , x } - k _ { y , y } ) ^ { 2 } + ( k _ { x , y } ) ^ { 2 } .
$$

Thus, $| \pmb { \sigma } | ^ { 2 }$ is nonnegative, which justifies the use of the absolute value sign.

(c) Discussion: The quantity $| \pmb { \sigma } |$ is called the shear of the bundle of rays because it measures the extent to which neighboring rays are sliding past each other [see,e.g., Sachs(1964)]. Hence,the focusing equation (22.37） says that shear focuses a bundle of rays (makes $d ^ { 2 } { \cal { Q } } ^ { 1 / 2 } / d \lambda ^ { 2 } < 0 )$ ; and spacetime curvature also focuses it if $R _ { \alpha \beta } k ^ { \alpha } k ^ { \beta } > 0$ ,but defocuses it if $R _ { \alpha \beta } k ^ { \alpha } k ^ { \beta } < 0$ .(When a bundle of toothpicks,originally circular in crosssection,is squeezed into an elliptic cross section, it is sheared.)

(d) Assume that the energy density $T _ { \hat { 0 } \hat { 0 } } .$ , as measured by any observer anywhere in spacetime,is nonnegative. By combining the focusing equation (22.37） with the Einstein field equation, conclude that

$$
\frac { d ^ { 2 } { d ^ { 1 / 2 } } } { d \lambda ^ { 2 } } \leq 0 \left( \begin{array} { l } { \mathrm { f o r ~ a n y ~ b u n d l e ~ o f ~ r a y s , ~ a l l ~ i n ~ t h e ~ s a m e } } \\ { \mathrm { s u r f a c e ~ o f ~ c o n s t a n t ~ p h a s e , ~ a n y w h e r e ~ i n } } \\ { \mathrm { s p a c e t i m e } } \end{array} \right)
$$

(focusing theorem). This theorem plays a crucial role in black-hole physics (S34.5)and in the theory of singularities (S34.6).

# \$22.6. KINETIC THEORY IN CURVED SPACETIME\*

The stars in a galaxy wander through spacetime, each on its own geodesic world line, each helping to produce the spacetime curvature felt by allthe others. Photons, left over from the hot phases of the big bang,bathe the Earth, bringing with themselves data on the homogeneity and isotropy of the universe. Theoretical analyses of these and many other problems are unmanageable, if they attempt to keep track of the motion of every single star or photon. But a statistical description gives accurate results and is powerful. Moreover,for most problems in astrophysics and cosmology, the simplest of statistical descriptions-one ignoring collisions-is adequate. Usually collisions are unimportant for the large-scale behavior of a system (e.g:; a galaxy), or they are so important that a fuid description is possible (e.g., in a stellar interior).

Consider,then, a swarm of particles (stars,or photons,or black holes,or ...) that move through spacetime on geodesic world lines, without colliding. Assume, for simplicity,that the particles all have the same rest mass. Then all information of a statistical nature about the particles can be incorporated into a single function, the “distribution function” or “number density in phase space", $\mathfrak { X }$

Define $\mathfrak { X }$ in terms of measurements made by a specific local Lorentz observer at a specific event $\mathcal { P } _ { 0 }$ in curved spacetime. Give the observer a box with 3-volume $\mathcal { V } _ { \pmb { \varepsilon } }$ (and with imaginary walls). Ask the observer to count how many particles, $N ,$ are inside the box and have local-Lorentz momentum components $p ^ { j }$ in the range

Volume in phase space for a group of identical particles

$$
P ^ { j } - \frac { 1 } { 2 } { \cal { \cal { A } } } p ^ { j } < p ^ { j } < P ^ { j } + \frac { 1 } { 2 } { \cal { \cal { A } } } p ^ { j } .
$$

(He can ignore the particle energies $p ^ { 0 }$ ； since all particles have the Same rest mass $m$ energy

$$
p ^ { 0 } = ( m ^ { 2 } + p ^ { 2 } ) ^ { 1 / 2 }
$$

is fixed uniquely by momentum.) The volume in momentum space occupied by the $N$ particles is $\mathcal { V } _ { p } = \varDelta p ^ { \boldsymbol { \tau } } \varDelta p ^ { \boldsymbol { \nu } } \varDelta p ^ { \boldsymbol { z } }$ ； and the volume in phase space is

$$
\begin{array} { r } { \mathcal { V } \equiv \mathcal { V } _ { \texttt { r } } \mathcal { T } _ { p } . } \end{array}
$$

Lorentz invariance of volume in phase space

Other observers at $\mathcal { P } _ { 0 }$ ,moving relative to the first, will disagree on how much spatial volume $\mathcal { V } _ { \pmb { z } }$ and how much momentum volume $\mathcal { T } _ { p }$ these same $N$ particles occupy:

$\mathcal { V } _ { \pmb { \varepsilon } }$ and $\mathcal { V } _ { p }$ depend on the choice of Lorentz frame.

However, all observers will agree on the value of the product $\mathcal { V } \equiv \mathcal { T } _ { \textit { \texttt { z } } } \mathcal { T } _ { \textit { p } }$ ("volume in phase space"):

The phase-space volume $\cdot \boldsymbol { \mathcal { V } }$ occupied by a given set of $N$ identical particles at a given event in spacetime is independent of the local Lorentz frame in which it is measured.

(See Box 22.5 for proof.) Moreover, as the same $N$ particles move through spacetime along their geodesic world lines (and through momentum space),the volume $\mathcal { V }$ they span in phase space remains constant:

Liouville's theorem (conservation of volume in phase space)

The $\mathcal { V }$ occupied by a given swarm of $N$ particles is independent of location along the world line of the swarm ("Liouville's theorem in curved spacetime").

(See Box 22.6 for proof.)

Number density in phase space (distribution function)

More convenient for applications than the volume $\mathcal { V }$ in phase space occupied by a given set of $N$ particles is the“number density in phase space”("distribution function") in the neighborhood of one of these particles:

$$
{ \mathcal { X } } \equiv N / { \mathcal { V } } .
$$

On what does this number density depend? It depends on the location in spacetime, ${ \mathcal P }$ ,at which the measurements are made.It also depends on the 4-momentum $\pmb { \rho }$ of the particle in whose neighborhood the measurements are made.But because the particles all have the same rest mass, $\pmb { \rho }$ cannot take on any and every value in the tangent space at $\mathcal { P }$ Rather, $\pmb { \rho }$ is confined to the “forward mass hyperboloid" at $\mathcal { P }$ ：

Thus,

$$
\mathcal { X } = \mathcal { X } \left[ \left( \begin{array} { l } { \mathrm { l o c a t i o n } , \mathcal { P } , } \\ { \mathrm { i n ~ s p a c e t i m e } } \end{array} \right) , \left( \begin{array} { l } { 4 \mathrm { - m o m e n t u m } p , \mathrm { w h i c h ~ m u s t ~ l i e } } \\ { \mathrm { o n ~ t h e ~ f o r w a r d ~ m a s s ~ h y p e r b o l o i d } } \\ { \mathrm { o f ~ t h e ~ t a n g e n t ~ s p a c e ~ a t } \mathcal { P } } \end{array} \right) \right] .
$$

Pick some one particle in the swarm,with geodesic world line $\mathcal { P } ( \lambda ) \left[ \lambda = \right.$ (affine parameter) $=$ (proper time, if particle has finite rest mass)], and with 4-momentum

Box 22.5 VOLUME IN PHASE SPACE

# A. For Swarm of Identical Particles with Nonzero Rest Mass

Pick an event $\mathcal { P } _ { 0 }$ ，through which passes a particle named“John”with a 4-momentum named $" \mathbf { \nabla } _ { \mathbf { \vec { P } } } \mathbf { \vec { \nu } } ^ { \mathbf { \vec { \nu } } }$ . In John's local Lorentz rest frame at $\mathcal { P } _ { 0 }$ ("barred frame", ${ \overline { { \mathcal { S } } } } ^ { \cdot }$ ), select a small 3-volume, $\mathcal { V } _ { z } \equiv \varDelta \bar { x } \varDelta \bar { y }$ $\pmb { \varDelta \overline { { z } } } ,$ ,containing him.Also select a small $^ { \mathfrak { s } \mathfrak { s } }$ -volume in momentum space," $\mathcal { V } _ { \bar { p } } \equiv \varDelta p ^ { \bar { x } } \varDelta p ^ { \bar { y } } \varDelta p ^ { \bar { z } }$ centered on John's momentum, which is $\dot { P } ^ { \tilde { \tau } } = P ^ { \tilde { \tau } } =$ $P ^ { \overline { { z } } } = 0 .$ Focus attention on all particles whose world lines pass through $\mathcal { V } _ { \overline { { \pmb { \varepsilon } } } }$ and which have momenta $p ^ { \dagger }$ in the range $\mathcal { V } _ { \overline { { p } } }$ surrounding $P ^ { \dagger } = 0$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/1a6267e2448e4a177e830a178da5511d058f2d248d7e30dd31d665dc36690358.jpg)

Examine this bundle in another local Lorentz frame("unbarred frame",S) at ${ \mathcal { P } } _ { 0 } ,$ which moves with speed $\beta$ relative to the rest frame. Orient axes so the relative motion of the frames is in the $_ x$ and $\bar { x }$ directions. Then the space volume $\mathcal { T } _ { \pi }$ occupied in the new frame has $\varDelta y = \varDelta \bar { y }$ ， $\varDelta z = \varDelta \overline { { z } }$ (no effect of motion on transverse directions),and $\varDelta x = ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \varDelta \overline { { x } }$ (Lorentz contraction in longitudinal direction). Hence $\mathcal { V } _ { \varepsilon } = ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \mathcal { V } _ { \frac { - } { \varepsilon } }$ ("transformation law for space volumes")or, equivalently [since $P ^ { 0 } = m / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } ]$

$$
P ^ { 0 } \mathcal { V } _ { \overline { { x } } } = m \mathcal { V } _ { \overline { { x } } } = \binom { \mathrm { c o n s t a n t , ~ i n d e p e n d e n t } } { \mathrm { o f ~ L o r e n t z ~ f r a m e } } .
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/512f5fa5c76c9762f1cb5517057e25852ef1ad98a41fdaf98e8fac3aa51cf36c.jpg)

A momentum-space diagram, analogous to the spacetime diagram, depicts the momentum spread for_particles in the bundle,and shows that $\varDelta p ^ { \pm } =$ $\Delta p ^ { \overline { { \tau } } } / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 }$ .The Lorentz transformation from $\overline { { \boldsymbol { s } } }$ to $s$ leaves transverse components of momenta unaffected; so $\varDelta p ^ { y } = \varDelta p ^ { \widetilde { y } }$ ， $A p ^ { z } = 4 p ^ { \bar { z } }$ Hence $\mathcal { V } _ { p } = \mathcal { V } _ { \bar { p } } / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 }$ ("transformation law for momentum volumes"); or, equivalently

$$
{ \frac { { \mathcal { V } } _ { p } } { P ^ { 0 } } } = { \frac { { \mathcal { V } } _ { \bar { p } } } { m } } = { \binom { { \mathrm { c o n s t a n t , ~ i n d e p e n d e n t } } } { { \mathrm { o f ~ L o r e n t z ~ f r a m e } } } } .
$$

Although the spatial 3-volumes $\mathcal { V } _ { \pmb { \varepsilon } }$ and $\mathcal { V } _ { \overline { { \pmb { \mathscr { x } } } } }$ differ from one frame to another,and the momentum 3-volumes $\mathcal { V } _ { p }$ and $\mathcal { V } _ { \overline { { p } } }$ differ, the volume in six-dimensional phase space is Lorentz-invariant:

$$
\mathcal { V } \equiv \mathcal { V } _ { \overline { { x } } } \mathcal { V } _ { \overline { { p } } } = \mathcal { V } _ { x } \mathcal { V } _ { p } .
$$

It is a frame-independent, geometric object!

# B. For Swarm of ldentical Particles with Zero Rest Mass

Examine a sequence of systems,each with particles of smaller rest mass and of higher velocity relative to a laboratory.For every bundle of particles in each system, $P ^ { \mathrm { { i } } } \mathcal { V } _ { \pi } , \mathcal { V } _ { p } / P ^ { \mathrm { { i } } }$ ,and $\mathcal { V } _ { \pmb { \mathscr { x } } } \mathcal { V } _ { \pmb { \mathscr { p } } }$ are Lorentzinvariant.Hence,in the limit as $m \longrightarrow 0$ ，as $\beta \longrightarrow 1$ ,and as $P ^ { 0 } = m / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \longrightarrow$ finite value (particles of zero rest mass moving with speed of light), $P ^ { 0 } \mathcal { V } _ { \pmb { x } }$ and $\mathcal { V } _ { p } / P ^ { 0 }$ and $\mathcal { V } _ { \pmb { \mathscr { s } } } \mathcal { V } _ { \pmb { \mathscr { p } } }$ are still Lorentz-invariant, geometric quantities.

Examine a very small bundle of identical particles that move through curved spacetime on neighboring geodesics. Measure the bundle's volume in phase space, $\mathcal { V }$ $( \mathcal { V } = \mathcal { V } _ { z } \mathcal { V } _ { , p }$ in any local Lorentz frame), as a function of affine parameter $\lambda$ along the central geodesic of the bundle. The following calculation shows that

$$
d \mathcal { V } / d \lambda = 0 \qquad \binom { \mathrm { { ' } L i o u v i l l e ~ t h e o r e m ~ i n } } { \mathrm { { c u r v e d ~ s p a c e t i m e } ^ { , 9 } } } .
$$

Proof for particles of finite rest mass: Examine particle motion during time interval $\delta \tau$ ,using local Lorentz rest frame of central particle. All velocities are small in this frame, so

$$
p ^ { \tilde { j } } = m d x ^ { \tilde { j } } / d \overline { { t } } .
$$

Hence (see pictures) the spreads in momentum and position conserve $\varDelta \overline { { x } } \varDelta \bar { p ^ { \bar { x } } }$ ,4y $\varDelta p ^ { \tilde { \nu } }$ ,and $\Delta \overline { { z } } \Delta p ^ { \overline { { z } } }$ ； i.e.,

$$
. \frac { d \mathcal { V } } { d \tau } = \frac { \delta ( \varDelta \overline { { x } } \varDelta \overline { { y } } \varDelta \overline { { z } } \varDelta p ^ { \overline { { x } } } \varDelta p ^ { \overline { { y } } } \varDelta p ^ { \overline { { z } } } ) } { \delta \overline { { t } } } = 0 .
$$

But $\tau = a \lambda + b$ for some arbitrary constants $^ { a }$ and$^ { b }$ ； so $, d \mathcal { V } / d \lambda = 0$

Prooffor particles of zero rest mass. Examine particle motion in local Lorentz frame where central particle has ${ \pmb P } = P ^ { 0 } ( { \pmb e } _ { 0 } + { \pmb e } _ { \tau } )$ . In this frame, all particleshave $p ^ { y } \ll p ^ { 0 }$ ， $p ^ { z } \ll p ^ { 0 }$ ， $p ^ { \pm } = p ^ { 0 } + $ ${ \cal O } ( [ p ^ { y } ] ^ { 2 } / P ^ { 0 } ) \approx P ^ { 0 }$ Since $p ^ { \alpha } = d x ^ { \alpha } / d \lambda$ for appropriate normalization of afine parameters (see Box 22.4), one can write $d x ^ { j } / d t = \dot { p } ^ { j } / p ^ { 0 }$ ； i.e.,

$$
\begin{array} { c } { { \frac { d x } { d t } = 1 + O ( [ p ^ { \nu } / P ^ { 0 } ] ^ { 2 } + [ p ^ { z } / P ^ { 0 } ] ^ { 2 } ) } } \\ { { \approx 1 , } } \end{array}
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/884e9419cc77941f8155021cab5073bc93bfe44472fc57991034ff91e48e71ee.jpg)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/42fa825272a340bcf23b97f3f5727ca234763e0c2edf5e36bd50b3547fa0caf6.jpg)

Each particle moves with speed $d \widetilde { x } / \widetilde { d t }$ proportional to height in diagram

$$
d \widetilde { x } / { \widetilde { d t } } = p ^ { \overline { { z } } } / m ,
$$

and conserves its momentum, $d p ^ { \overline { { x } } } / \widetilde { d t } = 0$ .Hence the region occupied by particles deforms,but maintains its area. Same is true for $( y - p ^ { \pmb { \nu } } )$ and $( z - p ^ { z } )$

$$
\frac { d y } { d t } = \frac { p ^ { y } } { P ^ { 0 } } , \frac { d z } { d t } = \frac { p ^ { z } } { P ^ { 0 } } .
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/7e4a963adeb73de072722b71556546c84a0a32602dda75ddbd9538c2a36e1deb.jpg)  
Each particle("photon") moves with $d x / d t = 1$ and $d p ^ { z } / d t = 0$ in the local Lorentz frame.Area and shape of occupied region are preserved.

Hence (see pictures) $\boldsymbol { \varDelta } \boldsymbol { x } \boldsymbol { \varDelta } p ^ { \boldsymbol { \varepsilon } }$ 4y $\varDelta p ^ { y }$ and $\varDelta z \varDelta p ^ { z }$ are all conserved; and

$$
\frac { d \mathcal { V } } { d t } = \frac { \delta ( \varDelta x \varDelta y \varDelta z \varDelta p ^ { x } \varDelta p ^ { y } \varDelta p ^ { z } ) } { \delta t } = 0 .
$$

But $t$ and the affine parameter $\lambda$ of central particle are related by $t = \bar { P } ^ { 0 } \lambda$ [cf. equation (16.4); thus

$$
d \mathcal { V } / d \lambda = 0 .
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/43649d62e44cc30d6f3c2234bbae11b6a0b346e81388012e85300e6e5cf57e3b.jpg)

Particle("photon") speedsare proportional to height in diagram

$$
\begin{array} { r } { d y / d t = p ^ { y } / P ^ { 0 } , } \end{array}
$$

and $d p ^ { y } / d t = 0$ Hence,occupied region deforms but maintains its area. Same is true of z-p.

${ \pmb \rho } ( \lambda )$ .Examine the density in phase space in this particle's neighborhood at each point along its world line:

$$
\begin{array} { r } { \mathcal { X } = \mathcal { X } [ \mathcal { P } ( \lambda ) , \pmb { p } ( \lambda ) ] . } \end{array}
$$

Calculate ${ \mathcal { R } } ( \lambda )$ as follows: (l) Pick an initial event ${ \mathcal { P } } ( 0 )$ on the world line,and a phase-space volume $\mathcal { V }$ containing the particle. (2) Cover with red paint all the particles contained in $\mathcal { V }$ at ${ \mathcal { P } } ( 0 )$ .(3) Watch the red particles move through spacetime alongside the initial particle. (4) As they move,the phase-space region they occupy changes shape extensively; but its volume $\mathcal { V }$ remains fixed (Liouville's theorem). Moreover, no particles can enter or leave that phase-space region (once in, always in; once out, always out; boundaries of phase-space region are attached to and move with the particles). (5) Hence,at any $\lambda$ along the initial particle's world line,the particle is in a phase-space region of unchanged volume $\mathcal { V }$ ,unchanged number of particles $N ,$ and unchanged ratio $\mathcal { X } = N / \mathcal { V }$ ：

$$
{ \frac { d { \mathcal { D } } \zeta [ { \mathcal { P } } ( \lambda ) , \pmb { \rho } ( \lambda ) ] } { d \lambda } } = 0 .
$$

Collisionless Boltzmann equation (kinetic equation)

This equation for the conservation of $\mathfrak { N }$ along a particle's trajectory in phase space is called the“collisionless Boltzmann equation,”or the “kinetic equation.”

Photons provide an important application of the Boltzmann equation. But when discussing photons one usually does not think in terms of the number density in phase space. Rather,one speaks of the“specific intensity" $I _ { \nu }$ of radiation at a given frequency $\nu$ ,flowing in a given direction. $\pmb { n }$ ,as measured in a specified local Lorentz frame:

$$
I _ { \nu } \equiv \frac { d ( \mathrm { e n e r g y } ) } { d ( \mathrm { t i m e } ) d ( \mathrm { a r e a } ) d ( \mathrm { f r e q u e n c y } ) d ( \mathrm { s o l i d a n g l e } ) } .
$$

Distribution function for photons expressed in terms of specific intensity, $\prime _ { \nu }$

(See Figure 22.2). A simple calculation in the local Lorentz frame reveals that

$$
{ \mathcal D } = h ^ { - 4 } ( I _ { \nu } / \nu ^ { 3 } ) ,
$$

Invariance and conservation of $I _ { \nu } / \nu ^ { 3 }$

where $\pmb { h }$ is Planck's constant (see Figure 22.2).Thus,if two different observers at the same or different events in spacetime look at the same photon (and neighboring photons) as it passes them,they will see different frequencies $\nu$ ("doppler shift," “cosmological red shift,”“gravitational redshift"),and different specific intensities $I _ { \nu }$ ; but they will obtain identical values for the ratio $I _ { \nu } / \nu ^ { 3 }$ .Thus $I _ { \nu } / \nu ^ { 3 }$ like $\mathfrak { N }$ ,is invariant from observer to observer and from event to event along a given photon's world line.

# EXERCISES

# Exercise 22.15. INVERSE SQUARE LAW FOR FLUX

The specific flux of radiation entering a telescope from a given source is defined by

$$
F _ { \nu } = \int I _ { \nu } d \Omega ,
$$

where integration is over the total solid angle (assumed $\lessleqslant 4 \pi$ ）subtended by the source on the observer's sky. Use the Boltzmann equation (conservation of $I _ { \nu } / \nu ^ { 3 } )$ to show that $F _ { \nu } \propto$ (distance from source)-² for observers who are all at rest relative to each other in flat spacetime.

# Exercise 22.16. BRIGHTNESS OF THE SUN

Does the surface of the sun look any brighter to an astronaut standing on Mercury than to a student standing on Earth?

# Exercise 22.17. BLACK BODY RADIATION

An“optically thick” source of black-body radiation (e.g.,the surface of a star,or the hot matter filling the universe shortly after the big bang) emits photons isotropically with a specific intensity,as seen by an observer at rest near the source,given (Planck radiation law） by

$$
I _ { \nu } = { \frac { 2 h \nu ^ { 3 } } { e ^ { h \nu / k T } - 1 } } .
$$

Here $T$ is the temperature of the source. Show that any observer, in any local Lorentz frame, anywhere in the universe,who examines this radiation as it flows past him,will also see a black-body spectrum. Show,further, that if he calculates a temperature by measuring the specific intensity $I _ { \nu }$ at any one frequency,and if he calculates a temperature from the shape of the spectrum, those temperatures will agree.(Radiation remains black body rather than being“diluted”into“grey-body.") Finally,show that the temperature he measures is redshifted by precisely the same factor as the frequency of any given photon is redshifted,

$$
\frac { T _ { \mathrm { { o b s e r v e d } } } } { T _ { \mathrm { { e m i t t e d } } } } = \left( \frac { \nu _ { \mathrm { { o b s e r v e d } } } } { \nu _ { \mathrm { { e m i t t e d } } } } \right) \mathrm { { f o r } \ a \ g i v e n \ p h o t o n . }
$$

[Note that the redshifts can be “Doppler”in origin,“cosmological”inorigin,“gravitational" in origin,or some inseparable mixture.Allthat matters is the fact that the parallel-transport law for a photon's 4-momentum, $\pmb { \nabla _ { p } p } = 0$ ，guarantees that the redshift $\nu _ { \mathrm { o b s e r v e d } } / \nu _ { \mathrm { e m i t t e d } }$ is independent of frequency emitted.]

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0009_pages_0561-0630/auto/images/ce0c45bd2f9f5b3a484167ee3dbcd930d30091b212bcf03496a671d0e56e5b26.jpg)  
3-momentum volume,with direction of momentum vectors reversed for ease of visualization (telescope as an emitter,not a receiver!)

Figure 22.2.   
Number density in phase space for photons,interpreted in terms of the specific intensity $I _ { \nu }$ An astronomer has a telescope with filter that admits only photons ariving from within a smallsolid angle $\pmb { \varDelta \pmb { \varOmega } }$ about the $z$ -direction,and having energies between $p ^ { \mathbf { 0 } }$ and $p ^ { 0 } + 4 p ^ { 0 }$ .The collecting area, $\pmb { \mathcal { q } }$ ,of his telescope lies in the $\pmb { x }$ ， $_ { y }$ -plane (perpendicular to the incoming photon beam).Let $\pmb { \delta N }$ be the number of photons that cross the area $\boldsymbol { \mathcal { Q } }$ in a time interval δt.[All energies,areas,times,and lengths are measured in the orthonormal frame ("proper reference frame; $\ S 1 3 . 6 )$ ，which the astronomer Fermi-Walker transports with himself along his (possibly accelerated） world line-or,equivalently,in a local Lorentz frame momentarily at rest with respect to the astronomer.] The $\delta N$ photons, just before the time interval $\delta t$ begins,lie in the cylinder of area $\boldsymbol { \mathcal { q } }$ and height $\delta z = \delta t$ shown above.Their spatial 3-volume is thus $\begin{array} { r } { \mathcal { V } _ { \pmb { z } } = \mathcal { Q } \delta t . } \end{array}$ Their momentum 3-volume is $\mathcal { V } _ { p } = ( p ^ { 0 } ) ^ { 2 } \varDelta p ^ { 0 } \varDelta \varOmega$ (see drawing). Hence,their number density in phase space is

$$
\begin{array} { r } { \mathcal { X } = \frac { \delta N } { \mathcal { T } _ { \mathfrak { r } } \mathcal { T } _ { \mathfrak { p } } } = \frac { \delta N } { \mathcal { T } \delta t ( \mathfrak { p } ^ { 0 } ) ^ { 2 } ( \varDelta \mathfrak { p } ^ { 0 } ) \varDelta \varOmega } = \frac { \delta N } { \mathit { h } ^ { 3 } \mathcal { Q } \delta t \nu ^ { 2 } \varDelta \nu \varDelta \varOmega } } \end{array}
$$

where ${ \pmb \nu }$ is the photon frequency measured by the telescope $( p ^ { 0 } = h \nu _ { \mathrm { \scriptscriptstyle { \perp } } }$ .

The specific intensity of the photons, $I _ { \nu }$ (a standard concept in astronomy),is the energy per unit area per unit time per unit frequency per unit solid angle crossng a surface perpendicular to the beam: i.e.,

$$
I _ { \nu } = \frac { h \nu ~ \delta N } { \textit { a } \delta \iota ~ \varDelta \nu ~ \varDelta \Omega } .
$$

Direct comparison reveals $\mathcal { X } = h ^ { - 4 } ( I _ { \nu } / \nu ^ { 3 } )$

Thus,conservation of $\boldsymbol { \mathcal { R } }$ alonga photon's world line implies conservation of $I _ { \nu } / \nu ^ { 3 }$ .This conservation lawfinds important applications in cosmology (e.g.,Box 29.2andEx.29.5)and in thegravitational lens effect (Refsdal 1964);see also exercises 22.15-22.17.

# Exercise 22.18. STRESS-ENERGY TENSOR

(a) Show that the stress-energy tensor for a swarm of identical particles at an event $\boldsymbol { \mathscr { s } } _ { 0 }$ can be written as an integral over the mass hyperboloid of the momentum space at $\mathcal { P } _ { \mathbf { 0 } }$ ：

$$
{ \pmb \tau } = \int ( \Im \pmb { \tau } { \pmb \rho } \otimes { \pmb p } ) ( d ^ { * } \pmb { \gamma } _ { \pmb { p } } / p ^ { 0 } ) ,
$$

(Notice from Box 22.5 that $d \mathcal { V } _ { p } / p ^ { 0 }$ is a Lorentz-invariant volume element for any segment of the mass hyperboloid.)

(b) Verify that the Boltzmann equation, $d \mathcal { D } / d \lambda = 0$ ,implies $\pmb { \nabla } \cdot \pmb { r } = 0$ for any swarm of identical particles.[Hint: Calculate $\mathbf { \nabla } \cdot \mathbf { \vec { r } }$ in a local Lorentz frame,using the above expression for $\pmb { \tau } ,$ and using the geodesic equation in the form $D p ^ { \mu } / d \lambda = 0 . ]$

ExerciSe 22.19. KINETIC THEORY FOR NONIDENTICAL PARTICLES

For a swarm of particles with a wide distribution of rest masses, define

$$
\mathcal { R } = \frac { \dot { \mathrm { ~ \it ~ \_ ~ } } \Delta N } { \dot { \mathcal { r } } _ { \ast } \mathcal { T } _ { \ast } \Delta m } ,
$$

where $\mathcal { V } _ { \pmb { z } }$ and $\mathcal { T } _ { p }$ are spatial and momentum 3-volumes, and $\pmb { \mathscr { A } N }$ is the number of particles in the region $\mathcal { T } _ { \texttt { z } } \mathcal { V } _ { p }$ with rest masses between $m - 4 m / 2$ and $m + \Delta m / 2$ . Show the following.

（a） $\because \gamma _ { p } \lrcorner \lrcorner m$ is independent of Lorentz frame and independent of location on the world tube of a bundle of particles.

(b) $\mathfrak { X }$ can be regarded as a function of location $\mathcal { P }$ in spacetime and 4-momentum $\pmb { \rho }$ inside the future light cone of the tangent space at $\mathcal { P }$ ：

$$
{ \mathcal { X } } = { \mathcal { X } } ( { \mathcal { P } } , { \pmb { p } } ) .
$$

(c） $\mathfrak { X }$ satisfies the collsionless Boltzmann equation (kinetic equation)

$$
{ \frac { d { \mathcal { H } } [ { \mathcal { P } } ( \lambda ) , p ( \lambda ) ] } { d \lambda } } = 0 \qquad { \mathrm { a l o n g ~ g e o d e s i c ~ t r a j e c t o r y ~ o f ~ a n y ~ p a r t i c l e . } }
$$

(d) $\mathfrak { X }$ can be rewritten in a local Lorentz frame as

$$
\mathcal { X } = \frac { A N } { [ ( p ^ { 0 } / m ) ~ 4 x ~ 4 y ~ 4 z ] [ 4 p ^ { 0 } ~ 4 p ^ { x } ~ 4 p ^ { y } ~ \varDelta p _ { . } ^ { z } ] } .
$$

(e) The stress-energy tensor at an event $\mathcal { P }$ can be written as an integral over the interior of the future light cone of momentum space

$$
T ^ { \mu \nu } = \int ( \mathcal { R } p ^ { \mu } p ^ { \nu } ) m ^ { - 1 } d p ^ { 0 } d p ^ { 1 } d p ^ { 2 } d p ^ { 3 }
$$

in a local Lorentz frame (Track-1 notation for integral; see Box 5.3);

$$
\begin{array} { l } { { \pmb { \tau } = \displaystyle \int ( \mathscr { X } { \pmb p } \otimes { \pmb p } ) m ^ { - 1 * } 1 \qquad \mathrm { i n ~ f r a m e - i n d e p e n d e n t ~ n o t a } } } \\ { { \qquad = \displaystyle \int ( \mathscr { X } { \pmb p } \otimes { \pmb p } ) m ^ { - 1 } d p ^ { 0 } \wedge d p ^ { 1 } \wedge d p ^ { 2 } \wedge d p ^ { 3 } } } \end{array}
$$

in a local Lorentz frame (Track-2 notation; see Box 5.4).

PART V

# RELATIVISTIC STARS

Wherein the reader,armed with the magic potions and powers of Geometrodynamics,conquers the stars.
