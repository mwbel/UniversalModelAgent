![](images/e7b7b374cd7f93f4f842e0f641882613a5ed3e7cd4154833e9a8c44cfbbeb28e.jpg)  
Figure 12.1 Time evolution of PV field under merger of two vortices.

As a simple demonstration we consider the merger of two vortices with parameters $f _ { 0 } = c _ { 0 } = L _ { R } = 1$ . The initial velocity field is set equal to $\pmb { u } ^ { 9 }$ with an initial layer-depth $h$ such that the Rossby number satisfies ${ \sf R o } \approx 0 . 1$ and $L \approx L _ { R }$ , i.e. $\mathsf { B u } \approx 1$ . This setting complies with quasi-geostrophic theory. We show snapshots of the time evolution of the PV field $q$ over 60 time units in Fig. 12.1. In Fig. 12.2 we demonstrate the excellent conservation of total energy and maintenance of geostrophic balance by monitoring the ratio of the $L _ { 2 }$ -norm of the ageostrophic velocity $\pmb { u } ^ { \mathrm { a g } } : = \pmb { u } - \pmb { u } ^ { \mathrm { g } }$ to the $L _ { 2 }$ -norm of the geostrophic wind approximation $\pmb { u } ^ { 9 }$

$$
R ( t ) : = \frac { \| \pmb { u } ^ { \mathrm { a } 9 } ( t ) \| _ { 2 } } { \| \pmb { u } ^ { \mathrm { g } } ( t ) \| _ { 2 } } .
$$

Note that $R ( t ) = 0$ at $t = 0$ . The simulation was run with $N = 2 6 2 1 4 4$ particles, $\Delta x = 2 \pi / 1 2 8$ and a smoothing length $\alpha = 2 \Delta x$ .

One can apply the Hamiltonian particle-mesh method to the shallow-water equations on the sphere which provides a simple model for global atmospheric circulation [65]. Furthermore, the Hamiltonian particle-mesh method can be extended to fully three-dimensional flows. The basic approach and its relation to geostrophic and hydrostatic balance have been outlined by COTTER AND REICH [47].

![](images/053c12de10bcc7ce0de2cbfce23f90da84e9a81268305e975b6703ff74b85de5.jpg)  
Figure 12.2 Ratio $R ( t )$ of ageostrophic to geostrophic velocity contributions and relative error in energy.

# 12.3 Multi-symplectic PDEs

When we derived the Hamiltonian formulation of the wave equation (12.1), the PDE (12.1) was rewritten as a system of equations with only first-order derivatives in time. Let us now rewrite (12.1) as a system of equations containing only first-order derivatives in space and time. We obtain, for example,

$$
\begin{array} { c } { - v _ { t } - p _ { x } = f ^ { \prime } ( u ) , } \\ { u _ { t } = v , } \\ { u _ { x } = w , } \\ { 0 = p + \sigma ^ { \prime } ( w ) . } \end{array}
$$

As first noted by BRIDGES [31, 30], this system is of the general from

$$
K z _ { t } + L z _ { x } = \nabla _ { z } S ( z ) ,
$$

where $z \in \mathbb { R } ^ { d }$ is the state variable, $K , L \ \in \ \mathbb { R } ^ { d \times d }$ are two (constant) skewsymmetric matrices, $S : \mathbb { R } ^ { d }  \mathbb { R }$ is a smooth function, and $\nabla _ { z }$ is the standard gradient in $\mathbb { R } ^ { d }$ .

Example3 In case of the nonlinear wave equation (12.1)，we can take $z =$ $( u , v , p , w ) ^ { T } \in \mathbb { R } ^ { 4 }$

$$
S ( z ) = { \frac { 1 } { 2 } } v ^ { 2 } + w p + \sigma ( w ) + f ( u ) ,
$$

and

