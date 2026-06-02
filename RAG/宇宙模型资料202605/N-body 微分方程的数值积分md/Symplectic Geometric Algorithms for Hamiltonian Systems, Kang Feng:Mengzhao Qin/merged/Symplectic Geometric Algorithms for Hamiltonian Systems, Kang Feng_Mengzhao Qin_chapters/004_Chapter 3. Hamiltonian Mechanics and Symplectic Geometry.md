# Chapter 3. Hamiltonian Mechanics and Symplectic Geometry

Hamiltonian mechanics is geometry in phase space. Phase space has the structure of a symplectic manifold.

# 3.1 Symplectic Manifold

A symplectic manifold is a smooth manifold $M$ equipped with a closed, nondegenerate, 2-form called the symplectic form. On a symplectic manifold, as on a Riemannian manifold, there is a natural isomorphism between the vector field and the 1-form. Symplectic manifolds arise naturally in abstract formulations of classical mechanics and analytical mechanics as the cotangent bundles of manifolds, e.g., in the Hamiltonian formulation of classical mechanics, which provides one of the major motivations for the field. The set of all possible configurations of a system is modelled as a manifold, and this manifold’s cotangent bundle describes the phase space of the system.

Any real-valued differentiable function $H$ on a symplectic manifold can serve as an energy function or Hamiltonian. Associated to any Hamiltonian is a Hamiltonian vector field; the integral curves of the Hamiltonian vector field are solutions to the Hamilton–Jacobi equations. The Hamiltonian vector field defines a flow on the symplectic manifold, called a Hamiltonian flow or symplectomorphism. By Liouville’s theorem, Hamiltonian flows preserve the volume form on the phase space. The vector fields on a manifold form a Lie algebra. The Hamiltonian vector fields on a symplectic manifold form a Lie algebra. The operation in this algebra is called Poisson bracket.

# 3.1.1 Symplectic Structure on Manifolds

Definition 1.1. Let $M _ { 2 n }$ be an even-dimensional differential manifold. A symplectic structure on $M _ { 2 n }$ is a closed nondegenerate differential 2-form $\omega$ on $M _ { 2 n } ^ { \mathrm { \tiny [ A i \bar { M } 7 8 , \bar { A } r n 8 9 ] } }$ .

$1 ^ { \circ }$ d $\omega = 0$ is closed. $2 ^ { \circ }$ $\forall x \in M , \exists \xi \in T _ { x } M$ , s.t., if

$$
\omega ( \xi , \eta ) = 0 , \quad \forall \eta \in T _ { x } { \cal M } ,
$$

then $\xi = 0$ (nondegenerate).

The pair $( M , \omega )$ is called a symplectic manifold. We call it a presymplectic (almost symplectic) manifold, if only condition $1 ^ { \circ }$ $( 2 ^ { \circ }$ ) is satisfied.

Example 1.2. Consider the vector space $\mathbf { R } ^ { 2 n }$ with coordinates $( p _ { i } , q _ { i } )$ . Let $\omega =$ $\sum _ { i = 1 } ^ { n } \mathbf { d } p _ { i } \wedge \mathbf { d } q _ { i } .$ . Then, $\omega$ defines a symplectic structure. Given two tangent vectors

$$
\xi ^ { j } = ( \xi _ { 1 } ^ { j } , \cdot \cdot \cdot , \xi _ { n } ^ { j } ; \eta _ { 1 } ^ { j } , \cdot \cdot \cdot , \eta _ { n } ^ { j } ) , \quad j = 1 , 2 ,
$$

we have

$$
\omega ( \xi ^ { 1 } , \xi ^ { 2 } ) = \sum _ { i = 1 } ^ { n } \eta _ { i } ^ { 1 } \cdot \xi _ { i } ^ { 2 } - \eta _ { i } ^ { 2 } \cdot \xi _ { i } ^ { 1 } .
$$

This example shows that any symplectic manifold can have standard symplectic structure at least locally.

Exercise 1.3. Verify that $( \mathbf { R } ^ { 2 n } , \omega )$ is a symplectic manifold. For $n = 1$ , $\omega$ becomes an area measure on a plane.

# 3.1.2 Standard Symplectic Structure on Cotangent Bundles

Let $M$ be an $n$ -dimensional differential manifold. A 1-form on $T _ { x } M$ , the tangent space to $M$ at a point $x$ , is called a cotangent vector to $M$ at $x$ . The set of all cotangent vectors to $M$ at $x$ forms an $n$ -dimensional vector space, dual to the tangent space $T _ { x } M$ . We will denote this vector space of cotangent vectors by $T _ { x } ^ { * } M$ and call it the cotangent space to $M$ at $x$ . The union of the cotangent space to the manifold at all of its points is called cotangent bundle, denoted as $T ^ { * } M$ . Let $( q _ { 1 } , \cdots , q _ { n } )$ be the local coordinates of $M$ and $( p _ { 1 } , \cdots , p _ { n } )$ be the coordinates of the fiber. Then $( q , p )$ becomes a local coordinate of $T ^ { * } M$ , and $T ^ { * } M$ is equipped with a structure of differential manifold. Locally, $\omega = \sum _ { i = 1 } ^ { n } \mathrm { d } p _ { i } \wedge \mathrm { d } q _ { i }$ is a natural symplectic structure of $T ^ { * } M ^ { [ \mathrm { A M } 7 8 , \mathrm { A r n } 8 9 ] }$ . In order to give a coordinate-free definition of the form $\omega$ , we first define a distinguished 1-form on $T ^ { * } M$ . Let $\pi : T ^ { * } M \to M$ be a natural projection. Let $\xi \in T _ { p } ( T ^ { * } M )$ be a vector tangent to the cotangent bundle at the point $p \in T _ { x } ^ { * } M$ . The derivative taken tangent mapping $\pi _ { * } : T _ { p } ( T ^ { * } M ) \to T _ { \pi ( p ) } M$ of the natural projection $\pi : T ^ { * } M \to M$ takes $\xi$ to a vector $\pi _ { * } ( \xi )$ tangent to $M$ at $x = \pi ( p )$ . We define the 1-form $\sigma$ on $T ^ { * } M$ by the relation $\sigma = p ( \pi _ { * } ( \xi ) )$ , which has a form under the local coordinate as follows

$$
\xi = \sum _ { i = 1 } ^ { n } a _ { i } { \frac { \partial } { \partial p _ { i } } } + b _ { i } { \frac { \partial } { \partial q _ { i } } } , \quad \pi _ { * } ( \xi ) = \sum _ { i = 1 } ^ { n } b _ { i } { \frac { \partial } { \partial q _ { i } } } .
$$

Therefore, $p ( \pi _ { * } ( \boldsymbol { \xi } ) ) = \sum _ { i = 1 } ^ { n } p _ { i } b _ { i }$ , which results in

$$
\sigma = \sum _ { i = 1 } ^ { n } p _ { i } \mathrm { d } q _ { i } , \quad \omega = \mathrm { d } \sigma = \sum _ { i = 1 } ^ { n } \mathrm { d } p _ { i } \wedge \mathrm { d } q _ { i } .
$$

# 3.1.3 Hamiltonian Vector Fields

As we pointed out in Section 2.3 of Chapter 2, the symplectic structure of a symplectic space is similar to a Euclidean structure in some aspects. The symplectic structure on a symplectic manifold is also similar to a Riemann structure, which defines the Euclidean structure on a tangent space so that the tangent space becomes isomorphic to the cotangent space. The same is true for a symplectic structure. Let $( M , \omega )$ be a symplectic manifold; $\forall \eta \in T _ { x } M$ , there exists a linear form on $T _ { x } M$ : $T _ { x } M \ni \xi $ $\omega ( \xi , \eta )$ ; therefore, $\omega ( \cdot , \eta )$ defines an element of the cotangent space. Thus, we get a linear mapping $\Omega : T _ { x } M  T _ { x } ^ { * } M .$ , $\eta \to \omega ( \cdot , \eta )$ . The non-degeneracy of $\omega$ shows that $\Omega$ is an injective. Since $T _ { x } M$ and $T _ { x } ^ { * } M$ have the same dimensions, $\Omega$ must be an isomorphism, i.e.,

$$
\omega ( \xi , \eta ) = ( \Omega \eta ) \xi .
$$

Using the local coordinates, we can set $( M , \omega ) = ( \mathbf { R } ^ { 2 n } , \mathbf { d } p \wedge \mathbf { d } q )$ . For ξ = (q1, · · ·, $\begin{array} { l } { { q _ { n } ; p _ { 1 } , \cdots , p _ { n } ) , \ q = ( q _ { 1 } ^ { \prime } , \cdots , q _ { n } ^ { \prime } ; p _ { 1 } ^ { \prime } , \cdots , p _ { n } ^ { \prime } ) , \ ( \Omega \eta ) \xi = \omega ( \xi , \eta ) = \displaystyle \sum _ { i = 1 } ^ { n } p _ { i } q _ { i } ^ { \prime } - p _ { i } ^ { \prime } q _ { i } } } \end{array}$ , $\Omega$ has a matrix representation as $\left[ \begin{array} { l l } { O } & { - I } \\ { I } & { O } \end{array} \right]$ , i.e., $\Omega = - J , \Omega ^ { - 1 } = J .$ i=1

Although the above results are defined for the tangent and cotangent space at a specific point $x \in M$ , they can be easily extended to the entire tangent and cotangent bundle. Let $\theta$ be a 1-form on $M$ , i.e., a $C ^ { \infty }$ section on $T ^ { \ast } M . \Omega ^ { - 1 } \theta$ should be on a vector field on $M$ , i.e., a section on $T M$ . One of the most important cases is when $\theta = \mathrm { d } H$ is an exact differential form, i.e., $\theta$ is a $C ^ { \infty }$ total differential on $M$ . We denote it by $\Omega ^ { - 1 } = J$ .

We often say that $J \mathrm { d } H$ is Hamiltonian vector field $\left[ { \bf A M } 7 8 , { \bf A r n } 8 9 \right]$ with Hamiltonian function $H$ , which can be represented using the local coordinate as $( M , \omega ) =$ $( \mathbf { R } ^ { 2 n } , \mathrm { d } p \wedge \mathrm { d } q )$ .

