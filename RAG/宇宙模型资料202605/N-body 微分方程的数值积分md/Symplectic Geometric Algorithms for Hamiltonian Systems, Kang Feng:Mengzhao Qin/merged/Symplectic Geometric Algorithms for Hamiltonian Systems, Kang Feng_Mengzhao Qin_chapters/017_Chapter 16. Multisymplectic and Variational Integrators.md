# Chapter 16. Multisymplectic and Variational Integrators

Recently, multisymplectic discretizations have been drawing much attention and, therefore, have become the vigorous component of the structure-preserving algorithms. In this chapter, we systematically develop what our research group has achieved in the field of multisymplectic discretizations. Some very interesting new issues arising in this field are also given. Multisymplectic and variational integrators are studied from a comparative point of view. The implementation issues of multisymplectic integrators are discussed, and composition methods to construct higher order multisymplectic integrators are presented. The equivalence of variational integrators to multisymplectic integrators is proved. Several generalizations are also described.

# 16.1 Introduction

The introduction of symplectic integrators is a milestone in the development of numerical analysis[Fen85] . It has led to the establishment of structure-preserving algorithms, a very promising subject. Due to its high accuracy, good stability and, in particular, the capability for long-term computation, the structure-preserving algorithms have proved to be very powerful in numerical simulations. The applications of structure-preserving algorithms can be found on diverse branches of physics, such as celestial mechanics, quantum mechanics, fluid dynamics, geophysics[LQHD07,MPSM01,WHT96] , etc.

Symplectic algorithms for finite dimensional Hamiltonian systems have been well established. They not only bring new insights into existing methods but also lead to many powerful new numerical methods. The structure-preserving algorithms for infinite dimensional Hamiltonian systems are comparatively less explored. Symplectic integrators for infinite dimensional Hamiltonian systems were also considered [Qin90,LQ88,Qin87,Qin97a] . The basic idea is, first to discretize the space variables appropriately so that the resulting semi-discrete system is a Hamiltonian system in time; and second, to apply symplectic methods to this semi-discrete system. The symplectic integrator obtained in this way preserves a symplectic form which is a sum over the discrete space variables. In spite of its success, a problem remains: the change of the symplectic structure over the spatial domain is not reflected in such methods.

This problem was solved by introducing the concept of multisymplectic integrators (Bridges and Reich[BR01a,BR06] ). In general, an infinite dimensional Hamiltonian system can be reformulated as a multisymplectic Hamiltonian system in which associated to every time and space direction, there exists a symplectic structure and a multisymplectic conservation law is satisfied. The multisymplectic conservation law is completely local and reflects the change of the symplecticity over the space domain. A multisymplectic integrator is a numerical scheme for the multisymplectic Hamiltonian system which preserves a discrete multisymplectic conservation law, characterizing the spatial change of the discrete symplectic structure. The multisymplectic integrator is the direct generalization of the symplectic integrator and has good performance in conserving local conservation laws. A disadvantage of the multisymplectic integrator is the introduction of many new variables which usually are not needed in numerical experiments. To solve this problem, we can eliminate the additional variables from some multisymplectic integrators and obtain a series of new schemes for the equations considered. On the construction of multisymplectic integrators, it was proved that using symplectic Runge–Kutta integrators in both directions lead to multisymplectic integrators[Rei00] . In this chapter, another approach, namely the composition method will be presented.

The multisymplectic integrator is based on the Hamiltonian formalism. In the Lagrangian formalism, a geometric-variational approach to continuous and discrete mechanics and field theories is known by Marsden, Patrik, and Shkoller[MPS98] . The multisymplectic form is obtained directly from the variational principle, staying entirely on the Lagrangian side, but the local energy and momentum conservation laws are not particularly addressed. By disretizing the Lagrangian and using a discrete variational principle, variational integrators are obtained, which satisfy a discrete multisymplectic $\mathrm { f o r m ^ { \mathrm { [ M P S 9 8 ] } } }$ . Taking the sine-Gordon equation and the nonlinear Schrodinger equation ¨ as examples, we will show that some variational integrators are equivalent to multisymplectic integrators.

In addition to the standard multisymplectic and variational integrators, we have more ambitious goal of presenting some generalizations, including multisymplectic Fourier pseudospectral methods on real space, nonconservative multisymplectic Hamiltonian systems, constructions of multisymplectic integrators for modified equations and multisymplectic Birkhoffian systems[SQ01,SQWR08,SQS07] .

This chapter is organized as follows. In the next Section 16.2, the basic theory of multisymplectic geometry and multisymplectic Hamiltonian systems is presented. Section 16.3 is devoted to developing multisymplectic integrators. In Section 16.4, the variational integrators are discussed. In Section 16.5, some generalizations are given.

# 16.2 Multisymplectic Geometry and Multisymplectic Hamiltonian Systems

In this section, the basic theory needed for multisymplectic and variational integrators is discussed. The basic theory includes multisymplectic geometry and multisymplectic Hamiltonian system. We will present the theory from the perspective of the total variation[Lee82,Lee87] , always named Lee variational integrator (see Chapter 14)[Che02,CGW03] .

1. Multisymplectic geometry Exclusively, local coordinates are used and the notion of prolongation spaces instead of jet bundles $[ \mathrm { O l v 8 6 } , \mathrm { C h e 0 } 5 \mathrm { c } ]$ is employed. The covariant configuration space is denoted by $X \times U$ and $X$ represents the space of independent variables with coordinates $\displaystyle { \mathfrak { c } } ^ { \mu } \left( \mu = 1 , 2 , \cdots , n , 0 \right)$ , and $U$ the space of dependent variables with coordinates $u ^ { A } \left( A = 1 , 2 , \cdot \cdot \cdot , N \right)$ . The first-order prolongation of $X \times$ $U$ is defined to be

$$
U ^ { ( 1 ) } = X \times U \times U _ { 1 } ,
$$

where $U _ { 1 }$ represents the space consisting of first-order partial derivatives of $u ^ { A }$ with respect to $x ^ { \mu }$ .

Let $\phi : X \to U$ be a smooth function, then its first prolongation is denoted by

$$
\mathrm { p r } ^ { 1 } \phi = ( x _ { \mu } , \phi ^ { A } , \phi _ { \mu } ^ { A } ) .
$$

A Lagrangian density, $\mathcal { L }$ is defined as follows:

$$
\begin{array} { r l } & { \mathcal { L } : U ^ { ( 1 ) } \longrightarrow \Lambda ^ { n + 1 } ( X ) , } \\ & { } \\ & { \mathcal { L } ( \mathrm { p r } ^ { 1 } \phi ) = L ( x _ { \mu } , \phi ^ { A } , \phi _ { \mu } ^ { A } ) \mathrm { d } ^ { n + 1 } x , } \end{array}
$$

where $\Lambda ^ { n + 1 } ( X )$ is the space of $n + 1$ forms over $X$ .

Corresponding to the Lagrangian density (2.2), the action functional is defined by

$$
\mathcal { S } ( \phi ) = \int _ { M } L ( x _ { \mu } , \phi ^ { A } , \phi _ { \mu } ^ { A } ) \mathrm { d } ^ { n + 1 } x , \quad M \mathrm { i s  a n o p e n s e t i n } X .
$$

Let $V$ be a vector field on $X \times U$ with the form

$$
V = \xi ^ { \mu } ( { \pmb x } ) \frac { \partial } { \partial x ^ { \mu } } + \alpha _ { A } ( { \pmb x } , { \pmb u } ) \frac { \partial } { \partial u ^ { A } } ,
$$

where $\pmb { x } = ( x ^ { 1 } , \cdots , x ^ { n } , x ^ { 0 } )$ , $\pmb { u } = ( u ^ { 1 } , \cdots , u ^ { N } )$ and we use Einstein summation convention here.

The flow $\exp ( \lambda V )$ of the vector field $V$ is a one-parameter transformation group of $X \times U$ and transforms a map $\phi : M \to U$ to a family of maps $\tilde { \phi } : \tilde { M } \to U$ depending on the parameter $\lambda$ . Now, we calculate the variation of the action functional (2.3). For simplicity , let $n = 1 , N = 1$ and $x ^ { 1 } = x , x ^ { 0 } = t , u ^ { 1 } = u , \alpha _ { 1 } = \alpha$ , then it follows that

$$
\delta S = \frac { \mathrm { d } } { \mathrm { d } \lambda } \Big \vert _ { \lambda = 0 } S ( \tilde { \phi } ) = \frac { \mathrm { d } } { \mathrm { d } \lambda } \Big \vert _ { \lambda = 0 } \int _ { \tilde { M } } L ( \tilde { x } , \tilde { t } , \tilde { \phi } , \tilde { \phi } _ { \tilde { x } } , \tilde { \phi } _ { \tilde { t } } ) \mathrm { d } \tilde { x } \wedge \mathrm { d } \tilde { t } = A + B ,
$$

where

$$
\begin{array} { r l r } { A } & { = } & { \displaystyle { \int _ { M } [ ( \frac { \partial { \cal L } } { \partial t } + D _ { t } \Big ( \frac { \partial { \cal L } } { \partial \phi _ { t } } \phi _ { t } - { \cal L } \Big ) + D _ { x } \Big ( \frac { \partial { \cal L } } { \partial \phi _ { x } } \phi _ { t } \Big ) ) \xi ^ { 0 } \ } \mathrm { ~ } } \\ & { } & { \displaystyle { + \Big ( \frac { \partial { \cal L } } { \partial x } + D _ { x } \Big ( \frac { \partial { \cal L } } { \partial \phi _ { x } } \phi _ { x } - { \cal L } \Big ) + D _ { t } \Big ( \frac { \partial { \cal L } } { \partial \phi _ { t } } \phi _ { x } \Big ) \Big ) \xi ^ { 1 } \ ~ } } \\ & { } &  \displaystyle { + ( \frac { \partial { \cal L } } { \partial \phi } - D _ { x } \frac { \partial { \cal L } } { \partial \phi _ { x } } - D _ { t } \frac { \partial { \cal L } } { \partial \phi _ { t } } ) \alpha \Bigg ] \ \mathrm { d } x \wedge \mathrm { d } t , } \end{array}
$$

and

$$
\begin{array} { l } { B = \displaystyle \int _ { \partial M } \left[ \left( \left( \frac { \partial L } { \partial \phi _ { t } } \phi _ { t } - L \right) \mathrm { d } x - \frac { \partial L } { \partial \phi _ { x } } \phi _ { t } \mathrm { d } t \right) \xi ^ { 0 } \right. } \\ { \displaystyle \left. + \left( \left( L - \frac { \partial L } { \partial \phi _ { x } } \phi _ { x } \right) \mathrm { d } t + \frac { \partial L } { \partial \phi _ { t } } \phi _ { x } \mathrm { d } x \right) \xi ^ { 1 } \right. } \\ { \displaystyle \left. + \left( \frac { \partial L } { \partial \phi _ { x } } \mathrm { d } t - \frac { \partial L } { \partial \phi _ { t } } \mathrm { d } x \right) \alpha \right] . } \end{array}
$$

If $\xi ^ { 1 } ( x ) , \xi ^ { 0 } ( x )$ , and $\alpha ( x , t , \phi ( x , t ) )$ have compact support on $M$ , then $B = 0$ . In this case, with the requirement of $\delta { \cal S } = 0$ and from (2.4), the variation $\xi ^ { 0 }$ yields the local energy evolution equation

$$
\frac { \partial L } { \partial t } + D _ { t } \Big ( \frac { \partial L } { \partial \phi _ { t } } \phi _ { t } - L \Big ) + D _ { x } \Big ( \frac { \partial L } { \partial \phi _ { x } } \phi _ { t } \Big ) = 0 ,
$$

and the variation $\xi ^ { 1 }$ the local momentum evolution equation

$$
\frac { \partial L } { \partial x } + D _ { x } \Big ( \frac { \partial L } { \partial \phi _ { x } } \phi _ { x } - L \Big ) + D _ { t } \Big ( \frac { \partial L } { \partial \phi _ { t } } \phi _ { x } \Big ) = 0 .
$$

For a conservative $L$ , i.e., the one that does not depend on $x , t$ explicitly, (2.6) and (2.7) become the local energy conservation law and the local momentum conservation law respectively.

The variation $\alpha$ yields the Euler–Lagrange equation

$$
\frac { \partial L } { \partial \phi } - D _ { x } \frac { \partial L } { \partial \phi _ { x } } - D _ { t } \frac { \partial L } { \partial \phi _ { t } } = 0 .
$$

If the condition that $\xi ^ { 1 } ( x , t ) , \xi ^ { 0 } ( x , t )$ , $\alpha ( x , t , \phi ( x , t ) )$ have compact support on $M$ is not imposed, then from the boundary integral $B$ , we can define the Cartan form

$$
\varTheta _ { \mathcal { L } } = \frac { \partial L } { \partial \phi _ { x } } \mathrm { d } \phi \wedge \mathrm { d } t - \frac { \partial L } { \partial \phi _ { t } } \mathrm { d } \phi \wedge \mathrm { d } x + \left( L - \frac { \partial L } { \partial \phi _ { x } } \phi _ { x } - \frac { \partial L } { \partial \phi _ { t } } \phi _ { t } \right) \mathrm { d } x \wedge \mathrm { d } t ,
$$

which satisfies using the interior product $\lrcorner$ and the pull-back mapping $( ) ^ { * }$

$$
B = \int _ { \partial M } ( \mathbf { p r } ^ { 1 } \phi ) ^ { * } ( \mathbf { p r } ^ { 1 } V \rfloor \theta _ { \mathcal { L } } ) .
$$

The multisymplectic form is defined to be $\Omega _ { \mathcal { L } } = \mathbf { d } \theta _ { \mathcal { L } }$ .

Theorem 2.1. [MPS98,GAR73] Suppose $\phi$ is the solution of (2.8), and let $\eta ^ { \lambda }$ and $\zeta ^ { \lambda }$ be two one-parameter symmetry groups of Equation (2.8), and $V _ { 1 }$ and $V _ { 2 }$ be the corresponding infinitesimal symmetries, then we have the multisymplectic form formula

$$
\int _ { \partial M } ( \mathrm { p r } ^ { 1 } \phi ) ^ { * } ( \mathrm { p r } ^ { 1 } \mathrm { V } _ { 1 } ] \ \mathrm { p r } ^ { 1 } \mathrm { V } _ { 2 } \lrcorner \ \Omega _ { \mathcal { L } } ) = 0 .
$$

