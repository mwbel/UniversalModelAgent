plus a remainder term exponentially small in $\Delta t$ . The modified Hamiltonian $\tilde { H }$ can be, at least formally, transformed to action-angle variables $( \mathsf { I } , \phi )$ which yields a Hamiltonian of the form

$$
\tilde { H } ( \mathbf { I } , \pmb { \phi } ; \Delta t ) = H _ { 0 } ( \mathbf { I } ) + \Delta t ^ { p } \tilde { H } _ { 1 } ( \mathbf { I } , \pmb { \phi } ; \Delta t ) .
$$

This perturbed Hamiltonian can be investigated by the NEKKHOROSHEV theorem with $\varepsilon = \Delta t ^ { p }$ . In particular, the key ingredients of the elegant proof by LOSCHAK AND NEISHTADT [116] are conservation of total energy $\tilde { H }$ , the conservation of an adiabatic invariant $J = \pmb { \omega } _ { * } ^ { T } \mathbb { I }$ , where $\pmb { \omega } _ { * } = \nabla _ { \mathrm { l } } H _ { 0 } ( \mathbf { l } _ { * } )$ is a completely resonant frequency vector close to $\pmb { \omega } = \nabla _ { \mathsf { I } } H _ { 0 } ( \pmb { \mathsf { I } } )$ , and convexity of $H _ { 0 } ( \mathbf { l } )$ . These three conditions also hold for the modified equations and the long-time conservation of the action variables also applies to the numerical integration scheme. This result extends to the symplectic integration of perturbed integrable systems of the form (5.26). An elegant proof has been given by MOAN [135] using results of KUKSIN AND POSCHEL ¨ [100] on the embedding of symplectic maps into the flow of non-autonomous Hamiltonian systems.

An extensive discussion of integrable and near-integrable systems and their behavior under symplectic integration can also be found in the monograph [80].

# Hyperbolic systems

Completely contrary to integrable systems, solutions of hyperbolic systems [76] diverge exponentially everywhere in phase space. This makes the solution behavior unpredictable over long time intervals and leads to “chaotic” dynamics. Strictly hyperbolic systems are difficult to find, but the notion of hyperbolicity is very fruitful for mathematical studies. Firstly, Hamiltonian hyperbolic systems remain hyperbolic under small changes in the Hamiltonian (structural stability), secondly the statistical mechanics of hyperbolic systems is quite well understood. Let us hence assume that a hyperbolic Hamiltonian system is integrated numerically by a symplectic method. We can assume that the associated modified Hamiltonian system is also hyperbolic. We also know that a symplectic method will approximately conserve energy over exponentially long time intervals. However, because of the exponential divergence of solutions, the numerical computed trajectory will not stay close to the exact solution of the modified problem over time periods larger than $\mathcal { O } ( \Delta t ^ { - 1 } )$ . On the other hand, hyperbolic systems possess a shadowing property [76, 173]. Applied to our situation, one can conclude that any numerical trajectory can be shadowed by some exact solution of the modified problem over exponentially long periods of time (before a significant drift in energy is observed). In what sense is that information useful? Often one is not interested in an individual solution but in the time average of some observable $\mathcal { A }$ along trajectories. It turns out that for a hyperbolic Hamiltonian system the limit

$$
\langle \mathcal { A } \rangle = \operatorname* { l i m } _ { \tau \to \infty } \frac { 1 } { \tau } \int _ { 0 } ^ { \tau } \mathcal { A } ( \pmb { q } ( t ) , \pmb { p } ( t ) ) d t
$$

is independent of the chosen trajectory for almost all initial values $\left( q _ { 0 } , p _ { 0 } \right)$ provided that the initial conditions are from one and the same energy $E$ hypersurface, i.e.

$$
H ( q _ { 0 } , p _ { 0 } ) = E .
$$

In other words, the infinite time average $\langle \mathcal { A } \rangle$ depends only on the energy of the trajectory.6 Computationally, we can only perform finite-time averages

$$
\bar { \boldsymbol { \mathcal { A } } } ( \tau ) = \frac { 1 } { \tau } \int _ { 0 } ^ { \tau } \boldsymbol { \mathcal { A } } ( \boldsymbol { q } ( t ) , \boldsymbol { p } ( t ) ) d t .
$$

But the existence of a large deviation theorem [207] implies that the set of all initial points for which

$$
| \bar { \mathcal { A } } ( \tau ) - \langle \mathcal { A } \rangle | \geq \delta
$$

has a measure that goes to zero exponentially fast in $\tau$ for a given fixed tolerance $\delta > 0$ . Since, roughly speaking, numerical trajectories obtained from a symplectic integration method shadow some exact solution of a slightly perturbed hyperbolic Hamiltonian system, the same statement is true for numerically computed time averages. A precise formulation of such a result has been given by REICH in [158].

Numerical evidence for such a behavior can indeed be found even if the system is not provably hyperbolic. As a demonstration, we simulate a molecular $N .$ -body problem similar to what has been used in Section 4.5. A total of $N = 4 9$ particles move in the $\left( x , y \right)$ -plane under the influence of a pair-wise repulsive potential and periodic boundary conditions are applied in the $x$ and $y$ directions. The equations of motion conserve energy and total linear momentum. We take the mean kinetic energy (temperature) as our observable; i.e.,

$$
\mathcal { A } = \frac { 1 } { 2 N } \sum _ { i = 1 } ^ { N } | | p _ { i } | | ^ { 2 } .
$$

We perform four simulations with random initial conditions from the constant energy level $E = H ( \pmb { q } _ { 0 } , \pmb { p } _ { 0 } ) = 2 0 0 0$ with zero total linear momentum. The computed finite-time averages $\bar { \mathcal { A } } ( \tau )$ , $\tau \in [ 0 , 1 0 ]$ , can be found in Fig. 5.5. The averages at $\tau = 1 0$ are all within a $\delta = 0 . 0 1$ distance of each other.

This property of a symplectic integration method helps to explain the great success of the St¨ormer–Verlet method for molecular dynamics simulations [198, 4]. See Chapter 11 for further details.

![](images/fa555c141d286437cbffb409d2e09cf72aae07be99f67d47986a33eb9f2782a3.jpg)  
Figure 5.5 Time-averaged temperature computed along four different trajectories with one and the same initial energy $E = 2 0 0 0$ and zero total linear momentum.

# Adiabatic invariants

We have extensively discussed and used the harmonic oscillator

$$
\ddot { q } = - \omega ^ { 2 } q ,
$$

as an example throughout the book because of its simplicity. Let us now complicate the matter slightly by considering a harmonic oscillator with slowly varying frequency; for example

$$
\omega ( \varepsilon t ) = \frac { 1 } { \sqrt { 1 + 0 . 2 5 \sin ( 2 \pi \varepsilon t ) } } ,
$$

with $\varepsilon \ll 1$ a small parameter [7]. The behavior of such a time-dependent Hamiltonian system with Hamiltonian

$$
H ( p , q , \varepsilon t ) = \frac { 1 } { 2 } \left( p ^ { 2 } + \omega ( \varepsilon t ) ^ { 2 } q ^ { 2 } \right) ,
$$

becomes more transparent when going to action-angle variables $( J , \phi )$ . Upon using the generating function [7, 8, 73] (compare also Section 6.4)

$$
S ( q , \phi , t ) = { \frac { 1 } { 2 } } \omega ( \varepsilon t ) q ^ { 2 } \cot \phi
$$

the transformation is defined by

$$
p = { \frac { \partial S } { \partial q } } = \omega ( \varepsilon t ) q \cot \phi ,
$$

and

$$
J = - { \frac { \partial S } { \partial \phi } } = { \frac { 1 } { 2 } } \omega ( \varepsilon t ) q ^ { 2 } { \frac { 1 } { \sin ^ { 2 } \phi } } .
$$

We can solve this system for $( q , p )$ to obtain

$$
\begin{array} { l } { q = \sqrt { \displaystyle \frac { 2 J } { \omega } } \sin \phi , } \\ { p = \sqrt { 2 \omega J } \cos \phi . } \end{array}
$$

The corresponding transformed Hamiltonian is

$$
\begin{array} { l } { \displaystyle \bar { H } ( J , \phi , \varepsilon t ) = H ( p , q , \varepsilon t ) + \frac { \partial S } { \partial t } } \\ { \displaystyle = \omega ( \varepsilon t ) J + \frac { \varepsilon } { 2 } \frac { \omega ^ { \prime } ( \varepsilon t ) } { \omega ( \varepsilon t ) } J \sin 2 \phi } \\ { \displaystyle = \omega ( \varepsilon t ) J + \varepsilon f ( J , \phi , \varepsilon t ) , } \end{array}
$$

$\begin{array} { r } { f ( J , \phi , \varepsilon t ) = \frac { \varepsilon } { 2 } \frac { \omega ^ { \prime } ( \varepsilon t ) } { \omega ( \varepsilon t ) } J \sin 2 \phi } \end{array}$

Following the work of NEISHTADT [143], it is known that there exists another symplectic change of coordinates $( J , \dot { \phi } ) \stackrel { \cdot } {  } ( \tilde { J } , \tilde { \phi } )$ which is $\varepsilon$ close to the identity such that the transformed Hamiltonian is of the form

$$
\hat { H } ( \tilde { J } , \tilde { \phi } , t ) = \omega ( \varepsilon t ) \tilde { J } + \varepsilon ^ { 2 } \tilde { g } ( \tilde { J } , \varepsilon t ; \varepsilon ) + e ^ { - c / \varepsilon } \tilde { f } ( \tilde { J } , \tilde { \phi } , \varepsilon t ; \varepsilon ) ,
$$

$c > 0$ some constant and $\tilde { f }$ and $\tilde { g }$ are bounded functions. Hence we have

$$
| J ( 0 ) - J ( t ) | = \mathcal { O } ( \varepsilon ) , \qquad \mathrm { f o r } \qquad | t | \leq e ^ { c / ( 2 \varepsilon ) } ,
$$

and the action variable $J$ is called an adiabatic invariant [7, 8, 73]. The action variable $J$ can also be given a geometric interpretation. Over short time intervals, the motion is essentially periodic with a practically constant frequency $\omega _ { 0 } ~ \approx$ $\omega ( \varepsilon t )$ . Denote the area enclosed by the periodic orbits of

$$
\dot { q } = p , \qquad \dot { p } = - \omega _ { 0 } ^ { 2 } q ,
$$

by $A$ , then

$$
J = \frac { 1 } { 2 \pi } \oint p d q = \frac { A } { 2 \pi } .
$$

Note that the energy $H = \bar { H }$ will show a systematic drift since $J$ is nearly constant and the product $\begin{array} { r } { \omega ( \varepsilon t { } ) J \approx H } \end{array}$ will follow changes in the frequency $\omega$ which can be of order one.

If the time-dependent equation of motion

$$
\ddot { q } = - \omega ( \varepsilon t ) ^ { 2 } q
$$

is solved by a symplectic second-order integration method (see the Exercises of Chapter 4 as well as Example 6 below), then there exists a modified timedependent Hamiltonian $\tilde { H } ( \Delta t )$ which, written in action-angle variables, takes the form

$$
\tilde { H } ( J , \phi , \varepsilon t , \Delta t ) = \omega ( \varepsilon t ) J + \varepsilon t ( J , \phi , \varepsilon t ) + \Delta t ^ { 2 } g ( J , \phi , \varepsilon t ; \varepsilon , \Delta t ) ,
$$

$g$ an appropriate function. Now assume that $\Delta t ^ { 2 }$ is bounded by $\varepsilon \colon \Delta t ^ { 2 } < K \varepsilon$ . Then it can be shown that an estimate of type (5.27) also holds for the numerical method [159]. See also [175] for further numerical experiments.

Example 6Any time-dependent Hamiltonian $H ( \pmb { q } , \pmb { p } , t )$ can be treated within the framework of autonomous Hamiltonian systems by enlarging the phase space by two additional variables $( Q , P )$ . This has been discussed in the Exercises of Chapter 4. Let us apply the idea to the Hamiltonian

$$
H ( q , p , t ) = { \frac { 1 } { 2 } } \left[ p + \omega ( \varepsilon t ) ^ { 2 } q ^ { 2 } \right] , \qquad \omega ( \varepsilon t ) = { \frac { 1 } { \sqrt { 1 + 0 . 2 5 \sin ( 2 \pi \varepsilon t ) } } } .
$$

We define the extended Hamiltonian $\bar { H } ( q , p , Q , P )$ as

$$
\bar { H } = \frac 1 2 \left[ p + \omega ( Q ) ^ { 2 } q ^ { 2 } \right] + \varepsilon P .
$$

The associated equations of motion are

$$
\begin{array} { l } { \displaystyle { \frac { d } { d t } q = p , } } \\ { \displaystyle { \frac { d } { d t } p = - \omega ( Q ) ^ { 2 } q , } } \\ { \displaystyle { \frac { d } { d t } Q = \varepsilon , } } \\ { \displaystyle { \frac { d } { d t } P = - \omega ( Q ) \omega ^ { \prime } ( Q ) q ^ { 2 } . } } \end{array}
$$

The variable $Q$ is equal to slow time $\varepsilon t$ , i.e. $Q = \varepsilon t$ . The equations can be integrated by a second-order splitting method using the split Hamiltonian

$$
\bar { \cal H } _ { 1 } = \frac { 1 } { 4 } \omega ( Q ) ^ { 2 } q ^ { 2 } , \qquad \bar { \cal H } _ { 2 } = \frac { 1 } { 2 } p ^ { 2 } + \varepsilon { \cal P } , \qquad \bar { \cal H } _ { 3 } = \frac { 1 } { 4 } \omega ( Q ) ^ { 2 } q ^ { 2 } .
$$

One can iminate the variable $P$ and obtains a modified St¨ormer–Verlet method.

We perform a series of experiments with constant $\Delta t$ and increasing values of $\varepsilon$ in the range $\varepsilon \in [ 0 . 0 0 1 , 0 . 0 5 ]$ . The initial conditions are $q ( 0 ) = 1$ and $p ( 0 ) = 0$ . We monitor the time evolution of the adiabatic invariant

$$
J = \frac { 1 } { 2 \omega } \left[ p ^ { 2 } + \omega ^ { 2 } q ^ { 2 } \right] ,
$$

and plot

$$
\Delta J _ { m a x } = \operatorname* { m a x } _ { t \in [ 0 1 0 0 ] } | J ( t ) - J ( 0 ) |
$$

as a function of $\varepsilon$ for several values of $\Delta t$ . See Fig. 5.6. As expected, we obtain a behavior of type

$$
\Delta J _ { m a x } ( \Delta t , \varepsilon ) \approx c _ { 1 } \Delta t ^ { 2 } + c _ { 2 } \varepsilon .
$$

![](images/e85eb9278337cd7c9dad765d811009020db9f4320d8b7bfe33264f60b79234cc.jpg)  
Figure 5.6 Variation in the adiabatic invariant $\jmath$ as a function of $\varepsilon$ for different values of the stepsize $\Delta t$ . ✷

# 5.3 Geometric integration and modified equations

An important aspect of backward error analysis is to show that the modified equations possess the same qualitative solution behavior as the given problem. A rigorous proof of such a statement is, in most cases, difficult. But it can be shown relatively easily that certain geometric aspects are preserved if the numerical method is chosen appropriately. We have discussed this already for

Hamiltonian systems and symplectic integration methods. The following more general result can be formulated:

Theorem 1 Whenever the flow map of a given differential equation posesses some geometric properties such as existence of first integrals, time reversiblity, preservation of volume, symplecticness, and the numerical discretization preserves these properties exactly, then the flow map of the modified differential equation will also satisfy these geometric properties. ✷

Proof. A proof of the theorem can be found in [153, 158]. See also [77, 16, 83, 74, 80].

Because of its importance, we discuss the case of symplectic methods in detail. Recall that the modified vector fields are recursively defined by

$$
\delta { \pmb f } _ { i + 1 } : = \operatorname* { l i m } _ { \tau  0 } \frac { { \pmb \psi } _ { \tau } - { \pmb \phi } _ { \tau , \tilde { \pmb f } _ { i } ( \tau ) } } { \tau ^ { i + 2 } } .
$$

We introduce the short-hand notation

$$
\pmb { \phi } _ { \tau } : = \pmb { \phi } _ { \tau , \tilde { \pmb { f } } _ { i } ( \tau ) } ,
$$

and obtain the relation

$$
\partial _ { z } \pmb { \psi } _ { \tau } = \partial _ { z } \pmb { \phi } _ { \tau } + \tau ^ { i + 2 } \partial _ { z } [ \delta \pmb { f } _ { i + 1 } ] + \mathcal { O } ( \tau ^ { i + 3 } ) .
$$

Let us now investigate the expression

$$
\pmb { F } _ { \tau } : = \frac { 1 } { \tau ^ { i + 2 } } \left[ \left( \partial _ { z } \pmb { \psi } _ { \tau } \right) ^ { T } \pmb { J } ^ { - 1 } \partial _ { z } \pmb { \psi } _ { \tau } - \left( \partial _ { z } \pmb { \phi } _ { \tau } \right) ^ { T } \pmb { J } ^ { - 1 } \partial _ { z } \pmb { \phi } _ { \tau } \right] .
$$

Since both $\psi _ { \tau }$ and $\pmb { \phi } _ { \tau }$ are symplectic maps, we have $\pmb { F } _ { \tau } = \pmb { 0 }$ .

The next step is to make use of (5.28). This yields

$$
\begin{array} { r l } & { { \cal F } _ { \tau } = - \left( \partial _ { z } [ \delta { \cal F } _ { i + 1 } ] \right) ^ { T } J ^ { - 1 } \partial _ { z } \phi _ { \tau } - \left( \partial _ { z } \phi _ { \tau } \right) ^ { T } J ^ { - 1 } \partial _ { z } [ \delta { \cal F } _ { i + 1 } ] + { \cal O } ( \tau ) } \\ & { \quad \quad = - \left( \partial _ { z } [ \delta { \cal F } _ { i + 1 } ] \right) ^ { T } J ^ { - 1 } - J ^ { - 1 } \partial _ { z } [ \delta { \cal F } _ { i + 1 } ] + { \cal O } ( \tau ) . } \end{array}
$$

Hence, upon taking the limit $\tau  0$ , one derives the condition

$$
\begin{array} { r } { \left( \partial _ { z } [ \delta \pmb { f } _ { i + 1 } ] \right) ^ { T } J ^ { - 1 } + J ^ { - 1 } \partial _ { z } [ \delta \pmb { f } _ { i + 1 } ] = \mathbf { 0 } , } \end{array}
$$

which is equivalent to $\delta f _ { j + 1 }$ being locally Hamiltonian [7]. The existence of a global modified Hamiltonian can be deduced either from the fact that the domain $z \in \Omega \subset \mathbb { R } ^ { 2 d }$ is simply connected or by explicit construction of a global Hamiltonian $\delta H _ { i + 1 }$ . For composition methods this is possible using the results of Section 5.4. Another explicit construction is provided by the generating function approach to the design of symplectic methods [16, 80]. We will discuss this approach briefly in Chapter 6.

Other applications of the theorem can be proven in a similar manner. See the exercises at the end of this chapter. ✷

Let us now focus on another application of Theorem 1. If a Hamiltonian $H$ is in involution with a function $F$ , i.e. $\{ H , F \} = 0$ , then $F$ is a first integral of the equations of motion with Hamiltonian $H$ . Let $\pmb { \phi } _ { \tau , F }$ denote the flow map of

$$
\frac { d } { d \tau } z = J \nabla _ { z } F ( z ) .
$$

Since the Poisson bracket of $F$ and $H$ is zero, the two associated flow maps commute, i.e.

$$
\pmb { \phi } _ { t , H } \circ \pmb { \phi } _ { \tau , F } = \pmb { \phi } _ { \tau , F } \circ \pmb { \phi } _ { t , H } ,
$$

which is equivalent to

$$
\begin{array} { r } { \pmb { \phi } _ { t , H } = \pmb { \phi } _ { - \tau , F } \circ \pmb { \phi } _ { t , H } \circ \pmb { \phi } _ { \tau , F } = \pmb { \phi } _ { \tau , F } ^ { - 1 } \circ \pmb { \phi } _ { t , H } \circ \pmb { \phi } _ { \tau , F } . } \end{array}
$$

Hence the flow map $\Phi _ { t , H }$ is invariant under the transformation ${ \pmb \psi } _ { \tau } : = { \pmb \phi } _ { \tau , F }$ . In fact, the reverse statement, called NOETHER’s theorem, that any one-parameter family of symmetries gives rise to a first integral, is also true. See OLVER [149], ARNOLD [7], and MARSDEN AND RATIU [124] for an extensive discussion of symmetries in classical mechanics.

For example, consider the differential equation

$$
\frac { d } { d \tau } \pmb { q } = \pmb { f } ( \pmb { q } ) ,
$$

and denote the associated flow map by $\phi _ { \tau }$ . Then we can consider the oneparameter family of canonical point transformations $\pmb { \psi } _ { \tau }$ defined by (compare Section 3.5)

$$
\begin{array} { r l } & { \bar { \pmb q } ( \tau ) = \pmb { \phi } _ { \tau } ( \pmb q ) , } \\ & { \bar { \pmb p } ( \tau ) = [ \nabla _ { \pmb q } \pmb \phi _ { \tau } ( \pmb q ) ] ^ { - 1 } \pmb p . } \end{array}
$$

This transformation is equivalent to the flow map of a Hamiltonian system with Hamiltonian $F = p ^ { T } f ( q )$ , i.e.,

$$
\pmb { \psi } _ { \tau } = \pmb { \phi } _ { \tau , F } .
$$

Hence, if $F$ is a first integral of $H$ , i.e. $\{ H , F \} = 0$ , then $\Phi _ { t , H }$ is invariant under $\psi _ { \tau }$ and vice versa.

Example7 Let us look at the following particular class of linear transformations. Given a linear matrix group7 $\mathcal { G } \subset \mathbb { R } ^ { d \times d }$ , we can apply elements (matrices) of $\mathcal { G }$ to $\pmb q$ , hence defining new coordinates

$$
\bar { \pmb q } = { \pmb Q } \pmb q , \qquad { \pmb Q } \in \mathcal { G } \subset \mathbb { R } ^ { d \times d } .
$$

Any matrix group $\mathcal { G }$ has an associated matrix algebra $\textbf { \mathfrak { g } } \subset \mathbb { R } ^ { d \times d }$ . The important property for our purposes is that the matrix exponential of any matrix $\pmb { A } \in \mathfrak { g }$ yields a matrix that is in the associated group $\mathcal { G }$ . In fact any matrix $Q \in { \mathcal { G } }$ can be represented by the matrix exponential of some matrix $\pmb { A }$ in $\pmb { 9 }$ [149]. Hence we consider the linear differential equation

$$
{ \dot { \pmb q } } = { \pmb A } \pmb q , \qquad { \pmb A } \in { \pmb g } ,
$$

and obtain

$$
\bar { \pmb q } ( \tau ) = \pmb Q ( \tau ) \pmb q , \qquad \pmb Q ( \tau ) = e ^ { \tau \pmb A } .
$$

To derive a symplectic transformation from $( \pmb q , \pmb p )$ to $( { \bar { q } } , { \bar { p } } )$ , we follow (5.30) and introduce canonical momenta

$$
\bar { \pmb { p } } ( \tau ) = \pmb { Q } ( \tau ) ^ { - T } \pmb { p } .
$$

The Hamiltonian associated with this one-parametric family of symplectic transformations is $F _ { A } = p ^ { T } A q$ .

The function $F _ { A }$ is a first integral if the given equations of motion are invariant under the symmetry group generated by $\mathcal { G }$ . Furthermore, any matrix $\pmb { A } \in \mathfrak { g }$ will lead to a first integral. But only a finite number, equal to the dimension of the matrix algebra g, of these integrals will be independent. For example, take the algebra of $3 \times 3$ skew-symmetric matrices which is the algebra associated to the group $S O ( 3 )$ of orthogonal matrices. This algebra is three dimensional and any matrix in the algebra can be expressed as a linear combination of

$$
\begin{array} { r } { \pmb { A } _ { 1 } = \left[ \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] , \quad \pmb { A } _ { 2 } = \left[ \begin{array} { c c c } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \end{array} \right] , \quad \pmb { A } _ { 3 } = \left[ \begin{array} { c c c } { 0 } & { - 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] . } \end{array}
$$

The associated three first integrals are

$$
F _ { A _ { 1 } } = p _ { 3 } q _ { 2 } - p _ { 2 } q _ { 3 } , \quad F _ { A _ { 2 } } = p _ { 1 } q _ { 3 } - p _ { 3 } q _ { 1 } , \quad F _ { A _ { 3 } } = p _ { 2 } q _ { 1 } - p _ { 1 } q _ { 2 } ,
$$

which are the three components of the angular momentum vector $m = \pmb { q } \times \pmb { p }$ . (We had already seen in Section 4.4 that the St¨ormer–Verlet method conserves angular momentum.) ✷

$^ 7 \mathsf { A }$ set $\mathcal { G }$ of invertible $d \times d$ matrices forms a matrix group in $\mathbb { R } ^ { d \times d }$ , if the product of any two matrices A, $B \in { \mathcal { G } }$ is in $\mathcal { G }$ ; i.e., $\pmb { A } \pmb { B } \in \mathcal { G }$ [149].

Let us now assume that a symplectic method $\psi _ { \Delta t }$ is invariant under a family of symplectic transformations $\pmb { \phi } _ { \tau , F }$ generated by a Hamiltonian $F$ , i.e.

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \tau , F } ^ { - 1 } \circ \pmb { \psi } _ { \Delta t } \circ \pmb { \phi } _ { \tau , F } ,
$$

