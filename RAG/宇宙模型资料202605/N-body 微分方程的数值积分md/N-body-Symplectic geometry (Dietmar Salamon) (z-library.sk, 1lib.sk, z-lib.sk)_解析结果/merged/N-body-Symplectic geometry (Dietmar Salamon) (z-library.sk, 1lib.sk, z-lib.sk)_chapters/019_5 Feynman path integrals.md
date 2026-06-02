# 5 Feynman path integrals

Heuristically a variational family $( \pi , \phi )$ together with some sort of measure on the fibers determines a distribution on the base

$$
f ( x ) = \int _ { \stackrel { c \epsilon P } { \pi ( c ) = x } } e ^ { i \phi ( c ) / \hbar } { \mathcal { D } } c .
$$

If the base is a product $X = X _ { 0 } \times X _ { 1 }$ the distribution may be interpreted as an integral kernel

$$
K ( x _ { 1 } , x _ { 0 } ) = \int e ^ { i \phi ( c ) / \hbar } { \mathcal D } { \mathsf c }
$$

of an operator from a space of functions on $X _ { 0 }$ to a space of functions on $X _ { 1 }$

$$
U f ( x _ { 1 } ) = \int _ { X _ { 0 } } K ( x _ { 1 } , x _ { 0 } ) f ( x _ { 0 } ) d x _ { 0 } .
$$

Formally the Feynman path integral is an example of this. The composition formula of Proposition 2.1 should correspond to the composition of operators.

Consider a time dependent quadratic Hamiltonian

$$
\begin{array} { r c l } { H ( t , x , y ) } & { = } & { H _ { 0 } ( t ) + \langle H _ { x } ( t ) , x \rangle + \langle H _ { y } ( t ) , y \rangle } \\ & & { + \frac { 1 } { 2 } \langle H _ { x x } ( t ) x , x \rangle + \langle H _ { y x } ( t ) x , y \rangle + \frac { 1 } { 2 } \langle H _ { y y } ( t ) y , y \rangle } \end{array}
$$

where $H _ { x x } ( t ) , H _ { y x } ( t ) , H _ { y y } ( t )$ are as before, $H _ { x } ( t ) , H _ { y } ( t ) \in \mathsf { R } ^ { n }$ ,and $H _ { 0 } ( t ) \in \mathbb { R }$ · Let $\phi ( c )$ denote the action integral. The Feynman path integral associated to $H$ is the formal expression

$$
\mathcal { U } ( t _ { 1 } , t _ { 0 } , H ) f ( x _ { 1 } ) = \int _ { \stackrel { c \in \mathcal { P } ( t _ { 0 } , t _ { 1 } ) } { x ( t _ { 1 } ) = x _ { 1 } } } e ^ { i \phi ( c ) / \hbar } f ( x ( t _ { 0 } ) ) \mathcal { D } c .
$$

where $\boldsymbol { c } = ( x , y )$ .Feynman was led to integrals of this type by physical considerations. He assigned a phase $e ^ { i \phi ( c ) / \hbar }$ to each classical path c and summed over all paths c. Our goal is to interpret this integral as a limit in the same way Feynman did. The discrete analogue of the path integral is the expression

$$
\mathcal { U } ^ { T } ( t _ { 1 } , t _ { 0 } , H ) f ( x _ { 1 } ) = \int _ { \stackrel { c \in \mathcal { P } ^ { T } ( t _ { 0 } , t _ { 1 } ) } { x \in ( t _ { 1 } ) = x _ { 1 } } } e ^ { i \phi ^ { T } ( c ) / \hbar } f ( x ( t _ { 0 } ) ) \mathcal { D } c
$$

where

$$
{ \mathcal { D } } \mathsf { c } = \prod _ { t _ { 0 } \leq t < t _ { 1 } } ( 2 \pi \hbar ) ^ { - n } \operatorname* { d e t } \left( \mathbb { 1 } - ( t ^ { + } - t ) H _ { x y } \right) ^ { 1 / 2 } d x ( t ) d y ( t ) .
$$

The order of integration is the time-order,i.e. first $d { \boldsymbol x } ( t _ { 0 } )$ , then $d y ( t _ { 0 } )$ , then $d { \boldsymbol x } \big ( t _ { 0 } ^ { + } \big )$ etc. The notation $\mathcal { D } \boldsymbol { c }$ hides the normalization which makes the Feynman product a unitary operator. The integral does not converge absolutely as an integral in all its variables. Interchanging the order of integration requires justification.