# 2. Multisymplectic Hamiltonian systems

A large class of partial differential equations can be represented a $_ \mathrm { ; } [ { \bf B R 0 6 , B r i 9 7 } ]$

$$
\boldsymbol { M } \boldsymbol { z } _ { t } + \boldsymbol { K } \boldsymbol { z } _ { x } = \boldsymbol { \bigtriangledown } _ { \boldsymbol { z } } \boldsymbol { S } ( \boldsymbol { z } ) ,
$$

where $z \in \mathbf { R } ^ { n }$ , $M$ and $K$ are antisymmetric matrices in $\mathbf { R } ^ { n \times n } , n \geq 3$ and $S : \mathbf { R } ^ { n } \to$ $\mathbf { R }$ is a smooth function. Here for simplicity, we only consider one space dimension.

We call (2.12) a multisymplectic Hamiltonian system, since it possesses a multisymplectic conservation law

$$
D _ { t } \omega + D _ { x } \kappa = 0 ,
$$

where $D _ { t } = \frac { \mathrm { ~ d ~ } } { \mathrm { ~ d ~ } t }$ , $D _ { x } = \frac { \mathrm { ~ d ~ } } { \mathrm { ~ d ~ } x }$ and $\omega$ and $\kappa$ are the presymplectic form

$$
\omega = \frac { 1 } { 2 } \mathbf { d } z \wedge M \mathbf { d } z , \quad \kappa = \frac { 1 } { 2 } \mathbf { d } z \wedge K \mathbf { d } z ,
$$

which are associated to the time direction and the space direction, respectively.

The system (2.12) satisfies a local energy conservation law

$$
\begin{array} { r } { D _ { t } E + D _ { x } F = 0 , } \end{array}
$$

with energy density

$$
E = S ( z ) - \frac { 1 } { 2 } z ^ { \mathrm { T } } K z _ { x }
$$

and energy flux

$$
F = \frac { 1 } { 2 } z ^ { \mathrm { T } } K z _ { t } .
$$

The system (2.12) also has a local momentum conservation law

$$
D _ { t } I + D _ { x } G = 0
$$

with momentum density

$$
I = \frac { 1 } { 2 } z ^ { \mathrm { T } } M z _ { x }
$$

and momentum flux

$$
G = S ( z ) - \frac { 1 } { 2 } z ^ { \mathrm { T } } M z _ { t } .
$$

The multisymplectic Hamiltonian system can be obtained from the Lagrangian density and the covariant Legendre transform, or Legendre–Hodge transformation[Bri06] . The relationship between the Lagrangian and the Hamiltonian formalisms is explained in the following diagram, where in each line the corresponding equations are given[Che05c,Che02,LQ02] .

$$
\frac { \partial L } { \partial \phi } - D _ { x } \frac { \partial L } { \partial \phi _ { x } } - D _ { t } \frac { \partial L } { \partial \phi _ { t } } = 0 \Longleftrightarrow M z _ { t } + K z _ { x } = \bigtriangledown z ^ { S ( z ) } ,
$$

$$
\int _ { \partial M } ( { \mathrm p } \mathrm { \bf r } ^ { 1 } \phi ) ^ { * } ( { \mathrm p } \mathrm { \bf r } ^ { 1 } V _ { 1 } - \mathrm { \bf \delta p r } ^ { 1 } V _ { 2 } \vert \Omega _ { \mathcal { L } } ) = 0 \Longleftrightarrow D _ { t } \omega + D _ { x } \kappa = 0 ,
$$

$$
D _ { t } \left( \frac { \partial L } { \partial \phi _ { t } } \phi _ { t } - L \right) + D _ { x } \left( \frac { \partial L } { \partial \phi _ { x } } \phi _ { t } \right) = 0 \Longleftrightarrow D _ { t } E + D _ { x } F = 0 ,
$$

$$
D _ { x } \left( \frac { \partial { \cal { L } } } { \partial \phi _ { x } } \phi _ { x } - { \cal { L } } \right) + D _ { t } \left( \frac { \partial { \cal { L } } } { \partial \phi _ { t } } \phi _ { x } \right) = 0 \Longleftrightarrow D _ { t } { \cal { I } } + D _ { x } { \cal { G } } = 0 .
$$

# 16.3 Multisymplectic Integrators and Composition Methods

The concept of the multisymplectic integrators for the system (2.12) was introduced by Bridges and Reich[BR01a] . A multisymplectic integrator is a numerical scheme for (2.12) which preserves a discrete multisymplectic conservation law. The multisymplectic integrator is the direct generalization of the symplectic integrator and has good performance in maintaining local conservation laws. Using symplectic Runge–Kutta integrators in both directions leads to multisymplectic integrators[Rei00] .

A popular multisymplectic integrator is the multisymplectic Preissman integrator which is obtained by using the midpoint method in both directions. Discretizing (2.12) by the midpoint method in both directions with step-size $\Delta t$ and $\Delta \tau$ yields

$$
\begin{array} { r } { M \frac { z _ { i + \frac { 1 } { 2 } } ^ { j + 1 } - z _ { i + \frac { 1 } { 2 } } ^ { j } } { \Delta t } + K \frac { z _ { i + 1 } ^ { j + \frac { 1 } { 2 } } - z _ { i } ^ { j + \frac { 1 } { 2 } } } { \Delta x } = \nabla _ { z } S \left( z _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } \right) , } \end{array}
$$

where $\Delta t$ and $\Delta x$ are the time step size and space step size, respectively, and

$$
\begin{array} { r l } & { z _ { i } ^ { j } \approx z ( i \Delta z , j \Delta t ) , \quad z _ { i + \frac { 1 } { 2 } } ^ { j + 1 } = \frac { 1 } { 2 } \left( z _ { i } ^ { j + 1 } + z _ { i + 1 } ^ { j + 1 } \right) , } \\ & { z _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } = \frac { 1 } { 4 } \left( z _ { i } ^ { j } + z _ { i + 1 } ^ { j } + z _ { i } ^ { j + 1 } + z _ { i + 1 } ^ { j + 1 } \right) , \quad \mathrm { e t c . } } \end{array}
$$

The scheme (3.1) satisfies the discrete multisymplectic conservation law

$$
\frac { \omega _ { i + \frac { 1 } { 2 } } ^ { j + 1 } - \omega _ { i + \frac { 1 } { 2 } } ^ { j } } { \Delta t } + \frac { \kappa _ { i + 1 } ^ { j + \frac { 1 } { 2 } } - \kappa _ { i } ^ { j + \frac { 1 } { 2 } } } { \Delta x } = 0 ,
$$

which can be proved by direct calculations.

Example 3.1. First, consider the sine-Gordon equation[Che06b,WM01]

$$
u _ { t t } - u _ { x x } + \sin { u } = 0 .
$$

Introducing the new variables $v = u _ { t }$ and $w = u _ { x }$ , Equation (3.3) is equivalent to the system

$$
- v _ { t } + w _ { x } = \sin u , \quad u _ { t } = v , \quad - u _ { x } = - w ,
$$

which can be represented as

$$
M _ { 1 } z _ { t } + K _ { 1 } z _ { x } = \nabla _ { z } S _ { 1 } ( z ) ,
$$

where

$$
\begin{array} { r } { z = ( u , v , w ) ^ { \mathrm { T } } , \quad S _ { 1 } ( z ) = \frac { 1 } { 2 } ( v ^ { 2 } - w ^ { 2 } ) - \cos { ( u ) } } \end{array}
$$

and

$$
M _ { 1 } = \left( \begin{array} { c c c } { { 0 } } & { { - 1 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) , \quad K _ { 1 } = \left( \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

Applying the multisymplectic integrator (3.1) to (3.3) yields

$$
\begin{array} { r l } { - \frac { v _ { i + \frac { 1 } { 2 } } ^ { j + 1 } - v _ { i + \frac { 1 } { 2 } } ^ { j } } { \Delta t } + \frac { w _ { i + 1 } ^ { j + \frac { 1 } { 2 } } - w _ { i } ^ { j + \frac { 1 } { 2 } } } { \Delta x } = \sin { u _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } } , } & { } \\ { \frac { u _ { i + \frac { 1 } { 2 } } ^ { j + 1 } - u _ { i + \frac { 1 } { 2 } } ^ { j } } { \Delta t } = v _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } , } & { } \\ { - \frac { u _ { i + 1 } ^ { j + \frac { 1 } { 2 } } - u _ { i } ^ { j + \frac { 1 } { 2 } } } { \Delta x } = - w _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } . } & { } \end{array}
$$

Eliminating $v$ and $w$ from (3.6), a nine-point integrator for $u$ is derived

$$
\frac { u _ { ( i ) } ^ { j + 1 } - 2 u _ { ( i ) } ^ { j } + u _ { ( i ) } ^ { j - 1 } } { \Delta t ^ { 2 } } - \frac { u _ { i + 1 } ^ { ( j ) } - 2 u _ { i } ^ { ( j ) } + u _ { i - 1 } ^ { ( j ) } } { \Delta x ^ { 2 } } + \overline { { \sin } } \big ( \bar { u } _ { i } ^ { j } \big ) = 0 ,
$$

where

$$
\begin{array} { r l } & { u _ { ( i ) } ^ { l } = \frac { u _ { i - 1 } ^ { l } + 2 u _ { i } ^ { l } + u _ { i + 1 } ^ { l } } { 4 } , \qquad l = j - 1 , j , j + 1 , } \\ & { u _ { m } ^ { ( j ) } = \frac { u _ { m } ^ { j - 1 } + 2 u _ { m } ^ { j } + u _ { m } ^ { j + 1 } } { 4 } , \quad m = i - 1 , i , i + 1 , } \\ & { \overline { { \sin } } ( \bar { u } _ { i } ^ { j } ) = \frac { 1 } { 4 } \big ( \sin \big ( \bar { u } _ { i } ^ { j } \big ) + \sin \big ( \bar { u } _ { i - 1 } ^ { j } \big ) + \sin \big ( \bar { u } _ { i - 1 j - 1 } \big ) + \sin \big ( \bar { u } _ { i j - 1 } \big ) \big ) , } \\ & { \bar { u } _ { i } ^ { j } = \frac { 1 } { 4 } \big ( u _ { i } ^ { j } + u _ { i + 1 } ^ { j } + u _ { i + 1 } ^ { j + 1 } + u _ { i } ^ { j + 1 } \big ) , \qquad \bar { u } _ { i - 1 } ^ { j } = \frac { 1 } { 4 } \big ( u _ { i - 1 } ^ { j } + u _ { i } ^ { j } + u _ { i } ^ { j + 1 } + u _ { i - 1 } ^ { j + 1 } \big ) , } \\ & { \bar { u } _ { i - 1 } ^ { j - 1 } = \frac { 1 } { 4 } \big ( u _ { i - 1 } ^ { j - 1 } + u _ { i } ^ { j - 1 } + u _ { i } ^ { j } + u _ { i - 1 } ^ { j } \big ) , \quad \bar { u } _ { i } ^ { j - 1 } = \frac { 1 } { 4 } \big ( u _ { i } ^ { j - 1 } + u _ { i + 1 } ^ { j - 1 } + u _ { i + 1 } ^ { j } + u _ { i } ^ { j } \big ) . } \end{array}
$$

Second, consider the nonlinear Schrodinger equation ¨ , written in the form

$$
i \psi _ { t } + \psi _ { x x } + V ^ { \prime } \left( | \psi | ^ { 2 } \right) \psi = 0 .
$$

Using $\psi = p + i q$ and introducing a pair of conjugate momenta $v = p _ { x } , w = q _ { x }$ , Equation (3.8) can be represented[Che06b,Che05b,CQ02,CQT02,SHQ06,SMM04,SQL06,Che04a] as a multisymplectic Hamiltonian system

$$
M _ { 2 } z _ { t } + K _ { 2 } z _ { x } = \bigtriangledown z S _ { 2 } ( z ) ,
$$

where

$$
\begin{array} { l } { \displaystyle { z = ( p , q , v , w ) ^ { \mathrm { T } } , \quad S _ { 2 } ( z ) = \frac { 1 } { 2 } \left( v ^ { 2 } + w ^ { 2 } + V ( p ^ { 2 } + q ^ { 2 } ) \right) } } \end{array}
$$

and

