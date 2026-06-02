# Chapter 12. Poisson Bracket and Lie–Poisson Schemes

In this chapter, a clear Lie–Poisson Hamilton–Jacobi theory is presented. It is also shown how to construct a Lie–Poisson scheme integrator by generating function, which is different from the Ge–Marsden[GM88] method.

# 12.1 Poisson Bracket and Lie–Poisson Systems

Before introducing the Lie–Poisson system, let us first review more general about the Poisson system.

# 12.1.1 Poisson Bracket

Take a system with finite dimensions as an example. Give a manifold $M$ and two smooth functions $F , G$ on $M$ , i.e., $F , G \in C ^ { \infty } ( M )$ . If an operation $\{ \cdot , \cdot \}$ defined on $C ^ { \infty } ( M )$ satisfies the following 4 properties, then $\{ \cdot , \cdot \}$ is called Poisson bracket, and $( M , \{ \cdot , \cdot \} )$ is called Poisson manifold $\left[ \mathrm { O l v } 9 3 \right]$ .

# 1. Bilinearity

$$
\begin{array} { r } { \{ a F _ { 1 } + b F _ { 2 } , H \} = a \{ F _ { 1 } , H \} + b \{ F _ { 2 } , H \} , } \\ { \{ } \\ { F , a H _ { 1 } + b H _ { 2 } \} = a \{ F , H _ { 1 } \} + b \{ F , H _ { 2 } \} . } \end{array}
$$

2. Skew-Symmetry

$$
\{ F , H \} = - \{ H , F \} .
$$

3. Jacobi Identity

$$
\{ \{ F , H \} , G \} + \{ \{ H , G \} , F \} + \{ \{ G , F \} , H \} = 0 .
$$

# 4. Leibniz Rule

$$
\{ F _ { 1 } \cdot F _ { 2 } , H \} = F _ { 1 } \{ F _ { 2 } , H \} + F _ { 2 } \{ F _ { 1 } , H \} .
$$

Given a Hamiltonian function $H \in C ^ { \infty } ( M )$ , the induced equation

$$
\dot { F } = \{ F , H \} , \quad \forall F \in C ^ { \infty } ( M )
$$

is called the generalized Hamiltonian equation. The most general case of Hamiltonian system is the one with symplectic structure, whose equations have the form:

$$
{ \dot { z } } = J H _ { z } , \quad J = { \left[ \begin{array} { l l } { O } & { I } \\ { I } & { O } \end{array} \right] } , \quad z = { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } .
$$

According to Darboux theorem, a general Poisson system with finite dimensions can be transformed into a local coordinate form, whose equations may be written as

$$
\begin{array} { r } { \dot { z } = K ( z ) H _ { z } , } \end{array}
$$

the corresponding Poisson bracket is

$$
\{ F , H \} = ( \nabla _ { z } F ( z ) ) ^ { \mathrm { T } } K ( z ) \nabla _ { z } H ( z ) , \quad \forall F , H \in C ^ { \infty } ( M ) .
$$

$K ( z )$ satisfies 4 properties the above , if and only if $K ( z ) = ( k _ { i j } ( z ) )$ satisfies

$$
k _ { i j } ( z ) \frac { \partial k _ { l m } ( z ) } { \partial z _ { i } } + k _ { i l } ( z ) \frac { \partial k _ { m j } } { \partial z _ { i } } + k _ { i m } ( z ) \frac { \partial k _ { j l } } { \partial z _ { i } } = 0 , \quad j , l , m = 1 , 2 , \cdot \cdot , n .
$$

We remark that any antisymmetry constant matrix satisfies (1.2) and hence is a Hamiltonian operator, and the bracket defined by it is a Poisson bracket. We will discuss its algorithm in more detail in the next section.

Definition 1.1. A diffeomorphism $z  { \widehat { z } } = g ( z ) : M  M$ is called a Poisson mapping, if it preserves the Poisson bracket, i.e.,

$$
\{ F \circ g , H \circ g \} = \{ F , H \} \circ g , \quad \forall F , H \in C ^ { \infty } ( M ) .
$$

Theorem 1.2. For a Poisson manifold with structure matrix $K ( z )$ , Equation (1.3) is equivalent to

$$
g _ { z } K ( z ) g _ { z } ^ { \mathrm { T } } = K ( \widehat { z } ) ,
$$

where $g _ { z }$ is the Jacobian matrix of $g$ with respect to $z$ .

Proof.

$$
\begin{array} { l } { \{ F \circ g , H \circ g \} } \\ { = \ ( F \circ g ) _ { z } K ( z ) ( H \circ g ) _ { z } ^ { \mathrm { T } } } \\ { = \ F _ { z } ( g ( z ) ) \frac { \partial g } { \partial z } K ( z ) \left( \frac { \partial g } { \partial z } \right) ^ { \mathrm { T } } \left( H _ { z } ( g ( z ) \right) ^ { \mathrm { T } } } \\ { = \ F _ { z } ( g ( z ) ) \frac { \partial \mathbf { \Psi } } { \partial z } K ( z ) \left( \frac { \partial g } { \partial z } \right) ^ { \mathrm { T } } \left( \nabla H \circ g \right) , } \end{array}
$$

and

$$
\{ F , H \} \circ g = \nabla F ^ { \mathrm { T } } K \nabla H ( g ( z ) ) = ( \nabla F \circ g ) ^ { \mathrm { T } } K ( g ( z ) ) ( \nabla H \circ g ) .
$$

By comparison, we get

$$
g _ { z } ( z ) K ( z ) ( g _ { z } ( z ) ) ^ { \mathrm { T } } = K ( g ( z ) ) = K ( \widehat { z } ) .
$$

The theorem is proved.

A Hamiltonian system on a Poisson manifold usually refers to the following ODEs

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { K } ( \boldsymbol { z } ) \nabla \boldsymbol { H } ( \boldsymbol { z } ) ,
$$

where $H ( z )$ is a Hamiltonian function.

The phase flow of the Equation (1.4), which is expressed as $g ^ { t } ( z ) = g ( t , z ) =$ $g _ { H } ( t , z )$ , is a one parameter diffeomorphism group (at least locally), i.e.,

$$
g ^ { 0 } = \mathrm { i d e n t i t y } , \quad g ^ { t _ { 1 } + t _ { 2 } } = g ^ { t _ { 1 } } \circ g ^ { t _ { 2 } } .
$$

Theorem 1.3. The phase flow $g _ { H } ( z , t )$ of the Hamiltonian system (1.4) is a one parameter group of Poisson maps, i.e.,

$$
\{ F \circ g ( z , t ) , G \circ g ( z , t ) \} = \{ F , G \} \circ g ( z , t ) .
$$

Proof. $\mathrm { S e e } ^ { \mathrm { [ O l v 9 3 ] } }$ .

By Theorem 1.2, we get

$$
g _ { z } ( z , t ) K ( z ) ( g _ { z } ( z , t ) ) ^ { \mathrm { T } } = K ( g ( z ) ) .
$$

Definition 1.4. A smooth function $C ( z )$ is called a Casimir function, if

$$
\{ C ( z ) , F ( z ) \} = 0 , \quad \forall F \in C ^ { \infty } ( M ) .
$$

Definition 1.5. $F ( z ) \in C ^ { \infty } ( M )$ is a first integral of Hamiltonian system, iff $\{ F , H \} =$ 0. Obviously, every Casimir function is a first integral.

# 12.1.2 Lie–Poisson Systems

The Lie–Poisson system is a $\mathrm { t y p e ^ { [ M W 8 3 , M R 9 9 ] } }$ of common Poisson systems. Its structure space is the dual space of any Lie algebra, and its bracket is called Lie–Poisson bracket. There are two types of definition for the Lie–Poisson bracket: one relies on the coordinate definition, and the other does not rely on the coordinate definition.

Lie–Poisson bracket. Let $\mathbf { g }$ be a $r$ -dimensional Lie algebra, $C _ { i j } ^ { k } \left( i , j , k = 1 , 2 , \cdot \cdot \cdot , r \right)$ be the configuration constants of $\mathbf { g }$ w.r.t. basis $v _ { 1 } , v _ { 2 } , \cdots , v _ { r }$ . Let $V$ be another $r$ - dimensional linear space, with coordinate $x = ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { r } )$ . Then Lie–Poisson bracket is defined by:

$$
\{ F , H \} = \sum _ { i , j , k = 1 } ^ { r } C _ { i j } ^ { k } x ^ { k } \frac { \partial F } { \partial x _ { i } } \frac { \partial H } { \partial x _ { j } } , \quad \forall F , H \in C ^ { \infty } ( \mathbf { R } ) .
$$

According to the notation of the Poisson system

$$
k ^ { i j } ( x ) = \sum _ { l = 1 } ^ { r } C _ { i j } ^ { l } x ^ { l } .
$$

It is easy to verify that $\{ F , H \}$ satisfies the 4 properties of a Poisson bracket. For the infinite dimensional evolution equations, there exists a corresponding coordinate definition; see the literatures[Arn89,MR99] .

Lie group action and momentum mapping. The Lie–Poisson system is closely related to the Hamiltonian system with symmetry.

Definition 1.6. The invariant property of a Hamiltonian system under one parameter differomorphism group is called symmetry of the Hamiltonian system. Under certain circumstance, this invariant property is called momentum. The corresponding mapping is called momentum mapping.

The Lie group, action on manifold $M , \forall g \in G$ , and corresponds to a self-homeomorphism $\phi _ { g }$ on $M$ . Below, we consider only the translation action of $G$ on itself and the induced action on $_ { T G }$ and $T ^ { * } G$ .

Definition 1.7. Infinitesimal generator vector field: let $\mathbf { g }$ be a Lie algebra of $G , \xi \in \mathbf { g }$ , then exp $t \xi \in G$ ,

$$
\xi _ { M } = \frac { \mathrm { d } } { \mathrm { d } t } \bigg \vert _ { t = 0 } \phi _ { \exp { t } \xi } ( x ) , \quad x \in M
$$

is called infinitesimal generator vector field of the flow $F _ { t } = \phi _ { \mathrm { e x p } ~ t \xi }$

Definition 1.8 (Lifted action). Action $\phi _ { g } \ : \ M \to \ M$ may induce action $\widetilde { \phi } _ { g }$ : $T ^ { * } M \to T ^ { * } M$ , which is defined as follows:

$$
\begin{array} { r } { \widetilde { \phi } _ { g } ( \alpha ) = T ^ { * } \phi _ { g ^ { - 1 } } = ( T ^ { * } \phi _ { g } ) ^ { - 1 } ( \alpha ) , \quad \alpha \in T _ { \phi ( g ) } ^ { * } ( x ) . } \end{array}
$$

Thus, we can prove that the lifted mapping of a diffeomorphism is symplectic.

Definition 1.9 (Momentum mapping). Let $( P , \omega )$ be a connected symplectic manifold. Let $G$ be a Lie group, $\phi _ { g } : P \to P$ a symplectic action. We call $\mathcal { I } : P \to { \bf g } ^ { * } ( { \bf g } ^ { * }$ is the dual space of $\mathrm { g }$ ) a momentum mapping, if $\mathcal { I }$ satisfies

$$
\forall \xi \in \mathbf { g } , \quad \mathrm { d } \widehat { \mathcal { I } } ( \xi ) = i _ { \xi _ { p } } \omega ,
$$

where $\widehat { \mathcal { I } } ( \xi )$ is defined by $\widehat { \mathcal { I } } ( \xi ) ( x ) = \langle \mathcal { I } ( x ) , \xi \rangle , \langle \cdot , \cdot \rangle$ denotes a scalar product, and $\xi _ { p }$ is the infinitesimal generator of the action to $\xi$ .

Theorem 1.10 (Generalized Noether theorem). Let $\phi$ be a symplectic action of $G$ on $( P , \omega )$ with a momentum mapping $\mathcal { I }$ . Suppose $H : P \to \mathbf { R }$ is $G$ -invariant, i.e.,

$$
H ( x ) = H ( \phi _ { g } ( x ) ) , \quad \forall x \in P , \quad g \in G ,
$$

then $\widehat { \mathcal { I } }$ is a first integral of $X _ { H }$ , i.e., if $F _ { t }$ is the phase flow of $X _ { H }$ , then

$$
\mathcal { I } ( F _ { t } ( x ) ) = \mathcal { I } ( x ) .
$$

Proof. See[MW83] .

Definition 1.11. A momentum mapping $\mathcal { I }$ is called $A d ^ { * }$ -equivariant, if

$$
\mathcal { I } ( \phi _ { g } ( x ) ) = A d _ { g ^ { - 1 } } ^ { * } \mathcal { I } ( x ) , \quad \forall g \in G ,
$$

that is, the following diagram commutes

$$
\begin{array} { r } { \begin{array} { r l r } & { P } & { \xrightarrow { \phi _ { g } } } \\ & { \mathcal { I } \Big \downarrow } \\ & { \mathcal { I } \Big \downarrow } \\ & { \mathbf { g } ^ { * } } & { \xrightarrow { A d _ { g ^ { - 1 } } ^ { * } } \mathbf { g } ^ { * } } \end{array} } \end{array}
$$

and we call such a group action as a Poisson action[AN90] .

Theorem 1.12. [MR99] $\mathcal { I }$ is $A d ^ { * }$ -equivariant momentum mapping, iff

$$
\{ \widehat { \mathcal { I } } ( \xi ) , \widehat { \mathcal { I } } ( \eta ) \} = \widehat { \mathcal { I } } ( [ \xi , \eta ] ) ,
$$

i.e., $\widehat { \mathcal { I } }$ is a Lie homomorphism.

Corollary 1.13. Let $\phi$ be a Poisson action of $G$ on the manifold $M$ , and $\widetilde { \phi }$ be the lifted action on $T ^ { * } ( M ) = P$ . Then this action $\widetilde { \phi }$ is symplectic and has an $A d ^ { * }$ -equivariant momentum mapping given by

$$
\mathcal { I } : \ : P \longrightarrow g ^ { * } , \quad \widehat { \mathcal { I } } ( \xi ) ( \alpha ( q ) ) = \alpha ( q ) \cdot \xi _ { M } ( q ) , \quad q \in M , \quad \alpha ( q ) \in T ^ { * } M .
$$

$\xi _ { M }$ is the infinitesimal generator of $\phi$ on $M$

Below, we will discuss the translation action of a Lie group on itself using the above theorem and deduction.

Let $G$ be a Lie group, $\phi : G \times G \to G$ be a left translation action $( g , h ) \to g h$ . Then its infinitesimal generator is

$$
\xi _ { G } ( g ) = T _ { e } R _ { g } \xi = R _ { g } ^ { * } \xi .
$$

Because lifted action is symplectic, by Corollary 1.13, we can obtain the momentum mapping:

$$
\mathcal { I } ( \alpha _ { q } ) ( \xi ) = \alpha _ { q } T _ { e } R _ { g } \xi = \alpha _ { q } R _ { g } ^ { * } \xi \Longrightarrow \mathcal { I } ( \alpha _ { q } ) = T _ { e } R _ { g } ^ { * } \alpha _ { q } = R _ { g } ^ { * } \alpha _ { q } ,
$$

or can rewrite it as

$$
\begin{array} { r } { \mathcal { I } _ { L } ( \alpha _ { q } ) = R _ { g } ^ { * } \alpha _ { q } . } \end{array}
$$

Likewise, we can obtain the similar result for the right translation

$$
\begin{array} { r } { \mathcal { I } _ { R } ( \alpha _ { q } ) = L _ { g } ^ { * } \alpha _ { q } . } \end{array}
$$

Lie–Poisson bracket and motion equation. In the previous sections, we have introduced the Lie–Poisson bracket and equations which are expressed by the local coordinates. Below, we will introduce an intrinsic definition of Lie–Poisson bracket and its induced equation of motion.

Let $\langle \cdot , \cdot \rangle$ be the pairing between $\mathbf { g } ^ { * }$ and $\mathbf { g } , \forall F \colon \mathbf { g } ^ { * } \to \mathbf { R } , { \frac { \delta F } { \delta \mu } } \in \mathbf { g } , \mu \in \mathbf { g } ^ { * } ,$ is defined by

$$
\mathrm { { D } } F ( \mu ) \gamma = \Big \langle \gamma , \frac { \delta F } { \delta \mu } \Big \rangle , \quad \gamma \in \mathbf { g } ^ { * } .
$$

If we regard $\mathbf { g } ^ { * * } \simeq \mathbf { g }$ , then $\mathsf { D } F ( \mu ) \in \mathsf { g } ^ { * * }$ becomes an element of $\mathbf { g }$ ,

$$
\{ F , G \} ( \mu ) = - \bigg \langle \mu , \Big [ \frac { \delta F } { \delta \mu } , \frac { \delta G } { \delta \mu } \Big ] \bigg \rangle ,
$$

where $[ \cdot , \cdot ]$ is the Lie bracket on g. The above equation is usually denoted as $\{ F , G \}$ . It is easy to verify that $\{ \cdot , \cdot \}$ satisfies the 4 properties of Poisson bracket, and are often called as $( \langle \langle - \rangle \rangle )$ Lie–Poisson bracket. They are first proposed by $\mathrm { L i e ^ { \left[ \mathrm { L i e 8 8 } \right] } }$ and are redefined by Berezin and others thereafter. We can prove that $\{ \cdot , \cdot \}$ can be derived from the left translation reduction of a typical Poisson bracket on $T ^ { * } G$ . If the right translation reduction is used, we have the Lie–Poisson bracket $\langle \langle + \rangle \rangle )$ :

$$
\{ F , G \} ( \mu ) = \Big \langle \mu , \Big [ \frac { \delta F } { \delta \mu } , \frac { \delta G } { \delta \mu } \Big ] \Big \rangle = \{ F , G \} _ { + } .
$$

Given a Lie–Poisson bracket, we can define the Lie–Poisson equation. Take $\{ \cdot , \cdot \}$ as an example.

Proposition 1.14. If $H _ { - } \in C ^ { \infty } ( \mathbf { g } ^ { * } )$ is a Hamiltonian function, then the evolutionary equation on $\mathbf { g } ^ { * }$ is:

$$
\dot { F } = \{ F , H \} _ { - } ,
$$

i.e.,

$$
\dot { \mu } = X _ { H _ { - } } ( \mu ) = a d _ { \frac { \delta H } { \delta \mu } } ^ { * } \mu .
$$

Proof. Because

$$
{ \dot { F } } ( \mu ) = D F ( \mu ) \cdot { \dot { \mu } } = \Big \langle { \dot { \mu } } , \frac { \delta F } { \delta \mu } \Big \rangle ,
$$

and

$$
\{ F , H _ { - } \} _ { - } ( \mu ) = - \Big \langle \mu , \Big [ \frac { \delta F } { \delta \mu } , \frac { \delta H } { \delta \mu } \Big ] \Big \rangle = \Big \langle \mu , a d _ { \frac { \delta H } { \delta \mu } } \frac { \delta F } { \delta \mu } \Big \rangle = \Big \langle a d _ { \frac { \delta H } { \delta \mu } } ^ { * } \mu , \frac { \delta F } { \delta \mu } \Big \rangle .
$$

Since $F$ is arbitrary, we obtain

$$
\begin{array} { r } { \dot { \mu } = a d _ { \frac { \delta H } { \delta \mu } } ^ { \ast } \mu . } \end{array}
$$

Likewise, for the right invariant system, the equation is

$$
\begin{array} { r } { \dot { \mu } = - a d _ { \frac { \delta H } { \delta \mu } } ^ { \ast } \mu . } \end{array}
$$

Henceforth, we will denote the system of left translation reduction as $\mathbf { g } _ { + } ^ { * }$ , and the right translation reduction as $\mathrm { g } _ { - } ^ { * }$ . Generally speaking, the rigid body and Heavy top system belongs to the left invariant system $\mathbf { g } _ { - } ^ { * }$ , and the continuous systems, such as plasma and the incompressible flow, are right invariant system $\mathbf { g } _ { + } ^ { * }$ . -

Lemma 1.15. $\mathcal { I } _ { L }$ , $\mathcal { I } _ { R }$ are Poisson mapping.

Proof. $\mathrm { S e e } ^ { \mathrm { [ M W 8 3 ] } }$ .

From this lemma, we can obtain the following reduction theorem (it will be used in the generating function theory later).

Theorem 1.16. $1 ^ { \circ }$ For the left invariant system $\mathrm { g _ { - } ^ { \ast } }$ , we have the following diagram commutes:

$$
\begin{array} { r l } { T ^ { * } G } & { { } \xrightarrow { G _ { H \circ \mathcal { I } _ { R } } ^ { t } } \ T ^ { * } G } \\ { \mathcal { I } _ { R } \Big \downarrow } & { { } \mathcal { I } _ { R } \Big \downarrow } \\ { \mathrm { g } _ { - } ^ { * } } & { { } \xrightarrow { G _ { H } ^ { t } } \quad \mathrm { g } _ { - } ^ { * } } \end{array}
$$

where ${ \cal H } : g ^ { * }  { \bf R }$ is a Hamiltonian function on $\mathbf { g } _ { - } ^ { * }$ , $G _ { H } ^ { t }$ is a phase flow of Hamiltonian function $H$ on $\mathbf { g } _ { - } ^ { * }$ , and $G _ { H \circ \mathcal { I } _ { R } } ^ { t }$ − is phase flow of Hamiltonian function $H \circ \mathcal { I } _ { R }$ on $T ^ { * } G$ .

$2 ^ { \circ }$ Similarly for right invariant system $\mathbf { g } _ { + } ^ { * }$ , we have

$$
\begin{array} { r l } { T ^ { * } G } & { { } \xrightarrow { G _ { H \circ \mathcal { I } _ { L } } ^ { t } } \ T ^ { * } G } \\ { \mathcal { I } _ { L } \Big \downarrow } & { { } \qquad \mathcal { I } _ { L } \Big \downarrow } \\ { g _ { + } ^ { * } } & { { } \xrightarrow { G _ { H } ^ { t } } \quad g _ { + } ^ { * } } \end{array}
$$

Theorem 1.17. The solutions of a Lie–Poisson system are a bundle of coadjoint orbits. Each coadjoint orbit is a symplectic manifold and is called symplectic leave of the Lie–Poisson system.

This theorem is from literature[AM78] . For Lie–Poisson system such as Heavy Top and the compressible flows, similar set of theories can be established. The readers can refer to literature[MRW90] for more details.

# 12.1.3 Introduction of the Generalized Rigid Body Motion

