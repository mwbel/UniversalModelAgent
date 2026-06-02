# 1 Lagrangian manifolds

A variational family is a pair

$$
\pi : { \cal P }  X , \qquad \phi : { \cal P }  { \bf R }
$$

consisting of a surjective submersion $\pmb { \pi }$ between manifolds $P$ and $X$ ，and a smooth function $\phi$ on $P$ .Each choice of ${ \textbf { \em x } } \in X$ determines a constrained variational problem

We call a critical point of $\phi | \pi ^ { - 1 } ( { \pmb x } )$ a fiber critical point of $\phi$ Denote by ${ \cal C } ( \pi , \phi ) \subset { \cal P }$ the set of all fiber critical points $c \in P$ of $\phi$ At a fiber critical point $c$ the differential $d \phi ( c )$ vanishes on the vertical tangent space


<!-- chunk 0004: pages 211-242 -->
ker $d \pi ( c ) = T _ { c } \pi ^ { - 1 } ( x )$ . This means that there exists a Lagrange multiplier $y \in T _ { x } ^ { * } X$ such that

$$
d \phi ( \mathbf { c } ) \gamma = \langle y , d \pi ( c ) \gamma \rangle
$$

for every $\gamma \in T _ { c } P$ . The Lagrange multiplier $\pmb { y }$ is uniquely determined since $d \pi ( c )$ is surjective. Consider the map

$$
\lambda _ { \pi , \phi } : C ( \pi , \phi ) \to T ^ { * } X
$$

defined by $\lambda _ { \pi , \phi } ( c ) = ( x , y )$ where ${ \mathfrak { x } } = \pi ( c )$ and $\pmb { y }$ is given by (1). Denote its image by

$$
\Lambda ( \pi , \phi ) = \{ ( x , y ) \in T ^ { * } X : \exists c \in \pi ^ { - 1 } ( x ) { \mathrm { ~ s u c h ~ t h a t ~ ( 1 ) } } \} .
$$

If $\Lambda = \Lambda ( \pi , \phi )$ is a set of this form then we say that $( \pi , \phi )$ defines $\Lambda$ and call $\phi$ a phase function for $\Lambda$ with respect to $\pmb { \pi }$ .An extreme case is where $P = X$ and $\pi : P \to X$ is the identity so that $\phi$ is a function on $X$ and $\Lambda = \operatorname { G r } ( d \phi )$ In this case $\phi$ is called a generating function for $\Lambda$

Let $N _ { \pi } \subset T ^ { * } P$ denote the fiber normal bundle:

$$
N _ { \pi } = \{ ( c , b ) \in T ^ { * } P : b \in \ker ( d \pi ( c ) ) ^ { \bot } \} .
$$

This is a co-isotropic submanifold of ${ \pmb T } ^ { \star } { \pmb P }$ and its symplectic quotient is $\mathbf { \nabla } T ^ { * } X$ ， In the lingo of [28] $\Lambda ( \pi , \phi )$ is the symplectic reduction of the Lagrangian manifold $\mathrm { G r } ( d \phi )$ .Recall that two submanifolds $G$ and $N$ of a manifold W are said to intersect

