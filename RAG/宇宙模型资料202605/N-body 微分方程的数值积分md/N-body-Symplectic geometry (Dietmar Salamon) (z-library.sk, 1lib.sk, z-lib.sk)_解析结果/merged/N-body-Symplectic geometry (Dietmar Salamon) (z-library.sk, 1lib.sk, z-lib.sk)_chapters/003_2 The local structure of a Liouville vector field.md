# 2 The local structure of a Liouville vector field

A smooth vector feld of a symplectic manifold $( P , \Omega )$ is called Liouville if its flow $\varphi _ { t }$ satisfies $\varphi _ { t } ^ { * } \Omega = e ^ { t } \Omega$ (or equivalently when $\mathcal { L } _ { \xi } \Omega = \Omega$ ,where $\pmb { \mathcal { L } }$ denotes the Lie derivative).

Assume that a Liouville vector field $\pmb { \xi }$ of a ${ \bf 2 } n$ -dimensional manifold $( P , \Omega )$ vanishes on a $\pmb { k }$ -dimensional isotropic submanifold $Q$ of $P$ and that at every point $\pmb q$ of $Q \xi ( q ) = 0$ and the eigenvalues of its 1-jet are 1, $1 / 2$ and 0. This means that in some coordinates

$$
J _ { q } ^ { 1 } ( \xi ) = \sum _ { i = 1 } ^ { k } ( 0 x _ { i } \frac { \partial } { \partial x _ { i } } + 1 y _ { i } \frac { \partial } { \partial y _ { i } } ) + \sum _ { r = k + 1 } ^ { n } ( \frac { 1 } { 2 } x _ { r } \frac { \partial } { \partial x _ { r } } + \frac { 1 } { 2 } y _ { r } \frac { \partial } { \partial y _ { r } } )
$$

where

$$
T _ { q } Q = \{ \cap _ { j = k + 1 } ^ { n } K e r d x _ { j } \} \cap \{ \cap _ { j = 1 } ^ { n } K e r d y _ { j } \} .
$$

The general linearization theorem would imply that the Liouville vector field $\pmb { \xi }$ is $C ^ { 0 }$ -conjugate to a linear map. But a smoother conjugacy is required in order to push forward the symplectic form. To prove that $\pmb { \xi }$ is smoothly conjugate to its linear part,we use a linearization theorem due to $\mathbf { G . S e l l }$ [12],which extends the linearization theorem of Sternberg [13] to the case of a vector field with resonant eigenvalues.We exploit the fact that the vector $\pmb { \xi }$ is Liouville, together with the explicit algorithm that Sel's theorem provides to compute a lower bound for the order of smoothness of the conjugacy.

Resonance: A collection of non-zero eigenvalues is resonant if one of them is an integral linear combination（with nonnegative coefficients whose sum is at least two ）of the others.i.e. Let $\lambda _ { 1 } , . . . , \lambda _ { N }$ be a set of non-zero eigenvalues repeated with multiplicities and let $\boldsymbol { m } = ( m _ { 1 } , . . . , m _ { N } )$ be nonnegative integers.Define $\left| m \right| = \sum m _ { i }$ and $\begin{array} { r } { \gamma ( \lambda _ { i } , m ) = \lambda _ { i } - \sum m _ { r } \lambda _ { r } } \end{array}$ .Then if a relation $\gamma ( \lambda _ { i } , m ) = 0$ holds for $| m | \geq 2$ the eigenvalues are said to be in resonance, and $| m |$ is called the order of resonance. Thus the eigenvalues of our Liouville vector field ${ \pmb \xi }$ are resonant of order 2.

If $( z ^ { 1 } , . . . , z ^ { N } )$ are coordinates with respect to the basis $\left( e _ { 1 } , . . . , e _ { N } \right)$ ,let $z ^ { m }$ stand for $z _ { 1 } ^ { m _ { 1 } } . . . z _ { N } ^ { m _ { N } }$ . The vector valued monomial $z ^ { m } \theta _ { i }$ is resonant if $\gamma ( \lambda _ { i } , m ) = 0$ and $| m | \geq 2$