Let $G$ be a Lie group (finite dimensional), $g ( t )$ be a movement on $G$ . We define:

Velocity: $V ( t ) = \dot { g } ( t ) \in T _ { g ( t ) } G$ ;

Angular velocity in body description: $W _ { B } ( t ) = T L _ { g ( t ) ^ { - 1 } } ( \dot { g } ( t ) ) \in \mathfrak { g } ;$

Angular velocity in space description: $W _ { S } ( t ) = T R _ { g ( t ) ^ { - 1 } } ( \dot { g } ( t ) ) \in \mathfrak { g } ;$

Momentum : $\begin{array} { r } { M ( t ) = A _ { g } \dot { g } } \end{array}$ , where $A _ { g } : T _ { g } G \to T _ { g } ^ { * } G$ is called a moment of inertia operator, it relates to the kinetic energy by

$$
T = \frac 1 2 ( \dot { g } , \dot { g } ) _ { g } = \frac 1 2 ( W _ { B } , W _ { B } ) = \frac 1 2 \langle A W _ { B } , W _ { B } \rangle = \frac 1 2 \langle A _ { g } \dot { g } , \dot { g } \rangle ,
$$

where $A \colon \mathbf { g } \to \mathbf { g } ^ { * }$ is a value of $A _ { g }$ at $g = e$ ;

Angular momentum in body description: $M _ { B } ( t ) = T ^ { * } R _ { g ( t ) } ( M ( t ) ) \in \mathbf { g } ^ { * }$ ;   
Angular momentum in space description: $M _ { S } ( t ) = T ^ { * } L _ { g ( t ) } ( M ( t ) ) \in \mathfrak { g } ^ { * }$ .

From the above definition, we can obtain the following conclusions:

$$
W _ { S } ( t ) = A d _ { g ( t ) } W _ { B } ( t ) , \quad M _ { S } ( t ) = A d _ { g ( t ) ^ { - 1 } } ^ { * } M _ { B } ( t ) , \quad M _ { B } ( t ) = A W _ { B } ( t ) .
$$

By Theorem 1.10, we get:

Theorem 1.18. Conservation of spatial angular momentum theorem

$$
\frac { \mathrm { d } } { \mathrm { d } t } M _ { S } ( t ) = 0 .
$$

Because the system that takes kinetic energy $T$ as the Hamiltonian function is left invariant, $M _ { S } ( t )$ is the momentum mapping exactly.

# Corollary 1.19. Euler equation

$$
\frac { \mathrm { d } } { \mathrm { d } t } M _ { B } ( t ) = \{ W _ { B } ( t ) , M _ { B } ( t ) \} = \{ A ^ { - 1 } M _ { B } ( t ) , M _ { B } ( t ) \} ,
$$

where $\{ \cdot , \cdot \}$ is defined by:

$$
\{ \xi , a \} = a d _ { \xi } ^ { * } a , \quad \forall \xi \in g , a \in g ^ { * } .
$$

Given below are two different proofs of the Euler equation.

Proof. $1 ^ { \circ }$ From the Lie–Poisson equation of the motion $\dot { \mu } = a d _ { \frac { \partial H } { \partial \mu } } ^ { * } \mu$ , we can obtain directly

$$
H = \frac { 1 } { 2 } ( W _ { B } ( t ) , M _ { B } ( t ) ) = \frac { 1 } { 2 } \big ( A ^ { - 1 } M _ { B } ( t ) , M _ { B } ( t ) \big ) ,
$$

$$
{ \frac { \delta H } { \delta M _ { B } } } = A ^ { - 1 } M _ { B } ( t ) = W _ { B } ( t ) .
$$

$2 ^ { \circ }$ By the definition of spatial angular momentum, we have

$$
M _ { B } ( t ) = A d _ { g ( t ) } ^ { * } A d _ { g ( 0 ) ^ { - 1 } } ^ { * } M _ { B } ( 0 ) = A d _ { g ( t ) } ^ { * } \eta .
$$

Since

$$
M _ { S } ( t ) = M _ { S } ( 0 ) \Longrightarrow A d _ { g ( t ) ^ { - 1 } } ^ { * } M _ { B } ( t ) = A d _ { g ( 0 ) ^ { - 1 } } ^ { * } M _ { B } ( 0 ) = \eta .
$$

This also indicates that the trajectory of Lie–Poisson equation lies in some coadjoint orbit. From

$$
\langle M _ { B } ( t ) , \xi \rangle = \langle A d _ { g ( t ) } ^ { * } \eta , \xi \rangle = \langle \eta , A d _ { g ( t ) } \xi \rangle , \quad \forall \xi \in { \bf g } ,
$$

taking time derivatives on two sides, we get

$$
\left. \frac { \mathrm { d } M _ { B } ( t ) } { \mathrm { d } t } , \xi \right. = \left. \eta , [ T R _ { g ( t ) ^ { - 1 } } ( \dot { g } ( t ) ) , A d _ { g ( t ) } \xi ] \right. ,
$$

since

$$
\frac { \textrm { d } } { \textrm { d } t } A d _ { g ( t ) } \xi = [ T R _ { g ( t ) ^ { - 1 } } \dot { g } ( t ) , A d _ { g ( t ) } \xi ]
$$

$( \mathrm { s e e } ^ { \mathrm { [ A M 7 8 ] } } )$ , then

$$
\begin{array} { l l l } { \left. \frac { { \mathrm { d } } M _ { B } ( t ) } { { \mathrm { d } } t } , \xi \right. } & { = } & { \left. \eta , \left[ T R _ { g ( t ) } - \dot { y } ( t ) , A d _ { g ( t ) } \xi \right] \right. } \\ & { = } & { \left. \eta , A d _ { g ( t ) } [ T L _ { g ( t ) } - \dot { y } ( t ) , \xi ] \right. } \\ & { = } & { \left. A d _ { g ( t ) } ^ { * } \eta , a d _ { T L _ { g ( t ) } - 1 } \dot { y } ( t ) \xi \right. } \\ & { = } & { \left. M _ { B } ( t ) , a d _ { T L _ { g ( t ) } - 1 } \dot { y } ( t ) \xi \right. } \\ & { = } & { \left. a d _ { T L _ { g ( t ) } - 1 } ^ { * } \dot { y } ( t ) ^ { M } B ( t ) , \xi \right. } \\ & { \implies \frac { { \mathrm { d } } M _ { B } ( t ) } { { \mathrm { d } } t } = a d _ { T L _ { g ( t ) } - 1 } ^ { * } \dot { y } ( t ) ^ { M } B ( t ) = \left\{ W _ { B } ( t ) , { M } _ { B } ( t ) \right\} . } \end{array}
$$

The proof can be obtained.

Generally speaking, an equation of motion on $T ^ { * } G$ , if it has Hamiltonian function $H = T$ , it can be expressed by

$$
\begin{array} { r c l } { { \dot { g } ( t ) ~ = ~ T L _ { g ( t ) } \frac { \partial H } { \partial \mu } = L _ { g ( t ) ^ { * } } \frac { \partial H } { \partial \mu } , } } \\ { { \dot { \mu } ( t ) ~ = ~ a d _ { \frac { \partial H } { \partial \mu } } ^ { * } \mu ( t ) . } } \end{array}
$$

Its solution is $\mu ( t ) = A d _ { g ( t ) } ^ { * } A d _ { g ( 0 ) ^ { - 1 } } ^ { * } \mu ( 0 )$ . The Equation (1.14) is called as the Lie– Poisson equation.

# 12.2 Constructing Difference Schemes for Linear Poisson Systems

Since the phase flow of Hamiltonian system is Poisson phase flow, which preserves the Poisson structure, it is important to construct difference schemes for system (1.4) that preserve the same property. Difference scheme that preserves the Poisson bracket is called as the Poisson difference scheme.

One special case of the Poisson phase flow is the symplectic phase flow. How to construct the symplectic difference schemes has already been described in the previous chapters. The reader can also refer to literatures[Fen85,FWQW89,FQ87,CS90] for more details. However, the numerical algorithm for a general Poisson phase flow is still in its infancy. So far the results are limited to cases where structure matrix $K$ is constant $[ \mathrm { W a n } \dot { 9 } 1 , Z \mathrm { Q } 9 4 , \mathrm { A K W } 9 3 , \mathrm { K a r } 0 4 ]$ and $K ( z )$ is linear (Lie–Poisson) only. We will discuss the results for the Lie–Poisson case in the next section. In this section, we will discuss the results when $K$ is a constant matrix.

# 12.2.1 Constructing Difference Schemes for Linear Poisson Systems

Without loss of generality, we assume that $K$ is an odd-dimensional matrix. Because odd dimensional antisymmetric matrix is definitely degenerated, there exists a coordinate transformation $P \in G L ( n )$ such that $P K P ^ { \mathrm { { T } } } = \left[ \begin{array} { c c } { J _ { 2 r } } & { O } \\ { O } & { O _ { s } } \end{array} \right] .$ .

Definition 2.1. A difference scheme $\widehat z = g _ { H } ^ { \tau } ( z )$ is called a Poisson scheme, if and only if $g _ { z } K g _ { z } ^ { \mathrm { T } } = K$ .

Next, we have:

Definition 2.2. $S _ { K } ( n ) = \{ A \in G L ( n ) \mid A K A ^ { \mathrm { T } } = K \}$ , then the set $S _ { K } ( n )$ has the following properties:

$1 ^ { \circ }$ When the rank of $K$ is an even number and non-singular, then $K$ has all the properties of a symplectic matrix.

$2 ^ { \circ }$ When the rank of $K$ is an odd number, it must be degenerated. It is easy to verify that $S _ { K } ( n )$ is a group and we call it as $K$ -symplectic group. Its Lie algebra is

$$
s _ { K } ( n ) = \{ a \in g l ( n ) \mid a K + K a ^ { \operatorname { T } } = 0 \} .
$$

According to Feng et al. $[ \mathrm { F W Q 9 0 } ]$ , we can establish the relationship between $S _ { K } ( n )$ and $s _ { K } ( n )$ via Cayley transformation. If $A \in S _ { K } ( n )$ , namely if $A K A ^ { \mathrm { T } } = K$ , then

$$
B = ( I - A ) ( I + A ) ^ { - 1 } = ( I + A ) ^ { - 1 } ( I - A )
$$

is an element of $s _ { K } ( n )$ . However, if $B \in s _ { K } ( n )$ , then

$$
A = ( I - B ) ( I + B ) ^ { - 1 } = ( I + B ) ^ { - 1 } ( I - B )
$$

is an element of $S _ { K } ( n )$

For a generalized Cayley transformation, we have the following result similarly:

Theorem 2.3. Given $\begin{array} { r } { \phi ( \Lambda ) = \frac { p ( \Lambda ) } { p ( - \Lambda ) } } \end{array}$ , $p ( \Lambda )$ is a polynomial that satisfies $p ( 0 ) = 1$ $\dot { p } ( 0 ) \neq 0$ , if $B \in s _ { K } ( n )$ , then

$$
A = \phi ( B ) \in S _ { K } ( n ) .
$$

Therefore, we may use Pade approximation and pseudo-spectral method (the ´ Chebyshev spectral method) to construct the Poisson schemes for the linear Poisson system. The Pade approximation has been described in the literatures ´ [Qin89,ZQ94,FWQ90] in detail. Below, we will briefly describe the Chebyshev spectral method to construct the Poisson scheme. The Chebyshev spectral method is a highly effective method to approximate $\mathrm { e } ^ { A }$ . The detailed explanation of this is described in literature[TF85] . Here, we give only the result.

The Chebyshev spectral method is an approach based on series expansion by Chebyshev polynomial, i.e.,

$$
\mathbf { e } ^ { x } = \sum _ { k = 0 } ^ { \infty } C _ { k } J _ { k } ( R ) Q _ { k } \Big ( \frac { x } { R } \Big ) , \quad | x | < R ,
$$

where $x$ is a real number and $Q _ { k }$ is the Chebyshev complex orthogonal multinomial. $Q _ { k }$ satisfies the following recurrence relation:

$$
\begin{array} { l } { { Q _ { 0 } ( x ) = 1 , } } \\ { { \ } } \\ { { Q _ { 1 } ( x ) = x , } } \\ { { \ } } \\ { { Q _ { k + 1 } ( x ) = Q _ { k - 1 } ( x ) + 2 x Q _ { k } ( x ) , } } \end{array}
$$

where $C _ { 0 } = 1$ , and $C _ { k } = 2$ for $k > 0 , J _ { k }$ denotes the $k$ -order Bessel function. $Q _ { k }$ denotes the Chebyshev polynomial. $R$ is chosen arbitrarily. During computing, we calculate $J _ { k } ( R )$ first, and then calculate $Q _ { k }$ using the above recursive procedure.

Using the generalized Cayley transformation, and

$$
\mathrm { e } ^ { A } = { \frac { \mathrm { e } ^ { \frac { A } { 2 } } } { \mathrm { e } ^ { \frac { - A } { 2 } } } } ,
$$

and applying the Chebyshev spectral method to the numerator and denominator respectively, we can obtain the Poisson algorithm.

It was pointed out in literature $\left[ \mathrm { T F 8 5 } \right] ^ { - }$ that when $k > R$ , the series converges exponentially. Therefore, the summation in (2.1) is always finite. Where to truncate the series is determined by the size of $J _ { k } ( R )$ . Since $J _ { k } ( R )$ converges exponentially too, only a few steps of iteration is enough. Numerical tests show that this method has high accuracy and efficiency, especially when $A$ is a dense matrix. The above method can be applied only to the linear dynamic system, where $H$ is a quadratic form of $z$ ,

$$
\dot { z } = K B z .
$$

# 12.2.2 Construction of Difference Schemes for General Poisson Manifold

For a general $H$ , there are other methods to construct Poisson integrator such as method of generating function. The reader can refer to literatures[Fen85,FWQW89,FQ87] for more details. For a low-order scheme, we can construct directly using the implicit Euler scheme and verify it by criterion (1.3).

$$
\dot { z } = K \frac { \partial H } { \partial z } ,
$$

construct

$$
z ^ { k + 1 } = z ^ { k } + \tau K \nabla H \Big ( \frac { 1 } { 2 } ( I + B ) z ^ { k + 1 } + \frac { 1 } { 2 } ( I - B ) z ^ { k } \Big ) .
$$

Take derivative of (2.2) w.r.t. $z ^ { k }$ ,

$$
\widehat { z } _ { z } = I + \tau K H _ { z z } \Big ( \frac { 1 } { 2 } ( I + B ) \widehat { z } _ { z } + \frac { 1 } { 2 } ( I - B ) \Big ) ,
$$

i.e.,

$$
\Big ( I - \frac { 1 } { 2 } \tau K H _ { z z } ( I + B ) \Big ) \widehat { z } _ { z } = I + \frac { 1 } { 2 } \tau K H _ { z z } ( I - B ) ,
$$

where $z ^ { k + 1 } = { \widehat { z } } , z ^ { k } = z , x _ { y } = { \frac { \partial x } { \partial y } } ,$ , therefore,

$$
\widehat { z } _ { z } = \Big ( I - \frac { 1 } { 2 } \tau K H _ { z z } ( I + B ) \Big ) ^ { - 1 } \Big ( I + \frac { 1 } { 2 } \tau K H _ { z z } ( I - B ) \Big ) .
$$

To become a Poisson scheme, it should satisfy

$$
\begin{array} { r } { \widehat { z } _ { z } K \widehat { z } _ { z } ^ { \mathrm { T } } = K , } \end{array}
$$

i.e.,

$$
\begin{array} { r l } & { \left( I - \frac { 1 } { 2 } \tau K H _ { z z } ( I + B ) \right) ^ { - 1 } \left( I + \frac { 1 } { 2 } \tau K H _ { z z } ( I - B ) \right) K } \\ & { \cdot \left( I + \frac { 1 } { 2 } \tau K H _ { z } z ( I - B ) \right) ^ { \mathrm { T } } \left( I - \frac { 1 } { 2 } \tau K H _ { z } z ( I + B ) \right) ^ { - 1 } = K . } \end{array}
$$

After manipulation, we obtain

$$
K H _ { z z } ( K B ^ { \mathrm { T } } + B K ) H _ { z z } K = O .
$$

Therefore, if $K B ^ { \mathrm { T } } + B K = O$ , i.e., $B ^ { \mathrm { T } } \in { \mathfrak { s } } _ { K } ( n )$ , this scheme is a Poisson scheme.   
When $B = O$ , then the scheme becomes Euler midpoint scheme.

Denote

$$
z ^ { k + 1 } = G _ { H , B } ^ { \tau } z ^ { k } ,
$$

then for $B = O$ , the scheme is of second-order, for $B \neq O$ , it is only of first order. Using

$$
z ^ { k + 1 } = G _ { H , \pm B } ^ { \tau } z ^ { k } ,
$$

we can construct a composite scheme,

$$
\begin{array} { l } { { G _ { H , \pm B } ^ { \tau } = G _ { H , B } ^ { \frac { \tau } { 2 } } \circ G _ { H , - B } ^ { \frac { \tau } { 2 } } , } } \\ { { \ } } \\ { { G _ { H , \mp B } ^ { \tau } = G _ { H , - B } ^ { \frac { \tau } { 2 } } \circ G _ { H , B . } ^ { \frac { \tau } { 2 } } } } \end{array}
$$

Proposition 2.4. The above scheme has the second-order accuracy and the following proposition can be easily derived.

If $\phi _ { A } ( z ) = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z$ , where $A ^ { \mathrm { T } } = A$ , is a conservative quantity of Hamiltonian systemconserv $\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } \ : = \ : K \frac { \partial \boldsymbol { H } } { \partial \boldsymbol { z } }$ , and if of differe $A$ satisfies ce scheme $B ^ { \mathrm { T } } A + A B ^ { \mathrm { T } } = 0$ , then $\phi _ { A } ( z )$ is also $a$ $G _ { H , - B } ^ { \tau }$

Proof. Because $\phi _ { A } ( z )$ is a conservative quantity of Hamiltonian system,

$$
\frac { 1 } { 2 } \widehat { z } ^ { \mathrm { T } } A \widehat { z } = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z ,
$$

then

$$
\frac { 1 } { 2 } ( \widehat { z } + z ) ^ { \mathrm { T } } A ( \widehat { z } + z ) = 0 .
$$

From $B ^ { \mathrm { T } } A + A B ^ { \mathrm { T } } = 0$ , we obtain

$$
\begin{array} { r l } { \frac { 1 } { 2 } ( B ( \widehat z - z ) ) ^ { \mathrm T } A ( \widehat z - z ) } & { = \frac { 1 } { 2 } ( \widehat z - z ) B ^ { \mathrm T } A ( \widehat z - z ) } \\ & { = \frac { 1 } { 4 } ( \widehat z - z ) ^ { \mathrm T } ( B ^ { \mathrm T } A + A B ) ( \widehat z - z ) = 0 , } \\ { \left( \frac { 1 } { 2 } ( \widehat z + z ) + \frac { 1 } { 2 } B ( \widehat z - z ) \right) ^ { \mathrm T } A ( \widehat z - z ) } & { = 0 } \\ & { \Longrightarrow \tau w ^ { \mathrm T } A K H _ { z } ( w ) = 0 , \quad \forall ~ w \in \mathbb { R } ^ { n } . } \end{array}
$$

Let

$$
w = \frac { 1 } { 2 } ( z ^ { k + 1 } + z ^ { k } ) + \frac { 1 } { 2 } B ( z ^ { k + 1 } - z ^ { k } ) ,
$$

we obtain

$$
{ \frac { 1 } { 2 } } ( z ^ { k + 1 } ) ^ { \mathrm { T } } A z ^ { k + 1 } = { \frac { 1 } { 2 } } ( z ^ { k } ) ^ { \mathrm { T } } A z ^ { k } .
$$

The proof can be obtained.

# 12.2.3 Answers of Some Questions

# 1. Euler explicit scheme[LQ95a]

For a separable Hamiltonian $H$ in a standard Hamiltonian system, there exists an Euler explicit symplectic scheme. Similar question is raised for the Poisson system: does there exist an Euler explicit Poisson scheme for a separable $H ?$ The answer is “may not be”. We take $n = 3$ as an example to explain this point. Let

$$
K = \left[ \begin{array} { c c c } { { 0 } } & { { - c } } & { { b } } \\ { { } } & { { } } & { { } } \\ { { c } } & { { 0 } } & { { - a } } \\ { { - b } } & { { a } } & { { 0 } } \end{array} \right] ,
$$

$$
H = { \frac { 1 } { 2 } } ( z _ { 1 } ^ { 2 } + z _ { 2 } ^ { 2 } + z _ { 3 } ^ { 2 } ) ,
$$

then

$$
\dot { z } = K \frac { \partial H } { \partial z } = K z .
$$

To make scheme

$$
z ^ { k + 1 } = z ^ { k } + \tau K \nabla H \Big ( \frac { 1 } { 2 } ( I + B ) z ^ { k + 1 } + \frac { 1 } { 2 } ( I - B ) z ^ { k } \Big )
$$

a Poisson scheme, we should have

$$
K H _ { z z } ( K B ^ { \mathrm { T } } + B K ) H _ { z z } K = K ^ { 2 } B ^ { \mathrm { T } } K + K B K ^ { 2 } = O ,
$$

i.e., $K ^ { 2 } B ^ { \mathrm { T } } K \in S m ( n )$ (symmetrical matrix), here $K B ^ { \mathrm { T } } \in S m ( n )$ , i.e., $B K \in$ $S m ( n )$ . Expand scheme

$$
z ^ { k + 1 } = z ^ { k } + \tau K \nabla H ( w ) , \quad w = \frac { 1 } { 2 } ( I + B ) z ^ { k + 1 } + \frac { 1 } { 2 } ( I - B ) z ^ { k }
$$

into