for all $\Delta t \geq 0$ . A result by $\mathsf { G E }$ [68] states that $F$ is a first integral of $\psi _ { \Delta t }$ up to a constant $c ( \Delta t )$ . Often this constant can be shown to be equal to zero for all stepsizes $\Delta t$ . But even in the case that this is not possible one can still apply backward error analysis and Theorem 1 to obtain

$$
\pmb { \phi } _ { t , \tilde { H } } = \pmb { \phi } _ { \tau , F } ^ { - 1 } \circ \pmb { \phi } _ { t , \tilde { H } } \circ \pmb { \phi } _ { \tau , F } = \pmb { \phi } _ { - \tau , F } \circ \pmb { \phi } _ { t , \tilde { H } } \circ \pmb { \phi } _ { \tau , F } ,
$$

where we neglected terms exponentially small in $\Delta t$ . In other words, the two flow maps $\boldsymbol { \Phi } _ { t , \tilde { H } }$ and $\pmb { \phi } _ { \tau , F }$ commute and, hence, we must have $\{ \boldsymbol { F } , \tilde { H } \} = 0$ . As a consequence we can conclude that the numerical method has $F$ as a first integral (possibly up to a constant $c ( \Delta t )$ exponentially small in $\Delta t$ ).

On the other hand, following the above proof of Theorem 1 for symplectic maps, it is also relatively easy to show that any numerical method that preserves a first integral $F$ exactly has a modified equation that conserves $F$ . (See the Exercises at the end of this chapter.)

# 5.4 Modified equations for composition methods

The flow map of a linear differential equation

$$
{ \frac { d } { d t } } z = { \pmb { A } } z
$$

can be written

$$
\Phi _ { t , A } ( z ) = \mathrm { e } ^ { t A } z .
$$

Here the matrix exponential is defined by the convergent series expansion

$$
\mathrm { e } ^ { t A } = I _ { k } + t { \pmb { A } } + \frac { t ^ { 2 } } { 2 ! } { \pmb { A } } ^ { 2 } + \frac { t ^ { 3 } } { 3 ! } { \pmb { A } } ^ { 3 } + \cdot \cdot \cdot .
$$

It is important to note that, contrary to

$$
\mathrm { e } ^ { t a } \mathrm { e } ^ { t b } = \mathrm { e } ^ { t ( a + b ) } ,
$$

we have

$$
\mathrm { e } ^ { t A } \mathrm { e } ^ { t B } \neq \mathrm { e } ^ { t ( A + B ) } ,
$$

unless the two matrices $\pmb { A }$ and $B$ commute, i.e.

$$
[ A , B ] : = A B - B A = 0 .
$$

Instead there is a matrix $D ( t )$ such that

$$
\mathrm { e } ^ { t A } \mathrm { e } ^ { t B } = \mathrm { e } ^ { t D ( t ) } ,
$$

and the matrix $D ( t )$ is defined by a convergent expansion

$$
D ( t ) : = D _ { 0 } + t D _ { 1 } + t ^ { 2 } D _ { 2 } + t ^ { 3 } D _ { 3 } + \cdots .
$$

The matrices $D _ { j }$ , $i = 0 , 1 , \ldots , \infty$ , are given by the Baker–Campbell–Hausdorff (BCH) formula [196] which can be obtained from Taylor series expansion of the matrix exponential, i.e.

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \mathrm { e } ^ { t A } \mathrm { e } ^ { t B } = \left( I _ { k } + t A + \frac { t ^ { 2 } } { 2 } A ^ { 2 } + \cdots \right) \left( I _ { k } + t B + \frac { t ^ { 2 } } { 2 } B ^ { 2 } + \cdots \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = I _ { k } + t ( A + B ) + \displaystyle \frac { t ^ { 2 } } { 2 } \left( A ^ { 2 } + B ^ { 2 } + 2 A B \right) + \cdots } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = I _ { k } + t ( A + B ) + \displaystyle \frac { t ^ { 2 } } { 2 } \left( A + B \right) ^ { 2 } + \displaystyle \frac { t ^ { 2 } } { 2 } \left( A B - B A \right) + \cdots } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = I _ { k } + t ( A + B ) + \displaystyle \frac { t ^ { 2 } } { 2 } \left( A + B \right) + \displaystyle \frac { t ^ { 2 } } { 2 } [ A , B ] + \cdots } } \\ { { } } & { { } } & { { = \mathrm { e } ^ { t ( A + B ) + ( t ^ { 2 } / 2 ) \left[ A , B \right] + \cdots } . } } \end{array}
$$

Hence

$$
\begin{array} { l } { { { \cal D } _ { 0 } = A + B , } } \\ { { { \cal D } _ { 1 } = { \displaystyle \frac { 1 } { 2 } } [ A , B ] , } } \end{array}
$$

and further expansion yields the next two terms

$$
\begin{array} { l } { { \displaystyle { \cal D } _ { 2 } = \frac { 1 } { 1 2 } \left( [ { \cal A } , [ { \cal A } , { \cal B } ] ] + [ { \cal B } , [ { \cal B } , { \cal A } ] ] \right) , } } \\ { { \displaystyle { \cal D } _ { 3 } = \frac { 1 } { 2 4 } [ { \cal A } , [ { \cal B } , [ { \cal B } , { \cal A } ] ] ] . } } \end{array}
$$

The BCH formula allows for a relatively simple backward error analysis for splitting methods applied to linear differential equation. For example, consider the linear differential equation

$$
\frac { d } { d t } z = ( \pmb { A } + \pmb { B } ) z ,
$$

and assume that the matrix exponentials corresponding to the matrices $\pmb { A }$ and $B$ are easily computable. Then the composition method8 $\dot { \boldsymbol { z } } ^ { n + 1 } = \hat { \boldsymbol { R } } ( \Delta t ) \boldsymbol { z } ^ { n }$ with

$$
\hat { R } ( \Delta t ) = \mathrm { e } ^ { \Delta t A } \mathrm { e } ^ { \Delta t B }
$$

8This composition method is often called the Trotter formula [194].

is a first-order method. According to the BCH formula, the matrix $\hat { R } ( \Delta t )$ is the exact exponential corresponding to the linear differential equation

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } z = D ( \Delta t ) z } \\ { \displaystyle \qquad = \left( A + B + \frac { \Delta t } { 2 } [ { \pmb A } , { \pmb B } ] + \frac { \Delta t ^ { 2 } } { 1 2 } ( [ { \pmb A } , [ { \pmb A } , { \pmb B } ] ] + [ { \pmb B } , [ { \pmb B } , { \pmb A } ] ] ) + \cdots \right) z , } \end{array}
$$

at time $t = \Delta t$ . The second-order composition method9 with

$$
\hat { R } ( \Delta t ) : = \mathrm { e } ^ { ( \Delta t / 2 ) A } \mathrm { e } ^ { \Delta t B } \mathrm { e } ^ { ( \Delta t / 2 ) A }
$$

can be analyzed by multiple application of the BCH formula. We obtain the modified equation

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } z = D ( \Delta t ) z } \\ { \displaystyle \qquad = \left( A + B + \frac { \Delta t ^ { 2 } } { 2 4 } ( 2 [ B , [ B , A ] ] - [ A , [ A , B ] ] ) + \cdots \right) z . } \end{array}
$$

The important point is that the modified differential equation is based on the matrices $\pmb { A }$ and $B$ , the commutator $[ A , B ]$ , and repeated applications thereof.

We wish to extend this analysis to nonlinear differential equations

$$
{ \frac { d } { d t } } z = { \pmb f } ( z ) .
$$

Instead of the linear operator (matrix) $\pmb { A }$ , we now introduce the linear differential operator $L _ { f }$ , called the Lie derivative, which acts on smooth scalar-valued functions $g$ defined on phase space [7]. This operation, denoted by $L _ { f } g$ , is defined by

$$
L _ { f } g \left( z \right) : = \nabla _ { z } g ( z ) \cdot \pmb { f } ( z ) .
$$

It naturally extends to vector-valued functions $\pmb { g }$ by applying $L _ { f }$ to each component of $\pmb { g }$ . We denote this operation by $L _ { f } \pmb { g }$ . We can apply $L _ { f }$ repeatedly to itself, for example

$$
L _ { f } ( L _ { f } g ) = L _ { f } ^ { 2 } g ,
$$

and, as for the linear operator $\pmb { A }$ , we define the exponential of the operator $L _ { f }$ by the expansion (Lie series)

$$
\mathrm { e } ^ { t L _ { f } } : = \mathbf { i d } + t L _ { f } + \frac { t ^ { 2 } } { 2 ! } L _ { f } ^ { 2 } + \frac { t ^ { 3 } } { 3 ! } L _ { f } ^ { 3 } + \cdots .
$$

9This splitting is often called the Strang splitting [180].

This series can, formally, be obtained from (5.31) by replacing $\pmb { A }$ by $L _ { f }$ and $\prime$ by the identity map id; $\mathbf { i d } ( z ) = z$ .

Let us now return to the flow map $\boldsymbol { \phi } _ { t , f }$ of (5.33). Repeated differentiation of (5.33) with respect to time yields the remarkable identity

$$
\frac { d ^ { n } } { d t ^ { n } } z ( t ) _ { | t = 0 } = L _ { t } ^ { n - 1 } \pmb { f } ( z ) , \qquad z ( t ) = \pmb { \phi } _ { t , t } ( z ) .
$$

Using this result, the Taylor series expansion of $\boldsymbol { \phi } _ { t , f }$ about $t = 0$ can be written as

$$
\begin{array} { c } { { \phi _ { t , f } ( z ) = z + t \displaystyle { \frac { d } { d t } z ( 0 ) + \frac { t ^ { 2 } } { 2 ! } \frac { d ^ { 2 } } { d t ^ { 2 } } z ( 0 ) + \frac { t ^ { 3 } } { 3 ! } \frac { d ^ { 3 } } { d t ^ { 3 } } z ( 0 ) + \cdot \cdot \cdot } } } \\ { { = z + t f ( z ) + \displaystyle { \frac { t ^ { 2 } } { 2 ! } L _ { f } } f ( z ) + \frac { t ^ { 3 } } { 3 ! } L _ { f } ^ { 2 } f ( z ) + \cdot \cdot \cdot . } } \end{array}
$$

Let $L _ { f } ^ { j } \mathbf { i d } , \ j \geq 1$ , denote the operation of $L _ { f } ^ { i }$ on the identity map $\mathbf { i d } ( z ) = z$ . It is easily checked that $L _ { f } \mathbf { i d } = f$ and $L _ { f } ^ { 2 } \mathbf { i d } = L _ { f } f$ . More generally

$$
L _ { f } ^ { i } \mathbf { i d } = L _ { f } ^ { i - 1 } f ,
$$

for any $j \geq 1$ . Thus the flow map can be written as

$$
\begin{array} { l } { { \displaystyle \phi _ { t , f } = \mathbf { i d } + t { \pmb { f } } + \frac { t ^ { 2 } } { 2 ! } { \cal L } _ { f } { \pmb { f } } + \cdots } } \\ { ~ } \\ { { \displaystyle ~ = \left( \mathbf { i d } + t { \cal L } _ { f } + \frac { t ^ { 2 } } { 2 ! } { \cal L } _ { f } ^ { 2 } + \cdots \right) \mathbf { i d } } } \\ { ~ } \\ { { \displaystyle ~ = \mathrm { e } ^ { t { \cal L } _ { f } } \mathbf { i d } } . } \end{array}
$$

Furthermore, the action of the exponential on a function $h$ amounts to

$$
\mathsf { e } ^ { t L _ { f } } h = h \circ \Phi _ { t , f } .
$$

This can be seen from the expansion

$$
\mathrm { e } ^ { t L _ { f } } h = h + t L _ { f } h + \frac { t ^ { 2 } } { 2 ! } L _ { f } ^ { 2 } h + \cdots = h + t \frac { d } { d t } h + \frac { t ^ { 2 } } { 2 ! } \frac { d ^ { 2 } } { d t ^ { 2 } } h + \cdots = h \circ \Phi _ { t , f } .
$$

If we substitute $h$ by the flow map of a second vector field $\pmb { g }$ , then we obtain the composition formula

$$
\pmb { \phi } _ { t , f } \circ \pmb { \phi } _ { t , g } = \mathsf { e } ^ { t L _ { g } } \circ \pmb { \phi } _ { t , f } = \mathsf { e } ^ { t L _ { g } } \mathsf { e } ^ { t L _ { f } } \pmb { \mathrm { i } } \mathbf { d } .
$$

Note that the order of the exponentials is opposite to what one might have expected.

Using exponential notation, a first-order composition method, corresponding to the differential equation

$$
\frac { d } { d t } z = \pmb { f } ( z ) + \pmb { g } ( z ) ,
$$

can now be written as

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t , t } \circ \pmb { \phi } _ { \Delta t , g } = \mathrm { e } ^ { \Delta t L _ { g } } \mathrm { e } ^ { \Delta t L _ { f } } \mathbf { i } \mathbf { d } .
$$

For

$$
\pmb { f } = \left[ - \pmb { 0 } ^ { \phantom { \dagger } } \right] \quad \mathrm { a n d } \quad \pmb { g } = \left[ \pmb { M } ^ { - 1 } \pmb { p } ^ { \phantom { \dagger } } \right] ,
$$

this composition method corresponds to the symplectic Euler-A method

$$
\begin{array} { l } { { { \pmb q } ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb M } ^ { - 1 } { \pmb p } ^ { n } , } } \\ { { { \pmb p } ^ { n + 1 } = { \pmb p } ^ { n } - \Delta t \nabla _ { \pmb q } V ( { \pmb q } ^ { n + 1 } ) . } } \end{array}
$$

The BCH formula can be generalized to interpret the composition method (5.34) as the “exact” solution of a modified problem. The only formal modification necessary is to replace the matrix commutator by the Lie commutator10

$$
\left[ L _ { f } , L _ { g } \right] : = L _ { g } L _ { f } - L _ { f } L _ { g } .
$$

Thus we, formally, obtain the modified differential equation

$$
\frac { d } { d t } z = \tilde { { \boldsymbol { f } } } ( { \boldsymbol { z } } ; \Delta t ) ,
$$

with

$$
\begin{array} { r } { \mathrm { e } ^ { \Delta t L _ { \tilde { r } _ { \mathbf { i } } \mathbf { i } } } \mathrm { d } = \left( \mathbf { i } \mathbf { d } + \Delta t L _ { g } + \frac { \Delta t ^ { 2 } } { 2 ! } L _ { g } ^ { 2 } + \cdots \right) \left( \mathbf { i } \mathbf { d } + \Delta t L _ { f } + \frac { \Delta t ^ { 2 } } { 2 ! } L _ { f } ^ { 2 } + \cdots \right) \mathbf { i } \mathbf { d } } \\ { = \left( \mathbf { i } \mathbf { d } + \Delta t ( L _ { f } + L _ { g } ) + \frac { \Delta t ^ { 2 } } { 2 } \left( ( L _ { f } + L _ { g } ) ^ { 2 } + [ L _ { f } , L _ { g } ] \right) + \cdots \right) \mathbf { i } \mathbf { d } } \end{array}
$$

and, consequently

$$
L _ { \tilde { f } } = L _ { f } + L _ { g } + \frac { \Delta t } { 2 } [ L _ { f } , L _ { g } ] + \mathcal { O } ( \Delta t ^ { 2 } ) .
$$

Unlike the linear case, this series does not, in general, converge. A similar statement follows for the second-order splitting

$$
\boldsymbol { \psi } _ { \Delta t } = \boldsymbol { \Phi } _ { \Delta t / 2 , f } \circ \boldsymbol { \phi } _ { \Delta t , g } \circ \boldsymbol { \phi } _ { \Delta t / 2 , f } = \mathrm { e } ^ { ( \Delta t / 2 ) L _ { f } } \circ \mathrm { e } ^ { \Delta t L _ { g } } \circ \mathrm { e } ^ { ( \Delta t / 2 ) L _ { f } } \mathrm { i } \mathbf { d } ,
$$

which is, formally, obtained from (5.32) by substituting $\pmb { A }$ by $L _ { f }$ and $B$ by $L _ { g }$ , respectively.

10The definition (5.35) is sometimes replaced by

$$
\left[ L _ { f } , L _ { g } \right] : = L _ { f } L _ { g } - L _ { g } L _ { f } .
$$

We prefer (5.35) because of its natural link to the Poisson bracket. See (5.38).

Let us now assume that the two vector fields $\boldsymbol { f }$ and $\pmb { g }$ are Hamiltonian. We introduce the notation

$$
L _ { H } : = L _ { \{ \mathbf { i d } , H \} }
$$

to denote the differential operator $L _ { f }$ corresponding to the Hamiltonian vector field $\pmb { f } = \{ \mathbf { i d } , H \}$ with Hamiltonian $H$ and Lie–Poisson bracket $\{ . , . \}$ . Note that $L _ { H } f = \{ f , H \}$ [7]. For example, the Euler-A method can be written as

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t , V } \circ \pmb { \phi } _ { \Delta t , T } = \mathrm { e } ^ { \Delta t L _ { T } } \mathrm { e } ^ { \Delta t L _ { V } } \mathbf { i } \mathbf { d } .
$$

This method is symplectic and gives rise to a modified Hamiltonian differential equation

$$
\cfrac { d } { d t } z = \tilde { \pmb { f } } ( z ; \Delta t ) = J \nabla _ { z } \tilde { H } ( z ; \Delta t ) ,
$$

with modified Hamiltonian $\tilde { H } ( \Delta t )$ . Again the BCH formula can be used. We just have to note that the commutator of two Hamiltonian vector fields $H _ { 1 }$ and $H _ { 2 }$ is related to the Poisson bracket of the two corresponding Hamiltonian functions via the formula

$$
L _ { \{ H _ { 1 } , H _ { 2 } \} } = [ L _ { H _ { 1 } } , L _ { H _ { 2 } } ] .
$$

Thus we obtain for the Euler-A method the modified Hamiltonian

$$
\tilde { H } = T + V + \frac { \Delta t } { 2 } \{ V , T \} + \frac { \Delta t } { 1 2 } \left( \{ V , \{ V , T \} \} + \{ T , \{ T , V \} \} \right) + \cdots .
$$

Note that $\{ V , T \} ( \pmb { q } , \pmb { p } ) = \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \nabla _ { \pmb { q } } V ( \pmb { q } )$ and we recover the modified Hamiltonian $\tilde { H } _ { 1 } ( \Delta t )$ from Section 5.1.2. The second-order splitting (5.37) becomes

$$
\pmb { \psi } _ { \Delta t } = \mathrm { e } ^ { ( \Delta t / 2 ) L _ { H _ { 1 } } } \mathrm { e } ^ { \Delta t L _ { H _ { 2 } } } \mathrm { e } ^ { ( \Delta t / 2 ) L _ { H _ { 1 } } } \mathbf { i d } ,
$$

with modified Hamiltonian

$$
\tilde { \cal H } = { \cal H } _ { 1 } + { \cal H } _ { 2 } + { \frac { \Delta t ^ { 2 } } { 2 4 } } ( 2 \{ { \cal H } _ { 2 } , \{ { \cal H } _ { 2 } , { \cal H } _ { 1 } \} \} - \{ { \cal H } _ { 1 } , \{ { \cal H } _ { 1 } , { \cal H } _ { 2 } \} \} ) + \cdots .
$$

In particular, the St¨ormer–Verlet method corresponds to the second-order splitting (5.39) with $H _ { 1 } = V$ and $H _ { 2 } = \tau$ where $T = \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } / 2$ and $V = V ( \pmb q )$ . In other words, using exponential notation, the St¨ormer–Verlet method can be written more compactly as

$$
\pmb { \psi } _ { \Delta t } = \mathrm { e } ^ { ( \Delta t / 2 ) L _ { V } } \mathrm { e } ^ { \Delta t L _ { T } } \mathrm { e } ^ { ( \Delta t / 2 ) L _ { V } } \mathbf { i d } ,
$$

and the first terms of the modified Hamiltonian $\tilde { H } ( \Delta t )$ can be obtained from (5.40).

In summary, the Baker–Campbell–Hausdorff formula, originally derived for the composition of matrix exponentials, and a Lie algebraic treatment of composition methods are very useful for the derivation of higher-order methods and for the development of a backward error analysis. In this context, we like to mention, in particular, the work of DRAGT AND FINN [51], NERI [145], DRAGT et al. [52], SUZUKI [188, 189], and YOSHIDA [205].

# 5.5 Exercises

1. Modified equations. Find the exact modified equations for the symplectic scheme

$$
q ^ { n + 1 } = q ^ { n } + \Delta t p ^ { n + 1 } , \qquad p ^ { n + 1 } = p ^ { n } - \Delta t \omega ^ { 2 } q ^ { n } .
$$

Recall the discussion in Section 2.6 of Chapter 2.

2. Conservation of first integrals. Show that the modified equations exactly conserve a first integral if the method does so. Hint: follow the proof of Theorem 1, denote the first integral by $G ( z )$ , and consider the behavior of the function

$$
F _ { \tau } = \frac { 1 } { \tau ^ { i + 2 } } \left[ G ( \pmb { \phi } _ { \tau } ) - G ( \pmb { \psi } _ { \tau } ) \right] ,
$$

where Φτ = Φτ,f˜(τ).

3. Time-reversible methods and modified equations. Show that the modified equations are time reversible if the method is time reversible. Hint: note that time reversibility of a method is equivalent to (compare Chapter 4)

$$
\pmb { \psi } _ { \Delta t } \circ ( \pmb { S } \pmb { \psi } _ { \Delta t } \circ \pmb { S } ) - \mathbf { i d } = \pmb { 0 } .
$$

Use this fact to find an appropriate function $F _ { \tau }$ as used in the proof of Theorem 1.

4. Symmetric methods and modified equations. Show that the modified vector field expansion (5.7) contains only terms of even power in $\Delta t$ if the numerical method $\psi _ { \Delta t }$ is symmetric, i.e.

$$
{ \pmb { \psi } } _ { - \Delta t } = \left[ { \pmb { \psi } } _ { \Delta t } \right] ^ { - 1 } .
$$

This result implies that the order of a symmetric method is necessarily even (see Theorem 1 in Section 4.3.3. Hint: the flow map of the modified vector

field

$$
\tilde { \pmb f } ( \Delta t ) = \sum _ { i } \Delta t ^ { i } \delta \pmb f _ { i }
$$

satisfies

$$
\pmb { \phi } _ { - \Delta t , \tilde { t } ( \Delta t ) } = \left[ \pmb { \phi } _ { \Delta t , \tilde { t } ( \Delta t ) } \right] ^ { - 1 } = \pmb { \phi } _ { \Delta t , - \tilde { t } ( \Delta t ) } ,
$$

which gives the modified vector field for the map $[ { \pmb { \psi } } _ { \Delta t } ] ^ { - 1 }$ . Show also that ${ \pmb { \psi } } _ { - \Delta t }$ has the modified vector field

$$
\hat { \pmb f } ( \Delta t ) = \sum _ { i } ( - \Delta t ) ^ { i } \delta \pmb f _ { i } .
$$

Finally, use (5.41) and compare the corresponding modified vector fields.

5. Canonical point transformation. Prove that the transformation (5.29)–(5.30) is the flow map of the Hamiltonian vector field with Hamiltonian $F = p ^ { T } f ( q )$ . Hint: Rewrite (5.30) as

$$
\left[ \nabla _ { q } \phi _ { \tau } ( q ) \right] \bar { p } ( \tau ) = p ,
$$

differentiate with respect to $\tau$ , and set $\tau = 0$ .

6. Kepler problem and modified equations. Apply the St¨ormer–Verlet method to the planar Kepler problem

$$
H ( \pmb { q } , \pmb { p } ) = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { p } - \frac { 1 } { | | \pmb { q } | | } , \qquad \pmb { q } , \pmb { p } \in \mathbb { R } ^ { 2 } .
$$

Use the BCH formula (5.40) to compute the second-order corrections of the modified Hamiltonian $\tilde { H }$ for this particular problem. Verify the fourth-order convergence of the St¨ormer–Verlet method with respect to the modified Hamiltonian $\tilde { H } _ { 2 }$ numerically. Take, for $\mathsf { e x }$ ample, initial conditions $\pmb { q } = ( 1 , 0 ) ^ { T }$ and $\pmb { p } = ( 0 , 1 ) ^ { T }$ .

7. BCH formula. Verify the first two terms in the BCH formula (5.36) for the composition of two vector field exponentials

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t , t } \circ \pmb { \phi } _ { \Delta t , g } = \mathrm { e } ^ { \Delta t L _ { g } } \mathrm { e } ^ { \Delta t L _ { f } } \mathbf { i } \mathbf { d } .
$$

Also verify that the next term in the expansion is equal to

$$
\frac { \Delta t ^ { 2 } } { 1 2 } \left( [ L _ { f } , [ L _ { f } , L _ { g } ] ] + [ L _ { g } , [ L _ { g } , L _ { f } ] ] \right) .
$$

7. Lie derivatives. Verify formula (5.38), i.e. show that

