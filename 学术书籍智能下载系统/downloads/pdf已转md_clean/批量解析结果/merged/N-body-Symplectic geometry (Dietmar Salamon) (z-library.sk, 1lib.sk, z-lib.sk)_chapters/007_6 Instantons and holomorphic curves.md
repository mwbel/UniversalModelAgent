# 6 Instantons and holomorphic curves

The proof of Theorem 1.1 is based on a comparison between holomorphic curves in $M ( P )$ and self-dual instantons on the 4-manifold $\Sigma _ { h } \times \Pi$ . To carry this out we must choose a metric on $\Sigma _ { h }$ . Let $\langle , \rangle _ { s }$ be a one parameter family of metrics on $\pmb { \Sigma }$ such that

$$
\langle d h ( z ) \zeta _ { 0 } , d h ( z ) \zeta _ { 1 } \rangle _ { s } = \langle \zeta _ { 0 } , \zeta _ { 1 } \rangle _ { s + 1 } .
$$

Then the associated Hodge $\pmb { \cdot } \pmb { \ast } .$ -operators $* _ { s } : \Omega ^ { j } \left( \mathfrak { g } _ { P } \right) \to \Omega ^ { 2 - j } \left( \mathfrak { g } _ { P } \right)$ satisfy

$$
* _ { s + 1 } \circ f ^ { * } = f ^ { * } \circ * _ { s } .
$$

This defines a metric on $P _ { f }$ : whenever $\xi ( s ) , \eta ( s ) \in \Omega ^ { j } ( \mathfrak { g } _ { P } )$ with $\xi ( s + 1 ) =$ $f ^ { * } \xi ( s )$ and $\eta ( s + 1 ) = f ^ { \ast } \eta ( s )$ then the function

$$
\langle \xi ( s ) , \eta ( s ) \rangle _ { s } = \int _ { \Sigma } \langle \xi ( s ) \wedge * _ { s } \eta ( s ) \rangle
$$

is of period 1 in $\pmb { \mathscr { s } }$ . The inner product of $\pmb { \xi }$ and $\pmb { \eta }$ is defined as the integral of this function over the unit interval

$$
\langle \xi , \eta \rangle = \int _ { 0 } ^ { 1 } \int _ { \Sigma } \langle \xi ( s ) \wedge * _ { s } \eta ( s ) \rangle d s .
$$

Now recall that the tangent space to $M ( P )$ at $\pmb { A }$ is the quotient $H _ { A } ^ { 1 } ( \Sigma ) =$ $\mathtt { k e r } d _ { A } / \mathrm { i m } d _ { A }$ . The metrics on $\pmb { \Sigma }$ determine a family of complex structures

$$
J _ { s } = * _ { s } : H _ { A } ^ { 1 } ( \Sigma ) \to H _ { A } ^ { 1 } ( \Sigma )
$$

and condition (20) implies that these satisfy (5) with $\phi = \phi _ { f }$ . In order for the space of harmonic forms to be invariant under $\star _ { \mathfrak { s } }$ we must use the $L ^ { 2 }$ -adjoint $d _ { A } ^ { * } = - * _ { s } d _ { A } * _ { s }$ with respect to the $\pmb { \mathscr { s } }$ -metric.

Any smooth function $u : \mathbb { R } ^ { 2 } \to \mathcal { M } ( P )$ lifts to a smooth function $A :$ $\Pi ^ { 2 }  { \mathcal { A } } _ { \mathrm { f l a t } } ( P )$ . For any such map the partial derivatives $\partial A / \partial s$ and $\partial A / \partial t$ lie in the kernel of $d _ { A }$ but will in general not be harmonic. To apply a complex structure we must first project these derivatives into the space of harmonic forms corresponding to this complex structure. These projections can be described as $\partial A / \partial s - d _ { A } \Phi$ and $\partial A / \partial t - d _ { A } \Psi$ where $\Phi , \Psi \in \Omega ^ { 0 } ( \mathfrak { g } _ { P } )$ are uniquely determined by the requirement

$$
d _ { A } * _ { s } \left( \frac { \partial A } { \partial s } - d _ { A } \Phi \right) = 0 , \qquad d _ { A } * _ { s } \left( \frac { \partial A } { \partial t } - d _ { A } \Psi \right) = 0 .
$$

Thus our function $u = [ A ] : \mathbb { R } ^ { 2 } \to { \mathcal { M } } ( P )$ satisfies the nonlinear Cauchy-Riemann equations (6) if and only if there exist functions $\Phi , \Psi : \mathsf { R } ^ { 2 } \to \Omega ^ { 0 } ( \mathfrak { g } _ { P } )$ such that

$$
\frac { \partial A } { \partial t } - d _ { A } \Psi + \ast _ { s } \left( \frac { \partial A } { \partial s } - d _ { A } \Phi \right) = 0 .
$$

Moreover,the periodicity condition (7) with $\phi = \phi _ { f }$ is equivalent to

$$
A ( s + 1 , t ) = f ^ { * } A ( s , t ) , \quad \Phi ( s + 1 , t ) = \Phi ( s , t ) \circ f , \quad \Psi ( s + 1 , t ) = \Phi ( s , t ) \circ f .
$$

The limit condition (8) takes the form

$$
\operatorname* { l i m } _ { t \to \pm \infty } A ( s , t ) = A ^ { \pm } ( s ) , \quad \operatorname* { l i m } _ { t \to \pm \infty } \Phi ( s , t ) = \Phi ^ { \pm } ( s ) , \quad \operatorname* { l i m } _ { t \to \pm \infty } \Psi ( s , t ) = 0
$$

where $A ^ { \pm } ( s ) \in { \mathcal { A } } _ { \mathrm { f a t } } ( P )$ and $\dot { A } ^ { \pm } = d _ { A ^ { \pm } } \Phi ^ { \pm }$ . This means that $A ^ { \pm } + \Phi ^ { \pm } d s$ are flat connections on $P _ { f }$ . Strictly speaking,the periodicity conditions (22) need only be satisfied up to even gauge equivalence. However,any such triple $A , \Phi , \Psi$ can be transformed so as to obtain (22). (See the proof of Proposition 4.1.)

If two solutions of (21) and (22) are gauge equivalent by a family of even gauge transformations $g ( s , t ) \in \mathcal { G } _ { 0 } ( P )$ then

$$
g ( s + 1 , t ) = g ( s , t ) \circ f .
$$

This means that $\pmb { g }$ defines a gauge transformation on the bundle $P _ { f } \times \mathsf { R }$ over the 4-manifold $\Sigma _ { h } \times \mathbb { R }$ .Moreover,the action of $\pmb { g }$ on the triple $A , \Phi , \Psi$ corresponds to the interpretation of this triple as a connection $A + \Phi d s + \Psi \cdot$ dt on $P _ { f } \times \mathsf { R }$ . The curvature of this connection is the 2-form

$$
\begin{array} { r c l } { { F _ { A + \Phi d s + \Psi d t } } } & { { = } } & { { F _ { A } - \displaystyle \left( \frac { \partial A } { \partial s } - d _ { A } \Phi \right) \wedge d s - \displaystyle \left( \frac { \partial A } { \partial t } - d _ { A } \Psi \right) \wedge d t } } \\ { { } } & { { } } & { { ~ + \displaystyle \left( \frac { \partial \Psi } { \partial s } - \frac { \partial \Phi } { \partial t } + [ \Phi , \Psi ] \right) d s \wedge d t . } } \end{array}
$$

Hence the connection $A + \Phi d s + \Psi d t$ is self-dual if and only if

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial A } { \partial t } - d _ { A } \Psi + * _ { s } \left( \frac { \partial A } { \partial s } - d _ { A } \Phi \right) } } & { { = } } & { { 0 , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \frac { \partial \Phi } { \partial t } - \frac { \partial \Psi } { \partial s } - [ \Phi , \Psi ] + * _ { s } F _ { A } } } & { { = } } & { { 0 . } } \end{array}
$$

Note that the first equation in (24) agrees with (21) whereas the second equation replaces the condition on $A ( s , t )$ to be fat.

Now the holomorphic curves described by equation (21） with ${ { F } _ { A } } \mathrm { ~ = ~ } 0$ can be viewed as a limit case of the instantons described by equation (24). Following Atiyah [1] we stretch the mapping cylinder $\Sigma _ { h }$ so that the period converges to infinity. Formally this means that equation (22) is replaced by

$$
\begin{array} { r } { \mathrm { l } ( s + 1 / \varepsilon , t ) = f ^ { \ast } A ( s , t ) , \Phi ( s + 1 / \varepsilon , t ) = \Phi ( s , t ) \circ f , \Psi ( s + 1 / \varepsilon , t ) = \Phi ( s , t ) \circ f . } \end{array}
$$

and in (24) $\ast _ { s }$ is replaced by $\ast _ { \epsilon s }$ . Now rescale $A , \Phi$ ,and $\Psi$ ：

$$
A ^ { \varepsilon } ( s , t ) = A ( s / \varepsilon , t / \varepsilon ) , \Phi ^ { \varepsilon } ( s , t ) = 1 / \varepsilon \Phi ( s / \varepsilon , t / \varepsilon ) , \Psi ^ { \varepsilon } ( s , t ) = 1 / \varepsilon \Psi ( s / \varepsilon , t / \varepsilon )
$$

The triple $A ^ { \varepsilon } , \Phi ^ { \varepsilon } , \Psi ^ { \varepsilon }$ then satisfes the periodicity condition (22). Moreover, equation (24) becomes

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial A ^ { \epsilon } } { \partial t } - d _ { A ^ { \epsilon } } \Psi ^ { \epsilon } + * _ { s } \left( \frac { \partial A ^ { \epsilon } } { \partial s } - d _ { A ^ { \epsilon } } \Phi ^ { \epsilon } \right) } } & { { = } } & { { 0 , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \frac { \partial \Phi ^ { \epsilon } } { \partial t } - \frac { \partial \Psi ^ { \epsilon } } { \partial s } - [ \Phi ^ { \epsilon } , \Psi ^ { \epsilon } ] + \frac { 1 } { \varepsilon ^ { 2 } } * _ { s } F _ { A ^ { \epsilon } } } } & { { = } } & { { 0 . } } \end{array}
$$

This is equivalent to conformally rescaling the metric on $\pmb { \Sigma }$ by the factor $\varepsilon ^ { 2 }$

It follows from an implicit function theorem that near every solution of (21),(22) and (23) there is a solution of (25),(22)and (23) provided that $\varepsilon > 0$ is sufficiently small. This is a singular perturbation theorem and care must be taken with the dependence of the linearized operators on $\varepsilon$ Conversely,a family of solutions $A ^ { \varepsilon } , \Phi ^ { \varepsilon } , \Psi ^ { \varepsilon }$ of (25),(22)and (23) converges as $\varepsilon$ tends to O and the curvature of $A ^ { \varepsilon }$ converges to 0. The key point is an energy estimate. The Yang-Mils action of the rescaled equation is given by