$$
\left\{ \begin{array} { l l } { z _ { 1 } ^ { k + 1 } = z _ { 1 } ^ { k } - c \tau w _ { 2 } + b \tau w _ { 3 } , } \\ { \qquad \quad } \\ { z _ { 2 } ^ { k + 1 } = z _ { 2 } ^ { k } + c \tau w _ { 1 } - a \tau w _ { 3 } , } \\ { \qquad \quad } \\ { z _ { 3 } ^ { k + 1 } = z _ { 3 } ^ { k } - b \tau w _ { 1 } + a \tau w _ { 2 } . } \end{array} \right.
$$

To make sure the scheme is explicit, $w _ { 2 } , w _ { 3 }$ have to be a function of $z ^ { k }$ only. From

$$
w _ { 2 } = \frac { 1 } { 2 } ( z _ { 2 } ^ { k + 1 } + z _ { 2 } ^ { k } ) + \frac { 1 } { 2 } b _ { 2 1 } ( z _ { 1 } ^ { k + 1 } - z _ { 1 } ^ { k } ) + \frac { 1 } { 2 } b _ { 2 3 } ( z _ { 3 } ^ { k + 1 } - z _ { 3 } ^ { k } ) + \frac { 1 } { 2 } b _ { 2 2 } ( z _ { 2 } ^ { k + 1 } - z _ { 2 } ^ { k } ) ,
$$

we obtain $b _ { 2 1 } = 0 = b _ { 2 3 } , \ b _ { 2 2 } = - 1$ . Likewise, $b _ { 3 1 } = b _ { 3 2 } = 0 , b _ { 3 3 } = - 1 .$ Then $B$ has the form

$$
\left[ { \begin{array} { c c c } { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \end{array} } \right] ,
$$

substituting it into $B K ( \in S m ( n ) )$ , we know only when $a = 0$ , the scheme becomes an explicit scheme. Note that when $a = 0$ , $K$ is degenerated to the symplectic case. Therefore, in many situations, the separable system does not have an explicit scheme. Here the explicit scheme refers to the low-order finite-difference scheme, not the explicit analytic solution.

# 2. Midpoint scheme and Euler scheme

Below, we will answer the questions whether the midpoint scheme is a Lie–Poisson scheme of Euler equation, and whether there exists a Lie–Poisson scheme in a generalized Euler scheme[LQ95a,LQ95b] .

We already know that the answer for the first question is “no”. Now, we turn to the second question. The Euler equation has the form

$$
\dot { z } = J ( z ) H _ { z } = f ( z ) .
$$

For the case $n = 3$ ,

$$
J ( z ) = \left[ { \begin{array} { c c c } { 0 } & { - z _ { 3 } } & { z _ { 2 } } \\ { z _ { 3 } } & { 0 } & { - z _ { 1 } } \\ { - z _ { 2 } } & { z _ { 1 } } & { 0 } \end{array} } \right] ,
$$

$$
H = \frac { 1 } { 2 } \left( \frac { z _ { 1 } ^ { 2 } } { I _ { 1 } } + \frac { z _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { z _ { 3 } ^ { 2 } } { I _ { 3 } } \right) .
$$

We construct a generalized Euler scheme:

$$
\widehat { z } = z + \tau J ( w ) H _ { z } ( w ) = z + \tau f ( w ) ,
$$

where

$$
w = \frac { 1 } { 2 } ( \widehat { z } + z ) + \frac { 1 } { 2 } B ( \widehat { z } - z ) = \frac { 1 } { 2 } ( I + B ) \widehat { z } + \frac { 1 } { 2 } ( I - B ) z .
$$

The Jacobian matrix of map $z  { \widehat { z } }$ is

$$
A = \frac { \partial \widehat { z } } { \partial z } = I + \tau D _ { * } f ( w ) \left( \frac { \partial w } { \partial z } \right) ,
$$

where

$$
\begin{array} { r } { D _ { * } f ( z ) = D _ { * } J ( z ) H _ { z } = \left[ \begin{array} { c c c } { 0 } & { \frac { I _ { 2 } - I _ { 3 } } { I _ { 2 } I _ { 3 } } z _ { 3 } } & { \frac { I _ { 2 } - I _ { 3 } } { I _ { 2 } I _ { 3 } } z _ { 2 } } \\ { \frac { I _ { 3 } - I _ { 1 } } { I _ { 1 } I _ { 3 } } z _ { 3 } } & { 0 } & { \frac { I _ { 3 } - I _ { 1 } } { I _ { 1 } I _ { 3 } } z _ { 1 } } \\ { \frac { I _ { 1 } - I _ { 2 } } { I _ { 1 } I _ { 2 } } z _ { 2 } } & { \frac { I _ { 1 } - I _ { 2 } } { I _ { 1 } I _ { 2 } } z _ { 1 } } & { 0 } \end{array} \right] , } \\ { \frac { \partial w } { \partial z } = \frac { 1 } { 2 } ( I + B ) A + \frac { 1 } { 2 } ( I - B ) , } \end{array}
$$

therefore

$$
A = ( I - \tau D _ { * } f ( w ) ( I + B ) ) ^ { - 1 } ( I + \tau D _ { * } f ( w ) ( I - B ) ) .
$$

For the Euler scheme to be a Poisson scheme, it has to be $A J ( z ) A ^ { \mathrm { T } } = J ( \widehat { z } )$ , therefore:

$$
\begin{array} { r c l } { { } } & { { } } & { { A J ( z ) A ^ { \mathrm { T } } = ~ ( I - \tau D _ { * } f ( w ) ( I + B ) ) ^ { - 1 } ( I + \tau D _ { * } f ( w ) ( I - B ) ) J ( z ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \cdot ~ ( I + \tau ( I - B ^ { \mathrm { T } } ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) ( I - \tau ( I + B ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ J ( \widehat z ) , } } \end{array}
$$

$$
\begin{array} { r l } & { ( I + \tau D _ { * } f ( w ) ( I - B ) ) J ( z ) ( I + \tau ( I - B ^ { \mathrm { T } } ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) } \\ & { } \\ & { = ( I - \tau D _ { * } f ( w ) ( I + B ) ) J ( \widehat { z } ) ( I - \tau ( I + B ^ { \mathrm { T } } ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } ) , } \end{array}
$$

after manipulation,

$$
\begin{array} { r l } & { J ( \hat { z } ) - J ( z ) + \tau ^ { 2 } D _ { * } f ( w ) [ ( I + B ) J ( \hat { z } ) ( I + B ^ { \mathrm { T } } ) - ( I - B ) J ( z ) ( I - B ^ { \mathrm { T } } ) ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } } \\ & { = \tau [ J ( z ) ( I - B ^ { \mathrm { T } } ) + J ( \hat { z } ) ( I + B ^ { \mathrm { T } } ) ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } + \tau D _ { * } f ( w ) [ ( I - B ) J ( z ) + ( I + B ) J ( \hat { z } ) ] } \\ & { = J ( \hat { z } - z ) + \tau ^ { 2 } D _ { * } f ( w ) [ J ( \hat { z } - z ) + B J ( \hat { z } + z ) + J ( \hat { z } + z ) B ^ { \mathrm { T } } + B J ( \hat { z } - z ) B ^ { \mathrm { T } } ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } . } \end{array}
$$

Because $\tau$ is arbitrary, and $\widehat { z } - z = { O } ( \tau )$ , we can have

$$
\left\{ \begin{array} { l l } { \begin{array} { r l } & { J ( \widehat { z } - z ) = \tau J ( \widehat { z } + z ) ( D _ { * } f ( w ) ) ^ { \mathrm { T } } + \tau D _ { * } f ( w ) J ( \widehat { z } + z ) , } \\ & { \tau ^ { 2 } D _ { * } f ( w ) [ B J ( \widehat { z } + z ) + J ( \widehat { z } + z ) B ^ { \mathrm { T } } ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } } \end{array} } \\ { \begin{array} { r l } & { = \tau J ( \widehat { z } - z ) B ^ { \mathrm { T } } ( D _ { * } f ( w ) ) ^ { \mathrm { T } } + \tau D _ { * } f ( w ) B J ( \widehat { z } - z ) , } \\ & { D _ { * } f ( w ) [ J ( \widehat { z } - z ) + B J ( \widehat { z } - z ) B ^ { \mathrm { T } } ] ( D _ { * } f ( w ) ) ^ { \mathrm { T } } = O . } \end{array} } \end{array} \right.
$$

When $B = O$ , the above equation is the midpoint scheme, $w = \frac { 1 } { 2 } ( \widehat { z } + z )$ . It is easy to verify that the last equality in the above equations is dissatisfied. Hence the midpoint scheme is not a Poisson scheme. When $B \neq O$ , after complex computation, we can obtain similarly that there does not exist any $B \in g l ( n )$ to satisfy the above 3 formulas. Therefore, there does not exist a Poisson scheme in a generalized Euler form.

# 12.3 Generating Function and Lie–Poisson Scheme

The generating function method plays a crucial role in constructing the symplectic scheme (see the literatures[FWQW89,CS90,CG93] for details). Therefore, how to use the generating function method to construct the Lie–Poisson scheme becomes a research hot spot. The literatures in this aspect include[GM88,Ge91,CS91] . We have also investigated the generating function for Lie–Poisson system in details, and discovered that the Ge–Marsden method needs further improvement. Below is our understanding and derivation on the generating function and the Hamilton–Jacobi theory[LQ95b] .

# 12.3.1 Lie–Poisson–Hamilton–Jacobi (LPHJ) Equation and Generating Function

According to the diagram in Section 12.1 (for the left invariant system),

$$
\begin{array} { r l } { T ^ { * } G } & { { } \xrightarrow { G _ { H \circ \mathcal { T } _ { R } } ^ { t } = S } \ T ^ { * } G } \\ { \mathcal { T } _ { R } \bigg \downarrow } & { { } \mathcal { T } _ { R } \bigg \downarrow } \\ { \mathbf { g } ^ { * } } & { { } \xrightarrow { G _ { H } ^ { t } = P } \quad \mathbf { g } ^ { * } } \end{array}
$$

the phase flow determined by $H$ on $\mathbf { g } ^ { * }$ can induce a phase flow on $T ^ { * } G$ determined by $H \circ \mathcal { I } _ { R }$ . Let $u ^ { t } ( q , q _ { 0 } )$ be a first kind generating function of the symplectic map $S$ . Then we have the following properties.

Property 3.1. If $u : G \times G \to \mathbf { R }$ is invariant under the left action of $G$ , i.e.,

$$
u ^ { t } ( g q , g q _ { 0 } ) = u ^ { t } ( q , q _ { 0 } ) ,
$$

then the symplectic mapping generated by $u , S : \ ( q _ { 0 } , p _ { 0 } ) \to ( p , q )$ , where:

$$
p _ { 0 } = - \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q _ { 0 } } , \quad p = \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q } ,
$$

preserves momentum mapping $\mathcal { I } _ { L }$ . That is to say,

$$
{ \mathcal { I } } _ { L } \circ S = { \mathcal { I } } _ { L } .
$$

For the right-invariant translation on $G$ ,

$$
{ \mathcal { I } } _ { R } \circ S = { \mathcal { I } } _ { R } .
$$

Definition 3.2. If $G$ acts on the configuration space without fixed point, then we say $G$ acts on $G$ freely.

Property 3.3. If $G$ acts on $G$ freely, and its induced symplectic mapping $S$ preserves the momentum mapping $\mathcal { T } _ { L }$ , then the first-kind generating function of $S$ is left invariant.

Proof. See[GM88] .

For a left-invariant system, such as a generalized rigid body, the Hamiltonian function is left invariant, the phase flow isa first integral for this dynamics, i.e., left invariant, the momentum mappiis invariant under the phase flow of $\mathcal { T } _ { L }$ $\mathcal { I } _ { L }$ $G _ { H \circ { \mathcal { I } } _ { R } } ^ { t }$ RTherefore, if the action is free (generally speaking, the action is locally free), the firstkind generating function is left invariant.

Let $u ^ { t } ( q , q _ { 0 } )$ be the first-kind generating function of $S$ , then by the left invariance

$$
u ^ { t } ( q , q _ { 0 } ) = u ^ { t } ( e , q ^ { - 1 } q _ { 0 } ) = \widetilde { u } ^ { t } ( g ) , \quad g = q ^ { - 1 } q _ { 0 } .
$$

By Equation (3.2), we have

$$
\begin{array} { r l } & { p _ { 0 } = - \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q _ { 0 } } = - \frac { \partial \widetilde { u } ^ { t } ( q ^ { - 1 } q _ { 0 } ) } { \partial q _ { 0 } } = - \frac { \partial \widetilde { u } ^ { t } ( L _ { q ^ { - 1 } } q _ { 0 } ) } { \partial q _ { 0 } } = - L _ { q ^ { - 1 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Bigr | _ { g = q ^ { - 1 } } } \\ & { p = \frac { \partial u ^ { t } ( q , q _ { 0 } ) } { \partial q } = \frac { \partial \widetilde { u } ( q ^ { - 1 } q _ { 0 } ) } { \partial q } = \frac { \partial \widetilde { u } ( R _ { q _ { 0 } } V ( q ) ) } { \partial \widetilde { q } } = V ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Bigr | _ { g = q ^ { - 1 } q _ { 0 } } , } \\ & { V ( q ) = q ^ { - 1 } , } \\ & { V ^ { * } = - L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } , } \end{array}
$$

then

$$
p = - L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } ,
$$

therefore,

$$
\begin{array} { r c l } { { \mu _ { 0 } ~ = ~ { \cal L } _ { q _ { 0 } } ^ { * } p _ { 0 } = - { \cal L } _ { q _ { 0 } } ^ { * } { \cal L } _ { q ^ { - 1 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ - { \cal L } _ { q ^ { - 1 } q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } = - { \cal L } _ { g } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } , } } \end{array}
$$

and

$$
\begin{array} { r c l } { { \mu } } & { { = } } & { { L _ { q } ^ { * } p = - L _ { q } ^ { * } L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { - R _ { q ^ { - 1 } q _ { 0 } } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } = - R _ { g } ^ { * } \frac { \partial \widetilde { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } . } } \end{array}
$$

Through the above derivation, it is easy to prove (3.1)

$$
\begin{array} { r c l } { { { \cal M } _ { 0 } ~ = ~ R _ { q _ { 0 } } ^ { * } p _ { 0 } = - R _ { q _ { 0 } } ^ { * } L _ { q ^ { - 1 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } , } } \\ { { } } & { { } } & { { } } \\ { { { \cal M } ~ = ~ R _ { q } ^ { * } p = - R _ { q } ^ { * } L _ { q ^ { - 1 } } ^ { * } R _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ - L _ { q ^ { - 1 } } ^ { * } R _ { q _ { 0 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { g = q ^ { - 1 } q _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ - R _ { q _ { 0 } } ^ { * } L _ { q ^ { - 1 } } ^ { * } \frac { \partial \stackrel { \wedge } { u } } { \partial g } \Big | _ { q = q ^ { - 1 } q _ { 0 } } = { \cal M } _ { 0 } , } } \end{array}
$$

i.e.,

$$
{ \mathcal { T } } _ { L } \circ S = { \mathcal { T } } _ { L } .
$$

Take $g = q ^ { - 1 } q _ { 0 }$ , then

$$
\left\{ \begin{array} { l } { \displaystyle \mu _ { 0 } = - L _ { q } ^ { * } \frac { \partial \widetilde { u } ( \boldsymbol { g } ) } { \partial \boldsymbol { g } } , } \\ { \displaystyle \mu = - R _ { g } ^ { * } \frac { \partial \widetilde { u } ( \boldsymbol { g } ) } { \partial \boldsymbol { g } } = A d _ { g ^ { - 1 } } ^ { * } \mu _ { 0 } , } \end{array} \right.
$$

therefore $u ^ { t } ( q , q _ { 0 } ) = \widetilde { u } ^ { t } ( q ^ { - 1 } q _ { 0 } ) = \widetilde { u } ^ { t } ( g )$ defines a Poisson mapping:

$$
\mu _ { 0 }  \mu = A d _ { g ^ { - 1 } } ^ { * } \mu _ { 0 } .
$$

We now derive the conditions that $u ^ { t } ( q , q _ { 0 } )$ must meet.

$u ^ { t } ( q , q _ { 0 } )$ generates a symplectic map $S = G _ { H \circ J } ^ { t } = G _ { \overline { { H } } } ^ { t } .$ , where $\overline { { H } } = H \circ \mathcal { I }$ , and

$$
\begin{array} { l } { { S : ( p _ { 0 } , q _ { 0 } ) \longrightarrow ( p , q ) , } } \\ { { \ } } \\ { { p _ { 0 } = - \displaystyle { \frac { \partial u } { \partial q _ { 0 } } } , \quad p = \displaystyle { \frac { \partial u } { \partial q } } . } } \end{array}
$$

Because

$$
\begin{array} { l } { p \mathbf { d } q - p _ { 0 } \mathbf { d } q _ { 0 } = \displaystyle \frac { \partial u } { \partial q } \mathbf { d } q + \frac { \partial u } { \partial q _ { 0 } } \mathbf { d } q _ { 0 } , } \\ { \displaystyle \mathbf { d } u = \frac { \partial u } { \partial q } \mathbf { d } q + \frac { \partial u } { \partial q _ { 0 } } \mathbf { d } q _ { 0 } + \frac { \partial u } { \partial t } \mathbf { d } t = p \mathbf { d } q - p _ { 0 } \mathbf { d } q _ { 0 } + \frac { \partial u } { \partial t } \mathbf { d } t , } \end{array}
$$

we have

$$
\mathbf { d } \left( p \mathbf { d } q - p _ { 0 } \mathbf { d } q _ { 0 } + { \frac { \partial u } { \partial t } } \mathbf { d } t \right) = 0 .
$$

Note that

$$
{ \begin{array} { r l } & { \ d \left( p { \mathrm { d } } q - p _ { 0 } { \mathrm { d } } q _ { 0 } \right) = { \mathrm { d } } p \wedge { \mathrm { d } } q - { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } } \\ { = } & { \left( { \frac { \partial p } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } + { \frac { \partial p } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } + { \frac { \partial p } { \partial t } } { \mathrm { d } } t \right) \wedge \left( { \frac { \partial q } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } + { \frac { \partial q } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } + { \frac { \partial q } { \partial t } } { \mathrm { d } } t \right) - { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } } \\ { = } & { \left( { \frac { \partial p } { \partial p _ { 0 } } } { \frac { \partial q } { \partial q _ { 0 } } } - { \frac { \partial p } { \partial q _ { 0 } } } { \frac { \partial q } { \partial p _ { 0 } } } \right) { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } - { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } q _ { 0 } } \\ & { \ + { \frac { \partial q } { \partial t } } { \frac { \partial p } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } t + { \frac { \partial q } { \partial t } } { \frac { \partial p _ { 0 } } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } \wedge { \mathrm { d } } t } \\ & { \ - { \frac { \partial p } { \partial t } } { \frac { \partial q } { \partial p _ { 0 } } } { \mathrm { d } } p _ { 0 } \wedge { \mathrm { d } } t - { \frac { \partial p } { \partial t } } { \frac { \partial p } { \partial q _ { 0 } } } { \mathrm { d } } q _ { 0 } \wedge { \mathrm { d } } t } \end{array} }
$$

Since $( p _ { 0 } , q _ { 0 } ) \to ( p , q )$ is symplectic, we have

$$
g _ { z } J g _ { z } ^ { \mathrm { T } } = J \Longrightarrow f _ { 1 } = 0 .
$$

Because

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial q } { \partial t } = \frac { \partial \overline { { H } } } { \partial p } } \\ { \displaystyle \frac { \partial p } { \partial t } = - \frac { \partial \overline { { H } } } { \partial q } } \end{array} \right. \Longrightarrow \left\{ \begin{array} { l l } { \displaystyle f _ { 2 } = \frac { \partial \overline { { H } } } { \partial p } \mathbf { d } p \wedge \mathbf { d } t } \\ { \displaystyle f _ { 3 } = \frac { \partial \overline { { H } } } { \partial q } \mathbf { d } q \wedge \mathbf { d } t } \end{array} \right. ,
$$

therefore,

$$
{ \begin{array} { r l } & { \mathbf { d } p \wedge \mathbf { d } q - d p _ { 0 } \wedge \mathbf { d } q _ { 0 } } \\ & { = { \frac { \partial { \overline { { H } } } } { \partial p } } \mathbf { d } p \wedge \mathbf { d } t + { \frac { \partial { \overline { { H } } } } { \partial q } } \mathbf { d } q \wedge \mathbf { d } t = \mathbf { d } { \overline { { H } } } \wedge \mathbf { d } t } \\ & { \Longrightarrow \mathbf { d } { \overline { { H } } } \wedge \mathbf { d } t + \mathbf { d } \left( { \frac { \partial { \overline { { H } } } } { \partial t } } \right) \wedge \mathbf { d } t = 0 . } \end{array} }
$$

We have

$$
\textrm { d } \left( \overline { { H } } + \frac { \partial \overline { { H } } } { \partial t } \right) \wedge \mathbf { d } t = 0 .
$$

Therefore,

$$
\frac { \partial u } { \partial t } + \overline { { H } } ( p , q , t ) = c .
$$

Taking a proper initial value, we can obtain:

$$
\frac { \partial u } { \partial t } + \overline { { H } } ( p , q , t ) = 0 ,
$$

i.e.,

$$
\frac { \partial u ^ { t } ( p , q ) } { \partial t } + H \circ \mathcal { T } _ { R } ( p , q , t ) = 0 .
$$

Therefore we obtain the LPHJ equations

$$
\frac { \partial \overline { { u } } ( g ) } { \partial t } + H \bigg ( - R _ { g } ^ { * } \frac { \partial \overline { { u } } ( g ) } { \partial g } \bigg ) = 0 ,
$$

$$
g = q ^ { - 1 } q _ { 0 } .
$$

Remark 3.4. If we can construct a generating function $u ( g )$ , we then have $u ( q _ { 0 } , q )$ . This function can generate a symplectic mapping on $T ^ { * } G$ . By the commutative diagram, a Poisson mapping on ${ \bf g } ^ { * }$ can also be induced. This is a key point of constructing a Lie–Poisson integrator by generating function.

Remark 3.5. In order that the induced phase flow is a Poisson phase flow, the phase flow on $T ^ { * } G$ should be symplectic. Therefore, the condition of $g = q ^ { - 1 } q _ { 0 }$ cannot be discarded. Namely, when $t \to 0$ , $g = q ^ { - 1 } q _ { 0 }$ (unit element).

Remark 3.6. Only when $g = q ^ { - 1 } q _ { 0 }$ is satisfied, the momentum mapping is invariant. This is because the momentum mapping is

$$
\begin{array} { r } { \mathcal { I } _ { L } ( p , q ) = R _ { q } ^ { * } p = A d _ { q ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p , q ) . } \end{array}
$$

To make sure

$$
\begin{array} { r c l } { { \mathcal { I } _ { L } ( p _ { 0 } , q _ { 0 } ) = \mathcal { I } _ { L } ( p , q ) \implies A d _ { q _ { 0 } ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) = A d _ { q ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p , q ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \implies \mathcal { I } _ { R } ( p , q ) = A d _ { q } ^ { * } A d _ { q _ { 0 } ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { A d _ { ( q ^ { - 1 } q _ { 0 } ) ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) = A d _ { g ^ { - 1 } } ^ { * } \mathcal { I } _ { R } ( p _ { 0 } , q _ { 0 } ) . } } \end{array}
$$

If $g = q ^ { - 1 } q _ { 0 }$ , deriving back, we obtain the momentum mapping is invariant.

Remark 3.7. The above generating function theory can be transformed into the generating function theory on $\mathbf { g }$ (for details see literature[CS90] ). That is to say, the above generating function theory on $T ^ { * } G$ can be reformulated by the exponential mapping in terms of algebra variables, which has been done by Channell and Scovel[CS90] . Below, we list only some of their results.

For $g \in G$ , choose $\xi \in \{ \mathrm { g } \}$ , so that $g = \exp { ( \xi ) }$ . Then the LPHJ equation can be transformed into

$$
\left\{ \begin{array} { l l } { \frac { \partial s } { \partial t } + H ( - \mathbf { d } s \cdot \psi ( a d _ { \xi } ) ) = 0 , } \\ { M _ { 0 } = - \mathbf { d } s \cdot \chi ( a d _ { \xi } ) , } \\ { M = - \mathbf { d } s \cdot \psi ( a d _ { \xi } ) , } \end{array} \right.
$$

where

$$
\left\{ \begin{array} { l } { \displaystyle \chi ( a d _ { \xi } ) = \mathrm { i d } + \frac 1 2 a d _ { \xi } + \frac { 1 } { 1 2 } a d _ { \xi } ^ { 2 } + \cdots , } \\ { \displaystyle \psi ( a d _ { \xi } ) = \chi ( a d _ { \xi } ) \cdot e ^ { - a d _ { \xi } } \backsim \chi ( a d _ { \xi } ) - a d _ { \xi } , } \end{array} \right.
$$

and the condition $g = q ^ { - 1 } q _ { 0 }$ is transformed into

$$
s ( \xi , 0 ) = s _ { 0 } ( \xi ) = s _ { 0 } ( I ) ,
$$

i.e.,

$$
\xi | _ { t = 0 } = \operatorname { i d } .
$$

# 12.3.2 Construction of Lie–Poisson Schemes via Generating Function

The generating function theory to construct the symplectic scheme has been described in detail in the literatures[LQ95a,Fen86,FWQW89] . The next step is to use the generating function theory to construct the Lie–Poisson schemes. As we know, the generating function must generate identity transformation at time zero. From the previous section, the generating function should satisfy the condition (3.8), i.e., the group element becomes a unit element at $t = 0$ . We are not able to find a generating function universally applicable to a general Lie–Poisson system after a long time pursuit. Scovel[MS96] once suggested a possible solution using the Morse bundle theory. However, for the Hamilton function of quadratic form, we can find the low-order generating function. Below, we will give a brief description:

The Hamiltonian for $s o ( 3 ) ^ { * }$ is $H ( M ) = { \frac { 1 } { 2 } } M I ^ { - 1 } M .$ . From (3.6) and (3.7), using $u$ as the generating function, we have:

$$
\begin{array} { r c l } { { { \cal M } } } & { { = } } & { { - \mathrm { \bf d } u \cdot \psi ( a d _ { \xi } ) = - \mathrm { \bf d } u \left( 1 - \frac { 1 } { 2 } a d _ { \xi } + \frac { 1 } { 1 2 } a d _ { \xi } ^ { 2 } + { \cal O } ( a d _ { \xi } ^ { 3 } ) \right) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { - \mathrm { \bf d } u + \frac { 1 } { 2 } \mathrm { \bf d } u \cdot a d _ { \xi } + { \cal O } ( a d _ { \xi } ^ { 2 } ) . } } \end{array}
$$

After substituting $H$ into Equation (3.6) and using expansion of $\psi$ , we have

$$
\begin{array} { r l } & { \displaystyle \frac { \partial u } { \partial t } + H \left( - \mathbf { d } u + \frac { 1 } { 2 } \mathbf { d } u \cdot a d _ { \xi } - O ( a d _ { x i } ^ { 2 } ) \right) } \\ & { = \displaystyle \frac { \partial u } { \partial t } + \frac { 1 } { 2 } \left( - \mathbf { d } u + \frac { 1 } { 2 } \mathbf { d } u \cdot a d _ { \xi } + O ( a d _ { \xi } ^ { 2 } ) \right) I ^ { - 1 } \left( - \mathbf { d } u + \frac { 1 } { 2 } \mathbf { d } u \cdot a d _ { \xi } + O ( a d _ { \xi } ^ { 2 } ) \right) } \\ & { = \displaystyle \frac { \partial u } { \partial t } + \frac { 1 } { 2 } I ^ { - 1 } \mathbf { d } u \mathbf { d } u - \frac { 1 } { 2 } I ^ { - 1 } \mathbf { d } u \mathbf { d } u ( a d _ { \xi } ) + O ( a d _ { \xi } ^ { 2 } ) . } \end{array}
$$

Because $\xi$ and time $\tau$ have the same order of magnitude, the Equation (3.10) can be simplified as

$$
\begin{array} { r c l } { { \displaystyle { \frac { \partial u } { \partial t } } + H ( M ) \ = \ \frac { \partial u } { \partial t } + \frac { 1 } { 2 } I ^ { - 1 } \frac { \partial u } { \partial \xi } \frac { \partial u } { \partial \xi } - \frac { 1 } { 2 } I ^ { - 1 } \frac { \partial u } { \partial \xi } \left( \frac { \partial u } { \partial \xi } a d _ { \xi } \right) + O ( \tau ^ { 2 } ) } } \\ { { \displaystyle { } } } & { { \displaystyle { } } } & { { } } \\ { { \displaystyle { } } } &  { \displaystyle { = \ \frac { \partial u } { \partial t } + \frac { 1 } { 2 } I ^ { - 1 } \frac { \partial u } { \partial \xi } \frac { \partial u } { \partial \xi } + O ( \tau ^ { 2 } ) } } \\ { { \displaystyle { } } } & { { \displaystyle { } } } & { { } } \\ { { \displaystyle { } } } & { { \displaystyle { = \ 0 . } } } \end{array}
$$

From this, we can obtain a first-order generating function. Taking

$$
u = \frac { I \xi \cdot \xi } { 2 \tau } .
$$

It can be easily verified that the Equation (3.11) satisfies (3.10) to the approximate order. Therefore, we can use $u$ to construct the Lie–Poisson scheme.

We first calculate $\xi$ by solving

$$
M _ { 0 } = - I \boldsymbol { \xi } \cdot \boldsymbol { \chi } ( \boldsymbol { \xi } ) ,
$$

and then substitute it into Equation (3.6). Next, we calculate $M = \exp { ( \xi ) } M _ { 0 }$ . On repeating this procedure, we can obtain a Lie–Poisson algorithm.

Below, we will apply this algorithm to free rigid body. For motion of the rigid body, $\chi ( \xi )$ has a closed expression (see Subsection 12.5.2). Solving nonlinear (3.12) for $\xi$ becomes a key point. It is necessary to linearize (3.12). The iterative formula for $\xi$ is

$$
\bigl ( 1 + \tau \bigl ( c _ { 1 } \widehat { \xi } - \bigl ( c _ { 3 } \xi ( \xi + c _ { 4 } ) \bigr ) ( I ^ { - 1 } \widehat { M _ { 0 } \times \xi } ) + c _ { 2 } ( \widehat { I ^ { - 1 } p _ { 0 } } ) \bigr ) \bigr ) \delta \xi = \xi _ { k + 1 } - \xi _ { k } ,
$$

where

$$
\begin{array} { l l } { { c _ { 1 } = \displaystyle \frac { 2 - | \xi | \sin | \xi | - 2 \cos | \xi | } { | \xi | ^ { 4 } } , } } & { { c _ { 2 } = \displaystyle \frac { \cos | \xi | - 1 } { | \xi | ^ { 2 } } , \nonumber } } \\ { { c _ { 3 } = \displaystyle \frac { - 2 | \xi | - | \xi | \cos | \xi | + 3 \sin | \xi | } { | \xi | ^ { 5 } } , } } & { { c _ { 4 } = \displaystyle \frac { 2 | \xi | - \sin | \xi | } { | \xi | ^ { 3 } } . } } \end{array}
$$

In fact, the above algorithm is applicable even when $H$ is a polynomial.

Ge–Marsden[GM88] have proposed an algorithm, which neglects the generating function condition (3.8). Therefore, it has certain flaw. Below, we will explain it from the theoretical point of view.

First, we should point out that the Ge–Marsden algorithm can only give the firstorder scheme for simple system such as the free rigid body. Its second-order scheme, however, is not a second-order approximation to the original system, as we will prove it below.

Generally speaking, a generating function can be given as the following equation

$$
u = u _ { 0 } + \sum _ { n = 1 } ^ { \infty } \frac { ( \delta t ) ^ { n } } { n ! } u _ { n } ,
$$

where $u _ { 0 } = { \frac { ( \xi , \xi ) } { 2 } }$ generates the identical transformation at time $t = 0$ . Substituting (3.13) into the LPHJ equation, we have

$$
u _ { 1 } = - H ( V ) , \quad u _ { 2 } = \frac { \partial H } { \partial V } \cdot \mathrm { d } u _ { 1 } \cdot \psi ( a d _ { \xi } ) , \cdot \cdot \cdot .
$$

Below, we will take $s o ( 3 ) ^ { * }$ as an example to explain the flaw of this algorithm.

For $s o ( 3 ) ^ { * }$ , $u _ { 0 } = \frac { \xi ^ { 2 } } { 2 }$ , and hence $V = \xi$ . The first-order scheme is

$$
S _ { 1 } = u _ { 0 } + \tau u _ { 1 } = \frac { \xi ^ { 2 } } { 2 } - \tau H ( \xi ) = \frac { \xi ^ { 2 } } { 2 } - \frac { \tau } { 2 } \xi I ^ { - 1 } \xi .
$$

The generating function for the second-order scheme is

$$
\begin{array} { r c l } { { } } & { { } } & { { S _ { 2 } ~ = ~ S _ { 1 } + \displaystyle \frac { \tau ^ { 2 } } { 2 } u _ { 2 } = \displaystyle \frac { \xi ^ { 2 } } { 2 } - \tau H ( \xi ) + \displaystyle \frac { \tau ^ { 2 } } { 2 } \frac { \partial H } { \partial V } \cdot \mathrm { d } u _ { 1 } \cdot \psi ( a d _ { \xi } ) } } \\ { { } } & { { } } & { { ~ = ~ \displaystyle \frac { \xi ^ { 2 } } { 2 } - \displaystyle \frac { \tau } { 2 } \xi I ^ { - 1 } \xi - \displaystyle \frac { \tau ^ { 2 } } { 2 } I ^ { - 1 } \xi \big ( I ^ { - 1 } \xi \cdot \psi ( \xi ) \big ) . } } \end{array}
$$

Using the system of Equation (3.6) (for $S O ( 3 ) \ M , M _ { 0 }$ denote angular momentum), we get:

$$
M - M _ { 0 } = - \mathrm { d } u \cdot a d _ { \xi } .
$$

Next, we will prove that $S _ { 1 }$ indeed generates a first-order Lie–Poisson scheme to the Euler equation. However, $S _ { 2 }$ actually is not a second-order approximation to the Euler equation. Furthermore, we will find that with this algorithm, it is impossible to construct difference scheme that preserves the momentum mapping.

Because

$$
\mathbf { d } S _ { 1 } = \mathbf { d } \left( \frac { \xi ^ { 2 } } { 2 } - \frac { \tau } { 2 } \xi \cdot I ^ { - 1 } \xi \right) = \xi - \tau I ^ { - 1 } \xi
$$

and $M _ { 0 } = - \mathrm { d } S _ { 1 } \cdot \chi ( a d _ { \xi } ) = ( - \xi + \tau I ^ { - 1 } \xi ) \cdot \chi ( \xi )$ , we have $\xi = - M _ { 0 } + O ( \tau )$ . By Equation (3.15) and applying $\xi \cdot a d _ { \xi } = 0$ , we obtain

$$
\begin{array} { l } { M - M _ { 0 } ~ = ~ ( \xi - \tau I ^ { - 1 } \xi ) \cdot a d _ { \xi } = - \tau I ^ { - 1 } \xi \cdot a d _ { \xi } } \\ { ~ = ~ \tau [ \xi , I ^ { - 1 } \xi ] = \tau [ - M _ { 0 } + O ( \tau ) , I ^ { - 1 } ( - M _ { 0 } + O ( \tau ) ) ] } \\ { ~ = ~ \tau [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] + O ( \tau ^ { 2 } ) . } \end{array}
$$

This is a first-order approximation to the Euler equation

$$
\begin{array} { r } { \dot { M } = [ M , I ^ { - 1 } M ] . } \end{array}
$$

For the second-order generating function $S _ { 2 }$ , we first calculate $\chi ( \xi )$ . Let $\chi ( \xi ) =$ $1 + a _ { 1 } \xi + a _ { 2 } \xi ^ { 2 }$ , where $a _ { 1 } , a _ { 2 }$ have closed analytical expression (see Subsection 12.5.2) as follows

$$
\begin{array} { l } { \displaystyle a _ { 1 } = \frac { 1 - \cos | \xi | } { \sin ^ { 2 } | \xi | + ( 1 - \cos | \xi | ) ^ { 2 } } , } \\ { \displaystyle a _ { 2 } = \frac { \frac { ( \cos | \xi | - 1 ) ^ { 2 } } { | \xi | ^ { 2 } } + \frac { \sin | \xi | - | \xi | } { | \xi | } + ( \sin | \xi | - | \xi | ) | \xi | } { \sin ^ { 2 } | \xi | + ( 1 - \cos | \xi | ) ^ { 2 } } , } \end{array}
$$

therefore,

$$
\begin{array} { l } { { u _ { 2 } ~ = ~ - I ^ { - 1 } \xi ( I ^ { - 1 } \xi \cdot \psi ( \xi ) ) } } \\ { { { } } } \\ { { { } } } \\ { { { } = ~ - \langle I ^ { - 1 } \xi , I ^ { - 1 } \xi \rangle - a _ { 2 } I ^ { - 1 } \xi ( I ^ { - 1 } \xi \cdot \xi ^ { 2 } ) , } } \end{array}
$$

then

$$
\begin{array} { r } { \textrm { d } S _ { 2 } = \xi - \tau I ^ { - 1 } \xi - \tau ^ { 2 } ( I ^ { - 1 } ) ^ { 2 } \xi - \frac { \tau ^ { 2 } } { 2 } \textrm { d } \big ( a _ { 2 } I ^ { - 1 } \xi \cdot ( I ^ { - 1 } \xi \cdot \xi ^ { 2 } ) \big ) , } \end{array}
$$

by

$$
M _ { 0 } = - \mathbf { d } S _ { 2 } \cdot \chi ( \xi ) = - \xi + \tau \xi \cdot \chi ( \xi ) + O ( \tau ^ { 2 } ) ,
$$

we have

$$
\xi = - M _ { 0 } + \tau \xi \cdot \chi ( \xi ) + O ( \tau ^ { 2 } ) .
$$

From Equation (3.15), we get

$$
\begin{array} { r l } { M - M _ { 0 } \ = \ - { \mathrm { d } } S _ { 2 } \cdot a d _ { \xi } } \\ { \ } & { \ - ( \xi - { \tau } { I ^ { - 1 } } \xi - { \tau } ^ { 2 } ( \ \widehat { I ^ { - 1 } \xi } ) ^ { 2 } - \frac { { \tau } ^ { 2 } } { 2 } { \mathrm { d } } ( a _ { 2 } { I ^ { - 1 } } \xi \cdot ( { I ^ { - 1 } } \xi \cdot \widehat { \xi ^ { 2 } } ) ) ) \cdot \widehat { \xi } } \\ { \ } & { \ = \ \tau [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] + a _ { 1 } \tau ^ { 2 } \big ( [ [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] , I ^ { - 1 } M _ { 0 } ] } \\ & { \ + [ M _ { 0 } , I ^ { - 1 } [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] ] \big ) } \\ & { \ + a _ { 2 } \big ( I ^ { - 1 } M _ { 0 } ( I ^ { - 1 } M _ { 0 } \cdot \widehat { M _ { 0 } ^ { 2 } } ) + I ^ { - 1 } ( I ^ { - 1 } M _ { 0 } \cdot \widehat { M _ { 0 } ^ { 2 } } ) M _ { 0 } \big ) } \\ & { \ - \frac { \tau ^ { 2 } } { 2 } { \mathrm { d } } \big ( a _ { 2 } \cdot I ^ { - 1 } \xi ( I ^ { - 1 } \xi \cdot \widehat { \xi ^ { 2 } } ) \big ) \cdot \widehat { \xi } + O ( \tau ^ { 3 } ) . } \end{array}
$$

According to the Euler equation (3.16), its second-order approximation should be

$$
\begin{array} { r l } { M - M _ { 0 } = } & { \tau [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] + \frac { \tau ^ { 2 } } { 2 } ( [ [ M _ { 0 } , I ^ { - 1 } M _ { 0 } ] , I ^ { - 1 } M _ { 0 } ] } \\ & { + [ M _ { 0 } , I ^ { - 1 } [ I ^ { - 1 } M _ { 0 } , M _ { 0 } ] ] ) + O ( \tau ^ { 3 } ) . } \end{array}
$$

As $t  0 , \xi  M _ { 0 }$ , by comparison, we found that the Equation (3.17) is not an approximation to the Equation (3.18). Therefore, the generating function $S _ { 2 }$ cannot generate the second-order approximation to the Euler equation.

We have shown that $S _ { 1 }$ generates a first-order Lie–Poisson scheme. However, a momentum mapping preserving scheme should satisfy $J _ { L } ( q , M ) = J _ { L } ( q _ { 0 } , M _ { 0 } )$ . For $T ^ { * } S O ( 3 )$ , this becomes $q M = q _ { 0 } M _ { 0 }$ , and hence $M = q ^ { - 1 } q _ { 0 } M _ { 0 }$ . Therefore, it is necessary to estimate $q \in G$ . If we had formula $M = g M _ { 0 }$ , a very natural idea is to make $g = q ^ { - 1 } q _ { 0 }$ , which leads to $q = q _ { 0 } g ^ { - 1 }$ . An algorithm well constructed on $s o ( 3 ) ^ { * }$ should lead to a good approximation of $q \in S O ( 3 )$ to equation of motion. The scheme that satisfies Equations (3.6) and the condition (3.8) and is generated by our generating function theory that belongs to this type. However, the scheme constructed via algorithm[GM88] does not belong to this type. Because the condition (3.8) is neglected, it is impossible to construct the algorithm on $G$ using algorithm[GM88] . This can be illustrated as follows.

Using another representation of (3.6)

$$
M _ { 0 } = - \mathsf { d } u \cdot \chi ( a d _ { \xi } ) , \quad M = \exp { ( a d _ { \xi } ) } M _ { 0 } ,
$$

and $\xi = ( - M _ { 0 } + \tau I ^ { - 1 } \xi ) \cdot \chi ( \xi )$ , if we let $q = q _ { 0 } g ^ { - 1 } = q _ { 0 } \exp \left( - \xi \right) = q _ { 0 } \exp \left( \left( M _ { 0 } - \right. \right.$ $\tau I ^ { - 1 } \xi ) \cdot \chi ( \xi ) )$ , then $q$ is not a first-order approximation to the equation of motion ${ \dot { q } } =$ $q I ^ { - 1 } \widehat { M }$ . In fact, the algorithm[GM88] cannot produce the form of $q$ alone to construct momentum mapping preserving scheme.

# 12.4 Construction of Structure Preserving Schemes for Rigid Body

We have already introduced the equation of motion for generalized rigid body in previous section. In this section, we will take $S O ( 3 )$ as an example to explain how to construct structure-preserving schemes.

# 12.4.1 Rigid Body in Euclidean Space

Let $\Lambda ( t ) \in S O ( 3 )$ , such that $\Lambda ( t ) \Lambda ( t ) ^ { \mathrm { T } } = I$ , $| \Lambda ( t ) | = 1$ . Then the equation of motion for the free rigid body can be formulated as

$$
\dot { \Lambda } ( t ) = \Lambda ( t ) \widehat { W } ( t ) ,
$$

where $\widehat { W } ( t ) \in s o ( 3 )$ , $s o ( 3 )$ is the Lie algebra of $S O ( 3 )$ . The isomorphism relation, $s o ( 3 ) \simeq \mathbf { R } ^ { 3 }$ , can be realized through the following equations:

$$
\begin{array} { r l } & { \widehat { W } ( t ) \simeq W ( t ) \in { \bf R } ^ { 3 } , } \\ & { \left[ \begin{array} { c c c } { 0 } & { - w _ { 3 } } & { w _ { 2 } } \\ { w _ { 3 } } & { 0 } & { - w _ { 1 } } \\ { - w _ { 2 } } & { w _ { 1 } } & { 0 } \end{array} \right] \simeq \left[ \begin{array} { c } { w _ { 1 } } \\ { w _ { 2 } } \\ { w _ { 3 } } \\ { w _ { 3 } } \end{array} \right] , } \end{array}
$$

$$
\widehat W ( t ) \cdot a = W \times a , \quad a \in { \bf R } ^ { 3 } .
$$

The $\widehat W ( t )$ in Equation (4.1) is called angular velocity in the body description. $\widehat { W } ( t ) =$ $\Lambda ( t ) ^ { - 1 } \dot { \Lambda } ( t )$ is consistent with the definition of generalized rigid body. The corresponding Euler equation is

$$
\dot { M } = [ M , W ] , \quad M = J W ,
$$

where $J$ is called inertia operator, $M$ the body angular momentum. The body variables and the spatial variables have the following relations:

$$
\left\{ \begin{array} { l } { \omega = A W , } \\ { m = \Lambda M , \quad \widehat { \omega } = \Lambda \widehat { W } \Lambda ^ { \mathrm { T } } \Longrightarrow \omega = \Lambda W , } \\ { a = \Lambda A , } \end{array} \right.
$$

here $A$ is an acceleration.

Operator “  ” has the following equalities:

$$
\begin{array} { r c l } { \widehat { \boldsymbol { u } \times \boldsymbol { v } } } & { = } & { [ \widehat { \boldsymbol { u } } , \widehat { \boldsymbol { v } } ] , } \\ { \widehat { \boldsymbol { u } } \cdot \boldsymbol { v } } & { = } & { \boldsymbol { u } \times \boldsymbol { v } , } \\ { \widehat { \boldsymbol { \left[ u , \widehat { \boldsymbol { v } } \right] } \cdot \boldsymbol { w } } } & { = } & { \left( \boldsymbol { u } \times \boldsymbol { v } \right) \times \boldsymbol { w } , } \\ { \boldsymbol { u } \cdot \boldsymbol { v } } & { = } & { \frac { 1 } { 2 } \mathrm { t r } \left( \widehat { u } \widehat { \boldsymbol { v } } \right) . } \end{array}
$$

The equation of motion of the rigid body may be expressed on space $S U ( 2 )$ or $S H _ { 1 }$ (unit quaternion). Applying their equivalence (their Lie algebra is isomorphism), we may obtain different forms of the Equation (4.1) under $S U ( 2 )$ and $S H _ { 1 }$ .

$S U ( 2 )$ : $U \in S U ( 2 )$ , satisfies

$$
\begin{array} { r } { \begin{array} { r } { U U ^ { * } = I , \quad | U | = 1 . } \end{array} } \end{array}
$$

The equation of motion becomes

$$
\dot { U } = U \Omega _ { u } ,
$$

where $\Omega _ { u } = U ^ { * } U \in s u ( 2 )$ , satisfies $\Omega _ { u } + \Omega _ { u } ^ { * } = 0$ , tr $\Omega _ { u } = 0$ . In $s u ( 2 )$ , we choose

$$
\{ ( - \mathrm { i } \sigma _ { 1 } ) , ( - \mathrm { i } \sigma _ { 2 } ) , ( - \mathrm { i } \sigma _ { 3 } ) \}
$$

as a basis, where

$$
\begin{array} { r l } & { \sigma _ { 1 } = \left[ \begin{array} { l l } { 0 } & { 1 } \\ { } & { } \\ { 1 } & { 0 } \end{array} \right] , \quad \sigma _ { 2 } = \left[ \begin{array} { l l } { 0 } & { - \mathbf { i } } \\ { } & { } \\ { \mathbf { i } } & { 0 } \end{array} \right] } \\ & { \sigma _ { 3 } = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { } & { } \\ { 0 } & { - 1 } \end{array} \right] , \quad \sigma _ { 0 } = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { } & { } \\ { 0 } & { 1 } \end{array} \right] } \end{array}
$$

are 4 Pauli matrices.

It is easy to see that

$$
\sum _ { i = 1 } ^ { 3 } \omega _ { i } \sigma _ { i } = \left[ \begin{array} { c c } { - \mathrm { i } \omega _ { 3 } } & { - \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } \\ { } & { } \\ { \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } & { \mathrm { i } \omega _ { 3 } } \end{array} \right] \in S U ( 2 ) .
$$

Hence

$$
\Omega _ { u } = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) \in s u ( 2 ) \simeq \mathbf { R } ^ { 3 } \simeq s o ( 3 ) ,
$$

using the matrix notation, rewrite the equation:

$$
\left[ \begin{array} { c c } { \dot { \sigma } } & { \dot { \beta } } \\ { \dot { \gamma } } & { \dot { \delta } } \end{array} \right] = \left[ \begin{array} { c c } { \sigma } & { \beta } \\ { \gamma } & { \delta } \end{array} \right] \left[ \begin{array} { c c } { - \mathrm { i } \omega _ { 3 } } & { - \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } \\ { \omega _ { 2 } - \mathrm { i } \omega _ { 1 } } & { \mathrm { i } \omega _ { 3 } } \end{array} \right] .
$$

$\forall Q \in S H _ { 1 }$ , $\| Q \| = 1$ , $Q = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } ) \in H$ (set of all quaternion). The equation of motion becomes $\dot { Q } = Q \Omega _ { h }$ , where $\ddot { \Omega _ { h } } = \overline { { Q } } \dot { Q } = Q ^ { - 1 } \dot { Q } \in s h _ { 1 }$ (quaternion with zero real part). Let

$$
\begin{array} { r } { \Omega _ { h } = \omega _ { 1 } i + \omega _ { 2 } j + \omega _ { 3 } k = ( 0 , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) , \quad \omega _ { h } = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) . } \end{array}
$$

Rewrite the equation of motion into the quaternion form

$$
\begin{array} { r c l } { ( \dot { q } _ { 0 } , \dot { q } _ { 1 } , \dot { q } _ { 2 } , \dot { q } _ { 3 } ) } & { = } & { ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } ) \cdot ( 0 , \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) } \\ & & { \implies \left\{ \begin{array} { l } { \dot { q } _ { 0 } = - q \omega = - ( q , \omega ) , } \\ { \dot { q } = q _ { 0 } \omega ^ { \mathrm { T } } + q \widehat { \omega } , } \end{array} \right. \quad q = ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) . } \end{array}
$$

The Euler equation of motion becomes

$$
\begin{array} { l l l } { { s o _ { 3 } ^ { * } : } } & { { \cfrac { \mathrm { d } M } { \mathrm { d } t } = [ M , W ] ; } } & { { } } \\ { { } } & { { } } & { { } } \\ { { s u _ { 2 } ^ { * } : } } & { { \cfrac { \mathrm { d } M _ { u } } { \mathrm { d } t } = \cfrac 1 2 [ M _ { u } , W _ { u } ] = [ M _ { u } , W ] , } } & { { M _ { u } = 2 M , \quad \omega _ { u } = \cfrac 1 2 W ; } } \\ { { } } & { { } } & { { } } \\ { { s h _ { 1 } ^ { * } : } } & { { \cfrac { \mathrm { d } M _ { h } } { \mathrm { d } t } = \cfrac 1 2 [ M _ { h } , W _ { h } ] = [ M _ { h } , W ] , } } & { { M _ { h } = 2 M , \quad \omega _ { h } = \cfrac 1 2 W . } } \end{array}
$$

If the unified Euler equation of motion is used, we have

$$
{ \frac { \mathrm { d } { \cal M } } { \mathrm { d } t } } = [ { \cal M } , { \cal W } ] .
$$

If $\omega$ is assigned using the values of $S O ( 3 )$ , then the corresponding equation of motion becomes:

$$
\begin{array} { r l } & { \dot { \Lambda } = \Lambda \widehat { W } ( t ) , ~ W ( t ) = ( \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } ) , } \\ & { \dot { Q } = Q \Omega _ { h } , ~ \Omega _ { h } = \left( 0 , \frac { \omega _ { 1 } } { 2 } , \frac { \omega _ { 2 } } { 2 } , \frac { \omega _ { 3 } } { 2 } \right) , } \\ & { \dot { U } = U \Omega _ { u } , ~ \Omega _ { u } = \left( \frac { \omega _ { 1 } } { 2 } , \frac { \omega _ { 2 } } { 2 } , \frac { \omega _ { 3 } } { 2 } \right) . } \end{array}
$$

After the above transformation, the equation of motion becomes more simpler. The number of unknowns become fewer from the original 9 $( S O ( 3 ) )$ to 4 complex variables $( S U ( 2 ) )$ ), and then reduced to 4 real variables $( S H _ { 1 } )$ . The computation storage and operation may be sharply reduced for large-scale scientific computations.

More details about the relations among $S O ( 3 )$ , $S U ( 2 )$ and $S H _ { 1 }$ will be given in Section 12.5.

# 12.4.2 Energy-Preserving and Angular Momentum-Preserving Schemes for Rigid Body

With the equation of motion of rigid body, we may construct the corresponding difference scheme[LQ95a] . One type of important schemes is the structure-preserving scheme. Structure-preserving may have some different meaning for different systems. For example, it could mean to preserve the original system’s physical structure, the symmetry, or invariant physical quantities.

The total energy and the angular momentum, especially the angular momentum, are important invariants for the rigid motion. Many experiments indicated that the energy and the angular momentum can be well maintained, which is essential for computer simulation to have a good approximation to the real motion.

The equation of motion for the rigid body is

$$
\left\{ \begin{array} { l } { \dot { \Lambda } ( t ) = \Lambda ( t ) \widehat { W } ( t ) , } \\ { \dot { M } ( t ) = M ( t ) \times W ( t ) } \\ { M ( t ) = I \cdot W ( t ) } \end{array} \right\} \Longrightarrow I \cdot \dot { W } ( t ) = I W ( t ) \times W ( t ) ,
$$

where $I$ is the inertia operator.

Note that the energy function $H = \frac { 1 } { 2 } ( M ( t ) , W ( t ) ) = \frac { 1 } { 2 } \widehat { W } ( t ) J \widehat { W } ( t )$ is a Hamiltonian function and the spatial angular momentum $M ( t ) { \overline { { \ } } } = \Lambda M ( t ) \Leftrightarrow { \widehat { M } } ( t ) =$ $\Lambda \widehat { M } ( t ) \Lambda ( t ) ^ { \mathrm { T } }$ becomes momentum mapping. To maintain the energy and the angular momentum invariant is just to maintain the Hamilton function and the momentum mapping of the Lie–Poisson system invariant.

The energy invariance is mainly manifested in solving Euler equations, and the angular momentum invariance concerns more with equations of motion on $S O ( 3 )$ . Using relation $\Lambda _ { n + 1 } M _ { n + 1 } \ = \ \Lambda _ { n } M _ { n }$ , we can derive the formula for which $\Lambda _ { n + 1 }$ should satisfy. For Euler equation $\dot { M } ( t ) = M ( t ) \times W ( t ) = M ( t ) \times I ^ { - 1 } M ( t )$ , the midpoint scheme preserves the Hamiltonian function, i.e., it is energy-preserving (in fact midpoint scheme preserves all functions of quadratic form).

The midpoint scheme for Euler equation is

$$
\frac { M _ { n + 1 } - M _ { n } } { \delta t } = \frac { M _ { n + 1 } + M _ { n } } { 2 } \times I \frac { M _ { n + 1 } + M _ { n } } { 2 } ,
$$

multiply $I ^ { - 1 } { \frac { M _ { n + 1 } + M _ { n } } { 2 } }$ via inner product on both sides,

$$
\left( M _ { n + 1 } - M _ { n } \right) \cdot ( I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) ) = 0 \Longrightarrow I ^ { - 1 } M _ { n + 1 } \cdot M _ { n + 1 } = I ^ { - 1 } M _ { n } \cdot M _ { n } ,
$$

i.e., $H _ { n + 1 } = H _ { n }$ . Since $I ^ { - 1 }$ is a symmetric operator, we have

$$
M _ { n } \cdot I ^ { - 1 } M _ { n + 1 } = M _ { n + 1 } \cdot I ^ { - 1 } M _ { n } .
$$

Rewrite scheme (4.3) into

$$
\begin{array} { l c l } { { M _ { n + 1 } } } & { { = } } & { { M _ { n } + \displaystyle \frac { \delta t } { 4 } ( M _ { n + 1 } + M _ { n } ) \times I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) } } \\ { { } } & { { \Longrightarrow } } & { { \left( I + \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) \right) M _ { n + 1 } = \left( I - \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( \displaystyle \widehat { M _ { n + 1 } + M _ { n } } ) \right) M _ { n } } } \\ { { } } & { { \Longrightarrow } } & { { M _ { n + 1 } = \left( I + \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( \displaystyle \widehat { M _ { n + 1 } + M _ { n } } ) \right) ^ { - 1 } \left( I - \displaystyle \frac { \delta t } { 4 } I ^ { - 1 } ( \displaystyle \widehat { M _ { n + 1 } + M _ { n } } ) \right) M _ { n } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \Lambda _ { n + 1 } ^ { - 1 } \Lambda _ { n } M _ { n } . } } \end{array}
$$

By conservation of angular momentum:

$$
\Lambda _ { n + 1 } M _ { n + 1 } = \Lambda _ { n } M _ { n } .
$$

By comparison, we obtain

$$
\Lambda _ { n + 1 } = \Lambda _ { n } \bigg ( I - \frac { \delta t } { 4 } I ^ { - 1 } \big ( \widehat { M _ { n + 1 } + M _ { n } } \big ) \bigg ) ^ { - 1 } \bigg ( I + \frac { \delta t } { 4 } I ^ { - 1 } \big ( \widehat { M _ { n + 1 } + M _ { n } } \big ) \bigg ) .
$$

Since

$$
\frac { \delta t } { 4 } I ^ { - 1 } ( M _ { n + 1 } + M _ { n } ) = \frac { \delta t } { 2 } W _ { n } + O ( \delta t ^ { 2 } ) ,
$$

from Cayley transformation, we know this is a second-order approximation to equation $\dot { \Lambda } = \Lambda \widehat { W }$ .

In brief, if we construct an energy-preserving scheme on $s o ( 3 ) ^ { * }$ , we may obtain a scheme approximate to the equation of motion by using the conservation of an angular momentum. We remark that this highly depends on the schemes constructed on $s o ( 3 ) ^ { * }$ . Not every scheme on $s o ( 3 ) ^ { * }$ corresponds to a good approximation scheme to the equation of motion on $S O ( 3 )$ . Ge–Marsden algorithm for Lie–Poisson system is a typical example.

# 12.4.3 Orbit-Preserving and Angular-Momentum-Preserving Explicit Scheme

The orbit-preserving $\mathrm { [ L O 9 5 a ] }$ here means the motion trajectory remains at coadjoint orbit. For rigid body this means in every time step

$$
M _ { n + 1 } = \Lambda _ { n } M _ { n } , \exists \Lambda _ { n } \in S O ( 3 ) .
$$

The midpoint scheme constructed in (4.2) is a kind of implicit orbit-preserving scheme. Below, we will derive explicit orbit-preserving schemes.

The equation is

$$
\dot { M } = M \times W = - W \times M = - \widehat { W } \cdot M , \quad \widehat { W } \in S O ( 3 ) , \quad \widehat { W } = I ^ { - 1 } M .
$$

Assume the difference scheme to be constructed has the form

$$
M _ { n + 1 } = \exp { ( b ( \delta t ) ) } M _ { n } .
$$

It is easy to see when $b ( \delta t ) = - \delta t W _ { n } = - \delta t ( I ^ { - 1 } M _ { n } )$ , (4.4) is a first-order scheme. Expanding the scheme (4.4), we obtain

$$
M _ { n + 1 } = M _ { n } + b ( \delta t ) M _ { n } + \frac { 1 } { 2 } \big ( b ( \delta t ) \big ) ^ { 2 } M _ { n } + \frac { 1 } { 3 ! } \big ( b ( \delta t ) \big ) ^ { 3 } M _ { n } + \cdots .
$$

Using Taylor expansion, we have

$$
\begin{array} { r c l } { { } } & { { } } & { { M _ { n + 1 } ~ = ~ M _ { n } - \delta t \widehat W _ { n } M _ { n } + \Big ( \frac { \ddot { M } } { 2 } \Big ) \delta t ^ { 2 } + \Big ( \frac { M ^ { ( 3 ) } } { 3 ! } \Big ) \delta t ^ { 3 } + \cdots } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ M _ { n } - \delta t \widehat W _ { n } M _ { n } + \frac { \delta t ^ { 2 } } { 2 } ( M _ { n } \times W _ { n } \times W _ { n } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \frac { \delta t ^ { 2 } } { 2 } \big ( M _ { n } \times I ^ { - 1 } ( M _ { n } \times W _ { n } ) \big ) + \cdots . } } \end{array}
$$

Let

$$
b ( \delta t ) = \delta t B _ { 1 } + \delta t ^ { 2 } B _ { 2 } + \delta t ^ { 3 } B _ { 3 } + \cdots ,
$$

substitute it into (4.5), and retain only the first two terms

$$
\begin{array} { r c l } { { { \cal M } _ { n + 1 } } } & { { = } } & { { { \cal M } _ { n } + \delta t B _ { 1 } { \cal M } _ { n } + \delta t ^ { 2 } B _ { 2 } { \cal M } _ { n } + \displaystyle \frac { 1 } { 2 } ( \delta t B _ { 1 } + \delta t ^ { 2 } B _ { 2 } ) ^ { 2 } { \cal M } _ { n } + o ( \delta t ^ { 3 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { { \cal M } _ { n } + \delta t B _ { 1 } { \cal M } _ { n } + \delta t ^ { 2 } B _ { 2 } { \cal M } _ { n } + \displaystyle \frac { 1 } { 2 } \delta t ^ { 2 } B _ { 1 } ^ { 2 } { \cal M } _ { n } + o ( \delta t ^ { 3 } ) . } } \end{array}
$$

Comparing the coefficients of Equation (4.6) with those of (4.7), we have

$$
\begin{array} { r c l } { { } } & { { B _ { 1 } } } & { { = } } & { { - \widehat { W } _ { n } , } } \\ { { } } & { { } } & { { } } \\ { { ( B _ { 1 } ^ { 2 } + 2 B _ { 2 } ) M _ { n } } } & { { = } } & { { ( M _ { n } \times W _ { n } \times W _ { n } ) + ( M _ { n } \times I ^ { - 1 } ( M _ { n } \times W _ { n } ) ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \widehat { W } _ { n } ^ { 2 } M _ { n } - \left( I ^ { - 1 } ( \widehat { M _ { n } \times W _ { n } } ) \right) M _ { n } , } } \end{array}
$$

then

$$
\begin{array} { l } { { \displaystyle B _ { 1 } = - \widehat { W } _ { n } , } } \\ { { \displaystyle B _ { 2 } = - \frac { 1 } { 2 } \big ( I ^ { - 1 } ( \widehat { M _ { n } \times W _ { n } } ) \big ) . } } \end{array}
$$

Likewise, we can construct third or fourth order schemes. Here we give only the result

$$
\begin{array} { r c l } { { { \cal B } _ { 3 } } } & { { = } } &  { \frac 1 6 \widehat { \displaystyle ( W \big ( I ^ { - 1 } ( { \widehat { \cal M } } \times { \hat { \cal W } } ) \big ) \big ) + 2 I ^ { - 1 } ( { \widehat { \cal M } } \times { \hat { \cal W } } ) { \widehat { \cal W } } + I ^ { - 1 } ( { \cal M } \widehat { \times { \hat { \cal W } } \times { \cal W } } ) } } \\ { { } } & { { } } & { { { } } } \\ { { } } & { { } } & { { + \big ( I ^ { - 1 } \big ( { \cal M } \times { \widehat { \ I ^ { - 1 } ( { \cal M } } \times { \cal W } ) } \big ) \big ) - \frac 1 2 B _ { 1 } B _ { 2 } - \frac 1 2 B _ { 2 } B _ { 1 } . } } \end{array}
$$

Another way to construct the orbit-preserving scheme is the modified R–K method, which can be described as follows.

If the initial value $M _ { 0 }$ is known, let:

$$
\begin{array} { r l } & { \mu _ { 0 } = M _ { 0 } , } \\ & { \mu _ { 1 } = \mathrm { { e } } ^ { \tau c _ { 1 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } , } \\ & { \mu _ { 2 } = \mathrm { { e } } ^ { \tau c _ { 2 1 } ( - \widehat { I ^ { - 1 } \mu _ { 1 } } ) } \mathrm { { e } } ^ { \tau c _ { 2 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } , } \\ & { \qquad \cdots } \\ & { \mu _ { r } = \mathrm { { e } } ^ { \tau c _ { r , r - 1 } ( - \widehat { I ^ { - 1 } \mu _ { r - 1 } } ) } \mathrm { { e } } ^ { \tau c _ { r , r - 2 } ( - \widehat { I ^ { - 1 } \mu _ { r - 2 } } ) } \cdots \mathrm { { e } } ^ { \tau c _ { r , 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } , } \end{array}
$$

the $( r + 1 )$ -th order approximation of the equation is

$$
M = \mathrm { e } ^ { \tau c _ { r } ( - \widehat { I ^ { - 1 } \mu _ { r } } ) } \mathrm { e } ^ { \tau c _ { r - 1 } ( - \widehat { I ^ { - 1 } \mu _ { r - 1 } } ) } \cdot \cdot \cdot \mathrm { e } ^ { \tau c _ { 0 } ( - \widehat { I ^ { - 1 } \mu _ { 0 } } ) } M _ { 0 } .
$$

Comparing the coefficients between the above equation and the Taylor expansion (4.6), we obtain $c _ { i j }$ and $c _ { s }$ . Take $r = 1$ as an example.

$$
\begin{array} { r l } & { \mathrm { ( s u r e ) } } \\ & { \mathrm { ( a s u r e ) } } \\ & { = \left( \begin{array} { c c } { 1 } & { r _ { 1 } } \\ { - r _ { 2 } } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { r _ { 2 } } \end{array} \right) \mathrm { ( } A r _ { 1 } - r _ { 1 } } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right)  \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 1 } \\ { 1 } & { - r _ { 2 } A _ { 1 } ^ { - 1 } r _ { 2 } } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { \overline { { A } } _ { 2 1 } ^ { - 1 } } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { - r _ { 2 } A _ { 1 } ^ { - 1 } r _ { 1 } } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } \\ & { \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right) } \\ &  \quad = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } &  0  \end{array}
$$

By the Taylor expansion, we have

$$
\left\{ \begin{array} { l l } { c _ { 0 } + c _ { 1 } = 1 , } \\ { \displaystyle { c _ { 1 } c _ { 1 0 } = \frac { 1 } { 2 } } , } \\ { c _ { 0 } ^ { 2 } + c _ { 1 } ^ { 2 } + 2 c _ { 0 } c _ { 1 } = ( c _ { 0 } + c _ { 1 } ) ^ { 2 } = 1 , } \end{array} \right. \Longrightarrow \left\{ \begin{array} { l l } { c _ { 0 } + c _ { 1 } = 1 , } \\ { \displaystyle c _ { 1 } c _ { 1 0 } = \frac { 1 } { 2 } . } \end{array} \right.
$$

Set $c _ { 0 } = c _ { 1 } = \frac { 1 } { 2 } , c _ { 1 0 } = 1$ 12 , c10 = 1 or c0 = 0, c1 = 1, c10 = 2 , we obtain a second-order modified $\mathbf { R - K }$ method.

Literature[CG93] gives the modified R–K methods for general dynamic system. The scheme on $s o ( 3 ) ^ { * }$ constructed via the above methods can be written as $M _ { n + 1 } = \Lambda M _ { n }$ . Take $\Lambda _ { n + 1 } ^ { - 1 } \Lambda _ { n } = \Lambda$ , we obtain $\Lambda _ { n + 1 } = \Lambda _ { n } \Lambda ^ { - 1 }$ . It is easy to verify that the $\Lambda _ { n + 1 } =$ $\Lambda _ { n } \Lambda ^ { - 1 }$ approximates $\dot { \Lambda } = \Lambda W$ in the same order of accuracy as scheme $M _ { n + 1 } =$ $\Lambda M _ { n }$ .

# 12.4.4 Lie–Poisson Schemes for Free Rigid Body

We have mentioned how to construct a scheme to preserve the angular momentum and the Lie–Poisson structure. The free rigid motion is a simple Lie–Poisson system. Among existing methods, Ge–Marsden algorithm is a first-order method to preserve the Lie–Poisson structure (we thus prove that this method is unable to maintain angular momentum). In Section 12.3, we introduced a generating-function method which is slow. We will introduce a fast method in this section. It is a split Lie–Poisson method[LQ95a] . It is also an angular momentum preserving method.

Because the free rigid motion’s Hamiltonian function is separable, we can use the composite method to construct Lie–Poisson scheme according to separable system’s procedure. MacLachlan introduced an explicit method[McL93] which requires analytic solution for each split subsystem at every step. The midpoint method proposed below is also an explicit Lie–Poisson method but with few computations.

The rigid motion’s Lie–Poisson equation is

$$
\left[ \begin{array} { c } { \dot { x } _ { 1 } } \\ { \dot { x } _ { 2 } } \\ { \dot { x } _ { 3 } } \end{array} \right] = \left[ \begin{array} { c c c } { 0 } & { - x _ { 3 } } & { x _ { 2 } } \\ { x _ { 3 } } & { 0 } & { - x _ { 1 } } \\ { - x _ { 2 } } & { x _ { 1 } } & { 0 } \end{array} \right] \left[ \begin{array} { c } { \frac { \partial H } { \partial x _ { 1 } } } \\ { \frac { \partial H } { \partial x _ { 2 } } } \\ { \frac { \partial H } { \partial x _ { 3 } } } \end{array} \right] ,
$$

where $x \ = \ ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { \mathrm { T } } \ \in \ \mathbf { R } ^ { 3 }$ is an angular momentum, $H = \frac { 1 } { 2 } \langle I ^ { - 1 } x , x \rangle$ is a Hamiltonian function and energy function of system.

For a separable system, $I$ is usually a diagonal matrix. Without loss of generality, let $H = \frac { 1 } { 2 } \bar { ( a _ { 1 } x _ { 1 } ^ { 2 } + a _ { 2 } x _ { 2 } ^ { 2 } + a _ { 3 } x _ { 3 } ^ { 2 } ) }$ . According to the decomposition rule, the fewer the split steps the better. We can use Casimir function of the Lie–Poisson equation to rewrite the system’s Hamilton function, and obtain an equivalent system. Note that $| x | ^ { 2 } = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 }$ is a first integral of the system. Let

$$
\overline { { { H } } } = H - \frac { 1 } { 2 } a _ { 1 } | x | ^ { 2 } = \frac { 1 } { 2 } ( a _ { 2 } - a _ { 1 } ) x _ { 2 } ^ { 2 } + \frac { 1 } { 2 } ( a _ { 3 } - a _ { 1 } ) x _ { 3 } ^ { 2 } = H _ { 1 } + H _ { 2 } ,
$$

where $H _ { 1 } = \frac { 1 } { 2 } ( a _ { 2 } - a _ { 1 } ) x _ { 2 } ^ { 2 } , H _ { 2 } = \frac { 1 } { 2 } ( a _ { 3 } - a _ { 1 } ) x _ { 3 } ^ { 2 } .$

Substituting $H _ { 1 }$ into the Lie–Poisson equation (1.1), we have

$$
\dot { x } = J ( x ) \frac { \partial H _ { 1 } } { \partial x } = \left[ \begin{array} { c } { - ( a _ { 2 } - a _ { 1 } ) x _ { 2 } x _ { 3 } } \\ { 0 } \\ { 0 } \\ { ( a _ { 2 } - a _ { 1 } ) x _ { 1 } x _ { 2 } } \end{array} \right] ,
$$

where

$$
J ( x ) = \left[ \begin{array} { c c c } { { 0 } } & { { - x _ { 3 } } } & { { x _ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { x _ { 3 } } } & { { 0 } } & { { - x _ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { - x _ { 2 } } } & { { x _ { 1 } } } & { { 0 } } \end{array} \right] .
$$

This equation can be simplified as a standard symplectic system

$$
\left\{ \begin{array} { l l } { \dot { x } _ { 1 } = - ( a _ { 2 } - a _ { 1 } ) x _ { 2 } x _ { 3 } , } \\ { ~ } \\ { \dot { x } _ { 3 } = ( a _ { 2 } - a _ { 1 } ) x _ { 1 } x _ { 2 } , } \end{array} \right.
$$

where $x _ { 2 }$ is a constant.

Among symplectic difference schemes for the standard symplectic system (4.10), only a few of them can preserve the Lie-Poisson structure of the original system (4.9).

Theorem 4.1. For the system (4.9), the midpoint scheme is a Lie–Poisson scheme[LQ95a] .

In order to prove the Theorem 4.1, we need the following lemma first.

Lemma 4.2. For the system (4.9), a symplectic algorithm for the standard symplectic system (4.10) preserves Poisson structure, if and only if the following three conditions are satisfied

$$
\left\{ \begin{array} { l l } { - x _ { 1 1 } x _ { 3 } + x _ { 1 3 } x _ { 1 } = - \widehat { x } _ { 3 } , } \\ { \qquad } \\ { x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } = - \widehat { x } _ { 1 } , } \\ { \qquad } \\ { x _ { 1 2 } \widehat { x } _ { 1 } + x _ { 3 2 } \widehat { x } _ { 3 } = 0 , } \end{array} \right.
$$

where $x _ { i } = x _ { i } ^ { n } , \widehat { x _ { i } } = x _ { i } ^ { n + 1 } , x _ { i j } = \frac { \partial \widehat { x _ { i } } } { \partial x _ { j } } .$

Proof. By the Theorem 1.2, a scheme is of Poisson if and only if

$$
\left( \frac { \partial \widehat { x } } { \partial x } \right) J ( x ) \left( \frac { \partial \widehat { x } } { \partial x } \right) ^ { \mathrm { T } } = J ( \widehat { x } ) .
$$

Expanding the above equation, we get

$$
{ \begin{array} { r l } & { \left[ { \begin{array} { c c c } { x _ { 1 1 } } & { x _ { 1 2 } } & { x _ { 1 3 } } \\ { 0 } & { 1 } & { 0 } \\ { x _ { 3 1 } } & { x _ { 3 2 } } & { x _ { 3 3 } } \end{array} } \right] \left[ { \begin{array} { c c c } { 0 } & { - x _ { 3 } } & { x _ { 2 } } \\ { x _ { 3 } } & { 0 } & { - x _ { 1 } } \\ { - x _ { 2 } } & { x _ { 1 } } & { 0 } \end{array} } \right] \left[ { \begin{array} { c c c } { x _ { 1 1 } } & { 0 } & { x _ { 3 1 } } \\ { x _ { 1 2 } } & { 1 } & { x _ { 3 2 } } \\ { x _ { 1 3 } } & { 0 } & { x _ { 3 3 } } \end{array} } \right] } \\ { = } & { \left[ { \begin{array} { c c c } { 0 } & { - { \hat { x } } _ { 3 } } & { { \hat { x } } _ { 2 } } \\ { { \hat { x } } _ { 3 } } & { 0 } & { - { \hat { x } } _ { 1 } } \\ { - { \hat { x } } _ { 2 } } & { { \hat { x } } _ { 1 } } & { 0 } \end{array} } \right] , } \end{array} }
$$

i.e.,

$$
\left[ \begin{array} { c c c } { { 0 } } & { { - x _ { 1 1 } x _ { 3 } + x _ { 1 3 } x _ { 1 } } } & { { a _ { 1 3 } } } \\ { { x _ { 1 1 } x _ { 3 } - x _ { 1 3 } x _ { 1 } } } & { { 0 } } & { { x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } } } \\ { { - a _ { 1 3 } } } & { { x _ { 3 3 } x _ { 1 } - x _ { 3 1 } x _ { 3 } } } & { { 0 } } \end{array} \right] = \left[ \begin{array} { c c c } { { 0 } } & { { - \widehat { x } _ { 3 } } } & { { \widehat { x } _ { 2 } } } & { { - \widehat { x } _ { 3 } } } \\ { { \widehat { x } _ { 3 } } } & { { 0 } } & { { - \widehat { x } _ { 1 } } } \\ { { - \widehat { x } _ { 2 } } } & { { \widehat { x } _ { 1 } } } & { { 0 } } \end{array} \right] .
$$

where $a _ { 1 3 } = ( x _ { 1 2 } x _ { 3 } - x _ { 1 3 } x _ { 2 } ) x _ { 3 1 } + ( x _ { 1 3 } x _ { 1 } - x _ { 1 1 } x _ { 3 } ) x _ { 3 2 } + ( x _ { 1 1 } x _ { 2 } - x _ { 1 2 } x _ { 1 } ) x _ { 3 3 }$

Since the scheme is symplectic for (4.10), we have

$$
- x _ { 1 3 } x _ { 3 1 } + x _ { 1 1 } x _ { 3 3 } = 1 .
$$

So $a _ { 1 3 }$ can be simplified as:

$$
a _ { 1 3 } = ( x _ { 3 } x _ { 3 1 } - x _ { 1 } x _ { 3 3 } ) x _ { 1 2 } + ( x _ { 1 3 } x _ { 1 } - x _ { 1 1 } x _ { 3 } ) x _ { 3 2 } + x _ { 2 } .
$$

Comparing the corresponding elements of the matrix on both sides and using the condition $\widehat { x } _ { 2 } = x _ { 2 }$ , we have

$$
\left\{ \begin{array} { l l } { x _ { 1 1 } x _ { 3 } - x _ { 1 3 } x _ { 1 } = \widehat { x } _ { 3 } , } \\ { \qquad } \\ { x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } = - \widehat { x } _ { 1 } , } \\ { \qquad } \\ { x _ { 1 2 } \widehat { x } _ { 1 } + x _ { 3 2 } \widehat { x } _ { 3 } = 0 . } \end{array} \right.
$$

Thus before the lemma is proved.

Now we will prove the Theorem 4.1.

Proof. The midpoint scheme for system (4.9) is (here, $I = \left( I _ { 1 } , I _ { 2 } , I _ { 3 } \right) = \left( a _ { 1 } , a _ { 2 } , a _ { 3 } \right) )$

$$
\left\{ \begin{array} { l l } { \widehat { x } _ { 1 } = x _ { 1 } + \tau ( I _ { 1 } - I _ { 2 } ) \frac { \widehat { x } _ { 3 } + x _ { 3 } } { 2 } x _ { 2 } , } \\ { \widehat { x } _ { 2 } = x _ { 2 } , } \\ { \widehat { x } _ { 3 } = x _ { 3 } + \tau ( I _ { 2 } - I _ { 1 } ) \frac { \widehat { x } _ { 1 } + x _ { 1 } } { 2 } x _ { 2 } . } \end{array} \right.
$$

Its Jacobian matrix is $\left[ { \begin{array} { c c c } { x _ { 1 1 } } & { x _ { 1 2 } } & { x _ { 1 3 } } \\ { 0 } & { 1 } & { 0 } \\ { x _ { 3 1 } } & { x _ { 3 2 } } & { x _ { 3 3 } } \end{array} } \right] , { \mathrm { w h e r } }$ e

$$
\left\{ \begin{array} { l l } { \displaystyle x _ { 1 1 } = 1 + \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 2 } x _ { 3 1 } , } \\ { \displaystyle x _ { 1 2 } = \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) ( \widehat { x } _ { 3 } + x _ { 3 } ) + \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 2 } x _ { 3 2 } , } \\ { \displaystyle x _ { 1 3 } = \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 3 3 } x _ { 2 } + \frac { T } { 2 } ( I _ { 1 } - I _ { 2 } ) x _ { 2 } , } \\ { \displaystyle x _ { 3 1 } = \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 1 1 } x _ { 2 } + \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } , } \\ { \displaystyle x _ { 3 2 } = \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) ( \widehat { x } _ { 1 } + x _ { 1 } ) + \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } , } \\ { \displaystyle x _ { 3 3 } = 1 + \frac { T } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } x _ { 1 3 } . } \end{array} \right.
$$

Solving the above equations, we get

$$
\left\{ \begin{array} { l l } { \displaystyle x _ { 1 1 } = x _ { 3 3 } = \frac { 1 - a ^ { 2 } } { 1 + a ^ { 2 } } , } \\ { \displaystyle x _ { 1 2 } = \frac { \frac { 7 } { 2 } \left( I _ { 1 } - I _ { 2 } \right) \widehat x _ { 3 } } { 1 + a ^ { 2 } } , } \\ { \displaystyle x _ { 1 3 } = - x _ { 3 1 } = - \frac { 2 a } { 1 + a ^ { 2 } } , } \\ { \displaystyle x _ { 3 2 } = \frac { \frac { 7 } { 2 } \left( I _ { 2 } - I _ { 1 } \right) \widehat x _ { 1 } } { 1 + a ^ { 2 } } , } \end{array} \right.
$$

where

$$
a = \frac { \tau } { 2 } ( I _ { 2 } - I _ { 1 } ) x _ { 2 } .
$$

Substituting the system of Equations (4.12) into condition (4.11), we find that all conditions are satisfied. Therefore, by Lemma 4.2, the scheme is of Poisson. $\blacktriangle$

Lemma 4.3. [FQ91] Consider dynamic system ${ \dot { x } } = a ( x )$ . If $a$ can be split into $a =$ $a _ { 1 } + a _ { 2 } + \cdots + a _ { k }$ , and $\boldsymbol { g } ^ { s } \sim \boldsymbol { e } _ { a } ^ { s }$ is phase flow of a dynamic system, then

$$
g _ { i } ^ { s } \sim e _ { a _ { i } } ^ { s } , \quad 2 n d - o r d e r , \quad \forall i \implies g _ { 1 } ^ { \frac { s } { 2 } } \circ \cdot \cdot \cdot g _ { k } ^ { \frac { s } { 2 } } \circ g _ { k } ^ { \frac { s } { 2 } } \circ \cdot \cdot \cdot g _ { 1 } ^ { \frac { s } { 2 } } \smile e _ { a } ^ { s } , \quad 2 n d - o r d e r .
$$

Proof. For the standard symplectic system (4.10), the generalized Euler scheme

$$
\widehat { \boldsymbol { x } } = \boldsymbol { x } + \tau J \nabla H ( B \widehat { \boldsymbol { x } } + ( I - B ) \boldsymbol { x } )
$$

is symplectic, iff

$$
B = \frac 1 2 ( I + C ) , \quad J C + C ^ { \mathrm { T } } J = O .
$$

It is natural to ask what kind of symplectic difference scheme for the system (4.10) is also a Poisson scheme for the system (4.9). Below we restrict our discussion to the generalized Euler scheme (4.14).

Let C = c1 c2 ! , then the symplectic condition (4.14) turns into $c _ { 4 } = - c _ { 1 }$ Therefore,

$$
B = \frac { 1 } { 2 } \left[ \begin{array} { c c } { 1 + c _ { 1 } } & { c _ { 2 } } \\ { c _ { 3 } } & { 1 - c _ { 1 } } \end{array} \right] ,
$$

then

$$
\begin{array} { r l r } {  { B \widehat { x } + ( I - B ) x \ = \ \frac { 1 } { 2 } [ \begin{array} { l } { ( 1 + c _ { 1 } ) \widehat { x } _ { 1 } + ( 1 - c _ { 1 } ) x _ { 1 } + c _ { 2 } ( \widehat { x } _ { 3 } - x _ { 3 } ) } \\ { c _ { 3 } ( \widehat { x } _ { 1 } - x _ { 1 } ) + ( 1 - c _ { 1 } ) \widehat { x } _ { 3 } + ( 1 - c _ { 1 } ) x _ { 3 } } \end{array} ] } } \\ & { } & { \ = \ \frac { 1 } { 2 } [ \begin{array} { l } { z _ { 1 } } \\ { z _ { 3 } } \end{array} ] , } \end{array}
$$

then Euler scheme becomes

$$
\left\{ \begin{array} { l l } { \widehat { x } _ { 1 } = x _ { 1 } - a z _ { 3 } , } \\ { \qquad } \\ { \widehat { x } _ { 3 } = x _ { 3 } - a z _ { 1 } , } \end{array} \right.
$$

where $a$ is defined by Equation (4.13), $z _ { 1 } , z _ { 3 }$ are defined by Equation (4.15).

After complex computations, the elements of Jacobian matrix of the solution are

$$
\begin{array} { r l } & { x _ { 1 1 } = \cfrac { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) - a ^ { 2 } ( 1 - c _ { 1 } ) ^ { 2 } } { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) + a ^ { 2 } ( 1 - c _ { 1 } ^ { 2 } ) } , } \\ & { x _ { 1 3 } = \cfrac { - 2 a ( 1 - a c _ { 2 } ) } { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) + a ^ { 2 } ( 1 - c _ { 1 } ^ { 2 } ) } , } \\ & { \widehat { x } _ { 3 } = \cfrac { ( ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) - a ^ { 2 } ( 1 - c _ { 1 } ) ^ { 2 } ) x _ { 3 } + 2 a ( 1 + a c _ { 3 } ) x _ { 1 } } { ( 1 + a c _ { 3 } ) ( 1 - a c _ { 2 } ) + a ^ { 2 } ( 1 - c _ { 1 } ^ { 2 } ) } , } \\ & { x _ { 1 1 } x _ { 3 } - x _ { 1 3 } x _ { 1 } = \widehat { x } _ { 3 } \quad ( \sec { ( 4 . 1 1 ) } ) . } \end{array}
$$

Since $x _ { 1 } , x _ { 3 }$ are arbitrary real number, we can get

$$
c _ { 1 } = 0 , \quad c _ { 2 } = - c _ { 3 } .
$$

Substituting Equation (4.17) into (4.16), and recalculating the Jacobian matrix, we have

$$
\begin{array} { l } { { x _ { 3 1 } = \displaystyle \frac { 2 a ( 1 - a c _ { 2 } ) } { a ^ { 2 } + ( 1 - a c _ { 2 } ) ^ { 2 } } , ~ x _ { 3 3 } = \displaystyle \frac { ( 1 - a c _ { 2 } ) ^ { 2 } - a ^ { 2 } } { a ^ { 2 } + ( 1 - a c _ { 2 } ) ^ { 2 } } , } } \\ { { { } } } \\  { { \widehat x _ { 1 } = \displaystyle \frac { ( ( 1 - a c _ { 2 } ) ^ { 2 } - a ^ { 2 } ) x _ { 1 } } { a ^ { 2 } + ( 1 - a c _ { 2 } ) ^ { 2 } } . } } \end{array}
$$

It is easy to see that one of the conditions (4.11)

$$
x _ { 3 1 } x _ { 3 } - x _ { 3 3 } x _ { 1 } = - \widehat { x } _ { 1 }
$$

is satisfied. Likewise, we can prove that another condition of (4.11) is also satisfied.

From (4.17), we have $C = c J$ , where $c$ is an arbitrary constant and

$$
J = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { } } & { { } } \\ { { - 1 } } & { { 0 } } \end{array} \right] .
$$

Therefore, the lemma is completed.

# 12.4.5 Lie–Poisson Scheme on Heavy Top

The Lie–Poisson algorithm as we discussed in the previous sections are based on the dual space of semi-simple Lie algebra. In practice, we often have some Lie-Poisson system whose configuration space is not based on semi-simple Lie algebra, but on the dual space of the semi-product of Lie algebra and linear space. Such systems include but not limited to heavy top and compressible hydrodynamics flows. The reader can refer to literature[MRW90] for a more detailed discussion. In such configuration space, there exists no momentum mapping as we discussed in previous sections. The angular momentum is preserved only along a specific direction. Therefore, the generating function theory is no longer valid. However, using Lie–Poisson equations under local coordinates, we can construct the Lie–Poisson algorithm and the angular momentum preserving scheme. We will illustrate this by heavy top as an example.

Heavy top is a gravity body under the action of gravity with a fixed point. The free rigid body is a heavy top with the fixed point in center of mass. Its configuration space is 3 dimensional Euclid space $E ( 3 )$ . Its Lie algebra is no longer semisimple. Its phase space $e ^ { * } ( 3 )$ has 6 coordinates $\{ x _ { 1 } , x _ { 2 } , x _ { 3 } , p _ { 1 } , p _ { 2 } , p _ { 3 } \}$ . The Poisson bracket operation on $e ^ { * } ( 3 )$ is

$$
\{ x _ { i } , x _ { j } \} = \varepsilon _ { i j k } x _ { k } , ~ \{ x _ { i } , p _ { i } \} = \varepsilon _ { i j k } p _ { k } , ~ \{ p _ { i } , p _ { j } \} = 0 ,
$$

where

$$
\varepsilon _ { i j k } = { \left\{ \begin{array} { l l } { ( i , j , k ) , } & { i , j , k { \mathrm { ~ i s ~ n o t ~ t h e ~ s a m e } } , } \\ { 0 , } & { i , j , k { \mathrm { ~ i s ~ t h e ~ s a m e } } . } \end{array} \right. }
$$

There are two independent Casimir functions for bracket (4.18)

$$
f _ { 1 } = \sum _ { i = 1 } ^ { 3 } p _ { i } ^ { 2 } , \quad f _ { 2 } = \sum _ { i = 1 } ^ { 3 } p _ { i } x _ { i } .
$$

Let $H ( x , p )$ be the Hamiltonian function of system. Introducing notation $u _ { i } =$ ${ \frac { \partial H } { \partial p _ { i } } } , \Omega _ { i } = { \frac { \partial { \bar { H } } } { \partial x _ { i } } }$ . Then the Lie–Poisson equation has the form of Kirchhoff equation

$$
\dot { p } = [ p , \Omega ] , \quad \dot { x } = [ x , \omega ] + [ p , u ] ,
$$

where square bracket denotes cross product. $H$ is the system’s energy, $x$ and $p$ are angular momentum, and momentum under momentum coordinate. For a general case, energy $H$ is of quadratic form about $x , p$ , and positive definite, which can be given as follows


<!-- chunk 0009: pages 561-630 -->
$$
2 H = \sum _ { i = 1 } ^ { 3 } a _ { i } x _ { i } ^ { 2 } + \sum _ { i , j = 1 } ^ { 3 } b _ { i j } ( p _ { i } x _ { j } + x _ { i } p _ { j } ) + \sum _ { i , j = 1 } ^ { 3 } c _ { i j } p _ { i } p _ { j } .
$$

For heavy top, the energy is often expressed as the sum of kinetic energy and potential energy, i.e.,

$$
H ( x , p ) = \frac { x _ { 1 } ^ { 2 } } { 2 I _ { 1 } } + \frac { x _ { 2 } ^ { 2 } } { 2 I _ { 2 } } + \frac { x _ { 3 } ^ { 2 } } { 2 I _ { 3 } } + \gamma _ { 1 } p _ { 1 } + \gamma _ { 2 } p _ { 2 } + \gamma _ { 3 } p _ { 3 } ,
$$

where $I _ { i }$ is the main movement inertia of the rigid body, $\gamma _ { i }$ $( i = 1 , 2 , 3$ ) are three coordinates of the center of mass. It is easy to see that this is a separable system.

The structure matrix of the Lie–Poisson system is

$$
\left[ \begin{array} { c c } { { J ( x ) } } & { { J ( p ) } } \\ { { } } & { { } } \\ { { J ( p ) } } & { { O } } \end{array} \right] ,
$$

where $J ( x )$ is defined in Subsection 12.4.4.

It is difficult to construct Lie–Poisson algorithm on heavy top than on the free rigid body because the generating function methods are no longer suitable. However, it may become easier by the composition method and the Lemma 4.3.

We will first split the Hamiltonian function $H$ of heavy top system into six part $H = \sum _ { i = 1 } ^ { 6 } H _ { i }$ , where

$$
H _ { i } = \frac { x _ { i } ^ { 2 } } { 2 I _ { i } } , H _ { i + 3 } = \gamma _ { i } p _ { i } , i = 1 , 2 , 3 .
$$

We will take $H _ { 1 } , H _ { 4 }$ as examples to construct Lie–Poisson scheme.

First, we will take $H _ { 1 }$ as the Hamilton function, then

$$
\left[ \begin{array} { c } { \dot { x } } \\ { \dot { p } } \end{array} \right] = \left[ \begin{array} { c c } { J ( x ) } & { J ( p ) } \\ { J ( p ) } & { 0 } \end{array} \right] \left[ \begin{array} { c } { \frac { \partial H _ { 1 } } { \partial x } } \\ { 0 } \end{array} \right] ,
$$

after manipulating, we get

$$
\left\{ \begin{array} { l } { x _ { 1 } = 0 , } \\ { x _ { 2 } = \frac { x _ { 3 } x _ { 1 } } { I _ { 1 } } , } \\ { x _ { 3 } = - \frac { x _ { 2 } x _ { 1 } } { I _ { 1 } } , } \\ { p _ { 1 } = 0 , } \\ { p _ { 2 } = \frac { x _ { 1 } p _ { 3 } } { I _ { 1 } } , } \\ { p _ { 3 } = - \frac { x _ { 1 } p _ { 2 } } { I _ { 1 } } . } \end{array} \right.
$$

Theorem 4.4. The Midpoint scheme of (4.22) is Poisson scheme for heavy top.

Proof. By Theorem 1.2, the midpoint scheme is the Poisson scheme iff mapping

$$
( x , p ) \longrightarrow ( { \widehat { x } } , { \widehat { p } } )
$$

satisfies

$$
\left[ \begin{array} { l l } { \frac { \partial \widehat { x } } { \partial x } } & { \frac { \partial \widehat { x } } { \partial p } } \\ { \frac { \partial \widehat { p } } { \partial x } } & { \frac { \partial \widehat { p } } { \partial p } } \end{array} \right] \left[ \begin{array} { l l } { J ( x ) } & { J ( p ) } \\ { J ( p ) } & { O } \end{array} \right] \left[ \begin{array} { l l } { \frac { \partial \widehat { x } } { \partial x } } & { \frac { \partial \widehat { p } } { \partial x } } \\ { \frac { \partial \widehat { x } } { \partial p } } & { \frac { \partial \widehat { p } } { \partial p } } \end{array} \right] = \left[ \begin{array} { l l } { J ( \widehat { x } ) } & { J ( \widehat { p } ) } \\ { J ( \widehat { p } ) } & { O } \end{array} \right] .
$$

Denote $\left( \frac { \partial \widehat { y } } { \partial z } \right) = \widehat { y } _ { z }$ , then the expand Equation (4.23),

$$
\left\{ \begin{array} { l l } { \widehat { x } _ { x } J ( x ) \widehat { x } _ { x } ^ { \mathrm { T } } = J ( \widehat { x } ) , } \\ { \widehat { x } _ { x } J ( x ) \widehat { p } _ { x } ^ { \mathrm { T } } + \widehat { x } _ { x } J ( p ) \widehat { p } _ { p } ^ { \mathrm { T } } = J ( \widehat { p } ) , } \\ { \widehat { p } _ { x } J ( x ) \widehat { p } _ { x } ^ { \mathrm { T } } + \widehat { p } _ { p } J ( p ) \widehat { p } _ { x } ^ { \mathrm { T } } + \widehat { p } _ { x } J ( p ) \widehat { p } _ { p } ^ { \mathrm { T } } = 0 . } \end{array} \right.
$$

From the results of Subsection12.4.4, the first equation of system (4.24) is obviously hold. Note also

$$
\widehat { p } _ { x } = \left[ \begin{array} { c c c } { 0 } & { p _ { 2 1 } } & { p _ { 3 1 } } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] , \quad \widehat { p } _ { p } = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { p _ { 2 2 } } & { p _ { 2 3 } } \\ { 0 } & { p _ { 3 2 } } & { p _ { 3 3 } } \end{array} \right] ,
$$

where p21 = $p _ { 2 1 } = \frac { \partial \widehat { p } _ { 2 } } { \partial x _ { 1 } }$ , $p _ { 3 1 } = \frac { \partial \widehat { p } _ { 3 } } { \partial x _ { 1 } }$ $p _ { i j } = \frac { \partial \widehat { p } _ { i } } { \partial p _ { j } } \left( i , j = 2 , 3 \right)$ . Through the computation, we have

$$
\begin{array} { l l } { { p _ { 2 2 } = x _ { 2 2 } , \quad p _ { 2 3 } = x _ { 2 3 } , \quad p _ { 3 2 } = x _ { 3 2 } , \quad p _ { 3 3 } = x _ { 3 3 } , \quad } } \\ { { \mathrm { } } } \\ { { p _ { 2 1 } = { \displaystyle \frac { \tau \widehat { p _ { 3 } } } { I _ { 1 } } } , \quad p _ { 3 1 } = { \displaystyle \frac { - \tau \widehat { p _ { 2 } } } { I _ { 1 } } } , \quad } } \end{array}
$$

where $a$ is defined by the Euler scheme (4.16).

Substituting (4.25) into Equation (4.24), the 2nd and 3rd equations of (4.24) are also hold. -

If $H _ { 4 }$ is taken as Hamiltonian function of a system, the equation degenerates into a constant equation. Then constructing Lie–Poisson scheme is trivial.

For a Hamiltonian function of general form, we need to perform a transformation, so that the equation is easier for constructing the Lie–Poisson scheme. Take the free rigid body as the example.

For a quadratic form, we have

$$
H = H _ { i } + H _ { i j } = \frac { 1 } { 2 } a _ { i } x _ { i } ^ { 2 } + \frac { 1 } { 2 } a _ { i j } ( x _ { i } + x _ { j } ) ^ { 2 } ,
$$

i.e., we can eliminate the mixed items and transform it into a sum of squares. Next, we can construct Lie–Poisson scheme for system with $H _ { i j }$ as Hamiltonian function. Take $H _ { 1 2 }$ as an example

$$
\dot { x } = J ( x ) \frac { \partial H _ { 1 2 } } { \partial x } .
$$

It is easy to see that $x _ { 1 } + x _ { 2 }$ is a Casimir function of system. Expanding Equation (4.26) yields

$$
\left[ \begin{array} { c } { \dot { x } _ { 1 } } \\ { \dot { x } _ { 2 } } \\ { \dot { x } _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { - a _ { 1 2 } x _ { 3 } ( x _ { 1 } + x _ { 2 } ) } \\ { a _ { 1 2 } x _ { 3 } ( x _ { 1 } + x _ { 2 } ) } \\ { a _ { 1 2 } ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } ) } \end{array} \right] .
$$

Since $x _ { 1 } + x _ { 2 }$ is a constant, denote $c = x _ { 1 } + x _ { 2 }$ , the Equation (4.27) becomes

$$
\left\{ \begin{array} { l l } { \dot { x } _ { 1 } = - c a _ { 1 2 } x _ { 3 } , } \\ { } \\ { \dot { x } _ { 2 } = c a _ { 1 2 } x _ { 3 } , } \\ { } \\ { \dot { x } _ { 3 } = c a _ { 1 2 } ( c - 2 x _ { 2 } ) . } \end{array} \right.
$$

The midpoint scheme to the above equations is no longer Lie–Poisson scheme. However, we can solve system of the Equations (4.28) analytically without difficulty.

# 12.4.6 Other Lie–Poisson Algorithm

Apart from the Lie–Poisson algorithm described above, we have other Lie–Poisson algorithms, which include but not limited to Scovel and MacLaclan[MS95] constrained Hamiltonian algorithm, and Veselov[Ves91b,Ves88] discrete Lagrangian system approach, as well as the reduction method mentioned before. Below, we will give a brief introduction to these method.

# 1. Constrained Hamiltonian algorithm

The detailed description about the constrained Hamiltonian algorithm can be found in literature[MS95] and its references. Here we apply it to rigid motion only.

The structure space for a rigid motion is $S O ( n ) = N$ . Take a larger linear space $M = g l ( n )$ . Then the constraint function of $N$ on $M$ is

$$
\phi ( \boldsymbol { q } ) = \boldsymbol { q } ^ { \mathrm { T } } \boldsymbol { q } - 1 , \quad \forall \ \boldsymbol { q } \in M .
$$

Note that $\phi ( q ) = 0$ on $N$ , and $\mathbf { d } \phi ( q ) = T _ { q } ( M ) \to \mathbf { R }$ is a differential mapping. Assume on $T ^ { * } M$ , there exists a non-constraint system of Hamiltonian equations

$$
\left\{ \begin{array} { l } { \dot { p } = - \partial _ { q } H , } \\ { ~ } \\ { \dot { q } = \partial _ { p } H . } \end{array} \right.
$$

Then on $T ^ { * } N$ , if the local coordinates $( p , q )$ on $T ^ { * } M$ is still used, we should have

$$
\phi ( q ) = 0 \Longrightarrow \mathrm { d } \phi \cdot \dot { q } = \mathrm { d } \phi \cdot \partial _ { p } H = \{ H , \phi \} .
$$

Therefore, on $T ^ { * } M$ , there exists an embedded submanifold

$$
C M = \{ ( p , q ) \in T ^ { * } M : \phi ( q ) = 0 , \{ H , \phi \} = 0 \} ,
$$

which can induce a mapping

$$
\psi : \quad C M \longrightarrow T ^ { * } M , \quad ( p , q ) \longrightarrow ( p _ { - } , q ) ,
$$

where $p _ { - } = \psi ( p , q )$ . It is easy to verify that this is an isomorphic mapping and preserving the symplectic structure.

There exist constrained equations of dynamic system on $C M$ ,

$$
\left\{ \begin{array} { l l } { \dot { q } = \partial _ { p } H , } \\ { ~ } \\ { \dot { p } = - \partial _ { q } H + \mathrm { d } \phi \cdot \mu . } \end{array} \right.
$$

If it is easy to construct structure-preserving scheme for the Equation (4.29) (e.g. when (4.29) is a separable system), then we can use map $\psi$ to induce the algorithm on $T N$ .

Take $S O ( n )$ as an example.

On $^ { T M }$ we have a Lagrangian function $L ( q , \dot { q } ) = \frac { 1 } { 2 } \operatorname { t r } \left( \dot { q } J \dot { q } ^ { \mathrm { T } } \right)$ . Using the Legendre transformation, we can obtain Hamiltonian function $H ( p , q ) = { \frac { 1 } { 2 } } \operatorname { t r } \left( p J ^ { - 1 } p ^ { \mathrm { T } } \right)$ on $T ^ { * } M$ . Therefore, using (4.29), we can obtain the constrained Hamiltonian equation of the dynamic system:

$$
\left\{ { \begin{array} { l } { { \dot { q } } = { \frac { 1 } { 2 } } p J ^ { - 1 } , } \\ { { \dot { p } } = \mathbf { d } \psi \cdot \mu = 2 q \mu , } \end{array} } \right.
$$

which is a separable Hamilton system obviously. It is easy to construct the explicit symplectic difference scheme. But on $T N$ , the Hamiltonian function becomes $H ( p , q ) = \frac { 1 } { 4 } \mathrm { t r } ( I ^ { - 1 } ( q ^ { \mathrm { T } } p ) ( q ^ { \mathrm { T } } p ) ^ { \mathrm { T } } )$ , and its Hamiltonian equations are

$$
\left\{ \begin{array} { l l } { \dot { q } = q I ^ { - 1 } ( q ^ { \mathrm { T } } p ) = \frac { \partial H } { \partial p } , } \\ { \dot { p } = p I ^ { - 1 } ( q ^ { \mathrm { T } } p ) = - \frac { \partial H } { \partial q } , } \end{array} \right.
$$

where $q \in S O ( n )$ , $q ^ { \mathrm { T } } p \in s o ( n )$ . This is not a separable Hamilton system. Therefore, constructing its symplectic difference method will be difficult and computationally complicated. However using (4.30) and maps $\psi$ , we can construct the algorithm for $S O ( n )$ easily. Note that ${ \psi } ( p ) = \frac { 1 } { 2 } ( p - q p ^ { \mathrm { T } } q )$ in this case.

Scovel and McLachlan[MS95] proved this algorithm preserves the momentum mapping. We remark that the constraint Hamiltonian system has advantage only when the expansion system is separable. Otherwise this algorithm is impractical. Take the rigid body as an example. On $T ^ { * } S O ( 3 )$ , if Euler equation is to be solved, there are only 6 unknowns. If we expand it to $T ^ { * } G L ( n )$ , the number of unknown becomes 18. If system is not separable, then the computation cost will definitely increase.

# 2. Veselov–Moser algorithm

Veselov–Moser algorithm $[ \mathrm { M V } 9 1 ]$ is to discretize Lagrange function first and then apply Legendre transformation to the discrete Lagrange function. The constructed algorithm preserves discreted symplectic structure, thus also preserves system’s Lie– Poisson structure. The concrete procedure is as follows:

$1 ^ { \circ }$ First discretize the Lagrange function. $2 ^ { \circ }$ Add constraint and find the solution for $\delta S = 0$ $3 ^ { \circ }$ Obtain the discrete equation. $4 ^ { \circ }$ Solve this equation.

For $S O ( n )$ , $S = \sum _ { k = 1 } ^ { n } \operatorname { t r } \left( X _ { k } J X _ { k + 1 } ^ { \mathrm { T } } \right)$ . The constrained Lagrange function is

$$
L = S + \sum _ { k = 1 } ^ { n } ( X _ { k } X _ { k } ^ { \mathrm { T } } - 1 ) ,
$$

then

$$
\delta L = 0 \Longrightarrow X _ { k + 1 } J + X _ { k - 1 } J = \Lambda _ { k } X _ { k } , \quad \forall \ k \in { \bf Z } ,
$$

from this, we can have a system of equations

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { M _ { k + 1 } = w _ { k } M _ { k } w _ { k } ^ { - 1 } , } \\ { M _ { k } = w _ { k } ^ { \mathrm { T } } J - J w _ { k } , } \end{array} \right. \quad w _ { k } \in O ( n ) , } \end{array}
$$

where $w _ { k } = X _ { k + 1 } ^ { - 1 } X _ { k }$ . It is easy to prove that this discrete system of equations converges to continuous system of Euler-Arnold equations:

$$
\left\{ \begin{array} { l l } { \dot { M } = [ M , \Omega ] , } \\ { M = J \Omega + \Omega J , } \end{array} \right. \quad \Omega \in o ( n ) .
$$

To solve Equation (4.32), the key lies in solving for $w _ { k }$ . In order to make iteration $( X _ { k } , Y _ { k } )  ( X _ { k + 1 } , Y _ { k + 1 } )$ symplectic, $Y _ { k } = X _ { k + 1 }$ , we need

$$
Y _ { k + 1 } J + X _ { k } J = \Lambda _ { k } X _ { k + 1 } , \quad \Lambda _ { k } \in S m ( n ) .
$$

This is because

$$
\begin{array} { l l l } { { Y _ { k + 1 } J + X _ { k } J } } & { { = } } & { { X _ { k + 1 } w _ { k + 1 } ^ { \mathrm { T } } J + X _ { k } J } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { X _ { k + 1 } ( w _ { k + 1 } ^ { \mathrm { T } } J + X _ { k + 1 } ^ { \mathrm { T } } X _ { k } J ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { X _ { k + 1 } ( w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J ) . } } \end{array}
$$

See also

$$
J w _ { k } ^ { \mathrm { T } } - w _ { k } J = M _ { k + 1 } = w _ { k + 1 } ^ { \mathrm { T } } J - J w _ { k + 1 } ,
$$

then

$$
J w _ { k } ^ { \mathrm { T } } + J w _ { k + 1 } = w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J ,
$$

i.e., $w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J$ is symmetric. Thus ∃ Λk, $\Lambda _ { k } = \Lambda _ { k } ^ { \mathrm { T } }$ , so that

$$
X _ { k + 1 } ( w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J ) = \Lambda _ { k } X _ { k + 1 } .
$$

Therefore,

$$
Y _ { k + 1 } J + X _ { k } J = \Lambda _ { k } X _ { k + 1 }
$$

satisfies symplectic condition.

The next question is how to solve $w _ { k } ^ { \mathrm { T } } J - J w _ { k } = M _ { k } = t m _ { k }$ for $w _ { k } ?$ The numerical experiments show that not all solutions $w _ { k }$ that satisfy Equations (4.32) are the solutions we want. To solve $\omega _ { k }$ quickly, we propose to use the Quaternion method. $w \in S O ( 3 )$ corresponds to an element $q = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } )$ in $S H _ { 1 }$ . Their relations will be given in Section 12.5. Then the second equation in Equation (4.32) becomes

$$
\left\{ \begin{array} { l l } { 2 ( \alpha _ { 2 } - \alpha _ { 1 } ) q _ { 2 } q _ { 1 } + 2 ( \alpha _ { 1 } + \alpha _ { 2 } ) q _ { 3 } q _ { 0 } = - \delta t m _ { 3 } , } \\ { 2 ( \alpha _ { 3 } - \alpha _ { 1 } ) q _ { 3 } q _ { 1 } - 2 ( \alpha _ { 3 } + \alpha _ { 1 } ) q _ { 2 } q _ { 0 } = \delta t m _ { 2 } , } \\ { 2 ( \alpha _ { 3 } - \alpha _ { 2 } ) q _ { 3 } q _ { 2 } + 2 ( \alpha _ { 3 } + \alpha _ { 2 } ) q _ { 1 } q _ { 0 } = - \delta t m _ { 1 } , } \end{array} \right.
$$

in addition,

$$
q _ { 0 } ^ { 2 } + q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } = 1 .
$$

Solving the above nonlinear equations for $\left( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } \right)$ is not an easy task. We found that when iteration step size is small, $q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 }$ behaves reasonable. However, when the step size is large, the solution behaves erratically. Numerical experiments show that solving these nonlinear equations is quite time-consuming, and hence this method is not recommended in practice.

# 3. Reduction method

Reduction method bases on the momentum mapping discussed in previous sections. We have mentioned that the solution of a Lie–Poisson system lies in a coadjoint orbit in Section 12.2, and this orbit has non-degenerated symplectic structure. If we can construct the symplectic algorithm on this reduced orbit, then this algorithm is naturally Lie–Poisson. Moreover it preserves the Casimir function and also preserves the orbit. Below, we will take $S O ( 3 )$ as an example to illustrate this method.

The coadjoint orbit of $S O ( 3 )$ is a two dimensional spherical surface $S _ { 2 } ^ { r }$ . On $S _ { 2 } ^ { r }$ , we have a symplectic structure

$$
\omega _ { \mu } ( \xi _ { \mathbf { g } ^ { * } } ( \mu ) , \eta _ { \mathbf { g } ^ { * } } ( \mu ) ) = - \mu [ \xi , \eta ] ,
$$

and Hamiltonian function

$$
H _ { \mu } ( A d _ { g ^ { - 1 } } ^ { * } \mu ) = \frac { 1 } { 2 } I ^ { - 1 } ( A d _ { g ^ { - 1 } } ^ { * } \mu ) ^ { 2 } ,
$$

where $A d _ { g ^ { - 1 } } ^ { * } \mu$ denotes an element on $S _ { 2 } ^ { r }$ .

How to choose the chart and local coordinate on $S _ { 2 } ^ { r }$ , so that the symplectic structure becomes simple, is very important. We once selected the spherical coordinate to be the local coordinate and the corresponding symplectic structure and Hamiltonian function become very complicated. However, if the Euler angle coordinate is used, the equations become very simple.

Let

$$
S _ { 2 } ^ { r } = \{ ( x , y , z ) ~ | ~ x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = r ^ { 2 } \} ,
$$

where $x , y , z$ are three angular momentums in the body description. Using Euler angle coordinate $\theta , \psi$ to do the following coordinate transformation:

$$
\left\{ \begin{array} { l l } { x = r \sin \theta \cos \varphi , } \\ { y = r \sin \theta \sin \varphi , } \\ { z = r \cos \theta . } \end{array} \right.
$$

Lie–Poisson (Euler) equation may become the following Hamiltonian equations:

$$
\left\{ \begin{array} { l } { \displaystyle \dot { \theta } = - \frac { 1 } { r \sin \theta } \frac { \partial H } { \partial \varphi } , } \\ { \displaystyle \dot { \varphi } = \frac { 1 } { r \sin \theta } \frac { \partial H } { \partial \theta } , } \end{array} \right.
$$

where

$$
H = { \frac { 1 } { 2 } } \left( { \frac { r ^ { 2 } \sin ^ { 2 } \theta \cos ^ { 2 } \varphi } { I _ { 1 } } } + { \frac { r ^ { 2 } \sin ^ { 2 } \theta \sin ^ { 2 } \varphi } { I _ { 2 } } } + { \frac { r ^ { 2 } \cos ^ { 2 } \theta } { I _ { 3 } } } \right) .
$$

We can construct a non-standard symplectic algorithm for Equations (4.34) or we can simplify the problem further by transformation

$$
( \theta , \varphi )  ( \cos \theta , \varphi ) = ( x _ { 1 } , x _ { 2 } ) ,
$$

then

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } x _ { 1 } } { \mathrm { d } t } = \frac { 1 } { r } \frac { \partial H } { \partial x _ { 2 } } , } \\ { \frac { \mathrm { d } x _ { 2 } } { \mathrm { d } t } = - \frac { 1 } { r } \frac { \partial H } { \partial x _ { 1 } } . } \end{array} \right.
$$

This is a Hamiltonian system with standard symplectic structure, and its symplectic algorithm is easy to construct.

To sum up, constructing Lie–Poisson scheme for a Lie–Poisson system has three methods. The first method is to lift it to $T ^ { * } G$ and construct the symplectic algorithm (includes constraint Hamiltonian method) on it. The second is the direct construction based on $\mathbf { g } ^ { * }$ (generating function method and composition method). The third is to construct symplectic algorithm on the reduced coadjoint orbit.

# 12.5 Relation Among Some Special Group and Its Lie Algebra

In this section, we present relation among special group and its Lie algebra.

# 12.5.1 Relation Among $S O ( 3 ) , s o ( 3 )$ and $S H _ { 1 } , S U ( 2 )$

Let

$$
\begin{array} { l } { { \Lambda \in S O ( 3 ) , \quad \Lambda \Lambda = 1 , \quad | \Lambda | = 1 , } } \\ { { \nonumber } } \\ { { \widehat { \xi } \in s o ( 3 ) \Longrightarrow \widehat { \xi } + \widehat { \xi } ^ { \mathrm { T } } = 0 , } } \end{array}
$$

$q \in S H _ { 1 }$ is a normal Quaternion $q = ( q _ { 0 } , \overline { { { q } } } ) = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } ) , \overline { { { q } } } = ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) ,$

$$
q _ { 0 } ^ { 2 } + \lVert \overline { { q } } \rVert ^ { 2 } = 1 = q _ { 0 } ^ { 2 } + q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } .
$$