We will use $J : \ T ^ { * } M \to T M _ { * }$ to denote the above isomorphism. Let $H$ be a function on the symplectic manifold $M ^ { 2 n }$ . Then, $\mathrm { d } H$ is a 1-form on $M$ , and at every point there exists a tangent vector associated with it. Thus, we can obtain a vector field $J \mathrm { d } H$ on $M$ . From

$$
J = \left[ \begin{array} { c c } { O } & { I } \\ { - I } & { O } \end{array} \right] , \quad \mathbf { d } H = H _ { q } \mathbf { d } q + H _ { p } \mathbf { d } p ,
$$

we obtain the Hamiltonian vector field

$$
J \mathrm { d } H = \left[ \begin{array} { c c } { O } & { I } \\ { - I } & { O } \end{array} \right] \left[ \begin{array} { c } { H _ { q } } \\ { H _ { p } } \end{array} \right] = \left[ \begin{array} { c } { H _ { p } } \\ { - H _ { q } } \end{array} \right] ,
$$

which has an expression under local basis for the tangent field

$$
H _ { p } \frac { \partial } { \partial q } - H _ { q } \frac { \partial } { \partial p } .
$$

# 3.1.4 Darboux Theorem

Symplectic geometry arises from the globalization of the symplectic algebra considered in the previous chapter. First, we prove Darboux’s theorem, according to which every symplectic manifold has local coordinates $p , q$ in which the symplectic structure can be written in the simplest way $\omega = \mathrm { d } p \wedge \mathrm { d } q$ .

Theorem 1.4 (Darboux theorem). Let $\omega$ be a closed non-degenerate 2-form on a manifold $M ^ { 2 n }$ . Then, $\mathrm { d } \omega = 0$ iff there exists a local coordinate system $( u , \varphi )$ for every $m \in M$ , such that

$$
\varphi ( m ) = 0 , \quad \varphi ( u ) = ( x _ { 1 } ( u ) , \cdots , x _ { n } ( u ) , y _ { 1 } ( u ) , \cdots , y _ { n } ( u ) ) ,
$$

and

$$
\omega | _ { u } = \sum _ { i = 1 } ^ { n } \mathbf { d } x _ { i } \wedge \mathbf { d } y _ { i } .
$$

Proof. The sufficiency can be easily derived, since $\sum _ { i = 1 } ^ { n } \mathbf { d } x _ { i } \wedge \mathbf { d } y _ { i }$ is a closed form.

Necessity. We first assume that $M \ = \ E$ is a linear space, and $m \ = \ 0 \ \in \ E$ . Let $\omega _ { 1 }$ be the constant-form $\omega ( 0 )$ , ${ \widetilde { \omega } } = \omega _ { 1 } - \omega$ , $\omega _ { t } ~ = ~ \omega + t \widetilde { \omega }$ $0 \leq t \leq 1$ ). For each $t$ , $\omega _ { t } ( 0 ) = \omega ( 0 )$ " "is nondegenerate. Hence, by the openness of the set of isomorphisms from $E$ to $E ^ { * }$ , there exists a neighborhood of 0 on which $\omega _ { t }$ ( $0 \leq$ $t \leq 1 $ ) is nondegenerate for all $0 \leq t \leq 1$ . We can assume that this neighborhood is a ball. Thus by Poincare lemma, there exists a 1-form ´ $\theta$ s.t. $\widetilde { \omega } = \mathrm { d } \theta$ . Without loss of generality, we assume $\theta ( 0 ) = 0$ . Since $\omega _ { t }$ "is nondegenerate, there exists a smooth vector field $X$ , s. t. $i _ { X } \omega _ { t } = - \theta$ . Since $X _ { t } ( 0 ) = 0$ , from the local existence theory of ODEs, there is a sufficiently small ball on which the integral curves of $X _ { t }$ are well defined for $t \in [ 0 , 1 ]$ . Let $F _ { t }$ be the flow starting at $F _ { 0 } =$ identity. By the Lie derivative formula for a time-dependent vector field, we have

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } } { \mathrm { d } t } ( F _ { t } ^ { * } \omega _ { t } ) ~ = ~ F _ { t } ^ { * } ( L _ { X _ { t } } \omega _ { t } ) + F _ { t } ^ { * } \frac { \mathrm { d } } { \mathrm { d } t } \omega _ { t } } \\ { = ~ F _ { t } ^ { * } \mathrm { d } i _ { X _ { t } } \omega _ { t } + F _ { t } ^ { * } \widetilde { \omega } = F _ { t } ^ { * } ( - \mathrm { d } \theta + \widetilde { \omega } ) = 0 . } \end{array}
$$

Therefore, $F _ { 1 } ^ { * } \omega _ { 1 } = F _ { 0 } ^ { * } \omega = \omega .$ . So $F _ { 1 }$ provides the chart transforming $\omega$ to the constant form $\omega _ { 1 }$ .

# 3.2 Hamiltonian Mechanics on $\mathbf { R } ^ { 2 n }$

Darboux theorem shows that every symplectic manifold of dimension $2 n$ is locally identified with the standard symplectic manifold $( \mathbf { R } ^ { 2 n } , \omega )$ . Thus, the results obtained in $( \mathbf { R } ^ { 2 n } , \omega )$ can be locally transferred to any finite-dimensional symplectic manifolds. Therefore, in this section, we only consider Hamiltonian systems in $\mathbf { R } ^ { 2 n }$ with the standard symplectic structure $\omega = \mathrm { d } p \wedge \mathrm { d } q$ .

# 3.2.1 Phase Space on $\mathbf { R } ^ { 2 n }$ and Canonical Systems

# 1. 1-form and 2-form in $\mathbf { R } ^ { 2 n }$

In $\mathbf { R } ^ { 2 n }$ , we denote

$$
{ \begin{array} { r l } { z ~ = ~ ( z _ { 1 } , \cdot \cdot \cdot , z _ { n } , z _ { n + 1 } , \cdot \cdot \cdot , z _ { 2 n } ) ^ { \prime } } \\ & { = ~ ( p _ { 1 } , \cdot \cdot \cdot , p _ { n } , q _ { 1 } , \cdot \cdot \cdot , q _ { n } ) ^ { \prime } } \\ & { = ~ { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } \in \mathbf { R } ^ { 2 n } , } \end{array} }
$$

where the prime indicates the matrix transpose.

Definition 2.1. A fundamental differential 1-form and 2-form in $\mathbf { R } ^ { 2 n }$ are defined by the following formulae:

$$
\begin{array} { r l r } {  { 1 \mathrm { - f o r m : } \ \theta = \displaystyle \sum _ { i = 1 } ^ { n } p _ { i } \mathrm { d } q _ { i } = \sum _ { i = 1 } ^ { n } z _ { i } \mathrm { d } z _ { n + i } ; } } \\ & { } & { 2 \mathrm { - f o r m : } \ \omega = \mathbf { d } \theta = \mathbf { d } p \wedge \mathbf { d } q = \displaystyle \sum _ { i = 1 } ^ { n } \mathbf { d } p _ { i } \wedge \mathrm { d } q _ { i } = \sum _ { i = 1 } ^ { n } \mathbf { d } z _ { i } \wedge \mathbf { d } z _ { n + i } . } \end{array}
$$

Thus, it can be seen that $\omega$ satisfies the following propoties:

$1 ^ { \circ }$ Closed: d $\omega = \operatorname { d } \operatorname { d } \theta = 0$ .   
$2 ^ { \circ }$ Non-degenerate: $\omega ( \xi , \eta ) = 0$ , $\forall \ \eta \in T _ { z } \mathbf { R } ^ { 2 n } \Rightarrow \xi = 0 ,$ z R2n.   
$3 ^ { \circ }$ Anti-symmetric: $\omega ( \xi , \eta ) = - \omega ( \eta , \xi ) , \forall \xi , \eta \in T _ { z } \mathbf { R } ^ { 2 n } , z \in \mathbf { R } ^ { 2 n } .$ .

Any differential 2-form satisfying the conditions 1, 2 and 3 is called a symplectic structure in $\mathbf { R } ^ { 2 n }$ . $\omega$ is called the standard symplectic structure in $\mathbf { R } ^ { 2 n }$ . $\theta$ is called the standard 1-form. $\mathbf { R } ^ { 2 n }$ equipped with $\omega$ is called the symplectic space, or symplectic manifold, denoted by $( \mathbf { R } ^ { 2 n } , \omega )$ , or briefly, $\mathbf { R } ^ { 2 n }$ .

$$
\begin{array} { l } { \omega ( \xi , \eta ) ~ = ~ \displaystyle \sum _ { i = 1 } ^ { n } \mathbf { d } z _ { i } \wedge \mathbf { d } z _ { n + i } ( \xi , \eta ) = \displaystyle \sum _ { i = 1 } ^ { n } ( \xi _ { i } \eta _ { n + i } - \eta _ { i } \xi _ { n + i } ) } \\ { ~ = ~ ( \xi _ { 1 } , \cdots , \xi _ { 2 n } ) \left[ \begin{array} { c c } { { { \cal O } } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { { \cal O } } } \end{array} \right] \left[ \begin{array} { c } { { \eta _ { 1 } } } \\ { { \vdots } } \\ { { \eta _ { 2 n } } } \end{array} \right] } \\ { ~ = ~ \xi ^ { \prime } J \eta , } \end{array}
$$

where $J = \left[ \begin{array} { c c } { { O } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { O } } \end{array} \right]$ , and $( \xi _ { 1 } , \cdots , \xi _ { 2 n } ) ^ { \prime }$ represents the vector $\xi \in T _ { z } \mathbf { R } ^ { 2 n }$ consisting of components $\xi _ { i }$ . The Equation (2.1) is the matrix representation of the 2-form $\omega$ on $T _ { z } \mathbf { R } ^ { 2 n }$ .

# 2. Hamiltonian vector fields on $\mathbf { R } ^ { 2 n }$

To each vector $\xi$ , tangent to the symplectic manifold $( \mathbf { R } ^ { 2 n } , \omega )$ at the point $z$ , we associate a 1-form $\omega _ { \xi } ^ { 1 }$ on $T _ { z } \mathbf { R } ^ { 2 n }$ by the formula

$$
\omega _ { \xi } ^ { 1 } ( \eta ) = \omega ^ { 2 } ( \eta , \xi ) , \quad \forall \eta \in T _ { z } \mathbf { R } ^ { 2 n } .
$$

We denote this correspondence by

