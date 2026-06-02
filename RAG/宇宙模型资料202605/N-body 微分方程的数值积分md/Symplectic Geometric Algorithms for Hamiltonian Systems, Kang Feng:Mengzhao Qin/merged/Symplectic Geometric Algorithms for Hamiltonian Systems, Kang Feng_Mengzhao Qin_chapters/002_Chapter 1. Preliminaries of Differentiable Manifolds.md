# Chapter 1. Preliminaries of Differentiable Manifolds

Before introducing the concept of differentiable manifold, we first explain what mapping is. Given two sets $X$ , $Y .$ , and a corresponding principle, if for any $x \in X$ , there exists $y = f ( x ) \in Y$ to be its correspondence, then $f$ is a mapping of the set $X$ into the set $Y$ , which is denoted as $f : X \to Y . X$ is said to be the domain of definition of $f$ , and $f ( x ) = \{ f ( x ) \mid x \in X \} \subset Y$ is said to be the image of $f$ . If $f ( X ) = Y$ , then $f$ is said to be surjective or onto; if $f ( x ) = f ( x ^ { \prime } ) \Rightarrow x = x ^ { \prime }$ , then $f$ is said to be injective (one-to-one); if $f$ is both surjective and injective (i.e., $X$ and $Y$ have a one-to-one correspondence under $f$ ), $f$ is said to be bijective. For a bijective mapping $f$ , if we define $x = f ^ { - 1 } ( y )$ , then $f ^ { - 1 } : Y \to X$ is said to be the inverse mapping of $f$ . In abstract algebra, a homomorphism is a structure-preserving map between two algebraic structures (such as groups, rings, or vector spaces). For example, for two groups $G$ and $G ^ { \prime }$ and a mapping $f : G \to G ^ { \prime }$ , $a  f ( a )$ , if $f ( a , b ) = f ( a ) \cdot f ( b ) , \forall a , b \in G$ , then $f$ is said to be a homomorphism from $G$ to $G ^ { \prime }$ . A homomorphism is a map from one algebraic structure to another of the same type that preserves all the relevant structures, i.e., properties such as identity element, inverse element, and binary operations. An isomorphism is a bijective homomorphism. If $f$ is a $G  G ^ { \prime }$ homomorphic mapping, and also a one-to-one mapping from $G$ to $G ^ { \prime }$ , then $f$ is said to be a $G  G ^ { \prime }$ isomorphic mapping. An epimorphism is a surjective homomorphism. Given two topological spaces $( x , \tau )$ and $( y , \tau )$ , if the mapping $f : X \to Y$ is one-to-one, and both $f$ and its inverse mapping $f ^ { - 1 } : Y \to X$ are continuous, then $f$ is said to be a homeomorphism. If $f$ and $f ^ { - 1 }$ are also differentiable, then the mapping is said to be diffeomorphism. A monomorphism (sometimes called an extension) is an injective homomorphism. A homomorphism from an object to itself is said to be an endomorphism. An endomorphism that is also an isomorphism is said to be an automorphism. Given two manifolds $M$ and $N$ , a bijective mapping $f$ from $M$ to $N$ is called a diffeomorphism if both $f : M \to N$ and its inverse $f ^ { - 1 } : N \to M$ are differentiable (if these functions are $r$ times continuously differentiable, $f$ is said to be a $C ^ { r }$ -diffeomorphism).

Many differential mathematical methods and concepts are used in classical mechanics and modern physics: differential equations, phase flow, smooth mapping, manifold, Lie group and Lie algebra, and symplectic geometry. If one would like to construct a new numerical method, one needs to understand these basic theories and concepts. In this book, we briefly explain manifold, symplectic algebra, and symplectic geometry. In a series of books[AM78,Che53,Arn89,LM87,Ber00,Wes81] can be found these materials.

# 1.1 Differentiable Manifolds

The concept of manifold is an extension of Euclidean space. Roughly speaking, a manifold is an abstract mathematical space where every point has a neighborhood that resembles Euclidean space (homeomorphism). Differentiable manifold is one of the manifolds that can have differentiable structures.

# 1.1.1 Differentiable Manifolds and Differentiable Mapping

Definition 1.1. A Hausdorff space $M$ with countable bases is called an $n$ -dimensional topological manifold, if for any point in $M$ there exists an open neighborhood homeomorphic to an open subset of $\mathbf { R } ^ { n }$ .

Remark 1.2. Let $( U , \varphi ) , ( V , \psi )$ be two local coordinate systems (usually called chart) on the topological manifold $M . \ ( U , \varphi ) , ( V , \psi )$ are said to be compatible, if $U \cap V = \emptyset$ , or the change of coordinates $\varphi \circ \psi ^ { - 1 }$ and $\psi \circ \varphi ^ { - 1 }$ are smooth when $U \cap V \neq \emptyset$ .

Definition 1.3. A chart is a domain $U \subset \mathbf { R } ^ { n }$ together with a 1 to 1 mapping $\varphi : W \to$ $U$ of a subset $W$ of the manifold $M$ onto $U$ . $\varphi ( x )$ is said to be the image of the point $x \in W \subset M$ on the chart $U$ .

Definition 1.4. A collection of charts $\varphi _ { i } : W _ { i } \to U _ { i }$ is an atlas on $M$ if $1 ^ { \circ }$ Any two charts are compatible. $2 ^ { \circ }$ Any point $x \in M$ has an image on at least one chart.

Remark 1.5. If a smooth atlas on a topological manifold $M$ possesses with its all compatible local coordinate systems (chart), then this smooth atlas is called the maximum atlas.

Definition 1.6. If an $n$ -dimensional topological manifold $M$ is equipped with the maximal smooth atlas $\mathcal { A }$ , then $( M , A )$ is called the $n$ -dimensional differentiable manifold, and $\mathcal { A }$ is called the differentiable structure on $M$ .

Definition 1.7. Two atlases on $M$ are equivalent if their union is also an atlas (i.e., if any chart of the first atlas is compatible with any chart of the second).

Remark 1.8. Suppose $M$ is the $n$ -dimensional topological manifold, $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \}$ is a smooth atlas on $M$ . Then there exists a unique differentiable structure $\ b { A } ^ { * }$ , which contains $\mathcal { A }$ . Hence, a smooth atlas determines a unique differentiable structure on $M$ . The local coordinate system will be called (coordinate) chart subsequently.

Definition 1.9. A differentiable manifold structure on $M$ is a class of equivalent atlases.

Definition 1.10. A differentiable manifold $M$ is a set $M$ together with a differentiable manifold structure on it. A differentiable manifold structure is induced on set $M$ if an atlas consisting of compatible charts is prescribed.

Below are examples of differentiable manifold.

Example 1.11. $\mathbf { R } ^ { n }$ is an $n$ -dimensional differentiable manifold. Let $\mathcal { A } = \{ ( \mathbf { R } ^ { n } , I ) \}$ , where $I$ is the identity mapping.

Example 1.12. $S ^ { n }$ is an $n$ -dimensional differentiable manifold. We only discuss the $n = 1$ case. Let

$$
\begin{array} { r l } & { U _ { 1 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 1 } > 0 \} , \quad U _ { 2 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 1 } < 0 \} , } \\ & { } \\ & { U _ { 3 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 2 } > 0 \} , \quad U _ { 4 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 2 } < 0 \} . } \end{array}
$$

Define $\varphi _ { i } : U _ { i } \to ( - 1 , 1 )$ , such that (s.t.)

$$
\varphi _ { i } ( u ^ { 1 } , u ^ { 2 } ) = u ^ { 2 } , \quad i = 1 , 2 ; \quad \varphi _ { i } ( u ^ { 1 } , u ^ { 2 } ) = u ^ { 1 } , \quad i = 3 , 4 .
$$

Note that on $\varphi _ { 1 } ( U _ { 1 } \cap U _ { 3 } )$

$$
\varphi _ { 3 } \circ \varphi _ { 1 } ^ { - 1 } : u ^ { 2 } \longrightarrow ( \sqrt { 1 - ( u ^ { 2 } ) ^ { 2 } } , u ^ { 2 } ) \longrightarrow \sqrt { 1 - ( u ^ { 2 } ) ^ { 2 } }
$$

is smooth, then $\scriptstyle { \mathcal { A } } = \{ ( U _ { k } , \varphi _ { k } ) \}$ is a smooth atlas on $S ^ { 1 }$ .

Example 1.13. $R P ^ { n }$ is an $n$ -dimensional differentiable manifold.

Let

$$
U _ { k } = \{ [ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) ] \mid ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) \in S ^ { n } , u ^ { k } \neq 0 \} , \quad k = 1 , \cdots , n + 1
$$

defines $\varphi _ { k } : U _ { k } \to \operatorname { I n t } B ^ { n } ( 1 )$ , s.t.

$$
\varphi _ { k } ( [ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) ] ) = u ^ { k } | u ^ { k } | ^ { - 1 } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { k - 1 } , u ^ { k + 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) ,
$$

where $B ^ { n } ( 1 ) = \left\{ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } ) \in { \bf \delta R } ^ { n } \Big | \sum _ { i = 1 } ^ { n } ( u ^ { i } ) ^ { 2 } \le 1 \right\}$ . It is easy to prove that $\mathcal { A }$ $\mathbf { \Omega } = \{ ( U _ { k } , \varphi _ { k } ) \}$ is a smooth atlas on $R P ^ { n }$ .

Example 1.14. Let $M , N$ be $m$ - and $n$ -dimensional differentiable manifolds, respectively, then $M \times N$ is a $m + n$ dimensional differentiable manifold (product manifold).

Suppose ${ \mathcal { A } } = \{ ( U _ { \alpha } , \varphi _ { \alpha } ) \} , B = \{ ( V _ { \alpha } , \psi _ { \alpha } ) \}$ are smooth atlases on $M , N$ respectively. Denote $\mathcal { A } \times \mathcal { B } { = } \{ ( U _ { \alpha } \times V _ { \lambda } , \varphi _ { \alpha } \times \psi _ { \lambda } ) \}$ , where $\varphi _ { \alpha } \times \psi _ { \lambda } \colon U _ { \alpha } \times V _ { \lambda } \to$ $\varphi _ { \alpha } ( U _ { \alpha } ) \times \psi _ { \lambda } ( V _ { \lambda } ) , ( \varphi _ { \alpha } \times \psi _ { \lambda } ) ( p , q ) = { \big ( } \varphi _ { \alpha } ( p ) , \psi _ { \lambda } ( q ) { \big ) } , ( p , q ) \in U _ { \alpha } \times V _ { \lambda }$ , then $\mathcal { A } \times \mathcal { B }$ is a smooth atlas on $M \times N$ .

Definition 1.15. Let $M , N$ be $m$ - and $n$ -dimensional differentiable manifolds, respectively. A continuous mapping $f : M \to N$ is called $C ^ { k }$ differentiable at $p \in M$ , if the local representation $\widehat { f } = \psi \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \psi ( V )$ is $C ^ { k }$ differentiable for the charts $( U , \varphi ) , ( V , \psi )$ corresponding to points $p$ and $f ( \boldsymbol p )$ , and $f ( U ) \subset V$ . If $f$ is $C ^ { k }$ differentiable in each $p \in M$ , then $f$ is called $C ^ { k }$ differentiable, or called $C ^ { k }$ mapping. See Fig. 1.1.

![](images/39508fc6254819a70f06e2da49b1e6b8112a613660f261ed35290dbf5e95258e.jpg)  
Fig. 1.1. A differentiable mapping

Example 1.16. Let $M _ { 1 }$ , $M _ { 2 }$ be $m$ - and $n$ -dimensional differentiable manifolds, respectively. Define $\theta _ { 1 } : M _ { 1 } \times M _ { 2 } \to M _ { 1 }$ , $\theta _ { 2 } : M _ { 1 } \times M _ { 2 } \to M _ { 2 }$ , such that

$$
\theta _ { 1 } ( p , q ) = p , \quad \theta _ { 2 } ( p , q ) = q , \quad \forall ( p , q ) \in M _ { 1 } \times M _ { 2 } ,
$$

then $\theta _ { 1 } , \theta _ { 2 }$ are all smooth mappings.

If the charts on $M _ { 1 } , M _ { 2 }$ are denoted by $( U , \varphi ) , ( V , \psi )$ , then it is easy to show that $( U \times V , \varphi \times \psi )$ is the chart on $\mathbf { M } _ { 1 } \times M _ { 2 }$ . Thus, the local coordinate expression of $\theta _ { 1 }$ ,

$$
\widehat { \theta } _ { 1 } = \varphi \circ \theta _ { 1 } \circ ( \varphi \times \psi ) ^ { - 1 } : ( \varphi \times \psi ) ( U \times V ) \longrightarrow \varphi ( U ) , \quad \widehat { \theta } _ { 1 } ( u , v ) = u
$$

is a smooth mapping. Therefore, $\theta _ { 1 }$ is a smooth mapping. Likewise, $\theta _ { 2 }$ is also a smooth mapping.

Example 1.17. Let $M , N _ { 1 } , N _ { 2 }$ be differentiable manifolds.

$$
f _ { 1 } : M \longrightarrow N _ { 1 } , \quad f _ { 2 } : M \longrightarrow N _ { 2 }
$$

are $C ^ { k }$ -mapping. Define

$$
f : M \longrightarrow N _ { 1 } \times N _ { 2 } , \quad f ( p ) = ( f _ { 1 } ( p ) , f _ { 2 } ( p ) ) , \quad \forall p \in M ,
$$

then $f$ is a $C ^ { k }$ -mapping.

$\forall p _ { 0 } \in M$ , let $N _ { 1 }$ contain the chart $( V , \psi )$ of $f _ { 1 } ( p _ { 0 } )$ , and let $N _ { 2 }$ contain the chart $( W , \chi )$ of $f _ { 2 } ( \boldsymbol { p } _ { 0 } )$ , and $M$ contain the chart $( U , \varphi )$ of $p _ { 0 }$ . Assume $f _ { 1 } ( U ) \subset V , f _ { 2 } ( U ) \subset$ $W$ , and

$$
\begin{array} { r l } & { \widehat { f } _ { 1 } : \psi \circ f _ { 1 } \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow \psi ( V ) , } \\ & { } \\ & { \widehat { f } _ { 2 } : \chi \circ f _ { 2 } \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow \chi ( W ) } \end{array}
$$

are all $C ^ { k }$ -mapping, and $( V \times W , \varphi \times \chi )$ is a chart that contains $( f _ { 1 } ( p _ { 0 } ) , f _ { 2 } ( p _ { 0 } ) ) =$ $f ( p _ { 0 } )$ on the product manifold $N _ { 1 } \times N _ { 2 }$ , which satisfies $f ( U ) \subset V \times W$ . Then we have

$$
\widehat { f } = ( \psi \times \chi ) \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow ( \psi \times \chi ) ( U \times W ) , \quad \widehat { f } = ( \widehat { f } _ { 1 } , \widehat { f } _ { 2 } ) ,
$$

i.e., $f$ is $C ^ { k }$ -mapping.

Remark 1.18. According to the definition, if $f : { \cal M }  { \cal N } , g : { \cal N }  { \cal L }$ are $C ^ { k }$ - mappings, then $g \circ f : M \to L$ is also a $C ^ { k }$ -mapping.

Definition 1.19. Let $M , N$ be differentiable manifolds, $f : M \to N$ is a homeomorphism. If $f , f ^ { - 1 }$ are smooth, then $f$ is called diffeomorphism from $M$ to $N$ . If there exists a diffeomorphism between differentiable manifolds $M$ and $N$ , then $M$ and $N$ are called differentiable manifolds under diffeomorphism, denoted by $M \simeq N$ .

If we define two smooth atlases $( { \bf R } , I ) , ( { \bf R } , \varphi )$ on $\mathbf { R }$ , and $\varphi : \mathbf { R }  \mathbf { R } , \varphi ( u ) = u ^ { 3 }$ , because the change of coordinates $I \circ \varphi ^ { - 1 } ( u ) = \sqrt [ 3 ] { u }$ in $u = 0$ is not differentiable, then $( \mathbf { R } , I )$ and $( \mathbf { R } , \varphi )$ determine two different differentiable structures $\mathcal { A }$ , $\mathcal { A } ^ { \prime }$ on $\mathbf { R }$ . However, if we define $f : ( \mathbf { R } , { \mathcal { A } } )  ( \mathbf { R } , { \mathcal { A } } ^ { \prime } )$ , $\{ f ( u ) \} = u ^ { 3 }$ , then $( \mathbf { R } , { \mathcal { A } } ) \simeq ( \mathbf { R } , { \mathcal { A } } ^ { \prime } )$ .

In fact, there exist examples that are not homeomorphism in a differentiable manifold, like the famous Milnor exotic sphere.

# 1.1.2 Tangent Space and Differentials

In order to establish the differential concept for differentiable mapping on a differentiable manifold, we first need to extend the concept of tangent of curve and tangent plane of surface in Euclidean space. If we take the tangent vector in Euclidean space not simply as a vector with size and direction, but as a linear mapping, which satisfies the Leibniz rule, from the differentiable functional space to $\mathbf { R }$ , then the definition of tangent vector can be given similarly for a manifold.

Let $M$ be the $m$ -dimensional differentiable manifold, $p \in M$ be a fixed point. Let $C ^ { \infty } ( p )$ be the set of all smooth functions that are defined in some neighborhood of $p$ . Define operations on $M$ that have the following properties:

$$
\begin{array} { l } { { ( f + g ) ( p ) = f ( p ) + g ( p ) , } } \\ { { \mathit { \Omega } } } \\ { { ( \alpha f ) ( p ) = \alpha f ( p ) , } } \\ { { \mathit { \Omega } } } \\ { { ( f g ) ( p ) = f ( p ) g ( p ) . } } \end{array}
$$

Definition 1.20. A tangent vector $X _ { p }$ at the point $p \in M$ is a mapping

$$
X _ { p } : C ^ { \infty } \longrightarrow \mathbf { R } ,
$$

that has the following properties:

$1 ^ { \circ }$ $X _ { p } ( f ) = X _ { p } ( g )$ , if $f$ , $g \in C ^ { \infty } ( p )$ are consistent in some neighborhood of the point $p$ .

$2 ^ { \circ }$ $X _ { p } ( \alpha f + \beta g ) = \alpha X _ { p } ( f ) + \beta X _ { p } ( g ) , \forall \ : f$ , $g \in C ^ { \infty } ( p )$ , $\forall \alpha$ , β ∈ R.

$3 ^ { \circ }$ $X _ { p } ( f g ) = f ( p ) X _ { p } ( g ) + g ( p ) X _ { p } ( f ) , \forall f , g \in C ^ { \infty } ( p )$ (which is equivalent to the derivative operation in Leibniz rule).

Denote $T _ { p } M = \{ { \mathrm { A l l } } $ tangent vectors at the point $p \in M \}$ and define operation:

$$
\begin{array} { r l } & { ( X _ { p } + Y _ { p } ) ( f ) = X _ { p } ( f ) + Y _ { p } ( f ) , } \\ & { ( k X _ { p } ) ( f ) = k X _ { p } ( f ) , \quad \forall f \in C ^ { \infty } ( p ) . } \end{array}
$$

It is easy to verify that $T _ { p } M$ becomes the vector space that contains the above operation, which is called the tangent space at the point $p$ of the differential manifold $M$ .

Remark 1.21. By definition of the tangent vector, it is easy to know that if $f$ is the constant function, $X _ { p } ( f ) = 0$ for $X _ { p } \in T _ { p } M$ .

Lemma 1.22. Let $( U , \varphi )$ be the chart that contains $p \in M$ , and let $x ^ { 1 } , \cdots , x ^ { m }$ , $\varphi ( p )$ $\mathbf { \Sigma } = ( a ^ { 1 } , \cdots , a ^ { m } )$ be the coordinate functions. If $f \in C ^ { \infty } ( p )$ , then there exists a function $g _ { i }$ in some neighborhood $W$ of $p \in M$ , such that

$$
f ( \boldsymbol { q } ) = f ( \boldsymbol { p } ) + \sum _ { i = 1 } ^ { m } ( x ^ { i } ( \boldsymbol { q } ) - a ^ { i } ) g _ { i } ( \boldsymbol { q } ) , \quad \forall \boldsymbol { q } \in W ,
$$

$$
g _ { i } ( p ) = \frac { \partial f } { \partial x ^ { i } } \Big | _ { p } \Big ( w h e r e \frac { \partial f } { \partial x ^ { i } } \Big | _ { p } = \frac { \partial } { \partial x ^ { i } } \Big | _ { p } ( f ) = \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } \Big | _ { \varphi ( p ) } \Big ) .
$$

Proof. Assume $\varphi ( p ) = O \in \mathbf { R } ^ { m }$ , and $f$ is well defined in some neighborhood of $p$ . Let $W = \varphi ^ { - 1 } ( B ^ { m } )$ . Then $\forall q \in W$ and we have

$$
f ( q ) - f ( p ) = f \circ \varphi ^ { - 1 } ( u ) - f \circ \varphi ^ { - 1 } ( O ) .
$$

After calculation, we obtain

$$
f ( q ) - f ( p ) = \sum _ { i = 1 } ^ { m } u ^ { i } \overline { { { g } } } _ { i } ( u ) ,
$$

where gi(u) =  10 ∂f ◦ ϕ−1∂ui ( $\begin{array} { r } { \overline { { g } } _ { i } ( u ) \ = \ \int _ { 0 } ^ { 1 } \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } ( s u ^ { 1 } , \cdots , s u ^ { m } ) \mathrm { d } s \ ( i \ = \ 1 , \cdots , m ) } \end{array}$ . Let $\overline { { { g } } } _ { i } ( \varphi ( q ) ) \ =$ $g _ { i } ( q )$ , then $g _ { i }$ is smooth on $W$ , and satisfies

$$
\begin{array} { l } { f ( q ) = f ( p ) + \displaystyle \sum _ { i = 1 } ^ { m } x ^ { i } ( q ) g _ { i } ( q ) , } \\ { g _ { i } ( p ) = \overline { { g } } _ { i } ( O ) = \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } \Big | _ { O } = \frac { \partial f } { \partial x ^ { i } } \Big | _ { p } . } \end{array}
$$

Hence lemma is proved.

Theorem 1.23. Define $\frac { \partial } { \partial x ^ { i } } \Big | _ { p } : C ^ { \infty } ( p )  { \bf R } , \frac { \partial } { \partial x ^ { i } } \Big | _ { p } ( f ) = \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } \Big | _ { \varphi ( p ) } , \forall f \in$ $C ^ { \infty } ( p )$ , then ${ \frac { \partial } { \partial x ^ { i } } } \bigg | _ { p } \left( i = 1 , \cdot \cdot \cdot , m \right)$ is a group of bases for $T _ { p } M$ . Therefore, $\mathrm { d i m } T _ { p } M$ $= m$ , and for $X _ { p } \in T _ { p } M$ , we have

$$
X _ { p } = \sum _ { i = 1 } ^ { m } X _ { p } ( x ^ { i } ) { \frac { \partial } { \partial x ^ { i } } } { \bigg | } _ { p } .
$$

Proof. $\forall X _ { p } \in T _ { p } M$ , as $f \in C ^ { \infty } ( p )$ . By Lemma 1.22, we know

$$
f = f ( \boldsymbol { p } ) + \sum _ { i = 1 } ^ { m } ( x ^ { i } - a ^ { i } ) g _ { i } ,
$$

then

$$
X _ { p } ( f ) = \sum _ { i = 1 } ^ { m } X _ { p } [ ( x ^ { i } - a ^ { i } ) g _ { i } ] = \sum _ { i = 1 } ^ { m } X _ { p } ( x ^ { i } ) { \frac { \partial f } { \partial x ^ { i } } } { \Big | } _ { p } = \sum _ { i = 1 } ^ { m } X _ { p } ( x ^ { i } ) { \frac { \partial } { \partial x ^ { i } } } { \Big | } _ { p } ( f ) .
$$

The decomposed coefficients, $\{ X _ { p } ( x ^ { i } ) \}$ , of $X _ { p }$ with respect to (w.r.t.) the bases $\frac { \partial } { \partial x ^ { i } } \Big | _ { p } \ ( i \ = \ 1 , \cdot \cdot \cdot , m )$ are called coordinates of the tangent vector $X _ { p }$ w.r.t. the char $( U , \varphi )$ . -

Remark 1.24. By Theorem 1.23 we know: if the coordinates of $X _ { p }$ w.r.t. chart $( U , \varphi )$ are defined as $( X _ { p } ( x ^ { 1 } ) , \cdot \cdot \cdot , X _ { p } ( x ^ { m } ) )$ , then $T _ { p } M$ and $\mathbf { R } ^ { m }$ are isomorphisms, and the basis for $T _ { p } M$ corresponds exactly to the standard basis for $\mathbf { R } ^ { m }$ , i.e., $\left. { \frac { \partial } { \partial x ^ { i } } } \right| _ { p } \mapsto e _ { i } =$ $( 0 , \cdots , 1 , 0 , \cdots , 0 )$ .

# 1. Definition and properties of differentials of mappings

The definition of differentials of a mapping is as follows:

Definition 1.25. Let $f : M \to N$ be a smooth mapping. $\forall p \in M$ , $X _ { p } \in T _ { p } M$ , we define $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ that satisfies:

$$
f _ { * p } ( X _ { p } ) ( g ) = X _ { p } ( g \circ f ) , \quad \forall g \in C ^ { \infty } ( f ( p ) ) .
$$

This linear mapping $f _ { \ast p }$ is called the differential of $f$ at the $p \in M$ .

Definition 1.26. The differential of the identity mapping $I$ is an identity mapping, i.e., $I _ { \ast p } : T _ { p } M \to T _ { p } M$ .

Remark 1.27. Let $M , N , L$ be differentiable manifolds, $p \in M$ , and $f : M \to N ,$ g : $N  L$ are smooth mappings, then $( g \circ f ) _ { \ast p } = g _ { \ast f ( p ) } \circ f _ { \ast p }$ .

Remark 1.28. If $f : M \to N$ is a diffeomorphism, then $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is a isomorphism.

Proposition 1.29. Let $x ^ { 1 } , \cdots , x ^ { m }$ , $y ^ { 1 } , \cdots , y ^ { n }$ be the coordinate functions of $( U , \varphi )$ , $( V , \psi )$ respectively, then

$$
f _ { \ast p } \bigg ( \frac { \partial } { \partial x ^ { i } } \Big | _ { p } \bigg ) = \sum _ { j = 1 } ^ { n } \frac { \partial f _ { j } } { \partial x ^ { i } } \Big | _ { p } \frac { \partial } { \partial y ^ { j } } \Big | _ { f ( p ) } ,
$$

where $f _ { j } = y ^ { j } \circ f$ .


<!-- chunk 0002: pages 71-140 -->
Proof. Since

$$
f _ { \ast p } \Big ( \frac { \partial } { \partial x ^ { i } } \Big | _ { p } \Big ) ( y ^ { k } ) = \frac { \partial } { \partial x ^ { i } } \Big | _ { p } ( y ^ { k } \circ f ) = \frac { \partial f _ { k } } { \partial x ^ { i } } \Big | _ { p } ,
$$

therefore, by Theorem 1.23 we have

$$
\begin{array} { r c l } { \displaystyle f _ { * p } \Big ( \frac { \partial } { \partial x ^ { i } } \Big | _ { p } \Big ) } & { = } & { \displaystyle \sum _ { i , j = 1 } ^ { n } \frac { \partial f _ { j } } { \partial x ^ { i } } \Big | _ { p } \frac { \partial y ^ { k } } { \partial y ^ { j } } \Big | _ { f ( p ) } } \\ & { = } & { \displaystyle \sum _ { i , j = 1 } ^ { n } \frac { \partial f _ { j } } { \partial x ^ { i } } \Big | _ { p } \frac { \partial } { \partial y ^ { j } } \Big | _ { f ( p ) } ( y ^ { k } ) . } \end{array}
$$

Therefore the proposition is completed.

Let Xp =  ∂∂ xi ， $f _ { * p } ( X _ { p } ) \ : = \ : \sum _ { j = 1 } ^ { n } \beta ^ { j } \frac { \partial } { \partial y ^ { j } } \Bigr | _ { f ( p ) }$ , by Proposition 1.29, we i=1 p   
have

$$
\left( \begin{array} { c } { \beta ^ { 1 } } \\ { \vdots } \\ { \beta ^ { n } } \end{array} \right) = \left( \begin{array} { c c c } { \frac { \partial f _ { 1 } } { \partial x ^ { 1 } } } & { \cdots } & { \frac { \partial f _ { 1 } } { \partial x ^ { m } } } \\ { \vdots } & & { \vdots } \\ { \frac { \partial f _ { n } } { \partial x ^ { 1 } } } & { \cdots } & { \frac { \partial f _ { n } } { \partial x ^ { m } } } \end{array} \right) \left( \begin{array} { c } { \alpha ^ { 1 } } \\ { \vdots } \\ { \alpha ^ { m } } \end{array} \right) .
$$

This matrix $\left( \frac { \partial f _ { i } } { \partial x ^ { j } } \right) _ { n \times m }$ is the Jacobian matrix of $f$ at $p$ w.r.t. charts $( U , \varphi ) , ( V , \psi )$ . Its rank $r k _ { p } f$ is called the rank of $f : M \to N$ at the $p$ . From the above equations, we can easily observe that $f _ { \ast p }$ is equivalent to $ { \mathrm { D } } { \widehat { f } } ( \varphi ( p ) )$ under the assumption of isomorphism, where $\mathrm { D } \widehat { f } ( \varphi ( p ) )$ is the differential at $\varphi ( p )$ of the local representation of $f , \widehat { f } = \psi \circ f \circ \varphi ^ { - 1 }$ .

# 2. Geometrical meaning of differential of mappings

A smooth curve on $M$ is a smooth mapping $c : ( a , b ) \to M$ . The tangent vector, $c _ { * t _ { 0 } } \left( \frac { \mathrm { d } } { \mathrm { d } t } \bigg | _ { t _ { 0 } } \right)$ on $T _ { c ( t _ { 0 } ) } M$ is called the velocity vector of $c$ at $t _ { 0 }$ . Let $f : M \to N$ be a smooth mapping. Then, $f \circ c$ is a smooth curve on $N$ that passes $f ( \boldsymbol p )$ . By composite differentiation, we have

$$
( f \circ c ) _ { * t _ { 0 } } \Big ( \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t = t _ { 0 } } \Big ) = f _ { * p _ { 0 } } \circ c _ { * t _ { 0 } } \Big ( \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t = t _ { 0 } } \Big ) ,
$$

i.e., $f _ { \ast p _ { 0 } }$ transforms the velocity vector of $c$ at $t _ { 0 }$ to the velocity vector of $f \circ c$ at $t _ { 0 }$

# 1.1.3 Submanifolds

The extension of the curve and surface on Euclidean space to the differentiable manifold is the submanifold. In the following section, we focus on the definitions of three submanifolds and their relationship. First, we describe a theorem.

# 1. Inverse function theorem

Theorem 1.30. Let $M$ , $N$ be $m$ -dimensional differentiable manifolds, $f : M \to N$ is a smooth mapping, $p \in M .$ . If $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is an isomorphism, then there exists a neighborhood, $W$ of $p \in M$ , such that

$1 ^ { \circ }$ $f ( W )$ is a neighborhood of $f ( \boldsymbol p )$ in $N$ . $2 ^ { \circ }$ $f | _ { W } : W \to f ( W )$ is a diffeomorphism (this theorem is an extension of the inverse function theorem for a manifold).

Proof. Consider charts $( U , \varphi )$ on $M$ about $p \in M$ and $( V , \psi )$ on $N$ about $f ( p ) \in N$ , so that $f ( U ) \subset V$ . Then, the local representation $\widehat { f } = \psi \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \psi ( V )$ is a smooth mapping. Since $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is an isomorphism, $\operatorname { D } { \hat { f } } ( \varphi ( p ) ) ~ { \mathrm { : } }$ $\mathbf { R } ^ { m } \to \mathbf { R } ^ { m }$ is also an isomorphism. By the inverse function theorem, there exists a neighborhood $O$ of $\varphi ( p ) \in \mathbf { R } ^ { m }$ such that ${ \widehat { f } } ( O )$ is a neighborhood of $\psi ( f ( p ) )$ in $\mathbf { R } ^ { m }$ , and ${ \widehat { f } } : O \to { \widehat { f } } ( O )$ is a diffeomorphism. $O$ has to be chosen appropriately. Let $O \subset \varphi ( U )$ , and ${ \widehat { f } } ( O ) \subset \psi ( V )$ . Let $W = \varphi ^ { - 1 } ( O )$ . Then, $W$ is the neighborhood of $p$ , which meets our requirement. -

Remark 1.31. Given a chart $( V , \psi )$ on $N$ , $f ( p ) \subset V$ , choose $\varphi = \psi \circ f$ and some neighborhood $U$ of $p$ , such that $\varphi ( U ) \subset V$ . By $2 ^ { \circ }$ of Theorem 1.30, $f | _ { W } : W \to$ $f ( W )$ is a diffeomorphism and $( U , \varphi )$ is a chart on $M$ . Hence ${ \widehat { f } } = \psi \circ f \circ \varphi ^ { - 1 } = I$ is an identity mapping from $\varphi ( U )$ to $\psi ( V )$ .

Example 1.32. Suppose $f : \mathbf { R }  S ^ { 1 }$ , defined by $f ( t ) = ( \cos t , \sin t )$ . Using the chart of Example 1.11, we obtain

$$
\widehat { f ^ { \prime } } ( t ) = \left\{ \begin{array} { l l } { \cos t , } & { t \in \Big ( k \pi - \frac { \pi } { 2 } , k \pi + \frac { \pi } { 2 } \Big ) , } \\ { - \sin t , } & { t \in ( k \pi , ( k + 1 ) \pi ) . } \end{array} \right.
$$

Obviously, ${ \widehat { f } } ^ { \prime } ( t ) \neq 0 , \forall t \in \mathbf { R }$ . However, $f : \mathbf { R }  S ^ { 1 }$ is not injective. Thus, $f$ is not a diffeomorphism. This example shows that $f _ { * p } : T _ { p } M \to T _ { f ( p ) } \ N$ isomorphism and $f : M \to N$ homeomorphism at some neighborhood of $p$ are only local properties.

We have discussed the case where $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is an isomorphism. In the following section we turn to the case when $f _ { \ast p }$ is injective.

# 2. Immersion

Definition 1.33. Let $M , N$ be differentiable manifolds, and $f : M \to N$ a smooth mapping, and $p \in M$ . If $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is injective (i.e., $r k _ { p } f = m$ ), then $f$ is said to immerse at $p$ . If $f$ immerses at every $p \in M$ , then $f$ is called an immersion.

Below are some examples of immersion.

Example 1.34. Let $U \in \mathbf { R } ^ { m }$ be an open subset, $\alpha : U  \mathbf { R } ^ { n } , \alpha ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) =$ $( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } , 0 , \cdot \cdot \cdot , 0 )$ .

By definition, $\alpha$ is obviously an immersion, and is often called a model immersion.

Proposition 1.35. Let $M , N$ be $m$ - and $n$ -dimensional differentiable manifolds respectively; $f : M \to N$ is a smooth mapping, $p \in M .$ . If $f$ immerses at $p$ , then there exist charts $( U , \varphi )$ on $M$ about $p \in M$ and $( V , \psi )$ on $N$ about $f ( p ) \in N$ in which the coordinate description $\widehat { f } = \psi \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \psi ( V )$ has the form

$$
\widehat { f } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } , 0 , \cdot \cdot \cdot , 0 ) .
$$

Proof. Choose charts $( U _ { 1 } , \varphi _ { 1 } )$ and $( V _ { 1 } , \psi _ { 1 } )$ appropriately so that $p \in U _ { 1 } , f ( p ) \in$ $V _ { 1 } , \varphi _ { 1 } ( p ) = 0 \in \mathbf { R } ^ { m } , \psi _ { 1 } ( f ( p ) ) = 0 ^ { \prime } \in \mathbf { R } ^ { n }$ and $f ( U _ { 1 } ) \subset V _ { 1 }$ . Since $f$ immerses at $p$ , the rank of Jacobian $J _ { \widehat { f } } ( 0 ) = \left. \left( \frac { \partial \widehat { f } _ { i } } { \partial u ^ { j } } \right) \right| _ { 0 }$ is $m$ , where ${ \widehat { f } } = ( { \widehat { f } } _ { 1 } , \cdots , { \widehat { f } } _ { n } )$ . We can assume that the first $m$ rows in the Jacobian matrix $J _ { \widehat { f } } ( 0 )$ are linearly independent. Then, define a mapping for $\varphi _ { 1 } ( U _ { 1 } ) \times { \mathbf { R } } ^ { n - m }  { \mathbf { R } } ^ { n } = { \mathbf { R } } ^ { m } \times { \mathbf { R } } ^ { n - m }$ by

$$
g ( u , v ) = { \widehat { f } } ( u ) + ( 0 , v ) .
$$

It is easy to prove that $g ( u , 0 ) = { \widehat { f } } ( u )$ maps origin $0 ^ { \prime }$ to itself in $\mathbf { R } ^ { n }$ and the rank of $J _ { g } ( O ^ { \prime } ) = \left[ J _ { \widehat { f } } ( O ) \begin{array} { c } { { 0 } } \\ { { I _ { n - m } } } \end{array} \right]$ is $n$ , where 0 denotes a $m \times ( n - m )$ zero matrix, and by the inverse function theorem, $g$ is a diffeomorphism from a neighborhood of origin of $\mathbf { R } ^ { m }$ to a neighborhood of origin of $\mathbf { R } ^ { n }$ . Shrink $U _ { 1 } , V _ { 1 }$ so that they become $U , V$ , and let $\varphi = \varphi _ { 1 } | U , \psi = g ^ { - 1 } \circ ( \psi | V )$ . Since $\psi \circ f \circ \varphi ^ { - 1 } = g ^ { - 1 } \circ \psi _ { 1 } \circ f \circ \varphi _ { 1 } ^ { - 1 } = g ^ { - 1 } \circ { \widehat { f } } =$ $g ( u , 0 )$ , the proposition is proved. -

Remark 1.36. By definition of immersion, if $f : M \to N$ immerses at $p \in M$ , then $f$ immerses in some neighborhood of $p$ .

Remark 1.37. By Proposition 1.35, $f$ limited in some neighborhood of $p$ has a local injective expression $\widehat { f } = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } , 0 , \cdot \cdot \cdot , 0 )$ . Then, $f$ limited in some neighborhood of $p$ is injective. Note that this is only a local injection, not total injective.

Definition 1.38. Let $N , N ^ { \prime }$ be differentiable manifolds, $N ^ { \prime } \subset N$ . If the inclusion map $i : N ^ { \prime } \to N$ is an immersion, then $N ^ { \prime }$ is said to be an immersed submanifold of $N$ .

Remark 1.39. Suppose $f$ is an immersion and injective (such $f$ would henceforth be called injective immersion), $M$ is a smooth atlas ${ \mathcal { A } } = \{ ( U _ { \alpha } , \varphi _ { \alpha } ) \}$ . Denote $f A =$ $\{ ( f ( U _ { \alpha } ) , \varphi _ { \alpha } \circ f ^ { - 1 } ) \}$ . Then, it is easy to prove that $\{ f ( M ) , f { \mathcal { A } } \}$ is a differentiable manifold. Since $f$ has a local expression $\widehat { f } = \varphi _ { \alpha } \circ f ^ { - 1 } \circ f \circ \varphi _ { \alpha } ^ { - 1 } = I : \varphi _ { \alpha } ( U _ { \alpha } ) \to$ $\varphi _ { \alpha } ( U _ { \alpha } )$ , $f : M \to f ( M )$ is a diffeomorphism, i.e., $f _ { * p } : T _ { p } M \to T _ { f ( p ) } f ( M )$ is an isomorphism. Since $f$ is an immersion, the inclusion map $i : f ( M ) \to N$ is also an immersion. Hence, $f ( M )$ is an immersed submanifold of $N$ .

From the following example, we can see that the manifold topology of an immersed submanifold may be inconsistent with its subspace topology and can be very complex.

Example 1.40. $T ^ { 2 } = S ^ { 1 } \times S ^ { 1 } = \{ ( z _ { 1 } , z _ { 2 } ) \in \mathbf { C } \times \mathbf { C } | | z _ { 1 } | = | z _ { 2 } | = 1 \}$ . Define $f : \mathbf { R }  T ^ { 2 }$ , s.t. $f ( t ) = ( { \mathrm { e } } ^ { 2 \pi i t } , \ { \mathrm { e } } ^ { 2 \pi i \alpha } )$ , where $\alpha$ is an irrational number. We can prove that $f ( \mathbf { R } )$ , which is a differentiable manifold derived from $f$ , is an immersed submanifold of $T ^ { 2 }$ , and $f ( \mathbf { R } )$ is dense in $T ^ { 2 }$ .

We may regard $T ^ { 2 }$ as a unit square on the plane of $\mathbf { R } ^ { 2 }$ , which is also a 2D manifold that has equal length on opposite sides. It can be represented by a pair of ordered real numbers $( x , y )$ , where $x , y$ are mod $\mathbb { Z }$ real numbers. Define

$$
\varphi : { \bf R } ^ { 2 } \longrightarrow S ^ { 1 } \times S ^ { 2 } , \quad \varphi ( u ^ { 1 } , u ^ { 2 } ) = ( { \bf e } ^ { 2 \pi i u ^ { 1 } } , { \bf e } ^ { 2 \pi i u ^ { 2 } } )
$$

and define “ $\sim " : ( u ^ { 1 } , u ^ { 2 } ) \sim ( v ^ { 1 } , v ^ { 2 } ) \Leftrightarrow u ^ { 1 } = v ^ { 1 } ( \mathrm { m o d } \mathbb { Z } )$ , $u ^ { 2 } = v ^ { 2 } ( { \mathrm { m o d } } \mathbb { Z } )$ , and let $W = \left( u _ { 0 } ^ { 1 } - { \frac { 1 } { 2 } } , u _ { 0 } ^ { 1 } + { \frac { 1 } { 2 } } \right) \times \left( u _ { 0 } ^ { 2 } - { \frac { 1 } { 2 } } , u _ { 0 } ^ { 2 } + { \frac { 1 } { 2 } } \right)$ . Then, $( \varphi ( W ) , \varphi ^ { - 1 } )$ is a chart of $T ^ { 2 } = S ^ { 1 } \times S ^ { 1 }$ that contains $f ( t _ { 0 } )$ . Choose a neighborhood $U$ of $t _ { 0 } \in \mathbf { R }$ so that $f ( U ) \subset \varphi ( W )$ . Then, the local expression of $f$ , $\widehat { f } = ( t , \alpha t )$ is an immersion at $t _ { 0 }$ . It is easy to prove that if $\varphi ^ { - 1 } f ( \mathbf { R } )$ is dense in $\mathbf { R } ^ { 2 }$ , then $f ( \mathbf { R } )$ is dense in $T ^ { 2 } = S ^ { 1 } \times S ^ { 1 }$ . By definition, $f$ is injective. It is concluded that the topology of $T ^ { 2 }$ is different from the topology of $f ( U )$ , which derives from $f ( \mathbf { R } )$ .

# 3. Regular submanifolds

The type of submanifold given below has a special relationship to its parent differential manifold, which is similar to that of Euclidean space and its subspace.

Definition 1.41. Let $M ^ { \prime } \subset M$ have the subspace topology, and $k$ be some nonnegative integer, $0 \leq k \leq m$ . If there exists a chart $( U , \varphi )$ of $M$ that contains $p$ in every $p \in M ^ { \prime }$ , so that

Then $M ^ { \prime }$ is said to be a $k$ -dimensional regular submanifold of $M$ , and the chart is called submanifold chart.

Let $\mathcal { A } ^ { \prime } = \{ ( U _ { \alpha } , \varphi _ { \alpha } ) \}$ be a set that contains all submanifold charts on $M$ . Denote $\widetilde { \mathcal { A } } { = } \{ ( \widetilde { U } _ { \alpha } , \widetilde { \varphi } _ { \alpha } ) \}$ , where $\widetilde { U } _ { \alpha } = U _ { \alpha } \cap M ^ { \prime }$ , $\widetilde { \varphi } _ { \alpha } = \pi \circ ( \varphi _ { \alpha } | \widetilde { U } _ { \alpha } )$ , $\pi : \mathbf { R } ^ { k } \times \mathbf { R } ^ { m - k }  \mathbf { R } ^ { k }$ . Since $M ^ { \prime }$ "has the subspace topology, $\widetilde { U } _ { \alpha }$ "is an open set of $M ^ { \prime }$ , and $\widetilde { \varphi } _ { \alpha } : \widetilde { U } _ { \alpha } \to \widetilde { \varphi } _ { \alpha } ( \widetilde { U } _ { \alpha } )$ is a homeomorphism for $\widetilde { U } _ { \alpha }$ to $\widetilde { \varphi } _ { \alpha } ( \widetilde { U } _ { \alpha } ) \subset \mathbf { R } ^ { k }$ . Moreover, $U _ { \alpha } \bigcup U _ { \alpha } = M ^ { \prime }$ ", and hence $\widetilde { A }$ is an atlas of $M ^ { \prime } . \forall ( \widetilde { U } _ { \alpha } , \widetilde { \varphi } _ { \alpha } ) , ( \widetilde { U } _ { \beta } , \widetilde { \varphi } _ { \beta } ) \in \widetilde { \mathcal { A } }$ and $\widetilde { U } _ { \alpha } \cap \widetilde { U } _ { \beta } \neq \emptyset$ , we have

$$
\widetilde { \varphi _ { \beta } } \circ \widetilde { \varphi } _ { \alpha } ^ { - 1 } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { k } ) = \pi \circ \varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { k } , 0 , \cdot \cdot \cdot , 0 ) .
$$

Obviously, $\widetilde { A }$ is a smooth atlas of $M ^ { \prime }$ , which determines a differentiable structure of $M ^ { \prime }$ . Thus, $M ^ { \prime }$ is a $k$ -dimensional differentiable manifold.

Below is an example of regular submanifold.

Example 1.42. Let $M$ , $N$ be $m$ - and $n$ -dimensional differentiable manifolds respectively, and $f : M \to N$ be a smooth mapping. Then, the graph of $f$

$$
\mathsf { g } r ( f ) = \{ ( p , f ( p ) ) \in M \times N | p \in M \}
$$

is an $m$ -dimensional closed submanifold of $M \times N$ ( closed regular submanifold ).

Proof. Consider charts $( U , \varphi )$ , ( $\begin{array} { r } { V , \psi ) , p _ { 0 } \in U , f ( p _ { 0 } ) \in V , \varphi ( p _ { 0 } ) = O \in \mathbf { R } ^ { m } . } \end{array}$ , $\psi ( f ( p _ { 0 } ) ) = O ^ { \prime } \in \mathbf { R } ^ { n }$ , $f ( U ) ~ \subset ~ V$ , and define $G : \varphi ( U ) \times \psi ( V ) \to { \bf R } ^ { n + m } =$ $\mathbf { R } ^ { m } \times \mathbf { R } ^ { n }$ , so that

$$
G ( u , v ) = ( u , v - { \widehat f } ( u ) ) .
$$

It is easy to prove that $G ( g r ( \widehat { f } ) ) = \{ ( u , O ^ { \prime } ) \mid u \in \varphi ( U ) \}$ , and the rank of

$$
J _ { G } ( O , O ^ { \prime } ) = \left( \begin{array} { c c } { { I _ { m } } } & { { O } } \\ { { - D \widehat { f } ( O ) } } & { { I _ { n } } } \end{array} \right)
$$

is $n + m$ . Since $G ( O , O ^ { \prime } ) = ( O , O ^ { \prime } )$ , $G$ homeomorphically maps some neighborhood $\widetilde { U }$ of $( O , O ^ { \prime } )$ on $\varphi ( U ) \times \psi ( V )$ to some neighborhood $\widetilde { V }$ of $( O , O ^ { \prime } )$ on $\mathbf { R } ^ { n + m }$ . Denote

$$
W = ( \varphi \times \psi ) ^ { - 1 } ( \widetilde { U } ) , \quad \chi = G \circ ( \varphi \times \psi ) | W .
$$

Then, $( W , \chi )$ is a chart of $M \times N$ that contains $( p _ { 0 } , f ( p _ { 0 } ) )$ , and

$$
\begin{array} { l } { { \chi ( p _ { 0 } , f ( p _ { 0 } ) ) = ( O , O ^ { \prime } ) \in { \bf R } ^ { n + m } , } } \\ { { \chi ( W \cap g r ( f ) ) = \{ ( u , v ) \in \chi ( W ) | v = 0 \} . } } \end{array}
$$

The proof can be obtained.

Remark 1.43. If $N ^ { \prime }$ is a regular submanifold $N$ , $f : M \to N$ is a smooth mapping, $f ( M ) \subset N ^ { \prime }$ , then $f : { \cal M } \ :  \ : { \cal N } ^ { \prime }$ is also a smooth mapping. Let $( U , \varphi ) , ( V , \psi )$ be charts of $N$ , then $( \widetilde { V } , \widetilde { \psi } )$ is a induced chart of $N ^ { \prime }$ from $N$ . Then, by the fact that $N ^ { \prime }$ is a regular submanifold of $N$ , we know $\psi \circ f \circ \varphi ^ { - 1 } ( u ) = ( \widetilde { \psi } \circ f \circ \varphi ^ { - 1 } ( u ) , 0 )$ . Then, the smoothness of $f : M \to N$ leads to the smoothness of $f : M \to N ^ { \prime }$ .

Remark 1.44. Let $M ^ { \prime }$ be a $k$ -dimensional regular submanifold of $M$ , then $i : M ^ { \prime } \to$ $M$ is the inclusion mapping. Take a submanifold chart $( U , \varphi )$ of $M$ that induces the chart $( \widetilde { U } , \widetilde { \varphi } )$ of $M ^ { \prime }$ . Then, $\hat { i } = \varphi \circ i \circ \widetilde { \varphi } ^ { - 1 } : \widetilde { \varphi } ( \widetilde { U } ) \to \varphi ( U )$ has the form

$$
\widehat i ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { k } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { k } , 0 , \cdot \cdot \cdot , 0 ) .
$$

Thus, $i _ { * p } : T _ { p } M ^ { \prime } \to T _ { p } M$ is injective, which means that the regular submanifold is definitely an immersed submanifold.

# 4. Embedded submanifolds

Definition 1.45. Let $f : M \to N$ be an injective immersion. If $f : M \to f ( M )$ is a homeomorphism, where $f ( M )$ has the subspace topology of $N$ , then $f ( M )$ is an embedded submanifold of $N$ .

Proposition 1.46. Suppose $f : M \to N$ is an embedding, then $f ( M )$ is a regular submanifold of $N$ , and $f : M \to f ( M )$ is a diffeomorphism.

Proof. Since $f$ is an embedding, $f$ is an immersion , $\forall q \in f ( M ) , \exists p \in M$ so that $f ( p ) = q$ . Let charts $( U , \varphi ) , ( V , \psi ) , p \in U , f ( p ) \in V { \mathrm { s o } }$ that $\varphi ( p ) = { \cal O } \in { \bf R } ^ { m } , \psi ( q ) =$ $O ^ { \prime } \in { \mathbf { R } } ^ { n } , f ( U ) \subset V$ , and $\widehat { f } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } , \cdot \cdot \cdot , 0 )$ . Since $f : M \to$ $f ( M )$ is a homeomorphism, if $U$ is an open subset of $M$ , then $f ( U )$ is an open subset of $f ( M )$ , and there exists an open subset $W _ { 1 } \subset N$ so that $f ( U ) = W _ { 1 } \cap f ( M )$ . Denote $W = V \cap W _ { 1 }$ , $\chi = \psi | W$ . Then, $\chi ( q ) = O ^ { \prime } \in \mathbf { R } ^ { n }$ , and

$$
\chi ( W \cap f ( M ) ) = \{ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } ) \in \chi ( W ) \mid u ^ { m + 1 } = \cdot \cdot \cdot = u ^ { n } = 0 \} ,
$$

i.e., $( W , \chi )$ is a submanifold chart of $N$ that contains $q$ , which also means that $f ( M )$ is a regular submanifold of $N$ . Let $( \widetilde W , \widetilde \chi )$ be a chart of $f ( M )$ induced from $( W , \chi )$ . Then from $\chi \circ f \circ \varphi ^ { - 1 } ( u ) = ( \widetilde { \chi } \circ f \circ \varphi ^ { - 1 } ( u ) , 0 )$ , we conclude that $f : M \to f ( M )$ is a diffeomorphism.

Remark 1.47. If $f$ is an immersion, then we can appropriately choose the charts of $M , N$ , such that $f$ has the local expression $\widehat { f } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } , \cdot \cdot \cdot , 0 )$ . Therefore, it is easy to see that $f$ can be an injective immersion in the neighborhood $U$ of $p$ , and $f : U \to f ( U )$ is a homeomorphism. Obviously, $f ( U )$ has the induced subspace topology from $N$ . Therefore, $f \mid U : U \to N$ is an embedding.

Definition 1.48. Let $X$ , $Y$ be two topological spaces, and $f : X \to Y$ be continuous. If for every compact subset $K$ in $Y$ , we have $f ^ { - 1 } ( K )$ to be a compact subset in $X$ , then $f$ is said to be a proper mapping.

Proposition 1.49. Let $f : M \to N$ be an injective immersion. If $f$ is a proper mapping, then $f$ is an embedding.

Proof. It would be sufficient to prove $f ^ { - 1 } : f ( M ) \to M$ is continuous. Assume there exist an open set $W$ of $M$ and a sequence of points $\left\{ q _ { i } \right\}$ of $f ( M )$ s.t. $q _ { i } \notin f ( W )$ ,but $\left\{ q _ { i } \right\}$ converges to some point $q _ { i }$ of $f ( W )$ . Denote $p _ { i } = f ^ { - 1 } ( q _ { i } )$ , $p _ { 0 } = f ^ { - 1 } ( q _ { 0 } )$ , $p _ { 0 } \in$ $W$ . Since $\{ q _ { 0 } , q _ { i } \} ( i = 1 , 2 , \cdot \cdot \cdot )$ is compact, and $f$ is a proper mapping, $\{ p _ { 0 } , p _ { i } \} ( i =$ $1 , 2 , \cdot \cdot \cdot )$ is a compact set of $M$ . Let $p _ { 1 } ~ \in ~ M$ be the convergence of $\{ p _ { i } \}$ . Since $f$ is continuous, $\{ f ( p _ { i } ) \}$ converges to $f ( p _ { 1 } )$ , i.e., $f ( p _ { 1 } ) = f ( p _ { 0 } )$ . Thus, $p _ { 0 } ~ = ~ p _ { 1 }$ . Therefore, when $i$ is large enough, there exists $p _ { i } \in W$ , and $q _ { i } = f ( p _ { i } ) \in f ( W )$ . This is in contradiction with $q _ { i } \not \in f ( W )$ . -

Remark 1.50. Let $f$ be an injective immersion. If $M$ is compact, then $f$ is a proper mapping. By Proposition 1.49, $f$ is an embedding.

# 1.1.4 Submersion and Transversal

Below we will discuss the local property of $f$ when $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is surjective.

Definition 1.51. $f$ is smooth, $p \in M$ . If $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is surjective, then $f$ is a submersion at $p$ ; if $f$ is a submersion at every $p \in M$ , then $f$ is said be a submersion.

Similar to the proposition for $f$ that immerses at $p$ , we have the following proposition.

Proposition 1.52. Given a smooth $f$ and $p \in M$ , if $f$ submerses at $p$ , then there exists chart $( U , \varphi )$ on $M$ about $p$ and $( V , \psi )$ on $N$ about $f ( p ) \in N$ in which ${ \widehat { f } } =$ $\psi \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \psi ( V )$ has the form

$$
\widehat { f } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } ) .
$$

Proof. Take charts $( U _ { 1 } , \varphi _ { 1 } ) , ( V , \psi _ { 1 } ) , p \in U _ { 1 } , f ( p ) \in V , \varphi _ { 1 } ( p ) = O \in \mathbf { R } ^ { m }$ , $\psi _ { 1 } ( f ( p ) )$ $\mathbf { \Phi } = O ^ { \prime } \in \mathbf { R } ^ { n }$ and $f ( U _ { 1 } ) \subset V$ . Since $f$ is a submersion, $J _ { \widehat { f } } ( O ) = \Big ( \frac { \partial \widehat { f } _ { i } } { \partial u ^ { j } } \Big ) \Big | _ { O }$ has rank $n$ , where ${ \widehat { f } } = ( { \widehat { f } } _ { 1 } , \cdots , { \widehat { f } } _ { n } )$ . We assume that the first $n$ rows of $J _ { \hat { f } } ( O )$ are linearly independent. Let $g : \varphi _ { 1 } ( U _ { 1 } ) \to \psi ( V ) \times \mathbf { R } ^ { m - n }$ satisfy

$$
g ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( \widehat { f } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) , u ^ { n + 1 } , \cdot \cdot \cdot , u ^ { m } ) .
$$

Then, $g ( O ) = O$ , and $J _ { g } ( O ) = \left[ \begin{array} { c } { { J _ { \widehat { f } } ( O ) } } \\ { { O } } \end{array} \right]$ has rank $n$ . By the inverse function theorem, $g ( O )$ maps a neighborhood $W$ at $O$ diffeomorphically to a neighborhood of $g ( W ) \subset \psi ( V ) \times \mathbf { R } ^ { m - n }$ . Let $U = W \cap U _ { 1 }$ , $\varphi = g \circ ( \varphi _ { 1 } | U )$ , then $\psi \circ f \circ \varphi _ { 1 } ^ { - 1 } \circ g ^ { - 1 } =$ $\beta \circ g \circ g ^ { - 1 } = \beta$ , and $\beta : \mathbf { R } ^ { m }  \mathbf { R } ^ { n }$ , $\beta ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } )$ is a projection from $\mathbf { R } ^ { m } \to \mathbf { R } ^ { n }$ . $\blacktriangle$

Remark 1.53. By Definition 1.51, if $f : M \to N$ is a submersion at $p \in M$ , then $f$ is a submersion in some neighborhood of $p$ .

Remark 1.54. If $f : M \to N$ is a submersion, then $f$ is an open mapping (i.e., open set mapping to an open set). Furthermore, $f ( M )$ is an open subset of $N$ .

Let $G$ be an open subset of $M , \forall q \in f ( G )$ . There exists a $p \in G$ , s.t. $f ( p ) = q$ . Since $f$ is a submersion, there exist charts $( U , \varphi ) , ( V , \psi ) , p \in U , q \in V$ , s.t. $U \subset G$ , and ${ \widehat { f } } : \varphi ( U ) \to \psi ( V ) , { \widehat { f } } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } )$ . Let $H = \beta ( \varphi ( U ) )$ , where $\beta ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } )$ , s.t. $H \subset \psi ( V )$ . Thus, $\psi ^ { - 1 } ( H )$ is a neighborhood of $q \in N$ , $\psi ^ { - 1 } ( H ) \subset f ( G )$ , i.e., $f ( G )$ is an open subset of $N$ .

Next, we consider under what condition would $f ^ { - 1 } ( q _ { 0 } )$ be a regular submanifold of $M$ , and $\forall q _ { 0 } \in N$ be fixed.

Definition 1.55. Given $f : M \to N$ is smooth, $p \in M$ , if $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is surjective, then $p$ is said to be a regular point of $f$ (i.e., $f$ submerses at $p$ ), otherwise $p$ is said to be a critical point of $f$ , and $q \in N$ is called a regular value of $f$ , if $q \not \in f ( M )$ or $q \in f ( M )$ , but each $p \in f ^ { - 1 } ( q )$ is a regular point of $f$ ; otherwise, $q$ is called a critical value of $f$ .

Remark 1.56. When $\dim M \ < \ \dim N$ , as a result of $\mathrm { d i m } T _ { p } M \ = \ \mathrm { d i m } M <$ $\dim N \ : = \ : \dim T _ { f ( p ) } N$ , for $q \in f ( M ) , p \in f ^ { - 1 } ( q ) , p$ cannot be a regular point of $f$ . Hence, $q \in N$ is a regular value of $f \Leftrightarrow q \not \in f ( M )$ .

Theorem 1.57. Let $f : { \cal { M } }  { \cal { N } }$ be smooth, $q \in N$ ; if $q$ is a regular value of $f$ , and $f ^ { - 1 } ( q ) \neq 0$ , then $f ^ { - 1 } ( q )$ is an $( m - n )$ -dimensional regular submanifold of $M$ . Moreover, $\forall p \in f ^ { - 1 } ( q )$ ,

$$
T _ { p } \{ f ^ { - 1 } ( q ) \} = \ker f _ { * p } .
$$

Proof. Since $q$ is a regular value, $\forall p \in f ^ { - 1 } ( q )$ , $f$ submerses at $p$ by definition. By the Proposition 1.52, there exist charts $( U , \varphi ) , ( V , \psi ) , p \in U , f ( p ) = q \in V , \varphi ( p _ { 0 } ) =$ $O \in { \bf R } ^ { m } , \psi ( q ) = O ^ { \prime } \in { \bf R } ^ { n }$ , and ψ ◦ f ◦ ϕ−1(u1, · · · , um) = f (u1, · · · , um) = (u $^ { \downarrow , \cdot \cdot , u ^ { n } ) , \varphi \{ U \cap f ^ { - 1 } ( q ) \} } = \{ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) \in \varphi ( U ) \mid u ^ { 1 } = \cdot \cdot \cdot = u ^ { n } = 0 \}$ , i.e., $( U , \varphi )$ is a submanifold chart of $M$ that contains $p$ . Therefore, $f ^ { - 1 } ( q )$ is a regular submanifold of $M$ , and $\dim f ^ { - 1 } ( q ) = m - n$ .

Note that $f | _ { f ^ { - 1 } ( q ) } : f ^ { - 1 } ( q ) \to M , f | _ { f ^ { - 1 } ( q ) } = f \circ i , i : f ^ { - 1 } ( q ) \to M$ is an inclusion mapping. Since $f | _ { f ^ { - 1 } ( q ) } = q$ is a constant mapping, $f _ { \ast p } \circ i _ { \ast p } = ( f | _ { f ^ { - 1 } ( q ) } ) _ { \ast p } = 0$ , i.e., $i _ { * p } ( T _ { p } \{ f ^ { - 1 } ( q ) \} ) \subset \mathrm { ~ k e r } f _ { * p }$ . Furthermore, because $q$ is a regular value of $f$ , $f _ { * p } ( T _ { p } M ) = T _ { q } N$ , and $\dim \ker f _ { * p } = \dim T _ { p } M - \dim f _ { * p } ( T _ { p } M ) = m - n \ =$ $\dim f ^ { - 1 } ( q )$ . Therefore, we have $T _ { p } \{ f ^ { - 1 } ( q ) \} = \ker f _ { \ast p }$ . -

Remark 1.58. Given $f : M \to N$ is smooth, $\mathrm { d i m } { \cal M } = \mathrm { d i m } { \cal N } , { \cal M }$ is compact. If $q \in N$ is a regular value of $f$ , then $f ^ { - 1 } ( q ) = \emptyset$ or $f ^ { - 1 } ( q )$ consists of finite points.

By Theorem 1.57, if $f ^ { - 1 } ( q ) \neq 0$ , then $f ^ { - 1 } ( q )$ is a 0-dimensional regular submanifold of $M$ . By definition, we have $\varphi ( U \cap f ^ { - 1 } ( q ) ) = O \in \mathbf { R } ^ { m }$ , i.e., every point in $f ^ { - 1 } ( q )$ is an isolated point. Moreover due to the compactness of $f ^ { - 1 } ( q ) , f ^ { - 1 } ( q )$ must consist of finite points.

Below, we give some applications of Theorem 1.57.

Example 1.59. Let $f : \mathbf { R } ^ { n + 1 }  \mathbf { R }$ , and $f ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) = \sum _ { i = 1 } ^ { n + 1 } ( u ^ { i } ) ^ { 2 } .$

From the Jacobian matrix of $f$ at $( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } )$ , we know $f$ is not a submersion at $( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) \Leftrightarrow u ^ { 1 } = \cdot \cdot \cdot = u ^ { n + 1 } = 0$ . Therefore, any non-zero real number is a regular value of $f$ . According to the Theorem 1.57, the $n$ -dimensional unit sphere $S ^ { n } = f ^ { - 1 } ( 1 )$ is an $n$ -dimensional regular submanifold on $\mathbf { R } ^ { n + 1 }$ .

Example 1.60. Let $f : { \bf R } ^ { 3 }  { \bf R }$ , and $f ( u ^ { 1 } , u ^ { 2 } , u ^ { 3 } ) = ( a - \sqrt { ( u ^ { 1 } ) ^ { 2 } + ( u ^ { 2 } ) ^ { 2 } } ) ^ { 2 } +$ $( u ^ { 3 } ) ^ { 2 } , a > 0$ .

The assumption tells us that any non-zero real number is a regular point of $f$ . Then, $0 < b ^ { 2 } < a ^ { 2 }$ is a regular value of $f$ . Therefore, by Theorem 1.57, $T ^ { 2 } = f ^ { - 1 } ( b ^ { 2 } )$ is a 2-dimensional regular submanifold on $\mathbf { R } ^ { 2 }$ .

If $M ^ { \prime }$ is a regular submanifold of $M$ , then $\mathrm { d i m } { \cal M } - \mathrm { d i m } { \cal M ^ { \prime } } = \mathrm { c o d i m } { \cal M ^ { \prime } }$ is called the $M$ -codimension of $M ^ { \prime }$ . Denote $M ^ { \prime } = \{ p \in M \mid f _ { i } ( p ) = 0 ( i = 1 , \cdot \cdot \cdot , k ) \}$ and consider the mapping

$$
{ \cal F } : { \cal M } \longrightarrow { \bf R } ^ { k } , \quad { \cal F } ( p ) = ( f _ { 1 } ( p ) , \cdots , f _ { k } ( p ) ) .
$$

If $f _ { i } : M \to \mathbf { R }$ is smooth, then $F$ is smooth too, and $M ^ { \prime } = F ^ { - 1 } ( O )$

Proposition 1.61. Suppose $M ^ { \prime }$ is a subset of $M$ . Then, $M ^ { \prime }$ is a $k$ -codimensional regular submanifold of $M$ if and only if for all $q \in M ^ { \prime }$ , there exists a neighborhood $U$ of $q \in M$ and a smooth mapping $F : U \to \mathbf { R } ^ { k }$ , s.t.

$1 ^ { \circ }$ $U \cap M ^ { \prime } = F ^ { - 1 } ( O )$ .   
$2 ^ { \circ }$ $F : U \to \mathbf { R } ^ { k }$ is a submersion.

Proof. Necessity. By the definition of the regular submanifold, if $M ^ { \prime }$ is a $k$ -codimensional regular submanifold of $M$ , then $\forall p \in M ^ { \prime }$ , there exists a submanifold chart $( U , \varphi )$ of $M$ that contains $p$ s.t. $\varphi ( p ) = O \in \mathbf { R } ^ { m }$ , and $\varphi ( U \cap M ^ { \prime } ) = \{ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) \in$ $\varphi ( U ) \mid u ^ { m - k + 1 } = \cdots = u ^ { m } = 0 \}$ . Let us denotes the projection by $\boldsymbol { \pi } : \mathbf { R } ^ { m } =$ $\mathbf { R } ^ { m - k } \times \mathbf { R } ^ { k }  \mathbf { R } ^ { k }$ , let $F = \pi \circ \varphi : U \to \mathbf { R } ^ { k }$ . Then, $F$ is smooth, and $F ^ { - 1 } ( O ) =$ $( \pi \circ \varphi ) ^ { - 1 } ( O ) = U \cap M ^ { \prime } , F _ { * q } = \pi _ { * \varphi ( q ) } \circ \varphi _ { * q }$ . Since $\varphi _ { * q }$ is an isomorphism and $\pi _ { * \varphi ( q ) }$ is surjective, $F$ submerses at $q$ .

Sufficiency. If $\forall q \in U \cap M ^ { \prime } , F$ submerses at $q$ , then $O \in \mathbf { R } ^ { k }$ is a regular value of $F$ . By Theorem 1.57, $F ^ { - 1 } ( O )$ is a $k$ -codimensional regular submanifold of $U$ , i.e., $M ^ { \prime }$ is a $k$ -codimensional regular submanifold of $M$ .

We know that if $q \in N$ is a regular value of $f : M \to N$ , and $f ^ { - 1 } ( q ) \neq 0$ , then $f ^ { - 1 } ( q )$ is a regular submanifold of $M$ . Assume that $Z$ is a regular submanifold of $N$ . Then, under what condition would $f ^ { - 1 } ( Z )$ be a regular submanifold of $M ?$ For this question, we have the following definition.

Definition 1.62. Suppose $Z$ is a regular submanifold of $N$ , $f : M \to N$ is smooth, $p \in M$ . Then, we say $f$ is transversal to $Z$ at $p$ , if $f ( p ) \notin Z$ or when $f ( p ) \in Z$ has

$$
f _ { * p } T _ { p } M + T _ { f ( p ) } Z = T _ { f ( p ) } N ,
$$

denoted by $f \top _ { p } Z$ . If $\forall p \in M , f \top _ { p } Z$ , then $f$ is transversal to $Z$ , denoted by $f \top Z$ .

Remark 1.63. If $\dim M + \dim Z < \dim N$ , then $f ^ { \top } Z \Leftrightarrow f ( M ) \cap Z = \emptyset$ ; if $q \in N$ is a regular value of $f$ , then $\forall p \in f ^ { - 1 } ( q )$ , $f \top _ { p } Z$ ; if $f : M \to N$ is a submersion, then for any regular submanifold $Z$ of $N$ , $f \top Z$ .

For transversality, we focus on its geometric property.

Example 1.64. $M = \mathbf { R }$ , $N = { \bf R } ^ { 2 } , Z$ is $x$ -axis in $\mathbf { R } ^ { 2 }$ , $f : M \to N$ , $f ( t ) = ( t , t ^ { 2 } )$

When $t \neq 0$ , as a result of ${ f ( t ) \not \in Z , f \top } _ { t } Z$ ;

When $t = 0$ , $J _ { f } ( 0 ) = ( 1 , 0 ) ^ { \prime }$ , note that $f _ { * 0 } \left( \left. \frac { \mathrm { d } } { \mathrm { d } t } \right| _ { 0 } \right) = ( 1 , 0 ) \left( \frac { \partial } { \partial u ^ { 1 } } , \frac { \partial } { \partial u ^ { 2 } } \right) ^ { \prime } = \frac { \mathrm { d } } { \mathrm { d } u ^ { 1 } } ,$ $f _ { * 0 } T _ { 0 } M = T _ { ( 0 , 0 ) } Z .$ Therefore, $f _ { * 0 } T _ { 0 } M + T _ { ( 0 , 0 ) } Z = T _ { ( 0 , 0 ) } N$ is impossible to establish. Thus, $f$ is not transversal to $Z$ at 0.

However, if we change $f$ to $f ( t ) = ( t , t ^ { 2 } - 1 )$ , we obtain: when $t \neq \pm 1 , f ( t ) \notin$ Z, so f tZ; when t = 1, Jf (1) = (1, 2) , therefore f∗1  d t  $f _ { * 1 } \Big ( \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { 1 } \Big ) = \left. \frac { \partial } { \partial u ^ { 1 } } \right| _ { ( 1 , 0 ) } +$ 2 ∂u2  (1,0) , i.e., $f _ { * 1 } T _ { 1 } M + T _ { ( 1 , 0 ) } Z = T _ { ( 1 , 0 ) } N$ , and hence $f \top _ { 1 } Z$ . Similarly, we have $f \top _ { - 1 } Z$ . Thus, $f \top Z$ .

Submanifold transverse: Let $Z , Z ^ { \prime }$ be two regular submanifolds of $N , i : Z ^ { \prime } \to N$ is an inclusion mapping. If $i \top Z$ , then submanifold $Z ^ { \prime }$ is transversal to $Z$ , denoted as $Z ^ { \prime } \top Z$ . If $Z ^ { \prime } { \top } Z , \forall p \in Z \cap Z ^ { \prime }$ , by definition, we have

$$
i _ { * p } ( T _ { p } Z ^ { \prime } ) + T _ { p } Z = T _ { p } N ,
$$

i.e.,

$$
\begin{array} { r } { T _ { p } Z ^ { \prime } + T _ { p } Z = T _ { p } N . } \end{array}
$$

We assume that $f : { \cal M }  N$ is smooth, and $Z$ is a $k$ -codimensional regular submanifold of $N$ $, p \in M , f ( p ) = q \in Z$ . According to the Proposition 1.61, there exists a submanifold chart $( V , \psi )$ of $N$ that contains $q$ , s.t. $\pi \circ \psi : V \to \mathbf { R } ^ { k }$ is a submersion, and $Z \cap V = ( \pi \circ \psi ) ^ { - 1 } ( O )$ . Now, take a neighborhood of $p$ in $M$ , s.t., $f ( U ) \subset V$ , then $\pi \circ \psi \circ f : U \to \mathbf { R } ^ { k }$ .

Proposition 1.65. $f \top _ { p } Z \Leftrightarrow \pi \circ \psi \circ f : U  \mathbf { R } ^ { k }$ submerses at $p$

Proof. Since $\pi \circ \psi$ submerses at $f ( \boldsymbol p )$ , $O \in \mathbf { R } ^ { k }$ is a regular value of $\pi \circ \psi$ . From $Z \cap V = ( \pi \circ \psi ) ^ { - 1 } ( O )$ , we know for every $q \in Z \cap V$ , there exists a $( \pi \circ \psi ) _ { * q } T _ { q } N =$ $T _ { o } { \bf R } ^ { k }$ . By Theorem 1.57, $\ker ( \pi \circ \psi ) _ { * q } = T _ { q } Z .$ Therefore, $f _ { * p } T _ { p } M + T _ { q } Z = T _ { q } N $ $( \pi \circ \psi ) _ { * q } ( f _ { * p } T _ { p } M ) = T _ { o } { \bf R } ^ { k }  ( \pi \circ \bar { \psi } \circ f ) _ { * p } ( T _ { p } M ) = T _ { o } { \bf R } ^ { \bar { k } }$ , i.e., $\pi \circ \psi \circ f$ submerses at $p$ .

Remark 1.66. Extending from the conclusion of Proposition 1.65, we have $f \top Z $ $O \in \mathbf { R } ^ { k }$ are regular values of $\pi \circ \psi \circ f : U \to \mathbf { R } ^ { k }$ .

Remark 1.67. Since $f \top _ { p } Z$ , i.e., $\pi \circ \psi \circ f : U \to \mathbf { R } ^ { k }$ submerses at $p$ . By Proposition 1.52, we can choose a coordinate chart s.t. $\pi \circ \psi \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \mathbf { R } ^ { k }$ has the form

$$
( \pi \circ \psi \circ f \circ \varphi ^ { - 1 } ) ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) = ( u ^ { m - k + 1 } , \cdot \cdot \cdot , u ^ { m } ) .
$$

Then, $\widehat { f } = \psi \circ f \circ \varphi ^ { - 1 }$ can be represented by

$$
\widehat { f } = ( \eta _ { 1 } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) , \cdot \cdot \cdot , \eta _ { n - k } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) , u ^ { m - k + 1 } , \cdot \cdot \cdot , u ^ { m } ) .
$$

Theorem 1.68 (Extension of Theorem 1.57). Suppose $f : M \to N$ is smooth, $Z$ is a $k$ -codimensional regular submanifold of $N$ . If $f \top Z$ and $f ^ { - 1 } ( Z ) \neq \emptyset$ , then $f ^ { - 1 } ( Z )$ is a $k$ -codimensional regular submanifold of $M$ , and $\forall p \in f ^ { - 1 } ( Z )$ ,

$$
T _ { p } \{ f ^ { - 1 } ( Z ) \} = f _ { \ast p } ^ { - 1 } \{ T _ { f ( p ) } Z \} .
$$

Proof. $\forall p \in f ^ { - 1 } ( Z )$ , there exists $q \in Z$ , denoted by $q \ = \ f ( p )$ . Since $Z$ is a $k$ - codimensional regular submanifold of $N$ , there exists a submanifold chart $( V , \psi )$ of $N$ that contains $p$ . Let $U = f ^ { - 1 } ( V )$ . From $f \top Z$ , we know that $O \in \mathbf { R } ^ { k }$ is a regular value of $\pi \circ \psi \circ f$ , and

$$
U \cap f ^ { - 1 } ( Z ) = ( \pi \circ \psi \circ f ) ^ { - 1 } ( O ) .
$$

By Theorem 1.57, $U \cap f ^ { - 1 } ( Z )$ is a $k$ -codimensional regular submanifold of $U$ , and

$$
\begin{array} { r l } { T _ { p } \{ f ^ { - 1 } ( Z ) \} } & { = \ker ( \pi \circ \psi \circ f ) _ { \ast p } } \\ & { = f _ { \ast p } ^ { - 1 } \{ ( \pi \circ \psi ) _ { \ast q } ^ { - 1 } ( O ) \} } \\ & { = f _ { \ast p } ^ { - 1 } \{ T _ { f ( p ) } Z \} . } \end{array}
$$

The theorem is proved.

# 1.2 Tangent Bundle

The tangent bundle of a differentiable manifold $M$ is the disjoint union of the tangent spaces of $M$ . It is useful, in distinguishing between the tangent space and bundle, to consider their dimensions, $n$ and $2 n$ respectively. In other words, the tangent bundle accounts for dimensions in the positions in the manifold as well as directions tangent to it. Since we can define a projection map, for each element of the tangent bundle giving the element in the manifold whose tangent space the first element lies in, tangent bundles are also fiber bundles.

# 1.2.1 Tangent Bundle and Orientation

In this section, we will discuss two invariable properties under diffeomorphism– tangent bundle and orientation.

# 1. Tangent Bundle

Definition 2.1. The Triple $( T M , M , \pi )$ is called tangent bundle of differentiable manifold $M$ (sometimes simply called $T M$ ), where $T M = \bigcup _ { p \in M } T _ { p } M$ , projection map

$\pi : T M  M$ satisfies $\pi ( X _ { p } ) = p$ , $\forall X _ { p } \in T M$ . For every $p \in M , \pi ^ { - 1 } ( p ) = T _ { p } M$ is called fiber at $p$ of tangent bundle $^ { T M }$ .

Proposition 2.2. Let $M$ be an $m$ -dimensional differentiable manifold, then T M is a $2 m$ -dimensional differentiable manifold, and $\pi : T M  M$ is a submersion.

Proof. Let $( U , \varphi )$ be a chart on $M$ , and its coordinate function be $x ^ { 1 } , \cdots , x ^ { m }$ . Then, $\forall X _ { p } \in \pi ^ { - 1 } ( U )$ , $X _ { p } = \sum _ { i } a ^ { i } { \frac { \partial } { \partial x ^ { i } } } { \Big | } _ { \jmath }$ . Define $\varphi _ { U } : \pi ^ { - 1 } ( U ) \to \varphi ( U ) \times \mathbf { R } ^ { m }$ , s.t.

$$
\varphi _ { U } ( X _ { p } ) = ( \varphi ( p ) ; a ^ { 1 } , \cdot \cdot \cdot , a ^ { m } ) ,
$$

obviously $\varphi _ { U }$ is a 1 to 1 mapping.

Note that as $( U , \varphi )$ takes all the charts on $M$ , all the corresponding $\pi ^ { - 1 } ( U )$ constitutes a covering of $^ { T M }$ . Hence, if the topology of $\pi ^ { - 1 } ( U )$ is given, the subset of $\pi ^ { - 1 } ( U )$ is open, iff the image of $\varphi _ { U }$ is an open set of $\varphi ( U ) \times \mathbf { R } ^ { m }$ . It is easy to prove that by the 1 to 1 correspondence of $\varphi _ { U }$ , the topology of $\varphi _ { U }$ on the $\mathbf { R } ^ { m } \times \mathbf { R } ^ { m } = \mathbf { R } ^ { 2 m }$ subspaces can be lifted on $\pi ^ { - 1 } ( U )$ . The topology on $^ { T M }$ can be defined as follows: $W$ is called an open subset of $T M$ , iff $W \cap \pi ^ { - 1 } ( U )$ is an open subset of $\pi ^ { - 1 } ( U )$ . It is easy to deduce that $^ { T M }$ constitutes a topological space that satisfies the following conditions:

$1 ^ { \circ }$ $^ { T M }$ is a Hausdorff space that has countable bases. $2 ^ { \circ }$ $\pi ^ { - 1 } ( U )$ is an open subset of $^ { T M }$ , and $\varphi _ { U }$ is a homeomorphism from $\pi ^ { - 1 } ( U )$ to an open subset of R2m.

Furthermore, it can be proved that the manifold structure on $T M$ can be naturally induced from the manifold structure on $M$ . We say that $\{ ( \pi ^ { - 1 } ( U ) , \varphi _ { U } ) \} = \mathcal { A }$ is a smooth atlas of $^ { T M }$ . For any chart $( \pi ^ { - 1 } ( U ) , \varphi _ { U } )$ , there exists a $( \pi ^ { - 1 } ( V ) , \psi _ { V } ) \in$ $\mathcal { A }$ , and $\pi ^ { - 1 } ( U ) \cap \pi ^ { - 1 } ( V ) \neq \emptyset$ . Let $x ^ { 1 } , \cdots , x ^ { m }$ and $y ^ { 1 } , \cdots , y ^ { m }$ be the coordinate functions of the charts $( \dot { U } , \dot { \varphi } ) , ( V , \psi )$ . Then,

$$
{ \begin{array} { l l l } { \displaystyle \psi _ { V } \circ \varphi _ { U } ^ { - 1 } ( u ; a ^ { 1 } , \cdot \cdot \cdot , a ^ { m } ) } & { = } & { \displaystyle \psi _ { V } { \Biggl ( } \sum _ { i } a ^ { i } \left. { \frac { \partial } { \partial x ^ { i } } } \right| _ { \varphi ^ { - 1 } ( u ) } { \Biggr ) } } \\ & { = } & { \displaystyle \psi _ { V } { \Biggl ( } \sum _ { j } { \Biggl ( } \sum _ { i } a ^ { i } \left. { \frac { \partial y ^ { j } } { \partial x ^ { i } } } \right| _ { \varphi ^ { - 1 } ( u ) } { \Biggr ) } \left. { \frac { \partial } { \partial y ^ { j } } } \right| _ { \psi \circ \varphi ^ { - 1 } ( u ) } { \Biggr ) } } \\ & { = } & { \displaystyle { \Biggl ( } \psi \circ \varphi ^ { - 1 } ( u ) ; \sum _ { i } a ^ { i } \left. { \frac { \partial y ^ { 1 } } { \partial x ^ { i } } } \right| _ { \varphi ^ { - 1 } ( u ) } , \cdot \cdot \cdot , \sum _ { i } a ^ { i } \left. { \frac { \partial y ^ { m } } { \partial x ^ { i } } } \right| _ { \varphi ^ { - 1 } ( u ) } { \Biggr ) } } \end{array} }
$$

It is easy to conclude that $^ { T M }$ is a $2 m$ -dimensional manifold, $\mathcal { A }$ is a differentiable structure on $^ { T M }$ . From the charts $( U , \varphi )$ of $M$ and $( \pi ^ { - 1 } ( U ) , \varphi _ { U } )$ of $T M$ , we know $\widehat { \boldsymbol { \pi } } = \varphi \circ \boldsymbol { \pi } \circ \varphi _ { U } ^ { - 1 } : \varphi ( U ) \times \mathbf { R } ^ { m }  \varphi ( \overleftarrow { U } )$ has the form:

$$
\widehat { \pi } ( u ; a ^ { 1 } , \cdot \cdot \cdot , a ^ { m } ) = u .
$$

By the definition of submersion, $\pi$ is a submersion.

Given below are examples of two trivial tangent bundles (if there exists a diffeomorphism from its tangent bundle $T M$ to $M \times \mathbf { R } ^ { m }$ , and this diffeomorphism limited on each fiber of $T M \left( T _ { p } M \right)$ is a linear isomorphism from $T _ { p } M$ to $\{ p \} \times \mathbf { R } ^ { m } )$ ).

Example 2.3. Let $U$ be an open subset of $\mathbf { R } ^ { m }$ and $T U \simeq U \times \mathbf { R } ^ { m }$

$\forall \bar { X } _ { u } \in T U , X _ { u } = \sum _ { i } \bar { a ^ { i } } \frac { \partial } { \partial u ^ { i } } \Big | _ { u }$ , where $\left\{ \frac { \partial } { \partial u ^ { i } } \Big | _ { u } \left( i = 1 , \cdot \cdot \cdot , m \right) \right\}$ is the basis of $T _ { u } U$ . Then, it is easy to prove that

$$
X _ { u } \longmapsto ( u ; a ^ { 1 } , \cdot \cdot \cdot , a ^ { m } )
$$

is a diffeomorphism from $T U$ to $U \times \mathbf { R } ^ { m }$ . Moreover, since each fiber $T _ { u } U$ of $T U$ is a linear space, maps limited on $T _ { u } U$ is a linear isomorphism from $T _ { u } U$ to $\{ u \} \times \mathbf { R } ^ { m }$ i.e., $T U$ is a trivial tangent bundle.

Example 2.4. $T S ^ { 1 }$ is a trivial tangent bundle, i.e., $T S ^ { 1 } \simeq S ^ { 1 } \times { \bf R }$

Let $\scriptstyle { \mathcal { A } } = \{ ( U , \varphi ) , ( V , \psi ) \}$ be a smooth atlas on $S ^ { 1 }$ , where

$$
\begin{array} { l l } { { U = \{ ( \cos \theta , \sin \theta ) | 0 < \theta < 2 \pi \} , } } & { { \varphi ( \cos \theta , \sin \theta ) = \theta , } } \\ { { V = \{ ( \cos \theta , \sin \theta ) | - \pi < \theta < \pi \} , } } & { { \psi ( \cos \theta , \sin \theta ) = \theta , } } \end{array}
$$

$$
\psi \circ \varphi ^ { - 1 } ( \theta ) = \left\{ \begin{array} { l l } { \theta , } & { 0 < \theta < \pi , } \\ { \theta - 2 \pi , } & { \pi < \theta < 2 \pi . } \end{array} \right.
$$

Define $f : T S ^ { 1 } \to S ^ { 1 } \times \mathbf { R }$ , s.t.

$$
f ( X _ { p } ) = \left\{ \begin{array} { l l } { ( p ; a ) , } & { p \in U , \quad X _ { p } = a \displaystyle \frac { \partial } { \partial x } \Big \vert _ { p } , } \\ { ( p ; b ) , } & { p \in V , \quad X _ { p } = b \displaystyle \frac { \partial } { \partial y } \Big \vert _ { p } , } \end{array} \right.
$$

where $x , y$ are the coordinate functions on $( U , \varphi ) , ( V , \psi )$ respectively. When $p \in U$ $V$ , we have

$$
\frac { \partial } { \partial x } \Big \vert _ { p } = \frac { \partial y } { \partial x } \Big \vert _ { p } \frac { \partial } { \partial y } \Big \vert _ { p } = \frac { \partial } { \partial y } \Big \vert _ { p } .
$$

Therefore, $f$ has the definition and is a 1 to 1 correspondence. Moreover, $f$ and $f ^ { - 1 }$ are smooth. Hence, $T S ^ { 1 }$ is a trivial tangent bundle.

Apart from trivial tangent bundles, there exists a broad class of nontrivial tangent bundles. For an example, $T S ^ { 2 }$ is a nontrivial tangent bundle.

Definition 2.5. Let $f : M \to N$ be smooth. Define a mapping $T f : T M  T N$ , s.t.

$$
T \mathfrak { f } | _ { T _ { p } M } = \mathfrak { f } _ { * p } , \quad \forall p \in M ,
$$

then $T f$ is called the tangent mapping of $f$ .

Remark 2.6. $\forall X _ { p } \in \ T _ { p } M$ , there exist charts $( U , \varphi )$ on $M$ about $p$ and $( V , \psi )$ on $N$ about $f ( \boldsymbol p )$ , s.t. ${ \bar { f } } ( U ) ~ \subset ~ V$ . By $\pi _ { 1 } \ : \ T M \ \to \ M , \pi _ { 2 } \ : \ T N \ \to \ N$ , it is naturally derived that $( \pi _ { 1 } ^ { - 1 } ( U ) , \varphi _ { U } ) , ( \pi _ { 2 } ^ { - 1 } ( V ) , \psi _ { V } )$ are charts on $T M , T N$ , and $T f ( \pi _ { 1 } ^ { - 1 } ( \dot { U } ) ) \subset \pi _ { 2 } ^ { - 1 } ( V )$ . Note that

$$
\begin{array} { l } { \displaystyle \psi _ { V } \circ T f \circ \varphi _ { U } ^ { - 1 } \big ( u ; a ^ { 1 } , \cdots , a ^ { m } \big ) } \\ { \displaystyle = \Big ( \psi \circ f \circ \varphi _ { U } ^ { - 1 } ; \sum _ { i } a ^ { i } \frac { \partial f _ { 1 } } { \partial x ^ { i } } \Big | _ { \varphi ^ { - 1 } ( u ) } , \cdots , \sum _ { i } a ^ { i } \frac { \partial f _ { n } } { \partial x ^ { i } } \Big | _ { \varphi ^ { - 1 } ( u ) } \Big ) , } \end{array}
$$

which may be simplified as

$$
\psi _ { V } \circ T f \circ \varphi _ { U } ^ { - 1 } ( u ; \alpha ) = \big ( \widehat { f } ( u ) ; \operatorname { D } \widehat { f } ( u ) \alpha \big ) ,
$$

where $\alpha = ( a ^ { 1 } , \cdot \cdot \cdot , a ^ { m } )$ . Therefore, $T f$ is a smooth mapping.

Remark 2.7. Let $M , N , L$ be the differentiable manifolds. By the definition of tangent mapping, if $f : M \to N$ and $g : N  L$ are smooth, then

$$
T ( g \circ f ) = T g \circ T f .
$$

Remark 2.8. If $f : M \to N$ is a diffeomorphism, then $T f : T M  T N$ is also a diffeomorphism.

# 2. Orientation

Next, we introduce the concept of orientation for differentiable manifolds.

Given $V$ as a $m$ -dimensional vector space, $\{ e _ { 1 } ^ { \prime } , \cdot \cdot \cdot , e _ { m } ^ { \prime } \} , \{ e _ { 1 } ^ { \prime \prime } , \cdot \cdot \cdot , e _ { m } ^ { \prime \prime } \}$ as $V$ ’s two ordered bases, if $e _ { j } ^ { \prime \prime } = \sum _ { i = 1 } ^ { m } a _ { i j } e _ { i } ^ { \prime } \left( j = 1 , \cdots , m \right)$ , then

$$
( e _ { 1 } ^ { \prime \prime } , \cdot \cdot \cdot , e _ { m } ^ { \prime \prime } ) = ( e _ { 1 } ^ { \prime } , \cdot \cdot \cdot , e _ { m } ^ { \prime } ) A ,
$$

where $A = ( a _ { i j } ) _ { m \times m } .$ . If det $A > 0$ , we call $\{ e _ { i } ^ { \prime \prime } \}$ and $\{ e _ { j } ^ { \prime } \}$ concurrent; otherwise, if det $A \ : < \ : 0$ , we call $\{ e _ { i } ^ { \prime \prime } \}$ and $\{ e _ { j } ^ { \prime } \}$ reverse. Then, a direction $\mu$ of $V$ can be expressed by a concurrent class $[ \{ e _ { j } ^ { \prime } \} ]$ equivalent to $\{ e _ { j } ^ { \prime } \}$ . The other direction $- \mu$ can be expressed by an equivalent class to the reverse direction of $\{ e _ { j } ^ { \prime } \} . ( V , \mu )$ is called an orientable vector space.

Let $( V , \mu )$ , $( W , \nu )$ be two orientable vector spaces. $A : V \to W$ is a linear isomorphism from $V$ to $W$ . If the orientation of $W$ , which is induced by $A$ , is consistent with $\nu$ , i.e., $A \mu = \nu$ , then $A$ preserves orientations. Otherwise, $A$ reverses orientations. In the below section, we extend the orientation concept to differentiable manifolds.

Definition 2.9. Let $M$ be an $m$ -dimensional differentiable manifold, $\forall p \in M$ , $\mu _ { p }$ is the orientation of $T _ { p } M$ , s.t.

$$
\varphi _ { \ast q } : ( T _ { q } M , \mu _ { q } ) \longrightarrow ( T _ { \varphi ( q ) } { \bf R } ^ { m } , \nu _ { \varphi ( q ) } ) , \quad \forall q \in U
$$

are all linear isomorphisms that preserves orientations, where $( U , \varphi )$ is a chart that contains $p$ , and

$$
\nu _ { \varphi ( q ) } = \left[ \frac { \partial } { \partial u ^ { 1 } } \Big | _ { \varphi ( q ) } , \cdots , \frac { \partial } { \partial u ^ { m } } \Big | _ { \varphi ( q ) } \right] .
$$

Then, $\mu = \{ \mu _ { p } | p \in M \}$ is the orientation on $M$ , and $( M , \mu )$ is called an orientable differentiable manifold.

Remark 2.10. The Definition 2.9 shows that if $( M , \mu )$ is an orientable differentiable manifold, $W$ is an open subset of $M$ , then $\forall p \in M$ and there exists an orientation $\mu _ { p }$ of $T _ { p } M .$ . This gives an orientation on $W$ , denoted by $\mu | W$ . Then, $( W , \mu | W )$ is also an orientable differentiable manifold. Specifically, if $( U , \varphi )$ is a chart on $M$ , then $( U , \mu _ { p } )$ is an orientable differentiable manifold.

Remark 2.10 shows that $M$ may be locally orientable. Next, we discuss how to construct a global orientation.

Proposition 2.11. Let $M$ be an $m$ -dimensional differentiable manifold, then $M$ is orientable, iff there exists $a$ smooth atlas, $\mathcal { A } = \{ ( U _ { \alpha } , \varphi _ { \alpha } ) \}$ , on $M$ , s.t. $\forall \left( U _ { \alpha } , \varphi _ { \alpha } \right)$ , $( U _ { \beta } , \varphi _ { \beta } ) \in \mathcal { A }$ , if $U _ { \alpha } \cap U _ { \beta } \neq \emptyset$ , then

$$
\begin{array} { r } { \operatorname* { d e t } J _ { \varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 } } ( \varphi _ { \alpha } ( q ) ) > 0 , \quad \forall q \in U _ { \alpha } \cap U _ { \beta } , } \end{array}
$$

where $J _ { \varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 } } ( \varphi _ { \alpha } ( q ) )$ is the Jacobian matrix of $\varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 }$ at $\varphi _ { \alpha } ( q )$ .

Proof. Necessity. Since $M$ is orientable, select one of the orientations of $M$ , $\mu =$ $\{ \mu _ { p } \ | \ p \in M \}$ . According to Definition 2.9, $\forall p \in M$ , there exists a chart $( U , \varphi )$ on $M$ about $p$ , s.t. $\forall q \in U$ ,

$$
\varphi _ { * q } \mu _ { q } = \Big [ \frac { \partial } { \partial u ^ { 1 } } \Big | _ { \varphi ( q ) } , \cdots , \frac { \partial } { \partial u ^ { m } } \Big | _ { \varphi ( q ) } \Big ] .
$$

Denote a set consisting of all such charts by $\mathcal { A }$ . Then, $\mathcal { A }$ is a smooth atlas of $M$ , and the properties of $\mathcal { A }$ described in the proposition are easy to prove.

Sufficiency. Let $\mathcal { A }$ be an atlas that satisfies all the properties of the proposition. Choose $\left( U _ { \alpha } , \varphi _ { \alpha } \right)$ , $( U _ { \beta } , \varphi _ { \beta } ) \in \mathcal { A }$ and $U _ { \alpha } \cap U _ { \beta } \neq \emptyset$ , and use $x ^ { 1 } , \cdots , x ^ { m }$ and $y ^ { 1 } , \cdots , y ^ { m }$ to represent the coordinate functions of $\left( U _ { \alpha } , \varphi _ { \alpha } \right)$ , $( U _ { \beta } , \varphi _ { \beta } )$ respectively. Note that

$$
\Bigl ( \frac { \partial } { \partial x ^ { 1 } } \Big | _ { p } , \cdots , \frac { \partial } { \partial x ^ { m } } \Big | _ { p } \Bigr ) = \Bigl ( \frac { \partial } { \partial y ^ { 1 } } \Big | _ { p } , \cdots , \frac { \partial } { \partial y ^ { m } } \Big | _ { p } \Bigr ) J _ { \varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 } } ( \varphi _ { \alpha } ( q ) ) ,
$$

and by supposition $J _ { \varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 } } ( \varphi _ { \alpha } ( q ) ) > 0$ , we have

$$
{ \Big [ } { \frac { \partial } { \partial x ^ { 1 } } } { \Big | } _ { p } , \cdots , { \frac { \partial } { \partial x ^ { m } } } { \Big | } _ { p } { \Big ] } = { \Big [ } { \frac { \partial } { \partial y ^ { 1 } } } { \Big | } _ { p } , \cdots , { \frac { \partial } { \partial y ^ { m } } } { \Big | } _ { p } { \Big ] } ,
$$

i.e., $M$ is orientable.

Remark 2.12. If $f : { \cal { M } }  { \cal { N } }$ is a diffeomorphism, $f A = \{ f ( U _ { \alpha } ) , \varphi _ { \alpha } \circ f ^ { - 1 } \}$ is a smooth atlas. Pick two charts on $N$ , $( f ( \varphi _ { \alpha } ) , \varphi _ { \alpha } \circ f ^ { - 1 } ) , ( f ( \varphi _ { \beta } ) , \varphi _ { \beta } \circ f ^ { - 1 } )$ , we have det $J _ { \varphi _ { \beta } \circ f ^ { - 1 } \circ f \circ \varphi _ { \alpha } ^ { - 1 } } ( \varphi _ { \alpha } ( q ) ) = \operatorname* { d e t } J _ { \varphi _ { \beta } \circ \varphi _ { \alpha } ^ { - 1 } } ( \varphi _ { \alpha } ( q ) ) , \ \forall q$ $\forall q \in U _ { \alpha } \cap U _ { \beta }$ . If $M$ is βorientable, then $N$ α β αis possible, which means orientation is an invariable property under diffeomorphism.

Proposition 2.13. Let $M$ be a connected differentiable manifold; if $M$ is orientable, then $M$ has only two orientations.

Proof. If $\mu = \{ \mu _ { p } \mid p \in M \}$ is an orientation of $M$ , then $- \mu$ is also an orientation. Therefore, $M$ has at least two orientations. Assume there exists another orientation, denoted as $\nu = \{ \nu _ { p } \mid p \in M \}$ . Let $S = \{ p \in M \mid \mu _ { p } = \nu _ { p } \}$ . $\forall p \in S$ , take charts $( U , \varphi ) , ( V , \psi )$ of $M$ about $p$ , s.t. $\mu , \nu$ satisfy all the requirements of Definition 2.9. As a result of $\mu _ { p } = \nu _ { p }$ , we have

$$
\operatorname* { d e t } J _ { \psi \circ \varphi ^ { - 1 } } ( \varphi ( p ) ) > 0 .
$$

By continuity, there exists a neighborhood of $\varphi ( p ) , W \subset \varphi ( U \cap V )$ , s.t.

$$
\operatorname* { d e t } J _ { \psi \circ \varphi ^ { - 1 } } ( \varphi ( u ) ) > 0 , \quad \forall u \in W .
$$

Denote $O = \varphi ^ { - 1 } ( W )$ . Then, $O$ is a neighborhood of $p$ in $M$ , and $O \subset S$ , i.e., $S$ is an open subset of $M$ . Similarly, $M \backslash S$ is also an open subset of $M$ . Since $M$ is connected, we have either $S = \emptyset$ or $S = M$ . If $S = \emptyset$ , then $\mu = - \nu$ ; if $S = M$ , then $\mu = \nu$ . -

Remark 2.14. By the Proposition 2.13, any connected open set on an orientable differentiable manifold $M$ has two and only two orientations.

Remark 2.15. Let $( U , \varphi ) , ( V , \psi )$ be two charts on $M$ , and $U$ and $V$ be connected. If $U \cap V \neq \emptyset$ , then det $J _ { \psi \circ \varphi ^ { - 1 } }$ preserves the orientation on $\varphi ( U \cap V )$ .

Example 2.16. $S ^ { 1 }$ is an orientable differential manifold. Let the smooth atlas of $S ^ { 1 }$ be $\mathcal { A } = \{ ( \mathcal { U } _ { + } , \varphi _ { + } ) , ( \mathcal { U } _ { - } , \varphi _ { - } ) \}$ , where

$$
U _ { + } = S ^ { 1 } \backslash \{ ( 0 , - 1 ) \} , \quad U _ { - } = S ^ { 1 } \backslash \{ ( 0 , 1 ) \} ,
$$

$\varphi _ { \pm } : U _ { \pm } \to \mathbf { R }$ , s.t.

$$
\varphi _ { + } ( u ^ { 1 } , u ^ { 2 } ) = \frac { u ^ { 1 } } { 1 + u ^ { 2 } } , \quad \varphi _ { - } ( u ^ { 1 } , u ^ { 2 } ) = \frac { - u ^ { 1 } } { u ^ { 2 } - 1 } .
$$

Since

$$
\varphi _ { + } \circ \varphi _ { - } ^ { - 1 } ( u ) = - \frac { 1 } { u } , \quad \forall u \in \varphi _ { - } ( U _ { + } \cap U _ { - } ) ,
$$

we have

$$
\operatorname* { d e t } J _ { \varphi _ { + } \circ \varphi _ { - } ^ { - 1 } } ( u ) = \frac { 1 } { u ^ { 2 } } > 0 , \quad \forall u \in \varphi _ { - } ( U _ { + } \cap U _ { - } ) .
$$

Similarly

$$
\operatorname * { d e t } J _ { \varphi _ { - } \circ \varphi _ { + } ^ { - 1 } } ( u ) > 0 , \quad \forall u \in \varphi _ { + } ( U _ { + } \cap U _ { - } ) ,
$$

i.e., $S ^ { 1 }$ is orientable.

Example 2.17. Mobius strip is a non-orientable surface. Define equivalent relation“ ¨ ” on $[ 0 , 1 ] \times ( 0 , 1 )$ :

$$
\begin{array} { l l } { ( u , v ) \sim ( u , v ) , } & { 0 < u < 1 , \quad 0 < v < 1 , } \\ { \qquad } & { } \\ { ( 0 , v ) \sim ( 1 , 1 - v ) , } & { 0 < v < 1 , } \end{array}
$$

$[ 0 , 1 ] \times ( 0 , 1 ) \backslash \sim$ is a Mobius strip, ¨ $\mathcal { A } = \{ ( U , \varphi ) , ( V , \psi ) \}$ is its smooth atlas

$$
\begin{array} { l l } { { U = M \backslash \{ 0 \} \times ( 0 , 1 ) , } } & { { V = M \backslash \left\{ \displaystyle \frac { 1 } { 2 } \right\} \times ( 0 , 1 ) , } } \\ { { } } & { { } } \\ { { \varphi : U \longrightarrow ( 0 , 1 ) \times ( 0 , 1 ) , } } & { { \psi : V \longrightarrow \Big ( - \displaystyle \frac { 1 } { 2 } , \displaystyle \frac { 1 } { 2 } \Big ) \times ( 0 , 1 ) , } } \end{array}
$$

which satisfies:

$$
\begin{array} { r l } & { \boldsymbol { \varphi } ( u , v ) = ( u , v ) , } \\ & { \boldsymbol { \psi } \circ \boldsymbol { \varphi } ^ { - 1 } ( u , v ) = \left\{ \begin{array} { l l } { ( u , v ) , } & { 0 \leq \frac { 1 } { 2 } , } \\ { \vphantom { \left( u - 1 , 1 - v \right) } ( u - 1 ) , } & { \frac { 1 } { 2 } < u \leq 1 , } \\ { \vphantom { \left( u , v \right) } ( u , v ) , } & { \left( u , v \right) \in \left( 0 , \frac { 1 } { 2 } \right) \times ( 0 , 1 ) , } \\ { \vphantom { \left( u - 1 , 1 - v \right) } ( u - 1 , 1 - v ) , } & { \left( u , v \right) \in \left( \frac { 1 } { 2 } , 1 \right) \times ( 0 , 1 ) , } \end{array} \right. } \end{array}
$$

i.e.,

$$
\mathrm { d e t ~ } J _ { \psi \circ \varphi ^ { - 1 } } ( u , v ) = \left\{ \begin{array} { l l } { \begin{array} { r l } { 1 , } & { ( u , v ) \in \left( 0 , \frac { 1 } { 2 } \right) \times ( 0 , 1 ) , } \\ { - 1 , } & { ( u , v ) \in \left( \frac { 1 } { 2 } , 1 \right) \times ( 0 , 1 ) . } \end{array} } \end{array} \right.
$$

By the Remark 2.15, Mobius strip is a nonorientable surface. ¨

Definition 2.18. Let $M , N$ be two orientable differential manifolds, and $f : M \to N$ be a local diffeomorphism ( diffeomorphism in the neighborhood of any $p \in M$ ). If for every $p \in M$ , there exists a $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ that preserves (or reverses) the orientation, then $f$ is said to preserve the orientation (or reverse the orientation).

Proposition 2.19. $f : M \to N$ is a diffeomorphism; if $M$ is a connection, then $f$ preserves the orientation or reverses the orientation.

Proof. Let $S = \{ p \in M \mid f _ { * p } : T _ { p } M \to T _ { f ( p ) } N$ preserves the orientation}. $\forall p \in S$ , because $f _ { \ast p }$ preserves orientation, det $J _ { f } ( p ) > 0$ . From the continuity, there exists $U$ , s.t. det $J _ { f } ( q ) > 0$ , $\forall q \in U$ , i.e., $U \subset S$ . Similarly, $M \backslash S$ is also an open subset of $M$ . Since $M$ is connected, $S = \emptyset$ or $S = M$ . When $S = \emptyset$ , then $f$ preserves the inverse orientation, otherwise $S = M$ ) $f$ preserves the orientation.

# 1.2.2 Vector Field and Flow

Similar to Euclidean space, differentiable manifold also has the concept of vector field and curve of solution.

Definition 2.20. Let $M$ be a differentiable manifold. If map $X : M  T M$ has the property $\pi \circ X = I : M \to M$ , then $X$ is said to be a vector field of $M$ , and is also called a section in the tangent bundle $^ { T M }$ , where $\pi : T M  M$ is a projection. If the map $X$ is smooth, then $X$ is called a smooth vector field.

Proposition 2.21. $X$ is a smooth vector field on $M$ , iff for every $f \in C ^ { \infty } ( M )$ there exists a $X f \in C ^ { \infty } ( M )$ , and $C ^ { \infty } ( M ) \ = \ \left\{ \begin{array} { r l r l } \end{array} \right.$ all smooth functions on $M \}$ , $X f :$ $M \to \mathbf { R } , X f ( p ) = X _ { p } ( f )$ , ∀ p ∈ M, $f \in C ^ { \infty } ( M )$ .

Proof. Necessity. Suppose $( U , \varphi )$ is a chart of $M$ , and $( \pi ^ { - 1 } ( U ) , \varphi _ { U } )$ is an induced natural chart of $T M$ . Suppose $X$ can be expressed as

$$
X _ { p } = \sum _ { i } a ^ { i } ( p ) \frac { \partial } { \partial x ^ { i } } \bigg | _ { p } , \quad \forall p \in U ,
$$

$$
\begin{array} { r l } & { \widehat { X } = \varphi _ { U } \circ X \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow \varphi ( U ) \times \mathbf { R } ^ { m } , } \\ & { } \\ & { \widehat { X } ( u ) = ( u ; a ^ { 1 } \circ \varphi ^ { - 1 } ( u ) , \cdots , a ^ { m } \circ \varphi ^ { - 1 } ( u ) ) , } \end{array}
$$

we know, if $X$ is smooth, then $a ^ { 1 } , \cdots , a ^ { m }$ are smooth too. Since

$$
( X f ) ( p ) = X _ { p } f = \sum _ { i } a ^ { i } ( p ) { \frac { \partial f } { \partial x ^ { i } } } { \Bigr | } _ { p } , \quad \forall p \in U ,
$$

$( X f ) | _ { U }$ is smooth.

Sufficiency. $\forall p \in M$ , let $( U , \varphi )$ be a chart on $M$ about $p$ , where its coordinate function $x ^ { 1 } , \cdots , x ^ { m }$ may be expanded to smooth $\widetilde { x } ^ { i }$ on the entire $M$ , and satisfy ${ \widetilde { x } } ^ { i } =$ $x ^ { i }$ on some neighborhood of $p$ on $V \subset U$ . Then,

$$
X _ { q } = \sum _ { i } X _ { q } ( \widetilde { x } ^ { i } ) \frac { \partial } { \partial x ^ { i } } \Big | _ { q } , \quad \forall q \in U ,
$$

by the supposition $X _ { q } ( \widetilde { x } ^ { i } )$ is smooth, i.e., $X$ is also smooth.

Definition 2.22. Let $X$ be a smooth vector field on the differentiable manifold $M$ . The solution curve of $X$ through $p$ refers to a smooth mapping $c : J  M$ s.t. $c ( 0 ) = p$ , and

$$
c _ { * t } \left( \left. \frac { \mathrm { d } } { \mathrm { d } t } \right| _ { t } \right) = X _ { c ( t ) } , \quad \forall t \in J ,
$$

i.e., the velocity vector at $t$ of a smooth curve $c$ is exactly the value of the vector field at $p$ on $M$ .

Proposition 2.23. Let $f : M \to N$ be a diffeomorphism, $X$ be a smooth vector field on $M$ . If we denote $f _ { * } X = T f \circ X \circ f ^ { - 1 } : N  T N$ , then $f _ { * } X$ is a smooth vector field on $N$ , and c is a solution curve of $X$ through $p \in M$ , iff $f \circ c$ is a solution curve of $f _ { * } X$ through $f ( \boldsymbol p )$ .

Proof. By the definition of tangent mapping, we have

$$
\begin{array} { r l } { \pi _ { 2 } \circ ( f _ { * } X ) } & { = \pi _ { 2 } \circ ( T f \circ X \circ f ^ { - 1 } ) } \\ & { = f \circ ( \pi _ { 1 } \circ X ) \circ f ^ { - 1 } = I . } \end{array}
$$

Since $f ^ { - 1 }$ , $X$ , $T f$ are smooth, $f _ { * } X$ is a smooth vector field on $N$ .

If $c : J  M$ is a solution curve of $X$ through $p$ , then $f \circ c ( 0 ) = f ( 0 ) = f ( p )$ , and

$$
\begin{array} { r l } { ( f \circ c ) _ { \ast t } \Big ( \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t } \Big ) } & { = f _ { \ast c ( t ) } \circ c _ { \ast t } \Big ( \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t } \Big ) } \\ & { = f _ { \ast c ( t ) } ( X _ { c } ( t ) ) = ( f _ { \ast } X ) _ { f \circ c ( t ) } , \quad \forall t \in J . } \end{array}
$$

Therefore the proposition is completed.

Remark 2.24. Let $X$ be a smooth vector field on the differentiable manifold $M$ , and $( U , \varphi )$ be a chart on $M$ . By Proposition 2.23, we have $\varphi _ { * } ( X \mid U )$ to be a smooth vector field of $\varphi ( U )$ .

Remark 2.25. If $\varphi _ { * } ( X \mid U )$ has an expression

$$
\{ \varphi _ { * } ( X \mid U ) \} _ { u } = \sum _ { i = 1 } ^ { m } { a ^ { i } ( u ) \frac { \partial } { \partial u ^ { i } } \Big | _ { u } } , \quad \forall u \in \varphi ( U ) ,
$$

then

$$
( \varphi \circ c ) _ { * t } \Big ( \frac { \partial } { \partial t } \Big | _ { t } \Big ) = \sum _ { i = 1 } ^ { m } \frac { \partial ( \varphi \circ c ) _ { i } } { \partial t } \Big | _ { t } \frac { \partial } { \partial u ^ { i } } \Big | _ { \varphi \circ c ( t ) } , \quad \forall t \in { \cal J } ,
$$

where $( \varphi \circ c ) _ { i }$ is the $i$ -th component of $\varphi \circ c$ .

Therefore, according to Proposition 2.23, there exists a solution curve, $c : J  U$ , of $X$ through $p$ , iff $\varphi \circ c$ is a solution of

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } u ^ { i } } { \mathrm { d } t } = a ^ { i } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { m } ) , \quad i = 1 , \cdot \cdot \cdot , m , } \\ { \qquad } \\ { u ( 0 ) = \varphi ( p ) . } \end{array} \right.
$$

Strictly speaking, a vector field on $\mathbf { R } ^ { n }$ is a mapping $A : \mathbf { R } ^ { n } \to T ( \mathbf { R } ^ { n } )$ ,i.e.,

$$
\forall x \in \mathbf { R } ^ { n } , \quad A ( x ) \in T _ { x } \mathbf { R } ^ { n } .
$$

Since $( e _ { 1 } ) _ { x } , \cdot \cdot \cdot , ( e _ { n } ) _ { x }$ form a basis on $T _ { x } \mathbf { R } ^ { n }$ , we can write $\left\{ \frac { \partial } { \partial x _ { 1 } } , \cdots , \frac { \partial } { \partial x _ { n } } \right\}$ ∂  , therefore

$$
A ( x ) = \sum _ { i = 1 } ^ { n } A _ { i } ( x ) ( e _ { i } ) _ { x } .
$$

If $A _ { i } ( x ) \in C ^ { \infty }$ , then $A ( x )$ is called a smooth vector field on $\mathbf { R } ^ { n }$ . The set of all smooth vector fields on $\mathbf { R } ^ { n }$ is denoted by $\mathcal { X } ( \mathbf { R } ^ { n } )$ . For any vector $A ( x ) , B ( x ) \in { \mathcal { X } } ( \mathbf { R } ^ { n } )$ define:

$$
\begin{array} { l l } { ( \alpha A + \beta B ) ( x ) = \alpha A ( x ) + \beta B ( x ) , } & { \alpha , \beta \in \mathbf { R } , } \\ { \qquad } & { } \\ { ( f A ) ( x ) = f ( x ) A ( x ) , } & { f ( x ) \in C ^ { \infty } ( \mathbf { R } ^ { n } ) . } \end{array}
$$

Then, $\mathcal { X } ( \mathbf { R } ^ { n } )$ is a $C ^ { \infty }$ module of $C ^ { \infty }$ -vector on $\mathbf { R } ^ { n }$ .

If we denote $A ( x ) \in { \mathcal { X } } ( \mathbf { R } ^ { n } )$ by $( A _ { 1 } ( x ) , \cdot \cdot \cdot , A _ { n } ( x ) ) ^ { \prime }$ , i.e.,

$$
A ( x ) = \sum _ { i = 1 } ^ { n } A _ { i } ( x ) ( e _ { i } ) _ { x } = ( A _ { 1 } ( x ) , \cdot \cdot \cdot , A _ { n } ( x ) ) ^ { \prime } ,
$$

then $A ( x )$ is a $C ^ { \infty } n$ -value function.

# 1.3 Exterior Product

Exterior product is one of the algebraic operations. It has quite an interesting geometric background. In this section, we would like to construct a new linear space from an original linear space so that the new space has not only the linear space algebraic structure, but also a new algebraic operation — exterior product. This forms a basis for the differential form introduced later. These materials can be found in a series of book $\left. \left[ \mathbf { A M } 7 8 , \mathbf { C h e } 5 3 , \mathbf { A r n } 8 9 , \mathbf { E d e } 8 5 , \mathbf { F l a } \right] \right.$ .

In $\mathbf { R } ^ { 3 }$ , let the vectors be

$$
\begin{array} { r } { a _ { 1 } = a _ { 1 1 } i + a _ { 1 2 } j + a _ { 1 3 } k , } \\ { \quad } \\ { a _ { 2 } = a _ { 2 1 } i + a _ { 2 2 } j + a _ { 2 3 } k , } \\ { \quad } \\ { a _ { 3 } = a _ { 3 1 } i + a _ { 3 2 } j + a _ { 3 3 } k , } \end{array}
$$

where $a _ { 1 } , a _ { 2 } , a _ { 3 }$ are linearly independent. Then,

$$
V = \left\{ x \in \mathbf { R } ^ { 3 } \mid x = \alpha _ { 1 } a _ { 1 } + \alpha _ { 2 } a _ { 2 } + \alpha _ { 3 } a _ { 3 } , \ 0 \leq \alpha _ { 1 } , \ \alpha _ { 2 } , \ \alpha _ { 3 } \leq 1 \right\}
$$

a spanned parallelepiped by vectors $a _ { 1 } , a _ { 2 } , a _ { 3 }$ . We introduce a new operation, $\wedge$ between $a _ { 1 } , a _ { 2 } , a _ { 3 }$ as follows:

$$
a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 } = \left| \begin{array} { l l l } { { a _ { 1 1 } } } & { { a _ { 1 2 } } } & { { a _ { 1 3 } } } \\ { { a _ { 2 1 } } } & { { a _ { 2 2 } } } & { { a _ { 2 3 } } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { a _ { 3 3 } } } \end{array} \right| .
$$

The geometric meaning of $a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 }$ is the orientable volume of $V$ , where orientation means the sign of the volume is positive or negative. If the right hand law is followed, the volume has the plus sign, otherwise it has the minus sign . It is easy to see that operation $\wedge$ satisfies the following laws:

$1 ^ { \circ }$ Multilinear. Let $a _ { 2 } = \beta b + \gamma c , b .$ , $c$ be vectors, $\beta , \gamma$ be real numbers. Then,

$$
a _ { 1 } \wedge ( \beta b + \gamma c ) \wedge a _ { 3 } = \beta ( a _ { 1 } \wedge b \wedge a _ { 3 } ) + \gamma ( a _ { 1 } \wedge c \wedge a _ { 3 } ) .
$$

# $2 ^ { \circ }$ Anti-commute

$$
\begin{array} { r } { a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 } = - a _ { 2 } \wedge a _ { 1 } \wedge a _ { 3 } , } \\ { a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 } = - a _ { 3 } \wedge a _ { 2 } \wedge a _ { 1 } , } \\ { a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 } = - a _ { 1 } \wedge a _ { 3 } \wedge a _ { 2 } . } \end{array}
$$

From $2 ^ { \circ }$ we know that if $a _ { 1 } , a _ { 2 } , a _ { 3 }$ has two identical vectors, then $a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 } = 0$

Example 3.1. Let $e _ { 1 } , e _ { 2 } , e _ { 3 }$ be a basis in $\mathbf { R } ^ { 3 }$ , which are not necessarily orthogonal, and let $a _ { 1 } , a _ { 2 } , a _ { 3 }$ be three vectors in $\mathbf { R } ^ { 3 }$ , which can be represented by

$$
\begin{array} { r } { a _ { 1 } = a _ { 1 1 } e _ { 1 } + a _ { 1 2 } e _ { 2 } + a _ { 1 3 } e _ { 3 } , } \\ { a _ { 2 } = a _ { 2 1 } e _ { 1 } + a _ { 2 2 } e _ { 2 } + a _ { 2 3 } e _ { 3 } , } \\ { a _ { 3 } = a _ { 3 1 } e _ { 1 } + a _ { 3 2 } e _ { 2 } + a _ { 3 3 } e _ { 3 } . } \end{array}
$$

By multilinearity and anti-commutativity of $\wedge$ , after the computation, we have

$$
a _ { 1 } \wedge a _ { 2 } \wedge a _ { 3 } = { \left| \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right| } e _ { 1 } \wedge e _ { 2 } \wedge e _ { 3 } .
$$

Example 3.2. Let $e _ { 1 } , e _ { 2 } , e _ { 3 }$ be a basis in $\mathbf { R } ^ { 3 }$ , and

$$
\begin{array} { r } { a _ { 1 } = a _ { 1 1 } e _ { 1 } + a _ { 1 2 } e _ { 2 } + a _ { 1 3 } e _ { 3 } , } \\ { a _ { 2 } = a _ { 2 1 } e _ { 1 } + a _ { 2 2 } e _ { 2 } + a _ { 2 3 } e _ { 3 } . } \end{array}
$$

Then,

$$
a _ { 1 } \wedge a _ { 2 } = { \left| \begin{array} { l l } { a _ { 1 1 } } & { a _ { 1 2 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } \end{array} \right| } e _ { 1 } \wedge e _ { 2 } + { \left| \begin{array} { l l } { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 2 } } & { a _ { 2 3 } } \end{array} \right| } e _ { 2 } \wedge e _ { 3 } + { \left| \begin{array} { l l } { a _ { 1 3 } } & { a _ { 1 1 } } \\ { a _ { 2 3 } } & { a _ { 2 1 } } \end{array} \right| } e _ { 3 } \wedge e _ { 1 } .
$$

The geometric significance of this formula is that the projection of the parallelepiped spanned by the pair of vectors $a _ { 1 }$ and $a _ { 2 }$ onto the coordinate plane $e _ { 1 } e _ { 2 } , e _ { 2 } e _ { 3 } , e _ { 3 } e _ { 1 }$ is equal to $A _ { 1 2 } , A _ { 2 3 }$ , and $A _ { 3 1 }$ respectively. Abstracting from the multilinearity and the anti-commutativity, which is satisfied by the operation wedge, we can obtain the concept of exterior product.

# 1.3.1 Exterior Form

# 1. 1- Form

In this section, $\mathbf { R } ^ { n }$ is an $n$ -dimensional real vector space, where the vectors are denoted by $\xi , \eta , \cdots \in \mathbf { R } ^ { n }$ .

Definition 3.3. A form of degree 1 (or a 1-form) on $\mathbf { R } ^ { n }$ is a linear function $\omega : \mathbf { R } ^ { n } \to \mathbf { \Omega }$ $\mathbf { R }$ , i.e.,

$$
\omega ( \lambda _ { 1 } \xi _ { 1 } + \lambda _ { 2 } \xi _ { 2 } ) = \lambda _ { 1 } \omega ( \xi _ { 1 } ) + \lambda _ { 2 } \omega ( \xi _ { 2 } ) , \quad \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } , \quad \xi _ { 1 } , \xi _ { 2 } \in { \bf R } ^ { n } .
$$

The set of all 1-forms on $\mathbf { R } ^ { n }$ is denoted by $\Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ . For $\omega _ { 1 } , \omega _ { 2 } \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ , define

$$
( \lambda _ { 1 } \omega _ { 1 } + \lambda _ { 2 } \omega _ { 2 } ) ( \xi ) = \lambda _ { 1 } \omega _ { 1 } ( \xi ) + \lambda _ { 2 } \omega _ { 2 } ( \xi ) , \quad \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } .
$$

Then, $\Lambda ^ { 1 } \mathbf { R } ^ { n }$ becomes a vector space, i.e., the dual space $( \mathbf { R } ^ { n } ) ^ { * }$ of $\mathbf { R } ^ { n }$

Let

$$
e _ { 1 } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] } , \quad e _ { 2 } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { \vdots } \\ { 0 } \end{array} \right] } , \quad \cdots , \quad e _ { n } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \vdots } \\ { 1 } \end{array} \right] }
$$

be the standard basis on $\mathbf { R } ^ { n }$ . $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ forms the coordinate system on $\mathbf { R } ^ { n }$ , i.e., if $\xi = a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + \cdot \cdot \cdot + a _ { n } e _ { n }$ , then $x _ { i } ( \xi ) = a _ { i }$ , especially $x _ { i } ( e _ { j } ) = \delta _ { i j }$ . Obviously, $x _ { i } \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ . For any $\omega \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ ,

$$
\omega ( \xi ) = \omega { \Big ( } \sum _ { i = 1 } ^ { n } a _ { i } e _ { i } { \Big ) } = \sum _ { i = 1 } ^ { n } a _ { i } \omega ( e _ { i } ) = \sum _ { n } ^ { i = 1 } \omega ( e _ { i } ) x _ { i } ( \xi ) ,
$$

and so

$$
\omega = \omega ( e _ { 1 } ) x _ { 1 } + \omega ( e _ { 2 } ) x _ { 2 } + \cdot \cdot \cdot + \omega ( e _ { n } ) x _ { n } .
$$

Thus, $x _ { 1 } , \cdots , x _ { n }$ is a basis on $\Lambda ^ { 1 } ( { \bf R } ^ { n } ) , \Lambda ^ { 1 } ( { \bf R } ^ { n } ) = \{ x _ { i } \} _ { i = 1 , \cdots , n } .$

Example 3.4. If $F$ is a uniform force field on a Euclidean space $\mathbf { R } ^ { 3 }$ , then its work $A$ on a displacement $\xi$ is a 1-form acting on $\xi$ ,

$$
\omega _ { F } ( \xi ) = ( F , \xi ) = F _ { 1 } a _ { 1 } + F _ { 2 } a _ { 2 } + F _ { 3 } a _ { 3 } , \quad \xi = a _ { 1 } e _ { 1 } + a _ { 2 } e _ { 2 } + a _ { 3 } e _ { 3 }
$$

or

$$
\omega _ { F } = F _ { 1 } x _ { 1 } + F _ { 2 } x _ { 2 } + F _ { 3 } x _ { 3 } .
$$

# 2. 2-Forms

Definition 3.5. An exterior form of degree 2 (or a 2-form) is a bilinear, skewsymmetric function $\omega ^ { 2 } \colon \mathbf { R } ^ { n } \times \mathbf { R } ^ { n }  \mathbf { R }$ , i.e.,

$$
\begin{array} { r l } & { \omega ^ { 2 } ( \lambda _ { 1 } \xi _ { 1 } + \lambda _ { 2 } \xi _ { 2 } , \xi _ { 3 } ) = \lambda _ { 1 } \omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 3 } ) + \lambda _ { 2 } \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 3 } ) , } \\ & { } \\ & { \omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) = - \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 1 } ) , \quad \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } \in { \bf R } ^ { n } , \quad \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } . } \end{array}
$$

The set of all 2-forms on $\mathbf { R } ^ { n }$ is denoted by $\Lambda ^ { 2 } ( { \bf R } ^ { n } ) = \Lambda ^ { 2 }$ .

Similarly, if we define the sum of two 2-forms $\omega _ { 1 } ^ { 2 } , \omega _ { 2 } ^ { 2 }$ and scalar multiplication as follows

$$
\begin{array} { c } { { ( \lambda _ { 1 } \omega _ { 1 } ^ { 2 } + \lambda _ { 2 } \omega _ { 2 } ^ { 2 } ) ( \xi _ { 1 } , \xi _ { 2 } ) = \lambda _ { 1 } \omega _ { 1 } ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) + \lambda _ { 2 } \omega _ { 2 } ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) , } } \\ { { { } } } \\ { { \omega _ { 1 } ^ { 2 } , \omega _ { 2 } ^ { 2 } \in \Lambda ^ { 2 } ( { \bf R } ^ { n } ) , \quad \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } , } } \end{array}
$$

then $\Lambda ^ { 2 } ( \mathbf { R } ^ { n } )$ becomes a vector space on $\mathbf { R }$ .

Property 3.6. The skew-symmetric condition $\omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) - \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 1 } )$ is equivalent to $\omega ^ { 2 } ( \xi , \xi ) = 0$ , $\forall \xi \in \mathbf { R } ^ { n }$ since from the latter it follows that

$$
\begin{array} { r l } { 0 } & { = \omega ^ { 2 } ( \xi _ { 1 } + \xi _ { 2 } , \xi _ { 1 } + \xi _ { 2 } ) } \\ & { = - \omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 1 } ) + \omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) + \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 1 } ) + \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 2 } ) } \\ & { = \omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) + \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 1 } ) . } \end{array}
$$

i.e., $\omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } ) = \omega ^ { 2 } ( \xi _ { 2 } , \xi _ { 1 } )$

Example 3.7. Let $S ( \xi _ { 1 } , \xi _ { 2 } )$ be the oriented area of the parallelogram constructed on the vector $\xi _ { 1 }$ and $\xi _ { 2 }$ of the oriented Euclidean plane $\mathbf { R } ^ { 2 }$ , i.e.,

$$
\begin{array} { r } { S ( \xi _ { 1 } , \xi _ { 2 } ) = \left| \begin{array} { c c } { \xi _ { 1 1 } } & { \xi _ { 1 2 } } \\ { \xi _ { 2 1 } } & { \xi _ { 2 2 } } \end{array} \right| , } \end{array}
$$

where

$$
\xi _ { 1 } = \xi _ { 1 1 } e _ { 1 } + \xi _ { 1 2 } e _ { 2 } , \qquad \xi _ { 2 } = \xi _ { 2 1 } e _ { 1 } + \xi _ { 2 2 } e _ { 2 } .
$$

Example 3.8. Let $v$ be a given vector on the oriented Euclidean space $\mathbf { R } ^ { 3 }$ . The triple scalar product on other two vectors $\xi _ { 1 }$ and $\xi _ { 2 }$ is a 2-form:

$$
\omega ( \xi _ { 1 } , \xi _ { 2 } ) = ( v , [ \xi _ { 1 } , \xi _ { 2 } ] ) = \left| \begin{array} { l l l } { v _ { 1 } } & { v _ { 2 } } & { v _ { 3 } } \\ { \xi _ { 1 1 } } & { \xi _ { 1 2 } } & { \xi _ { 1 3 } } \\ { \xi _ { 2 1 } } & { \xi _ { 2 2 } } & { \xi _ { 2 3 } } \end{array} \right| ,
$$

$$
v = \sum _ { i = 1 } ^ { 3 } v _ { i } e _ { i } ^ { j } , \xi _ { j } = \sum _ { i = 1 } ^ { 3 } \xi _ { j i } e _ { i } ( j = 1 , 2 ) .
$$

# 3. $\boldsymbol { k }$ -Forms

We denote the set of all permutations of the set $\{ 1 , 2 , \cdots , k \}$ by $S _ { k }$ and its element by

$$
\begin{array} { l } { \sigma = \{ \sigma ( 1 ) , \sigma ( 2 ) , \cdots , \sigma ( k ) \} = \{ i _ { 1 } , i _ { 2 } , \cdots , i _ { k } \} \in \nu _ { k } , } \\ { \varepsilon ( \sigma ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f } \sigma \in \nu _ { k } \mathrm { ~ i s ~ e v e n } , } \\ { - 1 , } & { \mathrm { i f } \sigma \in \nu _ { k } \mathrm { ~ i s ~ o d d } . } \end{array} \right. } \end{array}
$$

Definition 3.9. An exterior form of degree $k$ (or a $k$ -form) is a function of $k$ vectors that is $k$ -linear and skew-symmetric:

$$
\begin{array} { c } { { \omega ( \lambda _ { 1 } \xi _ { 1 } ^ { \prime } + \lambda _ { 2 } \xi _ { 1 } ^ { \prime \prime } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { k } ) = \lambda _ { 1 } \omega ( \xi _ { 1 } ^ { \prime } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { k } ) + \lambda _ { 2 } \omega ( \xi _ { 1 } ^ { \prime \prime } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { k } ) , } } \\ { { \omega ( \xi _ { i _ { 1 } } , \xi _ { i _ { 2 } } , \cdot \cdot \cdot , \xi _ { i _ { k } } ) = \varepsilon ( \sigma ) \omega ( \xi _ { 1 } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { k } ) , } } \\ { { \xi _ { 1 } ^ { \prime } , \xi _ { 1 } ^ { \prime \prime } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { k } \in { \bf R } ^ { n } , \quad \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } , \quad \sigma \in \nu _ { k } , } } \end{array}
$$

where $\sigma = ( i _ { 1 } , i _ { 2 } , \cdots , i _ { k } ) \in S _ { k }$ .

Example 3.10. The oriented volume of the parallelepiped with edges $\xi _ { 1 } , \xi _ { 2 } , \cdots , \xi _ { n }$ in the oriented Euclidean space $\mathbf { R } ^ { n }$ is an $n$ -form.

$$
V ( \xi _ { 1 } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { n } ) = \left| \begin{array} { c c c } { { \xi _ { 1 1 } } } & { { \cdot \cdot \cdot } } & { { \xi _ { 1 n } } } \\ { { \xi _ { 2 1 } } } & { { \cdot \cdot \cdot } } & { { \xi _ { 2 n } } } \\ { { } } & { { } } & { { \vdots } } \\ { { \xi _ { n 1 } } } & { { \cdot \cdot \cdot } } & { { \xi _ { n n } } } \end{array} \right| ,
$$

where $\xi _ { i } = \xi _ { i _ { 1 } } e _ { 1 } + \cdot \cdot \cdot + \xi _ { i _ { n } } e _ { n }$

The set of all $k$ -forms in $\mathbf { R } ^ { n }$ is denoted by $\Lambda ^ { k } ( \mathbf { R } ^ { n } )$ . It forms a real vector space if we introduce operations of addition.

$$
\begin{array} { r l } & { ( \lambda _ { 1 } \omega _ { 1 } ^ { k } + \lambda _ { 2 } \omega _ { 2 } ^ { k } ) ( \xi _ { 1 } , \xi _ { 2 } , \cdots , \xi _ { k } ) = \lambda _ { 1 } \omega _ { 1 } ^ { k } ( \xi _ { 1 } , \xi _ { 2 } , \cdots , \xi _ { k } ) + \lambda _ { 2 } \omega _ { 2 } ^ { k } ( \xi _ { 1 } , \xi _ { 2 } , \cdots , \xi _ { k } ) , } \\ & { \quad \quad \quad \quad \quad \quad \quad \omega _ { 1 } ^ { k } , \omega _ { 2 } ^ { k } \in \Lambda ^ { k } ( { \bf R } ^ { n } ) , \quad \lambda _ { 1 } , \lambda _ { 2 } \in { \bf R } . } \end{array}
$$

it

Question 3.11. Show that if $\eta _ { j } = \sum _ { i = 1 } ^ { k } a _ { j i } \xi _ { i } \left( j = 1 , \cdot \cdot \cdot , k \right)$ , then

$$
\omega ^ { k } ( \eta _ { 1 } , \eta _ { 2 } , \cdot \cdot \cdot , \eta _ { k } ) = \operatorname* { d e t } { ( a _ { j i } ) \omega ^ { k } ( \xi _ { 1 } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { k } ) } .
$$

# 1.3.2 Exterior Algebra

# 1. The exterior product of two 1-forms

In the previous section, we have defined various exterior forms. We now introduce one more operation: exterior multiplication of forms. As a matter of fact, these forms can be generated from the 1-forms by an operation called exterior product.

Definition 3.12. For $\omega _ { 1 }$ and $\omega _ { 2 } \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ , the exterior product of $\omega _ { 1 }$ and $\omega _ { 2 }$ denoted by $\omega _ { 1 } \wedge \omega _ { 2 }$ is defined by the formula

$$
\begin{array} { r } { ( \omega _ { 1 } \wedge \omega _ { 2 } ) ( \xi _ { 1 } , \xi _ { 2 } ) = \left| \begin{array} { l l } { \omega _ { 1 } ( \xi _ { 1 } ) } & { \omega _ { 2 } ( \xi _ { 1 } ) } \\ { \omega _ { 1 } ( \xi _ { 2 } ) } & { \omega _ { 2 } ( \xi _ { 2 } ) } \end{array} \right| , \quad \xi _ { 1 } , \xi _ { 2 } \in { \bf R } ^ { n } , } \end{array}
$$

which denotes the oriented area of the image of the parallelogram with sides $\omega ( \xi _ { 1 } )$ and $\omega ( \xi _ { 2 } )$ on the $\omega _ { 1 } , \omega _ { 2 }$ plane.

It is not hard to verify that $\omega _ { 1 } \wedge \omega _ { 2 }$ really is a 2-form and has properties

$$
\begin{array} { c } { { \omega _ { 1 } \wedge \omega _ { 2 } = - \omega _ { 2 } \wedge \omega _ { 1 } , } } \\ { { { } } } \\ { { \left( \lambda _ { 1 } \omega _ { 1 } ^ { \prime } + \lambda _ { 2 } \omega _ { 1 } ^ { \prime \prime } \right) \wedge \omega _ { 2 } = \lambda _ { 1 } \omega _ { 1 } ^ { \prime } \wedge \omega _ { 2 } + \lambda _ { 2 } \omega _ { 1 } ^ { \prime \prime } \wedge \omega _ { 2 } . } } \end{array}
$$

Now suppose we have chosen a system of linear coordinates on $\mathbf { R } ^ { n }$ , i.e., we are given $n$ independent 1-forms, $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ . We will call these forms basic. The exterior products of the basic forms are the 2-forms $x _ { i } \wedge x _ { j }$ . By skew-symmetry,

$$
\begin{array} { r l } & { x _ { i } \in \Lambda ^ { 1 } ( { \bf R } ^ { n } ) , \quad x _ { i } \wedge x _ { i } = 0 , } \\ & { x _ { i } \wedge x _ { j } = - x _ { j } \wedge x _ { i } , } \\ & { ( x _ { i } \wedge x _ { j } ) ( \xi _ { 1 } , \xi _ { 2 } ) = \left| \begin{array} { l l } { x _ { i } ( \xi _ { 1 } ) } & { x _ { j } ( \xi _ { 1 } ) } \\ { x _ { i } ( \xi _ { 2 } ) } & { x _ { j } ( \xi _ { 2 } ) } \end{array} \right| } \\ & { \qquad = \left| \begin{array} { l l } { a _ { i } } & { a _ { j } } \\ { b _ { i } } & { b _ { j } } \end{array} \right| = a _ { i } b _ { j } - a _ { j } b _ { i } , } \end{array}
$$

where $\xi _ { 1 } = \sum _ { i } a _ { i } e _ { i }$ , $\xi _ { 2 } = \sum _ { i } b _ { i } e _ { i }$ . It is the oriented area of the parallelogram with sides $( x _ { i } ( \xi _ { 1 } ) , x _ { i } ( \xi _ { 2 } ) )$ and $( x _ { j } ( \xi _ { 1 } ) , x _ { j } ( \xi _ { 2 } ) )$ in the $( x _ { i } , x _ { j } )$ -plane.

For any $\omega \in \Lambda ^ { 2 } ( \mathbf { R } ^ { n } )$

$$
\begin{array} { r l } { \omega ( \xi _ { 1 } , \xi _ { 2 } ) } & { = \displaystyle \sum _ { i , j = 1 \atop i < j } ^ { n } \omega ( a _ { i } e _ { i } , b _ { j } e _ { j } ) = \displaystyle \sum _ { i , j = 1 \atop i < j } ^ { n } a _ { i } b _ { j } \omega ( e _ { i } , e _ { j } ) } \\ & { = \displaystyle \sum _ { i < j } ( a _ { i } b _ { j } - a _ { j } b _ { i } ) \omega ( e _ { i } , e _ { j } ) = \displaystyle \sum _ { i < j } \omega ( e _ { i } , e _ { j } ) ( x _ { i } \wedge x _ { j } ) ( \xi _ { 1 } , \xi _ { 2 } ) , } \end{array}
$$

where $\xi _ { 1 } = \sum _ { i } a _ { i } e _ { i } , \xi _ { 2 } = \sum _ { i } b _ { i } e _ { i }$ . Thus,

$$
\omega = \sum _ { i < j } \omega ( e _ { i } , e _ { j } ) x _ { i } \wedge x _ { j } ,
$$

i.e., $\{ x _ { i } \land x _ { j } \} _ { i < j }$ generate $\Lambda ^ { 2 } ( \mathbf { R } ^ { n } )$ . In addition, if

$$
\sum _ { i < j } a _ { i j } x _ { i } \wedge x _ { j } = 0 ,
$$

acting on $e _ { l } , e _ { k } ( l < k )$ , we get

$$
a _ { k l } = \sum _ { i < j } a _ { i j } ( x _ { i } \wedge x _ { j } ) ( e _ { l } , e _ { k } ) = 0 .
$$

Thus, $\{ x _ { i } \land x _ { j } \} _ { i < j }$ are linearly independent and they form a base of $\Lambda ^ { 2 } ( \mathbf { R } ^ { n } )$ , which implies that the dimension of $\Lambda ^ { 2 } ( \mathbf { R } ^ { n } )$ is $\left( \begin{array} { l } { n } \\ { 2 } \end{array} \right)$

In the oriented Euclidean space $\mathbf { R } ^ { 3 }$ , the base of $\Lambda ^ { 2 } ( \mathbf { R } ^ { 3 } )$ is $x _ { 1 } \wedge x _ { 2 } , x _ { 2 } \wedge x _ { 3 }$ , and $x _ { 3 } \wedge x _ { 1 } = - x _ { 1 } \wedge x _ { 3 }$ . Any 2-form $\omega \in \Lambda ^ { 2 } ( \mathbf { R } ^ { 3 } )$ can be represented as

$$
\omega = P x _ { 2 } \wedge x _ { 3 } + Q x _ { 3 } \wedge x _ { 1 } + R x _ { 1 } \wedge x _ { 2 } .
$$

# 2. Exterior monomials

Definition 3.13. For $\omega _ { 1 } , \cdots , \omega _ { k } \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ , we define their exterior product $\omega _ { 1 } \wedge$ $\cdots \wedge \omega _ { k }$ as follows:

$$
\begin{array} { r } { ( \omega _ { 1 } \wedge \cdot \cdot \cdot \wedge \omega _ { k } ) ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k } ) = \left| \begin{array} { c c c } { \omega _ { 1 } ( \xi _ { 1 } ) } & { \cdot \cdot \cdot } & { \omega _ { 1 } ( \xi _ { k } ) } \\ { \vdots } & & { \vdots } \\ { \omega _ { k } ( \xi _ { 1 } ) } & { \cdot \cdot \cdot } & { \omega _ { k } ( \xi _ { k } ) } \end{array} \right| . } \end{array}
$$

In other words, the value of a product of 1-forms on the parallelepiped $\xi _ { 1 } , \cdots , \xi _ { k }$ is equal to the oriented volume of the image of the parallelepiped in the oriented Euclidean coordinate space $\mathbf { R } ^ { n }$ under the mapping $\xi \to ( \omega _ { 1 } ( \xi ) , \cdot \cdot \cdot , \omega _ { k } ( \xi ) )$ .

Question 3.14. Prove that $\omega _ { 1 } \wedge \cdots \wedge \omega _ { k }$ really is a $k$ -form.

# Property 3.15. We have the following properties:

$1 ^ { \circ }$ $\begin{array} { r } { ( \lambda ^ { \prime } \omega _ { 1 } ^ { \prime } + \lambda ^ { \prime \prime } \omega _ { 1 } ^ { \prime \prime } ) \wedge \omega _ { 2 } \wedge \cdots \wedge \omega _ { k } = \lambda ^ { \prime } \omega _ { 1 } ^ { \prime } \wedge \cdots \wedge \omega _ { k } + \lambda ^ { \prime \prime } \omega _ { 1 } ^ { \prime \prime } \wedge \cdots \wedge \omega _ { k } . } \end{array}$ $2 ^ { \circ }$ $\omega _ { \sigma ( 1 ) } \wedge \omega _ { \sigma ( 2 ) } \wedge \cdots \wedge \omega _ { \sigma ( k ) } = \varepsilon ( \sigma ) \omega _ { 1 } \wedge \omega _ { 2 } \wedge \cdots \wedge \omega _ { k }$ .   
$3 ^ { \circ }$ If $i \neq j , \omega _ { i } = \omega _ { j }$ , then $\omega _ { 1 } \wedge \cdot \cdot \cdot \wedge \omega _ { k } = 0$ .   
$4 ^ { \circ }$ If $\omega _ { 1 } , \cdots , \omega _ { k }$ are linearly dependent, then $\omega _ { 1 } \wedge \cdot \cdot \cdot \wedge \omega _ { k } = 0$ .   
$5 ^ { \circ }$ If $\beta _ { i } = \sum _ { j = 1 } ^ { k } a _ { i j } \omega _ { j } \left( i = 1 , \cdot \cdot \cdot , k \right)$ , then

$$
\beta _ { 1 } \wedge \cdot \cdot \cdot \wedge \beta _ { k } = \operatorname* { d e t } { \left( a _ { i j } \right) } \omega _ { 1 } \wedge \cdot \cdot \cdot \wedge \omega _ { k } .
$$

Proof. Here we only prove $5 ^ { \circ }$ , the others are easy. By the linearity of the exterior product,

$$
\begin{array} { r l } { \beta _ { 1 } \wedge \dots \wedge \beta _ { k } } & { = \left( \displaystyle \sum _ { i _ { 1 } = 1 } ^ { k } a _ { 1 i _ { 1 } } \omega _ { i _ { 1 } } \right) \wedge \dots \wedge \left( \displaystyle \sum _ { i _ { k } = 1 } ^ { k } a _ { k i _ { k } } \omega _ { i _ { k } } \right) } \\ & { = \displaystyle \sum _ { i _ { 1 } , \dots , i _ { k } = 1 } ^ { k } a _ { 1 i _ { 1 } } \cdot \cdot \cdot a _ { k i _ { k } } \omega _ { i _ { 1 } } \wedge \dots \wedge \omega _ { i _ { k } } } \\ & { = \displaystyle \sum _ { i _ { 1 } , \dots , i _ { k } \in \nu _ { k } } a _ { 1 i _ { 1 } } \cdot \cdot \cdot a _ { k i _ { k } } \varepsilon ( i _ { 1 } , \cdot \cdot , i _ { k } ) \omega _ { 1 } \wedge \dots \wedge \omega _ { k } \quad ( \mathrm { b y ~ } 2 ^ { \circ } ) } \\ & { = \mathrm { d e t } ( a _ { i j } ) \omega _ { 1 } \wedge \dots \wedge \omega _ { k } . } \end{array}
$$

The proof can be obtained.

Theorem 3.16. $\{ x _ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge x _ { i _ { k } } \} _ { i _ { 1 } < \cdots < i _ { k } }$ form a basis on $\Lambda ^ { k } ( \mathbf { R } ^ { n } )$ ,and so the dimension of $\Lambda ^ { k } ( { \bf R } ^ { n } ) = \left( \begin{array} { l } { { n } } \\ { { k } } \end{array} \right)$ .

Proof. $\mathrm { F o r } \xi _ { i } = \sum _ { j = 1 } ^ { n } \xi _ { i j } e _ { j } \ ( i = 1 , \cdot \cdot \cdot , k ) , \ \xi _ { i } \in \mathbf { R } ^ { n } $ , then

$$
\begin{array} { r l } { \omega ( \xi _ { 1 } , \cdots , \xi _ { k } ) } & { = \omega \Big ( \displaystyle \sum _ { j _ { 1 } = 1 } ^ { n } \xi _ { i , j _ { 1 } } e _ { j _ { 1 } } , \cdots , \displaystyle \sum _ { j _ { k } = 1 } ^ { n } \xi _ { k j _ { k } } e _ { j _ { k } } \Big ) } \\ & { = \displaystyle \sum _ { j _ { 1 } , \cdots , j _ { k } = 1 } ^ { n } \xi _ { i j _ { 1 } } \cdots \xi _ { k j _ { k } } \omega ( e _ { j _ { 1 } } , \cdots , e _ { j _ { k } } ) } \\ & { = \displaystyle \sum _ { i _ { 1 } < \cdots < j _ { k } } \frac { 1 } { ( j _ { 1 } ^ { \prime } , \cdots , j _ { k } ^ { \prime } ) \in \mathcal { E } ^ { k } ( i _ { 1 } , \cdots , i _ { k } ) } \delta ( j _ { 1 } ^ { \prime } , \cdots , j _ { k } ^ { \prime } ) } \\ & { \quad \cdot \xi _ { i j _ { 1 } ^ { \prime } } \cdots \xi _ { k j _ { k } ^ { \prime } } \omega ( \xi _ { i _ { 1 } } , \cdots , \xi _ { i _ { k } } ) } \\ & { = \displaystyle \sum _ { i _ { 1 } < \cdots < j _ { k } } \omega ( e _ { 1 } , \cdots , e _ { k _ { k } } ) x _ { i _ { 1 } } \wedge \cdots \wedge x _ { i _ { k } } ( \xi _ { 1 } , \cdots , \xi _ { k } ) . } \end{array}
$$

So

$$
\omega = \sum _ { i _ { 1 } < \cdots < i _ { k } } \omega ( e _ { i _ { 1 } } , \cdot \cdot \cdot , e _ { i _ { k } } ) x _ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge x _ { i _ { k } } .
$$

Thus, $\{ x _ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge x _ { i _ { k } } \} _ { i _ { 1 } < \cdots < i _ { k } }$ generate $\Lambda ^ { k } ( \mathbf { R } ^ { n } )$ . Obviously, they are linearly indek kpendent. Consequently, they form a basis on $\Lambda ^ { k } ( \mathbf { R } ^ { n } )$ .

In particular,

$$
\dim \Lambda ^ { k } ( \mathbf { R } ^ { n } ) = { \left( \begin{array} { l } { n } \\ { k } \end{array} \right) } .
$$

If $k = n$ , then $\dim \Lambda ^ { n } ( \mathbf { R } ^ { n } ) \ : = \ : \left( \begin{array} { l } { { n } } \\ { { n } } \end{array} \right) \ : = \ : 1$ , $\forall \omega \in \Lambda ^ { n } ( \mathbf { R } ^ { n } )$ , and there must be $\omega = a x _ { 1 } \wedge \cdot \cdot \cdot \wedge x _ { k }$ , for some number $a \in \mathbf { R }$ .

For $k > n$

$$
\dim \left( \Lambda ^ { k } ( \mathbf { R } ^ { n } ) \right) = 0 , \quad \Lambda ^ { k } ( \mathbf { R } ^ { n } ) = \{ 0 \} .
$$

Therefore, the theorem is completed.

Definition 3.17. Let $\omega ^ { k } = \omega _ { 1 } \wedge \cdot \cdot \cdot \wedge \omega _ { k } , \ \omega ^ { l } = \omega _ { k + 1 } \wedge \cdot \cdot \cdot \wedge \omega _ { k + l } ,$ $\omega _ { i } \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ ( $i =$ $1 , \cdots , k + l )$ . Define their product $\omega ^ { k } \wedge \omega ^ { l }$ to be the monomial

$$
\begin{array} { r c l } { \omega ^ { k } \wedge \omega ^ { l } } & { = } & { \left( \omega _ { 1 } \wedge \cdots \wedge \omega _ { k } \right) \wedge \left( \omega _ { k + 1 } \wedge \cdots \wedge \omega _ { k + l } \right) } \\ & & { = } & { \omega _ { 1 } \wedge \cdots \wedge \omega _ { k } \wedge \omega _ { k + 1 } \wedge \cdots \wedge \omega _ { k + l } . } \end{array}
$$

Property 3.18. If $\omega _ { 1 } , \omega _ { 2 }$ , and $\omega _ { 3 }$ are monomials, then

$1 ^ { \circ }$ $\left( \lambda _ { 1 } \omega _ { 1 } + \lambda _ { 2 } \omega _ { 2 } \right) \wedge \omega _ { 3 } = \lambda _ { 1 } \omega _ { 1 } \wedge \omega _ { 3 } + \lambda _ { 2 } \omega _ { 2 } \wedge \omega _ { 3 } .$

$$
\begin{array} { r l } { { 2 } ^ { \circ } } & { { } \omega _ { 1 } \wedge \omega _ { 2 } = ( - 1 ) ^ { k l } \omega _ { 2 } \wedge \omega _ { 1 } , \omega _ { 1 } \in \Lambda ^ { k } , \omega _ { 2 } \in \Lambda ^ { l } . } \\ { 3 ^ { \circ } } & { { } ( \omega _ { 1 } ^ { k } \wedge \omega _ { 2 } ^ { l } ) \wedge \omega _ { 3 } ^ { m } = \omega _ { 1 } ^ { k } \wedge ( \omega _ { 2 } ^ { l } \wedge \omega _ { 3 } ^ { m } ) , \omega _ { 1 } \in \Lambda ^ { k } , \omega _ { 2 } \in \Lambda ^ { l } , \omega _ { 3 } \in \Lambda ^ { m } . } \end{array}
$$

# 3. Exterior product of forms

We now turn to define the exterior product of an arbitrary $k$ -form $\omega ^ { k }$ with an arbitrary $l$ -form $\omega ^ { l }$ .

Definition 3.19. The exterior product $\omega ^ { k } \wedge \omega ^ { l }$ of a $k$ -form $\omega ^ { k }$ on $\mathbf { R } ^ { n }$ with an $l$ -form $\omega ^ { l }$ on $\mathbf { R } ^ { n }$ is the $( k + l )$ -form on $\mathbf { R } ^ { n }$ , defined by the formula

$$
( \omega ^ { k } \wedge \omega ^ { l } ) ( \xi _ { 1 } , \cdots , \xi _ { k + l } ) = \sum _ { i _ { 1 } < \cdots < i _ { k } ; j _ { 1 } < \cdots < j _ { l } } \varepsilon ( \sigma ) \omega ^ { k } ( \xi _ { i _ { 1 } } , \cdots , \xi _ { i _ { k } } ) \omega ^ { l } ( \xi _ { j _ { 1 } } , \cdots , \xi _ { j _ { l } } ) ,
$$

where $\sigma = ( i _ { 1 } , i _ { 2 } , \cdots , i _ { k } , j _ { 1 } , \cdots , j _ { l } )$ is a permutation of the numbers $( 1 , \cdots , k + l )$ .

Example 3.20. For $k = l = 1$ ,

$$
\begin{array} { r l } { ( \omega _ { 1 } \wedge \omega _ { 2 } ) ( \xi _ { 1 } , \xi _ { 2 } ) } & { = \omega _ { 1 } ( \xi _ { 1 } ) \omega _ { 2 } ( \xi _ { 2 } ) - \omega _ { 1 } ( \xi _ { 2 } ) \omega _ { 2 } ( \xi _ { 1 } ) } \\ & { = \left| \begin{array} { l l } { \omega _ { 1 } ( \xi _ { 1 } ) } & { \omega _ { 2 } ( \xi _ { 1 } ) } \\ { \omega _ { 1 } ( \xi _ { 2 } ) } & { \omega _ { 2 } ( \xi _ { 2 } ) } \end{array} \right| , } \end{array}
$$

which agrees with the definition of multiplication of 1-forms.

Example 3.21. For $\omega _ { 1 } \in \Lambda ^ { 2 }$ and $\omega _ { 2 } \in \Lambda ^ { 1 }$ ,

$$
\begin{array} { r l } { ( \omega _ { 1 } \wedge \omega _ { 2 } ) ( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } ) } & { = \omega _ { 1 } ( \xi _ { 1 } , \xi _ { 2 } ) \omega _ { 2 } ( \xi _ { 3 } ) - \omega _ { 1 } ( \xi _ { 1 } , \xi _ { 3 } ) \omega _ { 2 } ( \xi _ { 2 } ) } \\ & { \phantom { = } + \omega _ { 1 } ( \xi _ { 2 } , \xi _ { 3 } ) \omega _ { 2 } ( \xi _ { 1 } ) . } \end{array}
$$

Proposition 3.22. $\omega ^ { k } \wedge \omega ^ { l }$ defined above is actually a $\ : ( k + l ) \ :$ -form.

The linearity of $\omega ^ { k } \wedge \omega ^ { l }$ is based on the linearity of $\omega ^ { k }$ and $\omega ^ { l }$ . The skew-symmetry is based on the following.

Lemma 3.23. If $\omega$ is a $k$ -linear function on $\mathbf { R }$ , then the following conditions are equivalent.

$1 ^ { \circ }$ $\omega ( \xi _ { \sigma ( 1 ) } , \cdot \cdot \cdot , \xi _ { \sigma ( k ) } ) = \varepsilon _ { ( \sigma ) } \omega ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k } ) , \forall \sigma \in \nu _ { k } .$ $2 ^ { \circ }$ $\omega ( \xi _ { 1 } , \cdots , \xi _ { i } , \cdot \cdot \cdot , \xi _ { j } , \cdot \cdot \cdot , \xi _ { k } ) = - \omega ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { j } , \cdot \cdot , \xi _ { i } , \cdot \cdot \cdot , \xi _ { k } ) , \forall i \neq j .$ .   
$3 ^ { \circ }$ $\omega ( \xi _ { 1 } , \cdots , \xi _ { k } ) = 0 ,$ , if $\dot { \cdot } \xi _ { i } = \xi _ { j } , \forall i \neq j$ .   
4◦ $\omega ( \xi _ { 1 } , \cdots , \xi _ { k } ) = 0$ , where $\xi _ { i } = \xi _ { i + 1 }$ $\ : 1 \leq i \leq n - 1 \ : \AA \ : \ :$ ).   
$5 ^ { \circ }$ $\omega ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k } ) = 0$ , $\xi _ { 1 } , \cdots , \xi _ { k }$ are linearly dependent.

The proof is left to the reader. Now we turn to prove Proposition 3.22. For this we only need to prove $4 ^ { \circ }$ of Lemma 3.23.

Proof. By $4 ^ { \circ }$ in Lemma 3.23, we only need to prove that if $\xi _ { i ^ { \prime } } = \xi _ { i ^ { \prime } + 1 }$ , then $( \omega ^ { k } \wedge$ $\omega ^ { l } ) ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { i ^ { \prime } } , \xi _ { i ^ { \prime } + 1 } , \cdot \cdot \cdot , \xi _ { k + l } ) = 0$ .

Consider the terms of the right hand side in (1.2). If $i ^ { \prime } , i ^ { \prime } + 1 \in ( i _ { 1 } , \cdots , i _ { k } )$ , then $\omega ^ { k } ( \xi _ { i _ { 1 } } , \cdot \cdot \cdot , \xi _ { i _ { k } } ) = 0 .$ Therefore,

$$
\omega ^ { k } ( \xi _ { i _ { 1 } } , \cdot \cdot \cdot , \xi _ { i _ { k } } ) \omega ^ { l } ( \xi _ { j + 1 } , \cdot \cdot \cdot , \xi _ { j + l } ) = 0 .
$$

When $i ^ { \prime } , i ^ { \prime } + 1 \in ( j _ { 1 } , \cdots , j _ { l } )$ , the case is similar. If $i ^ { \prime } \in ( i _ { 1 } , \cdots , i _ { k } )$ and $i ^ { \prime } + 1 \in$ $( j _ { 1 } , \cdots , j _ { l } )$ , i.e., $i _ { 1 } < \cdots < i _ { h } < i ^ { \prime } < i _ { h + 1 } < \cdots < i _ { k }$ and $j _ { 1 } < \cdot \cdot \cdot < j _ { n } < i ^ { \prime } + 1 <$ $j _ { n + 1 } < \cdots < j _ { l }$ , then there is another term such that

$$
\begin{array} { l } { { i _ { 1 } < \cdots < i _ { h } < i ^ { \prime } + 1 < i _ { h + 1 } < \cdots < i _ { k } , } } \\ { { \ } } \\ { { j _ { 1 } < \cdots < j _ { n } < i ^ { \prime } < j _ { n + 1 } < \cdots < j _ { l } . } } \end{array}
$$

The condition $\xi _ { i ^ { \prime } + 1 } = \xi _ { i ^ { \prime } }$ implies that

$$
\begin{array} { r l } & { \omega ^ { k } ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { i ^ { \prime } } , \cdot \cdot \cdot , \xi _ { i _ { k } } ) \omega ^ { l } ( \xi _ { j _ { 1 } } , \cdot \cdot \cdot , \xi _ { i ^ { \prime } + 1 } , \cdot \cdot \cdot , \xi _ { j _ { l } } ) } \\ & { \quad = \omega ^ { k } ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { i ^ { \prime } + 1 } , \cdot \cdot \cdot , \xi _ { i _ { k } } ) \omega ^ { l } ( \xi _ { j _ { 1 } } , \cdot \cdot \cdot , \xi _ { i ^ { \prime } } , \cdot \cdot \cdot , \xi _ { j _ { l } } ) . } \end{array}
$$

However, the sign $\varepsilon ( \sigma ) = - \varepsilon ( \sigma ^ { \prime } )$ where

$$
\begin{array} { l } { { \sigma = ( i _ { 1 } , \cdots , i ^ { \prime } , \cdots , i _ { k } , j _ { 1 } , \cdots , i ^ { \prime } + 1 , \cdots , j _ { l } ) , } } \\ { { \nonumber } } \\ { { \sigma ^ { \prime } = ( i _ { 1 } , \cdots , i ^ { \prime } + 1 , \cdots , i _ { k } , j _ { 1 } , \cdots , i ^ { \prime } , \cdots , j _ { l } ) . } } \end{array}
$$

Thus, the right side in $1 ^ { \circ }$ is equal to 0, i.e.,

$$
( \omega ^ { k } \wedge \omega ^ { l } ) ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k + l } ) = 0 .
$$

Hence lemma is proved.

Theorem 3.24. The exterior product of forms defined above is skew-commutative, distributive, and associative, i.e.,

$1 ^ { \circ }$ skew-commutative: $\omega ^ { k } \wedge \omega ^ { l } = ( - 1 ) ^ { k l } \omega ^ { l } \wedge \omega ^ { k }$ . $2 ^ { \circ }$ distributive : $: ( \lambda _ { 1 } \omega _ { 1 } ^ { k } + \lambda _ { 2 } \omega _ { 2 } ^ { k } ) \wedge \omega ^ { l } = \lambda _ { 1 } \omega _ { 1 } ^ { k } \wedge \omega ^ { l } + \lambda _ { 2 } \omega _ { 2 } ^ { k } \wedge \omega ^ { l } .$ $3 ^ { \circ }$ associative : $( \omega ^ { k } \wedge \omega ^ { l } ) \wedge \omega ^ { m } = \omega ^ { k } \wedge ( \omega ^ { l } \wedge \omega ^ { m } )$ .

For monomials, it coincides with the exterior product defined above.

Distributivity follows from the fact that every term in Equation (1.2) is linear with respect to $\omega ^ { k }$ and $\omega ^ { l }$ .

Since

$$
\begin{array} { r l } & { ( \omega ^ { k } \wedge \omega ^ { l } ) ( \xi _ { 1 } , \cdots , \xi _ { k + l } ) } \\ { = } & { \underset { i _ { 1 } < \cdots < i _ { k } ; j _ { 1 } < \cdots < j _ { l } } { = } \varepsilon ( i _ { 1 } , \cdots , i _ { k } , j _ { 1 } , \cdots , j _ { l } ) \omega ^ { k } ( \xi _ { i _ { 1 } } , \cdots , \xi _ { i _ { k } } ) \omega ^ { l } ( \xi _ { j _ { 1 } } , \cdots , \xi _ { j _ { l } } ) } \\ { = } & { \underset { i _ { 1 } < \cdots < i _ { k } ; j _ { 1 } < \cdots < j _ { l } } { \sum } ( - 1 ) ^ { k l } \varepsilon ( j _ { 1 } , \cdots , j _ { l } , i _ { 1 } , \cdots , i _ { k } ) \omega ^ { l } ( \xi _ { j _ { 1 } } , \cdots , \xi _ { j _ { l } } ) \omega ^ { k } ( \xi _ { i _ { 1 } } , \cdots , \xi _ { i _ { k } } ) } \\ { = } & { ( - 1 ) ^ { k l } ( \omega ^ { l } \wedge \omega ^ { k } ) ( \xi _ { 1 } , \cdots , \xi _ { k + l } ) , } \end{array}
$$

we get skew-commutativity.

In order to prove associativity, we first prove that for monomials the exterior product defined by Definition 3.19 coincides with the exterior product in Definition 3.17. Since we have not get proved the equivalence of the Definition 3.17 of exterior product of $k 1$ -forms with the Definition 3.19 , we will temporarily denote the exterior product of $k$ 1-forms by the symbol $\barwedge$ , so that our monomials have the form

$$
\omega ^ { k } = \omega _ { 1 } \overline { { \wedge } } \cdot \cdot \cdot \overline { { \wedge } } \omega _ { k } \quad \mathrm { a n d } \quad \omega ^ { l } = \omega _ { k + 1 } \overline { { \wedge } } \cdot \cdot \cdot \overline { { \wedge } } \omega _ { k + l } .
$$

where $\omega _ { 1 } , \cdots , \omega _ { k + l }$ are 1-forms.

Lemma 3.25. The exterior product of two monomials is a monomial.

$$
\left( \omega _ { 1 } \overline { { \Lambda } } \cdot \cdot \cdot \overline { { \Lambda } } \omega _ { k } \right) \wedge \left( \omega _ { k + 1 } \overline { { \Lambda } } \cdot \cdot \cdot \overline { { \Lambda } } \omega _ { k + l } \right) = \omega _ { 1 } \overline { { \Lambda } } \cdot \cdot \cdot \overline { { \Lambda } } \omega _ { k } \overline { { \Lambda } } \omega _ { k + 1 } \overline { { \Lambda } } \cdot \cdot \cdot \overline { { \Lambda } } \omega _ { k + l } .
$$

Proof.

$$
\begin{array} { r l } & { \mathsf { \Gamma } ( ( \omega _ { 1 } \widetilde { \Lambda } \cdot \cdots \widetilde { \Lambda } \omega _ { k } ) \wedge ( \omega _ { k + 1 } \widetilde { \Lambda } \cdot \cdots \widetilde { \Lambda } \omega _ { k + 1 } ) ) ( \xi _ { 1 } , \cdots , \xi _ { k + l } ) } \\ & { = \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } ; j _ { 1 } < \cdots < j _ { l } } \varepsilon ( i _ { 1 } , \cdots , i _ { k } , j _ { 1 } , \cdots , j _ { l } ) ( \omega _ { 1 } \widetilde { \Lambda } \cdot \cdots \widetilde { \Lambda } \omega _ { k } ) ( \xi _ { i _ { 1 } } , \cdots , \xi _ { i _ { k } } ) } \\ & { \quad \cdot ( \omega _ { k + 1 } \widetilde { \Lambda } \cdot \cdots \widetilde { \Lambda } \omega _ { k + l } ) ( \xi _ { j _ { 1 } } , \cdots , \xi _ { j _ { l } } ) } \\ & { = \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } ; j _ { 1 } < \cdots < j _ { l } } \varepsilon ( i _ { 1 } , \cdots , i _ { k } , j _ { 1 } , \cdots , j _ { l } ) \underset { 1 \leq i \leq k ; 1 \leq m \leq k } { \mathrm { d e t } } \omega _ { i } ( \xi _ { i _ { m } } ) } \\ & { \quad \cdot _ { k + 1 \leq j \leq k + l ; 1 \leq m \leq k } \omega _ { j } ( \xi _ { j _ { m } } ) } \\ & { = \frac { 1 } { 1 \leq i \leq k + l ; 1 \leq j \leq k + l } \omega _ { i } ( \xi _ { j } ) = \omega _ { 1 } \widetilde { \Lambda } \cdot \cdots \widetilde { \Lambda } \omega _ { k + l } ( \xi _ { 1 } , \cdots , \xi _ { k + l } ) . } \end{array}
$$

Therefore, the lemma is completed.

Thus,

$$
\begin{array} { r l } & { \omega _ { 1 } \overline { { \Lambda } } \omega _ { 2 } = \omega _ { 1 } \wedge \omega _ { 2 } , } \\ & { } \\ & { \omega _ { 1 } \overline { { \Lambda } } \omega _ { 2 } \overline { { \Lambda } } \omega _ { 3 } = ( \omega _ { 1 } \overline { { \Lambda } } \omega _ { 2 } ) \wedge \omega _ { 3 } = ( \omega _ { 1 } \wedge \omega _ { 2 } ) \wedge \omega _ { 3 } , } \\ & { } \\ & { \omega _ { 1 } \overline { { \Lambda } } \omega _ { 2 } \overline { { \Lambda } } \omega _ { 3 } = \omega _ { 1 } \wedge \big ( \omega _ { 2 } \overline { { \Lambda } } \omega _ { 3 } \big ) = \omega _ { 1 } \wedge ( \omega _ { 2 } \wedge \omega _ { 3 } ) . } \end{array}
$$

It follows that

$$
( \omega _ { 1 } \wedge \omega _ { 2 } ) \wedge \omega _ { 3 } = \omega _ { 1 } \wedge ( \omega _ { 2 } \wedge \omega _ { 3 } ) ,
$$

and denoted by $\omega _ { 1 } \wedge \omega _ { 2 } \wedge \omega _ { 3 }$ . Thus, $\omega _ { 1 } \overline { { { \wedge } } } \omega _ { 2 } \overline { { { \wedge } } } \omega _ { 3 } = \omega _ { 1 } \wedge \omega _ { 2 } \wedge \omega _ { 3 }$

In general, we have

$$
\omega _ { 1 } \overline { { \wedge } } \omega _ { 2 } \overline { { \wedge } } \cdot \cdot \cdot \overline { { \wedge } } \omega _ { k } = \big ( \cdot \cdot \cdot \big ( \big ( \omega _ { 1 } \wedge \omega _ { 2 } \big ) \wedge \omega _ { 3 } \big ) \wedge \cdot \cdot \cdot \wedge \omega _ { k } \big ) .
$$

We now prove associativity. By Theorem 3.16, $\omega ^ { k } \in \Lambda ^ { k } , \omega ^ { l } \in \Lambda ^ { l }$ and $\omega ^ { m } \in \Lambda ^ { m }$ can be represented by the following formulae resp.

$$
\begin{array} { l } { { \omega ^ { k } = \displaystyle \sum a _ { i _ { 1 } \cdots i _ { k } } x _ { i _ { 1 } } \wedge \cdots \wedge x _ { i _ { k } } , } } \\ { { } } \\ { { \omega ^ { l } = \displaystyle \sum b _ { j _ { 1 } \cdots j _ { l } } x _ { j _ { 1 } } \wedge \cdots \wedge x _ { j _ { l } } , } } \\ { { } } \\ { { \omega ^ { m } = \displaystyle \sum c _ { h _ { 1 } \cdots h _ { m } } x _ { h _ { 1 } } \wedge \cdots \wedge x _ { h _ { m } } . } } \end{array}
$$

By distributivity and associativity for monomials,

$$
\begin{array} { r l } { \sigma ^ { k } \wedge \omega ^ { l } ) \wedge \omega ^ { m } } & { = \displaystyle \sum _ { k , l , m } a b c \big ( \big ( x _ { i 1 } \wedge \cdot \cdot \cdot \wedge x _ { i k } \big ) \wedge \big ( x _ { j 1 } \wedge \cdot \cdot \cdot \wedge x _ { j l } \big ) \big ) \wedge \big ( x _ { h 1 } \wedge \cdot \cdot \cdot \wedge x _ { h m } \big ) } \\ & { = \displaystyle \sum _ { k , l , m } a b c \big ( x _ { i 1 } \wedge \cdot \cdot \cdot \wedge x _ { i k } \big ) \wedge \big ( \big ( x _ { j 1 } \wedge \cdot \cdot \cdot \wedge x _ { j l } \big ) \wedge \big ( x _ { h 1 } \wedge \cdot \cdot \cdot \wedge x _ { h m } \big ) \big ) } \\ & { = \omega ^ { k } \wedge ( \omega ^ { l } \wedge \omega ^ { m } ) . } \end{array}
$$

Based on linear space $\Lambda ^ { k } \left( k = 0 , 1 , 2 , \cdots , n \right)$ , we may construct a bigger linear space $\Lambda$ , which is a direct sum of $\Lambda ^ { 1 } , \Lambda ^ { 1 } , \cdots , \Lambda ^ { n }$ , i.e.,

$$
\Lambda = \Lambda ^ { 0 } { \dot { + } } \Lambda ^ { 1 } { \dot { + } } \cdot \cdot \cdot { \dot { + } } \Lambda ^ { n } .
$$

Each element $\omega$ may be represented as

$$
\omega = \omega _ { 0 } + \omega _ { 1 } + \cdot \cdot \cdot + \omega _ { n } , \quad \omega _ { i } \in \Lambda ^ { i } ,
$$

and this kind of expression is unique. In $\Lambda$ there is not only algebraic structure of the linear space, but also the definition of the exterior product. Direct sum $\Lambda$ is the Grassmann algebra produced by the linear space which contained the entire real number field and the linear space.

$$
1 , x _ { 1 } , \cdot \cdot \cdot , x _ { n } , x _ { i } \wedge x _ { j } ( i < j ) , \cdot \cdot \cdot , x _ { 1 } \wedge x _ { 2 } \wedge \cdot \cdot \cdot \wedge x _ { n }
$$

form the basis of $\Lambda$ , whose dimension is $\dim ( \Lambda ) = \sum _ { i = 0 } ^ { n } { \left( \begin{array} { l } { n } \\ { i } \end{array} \right) } = 2 ^ { n } .$

# 1.4 Foundation of Differential Form

There is no strict definition on how to define $\mathrm { d } f$ for a smooth function and ${ \mathrm { d } } x$ for $\mathrm { d } x _ { 1 } , \cdots , \mathrm { d } x _ { n }$ , in classical mathematical analysis. The differential of the independent variable is equal to its increment in classical mathematical analysis, which is improper in a general sense. Here, we always regard $\mathrm { d } x _ { 1 } , \cdots , \mathrm { d } x _ { n }$ as some basis of a linear space, which is called the differential space.

# 1.4.1 Differential Form

A vector $\xi$ on $\mathbf { R } ^ { n }$ is a vector from 0 into $\xi$ . A tangent vector $( x , \xi ) \in T _ { x } \mathbf { R } ^ { n }$ on $\mathbf { R } ^ { n }$ at $x$ is a vector from $x$ to $x + \xi$ i.e., a fixed vector starting from $x$ to $x + \xi$ . Tangent vector $( x , \xi )$ is usually denoted by $\xi _ { x }$ .

For $( x , \xi ) , ( x , \eta ) \in T _ { x } \mathbf { R } ^ { n } \mathfrak { c }$ define:

$$
\alpha ( x , \xi ) + \beta ( x , \eta ) = ( x , \alpha \xi + \beta \eta ) , \quad \alpha , \beta \in \mathbf { R }
$$

or $\alpha \xi _ { x } + \beta \eta _ { x } = ( \alpha \xi + \beta \eta ) _ { x }$ .Then, the tangent space $T _ { x } \mathbf { R } ^ { n }$ to $\mathbf { R } ^ { n }$ at $x$ forms a vector space, and $( e _ { 1 } ) _ { x } , \cdot \cdot \cdot , ( e _ { n } ) _ { x }$ is its standard basis. The set

$$
T ( \mathbf { R } ^ { n } ) = \bigcup _ { x \in \mathbf { R } ^ { n } } T _ { x } \mathbf { R } ^ { n }
$$

is called the tangent bundle on $\mathbf { R } ^ { n }$ , see Section 1.2. Notice that the tangent bundle $T ( \mathbf { R } ^ { n } )$ consists of all fixed vectors on $\mathbf { R } ^ { n }$ .

The mapping $\pi : T \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ defined by the following formula:

$$
\pi ( \xi _ { x } ) = x , \quad \forall \xi _ { x } \in T _ { x } \mathbf { R } ^ { n }
$$

is called the tangent bundle projection. $\pi ^ { - 1 } ( x ) \ : = \ : T _ { x } \mathbf { R } ^ { n }$ is called the fiber of the tangent bundle over the point. The dual space of $T _ { x } \mathbf { R } ^ { n }$ denoted by $T _ { x } ^ { * } \mathbf { R } ^ { n }$ is called the cotangent vector space to $\mathbf { R } ^ { n }$ at $x$ consisting of all linear functions from $T _ { x } \mathbf { R } ^ { n }$ into $\mathbf { R } ^ { n }$ . Its element is called a covector (covariant vector) or a cotangent vector to $\mathbf { R } ^ { n }$ at $x$ , and

$$
T ^ { * } ( \mathbf { R } ^ { n } ) = \bigcup _ { x \in \mathbf { R } ^ { n } } T _ { x } ^ { * } \mathbf { R } ^ { n }
$$

is called the cotangent bundle.

The cotangent bundle projection:

$$
\pi ^ { * } : T ^ { * } ( \mathbf { R } ^ { n } ) \longrightarrow \mathbf { R } ^ { n }
$$

is similarly defined :

$$
\pi ^ { * } ( \omega _ { x } ) = x , \quad \forall \omega _ { x } \in T _ { x } ^ { * } \mathbf { R } ^ { n } .
$$

We now introduce a natural topological structure into $T ^ { * } \mathbf { R } ^ { n }$ . The element in $T ^ { * } \mathbf { R } ^ { n }$ can be represented as a vector consisting of $2 n$ components $( q _ { 1 } , \cdot \cdot \cdot , q _ { n } , p _ { 1 } , \cdot \cdot \cdot ,$ $p _ { n } )$ , where $( q _ { 1 } , \boldsymbol { \cdot } \boldsymbol { \cdot } \boldsymbol { \cdot } , q _ { n } ) ^ { \prime } \in \mathbf { R } ^ { n } , ( p _ { 1 } , \boldsymbol { \cdot } \boldsymbol { \cdot } \boldsymbol { \cdot } , p _ { n } ) ^ { \prime } \in T _ { q } ^ { * } \mathbf { R } ^ { n }$ , viewed as $\mathbf { R } ^ { n }$ . Thus, topology in $T ^ { * } \mathbf { R } ^ { n }$ is the product topology in $\mathbf { R } ^ { n } \times \bar { \mathbf { R } } ^ { n }$ . $T ^ { * } \mathbf { R } ^ { n }$ equipped with such a topology forms a $2 n$ -dimensional manifold.

For any tangent space $T _ { x } \mathbf { R } ^ { n }$ to $\mathbf { R } ^ { n }$ at $x$ denoted by $T _ { x } \mathbf { R } ^ { n } = \{ ( x , \xi ) | \xi \in \mathbf { R } ^ { n } \}$ , the set of all $k$ -forms on $T _ { x } \mathbf { R } ^ { n }$ is denoted by $\Lambda ^ { k } ( T _ { x } \mathbf { R } ^ { n } )$ .

$\operatorname { \mathrm { \Large ~ \Lambda } } ^ { k } ( \mathbf { R } ^ { n } ) \ = \ \bigcup _ { x \in \mathbf { R } ^ { n } } \Lambda ^ { k } ( T _ { x } \mathbf { R } ^ { n } )$ is called the exterior $k$ -forms bundle on $\mathbf { R } ^ { n }$ . The direct sum $\Lambda ^ { n } ( \mathbf { R } ^ { n } )$ Rof $k$ -form bundles $\Lambda ^ { k } ( \mathbf { R } ^ { n } ) ( k = 0 , 1 , \cdots , n )$ ,

$$
\Lambda ( { \bf R } ^ { n } ) = \Lambda ^ { 0 } ( { \bf R } ^ { n } ) { + } \Lambda ^ { 1 } ( { \bf R } ^ { n } ) { + } \dots { + } \Lambda ^ { n } ( { \bf R } ^ { n } )
$$

is called the bundle of exterior forms on $\mathbf { R } ^ { n }$ ( where $\Lambda ^ { 0 } ( \mathbf { R } ^ { n } ) = \mathbf { R } ^ { n } .$ ).

Definition 4.1. A differential $k$ -form is a mapping $\omega : \mathbf { R } ^ { n } \to \Lambda ^ { k } ( \mathbf { R } ^ { n } )$ , such that $\omega ( x ) \in \Lambda ^ { k } ( T _ { x } \mathbf { R } ^ { n } )$ . If $\varphi _ { 1 } ( x ) , \cdots , \varphi _ { n } ( x )$ is the dual basis to $( e _ { 1 } ) _ { x } , \cdot \cdot \cdot , ( e _ { n } ) _ { x }$ on $\mathbf { R } ^ { n }$ , then

$$
\omega ( x ) = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } \cdots i _ { k } } ( x ) \varphi _ { i _ { 1 } } ( x ) \wedge \cdots \wedge \varphi _ { i _ { k } } ( x ) ,
$$

where $a _ { i _ { 1 } \cdots i _ { k } } ( x ) \in { \mathcal { F } } ( \mathbf { R } ^ { k } )$ , the totality of functions on $\mathbf { R } ^ { n }$

$\omega$ is called continuous, differentiable, etc., if $a _ { i _ { 1 } \cdots i _ { k } }$ is continuous, differentiable ketc., respectively. From now on, we shall assume that forms that are differentiable will always mean $( C ^ { \infty } )$ .

The set of all differentiable $k$ -differential forms on $\mathbf { R } ^ { n }$ is denoted by $\Omega ^ { k } ( \mathbf { R } ^ { n } )$ , in particular $\Omega ^ { 0 } ( \mathbf R ^ { n } ) = C ^ { \infty } ( \mathbf R ^ { n } ) . \forall \omega _ { 1 } , \omega _ { 2 } \in \Omega ^ { k } ( \mathbf R ^ { n } ) , f \in C ^ { \infty } ( \mathbf R ^ { n } )$ , define:

$$
\begin{array} { c } { { ( \omega _ { 1 } + \omega _ { 2 } ) ( x ) = \omega _ { 1 } ( x ) + \omega _ { 2 } ( x ) , } } \\ { { { } } } \\ { { ( f \omega ) ( x ) = f ( x ) \cdot \omega ( x ) . } } \end{array}
$$

Then, $\Omega ^ { \infty } ( \mathbf { R } ^ { n } )$ forms a $C ^ { \infty } ( \mathbf { R } ^ { n } )$ -module, i.e., vector space over a ring. $\forall \omega ^ { k } \in$ $\Omega ^ { k } ( { \mathbf { R } } ^ { n } ) , \omega ^ { l } \in \Omega ^ { l } ( { \mathbf { R } } ^ { n } )$ , define their exterior product $\omega ^ { k } \wedge \omega ^ { l } \in \Omega ^ { k + l } ( \mathbf { R } ^ { n } )$ as

$$
( \omega ^ { k } \wedge \omega ^ { l } ) ( x ) = \omega ^ { k } ( x ) \wedge \omega ^ { l } ( x ) .
$$

By this formula, we have:

$$
f \cdot \omega = f \wedge \omega , \quad f \in C ^ { \infty } ( \mathbf { R } ^ { n } ) \quad ( = \Omega ^ { 0 } ( \mathbf { R } ^ { n } ) ) .
$$

By the Theorem 3.24, the exterior product of differential forms defined above is distributive, skew-symmetric, and associative.

If $f : \mathbf { R } ^ { n }  \mathbf { R }$ is differentiable, then $\mathsf { D } f ( x ) \in \Lambda ^ { 1 } ( \mathbf { R } ^ { n } )$ , where $ Ḋ \mathrm Ḋ f Ḍ Ḍ$ is the derivative of $f ( x )$ at $x$ . Thus, we get a differential 1-form $\mathrm { d } f \in \Omega ^ { 1 } ( \mathbf { R } ^ { n } )$ , defined as

$$
\mathrm { d } f ( \xi _ { x } ) =  { \mathbf Ḋ f Ḍ } ( x ) \xi = \sum _ { i = 1 } ^ { n } D _ { i } f ( x ) \xi _ { i } , \quad \xi = \sum \xi _ { i } e _ { i } .
$$

Replacing $f$ with $x ^ { i }$ for any $x = ( x ^ { 1 } , \cdot \cdot \cdot , x ^ { i } , \cdot \cdot \cdot , x ^ { n } )$ yields:

$$
\mathrm { d } x ^ { i } ( \xi _ { x } ) = \mathrm { D } x ^ { i } ( \xi ) = \xi _ { i } ,
$$

or

$$
\mathrm { d } x ^ { i } ( ( e _ { j } ) _ { x } ) = \mathrm { D } x ^ { i } ( e _ { j } ) = \delta _ { i j } .
$$

Thus, $\mathrm { d } x ^ { 1 } , \cdots , \mathrm { d } x ^ { n }$ form the dual basis to $( e _ { 1 } ) _ { x } , \cdots , ( e _ { n } ) _ { x } . \forall \omega \in \Omega ^ { k } ( \mathbf { R } ^ { n } )$ , $\omega$ can be written as

$$
\omega ( x ) = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } \cdots i _ { k } } ( x ) \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } ,
$$

where $a _ { i _ { 1 } \cdots i _ { k } } ( x ) \in C ^ { \infty } ( \mathbf { R } ^ { n } )$

kRepresented by $\mathrm { d } x ^ { 1 } , \cdots , \mathrm { d } x ^ { n }$ , the differential $\mathrm { d } f$ 1-form is

$$
\mathrm { d } f = \operatorname { D } _ { 1 } f \mathrm { d } x ^ { 1 } + \cdot \cdot \cdot + \operatorname { D } _ { n } f \mathrm { d } x ^ { n }
$$

or in a classical notation

$$
\mathbf { d } f = { \frac { \partial f } { \partial x ^ { 1 } } } \mathrm { d } x ^ { 1 } + \cdots + { \frac { \partial f } { \partial x ^ { n } } } \mathrm { d } x ^ { n } ,
$$

since

$$
\mathrm { d } f ( \xi _ { x } ) =  { \mathbf { D } } f ( x ) ( \xi ) = \sum _ { i = 1 } ^ { n } \xi _ { i }  { \mathbf { D } } _ { i } f = \sum _ { i = 1 } ^ { n }  { \mathbf { D } } _ { i } f \mathrm { d } x ^ { i } ( \xi _ { x } ) , \quad \forall \xi _ { x } \in T _ { x }  { \mathbf { R } } ^ { n } .
$$

Theorem 4.2. Every differential $k$ -form on the space $\mathbf { R } ^ { n }$ with $a$ given coordinate system $x _ { 1 } , \cdots , x _ { n }$ can be represented uniquely in the form

$$
\omega ^ { k } = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } \cdots i _ { k } } ( x ) \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } ,
$$

where the $a _ { i _ { 1 } \cdots i _ { k } } ( x )$ are smooth functions on $\mathbf { R } ^ { n }$ .

As a particular case of Theorem 4.2, let $k = 1$ . Thus, we have:

Theorem 4.3. Every differential 1-form on the space $\mathbf { R } ^ { n }$ with a given coordinate system $x _ { 1 } , \cdots , x _ { n }$ can be represented uniquely with smooth function $a _ { i } ( x )$ as follows:

$$
\omega = a _ { 1 } ( x ) \mathrm { d } x ^ { 1 } + \cdot \cdot \cdot + a _ { n } ( x ) \mathrm { d } x ^ { n } .
$$

Example 4.4. Calculate the value of the forms $\omega = \mathrm { d } r ^ { 2 } ( r ^ { 2 } = ( x ^ { 1 } ) ^ { 2 } + ( x ^ { 2 } ) ^ { 2 } )$ on the vectors $\xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 }$ . (Fig. 4.1), the results in full in the Table 4.1.

![](images/a30e2cbb407003e94150c39c57d99c83b29217efa76ad7695595b5aa0a6abe4a.jpg)  
Fig. 4.1. Example 4.4 graphical representations

Table 4.1. Example 4.4 table representations   

<table><tr><td></td><td>m1</td><td>2</td><td>3</td></tr><tr><td>W1</td><td>0</td><td>-1</td><td>1</td></tr><tr><td>W2</td><td>0</td><td>-2</td><td>一 -2</td></tr><tr><td>W3</td><td>0</td><td>18</td><td>0</td></tr></table>

For example, calculate the value of $\omega _ { 3 }$ in vectors $\xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 }$ as follows:

$$
\begin{array} { r l } & { \omega _ { 3 } ( x ) ( \xi _ { i } ) = \mathrm { d } r ^ { 2 } = 2 x ^ { 1 } \mathrm { d } x ^ { 1 } + 2 x ^ { 2 } \mathrm { d } x ^ { 2 } , } \\ & { \omega _ { 3 } ( x ) ( \xi _ { 1 } ) = 2 \cdot 0 \cdot \mathrm { d } x ^ { 1 } ( \xi _ { 1 } ) + 2 \cdot 0 \cdot \mathrm { d } x ^ { 2 } ( \xi _ { 1 } ) = 0 , } \\ & { \omega _ { 3 } ( x ) ( \xi _ { 2 } ) = 2 \cdot 2 \cdot \mathrm { d } x ^ { 1 } ( \xi _ { 2 } ) + 2 \cdot 2 \cdot \mathrm { d } x ^ { 2 } ( \xi _ { 2 } ) = 4 \times ( - 1 ) + 4 \times ( - 1 ) = - 8 , } \\ & { \omega _ { 3 } ( x ) ( \xi _ { 3 } ) = 2 \cdot 2 \cdot \mathrm { d } x ^ { 1 } ( \xi _ { 3 } ) + 2 \cdot 2 \cdot \mathrm { d } x ^ { 2 } ( \xi _ { 3 } ) = 4 \times 1 + 4 \times ( - 1 ) = 0 . } \end{array}
$$

Example 4.5. Calculate $\omega _ { 1 } = \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 }$ , $\omega _ { 2 } = x ^ { 1 } \mathrm { d } x ^ { 3 } \wedge \mathrm { d } x ^ { 2 } - x ^ { 2 } \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 1 }$ , and $\omega _ { 3 } =$ $r \mathrm { d } r \wedge \mathrm { d } \varphi ( x _ { 1 } = r \cos \varphi , \ x _ { 2 } = r \sin \varphi )$ in vectors $( \xi _ { 1 } , \eta _ { 1 } ) , ~ ( \xi _ { 2 } , \eta _ { 2 } )$ , and $( \xi _ { 3 } , \eta _ { 3 } )$ (see Fig. 4.2), result as follows:

Table 4.2. Example 4.5 table representations   

<table><tr><td></td><td>(1，n1）</td><td>(2,2)</td></tr><tr><td>W1</td><td>1</td><td>1</td></tr><tr><td>W2</td><td>2</td><td>1</td></tr><tr><td>W3</td><td>1</td><td>1</td></tr></table>

![](images/19d133bb07d5041635944eca7306d31461814f5e964370b0c5792608f683d837.jpg)  
Fig. 4.2. Example 4.5 graphical representations

Example 4.6. Calculate the value of the forms $\omega _ { 1 } = \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 }$ , $\omega _ { 2 } = x ^ { 1 } \mathrm { d } x ^ { 3 } \wedge$ ${ \mathrm { d } } x ^ { 2 }$ , $\omega _ { 3 } = \mathrm { d } x ^ { 3 } \wedge \mathrm { d } r ^ { 2 }$ on the vectors $\xi , \eta$ at the point $x$ , where $r ^ { 2 } = ( x ^ { 1 } ) ^ { 2 } + ( x ^ { 2 } ) ^ { 2 } +$ $( x ^ { 3 } ) ^ { 2 } , \xi = ( 1 , 1 , 1 ) ^ { \prime }$ , $\eta = ( 1 , 2 , 3 ) ^ { \prime }$ , $x = ( 2 , 0 , 0 )$ .

The detailed calculation is shown bellow as follows:

$$
\begin{array} { r l } & { \omega _ { 1 } ( \xi , \eta ) = \mathrm { d } { x ^ { 2 } } \wedge \mathrm { d } { x ^ { 3 } } ( \xi , \eta ) = \left| \begin{array} { l l } { \mathrm { d } { x ^ { 2 } } ( \xi ) } & { \mathrm { d } { x ^ { 3 } } ( \xi ) } \\ { \mathrm { d } { x ^ { 2 } } ( \eta ) } & { \mathrm { d } { x ^ { 3 } } ( \eta ) } \end{array} \right| = \left| \begin{array} { l } { 1 } \\ { 2 } \end{array} \right. } \\ & { \omega _ { 2 } ( \xi , \eta ) = 2 \cdot \mathrm { d } { x ^ { 3 } } \wedge \mathrm { d } { x ^ { 2 } } ( \xi , \eta ) = - 2 \omega _ { 1 } ( \xi , \eta ) = - 2 , } \\ & { \omega _ { 3 } ( \xi , \eta ) = \mathrm { d } { x ^ { 3 } } \wedge \mathrm { d } { y ^ { 2 } } ( \xi , \eta ) } \\ & { \qquad \quad = \mathrm { d } { x ^ { 3 } } \wedge ( 2 { x ^ { 1 } } \mathrm { d } { x ^ { 1 } } + 2 { x ^ { 2 } } \mathrm { d } { x ^ { 2 } } + 2 { x ^ { 3 } } \mathrm { d } { x ^ { 3 } } ) ( \xi , \eta ) } \\ & { \qquad \quad = 2 { x ^ { 1 } } \mathrm { d } { x ^ { 3 } } \wedge \mathrm { d } { x ^ { 1 } } ( \xi , \eta ) - 2 { x ^ { 2 } } \mathrm { d } { x ^ { 2 } } \wedge \mathrm { d } { x ^ { 3 } } ( \xi , \eta ) } \\ & { \qquad \quad = 2 \cdot 2 \cdot \mathrm { d } { x ^ { 3 } } \wedge \mathrm { d } { x ^ { 1 } } ( \xi , \eta ) - 2 \cdot 0 \cdot \mathrm { d } { x ^ { 2 } } \wedge \mathrm { d } { x ^ { 3 } } ( \xi , \eta ) } \\ & { \qquad \quad = 4 \left| \begin{array} { l l } { \mathrm { d } { x ^ { 3 } } ( \xi ) } & { \mathrm { d } { x ^ { 1 } } ( \xi ) } \\ { \mathrm { d } { x ^ { 3 } } ( \eta ) } & { \mathrm { d } { x ^ { 1 } } ( \eta ) } \end{array} \right| = 4 \left| \begin{array} { l l } { 1 } & { 1 } \\ { 3 } & { 1 } \end{array} \right| = - 8 . } \end{array}
$$

# 1.4.2 The Behavior of Differential Forms under Maps

First, we consider the behavior of differential forms under maps. Let $f : \mathbf { R } ^ { n }  \mathbf { R } ^ { m }$ be a differential mapping. $ Ḋ \mathrm Ḋ f Ḍ Ḍ ( x )$ is the linear transformation from $\mathbf { R } ^ { n }$ to $\mathbf { R } ^ { m }$ , which is the derivative of $f$ , and $\mathsf { D } F ( x ) = \frac { \partial f ^ { i } } { \partial x _ { j } }$ the Jacobian of $f$ at $x$ . It induces a linear transformation $f _ { * }$ from the tangent space $T _ { x } \mathbf { R } ^ { n }$ to $\mathbf { R } ^ { n }$ at $x$ into the tangent space $T _ { f ( x ) } \mathbf { R } ^ { m }$ to $\mathbf { R } ^ { m }$ at $f ( x )$ , i.e.,

$$
f _ { * } ( \xi _ { x } ) = ( \mathrm { D } f ( x ) ( \xi ) ) _ { f ( x ) } , \quad \forall \xi _ { x } \in T _ { x } \mathbf { R } ^ { n } .
$$

Definition 4.7. Let $f ^ { * } : \Omega ^ { k } ( T _ { f ( x ) } \mathbf { R } ^ { m } )  \Omega ^ { k } ( T _ { x } \mathbf { R } ^ { n } )$ be a linear map:

$$
( f ^ { * } \omega ( x ) ) ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k } ) = \omega ( f ( x ) ) ( f _ { * } \xi _ { 1 } , \cdot \cdot \cdot , f _ { * } \xi _ { k } ) , \quad \xi _ { i } \in T _ { x } \mathbf { R } ^ { n } .
$$

$f ^ { * }$ can be expanded on $\Omega ^ { k } ( \mathbf { R } ^ { m } )$

$$
( f ^ { * } \omega ) ( x ) = f ^ { * } \omega ( x ) .
$$

$f ^ { * } \omega$ is called the pull-back of $\omega$ under $f$ , which is the dual transformation of $f _ { * }$ .

$$
\begin{array} { r l } { { \mathrm { e o r e m ~ } 4 . 8 . } } & { { \displaystyle { L e t } ~ f : { \bf R } ^ { n }  { \bf R } ^ { m } , ~ h : { \bf R } ^ { m }  { \bf R } ^ { l } , f , h \in C ^ { \infty } . T h e n } , } \\ { { \mathrm { 1 } ^ { \circ } } } & { { \displaystyle f ^ { * } ( \mathrm { d } y ^ { i } ) = \sum _ { j = 1 } ^ { n } \frac { \partial f ^ { i } } { \partial x ^ { j } } \mathrm { d } x ^ { j } . } } \\ { { \mathrm { 2 } ^ { \circ } } } & { { \displaystyle f ^ { * } ( \omega _ { 1 } + \omega _ { 2 } ) = f ^ { * } \omega _ { 1 } + f ^ { * } \omega _ { 2 } . } } \\ { { \mathrm { 3 } ^ { \circ } } } & { { \displaystyle f ^ { * } ( \omega \wedge \eta ) = f ^ { * } \omega \wedge f ^ { * } \eta . } } \\ { { \mathrm { 4 } ^ { \circ } } } & { { \displaystyle f ^ { * } ( g \cdot \omega ) = ( g \circ f ) \cdot f ^ { * } \omega , ~ \forall g \in C ^ { \infty } ( { \bf R } ^ { m } ) . } } \\ { { \mathrm { 5 } ^ { \circ } } } & { { \displaystyle ( h \circ f ) ^ { * } = f ^ { * } \circ h ^ { * } } . } \end{array}
$$

Proof. The proof is not difficult. We only prove $1 ^ { \circ }$ , $4 ^ { \circ }$ and $5 ^ { \circ } . \forall \xi _ { x } \in T _ { x } \mathbf { R } ^ { n }$ ,

$$
\begin{array} { r c l } { f ^ { * } ( \mathbb { d } y ^ { i } ) ( \xi _ { x } ) } & { = } & { \mathbb { d } x ^ { i } ( f _ { * } \xi _ { x } ) = ( f _ { * } \xi ) _ { i } } \\ & & { = } & { \displaystyle \sum _ { j = 1 } ^ { n } \frac { \partial f ^ { i } } { \partial x ^ { j } } \xi _ { j } = \sum _ { j = 1 } ^ { n } \frac { \partial f ^ { i } } { \partial x ^ { j } } \mathbb { d } x ^ { j } ( \xi _ { x } ) . } \end{array}
$$

Thus, we have

$$
f ^ { * } ( \mathrm { d } y ^ { i } ) = \sum _ { j = 1 } ^ { n } { \frac { \partial f ^ { i } } { \partial x ^ { j } } } \mathrm { d } x ^ { j } .
$$

The theorem is proved.

Example 4.9. Let $y = f ( x ^ { 1 } , x ^ { 2 } ) = ( x ^ { 1 } ) ^ { 2 } + ( x ^ { 2 } ) ^ { 2 } , \omega = \mathrm { d } y ,$

$$
\begin{array} { r l } { f ^ { * } \omega } & { = \mathbf { d } x ( f _ { * } \xi _ { x } ) = \displaystyle \frac { \partial f } { \partial x ^ { 1 } } \mathbf { d } x ^ { 1 } ( \xi _ { x } ) + \frac { \partial f } { \partial x ^ { 2 } } \mathbf { d } x ^ { 2 } ( \xi _ { x } ) } \\ & { = 2 x ^ { 1 } \mathbf { d } x ^ { 1 } + 2 x ^ { 2 } \mathbf { d } x ^ { 2 } . } \end{array}
$$

Before proving $4 ^ { \circ }$ , let us understand the following theorem.

Theorem 4.10. Let $f = ( f ^ { 1 } , \cdot \cdot \cdot , f ^ { m } ) ^ { \prime } = ( y ^ { 1 } , \cdot \cdot \cdot , y ^ { m } )$ , $f : \mathbf { R } ^ { n }  \mathbf { R } ^ { m }$ be a differentiable mapping with Jacobian $\left( { \frac { \partial f ^ { i } } { \partial x ^ { j } } } \right) _ { m \times n } = \left( { \frac { \partial y ^ { i } } { \partial x ^ { j } } } \right) _ { m \times }$ . For $\omega \in \Omega ^ { k } ( \mathbf { R } ^ { m } )$ ,

$$
\omega = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } , \cdots , i _ { k } } ( y ) \mathrm { d } y ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } y ^ { i _ { k } } ,
$$

we have

$$
f ^ { * } \omega = \sum _ { i _ { 1 } < \cdots < i _ { k } ; ~ j _ { 1 } < \cdots < j _ { k } } a _ { i _ { 1 } , \cdots , i _ { k } } ( f ( x ) ) \Delta \left[ \begin{array} { l l l } { { i _ { 1 } } } & { { \cdots } } & { { i _ { k } } } \\ { { j _ { 1 } } } & { { \cdots } } & { { j _ { k } } } \end{array} \right] \mathrm { d } x ^ { j _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { j _ { k } } ,
$$

$$
w h e r e \Delta \left[ \begin{array} { c c c } { i _ { 1 } } & { \cdots } & { i _ { k } } \\ { j _ { 1 } } & { \cdots } & { j _ { k } } \end{array} \right] i s t h e \left[ \begin{array} { c c c } { i _ { 1 } } & { \cdots } & { i _ { k } } \\ { j _ { 1 } } & { \cdots } & { j _ { k } } \end{array} \right] - m i n o r o f m a t r i x \left( \frac { \partial y ^ { i } } { \partial x ^ { j } } \right) _ { j = 1 , \cdots , n }
$$

Proof.

$$
\begin{array} { r l }  \Gamma ^ { \prime } ( \mathbf { S } ^ { \prime } ) = \mathcal { P } ^ { \prime } ( \underset { \mathbf { x } \in \mathbb { R } _ { n + 1 } } { \sum ^ { \infty } } \omega _ { \mathbf { x } , - \mathbf { x } , - \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } ) } \\  \Gamma ^ { \prime } ( \mathbf { S } ^ { \prime } ) = \mathcal { P } ^ { \prime } ( \underset { \mathbf { x } \in \mathbb { R } _ { n + 1 } } { \sum ^ { \infty } } \omega _ { \mathbf { x } , \mathbf { x } , - \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } ) } \\  = \mathcal { P } ^ { \prime } ( \underset { \mathbf { x } \in \mathbb { R } _ { n + 1 } } { \sum ^ { \infty } } \omega _ { \mathbf { x } , \mathbf { x } , - \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } ) } \\  = \mathcal { P } ^ { \prime } ( \underset { \mathbf { x } \in \mathbb { R } _ { n + 1 } } { \sum ^ { \infty } } \omega _ { \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } ) } \\  = \mathcal { P } ^ { \prime } ( \underset { \mathbf { x } \in \mathbb { R } _ { n + 1 } } { \sum ^ { \infty } } \omega _  \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x } , \mathbf { x }  \end{array}
$$

The following deduction gives the proof for $4 ^ { \circ }$ .

Proof. If $f : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ is differentiable, then

$$
f ^ { * } ( g \mathrm { d } x ^ { 1 } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { n } ) = g \circ f \operatorname* { d e t } { ( f ^ { \prime } ) } \mathrm { d } x ^ { 1 } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { n } ,
$$

where $f ^ { \prime } = \mathrm { D } f = \left( { \frac { \partial f ^ { i } } { \partial x ^ { j } } } \right)$

For proof of $5 ^ { \circ }$ :

Proof.

$$
\begin{array} { r l } { [ f ^ { * } ( h ^ { * } \omega ) ] ( x ) ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { p } ) = } & { ( h ^ { * } \omega ) ( f ( x ) ) ( f _ { * } \xi _ { 1 } , \cdot \cdot \cdot , f _ { * } \xi _ { p } ) } \\ { = } & { \omega ( h ( f ( x ) ) ) ( h _ { * } f _ { * } \xi _ { 1 } , \cdot \cdot \cdot , h _ { * } f _ { * } \xi _ { p } ) } \\ { = } & { \omega ( h \circ f ) ( x ) ( ( h f ) _ { * } \xi _ { 1 } , \cdot \cdot \cdot , ( h f ) _ { * } \xi _ { p } ) } \\ { = } & { [ ( h \circ f ) ^ { * } \omega ] ( x ) ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { p } ) . } \end{array}
$$

Therefore, $( h \circ f ) ^ { * } = f ^ { * } \circ h ^ { * }$ .

# 1.4.3 Exterior Differential

We now define an operator similar to differentiation in classical mathematical analysis. We have introduced the function differential on the manifold, namely if $f \in C ^ { \infty } ( \mathbf { R } ^ { n } )$ , and $\mathbf { d } f | _ { x } \in \mathbf { \Gamma } T _ { x } \mathbf { R } ^ { n }$ , then $\mathrm { d } f$ is a 1-form on $\mathbf { R } ^ { n }$ . Therefore, we may say operator $\mathbf { d } : \Omega ^ { 0 } ( \mathbf { R } ^ { n } ) \to \Omega ^ { 1 } ( \mathbf { R } ^ { n } )$ maps the 0-form defined on $\mathbf { R } ^ { n }$ onto the 1-form on $\mathbf { R } ^ { n }$ . We need to extend this operator to the exterior algebra $\Omega ( \mathbf { R } ^ { n } )$ on $M$ .

Definition 4.11. The exterior differential operator d on an exterior algebra $\omega ( \mathbf { R } ^ { n } )$ of manifold $M$ is a mapping

$$
\begin{array} { r } { \mathbf { d } : \Omega ^ { k } ( { \mathbf { R } ^ { n } } ) \longrightarrow \Omega ^ { k + 1 } ( { \mathbf { R } ^ { n } } ) , } \end{array}
$$

where $k = 0 , 1 , \cdots , n$ .

Exterior algebra may be represented by the local coordinate system of $M$ as

$$
\omega = \sum _ { 1 \leq i _ { 1 } < \cdots < i _ { k } \leq n } a _ { i _ { 1 } , \cdots , i _ { k } } \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } ,
$$

which is a $k$ -form. Then,

$$
\begin{array} { r l } { \mathrm { d } \omega } & { = \displaystyle \sum _ { 1 \leq i _ { 1 } < \cdots < i _ { k } \leq n } \mathrm { d } a _ { i _ { 1 } , \cdots , i _ { k } } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & { = \displaystyle \sum _ { 1 \leq i _ { 1 } < \cdots < i _ { k } \leq n } \displaystyle \sum _ { j = 1 } ^ { n } \frac { \partial a _ { i _ { 1 } , \cdots , i _ { k } } } { \partial x ^ { j } } \mathrm { d } x ^ { j } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } . } \end{array}
$$

Here ${ \mathrm { d } }$ is called an exterior differential operator.

In particular, if $\omega = f \in \Omega ^ { 0 } ( \mathbf { R } ^ { n } ) = C ^ { \infty } ( \mathbf { R } ^ { n } )$ , then

$$
\mathrm { d } \omega = \sum _ { j = 1 } ^ { n } \frac { \partial f } { \partial x ^ { j } } \mathrm { d } x ^ { j } .
$$

From this, we can see that when $\omega \in \Omega ^ { n } ( \mathbf { R } ^ { n } ) , \mathrm { d } \omega = 0$ .

Theorem 4.12. Exterior differential operator d has the following properties:

$1 ^ { \circ }$ $\mathrm { d } ( \omega + \eta ) = \mathrm { d } \omega + \mathrm { d } \eta$ .   
$2 ^ { \circ }$ $\forall \omega ^ { k } \in \Omega ^ { k } , \omega ^ { l } \in \Omega ^ { l } ,$ , has $\mathrm { d } ( \omega ^ { k } \wedge \omega ^ { l } ) = \mathrm { d } \omega ^ { k } \wedge \omega ^ { l } + ( - 1 ) ^ { k } \omega ^ { k } \wedge \mathrm { d } \omega ^ { l } .$ $3 ^ { \circ }$ $\mathrm { d } ( \mathrm { d } \omega ) = 0$ or in simple form $\mathrm { d } ^ { 2 } \omega = 0$ .   
$4 ^ { \circ }$ $f ^ { * } \mathrm { d } \omega = \mathrm { d } f ^ { * } \omega$ .

Proof. $1 ^ { \circ }$ The proof is obvious.

$2 ^ { \circ }$ Let

$$
\begin{array} { l } { { \displaystyle \omega ^ { k } ( x ) = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } , \cdots , i _ { k } } \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } , } } \\ { { \displaystyle \omega ^ { l } ( x ) = \sum _ { j _ { 1 } < \cdots < j _ { l } } b _ { j _ { 1 } , \cdots , j _ { l } } \mathrm { d } x ^ { j _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { j _ { l } } . } } \end{array}
$$

Then,

$$
\omega ^ { k } \wedge \omega ^ { l } = \sum _ { \substack { i _ { 1 } < \cdots < i _ { k } ; j _ { 1 } < \cdots < j _ { l } } } a _ { i _ { 1 } , \cdots , i _ { k } } ( x ) b _ { j _ { 1 } , \cdots , j _ { l } } ( x ) \mathrm { d } x ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { i _ { k } } \wedge \mathrm { d } x ^ { j _ { 1 } } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { j _ { l } }
$$

By definition,

$$
\begin{array} { r l } & { \mathrm { d } ( \omega ^ { k } \wedge \omega ^ { i } ) = \underset { \mathrm { i } \leq \cdots < k \leq i \leq 1 } { \sum } \underset { \substack { \hat { x } = \cdots < k \leq i \leq 1 } } \overset { \mathbb { P } } { \underset { \mathrm { i } \leq i \leq 1 } { \sum } } \frac { \partial ( \omega ^ { k } ) } { \partial x ^ { i } } \mathrm { d } \hat { x } ^ { i } \wedge \mathrm { d } \hat { x } ^ { i } \wedge \cdots \wedge \mathrm { d } \hat { x } ^ { i } \wedge \mathrm { d } \hat { x } ^ { i } \wedge \cdots \wedge \mathrm { d } \hat { x } ^ { i } } \\ & { \stackrel { } { = } } \\ & { \underset { \mathrm { i } \leq \cdots < k \leq i \leq 1 } { \sum } \underset { \substack { \hat { x } = \cdots < k \leq i \leq 1 } } ( \overset { \mathbb { P } } { \underset { \mathrm { i } \leq i \leq 1 } { \sum } } b _ { i - i \cdot i \cdot i } \frac { \partial A _ { i - 1 \cdot i \cdot i \cdot i } } { \partial x ^ { i } } + a _ { 1 \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i }  } \\ & {  \qquad \mathrm { i } \underset { \mathrm { i } \leq i \leq 1 } { \sum } b _ { i } ^ { i } \wedge \cdots \wedge \mathrm { d } \hat { x } ^ { i } \wedge \mathrm { d } \hat { x } ^ { i } \qquad } \\ &  \stackrel { } { = } \underset { \mathrm { i } \leq i \leq 1 } { \sum } \underset { \substack { \hat { x } = \cdots < k \leq i \leq 1 } } \overset { \mathbb { P } } { \underset { \mathrm { i } \leq i \leq i \leq 1 } { \sum } } \partial _  i \leq 1 \cdots i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \cdot i \ \end{array}
$$

$3 ^ { \circ }$ The proof is as follows:

$$
\begin{array} { r l } { { \bf d } ( \mathrm { d } \omega ) } & { = \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \displaystyle \sum _ { i , j = 1 } ^ { n } \frac { \partial ^ { 2 } a } { \partial x ^ { i } \partial x ^ { j } } \mathrm { d } x ^ { i } \wedge \mathrm { d } x ^ { j } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & { = \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \displaystyle \sum _ { i < j } \left( \frac { \partial ^ { 2 } a } { \partial x ^ { i } \partial x ^ { j } } - \frac { \partial ^ { 2 } a } { \partial x ^ { j } \partial x ^ { i } } \right) \mathrm { d } x ^ { i } \wedge \mathrm { d } x ^ { j } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & { = 0 , } \end{array}
$$

since

$$
{ \frac { \partial ^ { 2 } a } { \partial x ^ { i } \partial x ^ { j } } } = { \frac { \partial ^ { 2 } a } { \partial x ^ { j } \partial x ^ { i } } } .
$$

$4 ^ { \circ }$ By Theorem 4.8, $1 ^ { \circ } \forall \omega = g \in C ^ { \infty } ( \mathbf { R } ^ { n } )$ , we have:

$$
\begin{array} { r l } { f ^ { * } \mathrm { d } g = } & { f ^ { * } \left( \displaystyle \sum _ { i = 1 } ^ { m } \frac { \partial g } { \partial y ^ { i } } \mathrm { d } y ^ { i } \right) = \displaystyle \sum _ { i = 1 } ^ { m } \frac { \partial g } { \partial y ^ { i } } \circ f \cdot f ^ { * } ( \mathrm { d } y ^ { i } ) } \\ { = } & { \displaystyle \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { m } \frac { \partial g ( f ( x ) ) } { \partial y ^ { i } } \cdot \frac { \partial f ^ { i } } { \partial x ^ { j } } \mathrm { d } x ^ { j } } \\ { = } & { \displaystyle \sum _ { j = 1 } ^ { n } \frac { \partial g ( f ( x ) ) } { \partial x ^ { j } } \mathrm { d } x ^ { j } = \mathrm { d } ( g \circ f ) = \mathrm { d } f ^ { * } g . } \end{array}
$$

Furthermore, $\forall \omega \in \Omega ^ { k } ( \mathbf { R } ^ { m } )$ ,

$$
{ \begin{array} { r l r l } { f ^ { \infty } ( \mathrm { d } \omega ) } & { = f ^ { * } \left( \displaystyle \sum _ { i _ { 1 } < i < s < k _ { \perp } } \displaystyle \sum _ { k = 1 } ^ { m } { \frac { \partial } { \partial \partial g } } \mathrm { d } y ^ { k } \cdot \mathrm { A d } y ^ { * } \wedge \dots \cdot \mathrm { A d } y ^ { * } \right) } \\ & { = f ^ { * } \left( \displaystyle \sum _ { i _ { 1 } < i < s < k _ { \perp } } \mathrm { d } \alpha \cdot \mathrm { A d } y ^ { k _ { \perp } ^ { \infty } } \wedge \dots \cdot \mathrm { A d } y ^ { k _ { \perp } ^ { \infty } } \right) } \\ & { = \displaystyle \sum _ { i _ { 1 } < i < s < k _ { \perp } } f ^ { * } ( \mathrm { d } \omega ) \wedge f ^ { * } \left( \mathrm { d } y ^ { \perp } \wedge \dots \cdot \mathrm { A d } y ^ { k _ { \perp } ^ { \infty } } \right) } \\ & { \leq \displaystyle \sum _ { i _ { 1 } < i < s < k _ { \perp } } \mathrm { d } \left( f ^ { * } \alpha \right) \wedge f ^ { * } \left( \mathrm { d } y ^ { \perp } \wedge \dots \cdot \mathrm { A d } y ^ { k _ { \perp } ^ { \infty } } \right) } \\ & { = \displaystyle \sum _ { i _ { 1 } < i < s < k _ { \perp } } \mathrm { d } \left( f ^ { * } \alpha \right) \wedge f ^ { * } \left( \mathrm { d } y ^ { \perp } \wedge \dots \cdot \mathrm { A d } y ^ { k _ { \perp } ^ { \infty } } \right) } \\ & { = \displaystyle \partial \left( \displaystyle \sum _ { i _ { 1 } < s < k _ { \perp } } f ^ { * } \alpha \cdot \mathrm { A d } y ^ { * } \left( \mathrm { d } y ^ { \perp } \wedge \dots \dots \cdot \mathrm { A d } y ^ { k _ { \perp } ^ { \infty } } \right) \right) } & & { ( \mathrm { b y } \geq s ) ^ { \prime } } \\ & { = \mathrm { d } f ^ { * } \alpha . } \end{array} }
$$

Therefore, the theorem is completed.

# 1.4.4 Poincare Lemma and Its Inverse Lemma ´

Definition 4.13. A differential form $\omega$ is closed if $\mathrm { d } \omega = 0$ , and is exact if there exists a differential form $\eta$ such that $\omega = \mathrm { d } \eta$ .

Clearly if $\omega$ is exact, then it is closed by the formula $\mathrm { d } ^ { 2 } \omega = 0$ . However, the converse is not always true. The following Poincare lemma asserts that in the neighbour- ´ hood of each point, the closed is equivalent to the exact. Before stating the Poincare´ lemma, we introduce a notion.

Definition 4.14. An open set $A \subset \mathbf { R } ^ { n }$ is star-shaped with respect to 0, if for any $x \in A$ the set $\{ \alpha x \mid \alpha \in [ 0 , 1 ] \} \subset A$ .

Evidently, $\mathbf { R } ^ { n }$ is a star-shaped open set, and every convex set containing 0 is a star-shaped open set with respect to 0.

Theorem 4.15 (Poincare lemma). ´ Let $A \subset \mathbf { R } ^ { n }$ be an open star-shaped set with respect to 0. Then, every closed form on $A$ is exact.

Proof. We will construct an $\mathbf { R }$ -linear mapping $H : \Omega ^ { k } ( A ) \to \Omega ^ { k - 1 } ( A )$ , such that $\mathbf { d } \circ H + H \circ \mathbf { d } = \mathbf { i d }$ : $\Omega ^ { k } ( A ) \to \Omega ^ { k } ( A )$ , i.e., $\omega = \mathbf { d } \circ H ( \omega ) + H \mathbf { d } \omega$ . Then, from $\mathrm { d } \omega = 0$ , if follows that $\boldsymbol { \omega } = \mathrm { d } ( H ( \boldsymbol { \omega } ) )$ . Taking $\eta = H ( \omega )$ , we get

$$
\omega = \mathrm { d } \eta .
$$

Let

$$
\omega = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } \cdots i _ { k } } ( x ) \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } .
$$

Define

$$
\begin{array} { r l } { H ( \omega ) ( x ) = } & { \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \displaystyle \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } \biggl ( \displaystyle \int _ { 0 } ^ { 1 } t ^ { k - 1 } a _ { i _ { 1 } \cdots i _ { k } } ( t x ) \mathrm { d } t x ^ { i _ { j } } } \\ & { \cdot \mathrm { d } x ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge \widehat { \mathrm { d } x ^ { i _ { j } } } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { i _ { k } } \biggr ) , } \end{array}
$$

where the symbol “  ” over ${ \mathrm { d } } x ^ { i _ { j } }$ indicates that it is omitted.

$$
\begin{array} { r l r l } { \mathrm { d } H ( \omega ) } & { = } & { \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \displaystyle \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } ( \int _ { 0 } ^ { 1 } t ^ { k - 1 } a ( i _ { k } ) \mathrm { d } t ) \mathrm { d } x ^ { i _ { j } } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & { } & { \displaystyle + \sum _ { i _ { 1 } < \cdots < i _ { k } } \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } ( \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { 1 } t ^ { k } \frac { \partial a ( i , x ) } { \partial x ^ { i } } \mathrm { d } x ^ { i _ { 1 } } \mathrm { d } x ^ { i _ { 2 } } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } }  } \\ & { } & { \displaystyle = } & { k \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } ( \int _ { 0 } ^ { 1 } t ^ { k - 1 } a ( i , x ) \mathrm { d } t ) \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { j } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & { } & { \displaystyle +  \sum _ { i _ { 1 } < \cdots < i _ { k } } \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { 1 } t ^ { k } \frac { \partial a ( i , x ) } { \partial x ^ { i } } \mathrm { d } t x ^ { i _ { 1 } } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \qquad } \\ & { } & { \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { 1 } t ^ { k } \frac { \partial a ( i , x ) } { \partial x ^ { i } } \mathrm { d } t x ^ { i _ { 1 } } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \qquad } \\ & { } & { \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \mathrm { d } x ^ { i _ { k } } . } \end{array}
$$

On the other hand,

$$
\begin{array} { r l } { \mathrm { d } \omega } & { = \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \sum _ { i = 1 } ^ { n } \frac { \partial a } { \partial x ^ { i } } \mathrm { d } x ^ { i } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } , } \\ { H \mathrm { d } \omega } & { = \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \Bigg \{ \sum _ { i = 1 } ^ { n } \Big ( \int _ { 0 } ^ { 1 } t ^ { k } \frac { \partial a ( t x ) } { \partial x ^ { i } } \mathrm { d } t \Big ) x ^ { i } \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \end{array}
$$

$$
\begin{array} { l } { { + \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j } \int _ { 0 } ^ { 1 } t ^ { k } \frac { \partial a ( t x ) } { \partial x ^ { i } } \mathrm { d } t x ^ { i _ { j } } \mathrm { d } x ^ { i } \wedge \mathrm { d } x ^ { i _ { 1 } } \wedge \dots } } \\ { { \wedge \widehat { \mathrm { d } x ^ { i _ { j } } } \wedge \dots \wedge \mathrm { d } x ^ { i _ { k } } \Big \} . } } \end{array}
$$

The second term of the right hand side in this equality coincides with the second term in Equation (1.3) except for the sign. Adding them together, we get

$$
\begin{array} { r c l } { \displaystyle \mathrm { d } H ( \omega ) + H \mathrm { d } \omega } & { = } & { k \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \int _ { 0 } ^ { 1 } t ^ { k - 1 } a ( t x ) \mathrm { d } t \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & & { + \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \displaystyle \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { 1 } t ^ { k } \frac { \partial a ( t x ) } { \partial x ^ { i } } \mathrm { d } t x ^ { i } \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } } \\ & { = } & { \displaystyle \sum _ { i _ { 1 } < \cdots < i _ { k } } \int _ { 0 } ^ { 1 } \left( k t ^ { k - 1 } a ( t x ) + \displaystyle \sum _ { i = 1 } ^ { n } t ^ { k } \frac { \partial a ( t x ) } { \partial x ^ { i } } x ^ { i } \right) \mathrm { d } t \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } . } \end{array}
$$

Notice that

$$
k t ^ { k - 1 } a ( t x ) + \sum _ { i = 1 } ^ { n } t ^ { k } x ^ { i } { \frac { \partial a ( t x ) } { \partial x ^ { i } } } = { \frac { \mathrm { d } } { \mathrm { d } t } } { \big ( } t ^ { k } a ( t x ) { \big ) } .
$$

Thus,

$$
\begin{array} { r l } { \displaystyle \int _ { 0 } ^ { 1 } } & { \left( k t ^ { k - 1 } a ( t x ) + \sum _ { i = 1 } ^ { n } t ^ { k } \frac { \partial a ( t x ) } { \partial x ^ { i } } x ^ { i } \right) \mathrm { d } t } \\ { = } & { \displaystyle \int _ { 0 } ^ { 1 } \frac { \mathrm { d } } { \mathrm { d } t } \left( t ^ { k } a ( t , x ) \right) \mathrm { d } t = a ( x ) . } \end{array}
$$

Then, we have

$$
 \mathrm { d } H ( \omega ) + H \mathrm { d } \omega = \sum _ { i _ { 1 } < \cdots < i _ { k } } a _ { i _ { 1 } \cdots i _ { k } } ( x ) \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { k } } = \omega ,
$$

i.e.,

$$
\mathrm { d } H + H \mathrm { d } = \mathrm { i d } .
$$

Therefore, the theorem is completed.

# 1.4.5 Differential Form in $\mathbf { R } ^ { 3 }$

We now assume that $\mathbf { R } ^ { 3 }$ is a three-dimensional oriented Euclidean space. The square of the length element in $\mathbf { R } ^ { 3 }$ has the form

$$
\mathrm { d } s ^ { 2 } = ( \mathrm { d } x ^ { 1 } ) ^ { 2 } + ( \mathrm { d } x ^ { 2 } ) ^ { 2 } + ( \mathrm { d } x ^ { 3 } ) ^ { 2 } .
$$

For any vector $A \in \mathbf { R } ^ { 3 }$ , we define a corresponding 1-form $\omega _ { A } ^ { 1 }$ and a 2-form $\omega _ { A } ^ { 2 }$ by the formula

$$
\omega _ { A } ^ { 1 } ( \boldsymbol { \xi } ) = ( A , \boldsymbol { \xi } ) , \quad \omega _ { A } ^ { 2 } ( \boldsymbol { \xi } , \boldsymbol { \eta } ) = ( A , [ \boldsymbol { \xi } , \boldsymbol { \eta } ] ) , \quad \forall \boldsymbol { \xi } , \boldsymbol { \eta } \in { \bf R } ^ { 3 } ,
$$

where $( ~ , ~ )$ stands for usual inner product and $( ~ , ~ [ ~ ] )$ for triple scalar product.

Let $\begin{array} { r } { A = A _ { 1 } e _ { 1 } + A _ { 2 } e _ { 2 } + A _ { 3 } e _ { 3 } } \end{array}$ and $\omega _ { A } ^ { 1 } = a _ { 1 } \mathrm { d } x ^ { 1 } + a _ { 2 } \mathrm { d } x ^ { 2 } + a _ { 3 } \mathrm { d } x ^ { 3 }$ . Then by definition, on one hand, $\omega _ { A } ( e _ { j } ) = \sum _ { i = 1 } ^ { 3 } a _ { i } \mathrm { d } x ^ { 1 } ( e _ { j } ) = A _ { j }$ ; on the other hand, $\omega _ { A } ( e _ { j } ) = $ $( A , e _ { j } ) = A _ { j }$ . Thus, $a _ { j } = A _ { j }$ , i.e., $\omega _ { A } ^ { 1 } = A _ { 1 } \mathrm { d } x ^ { 1 } + A _ { 2 } \mathrm { d } x ^ { 2 } + A _ { 3 } \mathrm { d } x ^ { 3 }$ . Similarly, we can get

$$
\omega _ { A } ^ { 2 } = A _ { 1 } \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 } + A _ { 2 } \mathrm { d } x ^ { 3 } \wedge \mathrm { d } x ^ { 1 } + A _ { 3 } \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } .
$$

It is easy to observe that

$$
\omega _ { A } ^ { 2 } = ^ { * } ( \omega _ { A } ^ { 1 } ) , \quad \omega _ { A } ^ { 1 } = { } ^ { b } ( A ) .
$$

Here, the top left hand corner “\*” $( ^ { 6 6 } b ^ { 7 } )$ represents the Hodge (sharp) operator respectively, namely $\ast : \wedge ^ { k } ( \mathbf { R } ^ { m } ) \to \wedge ^ { n - k } ( \mathbf { R } ^ { m } ) ; b : \mathbf { R } \to \mathbf { R } ^ { \ast }$ .

We now introduce three operators that play an important role in classical vector analysis, i.e., gradient, curl, and divergence.

Definition 4.16. Let $f \in C ^ { \infty } ( { \bf R } ^ { 3 } )$ and $A \in \mathcal { X } ( \mathbf { R } ^ { 3 } )$ . The grad $f$ and curl $A \in \mathcal { X } ( \mathbf { R } ^ { 3 } )$ and div $( A ) \in C ^ { \infty } ( \mathbf { R } ^ { 3 } )$ defined as follows

$$
\omega _ { \mathrm { g r a d } _ { f } } ^ { 1 } = \mathrm { d } f , \quad \omega _ { \mathrm { c u r l } \ A } ^ { 2 } = \mathrm { d } \omega _ { A } ^ { 1 } , \quad \mathrm { a n d } \quad \mathrm { d } \omega _ { A } ^ { 2 } = \mathrm { d i v } A = \omega _ { A } ^ { 3 } ,
$$

where $\omega ^ { 3 } = \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 }$ is the volume element in $\mathbf { R } ^ { 3 }$ .

By this definition,

$$
\omega _ { \mathrm { g r a d } _ { f } } ^ { 1 } = \mathrm { d } f = \frac { \partial f } { \partial x ^ { 1 } } \mathrm { d } x ^ { 1 } + \frac { \partial f } { \partial x ^ { 2 } } \mathrm { d } x ^ { 2 } + \frac { \partial f } { \partial x ^ { 3 } } \mathrm { d } x ^ { 3 } .
$$

Thus,

$$
{ \begin{array} { r l } { \operatorname { g r a d } f } & { = { \frac { \partial f } { \partial x ^ { 1 } } } e _ { 1 } + { \frac { \partial f } { \partial x ^ { 2 } } } e _ { 2 } + { \frac { \partial f } { \partial x ^ { 3 } } } e _ { 3 } } \\ & { = \left( { \frac { \partial f } { \partial x ^ { 1 } } } , { \frac { \partial f } { \partial x ^ { 2 } } } , { \frac { \partial f } { \partial x ^ { 3 } } } \right) = { \frac { \partial f } { \partial x } } , } \end{array} }
$$

and so

$$
\begin{array} { r l } { \omega _ { \mathrm { c u r l } , A } ^ { 2 } = } & { \mathrm { d } \omega _ { A } ^ { 1 } = \mathrm { d } \big ( A _ { 1 } ( x ) \mathrm { d } x ^ { 1 } + A _ { 2 } ( x ) \mathrm { d } x ^ { 2 } + A _ { 3 } ( x ) \mathrm { d } x ^ { 3 } \big ) } \\ { = } & { \Big ( \frac { \partial A _ { 1 } } { \partial x ^ { 1 } } \mathrm { d } x ^ { 1 } + \frac { \partial A _ { 1 } } { \partial x ^ { 2 } } \mathrm { d } x ^ { 2 } + \frac { \partial A _ { 1 } } { \partial x ^ { 3 } } \mathrm { d } x ^ { 3 } \Big ) \wedge \mathrm { d } x ^ { 1 } } \\ & { + \Big ( \frac { \partial A _ { 2 } } { \partial x ^ { 1 } } \mathrm { d } x ^ { 1 } + \frac { \partial A _ { 2 } } { \partial x ^ { 2 } } \mathrm { d } x ^ { 2 } + \frac { \partial A _ { 2 } } { \partial x ^ { 3 } } \mathrm { d } x ^ { 3 } \Big ) \wedge \mathrm { d } x ^ { 2 } } \\ & { + \Big ( \frac { \partial A _ { 3 } } { \partial x ^ { 1 } } \mathrm { d } x ^ { 1 } + \frac { \partial A _ { 3 } } { \partial x ^ { 2 } } \mathrm { d } x ^ { 2 } + \frac { \partial A _ { 3 } } { \partial x ^ { 3 } } \mathrm { d } x ^ { 3 } \Big ) \wedge \mathrm { d } x ^ { 3 } } \\ { = } & { \Big ( \frac { \partial A _ { 3 } } { \partial x ^ { 2 } } - \frac { \partial A _ { 2 } } { \partial x ^ { 3 } } \Big ) \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 } + \Big ( \frac { \partial A _ { 1 } } { \partial x ^ { 3 } } - \frac { \partial A _ { 3 } } { \partial x ^ { 1 } } \Big ) \mathrm { d } x ^ { 3 } \wedge \mathrm { d } x ^ { 1 } } \\ & { + \Big ( \frac { \partial A _ { 2 } } { \partial x ^ { 1 } } - \frac { \partial A _ { 1 } } { \partial x ^ { 2 } } \Big ) \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } , } \end{array}
$$

where

$$
{ \begin{array} { r l } { \operatorname { c u r l } { A } } & { = \left( { \frac { \partial A _ { 3 } } { \partial x ^ { 2 } } } - { \frac { \partial A _ { 2 } } { \partial x ^ { 3 } } } \right) e _ { 1 } + \left( { \frac { \partial A _ { 1 } } { \partial x ^ { 3 } } } - { \frac { \partial A _ { 3 } } { \partial x ^ { 1 } } } \right) e _ { 2 } + \left( { \frac { \partial A _ { 2 } } { \partial x ^ { 1 } } } - { \frac { \partial A _ { 1 } } { \partial x ^ { 2 } } } \right) e _ { 3 } } \\ & { = { \left| \begin{array} { l l l } { e _ { 1 } } & { e _ { 2 } } & { e _ { 3 } } \\ { { \frac { \partial } { \partial x ^ { 1 } } } } & { { \frac { \partial } { \partial x ^ { 2 } } } } & { { \frac { \partial } { \partial x ^ { 3 } } } } \\ { A _ { 1 } } & { A _ { 2 } } & { A _ { 3 } } \end{array} \right| } , } \\ { { \boldsymbol { \omega } } _ { \mathrm { d i v } } ^ { 3 } { \mathrm { ~ } } _ { A } } & { = \mathrm { d } { \omega } _ { A } ^ { 2 } = \mathrm { d } ( A _ { 1 } \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 } + A _ { 2 } \mathrm { d } x ^ { 3 } \wedge \mathrm { d } x ^ { 1 } + A _ { 3 } \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } ) } \\ & { = \left( { \frac { \partial A _ { 1 } } { \partial x ^ { 1 } } } + { \frac { \partial A _ { 2 } } { \partial x ^ { 2 } } } + { \frac { \partial A _ { 3 } } { \partial x ^ { 3 } } } \right) \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 } . } \end{array} }
$$

Therefore,

$$
\operatorname { d i v } A = { \frac { \partial A _ { 1 } } { \partial x ^ { 1 } } } + { \frac { \partial A _ { 2 } } { \partial x ^ { 2 } } } + { \frac { \partial A _ { 3 } } { \partial x ^ { 3 } } } .
$$

Since

$$
\omega _ { \mathrm { c u r l ~ g r a d } _ { f } } ^ { 2 } = \mathrm { d } \omega _ { \mathrm { g r a d } _ { f } } ^ { 1 } = \mathrm { d } \left( \mathrm { d } f \right) = 0 ,
$$

$$
\operatorname { d i v } \operatorname { c u r l } { ( A ) \omega ^ { 3 } } = \operatorname { d } \left( \omega _ { \operatorname { c u r l } A } ^ { 2 } \right) = \operatorname { d } \left( \operatorname { d } \omega _ { A } ^ { 1 } \right) = 0 ,
$$

we easily get two equalities in classical vector analysis:

$$
\mathrm { c u r l ~ g r a d } = 0 , \quad \mathrm { d i v } \mathrm { c u r l } = 0 .
$$

# 1.4.6 Hodge Duality and Star Operators

Let us introduce the Hodge operator as a linear transformation:

$$
* : \Lambda ^ { p } \longrightarrow \Lambda ^ { n - p } .
$$

Definition 4.17. Denoting $^ { \ast \upsilon }$ as a element in $\Lambda ^ { n - p }$ , $\forall u \in \Lambda ^ { p }$ , we have

$$
u \Lambda * v = ( u , v ) e _ { n } .
$$

For brevity, we write $u \Lambda * v$ as $u \ast v$ .

If $\upsilon$ is a scalar, $u$ must also be a scalar. By the above formula, we get $* v = v e _ { n }$

Example 4.18. If

$$
\alpha = \sum _ { i _ { 1 } < \cdots < i _ { p } } a _ { i _ { 1 } \cdots i _ { p } } \mathrm { d } x ^ { i _ { 1 } } \wedge \cdots \wedge \mathrm { d } x ^ { i _ { p } } ,
$$

then

$$
\ast \alpha = \sum _ { i _ { 1 } < \cdots < i _ { p } } b _ { j _ { 1 } \cdots j _ { n - p } } \mathrm { d } x ^ { j _ { 1 } } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { j _ { n - p } } ,
$$

where

$$
b _ { j _ { 1 } \cdots j _ { n - p } } = \sum _ { i _ { 1 } < \cdots < i _ { p } } \varepsilon _ { i _ { 1 } \cdots i _ { p } j _ { 1 } \cdots j _ { n - p } } a ^ { i _ { 1 } \cdots i _ { p } } ,
$$

$\varepsilon _ { i _ { 1 } \cdots i _ { p } j _ { 1 } \cdots j _ { n - p } }$ is the generalized Kronecker symbol.

Star operators in 3-dimensional space have the following properties:

# Property 4.19.

$1 ^ { \circ }$ d x = d y  d z .   
$2 ^ { \circ }$ d y = d z d x.   
$3 ^ { \circ }$ $* \mathrm { d } z = \mathrm { d } x \wedge \mathrm { d } y .$ .   
$4 ^ { \circ }$ $* \left( \mathrm { d } x \wedge \mathrm { d } y \wedge \mathrm { d } z \right) = 1 .$   
$5 ^ { \circ }$ Let $\omega = a _ { 1 } \mathrm { d } x ^ { 1 } + a _ { 2 } \mathrm { d } x ^ { 2 } + a _ { 3 } \mathrm { d } x ^ { 3 }$ , then   
${ \ast \mathrm { d } } \omega = \left( { \frac { \partial a _ { 3 } } { \partial x ^ { 2 } } } - { \frac { \partial a _ { 2 } } { \partial x ^ { 3 } } } \right) \mathrm { d } x ^ { 1 } + \left( { \frac { \partial a _ { 1 } } { \partial x ^ { 3 } } } - { \frac { \partial a _ { 3 } } { \partial x ^ { 1 } } } \right) \mathrm { d } x ^ { 2 } + \left( { \frac { \partial a _ { 2 } } { \partial x ^ { 1 } } } - { \frac { \partial a _ { 1 } } { \partial x ^ { 2 } } } \right) \mathrm { d } x ^ { 3 } .$ $6 ^ { \circ } \quad * { \textrm { d } } * \omega = \frac { \partial a _ { 1 } } { \partial x ^ { 1 } } + \frac { \partial a _ { 2 } } { \partial x ^ { 2 } } + \frac { \partial a _ { 3 } } { \partial x ^ { 3 } } .$   
$7 ^ { \circ }$ grad $= \mathrm { d }$ (operation on $\Lambda ^ { 0 } ( \mathbf { R } ^ { 3 } ) ,$ ).   
$8 ^ { \circ }$ $\mathrm { r o t } = * \mathrm { d }$ (operation on $\Lambda ^ { 1 } ( \mathbf { R } ^ { 3 } )$ ).   
$9 ^ { \circ }$ $\mathrm { d i v } = * \mathrm { d } *$ (operation on $\Lambda ^ { 2 } ( \mathbf { R } ^ { 3 } ) ,$ .

# 1.4.7 Codifferential Operator $\delta$

We know that the exterior differential operator $\textrm { d } \colon \Lambda ^ { k } ( M ) \to \Lambda ^ { k + 1 } ( M )$ is a linear differential operator of first order, which increases one order in the form of differential form. However, Hodge star operator $\ast : \Lambda ^ { k } ( M ) \to \Lambda ^ { n - k } ( M )$ essentially is a dual operator. From this, one may ask whether it is possible to define a kind of $^ { - 1 }$ linear differential operator $\delta : \Lambda ^ { k } ( M ) \to \Lambda ^ { k - 1 } ( M )$ . The answer is yes.

Definition 4.20. The codifferential operator $\delta$ is a kind of linear differential operator of $^ { - 1 }$ order. $\delta \colon \Lambda ^ { k } ( M ) \to \Lambda ^ { k - 1 } ( M )$ . It can be represented by

$$
\delta = - ( - 1 ) ^ { g } ( - 1 ) ^ { n ( k + 1 ) } * \mathsf { d } * .
$$

If our manifold is an oriented Riemann manifold, then $g = 1$ .

Definition 4.21. The $k$ -form $\omega$ is called coclosed, if $\delta \omega = 0$ ; it is called coexact, if there exists a $\theta \in \Lambda ^ { k + 1 } ( M )$ s.t. $\omega = \delta \theta$ . The relation between operators $\delta$ , d, and $^ *$ leads to the following theorem.

Theorem 4.22. A codifferential operator $\delta$ has the following properties:

$$
\begin{array} { r l } { 2 ^ { \circ } } & { \ast \delta \mathbf { d } = \mathbf { d } \delta \ast , \ast \mathbf { d } \delta = \delta \mathbf { d } \ast . } \\ { 3 ^ { \circ } } & { \mathbf { d } \ast \delta = \delta \ast \mathbf { d } = 0 . } \\ { 4 ^ { \circ } } & { \ast ( \delta \omega ) = ( - 1 ) ^ { k } \mathbf { d } ( \ast \omega ) , \omega \in \Lambda ^ { k } ( M ) . } \\ { 5 ^ { \circ } } & { \delta ( \ast \omega ) = ( - 1 ) ^ { n - k + 1 } ( \mathbf { d } \omega ) , \omega \in \Lambda ^ { k } ( M ) . } \end{array}
$$

# 1.4.8 Laplace–Beltrami Operator

Definition 4.23. Linear mapping

$$
\Delta = { \bf d } \delta + \delta { \bf d } , \quad \Lambda ^ { k } ( M ) \longrightarrow \Lambda ^ { k } ( M )
$$

is called Laplace–Beltrami operator on Riemann manifold.

If $k = 0$ , for $f \in \Lambda ^ { 0 } ( M )$ , we have $\delta f = 0$ , and then

$$
\Delta f = \delta \mathrm { d } f .
$$

Theorem 4.24. The Laplace–Beltrami operator obeys the following rule:

$$
\begin{array} { r l } { { 1 } ^ { \circ } } & { { } \Delta = ( \mathrm { d } + \delta ) ^ { 2 } . } \\ { 2 ^ { \circ } } & { { } \mathrm { d } \cdot \Delta = \Delta \cdot \mathrm { d } = \mathrm { d } \cdot \delta \cdot \mathrm { d } . } \\ { 3 ^ { \circ } } & { { } \delta \cdot \Delta = \Delta \cdot \delta = \delta \cdot \mathrm { d } \cdot \delta . } \\ { 4 ^ { \circ } } & { { } * \Delta = \Delta * . } \end{array}
$$

Example 4.25. Let $f \in \Lambda ^ { 0 } ( \mathbf { R } ^ { 3 } )$ . For a rectangular coordinate system $\delta$ , we have

$$
\Delta f = \delta \mathbf { d } f = \delta { \frac { \partial f } { \partial x ^ { i } } } \mathbf { d } x ^ { i } .
$$

Since $\delta = - ( - 1 ) ^ { g } ( - 1 ) ^ { n ( k + 1 ) } * \mathtt { d } * = * \mathtt { d } * ,$ ,

$$
\Delta f = * \mathbf { d } * \left( { \frac { \partial f } { \partial x ^ { i } } } \mathrm { d } x ^ { i } \right) = \sum { \frac { \partial ^ { 2 } f } { ( \partial x ^ { i } ) ^ { 2 } } } .
$$

Obviously, for $\mathbf { R } ^ { 3 }$ , the Laplace–Beltrami operator $\Delta : \ \Lambda ^ { 0 } ( { \bf R } ^ { 3 } )  \ \Lambda ^ { 0 } ( { \bf R } ^ { 3 } )$ is the usual Laplace operator $\Delta = \sum _ { i = 1 } ^ { 3 } \frac { \partial ^ { 2 } } { ( \partial x ^ { i } ) ^ { 2 } } .$

The corresponding relationship in action on the form operators ${ \mathrm { d } }$ and $\delta$ and action on the coefficient of vector analysis can be summarized as follows:

$$
\begin{array} { l c c c c c c c } { { \mathrm { f o r m } : } } & { { \Lambda ^ { 0 } } } & { { \stackrel { \mathrm { d } } { \longleftrightarrow } } } & { { \Lambda ^ { 1 } } } & { { \stackrel { \mathrm { d } } { \longleftrightarrow } } } & { { \Lambda ^ { 2 } } } & { { \stackrel { \mathrm { d } } { \longleftrightarrow } } } & { { \Lambda ^ { 3 } } } \\ { { } } & { { \delta } } & { { \delta } } & { { \delta } } & { { \delta } } & { { } } \\ { { \mathrm { c o e f . : } } } & { { \mathrm { s c a l a r } } } & { { \stackrel { \mathrm { g r a d } } { \longleftrightarrow } } } & { { \mathrm { v e c t o r } } } & { { \stackrel { \mathrm { c u r l } } { \longleftrightarrow } } } & { { \mathrm { v e c t o r } } } & { { \stackrel { \mathrm { d i v } } { \longleftrightarrow } } } & { { \mathrm { s c a l a } } } \\ { { } } & { { - \mathrm { d i v } } } & { { \mathrm { c u r l } } } & { { - \mathrm { g r a d } } } & { { } } & { { } } \end{array}
$$

We can easily obtain two equations in classical vector analysis:

$$
\begin{array} { l l } { { \mathrm { d } \mathrm { d } = 0 : } } & { { \mathrm { r o t \ g r a d = 0 , } } } \\ { { } } & { { } } \\ { { \mathrm { ~ d i v \ r o t = 0 . } } } \\ { { \delta \delta = 0 : } } & { { - \mathrm { r o t \ g r a d = 0 , } } } \\ { { } } & { { } } \\ { { } } & { { - \mathrm { d i v \ r o t = 0 . } } } \end{array}
$$

# 1.5 Integration on a Manifold

The integral of an $n$ -form on an $n$ -manifold is defined in terms of integral over sets in $\mathbf { R } ^ { n }$ by means of partition of unity subordinate of an atlas.

# 1.5.1 Geometrical Preliminary

Chains. A singular $k$ -cube in $M \subset \mathbf { R } ^ { n }$ is a continuous function $c : [ 0 , 1 ] ^ { k } \to M$ , where $[ 0 , 1 ] ^ { n } = [ 0 , 1 ] \times \cdot \cdot \cdot \times [ 0 , 1 ]$ , ${ \bf R } ^ { 0 } = [ 0 , 1 ] ^ { 0 } = \{ 0 \}$ .

A singular 0-cube in $M$ is a function $c : [ 0 , 1 ] ^ { 0 } = \{ 0 \} \to M$ , i.e., a point in $M$ . A singular 1-cube in $M$ is a usual curve. The standard $n$ -cube in $\mathbf { R } ^ { n }$ is the identity mapping $I ^ { n } : [ 0 , 1 ] ^ { n } \to \mathbf { R } ^ { n } , I ^ { n } ( x ) = x , \forall x \in [ 0 , 1 ] ^ { n } .$

Definition 5.1. A $k$ -chain $C$ in $M$ is a linear combination of finite singular $k$ -cubes $c _ { i }$ in $M$ , i.e.,

$$
c = \alpha _ { 1 } c _ { 1 } + \cdot \cdot \cdot + \alpha _ { r } c _ { r } , \quad \alpha _ { i } \in \mathbf { R } , \quad i = 1 , \cdot \cdot \cdot , r .
$$

The set of all $k$ -chains in $M$ is denoted by $C ^ { k } ( M )$ . $C ^ { k } ( M )$ forms a vector space on $\mathbf { R }$ if we introduce in $C ^ { k } ( M )$ the addition and multiplication by scalar by the following formulae:

$$
\begin{array} { l } { { \displaystyle c ^ { 1 } + c ^ { 2 } = \sum _ { i = 1 } ^ { r } \alpha _ { i } ^ { 1 } c _ { i } + \sum _ { i = 1 } ^ { r } \alpha _ { i } ^ { 2 } c _ { i } = \sum _ { i = 1 } ^ { r } ( \alpha _ { i } ^ { 1 } + \alpha _ { i } ^ { 2 } ) c _ { i } , \hfill } } \\ { { \displaystyle \alpha c ^ { 1 } = \alpha \sum _ { i = 1 } ^ { r } \alpha _ { i } ^ { 1 } c _ { i } = \sum _ { i = 1 } ^ { r } ( \alpha \alpha _ { i } ^ { 1 } ) c _ { i } , } } \end{array}
$$

where $c ^ { j } = \sum _ { i = 1 } ^ { r } \alpha _ { i } ^ { j } c _ { i } \left( j = 1 , 2 \right)$ are two $k$ -chains in $M$ . Without loss of generality, we assume that different chains $c ^ { 1 }$ and $c ^ { 2 }$ are generated by the same set of $k$ -cubes $\{ c _ { 1 } , \cdots , c _ { r } \}$ . For example, let $c ^ { 1 } = c _ { 1 } + 2 c _ { 2 }$ , $c ^ { 2 } = c _ { 1 } + c _ { 3 }$ , where $c _ { 3 } \neq c _ { 2 }$ . We only need to rewrite $c ^ { 1 }$ and $c ^ { 2 }$ as $c ^ { 1 } = c _ { 1 } + 2 c _ { 2 } + 0 \cdot c _ { 3 }$ , $c ^ { 2 } = c _ { 1 } + 0 \cdot c _ { 2 } + c _ { 3 }$ .

Boundary of Chains Corresponding to the exterior operator d: $\Omega ^ { k } \to \Omega ^ { k + 1 }$ , there is a boundary operator $\partial : C ^ { k } ( M ) \to C ^ { k - 1 } ( M )$ , as defined below:

$$
\begin{array} { r l } & { \partial \left[ 0 , 1 \right] = \{ 1 \} - \{ 0 \} , } \\ & { \partial \left[ 0 , 1 \right] ^ { 2 } = \partial \left( [ 0 , 1 ] \times [ 0 , 1 ] \right) = \{ 1 \} \times [ 0 , 1 ] - \{ 0 \} \times [ 0 , 1 ] } \\ & { \qquad - [ 0 , 1 ] \times \{ 1 \} + [ 0 , 1 ] \times \{ 0 \} . } \end{array}
$$

For general $[ 0 , 1 ] ^ { k } , \forall x \in [ 0 , 1 ] ^ { k - 1 }$ , denote

$$
\begin{array} { r } { I _ { ( i , 0 ) } ^ { k } ( x ) = I ^ { k } ( x _ { 1 } , \cdots , x _ { i - 1 } , 0 , x _ { i } , \cdots , x _ { k - 1 } ) , } \\ { I _ { ( i , 1 ) } ^ { k } ( x ) = I ^ { k } ( x _ { 1 } , \cdots , x _ { i - 1 } , 1 , x _ { i } , \cdots , x _ { k - 1 } ) . } \end{array}
$$

We call $I _ { ( i , 0 ) } ^ { k }$ and $I _ { ( i , 1 ) } ^ { k }$ as $( i , 0 )$ - and $( i , 1 )$ -surface respectively, and

$$
\partial I ^ { k } = \partial [ 0 , 1 ] ^ { k } = \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { i + \alpha } I _ { ( i , \alpha ) } ^ { n } .
$$

For any $k$ -cube $c : [ 0 , 1 ] ^ { k } \to M$ , the $( i , \alpha )$ -surface is defined as

$$
c _ { ( i , \alpha ) } = c \circ I _ { ( i , \alpha ) } ^ { k } .
$$

The boundary $\partial c$ of the $k$ -cube $c$ is

$$
\partial c = \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { i + \alpha } c \circ I _ { ( i , \alpha ) } ^ { k } = \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { i + \alpha } c _ { ( i , \alpha ) } .
$$

The boundary of any $k$ -chain $c = \sum _ { j } \alpha _ { j } c _ { j }$ is

$$
\partial c = \sum _ { j } \alpha _ { j } \partial c _ { j } .
$$

Theorem 5.2. For any $k$ -chain $c _ { * }$ , $\partial ( \partial c ) = 0$ , or briefly $\partial ^ { 2 } = 0$ .

Proof. Firstly, assume $i \leq j$ and consider $( I _ { ( i , \alpha ) } ^ { k } ) _ { ( j , \beta ) }$ . For $x \in [ 0 , 1 ] ^ { k - 2 }$ , we have

$$
\begin{array} { r l } { ( I _ { ( i , \alpha ) } ^ { k } ) _ { ( j , \beta ) } ( x ) } & { = I _ { ( i , \alpha ) } ^ { k } ( x _ { 1 } , \cdots , x _ { j - 1 } , \beta , x _ { j } , \cdots , x _ { k - 2 } ) } \\ & { } \\ & { = I ^ { k } ( x _ { 1 } , \cdots , x _ { i - 1 } , \alpha , x _ { i } , \cdots , x _ { j - 1 } , \beta , x _ { j } , \cdots , x _ { k - 2 } ) . } \end{array}
$$

Similarly, we have

$$
\begin{array} { r l } { ( I _ { ( j + 1 , \beta ) } ^ { k } ) _ { ( i , \alpha ) } ( x ) } & { = I _ { ( j + 1 , \beta ) } ^ { k } ( x _ { 1 } , \cdot \cdot \cdot , x _ { i - 1 } , \alpha , x _ { i } , \cdot \cdot , x _ { k - 2 } ) } \\ & { = I ^ { k } ( x _ { 1 } , \cdot \cdot \cdot , x _ { i - 1 } , \alpha , x _ { i } , \cdot \cdot \cdot , x _ { j - 1 } , \beta , x _ { j } , \cdot \cdot \cdot , x _ { k - 2 } ) . } \end{array}
$$

Thus, if $i \ \leq \ j$ , $( I _ { ( i , \alpha ) } ^ { k } ) _ { ( j , \beta ) } ( x ) = ( I _ { ( j + 1 , \beta ) } ^ { k } ) _ { ( i , \alpha ) } ( x )$ , it is easy to see that for any $k$ -cube $c$ , $( c _ { ( i , \alpha ) } ) _ { ( j , \beta ) } = \left( c _ { ( j + 1 , \beta ) } \right) _ { ( i , \alpha ) }$ as $i \leq j$ . Now,

$$
\begin{array} { r l } { \displaystyle \partial ( \partial c ) } & { = \partial \left( \displaystyle \sum _ { i = 1 } ^ { k } \displaystyle \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { i + \alpha } c _ { ( i , \alpha ) } \right) } \\ & { = \displaystyle \sum _ { i = 1 } ^ { k } \displaystyle \sum _ { \alpha = 0 , 1 } \sum _ { j = 1 } ^ { k - 1 } \displaystyle \sum _ { \beta = 0 , 1 } ( - 1 ) ^ { i + \alpha + j + \beta } \big ( c _ { ( i , \alpha ) } \big ) _ { ( j , \beta ) } . } \end{array}
$$

In this sum, $\left( c _ { \left( i , \alpha \right) } \right) _ { \left( j , \beta \right) }$ and $( c _ { ( j + 1 , \beta ) } ) _ { ( i , \beta ) }$ occur simultaneously with the opposite sign. Then, all terms disappear in pairs and $\dot { \partial } ( \partial c ) = 0$ . Consequently, for any $k$ -chain $c = \sum _ { i = 1 } ^ { r } \alpha _ { i } c _ { i }$ , where $c _ { i }$ $( i = 1 , \cdots , r )$ are the $k$ -cubes,

$$
\partial ( \partial c ) = \partial \left( \sum _ { i = 1 } ^ { r } a _ { i } \partial c _ { i } \right) = \sum _ { i = 1 } ^ { r } a _ { i } \partial ( \partial c _ { i } ) = 0 .
$$

The theorem is proved.

Definition 5.3. A $k$ -chain $c$ is called a cycle if $\partial c = 0$ . A $k$ -chain $c$ is called a boundary if there is a $k + 1$ -chain $c _ { 1 }$ such that $c = \partial c _ { 1 }$ . Obviously, boundaries imply cycles. However, the converse is not always true.

# 1.5.2 Integration and Stokes Theorem

For any $\omega \in \Omega ^ { k } ( [ 0 , 1 ] ^ { k } )$ , there is a $f \in C ^ { \infty } ( ( 0 , 1 ) ^ { k } )$ such that $\omega = f \mathrm { d } x ^ { 1 } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { k }$ . Define the integral of $\omega$ on $[ 0 , 1 ] ^ { k }$ as

$$
\int _ { [ 0 , 1 ] ^ { k } } \omega = \int _ { [ 0 , 1 ] ^ { k } } f ,
$$

i.e.,

$$
\int _ { [ 0 , 1 ] ^ { k } } \omega = \int _ { [ 0 , 1 ] ^ { k } } f \mathrm { d } x ^ { 1 } \cdot \cdot \cdot \mathrm { d } x ^ { k } ,
$$

where the right hand side is a Riemannian integral of $f$ on $[ 0 , 1 ] ^ { k }$ .

If $\omega \in C ^ { k } ( M )$ and $c$ is a $k$ -cube in $M$ , we define the integral of $\omega$ on $c$ as

$$
\int _ { c } \omega = \int _ { [ 0 , 1 ] ^ { k } } c ^ { * } \omega .
$$

In particular,

$$
\begin{array} { r l } { \displaystyle \int _ { I ^ { k } } f \mathrm { d } x ^ { 1 } \wedge \dots \wedge \mathrm { d } x ^ { k } } & { = \displaystyle \int _ { [ 0 , 1 ] ^ { k } } ( I ^ { k } ) ^ { * } ( f \mathrm { d } x ^ { 1 } \wedge \dots \wedge \mathrm { d } x ^ { k } ) } \\ & { = \displaystyle \int _ { [ 0 , 1 ] ^ { k } } f ( x ^ { 1 } , \dots , x ^ { k } ) \mathrm { d } x ^ { 1 } \cdot \cdot \cdot \mathrm { d } x ^ { k } . } \end{array}
$$

If $c$ is a 0-cube, we define

$$
\int _ { c } \omega = \omega ( c ( 0 ) ) .
$$

The integral of $\omega$ on a $k$ -chain $c = \sum _ { i } a _ { i } c _ { i }$ is

$$
\int _ { c } \omega = \sum _ { i } a _ { i } \int _ { c _ { i } } \omega ,
$$

where $c _ { i }$ are $k$ -cubes in $M$ .

Example 5.4. For $k = 1 , c : [ 0 , 1 ] \to \mathbf { R } ^ { 2 }$ is a curve defined by $x = \cos 2 \pi \theta , \ y =$ sin $2 \pi \theta$ $1 \leq \theta \leq 1$ ), i.e., a circle on $( x , y )$ -plane. Let

$$
\omega = P ( x , y ) \mathrm { d } x + Q ( x , y ) \mathrm { d } y ,
$$

then, the integral of $\omega$ on $c$ is

$$
\begin{array} { r l } { \displaystyle \int _ { c } \omega } & { = \displaystyle \int _ { c } P ( x , y ) \mathrm { d } x + Q ( x , y ) \mathrm { d } y } \\ { \displaystyle } & { = \displaystyle \int _ { [ 0 , 1 ] } c ^ { * } ( P ( x , y ) \mathrm { d } x + Q ( x , y ) \mathrm { d } y ) } \\ { \displaystyle } & { = \displaystyle \int _ { 0 } ^ { 1 } \big ( - P ( \cos 2 \pi \theta , \sin 2 \pi \theta ) 2 \pi \sin 2 \pi \theta } \\ { \displaystyle } & { ~ + Q ( \cos 2 \pi \theta , \sin 2 \pi \theta ) 2 \pi \cos 2 \pi \theta \big ) \mathrm { d } \theta , } \end{array}
$$

which is the usual integral along a curve.

Theorem 5.5 (Stokes theorem). If $\omega$ is a $\left( k - 1 \right)$ -form on an open set $M \subset \mathbf { R } ^ { n }$ and c is a $k$ -chain in $M _ { ☉ }$ , then

$$
\int _ { c } \mathrm { d } \omega = \int _ { \partial \mathrm { c } } \omega .
$$

Proof. $1 ^ { \circ }$ Firstly, we assume $c = I ^ { k }$ and $\omega$ is a $\left( k - 1 \right)$ -form on $[ 0 , 1 ] ^ { k }$ . Then, $\omega$ is a sum of $\left( k - 1 \right)$ -forms of the type

$$
f \mathrm { d } x ^ { 1 } \wedge \cdot \cdot \cdot \wedge \widehat { \mathrm { d } x ^ { i } } \wedge \cdot \cdot \cdot \wedge \mathrm { d } x ^ { k } .
$$

Thus, it suffices to prove the theorem for each of these.

$$
\begin{array} { r l } { \displaystyle \int _ { t ^ { k } } \deg \ } & { \displaystyle = \ \int _ { t ^ { k } } \deg ^ { \prime } \Lambda \cdot \dots \cdot \Lambda \widehat { \mathrm { d } x ^ { k } } \wedge \dots \wedge \mathrm { d } x ^ { k } } \\ & { \ = \ \int _ { [ 0 , 1 ] ^ { k } } \sum _ { \hat { \mathcal { D } } \neq i } ^ { \hat { \mathcal { D } } } \mathrm { d } t ^ { \hat { \mathcal { D } } } \wedge \dots \wedge \widehat { \mathrm { d } x ^ { k } } \wedge \dots \wedge \mathrm { d } x ^ { k } } \\ & { \ = \ \int _ { [ 0 , 1 ] ^ { k } } ( - 1 ) ^ { t ^ { k - 1 } } \frac { \partial f } { \partial x ^ { 2 i } } \mathrm { d } x ^ { 1 } \wedge \dots \wedge \widehat { \mathrm { d } x ^ { k } } \wedge \dots \wedge \mathrm { d } x ^ { k } } \\ & { \ = \ ( - 1 ) ^ { k - 1 } \int _ { [ 0 , 1 ] ^ { k } } \frac { \partial f } { \partial x ^ { 2 i } } ( x ^ { 1 } , \dots , x ^ { k } ) \mathrm { d } x ^ { 1 } \dots \mathrm { d } x ^ { k } } \\ & { \ = \ ( - 1 ) ^ { k - 1 } \int _ { [ 0 , 1 ] ^ { k - 1 } } ( f ( x ^ { 1 } , \dots , 1 , \dots , x ^ { k } ) } \\ & { \quad - f ( x ^ { 1 } , \dots , 0 , \dots , x ^ { k } ) ) \mathrm { d } x ^ { 1 } \wedge \dots \wedge \mathrm { d } x ^ { k } \wedge \dots \wedge \mathrm { d } x ^ { k } } \end{array}
$$

Notice that

$$
\begin{array} { r l } & { \int _ { [ 0 , 1 ] ^ { k - 1 } } I _ { ( j , \alpha ) } ^ { k ^ { * } } \big ( f \mathrm { d } x ^ { 1 } \wedge \dots \wedge \widehat { \mathrm { d } x ^ { i } } \wedge \dots \wedge \mathrm { d } x ^ { k } \big ) } \\ & { = \displaystyle \int _ { [ 0 , 1 ] ^ { k - 1 } } f \big ( x ^ { 1 } , \dots , x ^ { j - 1 } , \alpha , x ^ { j } , \dots , x ^ { k } \big ) \Big ( I _ { ( j , \alpha ) } ^ { k ^ { * } } \mathrm { d } x ^ { 1 } \Big ) \wedge \dots \wedge \mathrm { d } x ^ { i } \wedge \dots \wedge \Big ( I _ { ( j , \alpha ) } ^ { k ^ { * } } \mathrm { d } x ^ { k } \Big ) } \\ & { = \left\{ \begin{array} { l l } { 0 , } & { i \not = j , } \\ { \displaystyle \int _ { [ 0 , 1 ] ^ { k - 1 } } f ( x ^ { 1 } , \dots , \alpha , \dots , x ^ { k } ) \mathrm { d } x ^ { 1 } \dots \widehat { \mathrm { d } x ^ { i } } \dots \mathrm { d } x ^ { k } , } & { i = j . } \end{array} \right. } \end{array}
$$

Thus,

$$
\begin{array} { l } { { \displaystyle \int _ { \partial I ^ { k } } f \mathrm { d } x ^ { 1 } \wedge \dots \wedge \widehat { \mathrm { d } x ^ { i } } \wedge \dots \wedge \mathrm { d } x ^ { k } } } \\ { { \displaystyle \quad = \sum _ { j = 1 } ^ { n } \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { j + \alpha } \int _ { [ 0 , 1 ] ^ { k - 1 } } I _ { ( j , \alpha ) } ^ { k ^ { * } } ( f \mathrm { d } x ^ { 1 } \wedge \dots \wedge \widehat { \mathrm { d } x ^ { i } } \wedge \dots \wedge \mathrm { d } x ^ { k } ) } } \\ { { \displaystyle \quad = ( - 1 ) ^ { i + 1 } \int _ { [ 0 , 1 ] ^ { k - 1 } } \big ( f ( x ^ { 1 } , \dots , x ^ { i - 1 } , 1 , \dots , x ^ { k } ) } } \\ { { \displaystyle \qquad \quad - f ( x ^ { 1 } , \dots , 0 , \dots , x ^ { k } ) \big ) \mathrm { d } x ^ { 1 } \wedge \dots \wedge \widehat { \mathrm { d } x ^ { i } } \wedge \dots \wedge \mathrm { d } x ^ { k } . } } \end{array}
$$

In other words,

$$
\int _ { I ^ { k } } \mathrm { d } \omega = \int _ { \partial I ^ { k } } \omega .
$$

$2 ^ { \circ }$ For a singular $k$ -cube $c$ , since

$$
\begin{array} { c l } { \displaystyle \partial c } & { = \displaystyle \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } \left( - 1 \right) ^ { i + \alpha } c _ { ( i , \alpha ) } } \\ { \displaystyle } & { = \displaystyle \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } \left( - 1 \right) ^ { i + \alpha } c \circ I _ { ( i , \alpha ) } ^ { k } , } \end{array}
$$

by definition of integration,

$$
\begin{array} { l } { { \displaystyle \int _ { \partial c } \omega = \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { i + \alpha } \int _ { c \circ I _ { ( i , \alpha ) } ^ { k } } \omega } } \\ { { \displaystyle \qquad = \sum _ { i = 1 } ^ { k } \sum _ { \alpha = 0 , 1 } ( - 1 ) ^ { i + \alpha } \int _ { I _ { ( i , \alpha ) } ^ { * } } c ^ { * } \omega = \int _ { \partial I ^ { k } } c ^ { * } \omega , } } \end{array}
$$

$$
\int _ { c } \mathrm { d } \omega = \int _ { I ^ { k } } c ^ { * } \mathrm { d } \omega = \int _ { I ^ { k } } \mathrm { d } c ^ { * } \omega = \int _ { \partial I ^ { k } } c ^ { * } \omega ,
$$

$\int _ { c } \mathrm { d } \omega = \int _ { \partial c } \omega$ , for any singular $k$ -cube $c$

Finally, if $c$ is a $k$ -chain, i.e., $c = \sum _ { i = 1 } ^ { k } \alpha _ { i } c _ { i }$ , where $c _ { i }$ are singular $k$ -cubes, then

$$
\int _ { c } \mathrm { d } \omega = \sum _ { i = 1 } ^ { k } a _ { i } \int _ { c _ { i } } \mathrm { d } \omega = \sum _ { i = 1 } ^ { k } a _ { i } \int _ { \partial c _ { i } } \omega = \int _ { \partial c } \omega .
$$

Therefore, the theorem is completed.

Example 5.6. Consider the 1-form

$$
\omega ^ { 1 } = p _ { 1 } \mathrm { d } q _ { 1 } + \cdot \cdot \cdot + p _ { n } \mathrm { d } q _ { n } ,
$$

on $\mathbf { R } ^ { 2 n }$ with the coordinates $p _ { 1 } , \cdot \cdot \cdot , p _ { n } , q _ { 1 } , \cdot \cdot \cdot , q _ { n } ; \mathrm { d } \omega ^ { 1 } = \mathrm { d } p _ { 1 } \wedge \mathrm { d } q _ { 1 } + \cdot \cdot \cdot + \mathrm { d } p _ { n } \wedge$ $\mathrm { d } q _ { n } = \mathrm { d } p \wedge \mathrm { d } q$ . Thus,

$$
\int \int _ { c _ { i } } \mathrm { d } p \wedge \mathrm { d } q = \int _ { \partial c _ { i } } p \mathrm { d } q .
$$

In particular, if $c _ { i }$ is a cycle , i.e., $\partial c _ { i } = 0$ , then $\int \int _ { c _ { i } } \mathrm { d } \boldsymbol { p } \wedge \mathrm { d } q = 0 .$

# 1.5.3 Some Classical Theories on Vector Analysis

Here, we assume $\mathbf { R } ^ { 3 }$ is the oriented 3-dim Euclidian space. By Subsection 1.4.5, every vector field $A$ on $\mathbf { R } ^ { 3 }$ corresponds to a 1-form $\omega _ { A } ^ { 1 }$ and a 2-form $\omega _ { A } ^ { 2 }$ :

$$
\begin{array} { c } { A = ( A _ { 1 } ( x ) , A _ { 2 } ( x ) , A _ { 3 } ( x ) ) , } \\ { \omega _ { A } ^ { 1 } = A _ { 1 } ( x ) \mathrm { d } x ^ { 1 } + A _ { 2 } ( x ) \mathrm { d } x ^ { 2 } + A _ { 3 } ( x ) \mathrm { d } x ^ { 3 } , } \\ { A _ { 1 } ( x ) \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 } + A _ { 2 } ( x ) \mathrm { d } x ^ { 3 } \wedge \mathrm { d } x ^ { 1 } + A _ { 3 } ( x ) \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } . } \end{array}
$$

Suppose a 1-chain $c _ { 1 }$ represents a curve $l$ (with the same orientation). Then,

$$
\int _ { c _ { 1 } } \omega _ { A } ^ { 1 } = \int _ { c _ { 1 } } A _ { 1 } \mathrm { d } x ^ { 1 } + A _ { 2 } \mathrm { d } x ^ { 2 } + A _ { 3 } \mathrm { d } x ^ { 3 } = \int _ { l } A \cdot \mathrm { d } l ,
$$

which shows that the integral of $\omega _ { A } ^ { 1 }$ on a l-chain $c _ { 1 }$ representing a curve $l$ is the circulation of the field $A$ over the curve $l$ . If $A$ is a force field, then the integral of $\omega _ { A } ^ { 1 }$ on a 1-chain $c _ { 1 }$ is the work done by $A$ along the curve $l$ .

Suppose a 2-chain $c _ { 2 }$ represents an oriented surface $S$ . Then,

$$
\begin{array} { r l } { \displaystyle \int _ { c _ { 2 } } \omega _ { A } ^ { 2 } } & { = \displaystyle \int _ { c _ { 2 } } A _ { 1 } \mathrm { d } x ^ { 2 } \wedge \mathrm { d } x ^ { 3 } + A _ { 2 } \mathrm { d } x ^ { 3 } \wedge \mathrm { d } x ^ { 1 } + A _ { 3 } \mathrm { d } x ^ { 1 } \wedge \mathrm { d } x ^ { 2 } } \\ & { = \displaystyle \int _ { S } A _ { 1 } \mathrm { d } x ^ { 2 } \mathrm { d } x ^ { 3 } + A _ { 2 } \mathrm { d } x ^ { 1 } \mathrm { d } x ^ { 3 } + A _ { 3 } \mathrm { d } x ^ { 1 } \mathrm { d } x ^ { 2 } } \\ & { = \displaystyle \int _ { S } A \mathrm { d } n . } \end{array}
$$

In other words, the integral of $\omega _ { A } ^ { 2 }$ on a 2-chain $c _ { 2 }$ representing an oriented surface $S$ is the flux of the field $A$ though the surface $S$ .

Applying the Stokes’ theorem to different cases, we can get three important theorems in classical calculus, Green theorem, Gauss theorem, and Stokes theorem.

Theorem 5.7 (Green theorem). Let $c _ { 2 }$ represent a 2-dim domain $D$ , $\partial c _ { 2 }$ the boundary $l$ of $D$ , and $\omega = P ( x , y ) \mathrm { d } x + Q ( x , y ) \mathrm { d } y \in C ^ { 1 } ( \mathbf { R } ^ { 2 } )$ . Then,

$$
\begin{array} { l } { \displaystyle \int _ { c _ { 2 } } \mathrm { d } \omega ~ = ~ \int _ { c _ { 2 } } \mathrm { d } ( P \mathrm { d } x + Q \mathrm { d } y ) , } \\ { \displaystyle \int _ { \partial c _ { 2 } } \omega \mathrm { d } l ~ = ~ \int _ { l } P \mathrm { d } x + Q \mathrm { d } y } \\ { ~ = ~ \int _ { c _ { 2 } } \big ( \frac { \partial Q } { \partial x } - \frac { \partial P } { \partial y } \big ) \mathrm { d } x \wedge \mathrm { d } y = \int _ { D } \big ( \frac { \partial Q } { \partial x } - \frac { \partial P } { \partial y } \big ) \mathrm { d } x \mathrm { d } y . } \end{array}
$$

Proof. Since

$$
{ \mathsf { d } } \left( P { \mathsf { d } } x + Q { \mathsf { d } } y \right) = { \Big ( } { \frac { \partial Q } { \partial x } } - { \frac { \partial P } { \partial y } } { \Big ) } { \mathsf { d } } x \wedge { \mathsf { d } } y ,
$$

$\int _ { \partial c } \omega \mathrm { d } l = \int _ { c } \mathrm { d } \omega$

$$
\int _ { D } \Big ( \frac { \partial Q } { \partial x } - \frac { \partial P } { \partial y } \Big ) { \mathrm { d } } x { \mathrm { d } } y = \int _ { l } P { \mathrm { d } } x + Q { \mathrm { d } } y ,
$$

which is the classical Green theorem.

Theorem 5.8 (Gauss theorem). If a 3-chain $c _ { 3 }$ represents a domain in $\mathbf { R } ^ { 3 }$ , $\partial c _ { 3 }$ represents the boundary $S = \partial D$ of $D$ , and $\omega _ { A } ^ { 2 } = A _ { x } \mathrm { d } y { \wedge } \mathrm { d } z { + } A _ { y } d z { \wedge } \mathrm { d } x { + } A _ { z } \mathrm { d } x { \wedge } \mathrm { d } y$ is a 2-form on $\mathbf { R } ^ { 3 }$ , then

$$
\begin{array} { r l } { \displaystyle \int _ { c _ { 3 } } \mathrm { d } \omega _ { A } ^ { 2 } ~ = ~ } & { \displaystyle \int _ { c _ { 3 } } \Big ( \frac { \partial A _ { x } } { \partial x } + \frac { \partial A _ { y } } { \partial y } + \frac { \partial A _ { z } } { \partial z } \Big ) \mathrm { d } x \wedge \mathrm { d } y \wedge \mathrm { d } z } \\ { ~ } & { ~ = ~ \displaystyle \int _ { D } \mathrm { d i v } A \mathrm { d } x \mathrm { d } y \mathrm { d } z , } \\ { \displaystyle \int _ { \partial c _ { 3 } } \omega ~ = ~ \displaystyle \int _ { S } A _ { x } \mathrm { d } y \mathrm { d } z + A _ { y } \mathrm { d } x \mathrm { d } z + A _ { z } \mathrm { d } x \mathrm { d } y . } \end{array}
$$

Thus, by Stokes’ theorem, we obtain Gauss theorem.

# Theorem 5.9 (Classical Stokes theorem).

$$
\int _ { D } \mathrm { d i v } A \mathrm { d } x \mathrm { d } y \mathrm { d } z = \int _ { S } A _ { x } \mathrm { d } y \mathrm { d } z + A _ { y } \mathrm { d } x \mathrm { d } z + A _ { z } \mathrm { d } x \mathrm { d } y .
$$

If a 2-chain $C$ in $\mathbf { R } ^ { 3 }$ represents an oriented surface $S$ , its boundary is $l = \partial S =$ $\partial c _ { 2 }$ and $\omega _ { A } ^ { 1 } = A _ { x } \mathrm { d } x + A _ { y } \mathrm { d } y + A _ { z } \mathrm { d } z$ is a 1-form on $\mathbf { R } ^ { 3 }$ . Then, the Stokes’ theorem shows

$$
\int _ { l } A _ { x } d x + A _ { y } d y + A _ { z } \mathrm { d } z = \int _ { S } \operatorname { c u r l } A \mathrm { d } s .
$$

Here we use the equality: $\mathrm { d } \omega _ { A } ^ { 1 } = \omega _ { \mathrm { c u r l } A } ^ { 1 }$

# 1.6 Cohomology and Homology

The set of all closed $k$ -forms, denoted by $Z ^ { k }$ , forms a subspace of $\Omega ^ { k }$ and the set of all exact $k$ -forms, denoted by $B ^ { k }$ , also forms a subspace of $\Omega ^ { k }$ . The quotient space

$$
H ^ { k } ( M , \mathbf { R } ) = { \frac { Z ^ { k } } { B ^ { k } } } \equiv \ { \frac { \mathrm { k e r } \mathrm { d } _ { k } } { \mathrm { i m } \mathrm { d } _ { k - 1 } } } ,
$$

is called the $k$ -th cohomology space. An element in $H ^ { k }$ is an equivalent class of closed forms, in which two closed forms $\omega _ { 1 }$ and $\omega _ { 2 }$ are equivalent if there is a $\left( k - 1 \right)$ -form $\theta$ such that $\omega _ { 1 } - \omega _ { 2 } = \mathrm { d } \theta$ , where ${ \mathrm { d } }$ is called the exterior differential operator. It is a mapping

$$
\begin{array} { r } { \mathbf { d } : \Omega ^ { k } ( M ) \longrightarrow \Omega ^ { k + 1 } ( M ) . } \end{array}
$$

The kernel of ${ \mathrm { d } }$ is the subspace $Z ^ { k }$ of the closed $k$ -form, the image of ${ \mathrm { d } }$ is the space $B ^ { k }$ of exact differential form. For every $k$ -form, we have $\mathrm { d } \omega ^ { k } = 0$ . Then

$$
B ^ { k } \subseteq Z ^ { k } .
$$

Similarly, the set of all $k$ -cycles, denoted by $Z _ { k }$ , and the set of all $k$ -boundaries, denoted by $B _ { k }$ , form a subspace of the vector space $C ^ { k }$ . The corresponding quotient space

$$
H _ { k } ( M , \mathbf { R } ) = \frac { Z _ { k } } { B _ { k } } = \frac { \ker \partial _ { k } } { \mathrm { i m } \partial _ { k + 1 } }
$$

is called the $k$ -th homology space. An element in $H _ { k }$ is a class of cycles differing from one another only by a boundary.

Definition 6.1. The dimension of $H ^ { k } ( H _ { k } )$ , denoted by $b ^ { k } ( b _ { k } )$ , is called the $k$ -th Betti number.

Theorem 6.2 (De Rham theorem). The two Betti numbers are the same, i.e.,

$$
b ^ { k } = b _ { k } .
$$

Example 6.3. $M \subset \mathbf { R } ^ { n }$ is an open set. We consider $H ^ { 0 } ( M , { \bf R } )$ and $H _ { 0 } ( M , { \bf R } )$ , $B ^ { 0 } =$ $\{ 0 \}$ , for there is no such form smaller than 0-form. If $\omega \in \Omega ^ { 0 } ( M )$ , then $\omega = f \in$ $C ^ { \infty } ( M ) , \mathrm { d } f = 0$ means that $f$ is equal to a constant (local), and:

$$
Z ^ { 0 } ( M ) = \underbrace { \mathbf { R } \times \cdots \times \mathbf { R } } _ { m } .
$$

If $M$ has components connected by $m$ paths. Since $H ^ { 0 } ( M , { \bf R } ) = Z ^ { 0 } ( M )$ , and $b ^ { 0 } = \mathrm { d i m } \left( H ^ { 0 } ( M , { \bf R } ) \right) = m $ , it is easy to see that , $Z _ { 0 } ( M )$ is generated by all points in $M$ and $m _ { 1 } , m _ { 2 } \in M \subset Z _ { 0 } ( M )$ is equivalent, iff they have components connected by the same path. Thus, $H _ { 0 } ( M , { \bf R } ) = { \bf R } \times \cdot \cdot \cdot \times { \bf R }$ and $b _ { 0 } = \mathrm { d i m } \left( H _ { 0 } ( M , { \bf R } ) \right) = m$ . 12m We have $b ^ { 0 } = b _ { 0 }$ . The De Rham theorem holds good for $k = 0$ in this case.

# 1.7 Lie Derivative

The Lie derivative may be defined in several equivalent ways. In this section, to keep things simple, we begin by defining the Lie derivative acting on scalar functions and vector fields. The Lie derivative can also be defined to act on general tensors, as discussed later in the article.

# 1.7.1 Vector Fields as Differential Operator

Let $X ( x ) = \sum _ { i = 0 } ^ { n } X _ { i } ( x ) e _ { i } = ( X _ { 1 } ( x ) , \cdot \cdot \cdot , X _ { n } ( x ) )$ be a vector field on $\mathbf { R } ^ { n }$ , and $\omega ^ { 1 } =$ $\sum _ { i = 0 } ^ { n } a _ { i } ( x ) \operatorname { d } x ^ { i }$ be a 1-form on $\mathbf { R } ^ { n }$ . $\langle \omega ^ { 1 } , X \rangle ( x ) = \langle \omega ^ { 1 } ( x ) , X ( x ) \rangle$ is the function on

$\mathbf { R } ^ { n }$ , where $\langle ~ , ~ \rangle$ is the dual bracket between $T _ { x } \mathbf { R } ^ { n }$ and $T _ { x } ^ { * } \mathbf { R } ^ { n }$ . This defines the natural bilinear mapping of

$$
\Lambda ^ { 1 } ( \mathbf { R } ^ { n } ) \times \mathcal { X } ( \mathbf { R } ^ { n } ) \longrightarrow C ^ { \infty } ( \mathbf { R } ^ { n } ) .
$$

If $\omega ^ { 1 } = \mathrm { d } f = \sum \frac { \partial f } { \partial x ^ { i } } \mathrm { d } x ^ { i }$ , then

$$
\langle \mathrm { d } f , X \rangle = \sum _ { i = 1 } ^ { n } { \frac { \partial f } { \partial x ^ { i } } } X _ { i } = \sum _ { i = 1 } ^ { n } X _ { i } ( x ) { \frac { \partial f } { \partial x ^ { i } } } .
$$

Denote $\langle \mathrm { d } f , X \rangle = L _ { X } f$ , i.e., $L _ { X } f = \sum _ { i = 1 } ^ { n } X _ { i } { \frac { \partial f } { \partial x ^ { i } } }$ $\forall f \in C ^ { \infty } ( \mathbf { R } ^ { n } )$ . Thus, any smooth vector field may be viewed as a linear partial differential operator on $\mathbf { R } ^ { n }$ of order 1, without zero terms and smooth coefficient, i.e., there is a correspondence between $X ( x ) \in { \mathcal { X } } ( \mathbf { R } ^ { n } )$ and $L _ { X }$ :

$$
X ( x ) = \sum _ { i = 1 } ^ { n } X _ { i } ( x ) e _ { i } \longrightarrow L _ { X } = \sum _ { i = 1 } ^ { n } X _ { i } ( x ) { \frac { \partial } { \partial x ^ { i } } } .
$$

It is one to one, and so hereafter, we can also write $X ( x ) = \sum _ { i = 1 } ^ { n } X _ { i } ( x ) e _ { i }$ as

$$
X ( x ) = \sum _ { i = 1 } ^ { n } X _ { i } ( x ) { \frac { \partial } { \partial x ^ { i } } } .
$$

Definition 7.1. For any two vector fields $X , Y \in { \mathcal { X } } ( \mathbf { R } ^ { n } )$ , define

$$
[ X , Y ] = X Y - Y X ,
$$

i.e.,

$$
[ X , Y ] f = X ( Y f ) - Y ( X f ) , \quad \forall f \in C ^ { \infty } ( \mathbf { R } ) ,
$$

where $X f$ is viewed as $L _ { X } f$ , and $[ X , Y ]$ is called the commutator or the Poisson bracket of $X , Y$ .

Proposition 7.2. Let $X = \sum _ { i = 1 } ^ { n } X _ { i } ( x ) { \frac { \partial } { \partial x ^ { i } } } , Y = \sum _ { i = 1 } ^ { n } Y _ { i } ( x ) { \frac { \partial } { \partial x ^ { i } } } , t h$ hen

$$
[ X , Y ] = \sum _ { i = 1 } ^ { n } \sum _ { k = 1 } ^ { n } \Big ( X _ { k } \frac { \partial Y _ { i } } { \partial x ^ { k } } - Y _ { k } \frac { \partial X _ { i } } { \partial x ^ { k } } \Big ) \frac { \partial } { \partial x ^ { i } } .
$$

Proof. $\forall f \in C ^ { \infty } ( \mathbf { R } ^ { n } )$ ,

$$
\begin{array} { l } { [ X , Y ] f } { = X ( Y f ) - Y ( X f ) } \\ { = X \Big ( \displaystyle \sum _ { i = 1 } ^ { n } Y _ { i } \frac { \partial f } { \partial x ^ { i } } \Big ) - Y \Big ( \displaystyle \sum _ { i = 1 } ^ { n } X _ { i } \frac { \partial f } { \partial x ^ { i } } \Big ) } \\ { = \displaystyle \sum _ { k = 1 } ^ { n } \displaystyle \sum _ { i = 1 } ^ { n } \Big ( X _ { k } \frac { \partial Y _ { i } } { \partial x ^ { k } } \frac { \partial f } { \partial x ^ { i } } + X _ { k } Y _ { i } \frac { \partial ^ { 2 } f } { \partial x ^ { i } \partial x ^ { k } } - Y _ { k } \frac { \partial X _ { i } } { \partial x ^ { k } } \frac { \partial f } { \partial x ^ { i } } - Y _ { k } X _ { i } \frac { \partial f ^ { 2 } } { \partial x ^ { i } \partial x ^ { k } } \Big . } \\ { = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } \Big ( X _ { k } \frac { \partial Y _ { i } } { \partial x ^ { k } } - Y _ { k } \frac { \partial X _ { i } } { \partial x ^ { k } } \Big ) \frac { \partial f } { \partial x ^ { i } } . } \end{array}
$$

Thus,

$$
[ X , Y ] = \sum _ { i = 1 } ^ { n } \sum _ { k = 1 } ^ { n } \Big ( X _ { k } \frac { \partial Y _ { i } } { \partial x ^ { k } } - Y _ { k } \frac { \partial X _ { i } } { \partial x ^ { k } } \Big ) \frac { \partial } { \partial x ^ { i } } .
$$

The $i$ -th component of $[ X , Y ]$ is

$$
[ X , Y ] _ { i } = \sum _ { k = 1 } ^ { n } \Big ( X _ { k } \frac { \partial Y _ { i } } { \partial x ^ { k } } - Y _ { k } \frac { \partial X _ { i } } { \partial x ^ { k } } \Big ) .
$$

In this manner, $[ X , Y ]$ may be represented by $\frac { \partial Y } { \partial x } X - \frac { \partial X } { \partial x } Y$ Y , where $\textstyle { \frac { \partial Y } { \partial x } }$ is the Jacobian of $Y$ . -

Theorem 7.3. Let $X _ { 1 } , X _ { 2 } , X _ { 3 } \in { \mathcal { X } } ( \mathbf { R } ^ { n } )$ and $f , g \in C ^ { \infty } ( \mathbf { R } ^ { n } )$ . Then,

${ \mathrm { ~  ~ \Omega ~ } } ^ { \circ } \quad [ X _ { 1 } , X _ { 2 } ] = - [ X _ { 2 } , X _ { 1 } ] .$ . $\begin{array} { r l } { { 2 } ^ { \circ } } & { [ \alpha _ { 1 } X _ { 1 } + \alpha _ { 2 } X _ { 2 } , X _ { 3 } ] = \alpha _ { 1 } [ X _ { 1 } , X _ { 3 } ] + \alpha _ { 2 } [ X _ { 2 } , X _ { 3 } ] . } \\ { { 3 } ^ { \circ } } & { [ f X _ { 1 } , g X _ { 2 } ] = f ( X _ { 1 } g ) X _ { 2 } - g ( X _ { 2 } f ) X _ { 1 } + f g [ X _ { 1 } , X _ { 2 } ] . } \\ { { 4 } ^ { \circ } } & { [ X _ { 1 } , [ X _ { 2 } , X _ { 3 } ] ] + [ X _ { 2 } , [ X _ { 3 } , X _ { 1 } ] ] + [ X _ { 3 } , [ X _ { 1 } , X _ { 2 } ] ] = 0 . } \end{array}$

The equality $4 ^ { \circ }$ is called Jacobi identity.

Proof. $1 ^ { \circ }$ and $2 ^ { \circ }$ are evident. $4 ^ { \circ }$ follows immediately from the expansion $3 ^ { \circ }$ :

$$
\begin{array} { r l } { \bigl [ f X _ { 1 } , g X _ { 2 } \bigr ] } & { = \bigl ( f X _ { 1 } \bigr ) \bigl ( g X _ { 2 } \bigr ) - \bigl ( g X _ { 2 } \bigr ) \bigl ( f X _ { 1 } \bigr ) } \\ & { = f \bigl ( X _ { 1 } g \bigr ) X _ { 2 } + f g X _ { 1 } X _ { 2 } - g \bigl ( X _ { 2 } f \bigr ) X _ { 1 } - f g X _ { 2 } X _ { 1 } } \\ & { = f \bigl ( X _ { 1 } g \bigr ) X _ { 2 } - g \bigl ( X _ { 2 } f \bigr ) X _ { 1 } + f g \bigl [ X _ { 1 } , X _ { 2 } \bigr ] . } \end{array}
$$

The proof can be obtained.

# 1.7.2 Flows of Vector Fields

In Subsection 1.2.2, we have already discussed vector field and the flow of a general differentiable manifold. Now, we focus on applications to the dynamic system.

(1) Phase space: The set of all possible states of a process is called phase space. For example, consider the motion of system in classical mechanics, whose future and past are uniquely determined by the initial position and initial velocities of all points in the system. The phase space of a mechanical system is the set whose elements are the sets of positions and velocities of all points of the given system. This is exactly the tangent space we discussed earlier.

(2) Differentiable process: A process is called differentiable if its phase space has the structure of a differentiable manifold, and the change of state with time is described by differentiable functions. Let $M$ be the phase space. A point of this space is a defined state of the process. Assume that at instant $t = 0$ the process was in state $x$ . Then at another moment, the process $t$ will be in another state. Denote this new state of the process by $g ^ { t } x$ . We have defined for each $t$ a mapping $g ^ { t }$

$$
g ^ { t } : M \longrightarrow M .
$$

This is called the transformation in time $t$ , which takes the state at instance 0 to the state at the instant $t$

$$
g ^ { 0 } = \mathrm { i d } , \quad g ^ { t + s } = g ^ { t } \cdot g ^ { s } .
$$

Let $y = g ^ { s } x$ be the state after time $s$ , and the state $z = g ^ { t } y$ again after time $t$ . The effect is the same as advancing $x$ to time $t + s$ , i.e.,

$$
z = g ^ { t + s } x .
$$

Thus, we can define a one parameter transformation group.

Definition 7.4. The mapping family $\{ g ^ { t } \}$ of set $M$ to itself is called a one parameter transformation group on filed $M$ , if $\forall s , t \in \mathbf { R }$ satisfies:

$$
g ^ { t + s } = g ^ { t } \cdot g ^ { s } , \quad g ^ { 0 } = I .
$$

Definition 7.5. The set $M$ and the corresponding one parameter transformation group $\{ g ^ { t } \}$ that maps $M$ to itself compose $( M , \{ g ^ { t } \} )$ , which is called the phase flow, where set $M$ is called the phase space, and its element is called the phase point.

(3) Diffeomorphism: If there exists a 1−1 map $f : U \to V$ so that $f$ and $f ^ { - 1 }$ : $V  U$ are both differentiable, then $f$ is said to be a diffeomorphism.

(4) One parameter diffeomorphism groups: The one parameter differmorphism group $\{ g ^ { t } \}$ on manifold $M$ is a collection of mappings from the direct product $\mathbf { R } \times M$ to $M$ :

$$
g : \mathbf { R } \times M \longrightarrow M , \quad g ( t , x ) = g ^ { t } \cdot x , \quad t \in \mathbf { R } , x \in M
$$

which satisfies:

$1 ^ { \circ }$ $g$ is a differentiable mapping.   
$2 ^ { \circ }$ $\forall t \in \mathbf { R }$ , $g ^ { t } : M \to M$ is a differomorphism.   
$3 ^ { \circ }$ Family $\{ g ^ { t } , t \in \mathbf { R } \}$ is one parameter transformation group for $M$ .

Dynamical system: the autonomous differential equation defined by a field $X$ is the equation

$$
\frac { \mathrm { d } x ( t ) } { \mathrm { d } t } = X ( x ( t ) ) , \quad x | _ { t = 0 } = x _ { 0 } \quad \mathrm { ( i n i t i a l \ v a l u e ) } .
$$

The image of the mapping $x ( t )$ is called a phase space, and the graph of the mapping $x ( t )$ is called an integral curve. The integral curve lies in the direct product of the time axis and the phase space, which is called $M \times \mathbf { R }$ extended space. Such an equation is called a dynamic system, whose phase flow $g ^ { t } , M \to M$ , $\{ g ^ { t } , t \in \mathbf { R } \}$ composes a group:

$$
g ^ { t } \cdot g ^ { s } = g ^ { t + s } , ~ g ^ { 0 } = \mathrm { i d } , ~ g ^ { - t } = \{ g ^ { t } \} ^ { - 1 } .
$$

Let $X$ be a smooth vector field on $\mathbf { R } ^ { n }$ . The solution curve through $x _ { 0 }$ is a differentiable mapping $t \to x ( t )$ : $I \to \mathbf { R } ^ { n }$ , where $I$ is an interval in $\mathbf { R }$ and $0 \in I$ , such that

$$
{ \frac { \mathrm { d } x ( t ) } { \mathrm { d } t } } = { \dot { x } } ( t ) = X ( x ( t ) ) , \quad t \in I , \quad x ( 0 ) = x _ { 0 } .
$$

It can be represented by its components as

$$
\frac { \mathrm { d } x _ { i } ( t ) } { \mathrm { d } t } = X _ { i } ( x _ { 1 } ( t ) , \cdot \cdot \cdot , x _ { n } ( t ) ) , \quad t \in I ; \quad i = 1 , \cdot \cdot \cdot , n , \quad x _ { i } ( 0 ) = x _ { i _ { 0 } } ,
$$

where $x ( t ) = ( x _ { 1 } ( t ) , \cdot \cdot \cdot , x _ { n } ( t ) )$ . It is well known that there is a unique differentiable solution $x ( t , x _ { 0 } )$ for the above system, which depends differentiably on the initial value $x _ { 0 }$ in some neighborhood.

The mapping $\phi _ { X } ^ { t }$ from (some neighborhood of) $\mathbf { R } ^ { n }$ to itself is defined by

$$
\phi _ { X } ^ { t } ( x _ { 0 } ) = x ( t , x _ { 0 } ) .
$$

Suppose $t$ is small enough, and is a diffeomorphism in (some neighborhood of) $\mathbf { R } ^ { n }$ . It has the following properties:

$1 ^ { \circ }$ $\phi _ { X } ^ { t _ { 1 } + t _ { 2 } } = \stackrel { \sim } { \phi } _ { X } ^ { t _ { 1 } } \cdot \stackrel { \sim } { \phi } _ { X } ^ { t _ { 2 } }$ $2 ^ { \circ }$ $\phi _ { X } ^ { 0 } = \mathrm { i d }$ . $3 ^ { \circ }$ $\phi _ { X } ^ { - t } = ( \phi _ { X } ^ { t } ) ^ { - 1 }$ .

Thus, such a class $\{ \phi _ { X } ^ { t } \}$ of the mappings $\phi _ { X } ^ { t }$ forms a group, called as a local 1- parameter transformations group in $\mathbf { R } ^ { n }$ , or a local dynamics system in $\mathbf { R } ^ { n }$ , or a flow in $\mathbf { R } ^ { n }$ .

# 1.7.3 Lie Derivative and Contraction

Let $\varphi : \mathbf { R } ^ { n } \to \mathbf { R } ^ { n }$ be a diffeomorphism and $Y \in \mathcal { X } ( \mathbf { R } ^ { m } )$ be a smooth vector field on $\mathbf { R } ^ { n }$ . The pullback $\varphi ^ { * } Y$ of $Y$ is a smooth vector field on $\mathbf { R } ^ { n }$ , defined by the formula

$$
( \varphi ^ { * } Y ) ( x ) = ( D \varphi ^ { - 1 } ) ( y ) Y ( y ) = \varphi _ { * } ^ { - 1 } ( y ) Y ( y ) , \quad y = \varphi ( x ) .
$$

Definition 7.6. Let $X$ and $Y$ be two vector fields. The Lie derivative $L _ { X } Y$ of $Y$ with respect to $X$ is defined by

$$
L _ { X } Y = { \frac { \mathrm { d } } { \mathrm { d } t } } { \big ( } \phi _ { X } ^ { t ^ { * } } Y { \big ) } { \big | } _ { t = 0 } ,
$$

where $\phi _ { X } ^ { t }$ is the flow of $X$ .

Theorem 7.7. Let $X$ and $Y$ be two vector fields. Then we have

$$
\begin{array} { l } { { ( \phi _ { X } ^ { t } Y ) f = \phi _ { X } ^ { t ^ { * } } ( Y \phi _ { X } ^ { - t ^ { * } } f ) , \forall f \in C ^ { \infty } ( \mathbf { R } ^ { n } ) . } } \\ { { \frac { \mathrm { d } } { \mathrm { d } t } ( \phi _ { X } ^ { t ^ { * } } f ) = \phi _ { X } ^ { t ^ { * } } ( X f ) . } } \\ { { L _ { X } Y = [ X , Y ] . } } \end{array}
$$

Proof. $1 ^ { \circ }$ By definition,

$$
{ \begin{array} { r l r l } { ( \phi _ { X } ^ { t ^ { * } } Y ) f ( x ) } & { = \langle \mathrm { d } f ( x ) , ( \phi _ { X } ^ { t ^ { * } } \cdot Y ) ( x ) \rangle = \langle \mathrm { d } f ( x ) , D \phi _ { X } ^ { - t } ( y ) Y ( y ) \rangle } & & { { \mathrm { ( } } y = \phi _ { X } ^ { t } ( x ) { \mathrm { ) } } } \\ & { = \langle ( D \phi _ { X } ^ { - t } ( y ) ) ^ { t } \mathrm { d } f ( x ) , Y ( y ) \rangle } \\ & { = \langle \mathrm { d } ( f \circ \phi _ { X } ^ { - 1 } ( y ) ) ^ { t } , Y ( y ) \rangle } \\ & { = \langle \mathrm { d } { \tilde { f } } ( y ) , Y ( y ) \rangle } & & { { \mathrm { ( } } { \tilde { f } } = f \circ \phi _ { X } ^ { t } { \mathrm { ) } } } \\ & { = ( Y { \tilde { f } } ) ( y ) = ( Y { \tilde { f } } ) ( \phi _ { X } ^ { t } ( x ) ) } \\ & { = \phi _ { X } ^ { t ^ { * } } ( Y { \tilde { f } } ) ( x ) = \phi _ { X } ^ { t ^ { * } } ( Y ( \phi _ { X } ^ { - t } ( y ) ) ) ( x ) } \\ & { = \phi _ { X } ^ { t ^ { * } } ( Y ( \phi _ { X } ^ { - t ^ { * } } f ) ) ( x ) . } \end{array} }
$$

$2 ^ { \circ }$ The proof is as follows:

$$
\begin{array} { r l } { \displaystyle \frac { \mathrm { d } } { \mathrm { d } t } \big ( \phi _ { X } ^ { t ^ { * } } f \big ) } & { = \displaystyle \frac { \mathrm { d } } { \mathrm { d } t } f \big ( \phi _ { X } ^ { t } ( x ) \big ) = \sum _ { i = 1 } ^ { n } \frac { \partial f } { \partial x ^ { i } } X _ { i } \big ( \phi _ { X } ^ { t } ( x ) \big ) } \\ & { = \displaystyle ( X f ) \big ( \phi _ { X } ^ { t } ( x ) \big ) = \phi _ { X } ^ { t ^ { * } } ( X f ) . } \end{array}
$$

$3 ^ { \circ }$ The proof is as follows:

$$
\begin{array} { l } { { ( L _ { X } Y ) f ~ = \frac { \mathrm { d } } { \mathrm { d } t } \big ( \phi _ { X } ^ { t ^ { * } } Y \big ) f \big | _ { t = 0 } = \frac { \mathrm { d } } { \mathrm { d } t } \big ( \phi _ { X } ^ { t ^ { * } } \big ( Y \cdot \phi _ { X } ^ { - t ^ { * } } f \big ) \big ) \big | _ { t = 0 } } } \\ { { ~ = \big ( \phi _ { X } ^ { t ^ { * } } X Y \cdot \phi _ { X } ^ { - t ^ { * } } f - \phi _ { X } ^ { t ^ { * } } Y \phi _ { X } ^ { - t ^ { * } } X f \big ) \big | _ { t = 0 } } } \\ { { ~ = X Y f - Y X f = [ X , Y ] f , ~ \forall f . } } \end{array}
$$

Thus, we get

$$
L _ { X } Y = [ X , Y ] .
$$

Therefore, the theorem is completed.

By the equality $3 ^ { \circ }$ , the Jacobi identity about the Poisson bracket $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ shows that the operator $L _ { X }$ is a $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ -derivative on the algebra $\mathcal { X } ( \mathbf { R } ^ { n } )$ with binary operator $[ , ]$ , i.e.,

$$
L _ { X } \{ X _ { 1 } , X _ { 2 } \} = \{ L _ { X } X _ { 1 } , X _ { 2 } \} + \{ X _ { 1 } , L _ { X } X _ { 2 } \} .
$$

Definition 7.8. $\forall \omega \in \Omega ^ { k } ( \mathbf { R } ^ { n } )$ , the Lie derivative $L _ { X } \omega$ of $\omega$ with respect to a vector field $X \in { \mathcal { X } } ( \mathbf { R } ^ { n } )$ is defined by

$$
L _ { X } \omega = \left. { \frac { \mathrm { d } } { \mathrm { d } t } } \phi _ { X } ^ { t ^ { * } } \omega \right| _ { t = 0 } = \operatorname * { l i m } _ { t \to 0 } { \frac { 1 } { t } } \big ( \phi _ { X } ^ { t ^ { * } } \omega - \omega \big ) .
$$

Theorem 7.9. The Lie derivative $L _ { X }$ with respect to $X \in \mathcal { X } ( \mathbf { R } ^ { n } )$ has the following properties:

$\quad 1 ^ { \circ } \quad L _ { X } f = X f = \sum _ { i = 1 } ^ { n } X _ { i } { \frac { \partial f } { \partial x ^ { i } } } $ , $f \in C ^ { \infty } ( \mathbf { R } ^ { n } ) $ , i.e., the Lie derivatives of a function $f$ with respect to $X$ is the directional derivative in direction $X ( x )$ .

$2 ^ { \circ }$ $L _ { X }$ is a $\Lambda$ -derivative, i.e., $L _ { X }$ is $\mathbf { R }$ -linear,

$$
\begin{array} { l } { { { \cal L } _ { X } ( \alpha \omega _ { 1 } + \beta \omega _ { 2 } ) = \alpha { \cal L } _ { X } \omega _ { 1 } + \beta { \cal L } _ { X } \omega _ { 2 } , } } \\ { { { } } } \\ { { { \cal L } _ { X } ( \omega _ { 1 } \wedge \omega _ { 2 } ) = { \cal L } _ { X } \omega _ { 1 } \wedge \omega _ { 2 } + \omega _ { 1 } \wedge { \cal L } _ { X } \omega _ { 2 } . } } \end{array}
$$

3◦ $L _ { X } d = d L _ { X } $

Proof. $1 ^ { \circ }$ We have $\frac { \mathop { } { \bf d } } { \mathop { } { \bf d } t } \phi _ { X } ^ { t ^ { * } } f = \phi _ { X } ^ { t ^ { * } } ( X f )$ , and so

$$
{ \cal L } _ { X } f = \left. { \frac { \operatorname { d } } { \operatorname { d } t } } \right| _ { t = 0 } ( \phi _ { X } ^ { t ^ { * } } f ) = \left. ( \phi _ { X } ^ { t ^ { * } } X f ) \right| _ { t = 0 } = X f .
$$

$2 ^ { \circ }$ It is obvious that $L _ { X }$ is $\mathbf { R }$ -linear,

$$
\begin{array} { r l } {  L _ { X } ( \omega _ { 1 } \wedge \omega _ { 2 } ) =  \frac { \mathrm { d } } { \mathrm { d } t } | _ { t = 0 } \phi _ { X } ^ { t ^ { * } } ( \omega _ { 1 } \wedge \omega _ { 2 } ) } \\ { = } & { \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t = 0 } \big ( \phi _ { X } ^ { t ^ { * } } \omega _ { 1 } \wedge \phi _ { X } ^ { t ^ { * } } \omega _ { 2 } \big ) } \\ { = } & { \Big (  \frac { \mathrm { d } } { \mathrm { d } t } | _ { t = 0 } \phi _ { X } ^ { t ^ { * } } \omega _ { 1 } \Big ) \wedge \omega _ { 2 } + \omega _ { 1 } \wedge \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t = 0 } \phi _ { X } ^ { t ^ { * } } \omega _ { 2 } } \\ { = } & { L _ { X } \omega _ { 1 } \wedge \omega _ { 2 } + \omega _ { 1 } \wedge L _ { X } \omega _ { 2 } . } \end{array}
$$

$3 ^ { \circ }$ The proof is as follows:

$$
\begin{array} { r l } { { \cal L } _ { X } \mathrm { d } \omega = } & { \frac { \mathrm { d } } { \mathrm { d } t } \bigg | _ { t = 0 } \phi _ { X } ^ { t ^ { * } } \mathrm { d } \omega = \frac { \mathrm { d } } { \mathrm { d } t } \bigg | _ { t = 0 } \mathrm { d } \phi _ { X } ^ { t ^ { * } } \omega } \\ { = } & { \mathrm { d } \frac { d } { \mathrm { d } t } \bigg | _ { t = 0 } \phi _ { X } ^ { t ^ { * } } \omega = \mathrm { d } { \cal L } _ { X } \omega . } \end{array}
$$

Therefore, the theorem is completed.

Definition 7.10. Let $X \in \mathcal { X } ( \mathbf { R } ^ { n } )$ and $\omega \in \Omega ^ { k } ( \mathbf { R } ^ { n } )$ . The contraction $i _ { X } \omega$ of $X$ and $\omega$ is defined by

$$
i _ { X } \omega ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k - 1 } ) = \omega ( X ( x ) , \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { k - 1 } ) , \quad \xi _ { i } \in T _ { k } \mathbf { R } ^ { n } , \quad i = 1 , \cdot \cdot \cdot , k - 1 .
$$

$i _ { X } f = 0$ , for $f \in C ^ { \infty } ( \mathbf { R } ^ { n } ) = \Omega ^ { 0 } ( \mathbf { R } ^ { n } ) . i _ { X }$ maps $k$ -forms into $\left( k - 1 \right)$ -forms, i.e.,

$$
\Omega ^ { k } ( { \mathbf { R } } ^ { n } ) \longrightarrow \Omega ^ { k - 1 } ( { \mathbf { R } } ^ { n } ) .
$$

Theorem 7.11. Let $\omega _ { 1 } , \omega _ { 2 } \in \Omega ^ { k } ( \mathbf { R } ^ { n } )$ , $\omega _ { 3 } \in \Omega ^ { l } ( \mathbf { R } ^ { n } )$ . Then,

$1 ^ { \circ }$ $i _ { X }$ is a $\Lambda$ -antiderivative, i.e., R-linear. ${ \bf R } \ – l i n e a r : \ i _ { X } ( \alpha _ { 1 } \omega _ { 1 } + \alpha _ { 2 } \omega _ { 2 } ) = \alpha _ { 1 } i _ { X } \omega _ { 1 } + \alpha _ { 2 } i _ { X } \omega _ { 2 } , \quad \alpha _ { 1 } , \alpha _ { 2 } \in { \bf R } .$ anti-derivative : $i _ { X } ( \omega _ { 1 } \wedge \omega _ { 3 } ) = i _ { X } \omega _ { 1 } \wedge \omega _ { 3 } + ( - 1 ) ^ { k } \omega _ { 1 } \wedge i _ { X } \omega _ { 3 } .$   
$2 ^ { \circ }$ $i _ { f X + g Y } = f i _ { X } + g i _ { Y } , \forall f , g \in C ^ { \infty } ( \mathbf { R } ^ { n } ) , X , Y \in \mathcal { X } ( \mathbf { R } ^ { n } ) .$   
$3 ^ { \circ }$ iXdf = LXf, f ∈ C∞(Rn).   
$4 ^ { \circ }$ $L _ { X } = i _ { X } \mathrm { d } + \mathrm { d } i _ { X }$ , (Cartan’s Magic formula).   
$5 ^ { \circ }$ $L _ { f X } = f L _ { X } + \mathrm { d } f \wedge i _ { X } .$

Proof. $1 ^ { \circ }$ R-linearity of $i _ { x }$ is evident.

$$
\begin{array} { l } { { \displaystyle i _ { X _ { 1 } } ( \omega _ { 1 } \wedge \omega _ { 3 } ) ( \xi _ { 2 } , \cdots , \xi _ { k + l - 1 } ) } } \\ { { \displaystyle = ( \omega _ { 1 } \wedge \omega _ { 3 } ) ( X _ { 1 } ( x ) , \xi _ { 2 } , \cdots , \xi _ { k + l } ) } } \\ { { \displaystyle = ( \omega _ { 1 } \wedge \omega _ { 3 } ) ( \xi _ { 1 } , \xi _ { 2 } , \cdots , \xi _ { k + l } ) } } \\  { \displaystyle = \sum _ { \sigma ( 1 ) < \cdots < \sigma ( k ) \} \sum _ { \sigma ( k + 1 ) < \cdots < \sigma ( k + l ) } \varepsilon ( \sigma ) \omega _ { 1 } ( \xi _ { \sigma ( 1 ) } , \cdots , \xi _ { \sigma ( k ) } ) \omega _ { 3 } ( \xi _ { \sigma ( k + 1 ) } , \cdots , \xi _ { \sigma ( k + l ) } ) } } \\ { { \displaystyle = \sum _ { \substack { i \in \{ \sigma ( 1 ) \cdots \sigma ( k ) \} } } ^ { \prime } + \sum _ { \substack { i \in \{ \sigma ( k + 1 ) \cdots \sigma ( k + l ) \} } } ^ { \prime \prime } } . } \end{array}
$$

In the first part, it must be $\sigma ( 1 ) = 1$ since $\sigma ( 1 ) < \cdots < \sigma ( k ) .$ . Similarly, in the second part, $\sigma ( k + 1 ) = 1$ .

Set

$$
\begin{array} { l } { { \sigma ^ { \prime } = \{ \sigma ( 2 ) , \cdots , \sigma ( k ) , \sigma ( k + 1 ) , \cdots , \sigma ( k + l ) \} , } } \\ { { \nonumber } } \\ { { \sigma ^ { \prime \prime } = \{ \sigma ( 1 ) , \cdots , \sigma ( k ) , \sigma ( k + 2 ) , \cdots , \sigma ( k + l ) \} . } } \end{array}
$$

Then,

$$
\begin{array} { r l r l } & { \varepsilon ( \sigma ) = \varepsilon ( \sigma ^ { \prime } ) , } & { \mathrm { i f } } & { i \in \{ \sigma ( 1 ) , \cdots , \sigma ( k ) \} , } \\ & { \varepsilon ( \sigma ) = ( - 1 ) ^ { k } \varepsilon ( \sigma ^ { \prime \prime } ) , } & { \mathrm { i f } } & { i \in \{ \sigma ( k + 1 ) , \cdots , \sigma ( k + l ) \} . } \end{array}
$$

Thus,

$$
\begin{array} { r l } & { \| x ( z ) , \psi ( x , z ) \| \leq \| \hat { g } ( \xi , \eta , \zeta , \xi , \eta + 1 ) } \\ & { = \qquad \quad \times \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad  \\ & { = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad \quad \quad  \\ & { = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \ \end{array}
$$

Thus, we get the equality

$$
i _ { X } ( \omega _ { 1 } \wedge \omega _ { 3 } ) = i _ { X } \omega _ { 1 } \wedge \omega _ { 3 } + ( - 1 ) ^ { k } \omega _ { 1 } \wedge i _ { X } \omega _ { 3 } .
$$

$2 ^ { \circ }$ The proof is as follows:

$$
\begin{array} { r l } & { ( i _ { f X + g Y } \omega ) ( \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) } \\ & { = \omega ( f X + g Y , \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) } \\ & { = f ( x ) \omega ( X ( x ) , \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) + g ( x ) \omega ( Y ( x ) , \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) } \\ & { = f ( x ) i _ { X } \omega ( \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) + g ( x ) i _ { Y } \omega ( \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) } \\ & { = ( f ( x ) i _ { X } + g ( x ) i _ { Y } ) ( \xi _ { 1 } , \cdots , \xi _ { k - 1 } ) . } \end{array}
$$

This is the equation $2 ^ { \circ }$ .

$3 ^ { \circ }$ $i _ { X } \mathbf { d } f = \mathbf { d } f ( X ) = X f = L _ { X } f$ .   
$4 ^ { \circ }$ By induction with respect to $k$ . $k = 0$ . i.e., $3 ^ { \circ }$ .

Suppose that $4 ^ { \circ }$ holds good for $k$ . Then for $k + 1$ , $\omega$ can be written as a sum of the forms like $\omega ^ { 1 } \wedge \mathrm { d } f$ where $\omega ^ { 1 } \in \Omega ^ { k } ( \mathbf { R } ^ { n } )$ and $f \in C ^ { \infty } ( \mathbf { R } ^ { n } )$ . By linearity of $L _ { X }$ , without loss of generality we may assume $\omega = \omega ^ { 1 } \wedge \mathrm { d } f$ . Then,

$$
\begin{array} { r l } { L _ { X } ( \omega \wedge \mathrm { d } f ) } & { = L _ { X } \omega \wedge \mathrm { d } f + \omega \wedge L _ { X } \mathrm { d } f } \\ & { = ( i _ { X } \mathrm { d } \omega + \mathrm { d } i _ { X } \omega ) \wedge \mathrm { d } f + \omega \wedge \mathrm { d } L _ { X } f . } \end{array}
$$

On the other hand,

$$
\begin{array} { r l } & { ( i _ { X } \mathbf { d } + \mathbf { d } i _ { X } ) ( \omega \wedge \mathbf { d } f ) } \\ & { = i _ { X } \mathbf { d } ( \omega \wedge \mathbf { d } f ) + ( \mathbf { d } i _ { X } ) ( \omega \wedge \mathbf { d } f ) } \\ & { = i _ { X } ( \mathbf { d } \omega \wedge \mathbf { d } f ) + \mathbf { d } ( i _ { X } \omega \wedge \mathbf { d } f + ( - 1 ) ^ { k } \omega \wedge i _ { X } \mathbf { d } f ) } \\ & { = i _ { X } \mathbf { d } \omega \wedge \mathbf { d } f + ( - 1 ) ^ { k + 1 } \mathbf { d } \omega \wedge i _ { X } \mathbf { d } f + \mathbf { d } i _ { X } \omega \wedge \mathbf { d } f } \\ & { \quad + ( - 1 ) ^ { k } \mathbf { d } \omega \wedge i _ { X } f + ( - 1 ) ^ { 2 k } \omega \wedge \mathbf { d } L _ { X } f } \\ & { = ( i _ { X } \mathbf { d } + \mathbf { d } i _ { X } ) \omega \wedge \mathbf { d } f + \omega \wedge \mathbf { d } L _ { X } f , } \end{array}
$$

thus, $L _ { X } ( \omega \wedge \mathrm { d } f ) = ( i _ { X } \mathrm { d } + \mathrm { d } i _ { X } ) ( \omega \wedge \mathrm { d } f )$ , i.e.,

$$
L _ { X } = i _ { X } \mathbf { d } + \mathbf { d } i _ { X } .
$$

$5 ^ { \circ }$ The proof is as follows:

$$
\begin{array} { r l } { L _ { f X } } & { = ( \mathrm { d } i _ { f X } + i _ { f X } \mathrm { d } ) \omega } \\ & { = \mathrm { d } ( f i _ { X } \omega ) + f i _ { X } \mathrm { d } \omega } \\ & { = \mathrm { d } f \wedge i _ { X } \omega + f \mathrm { d } i _ { X } \omega + f i _ { X } \mathrm { d } \omega } \\ & { = ( f L _ { X } + \mathrm { d } f \wedge i _ { X } ) \omega , } \end{array}
$$

so

$$
L _ { f X } = f L _ { X } + \mathbf { d } f \wedge i _ { X } .
$$

Therefore, the theorem is completed.

Every $k$ -form $\omega$ on $\mathbf { R } ^ { n }$ can also be considered as a function on $\mathcal { X } ^ { k } ( \mathbf { R } ^ { n } ) \colon \mathcal { X } ^ { k } ( \mathbf { R } ^ { n } )$ $\to C ^ { \infty } ( \mathbf { R } ^ { n } )$ , i.e.,

$$
\omega ( X _ { 1 } , \cdots , X _ { k } ) ( x ) = \omega ( x ) ( X _ { 1 } ( x ) , \cdots , X _ { k } ( x ) ) , \quad X _ { i } \in { \mathcal { X } } ( \mathbf { R } ^ { n } ) , \quad i = 1 , \cdots , k .
$$

It is linear, skew-symmetric.

Theorem 7.12. Let $\omega \in \Omega ^ { k } ( \mathbf { R } ^ { n } )$ , be vector fields on $\mathbf { R } ^ { n }$ . Then,

$$
\begin{array}{c} { \begin{array} { r l } & { { \mathsf { c o r e m ~ } } / { \mathbf { 1 } } { \boldsymbol { \bot } } . { \begin{array} { l } { . . . 6 t w \in { \mathrm {  ~ S I } } ^ { k } \left( { \mathrm {  ~ K } } ^ { \times } \right) , ~ { \boldsymbol { \lambda } } _ { i } ~ ( { \mathrm {  ~ l } } = 1 , \cdots , k ) ~ b e ~ \nu e c t o r f J e t a s ~ o n ~ { \mathrm {  ~ K } } ^ { \times } \cdot ~ { \mathrm {  ~ I } } n e n , } \\ { ~ 1 ^ { \circ } ~ ( L _ { X } \omega ) ( X _ { 1 } , \cdots , X _ { k } ) = L _ { X } \left( \omega ( X _ { 1 } , \cdots , X _ { k } ) \right) - \displaystyle \sum _ { i = 1 } ^ { k } \omega ( X _ { 1 } , \cdots , L _ { X } X _ { i } , \cdots , X _ { k } ) . } \end{array} } } \\ & { } \\ & { ~ 2 ^ { \circ } ~ d \omega ( X _ { 0 } , \cdots , X _ { k } ) = \displaystyle \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { i } L _ { X _ { i } } \left( \omega ( X _ { 0 } , \cdots , { \widehat { X } } _ { i } , \cdots , X _ { j } , \cdots , X _ { k } ) \right. } \\ & { \qquad \left. + \displaystyle \sum _ { i < j } ( - 1 ) ^ { i + j } \omega ( L _ { X _ { i } } X _ { j } , X _ { 0 } , \cdots , { \widehat { X } } _ { i } , \cdots , { \widehat { X } } _ { j } , \cdots , X _ { k } ) . \right. } \end{array} }  \end{array} 
$$

Proof.

$1 ^ { \circ }$ By the definition of $L _ { X }$ and the Theorem 7.7, since

$$
\begin{array} { l } { ( \phi _ { X } ^ { t ^ { * } } \omega ) ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) } \\ { = \omega ( \phi _ { X } ^ { - t ^ { * } } X _ { 1 } , \cdot \cdot \cdot , \phi _ { X } ^ { - t ^ { * } } X _ { k } ) ( \phi _ { X } ^ { t } X ) } \\ { = \phi _ { X } ^ { t ^ { * } } ( \omega ( \phi _ { X } ^ { - t ^ { * } } X _ { 1 } , \cdot \cdot \cdot , \phi _ { X } ^ { - t ^ { * } } X _ { k } ) ) , } \end{array}
$$

we have

$$
\begin{array} { r l } { ( L _ { X } \omega ) ( X _ { 1 } , \cdots , X _ { k } ) } & { = \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t = 0 } ( \phi _ { X } ^ { t ^ { * } } \omega ) ( X _ { 1 } , \cdots , X _ { k } ) } \\ & { = \frac { \mathrm { d } } { \mathrm { d } t } \Big | _ { t = 0 } \bigl ( \phi _ { X } ^ { t ^ { * } } \omega ( \phi _ { X } ^ { - t ^ { * } } X _ { 1 } , \cdots , \phi _ { X } ^ { - t ^ { * } } X _ { k } ) \bigr ) } \\ & { = L _ { X } \bigl ( \omega ( X _ { 1 } , \cdots , X _ { k } ) \bigr ) - \displaystyle \sum _ { i = 1 } ^ { k } \omega ( X _ { 1 } , \cdots , L _ { X } X _ { i } , \cdots , X _ { k } ) . } \end{array}
$$

$2 ^ { \circ }$ By induction with respect to $k$ , $k = 0$ is evident:

$$
\mathrm { d } f ( X ) = L _ { X } f , \quad f \in C ^ { \infty } ( \mathbf { R } ^ { n } ) = \Omega ^ { 0 } ( \mathbf { R } ^ { n } ) .
$$

Suppose $2 ^ { \circ }$ holds for $k - 1$ . Then for $k$ , by $1 ^ { \circ }$ ,

$$
\begin{array} { r l } { \displaystyle \mathrm { d } \omega ( X _ { 0 } , X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) } & { = ( i _ { X _ { 0 } } \mathrm { d } \omega ) ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) } \\ { \displaystyle } & { = ( L _ { X _ { 0 } } \omega ) ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) - ( \mathrm { d } i _ { X _ { 0 } } \omega ) ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) } \\ { \displaystyle } & { = L _ { X _ { 0 } } \big ( \omega ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) \big ) - \displaystyle \sum _ { i = 1 } ^ { k } \omega ( X _ { 1 } , \cdot \cdot \cdot , L _ { X _ { 0 } } X _ { i } , \cdot \cdot \cdot , X _ { k } ) } \\ { \displaystyle } & { \quad - ( \mathrm { d } i _ { X _ { 0 } } \omega ) ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) , } \end{array}
$$

where $i _ { X _ { 0 } } \omega \in \Omega ^ { k - 1 } ( \mathbf { R } ^ { n } )$ . By inductive hypothesis,

$$
\begin{array} { l } { { ( \mathrm { d } i _ { X _ { 0 } } \omega ) ( X _ { 1 } , \cdot \cdot \cdot , X _ { k } ) } } \\ { { \displaystyle = \sum _ { i = 1 } ^ { k } ( - 1 ) ^ { i - 1 } L _ { X _ { i } } \left( i _ { X _ { 0 } } \omega ( X _ { 1 } , \cdot \cdot \cdot , \widehat { X } _ { i } , \cdot \cdot , X _ { k } ) \right) } } \\ { { \displaystyle \quad + \sum _ { 1 \leq i \leq j \leq k } ( - 1 ) ^ { i + j } i _ { X _ { 0 } } \omega ( L _ { X _ { i } } X _ { j } , X _ { 1 } , \cdot \cdot \cdot , \widehat { X } _ { i } , \cdot \cdot \cdot , \widehat { X } _ { j } , \cdot \cdot \cdot , X _ { k } ) } } \end{array}
$$

$$
\begin{array} { l } { \displaystyle = \sum _ { i = 1 } ^ { k } ( - 1 ) ^ { i - 1 } L _ { X _ { i } } \left( \omega ( X _ { 0 } , X _ { 1 } , \cdots , \widehat { X } _ { i } , \cdots , X _ { k } ) \right) } \\ { \displaystyle \quad + \sum _ { 1 \leq i \leq j \leq k } ( - 1 ) ^ { i + j - 1 } \omega ( L _ { X _ { i } } X _ { j } , X _ { 0 } , \cdots , \widehat { X } _ { i } , \cdots , \widehat { X } _ { j } , \cdots , X _ { k } ) . } \end{array}
$$

Thus, we get

$$
\begin{array} { l } { \displaystyle \mathrm { d } \omega ( X _ { 0 } , \cdot \cdot , X _ { k } ) } \\ { = L _ { X _ { 0 } } ( \omega ( X _ { 1 } , \cdot \cdot , X _ { k } ) ) + \displaystyle \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j _ { w } } ( X _ { 1 } , \cdot \cdot , L _ { X _ { 0 } } X _ { j } , \cdot \cdot , X _ { k } ) } \\ { \displaystyle } \\ { \displaystyle \quad + \sum _ { i = 1 } ^ { k } ( - 1 ) ^ { i _ { L } } L _ { X _ { i } } ( \omega ( X _ { 0 } , \cdot \cdot , \hat { X _ { i } } , \cdot , \cdot , X _ { k } ) ) } \\ { \displaystyle \quad + \sum _ { 1 \leq i < j < k } ( - 1 ) ^ { i + i _ { \omega } } ( L _ { X _ { i } } X _ { j } , X _ { 0 } , \cdot \cdot , \hat { X _ { i } } , \cdot \cdot , \hat { X _ { j } } , \cdot \cdot , X _ { k } ) } \\ { \displaystyle } \\ { = \displaystyle \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { i } L _ { X _ { i } } ( \omega ( X _ { 0 } , \cdot \cdot , \hat { X _ { i } } , \cdot , \cdot , X _ { k } ) ) } \end{array}
$$$$
\begin{array} { l } { { \displaystyle = \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { i } L _ { X _ { i } } \left( \omega ( X _ { 0 } , \cdot \cdot \cdot , \widehat { X } _ { i } , \cdot \cdot , X _ { k } ) \right) } } \\ { { \displaystyle \quad + \sum _ { i < j } ( - 1 ) ^ { i + j } \omega ( L _ { X _ { i } } X _ { j } , X _ { 0 } , \cdot \cdot \cdot , \widehat { X } _ { i } , \cdot \cdot \cdot , \widehat { X } _ { j } , \cdot \cdot \cdot , X _ { k } ) . } } \end{array}
$$

Finally , the theorem is completed.

# Bibliography

[AA88] D.V. Anosov and V.I. Arnold: Dynamical Systems I. Springer, Berlin, (1988).   
[AA89] V. I. Arnold and A. Avez: Ergodic Problems of Classical Mechanics. Addison-Wesley and Benjamin Cummings, New York, (1989).   
[Abd99] S. S. Abdullaev: A new integration method of Hamiltonian systems by symplectic maps. J. Phys. A: Math. Gen., 32(15):2745–2766, (1999).   
[Abd02] S. S. Abdullaev: The Hamilton–Jacobi method and Hamiltonian maps. J. Phys. A: Math. Gen., 35(12):2811–2832, (2002).   
[AKN78] V. I. Arnold, V. V. Kozlov, and A. I. Neishtadt: Mathematical Aspects of Classical and Celestial Mechanics. Springer, Berlin, Second edition, (1978).   
[AM78] R. Abraham and J. E. Marsden: Foundations of Mechanics. Addison-Wesley, Reading, MA,Second edition, (1978).   
[AMR88] R. Abraham, J. E. Marsden, and T. Ratiu: Manifolds, Tensor Analysis, and Applications. AMS 75. Springer-Verlag, Berlin, Second edition, (1988).   
[AN90] A. I. Arnold and S.P. Novikov: Dynamical System IV. Springer Verlag, Heidelberg, (1990).   
[AP92] D. K. Arrowsmith and C. M. Place: Dynamical Systems: Differential Equations, Maps, and Chaotic Behavior. Chapman & Hall, New York, (1992).   
[Arn78] V. I. Arnold: Ordinary Differential Equations. The MIT Press, New York (1978).   
[Arn88] V. I. Arnold: Geometrical Methods in the Theory of Ordinary Differential Equations. Springer-Verlag, Berlin, (1988).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Berlin Heidelberg: Springer-Verlag, GTM 60, Berlin ,Second edition, (1989).   
[Ber00] R. Berndt: An Introduction to Symplectic Geometry. AMS Providence, Rhode Island, (2000).   
[Bir23] G. D. Birkhoff: Relativity and Modern Physics. Harvard Univ. Press, Cambridge, Mass., Second edition, (1923).   
[BK89] G.W. Bluman and S. Kumei: Symmetries and Differential Equations. AMS 81. Springer-Verlag, New York, (1989).   
[Car65] C. Carathe’odory: Calculus of Variation and Partial Differential Equations of First Order, Vol.1. Holden-Day, San Franscisco, (1965).   
[Car70] H. Cartan: Differential Forms. Houghton-Mifflin, Boston, (1970).   
[Che53] S. S. Chern: Differential Manifolds. Lecture notes. University of Chicago, (1953).   
[Ede85] D. G. B Edelen: Applied Exterior Calculus. John Wiley and Sons, New York, First edition, (1985).   
[Fla] H. Flanders: Differential Forms. Academie Press, New York, Second edition. (1963).   
[GS84] V. Guillemin and S. Sternberg: Symplectic Techniques in Physics. Cambridge University Press, Cambridge, (1984).   
[Lan95] S. Lang: Differential and Riemannian Manifolds. Springer-Verlag, New York, (1995).   
[LM87] P. Libermann and C.M. Marle: Symplectic Geometry and Analytical Mechanics. Reidel Pub. Company, Boston, First edition, (1987).   
[Mac70] S. MacLanc: Hamiltonian mechanics and geometry. Amer. Math. Mon., 77(6):570– 586, (1970).   
[Poi93] H. Poincare:´ Les Methodes Nouvelles de la M ´ ecanique C ´ eleste, Tome II ´ . Gauthier-Villars, Paris, Second edition, (1893).   
[Poi99] H. Poincare:´ Les Methodes Nouvelles de la M ´ ecanique C ´ eleste. Tome III ´ . Gauthiers-Villars, Paris, Second edition, (1899).   
[Sc77] M. Schreiber: Differential Forms. Springer-Verlag, New York, First edition, (1977).   
[Sie43] C.L. Siegel: Symplectic geometry. Amer.and math. J. Math, 65:1–86, (1943).   
[Spi68] M. Spivak: Calculus on Manifolds. The Benjamin/Cummings publishing company, London, New York, First edition, (1968).   
[Tre75] F. Treves: Pseodo-Differential Operator. Acad. Press, New York, First edition, (1975).   
[Wei77] A. Weinstein: Lectures on symplectic manifolds. In CBMS Regional Conference, 29. American Mathematical Society, Providence, RI, (1977).   
[Wes81] C. Von. Westenholz: Differential Forms in Mathmatical Physics. North-Holland, Amsterdam, Second edition, (1981).