We assume

$$
\forall \xi \in \mathbf { R } ^ { 3 } , \quad \xi = ( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } ) \Longrightarrow \widehat { \xi } = \left[ \begin{array} { c c c } { 0 } & { - \xi _ { 3 } } & { \xi _ { 2 } } \\ { \xi _ { 3 } } & { 0 } & { - \xi _ { 1 } } \\ { - \xi _ { 2 } } & { \xi _ { 1 } } & { 0 } \end{array} \right] \in s o ( 3 ) ,
$$

$\xi$ is called the axial quantity of ${ \widehat { \xi } } .$ When $\widehat { A } \in s o ( 3 )$ , $A$ expresses its axial quantity.

# 1. Transformation between $S O ( 3 )$ and $S H _ { 1 }$

$\forall ~ q \in S H _ { 1 }$ , $x \in \mathrm { ~ } q _ { 0 } \simeq \mathbf { R } ^ { 3 }$ , $q x q ^ { - 1 }$ represents a rotation of $x$ . Using isomorphic mapping:

$$
{ \cal A } ( q ) = \left[ \begin{array} { c c } { { q _ { 0 } + q _ { 1 } \mathrm { i } } } & { { q _ { 2 } + q _ { 3 } \mathrm { i } } } \\ { { - q _ { 2 } + q _ { 3 } \mathrm { i } } } & { { q _ { 0 } - q _ { 1 } \mathrm { i } } } \end{array} \right] , \quad H \simeq { \bf C } ^ { 2 } ,
$$

