# 2 Instanton homology

In this section we discuss Floer's instanton homology for nontrivial SO(3)- bundle.All the theorems are due to Floer [11], [13]. Let $\pmb { M }$ be a compact connected oriented 3-dimensional manifold without boundary and $\pi : Q $ $\pmb { M }$ be a principal bundle with structure group $G = { \bf S } 0 ( { \bf 3 } )$ . We identify the space $\pmb { A } ( Q )$ of connections on $Q$ with the space of smooth Lie algebra valued 1-forms ${ \pmb a } \in \Omega ^ { 1 } ( Q , { \pmb \mathfrak { g } } )$ which are equivariant with respect to the adjoint action of $\pmb { G }$ and canonical in the fibres:

$$
a _ { p x } ( v x ) = x ^ { - 1 } a _ { p } ( v ) x , \qquad a _ { p } ( p \xi ) = \xi
$$

for $v \in T _ { p } Q , x \in G$ and $\xi \in { \mathfrak { g } }$ The space $\mathcal { G } ( Q )$ of gauge transformations can be canonically identified with the space smooth maps $g : Q  G$ which

are equivariant under the action of $\pmb { G }$ on itself through inner automorphisms:

$$
g ( p x ) = x ^ { - 1 } g ( p ) x .
$$

Thus gauge transformations are sections of the adjoint bundle $G _ { Q } = Q \times _ { \bf a d } G$ which consists of equivalence classes of pairs $[ p , A ]$ where $p \in Q$ and ${ \pmb g } \in G$ under the equivalence relation $[ p , g ] \equiv [ p x , x ^ { - 1 } g x ]$ for ${ \pmb x } \in G$ .With these identifications ${ \mathcal { G } } ( Q )$ acts on $\pmb { A } ( Q )$ by the formula

$$
g ^ { * } a = g ^ { - 1 } d g + g ^ { - 1 } a g .
$$

Let ${ \mathfrak { g } } _ { \mathfrak { d } } ( Q )$ denote the component of the identity in $\mathcal { G } ( Q )$ and consider the quotient

$$
\mathscr { C } ( Q ) = \mathscr { A } ( Q ) / \mathscr { G } _ { 0 } ( Q ) .
$$

This space is not an infinite dimensional manifold since the group $\mathcal { G } _ { 0 } ( Q )$ does not act freely on $\pmb { A } ( Q )$ . However,almost every connection is a regular point of the action. More precisely, let

$$
{ \mathcal { G } } _ { a } = \{ g \in { \mathcal { G } } ( Q ) : g ^ { * } a = a \}
$$

denote the isotropy subgroup of a connection $a \in \mathcal { A } ( Q )$

Lemma 2.1 The isotropy subgroup of $\pmb { a }$ connection $a \in \mathcal { A } ( Q )$ is discrete if and only if

$$
{ \mathcal { G } } _ { a } \cap { \mathcal { G } } _ { 0 } ( Q ) = \{ 1 \} .
$$

Connections with ${ \pmb a }$ discrete isotropy subgroup are called regular.

Proof: Suppose that $g \in \mathcal { G } _ { a } \cap \mathcal { G } _ { 0 } ( Q )$ and ${ \pmb g } \neq { \bf 1 }$ . Then $\pmb { g }$ lifts to a map ${ \tilde { \pmb { \mathscr { g } } } } : Q  S U ( 2 )$ and $\tilde { \pmb { g } } ( \pmb { p } ) \in S U ( 2 )$ commutes with the holonomy subgroup $\tilde { \cal H } \subset S U ( 2 )$ of $\pmb { a }$ at the point $p \in Q$ lifted to $S U ( 2 )$ Since $g \neq 1$ the matrix $\tilde { \pmb g } ( \pmb { p } )$ has two distinct eigenvalues and both eigenspaces are invariant under the holonomy group $\tilde { H }$ . Thus there exists a circle of matrices in $S U ( 2 )$ commuting with $\tilde { H }$ and therefore $\pmb { \mathcal { G } _ { a } }$ is not discrete. □

The group of components of ${ \mathfrak { G } } ( Q )$ acts on $\mathcal { C } ( Q )$ . These components are characterized by two invariants, the degree

$$
\deg : \mathcal { G } ( Q ) \to \pmb { \mathscr { Z } }
$$

and the parity

$$
\eta : { \mathcal { G } } ( Q ) \to H ^ { 1 } ( M ; { \mathbf { Z } } _ { 2 } ) .
$$

The definition of the degree is based on the next lemma. The proof was personally communicated to the second author by John Jones.

