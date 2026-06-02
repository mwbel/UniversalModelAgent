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

# 5 Proof of the Main Result

In this section we prove Theorem 1.2. Let $\Omega \subset \mathbb { C } ^ { n }$ with ${ \overline { { \Omega } } } \subset U _ { \Sigma }$ and assume $e ( \Sigma ) < c ( \Omega )$ .If $\pmb { \Omega }$ is unbounded we have $\varphi _ { \Sigma } ( \Omega ) \cap \Omega \neq \emptyset$ since $\varphi _ { \Sigma } = \mathrm { I d }$ outside of a compact subset $\pmb { K }$ of $\mathbb { C } ^ { n }$ . So we may assume without loss of generality that $\pmb { \Omega }$ is bounded. Arguing indirectly let us assume $\varphi _ { \Sigma } ( \overline { { \Omega } } ) \cap \overline { { \Omega } } = \mathring { \varnothing } . \mathbb { C } ^ { n + 1 } \setminus \Sigma$ has two connected components $C ^ { + }$ and $C ^ { - }$ ， where $C ^ { + }$ is distinguished by the fact that it contains $( \mathbf { 0 } , \ldots , \mathbf { 0 } , - { \pmb { a } } + { \dot { \imath } } )$ for all large ${ \pmb a } \in { \pmb R }$ Fix ${ \pmb \delta } > { \pmb 0 }$ . We find ${ \pmb a } > { \pmb 0 }$ and $c ^ { - } < 0 , c ^ { + } > 0$ and $\Psi \in \mathcal { D }$ such that

$$
\begin{array} { r l } & { \Psi ( { \Sigma } ) \subset ( { \mathbb C } ^ { n } \oplus { \mathbb R } ) \cup ( { \mathbb C } ^ { n } \oplus ( - a , a ) \oplus i ( c _ { - } , c _ { + } ) ) } \\ & { 2 a ( c ^ { + } - c ^ { - } ) < e ( { \Sigma } ) + \delta . } \end{array}
$$

We note that $\Psi ( { \boldsymbol { \Sigma } } )$ has the same holonomy. So we may assume without loss of generality that $\Psi ( { \boldsymbol { \Sigma } } )$ is $\pmb { \Sigma }$ . That is

$$
\begin{array} { r l } & { \Sigma \subset ( { \mathbb C } ^ { n } \oplus { \mathbb R } ) \cup ( { \mathbb C } ^ { n } \oplus ( - a , a ) \oplus i ( c _ { - } , c _ { + } ) ) } \\ & { 2 a ( c ^ { + } - c ^ { - } ) < e ( \Sigma ) + \delta . } \end{array}
$$

We foliate an open neighbourhood in $C ^ { + } \cup \Sigma$ by hyperplanes $\Sigma _ { \epsilon } , 0 \le \epsilon \le \epsilon _ { 0 }$ with $\Sigma _ { 0 } = \Sigma$ and

$$
\Sigma _ { \epsilon } \subset ( { \bf C } ^ { n } \oplus { \bf R } \oplus i \epsilon ) \cup ( { \bf C } ^ { n } \oplus ( - a , a ) \oplus i ( c _ { - } , c _ { + } ) ) ~ .
$$

Here ${ \bf \epsilon } \epsilon _ { 0 } > { \bf 0 }$ is supposed to be sufficiently small. With the obvious identification every $\Sigma _ { \epsilon }$ defines a holonomy

$$
\varphi _ { \epsilon } : U _ { \epsilon } \longrightarrow { \bf c } ^ { n } \ .
$$

If $\epsilon _ { 0 } > 0$ is small enough we have ${ \overline { { \Omega } } } \subset U _ { \epsilon }$ for every $\epsilon \in [ 0 , \epsilon _ { 0 } ]$ and $\varphi _ { \epsilon } ( \overline { { \Omega } } ) \cap \overline { { \Omega } } = \varnothing$ ， since the same is true for $\varphi _ { 0 } = \varphi _ { \Sigma }$ . Pick a $H \in \mathcal { H } _ { a d } ( \Omega )$ with

$$
m ( H ) \geq c ( \Omega ) - \delta \ .
$$

Pick a $\varphi _ { + } \in \theta _ { c ^ { + } }$ with

$$
d ( \varphi _ { + } ) \leq 2 a c _ { + } + \delta \ .
$$

Choose a smooth map $\gamma _ { 1 } : \mathbb { R } \longrightarrow [ 0 , + \infty )$ satisfying (assuming $\epsilon _ { 0 } < c _ { + }$ ）

$$
\begin{array} { r } { \begin{array} { l l l l } { \gamma _ { 1 } ( s ) } & { = } & { 0 } & { \mathrm { ~ f o r ~ } s \le 0 } \\ { \gamma _ { 1 } ^ { \prime } ( s ) } & { > } & { 0 } & { \mathrm { ~ f o r ~ } s \in ( 0 , \epsilon _ { 0 } ) } \\ { \gamma _ { 1 } ( s ) } & { = } & { c _ { 1 } } & { \mathrm { ~ f o r ~ } s \ge \epsilon _ { 0 } } \end{array} } \end{array}
$$

with $\pmb { c _ { 1 } }$ a constant bigger than $2 a ( c _ { + } - c _ { - } + 2 )$ . Next choose a smooth map $\gamma _ { 2 } : \mathbb { R } \longrightarrow [ c _ { 1 } , + \infty )$ satisfying

$$
\begin{array} { l } { { \gamma _ { 2 } \left( s \right) = c _ { 1 } \mathrm { f o r } s \le c _ { + } } } \\ { { \gamma _ { 2 } ^ { \prime } \left( s \right) > 0 \mathrm { f o r } s > c _ { + } } } \end{array}
$$

Now we define a smooth Hamitonian $K : \mathbb { C } ^ { n + 1 } \longrightarrow [ 0 , + \infty )$ by

$$
\begin{array} { l c l } { { K ( z ) } } & { { = } } & { { 0 \ \mathrm { f o r } \ z \in C ^ { - } } } \\ { { K ( z ) } } & { { = } } & { { \gamma _ { 1 } ( \epsilon ) \ \mathrm { f o r } \ z \in \Sigma _ { \epsilon } , 0 \leq \epsilon \leq \epsilon _ { 0 } } } \\ { { K ( z ) } } & { { = } } & { { c _ { 1 } \ \mathrm { f o r } \ z \in C ^ { + } \ \backslash \ \cup \Sigma _ { \epsilon } ) , \ \mathrm { I m } \ z _ { n + 1 } \leq c _ { + } } } \\ { { K ( z ) } } & { { = } } & { { \gamma _ { 2 } ( \mathrm { I m } z _ { n + 1 } ) \ \mathrm { f o r } \ \mathrm { I m } z _ { n + 1 } > c _ { + } \ . } } \end{array}
$$

By construction we have

$$
K ( z ) \geq \varphi _ { + } ( \operatorname { I m } z _ { n + 1 } ) , z \in \mathbb { C } ^ { n + 1 } \ . \nonumber
$$

Finally take a $\varphi _ { - } \in \theta _ { c _ { - } }$ with

$$
\varphi _ { - } ( \mathrm { I m } z _ { n + 1 } ) \geq K ( z ) , z \in \mathbb { C } ^ { n + 1 } \ .
$$

Defining $\varphi : \mathbb { R } \longrightarrow [ 0 , + \infty )$ by

$$
{ \begin{array} { l l l l } { \varphi ( s ) } & { = } & { 0 } & { { \mathrm { f o r ~ } } s \leq 0 } \\ { \varphi ( s ) } & { = } & { \gamma _ { 1 } ( s ) } & { { \mathrm { f o r ~ } } 0 \leq s \leq \epsilon _ { 0 } } \\ { \varphi ( s ) } & { = } & { c _ { 1 } } & { { \mathrm { f o r ~ } } \epsilon _ { 0 } \leq s \leq c _ { + } } \\ { \varphi ( s ) } & { = } & { \gamma _ { 2 } ( s ) } & { { \mathrm { f o r ~ } } s \geq c _ { + } } \end{array} }
$$

we see that $\pmb { K }$ satisfies (27) and (28)of section III with the $\varphi$ defined above for suitable constants $R _ { 1 }$ and $R _ { 2 } > 0$ . We define now a smooth functional $\tilde { \Phi } : E \longrightarrow \mathbb { R }$ by (with $\pmb { \alpha } ( t ) = ( 0 , \ldots , 0 , - \pmb { a } + t \pmb { a } ) )$

$$
\tilde { \Phi } ( z ) = \Phi ( z ) - \int _ { 0 } ^ { 1 } H ( z _ { 1 } , \dots , z _ { n } ) d t - \int _ { 1 } ^ { 2 } K ( z + \alpha ) d t \ ,
$$

and comparison functionals $\Phi _ { + }$ and $\Phi _ { - }$ by

$$
\begin{array} { l c l } { { \Phi _ { + } ( z ) } } & { { = } } & { { \Phi ( z ) - \int _ { 1 } ^ { 2 } \varphi _ { + } ( \mathrm { I m } z _ { n + 1 } ) d t } } \\ { { \Phi _ { - } ( z ) } } & { { = } } & { { \Phi ( z ) - \int _ { 1 } ^ { 2 } \varphi _ { - } ( \mathrm { I m } z _ { n + 1 } ) d t \ . } } \end{array}
$$

The max-min values of $\Phi _ { + }$ and $\Phi$ _ are $d ( \varphi _ { + } )$ and $d ( \varphi _ { - } )$ respectively. In view of Proposition 4.3 these values remain the same if we substract from $\Phi _ { + }$ and $\Phi _ { - }$ the functional $z \longrightarrow \int _ { 2 } ^ { 1 } H ( z _ { 1 } , . . . , z _ { n } ) d t$ for $H \in \mathcal { H } _ { a d } ( \Omega )$ . Next observe that for $z \in E$

