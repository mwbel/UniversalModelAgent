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

# 7 Representations

The group $\mathbf { E M p } ( 2 n )$ of all unitary operators of the form

$$
U = \mathcal { U } ( t _ { 1 } , t _ { 0 } , H )
$$

where $\pmb { H }$ runs over the time dependent quadratic Hamiltonians and $t _ { 1 } , t _ { 0 }$ range over the real numbers form a finite dimensional group called the extended metaplectic goup. The subgroup $\mathbf { M } _ { \mathbf { P } } ( 2 n )$ obtained by taking only

homogeneous quadratic Hamiltonians $\pmb { H }$ in (10) is called the metaplectic group. The subgroup $\operatorname { H G } ( 2 n )$ obtained by taking only affine Hamiltonians $H$ in (10) is called the Heisenberg group. By Theorem 5.2 the map

$$
\mathrm { E M p } ( 2 n ) \to \mathrm { E S p } ( W , \hbar ) : \mathcal { U } ( t _ { 1 } , t _ { 0 } , H ) \mapsto \mathfrak { g } _ { t _ { 0 } } ^ { t _ { 1 } } ( H )
$$

is a well-defined double cover (which depends on $\pmb { \hbar }$ ). This repesentation of the double cover of the symplectic group is called Siegel-Shale-Weil representation or the metaplectic representation. The restriction of the double cover to the Heisenberg group is injective and the resulting representation is called the Heisenberg representation.

Here is a more explicit description of the Heisenberg representation. If $H$ is an affine Hamiltonian with constant coefficients then

$$
\mathcal { U } ( t , t _ { 0 } , H ) = \mathcal { T } ( ( t - t _ { 0 } ) H )
$$

where

$$
\begin{array} { r } { \mathcal { T } ( H ) = e ^ { - i H _ { 0 } / \hbar - i \langle H _ { x } , x \rangle / \hbar + i \langle H _ { x } , H _ { y } \rangle / 2 \hbar } f ( x - H _ { y } ) . } \end{array}
$$

If $\pmb { \Psi }$ is a symplectic matrix then the map $H \mapsto T ( H \circ \Psi )$ is another such representation corresponding to the same value of Planck's constant $\pmb { \hbar }$ By the Stone-von Neumann theorem these representations are unitarily isomorphic. In other words there exists a unitary operator $U : L ^ { 2 } ( \mathbb { R } ^ { n } ) \to L ^ { 2 } ( \mathbb { R } ^ { n } )$ ,unique up to multiplication by a complex number of modulus 1,such that

$$
\mathcal { T } ( H \circ \Psi ) = U ^ { - 1 } \circ \mathcal { T } ( H ) \circ U .
$$

Such an intertwining operator $\boldsymbol { U }$ may be taken as a lift of $\Psi$ to the metaplectic group. This is apparently how the metaplectic representation was discovered (see [23]). The elements of the metaplectic representation are thus viewed as intertwining operators of various incarnations of the Heisenberg representation. See [20] for an exposition in terms of co-adjoint orbits and polarizations.

# 8Quantum field theory

By generalizing from affne symplectomorphisms to affine symplectic relations it should be possible to generalize the extended metaplectic representation to the extended metaplectic functor. An extended Lagrangian subspace is a Legendrian submanifold of $W$ which covers an affine Lagrangian subspace of $\pmb { \mathbb { R } } ^ { 2 n }$ . A quadratic function $S : \mathbb { R } ^ { n }  \mathbb { R }$ determines an extended Lagrangian subspace $L ( S )$ via

$$
L ( S ) = \{ ( x , y , u ) \in W : y = \partial _ { x } S ( x ) , \ u = e ^ { i S ( x ) / \hbar } \} .
$$