Lemma 2.2 (1） If $w _ { 2 } ( Q ) = 0$ then the induced map $\pi _ { * } : H _ { 3 } ( Q , { \bf 7 } ) \to$ $H _ { 3 } ( M , \mathbf { \vec { z } } )$ is onto.   
(2)If $w _ { 2 } ( Q ) \neq 0$ then the induced map $\pi ^ { * } : H ^ { 3 } ( M , \mathbb { Z } _ { 2 } ) \to H ^ { 3 } ( Q , \mathbb { Z } _ { 2 } )$ is zero and $H _ { 3 } ( M , \mathbf { Z } ) / \mathrm { i m } \pi _ { * } = \mathbf { Z } _ { 2 }$   
(3) For every $g \in { \mathcal { G } } ( Q )$ the induced map $g _ { * } : H _ { 3 } ( Q , \mathbf { Z } ) \to H _ { 3 } ( \mathrm { S O ( 3 ) } , \mathbf { Z } )$ descends to a homomorphism $H _ { 3 } ( M , { \bf Z } )  H _ { 3 } ( \mathrm { S O ( 3 ) } , { \bf Z } )$

Proof: Examine the spectral sequence of the bundle $Q  M$ with integer coefficients to obtain

$$
H _ { 3 } ( Q , \mathbf { Z } ) / \ker \pi _ { * } \simeq \operatorname { i m } \pi _ { * } \simeq \ker \Bigl ( d _ { 2 } : H _ { 3 } ( M , \mathbf { Z } ) \to H _ { 1 } ( M , \mathbf { Z } _ { 2 } ) \Bigr ) .
$$

Now we also have that the image of the fundamental class $[ M ]$ under $d _ { 2 }$ ： $H _ { 3 } ( M , \mathbf { Z } ) \to H _ { 1 } ( M , \mathbf { Z } _ { 2 } )$ is the Poincaré dual of $w _ { 2 } ( Q )$ . Hence $\pmb { \pi } _ { \ast }$ is onto if and only if ${ \mathfrak { w } } _ { 2 } ( Q ) = 0$ and $\mathrm { i m } \pi _ { * } = \langle 2 [ M ] \rangle$ otherwise. This proves statements (1) and (2).

Now let $\iota : \mathrm { S O } ( 3 )  Q$ be the inclusion of a fiber and denote the induced map on homology by $\iota _ { * } : H _ { 3 } ( \mathrm { S O } ( 3 ) , { \bf Z } )  H _ { 3 } ( Q , { \bf Z } )$ . Then it follows again by examining the spectral sequence that $\pmb { \iota } _ { \ast }$ is injective and

$$
\mathrm { i m } \iota _ { * } \subset \ker \pi _ { * } , \qquad \ker \pi _ { * } / \mathrm { i m } \iota _ { * } \simeq H _ { 2 } ( M , \mathbf { Z } _ { 2 } )
$$

For every gauge transformation $g : Q  \mathsf { S O } ( 3 )$ denote $g _ { * } : H _ { 3 } ( Q , { \bf Z } ) \to$ $H _ { 3 } ( { \bf S O ( 3 ) } , { \bf Z } )$ . The composition $\textbf { \em g o } \pmb { \iota }$ is homotopic to a constant and hence we have $\mathrm { i m } \iota _ { * } \subset \ker g _ { * }$ . This implies that ${ \pmb { g } } _ { \ast }$ descends to a homomorphism $H _ { 3 } ( Q , { \bf Z } ) / \mathrm { i m } \iota _ { * } \to H _ { 3 } ( \mathrm { S O ( 3 ) } , { \bf Z } ) = { \bf Z }$ . Any such homomorphism must vanish on the subgroup ker $\pi _ { * } / \mathrm { i m } \iota _ { * } \simeq H _ { 2 } ( M , \mathbf { Z } _ { 2 } )$ . Thus we have proved that

$$
\ker \pi _ { * } \subset \ker g _ { * }
$$

for every gauge transformation ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$ . In view of statement (2) it suffices to prove that

$$
\begin{array} { r l r } { w _ { 2 } ( Q ) \neq 0 } & { { } \implies } & { \mathsf { i m } g _ { * } \subset \langle 2 [ \mathrm { S O } ( 3 ) ] \rangle } \end{array}
$$

for every gauge transformation ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$ . We prove instead that the dual homomorphism $g ^ { \ast } : H ^ { 3 } ( \mathrm { S O } ( 3 ) , \mathbb { Z } _ { 2 } )  H ^ { 3 } ( Q , \mathbb { Z } _ { 2 } )$ is zero. To see this consider the generator $\alpha \in H ^ { 1 } ( \mathrm { S O } ( 3 ) , \mathbf { Z } _ { 2 } )$ . Since $\iota ^ { * } g ^ { * } = 0$ it follows that $g ^ { \ast } \alpha = \pi ^ { \ast } \beta$ for some $\beta \in H ^ { 1 } ( M , \mathbf { Z } _ { 2 } )$ . Hence $g ^ { * } ( \alpha ^ { 3 } ) = \pi ^ { * } ( \beta ^ { 3 } ) = 0$ where the last assertion follws from statement (2). This proves the lemma. □

For ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$ the induced homomorphism ${ \cal H } _ { 3 } ( M , { \bf Z } ) = { \bf Z }  { \cal H } _ { 3 } ( G , { \bf Z } ) = { \bf Z }$ is determined by an integer $\deg ( g )$ called the degree of $\pmb { g }$ .Alternatively, the degree can be defined as the intersection number of the submanifolds graph $( g ) = \{ [ p , g ( p ) ] : p \in Q \}$ and graph (1) of the adjoint bundle $G _ { Q }$ ·

The homomorphism $g _ { * } : \pi _ { 1 } ( Q ) \to \pi _ { 1 } ( G ) = \mathbb { Z } _ { 2 }$ descends to a homomorphism $\eta ( g ) : \pi _ { 1 } ( M ) \to { \mathbf { Z } } _ { 2 }$ , called the parity of $\pmb { g }$ . It is the obstruction for $\pmb { g }$ to lift to a map ${ \tilde { \pmb { \mathfrak { g } } } } : { \pmb { Q } }  \mathbf { S U } ( 2 )$ . A gauge transformation is called even if $\eta ( g ) = 0$ . Every even gauge transformation is of even degree but not vice versa. Moreover, the map $\eta : \mathcal { G } ( Q )  H ^ { 1 } ( M , \mathbf { Z } _ { 2 } )$ is always onto. Throughout we shall assume the following hypothesis.

Hypothesis (H1) Every cohomology class $\eta \in H ^ { 1 } ( M ; \mathbf { Z } _ { 2 } )$ can be represented by finitely many embedded oriented Riemann surfaces. Moreover $w _ { 2 } ( Q ) \neq 0$

If $M$ is orientable then every one dimensional integral cohomology class can be represented by finitely many embedded oriented Riemann surfaces. So the first part of hypothesis (H1) will be satisfied whenever $\pmb { M }$ is orientable and there is no 2-torsion in $H _ { 1 }$ .Also note that (H1) implies the following weaker hypothesis.

Hypothesis (H2) There exists an embedding $\iota : \Sigma \to M$ of a Riemann surface such that $\iota ^ { * } Q$ is the nontrivial $S O ( 3 )$ -bundle over $\pmb { \Sigma }$

Some important consequences of hypotheses (H1) and (H2) are summarized in the next lemma. The proof will be given in the appendix.

Lemma 2.3 (1) Two gauge transformations are homotopic if and only if they have the same degree and the same parity.

(2) Assume $( H 1 )$ . Then for every ${ \mathfrak { g } } \in { \mathcal { G } } ( Q )$

$$
\deg ( g ) \equiv w _ { 2 } ( Q ) \cdot \eta ( g ) { \pmod { 2 } } .
$$

Conversely, for every integer $\pmb { k }$ and every $\eta \in H ^ { 1 } ( M ; \mathbf { Z } _ { 2 } )$ with $\pmb { k } \equiv$ $w _ { 2 } ( Q ) \cdot \eta$ (mod 2) there exists $\pmb { a }$ gauge transformation with $\deg ( g ) = k$ and $\eta ( g ) = \eta$

(3) Assume $\left( H 2 \right)$ . Then there exists a gauge transformation $\pmb { g }$ of degree 1.

Remark 2.4 (i) If $Q = \mathsf { R } P ^ { 3 } \times S O ( 3 )$ then there exists a gauge transformation of degree 1. However, for such a gauge transformation equation (1) is violated since ${ w _ { 2 } ( Q ) = 0 }$ .If $M$ isa homology 3-sphere and $Q = M \times \mathsf { S } 0 ( 3 )$ is the product bundle then equation (1) is trivially satisfied but there is no gauge transformation of degree 1.

(ii) Another interesting example is the (unique) nontrivial SO(3)-bundle $\pi : Q  \mathbb { R } P ^ { 3 }$ . This bundle does not satisfy hypothesis (H2). It can be represented in the form $Q = S ^ { 3 } \times _ { \pmb { \imath } _ { 2 } }$ SO(3) with $( { \pmb x } , A ) \sim ( - { \pmb x } , R A )$ where $R \in \mathsf { S O } ( 3 )$ is a reflection, i.e. $R ^ { 2 } = \mathbb { 1 }$ A gauge transformation of this bundle is a smooth map $g : S ^ { 3 }  \mathbb { S } { \mathsf { O } } ( 3 )$ such that $g ( - x ) = R g ( x ) R$ . Any such map lifts to a smooth map $\tilde { \pmb { g } } : S ^ { 3 }  \mathbb { S } \mathbb { U } ( 2 )$ and the degree of $\pmb { g }$ in the above sense is the degree of the lift $\pmb { \tilde { g } }$ (or half the degree of $\pmb { g }$ as a map between oriented 3-manifolds). The lift $\tilde { \pmb g }$ is necessarily of even degree.So in this case there is no gauge transformation of degree 1. Hence statements (2) and (3) of Lemma 2.3 are both violated.

The space $\pmb { A } ( Q )$ of connections on $Q$ is an affine space whose associated vector space is $\Omega ^ { 1 } ( { \mathfrak { g } } _ { Q } )$ . Here ${ \mathfrak { g } } _ { Q } = Q \times _ { G } { \mathfrak { g } }$ is the vector bundle over $\pmb { M }$ associated to $Q$ via the adjoint representation of $\pmb { G }$ on its Lie algebra. We think of an infinitesimal connection $\alpha \in \Omega ^ { 1 } ( \mathfrak { g } _ { Q } )$ as an invariant and horizontal 1-form on $Q$ .The Lie algebra of ${ \mathfrak { G } } ( Q )$ is the space of invariant ${ \mathfrak { g } }$ -valued functions on $Q$ and so may be identified with $\Omega ^ { 0 } ( { \mathfrak { g } } _ { Q } )$ .The infinitesimal action of $\mathcal { G } ( Q )$ is given by the covariant derivative

$$
d _ { a } : \Omega ^ { 0 } ( \mathfrak { g } _ { Q } ) \to \Omega ^ { 1 } ( \mathfrak { g } _ { Q } ) , \qquad d _ { a } \eta = d \eta + [ a \wedge \eta ] .
$$

Thus the tangent space to the configuration space $\mathcal { C } ( Q )$ at a regular connection $\pmb { a }$ is the quotient $\Omega ^ { 1 } ( { \mathfrak { g } } _ { Q } ) / { \mathrm { i m } } d _ { a }$ ：

The curvature of a connection is the 2-form

$$
F _ { a } = d a + \frac { 1 } { 2 } [ a \wedge a ] \in \Omega ^ { 2 } ( M ; \mathfrak { g } _ { Q } )
$$

and determines a natural 1-form on the space of connections via the linear functional

$$
\alpha \mapsto \int _ { M } \langle F _ { a } \wedge \alpha \rangle
$$

on $T _ { a } \mathcal { A } ( Q ) = \Omega ^ { 1 } ( \mathfrak { g } _ { Q } )$ . Here $\langle , \rangle$ denotes the invariant inner product on the Lie algebra $\mathfrak { g }$ given by minus the Killing form or 4 times the trace.We shall denote this 1-form by $\pmb { F }$ . The Bianchi identity asserts that $\pmb { F }$ is closed. Since the affine space $\pmb { A } ( Q )$ is contractible this implies that $\pmb { F }$ is the differential of a function. Integrating $\pmb { F }$ along a path which starts at a fixed flat connection ${ a _ { 0 } \in \mathcal { A } ( Q ) }$ we obtain the Chern-Simons functional

$$
\mathcal { C } S ( a _ { 0 } + \alpha ) = \frac 1 2 \int _ { M } \Big ( \langle d _ { a _ { 0 } } \alpha \wedge \alpha \rangle + \frac 1 3 \langle \left[ \alpha \wedge \alpha \right] \wedge \alpha \rangle \Big )
$$

for $\alpha \in \Omega ^ { 1 } ( \mathfrak { g } _ { Q } )$ . One can check directly that

$$
d \mathcal { C } \mathcal { S } ( a ) \alpha = \int _ { M } \langle F _ { a } \wedge \alpha \rangle
$$

for $a \in \mathcal { A } ( Q )$ and $\alpha \in \Omega ^ { 1 } ( \mathfrak { g } _ { Q } )$ . Thus the fat connections on $Q$ appear as the critical points of the Chern-Simons functional. Since the 1-form $d { \mathcal { C } } { \mathcal { S } } = F$ is invariant and horizontal it follows that the difference $\mathcal { C } \mathcal { S } ( g ^ { * } a ) - \mathcal { C } \mathcal { S } ( a )$ is independent of the connection ${ \pmb a }$ and is locally independent of the gauge transformation $\pmb { g }$ . So it depends only on the component of ${ \mathcal { G } } ( Q )$ and it turns out that

$$
\begin{array} { r } { \mathcal { C S } ( { a } ) - \mathcal { C S } ( { g } ^ { * } { a } ) = 8 \pi ^ { 2 } \deg ( g ) . } \end{array}
$$

Hence as a function on the quotient $\pmb { \mathscr { A } } ( Q ) / \pmb { \mathscr { G } } ( Q )$ the Chern-Simons functional takes values in $S ^ { 1 }$ .Note that this function is only well defined up to an additive constant which we have chosen such that $\mathcal { C S } ( a _ { 0 } ) = 0$

Denote the space of flat connections by

$$
\begin{array} { r } { A _ { \mathrm { f a t } } ( Q ) = \left\{ a \in \mathcal { A } ( Q ) : F _ { a } = 0 \right\} . } \end{array}
$$

For every flat connection $a \in { \mathcal { A } } _ { \mathrm { f a a t } } ( Q )$ there is a chain complex

$$
\Omega ^ { 0 } ( \mathfrak { g } _ { Q } ) \overset { d _ { A } } \longrightarrow \Omega ^ { 1 } ( \mathfrak { g } _ { Q } ) \overset { d _ { A } } \longrightarrow \Omega ^ { 2 } ( \mathfrak { g } _ { Q } ) \overset { d _ { A } } \longrightarrow \Omega ^ { 3 } ( \mathfrak { g } _ { Q } ) .
$$

with associated cohomology groups $H _ { \mathfrak { a } } ^ { j } ( M )$ . These cohomology groups can be identified with the spaces of harmonic forms

$$
H _ { \mathbf { a } } ^ { j } ( M ) = \ker d _ { \mathbf { a } } \cap \ker d _ { \mathbf { a } } ^ { * }
$$

where $d _ { a } ^ { * }$ denotes the $L ^ { 2 }$ -adjoint of $d _ { a } : \Omega ^ { j - 1 } \to \Omega ^ { j }$ with respect to a Riemannian metric on $M$ . A flat connection is called nondegenerate if $H _ { \mathbf { a } } ^ { 1 } ( M ) = 0$ This is consistent with the Chern-Simons point of view since the Hessian of $c s$ at a critical point $a \in \mathcal { A } _ { \mathrm { f i a t } } ( Q )$ is given by $\star d _ { a }$ and should be viewed as an operator on the quotient $\Omega ^ { 1 } ( { \mathfrak { g } } _ { Q } ) / { \mathrm { i m } } d _ { a }$ . Here $* : \Omega ^ { j }  \Omega ^ { 3 - j }$ denotes the Hodge- $^ { \cdot * }$ -operator with respect to the Riemannian metric on $M$ and the invariant inner product on $\mathfrak { g }$ ．So the flat connection $\pmb { a }$ is nondegenerate if and only if the Hessian of $c s$ at $\pmb { a }$ is invertible. Note that a flat connection $\pmb { a }$ is both regular and nondegenerate if and only if the extended Hessian

$$
D _ { a } = \left( \begin{array} { c c } { { \ast d _ { a } } } & { { d _ { a } } } \\ { { d _ { a } ^ { \ast } } } & { { 0 } } \end{array} \right)
$$

is nonsingular. Here $D _ { \pmb { a } }$ is a selfadjoint operator on $\Omega ^ { 1 } ( { \mathfrak { g } } _ { Q } ) \oplus \Omega ^ { 0 } ( { \mathfrak { g } } _ { Q } )$

Lemma 2.5 If $( H 2 )$ is satisfed then every flat connection on $Q$ is regular.

Proof: By (H2) there exists an embedding $\iota : \Sigma \to M$ of an oriented Riemann surface such that $w _ { 2 } ( \iota ^ { * } Q ) \not = 0$ .Let $a \in \mathcal { A } _ { \mathrm { f i a t } } ( Q )$ and $g \in \mathcal { G } _ { a } \cap \mathcal { G } _ { 0 } ( Q )$ Then $v ^ { * } a \in A _ { \mathrm { f i a t } } ( v ^ { * } Q )$ and $\iota ^ { * } g \in \mathcal { G } _ { \iota ^ { * } a } \cap \mathcal { G } _ { 0 } ( \iota ^ { * } Q )$ . By Lemma 4.1 below $\pmb { \iota } ^ { * } \pmb { g } = \mathbb { 1 }$ and hence $\pmb { g } = \mathbb { 1 }$ □

Remark 2.6 It is easy to construct regular fat connections with $\mathcal { G } _ { \mathfrak { a } } \neq \{ \| \}$ The holonomy of such a connection is conjugate to the abelian subgroup of diagonal matrices in $S O ( 3 )$ with diagonal entries ±1

Via the holonomy the flat connections on $Q$ correspond naturally to representations

$$
\rho : \pi _ { 1 } ( M )  { \mathrm { S O } } ( 3 ) .
$$


<!-- chunk 0002: pages 71-140 -->
The second Stiefel-Whitney class $w _ { 2 } ( Q ) \in H ^ { 2 } ( M ; { \mathbf { Z } _ { 2 } } )$ appears as the cohomology class

$$
w _ { \rho } \in H ^ { 2 } ( \pi _ { 1 } ( M ) , \mathbf { Z } _ { 2 } )
$$

associated to $\pmb { \rho }$ as follows. Choose any map $\tilde { \rho } : \pi _ { 1 } ( M ) \to \mathrm { S U } ( 2 )$ which lifts $\pmb { \rho }$ and define $w _ { \rho } ( \gamma _ { 1 } , \gamma _ { 2 } ) = \tilde { \rho } ( \gamma _ { 1 } \gamma _ { 2 } ) \tilde { \rho } ( \gamma _ { 2 } ) ^ { - 1 } \tilde { \rho } ( \gamma _ { 1 } ) ^ { - 1 } = \pm 1$ .Then ${ \pmb w } _ { \pmb \rho }$ is a cocycle:

$$
\begin{array} { r } { \partial w _ { \rho } ( \gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 } ) = w _ { \rho } ( \gamma _ { 2 } , \gamma _ { 3 } ) w _ { \rho } ( \gamma _ { 1 } \gamma _ { 2 } , \gamma _ { 3 } ) w _ { \rho } ( \gamma _ { 1 } , \gamma _ { 2 } \gamma _ { 3 } ) w _ { \rho } ( \gamma _ { 1 } , \gamma _ { 2 } ) = 1 . } \end{array}
$$

The coboundaries are functions of the form

$$
\partial f ( \gamma _ { 1 } , \gamma _ { 2 } ) = f ( \gamma _ { 1 } ) f ( \gamma _ { 1 } \gamma _ { 2 } ) f ( \gamma _ { 2 } )
$$

for some map $f : \pi _ { 1 } ( M ) \to \{ \pm 1 \}$ . Hence $w _ { \pmb { \rho } }$ is a coboundary if and only if the lift $\tilde { \rho } : \pi _ { 1 } ( M ) \to \mathrm { S U } ( 2 )$ can be chosen to be a homomorphism. The cohomology class of $w _ { \pmb { \rho } }$ is independent of the choice of the lift $\tilde { \pmb { \rho } }$ . It determines the second Stiefel-Whitney class of the bundle $Q$ via the natural homomorphism $\iota : H ^ { 2 } ( \pi _ { 1 } ( M ) , \mathbf { Z } _ { 2 } ) \to H ^ { 2 } ( M , \mathbf { Z } _ { 2 } )$