Statement of Sel's theorem: Assume we have the equation $\dot { w } = A ( q ) w +$ $F ( w , q )$ where $A ( q )$ is a matrix and $F ( 0 , q ) = 0$ . When $\pmb { A }$ is hyperbolic, let $\Sigma ^ { + } ( A )$ denote those eigenvalues $\lambda$ of $A$ with $R e \lambda > 0$ and $\Sigma ^ { - } ( A )$ those with $R e \lambda < 0$ .If $\Sigma ^ { i } ( A ) \neq \emptyset$ where $i = + \infty -$ ,the spectral spread is defined to be

$$
\rho ^ { i } = \frac { m a x \{ | R e \lambda | \ : \ \lambda \in \Sigma ^ { i } ( A ) \} } { m i n \{ | R e \lambda | \ : \ \lambda \in \Sigma ^ { i } ( A ) \} } .
$$

The r-smoothness of $\pmb { A }$ is the largest integer $K \geq 0$ such that

$$
\begin{array} { r l } { 1 . \ r - K \rho ^ { - } \ge 0 , \mathrm { i f } \ \Sigma ^ { + } ( A ) = \emptyset } & { } \\ { 2 . \ r - K \rho ^ { + } \ge 0 , \mathrm { i f } \ \Sigma ^ { - } ( A ) = \emptyset } & { } \end{array}
$$

3. There exist positive numbers $M , N$ with $r = M + N \mathrm { ~ , ~ } M - K \rho ^ { + } \geq 0 ,$ $N - K \rho ^ { - } \ge 0$ if $\Sigma ^ { + } ( A ) \neq \emptyset$ and $\Sigma ^ { - } ( A ) \neq \emptyset$

Now suppose that the following condition holds for some integer $r \geq 2$ This is condition ${ } ^ { \mathfrak { n } } \mathbf { B } ^ { \mathfrak { n } }$ in [12]).

$D ^ { j } F ( q _ { 0 } , q ) = 0$ for $0 \leq j \leq r - 1$ and $R e \gamma ( \lambda , m ) \neq 0$ for all $\begin{array} { r } { \lambda \in \sum A ( q ) = \sum ^ { + } A ( q ) \cup \sum ^ { - } A ( q ) } \end{array}$ for all $\pmb { m }$ with $| m | = r$ and for all $\pmb q \in \hat { V }$ neighborhood of ${ \pmb q } _ { \ r _ { 0 } }$

Then Sells Theorem asserts that there is a $C ^ { \kappa }$ smooth linearizing conjugation $w = z + \Phi ( z , q )$ between $\dot { w } = A ( \pmb \theta ) w + F ( w , \pmb \theta )$ and $\dot { z } = A ( q ) z$ ，where $\Phi$ varies smoothly in terms of the parameter $\pmb q$ and is of class $C ^ { \kappa }$ in $\pmb { z }$ ,where $\pmb { K }$ is the r-smoothness of $A ( q _ { 0 } )$

In the case of the Liouville vector field $\pmb { \xi }$ we have $R e \gamma ( \lambda , m ) = 0$ for some pair $( \lambda , m )$ with $| m | = 2$ . Hence Sell's theorem must be applied with $\mathbf { \eta } _ { r } \geq \mathbf { 3 }$ Therefore one has to find coordinates in which $\pmb { \xi }$ has no quadratic terms. The first step is to construct a Darboux chart near each point in $Q$ which is adapted to ${ \pmb \xi }$

Construction of an adapted Darboux chart: Because the Liouville vector field ${ \pmb \xi }$ vanishes on the isotropic submanifold $\overline { { Q } }$ of $( P , \Omega )$ ， $Q$ is an invariant manifold of the field $\pmb { \xi }$ which consist of fixed points. Since at any point $\pmb q$ in $Q$ , the tangent space to $P$ at $\pmb q$ can be written as $\qquad T _ { \boldsymbol { q } } P = T _ { \boldsymbol { q } } Q \oplus N _ { \boldsymbol { q } } ,$ where $N _ { q } = ( T _ { q } Q ) ^ { \perp _ { G } }$ and the nonzero eigenvalues of ${ \pmb \xi }$ at a singular point $q \in Q$ are assumed to be 1 or $1 / 2$ we have that $m ( D \varphi _ { \tau } | _ { N _ { q } ^ { u } } ) = e ^ { 1 / 2 }$ and $\| D \varphi _ { \tau } | _ { T _ { q } Q } \| = e ^ { 0 }$