Theorem 5.1 The limit

$$
\mathcal { U } ( t _ { 1 } , t _ { 0 } , H ) = \operatorname* { l i m } _ { | T | \to 0 } \mathcal { U } ^ { T } ( t _ { 1 } , t _ { 0 } , H )
$$

exists in the strong operator topology. $\boldsymbol { { H } }$ is a unitary operator on $L ^ { 2 } ( \mathbb { R } ^ { n } )$ Here the partitions partition the interval $[ t _ { 0 } , t _ { 1 } ]$

We now give an explicit formula for the operator $\mathcal { U } ( t _ { 1 } , t _ { 0 } , H )$ . According to the philosophy of Fourier integral operators it should be possible to replace $\phi$ by any other phase function defining the same symplectic relation provided that $\mathcal { D } \boldsymbol { c }$ is modifed appropriately. In the case at hand the symplectic relation is the graph of the evolution system $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ (see Example 3.3) so it is natural to seek a formula in terms of the generating function $S ( \boldsymbol { x } _ { 0 } , \boldsymbol { x } _ { 1 } )$ from $t _ { 0 }$ to $t _ { 1 }$ . Let $\boldsymbol { \Psi } _ { t _ { 0 } } ^ { t _ { 1 } }$ denote the linear part of $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ ， $\mu = \mu ( t _ { 0 } , t _ { 1 } , H )$ denote the Maslov index of $[ t _ { 0 } , t _ { 1 } ] \to \mathrm { S p } ( 2 n ) : t \mapsto \Psi _ { t _ { 0 } } ^ { t }$ ,and $B = B ( t _ { 1 } , t _ { 0 } )$ denote the right upper block in the block decomposition （7） of $\Psi _ { t _ { 0 } } ^ { t _ { 1 } }$

Theorem 5.2 If $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ admits a generating function then $\mathcal { U } ( t _ { 1 } , t _ { 0 } , H )$ is given $b y$

$$
\mathcal { U } ( t _ { 1 } , t _ { 0 } , H ) f ( x _ { 1 } ) = \frac { ( 2 \pi \hbar ) ^ { - n / 2 } } { \vert \operatorname* { d e t } B \vert ^ { 1 / 2 } } e ^ { i \pi \mu / 2 } \underset { \mathbb { R } ^ { n } } { \int } e ^ { i S ( x _ { 0 } , x _ { 1 } ) / \hbar } f ( x _ { 0 } ) d x _ { 0 } .
$$

The formula is first proved in the case of discrete time and then convergence as well as the continuous time formula are obvious. To prove the analogous formula in discrete time note that Taylor's formula

$$
{ \phi } ^ { T } ( c ) = S ^ { T } ( x _ { 0 } , x _ { 1 } ) + \scriptstyle \frac { 1 } { 2 } \langle W _ { t _ { 0 } t _ { 1 } } ^ { T } \gamma , \gamma \rangle
$$

is exact (since the action is quadratic). Here $c = c _ { 0 } + \gamma . ~ c$ $c _ { 0 }$ is a fiber critical   
Then theh $\pi ( c _ { 0 } ) = ( x _ { 0 } , x _ { 1 } )$ $S ^ { T } ( x _ { 0 } , x _ { 1 } ) = \phi ^ { T } ( c _ { 0 } )$ $\gamma$ $\overline { { W _ { t _ { 0 } t _ { 1 } } ^ { T } } }$   
rem 4.1.

Associated to the Hamiltonian $H ( t , x , y )$ is a second order differential operator $H ( t , Q , P )$ where $Q _ { j }$ and $P _ { j }$ denote the self-adjoint operators

$$
\left( P _ { j } f \right) ( x ) = - i \hbar \partial _ { j } f ( x ) , \qquad \left( Q _ { j } f \right) ( x ) = x _ { j } f ( x ) ,
$$

and $H ( t , Q , P )$ results from $H ( t , x , y )$ by making the following substitutions

$$
x _ { j } \mapsto Q _ { j } , \qquad y _ { j } \mapsto P _ { j } ,
$$

$$
x _ { j } x _ { k } \mapsto Q _ { j } Q _ { k } , \qquad y _ { j } y _ { k } \mapsto P _ { j } P _ { k } , \qquad x _ { k } y _ { j } \mapsto Q _ { k } P _ { j } - \frac { i \hbar } { 2 } \delta _ { j k } \mathbb { 1 } .
$$