$$
\begin{array} { r l } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } \varphi _ { + } \big ( \mathrm { I m } z _ { n + 1 } \big ) d t } \\ { = } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } \varphi _ { + } \big ( \mathrm { I m } \big ( z _ { n + 1 } + ( - a + t a ) \big ) \big ) d t } \\ { \geq } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } K \big ( z ( t ) + \alpha ( t ) \big ) d t } \\ { \geq } & { \int _ { 0 } ^ { 1 } H \big ( z _ { 1 } , \dots , z _ { n } \big ) d t - \int _ { 1 } ^ { 2 } \varphi _ { - } \big ( \mathrm { I m } \big ( z _ { n + 1 } \big ) \big ) d t \ . } \end{array}
$$

As a consequence

$$
d \bigl ( \varphi _ { - } \bigr ) \leq \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } \bigl ( h ( z ) \bigr ) \leq d \mathopen { } \mathclose \bgroup \left( \varphi _ { + } \aftergroup \egroup \right) ~ .
$$

Consequently in view of previous results

$$
2 a c _ { - } \le \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } \left( h ( z ) \right) \le 2 a c _ { + } + \delta \ .
$$

This result is true for any ${ \cal H } \in { \mathcal { H } } _ { a d } ( \Omega )$ . Now let (54) hold and let $\tilde { \Phi } _ { \tau }$ be the functional obtained from $\tilde { \Phi }$ by replacing $H$ by $\pmb { \tau H }$ for $\pmb { \tau } \in [ \mathbf { 0 } , \mathbf { 1 } ]$ . Since

$$
\left| \tilde { \Phi } _ { \tau _ { 1 } } ( z ) - \tilde { \Phi } _ { \tau _ { 2 } } ( z ) \right| \ \leq m ( H ) \left| \tau _ { 1 } - \tau _ { 2 } \right|
$$

we see that

$$
\tilde { d } _ { \tau } : = \operatorname* { s u p } _ { h \in B } \operatorname* { i n f } _ { z \in E ^ { - } } \tilde { \Phi } _ { \tau } ( h ( z ) )
$$

is a continuous,non increasing function of $\tau \in [ 0 , 1 ]$ ,with range in theinterval $[ 2 a c _ { - } , 2 a c _ { + } + \delta ]$ . Since $\tilde { \Phi } _ { \tau }$ satisfies $( W P S ) _ { d }$ for every $\pmb { d } \in \pmb { \mathbb { R } }$ in view of the results in section III we find for every $\tau \in [ 0 , 1 ]$ a critical point $z ^ { \tau }$ of $\tilde { \Phi } _ { \tau }$ Defining $u ( t ) = \alpha ( t ) + z ^ { \tau } ( t )$ we see that $\pmb { u }$ solves

$$
\begin{array} { r c l } { { i \frac { d } { d t } u } } & { { = } } & { { \bigl ( H ^ { \prime } ( u _ { 1 } , \ldots , u _ { n } ) , 0 \bigr ) \ \mathrm { o n } \ [ 0 , 1 ] } } \\ { { i \frac { d } { d t } u } } & { { = } } & { { K ^ { \prime } ( u ) \ \mathrm { o n } \ [ 1 , 2 ] } } \\ { { u _ { k } ( 0 ) } } & { { = } } & { { u _ { k } ( 2 ) \ \mathrm { f o r } \ k = 1 , \ldots , n } } \\ { { \mathrm { R e } u _ { n + 1 } ( 0 ) } } & { { = } } & { { - a \ , \ \mathrm { R e } u _ { n + 1 } ( 2 ) = a \ . } } \end{array}
$$

Assume first for some $t \in [ 1 , 2 ]$ we have $\operatorname { I m } z _ { n + 1 } \geq c _ { + }$ . Then we must have

$$
u ( t ) = ( * , \ldots , * , - a , + 2 a ( t - 1 ) + \tau i )
$$

for $t \in [ 1 , 2 ]$ with $^ *$ being constants. Here $\pmb { \tau }$ satisfies (and is uniquely determined by) $\gamma _ { 2 } ^ { \prime } ( \tau ) = 2 a$ . We calculate using the properties of $\pmb { K }$

$$
\begin{array} { l l l } { { \tilde { \Phi } _ { \tau } ( z ^ { \tau } ) } } & { { \le } } & { { 2 a ( c _ { + } + 1 ) - c _ { 1 } } } \\ { { } } & { { \le } } & { { 2 a ( c _ { + } + 1 ) - 2 a ( c _ { + } - c _ { - } + 2 ) } } \\ { { } } & { { = } } & { { 2 a c _ { - } - 2 a } } \\ { { } } & { { < } } & { { 2 a c _ { - } ~ . } } \end{array}
$$

This contradicts (66) if $\begin{array} { r } { \tilde { \Phi } _ { \tau } \big ( z ^ { \tau } \big ) \equiv \operatorname* { s u p } _ { h \in { \cal B } } \operatorname* { i n f } _ { z \in { \cal E } ^ { - } } \tilde { \Phi } _ { \tau } \big ( h ( z ) \big ) } \end{array}$

Using (68) again we see that $\pmb { u }$ cannot be constant on [1,2]. The possibility left is that $\boldsymbol { u } ( t ) \in \Sigma _ { \epsilon }$ for some $\epsilon \in ( 0 , \epsilon _ { 0 } )$ . We note that

$$
\varphi _ { \epsilon } ( u _ { 1 } ( 1 ) , \dots , u _ { n } ( 1 ) ) = ( u _ { 1 } ( 2 ) , \dots , u _ { n } ( 2 ) ) \ .
$$

By the properties of $H \in \mathcal { H } _ { a d } ( \Omega )$ we see that in case $( u _ { 1 } ( 1 ) , \ldots , u _ { n } ( 1 ) ) \ \in$ $\overline { { \Omega } }$ we must have $( u _ { 1 } ( 0 ) , \ldots , u _ { n } ( 0 ) ) \in { \overline { { \Omega } } }$ implying in view of the boundary condition on $\pmb { u }$ that $\varphi _ { \epsilon } ( u _ { 1 } ( 1 ) , \dots , u _ { n } ( 1 ) ) \in { \overline { { \Omega } } }$ .This,however, contradicts our assumption. So we must have $( u _ { 1 } ( 1 ) , \ldots , u _ { n } ( 1 ) ) \notin \overline { { \Omega } }$ Consequently $\pmb { u }$ is constant on [0,1]. Hence $\pmb { u }$ solves

$$
\begin{array} { r l } & { i \frac { d } { d t } u = K ^ { \prime } ( u ) \mathrm { ~ o n ~ } [ 1 , 2 ] } \\ & { u _ { k } ( 1 ) = u _ { k } ( 2 ) \mathrm { ~ f o r ~ } k = 1 , \dots , n } \\ & { \mathrm { R e } u _ { n + 1 } ( 1 ) = - a , \mathrm { ~ R e } u _ { n + 1 } ( 2 ) = a } \\ & { \left( u _ { 1 } ( 1 ) , \dots , u _ { n } ( 1 ) \right) \notin \overline { { \Omega } } \ . } \end{array}
$$

Hence $z ^ { \tau }$ is a critical point of the smooth fuctional $\hat { \pmb { \Phi } }$ defined by

$$
\hat { \Phi } ( z ) = \Phi ( z ) - \int _ { 1 } ^ { 2 } K ( z ) d t \mathrm { ~ . ~ }
$$

The gradient of $\hat { \Phi }$ at every point is a nonlinear Fredholm operator. Given any critical point $\pmb { z }$ we can construct a finite dimensional manifold $M _ { z } \subset E$ containing all critical points of $\hat { \Phi }$ close to $\pmb { z }$ and the critical points of $\hat { \Phi } \mid M _ { z }$ coincide. Using the Morse-Sard-theorem it follows that the critical levels of $\hat { \Phi }$ are a closed set of measure zero. Denote it by $\boldsymbol { \Gamma }$ . Clearly

$$
\tilde { \Phi } _ { \tau } ( z _ { \tau } ) \in - \tau m ( H ) + \Gamma \ .
$$

Since $\tau \longrightarrow \tilde { d } _ { \tau } = \tilde { \Phi } _ { \tau } ( z ^ { \tau } )$ is continuous and non increasing we find

$$
\tilde { d } _ { \tau } = - \tau m ( H ) + \tilde { d } _ { 0 } \ .
$$

In view of (66)

$$
2 a c _ { - } \leq - \tau m ( H ) + \tilde { d } _ { 0 } \leq 2 a c _ { + } + \delta
$$

for every $\tau \in [ 0 , 1 ]$ . Hence $\tilde { d } _ { 0 } \leq 2 a c _ { + } + \delta$ and $2 a c _ { - } \leq - m ( H ) + \tilde { d } _ { 0 }$ .This implies

$$
m ( H ) \leq 2 a ( c _ { + } - c _ { - } ) + \delta \ .
$$

Since by (54) $m ( H ) \geq { \mathfrak { c } } ( \Omega ) - \delta$ we deduce

$$
\begin{array} { l l l } { { \mathrm { c } ( \Omega ) } } & { { \leq } } & { { 2 a ( \mathrm { c } _ { + } - \mathrm { c } _ { - } ) + \delta + \delta } } \\ { { } } & { { \leq } } & { { e ( \Sigma ) + 3 \delta ~ . } } \end{array}
$$

Since $\delta$ was arbitrarily chosen

$$
{ \sf c } ( \Omega ) \leq e ( \Sigma ) \ .
$$