Where $m ( L ) = i n f \{ \| L v \| : \| v \| = 1 \}$ is the minimum norm of the linear map $L$ and $\| L \| = s u p \{ \| L v \| : \| v \| = 1 \}$ is the norm of $L$

It follows that $Q$ is $\pmb { r }$ -normally hyperbolic for all $\pmb { r } \in \mathbb { N }$ and all $q \in Q$ Therefore we can apply the Center Manifold Theorem ([7], [5]),which states that under these conditions

i) $P$ is smoothly foliated by strong unstable $\varphi _ { t }$ -invariant submanifolds $W _ { g }$ which are transverse to $Q$ ,i.e. $P = \cup _ { q \in Q } W _ { q }$

ii) each $W _ { \mathfrak { g } }$ is a $C ^ { \pm }$ -manifold and the map $\pi : P \to Q$ given by $\pi ( W _ { \mathfrak { q } } ) = \mathfrak { q }$ is $C ^ { r }$ . Points of $W _ { g }$ are characterized by the fact that the distance from $\varphi _ { t } ( \pmb { p } )$ to $\varphi _ { t } ( q )$ goes to zero exponentially fast as $\pmb { t }$ goes to $- \infty$

Let us denote by $W$ the foliation of $P$ by the strong unstable manifolds $W _ { \mathfrak { g } }$ ，where $W _ { \mathfrak { g } }$ is the leaf through a point $\pmb q$ in $Q$ . Since $W$ is a coisotropic foliation $( T W ) ^ { \perp }$ considered as a subbundle of $\pmb { T W }$ is integrable. (See [14] p.11).Consequently $T W ^ { \perp }$ is the tangent bundle to an isotropic foliation of $W$ , which we denote by $W ^ { \perp }$ . Now let $\pmb q$ be a point in the isotropic submanifold $Q$ ，and let $U$ be a neighborhood of $\pmb q$ in $P$ sufficiently small so that the foliations of $\boldsymbol { U }$ defined by $W ^ { \perp }$ and $W$ are simple, i.e. the set of the leaves of the foliation are smooth manifolds and the corresponding projections

$$
\Phi : U \longrightarrow \frac { P \cap U } { W ^ { \bot } \cap U } = B _ { W ^ { \bot } }
$$

and

$$
\Psi : U \longrightarrow \frac { P \cap U } { W \cap U } = B _ { W }
$$

are submersions.Then there is a unique Poisson structure on $B _ { W ^ { \bot } }$ such that $\Phi$ is a Poisson morphism,whose rank at $\Phi ( { \pmb x } )$ is equal to the rank of the 2-form $\Omega | _ { W }$ induced by $\pmb { \Omega }$ on the leaf $W _ { \pmb { x } }$ through $\pmb { x }$ ，which equals $2 n - 2 k$ ， and there is a unique Poisson structure on $B _ { W }$ such that $\Psi$ is a Poisson morphism,whose rank at $\Psi ( { \pmb x } )$ equals the rank of $\Omega | _ { W _ { \Vec { x } } ^ { \bot } }$ ，which equals zero since $W _ { \pmb { x } } ^ { \pmb { \bot } }$ is isotropic. (See [6]).

We use these unique Poisson structures on $B _ { W ^ { \bot } }$ and $B _ { W }$ to construct Darboux coordinates adapted to the leaves of the foliations $W$ and $W ^ { \perp }$ . More precisely, we construct coordinates $( U ; x _ { 1 } , . . . , x _ { n } , y _ { 1 } , . . . , y _ { n } )$ near a point $\pmb q$ in $Q$ such that