$$
L _ { \{ H _ { 1 } , H _ { 2 } \} } f = L _ { H _ { 1 } } [ L _ { H _ { 2 } } f ] - L _ { H _ { 2 } } [ L _ { H _ { 1 } } f ] = \left( L _ { H _ { 1 } } L _ { H _ { 2 } } - L _ { H _ { 2 } } L _ { H _ { 1 } } \right) f ,
$$

by using $L _ { H } f = \{ f , H \}$ , $\{ f , g \} = - \{ g , f \}$ , and the Jacobi identity [7]

$$
\{ \{ f , g \} , h \} + \{ \{ g , h \} , f \} + \{ \{ h , f \} , g \} = 0 .
$$

8. Conservation of modified energy. If one is only interested in monitoring the conservation of a more accurate energy expression, then one does not necessarily have to use a modified Hamiltonian $\tilde { H } ( q , p ; \Delta t )$ as previously discussed. This has been pointed out by SKEEL AND HARDY [177] who gave a practical construction for high-order modified energies. Below we describe a somewhat similar approach which has been used by MOORE AND REICH [137] to verify numerical energy conservation laws for Hamiltonian PDEs. The idea has also been used by HAIRER AND LUBICH to prove conservation of energy for the St¨ormer–Verlet and related methods [81].

We write the St¨ormer–Verlet method in its leapfrog form

$$
\frac { { \pmb q } ^ { n + 1 } - 2 { \pmb q } ^ { n } + { \pmb q } ^ { n - 1 } } { \Delta t ^ { 2 } } = - \nabla _ { \pmb q } V ( { \pmb q } ) .
$$

a. Show that

$$
\frac { q ( t _ { n } + \Delta t ) - 2 q ( t _ { n } ) + q ( t _ { n } - \Delta t ) } { \Delta t ^ { 2 } } = \ddot { q } ( t _ { n } ) + \frac { \Delta t ^ { 2 } } { 1 2 } q ^ { ( 4 ) } ( t _ { n } ) + \mathcal { O } ( \Delta t ^ { 4 } ) ,
$$

where $q ( t )$ is sufficiently smooth.

b. We use the result to formulate the following modified equation

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } \pmb { q } + \frac { \Delta t ^ { 2 } } { 1 2 } \frac { d ^ { 4 } } { d t ^ { 4 } } \pmb { q } = - \nabla _ { \pmb { q } } V ( \pmb { q } )
$$

for the leapfrog method. Show that

$$
E = { \frac { 1 } { 2 } } \| { \dot { \pmb q } } \| ^ { 2 } + V ( { \pmb q } ) + { \frac { \Delta t ^ { 2 } } { 1 2 } } \left[ { \dot { \pmb q } } \cdot { \pmb q } ^ { ( 3 ) } - { \frac { 1 } { 2 } } \| { \dot { \pmb q } } \| ^ { 2 } \right]
$$

is conserved along the solutions of the modified equations (5.42).

c. Show that the modified equation (5.42) is the Euler–Lagrange equation for the Lagrangian functional

$$
\mathcal { L } [ \pmb { q } ] = \int _ { t _ { 0 } } ^ { t _ { 1 } } \left[ \frac { 1 } { 2 } \| \pmb { \dot { \dot { \mathbf { q } } } } \| ^ { 2 } - V ( \pmb { q } ) - \frac { \Delta t ^ { 2 } } { 2 4 } \| \pmb { \dot { \dot { \mathbf { q } } } } \| ^ { 2 } \right] d t .
$$

d. How would you verify numerically that the modified energy (5.43) is preserved to fourth-order along numerical solutions $\{ \pmb q ^ { n } \} .$ Hint: See [137].

# 6

# Higher-order methods

In Chapter 4, we introduced several first- and second-order symplectic integration methods for Hamiltonian systems. In this chapter, we will discuss the construction of “higher-order” symplectic methods (with order greater than two), focusing in particular on those types of schemes that have been found to be most useful for practical computations. In traditional practice, higher-order integrators are employed for solving problems with relatively smooth solutions, such as gravitational simulations (solar system simulations, satellite trajectories). They are also traditionally used for many types of computations when very high accuracy (for example near the rounding error of the computer) is desired.

As we have seen in Chapter 2, the appropriateness of a given numerical method for a given computational task is a complicated issue. In some cases, the principles of geometric integration are in contradiction with the demand for high accuracy. If the purpose of simulation is to reconstruct, as exactly as possible, a particular trajectory segment, it may not matter what sort of qualitative features the integrator possesses: the efficiency of the integration method in terms of solution error per unit work is instead of paramount importance. Since the development of symplectic integrators adds a number of additional constraints on the design of the method, such schemes typically sacrifice something in efficiency compared with their nonsymplectic counterparts at similar accuracy, for example requiring an extra force evaluation or two at each timestep. Thus the problem of correctly determining the precise entry point and time instant that a space probe arrives at the Martian atmosphere is a task best handled by a standard integration method, for example, a high-order multistep integrator (for example, DIVA [99]) or explicit Runge–Kutta method (for example, RKSUITE [29]). These methods are well-suited to short time integration at extreme high accuracy.

On the other hand, it is often the case that integrations are carried out on terrifically long time intervals, or with respect to a large set of initial data. The goal is to accurately represent the qualitative long-term dynamics of the model, but some tolerance of individual trajectory error may be acceptable. Examples where this is the case include studies of the stability of the solar system, planet formation, and stellar cluster evolution. In some of the outer solar system simulations of SUSSMAN AND WISDOM for example, the computation was performed on a time interval of 100 million years [187], and more recent simulations have pushed the time intervals into the billions of years. On such time intervals, even the trajectories of the relatively slow-moving outer planets cannot be resolved to very high accuracy. Instead, the goal of these types of calculations is generally to obtain a useful, qualitatively correct result regarding a robust pattern in the long-term evolution of the system. The particular initial conditions are chosen arbitrarily within some set, and the questions asked concern the generic behavior for initial conditions within this set. In this setting, the most natural and efficient scheme is often some sort of geometric integrator, for example a symplectic or time-symmetric method.

To clarify this discussion, consider the challenge of predicting collisions of the earth with near-earth asteroids using simulation. One might ask either of the following questions, which are answerable in part using simulation: (i) when will a given object next collide with the earth and with what impact force, or (ii) on average how often will the earth be hit by such an object and with what average impact force. If the problem at hand is similar to the first one, then the best method for simulation is likely to be a traditional, high-order integrator with optimized choice of integration parameters. If the problem is more like the second one, the use of a high-order symplectic method may be indicated. Note that each of the two types of problems also requires a suitable choice of data: very accurate initial data and parameters for questions of type (i) and perhaps a sampling from an appropriate range of suitable initial data and model parameters in the case (ii).

In summary, accurate simulation of nonlinear systems generally calls for a high-order method. On the other hand, the efficient solution of nonlinear systems over very long time intervals or with many initial points typically benefits from the preservation of geometric properties such as the symplectic structure or a reversing symmetry. In this chapter, we will explain how to develop methods to provide us with some of the best aspects of both worlds: high order to improve the accuracy of the method when high accuracy is needed, as well as conservation of available geometric structure.

# 6.1 Construction of higher-order methods

The design of a symplectic integrator of order $p \geq 1$ involves, roughly speaking, two steps. First a stepsize dependent family of symplectic maps,

$$
\begin{array} { r } { z ^ { n + 1 } = \pmb { \psi } _ { \Delta t } ( z ^ { n } ; \gamma _ { 1 } , \gamma _ { 2 } , \dots , \gamma _ { k } ) , } \end{array}
$$

is defined in terms of $k$ arbitrary parameters. The method is then “fine tuned” by adjusting the parameters so that the local error of the method is $O ( \Delta t ^ { p + 1 } )$

$$
\begin{array} { r } { \pmb { \psi } _ { \Delta t } ( z ) - \pmb { \phi } _ { \Delta t } ( z ) = \pmb { \mathcal { O } } ( \Delta t ^ { p + 1 } ) . } \end{array}
$$

In this chapter, we will discuss higher-order methods for general canonical Hamiltonian systems

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \pmb { q } = \nabla _ { p } H ( \pmb { q } , \pmb { p } ) , } \\ { \displaystyle \frac { d } { d t } \pmb { p } = - \nabla _ { \pmb { q } } H ( \pmb { q } , \pmb { p } ) ) , } \end{array}
$$

with an important special class of canonical systems obtained for Hamiltonian functions that are separable into kinetic and potential energy, i.e. of type

$$
H ( \pmb { q } , \pmb { p } ) = T ( \pmb { p } ) + V ( \pmb { q } ) .
$$

We cover several approaches to the derivation of higher-order methods: composition methods, classical Runge–Kutta (RK) as well as partitioned Runge–Kutta (PRK) methods, and methods based on generating functions.

Composition methods offer an attractive and inexpensive way to obtain higherorder symplectic methods. They only require either (1) a splitting of the Hamiltonian into two or more explicitly solvable subproblems or, if this is not available, (2) a symmetric second-order symplectic approximation. The latter approach can, of course, be applied to any Hamiltonian problem, whether or not a splitting can be identified. Composition methods are not restricted to Hamiltonian problems and provide a general, systematic way to construct higher-order methods that preserve underlying geometric properties of the analytic problem.

On the other hand, there is a very well-developed order theory for RK and PRK methods and we “only” have to identify those schemes within these classes that are symplectic. This and the mathematical elegance of RK methods have contributed to their great popularity, especially among numerical analysts. However, it appears that, for many problems, symplectic RK methods are necessarily implicit and therefore more expensive in their implementation and are outperformed by composition methods unless very high precision computations are required.

# 6.2 Composition methods

In this section, we introduce the composition method approach to higher-order integration of Hamiltonian systems. We begin our treatment with systems in separable Hamiltonian form. The reader is referred to the survey article by MCLACHLAN AND QUISPEL [132] for a general discussion of splitting and composition methods.

We also wish to point to NERI [145], FOREST AND RUTH [62], YOSHIDA [205], and SUZUKI [188]) for early contributions to the theory of composition methods and their application to symplectic integration.

# 6.2.1 Composition methods for separable Hamiltonian systems

Consider a separable Hamiltonian system

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \pmb q } = \nabla _ { \pmb { p } } T ( { \pmb p } ) } , } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = - \nabla _ { \pmb { q } } V ( { \pmb q } ) , } } \end{array}
$$

and observe that each of the two Hamiltonian subsystems

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \pmb q } = { \bf 0 } } , } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = - \nabla _ { { \pmb q } } V ( { \pmb q } ) , } } \end{array}
$$

and

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \pmb { q } = \nabla _ { p } T ( \pmb { p } ) , } \\ { \displaystyle \frac { d } { d t } p = \pmb { 0 } } \end{array}
$$

is exactly solvable. Let us denote the corresponding flow maps by $\psi _ { t , V }$ and $\psi _ { t , T }$ , respectively. First- and second-order methods can be obtained by simple compositions of these flow maps, as discussed in Chapters 4 and 5.

Here we will generalize this approach to methods of arbitrarily high order. For this purpose, we consider a multi-composition of the form

$$
\pmb { \psi } _ { \Delta t } : = \pmb { \phi } _ { c _ { s } \Delta t , V } \circ \pmb { \phi } _ { d _ { s } \Delta t , T } \circ \cdot \cdot \cdot \circ \pmb { \phi } _ { c _ { 1 } \Delta t , V } \circ \pmb { \phi } _ { d _ { 1 } \Delta t , T } \circ \pmb { \phi } _ { c _ { 0 } \Delta t , V } ,
$$

with $\{ c _ { i } \} _ { i = 0 , \dots , s }$ and $\{ d _ { i } \} _ { i = 1 , \dots , s }$ representing appropriate weight factors. The integer $S$ is termed the number of stages of the concatenation method.

A method is said to be consistent if the order is at least one, i.e., if the local error is at least $O ( \Delta t ^ { 2 } )$ . Let us determine the requirement on the method parameters in a composition method for consistency. Observe that the terms in (6.3) commute to second order, so we have, for example

$$
\begin{array} { r } { \pmb { \phi } _ { d _ { 1 } \Delta t , T } \circ \pmb { \phi } _ { c _ { 1 } \Delta t , V } = \pmb { \phi } _ { c _ { 1 } \Delta t , V } \circ \pmb { \phi } _ { d _ { 1 } \Delta t , T } + O ( \Delta t ^ { 2 } ) , } \end{array}
$$

We apply this fact recursively $s$ times and use the group property associated to the flow maps on $\tau$ and $V$ , for example

$$
\Phi _ { \alpha T } \circ \Phi _ { \beta T } = \Phi _ { ( \alpha + \beta ) T } ,
$$

for any scalar $\alpha , \beta$ . It follows that

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { ( d _ { 1 } + d _ { 2 } + . . . + d _ { s } ) \Delta t , T } \circ \pmb { \phi } _ { ( c _ { 0 } + c _ { 1 } + c _ { 2 } + . . . + c _ { s } ) \Delta t , V } + O ( \Delta t ^ { 2 } ) .
$$

Since consistency is to be a property of the method, and hence should hold independent of $T$ and $V$ , the following consistency conditions result

$$
\sum _ { i = 0 } ^ { s } c _ { i } = \sum _ { i = 1 } ^ { s } d _ { i } = 1 .
$$

Furthermore, if a consistent composition (6.3) is symmetric, i.e.

$$
c _ { i } = c _ { s - i } \qquad { \mathrm { a n d } } \quad d _ { i } = d _ { s + 1 - i } ,
$$

$i = 1 , \dots , s$ , then the method is automatically second order.

The St¨ormer–Verlet method (2.16)–(2.18) of Section 2.4 is obtained by choosing $s = 1$ , $c _ { 0 } = 1 / 2$ , $d _ { 1 } = 1$ , $c _ { 1 } = 1 / 2$ . The method is clearly consistent and symmetric; in fact, we have already pointed out in earlier chapters that this is a second-order method.

The conditions on the weight factors $C _ { I }$ and $d _ { j }$ to obtain order $p > 1$ can, for example, be obtained by a recursive application of the Baker–Campbell–Hausdorff formula (see Section 5.4). Another approach to derive order conditions uses an extension of Runge–Kutta rooted trees to composition methods [142].

Once the algebraic-order conditions are developed, it becomes an interesting challenge to find solutions to the resulting nonlinear system. Typically, one chooses the number of stages high enough so that, at a given order, there are too many parameters for the number of order conditions; one can then impose some additional conditions (such as minimization of some coefficient or coefficients appearing in the leading term of the error expansion) so that a (locally) unique and optimal solution is obtained.

In Table 6.1, we summarize two popular methods by providing the coefficients. Both methods have an even number of stages and are symmetric and, hence, we only have to give the first $s / 2$ coefficients. References are also given in this table to the publication where the method appeared. These methods can be applied to any canonical Hamiltonian system with separable Hamiltonian $H = T ( p ) + V ( q )$ . In fact, the listed methods can also be applied to any splitting $H = H _ { 1 } + H _ { 2 }$ with explicitly solvable Hamiltonian functions $H _ { 1 }$ and $H _ { 2 }$ .

Since the number of order conditions for general composition methods (6.3) rapidly grows with the desired order of the method, one may attempt to restrict the search for higher-order methods to methods based on the concatenation using a second-order symmetric method as discussed below.

Table 6.1 Symmetric composition methods for separable Hamiltonian systems   

<table><tr><td>stages</td><td>order</td><td>coefficients</td><td></td><td>reference</td></tr><tr><td rowspan="4">6</td><td rowspan="4">4</td><td>Co = 0.0792036964311957</td><td>dl = 0.209515106613362</td><td rowspan="4">BLANES&amp;</td></tr><tr><td>C1 = 0.353172906049774</td><td>d = -0.143851773179818</td></tr><tr><td>C = -0.0420650803577195</td><td>d=1/2-d-d</td></tr><tr><td>C=1-2(co+C+C2)</td><td></td></tr><tr><td rowspan="6">10</td><td rowspan="6">6</td><td>Co = 0.0502627644003922</td><td>di = 0.148816447901042</td><td rowspan="6">BLANES&amp;</td></tr><tr><td>Cl = 0.413514300428344</td><td>d2 = -0.132385865767784</td></tr><tr><td>C = 0.0450798897943977</td><td>d = 0.067307604692185</td></tr><tr><td>C3 = -0.188054853819569</td><td>d4 = 0.432666402578175</td></tr><tr><td>C4 = 0.541960678450780</td><td>d5=1/2- M 14 di</td></tr><tr><td>14</td><td>i=1</td></tr></table>

# 6.2.2 Composition methods based on second-order symmetric methods

It was observed by YOSHIDA [205] and SUZUKI [188]) that an efficient way to obtain higher-order methods for separable Hamiltonian systems is to restrict the search to methods based on the concatenation of a second-order symmetric method with stepsize $w \Delta t$ . For example, in the case of a separable Hamiltonian system, we might base this on

$$
\psi _ { w \Delta t } : = \pmb { \phi } _ { w \Delta t / 2 , T } \circ \pmb { \phi } _ { w \Delta t , V } \circ \pmb { \phi } _ { w \Delta t / 2 , T } .
$$

Here $w \neq 0$ is a free parameter. Note that ${ \pmb { \psi } } _ { w \Delta t }$ is a second-order approximation to the exact flow map $\Phi _ { t , H }$ with $t = w \Delta t$ .

Higher-order methods are constructed by $S ^ { \th }$ -fold concatenating ${ \pmb { \psi } } _ { w \Delta t }$ with different values for $W$ , i.e.

$$
\widetilde { \pmb { \psi } } _ { \Delta t } = \pmb { \psi } _ { w _ { s } \Delta t } \circ \pmb { \psi } _ { w _ { s - 1 } \Delta t } \circ \cdots \circ \pmb { \psi } _ { w _ { 2 } \Delta t } \circ \pmb { \psi } _ { w _ { 1 } \Delta t } ,
$$

with $\{ w _ { i } \} _ { i = 1 , \dots , s }$ as free parameters. We also require that the concatenation method (6.5) is symmetric, i.e.

$$
w _ { s + 1 - i } = w _ { i } , \qquad i = 1 , \dots , s ,
$$

and only consider odd values of $s$ . The reason for considering symmetric methods based on the composition of symmetric methods is twofold: (i) symmetric methods are always of even order (see Theorem 1 in Section 4.3.3) and time reversible, (ii) the odd power terms in the Taylor expansion of the local error vanish and, therefore, the order conditions simplify. We present three methods of type (6.5) in Table 6.2. Because of symmetry, we again only provide the $( s + 1 ) / 2$ first coefficients $W _ { j }$ .

Table 6.2 Symmetric composition methods based on a symmetric second-order method   

<table><tr><td>stages</td><td>order</td><td>coefficients</td><td>reference</td></tr><tr><td rowspan="3">5</td><td rowspan="3">4</td><td>W1=0.28</td><td rowspan="3">McLACHLAN[130]</td></tr><tr><td>W2 = 0.62546642846767004501 12</td></tr><tr><td>W3=1-2 i=1 Wi</td></tr><tr><td rowspan="4">7</td><td rowspan="4">6</td><td>Wl = 0.78451361047755726382</td><td rowspan="4">YoSHIDA[205]</td></tr><tr><td>W2 = 0.23557321335935813368</td></tr><tr><td>W3 = -1.17767998417887100695</td></tr><tr><td>3 W4=1-2 Wi</td></tr><tr><td rowspan="5">9</td><td rowspan="5">6</td><td>Wi=0.39216144400731413928</td><td rowspan="5">KAHAN AND LI[97]</td></tr><tr><td>W2 = 0.33259913678935943860</td></tr><tr><td>W3 = -0.70624617255763935981</td></tr><tr><td>W4 = 0.08221359629355080023</td></tr><tr><td>W5=1-2 14 -i=1 Wi</td></tr><tr><td rowspan="8">15</td><td rowspan="8"></td><td>Wl = .74167036435061295345</td><td rowspan="8">McLACHLAN[130]</td></tr><tr><td>W2 =-.40910082580003159400</td></tr><tr><td></td></tr><tr><td>W3= .19075471029623837995</td></tr><tr><td>W4 = -.57386247111608226666</td></tr><tr><td>W5 = .29906418130365592384</td></tr><tr><td>W6 = .33462491824529818378</td></tr><tr><td>W7= .31529309239676659663</td></tr><tr><td></td><td></td><td>Wi</td></tr></table>

For the concatenation methods (6.5) it is not essential that the method (6.4) is used. The necessary requirement is that the method is of one-step form, is second order and symmetric. For example, one could replace the method (6.4) by the standard St¨ormer–Verlet method (which is obtained from (6.4) by interchanging $V$ and $\tau$ ) or by the implicit midpoint rule. Thus, in contrast to (6.3), this concatenation method can also be used to obtain higher-order methods for general Hamiltonian systems (6.1)–(6.2) as long as we are able to identify a second-order and symmetric method $\psi _ { \Delta t }$ for the problem at hand.

# 6.2.3 Post-processing of composition methods

Composition methods of type (6.5) can be enhanced by the idea of postprocessing [117, 204, 131]. Introduce a coordinate transformation

$$
{ \widehat { z } } = \psi ( z ) ,
$$

and design a one-step method

$$
\widehat { \boldsymbol { z } } ^ { n + 1 } = \widehat { \pmb { { \psi } } } _ { \Delta t } ( \widehat { \boldsymbol { z } } ^ { n } ) ,
$$

such that the composed map

$$
\widetilde { \pmb { \psi } } _ { \Delta t } = \pmb { \psi } ^ { - 1 } \circ \widehat { \pmb { \psi } } _ { \Delta t } \circ \pmb { \psi }
$$

is a higher-order method for the given differential equation. Observe that

$$
\begin{array} { r l } & { \pmb { \widetilde { \psi } } _ { \Delta t } ^ { 2 } = \pmb { \psi } ^ { - 1 } \circ \pmb { \widehat { \psi } } _ { \Delta t } \circ \pmb { \psi } \pmb { \psi } ^ { - 1 } \circ \pmb { \widehat { \psi } } _ { \Delta t } \circ \pmb { \psi } } \\ & { \qquad = \pmb { \psi } ^ { - 1 } \circ \pmb { \widehat { \psi } } _ { \Delta t } ^ { 2 } \circ \pmb { \psi } , } \end{array}
$$

and, similarly

$$
\tilde { \pmb { { \psi } } } _ { \Delta t } ^ { m } = \pmb { { \psi } } ^ { - 1 } \circ \hat { \pmb { { \psi } } } _ { \Delta t } ^ { m } \circ \pmb { { \psi } } .
$$

Thus time integration is done in terms of the variable $\widehat { \boldsymbol { z } }$ with $\pmb { \psi }$ only applied infrequently whenever an output value is needed in terms of the original variable $z$ . Because of this, we can afford for $\pmb { \psi }$ to be relatively expensive to evaluate as long as $\widehat { \pmb { { \psi } } } _ { \Delta t }$ is “cheap.”

Now assume that we are given a second-order symmetric method

$$
z ^ { n + 1 } = \pmb { \psi } _ { \Delta t } ( z ^ { n } ) .
$$

As in Section 6.2.2, define a symmetric composition method of type (6.5) by ( $S$ odd)

$$
\begin{array} { r } { \widehat { \pmb { \psi } } _ { \Delta t } = \pmb { \psi } _ { w _ { 1 } \Delta t } \circ \pmb { \psi } _ { w _ { 2 } \Delta t } \circ \cdot \cdot \cdot \circ \pmb { \psi } _ { w _ { 2 } \Delta t } \circ \pmb { \psi } _ { w _ { 1 } \Delta t } , } \end{array}
$$

with $\{ w _ { i } \} _ { i = 1 , \dots , ( s + 1 ) / 2 }$ free parameters; i.e. the transformed variable $\widehat { \boldsymbol { z } }$ is updated according to (6.6) using (6.8). We still need the transformation $\psi$ . Here we use

$$
\psi = \pmb { \psi } _ { - c _ { m } \Delta t } \circ \pmb { \psi } _ { - c _ { m - 1 } \Delta t } \circ \cdot \cdot \cdot \circ \pmb { \psi } _ { - c _ { 1 } \Delta t } \circ \pmb { \psi } _ { c _ { m } \Delta t } \circ \pmb { \psi } _ { c _ { m - 1 } \Delta t } \circ \cdot \cdot \circ \pmb { \psi } _ { c _ { 2 } \Delta t } \circ \pmb { \psi } _ { c _ { 1 } \Delta t } ,
$$

with $\{ c _ { i } \} _ { i = 1 , \dots , m }$ as free parameters. Note that the inverse of $\pmb { \psi }$ is easy to compute since the basic method $\psi _ { \Delta t }$ is symmetric, i.e.

$$
\psi ^ { - 1 } = \pmb { \psi } _ { - c _ { 1 } \Delta t } \circ \pmb { \psi } _ { - c _ { 2 } \Delta t } \circ \cdot \cdot \cdot \circ \pmb { \psi } _ { - c _ { m } \Delta t } \circ \pmb { \psi } _ { c _ { 1 } \Delta t } \circ \pmb { \psi } _ { c _ { 2 } \Delta t } \circ \cdot \cdot \cdot \circ \pmb { \psi } _ { c _ { m - 1 } \Delta t } \circ \pmb { \psi } _ { c _ { m } \Delta t } .
$$

In Table 6.3 we give the coefficients for a sixth-order method due to BLANES [22]. Numerical comparisons of these methods can be found in Section 6.5.