$$
\begin{array} { r l } & { \mathcal { V } \mathcal { M } _ { \varepsilon } ( A ^ { \varepsilon } + \Phi ^ { \varepsilon } d s + \Psi ^ { \varepsilon } d t ) } \\ & { \quad = \displaystyle \int _ { - \infty } ^ { \infty } \int _ { 0 } ^ { 1 } \left( \left\| \frac { \partial A ^ { \varepsilon } } { \partial t } - d _ { A ^ { \varepsilon } } \Psi ^ { \varepsilon } \right\| _ { s } ^ { 2 } + \frac { 1 } { \varepsilon ^ { 2 } } \| F _ { A ^ { \varepsilon } } \| _ { s } ^ { 2 } \right) d s d t } \\ & { \quad = \mathcal { C } \mathcal { S } ( A ^ { - } + \Phi ^ { - } d s ) - \mathcal { C } \mathcal { S } ( A ^ { + } + \Phi ^ { + } d s ) . } \end{array}
$$

This shows that the $L ^ { 2 }$ -norm of $\pmb { F _ { A } } \bullet$ on $\Sigma _ { h } \times \mathbb { R }$ converges to 0 as $\varepsilon$ tends to 0. Now Uhlenbeck's compactness theorem requires an $L ^ { \infty }$ -estimate of the form

$$
\operatorname* { s u p } _ { \varepsilon > 0 } \left( \frac { 1 } { \varepsilon ^ { 2 } } \left\| F _ { A ^ { \varepsilon } } \right\| _ { L ^ { \infty } \left( \Sigma _ { h } \times \mathbb { R } \right) } + \left\| \partial A ^ { \varepsilon } / \partial t - d _ { A ^ { \varepsilon } } \Psi ^ { \varepsilon } \right\| _ { L ^ { \infty } \left( \Sigma _ { h } \times \mathbb { R } \right) } \right) < \infty .
$$

The proof of this estimate involves a bubbling argument. Roughly speaking,the estimate (27) may be violated in arbitrarily small neighborhoods of finitely many points and in this case either instantons on $S ^ { 4 }$ or instantons on $\Sigma \times \mathbf { C }$ or holomorphic spheres in $M ( P )$ will split off.But this can be avoided in the case which is relevant for the construction of the Floer homology groups namely when the relative Morse index is 1:

$$
\mu ( A ^ { - } + \Phi ^ { - } d s ) - \mu ( A ^ { + } + \Phi ^ { + } d s ) = 1 .
$$

Now there are two such relative Morse indices; one in the Chern-Simons theory given by the spectral flow of the operator family $D _ { { \mathsf { a } } ( t ) }$ (section 2) and one in symplectic Floer homology given by the Maslov index (section 3). We must prove that both relative Morse indices agree. We shall address this problem as well as singular perturbation and compactness in a separate paper.

# 7Perturbations

The methods we have discussed so far require the assumption that all flat connections on the bundle $Q = P _ { f }$ respectively all fixed points of the symplectomorphism $\phi _ { f }$ on $M ( P )$ are nondegenerate. The purpose of this section is to show why this assumption is redundant.In particular we wish to apply Theorem 1.1 to $f = \mathrm { i d }$ in which case all flat connections are degenerate. Nevertheless we obtain the following

Theorem 7.1 The instanton homology of the bundle $P \times S ^ { 1 }$ over $\Sigma \times S ^ { 1 }$ is naturally isomorphic to the homology of the moduli space $M _ { F } ( P )$

$$
H F _ { k } ^ { \mathrm { i n s t } } ( \Sigma \times S ^ { 1 } , P \times S ^ { 1 } ) = \bigoplus _ { j = k ( \mathrm { m o d ~ 4 } ) } H _ { j } ( \mathcal { M } ( P ) ; \mathbf { Z } _ { 2 } ) .
$$

To construct the symplectic Floer homology groups in the degenerate case we must perturb the nonlinear Cauchy-Riemann equations (6) by a Hamiltonian term as in the proof of Theorem 3.3. Likewise we must consider perturbations of the Chern-Simons functional on the space of connections on $P _ { f }$ as in [11] and [27] to construct the instanton homology groups of section 2.

We shall construct a smooth family of Hamiltonian functions $H _ { s } : { \mathcal { A } } ( P ) \to$ R which satisfy

$$
H _ { s } ( g ^ { * } A ) = H _ { s } ( A ) = H _ { s + 1 } ( f ^ { * } A )
$$

for $A \in { \mathcal { A } } ( P )$ and ${ \mathfrak { g } } \in { \mathcal { G } } _ { 0 } ( P )$ . The differential of $H _ { s }$ can be represented by a smooth map $X _ { s } : \mathcal { A } ( P ) \to \Omega ^ { 1 } ( \mathfrak { g } _ { P } )$ such that

$$
d H _ { s } ( A ) \alpha = \int _ { \Sigma } \langle X _ { s } ( A ) \wedge \alpha \rangle .
$$

In other words $X _ { s } : \mathcal { A } ( P ) \to \Omega ^ { 1 } ( \mathfrak { g } _ { P } )$ is the Hamiltonian vector field on $\pmb { A } ( P )$ corresponding to the Hamiltonian function $H _ { s }$ . Since $H _ { s }$ is invariant under $\mathcal { G } _ { \bf 0 } ( P )$ the vector fields $X _ { s }$ satisfy

$$
X _ { s } ( g ^ { * } A ) = g ^ { - 1 } X _ { s } ( A ) g , \qquad d _ { A } X _ { s } ( A ) = 0 , \qquad X _ { s + 1 } ( f ^ { * } A ) = f ^ { * } X _ { s } ( A )
$$

for $\mathfrak { g } \in \mathcal { G } _ { 0 } ( P )$ and $A \in { \mathcal { A } } ( P )$ .The vector fields $X _ { s }$ that arise from the holonomy will be smooth with respect to the $W ^ { k , p }$ -norm for all $\pmb { k }$ and $\pmb { p }$ and hence give rise to a Hamiltonian fow $\psi _ { s } : \mathcal { A } ( P )  \mathcal { A } ( P )$ defined by

$$
\frac { d } { d s } \psi _ { s } = X _ { s } \circ \psi _ { s } , \qquad \psi _ { 0 } = \mathrm { i d } .
$$

The diffeomorphisms $\psi _ { s }$ preserve the symplectic structure and are equivariant under the action of ${ \mathcal { G } } _ { 0 } ( P )$

$$
\psi _ { s } ( g ^ { * } A ) = g ^ { * } \psi _ { s } ( A ) , \qquad F _ { \psi _ { s } ( A ) } = F _ { A } .
$$

Moreover,

$$
\psi _ { s + 1 } \circ \psi _ { 1 } { } ^ { - 1 } ( f ^ { * } A ) = f ^ { * } \psi _ { s } ( A )
$$

for $A \in { \mathcal { A } } ( P )$ .The restriction of this identity to the Marsden-Weinstein quotient $M ( P )$ can be written in the form

$$
\psi _ { s + 1 } \circ \phi _ { f , H } = \phi _ { f } \circ \psi _ { s } , \qquad \phi _ { f , H } = \psi _ { 1 } ^ { \scriptscriptstyle - 1 } \circ \phi _ { f } .
$$

The symplectomorphism $\phi _ { f , H } : \mathcal { M } ( P )  \mathcal { M } ( P ) $ is related to $\phi _ { f }$ by a Hamiltonian isotopy.

To construct the Hamiltonian functions $H _ { s }$ and the Hamiltonian vector fields $X _ { s }$ we first recall some basic facts about the holonomy of a connection on $P$ . For any loop $\gamma ( \theta + 1 ) = \gamma ( \theta ) \in P$ the holonomy determines a map $\rho = \rho _ { \gamma } : \mathcal { A } ( P )  \operatorname { S U } ( 2 )$ defined by $\rho ( A ) = g ( 1 )$ where $g ( \pmb \theta ) \in \mathrm { S U } ( 2 )$ is the unique solution of the ordinary differential equation

$$
\dot { g } + A ( \dot { \gamma } ) g = 0 , \qquad g ( 0 ) = 1 .
$$

This equation is meaningful since the Lie algebra of SO(3) agrees with the Lie algebra of SU(2). The differential of $\pmb { \rho }$ can be expressed in terms of $\pmb { g }$ ：

$$
\rho ( A ) ^ { - 1 } d \rho ( A ) \alpha = - \int _ { 0 } ^ { 1 } g ^ { - 1 } \alpha ( \dot { \gamma } ) g d \theta
$$

for $\alpha \in \Omega ^ { 1 } ( { \mathfrak { g } } _ { P } )$

Now choose $2 k$ embeddings $\gamma _ { j } : \mathbb { R } / \mathbb { Z } \times \mathbb { R }  P$ of the annulus such that the projections $\pi \circ \gamma _ { j }$ are orientation preserving, generate the fundamental group of $\pmb { \Sigma }$ ,and satisfy $\gamma _ { j } ( 0 , \lambda ) = p _ { \lambda }$ for every $j$ Denote by $\rho _ { \lambda } : { \mathcal { A } } ( P ) \to { \mathrm { S U } } ( 2 ) ^ { 2 k }$ the holonomy along the loops $\theta \mapsto \gamma _ { j } ( \theta , \lambda )$ for $\lambda \in \mathbb { R }$ Now choose a smooth family of functions $h _ { s } : \mathrm { S U } ( 2 ) ^ { 2 k } \to \mathsf { R }$ which are invariant under conjugacy and vanishes for $\pmb { \mathscr { s } }$ near O and 1. Let $\beta : \mathbb { R }  \mathbb { R }$ be a smooth cutoff function supported in $[ - 1 , 1 ]$ with mean value 1 and define $H _ { s } : { \mathcal { A } } ( P ) \to { \mathbb { R } }$ by

$$
H _ { s } ( A ) = \int _ { - 1 } ^ { 1 } \beta ( \lambda ) h _ { s } ( \rho _ { \lambda } ( A ) ) d \lambda
$$

for $A \in { \mathcal { A } } ( P )$ and $0 \leq s \leq 1$

The partial derivative of $h _ { s }$ with respect to $U _ { j }$ can be represented by a function $\eta _ { j } : [ 0 , 1 ] \times \mathrm { S U } ( 2 ) ^ { 2 k } \to \mathfrak { s u } ( 2 )$ such that

$$
\frac { \partial h _ { s } } { \partial U _ { j } } ( U ) U _ { j } \xi = \langle \eta _ { j } ( s , U ) , \xi \rangle .
$$

Define $X _ { s } : \mathcal { A } ( P ) \to \Omega ^ { 1 } ( \mathfrak { g } _ { P } )$ by

$$
X _ { s } ( A ) = \sum _ { j = 1 } ^ { 2 k } X _ { j } ( s , A )
$$

for ${ \mathfrak { d } } \leq s \leq 1$ where $X _ { j } ( s , A ) \in \Omega ^ { 1 } ( \mathfrak { g } _ { P } )$ is supported in $\gamma _ { j } ( S ^ { 1 } \times [ - 1 , 1 ] )$ and

$$
\gamma _ { j } ^ { \ast } X _ { j } ( s , A ) = \beta g _ { j } \eta _ { j } ( s , \rho _ { \lambda } ( A ) ) { g _ { j } } ^ { - 1 } d \lambda .
$$

Here ${ \pmb \theta } \mapsto { \pmb g } _ { j } ( { \pmb \theta } , { \pmb \lambda } )$ is the holonomy of $\pmb { A }$ along the loop $\theta \mapsto \gamma _ { j } ( \theta , \lambda )$ The vector field $X _ { s }$ is related to the Hamiltonian $H _ { s }$ as above for $0 \leq s \leq 1$ .Both can be extended to ${ \pmb s } \in { \pmb R }$ by (28)and (29).

