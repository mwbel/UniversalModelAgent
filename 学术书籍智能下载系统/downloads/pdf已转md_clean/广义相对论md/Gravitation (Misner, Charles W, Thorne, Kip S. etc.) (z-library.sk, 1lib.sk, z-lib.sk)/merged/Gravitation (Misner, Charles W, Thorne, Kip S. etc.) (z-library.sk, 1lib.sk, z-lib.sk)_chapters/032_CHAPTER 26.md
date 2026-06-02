CHAPTER 26

STELLAR PULSATIONS

# \$26.1． MOTIVATION

This chapter is entirely Track 2,but it neither depends on nor prepares for any other chapter.

The raison d'etre of this chapter

In relativistic astrophysics,as elsewhere in physics, most problems of deep physical interest are too diffcult and too complex to be solved exactly. They can be solved only by use of approximation techniques. And of all approximation techniques, the one that has the widest range of application is perturbation theory.

Perturbation calculations are typically long, tedious, and filled with complicated mathematical expressons. Therefore, they are not appropriate for a textbook such as this. Nevertheless, because it is so important that aspiring astrophysicists know how to set up and carry out perturbation calculations in general relativity, the authors have chosen to present one example in detail.

The example chosen is an analysis of adiabatic,radial pulsations of a nonrotating, relativistic star. Two features of this example are noteworthy: (l) it is sufficiently complex to be instructive, but sufficiently simple to be presentable; (2) in the results of the calculation one can discern and quantify the relativistic instability that is so important for modern astrophysics (see Chapter 24).

The calculation presented here is paterned after that of Chandrasekhar (1964a,b), which first revealed the existence of the relativistic instability. For an alternative calculation, based on the concept of “extremal energy,” see Appendix B of Harrison, Thorne, Wakano,and Wheeler (l965); and for a calculation based on extremal entropy,see Cocke (1965).

# \$26.2. SETTING UP THE PROBLEM

The system to be analyzed is a sphere of perfect fluid, pulsating radially with very small amplitude. To analyze the pulsations one needs (a) the exact equations governing the equilibrium configuration about which the sphere pulsates; (b) a coordinate system for the vibrating sphere that reduces,for zero pulsation amplitude, to the standard Schwarzschild coordinates of the equilibrium sphere; (c) a set of small functions describing the pulsation (radial displacement and velocity, pressure and density perturbations, first-order changes in metric coefficients), in which to linearize; and (d) a set of equations governing the evolution of these “perturbation functions.”

Setting up the analysis of stellar pulsations

# a.Equilibrium Configuration

The equations of structure for the equilibrium sphere are those summarized in $\ S 2 3 . 7$ It will be useful to rewrite them here, with a few changes of notation (use of subscript $" o ^ { \bullet }$ to denote “unperturbed configuration"; use of $\varLambda = - \frac { 1 } { 2 } \ln \left( 1 - 2 m / r \right)$ in place of $m$ in all equations; use of a prime to denote derivatives with respect to $r$ ：

$$
d s ^ { 2 } = - e ^ { 2 \phi _ { o } } d t ^ { 2 } + e ^ { 2 \Lambda _ { o } } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

# Equilibrium configuration of star

$$
\ A _ { o } ^ { \prime } = { \frac { 1 } { 2 r } } ( 1 - e ^ { 2 \Lambda _ { o } } ) + 4 \pi r \rho _ { o } e ^ { 2 \Lambda _ { o } } ,
$$

$$
p _ { o } ^ { \prime } = - ( \rho _ { o } + p _ { o } ) \phi _ { o } ^ { \prime } ,
$$

$$
\phi _ { o } ^ { ~ \prime } = - \frac { 1 } { 2 r } ( 1 - e ^ { 2 \varLambda _ { o } } ) + 4 \pi r p _ { o } e ^ { 2 \varLambda _ { o } } .
$$

# b. Coordinates for Perturbed Configuration

-The gas sphere pulsates in a radial, i.e., spherically symmetric, manner. Consequently, its spacetime geometry must be spherical. In Box 23.3 it is shown that for any spherical spacetime, whether dynamic or static, one can introduce Schwarzschild coordinates with a line element

$$
\begin{array} { c } { { d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 \Lambda } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) , } } \\ { { { } } } \\ { { \phi = \phi ( t , r ) , \qquad \Lambda = A ( t , r ) . } } \end{array}
$$

Coordinates for perturbed configuration

One uses these coordinates for the pulsating_sphere -because they reduce to the unperturbed-coordinates when the pulsations have zero amplitude.

# c. Perturbation Functions

When the pulsations have very small amplitude, the metric coefficients, $\pmb { \phi }$ and $\pmb { A }$ ， and the thermodynamic variables $\vec { p } , \vec { \pmb { \rho } } ,$ and $\pmb { n }$ as measured in the fluid's rest frame