# 6.3 Runge–Kutta methods

An alternative approach to higher-order integration is provided by the class of Runge–Kutta (RK) methods. It is well-known that certain implicit RK methods of Radau type (generalizing the implicit Euler method) are useful in the context of systems with strong dissipation, such as electronic circuits or chemical reaction dynamics. For these so-called stiff systems, implicit methods are often much more efficient than explicit methods. This is due to the inherent stepsize restriction of explicit methods in the context of strong dissipation (see, for example, [82, 84]). The situation is different for Hamiltonian systems for which, in general, implicit methods are found to be less competitive compared with the best explicit methods.

Table 6.3 Symmetric composition methods with post-processing   

<table><tr><td>stages</td><td>order</td><td>coefficients</td><td></td><td>reference</td></tr><tr><td>7</td><td>6</td><td>Wl = 0.513910778424374 W2 = 0.364193022833858</td><td>C1 =-(C2+C3+C4+C5) C2 = -0.461165940466494</td><td>BLANES[22]</td></tr></table>

The situation is slightly different for partitioned Runge–Kutta methods where explicit methods exist for separable Hamiltonian systems. However, these methods can also be discussed in the context of splitting methods [148, 172].

On the other hand, implicit Runge–Kutta and partitioned Runge–Kutta methods often provide the only reasonable means for symplectic treatment of nonseparable Hamiltonian systems. Below, we give a brief summary of the relevant issues for classical and partitioned Runge–Kutta methods.

# 6.3.1 Implicit Runge–Kutta methods

The general formula of an $S \cdot$ -stage Runge–Kutta method applied to a Hamiltonian system (6.1)–(6.2) is

$$
\begin{array} { l } { { Q _ { i } = q ^ { n } + \Delta t \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } , ~ } } \\ { { { } } } \\ { { P _ { i } = p ^ { n } + \Delta t \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } G _ { j } , ~ } } \\ { { { } } } \\ { { q ^ { n + 1 } = q ^ { n } + \Delta t \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } , } } \\ { { { } } } \\ { { p ^ { n + 1 } = p ^ { n } + \Delta t \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } G _ { i } . } } \end{array}
$$

with $s \geq 1$ the number of stages, $( Q _ { i } , P _ { i } ) , ~ i ~ = ~ 1 , \ldots , s$ , the internal stage

variables, and the abbreviations

$$
\begin{array} { l l } { { { \pmb F } _ { i } = + \nabla _ { p } H ( { \pmb Q } _ { i } , { \pmb P } _ { i } ) , \ } } & { { i = 1 , . . . , s , } } \\ { { { \pmb G } _ { i } = - \nabla _ { q } H ( { \pmb Q } _ { i } , { \pmb P } _ { i } ) , \ } } & { { i = 1 , . . . , s . } } \end{array}
$$

Recall that we called a Runge–Kutta method “explicit” in Section 2.4 if the coefficients $\{ a _ { i j } \}$ satisfy $a _ { i j } = 0$ for $j \geq i$ and implicit otherwise. For implicit methods, the equations (6.10)–(6.11) are, in general, a system of nonlinear equations which must be solved by some iterative method, such as Newton’s method or fixed-point iteration. Because implicit methods are based on iteration, and several force (or vector field) evaluations are needed at each timestep, they are typically more costly to implement than $\mathsf { e x }$ plicit methods. However, good starting approximations can greatly enhance the efficiency of the necessary iterative method. This has been discussed by HAIRER, LUBICH AND WANNER [80] and by CALVO AND PORTILLO [41].

An example of a symplectic Runge–Kutta method is provided by the implicit midpoint rule, which can be written as a one-stage $\langle s = 1$ ) RK method:

$$
\begin{array} { r } { Q _ { 1 } = \pmb { q } ^ { n } + \frac { \Delta t } { 2 } \nabla _ { p } H ( Q _ { 1 } , P _ { 1 } ) , } \\ { P _ { 1 } = \pmb { p } ^ { n } - \frac { \Delta t } { 2 } \nabla _ { q } H ( Q _ { 1 } , P _ { 1 } ) , } \\ { \pmb { q } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta t \nabla _ { p } H ( Q _ { 1 } , P _ { 1 } ) , } \\ { \pmb { p } ^ { n + 1 } = \pmb { p } ^ { n } - \Delta t \nabla _ { q } H ( Q _ { 1 } , P _ { 1 } ) . } \end{array}
$$

The corresponding coefficients in (6.10)–(6.13) are $a _ { 1 1 } = 1 / 2$ and $b _ { 1 } ~ = ~ 1$ . For a general (implicit) $S$ -stage $\mathsf { R K }$ method we have $s ^ { 2 }$ parameters $\{ a _ { i j } \}$ and $S$ parameters $\{ b _ { i } \}$ . Conditions on the parameters $\{ a _ { i j } \}$ and $\{ b _ { i } \}$ that insure a certain order of the corresponding method can be obtained by Taylor series expansion of the exact time- $\Delta t$ -flow map and its approximation generated by the RK method followed by a matching of the terms in $\Delta t$ up to the desired order of the method. Since the complexity of the resulting equations, or order conditions, increases rapidly with the desired order of the method, simplifying conditions are often introduced. This leads to special classes of $\mathsf { R K }$ methods like the Gauss-Legendre methods, the Radau methods, and the Lobatto methods which are all based on the idea of collocation. We refer the reader to the textbooks by HAIRER, NORSETT AND WANNER [82] and HAIRER AND WANNER [84] for a detailed exposition of this material.

Further restrictions apply if we demand that the RK method is symplectic. As first shown by SANZ-SERNA [170], LASAGNI [106], and SURIS [185] the conditions on the parameters $\{ a _ { i j } \}$ and $\{ b _ { i } \}$ are:

$$
b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } = 0 , \qquad i , j = 1 , \dots , s .
$$

Proof: It is convenient to first express the Runge–Kutta method in more compact form. We associate with any $S \cdot$ -stage Runge–Kutta method the $s \times s$ matrix $A = \left\{ \boldsymbol { a } _ { i j } \right\}$ and the column vector $b = \{ b _ { i } \}$ . We also introduce tensor product notation. The tensor product $\tau _ { \infty } s$ , of an arbitrary $m \times m$ matrix ${ \cal T } = \{ t _ { i j } \}$ and an arbitrary $n \times n$ matrix $S = \{ s _ { i j } \}$ , is a $k \times k$ matrix, $k = m n$ , defined by

$$
\pmb { T } \otimes \pmb { S } = \left[ \begin{array} { c c c c } { t _ { 1 1 } \pmb { S } } & { t _ { 1 2 } \pmb { S } } & { \cdot \cdot \cdot } & { t _ { 1 m } \pmb { S } } \\ { t _ { 2 1 } \pmb { S } } & { t _ { 2 2 } \pmb { S } } & { \cdot \cdot \cdot } & { t _ { 2 m } \pmb { S } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { t _ { m 1 } \pmb { S } } & { t _ { m 2 } \pmb { S } } & { \ldots } & { t _ { m m } \pmb { S } } \end{array} \right] .
$$

An account of the properties of tensor products is given by LANCHESTER [103]. For our purposes it is sufficient to know that

$$
( R \otimes { \pmb S } ) ( { \pmb T } \otimes { \pmb S } ) = ( R { \pmb T } ) \otimes { \pmb S } ,
$$

whenever the products are defined.

Using tensor product notation, a $\mathsf { R K }$ method (6.10)–(6.13) can be compactly rewritten as

$$
\begin{array} { c } { q ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t ( { \pmb b } ^ { T } \otimes { \pmb I } ) { \pmb F } , } \\ { p ^ { n + 1 } = { \pmb p } ^ { n } + \Delta t ( { \pmb b } ^ { T } \otimes { \pmb I } ) { \pmb G } , } \\ { { \pmb Q } = { \pmb e } \otimes { \pmb q } ^ { n } + \Delta t ( { \pmb A } \otimes { \pmb I } ) { \pmb F } , } \\ { { \pmb P } = { \pmb e } \otimes { \pmb p } ^ { n } + \Delta t ( { \pmb A } \otimes { \pmb I } ) { \pmb G } , } \end{array}
$$

where $\pmb { e } = [ 1 , 1 , \dots , 1 ] ^ { T } \in \mathbb { R } ^ { s } , \pmb { I } \in \mathbb { R } ^ { d \times d }$ is the identity matrix, and

$$
\begin{array} { r } { Q = \left[ \begin{array} { c } { Q _ { 1 } } \\ { Q _ { 2 } } \\ { \vdots } \\ { Q _ { s } } \end{array} \right] \in \mathbb { R } ^ { s d } , \qquad F = \left[ \begin{array} { c } { F _ { 1 } } \\ { F _ { 2 } } \\ { \vdots } \\ { F _ { s } } \end{array} \right] \in \mathbb { R } ^ { s d } , } \end{array}
$$

etc. The linearization of a RK method (6.10)–(6.13) is now implicitly defined by the system

$$
\begin{array} { c } { d pmb { q } ^ { n + 1 } = d \pmb { q } ^ { n } + \Delta t ( \pmb { b } ^ { T } \otimes \pmb { I } ) d \pmb { F } , } \\ { d \pmb { p } ^ { n + 1 } = d \pmb { p } ^ { n } + \Delta t ( \pmb { b } ^ { T } \otimes \pmb { I } ) d \pmb { G } , } \\ { d \pmb { Q } = \pmb { e } \otimes d \pmb { q } ^ { n } + \Delta t ( \pmb { A } \otimes \pmb { I } ) d \pmb { F } , } \\ { d \pmb { P } = \pmb { e } \otimes d \pmb { p } ^ { n } + \Delta t ( \pmb { A } \otimes \pmb { I } ) d \pmb { G } . } \end{array}
$$

where $d F = F _ { Q } d Q + F _ { P } d P$ etc. It is important to keep in mind that, because we started from a Hamiltonian system

$$
F _ { Q } = - { \cal G } _ { P } ^ { T } , \quad F _ { P } = F _ { P } ^ { T } , \quad G _ { Q } = G _ { Q } ^ { T } .
$$

The first two equations (6.15)–(6.16) are combined to give

$$
\begin{array} { r } { \frac { d q ^ { n + 1 } \wedge d p ^ { n + 1 } - d q ^ { n } \wedge d p ^ { n } } { \Delta t } = d q ^ { n } \wedge ( b ^ { T } \otimes I ) d G - d p ^ { n } \wedge ( b ^ { T } \otimes I ) d F + } \\ { \qquad \Delta t ( b ^ { T } \otimes I ) d F \wedge ( b ^ { T } \otimes I ) d G \qquad } \\ { = d q ^ { n } \wedge ( b ^ { T } \otimes I ) d G - d p ^ { n } \wedge ( b ^ { T } \otimes I ) d F + } \\ { \qquad \Delta t d F \wedge ( b b ^ { T } \otimes I ) d G . \qquad } \end{array}
$$

Next we introduce the diagonal matrix $\boldsymbol { B } \in \mathbb { R } ^ { s \times s }$ via $B e = b$ . Hence we obtain from (6.17)–(6.18) the identities

$$
\begin{array} { r l } & { d Q \wedge ( B \otimes I ) d G = e \otimes d \pmb { q } ^ { n } \wedge ( B \otimes I ) d \pmb { G } + \Delta t ( \pmb { A } \otimes I ) d \pmb { F } \wedge ( \pmb { B } \otimes I ) d \pmb { G } } \\ & { \qquad = d \pmb { q } ^ { n } \wedge ( \pmb { b } ^ { T } \otimes I ) d \pmb { G } + \Delta t d \pmb { F } \wedge ( \pmb { A } ^ { T } \pmb { B } \otimes I ) d \pmb { G } , } \end{array}
$$

and

$$
\begin{array} { r l } & { d P \wedge ( B \otimes I ) d F = e \otimes d p ^ { n } \wedge ( B \otimes I ) d F + \Delta t ( A \otimes I ) d G \wedge ( B \otimes I ) d F } \\ & { \qquad = d p ^ { n } \wedge ( b ^ { T } \otimes I ) d F - \Delta t d F \wedge ( B ^ { T } A \otimes I ) d G . } \end{array}
$$

These three equations, obtained so far, can be combined into a single equation

$$
\begin{array} { r } { \frac { d \pmb { q } ^ { n + 1 } \wedge d \pmb { p } ^ { n + 1 } - d \pmb { q } ^ { n } \wedge d \pmb { p } ^ { n } } { \Delta t } = \Delta t d \pmb { F } \wedge \left( \left\{ b \pmb { b } ^ { T } - \pmb { B } \pmb { A } - \pmb { A } ^ { T } \pmb { B } \right\} \otimes \pmb { I } \right) d \pmb { G } + } \\ { + d \pmb { Q } \wedge ( \pmb { B } \otimes \pmb { I } ) d \pmb { G } - d \pmb { P } \wedge ( \pmb { B } \otimes \pmb { I } ) d \pmb { F } . } \end{array}
$$

The symplecticity condition (6.14) is equivalent to

$$
B A + A ^ { T } B - b b ^ { T } = \mathbf { 0 } .
$$

Furthermore, since (6.19)

$$
\begin{array} { r l } & { d Q \wedge ( B \otimes I ) d G - d P \wedge ( B \otimes I ) d F = d Q \wedge ( B \otimes I ) G _ { P } d P - } \\ & { ~ - d P \wedge ( B \otimes I ) F _ { Q } d Q } \\ & { ~ = - d P \wedge ( B \otimes I ) \left\{ F _ { Q } + G _ { P } ^ { T } \right\} d Q } \\ & { ~ = 0 . } \end{array}
$$

Table 6.4 Coefficients for the two-stage Gauss–Legendre method of orders 4 and 6   

<table><tr><td>4th order/2 stage a=-</td><td>a11=</td><td></td><td>12=-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>21=</td><td></td><td></td><td></td><td></td><td>22=</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>=+</td><td></td><td>b1=</td><td></td><td></td><td></td><td></td><td>b2=</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6th order/3 stage</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1 C1=</td><td>15</td><td>a11=</td><td>A</td><td></td><td></td><td>a12=</td><td>2</td><td></td><td>√15 15</td><td></td><td>5</td><td>√15 30</td></tr><tr><td>10</td><td></td><td>a21=</td><td>3</td><td>+</td><td>V15</td><td></td><td></td><td></td><td></td><td></td><td></td><td>√15</td></tr><tr><td>=</td><td></td><td></td><td></td><td></td><td>24 会</td><td></td><td>2</td><td>+</td><td>V15</td><td></td><td>5</td><td>23=-</td></tr><tr><td>8=+</td><td></td><td>a31=</td><td>品</td><td>+</td><td></td><td>a32=</td><td></td><td>15</td><td></td><td>a33=</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>b1=</td><td></td><td></td><td>b=</td><td></td><td></td><td></td><td>b3=</td><td></td><td></td></tr></table>

Thus

$$
d { \pmb q } ^ { n + 1 } \wedge d { \pmb p } ^ { n + 1 } = d { \pmb q } ^ { n } \wedge d { \pmb p } ^ { n } ,
$$

as desired.

Upon setting $j = j$ in (6.14), we obtain $2 a _ { i i } - b _ { i } = 0$ for $b _ { i } \neq 0$ , which implies that $a _ { i i } \neq 0$ . Thus we obtain the following important restriction on symplectic $\mathsf { R K }$ methods:

Lemma 1 Symplectic Runge–Kutta methods are necessarily implicit, i.e., $a _ { i j } \neq$ 0 for some $i , j \in \{ 1 , \dots , s \}$ , $j \geq j$ . ✷

Among implicit $\mathsf { R K }$ methods, the Gauss–Legendre methods can be shown to satisfy (6.14) [39]. For example, the two-stage Gauss–Legendre method given in Table 6.4 is fourth order and symplectic. The additional coefficients $C _ { I }$ are needed when solving time-dependent Hamiltonian problems. Specifically, each stage variable $( Q _ { i } , P _ { i } )$ is an approximation to the exact solution at time $t _ { i } =$ $t _ { n } + c _ { i } \Delta t$ .

More generally, Gauss–Legrendre methods with $s \geq 1$ stages are of order $p = 2 s$ . This is the optimal order obtainable for a given number of stages among all possible symplectic collocation Runge–Kutta methods.

Implicit RK methods require the solution of the nonlinear equations (6.10)– (6.11). In general, these nonlinear equations can be solved by Newton’s method, but this task requires the computation of the Jacobian and its inverse. This can be avoided provided the stepsize $\Delta t$ is small enough. In this case, the following fixed-point iteration can be used instead of Newton’s method:

For $I = 1 , \ldots$ , till convergence

$$
\begin{array} { l } { { Q _ { i } ^ { I } = { \pmb q } ^ { n } + \Delta t \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } { \cal F } _ { j } ^ { I - 1 } , \quad i = 1 , \ldots , s , } } \\ { { \nonumber } } \\ { { P _ { i } ^ { I } = p ^ { n } + \Delta t \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } { \cal G } _ { j } ^ { I - 1 } , \quad i = 1 , \ldots , s , } } \end{array}
$$

with

$$
\begin{array} { r } { \pmb { F } _ { j } ^ { I - 1 } = + \nabla _ { p } H ( \pmb { Q } _ { j } ^ { I - 1 } , \pmb { P } _ { j } ^ { I - 1 } ) , } \\ { \pmb { G } _ { j } ^ { I - 1 } = - \nabla _ { q } H ( \pmb { Q } _ { j } ^ { I - 1 } , \pmb { P } _ { j } ^ { I - 1 } ) } \end{array}
$$

and initial values $\pmb { Q } _ { j } ^ { 0 } = \pmb { q } ^ { n } , P _ { j } ^ { 0 } = \pmb { p } ^ { n } .$

It is worth pointing out that the condition (6.14) also implies that the corresponding Runge–Kutta method exactly preserves any quadratic first integral of the form

$$
\boldsymbol { I } = \boldsymbol { z } ^ { T } \boldsymbol { C } \boldsymbol { z } + \boldsymbol { d } ^ { T } \boldsymbol { z } , \quad \boldsymbol { z } = ( \boldsymbol { q } , \boldsymbol { p } ) ^ { T } ,
$$

$C \in \mathbb { R } ^ { 2 d \times 2 d }$ a symmetric matrix and $\pmb { d } \in \mathbb { R } ^ { 2 d }$ a vector. For example, the Gauss– Legendre methods exactly preserve total linear and angular momentum for Hamiltonian systems with pairwise distance-dependent interactions. They also conserve the Hamiltonian of linear systems since the Hamiltonian $H$ is quadratic in $\pmb q$ and $\pmb { p }$ . The proof of this result has been given by COOPER [46] and is analogous to a result given below for integrals of partitioned Runge–Kutta methods.

# 6.3.2 Partitioned Runge–Kutta methods

Runge–Kutta methods were designed for general differential equations without assuming that the phase space variable $z$ can be partitioned into two sets of variables $\pmb q$ and $p$ as is the case for canonical Hamiltonian systems (6.1)–(6.2). Examining (6.10)–(6.13), it seems natural to use a different set of parameters $\{ a _ { i j } \}$ and $\{ b _ { i } \}$ for each variable $\pmb q$ and $p$ . Let us denote these parameter sets by $\{ \widehat { a } _ { i j } \}$ , $\{ \widehat { b } _ { i } \}$ and $\{ \widetilde { a } _ { i j } \} , \ \{ \widetilde { b } _ { i } \}$ , respectively. This leads us to the class of partitioned Runge–Kutta (PRK) methods (already introduced in Section 2.5)

$$
\pmb { Q } _ { i } = \pmb { q } ^ { n } + \Delta t \sum _ { j = 1 } ^ { s } \widehat { \sf a } _ { i j } \pmb { F } _ { j } , \qquad i = 1 , \ldots , s ,
$$

$$
\begin{array} { l } { { P _ { i } = p ^ { n } + \Delta t \displaystyle \sum _ { j = 1 } ^ { s } \widetilde { a } _ { i j } \pmb { G } _ { j } , \qquad i = 1 , \dots , s , } } \\ { { \mathrm { } } } \\ { { \displaystyle q ^ { n + 1 } = q ^ { n } + \Delta t \displaystyle \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } F _ { i } , } } \\ { { \displaystyle p ^ { n + 1 } = p ^ { n } + \Delta t \displaystyle \sum _ { i = 1 } ^ { s } \widetilde { b } _ { i } \pmb { G } _ { i } , } } \end{array}
$$

with $S$ again the number of stages and $F _ { j }$ and $G _ { j }$ defined as before for RK methods. Thus we now have $2 s ( s + 1 )$ free parameters to obtain a certain order and to guarantee symplecticness. Order conditions for PRK methods are derived in the same way as for implicit $\mathsf { R K }$ methods and we again refer the interested reader to the textbooks by HAIRER, NORSETT, AND WANNER [82] and HAIRER AND WANNER [84].

The conditions for a PRK method to be symplectic are:

# CONDITION OF SYMPLECTICNESS FOR PARTITIONED RK METHODS

$$
\begin{array} { r l } { \widehat { b } _ { i } \widetilde { a } _ { i j } + \widetilde { b } _ { j } \widehat { a } _ { j j } - \widehat { b } _ { i } \widetilde { b } _ { j } = 0 , } & { \quad i , j = 1 , \ldots , s , } \\ { \widehat { b } _ { i } - \widetilde { b } _ { i } = 0 , } & { \quad i = 1 , \ldots , s . } \end{array}
$$

The proof of this condition is very similar to the proof given in the previous section for Runge–Kutta methods, and is omitted.

As first shown by SUN [184], proper combination of Lobatto IIIA and Lobatto IIIB Runge–Kutta methods gives rise to symplectic PRK methods. It should be noted that neither of the two classes of RK methods are symplectic, in general, when considered individually! An example of symplectic PRK method, that is based on a Lobatto IIIA–IIIB pair, is the second-order generalized leapfrog scheme.

$$
\begin{array} { l } { { \displaystyle { \pmb { p } } ^ { n + 1 / 2 } = { \pmb { p } } ^ { n } - \frac { \Delta t } { 2 } \nabla _ { \pmb { q } } H ( { \pmb { p } } ^ { n + 1 / 2 } , { \pmb { q } } ^ { n } ) } , } \\ { { \displaystyle { \pmb { q } } ^ { n + 1 } = { \pmb { q } } ^ { n } + \frac { \Delta t } { 2 } \left[ \nabla _ { \pmb { p } } H ( { \pmb { p } } ^ { n + 1 / 2 } , { \pmb { q } } ^ { n } ) + \nabla _ { \pmb { p } } H ( { \pmb { p } } ^ { n + 1 / 2 } , { \pmb { q } } ^ { n + 1 } ) \right] } , } \\ { { \displaystyle { \pmb { p } } ^ { n + 1 } = { \pmb { p } } ^ { n + 1 / 2 } - \frac { \Delta t } { 2 } \nabla _ { \pmb { q } } H ( { \pmb { p } } ^ { n + 1 / 2 } , { \pmb { q } } ^ { n + 1 } ) } . } \end{array}
$$

Table 6.5 Coefficients for the threestage Lobatto IIIA–IIIB pair of order 4   

<table><tr><td>a=0 =1/2 =1</td><td>a11=0 21= 5/24 31=1/6</td><td>12=0 22=1/3 32=2/3</td><td>a13=0 a23=-1/24 33=1/6</td></tr><tr><td></td><td>b=1/6</td><td>b=2/3</td><td>b=1/6</td></tr><tr><td>=0</td><td>a1=1/6</td><td>a12 =-1/6</td><td>a13=0</td></tr><tr><td>=1/2</td><td>a21=1/6</td><td>a22 =1/3</td><td>&gt;</td></tr><tr><td></td><td></td><td></td><td>a23=0</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>=1</td><td>a31= 1/6</td><td>a32=5/6</td><td>a13=0</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>b=1/6</td><td>b=2/3</td><td>b=1/6</td></tr></table>

In fact, the generalized leapfrog method is the combination of the trapezoidal rule (Lobatto IIIA) for the $\pmb q$ variable with a variant of the midpoint rule (Lobatto IIIB) for the $\pmb { p }$ variable. The generalized leapfrog method is ideal for low-order integration of non-separable Hamiltonian problems and can be used as a basic method for higher-order symmetric compositions methods as described in Sections 6.2.2 and 6.2.3.

In Table 6.5, we give the coefficients for a three-stage fourth-order Lobatto IIIA–IIIB PRK method.

Higher-order symplectic PRK methods are implicit when applied to general Hamiltonian systems of type (6.1)–(6.2) and can be solved by a fixed-point iteration similar to the one discussed for implicit RK methods, or by Newton iteration.

The situation changes for systems with a separable Hamiltonian,

$$
H ( \pmb { q } , \pmb { p } ) = T ( \pmb { p } ) + V ( \pmb { q } ) .
$$

While symplectic $\mathsf { R K }$ methods are still necessarily implicit, explicit PRK methods can be found. However, this class of explicit PRK methods is equivalent to the class of composition methods and so we do not discuss them here in any further detail [148, 172].

We close this section with a proof of the fact that the symplecticness conditions (6.26)–(6.27) also imply exact preservation of any first integral of the form

$$
I = \pmb { q } ^ { T } \pmb { W } \pmb { p } + \pmb { d } _ { 1 } ^ { T } \pmb { q } + \pmb { d } _ { 2 } ^ { T } \pmb { p } ,
$$