$$
\bullet Q \cap U = \{ y _ { i } = 0 \} _ { i = 1 } ^ { k } \cap \{ x _ { r } = 0 \} _ { r = k + 1 } ^ { n } \cap \{ y _ { r } = 0 \} _ { r = k + 1 } ^ { n } \ : ,
$$

· the leaf through a point $\pmb q$ in $Q \cap U$ is given by

$$
{ \it W } _ { q } \cap { \it U } = \{ p \in { \it U } : x _ { i } ( p ) = x _ { i } ( q ) i = 1 , . . . , k \} ,
$$

and

$$
\bullet \ \Omega = \sum _ { i = 1 } ^ { k } d x _ { i } \wedge d y _ { i } + \sum _ { r = k + 1 } ^ { n } 2 d x _ { r } \wedge d y _ { r } .
$$

value In these coordinates the eigenspace for $\lambda = 1 / 2$ is exactly thesacesand by $L ( \xi )$ corresponding to the eigen- $\{ \frac { \partial } { \partial x _ { r } } , \frac { \partial } { \partial y _ { r } } \} _ { r = k + 1 } ^ { n }$ and the eigenspace corresponding to the eigenvalue is exactly the space spanned by $\big \{ \frac { \partial } { \partial y _ { i } } \big \}$ . i.e. the linear part of ${ \pmb \xi }$ is

$$
L ( \xi ) = \sum _ { i = 1 } ^ { k } y _ { i } \frac { \partial } { \partial y _ { i } } + \sum _ { r = k + 1 } ^ { n } ( \frac { 1 } { 2 } x _ { r } \frac { \partial } { \partial x _ { r } } + \frac { 1 } { 2 } y _ { r } \frac { \partial } { \partial y _ { r } } ) .
$$

Details can be found in [2] and [3].

In the situation we are considering,the eigenvalues of the Liouville vector field $\pmb { \xi }$ (i.e. the eigenvalues of $A ( q )$ )at the singular point $\pmb q$ satisfy the integral relations

$$
\lambda _ { i } = 1 \lambda _ { r } + 1 \lambda _ { s }
$$

where $\begin{array} { r } { \lambda _ { i } = 1 \ , \ i = 1 , . . . , k \ \lambda _ { r } = \lambda _ { s } = \frac { 1 } { 2 } } \end{array}$ ， $r , s = k + 1 , . . . , n$ . According to the definition the possible resonant monomials in each fiber are

$$
( * ) \qquad x _ { r } x _ { s } { \frac { \partial } { \partial y _ { i } } } \ , \ y _ { r } y _ { s } { \frac { \partial } { \partial y _ { i } } } \ , \ x _ { r } y _ { s } { \frac { \partial } { \partial y _ { i } } }
$$

for $i = 1 , . . . , k ; r , s = k + 1 , . . . , n$ . Thus

$$
\xi = L ( \xi ) + \sum _ { r = k + 1 } ^ { n } E _ { r } { \frac { \partial } { \partial x _ { r } } } + \sum _ { \ell = 1 } ^ { n } F _ { \ell } { \frac { \partial } { \partial y _ { \ell } } }
$$

where for each $\boldsymbol { q } = ( \pmb { x } _ { 1 } , . . . , \pmb { x } _ { k } )$ the functions $E _ { r } ( q , \cdot ) , F _ { \ell } ( q , \cdot )$ vanish to higher order than $\begin{array} { r } { \big ( \sum _ { r = k + 1 } ^ { n } | x _ { r } | ^ { 2 } + \sum _ { l = 1 } ^ { n } | y _ { \ell } | ^ { 2 } \big ) ^ { 1 / 2 } } \end{array}$ . Denote by $\xi ^ { q }$ the restriction of $\pmb { \xi }$ to $W _ { g }$

Proposition 2.1 For each $\pmb q$ the Taylor expansion of $\xi ^ { q }$ contains no resonant quadratic terms.