have very nearly their unperturbed values. Denote by $\delta \phi , \delta A , \delta p , \delta \rho .$ and ${ \pmb \delta } _ { n }$ the perturbations at fixed coordinate locations:

$$
\begin{array} { l } { { \phi ( t , r ) = \phi _ { o } ( r ) + \delta \phi ( t , r ) , \ ~ A ( t , r ) = A _ { o } ( r ) + \delta A ( t , r ) , } } \\ { { \nonumber } } \\ { { p ( t , r ) = p _ { o } ( r ) + \delta p ( t , r ) , \qquad \rho ( t , r ) = \rho _ { o } ( r ) + \delta \rho ( t , r ) , } } \end{array}
$$

$$
\boldsymbol { n } ( t , \boldsymbol { r } ) = \boldsymbol { n } _ { o } ( \boldsymbol { r } ) + \delta \boldsymbol { n } ( t , \boldsymbol { r } ) .
$$

Besides $\delta \phi , \delta A , \delta p , \delta \rho$ and ${ \pmb \delta } { \pmb n }$ ,one more perturbation function is needed to describe the pulsations: the radial displacement ${ \pmb \xi }$ of the fluid from its equilibrium position:

A fluid element located at coordinate radius $r$ in the unperturbed configuration is displaced to coordinate radius $r + \xi ( r , t )$ at coordinate time $t$ in the vibrating configuration.

To make the analysis of the pulsations tractable,all equations will be linearized in the perturbation functions $\xi ,$ 8Φ,8A,δp, $\delta _ { \rho }$ and ${ \pmb \delta } _ { \pmb n }$

# d. Equations of Evolution

How to derive equations governing the perturbation functions

The evolution of the perturbation functions with time will be governed by the Einstein field equations, the local law of conservation of energy-momentum $\pmb { \bigtriangledown } \cdot \pmb { \cal T } =$ O,and the laws of thermodynamics-all appropriately linearized. The analysis from here on is nothing but a reduction of those equations to “manageable form.” Of course, the reduction will proceed most efficiently if one knows in advance what form one seeks.The goalin this calculation and in most similar calculations is simple: (l) obtain a set of dynamic equations for the true dynamic degrees of freedom (only the fluid displacement $\xi$ in this case; the fluid displacement and the amplitudes of the gravitational waves in a nonspherical case, where waves are possble); and (2) obtain a set of initial-value equations expressing the remaining perturbation functions $( \delta \phi , \delta A , \delta p , \delta \rho _ { ; }$ and ${ \pmb \delta } { \pmb n }$ in this case) in terms of the dynamic degrees of freedom $( \xi )$

# $\$ 20.3$ .EULERIAN VERSUS LAGRANGIAN PERTURBATIONS

Eulerian perturbations defined

Lagrangian perturbations defined

Before deriving the dynamic and initial-value equations,it is useful to introduce a new concept: the “Lagrangian perturbation” in a thermodynamic variable. The perturbations $\delta p , \delta \rho$ ,and ${ \delta } n$ of equations (26.3) are Eulerian perturbations in $p , \rho ,$ and $\pmb { n }$ ； i.e.,they are changes measured by an observer who sits forever at a fixed point $( t , r , \theta , \phi )$ in the coordinate grid. By contrast, the Lagrangian perturbationsdenoted $ { \Delta p } ,  { \Delta \rho }$ and $\pmb { A } \pmb { n }$ -are changes measured by an observer who moves with the fluid; i.e., by an observer who would sit at radius $\gamma$ in the unperturbed configuration, but sits at $r + \xi ( t , r )$ in the perturbed configuration:

$$
\begin{array} { r l r } & { } & { \boldsymbol { A } p ( t , r ) = p [ t , r + \xi ( t , r ) ] - p _ { o } ( r ) } \\ & { } & { \approx \boldsymbol { \delta } p + p _ { o } \boldsymbol { \xi } ; } \\ & { } & { \boldsymbol { A } \rho ( t , r ) = \rho [ t , r + \xi ( t , r ) ] - \rho _ { o } ( r ) } \\ & { } & { \approx \boldsymbol { \delta } \rho + \rho _ { o } \boldsymbol { \xi } ; } \\ & { } & { \boldsymbol { A } n ( t , r ) = n [ t , r + \xi ( t , r ) ] - n _ { o } ( r ) } \\ & { } & { \approx \boldsymbol { \delta } n + n _ { o } \boldsymbol { \xi } . } \end{array}
$$

# \$26.4. INITIAL-VALUE EQUATIONS

# a. Baryon Conservation

The law of baryon conservation, $\mathbf { \nabla } \pmb { \nabla } \cdot ( \pmb { n } \pmb { u } ) = 0$ (822.2)，governs the evolution of perturbations $\pmb { 4 n }$ and ${ \pmb \delta } _ { \pmb n }$ in baryon number. By applying the chain rule to the divergence and using the relation $\pmb { u } \cdot \pmb { \nabla } n = \pmb { \nabla } _ { \pmb { u } } n = d n / d \tau _ { \pmb { \mathrm { . } } }$ ,one can rewrite the conservation law as