$W \in \mathbb { R } ^ { d \times d }$ a constant matrix, $d _ { 1 } \in \mathbb { R } ^ { d }$ and $\pmb { d } _ { 2 } \in \mathbb { R } ^ { d }$ two vectors. Recall from Section 5.3 that first integrals of this type arise from the symmetry of $H$ under a linear canonical point transformation. For example, symplectic PRK methods exactly preserve total linear and angular momentum for systems with pairwise distance-dependent interactions.

Using the same tensor product notation and the abbreviations introduced in the previous section, a partitioned RK method (6.22)–(6.25) can be rewritten as

$$
\begin{array} { c } { q ^ { n + 1 } = { { \pmb q } ^ { n } } + \Delta t ( \widehat { { \pmb b } } ^ { T } \otimes { \pmb I } ) { \cal F } , } \\ { p ^ { n + 1 } = { { \pmb p } ^ { n } } + \Delta t ( \widetilde { { \pmb b } } ^ { T } \otimes { \pmb I } ) { \pmb G } , } \\ { { { \pmb Q } } = { \pmb e } \otimes { \pmb q } ^ { n } + \Delta t ( \widehat { { \pmb A } } \otimes { \pmb I } ) { \cal F } , } \\ { { { \pmb P } } = { \pmb e } \otimes { \pmb p } ^ { n } + \Delta t ( \widetilde { { \pmb A } } \otimes { \pmb I } ) { \pmb G } , } \end{array}
$$

where $\widehat { \pmb { A } } = \{ \widehat { a } _ { i j } \}$ , $\widetilde { A } = \big \{ \widetilde { a } _ { i j } \big \}$ , $\widehat { \pmb { b } } = \{ \widehat { b } _ { i } \}$ , and $\widetilde { \boldsymbol { b } } = \{ \widetilde { \boldsymbol { b } } _ { i } \}$ are the coefficient matrices, vectors respectively, of the PRK method. The conditions of symplecticness (6.26)–(6.27) are equivalent to

$$
\widehat { B } \widetilde { \pmb { A } } + \widehat { \pmb { A } } ^ { T } \widetilde { \pmb { B } } - \widehat { \pmb { b } } \widetilde { \pmb { b } } ^ { T } = \mathbf { 0 } , \qquad \widehat { \pmb { b } } = \widetilde { \pmb { b } } .
$$

In the sequel we will assume $\pmb { b } = \widehat { \pmb { b } } = \widetilde { \pmb { b } }$ and denote the associated diagonal $S \times S$ matrix by $B$ .

Let us assume that the given Hamiltonian ODE has a first integral of the from (6.31) with, for simplicity, $d _ { 1 } = d _ { 2 } = \mathbf { 0 }$ . We now check conservation of such first integrals under timestepping by symplectic PRK methods.

The first two equations (6.32)–(6.33) can be combined to yield

$$
\begin{array} { r l } & { \frac { ( \pmb { q } ^ { n + 1 } ) ^ { T } W p ^ { n + 1 } - ( \pmb { q } ^ { n } ) ^ { T } W p ^ { n } } { \Delta t } = ( \pmb { q } ^ { n } ) ^ { T } ( \pmb { b } ^ { T } \otimes \pmb { W } ) \pmb { G } + \pmb { F } ^ { T } ( \pmb { b } \otimes \pmb { W } ) p ^ { n } } \\ & { \qquad + \Delta t \pmb { F } ^ { T } ( \pmb { b } \pmb { b } ^ { T } \otimes \pmb { W } ) \pmb { G } . } \end{array}
$$

Similarly, equations (6.34)–(6.35) give rise to

$$
Q ^ { T } ( B \otimes W ) G = ( q ^ { n } ) ^ { T } ( b \otimes W ) G + \Delta t F ^ { T } ( \widehat { A } ^ { T } B \otimes W ) G ,
$$

and

$$
\boldsymbol { F } ^ { T } ( \boldsymbol { B } \otimes \boldsymbol { W } ) \boldsymbol { P } = \boldsymbol { F } ^ { T } ( \boldsymbol { b } \otimes \boldsymbol { W } ) \boldsymbol { p } ^ { n } + \Delta t \boldsymbol { F } ^ { T } ( \boldsymbol { B } \tilde { \boldsymbol { A } } \otimes \boldsymbol { W } ) \boldsymbol { G } .
$$

These formulas may be combined to yield

$$
\begin{array} { r l } & { \frac { ( \boldsymbol { q } ^ { n + 1 } ) ^ { T } \boldsymbol { W } p ^ { n + 1 } - ( \boldsymbol { q } ^ { n } ) ^ { T } \boldsymbol { W } p ^ { n } } { \Delta t } = \Delta t \boldsymbol { F } ^ { T } ( \left\{ b \boldsymbol { b } ^ { T } - B \boldsymbol { \tilde { A } } - \boldsymbol { \widehat { A } } ^ { T } \boldsymbol { B } \right\} \otimes \boldsymbol { W } ) \boldsymbol { G } } \\ & { \qquad + \boldsymbol { Q } ^ { T } ( \boldsymbol { B } \otimes \boldsymbol { W } ) \boldsymbol { G } + \boldsymbol { F } ^ { T } ( \boldsymbol { B } \otimes \boldsymbol { W } ) \boldsymbol { P } . } \end{array}
$$

Note that ${ d I } / { d t } = 0$ implies that

$$
\pmb { Q } ^ { T } ( \pmb { B } \otimes \pmb { W } ) \pmb { G } + \pmb { F } ^ { T } ( \pmb { B } \otimes \pmb { W } ) \pmb { P } = \pmb { 0 } .
$$

Hence symplectic PRK methods preserve first integrals arising from an invariance of the Hamiltonian $H$ under linear point transformations. The same statement is of course true for symplectic classical RK methods where $\widehat { \pmb { A } } = \widetilde { \pmb { A } }$ .

# 6.4 Generating functions

Composition methods offer a systematic way to the construction of symplectic maps; they rely on a splitting of the Hamiltonian into explicitly solvable Hamiltonian problems and the group property of symplectic maps under composition. In contrast, the symplectic RK methods appear more as a pure strike of good luck. However, symplectic $\mathsf { R K }$ methods and other available symplectic methods can be derived from a generating function [7, 73] that automatically guarantees the symplecticness of the associated method. We will give a brief summary of generating function methods in this section.

Generating functions are scalar valued functions $S$ that can be used to derive symplectic maps from $( \pmb q , \pmb p )$ to $( { \bar { q } } , { \bar { p } } )$ in a systematic manner. There exists several types of generating funtions. We focus here on the following two: (i) $S _ { 1 } ( q , \bar { p } )$ and (ii) $S _ { 2 } ( \pmb q , \bar { \pmb q } )$ . The associated symplectic map ${ \pmb { \psi } } : ( { \pmb q } , { \pmb p } )  ( { \pmb { \bar { q } } } , { \pmb { \bar { p } } } )$ is defined implicitly by either

$$
\pmb { p } = \nabla _ { \pmb { q } } S _ { 1 } ( \pmb { q } , \bar { \pmb { p } } ) , \quad \bar { \pmb { q } } = \nabla _ { \bar { \pmb { p } } } S _ { 1 } ( \pmb { q } , \bar { \pmb { p } } ) ,
$$

or

$$
\pmb { p } = - \nabla _ { \pmb { q } } S _ { 2 } ( \pmb { q } , \bar { \pmb { q } } ) , \quad \bar { \pmb { p } } = \nabla _ { \bar { \pmb { q } } } S _ { 2 } ( \pmb { q } , \bar { \pmb { q } } ) ,
$$

respectively. The symplecticness of $\pmb { \psi }$ is easily verified (see the Exercises).

Let us focus first on generating functions of type $S _ { 1 }$ . The identity map corresponds to $S _ { 1 } = \pmb { q } ^ { T } \bar { \pmb { p } }$ . One can now unfold the identity by going to a parameter dependent family of generating functions:

$$
S _ { 1 } ( \pmb q , \bar { p } ( \tau ) , \tau ) = \pmb q ^ { T } \bar { p } ( \tau ) + \tau \Delta S _ { 1 } ( \pmb q , \bar { p } ( \tau ) , \tau ) .
$$

According to (6.36), this yields an associated family of symplectic maps,

$$
\begin{array} { r } { \left[ \bar { \pmb q } ( \tau ) \right] = \pmb { \psi } _ { \tau } \left( \left[ \begin{array} { c } { \pmb q } \\ { \pmb { p } } \end{array} \right] \right) . } \end{array}
$$

A simple example of (6.38) is provided by

$$
S _ { 1 } ( \pmb q , \bar { p } ( \tau ) , \tau ) = \pmb q ^ { T } \bar { p } ( \tau ) + \tau H ( \pmb q , \bar { p } ( \tau ) ) ,
$$

and (6.36) results in

$$
p = \bar { p } ( \tau ) + \tau \nabla _ { q } H ( q , \bar { p } ( \tau ) ) , \quad \bar { q } ( \tau ) = q + \tau \nabla _ { \bar { p } } H ( q , \bar { p } ( \tau ) ) .
$$

If we set $\tau = \Delta t$ and identify $( \pmb q , \pmb p )$ with $\left( { \pmb q } ^ { n } , { \pmb p } ^ { n } \right)$ and $( { \bar { q } } , { \bar { p } } )$ with $( \pmb q ^ { n + 1 } , \pmb { p } ^ { n + 1 } )$ , respectively, the symplectic Euler-B method emerges.

Perhaps more importantly, a fundamental result in classical mechanics states that there is a generating function $S _ { 1 }$ of type (6.38) such that the associated

transformation $\pmb { \psi } _ { \tau }$ is equivalent to the exact flow map $\pmb { \phi } _ { \tau , H }$ of a canonical Hamiltonian system with Hamiltonian $H$ . The generating function $S _ { 1 }$ satisfies the Hamilton–Jacobi equation [7, 8]

$$
\partial _ { \tau } S _ { 1 } ( q , \bar { p } , \tau ) - H ( \nabla _ { \bar { p } } S _ { 1 } ( q , \bar { p } , \tau ) , \bar { p } ) = 0 .
$$

Hence one can try to obtain symplectic methods by approximately solving the Hamilton–Jacobi equation (6.39) near the identity transformation and to use the approximative $S _ { 1 }$ to define a symplectic integration method via (6.36). Indeed, this approach was followed by FENG [58] and CHANNEL AND SCOVEL [43, 44] and inspired early investigations of symplectic methods. Later it was shown by LASAGNI [106, 107] and SURIS [186] that symplectic (partitioned) Runge–Kutta methods can be derived from generating functions of both types $S _ { 1 }$ and $S _ { 2 }$ , respectively. These results are important since they guarantee the existence of globally defined modified Hamiltonian functions in backward error analysis [16, 80] (see the Exercises).

Generating functions of type $S _ { 2 }$ are also very useful because of their close connection to Largange’s equation (recall Section 3.2) and the Lagrangian variational principle [7, 73]. We illustrate the basic idea by a simple example. Take the Lagrangian function

$$
L ( q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { 2 } - V ( q )
$$

of a single degree-of-freedom particle system with mass equal to one and a potential energy function $V ( q )$ . One can replace the time derivative in $L$ by a discrete approximation and use this approximation as a generating function of type $S _ { 2 }$ , e.g.

$$
S _ { 2 } ( q , \bar { q } ; \tau ) = \tau L \left( q , \frac { \bar { q } - q } { \tau } \right) = \frac { \tau } { 2 } \left( \frac { \bar { q } - q } { \tau } \right) ^ { 2 } - \tau V ( q ) .
$$

The associated symplectic transformation is given by

$$
p = - \frac { \partial S _ { 2 } } { \partial q } = - \frac { q - \bar { q } } { \tau } + \tau V ^ { \prime } ( q ) , \qquad \bar { p } = \frac { \partial S _ { 2 } } { \partial \bar { q } } = \frac { \bar { q } - q } { \tau } .
$$

After sorting variables, we obtain the explicit expression

$$
\bar { p } = p - \tau V ^ { \prime } ( q ) , \qquad \bar { q } = q + \tau \bar { p } ,
$$

which turns again into the symplectic Euler-B method with $( q , p ) = ( q ^ { n } , p ^ { n } )$ , $( \bar { q } , \bar { p } ) = ( q ^ { n + 1 } , p ^ { n + 1 } )$ , and $\tau = \Delta t$ . See the survey article by MARSDEN AND WEST [125] for a detailed discussion of this particular generating function approach to symplectic integration and the closely related discrete variational principle. See also the Exercises.

# 6.5 Numerical experiments

# 6.5.1 Arenstorf orbits

Let us consider the gravitational system consisting of a couple of massive bodies and one light one moving in the $\left( x , y \right)$ -plane. We assume that the orbit of the two heavy bodies is essentially circular, and that the mass of the light body is so small that we can neglect the influence of the light body (for example, asteroid) on the motion of the two heavy ones. It is convenient to pass to a moving reference frame which rotates with the angular velocity of the planetary system around the center of mass of the two heavy bodies. We also choose units of length and time and mass so that the angular velocity of rotation, the sum of the masses of the heavy bodies, and the gravitational constant are all equal to one. The equations of motion for the light body are then given by

$$
\begin{array} { r } { \ddot { x } = + 2 \dot { y } - V _ { x } ( x , y ) , } \\ { \ddot { y } = - 2 \dot { x } - V _ { y } ( x , y ) , } \end{array}
$$

where the potential $V$ is given by

$$
V ( x , y ) = - \frac { x ^ { 2 } + y ^ { 2 } } { 2 } - \frac { \mu _ { 1 } } { r _ { 1 } } - \frac { \mu _ { 2 } } { r _ { 2 } } .
$$

Here $\mu _ { 1 }$ is the mass of the first (lighter) heavy body, $\mu _ { 2 } = 1 - \mu _ { 1 }$ is the mass of the second heavy body, and

$$
r _ { 1 } = \sqrt { ( x - \mu _ { 2 } ) ^ { 2 } + y ^ { 2 } } , \quad r _ { 2 } = \sqrt { ( x + \mu _ { 1 } ) ^ { 2 } + y ^ { 2 } }
$$

are the distances from the light body to the two heavy bodies which (in the moving coordinate frame) are fixed at points $( \mu _ { 2 } , 0 )$ and $\left( - \mu _ { 1 } , 0 \right)$ . This problem is also called the restricted three-body problem. See [8] for further details.

The restricted three-body problem possesses interesting periodic solutions often called Arenstorf orbits. For example, $\mu _ { 1 } = 0 . 0 1 2 2 7 7 4 7 1$ and initial data

$$
\begin{array} { l l } { { x = 0 . 9 9 4 , } } & { { \dot { x } = 0 , } } \\ { { y = 0 , } } & { { \dot { y } = - 2 . 0 0 1 5 8 5 1 0 6 3 7 9 0 8 2 } } \end{array}
$$

lead to a periodic orbit with period

$$
T = 1 7 . 0 6 5 2 1 6 5 6 0 1 5 7 9 6 2 5 5 .
$$

The numerical computation of this orbit faces difficulties because of the two singularities in $V$ at $\left( x , y \right) = \left( \mu _ { 2 } , 0 \right)$ and $( x , y ) = ( - \mu _ { 1 } , 0 )$ . Note that the periodic orbit gets very close to the first singularity at $t = k \cdot T$ , $k = 0 , \pm 1 , \pm 2 , . . .$ , which makes this a challenging problem for numerical computations. See Fig. 6.1 for a graphical presentation and [82] for the numerical computation of the Arenstorf orbit using “standard” numerical methods.

![](images/ad796c0908733923340888e3bdbddebca116f2c27ef69fc9ce45ca35e0a02cc8.jpg)  
Figure 6.1 Arenstorf orbit of the restricted three-body problem. The two (fixed) heavy bodies are marked by $^ *$ .

Let us discuss the Hamiltonian structure of the restricted three-body problem. In fact, the equations (6.40)–(6.41) can be brought into the form of the equations of motion for a particle in a magnetic field. We define $\pmb { q } = ( x , y , 0 ) ^ { T }$ and $p =$ $( \dot { x } , \dot { y } , 0 ) ^ { T }$ and obtain the Hamiltonian

$$
H = \frac { 1 } { 2 } | | \pmb { p } | | ^ { 2 } + V ( \pmb { q } ) , \quad V ( \pmb { q } ) = V ( x , y ) .
$$

The restricted three-body equations of motion are then equivalent to

$$
\begin{array} { l } { \displaystyle { \frac { d } { d t } \boldsymbol { q } = \boldsymbol { p } , } } \\ { \displaystyle { \frac { d } { d t } \boldsymbol { p } = \boldsymbol { b } \times \boldsymbol { p } - \nabla _ { \boldsymbol { q } } V ( \boldsymbol { q } ) , } } \end{array}
$$

with $\pmb { b } = ( 0 , 0 , - 2 ) ^ { T }$ . Both Scovel’s method from Section 4.5.2 and the implicit midpoint method can now be used to obtain symplectic integration methods.

We apply the higher-order composition methods from the previous subsections to the Arenstorf orbit of the restricted three-body problem. Scovel’s method is used as the basic second-order integrator, i.e.

$$
\psi _ { w \Delta t } = \pmb { \phi } _ { w \Delta t / 2 , V } \circ \pmb { \phi } _ { w \Delta t , T } \circ \pmb { \phi } _ { w \Delta t / 2 , V } .
$$

The equations of motion are integrated over one period $\tau$ and the error in the coordinates $( x ( t ) , y ( t ) )$ of the light body at $t = T$ , i.e.

$$
e ( T ) = \mathsf { m a x } ( x ( T ) - 0 . 9 9 4 , y ( T ) ) ,
$$

is recorded as a function of the necessary number of force evaluations per unit time interval. See Fig. 6.2 for a comparison of the various methods. We find that higher accuracy of a method pays off in terms of efficiency over a fixed time interval (here one period). In particular, both the sixth-order method of Table 6.1 and the eighth-order method of Table 6.2 work very well. We mention that this problem offers significant scope for adaptive integration. We will come back to this issue in Chapter 9.

![](images/d1ad4e9960638758ffa26f269852d7e86df39e15ffbea4911dc58d5f408f9a72.jpg)  
Figure 6.2 Accuracy versus efficiency comparison of fourth-order $( x )$ and sixth-order (o) composition methods of Table 6.1, the sixth-order 7-stages $( + )$ and 9-stages $( * )$ composition methods of Table 6.2, the sixth-order $( \boxed { \square } )$ post-processed method of Table 6.3, and the eighth-order $( \diamond )$ composition method of Table 6.2 using the Arenstorf orbit of the restricted three-body problem as a numerical test case.

# 6.5.2 Solar system

To compare the relative efficiencies of the different methods a model of the solar system was constructed as follows. The model used was based on ten bodies: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, and the

Sun with the entire system rotating around its center of gravity, and uses an all-body potential. The integrator ignores all but gravitational forces.

The Hamiltonian equation, where $m _ { j }$ is the mass of the i th planet and $G$ is the gravitational constant is

$$
H ( q , p ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { 1 0 } \frac { | | p _ { i } | | ^ { 2 } } { m _ { i } } - \sum _ { i = 1 } ^ { 9 } \sum _ { j = i + 1 } ^ { 1 0 } \frac { G m _ { i } m _ { j } } { | | q _ { i } - q _ { j } | | } .
$$

Then the differential equations are

$$
\dot { q } _ { i } = \frac { p _ { i } } { m _ { i } } , \dot { p } _ { i } = \sum _ { j = 1 , j \neq i } ^ { 1 0 } \frac { G m _ { i } m _ { j } ( q _ { i } - q _ { j } ) } { | | q _ { i } - q _ { j } | | ^ { 3 } } , i = 1 , 2 , \ldots , N .
$$

This model treats the Sun as one of the bodies and the entire system orbits around the centre of mass of the system. Initial data were taken from the DE118 18-digit state vectors provided by the NASA Jet Propulsion Laboratory, and represents the state of the Solar System at Julian date 2440400.50 (00:00 on June 28, 1969).

All of the composition and post-processing schemes were based on the secondorder St¨ormer–Verlet method. The methods compared were as follows:

<table><tr><td rowspan=1 colspan=1>label</td><td rowspan=1 colspan=1>order</td><td rowspan=1 colspan=1>method type</td><td rowspan=1 colspan=1>table</td><td rowspan=1 colspan=1>entry</td></tr><tr><td rowspan=1 colspan=1>2nd4thM</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>VerletComposition</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>4thRK</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Runge-Kutta</td><td rowspan=1 colspan=1>6.4</td><td rowspan=4 colspan=1>1312</td></tr><tr><td rowspan=1 colspan=1>6thM</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Composition</td><td rowspan=1 colspan=1>6.2</td></tr><tr><td rowspan=1 colspan=1>6thPP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Post-processing</td><td rowspan=1 colspan=1>6.3</td></tr><tr><td rowspan=1 colspan=1>6thRK</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Runge-Kutta</td><td rowspan=1 colspan=1>6.4</td></tr><tr><td rowspan=1 colspan=1>6thY</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Composition</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>8thM</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>Composition</td><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>4</td></tr></table>

The methods have been compared by plotting the maximum energy error over a ten year simulation against the number of force evaluations done, as shown in Fig. 6.3. From the graph it is clear that the high-order explicit methods dominate for small maximum errors, with the post-processing and eighth-order methods providing the greatest efficiency. The implicit Runge–Kutta methods fare less well in the comparison.

In this model each step of the Runge–Kutta method was resolved to a fixed arbitrary value which was small enough so that there was no influence on the maximum energy error. This approach gives rise to the odd curves in the work– energy diagrams at large stepsize, as, at the large stepsizes corresponding to the larger maximum energy error, the simplified nonlinear solver becomes inefficient and increasing numbers of iterations are needed to resolve the solution to the specified accuracy.

![](images/3ec93c707b15d92cf396b9fc0189b7f34621c4f52ad16c98bc4232983a171204.jpg)  
Figure 6.3 Comparison of method efficiency for the solar system model.

Longer simulations demonstrate the procession in Pluto’s orbit; this can be seen in Fig. 6.4 which represents the trajectories in the Solar System over one million years.

# 6.6 Exercises

1. Numerical comparison for Arenstorf orbit. Implement Scovel’s second-order splitting method (compare Section 4.5.2) for the restricted three-body problem of Section 6.5.1. Using Scovel’s method, also implement the higher-order composition methods as described in Sections 6.2.2–6.2.3. Reproduce the data shown in Fig. 6.2. Note that the work per unit time interval is defined as the number of timesteps taken to approximate the solution over one period

![](images/8ffe76795894a83dbae2d3810ae8390a8df4d6c5ddbef0e251cc0bf75f6964e5.jpg)  
Figure 6.4 One million year simulation of the solar system. The cloud of points illustrates the precession in the orbit of Pluto.

$T$ multiplied by the number of stages of the method and divided by the period $T$ . The accuracy is defined in terms of the absolute error in the computed positions after one period, i.e.

$$
e ( T ) = \mathsf { m a x } ( x ( T ) - 0 . 9 9 4 , y ( T ) ) .
$$

2. Higher-order composition methods. Let $\psi _ { \Delta t }$ be a symmetric and symplectic method of order two (for example the St¨ormer–Verlet method). Show that the composed method

$$
\hat { \pmb { { \psi } } } _ { \Delta t } = { \pmb { { \psi } } } _ { w _ { 1 } \Delta t } \circ { \pmb { { \psi } } } _ { w _ { 2 } \Delta t } \circ { \pmb { { \psi } } } _ { w _ { 1 } \Delta t }
$$

is fourth order if

$$
2 w _ { 1 } + w _ { 2 } = 1 , \qquad 2 w _ { 1 } ^ { 3 } + w _ { 2 } ^ { 3 } = 0 .
$$

Hint: Since $\psi _ { \Delta t }$ is symplectic, there exists a modified Hamiltonian $\tilde { H } ( \Delta t )$ whose corresponding time- $\Delta t$ -flow map is “identical” to $\psi _ { \Delta t }$ (see Chapter 5). Because $\psi _ { \Delta t }$ is also symmetric, the Taylor expansion of $\tilde { H } ( \Delta t )$ contains only terms of even order in $\Delta t$ (see Exercises in Chapter 5). Use the Taylor series expansion

$$
\tilde { H } ( \Delta t ) = H + \Delta t ^ { 2 } \delta H _ { 2 } + \Delta t ^ { 4 } \delta H _ { 4 } + . . .
$$

to derive a modified Hamiltonian for the (symplectic and symmetric) maps ${ \pmb { \psi } } _ { w _ { i } \Delta t }$ . Finally, use the BCH formula of Section 5.4 to derive the modified Hamiltonian for the method $\hat { \pmb { { \psi } } } _ { \Delta t }$ . Show that $2 w _ { 1 } + w _ { 2 } = 1$ implies second order. If also $2 w _ { 1 } ^ { 3 } + w _ { 2 } ^ { 3 } = 0$ , then the method is fourth order.

3. Symplectic methods from generating functions. Show that a map ${ \pmb { \psi } } : ( { \pmb { q } } , { \pmb { p } } ) $ $( { \bar { q } } , { \bar { p } } )$ defined by either (6.36) or (6.37) is symplectic. Find a generating function that yields the symplectic Euler-A method.

4. Hamilton–Jacobi equation. Given a generating function (6.38) that satisfies the Hamilton–Jacobi equation (6.39), show that the associated symplectic map (6.36) is equivalent to the flow map $\pmb { \phi } _ { \tau , H }$ . Hint: Differentiate

$$
\pmb { p } = \nabla _ { \pmb { q } } S _ { 1 } ( \pmb { q } , \bar { \pmb { p } } ( \tau ) , \tau ) ,
$$

with respect to $\tau$ and compare with the gradient of (6.39) with respect to $\pmb q$ . Repeat the same calculation for

$$
\bar { \pmb q } ( \tau ) = \nabla _ { \bar { \pmb { p } } } S _ { 1 } ( \pmb q , \bar { \pmb { p } } ( \tau ) , \tau ) .
$$

Also note that

$$
\begin{array} { r } { \left[ \bar { \pmb q } ( \tau ) \right] = \pmb { \phi } _ { \tau , H } \left( \left[ \begin{array} { c } { \pmb q } \\ { \pmb { p } } \end{array} \right] \right) } \end{array}
$$

is equivalent to

$$
\frac { d } { d \tau } \bar { p } = - \nabla _ { \bar { q } } H ( \bar { q } , \bar { p } ) , \qquad \frac { d } { d \tau } \bar { q } = \nabla _ { \bar { p } } H ( \bar { q } , \bar { p } ) .
$$

5. Symplectic methods from generating functions. Given a Lagrangian functions $L ( \pmb q , \dot { \pmb q } ) = \| \dot { \pmb q } \| ^ { 2 } / 2 - V ( \pmb q )$ . What symplectic method do you obtain from the generating function

$$
S ( q , \bar { q } , \tau ) = \tau L \left( \frac { q + \bar { q } } { 2 } , \frac { \bar { q } - q } { \tau } \right) = \frac { \tau } { 2 } | | \frac { \bar { q } - q } { \tau } | | ^ { 2 } - \tau V \left( \frac { \bar { q } + q } { 2 } \right) \bar { \tau }
$$

One can clearly apply this approach to more general Lagrangian functions $L \left( \pmb { q } , \dot { \pmb { q } } \right)$ . Take, for example, the Lagrangian function (3.17) given in Section 3.2 to describe the motion of a charged particle in a magnetic field. Discuss several options to obtain a generating function and compare the associated numerical methods with the ones used in Section 4.5.2.

6. Modified Hamiltonian functions via generating functions. Let $S _ { H }$ denote the generating function of type (6.38) for the exact flow map $\pmb { \phi } _ { \tau , H }$ . Show that

$$
S _ { H } ( q , \bar { p } , \tau ) = q ^ { T } \bar { p } + \tau H ( q , \bar { p } ) + \frac { \tau ^ { 2 } } { 2 } \nabla _ { q } H ( q , \bar { p } ) ^ { T } \nabla _ { \bar { p } } H ( q , \bar { p } ) + \mathcal { O } ( \tau ^ { 3 } ) ,
$$

via explicit Taylor expansion of (6.39) for $S _ { 1 } = S _ { H }$

The symplectic Euler-B method $\psi _ { \Delta t }$ can be obtained from the generating function

$$
\begin{array} { r } { S ( \pmb { q } , \bar { \pmb { p } } , \Delta t ) = \pmb { q } ^ { T } \bar { \pmb { p } } + \Delta t H ( \pmb { q } , \bar { \pmb { p } } ) . } \end{array}
$$

Show that the first-order modified Hamiltonian is given by

$$
\tilde { H } _ { 1 } = H + \Delta t \delta H _ { 1 } ,
$$

with

$$
\delta \tilde { H } _ { 1 } ( q , p ) = \operatorname* { l i m } _ { \tau  0 } \frac { S ( q , p , \tau ) - S _ { H } ( q , p , \tau ) } { \tau ^ { 2 } } .
$$

Can this approach be generalized to higher-order corrections? See also [80].

7. Discrete variational mechanics. Consider the Lagrangian function $L \left( q , \dot { q } \right)$ and the action integral

$$
L [ q ] = \int _ { t _ { 0 } } ^ { t _ { 1 } } L ( q ( t ) , \dot { q } ( t ) ) d t .
$$

We replace the integral by a finite sum

$$
L [ \{ q ^ { n } \} ] = \sum _ { n } L \left( q ^ { n } , \frac { q ^ { n + 1 } - q ^ { n } } { \Delta t } \right) \Delta t
$$

and find the local minimizer from the condition

$$
\frac { \partial } { \partial q ^ { n } } L [ \{ q ^ { n } \} ] = 0 .
$$

What numerical scheme do you obtain by explicitly evaluating the formula for $L ( q , \dot { q } ) = \dot { q } ^ { 2 } / 2 - V ( q ) ?$ The derivation is a simple example of the discrete variational principle [125].

# 7

# Constrained mechanical systems

In this chapter, we discuss the problem of simulating a mechanical system subject to one or several constraints. This subject is rather broad, and there are many theoretical issues which arise in the most general settings concerning the formulation of the equations of motion and the properties of solutions. To simplify the discussion, we primarily restrict ourselves to the treatment of constraints which can be described by algebraic relations among the position variables of the system, i.e., defined by equations of the form

$$
g _ { i } ( \pmb q ) = 0 , \qquad i = 1 , \ldots , m ,
$$

for smooth functions $g _ { j }$ . A mechanical system subject to such constraints is typically termed holonomic. Derivation of equations of motion for a holonomically constrained mechanical system is not very much more complicated than for an unconstrained system.

When it comes to numerical discretization, however, the constraints introduce a few challenges. For one thing, the propagation of errors in numerical algorithms for a constrained differential equation is more complicated than for ordinary differential equations. For another, the constraints are often an intrinsic component of the modeling of the system, and the configuration manifold (the set of points for which the constraints are satisfied) is an essential part of the extension of the concept of symplecticness. For these reasons, it seems important that the constraints are accurately resolved at each step. This is in contrast to the case for unconstrained systems, where a certain error growth must generally be tolerated.

In this chapter, we will introduce several approaches for numerical discretization of holonomically constrained systems, focusing initially on the SHAKE method due to RYCKAERT, CICCOTTI, AND BERENDSEN [167] and RATTLE [5] variant, as these have proven very popular in molecular dynamics. We then develop more general type of methods. Recently, schemes like those discussed in this chapter have seen widespread use in computer graphics and gaming applications.

# 7.1 N-body systems with holonomic constraints

In the introduction of this book, we have already encountered simple examples of constrained Hamiltonian systems (the bead on a wire, the spherical pendulum). It was shown that D’Alembert’s principle enabled us to write equations of motion with respect to a single constraint $g ( \pmb q ) = 0$ by introducing a constraint force that always acts in the direction of the normal to the constraint surface.

The extension of the Newtonian formulation to systems with multiple particles and multiple holonomic constraints is straightforward. Given m algebraic constraints $g _ { i } ( \pmb q ) = 0$ , $i = 1 , \dots , m$ , on a multiparticle system, it can be shown that the constraint forces due to each constraint act in the normal direction to the corresponding surface. Newton’s Second Law then suggests the following form for the equations of motion:

$$
\begin{array} { c } { { \displaystyle \overline { { \frac { d } { d t } } } q = v , } } \\ { { { \cal M } \displaystyle \frac { d } { d t } v = - \nabla _ { q } V ( q ) - \sum _ { i = 1 } ^ { m } \nabla _ { q } g _ { i } ( q ) \lambda _ { i } , } } \\ { { 0 = g _ { i } ( q ) , \qquad i = 1 , 2 , \ldots , m . } } \end{array}
$$

Here, as in previous chapters, $M$ represents a positive definite and symmetric (typically diagonal) mass matrix. We typically impose the assumption that the gradients of the constraint functions $\nabla _ { q } g _ { i } ( q )$ form a linearly independent set.

We define the configuration manifold $\mathcal { M }$ as the space of all positions subject to the position constraints:

$$
\mathcal { M } = \{ \pmb q \in \mathbb { R } ^ { d } | \ g _ { i } ( \pmb q ) = 0 , i = 1 , \ldots , m \} .
$$

Let $\bar { \pmb q }$ be a point of the configuration manifold and consider the set of all smooth parameterized curves containing $\bar { \pmb q }$ and lying in ${ \mathcal { M } } .$ . Each such parameterized curve $\pmb q ( t )$ (with, say, $\pmb q ( t _ { 0 } ) = \bar { \pmb q } ,$ ) has a certain velocity vector $\bar { \pmb v }$ at $t = t _ { 0 }$ , $\bar { \pmb v } = \dot { \pmb q } ( t _ { 0 } )$ . Obviously, because of $g _ { i } ( \pmb { q } ( t ) ) = 0$ for all $t$ , we must have that

$$
\cfrac { d } { d t } g _ { i } ( \pmb { q } ( t ) ) = \nabla _ { \pmb { q } } g _ { i } ( \pmb { q } ( t ) ) \cdot \pmb { \dot { q } } ( t ) = \nabla _ { \pmb { q } } g _ { i } ( \pmb { q } ( t ) ) \cdot \pmb { v } ( t ) = 0 ,
$$

and, in particular

$$
\nabla _ { q } g _ { i } ( \bar { q } ) \cdot \bar { \pmb { v } } = 0 .
$$

The set of all possible velocity vectors at the point $\bar { \pmb q }$ is a linear vector space

$$
T _ { \bar { q } } \mathcal { M } = \{ \bar { \pmb { v } } \in \mathbb { R } ^ { d } | ( \nabla _ { \pmb { q } } g _ { i } ( \bar { \pmb { q } } ) ) \cdot \bar { \pmb { v } } = 0 , i = 1 , \ldots , m \} ,
$$

![](images/a116e79f767c4a385758915335bea876f299eeb2bb19426c001eabc4ef47d440.jpg)  
Figure 7.1 The tangent space.

called the tangent space at $\bar { \pmb q }$ (Fig. 7.1). The tangent bundle of $\mathcal { M }$ is the space of all pairs $( \pmb q , \pmb v )$ with $\pmb q$ lying in $\mathcal { M }$ and $\pmb { v }$ lying in $T _ { q } \mathcal { M } .$ . The tangent bundle is denoted $T \mathcal { M }$ .

The system (7.1)–(7.3) can be written more compactly by introducing the vector function $g ( \pmb q ) = ( g _ { 1 } ( \pmb q ) , \dots , g _ { m } ( \pmb q ) ) ^ { T }$ , denoting its Jacobian matrix by

$$
\pmb { G } ( \pmb { q } ) = g _ { \pmb { q } } ( \pmb { q } ) , \quad \mathrm { o r , ~ e q u i v a l e n t l y , } \quad \pmb { G } ( \pmb { q } ) ^ { T } = \nabla _ { \pmb { q } } \pmb { g } ( \pmb { q } ) ,
$$

and letting $\pmb { \lambda }$ represent the $m$ -vector of multipliers $\pmb { \lambda } = ( \lambda _ { 1 } , \ldots , \lambda _ { m } ) ^ { T }$ . Then the equations of motion become

$$
\begin{array} { c } { \displaystyle \frac { d } { d t } \pmb { q } = \pmb { v } , } \\ { \displaystyle M \frac { d } { d t } \pmb { v } = - \nabla _ { \pmb { q } } V ( \pmb { q } ) - \pmb { G } ( \pmb { q } ) ^ { T } \pmb { \lambda } , } \\ { \displaystyle \pmb { 0 } = \pmb { g } ( \pmb { q } ) . } \end{array}
$$

![](images/1a0d6655a83fc9a004af3f5a583ae218b3a054d7e44b602b67c2e823a91c764a.jpg)

Example 1 Considera simple constraint chain in the plane made up of $N .$ -point particles with masses $m _ { 1 } , m _ { 2 } , \dots , m _ { N }$ , with each successive pair of particles joined by a length constraint, say with lengths $I _ { 1 } , I _ { 2 } , \ldots , I _ { N - 1 }$ . If, moreover, the first point is linked to the origin by a similar length constraint (say with length $I _ { 0 }$ ), then we have a multiple pendulum (see diagram). These problems are important model problems used in biochemistry and biophysics (polymers exhibit such a chain structure) as well as in engineering.

We might assume that the system moves in some applied uniform potential energy field $V = \textstyle \sum _ { i = 1 } ^ { N } \phi ( \pmb { q } _ { i } )$ , so that the external force acting on the i th particle is

$$
\pmb { F } _ { i } = - \nabla _ { \pmb { q } _ { i } } \phi ( \pmb { q } _ { i } ) .
$$

Let us number the multipliers in accordance with the indexing of the constraints, then following the discussion of this section, the equations of motion are, for any of the internal nodes of the chain

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } { \pmb q } _ { i } = { \pmb v } _ { i } , } \\ { \displaystyle m _ { i } \frac { d } { d t } { \pmb v } _ { i } = { \pmb F } _ { i } - \lambda _ { i - 1 } ( { \pmb q } _ { i } - { \pmb q } _ { i - 1 } ) - \lambda _ { i } ( { \pmb q } _ { i } - { \pmb q } _ { i + 1 } ) , } \end{array}
$$