The Casson invariant $\lambda ( M ; Q )$ of the Manifold $M$ (with respect to the bundle $Q$ ） can roughly be defined as “half the number of representations $\rho : \pi _ { 1 } ( M ) \to S O ( 3 )$ with $\iota ( w _ { \rho } ) = w _ { 2 } ( Q ) ^ { \mathfrak { n } }$ or “half the number of zeros of ${ \pmb { F } } ^ { \pmb { \mathscr { n } } }$ Here the flat connections are to be counted modulo even gauge equivalence and with appropriate signs. This is analogous to the Euler number of a vector field on a finite dimensional manifold. As in finite dimensions we will in general have to perturb the 1-form $\pmb { F }$ to ensure finitely many nondegenerate zeros. In [11] Floer discovered a refinement of the Casson invariant which is called instanton homology. These homology groups result from Floer's new approach to infinite dimensional Morse theory applied to the Chern-Simons functional. The Casson invariant appears as the Euler characteristic of instanton homology.

The $L ^ { 2 }$ -gradient of the Chern-Simons functional with respect to the Riemannian metric on $M$ and the invariant inner product on $\mathfrak { g }$ is given by grad $\mathcal { C S } ( a ) = \ast F _ { a } \in \Omega ^ { 1 } ( \mathfrak { g } _ { Q } )$ . Thus a gradient flow line of the Chern-Simons functional is a smooth 1-parameter family of connections $a ( t ) \in \mathcal { A } ( Q )$ satisfying the nonlinear partial differential equation

$$
\dot { a } + * F _ { a } = 0 .
$$

The path ${ \pmb a } ( t )$ of connections on $Q$ can also be viewed as a connection on the bundle $Q \times \mathbf { R }$ over the 4-manifold $M \times \pmb { \mathrm { R } }$ .In this interpretation (3) is precisely the self-duality equation with respect to the product metric on $M \times \mathbf { R }$ Moreover,the Yang-Mill functional agrees with the fow energy

$$
\mathcal { V } \mathcal { M } ( a ) = \textstyle { \frac { 1 } { 2 } } \int _ { - \infty } ^ { \infty } \left( \left\| \dot { a } \right\| ^ { 2 } + \left\| F _ { a } \right\| ^ { 2 } \right) d t .
$$

The key obstacle for Morse theory in this context is that equation (3) does not define a well posed initial value problem and the Morse index of every critical point is infinite. In [11] Floer overcame this difficulty by studying only the space of bounded solutions of (3) and constructing a chain complex as was done by Witten [30] in finite dimensional Morse theory (see also [24]). In order to describe how this works we make another assumption on the bundle $Q$

Hypothesis (H3) Every fat connection on $Q$ is nondegenerate.

This condition will in general not be satisfied. If there are degenerate fat connections then we perturb the Chern-Simons functional in order to ensure nondegenerate critical points for the perturbed functional.

If (H3) is satisfied then for every smooth solution $a ( t ) \in \mathcal { A } ( Q )$ of (3)with finite Yang-Mils action there exist fat connections $a ^ { \pm } \in \mathcal { A } _ { \mathrm { f l a t } } ( Q )$ such that ${ \pmb a } ( t )$ converges exponentially with all derivatives to $a ^ { \pm }$ as $t$ tends to ±o (see for example [18]). Conversely,if ${ \pmb a } ( t )$ is a solution of (3) for which these limits exist then the Yang-Mills action is finite:

$$
\begin{array} { r } { \mathcal { V } M ( a ) = \mathcal { C } \mathcal { S } ( a ^ { - } ) - \mathcal { C } \mathcal { S } ( a ^ { + } ) . } \end{array}
$$

Fix two flat connections $a ^ { \pm } \in \mathcal { A } _ { \mathrm { f a t } } ( Q )$ and consider the space of those solutions $a ( t ) \in \mathcal { A } ( Q )$ of (3) which also satisfy

$$
\operatorname* { l i m } _ { t \to \pm \infty } a ( t ) = g _ { \pm } ^ { * } a ^ { \pm } , \qquad g _ { \pm } \in { \mathcal G } _ { 0 } ( Q ) .
$$

These solutions are usually termed instantons or connecting orbits from ${ \pmb a } ^ { - }$ to $a ^ { + }$ . The moduli space of these instantons is denoted by

$$
\mathcal { M } ( a ^ { - } , a ^ { + } ) = \frac { \{ a ( t ) \in \mathcal { A } ( Q ) : ( 3 ) , ( 4 ) \} } { \mathcal { G } _ { 0 } ( Q ) } .
$$

The next theorem due to Floer [11] summarizes some key properties of these moduli spaces.

Theorem 2.7 Assume $\left( H 2 \right)$ and $\left( H 3 \right)$ . For a generic metric on $M$ the moduli space $\mathcal { M } ( a ^ { - } , a ^ { + } )$ is $\pmb { a }$ finite dimensional oriented paracompact manifold for every pair of flat connections $a ^ { \pm } \in \mathcal { A } _ { \mathrm { f l a t } } ( Q )$ . There exists $\pmb { a }$ function $\mu : \mathcal { A } _ { \sf H a t } ( Q )  \pmb { \mathrm { Z } }$ such that

$$
\dim { \mathcal { M } } ( a ^ { - } , a ^ { + } ) = \mu ( a ^ { - } ) - \mu ( a ^ { + } ) .
$$

This function $\pmb { \mu }$ satisfies

$$
\mu ( a ) - \mu ( g ^ { * } a ) = 4 \deg ( g )
$$

for $a \in \mathcal { A } _ { \mathrm { f i a t } } ( Q )$ and $g \in { \mathcal { G } } ( Q )$

In our context the integer $\mu ( a )$ plays the same role as the Morse index does in finite dimensional Morse theory. The number $\mu ( a ^ { - } ) { - } \mu ( a ^ { + } )$ is given by the spectral flow [3] of the operator family $D _ { { \boldsymbol { \mathsf { a } } } ( t ) }$ as the connection $a ( t ) \in \mathcal { A } ( Q )$ runs from ${ \pmb a } ^ { - }$ to ${ \pmb a } ^ { + }$ . So the function $\mu : \mathcal { A } _ { \mathrm { f i a t } } ( Q ) \to \mathbb { Z }$ is only defined up to an additive constant. We will choose this constant such that $\mu ( a _ { 0 } ) = 0$ where $a _ { 0 } \in \mathcal { A } _ { \mathrm { f i a t } } ( Q )$ is a fixed flat connection.

To construct the instanton homology groups we can now proceed as in finite dimensional Morse theory [30]. The key idea is to construct a chain complex over the flat connections and to use the instantons to construct a boundary operator. For simplicity of the exposition we restrict ourselves to coefficients in $\mathbf { Z _ { 2 } }$

Let $c$ be the vector space over $\mathbf { Z _ { 2 } }$ generated by the flat connections modulo gauge equivalence. For now we divide only by the component of the identity ${ \mathcal { G } } _ { 0 } ( Q )$ . This vector space is graded by $\pmb { \mu }$ .It follows from Uhlenbeck's compactness theorem [28] that the space

$$
C _ { k } = \bigoplus _ { \substack { a \in A _ { \mathrm { f i a t } } ( Q ) / \sigma _ { 0 } ( Q ) } } \mathbf { Z } _ { 2 } \langle a \rangle
$$

is finite dimensional for every integer $\pmb { k }$ . It follows also from Uhlenbeck's compactness theorem that the moduli space $\mathcal { M } ( a ^ { - } , a ^ { + } )$ consists of finitely many instantons (modulo time shift) whenever

$$
\mu ( a ^ { - } ) - \mu ( a ^ { + } ) = 1 .
$$

Let $n _ { 2 } ( a ^ { - } , a ^ { + } )$ denote the number of such instantons, counted modulo 2. These numbers determine a linear map $\partial : C _ { k + 1 }  C _ { k }$ defined by

$$
\partial \langle b \rangle = \sum _ { \mu ( a ) = k } n _ { 2 } ( b , a ) \langle a \rangle
$$

for $b \in { \mathcal { A } } _ { \mathtt { f l a t } } ( Q )$ with $\mu ( b ) = k + 1$ .In [11] Floer proved that $( C , \partial )$ is a chain complex and that its homology is an invariant of the bundle $Q  M$

Theorem 2.8 Assume (H2) and $( H 3 )$

(1) The above map $\partial : C \to C$ satisfies $\partial ^ { 2 } = 0$ . The associated homology groups

$$
H F _ { k } ^ { \mathrm { i n s t } } ( M ; Q ) = { \frac { \ker \partial _ { k - 1 } } { \mathrm { i m } \partial _ { k } } }
$$

are called the Floer homology groups of the pair $( M , Q )$ ·

(2) The Floer homology groups $H F _ { k } ^ { \mathrm { i n s t } } ( M ; Q )$ are independent of the metric on M used to construct them.

To prove $\pmb { \partial } ^ { 2 } = \pmb { 0 }$ we must show that

$$
\sum _ { b \in A _ { \underset { \mu ( b ) = k } { \prod _ { a , t } ( Q ) } / \mathcal { Q } _ { 0 } ( Q ) } } n _ { 2 } \big ( c , b \big ) n _ { 2 } \big ( b , a \big ) \quad \in \quad 2 \mathbf { Z }
$$

whenever $\pmb { \mu } ( \pmb { a } ) = \pmb { k } - \pmb { 1 }$ and $\mu ( { \mathsf { c } } ) = k + 1$ . This involves a glueing argument for pairs of instantons running from $^ { \pmb { c } }$ to $\pmb { b }$ and from $\pmb { b }$ to a. Such a pair gives rise to a (unique) 1-parameter family of instantons running from c to $\pmb { a }$ . Now the space of instantons running from c to $\pmb { a }$ (modulo time shift） is a 1-dimensional manifold and has therefore an even number of ends. This implies $\partial ^ { 2 } = 0$ . That any two instanton homology groups corresponding to different metrics are naturally isomorphic can be proved along similar lines.

Remark 2.9 (i) The Floer homology groups $H F _ { * } ^ { \mathrm { i n s t } } ( M ; Q )$ are new invariants of the 3-manifold $\pmb { M }$ which cannot be derived from the classical invariants of differential topology.

(ii) The Floer homology groups are graded modulo 4. From Lemma 2.3 it follows that there exists a gauge transformation $g \in { \mathcal { G } } ( Q )$ of degree 1 and by Theorem 2.7 the map $a \mapsto g ^ { * } a$ induces an isomorphism

$$
H F _ { k + 4 } ^ { \mathrm { i n s t } } ( M ; Q ) = H F _ { k } ^ { \mathrm { i n s t } } ( M ; Q ) .
$$

Note however that the even gauge transformations $g \in { \mathcal { G } } ^ { \mathrm { e v } } ( Q )$ only give rise to a grading modulo 8. So the Euler characteristic of $H F _ { * } ^ { \mathrm { i n s t } } ( M ; Q )$ is the number

$$
\begin{array} { r c l } { { \chi ( H F _ { * } ^ { \mathrm { i n s t } } ( M ; Q ) ) } } & { { = } } & { { \displaystyle \sum _ { k = 0 } ^ { 3 } ( - 1 ) ^ { k } \mathrm { d i m } H F _ { k } ^ { \mathrm { i n s t } } ( M ; Q ) } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \sum _ { a \in A _ { \mathrm { f a t } } ( Q ) / \mathcal { G } ^ { \mathrm { e v } } ( Q ) } ( - 1 ) ^ { \mu ( a ) } . } } \end{array}
$$

This is the Casson invariant $\lambda ( M ; Q )$ ·

(iii) By Lemma 2.3 the group of components of the space of degree-0 gauge transformations $\{ g \in { \mathcal { G } } ( Q ) : \deg ( g ) = 0 \}$ is isomorphic to the finite group

$$
\Gamma = \{ \eta ( g ) : g \in \mathcal { G } ( Q ) , \deg ( g ) = 0 \} \subset H ^ { 1 } ( M ; \mathbf { Z } _ { 2 } ) .
$$

This group acts on $H F _ { k } ^ { \mathrm { i n s t } } ( M ; Q )$ for every $\pmb { k }$ through permutations of the canonical basis.By Remark 2.6 the group $\mathbf { r }$ does not act freely. The above definition of the Casson invariant ignores this action of $\mathbf { r }$ (iv） The same construction works over the integers.For this we must assign a number $+ 1$ or $^ { - 1 }$ to each instanton running from ${ \pmb a } ^ { - }$ to ${ \pmb a } ^ { + }$ whenever $\mu ( a ^ { - } ) - \mu ( a ^ { + } ) = 1$ . This involves a consistent choice of orientations for the Moduli spaces $\mathcal { M } ( a ^ { - } , a ^ { + } )$

(v)If Hypothesis (H3) is violated then the Floer homology groups can still be defined. The construction then requires a suitable perturbation of the Chern-Simons functional. This will be discussed in Section 7.   
(vi) It represents a much more serious problem if Hypothesis (H2) fails. This is because of the presence of flat connections which are not regular. Such connections cannot be removed by a gauge invariant perturbation.   
(vii) If $Q$ is the trivial $S O ( 3 )$ -bundle over a homology-3-sphere $M$ then the only flat connection which is not regular is the trivial connection. In this case the difficulty mentioned in (vi) does not arise.This is in fact the context of Floer's original work on instanton homology [11].

# 3Floer homology for symplectic fixed points

In [12] Floer developed a similar theory for fixed points of symplectomorphisms.In his original work Floer assumed that the symplectomorphism $\phi$ is exact and he proved that the Floer homology groups $H F _ { * } ^ { \mathrm { s y m p } } ( \mathcal { M } , \phi )$ are isomorphic to the homology of the underlying symplectic manifold $( M , \omega )$ · Like Floer we assume that $\mathcal { M }$ is compact and monotone. This means that the first Chern class $\mathbf { c _ { 1 } }$ of $\pmb { T } \pmb { M }$ agrees over $\pmb { \pi _ { 2 } ( M ) }$ with the cohomology class of the symplectic form $\pmb { \omega }$ . Unlike Floer we assume in addition that $\mathcal { M }$ is simply connected but we do not require the symplectomorphism $\phi : \mathcal { M } \to \mathcal { M }$ to be isotopic to the identity. Then there are Floer homology groups of $\phi$ whose Euler characteristic is the Lefschetz number.Here is how this works.

The fixed points of $\phi$ can be represented as the critical points of a function on the space of smooth paths

$$
\Omega _ { \phi } = \left\{ \gamma : \mathsf { R } \to \mathcal { M } : \gamma ( s + 1 ) = \phi ( \gamma ( s ) ) \right\} .
$$

The tangent space to $\Omega _ { \phi }$ at $\gamma$ is the space of vector fields $\xi ( s ) \in T _ { \gamma ( s ) } {  { \mathcal { M } } }$ along $\pmb { \gamma }$ such that $\xi ( s + 1 ) = d \phi ( \gamma ( s ) ) \xi ( s )$ . The space $\Omega _ { \phi }$ carries a natural 1-form

$$
T _ { \gamma } \Omega _ { \phi }  \mathbb { R } : \xi \mapsto - \int _ { \gamma } \iota ( \xi ) \omega .
$$

This 1-form is closed but not exact since $\Omega _ { \phi }$ is not simply connected.Since $\mathcal { M }$ is simply connected the fundamental group of $\Omega _ { \phi }$ is $\pi _ { 1 } ( \Omega _ { \phi } ) = \pi _ { 2 } ( { \mathcal { M } } )$ .The universal cover $\tilde { \Omega } _ { \phi }$ can be explicitly represented as the space of homotopy classes of smooth maps $u : \mathbb { R } \times I  \mathcal { M }$ such that

$$
u ( s , 0 ) = x _ { 0 } , \qquad u ( s + 1 , t ) = \phi ( u ( s , t ) ) , \qquad u ( s , 1 ) = \gamma ( s ) .
$$

Here ${ \pmb x _ { 0 } = \phi ( \pmb x _ { 0 } ) }$ is a reference point chosen for convenience of the notation. The homotopy class $[ \pmb { u } ]$ is to be understood subject to the boundary condition at $t \ : = \ : 0$ and $t = 1$ .The second homotopy group $\pmb { \pi _ { 2 } ( \mathcal { M } ) }$ acts on $\tilde { \Omega } _ { \phi }$ by taking connected sums.A sphere in $\mathcal { M }$ can be represented by a function ${ \pmb v }$ ： $\mathbb { R } \times I  { \mathcal { M } }$ such that $v ( s , 0 ) = v ( s , 1 ) = v ( 0 , t ) = x _ { 0 }$ and $v ( s + 1 , t ) = v ( s , t )$ for $s , t \in \mathbb { R }$ . The connected sum of $[ u ] \in \tilde { \Omega } _ { \phi }$ and $[ v ] \in \pi _ { 2 } ( { \mathcal { M } } )$ is given by $\boldsymbol { u } \# \boldsymbol { v } ( s , t ) = \boldsymbol { v } ( 2 t , s )$ for $t \leq 1 / 2$ and $u \# v ( s , t ) = u ( 2 t - 1 , s )$ for $t \geq 1 / 2$ ·

The pullback of the above 1-form on $\Omega _ { \phi }$ is the differential of the function

$$
\widetilde { a } _ { \phi } : \widetilde { \Omega } _ { \phi }  \mathbb { R } , \qquad \widetilde { a } _ { \phi } ( u ) = \int u ^ { * } \omega
$$

called the symplectic action. This function satisfies

$$
\widetilde { a } _ { \phi } ( u \# v ) = \widetilde { a } _ { \phi } ( u ) + \int _ { S ^ { 2 } } v ^ { * } w
$$

for every sphere $v : S ^ { 2 } \to { \mathcal { M } }$ Since $\mathcal { M }$ is monotone the symplectic form $\pmb { \omega }$ is integral and hence $\widetilde { \pmb { a } } _ { \phi }$ descends to a map $a _ { \phi } : \Omega _ { \phi } \to \mathbb { R } / \mathbb { Z }$ .By construction the diferential of ${ \pmb a } _ { \phi }$ is the above 1-form on $\Omega _ { \phi }$ . So the critical points of ${ \pmb a } _ { \phi }$ are the constant paths in $\Omega _ { \phi }$ and hence the fixed points of $\phi$

An almost complex structure $J : T { \cal M }  T { \cal M }$ is said to be compatible with $\omega$ if the bilinear form

$$
\langle \xi , \eta \rangle = \omega ( \xi , J \eta )
$$

defines a Riemannian metric on $\mathcal { M }$ . The space $\mathcal { I } ( M , \omega )$ of such almost complex structures is contractible. A symplectomorphism $\phi$ acts on $\mathcal { I } ( M , \omega )$ by pulback $J \mapsto \phi ^ { * } J$ . To construct a metric on $\Omega _ { \phi }$ choose a smooth family $J _ { s } \in \mathcal { I } ( M , \omega )$ such that

$$
J _ { s } = \phi ^ { * } J _ { s + 1 } .
$$

This condition guarantees that for any two vectorfields $\xi , \eta \in T _ { \gamma } \Omega _ { \phi }$ the expression $\langle \xi ( s ) , \eta ( s ) \rangle _ { s } = \omega ( \xi ( s ) , J _ { s } ( \gamma ( s ) ) \eta ( s ) )$ is of period 1 in $\pmb { \mathscr { s } }$ . Hence define the inner product of $\pmb { \xi }$ and $\pmb { \eta }$ by

$$
\langle \xi , \eta \rangle = \int _ { 0 } ^ { 1 } \langle \xi ( s ) , \eta ( s ) \rangle _ { s } d s .
$$

The gradient of ${ \pmb a } _ { \phi }$ with respect to this metric on $\Omega _ { \phi }$ is given by grad $a _ { \phi } ( \gamma ) =$ $J _ { s } ( \gamma ) \dot { \gamma }$ . Hence a gradient flow line of ${ \pmb a } _ { \phi }$ is a smooth map $u : \mathbb { R } ^ { 2 } \to \mathcal { M }$ satisfying the nonlinear partial differential equation

$$
\frac { \partial u } { \partial t } + J _ { s } ( u ) \frac { \partial u } { \partial s } = 0
$$

and the periodicity condition

$$
u ( s + 1 , t ) = \phi ( u ( s , t ) ) .
$$

Condition (5) guarantees that whenever $\pmb { u } ( s , t )$ is a solution of (6) then so is $v ( s , t ) = \phi ( u ( s - 1 , t ) )$ . Condition (7) requires that these two solutions agree.

As in section 2 equations (6) and (7) do not define a well posed Cauchy problem and the Morse index of any critical point is infinite.However, the solutions of (6) are precisely Gromov's pseudoholomorphic curves [16]. It follows from Gromov's compactness that every solution of (6) and (7) with finite energy

$$
E ( u ) = \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } \int _ { 0 } ^ { 1 } \left( | \partial _ { s } u | _ { s } ^ { 2 } + | \partial _ { t } u | _ { s } ^ { 2 } \right) d s d t < \infty
$$

has limits

$$
\operatorname* { l i m } _ { t  \pm \infty } u ( s , t ) = x ^ { \pm } = \phi ( x ^ { \pm } ) .
$$

(See for example [24],[31].) Conversely,any solution of (6),(7),and (8) has finite energy. Given any two fixed points $x ^ { \pm }$ let

$$
\mathbf { \mathcal { M } } ( \mathbf { \mathcal { x } } ^ { - } , \mathbf { \mathcal { x } } ^ { + } )
$$

denote the space of these solutions.

For any function $u : \mathbb { R } ^ { 2 } \to { \mathcal { M } }$ which satisfies (7) and (8) we introduce the Maslov index as follows.Let $\Phi ( s , t ) : \mathbb { R } ^ { 2 n }  T _ { u ( s , t ) } \mathcal { M }$ be a trivialization of $\pmb { u } ^ { \ast T M }$ as a symplectic vector bundle such that

$$
\Phi ( s + 1 , t ) = d \phi ( u ( s , t ) ) \Phi ( s , t ) .
$$

Consider the paths of symplectic matrices $\Psi ^ { \pm } ( s ) = \Phi ( s , \pm \infty ) ^ { - 1 } \Phi ( 0 , \pm \infty )$ These satisfy $\Psi ^ { \pm } ( 0 ) = \mathbb { 1 }$ and $\Psi ^ { \pm } ( 1 )$ is conjugate to $d \phi ( x ^ { \pm } )$ . In particular 1 is not an eigenvalue of $\Psi ^ { \pm } ( 1 )$ . The homotopy class of such a path is determined by its Maslov index $\mu ( \Psi ^ { \pm } ) \in \mathbb { Z }$ introduced by Conley and Zehnder [5]. Roughly speaking the Maslov index counts the number of times $\pmb { \mathscr { s } }$ such that 1 is an eigenvalue of the symplectic matrix $\Psi ^ { \pm } ( s )$ . The integer

$$
\mu ( u ) = \mu ( \Psi ^ { - } ) - \mu ( \Psi ^ { + } )
$$

is independent of the choice of the trivialization and is called the Maslov index of $\pmb { u }$ . This number depends only on the homotopy class of $\pmb { u }$ .For a detailed account of the Maslov index and its role in Floer homology we refer to [25]. The next theorem is due to Floer [12].

Lemma 3.1 If $\pmb { u }$ satisfies (7) and (8) then

$$
\mu ( u \# v ) = \mu ( u ) + 2 \int _ { S ^ { 2 } } v ^ { * } c _ { 1 }
$$

for any sphere $v : S ^ { 2 } \to { \mathcal { M } }$

Theorem 3.2 For a generic family of almost complex structures satisfying (5) the space $\mathcal { M } ( x ^ { - } , x ^ { + } )$ is a finite dimensional manifold for every pair of fixed points $x ^ { \pm } = \phi ( x ^ { \pm } )$ . The dimension of $\mathcal { M } ( x ^ { - } , x ^ { + } )$ is given by the Maslov index

$$
\dim _ { u } { \mathcal { M } } ( x ^ { - } , x ^ { + } ) = \mu ( u )
$$

locally near $u \in \mathcal { M } ( x ^ { - } , x ^ { + } )$ ·

By Lemma 3.1 the Maslov index induces a map

$$
\mu : \mathrm { F i x } ( \phi ) \to \mathbb { Z } _ { 2 N }
$$

such that $\mu ( u ) = \mu ( x ^ { - } ) { - } \mu ( x ^ { + } ) ( \mathrm { m o d } 2 N )$ for every solution $\pmb { u }$ of (7) and (8). Here the integer $N$ is defined by $\mathsf { c } _ { 1 } ( \pi _ { 2 } ( \mathcal { M } ) ) = N \mathbf { Z }$ This function $\pmb { \mu }$ ： $\mathbb { F } \mathrm { i x } ( \phi )  \mathbb { Z } _ { 2 N }$ is only defined up to an additive constant. We may choose this constant such that

$$
( - 1 ) ^ { \mu ( x ) } = \mathrm { s i g n } \operatorname* { d e t } ( \mathbb { 1 } - d \phi ( x ) )
$$

for every fixed point ${ \pmb x } = \phi ( { \pmb x } )$ . The manifold $\mathcal { M } ( x ^ { - } , x ^ { + } )$ is not connected and the dimension depends on the component. It follows from Theorem 3.2 that the dimension is well defined modulo $2 N$

$$
\dim { \mathcal { M } } ( x ^ { - } , x ^ { + } ) = \mu ( x ^ { - } ) - \mu ( x ^ { + } ) { \mathrm { ~ ( m o d ~ } } 2 N ) .
$$

The Floer homology groups of $\phi$ can now be constructed as follows. Let $c$ be the vector space over $\mathbf { Z _ { 2 } }$ freely generated by the fixed points of $\phi$ This vector space is graded modulo $2 N$ by the Maslov index. It is convenient to define

$$
\begin{array} { c c } { { C _ { k } = } } & { { \bigoplus _ { z = \phi ( z ) \atop \mu ( z ) = k ( \mathrm { m o d } \ 2 N ) } { \bf { Z } } _ { 2 } \langle { \bf { \Psi } } x \rangle } } \end{array}
$$

for every integer $\pmb { k }$ keeping in mind that $C _ { k + 2 N } = C _ { k }$ . Since $\mathcal { M }$ is monotone it follows from Gromov's compactness for pseudoholomorphic curves that the 1-dimensional part of the space $\mathcal { M } ( x ^ { - } , x ^ { + } )$ consists of finitely many connecting orbits (modulo time shift） whenever $\mu ( x ^ { - } ) - \mu ( x ^ { + } ) = 1 ( \mathrm { m o d } 2 N )$ . Let $n _ { 2 } ( x ^ { - } , x ^ { + } )$ be the number of these connecting orbits modulo 2. This gives a linear map $\partial : C _ { k + 1 }  C _ { k }$ via the formula

$$
\partial \langle y \rangle = \sum _ { \begin{array} { c } { { x = \phi ( x ) } } \\ { { \mu ( x ) = k ( \mathrm { m o d } ~ 2 N ) } } \end{array} } n _ { 2 } ( y , x ) \langle x \rangle
$$

for ${ y } = \phi ( { y } )$ with $\mu ( y ) = k + 1 ( \mathrm { m o d } ~ 2 N )$ . In [12] Floer proved that $( C , \partial )$ is a chain complex.

Theorem 3.3 Assume that $\mathcal { M }$ is simply connected and monotone.

(1) The above map $\partial : C \to C$ satisfes $\partial ^ { 2 } = 0$ . The associated homology groups

$$
H F _ { k } ^ { \mathrm { s y m p } } ( { \cal M } ; \phi ) = { \frac { \ker \partial _ { k - 1 } } { \mathrm { i m } \partial _ { k } } }
$$

are called the Floer homology groups of the pair $( M , \phi )$ ·

(2) The Floer homology groups $H F _ { k } ^ { \mathrm { s y m p } } ( \mathcal { M } , \phi )$ are independent of the almost complex structure $\pmb { J }$ used to construct them; they depend on $\phi$ only up to symplectic isotopy.

(3）If $\dot { \phi }$ is isotopic to the identity in the class of symplectomorphisms then the Floer homology groups of $\phi$ are naturally isomorphic to the homology of the manifold M

$$
H F _ { k } ^ { \mathrm { s y m p } } ( { \cal M } ; \phi ) = \bigoplus _ { j = k ( \mathrm { m o d } \ 2 N ) } H _ { j } ( { \cal M } ; { \bf Z } _ { 2 } ) .
$$

Proof of (2): To prove that $H F _ { * } ^ { \mathrm { s y m p } } ( \mathcal { M } ; \phi )$ depends only on the isotopy class of $\phi$ we must generalize the above construction. Let

$$
\phi _ { s } = \psi _ { s } ^ { - 1 } \circ \phi
$$

be an isotopy of symplectomorphisms from $\phi _ { \mathbf { 0 } } = \phi$ to $\phi _ { 1 }$ . Since $\mathcal { M }$ is simply connected there exists a family of Hamiltonian vector fields $X _ { s } : { \mathcal { M } } \to T { \mathcal { M } }$ such that

$$
{ \frac { d } { d s } } \psi _ { s } = X _ { s } \circ \psi _ { s } .
$$

This means that the 1-form obtained by contracting $X _ { s }$ with the symplectic form $\pmb { \omega }$ is exact

$$
\iota ( X _ { s } ) \omega = d H _ { s } .
$$

The isotopy can be chosen such that

$$
\psi _ { s + 1 } \circ \phi _ { 1 } = \phi _ { 0 } \circ \psi _ { s }
$$

or equivalently

$$
\phi ^ { * } X _ { s + 1 } = X _ { s } , \qquad H _ { s + 1 } \circ \phi = H _ { s } .
$$

Now replace equation (6) by

$$
\frac { \partial u } { \partial t } + J _ { s } ( u ) \frac { \partial u } { \partial s } - \nabla H _ { s } ( u ) = 0 .
$$

Here $\nabla H _ { s } = J _ { s } \boldsymbol { X } _ { s }$ is the gradient of the Hamiltonian function $H _ { s } : \mathcal { M }  \mathbb { R }$ with respect to the metric induced by $J _ { s }$ .It follows from (5) that whenever $u ( s , t )$ is a solution of (11) then so is $v ( s , t ) = \phi ( u ( s - 1 , t ) )$ . Hence the periodicity condition (7) is consistent with (11). One can prove by exactly the same arguments as in [12] that $H F _ { * } ^ { \mathrm { s y m p } } ( \mathcal { M } ; \phi )$ is isomorphic to the Floer homology constructed with (11) instead of (6).We denote these Floer homology groups by $H F _ { * } ^ { \mathrm { s y m p } } ( { \cal M } ; \phi , { \cal H } )$

The stationary points of equation (11) (that is ${ \partial } u / { \partial t } = 0 ,$ ）with the boundary condition (7） are the paths $\gamma \in \Omega _ { \phi }$ for which $\gamma ( s ) = \psi _ { s } ( \gamma ( 0 ) )$ These paths are in one-to-one correspondence with the fixed points of $\phi _ { 1 } =$ $\psi _ { 1 } ^ { - 1 } \phi$ . Now let $u : \mathbb { R } ^ { 2 } \to { \mathcal { M } }$ be any solution of (11) and (7) and define

$$
v ( s , t ) = \psi _ { s } ^ { - 1 } ( u ( s , t ) ) , \qquad I _ { s } = \psi _ { s } ^ { * } J _ { s } .
$$

Then $\phi _ { 1 } { ^ * I _ { s + 1 } } = I _ { s }$ and $\boldsymbol { v } ( \boldsymbol { s } , t )$ satisfies the partial differential equation

$$
\frac { \partial v } { \partial t } + I _ { s } ( v ) \frac { \partial v } { \partial s } = 0
$$

and the periodicity condition

$$
v ( s + 1 , t ) = \phi _ { 1 } ( v ( s , t ) ) .
$$

Hence there is a one-to-one correspondence between the solutions of (11) and (7) on the one hand and the solutions of (12) and (13) on the other hand. This shows that $H F _ { * } ^ { \mathrm { s y m p } } ( { \cal M } ; \phi , { \cal H } )$ is isomorphic to $H F _ { * } ^ { \mathrm { s y m p } } ( \mathcal { M } ; \phi _ { 1 } )$

Remark 3.4 (i) A similar construction works for monotone symplectic manifolds $\mathcal { M }$ which are not simply connected. In this case $\Omega _ { \phi }$ will no longer be connected and there are Floer homology groups for every homotopy class of paths. Moreover, the fundamental group of $\Omega _ { \phi }$ will no longer be isomorphic to $\pmb { \pi _ { 2 } ( M ) }$ and ${ \pmb a } _ { \phi }$ may not take values in $S ^ { 1 }$ . If this is the case then the Floer homology groups will be modules over a suitable Novikov ring as in [17]. Finally,not every isotopy of symplectomorphisms corresponds to a time dependent Hamiltonian vector field but the Floer homology groups will only be invariant under Hamiltonian isotopy.

(ii) In [17] the construction of the Floer homology groups has been generalized to some classes of non-monotone symplectic manifolds. The results in [17] include the case where the first Chern class $c _ { 1 }$ vanishes over $\pmb { \pi _ { 2 } ( M ) }$ but $\omega$ does not. In this case the Floer homology groups are modules over the Novikov ring associated to the ordering on $\pmb { \pi _ { 2 } ( M ) }$ determined by $\omega$

(iii) Theorem 3.3 implies the Arnold conjecture for simply connected monotone symplectic manifolds $\mathcal { M }$ : If $\phi$ is the time-l-map of a time dependent Hamiltonian vector feld with nondegenerate fixed points then the number of fixed points of $\phi$ can be estimated below by the sum of the Betti numbers.In [12] Floer proved this result without assuming $\mathcal { M }$ to be simply connected.

(iv) It follows from (9) that the Euler characteristic of $H F _ { * } ^ { \mathrm { s y m p } } ( \mathcal { M } ; \phi )$ is the Lefschetz number of $\phi$

$$
\begin{array} { l l l } { \displaystyle \chi ( H F _ { k } ^ { \mathrm { s y m p } } ( { \mathcal M } ; { \phi } ) ) } & { = } & { \displaystyle \sum _ { k = 0 } ^ { 2 N - 1 } ( - 1 ) ^ { k } \dim H F _ { k } ^ { \mathrm { s y m p } } ( { \mathcal M } ; { \phi } ) } \\ & { = } & { \displaystyle \sum _ { x = \phi ( x ) } \mathrm { s i g n } \operatorname* { d e t } ( \mathbb { 1 } - d \phi ( x ) ) } \\ & { = } & { L ( \phi ) . } \end{array}
$$

# 4Flat connections over a Riemann surface

Let $\pi : P \to \Sigma$ be principal $S O ( 3 )$ -bundle over a compact oriented Riemann surface $\pmb { \Sigma }$ of genus $\pmb { k }$ .Up to isomorphism there are only two such bundles characterized by the second Stiefel-Whitney class. We assume $w _ { 2 } ( P ) = 1$ so the bundle is nontrivial. As in section 1 let $A ( P )$ denote the space of connections on $P$ and ${ \mathcal { G } } ( P )$ denote the group of gauge transformations. The component of the identity

$$
{ \mathcal { G } } _ { 0 } ( P ) = \{ g \in { \mathcal { G } } ( P ) : g \sim 1 \}
$$

can be characterized as the subgroup of even gauge transformation that is those which lift to $S U ( 2 )$ . Alternatively ${ \mathcal { G } } _ { 0 } ( P )$ can be described as the kernel of the epimorphism $\eta : \mathcal { G } ( P ) \to H ^ { 1 } ( \Sigma ; \mathbf { Z } _ { 2 } )$ which,as in section 1,assigns to each gauge transformation its parity $\pmb { \eta } ( \pmb { g } )$ . Here $\pmb { \eta }$ induces an isomorphism from the group of components of ${ \mathcal { G } } ( P )$ to $H ^ { 1 } ( \Sigma ; \mathbb { Z } _ { 2 } ) \approx { \mathbb Z } _ { 2 } ^ { 2 k }$

Recall from [2] that the affine space $A ( P )$ is an infinite dimensional symplectic manifold with symplectic form

$$
\omega _ { A } ( a , b ) = \int _ { \Sigma } \langle a \wedge b \rangle
$$

for $a , b \in \displaystyle T _ { A } A ( P ) = \Omega ^ { 1 } ( \mathfrak { g } _ { P } )$ . The gauge group $\mathcal { G } _ { \bf 0 } ( P )$ acts on this manifold by symplectomorphisms.The Lie algebra $\mathrm { L i e } ( \mathcal { G } _ { 0 } ( P ) ) = \Omega ^ { 0 } ( { \mathfrak { g } } _ { P } )$ acts by Hamiltonian vector ffelds $\mathcal { A } ( P )  \Omega ^ { 1 } ( { \mathfrak { g } } _ { P } ) : A \mapsto d _ { A } \xi$ where $\pmb { \xi } \in \Omega ^ { 0 } ( \{ \mathfrak { g } q \}$ . The associated Hamiltonian functions are $\begin{array} { r } { A ( P )   { \mathbb { R } } : A \mapsto \int _ { \Sigma } \langle F _ { A } \wedge \xi \rangle } \end{array}$ . Thus the curvature

$$
\mathcal { A } ( P ) \mapsto \Omega ^ { 2 } \left( \mathfrak { g } _ { P } \right) : A \mapsto F _ { A }
$$

is the moment map and the corresponding Marsden-Weinstein quotient is the moduli space

$$
\mathcal { M } ( P ) = \mathcal { A } _ { \mathrm { d a t } } ( P ) / \mathcal { G } _ { 0 } ( P ) .
$$

of flat connections modulo even gauge equivalence.

Since $P$ is the nontrivial SO(3)-bundle the space $M ( P )$ is a compact manifold of dimension $\pmb { 6 } \pmb { k } - \pmb { 6 }$ provided that $k \geq 2$ .Moreover, every conformal structure on $\pmb { \Sigma }$ induces a Kahler structure on $M ( P )$ . To see this consider the DeRham complex

$$
\Omega ^ { 0 } ( \mathfrak { g } _ { P } ) \xrightarrow { d _ { A } } \Omega ^ { 1 } ( \mathfrak { g } _ { P } ) \xrightarrow { d _ { A } } \Omega ^ { 2 } \bigl ( \mathfrak { g } _ { P } \bigr )
$$

twisted by a flat connection $\pmb { A }$ . It follows from Lemma 4.1 below that $d _ { A }$ ： $\Omega ^ { 0 } \to \Omega ^ { 1 }$ is injective and hence $H _ { A } ^ { 0 } ( \Sigma ) = 0$ . The first cohomology $H _ { A } ^ { 1 } ( \Sigma ) =$ ker $d _ { A } \cap d _ { A } ^ { * } \subset \Omega ^ { 1 } ( { \mathfrak { g } } _ { P } )$ appears as the tangent space of the manifold $M ( P )$ at $\pmb { A }$ . A conformal structure on $\pmb { \Sigma }$ determines a Hodge-\*-operator

$$
H _ { A } ^ { 1 } ( \Sigma ) \to H _ { A } ^ { 1 } ( \Sigma ) : a \mapsto * a
$$

for $A \in { \mathcal { A } } _ { \mathrm { f i a t } } ( P )$ . These operators form an integrable complex structure on $M ( P )$ which is compatible with the symplectic form (14) The associated Kahler metric is given by

$$
\langle a , b \rangle = \int _ { \Sigma } \langle a \wedge * b \rangle
$$

for $a , b \in H _ { A } ^ { 1 } ( \Sigma )$

Via the holonomy the space $M ( P )$ can be identifed with the space of odd representations of the fundamental group of $P$ in SU(2):

$$
\mathscr { M } ( P ) = \frac { \mathrm { H o m } ^ { \mathrm { o d d } } ( \pi _ { 1 } ( P ) , \mathrm { S U } ( 2 ) ) } { \mathrm { S U } ( 2 ) } .
$$

More precisely, since ${ \mathfrak { g } } = { \mathfrak { s o } } ( 3 ) = { \mathfrak { s u } } ( 2 )$ the holonomy of a fat connection $A \in { \mathcal { A } } _ { \mathrm { f i a t } } ( P )$ at a point $p _ { 0 } \in P$ determines a homomorphism $\rho _ { A } : \pi _ { 1 } ( P ) \to$ SU(2)whose image is denoted by $H _ { A } ( p _ { 0 } ) \ = \ \rho _ { A } ( \pi _ { 1 } ( P ) )$ .Since $P$ is the nontrivial bundle its fundamental group is given by $2 k + 1$ generators

$$
\alpha _ { 1 } , \ldots \alpha _ { k } , \beta _ { 1 } , \ldots , \beta _ { k } , \varepsilon
$$

with relations

$$
\prod _ { j = 1 } ^ { k } [ \alpha _ { j } , \beta _ { j } ] = \varepsilon , \quad [ \alpha _ { j } , \varepsilon ] = 1 , \quad [ \beta _ { j } , \varepsilon ] = 1 , \quad \varepsilon ^ { 2 } = 1 .
$$

A homomorphism $\rho : \pi _ { 1 } ( P ) \to \mathrm { S U } ( 2 )$ is called odd if $\rho ( \varepsilon ) = - 1$ . Any such homomorphism is given by a $\mathbf { 2 } k$ -tuple of matrices $U _ { j } , V _ { j } \in \mathrm { S U } ( 2 )$ such that

$$
\prod _ { j = 1 } ^ { k } [ U _ { j } , V _ { j } ] = - 1
$$

The space of conjugacy classes of such homomorphisms is easily seen to be a compact manifold of dimension $6 k - 6$ . In particular, every flat connection on $P$ is regular.

Lemma 4.1 If $A \in { \mathcal { A } } _ { \mathrm { f l a t } } ( P )$ then $\mathcal { G } _ { A } \cap \mathcal { G } _ { 0 } ( P ) = \{ 1 \}$

Proof: Let $g \in \mathcal { G } _ { A } \cap \mathcal { G } _ { 0 } ( P )$ and let $\tilde { \pmb { g } } :  { \boldsymbol { P } }  \mathbf { S }  { \mathbf { U } } ( 2 )$ be a lift of $\pmb { g }$ . Then $\tilde { \pmb { g } } ( p _ { \mathbf { 0 } } )$ commutes with $H _ { A } ( p _ { 0 } )$ .By the above discussion $H _ { A } ( p _ { 0 } )$ is not an abelian subgroup of SU(2). Hence $\tilde { g } ( p _ { 0 } ) = \pm \mathbb { 1 }$ and $\begin{array} { r } { g ( p _ { 0 } ) = \mathbb { 1 } } \end{array}$ □

The topology of the moduli space $M ( P )$ has been studied extensively by Atiyah and Bott [2] and Newsteadt [21]. We recall those results which are of interest to us.

Theorem 4.2 Assume $k \geq 2$ . The moduli space $M ( P )$ is connected and simply connected and $\pi _ { 2 } ( { \mathcal { M } } ( P ) ) = { \pmb { \mathbb { Z } } }$ ·

It is easy to see that $M ( P )$ is connected for $k \geq 1$ and simply connected for $k \geq 2$ [21]. Define

$$
R _ { k } : \operatorname { S U } ( 2 ) ^ { 2 k } \to \operatorname { S U } ( 2 ) : ( U _ { 1 } , \ldots , U _ { k } , V _ { 1 } , \ldots , V _ { k } ) \mapsto \prod _ { j = 1 } ^ { k } [ U _ { j } , V _ { j } ] .
$$

A $\pmb { 2 k }$ -tuple in $X _ { k } = \mathbf { S } \mathbf { U } ( 2 ) ^ { 2 k }$ is a singular point for $R _ { k }$ if and only if all $\mathbf { 2 } k$ matrices commute. Hence the set $S _ { k }$ of singular points is a $( 2 k + 2 )$ dimensional stratified subvariety of $Z _ { k } = { R _ { k } } ^ { - 1 }$ (1).Hence there is a fibration $R _ { k } : X _ { k } \setminus \mathcal { Z } _ { k } \to \operatorname { S U } ( 2 ) \setminus \{ 1 \}$ with fibre $F _ { k } = { R _ { k } } ^ { - 1 } { \left( - \mathbb { 1 } \right) }$ over a contractible base. The space $X _ { k } \setminus Z _ { k }$ is connected for $k \geq 1$ and simply connected for $k \geq 2$ and so is $\smash { F _ { k } }$ . Now SO(3) acts freely on $\pmb { F _ { k } }$ and the quotient is $M ( P )$ The homotopy exact sequence of the fibration

$$
\mathrm { S O ( 3 ) } \hookrightarrow F _ { k } \to { \mathcal { M } } ( P )
$$

shows that $M ( P )$ is connected and simply connected. Using the linking number of a sphere in $X _ { k } \setminus Z _ { k }$ with the codimension-3 submanifold $Z _ { k } \setminus S _ { k }$ we see that $\pi _ { 2 } ( F _ { k } ) = \pi _ { 2 } ( X _ { k } \setminus Z _ { k } ) = { \bf { Z } }$ .But in this case the fundamental group of SO(3) enters the exact sequence

$$
\mathbf { 0 } \to \mathbf { Z } \to \pi _ { 2 } ( { \mathcal { M } } ( P ) ) \to \mathbf { Z } _ { 2 } \to \mathbf { 0 }
$$

and we can only deduce that either $\pi _ { 2 } ( { \mathcal { M } } ( P ) ) = { \pmb { \mathbb { Z } } }$ or $\pi _ { 2 } ( { \mathcal { M } } ( P ) ) = { \mathbf { \mathbb { Z } } } \oplus { \mathbf { \mathbb { Z } } } _ { 2 }$ ， We must rule out the latter case. This requires the approach of Atiyah and Bott [2] using infinite dimensional Morse theory.

Theorem 4.3 Assume $k \geq 2$ . Then the (infinite dimensional) space $A _ { \mathrm { f l a t } } ( P )$ of flat connections on $P$ is simply connected and $\pi _ { 2 } ( \mathcal { A } _ { \mathrm { f l a t } } ( P ) ) = 0$

The proof of this result is based on Morse theory for the Yang-Mills functional

$$
\mathcal { V } \mathcal { M } ( A ) = \int _ { \Sigma } \left\| F _ { A } \right\| ^ { 2 }
$$

on the space of connections $A ( P )$ . The idea is to extend a loop $A _ { 1 } : S ^ { 1 } $ $A _ { \mathrm { f l a t } } ( P )$ to a map $A : D \to A ( P )$ on the unit disc.Then use the gradient flow of the Yang-Mills functional to ‘push this extension down’ to the set $A _ { \mathrm { f l a t } } ( P )$ of absolute minima. This requires that all the non-minimal critical manifolds have Morse index at least 3 so that the extension $\pmb { A }$ in general position does not intersect their stable manifolds. The same consideration gives $\pi _ { 2 } ( \mathcal { A } _ { \mathrm { f l a t } } ( P ) ) = 0$ if these Morse indices are at least 4. The details of this argument are carried out in [6]. In [2] Atiyah and Bott used an alternative stratification of the space $\pmb { A } ( P )$ to prove Theorem 4.3.

Now the homotopy exact sequence of the fibration $\mathcal { G } _ { 0 } \hookrightarrow \mathcal { A } _ { \mathrm { f l a t } } ( P ) \to$ $M ( P )$ shows that

$$
\pi _ { 2 } ( { \cal M } ( P ) ) = \pi _ { 1 } ( { \mathcal G } _ { 0 } ( P ) ) = { \bf Z } .
$$

The last identity follows from Lemma 1.2 applied to the bundle $Q = P \times S ^ { 1 }$ over the 3-manifold $M = \Sigma \times S ^ { 1 }$ . The isomorphism $\pi _ { 1 } ( \mathcal { G } _ { 0 } ( P ) ) = \mathbb { Z }$ is given by the degree of a loop $g ( s ) \in \mathcal { G } _ { 0 } ( P )$ regarded as a gauge transformation of $P \times S ^ { 1 }$

We shall now give a more explicit description of the isomorphism from $\pi _ { 1 } ( \mathcal { G } _ { 0 } ( P ) )$ to $\pi _ { 2 } ( { \mathcal { M } } ( P ) )$ .Let $A _ { 0 } \in \mathcal { A } _ { \mathrm { f i a t } } ( P )$ be a flat connection and let $g ( \theta ) \in \mathcal { G } _ { 0 } ( P )$ be a loop of gauge transformations such that $\begin{array} { r } { g ( 0 ) = g ( 1 ) = 1 } \end{array}$ · By Theorem 4.3 there exists a map $A : D \to { \mathcal { A } } _ { \mathrm { f a t } } ( P )$ on the unit disc such that

$$
A ( e ^ { 2 \pi i \theta } ) = A _ { 1 } ( \theta ) = g ( \theta ) ^ { * } A _ { 0 } .
$$

This map represents a sphere in the moduli space $M ( P )$ since the boundary of $D$ is mapped to a point. An easy calculation shows that the integral of the symplectic form over this sphere is given by

$$
\begin{array} { l l l } { { \displaystyle \int _ { D } \int _ { \Sigma } \left. \frac { \partial A } { \partial s } \wedge \frac { \partial A } { \partial t } \right. d s d t } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \int _ { \Sigma } \left. \frac { d A _ { 1 } } { d \theta } \wedge ( A _ { 1 } - A _ { 0 } ) \right. d \theta } } \\ { { } } & { { = } } & { { \displaystyle 8 \pi ^ { 2 } \deg ( g ) . } } \end{array}
$$

The last identity follows from equation (2） applied to the Chern-Simons functional on the bundle $Q = P \times S ^ { 1 }$

Remark 4.4 (i) The group $\pi _ { 0 } ( \mathcal { G } ( P ) ) = \mathcal { G } ( P ) / \mathcal { G } _ { 0 } ( P ) = { \mathbf Z _ { 2 } } ^ { 2 k }$ of components of the gauge group acts on the moduli space by symplectomorphism $\mathcal { M } ( P ) \to \mathcal { M } ( P ) : [ A ] \mapsto [ g ^ { * } A ]$ . This action is not free:it is easy to construct a flat connection whose isotropy subgroup $\mathcal { G } _ { A }$ is nontrivial but discrete.

(ii） The tangent bundle of $M ( P )$ is a complex vector bundle and therefore has Chern classes. It follows from our theorem about the spectral flow [7] that the integral of the frst Chern class $c _ { 1 } \in H ^ { 2 } ( { \mathcal { M } } ( P ) ; { \mathbf { Z } } )$ over the sphere $A : D \to { \mathcal { A } } _ { \mathrm { f a t } } ( P )$ satisfying (15) is given by $\mathbf { 2 } { \mathrm { ~ d e g } } ( { \pmb g } )$ This was already known to Atiyah and Bott [2].

# 5Mapping cylinders

Continue the notation of the previous section. Any diffeomorphism $h : \Sigma $ $\pmb { \Sigma }$ lifts to an automorphism $f : P \to P$ since ${ \pmb h } ^ { * } { \pmb P }$ is isomorphic to $P$ . We assume throughout that $\pmb { h }$ is orientation preserving. The automorphism $f$ induces a symplectomorphism

$$
\phi _ { f } : \mathcal { M } ( P ) \to \mathcal { M } ( P )
$$

defined by $\phi _ { f } ( [ A ] ) = [ f ^ { * } A ]$ . In the context of representations of the fundamental group this symplectomorphism is given by $\rho \mapsto \rho \circ f _ { * }$ .Hence the symplectomorphism $\phi _ { f }$ depends only on the homotopy class of $f$ . A fixed point of $\phi _ { f }$ is an equivalence class of a flat connection $A _ { 0 } \in \mathcal { A } _ { \mathrm { f l a t } } ( P )$ such that $g ^ { * } f ^ { * } A _ { 0 } = A _ { 0 }$ for some gauge transformation ${ \mathfrak { g } } \in { \mathcal { G } } _ { 0 } ( P )$ . This can be written as

$$
f _ { g } ^ { * } A _ { 0 } = A _ { 0 }
$$

where the automorphism $f _ { g } \in \operatorname { A u t } ( P )$ is defined by

$$
f _ { g } ( p ) = f ( p ) g ( p )
$$

for ${ \pmb p } \in { \pmb P }$ . The diferential of $\phi _ { f }$ at the fixed point $\pmb { A _ { 0 } }$ is the linear map

$$
f _ { g } ^ { * } : H _ { A _ { 0 } } ^ { 1 } ( \Sigma ) \to H _ { A _ { 0 } } ^ { 1 } ( \Sigma ) .
$$

Here we identify $H _ { A _ { 0 } } ^ { 1 }$ with the quotient ker $d _ { A _ { 0 } } / \mathrm { i m } d _ { A _ { 0 } }$ rather than the space of harmonic forms which willin general not be invariant under $f _ { g } ^ { * }$

Remark 5.1 For every ${ \pmb g } \in { \pmb \mathcal G } ( { \pmb P } )$ and every $A \in { \mathcal { A } } ( P )$

$$
f ^ { * } g ^ { * } A = ( g \circ f ) ^ { * } f ^ { * } A .
$$

Hence the symplectomorphism $\mathcal { M } ( P ) \to \mathcal { M } ( P ) : [ A ] \mapsto [ g ^ { * } A ]$ commutes with $\phi _ { f }$ whenever $\pmb { g }$ is homotopic to ${ \pmb g } \circ { \pmb f }$ or equivalently the parity $\pmb { \eta } ( \pmb { g } )$ is in the kernel of the homomorphism $\mathbb { 1 } - h ^ { * } : H ^ { 1 } ( \Sigma , \mathbf { Z } ^ { 2 } ) \to H ^ { 1 } ( \Sigma , \mathbf { Z } ^ { 2 } )$ .Define

$$
{ \mathcal G } _ { f } ( P ) = \{ g \in { \mathcal G } ( P ) : g \sim g \circ f \} , \qquad \Gamma _ { f } = { \mathcal G } _ { f } ( P ) / { \mathcal G } _ { 0 } ( P ) .
$$

Then $\Gamma _ { f } \simeq \ker ( \mathbb { 1 } - h ^ { * } )$ is a finite group which acts on $M ( P )$ by symplectomorphisms which commute with $\phi _ { f }$ .In particular, $\Gamma _ { f }$ acts on the fixed points of $\phi _ { f }$ . More explicitly, if $[ A _ { 0 } ] \in \mathbb { F i x } ( \phi _ { f } )$ and $g _ { 0 } \in { \mathcal { G } } _ { f } ( P )$ then $[ A _ { 0 } ^ { \prime } ] = [ g _ { 0 } ^ { * } A _ { 0 } ] \in \mathbb { F } \mathrm { i } \mathbf { x } ( \phi _ { f } )$ . To see this choose ${ \mathfrak { g } } \in { \mathcal { G } } _ { 0 } ( P )$ such that $g ^ { * } f ^ { * } A _ { 0 } = A _ { 0 }$ and define $g ^ { \prime } = ( g _ { 0 } \circ f ) ^ { - 1 } g g _ { 0 } \in \mathcal { G } _ { 0 } ( P )$ . Then $g ^ { \prime * } f ^ { * } A _ { 0 } ^ { \prime } = A _ { 0 } ^ { \prime }$

The automorphism $\pmb { f }$ also determines a principal SO(3)-bundle

$$
P _ { f } \to \Sigma _ { h } .
$$

Here $Q = P _ { f }$ denotes the mapping cylinder of $P$ for the automorphism $f$ That is the set of equivalence classes of pairs $[ p , s ] \in P \times \mathbb { R }$ under the equivalence relation generated by $[ p , s + 1 ] \equiv [ f ( p ) , s ]$ .Likewise the 3-manifold $M = \Sigma _ { h }$ denotes the mapping cylinder of the Riemann surface $\pmb { \Sigma }$ for the diffeomorphism $\pmb { h }$ . This bundle satisfies hypothesis (H1) of section 1.A connection $a \in { \mathcal { A } } ( P _ { f } )$ is a 1-form $a = A + \Phi d s$ where $A ( s ) \in { \mathcal { A } } ( P ) , { \Phi } ( s ) \in \Omega ^ { 0 } ( { \mathfrak { g } } _ { P } )$ for $\pmb { \mathscr { s } } \in \pmb { \mathbb { R } }$ and

$$
A ( s + 1 ) = f ^ { * } A ( s ) , \qquad \Phi ( s + 1 ) = \Phi ( s ) \circ f .
$$

Now the group $\mathcal { G } ( P _ { f } )$ of gauge transformations of $P _ { f }$ consists of smooth 1- parameter families of gauge transformations $g ( s ) \in { \mathcal { G } } ( P )$ such that

$$
g ( s + 1 ) = g ( s ) \circ f .
$$

Such a gauge transformation acts on a connection $a = A + \Phi d s \in A ( P _ { f } )$ by

$$
g ^ { * } a = g ^ { * } A + \left( g ^ { - 1 } \dot { g } + g ^ { - 1 } \Phi g \right) \ d s .
$$

Here we use the notation $\pmb { g } ^ { \ast }$ ambiguously: ${ \pmb g } ^ { \ast } { \pmb a }$ denotes the action of $\mathfrak { g } \in \mathcal { G } ( P _ { f } )$ on $a \in \mathcal { A } ( P _ { f } )$ whereas ${ \pmb g } ^ { \star } { \pmb A }$ denotes the pointwise action of $g ( s ) \in { \mathcal { G } } ( P )$ on $A ( s ) \in A ( P )$

Remark 5.2 Consider the normal subgroups

$$
\mathcal { G } _ { 0 } ( P _ { f } ) \subset \mathcal { G } _ { \Sigma } ( P _ { f } ) \subset \mathcal { G } ( P _ { f } )
$$

where $\mathcal { G } _ { \Sigma } ( P _ { f } ) = \{ g \in \mathcal { G } ( P _ { f } ) : g ( s ) \in \mathcal { G } _ { 0 } ( \Sigma ) \forall s \}$ and $\mathscr { G } _ { 0 } ( P _ { f } )$ is the component of $\pmb { \mathbb { 1 } }$ Then

$$
\mathcal G ( P _ { f } ) / \mathcal G _ { \Sigma } ( P _ { f } ) \simeq \Gamma _ { f } , \qquad \mathcal G _ { \Sigma } ( P _ { f } ) / \mathcal G _ { 0 } ( P _ { f } ) \simeq \mathbf { Z } .
$$

The second isomorphism is given by the degree while the first follows from the fact that ${ \pmb g } _ { \pmb 0 } \in \mathcal { G } ( P )$ extends to a gauge transformation of $P _ { f }$ if and only if $g _ { 0 } \in \mathcal { G } _ { f } ( P )$ .The first isomorphism shows that $\Gamma _ { f }$ is the group of components of gauge transformations of $P _ { f }$ of degree zero

The path space $\Omega _ { \phi _ { f } }$ can be naturally identified with a subquotient of the space of connections on $P _ { f }$ . Consider the subspace

$$
{ \cal A } _ { \Sigma } ( P _ { f } ) = \left\{ { \cal A } + \Phi { \cal d } s \in { \cal A } ( P _ { f } ) : { \cal F } _ { \cal A } = 0 , { \cal d } _ { \cal A } ^ { \ast } \left( { \cal d } { \cal A } / { \cal d } s - { \cal d } _ { \cal A } \Phi \right) = 0 \right\} .
$$

If $A { + } \Phi d s \in { \mathcal { A } } _ { \Sigma } ( P _ { f } )$ then $\pmb { \Phi }$ is uniquely determined by $\pmb { A }$ . In fact $d A / d s { - } d _ { A } \Phi$ represents the projection of $d A / d s$ onto the space $H _ { A } ^ { 1 } ( \Sigma ) = T _ { [ A ] } { \cal M } ( P )$ of harmonic forms.

Proposition 5.3 There are natural bijections

$$
\Omega _ { \phi _ { f } } \simeq { \cal A } _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { \Sigma } ( P _ { f } ) , \qquad \widetilde { \Omega } _ { \phi _ { f } } \simeq { \cal A } _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { 0 } ( P _ { f } ) .
$$

In particular, $\Omega _ { \phi _ { f } }$ is connected and

$$
\pi _ { 1 } ( \Omega _ { \phi _ { f } } ) \simeq \mathcal { G } _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { 0 } ( P _ { f } ) \simeq \pi _ { 2 } ( \boldsymbol { \mathcal { M } } ( \boldsymbol { P } ) ) .
$$

Proof: A point in the space $\Omega _ { \phi _ { f } }$ is a smooth path $\gamma : \pmb { \mathsf { R } }  \mathcal { M } ( P )$ such that $\gamma ( s + 1 ) = \phi _ { f } ( \gamma ( s ) )$ . Such a path lifts to a smooth map $A : \mathbb { R } \to { \mathcal { A } } _ { \mathrm { f a t } } ( P )$ satisfying

$$
A ( s + 1 ) = h ( s ) ^ { * } f ^ { * } A ( s ) .
$$

for some smooth map $\pmb { h } : \pmb { \mathsf { R } }  \mathcal { G } _ { \mathbf { 0 } } ( P )$ . Two such pairs $( A , h )$ and $( A ^ { \prime } , h ^ { \prime } )$ represent the same path $\gamma : \pmb { \mathsf { R } }  \mathcal { M } ( P )$ if and only if there exists a smooth map $g : \mathsf { R } \to { \mathcal { G } } _ { 0 } ( P )$ such that

$$
A ^ { \prime } ( s ) = g ( s ) ^ { * } A ( s ) , \qquad h ^ { \prime } ( s ) = ( g ( s ) \circ f ) ^ { - 1 } h ( s ) g ( s + 1 ) .
$$

Every path $\pmb { \gamma }$ can be represented by a pair $( A , h )$ with $h ( s ) \equiv 1$ . To see this choose, for any given pair $( A , h )$ ,a path $g : [ 0 , 1 ] \to { \mathcal { G } } _ { 0 } ( P )$ such that $\pmb { g } ( s ) = 1$ for $\pmb { \mathscr { s } }$ near O and $g ( \mathscr { s } ) = h ( \mathscr { s } ) ^ { - 1 }$ for $\pmb { \mathscr { s } }$ near 1. Then $\pmb { g } ( \pmb { s } )$ extends to a unique function $\begin{array} { r } { \pmb { \mathsf { R } }  \pmb { \mathcal { G } } _ { \mathbf { 0 } } ( P ) } \end{array}$ satisfying

$$
h ( s ) g ( s + 1 ) = g ( s ) \circ f .
$$

This proves the first statement.

To prove the second statement recall from Theorem 4.3 that $A _ { \mathrm { f l a t } } ( P )$ is connected and simply connected and $\pi _ { 2 } ( \mathcal { A } _ { \mathrm { f l a t } } ( P ) ) = 0$ . Hence $A _ { \Sigma } ( P _ { f } )$ is connected and simply connected.By the homotopy exact sequence

$$
\pi _ { 1 } ( \mathcal { A } _ { \Sigma } ( P _ { f } ) ) \to \pi _ { 1 } ( \mathcal { A } _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { 0 } ( P _ { f } ) ) \to \pi _ { 0 } ( \mathcal { G } _ { 0 } ( P _ { f } ) )
$$

the quotient $A _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { 0 } ( P _ { f } )$ is simply connected. Hence this quotient is the universal cover of $A _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { \Sigma } ( P _ { f } ) \simeq \Omega _ { \phi _ { f } }$ □

The Chern-Simons functional on the space of connections $\pmb { A } ( P _ { f } )$ is given by the formula

$$
\mathcal { C } \mathcal { S } ( A + \Phi d s ) = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \int _ { \Sigma } \left( \left. \dot { A } \wedge ( A - A _ { 0 } ) \right. + \left. F _ { A } \wedge \Phi \right. \right) d s
$$

Here $\pmb { A _ { 0 } }$ is any flat connection on $P$ such that $f ^ { * } A _ { 0 } = A _ { 0 }$ . A simple calculation shows that the restriction of $c s$ to $A _ { \Sigma } ( P _ { f } )$ induces the symplectic action functional on $\widetilde { \Omega } _ { \phi _ { f } } = \mathcal { A } _ { \Sigma } ( P _ { f } ) / \mathcal { G } _ { 0 } ( P _ { f } )$ .We shall in fact prove that the critical points of the Chern-Simons functional, that is the flat connections on $P _ { f }$ ，agree with the critical points of the symplectic action,that is the fixed points of $\phi _ { f }$ . To see this note that the curvature of the connection $a = A + \Phi d s$ is the 2-form

$$
F _ { A + \Phi d s } = F _ { A } + \left( d _ { A } \Phi - \dot { A } \right) \wedge d s
$$

Thus the flat connections on $P _ { f }$ are smooth families of fat connections $A ( s ) \in$ $A _ { \mathrm { f l a t } } ( P )$ such that $d A / d s \in \mathrm { i m } d _ { A }$ and (17) is satisfed.

Proposition 5.4 The map $A ( P _ { f } )  A ( P ) : A + \Phi d s \mapsto A ( 0 )$ induces a bijection

In particular

$$
\begin{array} { r l r } & { } & { \mathcal { A } _ { \mathtt { H a t } } ( P _ { f } ) / \mathcal { G } _ { \Sigma } ( P _ { f } ) \simeq \mathrm { F i x } ( \phi _ { f } ) . } \\ & { } & { ( P _ { f } ) / \mathcal { G } ( P _ { f } ) \simeq \mathrm { F i x } ( \phi _ { f } ) / \Gamma _ { f } . \quad } \end{array}
$$

Proof: First assume that $a = A + \Phi d s \in A _ { \mathrm { { H a t } } } ( P _ { f } )$ . Then $A ( s ) \in { \mathcal { A } } _ { \mathrm { f a a t } } ( P )$ for every $\pmb { \mathscr { s } }$ and $\dot { A } = d _ { A } \Phi$ Let $g ( s ) \in { \mathcal { G } } ( P )$ be the unique solution of the ordinary differential equation $\dot { \pmb { g } } + \Phi \pmb { g } = { \bf 0 }$ with ${ \pmb g } ( { \pmb 0 } ) = { \pmb 1 }$ Then $g ( s ) ^ { * } A ( s ) \equiv$ $A _ { 0 }$ and hence it follows from (17) that $g ( 1 ) ^ { * } f ^ { * } A _ { 0 } = g ( 1 ) ^ { * } A ( 1 ) = A _ { 0 }$ By construction, $g ( 1 ) \in \mathcal { G } _ { 0 } ( P )$ and hence $A _ { 0 }$ represents a fixed point of $\phi _ { f }$ . This proves that there is a well defined map $A _ { \mathrm { f a a t } } ( P _ { f } ) / \mathcal { G } _ { \Sigma } ( P _ { f } )  \mathrm { F i x } ( \phi _ { f } )$ given by $A + \Phi d s \mapsto A ( 0 )$

We prove that this map is onto. Suppose that $A _ { 0 } \in \mathcal { A } _ { \mathrm { f l a t } } ( P )$ represents a fixed point of $\phi _ { f }$ and let $g _ { 1 } \in \mathcal { G } _ { 0 } ( P )$ such that $g _ { 1 } ^ { * } f ^ { * } A _ { 0 } = A _ { 0 }$ Choose a smooth l-parameter family of connections $g ( s ) \in \mathcal { G } _ { 0 } ( P )$ such that $\pmb { g } ( \mathbf { 0 } ) = \mathbf { 1 }$ ， $g ( 1 ) = g _ { 1 }$ and $g ( s + 1 ) = ( g ( s ) \circ f ) g _ { 1 }$ for every $\pmb { \mathscr { s } }$ .Let $A ( s ) \in { \mathcal { A } } _ { \mathrm { f a a t } } ( P )$ be defined by $g ( s ) ^ { * } A ( s ) = A _ { 0 }$ and $\Phi ( s ) = - \dot { g } ( s ) g ( s ) ^ { - 1 }$ . Then $a = A + \Phi d s$ is the required flat connection on $P _ { f }$ .

We prove that the map is injective. Let $a , a ^ { \prime } \in \mathcal { A } _ { \mathrm { f a t } } \big ( P _ { f } \big )$ such that $A ^ { \prime } ( { \bf 0 } ) =$ ${ \pmb g } _ { \bf 0 } ^ { \ast } { \pmb A } ( { \bf 0 } )$ for some ${ \mathfrak { g } } _ { 0 } \in { \mathcal { G } } _ { 0 } ( P )$ . Define $g ( s ) \in \mathcal { G } _ { 0 } ( P )$ to be the unique solution of the ordinary differential equation $\dot { \pmb g } = \pmb g \pmb \Phi ^ { \prime } - \pmb \Phi g$ ， ${ \pmb g } ( { \pmb 0 } ) = { \pmb g } _ { \mathbf 0 }$ . Then

$$
\frac { d } { d s } g ^ { * } { \cal A } = g ^ { - 1 } \dot { \cal A } g + d _ { g ^ { * } { \cal A } } ( g ^ { - 1 } \dot { g } ) = g ^ { - 1 } d _ { A } \Phi g + d _ { g ^ { * } { \cal A } } ( \Phi ^ { \prime } - g ^ { - 1 } \Phi g ) = d _ { g ^ { * } { \cal A } } \Phi ^ { \prime } .
$$

Here we have used $\dot { A } = d _ { A } \Phi$ . Since $A ^ { \prime } ( 0 ) = g ( 0 ) ^ { * } A ( 0 )$ and $\dot { \pmb { A } } ^ { \prime } = d _ { A ^ { \prime } } \pmb { \Phi } ^ { \prime }$ it follows that $g ( s ) ^ { * } A ( s ) = A ^ { \prime } ( s )$ for every $\pmb { \mathscr { s } }$ .Moreover it follows from (17) that $g ( s + 1 ) ^ { - 1 } g ( s ) \circ f \in { \mathcal { G } } _ { A ( s + 1 ) } \cap { \mathcal { G } } _ { 0 } ( P )$ .By Lemma 4.1 this implies $g ( s + 1 ) =$ $\pmb { g } ( \pmb { s } ) \circ \pmb { f }$ . Hence $\pmb { g } ( \pmb { s } )$ defines a gauge transformation of $P _ { f }$ and $\pmb { a } ^ { \prime } = \pmb { g } ^ { * } \pmb { a }$ □

Proposition 5.5 A flat connection $A + \Phi d s \in \mathcal { A } _ { \mathrm { f a t } } ( P _ { f } )$ is nondegenerate as a critical point of the Chern-Simons functional if and only if $\left[ A ( 0 ) \right]$ is $\pmb { a }$ nondegenerate fixed point of $\phi _ { f }$

Proof: Let $a = A + \Phi d s \in A _ { \mathrm { f a t } } ( P _ { f } )$ be a flat connection and define $A _ { 0 } = A ( 0 ) \in \mathcal { A } _ { \mathrm { f a t } } ( P )$ Then $f _ { g } ^ { * } A _ { 0 } = A _ { 0 }$ where ${ \mathfrak { g } } \in { \mathcal { G } } _ { 0 } ( P )$ is defined by $\begin{array} { r } { \pmb { g } = \pmb { g } ( 1 ) } \end{array}$ for the unique solution $g ( s ) \in \mathcal { G } _ { 0 } ( P )$ of $\dot { g } ( s ) + \Phi ( s ) g ( s ) = 0$ with $\pmb { g ( 0 ) } = \mathbb { 1 }$ . We must show that

$$
\mathbb { 1 } - f _ { g } ^ { * } : H _ { A _ { 0 } } ^ { 1 } ( \Sigma ) \to H _ { A _ { 0 } } ^ { 1 } ( \Sigma )
$$

is an isomorphism if and only if $H _ { A + \Phi d s } ^ { 1 } ( \Sigma _ { h } ) = 0$ . The latter means that whenever $\alpha + \phi d s \in \Omega ^ { 1 } ( \mathfrak { g } _ { P _ { f } } )$ is an infinitesimal connection such that

$$
d _ { A } \alpha = 0 , \qquad d _ { A } \phi = \dot { \alpha } + [ \Phi \wedge \alpha ]
$$

then there exists a $\pmb { \xi } \in \Omega ^ { 0 } \big ( \mathfrak { g } _ { P _ { f } } \big )$ such that

$$
\alpha = d _ { A } \xi , \qquad \phi = \dot { \xi } + [ \Phi \wedge \xi ] .
$$

Replacing $\pmb { a }$ by $\pmb { g } ^ { * } \pmb { a }$ and $\pmb { f }$ by $f _ { g ( 1 ) }$ we may assume without loss of generality that $\bar { \Phi } ( s ) \equiv 0$ and $A ( s ) \equiv A _ { 0 }$

Assume first that $\pmb { \mathbb { 1 } } - \pmb { f ^ { * } }$ is an isomorphism of $H _ { A _ { 0 } } ^ { 1 }$ .Let $\alpha ( s ) \in \Omega ^ { 1 } ( { \mathfrak { g } } _ { P } )$ and $\phi \in \Omega ^ { 0 } ( \mathfrak { g } _ { P } )$ satisfy (18) and the boundary conditions $\alpha ( s + 1 ) = f ^ { * } \alpha ( s ) .$ ， $\phi ( s + 1 ) = \phi ( s ) \circ f$ .Then

$$
f ^ { * } \alpha ( 0 ) - \alpha ( 0 ) = d _ { A _ { 0 } } \int _ { 0 } ^ { 1 } \phi ( s ) d s , \qquad d _ { A _ { 0 } } \alpha ( 0 ) = 0 .
$$

Since $\mathbb { 1 } - f ^ { * } : H _ { A _ { 0 } } ^ { 1 } \to H _ { A _ { 0 } } ^ { 1 }$ is injective there exists a $\pmb { \xi _ { 0 } } \in \Omega ^ { 0 } ( \{ \mathfrak { g } _ { P } \}$ such that ${ \alpha ( 0 ) = d _ { A _ { 0 } } \xi _ { 0 } }$ . Define

$$
\xi ( s ) = \xi _ { 0 } + \int _ { 0 } ^ { s } \phi ( \theta ) d \theta .
$$

Then $\phi = \dot { \xi }$ ,hence $\dot { \alpha } = d _ { A _ { 0 } } \dot { \xi }$ , and hence ${ \pmb { \alpha } } = d _ { A _ { 0 } } { \pmb { \xi } }$ .The latter identity implies that $d _ { A _ { 0 } } \xi ( s + 1 ) = f ^ { \ast } d _ { A _ { 0 } } \xi ( s )$ and hence $\xi ( s + 1 ) = \xi ( s ) \circ f$

Conversely, suppose that $\mathbb { 1 } - f ^ { * } : H _ { A _ { 0 } } ^ { 1 } \to H _ { A _ { 0 } } ^ { 1 }$ is not injective. Then there exist $\alpha _ { 0 } \in \Omega ^ { 1 } ( { \mathfrak { g } } _ { P } )$ and $\pmb { \xi _ { 0 } } \in \Omega ^ { 0 } ( \{ \mathfrak { g } _ { P } ) $ such that

$$
f ^ { * } \alpha _ { 0 } - \alpha _ { 0 } = d _ { A _ { 0 } } \xi _ { 0 } , \qquad d _ { A _ { 0 } } \alpha _ { 0 } = 0 , \qquad \alpha _ { 0 } \not \in \mathrm { i m } d _ { A _ { 0 } } .
$$

Choose any function $\phi ( s ) \in \Omega ^ { 0 } ( { \mathfrak { g } } _ { P } )$ satisfying

$$
\xi _ { 0 } = \int _ { 0 } ^ { 1 } \phi ( s ) d s , \qquad \phi ( s + 1 ) = \phi ( s ) \circ f .
$$

For example take a cutoff function $\beta : [ 0 , 1 ] \to \mathbb { R }$ of mean value 1 which vanishes near ${ \mathfrak { s } } = { \mathfrak { d } }$ and $\mathfrak { s } = 1$ and define $\phi ( s + j ) = \beta ( s ) \xi _ { 0 } \circ f ^ { j }$ for $0 \leq s \leq 1$ and $j \in \mathbb { Z }$ Let $\alpha ( s ) \in \Omega ^ { 1 } ( { \mathfrak { g } } _ { P } )$ be the unique solution of $\dot { \alpha } = d _ { A _ { 0 } } \phi$ with ${ \pmb { \alpha } } ( \mathbf { 0 } ) = { \pmb { \alpha _ { 0 } } }$ .Then $\pmb { \alpha }$ and $\phi$ satisfy (18) but are not of the form (19) since $\alpha _ { 0 } \not \in \mathrm { i m } d _ { A _ { 0 } }$ . This shows that ${ H } _ { A + \Phi d s } ^ { 1 } \neq 0$ □

Remark 5.6 It is an open question whether every symplectomorphism $\phi$ ： $\mathcal { M } ( P )  \mathcal { M } ( P )$ is isotopic (within the group of symplectomorphisms） to one of the form $\phi _ { f }$ for $f \in \operatorname { A u t } ( P )$ . It is also an open question whether $f _ { 0 }$ and $f _ { 1 }$ are isotopic whenever $\phi _ { f _ { 0 } }$ and $\phi _ { f _ { 1 } }$ are isotopic.