$$
\Omega : \ { \cal T } _ { z } { \bf R } ^ { 2 n } \longrightarrow { \cal T } _ { z } ^ { * } { \bf R } ^ { 2 n } ,
$$

$$
\omega _ { \xi } ^ { 1 } ( \eta ) = \Omega \xi ( \eta ) = \omega ^ { 2 } ( \eta , \xi ) = ( - i _ { \xi } \omega ) \eta , \quad \forall \ \eta \in T _ { z } \mathbf { R } ^ { 2 n } ,
$$

or

$$
\begin{array} { r } { \omega _ { \xi } ^ { 1 } = \Omega \xi = - i _ { \xi } \omega . } \end{array}
$$

From the equation $\omega ( \eta , \xi ) = \eta ^ { \prime } J \xi = ( J \xi ) ^ { \prime } \eta$ , it follows that

$$
\omega _ { \xi } ^ { 1 } = \Omega \xi = J \xi
$$

or

$$
\begin{array} { l } { \displaystyle \omega _ { \xi } ^ { 1 } ~ = ~ \Omega \xi = \sum _ { i = 1 } ^ { 2 n } ( J \xi ) _ { i } { \bf d } z _ { i } } \\ { ~ = ~ \xi _ { n + 1 } { \bf d } z _ { 1 } + \dots + \xi _ { 2 n } { \bf d } z _ { n } - \xi _ { 1 } { \bf d } z _ { n + 1 } - \xi _ { n } { \bf d } z _ { 2 n } . } \end{array}
$$

Obviously, $\Omega$ is an isomorphism from the tangent space $T _ { z } \mathbf { R } ^ { 2 n }$ into the cotangent space $T _ { z } ^ { * } \mathbf { R } ^ { 2 n }$ . This naturally induces a mapping from $\mathcal { X } ( \mathbf { R } ^ { 2 n } )$ into $\Omega ^ { 1 } ( \mathbf { R } ^ { 2 n } )$ :

$$
\omega _ { X } ^ { 1 } = \Omega ( X ) ( z ) = \Omega ( X ( z ) ) = - i _ { X } \omega , \quad \forall \ X \in \mathcal { X } ( \mathbf { R } ^ { 2 n } ) .
$$

In particular, if $H \in C ^ { \infty } ( \mathbf { R } ^ { 2 n } )$ , then $\mathrm { d } H \in \Omega ^ { 1 } ( \mathbf { R } ^ { 2 n } )$ , $\Omega ^ { - 1 } \mathrm { d } H$ is a vector field on $\mathbf { R } ^ { 2 n }$ , and we denote it as $X _ { H }$ .

Definition 2.2. The vector field $X _ { H } = \Omega ^ { - 1 } \mathrm { d } H$ is called a Hamiltonian vector field, and $H$ is called the Hamiltonian function.

If we write d $H = ( H _ { z _ { 1 } } , \cdot \cdot \cdot , H _ { z _ { 2 n } } ) ^ { \prime } = H _ { z }$ , then

$$
\begin{array} { l } { X _ { H } = J ^ { - 1 } H _ { z } , } \\ { \mathrm { d } H = \Omega X _ { H } = - i _ { X } \omega . } \end{array}
$$

# 3. Canonical systems

Now, we consider a canonical equation in $\mathbf { R } ^ { 2 n }$ .

# Definition 2.3.

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J ^ { - 1 } H _ { z }
$$

or

$$
\frac { \mathrm { d } p } { \mathrm { d } t } = - H _ { q } , \quad \frac { \mathrm { d } q } { \mathrm { d } t } = H _ { p } .
$$

Since $J ^ { - 1 } H _ { z }$ is the matrix representation of a Hamiltonian vector field $\Omega ^ { - 1 } \mathrm { d } H =$ $X _ { H }$ , the Equation (2.2) can be rewritten as

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = X _ { H } ( z ) .
$$

The phase flow of the Hamiltonian vector field is denoted as $\phi _ { H } ^ { t }$ , and called the Hamiltonian phase flow.

Theorem 2.4. A Hamiltonian phase flow preserves the symplectic structure :

$$
( \phi _ { H } ^ { t } ) ^ { * } \omega = \omega .
$$

Proof. Since

$$
\begin{array} { r c l } { \displaystyle \frac { \mathrm { d } } { \mathrm { d } t } ( \phi _ { H } ^ { t } ) ^ { * } \omega } & { = } & { \displaystyle \frac { \mathrm { d } } { \mathrm { d } s } ( \phi _ { H } ^ { t + s } ) ^ { * } \big | _ { s = 0 } \omega } \\ & & { = } & { \displaystyle \frac { \mathrm { d } } { \mathrm { d } s } ( \phi _ { H } ^ { t } ) ^ { * } \cdot ( \phi _ { H } ^ { s } ) ^ { * } \big | _ { s = 0 } \omega } \\ & & { = } & { ( \phi _ { H } ^ { t } ) ^ { * } L _ { X _ { H } } \omega , } \end{array}
$$

and

$$
\begin{array} { r c l } { { { \cal L } _ { X _ { H } } \omega } } & { { = } } & { { ( i _ { X _ { H } } { \bf d } + { \bf d } i _ { X _ { H } } ) \omega = i _ { X _ { H } } { \bf d } \omega + { \bf d } i _ { X _ { H } } \omega } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 0 + ( - { \bf d } ( { \bf d } H ) ) = 0 , } } \end{array}
$$

we have

$$
\frac { \mathrm { d } } { \mathrm { d } t } ( \phi _ { H } ^ { t } ) ^ { * } \omega = 0 ,
$$

i.e.,

$$
( \phi _ { H } ^ { t } ) ^ { * } \omega = ( \phi _ { H } ^ { t } ) ^ { * } \big | _ { t = 0 } \omega = \omega .
$$

The theorem is proved.

# 4. Integral invariants $\left[ \mathbf { A r n 8 9 } \right]$

Let $g : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ be a differentiable mapping.

Definition 2.5. A differential $k$ -form $\omega ^ { k }$ is called an integral invariant of the map $g$ , if the integrals of $\omega$ on any $k$ -chain $c$ and on its image under $g$ are the same, i.e.,

$$
\int _ { g c } { \omega } ^ { k } = \int _ { c } { \omega } ^ { k } .
$$

Example 2.6. If $n = 1 , \ \omega ^ { 2 } =  { \mathbf { d } } p \wedge  { \mathbf { d } } q$ is the area element, then $\omega ^ { 2 }$ is the integral invariant of the map whose Jacobian determinant is equal to 1.

Theorem 2.7. A $k$ -form $\omega ^ { k }$ is an integral invariant of a map g if and only if

$$
g ^ { * } \omega ^ { k } = \omega ^ { k } .
$$

The proof is left for the reader to derive as a separate exercise.

Theorem 2.8. If the forms $\omega ^ { k }$ and $\omega ^ { l }$ are integral invariants of the map g, then the form $\omega ^ { k } \wedge \omega ^ { l }$ is also an integral invariant of $g$ .

This follows immediately from the Theorem 2.7.

Theorem 2.9. Let $\omega ^ { 2 }$ be a standard symplectic structure. Then, $\omega ^ { 2 } , ( \omega ^ { 2 } ) ^ { 2 } = \omega ^ { 2 } \wedge$ $\omega ^ { 2 }$ , $( \omega ^ { 2 } ) ^ { 3 } = \omega ^ { 2 } \wedge \omega ^ { 2 } \wedge \omega ^ { 2 } , \cdot \cdot \cdot$ are all the integral invariants of a Hamiltonian phase flow.

We define a volume element on $\mathbf { R } ^ { 2 n }$ using $( \omega ^ { 2 } ) ^ { n }$ . Then, a Hamiltonian phase flow preserves volume, and we obtain Liouville’s theorem from the Theorem 2.4. Since the form $( \omega ^ { 2 } ) ^ { k }$ is proportional to

$$
\omega ^ { 2 k } = \sum _ { i _ { 1 } < \cdots < i _ { k } } \mathrm { d } p _ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } p _ { i _ { k } } \wedge \mathrm { d } q _ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } q _ { i _ { k } } ,
$$

the integral of $\omega ^ { 2 k }$ is equal to the sum of the oriented volume of projections onto the coordinate planes $( p _ { i _ { 1 } } , \cdot \cdot \cdot , p _ { i _ { k } } , q _ { i _ { 1 } } , \cdot \cdot \cdot , q _ { i _ { k } } ) .$ Therefore, a Hamiltonian phase flow k kpreserves the sum of the oriented area as projections onto the coordinate planes $\left( p _ { i _ { 1 } } , \cdot \cdot \cdot , p _ { i _ { k } } , q _ { i _ { 1 } } , \cdot \cdot \cdot , q _ { i _ { k } } \right)$ $( 1 \leq k \leq n )$ ).

# 3.2.2 Canonical Transformation

Definition 2.10. [Arn89] A diffeomorphism $g : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ , $\widehat z = g ( z )$ is called a canonical transformation on $\mathbf { R } ^ { 2 n }$ , if for every $z \in \mathbf { R } ^ { 2 n }$ , $M = \frac { \partial \widehat { z } } { \partial z } \in S p ( 2 n )$ .

It is easy to see that a linear canonical transformation is a symplectic transformation.

Theorem 2.11. A diffeomorphism $g$ is canonical if and only if g preserves $\omega$ , i.e., $g ^ { * } \omega = \omega$ . In other words, if we denote ${ \widehat { z } } = g ( z ) = { \left[ \begin{array} { l } { P ( z ) } \\ { Q ( z ) } \end{array} \right] }$ , i.e.,

$$
z = { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } { \xrightarrow { \ g } } { \left[ \begin{array} { l } { P ( z ) } \\ { Q ( z ) } \end{array} \right] } = { \widehat { z } } ,
$$

then $g$ is canonical iff $\operatorname { d } P \wedge \operatorname { d } Q = \operatorname { d } p \wedge \operatorname { d } q$ .

Thus, a Hamiltonian phase flow $\phi _ { H } ^ { t }$ is a one-parameter group of canonical transformations on $\mathbf { R } ^ { 2 n }$ .

Proof. For every $\boldsymbol { \xi } , \boldsymbol { \eta } \in T _ { z } \mathbf { R } ^ { 2 n }$ ,

$$
( g ^ { * } \omega ) ( \xi , \eta ) = \omega ( g _ { * } \xi , g _ { * } \eta ) = \xi ^ { \prime } M ^ { \prime } J M \eta ,
$$