we can obtain $\forall ~ q \in H , \exists \Lambda \in S O ( 3 ) , \forall ~ x \in$ , we have

$$
A ( q x q ^ { - 1 } ) = A ( 0 , \Lambda x ) .
$$

From this we can get $\Lambda$ .

Given $q = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } )$ , then

$$
\Lambda = 2 \left[ \begin{array} { c c c c } { { q _ { 0 } ^ { 2 } + q _ { 1 } ^ { 2 } - \frac { 1 } { 2 } } } & { { q _ { 1 } q _ { 2 } - q _ { 0 } q _ { 3 } } } & { { q _ { 0 } q _ { 2 } + q _ { 1 } q _ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { q _ { 1 } q _ { 2 } + q _ { 0 } q _ { 3 } } } & { { q _ { 0 } ^ { 2 } + q _ { 2 } ^ { 2 } - \frac { 1 } { 2 } } } & { { q _ { 2 } q _ { 3 } - q _ { 0 } q _ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { q _ { 1 } q _ { 3 } - q _ { 0 } q _ { 2 } } } & { { q _ { 0 } q _ { 1 } + q _ { 2 } q _ { 3 } } } & { { q _ { 0 } ^ { 2 } + q _ { 3 } ^ { 2 } - \frac { 1 } { 2 } } } \end{array} \right] ,
$$

or simplify as

$$
\Lambda = ( 2 q _ { 0 } ^ { 2 } - 1 ) 1 + 2 q _ { 0 } \widehat { q } + 2 q \otimes q .
$$

It is easy to see that, if $\Lambda = ( \Lambda _ { i j } )$ is known, then

$$
\left. \begin{array} { l } { q _ { 0 } = \frac { 1 } { 2 } \sqrt { 1 + \operatorname { t r } \Lambda } , } \\ { q _ { 1 } = \frac { \left( Q _ { 3 2 } - Q _ { 2 3 } \right) } { 4 q _ { 0 } } } \\ { q _ { 2 } = \frac { \left( Q _ { 1 3 } - Q _ { 3 1 } \right) } { 4 q _ { 0 } } } \\ { q _ { 3 } = \frac { \left( Q _ { 2 1 } - Q _ { 1 2 } \right) } { 4 q _ { 0 } } } \end{array} \right\} \Longrightarrow q = \frac { 1 } { 4 q _ { 0 } } ( \Lambda - \Lambda ^ { \operatorname { T } } ) .
$$

# 2. Relation between $s o ( 3 )$ and $S O ( 3 )$

The relation between $s o ( 3 )$ and $S O ( 3 )$ is the relation between Lie algebra and Lie group. Let $\widehat { \xi }$ be an antisymmetry matrix for the axial quantity $\bar { \xi }$ , then $\exp \left( \widehat { \varepsilon } \right)$ denotes a rotation in $S O ( 3 )$ . We have the expansion

$$
\exp \left( { \widehat { \xi } } \right) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { n ! } } { \widehat { \xi } } ^ { n } \in S O ( 3 ) .
$$