Remark 7.2 Any smooth Hamiltonian function $H _ { s } : \mathcal { M } ( P ) \to \mathbb { R }$ can be represented in the form $H _ { s } = h _ { s } \circ \rho _ { \lambda } : { \mathcal { A } } _ { \mathrm { H a t } } ( P ) \to \mathbb { R }$ where $h _ { s } : \mathrm { S U } ( 2 ) ^ { 2 k } \to \mathsf { R }$ is invariant under conjugacy. The functions $h _ { s } : \mathrm { S U } ( 2 ) ^ { 2 k } \to \mathsf { R }$ can be chosen such that $\phi _ { f , H }$ has only nondegenerate fixed points. We do not assume here that $H _ { s }$ is invariant under the action of $\Gamma _ { f }$ . This would require a transver-sality theorem which takes account of the action of a finite group.

The perturbed Chern-Simons functional $\mathcal { C S } _ { H } : \mathcal { A } ( P _ { f } )  \mathbb { R }$ is defined by

$$
\mathcal { C S } _ { H } ( a ) = \mathcal { C S } ( a ) - \int _ { 0 } ^ { 1 } H _ { s } ( A ( s ) ) d s .
$$

for $a = A + \Phi d s \in A ( P _ { f } )$ . Its diferential is given by

$$
d \mathcal { C S } _ { H } ( A + \Phi d s ) ( \alpha + \phi d s ) = \int _ { 0 } ^ { 1 } \int _ { \Sigma } \left( \langle ( \dot { A } - d _ { A } \Phi - X _ { s } ( A ) ) \wedge \alpha \rangle + \langle F _ { A } \wedge \phi \rangle \right) d s
$$

Hence a connection $A + \Phi d s$ on $P _ { f }$ is a critical point of $\mathcal { C } \mathcal { S } _ { H }$ if and only if $A ( s )$ is flat for every $\pmb { \mathscr { s } }$ and

$$
\dot { A } - d _ { A } \Phi - X _ { s } ( A ) = 0 .
$$

Now the restriction of $H _ { s }$ to the moduli space $M ( P )$ of flat connections is in the class of perturbations for symplectic Floer homology considered in the proof of Theorem 3.3. In other words the restriction of $\mathcal { C } \mathcal { S } _ { H }$ to the space of paths $\Omega _ { \phi _ { f } } = \mathcal { A } _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { \Sigma } ( P _ { f } )$ is the perturbed symplectic action functional and this restriction has the same critical points as $\mathcal { C } \mathcal { S } _ { H }$ . They are in one-to-one correspondence with the fixed points of the symplectomorphism $\phi _ { f , H }$ The class of perturbations discussed here is large enough in order to obtain nondegenerate critical points.

# A Proof of Lemma 2.3

Let $Q  M$ be a principal $S O ( 3 )$ -bundle over a compact 3-manifold.Here we denote the unit interval by $I = [ 0 , 1 ]$

Lemma A.l For every integer $\pmb { k } \in \mathbb { Z }$ there exists a gauge transformation ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$ with $\deg ( g ) = 2 k$ and $\pmb { \eta } ( \pmb { g } ) = \mathbf { 0 }$

Proof: The condition $\eta ( g ) = 0$ means that $g : Q  G$ lifts to a map ${ \tilde { \pmb { g } } } : { \boldsymbol { Q } }  S U ( 2 )$ .Let $\iota : \Sigma \to M$ be an embedding of an oriented Riemann surface. Then $\pmb { \iota }$ extends to an embedding of a tubular neighborhood t : $\Sigma \times I  M$ . Cut out a disc $D \subset \Sigma$ and define $\tilde { \pmb g } = 1$ outside $\iota ( D \times I )$ . Now trivialize $Q$ over $\iota ( D \times I )$ and choose $\tilde { g } \circ \iota : D \times I  S U ( 2 )$ of degree $\pmb { k }$ with $\tilde { g } \circ \iota ( \partial ( D \times I ) ) = 1$ □

Lemma A.2 Let $\iota : \Sigma \to M$ be an embedding of an oriented Riemann surface with $w _ { 2 } ( \iota ^ { * } Q ) = j \in \{ 0 , 1 \}$ . Then there exists a gauge transformation $g : Q  S O ( 3 )$ of degree $j$ whose parity

$$
\eta ( g ) = \eta _ { \Sigma } : \pi _ { 1 } ( M ) \to { \mathbf Z } _ { 2 }
$$

is given by the intersection number of a loop with $\pmb { \Sigma }$

Proof: Extend $\pmb { \iota }$ to an embedding of a tubular neighborhood $\iota : \Sigma \times I  M$ If ${ w _ { 2 } ( \iota ^ { * } Q ) = 0 }$ define $g \circ \iota ( z , t ) = g _ { 0 } ( t )$ for $z \in \Sigma$ and $t \in I$ where $g _ { 0 } ( t )$ is a nontrivial loop in $S O ( 3 )$ with $g _ { 0 } ( 0 ) = g _ { 0 } ( 1 ) = 1$ . Extend by $g ( p ) = 1$ outside $\iota ( \Sigma \times I )$

$w _ { 2 } ( \iota ^ { * } Q ) = 1$ define $g ( p ) = 1$ for $p \notin \iota ( \Sigma \times I )$ as above. Moreover decompose $\pmb { \Sigma }$ as

$$
\Sigma = \Sigma _ { 1 } \cup \Sigma _ { 2 }
$$

where $\Sigma _ { 1 } = D \subset \Sigma$ is a disc and $\Sigma _ { 2 } = { \bf c l } ( \Sigma \setminus D )$ . Choose sections $\sigma _ { j }$ ： $\Sigma _ { j } \times I \to Q | _ { \iota ( \Sigma _ { j } \times I ) }$ for $j = 1 , 2$ such that

$$
\sigma _ { 2 } ( e ^ { 2 \pi i \theta } ) = \sigma _ { 1 } ( e ^ { 2 \pi i \theta } ) g _ { 0 } ( \theta ) .
$$

Here $g _ { 0 } ( \theta )$ is the loop in $S O ( 3 )$ covered by

$$
\gamma ( \theta ) = \left( \begin{array} { c c } { { e ^ { \pi i \theta } } } & { { 0 } } \\ { { 0 } } & { { e ^ { - \pi i \theta } } } \end{array} \right) \in \mathrm { S U } ( 2 ) .
$$

Define $\pmb { g }$ on $\iota ( \Sigma \times I )$ by

$$
g \circ \sigma _ { j } ( z , t ) = g _ { 0 } ( t ) , \qquad z \in \Sigma _ { j } , \quad t \in I .
$$

This is consistent with the patching condition since $g _ { 0 } ( \theta ) g _ { 0 } ( t ) g _ { 0 } ( \theta ) ^ { - 1 } = g _ { 0 } ( t )$

We prove that $h = g \cdot g$ lifts to $\tilde { h } : Q  S U ( 2 )$ and that $\tilde { h }$ is of degree 1. To see this note that

$$
\tilde { h } \circ \sigma _ { j } ( z , t ) = \gamma ( 2 t ) , \qquad z \in \Sigma _ { j } , \quad t \in I ,
$$

and $\tilde { h } ( p ) = 1$ for $p \notin \iota ( \Sigma \times I )$ . Now choose a continuous function

$$
\beta ( r , t ) = \left( \begin{array} { c c } { { a + i b } } & { { c } } \\ { { - c } } & { { a - i b } } \end{array} \right) \in \mathrm { S U } ( 2 ) , \qquad 0 \leq t \leq 1 \leq r \leq 2 .
$$