whereas the first node obeys

$$
\begin{array} { c } { { \displaystyle \frac { d } { d t } { \pmb q } _ { 1 } = { \pmb v } _ { 1 } , } } \\ { { \displaystyle m _ { 1 } \frac { d } { d t } { \pmb v } _ { 1 } = { \pmb F } _ { 1 } - \lambda _ { 0 } { \pmb q } _ { 1 } - \lambda _ { 1 } ( { \pmb q } _ { 1 } - { \pmb q } _ { 2 } ) , } } \end{array}
$$

and the last node moves according to

$$
\begin{array} { c } { { \displaystyle \frac { d } { d t } { \pmb q } _ { N } = { \pmb v } _ { N } , } } \\ { { m _ { N } \displaystyle \frac { d } { d t } { \pmb v } _ { N } = { \pmb F } _ { N } - \lambda _ { N - 1 } ( { \pmb q } _ { N } - { \pmb q } _ { N - 1 } ) . } } \end{array}
$$

Here the constraints take the form

$$
g _ { i } ( { \pmb q } ) = \frac { 1 } { 2 } ( \| { \pmb q } _ { i } - { \pmb q } _ { i + 1 } \| ^ { 2 } - I _ { i } ^ { 2 } ) = 0 ,
$$

for $i = 1 , \dots , N - 1$ , while $\begin{array} { r } { g _ { 0 } ( \pmb q ) = \frac { 1 } { 2 } ( \| \pmb q _ { 1 } \| ^ { 2 } - I _ { 0 } ^ { 2 } ) = 0 } \end{array}$ . The transpose of the constraint Jacobian matrix, $G ( \pmb q ) ^ { T }$ , here is