where $M = g _ { * } = \frac { \partial g } { \partial z }$ ∂g is Jacobian of g.

$$
\begin{array} { r l r l } { g \mathrm { c a n o n i c a l } } & { \Longleftrightarrow M ^ { \prime } J M = J , } & & { \forall z \in \mathbf { R } ^ { 2 n } , } \\ & { \Longleftrightarrow \xi ^ { \prime } M ^ { \prime } J M \eta = \xi ^ { \prime } J \eta , } & & { \forall \xi , \eta \in T _ { z } \mathbf { R } ^ { 2 n } , \ z \in \mathbf { R } ^ { 2 n } , } \\ & { \Longleftrightarrow g ^ { * } \omega ( \xi , \eta ) = \omega ( \xi , \eta ) , } & & { \forall \xi , \eta \in T _ { z } \mathbf { R } ^ { 2 n } , } \\ & { \Longleftrightarrow g ^ { * } \omega = \omega . } \end{array}
$$

Therefore, the theorem is completed.

Definition 2.12. A diffeomorphism $g : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ is conformally canonical if its Jacobian $M ( z ) = \frac { \partial g ( z ) } { \partial z } \in C S p ( 2 n )$ , $\forall z \in \mathbf { R } ^ { 2 n }$ .

Besides the parameters above, a canonical transformation $g ( z )$ can be determined by whether or not it transforms every canonical equation into a canonical equation. We first consider a conformally canonical transformation.

Let $\widehat { z } \ = \ g ( z , t )$ be a time-dependent transformation and $M ( z , t ) ~ = ~ \frac { \partial \widehat { z } } { \partial z } ~ =$ $\frac { \partial g ( z , t ) } { \partial z }$ , the Jacobian of g(z, t) with respect to z.

Theorem 2.13. The time-dependent transformation $z = g ^ { - 1 } ( \widehat { z } , t ) : \mathbf { R } ^ { 2 n } \to \mathbf { R } ^ { 2 n }$ transforms every canonical equation

$$
\frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = J ^ { - 1 } \widehat { H } _ { \widehat { z } } ( \widehat { z } ) ,
$$

with the Hamiltonian $\widehat { H } ( \widehat { z } )$ into a canonical equation

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J ^ { - 1 } H _ { z } ( z ) ,
$$

with some Hamiltonian $H ( z )$ , iff $M ( z , t ) = \frac { \partial \hat { z } } { \partial z }$ satisfies

$$
M ^ { \prime } J M = \mu J ,
$$

where $\mu \neq 0$ , independent of $z$ and $t$ .

Proof.

$$
\frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = \frac { \partial \widehat { z } } { \partial z } \frac { \mathrm { d } z } { \mathrm { d } t } + \frac { \partial g } { \partial t } = M \frac { \mathrm { d } z } { \mathrm { d } t } + \frac { \partial g } { \partial t } .
$$

Set $\overline { { H } } ( z ) = \widehat { H } ( g ( z , t ) , t ) = \widehat { H } \circ g$ ; then $\overline { { H } } _ { z } = { \left( \frac { \partial \widehat { z } } { \partial z } \right) } ^ { \prime } \widehat { H } _ { \widehat { z } }$ . Thus, from the equation

$$
\frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = J ^ { - 1 } \widehat { H } _ { \widehat { z } } ,
$$

we have

$$
M \frac { \mathrm { d } z } { \mathrm { d } t } + \frac { \partial g } { \partial t } = J ^ { - 1 } M ^ { - 1 ^ { \prime } } \overline { { { H } } } _ { z } ,
$$

i.e.,

$$
\begin{array} { l } { { \displaystyle { \frac { \mathrm { d } z } { \mathrm { d } t } \ = \ M ^ { - 1 } \left( J ^ { - 1 } M ^ { - 1 ^ { \prime } } \overline { { { H } } } _ { z } - \frac { \partial g } { \partial t } \right) } } } \\ { { \displaystyle \ } } \\ { { \displaystyle \ = \ J ^ { - 1 } \left( J M ^ { - 1 } J ^ { - 1 } M ^ { - 1 ^ { \prime } } \overline { { { H } } } _ { z } - J M ^ { - 1 } \frac { \partial g } { \partial t } \right) } } \\ { { \displaystyle \ = \ J ^ { - 1 } ( u + v ) , } } \end{array}
$$

where u = BHz, B = JM−1J−1M −1 , $B = J M ^ { - 1 } J ^ { - 1 } M ^ { - 1 ^ { \prime } } , v = C { \frac { \partial g } { \partial t } }$ , $C = - J M ^ { - 1 }$ , and $u$ depends on the Hamiltonian $\widehat { H }$ as well as on $\widehat { z }$ , and $v$ depends only on $\widehat { z }$ .

For every ${ \widehat { H } } \in C ^ { \infty } ( \mathbf { R } ^ { 2 n } )$ , there exists another function $H ( z )$ , such that

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { J } ^ { - 1 } \boldsymbol { H } _ { \boldsymbol { z } } ,
$$

iff there exists a function $H ( z ) \in C ^ { \infty } ( \mathbf { R } ^ { 2 n } )$ , such that

$$
u + v = \frac { \partial H } { \partial z } ,
$$

i.e., $u + v$ is a gradient transformation. We know that a Jacobian matrix which equals to $u + v$ and $\frac { \partial \left( u + v \right) } { \partial z }$ is symmetric, i.e.,

$$
\frac { \partial u _ { i } } { \partial z _ { k } } + \frac { \partial v _ { i } } { \partial z _ { k } } = \frac { \partial u _ { k } } { \partial z _ { i } } + \frac { \partial v _ { k } } { \partial z _ { i } } , \quad \forall \widehat { H } ( z ) , \quad i , k = 1 , \cdots , 2 n .
$$

In the above equation , taking $\widehat { H }$ as a constant, we get

$$
\frac { \partial v _ { i } } { \partial z _ { k } } = \frac { \partial v _ { k } } { \partial z _ { i } } , \quad i , k = 1 , \cdot \cdot \cdot , 2 n .
$$

Consequently,

$$
\frac { \partial u _ { i } } { \partial z _ { k } } = \frac { \partial u _ { k } } { \partial z _ { i } } , \quad \forall \widehat { H } ( \widehat { z } ) , \quad i , k = 1 , \cdots , 2 n .
$$

Notice that $u _ { i } = ( B \overline { { H } } _ { z } ) _ { i } = \sum _ { j = 1 } ^ { 2 n } B _ { i j } \overline { { H } } _ { z _ { j } }$ , (2.6) becomes

$$
\frac { \partial } { \partial z _ { k } } \Big ( \sum _ { j = 1 } ^ { 2 n } B _ { i j } \frac { \partial \overline { { H } } } { \partial z _ { j } } \Big ) = \frac { \partial } { \partial z _ { i } } \Big ( \sum _ { j = 1 } ^ { 2 n } B _ { k j } \frac { \partial \overline { { H } } } { \partial z _ { j } } \Big ) .
$$

Expanding it, we get

$$
\sum _ { j = 1 } ^ { 2 n } \frac { \partial B _ { i j } } { \partial z _ { k } } \frac { \partial \overline { { { H } } } } { \partial z _ { j } } + \sum _ { j = 1 } ^ { 2 n } B _ { i j } \frac { \partial ^ { 2 } \overline { { { H } } } } { \partial z _ { k } \partial z _ { j } } = \sum _ { j = 1 } ^ { 2 n } \frac { \partial B _ { k j } } { \partial z _ { i } } \frac { \partial \overline { { { H } } } } { \partial z _ { j } } + \sum _ { j = 1 } ^ { 2 n } B _ { k j } \frac { \partial ^ { 2 } \overline { { { H } } } } { \partial z _ { i } \partial z _ { j } } .
$$

Take $\widehat { H } ( \widehat { z } ) = z _ { l } \circ g ^ { - 1 } ( l = 1 , \cdots , 2 n )$ , then $\widehat { H } ( z ) = z _ { l } \left( l = 1 , \cdots , 2 n \right)$ . By this, Equation (2.8) gets split into classes of equations:

$$
\begin{array} { c c } { { \displaystyle \frac { \partial B _ { i j } } { \partial z _ { k } } = \frac { \partial B _ { k j } } { \partial z _ { i } } , } } & { { i , k , j = 1 , \cdots , 2 n , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { 2 n } B _ { i j } \frac { \partial ^ { 2 } H } { \partial z _ { k } \partial z _ { j } } = \sum _ { j = 1 } ^ { 2 n } B _ { k j } \frac { \partial ^ { 2 } \overline { { H } } } { \partial z _ { i } \partial z _ { j } } , } } & { { i , k = 1 , \cdots , 2 n . } } \end{array}
$$

Set $A = \frac { \partial ^ { 2 } \overline { { H } } } { \partial z _ { k } \partial z _ { j } } ,$ . Obviously, $A$ is symmetric, i.e., $A ^ { \prime } = A$ . Then, (2.10) indicates

$$
B A = ( B A ) ^ { \prime } = A ^ { \prime } B ^ { \prime } = A B ^ { \prime } , \quad \forall A ^ { \prime } = A .
$$

This implies

$$
B = \mu ( \boldsymbol { z } , t ) I ,
$$

where $\mu \neq 0$ . Since $| B | \ne 0$ , or

$$
\begin{array} { r } { B _ { i j } = \mu ( z , t ) \delta _ { i j } . } \end{array}
$$

Substituting it into (2.9), we get

$$
\frac { \partial \mu } { \partial z _ { k } } \delta _ { i j } = \frac { \partial \mu } { \partial z _ { i } } \delta _ { k j } , \quad i , j , k = 1 , \cdots , 2 n .
$$

From this, it follows that

$$
\frac { \partial \mu } { \partial z _ { i } } = 0 , \quad i = 1 , \cdots , 2 n ,
$$

i.e., $\mu \ = \ \mu ( t )$ is independent of $z$ . Thus, $J M ^ { - 1 } J ^ { - 1 } M ^ { - 1 ^ { \prime } } = B = \mu ( t ) I $ , i.e., $M ^ { \prime } J M = \mu ^ { - 1 } ( t ) J ,$ $M$ is conformally symplectic with $\mu ^ { - 1 } ( t )$ .

We now prove that $\mu$ is independent of $t$ . Since

