2.12.THEOREM (loc. cit.). Assume that the level set $J ^ { - 1 } ( \mathcal { O } )$ is connected. Then the reduced space $M _ { \mathcal { O } }$ has a unique open stratum. $\ b { I t }$ is connected and dense.

2.13.REMARk. We note two important cases when thelevel set is connected. First, if $M$ is a symplectic vector space and $\pmb { G }$ acts linearly on $M$ then the zero level set is conical and so is connected. Secondly, $\mathbf { F }$ . Kirwan has proved [11] that if the moment map $J$ is proper (for example if $M$ is compact） and $M$ is connected then the zero level set $J ^ { - 1 } ( 0 )$ is connected．It follows then from the shifting trick,Proposition 2.16 below,that the level set $J ^ { - 1 } ( \mathcal { O } )$ is connected for any compact orbit $\scriptscriptstyle \mathcal { O }$

The symplectic structure on the dense open stratum determines the Poisson structure on the whole reduced space and, therefore, the symplectic structures on all the lower-dimensional strata by condition (iii) of Definition 2.10.We will refer to the dense open stratum as the top stratum. Condition (i) also has some interesting consequences. Suppose that the top stratum is twodimensional as in Section 1. Then all the other strata are zero-dimensional, i.e., they are isolated points. There is a temptation in view of Theorem 2.12 to discard all the lower-dimensional strata. We will see in the next section that giving in to such a temptation leads to a loss of interesting information.

# 2.2Hamiltonian Mechanics on a Stratifed Symplectic Space

Just as we defined in Section 1.1 a diffeomorphism between two reduced spaces，one can define an isomorphism between two stratifed symplectic spaces.

2.14. DEFINITION. Let $X$ and $\boldsymbol { Y }$ be two stratifed symplectic spaces. A map $\phi : X \to Y$ is an isomorphism if $\phi$ is a homeomorphism and the pullback map $\phi ^ { * } : C ^ { \infty } ( Y ) \to C ^ { \infty } ( X )$ ， $f \mapsto f \circ \phi$ is an isomorphism of Poisson algebras.

Note that we do not explicitly require that $\phi$ be strata-preserving. The reason for this is that the stratification of a stratified symplectic space $X$ is completely determined by the Poisson algebra structure on the space of smooth functions on $X$ ,as we shall see shortly.

2.15.ExAMPLE (the ‘shifting trick'). Let $M$ be a Hamiltonian $\pmb { G }$ -space with momentum map $J : M \to { \mathfrak { g } } ^ { * }$ and let $\scriptscriptstyle \mathcal { O }$ be any coadjoint orbit of $\pmb { G }$ . Consider the symplectic manifold $M \times \mathcal { O } ^ { - }$ ，the symplectic product of $M$ with the coadjoint orbit $\mathcal { O }$ ,endowed with the opposite of the Kirillov symplectic form. The diagonal action of $\pmb { G }$ on $M \times \mathcal { O } ^ { - }$ is Hamiltonian with momentum map $J _ { \mathcal { O } }$ given by $J _ { \mathcal { O } } ( m , \nu ) = J ( m ) - \nu$ . It is easy to check that the cartesian projection $\Pi : M \times \mathcal { O } ^ { - } \to M$ restricts to an equivariant bijection $J _ { \mathcal { O } } ^ { - 1 } ( 0 ) \cong J ^ { - 1 } ( \mathcal { O } )$ .As a result, $\Pi$ descends to a bijection bet ween reduced spaces,

$$
\tilde { \Pi } : ( M \times \mathcal { O } ^ { - } ) _ { 0 } \tilde {  } M _ { \mathcal { O } } .
$$

2.16.PROPOsITION.Assume that the orbit $\mathcal { O }$ is a closed subset of ${ \mathfrak { g } } ^ { * }$ . Then the map $\tilde { \Pi }$ is an isomorphism of stratified symplectic spaces.

See [5] for a proof.

2.17.DEFINITION.A ffow $\{ \phi _ { t } \}$ on a stratified symplectic space $\boldsymbol { X }$ is a oneparameter family of isomorphisms $\phi _ { t } : X \to X , t \in \mathbf { R }$ ,such that $\phi _ { t + s } = \phi _ { t } \circ \phi _ { s }$ for all $t$ and $\pmb { s }$

2.18.DEFINITION．Let $\pmb { h }$ be a smooth function on a stratified symplectic space $X , \ h \in C ^ { \infty } ( X )$ A Hamiltonian flow of $\boldsymbol { h }$ is a fow $\{ \phi _ { t } \}$ having the property that for any function $f \in C ^ { \infty } ( X )$

$$
\frac { d } { d t } ( f \circ \phi _ { t } ) = \{ f , h \} \circ \phi _ { t } .
$$

This is Heisenberg's form of Hamilton's equations. Since the space $\boldsymbol { x }$ is not necessarily a manifold,(6) cannot be reduced to a system of ordinary diferential equations. For this reason the existence and uniqueness of the Hamiltonian flow is not immediately obvious. If $X$ is a reduced space, the Hamiltonian flow does indeed exist and is unique [21]. Moreover,the follwing lemma holds.

2.19.LEMMA (cf.[21]).Let $M _ { \mathcal { O } }$ be the reduced space of a Hamiltonian $\pmb { G }$ space $M$ ata coadjoint orbit $\mathcal { O }$ of $\pmb { G }$ .The Hamiltonian flow of a smooth function $h \in C ^ { \infty } ( M _ { \mathcal { O } } )$ preserves the stratification. The restriction of the flow of $\pmb { h }$ to a stratum $s$ equals the Hamiltonian flow of the restriction $h | _ { s }$

The connected components of the strata are the symplectic leaves of $M _ { \mathcal { O } }$ ， i.e.,given any pair of points $p , q$ in a connected component of a stratum of $M _ { \mathcal { O } }$ ,there exists a piecewise smooth path joining $\pmb { p }$ to $\pmb q$ ,consisting of a finite number of Hamiltonian trajectories of smooth functions on $M _ { \mathcal { O } }$ .Thus the Poisson structure of $C ^ { \infty } ( M _ { \mathcal { O } } )$ determines the stratification of $M _ { \mathcal { O } }$

2.20.REMARK.It follows that a zero-dimensional stratum of the reduced space $M _ { \mathcal { O } }$ is automatically a fixed point of any Hamiltonian flow. Thus the zero-dimensional strata of $M _ { \mathcal { O } }$ determine relative equilibria in the original space $M$

# 2.3Orbit Types

We now explain where the stratification of a reduced space comes from and how it can be computed. Let $\pmb { G }$ be a Lie group acting properly on a manifold $M$ . (For example if $\pmb { G }$ is compact then its action is automatically proper.) For a subgroup $\pmb { H }$ of $\pmb { G }$ denote by $M _ { ( H ) }$ the set of all points whose stabilizer is conjugate to $H$ ，

$$
M _ { ( H ) } = \{ m \in M : G _ { m } { \mathrm { ~ i s ~ c o n j u g a t e ~ t o ~ } } H \} .
$$

By virtue of the slice theorem for proper actions (see e.g. Palais [17]),the set $M _ { ( H ) }$ is a smooth submanifold of $M$ , called the manifold of orbit type $( H )$ Thus we have a decomposition $M = \operatorname { I I } _ { H < G } M _ { ( H ) }$ of $M$ into a disjoint union of manifolds. Theorem 2.11 can now be restated as follows.

2.21.THEOREM. Let $( M , \omega )$ be a Hamiltonian $\pmb { G }$ -space with moment map $J : M \to { \mathfrak { g } } ^ { * }$ and let $\scriptscriptstyle \mathcal { O }$ beacoadjoint orbit of $\pmb { G }$ . Assume that the action of $\pmb { G }$ on $J ^ { - 1 } ( { \mathcal { O } } )$ is proper. Then the intersection of the preimage of the orbit $J ^ { - 1 } ( { \mathcal { O } } )$ with a manifold of the form $M _ { ( H ) }$ ， $H < G$ ,is a manifold.The orbit space

$$
( M _ { \mathcal { O } } ) _ { ( H ) } : = ( J ^ { - 1 } ( \mathcal { O } ) \cap M _ { ( H ) } ) / G
$$

is also a manifold. There exists a unique symplectic form $\omega _ { \left( H \right) }$ on $( M _ { \mathcal { O } } ) _ { ( H ) }$ such that the pullback of $\omega _ { \left( H \right) }$ by the orbit map $J ^ { - 1 } ( \mathcal { O } ) \cap M _ { ( H ) } \to ( M _ { \mathcal { O } } ) _ { ( H ) }$ coincides with the restriction to $J ^ { - 1 } ( \mathcal { O } ) \cap M _ { ( H ) }$ of the symplectic form $\omega$ Finally,the decomposition of $M _ { \mathcal { O } } : = J ^ { - 1 } ( \mathcal { O } ) / G$ ，the reduced space of $M$ at the orbit $\scriptscriptstyle \mathcal { O }$ ， given by

$$
M o = \coprod _ { H < G } ( M o ) _ { ( H ) }
$$

is a symplectic stratifcation of $M o$

It is a curious fact that each stratum $( M _ { \mathcal { O } } ) _ { ( H ) }$ may also obtained by a regular Marsden-Weinstein reduction. To keep the discussion simple let us assume that $\mathcal { O }$ is the zero orbit.(This is no loss of generality by virtue of the shifting trick.） For a subgroup $H$ of $\pmb { G }$ define

$$
M _ { H } = \left\{ m \in M : G _ { m } { \mathrm { ~ i s ~ e x a c t l y ~ } } H \right\}
$$

It is well-known that $M _ { H }$ is a symplectic submanifold of $M$ . The action of $\pmb { G }$ does not preserve the manifold $M _ { H }$ . However, the smaller group $L =$ $N _ { G } ( H ) / H$ does act on $M _ { H }$ , where $N _ { G } ( H )$ denotes the normalizer of $H$ in $\pmb { G }$ Moreover, the action of $L$ is Hamiltonian and the corresponding moment map $J _ { L } : M _ { H } \to \mathbb { I } ^ { * }$ is essentially the restriction of the moment map $J : M \to { \mathfrak { g } } ^ { * }$ to $M _ { H }$

2.22.THEOREM (cf.[21]). Zero is a regular value of the moment map $J _ { L }$ The Marsden-Weinstein reduced space $( J _ { L } ) ^ { - 1 } ( 0 ) / L$ issymplectically isomorphic to the stratum $( M _ { 0 } ) _ { ( H ) }$

This theorem provides us with a simple recipe for lifting integral curves of a reduced Hamiltonian flow on the reduced space $M _ { 0 }$ to the level set $J ^ { - 1 } ( 0 )$ Namely, let $\bar { h }$ be an invariant smooth function on the manifold $M$ ,and let $\pmb { h }$ be the smooth function on the reduced space induced by $\bar { h }$ .Let $\bar { \Phi } _ { t }$ and $\Phi _ { t }$ ， denote the Hamiltonian fows of $\bar { h }$ and $\pmb { h }$ ,respectively. If $\gamma ( t )$ is an integral curve of the function $\pmb { h }$ ,then it lies inside some stratum $( M _ { 0 } ) _ { ( H ) }$ ，and the classical recipe for lifting a reduced flow (see e.g. [1]) can be used to lift $\gamma ( t )$ to an integral curve of the Hamiltonian $\bar { h }$ ,lying in the manifold $M _ { H }$

# 2.4The Closure of a Coadjoint Orbit as a Stratified Symplectic Space

The object of this section is to show that for a large class of Lie groups the closure of every coadjoint orbit is a stratified symplectic space. In Section 4 we shall see that in some cases a reduced space of a Hamiltonian space can be identified with the closure of a coadjoint orbit of a different group.

2.23.THEOREM.Let $H$ be a reductive Lie group and let $\mathcal { O } \subset \mathfrak { h } ^ { * }$ be a coadjoint orbit of $\pmb { H }$ . Then the closure $\bar { \mathcal { O } }$ of $\scriptscriptstyle \mathcal { O }$ is a stratifed symplectic space. The strata are the $H$ -orbits in $\bar { \mathcal { O } }$ ，

PROOF. We take the space $C ^ { \infty } ( { \bar { \mathcal { O } } } )$ of smooth functions on $\bar { \mathcal { O } }$ to be the space of Whitney smooth functions. Recall that a continuous map $f : { \bar { \mathcal { O } } }  { \bar { \mathbf { R } } }$ is called Whitney smooth if and only if there exists a function $F \in C ^ { \infty } ( { \mathfrak { h } } ^ { * } )$ such that $F | _ { \bar { \mathcal { O } } } = f$

It is easy to see that $C ^ { \infty } ( { \bar { \mathcal { O } } } )$ is naturally a Poisson algebra. Indeed, since the coadjoint orbits are the symplectic leaves of the Poisson structure on ${ \mathfrak { h } } ^ { * }$ ， for all $\pmb { F }$ ， $G \in C ^ { \infty } ( { \mathfrak { h } } ^ { * } )$ and ${ \pmb x } \in \bar { \mathcal { O } }$ the bracket $\{ F , G \} ( { \pmb x } )$ depends only on the restrictions of $\pmb { F }$ and $G$ to the coadjoint orbit of $\pmb { x }$ ,which is contained in $\bar { \mathcal { O } }$ Thus the bracket $\{ \cdot , \cdot \} _ { \bar { \mathcal { O } } }$ given by

$$
\{ F | _ { \bar { \mathcal { O } } } , G | _ { \bar { \mathcal { O } } } \} _ { \bar { \mathcal { O } } } ( x ) : = \{ F , G \} ( x )
$$

is well-defined. The partition of $\bar { \mathcal { O } }$ into coadjoint orbits is a decomposition. The local finiteness follows from the assumption that $H$ is reductive. The proof of the fact that $\bar { \mathcal { O } }$ is a stratifed space requires some machinery.

2.24.DEFINITION．Let $X$ be a subspace of $\mathbf { R } ^ { n }$ ． A decomposition of $X$ is called a Whitney stratification if the pieces of $X$ are smooth submanifolds of $\mathbf { R } ^ { n }$ and if for each pair of pieces $P , Q$ with $P \leq Q$ the following condition of Whitney holds:

WHITNEY's CONDITION B. Let $\pmb { p }$ be an arbitrary point in $P$ and let $\{ p _ { i } \}$ and $\left\{ q _ { i } \right\}$ be sequences in $P$ ，resp. $Q$ ，both converging to $\pmb { p }$ Assume that the lines $l _ { i }$ joining ${ \mathfrak { p } } _ { \mathfrak { i } }$ and ${ { q } _ { i } }$ converge (in the projective space $\mathbf { R } P ^ { n - 1 } .$ toa line $l$ ,and that the tangent planes $T _ { q _ { i } } Q$ converge (in the Grassmannian of $( \dim Q )$ -planes in $\mathbf { R } ^ { n }$ ) to a plane $\tau$ . Then $\iota$ is contained in $\tau$

It follows from Mather's theory of control data (see [14]) that a Whitney stratified subset of Euclidean space is a stratifed space in the sense of our Definition 2.6. An outline of the argument can be found in [8, page 40]. So it suffices to show that $\bar { \mathcal { O } }$ is a Whitney stratified space.

Since $H$ is reductive,the coadjoint representation $A d ^ { * } : H \to G l ( \mathfrak { h } ^ { * } )$ is algebraic,i.e., the image $A d ^ { * } ( H )$ is an algebraic subgroup of $G l ( { \mathfrak { h } } ^ { * } )$ and the coadjoint action of $A d ^ { * } ( H )$ on ${ \mathfrak { h } } ^ { * }$ is algebraic (see e.g. [23] for a proof). Now a coadjoint orbit $A d ^ { * } ( H ) \cdot q , q \in \mathfrak { h } ^ { * }$ ,issemialgebraic by the Seidenberg-Tarski theorem, since it is the image of $A d ^ { * } ( H )$ under the algebraic map‘evaluation at $\pmb q ^ { \prime }$ ，which sends $a \in A d ^ { * } ( H )$ to $a \cdot q$ Let $\mathcal { O } _ { 1 }$ and $\mathcal { O } _ { 2 }$ be two orbits in $\bar { \mathcal { O } }$ with $\mathcal { O } _ { 1 }$ contained in the closure of $\mathcal { O } _ { 2 }$ . The two orbits are smooth and semialgebraic. Therefore a theorem of Wall [24,p. 337] applies. In this case the theorem says that Whitney's condition B for the pair $( \mathcal { O } _ { 1 } , \mathcal { O } _ { 2 } )$ holds at all points of $\mathcal { O } _ { 1 }$ except possibly for the points in a semialgebraic subvariety of dimension strictly less than the dimension of $\mathcal { O } _ { 1 }$ . In particular condition B holds at some point of $\mathcal { O } _ { 1 }$ . But the pair $( \mathcal { O } _ { 1 } , \mathcal { O } _ { 2 } )$ is $H$ -homogeneous, so condition B holds everywhere. This proves that $\bar { \mathcal { O } }$ isa Whitney stratified space. □

# 3Reduction of Cotangent Bundles

# 3.1 The Cotangent Bundle of a Quotient Variety

We have seen in Section 1 that the singular reduced space $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ is a symplectic orbifold. There are a few other interesting examples of singular reduced spaces coming from reduction of cotangent bundles which turn out to be orbifolds. In order to understand what makes these examples work it will be helpful to consider lifted actions on cotangent bundles in general. (We caution the reader that not every reduced space is an orbifold; see [5] for a counterexample.） Let $G$ be a Lie group acting smoothly and properly on a smooth manifold $X$ . Let $\pmb { x }$ be a point in $\boldsymbol { x }$ and $\pmb { H }$ the stabilizer of $\pmb { x }$ in $G$ ．Since the action is proper $H$ is compact.Therefore there exists an $H$ -equivariant splitting of the tangent space to $\boldsymbol { x }$ at $\pmb { x }$ ：

$$
T _ { x } X = T _ { x } ( G \cdot x ) \oplus V
$$

where $V$ is some subspace of the tangent space. Let $B$ be a small $H$ -invariant ball in $V$ centered at the origin.The slice theorem asserts that a neighbourhood of the orbit $G \cdot x$ in $\boldsymbol { x }$ is $G$ -equivariantly diffeomorphic to the associated bundle $G \times _ { H } B$

If the action of $G$ is free,it follows from the slice theorem that $X$ isa principal $G$ -bundle over the orbit space $Q = X / G$ . Lift the action of $G$ to an action on the cotangent bundle. It is well-known (see e.g.[1]) that in this case the reduced space at the zero level is simply the cotangent bundle of the base, $( T ^ { * } X ) _ { 0 } = T ^ { * } Q$ . This result has been recently generalized by Emmrich and Romer [6] to the case when the action of $G$ on $X$ is of constant orbit type,that is,there exists a subgroup $\pmb { H }$ of $G$ such that for any ${ \pmb x } \in { \pmb X }$ the orbit $G \cdot \pmb { x }$ is diffeomorphic to the homogeneous space $G / H$ . Alternatively, by virtue of the slice theorem,the action of $G$ on $X$ is of constant orbit type if and only if $X$ is a fibre bundle over the orbit space $Q = X / G$ with typical fibre $G / H$ . Emmrich and Romer showed that in this case the reduced space $( T ^ { * } X ) _ { 0 }$ is again $T ^ { * } Q$ ,the cotangent bundle of the orbit space.

Let us now consider the general case of an action of $G$ on $\boldsymbol { X }$ ,that is,we make no assumption concerning the structure of the orbits. Lift the action of $G$ to an action on the cotangent bundle $\mathbf { \nabla } T ^ { * } X$ and let $J : T ^ { * } X \to { \mathfrak { g } } ^ { * }$ be the corresponding moment map.Recall that for $( { \pmb x } , { \pmb \eta } ) \in T _ { { \pmb x } } ^ { * } X$ the value of $J$ is defined by

$$
\langle \xi , J ( x , \eta ) \rangle = - \langle \xi x ( x ) , \eta \rangle ,
$$

where $\langle \cdot , \cdot \rangle$ on the left hand side of the equation denotes the pairing between the Lie algebra $\pmb { \mathfrak { g } }$ and its dual,and on the right hand side the pairing between the tangent and the cotangent spaces of $\boldsymbol { x }$ at $\pmb { x }$ ，while $\xi _ { X } ( { \pmb x } )$ is the vector obtained by evaluating at $\pmb { x }$ the vector feld defined by the infinitesimal action ${ \pmb \xi }$ on $X$ . Let us compute the zero level set of the moment map. It follows from (7) that

$$
J ^ { - 1 } ( 0 ) \cap T _ { x } ^ { * } X = \{ \eta : \langle \xi _ { X } ( x ) , \eta \rangle = 0
$$

We have proved:

3.1.LEMMA. Let $J : T ^ { * } X \to { \mathfrak { g } } ^ { * }$ be the moment map induced by the lift of the action $G$ on $\boldsymbol { x }$ to an action on $\mathbf { \nabla } T ^ { * } X$ . Then the intersection of the zero level set of the moment map with the fibre of the cotangent space at a point ${ \pmb x } \in { \pmb X }$ is $( T _ { x } ( G \cdot x ) ) ^ { \circ }$ ,the annihilatorof the tangent space to theorbit through $\pmb { x }$ . Consequently,

$$
J ^ { - 1 } ( 0 ) = \coprod _ { x \in X } ( T _ { x } ( G \cdot x ) ) ^ { \circ } .
$$

3.2.REMARk. It follows from the description (8) of the zero level set that it retracts onto $X$ . In particular, if $X$ is connected then the level set $J ^ { - 1 } ( 0 )$ is connected as well.

For a point $\pmb { x }$ in $X$ we call the orbit space $( T _ { x } ( G \cdot x ) ) ^ { \circ } / G _ { x }$ the cotangent cone of $X / G$ at the point $G \cdot x \in X / G$ .It is easy to see that this definition does not depend on the choice of the point ${ \pmb x } \in G \cdot { \pmb x } .$ ,i.e.,if ${ \pmb x } ^ { \prime } = { \pmb a } \cdot { \pmb x }$ for some ${ \pmb a } \in G$ ,then multiplication by $\pmb { a }$ induces an isomorphism between the orbit spaces $( T _ { x } ( G \cdot x ) ) ^ { \circ } / G _ { x }$ and $( T _ { x ^ { \prime } } ( G \cdot x ^ { \prime } ) ) ^ { \circ } / G _ { x ^ { \prime } }$ .Moreover, the quotient

$$
J ^ { - 1 } ( 0 ) / G = \biggl ( \prod _ { x \in X } ( T _ { x } ( G \cdot x ) ) ^ { \circ } \biggr ) \bigg / G
$$

is set-theoretically the disjoint union of all cotangent cones to $X / G$ . Therefore the following definition makes sense.

3.3.DEFINITION. The cotangent bundle of an orbit space $X / G$ is the stratified symplectic space $T ^ { * } ( X / G ) : = J ^ { - 1 } ( 0 ) / G$

3.4. ExAMPLE. Suppose that $G$ is finite. Then $J \ = \ 0$ ，s0 $T ^ { * } ( X / G ) : =$ $J ^ { - 1 } ( 0 ) / G = T ^ { * } ( X ) / G$

3.5.REMARK.The cotangent bundle $T ^ { * } ( X / G )$ is not a locally trivial bundle over the base variety $X / G$ , since the fibres may vary from point to point. Nor is the projection $T ^ { * } ( X / G ) \to X / G$ a stratification-preserving map.

3.6.EXAMPLE. Let $X =  { \mathbf { R } } ^ { 2 }$ and let $G = S O ( 2 )$ act on $X$ in the standard way. Then the quotient $X / G$ is a closed half-line $[ 0 , \infty )$ . It consists of two strata: the end-point $\{ 0 \}$ and the open half-line $( 0 , \infty )$ . We saw in Section 1 that the cotangent bundle $T ^ { * } ( X / G )$ of the half-line is a cone.The fibre $\pi ^ { - 1 } ( x )$ of the projection $\pi : T ^ { * } ( X / G ) \to X / G$ is a line if ${ \pmb x } \in ( { \pmb 0 } , \infty )$ ，but it is a closed half-line if ${ \pmb x } = { \pmb 0 }$ . So $T ^ { * } ( X / G )$ is not a locally trivial bundle over $X / G$ . Notice that $\pi ^ { - 1 } ( 0 )$ intersects the top stratum of $T ^ { * } ( X / G )$ . So the preimage of the stratum $\{ 0 \}$ is not a union of strata.

It seems unlikely to us that the smooth structure of a cotangent bundle $T ^ { * } ( X / G )$ depends on the way in which the orbit space $X / G$ is written as a quotient. More precisely, we make the following

3.7.CONJECTURE. Let $G$ and $\pmb { H }$ beLie groups and let $\boldsymbol { X }$ ,resp. $Y$ ,besmooth manifolds on which $G$ ，resp. $H$ act properly. Assume that the orbit spaces $X / G$ and $Y / H$ are diffeomorphic in the sense that there exists a homeomorphism $\phi : X / G \to Y / H$ such that the pullback map $\phi ^ { * }$ isan isomorphism from $C ^ { \infty } ( Y / H ) : = C ^ { \infty } ( Y ) ^ { H }$ to $C ^ { \infty } ( X / G ) : = C ^ { \infty } ( X ) ^ { G }$ . Then the cotangent bundles of $X / G$ and $Y / H$ are isomorphic in the sense of Defnition 2.14.

In his unpublished thesis [19], Schwarz showed that modulo some assumptions $T ^ { * } ( X / G )$ and $T ^ { * } ( Y / H )$ are homeomorphic if $X / G$ and $Y / H$ are diffeomorphic. In the next sections we prove a version of this result and provide some experimental evidence for Conjecture 3.7.

# 3.2 Cross-sections

Let $\boldsymbol { x }$ be a smooth manifold and $G$ a Lie group acting on $\boldsymbol { x }$ .Often one can compute the cotangent bundle of the quotient variety $X / G$ by means of a cross-section of the $G$ -action, i.e.,a pair $( Y , H )$ ，where $\boldsymbol { Y }$ is an embedded submanifold of $\boldsymbol { x }$ and $H$ a Lie group acting on $\boldsymbol { Y }$ such that every $G$ -orbit in $X$ intersects $\boldsymbol { Y }$ in exactly one $H$ -orbit.If $( Y , H )$ is a cross-section,it is easy to see that the natural map $Y / H \to X / G$ is a homeomorphism. $\mathbf { O n }$ an additional assumption we show now that the cotangent bundles $T ^ { * } ( X / G )$ and $T ^ { * } ( Y / H )$ are also homeomorphic.

3.8.PROPOSITION. Let $X$ be a Riemannian $G$ -manifold. Assume that $( Y , H )$ is a cross-section of the $G$ -action on $\boldsymbol { x }$ .Assume further that the cross-section is orthogonal in the sense that for all $\pmb { y }$ in $\boldsymbol { Y }$

$$
T _ { y } ( G \cdot y ) = \left( ( T _ { y } Y ) ^ { \perp } \cap ( T _ { y } G \cdot y ) \right) \oplus \left( T _ { y } Y \cap T _ { y } ( G \cdot y ) \right) .
$$

Then the inclusion $Y \subset X$ induces a homeomorphism $( T ^ { * } Y ) _ { 0 } \xrightarrow { \simeq } ( T ^ { * } X ) _ { 0 }$

3.9.REMARK. Suppose the cross-section $Y$ is the set of fixed points for some subgroup $K$ of $G$ .Let $H$ be the‘Weyl group' $N ( K ) / K$ .The statement (9) regarding the orthogonality of the intersections of the $G$ -orbits with $\boldsymbol { Y }$ holds automatically in this case. This follows easily from the proof of the slice theorem.

PROOF. The metric allows us to identify equivariantly tangent and cotangent bundles of $X$ and of $\boldsymbol { Y }$ , giving rise to a symplectic embedding

$$
T ^ { * } Y \simeq T Y \hookrightarrow T X \simeq T ^ { * } X .
$$

Let $J _ { X } : T X \to { \mathfrak { g } } ^ { * }$ and $J _ { Y } : T Y \to { \mathfrak { h } } ^ { * }$ denote the moment maps. Let $\pmb { y }$ be a point in $\boldsymbol { Y }$ . Since the orbit $G \cdot y$ intersects $Y$ in a single $H$ -orbit,(9) implies that

$$
T _ { y } ( G \cdot y ) = \left( ( T _ { y } Y ) ^ { \perp } \cap ( T _ { y } G \cdot y ) \right) \oplus ( T _ { y } ( H \cdot y ) )
$$

is an orthogonal decomposition. Hence $( T _ { y } ( G \cdot y ) ) ^ { \perp } = V _ { 1 } \oplus V _ { 2 }$ ，where $V _ { 1 } =$ $( T _ { y } H \cdot y ) ^ { \perp } \cap T _ { y } Y$ and $V _ { 2 } = ( T _ { y } G \cdot y ) ^ { \perp } \cap ( T _ { y } Y ) ^ { \perp }$ ,so that

$$
J _ { X } ^ { - 1 } ( 0 ) \cap T _ { y } ^ { * } X = V _ { 1 } \oplus V _ { 2 }
$$

and

$$
J _ { Y } ^ { - 1 } ( 0 ) \cap T _ { y } ^ { * } Y = V _ { 1 } .
$$

This gives us an inclusion $J _ { Y } ^ { - 1 } ( 0 ) \to J _ { X } ^ { - 1 } ( 0 )$ . Composing with the orbit map $J _ { X } ^ { - 1 } ( 0 )  J _ { X } ^ { - 1 } ( 0 ) / G = ( T ^ { * } X ) _ { 0 }$ gives us a map from $J _ { Y } ^ { - 1 } ( 0 )$ to $( T ^ { * } X ) _ { 0 }$ .We claim that this map descends to a map from $J _ { Y } ^ { - 1 } ( 0 ) / H$ to $( T ^ { * } X ) _ { 0 }$ . Indeed, suppose $( y ^ { \prime } , \eta ^ { \prime } )$ and $( \pmb { y } , \pmb { \eta } )$ are two points in $J _ { Y } ^ { - 1 } ( 0 )$ and $\pmb { a } \cdot ( \pmb { y } ^ { \prime } , \pmb { \eta } ^ { \prime } ) = ( \pmb { y } , \pmb { \eta } )$ for some $a \in H$ .By assumption $G \cdot y \cap Y = H \cdot y$ ,so there is $b \in G$ with $\pmb { b } \cdot \pmb { y } ^ { \prime } = \pmb { y }$ It is therefore no loss of generality to assume that $\boldsymbol { y } = \boldsymbol { y } ^ { \prime }$ . In this case $\eta$ and $\eta ^ { \prime }$ both lie in $V _ { 1 }$ and $\textbf { \em a } \in \boldsymbol { H } _ { y }$ . Locally near $\pmb { y }$ the space $Y$ is $\pmb { H }$ -equivariantly diffeomorphic to the associated bundle $H \times _ { H _ { y } } V _ { 1 }$ , so locally

$$
Y / H \simeq ( H \times _ { H _ { y } } V _ { 1 } ) / H = V _ { 1 } / H _ { y } .
$$

Here $H _ { y }$ denotes the stabilizer of $\pmb { y }$ in $H$ . Similarly,

$$
X / G \simeq ( G \times _ { G _ { y } } ( V _ { 1 } \oplus V _ { 2 } ) ) / G = ( V _ { 1 } \oplus V _ { 2 } ) / G _ { y } ,
$$

where $G _ { y }$ denotes the stabilizer of $\pmb { y }$ in $G$ . We have assumed that $( Y , H )$ is a cross-section for the $G$ -action,and therefore $X / G \simeq Y / H$ . It follows that $\eta , \eta ^ { \prime } \in V _ { 1 }$ lie in the same $H _ { y }$ -orbit ifandonly if $\eta , \eta ^ { \prime } \in V = V _ { 1 } \oplus V _ { 2 }$ lie in the same $G _ { y }$ orbit.We conclude that there is $\mathbf { c } \in G$ with $\mathbf { c } \cdot ( y , \eta ) = ( y ^ { \prime } , \eta ^ { \prime } )$ ， thereby proving the existence of a continuous map

$$
\varphi : ( T ^ { * } Y ) _ { 0 } = J _ { Y } ^ { - 1 } ( 0 ) / H  ( T ^ { * } X ) _ { 0 } .
$$

A similar argument shows that $\varphi$ is bijective and that $\varphi ^ { - 1 }$ is continuous.

3.10.REMARK.This proof shows that each $G$ orbit in $J _ { X } ^ { - 1 } ( 0 )$ intersects $J _ { Y } ^ { - 1 } ( 0 )$ in a single $H$ -orbit,in other words,that the pair $( J _ { Y } ^ { - 1 } ( 0 ) , H )$ isa cross-section of the $G$ -action on $J _ { X } ^ { - 1 } ( 0 )$ ·

# 3.3 Row, Row, Row your Boat

Let $X$ be the unit two-sphere in $\mathbb { R } ^ { 3 }$ and let $G$ be the circle acting on $X$ by rotations on the $_ { z }$ -axis. The space $\boldsymbol { x }$ is the configuration space of the spherical pendulum and $G$ is its group of symmetries.Now let $Y$ be a great circle through the poles and let $H$ be the group $\mathbf { Z _ { 2 } }$ acting on $\boldsymbol { Y }$ by reflection in the $_ { z }$ -axis. Then the pair $( Y , H )$ is obviously an orthogonal cross-section of the $G$ -action on $\boldsymbol { x }$ .Let $J _ { X }$ be the momentum map of the lifted action of $G$ on $\pmb { T } ^ { * } X$ . The lifted action of $\pmb { H }$ on $T ^ { \ast } Y$ has trivial momentum map, since $H$ is finite. By Proposition 3.8,the pair $( T ^ { * } Y , H )$ is a cross-section for the $G$ -action on $J _ { X } ^ { - 1 } ( 0 )$ . The physical meaning of this fact is that a spherical pendulum with zero angular momentum is just a planar pendulum.

Let us describe the orbifold $( T ^ { * } Y ) / H$ in some detail. We identify the meridian $Y$ with $S ^ { 1 } = \left\{ { e } ^ { i \theta } : \theta \in \mathbf { R } \right\}$ in such a manner that the south pole is mapped to $1 \in S ^ { 1 }$ . We cover $( T ^ { * } Y ) / H = ( S ^ { 1 } \times \mathbf { R } ) / \mathbf { Z _ { 2 } }$ with two orbifold charts. The domain of both charts is the strip $D = ( - \pi , \pi ) \times \mathbf { R } \subset \mathbf { R } ^ { 2 }$ equipped with the $\mathbf { Z _ { 2 } }$ -action generated by reflection in the origin. The chart maps $\psi _ { 1 }$ and $\psi _ { 2 }$ are given by:

$$
\begin{array} { r } { \begin{array} { r l } & { \psi _ { 1 } : D \to ( S ^ { 1 } \times { \bf R } ) / { \bf Z } _ { 2 } , \quad ( \theta , r ) \mapsto [ e ^ { i \theta } , r ] , } \\ & { \psi _ { 2 } : D \to ( S ^ { 1 } \times { \bf R } ) / { \bf Z } _ { 2 } , \quad ( \theta , r ) \mapsto [ - e ^ { i \theta } , r ] , } \end{array} } \end{array}
$$

where $[ x , y ]$ denotes the equivalence class of $( x , y ) \in S ^ { 1 } \times \mathbf { R }$ . It is easy to write down the transition map from one chart to the other. The resulting space has the shape of a‘canoe’with two isolated conical singularities. We encourage the reader to construct this orbifold with paper and glue.

We claim that the natural homeomorphism

$$
\phi : ( T ^ { * } Y ) / H = T ^ { * } ( Y / H ) \to T ^ { * } ( X / G )
$$

is an isomorphism of reduced spaces.It obviously suffices to show that $\phi :$ $O _ { i } \to \phi ( O _ { i } )$ is an isomorphism,where $O _ { i } = \psi _ { i } ( D )$ for $\dot { \iota } = 1$ ,2. Note that $\phi ( \psi _ { i } ( D ) )$ is the space obtained by reducing $T ^ { * } ( X - \{ * \} )$ at zero, where $\{ * \}$ is either the south or the north pole of the sphere $X$ ,depending on whether ${ \dot { \mathfrak { z } } } = 1$ or 2.But $X - \{ * \}$ is $G$ -equivariantly diffeomorphic to the plane $\scriptstyle \mathbf { R } ^ { 2 }$ ,if we let $G = S O ( 2 )$ act on $\scriptstyle \mathbf { R } ^ { 2 }$ in the standard fashion.So the maps $\phi : O _ { i } \to$ $\phi ( O _ { i } )$ are,up to changes of coordinates,equal to the map $\mathbf { R } ^ { 2 } / \mathbf { Z } _ { 2 }  ( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ exhibited in Section 1,which is an isomorphism. Therefore,the map (10) is also an isomorphism.

The two isolated singularities of the ‘canoe’are relative equilibria of the spherical pendulum. Both are actually absolute equilibria, corresponding to the pendulum pointing straight up or down. For an alternative computation of the ‘canoe' using invariant polynomials,see [3].

# 3.4Reduction of the Cotangent Bundle of a Symmetric Space

Consider the special orthogonal group $S O ( n )$ acting by conjugation on $S ^ { 2 } ( \mathbf { R } ^ { n } )$ the space of real symmetric $\textit { \textbf { n } } \times \textit { \textbf { n } }$ -matrices. Let $S _ { n }$ denote the symmetric group on $\pmb { n }$ letters acting on $\mathbf { R } ^ { n }$ by permuting the coordinates and hence on ${ \pmb T } ^ { * } { \pmb R } ^ { n }$ by permuting the coordinates in pairs. Note that $\mathbf { R } ^ { n }$ embeds into $S ^ { 2 } ( \mathbf { R } ^ { n } )$ as the set of diagonal matrices. Since any symmetric matrix is diagonalizable, the pair $( \mathbf { R } ^ { n } , S _ { n } )$ is a cross-section of the $S O ( n )$ -action on $S ^ { 2 } ( \mathbf { R } ^ { n } )$ . Therefore $S ^ { 2 } ( \mathbf { R } ^ { n } ) / S O ( n )$ is homeomorphic to $\mathbf { R } ^ { n } / S _ { n }$ .The vector space $S ^ { 2 } ( \mathbf { R } ^ { n } )$ has a natural $S O ( n )$ -invariant inner product:

$$
( ( a _ { i j } ) , ( b _ { k l } ) ) = \mathrm { t r a c e } ( ( a _ { i j } ) ( b _ { k l } ) ) = \sum _ { i j } a _ { i j } b _ { i j } .
$$

Remark 3.9 implies that the cross-section $( \mathbf { R } ^ { n } , S _ { n } )$ is orthogonal． Therefore Proposition 3.8 provides us with a homeomorphism $\phi : ( T ^ { * } \mathbf { R } ^ { n } ) _ { 0 } \ \to$ $( T ^ { * } S ^ { 2 } ( \mathbf { R } ^ { n } ) ) _ { 0 }$ . We contend that $\phi$ is an isomorphism of reduced spaces. Since the group $S _ { n }$ is finite,the zero level set of the $S _ { n }$ -moment map is the whole space $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ , which embeds naturally into $T ^ { * } S ^ { 2 } ( \mathbf { R } ^ { n } ) \simeq S ^ { 2 } ( \mathbf { R } ^ { n } ) \times S ^ { 2 } ( \mathbf { R } ^ { n } )$ In fact $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ is a subset of the zero level set of the $S O ( n )$ -moment map $J : T ^ { * } S ^ { 2 } ( \mathbf { R } ^ { n } ) \ \to \ 5 0 ( n ) ^ { * }$ .Clearly any $S O ( n )$ -invariant function on $T ^ { * } S ^ { 2 } ( \mathbf { R } ^ { n } )$ restricts to an $S _ { n }$ -invariant function on $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ . This implies that $\phi ^ { * } C ^ { \infty } ( ( T ^ { * } S ^ { 2 } ( \mathbf { R } ^ { n } ) ) _ { 0 } )$ is contained in $C ^ { \infty } ( ( T ^ { * } \mathbf { R } ^ { n } ) _ { 0 } ) = C ^ { \infty } ( \mathbf { R } ^ { n } \times \mathbf { R } ^ { n } ) ^ { S _ { n } }$ To show that $\phi$ is an isomorphism of reduced spaces we need to prove that $\phi ^ { * } C ^ { \infty } ( T ^ { * } S ^ { 2 } ( \mathbf { R } ^ { n } ) )$ is equal to $C ^ { \infty } ( ( T ^ { * } \mathbf { R } ^ { n } ) _ { 0 } )$ . By the same argument as the one we have used in the example of Section 1,it is enough to show that there is a set $\{ \sigma _ { i j } \}$ of polynomials that generates the $S _ { n }$ -invariant polynomials on $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ and has the property that each $\sigma _ { i j }$ is the restriction of an $S O ( n )$ -invariant polynomial on $S ^ { 2 } ( \mathbf { R } ^ { n } ) \times S ^ { 2 } ( \mathbf { R } ^ { n } )$ ."According to Weyl [25], the polynomials

$$
\sigma _ { k l } ( x , y ) = \sum _ { i j } x _ { i } ^ { k } y _ { j } ^ { l } , \quad 1 \leq k , l \leq n ,
$$

generate the $S _ { n }$ -invariant polynomials on $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n }$ . On the other hand, $\sigma _ { k l }$ is the restriction of the $S O ( n )$ -invariant polynomial $\tau _ { k l } ( A , B ) = \mathrm { t r a c e } ( A ^ { k } B ^ { l } ) .$ so the polynomials (11) are the required set.We have thus proved that

$$
( T ^ { \ast } S ^ { 2 } ( \mathbf { R } ^ { n } ) ) _ { 0 } \simeq ( \mathbf { R } ^ { n } \times \mathbf { R } ^ { n } ) / S _ { n }
$$

as stratified symplectic spaces.

More generally, let $G$ be a semisimple Lie group over $\mathbf { R } , K$ a maximal compact subgroup of $G$ and ${ \mathfrak { g } } = { \mathfrak { k } } \oplus { \mathfrak { p } }$ a Cartan decomposition of ${ \mathfrak { g } } = L i e ( G )$ . Then $K$ acts on $\mathfrak { p }$ by conjugation. Pick a maximal abelian subspace $\pmb { \mathfrak { a } }$ of $\mathfrak { p }$ and let $W = N ( { \mathfrak { a } } ) / C ( { \mathfrak { a } } )$ denote the Weyl group.It is well-known that the restriction map $\mathbf { R } [ \mathfrak { p } ] \to \mathbf { R } [ \mathfrak { a } ]$ from polynomials on $\mathfrak { p }$ to polynomials on ${ \pmb a }$ gives rise to an isomorphism $\mathbf { R } [ \mathfrak { p } ] ^ { K } \to \mathbf { R } [ \mathfrak { a } ] ^ { W }$ . The quotient spaces ${ \mathfrak { a } } / W$ (the Weyl chamber)and ${ \mathfrak { p } } / K$ are therefore isomorphic. The computation above verifies Conjecture 3.7 in the special case ${ \cal G } = S l ( n , { \bf R } )$ ,showing that we have an isomorphism of cotangent bundles, $( T ^ { * } \mathfrak { a } ) / W = T ^ { * } ( \mathfrak { a } / W ) \cong T ^ { * } ( \mathfrak { p } / K )$ For arbitrary $G$ ,Conjecture 3.7 would follow from (but is not equivalent to):

3.11. CoNJECTURE. The restriction map $\mathbf { R } [ { \mathfrak { p } } \times { \mathfrak { p } } ] ^ { K } \to \mathbf { R } [ { \mathfrak { a } } \times { \mathfrak { a } } ] ^ { W }$ is surjective.

# 4Poisson Embeddings of Reduced Spaces

The goal of this section is to show that in some cases a reduced space of a symplectic representation space can be realized as the closure of a coadjoint orbit in the dual of some Lie algebra (cf. Section 2.4). For the remainder of this section,let $K$ be a compact group acting linearly on a symplectic vector space $V$ and preserving its symplectic form $\omega$ . Then the action of $K$ is

Hamiltonian. Let $J : V \to { \ell ^ { * } }$ denotes the corresponding moment map. The ring of invariant polynomials $\mathbf { R } [ V ] ^ { K }$ is finitely generated.We now make the following assumption:

AsSUMPTION Q. The ring of all $K$ -invariant polynomials on $V$ is generated by the homogeneous quadratic $K$ -invariant polynomials.

The space of homogeneous quadratic polynomials, ${ \bf R } _ { 2 } [ V ]$ ，and the space of invariant polynomials are both closed under the Poisson bracket.It follows that their intersection,

$$
\begin{array} { r } { \mathfrak { h } : = \mathbf { R } _ { 2 } [ V ] ^ { K } , } \end{array}
$$

which is the space of invariant homogeneous quadratic polynomials,is also closed under the Poisson bracket.The algebra ${ \bf R } _ { 2 } [ V ]$ is canonically isomorphic to the Lie algebra ${ \mathfrak { s p } } ( V )$ of all infinitesimally symplectic linear transformations: the isomorphism takes a quadratic polynomial to its associated Hamiltonian vector field. The inverse map sends $\pmb { \xi } \in \mathfrak { s p } ( V , \omega )$ to the polynomial $1 / 2 \omega ( \xi v , v )$ . Thus we can view $\mathfrak { h }$ as a subalgebra of ${ \mathfrak { s p } } ( V )$

Consider the map $\sigma : V \to { \mathfrak { h } } ^ { * }$ defined by

$$
\langle \sigma ( v ) , P \rangle = P ( v )
$$

where $P \in { \mathfrak { h } }$ and $\langle \cdot , \cdot \rangle$ denotes the canonical pairing of a vector space with its dual.This is the Hilbert map of classical invariant theory. It is manifestly $K$ -invariant,and so induces a map $\bar { \sigma } : V / K \to \mathfrak { h } ^ { * }$ . Assumption $\mathbf { Q }$ above implies that $\pmb { \sigma }$ separates $K$ -orbits.Thus $\bar { \pmb { \sigma } }$ is a homeomorphism onto its image $\sigma ( V ) \subset { \mathfrak { h } } ^ { * }$ .Let $H$ be the connected subgroup of $S p ( V )$ whose Lie algebra is $\mathfrak { h }$ . Note that the map $\pmb { \sigma }$ is the momentum map for the $H$ action on $V$ . It is $H$ -equivariant. (Here $\pmb { H }$ acts on ${ \mathfrak { h } } ^ { * }$ by the coadjoint action.)

4.1.REMARK.It is perhaps helpful to rephrase the above discussion in coordinates. Let $\sigma _ { 1 } , \ldots , \sigma _ { N }$ be a basis for the space $\mathfrak { h }$ of invariant homogeneous quadratic polynomials. The Poisson bracket of any two generators is again a homogeneous quadratic $K$ -invariant polynomial (or zero),which demonstrates that ${ \mathfrak { h } }$ is a Lie algebra. This Lie algebra has structure constants ${ \bf c } _ { i j } ^ { k } \in \bf R$ defined by

$$
\{ \sigma _ { i } , \sigma _ { j } \} = \sum _ { k } c _ { i j } ^ { k } \sigma _ { k } .
$$

The map $\pmb { \sigma }$ ,in terms of this choice of coordinates on ${ \mathfrak { h } } ^ { * }$ is

$$
\sigma : V \to \mathbf { R } ^ { N } , \quad v \mapsto ( \sigma _ { 1 } ( v ) , \dots , \sigma _ { N } ( v ) ) ,
$$

where we have identiffed $\mathbf { R } ^ { N }$ with ${ \mathfrak { h } } ^ { * }$ ,the isomorphism being the one associated to choosing the basis of ${ \mathfrak { h } } ^ { * }$ which is dual to the basis ${ \pmb { \sigma } } _ { i }$

4.2.REMARK.Motivated by problems in representation theory,Howe [9] defined a reductive dual pair to be a pair of reductive subgroups of $S p ( V )$ that are each other's centralizers.The groups $K$ and $H$ above clearly commute with each other and it is easy to see that $H$ is (the identity component of) the centralizer of $K$ . It is not true in general that $K$ is the centralizer of $H$ ， as the example of $K = S U ( 2 )$ acting on $V = \mathbf { C } ^ { 2 }$ clearly indicates.One can get around the problem of $K$ not being the full centralizer of $\pmb { H }$ in $S p ( V )$ by replacing it with $K ^ { \prime } : =$ the centralizer of $\pmb { H }$ in $S p ( V )$ . However,it is not at all clear why $K ^ { \prime }$ and $H$ should be reductive. Also, given a dual pair $( K , H )$ with $K$ compact, it is not clear whether the quadratic polynomials corresponding to ${ \mathfrak { h } } = L i e ( H )$ generate $\mathbf { R } [ V ] ^ { K }$

However,in three interesting physical examples of symplectic representations of $K$ satisfying condition $\mathbf { Q }$ ,the groups $K$ and $H$ do form a reductive dual pair:

1. the planar $N$ -body problem $( S O ( 2 )$ acting diagonally on $( T ^ { * } \mathbf { R } ^ { 2 } ) ^ { N } )$ ； 2. the $\pmb { d }$ -dimensional $N$ -body problem $( O ( d )$ acting diagonally on $( T ^ { * } \mathbf { R } ^ { d } ) ^ { N } )$ ,this example is worked out in the next section; 3. $U ( p )$ acting on $\mathbf { C } ^ { p } \otimes \mathbf { C } ^ { q }$ ·

These examples seem to hint at an interesting connection between reductive dual pairs and condition $\mathbf { Q }$

Now let $\scriptscriptstyle \mathcal { O }$ be a coadjoint orbit of $K$ . Consider the corresponding reduced space $V _ { \mathcal { O } } = J ^ { - 1 } ( \mathcal { O } ) / K$ . We claim that the map $\bar { \sigma } : V _ { \mathcal { O } } \to \mathfrak { h } ^ { * }$ induced by the $\pmb { H }$ -momentum map $\pmb { \sigma }$ is a Poisson embedding in the following sense.

4.3.DEFINITION.Let $X$ be a stratified symplectic space and let $P$ be a Poisson manifold．A proper Poisson embedding of $\boldsymbol { x }$ into $P$ is a proper injective map $j : X \to P$ such that

i. the pullback by $j$ of every smooth function on $P$ is a smooth function on $\boldsymbol { x }$ ； ii. the pullback map $j ^ { * } : C ^ { \infty } ( P ) \to C ^ { \infty } ( X )$ is surjective; iii. the pullback map $j ^ { \ast }$ is a morphism of Poisson algebras.

We mention a few obvious consequences of this definition: the image of a proper Poisson embedding $j : X \to P$ is closed; $j$ is a homeomorphism onto its image; the kernel of $j ^ { * }$ ，which is the set of smooth functions vanishing on the image $j ( X )$ ,is a Poisson ideal inside $C ^ { \infty } ( P )$ ； and the set of Whitney smooth functions on $j ( X )$ is a Poisson algebra,which is isomorphic to $C ^ { \infty } ( X )$ Therefore $j ( X )$ is a stratified symplectic space (stratified by the images of the strata in $X$ )and $j : X \to j ( X )$ is an isomorphism of stratified symplectic spaces.

4.4.THEOREM.Suppose that assumption $Q$ holds. Let $H$ be the closed connected Lie subgroup of $S p ( V )$ described above,and $\sigma : V \to { \mathfrak { h } } ^ { * }$ its associated momentum map.Let $\scriptscriptstyle \mathcal { O }$ be an arbitrary coadjoint orbit of $K$ .Then the following statements hold.

1. The map $\bar { \sigma } : V _ { \mathcal { O } } \to \mathfrak { h } ^ { * }$ isa proper Poisson embedding of the $K$ -reduced space $V _ { \mathcal { O } }$ (where the bracket on ${ \mathfrak { h } } ^ { * }$ is the usual Lie-Poisson bracket);   
2. Each connected component of a symplectic stratum of $V _ { \mathcal { O } }$ is mapped symplectomorphicallyby $\bar { \pmb { \sigma } }$ onto a coadjoint orbit of $\pmb { H }$ contained in $\bar { \sigma } ( V _ { \mathcal { O } } )$ ；   
3. The image $\bar { \sigma } ( V _ { \mathcal { O } } )$ of the Poisson embedding is the closure of a single coadjoint orbit of $H$ ，

PROOF.1.We check the conditions of Definition 4.3. The square of the distance to the origin in $V$ is a $K$ -invariant polynomial function.From this it follows easily that the Hilbert map $\pmb { \sigma }$ is proper.Hence the map $\bar { \boldsymbol { \sigma } } : V _ { \mathcal { O } }  \mathfrak { h } ^ { * }$ is proper. It is injective because the Hilbert map separates the $K$ -orbits. It is not hard to see from the definition of smooth functions on $V _ { \mathcal { O } }$ that $\bar { \pmb { \sigma } }$ pulls back smooth functions to smooth functions. That the pullback map $\bar { \sigma } ^ { * } : C ^ { \infty } ( \mathfrak { h } ^ { * } ) \to C ^ { \infty } ( V _ { \mathcal { O } } )$ is surjective is an easy consequence of Schwarz's theorem [20]. It is a homomorphism of Poisson algebras,because the Hilbert map $\pmb { \sigma }$ ,being the $H$ -momentum map, is a Poisson map.

2. The connected components of the symplectic strata are the symplectic leaves of the reduced space $V _ { \mathcal { O } }$ ,i.e., they are swept out by the Hamiltonian flows of smooth functions (see Lemma 2.19). Since the Poisson algebras $C ^ { \infty } ( V _ { \mathcal { O } } )$ and $C ^ { \infty } ( j ( V _ { \mathcal { O } } ) )$ are isomorphic,the embedding $j$ maps leaves onto leaves. But the leaves of ${ \mathfrak { h } } ^ { * }$ are simply the coadjoint $H$ -orbits. (Here we use that $H$ is connected.)

3.Theorem 4.6 below states that the level set $J ^ { - 1 } ( { \mathcal { O } } )$ is connected. It follows now from Theorem 2.12 that the reduced space $V _ { \mathcal { O } }$ has a connected open dense stratum $S _ { t o p }$ so the set $\bar { \sigma } ( V _ { \mathcal { O } } )$ has to be the closure of $\bar { \sigma } ( S _ { t o p } )$ , which is a single coadjoint orbit by statement 2 of this theorem.

4.5.REMARK.Denote the stratified symplectic space $\bar { \sigma } ( V _ { \mathcal { O } } )$ by $\scriptstyle { X _ { \mathcal { O } } }$ . If the group $H$ is semisimple then we use a Killing form to identify $\mathfrak { h }$ with ${ \mathfrak { h } } ^ { * }$ in an $H$ -equivariant way. If $\scriptscriptstyle \mathcal { O }$ is the zero orbit,then the image $X _ { 0 } = \sigma ( J ^ { - 1 } ( 0 ) )$ described in Theorem 4.4 is neccessarily the closure of a nilpotent orbit. This is because $J ( 0 ) = 0$ and $\sigma ( 0 ) = 0$ so that $0 \in \sigma ( J ^ { - 1 } ( 0 ) )$ . And the only orbits whose closure contains O are the nilpotent ones.

More generally $\scriptstyle { \boldsymbol { X } } _ { \mathcal { O } }$ contains a single semisimple orbit orbit $Q$ and any other orbit $P$ contained in $X _ { \mathfrak { o } }$ fibres over $Q$ . The fbration $\pi _ { P } : P \to Q$ is simply the projection of $\eta \in P$ onto its semisimple part, $\pi _ { P } ( \eta ) = \eta _ { s s }$ . The fibre of $\pi _ { P }$ is the orbit of the nilpotent part $\eta _ { n }$ of $\eta$ under the action of the stabilizer group $H _ { \eta _ { \delta \delta } }$ of $\eta _ { s s }$ . Note that $\eta _ { n }$ is nilpotent in $L i e ( H _ { \eta _ { s \theta } } )$ . It follows that one can view the map $\pi : X o  Q$ as a fibre bundle with typical fibre being the closure of a nilpotent orbit in some smaller reductive group. These facts about the structure of orbits of a semisimple group are well-known and we refer the reader to [23] for proofs and further references. It was shown in [12] that if a (co)adjoint orbit $P$ fibres over an semisimple orbit $Q$ then the fibration is symplectic. Thus the map $\pi : X o  Q$ can be viewed as a fibration of stratified symplectic spaces.

To conclude this section,we prove the connectivity statement used in the proof of Theorem 4.4. This result does not use assumption $\mathbf { Q }$

4.6.THEOREM.Let $K$ be a compact group acting linearly on a symplectic vector space $V$ and preserving its symplectic form $\omega$ .Let $J : V \to { \ell ^ { * } }$ denotes the corresponding moment map. Then for any coadjoint orbit $\scriptscriptstyle \mathcal { O }$ of $K$ the set $J ^ { - 1 } ( { \mathcal { O } } )$ is connected.

PROOF. Without loss of generality we may assume that $V$ is $\mathbf { C } ^ { n }$ with the standard symplectic form and $K$ is a subgroup of the unitary group $U ( n )$ Let $\mathcal { O }$ be a coadjoint orbit of $K$ . We will show that for any $r > 0$ the closed ball

$$
\bar { B } ( r ) = \left\{ z \in \mathbf { C } ^ { n } : | z | ^ { 2 } \leq r \right\}
$$

intersects $J ^ { - 1 } ( \mathcal { O } )$ in a connected set. Clearly this will prove the theorem.

Note first that the central circle subgroup of $U ( n )$ ，

$$
U ( 1 ) = \left\{ \left( \begin{array} { c c c } { { e ^ { i \theta } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { e ^ { i \theta } } } \end{array} \right) : \theta \in { \bf R } \right\}
$$

commutes with $\pmb { K }$ and therefore preserves the level set $J ^ { - 1 } ( { \mathcal { O } } )$ . Consider now the space $N ( r )$ obtained from $\bar { B } ( \boldsymbol { r } )$ by identifying the points on the boundary that lie in the same $U ( 1 )$ -orbit.Let $q : \bar { B } ( r )  N ( r )$ denote the quotient map. Since $J ^ { - 1 } ( \mathcal { O } )$ is $U ( 1 )$ -invariant and the fibres of $\pmb q$ are connected,the set $J ^ { - 1 } ( { \mathcal { O } } ) \cap { \bar { B } } ( r )$ is connected if and only if its image under $\pmb q$ is connected in $N ( r )$ . We will see shortly that $N ( r )$ is $K$ -equivariantly symplectomorphic to $\mathbf { C } P ^ { n } ( r )$ ,the complex projective space with the symplectic form equal to the standard one times $\pmb { r }$ . We will also see that under this identification the action of $K$ on $N ( r )$ becomes Hamiltonian with the moment map $J _ { \tau } : N ( r ) \to \ell ^ { * }$ having the property that $J _ { \tau } ^ { - 1 } ( \mathcal { O } ) = q ( J ^ { - 1 } ( \mathcal { O } ) \cap \bar { B } ( r ) )$

Consider the action of $U ( 1 )$ on $\mathbf { C } ^ { n } \times \mathbf { C }$ corresponding to the Hamiltonian $\phi ( z , w ) = | z | ^ { 2 } + | w | ^ { 2 } - r$ for $( z , w ) \in \mathbf { C } ^ { n } \times \mathbf { C }$ Then

$$
\phi ^ { - 1 } ( 0 ) = \left\{ ( z , w ) \in \mathbf { C } ^ { n } \times \mathbf { C } : | z | ^ { 2 } + | w | ^ { 2 } = r \right\}
$$

and $\phi ^ { - 1 } ( 0 ) / U ( 1 ) \simeq { \bf C } P ^ { n } ( r )$ Now, $K$ acts on $\mathbf { C } ^ { n } \times \mathbf { C }$ by acting trivally on the second factor. Since the actions of $K$ and $U ( 1 )$ on $\mathbf { C } ^ { n } \times \mathbf { C }$ commute, the action of $K$ descends to a Hamiltonian action on the reduced space $\mathbf { C } P ^ { n } ( r )$ The corresponding moment map $J _ { r }$ is obtained by extending $J : \mathbf { C } ^ { n } \to \mathbf { \mathcal { E } } ^ { * }$ by zero to a map on $\mathbf { C } ^ { n } \times \mathbf { C }$ ,restricting the extension to the sphere $\phi ^ { - 1 } ( 0 )$ and pushing it down to a map on the quotient $\mathbf { C } P ^ { n } ( r )$

To get the identification of $N ( r )$ with $\mathbf { C } P ^ { n } ( r )$ we start out by embedding $\bar { B } ( \boldsymbol { r } )$ into $\phi ^ { - 1 } ( 0 )$ via the map

$$
f : z \mapsto { \Big ( } z , { \sqrt { r - | z | ^ { 2 } } } { \Big ) } .
$$

Composing $f$ with the orbit map $\phi ^ { - 1 } \to \phi ^ { - 1 } / U ( 1 )$ we get a map $f ^ { \prime }$ from $\bar { B } ( \boldsymbol { r } )$ onto $\mathbf { C } P ^ { n } ( r )$ . It is easy to see that $f ^ { \prime }$ descends to a homeomorphism $f ^ { \prime \prime }$ from $N ( r )$ to $\mathbf { C } P ^ { n } ( r )$ . It is also easy to see that

$$
f ^ { \prime \prime } ( q ( J ^ { - 1 } ( \mathcal { O } ) \cap \bar { B } ( r ) ) ) = f ^ { \prime } ( q ( J ^ { - 1 } ( \mathcal { O } ) \cap \bar { B } ( r ) ) ) = J _ { r } ^ { - 1 } ( \mathcal { O } ) .
$$

Obviously, the moment map $J _ { \tau } : { \bf C } P ^ { n } ( r ) \to { \bf \Delta } \mathfrak { k } ^ { * }$ is proper. So Remark 2.13 implies that the set $J _ { \tau } ^ { - 1 } ( \mathcal { O } )$ is connected and we are done. □

# 5Reduced Space at Angular Momentum Zero for $\mathscr { n }$ Particles in $d$ -space

Let $V$ be the phase space for $\pmb { n }$ particles in $\pmb { d }$ -dimensional Euclidean space;

$$
\begin{array} { r l r } { V } & { = } & { T ^ { * } \mathbf { R } ^ { d } \times T ^ { * } \mathbf { R } ^ { d } \times \ldots T ^ { * } \mathbf { R } ^ { d } \quad ( n \ \mathrm { t i m e s } ) } \\ & { = } & { \mathbf { R } ^ { d } \times \mathbf { R } ^ { d } \times \ldots \mathbf { R } ^ { d } \quad ( 2 n \ \mathrm { t i m e s } ) . } \end{array}
$$

Take $G = O ( d )$ to be the orthogonal group associated to $\mathbf { R } ^ { d }$ ，with ${ \pmb g } \in G$ acting on $V$ according to

$$
g \cdot { \big ( } q _ { 1 } , p ^ { 1 } , q _ { 2 } , p ^ { 2 } , \ldots , q _ { n } , p ^ { n } { \big ) } = { \big ( } g q _ { 1 } , g p ^ { 1 } , g q _ { 2 } , g p ^ { 2 } , \ldots , g q _ { n } , g p ^ { n } { \big ) } .
$$

We will use Greek indices, $\mu , \nu$ ,etc.for the particle labels,and Latin indices $i , j$ etc. to index the coordinates on the Euclidean space $\mathbf { R } ^ { d }$ So $V$ has coordinates $( q _ { \mu } ^ { i } , p _ { j } ^ { \nu } )$ ,for $\mu , \nu = 1 , 2 , \ldots , n$ and $i , j = 1 , 2 , \ldots , d ;$ ，which shows that

$$
M \cong \mathbb { R } ^ { d } \otimes \mathbb { R } ^ { 2 n } .
$$

Under this isomorphism the $G$ -action becomes $g ( \pmb { x } \otimes z ) ~ = ~ g \pmb { x } \otimes z$ The symplectic form on $V$ is $\Omega = \Sigma _ { i , \mu } d q _ { \mu } ^ { i } \wedge d p _ { i } ^ { \mu }$ . The momentum map for the $O ( d )$ -action is

$$
J ( q , p ) = \Sigma _ { \mu } q _ { \mu } \wedge p ^ { \mu } ,
$$

where we have used the inner product on $\mathbf { R } ^ { d }$ to identify $\Lambda ^ { 2 } \mathbf { R } ^ { d }$ with the Lie algebra of $O ( d )$ and its dual space.Equation (12) expresses $V$ as the tensor product of the inner product space $\mathbf { R } ^ { d }$ with the symplectic vector space $\mathbf { R } ^ { 2 n }$ Since $\begin{array} { r } { h \in H : = S p ( n , \mathbf { R } ) } \end{array}$ acts by $\pmb { h } ( \pmb { x } \otimes \pmb { z } ) = \pmb { x } \otimes \pmb { h } \pmb { z }$ ,it is clear that the actions of $G = O ( d )$ and of $H$ commute. The momentum map for the $S p ( n , \mathbf { R } )$ -action is given by

$$
\sigma ( q , p ) = \left( \begin{array} { l l } { { q _ { \mu } \cdot q _ { \nu } } } & { { q _ { \mu } \cdot p ^ { \nu } } } \\ { { p ^ { \mu } \cdot q _ { \nu } } } & { { p ^ { \mu } \cdot p ^ { \nu } } } \end{array} \right) .
$$

Here ' denotes the inner product on $\mathbf { R } ^ { d }$ ： $q _ { \mu } \cdot q _ { \nu } = \Sigma _ { i } q _ { \mu } ^ { i } q _ { \nu } ^ { i }$ . Thus $S = \sigma ( q , p )$ is a symmetric $2 n \times 2 n$ -matrix which we have written in terms of four $n \times n -$ blocks.

In saying that $\pmb { \sigma }$ is the momentum map we are identifying the space $S ^ { 2 } ( \mathbf { R } ^ { 2 n } )$ of symmetric $2 n \times 2 n$ -matrices on $\mathbf { R } ^ { 2 n }$ with the dual of the Lie algebra of ${ \mathfrak { s p } } ( n , \mathbf { R } )$ since the target of the map $\pmb { \sigma }$ is $S ^ { 2 } ( \mathbf { R } ^ { 2 n } )$ .What is the identification $S ^ { 2 } ( \mathbf { R } ^ { 2 n } ) \cong { \mathfrak { s p } } ( n , \mathbf { R } ) ^ { * } ?$ The trace pairing (Killing form) $( S _ { 1 } , S _ { 2 } ) \mapsto \operatorname { t r a c e } S _ { 1 } S _ { 2 }$ induces an isomorphism ${ \mathfrak { s p } } ( n , \mathbf { R } ) \cong { \mathfrak { s p } } ( n , \mathbf { R } ) ^ { * }$ . The identification of $S ^ { 2 } ( \mathbf { R } ^ { 2 n } )$ with ${ \mathfrak { s p } } ( n , \mathbf { R } )$ is described by mapping $s$ to $J S$ where $J$ is the symplectic operator: $J ^ { 2 } = - 1$ ， $J J ^ { t } = I$ ， $\Omega ( v , w ) = \langle v , J w \rangle$ . Composing these identifications yields the desired one: ${ \mathfrak { s p } } ( n , \mathbf { R } ) ^ { * } \cong S ^ { 2 } ( \mathbf { R } ^ { 2 n } )$ .Under this isomorphism the coadjoint action of $S p ( n , \mathbf { R } )$ intertwines with the action $S \mapsto g S g ^ { t }$ of $S p ( n , \mathbf { R } )$ on $S ^ { 2 } ( \mathbf { R } ^ { 2 n } )$

The ‘first main theorem of invariant theory' (see e.g. [25,Theorem 2.9A]) states that the entries of $S = \sigma ( q , p )$ in the formula for $\pmb { \sigma }$ form a basis for the $O ( d )$ -invariant polynomials on $V$ . Consequently assumption $\mathbf { Q }$ of the previous section holds and so the restriction of $\bar { \pmb { \sigma } }$ to $J ^ { - 1 } ( 0 ) / O ( d )$ is an isomorphism onto its image.(As in the previous section, $\bar { \sigma } : M / O ( d )  S ^ { 2 } ( \mathbf { R } ^ { 2 } n )$ is the map induced by $\pmb { \sigma }$ ）What is its image?

Let $\Sigma \subset S ^ { 2 } ( \mathbf { R } ^ { 2 } n )$ denote the set of nonnegative symmetric matrices whose kernel is coisotropic. (This means that the kernel contains its $\pmb { \Omega }$ -orthogonal complement.）Let $\Sigma _ { k } \subset \Sigma$ denote the subset of $\Sigma$ consisting of matrices of rank $\pmb { k }$ ,and let

$$
\Sigma ^ { k } = \cup _ { i \leq k } \Sigma _ { k }
$$

denote the subset of matrices with rank at most $\pmb { k }$ As a subset of ${ \mathfrak { s p } } ( n , \mathbf { R } )$ the set $\Sigma _ { j }$ is a single coadjoint orbit,and $\Sigma ^ { k } = \overline { { \Sigma } } _ { k }$ is the union of $k + 1$ nilpotent orbits,these being the $\Sigma _ { j }$ ， $j \le k$ ，with $\Sigma _ { 0 } = \{ 0 \}$ . These are the strata of $\Sigma ^ { k }$ . We will show that $\sigma ( J ^ { - 1 } ( 0 ) ) = \Sigma ^ { k }$ where $k = \operatorname* { m i n } ( d , n )$ . Once this is shown we will have proven:

5.1.THEOREM.Let $V _ { 0 }$ denote the reduced space at angular momentum 0 for the action of $O ( d )$ on the phase space $V$ ofof $\pmb { n }$ particles in $\pmb { d }$ -space. Then $V _ { 0 }$ is isomorphic as a stratified symplectic space to the set $\Sigma ^ { k }$ described in (14)，where $k = \operatorname* { m i n } ( d , n )$ ．The isomorphism is the one induced by the $S p ( n , \mathbf { R } )$ -momentum map,namely the restriction of $\bar { \pmb { \sigma } }$ to $J ^ { - 1 } ( 0 ) / O ( d )$

PROOF.We proved in the previous section that $\pmb { \sigma }$ induces an isomorphism with all the desired properties. It remains to prove that the image of $\pmb { \sigma }$ restricted to $J ^ { - 1 } ( 0 )$ is $\Sigma ^ { k }$ . We have

$$
\sigma ( q , p ) = \left( \begin{array} { l } { q _ { 1 } } \\ { q _ { 2 } } \\ { \vdots } \\ { q _ { n } } \\ { p ^ { 1 } } \\ { p ^ { 2 } } \\ { \vdots } \\ { p ^ { n } } \end{array} \right) \left( q _ { 1 } ^ { t } q _ { 2 } ^ { t } \cdot . . . q _ { n } ^ { t } p ^ { 1 ^ { t } } p ^ { 2 ^ { t } } . . . p ^ { n ^ { t } } \right) .
$$

From this expression,it is clear that $\sigma ( q , p )$ is nonnegative. Since each of the two factors of $\sigma ( q , p )$ is a matrix with rank less than or equal to $\pmb { d }$ ,the matrix ${ \pmb \sigma } ( { \pmb q } , { \pmb p } )$ has rank less than or equal to $\pmb { d }$

5.2.REMARK. These are the only constraints on the image of $\pmb { \sigma }$ . This is the content of the the‘second main theorem of invariant theory' for the orthogonal group [25,Theorem 2.17A]. However, we do not need this result to prove our theorem,as it will in our case follow from equivariance.

Now let us restrict $\pmb { \sigma }$ to $J ^ { - 1 } ( 0 )$ . There we have $q _ { 1 } \wedge p ^ { 1 } + q _ { 2 } \wedge p ^ { 2 } + \dots q _ { n } \wedge p ^ { n } =$ 0.Let us assume for simplicity that the $q ^ { i }$ are linearly independent.Then Cartan's lemma (see e.g. [22,p.19]) states that we have $p ^ { \mu } = \Sigma S ^ { \mu \nu } q _ { \nu }$ for some symmetric $\pmb { n } \times \pmb { n }$ matrix $\boldsymbol { S }$ . A direct calculation now shows that in this case

$$
\sigma ( q , p ) = \left( \begin{array} { c c } { { M } } & { { M S } } \\ { { S M } } & { { S M S } } \end{array} \right) ,
$$

where $M _ { \mu , \nu } = q _ { \mu } \cdot q _ { \nu }$ is the matrix of inner products. Note that

$$
\sigma ( q , p ) \left( \begin{array} { r } { { S } } \\ { { - I } } \end{array} \right) = 0 ,
$$

from which it follows that the kernel of the map $\sigma ( q , p )$ contains the La-grangian subspace $\left\{ ( S y , - y ) : y \in \mathbb { R } ^ { n } \right\}$ . But any subspace containing a Lagrangian one is coisotropic,so we have proved our result in this particular case.

In general the $q ^ { \dot { \pm } }$ are not linearly independent.But a slight variant of the proof of Cartan's lemma shows us that the dimension of the space spanned by $\left\{ q _ { 1 } , q _ { 2 } , \ldots , p ^ { 1 } , p ^ { 2 } , \ldots , p ^ { n } \right\}$ is less than or equal to $\pmb { n }$ . It follows from the factorization of $\pmb { \sigma }$ that the rank of $\sigma ( q , p )$ is always less than or equal to $\pmb { n }$ . We have proved the statement regarding the rank of the matrices in $\sigma ( J ^ { - 1 } ( 0 ) )$

A few moments’reflection should convince the reader that each $\Sigma _ { j }$ isa single orbit of the $S p ( n , \mathbf { R } )$ -action on $S ^ { 2 } ( \mathbf { R } ^ { 2 } n )$ . Hint: Write $\mathbf { R } ^ { 2 n } = L _ { 1 } \oplus L _ { 2 }$ where the $L _ { i }$ are Lagrangian subspaces and $A \in \Sigma _ { j }$ annihilates $L _ { 2 }$ .Note that $S p ( n , \mathbf { R } )$ acts transitively on pairs $( L _ { 1 } , L _ { 2 } )$ of transverse Lagrangian subspaces,and that,relative to this splitting $g \oplus g ^ { t } \in S p ( n , \mathbf { R } )$ for any ${ \pmb g } \in \qquad $ $G l ( L _ { 1 } )$ . (The symplectic form allows us to identify $L _ { 2 }$ with the dual of $L _ { 1 }$ .） Now suppose that we can show that there is some matrix $A \in \Sigma _ { k } \cap \sigma ( J ^ { - 1 } ( 0 ) )$ Then it follows from the $\mathit { S p }$ -equivariance of $\pmb { \sigma }$ and the $\mathit { S p }$ -invariance of $J$ that $\Sigma _ { k } \subset \sigma ( J ^ { - 1 } ( 0 ) )$ . It is also clear that the closure of $\Sigma _ { k }$ is $\Sigma ^ { k }$ . The map $\pmb { \sigma }$ ,being homogeneous and quadratic, is a closed map. It now follows from $\Sigma _ { k } \subset \sigma ( J ^ { - 1 } ( 0 ) )$ that $\sigma ( J ^ { - 1 } ( 0 ) = \Sigma ^ { k }$ as desired. Thus all we have to do is produce a single matrix $A$ in $\Sigma _ { k }$ which we can be written in the form $\sigma ( q , p )$ for some $( q , p ) \in J ^ { - 1 } ( 0 )$ . Take $( q , p ) = ( q , 0 )$ .If $d \geq n$ ，set $q = ( e _ { 1 } , e _ { 2 } , \ldots e _ { n } )$ ， the first $\pmb { n }$ elements of an orthonormal basis $\{ ( e _ { 1 } , e _ { 2 } , \ldots , e _ { d } \}$ for $\mathbf { R } ^ { d }$ .Then (see (15))

$$
\sigma ( q , p ) = \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $\boldsymbol { I }$ is the $\textit { \textbf { n } } \times \textit { \textbf { n } }$ identity matrix. This proves the theorem for the case $d \geq n$ . In case $d < n$ ，take $\boldsymbol { q } = ( e _ { 1 } , e _ { 2 } , \ldots , e _ { d } , 0 , \ldots , 0 )$ . Then $\sigma ( q , p )$ again has the above form,except now $I$ is the $d \times d$ -identity matrix. □

5.3.REMARK. The dual pair just discussed, $( O ( d ) , S p ( n , \mathbf { R } ) )$ ,is the subject of [2].See also [9] and [10,pp.501-507].

5.4.REMARK $( O ( d )$ versus $S O ( d ) ,$ ).Suppose,in the above discussion,that we replace $O ( d )$ by the special orthogonal group $S O ( d )$ . Then the corresponding reduced space will be a branched double cover over the $O ( d )$ -reduced space.This is because $O ( d ) / S O ( d )$ is the two-element group.Assumption $\mathbf { Q }$ fails for the group $S O ( d )$ . Thus we cannot use dual pairs alone to construct its reduced space. The additional, nonquadratic invariants are the $\pmb { d }$ -ple products $\mathbf { d e t } [ v _ { 1 } , \ldots , v _ { d } ]$ ,where the $v _ { i }$ are any of the vectors $q _ { 1 } , \ldots , p ^ { n }$ . They satisfy the relation $\operatorname* { d e t } [ v _ { 1 } , \ldots , v _ { d } ] ^ { 2 } = \operatorname* { d e t } [ v _ { i } \cdot v _ { j } ]$ . In the special case $d = 2$ ， the $\pmb { d }$ -ple product is quadratic and we can realize the reduced space via dual pairs.Let us consider the case of our example in Section 1: $d = 2$ ， $\pmb { n } = 1$ The invariants were written down in Section 1.3 as $\left( \sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 } , \sigma _ { 4 } \right)$ $\pmb { \sigma _ { 3 } }$ is the 2-ple product,i.e., the signed area. The other invariants are $O ( 2 )$ -invariants. There is one relation,equation (3). It is quadratic in $\pmb { \sigma _ { 3 } }$ ,explicitly showing how the $S O ( 2 )$ -reduced space is a branched double cover of the $O ( 2 )$ -reduced space.

# References

[1] R. Abraham and J. Marsden,Foundations of Mechanics,second edition, Benjamin/Cummings,Reading,1978.   
[2] J.D. Adams, Discrete Spectrum of the Reductive Dual Pair $( O ( p , q ) , S p ( 2 m ) )$ ,Invent.Math.74 (1983),449-475.   
[3] J.Arms,R. Cushman,M. Gotay,A Universal Reduction Procedure for Hamiltonian Group Actions,preprint 591,University of Utrecht,the Netherlands,1989.   
[4] J. Arms, M. Gotay and G. Jennings, Geometric and Algebraic Reduction for Singular Momentum Maps,Advances in Mathematics 79 (1990), 43- 103.   
[5] R.Cushman and R. Sjamaar,On Singular Reduction of Hamiltonian Spaces,to appear in the proceedings of the Colloque international en l'honneur de Jean-Marie Souriau, 1990.   
[6] C.Emmrich, H. Romer,Orbifolds as Configuration Spaces of Systems with Gauge Symmetries,Commun. Math.Phys.129 (1990),69-94.   
[7] M.Goresky and R. MacPherson, Intersection Homology Theory, Topology 19 (1980),135-162.   
[8] M.Goresky and R.MacPherson， Stratified Morse Theory， Springer-Verlag,New York,1988.   
[9] R.Howe, Remarks on Classical Invariant Theory, Trans. of the AMS 313 (1989) no. 2,539-570.   
[10] D.Kazhdan,B.Kostant and S. Sternberg,Hamiltonian Group Actions and Dynamical Systems of Calogero Type, Comm. Pure Appl. Math.31 (1978), 481-507.   
[11] F.Kirwan,Cohomology of Quotients in Symplectic and Algebraic Geometry,Mathematical Notes 31,Princeton University Press,Princeton, 1984.   
[12] E.Lerman,Symplectic Fibrations and Weight Multiplicities of Compact Groups,PhD thesis,MIT,1989.   
[13] J.Marsden and A.Weinstein,Reduction of Symplectic Manifolds with Symmetry,Rep.Math.Phys.5 (1974),121-130.   
[14] J.Mather,Notes on Topological Stability,Harvard University,1970, unpublished.   
[15] J.M. Montesinos, Classical Tesselations and Three-Manifolds,Springer-Verlag,Berlin,1987.   
[16] M. Otto,A Reduction Scheme for Phase Spaces with Almost Kahler Symmetry. Regularity Results for Momentum Level Sets,J. Geom. Phys. 4 (1987),101-118.   
[17] R. S.Palais,On the Existence of Slices for Actions of Non-compact Lie Groups,Annals of Math.73 (1961),295-323.   
[18] I. Satake,On a Generalization of the Notion of Manifold, Proc. Nat. Acad. Sc.42 (1956),359-363.   
[19] G. W. Schwarz, Generalized Orbit Spaces,revised version of PhD thesis, MIT,1972,unpublished.   
[20] G.W. Schwarz, Smooth Functions Invariant under the Action of a Compact Lie Group,Topology 14 (1975),63-68.   
[21] R. Sjamaar, E. Lerman, Stratified symplectic spaces and reduction, to appear in Ann.Math.   
[22] S. Sternberg, Lectures on Differential Geometry, Chelsea,second edition, 1983.   
[23] V. S. Varadarajan, Harmonic Analysis on Real Reductive Groups,Lecture Notes in Mathematics 576,Springer-Verlag,New York,1977.   
[24] C.T. C.Wall,Regular Stratifications,in: Dynamical Systems,Warwick 1974, A. Manning, editor, Lecture Notes in Mathematics 468, Springer-Verlag,New York,1975.   
[25] H. Weyl,The Classical Groups,Princeton Univ. Press,second edition, Princeton,1939.

# Remarks on the uniqueness of symplectic blowing up

by Dusa McDuff\*

# \$1 Introduction

In [M2] we began the classification of those symplectic 4-manifolds which satisfy

Hypothesis S: $( \lor , \omega )$ contains a symplectically embedded 2-sphere with nonnegative self-intersection number.

Our results are as follows: see [M3]. By blowing down “exceptional spheres” (i.e. symplectically embedded 2-spheres with self-intersection-1), every symplectic 4-manifold may be reduced to a minimal manifold (i.e. one which contains no exceptional spheres).Moreoever,if $( \mathrm { V } , \omega )$ satisfies Hytpothesis S,so does its minimal reduction. (In fact, the class of manifolds satisfying Hypothesis S is closed under blowing up and down.） The minimal manifolds in this class are $\bf { \pmb { C P ^ { 2 } } }$ and manifolds which fiber over a Riemann surface M with fiber $\mathbb { S } ^ { 2 }$ . By analogy with the complex case,manifolds which satisfy Hypothesis S and have minimal reduction $\mathbf { \pmb { C P ^ { 2 } } }$ or $\mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 2 }$ are called rational,and those which are ${ \tt S } ^ { 2 }$ -fibrations over a Riemann surface M are said to be ruled. In the minimal, rational case on can show the symplectic form is Kähler and is uniquely determined up to diffeomorphism by its cohomology class. In the ruled case, the situation is more complicated,though uniqueness holds when the ffber $\mathbf { F }$ is not too large. Unfortunately,as Francois Lalonde has pointed out, Theorem 1.3 in [M2] does not hold as stated. The cohomological restrictions in Theorem 1.3 (i)(b) hold only when the base is a sphere, and the proof of uniqueness for bundles over Riemann surfaces of genus $\mathbf g > 0$ works only under certain cohomological restrictions.For example,in the case of the trivial bundle, it suffces that the cohomology class a of $\omega$ be such that $\mathsf { a } ( [ \mathsf { M } \times \mathsf { p t } ] ) { - } [ \mathsf { g } / 2 ] \mathsf { a } ( [ \mathsf { F } ] ) > 0$ ,and in the non-trivial case it is enough to have a $( [ \mathbf { M } _ { - } ] ) { - } [ ( \mathbf { g } { - } 1 ) / 2 ] ~ \mathsf { a } ( [ \mathrm { F } ] ) { > } 0$ ,where M_is a section with self-intersection number $^ { - 1 }$ . Full details may be found in [M4].

One outstanding question in this classification concerns the uniqueness of blowing up and down． As was pointed out in [M1],blowing up in the symplectic category is not a local operation: in order to defne a symplectic form $\tilde { \omega }$ on the manifold $\tilde { \mathsf { V } }$ ,obtained by blowing up $\mathbf { V }$ at a point, one needs to embed a whole symplectic ball into $\mathrm { v }$ . Moreoever, the radius $\lambda$ of the ball is related to the cohomology class of $\tilde { \omega }$ by the formula: ${ \tilde { \omega } } ( { \bf S } ) = \pi \lambda ^ { 2 }$ , where S is a copy of ${ \tt C P } ^ { \tt 1 }$ in the exceptional divisor $\Sigma = \mathbb { C } \mathrm { P } ^ { \mathrm { n } - 1 }$ . Conversely, in order to blow down an exceptional divisor $\Sigma$ in $\mathbf { W }$ one cuts $\mathbf { W }$ open along $\Sigma$ and glues in a large ball. We showed in [M2] that the minimal reduction of a symplectic 4-manifold $( \mathrm { V } , \omega )$ is determined up to isotopy by the homology classes of the blown down spheres. However the extent to which blowing up is unique is not yet clear.

This note begins with a careful discussion (valid in arbitrary dimensions) of the relationship between isotopy classes of symplectic forms on $\tilde { \mathsf { V } }$ and the space $\mathbf { E m b } _ { \omega } ( \mathbf { B } ( \lambda ) , \mathbf { V } )$ of symplectic embeddings of the closed $\bf { 2 n }$ -ball of radius $\lambda$ into V.Specialising to dimension 4,we then give a simpler proof of the main result of [M1] which states that there is a unique way to blow up one point in $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ . This proof extends to two points. Our result may be stated in several equivalent ways. Note that we will always assume that $\mathbb { R } ^ { 4 }$ and $\mathbf { C P ^ { 2 } }$ have their standard symplectic structures $\omega _ { 0 }$ and $\tau _ { 0 }$ ，where $\tau _ { 0 }$ is normalised so that $\tau _ { 0 } ( \mathbb { C } \mathrm { P } ^ { 1 } ) = \pi$

Theorem 1.1 (i) The space of symplectic embeddings of two disjoint balls into the open unit 4-ball Int $\mathbf { B } ^ { 4 } ( 1 ) \subset \mathbb { R } ^ { 4 }$ is connected.   
(ii) The space of symplectic embeddings of one ball into the open polydisc Int $\mathbf { B } ^ { 2 } ( \mathbf { r } _ { 1 } ) \times \mathbf { B } ^ { 2 } ( \mathbf { r } _ { 2 } ) \subset \mathbf { R } ^ { 4 }$ is connected, for any $\mathbf { r } _ { 1 } \leq \mathbf { r } _ { 2 }$   
(iii）Let ${ \bf { X } _ { k } }$ denote the manifold obtained by blowing up k points in $\mathbf { \pmb { C P ^ { 2 } } }$ .If $\mathbf { k } { = } 1$ or 2,any two cohomologous symplectic forms on ${ \bf { X } _ { k } }$ , which are rational, i.e.which satisfy Hypothesis $S$ ，are symplectomorphic. In particular, they are Kahler.

Throughout, we use the language and notation of [M2].

# \$2 Blowing up and down in the symplectic category

If $\mathbf { x }$ is any point in a symplectic manifold $( \lor , \omega )$ ，there always is an $\omega$ compatible almost complex structure $\mathbf { J }$ on $\mathbf { V }$ which is integrable near x. (Recall that ${ \bf J }$ is $\omega$ -compatible iff $\omega ( { \mathbf v } , { \mathbf J } { \mathbf v } ) > { \mathbf 0 }$ and $\omega ( { \mathbf v } , { \mathbf w } ) = \omega ( \mathbf J { \mathbf v } , \mathbf J { \mathbf w } )$ for all non-zero tangent vectors V and w.） Hence one can blow up $\mathbf { V }$ at the point $\mathbf { x }$ just as if it were a complex manifold,by replacing $\mathbf { x }$ by the copy $\pmb { \Sigma }$ of the complex projective space $\pmb { \mathbb { C } } \mathbf { P } ^ { \mathbf { n } - 1 }$ formed by all J-complex lines through the origin in the tangent space $\mathbf { T _ { x } }$ to $\mathbf { V }$ at $\mathbf { x }$ .(More precisely, one replaces a neighbourhood of $\mathbf { x }$ by a neighbourhood $\mathbf { N } ( \mathbf { Z } )$ of the zero section Z of the canonical line bundle over $\bf { \tt C P ^ { n - 1 } }$ .）Let us call this manifold $\tilde { \bf V } ( { \bf J } , { \bf x } )$ .It is easy to see that if $\mathbf { J ^ { \prime } }$ and $\mathbf { x ^ { \prime } }$ are another such pair and if $\gamma$ is a homotopy class of paths in the principal $\mathbf { S p } ( 2 \mathbf { n } , \mathbf { R } )$ -bundle $\mathbf { P }$ over $\mathbf { V }$ with endpoints lying over $\mathbf { x }$ and $\mathbf { x ^ { \prime } }$ ,then there is a diffeomorphism

$$
f _ { \gamma } : ( \tilde { \mathrm { V } } ( \mathbf { J } , \mathbf { x } ) , \Sigma )  ( \tilde { \mathrm { V } } ( \mathbf { J } ^ { ' } , \mathbf { x } ^ { \prime } ) , \Sigma ^ { \prime } )
$$

which is unique up to isotopy (Remember that the space of $\omega$ -compatible ${ \bf J }$ is contractible.） In particular,if we want to fix an identification of the exceptional divisor $\pmb { \Sigma }$ with $\bf { C P ^ { n - 1 } }$ we need to choose an identification of $\mathrm { T } _ { \mathbf { x } }$ with $\pmb { \mathbb { C } } ^ { \mathbf { n } }$ , i.e. an element $\mathbf { p }$ of $\mathbf { P }$ which lies over $\mathbf { x }$ . We will write $\tilde { \mathbf { V } } _ { \mathbf { p } }$ for the blow-up of $\mathbf { V }$ at $\mathbf { x }$ ， where $\Sigma$ is identified with $\bf { C P ^ { n - 1 } }$ via $\mathbf { p }$ ,and will write $\tilde { \mathsf { V } }$ forany manifold diffeomorphic to some $\tilde { \mathbf { V } } _ { \mathbf { p } }$

In order_to define a symplectic blow-up one also must put a symplectic form $\tilde { \omega }$ on $\tilde { \mathsf { V } }$ . It is natural to try to define $\tilde { \omega }$ so that it is standard on the exceptional divisor $\pmb { \Sigma }$ and equal to $\varphi ^ { * } \omega$ outside an e-neighbourhood of $\pmb { \Sigma }$ ， where $\varphi : \tilde { \mathsf { V } } \to \mathbf { V }$ is the obvious projection taking $\pmb { \Sigma }$ to $\mathbf { x }$ . In fact,we cannot quite do this: as mentioned above,in the symplectic category the operation of blowing up does not just change $\mathbf { V }$ at a single point but affects a whole ball around the point.

In order to explain this,we will start with blowing down. Thus we will suppose that $\pmb { \Sigma }$ is a symplectically embedded copy of $\pmb { \mathbb { C } } \mathbf { P ^ { n - 1 } }$ in a symplectic $\mathbf { 2 n } \cdot$ -dimensional manifold $( \mathbb { W } , \omega )$ ,and that the restriction $\omega | \Sigma$ is $\lambda ^ { 2 } \tau _ { 0 }$ . Further, we will suppose that $\Sigma$ has the correct normal bundle,i.e. that $\mathsf { c } _ { 1 } ( \nu _ { \Sigma } ) = - [ \tau _ { 0 } ]$ ： The standard model for $\pmb { \Sigma }$ is the zero section Z in the canonical line bundle over $\pmb { \mathbb { C } } \mathbf { P } ^ { \mathbf { n } - 1 }$ with appropriate symplectic form $\pmb { \rho } _ { \lambda }$ . We showed in [M1] that, for each $\epsilon > 0$ ，there is a symplectomorphism $\Phi _ { \epsilon }$ between the deleted $\epsilon \mathfrak { r }$ neighbourhood $\mathbf { N } _ { \epsilon } ( \mathbf { Z } ) - \mathbf { Z }$ of Z and the spherical shell $\mathbf { B } ( \lambda + \epsilon ) - \mathbf { B } ( \lambda )$ in $\mathbb { R } ^ { 2 { \mathbf { n } } }$ , where $\mathbf { B } ( \lambda )$ denotes the closed ball of radius $\lambda$ and center $\{ \boldsymbol { 0 } \}$ in $\mathbb { R } ^ { 2 { \mathbf { n } } }$ . Thus, the symplectic neighbourhood theorem implies that:

Lemma 2.1 ([M1]) For sufficiently small $\epsilon > 0$ there is a neighbourhood $\mathbf { N } _ { \epsilon } ( \Sigma )$ of $\Sigma$ in W such that $\mathrm { N } _ { \epsilon } ( \Sigma ) - \Sigma$ is symplectomorphic to $\mathbf { B } ( \lambda { + } \epsilon ) { - } \mathbf { B } ( \lambda ) \subset$ $\mathbb { R } ^ { 2 { \mathbf { n } } }$ .

Definition 2.2: blowing down Suppose that $\Sigma = \mathbb { C P } ^ { \mathrm { n - 1 } }$ is embedded in $( \mathbb { W } , \omega )$ with normal bundle as above,and let $\epsilon > 0$ be so small that Lemma 2.1 holds. Then the blow down of W along $\pmb { \Sigma }$ is obtained by cutting out $\mathbf { N } _ { \epsilon } ( \Sigma )$ from $\mathbf { W }$ and sewing $\mathbb { B } ( \lambda + \epsilon )$ back in. By arguments similar to those in Lemma 2.4 below,one can show that this construction depends only on the choice of symplectomorphism $\phi$ between $( \Sigma , \omega )$ and $\left( \mathbb { Z } , \lambda ^ { 2 } \tau _ { 0 } \right)$ In particular,it is independent of the choice both of é and of the extension of $\phi$ to $\mathbf { N } _ { \epsilon } ( \Sigma )$ which is used to define the symplectomorphism between ${ \bf N } _ { \epsilon } ( \Sigma ) - \Sigma$ and $\mathbf { B } ( \lambda + \epsilon ) - \mathbf { B } ( \lambda )$ . Note that in dimension 4, $\Sigma$ is just a symplectically embedded 2-sphere with self-intersection number $^ { - 1 }$ : such a sphere is called an exceptional sphere.

Definition 2.3: blowing up Conversely,a blow up $( \tilde { \nabla } _ { \ g } , \tilde { \omega } _ { \ g } )$ of $( \mathrm { v } , \omega )$ of weight $\lambda$ is obtained from a symplectic embedding $\pmb { \mathrm { g } }$ of the ball $\mathbf { B } ^ { 2 \mathbf { n } } ( \lambda )$ into $\mathbf { V }$ by extending $\pmb { \mathrm { g } }$ to a symplectic embedding ${ \bf g _ { 0 } }$ of the ball $\mathbf { B } ^ { 2 \mathbf { n } } ( \lambda + \epsilon )$ ,and then replacing the image ${ \bf g _ { 0 } } ( { \bf B ^ { 2 n } } ( \lambda + \delta ) )$ by the standard neighbourhood $\mathbf { N } _ { \delta } ( \mathbf { Z } )$ for some $\delta \in ( 0 , \epsilon )$ . Thus the manifold $\tilde { \ V } _ { \mathbf { g } } = \tilde { \ V } ( g _ { \mathbf { 0 } } , \ \delta )$ is defined to be:

$$
\begin{array} { r } { \tilde { \mathrm { V } } ( \mathrm { g } _ { 0 } , \delta ) = \left( \mathrm { V } - \mathrm { I n t } { \mathrm { g } } _ { 0 } ( \mathrm { B } ( \lambda + \delta ) ) \right) \cup \mathrm { N } _ { \delta } ( \mathrm { Z } ) , } \end{array}
$$

where $0 < \delta < \epsilon$ and $\mathbf { N } _ { \delta } ( \mathbf { Z } )$ is the neighbourhood of the zero section Z of $\gamma$ whose boundary is taken by $\Phi _ { \epsilon }$ to $\mathbf { S ^ { 2 n - 1 } } ( \lambda + \delta )$ , attached via $\mathbf { g _ { 0 } o } \Phi _ { \epsilon }$ . The form $\omega _ { \pmb { \xi } }$ equals $\omega$ on $\mathrm { V - I n t } \ \mathrm { g } _ { 0 } \big ( B ( \lambda + \delta ) \big )$ and the standard form $\pmb { \rho } _ { \pmb { \lambda } }$ on $\mathbf { N } _ { \delta } ( \mathbf { Z } )$ . It is easy to check that this is independent of the choice of $\delta$ ，We will denote the exceptional divisor in $\tilde { \mathsf { V } } ( \mathbf { g _ { 0 } } , \delta )$ by $\Sigma$

Lemma 2.4 (i) The manifold $\tilde { \nabla } _ { \mathbf { g } } = \tilde { \mathbf { V } } ( \mathbf { g } _ { \mathbf { 0 } } , \delta )$ is independent of the choice of extension ${ \pmb \mathrm { g o } }$ . More precisely, if go and ${ \pmb { \mathrm { g } } } _ { \pmb { 1 } }$ are two extensions of $\pmb { \mathrm { g } }$ to $\mathbf { B } ( \lambda + \epsilon )$ there is,for sufficiently small ${ \delta > 0 }$ ， a symplectomorphism $( \tilde { \bf V } ( { \bf g } _ { 0 } , \delta ) , \dot { \tilde { \boldsymbol { \omega } } } _ { \bf g } ) $ $( \tilde { \mathbb { V } } ( \mathbf { g } _ { 1 } , \delta ) , \tilde { \omega } _ { \mathbf { g } } )$ which is unique up to isotopy and which is the identity on $\pmb { \Sigma }$ (ii) $\tilde { \mathrm { v } } _ { \mathrm { g } }$ may be identifed with the blow-up $\tilde { \mathbf { V } } _ { \mathbf { p } ( \pmb { \mu } ) }$ of $\mathbf { V }$ at $\mathbf { p } ( \mathbf { g } ) = \mathrm { d } \mathbf { g } ( \mathbf { 0 } )$ by ${ \pmb a } _ { }$ diffeomorphism which is unique up to isotopy and which is the identity on $\pmb { \Sigma }$

Proof (i) Without loss of generality,we may suppose that $\mathsf { V } = \mathbb { R } ^ { 2 \mathrm { n } }$ and that $\pmb { \mathrm { g } }$ and ${ \tt g o }$ are the obvious inclusions. Clearly,it suffces to construct a compactly supported symplectomorphism $\phi$ of Int $\mathbb { B } ( \lambda + \epsilon )$ which restricts to ${ \bf g _ { 1 } }$ on $\mathbb { B } ( \lambda + \delta ^ { \prime } )$ for some $\delta ^ { \prime } \in ( 0 , \epsilon )$ ,and which is unique up to isotopy. To this end,choose a smooth cut off function $\alpha : \mathbb { R } \to [ 0 , 1 ]$ which equals 1 near O and O near 1,let $\alpha _ { \delta } ( { \bf x } ) = \alpha ( ( | | { \bf x } | | - \lambda ) / \delta )$ ,and define $\mathbf { h } ( \mathbf { t } , \delta ) : \mathbf { B } ( \lambda + \epsilon )  \mathbb { V }$ by:

$$
\mathrm { h } ( \mathbf { t } , \delta ) ( \mathbf { x } ) = \mathbf { x } + \mathrm { t } \alpha _ { \delta } ( \mathbf { x } ) ( \mathbf { g } _ { 1 } ( \mathbf { x } ) - \mathbf { x } ) \quad \mathrm { f o r } \quad 0 \leq \mathrm { t } \leq 1 .
$$

Note that $\mathbf { h } ( \mathbf { t } , \delta )$ - id has support in Int $\mathbb { B } ( \lambda + \delta )$ for all $\mathbf { t }$ ,and that $\mathbf { h } ( 1 , \delta ) = \mathbf { g } _ { 1 }$ near $\mathbf { B } ( \lambda )$

Let $c$ be a convex neighbourhood of $\omega _ { 0 }$ in the space of all symplectic forms on $\mathbb { B } ( \lambda + \epsilon )$ which equal $\omega _ { 0 }$ near $\partial \mathbf { B } ( \lambda + \epsilon )$ ,and let $u$ be a convex neighbourhood of the identity in the group of compactly supported diffeomorphisms of $\mathbb { B } ( \lambda + \epsilon )$ such that $\mathbf { h } ^ { * } ( \omega _ { 0 } ) \in \mathcal { C }$ for all $\mathbf { h } \in \mathcal { U }$ . Then,by the convexity of $c$ ,the path $\mathrm { \ t } \omega _ { 0 } + ( 1 - \mathrm { \ t } ) \mathrm { h } * \omega _ { 0 }$ ， $\mathbf { 0 } \leq \mathbf { t } \leq 1$ ,lies in $c$ ,and Moser's argument implies that there is aretraction $\mathbf { R }$ from $u$ into the group of compactly supported symplectic diffeomorphisms of $\mathbb { B } ( \lambda + \epsilon )$ . Now observe that,because $\mathfrak { g } _ { 1 } ( \mathbf { x } ) - \mathbf { x } = \mathbf { 0 }$ on $\mathbf { B } ( \boldsymbol { \lambda } )$ ,the maps $\mathbf { h } ( \mathbf { t } , \delta ) , \delta  \mathbf { 0 }$ ,defined above converge to the identity in the $\mathbf { \vec { C } ^ { 1 } }$ -norm on $\mathbb { B } ( \lambda + \epsilon )$ . Hence there is $\delta _ { 0 } > 0$ such that $\mathrm { h } ( \mathfrak { t } , \delta ) \in \mathcal { U }$ when

$0 \leq \mathfrak { t } \leq 1$ and $\delta \leq \delta _ { \mathfrak { g } }$ . Put $\phi = \mathrm { R } ( \mathrm { h } ( 1 , \ \delta _ { 0 } ) )$ . Because $\mathrm { R } ( \mathrm { h } ) { - } \mathrm { h }$ is supported in the closure of the set on which $\mathrm { h } ^ { * } ( \omega _ { 0 } ) \neq \omega _ { 0 }$ ,thismap $\phi$ restricts to ${ \pmb { \mathrm { g } } } _ { 1 }$ on $\mathbb { B } ( \lambda + \delta ^ { \prime } )$ for sufficiently small $\delta ^ { \prime }$ . It remains to check that the isotopy class of $\phi$ is independent of the choice of $\pmb { \alpha }$ and $\delta _ { \mathbf { 0 } }$ .But this follows by the convexity of $u$

(ii) Let $\operatorname { E m b } ( \mathbf { B } ( \lambda ) , \mathbf { V } )$ denote the space of (not necessarily symplectic) embeddings of $\mathbf { B } ( \lambda )$ into $\mathbf { V }$ ，and let $\mathbf { E }$ be the total space of the principal $\mathrm { G L } ( 2 \mathbf { n } , \mathbb { R } )$ bundle over $\mathbf { V }$ .By using the exponential map associated to some metric on $\mathbf { V }$ ，one can define an inclusion $\mathbf { \sigma } _ { 1 : } \mathbf { E }  \mathbf { \sigma } \mathbf { E m b } ( \mathbf { B } ( \lambda ) , \mathbf { \sigma } \mathbf { V } )$ which is homotopy inverse to the map ${ \mathfrak { g } } \mapsto \mathrm { d } { \mathfrak { g } } ( { \mathfrak { 0 } } )$ . Thus $\operatorname { E m b } _ { \omega } ( \mathbf { B } ( \lambda ) , \mathbf { V } )$ deformation retracts inside $\operatorname { E m b } ( \mathbf { B } ( \lambda ) , \mathbf { V } )$ to $\mathbf { \tau } _ { 1 } ( \mathbf { P } )$ . The desired conclusion now follows easily.

It follows that if we restrict attention to the space $\operatorname { E m b } _ { \omega }$ $( \mathbf { B } ( \boldsymbol { \lambda } ) , \mathbf { V } , \mathbf { p } )$ of symplectic embeddings such that $\deg ( 0 ) = \mathfrak { p }$ ,we may identify all the manifolds $\tilde { \mathrm { V } } _ { \mathrm { g } }$ and call them $\tilde { \mathbf { V } } _ { \mathbf { p } }$

Proposition 2.5 The isotopy class of the form $\tilde { \omega } _ { \tt g }$ on $\tilde { \mathbf { V } } _ { \mathbf { p } }$ depends only onthe isotopy class of $\pmb { \mathrm { g } }$ in $ { \mathbf { E m b } } _ { \omega } (  { \mathbf { B } } ( \lambda ) ,  { \mathbf { V } } ,  { \mathbf { p } } )$ ：

Proof Let $\mathbf { f _ { t } } , \ \mathbf { 0 } \ \leq \ \mathbf { t } \ \leq \ 1$ ，bea smooth family of symplectic embeddings $\mathbf { B } ( \lambda )  \mathbf { V }$ such that $\mathrm { d f } _ { \mathbf { t } } ( \mathbf { 0 } ) = \mathbf { p }$ for all $\mathbf { t }$ . Extend these to $\mathbb { B } ( \lambda + \epsilon )$ for some $\epsilon > 0$ and let $\tilde { \mathsf { V } } ( \mathrm { t } ) = \tilde { \mathsf { V } } ( \tilde { f } _ { \mathrm { t } } , \tilde { \epsilon } / 2 )$ . By the symplectic isotopy extension theorem, there is an ambient symplectic isotopy $\mathbf { F _ { t } }$ of $\mathbf { V }$ such that $\mathbf { F t } \circ \mathbf { f _ { 0 } } = \mathbf { f _ { t } }$ on $\mathbb { B } ( \lambda + \epsilon )$ . Clearly,this induces a family of symplectomorphisms $\Psi _ { \mathbf { t } } : \tilde { \mathbf { V } } ( \mathbf { 0 } ) \to$ $\tilde { \bf V } ( { \bf t } )$ .Further, it is easy to see that one can choose the diffeomorphisms $\phi _ { \mathbf { t } } : \tilde { \mathbb { V } } _ { \mathbf { p } }  \tilde { \mathbb { V } } ( \mathbf { t } )$ of Lemma 2.4(ii) to be smooth in the sense that the composites $\Phi _ { \mathbf { t } } = \phi _ { \mathbf { t } } ^ { - 1 } \circ \Psi _ { \mathbf { t } } \circ \phi _ { \mathbf { 0 } }$ form a smooth family of diffeomorphisms of $( \tilde { \mathsf { V } } _ { \mathsf { p } } , \bar { \mathsf Z } )$ . But if $\mathbf { f _ { 0 } } = \mathbf { g }$ and $\mathbf { f } _ { 1 } = \mathbf { h }$ ,the construction implies that $\tilde { \omega } _ { \mathbf { g } } = \Phi _ { 1 } { ^ * } ( \tilde { \omega } _ { \mathbf { h } } )$ . Hence $\tilde { \omega } _ { \pmb { \mathrm { g } } }$ and $\tilde { \omega } _ { \bf h }$ are isotopic.

Note that in the above construction, the path $\bf { f _ { t } }$ in $\operatorname { \mathbf { E m b } } _ { \omega } ( \mathbf { B } ( \lambda ) , \mathbf { V } , \mathbf { p } )$ gives rise to a family of symplectic forms on $\tilde { \nabla } _ { \mathbf { p } }$ whose restrictions to $\Sigma$ are constant. One could ask whether the converse of Proposition 2.5 holds: that is,if ${ \tilde { \omega } } _ { \mathbf { g } }$ and $\tilde { \omega } _ { \mathbf { h } }$ are isotopic by an arbitrary isotopy (which need not be constant on $\pmb { \Sigma }$ ）， must the embeddings $\pmb { \mathrm { g } }$ and h be isotopic? Even if one restricts to dimension 4, it is not clear that this holds in general. However,one can prove the following slightly weaker result. We will say that two embeddings g, $\begin{array} { r } { \mathbf { h } \in \mathbb { E } \mathbf { m } \mathbf { b } _ { \omega } ( \mathbf { B } ( \lambda ) . } \end{array}$ ， V) are equivalent (and write ${ \tt g } \approx { \bf h }$ )iff there is a symplectomorphism $\phi$ of (V, $\omega$ ）such that $\phi \circ \mathbf { g } = \mathbf { h }$ ·

Proposition 2.6 If dim $\mathrm { V } { = } 4$ ， $\mathbf { g } \approx \mathbf { h }$ if the blow-ups $( \tilde { \nabla } , \tilde { \omega } _ { \mathbf { g } } )$ and $( \tilde { \vee } , \tilde { \omega } _ { \mathbf { h } } )$ are symplectomorphic by a symplectomorphism which preserves the homology class $[ \Sigma ]$

Proof Let $\phi : ( \tilde { \mathbb { V } } , \tilde { \omega } _ { \mathtt { g } } )  ( \tilde { \mathbb { V } } , \tilde { \omega } _ { \mathtt { h } } )$ be a symplectomorphism which preserves the homology class $[ \Sigma ]$ . Then,as in [M2] (3.3),because for generic $\mathbf { J }$ there is a unique J-holomorphic representative of the class $[ \Sigma ]$ ,there is a $\tilde { \omega } _ { \mathbf { h } }$ -symplectic isotopy of $\tilde { \mathsf { V } }$ which takes $\phi ( \Sigma )$ to $\Sigma$ . Hence we may suppose that $\phi ( \Sigma ) = \Sigma$ ， and it easily follows that ${ \tt g } \approx { \bf h }$ . The converse is obvious.

Proposition 2.7 If $\mathrm { \Delta V = I n t }$ B(1), $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ or $\mathbf { S ^ { 2 } } \times \mathbf { S ^ { 2 } }$ ,the blow-ups $( \tilde { \nabla } , \tilde { \omega } _ { \mathbf { g } } )$ and $( \tilde { \mathbb { V } } , \tilde { \omega } _ { \mathbf { h } } )$ are symplectomorphic by a map which induces the identity on homology iff the embeddings g and h are isotopic.

Proof By Proposition 2.6,it suffces to show that for each of the three listed manifolds the group of compactly supported symplectomorphisms which are the identity on homology is connected.Gromov showed in [G1] that this group is contractible when $\mathbf { V } = \mathbf { I n t } ~ \mathbf { B } ( 1 )$ ,and that it deformation retracts onto SU(3) when $\mathbf { V } = \mathbf { \mathbb { C } P ^ { 2 } }$ . When $\mathbf { V } = \mathbf { S ^ { 2 } } \times \mathbf { S ^ { 2 } }$ ,one must distinguish two cases depending on the cohomology class of $\omega$ . Let $\pmb { \sigma _ { 1 } }$ $\left( \mathrm { r e s p } \ \sigma _ { 2 } \right)$ denote the pull-back to $\mathbf { S ^ { 2 } } \times \mathbf { S ^ { 2 } }$ of the standard area form on ${ \mathbb S } ^ { 2 }$ with total area $\pmb { \pi }$ via projection onto the first (resp.second) factor.If $\omega = \lambda ( \sigma _ { 1 } \oplus \sigma _ { 2 } )$ ,Gromov showed that the group of symplectomorphisms under consideration deformation retracts onto $\mathbf { S O ( 3 ) } \times \mathbf { S O ( 3 ) }$ : see [G1] 0.3.C. (Note that in this case the whole group of symplectomorphisms is disconnected, since it is possible to interchange the two factors.） If $\omega = \lambda \sigma _ { 1 } \oplus \mu \sigma _ { 2 }$ where $\lambda \neq \mu$ ,this is no longer true. However, his proof shows that the group is connected,which is all we need here.

Appropriate versions of the above propositions apply to embeddings of a finite union of disjoint balls. In particular,there is a unique way of blowing up ${ \tt C P } ^ { 2 }$ at $\mathbf { k }$ points with weights $\lambda _ { 1 } , \ldots , \lambda _ { k }$ iff the space $\mathrm { E m b } _ { \omega } ( \mathrm { I I B } ( \lambda _ { \mathrm { i } } ) , \mathbb { C P } ^ { 2 } )$ is path-connected. (Here $\mathrm { { I I B } } ( \lambda _ { \mathrm { i } } )$ denotes the disjoint union of the balls $\mathbf { B } ( \lambda _ { 1 } ) , \ldots , \mathbf { B } ( \lambda _ { \mathbf { k } } ) .$ ） We now show that $\mathrm { E m b } _ { \omega } ( \mathrm { I I B } ( \lambda _ { \mathrm { i } } ) , \mathbb { C P } ^ { 2 } )$ is path-connected if $\operatorname { E m b } _ { \omega } ( \operatorname { I I B } ( \lambda _ { \mathrm { i } } )$ ,Int B(1)) is also,thereby reproving Proposition 1.4 of [M1]. Let ibe the standard symplectic embedding of Int B(1) onto $\mathbf { \mathbb { C } P ^ { 2 } - \mathbb { C } P ^ { 1 } }$ given by

$$
\iota ( \mathbf { z } , \mathbf { w } ) = [ \sqrt { 1 - | \mathbf { z } | ^ { 2 } - | \mathbf { w } | ^ { 2 } } : \mathbf { z } : \mathbf { w } ] .
$$

Note that $\iota ^ { * } \tau _ { 0 } = \omega _ { 0 }$ because $\pmb { \iota }$ factors though the obvious projection $\pi : { \bf S } ^ { 5 } $ $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ ,and $\pi ^ { * } \tau _ { 0 } = \omega _ { 0 } \vert \mathrm { \bf S } ^ { 5 } .$ ） Further,define $\kappa$ : Int $( \mathbf { B } ^ { 2 } ( \mathbf { r _ { 1 } } ) \times \mathbf { B } ^ { 2 } ( \mathbf { r _ { 2 } } ) )  \mathbf { S } ^ { 2 } \times \mathbf { S } ^ { 2 }$ to be a product of embeddings $\mathrm { B } ^ { 2 } ( \mathrm { r _ { i } } )  \mathrm { S } ^ { 2 } -$ pt.,where we take the symplectic form on $\mathbf { S ^ { 2 } } \times \mathbf { S ^ { 2 } }$ to be a product of embeddings $\mathbf { B } ^ { 2 } ( \mathbf { r _ { i } } ) \to \mathbf { S ^ { 2 } }$ -pt., where we take the symplectic form on $\mathbf { S ^ { 2 } } \times \mathbf { S ^ { 2 } }$ to be $\mathbf { r _ { 1 } } ^ { 2 } \sigma _ { 1 } \oplus r _ { 2 } ^ { 2 } \sigma _ { 2 }$ so that $\pmb { \kappa }$ may be chosen to be symplectic.

Proposition 2.8 (i) $\pmb { \iota }$ induces an isomorphism between $\pi _ { 0 } \big ( \mathrm { E m b } _ { \omega } ( \mathrm { I I B } ( \lambda _ { \mathrm { i } } )$ ， Int B(1)) and $\pi _ { 0 } ( ( \operatorname { E m b } _ { \omega } ( \operatorname { I I B } ( \lambda _ { \mathrm { i } } ) , \mathbb { C P } ^ { 2 } ) ) ) ,$ .

(i) $\pmb { \kappa }$ induces an isomorphism between $\pi _ { 0 } \big ( \mathrm { E m b } _ { \omega } ( \mathrm { I I B } ( \lambda _ { \mathrm { i } } ) , \mathrm { I n t } ( \mathrm { B } ^ { 2 } ( \mathrm { r } _ { 1 } ) \times \mathrm { B } ^ { 2 } ( \mathrm { r } _ { 2 } ) ) \big )$ and $\pi _ { \mathbf { 0 } } ( \operatorname { E m b } _ { \omega } ( \operatorname { I I B } ( \lambda _ { \mathrm { i } } ) , \mathbb { S } ^ { 2 } \times \mathbb { S } ^ { 2 } )$ ）.

Proof (i) Let $\mathbf { g _ { t } } , \mathbf { 0 } \leq \mathbf { t } \leq 1$ ,be a path in $\mathrm { E m b } _ { \omega } ( \mathrm { I I B } ( \lambda _ { \mathrm { i } } ) , \mathbb { C P } ^ { 2 } )$ with ${ \pmb \mathrm { g o } }$ and $\pmb { \mathrm { g } } _ { 1 }$ in Im i,and let S denote the 2-sphere in ${ \tt C P } ^ { 2 }$ whose complement is Im l. Suppose that we can find a smooth path $\mathbf { S _ { t } }$ of symplectically embedded 2- spheres with $\mathbf { S _ { 0 } } = \mathbf { S _ { 1 } } = \mathbf { S _ { \alpha } }$ such that $\mathbf { S _ { t } }$ is disjoint from $\operatorname { I m } \ \pmb { \mathrm { g } } _ { \pmb { \mathrm { t } } }$ for each $\mathbf { t }$ . The isotopy extension theorem then implies that there is a path $\phi _ { \mathbf { t } }$ of symplectic diffeomorphisms of $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ such that $\phi _ { 0 } = \mathrm { i d }$ .and $\phi _ { \mathbf { t } } ( \mathbf { S } ) = \mathbf { S _ { t } }$ . Further, because the group of symplectomorphisms $\phi$ of $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ such that $\phi ( \mathbf { S } ) = \mathbf { S }$ is connected, we may also suppose that $\phi _ { 1 } = \mathrm { i d }$ Thus $\phi _ { \mathbf { t } } ^ { - 1 } \circ \mathbf { g _ { t } }$ is a path in Im 1joining go to $\pmb { \mathrm { g } } _ { 1 }$

To find the $\mathbf { S _ { t } }$ ,let ${ \bf X _ { k } }$ denote $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ blown up at $\mathbf { k }$ points,and let S be the lift of S.(This is disjoint from the exceptional spheres.) ${ \bf { X _ { k } } }$ has a path $\pmb { \sigma _ { \mathbf { t } } }$ of symplectic forms given by the embeddings $\pmb { \mathrm { g } } _ { \pmb { \mathrm { t } } }$ . Note that both $\pmb { \sigma _ { 0 } }$ and $\pmb { \sigma _ { 1 } }$ are non-degenerate on S. Now choose a path $\mathbf { J _ { t } }$ of almost complex structures on ${ \bf { X } _ { k } }$ so that $\mathbf { J _ { t } }$ is $\pmb { \sigma _ { t } }$ -compatible for each $\mathbf { t }$ , the exceptional spheres are $\mathbf { J _ { t } } \mathbf { . }$ holomorphic for each $\mathbf { t }$ and S is ${ \bf { { J } } } _ { \bf { { 0 } } }$ -holomorphic. Then,as in [M1],there is a unique $\mathbf { J _ { t } }$ -holomorphic sphere through every pair of points outside the exceptional spheres,and so one can pick out a smooth family of embedded spheres $\tilde { \mathbf { S } } _ { \mathbf { t } }$ starting at S such that $\tilde { \mathbf { S } } _ { \mathbf { t } }$ is $\mathbf { J _ { t } }$ -holomorphic for each $\mathbf { t }$ . These spheres cannot meet the exceptional spheres in ${ \bf { X _ { k } } }$ since the relevant homology classes have zero intersection. Further,the space of ${ \pmb \sigma } _ { 1 }$ -symplectically embedded 2- spheres in class [S] is connected,because each such sphere is J-holomorphic for some $\pmb { \sigma _ { 1 } }$ -tame J. Thus,we may suppose that $\tilde { \mathsf { S } } _ { 1 } = \tilde { \mathsf { S } }$ , and take the $\mathbf { S _ { t } }$ to be the images of the $\tilde { \mathbf { S } } _ { \mathbf { t } }$ in the blow down $\mathbf { \pmb { C P ^ { 2 } } }$ of ${ \bf { X _ { k } } }$

(ii) The proof of (ii) is similar and will be left to the reader.Here,because the complement of Im $\pmb { \kappa }$ is $\mathbf { S ^ { 2 } } \times \mathbf { \ p t } \cup \mathbf { p t } \times \mathbf { S ^ { 2 } }$ ，one had to find two families $\tilde { \mathbf { S } } _ { \mathbf { t } }$ and $\tilde { \mathbf { S } } _ { \mathbf { t } } ^ { \prime }$ of curves, one in class $\mathbf { A } = [ \mathbf { S } ^ { 2 } \times \mathbf { p } \mathbf { t } ]$ and the other in class $\mathbf { B } = \left[ \mathbf { p } \mathbf { t } \times \mathbf { S } ^ { 2 } \right]$ ·

# \$3 Uniqueness of blow ups of CP²

Our argument is based on the following easy lemma.

Lemma 3.1 Suppose that $\mathbf { U }$ is a star-shaped open subset of $\mathbb { R } ^ { 4 }$ and let $\pmb { \sigma }$ be any symplectic form on $\mathbb { R } ^ { 4 }$ which equals the standard form outside some compact subset of U. Then there is a diffeomorphism $\phi$ of $\mathbb { R } ^ { 4 }$ with support in U such that $\phi * \sigma = \omega _ { 0 }$

Proof We will suppose that $\mathbf { U }$ is star-shaped about the origin. Define $\sigma _ { \mathbf { t } } =$ $\mathbf { t ^ { 2 } } . { \mu _ { \mathrm { t } } } ^ { * } ( \sigma )$ for $\mathbf { 0 < t \leq 1 }$ ， where $\mu _ { \mathrm { t } } : \mathbb { R } ^ { 4 } \to \mathbb { R } ^ { 4 }$ is the expansion $\mathbf { x } \mapsto \mathbf { x } / \mathbf { t }$ . Then $\sigma _ { 1 } = \sigma$ and, for all $\mathbf { t }$ ， $\sigma _ { \mathbf { t } } = \omega _ { \mathbf { 0 } }$ outside some compact subset of $\mathbf { t } { \cdot } \mathbf { U }$ .We may choose $\mathbf { t } > \mathbf { 0 }$ and $\lambda > 0$ so that $\mathbf { t } { \cdot } \mathbf { U } \subset$ Int $\mathbf { B } ^ { 2 } ( \lambda ) \times \mathbf { B } ^ { 2 } ( \lambda ) \subset \mathbb { U }$ . Then $\pmb { \sigma _ { \mathbf { t } } }$ is standard near the boundary of the polydisc $\mathrm { \bf B } ^ { 2 } ( \lambda ) \times \mathrm { \bf B } ^ { 2 } ( \lambda )$ ,and so, by [G1] $2 . 4 . \mathrm { A } _ { 1 }$ ,there is a diffeomorphism $\phi$ with support in $\mathbf { B } ^ { 2 } ( \lambda ) \times \mathbf { B } ^ { 2 } ( \lambda )$ such that $\phi * \sigma = \omega _ { 0 }$ ·

Next， consider $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ with its standard Kähler metric ${ \pmb \mu _ { 0 } }$ ， normalised as before so that the area of a complex line is $\pmb { \pi }$ . Thus each complex projective line is isometric to the sphere $\mathbf { S } ^ { 2 } ( 1 / 2 )$ of radius $1 / 2$ in ${ \mathbb R } ^ { 3 }$ . Fix a complex projective line S,identify $\pmb { \mathbb { C P } ^ { 2 } } - \pmb { S }$ with Int $\mathbf { B } ( 1 ) \subseteq \mathbf { C } ^ { 2 }$ via the map $\bullet$ of (2.7.1) and let $\mathbf { B } = \mathbf { B _ { g } } ( \mathbf { x } , \mathbf { r } )$ be a metric ball in $\pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ with center on S.

Lemma 3.2 The set ${ \textrm { U } } \subset$ Int B(1) which is mapped by ito CP²-(SUB) is star-shaped.

Proof This holds because the rays through $\{ \boldsymbol { 0 } \}$ in B(1) are mapped by 1 to geodesics from $\mathbf { x } _ { 0 } = \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { 1 } } } } } ( \mathbf { \mathbf { \mathbf { 0 } } } )$ to S,and metric balls are geodesically convex.

Lemma 3.3 The set $\mathrm { \bf B ( \lambda _ { 1 } ) } \mathrm { \bf U B ( \lambda _ { 2 } ) }$ embeds symplectically onto a pair of metric balls in $\bf { \pmb { C P ^ { 2 } } }$ $\lambda _ { 1 } { } ^ { 2 } + \lambda _ { 2 } { } ^ { 2 } < 1$

Proof Using the fact that $\pmb { \iota }$ $. \ ( \mathbf { B } ( \lambda ) )$ is a metric ball,one easily checks that $\mathbf { B } ( \lambda )$ is symplectomorphic to $\mathbf { B _ { \mathbf { g } } ( \mathbf { x } , \mathbf { r } ) }$ iff $\lambda = \sin ( \mathbf { r } )$ .Therefore the condition ${ \lambda _ { 1 } } ^ { 2 } + { \lambda _ { 2 } } ^ { 2 } < 1$ is equivalent to $\mathbf { r } _ { 1 } + \mathbf { r } _ { 2 } < \pi / 2$ . But because the diameter of the projective lines in $( { \tt C P ^ { 2 } } , { \tt g } )$ is $\pi / 2 .$ ,this is exactly the condition which allows one to place the metric balls so that they have disjoint intersections with the projective line S through their centers.But then they are disjoint by Lemma 3.2.

We will call a symplectic embedding of $\mathrm { { B } } ( \lambda _ { 1 } ) \operatorname { I I B } ( \lambda _ { 2 } )$ onto a pair of metric balls in $( \mathbf { C P ^ { 2 } } , \mu _ { 0 } )$ a “standard embedding”. Note that these are all isotopic, and that they give rise to Kähler forms on ${ \bf { X } } _ { 2 }$ . Further,by [G1] 0.2.B (see also [M1]), $\mathbf { B } ( \lambda _ { 1 } ) \operatorname { I I } \mathbf { B } ( \lambda _ { 2 } )$ embeds symplectically into $\textstyle \mathbf { C P ^ { 2 } }$ iff ${ \lambda _ { 1 } } ^ { 2 } + { \lambda _ { 2 } } ^ { 2 } < 1$ . Hence there is a standard embedding whenever there is a symplectic embedding. We now show:

Theorem 3.4 Any symplectic embedding of $\mathrm { \bf B } ( \lambda _ { 1 } ) \mathrm { \bf U B } ( \lambda _ { 2 } )$ into ${ \tt C P } ^ { 2 }$ is isotopic to a standard embedding. Thus, $\operatorname { E m b } _ { \omega } ( \mathbf { B } ( \lambda _ { 1 } ) \operatorname { I I } \mathbf { B } ( \lambda _ { 2 } ) , \mathbf { C P } ^ { 2 } )$ is pathconnected (provided it is non-empty).

Proof Let $\pmb { \sigma }$ be the symplectic form on ${ \bf { X } } _ { 2 }$ constructed from the symplectic embedding $\mathbf { g } \colon \mathbf { B } ( \lambda _ { 1 } ) \operatorname { I I B } ( \lambda _ { 2 } ) \to \mathbf { C P } ^ { 2 }$ . By Proposition 2.7 it suffices to show that it is symplectomorphic to a standard form $\pmb { \tau }$ ,i.e. one constructed from a standard embedding.Let A denote the homology class of the projective lines in $\bf { \pmb { C P ^ { 2 } } }$ and also of their lifts to ${ \bf { X } } _ { 2 }$ ,and let $\mathbf { E _ { 1 } } , \mathbf { E _ { 2 } }$ be the homology classes of the exceptional curves $\Sigma _ { 1 } , \Sigma _ { 2 }$ . Choose a $\pmb { \sigma }$ -tame almost complex structure ${ \bf J } _ { 1 }$ on ${ \bf X _ { 2 } }$ such that the two exceptional curves in ${ \bf { X } _ { 2 } }$ are ${ \bf J } _ { 1 }$ -holomorphic. Using the fact that for each $\pmb { \tau _ { 0 } }$ -tame ${ \bf J }$ on $\bf { \pmb { C P ^ { 2 } } }$ there is a unique $\mathbf { J }$ -holomorphic Acurve through each pair of points,and arguing as in [M1] Lemma 3.3,one can easily show that there is a unique ${ \bf J } _ { 1 }$ -holomorphic curve C in ${ \bf { X } } _ { 2 }$ in the class A-$\mathbf { E _ { 1 } } - \mathbf { E _ { 2 } }$ . (In fact, this curve is a component of the unique ${ \bf J _ { 1 } }$ -holomorphic Acusp-curve which meets $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ .） It follows from positivity of intersections (see [M2](2.5)) that C is embedded and meets each exceptional curve once transversally. Therefore,by the symplectic neighbourhood theorem，there is a symplectomorphism from a neighbourhood $\mathbf { N }$ of $\mathbf { Y } = \mathbf { C } \cup \Sigma _ { 1 } \cup \Sigma _ { 2 }$ to a neighbourhood of the corresponding curves in the standard model $( \mathrm { X } _ { 2 } , \tau )$ It follows that the deleted neighbourhood $\mathbf { N } - \mathbf { Y }$ is symplectomorphic to a neighbourhood of the boundary of the star-shaped set ${ \textrm { U } } \subset$ Int B(1),where $\iota \ ( \mathbf { U } ) = \mathbb { C } \mathbf { P } ^ { 2 } - ( \mathbf { S } \cup \mathbf { B } _ { 1 } \cup \mathbf { B } _ { 2 } )$ . The result now follows from Lemma 3.1.■

Theorem 1.1 follows by combining Theorem 3.4 with Propositions 2.6 and 2.7.

Note 3.5 The proof of Theorem 3.4 clearly applies to one ball, and so gives a new proof of the main result in [M1].

# (3.6) Embeddings of more than two balls.

Note that,given any two symplectic embeddings g $\mathbf { \sigma } _ { 1 } , \mathbf { g } _ { 2 } : \mathrm { { I I B } } ( \lambda _ { \mathbf { i } } )  \mathrm { { V } }$ ，one can always decrease the $\lambda _ { i }$ to a set of radii $\lambda _ { \mathbf { i } } ^ { \prime }$ such that the restrictions of $\pmb { \mathrm { g } } _ { 1 }$ and ${ \pmb { \mathrm { g } } } _ { 2 }$ to $\mathrm { U B } ( \lambda _ { \mathbf { i } } ^ { \prime } )$ are isotopic. (This holds because the group of symplectomorphisms of $( \mathbb { V } , \omega )$ acts $\mathbf { k }$ -transitively on $\mathbf { V }$ ,and so is true for any symplectic manifold V.) Of course, the size of the $\lambda _ { \mathrm { i } } ^ { \prime }$ depends on $\pmb { \mathrm { g } }$ in general: in fact, there are no cases besides those mentioned above when the $\lambda _ { \mathbf { i } } ^ { \prime }$ may be chosen independently of $\pmb { \mathrm { g } } _ { 1 }$ and ${ \pmb { \mathrm { g } } } _ { 2 }$

However, there is a little more to be said about $> 2$ balls in $\mathbf { \pmb { C P ^ { 2 } } }$ . First, observe that the proof of Theorem 3.4 applies to any symplectic embedding $\mathbf { g } : \coprod \mathbf { B } ( \lambda _ { \mathbf { i } } ) \ \to \ \pmb { \mathbb { C } } \mathbf { P } ^ { 2 }$ such that there is a J-holomorphic $\left( \mathbf { A } \mathrm { - } \sum \mathbf { i } \mathbf { E } _ { \mathbf { i } } \right)$ -curve in $( \mathbf { X } _ { k } , \tilde { \omega } _ { \mathbf { g } } )$ for some $\tilde { \omega } _ { \mathbf { g } }$ -tame J.Hence these embeddings are isotopic to standard embeddings,i.e. embeddings whose image is a union of metric balls. This condition can be satisfied only if $\tilde { \omega } _ { \mathrm { g } } ( \mathrm { A } - \Sigma _ { \mathrm { i } } \mathrm { E } _ { \mathrm { i } } ) > 0$ i.e. $\Sigma _ { \mathrm { i } } \ \lambda _ { \mathrm { i } } ^ { 2 } < 1$ , and so is more restrictive than the symplectic packing inequalities given in [G1] 0.2.B. (For example,if $\mathbf { k } \leq \mathbf { 5 }$ there is a symplectic embedding of $\mathrm { { I I B } } ( \lambda _ { \mathrm { i } } )$ into $\pmb { \mathbb { C } P ^ { 2 } }$ if $\lambda _ { 1 } { } ^ { 2 } + \ldots + \lambda _ { \mathbf { k } } { } ^ { 2 } < 2$ and $\lambda _ { \mathrm { i } } ^ { 2 } + \lambda _ { \mathrm { j } } ^ { 2 } < 1$ for all pairs $\mathrm { i } \neq \mathrm { j }$ ）However,it is not clear that the numerical condition $\Sigma _ { \mathrm { i } } \lambda _ { \mathrm { i } } ^ { 2 } < 1$ is sufficient to guarantee that there is a J-holomorphic $\left( \mathrm { A } \mathrm { - } \sum \mathrm { \mathbf { i } } \mathrm { E } _ { \mathbf { i } } \right)$ -curve since, when $\textbf { k } > 2$ ， these curves have negative index and so are never generic. Equivalently,one needs to find a symplectically embedded 2-sphere $\mathbf { C }$ in $\mathbf { \pmb { C P ^ { 2 } } }$ which meets each ball $\bf { g } ( \bf { B } ( \lambda _ { i } ) )$

in the image under $\pmb { \mathrm { g } }$ of a flat disc through the center of $\mathbf { B } ( \lambda _ { \mathbf { i } } )$ . By elementary arguments (see [G2] $\mathbf { 3 . 4 . 2 \ B ^ { \prime } } ,$ ） one can show that the space of symplectic embeddings of a 2-disc into any symplectic 4-manifold is connected.Hence one can arrange that the intersection of C with Im g contains these flat discs, but it is not clear that one can isotop away allthe other parts of $\mathbf { C } \cap \mathbf { I m } \ \mathbf { g }$

We end by proving a result stated in [M1].We pointed out there that all cohomolgous Kahler structures on ${ \bf { X _ { k } } }$ are symplectomorphic. We will call the corresponding component of $\mathrm { E m b } _ { \omega } ( \mathrm { I I B } ( \lambda _ { \mathrm { i } } ) , \mathbb { C P } ^ { 2 } )$ the “standard component”.

Proposition 3.7 If $\pmb { \mathscr { g } }$ is an embedding of $\mathrm { { I I B } } ( \lambda _ { \mathrm { i } } )$ into Int B(1) which is isometric with respect to the usual flat metric on ${ \mathfrak { C } } ^ { \mathbf { n } }$ ,then l o $\pmb { \mathrm { g } }$ belongs to the standard component.

Proof Let $\mathbf { J _ { 0 } }$ be the standard complex structure on ${ \mathfrak { C } } ^ { 2 }$ .We first claim that it suffices to show that there is an integrable $\pmb { \tau _ { 0 } }$ -tame almost complex structure Jon $\bf { \pmb { C P ^ { 2 } } }$ which extends the complex structure $( \iota \circ \mathbf { g } ) _ { * } \mathbf { J _ { 0 } }$ on $\operatorname { I m } \pmb { \iota } \circ \pmb { \mathrm { g } }$ To see this,observe that such a $\mathbf { J }$ induces a complex structure $\tilde { \mathbf { J } }$ on the blow-up ${ \bf X _ { k } }$ which is tamed by the form ${ \tilde { \omega } } _ { \mathbf { g } }$ The set $s$ of forms cohomologous to ${ \tilde { \omega } } _ { \mathbf { g } }$ and tamed by $\tilde { \mathbf { J } }$ contains forms which are compatible with $\tilde { \mathbf { J } }$ and hence $\tilde { \bf J }$ Kahler. (Recall that $\omega$ tames ${ \bf J }$ iff $\omega ( { \bf v } , { \bf J } { \bf v } ) > 0$ for $\mathbf { v } \neq \mathbf { 0 }$ ,and is compatible with Jif, in addition, $\omega ( { \mathbf { v } } , { \mathbf { w } } ) = \omega ( \mathbf { J } { \mathbf { v } } , \mathbf { J } { \mathbf { w } } ) .$ ）Since $s$ is convex, $\tilde { \omega } _ { \mathbf { g } }$ is symplectomorphic to a Kähler form,as required.

By hypothesis,the mapping given by $\pmb { \mathrm { g } }$ of each ball $\mathbb { B } ( \lambda _ { \mathtt { i } } )$ may be described as a translation followed by a unitary rotation. In particular $\mathbf { g _ { * } ( J _ { 0 } ) } = \mathbf { J _ { 0 } }$ Therefore, it suffices to show that,if $0 < \epsilon _ { 2 } < \epsilon _ { 1 } < 1$ ，there is a $\omega _ { 0 }$ -tame complex structure J on Int B(1) which equals the usual complex structure ${ \bf { { J } } } _ { \bf { { 0 } } }$ in $\mathbf { B } ( 1 { - } \epsilon _ { 1 } )$ and equals ${ \bf J } _ { 1 }$ outside $\mathbf { B } ( 1 - \epsilon _ { 2 } )$ where ${ \bf J } _ { 1 }$ denotes the pull-back by 1of the usual complex structure $\mathbf { \pmb { C P ^ { 2 } } }$ . But, it is easy to see that $\mathbf { J } _ { 1 } = \Psi ^ { * } \mathbf { J _ { 0 } }$ where $\Psi : \operatorname { I n t } \ \mathbf { B } ( 1 )  \mathbb { C } ^ { 2 }$ is a map of the form $\mathbf { x } \mapsto \mathbf { r } ( | | \mathbf { x } | | ) \mathbf { x }$ (In fact, $\Psi$ is essentially stereographic projection.） Thus,for all $\lambda < 1$ ， $\mathbf { J _ { 0 } }$ and ${ \bf J _ { 1 } }$ agree on the complex part of the tangent bundle of the sphere $\partial \mathbf { B } ( \boldsymbol { \lambda } )$ , and differ by a scalar factor (depending only on $\lambda$ ）on the vector feld ${ \pmb \xi }$ which generates the Hopf flow $( \mathbf { z } , \mathbf { w } ) \mapsto ( \mathrm { e } ^ { \mathrm { i } \theta } \mathbf { z } , \mathrm { e } ^ { \mathrm { i } \theta } \mathbf { w } )$ . Since both are tamed by $\omega _ { 0 }$ ,it is not hard to find an integrable $\omega _ { 0 }$ -tame ${ \bf J }$ on the annulus $\mathbf { B } ( 1 - \epsilon _ { 2 } ) - \mathbf { B } ( 1 - \epsilon _ { 1 } )$ which has the form $\phi ^ { \ast } \mathbf { J _ { 0 } }$ for suitable $\phi$ and which interpolates between them.

We claimed in Note 2.5 of $\mathbf { [ M 1 ] }$ that the form $\tilde { \omega } _ { \pmb { \mathrm { g } } }$ on ${ \bf { X _ { k } } }$ is Kahler iff the complex structure $\mathbf { g } _ { * } ( \mathbf { J _ { 0 } } )$ on Im $\pmb { \mathrm { g } }$ extends to an $\omega _ { 0 }$ -tame complex structure J on B(1) which equals $\mathbf { J _ { 0 } }$ near $\partial \mathbf { B } ( 1 )$ . The above argument shows that one can ask equivalently that the extension ${ \bf J }$ equal ${ \bf J _ { 1 } }$ near $ { \partial }  { \mathbf { B } } ( 1 )$ , and it also proves the ${ } ^ { \mathfrak { s e } } { } _ { 1 \mathrm { { f } } } { } ^ { \mathfrak { n } }$ part of the claim. To prove the “only if” part one can argue as follows. By construction, the form $\tilde { \omega } _ { \mathbf { g } }$ is non-degenerate on the exceptional spheres $\Sigma _ { 1 } , \ldots , \Sigma _ { \mathbf { k } }$ in ${ \bf { X _ { k } } }$ ,and it is Kahler iff there is a compatible complex structure

Jon ${ \bf { X _ { k } } }$ . Now, the exceptional spheres $\pmb { \Sigma _ { \mathbf { i } } }$ need not be $\tilde { \mathbf { J } }$ -holomorphic,but,by the argument in Proposition 2.6 above, there is always a ${ \tilde { \omega } } _ { \mathbf { g } }$ -symplectic isotopy $\Psi _ { \mathbf { t } }$ of ${ \bf { X _ { k } } }$ such that the $\pmb { \Sigma _ { \mathbf { i } } }$ are $( \Psi _ { 1 } ) _ { * } \tilde { \mathbf { J } }$ -holomorphic.Therefore,by replacing j by $( \Psi _ { 1 } ) _ { * } \tilde { \mathbf { J } }$ ,we may suppose that the $\pmb { \Sigma _ { \mathbf { i } } }$ are $\tilde { \mathbf { J } }$ -holomorphic.Further,since the complex structure in the neighbourhood of a rational holomorphic curve in a complex surface is uniquely determined by the topological type of the normal bundle, $\tilde { \mathbf { J } }$ is standard near the $\pmb { \Sigma _ { \mathbf { i } } }$ and near any complex projective line and so descends to give the required complex structure on Int B(1).

# References

G1. Gromov, M.: Pseudo-holomorphic curves in almost complex manifolds, Invent.Math 82 (1985),307-347.   
G2. Gromov,M.:Partial Differential Relations, Spring-Verlag 1986.   
M1. McDuff,D.: Blow ups and symplectic embeddings in dimension 4, Topology,1991.   
M2. McDuff, D.: The Structure of Rational and Ruled Symplectic 4-manifolds,Journ. Amer. Math. Soc. 3 (1990),679-712.   
M3. McDuff, D.: Symplectic 4-manifolds, toappear in Proceedingsof International Congress of Mathematics,Kyoto,1990.   
M4. McDuff, D.: Notes on Rules symplectic manifolds,preprint, January 1992.

# The 4-Dimensional Symplectic Camel and Related Results

DUSA MCDUFF AND LISA TRAYNOR January 1991,revised January 1992

# $\ S 1$ INTRODUCTION

Consider $\pmb { \mathbb { R } } ^ { 4 }$ with the standard symplectic structure $\omega _ { 0 }$ . The open set ${ \cal E } _ { \lambda } \subset ( { \mathbb R } ^ { 4 } , \omega _ { 0 } )$ is defined to be the union of the two half spaces $\{ y _ { 1 } < 0 \}$ ， $\left\{ y _ { 1 } \ > \ 0 \right\}$ ，and the open 3-ball $U ( \lambda ) : = \{ ( x _ { 1 } , 0 , x _ { 2 } , y _ { 2 } ) \colon x _ { 1 } ^ { 2 } + x _ { 2 } ^ { \dot { 2 } } + y _ { 2 } ^ { 2 } <$ $\lambda ^ { 2 } \} \subset \{ y _ { 1 } = 0 \}$ . The 4-dimensional symplectic camel problem, first posed by Gromov,asks the following question $[ \mathbf { A } ]$ : Using a 1-parameter family of symplectic diffeomorphisms,can a closed ball $B ( R )$ of radius $\textstyle R \geq \lambda$ be moved from one half space of $\pmb { { \cal E } } _ { \lambda }$ to the other? It is not hard to see that it is possible to move such a ball from one half space to the other via a 1-parameter family of volume-preserving diffeomorphisms. However, using tools developed in Gromov's 1985 paper $\mathbf { \left[ G \right] }$ ,it has been proven that it is impossible to carry out this construction using a 1-parameter family of symplectic diffeomorphisms.Eliashberg and Gromov sketch a proof in {EG,3.4],which is valid in all dimensions and uses Eliashberg's technique of filling by holomorphic discs.

Rephrased, this result says the space ${ \pmb \mathcal { E } } ( R , \lambda )$ of symplectic embeddings of $B ( R )$ into $\pmb { { \cal E } } _ { \lambda }$ has at least two components when $\pmb { R } \geq \lambda$ . Viterbo then conjectured that $\pmb { { \cal E } } _ { \lambda }$ and ${ \pmb { E } } _ { \pmb { \mu } }$ are not symplectomorphic when $\lambda \neq \mu$ . This conjecture could immediately be proven if one also knew that ${ \pmb \mathcal { E } } ( R , \lambda )$ has exactly one component when $\pmb { R } < \lambda$ . However there might be an embedding whose image is so tangled up in the “hole" $U ( \lambda )$ of ${ \pmb E } _ { \lambda }$ that it is impossible to isotop it to one side or the other.Thus it is not known whether an arbitrary embedding is symplectically isotopic to one of the standard inclusions. As we will see below,an embedding which has an extension to the ball of radius $\pm \lambda$ is symplectically isotopic to an inclusion.Using this,we will show:

MAIN THEOREM. $\pmb { { \cal E } } _ { \lambda }$ is symplectomorphic to ${ \pmb { E } } _ { \pmb { \mu } }$ if and only if $\lambda = \mu$

Our proof uses techniques specific to dimension 4, but we conjecture the result is true in higher dimensions as well.

In order to explain the proof,it is convenient to introduce the folowing terminology. Let $g _ { R } ^ { + }$ and $\pmb { g } _ { R } ^ { - }$ be elements of $\pmb { \mathcal { E } } ( R , \lambda )$ which embed $B ( R )$ linearly into the spaces $\left\{ y _ { 1 } ~ < ~ 0 \right\}$ and $\{ y _ { 1 } ~ > ~ 0 \}$ ，respectively. Further, let $\pmb { \mathcal { E } } ( R , R _ { 1 } , \lambda )$ denote the subset of $\pmb \mathcal { \varepsilon } ( R , \lambda )$ consisting of those embeddings which extend to $B ( R _ { 1 } )$ . Then we have:

EXTENDABLE EMBEDDINGS LEMMA.Every element in $\mathcal { E } ( R , R + \lambda , \lambda )$ is symplectically isotopic either to $g _ { R } ^ { + }$ or to $\pmb { g } _ { R } ^ { - }$

PROOF OF MAIN THEOREM: Suppose $\psi \colon E \lambda \ \to \ E _ { \mu }$ is a symplectomorphism with $\lambda < \mu$ ,and $\pmb { R }$ is chosen so that $\lambda < R < \mu$ . Then $\psi _ { \ast }$ induces an isomorphism

$$
\pi _ { 0 } ( { \mathcal E } ( R , \lambda ) ) \longrightarrow \pi _ { 0 } ( { \mathcal E } ( R , \mu ) ) .
$$

By the symplectic camel theorem, the embeddings $g _ { R } ^ { \pm }$ represent distinct elements in $\pi _ { \mathbf { 0 } } ( { \mathcal { E } } ( R , \lambda ) )$ . But,because they extend over $B ( R + \mu )$ ，the above Lemma implies that their composites with $\psi$ are isotopic to standard linear embeddings into ${ \pmb \mathcal { E } } ( R , { \pmb \mu } )$ , and hence, since $R < \mu$ , represent the same element of $\pi _ { 0 } ( \mathcal { E } ( R , \mu ) )$ . This contradiction proves the theorem.■

The Extendable Embeddings Lemma is proved by using the special properties of fllings in dimension 4. Recall that a flling of a 2-sphere $\pmb { S }$ isa 1-parameter family of disjoint,embedded $\pmb { J }$ -holomorphic discs whose boundaries foliate $s$ and whose union ${ \pmb F } ( { \pmb J } )$ is homeomorphic to a 3-ball. Eliashberg has proven,although not published all details of his proof, that an embedded copy $s$ of $S ^ { 2 }$ in $\pmb { \mathbb { R } } ^ { 4 }$ can be filled as long as it sits inside a ${ \pmb J }$ convex hypersurface $\partial \Omega$ ,for some integrable, $\omega _ { 0 }$ -tame $\pmb { J }$ (see [E], $[ \mathbf { K } ] ,$ .In $\ S 2 \mathrm { - } \ S 4$ ，we write out the details of his proof in the special case when $s , \ J$ and $\partial \Omega$ are all “standard” near $s$ . In this case,because there are no hyperbolic points,we do not need to assume that $\pmb { J }$ is everywhere integrable.For completeness, the proof of the Camel Theorem is sketched in $\ S 5$ . In fact,in order to prove the Camel Theorem,one does not need the discs in the flling to be disjoint and embedded.All that matters is that the filling, $\pmb { F } ( \pmb { J } )$ ，of the boundary sphere of the “hole” $U ( \lambda )$ in $\pmb { { \cal E } } _ { \lambda }$ separates $\pmb { { \cal E } } _ { \lambda }$ . Thus it is easy to extend the proof to higher dimensions. However,to prove the Extendable Embeddings Lemma we need these special properties, since the main step is to join a suitable filling to the“wall” $\pmb { \mathrm { R } } ^ { 4 } - \pmb { \mathrm { E } } _ { \lambda }$ to create a hypersurface $Q$ in $\pmb { \mathbb { R } } ^ { 4 }$ such that the pair $( \mathbb { R } ^ { 4 } , Q )$ is symplectomorphic to $( \mathbb { R } ^ { 4 } , \mathbb { R } ^ { 3 } )$ . The details are given in $\ S 6$

We would like to thank $\mathbf { Y _ { 2 } }$ .Eliashberg and W. Klingenberg for explaining the technique of filling by ${ \bf J }$ -holomorphic discs to us.

# $\ S 2$ BASIC DEFINITIONS

Given a Riemann surface $( \Sigma , i )$ and an almost complex manifold $( V , J )$ ， a ${ \pmb J }$ -holomorphic map of $\pmb { \Sigma }$ into $V$ is a $( C ^ { 1 } )$ map $f \colon \Sigma  V$ with ${ \pmb J }$ -linear derivative, i.e.

$$
d f \circ i = J \circ d f .
$$

Recall,also, that an almost complex structure $\pmb { J }$ is said to be $\omega$ -tame if $\boldsymbol { \omega } ( \boldsymbol { v } , J \boldsymbol { v } ) > 0$ for all non-zero tangent vectors ${ \pmb v }$ ，and $\omega$ -compatible (or $\omega$ · calibrated) if $\omega ( v , w ) = \omega ( J v , J w )$ . We will use the coordinates $z _ { 1 } = x _ { 1 } + i y _ { 1 }$ and $z _ { 2 } = x _ { 2 } + i y _ { 2 }$ on $\mathbb { C } ^ { 2 } = \mathbb { R } ^ { 4 }$ and will write ${ \pmb J } _ { \pmb 0 }$ for the standard $\omega _ { 0 } \cdot$ compatible almost complex structure on $\pmb { \mathbb { R } } ^ { 4 }$ ，

Let $\partial \Omega$ be an oriented hypersurface in an almost complex 4-manifold $( V , J )$ , and, for each $\pmb { x } \in \partial \Omega$ ,let $\xi _ { x , J }$ be the maximal $\pmb { J }$ -invariant subspace of the tangent space $\pmb { T } _ { \pmb { x } } \partial \Omega$ $\partial \Omega$ is said to be $\pmb { J }$ -convex if for one (and hence any) defining 1-form $\pmb { \alpha }$ of ${ \pmb \xi }$ we have $d \alpha ( v , J v ) > 0$ for all non-zero $v \in \xi _ { x , J }$ Since $\xi = k e r \ \pmb { \alpha }$ ,it follows that $\pmb { \xi }$ is a contact structure on $\partial \Omega$

Throughout this paper, $\Omega \subset \mathbb { R } ^ { 4 }$ will denote a domain bounded by a smooth hypersurface $\partial \Omega$ . For our applications,we will be able to choose $\pmb { \Omega }$ so that $\partial \Omega$ is transverse to the radial vector field

$$
\partial = x _ { 1 } { \frac { \partial } { \partial x _ { 1 } } } + y _ { 1 } { \frac { \partial } { \partial y _ { 1 } } } + x _ { 2 } { \frac { \partial } { \partial x _ { 2 } } } + y _ { 2 } { \frac { \partial } { \partial y _ { 2 } } } .
$$

Consider ${ \pmb { \alpha } } = i ( \partial ) \omega _ { { \bf 0 } }$ . Then since $d \alpha = 2 \omega _ { 0 }$ and $\pmb { \partial }$ is transverse,it follows that $\pmb { \alpha }$ is a contact form on $\partial \Omega$ . Moreover, $\partial \Omega$ is $\pmb { J }$ -convex for any $\omega _ { 0 }$ -tame $\pmb { J }$ such that ker ${ \pmb { \alpha } } | _ { \partial \Omega }$ is $\pmb { J }$ -invariant. It will be convenient to assume further that $\Omega \cap \{ | y _ { 1 } | < \beta \} = B ^ { 4 } \cap \{ | y _ { 1 } | < \beta \}$ ， for some ${ \boldsymbol { \beta } } > \mathbf { 0 }$ ，where $B ^ { 4 }$ is the unit ball centered at the origin. In particular,notice that the standard unit 2-sphere $S \subset \{ y _ { 1 } = 0 \}$ sits inside $\partial \Omega$ ·

With $\pmb { \Omega }$ as described above,it is possible to construct a smooth function $\varphi$ on $\pmb { \mathbb { R } } ^ { 4 }$ such that $\Omega = \{ \varphi \leq 1 \}$ and $\partial \Omega = \{ \varphi = 1 \}$ .Let $\mathcal { I }$ be the set of smooth, $\omega _ { 0 }$ -compatible almost complex structures on $\pmb { \mathbb { R } } ^ { 4 }$ and let $c _ { \mathfrak { a } }$ be the open subset of $\mathcal { I }$ consisting of those $\pmb { J }$ which make dn $\pmb { J }$ -convex. Fix $1 > \varepsilon > 0$ and let

$$
{ \mathcal { I } } _ { \Omega } = \{ J \in { \mathcal { C } } _ { \Omega } : J = J _ { 0 } { \mathrm { ~ o n ~ } } \{ \varphi > 1 - \varepsilon \} \cap \{ | y _ { 1 } | < \beta \} \} .
$$

It follows from the above remarks that $\mathcal { I } _ { \Omega }$ is nonempty. Next, given $\pmb { \delta }$ such that $1 - \varepsilon < \delta < 1$ , put

$$
S _ { \delta } = \{ ( x _ { 1 } , 0 , x _ { 2 } , y _ { 2 } ) \in S \colon | x _ { 1 } | < \delta \} .
$$

Then $S _ { \delta }$ is diffeomorphic to an open annulus and, since the elements of $\mathcal { I } _ { \Omega }$ are standard near $s$ ， for each $J \in \mathcal { T } _ { \mathfrak { a } }$ ， $S _ { \delta }$ is a totally real surface sitting inside a ${ \pmb J }$ -convex $\partial \Omega$ . (Recall that a submanifold $M \in ( V , J )$ is said to be totally real if $T M \cap J T M = \{ 0 \}$ .）Let $D$ be the unit disc in C with almost complex structure $\pmb { i }$ and let $\pmb { A }$ be the generator of $\pi _ { 2 } ( \mathbb { R } ^ { 4 } , S _ { \delta } )$ which is represented by

$$
\begin{array} { l c r } { \displaystyle ( D , \partial )  ( { \boldsymbol \mathsf { R } } ^ { 4 } , S _ { \delta } ) } \\ { \displaystyle ( x , y ) \mapsto ( 0 , 0 , x , y ) . } \end{array}
$$

Notice that by our construction of $\mathcal { T } _ { \Omega }$ , for each $\pmb { c }$ such that $1 - \varepsilon < | c | < 1 .$ ，

$$
f _ { c } ( x , y ) = ( c , 0 , \sqrt { 1 - c ^ { 2 } } x , \sqrt { 1 - c ^ { 2 } } y )
$$

isa ${ \pmb J }$ -holomorphic map representing $\pmb { A }$ for all $\smash { J \in \mathcal { T } _ { \vartheta } }$ .We denote the images of these flat maps at height $\pmb { c }$ by $D _ { c }$ . Finally, for $J \in \mathcal { I } _ { \Omega }$ ，we define a $\pmb { J }$ -holomorphic A-disc to be the image of a $\pmb { J }$ -holomorphic map

$$
f \colon ( D , \partial )  ( \mathbb { R } ^ { 4 } , S _ { \delta } ) ,
$$

which represents $A \in \pi _ { 2 } ( \mathbb { R } ^ { 4 } , S _ { \delta } )$ and is in the connected component of the flat discs. Thus each $\pmb { J }$ -holomorphic $\pmb { A }$ -disc, Im $f$ , may be joined to a flat disc, $D _ { c }$ ,by a path $I m \ f _ { t }$ of ${ { J } _ { t } }$ -holomorphic $\pmb { A }$ -discs, where $J _ { t } \in \mathcal { T } _ { \Omega }$

# \$3 PROPERTIES OF $\pmb { J }$ -HOLOMORPHIC A-DISCS

Technically,we only require a $\pmb { J }$ -holomorphic map of the disc, $f$ , to have $\pmb { J }$ -linear derivative on the closed disc.However,since the boundary is sent to $S _ { \delta }$ , we can say more because of the following.

LEMMA 3.1. For some neighborhood $U$ of $S _ { \delta }$ in $( \mathbb { R } ^ { 4 } , J _ { 0 } )$ there is an antiholomorphicreflection $\sigma \colon U \to U$ in $S _ { \delta }$ ·

PROOF: Consider the cylinder $C = \{ ( x _ { 1 } , 0 , x _ { 2 } , y _ { 2 } ) \colon | x _ { 1 } | < 1 - \delta , x _ { 2 } ^ { 2 } + y _ { 2 } ^ { 2 } =$ 1}.There exists a neighborhood $U _ { 1 }$ of $c$ in $\mathbb { C } ^ { 2 }$ and $\sigma _ { 1 } \colon U _ { 1 } \to U _ { 1 }$ an antiholomorphic reflection in $c$ given by $\sigma ( z _ { 1 } , z _ { 2 } ) = ( \overline { { z _ { 1 } } } , \frac { 1 } { \overline { { z _ { 2 } } } } )$ . Choosing $U _ { 1 }$ sufficiently small,let $\boldsymbol { U }$ be the image of $U _ { 1 }$ under the biholomorphism $\varphi ( z _ { 1 } , z _ { 2 } ) \stackrel { \cdot } { = } \left( z _ { 1 } , \sqrt { 1 - z _ { 1 } ^ { 2 } } z _ { 2 } \right)$ and define $\pmb { \sigma }$ on $\boldsymbol { U }$ by $\sigma = \varphi \circ \sigma _ { 1 } \circ \varphi ^ { - 1 }$

Thus,by the Schwarz reflection principle, $f$ has a unique $\pmb { J }$ -holomorphic extension to a neighborhood of the closed disc.

PROPOSITION 3.2. All interior points of a $\pmb { J }$ -holomorphic A-disc are contained in Int $\pmb { \Omega }$

PROOF: Suppose there exists an $f$ such that Int $f$ is not contained in $I n t \Omega$ Since $f$ ,by definition,is in the connected component of the flat discs, there exists a family $f _ { t }$ of ${ { J } _ { t } }$ -holomorphic discs such that,for some $\pmb { t _ { 0 } }$ ，we have Im $f _ { t } \subset \Omega$ ，for $t \leq t _ { 0 }$ ，and Im $f _ { t _ { 0 } }$ is tangent to $\partial \Omega$ from the inside at $p = f _ { t _ { 0 } } ( z _ { 0 } )$ . We can break this into two cases.

(i) $z _ { 0 } \in$ Int $D$ . This is impossible by an application of the maximum principle. See [M5,Lemma 2.4].

(ii) $z _ { \mathbf { 0 } } \in \partial D$ . By construction $\scriptstyle J = J _ { 0 }$ near $\pmb { \mathscr { p } } \in S _ { \delta }$ ,and $\partial \Omega$ coincides with $S ^ { 3 }$ near $S _ { \delta }$ .Let $T _ { p } ^ { \mathbb { C } } S ^ { 3 }$ be the complex part of the tangent space to $\partial \Omega$ at $\pmb { p }$ and $( T _ { p } ^ { \mathbb { C } } S ^ { 3 } ) ^ { \perp }$ its $\omega _ { 0 }$ perpendicular. Then, if $\pi _ { p }$ is the orthogonal projection of $\pmb { \mathbb { R } } ^ { 4 }$ onto the complex line $( T _ { p } ^ { \mathbb { C } } S ^ { 3 } ) ^ { \perp }$ , the composite $\pi _ { p } \circ f _ { t _ { 0 } }$ is holomorphic in a neighbourhood of $\partial D$ in C.If it had a zero of infinite order at ${ z } _ { 0 }$ ,it would be constant near $\partial D$ ,which would contradict the fact that $f _ { t _ { 0 } }$ represents $\pmb { A }$ · Thus it must have a zero of finite order at ${ \pmb z _ { 0 } }$ and,by hypothesis,must have a zero of order at least two.Hence it maps a neighborhood of $z _ { \mathbf { 0 } } \in \partial D$ onto a neighborhood of $\mathbf { 0 } \in T _ { p } ^ { \mathbb { C } } S ^ { 3 } \equiv \mathbb { C }$ .But this is impossible, since Im $f _ { t _ { 0 } } \subset \Omega$ and $\pi _ { p }$ takesa neighborhood of $\pmb { p }$ in $\pmb { \Omega }$ into a half space in C.■

Because $S _ { \delta }$ is totally real, $\pmb { T S _ { \delta } } \cap \pmb { T ^ { \pmb { \tau } } } S ^ { 3 }$ is a real, orientable line field on $S _ { \delta }$ . It is not hard to check that this line feld is vertical,i.e.that its integral curves are the restrictions to $S _ { \delta }$ of the great arcs on $\pmb { S }$ through the poles $\{ ( \pm 1 , 0 , 0 , 0 ) \}$ . The above proof tells us the following.

COROLLARY 3.3. $f | _ { \partial D }$ is never vertical, i.e.

$$
T _ { p } ( f | _ { \partial D } ) \neq T _ { p } S _ { \delta } \cap T _ { p } ^ { \mathbb { C } } S ^ { 3 } .
$$

We will derive further important properties of our discs by a “doubling argument.” Let $N = U \cup I n t \ \Omega$ where $\boldsymbol { U }$ is as in Lemma 3.1. Let $N _ { 1 } , N _ { 2 }$ be two copies of $\pmb { N }$ and let $U _ { \mathbf { i } }$ be the copy of $\boldsymbol { U }$ in $N _ { \mathbf { i } }$ . Form the double

$$
V = N _ { 1 } \cup _ { \sigma } N _ { 2 } = { \frac { N _ { 1 } \amalg N _ { 2 } } { p \sim \sigma ( p ) } } \quad { \mathrm { f o r ~ } } p \in U _ { 1 } .
$$

One can check $V$ is a manifold and further that

$$
T _ { p } V = \left\{ \begin{array} { l l } { T _ { p } N _ { i } , } & { p \notin U _ { i } } \\ { \frac { T _ { p } N _ { 1 } \operatorname { I I } T _ { \sigma ( p ) } N _ { 2 } } { ( p , v ) \sim ( \sigma ( p ) , \sigma _ { * } v ) } , } & { p \in U _ { 1 } . } \end{array} \right.
$$

Consider

$$
J ^ { V } ( p ) = \left\{ \begin{array} { l l } { J ( p ) , } & { p \in N _ { 1 } } \\ { - J ( p ) , } & { p \in N _ { 2 } . } \end{array} \right.
$$

Since $\pmb { \sigma }$ is anti-holomorphic and $\pmb { J }$ is smooth,it follows that $J ^ { V }$ is a welldefined, smooth almost complex structure on $V$

Given a $\pmb { J }$ -holomorphic map $f \colon ( D , \partial )  ( \Omega , S _ { \delta } )$ a $\pmb { J } ^ { V }$ -holomorphic map $f ^ { V } \colon ( S ^ { 2 } , i ) = ( \mathbb { C } \cup \{ \infty \} , i ) \to ( V , J ^ { V } )$ can be constructed as follows. Let $f _ { 1 } , f _ { 2 }$ be copies of $f$ into $N _ { 1 } , N _ { 2 }$ respectively and let $r \colon { \bf C } ^ { 2 } \cup \{ \infty \}  { \bf C } ^ { 2 } \cup \{ \infty \}$ be the antiholomorphic reflection through $S ^ { 1 }$ given by $r ( z ) = 1 / \overline { { z } }$ .Define $f ^ { V } \colon \mathbf { C } \cup \{ \infty \}  V$ by

$$
f ^ { V } ( z ) = { \left\{ \begin{array} { l l } { f _ { 1 } ( z ) , } & { | z | \leq 1 } \\ { f _ { 2 } \circ r ( z ) , } & { | z | > 1 . } \end{array} \right. }
$$

It is not hard to verify that $f ^ { V }$ is a smooth, $\ J ^ { V }$ -holomorphic map of the sphere.

PROPOSITION 3.4. The $\pmb { J }$ -holomorphic $\pmb { A }$ -discs are embedded and disjoint.

PROOF: Let $f$ be a $\pmb { J }$ -holomorphic map representing A,and $z$ the image of its double. We will show that $z$ is embedded and is disjoint from the image $z ^ { \prime }$ of the double of any other $\pmb { J }$ -holomorphic $\pmb { A }$ -disc. Let $D _ { c }$ be a fat $\pmb { J }$ -holomorphic A-disc and $S _ { c }$ its double. Then $z$ and $S _ { c }$ are homologous $J ^ { V }$ -holomorphic 2-spheres and $\pmb { S _ { c } }$ is embedded. But it is shown in [M2, theorem 1.3] that there is a homological criterion for a J-holomorphic 2- sphere $c$ to be embedded: namely, $c$ is embedded if its virtual genus $g ( C )$ is 0,where $g ( C ) = 1 + { \textstyle \frac { 1 } { 2 } } ( C \cdot C - \mathsf { c } ( C ) )$ . (Here $\mathsf { c } \in H ^ { 2 } ( V ; \mathbf { Z } )$ is the first Chern class of the complex vector bundle $( T V , J )$ .） Since $g ( Z ) = g ( S _ { c } ) = 0$ ， it follows that Z is embedded. Further

$$
Z \bullet Z ^ { \prime } = S _ { c } \bullet S _ { c } = 0 .
$$

But,by [M2,theorem 1.1],every intersection point of $z$ with $z ^ { \prime }$ contributes positively to the algebraic intersection number $z \cdot z ^ { \prime }$ . Hence $z$ and $z ^ { \prime }$ are disjoint.

COROLLARY 3.5. For all $\pmb { J }$ -holomorphic A maps $f$ ，

$$
\left| \omega _ { 0 } \cdot \overrightarrow { \mathrm { a } } r \mathrm { e a } \mathrm { ~ o f ~ } f \right| = \left| \int _ { f ( D ) } \omega _ { 0 } \right| \leq \pi .
$$

PROOF: By an easy calculation,integrating $\omega _ { 0 }$ over a portion of the top hemisphere of the 2-sphere $s$ $\left( \pmb { x } _ { 1 } > \pmb { 0 } \right)$ gives a positive value while integrating over a portion of the bottom hemisphere produces a negative value. The result now follows from Stokes' theorem and the fact that $I m \textbf { } f$ is an embedded disc with boundary on $S _ { \delta } \subset S$

# $\ S 4$ FILLING THE SPHERE

In this section we show that the unit 2-sphere $s$ in the hyperplane $\{ y _ { 1 } =$ ${ \bf 0 } \}$ has a $\pmb { J }$ -filling $\pmb { F } ( \pmb { J } )$ for all $J \in \mathcal { I } _ { \Omega }$ . More precisely:

(4.1） SPHERE FILLING THEOREM.For all $\smash { J \in \mathcal { T } _ { \vartheta } }$ ,there is a l-parameter family of disjoint, $\pmb { J }$ -holomorphic discs whose boundaries foliate $s$ and whose union $\pmb { F } ( \pmb { J } )$ is diffeomorphic to $B ^ { 3 }$

Note that $\pmb { F } ( \pmb { J } )$ contains two degenerate discs at the poles $( \pm 1 , 0 , \mathbf { 0 } , \mathbf { 0 } )$ of $\pmb { S }$ ·

We will just give a sketch of the proof since it follows by standard Fredholm theory from the results of $\ S 3$ . The first step is to define suitable Banach manifolds of almost complex structures and maps.

The results used in Proposition 3.4 require that $\pmb { J }$ be smooth.Therefore, we will use the following procedure of Floer [F] to construct a Banach manifold $N ( J ) \subset \mathcal { T } _ { \Omega }$ containing a given $\pmb { J }$ . The tangent space $\pmb { T } _ { J } \mathcal { T } _ { \Omega }$ to $\mathcal { I } _ { \Omega }$ at $\pmb { J }$ consists of the space $C ^ { \infty } ( S \ j )$ of smooth sections $j$ of the bundle End $( T _ { \tt L } \pmb { \mathbb { R } } ^ { 4 } )$ such that $j J + J j = 0$ ， $\langle j \alpha , \beta \rangle + \langle \alpha , j \beta \rangle = 0$ (where $\langle ~ , ~ \rangle$ is the standard inner product),and ${ j ( { \pmb x } ) = \bf 0 }$ on $\{ \varphi > 1 - \varepsilon \} \cap \{ | y _ { 1 } | < \beta \}$ Let $\bar { \varepsilon } = ( \varepsilon _ { i } ) _ { i \in \mathbb { N } }$ be any sequence of positive real numbers. Then

$$
\| \boldsymbol j \| _ { \boldsymbol \varepsilon } = \sum _ { \boldsymbol k \in \mathbb { N } } \varepsilon _ { \boldsymbol k } \operatorname* { m a x } _ { \boldsymbol { x } \in \mathbb { R } ^ { 4 } } | D ^ { \boldsymbol k } \boldsymbol j ( \boldsymbol x ) |
$$

is a norm on the linear space

$$
C ^ { \sharp } ( S _ { J } ) = \{ j \in C ^ { \infty } ( S _ { J } ) : \lVert j \rVert _ { \bar { \varepsilon } } < \infty \} .
$$

Further,one can check $C ^ { \bar { \varepsilon } } ( S _ { J } )$ is a Banach space. As Floer has shown $[ \mathbf { F } ,$ Lemma 5.1],it is possible to choose $\bar { \varepsilon }$ so that $C ^ { \bar { \varepsilon } } ( S _ { J } )$ is dense in $\pmb { T } _ { J } \pmb { \mathcal { T } } _ { \Omega }$ with respect to the $L ^ { 2 }$ -norm. Choose $\pmb { r } > \pmb { 0 }$ small enough so that, for $\| \boldsymbol j \| _ { \widetilde \epsilon } < r$ ,the exponential map is injective. Let $N ^ { \prime } ( J ) = \{ j \in C ^ { \bar { \varepsilon } } ( S _ { J } ) : \| j \| _ { \bar { \varepsilon } } < r \}$ . Then $N ^ { \prime } ( J )$ is an open set of a Banach space and thus a Banach manifold. Define $N ( J )$ to be the image of $N ^ { \prime } ( J )$ under the exponential map diffeomorphism.

Now, fix $\pmb { \mathscr { s } } > 1$ and let $\mathcal { F } = \mathcal { F } _ { A , s } ^ { \delta }$ be the Sobolev space $H ^ { s + 1 } ( D , \partial ; \mathbb { R } ^ { 4 } , S _ { \delta } )$ of all maps $f \colon ( D , \partial )  ( \mathbb { R } ^ { 4 } , S _ { \delta } )$ whose $( s + 1 ) ^ { t h }$ derivative is $L ^ { 2 }$ and which represent $A \in \pi _ { 2 } ( \mathbb { R } ^ { 4 } , S _ { \delta } )$ ：

For ${ \pmb J } _ { 1 } \in \mathcal { T } _ { \Omega }$ , define

$$
\begin{array} { r } { \mathcal { M } = \mathcal { M } ( N ( J _ { 1 } ) ) = \{ ( f , J ) \in \mathcal { F } \times N ( J _ { 1 } ) : \bar { \partial } _ { J } f = d f + J \circ d f \circ } \end{array}
$$

PROPOSITION 4.2. $\mathcal { M }$ is a Banach submanifold of $\mathcal { F } \times N ( J _ { 1 } )$

PROOF: This can be proved locally using the procedure of McDuf [M1, \$4]. There are two points to note. First observe that,because $S _ { \delta }$ is totally real, the boundary conditions imposed on our maps are elliptic (see [BB]). Thus,in the notation of [M1,\$4], $\pmb { L } _ { J }$ is still Fredholm and $I m \ d \Phi$ is closed and of finite dimension. The proof that O is a regular value of $d \Phi _ { ( f , J ) }$ goes through as before,provided that Im $f$ intersects the part of $\pmb { \mathbb { R } } ^ { 4 }$ where the elements of $\mathcal { T } _ { \Omega }$ are allowed to vary. However,one must also consider the possibility that Im $f$ is contained in the region $\left\{ \varphi \geq 1 - \varepsilon \right\} \cap \left\{ \left| y _ { 1 } \right| \leq \beta \right\}$ where $\pmb { J }$ is constrained to equal ${ \pmb J } _ { \pmb 0 }$ .But then the integrability tensor of $\pmb { J }$ vanishes on $I m \textbf { } f$ . Thus $L _ { J }$ is just the usual $\bar { \partial }$ operator and so is surjective, as required. ■

It follows as in McDuf [M1,Proposition 4.2] that the projection map

$$
P _ { A } = P _ { A , J _ { 1 } } \colon \mathcal { M } ( N ( \bar { J } _ { 1 } ) )  N ( \bar { J } _ { 1 } )
$$

is Fredholm.By the Sard-Smale theorem, there is a subset of second category $N ( J _ { 1 } ) _ { r \epsilon g } \subset N ( J _ { 1 } )$ which consists of regular elements. For these ${ \pmb J }$ ,the inverse image

$$
P _ { A } ^ { - 1 } ( J ) = : { \mathcal { M } } _ { p } ( J , A , \delta )
$$

is a manifold.Let $( \mathcal { T } _ { \Omega } ) _ { r \epsilon g }$ be the union of all the $N ( J ) _ { r \epsilon g } , J \in \mathcal { T } _ { \Omega }$ . Since this is an uncountable union, the set $( \mathcal { T } _ { \Omega } ) _ { r \epsilon g }$ need not be of second category. However,it is dense.

Since the index of $P _ { A , J }$ is determined by the symbol of the elliptic operator $\pmb { L } _ { J }$ ，one easily sees that it is independent of $J \in \mathcal { T } _ { \Omega }$ ，and so may be calculated by considering a specially nice ${ \pmb J }$ . Thus,suppose that $\scriptstyle J \ = \ J _ { 0 }$ near the unit ball $B ^ { 3 } \subset \{ y _ { 1 } = 0 \}$ . Then the flat maps $f _ { c }$ ,for $| { \mathsf { c } } | < 1 - \varepsilon$ are $\pmb { J }$ -holomorphic. Since the boundaries of these flat discs completely fill $S _ { \delta }$ and,by Proposition 3.4,we know that distinct discs must be disjoint,it follows that these flat discs are the only $\pmb { J }$ -holomorphic $\pmb { A }$ -discs.Thus, there is a 4-parameter family of flat ${ \pmb J }$ -holomorphic A-discs. (Note that three of these dimensions correspond to the reparametrization group $P S L ( 2 , \pmb { \mathbb { R } } ) .$ ） Further, since $\pmb { J }$ is integrable near the image of each flat disc, $\pmb { L } _ { J }$ is the usual $\hat { \hat { \partial } }$ operator and it is easy to see that $( f _ { c } , J )$ is a regular point for all c. It follows that $\pmb { J }$ is a regular value for $P _ { A , J }$ .Hence the index of $P _ { A , J }$ is 4 and we have shown:

PROPOSITION 4.3.For all ${ \pmb J }$ in a dense set $( \mathcal { T } _ { \Omega } ) _ { r \epsilon g }$ of $\mathcal { I } _ { \Omega }$ ， $M _ { p } ( J , A , \delta )$ isa smooth 4-manifold.

The next step is to compactify the manifolds $\mathcal { M } _ { p } ( J _ { i } , A , \delta )$ .It is not enough simply to quotient out by the noncompact reparametrization group $G = P S L ( 2 , \pmb { \mathsf { R } } )$ of all biholomorphisms of the disc,because $S _ { \delta }$ is itself not compact. To fix this, we will consider the closure $\overline { { S } } _ { \delta }$ of $S _ { \delta }$ . Let ${ \overline { { \mathcal { M } } } } _ { p } ( J , A , \delta )$ consist of all ${ \bf J }$ -holomorphic discs with image in $( \Omega , { \overline { { S } } } _ { \delta } )$

LEMMA 4.4. $\overline { { \mathcal { M } } } _ { p } ( J , A , \delta ) = \mathcal { M } _ { p } ( J , A , \delta ) \cup ( f _ { \delta } ) _ { G } \cup ( f _ { - \delta } ) _ { G } ,$ where $( f _ { \delta } ) _ { G }$ is the $G$ orbit of thefat discat height $\delta$ and similarly for $( f _ { - \delta } ) _ { G }$

PROOF:The inclusion $\supset$ is clear. Conversely, suppose there exists an $f$ such that Im $f$ is a non-flat A-disc which intersects one of the circles of $\overline { { S } } _ { \delta } \backslash S _ { \delta }$ By construction of $\mathcal { I } _ { \Omega }$ and definition of $\delta$ ,there are flat $\pmb { J }$ -holomorphic discs whose boundaries lie on these circle. Thus, $I m f$ must intersect one of these flat discs,which contradicts Proposition 3.4.■

PROPOSITION 4.5.For all $\textbf { \textit { J } } \in \ \mathcal { I } _ { \Omega }$ ，the space of unparametrized $\pmb { J }$ -holomorphic A-discs, $\overline { { \mathcal { M } } } _ { p } ( J , A , \delta ) / G$ is diffeomorphic to a compact interval.

PROOF: First suppose $J \in ( \mathcal { I } _ { \Omega } ) _ { r \epsilon g }$ . It is easy to see that in this case $\overline { { \mathcal { M } } } _ { p } ( J , A , \delta ) / G$ is a1-dimensional manifold with two boundary points given by $[ f _ { \pm \delta } ]$ . Therefore,it suffices to prove that it is compact and connected.

To see that this space is compact,double all the discs so that they become $J ^ { V }$ -holomorphic $A ^ { V }$ -spheres. Construct a metric $g _ { J } ^ { V }$ on $V$ by piecing together $g _ { 1 } ( v , w ) \bar { = } \omega _ { 0 } ( v , J ^ { \bar { V } } w )$ on $N _ { 1 }$ and $g _ { 2 } ( v , w ) = - \dot { \omega _ { 0 } } ( v , J ^ { V } w )$ on $N _ { 2 }$ ， and observe that,by Corollary 3.5,all the $\ J ^ { V }$ -holomorphic $A ^ { V }$ -spheres are uniformly bounded in the associated $H ^ { 1 }$ Sobolev norm. Thus one can apply the standard compactness theorem for closed J-holomorphic spheres. (See, for example,[M4,(2.4)].） Clearly,any limiting cusp-curve is the double of a $\pmb { J }$ -holomorphic “cusp-disc”in $\pmb { \Omega }$ . The most general form for such a cuspdisc is a connected union of $\pmb { J }$ -holomorphic components, some of which are discs and some of which are “bubbles”(i.e. $\pmb { J }$ -holomorphic spheres).In our case,Corollary 3.3 implies that the boundary of the cusp-disc is transverse to the vertical,and so only one of its components can be a disc. Further, there can be no bubbles since $\pi _ { 2 } ( \Omega ) = 0$ . Hence, the limit must consist of a single disc.This proves compactness.(An alternative proof,which does not use doubling, may be constructed by the methods of [O].)

It follows that one connected component of ${ \overline { { \mathcal { M } } } } _ { p } ( J , A , \delta )$ is diffeomorphic to a compact interval. Since this component is non-empty and contains the fat discs $f _ { \pm \delta }$ , the boundaries of the discs in this component must fill out the whole of $S _ { \delta }$ . But distinct discs are disjoint.Therefore there can be no other discs and ${ \overline { { \mathcal { M } } } } _ { p } ( J , A , \delta )$ is connected,as claimed.

Now consider an arbitrary $\pmb { J }$ . We first claim that there is a $\pmb { J }$ -holomorphic disc through each point of $S _ { \delta }$ . This follows from the compactness theorem, because it is true for regular $\pmb { J }$ and because regular elements are dense in $\mathcal { I } _ { \Omega }$ . Next observe that,if $\pmb { \alpha }$ is a vertical arc in $s$ going from one pole to the other,Corollary 3.3 implies that each disc intersects $\pmb { \alpha }$ exactly once.The result now follows easily. ■

# (4.6) PROOF OF THEOREM 4.1.

Let

$$
\mathcal { M } _ { p } ( \boldsymbol { J } , \boldsymbol { A } ) = \overline { { \mathcal { M } } } _ { p } ( \boldsymbol { J } , \boldsymbol { A } , \boldsymbol { \delta } ) \cup \{ f _ { c } \circ \gamma \colon \boldsymbol { \delta } < | \mathsf { c } | \leq 1 , \gamma \in G \} ,
$$

and let $F ( J )$ be the image of the evaluation map

$$
e _ { D } ( J ) \colon { \mathcal { M } } _ { p } ( J , A ) \times _ { G } ( D , \partial ) \to ( \mathbb { R } ^ { 4 } , S ) .
$$

We showed that $\partial { \cal F } ( J ) = { \cal S }$ in the proof of Proposition 4.5. Since $\pmb { G }$ acts freely away from the degenerate discs at the poles, $\overline { { \mathcal { M } } } _ { p } ( J , A , \delta ) \times _ { G } ( D , \partial )$ is a fber bundle over the interval $\overline { { \mathcal { M } } } _ { p } ( J , A , \delta ) / G$ with fiber $( D , \partial )$ . Thus $M _ { p } ( J , A ) \times _ { G } ( D , \partial )$ ,with its obvious smooth structure,is diffeomorphic to a 3-ball. By Proposition 3.4, $\pmb { e } _ { D } ( J )$ is injective and restricts to an embedding on each disc. The fact that it is a diffeomorphism onto its image $F ( J )$ may be proved by the argument in [M3, Lemma 3.5]. ■

# $\ S 5$ THE CAMEL THEOREM

We start by constructing particular regions $\pmb { \Omega }$ to which we can apply our Sphere Filling result. The regions will be constructed by centering large 4-balls of radius $\pmb { \kappa }$ at $( 0 , \pm \kappa , 0 , 0 )$ and smoothing the union via a“solid cylinder” which agrees with $B ^ { 4 } ( \lambda )$ near $\left\{ y _ { 1 } = 0 \right\}$ .More precisely, choose $\kappa > \lambda > 0$ and consider $\Omega ( \kappa , \lambda ) = \{ \varphi _ { \kappa , \lambda } \leq 1 \}$ for $\varphi _ { \kappa , \lambda } = \frac { \textstyle 1 } { \kappa ^ { 2 } } ( x _ { 1 } ^ { 2 } + \rho ( y _ { 1 } ) +$ $x _ { 2 } ^ { 2 } + y _ { 2 } ^ { 2 } )$ where $\rho = \rho _ { \kappa , \lambda }$ is a smooth function such that

$$
\rho ( y _ { 1 } ) = \left\{ \begin{array} { l l } { ( y _ { 1 } + \kappa ) ^ { 2 } , } & { y _ { 1 } < - \alpha _ { \kappa , \lambda } } \\ { ( y _ { 1 } - \kappa ) ^ { 2 } , } & { y _ { 1 } > \alpha _ { \kappa , \lambda } } \\ { y _ { 1 } ^ { 2 } + \kappa ^ { 2 } - \lambda ^ { 2 } , } & { | y _ { 1 } | < \beta _ { \kappa , \lambda } } \end{array} \right.
$$

and

$$
\rho ( y _ { 1 } ) \leq m i n ( ( y _ { 1 } + \kappa ) ^ { 2 } , ( y _ { 1 } - \kappa ) ^ { 2 } ) .
$$

Here we assume that $0 < \beta _ { \kappa , \lambda } < \alpha _ { \kappa , \lambda } $ ，and that, for each $\lambda$ $\lambda , \alpha _ { \kappa , \lambda }  0$ as $\kappa  \infty$ .Then, $E _ { \lambda } = \cup _ { \kappa } I n t ( \Omega ( \kappa , \lambda ) )$ . Also notice these conditions guarantee that $\Omega ( \kappa , \lambda ) | _ { | y _ { 1 } | < \beta _ { \kappa , \lambda } } = B ^ { 4 } ( \lambda ) | _ { | y _ { 1 } | < \beta _ { \kappa , \lambda } }$ . An easy calculation shows:

LEMMA 5.1. It is possible to choose $\pmb { \rho }$ so that it satisfes (1) and (2) and so that $\partial \Omega ( \kappa , \lambda ) = \{ \varphi _ { \kappa , \lambda } = 1 \}$ is transverse to the radial vector feld $\partial$

We can therefore apply our fillng result to $S ^ { 2 } ( \lambda ) \subset \partial \Omega ( \kappa , \lambda )$

(5.2) THE CAMEL THEOREM. If $\pmb { R } \geq \lambda$ , a standard linear embedding $\pmb { g } _ { R } ^ { - }$ of $B ( R )$ into $E _ { \lambda } \cap \{ y _ { 1 } < 0 \}$ is not symplectically isotopic to the corresponding embedding $g _ { R } ^ { + }$ into $E _ { \lambda } \cap \left\{ y _ { 1 } > 0 \right\}$ ：

PROOF:Any isotopy $g _ { t } , 1 \leq t \leq 2$ from $\pmb { g } _ { R } ^ { - }$ to $g _ { R } ^ { + }$ is contained in a compact subset of $\pmb { { \cal E } } _ { \lambda }$ and hence in Int $\Omega = I n t \ \Omega ( \kappa , \lambda )$ for some $\pmb { \kappa }$ .Let $J _ { t } \in \mathcal { T } _ { \Omega }$ be a smooth family of almost complex structures chosen so that ${ \bar { J } } _ { t } = ( g _ { t } ) _ { * } { \bar { J } } _ { 0 }$ on Im ${ \pmb g } _ { \pmb t }$ . Because each filling $F ( J _ { t } )$ disconnects $\pmb { \Omega }$ , the set

$$
X = \{ ( t , x ) : x \in F ( J _ { t } ) , 1 \leq t \leq 2 \}
$$

disconnects $[ 1 , 2 ] \times \Omega$ . Further, since $( g _ { t } ) _ { * } J _ { 0 } = J _ { 0 }$ when $t = 1 , 2$ ,we may suppose that ${ { J } _ { 1 } }$ and $\scriptstyle { \mathcal { J } } _ { 2 }$ equal ${ \pmb J } _ { \pmb 0 }$ near the 3-ball $B ^ { 3 } ( \lambda ) \subset \{ y _ { 1 } = 0 \}$ . Then $F ( J _ { t } ) = B ^ { 3 } ( \lambda )$ when $t = 1 , 2$ and so the points $( 1 , g _ { 1 } ( 0 ) )$ and $( 2 , g _ { 2 } ( 0 ) )$ lie in distinct components of $( [ 1 , 2 ] \times \Omega ) \setminus X$ .Therefore, the path $( t , g _ { t } ( 0 ) )$ ， $1 \leq t \leq 2$ ，must intersect $\boldsymbol { x }$ .In other words, for some $\pmb { t }$ ，there is a ${ { J } _ { t } }$ holomorphic $\pmb { A }$ -disc $c$ through $g _ { t } ( 0 )$ . The argument is now completed in the usual way: see $[ \mathbf { G } ]$ or $[ \mathbf { M 4 } , ( 2 . 5 . 2 ) ]$ . Let $C ^ { \prime }$ be the pull-back of the disc $c$ by ${ \pmb g } _ { \pmb t }$ . Then $C ^ { \prime }$ isa ${ \pmb J _ { 0 } }$ -holomorphic curve through the center of the ball $B ( R )$ with boundary on $\partial B ( R )$ . Thus $C ^ { \prime }$ is a minimal surface and, by the monotonicity theorem,must have area $\geq \pi R ^ { 2 }$ with respect to the standard metric. On the other hand, this area can be calculated by integrating $\omega _ { 0 }$ over $C ^ { \prime }$ and hence is strictly bounded above by the integral of $\omega _ { 0 }$ over $c$ Yet we know,by corollary 3.5, that $\omega _ { 0 } ( C ) \le \pi \lambda ^ { 2 }$

# $\ S 6$ EMBEDDINGS OF BALLS

In this section we prove the Extendable Embeddings Lemma which states that any embedding $\pmb { g }$ of $B ( R )$ into $\pmb { { \cal E } } _ { \lambda }$ which extends to $B ( R { + } \lambda )$ is isotopic to one of the standard linear embeddings $g _ { R } ^ { \pm }$ . The following Lemma shows why we require that $\pmb { g }$ extend to $B ( R + \lambda )$ . We will suppose that $\pmb { \Omega }$ is one of the regions $\Omega _ { \kappa , \lambda } \subset E _ { \lambda }$ defined in $\ S 5$

LEMMA 6.1. If $g ( B ( R + \lambda ) ) \subset I n t ~ \Omega$ , then for every $J \in \mathcal { T } _ { \Omega }$ which equals $g _ { * } ( J _ { 0 } )$ on $g \big ( B \big ( R + \lambda \big ) \big )$ ,the flling $F ( J )$ does not intersect $g \big ( B \big ( R \big ) \big )$

PROOF: If $g ( B ( R ) )$ did intersect $F ( J )$ ， there would be a $J _ { 0 }$ -holomorphic curve $C ^ { \prime }$ of area $\scriptstyle < \pi \lambda ^ { 2 }$ through a point $z \in B ( R ) \subset B ( R + \lambda )$ . Since $C ^ { \prime }$ goes through the center of the ball $B ( z , \lambda ) \subset B ( R + \lambda )$ , this leads to a contradiction as in the proof of the Camel Theorem (5.2).■

PROPOSITION 6.2．Let $W = { \mathsf { R } } ^ { 3 } - B ^ { 3 } ( \lambda ) \subset \{ y _ { 1 } = 0 \}$ . For all $J \in \mathcal { T } _ { \Omega }$ ,the filling $F ( J )$ may be $\varepsilon$ -perturbed so that it fits together with W to form a 3-manifold $\pmb { Q }$ such that $\left( \mathbb { R } ^ { 4 } , Q , \omega _ { 0 } \right)$ is symplectomorphic to $\left( \mathbb { R } ^ { 4 } , \mathbb { R } ^ { 3 } , \omega _ { 0 } \right)$

Before proving Proposition 6.2, we show how Lemma 6.1 and Proposition 6.2 together prove our Extendable Embeddings Lemma. If $g \in \mathcal { E } ( R , R +$ $\lambda , \lambda )$ ,Lemma 6.1 tells us that $g \big ( B \big ( R \big ) \big )$ must lie on one of the sides of $W \cup F ( J )$ . Since we may choose $\varepsilon$ sufficiently small so that $Q \cap g ( B ( R ) ) = \emptyset$ ， this means $g \big ( B \big ( R \big ) \big )$ lies in a subset of $\pmb { { \cal E } } _ { \lambda }$ which is symplectomorphic to a half-space and hence to the whole of $\pmb { \mathbb { R } } ^ { 4 }$ . However, the space of symplectic embeddings of a ball into $\pmb { \mathbb { R } } ^ { 4 }$ is connected. In fact,it has the same homotopy type as the symplectic linear group $S p ( 4 , \pmb { \mathbb { R } } )$ . Hence $\pmb { \mathscr { g } }$ is isotopic to $g _ { R } ^ { \pm }$ as claimed.

In the course of proving Proposition 6.2,we will use a “parameterized family of fllings.” Consider the following 2-spheres and 4-balls of radius $\gamma$ ：

$$
\begin{array} { r l } & { S ( \gamma , s ) = \bigl \{ x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + y _ { 2 } ^ { 2 } = \gamma ^ { 2 } , y _ { 1 } = s \bigr \} , } \\ & { B ( \gamma , s ) = \bigl \{ x _ { 1 } ^ { 2 } + ( y _ { 1 } - s ) ^ { 2 } + x _ { 2 } ^ { 2 } + y _ { 2 } ^ { 2 } \leq \gamma ^ { 2 } \bigr \} . } \end{array}
$$

If we choose an almost complex structure $\pmb { J }$ such that $\begin{array} { r } { \mathbf { J } = J _ { \mathbf { 0 } } } \end{array}$ outside the 4-ball $B ( \mu ) \ = \ B ( \mu , 0 )$ and choose $\gamma > 2 \mu$ so that $B ( \mu ) \subset B ( \gamma , s )$ for $- \mu \leq s \leq \mu$ then, for each $\pmb { \mathscr { s } }$ , we may let $B ( \gamma , s )$ play the role of $\pmb { \Omega }$ , and so may fill $S ( \gamma , s )$ with respect to $\pmb { J }$ . Denote the filling by $F ^ { s } ( J )$

LEMMA 6.3. $F ^ { r } ( J ) \cap F ^ { s } ( J ) = \emptyset \ \mathrm { w h e n } \ r \neq s .$

PROOF: Notice that ${ \cal F } ^ { r } ( J ) \subset { \cal B } ( \gamma , r )$ for all $\pmb { r }$ by Proposition 3.2,and that $B ( \gamma , r ) \cap S ( \gamma , s ) = \emptyset$ when $\textit { \textbf { r } } \neq s$ .Thus if the discs $D ^ { r } \in F ^ { r } ( J )$ and $D ^ { s } \in F ^ { s } ( J )$ intersect,they must do so at a point which is in the interior of each disc.But this is impossible by positivity of intersections: see Proposition 3.4.■

PROOF OF PROPOsITION 6.2: We first construct the hypersurface $\pmb { Q }$ . It will be defined as the union of a 1-parameter family of symplectic 2-manifolds, each of which consists of a disc in the filling $F ( J )$ extended so as to join together with a fat 2-plane $\{ x _ { 1 } = \mathrm { c o n s t a n t }$ ， $y _ { 1 } = 0 \}$ outside some large ball.

By Corollary 3.3,the discs in $F ( J )$ meet any vertical arc $\pmb { \alpha }$ on $S = S ^ { 2 } ( \lambda )$ once transversally. Let $D _ { \nu } = I m \ f _ { \nu }$ be the disc in $F ( J )$ which intersects

this arc $\pmb { \alpha }$ at ${ \pmb x } _ { 1 } = { \pmb \nu }$ . Then

$$
\begin{array} { r l } & { f _ { \nu } ^ { * } \omega _ { 0 } = f _ { \nu } ^ { * } ( d x _ { 1 } \wedge d y _ { 1 } + d x _ { 2 } \wedge d y _ { 2 } ) } \\ & { \qquad = ( \pi _ { 1 } \circ f _ { \nu } ) ^ { * } ( d x _ { 1 } \wedge d y _ { 1 } ) + ( \pi _ { 2 } \circ f _ { \nu } ) ^ { * } ( d x _ { 2 } \wedge d y _ { 2 } ) , } \end{array}
$$

where $\pi _ { i }$ denotes the projection onto the $( x _ { i } , y _ { i } )$ plane. Both terms here are $\geq 0$ near $\partial D$ since $\pi _ { i } \circ f _ { \nu }$ is ${ \pmb J } _ { \pmb 0 }$ -holomorphic near $\partial D$ . Moreover, the second term is strictly positive,because the boundary of $\scriptstyle D _ { \nu }$ is transverse to the vertical arcs. Thus,by flattening the ${ \pmb y _ { 1 } }$ coordinate of $f _ { \nu }$ near $\partial D$ ，we can perturb the disc $\smash { D _ { \nu } }$ to a disc $\tilde { D } _ { \nu } = I m \ \tilde { f } _ { \nu }$ which is infinitely tangent to the hyperplane $\left\{ y _ { 1 } = 0 \right\}$ along its boundary and which is still symplectically embedded. Clearly,we may suppose that this perturbation is smooth with respect to $\pmb { \nu }$ ,and that all the discs $\tilde { D } _ { \nu } , - \lambda < \nu < \lambda$ ,are disjoint. Note that this perturbation does not alter the flat discs $\scriptstyle D _ { \nu }$ for $\pmb { \nu }$ near $\pm \lambda$

Now,let $P _ { \nu }$ be the portion of the fat plane $\{ ( x _ { 1 } , y _ { 1 } ) = ( \nu , 0 ) \}$ which lies outside $B ^ { 3 } ( \lambda )$ ,i.e. $P _ { \nu } = \{ ( \nu , 0 , x _ { 2 } , y _ { 2 } ) \not \in B ^ { 3 } ( \lambda ) \}$ .Perturb each $P _ { \nu }$ inside the hyperplane $\{ y _ { 1 } = 0 \}$ to a 2-dimensional space ${ \tilde { P } } _ { \nu }$ which is still a graph over the $\left( { { x } _ { 2 } } , { { y } _ { 2 } } \right)$ plane and which joins smoothly with $\partial \tilde { D } _ { \nu }$ . Then $L _ { \nu } = \mathcal { \bar { \tilde { D } } } _ { \nu } \cup \mathcal { \tilde { P } } _ { \nu }$ is a smoothly embedded 2-manifold which equals $P _ { \nu }$ outside a compact set. It is symplectic since both $\omega _ { 0 } | _ { \tilde { D } _ { \nu } }$ and $\omega _ { 0 } \big | _ { \tilde { P } _ { \nu } }$ are positive. Again, we may suppose that the $\scriptstyle { L _ { \nu } }$ vary smoothly with respect to $\pmb { \nu }$ ,and that they coincide with the fat planes $\{ ( x _ { 1 } , y _ { 1 } ) = ( \nu , 0 ) \}$ outside some compact subset $X$ of the strip $\vert x _ { 1 } \vert < \lambda \in \mathbb { R } ^ { 4 }$ ：

Let $Q \ = \ \cup _ { \nu } \bar { L } _ { \nu }$ . By construction, $\boldsymbol { Q }$ is foliated by the symplectic 2- manifolds $L _ { \nu }$

We now construct a symplectomorphism from $( \mathbb { R } ^ { 4 } , Q )$ to $( \mathbb { R } ^ { 4 } , \mathbb { R } ^ { 3 } )$ . Choose a ${ \pmb J } ^ { \prime }$ which equals ${ \pmb J } _ { \pmb 0 }$ outside some large 4-ball $B ( \mu )$ containing the compact subset $X$ defined above and such that the leaves of the foliation of $Q$ are $J ^ { \prime }$ -holomorphic.With $\gamma$ as in Lemma 6.3,let $S ( \gamma , s )$ be the 2-sphere in $\left\{ y _ { 1 } ~ = ~ s \right\}$ with filling $F ^ { s } ( J ^ { \prime } )$ .Note that the discs in $F ^ { 0 } ( J ^ { \prime } )$ are just the intersections of the leaves $L _ { \nu }$ with the ball $B ( \gamma , 0 )$ ．By Lemma 6.3,we know that the fillings $F ^ { s } ( J ^ { \prime } )$ are mutually disjoint. Thus, by repeating the above argument,we can perturb the $F ^ { s } ( J ^ { \prime } )$ so they fit together with the hyperplanes $\{ y _ { 1 } = s \}$ to form a foliation of $\pmb { \mathbb { R } } ^ { 4 }$ with leaves $Q ^ { s }$ ，each of which is foliated by symplectic 2-planes. Further,outside of a compact subset of $\pmb { \mathbb { R } } ^ { 4 }$ ， $Q ^ { s }$ coincides with $\{ y _ { 1 } = s \}$ and is foliated by the planes $\{ x _ { 1 } =$ constant}.

$\Lambda ^ { s } = k e r \ \omega _ { 0 } \big | _ { Q ^ { s } }$ $Q ^ { s }$ 3 se $- \frac { \partial } { \partial { \pmb x } _ { 1 } }$ $\phi _ { t } ^ { s }$   
$Q ^ { s }$ smoothly in $\pmb { \mathscr { s } }$ so that it preserves the foliation of each $Q ^ { s }$ and has   
tangent outside a compact set. Choose $\pmb { K }$ large enough so that the   
plane $\{ x _ { 1 } = \stackrel { \cdot } { K } , y _ { 1 } = \mathscr { s } \}$ is a symplectic leaf in $Q ^ { s }$ for all $\pmb { \mathscr { s } }$ . Then define   
$\bar { \Phi } \colon \mathsf { R } ^ { 4 } \to \mathsf { R } ^ { 4 }$ by

$$
\Phi ( p ) = \left( K - t , s , x _ { 2 } , y _ { 2 } \right)
$$

where $p \in Q ^ { s }$ is the image of the point $\left( K , s , x _ { 2 } , y _ { 2 } \right)$ under the map $\phi _ { t } ^ { s }$ This takes $Q ^ { s }$ to the hyperplane $\Pi ^ { s } = \left\{ y _ { 1 } = s \right\}$ ,for all s,but is not quite symplectic. Thus to complete the proof of Proposition 6.2,it remains to show

LEMMA 6.4. There exists a diffeomorphism $\pmb { h }$ of $( \mathbb { R } ^ { 4 } , Q )$ such that $h ^ { * } \Phi ^ { * } \omega _ { 0 } = \omega _ { 0 }$

PROOF: Let $\xi ^ { s }$ be the vector field on $Q ^ { s }$ whose flow is $\phi _ { t } ^ { s }$ . By construction, $\begin{array} { r } { \Phi _ { * } ( \xi ^ { s } ) = - \frac { \partial } { \partial x _ { 1 } } } \end{array}$ .It follows that if ${ \mathfrak { q } } = ( x _ { 1 } , s , x _ { 2 } , y _ { 2 } )$ where $x _ { 1 } > K$ ，then for all $\mathfrak { t } , \Phi \circ \phi _ { t } ^ { \bar { s } } ( q ) = \tau _ { t } \circ \Phi ( q )$ where $\tau _ { t } ( x _ { 1 } , y _ { 1 } , x _ { 2 } , y _ { 2 } ) = ( x _ { 1 } - t , y _ { 1 } , x _ { 2 } , y _ { 2 } )$ Since the restriction of $\omega _ { 0 }$ to $Q ^ { s }$ is invariant under $\phi _ { t } ^ { s }$ ,we can then conclude $\Phi ^ { * } \omega _ { 0 } | _ { Q ^ { * } } = \omega _ { 0 } | _ { Q ^ { * } }$ for all s. It follows that the forms $\omega _ { r } = r \Phi ^ { * } \omega _ { 0 } + ( 1 - r ) \omega _ { 0 }$ are non-degenerate on $\pmb { \mathbb { R } } ^ { 4 }$ when $0 \leq r \leq 1$ . Suppose we can find a 1-form $\beta$ which vanishes at all points of $\boldsymbol { Q }$ and satisfies $d \beta = \Phi ^ { * } \omega _ { 0 } - \omega _ { 0 }$ . Then if the vector feld $v _ { r }$ defined by

$$
i ( v _ { r } ) \omega _ { r } + \beta = 0
$$

is integrable, the standard Moser method argument shows that the integral $h _ { r }$ of $v _ { r }$ satisfies $h _ { r } ^ { * } \omega _ { r } = \omega _ { 0 }$ . Since $h _ { r } = i d$ on $Q$ the desired diffeomorphism is then given by $\pmb { h _ { 1 } }$ ·

Consider $\beta = \Phi ^ { * } \big ( x _ { 1 } d y _ { 1 } + x _ { 2 } d y _ { 2 } \big ) - \big ( x _ { 1 } d y _ { 1 } + x _ { 2 } d y _ { 2 } \big )$ . Outside a compact set $K _ { 1 }$ ，

$$
\Phi ( x _ { 1 } , y _ { 1 } , x _ { 2 } , y _ { 2 } ) = \left( x _ { 1 } , y _ { 1 } , \psi _ { y _ { 1 } } ( x _ { 2 } , y _ { 2 } ) \right)
$$

where $\psi _ { y 1 } : \mathsf { R } ^ { 2 } \to \mathsf { R } ^ { 2 }$ is independent of $\pmb { x } _ { 1 }$ ,and equals the identity outside a compact set $K _ { 2 }$ in the $\left( { { y _ { 1 } } , { x _ { 2 } } , { y _ { 2 } } } \right)$ -space. It follows that outside $K _ { 1 }$ ，

$$
\omega _ { r } = d x _ { 1 } \wedge d y _ { 1 } + d x _ { 2 } \wedge d y _ { 2 } + r ( h _ { 1 } ~ d y _ { 1 } \wedge d x _ { 2 } + h _ { 2 } ~ d y _ { 1 } \wedge d y _ { 2 } )
$$

where $\left| h _ { 1 } \right|$ and $\left| h _ { 2 } \right|$ are bounded functions of $y _ { 1 } , x _ { 2 } , y _ { 2 }$ . It is then easy to check that given any bounded 1-form $\beta$ , the associated vector field $v _ { r }$ defined by the equation $( v _ { r } ) \omega _ { r } + \beta = 0$ has bounded growth and is thus integrable. The $\beta$ which we constructed above is in fact bounded. However since it does not vanish on $\pmb { Q }$ we make the following modifications.

$\Phi ^ { * } \omega _ { 0 } | _ { Q } = \omega _ { 0 } | _ { Q }$ implies that $\beta | _ { Q }$ is closed. From the description of $\Phi$ outside the compact set $K _ { 1 }$ ,it is easy to check $\beta | _ { Q }$ is bounded.Thus $\beta | _ { Q } = d f$ where $f$ is a function on $Q$ and we can extend $f$ to a function $\widetilde { f }$ on $\pmb { \mathbb { R } } ^ { 4 }$ so that $d \widetilde { f }$ is bounded. Then ${ \beta } ^ { \prime } = { \beta } - d \widetilde { f }$ is cohomologous to $\beta$ ， is still bounded,and vanishes for all vectors in $\pmb { T Q }$ . Lastly we modify $\beta ^ { \prime }$ to a form $\beta ^ { \prime \prime }$ which equals zero at all points of $Q$ . To do this,first choose coordinates $x _ { 1 } ^ { \prime } , y _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , y _ { 2 } ^ { \prime }$ on $\pmb { \mathbb { R } } ^ { 4 }$ so that $Q = \{ y _ { 1 } ^ { \prime } = 0 \}$ and so that these are the standard coordinates on $\pmb { \mathbb { R } } ^ { 4 }$ outside a compact set. Suppose

$$
\beta ^ { \prime } = \sum f _ { i } d x _ { i } ^ { \prime } + g _ { i } d y _ { i } ^ { \prime } .
$$

Then $f _ { 1 } , f _ { 2 }$ and $\pmb { g _ { 2 } }$ vanish on $Q$ by construction. Further,outside a compact set,g1=1 where $\psi _ { y _ { 1 } } ( x _ { 2 } , y _ { 2 } ) = ( \psi ^ { 1 } , \psi ^ { 2 } )$ Hence ${ \pmb g } _ { \bf 1 }$ is independent of ${ \pmb x } _ { 1 }$ and has compact support with respect to the other variables. Therefore $d \big ( g _ { 1 } y _ { 1 } ^ { \prime } \big )$ is bounded and we may take $\beta ^ { \prime \prime } = \beta ^ { \prime } - d ( g _ { 1 } y _ { 1 } ^ { \prime } )$ ■

# REFERENCES

[A] Arnol'd, V.I.， First steps in symplectic topology， Russian Math. Surveys 41 6 (1986), 1-21.   
[BB] Booss,B.and Bleecker,D.D.,“Topology and Analysis: The Atiyah-Singer index formula and gauge theoretic physics,” Springer-Verlag,New York,1985.   
[E] Eliashberg，Ya., Filling by holomorphic discs and its applications,“Geometry of low dimensional manifolds,”London mathematical society lecture note series no. 152,Cambridge Univ.Press,1990.   
[EG]Eliashberg,Y.and Gromov,M., Conver symplectic manifolds, preprint (1990).   
[F] Floer,A., The unregularized gradient flow of the symplectic action, Comm. Pure Appl.Math.XLI (1988),775-813.   
[G] Gromov, M., Pseudo-holomorphic curves on almost complex manifolds, Invent. Math.82 (1985),307-347.   
[K] Klingenburg,W., Filling a 2-sphere in $\mathbf { C ^ { 2 } }$ by holomorphic discs, in preparation.   
[M1] McDuff,D., Examples of symplectic structures, Invent. Math.89 (1987),13-36.   
[M2] The local behaviour of holomorphic curves in almost complex 4-manifolds,Jour.Diff Geom.34 (1991),143-164.   
[M3] Blow ups and symplectic embeddings in dimension 4,Topology 30 (1991),409-421.   
[M4] Elliptic methods in symplectic geometry,Bull. Amer. Math. Soc. 23 (1990),311-358.   
[M5] ，Symplectic manifolds with contact type boundaries,Invent.Math. 23 (1990),311-358.   
[0] Oh,Y.-G., Removal of boundary singularities of pseudo-holomorphic curves with lagrangian boundary conditions,preprint (1990).

# Differential forms and connections adapted to a contact structure,after M Ruminl

Pierre Pansu

U.R.A. 169 du C.N.R.S. Centre de Mathématiques Ecole Polytechnique F-91128 Palaiseau

U.R.A. 1169 du C.N.R.S. Mathématiques   
Université Paris-Sud   
F-91405 Orsay

pansu@cmep.polytechnique.fr

Michel Rumin is a student of Mikhael Gromov,who asked him the following question : Let $M$ be a manifold with contact structure $\pmb { \xi }$ ， $\pmb { \cal E }$ a vector bundle over $M$ . A partial connection on $\pmb { \cal E }$ is a covariant derivative $\nabla _ { \boldsymbol { v } } \pmb { e }$ defined for smooth sections e of $\pmb { \cal E }$ but only for vectors ${ \pmb v }$ in $\pmb { \xi }$ .In particular,parallel translation is defined only along Legendrian curves, that is curves which are tangent to ${ \pmb \xi }$ . Can one define the curvature of such a connection ？

Gromov provided the following hint : For an ordinary connection $\pmb { A }$ ， curvature arises in the asymptotics of holonomy around short loops. A loop encompasses a certain “span”(a 2-vector, see below), quadratic in length, and holonomy deviates from the identity by an amount proportional to curvature times span, that is, quadratic in length. In case $M$ has dimension 3 and carries a contact structure, then every Legendrian loop has essentially zero area. Gromov conjectured that,in this case,curvature should arise as the cubic term in the asymptotic expansion of holonomy.

Michel Rumin has found a notion of curvature for partially defined connections along the above lines. The point is to understand the exterior differential for a partially defined 1-form. In fact,M.Rumin constructs a substitute for the de Rham complex : a locally exact complex of hypoelliptic operators naturally attached to a contact manifold $( M , \pmb \xi )$ of dimension $\mathbf { \nabla } _ { 2 m + }$ 1.The operator which sends m-forms to $\mathbf { m } { + 1 }$ -forms is new. It is of second order.

In this lecture, after some comments on the asymptotics of holonomy, I explain M. Rumin's construction. Then I describe an application of M. Rumin's ideas to analysis on complex hyperbolic space :boundary values of $L ^ { 2 }$ harmonic forms.I learned most of the material presented here thanks to P.Y.Gaillard,V.Goldshtein,J. Heber,P. Julg and M.Rumin.

# 1ASYMPTOTIC EXPANSION OF HOLONOMY

In this section,I explain how the asymptotic expansion of the holonomy of a smooth connection specializes to Legendrian curves in a contact manifold.

1.1The classical formula.- I define the “span",i.e.,the algebraic area spanned by a loop $c$ in a vector space $V = \mathbf { R } ^ { n }$ . Let $\alpha \in \Lambda ^ { 2 } V ^ { \ast }$ be a 2-form, viewed as a translation invariant differential form on $V$ . Then $d \alpha = 0$ ，and there exists a 1-form $\beta$ such that $d { \boldsymbol { \beta } } = \alpha$ . The linear functional

$$
\alpha \mapsto \int _ { c } \beta
$$

on $\Lambda ^ { 2 } V ^ { \ast }$ corresponds to a unique 2-vector span(c).

Now let $M$ be a differentiable manifold, $x \in M , c \subset M$ a small loop through $\pmb { x }$ . Using coordinate charts $\phi$ we define various covectors

$$
\mathsf { s p a n } _ { \phi } ( c ) = \mathsf { s p a n } \left( \phi ( c ) \right) \in \Lambda ^ { 2 } T _ { x } M
$$

which coincide up to an error of size $o ( \tt a r e a ( c ) )$ , where area $\cdot ( c )$ ,the “geometric area”,is the least area of a surface spanned by $c$ .Thus it makes sense to state

1.2 FACT .-Let $D$ be a connection on some vector bundle $\pmb { \cal E }$ over a manifold $M$ For ${ \pmb x } \in \mathcal { M }$ ， $c$ a short loop through $\pmb { x }$ ，let $H o l ( D , c )$ denote the holonomy of the connection $D$ along $c$ (an endomorphism of the fbre $\scriptstyle { \pmb { E } } _ { \pmb { z } }$ ） Then,as the length of $c$ tends to 0,

$$
H o l ( D , c ) = 1 + \langle F ^ { D } , \mathsf { s p a n } ( c ) \rangle + o ( \mathsf { a r e a } ( c ) ) ,
$$

where ${ \pmb F } ^ { D }$ is the curvature of $\pmb { D }$ at $\pmb { x }$ ,an $\mathbb { E } n d ( E _ { z } )$ -valued 2-form on $\pmb { T _ { x } M }$

1.3The case of contact manifolds.- Geometric areas will be measured relative to Carnot-Caratheodory metrics. Given a norm on the plane feld ${ \pmb \xi }$ ，a Carnot-Caratheodory metric is defined by minimizing the length of Legendrian curves between two points.

In dimension $2 m + 1 \geq 5$ ,every Legendrian curve bounds a Legendrian surface,which has Hausdorff dimension 2. Thus we define the geometric area area(c) to be the infimum of the 2-dimensional Hausdorf measures of surfaces whose boundary is $\pmb { c }$ .However,in dimension 3,all smooth surfaces have Hausdorf dimension 3,and we take 3-dimensional Hausdorff measure in the definition of geometric area. Note that contact transformations are Lipschitz with respect to Carnot-Caratheodory metrics,so they preserve the rough size of geometric areas.

Recall that the Heisenberg group $\pmb { N }$ of dimension $2 m + 1$ is the simply connected group attached to the following Lie algebra $\mathcal { N }$ ：

$$
\mathcal { N } = \mathbf { R } ^ { 2 m } \oplus \mathbf { R }
$$

with center $\mathbf { R }$ and the Lie bracket is given by the symplectic form $\mathbb { R } ^ { 2 m } \times$ $\mathbf { R } ^ { 2 m }  \mathbf { R }$ The left-invariant plane field generated by the factor $\mathbf { R } ^ { 2 m }$ is a contact structure ${ \pmb \xi _ { 0 } }$ . Every contact manifold is locally isomorphic to the Heisenberg group $( N , \xi _ { \mathbf { 0 } } )$

We define the “algebraic area” spanned by a Legendrian loop c in the Heisenberg group as before, but replacing the symplectic vector space, which is the local model for manifolds,by the Heisenberg group,which is the local model for contact manifolds.

In dimensions $2 m + 1 \geq 5$ ,the closed left invariant 2-forms on $\pmb { N }$ all are pulled-back from $N / [ N , N ] = \mathbb { R } ^ { 2 m } = \xi _ { 0 }$ . For such an $\alpha = d \beta$ ,the formula

$$
\langle \mathsf { s p a n } \left( c \right) , \alpha \rangle = \int _ { c } \beta
$$

defines a 2-covector span $( c ) \in \Lambda ^ { 2 } \xi _ { 0 }$ ,equivariantly with respect to Heisenberg automorphisms, and also,up to an error controlled by geometric area, with respect to contact diffeomorphisms.

Note that,if $\tau$ denotes some left-invariant 1-form whose kernel is the canonical contact structure ${ \pmb \xi _ { 0 } }$ ,then

$$
\langle \mathsf { s p a n } \left( c \right) , d \tau \rangle = 0 .
$$

In dimension 3,all left-invariant 2-forms are closed,and one gets a 2-covector span $( c ) \in \Lambda ^ { 2 } \mathcal { N }$

In both cases,one has

1.4 FACT.- Let $D$ be a connection on some vector bundle $\pmb { \cal E }$ over a contact manifold $( M , \xi )$ Let ${ \pmb x } \in { \pmb M }$ ，and $c$ be a short Legendrian loop through $\pmb { x }$ Then,as the length of $c$ tends to 0,

$$
H o l ( D , c ) = 1 + \langle F ^ { D } , \mathsf { s p a n } \left( c \right) \rangle + o ( \mathsf { a r e a } ( c ) ) .
$$

In dimensions $2 m + 1 \geq 5$ ， geometric area is quadratic in length (Y.Eliashberg,unpublished) and we see that the projection of $F ^ { D }$ in

$$
\Lambda ^ { 2 } \xi ^ { * } / \mathbb { R } d \tau
$$

only depends on the restriction of $D$ to the ${ \pmb \xi }$ directions,i.e.,it is an invariant attached to the partial connection $\nabla = D _ { | \xi }$ . We call it the curvature of $\boldsymbol { \nabla }$ It has $( m ( m - 1 ) / 2 ~ - 1 ) ( \operatorname { r k } { \cal E } ) ^ { 2 }$ independant components.

In dimension 3, the geometric area is cubic in length,and we cannot ignore the vertical components of span $( c )$ . We define the curvature of $\nabla =$ $D _ { | \xi }$ to be the projection of $F ^ { D }$ mod multiples of the symplectic structure $d \tau$ It has $2 ( \mathbf { r } \mathbf { k } \ : E ) ^ { 2 }$ independant components.

In the next section, these definitions will be shown to fit into the formalism of Rumin differential forms.

# 2RUMIN'S COMPLEX

It is a substitute for the de Rham complex, where 1-forms are replaced by partial 1-forms,i.e., sections of the dual of a contact structure.

Let $( M , \xi )$ be a $2 m + 1$ -dimensional contact manifold. Let $\Omega ^ { * }$ denote the graded algebra of smooth differential forms. Let $\tau ^ { * }$ be the graded differential ideal generated by contact forms (i.e.,1-forms $\tau$ whose kernel is the contact hyperplane $\pmb { \xi }$ )and $\mathcal { T } ^ { \star }$ the annihilator of $\tau ^ { * }$ (i.e., forms $\pmb { \alpha }$ such that $\alpha \wedge \beta = 0$ for all $\beta \in \mathcal { T } ^ { * }$ ). It is again a graded differential ideal.

Once a contact form $\tau$ is chosen,the elements of $( \Omega ^ { \ast } / \mathcal { T } ^ { \ast } ) \oplus \mathcal { T } ^ { \ast }$ identify with sections of subbundles or quotients of $\Lambda ^ { \ast } \xi ^ { \ast }$ . Indeed, let

$$
L : \Lambda ^ { k } \xi ^ { * } \to \Lambda ^ { k + 2 } \xi ^ { * }
$$

denote exterior multiplication by $d \tau _ { | \xi }$

$$
E ^ { k } = \Lambda ^ { k } \xi ^ { * } / \mathrm { i m } { \cal L } ,
$$

for $k \leq m$ ,and

$$
E ^ { k } = \ker L \subset \Lambda ^ { k } \xi ^ { * } ,
$$

for $k \geq m$ . Then $( \Omega ^ { k } / \mathcal { T } ^ { k } ) \oplus \mathcal { T } ^ { k }$ coincides with smooth sections of $E ^ { k }$ if $k \leq m$ ,and with smooth sections of $E ^ { k - 1 }$ multiplied by $\tau$ if $k \geq m + 1$ .In particular,the elements in $\Omega ^ { 1 } / \mathcal { T } ^ { 1 }$ are sections of ${ { \bf { E } } ^ { 1 } }$ , i.e., partial 1-forms.

There is an induced complex

$$
d _ { \pmb { \mathscr { k } } } : ( \Omega ^ { * } / \mathcal { T } ^ { * } ) \oplus \mathcal { T } ^ { * }  ( \Omega ^ { * } / \mathcal { T } ^ { * } ) \oplus \mathcal { T } ^ { * } .
$$

One easily checks that $d _ { \xi }$ is locally exact at $\Omega ^ { k } / \tau ^ { k }$ (resp. at $\mathcal { T } ^ { k }$ )if $k < m$ (resp. if $k > m + 1 )$ . This has been observed independantly by $\mathbf { v }$ .Ginzburg [5],and generalized by Zhong Ge, [15].

2.1THEOREM (M. Rumin, [14]).- There exists a linear second order operator

$$
d _ { R } \ : \Omega ^ { m } / T ^ { m }  \mathcal { T } ^ { m + 1 }
$$

such that the sequence

$$
0 \to \mathbb { R } \to \Omega ^ { 0 } { \xrightarrow { d _ { \ell } } } \Omega ^ { 1 } / T ^ { 1 } { \xrightarrow { d _ { \ell } } } \cdots { \xrightarrow { d _ { \ell } } } \Omega ^ { m } / T ^ { m } { \xrightarrow { d _ { R } } } { \mathcal { T } } ^ { m + 1 } { \xrightarrow { d _ { \ell } } } \cdots { \xrightarrow { d _ { \ell } } } { \mathcal { T } } ^ { 2 m + 1 } \to 0
$$

is a locally exact complex, i.e., a resolution of the constant sheaf R.

We explain this in 3 dimensions.If $\alpha \in \Omega ^ { 1 }$ is a 1-form,there is a unique choice of a function $\pmb { f }$ so that $d ( \alpha + f \tau )$ vanishes on $\pmb { \xi }$ . Take

$$
d _ { R } \big ( \alpha \ m o d \ T ^ { 1 } \big ) = d \big ( \alpha + f \tau \big ) \in \mathcal { T } ^ { 2 } .
$$

The function $\pmb { f }$ is determined by the equation

$$
d \alpha _ { | \xi } + f d \tau _ { | \xi } = 0
$$

and depends on first derivatives of $\pmb { \alpha }$ (in the ${ \pmb \xi }$ directions only),thus $d _ { R }$ involves two derivatives in the $\pmb { \xi }$ directions.

Given a metric on $\pmb { \xi }$ ,there is a normalization of the contact form $\tau$ s0 that $| d \tau _ { | \xi } | = 1$ . One gets a pointwise inner product on $\Omega ^ { * } / \tau ^ { * } \oplus \mathcal { I } ^ { * }$ ,and a Hodge operator

$$
\ast : \Omega ^ { k } / \mathcal { T } ^ { k } \to \mathcal { T } ^ { 2 m + 1 - k }
$$

such that $\ast 1 = \tau \wedge ( d \tau ) ^ { m }$ and

$$
\langle \alpha , \beta \rangle * 1 = \alpha \wedge * \beta .
$$

2.2THEOREM (M. Rumin,[14]).- Given a metric on $\pmb { \xi }$ ,put $d _ { \xi } ^ { * } = - * d _ { \xi } *$ (resp. $d _ { R } ^ { * } = - * d _ { R ^ { * } } )$ . This is a formal adjoint to $d _ { \pmb { \xi } }$ (resp. $d _ { R _ { . } }$ )

The laplacians

$$
\begin{array} { r c l } { { \dot { n } - k ) d _ { \xi } d _ { \xi } ^ { * } + ( n - k - 1 ) d _ { \xi } ^ { * } d _ { \xi } } } & { { \mathrm { o n } } } & { { ( \Omega ^ { k } / \mathcal { T } ^ { k } ) \oplus \mathcal { T } ^ { k } \quad f \mathrm { o r } \quad k \ne m , m + 1 , } } \\ { { } } & { { } } & { { } } \\ { { ( d _ { \xi } d _ { \xi } ^ { * } ) ^ { 2 } + d _ { R } ^ { * } d _ { R } } } & { { \mathrm { o n } \quad \Omega ^ { m } / \mathcal { T } ^ { m } , } } \\ { { } } & { { } } & { { } } \\ { { ( d _ { \xi } ^ { * } d _ { \xi } ) ^ { 2 } + d _ { R } d _ { R } ^ { * } } } & { { \mathrm { o n } \quad \mathcal { T } ^ { m + 1 } , } } \end{array}
$$

are maximally hypoelliptic.

Maximal hypoelipticity means that, given vector felds $X _ { i }$ tangent to $\pmb { \xi }$ ,one locally has estimates of the form

$$
\parallel X _ { 1 } X _ { 2 } \alpha \parallel _ { 2 } \leq C \left( \parallel \Delta \alpha \parallel _ { 2 } + \parallel \alpha \parallel _ { 2 } \right)
$$

for the second order Laplacian,and similarly for the fourth order Laplacian.

There is an analogue in contact geometry of the principal symbol, which gives a criterion for hypoellipticity, see [11]. However this criterion becomes effective only when combined with clever Bochner type formulas, see [14]. Simultaneously,various vanishing theorems are obtained. They include the following important feature :on a CR manifold whose Webster torsion vanishes (these are integrability conditions on the metric,analogous to the Kähler condition for Hermitian metrics), the above Laplacians preserve the bidegree (the unusual choice of coefficients is essential).

Back to connections : A partial connection is a Lie algebra valued partial 1-form $\pmb { A }$ and one can make sense of the curvature $d A + A \wedge A$ as was done for $d A$ . In dimensions $2 m + 1 \geq 5$ ,it isa Lie algebra valued 2-form on $\pmb { \xi }$ mod $d \tau$ ,in dimension 3,it is a Lie algebra valued 2-form vanishing on $\pmb { \xi }$ ， as announced in the previous section.

# 3 $L ^ { 2 }$ -HARMONIC FORMS ON COMPLEX HYPERBOLIC SPACE

Complex hyperbolic $m + 1$ -space is a complete symmetric Kahler manifold,isometric to the unit ball of $\mathbf { C } ^ { m + 1 }$ equipped with its Bergman metric. It is the symmetric space of the simple Lie group $S U ( m + 1 , 1 )$ . It is a generalization of the unit disk in C,equipped with its Poincaré metric,which is the symmetric space of $S U ( 1 , 1 ) = P S L ( 2 , { \bf R } )$

The new feature when $m \geq 1$ is that the boundary $S ^ { 2 m + 1 }$ inherits a canonical contact structure. At a point $x \in S ^ { 2 m + 1 }$ , the contact plane $\xi _ { x }$ is the maximal complex vector subspace in $T _ { x } S ^ { 2 m + 1 } \subset T _ { x } \mathbf { C } ^ { m + 1 }$ .

Complex hyperbolic $m + 1$ -space has ${ \pmb { L } } ^ { 2 }$ -cohomology in the middle dimension $m + 1$ and in each type $( p , q )$ ， $p { + } q = m { + } 1$ . Following recent work by Pierre Julg and Michel Rumin ([9]),we explain that ${ \pmb L } ^ { 2 }$ -harmonic forms have boundary values,which realize an isomorphism with an explicit space of Rumin differential forms on the boundary,the sphere $S ^ { 2 m + \bar { 1 } }$ equipped with its canonical contact structure.

3.1 The case of real hyperbolic space.- Let us first explain the corresponding theory for real hyperbolic $2 m + 2$ -space,i.e., the space form of constant sectional curvature $^ { - 1 }$ $L ^ { 2 }$ -harmonic forms in the middle dimension are conformally invariant,so we can replace hyperbolic space minus one point with $S ^ { 2 m + 1 } \times \mathbf { R } _ { + }$ in a product metric, a situation which has been studied by Atiyah-Patodi-Singer,[1].

Since the Hodge $^ *$ commutes with the Laplacian and $\ast ^ { 2 } = ( - 1 ) ^ { m + 1 }$ ， harmonic forms split into self-dual and anti-self-dual forms $( \ast \alpha = \pm i _ { m } \alpha$ where $i _ { m } = 1$ if $m + 1$ is even, $i _ { m } = i$ if $m + 1$ is odd). The equations for a closed self dual (resp. anti-self-dual) form $\pmb { \alpha }$ on $S ^ { 2 m + 1 } \times \mathbf { R } _ { + }$ can be viewed as an ODE in the $\pmb { y } \in \mathbb { R } _ { + }$ variable. Splitting $\alpha = a \pm i _ { m } ( \ast a ) \wedge d y$ ,it reads

$$
d a = 0 \quad { \mathrm { a n d } } \quad { \frac { \partial } { \partial y } } a = - \pm i _ { m } d * a .
$$

This equation has constant operator coeffcients and explicit solutions in terms of data at $y = 0$ , i.e.,along the boundary, are easily found. This leads to

3.2PROPOSITION .- A closed, self-dual (resp. anti-self-dual) $m + 1 \cdot$ form $\pmb { \alpha }$ on real hyperbolic $2 m + 2$ -space hasa boundary value $B V ( \alpha )$ ，which is a closed $m + 1$ -form on $S ^ { 2 m + 1 }$ ,±-invariant under the operator

$$
F = \mathrm { s i g n } A , \quad A = i _ { m } d * _ { | \mathbf { k } \mathbf { e } \mathbf { r } d } .
$$

The $L ^ { 2 }$ norm translates into a Sobolev norm on the boundary :

$$
\parallel \alpha \parallel _ { 2 } = \parallel | A | ^ { - 1 / 2 } \alpha | _ { \partial } \parallel _ { 2 } .
$$

The ${ \pmb { L } } ^ { 2 }$ norm of harmonic forms is recovered as follows $\left( \mathbf { P } . \ \mathbf { J u l g } \right)$ ： Forms $\pmb { \alpha }$ smooth up to the boundary are dense in $L ^ { 2 }$ solutions of (1). Choose a smooth form $\beta$ such that $d { \boldsymbol { \beta } } = \alpha$ on $S ^ { 2 m + 1 } \times \mathbf { R } _ { + }$ and $d * \beta = 0$ on $S ^ { 2 m + 1 }$ ， then

$$
\begin{array} { l } { \displaystyle \| { \boldsymbol \alpha } \| _ { 2 } ^ { 2 } = \int _ { S ^ { 2 m + 1 } \times { \bf R } _ { + } } \pm i _ { m } { \alpha } \wedge { \boldsymbol \alpha } } \\ { \displaystyle = \int _ { S ^ { 2 m + 1 } } \beta \wedge \pm i _ { m } { \alpha } } \\ { \displaystyle = \int _ { S ^ { 2 m + 1 } } \langle { \boldsymbol \alpha } , \pm i _ { m } ( - 1 ) ^ { m + 1 } \ast { \boldsymbol \beta } \rangle } \\ { \displaystyle = \int _ { S ^ { 2 m + 1 } } \langle { \boldsymbol \alpha } , \pm { \boldsymbol A } ^ { - 1 } { \boldsymbol \alpha } \rangle } \\ { \displaystyle = \int _ { S ^ { 2 m + 1 } } \langle { \boldsymbol \alpha } , \pm i _ { 1 } ^ { 2 } { \boldsymbol \alpha } \rangle } \\ { \displaystyle = \| { \boldsymbol A } \| ^ { - 1 / 2 } \big ( \alpha _ { 1 S ^ { 2 m + 1 } } \big ) \| _ { 2 } ^ { 2 } . } \end{array}
$$

3.3Problem.- Since conformal mappings of $S ^ { 2 m + 1 }$ extend as isometries of real hyperbolic space, we observe that both the operator $\pmb { F }$ and the norm

$$
\| | A | ^ { - 1 / 2 } \alpha \| _ { 2 }
$$

on closed $m + 1$ -forms are Mobius invariants. More generally, since every quasiconformal mapping of $S ^ { 2 m + 1 }$ extends to a quasiisometry of real hyperbolic space,the norm on closed $m + 1$ -forms is quasiinvariant under quasiconformal mappings.To what extent is the operator $\pmb { F }$ invariant under quasiconformal mappings ?

3.4 The case of complex hyperbolic space.- A similar computation can be done in the complex case. Harmonic $m + 1$ -forms split into types and primitive components. Only primitive forms can be in $L ^ { 2 }$ .A conformal change leads to a metric on $S ^ { 2 m + 1 } \times \mathbf { R } _ { + }$ of the form

$$
g _ { | \xi } + y ^ { - 2 } g _ { | \xi ^ { \perp } } + d y ^ { 2 }
$$

where $\pmb { \xi }$ ,the complex tangent to $S ^ { 2 m + 1 }$ in the embedding of $S ^ { 2 m + 1 }$ in $\mathbf { C } ^ { m + 1 }$ ， is the canonical contact structure. The ODE for $\partial$ and $\overline { { \partial } }$ -closed primitive forms does not have constant,nor even commuting coefficients. Splitting forms on $S ^ { 2 m + 1 }$ according to $\xi \oplus \xi ^ { \perp }$ looks hopeless since the splitting is not invariant under the exterior differential. Nevertheless,Rumin's complex precisely extracts the part of $^ d$ that preserves the splitting.

It turns out that the ODE,when rephrased in terms of Rumin's $d _ { R }$ and $^ *$ operators, can be reduced to scalar equations. These equations are singular at $y = 0$ . Still, their $L ^ { 2 }$ solutions are determined by their values at $y = 0$ . One concludes

3.5THEOREM (P.Julg,[9]).- There exists a boundary value operator $B V$ on $L ^ { 2 }$ harmonic $m + 1$ -forms on complex hyperbolic $m + 1$ -space, with values in (non smooth) closed partial $m + 1$ -forms on $S ^ { 2 m + 1 }$ (i.e., elements of $\mathcal { I } m + 1 \cap \ker d _ { \xi } ,$ 9. $\scriptstyle { \mathit { \Pi } } _ { \mathit { \Pi } }$ is an isometry for the norm

$$
\| | A | ^ { - 1 / 2 } \alpha \| _ { 2 }
$$

where $A = i _ { m } d _ { R } * _ { | \ker d _ { \xi } }$

The boundary value operator $B V$ sends the Hodge $i _ { m } *$ to the operator $\ l { F } = \sin \ g { \bf { g } } { \bf { n } } \ l { A }$

The finer splitting of $L ^ { 2 }$ harmonic forms into complex types ${ \pmb { \mathcal { H } } } ^ { p , q }$ seems to translate as follows. Since the contact hyperplane $\pmb { \xi }$ carries a complex structure, Rumin forms of degree $k \geq m + 1$ split into types,

$$
\mathcal { I } ^ { k } = \bigoplus _ { p + q = k - 1 } \mathcal { I } ^ { p , q } .
$$

# Then

$\bullet$ for $\pmb { p }$ ， ${ \pmb q } \ge { \pmb 2 }$ ， $B V ( \mathcal { H } ^ { p , q } )$ consists of closed forms in $\mathcal { J } ^ { p - 1 , q } \oplus \mathcal { J } ^ { p , q - 1 }$ ；   
· $B V ( \mathcal { H } ^ { m + 1 , 0 } )$ (resp. $\Dot { B } V ( \mathcal { H ^ { 0 , m + 1 } } ) )$ consists of closed forms in ${ \mathcal { T } } ^ { m , 0 }$ (resp.in ${ \mathcal { T } } ^ { 0 , m } .$ ； $B V ( \mathcal { H } ^ { m , 1 } )$ (resp. $B V ( { \mathcal { H } } ^ { 1 , m } ) \big )$ isthe $L ^ { 2 }$ -orthogonal complement of $B V ( \mathcal { H } ^ { m + 1 , 0 } )$ (resp.of $B V ( \mathcal { H } ^ { 0 , m + 1 } ) )$ inside closed forms in ${ \mathcal { T } } ^ { m , 0 } \oplus$ $\mathcal { T } ^ { m - 1 , 1 }$ (resp. $\mathcal { T } ^ { 0 , m } + \mathcal { T } ^ { 1 , m - 1 } )$ , unless $m = 1$ ； when $m = 1$ ， $B V ( \mathscr { H } ^ { 1 , 1 } )$ is the orthogonal complement of $B V ( \mathcal { H } ^ { 2 , 0 } ) \oplus$ $B V ( \mathcal { H } ^ { 0 , 2 } )$ in $\mathcal T ^ { 2 } = \mathcal T ^ { 1 , 0 } \oplus \mathcal T ^ { 0 , 1 }$

3.6 The ring of representations of $S U ( m + 1 , 1 ) . -$ The ring $R ( G )$ consists of equivalence classes of formal differences of $G$ -modules with a finite difference of dimension,i.e.,of Fredholm $G$ -modules.

P. Julg and G. Kasparov ([10]) prove that $R ( S U ( m + 1 , 1 ) ) = R ( U ( m +$ 1)).

Theorem 3.5 is a crucial tool in the proof. Indeed,it allows them to construct a representative of an important element $\gamma$ of $R ( S U ( m + 1 , 1 ) )$ as a representation of $S U ( m + 1 , 1 )$ on a module over the algebra of continuous functions on the compactification $\overline { { \boldsymbol { X } } }$ of complex hyperbolic space - forms on $X$ plus Rumin forms on $\partial X$ - which implies that $\gamma = 1$

3.7Poisson transform.- The results 3.2 and 3.5 provide us with a Pois-son transform for closed middle degree forms,whose inverse is given by taking boundary values, in an $L ^ { 2 }$ setting.

More generally，one may naively wonder wether there is a Poisson transform for diferential forms on symmetric spaces $G / K$ with the following properties :

$\bullet$ it is $G$ -equivariant,   
$\bullet$ it commutes with the exterior differential,   
$\bullet$ it coincides with the ordinary Poisson transform for functions,   
$\bullet$ its inverse amounts to take some kind of boundary value,   
$\bullet$ its image consists of all harmonic forms on $G / K$

P.Y. Gaillard has studied in [4] the case of real hyperbolic space, i.e., $G = S O ( n , 1 )$ (see also [8]). The Poisson transform takes forms on the boundary isomorphicly onto coclosed harmonic forms,and commutes with exterior derivative. (There is however an exception $:$ in dimension $2 m + 1$ ， the Poisson transform kills coclosed $_ m$ -forms on the boundary,and thus reaches only closed and coclosed $_ m$ -forms on hyperbolic space). In general, Poisson transforms have boundary values only in degrees strictly less than half the dimension.

It is likely that there is an analogous Poisson transform for differential forms on complex hyperbolic space. Obviously,Rumin differential forms and modified exterior differential should be_used.Also,Poisson transforms are probably automaticly primitive, $\pmb { \partial }$ and $\overline { { \partial } }$ -coclosed.

# 4 ${ \pmb { L } } ^ { p }$ -COHOMOLOGY

The proof of P. Julg's theorem involves several magic identities satisfied by special functions.We present now a direct argument that shows that ${ \pmb L } ^ { 2 }$ -harmonic forms on complex hyperbolic space are representable by partial boundary values. It turns out that the method applies to ${ \pmb L } ^ { p }$ -cohomology as well.

Recall that the ${ \pmb { L } } ^ { p }$ -cohomology $H _ { p } ^ { * } ( X )$ of a Riemannian manifold $\boldsymbol { x }$ is the cohomology of the complex $( \Omega _ { ( p ) } ^ { * } ( X ) , d )$ where $\Omega _ { ( p ) } ^ { * } ( X )$ is the space of differential forms $\pmb { \alpha }$ with $| \alpha | \in \mathbb { L } ^ { p }$ and $| d \alpha | \in L ^ { p }$ . In general, the image

$$
d ( \Omega _ { ( p ) } ^ { k - 1 } ( X ) ) \subset \Omega _ { ( p ) } ^ { k } ( X )
$$

is not closed, and one defines reduced ${ \pmb L } ^ { \pmb { p } }$ -cohomology as the quotient

$$
\overline { { H } } _ { p } ^ { k } ( X ) = \Omega _ { ( p ) } ^ { k } ( X ) / \overline { { d \Omega _ { ( p ) } ^ { k - 1 } ( X ) } }
$$

by the closure of the image of $^ d$

If $H _ { p } ^ { * } ( X ) = \overline { { H } } _ { p } ^ { * } ( X )$ i.e.,iftheimage $d ( \Omega _ { ( p ) } ^ { k - 1 } ( X ) )$ is coed in $\Omega _ { ( p ) } ^ { k } ( X )$ we say that $X$ has only reduced $L ^ { p }$ -coh omology in degree $k$ . This property is invariant under coarse quasiisometries,like those arising from isomorphisms of cocompact isometry groups.

For $\mathscr { p } = 2$ ， there is exactly one $L ^ { 2 }$ -harmonic form in each reduced $L ^ { 2 }$ -cohomology class,i.e., the space of $L ^ { 2 }$ -harmonic forms is isomorphic to $\overline { { H } } _ { 2 } ^ { * } ( X )$

We explain next that on a negatively curved manifold,a closed form in ${ \pmb { L } } ^ { p }$ often admits a boundary value. We start again with the easier case of real hyperbolic space,which has been computed independently by V. Goldshtein, V. Kuz'minov and I. Shvedov,[6].

4.1 ${ \pmb L } ^ { { \pmb p } }$ -cohomology of real hyperbolic space.- One uses the decomposition of real hyperbolic $\pmb { n }$ -space $X$ as a warped product

$$
X = \mathbf { R } _ { + } \times _ { \sinh r } S ^ { n - 1 } .
$$

Split a $\pmb { k }$ -form $\pmb { \alpha }$ as

$$
\alpha = a + b \wedge d r
$$

where $^ { a }$ and $\pmb { b }$ are viewed as functions on $\mathbf { R } _ { + }$ with values in ${ \pmb { L } } ^ { p }$ -differential forms on the sphere $S ^ { n - 1 }$ . The ${ \pmb { L } } ^ { { \pmb { p } } }$ norm of $\pmb { \alpha }$ is roughly the norm of ${ \pmb a }$ in $L ^ { p } ( e ^ { ( n - 1 - k p ) r } { \bar { d } } r )$ plus the norm of $\pmb { b }$ in $L ^ { p } ( e ^ { ( n - 1 - ( k - 1 ) p ) r } d r )$ . The form $\pmb { \alpha }$ is closed iff $\pmb { a }$ is closed and $\begin{array} { r } { \frac { \partial } { \partial r } a = \pm d b } \end{array}$ , which can be written

$$
\frac { \partial } { \partial r } d ^ { - 1 } a = \pm d ^ { - 1 } d b
$$

where $d ^ { - 1 }$ takes exact $k$ -forms to coexact $k - 1$ -forms. Thus $d ^ { - 1 }$ denotes the pseudo-inverse of $d$

If $p < n - 1 / k - 1 , L ^ { p } ( e ^ { ( n - 1 - ( k - 1 ) p ) r } d r ) \subset L ^ { 1 } ( d r )$ s0 $d ^ { - 1 } { \pmb { \alpha } }$ converges in ${ \pmb L } ^ { \pmb { p } }$ as $r \to + \infty$ ,and $^ { a }$ converges to a distribution $a ( \infty ) = B V ( \alpha )$

f $\alpha \in d ( \Omega _ { ( p ) } ^ { k - 1 } )$ ,or if $p \leq n - 1 / k$ ,then $B V ( \alpha ) = 0$

Conversely, if $B V ( \alpha ) = 0$ ,then $\pmb { \alpha }$ admits a primitive $\beta$ in ${ \pmb { L } } ^ { { \pmb { p } } }$ . Indeed, the Poincaré homotopy formula

$$
\beta ( r ) = - \int _ { 0 } ^ { + \infty } b ( r + s ) d s
$$

(no dr component） solves $d { \boldsymbol { \beta } } = \alpha$ and is in ${ \pmb { L } } ^ { p }$ (Hardy inequality） for $p <$ $n - 1 / k - 1$

In conclusion,for real hyperbolic $\pmb { n }$ -space, ${ \pmb L } ^ { \pmb { p } }$ -cohomology in degree $\pmb { k }$ vanishes for $p \leq n - 1 / k$ ,and, for $n - 1 / k < p < n - 1 / k - 1$ ,it is isomorphic to a certain function space of closed $\pmb { k }$ -forms on $S ^ { n - 1 }$ . In particular, it is a Hausdorff Banach space, thus,for such values of $\pmb { p }$ and $k$ ,real hyperbolic space has only reduced cohomology. The $\pmb { L ^ { p } }$ norm can be recovered in terms of boundary values - up to a constant,see [12] for the case when $k = 1$

For $p = n - 1 / k - 1$ ,reduced cohomology vanishes but $L ^ { p }$ -cohomology is huge.

The same argument applies to manifolds with variable curvature. Indeed,what matters is the Lie derivative of the metric on forms under the radial vector ffeld $\frac { \partial } { \partial r }$ . This is controlled by sectional curvature. This leads to the following comparison result (Jens Heber's help was instrumental in obtaining the sharp curvature assumption).

4.2THEOREM [13].- Let $X$ be a complete simply connected Riemannian manifold of dimension $\pmb { n }$ with negatively $\delta$ -pinched sectional curvature, i.e., $- 1 \le K \le \delta < 0$ . For all

$$
p < 1 + \frac { n - k } { k - 1 } \sqrt { - \delta } ,
$$

an ${ \pmb L } ^ { \pmb { p } }$ closed $\pmb { k }$ -form admits a boundary value,which determines its cohomology class. In particular, $\boldsymbol { x }$ has only reduced $L ^ { p }$ -cohomology in degree $k$

4.3 ${ \pmb { L } } ^ { 2 }$ -cohomology of complex hyperbolic plane.- We now check that the $L ^ { 2 }$ -cohomology of complex hyperbolic plane in degree 2 is a limiting case of the above comparison theorem. Indeed, the theorem applies to ${ \pmb { L } } ^ { p }$ closed 2-forms on complex hyperbolic plane, for all $\mathbf { \hat { \boldsymbol { p } } } < \mathbf { \hat { \boldsymbol { 2 } } }$ : there exists a boundary value,which determines the $L ^ { p }$ -cohomology class.

For $\mathbf { \hat { \varepsilon } } ^ { p } \geq \mathbf { 2 }$ ,the boundary value does not exist any more,but a partial boundary operator will replace it,at least when $p < 4$

The complex hyperbolic plane in polar coordinates is not a warped product : the metric on spheres increases at different speeds along the factors of the splitting

$$
T S ^ { 3 } = \xi \oplus \xi ^ { \perp } .
$$

Accordingly,a 2-form has to be split into four components

$$
\alpha = a + a ^ { \prime } d \tau + b \wedge d r + b ^ { \prime } \tau \wedge d r .
$$

The $L ^ { p }$ norm of $\pmb { \alpha }$ in roughly the sum of the norms of $a \in L ^ { p } ( e ^ { ( 4 - 3 p ) r } d r )$ $a ^ { \prime } + b ^ { \prime } \in L ^ { p } \big ( e ^ { ( 4 - 2 p ) r } d r \big )$ ， $b \in L ^ { p } ( e ^ { ( 4 - p ) r } d r )$ For $\pmb { p = 2 }$ , the limiting exponent 0 for $\pmb { b ^ { \prime } }$ prevents one from having an ordinary boundary value as in the preceding paragraph.

If we view the forms $a + d a ^ { \prime } \wedge \tau \in \mathcal { T } ^ { 2 }$ and $b \in \Omega ^ { 1 } / \mathcal { T } ^ { 1 }$ as elements of Rumin's complex,the equation $d \alpha = 0$ implies

$$
d _ { \xi } \big ( a + d a ^ { \prime } \wedge \tau \big ) = 0
$$

and

$$
\frac { \partial } { \partial r } ( a + d a ^ { \prime } \wedge \tau ) = d _ { R } b
$$

which implies that $a + d a ^ { \prime } \wedge \tau$ converges (when $\mathfrak { p } < 4$ ),this is our partial boundary value $B V ( \pmb { \alpha } )$ . It factors through reduced ${ \pmb L } ^ { \pmb { p } }$ -cohomology，and is injective on the reduced cohomology.

It turns out that the complex hyperbolic plane has only reduced cohomology in degree 2. This is a special case of a theorem of A.Borel, [2]. It also follows from estimates on the spectrum of the Laplacian. Indeed, for ${ { \pmb L } ^ { 2 } }$ -functions and 1-forms,the spectrum of the Laplacian is bounded below, [3]. This implies an estimate of the form

$$
\parallel \beta \parallel _ { 2 } ^ { 2 } \leq C \left( \parallel d \beta \parallel _ { 2 } ^ { 2 } + \parallel \delta \beta \parallel _ { 2 } ^ { 2 } \right)
$$

for compactly supported 1-forms $\beta$ ，which therefore implies that the image $d ( \Omega _ { ( 2 ) } ^ { 1 } ( \mathbf { C } H ^ { 2 } ) )$ is closed in $\Omega _ { ( 2 ) } ^ { 2 } ( \mathbf { C } H ^ { 2 } )$ . We conclude that our partial boundary value $B V$ is injective on $L ^ { 2 }$ -cohomology .

This elementary approach cannot give the finer information on complex types contained in theorem 3.5.

# References

[1]M．ATIYAH，V. PATODI, I. SINGER,Spectral assymetry and Riemannian geometry，Math. Proc. Cambridge Philos. Soc. 78, 405-432 (1975).   
[2]A.BOREL,The $L ^ { 2 }$ -cohomology of negatively curved Rieman-nian symmetric spaces，Ann. Acad. Sci. Fennicae 1O,95-105 (1985).   
[3] H.DONNELLY, CH. FEFFERMAN, $L ^ { 2 }$ -cohomology and index theorem for the Bergman metric, Annals of Math. 118,(1983),593- 618.   
[4] P.Y.GAILLARD, Transformation de Poisson de formes différentielles， Comment.Math.Helvetici 61, 581- (1986).   
[5] V. GINzBURG,On closed characteristics of 2-forms, PhD Thesis,Berkeley (1990).   
[6] V. GOL'DSHTEIN, V. KUZ'MINOV,I. SHVEDOV, ${ \pmb L } ^ { { \pmb p } }$ -cohomology of noncompact riemannian manifolds, to appear in Sib. Mat. Zh.   
[7] M. GRoMov, Asymptotic properties of discrete groups, Preprint I.H.E.S. (1992).   
[8] A.JuHL,On the Poisson transformation for differential forms on hyperbolic spaces， Seminar Analysis der K.Weierstrass Institut 1987/88,p. 224-236,Teubner,Leipzig (1988).   
[9] P. JULG, $\kappa$ -theorie des $C ^ { \ast }$ -algebres associees a certains groupes hyperboliques， These d'Etat, Université de Strasbourg (1991).   
[10] P．JULG,G． KASPAROV, $\pmb { L }$ 'anneau ${ \cal K K } _ { G } ( { \bf C } , { \bf C } )$ pour $\boldsymbol { G } =$ $S U ( n , 1 )$ ，to appear in C.R. Acad. Sci. Paris.   
[11] B.HELFFER,J.NoURRIGAT,Hypoelipticité maximale pour des opérateurs polynomes de champs de vecteurs， Progress in Math.58, Bikhauser (1985).   
[12]P.PANsU,Cohomologie $L ^ { p }$ des varietes a courbure négative, cas du degré un， in “P.D.E.and Geometry $1 9 8 8 ^ { \mathfrak { n } }$ ,Rend. Sem. Mat.Torino,Fasc.spez., 95-120 (1989).   
[13] P.PANsU,Cohomologie $L ^ { p }$ et pincement,in preparation.   
[14] M.RuMIn, Un complexe de formes différentielles sur les variétés de contact，C.R. Acad. Sci. Paris 310, 401-404 (1990).   
[15] ZHONG GE, Generalized characteristics for Carnot-Caratheodory metrics, Preprint Univ. Arizona, Tuczon (1991).

# The Maslov class rigidity and non-existence of Lagrangian embeddings

Leonid Polterovich   
Institut des Hautes Etudes Scientifiques 35,route de Chartres   
91440-BURES sur YVETTE (France)\*

October 1990

# 1 Introduction and main results

1． An important question of symplectic topology is the following: given a manifold, does it admit a Lagrangian embedding into $\mathbb { C } ^ { n } ?$ A series of obstructions to existence of such embeddings arises due to pure topological reasons (see M.Audin's paper [1] for a detailed discussion). However in [3] M.Gromov discovered an obstruction of another nature. Using infinite-dimensional analysis he showed that on every embedded Lagrangian submanifold of $\mathbf { C } ^ { n }$ there exists a cycle with positive symplectic area.Thus the first Betti number of a manifold admitting a Lagrangian embedding into $\mathbf { C } ^ { n }$ does not vanish.

Besides the symplectic area there is another remarkable first cohomology class on Lagrangian submanifold of $\mathbf { C } ^ { n }$ - the Maslov class.Recently different restrictions on the Maslov class of Lagrangian embeddings were discovered (see [7],[5],[6]). It is natural to suppose that they also lead to an obstruction to existence of Lagrangian embeddings. In the present paper we construct such obstruction (see theorem 1 below). We use it in order to show that certain flat manifolds do not admit Lagrangian embeddings into $\mathbf { C } ^ { n }$ (see theorems 2,3 below)．Our approach is based on the Maslov class rigidity phenomenon for manifolds of non-positive curvature which was discovered by C. Viterbo (see [7] and section 2.2 below).

I am deeply grateful to I.H.E.S. for hospitality and to B. Bowditch, M. Gromov,M. Kapovich,J.-C. Sikorav and C. Vitero for numerous useful consultations and discussions.

2.We describe our obstruction in the following:

Theorem 1. Let $X$ and $Y$ be closed manifolds of dimension n admitting Riemannian metrics of non-positive sectional curvature. Suppose that there exists a Lagrangian embedding $f : Y \to T ^ { * } X$ such that the following conditions hold:

(c1) the Maslov class of $\pmb { f }$ vanishes; (c2) the composition of $\pmb { f }$ with the natural projection $T ^ { * } X  X$ induce monomorphism $A : H ^ { 1 } ( X ; { \mathbf { Z } } ) \to H ^ { 1 } ( Y ; { \mathbf { Z } } )$ which “expands” in the following sense:

$$
A ( H ^ { 1 } ( X ; \mathbf { Z } ) ) \subset m H ^ { 1 } ( Y ; \mathbf { Z } )
$$

where m is a positive integer such that $m > ( n + 1 ) / 2$ if $X$ is orientable and $m > n + 1$ $X$ is non-orientable.

Then $X$ does not admit a Lagrangian embedding into $\mathbf { C } ^ { n }$

Here the Maslov class $\mu _ { f } \in H ^ { 1 } ( Y , \pmb { \cal { Z } } )$ of a Lagrangian embedding $\pmb { f }$ ： $Y  T ^ { \ast } X$ is defined as follows. If $\gamma : \mathbb { R } / \pmb { \mathrm { \sf { Z } } }  V$ is a loop then the vector bundle $V = ( f \circ \gamma ) ^ { * } T ( T ^ { * } X )$ over $\mathbf { R } / \mathbf { Z }$ with fibers $V ( t ) = T _ { f ( \gamma ( t ) ) } T ^ { \ast } X$ has two Lagrangian subbundles $\Lambda _ { 0 } ( t ) = T _ { f ( \gamma ( t ) ) } ^ { * } X$ and $\Lambda _ { 1 } ( t ) = { \mathrm { r a n g e } } \mathrm { d f } ( \gamma ( t ) )$ . The integer $\smash { \big \langle \mu _ { f } , \gamma \big \rangle }$ is the relative Maslov index of $\Lambda _ { 0 }$ and $\Lambda _ { 1 }$

Theorem 1 is proved in $\ S \ O ^ { 2 }$

3. We will now give an application of Theorem 1. Let ${ \mathsf { T } } ^ { n }$ be a torus with coordinates ${ \mathfrak { x } } _ { 1 } , \ldots , { \mathfrak { x } } _ { n }$ (mod 1).

Consider a map $\alpha : \mathsf { T } ^ { n } \to \mathsf { T } ^ { n }$ , given by

$$
( x _ { 1 } , x _ { 2 } , \ldots , x _ { n - 1 } , x _ { n } ) \mapsto ( x _ { 1 } + 1 / ( 2 n - 2 ) , x _ { 3 } , \ldots , x _ { n } , - x _ { 2 } ) .
$$

Note that $\pmb { \alpha }$ generates a group, say $G$ , of transformations of the torus which is isomorphic to $\mathbf { Z } _ { 2 n - 2 }$ and acts freely. Denote by $K ^ { n }$ the quotient ${ \mathsf { T } } ^ { n } / G$

Theorem 2. If $\pmb { n } \geq \mathbf { 3 }$ then $K ^ { n }$ does not admit a Lagrangian embedding into $\mathbb { C } ^ { n }$ .

Remark 1. The manifold $K ^ { 2 }$ is the Klein bottle. Unfortunately our obstruction does not work in this case.

Remark 2. The manifold $K ^ { 3 }$ is described in the book [8],p.117 (there it is called $\mathcal { G } _ { 4 }$ ). One can check that $K ^ { 3 }$ is orientable. Thus there is no “soft” obstructions to Lagrangian embeddings of $K ^ { 3 }$ into ${ \mathbb C } ^ { 3 }$ (see [1], 4.3.2.). This means that $K ^ { 3 }$ admits a Lagrangian immersion into $\mathbb { C } ^ { 3 }$ as well as a totally real embedding.Moreover $H ^ { 1 } ( K ^ { 3 } , { \pmb { \mathrm { Z } } } ) = { \pmb { \mathrm { Z } } }$ . Thus the symplectic area control does not give an obstruction in this case.

The proof of Theorem 2 and its generalisation for certain fat manifolds one can find in $\ S 3$

# 2 Proof of theorem 1

1. For an element $\mu \in H ^ { 1 } ( W , \mathbf { Z } )$ denote by $\parallel \mu \parallel$ the non-negative integer such that

$$
\mu = \parallel \mu \parallel \cdot ( \mathrm { p r i m i t i v e \ e l e m e n t } ) .
$$

2. The Maslov class rigidity for manifolds of non-positive curvature is established in the following:

Proposition 1. (C. Viterbo, [7]). Let W be an embedded closed Lagrangian submanifold of $\mathbf { C } ^ { n }$ with the Maslov class $\mu$ . Suppose that W admits a Riemannian metric of non-positive sectional curvature. Then the following estimate holds:

$$
1 \leq \parallel \mu \parallel \leq n + 1
$$

Remark 3. Note that the Maslov class of each cycle is even if W is orientable. Thus in the orientable case one can improve the previous estimate: $\| { \boldsymbol { \mu } } \| \geq 2$

3. In this section we prove Theorem 1.We use essentially a construction invented by F.Lalonde and J.-C. Sikorav in [4].

Suppose that the manifold $X$ admits a Lagrangian embedding, say $\pmb { g }$ into $\mathbf { C } ^ { n }$ . Due to Weinstein's theorem one can extend $\pmb { g }$ to a symplectic embedding

$$
\varphi : { \mathcal { U } } \to \mathbb { C } ^ { n }
$$

where $u$ is a tubular neighbourhood of the zero section in $\mathbf { \nabla } T ^ { * } X$ .Let $f ^ { \prime }$ be a composition of $\pmb { f }$ with a suitable homothety along the fibres of $\mathbf { \nabla } T ^ { * } X$ such that $f ^ { \prime } ( Y ) \subset \mathcal { U }$ Denote by $h : Y \to \mathbf { C } ^ { n }$ the composition $\varphi \circ f ^ { \prime }$ . One can easily check that the following relation holds:

$$
\mu _ { h } = \mu _ { f } + A \mu _ { g }
$$

Thus $\mu _ { h } = A \mu _ { g }$ due to condition c1. Recall that due to Proposition 1 and Remark 3 the following inequalities hold: $\parallel \mu _ { g } \parallel \geq 1$ if $X$ is non-orientable and $\Vert { \textbf { \em { \mu } } } \Vert \geq 2$ if $\boldsymbol { x }$ is orientable. Thus $\parallel \mu _ { h } \parallel \ge m \parallel \mu _ { g } \parallel > n + 1$ due to condition $\mathbf { c 2 }$ .We get a contradiction with Proposition 1.□

# 3An obstruction to Lagrangian embeddings of certain flat manifolds

1.Let $W$ be a closed connected fat manifold of dimension $\pmb { \mathscr { n } }$ . Consider the torus ${ \bf T } ^ { n } = { \bf R } ^ { n } / { \bf Z } ^ { n }$ . It is well known (see [8], chapter 3) that $W$ can be represented as a quotient ${ \mathsf { T } } ^ { n } / G$ where $G$ is a finite group with the following properties:

(p1） $G$ acts freely on ${ \mathsf { T } } ^ { n }$ ； (p2）Each element $G \in G$ can be written as a transformation ${ \pmb g } ( { \pmb x } ) =$ $Q { \boldsymbol { x } } + p$ ,where $\pmb { x } \in \pmb { \mathbb { R } } ^ { n }$ , $Q \in { \mathrm { S L } } ( n ; \mathbf { Z } ) , p \in \mathbb { R } ^ { n }$

Denote by $\tau : G \to \mathbf { S L } ( n , \mathbf { Z } )$ the projection ${ \mathfrak { g } } \mapsto Q$

（p3） $\tau ^ { - 1 } \ ( \mathrm { i d } ) { = } \mathrm { i d }$

Denote by $\pmb \theta$ the natural covering $\mathsf { T } ^ { n } \to \bar { W }$ . Using another language one can say that $\pmb \theta$ is the covering corresponding to the maximal normal free abelian subgroup of the fundamental group of $W$

It is easy to check that the induced map $\theta ^ { * } : H ^ { 1 } ( W ; \mathbf { Z } ) \to H ^ { 1 } ( \mathbf { T } ^ { n } ; \mathbf { Z } )$ is a monomorphism (use transfer homomorphism,see chapter 3 written by $\mathbf { E }$ Floyd in [2]). Denote by $m ( W )$ the maximal positive integer such that

$$
\theta ^ { \ast } : H ^ { 1 } ( W , \mathsf { Z } ) \subset m ( W ) \cdot H ^ { 1 } ( \mathsf { T } ^ { n } , \mathsf { Z } ) .
$$

We assume be definition that $m ( W ) = 0$ if $H ^ { 1 } ( w , \pmb { \cal Z } ) = 0$

2. Theorem 3. Let W be a closed connected flat manifold of dimension n. suppose that $m ( W ) > n + 1$ if W is non-orientable and $m ( W ) > ( n + 1 ) / 2$ if W is orientable. Then W does not admit a Lagrangian embedding into $\mathbb { C } ^ { n }$

Theorem 3 follows from Theorem 1 (see \$1)and the following:

Proposition 2. Let W be a closed connected flat manifold. Let $\theta : \mathsf { T } ^ { n } \to$ W be the covering constructed in section 1. Then there exists a Lagrangian embedding $f : \mathsf { T } ^ { n } \to T ^ { * } W$ such that the following conditions hold:

(a) the Maslov class of $f$ vanishes; (b) $\pi \circ f = \theta$ where $\pmb { \pi }$ is the natural projection $T ^ { * } W \to W .$

Proposition 2 is proved in the next section.

3. Denote by $\pmb { \bar { \theta } }$ the induced sympletic covering $T ^ { * } \mathsf { T } ^ { n } \to T ^ { * } \boldsymbol { W } .$ For a translation invariant 1-form $\lambda$ on ${ \mathsf { T } } ^ { n }$ denote by $L _ { \lambda }$ its graph. By definition $L _ { \lambda }$ lies in $T ^ { \star } \mathsf { T } ^ { n }$ . Moreover $\pmb { L } _ { \pmb { \lambda } }$ is Lagrangian since $\lambda$ is closed.

Proposition 3. There exists a translation invariant 1-form $\lambda$ on Tn such that the map ${ \bar { \theta } } : L _ { \lambda } \to T ^ { * } W$ is an embedding.

Proof of Proposition 2. Set $f = \widetilde { \theta } \circ \kappa ^ { - 1 }$ where $\kappa : L ^ { \lambda } \to \mathsf { T } ^ { n }$ is the natural projection and $\lambda$ is chosen according to Proposition 3．Obviously $\pi \circ f = \theta$ .Moreover the Maslov class of $\pmb { f }$ vanishes since $\pmb { f }$ is transversal to fibers of the bundle $T ^ { * } W \to W .$ □

# 4. Proof of Proposition 3

Identify each tangent space to the torus with $\pmb { \mathsf { R } } ^ { n }$ and the set of translation invariant 1-forms on $\mathsf { T } ^ { n }$ with $( \boldsymbol { \mathsf { R } } ^ { n } ) ^ { \star }$ . In fact we have to prove that there exists covector $\pmb { \xi } \in ( \pmb { \mathbb { R } } ^ { n } ) ^ { \ast }$ such that $g ^ { \ast } \xi \neq \xi$ for every $g \in G \backslash \{ { \mathrm { i d } } \}$ . This fact follows immediately from finiteness of $G$ and properties ${ \tt p 2 }$ , p3 of the group $G$ (see Section 1)．□

# 5. Proof of Theorem 2

(1) We claim that $m ( K ^ { n } ) = 2 n - 2$ . Indeed consider the universal covering $\mathbb { R } ^ { n } \to K ^ { n }$ . The group of Deck transformation is generated by $\alpha , t _ { 2 } , \ldots , t _ { n } )$ where

$$
t _ { j } ( x _ { 1 } , \ldots , x _ { j } , \ldots , x _ { n } ) = ( x _ { 1 } , \ldots , x _ { j - 1 } , x _ { j } + 1 , x _ { j } + 1 , x _ { j + 1 } , \ldots , x _ { n } ) .
$$

One can easily check that the following relations hold:

$$
\begin{array} { r c l } { { \alpha ^ { 2 n - 2 } } } & { { = } } & { { t _ { 1 } ; } } \\ { { } } & { { } } & { { t _ { j } \alpha } } \\ { { } } & { { } } & { { t _ { n } \alpha } } \end{array} \nonumber = \alpha t _ { j + 1 } \quad \mathrm { f o r ~ } j = 2 , \ldots , n - 1 ;
$$

Now one can show that $H _ { 1 } ( W , \pmb { \cal Z } ) = \pmb { \cal Z } \oplus \pmb { \cal Z } _ { 2 }$ and find the homomorphism $H _ { 1 } ( \mathbf { T } ^ { n } , \mathbf { Z } ) \to H _ { 1 } ( W , \mathbf { Z } )$ . A direct computation gives us that $m ( K ^ { n } ) = 2 n - 2$ Our claim is proved.

(2) Note that $2 n - 2 > n + 1$ if $\mathbf { \mathfrak { n } } > 3$ . Thus $K ^ { n }$ does not admit a Lagrangian embedding into $\mathbf { C } ^ { n }$ due to Theorem 3.

(3） The last observation is that $K ^ { 3 }$ is orientable and $m ( K ^ { 3 } ) = 4 > ( 3 +$ $1 ) / 2$ . Thus $K ^ { 3 }$ does not admit a Lagrangian embedding into $\mathbf { C } ^ { n }$ due to Theorem 3.□

# References

[1] Audin,M.,Fibres normaux d'immersions en dimension double,points doubles d'immersions Lagrangiennes et plongements totalement réels, Comment,Math.Helv.63(1988),583-623.   
[2] Borel, A., Seminar on transformation groups,Annals of Math. Studies, 46,Princeton University Press,1960.   
[3] Gromov,M.,Pseudo-holomorphic curves in sympletci manifolds, Invent. Math.,82 (1985),307-347.   
[4] Lalonde, F.and Sikorav,J.-C. Sous-varietés Lagrangiennes et Lagrang-iennes exactes des fibres contangentes, Comment. Math. Helv. (to appear).   
[5] Polterovich, L., The Maslov class of Lagrange surfaces and Gromov's pseudoholomorphic curves, Trans.A.M.S. (to appear).   
[6] Polterovich, L., Monotone Lagrange submanifolds of linear spaces and the Maslov class in cotangent bundles,Math. Zeitschrift (to appear).   
[7] Viterbo,C.,A new obstruction to embedding Lagrangian tori, Invent. Math.,100 (1990),301-320.   
[8] Wolf, J., Spaces of constant curvature, McGraw-Hill, Inc.1967.

# Phase Functions and Path Integrals

Joel Robbint and Dietmar Salamon\*   
Mathematics Departmentt   
University of Wisconsin   
Madison,WI 53706 USA   
and   
Mathematics Institute\*   
University of Warwick   
Coventry CV4 7AL Great Britain

March 12, 1993

This note is an introduction to our forthcoming paper [17]. There we show how to construct the metaplectic representation using Feynman path integrals.We were led to this by our attempts to understand Atiyah's explanation of topological quantum field theory in [2].

Like Feynman's original approach in [9] (see also [10]) an action integral plays the role of a phase function. Unlike Feynman, we use paths in phase space rather than configuration space and use the symplectic action integral rather than the (classical) Lagrangian integral. We eventually restrict to (inhomogeneous) quadratic Hamiltonians so that the finite dimensional approximation to the path integral is a Gaussian integral.In evaluating this Gaussian integral the signature of a quadratic form appears. This quadratic form is a discrete approximation to the second variation of the action integral.

For Lagrangians of the form kinetic energy minus potential energy,evaluated on curves in configuaration space, the index of the second variation is well-defined and, via the Morse Index Theorem,1 related to the Maslov Index of the corresponding linear Hamiltonian system. The second variation of the symplectic action has both infnite index and infinite coindex.However, this second variation does have a well-defined signature via the aforementioned discrete approximation.This signature can be expressed in terms of the Maslov index of the corresponding linear Hamiltonian system. This is a symplectic analog of the Morse Index Theorem.

Our treatment is motivated by the formal similarity between Feynman path integrals and the Fourier integral operators of Hormander [13].A key point of Hrmander's theory is that the phase function which appears in the expression for a Fourier integral operator can be replaced by another phase function which defines the same symplectic relation.This is how Feynman path integrals can be evaluated: one replaces the symplectic action by the generating function of the corresponding symplectic relation.

In sections 1 and 2 we review how to use phase functions to construct Lagrangian manifolds and symplectic relations. These generalities are motivated by the examples in section 3 where the phase function is the action integral.

Our topic has a vast literature. Our formula for the metaplectic representation appears in [16] where it is obtained by other arguments. Souriau [26] found an explicit solution for the quantum harmonic oscillator involving the Maslov index (thus correcting Feynman's original formula which is valid only for short times). Keller [14] first noticed the phase shift due to the Maslov index in Theorem 5.2 below and for this reason the Maslov index is sometimes called the Keller-Maslov index. Duistermaat's article [8] explains how to interpret the Morse index in terms of the Maslov index but in the situation studied here the Morse index is undefined.The article [1] explains how Feynman and Dirac [7] were motivated by using the method of stationary phase to obtain classical mechanics as the limit (as $\hbar  0$ ）of quantum mechanics. Daubechies and Klauder [5] (see also [6]) have formulated a theory of path integrals on phase space where the Hamiltonian function can be any polynomial.They remark that the‘time slicing’construction used by Feynman does not generalize. However,our Hamiltonians are at worst quadratic and Feynman's original method is adequate.

# 1 Lagrangian manifolds

A variational family is a pair

$$
\pi : { \cal P }  X , \qquad \phi : { \cal P }  { \bf R }
$$

consisting of a surjective submersion $\pmb { \pi }$ between manifolds $P$ and $X$ ，and a smooth function $\phi$ on $P$ .Each choice of ${ \textbf { \em x } } \in X$ determines a constrained variational problem

We call a critical point of $\phi | \pi ^ { - 1 } ( { \pmb x } )$ a fiber critical point of $\phi$ Denote by ${ \cal C } ( \pi , \phi ) \subset { \cal P }$ the set of all fiber critical points $c \in P$ of $\phi$ At a fiber critical point $c$ the differential $d \phi ( c )$ vanishes on the vertical tangent space