An element of the extended symplectic group can be interpreted as an extended Lagrangian subspace of the external tensor product $W ^ { * } \otimes W$ over $\bar { \mathsf { R } } ^ { 2 n } \times \mathsf { R } ^ { 2 n }$ .(The bar indicates that the sign of the symplectic form in the first factor is reversed.） More generally given circle bundles $W _ { 0 } \to \mathbb { R } ^ { 2 n _ { 0 } }$ and $W _ { 1 } \to \mathbb { R } ^ { 2 n _ { 1 } }$ as in Section 6 let $W _ { 0 1 } \to \bar { { \bar { \mathsf { R } } } } ^ { 2 n _ { 0 } } \times { \bar { { \mathsf { R } } } } ^ { 2 n _ { 1 } }$ be endowed with the connection form ${ \pmb { \alpha } } _ { 1 } - { \pmb { \alpha } } _ { 0 }$ . Then an extended symplectic relation is an extended Lagrangian subspace of $\bar { \mathsf { R } } ^ { 2 n _ { 0 } } \times \mathsf { R } ^ { 2 n _ { 1 } }$ . Extended Lagrangian subspaces appear as the special case $n _ { 0 } = 0$ . The extended metaplectic functor assigns to each extended symplectic relation a distribution on $\mathbb { R } ^ { n _ { 0 } } \times \mathbb { R } ^ { n _ { 1 } }$ ,determined by the relation only up to a sign,and respecting the operation of composition defined in section 2.In the case of an extended symplectomorphism $g _ { t _ { 0 } } ^ { t _ { 1 } } ( H )$ the distribution is the distribution kernel of $\mathcal { U } ( t _ { 0 } , t _ { 1 } , H )$ . For a quadratic generating function $S ( { \boldsymbol { x } } )$ the distribution is $e ^ { i S ( x ) / \hbar }$ multiplied by a normalizing factor. Composition of extended symplectic relations corresponds to composition of distribution kernels; there should be a formula like

$$
\mathcal { U } ( R _ { 0 1 } \# R _ { 1 2 } ) = \mathrm { t r } ( \mathcal { U } ( R _ { 0 1 } ) \otimes \mathcal { U } ( R _ { 1 2 } ) ) .
$$

The extended metaplectic functor should give a simple model of Segal's axioms for topological quantum field theory. Taking the homology of a Riemann surface as the underlying symplectic vector space should lead to a $( 2 + 1 )$ dimensional theory. This is what Atiyah calls the Abelian case (without the lattice).

# References

[1] S. Albevario and R. Hoegh-Krohn,Feynman path integrals and the corresponding method of stationary phase,in Feynman Path Integrals,ed. S. Albevario et al, Springer Lecture Notes in Physics 106 (1978) 3-57.   
[2] M.F.Atiyah,The Geometry and Physics of Knots, Cambridge University Press,1990.   
[3] C. Conley and E. Zehnder,The Birkhoff-Lewis fixed point theorem and a conjecture of V.I. Arnold, Invent.Math.73 (1983), 33-49.   
[4] C.C. Conley and E.Zehnder,Morse-type index theory for flows and periodic solutions of Hamiltonian equations, Commun. Pure Appl. Math. 37 (1984), 207-253.   
[5] I.Daubechies and J.R.Klauder,Quantum mechanical path integrals with Wiener measure for all polynomial Hamiltonians,Phys. Rev Letters 52 (1984) 1161; J. Math. Physics 26 (1985) 2239-2256.   
[6] I.Daubechies,J.R. Klauder,and T. Paul,Wiener measures for path integrals with affine kinematic variables,J.Math.Physics 28 (1987) 85- 102.   
[7] P.A.M. Dirac, The Lagrangian in quantum mechanics, Phys. Zeitschr.d. Sovyetunion 3 (1933) 64-72.   
[8] J.J. Duistermaat, On the Morse index in variational calculus,Advances in Mathematics 21 (1976),173-195.   
[9] R.P. Feynman, Space-time approach to non-relativistic quantum mechanics,Rev. Mod.Phisics 20 (1948),367-387.   
[10] R.P. Feynman and A.R. Hibbs, Quantum Mechanics and Path Integrals, MacGraw-Hill,1965.   
[11] V. Guillemin and S. Sternberg, Geometric Asymptotics, AMS Math Surveys 14,1977.   
[12] V. Guillemin and S. Sternberg, Symplectic Techniques in Physics, Cambridge University Press,1984.   
[13] L. Hormander,Fourier integral operators I, Acta Math.127 (1971),79- 183.   
[14] J.B. Keller, Corrected Bohr-Sommerfeld quantum conditions for nonseparable systems,Annals of Physics 4 (1958),180-188.   
[15] B. Kostant,Quantization and unitary representations,in Modern Analysis and its Applications Springer Lecture Notes in Math 170 (1970) 87-207.   
[16] J.Leray, Lagrangian Analysis and Quantum Mechanics,MIT press,1981.   
[17] J.W.Robbin and D.A. Salamon,Path integrals on phase space and the metaplectic representation,Preprint,1992.   
[18] J.W.Robbin,and D.A.Salamon, The spectral fow and the Maslov index, Preprint 1992.   
[19] J.W. Robbin,and D.A. Salamon, A Maslov index for paths, Preprint 1992.   
[20] P.L. Robinson and J.H. Rawnsley, The metaplectic representation, $M p ^ { c }$ structures and geometric quantization ,Memoirs of the American Mathematical Society 81,1989.

[21] D. Salamon and E. Zehnder，Morse theory for periodic solutions of Hamiltonian systems and the Maslov index, to appear in Comm.Pure Appl. Math.

[22] I.E.Segal, Foundations of the theory of dynamical systems of infinitely many degrees of freedom (I)，Mat. Fys.Medd. Danske Vid. Selsk. 31 (1959) 1-39.

[23] IE. Segal, Transforms for operators and symplectic automorphisms over a locally compact abelian group,Math. Scand.13 (1963) 31-43.

[24] D.Shale,Linear symmetries of free boson felds, Trans. AMS 103 (1962), 149-167.

[25] J.M. Souriau, Structures des Systemes Dynamiques, Dunod,Paris,1970.

[26] J.M. Souriau, Construction explicite de 'indice de Maslov. Group Theoretical Methods in Physics Springer Lecture Notes in Physics 50 (1975), 117-148.

[27] A. Weil, Sur certaine groupes d'operateurs unitaires,Acta math 111 (1964),143-211.

[28] A. Weinstein, Lectures on Symplectic Manifolds, AMS Reg. Conf. Ser. Math. 29,1977.

# Symplectic Mappings which are Stable at Infinity Eduard Zehnder Eidg. Technische Hochschule, Zürich

# 1.A stability problem

If $\varphi$ is a symplectic diffeomorphism of $\pmb { \mathbb { R } } ^ { 2 n }$ ,i.e.

$$
\varphi ^ { * } \sigma = \sigma ,
$$

for the standard symplectic form $\pmb { \sigma }$ on $\pmb { R } ^ { 2 n }$ given by $\sigma ( \xi , \eta ) = \langle \xi , J \eta \rangle$ for $\ b { \xi } , \ b { \eta } \in \mathbb { R } ^ { 2 n }$ ，one would like to study the orbits $\mathcal { O } ( z ) = \{ \varphi ^ { j } ( z ) ~ | ~ j ~ \in \mathbb { Z } \}$ of the points $z \in \mathbb { R } ^ { 2 n }$ under all the iterates of $\varphi$ It is,of course, well known that the structure of all orbits of a symplectic mapping is extremely intricate; for a recent illustration of the complexity of the orbit structure for a symplectic mapping locally near an elliptic fixed point in the plane we point out C.Genecand [17]. It is, therefore,natural to search for special orbits only such as fixed points or periodic points.But instead of looking for special orbits we shall look for mappings $\varphi$ which have the property that all their orbits are bounded,i.e.

$$
\operatorname* { s u p } _ { j \in \mathbb { Z } } \left| \varphi ^ { j } ( z ) \right| < \infty \quad { \mathrm { f o r ~ a l l } } \quad z \in \mathbb { R } ^ { 2 n } .
$$

The statement (2) can be viewed as a qualitative stability statement namely the stability of a fictitious fxed point at infinity.

The symplectic mappings considered in the following will be rather special. They belong to the flow $\varphi ^ { t }$ of a time dependent Hamiltonian vectorfield on $\pmb { R } ^ { 2 n }$ defined by a time dependent Hamiltonian function $H ( t , z )$ ，where $t \in \mathbb { R }$ is the time and $z \in \mathbb { R } ^ { 2 n }$ . The fow is the solution of the initial value problem

$$
\begin{array} { c } { { { \frac { d } { d t } } \varphi ^ { t } ( z ) = J \nabla H \left( t , \varphi ^ { t } ( z ) \right) } } \\ { { \varphi ^ { 0 } ( z ) = z ~ , } } \end{array}
$$

so that every map $\varphi ^ { t }$ preserves the symplectic structure $\pmb { \sigma }$ ,i.e. $( \varphi ^ { t } ) ^ { * } \sigma = \sigma$ In case that the timedependence is periodic,for example $H ( t + 1 , z ) =$ $H ( t , z )$ ，we take $\varphi$ to be the time one map $\varphi ^ { 1 }$ of the flow,so that

$$
\varphi ^ { n } = \varphi \circ \varphi \circ \ldots \circ \varphi
$$

is the $\pmb { n }$ -times iterated map. If $H$ is independent of the time $t$ then we have $H { \bigl ( } \varphi ^ { t } ( z ) { \bigr ) } = H ( z )$ for all $t$ and all $z \in \mathbb { R } ^ { 2 n }$ . Consequently the stability (2) follows provided,for example,all the subsets $H ( z ) = { \mathrm { c o n s t } }$ are bounded. If,however, the function $H$ depends on time,the energy is not conserved anymore and the stability question is rather subtle.

# 2. Results for $\pmb { \cal R } ^ { 2 }$

For a symplectic mapping stability under al iterates can, in general, only be expected for maps on $\pmb { \cal R } ^ { 2 }$ and we therefore consider first the case $\boldsymbol { z } = ( x , y ) \in \mathbb { R } ^ { 2 }$ .Moreover,we look at the restricted class of Hamiltonian functions which describe so called "classical systems”, namely

$$
H ( t , x , y ) = \frac { 1 } { 2 } y ^ { 2 } + V ( t , x ) .
$$

Setting $\pmb { y } = \pmb { \dot { x } }$ , the corresponding Hamiltonian equation (2) is equivalent to the second order equation on the real line:

$$
\ddot { x } + V _ { x } ( t , x ) = 0 , \qquad x \in \mathbb { R } .
$$

The quest for potentials $V ( t , x )$ having the property that all the solutions ${ \pmb x } ( t )$ of (6)are bounded for all times was already emphasized by J.E.Littlewood.He constructed counter-examples of the form

$$
\ddot { x } + V _ { x } ( x ) = p ( t ) ,
$$

which possess unbounded solutions for forcing terms $p ( t )$ which are periodic in time but which are not continuous; we refer to M. Levi [3] and Y. Long [4].

If the timedependence is more intimately involved in the nonlinearity it is,of course,not even clear that the flow does exist over an infinite interval of time. Indeed C.V. Coffman and D.F. Ullrich [18] constructed an example, namely

$$
\ddot { x } + a ( t ) x ^ { 3 } = 0
$$

where $a ( t + 1 ) = a ( t )$ is periodic, continuous and even close to a positive constant,such that there are solutions blowing up in a time interval shorter than the period. In their example ${ \pmb a } ( t )$ is,however, not of bounded variation.

It should be recalled that the first positive result is due to G.R.Morris [7],who proved the stability statement (2) for the equation

$$
\ddot { x } + x ^ { 3 } = p ( t )
$$

with a continuous and time periodic forcing $p ( t )$ . His proof, based on J. Moser's twist theorem [14],gave rise to farreaching extensions to more general potentials $V ( t , x )$ ,which are sufficiently smooth and which depend periodically on the time $V ( t + 1 , x ) = V ( t , x )$ ，we refer for example to R. Dieckerhoff and E. Zehnder [8],M.Levi [11],S.Laederich and M. Levi [6], J. Norris [9] and Liu Bin [5].

In contrast to the time periodic forcing we are interested in the following in potentials $\boldsymbol { V }$ which depend quasiperiodically on the time.We therefore assume that

$$
V ( t , x ) = F ( \omega _ { 1 } t , \dots , \omega _ { N } t , x ) \ ,
$$

where $\omega = ( \omega _ { 1 } , \ldots , \omega _ { N } ) \in \bar { \mathsf { R } } ^ { N }$ is a given constant vector, the so called frequencies,and where $F ( \xi _ { 1 } , \dots , \xi _ { N } , x )$ is periodic with period 1 in every variable $\xi _ { j }$ ,so that $F ( \cdot , x )$ is a function on the torus $\pmb { T } ^ { N }$ . We shall use the abbreviating notation $V ( \omega t , x )$

The frequencies $\omega$ are assumed not only to be rationally independent but to satisfy,in addition,the diophantine conditions (D.C.)

$$
| \langle \omega , j \rangle | \geq \gamma | j | ^ { - \tau } \quad \mathrm { ~ f o r ~ a l l ~ } j \in { \bf Z } ^ { N } \backslash \{ 0 \} \ : ,
$$

with two constants $\tau > N$ and $\gamma > 0$ . Recall that almost every $\boldsymbol \omega \in \mathbb { R } ^ { N }$ meets these inequalities.

That stability is possible for quasiperiodic potentials will be illustrated for potentials having the following special form

$$
V ( \omega t , x ) = \sum _ { j = 1 } ^ { 2 d + 2 } a _ { j } ( \omega t ) x ^ { j } \ , d \geq 1
$$

where all the coefficients ${ \pmb a } _ { j }$ are quasiperiodic in time with frequencies $\omega$ ， and where, in addition,the leading coefficient $\pmb { a } \equiv \pmb { a } _ { 2 d + 2 }$ is positive

$$
{ a ( \omega t ) \geq \operatorname* { m i n } _ { \xi \in T ^ { N } } a ( \xi ) > 0 } .
$$

For this class of potentials the following rather surprising stability statement holds true:

Theorem 1．[1] Let $\varphi ^ { t } ( z )$ be the flow of the Hamiltonian system defined by the function $\begin{array} { r } { H ( t , z ) = \frac { 1 } { 2 } y ^ { 2 } + V ( \omega t , x ) } \end{array}$ where $\boldsymbol { z } = ( x , y ) \in \mathbb { R } ^ { 2 }$ ,and where $V$ is quasiperiodic in time $t$ satisfying (i1),(12) and (13). Assume that

$$
a _ { j } \in C ^ { k } ( T ^ { N } ) , \quad k > 4 \tau + 6
$$

for all $1 \leq j \leq 2 d + 2$ ,then

$$
\operatorname* { s u p } _ { t \in \mathbb { R } } \left. \varphi ^ { t } ( z ) \right. < \infty
$$

for every $z \in \mathbb { R } ^ { 2 }$

The smoothness requirement on $V$ necessary for the stability depends only on the number of underlying frequencies $\omega$ but not on the degree of $V$ as a polynomial in $\pmb { x }$ .

# 3. Sketch of the proof of theorem 1

The proof uses a well known technique: in order to get bounds for all solutions one proves the existence of quasiperiodic solutions using the fact that the phase space is $\pmb { \cal R } ^ { 2 }$ . Geometrically the idea is as follows. One writes the equation (6) as a system on the extended phase space $( x , y , t ) \in \mathbb { R } ^ { 3 }$ ：

$$
\begin{array} { l } { \dot { x } = y } \\ { \dot { y } = - V _ { x } ( \omega t , x ) } \\ { \dot { t } = 1 . } \end{array}
$$

By $X$ we abbreviate the vectorfield on $\pmb { \nabla } ^ { 3 }$ defined by the right hand side. The idea now is to construct for every $C > 0$ sufficiently large,an embedded cylinder $w : Z = \mathbb { R } \times S ^ { 1 } \to \mathbb { R } ^ { 3 }$

$$
w : ( t , s ) \longmapsto ( u ( t , s ) , t )
$$

containing the time axis in the interior,contaied in $A _ { C } = \{ ( x , y , t ) \in \mathbb { R } ^ { 3 } \ \vert$ $x ^ { 2 } + y ^ { 2 } \geq C ^ { 2 } \}$ and satisfying

$$
C < \operatorname* { i n f } _ { z } | u | < \operatorname* { s u p } _ { z } | u | < \infty
$$

and which,moreover, is tangential to the vectorfield $X$ on $\pmb { \mathbb { R } } ^ { 3 }$ . Therefore the surface $w ( z )$ is invariant under the fow $\scriptstyle ( \varphi ^ { t } ( z ) , t )$ of $X$ . If a solution $( z ( t ) , t )$ satisfies $| z ( t ^ { * } ) | \leq C$ for some $t ^ { * } \in \mathbb { R }$ then it follows by the invariance of the cylinder and by the uniqueness of O.D.E. that the solution $z ( t )$ exists for all time $\pmb { t } \in \pmb { \mathbb { R } }$ and satisfies,in view of (16), $| z ( t ) | \leq \operatorname* { s u p } u < \infty$ for $\pmb { t } \in \pmb { \mathbb { R } }$ ， so that $z ( t )$ is indeed bounded.

The existence of these invariant surfaces in $\pmb { \mathbb { R } } ^ { 3 }$ is a consequence of the observation that in the region $A _ { C }$ for large $c$ the system (14) can be viewed as a system close to an integrable one.For such systems the KAM theory is applicable. The techniques involved require an excessive amount of smoothness of the equation,as is well known. The near integrability is,on the other hand, not a priori obvious and its proof is one of the main tasks in prving theorem 1.

In order to make the required near integrability visible one uses transformation theory of time dependent Hamiltonian equations: firstly one rescales the time and the $\pmb { x }$ -variable appropriately, then one introduces action and angle variables and,after a further finite sequence of canonical transformations one finds the Hamiltonian in the following form,suitable to apply the analytical techniques.On the annulus $( \varphi , I ) \in S ^ { 1 } \times D$ ，where $D = \{ I \mid a \leq I \leq b \} \subset \mathbb { R }$ is a bounded interval, the Hamiltonian is given by the function

$$
\begin{array} { r } { H ( \varepsilon \omega t , \varphi , I , \varepsilon ) = H _ { 0 } ( I , \varepsilon ) + \varepsilon ^ { 3 } H _ { 1 } ( \varepsilon \omega t , \varphi , I , \varepsilon ) . } \end{array}
$$

Here $\varepsilon > 0$ is a small parameter,and the integrable part $H _ { 0 }$ satisfies the so called twist condition

$$
C < \frac { \partial ^ { 2 } H _ { 0 } } { \partial I ^ { 2 } } ( I , \varepsilon ) < C ^ { - 1 } , I \in { \cal D }
$$

for a constant $C > 0$ which is independent of $\varepsilon$

One is confronted with the analytical problem of finding,for every $\varepsilon > 0$ sufficiently small,a quasiperiodic solution contained in $S ^ { 1 } \times D$ having prescribed $1 + N$ frequencies $\left( \alpha , \varepsilon \omega \right) \in \mathbb { R } ^ { 1 + N }$ for an appropriate $\begin{array} { r } { \alpha = \frac { \partial H _ { 0 } } { \partial I } \overline { { ( I , \varepsilon ) } } } \end{array}$ To be more precise,recalling that $H = H ( \xi , \varphi , I , \varepsilon )$ is periodic in $\bar { \boldsymbol { \xi } } \in \boldsymbol { T } ^ { N }$ and $\varphi \in S ^ { 1 }$ one looks for a differentiable map

$$
w : T ^ { 1 + N } \longrightarrow S ^ { 1 } \times D ,
$$

$w ( \vartheta , \xi ) = \big ( u ( \vartheta , \xi ) , v ( \vartheta , \xi ) \big )$ and $u ( \vartheta , \xi ) - \vartheta , v ( \vartheta , \xi )$ periodic in $\vartheta , \xi$ ，which maps the constant vectorfield $\pmb { V }$ on $T ^ { 1 + N }$ defined by

$$
\dot { \vartheta } = \alpha , \quad \dot { \xi } = \varepsilon \omega ,
$$

into the given Hamiltonian vectorfield; i.e.

$$
d w \left( { \boldsymbol { \alpha } } _ { } \right) = J \nabla H \left( \xi , w ( \vartheta , \xi ) , \varepsilon \right)
$$

for all $\vartheta , \xi \in T ^ { 1 + N }$ ， It then follows that $\pmb { w }$ maps the solutions of $\pmb { V }$ into the required quasiperiodic solutions $z ( t ) = w ( \alpha t , \varepsilon \omega t )$ of the Hamiltonian equation defined by the function (16). In particular the cylinder $\hat { w } : \mathcal { S } ^ { 1 } \times$ $\pmb { \mathsf { R } }  S ^ { \mathbf { 1 } } \times D \times \pmb { \mathsf { R } }$ defined by $\hat { w } ( \vartheta , t ) = ( w ( \vartheta , \varepsilon \omega t ) , t )$ consists of solutions of the Hamiltonian vectorfield and hence is the required invariant surface leading to the bounds we are looking for.

The existence of solutions of the P.D.E. (21) uses J. Moser's technique in[13] together with the improvements,crucial for our regularity,in D. Salamon [15] and in D.Salamon and E. Zehnder [16]. For the technical details of the proof we refer to [1].

Summarizing,the stability is concluded from the fact that a dominant part of the phase space $\pmb { \cal R } ^ { 2 }$ for $| z |$ large is covered by quasiperiodic solutions. In particular we can state

Theorem 2. [1] The equation

$$
\ddot { x } + V _ { x } ( \omega t , x ) = 0 , \quad x \in \mathbb { R }
$$

with the potential $\boldsymbol { V }$ satisfying the assumptions of theorem 1 possesses uncountably many quasiperiodic solutions having $1 + N$ frequencies $( \alpha , \omega )$ satisfying the D.C.:

$$
| \alpha \cdot k + \langle \omega , j \rangle | \geq \gamma ( | k | + | j | ) ^ { - \tau }
$$

for all $( k , j ) \in Z ^ { 1 + N } \backslash \{ 0 \}$ with the constants $\gamma$ and $\pmb { \tau }$ as in (11).

For a related perturbation problem this statement was already conjectured by $\mathbf { v }$ .Arnold [21] in the early sixties.Finally it should be said that the ideas of this section lead to the stability for a relatively large class of quasiperiodic potentials,see [1].

# 4. Dropping the quasiperiodicity

As a sideremark we mention that as soon as the requirement on the recurrent nature of the time forcing is omitted unbounded solutions may show up for forcing terms which are small, smooth and tending to zero as time gives to infinity. The following simple example of instability illustrates this.

Proposition. [1] Given any $\varepsilon > 0$ and $\pmb { r } \in \mathbb { N }$ there exists a function $p \in C ^ { \infty } ( \pmb { \mathsf { R } } )$ satisfying

$$
| p | _ { C ^ { r } } \leq \varepsilon \quad \mathrm { a n d } \quad \operatorname* { l i m } _ { t  \infty } D ^ { j } p ( t ) = 0
$$

for $0 \leq j \leq r - 1$ ,such that the equation

$$
{ \ddot { x } } + x ^ { 3 } = p ( t ) , \qquad x \in \mathbb { R }
$$

possesses an unbounded solution ${ \pmb x } ( t )$ . Moreover,the growth rate of this solution is given by

$$
C \leq t ^ { - a } E ( t ) \leq C ^ { - 1 } , a = { \frac { 4 } { 2 r + 3 } } ,
$$

$t \geq 1$ , for a constant $C > 0$ ,where $\begin{array} { r } { E ( t ) = \frac { 1 } { 2 } \dot { x } ( t ) ^ { 2 } + \frac { 1 } { 4 } x ( t ) ^ { 4 } } \end{array}$ is the energy of the solution ${ \pmb x } ( t )$ . On the other hand the decay rate of the forcing is given by

$$
\operatorname* { s u p } _ { t > 0 } t ^ { b } \left| D ^ { j } p ( t ) \right| < \infty , b = \frac { 2 ( r - j ) } { 2 r + 3 }
$$

for $0 \leq j \leq r - 1$

For the elementary proof we refer to [1].

# 5. Exponential stability in higher dimensions

Turning to the stability question in higher dimensions we consider on the special phase space $( x , y ) \in T ^ { n } \times \mathsf { R } ^ { n }$ the Hamiltonian system defined by

$$
H ( \omega t , x , y ) = \frac { 1 } { 2 } \left| y \right| ^ { 2 } + V ( \omega t , x ) ,
$$

where $V = V ( \xi , x )$ is a function on $T ^ { N } \times T ^ { n }$ . In sharp contrast to the equations in section 2,the system is already given in action and angle variables. Since $\boldsymbol { V }$ is bounded,the system is in the region where $| y |$ is large near an integrable one. This allows again to conclude many quasiperiodic solutions having prescribed frequencies $( \lambda , \omega ) \in \mathbb { R } ^ { n } \times \mathbb { R } ^ { N }$ . To this end one solves the nonlinear P.D.E.

$$
d w \binom { \lambda } { \omega } = J \nabla H \big ( \xi , w ( \xi , x ) \big ) ,
$$

$( \xi , x ) \in T ^ { N } \times T ^ { n }$ , for a map $w : T ^ { N } \times T ^ { n }  \mathbb { R } ^ { n } \times T ^ { n }$ which is, for every fixed $\pmb { \zeta } \in \pmb { T } ^ { N }$ , an embedding $w ( \xi , \cdot ) : T ^ { n } \to T ^ { n } \times \mathbb { R } ^ { n }$ . For the existence proof which requires,of course,diophantine conditions on the frequencies and a suffcient amount of smoothness for the potential we refer to L.Chierchia and E. Zehnder [10].

We point out that there is no smallness assumption on the potential $V$ , instead the frequency vector $| \lambda |$ has to be chosen sufficently large.

In the special case $n = 1$ one concludes,as above, immediately the stability of all pendulum like equations with potentials $V ( t , x )$ which are periodic in $\pmb { x }$ and periodic or quasiperiodic in the time $t$ ，provided only $\boldsymbol { V }$ is sufficiently smooth.

Theorem 3. [10] [11] [12] Let $\varphi ^ { t } \bigl ( x ( 0 ) , y ( 0 ) \bigr ) = \bigl ( x ( t ) , y ( t ) \bigr )$ be the flow of the Hamiltonian system on $S ^ { 1 } \times \Vec { \mathbf { R } }$ belonging to the function (22） for $\pmb { n = 1 }$ .If $\omega$ satisfies D.C. and if $\pmb { V }$ is suffciently smooth,then

$$
\operatorname* { s u p } _ { t \in \mathbb { R } } | y ( t ) | < \infty
$$

for every $y ( 0 ) \in \pmb { \mathbb { R } }$

Although there exists an abundance of quasiperiodic and so bounded solutions, they do not lead to bounds for all solutions if $\pmb { n } > 1$ ，since the invariant surfaces covered by these solutions do not bound open sets.Recall now that N.N.Nekhoroshev [19] discovered estimates for the action variables of all solution not over the whole time but over an exponentially long interval of time for systems near integrable systems,provided the Hamiltonian is not only smooth, but real analytic and provided the corresponding integrable system meets convexity type conditions. One might therefore conjecture that such estimates hold true also for our global problem. Indeed the following statement of exponential stability replaces Theorem 3 in higher dimensions.

In order to formulate the result we assume $V ( x , t )$ to be real analytic on $T ^ { n } \times \mathbf { R }$ and moreover to have a holomorphic extension to a complex strip $| \mathrm { I m } x | < \sigma$ and $\left| \operatorname { I m } t \right| < \sigma$ for some $\pmb { \sigma } > \mathbf { 0 }$ such that

$$
\begin{array} { r } { | V | _ { \sigma } : = \underset { | \operatorname { I m } x | < \sigma } { \operatorname* { s u p } } | V ( x , \xi ) | < \infty . } \end{array}
$$

No periodicity or quasiperiodicity in $t$ is required. The following statement of exponential stability replaces (1.4) in higher dimensions.

Theorem 4. [2] Let $\varphi ^ { t } \bigl ( x ( 0 ) , y ( 0 ) \bigr ) = \bigl ( x ( t ) , y ( t ) \bigr )$ be the flow on $T ^ { n } \times \mathsf { R } ^ { n }$ of the Hamiltonian vectorfield corresponding to:

$$
\begin{array} { r } { H ( x , y , t ) = \frac { 1 } { 2 } \left| y \right| ^ { 2 } + V ( x , t ) . } \end{array}
$$

Assume that the potential $V = V ( x , \xi )$ is real analytic on $T ^ { n } \times \pmb { \mathbb { R } }$ and has,moreover,an analytic extension to a complex strip satisfying (24). Then there are positive constants $\pmb { T } ^ { \star }$ and $\pmb { R } ^ { \star }$ depending on $| V | _ { \sigma } , \sigma$ and the dimension $\pmb { n }$ such that for every $\rho \geq ( R ^ { * } ) ^ { \frac { 1 } { \alpha } }$

$$
| y ( t ) - y ( 0 ) | \le \rho
$$

for all $\pmb { t }$ in

$$
\left| t \right| \leq T ^ { * } e ^ { \frac { 1 } { R ^ { * } } \cdot \rho ^ { \alpha } } , \ \alpha = \frac { 2 } { n ^ { 2 } + n } \ ,
$$

where $\begin{array} { r } { T ^ { * } = \frac { \sigma } { \left| V \right| _ { \sigma } } \cdot { \left( \frac { 1 + e ^ { - \sigma } } { 1 - e ^ { - \sigma } } \right) } ^ { - n } , } \end{array}$

The assumptions are met for example if $V ( x , \omega t )$ depends quasiperiodically on $t$ provided $V ( x , \xi )$ is real analytic on $T ^ { n } \times T ^ { N }$

There is no smallness requirement on $\boldsymbol { V }$ ，the potential,however,is required to be more than real analytic quite in contrast to theorem 1.The proof uses the underlying ideas of N. Nekhoroshev [19] and of G. Benettin, L. Galgani and A. Giorgilli in [20] and we refer to [2] for the details.

6. References   
[1] M.Levi and E. Zehnder: Boundedness of solutions for quasiperiodic potentials,to be published.   
[2] A.Giorgilli and E. Zehnder: Exponential stability for quasiperiodic potentials,to be published.   
[3] M.Levi: A note on Littlewood's counter example, preprint FIM, ETH Zurich (1989).   
[4] Y. Long: Unbounded solution of a superlinear Duffing-equation, preprint Nankai University Tianjin (1989).   
[5] Lin Bin: Boundedness for solutions of nonlinear Hil's equations with periodic forcing terms via Moser's Twist Theorem,J.Diff. Eq.79 (1989), 304-315.   
[6] S.Laederich and M. Levi: Invariant curves and time-dependent potentials,preprint F.I.M.,ETH Zürich (1989).   
[7] G.R. Morris: A case of boundedness in Litlewood's problem on oscillatory differential equations,Bull． Austr. Math. Soc.14(1976), 71-93.   
[8] R.Dieckerhoff and E. Zehnder: Boundedness of solutions via the twist theorem.Ann. Scuola Norm. Sup.Pisa 14 (1987),79-95.   
[9] J.W. Norris: Boundedness in periodically forced second order conservative systems. Preprint University College of Wales,Aberystwyth (1989).   
[10] L. Chierchia and E. Zehnder: Asymptotic expansions of quasiperiodic solutions. Annali della Sc. Norm. Sup. Pisa Series IV, vol XVI (1989), 245-258.   
[11] M. Levi: Quasiperiodic motions in superquadratic time periodic potentials.Preprint BU (1990).   
[12] J. Moser: Quasiperiodic solutions of nonlinear partial differential equations.Bol. Soc. Bras.Mat.20 (1989),29-45.   
[13] J.Moser: On the construction of almost periodic solutions for ordinary differential equations.Proc. Int. Conf.Functional Analysis and related topics,Tokyo (1969),60-67.   
[14] J.Moser: On invariant curves of area preserving mappings of an annulus. Nachr. Akad. Wiss. Gotingen,Math.-Phys.Kl. II (1962), 1-20.   
[15] D.Salamon: The Kolmogorov-Arnold-Moser theorem.Preprint F.I.M. of the ETH Zürich (1986).   
[16] D. Salamon and E. Zehnder: KAM theory in configuration space, Comm.Math.Helv.64 (1989),84-132.   
[17] C.Genecand: Transversal homoclinic points near elliptic fixed points of area preserving diffeomorphisms of the plane,to appear in Dynamics Reported (1991).   
[18] C.V. Coffman and D.F. Ullrich: On the continuation of solutions of a certain non-linear differential equation,Monatshefte fur Mathematik 71 (5) 1967,385-392.   
[19] N.N. Nekhoroshev: Exponential estimate of the stability in time of near-integrable Hamiltonian systems,Russ. Math. surveys 32 (6) 1977, 1-65.   
[20] G.Benettin,L. Galgani, A. Giorgilli: A proof of Nekhoroshev's theorem for the stability times in nearly integrable Hamiltonian systems,Cel. Mechanics 37 (1985),1-25.   
[21] V.I. Arnold: On the behaviour of an adiabatic invariant under slow periodic variation of the Hamiltonian． Transl. Sov. Math．Dokl.3 (1961),136-140.