$$
M _ { 2 } = \left( \begin{array} { c c c c } { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) , \quad K _ { 2 } = \left( \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { - 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

From the multisymplectic Preissman integrator (3.1), we obtain a six-point integrator for (3.8)

$$
\textbf { i } \frac { \psi _ { [ i ] } ^ { j + 1 } - \psi _ { [ i ] } ^ { j } } { \Delta t } + \frac { \psi _ { i + 1 } ^ { j + \frac { 1 } { 2 } } - 2 \psi _ { i } ^ { j + \frac { 1 } { 2 } } + \psi _ { i - 1 } ^ { j + \frac { 1 } { 2 } } } { \Delta x ^ { 2 } } + \frac { 1 } { 2 } G _ { i , j } = 0 ,
$$

where

$$
\begin{array} { r l } & { \psi _ { [ i ] } ^ { r } = \frac { 1 } { 4 } \Big ( \psi _ { i - 1 , r } + 2 \psi _ { i , r } + \psi _ { i + 1 , r } \Big ) , \quad r = j , j + 1 , } \\ & { G _ { i , j } = V ^ { \prime } \Big ( \Big | \psi _ { i - \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } \Big | ^ { 2 } \Big ) \psi _ { i - \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } + V ^ { \prime } \Big ( \Big | \psi _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } \Big | ^ { 2 } \Big ) \psi _ { i + \frac { 1 } { 2 } } ^ { j + \frac { 1 } { 2 } } . } \end{array}
$$

Third, consider the KdV equation (Korteweg & de Vries)

$$
u _ { t } + 3 ( u ^ { 2 } ) _ { x } + u _ { x x x } = 0 .
$$

Introducing the new variables $\phi , v$ and $w$ , Equation (3.11) can be represented as

$$
M _ { 3 } z _ { t } + K _ { 3 } z _ { x } = \bigtriangledown z \boldsymbol { S } _ { 3 } ( z ) ,
$$

where

$$
\boldsymbol { z } = ( \phi , u , v , w ) ^ { \mathrm { T } } , \quad S _ { 3 } ( z ) = \frac { 1 } { 2 } \boldsymbol { v } ^ { 2 } + u ^ { 2 } - u w
$$

and

$$
M _ { 3 } = \left( \begin{array} { c c c c } { { 0 } } & { { { \frac { 1 } { 2 } } } } & { { 0 } } & { { 0 } } \\ { { - { \frac { 1 } { 2 } } } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) , \quad K _ { 3 } = \left( \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { - 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) .
$$

From the multisymplectic Preissman integrator (3.1), we obtain an eight-point integrator

$$
\frac { u _ { ( i ) } ^ { j + 1 } - u _ { ( i ) } ^ { j } } { \Delta t } + 3 \frac { \bar { u } _ { i + 1 } ^ { 2 } - \bar { u } _ { i - 1 } ^ { 2 } } { 2 \Delta x } + \frac { u _ { i + 1 } ^ { j + \frac { 1 } { 2 } } - 3 u _ { i } ^ { j + \frac { 1 } { 2 } } + 3 u _ { i - 1 } ^ { j + \frac { 1 } { 2 } } - u _ { i - 2 } ^ { j + \frac { 1 } { 2 } } } { \Delta x ^ { 3 } } = 0 ,
$$

where

$$
\begin{array} { l l l } { { u _ { ( i ) } ^ { l } = \displaystyle \frac { u _ { i - 2 } ^ { l } + 3 u _ { i - 1 } ^ { l } + 3 u _ { i } ^ { l } + u _ { i + 1 } ^ { l } } { 8 } , } } & { { l = j , j + 1 , } } & { { } } \\ { { } } & { { \bar { u } _ { m } ^ { 2 } = \displaystyle \frac { 1 } { 2 } \big ( ( u _ { m + 1 } ^ { j + \frac { 1 } { 2 } } ) ^ { 2 } + ( u _ { m } ^ { j + \frac { 1 } { 2 } } ) ^ { 2 } \big ) , } } & { { m = i - 1 , i + 1 . } } & { { } } \end{array}
$$

A twelve-point integrator for the KdV equation is known[ZQ00,AM04,MM05] , which can be reduced to the eight-point integrator (3.13). Numerical experiments with the integrators mentioned above are given in[WM01,CQT02,ZQ00] . For other soliton equations such as the ZK equation and the KP equation, similar results are obtained[Che03,LQ02] . The coupled Klein–Gordon–Schrodinger equation ¨ [KLX06]

$$
\begin{array} { l } { \displaystyle \mathrm { i } \psi _ { t } + \frac 1 2 \psi _ { x x } + \psi \varphi = 0 , } \\ { \displaystyle \varphi _ { t t } - \varphi _ { x x } + \varphi - | \psi | ^ { 2 } = 0 , \quad \mathrm { i } = \sqrt { - 1 } } \end{array}
$$

is a classical model which describes interaction between conservative complex neutron field and neutral meson Yukawa in quantum field theory.

KGS equation with initial boundary value conditions

$$
\begin{array} { r l r } & { } & { \psi ( 0 , x ) = \psi _ { 0 } ( x ) , \quad \varphi ( 0 , x ) = \varphi _ { 0 } ( x ) , \quad \varphi _ { t } ( 0 , x ) = \varphi _ { 1 } ( x ) , } \\ & { } & { \psi ( t , x _ { L } ) = \psi ( t , x _ { R } ) = \varphi ( t , x _ { L } ) = \varphi ( t , x _ { R } ) = 0 , } \end{array}
$$

where $\psi _ { 0 } ( x ) , \varphi _ { 0 } ( x )$ and $\varphi _ { 1 } ( x )$ are known functions. The problems (3.14), (3.15) and (3.16) has conservative quantity

$$
\| \psi \| ^ { 2 } = \int _ { x _ { L } } ^ { x _ { R } } \psi \bar { \psi } \mathrm { d } x = 1 .
$$

Setting $\psi = p +  { \mathbf { i } } q , \psi _ { x } = p _ { x } +  { \mathbf { i } } q _ { x } = f +  { \mathbf { i } } g ,$

$$
p _ { t } = v , \quad \varphi _ { x } = w , \quad z = ( p , q , f , \varphi , v , w ) ^ { \mathrm { T } } .
$$

The multisymplectic formation of KGS system (3.14) is

$$
\left\{ \begin{array} { l l } { q _ { t } + \frac { 1 } { 2 } f _ { x } = - \varphi p , } \\ { p _ { t } + \frac { 1 } { 2 } g _ { x } = - \varphi q , } \\ { - \frac { 1 } { 2 } p _ { x } = \frac { 1 } { 2 } f , } \\ { - \frac { 1 } { 2 } q _ { z } = - \frac { 1 } { 2 } g , } \\ { - \frac { 1 } { 2 } v _ { t } + \frac { 1 } { 2 } w _ { x } = \frac { 1 } { 2 } \varphi - \frac { 1 } { 2 } ( p ^ { 2 } + q ^ { 2 } ) , } \\ { \frac { 1 } { 2 } \varphi _ { t } - \frac { 1 } { 2 } v , } \\ { - \frac { 1 } { 2 } \varphi _ { x } = - \frac { 1 } { 2 } w . } \end{array} \right.
$$

System (3.17) can be written in standard Bridge form

$$
M \frac { \partial z } { \partial t } + K \frac { \partial z } { \partial x } = \nabla S ,
$$

where matrices $M$ and $K$ (3.18) are

$$
M = \frac { 1 } { 2 } \left( \begin{array} { c c c c c c c c } { 0 } & { - 2 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right) , \quad K = \frac { 1 } { 2 } \left( \begin{array} { c c c c c c c c } { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right)
$$

respectively, and the Hamiltonian function is

$$
S ( z ) = - \frac { 1 } { 2 } \varphi ( p ^ { 2 } + q ^ { 2 } ) + \frac { 1 } { 4 } ( \varphi ^ { 2 } + v ^ { 2 } - w ^ { 2 } - f ^ { 2 } - g ^ { 2 } ) .
$$

For the three local conservation laws corresponding to (3.17), (3.18), we have

$$
\begin{array} { l } { \omega ( z ) = - 2 \mathbf { d } p \wedge \mathbf { d } q - \mathbf { d } \varphi \wedge \mathbf { d } v , } \\ { \kappa ( z ) = \mathbf { d } p \wedge \mathbf { d } f + \mathbf { d } q \wedge \mathbf { d } q + \mathbf { d } \varphi \wedge \mathbf { d } w , } \\ { E ( z ) = - \frac { 1 } { 2 } \varphi ( p ^ { 2 } + q ^ { 2 } ) + \frac { 1 } { 4 } ( \varphi ^ { 2 } + v ^ { 2 } - p f _ { x } - q g _ { x } - \varphi w _ { x } ) , } \\ { F ( z ) = \frac { 1 } { 4 } ( p f _ { t } + q g _ { t } + \varphi w _ { t } - f p _ { t } - g q _ { t } - r w ) , } \\ { I ( z ) = - \frac { 1 } { 2 } \varphi ( p ^ { 2 } + q ^ { 2 } ) + \frac { 1 } { 4 } ( \varphi ^ { 2 } - w ^ { 2 } - f ^ { 2 } - g ^ { 2 } + \varphi v _ { t } ) + \frac { 1 } { 2 } ( p q _ { t } - q p _ { t } ) , } \\ { G ( z ) = \frac { 1 } { 4 } ( - 2 p g + 2 q f - q v _ { x } + v w ) . } \end{array}
$$

Recently, many math physical equations can be solved by Multisymlectic methods, such as Gross–Pitaevskii equation[TM03,TMZM08] , Maxwell’s equations[SQS07,SQ03,CYWB06,STMM07] , Camassa–Holm equation[Dah07] , Kadomtsev–Petviashvili equation[JYJ06] , Seismic wave equation[Che04b,Che04a,Che07a,Che07c,Che07b] , Dirac equation[H L04] , and nonlinear “good” Boussinesq equation $[ \mathrm { H Z Q 0 3 } , \mathrm { C h e 0 5 a } ]$ , etc.

Now, let us discuss the composition method for constructing high order multisymplectic integrators $[ \mathrm { C h e 0 5 c } , \mathrm { C Q 0 3 } ]$ . First, recall the definition of a composition method for $\mathbf { \bar { O } D E s } ^ { [ \mathrm { Y o s } 9 0 , \mathrm { Q Z 9 2 } , \mathrm { S u z 9 2 } ] }$ : Suppose there are $n$ integrators with corresponding operators $s _ { 1 } ( \tau ) , s _ { 2 } ( \tau ) , \cdot \cdot \cdot , s _ { n } ( \tau )$ of corresponding order $p _ { 1 } , p _ { 2 } , \cdots , p _ { n }$ , respectively, having maximal order $\mu = \mathrm { { m a x } } _ { i } ( p _ { i } )$ . If there exists constants $c _ { 1 } , c _ { 2 } , \cdots , c _ { n }$ such that the order of the integrator whose operator is the composition $s _ { 1 } ( c _ { 1 } \tau ) s _ { 2 } ( c _ { 2 } \tau ) \cdot \cdot \cdot s _ { n } ( c _ { n } \tau )$ is $m > \mu$ , then the new integrator is called composition integrator of the original $n$ integrators. This construction of higher order integrators from the lower order ones is called the composition method.

While constructing higher order integrators, the main task is to determine constants $c _ { 1 } , c _ { 2 } , \cdots , c _ { n }$ such that the scheme with the corresponding operator

$$
G _ { m } ( \tau ) = s _ { 1 } ( c _ { 1 } \tau ) s _ { 2 } ( c _ { 2 } \tau ) \cdot \cdot \cdot s _ { n } ( c _ { n } \tau )
$$

has order $m > \mu$ . Now, we will present the basic formula for determining the constants $\boldsymbol { c } _ { i } \left( i = 1 , \cdots , n \right)$ ). For this purpose, we introduce the symmetrization operator $S$

$$
S ( x ^ { p } z ^ { q } ) = \frac { p ! q ! } { ( p + q ) ! } \sum _ { P _ { m } } P _ { m } ( x ^ { p } z ^ { q } ) ,
$$

where $x , z$ are arbitrary noncommutable operators, $P _ { m }$ denotes the summation of all the operators obtained in all possible ways of permutation[Suz92] .

We also introduce a time-ordering operator $P$ :

$$
P ( x _ { i } x _ { j } ) = { \left\{ \begin{array} { l l } { x _ { i } x _ { j } , } & { { \mathrm { i f ~ } } i < j ; } \\ { x _ { j } x _ { i } , } & { { \mathrm { i f ~ } } j < i , } \end{array} \right. }
$$

where $x _ { i } , x _ { j }$ are noncommutable operators $[ \mathsf { S u z 9 2 } ]$ .

Set $G _ { m } ( \tau ) = s _ { 1 } ( c _ { 1 } \tau ) \cdot \cdot \cdot s _ { n } ( c _ { n } \tau )$ . The condition on which $G _ { m }$ has order $m$ reads

$$
P S ( x _ { 1 } ^ { n _ { 1 } } x _ { 2 } ^ { n _ { 2 } } x _ { 3 } ^ { n _ { 3 } } \cdot \cdot \cdot ) = 0 , \quad \sum _ { i = 1 } ^ { n } c _ { i } = 1 ,
$$

where $n _ { 1 } + 2 n _ { 2 } + 3 n _ { 3 } + \cdot \cdot \cdot \leq m$ , excluding $n _ { 2 } = n _ { 3 } = \cdot \cdot \cdot = 0$ .

Given a multisymplectic integrator for (2.12) with accuracy of order $\mathcal { O } ( \tau ^ { p } + \widehat { \tau } ^ { q } )$

$$
M ( s ( \tau ) z _ { i , j } ) + K ( \widehat { s } ( \widehat { \tau } ) z _ { i , j } ) = \nabla _ { z } \ ( \tilde { z } _ { i , j } ) ,
$$

where $s ( \tau )$ and $\widehat { s } ( \widehat { \tau } )$ are discrete operators in $t$ -direction and $x$ -direction respectively, and $\tau$ and $\widehat { \tau }$  are time step and space step respectively. $\tilde { z } _ { i , j } = f _ { s , \hat { s } } ( z _ { i , j } )$ is a function of $z _ { i , j }$ corresponding to the operators $s ( \tau )$ and $\widehat { s } ( \widehat { \tau } )$ .

Suppose $G _ { m } ( \tau )$ is the composition operator of $s ( \tau )$ with accuracy of order $\mathcal { O } ( \tau ^ { m } )$ , and ${ \widehat { G } } _ { n } ( { \widehat { \tau } } )$ is the composition operator of $\widehat { s } ( \widehat { \tau } )$ with accuracy of order $\mathcal { O } ( \widehat { \tau } ^ { n } )$ , then the multisymplectic integrator

$$
M \bigl ( G _ { m } ( \tau ) z _ { i , j } \bigr ) + K \bigl ( \widehat { G } _ { n } ( \widehat { \tau } ) z _ { i , j } \bigr ) = \nabla _ { z } S ( \widetilde { z } _ { i , j } )
$$

has accuracy of order $\mathcal { O } ( \tau ^ { m } + \widehat { \tau } ^ { n } )$ .

# 16.4 Variational Integrators

In this section, variational integrators are discussed. First, we present Veselov-type dicretizations of first-order multisymplectic field theory developed in $\left[ \mathrm { M P S 9 8 } \right]$ . For simplicity, let $n = 1$ , $N = 1$ , $X = \left( x , t \right)$ , $U = ( u )$ , and take $\widehat { \mathbb X } = \widehat { \left( \boldsymbol { x } _ { i } , t _ { j } \right) }$ and $\mathbb { U } = ( u _ { i j } )$ as the discrete versions of $X$ and $U$ . It is more suitable to use only the indices of the grid and set $\mathbb { X } = ( i , j )$ .

A rectangle $\boxed { \begin{array} { r l } \end{array} }$ of $\mathbb { X }$ is an ordered quadruple of the form

$$
\begin{array} { r } { \begin{array} { r } { \boxed { \Omega = \big ( ( i , j ) , ( i + 1 , j ) , ( i + 1 , j + 1 ) , ( i , j + 1 ) \big ) . } } \end{array} } \end{array}
$$

The $i -$ th component of $\sqsupset$ is the $i -$ th vertex of the rectangle, denoted by $\sqsupset ^ { i }$ . A point $( i , j ) \in \mathbb { X }$ is touched by a rectangle if it is a vertex of that rectangle. If $\mathbb { M } \subseteq \mathbb { X }$ , then $( i , j )$ is an interior point of $\mathbb { M }$ , if $\mathbb { M }$ contains all four rectangles that touch $( i , j )$ . We denote $\overline { { \mathbb { M } } }$ as the union of all rectangles touching interior points of $\mathbb { M }$ . A boundary point of $\mathbb { M }$ is a point in $\overline { { \mathbb { M } } }$ which is not an interior point. If $\mathbb { M } = \overline { { \mathbb { M } } }$ , we call $\mathbb { M }$ regular. int $\mathbb { M }$ is the set of the interior points of $\mathbb { M }$ , and $\partial \mathbb { M }$ is the set of boundary points.

The discrete first-order prolongation of $\mathbb { X } \times \mathbb { U }$ is defined by

$$
\mathbb { U } ^ { ( 1 ) } \equiv \bigl ( \mapsto ; u _ { i j } , u _ { i + 1 j } , u _ { i + 1 j + 1 } , u _ { i j + 1 } \bigr ) ,
$$

and the first order prolongation of the discrete map $\varphi : \mathbb { X }  \mathbb { U } ; \varphi ( i , j ) : = \varphi _ { i , j }$ by

$$
\begin{array} { r } { \mathrm { p r } ^ { 1 } \varphi \equiv \bigl ( \flat ; \varphi _ { i j } , \varphi _ { i + 1 j } , \varphi _ { i + 1 j + 1 } , \varphi _ { i j + 1 } \bigr ) . } \end{array}
$$

Corresponding to a discrete Lagrangian $\mathbb { L } : \mathbb { U } ^ { ( 1 ) }  R$ , we define the discrete functional

$$
\mathbb { S } ( \varphi ) = \sum _ { \Omega \subset \mathbb { M } } \mathbb { L } ( \mathrm { p r } ^ { 1 } \varphi ) \Delta x \Delta t = \sum _ { \Omega \subset \mathbb { M } } \mathbb { L } ( \bigtriangledown , \varphi _ { i j } , \varphi _ { i + 1 j } , \varphi _ { i + 1 j + 1 } , \varphi _ { i j + 1 } ) \Delta x \Delta t ,
$$

where $\Delta x$ and $\Delta t$ are the grid sizes in direction $x$ and $t$ , and $\mathbb { M }$ is a subset of $\mathbb { X }$ . In this chapter, only an equally spaced grid is considered.

Now for brevity of notations, let $\mathcal { M } = [ a , b ] \times [ c , d ]$ be a rectangular domain and consider a uniform rectangular subdivision

$$
\begin{array} { r l } & { a = x _ { 0 } < x _ { 1 } < \cdots < x _ { M - 1 } < x _ { M } = b , c = t _ { 0 } < t _ { 1 } < \cdots < t _ { N - 1 } < t _ { N } = d , } \\ & { x _ { i } = a + i \Delta x , \quad t _ { j } = c + j \Delta t , \quad i = 0 , 1 , \cdots , M , j = 0 , 1 , \cdots , N , } \\ & { M \Delta x = b - a , \quad N \Delta t = d - c . } \end{array}
$$

For autonomous Lagrangian and uniform rectangular subdivisions, the discrete action functional takes the form

$$
\mathbb { S } ( \varphi ) = \sum _ { i = 0 } ^ { M - 1 } \sum _ { j = 0 } ^ { N - 1 } \mathbb { L } \big ( \varphi _ { i j } , \varphi _ { i + 1 j } , \varphi _ { i + 1 j + 1 } , \varphi _ { i j + 1 } \big ) \Delta \boldsymbol { x } \Delta t .
$$

Using the discrete variational principle, we obtain the discrete Euler–Lagrange equation (variational integrator)

$$
\mathcal { D } _ { 1 } \mathbb { L } ^ { i j } + \mathcal { D } _ { 2 } \mathbb { L } ^ { i - 1 j } + \mathcal { D } _ { 3 } \mathbb { L } ^ { i - 1 j - 1 } + \mathcal { D } _ { 4 } \mathbb { L } ^ { i j - 1 } = 0 ,
$$

which satisfies the discrete multisymplectic form formula

$$
\sum _ { \substack { \Omega ; \Omega \cap \partial \mathbb { M } \neq \emptyset } } \left( \sum _ { l ; \Omega ^ { l } \in \partial \mathbb { M } } ( \mathrm { p r } ^ { 1 } \varphi ) ^ { \ast } \left( \mathrm { p r } ^ { 1 } \mathbb { V } _ { 1 } \bot \mathrm { p r } ^ { 1 } \mathbb { V } _ { 2 } \bot \Omega _ { \mathbb { L } } ^ { l } \right) \right) = 0 ,
$$

where $\Omega _ { \mathbb { L } } ^ { l } = \mathrm { d } \theta _ { \mathbb { L } } ^ { l }$ $( l = 1 , \cdots , 4 )$ and $\mathbb { V } _ { 1 }$ and $\mathbb { V } _ { 2 }$ are solutions of the linearized equation of (4.6). Now the discretizations of an autonomous Lagrangian $L ( \varphi , \varphi _ { x } , \varphi _ { t } )$ is considered

$$
\mathbb { L } ( \varphi _ { i j } , \varphi _ { i + 1 , j } , \varphi _ { i + 1 , j + 1 } , \varphi _ { i , j + 1 } ) = L \Big ( \bar { \varphi } _ { i j } , \frac { \varphi _ { i + 1 , j + \frac { 1 } { 2 } } - \varphi _ { i j + \frac { 1 } { 2 } } } { \Delta x } , \frac { \varphi _ { i + \frac { 1 } { 2 } j + 1 } - \varphi _ { i + \frac { 1 } { 2 } j } } { \Delta t } \Big ) ,
$$

where

$$
\begin{array} { l } { \displaystyle \bar { \varphi } _ { i j } = \frac { 1 } { 4 } \left( \varphi _ { i j } + \varphi _ { i + 1 j } + \varphi _ { i + 1 j + 1 } + \varphi _ { i j + 1 } \right) , } \\ { \displaystyle } \\ { \displaystyle \varphi _ { i j + \frac 1 2 } = \frac { 1 } { 2 } \left( \varphi _ { i j } + \varphi _ { i j + 1 } \right) , } \\ { \displaystyle \varphi _ { i + \frac 1 2 j + 1 } = \frac { 1 } { 2 } \left( \varphi _ { i j + 1 } + \varphi _ { i + 1 j + 1 } \right) } \end{array}
$$

etc. For the discrete Lagrangian, the discrete Euler–Lagrange equation (4.6) is a ninepoint variational integrator. The following results demonstrate the equivalence of variational integrators and multisymplectic integrators. Consider the sine-Gordon equation (3.3), then the Lagrangian is given by

$$
L ( u , u _ { x } , u _ { t } ) = \frac { 1 } { 2 } u _ { x } ^ { 2 } - \frac { 1 } { 2 } u _ { t } ^ { 2 } - \cos { ( u ) } .
$$

The discrete Euler–Lagrange equation (4.6) corresponding to (4.9) is just the ninepoint integrator (3.7). Consider the nonlinear Schrodinger equation (3.8), then the ¨ Lagrangian for (3.8) is given by

$$
L ( p , q , p _ { x } , q _ { x } , p _ { t } , q _ { t } ) = \frac { 1 } { 2 } \big [ p _ { x } ^ { 2 } + q _ { x } ^ { 2 } + p q _ { t } - q p _ { t } - V ( p ^ { 2 } + q ^ { 2 } ) \big ] .
$$

The discrete Euler–Lagrange equation (4.6) corresponding to (4.10) reads

$$
\begin{array} { r l } & { \mathfrak { i } \frac { \psi _ { [ i ] } ^ { j + 1 } - \psi _ { [ i ] } ^ { j - 1 } } { 2 \Delta t } + \frac { \psi _ { i + 1 } ^ { j + \frac { 1 } { 2 } } + \psi _ { i + 1 } ^ { j - \frac { 1 } { 2 } } - 2 \psi _ { i } ^ { j + \frac { 1 } { 2 } } - 2 \psi _ { i } ^ { j - \frac { 1 } { 2 } } + \psi _ { i - 1 } ^ { j + \frac { 1 } { 2 } } + \psi _ { i - 1 } ^ { j - \frac { 1 } { 2 } } } { \Delta x ^ { 2 } } } \\ & { \quad + \frac { 1 } { 4 } G _ { i , j } + \frac { 1 } { 4 } G _ { i , j - 1 } = 0 . } \end{array}
$$

The integrator (4.11) is equivalent to the integrator (3.10), since replacing $j$ by $j - 1$ in (3.10) and adding the resulting equation to (3.10) leads to (4.11) (see [CQ03] ).

# 16.5 Some Generalizations

In this section, some generalizations based on the multisymplectic geometry and multisymplectic Hamiltonian systems are presented.

# 1. Multisymplectic Fourier pseudospectral methods

On Fourier space, multisymplectic Fourier pseudospectral methods were considered in [BR01b] . Now, we discuss these methods on real space [CQ01a] and take the nonlinear Schrodinger equation as an example. Applying the Fourier pseudospectral method to ¨ the multisymplectic system (3.9) and using the notations

$$
\begin{array} { l } { { \mathbf { p } = ( p _ { 0 } , \cdots , p _ { N - 1 } ) ^ { \mathrm { T } } , \quad \mathbf { q } = ( q _ { 0 } , \cdots . q _ { N - 1 } ) ^ { \mathrm { T } } , } } \\ { { \mathbf { v } = ( v _ { 0 } , \cdots , v _ { N - 1 } ) ^ { \mathrm { T } } , \quad \mathbf { w } = ( w _ { 0 } , \cdots . w _ { N - 1 } ) ^ { \mathrm { T } } , } } \end{array}
$$

it follows

$$
\begin{array} { c } { { \frac { \mathrm { d } q _ { j } } { \mathrm { d } t } - ( D _ { 1 } { \mathbf v } ) _ { j } = 2 ( p _ { j } ^ { 2 } + q _ { j } ^ { 2 } ) p _ { j } , } } \\ { { \displaystyle - \frac { \mathrm { d } p _ { j } } { \mathrm { d } t } - ( D _ { 1 } { \mathbf w } ) _ { j } = 2 ( p _ { j } ^ { 2 } + q _ { j } ^ { 2 } ) q _ { j } , } } \\ { { ( D _ { 1 } { \mathbf p } ) _ { j } = v _ { j } , } } \\ { { ( D _ { 1 } { \mathbf q } ) _ { j } = w _ { j } , } } \end{array}
$$

where $j = 0 , 1 , \cdots , N - 1$ and $D _ { 1 }$ is the first order spectral differentiation matrix.

The Fourier pseudospectral semidiscretization (5.1) has $N$ semidiscrete multisymplectic conservation laws

$$
\frac { \mathrm { d } } { \mathrm { d } t } \omega _ { j } + \sum _ { k = 0 } ^ { N - 1 } ( D _ { 1 } ) _ { j , k } \kappa _ { j k } = 0 , \quad j = 0 , 1 , \cdots , N - 1 ,
$$

where

$$
\omega _ { j } = \frac { 1 } { 2 } ( \mathbf { d } z _ { j } \wedge M z _ { j } ) , \quad \kappa _ { j k } = \mathbf { d } z _ { j } \wedge K \mathbf { d } z _ { k } ,
$$

and $z _ { j } = ( p _ { j } , q _ { j } , v _ { j } , w _ { j } ) ^ { \mathrm { T } } ( j = 0 , 1 , \cdots , N - 1 ) .$

# 2. Nonconservative multisymplectic Hamiltonian systems

Nonconservative multisymplectic Hamiltonian systems refer to those depending on

the independent variables explicitly. Such an example is the Schrodinger equation ¨ with variable coefficients[HLHKA06] . Another example is the three-dimensional scalar seismic wave equation[Che04b,Che06a,Che07a,Che07b,Che04a]

$$
\nabla ^ { 2 } u - \frac { 1 } { c ( x , y , z ) ^ { 2 } } u _ { t t } = 0 ,
$$

where $\nabla ^ { 2 } u = u _ { x x } + u _ { y y } + u _ { z z }$ and $c ( x , y , z )$ is the wave velocity.

Introducing the new variables

$$
v = \frac { 1 } { c ( x , y , z ) } u _ { t } , \quad w = u _ { x } , \quad p = u _ { y } , \quad q = u _ { z } ,
$$

Equation (5.3) can be rewritten as

$$
M ( x , y , z ) \mathcal { Z } _ { t } + K \mathcal { Z } _ { x } + L \mathcal { Z } _ { y } + N \mathcal { Z } _ { z } = \nabla z \mathcal { S } ( \mathcal { Z } ) ,
$$

where $\mathcal { Z } = ( u , v , w , p , q ) ^ { \mathrm { T } }$ , $\mathcal { S } ( \mathcal { Z } ) = \frac { 1 } { 2 } \big ( v ^ { 2 } - w ^ { 2 } - p ^ { 2 } - q ^ { 2 } \big )$ and

$$
M ( x , y , z ) = \left( \begin{array} { c c c c c } { { 0 } } & { { - \frac { 1 } { c ( x , y , z ) } } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \frac { 1 } { c ( x , y , z ) } } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) ,
$$

$$
K = \left( \begin{array} { c c c c c } { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) ,
$$

$$
L = \left( \begin{array} { c c c c c } { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right) , \quad N = \left( \begin{array} { c c c c c } { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right) .
$$

The corresponding four presymplectic forms associated to the time direction and three space directions are respectively:

$$
\begin{array} { r l r } & { \omega = \displaystyle \frac { 1 } { 2 } \mathrm { d } \mathcal { Z } \wedge M ( x , y , z ) \mathrm { d } \mathcal { Z } , } & { \kappa _ { x } = \frac { 1 } { 2 } \mathrm { d } \mathcal { Z } \wedge K \mathrm { d } \mathcal { Z } , } \\ & { \kappa _ { y } = \displaystyle \frac { 1 } { 2 } \mathrm { d } \mathcal { Z } \wedge L \mathrm { d } \mathcal { Z } , } & { \kappa _ { z } = \displaystyle \frac { 1 } { 2 } \mathrm { d } \mathcal { Z } \wedge N \mathrm { d } \mathcal { Z } . } \end{array}
$$

Note that the time direction presymplectic form $\omega$ depends on the space variables $( x , y , z )$ . We can also obtain the corresponding multisymplectic integrators[Che06a] .

# 3. Construction of multisymplectic integrators for modified equations

Consider the linear wave equation

$$
u _ { t t } = u _ { x x } .
$$

Based on the two Hamiltonian formulations of (5.6) and using the hyperbolic functions, various symplectic integrators were constructed $\mathrm { i n } ^ { [ Q Z 9 3 ] }$ . By deriving the corresponding Lagrangians and their discrete counterparts, these symplectic integrators were proved to be multisymplectic integrators for the modified versions of (5.6) $\mathrm { i n } ^ { [ \mathrm { S Q 0 0 } ] }$ .

Let us present an example. Using hyperbolic function $\operatorname { t a n h } ( x )$ , we can obtain a symplectic integrator for (5.6) of accuracy $\mathcal { O } ( \Delta t ^ { 2 s } + \Delta x ^ { 2 m } )$ :

$$
u _ { i } ^ { j + 1 } - 2 u _ { i } ^ { j } + u _ { i } ^ { j - 1 } = \operatorname { t a n h } \Big ( 2 s , \frac { \Delta t } { 2 } \Big ) \operatorname { t a n h } \Big ( 2 s , \frac { \Delta t } { 2 } \Delta ( 2 m ) \Big ) \big ( u _ { i } ^ { j + 1 } - 2 u _ { i } ^ { j } + u _ { i } ^ { j - 1 } \Big ) \Dot { u } _ { i } ^ { j + 1 } + 2 \Dot { u } _ { i } ^ { j } + { \Dot { u } _ { i } ^ { j } } \Dot { u } _ { i } ^ { j + 1 } .
$$

where

$$
\Delta \left( 2 m \right) = \nabla _ { + } \nabla _ { - } \sum _ { j = 0 } ^ { m - 1 } ( - 1 ) ^ { j } \beta _ { j } \Bigl ( \frac { \Delta x ^ { 2 } \nabla _ { + } \nabla _ { - } } { 4 } \Bigr ) ^ { j } ,
$$

where

$$
\beta _ { j } = \frac { [ ( j ! ) ^ { 2 } 2 ^ { 2 j } ] } { [ ( 2 j + 1 ) ! ( j + 1 ) ] }
$$

and $\nabla _ { + }$ and $\nabla _ { - }$ are forward and backward difference operators respectively.

For $m = 2$ and $s = 2$ , the integrator (5.7) is a multisymplectic integrator of the modified equation

$$
u _ { t t } = u _ { x x } - \frac { \Delta t ^ { 2 } } { 6 } u _ { x x x x } - \frac { \Delta t ^ { 4 } } { 1 4 4 } u _ { x x x x x x } .
$$

For other hyperbolic functions, we can obtain similar results.

# 4. Multisymplectic Birkhoffian systems

The multisymplectic Hamiltonian system can be generalized to include dissipation terms. This generalization leads to the following multisymplectic Birkhoffian system

$$
M ( t , x , z ) z _ { t } + K ( t , x , z ) z _ { x } = \nabla _ { z } B ( t , x , z ) + \frac { \partial F } { \partial t } + \frac { \partial G } { \partial x } ,
$$

where $\boldsymbol { z } = ( z _ { 1 } , \cdots , z _ { n } ) ^ { \mathrm { T } }$ , $F = ( f _ { 1 } , \cdots , f _ { n } ) ^ { \mathrm { T } }$ , $G = ( g _ { 1 } , \cdots , g _ { n } ) ^ { \mathrm { T } }$ and $M = ( m _ { i j } )$ and $K = ( k _ { i j } )$ are two antisymmetric matrices with entries respectively:

$$
m _ { i j } = \frac { \partial f _ { j } } { \partial z _ { i } } - \frac { \partial f _ { i } } { \partial z _ { j } } , \quad k _ { i j } = \frac { \partial g _ { j } } { \partial z _ { i } } - \frac { \partial g _ { i } } { \partial z _ { j } } .
$$

The system (5.9) satisfies the following multisymplectic dissipation law:

$$
\frac { \mathrm { d } } { \mathrm { d } t } \bigg ( \frac 1 2 \mathrm { d } z \wedge M \mathrm { d } z \bigg ) + \frac { \mathrm { d } } { \mathrm { d } x } \bigg ( \frac 1 2 \mathrm { d } z \wedge K \mathrm { d } z \bigg ) = 0 .
$$

Let us present an example[SQ03,SQWR08] . Consider the equation describing the linear damped string:

$$
u _ { t t } - u _ { x x } + u + \alpha u _ { t } + \beta u _ { x } = 0 .
$$

Introducing new variables $p = u _ { t }$ and $q = u _ { x }$ , the Equation (5.11) can be cast into the form of (5.9) with

$$
M = \left( \begin{array} { c c c } { 0 } & { \mathrm { e } ^ { \alpha t - \beta x } } & { 0 } \\ { - \mathrm { e } ^ { \alpha t - \beta x } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) , \quad K = \left( \begin{array} { c c c } { 0 } & { 0 } & { - \mathrm { e } ^ { \alpha t - \beta x } } \\ { 0 } & { 0 } & { 0 } \\ { \mathrm { e } ^ { \alpha t - \beta x } } & { 0 } & { 0 } \end{array} \right) ,
$$

and

$$
\begin{array} { r } { \boldsymbol { z } = ( \boldsymbol { u } , \boldsymbol { p } , \boldsymbol { q } ) ^ { \mathrm { T } } , \quad \boldsymbol { B } = - \frac { 1 } { 2 } \mathrm { e } ^ { \alpha t - \beta x } ( \boldsymbol { u } ^ { 2 } + \boldsymbol { p } ^ { 2 } - \boldsymbol { q } ^ { 2 } + \alpha \boldsymbol { u } \boldsymbol { p } + \beta \boldsymbol { u } \boldsymbol { q } ) , } \\ { \boldsymbol { F } = \left( - \frac { 1 } { 2 } \mathrm { e } ^ { \alpha t - \beta x } \boldsymbol { p } , \frac { 1 } { 2 } \mathrm { e } ^ { \alpha t - \beta x } \boldsymbol { u } , 0 \right) ^ { \mathrm { T } } , \quad \boldsymbol { G } = \left( \frac { 1 } { 2 } \mathrm { e } ^ { \alpha t - \beta x } \boldsymbol { q } , 0 , - \frac { 1 } { 2 } \mathrm { e } ^ { \alpha t - \beta x } \right) ^ { \mathrm { T } } . } \end{array}
$$

Similarly, we can develop multisymplectic dissipation integrators for the system (5.9) which preserve a discrete version of the multisymplectic dissipation law (5.10).

# 5. Differential complex, methods and multisymplectic structure

Differential complexes have come to play an increasingly important role in numerical analysis recently. In particular, discrete differential complexes are crucial in designing stable finite element schemes[Arn02] . With regard to discrete differential forms, a generic Hodge operator was introduced in[Hip02] . It was shown that most finite element schemes emerge as its specializations. The connection between Veselov discrete mechanics and finite element methods was first suggested $\mathrm { i n } ^ { \mathrm { [ M P S 9 8 ] } }$ . Symplectic and multisymplectic structures in simple finite element methods are explored $\mathrm { i n } ^ { [ \mathrm { G j L K 0 4 } ] }$ . It will be of particular significance to study the multisymplectic structure for the finite element methods by using discrete differential complexes and in particular, discrete Hodge operators[STMM07] . We will explore this issue in the future.

# Bibliography

[AM04] U.M. Ascher and R.I. McLachlan: Multisymplectic box schemes and the Korteweg-de Vries equation. Appl. Numer. Math., 39:55–269, (2004).   
[Arn02] D.N. Arnold: Differential complexes and numerical stability. Plenary address delivered at ICM 2002. Beijing, China, (2002).   
[BR01a] T. J. Bridges and S. Reich: Multi-symplectic integrators: numerical schemes for Hamiltonian PDEs that conserve symplecticity. Physics Letters A, 284:184–193, (2001).   
[BR01b] T.J. Bridges and S. Reich: Multi-symplectic spectral discretizations for the Zakharov-Kuznetsov and shallow water equations. Physica D, 152:491–504, (2001).   
[BR06] T. J. Bridges and S. Reich: Numerical methods for Hamiltonian PDEs. J. Phys. A: Math. Gen., 39:5287–5320, (2006).   
[Bri97] T. J. Bridges: Multi-symplectic structures and wave propagation. Math. Proc. Cam. Phil. Soc., 121:147–190, (1997).   
[Bri06] T. J. Bridges: Canonical multisymplectic structure on the total exterior algebra bundle. Proc. R. Soc. Lond. A, 462:1531–1551, (2006).   
[CGW03] J. B. Chen, H.Y. Guo, and K. Wu: Total variation in Hamiltonian formalism and symplectic-energy integrators. J. of Math. Phys., 44:1688–1702, (2003).   
[Che02] J. B. Chen: Total variation in discrete multisymplectic field theory and multisymplectic energy momentum integrators. Letters in Mathematical Physics, 51:63–73, (2002).   
[Che03] J. B. Chen: Multisymplectic geometry, local conservation laws and a multisymplectic integrator for the Zakharov–Kuznetsov equation. Letters in Mathematical Physics, 63:115– 124, (2003).   
[Che04a] J. B. Chen: Multisymplectic geometry for the seismic wave equation. Commun.Theor. Phys., 41:561–566, (2004).   
[Che04b] J. B. Chen: Multisymplectic Hamiltonian formulation for a one-way seismic wave equation of high order approximation. Chin Phys. Lett., 21:37–39, (2004).   
[Che05a] J. B. Chen: Multisymplectic geometry, local conservation laws and Fourier pseudospectral discretization for the ”good” Boussinesq equation. Applied Mathematics and Computation, 161:55–67, (2005).   
[Che05b] J. B. Chen: A multisymplectic integrator for the periodic nonlinear Schrodinger ¨ equation. Applied Mathematics and Computation, 170:1394–1417, (2005).   
[Che05c] J. B. Chen: Variational formulation for multisymplectic Hamiltonian systems. Letters in Mathematical Physics, 71:243–253, (2005).   
[Che06a] J. B. Chen: A multisymplectic variational formulation for the nonlinear elastic wave equation. Chin Phys. Lett., 23(2):320–323, (2006).   
[Che06b] J. B. Chen: Symplectic and multisymplectic Fourier pseudospectral discretization for the Klein-Gordon equation. Letters in Mathematical Physics, 75:293–305, (2006).   
[Che07a] J. B. Chen: High order time discretization in seismic modeling. Geophysics, 72(5):SM115–SM122, (2007).   
[Che07b] J. B. Chen: Modeling the scalar wave equation with Nystron methods. ¨ Geophysics, 71(5):T158, (2007).   
[Che07c] J. B. Chen: A multisymplectic pseudospectral method for seismic modeling. Applied Mathematics and Computation, 186:1612–1616, (2007).   
[CQ01a] nonlinear Schrodinger equation. ¨ Electronic Transactions on Numerical Analysis, 12:193– 204, (2001).   
[CQ02] J.-B. Chen and M. Z. Qin. A multisymplectic variational integrator for the nonlinear Schrodinger equation. ¨ Numer. Meth. Part. Diff. Eq., 18:523–536, 2002.   
[CQ03] J. B. Chen and M. Z. Qin: Multisymplectic composition integrators of high order. J. Comput. Math., 21(5):647–656, (2003).   
[CQT02] J. B. Chen, M. Z. Qin, and Y. F. Tang: Symplectic and multisymplectic methods for the nonlinear Schrodinger equation. ¨ Computers Math. Applic., 43:1095–1106, (2002).   
[CWQ09] J. Cai, Y. S. Wang, and Z. H. Qiao: Multisymplectic Preissman scheme for the time-domain Maxwell’s equations. J. of Math. Phys., 50:033510, (2009).   
[CYQ09] J. X. Cai, Y.S.Wang, and Z.H. Qiao: Multisymplectic Preissman scheme for the time-domain Maxwell’s equations. J. of Math. Phys., 50:033510, (2009).   
[CYWB06] J. X. Cai, Y.S.Wang, B. Wang, and B.Jiang: New multisymplectic self-adjoint scheme and its composition for time-domain Maxwell’s equations. J. of Math. Phys., 47:123508, (2006).   
[Dah07] M. L. Dahlby: Geometrical integration of nonlinear wave equations. Master’s thesis, Norwegian University, NTNU, Trondheim, (2007).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[FQ87] K. Feng and M. Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[GAR73] P.L. GARCIA: The Poincare–Cartan invariant in the calculus of variations symposia mathematica. In in Convegno di Geometria Simplettica e Fisica Mathmatica XIV, pages 219–243. Academic Press, London, (1973).   
[GjLK04] H.Y. Guo, X.M. Ji, Y.Q. Li, and K.Wu: symplectic, multisymplectic structurepreserving in simple finite element method, Preprint arXiv: hep-th/0104151. (2004).   
[Hip02] R. Hiptmair: Finite elements in computational electromagnetism. Acta Numerica, 11:237–339, (2002).   
[HL04] J. Hong and C. Li: Multi-symplectic Runge–Kutta methods for nonlinear Dirac equations. J. of Comp. Phys., 211:448–472, (2004).   
[HLHKA06] J. L. Hong, Y. Liu, H.Munthe-Kass, and Zanna A: On a multisymplectic scheme for Schrodinger equations with variable coefficients. ¨ Appl. Numer. Math., 56:816–843, (2006).   
[HZQ03] L. Y Huang, W. P. Zeng, and M.Z. Qin: A new multi-symplectic scheme for nonlinear “good” Boussinesq equation. J. Comput. Math., 21:703–714, (2003).   
[JYJ06] B. Jiang, Y.S.Wang, and Cai J.X: New multisymplectic scheme for generalized Kadomtsev-Petviashvili equation. J. of Math. Phys., 47:083503, (2006).   
[KLX06] L. H. Kong, R. X. Liu, and Z.L. Xu: Numerical simulation interaction between Schrodinger equation, and Klein–Gorden field by multi-symplecticic methods. ¨ Applied Mathematics and Computation, 181:342–350, (2006).   
[Lag88] J. L. Lagrange: Mecanique Analytique ´ Blanchard, Paris, 5th edition, vol. 1, (1965).   
[Lee82] T. D. Lee: Can time be a discrete dynamical variable? Phys.Lett.B, 122:217–220, (1982).   
[Lee87] T. D. Lee: Difference equations and conservation laws. J. Stat. Phys., 46:843–860, (1987).   
[LQ88] C.W. Li and M.Z. Qin: A symplectic difference scheme for the infinite dimensional Hamiltonian system. J. Comput. Appl. Math, 6:164–174, (1988).   
[LQ02] T. T. Liu and M. Z. Qin: Multisymplectic geometry and multisymplectic Preissman scheme for the KP equation. J. of Math. Phys., 43:4060–4077, (2002).   
[LQHD07] X. S. Liu, Y.Y. Qi, J. F. He, and P. Z. Ding: Recent progress in symplectic algorithms for use in quantum systems. Communications in Computational Physics, 2(1):1–53, (2007).   
[MM05] K.W. Morton and D.F. Mayers: Numerical Solution of Partial Differential Equations: an introduction. Cambridge University Press, Cambridge, Second edition, (2005).   
[MPS98] J. E. Marsden, G.P. Patrick, and S. Shloller: Multi-symplectic geometry, variational integrators, and nonlinear PDEs. Communications in Mathematical Physics, 199:351–395, (1998).   
[MPSM01] J. E. Marsden, S. Pekarsky, S. Shkoller, and M.West: Variational methods, multisymplectic geometry and continuum mechanics. J.Geom. Phys., 38:253–284, (2001).   
[Olv86] P.J. Olver: Applications of Lie Groups to Differential Equations. Springer, New York, (1986).   
[Qin87] M. Z. Qin: A symplectic schemes for the Hamiltonian equations. J. Comput. Math., 5:203–209, (1987).   
[Qin90] M. Z. Qin: Multi-stage symplectic schemes of two kinds of Hamiltonian systems of wave equations. Computers Math. Applic., 19:51–62, (1990).   
[Qin97a] M. Z. Qin: A symplectic schemes for the PDEs. AMS/IP studies in Advanced Mathemateics, 5:349–354, (1997).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[QZ93] M. Z. Qin and W. J. Zhu: Construction of symplectic scheme for wave equation via hyperbolic functions $s i n h ( x ) , c o s h ( x )$ and tanh $\dot { \left( x \right) }$ . Computers Math. Applic., 26:1–11, (1993).   
[Rei00] S. Reich: Multi-symplectic Runge–Kutta collocation methods for Hamiltonian wave equations. J. of Comp. Phys., 157:473–499, (2000).   
[SHQ06] J. Q. Sun, W. Hua, and M. Z. Qin: New conservation scheme for the nonlinear Schrodinger system. Applied Mathematics and Computation, 177:446–451, (2006).   
[SMM04] J. Q. Sun, Z. Q. Ma, and M. Z. Qin: RKMK method of solving non-damping LL equations for ferromagnet chain equations. Applied Mathematics and Computation, 157:407–424, (2004).   
[SMQ06] J. Q. Sun, Z. Q. Ma, and M. Z. Qin: Simulation of envelope Rossby solution in pair of cubic Schrodinger equations. Applied Mathematics and Computation, 183:946–952, (2006).   
[SNW92] J.C. Simo, N.Tarnow, and K.K. Wong: Exact energy-momentum conserving algorithms and symplectic schemes for nonlinear dynamics. Comput. Methods Appl. Mech. Engrg., 100:63–116, (1992).   
[SQ00] Y. J. Sun and M.Z. Qin: Construction of multisymplectic schemes of any finite order for modified wave equations. J. of Math. Phys., 41:7854–7868, (2000).   
[SQ01] H. L. Su and M. Z. Qin: Multisymplectic Birkhoffian structure for PDEs with dissipation terms, arxiv:math.na 0302299, (2001).   
[SQ03] H. Su and M. Z. Qin: Symplectic schemes for Birkhoffian system. Technical Report arXiv: math-ph/0301001, (2003).   
[SQ04] Y. J. Sun and M. Z. Qin: A multi-symplectic schemes for RLW eqution. J. Comput. Math., 22:611–621, (2004).   
[SQ05] H. Su and M. Z. Qin: Multisymplectic geometry method for Maxwell’s equations and multisymplectic scheme. Technical Report arXiv. org math-ph/0302058, (2005).   
[SQL06] J. Q. Sun, M.Z. Qin, and T.T. Liu: Total variation and multisymplectic structure for the CNLS system. Commun.Theor. Phys., 46(2):966–975, (2006).   
[SQS07] H. L. Su, M.Z. Qin, and R. Scherer: Multisymplectic geometry method for Maxwell’s equations and multisymplectic scheme. Inter. J of Pure and Applied Math, 34(1):1–17, (2007).   
[SQWD09] J. Q. Sun, M. Z. Qin, H. Wei, and D. G. Dong: Numerical simulation of collision behavior of optical solitons in birefingent fibres. Commun Nonlinear Science and Numerical Simulation, 14:1259–1266, (2009).   
[SQWR08] H. L. Su, M. Z. Qin, Y. S. Wang, and R. Scherer: Multisymplectic Birkhoffian structure for PDEs with dissipation terms. Preprint No:2, Karlsruhe University, (2008).   
[STMM07] A. Stern, Y. Tong, M.Desbrun, and J.E. Marsden: Electomagnetism with variational integration and discretedifferential forms, arXiv:0707.4470v2, (2007).   
[Str68] G. Strang: On the construction and comparison of difference schemes. SIAM J. Numer. Anal., 5:506–517, (1968).   
[Str96] M. Struwe: Variational Methods Application to nonlinear PDEs and Hamiltonian systems, volume 34 of A Series of Modern Surveys in Mathematics. Springer-Verlag, Berlin, Second edition, (1996).   
[Suz92] M. Suzuki: General theory of higher-order decomposition of exponential operators and symplectic integrators. Physics Letters A, 165:387–395, (1992).   
[TM03] Y.M. Tian and M.Z.Qin: Explicit symplectic schemes for investigating the evolution of vortices in a rovating Bose–Einstein condensate. Comput. Phys. Comm., 155:132–143, (2003).   
[TMZM08] Y.M. Tian, M.Z.Qin, Y. M. Zhang, and T. Ma: The multisymplectic method for Gross–Pitaevskii equation. Comput. Phys. Comm., 176:449–458, (2008).   
[WHT96] J. Wisdom, M. Holman, and J. Touma: Symplectic Correctors. In Jerrold E. Marsden, George W. Patrick, and William F. Shadwick, editors, Integration Algorithms and Classical Mechanics, volume 10 of Fields Institute Communications, pages 217–244. Fields Institute, American Mathematical Society, July (1996).   
[WM01] Y. S. Wang and M. Z.Qin: Multisymplectic geometry and multisymplectic scheme for the nonlinear Klein–Gordon equation. J. of Phys.soc. of Japan, 70:653–661, (2001).   
[WWQ08] Y.S. Wang, B. Wang, and M. Z. Qin: Local structure-preserving algorithms for partial differential equation. Science in China (series A), 51(11):2115–2136, (2008).   
[Yos90] H. Yoshida: Construction of higher order symplectic integrators. Physics Letters A, 150:262–268, (1990).   
[Zha91b] M. Q. Zhang: Explicit unitary schemes to solve quantum operator equations of motion. J. Stat. Phys., 65(3/4), (1991).   
[Zha93a] M. Q. Zhang: Algorithms that preserve the volume amplification factor for linear systems. Appl. Math. Lett., 6(3):59–61, (1993).   
[Zha93b] M. Q. Zhang: Computation of n-body problem by 2-body problems. Physics Letters A, 197:255–260, (1993).   
[ZQ93a] M. Q. Zhang and M. Z. Qin: Explicit symplectic schemes to solve vortex systems. Comp. & Math. with Applic., 26(5):51, (1993).   
[ZQ93b] W. Zhu and M. Qin: Application of higer order self-adjoint schemes of PDEs. Computers Math. Applic., 25(12):31–38, (1993).   
[ZQ00] P. F. Zhao and M. Z. Qin: Multisymplectic geometry and multisymplectic Preissman scheme for the KdV equation. J. Phys. A: Math. Gen., 33:3613–3626, (2000).   
[ZW99] H.P. Zhu and J.K. Wu: Generalized canonical transformations and symplectic algorithm of the autonomous Birkhoffian systems. Progr. Natur. Sci., 9:820–828, (1999).   
[ZzT96] W. Zhu, X. Zhao, and Y. Tang: Numerical methods with a high order of accuracy applied in the quantum system. J. Chem. Phys., 104(6):2275–2286, (1996).

# Symbol

# Description

Matrix $A = \{ a _ { i j } \in M ( n ) \}$   
conjugate transpose of $A$   
transpose of $A$   
$J$ -orthogonal complement of $A$   
orthogonal complement of $A$   
smooth atlas   
adjoint representation   
coadjoint representation   
adjoint vector field   
coadjoint vector field   
take $a$ as the center of circle, $r$ is the radius ball space consist of all exact $k$ -form   
set of all $k$ -boundaries   
Betti number   
order conditions of Butcher.   
the complex numbers   
complex vector space of complex $n$ -vector   
space of $k$ -times differentiable functions   
space of smooth functions   
Casimir function   
$k$ -dimensional chain on $M$   
structure constant   
exterior derivative, exterior differential operator basis differential 1-form   
total differential   
determinant of matrix $A$   
divergence   
order of form (order of map) (order of polynomial) Euler step-transient operator   
identity element of group   
exponential function of $x$   
basis, symplectic basis   
phase of flow with vector field $a$   
exponential map   
differential element of function $f$   
Symbol   
$\begin{array} { r l } & { \frac { 1 } { \mathrm { d } t } = \frac { \eta } { \epsilon ^ { 2 } } } \\ & { + \frac { \eta } { \epsilon ^ { 2 } } } \\ & { + \frac { \eta } { \epsilon } } \\ & { \frac { 1 } { \mathrm { d } t } } \\ & { \frac { 1 } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } \eta } { \epsilon } } \\ & { \frac { \mathrm { d } \eta } { \epsilon } } \\ & { \frac { \mathrm { d } \eta } { \epsilon } } \\ & { \frac { \mathrm { d } \eta } { \epsilon } } \\ & { \frac { \mathrm { d } \eta } { \epsilon } } \\ & { \frac { \partial \theta } { \partial t } } \end{array} \qquad \mathrm { ~ d } \qquad \epsilon \in \mathcal { P } \mathrm { R } \times \mathcal { E } = \left[ \begin{array} { c } { \epsilon } \\ { \epsilon _ { 1 } } \\ { \epsilon _ { 2 } } \\ { \epsilon _ { 3 } } \\ { \epsilon _ { 3 } } \\ { \epsilon _ { 4 } } \\ { \epsilon _ { 5 } } \\ { \epsilon _ { 5 } } \end{array} \right] ,$ )   
$C _ { j k } ^ { i }$   
d   
${ \mathrm { d } } x ^ { i }$   
D   
det $A$   
div   
$\deg \omega \ ( \deg f ) ( \deg P ( x ) )$   
$E ^ { \tau }$   
$e$   
$\mathbf { e } ^ { x }$   
$e _ { i } , \{ e _ { i } , f _ { j } \}$   
$e _ { a } ^ { t }$   
exp, Exp   
$F ( t ) f$

# Symbol

$\mathbf { F }$ $\mathbf { F } ^ { n }$ $f _ { \ast p }$ $\mathcal { F } ( \mathbf { R } ^ { n } )$ $g ^ { k } ( M )$ $G$   
G2n,k   
g   
g∗   
Gl(n), Gl(n, R), Gl(n, C)   
gl(n)   
grad   
HK (M, R)(HK (M, R))   
H(p, q), H(z)   
i   
$i _ { X }$ ,   
$I$   
$I _ { n } , I _ { 2 n }$ $\begin{array} { r l } & { \mathrm { d } \overline { { \mathbf { u } } } ^ { \mathrm { ~ H ~ } } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } } \end{array}$   
Rnp , Rnqn $r ( t )$ $S$ $h , s$   
Description   
a field (usually $\mathbf { R }$ or C)   
vector space (over $\mathbf { F }$ ) of $n$ -vectors   
differential of the map $f$ in the $p$ place   
a class of all differentiable function on $\mathbf { R } ^ { n }$   
set of all $k$ -differential form on $M$   
group, Lie group   
$M ( 2 n , k )$ nonsingular equivalent class   
Lie algebra   
dual to the Lie algebra   
linear group on $\mathbf { R } ^ { n } , ( \mathbf { C } ^ { n } )$   
Lie algebra of $n \times n$ matrix   
gradient   
$k$ -th cohomology (homology) group on $M$   
Hamiltonian function   
including map   
contraction, interior product   
identity map   
identity matrix, standard Euclidean structure   
identity   
image of map $L$   
momentum map   
symplectic structure   
$\ddot { J } _ { 4 n }$ -symplectic structure   
$K$ -symplectic structure   
kernel of mapping $L$   
variation of $L$   
vector field $Y$ , differential form $\omega$ of Lie derivative   
manifold   
set of all real matrix with $n$ -row and $m$ -column   
set of all complex matrix with $n$ -row and $m$ -column   
set of all real matrix of order $n \times n$ on $\mathbf { R } ^ { \mathbf { n } }$   
set of all complex matrix of order $n \times n$ on $\mathbf { C } ^ { \mathbf { n } }$   
set of all matrix of order $n \times n$ on $\mathbf { F } ^ { \mathbf { n } }$   
orthogonal group, orthogonal Lie algebra   
zero matrix   
coordinate in momentum space   
coordinate in configuration space   
order of $p$   
real number   
$n$ -dimensional real vector space   
momentum space, configuration space in $\mathbf { R } ^ { n }$   
real projection space   
order of $t$ -tree   
symplectic transformation, $S$ -transformation   
step of time

# Symbol

# Description

$S L ( n ) , S L ( n , \mathbf { R } ) , S L ( n , \mathbf { C } )$   
$s l ( n )$   
$S O ( n )$   
$s o ( n )$   
$S p ( 2 n )$   
$s p ( 2 n )$   
$C S p ( 2 n )$   
$S p ( 0 )$   
$S p ( \mathrm { I } )$   
$S p ( \mathrm { I I } )$   
$\begin{array} { r l } & { \mathrm { S y s ~ ( 1 ) } } \\ & { \mathrm { S y s ~ ( 2 ) } } \\ & { \mathrm { S y s ~ ( 3 ) } } \\ & { \mathrm { S y s ~ ( 4 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 6 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \\ & { \mathrm { S y s ~ ( 5 ) } } \end{array}$ iff   
$\begin{array} { r l } & { V _ { \mathrm { { e } } } ^ { \prime } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \\ & { \times \sqrt { \pi } } \end{array}  ,$   
π−1(x) = T Rn   
special linear group, (real), (complex)   
Lie algebra of special linear group   
special orthogonal group   
Lie algebra of special orthogonal group   
symplectic group, symplectic matrix   
symplectic algebra, infinitesimal symplectic matrix   
conformal symplectic group   
0-class of symplectic matrix   
I-class of symplectic matrix   
II-class of symplectic matrix   
III-class of symplectic matrix   
symplectic diffeomorphism   
tangent bundle   
tangent space in place $x$   
cotangent bundle   
cotangent space in place of $x$   
symmetric group   
vector in $\mathbf { R } ^ { n }$ space   
local coordinate   
vector space   
vector field in place $p$ on manifold   
first, second, order derivative at $x$   
$x$ vector, coordinate component   
$y$ vector, coordinate component   
set of all tangent vector on $M$   
Hamiltonian vector field   
set of all smooth vector field on $R ^ { n }$

Darboux transformation inverse of Darboux transformation

variational derivative, codifferential operator   
symmetry of $t$ -tree   
density of $t$ -tree   
Kronecker symbol   
essential different labelings   
graphic of $f$   
step size of time   
step size of apace   
differential 1-form   
exterior of differential 1-form   
projection T Rn to Rn   
fiber in point $x$   
Symbol   
$\varphi ^ { * } \omega$ $\left( \varphi _ { * } \omega \right)$   
$\varphi ^ { \ast } f$ $( \varphi _ { * } f )$   
$\varphi ^ { * } Y$ $( \varphi _ { * } Y )$   
$\times$   
$\wedge$   
$\Lambda ^ { k } ( \mathbf { R } ^ { n } )$   
$\Lambda _ { n }$   
$\Lambda _ { n } ( K )$   
$f \top Z$   
$f \top _ { p } Z$   
$\Omega$   
$\Omega ^ { \# }$   
Ωb   
$\Omega ^ { k } ( { \bf R } ^ { n } ) , \Omega ^ { 0 } ( { \bf R } ^ { n } ) = C ^ { \infty } ( { \bf R } ^ { n } )$   
$\frac { \partial } { \partial x ^ { I } }$ or $\partial x ^ { i }$   
$\partial$   
$\begin{array} { r l } & { \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \\ & { \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \\ & { \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \\ & { \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \\ & { \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \\ & { - \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \\ & { \frac { 1 } { 2 } \times \mathcal { S } _ { \beta } ^ { \ast } } \end{array}$   
  
$\mathrm { C } _ { k } ^ { n } = \Big ( \begin{array} { l } { n } \\ { k } \end{array} \Big ) = \frac { n ! } { k ! ( n - k ) ! }$   
Description   
pull back of differential form (push-forward)   
pull back of function(push-forward)   
pull back of vector field (push-forward)   
product   
exterior product   
$k$ -th exterior bundle over $\mathbf { R } ^ { n }$   
Lagrangian subspace   
$K$ -Lagrangian subspace   
$f$ transverse to $Z$   
$f$ in the $p$ transverse to $Z$   
standard symplectic structure   
lift of mapping $\Omega ^ { \# } ( z _ { 1 } ) ( z _ { 2 } ) = \Omega ^ { - 1 } ( z _ { 1 } , z _ { 2 } )$   
down mapping $\Omega ^ { b } ( z _ { 1 } ) ( z _ { 2 } ) = \Omega ( z _ { 1 } , z _ { 2 } )$   
$k$ -differential form on $\mathbf { R } ^ { n }$   
partial derivative with respect to $x ^ { i }$   
boundary operator   
rotation   
divergence   
boundary integral   
integral of differential form   
empty set   
tensor product   
set-theoretic intersection   
set-theoretic union   
inclusion   
element of   
element of   
composition   
division   
not element of   
for   
homomorphism   
approximate   
similarly   
identity   
definition   
corresponding, equivalent, congruent relation   
conjugate congruent   
mapping   
extrusion   
extrusion mutually   
binomial coefficient

# Symbol

$\left( \begin{array} { c } { { n } } \\ { { k _ { 1 } , k _ { 2 } , \cdot \cdot \cdot , k _ { r } } } \end{array} \right) = \frac { n ! } { k _ { 1 } ! k _ { 2 } ! \cdot \cdot \cdot , k _ { r } ! }$ where $k _ { 1 } + \dot { k _ { 2 } } + \cdot \cdot \cdot + k _ { r } = n$   
$( a , b )$   
$[ a , b ]$   
$[ u , w ]$   
$[ A , B ]$   
$[ F , H ]$   
$( u , v )$   
$[ U , V ]$   
B   
U ◦+ V   
P1"P2   
- ,    
{ϕ, φ}   
a b   
a b   
1N (x) = x

# Description

multinomial coefficients.

open interval   
closed interval   
Lie bracket   
matrix commutator   
Poisson bracket   
inner product, Euclidean inner product   
symplectic inner product   
norm of matrix   
direct sum   
symplectic direct sum   
inner product   
Poisson bracket   
vector $a$ orthogonal to $b$ (Euclidean)   
vector $a$ symplectic orthogonal to $b$   
identity function

# Index

#

$\mathbf { A } ( \alpha )$ -stability, 550   
$\mathbf { a } ^ { * }$ –linear differential operator, 407   
$^ { a * }$ –Jacobian matrix, 407   
A-stability, 550   
ABC flow, 446   
action functional of Lagrangian density, 643   
${ \mathrm { A d } } ^ { * }$ -equivariant, 503   
adjoint integrator, 374   
adjoint method, 372   
all polynomials is symplectically separability   
in $\dot { \mathbf { R } } ^ { 2 n }$ , 207   
alternative canonical forms, 130   
angular momentum in body description, 505   
angular momentum in space description, 505   
angular momentum-preserving schemes for   
rigid body, 525   
angular velocity in body description, 505   
angular velocity in space description, 505   
anti-symmetric product, 117   
atlas, 40   
automorphism, 39   
autonomous Birkhoff’s equations, 618

# B

B-series, 417   
B-stability, 550   
backward error analysis, 432   
base of tangent space, 45   
BCH formula, 380, 413   
Betti numbers, 99   
bijective, 39   
bilinear antisymmetric form, 188   
binary forms, 116   
Birkhoffian system, 618   
black (fat )vertex, 309   
boundary of chains, 92   
Butcher tableau, 278

# C

calculate the formal energy, 267   
canonical equation, 170   
canonical forms under orthogonal   
transformation, 134   
canonical reductions of bilinear forms, 128   
canonical transformation, 172, 188   
Cartan form, 644   
Cartan’s Magic formula, 106   
Casimir function, 501   
Cayley transformation, 193   
centered Euler method, 416   
centered Euler scheme, 192, 200, 231   
chains, 91   
characteristic equations, 477   
chart, 40   
Chebyshev spectral method, 508   
classical Stokes theorem, 98   
closed form, 84   
closed nondegenerate differential 2-form, 165   
coadjoint orbits, 505   
coclosed form, 90   
codifferential operator, 89   
coefficient B-series for centered Euler   
scheme, 418   
coefficient B-series for exact solution, 418   
coefficient B-series for explicit Euler scheme,   
418   
coefficient B-series for implicit Euler scheme,   
418   
coefficient B-series for R–K method, 418   
coefficient B-series for trapezoidal scheme,   
418   
coefficients can be determined recursively,   
233   
coexact form, 90   
cohomology space, 98   
coisotropic subspace, 138   
commutativity of generator maps, 261   
commutator, 124, 179

commutator of two vector fields, 100   
comparison order conditions between symplectic R–K (R–K–N) method, 302   
comparison order conditions P–R–K method and symplectic P–R–K method, 318, 319, 333   
compatible of two local coordinate systems, 40   
complete non-integrability, 477   
complexifiable, 124   
complexification of real vector space and real linear transformation, 123   
composition laws, 419   
composition of centered Euler scheme, 372   
composition of trapezoid scheme, 365   
composition scheme is not $A$ -stable, 389   
compositional property of Lie series, 379   
condition for centered Euler to be volumepreserving, 444   
condition of symplectic P–R–K method, 303   
condition of variational self-adjointness, 619   
configuration space, 188   
conformally $K$ -symplectic group $C S p ( K , n , \mathbf { F } )$ , 120   
conformally canonical transformation, 173, 182   
conformally Hermitian, 117   
conformally identical, 114   
conformally orthogonal group $C O ( S , n , \mathbf { F } )$ , 120   
conformally symmetric, 114   
conformally symplectic group $C S p ( 2 n )$ , 144   
conformally unitary group $C U ( H , n , C )$ , 120   
congruence canonical forms of conformally symmetric, 130   
congruence canonical forms of Hermitian matrices, 130   
congruent reductions, 129   
conic function, 484   
conic Hamiltonian vector fields, 488   
conic map, 484   
conic symplectic, 484   
conic symplectic map, 484   
conic transformation, 488   
conservation Laws, 234   
conservation of spatial angular momentum theorem, 506   
constrained Hamiltonian algorithm, 537   
construction of the difference schemes via generating function, 213   
construct volume-preserving difference schemes, 454   
constructing s-scheme by 2nd kind g.f., 227

constructing s-scheme by Poincare type g.f., ´   
229   
constructing s-scheme via 1st kind g.f., 227   
construction of volume-preserving schemes   
via g.f., 464   
contact 1-form, 480   
contact algorithm, 483   
contact algorithm– $\overline { { C } }$ , 493   
contact algorithm– $\overline { { \mathbf { \nabla } \mathcal { P } } }$ , 492   
contact algorithm– $\overline { { Q } }$ , 492   
contact difference schemes, 492   
contact dynamical systems, 477   
contact element, 482   
contact generating function, 487   
contact geometry, 477   
contact Hamiltonian, 483, 492   
contact map, 486   
contact structure, 477, 481   
contact transformation, 483   
contactization of conic symplectic maps, 487   
contraction, 105   
convergence of symplectic difference   
schemes, 239   
coordinate Lagrangian subspaces, 147   
coordinate of tangent vector, 45   
coordinate subspaces, 139   
cotangent bundle, 76, 249   
cotangent vector, 76   
cycle, 93

# D

Darboux matrix, 231, 600   
Darboux theorem, 168, 190   
Darboux transformation, 249   
De Rham theorem, 99   
decomposed theorem of symplectic matrix, 155   
decompositions of source-free vector fields, 452   
definition of symplectic for LMM, 356   
density of tree $\gamma ( t )$ , 294   
diagonal formal flow, 415   
diagonal Pade approximant, 194 ´   
diagonally implicit method, 284   
diagonally implicit symplectic R–K method, 284   
diffeomorphism, 39, 102, 126, 188   
diffeomorphism group, 102   
differentiable manifold, 40   
differentiable manifold structure, 40   
differentiable mapping, 41   
differentiable mapping, differential concept, 43

differentiable structure, 40   
differential, 45   
differential $k$ -form, 77   
differential complex, 657   
diophantine condition, 566, 572   
diophantine frequency vectors, 552   
diophantine step sizes, 569   
direction field, 477   
discrete energy conservation law, 587   
discrete Euler–Lagrange equation, 587, 652   
discrete extended Lagrange 2-form, 589   
discrete Lagrange 2-form, 589   
discrete Lagrangian, 652   
discrete mechanics based on finite element   
methods, 606   
discrete multisymplectic conservation law,   
646   
discrete multisymplectic form formula, 652   
discrete total variation in the multisymplecti   
form, 605   
discrete variational principle in total   
variation, 596   
divergence-free system, 443, 449   
explicit Euler scheme, 204   
explike function, 349   
exponential matrix transform, 125   
extended canonical two form, 595   
extended configuration space, 581   
extended Lagrangian 1-form, 585   
extended phase space, 242   
extended symplectic 2-form, 585   
exterior algebra, 68   
exterior differential operator, 82   
exterior form, 66   
exterior monomials, 70   
exterior product, 64   
exterior product of forms, 72

# E

# F

fathers’ and sons’ relations, 297   
fiber of tangent bundle, 56   
first integrals, 234   
first order prolongation, 594, 643   
first order prolongation of $V$ , 584   
fixed point, 236   
formal energy, 264   
formal energy for symplectic R–K method,   
333, 339   
formal energy of centered Euler scheme, 344   
formal power series, 265, 407   
formal vector field, 432   
fourth order with 3-stage scheme, 365   
Frechet derivatives, 289   
free rigid body, 529   
eigenvalues of infinitesimal symplectic   
matrix, 159   
eigenvalues of symplectic matrix, 158   
elementary divisor in real space, 136   
elementary divisors in complex space, 136   
embedded submanifold, 538   
embedding submanifold, 51   
endomorphism, 39   
energy conservation law, 645   
energy density, 645   
energy equation, 644   
energy flux, 645   
energy-preserving schemes for rigid body,   
525   
epimorphism, 39   
equivalent atlas, 40   
Euclidean form, 118   
Euclidian structure, 137   
Euler centered scheme, 194   
Euler equation, 506   
Euler–Lagrange 1-form, 583   
Euler–Lagrange equation, 644   
Euler–Lagrange equation in FEM, 607   
even polynomial, 159   
exact form, 84   
exact symplectic mapping, 551   
exp maps, 412   
explicit Euler method, 415

# G

G-stability, 550   
Gauss IA-IA, 472   
Gauss theorem, 98   
Gauss–Legendre polynomial, 279   
Ge–Marsden theorem, 273   
general Hamilton–Jacobi equation, 221   
general linear group $G L ( n , \mathbf { F } )$ , 119   
general vector field, 583   
generalized Cayley transformation, 197, 198   
generalized Euler schemes, 231   
generalized Hamiltonian equation, 500   
generalized Lagrangian subspaces, 162   
generalized Noether theorem, 502   
generating function, 182, 219, 233, 601   
generating function and H.J. equation of the   
first kind, 223   
generating function and H.J. equation of the   
second kind, 223   
generating function for Lie–Poisson system,   
519   
generating function for volume-preserving,   
460   
generating function method, 432   
generating functions, 221, 255   
generating functions for Lagrangian   
subspaces, 160   
generator map, 255   
generators of $S p ( 2 n )$ , 155   
gradient map, 220   
gradient mapping, 219   
gradient transformation, 174   
graph of gradient map, 219   
graph of symplectic map, 219   
Grassmann algebra, 75   
Grassmann manifold, 143   
Green theorem, 97   
Gronwall inequality, 241   
group homomorphism, 126   
group of contact transformations, 483

# H

H-Stability, 401   
H-stability interval of explicit scheme, 404   
Hamilton–Jacobi equation, 182, 233, 462,   
602   
Hamilton–Jacobi equation for contact system,   
494   
Hamiltonian function, 187   
Hamiltonian mechanics, 165, 168   
Hamiltonian operator, 500   
Hamiltonian phase flow, 171   
Hamiltonian systems, 187   
Hamiltonian vector fields, 167, 170   
Hamiltonian–Jacobi equation, 627   
heavy top, 534   
Hermitian form, 117   
Hermitian, anti-Hermitian, 116   
high order symplectic-energy integrator, 600   
Hodge operator, 88   
homeomorphism, 39   
homogeneous symplectic, 484   
homology space, 99   
homomorphism, 39   
Hopf algebra, 433   
horizontal variation of $q ^ { i }$ , 586   
hyperplane, 478   
hypersurface, 477

# I

immersed submanifold, 48

immersion, 47   
implicit Euler method, 415   
impossible to construct volume-preserving   
algorithms analytically depending on   
source-free vector fields, 452   
infinitesimal generator vector field, 502   
infinitesimal symplectic matrices, 190   
injective, 39   
integral invariant, 171   
integral surface, 477   
integrator $S ( \tau )$ has a formal Lie expression,   
381   
invariance of generating functions, 261   
invariant groups for scalar products, 119   
invariant integral, 192   
invariant tori, 574   
invariant under the group $G$ of symplectic   
transformations, 234   
invariant under the phase flow of any   
quadratic Hamiltonian, 235   
invariants under congruences, 132   
inverse mapping, 39   
isomorphic mapping, 39   
isotropic subspace, 138   
isotropic, coisotropic, Lagrangian, 182

# J

Jacobi identity, 124, 177   
$J _ { 4 n }$ , $\tilde { J } _ { 4 n }$ -Lagrangian submanifold, 219, 622   
jet bundles, 643

#

$\tilde { K }$ -Lagrangian submanifold, 623   
$K ( z , { \dot { t } } )$ -symplectic, 621   
$k$ -forms, 67   
$K$ -symplectic group, 120   
$K$ -symplectic scheme, 622   
$K$ -symplectic structure, 190   
KAM iteration process, 556   
KAM theorem, 551   
KAM theorem of symplectic algorithms, 559   
Kane–Marsden–Ortiz integrator, 587

# L

L-stability, 550   
labeled $n$ -tree $\lambda \tau$ , 297   
labeled $P$ -tree, 309   
labeled graph, 292   
labeled trees, 298   
Lagrange 2-form in FEM, 607   
Lagrangian 2-form, 583   
Lagrangian density, 643   
Lagrangian mechanics, 581   
Lagrangian submanifold, 182, 250   
Lagrangian subspace, 138   
Lee-variational integrator, 581   
left translation action, 503   
Legendre transform, 645   
Legendre–Hodge transformation, 645   
Lie algebra, 125, 179, 190, 409   
Lie algebra of conformally invariant groups,   
128   
Lie bracket, 409   
Lie derivative, 103   
Lie group, 125   
Lie group action, 502   
Lie series, 377   
Lie–Poisson bracket, 501, 504   
Lie–Poisson equation, 504   
Lie–Poisson scheme, 519   
Lie–Poisson systems, 501   
Lie-Poisson-Hamilton-Jacobi equation, 514   
lifted action, 502   
linear damped oscillator, 629   
linear fractional transformation, 213   
linear Hamiltonian systems, 192   
linear multistep method, 347   
Liouville frequency vectors, 552   
Liouville’s phase-volume conservation law,   
189   
Liouville’s theorem, 172, 443   
Lobatto III A, 279, 280   
Lobatto III B, 279, 280   
Lobatto III C, 279, 280   
Lobatto IIIC-IIIC, 472   
Lobatto polynomial, 279   
local coordinate systems, 40   
log maps, 412   
logarithmic map, 434   
loglike function, 350

# M

Mobius strip, 61 ¨   
manifold, 40   
matrix representation of subspaces, 143   
maximum non-degeneracy, 477   
modified centered Euler scheme of sixth order, 433   
modified equation, 334, 432   
modified equation for centered Euler scheme, 336, 433   
modified integrators, 432   
momentum, 502   
momentum conservation law, 605, 645   
momentum density, 645   
momentum equation, 644   
momentum flux, 645   
momentum mapping, 502   
monomial, 207   
monomorphism, 39   
monotonic rooted labeled trees, 298   
Morse–Smale systems, 551   
multi-stage P–R–K method, 473   
multisymplectic Birkhoffian systems, 656   
multisymplectic conservation law, 605, 645   
multisymplectic dissipation law, 656   
multisymplectic form, 644   
multisymplectic form formula, 644   
multisymplectic Fourier pseudospectral methods, 654   
multisymplectic geometry, 643   
multisymplectic Hamiltonian system, 605   
multisymplectic Hamiltonian system for KdV equation, 648   
multisymplectic Hamiltonian system for KGS equation, 649   
multisymplectic Hamiltonian system for Schrodinger equation, 647 ¨   
multisymplectic Hamiltonian system for sine-Gordon equation, 646   
multisymplectic Hamiltonian systems, 645   
multisymplectic integrators, 646   
multisymplectic integrators for modified equations, 655   
multisymplectic-energy-momentum integrators, 605

#

natural product symplectic structure, 249   
near-0 formal power series, 409   
near-1 formal power series, 409   
nilpotent of degree 2, 204   
Noether theorem, 179   
non-exceptional matrices, 197   
non-existence of symplectic schemes   
preserving energy, 273   
non-superfluous tree, 299   
nonautonomous Birkhoff’s equation, 619   
nonautonomous Hamiltonian System, 242   
nonconservative multisymplectic Hamilto  
nian systems, 654   
nonexistence of SLMM for nonlinear   
Hamiltonian systems, 356   
nonresonant frequencies, 570   
normal Darboux matrix, 232, 239, 494   
normal Darboux matrix of a symplectic   
transformation, 600   
normalization coefficient B-series, 418   
normalization Darboux transformation, 251   
normalizing conditions, 453   
null space of 1-form, 478   
number of essential different labelings $\alpha ( t )$   
294   
numerical version of KAM theorem, 564

# O

obstruction, 450   
one-form (1-form), 66   
one-leg weighted Euler schemes, 231   
one-parameter group of canonical maps, 221   
operation $\wedge$ , 65   
optimization Method, 603   
orbit-preserving schemes, 527   
order conditions for symplectic R–K–N   
method, 319   
orientable differentiable manifold, 59   
orientable vector spaces, 59   
orthogonal group ${ \bar { O } } ( n , \mathbf { F } )$ , 119

# P

P–R–K method, 302   
Pade approximation, 193 ´   
Pade approximation table, 196 ´   
partitions and skeletons, 418   
Pfaffian theorem, 118   
phase flow, 102, 221, 408   
phase flow of contact system, 483   
phase flow- $e _ { F } ^ { t }$ , 235   
phase space, 102   
phase-area conservation law, 189   
Poincare lemma, 85, 220, 222´   
Poincare transformation, 250´   
Poincare’s generating function and H.J. ´   
equation, 223   
Poisson bracket, 177, 192, 499   
Poisson manifold, 499   
Poisson mapping, 500   
Poisson scheme, 508   
Poisson system, 500   
Poisson theorem, 179   
postprocessed vector field, 432   
Preissman integrator, 646   
preprocessed vector field integrators, 432   
preserve all quadratic first integrals of system   
236   
preserve angular momentum $p ^ { T } B q$ , 236   
preserving the contact structure, 483   
presymplectic form, 645   
presymplectic forms, 605   
product of cotangent bundles, 249   
product preservation property of Lie series,   
379   
prolongation spaces, 643   
proper mapping, 51   
properties of Lie series, 379   
pull-back, 80   
pull-back mapping, 374   
push-forward mapping, 374

# Q

quadratic bilinear form, 115   
quaternion form, 524

#

Radau I A, 279   
Radau IA-IA, 471   
Radau II A, 280   
Radau IIA-IIA, 472   
Radau polynomial, 279   
rational fraction, 200   
real representation of complex vector space,   
121   
reduction method, 540   
reflective polynomial, 158   
regular submanifold, 51, 53   
relationship between rooted tree and   
elementary differential, 293   
resonant, 568   
revertible approximations, 450   
Riemann structure, 167   
right translation, 503   
rigid body in Euclidean space, 523   
Rodrigue formula, 543   
root isomorphism, 298   
rooted $n$ -tree, 299   
rooted $P$ -tree, 309   
rooted $S$ -tree, 321   
rooted 3-tree, 298   
rooted labeled $n$ -tree $\rho \lambda \tau$ , 297   
rooted labeled $P$ -tree, 309   
rooted labeled $S$ -tree, 321   
rooted labeled 3-tree, 298   
rooted labeled trees, 298

# S

$S$ -graph, 321   
$S$ -orthogonal group, 119   
$S$ -tree, 321   
scalar product, 117   
section of tangent bundle, 62   
self-adjoint integrator, 376   
self-adjoint method, 372   
separable Hamiltonian system, 202   
separable systems for source-free systems,   
447   
sesquilinear form, 116   
simplify symplectic R–K conditions, 300   
simplifying condition of R–K method, 279   
$S m ( 2 n )$ matrices, 600   
small twist mappings, 558   
some theorems about $\mathbf { S p } ( \mathbf { 2 n } )$ , 151   
sons of the root, 297   
source-free system, 443, 449, 467   
$S p ( 2 n )$ matrices, 600   
$S p D _ { 2 n }$ the totality of symplectic operators,   
232   
$S p D _ { 2 n }$ the set of symplectic transformations,   
601   
special linear group $S L ( n , F )$ , 119   
special separable source-free systems, 458   
special type $S p _ { 2 n } ( \mathrm { I } )$ , 150   
special type $S p _ { 2 n } ( \mathrm { I I } )$ , 151   
special type $S p _ { 2 n } ( \mathrm { I I I } )$ , 151   
special type $S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } )$ , 151   
special types of $S p ( 2 n )$ , 148   
stability analysis for composition scheme,   
388   
standard antisymmetric matrix, 192   
standard symplectic structure, 169, 188, 249   
star operators, 88   
step size resonance, 568   
step transition, 415   
step-forward operator, 240   
Stokes theorem, 93   
structure-stability, 551   
subalgebra of a Lie algebra, 179   
submanifold, 46   
submersion, 51   
substitution law, 432   
superfluous trees, 298   
surjective, 39   
Sylvester’s law of inertia, 132   
${ \dot { S y m m } } ( 2 n )$ the set of symmetric   
transformations, 601   
$s y m m ( 2 n )$ the totality of symmetric   
operators, 232   
symmetric operators near nullity, 232   
symmetric pair, 216   
symmetric product, 117   
symmetrical composition, 376   
symmetry of tree $\bar { \boldsymbol { \sigma } } ( t )$ , 294   
symplectic algebra, 216   
symplectic algorithms as small twist   
mappings, 560   
symplectic basis, 145

symplectic conditions for $\mathbf { R - K }$ method, 281   
symplectic explicit $\mathrm { R - K - N }$ method (non-redundant 5-stage fifth order), 331   
symplectic form, 118   
symplectic geometry, 165, 188   
symplectic group, 188   
symplectic group $S p ( 2 n )$ , 144   
symplectic group $S p ( 2 n , F )$ , 119   
symplectic invariant algorithms, 235   
symplectic leave, 505   
symplectic LMM for linear Hamiltonian systems, 348   
symplectic manifold, 165   
symplectic map, 220   
symplectic mapping, 215   
symplectic matrix, 189   
symplectic operators near identity, 232   
symplectic pair, 217   
symplectic R–K method, 277, 279   
symplectic R–K–N method, 319   
symplectic R–K–N method (3-stage and 4-th order), 323   
symplectic schemes for Birkhoffian Systems, 625   
symplectic schemes for nonautonomous system, 244   
symplectic space, 137   
symplectic structure, 137, 165, 215, 477   
symplectic structure for trapezoidal scheme, 202   
symplectic structure in product space, 215   
symplectic subspace, 137   
symplectic-energy integrator, 596, 602   
symplectic-energy-momentum, 581   
symplectically separable Hamiltonian systems, 205   
symplectization of contact space, 487   
symplified order conditions for symplectic R–K–N method, 327   
symplified order conditions of explicit symplectic R–K method, 307

# T

table of coefficient $\omega ( \tau )$ for trees of order $\leqslant 5$ , 435   
table of coefficients $\sigma ( \tau ) , \gamma ( \tau ) , \breve { b } ( \tau )$ , and $\widehat { b } ( \tau )$ , 434   
table of composition laws for the trees of order $\leq 4$ , 436   
table of substitution law $^ *$ defined in for the trees of order $\leq 5$ , 437   
tangent bundle, 56   
tangent mapping, 58


<!-- chunk 0011: pages 701-701 -->
tangent space, 44   
tangent vector, 43   
the elementary differential, 291   
the inverse function to exp, 126   
the order of tree $r ( t )$ , 294   
time-dependent gradient map, 221   
topological manifold, 40   
total variation for Lagrangian mechanics, 583   
total variation in Hamiltonian mechanics, 593   
transversal, 54, 140, 143   
transversal Lagrangian subspaces, 148   
transversality condition, 181, 213, 221, 225,   
227, 250, 251, 460, 623   
trapezoidal method, 416   
trapezoidal scheme, 201   
tree, 298   
trivial tangent bundle, 57   
truncation, 233   
two-forms (2-forms), 66

#

Unitary group $U ( n , C )$ , 119   
Unitary product, 118

#

variational integrators, 651   
variational principle in Hamiltonian   
mechanics, 591   
vector field, 62   
vertical vector field, 582   
Veselov–Moser algorithm, 539   
volume-preserving 2-Stage P–R–K methods,   
471   
volume-preserving P-R–K method, 467   
volume-preserving R–K method, 467   
volume-preserving schemes, 444

#

$W$ -transformation, 304, 470   
white (meagre) vertex, 309   
Witt theorem, 132

#

$X$ -matrix, 305