such that $\beta ( 1 , t ) = \gamma ( 2 t ) , \beta ( r , 0 ) = \beta ( r , 1 ) = \beta ( 2 , t ) = 1 , a ^ { 2 } + b ^ { 2 }$ $a ^ { 2 } + b ^ { 2 } + c ^ { 2 } = 1$ and $c \geq 0$ . (Contract the equator over a hemisphere.） Moreover,assume that $\sigma _ { 1 } : D \times I  Q$ extends to the disc $D _ { 2 }$ of radius 2 with the overlap condition $\sigma _ { 2 } ( r e ^ { 2 \pi i t } ) = \sigma _ { 1 } ( r e ^ { 2 \pi i t } ) g _ { 0 } ( t )$ for $1 \leq r \leq 2$ . Also assume,up to homotopy, that $\tilde { h } \circ \sigma _ { 2 } ( z , t ) = 1$ for $z \notin D _ { 2 }$ and

$$
\tilde { h } \circ \sigma _ { 2 } ( z , t ) = \beta ( | z | , t ) , 1 \leq | z | \leq 2 , t \in I .
$$

By the overlap condition this implies

$$
\tilde { h } \circ \sigma _ { 1 } ( z , t ) = \gamma ( \theta ) \beta ( r , t ) \gamma ( \theta ) ^ { - 1 } = \left( \begin{array} { c c } { a + i b } & { c e ^ { 2 \pi i \theta } } \\ { - c e ^ { - 2 \pi i \theta } } & { a - i b } \end{array} \right)
$$

for $1 \leq | z | \leq 2$ and $t \in I$ ．Hence it follows from the definition of $\beta$ that $\tilde { h } \circ \sigma _ { 1 } ( z , t ) = 1$ whenever $| z | = 2$ or ${ \boldsymbol { t } } = \mathbf { 0 } , \mathbf { 1 }$ . Thus $\tilde { h } \circ \sigma _ { 1 }$ defined a map from $D _ { 2 } \times I / \partial ( D _ { 2 } \times I )  \mathrm { S U ( 2 ) }$ . Since $\pmb { c } \geq \mathbf { 0 }$ ,this map is of degree 1. □

Lemma A.3 If ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$ with $\deg ( g ) = 0$ and $\pmb { \eta } ( \pmb { g } ) = \mathbf { 0 }$ then $\pmb { g }$ is homotopic to 1.

Proof: If $\pmb { \eta } ( \pmb { g } ) = \mathbf { 0 }$ then $\pmb { g }$ lifts to $S U ( 2 ) = S ^ { 3 }$ . Hence the statement follows from the Hopf degree theorem.

Proof of Lemma 2.3: Statement (1) follows immediately from Lemma A.3.

We prove statement (2).By (H1) every cohomology class $\eta : \pi _ { 1 } ( M ) \to \mathbb { Z } _ { 2 }$ can be represented by finitely many embedded oriented Riemann surfaces $\iota _ { j } : \Sigma _ { j } \to M$ . The associated gauge transformations $g _ { j } : Q \to G$ constructed in Lemma A.2 all satisfy (1). This together with Lemma A.1 implies that for every ${ \pmb k } \in { \pmb Z }$ and every $\eta \in H ^ { 1 } ( M ; \mathbf { Z } _ { 2 } )$ with $\pmb { k } \equiv w _ { 2 } ( Q ) \cdot \pmb { \eta }$ (mod 2) there exists a gauge transformation ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$ such that $\deg ( g ) = k$ and $\eta ( g ) = \eta$

Conversely, we must prove that every gauge transformation $g \in { \mathcal { G } } ( Q )$ satisfies (1). By Lemma A.2 we may assume that $\eta ( g ) = 0$ . This implies that $\pmb { g }$ lifts to a map $\tilde { \pmb { g } } : \pmb { Q }  S U ( 2 )$ and hence $\deg ( g )$ is even.

We prove statement (3). By (H2) there exists an embedding $\iota : \Sigma \to M$ of an oriented Riemann surface such that $w _ { 2 } ( \iota ^ { * } Q ) = 1$ . So it follows from Lemma A.2 that there is a gauge transformation of degree 1. □

# References

[1] M.F. Atiyah, New invariants of three and four dimensional manifolds, Proc. Symp. Pure Math.48 (1988).

[2] M.F.Atiyah and R.Bott,The Yang Mills equations over Riemann surfaces,Phil. Trans.R. Soc. Lond. A 308 (1982),523-615.

[3] M.F. Atiyah, V.K. Patodi and I.M. Singer,Spectral asymmetry and Riemannian geometry III, Math. Proc. Camb. Phil. Soc.79 (1976),71- 99.

[4] S.E. Cappell, R. Lee and E.Y. Miller, Self-adjoint eliptic operators and manifold decomposition I: general techniques and applications to Casson's invariant,Preprint,1990.

[5] C.C. Conley and E. Zehnder,Morse-type index theory for flows and periodic solutions of Hamiltonian equations, Commun. Pure Appl. Math. 37 (1984), 207-253.

[6] G.D.Daskalopoulos and K.K. Uhlenbeck,An application of transver-sality to the topology of the moduli space of stable bundles,Preprint, 1990.

[7] S.Dostoglou and D.A. Salamon， Cauchy-Riemann operators,selfduality,and the spectral flow,Preprint,1992.

[8] S.Donaldson,M. Furuta and D. Kotschick, Floer homology groups in Yang-Mills theory, in preparation.

[9] A.Floer, Morse theory for Lagrangian intersections, J. Diff. Geom. 28 (1988), 513-547.

[10] A.Floer, A relative Morse index for the symplectic action, Commun. Pure Appl. Math.41(1988),393-407.

[11] A. Floer,An instanton invariant for 3-manifolds, Commun. Math. Phys. 118 (1988),215-240.

[12] A. Floer, Symplectic fixed points and holomorphic spheres, Commun. Math.Phys.120 (1989),575-611.

'13] A. Floer, Instanton homology and Dehn surgery,Preprint 1991.

[14] A.Floer,Instanton homology for knots,Preprint 1991.

[15] A.Floer and H. Hofer, Coherent orientations for periodic orbit problems in symplectic geometry, Preprint,Ruhr-Universität Bochum,1990.

[16] M.Gromov,Pseudoholomorphic curves in symplectic manifolds, Invent. Math.82 (1985),307-347.

[17] H. Hofer and D.A. Salamon，Floer homology and Novikov rings, Preprint, 1991.

[18] J. Jones,J. Rawnsley and D. Salamon, Instanton homology and Donaldson polynomials,Preprint,1991.   
[19] T. Kato, Perturbation Theory for Linear Operators Springer-Verlag, 1976.   
[20] D. McDuff, Elliptic methods in symplectic geometry, Bull. A.M.AS. 23 (1990),311-358.   
[21] P.E. Newsteadt, Topological properties of some spaces of stable bundles, Topology 6 (1967),241-262.   
[22] T.R. Ramadas, I.M. Singer and J. Weitsman, Some comments on Chern-Simons gauge theory Commun. Math. Phys. 126 (1989),421-431.   
[23] J. Sacks and K.Uhlenbeck,The existence of minimal immersions of 2-spheres, Annals of Math. 113 (1981), 1-24.   
[24] D. Salamon,Morse theory, the Conley index and Floer homology, Bull. L.M.S.22 (1990),113-140.   
[25] D. Salamon and E. Zehnder,Floer homology,the Maslov index and periodic orbits of Hamiltonian equations,‘Analysis et cetera', edited by P.H. Rabinowitz and E. Zehnder, Academic Press,1990, pp. 573-600.   
[26] S.Smale,An infinite dimensional version of Sard's theorem，Am.J. Math.87 (1973),213-221.   
[27] C.H. Taubes, Casson's invariant and gauge theory, J. Diff. Geom. 31 (1990), 547-599.   
[28] K.Uhlenbeck,Connections with $L ^ { p }$ bounds on curvature Commun. Math. Phys.83 (1982),31-42.   
[29] C. Viterbo, Intersections de sous-varietés Lagrangiennes, fonctionelles d'action et indice des systemes Hamiltoniens, Bull Soc. Math. France 115 (1987), 361-390.   
[30] E. Witten,Supersymmetry and Morse theory, J. Diff. Geom. I7 (1982), 661-692.   
[31] J.G. Wolfson, Gromov's compactness of pseudoholomorphic curves and symplectic geometry, J. Diff. Geom. 23(1988),383-405.   
[32] T. Yoshida,Floer homology and splitings of manifolds,Ann.of Math. 134 (1991), 277-323.

# An Energy-Capacity Inequality for the Symplectic Holonomy of Hypersurfaces Flat at Infinity

Y.Eliashberg\*and H.Hofert   
Department of Mathematics\*   
Stanford University   
California, 94305, USA   
and   
Institut fir Mathematikt   
Ruhr-Universität Bochum   
4630 Bochum, Germany

March 12,1993

# Contents

1 Introduction 95

2 Functional Analysis of the Action Integral 98

3 A Weak $P S \cdot$ -Condition for a Class of Functionals 10:

4 Some Estimates for Max-Min-Levels 106

5 Proof of the Main Result 109

# 1Introduction

The main purpose of this paper is the energy-capacity inequality for a special class of so-called flat at infinity hypersurfaces. The need for such an inequal-ity, which generalizes some results from [7] and [12],appeared in our study of

boundaries of symplectic manifolds (see [2]).The Corollary 1.4 of Theorem 1.2 plays the crucial role in [4].

Consider $\mathbf { c } ^ { n + 1 } = \mathbf { c } ^ { n } \oplus \mathbf { c }$ as a real vector space. We denote by $( * , * )$ the standard-C-valued Hermitian inner product and by $\omega = - \operatorname { I m } ( * , * )$ the associated symplectic form.

A flat at infinity hypersurface (abbreviated FIH in the following) $\pmb { \Sigma }$ in $\mathbb { C } ^ { n + 1 }$ is a hypersurface $\pmb { \Sigma }$ diffeomorphic to $\mathbb { R } ^ { 2 n + 1 }$ such that there exists a compact subset $\pmb { K }$ of $\mathbf { C } ^ { n + 1 }$ with

$$
\Sigma \setminus K = ( { \mathbb C } ^ { n } \oplus { \mathbb R } ) \setminus K .
$$

We denote by $\pmb { \mathcal { D } }$ the group of compactly supported symplectic diffeomorphisms in $\mathbb { C } ^ { n + 1 }$ . We define the energy $e ( \Sigma )$ of an asymptotically flat hypersurface as follows

$$
e ( \Sigma ) = \operatorname* { i n f } \left\{ 2 a ( c ^ { + } - c ^ { - } ) \mid a , c ^ { + } { \mathrm { ~ a n d ~ } } c ^ { - } { \mathrm { ~ s a t i s f y ~ } } ( 1 ) \right\}
$$

where

$$
\Psi ( \Sigma ) \subset ( \mathbb { C } ^ { n } \oplus \mathbb { R } ) \cup ( \mathbb { C } ^ { n } \oplus ( - a , a ) \oplus i ( c ^ { - } , c ^ { + } ) ) ~ .
$$

The energy is a very rough quantity measuring the $C ^ { \pmb { 0 } }$ -size of $\pmb { \Sigma }$ compared with $\mathbf { C } ^ { n } \oplus \mathbf { R }$ Surprisingly, $e ( \Sigma )$ also measures some $C ^ { 1 }$ -properties of $\pmb { \Sigma }$ .The goal of this paper will be to show this.

We define a line bundle $\mathcal { L } _ { \Sigma } \longrightarrow \Sigma$ over $\pmb { \Sigma }$ ，where the fibre over $z \in \Sigma$ consists of all $\xi \in T _ { z } \Sigma$ such that

$$
\omega ( \xi , \eta ) = 0 \quad \mathrm { f o r \ a l l } \quad \eta \in T _ { z } \Sigma \ .
$$

The one-dimensional distribution $\pmb { \mathcal { L } } _ { \Sigma }$ defines a foliation on $\pmb { \Sigma }$ .The leaf through some point $z \in \Sigma$ will be denoted by $L _ { \Sigma } ( z )$

In order to introduce the holonomy associated to $\pmb { \Sigma }$ , pick a number ${ \pmb a } > { \bf 0 }$ (which is supposed to be large enough) and define

$$
H _ { a } ^ { \pm } = \left\{ z \in \mathbb { C } ^ { n + 1 } \mid z _ { n + 1 } \in ( \pm a ) + i \mathbb { R } \right\} \mathrm { ~ . ~ }
$$

For all large ${ \pmb a } > { \bf 0 }$ we readily see that the leaves of the foliation are transversal to $H _ { \mathbf { a } } ^ { - }$ and $H _ { a } ^ { + }$ .For $z \in \Sigma \cap H _ { a } ^ { - } = ( \mathbb { C } ^ { n } \oplus \mathbb { R } ) \cap H _ { a } ^ { - }$ we consider $L _ { \Sigma } ( a ) \cap H _ { a } ^ { + }$ . We denote the collection of all points in $H _ { \mathfrak { a } } ^ { - } \cap \Sigma$ with $L _ { \Sigma } ( z ) \cap H _ { a } ^ { + } \neq \emptyset$ by $U _ { \Sigma }$ If ${ \pmb a } > { \pmb 0 }$ is large enough the latter intersection will consist of precisely one point denoted by $\varphi _ { \Sigma } ( z )$ . With the obvious identification we have $U _ { \Sigma } \subset \mathbf { C } ^ { n }$ and consider $\varphi _ { \Sigma }$ as a map from $U _ { \Sigma }$ into $\mathbf { C } ^ { n }$ .One easily verifies that $U _ { \Sigma }$ is open and dense and $\varphi _ { \Sigma }$ is the identity outside of a compact set. We call $\varphi _ { \Sigma }$ the holonomy of $\pmb { \Sigma }$ and note that $\varphi _ { \Sigma }$ is a symplectic map.

Next let us recal the definition of a symplectic capacity as given in [9] (see [2,3,6,10,11] for more information)．We adapt the definition to our special situation. Denote by $\varkappa$ the collection of all smooth Hamiltonians $H : \mathbb { C } ^ { n } \longrightarrow [ 0 , + \infty )$ satisfying:

There exists a number $m ( H ) > 0$ such that $0 \leq H \leq m ( H )$ Moreover $m ( H ) - H$ has compact support and there exists an open nonempty set $U$ with $H | U \equiv \mathbf { 0 }$ ：

Given $H \in \mathcal { H }$ we consider the Hamiltonian system

$$
{ \dot { x } } = X _ { H } ( x )
$$

and study its $\pmb { T }$ -periodic solutions with $0 < T \leq 1$ . We call $H$ admissible and write $H \in \mathcal { H } _ { a d }$ provided every $\pmb { T }$ -periodic solution of (5) with $\pmb { T } \in ( \mathbf { 0 } , 1 ]$ is constant.It is an easy exercise to show that $\mathcal { H } _ { a d }$ is nonempty. Given a nonempty domain $W \subset \mathbf { C } ^ { n }$ we denote by ${ \mathcal { H } } _ { a d } ( W )$ the subset of $\mathcal { H } _ { a d }$ consisting of all $H \in \mathcal { H } _ { a d }$ with : $\mathsf { s u p p } ( m ( H ) - H ) \subset W$ . Again $\mathcal { H } _ { a d } ( W ) \neq \emptyset$ . Finally, we define the following [9]:

$$
c ( W ) = \operatorname* { s u p } \{ m ( H ) \mid H \in { \mathcal { H } } _ { a d } ( W ) \} \ .
$$

It has been proved in [9] that

Proposition 1.1 The number $c ( W ) \in ( 0 , + \infty ]$ satisfies

$$
c ( B ^ { 2 n } ( 1 ) ) = c ( B ^ { 2 } ( 1 ) \times \mathbb { C } ^ { n - 1 } ) = \pi .
$$

(ii）If $\Psi : W \hookrightarrow V$ is an embedding satisfying $\Psi ^ { * } \omega = \alpha \omega$ for some ${ \pmb { \alpha } } \neq { \pmb { 0 } }$ ， then $c ( V ) \geq | \alpha | ~ c ( W )$

$c ( W )$ is called the (symplectic) capacity of $W$ . For more information see [2,3,7,6,9,12]. Our main result is the following:

Theorem 1.2 Let $\pmb { \Sigma }$ be an asymptotically flat hypersurface in $\mathbf { C } ^ { n + 1 }$ with holonomy $\varphi _ { \Sigma } : U _ { \Sigma } \longrightarrow { \mathbb c } ^ { n }$ and energy $e ( \Sigma )$ . Then for every open domain $\Omega \subset \mathbf { C } ^ { n }$ with ${ \overline { { \Omega } } } \subset U _ { \Sigma }$ and capacity $\pmb { c } ( \Omega )$ satisfying

$$
c ( \Omega ) > e ( \Sigma ) \ ,
$$

we have

$$
\varphi _ { \Sigma } ( \overline { { \Omega } } ) \cap \overline { { \Omega } } \neq \emptyset \ .
$$

Our first corollary is

Corollary 1.3 For every asymptotically flat hypersurface $\pmb { \Sigma }$ we have the inequality

$$
\operatorname* { i n f } \{ \alpha > 0 \quad | \quad F o r \ a l l \ d o m a i n s \Omega \subset \mathbb { C } ^ { n }
$$

We call the above inequality the energy-capacity inequality. Further, Theo rem 1.2 implies

Corollary 1.4 Suppose $\left( \Sigma _ { k } \right)$ is a sequence of asymptotically flat hypersurfaces such that $e ( \Sigma _ { k } ) \longrightarrow 0$ . Assume there exists an open dense set $U \subset \mathbb { C } ^ { n }$ such that $U _ { \Sigma _ { k } } \supset U$ for every $\pmb { k } \in \mathbb { N }$ ,and $\varphi _ { \Sigma _ { k } }$ converges in the compact open topology to some continuous map $\varphi : U \longrightarrow \mathbb { C } ^ { n }$ . Then $\varphi = \operatorname { I d } _ { U }$

The main result of this paper will be important in [4],where we study the question to which extent the symplectic topology of the interior of a domain determines the symplectic properties of the boundary.

The present paper,in particular Corollary 1.4 is strongly related to results in [7] and [12],where an affirmative answer is given to a conjecture of the first author.

The present set up, however, is much more general.

# 2Functional Analysis of the Action Integral

We define an unbounded selfadjoint operator $\pmb { L }$ with domain $D ( L )$ in $L ^ { 2 } ( 0 , 2 ; \mathbf { C } ^ { n + 1 } )$ by

$$
{ \begin{array} { r l } { D ( L ) = \left\{ } & { z \in H ^ { 1 , 2 } ( 0 , 2 ; \mathbf { C } ^ { n + 1 } ) \mid z _ { k } ( 0 ) = z _ { k } ( 2 ) { \mathrm { ~ f o r } } \right. } \\ & { k = 1 , \ldots , n { \mathrm { ~ a n d ~ } } \mathrm { R e } z _ { n + 1 } ( 0 ) = \mathrm { R e } z _ { n + 1 } ( 2 ) = 0 \} } \end{array} }
$$

and

$$
L z = - i \dot { z } : = - i \frac { d } { d t } z \ .
$$

The splitting $L ^ { 2 } ( 0 , 2 ; { \mathbb { C } } ^ { n + 1 } ) = L ^ { 2 } ( 0 , 2 ; { \mathbb { C } } ^ { n } ) \oplus L ^ { 2 } ( 0 , 2 ; { \mathbb { C } } )$ gives a splitting $L =$ $L _ { 1 } \oplus L _ { 2 }$ with

$$
\begin{array} { l l l } { { { \cal D } ( L _ { 1 } ) } } & { { = } } & { { \{ z \in { \cal H } ^ { 1 , 2 } ( 0 , 2 ; { \bf C } ^ { n } ) \mid z ( 0 ) = z ( 2 ) \} } } \\ { { { \cal D } ( L _ { 2 } ) } } & { { = } } & { { \{ z \in { \cal H } ^ { 1 , 2 } ( 0 , 2 ; { \bf C } ) \mid \mathrm { R e } z ( 0 ) = \mathrm { R e } z ( 1 ) = 0 \} \ . } } \end{array}
$$

We have for the spectrum of $L _ { 1 }$ and $\scriptstyle { L _ { 2 } }$

$$
\begin{array} { l l l } { { \sigma ( L _ { 1 } ) } } & { { = } } & { { \pi { \mathbf Z } } } \\ { { \sigma ( L _ { 2 } ) } } & { { = } } & { { { \frac { \pi } { 2 } } { \mathbf Z } \ , } } \end{array}
$$

where every element of $\sigma ( L _ { j } )$ is an eigenvalue of multiplicity ${ \bf 2 \it { n } }$ if $j = 1$ and multiplicity 1 if $j = 2$ . If we write $\boldsymbol z = ( x , y )$ according to our splitting we have a Fourier expansion

$$
\begin{array} { r } { x = \sum _ { k \in \pmb { \mathbb { Z } } } x ^ { ( k ) } e ^ { \pi i k t } \quad , \quad x ^ { ( k ) } \in \pmb { \mathbb { C } } ^ { n } } \\ { y = \sum _ { k \in \pmb { \mathbb { Z } } } y ^ { ( k ) } i e ^ { \frac { \pi } { 2 } i k t } \quad , \quad y ^ { ( k ) } \in \pmb { \mathbb { R } } \enspace , } \end{array}
$$

with the summability condition

$$
\begin{array} { l } { \sum \left| x ^ { ( k ) } \right| ^ { 2 } < \infty } \\ { \sum \left| y ^ { ( k ) } \right| ^ { 2 } < \infty } \end{array}
$$

for $z \in L ^ { 2 } ( 0 , 2 ; \mathbb { C } ^ { n + 1 } )$ . We denote by $E = E _ { 1 } \oplus E _ { 2 }$ the domain of $| L | ^ { \frac { 1 } { 2 } } \ =$ $| L _ { 1 } | ^ { \frac { 1 } { 2 } } \oplus | L _ { 2 } | ^ { \frac { 1 } { 2 } }$ .0n $E$ we define a Hilbertspace norm by

$$
\begin{array} { r c l } { { \| z \| ^ { 2 } } } & { { = } } & { { 2 \pi \left( \sum \left| k \right| \left| x ^ { ( k ) } \right| ^ { 2 } \right) + \pi \left( \sum \left| k \right| \left| y ^ { ( k ) } \right| ^ { 2 } \right) } } \\ { { } } & { { } } & { { + 2 \left( \left| x ^ { ( 0 ) } \right| ^ { 2 } + \left| y ^ { ( 0 ) } \right| ^ { 2 } \right) . } } \end{array}
$$

The norm $\parallel \parallel$ is induced by an inner product $( * , * ) . E$ also admits a splitting according to the parts of $\sigma ( L )$ contained in $( - \infty , 0 ) , \{ \mathbf { 0 } \}$ and $( \mathbf { 0 } , + \infty )$ .We write this as

$$
{ \cal E } = { \cal E } ^ { - } \oplus { \cal E } ^ { 0 } \oplus { \cal E } ^ { + } \ .
$$

Note that for example the elements in $E ^ { - }$ are Fourier series with summation over $k < 0$

We define a smooth map $\Phi : E \longrightarrow \mathbb { R }$ by

$$
\Phi ( z ) = \frac { 1 } { 2 } \left\| z ^ { - } \right\| ^ { 2 } - \frac { 1 } { 2 } \left\| z ^ { + } \right\| ^ { 2 } + a \int _ { 0 } ^ { 2 } \mathrm { I m } ( z _ { n + 1 } ( t ) ) d t \ ,
$$

where ${ \pmb a } > { \pmb 0 }$ is some fixed number. We note that $\Phi$ does not have any critical points. Our proof of the main result will rely on a careful study of suitable compact perturbations of $\Phi$ for a suitable choice of the constant ${ \pmb a } > { \pmb 0 }$ . The underlying nonlinear Functional analysis goes back to [1,5] and our approach is close to [4, 7, 8,9].

We begin by defining a suitable group $\pmb { \it { B } }$ of homeomorphism $h : E \longrightarrow$ $\pmb { \cal E }$ ：A homeomorphism $\pmb { h }$ belongs to $\pmb { \mathscr { B } }$ provided there exist continuous maps $\gamma ^ { \pm } : E \longrightarrow \mathbb { R }$ and $k : E \longrightarrow E$ such that $\gamma ^ { + } , \gamma ^ { - }$ and $\pmb { k }$ map bounded sets into compact sets. Further, there exists a constant $R = R ( h ) > 0$ such that $\gamma ^ { \pm } ( z ) = 0 , k ( z ) = 0$ for $z \in E ^ { - }$ with $\left\| z \right\| \geq R$ Moreover, $\pmb { h }$ can be written in the form

$$
\begin{array} { r l r } { h ( z ) } & { = } & { e ^ { \gamma ^ { - } ( z ) } z ^ { - } + z ^ { 0 } + e ^ { \gamma ^ { + } ( z ) } z ^ { + } - k ( z ) } \\ { z } & { = } & { z ^ { - } + z ^ { 0 } + z ^ { + } \in E ^ { - } \oplus E ^ { 0 } \oplus E ^ { + } ~ . } \end{array}
$$

The group $\pmb { \imath }$ is actually very large and contains all necessary deformations for a variational theory of a suitable global pertubation of $\Phi$ . We note that $\pmb { \it { B } }$ differs somewhat from the group introduced in [2]. We need

Lemma 2.1 For every $h \in B$ we have

$$
h ( E ^ { - } ) \cap ( E ^ { 0 } \oplus E ^ { + } ) \not = \emptyset \ .
$$

Proof: We have to find $z \in E ^ { - }$ with $P ^ { - } h ( z ) = 0$ ， where $P ^ { - } : E \longrightarrow E ^ { - }$ is the orthogonal projection. This equation is equivalent to

$$
\begin{array} { l } { { z = e ^ { - \gamma ^ { - } ( z ) } P ^ { - } k ( z ) = : T ( z ) } } \\ { { { } } } \\ { { z \in E ^ { - } ~ . } } \end{array}
$$

Since $\overline { { T ( E ^ { - } ) } }$ is compact, by our assumptions on $h \in B$ , we find a fixed point by Schauder's fixed point theorem. □

We say a functional $\Psi \in C ^ { \infty } ( E , \mathbb { R } )$ satisfies the weak Palais-Smale condition $( W P S )$ on level $\pmb { d } \in \pmb { \mathbb { R } }$ provided the following holds

Let $b : E \longrightarrow \mathbb { R }$ be a smooth map and assume $b ^ { \prime } : E \longrightarrow E$ maps bounded sets into compact sets. We define $\Phi _ { b }$ by

$$
\Phi _ { b } = \Phi - b \ .
$$

We assume that

$$
\Phi _ { b } ( z ) \longrightarrow + \infty \quad \mathrm { f o r } \quad \| z \| \longrightarrow + \infty , z \in E ^ { - }
$$

and

$$
\mathrm { s u p p } \Phi _ { b } ( E ^ { 0 } \oplus E ^ { + } ) < + \infty .
$$

We define a number $\pmb { d }$ by

$$
d = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \Phi _ { b } ( h ( z ) ) \ .
$$

Our main existence result for critical points is

Proposition 2.2 Assume $b$ is as described above. Then $\pmb { d } \in \pmb { \mathbb { R } }$ and if $( W P S ) _ { d }$ holds $\pmb { d }$ is a critical level.

Proof: By our assumption on $\pmb { b }$ we have

$$
\ : \operatorname * { s u p } \Phi _ { b } ( E ^ { + } \oplus E ^ { 0 } ) < + \infty , \ : \operatorname * { i n f } \Phi _ { b } ( E ^ { - } ) > - \infty \ :
$$

By Lemma 2.1 we know that

$$
h ( E ^ { - } ) \cap ( E ^ { 0 } \oplus E ^ { + } ) \not = \emptyset \ .
$$

Hence

$$
\mathrm { i n f } ~ \Phi _ { b } \bigl ( h \bigl ( E ^ { - } \bigr ) \bigr ) \leq \operatorname* { s u p } \Phi _ { b } \bigl ( E ^ { 0 } \oplus E ^ { + } \bigr ) < + \infty \ .
$$

This proves

$$
- \infty < \operatorname * { i n f } \Phi _ { b } \left( E ^ { - } \right) \le d \le \operatorname * { s u p } \Phi _ { b } \left( E ^ { 0 } \oplus E ^ { + } \right) < + \infty .
$$

Thus we know $\pmb { d } \in \pmb { \mathbb { R } }$ ，Arguing indirectly let us assume that $\pmb { d }$ is not a critical level. In view of $( W P S ) _ { d }$ we find $\epsilon > 0$ such that

$$
\| \Psi ^ { \prime } ( z ) \| \ \ge \epsilon \quad \mathrm { i f } \quad \Psi ( z ) \in [ d - \epsilon , d + \epsilon ] \ ,
$$

where $\Psi = \Phi - b$ . We find a smooth map $\beta : E \longrightarrow [ 0 , 1 ]$ satisfying

$$
\begin{array} { r l } { \beta ( z ) = 0 } & { \quad \mathrm { i f } \qquad \Psi ( z ) \notin [ d - 2 \epsilon , d + 2 \epsilon ] } \\ { \beta ( z ) = 1 } & { \quad \mathrm { i f } \qquad \Psi ( z ) \in [ d - \epsilon , d + \epsilon ] \enspace . } \end{array}
$$

Finally define a globall Lipschitz continuous map $\delta : \mathsf { R } \longrightarrow [ 0 , 1 ]$ by

$$
\begin{array} { r } { \delta ( s ) = \left[ \begin{array} { l l l l } { 1 } & { } & { \mathrm { i f } } & { } & { s \leq 1 } \\ { \frac { 1 } { s } } & { } & { \mathrm { i f } } & { } & { s > 1 } \end{array} \right. . } \end{array}
$$

Using $\Psi ^ { \prime } , \beta$ and $\delta$ we define a bounded locally Lipschitz continuous vector field by

$$
G ( z ) = \beta ( z ) \delta \left( \ \| \Psi ^ { \prime } ( z ) \| \ \right) \Psi ^ { \prime } ( z ) \ .
$$

By our assumption on $b$ we find $R > 0$ such that $\Psi ( z ) \geq d + 2 \epsilon$ for $z \in E ^ { - }$ and $\left\| z \right\| ~ \geq R$ . Hence $G ( z ) = 0$ for $z \in E ^ { - }$ with $\left\| z \right\| ~ \geq R$ . In view of the estimate (17) we find a number ${ \mathbf { \nabla } } T > 0$ ,such that for $h : E \longrightarrow E$ being the time $\mathbf { \nabla } \cdot \pmb { T }$ -map of the flow associated to the ordinary differential equation

$$
\dot { z } = G ( z ) \ ,
$$

we have

$$
\Phi _ { b } ( h ( z ) ) \geq d + \epsilon \mathrm { ~ p r o v i d e d ~ } \Phi _ { b } ( z ) \geq d - \epsilon .
$$

Using the variation of constant formula we deduce the following representation for $\pmb { h }$

$$
h ( z ) = e ^ { \gamma ^ { - } ( z ) } z ^ { - } + z ^ { 0 } + e ^ { \gamma ^ { + } ( z ) } z ^ { + } - k ( z ) \ ,
$$

see [2]. Hence $h \in B$ . By the definition of $\pmb { d }$ we find a $h _ { 0 } \in \mathcal { B }$ such that

$$
\Psi ( h _ { 0 } ( E ^ { - } ) ) \subset [ d - \epsilon , + \infty ) \ .
$$

Combining (22) and (23) gives

$$
\Psi ( h \circ h _ { 0 } ( E ^ { - } ) ) \subset [ d + \epsilon , + \infty ) \ .
$$

Hence

$$
d \geq \operatorname* { i n f } \Psi ( h \circ h _ { 0 } ( E ^ { - } ) ) \geq d + \epsilon . 
$$

Since $d \in \mathbb { R }$ this gives a contradiction in view of $h \circ h _ { 0 } \in B$

The following corollary will be frequently used.

Corollary 2.3 Let $\pmb { b }$ be as described above and assume $\Phi _ { b }$ has a unique critical level $d _ { 0 }$ and satisfies $( W P S ) _ { d }$ for every $d \in \mathbb { R }$ . Then we have the identity

$$
d _ { 0 } = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \Phi _ { b } ( h ( z ) ) .
$$

Proof: In view of Proposition 2.2 the righthand side of (26) has to be a critical level $d .$ By uniqueness $d = d _ { 0 }$ □

# 3A Weak PS-Condition for a Class of Functionals

Let ${ \pmb a } > { \pmb 0 }$ in the definition of $\Phi$ be fixed. Consider a smooth Hamiltonian $K : \mathbb { C } ^ { n + 1 } \longrightarrow [ 0 , + \infty )$ having the following properties:

Moreover:

Next we choose a $H \in \mathcal { H } _ { a d }$ and define $b : E \longrightarrow \mathbb { R }$ by

$$
b ( z ) = \int _ { 0 } ^ { 1 } H ( z _ { 1 } , \dots , z _ { n } ) d t + \int _ { 1 } ^ { 2 } K ( z + \alpha ) d t ,
$$

where

$$
\alpha ( t ) = ( 0 , \ldots , 0 , - a + t a ) \ .
$$

Under our assumption on $\pmb { H }$ and $\pmb { K }$ the map $b : E \longrightarrow \mathbb { R }$ is smooth and extends to a $C ^ { 1 }$ -map on $L ^ { 2 } ( 0 , 2 ; \mathbf { C } ^ { n + 1 } )$

Denoting the $L ^ { 2 }$ -gradient by $\nabla b$ we have the following relation between $\pmb { b } ^ { \prime }$ and $\nabla b$

$$
b ^ { \prime } ( z ) = \left( | L | + P ^ { 0 } \right) ^ { - 1 } \nabla b ( z ) , z \in E .
$$

In view of (27) and (28) we see that $\nabla b ( L ^ { 2 } )$ is $L ^ { 2 }$ -bounded. This implies that

$$
b ^ { \prime } ( E ) { \mathrm { ~ i s ~ b o u n d e d ~ i n ~ } } D ( L ) \subset E ,
$$

where $D ( L )$ is equipped with the graph norm.

Lemma 3.1 Suppose (27) and (28) hold. Then $\Psi = \Phi - b$ satisfies

$$
\begin{array} { r l } & { \Psi ( z )  + \infty f o r z \in E ^ { - } \ w i t h \ \| z \| \  + \infty } \\ & { \mathrm { s u p } \Psi \big ( E ^ { 0 } \oplus E ^ { + } \big ) < + \infty \ . } \end{array}
$$

Proof: For $z \in E ^ { - }$ we estimate

$$
\begin{array} { l l l } { \displaystyle \Psi ( z ) } & { = } & { \displaystyle \frac { 1 } { 2 } \left\| z ^ { - } \right\| ^ { 2 } - \frac { 1 } { 2 } \left\| z ^ { + } \right\| ^ { 2 } + a \int _ { 0 } ^ { 2 } \mathrm { I m } ( z _ { n + 1 } ( t ) ) d t - b ( z ) } \\ { \displaystyle } & { \geq } & { \displaystyle \frac { 1 } { 2 } \left\| z ^ { - } \right\| ^ { 2 } - \mathrm { c o n s t } ( 1 + \left\| z ^ { - } \right\| ) ~ , } \end{array}
$$

for a suitable constant const not depending on $z \in \mathcal { E } ^ { - }$ .Here we used that (27),(28) imply that $\pmb { K }$ has linear growth. Further we find a constant such that

$$
2 a \mathrm { I m } ( z _ { n + 1 } ) - K ( z + \alpha ( t ) ) \leq \mathrm { c o n s t } \ ,
$$

for all $z \in \mathbb { C } ^ { n + 1 }$ and $t \in [ 0 , 2 ]$ .For $z \in E ^ { 0 } \oplus E ^ { + }$ we estimate

$$
\begin{array} { r c l } { \Psi ( z ) } & { = } & { - \frac 1 2 \left\| z ^ { + } \right\| ^ { 2 } + a \int _ { 0 } ^ { 2 } \mathrm { I m } ( z _ { n + 1 } ( t ) ) d t } \\ & & { - \int _ { 0 } ^ { 1 } H ( z _ { 1 } ( t ) , \dots , z _ { n } ( t ) ) d t - \int _ { 1 } ^ { 2 } K ( z + \alpha ) d t } \\ & { \le } & { - \frac 1 2 \left\| z ^ { + } \right\| ^ { 2 } + a \int _ { 0 } ^ { 2 } \mathrm { I m } ( z _ { n + 1 } ( t ) ) d t } \\ & & { - 2 a \int _ { 1 } ^ { 2 } \mathrm { I m } ( z _ { n + 1 } ( t ) ) d t + \mathrm { c o n s t } } \\ & { \le } & { - \frac 1 2 \left\| z ^ { + } \right\| ^ { 2 } + a \int _ { 0 } ^ { 2 } \mathrm { I m } ( P ^ { 0 } z _ { n + 1 } ) d t } \\ & & { - 2 a \int _ { 1 } ^ { 2 } \mathrm { I m } ( P ^ { 0 } z _ { n + 1 } ) d t } \\ & & { + \mathrm { c o n s t } ( 1 + \left\| z ^ { + } \right\| ) } \\ & { = } & { - \frac 1 2 \left\| z ^ { + } \right\| ^ { 2 } + \mathrm { c o n s t } ( 1 + \left\| z ^ { + } \right\| ) \ . } \end{array}
$$

The next step is to show that $\Psi = \Phi - b$ satisfies $( W P S ) _ { d }$ for every $d \in \mathbb { R }$ provided (27) and (28) hold.

Proposition 3.2 Let $( z ( j ) ) \subset E$ be a sequence such that

$$
\Psi ^ { \prime } ( z ( j ) ) \longrightarrow 0 ~ a n d ~ \Psi ( z ( j ) ) \longrightarrow d \in \mathbb { R } .
$$

Then d is a critical level of $\Psi$

Proof: By (32) we know that $\theta ^ { \prime } ( E )$ is bounded in $D ( L )$ . Hence $\left( P ^ { - } + \right.$ $P ^ { + } ) b ^ { \prime } ( E )$ is bouded in $D ( L )$ . Since $\Psi ^ { \prime } ( z ( j ) ) \longrightarrow 0$ in $E$ we see that $\left( P ^ { - } + \right.$ $P ^ { + } ) z ( j )$ can be written as

$$
( P ^ { - } + P ^ { + } ) z ( j ) = u ( j ) + v ( j )
$$

with $( v ( j ) )$ bounded in $D ( L )$ and $u ( j ) \longrightarrow 0$ in $\pmb { \mathcal { E } }$ . By the compact embedding $D ( L ) \hookrightarrow E$ we may assume without loss of generality (after passing to a subsequence)

$$
\begin{array} { l l l } { v ( j ) } & { \longrightarrow } & { v \in D ( L ) \ , v ( j ) \to v \mathrm { ~ i n ~ } E } \\ { u ( j ) } & { \longrightarrow } & { 0 \mathrm { ~ i n ~ } E . } \end{array}
$$

Hence

$$
\begin{array} { r l } & { ( P ^ { - } + P ^ { + } ) ( z ( j ) ) \longrightarrow v \mathrm { ~ i n ~ } E } \\ & { \mathrm { w i t h ~ } v \in D ( L ) . } \end{array}
$$

If $( P ^ { 0 } u ( j ) )$ has a bounded subsequence we are done since $\mathrm { d i m } P ^ { 0 } E < \infty$ . In that case our discussion implies that $( z ( j ) )$ has a subsequence converging in $\pmb { { \cal E } }$ to some $\pmb { z }$ . Taking the limits in (35) implies then the desired result.Hence we may assume $\| P ^ { 0 } z ( j ) \| \longrightarrow + \infty$ .Assume first $( P ^ { \mathbf { 0 } } z ( j ) )$ has a subsequence such that the $( n + 1 )$ -component tends in norm to $+ \infty$ . So,after passing to a subsequence let us assume $| ( P ^ { 0 } z ( j ) ) _ { n + 1 } | \longrightarrow + \infty$ .Using (27)and (28) we see immediately that

$$
\begin{array} { r } { \left| a \int _ { 0 } ^ { 2 } \mathrm { I m } ( z ( j ) _ { n + 1 } ) d t - b ( z ( j ) ) \right| \longrightarrow + \infty } \end{array}
$$

as $j \longrightarrow + \infty$ Since $( { \scriptstyle { \frac { 1 } { 2 } } } \| z ( j ) ^ { - } \| ^ { 2 } \ - { \scriptstyle { \frac { 1 } { 2 } } } \| z ( j ) ^ { + } \| ^ { 2 } \ )$ is bounded we infer

$$
| \Psi ( z ( j ) ) | \longrightarrow + \infty \ ,
$$

contradicting our assumption $\Psi ( z ( j ) ) \longrightarrow d \in \mathbb { R }$ .Hence we may assume that the $( n + 1 )$ -component of $( P ^ { \mathbf { 0 } } z ( j ) )$ is bounded. Let us write $( P ^ { 0 } z ( j ) _ { r } )$ for the first $\pmb { n }$ components.Hence we know so far

$$
\begin{array} { r l r } { \| P ^ { 0 } z ( j ) _ { n + 1 } \| } & { { } \le } & { \mathrm { c o n s t } } \\ { \| P ^ { 0 } z ( j ) _ { r } \| } & { { } \longrightarrow } & { + \infty } \end{array}
$$

and may assume after taking a sequence

$$
P ^ { 0 } z ( j ) _ { n + 1 } \longrightarrow i \tau \ ,
$$

where ${ \pmb { \tau } } \in { \pmb { \mathbb { R } } }$ . Hence, using (28)

$$
K ^ { \prime } ( z ( j ) ) \longrightarrow ( 0 , . . . , 0 , i \varphi ^ { \prime } ( \tau ) )
$$

in $L ^ { 2 } ( 1 , 2 ; \mathbf { C } ^ { n + 1 } )$ and

$$
{ \cal H } ^ { \prime } ( z ( j ) _ { 1 } , \ldots , z ( j ) _ { n } ) \longrightarrow 0
$$

in $L ^ { 2 } ( 0 , 1 ; \mathbf { C } ^ { n } )$ . This implies

$$
b ^ { \prime } ( z ( j ) ) \longrightarrow \left( | L | + P ^ { 0 } \right) ^ { - 1 } \left( \chi ( 0 , \ldots , 0 , i \varphi ^ { \prime } ( \tau ) ) \right)
$$

in $D ( L )$ ， where $x$ is the characteristic function of the interval [1,2]. Moreover

$$
\Phi ^ { \prime } ( z ( j ) ) = z ( j ) ^ { - } - z ( j ) ^ { + } + \left( \frac { } { } | L | + P ^ { 0 } \right) ^ { - 1 } \left( 0 , \ldots , 0 , i a \right) \ .
$$

Since $\Psi ^ { \prime } ( z ( j ) ) \longrightarrow 0$ we conclude

$$
\begin{array} { l } { { v ^ { - } - v ^ { + } + \left( \left| L \right| + P ^ { 0 } \right) ^ { - 1 } \left( 0 , \ldots , 0 , i a \right) } } \\ { { = \left( \left| L \right| + P ^ { 0 } \right) ^ { - 1 } \left( \chi ( 0 , \ldots , 0 , i \varphi ^ { \prime } ( \tau ) ) \right) \ . } } \end{array}
$$

Applying $| L | + P ^ { 0 }$ gives

$$
\begin{array} { l } { - L v + ( 0 , \dots , i a ) = \chi ( 0 , \dots , 0 , i \varphi ^ { \prime } ( \tau ) ) } \\ { v \in D ( L ) \ . } \end{array}
$$

This precisely means

$$
\begin{array} { l } { { i \left( \displaystyle \frac { d v } { d t } + \displaystyle \frac { d \alpha } { d t } \right) = \chi ( 0 , . . . , 0 , i \varphi ^ { \prime } ( \tau ) ) } } \\ { { v \in D ( L ) \ . } } \end{array}
$$

Let us put $u ( t ) = v ( t ) + \alpha ( t )$ . Then

$$
\begin{array} { r c l } { \dot { u } } & { = } & { \chi ( t ) ( 0 , \dots , 0 , \varphi ^ { \prime } ( \tau ) ) \mathrm { ~ o n ~ } ( 0 , 2 ) } \\ { u _ { k } ( 0 ) } & { = } & { u _ { k } ( 2 ) \mathrm { ~ f o r ~ } k = 1 , \dots , n } \\ { \operatorname { R e } ( u _ { n + 1 } ) ( 0 ) } & { = } & { - a , \operatorname { R e } \bigl ( u _ { n + 1 } ( 2 ) \bigr ) = a \ . } \end{array}
$$

This implies $u _ { 1 } \ = \ \ldots \ = \ u _ { n } \ =$ const and $u _ { n + 1 } ( t ) ~ = ~ - a + i \tau$ for $t \in$ $[ 0 , 1 ] , u _ { n + 1 } ( t ) = - a + 2 ( t - 1 ) a + i \tau$ for $t \in [ 1 , 2 ]$ . Consequently $\varphi ^ { \prime } ( \tau ) = 2 a$

It is clear by (27) and (28) that

$$
d = \operatorname* { l i m } \Psi \big ( z ( j ) \big ) = 2 a \tau - \varphi ( \tau ) - m ( H ) \ .
$$

It remains to show that $\pmb { d }$ is a critical level. Let $\hat { \pmb u } ( t ) = ( 0 , \ldots , 0 , \ b u _ { n + 1 } ( t ) )$ ， where ${ \pmb u } _ { n + 1 }$ is as just defined. Let $z ( t )$ be given by $z ( t ) = ( 0 , \ldots , u _ { n + 1 } ( t ) +$ ${ \pmb a } - t { \pmb a } ) = \hat { { \boldsymbol u } } ( t ) - { \pmb \alpha } ( t )$ .Finally consider

$$
\gamma e _ { 1 } + z ( t )
$$

for $\gamma \geq 0$ a real number. For $\gamma$ large we have

$$
\begin{array} { r c l } { { K ^ { \prime } \left( \gamma e _ { 1 } + z ( t ) \right) } } & { { = } } & { { ( 0 , . . . , 0 , i \varphi ^ { \prime } ( \tau ) ) } } \\ { { } } & { { } } & { { } } \\ { { H ^ { \prime } \left( \left( \gamma e _ { 1 } + z ( t ) \right) _ { r } \right) } } & { { = } } & { { 0 \ . } } \end{array}
$$

Hence, for $\gamma$ large the map $\gamma e _ { 1 } + z ( t )$ which belongs to $D ( L )$ is a critical point for $\Psi$ with critical level

$$
\Psi ( \gamma e _ { 1 } + z ) = 2 a \tau - \varphi ( \tau ) - m ( H ) \ .
$$

This completes the proof of Proposition (3.2).

# 4Some Estimates for Max-Min-Levels

Let $l \in \pmb { \mathbb { R } }$ and assume $\varphi : \mathbb { R } \longrightarrow [ 0 , + \infty )$ is a smooth map satisfying

$$
\begin{array} { r c l } { { \varphi ( s ) } } & { { = } } & { { 0 \mathrm { ~ f o r ~ } s \leq l } } \\ { { \varphi ^ { \prime } ( s ) } } & { { > } } & { { 0 \mathrm { ~ f o r ~ } s > l } } \\ { { \varphi ^ { \prime } ( s ) } } & { { = } } & { { \mathrm { c o n s t > 2 } a \mathrm { ~ f o r ~ } s \mathrm { ~ l a r g e } } } \\ { { \varphi ^ { \prime } ( s _ { 0 } ) } } & { { = } } & { { 2 a \mathrm { ~ h a s ~ a ~ u n i q u e ~ s o l u t i o n } . } } \end{array}
$$

Here ${ } ^ { \mathfrak { a } } { } _ { \pmb { a } } { } ^ { \mathfrak { n } }$ is again the number occurring in the definition of $\Phi$ . We denote by $\theta _ { l }$ the collection of all $\varphi$ 's satisfying (36).We define $b : E \longrightarrow \mathbb { R }$ by

$$
b ( z ) = \int _ { 1 } ^ { 2 } \varphi ( \mathrm { I m } z _ { n + 1 } ( t ) ) d t \ .
$$

Then in view of 3.1 and 3.2 the functional $\Phi _ { b }$ satisfies $( W P S ) _ { d }$ for every $\pmb { d } \in \pmb { \mathbb { R } }$ and

$$
d = \operatorname* { s u p } _ { n \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \Phi _ { b } \bigl ( h ( z ) \bigr )
$$

is a real number and a critical level.A straight forward calculation shows that $\Phi _ { b }$ has precisely one critical level $\pmb { d }$ which satisfies $\Phi _ { b } ( z ) = d$ with $\pmb { z }$ of the form

$$
z ( t ) = ( \mathbf { c _ { 1 } } , \dots , c _ { n } , z _ { n + 1 } ( t ) ) \ ,
$$

where $\mathbf { { \mathfrak { c } } _ { 1 } } , \dots , \mathbf { { \mathfrak { c } } _ { n } } \in \mathbf { C } ^ { n }$ are any constants and

$$
\begin{array} { r c l } { { z _ { n + 1 } ( t ) } } & { { = } } & { { i \tau - t a \mathrm { ~ f o r ~ } t \in [ 0 , 1 ] } } \\ { { } } & { { } } & { { z _ { n + 1 } ( t ) } } \end{array}
$$

with $\varphi ^ { \prime } ( \tau ) = 2 a$ (which determines $\pmb { \tau }$ uniquely). We compute easily that

$$
\begin{array} { r } { d = \Phi _ { b } ( z ) = 2 a \tau - \varphi ( \tau ) \ . } \end{array}
$$

We have

Proposition 4.1 For fixed $\iota$ consider for $\varphi \in \pmb { \theta } _ { l }$ the corresponding min max value $d ( \varphi )$ . Then

$$
\operatorname * { i n f } _ { \varphi \in \theta _ { l } } d ( \varphi ) = 2 a l \ .
$$

Proof: By the previous discussion ${ \Phi } _ { b }$ with $b = b ( \varphi )$ has a unique critical level

$$
d ( \varphi ) = 2 a \tau - \varphi ( \tau ) \ ,
$$

where $\pmb { \tau }$ is determined by the equation

$$
\varphi ^ { \prime } ( \tau ) = 2 a \ .
$$

Given ${ \boldsymbol { \delta } } > \mathbf { 0 }$ and $\varphi \in \theta _ { l }$ we find $\tilde { \varphi } \in \theta _ { l }$ with

$$
\tilde { \varphi } \geq \varphi
$$

and

$$
\tilde { \varphi } ^ { \prime } ( \tau ) = 2 a \Rightarrow \tilde { \varphi } ( \tau ) \leq \delta \ .
$$

By the definition of $d ( \varphi )$ it follows immediately that

$$
d ( \tilde { \varphi } ) \leq d ( \varphi ) \ .
$$

Moreover,(39) implies in view of $\tau > l$

$$
\begin{array} { l c l } { { d ( \tilde { \varphi } ) } } & { { = } } & { { 2 a \tau - \tilde { \varphi } ( \tau ) } } \\ { { } } & { { \geq } } & { { 2 a l - \delta ~ . } } \end{array}
$$

Since $\delta$ was arbitrarily choosen we find in view of (40) and (41)

$$
\operatorname * { i n f } _ { \varphi \in \theta _ { l } } d ( \varphi ) \geq 2 a l .
$$

Since for given ${ \pmb \delta } > { \pmb 0 }$ ,we find $\tilde { \varphi } \in \theta _ { l }$ with $\tilde { \varphi } ^ { \prime } ( \tau ) = 2 a$ for $\tau < l + \delta$ ， we deduce

$$
\begin{array} { l l l } { { d ( \tilde { \varphi } ) } } & { { \leq } } & { { 2 a ( l + \delta ) - \tilde { \varphi } ( \tau ) } } \\ { { } } & { { \leq } } & { { 2 a l + 2 a \delta ~ . } } \end{array}
$$

This implies the desired equality

$$
\operatorname* { i n f } _ { \varphi \in \theta _ { l } } d ( \varphi ) = 2 a l
$$

with

$$
d ( \varphi ) = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \Big [ \Phi \big ( h ( z ) \big ) - \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } h ( z ) _ { n + 1 } ) d t \Big ] \enspace .
$$

Next assume $H \in \mathcal { H } _ { a d }$ .For $\tau \in [ 0 , 1 ]$ and $\varphi \in \theta _ { l }$ we define $b _ { \tau }$ by

$$
\begin{array} { l l l } { \displaystyle b _ { \tau } ( z ) } & { : = } & { \displaystyle b _ { \tau , \varphi , H } ( z ) } \\ { \displaystyle } & { = } & { \displaystyle \tau \int _ { 0 } ^ { 1 } H ( z _ { 1 } , \dots , z _ { n } ) d t + \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } z _ { n + 1 } ( t ) ) d t \ . } \end{array}
$$

Finally we put $\Phi _ { \tau } : = \Phi - b _ { \tau }$ . We have in view of Proposition 4.1 the estimate

$$
\begin{array} { r l } & { - m ( H ) + \Phi ( z ) - \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } z _ { n + 1 } ) d t } \\ { \le } & { \Phi ( z ) - \int _ { 0 } ^ { 1 } H ( z _ { 1 } , . . . , z _ { n } ) d t - \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } z _ { n + 1 } ) d t } \\ { \le } & { \Phi ( z ) - \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } z _ { n + 1 } ) d t \ . } \end{array}
$$