Pay attention to the mixed term: $Q _ { j }$ and $P _ { j }$ do not commute. If the Hamiltonian has the form $H = { \scriptstyle { \frac { 1 } { 2 } } } | y ^ { 2 } | + V ( x )$ the equation in the next theorem is the Schrodinger equation.

Theorem 5.3 The operators $\mathcal { U } ( t , t _ { 0 } , H )$ are the evolution operators of the time-dependent partial differential equation

$$
i \hbar { \frac { \partial u } { \partial t } } = H ( t , Q , P ) u .
$$

Proof:Assume that $\psi _ { t _ { 0 } } ^ { t }$ admits a generating function and let $S ( t , x , x _ { 0 } )$ be given by the action． Let $B ( t )$ denote the right upper block in the block decomposition of $\Psi _ { t _ { 0 } } ^ { t } = d \psi _ { t _ { 0 } } ^ { t }$ and abbreviate $\lambda = { e ^ { i \pi \mu \left( { \bar { t } } , { \bar { t } } _ { 0 } , H \right) / 2 } } \left( { 2 \pi \hbar } \right) ^ { - n / 2 }$ . Then

$$
u ( t , x ) = \mathcal { U } ( t , t _ { 0 } , H ) f ( x ) = \lambda | \operatorname* { d e t } B ( t ) | ^ { - 1 / 2 } \intop _ { \mathbb { R } ^ { n } } e ^ { i S ( t , x , x _ { 0 } ) / \hbar } f ( x _ { 0 } ) d x _ { 0 } .
$$

Diferentiating with respect to $\pmb { x }$ gives

$$
P _ { j } u = \lambda | \operatorname* { d e t } B | ^ { - 1 / 2 } \int _ { \pmb { R ^ { n } } } \frac { \partial S } { \partial x _ { j } } e ^ { i S / \hbar } f
$$

and

$$
P _ { j } P _ { k } u = - i \hbar \frac { \partial ^ { 2 } S } { \partial x _ { j } \partial x _ { k } } u + \lambda | \operatorname* { d e t } { B } | ^ { - 1 / 2 } \int \frac { \partial S } { \partial n } \frac { \partial S } { \partial x _ { j } } e ^ { i S / \hbar } f
$$

Hence the right hand side of the equation is

$$
\begin{array} { r c l } { { H ( t , Q , P ) u } } & { { = } } & { { \displaystyle - i \hbar { \frac { 1 } { 2 } } \mathrm { t r } \left( H _ { y x } + H _ { y y } D B ^ { - 1 } \right) u } } \\ { { } } & { { } } & { { \displaystyle + \lambda | \operatorname* { d e t } B | ^ { - 1 / 2 } \underset { \mathrm { R } ^ { n } } { \overset { \displaystyle - } { \sum } } H ( t , x , \partial _ { x } S ) e ^ { i S / \hbar } f . } } \end{array}
$$

Here we have used the identity $\partial ^ { 2 } S / \partial x ^ { 2 } = D B ^ { - 1 }$ where $D = D ( t )$ is the lower right block in the block decomposition （7) of ${ \Psi } _ { t _ { 0 } } ^ { t }$ . Now

$$
\begin{array} { r c l } { { \displaystyle \frac { d } { d t } | \operatorname* { d e t } B | ^ { - 1 / 2 } } } & { { = } } & { { \displaystyle - { \frac { 1 } { 2 } } \mathrm { t r } \bigl ( \dot { B } B ^ { - 1 } \bigr ) | \operatorname* { d e t } B | ^ { - 1 / 2 } } } \\ { { } } & { { = } } & { { \displaystyle - { \frac { 1 } { 2 } } \mathrm { t r } \bigl ( H _ { y x } + H _ { y y } D B ^ { - 1 } \bigr ) | \operatorname* { d e t } B | ^ { - 1 / 2 } } } \end{array}
$$

and hence

$$
i \hbar \frac { \partial u } { \partial t } = - i \hbar \mathsf { \Omega } _ { 2 } ^ { 1 } \mathrm { t r } \left( H _ { y x } + H _ { y y } D B ^ { - 1 } \right) u - \lambda | \operatorname* { d e t } B | ^ { - 1 / 2 } \intop _ { \mathsf { R } ^ { n } } \frac { \partial S } { \partial t } e ^ { i S / \hbar } f .
$$

Since $\boldsymbol { S }$ satisfies the Hamilton-Jacobi equation $\partial _ { t } S + H ( t , x , \partial _ { x } S ) = 0$ this proves the statement whenever $\psi _ { t _ { 0 } } ^ { t }$ admits a generating function. The general case follows since both sides of the equation depend continuously on $H$ □