Derivation of initial value equations:

(1）for baryon perturbations An and δn

$$
\begin{array} { l } { { d n / d \tau = - n ( \pmb { \nabla } \cdot \pmb { u } ) . } } \\ { { \qquad \pmb { \dot { \mathrm { t } } } \qquad \qquad \mathrm { [ d e r i v a t i v e ~ o f ~ } n \mathrm { ~ a l o n g ~ f i u i d ~ w o r l d ~ l i n e ] } } } \end{array}
$$

In terms of $\pmb { \mathscr { s n } }$ ,the perturbation measured by an observer moving with the fluid, this equation can be rewritten as

$$
\begin{array} { r } { \frac { d \varDelta n } { d \tau } = - n ( \pmb { \nabla } \cdot \pmb { u } ) . } \end{array}
$$

To reduce this equation further, one needs an expression for the fluid's 4-velocity. It is readily derived from

$$
\begin{array} { c } { { \displaystyle \frac { u ^ { \tau } } { u ^ { t } } = \left( \frac { d r / d \tau } { d t / d \tau } \right) = \left( \frac { d r } { d t } \right) _ { \mathrm { { a l o n g w o r l d i n e } } } = \frac { \partial \xi } { \partial t } { \equiv } \dot { \xi } , } } \\ { { ( u ^ { t } ) ^ { 2 } e ^ { 2 \phi } - ( u ^ { \tau } ) ^ { 2 } e ^ { 2 \varLambda } = 1 . } } \end{array}
$$

The result to first order in $\xi , \delta A$ and $\delta \varPhi$ is

$$
u ^ { t } = e ^ { - \phi } = e ^ { - \phi _ { o } } ( 1 - \delta \phi ) , ~ u ^ { r } = \dot { \xi } e ^ { - \phi _ { o } } .
$$

Using these components in equation (26.5),and using the relations

$$
\frac { d } { d \tau } = \pmb { u } = u ^ { \alpha } \frac { \partial } { \partial x ^ { \alpha } } , \qquad \pmb { \nabla } \cdot \pmb { u } = \frac { 1 } { \sqrt { - g } } ( \sqrt { - g } u ^ { \alpha } ) _ { , \alpha } ,
$$

together with the vibrating metric (26.2), one reduces equation (26.5) to a relation whose time integral is

$$
\begin{array} { r } { \varDelta n = - n _ { o } [ r ^ { - 2 } e ^ { - \varLambda _ { o } } ( r ^ { 2 } e ^ { \varLambda _ { o } } \xi ) ^ { \prime } + \delta \varLambda ] . } \end{array}
$$

This is the initial value equation for $\pmb { \mathscr { s n } }$ in terms of the dynamic variable $\xi .$ The initial-value equation for $\delta n$ ,which will not be needed later, one obtains by combining with equation (26.4c).

# b. Adiabaticity

(2) for pressure perturbations $\Delta p$ and $\delta p$

For adiabatic vibrations (negligible heat transfer between neighboring fluid elements), the Lagrangian changes in number density and pressure are related by

$$
\begin{array} { l } { \displaystyle \left( \frac { \partial \ln p } { \partial \ln n } \right) _ { s } \equiv \varGamma _ { 1 } = \frac { n } { p } \frac { \varDelta p } { \varDelta n } . } \\ { \displaystyle \left[ \begin{array} { l } { \mathrm { d e f n i t i o n ~ o f ~ a d i a - } } \\ { \mathrm { b a t i c ~ i n d e x } , \varGamma _ { 1 } } \end{array} \right] } \end{array}
$$

Combining this adiabatic relation with equation (26.7) for $\pmb { \mathscr { s n } }$ , and equation (26.4a) for $\delta p$ in terms of $\pmb { \mathscr { s p } }$ ,one obtains the following initial-value equation for $\delta p$ ：

$$
\delta p = - { \cal T } _ { 1 } p _ { o } [ r ^ { - 2 } e ^ { - \Lambda _ { o } } ( r ^ { 2 } e ^ { \Lambda _ { o } } \xi ) ^ { \prime } + \delta A ] - \xi p _ { o } ^ { \prime } .
$$

# c. Energy Conservation

(3) for density perturbations $\pmb { \varDelta \rho }$ and $\delta \rho$

The local law of energy conservation [first law of thermodynamics; ${ \pmb u } \cdot ( { \pmb v } \cdot { \pmb r } ) = 0$ see $\ S 8 2 2 . 2$ and 22.3] says that

$$
\frac { d \rho } { d \tau } = \frac { ( \rho + p ) } { n } \frac { d n } { d \tau } .
$$

Rewritten in terms of Lagrangian perturbations (recall: $d / d \tau$ is a time derivative as measured by an observer moving with the fluid),this reads

$$
\frac { d \varDelta \rho } { d \tau } = \frac { \rho + p } { n } \frac { d \varDelta n } { d \tau } ,
$$

which has as its time integral (first-order analysis!)

$$
\Delta \rho = \frac { \rho _ { o } + p _ { o } } { n _ { o } } \Delta \dot { n } .
$$

(The constant of integration is zero, because, when $\varDelta n = 0 , \ \varDelta \rho$ must also vanish.) Combining this with equation (26.7) for $\pmb { \mathscr { s n } }$ and equation (26.4b) for $\delta _ { \rho }$ in terms of $\pmb { \mathscr { s } } _ { \pmb { \rho } }$ ,one obtains the following initial-value equation for $\delta _ { \rho }$ ：

$$
\delta \rho = - ( \rho _ { o } + p _ { o } ) [ r ^ { - 2 } e ^ { - \varLambda _ { o } } ( r ^ { 2 } e ^ { \varLambda _ { o } } \xi ) ^ { \prime } + \delta \varLambda ] - \xi \rho _ { o } ^ { \prime } .
$$

# d. Einstein Field Equations

Two of the Einstein field equations, when linearized,reduce to initial-value equations for the metric perturbations $\pmb { \delta A }$ and $\delta \varPhi$ . The equations needed, expressed in an orthonormal frame

$$
\omega ^ { \hat { t } } = e ^ { \phi } d t , \quad \quad \omega ^ { \hat { \tau } } = e ^ { A } d r , \quad \quad \omega ^ { \hat { \theta } } = r d \theta , \quad \quad \omega ^ { \hat { \phi } } = r \sin \theta d \phi ,
$$

are $G _ { \hat { r } \hat { t } } = 8 \pi T _ { \hat { r } \hat { t } } ,$ and $G _ { \hat { \pi } } = 8 \pi T _ { \hat { \pi } } .$ The components of the Einstein tensor in this orthonormal frame were evaluated in exercise l4.16:

$$
\begin{array} { r l } & { \mathrel { \phantom { = } } \textstyle \{ \begin{array} { l } { { \mathrm { l i n e a r i z e d } } ] } \\ { { \phantom { = } } } \\ { { G _ { \hat { r } \hat { t } } = 2 ( \dot { \cal X } / r ) e ^ { - ( { \cal A } + \hat { \phi } ) } = 2 r ^ { - 1 } e ^ { - ( { \cal A } _ { \circ } + \phi _ { \circ } ) } \delta \dot { \cal A } ; } } \\ { { G _ { \hat { r } \hat { \tau } } = 2 ( \phi ^ { \prime } / r ) e ^ { - 2 { \cal A } } + r ^ { - 2 } ( e ^ { - 2 { \cal A } } - 1 ) } } \\ { { \phantom { = } } \textstyle = ( G _ { \hat { r } \hat { \tau } } ) _ { \circ } + 2 r ^ { - 1 } e ^ { - 2 { \cal A } _ { \circ } } \delta \phi ^ { \prime } - 2 e ^ { - 2 { \cal A } _ { \circ } } ( 2 r ^ { - 1 } \phi _ { \circ } ^ { \prime } + r ^ { - 2 } ) \delta { \cal A } . } \end{array}  } \\ & { \mathrel { \phantom { = } } \textstyle  \{ \begin{array} { l } { { \mathrm { l i n e a r i z e d } } } \\ { { \mathrm { l i n e a r i z e d } } } \end{array}  } \end{array}
$$

The components of te stress-energy tensor, $T _ { \hat { \alpha } \hat { \beta } } = ( \rho + p ) u _ { \hat { \alpha } } u _ { \hat { \beta } } + p \eta _ { \alpha \beta } \mathrm { , }$ as calculated using the 4-velocity (26.6) [transformed into the form $u _ { \widehat { o } } = - 1$ ， $u _ { \hat { \tau } } ^ { \cdot } = \dot { \xi } e ^ { \varLambda _ { 0 } - \phi _ { 0 } } ]$ and using expressions (26.3a) for $\pmb { \rho }$ and $p$ ,reduce to

$$
T _ { \hat { r } \hat { t } } = - ( \rho _ { o } + p _ { o } ) e ^ { \Lambda _ { o } - \phi _ { o } } \dot { \xi } , T _ { \hat { r } \hat { \tau } } = p _ { o } + \delta p .
$$

Consequently, the field equation $G _ { \hat { r } \hat { t } } = 8 \pi T _ { \hat { r } \hat { t } } $ -after integration with respect to time and choice of the constant of integration, so that $\delta A = 0$ when $\xi = 0$ -reduces to

$$
\delta A = - 4 \pi ( \rho _ { o } + p _ { o } ) r e ^ { 2 \varLambda _ { o } } \xi = - ( A _ { o } ^ { \prime } + \varPhi _ { o } ^ { \prime } ) \xi .
$$

This is the initial-value equation for 8A.The field equation $G _ { \widehat { r } \widehat { \tau } } = 8 \pi T _ { \widehat { r } \widehat { \tau } } ,$ after using (26.15) to remove $\pmb { \delta A }$ and (26.9) to remove $\delta \boldsymbol { p }$ ,and (26.1c) to remove ${ \pmb \phi } _ { \pmb 0 } ^ { \prime }$ ,reduces to

$$
\begin{array} { r l } & { \delta \phi ^ { \prime } = - 4 \pi { \cal T } _ { 1 } p _ { o } r ^ { - 1 } e ^ { 2 \Lambda _ { o } + \phi _ { o } } ( r ^ { 2 } e ^ { - \phi _ { o } } \xi ) ^ { \prime } } \\ & { ~ + ~ [ 4 \pi { p _ { o } } ^ { \prime } r - 4 \pi ( \rho _ { o } + p _ { o } ) ] e ^ { 2 \Lambda _ { o } } \xi . } \end{array}
$$

This is the initial-value equation for $\delta \varPhi$

# $\$ 20.5$ . DYNAMIC EQUATION AND BOUNDARY CONDITIONS

The dynamic evolution of the fluid displacement $\xi ( t , r )$ is governed by the Euler equation (22.13):

Derivation of equation of motion for fluid displacement $\pmb { \xi }$

$$
( \rho + p ) \times ( 4 \mathrm { - a c c e l e r a t i o n } ) = - ( \mathrm { p r o j e c t i o n \ o f \ } \Psi p \ \mathrm { o r t h o g o n a l \ t o } \ u ) .
$$

The 4-acceleration $\pmb { \sigma } = \pmb { \nabla } _ { \pmb { u } } \pmb { u }$ corresponding to the 4-velocity (26.6) in the metric (26.2) has as its only non-zero, linearized,covariant component:

$$
a _ { r } = \phi _ { o } ^ { ~ \prime } + \delta \phi ^ { \prime } + e ^ { 2 ( \mathcal { A } _ { o } - \phi _ { o } ) } \ddot { \xi } .
$$

[The component $a _ { t }$ is trivial in the sense that it leads to an Euler equation that duplicates (26.1c).]Combining this with $\rho + p = \rho _ { o } + p _ { o } + \delta \rho + \delta p$ , with the radial component $\bar { p _ { o } } ^ { \prime } + \delta p ^ { \prime }$ for the projection of $\triangledown p$ , and with the zero-order equation of hydrostatic equilibrium (26.1c),one obtains for the Euler equation

$$
( \rho _ { o } + p _ { o } ) e ^ { 2 ( \lambda _ { o } - \phi _ { o } ) } \ddot { \xi } = - \delta p ^ { \prime } - ( \hat { \delta } \rho + \hat { \delta } p ) \phi _ { o } ^ { \prime } - ( \rho _ { o } + p _ { o } ) \hat { \delta } \phi ^ { \prime } .
$$

This equation of motion is put into its most useful form by using the initial-value equations (26.9), (26.11),and (26.16) to reexpress $\delta p , \delta \rho$ ,and $\delta \varPhi ^ { \prime }$ in terms of $\xi ,$ and by then manipulating terms extensively with the aid of the zero-order equations of structure (26.1). The result is

$$
\begin{array} { r } { W \ddot { \zeta } = ( P \zeta ^ { \prime } ) ^ { \prime } + Q \xi , } \end{array}
$$

where $\boldsymbol { \zeta }$ is a “renormalized displacement function,”and $W , P , Q$ are functions of radius determined by the structure of the equilibrium star:

$$
\zeta \equiv r ^ { 2 } e ^ { - \phi _ { o } } \xi ;
$$

$$
W \equiv ( \rho _ { o } + p _ { o } ) r ^ { - 2 } e ^ { 3 \varLambda _ { o } + \phi _ { o } } ;
$$

$$
P \equiv { \cal T } _ { 1 } p _ { o } r ^ { - 2 } e ^ { \varLambda _ { o } + 3 \phi _ { o } } ;
$$

$$
Q \equiv e ^ { \Lambda _ { o } + 3 \phi _ { o } } \Big [ { \frac { ( p _ { o } ^ { \prime } ) ^ { 2 } } { \rho _ { o } + p _ { o } } } r ^ { - 2 } - 4 p _ { o } { ' r ^ { - 3 } } - 8 \pi ( \rho _ { o } + p _ { o } ) p _ { o } r ^ { - 2 } e ^ { 2 \Lambda _ { o } } \Big ] .
$$

Equation (26.19) is the dynamic equation governing the stellar pulsations. [This equation could be written in other forms; for instance, it_could be multiplied by $W ^ { - 1 }$ or any other non-zero factor, and terms could be regrouped. The form given in equation (26.19) is preferred because it leads to a self-adjoint eigenvalue problem for the oscillation frequencies,as indicated in Box 26.1.]

Boundary conditions on fluid displacement

Not all solutions of the dynamic equation are acceptable. To be physically acceptable, the displacement function must produce noninfinite density and pressure perturbations $( \delta \rho$ and $\delta \hat { p } .$ ）at the center of the sphere,which means

$$
( \xi / r ) \mathrm { ~ f i n i t e ~ o r ~ } z \mathrm { e r o ~ i n ~ l i m i t ~ a s ~ } r \longrightarrow 0
$$

[see (26.9) and (26.11)]; also,it must leave the pressure equal to zero at the star's surface,which means

$$
\begin{array} { r } { \begin{array} { r } { \varDelta p = - \varGamma _ { 1 } p _ { o } r ^ { - 2 } e ^ { \phi _ { o } } ( r ^ { 2 } e ^ { - \phi _ { o } } \xi ) ^ { \prime } \longrightarrow 0 \mathrm { ~ a s ~ } r \longrightarrow R } \\ { \lbrack \mathrm { s u r f a c e ~ r a d i u s } \rbrack \longrightarrow } \end{array} } \end{array}
$$

[see (26.8), (26.7),and (26.15)].

# \$26.6. SUMMARY OF RESULTS

Summary of theory of stellar puisations

If an initial displacement of the fluid, $\xi ( t = 0 , r )$ ,is specified subject to the boundary conditions (26.22), then its subsequent evolution $\xi ( t , r )$ can be calculated by inte-

grating the dynamic equation (26.19); and the form of the pressure, density,and metric perturbations can be calculated from $\xi ( t , r )$ using the initial-value equations (26.9), (26.11), (26.15),and (26.16).

Several important consequences of these results are explored in Boxes 26.1 and 26.2.

(continued on page 699)

# Box 26.1 EIGENVALUE PROBLEM AND VARIATIONAL PRINCIPLE FOR NORMAL-MODE PULSATIONS OF A STAR

Assume that the renormalized displacement function (26.2O) has a sinusoidal time dependence:

$$
\begin{array} { r } { \zeta = \xi ( r ) e ^ { - i \omega t } . } \end{array}
$$

Then the dynamic equation (26.19) and boundary conditions (26.22) reduce to an eigenvalue problem for the angular frequency $\pmb { \omega }$ and amplitude $\xi ( r )$ ：

$$
\begin{array} { r } { ( P \xi ^ { \prime } ) ^ { \prime } + Q \xi + \omega ^ { 2 } W \xi = 0 , } \end{array}
$$

$$
\xi / r ^ { 3 } ~ { \mathrm { f i n i t e ~ o r ~ z e r o ~ a s ~ } } r \longrightarrow 0 ,
$$

$$
\begin{array} { r } { T _ { 1 } p _ { 0 } r ^ { - 2 } e ^ { \phi _ { 0 } } \zeta ^ { \prime } \longrightarrow 0 \mathrm { ~ a s ~ } r \longrightarrow R . } \end{array}
$$

Methods for solving this eigenvalue problem are catalogued and discussed by Bardeen, Thorne,and Meltzer (l966). One method (but not the best for numerical calculations） is the variational principle:

$$
\omega ^ { 2 } = \mathrm { { e x t r e m a l ~ v a l u e ~ o f } } \left\{ \frac { \displaystyle \int _ { 0 } ^ { R } ( P \xi ^ { \prime 2 } - Q \xi ^ { 2 } ) d r } { \displaystyle \int _ { 0 } ^ { R } W \xi ^ { 2 } d r } \right\} ,
$$

where $\boldsymbol { \zeta }$ is varied over al functions satisfying the boundary conditions (2).[See e.g., $\ S 1 2 . 3$ of Mathews and Walker (1965) for discussion of the equivalence between this variational principle and the original eigenvalue problem.]

The absolute minimum value of expression (3) is the squared frequency of the fundamental mode of pulsation. If it is negative, the star is unstable $( e ^ { - \mathrm { i } \omega t }$ grows exponentially in time). If it is positive,the star is stable against adiabatic,radial perturbations. Therefore,since the denominator of expression (3) is positive definite,

$$
\left[ \begin{array} { l } { \mathrm { s t a b i l i t y ~ a g a i n s t } } \\ { \mathrm { a d i a b a t i c ~ r a d i a l } } \\ { \mathrm { p e r t u r b a t i o n s } } \end{array} \right] \Longleftrightarrow \left[ \begin{array} { r } { \int _ { 0 } ^ { R } ( P \xi ^ { \prime 2 } - Q \xi ^ { 2 } ) d r > 0 \mathrm { ~ f o r ~ a l l ~ f u n c t i o n s } } \\ { \qquad \xi \mathrm { ~ s a t i s f y i n g ~ } ( 2 ) } \end{array} \right] .
$$

By numerical solution of the eigenvalue equation (l), the pulsation frequencies have been calculated for a wide variety of models of neutron stars and supermassive stars.Example: The figure gives a plot of pulsation frequency as a function of central density for the lowest four normal modes of the Harrison-Wakano-Wheeler models at the endpoint of stellar evolution. (Make a detailed comparison with Figure 24.2.) These curves are based on calculations by Meltzer and Thorne (l966),with corrections for the fundamental mode of massive white dwarfs by Faulkner and Gribbin (1968).

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0011_pages_0701-0770/auto/images/925cb5e5d29e3b24012a5aa778375ce84cf9e150e77c18afe93c700a4d42735c.jpg)  
Box 26.1 (continued)

# Box 26.2 THE CRITICAL ADIABATIC INDEX FOR NEARLY NEWTONIAN STARS

# A. Fully Newtonian Stars

1. For a Newtonian star that pulsates sinusoidally, $\xi = \xi ( r ) e ^ { - i \omega t }$ , the dynamic equation (26.19) reduces to

$$
[ { \cal T } _ { 1 } p _ { o } r ( { \xi / r } ) ^ { \prime } ] ^ { \prime } + 3 ( { \cal T } _ { 1 } p _ { o } { \xi / r } ) ^ { \prime } - { 4 } p _ { o } { ^ { \prime } \xi / r } + \omega ^ { 2 } \rho _ { o } { \xi } = 0 .
$$

2.If ${ \cal T } _ { 1 } = 4 / 3$ throughout the star, the physically acceptable solution [solution satisfying boundary conditions (26.22)] for the fundamental mode of vibration (mode with lowest value of $\omega ^ { 2 }$ is

$$
\omega ^ { 2 } = 0 , ~ \xi = \epsilon r , ~ \epsilon = \mathrm { c o n s t . }
$$

Thus, for $\varGamma _ { 1 } = 4 / 3$ the fundamental mode is“neutrally stable”and has a “homologous” displacement function-independent of the star's equation of state or structure.

3.If $T _ { 1 }$ is allowed to differ slightly from $4 / 3$ in an $r$ -dependent way, then $\xi ( r )$ will differ slightly from the homologous form:

Consequently, if one uses the homologous expression $\xi = \epsilon r$ as a trial function in the variational principle of Box 26.l,one will obtain $\omega ^ { 2 }$ accurate to $O [ ( { \cal { I } } _ { 1 } - 4 / 3 ) ^ { 2 } ]$ . (Recall: first-order errors in trial function produce second-order errors in value of variational expression.) The Newtonian limit of the variational expression [equation (3) of Box 26.1] becomes,with the homologous choice of trial function,

$$
\omega ^ { 2 } = ( 3 \overline { { \cal T } } _ { 1 } - 4 ) \frac { \int _ { 0 } ^ { R } 3 p _ { o } r ^ { 2 } d r } { \int _ { 0 } ^ { R } \rho _ { o } r ^ { 4 } d r } + { \cal O } [ ( 3 \overline { { \cal T } } _ { 1 } - 4 ) ^ { 2 } ] ,
$$

where $\boldsymbol { \overline { { { T } } } _ { 1 } }$ is the pressure-averaged adiabatic index

$$
\begin{array} { r } { \overline { { T } } _ { 1 } = \frac { \displaystyle \int _ { 0 } ^ { R } { \cal T } _ { 1 } p _ { \circ } 4 \pi r ^ { 2 } d r } { \displaystyle \int _ { 0 } ^ { R } p _ { o } 4 \pi r ^ { 2 } d r } . } \end{array}
$$

By use of the Newtonian virial theorem for the nonpulsating star [equation (39.21b) or exercise 23.7], one can convert equation (3) into the form

$$
\omega ^ { 2 } = ( 3 \bar { \cal T } _ { 1 } - 4 ) | \varOmega | / { \cal I } ,
$$

where $\varOmega$ is the star's self-gravitational energy and $I = \int ( \rho _ { o } r ^ { 2 } ) 4 \pi r ^ { 2 } \ _ { \langle }$ dr is the trace of the second moment of its mass distribution (see Box 24.2 and exercise 39.6).

# B. Nearly Newtonian Stars

1. When one takes into account first-order relativistic corrections (corrections of order $M / R$ ), but ignores higher-order corrections, one can rewrite the variational expression [equation (3) of Box 26.1] in the form

$$
\omega ^ { 2 } = \frac { \displaystyle \int _ { 0 } ^ { R } p _ { o } [ { \cal T } _ { 1 } r ^ { 4 } \eta ^ { \prime 2 } + ( 3 { \cal T } _ { 1 } - 4 ) ( r ^ { 3 } \eta ^ { 2 } ) ^ { \prime } ] ( 1 + A _ { o } + 3 \phi _ { o } ) d r - \displaystyle \int _ { 0 } ^ { R } F _ { o } \eta ^ { 2 } d r } { \displaystyle \int _ { 0 } ^ { R } \rho _ { o } r ^ { 4 } ( 1 + 3 A _ { o } + \phi _ { o } + p _ { o } / \rho _ { o } ) \eta ^ { 2 } d r } ,
$$

where

$$
F _ { o } \equiv 8 \pi r ^ { 4 } p _ { o } \rho _ { o } + 8 r m _ { o } p _ { o } + \rho _ { o } { m _ { o } } ^ { 2 } , ~ \eta = \xi / r ^ { 3 } = ( \xi / r ) ( 1 - \varPhi _ { o } ) ,
$$

and $m _ { o } ( r )$ is the equilibrium mass inside radius $r$

2. For a relativistic star with $T _ { 1 } - 4 / 3$ of order $M / R$ and with $M / R \ll 1$ ,the homologous trial function $\xi = \epsilon r$ will still be highly accurate. Equally accurate,and easier to work with, will be $\xi = \epsilon r e ^ { \phi _ { \circ } } \approx \epsilon r ( 1 + \varPhi _ { o } )$ ，which corresponds to $\eta = \epsilon =$ constant. Its fractional errors will be of order $M / r ;$ and the errors which it produces in $\omega ^ { 2 }$ will be of order $( M / R ) ^ { 2 }$ .By inserting this trial function into the variational principle (6)and keeping only relativistic corrections of order $M / R _ { \mathrm { i } }$ one obtains

$$
\omega ^ { 2 } = 3 ( \vec { \Gamma } _ { 1 } - \varGamma _ { \mathrm { 1 c r i t } } ) | \varOmega | / I .
$$

Here $\boldsymbol { \overline { { { \cal { T } } } } _ { 1 } }$ is the pressure-averaged adiabatic index, and the critical value of the adiabatic index $\boldsymbol { T } _ { 1 \mathrm { c r i t } }$ is

$$
{ \cal T } _ { \mathrm { 1 c r i t } } = \frac { 4 } { 3 } + { \alpha } { \cal M } / R ,
$$

with $\pmb { \alpha }$ a positive constant of order unity given by

$$
\alpha = \frac { 1 } { 3 } \frac { R } { M | \varOmega | } \int _ { 0 } ^ { R } \biggl ( 3 \rho _ { o } \frac { { m _ { o } } ^ { 2 } } { r ^ { 2 } } + 4 p _ { o } \frac { m _ { o } } { r } \biggr ) 4 \pi r ^ { 2 } d r .
$$

Expressions (8)and (9) for the pulsation frequency and the adiabatic index play an important role in the theory of supermassive stars (S24.4).

3.For alternative derivations of the above result,see Chandrasekhar (1964a,b; 1965c),Fowler (1964,1965), Wright (1964).

# Exercise 26.1. DRAGGING OF INERTIAL FRAMES BY A SLOWLY ROTATING STAR

EXERCISE

A fluid sphere rotates very slowly. Analyze its rotation using perturbation theory; keep only effects and terms linear in the angular velocity of rotation.[Hints: (l) Centrifugal forces are second-order in angular velocity. Therefore,to first order the star is undeformed; its density and pressure distributions remain spherical and unperturbed. (2) Show, by symmetry and time-reversal arguments, that one can introduce coordinates in which

$$
\begin{array} { c } { { d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + r ^ { 2 } [ d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ] } } \\ { { - 2 ( r ^ { 2 } \mathrm { s i n } ^ { 2 } \theta ) \omega d \phi d t , } } \end{array}
$$

where

$$
\phi = \phi ( r ) , \ : { \cal { A } } = { \cal { A } } ( r ) , \ : { \mathrm { a n d } } \ : \omega = \omega ( r , \theta ) .
$$

Show that $\bar { \pmb { \phi } } = \bar { \pmb { \phi } } _ { o }$ and $\pmb { { \cal A } } = { \cal A } _ { o }$ (no perturbations!) to first-order in angular velocity. (3)Adopt the following precise definition of the angular velocity $\varOmega ( r , \theta )$ ：

$$
\mathcal { Q } \equiv u ^ { \phi } / u ^ { t } = ( d \phi / d t ) _ { \mathrm { m o v i n g w i t h t h e f l u i d } } .
$$

Assuming $u ^ { \prime } = u ^ { \theta } = 0$ (i.e., rotation in the $\phi$ direction), calculate the 4-velocity of the fluid. (4) Use the Einstein field equations to derive a differential equation for the metric perturbation $\pmb { \omega }$ in terms of the angular velocity $\pmb { \it { \Omega } }$ .(5） Solve that differential equation outside the star in terms of elementary functions,and express the solution for $\omega ( r , \theta )$ in terms of the star's total angular momentum $\pmb { S } .$ ，as measured using distant gyroscopes (see Chapter 19).] For the original analyses of this problem and of related topics,see Gurovich (1965),Doroshkevich,Zel'dovich,and Novikov (1965),Hartle and Sharp (1965),Brill and Cohen (1966), Hartle (1967),Krefetz (1967),Cohen and Brill (1968),Cohen (1968).

PART VI

# THE UNIVERSE

Wherein the reader,flushed with joy at his conquest of the stars,seeks to control the entira universe,and is foiled by an unfathomed mystery:the Initial Singularity.