Moreover for all $z \in E$ ：

$$
| \Phi _ { \tau _ { 2 } } ( z ) - \Phi _ { \tau _ { 1 } } ( z ) | \ \leq m ( H ) \left| \tau _ { 2 } - \tau _ { 1 } \right| \ .
$$

We define $d _ { \tau } : = d _ { \tau , \varphi , H }$ by

$$
d _ { \tau } = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \Phi _ { \tau } \big ( h ( z ) \big ) \ .
$$

In view of (43) the map $\tau \longrightarrow d _ { \tau }$ is continuous and non increasing. The crucial point is

Lemma ${ \bf 4 . 2 } \ \tau \longrightarrow d _ { \tau }$ is a constant map. In particular we have

$$
d ( \varphi ) = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in h ( E ^ { - } ) } \Big [ \Phi ( z ) - \int _ { 0 } ^ { 1 } H ( z _ { 1 } , \dots , z _ { n } ) d t - \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } z _ { n + 1 } ) d t \Big ]
$$

for every $H \in \mathcal { H } _ { a d } \mathrm { ~ } a n d \mathrm { ~ } \varphi \in \theta _ { l }$

Proof: $H$ vanishes on some nonempty set $U$ . Let $\delta \in U$ . We define $H _ { 0 }$ by

$$
H _ { 0 } ( z ) = \frac { \pi } { 3 } \left| ( z _ { 1 } , \dots , z _ { n } ) - \delta \right| ^ { 2 } .
$$