This， however, contradicts our assumption $e ( \Sigma ) ~ < ~ c ( \Omega )$ .This proves Theorem 1.2. □

# References

[1] Benci, V.and Rabinowitz,P.,Critical point theory for indefinite functionals,Invent.Math.,52,(197)9,241-273.   
[2] Ekeland,I. and Hofer,H., Symplectic topology and Hamiltonian dynamics,Math. Zeit.,200, (1990), 355-378.   
[3] Ekeland,I.and Hofer,H., Symplectic topology and Hamiltonian dynamics II, Math. Zeit.,203,(1990), 553-567.   
[4] Eliashberg，Y.and Hofer，H.，Towards the definition of symplectic boundary, to appear GAFA.   
[5] Hofer,H.,On strongly indefinite functionals with applications,TAMS, 275,(1983) 185-214.   
[6] Hofer,H., Symplectic capacities, in Geometry of low-dimensional manifolds，Vol. 2, edited by S. K. Donaldson and C.B. Thomas, pp.15-34, Cambridge University Press,1990.   
[7] Hofer, H., On the topological properties of symplectic maps, Proceedings of the Royal Society of Edinburgh,115 A, (1990), 25-38.   
[8] Hofer,H.and Zehnder,E.,Periodic solutions on hypersurfaces and a result by C. Viterbo, Inv. Math., 90,(1987),1-7

[9] Hofer,H.and Zehnder,E.,A new capacity for symplectic manifolds,in Analysis et cetera, edited by P.H. Rabinowitz and E. Zehnder,405-428, Academic press,1990.

[10] Sikorav， J.-C.,， Systemes Hamiltoniens et Topologie Symplectique, preprint,Dipartimento di Matematica dell' Universita di Pisa, 1990.

[11] Viterbo, C.， Capacites symplectiques et applications, Astéristique, Séminaire Bourbaki, 695,1989.

[12] Viterbo, C., Symplectic topology as the geometry of generating functions,preprint, January,1991.

# Caustics $D _ { k }$ at points of interface between two media

M. Kazarian

The object of our investigation is singularities of caustics at points of inter-face between two media. When a beam of light passes through the interface, it is refracted according to a well-known law: the ratio of sines of inclination angles of incoming and outgoing beams is equal to the ratio of speeds of propagation of waves in the media (fig.1). The bigger the inclination angle of the incoming beam the bigger the one of the outgoing beam, and for some angle we have an effect of complete reflection: if the inclination angle is larger then the beam is reflected. If the caustic approaches the interface at a point where there is no complete reflection it is only refracted preserving all its singularities.Quite a different situation occurs at points of complete reflection. At this points a caustic arises even if there was no caustic in the first medium (fg. 2). Let us call the caustic new if there was no caustic in the first medium.

Theorem 1. Suppose that the initial wave front and interface are in general position. Then the analytic continuation of the new caustic at a point of complete reflection together with the interface form a singularity which is diffeomorphic to the caustic $D _ { k }$ of the Lagrangian mapping given by the generating family

$$
F ( x , y , z ) = x ^ { 2 } y + y ^ { k - 1 } + q _ { k - 1 } y ^ { k - 2 } + . . . + q _ { 2 } y + q _ { 1 } x
$$