$$
\begin{array} { l l } { { J M ^ { - 1 } J ^ { - 1 } M ^ { - 1 ^ { \prime } } = \mu ( t ) I , } } & { { C = - J M ^ { - 1 } = - \mu ( t ) M ^ { \prime } J , } } \\ { { \displaystyle C _ { i j } = - \mu ( t ) \frac { \partial \hat { z } _ { l } } { \partial z _ { i } } J _ { l j } , } } & { { v = C \frac { \partial g } { \partial t } , } } \end{array}
$$

we have

$$
\begin{array} { r c l } { { v _ { i } ~ = ~ C _ { i j } \displaystyle \frac { \partial g _ { j } } { \partial t } = - \mu ( t ) \displaystyle \frac { \partial \widehat { z } _ { l } } { \partial z _ { i } } J _ { l j } \displaystyle \frac { \partial g _ { j } } { \partial t } , } } \\ { { \displaystyle \frac { \partial v _ { i } } { \partial z _ { k } } ~ = ~ \displaystyle \frac { \partial } { \partial z _ { k } } \Big ( - \mu ( t ) \displaystyle \frac { \partial \widehat { z } _ { l } } { \partial z _ { i } } J _ { l j } \displaystyle \frac { \partial g _ { j } } { \partial t } \Big ) } } \\ { { ~ } } & { { ~ = ~ - \mu ( t ) \Big ( \displaystyle \frac { \partial ^ { 2 } \widehat { z } _ { l } } { \partial z _ { k } \partial z _ { i } } J _ { l j } \displaystyle \frac { \partial g _ { j } } { \partial t } + \displaystyle \frac { \partial \widehat { z } _ { l } } { \partial z _ { i } } J _ { l j } \displaystyle \frac { \partial ^ { 2 } g _ { j } } { \partial z _ { k } \partial t } \Big ) . } } \end{array}
$$

Then, the system (2.5)

$$
\frac { \partial v _ { i } } { \partial z _ { k } } = \frac { \partial v _ { k } } { \partial z _ { i } } , \quad i , k = 1 , \cdot \cdot \cdot , 2 n
$$

is equivalent to

$$
\begin{array} { l } { \displaystyle - \mu ( t ) \Big ( \frac { \partial ^ { 2 } \widehat { z } _ { l } } { \partial z _ { k } \partial z _ { i } } J _ { l j } \frac { \partial g _ { j } } { \partial t } + \frac { \partial \widehat { z } _ { l } } { \partial z _ { i } } J _ { l j } \frac { \partial ^ { 2 } g _ { j } } { \partial z _ { k } \partial t } \Big ) } \\ { \displaystyle = \mu ( t ) \Big ( \frac { \partial ^ { 2 } \widehat { z } _ { l } } { \partial z _ { i } \partial z _ { k } } J _ { l j } \frac { \partial g _ { j } } { \partial t } + \frac { \partial \widehat { z } _ { l } } { \partial z _ { k } } J _ { l j } \frac { \partial ^ { 2 } g _ { j } } { \partial z _ { i } \partial t } \Big ) , } \end{array}
$$

i.e.,

$$
\frac { \partial \widehat { z _ { l } } } { \partial z _ { i } } J _ { l j } \left( \frac { \partial \widehat { z } _ { j } } { \partial z _ { k } } \right) _ { t } = \frac { \partial \widehat { z _ { l } } } { \partial z _ { k } } J _ { l j } \left( \frac { \partial \widehat { z _ { j } } } { \partial z _ { i } } \right) _ { t } ,
$$

i.e.,

$$
( M ^ { \prime } J M _ { t } ) _ { i k } = ( M ^ { \prime } J M _ { t } ) _ { k i } ,
$$

which shows show that $M ^ { \prime } J M _ { t }$ is a symmetric matrix. Therefore,

$$
M ^ { \prime } J M _ { t } = ( M ^ { \prime } J M _ { t } ) ^ { \prime } = M _ { t } ^ { \prime } J ^ { \prime } M = - M _ { t } ^ { \prime } J M .
$$

Then, we have

$$
( M ^ { \prime } J M ) _ { t } = M _ { t } ^ { \prime } J M + M ^ { \prime } J M _ { t } = M _ { t } ^ { \prime } J M - M _ { t } ^ { \prime } J M = 0 .
$$

However, $M ^ { \prime } J M = \mu ( t ) J$ , and so it follows that $\mu ( t ) = \mu =$ constant. Consequently, $M ^ { \prime } J M = \mu J ;$ , $\mu$ independent of $z$ and $t$ .

In particular, if $g$ is independent of $t$ , then $v = 0$ and $u = \mu \overline { { H } } _ { z } ( z )$ . Thus, we obtain the following Theorem 2.14.

Theorem 2.14. A transformation $g ( z ) = \widehat { z } : \mathbf { R } ^ { 2 n } \to \mathbf { R } ^ { 2 n }$ is conformally canonical with $\mu$ independent of $z$ iff $z = g ^ { - 1 } ( \widehat { z } )$ transforms every canonical system

$$
\frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = J ^ { - 1 } \widehat { H } _ { \widehat { z } }
$$

with the Hamiltonian $\widehat { H } ( \widehat { z } )$ into a canonical system

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J ^ { - 1 } H _ { z } ( z ) ,
$$

with the Hamiltonian $H ( z ) = \mu { \widehat { H } } ( g ( z ) ) = \mu { \widehat { H } } \circ g .$

For a further transform, we obtain Theorem 2.15.

Theorem 2.15. A transformation $\widehat { z } = g ( z ) : \mathbf { R } ^ { 2 n } \to \mathbf { R } ^ { 2 n }$ is canonical iff $g ^ { - 1 }$ transforms a canonical system

$$
\frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = J ^ { - 1 } \widehat { H } _ { \widehat { z } }
$$

with the Hamiltonian $\widehat { H } ( \widehat { z } )$ into a canonical system

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { J } ^ { - 1 } \boldsymbol { H } _ { \boldsymbol { z } } ,
$$

with Hamiltonian $H ( z ) = \widehat { H } ( g ( z ) ) = \widehat { H } \circ g$

# 3.2.3 Poisson Bracket

# 1. Poisson bracket

Definition 2.16. The Poisson bracket $\{ \phi ( z ) , \psi ( z ) \}$ of smooth functions $\phi ( z )$ and $\psi ( z )$ on $\mathbf { R } ^ { 2 n }$ is also a smooth function on $\mathbf { R } ^ { 2 n }$ , defined by the formula

$$
\begin{array} { r c l } { { \{ \phi , \psi \} ( z ) } } & { { = } } & { { \phi _ { z } ^ { \prime } J ^ { - 1 } \psi _ { z } = [ \phi _ { p } ^ { \prime } , \phi _ { q } ^ { \prime } ] \left[ \begin{array} { c c } { { { \cal O } } } & { { - I } } \\ { { I } } & { { { \cal O } } } \end{array} \right] \left[ \begin{array} { c } { { \psi _ { p } } } \\ { { \psi _ { q } } } \end{array} \right] } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { - ( \phi _ { p } ^ { \prime } \psi _ { q } - \phi _ { q } ^ { \prime } \psi _ { p } ) . } } \end{array}
$$

Property 2.17. Let $\phi , \psi , \chi$ be smooth functions on $\mathbf { R } ^ { 2 n }$ , then the Poisson bracket has following basic properties:

$1 ^ { \circ }$ anti-symmetric: $\{ \phi , \psi \} = - \{ \psi , \phi \}$ . $2 ^ { \circ }$ bilinear: $\{ \alpha \phi + \beta \psi , \chi \} = \alpha \{ \phi , \chi \} + \beta \{ \psi , \chi \} , \alpha , \beta \in { \bf R } .$ $3 ^ { \circ }$ Jacobi identity: $\{ \{ \phi , \psi \} , \chi \} + \{ \{ \psi , \chi \} , \phi \} + \{ \{ \chi , \phi \} , \psi \} = 0 .$

$1 ^ { \circ }$ and $2 ^ { \circ }$ are self-evident. The Jacobi identity can be proved by direct computation, but it also follows from the following proposition and the corresponding Jacobi identity of the vector field.

Proposition 2.18. Let $\phi$ and $\psi$ be smooth functions on $\mathbf { R } ^ { 2 n }$ . Then,

$1 ^ { \circ }$ $\{ \phi , \psi \} = - \omega ( X _ { \phi } , X _ { \psi } ) ,$ . $2 ^ { \circ }$ $\{ \phi , \psi \} = \mathrm { d } \phi ( X _ { \psi } ) = i _ { X _ { \phi } } \omega ( X _ { \psi } ) .$ . $3 ^ { \circ }$ $\{ \phi , \psi \} = i _ { X _ { \phi } } i _ { X _ { \psi } } \omega$ . $4 ^ { \circ }$ $\{ \phi , \psi \} ( z ) = { \frac { \operatorname * { d } } { \operatorname * { d t } } } { \Big | } _ { t = 0 } \phi ( \phi _ { \psi } ^ { t } z ) = L _ { X _ { \psi } } \phi ( z ) .$ $5 ^ { \circ }$ $\Omega ^ { - 1 } \mathrm { d } \left\{ \phi , \psi \right\} = - [ \Omega ^ { - 1 } \mathrm { d } \phi , \Omega ^ { - 1 } \mathrm { d } \psi ] = - [ X _ { \phi } , X _ { \psi } ] \Leftrightarrow X _ { \left\{ \phi , \psi \right\} } = - [ X _ { \phi } , X _ { \psi } ]$ , where $X _ { \phi } = \Omega ^ { - 1 } \mathrm { d } \phi$ is the Hamiltonian vector field of a Hamiltonian function $\phi$ .

Each of the equalities $1 ^ { \circ }$ , $2 ^ { \circ }$ , $3 ^ { \circ }$ and $4 ^ { \circ }$ can be a definition of the Poisson bracket of functions.

Proof. By definition,

$$
\begin{array} { l } { { \{ \phi , \psi \} ( z ) ~ = ~ \phi _ { z } ^ { \prime } J ^ { - 1 } \psi _ { z } = \phi _ { z } ^ { \prime } J ^ { - 1 } J J ^ { - 1 } \psi _ { z } } } \\ { { ~ = ~ - ( J ^ { - 1 } \phi _ { z } ) ^ { \prime } J ( J ^ { - 1 } \psi _ { z } ) = - \omega ( X _ { \phi } , X _ { \psi } ) } } \\ { { ~ = ~ - i _ { X _ { \phi } } \omega ( X _ { \psi } ) = \mathrm { d } \phi ( X _ { \psi } ) , } } \end{array}
$$