For $\pmb { \tau } > \mathbf { 0 }$ small we have

$$
H _ { 0 } \geq \tau H .
$$

We define $\tilde { \Phi } : E \longrightarrow \mathsf { R }$ by

$$
\tilde { \Phi } ( z ) = \Phi ( z ) - \int _ { 0 } ^ { 1 } H _ { 0 } ( z ( t ) ) d t - \int _ { 1 } ^ { 2 } \varphi ( \mathrm { I m } z _ { n + 1 } ) d t \mathrm { ~ . ~ }
$$

One estimates easily in view of (45) (recall $\sigma ( L _ { 1 } )$ ）

$$
\begin{array} { l } { { \widetilde { \Phi } ( z ) \longrightarrow + \infty \mathrm { ~ f o r ~ } \| z \|  \infty \mathrm { , ~ } z \in E ^ { - } } } \\ { { \mathrm { s u p ~ } \widetilde { \Phi } ( E ^ { + } \oplus E ^ { 0 } ) < \infty \mathrm { ~ . ~ } } } \end{array}
$$

Also $\tilde { \Phi }$ satisfies $( W P S ) _ { d }$ for every $\pmb { d } \in \pmb { \mathbb { R } }$ . (In fact it satisfies even the usual Palais-Smale condition.） The fact that it satisfes $( P S )$ follows as in Proposition 3.2 up to the point that the form (45)of $H _ { \mathbf { 0 } }$ even implies that ( $\left( | | P ^ { 0 } z ( j ) | | \right)$ is bounded on a Palais-Smale sequence

$$
{ \tilde { \Phi } } ( z ( j ) ) \longrightarrow d , { \tilde { \Phi } } ^ { \prime } ( z ( j ) ) \longrightarrow 0 .
$$

(The argument is similar as in [8]. Further $\tilde { \Phi }$ has precisely one critical point $\pmb { z }$ satisfying

$$
\tilde { \Phi } ( z ) = d ( \varphi ) ~ .
$$

Hence in view of (46) for ${ \pmb \tau } \geq { \bf 0 }$ small

$$
\begin{array} { l l l } { { d ( \varphi ) } } & { { = } } & { { \displaystyle \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } \big ( h ( z ) \big ) } } \\ { { } } & { { \le } } & { { \displaystyle \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \Phi _ { \tau } \big ( h ( z ) \big ) } } \\ { { } } & { { \le } } & { { d ( \varphi ) \ . } } \end{array}
$$

Consequently $\tau \longrightarrow d _ { \tau }$ is non increasing, continuous and constant for $\pmb { \tau }$ close to 0.The critical levels of $\Phi _ { \tau }$ for $\tau \in [ 0 , 1 ]$ are given by the set

$$
\Gamma _ { \tau } = \{ d ( \varphi ) - \tau H ( m ) \mid d H ( m ) = 0 \} .
$$

By Sard's theorem $\boldsymbol { \Gamma } _ { \tau }$ has measure zero. Moreover,it is evidently compact. Summing up,for some $\pmb { \tau _ { 0 } } > \mathbf { 0 }$ small

$$
\begin{array} { l } { { d _ { \tau } = d ( \varphi ) \ \mathrm { f o r } \ 0 \leq \tau \leq \tau _ { 0 } } } \\ { { d _ { \tau } \in \Gamma _ { \tau } \ \mathrm { f o r } \ \tau \in [ 0 , 1 ] \ . } } \end{array}
$$

The second part of (48)and the properties of $\Gamma _ { \tau }$ imply

$$
d _ { \tau } = d ( \varphi ) - \tau H ( m ) , \tau \in [ 0 , 1 ]
$$

for some $m \in \mathbb { C } ^ { n }$ . The first part of (48) implies $\begin{array} { r } { H ( m ) = 0 } \end{array}$ . This completes the proof of 4.2. □

Summing up the previous discussion we have the following crucial ${ \mathfrak { a } } _ { \mathfrak { a } }$ priori equality":

Proposition 4.3 For any $H \in \mathcal { H } _ { \mathfrak { a d } }$ we have the equality

$$
2 a l = \operatorname* { i n f } _ { \varphi \in \theta _ { l } } \operatorname* { s u p } _ { h \in \mathcal { B } } \operatorname* { i n f } _ { z \in h ( E ^ { - } ) } \left[ \Phi ( z ) - \int _ { 0 } ^ { 1 } H ( z _ { 1 } , \dots , z _ { n } ) d t - \int _ { 1 } ^ { 2 } \varphi ( \operatorname { I m } z _ { n + 1 } ) d t \right] \ .
$$