together with the plane $q _ { 1 } = 0$ for some $\pmb { k } \geq \mathbf { 3 }$ (for $\pmb { k } = 3$ it is better to write $A _ { 3 }$ instead of $D _ { 3 }$ ）□

Corollary. In three-dimensional space points of interface where refracted beams touch the interface form a line of complete reflection.

At a generic point of the line of complete reflection analytic continuation of the new caustic together with the interface form a singularity diffeomorphic to the cuspidal edge together with the tangent plane passing through the edge. Physically either one of the branches of the caustic is visible (fig.2a) or the caustic is invisible at all(fig. 2b).

At those points of the line of complete reflection,at which the reflected beam touches the line itself the analytic continuation of the new caustic together with the interface form a singularity diffeomorphic to the caustic

![](images/32c89c8001d25abc946fc1fb22769b209aa7d4b21e4a020b7cc921017582e2b9.jpg)  
Figure 1:

![](images/ac2fbe21573bd05e9a6a049aa3f73d51d819f1724dbbec559075f49d0c0f915c.jpg)  
Figure 2:

![](images/2c7368413bbc945f74a6c6bef4e091037ddb2926cb7a41a1330f141df7fabad4.jpg)  
Figure 3:

![](images/8a048c69bf16ec6260dd5fdf23b2c726a8b1b0d57a33b32d258f6cf7d78ab6f8.jpg)  
Figure 4:

$D _ { 4 }$ together with the tangent plane passing through one of the cuspidal edges (fig. 3a,4a). Physically visible parts of caustics are represented on fig.3b,4b.□

In three-dimensional space one more singularity may occur. Namely, suppose that there is a caustic in the first medium. Its smooth part intersects the interface transversally along some line. Along this line the inclination angle may change and at some points the caustic itself may have complete reflection. In such points the refracted caustic resembles a “symmetric butterfly”, that is a caustic with the generating family

$$
x ^ { 6 } + q _ { 3 } x ^ { 4 } + q _ { 2 } x ^ { 2 } + q _ { 1 } x
$$

(fig. 5, physically visible parts are represented on fig. 5b,c. They resemble correspondent parts of the caustic $D _ { 4 }$ but are not diffeomorphic to them). In [4] such a caustic arises as a stable caustic under the condition of symmetry. In our case a symmetry is not supposed and the differential type of this caustic seems to have an infinite number of moduli. It was noticed by V.M. Zakalyukin that if the interface is flat and the media are uniform then the caustic is really symmetric. Thus we can regard the problem of investigation of caustics at points of an interface as a problem of broken symmetry.

![](images/dde07d4a480d876e8e9bf566d121f10500491ec636f125d3904e30dd94abb871.jpg)  
Figure 5:

In Section 1 we formulate the problem mathematically as a problem for Lagrangian mappings.

In Section 2 we discuss the genericity condition and calculate the normal form for initial data of the propagation of waves in the second medium.

In Section 3 we solve an auxiliary problem of clasification of Lagrangian mappings with given boundary conditions. The results of this classification are used in the proof of Theorem 1.

The author is grateful to V.M. Zakalyukin for stating the problem and constant attention to the work. The author also expresses his thanks to V.I. Arnold for valuable observations.

# 1 Lagrangian manifolds at points of refraction

As we are interested in local questions only, in what follows we mean by manifolds and their submanifolds germs of the corresponding manifolds. We consider a smooth manifold $\pmb { M }$ which is divided into two parts $M _ { 1 }$ and $M _ { 2 }$ by a smooth hypersurface Γ. Two Hamiltonians ${ h _ { i } } : T ^ { * } M _ { i } \to \mathbb { R } , i = 1 , 2$ give rise to a propagation of waves in the media $M _ { i }$ . We assume $h _ { i }$ to be convex on impulses and have smooth continuations over neighbourhoods of $M _ { i }$ in $\pmb { T } ^ { \star } \pmb { M }$ Let $H _ { i } = \{ h _ { i } = 1 \}$ be the level surfaces of the Hamiltonians.

![](images/9409cba00fe574645a655fe03b797845f6a76d61dc9bd3f162e2d73681f86f71.jpg)  
Figure 6:

A disturbance propagates in medium $M _ { 1 }$ along the characteristics of $H _ { 1 }$ . When it comes to the boundary ${ \cal T } _ { \Gamma } ^ { * M }$ it changes by a jump in order to come to the surface $H _ { 2 }$ of the second Hamiltonian. This jump is done along the characteristics of $T _ { \Gamma } ^ { * M }$ which are covectors that are orthogonal to the tangent space $\pmb { T } _ { \ast } \mathbf { T }$ of the interface. Then the disturbance propagates along the characteristics of $H _ { 2 }$

A wave state in $M _ { 1 }$ corresponds to a Lagrangian submanifold $\pmb { L _ { 1 } } ~ \subset$ ${ \pmb T } ^ { * } { \pmb M } _ { 1 }$ . The construction described above gives the following. The boundary $\partial L _ { 1 } = L _ { 1 } \cap T _ { \Gamma } ^ { * } M$ is an isotropic submanifold of $T _ { \Gamma } ^ { * } M$ . The union of all the characteristics of $T _ { \Gamma } ^ { * M }$ passing through $\partial { { \pmb L } _ { 1 } }$ isa Lagrangian submanifold $N$ . Then $N \cap H _ { 2 } = L ^ { \prime }$ is an isotropic submanifold of $H _ { 2 }$ which forms the initial data for the propagation of waves in $M _ { 2 }$ , and the union of all the characteristics of $H _ { 2 }$ passing through $\pmb { L ^ { \prime } }$ is a Lagrangian submanifold $\pmb { L _ { 2 } }$ which corresponds to the wave state in $M _ { 2 }$ (fg. 6).

This construction will perhaps be clearer if we recall the notion of Lagrangian boundary. The manifold of characteristics of ${ \cal T } _ { \Gamma } ^ { * M }$ is naturally identified with ${ \pmb T } ^ { * } { \bf \vec { r } }$ . The projection of the boundary $\partial L = L \cap T _ { \Gamma } ^ { * } M$ of a

Lagrangian submanifold $L \subset T ^ { * } M$ is a Lagrangian submanifold $\bar { \partial } \bar { L } \subset T ^ { \ast } \Gamma$ which is called a Lagrangian boundary of $\pmb { L }$ . Now given the manifold $\pmb { L _ { 1 } }$ ， the manifold ${ \pmb L } _ { 2 }$ is defined uniquely by the following conditions:

(1) $\tilde { \partial } L _ { 1 } = \tilde { \partial } L _ { 2 }$ （ $\mathbf { \tilde { L } _ { 1 } }$ and ${ \pmb L } _ { 2 }$ define the same wave state on the boundary）, $( * )$ (2) $L _ { 2 } \subset H _ { 2 }$ ， and the problem in question is as follows: suppose the manifold $\pmb { L } _ { 1 }$ isin general position. What kind of singularities may have the Lagrangian submanifold $\pmb { L _ { 2 } }$ defined by the conditions $( * )$ as a caustic?

Although these conditions are symmetric with respect to the indices 1 and 2 (if we send the disturbance in inverse direction then $\pmb { L _ { 2 } }$ determines $\pmb { L } _ { 1 }$ according to these conditions） the caustic of $\pmb { L _ { 2 } }$ may not be in general position with respect to $\boldsymbol { \Gamma }$ and even have singularities that are not typical for generic Lagrangian mappings.

# 2Initial data for propogating of waves in the second medium

We use standard notation $q _ { 1 } , \ldots , q _ { n }$ for coordinates on $M$ and $p _ { 1 } , \ldots , p _ { n }$ for impulses. Let $\mathbf { r }$ be given by the equation $q _ { 1 } = 0$

A wave state in the whole space defines a wave state on an interface. From genericity conditions we can suppose that the projection of the boundary $\bar { \partial } \bar { L } _ { 1 } = \bar { \partial } L _ { 2 } \subset T ^ { \ast } \Gamma$ onto $\mathbf { r }$ has singularities which are typical for generic Lagrangian mappings. We will consider two cases:

A. The projection has no singularities,and $\bar { \partial } L _ { 1 }$ is reduced by a Lagrangian equivalence (i.e. a symplectomorphism of ${ \pmb T } ^ { \star } { \bf T }$ preserving the foliation) to the normal form $p _ { 2 } = \ldots = p _ { n } = 0$ B. The projection has a fold as a singularity and $\pmb { L }$ is reduced to the normal form $q _ { 2 } = p _ { 2 } ^ { 2 } , p _ { 3 } = . . . = p _ { n } = 0$

Proposition 2. In three-dimensional space on an interface at a point of complete refection in the case of general position a Lagrangian mapping has no singularity other than A and B above.□

Proof. For a two-dimensional interface possible singularities are foldings along some line and cusps at distinct points. But by a small perturbation of the interface we can obtain that a complete reflection does not occur at a cusp.□

Let us see now to which normal form one can reduce $L ^ { \prime } = \partial L _ { 2 }$ . Consider a projection of $H _ { 2 } \cap T _ { \Gamma } ^ { * } M$ along the characteristics of $T _ { \Gamma } ^ { * M }$ .Let $H ^ { \prime }$ be the set of critical values of this projection. The following lemma follows from the convexity condition.

Lemma $\pmb { \mathscr { s } }$ $H ^ { \prime }$ is a smooth hypersurface of $\mathbf { \vec { \nabla } } T ^ { * } \Gamma$ which has a folding over $\mathbf { r }$ .□

We can call $H ^ { \prime }$ the surface of complete reflection because complete reflections occur just at the points corresponding to $H ^ { \prime } \cap \bar { \partial } L _ { 1 }$

Proposition $\ 4 ( a )$ If there is no complete reflection one can reduce $\mathbf { \nabla } \mathbf { \bar { z } } ^ { \prime }$ by a Lagrangian equivalence of $\mathbf { \delta } _ { T ^ { * } } \mathbf { \delta } _ { M }$ to the form:

$a A : p _ { 1 } = . . . = p _ { n } = q _ { 1 } = 0 ;$ $a B : q _ { 2 } = p _ { 2 } , p _ { 1 } = p _ { 3 } = . . . = p _ { n } = q _ { 1 } = 0 \nonumber$ $( b )$ In the case of complete reflection one can reduce $\pmb { L ^ { \prime } }$ to the form: $b { \cal A } : q _ { 2 } = p _ { 1 } ^ { 2 } , p _ { 2 } = . . . = p _ { n } = q _ { 1 } = 0 ;$ $b B : p _ { 1 } ^ { 2 } = p _ { 2 } + q _ { 3 } , q _ { 2 } = p _ { 2 } ^ { 2 } , p _ { 3 } = . . . = p _ { n } = q _ { 1 } = 0 \nonumber$ □

We represent ${ \cal T } _ { \Gamma } ^ { * } M$ as $T ^ { * } \Gamma \times \pmb { \mathrm { R } }$ with coordinates $p _ { 2 } , \ldots , p _ { n } , q _ { 2 } , \ldots , q _ { n }$ on ${ \pmb T } ^ { \bullet } { \bf I }$ and ${ \pmb p _ { 1 } }$ on $\pmb { \mathrm { R } }$

Lemma 5. The restriction of a Lagrangian equivalence of $\pmb { T } ^ { * } \pmb { M }$ preserving $\boldsymbol { \Gamma }$ to $T _ { \Gamma } ^ { * M }$ can be reduced to the following transformations:

(1) A Lagrangian equivalence of ${ \pmb T } ^ { * } { \bf \vec { r } }$ (at coordinates $p _ { 2 } , . . . , p _ { n } , q _ { 2 } , . . . , q _ { n } \big )$ (2)Transformations of the form

$$
p _ { 1 } \mapsto { \tilde { p } } _ { 1 } = b _ { 1 } ( q _ { 2 } , \dots , q _ { n } ) p _ { 1 } + \sum _ { 2 } ^ { n } b _ { k } ( q _ { 2 } , \dots , q _ { n } ) p _ { k } + \operatorname { c } ( q _ { 2 } , \dots , q _ { n } ) , b _ { 1 } ( 0 ) \neq 0
$$

(i.e. transformations which are linear in $\pmb { p }$ ）.

To prove this lemma one has to express a Lagrangian equivalence of $\pmb { T } ^ { * } \pmb { M }$ as a power series in ${ \pmb q } _ { 1 }$

Proof of Proposition 4. If there is no complete reflection then $\pmb { L ^ { \prime } }$ is projected diffeomorphically onto $\bar { \partial } \bar { L } _ { 1 }$ along_the ${ \pmb p _ { 1 } }$ -axis. Consequently ${ \pmb p _ { 1 } }$ is a function of the point of the point of $\bar { \partial } \bar { L } _ { 1 }$ . If we choose coordinates $q _ { 2 } , \ldots , q _ { n }$ on $\bar { \partial } L _ { 1 }$ in the case $\pmb { a } \pmb { A }$ and coordinates $p _ { 2 } , q _ { 3 } , \ldots , q _ { n }$ in the case $\pmb { a } \pmb { B }$ we get

$$
\begin{array} { r c l } { A : p _ { 1 } } & { = } & { f ( q _ { 2 } , \dots , q _ { n } ) ; } \\ { B : p _ { 1 } } & { = } & { f ( p _ { 2 } , q _ { 3 } , \dots , q _ { n } ) = f _ { 1 } ( p _ { 2 } ^ { 2 } , q _ { 3 } , \dots , q _ { n } ) + p _ { 2 } f _ { 2 } ( p _ { 2 } ^ { 2 } , q _ { 3 } , \dots , q _ { n } ) } \\ & & { = } & { f _ { 1 } ( q _ { 2 } , \dots , q _ { n } ) + p _ { 2 } f _ { 2 } ( q _ { 2 } , \dots , q _ { n } ) . } \end{array}
$$

And we see that $L ^ { \prime }$ is reduced to the required form $p _ { 1 } = 0$ by means of a transformation of the form (2) in Lemma 5.

In the case of complete reflection the projection $\bar { L } ^ { \prime } \to \bar { \partial } \bar { L } _ { 1 }$ is 2-1 mapping. Critical values of this projection form a smooth submanifold $K ^ { e } \bar { \partial } \bar { L } _ { 1 }$ In the case $\pmb { b } \pmb { A }$ one can reduce $\kappa$ to the form $q _ { 2 } = 0$ by means of a diffeomorphism of $\mathbf { \varGamma }$ . Then $L ^ { \prime }$ is given by the equation

$$
b A : ( f _ { 1 } ( q _ { 2 } , \dots , q _ { n } ) p _ { 1 } + f _ { 2 } ( q _ { 2 } , \dots , q _ { n } ) ) ^ { 2 } = q _ { 2 } , f _ { 1 } ( 0 ) \neq 0 ,
$$

which is reduced to the required form $p _ { 1 } ^ { 2 } = q _ { 2 }$ by means of transformations of the form (2) in Lemma 5.

In the case $b B$ we have on $\bar { \partial } \bar { L } _ { 1 }$ a surface $\kappa$ of critical points of the projection onto $\mathbf { \varGamma }$ (the inverse image of the caustic) $p _ { 2 } = 0$ and a field of kernels of this projection $\partial / \partial \rho _ { 2 }$ .Suppose that at a generic point of $\kappa$ this surface is transversal to this field. In this case $\kappa$ can be reduced by means of a diffeomorphism of $\mathbf { r }$ to the form $p _ { 2 } + q _ { 3 } = 0$ . Hence $\pmb { L }$ is given by the equation

$$
b B : ( p _ { 1 } + f _ { 1 } ( p _ { 2 } , q _ { 3 } , \ldots , q _ { n } ) ) ^ { 2 } = ( p _ { 2 } + q _ { 3 } ) f _ { 2 } ( p _ { 2 } , q _ { 3 } , \ldots , q _ { n } ) , \quad f _ { 2 } ( 0 ) \neq 0 .
$$

The right-hand side is reduced by a transformation of the form (1) in Lemma 5 to the form $p _ { 2 } + q _ { 3 }$ ,and the left hand side is reduced to the form $p _ { 1 } ^ { 2 }$ by a transformation of the form (2) in Lemma 5 and we get the equation for $L ^ { \prime }$ in the required form $p _ { 1 } ^ { 2 } = p _ { 2 } + q _ { 3 }$

# 3 Lagrangian mappings with fixed boundary conditions

Proposition 4 leads us to the following auxiliary problem of the classification of Lagrangian mappings with fixed boundary conditions. Consider a diagram:

$$
\begin{array} { l c l } { { L ^ { \prime } \hookrightarrow } } & { { T _ { \Gamma } ^ { * } M } } & { { \to } } & { { \Gamma } } \\ { { \ \cap } } & { { \ \cap } } & { { \ \cap } } \\ { { \ L \hookrightarrow } } & { { T ^ { * } M } } & { { \to } } & { { M , } } \end{array}
$$

where $\Gamma , M , L ^ { \prime }$ are fixed smooth manifolds, $\mathbf { r }$ being given by the equation $q _ { 1 } = 0 , L ^ { \prime }$ being taken from Proposition 4 and $\pmb { L }$ being a Lagrangian submanifold containing $\pmb { L ^ { \prime } }$ as a submanifold.

Theorem ${ \pmb 6 }$ A generic Lagrangian submanifold $\pmb { L }$ in the class of Lagrangian submanifolds containing $L ^ { \prime }$ may be reduced by means of a Lagrangian equivalence of $\pmb { T } ^ { * } \pmb { M }$ preserving $\mathbf { r }$ to a form with one of the following generating families (the equation for $\mathbf { r }$ is $\pmb q _ { 1 } = 0$ ：

$a A : B _ { k } : F ( x , q ) = x ^ { k + 1 } + q _ { k } x ^ { k } + . . . + q _ { 2 } x ^ { 2 } + q _ { 1 } x ;$ ${ \pmb a } { \pmb B } : { \bf A }$ generic such germ can be reduced to the form

$$
F ( x , y , q ) = x ^ { 3 } + y ^ { 2 } + q _ { 2 } x + q _ { 1 } y ;
$$

A set of such germs of codimension 1 can be reduced to the form

$$
F ( x , y , q ) = x ^ { 3 } + x y ^ { 2 } + q _ { 3 } y ^ { 2 } + q _ { 2 } x + q _ { 1 } y .
$$

All the other germs have higher codimension;

$$
b A : D _ { k } : F ( x , q ) = x ^ { 2 } y + y ^ { k - 1 } + q _ { k - 1 } y ^ { k - 2 } + . . . + q _ { 2 } y + q _ { 1 } x .
$$

# Proof.aA Because

$$
T _ { 0 } L \subset ( T _ { 0 } L ^ { \prime } ) ^ { \bot } = \operatorname { S p a n } \langle \partial / \partial p _ { 1 } , \partial / \partial q _ { 1 } , \ldots , \partial / \partial q _ { n } \rangle ,
$$

we can choose either $( q _ { 1 } , \ldots , q _ { n } )$ or $\left( p _ { 1 } , q _ { 2 } , \ldots , q _ { n } \right)$ as coordinates on $\pmb { L }$ In the first case there is no singularity of the projection of $\pmb { L }$ onto $\pmb { M }$ ,and $\pmb { L }$ can be brought to the normal form $p _ { 1 } = . . . = p _ { n } = 0$ 、In the second case there exists a generating function $S ( p _ { 1 } , q _ { 2 } , \ldots , q _ { n } )$ such that $\pmb { L }$ is given by the equations

$$
q _ { 1 } = - \frac { \partial S } { \partial p _ { 1 } } , \quad p _ { 2 } = \frac { \partial S } { \partial q _ { 2 } } , \quad \ldots , \quad p _ { n } = \frac { \partial S } { \partial q _ { n } } .
$$

The condition $L ^ { \prime } \subset L$ gives rise to the following: all the partial derivatives of $s$ are known at the hypersurface ${ \mathfrak { p } } _ { 1 } = 0$ of the space of parameters (namely, they are equal to zero). This implies that $s$ is of the form

$$
S = p _ { 1 } ^ { 2 } \cdot \varphi ( p _ { 1 } , q _ { 2 } , \ldots , q _ { n } ) ,
$$

where $\varphi$ is a germ of some function. Hence $\pmb { L }$ is given by the generating family

$$
F ( x , q ) = S ( x , q _ { 2 } , \ldots , q _ { n } ) + x q _ { 1 } = x ^ { 2 } \varphi ( x , q _ { 2 } , \ldots , q _ { n } ) + x q _ { 1 } .
$$

Consequently for a generic $\varphi$ the function $f ( x ) = F ( x , 0 )$ is of the type $\pmb { A } _ { k }$ for some $\pmb { k }$ ，and $\pmb { F }$ is a versal deformation of $\pmb { f }$ ，which is $\mathbf { R } _ { + }$ -equivalent to the family

$$
F ( x , q ) = x ^ { k + 1 } + q _ { k - 1 } x ^ { k - 1 } + \ldots + q _ { 2 } x ^ { 2 } + q _ { 1 } x .
$$

Because we can only make transformations of the $\pmb q$ variables preserving $q _ { 1 } = 0$ , indeed we may only reduce the family to the form

$$
F ( x , q ) = x ^ { k + 1 } + q _ { k } x ^ { k } + \dots + q _ { 2 } x ^ { 2 } + q _ { 1 } x .
$$

Analogous calculations in the cases $\pmb { a } \pmb { B }$ and $\pmb { b } \pmb { A }$ show that the generating family may be chosen in the form

$$
\begin{array} { r } { a B : F ( x , y , q ) = x ^ { 3 } + x q _ { 2 } + y q _ { 1 } + y ^ { 2 } \varphi ( x , y , q _ { 3 } , \dots , q _ { n } ) ; } \\ { b A : F ( x , y , q ) = x ^ { 2 } y + x q _ { 2 } + y q _ { 1 } + y ^ { 2 } \varphi ( x , y , q _ { 3 } , \dots , q _ { n } ) . } \end{array}
$$

Standard classification theorems of critical point theory show that these families are versal deformations of the corresponding functions and $\pmb { \mathrm { R } } _ { + }$ equivalent to the families given in the theorem. Moreover,a reduction to the normal form may be made by means of changes of the variables $\pmb q$ preserving $q _ { 1 } = 0$ .□

The case $b B$ which is not considered in Theorem 6 is much more complicated. In this case (and in the more general cases) the generating family is not a versal deformation. Calculations show that the generating family in this case is of the form

$$
\begin{array} { r } { F ( x , q ) = \frac { 1 } { 6 } x ^ { 6 } + \frac { 1 } { 4 } x ^ { 4 } q _ { 3 } + \frac { 1 } { 2 } x ^ { 2 } q _ { 2 } + ( x ^ { 4 } + q _ { 3 } x ^ { 2 } + q _ { 2 } ) ^ { 2 } \varphi ( x , q _ { 2 } , \dots , q _ { n } ) + x q _ { 1 } . } \end{array}
$$

We are interested in the problem,to which form this family may be brought by means of $\mathbf { R } _ { + }$ -transformations. Even if we are not interested in the Lagrangian sub-manifold itself but only in its caustic,the problem is to which simplest form a germ of the family

$$
\frac { \partial F } { \partial x } = ( x ^ { 4 } + x ^ { 2 } q _ { 3 } + q _ { 2 } ) [ x + ( 8 x ^ { 3 } + 4 q _ { 3 } x ) \varphi + ( x ^ { 4 } + q _ { 3 } x ^ { 2 } + q _ { 2 } ) \varphi ^ { \prime } ] + q _ { 1 }
$$

may be brought by means of a $V$ -equivalence.

If we could bring this family to the same form with $\varphi = 0$ , we would have obtained a “symmetric butterfly” (fg.5,see [4]) but we cannot guarantee this.

Proof of Theorem 1. According to condition $( * )$ the manifold $L _ { 2 }$ is known to be contained in the level surface $H _ { 2 }$ of the Hamiltonian $h _ { 2 }$ .We can obtain any small perturbation of ${ \bf { { L } } } _ { 2 }$ by means of a corresponding perturbation of $H _ { 2 }$ . So we may assume ${ \pmb L } _ { 2 }$ to be in general position and make use of Theorem 6. However, the condition of convexity of the Hamiltonian implies a prohibition of some singularities from Theorem 6. Namely, if there is no complete intersection then the characteristics of $H _ { 2 }$ are transversal to the boundary $T _ { \Gamma } ^ { * } M$ .This means that ${ \pmb L } _ { 2 }$ is transversal to $T _ { \Gamma } ^ { * M }$ as well. From the list of Theorem 6 this condition is satisfied only by the simplest singularities: $F = x ^ { 2 } + x q _ { 1 }$ (the caustic is absent） in the case $\pmb { a } \pmb { A }$ and $F = x ^ { 3 } + y ^ { 2 } + q _ { 2 } x + q _ { 1 } y$ (the caustic is smooth and transversal to the boundary） in the case $\pmb { a } \pmb { B }$ ，

At the points of complete reflection $\mathbf { { { L } _ { 2 } } }$ may not be (and indeed is not) transversal to the boundary,and of all the singularities described in Theorem 6,only the case $\pmb { B } \pmb { a }$ may occur,which completes the proof.□

# References

[1] Arnold V.I., Critical points of functions and classifcation of functics, Uspechi math. nauk, v.29,1974,2,11-49 (in Russian).   
[2] Arnold V.I, Gusein-Zade, S.M. and Varchenko,A.N., Singularities of differentiable maps,I,Birkhauses,Boston,1985.   
[3] Janeczko,S.and Kowalczyk,A., Classification of generic 3-dimentional Lagrangian singularities with $( Z _ { 2 } ) ^ { 1 }$ -symmetries, preprint (1988).

[4] Janeczko, S.and Roberts,R.M., Classification of symmetric caustics I: Symplectic equivalence,in “Singularity theory and Applications,Warwick 1989,Part II" edited by R.M. Robert and I.N. Stewart, LNM1463, Springer-Verlag,Heidelberg,Berlin,1991,pp.193-219.

[5] Nye, J.F.,The catastrophe optics of liquid drop lenses, Proc. R. Soc. London A403 (1986),27-50.

[6] Zakalyukin, V.M., On Lagrangian and Legendrean singularities, Funct. anal.i pril.,1976,10,1,26-36.

# Examples of Singular Reduction

Eugene Lerman Richard Montgomery Reyer Sjamaar

Mathematisch Instituut der Rijksuniversiteit te Utrecht \* PO Box 80.010,3508 TA Utrecht,The Netherlands

January 1991

# Introduction

The construction of the reduced space for a symplectic manifold with symmetry,as formalized by Marsden and Weinstein [13],has proved to be very useful in many areas of mathematics ranging from classical mechanics to algebraic geometry. In the ideal situation, which requires the value of the moment map to be weakly regular,the reduced space is again a symplectic manifold.A lot of work has been done in the last ten years in the hope of finding a ‘correct' reduction procedure in the case of singular values. For example, Arms, Gotay and Jennings describe several approaches to reduction in [4]. At some point it has also been observed by workers in the field that in all examples the level set of a moment map modulo the appropriate group action is a union of symplectic manifolds.Recently Otto has proved that something similar does indeed hold,namely that such a quotient is a union of symplectic orbifolds [16]. Independently two of us,R. Sjamaar and E. Lerman,have proved a stronger result [21]. We proved that in the case of proper actions the reduced space, which we simply took to be the level set modulo the action, is a stratifed symplectic space. Thereby we obtained a global description of the possible dynamics,a procedure for lifting the dynamics to the original space and a local characterization of the singularities of the reduced space. (The precise definitions will be given below.） The goal of this paper is twofold. First of all, we would like to present a number of examples that illustrate the general theory. Secondly, in computing the examples we have noticed that many familiar methods for computing reduced spaces work nicely in the singular situations. For instance,in the case of a lifted action on a cotangent bundle the reduced space at the zero level is the‘cotangent bundle' of the orbit space.And in some cases the reduced space can be identified with the closure of a coadjoint orbit.

# 1 A Simple Example

Consider the standard action of the circle group $S O ( 2 )$ on $\scriptstyle \mathbf { R } ^ { 2 }$ ，and lift this action to $T ^ { * } \mathbf { R } ^ { 2 } \simeq \mathbf { R } ^ { 2 } \times \mathbf { R } ^ { 2 }$ . In coordinates,

$$
\left( \begin{array} { c } { { q ^ { 1 } } } \\ { { q ^ { 2 } } } \\ { { p _ { 1 } } } \\ { { p _ { 2 } } } \end{array} \right) \mapsto \left( \frac { { \cos \theta \ - \sin \theta } } { \sin \theta } \ \frac { 0 } { \cos \theta } \right) \left( \begin{array} { c } { { 0 } } \\ { { q ^ { 2 } } } \\ { { 0 } } \end{array} \right) ,
$$

and the canonical symplectic form is $\omega = d q ^ { 1 } \wedge d p _ { 1 } + d q ^ { 2 } \wedge d p _ { 2 }$ . The corresponding momentum map $J$ is the angular momentum $J ( q , p ) = q ^ { 1 } p _ { 2 } - q ^ { 2 } p _ { 1 }$ Zero is a singular value of $J$ . Let us compute the reduced space at zero, $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ ,which we will take to be the quotient $J ^ { - 1 } ( 0 ) / S O ( 2 )$ . The zero level set $J ^ { - 1 } ( 0 )$ is a union of a point, O,and of a hypersurface

$$
Z = \{ q ^ { 1 } p _ { 2 } - q ^ { 2 } p _ { 1 } = 0 : ( q ^ { 1 } , q ^ { 2 } , p _ { 1 } , p _ { 2 } ) \not = 0 \} .
$$

The hypersurface is a $S O ( 2 )$ -invariant coisotropic submanifold of $T ^ { * } \mathbf { R } ^ { 2 }$ . The group $S O ( 2 )$ acts freely on $z$ and the null directions of the restriction of the symplectic form $\omega$ to $z$ are precisely the orbital directions (just as in the regular case). Consequently the quotient $C _ { 1 } = Z / S O ( 2 )$ is a symplectic manifold.The other piece of the zero level set,the origin O,is fixed by the action of $S O ( 2 )$ and we may consider the quotient $C _ { 0 } = \{ 0 \} / S O ( 2 )$ as a zero-dimensional symplectic manifold. Thus the reduced space $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ is a disjoint union of two symplectic manifolds,

$$
( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } = C _ { 0 } \coprod C _ { 1 } .
$$

Let us give a more concrete description of the reduced space. We claim that $C _ { 1 }$ is $\mathbb { R } ^ { 2 } \backslash \{ 0 \}$ with the standard symplectic structure and that the reduced space as a whole is diffeomorphic to the orbifold $\scriptstyle \mathbf { R } ^ { 2 } / \mathbf { Z } _ { 2 }$ ,where the action of $\mathbf { Z _ { 2 } }$ is generated by the reflection $( x ^ { 1 } , x ^ { 2 } )  ( - x ^ { 1 } , - x ^ { 2 } )$ ·

# 1.1 Digression: Smooth Structures on Reduced Spaces

Let us explain what is meant by $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ being diffeomorphic to $\mathbf { R ^ { 2 } } / \mathbf { Z _ { 2 } }$ .In general, let $( M , \omega )$ be a Hamiltonian $\pmb { G }$ -space with corresponding moment map ${ \mathfrak { P } } : M \to { \mathfrak { g } } ^ { * }$ and let us assume that $\pmb { G }$ acts properly on $M$ . (In all the examples that follow the group $\pmb { G }$ is going to be compact and for compact groups the properness of the action is automatic.） For us the reduced space at zero, $M _ { 0 }$ ,is the topological space formed by dividing the zero level set $\Phi ^ { - 1 } ( 0 )$ by the group action,i.e.,

$$
M _ { 0 } = \Phi ^ { - 1 } ( 0 ) / G .
$$

(We will see later that $M _ { 0 }$ has a lot of structure,not just a topology.）As we have just seen, $\Phi ^ { - 1 } ( 0 )$ need not be a manifold and the action of $\pmb { G }$ on the zero level set need not be free. Thus there is no reason for the reduced space so defined to be a manifold (or even an orbifold). However,as Arms et al. have observed [3],it makes sense to single out a certain subset of the set of continous functions on $M _ { 0 }$ as follows.Call a function $\pmb { f } : M _ { 0 }  \mathbf { R }$ smooth if there exists a smooth $\pmb { G }$ -invariant function $\bar { f }$ on $M$ whose restriction to the zero level set $\Phi ^ { - 1 } ( 0 )$ equals the pullback of $f$ to $\Phi ^ { - 1 } ( 0 )$ by the orbit map $\pi : \Phi ^ { - 1 } ( 0 ) \to \Phi ^ { - 1 } ( 0 ) / G = M _ { 0 }$ ,i.e.,

$$
\bar { f } | _ { \Phi ^ { - 1 } ( 0 ) } = \pi ^ { * } f .
$$

Let us denote the set of smooth functions by $C ^ { \infty } ( M _ { 0 } )$ . A map $F : M _ { 0 } \to N$ ， where $N$ is a manifold (or an orbifold,or another reduced space),is smooth if for any function $\phi \in C ^ { \infty } ( N )$ the pullback $F ^ { \ast } \phi$ is a smooth function on $M _ { 0 }$ ， $\phi \circ F \in C ^ { \infty } ( M _ { 0 } )$ . It is now clear what we mean by two singular spaces being diffeomorphic.

1.1.REMARK.If $\pmb { G }$ is a discrete group acting symplectically on a manifold $( M , \omega )$ ,it makes sense to define the corresponding moment map to be the zero map,since the Lie algebra of $\pmb { G }$ is trivial. The reduced space is then a symplectic orbifold $M / G$ .(See [18] or [15] for the definition of an orbifold.）For example,the action of $\mathbf { Z _ { 2 } }$ on $\scriptstyle \mathbf { R } ^ { 2 }$ described above preserves the standard symplectic form $d x ^ { 1 } \wedge d x ^ { 2 }$ and the reduced space is the symplectic orbifold $\mathbf { R } ^ { 2 } / \mathbf { Z } _ { 2 }$ with ring of smooth functions isomorphic to the collection of the smooth even functions on $\scriptstyle \mathbf { R } ^ { 2 }$ .

# 1.2 The Reduced Space $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ as an Orbifold

Let us now go back to our example. Consider the 2-plane

$$
\begin{array} { r } { \Lambda = \{ ( q ^ { 1 } , q ^ { 2 } , p _ { 1 } , p _ { 2 } ) \in T ^ { * } \mathbf { R } ^ { 2 } : q ^ { 2 } = 0 , p _ { 2 } = 0 \} . } \end{array}
$$

This plane is symplectic,it is completely contained in the zero level set of the moment map $J$ and the $S O ( 2 )$ -orbit of any point $( q , p ) \in J ^ { - 1 } ( 0 )$ intersects $\Lambda$ in exactly two points.Indeed,a point $( \pmb { q } , \pmb { p } )$ lies in the zero level set if and only if $\pmb q$ and $\pmb { p }$ are collinear as vectors in $\scriptstyle \mathbf { R } ^ { 2 }$ . Consequently, $J ^ { - 1 } ( 0 ) / S O ( 2 )$ is homeomorphic to $\Lambda / \mathbf { Z _ { 2 } }$

What about the two smooth structures? Clearly any $S O ( 2 )$ -invariant function on $T ^ { * } \mathbf { R } ^ { 2 }$ restricts to a $\mathbf { Z _ { 2 } }$ -invariant function on $\Lambda$ .So the map $\Lambda / \mathbf { Z } _ { 2 } \to J ^ { - 1 } ( 0 ) / S O ( 2 )$ is smooth. To show that this map is a diffeomorphism it suffices to prove that any (smooth) $\mathbf { Z _ { 2 } }$ -invariant function on $\Lambda$ extends to a (smooth) $S O ( 2 )$ -invariant function on $T ^ { * } \mathbf { R } ^ { 2 }$ .By Schwarz's theorem [20] any smooth $\mathbf { Z _ { 2 } }$ -invariant function on $\Lambda$ is a smooth function of the invariants $( q ^ { 1 } ) ^ { 2 }$ ， ${ { p } _ { 1 } } ^ { 2 }$ and ${ \pmb q } ^ { 1 } p _ { 1 }$ (these functions are a set of generators of the $\mathbf { Z _ { 2 } }$ -invariant polynomials on $\Lambda$ ).Now $( q ^ { 1 } ) ^ { 2 }$ is the restriction to $\Lambda$ of the $S O ( 2 )$ -invariant $( q ^ { 1 } ) ^ { 2 } + ( q ^ { 2 } ) ^ { 2 }$ . Similarly,

$$
\begin{array} { r c l } { {  p _ { 1 }  ^ { 2 } } } & { { = } } & { {  ( p _ { 1 }  ^ { 2 } +  p _ { 2 }  ^ { 2 } ) | _ { \Lambda } } } \\ { { q ^ { 1 } p _ { 1 } } } & { { = } } & { {  ( q ^ { 1 } p _ { 1 } + q ^ { 2 } p _ { 2 } ) | _ { \Lambda } . } } \end{array}
$$

Consequently the map $J ^ { - 1 } ( 0 ) / S O ( 2 )  \Lambda / \mathbf { Z } _ { 2 }$ is smooth as well and, therefore,the two reduced spaces are diffeomorphic.

Note that the $\mathbf { Z _ { 2 } }$ -invariant functions on $\Lambda$ form a Poisson subalgebra of $C ^ { \infty } ( \Lambda )$ . So the smooth functions on the reduced space $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ form a Poisson algebra.This is an example of the fact proved by Arms et al. (loc.cit.) that the set of smooth functions on a reduced space $M _ { 0 }$ has a well-defined Poisson bracket induced by the bracket on the original manifold $M$

The Poisson bracket of $C ^ { \infty } ( ( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } )$ is compatible with the symplectic structure of the pieces $C _ { 1 }$ and $C _ { 0 }$ of the reduced space (see (1)) in the following sense.A pair of functions $\pmb { f }$ and $\pmb { g }$ in $C ^ { \infty } ( ( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } )$ restrict to a pair of smooth functions on the symplectic manifold $C _ { 1 }$ . The symplectic structure of $C _ { 1 }$ defines a Poisson bracket $\{ \cdot , \cdot \} _ { c _ { 1 } }$ . It is easy to check that this new bracket coincides with the bracket induced by the Poisson structure on $C ^ { \infty } ( ( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } )$ ， i.e.,

$$
\{ f \vert _ { C _ { 1 } } , g \vert _ { C _ { 1 } } \} _ { C _ { 1 } } = \{ f , g \} _ { ( T ^ { * } { \bf R } ^ { 2 } ) _ { 0 } } \Big \vert _ { C _ { 1 } } .
$$

Similarly,one can show that

$$
\left\{ f , g \right\} _ { ( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } } \Big | _ { C _ { 0 } } = 0 ,
$$

which is consistent with viewing $C _ { 0 }$ as a zero-dimensional symplectic manifold.We thus see that the Poisson bracket of $C ^ { \infty } ( ( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } )$ and the decomposition (1） of the reduced space into symplectic manifolds are intimately related.

# 1.3 Reduction via Invariants

Let us present a different calculation of the reduced space $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 }$ . The calculation uses invariant theory,an approach advocated by $\mathbf { R }$ .Cushman.We will realize the reduced space as a subspace of $\mathbb { R } ^ { 4 }$ cut out by the equations

$$
\left\{ \begin{array} { r c l } { { x _ { 1 } } ^ { 2 } } & { = } & { { x _ { 2 } } ^ { 2 } + { x _ { 3 } } ^ { 2 } } \\ { { x _ { 4 } } } & { = } & { 0 } \\ { { x _ { 1 } } } & { \geq } & { 0 } \end{array} \right.
$$

In words,this reduced space is diffeomorphic to the top half,with vertex included,of the standard cone in $\mathbb { R } ^ { 3 }$ . Consider a change of variables

$$
\left\{ \begin{array} { r c l } { { u _ { 1 } } } & { { = } } & { { { \frac { 1 } { 2 } } ( q ^ { 2 } - p _ { 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { u _ { 2 } } } & { { = } } & { { { \frac { 1 } { 2 } } ( q ^ { 1 } - p _ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { u _ { 3 } } } & { { = } } & { { { \frac { 1 } { 2 } } ( q ^ { 1 } + p _ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { u _ { 4 } } } & { { = } } & { { { \frac { 1 } { 2 } } ( q ^ { 2 } + p _ { 1 } ) } } \end{array} \right.
$$

and set

$$
\left\{ \begin{array} { r c l } { { z _ { 1 } } } & { { = } } & { { u _ { 1 } + i v _ { 1 } } } \\ { { z _ { 2 } } } & { { = } } & { { u _ { 2 } + i v _ { 2 } . } } \end{array} \right.
$$

We have thus identified $T ^ { * } \mathbf { R } ^ { 2 }$ with $\mathbf { C } ^ { 2 }$ .In these complex coordinates the symplectic form is given by $\omega = i \left( d z _ { 1 } \wedge d \bar { z } _ { 1 } + d z _ { 2 } \wedge d \bar { z } _ { 2 } \right)$ ,the action of the circle group $S O ( 2 ) \simeq U ( 1 )$ by

$$
e ^ { i \theta } \cdot ( z _ { 1 } , z _ { 2 } ) = ( e ^ { - i \theta } z _ { 1 } , e ^ { i \theta } z _ { 2 } )
$$

and the moment map by $J ( z _ { 1 } , z _ { 2 } ) = | z _ { 2 } | ^ { 2 } - | z _ { 1 } | ^ { 2 }$ . It is easy to see that the set of (real) invariant polynomials is generated by four polynomials:

$$
\begin{array} { r c l } { { \sigma _ { 1 } } } & { { = } } & { { | z _ { 2 } | ^ { 2 } + | z _ { 1 } | ^ { 2 } , } } \\ { { } } & { { } } & { { } } \\ { { \sigma _ { 2 } } } & { { = } } & { { z _ { 1 } z _ { 2 } + \overline { { { z _ { 1 } z _ { 2 } } } } , } } \\ { { } } & { { } } & { { } } \\ { { \sigma _ { 3 } } } & { { = } } & { { i ( z _ { 1 } z _ { 2 } - \overline { { { z _ { 1 } z _ { 2 } } } } ) , } } \\ { { } } & { { } } & { { } } \\ { { \sigma _ { 4 } } } & { { = } } & { { | z _ { 2 } | ^ { 2 } - | z _ { 1 } | ^ { 2 } . } } \end{array}
$$

The map $\sigma = ( \sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 } , \sigma _ { 4 } ) : \mathbf { C } ^ { 2 }  \mathbf { R } ^ { 4 }$ pushes down to an injective map $\bar { \sigma } : \mathbf { C } ^ { 2 } / S O ( 2 )  \mathbf { R } ^ { 4 }$ . The invariants satisfy the relations

$$
\left\{ \begin{array} { r c l l } { { \sigma _ { 1 } ^ { 2 } - \sigma _ { 4 } ^ { 2 } } } & { { = } } & { { \sigma _ { 2 } ^ { 2 } + \sigma _ { 3 } ^ { 2 } } } \\ { { \sigma _ { 1 } } } & { { \geq } } & { { 0 . } } \end{array} \right.
$$

Consequently the image of $\bar { \pmb { \sigma } }$ is a subset of $\mathbb { R } ^ { 4 }$ cut out by the equations

$$
\left\{ { \begin{array} { r c l } { { { x _ { 1 } } ^ { 2 } } } & { { = } } & { { { x _ { 2 } } ^ { 2 } + { x _ { 3 } } ^ { 2 } } } \\ { { { x _ { 1 } } } } & { { \geq } } & { { 0 } } \end{array} } \right.
$$

Therefore the reduced space $( T ^ { * } \mathbf { R } ^ { 2 } ) _ { 0 } : = \{ \sigma _ { 4 } = 0 \} / S O ( 2 )$ embeds in $\mathbb { R } ^ { 4 }$ as the subset cut out by (2) as claimed.If we ignore the fourth coordinate,we see that the reduced space is simply a round cone in $\mathbf { R } ^ { 3 }$ . Since the invariants

$\sigma _ { 1 } , \ldots , \sigma _ { 4 }$ are quadratic, their linear span in $C ^ { \infty } ( \mathbf { C } ^ { 2 } )$ forms a four-dimensional Lie algebra under the standard Poisson bracket.Alternatively,it is enough to note that

$$
\begin{array} { l l l } { { \{ \sigma _ { i } , \sigma _ { 4 } \} } } & { { = } } & { { 0 } } & { { \mathrm { f o r ~ } i = 1 , \ldots , 4 } } \\ { { \{ \sigma _ { 1 } , \sigma _ { 2 } \} } } & { { = } } & { { 2 \sigma _ { 3 } } } \\ { { \{ \sigma _ { 1 } , \sigma _ { 3 } \} } } & { { = } } & { { - 2 \sigma _ { 2 } } } \\ { { \{ \sigma _ { 2 } , \sigma _ { 3 } \} } } & { { = } } & { { 2 \sigma _ { 1 } . } } \end{array}
$$

Therefore, the correspondence

$$
\sigma _ { 4 }  { ( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} ) } \qquad \sigma _ { 1 }  { ( \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} ) }
$$

$$
\sigma _ { 2 }  ( \begin{array} { r r } { { - 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} ) \qquad \sigma _ { 3 }  ( \begin{array} { r r } { { 0 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} )
$$

establishes an isomorphism between the Lie algebra spanned by the generators of the invariants and ${ \mathfrak { g l } } ( 2 , \mathbf { R } )$ .The image cut out by (2) is nothing more than half of the nilpotent cone, the closure of the connected component of the principal nilpotent orbit in ${ \mathfrak { g l } } ( 2 , \mathbf { R } )$

More intrinsically this can be seen as follows. The moment map for the action of $S p ( T ^ { * } \mathbf { R } ^ { 2 } , \omega ) \simeq S p ( 2 , \mathbf { R } )$ on $T ^ { * } \mathbf { R ^ { 2 } } \simeq \mathbf { R ^ { 4 } }$ identifies ${ \mathfrak { s p } } ( 2 , \mathbf { R } )$ with the Poisson algebra of quadratic polynomials. The polynomials that commute with ${ \pmb { \sigma _ { 4 } } }$ then get identified with $\mathfrak { u } ( 1 , 1 )$ ，which is isomorphic to ${ \mathfrak { g l } } ( 2 , \mathbf { R } )$ . We will come back to this point in Section 5,Remark 5.4.

# 2A Summary of the General Theory

The goal of this section is to introduce the notion of a stratified symplectic space,to explain how this notion arises naturally in reduction and to describe some properties of reduced spaces.

# 2.1 Stratifications

The main idea of a stratification is that of a partition of a nice topological space into a disjoint union of manifolds. Thus a manifold is trivially a stratified space. A more interesting example of a stratified space is that of a cone on a manifold: given a manifold $M$ the open cone $\mathring { C } M$ on $M$ is the product $M \times [ 0 , \infty )$ modulo the relation $( { \pmb x } , { \pmb 0 } ) \sim ( { \pmb y } , { \pmb 0 } )$ for all $\textstyle { \mathfrak { x } } , { \mathfrak { y } } \in M$ . That is, ${ \mathring { C } } M$ is $M \times [ 0 , \infty )$ with the boundary collapsed to a point,the vertex $^ *$ of the cone. The cone ${ \mathring { C } } M$ is a disjoint union of two manifolds: $M \times ( 0 , \infty )$ and the vertex $^ *$ . Similarly one can consider the cone $\mathring { C } ( \mathring { C } M )$ on the cone $\mathring { C } M$ ，

$$
\mathring { C } ( \mathring { C } M ) = \left( \mathring { C } M \times [ 0 , \infty ) \right) \big / \sim .
$$

The space $\mathring { C } ( \mathring { C } M )$ is a union of three manifolds:

the vertex $^ *$ of $\mathring { C } ( \mathring { C } M )$ ；   
the open half line $\{ * \} \times ( 0 , \infty )$ through the vertex of $\mathring { C } M$ ； the manifold $( M \times ( 0 , \infty ) ) \times ( 0 , \infty )$

In general we will see that locally a stratified space is a cone on a cone on a cone .... Let us now make this precise.

2.1. DEFINITION. A decomposed space is a Hausdorff paracompact topological space $\boldsymbol { x }$ equipped with a locally finite partition $\textstyle X = \operatorname { U } _ { i \in \tau } S _ { i }$ into locally closed subsets $S _ { i }$ called pieces,each of which is a manifold.

We shall only consider decompositions each of whose pieces has the structure of a smooth manifold. A given space may be decomposed in a number of different ways.

2.2.ExAMPLE.Consider the subset of $\scriptstyle \mathbf { R } ^ { 2 }$

$$
Y = \{ ( { \boldsymbol { x } } ^ { 1 } , { \boldsymbol { x } } ^ { 2 } ) \in \mathbf { R } ^ { 2 } : { \boldsymbol { x } } ^ { 2 } = 0 \} \cup \{ ( { \boldsymbol { x } } ^ { 1 } , { \boldsymbol { x } } ^ { 2 } ) \in \mathbf { R } ^ { 2 } : { \boldsymbol { x } } ^ { 1 } \geq 0 , { \boldsymbol { x } } ^ { 2 } \geq 0 \} .
$$

The space $\boldsymbol { Y }$ can be broken up into a union of manifolds as

$$
Y = \{ x ^ { 2 } = 0 \} \cup \{ x ^ { 1 } > 0 , x ^ { 2 } > 0 \} \cup \{ x ^ { 1 } = 0 , x ^ { 2 } > 0 \}
$$

or as

$$
\begin{array} { l l l } { { Y } } & { { = } } & { { \{ x ^ { 1 } > 0 , x ^ { 2 } > 0 \} \cup \{ x ^ { 1 } = 0 , x ^ { 2 } > 0 \} \cup \{ ( 0 , 0 ) \} } } \\ { { } } & { { } } & { { \cup \{ x ^ { 1 } < 0 , x ^ { 2 } = 0 \} \cup \{ x ^ { 1 } > 0 , x ^ { 2 } = 0 \} . } } \end{array}
$$

2.3.ExAMPLE. A triangulated space is a decomposed space, if we declare the strata to be the (combinatorial) interiors of the simplexes.

2.4.EXAMPLE.If $X = \operatorname { L I } _ { i \in \tau } S _ { i }$ is a decomposed space, the cone $\mathring { C } X$ has a natural decomposition

$$
\mathring { C } X = \{ * \} \cup \coprod _ { i \in \mathcal { T } } S _ { i } \times ( 0 , \infty ) .
$$

2.5.ExAMPLE. The product of two decomposed spaces $X = \mathbb { U } S _ { i }$ and $Y =$ $\coprod P _ { j }$ is a decomposed space

$$
X \times Y = \coprod _ { i , j } S _ { i } \times P _ { j } .
$$

Define the dimension of a decomposed space $\boldsymbol { x }$ to be dim $X = \operatorname* { s u p } _ { i \in \tau } \dim S _ { i }$ We shall only consider finite-dimensional spaces.A stratification is a particular kind of decomposition. Its definition is recursive on the dimension of a decomposed space.

2.6.DEFINITION (cf. [7]). A decomposed space $X = \{ S _ { i } \} _ { i \in \tau }$ is called a stratified space if the pieces of $X$ , called strata,satisfy the following local condition:

Given a point $\pmb { x }$ in a piece $\boldsymbol { S }$ there exist an open neighbourhood $\boldsymbol { U }$ of $\pmb { x }$ in $X$ ， an open ball $B$ around $\pmb { x }$ in $\boldsymbol { S }$ ,a compact stratified space $L$ ,called the link of $\pmb { x }$ ,and a homeomorphism $\varphi : { \dot { B } } \times { \mathring { C } } { \dot { L } } \to U$ that preserves the decomposition, i.e.,maps pieces onto pieces.

2.7.REMARK. We say that a decomposed space $X$ satisfies the condition of the frontier if the closure of each piece is a union of connected components of pieces of $\boldsymbol { x }$ . It follows easily from Definition 2.6 that stratified spaces satisfy the condition of the frontier.

2.8.ExAMPLE.The decomposition (5) satisfies the frontier condition while (4) does not. So decomposition (4) is not a stratification.We leave it to the reader to check that decomposition (5) is a stratification.

2.9.ExAMPLE.A triangulated space is stratified by the interiors of its simplexes. The proof is an elementary exercise in PL-topology.

We are now in a position to define a stratified symplectic space.

2.10.DEFINITION.A stratifed symplectic space is a stratified space $X$ together with a distinguished subalgebra $C ^ { \infty } ( X )$ (a smooth structure) of the algebra of continuous functions on $\boldsymbol { x }$ such that:

(i) each stratum $s$ is a symplectic manifold;   
(ii) $C ^ { \infty } ( X )$ is a Poisson algebra;   
(iii） the embeddings $S \hookrightarrow X$ are Poisson.

Condition (iii) means that given two functions $f , g \in C ^ { \infty } ( X )$ their restrictions, $f | _ { S }$ and $\pmb { g } | _ { \mathcal { S } }$ ，to a stratum $\boldsymbol { S }$ are smooth functions on $s$ and their Poisson bracket at the points of $\boldsymbol { S }$ coincides with the Poisson brackets of the restrictions defined by the symplectic structure on $S \colon \{ f , g \} \big | _ { S } = \{ f | s , g | s \} s$

2.11.THEOREM (cf.[21]). Let $( M , \omega )$ be a Hamiltonian $\pmb { G }$ -space with moment map $J : M \to { \mathfrak { g } } ^ { * }$ and suppose that the action of the Lie group $\pmb { G }$ is proper.Then given an orbit $\mathcal { O } \in { \mathfrak { g } } ^ { * }$ the reduced space $M _ { \mathcal { O } } : = J ^ { - 1 } ( \mathcal { O } ) / G$ is a stratified symplectic space.