where $X _ { \phi } = \Omega ^ { - 1 } { \bf d } \phi = \sum _ { i = 1 } ^ { 2 n } ( J ^ { - 1 } \phi _ { z } ) _ { i } { \bf d } z _ { i } .$ . The Equations (2.13) and (2.14) are just $1 ^ { \circ }$ and $2 ^ { \circ }$ of Proposition 2.18 respectively. However,

$$
- \omega ( X _ { \phi } , X _ { \psi } ) = \omega ( X _ { \psi } , X _ { \phi } ) = i _ { X _ { \psi } } \omega ( X _ { \phi } ) = i _ { X _ { \phi } } i _ { X _ { \psi } } \omega ,
$$

and so $\{ \phi , \psi \} = i _ { X _ { \phi } } i _ { X _ { \psi } } \omega$ , which is $3 ^ { \circ }$ . For $4 ^ { \circ }$ , by Equation (2.14),

$$
\{ \phi , \psi \} = \mathbf { d } \phi ( X _ { \psi } ) = i _ { X _ { \psi } } \mathbf { d } \phi = L _ { X _ { \psi } } \phi ,
$$

since for $\phi \in C ^ { \infty } ( \mathbf { R } ^ { 2 n } ) , L _ { X } \phi = i _ { X } \mathbf { d } \phi$ . Finally, for $5 ^ { \circ }$ , we have

$$
\begin{array} { l } { { [ X _ { \phi } , X _ { \psi } ] ~ = ~ ( J ^ { - 1 } \psi _ { z } ) _ { z } J ^ { - 1 } \phi _ { z } - ( J ^ { - 1 } \phi _ { z } ) _ { z } J ^ { - 1 } \psi _ { z } } } \\ { { ~ } } \\ { { ~ = ~ J ^ { - 1 } \psi _ { z z } J ^ { - 1 } \phi _ { z } - J ^ { - 1 } \phi _ { z z } J ^ { - 1 } \psi _ { z } , } } \end{array}
$$

and

$$
\begin{array} { r c l } { { \{ \phi , \psi \} _ { z } } } & { { = } } & { { ( \phi ^ { \prime } { } _ { z } J ^ { - 1 } \psi _ { z } ) _ { z } = \phi _ { z z } J ^ { - 1 } \psi _ { z } - \psi _ { z z } J ^ { - 1 } \phi _ { z } , } } \\ { { } } & { { } } & { { } } \\ { { \Omega ^ { - 1 } \mathrm { d } \left\{ \phi , \psi \right\} } } & { { = } } & { { J ^ { - 1 } \{ \phi , \psi \} _ { z } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { J ^ { - 1 } \phi _ { z z } J ^ { - 1 } \psi _ { z } - J ^ { - 1 } \psi _ { z z } J ^ { - 1 } \phi _ { z } = - [ X _ { \phi } , X _ { \psi } ] . } } \end{array}
$$

Therefore, the proposition is completed.

Exercise 2.19. Show that the map $g : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ , sending $( p , q ) \to ( P ( p , q ) , Q ( p , q ) )$ is canonical, iff the Poisson bracket of any two functions in variables $( p , q )$ and $( P , Q )$ coincide:

$$
\left\{ \phi \circ g ^ { - 1 } , \psi \circ g ^ { - 1 } \right\} = \left\{ \phi , \psi \right\} \circ g ^ { - 1 } , \quad \forall \phi , \psi \in C ^ { \infty } ( \mathbf { R } ^ { 2 n } ) .
$$

i.e.,

$$
\begin{array} { l } { { \{ \phi , \psi \} _ { p , q } ~ = ~ \frac { \partial \psi } { \partial p } \frac { \partial \phi } { \partial q } - \frac { \partial \psi } { \partial q } \frac { \partial \phi } { \partial p } } } \\ { { { } ~ = ~ \frac { \partial \psi } { \partial P } \frac { \partial \phi } { \partial Q } - \frac { \partial \psi } { \partial Q } \frac { \partial \phi } { \partial P } } } \\ { { { } ~ = ~ \{ \phi , \psi \} _ { P , Q } . } } \end{array}
$$

Theorem 2.20. A function $F$ is a first integral of the phase flow with the Hamiltonian $H$ iff its Poisson bracket with $H$ is identically zero:

$$
\left\{ F , H \right\} = 0 .
$$

Proof. By the $4 ^ { \circ }$ of proposition above,

$$
L _ { X _ { H } } F = \frac { \mathrm { d } } { \mathrm { d } t } \bigg \vert _ { t = 0 } ( \phi _ { H } ^ { t } ) ^ { * } F = \{ F , H \} = 0 .
$$

Thus,

$$
\begin{array} { l } { { \displaystyle { \frac { \mathrm { d } } { \mathrm { d } t } } F ( \phi _ { H } ^ { t } ( z ) ) ~ = ~ { \frac { \mathrm { d } } { \mathrm { d } t } } ( \phi _ { H } ^ { t } ) ^ { * } F ( z ) = { \frac { \mathrm { d } } { \mathrm { d } s } } \Big \vert _ { s = 0 } ( \phi _ { H } ^ { t + s } ) ^ { * } F ( z ) } } \\ { { \displaystyle ~ = ~ { \frac { \mathrm { d } } { \mathrm { d } s } } ( \phi _ { H } ^ { t ^ { * } } \phi _ { H } ^ { s ^ { * } } ) \Big \vert _ { s = 0 } F ( z ) } } \\ { { \displaystyle ~ = ~ \phi _ { H } ^ { t ^ { * } } { \frac { \mathrm { d } } { \mathrm { d } s } } ( \phi _ { H } ^ { s } ) ^ { * } \Big \vert _ { s = 0 } F ( z ) = \phi _ { H } ^ { t ^ { * } } L _ { X _ { H } } F ( z ) = 0 , } } \end{array}
$$

i.e., $F$ is a first integral of the phase flow with the Hamiltonian $H$ . The necessary condition is evident.

From the Theorem 2.20, we immediately obtain the following.

Theorem 2.21. H is a first integral of the phase flow with Hamiltonian function $H$

Theorem 2.22 (E. Noether theorem). If a Hamiltonian $H$ is a first integral of the phase flow with a Hamiltonian function $H$ , then $F$ is also a first integral of the phase flow with the Hamiltonian function $H$ .

This follows immediately from the Theorem 2.21 and the fact that $\left\{ F , H \right\} =$ $- \{ H , F \}$ .

Theorem 2.23 (Poisson theorem). The Poisson bracket of the two first integrals $F _ { 1 } , F _ { 2 }$ of a system with a Hamiltonian function $H$ is again a first integral.

Proof. By the Jacobi identity,

$$
\begin{array} { r c l } { { \left\{ \left\{ F _ { 1 } , F _ { 2 } \right\} , H \right\} } } & { { = } } & { { \left\{ F _ { 1 } , \left\{ F _ { 2 } , H \right\} \right\} + \left\{ F _ { 2 } , \left\{ H , F _ { 1 } \right\} \right\} } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 0 + 0 = 0 , } } \end{array}
$$

which is what we require.

# 2. Lie algebras of Hamiltonian vector fields and functions

Definition 2.24. A Lie algebra is a vector space $L$ , together with a bilinear skewsymmetric operation $[ , ] : L \times L \to L$ , which satisfies the Jacobi identity.

The operation $[ , ]$ is usually called the commutator.

Therefore, the set of all vector fields on ${ \mathbf { R } } ^ { 2 n } , \mathcal { X } ( { \mathbf { R } } ^ { 2 n } )$ , together with the Poisson bracket $[ , ]$ , forms a Lie algebra; the set of all smooth functions on ${ \bf R } ^ { 2 n } , C ^ { \infty } ( { \bf R } ^ { 2 n } )$ , together with the Poisson bracket $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ , forms a Lie algebra too.

Definition 2.25. A linear subspace of a Lie algebra is called a subalgebra if the subspace is closed under the commutator, i.e., the commutator of any two elements of the subspace belongs to it.

Evidently, a subalgebra of a Lie algebra is itself a Lie algebra with the original commutator.

By the proposition and theorems above, we have:

Corollary 2.26. The Hamiltonian vector fields on $\mathbf { R } ^ { 2 n }$ form a subalgebra of the Lie algebra of all vector fields.

Corollary 2.27. The commutator of the Hamiltonian phase flow with a Hamiltonian form a subalgebra of the Lie algebra of all functions.

# 3.2.4 Generating Functions

Let a subset $S \subset \mathbf { R } ^ { 2 n }$ be an $r$ -dimensional submanifold in $\mathbf { R } ^ { 2 n }$ . For any fixed point $s \in S$ , there exists an open set $U \subset \mathbf { R } ^ { r }$ and a diffeomorphism $\varphi : U \to S$ such that $s \in \varphi ( U )$ . For simplicity, we consider the case only locally.

Definition 2.28. A subset $S \subset \mathbf { R } ^ { 2 n }$ is an $r$ -dim submanifold if there exists a one-toone smooth map $Z : U \subset \mathbf { R } ^ { r }  \mathbf { R } ^ { 2 n }$ such that

$$
S = \{ z = Z ( x ) \in \mathbf { R } ^ { 2 n } \mid x \in U \subset \mathbf { R } ^ { r } \} .
$$

The tangent space $T _ { z } S$ to $S$ at $z = Z ( x )$ is

$$
T _ { z } S = \left[ { \frac { \partial Z } { \partial x } } \right] = { \left[ \begin{array} { l l l } { { \frac { \partial Z _ { 1 } } { \partial x _ { 1 } } } } & { \cdots } & { { \frac { \partial Z _ { 1 } } { \partial x _ { r } } } } \\ & & { \vdots } \\ { { \frac { \partial Z _ { 2 n } } { \partial x _ { 1 } } } } & { \cdots } & { { \frac { \partial Z _ { 2 n } } { \partial x _ { r } } } } \end{array} \right] } = { \left[ \begin{array} { l } { { \frac { \partial P } { \partial x } } } \\ { { \frac { \partial Q } { \partial x } } } \end{array} \right] } \subset T _ { z } \mathbf { R } ^ { 2 n } ,
$$