Proof: The Taylor expansions of $\xi ^ { q }$ fit together to give a Taylor expansion of the vector feld $\pmb { \xi }$ in terms of the coordinates yi, xg， ys, $i = 1 , . . . , k ;$ $s = k + 1 , . . . , n$ ，with coefficients which are functions of the $\pmb { x _ { i } }$ ， $i = 1 , . . . , k$ It suffices to show that this expansion has no terms of the form $( * )$ . Notice that the vector field $\eta = \xi - L ( \xi )$ is hamiltonian since

$$
{ \mathcal { L } } _ { \eta } \Omega = d { \big ( } [ \xi - L ( \xi ) ] { \big ) } = \Omega - \Omega = 0 .
$$

Let $\pmb { H }$ be a hamiltonian function for $\pmb { \eta }$ (i.e. $\eta \lrcorner \Omega = d H \rangle$ If $\pmb { \eta }$ (therefore $\pmb { \xi } \ )$ had any resonant monomial, then the usual Taylor expansion of the hamiltonian function $\pmb { H }$ in terms of all the ${ \pmb x } _ { l } , { \pmb y } _ { l }$ would contain nonzero terms of the type:

$$
x _ { i } x _ { r } x _ { s } , \ x _ { i } x _ { r } y _ { s } , \ x _ { i } y _ { r } y _ { s }
$$

for $1 \leq i \leq k \ ; \ k + 1 \leq s , r \leq n$ . Consequently $\pmb { \eta }$ would also contain terms of the type

$$
x _ { i } x _ { s } \frac { \partial } { \partial x _ { r } } , \ x _ { i } x _ { s } \frac { \partial } { \partial y _ { r } } , \ x _ { i } y _ { s } \frac { \partial } { \partial x _ { r } } \ o r \ x _ { i } y _ { s } \frac { \partial } { \partial y _ { r } }
$$

which is impossible since the functions $E _ { r }$ and $F _ { \ell }$ do not contain terms which depend linearly on $\pmb { x } _ { \pmb { \mathscr { s } } }$ or $y _ { s } , k + 1 \le s \le n$ . Observe that for each leaf $W _ { \mathfrak { g } }$ ， the $\pmb { x _ { i } }$ are constants and so are coefficients.

By Poincaré-Dulac's theorem [1] p.184,the non-resonant quadratic terms can be annhilated by a polynomial change of variable,i.e.: the system $\dot { w } = \xi ^ { q } ( w )$ can be reduce to the form $\dot { w } = A ( q ) w + G ( w , q ) + F ( w , q )$ where $D ^ { 0 } F ( q _ { 0 } , q ) = D ^ { 1 } F ( q _ { 0 } , q ) = D ^ { 2 } F ( q _ { 0 } , q ) = 0$ and $\pmb { G }$ contains only the possible resonant terms.But by Proposition 2.1 $G ( w , q )$ vanishes identically. Therefore we can apply Sell's algorithm for $r = 3$ and obtain that the linearizing conjugation is of class $K = 1$ . Since the eigenvalues of $A ( q _ { 0 } )$ are 1or $1 / 2$ ， the spectral spread $\rho ^ { + }$ equals 2. Because $\Sigma ^ { - } A ( q _ { 0 } ) = \emptyset$ the rsmoothness of $A ( q _ { 0 } )$ is the largest integer $K \geq 0$ such that $r - K 2 \ge 0$ Thus for $K > 1$ in order to be able to apply Sell's algorithm we take $r = 2 K$ and since the only resonances occur with $| m | = 2$ we can perform a further $C ^ { \infty }$ -substitution,as in the proof of Poincaré theorem [1] p.181,to reduce the system $\dot { w } = A ( q ) w + F ( w , q )$ to the form $\dot { w } = A ( q ) w + o ( | w | ^ { r } )$ . Hence Sell's theorem guarantees that the linearizing conjugation $\Phi$ is of class $C ^ { \kappa }$ . This completes the proof of the following.

Theorem 2.2 For $k \geq 1$ , there is a $C ^ { k }$ -smooth linearizing conjugation between the Liouville vector feld ${ \pmb \xi }$ and its linear part on a neighborhood of each singular point $\pmb q$ of ${ \pmb \xi }$

This means that there is a local diffeomorphism on a neighborhood of $\pmb q$ in $P$ which carries the trajectories of the flow generated by the vector field ${ \pmb \xi }$ to the trajectories of the flow of its linear part,preserving the direction of motion.

This talk was given at the Symplectic Geometry Workshop held at the University of Warwick in August 1990. I would like to thank D.Salamon for his kind invitation.I am also grateful to Prof.D.McDuff for her constant advise, to Prof. J.Eels and to Prof. A. Verjovsky for their support and hospitality at the International Centre for Theoretical Physics,Trieste.

# References

[1] V.I. Arnold: Geometrical methods in the theory of ordinary differential equations.A Series of Comprehensive Studies in Mathematics 250. Springer-Verlag. (1988)   
[2] E. Ciriza: The symplectic structure of submanifolds of Kahler manifolds of non-positive curvature. Ph.D Thesis, State University of New York at Stony Brook. (1989)   
[3] E. Ciriza: The local structure of a Liouville vector field. To appear in Amer. J. Math.   
[4] E. Ciriza: On special submanifolds in symplectic geometry. To appear in Diff. Geom. and its Appl.   
[5] M.W. Hirsch, C.C. Pugh, M. Shub: Invariant manifolds. Lecture Notes in Math. 583. Springer-Verlag.(1977)   
[6] P. Libermann, C-M. Marle.: Symplectic Geometry and Analytical Mechanics.D.Reidel Publishing Company, Holland. (1987)   
[7] C. Robinson: Stable manifolds in hamiltonian systems. Contemporary Mathematics Vol 81, (1988)   
[8] D. McDuff: The symplectic structures of Kahler manifolds of non-positive curvature. J.Diff. Geometry 28. (1988)   
[9] D. McDuff: Symplectic structures on $\mathbf { R } ^ { 2 n }$ . Proceedings of the Seminaire Sud-Rhodanien (Lyon 1986). Travaux en Cours. Hermann, Paris.   
[10] J. Moser: On the volume elements on a manifold. Trans. Amer. Math. Soc. 120. (1965)   
[11] T. Nagano: 1-formes with their exterior derivative of maximal rank. J.Diff. Geometry 2. (1968)   
[12] G. Sell: Smooth linearization near a fixed point. Am. J. Math. 107 (1985).1035-1091   
[13] S. Sternberg: On contractions and a theorem of Poincare. Amer. J. Math. 79. (1957)   
[14] A. Weinstein: Lectures on symplectic manifolds. CBMS regional conference series in Math 29,Am. Math. Soc. (1977)

# Complex cobordism, Ashtekar's equations and diffeomorphisms

# S.K. DONALDSON

# 1．INTRODUCTION

In this note we will try to bring together two sets of ideas: first,the ideas of Segal [7] on the complexification of diffeomorphism groups and second the Ashtekar formulation [1] of the self-dual Einstein equation in 4 dimensions. The account here is rather informal; our main purpose is to point out the connection between these ideas,rather than proving specific results. In particular,while one may hope that interesting analytical problems andglobal questions may be involved in a later stage,we make no attempt to tackle such questions here. Constructions from Symplectic Geometry wil be fundamental in our discussion.

We will first describe this background in more detail. Recall that if $\pmb { G }$ is a Lie group with Lie algebra $\pmb { \mathfrak { g } }$ ,the complexification ${ \mathfrak { g } } ^ { c } = { \mathfrak { g } } \otimes { \mathbf { C } }$ of the Lie algebra always exists,as a complex Lie algebra. We say that $\pmb { G }$ has a complexification if there is a Lie group $G ^ { c }$ with Lie algebra ${ \mathfrak { g } } ^ { c }$ which contains $\pmb { G }$ as a subgroup realising the standard embedding ${ \mathfrak { g } } \subset { \mathfrak { g } } ^ { c }$ .It is well known that if $\pmb { G }$ is a compact group such a complexification exists, and if $\pmb { G }$ is finite dimensional a complexification exists up to a covering. But when we go to infinite dimensional groups the picture changes,and a complexification will not exist in general, even if one goes to a covering group.In his approach to Conformal Field Theory, Segal defines a semigroup $\pmb { A }$ which,he argues,should play the role of the complexification of the group $\operatorname { D i f f } ( S ^ { 1 } )$ of orientation-preserving diffeomorphisms of the circle.An element of $\pmb { A }$ is a 2-dimensional manifold $\pmb { X }$ ，with boundary,diffeomorphic to the standard annulus and with the additional structure

(1）An almost complex structure,smooth up to the boundary (2) Fixed parametrisations $j ^ { + } , j ^ { - } : S ^ { 1 } \to \partial X$ of the two boundary components

The composition in the semigroup $\pmb { A }$ is defined by gluing together annuli. This semigroup enjoys many of the properties one would hope for in a complexification of $\operatorname { D i f f } ( S ^ { 1 } )$ . In particular, there is a notion of the “action” of $\pmb { A }$ on the complexified Lie algebra,i.e. the sections of $\pmb { T S ^ { 1 } } \otimes \mathbf { C }$ over $S ^ { 1 }$ ，which gives a substitute for the adjoint action of the complexified group on its Lie algebra. This is the aspect of Segal's construction which we will attempt to generalise. The “action” is defined as follows: if $V$ is a holomorphic vector field over $x$ the boundary-values of $V$ ， pulled back by $j ^ { + } , j ^ { - }$ give sections $V ^ { + } , V ^ { - }$ of the complexified tangent bundle of the circle,and we then write $X ( V ^ { - } ) = V ^ { + }$ . It is easy to see that $V ^ { + }$ is uniquely determined by $\pmb { X }$ and

$V ^ { - }$ ，although the action is not really defined everywhere-for a fixed $\pmb { X }$ ， the transformed element $X ( V ^ { - } )$ will not exist for all $\pmb { V } ^ { - }$ ，although for a given real-analytic $\pmb { V } ^ { - }$ ，the transform $X ( V ^ { - } )$ will exist for all sufficiently $\mathbf { \omega } ^ { \mathsf { s e } } \mathbf { t h i n } ^ { \mathsf { s } }$ annuli $\pmb { X }$ . Contemplating Segal's scheme,one is lead to wonder if there are other situations in which it is useful to define a similar “adjoint orbit”of a fictitious complexified difeomorphism group. More generally, if $\pmb { G }$ is a Lie group,possibly infinite dimensional, which acts on a vector space $u$ one can ask for a definition which will generalise that of the orbit of the complexification $G ^ { c }$ on $u \otimes \mathbf { C }$ . There is an obvious answer to this question. We say that elements $U ^ { + } , U ^ { - } \in \mathcal { U } \otimes { \bf C }$ are ${ } ^ { 6 6 } G ^ { c }$ related” if there are

(1）An element $\pmb { g }$ of $\pmb { G }$   
(2) Smooth 1-parameter families $U _ { 1 } ( t ) , U _ { 2 } ( t ) \in \mathcal { U }$ parametrised by an interval $( - a , a ) \subset \mathbf { R }$ with $U _ { 1 } ( - a ) + i U _ { 2 } ( - a ) = U ^ { - } , U _ { 1 } ( a ) + i U _ { 2 } ( a ) =$ $g ( U ^ { + } )$   
(3) A smooth 1-parameter family $\pmb { \xi } ( t )$ in the Lie algebra of $\pmb { G }$ such that

$$
{ \frac { d } { d t } } ( U _ { 1 } + i U _ { 2 } ) = i \xi . ( U _ { 1 } + i U _ { 2 } ) .
$$

(In (2) we use the fact that ${ \pmb g } \in G$ acts on $u$ and so on $u ^ { c }$ .) It is easy to see that in the finite dimensional case $U ^ { \pm }$ are $G ^ { c }$ -related if and only if they lie in the same $G ^ { c }$ orbit so this is a reasonable definition. It is also not hard to check that this definition agrees with the one given by Segal, in the case of the diffeomorphism group of the circle. More generally if $\pmb { G }$ is a group of diffeomeorphism of a $\pmb { d }$ -manifold $\pmb { M }$ and $u$ is some space of tensor fields over $\pmb { M }$ then we can re-interpret the data above as a triple of tensor fields on the product space $M \times ( - \pmb { a } , \pmb { a } )$ , satisfying a differential equation corresponding to (1).It seems however that this interpretation will not be interesting in general. The key feature of Segal's case is that the data on the product space has an intrinsic interpretation (as a complex structure and holomorphic vector field),independent of the particular space-time description of the cylinder.This is a kind of extra $d + 1$ -dimensional “Lorentz invariance” of the equation (1),which does not hold in general. Our purpose here is to point out that there is another case where we have a similar intrinsic interpretation of the equation (1) in $( d + 1 )$ dimensions.

The other main motivation for our discussion comes from Nahm's equations. These are a system of ordinary differential equations for a triple $T _ { 1 } ( t ) , T _ { 2 } ( t ) , T _ { 3 } ( t )$ of elements of a Lie algebra ${ \mathfrak { g } } .$ ，depending on a real parameter $\pmb { t }$ . The equations are

$$
\begin{array} { c } { \displaystyle \frac { d T _ { 1 } } { d t } = \left[ T _ { 2 } , T _ { 3 } \right] } \\ { \displaystyle \frac { d T _ { 2 } } { d t } = \left[ T _ { 3 } , T _ { 1 } \right] } \\ { \displaystyle \frac { d T _ { 3 } } { d t } = \left[ T _ { 1 } , T _ { 2 } \right] } \end{array}
$$

The first two of these equations can be combined into

$$
\frac { d } { d t } ( T _ { 1 } + i T _ { 2 } ) = [ i T _ { 3 } , T _ { 1 } + i T _ { 2 } ] ,
$$

so a solution of Nahm's equations,over an interval $[ - a , a ]$ ， gives data of the kind considered above,with the adjoint representation of $\pmb { G }$ and $U _ { 1 } =$ $T _ { 1 } , U _ { 2 } = T _ { 2 } , \xi = T _ { 3 }$ . Let us say that a pair $U ^ { + } , U ^ { - }$ in ${ \mathfrak { g } } ^ { c }$ are “related by a Nahm solution” if $U ^ { + } = T _ { 1 } ^ { + } + i T _ { 2 } ^ { + }$ ， $U ^ { - } = T _ { 1 } ^ { - } + i T _ { 2 } ^ { - }$ and there is a solution of Nahm's equations over $[ - a , a ]$ with $T _ { 1 } ( \pm a ) = T _ { 1 } ^ { \pm }$ ， $T _ { 2 } ( \pm a ) = T _ { 2 } ^ { \pm }$ . Thus if $U ^ { + } , U ^ { - }$ are related by a Nahm solution they are also $G ^ { c }$ related. If the group $\pmb { G }$ is compact then the converse holds:a pair is related by a Nahm solution if and only if they are $G ^ { c }$ related,i.e. ifand only if they lie in the same orbit of the complexifed group. This is proved in [2] for the unitary groups by setting up Nahm's equations as the Euler-Lagrange equations for a functional on paths on the space $G ^ { c } / G$ ，and the argument has been extended to other compact groups by P. Saskida [7]. This identifcation is important in the work of Kronheimer [5] on adjoint orbits.From this point of view it is natural to investigate the corresponding question for infinitedimensional groups. The case of gauge groups leads to boundary value problems for Yang-Mills fields of the sort considered in [3]. Here we will look at diffeomorphism groups,the point being that we can make contact with the work of Ashtekar, who showed that Nahm's equations for the Lie algebra of the group of volume-preserving diffeomorphisms of a 3-manifold $\boldsymbol { Y }$ are a form of the self-dual Einstein equations on $Y \times \mathbf { R }$ .(Ashtekar's ideas have been extended by Mason and Newman [6], and we will make use of some of their simplifications.）