According to the properties of $S O ( 3 )$ , this expansion has a closed form, i.e., the Rodrigue formula

$$
\Lambda = \exp \left( \widehat { \xi } \right) = 1 + \frac { \sin \| \xi \| } { \| \xi \| } \widehat { \xi } + \frac { 1 } { 2 } \frac { \sin ^ { 2 } \left( \frac { 1 } { 2 } \| \xi \| \right) } { \left( \frac { 1 } { 2 } \| \xi \| \right) ^ { 2 } } \widehat { \xi } ^ { 2 } .
$$

We have two proofs of the above formula: one is from the geometry point of view and the other is from algebra point of view. Below, we will give details on the algebraic proof.

$\forall \widehat { \xi } \in s o ( 3 )$ , the following results hold after simple calculations:

$$
\widehat { \xi } ^ { 3 } = - \widehat { \xi } , \widehat { \xi } ^ { 4 } = - \widehat { \xi } ^ { 2 } , | \xi | = 1 .
$$

Substitute them into the above series expansion,

$$
\begin{array} { l } { { \exp \left( \widehat { \xi } \right) = \exp \left( \left\| \xi \right\| \cdot \widehat { n } \right) \left( n = \displaystyle \frac { \xi } { \| \xi \| } \right) } } \\ { { = 1 + \sin \left\| \xi \right\| \widehat { n } + \left( 1 - \cos \left\| \xi \right\| \right) \widehat { n } ^ { 2 } } } \\ { { = 1 + \displaystyle \frac { \sin \left\| \xi \right\| } { \left\| \xi \right\| } \widehat { \xi } + \displaystyle \frac { 1 } { 2 } \frac { \sin ^ { 2 } \displaystyle \frac { 1 } { 2 } \| \xi \| } { \left( \displaystyle \frac { 1 } { 2 } \| \xi \| \right) ^ { 2 } } \widehat { \xi } ^ { 2 } . } } \end{array}
$$