$Z ( x ) = { \bigl [ } { \begin{array} { l } { P ( x ) } \\ { Q ( x ) } \end{array} } { \bigr ] } .$

Let $f : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ be a smooth function. The graph of $f$ in the product space $\mathbf { R } ^ { n } \times \mathbf { R } ^ { n } = \mathbf { R } ^ { 2 n }$ ,

$$
\operatorname { g r } \left( f \right) : = G _ { f } = \left\{ { \left[ \begin{array} { l } { f ( q ) } \\ { q } \end{array} \right] } \in \mathbf { R } ^ { 2 n } \mid q \in \mathbf { R } ^ { n } \right\}
$$

is an $n$ -dim submanifold in $\mathbf { R } ^ { 2 n }$ , and its tangent space $T _ { z } G _ { f } = \left\{ \begin{array} { c } { { \frac { \partial f } { \partial q } } } \\ { { I } } \end{array} \right\}$ is transversal to $\mathbf { R } _ { p } ^ { n } = \left[ \begin{array} { l } { I } \\ { O } \end{array} \right]$ in $T _ { z } \mathbf { R } ^ { 2 n }$ for any $z \in G _ { f }$ .

Theorem 2.29. Let $S$ be an $n$ -dim submanifold in $\mathbf { R } ^ { 2 n }$ . $S$ is a graph of some function $f$ iff for any $z \in S$ , its tangent space $T _ { z } S$ to $S$ at $z$ is transversal to $\mathbf { R } _ { p } ^ { n }$ in $T _ { z } { \mathbf { R } } ^ { 2 n }$ .

Proof. We need to only prove the sufficiency. By definition, there are two functions $P ( x )$ and $Q ( x )$ , such that

$$
S = \left\{ { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } = { \left[ \begin{array} { l } { P ( x ) } \\ { Q ( x ) } \end{array} \right] } \mid x \in U \subset \mathbf { R } ^ { n } \right\} .
$$

Since $T _ { z } S = \left[ \begin{array} { l } { \frac { \partial P } { \partial x } } \\ { \frac { \partial Q } { \partial x } } \end{array} \right]$ is transversal to $\mathbf { R } _ { p } ^ { n } = \left[ \begin{array} { l } { I } \\ { O } \end{array} \right]$ in $T _ { z } \mathbf { R } ^ { 2 n }$ , we have $\left| \frac { \partial Q } { \partial x } \right| \neq 0$ . By the inverse function theorem, $q = Q ( x )$ has an inverse function $x = X ( q )$ with the Jacobian ${ \frac { \partial X } { \partial q } } = \left[ { \frac { \partial Q } { \partial X } } \right] ^ { - 1 }$ . This implies that

$$
T _ { z } S = \left[ \begin{array} { c c c c c c } { \frac { \partial P } { \partial x } } \\ { \frac { \partial Q } { \partial x } } \end{array} \right] = \left[ \begin{array} { c c c c c c } { \frac { \partial P } { \partial x } \left( \frac { \partial Q } { \partial q } \right) ^ { - 1 } } \\ { I } \end{array} \right] = \left[ \begin{array} { c c c c c c } { \frac { \partial P } { \partial x } \frac { \partial X } { \partial q } } \\ { I } \end{array} \right] = \left[ \begin{array} { c c c c c c } { \frac { \partial } { \partial q } ( P \circ X ) } \\ { I } \end{array} \right] .
$$

Setting $f = P \circ X$ , we get

$$
S = \left\{ { \left[ \begin{array} { l } { P ( x ) } \\ { Q ( x ) } \end{array} \right] } \in \mathbf { R } ^ { 2 n } \right\} = \left\{ { \begin{array} { l } { P \circ X ( q ) } \\ { q } \end{array} } \right\} = \left\{ { \begin{array} { l } { f ( q ) } \\ { q } \end{array} } \right\} , \quad T _ { z } S = \left[ { \begin{array} { l } { { \frac { \partial f } { \partial q } } } \\ { { I } } \end{array} } \right] ,
$$

$S$ is the graph of the function $f ( q ) = P \circ X ( q )$ .

$\operatorname { e t } W : \mathbf { R } ^ { 2 n } \to \mathbf { R } ^ { 2 n } , { \widehat { z } } = W ( z ) = { \left[ \begin{array} { l } { U ( p , q ) } \\ { V ( p , q ) } \end{array} \right] } , z = { \left[ \begin{array} { l } { \ p } \\ { q } \end{array} \right] } { \mathrm { ~ b e ~ a ~ d i f f } }$

$$
{ \frac { \partial W } { \partial z } } = { \left[ \begin{array} { l l } { { \frac { \partial U } { \partial p } } } & { { \frac { \partial U } { \partial q } } } \\ { { \frac { \partial V } { \partial p } } } & { { \frac { \partial V } { \partial q } } } \end{array} \right] } = { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } .
$$

If $f ( q )$ is a function with Jacobian $M = { \frac { \partial f } { \partial q } }$ , and $S = G _ { f }$ , the graph of $f$ , then

$$
W ( S ) = \left\{ { \widehat { z } } = W ( z ) ~ | ~ z = \left[ { \begin{array} { c } { f ( q ) } \\ { q } \end{array} } \right] \in S \right\}
$$

is an $n$ -dim submanifold in $\mathbf { R } ^ { 2 n }$ with Jacobian

$$
T _ { \hat { z } } W ( S ) = \frac { \partial W } { \partial z } \left[ \begin{array} { c } { \frac { \partial f } { \partial q } } \\ { I } \end{array} \right] = \left[ \begin{array} { c c } { A } & { B } \\ { C } & { D } \end{array} \right] \left[ \begin{array} { c } { M } \\ { I } \end{array} \right] = \left[ \begin{array} { c } { A M + B } \\ { C M + D } \end{array} \right] .
$$

Therefore, the theorem is completed.

By Theorem 2.29, $W ( s )$ is a graph of some function $g$ iff $T _ { \widehat { z } } W ( s ) = { \left\{ \begin{array} { l l } { A M + B } \\ { C M + D } \end{array} \right\} }$ is transversal to $\mathbf { R } _ { p } ^ { n }$ on $W ( S )$ , i.e., $\vert C M + D \vert \ne 0$ . Thus, we obtain the following theorem.

Theorem 2.30. Let $W ( z ) : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ be a diffeomorphism with Jacobian $\frac { \partial W } { \partial z } =$ $\left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right]$ and $f ( q )$ be a function with Jacobian $M = { \frac { \partial f } { \partial q } }$ . Then, $M$ satisfies the transversality condition: $\vert C M + D \vert \neq 0 ,$ , iff there exists a function $g ( q )$ with Jacobian $N = \frac { \partial g } { \partial q } = ( A M + B ) ( C M + D ) ^ { - 1 }$ such that $W ( G _ { f } ) = G _ { g } ,$ i.e., $W$ transforms the graph of $f$ into the graph of $g$ .

Definition 2.31. Let $f : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ be a transformation and $\varphi : \mathbf { R } ^ { n }  \mathbf { R }$ be a scalar function; if $f = \operatorname { g r a d } \varphi = \varphi _ { q } ( q )$ , then $\varphi$ is called a generating function of $f$ and $f$ called a gradient transformation[AM78,Fen86,FWQW89] .

Given an $n$ -value function $f$ on $\mathbf { R } ^ { n }$ , we may construct a differential 1-form $\omega ^ { 1 } =$ $f \mathrm { d } q = f _ { 1 } \mathrm { d } q _ { 1 } + \cdot \cdot \cdot + f _ { n } \mathrm { d } q _ { n }$ . If there exists a 0-form $\varphi$ such that $\omega ^ { 1 } = f \mathrm { d } q =$ $\mathrm { d } \varphi$ , i.e., $\omega ^ { 1 }$ is exact, then $f = \varphi _ { q }$ . In $\mathbf { R } ^ { n }$ , by Poincare lemma 4.15 in Subsection 1.4.4, the only requirement is that ω1 is closed, i.e., $\frac { \partial f } { \partial g }$ is symmetric. Thus, any transformation from $\mathbf { R } ^ { n }$ into itself with a symmetric Jacobian may be called a locally gradient transformation.

Definition 2.32. Let $S$ be an $r$ -dim submanifold in $\mathbf { R } ^ { 2 n }$ . $S$ is called an isotropic, coisotropic, Lagrangian, or $K$ -Lagrangian submanifold if for any $z \in S$ , $T _ { z } S$ is an isotropic, coisotropic, Lagrangian, or $K$ -Lagrangian subspace of $T _ { z } \mathbf { R } ^ { 2 n }$ respectively.

It is obvious that the graph of any gradient transformation is Lagrangian.

Corollary 2.33. A Lagrangian submanifold $S$ in $\mathbf { R } ^ { 2 n }$ is the graph of some gradient transformation $f : \mathbf { R } ^ { n }  \mathbf { R } ^ { n } , S = G _ { f } ,$ , iff its tangent space $T _ { z } S$ is transversal to $\mathbf { R } _ { p } ^ { n }$ in $T _ { z } \mathbf { R } ^ { 2 n }$ for any $z \in S$ .

Corollary 2.34. A transformation $W ( z ) : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ is a conformally canonical transformation iff $W ( s )$ is Lagrangian for any Lagrangian submanifold $S$ .

# 3.2.5 Hamilton–Jacobi Equations

Consider a canonical system

$$
\frac { \mathrm { d } z ( t ) } { \mathrm { d } t } = J ^ { - 1 } H _ { z } , \quad z ( 0 ) = z _ { 0 } ,
$$

with the Hamiltonian $H ( z ) = H ( p , q )$ . Let $z ( t ) = ( p ( t ) , q ( t ) ) ^ { \prime }$ be its solution and $G ( t )$ the 1-parameter group of diffeomorphisms in $\mathbf { R } ^ { 2 n }$ .

$$
G ( t ) : \ z _ { 0 } = \left[ \begin{array} { c } { { p _ { 0 } } } \\ { { q _ { 0 } } } \end{array} \right] \longrightarrow z ( t ) = G ( t ) z _ { 0 } = \left[ \begin{array} { c } { { p ( t ) } } \\ { { q ( t ) } } \end{array} \right] , \quad G ( 0 ) = I .
$$