# 6Geometric Quantization

A time dependent Hamiltonian $H$ on $\pmb { \mathbb { R } } ^ { 2 n }$ determines an evolution system on $W = \mathsf { R } ^ { 2 n } \times \mathsf { U } ( 1 )$ via the formula

$$
g _ { t _ { 0 } } ^ { t _ { 1 } } ( z _ { 0 } , u _ { 0 } ) = \big ( \psi _ { t _ { 0 } } ^ { t _ { 1 } } ( z _ { 0 } ) , u _ { 0 } e ^ { i \phi ( c ) / \hbar } \big )
$$

for $( z _ { 0 } , u _ { 0 } ) \in W = \mathbb { R } ^ { 2 n } \times \operatorname { U } ( 1 )$ where $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ is the evolution system generated by $H$ ， $\phi ( c )$ is the symplectic action integral evaluated at the curve $c ( t ) = \psi _ { t _ { 0 } } ^ { t } ( z _ { 0 } )$ If the generating function $S = \phi ( c )$ of $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ is defined then

$$
g _ { t _ { 0 } } ^ { t _ { 1 } } ( z _ { 0 } , u _ { 0 } ) = \left( \psi _ { t _ { 0 } } ^ { t _ { 1 } } ( z _ { 0 } ) , u _ { 0 } e ^ { i S ( x _ { 0 } , x _ { 1 } ) / \hbar } \right)
$$

where ${ \boldsymbol { z } } _ { j } = ( x _ { j } , y _ { j } )$ ， $z _ { 1 } = \psi _ { t _ { 0 } } ^ { t _ { 1 } } ( z _ { 0 } )$ . The group $\mathrm { E S p } ( W , \hbar )$ of all diffeomorphisms of W of form $\pmb { g } _ { t _ { 0 } } ^ { t _ { 1 } }$ where $H$ runs over the time dependent (inhomogeneous) quadratic Hamiltonians $\mathbb { R } \to \mathcal { F } _ { 2 }$ is called the extended symplectic group. The various groups $\mathbb { E } \mathbb { S } \mathbb { p } ( W , \pmb { \hbar } )$ depend set-theoretically on $\pmb { \hbar }$ but are isomorphic as abstract groups.There is a central extension

$$
1 \to \operatorname { U } ( 1 ) \to \operatorname { E S p } ( W , \hbar ) \to \operatorname { A S p } ( \mathbb { R } ^ { 2 n } ) \to 1
$$

where $\mathbf { A S p } ( \mathbf { R } ^ { 2 n } )$ denotes the affine symplectic group; the projection is given by $g _ { t _ { 0 } } ^ { t _ { 1 } } \mapsto \psi _ { t _ { 0 } } ^ { t _ { 1 } }$ and the U(1) subgroup consists of those $\pmb { g } _ { t _ { 0 } } ^ { t _ { 1 } }$ where $H$ is constant.

If the Hamiltonian $H$ is time independent then the corresponding evolution systems $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ and $\pmb { g } _ { t _ { 0 } } ^ { t _ { 1 } }$ are flows: denote by $X _ { H }$ and $Y _ { H }$ the vector fields generating these flows.Then $X _ { H }$ is the Hamiltonian vector field of $H$ ，and $Y _ { H }$ is a lift of $X _ { H }$ to $L$ . The Lie algebra to $\mathsf { A S p } ( \mathsf { R } ^ { 2 n } )$ is the image of quadratic Hamiltonians under the representation $H \mapsto X _ { H }$ but this representation is not faithful as the constant Hamiltonians map to zero. However the representation $H \mapsto Y _ { H }$ is faithful. Diferentiating gives the following

Proposition 6.1 The vector feld $Y _ { H }$ on W is given by

$$
Y _ { H } ( z , u ) = ( X _ { H } ( z ) , u \dot { \imath } s _ { H } / \hbar ) , \qquad s _ { H } = \langle y , \partial _ { y } H \rangle - H .
$$

Souriau [25] and Kostant [15] describe the extended symplectic group as the group of bundle automorphisms of the $U ( 1 )$ bundle $W \to \mathbb { R } ^ { 2 n }$ which cover affine symplectic transformations and preserve the connection form

$$
\pmb { \alpha } = - \frac { i } { \hbar } \langle y , d x \rangle + u ^ { - 1 } d u .
$$