$$
\left[ \begin{array} { c c c c c c c } { q _ { 1 } } & { q _ { 1 } - q _ { 2 } } & { { \bf 0 } } & { . . . } & { { \bf 0 } } & { { \bf 0 } } & { { \bf 0 } } \\ { { \bf 0 } } & { q _ { 2 } - q _ { 1 } } & { q _ { 2 } - q _ { 3 } } & { . . . } & { { \bf 0 } } & { { \bf 0 } } & { { \bf 0 } } \\ { { \bf 0 } } & { { \bf 0 } } & { q _ { 3 } - q _ { 2 } } & { . . . } & { { \bf 0 } } & { { \bf 0 } } & { { \bf 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { { \bf 0 } } & { { \bf 0 } } & { { \bf 0 } } & { . . . } & { { \bf 0 } } & { q _ { N - 1 } - q _ { N - 2 } } & { q _ { N - 1 } - q _ { N } } \\ { { \bf 0 } } & { { \bf 0 } } & { { \bf 0 } } & { . . . } & { { \bf 0 } } & { { \bf 0 } } & { q _ { N } - q _ { N - 1 } } \end{array} \right] .
$$

Just as for the one-particle, one-constraint case, the multipliers $\lambda _ { j }$ in the constrained Newton equations (7.6)–(7.8) could be eliminated by differentiating the velocity constraints (7.4) one more time with respect to $t$ , resulting, after an exercise in calculus, in a system of unconstrained differential equations

$$
\begin{array} { c } { \displaystyle \frac { d } { d t } \pmb { q } = \pmb { v } , } \\ { \displaystyle M \frac { d } { d t } \pmb { v } = - \nabla _ { \pmb { q } } V \big ( \pmb { q } ) - G ( \pmb { q } ) ^ { T } \pmb { \Lambda } ( \pmb { q } , \pmb { v } ) , } \end{array}
$$

with $\pmb { \Lambda } ( \pmb q , \pmb { v } )$ given by

$$
\begin{array} { r } { \Lambda ( \boldsymbol { q } , \boldsymbol { v } ) = - ( G M ^ { - 1 } G ^ { T } ) ^ { - 1 } [ G M ^ { - 1 } \nabla _ { \boldsymbol { q } } V ( \boldsymbol { q } ) + g _ { \boldsymbol { q } \boldsymbol { q } } < \boldsymbol { v } , \boldsymbol { v } > ] . } \end{array}
$$

Here we have used the shorthand $G = G ( q )$ and the symbol $g _ { q q } < v$ , $v >$ is to be understood to represent a vector of $m$ components with the ith component given by

$$
( g _ { i } ) _ { q q } < v , v > = \sum _ { k , I = 1 } ^ { d } \frac { \partial ^ { 2 } g _ { i } } { \partial q _ { k } \partial q _ { I } } v _ { k } v _ { I } .
$$

These equations are well defined provided the square $m \times m$ matrix $G M ^ { - 1 } G ^ { T }$ is nonsingular along the configuration manifold ${ \mathcal { M } } ,$ i.e., when $\pmb { g } ( \pmb { q } ) = \pmb { 0 }$ . Note that this is always the case if the matrix $G ( q )$ has full rank for $\pmb q \in \mathcal { M }$ (has linearly independent rows) and $M$ is positive definite (see Exercises). For prescribed initial conditions $( \pmb q _ { 0 } , \pmb v _ { 0 } ) \in \top \mathcal { M } ,$ , the associated solution $( \pmb q ( t ) , \pmb v ( t ) )$ of (7.9)–(7.11) stays in $T \mathcal { M }$ and, hence, such a solution $( \pmb q ( t ) , \pmb v ( t ) )$ also satisfies (7.6)–(7.8). For that reason, one often refers to the system of differential and algebraic equations (7.6)–(7.8) as a description of an ordinary differential equation (ODE) on a manifold (here $\tau { \mathcal { M } } )$ and (7.9)–(7.11) is called the underlying ODE.

# 7.2 Numerical methods for constraints

We now consider the development of numerical integration methods suitable for integrating a constrained mechanical system. The obvious geometric property that we would like to preserve is the constraint $\pmb { g } ( \pmb { q } ) = \pmb { 0 }$ . However, any such trajectory will also need to satisfy the tangency condition (7.5), thus we seek methods for solving (7.1)–(7.3) which preserve the tangent bundle $T \mathcal { M }$

There are many approaches to this problem. We have already seen in previous chapters that the use of different formulations of the equations can have a profound impact on the numerical integration process. Roughly speaking, methods for constrained integration can be divided into two classes: (i) methods based on integration of some related (unconstrained) ordinary differential equation, e.g., the underlying ODE (7.9)–(7.11), and (ii) methods based on direct discretization of the constrained equations of motion (7.1)–(7.3). In this section, we consider methods of the second class. Schemes of the other type are mentioned at the end of this chapter.

# 7.2.1 Direct discretization: SHAKE and RATTLE

Experience indicates that the best results can generally be obtained using a direct discretization of the equations of motion. The idea in direct discretization is to apply the ideas used to in constructing approximation methods for unconstrained differential equations to the constrained equations of motion. This requires some generalization of the standard types of methods. In this section, we will introduce popular methods which generalize the St¨ormer–Verlet method introduced in Chapter 2, and we comment on issues such as accuracy and stability. The results of this subsection will be generalized to more general constrained Hamiltonian systems in the next section.

SHAKE discretization was proposed in 1976 by RYCKAERT, CICCOTTI, AND BERENDSEN [167]. A paper of ANDERSEN [5] later introduced a related formulation, which he called RATTLE. LEIMKUHLER AND SKEEL [113] analyzed and compared the two methods, discovering, apparently for the first time, that they were (i) equivalent to each other and (ii) symplectic. Our treatment is based on the exposition of [113].

Upon rewriting (7.6)–(7.7) as a single second-order equation in $\pmb q$ and applying the standard leapfrog discretization (2.19) of Section 2.5, one quite naturally arrives at the SHAKE discretization

$$
\begin{array} { c } { M \frac { { \pmb q } ^ { n + 1 } - 2 { \pmb q } ^ { n } + { \pmb q } ^ { n - 1 } } { \Delta t ^ { 2 } } = - \nabla _ { \pmb { q } } V ( { \pmb q } ^ { n } ) - { \pmb G } ( { \pmb q } ^ { n } ) ^ { T } { \pmb \lambda } ^ { n } , } \\ { { \pmb 0 } = { \pmb g } ( { \pmb q } ^ { n + 1 } ) . } \end{array}
$$

The method can be implemented as follows. We solve (7.12) for $\pmb q ^ { n + 1 }$ and insert in (7.13), resulting in a system of $m$ equations in the $m$ unknown Lagrange multipliers $\pmb { \lambda } ^ { n } = \{ \lambda _ { i } ^ { n } \}$

$$
{ \bf 0 } = \tilde { { \pmb g } } ( { \pmb \lambda } ^ { n } ) : = { \pmb g } ( \bar { { \pmb q } } ^ { n + 1 } - \Delta t ^ { 2 } { \pmb M } ^ { - 1 } { \pmb G } ( { \pmb q } ^ { n } ) ^ { T } { \pmb \lambda } ^ { n } ) ,
$$

where

$$
\bar { \pmb q } ^ { n + 1 } : = 2 \pmb q ^ { n } - \pmb q ^ { n - 1 } - \Delta t ^ { 2 } \pmb M ^ { - 1 } \nabla _ { \pmb q } V ( \pmb q ^ { n } )
$$

represents an unconstrained step with the leapfrog method. Some possibilities for the treatment of these nonlinear equations will be discussed later in this section.

The equations (7.12)–(7.13) can be recast in a position-velocity formulation by setting ${ \pmb v } ^ { n + 1 / 2 } = ( { \pmb q } ^ { n + 1 } - { \pmb q } ^ { n } ) / \Delta t$ and defining $\pmb { v } ^ { n } = \frac { 1 } { 2 } \big ( \pmb { v } ^ { n - 1 / 2 } + \pmb { v } ^ { n + 1 / 2 } \big )$ , resulting in:

# SHAKE IN POSITION-VELOCITY FORM

$$
\begin{array} { c } { q ^ { n + 1 } = q ^ { n } + \Delta t { \boldsymbol v } ^ { n + 1 / 2 } , } \\ { { \displaystyle M { \boldsymbol v } ^ { n + 1 / 2 } = M { \boldsymbol v } ^ { n - 1 / 2 } - \Delta t \nabla _ { q } V ( q ^ { n } ) - \Delta t \boldsymbol G ( q ^ { n } ) ^ { T } } \boldsymbol \lambda ^ { n } , } \\ { { \displaystyle \mathbf 0 = g ( { \bf q } ^ { n + 1 } ) } , } \\ { { \displaystyle v ^ { n } = \frac 1 2 \left( { \boldsymbol v } ^ { n + 1 / 2 } + { \boldsymbol v } ^ { n - 1 / 2 } \right) . } } \end{array}
$$

SHAKE can be viewed as a mapping of ${ \mathcal { M } } ,$ , but it does not define a mapping of the tangent bundle $T \mathcal { M } .$ Yet, SHAKE is algebraically equivalent to another method, RATTLE, which is a mapping of the tangent bundle $T \mathcal { M } .$ The idea behind RATTLE is to correct the SHAKE solution so that it lies on $\tau { \mathcal { M } }$ through appropriate projection of the velocity $\pmb { v } ^ { n + 1 }$ on to the tangency constraint (7.5), the result being the scheme:

# RATTLE DISCRETIZATION

$$
\begin{array} { c } { { q ^ { n + 1 } = q ^ { n } + \Delta t v ^ { n + 1 / 2 } , } } \\ { { { \displaystyle M v ^ { n + 1 / 2 } = M v ^ { n } - \frac { \Delta t } { 2 } \nabla _ { q } V ( q ^ { n } ) - \frac { \Delta t } { 2 } G ( q ^ { n } ) ^ { T } \lambda _ { ( \mathrm { r } ) } ^ { n } , } } } \\ { { 0 = g ( q ^ { n + 1 } ) , } } \\ { { { \displaystyle M v ^ { n + 1 } = M v ^ { n + 1 / 2 } - \frac { \Delta t } { 2 } \nabla _ { q } V ( q ^ { n + 1 } ) - \frac { \Delta t } { 2 } G ( q ^ { n + 1 } ) ^ { T } \lambda _ { ( \mathrm { v } ) } ^ { n + 1 } , } } } \\ { { 0 = G ( q ^ { n + 1 } ) v ^ { n + 1 } . } } \end{array}
$$

The multipliers $\lambda _ { ( \mathsf { r } ) } ^ { n }$ are chosen in order to enforce the position constraints (7.20), while λn+1 relates to the velocity constraints (7.22) and is determined at time level $t _ { n }$ by the linear system

$$
\left[ G ( q ^ { n } ) M ^ { - 1 } G ( q ^ { n } ) ^ { T } \right] \lambda _ { ( \mathrm { v } ) } ^ { n } = G ( q ^ { n } ) \left( \frac { 2 } { \Delta t } { v } ^ { n - 1 / 2 } - M ^ { - 1 } \nabla _ { q } V ( q ^ { n } ) \right) .
$$

Combining equations (7.19) and

$$
M v ^ { n } = M v ^ { n - 1 / 2 } - \frac { \Delta t } { 2 } \nabla _ { q } V ( q ^ { n } ) - \frac { \Delta t } { 2 } G ( q ^ { n } ) ^ { T } \lambda _ { \mathrm { ( v ) } } ^ { n }
$$

results in

$$
M \pmb { v } ^ { n + 1 / 2 } = \pmb { M } \pmb { v } ^ { n - 1 / 2 } - \Delta t \nabla _ { \pmb { q } } V ( \pmb { q } ^ { n } ) - \frac { \Delta t } { 2 } \pmb { G } ( \pmb { q } ^ { n } ) ^ { T } ( \pmb { \lambda } _ { ( r ) } ^ { n } + \pmb { \lambda } _ { ( \vee ) } ^ { n } ) ,
$$

where $\lambda _ { ( \vee ) } ^ { n }$ is determined by (7.23) and is assumed to be computed at this stage. On the other hand, $\lambda _ { ( \mathsf { r } ) } ^ { n }$ is chosen so that

$$
g ( q ^ { n + 1 } ) = { \pmb g } ( { \pmb q } ^ { n } + \Delta t { \pmb v } ^ { n + 1 / 2 } ) = { \pmb 0 }
$$

at the next time level.

We recognize that (7.24) is equivalent to the SHAKE update (7.15) with $\pmb { \lambda } ^ { n }$ replaced by $\textstyle { \frac { 1 } { 2 } } ( \lambda _ { ( \mathfrak { r } ) } ^ { \eta } + \lambda _ { ( \mathfrak { v } ) } ^ { \eta } )$ . Thus RATTLE and SHAKE are formally equivalent when viewed as iterations from $\left( q ^ { n } , v ^ { n - \frac { 1 } { 2 } } \right)$ to $( q ^ { n + 1 } , v ^ { n + \frac { 1 } { 2 } } )$ . In other words, a proper initialization of RATTLE would produce a sequence of approximations identical to that produced by SHAKE, except that the two solutions would differ in the velocity approximation $\pmb { v } ^ { n }$ at the end of each timestep.

Example 2 Let us ilustrate the use of SHAKE with the familiar example of the planar pendulum. For the pendulum, applying SHAKE results in the discrete equations

$$
\begin{array} { r l } & { \qquad x _ { n + 1 } = x _ { n } + \Delta t u _ { n + 1 / 2 } , } \\ & { \qquad y _ { n + 1 } = y _ { n } + \Delta t v _ { n + 1 / 2 } , } \\ & { m u _ { n + 1 / 2 } = m u _ { n - 1 / 2 } - \Delta t x _ { n } \lambda _ { n } , } \\ & { m v _ { n + 1 / 2 } = m v _ { n - 1 / 2 } - \Delta t m g - \Delta t y _ { n } \lambda _ { n } , } \\ & { \qquad L ^ { 2 } = ( x _ { n + 1 } ) ^ { 2 } + ( y _ { n + 1 } ) ^ { 2 } , } \end{array}
$$

where we have violated our usual convention of writing time step index as a superscript rather than a subscript in order to avoid ambiguity with the multiplicative power.

The SHAKE method can be interpreted as follows: we first ignore the constraints and take a step of the St¨ormer–Verlet method, resulting for the pendulum in

$$
\begin{array} { l } { { \bar { x } _ { n + 1 } = x _ { n } + \Delta t u _ { n - 1 / 2 } , } } \\ { { \bar { y } _ { n + 1 } = y _ { n } + \Delta t v _ { n - 1 / 2 } - \Delta t ^ { 2 } g . } } \end{array}
$$

(This is always a point of a quadratic arc through the previous step.)

Next, we compute the oblique projection of the unconstrained step on to the configuration manifold along the direction of the normal to the constraint at the previous timestep $t _ { n }$ . For the pendulum, this means finding the intersection of a certain straight line with the circle by solving the following quadratic equation for $\lambda _ { n }$

$$
( \bar { x } _ { n + 1 } - \frac { 1 } { m } \Delta t ^ { 2 } x _ { n } \lambda _ { n } ) ^ { 2 } + ( \bar { y } _ { n + 1 } - \frac { 1 } { m } \Delta t ^ { 2 } y _ { n } \lambda _ { n } ) ^ { 2 } = L ^ { 2 } .
$$

The situation is diagrammed in Fig. 2. Note that there are, in general, two real solutions to this equation, corresponding to the two points of intersection with the circle. For small timesteps, the correct choice of multiplier will be obvious (the appropriate solution will be small in magnitude). As a simple rule, we might always choose the solution corresponding to the smaller value of the multiplier, but if the stepsize is sufficiently large, this approach could lead to an incorrect choice. In general, we should consider the smooth continuation of the solution in the parameter $\Delta t$ from $\Delta t = 0$ and $\lambda ^ { n } ( 0 ) = 0$ to the final value $\lambda ( \Delta t )$ .

![](images/9c87353f890015bb23c01bb208d12ebb09f956e565a4efdec7d051ac4ba91730.jpg)  
Figure 7.2 SHAKE discretization applied to the planar pendulum. Starting from a point on the circle $( \pmb { q } _ { n } = \left( x _ { n } , y _ { n } \right) ) ,$ ), an unconstrained step is taken (following a parabolic arc in the parameter $\Delta t$ ) to $\bar { \pmb q } _ { n + 1 } = ( \bar { x } _ { n + 1 } , \bar { y } _ { n + 1 } )$ . Next, we find the projection on to the circle of radius $L$ along the direction $\pmb { q } _ { n }$ . ✷

These same considerations enter into the discussion of the general case (7.14)– (7.17). The correct choice of the multiplier can be identified by smoothly continuing the solution as a function of the parameter $\Delta t$ starting from $\Delta t = 0$ and $\pmb { \lambda } ^ { n } ( 0 ) = \pmb { 0 }$ . For small timesteps, the correct choice of multiplier $\pmb { \lambda } ^ { n }$ will thus be small in magnitude, so that a Newton iteration started from the zero initial guess will tend to find the correct solution. For larger timesteps, though, caution must be exercised to make certain that the solution obtained is the correct one.

We next briefly comment on the error growth in these methods. Since SHAKE and RATTLE are formally equivalent, the propagation of errors is identical for the two methods. The modification of the end of timestep velocity in the RATTLE step does not effect the stability or global convergence of the method in any way.

It is relatively straightforward to derive a formula for the local error introduced in a single timestep using SHAKE or RATTLE based on comparison of the Taylor expansions of the solution and numerical solution in a step of size $\Delta t$ , starting from some given point $( \pmb { q } ^ { n } , \pmb { v } ^ { n } ) \in \tau _ { \mathcal { M } }$ . For both methods, this calculation shows that the local error is of order $\Delta t ^ { 3 }$ . Thus these methods are second-order accurate. (Higher-order schemes are discussed below, in the context of Hamiltonian systems.)

# 7.2.2 Implementation

At every step of the SHAKE (or RATTLE) discretization, we must solve a system of nonlinear equations of dimension equal to the number of constraints. In some cases, these constraints can be dealt with very easily. For example, if the constraints are linear, the work involved is usually a step of Gaussian elimination or the use of some other linear solver, and unless the dimension of the system is exceptionally large, or the equations poorly conditioned, this computation will be easy to implement. In other cases, the constraints may admit a decoupling that enables their simplified solution.

Example3Consider a system of $N$ particles，each of mass $m$ ，attachedto the surface of the unit sphere and interacting in some homogeneous two-body potential $\phi$ . The energy takes the form

$$
E = \frac 1 2 \sum _ { i = 1 } ^ { N } m _ { i } \| \pmb { v } _ { i } \| ^ { 2 } + V ( \pmb { q } _ { 1 } , \dots , \pmb { q } _ { N } ) ,
$$

where $\begin{array} { r } { V ( \pmb q ) = V ( \pmb q _ { 1 } , \dots , \pmb q _ { N } ) = \sum _ { i = 1 } ^ { N - 1 } \sum _ { j = i + 1 } ^ { N } \phi ( \| \pmb q _ { i } - \pmb q _ { j } \| ) } \end{array}$ . The equations of motion for the i th particle, $i = 1 , \dots , N$ , are

$$
\begin{array} { c } { \dot { \pmb q } _ { i } = { \pmb v } _ { i } , } \\ { m \dot { \pmb v } _ { i } = - \nabla _ { \pmb q _ { i } } V ( \pmb q ) - \pmb q _ { i } \lambda _ { i } , } \\ { \lVert { \pmb q } _ { i } \rVert ^ { 2 } = 1 , } \end{array}
$$

and the equations of the ith and jth particles are coupled only through the potential energy. Applying SHAKE discretization results in

$$
\begin{array} { r l } & { \pmb { q } _ { i } ^ { n + 1 } = \pmb { q } _ { i } ^ { n } + \Delta t \pmb { v } _ { i } ^ { n + 1 / 2 } , } \\ & { m \pmb { v } _ { i } ^ { n + 1 / 2 } = m \pmb { v } _ { i } ^ { n - \frac { 1 } { 2 } } - \Delta t \nabla _ { \pmb { q } _ { i } } V ( \pmb { q } ^ { n } ) - \Delta t \pmb { q } _ { i } ^ { n } \lambda _ { i } ^ { n } , } \\ & { \| \pmb { q } _ { i } ^ { n + 1 } \| ^ { 2 } = 1 , } \end{array}
$$

Introducing equation (7.26) into (7.25), then combining the resulting formula with the constraint (7.27) results in $N$ independent quadratic equations to be solved for the $N$ multipliers $\lambda _ { j } ^ { n }$ , $i = 1 , \dots , N$ . ✷

On the other hand, in most cases, such as for example the constraint chain, one has to solve a system of nonlinear equations for the multipliers $\pmb { \lambda } ^ { n } = \{ \lambda _ { i } ^ { n } \} _ { i = 1 , \dots , m }$ of the form

$$
g \left( \bar { q } ^ { n + 1 } - { \Delta t } ^ { 2 } M ^ { - 1 } \sum _ { i = 1 } ^ { m } G ( q ^ { n } ) ^ { T } \lambda ^ { n } \right) = 0 ,
$$

where $\bar { \pmb q } ^ { n + 1 }$ represents an unconstrained step using St¨ormer–Verlet/leapfrog. The paper [167] describing the SHAKE discretization also provided an iterative solver for the nonlinear equations (7.28); the term SHAKE is used typically to refer to the combined procedure of time discretization together with the iterative (coordinate resetting) algorithm for constraints. We divide these here into two procedures, namely SHAKE iteration for coordinate resetting and SHAKE discretization (7.14)–(7.16) .

In SHAKE iteration, we cycle through the constraints, adjusting one multiplier at each iteration. If $g _ { j }$ is the ith component of $g$ , we denote by $G _ { i } = \nabla _ { \pmb { q } } g _ { i } ( \pmb { q } )$ the i th row of the constraint Jacobian matrix (i.e. the gradient of the i th constraint function), then the iteration is as follows: First, we initialize

$$
\pmb { Q } : = \bar { \pmb { q } } ^ { n + 1 } = \pmb { q } ^ { n } + \Delta t \pmb { v } ^ { n - 1 / 2 } - \Delta t ^ { 2 } \pmb { M } ^ { - 1 } \nabla _ { \ b { q } } V ( \pmb { q } ^ { n } ) ,
$$

which is equivalent to taking $\pmb { \lambda } ^ { n }$ to be zero in (7.28).

Next, we cycle through the list of constraints and correct each constraint one after another by using the following procedure. For $i = 1 , \dots , m$ , compute an offset $\Delta \Lambda _ { j }$ in order to satisfy the i th linearized constraint equation

$$
\Delta \Lambda _ { i } : = \frac { g _ { i } ( Q ) } { G _ { i } ( Q ) M ^ { - 1 } G _ { i } ( { \pmb q } ^ { n } ) } ,
$$

and update $Q$ by

$$
\begin{array} { r } { Q : = Q - M ^ { - 1 } G _ { i } ( \pmb { q } ^ { n } ) ^ { T } \Delta \Lambda _ { i } . } \end{array}
$$

This cycle is repeated until all constraint residuals $g _ { i } ( Q )$ are smaller than some prescribed tolerance (usually a multiple of the unit rounding error). At this point we set $\pmb q ^ { n + 1 } = \pmb Q$ and continue with the next timestep.

As was shown in [13], SHAKE iteration is really a variant of nonlinear Gauss– Seidel–Newton iteration and its convergence can be justified and analyzed in the framework of Ortega and Rheinboldt [150]. In particular, it can be shown that, given a good enough initial guess for the multiplier, or a small enough step size $\Delta t$ , this iterative method eventually converges.

One can consider a variety of improvements to SHAKE iteration. Noting that SHAKE is essentially a nonlinear Gauss–Seidel iteration, it seems natural to consider the use of an SOR-type technique. For this purpose, we could introduce a parameter $\omega$ , changing the offset $\Delta \Lambda _ { j }$ at each step of iteration to $\omega \Delta \Lambda _ { j }$ .

The parameter ω can be a fixed value obtained through some preliminary experiment, or it can be obtained automatically during integration by a simple adaptive algorithm. We stress that this is a cost-free enhancement of SHAKE and it can lead to substantial speedups in the constraint-solving portion of a timestepping algorithm. Because the method is just an alternative nonlinear equation solver to SHAKE iteration, the converged numerical solution will not differ from that obtained by SHAKE iteration.

A second alternative to SHAKE iteration was also considered in [13]: we could use a Newton iteration, or variant thereof, to compute successive updates to the vector $\pmb { \lambda } ^ { n }$ . In particular, we could apply a true Newton iteration to the original nonlinear equations and use sparse matrix techniques to solve the resulting linear equations. This turns out to be somewhat expensive for most problems because the factorization of a matrix – even a sparse matrix – is relatively costly. A better alternative is to use a quasi-Newton iteration described below.

All these methods iteratively improve the whole vector of offsets $\pmb { \Delta } \pmb { \Lambda } =$ $\{ \Delta \Lambda _ { i } \}$

$$
\pmb { \cal A } : = \pmb { { \cal R } } ^ { - 1 } \pmb { g } ( \pmb { Q } ) ,
$$

where for the true Newton iteration (NIP) we have $\pmb { R } = \pmb { G } ( \pmb { Q } ) \pmb { M } ^ { - 1 } \pmb { G } ( \pmb { q } ^ { n } ) ^ { T }$ with $Q$ the latest approximation obtained from

$$
\pmb { Q } : = \pmb { Q } - \pmb { M } ^ { - 1 } \pmb { G } ( \pmb { q } ^ { n } ) ^ { T } \pmb { \Delta } \pmb { \Lambda } .
$$

For the quasi-Newton iteration we have $\pmb { R } = \pmb { G } \pmb { M } ^ { - 1 } \pmb { G } ^ { T }$ , with $\pmb { G } = \pmb { G } ( \pmb { q } ^ { k } )$ for some $\pmb q ^ { k }$ computed at a previous timestep $t _ { k }$ ( $\pmb { G }$ is updated as needed for convergence). Note that the quasi-Newton iteration matrix $R$ is symmetric and positive-definite and, hence, can be factorized in a very efficient manner [13].

SHAKE and RATTLE are particularly useful in the context of molecular dynamics. Further details will be provided in Chapter 11. We only mention here that the iterative techniques described in this section have been integrated into the CHARMM molecular dynamics software package [34] and successfully applied to several examples: $C _ { 6 0 }$ , a box of water, Myoglobin, BPTI; detailed results are reported in [13]. Roughly speaking, we can summarize the results as follows: (1) the use of an SOR parameter can improve SHAKE iteration convergence by a factor of two to three in protein dynamics simulations for no additional cost or loss of robustness, (2) the adaptive scheme for determining optimal $\omega$ in [13], although not robust, does demonstrate the feasibility of computing the SOR parameter adaptively, and (3) the symmetric adaptive Newton method may show improvement over SHAKE iteration at large step size $\Delta t$ for problems with high bond connectivity, e.g. the buckminsterfullerene $C _ { 6 0 }$ .

# 7.2.3 Numerical experiment

To conclude this section, we apply the RATTLE method to simulate a small model system consisting of six unit-mass particles linked by six rigid unit length constraints. The hexagonal starting configuration is shown in Fig. 7.3.

Note there are six multipliers and constraint equations, and, in the planar case that we consider here, a total of $2 \times 6 - 6 = 6$ degrees of freedom. The next nearest neighbors are linked by springs with rest length $\sqrt { 3 }$ . Pairs numbered (1,4), (2,5), and (3,6) are linked by springs with rest length 2 (see Fig. 7.3). In this way the system tends to retain the shape of a hexagon during simulation.

![](images/bafe2893b7c5119f8c8177bce8d474c3600ea5f8f13091483866f1c0f675120e.jpg)  
Figure 7.3 Diagram of a planar constraint loop consisting of six particles of unit mass.

We placed the system in a square box with sides at $x = \pm 2$ , $y = \pm 2$ . The interaction with the boundary of the box was introduced with the following soft wall potential

$$
V _ { \mathrm { w a l l } } = { \frac { \epsilon } { 6 } } \sum _ { i = 1 } ^ { 6 } \left[ ( x _ { i } + 2 ) ^ { - 6 } + ( x _ { i } - 2 ) ^ { - 6 } + ( y _ { i } + 2 ) ^ { - 6 } + ( y _ { i } - 2 ) ^ { - 6 } \right] .
$$

We chose $\epsilon = 0 . 0 1$ , strongly localizing collisions at nearly the point of contact with the boundary of the region.

It is important to make sure that the initial velocities are consistent with the constraint (7.5). This can always be achieved by a simple projection step. In our case, we simply initialized the positions at the global minimum of potential energy (regular hexagon configuration) and gave each atom of the system the same initial velocity, propelling the entire object rigidly toward the boundary. Following the first impact, the system begins chaotic tumbling and oscillatory vibration.

![](images/59d311a7f8f4d9524f77880a449048eac77824561f3943d3694ecba5c5fab577.jpg)  
Figure 7.4 Snapshots of the motion of the six particle chain.

We applied RATTLE to simulate the constraint chain over a time interval [0, 100]. Some frames of the motion are shown in Fig. 7.4.

We compare energy errors for various simulations. In the first run, the stepsize was set to $\Delta t = 0 . 0 8$ . The result, shown in the upper panel of Fig. 7.5, is not very encouraging. The energy seems to hop about in an almost random pattern. The jumps in energy coincide with close approaches of a particle of the chain to the walls of the box, i.e. “collisions.” Here the $r ^ { - 6 }$ potential gives rise to a strong restraining force, propelling the particle away at relatively high velocity. At these points, the stability of the method breaks down for this stepsize: in essence, the “perturbed Hamiltonian” expansion discussed in Chapter 5 does not really exist at these stepsizes; the exponentially small error term mentioned in Chapter 5 is not really small at all. When the stepsize is reduced, say to $\Delta t = 0 . 0 4$ , the energy is stabilized at nearly the correct value (see lower panel of Fig. 7.5).1

The second-order convergence of the RATTLE method can be verified numerically by computing trajectories with several different stepsizes, then graphing the error v. stepsize in logarithmic scale (see Fig. 7.6).

![](images/52f6e864278d3efa6d8966d3e78e6f67c6ca1ee762ca64aa448041f9995e8b5f.jpg)  
Figure 7.5 Energies against time for two runs of RATTLE on the six-particle chain, upper panel $\Delta t = 0 . 0 8$ , lower panel $\Delta t = 0 . 0 4$ .

![](images/fbbfd572803b73784fc7492cfcfd471c96077c7062c540b98345548795151e0b.jpg)  
Figure 7.6 Verification of second-order convergence of RATTLE.

# 7.3 Transition to Hamiltonian mechanics

We now turn to the Hamiltonian formalism with constraints. As done before in Chapter 3, we formally introduce conjugate momenta $p = M { \dot { q } }$ and rewrite (7.1)–(7.3) as

$$
\begin{array} { c } { { \displaystyle \frac { d } { d t } \pmb { q } = \pmb { M } ^ { - 1 } \pmb { p } , } } \\ { { \displaystyle \frac { d } { d t } \pmb { p } = - \nabla _ { \pmb { q } } V ( \pmb { q } ) - \pmb { G } ( \pmb { q } ) ^ { T } \pmb { \lambda } , } } \\ { { \displaystyle \ \mathbf { 0 } = \pmb { g } ( \pmb { q } ) . } } \end{array}
$$

The first equation is the gradient of the augmented Hamiltonian

$$
\tilde { H } = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } + \pmb { V } ( \pmb { q } ) + \pmb { g } ( \pmb { q } ) ^ { T } \pmb { \lambda } ,
$$

with respect to $p$ , while the second equation is equal to the negative gradient of $\tilde { H }$ with respect to $\pmb q$ with $\pmb { \lambda }$ treated as a constant.

The form of the Hamiltonian $\tilde { H }$ suggests a correspondence between Hamiltonian formulations with and without constraints. Let $H$ be the energy of a certain unconstrained mechanical system, so the equations of motion are just

$$
\begin{array} { c } { { \displaystyle { \frac { d } { d t } } \pmb { q } = + \nabla _ { p } H ( \pmb { q } , \pmb { p } ) , } } \\ { { \displaystyle { \frac { d } { d t } } \pmb { p } = - \nabla _ { \pmb { q } } H ( \pmb { q } , \pmb { p } ) . } } \end{array}
$$

Similar to the situation above, introduce the augmented Hamiltonian

$$
\tilde { H } ( \pmb { q } , \pmb { p } ) = H ( \pmb { q } , \pmb { p } ) + \pmb { g } ( \pmb { q } ) ^ { T } \pmb { \lambda } ,
$$

and write the equations of motion (the formulation of a constrained Hamiltonian system in natural coordinates):

$$
\begin{array} { c } { \displaystyle \frac { d } { d t } \pmb { q } = \nabla _ { p } H ( \pmb { q } , \pmb { p } ) , } \\ { \displaystyle \frac { d } { d t } \pmb { p } = - \nabla _ { \pmb { q } } H ( \pmb { q } , \pmb { p } ) - G ( \pmb { q } ) ^ { T } \pmb { \lambda } , } \\ { \displaystyle \ \mathbf { 0 } = \pmb { g } ( \pmb { q } ) . } \end{array}
$$

Example 4The constrained Hamiltonian formulation (7.29)-(7.31) can be derived from a constrained Lagrangian formulation. Recall from Chapter 3 that Lagrange’s equations for a mechanical system with Lagrangian function $L \left( \pmb { q } , \dot { \pmb { q } } \right)$ are given by

$$
\frac { d } { d t } \nabla _ { \dot { q } } L ( \pmb { q } , \dot { \pmb { q } } ) - \nabla _ { q } L ( \pmb { q } , \dot { \pmb { q } } ) = \mathbf { 0 } .
$$

These are the Euler–Lagrange equations minimizing the action integral

$$
\mathcal { L } [ \pmb { q } ] = \int _ { t _ { 0 } } ^ { t _ { 1 } } L ( \pmb { q } ( t ) , \dot { \pmb { q } } ( t ) ) d t .
$$

To obtain the constrained Lagrange’s equation we consider the augmented action integral

$$
{ \mathcal { L } } [ { \pmb q } , \lambda ] = \int _ { t _ { 0 } } ^ { t _ { 1 } } \left[ L ( { \pmb q } ( t ) , { \dot { \pmb q } } ( t ) ) - \lambda ( t ) ^ { T } { \pmb g } ( { \pmb q } ( t ) ) \right] d t ,
$$

and, upon taking variations in $\pmb q$ and $\pmb { \lambda }$ , derive the associated Euler–Lagrange equations

$$
\begin{array} { c } { \displaystyle \frac { d } { d t } \nabla _ { \dot { q } } L ( \dot { \pmb q } , \dot { \pmb q } ) = \nabla _ { q } L ( \pmb q , \dot { \pmb q } ) + \pmb { G } ( \pmb q ) ^ { T } \pmb \lambda , } \\ { \displaystyle \ \mathbf 0 = \pmb { g } ( \pmb q ) . } \end{array}
$$

The transition to the Hamiltonian formulation can be achieved by introducing the canonical momenta

$$
\pmb { p } = \nabla _ { \dot { \pmb { q } } } L ( \pmb { q } , \dot { \pmb { q } } ) ,
$$

and by employing the standard Legendre transformation

$$
\tilde { H } ( q , p , \lambda ) = p \cdot \dot { q } - \left[ L ( q , \dot { q } ) - \lambda ^ { T } g ( q ) \right] = H ( q , p ) + \lambda ^ { T } g ( q ) .
$$

For example, the $N .$ -body Lagrangian

$$
L ( { \pmb q } , { \dot { \pmb q } } ) = \frac { 1 } { 2 } { \dot { \pmb q } } ^ { T } { \pmb M } { \dot { \pmb q } } - { \cal V } ( { \pmb q } )
$$

gives rise to the Hamiltonian

$$
\tilde { H } = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } + \pmb { V } ( \pmb { q } ) + \pmb { g } ( \pmb { q } ) ^ { T } \pmb { \lambda } .
$$

It is easily verified that the constrained equations (7.29)–(7.31) can be reduced to the Lagrangian equations (7.32)–(7.33) and that both formulations lead to identical solutions curves $\pmb q ( t )$ . However, while $( \pmb q ( t ) , \dot { \pmb q } ( t ) ) \in T \mathcal { M } ,$ the