We can prove that $\| \xi \|$ is the angle of rotation $\exp \left( \widehat { \xi } \right)$ .

# 3. Transformation between $S O ( 3 )$ and $S H _ { 1 }$

The relation between $S O ( 3 )$ and $S H _ { 1 }$ is manifested by the relation between $s o ( 3 )$ and $S H _ { 1 }$ . A rotation in $S O ( 3 )$ , $( \theta , n )  ( \| \xi \| , \xi )$ ,

$$
\begin{array} { r c l } { { \forall \left( \| \xi \| , \xi \right) \in S O ( 3 ) \implies \widehat { \xi } \in s o ( 3 ) } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { \implies q _ { 0 } = \cos \frac { 1 } { 2 } \| \xi \| , } } & { { } } \\ { { } } & { { } } & { { } } \\ { { q } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \left( \frac { \sin \displaystyle \frac { 1 } { 2 } \| \xi \| } { \displaystyle \frac { 1 } { 2 } \| \xi \| } \right) \xi . } } \end{array}
$$

When $\| \xi \| \ll 1$ , we use

$$
{ \frac { \sin x } { x } } = 1 - { \frac { x ^ { 2 } } { 6 } } + { \frac { x ^ { 4 } } { 1 2 0 } } - { \frac { x ^ { 6 } } { 5 0 4 0 } }
$$

