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