natural coordinates $( \pmb q , \pmb p )$ must satisfy the equation (7.31) and the corresponding momentum-level constraint

$$
\frac { d } { d t } g ( q ) = G ( q ) \nabla _ { p } H ( q , p ) = \bf { 0 } .
$$

The subset of $\mathbb { R } ^ { 2 d }$ defined by (7.31) and (7.34) we term the phase space and denote by $\mathcal { P }$ .

Observe that the energy $H$ of the unconstrained system remains a first integral of (7.29)–(7.31). To see this, first observe that, along solutions

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } H ( { \boldsymbol { q } } , { \boldsymbol { p } } ) = H _ { { \boldsymbol { q } } } ( { \boldsymbol { q } } , { \boldsymbol { p } } ) { \dot { \boldsymbol { q } } } + H _ { \boldsymbol { p } } ( { \boldsymbol { q } } , { \boldsymbol { p } } ) { \dot { \boldsymbol { p } } } } \\ { = H _ { \boldsymbol { q } } ( { \boldsymbol { q } } , { \boldsymbol { p } } ) \nabla _ { \boldsymbol { p } } H ( { \boldsymbol { q } } , { \boldsymbol { p } } ) - H _ { \boldsymbol { p } } ( { \boldsymbol { q } } , { \boldsymbol { p } } ) \left[ \nabla _ { \boldsymbol { q } } H ( { \boldsymbol { q } } , { \boldsymbol { p } } ) + G ( { \boldsymbol { q } } ) ^ { T } \boldsymbol { \lambda } \right] } \\ { = - { \boldsymbol { \lambda } } ^ { T } \left[ G ( { \boldsymbol { q } } ) \nabla _ { \boldsymbol { p } } H ( { \boldsymbol { q } } , { \boldsymbol { p } } ) \right] , } \end{array}
$$

then note that the latter expression vanishes along the hidden constraint (7.34).

# 7.4 The symplectic structure with constraints

In this section, we show that (7.29)–(7.31) is indeed a generalization of unconstrained canonical Hamiltonian systems as discussed in Chapter 3. According to a perspective due to DIRAC [50], the flow of a Hamiltonian system on a manifold can be embedded in the flow of an unconstrained Hamiltonian system. Following this idea, the solutions of (7.29)–(7.31) can simply be viewed as evolving in the phase space of a standard canonical Hamiltonian system with extended Hamiltonian

$$
\hat { H } = H ( \pmb { q } , \pmb { p } ) + \pmb { g } ( \pmb { q } ) ^ { T } \pmb { \Lambda } ( \pmb { q } ^ { - 1 } , \pmb { p } ) ,
$$

and $\pmb { \Lambda } ( \pmb q , \pmb v )$ given by (7.11) if $H = { \pmb p } ^ { T } { \pmb M } ^ { - 1 } { \pmb p } / 2 + V ( { \pmb q } )$ or by a proper generalization for more general unconstrained Hamiltonian functions $H$ . The manifold $\mathcal { P }$ is an invariant manifold for the solution operator $\boldsymbol { \Phi } _ { t , \hat { H } }$ . For a discussion of Dirac’s method, see MARSDEN AND RATIU [124]; for a discussion of numerical methods based on this, see LEIMKUHLER AND REICH [111].

Dirac’s approach allows us to consider the symplectic structure on the phase space $\mathcal { P }$ as the restriction of the canonical symplectic structure $d \pmb { q } \wedge d \pmb { p }$ on $\mathbb { R } ^ { 2 d }$ to the phase space (submanifold) $\mathcal { P }$ . We outline the derivation of this restricted symplectic structure and its invariance under the flow operator of (7.29)–(7.31) in more detail in the remainder of this section. Contrary to this global approach, one can also introduce a symplectic structure on phase space by considering local parametrizations of $\mathcal { P }$ . This is the more traditional approach and a short outline will be provided later in this chapter.

In keeping with the notation introduced earlier in Chapters 3 and 4, we start with differential one-forms $d \pmb q$ and $d p$ defined over the unconstrained space $\mathbb { R } ^ { 2 d }$ . We now restrict these one-forms to the solution space by requiring that

$$
G ( q ) d q = \mathbf { 0 } { \mathrm { a n d } } f _ { q } ( q , p ) d q + f _ { p } ( q , p ) d p = \mathbf { 0 } ,
$$

for all $( \pmb { q } , \pmb { p } ) \in \mathcal { P }$ , where

$$
f ( \pmb { q } , \pmb { p } ) = \pmb { G } ( \pmb { q } ) \nabla _ { p } H ( \pmb { q } , \pmb { p } )
$$

is the hidden constraint function. In more abstract terms, the differential oneforms $( d \pmb { q } , d \pmb { p } )$ are now elements of the cotangent space $\tau ^ { * } { \mathcal { P } }$ of $\mathcal { P }$ (imbedded into $\mathbb { R } ^ { 2 d }$ ) [124].

The variational equations corresponding to (7.29)–(7.31) can be obtained by straightforward linearization and the resulting equations for the differential one-forms are

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } d { \pmb q } = H _ { p q } ( { \pmb q } , { \pmb p } ) d { \pmb q } + H _ { p p } ( { \pmb q } , { \pmb p } ) d { \pmb p } } , } } \\ { { \displaystyle { \frac { d } { d t } d { \pmb p } = - H _ { q q } ( { \pmb q } , { \pmb p } ) d { \pmb q } - H _ { q p } ( { \pmb q } , { \pmb p } ) d { \pmb p } - d \left( G ( { \pmb q } ) { \pmb \lambda } \right) , } } } \\ { { \displaystyle { \bf 0 } = G ( { \pmb q } ) d { \pmb q } . } } \end{array}
$$

It is easily verified by differentiation of (7.38) with respect to time that the solutions of (7.36)–(7.38) indeed satisfy (7.35). Hence we are left with the task to show that the canonical wedge product $d \pmb { q } \wedge d \pmb { p }$ , restricted to (7.35), is an invariant of (7.36)–(7.38). We need the following:

Lemma 1 Assume that the differential one-form dq satisfies (7.38), then

$$
d \pmb { q } \wedge d ( \pmb { G } ( \pmb { q } ) ^ { T } \pmb { \lambda } ) = \mathbf { 0 } .
$$

Proof:

$$
d \pmb { q } \wedge d \big ( \pmb { G } ( \pmb { q } ) ^ { T } \pmb { \lambda } \big ) = d \pmb { q } \wedge \pmb { G } ( \pmb { q } ) ^ { T } d \pmb { \lambda } + \sum _ { i = 0 } ^ { m } \lambda _ { i } d \pmb { q } \wedge \pmb { r } _ { i } d \pmb { q } ,
$$

where the components of $\pmb { \lambda }$ have been indexed by a subscript and

$$
\boldsymbol { \Gamma } _ { i } = \left\{ \frac { \partial ^ { 2 } g _ { i } } { \partial q _ { k } \partial q _ { I } } ( \pmb { q } ) \right\}
$$

is the (symmetric!) Hessian matrix of the i th constraint function. Now

$$
d \pmb { q } \wedge \pmb { G } ( \pmb { q } ) ^ { T } d \pmb { \lambda } = \pmb { G } ( \pmb { q } ) d \pmb { q } \wedge d \pmb { \lambda } = \pmb { 0 } ,
$$

for any values of $d \pmb { \lambda }$ because of (7.38). Finally, each of the terms of the summation can be eliminated since $d \pmb { q } \wedge \pmb { r } _ { i } d \pmb { q } = \pmb { 0 }$ . ✷

We now easily verify (dropping arguments to simplify notations) that

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } d { \pmb q } \wedge d { \pmb p } = d \dot { q } \wedge d { \pmb p } + d { \pmb q } \wedge d \dot { \pmb p } } } } \\ { { \displaystyle \qquad = ( H _ { p q } d { \pmb q } + H _ { p p } d { \pmb p } ) \wedge d p - d { \pmb q } \wedge \left[ H _ { q q } d { \pmb q } + H _ { q p } d { \pmb p } + d \left( { \pmb G } ^ { T } \pmb \lambda \right) \right] } } \\ { { \displaystyle \qquad = H _ { p q } d { \pmb q } \wedge d { \pmb p } - d { \pmb q } \wedge H _ { q p } d { \pmb p } + H _ { p p } d { \pmb p } \wedge d { \pmb p } - d { \pmb q } \wedge H _ { q q } d { \pmb q } } . } \end{array}
$$

These terms all vanish using the properties of the wedge product given in Chapter 3. Thus the canonical wedge product is preserved along solutions of (7.36)– (7.38).

In most textbooks on classical mechanics, mechanical systems subject to a holonomic constraint manifold $\mathcal { M }$ are formulated as Hamiltonian systems on the cotangent space $\tau ^ { * } { \mathcal { M } }$ (see ARNOLD [7] and MARSDEN AND RATIU [124]). Here we have defined constrained Hamiltonian systems over a different phase space $\mathcal { P }$ . However, it turns out, not entirely unexpectedly, that the cotangent space $\tau ^ { * } { \mathcal { M } }$ and the phase space $\mathcal { P }$ are diffeomorphic under the symplectic transformation

$$
( \pmb { q } , \pmb { p } ) \in \mathcal { P }  ( \pmb { q } , \pmb { \bar { p } } ) \in T ^ { * } \mathcal { M }
$$

defined by

$$
\bar { p } = p + G ( q ) ^ { T } \pmb { \mu } , \qquad G ( q ) \bar { p } = { \bf 0 } .
$$

Here we have identified $\tau ^ { * } { \mathcal { M } }$ with the tangent space $T \mathcal { M }$ as defined earlier in Section 7.1. Indeed, upon applying Lemma 1, it is easy to show that

$$
d \pmb { q } \wedge d \pmb { p } = d \pmb { q } \wedge d \pmb { \bar { p } } .
$$

Hence the symplectic structure on $\tau ^ { * } { \mathcal { M } }$ is again given by the restriction of the standard canonical structure to ${ \mathcal { T } } ^ { * } { \mathcal { M } }$ See also MCLACHLAN AND SCOVEL [133].

# 7.5 Direct symplectic discretization

We come to the direct symplectic integration of general Hamiltonian systems (7.29)–(7.30) subject to holonomic constraints (7.31). We first discuss general second-order methods and then briefly outline the derivation of higher-order methods by composition.

# 7.5.1 Second-order methods

In LEIMKUHLER AND SKEEL [113], the symplecticness of the SHAKE and RATTLE methods was first explained. Here we will introduce a generalization of this framework, following the ideas of REICH [155]. Let us consider a Hamiltonian system

$$
\tilde { H } = H ( \pmb { q } , \pmb { p } ) + \pmb { g } ( \pmb { q } ) ^ { T } \pmb { \lambda } ,
$$

subject to the constraint $g ( \pmb q ) = \pmb 0$ . Let us also assume that a second-order, symplectic, and symmetric integration method is known for the unconstrained system

$$
\frac { d } { d t } \pmb { q } = \nabla _ { p } H ( \pmb { q } , \pmb { p } ) , \quad \frac { d } { d t } \pmb { p } = - \nabla _ { q } H ( \pmb { q } , \pmb { p } ) .
$$

For $H = T ( p ) { + } V ( q )$ , this could, for example, be the St¨ormer–Verlet method. For a general, non-separable, Hamiltonian, one could apply the implicit midpoint rule or the generalized St¨ormer–Verlet/leapfrog method. In any case, let us denote the chosen method by $\psi _ { \Delta t }$ . Then the following method is a constraint-preserving, symplectic, symmetric, and second-order method for the constrained Hamiltonian system with Hamiltonian $\tilde { H }$ :

$$
\begin{array} { c } { { \displaystyle \bar { p } ^ { n } = p ^ { n } - \frac { \Delta t } { 2 } G ( q ^ { n } ) ^ { T } \lambda _ { ( r ) } ^ { n } , } } \\ { { \displaystyle ( q ^ { n + 1 } , \bar { p } ^ { n + 1 } ) = \psi _ { \Delta t } ( q ^ { n } , \bar { p } ^ { n } ) , } } \\ { { \displaystyle 0 = g ( q ^ { n + 1 } ) , } } \\ { { \displaystyle p ^ { n + 1 } = \bar { p } ^ { n + 1 } - \frac { \Delta t } { 2 } G ( q ^ { n + 1 } ) ^ { T } \lambda _ { ( v ) } ^ { n + 1 } , } } \\ { { \displaystyle 0 = G ( q ^ { n + 1 } ) \nabla _ { p } H ( q ^ { n + 1 } , p ^ { n + 1 } ) . } } \end{array}
$$

Note that this method reduces to RATTLE for $H = p ^ { T } M ^ { - 1 } p / 2 + V ( \pmb q )$ and taking the St¨ormer–Verlet method as $\psi _ { \Delta t }$ . This correspondence should guide us to the implementation of the method for a more general $\psi _ { \Delta t }$ .

Let us now briefly verify the various geometric properties of (7.39)–(7.43). (i) The method obviously conserves phase space $\mathcal { P }$ . However, without changing the propagation in the $\pmb q$ -variables, one can also enforce the cotangent space

$\tau ^ { * } { \mathcal { M } }$ by replacing the momentum-constraint equation (7.43) by

$$
\mathbf { 0 } = { \cal G } ( q ^ { n + 1 } ) p ^ { n + 1 } .
$$

See also MCLACHLAN AND SCOVEL [133]. (ii) The method is symplectic. Indeed, by the symplecticness of $\psi _ { \Delta t }$ we know that

$$
d { \pmb q } ^ { n } \wedge d \bar { \pmb p } ^ { n } = d { \pmb q } ^ { n + 1 } \wedge d \bar { \pmb p } ^ { n + 1 } .
$$

On the other hand, both momentum maps (7.39) and (7.42) are also symplectic. This is a consequence of Lemma 1 of Section 7.4. (iii) The method is also symmetric as easily shown by replacing $\Delta t$ by $- \Delta t$ and $( { \pmb q } ^ { n } , { \pmb p } ^ { n } , \pmb \lambda _ { ( \mathsf { r } ) } ^ { n } )$ by $( { \pmb q } ^ { n + 1 } , { \pmb p } ^ { n + 1 } , \pmb { \lambda } _ { ( \vee ) } ^ { n + 1 } )$ . (iv) The method is certainly consistent. Since it is also symmetric, second-order convergence follows.

Let us give an explicit example. We take the generalized St¨ormer–Verlet/ leapfrog method as $\psi _ { \Delta t }$ . This yields the method

$$
\begin{array} { c } { { p ^ { n + 1 / 2 } = p ^ { n } - \displaystyle \frac { \Delta t } { 2 } \nabla _ { q } H ( p ^ { n + 1 / 2 } , q ^ { n } ) - \displaystyle \frac { \Delta t } { 2 } G ( q ^ { n } ) \lambda _ { ( r ) } ^ { n } ~ , } } \\ { { q ^ { n + 1 } = q ^ { n } + \displaystyle \frac { \Delta t } { 2 } \left[ \nabla _ { p } H ( p ^ { n + 1 / 2 } , q ^ { n } ) + \nabla _ { p } H ( p ^ { n + 1 / 2 } , q ^ { n + 1 } ) \right] ~ , } } \\ { { \displaystyle \quad \quad \mathbf { 0 } = g ( q ^ { n + 1 } ) , } } \\ { { p ^ { n + 1 } = p ^ { n + 1 / 2 } - \displaystyle \frac { \Delta t } { 2 } \nabla _ { q } H ( p ^ { n + 1 / 2 } , q ^ { n + 1 } ) - \displaystyle \frac { \Delta t } { 2 } G ( q ^ { n + 1 } ) \lambda _ { ( v ) } ^ { n + 1 } , } } \\ { { \displaystyle \quad \quad \mathbf { 0 } = G ( q ^ { n + 1 } ) \nabla _ { p } H ( q ^ { n + 1 } , p ^ { n + 1 } ) . } } \end{array}
$$

This method has first been proposed by JAY [95].

Let us briefly comment on the conservation of first integrals. Assume we are given a function $F$ such that $\{ F , \tilde { H } \} = 0$ and, furthermore, both the unconstrained Hamiltonian $H$ as well as the constraints ${ \pmb g } ( { \pmb q } )$ are invariant under the Hamiltonian flow map of $F$ . Then (7.39)–(7.43) will preserve $F$ if and only if the unconstrained method $\psi _ { \Delta t }$ conserves $F$ .

# 7.5.2 Higher-order methods

Higher-order methods can now be obtained in two ways. One option is to generalize partitioned Runge–Kutta methods based on Lobbatto IIIA–IIIB quadrature rules to constrained Hamiltonian systems. For details see JAY [95]. However, the methods suffer from the same drawbacks as mentioned in Chapter 6 for general symplectic (partitioned) Runge–Kutta methods. The second option is to apply the idea of composition. Denote the second-order symmetric method (7.39)–(7.43) by $\hat { \pmb { { \psi } } } _ { \Delta t }$ . Then we consider the concatenation method

$$
\begin{array} { r } { \widetilde { \pmb { \psi } } _ { \Delta t } = \hat { \pmb { \psi } } _ { w _ { s } \Delta t } \circ \hat { \pmb { \psi } } _ { w _ { s - 1 } \Delta t } \circ \cdots \circ \hat { \pmb { \psi } } _ { w _ { 2 } \Delta t } \circ \hat { \pmb { \psi } } _ { w _ { 1 } \Delta t } , } \end{array}
$$

with $\{ w _ { i } \} _ { i = 1 , \dots , s }$ free parameters that can be chosen exactly as described in Chapter 6. For example, the coefficients for a sixth-order method, as given in Chapter 6, can be applied to (7.44) and, again, yield a sixth-order (constrained) method. The crucial point is that the error analysis for such composition methods is the same independent of the fact that $( \pmb { q } ^ { n } , \pmb { p } ^ { n } ) \in \mathcal { P }$ instead of $( \pmb { q } ^ { n } , \pmb { p } ^ { n } ) \in \mathbb { R } ^ { 2 d }$ . See REICH [155, 157] for further details.

# 7.6 Alternative approaches to constrained integration

In this section, we summarize some alternative approaches to integration of the constrained problem. Generally speaking, approaches can be divided into two classes of methods according to how they maintain the constraints: one class of schemes relies on a local parametrization of the constraint manifold, while the other uses projections.

The traditional treatment of constrained systems is based on a reduction to an unconstrained system in some minimal set of variables. The phase space of the problem then becomes a (flat) Euclidean space, but the parameters are defined as complicated nonlinear functions of the natural coordinates. The appeal of this approach is that the ordinary differential equations can then be treated directly by a standard numerical method. If the original constrained system is a holonomic Hamiltonian system, we show here that the reduced problem can also be taken to be Hamiltonian, hence a symplectic method can be used for discretization. However, we also point out some pitfalls with this approach and we do not recommend it for general integrations.

# 7.6.1 Parametrization of manifolds – local charts

Consider a constrained Hamiltonian system (7.1)–(7.3). The full rank assumption on $G ( q )$ assumed in the formulation of the Euler–Lagrange equations implies, via the implicit function theorem, that the components of the phase space variable $\pmb { z } = ( \pmb { q } , \pmb { p } ) \in \mathbb { R } ^ { 2 d }$ can at any point be separated into two subvectors $z _ { 1 }$ and $z _ { 2 }$ , of dimensions $2 m$ and $2 ( d - m )$ , respectively, and the constraints locally solved for $z _ { 1 }$ smoothly in terms of $z _ { 2 }$ . We say that the dimension of the manifold $T \mathcal { M }$ is $2 ( d - m )$ because of this fact. The local partitioning of the variables into $z _ { 1 }$ and $z _ { 2 }$ is one example of a parameterization of the constraint. More generally, we can introduce any set of independent variables (parameters) together with appropriate functions which allow us to describe, at least locally, the constraint surface in terms of those parameters.

Example 5Consider the plane pendulum which has the position constraint $x ^ { 2 } + y ^ { 2 } =$ $L ^ { 2 }$ and the tangency constraint $x { \dot { x } } + y { \dot { y } } = 0$ . As long as $y > 0$ , we can solve the position constraint for $y$ in terms of $X$

$$
y = \sqrt { L ^ { 2 } - x ^ { 2 } } ,
$$

and solve the tangency condition $x { \dot { x } } + y { \dot { y } } = 0$ for $v = { \dot { y } }$ in terms of $X$ , and $u = \dot { x }$

$$
v = - x u / \sqrt { L ^ { 2 } - x ^ { 2 } } .
$$

After differentiating with respect to time, it is formally possible to rewrite the pendulum equations of motion in terms of $X$ and $u$ only. A similar formulation could be used to described the case $y < 0$ , and we could as well rewrite the equations in terms of $y , v$ (with appropriate domain restrictions). ✷

Parameterizations are, at first glance, appealing mechanisms for describing constrained mechanical motion, however they may introduce a number of complications in practice. For instance, the set of parameters is usually only valid locally, i.e. within a finite region of space; for realistic mechanical problems we often need a set of parameterizations, defined in overlapping regions of space, which together include the entire phase space of the problem (the tangent bundle of $\mathcal { M }$ . The parameterizations are then typically taken to map parameters from an open subspace of Euclidean space (of dimension $2 ( d - m ) )$ on to the tangent bundle. Such a family of parameterizations is called an atlas of the manifold, and the individual parameterizations are referred to as local charts.

# 7.6.2 The Hamiltonian case

The concept of local chart carries over to the Hamiltonian setting. If we introduce a parameterization of the position constraint in terms of a parameter $\pmb { \xi }$ , then the corresponding canonical momenta $\pmb { \nu }$ are defined by a proper generalization of the canonical lift transformation introduced in Chapter 3. We summarize the important result in the following theorem.

Theorem 2 Consider the general mechanical system (7.29)–(7.31) subject to $m \ < \ d$ smooth constraint $g ( \pmb q ) = \pmb 0$ . Assume that $G ( q )$ is of full rank (has linearly independent rows) along the configuration manifold ${ \mathcal { M } } .$ . Suppose that $\phi : \mathbb { R } ^ { d - m }  \mathbb { R } ^ { d }$ defines a local coordinatization of the configuration space in terms of a new variable $\pmb { \xi } \in \mathbb { R } ^ { d - m }$ by

$$
\pmb { q } = \pmb { \phi } ( \pmb { \xi } ) .
$$

Then the canonical momenta $\pmb { \nu }$ are defined by the equations

$$
\begin{array} { r } { \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) ^ { T } \pmb { p } = \pmb { \nu } , } \end{array}
$$

and the Hamiltonian corresponding to the new variables is

$$
\tilde { H } ( \pmb { \xi } , \pmb { \nu } ) = H ( \pmb { \phi } ( \pmb { \xi } ) , \left( \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) ^ { T } \right) ^ { + } \pmb { \nu } ) ,
$$

where $\pmb { A } ^ { + } = \pmb { A } ^ { T } ( \pmb { A } \pmb { A } ^ { T } ) ^ { - 1 }$ represents a right pseudo-inverse of the matrix A.

Because the differential equations (7.29)–(7.31) can be expressed as an unconstrained Hamiltonian system in the parameters, we know that the two-form $d \pmb \xi \wedge d \pmb \nu$ will be preserved by the phase flow. This could be taken as a definition of the canonical two-form for the constrained system.

We have already seen that, along the constraint, the canonical two-form $d \pmb { q } \wedge d \pmb { p }$ is conserved. These two expressions are in fact equivalent, as the following theorem shows.

Theorem 3 If dq and dp represent a solution of the constrained variational equations (7.36)–(7.37), and $\pmb { \xi }$ and $\pmb { \nu }$ are defined as in Theorem 2, then

$$
d \pmb { q } \wedge d \pmb { p } = d \pmb { \xi } \wedge d \pmb { \nu } .
$$

Proof. The proof of this theorem is straightforward: first, note that

$$
\begin{array} { c } { d \pmb { q } \wedge d \pmb { p } = ( \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) d \pmb { \xi } ) \wedge d \pmb { p } } \\ { = d \pmb { \xi } \wedge ( \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) ) ^ { T } d \pmb { p } . } \end{array}
$$

Now

$$
d \pmb { \nu } = ( \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) ) ^ { T } d \pmb { p } + \sum _ { i = 1 } ^ { d } p _ { i } \phi _ { i , \pmb { \xi } \pmb { \xi } } d \pmb { \xi } ,
$$

where $\phi _ { j }$ is the ith component of the vector function $\phi$ and $\phi _ { i , \xi \xi }$ its Hessian. Therefore

$$
\begin{array} { l } { d \pmb { \xi } \wedge d \pmb { \nu } = d \pmb { \xi } \wedge ( \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) ) ^ { T } d \pmb { p } + \displaystyle \sum _ { i = 1 } ^ { d } p _ { i } d \pmb { \xi } \wedge \phi _ { i , \pmb { \xi } \pmb { \xi } } ( \pmb { \xi } ) d \pmb { \xi } } \\ { = d \pmb { \xi } \wedge ( \pmb { \phi } _ { \pmb { \xi } } ( \pmb { \xi } ) ) ^ { T } d \pmb { p } , } \end{array}
$$

which concludes the proof.

Although the above discussion is local in the sense that it assumes that the parameters are defined by a single coordinate chart, there is nothing to prevent extending the idea to a family of charts defining a “symplectic atlas.”