to deal with the singularity situation.

If $q _ { 0 } ^ { 2 } + \| q \| ^ { 2 } \neq 1$ , normalization is needed, which is just divided by $\sqrt { q _ { 0 } ^ { 2 } + \| q \| ^ { 2 } }$

Given $( q _ { 0 } , q ) \in S H _ { 1 }$ , we need to solve for $\widehat { \xi }$ . Since $\xi$ has the same direction as $q$ , we have

$$
\xi = \| \xi \| { \frac { q } { \| q \| } } ,
$$

where $\| \xi \|$ can be given by $\left\| \xi \right\| = 2 \sin ^ { - 1 } ( \left\| q \right\| )$ .

# 12.5.2 Representations of Some Functions in $S O ( 3 )$

By definition, we have

$$
\begin{array} { l } { { \displaystyle i e x ( \xi ) = \sum _ { n = 0 } ^ { \infty } \frac { \xi ^ { n } } { ( n + 1 ) ! } , } } \\ { { \displaystyle \chi ( \xi ) i e x ( - \xi ) = I d _ { \xi } . } } \end{array}
$$

For ${ \widehat { \xi } } \in s o ( 3 )$ , from $\left( \frac { \widehat { \xi } } { | | \xi | | } \right) ^ { 3 } = - \frac { \widehat { \xi } } { | | \xi | | }$ , we have

$$
{ \begin{array} { r l } { i e x ( - { \widehat { \xi } } ) } & { = \displaystyle \sum _ { n = 0 } ^ { \infty } { \frac { ( - { \widehat { \xi } } ) ^ { n } } { ( n + 1 ) ! } } = \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { ( { \widehat { \xi } } ) ^ { 2 k } } { ( 2 k + 1 ) ! } } + \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { ( - { \widehat { \xi } } ) ^ { 2 k + 1 } } { ( 2 k + 2 ) ! } } } \\ & { = \displaystyle \ 1 + \displaystyle \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k + 1 } \| \xi \| ^ { 2 k } } { ( 2 k + 1 ) ! } } \left( { \frac { { \widehat { \xi } } } { \| \xi \| } } \right) ^ { 2 } + \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { k + 1 } \| \xi \| ^ { 2 k + 1 } } { ( 2 k + 2 ) ! } } \cdot { \frac { { \widehat { \xi } } } { \| \xi \| } } } \\ & { = \displaystyle \ 1 + { \frac { | \xi | - \sin | \xi | } { | \xi | ^ { 3 } } } { \widehat { \xi } } ^ { 2 } + \displaystyle { \frac { \cos | \xi | - 1 } { | \xi | ^ { 2 } } } { \widehat { \xi } } } \\ & { = \displaystyle \ 1 + c _ { 1 } { \widehat { \xi } } + c _ { 2 } { \widehat { \xi } } ^ { 2 } , } \end{array} }
$$

where c1 = cos |ξ| − 1 , $c _ { 1 } ~ = ~ \frac { \cos ~ | \xi | - 1 } { | \xi | ^ { 2 } } , c _ { 2 } ~ = ~ \frac { | \xi | - \sin ~ | \xi | } { | \xi | ^ { 3 } }$ |ξ| − sin |ξ|3 . χ(ξ) can be obtained by formula $\chi ( \widehat { \xi } ) i e x ( - \widehat { \xi } ) = I d _ { \xi }$ .

Let $\chi ( \widehat { \xi } ) = 1 + a _ { 1 } \widehat { \xi } + a _ { 2 } \widehat { \xi } ^ { 2 }$ , then

$$
\begin{array} { r c l } { { \chi ( \widehat \xi ) i e x ( - \widehat \xi ) } } & { { = } } & { { ( 1 + a _ { 1 } \widehat \xi + a _ { 2 } \widehat \xi ^ { 2 } ) ( 1 + c _ { 1 } \widehat \xi + c _ { 2 } \widehat \xi ^ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 1 + ( a _ { 1 } + c _ { 1 } ) \widehat \xi + ( a _ { 1 } c _ { 1 } + c _ { 2 } + a _ { 2 } ) { \widehat \xi ^ { 2 } } + ( a _ { 1 } c _ { 2 } + a _ { 2 } c _ { 1 } ) { \widehat \xi ^ { 3 } } + a _ { 2 } c _ { 2 } { \widehat \xi ^ { 4 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 1 + ( a _ { 1 } + c _ { 1 } - ( a _ { 1 } c _ { 2 } + a _ { 2 } c _ { 1 } ) | \xi | ^ { 2 } ) \widehat \xi + ( c _ { 2 } + a _ { 2 } + a _ { 1 } c _ { 1 } - a _ { 2 } c _ { 2 } | \xi | ^ { 2 } ) \widehat \xi } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { I d , } } \end{array}
$$

therefore

$$
\left\{ \begin{array} { l l } { a _ { 1 } + c _ { 1 } - \left( a _ { 1 } c _ { 2 } + a _ { 2 } c _ { 1 } \right) | \xi | ^ { 2 } = 0 , } \\ { a _ { 1 } c _ { 1 } + c _ { 2 } + a _ { 2 } - a _ { 2 } c _ { 2 } | \xi | ^ { 2 } = 0 . } \end{array} \right.
$$

Solving the above equations, we have

$$
\begin{array} { l } { { a _ { 1 } = \displaystyle \frac { - c _ { 1 } } { ( 1 - c _ { 2 } | \xi | ^ { 2 } ) ^ { 2 } + c _ { 1 } ^ { 2 } | \xi | ^ { 2 } } = \displaystyle \frac { 1 - \cos | \xi | } { ( \sin | \xi | ) ^ { 2 } + ( 1 - \cos | \xi | ) ^ { 2 } } , \smallskip } } \\ { { a _ { 2 } = \displaystyle \frac { - c _ { 2 } + c _ { 2 } | \xi | ^ { 2 } + c _ { 1 } ^ { 2 } } { ( 1 - c _ { 2 } | \xi | ^ { 2 } ) ^ { 2 } + c _ { 1 } ^ { 2 } | \xi | ^ { 2 } } = \displaystyle \frac { \displaystyle \frac { ( \cos | \xi | - 1 ) ^ { 2 } } { | \xi | ^ { 2 } } + \displaystyle \frac { \sin | \xi | - | \xi | } { | \xi | } + ( \sin | \xi | - | \xi | ) | \xi | } { ( \sin | \xi | ) ^ { 2 } + ( 1 - \cos | \xi | ) ^ { 2 } } . } } \end{array}
$$

# Bibliography

[AKW93] M. Austin, P. S. Krishnaprasad, and L.-S. Wang: Almost Poisson integration of rigid body systems. J. of Comp. Phys., 107:105–117, (1993).   
[AM78] R. Abraham and J. E. Marsden: Foundations of Mechanics. Addison-Wesley, Reading, MA, Second edition, (1978).   
[AN90] A. I. Arnold and S.P. Novikov: Dynomical System IV. Springer Verlag, Berlin Heidelberg, (1990).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[CFSZ08] E. Celledoni, F. Fasso, N. S \` afstr ¨ om, and A. Zanna: The exact computation of the ¨ free rigid body motion and its use in splitting methods. SIAM J. Sci. Comput., 30(4):2084– 2112, (2008).   
[CG93] P. E. Crouch and R. Grossman: Numerical integration of ordinary differential equations on manifolds. J. Nonlinear. Sci., 3:1–33, (1993).   
[CS90] P. J. Channell and C. Scovel: Symplectic integration of Hamiltonian systems. Nonlinearity, 3:231–259, (1990).   
[CS91] P. J. Channel and J. S. Scovel: Integrators for Lie–Poisson dynamical systems. Physica D, 50:80–88, (1991).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen86] K. Feng: Symplectic geometry and numerical methods in fluid dynamics. In F. G. Zhuang and Y. L. Zhu, editors, Tenth International Conference on Numerical Methods in Fluid Dynamics, Lecture Notes in Physics, pages 1–7. Springer, Berlin, (1986).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FQ91] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FWQ90] K. Feng, H.M. Wu, and M.Z. Qin: Symplectic difference schemes for linear Hamiltonian canonical systems. J. Comput. Math., 8(4):371–380, (1990).   
[FWQW89] K. Feng, H. M. Wu, M.Z. Qin, and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[Ge91] Z. Ge: Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, (1991).   
[GM88] Z. Ge and J. E. Marsden: Lie–Poisson–Hamilton–Jacobi theory and Lie–Poisson integrators. Physics Letters A, pages 134–139, (1988).   
[HV06] E. Hairer and G. Vilmart: Preprocessed discrete Moser–Veselov algorithm for the full dynamics of the rigid body. J. Phys. A, 39:13225–13235, (2006).   
[Kar04] B. Karasozen: Poisson integrator. ¨ Math. Comput. Modelling, 40:1225–1244, (2004).   
[Lie88] S. Lie: Zur theorie der transformationsgruppen. Christiania, Gesammelte Abh., Christ. Forh. Aar., 13, (1988).   
[LQ95a] S. T. Li and M. Qin: Lie–Poisson integration for rigid body dynamics. Computers Math. Applic., 30:105–118, (1995).   
[LQ95b] S. T. Li and M. Qin: A note for Lie–Poisson– Hamilton–Jacobi equation and Lie– Poisson integrator. Computers Math. Applic., 30:67–74, (1995).   
[McL93] R.I. McLachlan: Explicit Lie–Poisson integration and the Euler equations. Physical Review Letters, 71:3043–3046, (1993).   
[MR99] J. E. Marsden and T. S. Ratiu: Introduction to Mechanics and Symmetry. Number 17 in Texts in Applied Mathematics. Springer-Verlag, Berlin, Second edition, (1999).   
[MRW90] J.E. Marsden, T. Radiu, and A. Weistein: Reduction and hamiltonian structure on dual of semidirect product Lie algebra. Contemporary Mathematics, 28:55–100, (1990).   
[MS95] R. I. McLachlan and C. Scovel: Equivariant constrained symplectic integration. J. Nonlinear. Sci., 5:233–256, (1995).   
[MS96] R. I. McLachlan and C. Scovel: A Survey of Open Problems in Symplectic Integration. In J. E. Mardsen, G. W. Patrick, and W. F. Shadwick, editors, Integration Algorithms and Classical Mechanics, pages 151–180. American Mathematical Society, New York, (1996).   
[MV91] J. Moser and A. P. Veselov: Discrete versions of some classical integrable systems and factorization of matrix polynomials. Communications in Mathematical Physics, 139:217– 243, (1991).   
[MW83] J.E. Marsden and A. Weinstein: Coadjoint orbits, vortices and Clebsch variables for incompressible fluids. Phys D, 7: (1983).   
[MZ05] R.I. McLachlan and A. Zanna: The discrete Moser–Veselov algorithm for the free rigid body. Foundations of Computational Mathematics, 5(1):87–123, (2005).   
[Olv93] P. J. Olver: Applications of Lie Groups to Differential Equations. GTM 107. Springer-Verlag, Berlin, Second edition, (1993).   
[Qin89] M. Z. Qin: Cononical difference scheme for the Hamiltonian equation. Mathematical Methodsand in the Applied Sciences, 11:543–557, (1989).   
[TF85] H. Tal-Fzer: Spectral method in time for hyperbolic equations. SIAM J. Numer. Anal., 23(1):11–26, (1985).   
[Ves88] A.P. Veselov: Integrable discrete-time systems and difference operators. Funkts. Anal. Prilozhen, 22:1–33, (1988).   
[Ves91] A.P. Veselov: Integrable maps. Russian Math. Surveys,, 46:1–51, (1991).   
[Wan91] D. L. Wang: Symplectic difference schemes for Hamiltonian systems on Poisson manifolds. J. Comput. Math., 9(2):115–124, (1991).   
[ZQ94] W. Zhu and M. Qin: Poisson schemes for Hamiltonian systems on Poisson manifolds. Computers Math. Applic., 27:7–16, (1994).   
[ZS07a] R.van Zon and J. Schofield: Numerical implementation of the exact dynamics of free rigid bodies. J. of Comp. Phys., 221(1):145–164, (2007).   
[ZS07b] R.van Zon and J. Schofield: Symplectic algorithms for simulations of rigid body systems using the exact solution of free motion. Physical Review E, 50:5607, (2007).