Let $M _ { 0 } = \left\{ \begin{array} { c } { { p _ { 0 } } } \\ { { q _ { 0 } } } \end{array} \right\}$ be an $n$ -dim initial manifold, $p _ { 0 }$ a function of $q _ { 0 }$ , and $M _ { 0 }$ form a Lagrangian manifold, i.e., M0 =  p0(q0)q0 and $\frac { \partial p _ { 0 } } { \partial q _ { 0 } } \in S m$ . Since $G ( t )$ : $\left[ \begin{array} { c } { { p _ { 0 } } } \\ { { q _ { 0 } } } \end{array} \right] \to \left[ \begin{array} { c } { { p ( t ) } } \\ { { q ( t ) } } \end{array} \right]$ is a canonical transformation for a fixed $t$ in some neighbourhood of $\mathbf { R } ^ { 2 n }$ , and

$$
G _ { * } ( t ) = { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } = { \left[ \begin{array} { l l } { { \frac { \partial p } { \partial p _ { 0 } } } } & { { \frac { \partial p } { \partial q _ { 0 } } } } \\ { { \frac { \partial q } { \partial p _ { 0 } } } } & { { \frac { \partial q } { \partial q _ { 0 } } } } \end{array} \right] }
$$

is a symplectic matrix,

$$
{ \left[ \begin{array} { l } { Y _ { 1 } } \\ { Y _ { 2 } } \end{array} \right] } = G _ { * } \left[ { \begin{array} { l } { { \frac { \partial p _ { 0 } } { \partial q _ { 0 } } } } \\ { I } \end{array} } \right] = { \left[ \begin{array} { l } { A { \frac { \partial p _ { 0 } } { \partial q _ { 0 } } } + B } \\ { C { \frac { \partial p _ { 0 } } { \partial q _ { 0 } } } + D } \end{array} \right] }
$$

is a symmetric pair. If $\left| C \frac { \partial p _ { 0 } } { \partial q _ { 0 } } + D \right| \neq 0$ , then $\left[ \begin{array} { l } { Y _ { 1 } } \\ { Y _ { 2 } } \end{array} \right] \sim \left[ \begin{array} { l } { N } \\ { I } \end{array} \right]$

$$
N = \left[ A \frac { \partial p _ { 0 } } { \partial q _ { 0 } } + B \right] \left[ C \frac { \partial p _ { 0 } } { \partial q _ { 0 } } + D \right] ^ { - 1 } \in S m ( n ) .
$$

By Theorem 2.29, $p$ can be represented as a function of $q$ , i.e., $p ( t ) = p ( q , t )$ .

Let ${ \cal H } ( q ) = - { \cal H } ( p , q ) | _ { p = p ( q ) } = - { \cal H } ( p ( q ) , q )$ . Consider a 1-form in $\mathbf { R } ^ { n + 1 }$

$$
\omega ^ { 1 } = p \mathsf { d } q + \overline { { H } } \mathsf { d } t .
$$

There is a scalar function $\varphi ( { \boldsymbol { q } } , t )$ such that

$$
\omega ^ { 1 } = p \mathbf { d } q + \overline { { H } } \mathbf { d } t = \mathbf { d } \varphi ,
$$

iff $\omega ^ { 1 }$ is closed, i.e., the following matrix

$$
\left[ \begin{array} { c c c c } { \frac { \partial p _ { 1 } } { \partial q _ { 1 } } } & { \cdots } & { \frac { \partial p _ { 1 } } { \partial q _ { n } } } & { \frac { \partial p _ { 1 } } { \partial t } } \\ { \vdots } & & { \vdots } & { \vdots } \\ { \frac { \partial p _ { n } } { \partial q _ { 1 } } } & { \cdots } & { \frac { \partial p _ { n } } { \partial q _ { n } } } & { \frac { \partial p _ { n } } { \partial t } } \\ { \frac { \partial \overline { H } } { \partial q _ { 1 } } } & { \cdots } & { \frac { \partial \overline { H } } { \partial q _ { n } } } & { \frac { \partial \overline { H } } { \partial t } } \end{array} \right] = \left[ \begin{array} { c c } { \frac { \partial p } { \partial q } } & { \frac { \partial p } { \partial t } } \\ { \frac { \partial \overline { H } ^ { \prime } } { \partial q } } & { \frac { \partial \overline { H } } { \partial t } } \end{array} \right]
$$

is symmetric. We know that the matrix $\frac { \partial p } { \partial q }$ is symmetric, and so we need to only prove

$$
\frac { \partial p } { \partial t } = \frac { \partial \overline { { H } } } { \partial q } .
$$

By canonical Equations (2.15),

$$
- H _ { q } = \frac { \mathrm { d } p ( q , t ) } { \mathrm { d } t } = \frac { \partial p } { \partial q } \frac { \partial q } { \partial t } + \frac { \partial p } { \partial t } = \frac { \partial p } { \partial q } H _ { p } + \frac { \partial p } { \partial t } .
$$

In addition,

$$
\frac { \partial \overline { { H } } } { \partial q } = - \frac { \partial H ( p ( q , t ) , q ) } { \partial q } = - \Big ( \frac { \partial p } { \partial t } \Big ) ^ { \prime } H _ { p } - H _ { q } .
$$

Thus,

$$
\frac { \partial p } { \partial t } = - H _ { q } - \frac { \partial p } { \partial q } H _ { p } = \frac { \partial \overline { { H } } } { \partial q } .
$$

Consequently, there exists a scalar function $\varphi ( { \boldsymbol { q } } , t )$ , s.t.

$$
p \mathbf { d } q + \overline { { H } } \mathbf { d } t = \mathbf { d } \varphi .
$$

Thus, it follows that

$$
\begin{array} { l } { \displaystyle { p = \frac { \partial \varphi } { \partial q } , } } \\ { \displaystyle { \varphi _ { t } = \overline { { H } } = - H ( p , q ) = - H ( \varphi _ { q } , q ) , } } \end{array}
$$

or

$$
\varphi _ { t } + H ( \varphi _ { q } , q ) = 0 ,
$$

which is called the Hamilton–Jacobi equation.

# Bibliography

[AA88] D.V. Anosov and V.I. Arnold: Dynamical Systems I. Springer, Berlin, (1988).   
[AA89] V. I. Arnold and A. Avez: Ergodic Problems of Classical Mechanics. Addison-Wesley, New York, (1989).   
[Abd02] S. S. Abdullaev: The Hamilton-Jacobi method and Hamiltonian maps. J. Phys. A: Math. Gen., 35(12):2811–2832, (2002).   
[AKN78] V. I. Arnold, V. V. Kozlov, and A. I. Neishtadt: Mathematical Aspects of Classical and Celestial Mechanics. Springer, Berlin, Second edition, (1978).   
[AM78] R. Abraham and J. E. Marsden: Foundations of Mechanics. Reading, MA: Addison-Wesley, Second edition, (1978).   
[AMR88] R. Abraham, J. E. Marsden, and T. Ratiu: Manifolds, Tensor Analysis, and Applications. AMS 75. Springer-Verlag, Berlin, Second edition, (1988).   
[AN90] A. I. Arnold and S.P. Novikov: Dynamical System IV. Springer Verlag, Berlin, (1990).   
[Arn88] V. I. Arnold: Geometrical Methods in The Theory of Ordinary Differential Equations. Springer-Verlag, Berlin, (1988).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Berlin Heidelberg: Springer-Verlag, GTM 60, Second edition, (1989).   
[Ber00] R. Berndt: An Introduction to Symplectic Geometry. AMS Providence, Rhode Island, (2000).   
[Bir23] G. D. Birkhoff: Relativity and Modern Physics. Harvard Univ. Press, Cambridge, Mass., Second edition, (1923).   
[BK89] G.W. Bluman and S. Kumei: Symmetries and differential equations. AMS 81. Springer-Verlag, New York, (1989).   
[Car65] C. Carathe’odory: Calculus of Variation and Partial Differential Equations of First Order, Vol.1. Holden-Day, San Franscisco, (1965).   
[Car70] H. Cartan: Differential Forms. Houghton-Mifflin, Boston, (1970).   
[CH53] R. Courant and D. Hilbert: Methods of Mathematical Physics. Interscience, New York, Second edition, (1953).   
[Che53] S. S. Chern: Differential Manifolds. University of Chicago, (1953). Lecture notes.   
[Fen86] K. Feng: Difference schemes for Hamiltonian formalism and symplectic geometry. J. Comput. Math., 4:279–289, (1986).   
[Fla] H. Flanders: Differential Forms. Academie Press, New York, Second edition, (1963).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Berlin, Springer, (1987).   
[FQ91a] K. Feng and M.Z. Qin: Hamiltonian Algorithms for Hamiltonian Dynamical Systems. Progr. Natur. Sci., 1(2):105–116, (1991).   
[FQ91b] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FQ03] K. Feng and M. Z. Qin: Symplectic Algorithms for Hamiltonian Systems. Zhejiang Science and Technology Publishing House, Hangzhou, in Chinese, First edition, (2003).


<!-- chunk 0004: pages 211-280 -->
[FWQW89] K. Feng, H. M. Wu, M.Z. Qin, and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[Gol80] H. Goldstein: Classical Mechanics. Addison-Wesley Reading, Massachusetts, (1980).   
[GS84] V. Guillemin and S. Sternberg: Symplectic Techniques in Physics. Cambridge University Press, Cambridge, (1984).   
[Lan95] S. Lang: Differential and Riemannian Manifolds. Springer-Verlag, Berlin, (1995).   
[LL99] L. D. Landau and E. M. Lifshitz: Mechanics, Volume I of Course of Theoretical Physics. Corp. Butterworth, Heinemann, New York, Third edition, (1999).   
[LM87] P. Libermann and C.M. Marle: Symplectic Geometry and Analytical Mechanics. Reidel Pub. Company, Boston, First edition, (1987).   
[Mac70] S. MacLanc: Hamiltonian mechanics and geometry. Amer. Math. Mon., 77(6):570– 586, (1970).   
[Sie43] C.L. Siegel: Symplectic geometry. Amer. J. Math, 65:1–86, (1943).   
[Tre75] F. Treves: Pseodo-Differential Operator. N.Y.: Acad. Press, First edition, (1975).   
[Wei77] A. Weinstein: Lectures on symplectic manifolds. In CBMS Regional Conference, 29. American Mathematical Society, Providence, RI , (1977).   
[Wes81] C. Von. Westenholz: Differential Forms in Mathematical Physics. North-Holland, Amsterdam, Second edition, (1981).