$$
K = \left[ \begin{array} { c c c c } { 0 } & { - 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] , \qquad L = \left[ \begin{array} { c c c c } { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] .
$$

According to BRIDGES [31, 30], a PDE of the form (12.33) is now called a multisymplectic PDE for the following reason. With each of the two skew-symmetric matrices we identify a pre-symplectic form;5 i.e.

$$
\omega = \frac { 1 } { 2 } d z \wedge K d z , \qquad \kappa = \frac { 1 } { 2 } d z \wedge L d z .
$$

These pre-symplectic forms satisfy a conservation law of symplecticness

$$
\omega _ { t } + \kappa _ { X } = 0 .
$$

Indeed, the variational equation

$$
K d z _ { t } + L d z _ { x } = { \cal A } ( { x } , t ) d z , \qquad { \cal A } ( { x } , t ) = S _ { z z } ( z ( x , t ) ) ,
$$

implies

$$
d z \wedge K d z _ { t } + d z \wedge L d z _ { x } = d z \wedge A ( x , t ) d z ,
$$

and, since $d z \wedge A ( x , t ) d z = 0$

$$
\frac { 1 } { 2 } \partial _ { t } ( d z \wedge K d z ) + \frac { 1 } { 2 } \partial _ { x } ( d z \wedge L d z ) = 0 .
$$

Note that

$$
\frac { d } { d t } \bar { \omega } = \frac { d } { d t } \int _ { 0 } ^ { L } \omega d x = \int _ { 0 } ^ { L } \omega _ { t } d x = - \left[ \kappa \right] _ { x = 0 } ^ { x = L } = 0 ,
$$

and conservation of the total symplectic form (12.2) is a consequence of the conservation law of symplecticness (12.34).

The Lagrangian formulation (12.20)–(12.21) of the shallow-water equations can also be rewritten as a multi-symplectic PDE of the form

$$
K z _ { t } + L _ { 1 } z _ { a } + L _ { 2 } z _ { b } = \nabla _ { z } S ( z ) ,
$$

where $K , L _ { 1 } , L _ { 2 }$ are again constant skew-symmetric matrices associated with the independent variables time $t$ and labels $\pmb { a } = ( a , b ) ^ { T }$ . The details can be found in [32]. As shown above for the nonlinear wave equation, the associated multisymplectic conservation law is of the form

$$
\partial _ { t } \omega + \partial _ { a } \kappa _ { 1 } + \partial _ { b } \kappa _ { 2 } = 0 ,
$$

where

$$
\omega = \frac { 1 } { 2 } d z \wedge K d z = \frac { h _ { o } f _ { 0 } } { 2 } d { \pmb X } \wedge J _ { 2 } d { \pmb X } + d { \pmb p } \wedge d { \pmb X }
$$

is the density of the symplectic form (12.22).

# 12.3.1 Conservation laws

Every multi-symplectic formulation (12.33) implies conservation laws of energy, momentum, and symplecticness [31, 30]. To derive those explicitly, let us introduce a decomposition of the two skew-symmetric matrices $\kappa$ and $\iota$ such that

$$
K = K _ { + } + K _ { - } \quad \mathrm { a n d } \quad L = L _ { + } + L _ { - } ,
$$

with

$$
K _ { + } ^ { T } = - K _ { - } \quad \mathrm { a n d } \quad L _ { + } ^ { T } = - L _ { - } .
$$

A decomposition of this form immediately implies that

$$
d z \wedge K _ { + } d z = d z \wedge K _ { - } d z \quad \mathrm { a n d } \quad d z \wedge L _ { + } d z = d z \wedge L _ { - } d z ,
$$

hence, the conservation law (12.34) holds with

$$
\omega = d z \wedge K _ { + } d z \quad \mathsf { a n d } \quad \kappa = d z \wedge L _ { + } d z .
$$

An energy conservation law (12.26) is obtained by taking the inner product of (12.33) and $z _ { t }$ . Since $\langle z _ { t } , K z _ { t } \rangle = 0$ , we obtain

$$
\langle z _ { t } , L z _ { x } \rangle = \langle z _ { t } , \nabla _ { z } S ( z ) \rangle = \partial _ { t } S ( z ) .
$$

Note that

$$
\begin{array} { r l } & { \langle z _ { t } , L z _ { x } \rangle = \langle z _ { t } , L _ { + } z _ { x } \rangle + \langle z _ { t } , L _ { - } z _ { x } \rangle } \\ & { \qquad = \langle z _ { t } , L _ { + } z _ { x } \rangle - \langle z _ { x } , L _ { + } z _ { t } \rangle } \\ & { \qquad = \partial _ { x } \langle z _ { t } , L _ { + } z \rangle - \partial _ { t } \langle z _ { x } , L _ { + } z \rangle , } \end{array}
$$

and the energy conservation law (12.26) is satisfied by

$$
E = S ( z ) + \langle z _ { x } , L _ { + } z \rangle \quad { \mathrm { a n d } } \quad F = - \langle z _ { t } , L _ { + } z \rangle .
$$

Similarly, taking the inner product with $z _ { x }$ , the momentum conservation law

$$
\partial _ { t } M + \partial _ { x } I = 0 ,
$$

is satisfied by

$$
M = - \langle z _ { x } , K _ { + } z \rangle \quad { \mathrm { a n d } } \quad I = S ( z ) + \langle z _ { t } , K _ { + } z \rangle .
$$

Example 4In case of the multi-symplectic formulation of the nonlinear wave equation (12.1), we can take a decomposition of the matrices $\kappa$ and $\iota$ defined by

$$
\begin{array} { r } { \boldsymbol { K } _ { + } = \left[ \begin{array} { c c c c } { 0 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] \quad \mathrm { ~ a n d ~ } \quad \boldsymbol { L } _ { + } = \left[ \begin{array} { c c c c } { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] . } \end{array}
$$

The conservation law of symplecticness becomes

$$
\partial _ { t } [ d u \wedge d v ] + \partial _ { x } [ d u \wedge d p ] = 0 .
$$

It is also easy to show that (12.26) is satisfied with

$$
E = \frac { 1 } { 2 } v ^ { 2 } + \sigma ( w ) + f ( u ) = \frac { 1 } { 2 } u _ { t } ^ { 2 } + \sigma ( u _ { x } ) + f ( u ) \quad \mathrm { a n d } \quad F = v p = - u _ { t } \sigma ^ { \prime } ( u _ { x } ) .
$$

Similarly, the momentum conservation law (12.37) is satisfied for

$$
M = w v = u _ { x } u _ { t }
$$

and

$$
I = \sigma ( w ) + p w - \frac { 1 } { 2 } v ^ { 2 } + f ( u ) = \sigma ( u _ { x } ) - \sigma ^ { \prime } ( u _ { x } ) u _ { x } - \frac { 1 } { 2 } u _ { t } ^ { 2 } + f ( u ) .
$$

An additional conservation law is obtained from the restriction of the multisymplectic conservation law (12.34) to the space of solutions $z ( x , t )$ via

$$
d z = z _ { t } d t + z _ { x } d x .
$$

Hence

$\omega _ { | z } = d z \wedge K d z = 2 \langle z _ { t } , K z _ { x } \rangle d t \wedge d x , \quad \kappa _ { | z } = d z \wedge L d z = 2 \langle z _ { t } , L z _ { x } \rangle d t \wedge d x .$ , and (12.34) reduces to

$$
\partial _ { t } \langle z _ { t } , K z _ { x } \rangle + \partial _ { x } \langle z _ { t } , L z _ { x } \rangle = 0 .
$$

If one applies a similar restriction

$$
d z = z _ { a } d a + z _ { b } d b
$$

to the multi-symplectic conservation law (12.35) of the shallow-water equations, then one finds that

$$
\omega _ { | z } = q , \qquad \kappa _ { | z } ^ { 1 } = \kappa _ { | z } ^ { 2 } = 0 ,
$$

and the restricted multi-symplectic conservation law is equivalent to conservation of potential vorticity, i.e. $q _ { t } = 0$ in the Lagrangian setting [32].

# 12.3.2 Traveling waves and dispersion

Traveling wave or soliton solutions are very easy to characterize once a multisymplectic formulation has been found. We make the ansatz

$$
z ( x , t ) = \pmb { \phi } ( x - c t ) = \pmb { \phi } ( \xi ) .
$$

Then the equation (12.33) becomes

$$
- c K \phi _ { \xi } + L \phi _ { \xi } = \nabla _ { \phi } S ( \phi ) .
$$

If we assume that the skew-symmetric matrix $L - c K$ is invertible, then we obtain the Hamiltonian ODE

$$
\frac { d } { d \xi } \phi = J _ { c } \nabla _ { \phi } S ( \phi ) , \qquad J _ { c } = [ L - c K ] ^ { - 1 } ,
$$

in the state variable $\pmb { \phi } \in \mathbb { R } ^ { n }$ and with Hamiltonian $S$ . It should be noted that the symplectic structure matrix $J _ { c }$ is a superposition of the temporal and spatial pre-symplectic structures $\omega$ and $\kappa$ , respectively.

As an example, let us consider the KdV equation (12.23). We introduce the velocity potential $\psi$ with $\psi _ { x } = u$ and obtain

$$
\psi _ { x t } + \frac { 1 } { 2 } \partial _ { x } ( \psi _ { x } ) ^ { 2 } + \psi _ { x x x x } = 0 .
$$

It should be kept in mind that $\psi$ is only uniquely determined up to a constant. To remove this ambiguity we apply the normalization $\textstyle { \int { \psi d x } = 0 }$ . A multi-symplectic formulation of type (12.33) is provided by

$$
\begin{array} { c } { u _ { t } + p _ { x } = 0 , } \\ { - \psi _ { t } - 2 w _ { x } = - p + u ^ { 2 } , } \\ { 2 u _ { x } = 2 w , } \\ { - \psi _ { x } = - u , } \end{array}
$$

$z = ( \psi , u , w , p ) ^ { T }$ and

$$
S = { \frac { 1 } { 3 } } u ^ { 3 } + w ^ { 2 } - p u .
$$

If we look for soliton solutions with wave speed $C$ , then the associated structure matrix $J _ { c }$ is given by

$$
J _ { c } ^ { - 1 } = \left[ \begin{array} { c c c c } { 0 } & { - c } & { 0 } & { 1 } \\ { c } & { 0 } & { - 2 } & { 0 } \\ { 0 } & { 2 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } \end{array} \right] .
$$

The equilibrium solutions are given by $\nabla _ { z } S ( z ) = \mathbf { 0 }$ and, hence, $U = w = p =$ 0. Since the value of $\psi$ does not enter the equations, we set it to $\psi = 0$ in accordance with our normalization condition $\textstyle { \int { \psi d x } = 0 }$ . Hence there is only one equilibrium and a soliton solution must correspond to a homoclinic connection. Indeed, such a homoclinic orbit exists for any $c > 0$ and the soliton solutions with wave speed $c > 0$ are of the form

$$
u ( x , t ) = 3 c \ { \mathrm { s e c h } } ^ { 2 } \left( { \frac { 1 } { 2 } } { \sqrt { c } } ( x - c t ) \right) .
$$

As in the analysis of Section 5.1.1, for linear PDEs we can make the (harmonic) wave ansatz

$$
z ( x , t ) = \pmb { \phi } ( x - c t ) = \pmb { a } \mathrm { e } ^ { j ( k x - \omega t ) } ,
$$

where $\pmb { \partial } \in \mathbb { C } ^ { d }$ is a constant vector, $k \geq 0$ is the wave number, $\omega$ is the frequency6 of the wave with wave speed $c = \omega / k$ , and $j = \sqrt { - 1 }$ . Upon substituting this into a linear multi-symplectic PDE

$$
K z _ { t } + L z _ { x } = A z ,
$$

one obtains the linear system of equations

$$
\left[ j \omega K - j k { \pmb { L } } + { \pmb { A } } \right] { \pmb { a } } = { \pmb { 0 } } .
$$

6One should not confuse the frequency $\omega$ with the two form $\omega$ defined earlier.

For a nontrivial solution $\pm \mathbf { 0 }$ , we must require that

$$
\operatorname* { d e t } \left[ j \omega K - j k L + { \cal A } \right] = 0 .
$$

The resulting polynomial expression in $\omega$ and $k$ is called the dispersion relation [201]. Consider, for example, the linear KdV equation

$$
u _ { t } + u _ { x } + u _ { x x x } = 0 ,
$$

which possesses a multi-symplectic structure identical to the nonlinear KdV equation (12.23), but with the Hamiltonian $S$ replaced by

$$
S = u ^ { 2 } + w ^ { 2 } - p u .
$$

The associated linear system of equations is

$$
\left[ \begin{array} { c c c c } { { 0 } } & { { j \omega } } & { { 0 } } & { { - j k } } \\ { { - j \omega } } & { { 2 } } & { { 2 j k } } & { { - 1 } } \\ { { 0 } } & { { - 2 j k } } & { { 2 } } & { { 0 } } \\ { { j k } } & { { - 1 } } & { { 0 } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c c c c } { { a _ { \psi } } } \\ { { a _ { u } } } \\ { { a _ { w } } } \\ { { a _ { p } } } \end{array} \right] = { \bf 0 } ,
$$

which gives rise to the dispersion relation

$$
\operatorname* { d e t } { \left[ \begin{array} { c c c c } { 0 } & { j \omega } & { 0 } & { - j k } \\ { - j \omega } & { 2 } & { 2 j k } & { - 1 } \\ { 0 } & { - 2 j k } & { 2 } & { 0 } \\ { j k } & { - 1 } & { 0 } & { 0 } \end{array} \right] } = 4 \omega k - 4 k ^ { 2 } + 4 k ^ { 4 } = 0 .
$$

The more common form of this relation is $\omega = k - k ^ { 3 }$ .

# 12.3.3 Multi-symplectic integrators

In this section, we discuss numerical schemes that preserve a discrete version of the conservation law of symplecticness. Such schemes are called multi-symplectic. The idea is to apply symplectic discretization methods in space and in time. This is in contrast to the numerical approach outlined in Section 12.2 where only the time discretization was explicitly treated by a symplectic method. In other words, multi-symplectic methods treat space and time on equal footing.

Here and throughout the remainder of the chapter, we use the notation $z _ { i } ^ { n }$ to denote a numerical approximation of $z ( x _ { i } , t _ { n } )$ , where $X _ { j }$ makes reference to a particular point on the spatial mesh and $t _ { n }$ refers to a specific point in time. We also define $\Delta x = x _ { i + 1 } - x _ { i }$ and $\Delta t = t _ { n + 1 } - t _ { n }$ and assume that both quantities are constant throughout the mesh. Then using both forward and backward differences, we define discrete approximations to $z _ { x }$ by

$$
\partial _ { x } ^ { + } z _ { i } ^ { n } : = \frac { z _ { i + 1 } ^ { n } - z _ { i } ^ { n } } { \Delta x } \quad \mathrm { a n d } \quad \partial _ { x } ^ { - } z _ { i } ^ { n } : = \frac { z _ { i } ^ { n } - z _ { i - 1 } ^ { n } } { \Delta x } ,
$$

and discrete approximations to $z _ { t }$ by

$$
\partial _ { t } ^ { + } z _ { i } ^ { n } : = \frac { z _ { i } ^ { n + 1 } - z _ { i } ^ { n } } { \Delta t } \quad \mathrm { a n d } \quad \partial _ { t } ^ { - } z _ { i } ^ { n } : = \frac { z _ { i } ^ { n } - z _ { i } ^ { n - 1 } } { \Delta t } .
$$

We have seen that the multi-symplectic formulation (12.33) provides a presymplectic form for each of the independent variables $x$ and $t$ . BRIDGES AND REICH [33] suggested to apply a symplectic discretization to each of the independent variables. We now give two specific examples for this approach.

# Euler box scheme

Given a Hamiltonian ODE, written as

$$
K z _ { t } = \nabla _ { z } H ( z ) , \quad K = J ^ { - 1 } ,
$$

consider the scheme

$$
K _ { + } \partial _ { t } ^ { + } z ^ { n } + K _ { - } \partial _ { t } ^ { - } z ^ { n } = \nabla _ { z } H ( z ^ { n } ) ,
$$

where ${ \cal K } = { \cal K } _ { + } + { \cal K } _ { - }$ is an appropriate decomposition in the sense discussed in Section 12.3.1.

As suggested by MOORE AND REICH [137], the discretization (12.43) can also be applied to the spatial part of a multi-symplectic PDE (12.33). This yields the semi-discretization

$$
K \partial _ { t } z _ { i } + L _ { + } \partial _ { x } ^ { + } z _ { i } + L _ { - } \partial _ { x } ^ { - } z _ { i } = \nabla _ { z } S ( z _ { i } ) .
$$

We next discretize in time to obtain the fully discrete equations

$$
\begin{array} { r } { K _ { + } \partial _ { t } ^ { + } z _ { i } ^ { n } + K _ { - } \partial _ { t } ^ { - } z _ { i } ^ { n } + L _ { + } \partial _ { x } ^ { + } z _ { i } ^ { n } + L _ { - } \partial _ { x } ^ { - } z _ { i } ^ { n } = \nabla _ { z } S ( z _ { i } ^ { n } ) . } \end{array}
$$

In order to show that this discretization satisfies a discrete conservation law of symplecticness, consider the discrete variational equation

$$
\begin{array} { r } { K _ { + } \partial _ { t } ^ { + } d z _ { i } ^ { n } + K _ { - } \partial _ { t } ^ { - } d z _ { i } ^ { n } + L _ { + } \partial _ { x } ^ { + } d z _ { i } ^ { n } + L _ { - } \partial _ { x } ^ { - } d z _ { i } ^ { n } = S _ { z z } ( z _ { i } ^ { n } ) d z _ { i } ^ { n } . } \end{array}
$$

Now take the wedge product of this equation with $d z _ { i } ^ { n }$ , and notice that we have

$$
d z _ { i } ^ { n } \wedge S _ { z z } ( z _ { i } ^ { n } ) d z _ { i } ^ { n } = 0 ,
$$

because $S _ { z z } ( z _ { i } ^ { n } )$ is a symmetric matrix. Then, for the terms containing $\partial _ { t } ^ { \pm }$ , we obtain

$$
d z _ { i } ^ { n } \wedge K _ { + } \partial _ { t } ^ { + } d z _ { i } ^ { n } + d z _ { i } ^ { n } \wedge K _ { - } \partial _ { t } ^ { - } d z _ { i } ^ { n } = \partial _ { t } ^ { + } \left( d z _ { i } ^ { n - 1 } \wedge K _ { + } d z _ { i } ^ { n } \right) .
$$

Doing the same for the terms containing $\partial _ { x } ^ { \pm }$ , we derive a discrete conservation law

$$
\partial _ { t } ^ { + } \omega _ { i } ^ { n } + \partial _ { x } ^ { + } \kappa _ { i } ^ { n } = 0 ,
$$

for

$$
\omega _ { i } ^ { n } = d z _ { i } ^ { n - 1 } \wedge K _ { + } d z _ { i } ^ { n } \quad \mathrm { a n d } \quad \kappa _ { i } ^ { n } = d z _ { i - 1 } ^ { n } \wedge L _ { + } d z _ { i } ^ { n } .
$$

Example 5The sine-Gordon equation can be rewritten as a multi-symplectic PDE

$$
- v _ { t } - p _ { x } = \sin ( u ) , \quad u _ { t } = v , \quad u _ { x } = - p .
$$

Spatial discretization by a method (12.43) yields

$$
- \frac { d } { d t } v _ { i } - \frac { p _ { i + 1 } - p _ { i } } { \Delta x } = \mathsf { s i n } ( u _ { i } ) , \quad \frac { d } { d t } u _ { i } = v _ { i } , \quad \frac { u _ { i } - u _ { i - 1 } } { \Delta x } = - p _ { i } ,
$$

or, equivalently

$$
- \frac { d } { d t } v _ { i } + \frac { u _ { i + 1 } - 2 u _ { i } + u _ { i - 1 } } { \Delta x } = \mathsf { s i n } ( u _ { i } ) , \quad \frac { d } { d t } u _ { i } = v _ { i } .
$$

The same spatial truncation is obtained from the truncated Hamiltonian

$$
H = \sum _ { i } \left[ \frac { 1 } { 2 } ( v _ { i } ) ^ { 2 } + \frac { 1 } { 2 } \left( \frac { u _ { i + 1 } - u _ { i } } { \Delta x } \right) ^ { 2 } + \left( 1 - \cos u _ { i } \right) \right] \Delta x
$$

and the Hamiltonian equations of motion

$$
\frac { d } { d t } v _ { i } = - \Delta x ^ { - 1 } \nabla _ { u _ { i } } H , \qquad \frac { d } { d t } u _ { i } = \Delta x ^ { - 1 } \nabla _ { v _ { i } } H .
$$

Another application of the discretization (12.43) in time yields the method (12.28). ✷

Let us now go back to the spatially discretized PDE (12.44). Taking the inner product with $\partial _ { t } z _ { i }$ yields

$$
\langle \partial _ { t } z _ { i } , L _ { + } \partial _ { x } ^ { + } z _ { i } \rangle + \langle \partial _ { t } z _ { i } , L _ { - } \partial _ { x } ^ { - } z _ { i } \rangle = \partial _ { t } S ( z _ { i } ) ,
$$

because $\langle \partial _ { t } z _ { i } , \nabla _ { z } S ( z _ { i } ) \rangle = \partial _ { t } S ( z _ { i } )$ . Next we note that

$$
\begin{array} { r l } & { \partial _ { t } E _ { i } = \partial _ { t } S ( z _ { i } ) + \partial _ { t } \langle \partial _ { x } ^ { - } z _ { i } , L _ { + } z _ { i } \rangle } \\ & { \qquad = \langle \partial _ { t } z _ { i } , L _ { + } \partial _ { x } ^ { + } z _ { i } \rangle + \langle \partial _ { t } z _ { i } , L _ { - } \partial _ { x } ^ { - } z _ { i } \rangle + \partial _ { t } \langle \partial _ { x } ^ { - } z _ { i } , L _ { + } z _ { i } \rangle } \\ & { \qquad = \langle \partial _ { t } z _ { i } , L _ { + } \partial _ { x } ^ { + } z _ { i } \rangle + \langle \partial _ { t } \partial _ { x } ^ { - } z _ { i } , L _ { + } z _ { i } \rangle } \\ & { \qquad = \partial _ { x } ^ { + } \langle \partial _ { t } z _ { i - 1 } , L _ { + } z _ { i } \rangle . } \end{array}
$$

Hence, the spatially discrete energy conservation law

$$
\partial _ { t } E _ { i } + \partial _ { x } ^ { - } F _ { i + 1 / 2 } = 0
$$

is obtained for the discrete energy density

$$
E _ { i } = S ( z _ { i } ) + \langle \partial _ { x } ^ { - } z _ { i } , L _ { + } z _ { i } \rangle ,
$$

and the energy flux

$$
F _ { i + 1 / 2 } = - \langle \partial _ { t } z _ { i } , L _ { + } z _ { i + 1 } \rangle .
$$

Now consider the momentum conservation law (12.37). A semi-discretized version of this law can be obtained in the same manner as the spatially discretized version of the energy conservation law by simply exchanging the roles of space and time. Hence, we formally discretized (12.33) in time using (12.43) and take the inner product with $\partial _ { x } z ^ { n }$ to get the semi-discretized momentum conservation law

$$
\partial _ { t } ^ { + } M ^ { n - 1 / 2 } + \partial _ { x } I ^ { n } = 0 ,
$$

where

$$
M ^ { n + 1 / 2 } = - \langle \partial _ { x } z ^ { n } , K _ { + } z ^ { n + 1 } \rangle \quad \mathrm { a n d } \quad I ^ { n } = S ( z ^ { n } ) + \langle \partial _ { t } ^ { - } z ^ { n } , K _ { + } z ^ { n } \rangle .
$$

See [137] for further details on the energy-momentum conservation of the fully discretized equations using modified equation analysis.

Example6 The semi-discretized energy conservation law for the Euler box scheme applied to the sine-Gordon equation is given by (12.29). Let us also derive the semidiscretized momentum conservation law. We formally introduce a symplectic Euler time-discretization of the multi-symplectic sine-Gordon equation

$$
- \partial _ { t } ^ { + } v ^ { n } - p _ { x } ^ { n } = \sin ( u ^ { n } ) , \quad \partial _ { t } ^ { - } u ^ { n } = v ^ { n } , \quad u _ { x } ^ { n } = - p ^ { n } .
$$

Taking the appropriate inner product and rearranging terms we obtain

$$
- u _ { x } ^ { n } \partial _ { t } ^ { + } v ^ { n } + v _ { x } ^ { n + 1 } \partial _ { t } ^ { + } u ^ { n } = \left( 1 - \cos ( u ^ { n } ) + ( v ^ { n + 1 } ) ^ { 2 } / 2 - ( p ^ { n } ) ^ { 2 } / 2 \right) _ { x } .
$$

The left-hand side is equivalent to

$$
- u _ { x } ^ { n } \partial _ { t } ^ { + } v ^ { n } + v _ { x } ^ { n + 1 } \partial _ { t } ^ { + } u ^ { n } = - \partial _ { t } ^ { + } ( u _ { x } ^ { n } v ^ { n } ) + \left( v ^ { n + 1 } \partial _ { t } ^ { + } u ^ { n } \right) _ { x } = - \partial _ { t } ^ { + } ( u _ { x } ^ { n } v ^ { n } ) + \partial _ { x } ( v ^ { n + 1 } ) ^ { 2 } .
$$

Hence the semi-discretized momentum conservation law is given by

$$
\begin{array} { r } { \partial _ { t } ^ { + } ( p ^ { n } v ^ { n } ) - \partial _ { x } \left( 1 - \cos ( u ^ { n } ) - ( v ^ { n + 1 } ) ^ { 2 } / 2 - ( p ^ { n } ) ^ { 2 } / 2 \right) = 0 . } \end{array}
$$

# Preissman box scheme

The Preissman box scheme can be viewed as the space-time version of the implicit midpoint scheme for ODEs and is widely used in hydraulics [1]. The scheme, applied to a multi-symplectic PDE, is given by

$$
\begin{array} { r } { \pmb { K } \partial _ { t } ^ { + } z _ { i + 1 / 2 } ^ { n } + \pmb { L } \partial _ { x } ^ { + } z _ { i } ^ { n + 1 / 2 } = \nabla _ { z } S ( z _ { i + 1 / 2 } ^ { n + 1 / 2 } ) , } \end{array}
$$

where we use the notation

$$
z _ { i } ^ { n + 1 / 2 } = \frac { 1 } { 2 } \left( z _ { i } ^ { n } + z _ { i } ^ { n + 1 } \right) , \qquad z _ { i + 1 / 2 } ^ { n } = \frac { 1 } { 2 } \left( z _ { i } ^ { n } + z _ { i + 1 } ^ { n } \right) ,
$$

and

$$
z _ { i + 1 / 2 } ^ { n + 1 / 2 } = \frac { 1 } { 4 } \left( z _ { i } ^ { n } + z _ { i } ^ { n + 1 } + z _ { i + 1 } ^ { n } + z _ { i + 1 } ^ { n + 1 } \right) .
$$

Example 7 The implicit midpoint method in space applied to the sine-Gordon equation results in

$$
\begin{array} { c } { \displaystyle { - \frac { d } { d t } \frac { v _ { i + 1 } + v _ { i } } { 2 } - \frac { p _ { i + 1 } - p _ { i } } { \Delta x } = \sin \left( \frac { u _ { i + 1 } + u _ { i } } { 2 } \right) , } } \\ { \displaystyle { \frac { d } { d t } \frac { u _ { i + 1 } + u _ { i } } { 2 } = \frac { v _ { i + 1 } + v _ { i } } { 2 } , } } \\ { \displaystyle { \frac { u _ { i + 1 } - u _ { i } } { \Delta x } = - \frac { p _ { i + 1 } + p _ { i } } { 2 } } . } \end{array}
$$

Note that this discretization is different from a midpoint discretization of the Hamiltonian

$$
H = \sum _ { i } \left[ \frac { 1 } { 2 } \left( \frac { v _ { i + 1 } + v _ { i } } { 2 } \right) ^ { 2 } + \frac { 1 } { 2 } \left( \frac { u _ { i + 1 } - u _ { i } } { \Delta x } \right) ^ { 2 } + \left( 1 - \cos \left( \frac { u _ { i + 1 } + u _ { i } } { 2 } \right) \right) \right] \Delta x
$$

and associated Hamiltonian equations of motion

$$
\frac { d } { d t } v _ { i } = - \Delta x ^ { - 1 } \nabla _ { u _ { i } } H , \qquad \frac { d } { d t } u _ { i } = \Delta x ^ { - 1 } \nabla _ { v _ { i } } H .
$$

It was shown by BRIDGES AND REICH [33] that the scheme (12.49) satisfies a discrete conservation law of symplecticness (12.45) with

$$
\omega _ { i } ^ { n } = \frac { 1 } { 2 } d z _ { i + 1 / 2 } ^ { n } \wedge K d z _ { i + 1 / 2 } ^ { n } \quad \mathrm { a n d } \quad \kappa _ { i } ^ { n } = \frac { 1 } { 2 } d z _ { i } ^ { n + 1 / 2 } \wedge L d z _ { i } ^ { n + 1 / 2 } .
$$

Similar to the Euler box scheme, a semi-discretized energy conservation law of type (12.46) can be derived for the spatially discretized system

$$
K \partial _ { t } z _ { i + 1 / 2 } + L \partial _ { x } ^ { + } z _ { i } = \nabla _ { z } S ( z _ { i + 1 / 2 } ) .
$$

In particular, taking the inner product with $\partial _ { t } z _ { i + 1 / 2 }$ , we obtain

$$
\langle \partial _ { t } z _ { i + 1 / 2 } , L \partial _ { x } ^ { + } z _ { i } \rangle = \partial _ { t } S ( z _ { i + 1 / 2 } ) ,
$$

which, after a few formal manipulations, leads to the spatially discrete energy conservation law

$$
\partial _ { t } E _ { i + 1 / 2 } + \partial _ { x } ^ { + } F _ { i } = 0 ,
$$

with

$$
E _ { i + 1 / 2 } = S ( z _ { i + 1 / 2 } ) + \langle \partial _ { x } ^ { + } z _ { i } , L _ { + } z _ { i + 1 / 2 } \rangle ,
$$

and

$$
F _ { i } = - \langle \partial _ { t } z _ { i } , L _ { + } z _ { i } \rangle .
$$

Upon applying the implicit midpoint method to (12.50) in time, the Preissman box scheme is obtained and one can consider the fully discretized energy conservation law

$$
\partial _ { t } ^ { + } E _ { i + 1 / 2 } ^ { n } + \partial _ { x } ^ { + } F _ { i } ^ { n + 1 / 2 } = \mathsf { R } _ { i + 1 / 2 } ^ { n + 1 / 2 } .
$$

The residual Rn+1/2 will be non-zero, in general. However, for a linear multisymplectic PDE

$$
K z _ { t } + L z _ { x } = A z ,
$$

$\pmb { A }$ a (constant) symmetric matrix, the residual is identically equal to zero and

$$
\partial _ { t } ^ { + } E _ { i + 1 / 2 } ^ { n } + \partial _ { x } ^ { + } F _ { i } ^ { n + 1 / 2 } = 0 ,
$$

along numerical solutions $\left\{ z _ { i } ^ { n } \right\}$ , where

$$
\begin{array} { r } { E _ { i + 1 / 2 } ^ { n } = \langle z _ { i + 1 / 2 } ^ { n } , \pm z _ { i + 1 / 2 } ^ { n } \rangle + \langle \partial _ { x } ^ { + } z _ { i } ^ { n } , L _ { + } z _ { i + 1 / 2 } ^ { n } \rangle , } \end{array}
$$

and

$$
F _ { i } ^ { n + 1 / 2 } = - \langle \partial _ { t } ^ { + } z _ { i } ^ { n } , L _ { + } z _ { i } ^ { n + 1 / 2 } \rangle .
$$

A semi-discretized momentum conservation law is derived in a similar manner by switching the roles of space and time. Thus the semi-discrete conservation law

$$
\partial _ { t } ^ { + } M ^ { n } + \partial _ { x } I ^ { n + 1 / 2 } = 0
$$

is obtained, where

$$
M ^ { n } = - \langle \partial _ { x } z ^ { n } , K _ { + } z ^ { n } \rangle ,
$$

and

$$
I ^ { n + 1 / 2 } = S ( z ^ { n + 1 / 2 } ) + \langle \partial _ { t } ^ { + } z ^ { n } , K _ { + } z ^ { n + 1 / 2 } \rangle .
$$

Again, the Preissman box scheme applied to a linear PDE (12.51) yields a fully discretized momentum conservation law

$$
\partial _ { t } ^ { + } M _ { i + 1 / 2 } ^ { n } + \partial _ { x } ^ { + } I _ { i } ^ { n + 1 / 2 } = 0 ,
$$

that is exactly satisfied by the numerical solutions $\left\{ z _ { i } ^ { n } \right\}$ .

See [33, 138] for more details on the energy and momentum conservation properties of the Preissman box scheme. The Preissman box scheme has been successfully applied to the KdV equation and the nonlinear Schr¨odinger equation (see, for example [209, 92]). A generalization to higher-order Gauss–Legendre RK methods has been given by REICH in [162].

Example 8 A Preissman box scheme discretization of the multi-symplectic formulation (12.38)–(12.41) of the KdV equation results in

$$
\begin{array} { r l } & { \quad \partial _ { t } ^ { + } u _ { i + 1 / 2 } ^ { n } + \partial _ { x } ^ { + } p _ { i } ^ { n + 1 / 2 } = 0 , } \\ & { - \partial _ { t } ^ { + } \phi _ { i + 1 / 2 } ^ { n } - 2 \partial _ { x } ^ { + } w _ { i } ^ { n + 1 / 2 } = - p _ { i + 1 / 2 } ^ { n + 1 / 2 } + ( u _ { i + 1 / 2 } ^ { n + 1 / 2 } ) ^ { 2 } , } \\ & { \quad \quad 2 \partial _ { x } ^ { + } u _ { i } ^ { n + 1 / 2 } = 2 w _ { i + 1 / 2 } ^ { n + 1 / 2 } , } \\ & { \quad \quad - \partial _ { x } ^ { + } \phi _ { i } ^ { n + 1 / 2 } = - u _ { i + 1 / 2 } ^ { n + 1 / 2 } . } \end{array}
$$

We assume that initially $\partial _ { x } ^ { + } u _ { i } ^ { 0 } = w _ { i + 1 / 2 } ^ { 0 }$ and $\partial _ { x } ^ { + } \phi _ { i } ^ { 0 } = u _ { i + 1 / 2 } ^ { 0 }$ . Upon collecting all approximations $U _ { j } ^ { n }$ at time-level $t _ { n }$ into a vector $\pmb { u } ^ { n } = \{ u _ { i } ^ { n } \}$ etc. and upon introducing two appropriate matrices $\pmb { A }$ and $D$ , we can rewrite the scheme as

$$
\begin{array} { c } { { \partial _ { t } ^ { + } { \pmb A } { \pmb u } ^ { n } + { \pmb D } { \pmb p } ^ { n + 1 / 2 } = { \bf 0 } , } } \\ { { - \partial _ { t } ^ { + } { \pmb A } \pmb \phi ^ { n } - 2 { \pmb D } { \pmb w } ^ { n + 1 / 2 } = - { \pmb A } { \pmb p } ^ { n + 1 / 2 } + ( { \pmb A } { \pmb u } ^ { n + 1 / 2 } ) * ( { \pmb A } { \pmb u } ^ { n + 1 / 2 } ) , } } \\ { { { \pmb D } { \pmb u } ^ { n } = { \pmb A } { \pmb w } ^ { n } , } } \\ { { { \pmb D } \pmb \phi ^ { n } = { \pmb A } { \pmb u } ^ { n } , } } \end{array}
$$

where $c = a * b$ denotes the component-wise vector product. Note that the averaging operator $\pmb { A }$ and the differentiation operator $D$ commute. We also assume that $\pmb { A }$ is invertible. Hence we can eliminate $\phi ^ { n } , \mathsf { \pmb { p } } ^ { n }$ and $w ^ { n }$ from the system and obtain the timestepping scheme

$$
\frac { \pmb { A } \pmb { u } ^ { n + 1 } - \pmb { A } \pmb { u } ^ { n } } { \Delta t } + \frac { 1 } { 2 } \pmb { A } ^ { - 1 } D \left[ ( \pmb { A } \pmb { u } ^ { n + 1 / 2 } ) * ( \pmb { A } \pmb { u } ^ { n + 1 / 2 } ) \right] + ( \pmb { A } ^ { - 1 } D ) ^ { 3 } \pmb { A } \pmb { u } ^ { n + 1 / 2 } = \pmb { 0 } .
$$

Finally, introduce the variable $\bar { \pmb { u } } ^ { n } = \pmb { A } \pmb { u } ^ { n }$ , then

$$
\frac { \bar { u } ^ { n + 1 } - \bar { u } ^ { n } } { \Delta t } + \frac { 1 } { 2 } A ^ { - 1 } D \left[ ( \bar { u } ^ { n + 1 / 2 } ) * ( \bar { u } ^ { n + 1 / 2 } ) \right] + ( A ^ { - 1 } D ) ^ { 3 } \bar { u } ^ { n + 1 / 2 } = \bf { 0 } .
$$

See [161] for a similar approach to the shallow-water Boussinesq equation.

# Discrete variational methods

The nonlinear wave equation (12.1) can also be derived from a Lagrangian variational principle. Consider the Lagrangian functional

$$
\mathcal { L } [ u ] = \int _ { t = 0 } ^ { T } \int _ { x = 0 } ^ { L } \mathsf { L } ( u _ { t } , u _ { x } , u ) d x d t ,
$$

with the Lagrangian density

$$
\mathsf { L } \bigl ( u _ { t } , u _ { x } , u \bigr ) = \frac { 1 } { 2 } u _ { t } ^ { 2 } - \sigma ( u _ { x } ) - f ( u ) .
$$

Then, using the Lagrangian variational principle, we derive the Euler–Lagrange equation

$$
\partial _ { t } \mathsf { L } _ { u _ { t } } + \partial _ { x } \mathsf { L } _ { u _ { x } } - \mathsf { L } _ { u } = 0 .
$$

For the particular Lagrangian density given above, the Euler–Lagrange equation reduces to the nonlinear wave equation (12.1).

The concept of multi-symplectic integration was first proposed in the context of the Euler–Lagrange equation (12.52) by MARSDEN, PATRICK, AND SHKOLLER [123] as a generalization of the discrete variational principle to first-order field theories.

Introduce, for example, the discrete density

$$
\mathsf { L } _ { i } ^ { n } = \mathsf { L } ( \partial _ { t } ^ { + } u _ { i } ^ { n } , \partial _ { x } ^ { + } u _ { i } ^ { n } , u _ { i } ^ { n } )
$$

and the associated discrete Lagrangian functional

$$
\mathcal { L } [ u _ { i } ^ { n } ] = \sum _ { i } \sum _ { n } \mathsf { L } _ { i } ^ { n } \Delta x \Delta t .
$$

Minimization of this functional along sequences $\left\{ u _ { i } ^ { n } \right\}$ yields the discrete Euler– Lagrange equations

$$
\partial _ { t } ^ { - } \mathsf { L } _ { \partial _ { t } ^ { + } u _ { i } ^ { n } } + \partial _ { x } ^ { - } \mathsf { L } _ { \partial _ { x } ^ { + } u _ { i } ^ { n } } - \mathsf { L } _ { u _ { i } ^ { n } } = 0 .
$$

See MARSDEN, PATRICK, AND SHKOLLER [123] for details on the underlying discrete multi-symplectic form formula and a proper differential geometric treatment.

For the nonlinear wave equation (12.1) and the above discrete Lagrangian density, the discrete variational principle yields the discretization

$$
\frac { u _ { i } ^ { n + 1 } - 2 u _ { i } ^ { n } + u _ { i } ^ { n - 1 } } { \Delta t ^ { 2 } } = \frac { \sigma ^ { \prime } \left( \frac { u _ { i + 1 } ^ { n } - u _ { i } ^ { n } } { \Delta x } \right) - \sigma ^ { \prime } \left( \frac { u _ { i } ^ { n } - u _ { i - 1 } ^ { n } } { \Delta x } \right) } { \Delta x } - f ^ { \prime } ( u _ { i } ^ { n } ) ,
$$

which is equivalent to Euler box scheme discretization applied to the nonlinear wave equation. In fact, the Euler–Lagrange equation (12.52) can be rewritten as a multi-symplectic PDE

$$
\begin{array} { r l } & { \cdot \ : p _ { x } = L _ { u } , } \\ & { u _ { t } = v , } \\ & { u _ { x } = w , } \\ & { \quad 0 = q + L _ { v } , } \\ & { \quad 0 = p + L _ { w } , } \end{array}
$$

and, hence, the variational and the multi-symplectic approach are complementary for first-order field theories, i.e. for Lagrangian densities of the form $\begin{array} { r l } { \mathrm { L } ( u _ { t } , u _ { x } , u ) = } \end{array}$ $\mathsf { L } ( v , w , u )$ .

The discrete variational approach can be generalized to second-order field theories such as the KdV equation. See, for example, [209].

# 12.3.4 Numerical dispersion and soliton solutions

We have seen in Section 12.3.2 that linear multi-symplectic PDEs can be discussed in terms of their dispersion relation. Following the idea of von Neumann stability analysis [140], a numerical dispersion relation can be defined by making the ansatz

$$
z _ { i } ^ { n } = a \mathrm { e } ^ { j ( K x _ { i } - \Omega t _ { n } ) } ,
$$

where $x _ { i } = i \Delta x$ , $t _ { n } = n \Delta t$ , and $j = \sqrt { - 1 }$ . It is easy to derive that, for example,

$$
\begin{array} { c } { { \displaystyle \partial _ { x } ^ { + } z _ { i + 1 / 2 } ^ { n } = \frac { \mathrm { e } ^ { - j \Omega \Delta t / 2 } - \mathrm { e } ^ { j \Omega \Delta t / 2 } } { \Delta t } \frac { \mathrm { e } ^ { j K \Delta x / 2 } + \mathrm { e } ^ { - j K \Delta x / 2 } } { 2 } \bar { z } _ { i + 1 / 2 } ^ { n + 1 / 2 } } } \\ { { = - \displaystyle \frac { 2 j } { \Delta t } \sin ( \Omega \Delta t / 2 ) \cos ( K \Delta x / 2 ) \bar { z } _ { i + 1 / 2 } ^ { n + 1 / 2 } , } } \end{array}
$$

where we used the “exact” midpoint approximation

$$
\bar { z } _ { i + 1 / 2 } ^ { n + 1 / 2 } : = \pmb { a } \mathrm { e } ^ { j ( K x _ { i + 1 / 2 } - \Omega t _ { n + 1 / 2 } ) } ,
$$

$t _ { n + 1 / 2 } = ( n + 1 / 2 ) \Delta t , x _ { i + 1 / 2 } = ( i + 1 / 2 ) \Delta x$ , which should not be confused with the approximation $z _ { i + 1 / 2 } ^ { n + 1 / 2 }$ used in the numerical scheme, i.e.

$$
z _ { i + 1 / 2 } ^ { n + 1 / 2 } = \cos ( \Omega \Delta t / 2 ) \cos ( K \Delta x / 2 ) \bar { z } _ { i + 1 / 2 } ^ { n + 1 / 2 } .
$$

If one substitutes these formulas and the corresponding expression for $\partial _ { x } ^ { + }$ into the Preissman box scheme, then the following linear system appears

$$
\left[ \frac { 2 j } { \Delta t } \tan ( \Omega \Delta t / 2 ) { \cal K } - \frac { 2 j } { \Delta x } \tan ( { \cal K } \Delta x / 2 ) { \cal L } + { \cal A } \right] a = 0 .
$$

This equation leads to the numerical dispersion relation via

$$
\operatorname* { d e t } \left[ \frac { 2 j } { \Delta t } \tan ( \Omega \Delta t / 2 ) { \cal K } - \frac { 2 j } { \Delta x } \tan ( { \cal K } \Delta x / 2 ) { \cal L } + { \cal A } \right] = 0 .
$$

Upon defining

$$
\omega = \frac { 2 } { \Delta t } \tan ( \Omega \Delta t / 2 )
$$

and

$$
k = \frac { 2 } { \Delta x } \tan ( K \Delta x / 2 ) ,
$$

the numerical dispersion relation turns into the analytic relation (12.42) for $k$ and $\omega$ .

The important point is that only wave numbers $\boldsymbol { K }$ with

$$
- \pi < K \Delta x \le \pi
$$

and frequencies $\Omega$ with

$$
- \pi < \Omega \Delta t \leq \pi
$$

are distinguishable in terms of the associated numerical solution $z _ { i } ^ { n }$ . Hence (12.53)–(12.54) can be uniquely solved for $( K , \Omega )$ in terms of $\Delta t \omega$ and $\Delta x k$ , respectively. In other words, the numerical discretization does not introduce any spurious modes. This is a desirable property of the multi-symplectic Preissman box scheme [9, 136].

One should, however, keep in mind that multi-symplectic methods can be subject to resonance instabilities very much like those discussed for large time step (LTS) methods in Chapter 10. The concept of a Krein signature has been generalized to multi-symplectic PDEs by BRIDGES in [30] and has been used to classify instabilities. The same concept could be used to study numerical-induced resonance instabilities similar to what has been outlined in Chapter 10.

We finally conduct a numerical experiment for the sine-Gordon equation over a periodic domain $x \in \left( { - L / 2 , L / 2 } \right]$ , $L = 6 0$ , and initial data

$$
u _ { o } ( x ) = 4 \tan ^ { - 1 } \left( \mathrm { e } ^ { ( x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } \right) + 4 \tan ^ { - 1 } \left( \mathrm { e } ^ { ( - x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } \right) ,
$$

and

$$
v _ { o } ( x ) = { \frac { - 4 c } { \sqrt { 1 - c ^ { 2 } } } } \left[ { \frac { \mathrm { e } ^ { ( x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } { 1 + \mathrm { e } ^ { 2 ( x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } } - { \frac { \mathrm { e } ^ { ( - x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } { 1 + \mathrm { e } ^ { 2 ( - x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } } \right] ,
$$

$c = 0 . 5$ . The solution consists of a pair of kink solitons moving with speed $c = 0 . 5$ in opposite directions which, due to the periodicity of the domain, meet at $x = 0$ and $x = L / 2$ .

We use the Euler box scheme and set the spatial mesh-size to $\Delta x = 0 . 0 1 8 7$ and the timestep to $\Delta t = 0 . 0 1$ . In Figs. 12.3 and 12.4, we plot the numerical errors in the local energy and momentum conservation laws under a soliton collision near $t = 1 0 0$ and $x = 0$ . These errors are defined in terms of fully discretized formulations of the semi-discrete conservation laws (12.29) and (12.48), for example we use formula (12.27) for the energy conservation law. One can clearly see that the errors are concentrated along the moving fronts of the two solitons. The error in energy increases locally whenever the two solitons collide. Interestingly enough this is not the case for the momentum conservation law. This indicates that the larger energy error near collisions is due to numerical timestepping errors in the “pendulum part”

![](images/f1370189f9a4bd8c62de9eb7e6809babc95748c8fb52f2bc86d64c6576ddf576.jpg)  
Figure 12.3 Numerical residual in the energy conservation law.

$$
\begin{array} { r } { u _ { t t } = - \sin ( u ) . } \end{array}
$$

# 12.3.5 Summary

At present the range of applicability and the advantages of classical symplectic methods, as described in Section 12.2, and multi-symplectic methods is an open question. A careful comparison of several methods has been carried out by AS-CHER AND MCLACHLAN [9] for the KdV equation. One should keep in mind that a large number of “classical” symplectic methods are in fact multi-symplectic. Furthermore, whatever method is chosen, it should correctly reflect the important physical quantities on a local discretization level. This is clearly the point of view taken with the multi-symplectic approach with regard to energy and momentum conservation. Other applications might lead to other relevant quantities such as potential vorticity (PV) and hence to other preferable discretization methods. In some cases, such as turbulent fluid flows, one also has to address the problem of numerically unresolved motion on sub-grid length scales. These issues are clearly beyond this exposition. But they would lead into the area of stochastic sub-grid modeling and averaging.

![](images/0934668c9c89dcf7dd3ab97f1feaf55ee72c86a2c42046f04464d0fcc5813ff6.jpg)  
Figure 12.4 Numerical residual in the momentum conservation law.

# 12.4 Exercises

1. Symplectic Euler scheme. Apply the scheme (12.43) to the canonical Hamiltonian

$$
\frac { d } { d t } p = - \nabla _ { \boldsymbol { q } } H ( \boldsymbol { q } , \boldsymbol { p } ) , \qquad \frac { d } { d t } \boldsymbol { q } = + \nabla _ { \boldsymbol { p } } H ( \boldsymbol { q } , \boldsymbol { p } ) ,
$$

with $z = ( q , p ) ^ { T }$ , and

$$
K _ { + } z = { \binom { q } { 0 } } \ .
$$

Show that the scheme preserves the symplectic form

$$
d { \pmb q } ^ { n + 1 } \wedge d { \pmb p } ^ { n } = d { \pmb q } ^ { n } \wedge d { \pmb p } ^ { n - 1 } .
$$

How can the scheme be related to a standard symplectic Euler method?

2. Nonlinear Schr¨odinger equation, Preissman box scheme. Consider complexvalued functions $\psi ( x , t )$ which satisfy the nonlinear Schr¨odinger equation

$$
j \psi _ { t } = \psi _ { x x } + | \psi | ^ { 2 } \psi ,
$$

over the spatial domain $x \in [ 0 , L )$ subject to periodic boundary conditions. We introduce the real part $\boldsymbol { a } ( \boldsymbol { x } , t )$ and the imaginary part $b ( x , t )$ of the wave function, i.e.

$$
\psi ( x , t ) = a ( x , t ) + j b ( x , t ) ,
$$

and rewrite the nonlinear Schr¨odinger equation as

$$
\begin{array} { r } { - b _ { t } = a _ { x x } + ( a ^ { 2 } + b ^ { 2 } ) a , } \\ { a _ { t } = b _ { x x } + ( a ^ { 2 } + b ^ { 2 } ) b . } \end{array}
$$

a. Write (12.55)–(12.56) in multi-symplectic form.

b. Apply the Preissman box scheme to the multi-symplectic formulation derived under (a).

c. The norm of the wave function is a conserved quantity for the nonlinear Schr¨odinger equation, i.e.

$$
\frac { d } { d t } \int _ { 0 } ^ { L } ( a ^ { 2 } + b ^ { 2 } ) d x = 0 .
$$

A discrete analog of this conservation law is

$$
\sum _ { i } \left[ ( a _ { i + 1 / 2 } ^ { n } ) ^ { 2 } + ( b _ { i + 1 / 2 } ^ { n } ) ^ { 2 } \right] = \sum _ { i } \left[ ( a _ { i + 1 / 2 } ^ { n + 1 } ) ^ { 2 } + ( b _ { i + 1 / 2 } ^ { n + 1 } ) ^ { 2 } \right] .
$$

Does this identity hold for the multi-symplectic scheme derived under (b)?

3. Sine-Gordon equation, energy-momentum conservation. Implement the Euler box scheme for the sine-Gordon equation over a periodic domain $x \in$ $( - L / 2 , L / 2 ]$ , $L = 6 0$ , and initial data

$$
u _ { o } ( x ) = 4 \tan ^ { - 1 } \left( \mathrm { e } ^ { ( x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } \right) + 4 \tan ^ { - 1 } \left( \mathrm { e } ^ { ( - x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } \right)
$$

and

$$
v _ { o } ( x ) = { \frac { - 4 c } { \sqrt { 1 - c ^ { 2 } } } } \left[ { \frac { \mathrm { e } ^ { ( x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } { 1 + \mathrm { e } ^ { 2 ( x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } } - { \frac { \mathrm { e } ^ { ( - x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } { 1 + \mathrm { e } ^ { 2 ( - x - L / 4 ) / \sqrt { 1 - c ^ { 2 } } } } } \right] ,
$$

with wave speed $c = 0 . 5$ .

a. Compute the numerical solution over a time-interval [0, 200] using a stepsize of $\Delta t = 0 . 0 1$ and a spatial mesh-size of $\Delta x = L / 3 2 0 0$ .   
b. Implement formula (12.27) into your scheme to monitor the residual in the energy conservation law. You should reproduce the results from Fig. 12.3.   
c. Find the analog of (12.27) for the momentum conservation law. Implement the formula into your scheme and monitor the residual in the discrete momentum conservation law.

4. Dispersion relation. Consider the linear advection equation

$$
{ \cal U } _ { t } + { \cal U } _ { X } = 0 .
$$

We introduce the velocity potential $\boldsymbol { u } = \boldsymbol { \phi } _ { x }$ and write the advection equation in the multi-symplectic form

$$
u _ { t } + w _ { x } = 0 , \quad - \phi _ { t } = - w + 2 u , \quad - \phi _ { x } = - u .
$$

a. Find the linear dispersion relation for the formulation (12.57).

b. Apply the Preissman box scheme to the multi-symplectic formulation (12.57). Discuss the associated numerical dispersion relations. Verify the result from Fig. 12.5.   
c. Compare the results from (b) with a direct application of the box scheme to the linear advection equation.   
d. The advection equation is an example of a noncanonical Hamiltonian system with Poisson operator $\mathcal { I } = - \partial _ { x }$ and Hamiltonian $\textstyle { \mathcal { H } } = \int u ^ { 2 } / 2 d x$ . Does the direct application of the box scheme to the linear wave equation lead to a “classical” symplectic method?

5. KdV and Schr¨odinger equation, mixed multi-symplectic discretization. Besides the two box schemes discussed in this chapter so far, another useful class of multi-symplectic methods can be obtained by applying the symplectic Euler scheme (12.43) in space and the implicit midpoint method in time.

![](images/0fb1a160223474278f521eff440729382ee6b093868ecf731c77a8eac5bfad7c.jpg)  
Figure 12.5 Numerical dispersion relation for Preissman box scheme applied to (12.57) and a Courant number $c = \Delta t / \Delta x = 1 0$ . We also plot the exact dispersion relation (’o’) for comparison.

a. What scheme do you obtain when applying this discretization to the multi-symplectic KdV formulation (12.38)–(12.41)? Show that, in terms of the variable $u$ , the scheme is equivalent to

$$
\partial _ { t } ^ { + } u _ { i + 1 / 2 } ^ { n } + \frac { 1 } { 2 } \partial _ { x } ^ { + } ( u _ { i } ^ { n + 1 / 2 } ) ^ { 2 } + \partial _ { x } ^ { + } \partial _ { x } ^ { - } \partial _ { x } ^ { + } u _ { i } ^ { n + 1 / 2 } = 0 .
$$

b. Discuss the dispersion relation of the linear KdV scheme

$$
\partial _ { t } ^ { + } u _ { i + 1 / 2 } ^ { n } + \partial _ { x } ^ { + } u _ { i } ^ { n + 1 / 2 } + \partial _ { x } ^ { + } \partial _ { x } ^ { - } \partial _ { x } ^ { + } u _ { i } ^ { n + 1 / 2 } = 0 .
$$

c. Apply the same space-time discretization to the nonlinear Schr¨odinger equations (12.55)–(12.56). Compare the scheme with the Preissman box scheme discretization of the same equations in terms of conservation properties and computational complexity.

6. Modified equation analysis. Application of the Euler box scheme to a multisymplectic PDE results in the discrete formula

$$
\begin{array} { r } { K _ { + } \partial _ { t } ^ { + } z _ { i } ^ { n } + K _ { - } \partial _ { t } ^ { - } z _ { i } ^ { n } + L _ { + } \partial _ { x } ^ { + } z _ { i } ^ { n } + L _ { - } \partial _ { x } ^ { - } z _ { i } ^ { n } = \nabla _ { z } S ( z _ { i } ^ { n } ) . } \end{array}
$$

Performing standard Taylor expansions, we find that

$$
\partial _ { t } ^ { + } z ( x _ { i } , t _ { n } ) = z _ { t } ( x _ { i } , t _ { n } ) + \frac { \Delta t } { 2 } z _ { t t } ( x _ { i } , t _ { n } ) + \mathcal { O } ( \Delta t ^ { 2 } )
$$

and similar terms for the other discrete derivative approximations.

a. Let us drop all terms of order $\mathcal { O } ( \Delta t ^ { 2 } , \Delta x ^ { 2 } )$ and higher in the Taylor expansions for the discrete derivatives. Verify that, following standard local error analysis, the Euler box scheme becomes formally equivalent to the modified PDE

$$
K z _ { t } + \frac { \Delta t } { 2 } A z _ { t t } + L z _ { x } + \frac { \Delta x } { 2 } B z _ { x x } = \nabla _ { z } S ( z ) ,
$$

where

$$
A = K _ { + } - K _ { - } , \qquad B = L _ { + } - L _ { - }
$$

are both symmetric matrices.

b. Write (12.58) as a multi-symplectic PDE over some enlarged phase space.

c. Use the multi-symplectic formulation, derived under (b), to find modified energy and momentum conservation laws. Note that these conservation laws can also be obtained by direct manipulation of the modified equation (12.58).

d. Show that (12.58) is the Euler–Lagrange equation arising from a Lagrangian functional $\mathcal { L }$ with density $L \left( z , z _ { t } , z _ { x } , z _ { t t } , z _ { x x } \right)$ . Find the specific form of $L$ .

e. The modified conservation laws, derived under (c), are satisfied by the Euler box scheme to second-order accuracy. What needs to be done to derive modified conservation laws that are satisfied to third-order by the Euler box scheme?

See [137, 138] for more details.

# References

[1] M.B. Abbott and D.R. Basco. Computational Fluid Dynamics. Harlow, Essex: Longman Scientific & Technical, 1989.   
[2] R. Abraham and J.E. Marsden. Foundations of Mechanics. Reading, MA: Benjamin Cummings Pub. Co. 2nd edition, 1978.   
[3] B.J. Alder and T.E. Wainwright. Hard-sphere molecular dynamics. J. Chem. Phys., 27:1208–1209, 1957.   
[4] M.P. Allen and D.J. Tildesley. Computer Simulation of Liquids. Oxford: Clarendon Press, 1987.   
[5] H.C. Andersen. Rattle: a “velocity” version of the Shake algorithm for molecular dynamics calculations. J. Comput. Phys., 52:24–34, 1983.   
[6] D.G. Andrews. An Introduction to Atmospheric Physics. Cambridge: Cambridge University Press, 2000.   
[7] V.I. Arnold. Mathematical Methods of Classical Mechanics. New York: Springer-Verlag, 2nd edition, 1989.   
[8] V.I. Arnold, V.V. Kozlov, and A.I. Neishtadt. Mathematical Aspects of Classical and Celestial Mechanics. Berlin Heidelberg: Springer-Verlag, 2nd edition, 1993.   
[9] U. Ascher and R.I. McLachlan. Multisymplectic box schemes and the Korteweg-de Vries equation. Appl. Numer. Math., 48:255–269, 2004.   
[10] U.M. Ascher, H. Chin, and S. Reich. Stablization of DAEs and invariant manifolds. Numer. Math., 67:131–149, 1994.   
[11] K. Atkinson. Elementary Numerical Analysis. New York: John Wiley & Sons, 1985.   
[12] S.P. Auerbach and A. Friedman. Long-time behavior of numerically computed orbits: small and intermediate timestep analysis of one-dimensional systems. J. Comput. Phys., 93:189–223, 1991.   
[13] E. Barth, K. Kuczera, B. Leimkuhler, and R.D. Skeel. Algorithms for constrained molecular dynamics. J. Comput. Chem., 16:1192–1209, 1995.   
[14] E. Barth, B. Laird, and B. Leimkuhler. Generating generalized distributions from dynamical simulation. J. Chem. Phys., 118:5759–5768, 2003.   
[15] E. Barth and B. Leimkuhler. Symplectic methods for conservative multibody systems. In J.E. Mardsen, G.W. Patrick, and W.F. Shadwick, editors, Integration Algorithms and Classical Mechanics, volume 10 of Fields Inst. Comm., pages 25–44. Amer. Math. Soc., 1996.   
[16] G. Benettin and A. Giorgilli. On the Hamiltonian interpolation of near to the identity symplectic mappings with application to symplectic integration algorithms. J. Stat. Phys., 74:1117–1143, 1994.   
[17] G. Benettin, A. M. Cherubini, and F. Fass\`o. A changing charts symplectic algorithm for rigid bodies and other dynamical systems on manifolds. SIAM J. Sci. Comput., 23:1189–1203, 2001.   
[18] G. Benettin, L. Galgani, and A. Giorgilli. Realization of holonomic constraints and freezing of high frequency degrees of freedom in the light of classical perturbation theory. Part I. Comm. Math. Phys., 113:87–103, 1987.   
[19] F. Benvenuto, G. Casati, and D. Shepelyansky. Dynamical localization: Hydrogen atom in magnetic and microwave fields. Phys. Rev. A, 55:1732–1735, 1997.   
[20] J.J. Biesiadecki and R.D. Skeel. Dangers of multiple-time-step methods. J. Comput. Phys., 109:318–328, 1993.   
[21] C.K. Birdsall and A.B. Langdon. Plasma Physics via Computer Simulations. New York: McGraw-Hill, 1981.   
[22] S. Blanes. High order numerical integrators for differential equations using composition and processing of low order methods. Appl. Numer. Math., 37:289–306, 2001.   
[35] R.C. Buck. Advanced Calculus. New York: McGraw-Hill, 3rd edition, 1978.   
[36] C. Budd, B. Leimkuhler, and M. Piggott. Scaling invariance and adaptivity. Appl. Numer. Math., 39:261–288, 2001.   
[37] R. Burden and J. Faires. Numerical Analysis. Brooks Cole Publishing, 7th edition, 2001.   
[38] S.R. Buss. Accurate and efficient simulation of rigid body rotations. J. Comput. Phys., 164:377–406, 2000.   
[39] J.C. Butcher. Numerical Methods for Ordinary Differential Equations. New York: John Wiley & Sons, 2003.   
[40] M.P. Calvo, A. Murua, and J.M. Sanz-Serna. Modified equations for ODEs. Contemp. Math., 172:63–74, 1994.   
[41] M.P. Calvo and A. Portillo. Are higher order equistage initializers better than standard starting algorithms? J. Comput. Appl. Math, 169:333– 344, 2004.   
[42] M.P. Calvo and J.M. Sanz-Serna. Variable steps for symplectic integrators. In Dundee Conference on Numerial Analysis 1991, volume 260 of Pitman Res. Notes Math. Ser., pages 34–48. Pitman, London, 1992.   
[43] P.J. Channel. Symplectic integration algorithms. Technical Report AT-6:ATN 83–9, Los Alamos National Laboratory, 1983.   
[44] P.J. Channel and J.S. Scovel. Integrators for Lie–Poisson dynamical systems. Physica D, 50:80–88, 1991.   
[45] S. Cirilli, E. Hairer, and B. Leimkuhler. Asymptotic error analysis of the Adaptive Verlet method. BIT, 39:25–33, 1999.   
[46] G.J. Cooper. Stability of Runge–Kutta methods for trajectory problems. IMA J. Numer. Anal., 7:1–13, 1987.   
[47] C.J. Cotter and S. Reich. Adiabatic invariance and applications to molecular dynamics and numerical weather prediction. BIT, to appear.   
[48] G. Dahlquist and A. Bj¨ork. Numerical Methods. Englewood Cliffs, NJ: Prentice-Hall, 1974.   
[49] R. de Vogelaere. Methods of integration which preserve the contact transformation property of the Hamiltonian equations. Technical Report 4, Dept. Math. Univ. of Notre Dame, 1956.   
[50] P.A.M. Dirac. Lectures on Quantum Mechanics. Technical Report 3, Belfer Graduate School Monographs, Yeshiva University, 1964.   
[51] A.J. Dragt and J.M. Finn. Lie series and invariant functions for analytic symplectic maps. J. Math. Phys., 17:2215–2227, 1976.   
[52] A.J. Dragt, F. Neri, G. Rangarajan, D.R. Douglas, L.M. Healy, and R.D. Ryne. Lie algebraic treatment of linear and nonlinear beam dynamics. Ann. Rev. Nucl. Part. Sci., 38:455–496, 1988.   
[53] P.G. Drazin. Solitons, volume 85 of London Mathematical Society Lecture Note Series. Cambridge: Cambridge University Press, 1983.   
[54] A. Dullweber, B. Leimkuhler, and R.I. McLachlan. Split-Hamiltonian methods for rigid body molecular dynamics. J. Chem. Phys., 107:5840– 5851, 1997.   
[55] D.R. Durran. Numerical Methods for Wave Equations in Geophysical Fluid Dynamics. Berlin: Springer-Verlag, 1998.   
[56] F. Fass\`o. Comparison of splitting algorithms for the rigid body. J. Comput. Phys., 189:527–538, 2003.   
[57] K. Feng. On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58, Beijing: Science Press, 1985.   
[58] K. Feng. Canonical difference schemes for Hamiltonian canonical differential equations. In International Workshop on Applied Differential Equations (Beijing, 1985), pages 59–73, Singapore: World Sci. Publishing, 1986.   
[59] K. Feng. Formal power series and numerical algorithms for dynamical systems. In T. Chan and Chong-Ci Shi, editors, Proceedings of International Conference on Scientific Computation (Hangzhao, China), volume 1 of Series on Appl. Math., pages 28–35, 1991.   
[60] E. Fermi, J. Pasta, and S. Ulam. Studies of nonlinear problems-I. Technical Report LA-1940, Los Alamos National Laboratory, Los Alamos, NM, 1955.   
[61] M. Fixman. Classical statistical mechanics of constraints: a theorem and applications to polymers. Proc. Nat. Acad. Sci., 71:3050–3053, 1974.   
[62] E. Forest and R.D. Ruth. Fourth order symplectic integration. Physica D, 43:105–117, 1990.   
[63] J. Frank, G. Gottwald, and S. Reich. The Hamiltonian particle-mesh method. In M. Griebel and M.A. Schweitzer, editors, Meshfree Methods for Partial Differential Equations, volume 26 of Lect. Notes Comput. Sci. Eng., pages 131–142, Berlin Heidelberg: Springer-Verlag, 2002.   
[64] J. Frank and S. Reich. Conservation properties of Smoothed Particle Hydrodynamics applied to the shallow-water equations. BIT, 43:40–54, 2003.   
[65] J. Frank and S. Reich. The Hamiltonian particle-mesh method for the spherical shallow water equations. Atmos. Sci. Lett., 5:89–95, 2004.   
[66] D. Frenkel and B. Smit. Understanding Molecular Simulation: From Algorithms to Applications. New York: Academic Press, 2nd edition, 2002.   
[67] B. Garc´ıa-Archilla, J.M. Sanz-Serna, and R.D. Skeel. The mollified impulse method for oscillatory differential equations. SIAM J. Sci. Comput., 20:930–963, 1998.   
[68] Z. Ge. Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, 1991.   
[69] Z. Ge and J. Marsden. Lie–Poisson integrators and Lie–Poisson Hamiltonian–Jacobi theory. Phys. Lett. A, 133:134–139, 1988.   
[70] C.W. Gear. Numerical Initial Value Problems in Ordinary Differential Equations. Englewood Cliffs, NJ: Prentice-Hall, 1971.   
[71] R.A. Gingold and J.J. Monaghan. Smoothed Particle Hydrodynamics: theory and application to non-spherical stars. Mon. Not. R. Astr. Soc., 181:375–389, 1977.   
[72] B. Gladman, M. Duncan, and J. Candy. Symplectic integrators for longterm integration in celestial mechanics. Celest. Mech., 52:221–240, 1991.   
[73] H. Goldstein, C. Pole, and J. Safko. Classical Mechanics. San Francisco, CA: Addison Wesley, 3nd edition, 2002.   
[74] O. Gonzalez, D.J. Higham, and A.M. Stuart. Qualitative properties of modified equations. IMA J. Numer. Anal., 19:169–190, 1999.

[89] W. Huang and B. Leimkuhler. The adaptive Verlet method. SIAM J. Sci. Comput., 18:239–256, 1997.   
[90] P. Hut, J. Makino, and S. McMillan. Building a better leapfrog. Astrophys. J. Lett., 443:L93–L96, 1995.   
[91] A. Iserles. A First Course in the Numerical Analysis of Differential Equations. Cambridge: Cambridge University Press, 1996.   
[92] A.L. Islas, D.A. Karpeev, and C.M. Schober. Geometric integrators for the nonlinear Schr¨odinger equation. J. Comput. Phys., 173:116–148, 2001.   
[93] J.A. Izaguirre, S. Reich, and R.D. Skeel. Longer time steps for molecular dynamics. J. Chem. Phys., 110:9853–9864, 1999.   
[94] S. Jang and G.A. Madden. Simple reversible molecular dynamics algorithms for Nos´e–Hoover chain dynamics. J. Chem. Phys., 107:9514– 9526, 1997.   
[95] L.O. Jay. Runge–Kutta type methods for index three differentialalgebraic equations with applications to Hamiltonian systems. Ph.D. thesis, Department of Mathematics, University of Geneva, Switzerland, 1994.   
[96] S. Jim´enez. Derivation of the discrete conservation laws for a family of finite difference schemes. Appl. Math. Comput., 64:13–45, 1994.   
[97] W. Kahan and R.C. Li. Composition constants for raising the order of unconventional schemes for ordinary differential equations. Math. Comp., 66:1089–1099, 1997.   
[98] A. Kol, B. Laird, and B. Leimkuhler. A symplectic method for rigid-body molecular simulation. J. Chem. Phys., 107:2580–2588, 1997.   
[99] F. Krogh. Issues in the design of a multistep code. Annals of Numer. Math., 1:423–437, 1994.   
[100] S. Kuksin and J. P¨oschel. On the inclusion of analytic symplectic maps in analytic Hamiltonian flows and its applications. In S. Kuksin, V. Lazutkin, and J. P¨oschel, editors, Seminar on Dynamical Systems (St. Petersburg, 1991), volume 12 of Progr. Nonlinear Differential Equations Appl., pages 96–116, Basel: Birkh¨auser Verlag, 1994.   
[101] A. Kværnø and B. Leimkuhler. A time-reversible, regularized, switching integrator for the $n$ -body problem. SIAM J. Sci. Comput., 22:1016– 1035, 2001.   
[102] B. Laird and B. Leimkuhler. Generalized dynamical thermostatting technique. Phys. Rev. E, 68:art. no. 016704, 2003.   
[103] P. Lancaster. Theory of Matrices. New York: Academic Press, 1969.   
[104] C. Lanczos. The Variational Principles of Mechanics. Toronto: University of Toronto Press, 1949.   
[105] L.D. Landau and E.M. Lifshitz. Course in Theoretical Physics, Vol. 1: Mechanics. Oxford: Pergamon Press, 1976.   
[106] F.M. Lasagni. Canonical Runge–Kutta methods. Z. Angew. Math. Phys., 39:952–953, 1988.   
[107] F.M. Lasagni. Integration methods for Hamiltonian differential equations. Unpublished manuscript, 1990.   
[108] E. Lee, A. Brunello, and D. Farrelly. Coherent states in a Rydberg atom: classical mechanics. Phys. Rev. A, 55:2203–2221, 1997.   
[109] B. Leimkuhler. Reversible adaptive regularization: perturbed Kepler motion and classical atomic trajectories. Philos. T. Roy. Soc. A, 357:1101– 1133, 1999.   
[110] B. Leimkuhler. A separated form of Nos´e dynamics for constant temperature and pressure simulation. Comput. Phys. Comm., 148:206–213, 2002.   
[111] B. Leimkuhler and S. Reich. Symplectic integration of constrained Hamiltonian systems. Math. Comp., 63:589–606, 1994.   
[112] B. Leimkuhler and S. Reich. A reversible averaging integrator for multiple time-scale dynamics. J. Comput. Phys., 171:95–114, 2001.   
[113] B. Leimkuhler and R.D. Skeel. Symplectic numerical integrators in constrained Hamiltonian systems. J. Comput. Phys., 112:117–125, 1994.   
[113a] B. Leimkuhler and C. Sweet. The canonical ensemble via symplectic integrators using ´e and ´e-Poincar´e chains. J. Chem. Phys. 121:106–116, 2004a.

[152] D.C. Rappaport. The Art of Molecular Dynamics Simulation. New York: Cambridge University Press, 1995.

153] S. Reich. Numerical integration of the generalized Euler equation. Technical Report TR 93-20, University of British Columbia, 1993.

S. Reich. Momentum conserving symplectic integrators. Physica D, 76:375–383, 1994.

S. Reich. Symplectic integration of constrained Hamiltonian systems by composition methods. SIAM J. Numer. Anal., 33:475–491, 1996.

[156] S. Reich. Symplectic methods for conservative multibody systems. In J.E. Mardsen, G.W. Patrick, and W.F. Shadwick, editors, Integration Algorithms and Classical Mechanics, volume 10 of Fields Inst. Com., pages 181–192. Amer. Math. Soc., 1996.

[157] S. Reich. On higher-order semi-explicit symplectic partitioned Runge– Kutta methods for constrained Hamiltonian systems. Numer. Math., 76:249–263, 1997.

58] S. Reich. Backward error analysis for numerical integrators. SIAM J. Numer. Anal., 36:475–491, 1999.

S. Reich. Conservation of adiabatic invariants under symplectic discretization. Appl. Numer. Math., 29:45–55, 1999.

S. Reich. Multiple times-scales in classical and quantum-classical molecular dynamics. J. Comput. Phys., 151:49–73, 1999.

S. Reich. Finite volume methods for multi-symplectic PDEs. BIT, 40:559–582, 2000.

S. Reich. Multi-symplectic Runge–Kutta collocation methods for Hamiltonian wave equations. J. Comput. Phys., 157:473–499, 2000.

S. Reich. Smoothed Langevin dynamics of highly oscillatory systems.   
Physica D, 138:210–224, 2000. E.J. Routh. Dynamics of a System of Rigid Bodies, Elementary Part.   
New York: Dover, 7th edition, 1960.

[165] H. Rubin and P. Ungar. Motion under a strong constraining force. Comm. Pure and Appl. Math., 10:65–87, 1957.

[166] R.D. Ruth. A canonical integration technique. IEEE Trans. Nucl. Sci., 30:2669–2671, 1983.   
[167] J.P. Ryckaert, G. Ciccotti, and H.J.C. Berendsen. Numerical integration of the cartesian equations of motion of a system with constraints: molecular dynamics of n-alkanes. J. Comput. Phys., 23:327–341, 1977.   
[168] R. Salmon. Practical use of Hamilton’s principle. J. Fluid Mech., 132:431–444, 1983.   
[169] R. Salmon. Lectures on Geophysical Fluid Dynamics. Oxford: Oxford University Press, 1999.   
[170] J.M. Sanz-Serna. Runge–Kutta schemes for Hamiltonian systems. BIT, 28:877–883, 1988.   
[171] J.M. Sanz-Serna. Symplectic integrators for Hamiltonian problems: an overview. Acta Numerica, 1:243–286, 1992.   
[172] J.M. Sanz-Serna and M.P. Calvo. Numerical Hamiltonian Problems. London: Chapman & Hall, 1994.   
[173] T. Sauer and J.A. York. Rigorous verification of trajectories for the computer simulation of dynamical systems. Nonlinearity, 4:961–979, 1994.   
[174] T. Schlick. Molecular Modeling and Simulation. New York: Springer-Verlag, 2002.   
[175] M. Shimada and H. Yoshida. Long-term conservation of adiabatic invariants by using symplectic integrators. Publ. Astron. Soc. Japan, 48:147– 155, 1996.   
[176] R.D. Skeel and C.W. Gear. Does variable step size ruin a symplectic integrator? Physica D, 60:311–313, 1992.   
[177] R.D. Skeel and D.J. Hardy. Practical construciton of modified Hamiltonians. SIAM J. Sci. Comput., 23:1172–1188, 2001.   
[178] D. Stoffer. On reversible and canonical integration methods. Technical Report SAM-Report No. 88-05, ETH Z¨urich, 1988.   
[179] D. Stoffer. Variable steps for reversible integration methods. Computing, 55:1–22, 1995.

[207] L.-S. Young. Large deviations in dynamical systems. Trans. Amer. Math. Soc., 318:525–543, 1990.

[208] V. Zeitlin. Finite-mode analogs of 2D ideal hydordynamcis: coadjoint orbits and local canonical structure. Physica D, 49:353–362, 1991.

[209] P.-F. Zhao and M.-Z. Qin. Multisymplectic geometry and multisymplectic Preissman scheme for the KdV equation. J. Phys. A, 33:3613–3626, 2000.

# Index

accuracy, 12, 105   
action integral, Euler–Lagrange equation,   
43   
adaptive integration, 234   
Adaptive Verlet method, 245   
adiabatic invariant, 106, 126, 264   
adjoint method, 84   
AKMA, 291   
AMBER, 291   
angular momentum, 46, 47, 66, 68, 88   
conservation of for an $n$ -body system, 48   
angular velocity, 211   
anharmonic oscillator, 40   
arclength parameterization, 246   
Arenstorf orbit, 161, 166   
Argon, 288   
asymptotic expansion, 118   
asymptotic stability, 27, 28   
autonomous Hamiltonian system, 39   
averaging, 126, 257, 264, 269, 272, 277

backward error analysis, 106, 235, 260 non-autonomous, 260, 280   
backward error analysis, for Adaptive Verlet, 249   
Baker–Campbell–Hausdorff formula, 134, 146   
bead-on-wire, 8, 10   
Blanes and Moan, higher-order methods of, 146   
body angular momentum, 211   
Boltzmann constant, 298

canonical ensemble, 297   
canonical Hamiltonian system, 38   
canonical lift transformation, 65   
canonical point transformation, 54   
canonical property (see also symplectic   
property), 53   
canonical structure matrix, 38   
canonical transformation, 68   
canonical transformation (see also   
symplectic transformation), 67   
Cayley–Klein parameters, 200   
celestial mechanics, 3, 4, 257   
central forces, 42, 43, 47, 67, 68   
chaotic dynamics, ix, 4, 12, 124   
CHARMM, 291   
charts of a manifold, 58, 191   
commutator of vector fields, 135   
commuting flow maps, 100   
composition methods, 76, 144, 166   
for rigid body motion, 217   
symmetric, 147   
configuration manifold, 170   
conjugate momenta, 43   
conservation of volume, 36   
of a Hamiltonian flow map, 55   
symplecticness vs., 55   
conservative systems, 3   
conserved quantity, see first integral   
constant of motion, see first integral   
constant pressure, 297   
constrained dynamics, 6, 169   
constrained formulation of rigid body mo  
tion, 201   
constrained Hamiltonian system, 39   
constrained numerical methods, 173   
constraint chain, 198   
constraint force, 7   
coordinate charts, 58   
Coulomb systems, 247   
critical point, 3, 41   
cross product, xiv   
D’Alembert’s Principle, 7, 170   
degree of freedom, 3   
diagonalizable matrix, 31   
diffeomorphism, 50   
differential, 61   
differential one-form, 61   
diffusion coefficient, 298   
Dirac theory of constraints, 186   
directional derivative, 61   
discrete variational methods, 168   
Diva, 142   
dot product, xiv   
double well potential, 303

eccentric orbits, 234   
eigenvalues, 28, 282 of a linear Hamiltonian system, 40 of a numerical method, 30, 258   
electron motion, 42   
energy conservation of, 3, 120, 141 of a Hamiltonian system, 37 of a mechanical system, 3 potential, 2   
energy drift, 24, 268   
energy functional, 5   
equilibration, 289   
equilibrium point, 3, 41, 67   
ergodicity, 293, 297   
error global, 17 local, 15 local propagation formula, 18   
error analysis, 15   
error bound, 21 for Euler’s method, 17   
error bounds for one-step methods, 18   
error estimate, 235, 242   
Euler, 12   
Euler angles, 199   
Euler equations, 200, 213 symplectic discretization of, 217   
Euler’s method, 14, 15, 27, 28, 32, 35 local error of, 16   
Euler-A, 26, 33, 35 for a general Hamiltonian system, 74 symplecticness of, 74, 99   
Euler-B, 26, 32, 33, 35, 70, 72, 100 as a splitting method, 80 for a general canonical Hamiltonian sy tem, 74 symplecticness of, 74

Euler–Lagrange equations, 8   
exponential growth, 28

fast modes, 32, 257, 261   
fast multipole method, 290   
Fermi–Pasta–Ulam problem, 99, 100   
first integrals, 38, 44, 106 conservation by numerical methods, 87 conservation of by numerical methods, 157 preservation of, 91 usefulness of, 48   
fixed-point iteration for Runge–Kutta methods, 155   
Floquet theory, 52   
flow map, 11, 36, 48, 50, 52 existence of for smooth Hamiltonians, 50 group property of, 34 operation on sets of points, 50   
fourth-order Runge–Kutta method, 23   
Gauss–Legendre Runge–Kutta methods, 151   
generalized baths, 308   
generalized ensembles, 311   
generalized Hamiltonian system, 38   
generalized leapfrog method, 156, 243   
generating functions, 126, 159, 167 and backward error analysis, 160, 168 and symplectic methods, 167   
geometric integrators, ix modified equations and, 129 accuracy v. efficiency of, 142 properties of, 105   
geometric property, 36, 45   
geophysical fluids, 320, 335 global circulation, 335 particle methods, 332   
global error, 17   
gradient, xv   
gravitational dynamics, 3, 4, 42, 98, 161, 236   
GROMACS, 291   
group property of the flow map, 34, 49   
growth factor, 106

H´enon map, 53 symplecticness of, 53 Hamilton–Jacobi equation, 160, 167

Hamiltonian matrix, 39   
Hamiltonian PDEs, 316 KdV equation, 325 sine-Gordon equation, 320, 353 noncanonical formulation, 324 Schr¨odinger equation, 353   
Hamiltonian system, 1, 36–38 with constraints, 184   
hard sphere model, 288   
harmonic oscillator, 27, 39, 49, 70 flow map of, 50   
Hessian matrix, 244   
high-frequency components, 32, 257, 261   
higher-order methods, 20, 142, 144 by composition, 144 for constrained dynamics, 190   
holonomic constraint, 169   
hyperbolic differential equation, 124   
identity map, 48   
impact oscillator, 239, 246   
implicit Euler method, 14 local error of, 16   
Implicit midpoint method, 14, 75, 151 local error of, 16 preserves quadratic first integrals, 91 symplecticness of, 76   
inertia tensor, 211   
inner product, xiv   
integrable Hamiltonian system, 47   
integral invariants, 55   
integral preservation symplecticness v., 73   
integrator, ix   
isothermal potential, 302

J, canonical structure matrix, 38 Jacobian matrix, xiv

Kahan and Li, high-order method of, 148   
KAM theorem, 2   
Kepler problem, 42, 47, 67, 99, 234, 247 backward error analysis for, 140 conserved quantities of, 46   
kinetic energy of rigid body rotation, 202 of rigid body translation, 202   
Lagrangian function, 168   
Lagrangian top, 219   
Langevin dynamics, 299   
large timestep methods, 257, 276, 271, 280   
leapfrog method, 26 generalized, 156   
Legendre transformation, 185   
Lennard–Jones oscillator, 18, 40, 41, 70 fourth-order Runge–Kutta method applied to, 23, 24 Euler’s method applied to, 19   
Lennard–Jones potential, 4, 91, 288   
Lie derivative, 141   
Lie group, 200   
Lie–Poisson bracket, 214   
Lie–Poisson system, 214   
linear Hamiltonian system, 39, 49, 52 eigenvalues of, 40   
linear momentum, 37, 48, 88   
linear system, 30, 33, 49 with constraints, 196   
linear/nonlinear splitting, 99   
Liouville’s Theorem, 55   
Lipschitz condition, 17 for a numerical method, 21   
Lobatto Runge–Kutta methods, 151   
Lobatto-IIIA–IIIB methods, 157 for constrained dynamics, 190   
local charts, 191   
local error, 15   
long-range force, 4   
Lorenz, 105   
magnetic field angular momentum and, 67 canonical Hamiltonian for, 104 motion in, 42 motion in a, 94 reversing symmetry and, 103 symplectic method for, 95   
magnetic momentum, 96   
Maple, xiii   
mass tensor, 203   
Mathematica, xiii   
MATLAB, xiii   
matrix exponential, 49   
McLachlan’s symmetric composition methods, 148   
MD, 287   
mechanical system, 169   
Methane model, 313   
microcanonical ensemble, 296   
modified equations, 108, 129, 355 for symmetric methods, 139   
modified Hamiltonians, for higher-order methods, 168   
molecular dynamics, 4–6, 23, 48, 91, 105, 257, 287 software for, 291   
molecular dynamics potentials, 292   
momentum constraint, 186   
Monte-Carlo, 287   
Morse oscillator, 9, 35   
multi–symplectic discretizations Preissman box scheme, 344   
multi-symplectic discretizations, 341 discrete conservation laws, 342, 345 discrete variational methods, 347 Euler box scheme, 342 numerical dispersion, 349   
multi-symplectic PDEs, 335 discretization, 341 solitons, 339 conservation laws, 337   
multiple pendulum, 171   
multiple timestepping, 257, 261 Equilibrium, 280, 285 impulse method, 263 mollified impulse method (MOLLY), 276, 283 reversible averaging (RA), 271   
multistep methods, 13, 142   
N-body problem, 2, 3, 287 angular momentum of, 88 applications of, 3 Hamiltonian for, 44 linear momentum of, 88 momentum conservation for, 67 on the sphere, 178   
NAMD, 291   
near-earth objects, 143   
neighbor list, 289   
Newton iteration, 244   
Newton’s equations, 2, 37, 52 discretization of, 15 Hamiltonian form of, 37   
non-autonomous Hamiltonian system, 39, 102   
non-separable Hamiltonian systems, 150, 157   
nonlinear oscillator, 8, 9, 40, 72   
norm, xiv   
Nos´e dynamics, 299, 314, 315 generalization of, 308–310 separated form of, 302   
Nos´e–Hoover method, 303   
Nos´e–Poincar´e method, 305, 307   
Notation, xiv   
NPT ensemble, 297   
numerical dispersion, 349, 354   
NVE ensemble, 296   
NVT ensemble, 297   
Octave, xiii   
one-form, 61   
one-step method, 13, 14   
order conditions, 145, 146   
order of a numerical method, 15, 20, 22   
order parameter, 92   
ordinary differential equations existence and uniqueness of solutions, 1   
orthogonal matrix, 200   
pair correlation function, 298   
parameterization, 191 of rigid body motion, 200   
partial differential equations, 5   
partitioned Runge–Kutta methods, 25, 26, 144, 155 symplecticness condition, 156   
pendulum, 8, 9, 33, 41, 176 multiple, 171   
periodic boundary conditions, 48, 288   
perturbed Hamiltonian, 235   
phase portrait, 41   
phase space, 3, 39 of a constrained system, 186   
Poincar´e transformation, 235, 236, 253, 306   
Poisson bracket, 45 properties of, 45   
polar coordinates, 54, 67   
post-processing methods, 164   
post-processing schemes, 148   
potential cut-off, 4   
potential cutoff, 313   
potential energy, 2, 5, 37   
programming, xiii   
projection methods, 195   
propagator for Euler’s method, 28 for St¨ormer–Verlet method, 28

quadratic first integrals, 90   
quantum mechanics, 101   
quaternion, 200

Radau Runge–Kutta methods, 151   
radial distribution function, 298   
rank-one updates, 243   
RATTLE (see also SHAKE), 169, 173, 175   
reflection symmetry, 81   
resonance instability, 281, 282, 350 Krein index, 284, 350 numerical, 257, 258, 265   
restricted three-body problem, 161   
reversible method, 238, 271   
reweighting, 311, 312   
rigid body dynamics, 6, 199 linear or planar, 206 angular momentum of, 211 definition of, 201 Hamiltonian formulation for, 204 in molecular dynamics, 6   
RKSUITE, 142   
Rodrigues’ Formula, 95   
Runge–Kutta methods, 22, 35, 142, 144, 149, 150, 164 fourth-order, 23 symplecticness condition for, 152 implicitness of, 150 partitioned (see partitioned Runge–Kutta method), 25   
Runge–Kutta–Nystr¨om method, 25   
Runge–Lenz vector, 47, 67

satellite orbits, 142   
scalar product, xiv   
Schr¨odinger Equation, 101   
Scovel’s method, 95, 162   
separable Hamiltonian, 144, 145

shadowing, 124   
SHAKE discretization, 169, 173, 313 application to a constraint chain, 181 error growth in, 177 implementation of, 178 symplecticness of, 174   
shallow-water equations, 320 geostrophic balance, 322 Lagrangian particle formulation, 323 particle discretizations, 330   
short range force, 4   
singular potential, 50   
SO(3), 200   
solar system, 143, 163   
soliton, 319, 350   
spatial discretization, 6 grid-based methods, 326 Hamiltonian Particle-Mesh (HPM) method, 332 particle-based methods, 330 particle-mesh methods, 332 Smoothed Particle Hydrodynamics (SPH), 330   
specific heat, 298   
sphere shallow-water equations on, 334 $N .$ -body problem on, 178   
splitting methods, 76, 78, 91, 144, 166, 217, 257, 263, 276 first-order, 77 for a separable Hamiltonian system, 79 for dynamics in a magnetic field, 94 for weakly coupled systems, 97 linear/nonlinear, 99, 100   
spring-mass system, 30, 33   
St¨ormer–Verlet method, 26, 35, 70, 71, 91 as a splitting method, 80 relationship to Euler-A and Euler-B, 81 symplecticness of, 80   
stability, 33, 70 for nonlinear systems, 33 of a numerical method, 27   
stability region, 33   
statistical mechanics, 296   
stepsize bounds, 248   
Strang splitting, 135   
Sundman transformation, 235   
symmetric adaptive composition, 251   
symmetric composition, 85 table of methods, 148   
symmetric methods modified equations for, 139 even order of, 86   
symmetric top, 209   
symmetry, 241   
Symplectic Euler, 26, 32, 33, 75, 84   
symplectic maps closure under composition, 99   
symplectic matrix, 53   
symplectic numerical method, 72 for constrained dynamics, 189 for rigid body motion, 207   
symplectic property, 52, 59, 60, 63 definition of a symplectic map, 53 of a Hamiltonian flow map, 54 same as area conservation for planar maps, 56   
symplectic structure, 38   
symplectic transformation, 67, 68   
symplectic two-form, 57, 61, 63   
symplectic variable stepsize, 253   
symplecticness conservation of volume vs., 55 integral preservation vs., 73   
temperature, 297   
temperature bath, 299   
thermalization, 289   
three-body problem, 4, 161, 166   
time reparameterization, 238   
time-dependent Hamiltonian system, 102   
time-reversal symmetry, 73, 236 and SHAKE/RATTLE discretization, 196 eigenvalues and, 83 flow map and, 83 for a Hamiltonian system, 82 linear systems, 83 vector fields and, 83   
timestepping schemes, 13   
torque, 214   
trajectory, 3, 11 discrete, 12   
trapezoidal rule, 14, 239 local error of, 16   
trees, 146   
Trotter factorization, 134   
two-form, 56, 60, 63 geometric interpretation of, 57 symplectic, 57, 63   
variable stepsize, 234, 235   
variational derivative, 5 as a gradient, 5   
variational equations, 51, 52, 67   
velocity autocorrelation function, 298   
volume preservation, 68   
Von Neumann, John, $\times$   
wave equation, 316 conservation laws, 316 Hamiltonian formulation, 317   
weakly coupled systems, 97   
weather prediction, 105   
wedge product, 63, 64 properties, 69   
Wilkinson, 106   
Yoshida method of, 148