- transversally in $W$ iff $T _ { z } W = T _ { z } G + T _ { z } N$ , and - cleanly in $W$ iff $T _ { z } ( G \cap N ) = T _ { z } G \cap T _ { z } N$ for $z \in G \cap N$ . (For clean interesection impose the condition that the intersection $G \cap N$ be a submanifold; for transverse intersections this follows.A transversal intersection is automatically clean.） We call the variational family $( \pi , \phi )$ tranversal (resp. clean) iff $\mathrm { G r } ( d \phi )$ intersects $N _ { \pi }$ transversally (resp. cleanly） in $P$

Proposition 1.1 If $( \pi , \phi )$ is a clean variational family, then $\Lambda ( \pi , \phi )$ is an immersed Lagrangian manifold. If $( \pi , \phi )$ is a transversal variational family, then $\lambda _ { \pi , \phi }$ is a Lagrangian immersion.2

Proof: Localize and choose co-ordinates so that $P = X \times U$ where $X \subset \mathbb { R } ^ { n }$ and $U \subset \mathbb { R } ^ { N }$ and that $\pi : X \times U \to X$ is the projection

$$
\pi ( \mathrm { c } ) = x , \qquad c = ( x , u ) .
$$

Then $C ( \pi , \phi )$ is defined by the equation $\partial _ { u } \phi = 0$ and $\Lambda ( \pi , \phi )$ is defined by eliminating $\pmb { u }$ from the equations

$$
\partial _ { u } \phi = 0 , \qquad y = \partial _ { x } \phi .
$$

The family is transversal ifO is a regular value of $\partial _ { u } \phi$ and clean iff $C ( \pi , \phi )$ is a manifold and the tangent space at a point $\mathbf { c } = ( x , u ) \in C ( \pi , \phi )$ is given by

$$
\begin{array} { r } { T _ { \mathfrak { c } } C ( \pi , \phi ) = \{ ( \xi , v ) \in \mathbb { R } ^ { n } \times \mathbb { R } ^ { N } : \partial _ { u } \partial _ { x } \phi ( x , u ) \xi + \partial _ { u } \partial _ { u } \phi ( x , u ) v = 0 \} . } \end{array}
$$

To prove Proposition 1.1 fix $c = ( x , u ) \in C ( \pi , \phi )$ and apply the next lemmawith $A = \partial _ { x } \partial _ { x } \phi ( x , u ) , B = \partial _ { x } \partial _ { u } \phi ( x , u ) , B ^ { T } = \partial _ { u } \partial _ { x } \phi ( x , u ) , C = \partial _ { u } \partial _ { u } \phi ( x , u )$ ，$d \partial _ { u } \phi ( x , u ) = ( B ^ { T } , C )$ ， $T = T _ { c } C ( \pi , \phi ) , \ell = d \lambda _ { \pi , \phi } ( c ) ,$

Lemma 1.2 Suppose that $A \in \mathbb { R } ^ { n \times n }$ and $C \in \mathbb { R } ^ { N \times N }$ are symmetric and that $B \in  { \mathbb { R } } ^ { n \times N }$ .Let

$$
T = \{ ( \xi , v ) : B ^ { T } \xi + C v = 0 \} \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { N }
$$

and $\ell : T \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n } \ b y$

$$
\ell ( \xi , v ) = ( \xi , A \xi + B v ) .
$$

Then $\ell ( T ) \subset \mathsf { R } ^ { n } \times \mathsf { R } ^ { n }$ is a Lagrangian subspace.

Proof: Note that $( \xi , \eta ) \in \ell ( T )$ iff the inhomogeneous system

$$
\begin{array} { r c l } { { B v } } & { { = } } & { { - A \xi + \eta } } \\ { { C v } } & { { = } } & { { - B ^ { T } \xi } } \end{array}
$$

has a solution $^ { v }$ . Hence $( \xi , \eta ) \in \ell ( T )$ if

$$
B ^ { T } \xi ^ { \prime } + C v ^ { \prime } = 0 \Longrightarrow \langle \xi ^ { \prime } , - A \xi + \eta \rangle + \langle v ^ { \prime } , - B ^ { T } \xi \rangle = 0 .
$$

On the other hand $( \xi , \eta ) \in \ell ( T ) ^ { \omega }$ iff

$$
B ^ { T } \xi ^ { \prime } + C v ^ { \prime } = 0 \Longrightarrow \left. \xi , A \xi ^ { \prime } + B v ^ { \prime } \right. - \left. \eta , \xi ^ { \prime } \right. = 0 .
$$

Hence $\ell ( T ) = \ell ( T ) ^ { \omega }$

At a critical point of a function, the Hessian is a well-defined quadratic form on the tangent space; at a fiber critical point $c$ the vertical Hessian is defined on the vertical tangent space. By Taylor's theorem the vertical Hessian $\Phi$ is characterized by the equation

$$
\phi ( c + \gamma ) = \phi ( c ) + { \textstyle \frac { 1 } { 2 } } \Phi ( \gamma ) + { \cal O } ( \| \gamma \| ^ { 3 } )
$$

for $d \pi ( c ) \gamma = 0$ .Here $c + \gamma = \exp _ { c } ( \gamma ) \in P$ where exp is an exponential map which carries vertical tangent vectors to the fiber; $\Phi$ is independent of the choice.

Proposition 1.3 Assume that $( \pi , \phi )$ is a transversal variational family, and $c \in C ( \pi , \phi )$ . Then $\Phi$ is non-degenerate iff $d \pi ( c ) : T _ { c } C ( \pi , \phi ) \to T _ { x } X$ is an isomorphism.

Proof: In local coordinates ${ \mathfrak { c } } = ( { \mathfrak { x } } , { \mathfrak { u } } )$ the tangent space $T _ { c } C ( \pi , \phi )$ is defined by the equation

$$
\partial _ { u } \partial _ { x } \phi ( c ) \hat { x } + \partial _ { u } \partial _ { u } \phi ( c ) \hat { u } = 0 .
$$

Hence the projection $( \hat { \pmb x } , \hat { \pmb u } ) \mapsto \hat { \pmb x }$ is an isomorphism on $T _ { c } C ( \pi , \phi )$ if and only if the Hessian matrix $\Phi = \partial _ { u } \partial _ { u } \phi ( c )$ is invertible. □

Definition 1.4 A fber critical point $c \in C ( \pi , \phi )$ is called nondegenerate if the fiber Hessian $\Phi$ is nondegenerate.This implies that

(1) $\operatorname { G r } ( d \phi )$ and $N _ { \pi }$ intersect transversally at $c _ { i }$ (2) $d \pi ( \mathrm { c } ) : T _ { c } C ( \pi , \phi )  T _ { x } X$ is invertible,and (3) $T _ { x } ^ { * } X \cap T _ { ( x , y ) } \Lambda ( \pi , \phi ) = 0 .$

In (3) $T _ { x } ^ { \ast } X \subset T _ { ( x , y ) } T ^ { \ast } X$ is the vertical tangent space of the cotangent bundle. The inverse

$$
G = d \pi ( c ) ^ { - 1 } : T _ { x } X \to T _ { c } C ( \pi , \phi )
$$

of the projection in (2) is called the Green's function of $\phi$ at c. By the implicit function theorem $\pi | C ( \pi , \phi )$ is a diffeomorphism in a neighborhood of ${ \mathfrak { x } } = \pi ( c )$ : we denote the local inverse by $\pmb { g }$ and callit the nonlinear Green's function. Clearly

$$
G = d g ( x ) .
$$

Remark 1.5 If the projection $\pi : C ( \pi , \phi ) \to X$ is a diffeomorphism, there is a global nonlinear Green's function $g \ : \ X \to P$ .Its image is the set $\begin{array} { r } { g ( X ) = C ( \pi , \phi ) } \end{array}$ of fiber critical points. In this case $\Lambda ( \pi , \phi )$ admits a generating function $\phi \circ g : X  \mathbb { R }$

# 2Symplectic relations

A symplectic relation from a symplectic manifold $M _ { 0 }$ to a symplectic manifold $M _ { 1 }$ is a Lagrangian submanifold of $\bar { M } _ { 0 } \times M _ { 1 }$ . The bar indicates that the sign of the symplectic form in the first factor has been reversed. We do not assume that $M _ { 0 }$ and $M _ { 1 }$ have the same dimension.A clean variational family $( \pi _ { 0 1 } , \phi _ { 0 1 } )$ with $\pi _ { 0 1 } : P _ { 0 1 } \to X _ { 0 } \times X _ { 1 }$ determines a symplectic relation from ${ \pmb T } ^ { \ast } X _ { 0 }$ to $T ^ { \ast } X _ { 1 }$ . The construction is as in the previous section but with a sign change. As before at a critical point $c$ there is a Lagrange multiplier $( - y _ { 0 } , y _ { 1 } ) \in T _ { x _ { 0 } } ^ { * } X _ { 0 } \times T _ { x _ { 1 } } ^ { * } X _ { 1 }$ such that

$$
d \phi _ { 0 1 } ( \mathrm { c } ) \gamma = \langle y _ { 1 } , \xi _ { 1 } \rangle - \langle y _ { 0 } , \xi _ { 0 } \rangle
$$

for every $\gamma \in T _ { c } P$ where $d \pi ( c ) \gamma = ( \xi _ { 0 } , \xi _ { 1 } )$ . Denote by the relation induced by $\phi _ { 0 1 }$ . We call $\phi _ { 0 1 }$ a phase function for $R _ { 0 1 }$ and call $R _ { 0 1 }$ the relation defined by $( \pi _ { 0 1 } , \phi _ { 0 1 } )$ . If $( \pi _ { 0 1 } , \phi _ { 0 1 } )$ is a clean variational family then $R _ { 0 1 }$ is a symplectic relation.In the extreme case where $P _ { 0 1 } = X _ { 0 } \times X _ { 1 }$ and $\pi _ { 0 1 }$ is the identity we call $\phi _ { 0 1 }$ a generating function for $R _ { 0 1 }$ .If $\psi _ { 1 0 }$ ： $T ^ { * } X _ { 0 } \to T ^ { * } X _ { 1 }$ is a symplectomorphism then its graph $R _ { 0 1 } = \mathrm { G r } ( \psi _ { 1 0 } )$ isa symplectic relation. In this case we call $\phi _ { 0 1 }$ a phase function (or generating function) for $\psi _ { 1 0 }$

The composition of two relations $R _ { 0 1 } \subset \bar { M } _ { 0 } \times M _ { 1 }$ and $R _ { 1 2 } \subset \bar { M } _ { 1 } \times M _ { 2 }$ is the relation

$$
R _ { 0 1 } \# R _ { 1 2 } = \left\{ \left( z _ { 0 } , z _ { 2 } \right) : \left( z _ { 0 } , z _ { 1 } \right) \in R _ { 0 1 } , \left( z _ { 1 } , z _ { 2 } \right) \in R _ { 1 2 } \right\} .
$$

Note that by our conventions the graph operation is a contravariant functor:

$$
\mathrm { G r } ( \psi _ { 2 1 } \circ \psi _ { 1 0 } ) = \mathrm { G r } ( \psi _ { 1 0 } ) \# \mathrm { G r } ( \psi _ { 2 1 } ) .
$$

A Lagrangian manifold is a special case of a symplectic relation (take $M _ { 0 }$ to be a point) and we have the formula

$$
\psi _ { 2 1 } \big ( \Lambda _ { 1 } \big ) = \Lambda _ { 1 } \# \mathrm { G r } ( \psi _ { 2 1 } )
$$

if $\Lambda _ { 1 } \subset M _ { 1 }$ is Lagrangian.

Let $( \pi _ { 0 1 } , \phi _ { 0 1 } )$ and $\left( \pi _ { 1 2 } , \phi _ { 1 2 } \right)$ be variational families with

$$
\pi _ { 0 1 } : P _ { 0 1 }  X _ { 0 } \times X _ { 1 } , \qquad \pi _ { 1 2 } : P _ { 1 2 }  X _ { 1 } \times X _ { 2 } .
$$

Define another variational family $( \pi _ { 0 2 } , \phi _ { 0 2 } )$ by

$$
P _ { 0 2 } = \{ ( c _ { 0 1 } , c _ { 1 2 } ) \in P _ { 0 1 } \times P _ { 1 2 } : \pi _ { 0 1 } ( c _ { 0 1 } ) = ( x _ { 0 } , x _ { 1 } ) , \pi _ { 1 2 } ( c _ { 1 2 } ) = ( x _ { 1 } , x _ { 2 } ) \}
$$

with $\pi _ { 0 2 } : P _ { 0 2 } \to X _ { 0 } \times X _ { 2 }$ given by

$$
\pi _ { 0 2 } ( c _ { 0 1 } , c _ { 1 2 } ) = ( x _ { 0 } , x _ { 2 } )
$$

and $\phi _ { 0 2 } : P _ { 0 2 } \to \mathbb { R }$ by

$$
\phi _ { 0 2 } ( c _ { 0 1 } , c _ { 1 2 } ) = \phi _ { 0 1 } ( c _ { 0 1 } ) + \phi _ { 1 2 } ( c _ { 1 2 } ) .
$$

Let $R _ { j k } \subset T ^ { * } X _ { j } \times T ^ { * } X _ { k }$ be the relation defined by $( \pi _ { j k } , \phi _ { j k } )$

Proposition 2.1 $R _ { 0 2 } = R _ { 0 1 } \# R _ { 1 2 }$

Proof: Fix $c _ { 0 2 } = ( c _ { 0 1 } , c _ { 1 2 } ) \in P _ { 0 2 }$ and

$$
\gamma _ { 0 2 } = ( \gamma _ { 0 1 } , \gamma _ { 1 2 } ) \in T _ { c _ { 0 1 } } P _ { 0 1 } \times T _ { c _ { 1 2 } } P _ { 1 2 }
$$

and introduce the notations $( { x } _ { j } , { x } _ { k } ) = { \pi } _ { j k } ( { c } _ { j k } )$ and

$$
d \pi _ { 0 1 } ( c _ { 0 1 } ) \gamma _ { 0 1 } = ( \xi _ { 0 } , \xi _ { 1 } ) , \quad d \pi _ { 1 2 } ( c _ { 1 2 } ) \gamma _ { 1 2 } = ( \xi _ { 1 } ^ { \prime } , \xi _ { 2 } ) .
$$

The tangent space to $P _ { 0 2 }$ at $\pmb { c _ { 0 2 } }$ is the set of all pairs $\gamma _ { 0 2 }$ such that $\pmb { \xi } _ { 1 } = \pmb { \xi } _ { 1 } ^ { \prime }$ . The tangent space to the fber of $P _ { 0 2 }$ is defined by the three constraints $\xi _ { 0 } = 0$ ， $\xi _ { 1 } = \xi _ { 1 } ^ { \prime }$ ，and $\xi _ { 2 } = 0$ Then $\pmb { c _ { 0 2 } }$ is a fiber critical point iff there are Lagrange multipliers $y _ { 0 } \in T _ { x _ { 0 } } ^ { * } X _ { 0 }$ ， $y _ { 1 } \in T _ { x _ { 1 } } ^ { * } X _ { 1 }$ ,and $y _ { 2 } \in T _ { x _ { 2 } } ^ { * } X _ { 2 }$ such that

$$
d \phi _ { 0 1 } ( c _ { 0 1 } ) \gamma _ { 0 1 } + d \phi _ { 1 2 } ( c _ { 1 2 } ) \gamma _ { 1 2 } = \langle y _ { 2 } , \xi _ { 2 } \rangle + \langle y _ { 1 } , \xi _ { 1 } - \xi _ { 1 } ^ { \prime } \rangle - \langle y _ { 0 } , \xi _ { 0 } \rangle
$$

for al $l \left( \gamma _ { 0 1 } , \gamma _ { 1 2 } \right) \in T _ { c _ { 0 1 } } P _ { 0 1 } \times T _ { c _ { 1 2 } } P _ { 1 2 }$ . In particular

$$
d \phi _ { 0 1 } ( c _ { 0 1 } ) \gamma _ { 0 1 } = \langle y _ { 1 } , \xi _ { 1 } \rangle - \langle y _ { 0 } , \xi _ { 0 } \rangle
$$

(take $\gamma _ { 1 2 } = 0$ and

$$
d \phi _ { 1 2 } ( c _ { 1 2 } ) \gamma _ { 1 2 } = \langle y _ { 2 } , \xi _ { 2 } \rangle - \langle y _ { 1 } , \xi _ { 1 } ^ { \prime } \rangle
$$

(take $\gamma _ { 0 1 } = 0 .$ ).This shows that $R _ { 0 2 } \subset \mathrm { R } _ { 0 1 } \# R _ { 1 2 }$ . For the reverse inclusion argue backwards. □

The composition operation has the following interpretation.For ${ \boldsymbol { \mathfrak { x } } } \in { \boldsymbol { X } }$ we identify $T _ { x } ^ { * } X$ with the vertical tangent space

$$
V = T _ { x } ^ { * } X \subset T _ { ( x , y ) } T ^ { * } X .
$$

It is a Lagrangian submanifold of $\mathbf { \nabla } T ^ { * } X$ . Now fix ${ \mathfrak { x } } _ { 0 } \in X _ { 0 }$ and $x _ { 2 } \in X _ { 2 }$ . The goal is to find all pairs $y _ { 0 } \in T _ { x _ { 0 } } ^ { * } X _ { 0 }$ and $y _ { 2 } \in T _ { x _ { 2 } } ^ { * } X _ { 2 }$ such that

$$
( x _ { 0 } , y _ { 0 } , x _ { 2 } , y _ { 2 } ) \in R _ { 0 2 } .
$$

These points correspond to Lagrangian intersections of the image of $T _ { x _ { 0 } } ^ { * } X _ { 0 }$ under $R _ { 0 1 }$ with the preimage of $T _ { x _ { 2 } } ^ { * } X _ { 2 }$ under $R _ { 1 2 }$ . For every point

$$
\left( x _ { 1 } , y _ { 1 } \right) \in \left( T _ { x _ { 0 } } ^ { * } X _ { 0 } \# R _ { 0 1 } \right) \cap \left( R _ { 1 2 } \# T _ { x _ { 2 } } ^ { * } X _ { 2 } \right)
$$

in this intersection there exist points $y _ { 0 } \in T _ { x _ { 0 } } ^ { * } X _ { 0 }$ and $y _ { 2 } \in T _ { x _ { 2 } } ^ { * } X _ { 2 }$ such that $( x _ { 0 } , y _ { 0 } , x _ { 1 } , y _ { 1 } ) \in R _ { 0 1 }$ and $( x _ { 1 } , y _ { 1 } , x _ { 2 } , y _ { 2 } ) \in R _ { 1 2 }$ and hence $( x _ { 0 } , y _ { 0 } , x _ { 2 } , y _ { 2 } ) \in R _ { 0 2 }$ as required. In the special case where $R _ { j k }$ is the graph of a symplectomorphism each intersection point $\left( { \mathfrak { x } } _ { 1 } , { \mathfrak { y } } _ { 1 } \right)$ determines ${ \pmb y } _ { \mathbf 0 }$ and ${ \pmb y } _ { 2 }$ uniquely. Thus given $\pmb { x _ { 0 } }$ and ${ \pmb x } _ { 2 }$ there is a one-to-one correspondence of Lagrangian intersection points in $T ^ { \ast } X _ { 1 }$ with points in $R _ { 0 2 } \cap \left( \hat { T _ { x _ { 0 } } ^ { * } } X _ { 0 } \times T _ { x _ { 2 } } ^ { * } X _ { 2 } \right)$

Now assume that $R _ { j k }$ is a manifold and fix

$$
( x _ { j } , y _ { j } , x _ { k } , y _ { k } ) \in R _ { j k } .
$$

Let $c _ { 0 2 } = ( c _ { 0 1 } , c _ { 1 2 } ) \in P _ { 0 2 }$ be the corresponding fiber critical point so that

$$
\pi _ { j k } ( c _ { j k } ) = \left( x _ { j } , x _ { k } \right)
$$

With this notation we have (3). In the tangent space $T _ { ( x _ { 1 } , y _ { 1 } ) } T ^ { * } X _ { 1 }$ there are three interesting Lagrangian subspaces:

$$
L _ { 0 } = T _ { ( x _ { 1 } , y _ { 1 } ) } \left( T _ { x _ { 0 } } ^ { * } X _ { 0 } \# R _ { 0 1 } \right) , \qquad L _ { 2 } = T _ { ( x _ { 1 } , y _ { 1 } ) } \left( R _ { 1 2 } \# T _ { x _ { 2 } } ^ { * } X _ { 2 } \right) ,
$$

and the vertical space

$$
V = T _ { x _ { 1 } } ^ { * } X _ { 1 } .
$$

We assume that $L _ { 0 }$ and $L _ { 2 }$ are transverse to $V$ . Then the pair $( L _ { 0 } , L _ { 2 } )$ determines a quadratic form on the quotient space $T _ { x _ { 1 } } X _ { 1 } = T _ { ( x _ { 1 } , y _ { 1 } ) } T ^ { * } X _ { 1 } / T _ { x _ { 1 } } ^ { * } X _ { 1 }$ To define it choose a Lagrangian complement $H$ of $V$ ：

$$
T _ { \left( x _ { 1 } , y _ { 1 } \right) } T ^ { * } X _ { 1 } = H \oplus V .
$$

Identify $\pmb { H }$ with the dual space $V ^ { \ast }$ using the symplectic form on $T _ { ( x _ { 1 } , y _ { 1 } ) } T ^ { * } X _ { 1 }$ Since $L _ { 0 }$ and $\scriptstyle { L _ { 2 } }$ are transverse to $V$ there exist quadratic forms $Q _ { j } : H $ $V = H ^ { \ast }$ such that

$$
L _ { 0 } = \mathrm { G r } ( Q _ { 0 } ) , \qquad L _ { 2 } = \mathrm { G r } ( Q _ { 2 } ) .
$$

There is a natural projection (isomorphism) $H \to T _ { x _ { 1 } } X _ { 1 }$ and the difference

$$
Q = Q _ { 0 } - Q _ { 2 }
$$

descends to a quadratic form $T _ { x _ { 1 } } X _ { 1 } \to T _ { x _ { 1 } } ^ { * } X _ { 1 }$ . The result is independent of the choice of $H$ . We abuse language and identify $Q$ with a form on $\pmb { T } _ { \pmb { x } _ { 1 } } \pmb { X } _ { 1 }$ The form $Q$ is called the composition form of $( L _ { 0 } , L _ { 2 } )$ .Denote by $\Phi _ { j k }$ the fiber Hessian at $c _ { j k }$ . Assume that the fiber critical points $c _ { j k } \in C _ { \phi _ { j k } }$ are nondegenerate and denote the Green's functin by $G _ { j k } : T _ { x _ { j } } X _ { j } \times T _ { x _ { k } } { \dot { X } } _ { k } $ $T _ { c _ { j k } } C _ { \phi _ { j k } }$ . Define

$$
G _ { 0 } \xi _ { 1 } = G _ { 0 1 } ( 0 , \xi _ { 1 } ) , \qquad G _ { 2 } \xi _ { 1 } = G _ { 1 2 } ( \xi _ { 1 } , 0 ) .
$$

Proposition 2.2 The linear map

$$
T _ { c _ { 0 2 } } \pi _ { 0 2 } ^ { - 1 } ( x _ { 0 } , x _ { 2 } )  T _ { c _ { 0 1 } } \pi _ { 0 1 } ^ { - 1 } ( x _ { 0 } , x _ { 1 } ) \times T _ { x _ { 1 } } X _ { 1 } \times T _ { c _ { 1 2 } } \pi _ { 1 2 } ^ { - 1 } ( x _ { 1 } , x _ { 2 } )
$$

given by

$$
\gamma _ { 0 2 } = \left( \gamma _ { 0 1 } , \gamma _ { 1 2 } \right) \mapsto \left( \gamma _ { 0 1 } - G _ { 0 } \xi _ { 1 } , \xi _ { 1 } , \gamma _ { 1 2 } - G _ { 2 } \xi _ { 1 } \right)
$$

where $\xi _ { 1 } = d \pi _ { 1 } ( c _ { 0 1 } ) \gamma _ { 0 1 }$ is an isomorphism. Moreover,

$$
\Phi _ { 0 2 } ( \gamma _ { 0 2 } ) = \Phi _ { 0 1 } ( \gamma _ { 0 1 } - G _ { 0 } \xi _ { 1 } ) + \Phi _ { 1 2 } ( \gamma _ { 1 2 } - G _ { 2 } \xi _ { 1 } ) + \langle Q \xi _ { 1 } , \xi _ { 1 } \rangle .
$$

Proof: In local coordinates we have

$$
\phi _ { 0 2 } ( x _ { 0 } , u _ { 0 1 } , x _ { 1 } , u _ { 1 2 } , x _ { 2 } ) = \phi _ { 0 1 } ( x _ { 0 } , u _ { 0 1 } , x _ { 1 } ) + \phi _ { 1 2 } ( x _ { 1 } , u _ { 1 2 } , x _ { 2 } ) .
$$

The relation $R _ { 0 1 }$ is defined by eliminating ${ \boldsymbol { u } } _ { 0 1 }$ from the nonlinear system

$$
\begin{array} { r c l } { - y _ { 0 } } & { = } & { \partial _ { x _ { 0 } } \phi _ { 0 1 } \big ( x _ { 0 } , u _ { 0 1 } , x _ { 1 } \big ) } \\ { y _ { 1 } } & { = } & { \partial _ { x _ { 1 } } \phi _ { 0 1 } \big ( x _ { 0 } , u _ { 0 1 } , x _ { 1 } \big ) } \\ { 0 } & { = } & { \partial _ { u _ { 0 1 } } \phi _ { 0 1 } \big ( x _ { 0 } , u _ { 0 1 } , x _ { 1 } \big ) . } \end{array}
$$

The last equation defines the set $C _ { \phi _ { 0 1 } }$ . The Lagrangian manifold $T _ { x _ { 0 } } ^ { \ast } X _ { 0 } \# R _ { 0 1 }$ is defined by fixing $\pmb { x _ { 0 } }$ and eliminating ${ \boldsymbol { \mathit { u } } } _ { 0 1 }$ from the last two.The tangent space $T _ { \mathsf { c o } _ { 1 } } R _ { \mathsf { 0 1 } }$ is defined by eliminating $v _ { 0 1 }$ from

$$
\begin{array} { r l r } { - \eta _ { 0 } } & { = } & { \big ( \partial _ { x _ { 0 } } \partial _ { x _ { 0 } } \phi _ { 0 1 } \big ) \xi _ { 0 } + \big ( \partial _ { x _ { 0 } } \partial _ { x _ { 1 } } \phi _ { 0 1 } \big ) \xi _ { 1 } + \big ( \partial _ { x _ { 0 } } \partial _ { u _ { 0 1 } } \phi _ { 0 1 } \big ) v _ { 0 1 } } \\ { \eta _ { 1 } } & { = } & { \big ( \partial _ { x _ { 1 } } \partial _ { x _ { 0 } } \phi _ { 0 1 } \big ) \xi _ { 0 } + \big ( \partial _ { x _ { 1 } } \partial _ { x _ { 1 } } \phi _ { 0 1 } \big ) \xi _ { 1 } + \big ( \partial _ { x _ { 1 } } \partial _ { u _ { 0 1 } } \phi _ { 0 1 } \big ) v _ { 0 1 } } \\ { 0 } & { = } & { \big ( \partial _ { u _ { 0 1 } } \partial _ { x _ { 0 } } \phi _ { 0 1 } \big ) \xi _ { 0 } + \big ( \partial _ { u _ { 0 1 } } \partial _ { x _ { 1 } } \phi _ { 0 1 } \big ) \xi _ { 1 } + \big ( \partial _ { u _ { 0 1 } } ^ { 2 } \phi _ { 0 1 } \big ) v _ { 0 1 } . } \end{array}
$$

The last equation defines the tangent space to $C _ { \phi _ { 0 1 } }$ and the Green's function $G _ { 0 1 }$ is given by solving for $v _ { 0 1 }$ . Thus

$$
\begin{array} { r } { G _ { 0 } \xi _ { 1 } = ( 0 , \Gamma _ { 0 } \xi _ { 1 } , \xi _ { 1 } ) , \qquad \Gamma _ { 0 } = - \left( \partial _ { u _ { 0 1 } } ^ { 2 } \phi _ { 0 1 } \right) ^ { - 1 } \partial _ { u _ { 0 1 } } \partial _ { x _ { 1 } } \phi _ { 0 1 } . } \end{array}
$$

To define the Lagrangian subspace ${ \cal L } _ { 0 } = T _ { ( x _ { 1 } , y _ { 1 } ) } \left( T _ { x _ { 0 } } ^ { * } X _ { 0 } \# R _ { 0 1 } \right)$ ，set ${ \pmb \xi } _ { 0 } = { \bf 0 }$ and eliminate ${ \boldsymbol { v } } _ { 0 1 }$ in the last two equations. Hence $L _ { 0 }$ is the graph of the symmetric matrix

$$
\begin{array} { r } { Q _ { 0 } = ( \partial _ { x _ { 1 } } ^ { 2 } \phi _ { 0 1 } ) + ( \partial _ { x _ { 1 } } \partial _ { u _ { 0 1 } } \phi _ { 0 1 } ) \Gamma _ { 0 } . } \end{array}
$$

Similarly, $L _ { 2 }$ is the graph of $Q _ { 2 }$ where

$$
- Q _ { 2 } = \bigl ( \partial _ { x _ { 1 } } ^ { 2 } \phi _ { 1 2 } \bigr ) + \bigl ( \partial _ { x _ { 1 } } \partial _ { u _ { 1 2 } } \phi _ { 1 2 } \bigr ) \Gamma _ { 2 } , \qquad \Gamma _ { 2 } = - \bigl ( \partial _ { u _ { 1 2 } } ^ { 2 } \phi _ { 1 2 } \bigr ) ^ { - 1 } \partial _ { u _ { 1 2 } } \partial _ { x _ { 1 } } \phi _ { 1 2 } .
$$

Now the tangent vector $\gamma _ { 0 2 }$ is in local co-ordinates given by

$$
\gamma _ { 0 2 } = ( 0 , \upsilon _ { 0 1 } , \xi _ { 1 } , \upsilon _ { 1 2 } , 0 )
$$

with $\gamma _ { 0 1 } = ( 0 , \upsilon _ { 0 1 } , \xi _ { 1 } )$ and $\gamma _ { 1 2 } = ( \xi _ { 1 } , v _ { 1 2 } , 0 )$ . Hence

$$
\gamma _ { 0 1 } - G _ { 0 } \xi _ { 1 } = ( 0 , \upsilon _ { 0 1 } - \Gamma _ { 0 } \xi _ { 1 } , 0 )
$$

and

$$
\begin{array} { l c l } { { \Phi _ { 0 1 } ( \gamma _ { 0 1 } - G _ { 0 } \xi _ { 1 } ) } } & { { = } } & { { \langle ( \partial _ { u _ { 0 1 } } ^ { 2 } \phi _ { 0 1 } ) v _ { 0 1 } , v _ { 0 1 } \rangle + 2 \langle ( \partial _ { u _ { 0 1 } } \partial _ { x _ { 1 } } \phi _ { 0 1 } ) \xi _ { 1 } , v _ { 0 1 } \rangle } } \\ { { } } & { { } } & { { - \langle \xi _ { 1 } , ( \partial _ { x _ { 1 } } \partial _ { u _ { 0 1 } } \phi _ { 0 1 } ) \Gamma _ { 0 } \xi _ { 1 } \rangle . } } \end{array}
$$

Similarly,

$$
\begin{array} { l c l } { { \Phi _ { 1 2 } ( \gamma _ { 1 2 } - { \cal G } _ { 2 } \xi _ { 1 } ) } } & { { = } } & { { \langle ( \partial _ { u _ { 1 2 } } ^ { 2 } \phi _ { 1 2 } ) v _ { 1 2 } , v _ { 1 2 } \rangle + 2 \langle ( \partial _ { u _ { 1 2 } } \partial _ { x _ { 1 } } \phi _ { 1 2 } ) \xi _ { 1 } , v _ { 1 2 } \rangle } } \\ { { } } & { { } } & { { - \langle \xi _ { 1 } , ( \partial _ { x _ { 1 } } \partial _ { u _ { 1 2 } } \phi _ { 1 2 } ) \Gamma _ { 2 } \xi _ { 1 } \rangle . } } \end{array}
$$

Subtract these two identities from the Hessian

$$
\begin{array} { r c l } { { \Phi _ { 0 2 } ( \gamma _ { 0 2 } ) } } & { { = } } & { { \langle ( \partial _ { u _ { 0 1 } } ^ { 2 } \phi _ { 0 1 } ) v _ { 0 1 } , v _ { 0 1 } \rangle + \langle ( \partial _ { u _ { 1 2 } } ^ { 2 } \phi _ { 1 2 } ) v _ { 1 2 } , v _ { 1 2 } \rangle } } \\ { { } } & { { } } & { { + 2 \langle ( \partial _ { u _ { 0 1 } \partial _ { x _ { 1 } } } \phi _ { 0 1 } ) \xi _ { 1 } , v _ { 0 1 } \rangle + 2 \langle ( \partial _ { u _ { 1 2 } \partial _ { x _ { 1 } } } \phi _ { 1 2 } ) \xi _ { 1 } , v _ { 1 2 } \rangle } } \\ { { } } & { { } } & { { + \langle ( \partial _ { x _ { 1 } } ^ { 2 } \phi _ { 0 1 } ) \xi _ { 1 } , \xi _ { 1 } \rangle + \langle ( \partial _ { x _ { 1 } } ^ { 2 } \phi _ { 1 2 } ) \xi _ { 1 } , \xi _ { 1 } \rangle . } } \end{array}
$$

and use the above formulae for $Q _ { 0 }$ and $Q _ { 2 }$ to prove the proposition.

# 3Examples

In our examples,except for the last one, the space $P$ is a space of paths and the work of the previous section can be interpreted formally. Alternatively one can introduce Hilbert manifold structures and generalize the previous work to the infinite dimensional case.

Example 3.1 Let $\boldsymbol { x }$ be a manifold and $L : \mathbb { R } \times T X  \mathbb { R }$ be a function. Fix $t _ { 0 } , t _ { 1 } \in \mathbb { R }$ and take $P _ { 0 1 } = P ( t _ { 0 } , t _ { 1 } )$ to be the space of all paths $c : [ t _ { 0 } , t _ { 1 } ] \to X$ Take $X _ { 0 } = X _ { 1 } = \nwarrow$ and define the projection $\pi = \pi _ { 0 1 }$ by evaluation at the endpoints:

$$
\pi ( c ) = ( c ( t _ { 0 } ) , c ( t _ { 1 } ) ) .
$$

The phase function $\phi = \phi _ { 0 1 }$ is the Lagrangian action integral

$$
\phi ( c ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } L ( t , c ( t ) , \dot { c } ( t ) ) d t
$$

from the calculus of variations.A tangent vector $\gamma \in T _ { c } P _ { 0 1 }$ is a vectorfield along $c$ and it is vertical iff it vanishes at the endpoints.A curve $c$ is a fiber critical point iff it satisfies the Euler-Lagrange equations

$$
\begin{array} { r } { \dot { y } = \partial _ { x } L , \qquad y = \partial _ { \dot { x } } L } \end{array}
$$

where $L = L ( t , x , \dot { x } )$ . The right side of Equation (2) consists of the boundary terms which result from the integration by parts in the derivation of the Euler-Lagrange equations. If $t _ { 1 }$ is replaced by $t$ and allowed to vary between $t _ { 0 }$ and $t _ { 1 }$ ，the restriction $c | [ t _ { 0 } , t ]$ is a fiber critical point of the new problem on $P ( t _ { 0 } , t )$ and the Lagrange mutiplier $y ( t )$ is the $y ( t )$ which appears in the Euler-Lagrange equations. When the Legendre transformation

$$
T X  T ^ { * } X : ( x , \dot { x } ) \mapsto ( x , y ) , \qquad y = \partial _ { \dot { x } } L
$$

is a diffeomorphism, the Euler-Lagrange equations take the form of Hamilton's equations

$$
\dot { x } = \partial _ { y } H , \qquad \dot { y } = - \partial _ { x } H
$$

where $H : T ^ { * } X \to \mathbb { R }$ is defined by eliminating $\dot { \pmb { x } }$ (via the Legendre transformation) from

$$
H ( t , x , y ) = \langle y , \dot { x } \rangle - L ( t , x , \dot { x } ) .
$$

Example 3.2 Specialize the previous example by taking $X$ a Riemannian manifold with energy function $L ( x , \dot { x } ) = { \textstyle \frac { 1 } { 2 } } | \dot { x } | _ { x } ^ { 2 }$ . Then the fiber critical points are the geodesics. The Hessian $\Phi = \Phi _ { 0 1 }$ is defined by

$$
\Phi ( \gamma ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } \langle ( W \gamma ) ( t ) , \gamma ( t ) \rangle _ { c ( t ) } d t
$$

where the operator $W$ is given by

$$
W \gamma = \frac { D ^ { 2 } \gamma } { d t ^ { 2 } } + R ( { \dot { c } } , \gamma ) { \dot { c } } .
$$

Here $D / d t$ denotes the covariant derivative along $c$ and $\gamma ( t ) \in T _ { c ( t ) } X$ . The linear second order differential equation $W \gamma = 0$ is the Jacobi equation. The geodesic is non-degenerate when its end points are not conjugate and the Green's function $G$ has its usual interpretation of assigning to the boundary conditions $\xi _ { 0 } \in T _ { x ( t _ { 0 } ) } X$ and $\xi _ { 1 } \in T _ { c ( t _ { 1 } ) } X$ the unique solution $\gamma = G ( \xi _ { 0 } , \xi _ { 1 } )$ of the boundary value problem

$$
W \gamma = 0 , \qquad \gamma ( t _ { 0 } ) = \xi _ { 0 } , \qquad \gamma ( t _ { 1 } ) = \xi _ { 1 } .
$$

Example 3.3 Again take $X _ { 0 } = X _ { 1 } = X$ but now take $\mathcal { P } ( t _ { 0 } , t _ { 1 } )$ the space of all curves

$$
c = ( x , y ) : [ t _ { 0 } , t _ { 1 } ] \to T ^ { * } X
$$

with projection $\pi = \pi _ { t _ { 0 } t _ { 1 } } : { \mathcal { P } } ( t _ { 0 } , t _ { 1 } ) \to X \times X$ given by

$$
\pi ( c ) = ( x ( t _ { 0 } ) , x ( t _ { 1 } ) ) .
$$

A time-dependent Hamiltonian $H : \mathbb { R } \times T ^ { * } X  \mathbb { R }$ determines a one-form $\pmb { \sigma } _ { H }$ on $\mathbb { R } \times T ^ { * } M$ via

$$
\sigma _ { H } = \langle y , d x \rangle - H d t
$$

called the action form of $H$ . Define the phase function $\phi = \phi _ { t _ { 0 } t _ { 1 } }$ to be the integral

$$
\phi ( c ) = \int _ { c } \sigma _ { H }
$$

of the action form along $c$ is called the action integral. A more explicit formula is

$$
\phi ( c ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } \Bigl ( \langle y , \dot { x } \rangle - H ( t , x , y ) \Bigr ) d t .
$$

where $c ( t ) = ( x ( t ) , y ( t ) )$ . As before the vertical critical points of $( \pi , \phi )$ are the solutions of the Euler-Lagrange equations of this functional. They are Hamilton's equations

$$
\dot { x } = \partial _ { y } H , \qquad \dot { y } = - \partial _ { x } H .
$$

The Lagrange multipliers in Equation (2) are given by $y _ { 0 } = y \big ( t _ { 0 } \big )$ and $y _ { 1 } =$ $y ( t _ { 1 } )$ . Assume for simplicity that these differential equations are complete. Then the symplectic relation determined by $\left( \pi _ { t _ { 0 } t _ { 1 } } , \phi _ { t _ { 0 } t _ { 1 } } \right)$ is $\mathrm { G r } \big ( \psi _ { t _ { 0 } } ^ { t _ { 1 } } \big )$ where $t \mapsto \psi _ { t _ { 0 } } ^ { t } ( x , y )$ is the solution of Hamilton's equations satisfying the initial condition $\psi _ { t _ { 0 } } ^ { t _ { 0 } } ( x , y ) = ( x , y )$ . These symplectomorphisms define an evolution system meaning that

$$
\psi _ { t _ { 1 } } ^ { t _ { 2 } } \circ \psi _ { t _ { 0 } } ^ { t _ { 1 } } = \psi _ { t _ { 0 } } ^ { t _ { 2 } } , \qquad \psi _ { t _ { 0 } } ^ { t _ { 0 } } = \mathbb { 1 } .
$$

Remark 3.4 Assume that $c _ { 0 }$ is a nondegenerate fiber critical point in the previous example. Then there is a local nonlinear Green's function which assigns to every point $\left( \pmb { x } _ { 0 } , \pmb { x } _ { 1 } \right)$ near $\pi ( c _ { 0 } )$ the unique solution $c ( t ) = ( x ( t ) , y ( t ) )$ near $c _ { 0 }$ of Hamilton's equation which satisfies ${ \pmb x } ( t _ { 0 } ) = { \pmb x } _ { 0 }$ and $\pmb { x } ( t _ { 1 } ) = \pmb { x } _ { 1 }$ .Let

$$
S _ { t _ { 0 } t _ { 1 } } ( x _ { 0 } , x _ { 1 } ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } \Bigl ( \langle y , \dot { x } \rangle - H ( t , x , y ) \Bigr ) d t
$$

denote the action integral of this solution. This is a local generating function of the symplectomorphism $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$

Remark 3.5 Now fix $t _ { 0 }$ and $\pmb { x _ { 0 } }$ . Then the generating function $S ( t , x ) =$ $S _ { t _ { 0 } t } ( x _ { 0 } , x )$ satisfies the Hamilton-Jacobi equation

$$
\partial _ { t } S + H ( t , x , \partial _ { x } S ) = 0 .
$$

To prove this diferentiate the identity

$$
S ( t , x ( t ) ) = \int _ { t _ { 0 } } ^ { t } \Bigl ( \langle y ( s ) , \dot { x } ( s ) \rangle - H ( s , x ( s ) , y ( s ) ) \Bigr ) d s
$$

with respect to $t$ and use $y = \partial S / \partial x$

Example 3.6 By a partition of $\pmb { \mathrm { R } }$ we mean an infinite discrete subset $\tau \subset { \mathbb { R } }$ extending to infinity in both directions.Every $t \in \tau$ has a unique successor $t ^ { + } \in \tau$ and predecessor $t ^ { - } \in \tau$ defined by

$$
t ^ { - } = \operatorname* { s u p } T \cap ( - \infty , t ) , \qquad t ^ { + } = \operatorname* { i n f } T \cap ( t , \infty ) .
$$

Denote the mesh of $\tau$ by

$$
\left| \mathcal { T } \right| = \operatorname* { s u p } _ { t \in \mathcal { T } } \left| t ^ { + } - t \right| .
$$

Now take $X = \pmb { \mathsf { R } } ^ { n }$ ， $T ^ { \ast } X = \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ ,and fix a time dependent Hamiltonian $H ( t , x , y )$ and a partition $\tau$ . Let $t _ { 0 } , t _ { 1 } \in \mathcal { T }$ with $t _ { 0 } < t _ { 1 }$ . Define the space

$$
\mathcal { P } ^ { T } ( t _ { 0 } , t _ { 1 } ) = \{ c = ( x , y ) : x : \mathcal { T } \cap [ t _ { 0 } , t _ { 1 } ] \to \mathbb { R } ^ { n } , y : \mathcal { T } \cap [ t _ { 0 } , t _ { 1 } ) \to \mathbb { R } ^ { n } \}
$$

of discrete paths in $\pmb { \mathbb { R } } ^ { 2 n }$ . These discrete paths are finite sequences of length $N$ and $N - 1$ where $N$ is the cardinality of the finite set $\mathcal { T } \cap [ t _ { 0 } , t _ { 1 } ]$ . The projection $\pi = \pi _ { t _ { 0 } t _ { 1 } } : { \mathcal { P } } ^ { T } ( t _ { 0 } , t _ { 1 } ) \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ is given by

$$
\pi ( c ) = ( x ( t _ { 0 } ) , x ( t _ { 1 } ) ) .
$$

The discrete action functional $\phi ^ { T } : \mathcal { P } ^ { T } ( t _ { 0 } , t _ { 1 } )  \mathbb { R }$ is defined by

$$
\phi ^ { T } ( c ) = \sum _ { \stackrel { t \in T } { t _ { 0 } \leq t < t _ { 1 } } } { \Bigl ( } \langle y ( t ) , x ( t ^ { + } ) - x ( t ) \rangle - H ( t , x ( t ^ { + } ) , y ( t ) ) ( t ^ { + } - t ) { \Bigr ) } .
$$

The vertical critical points of $( \pi ^ { T } , \phi ^ { T } )$ are the solutions of the discrete Hamiltonian equations

$$
\begin{array} { r l r } { x ( t ^ { + } ) - x ( t ) } & { = } & { \partial _ { y } H ( t , x ( t ^ { + } ) , y ( t ) ) ( t ^ { + } - t ) } \\ { y ( t ^ { + } ) - y ( t ) } & { = } & { - \partial _ { x } H ( t , x ( t ^ { + } ) , y ( t ) ) ( t ^ { + } - t ) . } \end{array}
$$

These equations define $( x ( t ^ { + } ) , y ( t ^ { + } ) )$ implicitly in terms of $( x ( t ) , y ( t ) )$ .Let $\left( y _ { 0 } , y _ { 1 } \right)$ be the Lagrange multipliers in equation (2). Then $y _ { 0 } = y ( t _ { 0 } )$ and $y _ { 1 } = y ( t _ { 1 } )$ is defined by equation (6).

Remark 3.7 Assume that $c _ { 0 } ^ { T }$ is a nondegenerate fiber critical point in the previous exampleand defineadiscrete generatingfunction $S _ { t _ { 0 } t _ { 1 } } ^ { T } \big ( x _ { 0 } , x _ { 1 } \big )$ as in the continuous case. Now fix a time interval $[ t _ { 0 } , t _ { 1 } ]$ ,let the mesh $| \tau |$ of the partition go to zero,and let $c _ { 0 } ^ { \mathcal { T } }$ converge to a nondegenerate fiber critical point of the continuous variational problem.Then we have a limit

$$
\operatorname* { l i m } _ { | T |  0 } S ^ { T } = S .
$$

This follows from standard arguments in the discretization of ordinary diferential equations.

# 4Hessians

We now compare the fiber Hessians in Examples 3.3 and 3.6. We take $X = \pmb { \mathbb { R } } ^ { n }$ and $T ^ { * } X = \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ . To simplify the notation we assume that for each $t$ the Hamiltonian $H ( t , x , y )$ is homogeneous quadratic in $( { \pmb x } , { \pmb y } )$ ：

$$
\begin{array} { r } { H ( t , x , y ) = \frac { 1 } { 2 } \langle H _ { x x } ( t ) x , x \rangle + \langle H _ { y x } ( t ) x , y \rangle + \frac { 1 } { 2 } \langle H _ { y y } ( t ) y , y \rangle } \end{array}
$$

where $H _ { x x } ( t ) , H _ { y x } ( t ) , H _ { y y } ( t )$ are $\mathscr { n } \times \mathscr { n }$ matrices with $H _ { x x }$ and $H _ { y y }$ symmetric. We abbreviate $H _ { x y } = H _ { y x } ^ { T }$

# Continuous time

In the continuous time case the fiber Hessian $\Phi = \Phi _ { t _ { 0 } t _ { 1 } }$ is given by

$$
\Phi ( \gamma ) = \langle W \gamma , \gamma \rangle
$$

for $\gamma = ( \xi , \eta ) : [ t _ { 0 } , t _ { 1 } ] \to \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ with $\xi ( t _ { 0 } ) = \xi ( t _ { 1 } ) = 0$ . The inner product on the right is the $L ^ { 2 }$ inner product and the fiber Hessian $W = W _ { t _ { 0 } t _ { 1 } }$ is the self-adjoint operator on $L ^ { 2 } ( [ t _ { 0 } , t _ { 1 } ] , \mathbb { R } ^ { n } \times \mathbb { R } ^ { n } )$ with dense domain

$$
\mathscr { W } ( t _ { 0 } , t _ { 1 } ) = H _ { 0 } ^ { 1 } ( [ t _ { 0 } , t _ { 1 } ] , \mathbb { R } ^ { n } ) \times H ^ { 1 } ( [ t _ { 0 } , t _ { 1 } ] , \mathbb { R } ^ { n } )
$$

given by $W ( \xi , \eta ) = ( u , v )$ where

$$
u = - \dot { \eta } - H _ { x x } \xi - H _ { x y } \eta , \qquad v = \dot { \xi } - H _ { y x } \xi - H _ { y y } \eta ,
$$

We call $W = W _ { t _ { 0 } t _ { 1 } }$ the second variation from $t _ { 0 }$ to $t _ { 1 }$ .By Proposition 1.3 the Hessian is nondegenerate if and only if the symplectomorphism $\psi _ { t _ { 0 } } ^ { t _ { 1 } }$ generated by $\pmb { H }$ admits a generating function.

# Discrete time

In discrete time we do the analogous thing. For $t _ { 0 } , t _ { 1 } \in \tau$ with $t _ { 0 } < t _ { 1 }$ define

$$
\begin{array} { r } { \mathcal { W } ^ { T } ( t _ { 0 } , t _ { 1 } ) = \left\{ { \gamma } = ( { \xi } , { \eta } ) \in \mathcal { P } ^ { T } ( t _ { 0 } , t _ { 1 } ) : { \xi } ( t _ { 0 } ) = { \xi } ( t _ { 1 } ) = 0 \right\} . } \end{array}
$$

This is a Hilbert space with the approximate $L ^ { 2 }$ -norm

$$
\| { \boldsymbol { \gamma } } \| _ { \mathcal { T } } ^ { 2 } = \sum _ { t _ { 0 } \leq t < t _ { 1 } } \left( | { \boldsymbol { \xi } } ( t ^ { + } ) | ^ { 2 } + | { \boldsymbol { \eta } } ( t ) | ^ { 2 } \right) ( t ^ { + } - t ) .
$$

In this case the fiber Hessian is the (finite dimensional) symmetric operator $W ^ { T } = W _ { t _ { 0 } t _ { 1 } } ^ { T } : \mathcal { W } ^ { T } ( t _ { 0 } , t _ { 1 } )  \mathcal { W } ^ { T } ( t _ { 0 } , t _ { 1 } )$ given by $W ^ { \tau } ( \xi , \eta ) = ( u , v )$ where

$$
u ( t ) = - \frac { \eta ( t ) - \eta ( t ^ { - } ) } { t - t ^ { - } } - H _ { x x } ( t ^ { - } ) \xi ( t ) - H _ { x y } ( t ^ { - } ) \eta ( t ^ { - } ) ,
$$

$$
v ( t ) = \frac { \xi ( t ^ { + } ) - \xi ( t ) } { t ^ { + } - t } - H _ { y x } ( t ) \xi ( t ^ { + } ) - H _ { y y } ( t ) \eta ( t ) .
$$

We call $W ^ { T } = W _ { t _ { 0 } t _ { 1 } } ^ { T }$ the discrete second variationfrom $t _ { 0 }$ t $t _ { 1 }$ By Proposition 1.3 the Hessian is nondegenerate if and only if the affine symplectomorphism $\phi _ { t _ { 0 } } ^ { t _ { 1 } }$ generated by the discrete Hamiltonian equations admits a generating function.

# Signature

The operator $W ^ { \tau }$ is defined on a finite dimensional space and hence has a well defined index (number of negative eigenvalues),coindex (number of positive eigenvalues),signature (coindex minus index),and nullity. For the operator W the index and coindex are both infinite and hence the signature is undefined. However, the signature of $W ^ { \tau }$ stabilizes when the mesh of the partition gets suffciently small. It is related to the Maslov index $\mu ( t _ { 0 } , t _ { 1 } , H )$ of the Hamiltonian flow (defined below) as follows.

Theorem 4.1 Assume that $W _ { t _ { 0 } t _ { 1 } }$ is non-degenerate. If the mesh $| \tau |$ is sufficiently small then

$$
\sin W _ { t _ { 0 } t _ { 1 } } ^ { \mathcal { T } } = 2 \mu ( t _ { 0 } , t _ { 1 } , H ) .
$$

Here is the definition of the Maslov index. Let $\ S _ { \mathbf { p } } ( 2 n )$ denote the symplectic group and ${ \widetilde { \mathsf { S p } } } ( 2 n )$ its universal cover. Think of an element of ${ \widetilde { \mathbf { S p } } } ( 2 n )$ covering $\Psi$ as a homotopy class of paths starting at $\mathbb { 1 }$ and ending at $\pmb { \Psi }$ . Define the Maslov cycle

$$
\Sigma = \{ \Psi \in \mathrm { S p } ( 2 n ) : \Psi \left( 0 \times \mathbf { R } ^ { n } \right) \cap \left( 0 \times \mathbf { R } ^ { n } \right) \neq \{ 0 \} \} ,
$$

and its complement

$$
\mathrm { S p } _ { 0 } ( 2 n ) = \mathrm { S p } ( 2 n ) \setminus \Sigma
$$

and denote by $\tilde { \Sigma }$ and ${ \widetilde { \mathsf { S p } } } _ { 0 } ( 2 n )$ the preimages under the covering map. For $\Psi _ { 1 0 } , \Psi _ { 2 1 } \in \mathrm { S p } _ { 0 } ( 2 n )$ let $Q ( \Psi _ { 2 1 } , \Psi _ { 1 0 } )$ denote the composition form of the pair $( \Psi _ { 1 0 } ( 0 \times \mathsf { R } ^ { n } ) , \Psi _ { 2 1 } ^ { - 1 } ( 0 \times \mathsf { R } ^ { n } ) )$ . If the matrices $\Psi _ { k j }$ are written in block matrix notation

$$
\Psi _ { k j } = { \left( \begin{array} { l l } { A _ { k j } } & { B _ { k j } } \\ { C _ { k j } } & { D _ { k j } } \end{array} \right) }
$$

then the composition form is given by

$$
Q = B _ { 2 1 } ^ { - 1 } B _ { 2 0 } B _ { 1 0 } ^ { - 1 } .
$$

Theorem 4.2 There is a unique locally constant map $\mu : { \widetilde { \mathrm { S p } } } _ { 0 } ( 2 n ) \to n / 2 + { \bf Z }$ such that

$$
\mu (  { \widetilde { \Psi } } _ { 2 0 } ) = \mu (  { \widetilde { \Psi } } _ { 2 1 } ) + \mu (  { \widetilde { \Psi } } _ { 1 0 } ) + \frac { 1 } { 2 }  { \mathrm { s i g n } } Q ( \Psi _ { 2 1 } , \Psi _ { 1 0 } )
$$

whenever $\tilde { \Psi } _ { 2 0 } = \tilde { \Psi } _ { 2 1 } \tilde { \Psi } _ { 1 0 }$ and $\tilde { \Psi } _ { k j }$ covers $\Psi _ { k j }$ .This is called the Maslov index.

The number $\mu (  { \tilde { \Psi } } )$ of Theorem 4.2 is essentially the intersection number of $\tilde { \Psi }$ with the Maslov cycle. The definition is modified to adjust for the fact that the curve $\tilde { \Psi }$ begins at the identity (which is an element of the Maslov cycle). For details see [19]. The number $\mu ( t _ { 0 } , t _ { 1 } , H )$ of Theorem 4.1 is the Maslov index of the curve $[ t _ { 0 } , t _ { 1 } ] \to \mathbf { S p } ( 2 n ) : t \mapsto \Psi _ { t _ { 0 } } ^ { t }$ defined by the evolution system generated by $\pmb { H }$

Remark 4.3 Suppose that the evolution system generated by the Hamiltonian $\pmb { H }$ isa symplectic shear

$$
\Psi _ { t _ { 0 } } ^ { t _ { 1 } } = \left( \begin{array} { c c } { \mathbb { 1 } } & { B ( t _ { 1 } , t _ { 0 } ) } \\ { 0 } & { \mathbb { 1 } } \end{array} \right) .
$$

Then $B ( t _ { 2 } , t _ { 0 } ) = B ( t _ { 2 } , t _ { 1 } ) + B ( t _ { 1 } , t _ { 0 } )$ and $B ( t _ { 0 } , t _ { 0 } ) = \mathbb { 1 }$ . The Maslov index is given by

$$
\begin{array} { r } { \mu ( t _ { 0 } , t _ { 1 } , H ) = - \frac { 1 } { 2 } \mathrm { s i g n } B ( t _ { 1 } , t _ { 0 } ) . } \end{array}
$$

For any two symmetric matrices $A , B$ such that $A , B , A + B$ ,and $A ^ { - 1 } + B ^ { - 1 }$ are nonsingular we have the signature identity

$$
\operatorname { s i g n } ( A ) + \operatorname { s i g n } ( B ) = \operatorname { s i g n } ( A + B ) + \operatorname { s i g n } ( A ^ { - 1 } + B ^ { - 1 } ) .
$$

This proves that the Maslov index as defined by intersection numbers satisfies the composition formula of Theorem 4.2 in the case of symplectic shears.The signature identity is obvious if the matrices are simultaneously diagonalizable. The general case can be proved with a homotopy argument.

Assume that $t _ { 0 } , t _ { 1 } , t _ { 2 } \in T$ are such that the Hessians $W _ { t _ { j } t _ { k } }$ are nondegenerate and denote by $Q ^ { \tau }$ the corresponding composition form as in equation (4). The composition forms $Q ^ { \tau }$ converge to the composition form $Q$ of the continuous time problem as the mesh $| \tau |$ tends to zero. If the mesh is sufficiently small then,by Proposition 2.2,

$$
\mathrm { s i g n } W _ { t _ { 0 } t _ { 2 } } ^ { T } = \mathrm { s i g n } W _ { t _ { 0 } t _ { 1 } } ^ { T } + \mathrm { s i g n } W _ { t _ { 1 } t _ { 2 } } ^ { T } + \mathrm { s i g n } Q ^ { T } .
$$

Thus the signature of the discrete second variation $W ^ { \tau }$ satisfies the composition formula of Theorem 4.2 and this can be used to prove Theorem 4.1. Alternatively one can prove Theorem 4.1 frst in the special case of a symplectic shear and then use a homotopy argument.

Remark 4.4 Theorem 4.2 is essentially due to Leray [16]. Leray's index $m ( { \tilde { \Psi } } )$ is related to ours by the formula

$$
m ( \widetilde { \Psi } ) = \mu ( \widetilde { \Psi } ) + \frac { n } { 2 } .
$$
