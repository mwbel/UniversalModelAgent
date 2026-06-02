# Chapter 2. Symplectic Algebra and Geometry Preliminaries

In order to deeply understand Hamiltonian mechanics, it is necessary to know basic concepts of symplectic algebra and geometry.

# 2.1 Symplectic Algebra and Orthogonal Algebra

Symplectic algebra and orthogonal algebra have several similar concepts. First, we start with the bilinear form.

# 2.1.1 Bilinear Form

# 1. Bilinear form

Definition 1.1 (Bilinear Form). Let $\mathbf { F } ^ { n }$ be an $n$ -dimensional linear space. A bilinear form on $\mathbf { F } ^ { n }$ is a mapping $\varphi : \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } \mapsto \mathbf { F } ^ { n }$ that satisfies:

$1 ^ { \circ }$ $\varphi ( \alpha u + \beta v , y ) = \alpha \varphi ( u , y ) + \beta \varphi ( v , y )$ . $2 ^ { \circ }$ $\begin{array} { r } { \varphi ( x , \alpha u + \beta v ) = \alpha \varphi ( x , u ) + \beta \varphi ( x , v ) , \ \forall \alpha , \ \beta \in \mathbf { F } , \ u , v , x , y \in \mathbf { F } ^ { n } . } \end{array}$

It is obvious that there exists a 1-1 correspondence between the matrix space $M ( n , \mathbf { F } )$ and the space of the bilinear form on $\mathbf { F } ^ { n }$ . As a matter of fact, given a matrix $A \in$ $M ( n , \mathbf { F } )$ , there is a bilinear form $\varphi _ { A }$ on $\mathbf { F } ^ { n }$ corresponding to

$$
\varphi _ { A } ( x , y ) = x ^ { \prime } A y = \sum _ { i , j = 1 } ^ { n } a _ { i j } x _ { i } y _ { j } .
$$

Conversely, given a bilinear form on $\mathbf { F } ^ { n }$ , there is also a matrix $A \in M ( n , \mathbf { F } )$ corresponding to

$$
A = A _ { \varphi } = [ a _ { i j } ] = [ \varphi ( e _ { i } , e _ { j } ) ] \in M ( n , \mathbf { F } ) ,
$$

such that $\varphi ( x , y ) = x ^ { \prime } A y$ , where $e _ { 1 } , e _ { 2 } , \cdots$ is a set of basis of $\mathbf { F } ^ { n }$ .

Definition 1.2 (Symmetric or Antisymmetric). A bilinear form $\varphi = \varphi _ { A }$ is called symmetric or antisymmetric if

$$
\varphi ( x , y ) = \varphi ( y , x ) \quad { \mathrm { o r } } \quad \varphi ( x , y ) = - \varphi ( y , x ) , \quad \forall x , y \in \mathbf { F } ^ { n } ,
$$

i.e., $A ^ { \prime } = A$ , $A ^ { \prime } = - A$ , respectively.

Definition 1.3 (Conformally Symmetric). A bilinear form $A$ is called conformally symmetric if

$$
\varphi ( x , y ) = 0 \Longleftrightarrow \varphi ( y , x ) = 0 ,
$$

i.e.,

$$
\{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } \mid \varphi ( x , y ) = 0 \} = \{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } \mid \varphi ( y , x ) = 0 \} .
$$

A matrix $A$ is called conformally symmetric if $x ^ { \prime } A y = 0 \Leftrightarrow x ^ { \prime } A ^ { \prime } y = 0$ , which is equivalent to saying that $\varphi _ { A }$ is conformally symmetric.

$\varphi$ is a non-degenerate map (or non-singular) if $\exists x \neq 0$ s.t. $\varphi ( x , y ) = 0$ , $\forall y \in \mathbf { F } ^ { n }$

Proposition 1.4. It is evident that the following claims are equivalent:

$1 ^ { \circ }$ $\varphi _ { A }$ is non-degenerate.   
2◦ If $\forall y \in \mathbf { F } ^ { n }$ , $\varphi _ { A } ( x , y ) = 0$ , then $x = 0$ .   
$3 ^ { \circ }$ $A$ is non-degenerate.

Definition 1.5 (Conformally Identical). A bilinear form $\varphi _ { A }$ is called conformally identical to $\varphi _ { B }$ if

$$
\{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } | \varphi _ { A } ( x , y ) = 0 \} = \{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } | \varphi _ { B } ( y , x ) = 0 \} .
$$

Proposition 1.6. The following claims are equivalent:

$1 ^ { \circ }$ $\varphi _ { A }$ is conformally identical to $\varphi _ { B }$ .   
$2 ^ { \circ }$ $\varphi _ { A } ( x , y ) = 0$ , iff $\varphi _ { B } ( x , y ) = 0$ .   
3◦ $x ^ { \prime } A y = 0$ , iff $x ^ { \prime } B y = 0$ .   
$4 ^ { \circ }$ $\exists \mu \in F , \mu \neq 0$ , such that $A = \mu B$ .

The equivalence of $1 ^ { \circ }$ , $2 ^ { \circ }$ and $3 ^ { \circ }$ is trivial. Next, we prove the equivalence between $1 ^ { \circ }$ and $4 ^ { \circ }$ .

Theorem 1.7. $\{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } | \varphi _ { A } ( x , y ) = 0 \} = \{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } | $ $\varphi _ { B } ( y , x ) = 0 \}$ ,   
iff $\exists \mu \in \mathbf { F } , \mu \neq 0$ , such that $A = \mu B$ .

Proof. The sufficiency is trivial. We only need to prove the necessity. Without loss of generality, we can assume $\mathbf { F } = \mathbf { R }$ . Then, we have

$$
\begin{array} { r l } & { \ker ( A ) = \{ y \in { \bf R } ^ { n } \mid A y = 0 \} = \{ y \in { \bf R } ^ { n } \mid x ^ { \prime } A y = 0 , \forall x \in { \bf R } ^ { n } \} , } \\ & { \ker ( B ) = \{ y \in { \bf R } ^ { n } \mid B y = 0 \} = \{ y \in { \bf R } ^ { n } \mid x ^ { \prime } B y = 0 , \forall x \in { \bf R } ^ { n } \} . } \end{array}
$$

By our assumption, $x ^ { \prime } A y = 0 \Leftrightarrow x ^ { \prime } B y = 0$ . Hence, $\ker ( A ) = \ker ( B )$ , denoted as $V$ , i.e., $V = \ker ( A ) = \ker ( B )$ . Then $\forall v \in \mathbf { R } ^ { n }$ ,

$$
A v \neq 0 \Longleftrightarrow B v \neq 0 .
$$

Since $x ^ { \prime } A y = 0 \Leftrightarrow x ^ { \prime } B y = 0 , \{ A v \} ^ { \perp } = \{ B v \} ^ { \perp }$ , and so

$$
\{ A v \} = \{ B v \} .
$$

This shows that there exists $\boldsymbol { \mu } ( v ) \in \mathbf { R }$ , $\mu \neq 0$ such that $A v = \mu ( v ) B v$ .

Next, we show $\mu ( v )$ is a non-zero constant.

Take a basis of $\mathbf { R } ^ { n } = \{ v _ { 1 } , \cdot \cdot \cdot , v _ { r } , v _ { r + 1 } , \cdot \cdot \cdot , v _ { n } \}$ , such that

$$
\left\{ v _ { r + 1 } , \cdot \cdot \cdot , v _ { n } \right\} = V = \ker ( A ) = \ker ( B ) .
$$

Thus, $A v _ { i } \neq 0 ( i = 1 , \cdots , r )$ , $A ( v _ { 1 } + v _ { 2 } + \cdot \cdot \cdot + v _ { r } ) \neq 0 .$ .

The above shows that there exist $\mu _ { 1 } , \cdots , \mu _ { r } , \mu _ { { \scriptscriptstyle  { p l } } }$ $\mu$ (all of which are no-zero), such that

$$
\begin{array} { r l } & { A v _ { i } = \mu _ { i } B v _ { i } , \quad i = 1 , \cdots , r , } \\ & { } \\ & { A ( v _ { 1 } + v _ { 2 } + \cdots + v _ { r } ) = \mu B ( v _ { 1 } + v _ { 2 } + \cdots + v _ { r } ) . } \end{array}
$$

Then,

$$
\begin{array} { l } { \mu _ { 1 } B v _ { 1 } + \cdot \cdot \cdot + \mu _ { r } B v _ { r } \ = \ \mu B ( v _ { 1 } + v _ { 2 } + \cdot \cdot \cdot + v _ { r } ) } \\ { \qquad } \\ { \qquad = \ \mu B v _ { 1 } + \cdot \cdot \cdot + \mu B v _ { r } . } \end{array}
$$

After manipulation, we get $( \mu _ { 1 } - \mu ) B v _ { 1 } + \cdot \cdot \cdot + ( \mu _ { r } - \mu ) B v _ { r } = 0 .$ , i.e.,

$$
B \left( ( \mu _ { 1 } - \mu ) v _ { 1 } + \cdot \cdot \cdot + ( \mu _ { r } - \mu ) v _ { r } \right) = 0 .
$$

Since $( \mu _ { 1 } - \mu ) v _ { 1 } + \cdot \cdot \cdot + ( \mu _ { r } - \mu ) v _ { r } \in \{ v _ { 1 } , \cdot \cdot \cdot , v _ { r } \}$ , it must be

$$
( \mu _ { 1 } - \mu ) v _ { 1 } + \cdot \cdot \cdot + ( \mu _ { r } - \mu ) v _ { r } = 0 .
$$

Then by the linear independence of $v _ { 1 } , \cdots , v _ { r }$ , we have

$$
\mu = \mu _ { 1 } = \cdot \cdot \cdot = \mu _ { r } .
$$

Therefore,

$$
A v _ { i } = \mu B v _ { i } , \quad i = 1 , \cdot \cdot \cdot , r .
$$

Similarly for $i = r + 1 , \cdot \cdot \cdot , n , A v _ { i } = 0 = \mu B v _ { i }$ . Thus, we have obtained $A = \mu B$ . -

From Theorem 1.7, we can easily derive the following theorems.

Theorem 1.8. $\varphi _ { A }$ is conformally symmetric, iff ∃ $\boldsymbol { \mu } \in \mathbf { F }$ , $\mu \neq 0$ , such that $A ^ { \prime } = \mu A$ .

Theorem 1.9. $A \in M ( n , \mathbf { R } )$ is conformally symmetric, iff $A ^ { \prime } = \pm A$ , i.e., $A$ is symmetric or antisymmetric.

# 2. Quadratic forms induced by bilinear form

Given a bilinear form $\varphi _ { A } ( x , y ) = \sum _ { i , j } ^ { n } a _ { i j } x _ { i } y _ { j }$ , we can get a quadratic bilinear form $\varphi _ { A } ( x , x ) = \sum _ { i , j } ^ { n } a _ { i j } x _ { i } x _ { j }$ . Obviously, we have the following propositions:


<!-- chunk 0003: pages 141-210 -->
Proposition 1.10. $\varphi _ { A } ( x + y , x + y ) - \varphi _ { A } ( x , x ) - \varphi _ { A } ( y , y ) = \varphi _ { A } ( x , y ) + \varphi _ { A } ( y , x ) .$

Proposition 1.11. $\varphi _ { A }$ is antisymmetric, iff $\varphi _ { A } ( x , x ) = 0$ , $\forall x \in \mathbf { F } ^ { n }$ .

Proposition 1.12. $\forall x \in \mathbf { F } ^ { n } , \varphi _ { A } ( x , x ) = \varphi _ { B } ( x , x ) ,$ , iff $A + A ^ { \prime } = B + B ^ { \prime }$ .

Proposition 1.13. If $A = A ^ { \prime } , B = B ^ { \prime }$ , then $\forall x \in \mathbf { F } ^ { n }$ , $\varphi _ { A } ( x , x ) = \varphi _ { B } ( x , x ) \Leftrightarrow$ $A = B$ .

Proposition 1.14. The following assertions are equivalent :

$1 ^ { \circ }$ $\varphi _ { A } = \varphi _ { B }$ .   
$2 ^ { \circ }$ $\left\{ \left\{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } \mid \varphi _ { A } ( x , y ) = 1 \right\} = \big \{ ( x , y ) \in \mathbf { F } ^ { n } \times \mathbf { F } ^ { n } \mid \varphi _ { B } ( x , y ) = 1 \big \} . \right.$ $3 ^ { \circ }$ $\varphi _ { A } ( x , y ) = 1 \Leftrightarrow \varphi _ { B } ( x , y ) = 1$ .   
$4 ^ { \circ }$ $x ^ { \prime } A y = 1 \Leftrightarrow x ^ { \prime } B y = 1 .$ .

# 2.1.2 Sesquilinear Form

# 1. Sesquilinear form

In a complex field $\mathbf { C }$ , there is an automorphism

$$
{ \textbf { C } } \ni z = x + { \mathrm { i } } y \mapsto { \overline { { z } } } = x - { \mathrm { i } } y \in { \bf C } ,
$$

such that

$$
{ \overline { { z _ { 1 } \cdot z _ { 2 } } } } = { \overline { { z _ { 1 } } } } \cdot { \overline { { z _ { 2 } } } } , \quad { \overline { { z _ { 1 } + z _ { 2 } } } } = { \overline { { z _ { 1 } } } } + { \overline { { z _ { 2 } } } } .
$$

This leads to a new kind of binary forms.

Definition 1.15 (Sesquilinear). A sesquilinear form on $\mathbf { C } ^ { n }$ is a mapping $\phi : \mathbf { C } ^ { n } \times \mathbf { \Sigma }$ ${ \bf C } ^ { n } \mapsto { \bf C }$ , such that for all $u , v , x \in \mathbf { C } ^ { n }$ , $\alpha , \beta \in \mathbf { C }$ , we have

$1 ^ { \circ }$ ${ \mathrm {  ~ \Sigma ~ } } ^ { \circ } \quad \phi ( \alpha u + \beta v , x ) = \overline { { \alpha } } \phi ( u , x ) + \overline { { \beta } } \phi ( v , x ) .$ .   
$2 ^ { \circ }$ $\phi ( x , \alpha u + \beta v ) = \alpha \phi ( x , u ) + \beta \phi ( x , v )$ .

Similarly, there exists a 1-1 correspondence between the complex matrix space $M ( n , \mathbf { C } )$ and the space of sesquilinear forms on $\mathbf { C } ^ { n }$ .

In fact, a complex matrix $A \ \in \ M ( n , \mathbf { C } )$ has a natural correspondence to a sesquilinear form $\phi _ { A }$ , which satisfies

$$
\phi _ { A } ( x , y ) = x ^ { * } A y = \sum _ { i , j } ^ { n } a _ { i j } { \overline { { x } } } _ { i } y _ { j } .
$$

Conversely, a sequilinear form $\phi$ has a natural correspondence to a complex matrix

$$
A = A _ { \phi } = [ a _ { i j } ] = [ \phi ( e _ { i } , e _ { j } ) ] \in M ( n , \mathbf { C } ) ,
$$

which satisfies $\phi ( x , y ) = x ^ { * } A _ { \phi } y$ .

Definition 1.16 (Hermitian). $\phi = \phi _ { A }$ is Hermitian or anti-Hermitian, if $\forall x , y \in$ $\mathbf { C } ^ { n } , \phi ( x , y ) = \overline { { \phi ( y , x ) } }$ or $\phi ( x , y ) = - { \overline { { \phi ( y , x ) } } }$ , i.e., $A ^ { * } = A$ or $A ^ { * } = - A$ . Such a complex matrix $A$ is called Hermitian or anti-Hermitian.

Definition 1.17 (Conformally Hermitian). $\phi = \phi _ { A }$ is called conformally Hermitian, if $\phi ( x , y ) = 0 \Leftrightarrow { \overline { { \phi ( y , x ) } } } = 0$ , then

$$
\{ ( x , y ) \in \mathbf { C } ^ { n } \times \mathbf { C } ^ { n } \mid \phi ( x , y ) = 0 \} = \{ ( x , y ) \in \mathbf { C } ^ { n } \times \mathbf { C } ^ { n } \mid { \overline { { \phi ( y , x ) } } } = 0 \} ,
$$

or

$$
x ^ { * } A y = 0 \Longleftrightarrow x ^ { * } A ^ { * } y = 0 .
$$

The matrix $A$ satisfying the above condition is called conformally Hermitian.

$\phi = \phi _ { A }$ is non-degenerate iff $\ b { \nexists x } \in \mathbf { C } ^ { n }$ , $x \neq 0$ , such that $\phi _ { A } ( x , y ) = 0 , \forall y \in$ $\mathbf { C } ^ { n }$ ; or iff $\forall y \in \mathbf { C } ^ { n }$ , $\phi ( x , y ) = 0 $ , then $x = 0$ ; or iff $A$ is non-degenerate.

# 2. Hermitian forms induced by sesquilinear forms

From a sesquilinear form on $\mathbf { C } ^ { n }$ , $\stackrel { \textstyle \cdot \textmd {  } } { \phi _ { A } ( x , y ) } = x ^ { * } A y = \sum _ { i , j } ^ { n } a _ { i j } \overline { { x _ { i } } } y _ { j }$ , we can induce a correspondent Hermitian form on $\mathbf { C } ^ { n }$ ,

$$
\phi _ { A } ( x , x ) = x ^ { * } A x = \sum _ { i , j } ^ { n } a _ { i j } { \overline { { x _ { i } } } } x _ { j } .
$$

If $A$ is Hermitian, then $\forall x \in \mathbf { C } ^ { n }$ , $\phi _ { A } ( x , x ) \in \mathbf { R }$ .

Remark 1.18. Hermitian forms have properties similar to Propositions 1.10 – 1.14, and Theorems 1.7 – 1.8.

Remark 1.19. Hermitian analogue of Theorem 1.9 as follows.

Theorem 1.20. $A \in M ( n , \mathbf { C } )$ is conformally Hermitian, iff $\exists \mu \in \mathbf { C }$ , $| \mu | = 1$ , such that $A ^ { * } = \mu A$ ; or iff $\exists \theta \in \mathbf { R }$ , such that $A ^ { * } = e ^ { \mathbf { i } \theta } A$ .

$$
A = A ^ { * * } = \overline { { \mu } } A ^ { * } = \overline { { \mu } } \mu A = | \mu | ^ { 2 } A . \operatorname { T h u s } , | \mu | ^ { 2 } = 1 .
$$

# 2.1.3 Scalar Product, Hermitian Product

A scalar product on $\mathbf { F } ^ { n }$ is a non-degenerate conformally symmetric bilinear form $\phi _ { G } ( x , y )$ , where $G ^ { \prime } = \pm G$ .

Symmetric products in $\mathbf { R } ^ { n } : ( x , y ) _ { S } = \varphi _ { S } ( x , y ) = x ^ { \prime } S y$ , $S ^ { \prime } = S$ , $| S | \neq 0$ . Anti-symmetric product in $\mathbf { R } ^ { n }$ : $[ x , y ] _ { K } = \varphi _ { K } ( x , y ) = x ^ { \prime } K y , K ^ { \prime } = - K , | K | \neq$ 0.

Remark 1.21. There does not exist any anti-symmetric scalar product in $\mathbf { F } ^ { 2 n + 1 }$ since $| K | = 0$ if $K ^ { \prime } = - K$ .

Hermitian products in $\mathbf { C } ^ { n }$ are non-degenerate Hermitian forms in $\mathbf { C } ^ { n }$ , i.e.,

$$
\langle x , y \rangle = x ^ { * } G y = \phi _ { G } ( x , y ) , \quad G ^ { * } = G , \quad | G | \neq 0 .
$$

Typical Examples are given below:

Example 1.22 (Symmetric case). Euclidean scalar product (Euclidean form) in $\mathbf { R } ^ { n }$ :

$$
( x , y ) = ( x , y ) _ { I } = x ^ { \prime } y = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } , \quad I ^ { \prime } = I .
$$

This induces a Euclidean length measure $| x | ^ { 2 } = ( x , x ) = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } .$

Example 1.23 (Anti-symmetrical case). Standard symplectic scalar product (symplectic form) in $\mathbf { R } ^ { 2 n }$ :

$$
[ x , y ] = [ x , y ] _ { J } = x ^ { \prime } J y = \sum _ { i = 1 } ^ { n } ( x _ { i } y _ { n + i } - x _ { n + i } y _ { i } ) ,
$$

where

$$
J = \left[ \begin{array} { c c } { 0 } & { I _ { n } } \\ { - I _ { n } } & { 0 } \end{array} \right] = J _ { 2 n } , \quad J ^ { \prime } = J ^ { - 1 } = - J .
$$

As $n = 1$ , we have

$$
[ x , y ] = x _ { 1 } y _ { 2 } - x _ { 2 } y _ { 1 } = { \left| \begin{array} { l l } { x _ { 1 } } & { y _ { 1 } } \\ { x _ { 2 } } & { y _ { 2 } } \end{array} \right| } ,
$$

which represents the oriented area of the parallelogram formed by the vector $x , y$ in $\mathbf { R } ^ { 2 }$ (see the image below).

For general $n$ , we get

$$
[ x , y ] = x ^ { \prime } J y = \sum _ { i = 1 } ^ { n } \left| { \begin{array} { c c } { x _ { i } } & { y _ { i } } \\ { x _ { n + i } } & { y _ { n + i } } \end{array} } \right|
$$

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0003_pages_0141-0210/auto/images/145c49174d740972f68567e8162e7fe3797696fb71079db99dda6a05396ed998.jpg)

which represents a sum of oriented areas of the parallelograms formed by projecting vectors $x , y \in \mathbf { R } ^ { 2 n }$ to the $( x _ { i } , x _ { n + i } )$ coordinate planes.

Remark 1.24 (Pfaffian theorem). For any $n$ , there exists a polynomial $P _ { n } ( x _ { i j } )$ with integer coefficients in variables $x _ { i j } ( i < j )$ such that

$$
\operatorname* { d e t } K = \operatorname* { d e t } \left[ k _ { i j } \right] = \left[ P _ { n } ( k _ { i j } ) \right] ^ { 2 } , \quad \forall \mathrm { a n t i \mathrm { - } s y m m e t r i c ~ m a t r i x ~ } K .
$$

Example 1.25 (Hermitian case). Unitary product in $\mathbf { C } ^ { n }$ :

$$
\langle w , z \rangle = \langle w , z \rangle _ { I } = w ^ { \ast } I z = w ^ { \ast } z , \quad w , z \in \mathbf { C } ^ { n } , I ^ { \ast } = I ,
$$

$\langle w , z \rangle$ induces $\| z \| = z ^ { \ast } z$ , which is the Euclidean length measure in $\mathbf { C } ^ { n }$ .

# 2.1.4 Invariant Groups for Scalar Products

This topic is discussed in detail in books[Wey39,Wey40,Art57] .

General linear group: $G L ( n , \mathbf { F } ) { = } \{ A \in M ( n , \mathbf { F } ) \mid { \operatorname* { d e t } A } \neq 0 \} .$ Special linear group: $S L ( n , \mathbf { F } ) { = } \{ A \in G L ( n , \mathbf { F } ) \mid { \mathrm { d e t } } A { = } 1 \}$ .

Orthogonal group: invariant group for the Euclidean scalar product $( x , y ) { = } \varphi _ { I } ( x , y ) =$ $x ^ { \prime } y$ ,

$$
O ( n , \mathbf { F } ) = \{ A \in G L ( n , \mathbf { F } ) \mid ( A x , A y ) = ( x , y ) , \forall x , y \in \mathbf { F } ^ { n } \} .
$$

From definition, we have

$$
A \in O ( n , \mathbf { F } ) \Longleftrightarrow A ^ { \prime } I A = A ^ { \prime } A = I .
$$

In particular, we denote $O ( n , \mathbf { R } )$ as $O ( n )$ , i.e., $O ( n , \mathbf { R } ) \equiv O ( n )$ .

Symplectic group: invariant group for the anti-symmetric scalar product $[ x , y ] =$ $\varphi _ { J } ( x , y ) = x ^ { \prime } J y$ ,

$$
S p ( 2 n , \mathbf { F } ) = \big \{ A \in G L ( 2 n , \mathbf { F } ) \mid [ A x , A y ] = [ x , y ] , \forall x , y \in \mathbf { F } ^ { 2 n } \big \} .
$$

From definition, we have

$$
A \in S p ( n , \mathbf { F } ) \Longleftrightarrow \bar { A } ^ { \prime } J A = J .
$$

We denote $S p ( n , \mathbf { F } ) \equiv S p ( n )$ .

Unitary group: invariant group for the Hermitian scalar product $\langle x , y \rangle { = } x ^ { * } y$

$$
U ( n , \mathbf { C } ) = \big \{ A \in G L ( n , \mathbf { C } ) \mid \langle A x , A y \rangle = \langle x , y \rangle , \forall x , y \in \mathbf { C } ^ { n } \big \} .
$$

From definition, we have

$$
A \in U ( n , \mathbf { C } ) \Longleftrightarrow A ^ { * } I A = I .
$$

Similarly, we denote $U ( n , \mathbf { C } ) \equiv U ( n )$

Invariant Group for Scalar Product $\varphi _ { G } , \phi _ { G }$ .

Here:

$$
\begin{array} { l l } { { \varphi _ { G } ( x , y ) = x ^ { \prime } G y , } } & { { G ^ { \prime } = \pm G , | G | \neq 0 , } } \\ { { { } } } & { { { } } } \\ { { \phi _ { G } ( x , y ) = x ^ { * } G y , } } & { { G ^ { * } = G , | G | \neq 0 . } } \end{array}
$$

The invariant group for $\varphi _ { G }$ is

$$
{ \begin{array} { l } { G ( G , n , \mathbf { F } ) \ = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid \varphi _ { G } ( A x , A y ) = \varphi _ { G } ( x , y ) , \forall x , y \in \mathbf { F } ^ { n } \right\} } \\ { = \ \left\{ A \in G L ( n , \mathbf { C } ) \mid A ^ { \prime } G A = G \right\} } \\ { = \ \left\{ A \in G L ( n , \mathbf { C } ) \mid A ^ { - 1 } = G ^ { - 1 } A ^ { \prime } G \right\} . } \end{array} }
$$

The symmetric case $G = S , S ^ { \prime } = S , \varphi _ { S } ( x , y ) = ( x , y ) _ { S } = x ^ { \prime } S y$ , where $G$ is called an $S$ -orthogonal group.

$$
{ \begin{array} { l } { O ( S , n , \mathbf { F } ) \ = \ G ( S , n , \mathbf { F } ) } \\ { \ } \\ { \qquad = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid ( A x , A y ) _ { S } = ( x , y ) _ { S } , \forall x , y \in \mathbf { F } ^ { n } \right\} } \\ { \qquad = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid A ^ { \prime } S A = S \right\} } \\ { \ } \\ { \qquad = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid A ^ { - 1 } = S ^ { - 1 } A ^ { \prime } S \right\} . } \end{array} }
$$

Special case: ${ \cal O } ( \bar { I } , n , { \bf F } ) \equiv { \cal O } ( n , { \bf F } )$ .

Anti-symmetrical case: $G = K , K ^ { \prime } = - K , \varphi _ { K } ( x , y ) = [ x , y ] _ { K } = x ^ { \prime } K y$ , where $G$ is called a $K$ -symplectic group.

$$
{ \begin{array} { l } { S p ( K , n , \mathbf { F } ) \ = \ G ( K , 2 n , \mathbf { F } ) } \\ { \ = \ \left\{ A \in G L ( 2 n , \mathbf { F } ) \mid [ A x , A y ] _ { K } = [ x , y ] _ { K } , \forall x , y \in \mathbf { F } ^ { 2 n } \right\} } \\ { \ = \ \left\{ A \in G L ( 2 n , \mathbf { F } ) \mid A ^ { \prime } K A = K \right\} } \\ { \ = \ \left\{ A \in G L ( 2 n , \mathbf { F } ) \mid A ^ { - 1 } = K ^ { - 1 } A ^ { \prime } K \right\} . } \end{array} }
$$

Special case: $S p ( J , 2 n , \mathbf { F } ) \equiv S p ( 2 n , \mathbf { F } )$ .

Hermitian case:

$$
\begin{array} { r c l } { { } } & { { { \cal G } } } & { { = } } & { { { \cal H } \in { \cal M } ( n , { \bf C } ) , { \cal H } ^ { * } = { \cal H } , | { \cal H } | \neq 0 , \phi _ { \cal H } ( x , y ) = \langle x , y \rangle _ { { \cal H } } = 0 , } } \\ { { } } & { { } } & { { { \cal U } ( { \cal H } , n , { \bf C } ) } } \\ { { } } & { { } } & { { = } } & { { \left\{ A \in { \cal G L } ( n , { \bf C } ) \mid \langle A x , A y \rangle _ { { \cal H } } = \langle x , y \rangle _ { { \cal H } } , \forall x , y \in { \bf C } ^ { n } \right\} } } \\ { { } } & { { } } & { { = } } & { { \left\{ A \in { \cal G L } ( n , { \bf C } ) \mid A ^ { * } { \cal H } A = { \cal H } \right\} } } \\ { { } } & { { } } & { { = } } & { { \left\{ A \in { \cal G L } ( n , { \bf F } ) \mid A ^ { - 1 } = { \cal H } ^ { - 1 } A ^ { * } { \cal H } \right\} . } } \end{array}
$$

Special case: $U ( I , n , \mathbf { C } ) \equiv U ( n , \mathbf { C } ) \equiv U ( n )$ .

Conformally Invariant Group for scalar Product $\varphi _ { G }$

$$
{ \begin{array} { r l } { C G ( G , n , \mathbf { F } ) \ = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid \varphi _ { G } ( A x , A y ) = 0 \Longleftrightarrow \varphi _ { G } ( x , y ) = 0 \right\} } \\ { = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid \exists \mu \in \mathbf { F } , \mu \neq 0 , { \mathrm { s u c h ~ t h a t } } A ^ { \prime } G A = \mu G \right\} } \\ { = \ \left\{ A \in G L ( n , \mathbf { F } ) \mid \exists \mu \in \mathbf { F } , \mu ^ { - 1 } \neq 0 , A ^ { - 1 } = \mu ^ { - 1 } G ^ { - 1 } A ^ { \prime } G \right\} . } \end{array} }
$$

When $G = S , S ^ { \prime } = S$ , we denote $C G ( S , n , \mathbf { F } )$ as $C O ( S , n , \mathbf { F } )$ . When $G = K , K ^ { \prime } = - K$ , we denote $C G ( K , n , \mathbf { F } )$ as $C S p ( K , n , \mathbf { F } )$ . When $G = H , H ^ { * } = H$ , we have

$$
\begin{array} { r c l } { C U ( H , n , \mathbf { C } ) } & { = } & { \left\{ A \in G L ( n , \mathbf { C } ) \mid \langle A x , A y \rangle _ { H } = 0 \Longleftrightarrow \langle x , y \rangle _ { H } = 0 \right\} } \\ & { = } & { \left\{ A \in G L ( n , \mathbf { C } ) \mid \exists \mu \in \mathbf { C } , \mu \neq 0 , \mathrm { s u c h t h a t } A ^ { * } H A = \mu H \right\} } \\ & { = } & { \left\{ A \in G L ( n , \mathbf { C } ) \mid \exists \mu \in \mathbf { C } , \mu \neq 0 , A ^ { - 1 } = \mu ^ { - 1 } H ^ { - 1 } A ^ { * } H \right\} . } \end{array}
$$

# 2.1.5 Real Representation of Complex Vector Space

Consider a mapping from $\mathbf { C } ^ { n }$ to $\mathbf { R } ^ { 2 n } \ \rho : \ z \ = \ x + \mathrm { i } y \ \mapsto \ \rho ( z ) \ = \ [ x , y ] ^ { \prime }$ , $z \in$ $\mathbf { C } ^ { n }$ , $x , y \in \mathbf { R } ^ { n }$ . Evidently $\rho : \mathbf { C } ^ { n } \mapsto \mathbf { R } ^ { 2 n }$ is injective, and it satisfies the following properties:

# Property 1.26.

$1 ^ { \circ }$ $\rho ( z + w ) = \rho ( z ) + \rho ( w ) , \quad \forall z , w \in \mathbf { C } ^ { n } .$   
$2 ^ { \circ }$ $\rho ( \alpha z ) = \alpha \rho ( z ) , \quad \forall \alpha \in \mathbf { R }$ .   
$3 ^ { \circ } \quad \rho ( \mathrm { i } z ) = \rho ( - y + \mathrm { i } x ) = { \left[ \begin{array} { l } { - y } \\ { x } \end{array} \right] } = { \left[ \begin{array} { l l } { 0 } & { - I } \\ { I } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = - J \rho ( z ) .$ $4 ^ { \circ }$ $\rho ( ( \alpha + \mathrm { i } \beta ) z ) = ( \alpha I - \beta J ) \rho ( z ) , \quad \alpha + \mathrm { i } \beta \in \mathbf { C } .$   
5◦ $\rho ( 0 ) = 0 \in { \bf R } ^ { 2 n } , 0 \in { \bf C } ^ { n }$ .

For $C = A + \mathrm { i } B \in M ( n , \mathbf { C } )$ , set $R ( C ) = { \left[ \begin{array} { l l } { A } & { - B } \\ { B } & { A } \end{array} \right] } \in M ( 2 n , \mathbf { R } ) . \operatorname { S i m i l a r l y } ,$ $R : C \to R ( C ) , M ( n , \mathbf { C } ) \mapsto M ( 2 n , \mathbf { R } )$ is injective.

Assume $C = A + \mathrm { i } B \in M ( n , \mathbf { C } )$ , $w = C z$ . Then,

$$
w = u + \mathrm { i } v = ( A + \mathrm { i } B ) ( x + \mathrm { i } y ) = ( A x - B y ) + \mathrm { i } ( B x + A y ) ,
$$

i.e.,

$$
{ \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } = { \left[ \begin{array} { l l } { A } & { - B } \\ { B } & { A } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } ,
$$

or

$$
\rho ( w ) = R ( C ) \rho ( z ) = \rho ( C z ) .
$$

Analogously, $R$ satisfies the following properties:

# Property 1.27.

$1 ^ { \circ }$ $R ( O _ { n } ) = O _ { 2 n }$ , $O _ { n } \in M ( n , \mathbf { C } ) .$   
$2 ^ { \circ }$ $R ( I _ { n } ) = I _ { 2 n } , I _ { n } \in M ( n , \mathbf { C } ) .$ .   
$3 ^ { \circ }$ $R ( \alpha C ) = \alpha R ( C ) , \forall \alpha \in \mathbf { R }$ .   
4 $\begin{array} { r } { \mathrm { ~  ~ { ~ \tilde { ~ } { ~ \theta ~ } ~ } ~ } R ( \mathrm { ~ i ~ } C ) = R ( \mathrm { ~ i ~ } A - B ) = \left[ \begin{array} { l l } { - B } & { - A } \\ { \ A } & { - B } \end{array} \right] = - J R ( C ) . } \end{array}$ 5◦ $R ( C _ { 1 } + C _ { 2 } ) = R ( C _ { 1 } ) + R ( C _ { 2 } ) , \forall C _ { 1 } , C _ { 2 } \in M ( n , \mathbf { C } ) .$ $6 ^ { \circ }$ $R ( C _ { 1 } \cdot C _ { 2 } ) = R ( C _ { 1 } ) R ( C _ { 2 } )$ .

The last assertion follows from the theorem below.

# Theorem 1.28.

$$
\operatorname* { d e t } ( A + \mathrm { i } B ) \neq 0 \Longleftrightarrow { \left| \begin{array} { l l } { A } & { - B } \\ { B } & { A } \end{array} \right| } \neq 0 .
$$

Real Representation of Unitary Group:

If $\operatorname* { d e t } ( H ) \neq 0 , H = P + \mathrm { i } Q \in M ( n , \mathbf { C } )$ is Hermitian, iff

$$
P ^ { \prime } = P , \quad Q ^ { \prime } = - Q .
$$

For $w = u + \mathrm { i } v , z = x + \mathrm { i } y \in \mathbf { C } ^ { n }$ , define $\langle w , z \rangle _ { H } = w ^ { * } H z$ .

$$
\begin{array} { l } { w ^ { * } H z \ = \ ( u + \mathrm { i } v ) ^ { * } H ( x + \mathrm { i } y ) } \\ { \ = \ ( u + \mathrm { i } v ) ^ { * } ( P + \mathrm { i } Q ) ( x + \mathrm { i } y ) } \\ { \ = \ ( u ^ { \prime } , v ^ { \prime } ) \left[ \begin{array} { l l } { P } & { - Q } \\ { Q } & { P } \end{array} \right] \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] + \mathrm { i } ( u ^ { \prime } , v ^ { \prime } ) \left[ \begin{array} { l l } { Q } & { P } \\ { - P } & { Q } \end{array} \right] \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] . } \end{array}
$$

The above equation shows that the Hermitian scalar product of $z$ and $w$ , $\langle w , z \rangle _ { H }$ consists of two parts: its real part is a Euclidean scalar product in $\mathbf { R } ^ { 2 n }$ (whose measure is a symmetric matrix $S$ ), denoted by the round bracket and its imaginary part can be taken as a new scalar product in $\mathbf { R } ^ { 2 n }$ (whose measure is an anti-symmetric matrix $K$ ), denoted by the square bracket. Therefore, we have $\langle w , z \rangle _ { H } { = } ( W , Z ) _ { S } + \mathbf { i } [ W , Z ] _ { K } ,$ , where

$$
\begin{array} { l } { { W = \rho ( w ) = \left[ \begin{array} { c } { { u } } \\ { { v } } \end{array} \right] , } } \\ { { Z = \rho ( z ) = \left[ \begin{array} { c c } { { x } } \\ { { y } } \end{array} \right] \in \mathbf { R } ^ { 2 n } , } } \\ { { H = P + \mathrm { i } Q , \quad P ^ { \prime } = P , } } \\ { { Q ^ { \prime } = - Q , S = S ^ { \prime } = \left[ \begin{array} { c c } { { P } } & { { - Q } } \\ { { Q } } & { { P } } \end{array} \right] , } } \\ { { K = - K ^ { \prime } = \left[ \begin{array} { c c } { { Q } } & { { P } } \\ { { - P } } & { { Q } } \end{array} \right] . } } \end{array}
$$

Let $T = R ( C ) = R ( A + \mathrm { i } B )$ . Then,

$$
\langle w , z \rangle _ { H } = \langle C w , C z \rangle _ { H } \Longleftrightarrow ( W , Z ) _ { S } + \mathrm { i } [ W , Z ] _ { K } = ( T W , T Z ) _ { S } + \mathrm { i } [ T W , T Z ] _ { K } .
$$

From this, we can derive the following equivalent conditions:

# Proposition 1.29.

$$
\begin{array} { r l } & { \mathrm { 1 ^ { \circ } } \quad U ( H , n , \mathbf { C } ) \ni C = A + \mathrm { i } B } \\ & { \quad = \{ C \in G L ( n , \mathbf { C } ) \mid \langle C w , C z \rangle _ { H } = \langle w , z \rangle _ { H } , \forall w , z \in \mathbf { C } ^ { n } \} . } \\ & { \mathrm { 2 ^ { \circ } } \quad T = \left[ \begin{array} { l l } { A } & { - B } \\ { B } & { A } \end{array} \right] , \operatorname* { d e t } T \neq 0 , } \end{array}
$$

$$
( W , Z ) _ { S } = ( T W , T Z ) _ { S } , \quad [ W , Z ] _ { K } = [ T W , T Z ] _ { K } .
$$

$3 ^ { \circ }$ $T \in G L ( n , \mathbf { C } )$ , $T \in O ( S , 2 n , \mathbf { R } ) \cap S p ( K , 2 n , \mathbf { R } )$ , where $K = S J$ $4 ^ { \circ }$ $T J = J T$ , $\operatorname* { d e t } T \neq 0$ , and $T ^ { \prime } S T = S$ , $T ^ { \prime } S J T = S J$ .

Hence, $G L ( n , \mathbf { C } )$ is identified with its real image ${ \cal G L } ( n , { \bf R } ) = \{ T \in { \cal G L } ( 2 n , { \bf R } ) \ |$ $T J = J T \}$ , and ${ \cal U } ( H , n , \mathbf { C } )$ is identified with its real image in $G L ( 2 n , \mathbf { R } )$ .

Since $H = P + \mathrm { i } Q$ is non-degenerate, and $S = R ( H ) , K = S J$ are also nondegenerate, we have: if $T J = J T , \quad T ^ { \prime } S T = S$ , then $T ^ { \prime } S J T = T ^ { \prime } S T J = S J$ ; if $T J = J T$ and $T ^ { \prime } S J T = S J$ , then $T ^ { \prime } S T = T ^ { \prime } S J ( - J ) T = - T ^ { \prime } S J T J = - S J ^ { 2 } =$ $S$ ; if $T ^ { \prime } S T = S$ and $T ^ { \prime } S J T = S J$ , then $| T | ^ { 2 } = 1 , T$ invertible, $S T = { T ^ { \prime } } ^ { - 1 } S$ . Hence, if $S J T = { T ^ { \prime } } ^ { - 1 } S J = S T J ,$ then $J T = T J$ .

Therefore, we have

$$
\begin{array} { l } { { { \cal U } ( H , n , { \bf C } ) ~ = ~ G L ( n , { \bf C } ) \cap { \cal O } ( S , 2 n , { \bf R } ) \cap S p ( K , 2 n , { \bf R } ) } } \\ { { { \mathrm { ~ } } } } \\ { { { \mathrm { ~ } } = ~ G L ( n , { \bf C } ) \cap { \cal O } ( S , 2 n , { \bf R } ) } } \\ { { { \mathrm { ~ } } = ~ G L ( n , { \bf C } ) \cap S p ( K , 2 n , { \bf R } ) } } \\ { { { \mathrm { ~ } } = ~ O ( S , 2 n , { \bf R } ) \cap S p ( K , 2 n , { \bf R } ) , } } \end{array}
$$

where $H = P + \mathrm { i } Q , P ^ { \prime } = P ;$ $Q ^ { \prime } = - Q$ , $S = R ( H )$ , $K = S J$ , $| H | \neq 0$ .

In particular, if $H = I$ , $S = I _ { 2 n }$ , $K = J _ { 2 n }$ , then

$$
\begin{array} { l } { { \displaystyle U ( n , { \bf C } ) ~ = ~ G L ( n , { \bf C } ) \cap { \cal O } ( 2 n , { \bf R } ) \cap S p ( 2 n , { \bf R } ) } } \\ { ~ = ~ G L ( n , { \bf C } ) \cap { \cal O } ( 2 n , { \bf R } ) } \\ { ~ = ~ G L ( n , { \bf C } ) \cap S p ( 2 n , { \bf R } ) } \\ { ~ = ~ O ( 2 n , { \bf R } ) \cap S p ( 2 n , { \bf R } ) . } \end{array}
$$

# 2.1.6 Complexification of Real Vector Space and Real Linear Transformation

In a complex vector space $V$ , we not only have the additive operator, but also the scalar multiplication by complex numbers: for $u \in V , \alpha + \mathrm { i } \beta \in \mathbf { C }$ , then $( \alpha + \mathrm { i } \beta ) u \in V$ . This can be realized by a scalar multiplication by real numbers $u \in V .$ , $\alpha \in \mathbf { R } \Leftrightarrow \alpha u \in V$ plus a single scalar multiplication by an imaginary unit i, i: $u \in V \Leftrightarrow \mathrm { i } u \in V$ , which can be seen as an operator

$$
l : V \longrightarrow V , \quad u \longrightarrow \mathrm { i } u = l ( u ) .
$$

$l$ is a real linear transformation of $V$ , i.e.,

$$
l ( \alpha u + \beta v ) = \alpha l ( u ) + \beta l ( v ) , \quad u , v \in V , \quad \alpha , \beta \in { \bf R } .
$$

Moreover, a complex linear transformation $T$ of $V$ satisfies:

the additive property: $T ( u + v ) = T ( u ) + T ( v )$ , the multiplication property: $T ( ( \alpha + \mathbf { i } \beta ) u ) = ( \alpha + \mathbf { i } \beta ) T ( u )$ .

The latter is simply the commutativity of complex linear transformation and complex scalar multiplication, which can be realized by

$$
T ( \mathbf { i } u ) = \mathbf { i } T ( u ) \sim T l = l T .
$$

Let

$$
{ \begin{array} { r l } { { \mathcal { L } } ( V , \mathbf { R } ) } & { = \{ T \mid T ( u + v ) = T ( u ) + T ( v ) , T ( \alpha u ) = \alpha T ( u ) , \forall u , v \in V , \alpha \in \mathbf { R } } \\ { { \mathcal { L } } ( V , \mathbf { C } ) } & { = \{ T \mid T ( u + v ) = T ( u ) + T ( v ) , T ( ( \alpha + \mathbf { i } \beta ) u ) } \\ & { = ( \alpha + \mathbf { i } \beta ) T ( u ) , \forall u , v \in V , \alpha , \beta \in \mathbf { R } \} . } \end{array} }
$$

Evidently, $T \in { \mathcal { L } } ( V , \mathbf { C } ) \Leftrightarrow$ iff $T \in { \mathcal { L } } ( V , \mathbf { R } )$ and $T ( \mathrm { i } u ) = \mathrm { i } T ( u )$ . Thus, the operator $l$ satisfies

$$
l \in \mathcal { L } ( V , { \bf R } ) , \quad \mathrm { i } ^ { 2 } = - 1 ,
$$

and

$$
T \in { \mathcal { L } } ( V , \mathbf { C } ) \quad { \mathrm { i f f } } \quad T \in { \mathcal { L } } ( V , \mathbf { R } ) , \quad { \mathrm { a n d } } \quad T l = l T .
$$

These observations form the basis for the following definitions and the method of complexification of real vector space.

Definition 1.30. A real vector space $V = V ( \mathbf { R } )$ is complexifiable if there exists an operator $l$ in $\mathcal { L } ( V , \mathbf { R } )$ such that $l ^ { 2 } = - I$ .

We can easily see that $V$ is complexifiable iff $\mathrm { d i m } V ( \mathbf { R } ) = 2 n .$ . This is because the operator equation $l ^ { 2 } = - I$ in ${ \mathcal { L } } ( V , \mathbf { R } )$ corresponds to the matrix equation $X ^ { 2 } = - I$ in $M ( m , { \mathbf R } ) , m \mathrel { \mathop = } \mathrm { d i m } _ { R } ( V )$ , which has no real solution for $m = 2 n + 1$ . (Since from $X ^ { 2 } = - I$ it follows that all eigenvalues of $X$ are $\pm \mathrm i$ , while for $m = 2 n + 1$ , $X \in M ( m , \mathbf { R } )$ has at least one real eigenvalue.) When $m = 2 n$ , there is a special solution

$$
X = \pm J , \quad ( \pm J ) ^ { 2 } = - I .
$$

If we introduce an isomorphism $J$ on $\mathbf { R } ^ { 2 n }$ , which satisfies $J ^ { 2 } \ = \ - I$ , then we say that $\mathbf { R } ^ { 2 n }$ is equipped with the complex structure. Hence, we can define operation $( a + \mathrm { i } b ) u = a u + b J u$ , and $\mathbf { R } ^ { 2 n }$ becomes the complex $n$ -dimensional space. $\mathbf { C } ^ { n }$ is called $\mathbf { R } ^ { 2 n }$ complexifiable.

# 2.1.7 Lie Algebra for $G L ( n , \mathbf { F } )$

# 1. Lie algebra

Definition 1.31. For $B _ { 1 } , B _ { 2 } \in M ( n , \mathbf { F } )$ , we define a commutator of $B _ { 1 } , B _ { 2 }$ as follows:

$$
\{ B _ { 1 } , B _ { 2 } \} = B _ { 1 } B _ { 2 } - B _ { 2 } B _ { 1 } ,
$$

which satisfies the following properties:

$1 ^ { \circ }$ $\{ B _ { 1 } , B _ { 2 } \} = - \{ B _ { 2 } , B _ { 1 } \}$ . $2 ^ { \circ }$ $\{ B _ { 1 } , \{ B _ { 2 } , B _ { 3 } \} \} + \{ B _ { 2 } , \{ B _ { 3 } , B _ { 1 } \} \} + \{ B _ { 3 } , \{ B _ { 1 } , B _ { 2 } \} \} = 0 .$

The equation $2 ^ { \circ }$ is called Jacobi identity.

Definition 1.32. A Lie algebra is a vector space equipped with a binary operation $L \times L \to L$ , which satisfies the Jacobi identity.

Hence, $M ( n , \mathbf { F } )$ , equipped with the above commutator, becomes a Lie algebra, denoted as $g l ( n , \mathbf { F } )$ . Since $g l ( n , \mathbf { F } )$ is the tangent vector space to $G L ( n , \mathbf { F } )$ at $I$ , ${ g l } ( n , { \bf F } )$ is called Lie algebra of the Lie group $G L ( n , \mathbf { F } )$ .

Definition 1.33. The Lie algebra of the Lie group $S L ( n , \mathbf { F } )$ is defined as follows:

$$
s l ( n , { \bf F } ) = \{ B \in g l ( n , { \bf F } ) \mid \mathrm { t r } B = 0 \} .
$$

Remark 1.34. If $\mathrm { t r } { \cal B } _ { 1 } = \mathrm { t r } { \cal B } _ { 2 } = 0$ , then $\mathrm { t r } \{ B _ { 1 } , B _ { 2 } \} = \mathrm { t r } ( B _ { 1 } B _ { 2 } - B _ { 2 } B _ { 1 } ) = 0$ . Therefore, $s l ( n , \mathbf { F } )$ is closed under $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ . As the matter of fact, for any $A , B , \operatorname { t r } \{ A , B \}$ is always equal to 0.

Definition 1.35. The Lie algebra of the Lie group $G ( G , n , \mathbf { F } )$ is defined as follows:

$$
g ( G , n , { \bf F } ) = \{ B \in g l ( n , { \bf F } ) | B ^ { \prime } G + G B = 0 \} .
$$

Remark 1.36. $g ( G , n , \mathbf { F } )$ is closed under $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ , i.e.,

$$
\{ B _ { 1 } , B _ { 2 } \} \in g ( G , n , \mathbf { F } ) , \quad \forall B _ { 1 } , B _ { 2 } \in g ( G , n , \mathbf { F } ) .
$$

If $B _ { i } ^ { \prime } G = - G B _ { i } \left( i = 1 , 2 \right)$ , then

$$
\begin{array} { r c l } { { \{ B _ { 1 } , B _ { 2 } \} ^ { \prime } G } } & { { = } } & { { ( B _ { 1 } B _ { 2 } - B _ { 2 } B _ { 1 } ) ^ { \prime } G } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( B _ { 2 } ^ { \prime } B _ { 1 } ^ { \prime } - B _ { 1 } ^ { \prime } B _ { 2 } ^ { \prime } ) G } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { B _ { 2 } ^ { \prime } B _ { 1 } ^ { \prime } G - B _ { 1 } ^ { \prime } B _ { 2 } ^ { \prime } G } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { B _ { 2 } ^ { \prime } ( - G B _ { 1 } ) - B _ { 1 } ^ { \prime } ( - G B _ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { G ( B _ { 2 } B _ { 1 } - B _ { 1 } B _ { 2 } ) } } \\ { { } } & { { } } & { { = } } & { { - G \{ B _ { 1 } , B _ { 2 } \} . } } \end{array}
$$

# 2. Exponential matrix transform

Definition 1.37. For $B \in M ( n , \mathbf { C } )$ , define

$$
\exp ( B ) = \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { k ! } } B ^ { k } = \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 0 } ^ { n } { \frac { 1 } { k ! } } B ^ { k } .
$$

Take the Chebyshev matrix norm

$$
| | B | | = \operatorname* { m a x } _ { i } \sum _ { j = 1 } ^ { m } | b _ { i j } | .
$$

Then, $| b _ { i j } | \leq | | B | | , | | B ^ { k } | | \leq | | B | | ^ { k }$ . Hence, the $n ^ { 2 }$ series $\left( \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { k ! } } B ^ { k } \right) _ { i , }$ are always j uniformly convergent, and convergent uniformly if $| | B | | \leq \beta , \forall \beta > 0$ .

Proposition 1.38. We have the following results:

$1 ^ { \circ }$ $\exp { ( T ^ { - 1 } B T ) } = T ^ { - 1 } \exp { ( B ) T }$ , $\forall T \in G L ( n , \mathbf { C } )$

$2 ^ { \circ }$ If $B$ has eigenvalues $\lambda _ { 1 } , \cdots , \lambda _ { n }$ (with multiplicities), then exp $B$ has the eigenvalues exp $\lambda _ { 1 } , \cdots , \exp { \lambda _ { n } }$ .

$3 ^ { \circ }$ $\begin{array} { l } { { \displaystyle \operatorname * { d e t } \left( \exp B \right) = \exp \left( \operatorname { t r } B \right) , \ \operatorname { t r } B = \sum _ { i = 1 } ^ { n } b _ { i i } } . } \\ { { \displaystyle \operatorname * { e x p } B \in G L ( n . \mathbf { C } ) , \ \forall B \in \left. M ( n . \mathbf { C } ) \right. } . } \end{array}$ $4 ^ { \circ }$ exp $5 ^ { \circ }$ $I f B _ { 1 } , B _ { 2 } \in M ( n , \mathbf { C } )$ , $B _ { 1 } B _ { 2 } = B _ { 2 } B _ { 1 }$ , then

$$
\exp { ( B _ { 1 } + B _ { 2 } ) } = \exp { B _ { 1 } } \cdot \exp { B _ { 2 } } = \exp { B _ { 2 } } \cdot \exp { B _ { 1 } } .
$$

$6 ^ { \circ }$ exp $B ^ { \prime } = ( \exp B ) ^ { \prime }$ , ${ \overline { { \exp } } } B = \exp { \overline { { B } } }$ .

$7 ^ { \circ }$ $\forall t \in \mathbf { R }$ , $i f \exp \left( t B \right) \in G L ( n , \mathbf { C } )$ , then

$$
\begin{array} { r l } & { \exp \left( ( t _ { 1 } + t _ { 2 } ) B \right) = \exp \left( t _ { 1 } B \right) \cdot \exp \left( t _ { 2 } B \right) , } \\ & { \exp \left( 0 \cdot B \right) = I , } \\ & { \exp \left( - t B \right) = ( \exp \left( t B \right) ) ^ { - 1 } . } \end{array}
$$

Therefore, the mapping $t \in \mathbf { R } \mapsto \exp \left( t B \right) \in G L ( n , \mathbf { C } )$ for a given $B$ is a group homomorphism of the additive group $R$ into the multiplicative group $G L ( n , \mathbf { C } )$ .

Theorem 1.39. There exists a neighborhood $W$ of $O _ { n }$ in $M ( n , \mathbf { C } )$ such that the exponential mapping $\exp : M ( n , \mathbf { C } ) \mapsto G L ( n , \mathbf { C } )$ is a diffeomorphism on $W$ .

Proof. The series $\sum _ { k = 0 } ^ { \infty } { \frac { B ^ { k } } { k ! } }$ is uniformly convergent in $| | B | | \leq \rho \left( \rho > 0 \right)$ . Therefore, $F _ { i j } = ( \exp B ) _ { i j }$ are the entire analytic functions of the complex variables $b _ { k l }$ ( $k , l =$ $1 , \cdots , n )$ ,

$$
F _ { i j } ( b _ { k l } ) = \delta _ { i j } + b _ { i j } + \cdot \cdot \cdot + ( { \mathrm { t e r m s ~ o f ~ d e g r e e } } ) \geq 2 .
$$

Therefore, the Jacobian matrix is

$$
\frac { \partial ( \exp B ) _ { i j } } { \partial \bar { b } _ { k l } } = \frac { \partial F _ { i j } ( b _ { k l } ) } { \partial b _ { k l } } = \delta _ { i j } ^ { k l } ,
$$

where $\delta _ { i j } ^ { k l } = { \left\{ \begin{array} { l l } { 1 , } & { k = i , \quad l = j , } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }$

Since det $( \dot { \delta } _ { i j } ^ { k l } ) = 1 \neq 0$ , by implicit function theorem, there exists a neighborhood $W \subset \{ | | B | | < { \overset { } { \rho } } \}$ , such that $B \mapsto \exp B$ is a diffeomorphism on $W$ . -

Remark 1.40. The inverse function to $B \mapsto \exp B = A$ is

$$
A \longmapsto \log A = \log \left( I + ( A - I ) \right) = \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } } { k } } ( A - I ) ^ { k } ,
$$

which is uniformly convergent for $| | A - I | | \leq \rho < 1$ .

Proposition 1.41. The function $A ( t ) = \exp \left( t B \right)$ , $\forall t \in \mathbf { R }$ satisfies the following properties:

$$
\begin{array} { r l } & { A ( 0 ) = I , } \\ & { A ( t _ { 1 } + t _ { 2 } ) = A ( t _ { 1 } ) A ( t _ { 2 } ) = A ( t _ { 2 } ) A ( t _ { 1 } ) , } \\ & { A ( - t ) = ( A ( t ) ) ^ { - 1 } , } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } A ( t ) = B A ( t ) , \quad \frac { \mathrm { d } } { \mathrm { d } t } A ( t ) | _ { t = 0 } = B . } \end{array}
$$

Proposition 1.42. For $A _ { 1 }$ , $A _ { 2 } \in G L ( n , \mathbf { C } )$ , its commutator is defined by

$$
\{ A _ { 1 } , A _ { 2 } \} _ { G } = A _ { 1 } A _ { 2 } A _ { 1 } ^ { - 1 } A _ { 2 } ^ { - 1 } \quad ( c o m m u t a t o r i n L i e g r o u p ) .
$$

Then for $A _ { i } ( t ) = \exp { t B _ { i } ( i = 1 , 2 ) } , \forall t \in { \bf R } ,$ we have

$$
\begin{array} { r l } & { \{ A _ { 1 } ( t ) , A _ { 2 } ( t ) \} _ { G } = I + t ^ { 2 } \{ B _ { 1 } , B _ { 2 } \} _ { g } + o ( t ^ { 4 } ) , } \\ & { \{ A _ { 1 } ( t ) , A _ { 2 } ( t ) \} _ { G } | _ { t = 0 } = I _ { n } , } \\ & { \frac { \mathrm { d } } { \mathrm { d } t } \{ A _ { 1 } ( t ) , A _ { 2 } ( t ) \} _ { G } | _ { t = 0 } = 0 , } \\ & { \frac { 1 } { 2 } \frac { \mathrm { d } ^ { 2 } } { \mathrm { d } t ^ { 2 } } \{ A _ { 1 } ( t ) , A _ { 2 } ( t ) \} _ { G } | _ { t = 0 } = \{ B _ { 1 } , B _ { 2 } \} _ { g } , } \end{array}
$$

where $\{ B _ { 1 } , B _ { 2 } \} _ { g } = B _ { 1 } B _ { 2 } - B _ { 2 } B _ { 1 }$ is the commutator in Lie algebra.

Proposition 1.43. If $B \in g ( G , n , \mathbf { F } )$ and $f ( \lambda ) = \sum _ { k = 0 } ^ { n } \alpha _ { k } \lambda ^ { k }$ , $\alpha _ { k } \in \mathbf { F }$ , then $( B ^ { k } ) ^ { \prime } G =$ $G ( - B ) ^ { k } , ( f ( B ) ) ^ { \prime } G = G f ( - B ) .$

Theorem 1.44. $A ( t ) = \exp { ( t B ) } \in G ( G , n , \mathbf { F } )$ , $\forall t \in \mathbf { R }$ iff $B \in g ( G , n , \mathbf { F } )$ .

Proof. Let $C ( t ) = A ^ { \prime } ( t ) G A ( t )$ , then $C ( 0 ) = G$ ,

$$
{ \begin{array} { l } { { \frac { \mathrm { d } } { \mathrm { d } t } } C ( t ) \ = \ { \frac { \mathrm { d } \ A ^ { \prime } ( t ) } { \mathrm { d } t } } G A ( t ) + A ^ { \prime } ( t ) G { \frac { \mathrm { d } A ( t ) } { \mathrm { d } t } } } \\ { \ = \ B A ^ { \prime } ( t ) G A ( t ) + A ^ { \prime } ( t ) G B A ( t ) } \\ { \ = \ A ^ { \prime } ( t ) ( B ^ { \prime } G + G B ) A ( t ) . } \end{array} }
$$

Thus, $A ( t ) \in G ( G , n , \mathbf { F } ) , \forall t \in \mathbf { R }$ iff $C ( t ) \equiv G$ , i.e., ${ \frac { \mathrm { d } } { \mathrm { d } t } } C ( t ) = 0 .$ . Then, in order to prove the theorem, we need only to show that the latter condition is equivalent to $B \in g ( G , n , \mathbf { F } )$ , i.e., $B ^ { \prime } G + G B = 0$ .

If ${ \frac { \mathrm { d } } { \mathrm { d } t } } C ( t ) = 0$ , then $\begin{array} { r } { \left. \frac { \mathrm { d } } { \mathrm { d } t } C ( t ) \right| _ { t = 0 } = I ^ { \prime } ( B ^ { \prime } G + G B ) I = B ^ { \prime } G + G B = 0 . } \end{array}$ , and so $B \in g ( G , n , \mathbf { F } )$ . Conversely, if $B ^ { \prime } G + G B = 0$ , by (1.1),

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } C ( t ) = 0 ,
$$

then $C ( t ) = C ( 0 ) = G$ , i.e., $A ^ { \prime } ( t ) G A ( t ) = G$ , $\forall t \in \mathbf { R }$ .

# 3. Lie algebra of conformally invariant groups $C G ( G , n , \mathbf { F } )$

Definition 1.45. Define

$$
c g ( G , n , \mathbf { F } ) = \big \{ B \in g l ( n , \mathbf { F } ) \mid B ^ { \prime } G + G B = \beta G , \mathrm { f o r ~ s o m e ~ } \beta \in \mathbf { F } \big \} .
$$

Since $B _ { 1 } , B _ { 2 } \in c g ( G , n , \mathbf { F } )$ , then

$$
\begin{array} { r c l } { { \{ B _ { 1 } , B _ { 2 } \} ^ { \prime } G ~ = ~ ( B _ { 1 } B _ { 2 } - B _ { 2 } B _ { 1 } ) ^ { \prime } G = B _ { 2 } ^ { \prime } B _ { 1 } ^ { \prime } G - B _ { 1 } ^ { \prime } B _ { 2 } ^ { \prime } G } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ B _ { 2 } ^ { \prime } ( \beta _ { 1 } G - G B _ { 1 } ) - B _ { 1 } ^ { \prime } ( \beta _ { 2 } G - G B _ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ \beta _ { 1 } \beta _ { 2 } G - \beta _ { 1 } G B _ { 2 } - ( \beta _ { 2 } G - G B _ { 2 } ) B _ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - \beta _ { 1 } \beta _ { 2 } G + \beta _ { 2 } G B _ { 1 } + ( \beta _ { 1 } G - G B _ { 1 } ) B _ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ G ( B _ { 2 } B _ { 1 } - B _ { 1 } B _ { 2 } ) = - G \{ B _ { 1 } , B _ { 2 } \} . } } \end{array}
$$

$\{ B _ { 1 } , B _ { 2 } \} \in c g ( G , n , \mathbf { F } )$ . This shows that $c g ( G , n , { \bf F } )$ is closed under $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ . Therefore, $c g ( G , n , { \bf F } )$ is a subalgebra of $g l ( n , \mathbf { F } )$ equipped with the induced binary operation $\left\{ \begin{array} { r l } \end{array} \right. , \left. \begin{array} { r l } \end{array} \right\}$ , called as the Lie algebra of the conformally invariant group $C G ( G , n , \mathbf { F } )$ .

Theorem 1.46. Let $A ( t ) \mathbf { = } \exp ( t B ) ,$ , then $A ( t ) \in C G ( G , n , \mathbf { F } )$ iff $B \in c g ( G , n , \mathbf { F } )$

# 2.2 Canonical Reductions of Bilinear Forms

In Section 2.1, we have seen that for a given bilinear form $\varphi$ on $\mathbf { F } ^ { n }$ , there is a matrix $G$ in $M ( n , \mathbf { F } )$ such that under natural base, $\varphi$ can be represented by $G$ :

$$
\varphi ( x , y ) = x ^ { \prime } G y , \quad G _ { i j } = \varphi ( e _ { i } , e _ { j } ) .
$$

The representative matrix $G$ will change as the base changes. In this section, we want to make sure how the matrix $G$ changes.

Let $\mathbf { F } _ { } ^ { n } = \{ e _ { 1 } , \cdots , e _ { n } \} = \{ f _ { 1 } , \cdots , f _ { n } \}$ , where $e _ { 1 } , \cdots , e _ { n }$ is the standard base and $f _ { 1 } , \cdots , f _ { n }$ is a new base. Then,

$$
f _ { i } = \sum _ { j = 1 } ^ { n } t _ { j i } e _ { j } , \qquad T = [ t _ { i j } ] \in G L ( n , \mathbf { F } ) ,
$$

$$
x = \sum _ { i = 1 } ^ { n } x _ { i } e _ { i } = \sum _ { i = 1 } ^ { n } u _ { i } { \bar { f } } _ { i } , \quad x = { \left[ \begin{array} { l } { x _ { 1 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] } = T u = T { \left[ \begin{array} { l } { u _ { 1 } } \\ { \vdots } \\ { u _ { n } } \end{array} \right] } ,
$$

$$
y = \sum _ { i = 1 } ^ { n } y _ { i } e _ { i } = \sum _ { i = 1 } ^ { n } v _ { i } { \bar { f } } _ { i } , \quad y = { \left[ \begin{array} { l } { y _ { 1 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } = T v = T { \left[ \begin{array} { l } { v _ { 1 } } \\ { \vdots } \\ { v _ { n } } \end{array} \right] } .
$$

Assume that under the new base ${ \bar { f } } _ { 1 } , \cdots , { \bar { f } } _ { n }$ , the representative matrix of $\varphi$ is $\overline { { G } }$ . Then,

$$
\begin{array} { l } { { \overline { { { G } } } _ { i j } ~ = ~ \varphi ( \bar { f } _ { i } , \bar { f } _ { j } ) = \varphi \bigg ( \displaystyle \sum _ { k = 1 } ^ { n } t _ { k i } e _ { k } , \displaystyle \sum _ { l = 1 } ^ { n } t _ { l j } e _ { l } \bigg ) } } \\ { { ~ = ~ \displaystyle \sum _ { k , l = 1 } ^ { n } t _ { k i } \varphi ( e _ { k } , e _ { l } ) t _ { l j } = ( T ^ { \prime } G T ) _ { i j } , } } \end{array}
$$

i.e.,

$$
{ \overline { { G } } } = T ^ { \prime } G T ,
$$

$$
\begin{array} { l } { \displaystyle \varphi ( x , y ) = \varphi \Big ( \sum _ { i = 1 } ^ { n } x _ { i } e _ { i } , \sum _ { j = 1 } ^ { n } y _ { j } e _ { j } \Big ) = \sum _ { i , j = 1 } ^ { n } x _ { i } \varphi ( e _ { i } , e _ { j } ) y _ { j } = \sum _ { i , j = 1 } ^ { n } x _ { i } G _ { i j } y _ { j } = x ^ { \prime } G y } \\ { = \varphi \Big ( \sum _ { i = 1 } ^ { n } u _ { i } \bar { f } _ { i } , \sum _ { j = 1 } ^ { n } v _ { j } \bar { f } _ { j } \Big ) = \sum _ { i , j = 1 } ^ { n } u _ { i } \varphi ( \bar { f } _ { i } , \bar { f } _ { j } ) v _ { j } } \\ { = \sum _ { i , j = 1 } ^ { n } u _ { i } \overline { { G } } _ { i j } v _ { j } = u ^ { \prime } \overline { { G } } v . } \end{array}
$$

# 2.2.1 Congruent Reductions

Definition 2.1. Let $G _ { 1 }$ and $G _ { 2 } \in M ( n , \mathbf { F } )$ . $G _ { 1 }$ is congruent to $G _ { 2 }$ , if there exists a non-singular matrix $T \in G L ( n , \mathbf { F } )$ , such that $T ^ { \prime } G _ { 1 } T = G _ { 2 }$ , denoted by $G _ { 1 } \sim G _ { 2 }$ .

Thus, the representative matrices of a bilinear form $\varphi$ on $\mathbf { R } ^ { n }$ under different bases are congruent to one another.

If $G _ { 1 }$ is congruent to $G _ { 2 }$ , then the equality $G _ { 1 } ^ { \prime } = \varepsilon G _ { 1 }$ implies the equality $G _ { 2 } ^ { \prime } =$ $\varepsilon G _ { 2 }$ with the same parity $\varepsilon$ and rank $G _ { 1 } = \mathrm { r a n k } G _ { 2 }$ .

Let $\phi$ be a conjugate bilinear form on $\mathbf { C } ^ { n }$ . $G$ is the representative matrix of $\phi$ under the standard base, i.e.,

$$
\phi ( x , y ) = x ^ { * } G y , \quad y = { \left[ \begin{array} { l } { y _ { 1 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } , \quad x = { \left[ \begin{array} { l } { x _ { 1 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] } \in \mathbf { C } ^ { n } .
$$

If ${ \bar { f } } _ { 1 } , \cdots , { \bar { f } } _ { n }$ is another base on $\mathbf { C } ^ { n }$ and $\bar { f } _ { j } = \sum _ { i = 1 } ^ { n } t _ { i j } e _ { i } , T = [ t _ { i j } ] \in G L ( n , \mathbf { C } ) ,$ then similarly we can get

$$
{ \overline { { G } } } = T ^ { * } G T ,
$$

where $\overline { G }$ is the representative matrix of $\phi$ under the base ${ \bar { f } } _ { 1 } , \cdots , { \bar { f } } _ { n }$ .

Definition 2.2. Let $G _ { 1 }$ and $G _ { 2 } \in M ( n , \mathbf { C } )$ . $G _ { 1 }$ is congruent to $G _ { 2 }$ if there exists a matrix $T \in G L ( n , \mathbf { C } )$ , such that $T ^ { * } G _ { 1 } T = G _ { 2 }$ , denoted by $G _ { 1 } \stackrel { c } { \sim } G _ { 2 }$ .

If $G _ { 1 } \stackrel { c } { \sim } G _ { 2 }$ , then rank $G _ { 1 } = \mathrm { r a n k } G _ { 2 }$ and the equality $G _ { 1 } ^ { * } = \varepsilon G _ { 1 }$ implies the equality $G _ { 2 } ^ { * } = \varepsilon G _ { 2 }$ with the same factor $\varepsilon$ .

Remark 2.3. $G$ is a conformal Hermitian matrix, i.e., $\overline { { G } } ^ { \prime } = \varepsilon G$ with $\overline { { G } } , \varepsilon \in \mathbf { C }$ , and $| \varepsilon | = 1$ , if and only if $\varepsilon = e ^ { \mathrm { i } \theta }$ and $G ^ { * } = e ^ { \mathbf { i } \theta } G$ , if and only if $e ^ { \frac { \mathbf { i } _ { \theta } } { 2 } } G$ is a Hermitian matrix.

Definition 2.4. Let $\varphi ( x , y ) = \varphi _ { G } ( x , y ) = x ^ { \prime } G y$ be a bilinear form induced by $G$ . For a subspace $U \subset \mathbf { R } ^ { n } / \mathbf { C } ^ { n }$ , the subspace $U ^ { \varphi } \subset \mathbf { R } ^ { n } / \mathbf { C } ^ { n }$ defined by

$$
U ^ { \varphi } = \{ x \in \mathbf { R } ^ { n } / \mathbf { C } ^ { n } \mid \varphi ( x , y ) = x ^ { \prime } G y = 0 , \forall y \in U \}
$$

is called the $G$ -orthogonal complement of $U$ .

# 2.2.2 Congruence Canonical Forms of Conformally Symmetric and Hermitian Matrices

We list congruence canonical forms of conformally symmetric and Hermitian matrices in Table 2.1 as a comparison.

$$
\mathbf { F } = \mathbf { R } / \mathbf { C } .
$$

# 1. Alternative canonical forms

Let $T = \frac { 1 } { \sqrt { 2 } } \left[ \begin{array} { c c } { I } & { I } \\ { I } & { - I } \end{array} \right] , \ \mathrm { t h e n } \ T ^ { \prime } \left[ \begin{array} { c c } { O } & { I } \\ { I } & { O } \end{array} \right] T = \left[ \begin{array} { c c } { I } & { O } \\ { O } & { - I } \end{array} \right] .$ where $\mathbf { F } ^ { n } = V +$ $U = \{ x \in \mathbf { F } ^ { n } \mid \varphi ( x , y ) = 0$ , ∀ y ∈ F } = (F ) , onical symplectic quadrati $\dim V \ : = \ : r$ $\dim U \ =$ $n - r , \varphi$ $J$ $\left[ \begin{array} { c c } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right]$

$$
\begin{array} { r } { \mathrm { L e t } T = [ t _ { i j } ] , t _ { i j } = \left\{ \begin{array} { l l } { \delta _ { k , j } , } & { i = 2 k - 1 , } \\ { \delta _ { k + n , j } , } & { i = 2 k , } \end{array} \right. \ } & { i , j = 1 , \cdots , 2 n . \ \mathrm { T h e n } , } \end{array}
$$

$$
T ^ { \prime } \left[ \begin{array} { c c c c c } { { } } & { { 0 } } & { { 1 } } & { { } } & { { } } \\ { { \pm 1 } } & { { 0 } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { 0 } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { \pm 1 } } & { { 0 } } \end{array} \right] T = \left[ \begin{array} { c c } { { } } & { { { \cal O } } } & { { { \cal I } _ { n } } } \\ { { \pm { \cal I } _ { n } } } & { { { \cal O } } } \end{array} \right] _ { 2 n \times 2 n } .
$$

Thus, the canonical forms listed in Table 2.1 have the following alternative forms:

Table 2.1. Canonical form of conformal matrix and Hermitian matrices   

<table><tr><td rowspan=1 colspan=1>Matrix</td><td rowspan=1 colspan=2>Canonical form</td></tr><tr><td rowspan=1 colspan=1>G&#x27;=G,in Cor R,JJs-block      JOn-r]2s=r</td><td rowspan=1 colspan=1>u,v∈R,s.t.(u,v)≠0.Leta1 =u,a2=  Uu,）=（a1,a1）=(a2,a2)=0,(a1,a2)=-φ(a2,a1)=1</td><td rowspan=1 colspan=1>{a1,a2}n {a1,a2}={0}，G~0G1</td></tr><tr><td rowspan=1 colspan=1>G&#x27;= G,inC,IrOn-r</td><td rowspan=1 colspan=1>u ∈CT,s.t.(u,u)≠0.uLet a1 =(u,u)(a1,a1)=1</td><td rowspan=1 colspan=1>{a1}n{a1}={0},{a1}={a2,..·,ar},q[a]</td></tr><tr><td rowspan=1 colspan=1>G&#x27;=G,inR,Ip-IqOn-rp+q=r</td><td rowspan=1 colspan=1>u∈R,s.t.(u,u)≠0.uLet a1=√l(u,u)l(a1,a1)=±1</td><td rowspan=1 colspan=1>{a1}n{a1}={0},{a1}= {a2,.,ar},</td></tr><tr><td rowspan=1 colspan=1>G*=G,G*=eGIp-IqOn-r-i0e2Ip-ie-e2IqOn-rp+q=r</td><td rowspan=1 colspan=1>u ∈C,s.t.(u,u)≠0.uLeta1=l(u,u)l(a1,a1)= signφ(u,u)=±1</td><td rowspan=1 colspan=1>{a1}n{a1}={0},{a1}={a2,...,ar},[±10]G~0G</td></tr></table>

$$
\left[ \begin{array} { l l l l } { 0 } & { I _ { s } } & & \\ { I _ { s } } & { 0 } & & \\ & & { \sigma I _ { d } } & \\ & & & { O _ { n - r } } \end{array} \right] \sim G ^ { \prime } = G , \qquad \mathrm { i n ~ } \mathbf { R } \quad \mathrm { o r } \quad ( G ^ { * } = G , \mathrm { i n } { \bf C } ) ,
$$

$$
\left[ \begin{array} { c c c c } { { 0 } } & { { I _ { s } } } & { { } } & { { } } \\ { { e ^ { - \mathrm { i } \theta } I _ { s } } } & { { 0 } } & { { } } & { { } } \\ { { } } & { { } } & { { \sigma e ^ { - { \frac { \mathrm { i } \theta } { 2 } } } I _ { d } } } & { { } } \\ { { } } & { { } } & { { } } & { { O _ { n - r } } } \end{array} \right] G ^ { * } = e ^ { \mathrm { i } \theta } G , \mathrm { i n } { \bf C } ,
$$

$$
\begin{array} { l } { { \mathrm { r e } ~ s = \operatorname* { m i n } ( p , q ) , ~ d = | p - q | , ~ \sigma = \mathrm { s i g n } ( p - q ) , ~ p + q = r = 2 s + d , ~ p - q = \frac { 1 } { 2 } ( 1 - q ) , } } \\ { { \mathrm { } ~ p = \frac { 1 } { 2 } ( r + \sigma d ) = s + \frac { 1 } { 2 } ( 1 + \sigma ) d , ~ q = \frac { 1 } { 2 } ( r - \sigma d ) = s + \frac { 1 } { 2 } ( 1 - \sigma ) d . } } \end{array}
$$

# 2. Invariants under congruences

Theorem 2.5. Let $G$ be a conformally symmetric matrix in $\mathbf { F } ^ { n } ( = \mathbf { R } ^ { n }$ or $\mathbf { C } ^ { n }$ ), i.e., $G ^ { \prime } = \varepsilon G$ . Then, the quantities $\varepsilon ( G ) , r ( G )$ and $s ( G )$ are the invariants under congruences. Moreover, if $\varepsilon = - 1$ , then $r = 2 s$ , if $\varepsilon = 1$ , then $p ( G ) , q ( G ) , d ( G )$ and $\sigma ( G )$ are invariants under congruences.

If $G$ is conformal Hermitian, i.e., $G ^ { * } = \varepsilon G$ with $\varepsilon = e ^ { i \theta }$ , then the quantities $\varepsilon ( G ) , r ( G ) , s ( G ) , p ( G ) , q ( G )$ and $\sigma ( G )$ are invariants under congruences.

Theorem 2.6 (Sylvester’s law of inertia). Let $\varphi ( x )$ be a quadratic form in $\mathbf { R } ^ { n }$ and $x = T y$ , $\operatorname* { d e t } ( T ) \neq 0 .$ . If

$$
{ \begin{array} { l } { \varphi ( x ) \ = \ x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + \cdot \cdot \cdot + x _ { p } ^ { 2 } - x _ { p + 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n } ^ { 2 } } \\ { \ = \ y _ { 1 } ^ { 2 } ( x ) + y _ { 2 } ^ { 2 } ( x ) + \cdot \cdot \cdot + y _ { q } ^ { 2 } ( x ) - y _ { q + 1 } ^ { 2 } ( x ) - \cdot \cdot \cdot - y _ { n } ^ { 2 } ( x ) , } \end{array} }
$$

then $p = q$

Similarly, let $\phi ( x )$ be a quadratic form in $\mathbf { C } ^ { n }$ and $x = T y , \operatorname* { d e t } T \neq 0 .$ If

$$
\begin{array} { l } { { \phi ( x ) ~ = ~ | x _ { 1 } | ^ { 2 } + | x _ { 2 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { p } | ^ { 2 } - | x _ { p + 1 } | ^ { 2 } - \cdot \cdot \cdot - | x _ { n } | ^ { 2 } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = ~ | y _ { 1 } | ^ { 2 } + | y _ { 2 } | ^ { 2 } + \cdot \cdot \cdot + | y _ { q } | ^ { 2 } - | y _ { q + 1 } | ^ { 2 } - \cdot \cdot \cdot - | y _ { n } | ^ { 2 } , } } \end{array}
$$

then $p = q$

Proof. If $p \ > \ q$ , then $p + ( n - q ) \ > \ n$ . Thus, the equations $x _ { 1 } = 0 , \cdots , x _ { p } =$ 0, $y _ { q + 1 } ( x ) = 0$ , · · · , $y _ { n } ( x ) = 0$ has a non-zero solution $\xi \neq 0$ . By (2.1),

$y _ { 1 } ^ { 2 } ( \xi ) + \cdot \cdot \cdot + y _ { q } ^ { 2 } ( \xi ) + \xi _ { p + 1 } ^ { 2 } + \cdot \cdot \cdot + \xi _ { n } ^ { 2 } = \xi _ { 1 } ^ { 2 } + \cdot \cdot \cdot + \xi _ { p } ^ { 2 } + y _ { q + 1 } ^ { 2 } ( \xi ) + \cdot \cdot \cdot + y _ { n } ^ { 2 } ( \xi ) = 0 ,$ and thus $\xi _ { p + 1 } = 0 , \ldots , \xi _ { n } = 0$ . Then, we have $\xi = 0$ , which is a contradiction. This shows that $p \leq q$ . Similarly, $q \leq p$ , then $p = q$ . -

Theorem 2.7 (Witt). If a non-singular Hermitian matrix $\left[ \begin{array} { l l } { G _ { 0 } } & { 0 } \\ { 0 } & { G _ { 1 } } \end{array} \right]$ is conjugate congruent to $\left[ \begin{array} { l l } { G _ { 0 } } & { 0 } \\ { 0 } & { G _ { 2 } } \end{array} \right]$ , then $G _ { 1 }$ is conjugate congruent to $G _ { 2 }$ .

Proof. We first prove the case $G _ { 0 } = 1$ , i.e., 1 00 G1 ! ∼ 1 00 G 2 ! . Let $T = \left[ \begin{array} { l l } { a } & { \bar { b } ^ { \prime } } \\ { c } & { d } \end{array} \right]$ and T ∗ $T ^ { * } \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { G _ { 1 } } \end{array} \right] ^ { - } T = \left[ \begin{array} { l l } { 1 } & { \mathbf { \bar { 0 } } } \\ { 0 } & { G _ { 2 } } \end{array} \right]$ . Then, ,i.e., $\begin{array} { r } { \mathrm {  { ~ \frac { ~ 1 } { ~ 1 } ~ } } 0 } \\ { 0 \mathrm {  { ~ \ G ~ } } _ { 2 } \mathrm {  { ~ ] ~ } } = [ \begin{array} { l l } { \overline { { a } } } & { c ^ { * } } \\ { \overline { { b } } } & { d ^ { * } } \end{array} ] [ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { G _ { 1 } } \end{array} ] [ \begin{array} { l l } { a } & { \overline { { b } } ^ { \prime } } \\ { c } & { d } \end{array} ] = [ \begin{array} { l l } { \overline { { a } } a + c ^ { * } G _ { 1 } c } & { \overline { { a } } \overline { { b } } ^ { \prime } + c ^ { * } G _ { 1 } d } \\ { \overline { { b } } a + d ^ { * } G _ { 1 } c } & { \overline { { b } } \overline { { b } } ^ { \prime } + d ^ { * } G _ { 1 } d } \end{array} ] } \end{array}$ ,i.e.,

$$
\begin{array} { l l } { { \overline { { { a } } } a + c ^ { * } G _ { 1 } c = 1 , \quad \overline { { { a } } } \bar { b } ^ { \prime } + c ^ { * } G _ { 1 } d = 0 , } } \\ { { \bar { \overline { { { b } } } } a + d ^ { * } G _ { 1 } c = 0 , \quad \bar { \overline { { { b } } } } \bar { b } ^ { \prime } + d ^ { * } G _ { 1 } d = G _ { 2 } . } } \end{array}
$$

Let $d _ { \lambda } = d + \lambda c b ^ { \prime }$ ,

$$
\begin{array} { r c l } { { d _ { \lambda } ^ { * } G _ { 1 } d _ { \lambda } \ = \ ( d ^ { * } + \overline { { { \lambda } } } \bar { b } c ^ { * } ) G _ { 1 } ( d + \lambda c \bar { b } ^ { \prime } ) } } \\ { { } } & { { } } \\ { { } } & { { = \ d ^ { * } G _ { 1 } d + \overline { { { \lambda } } } \bar { b } c ^ { * } G _ { 1 } d + \lambda d ^ { * } G _ { 1 } c \bar { b } ^ { \prime } + | \lambda | ^ { 2 } \bar { \bar { b } } c ^ { * } G _ { 1 } c \bar { b } ^ { \prime } } } \\ { { } } & { { } } & { { = \ G _ { 2 } - \bar { \bar { b } } \bar { b } ^ { \prime } - \overline { { { \lambda } } } \bar { b } \bar { a } \bar { b } ^ { \prime } - \lambda \bar { \bar { b } } a \bar { b } ^ { \prime } + | \lambda | ^ { 2 } ( \bar { \bar { b } } \bar { b } ^ { \prime } - \bar { a } a \bar { \bar { b } } \bar { b } ^ { \prime } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = \ G _ { 2 } - ( 1 + \lambda a + \bar { a } \bar { \lambda } - ( 1 - | a | ^ { 2 } ) | \lambda | ^ { 2 } ) \bar { \bar { b } } \bar { b } ^ { \prime } . } } \end{array}
$$

If $\lambda$ satisfies the equation

$$
1 + \lambda a + \overline { { { a } } } \overline { { { \lambda } } } - ( 1 - | a | ^ { 2 } ) | \lambda | ^ { 2 } = 0 ,
$$

then

It only needs to take

$$
d _ { \lambda } ^ { \ast } G _ { 1 } d _ { \lambda } = G _ { 2 } .
$$

$$
\lambda = { \left\{ \begin{array} { l l } { - { \frac { 1 } { 2 } } , } & { { \mathrm { i f ~ } } a = 1 , } \\ { { \frac { 1 } { 1 - a } } , } & { { \mathrm { i f ~ } } a \neq 1 . } \end{array} \right. }
$$

If the order $r$ of $G _ { 0 }$ is larger than 1, then

$$
G _ { 0 } \stackrel { c } { \sim } \left[ \begin{array} { c c c } { { \pm 1 } } & { { } } & { { 0 } } \\ { { } } & { { \ddots } } \\ { { 0 } } & { { } } & { { \pm 1 } } \end{array} \right] _ { r \times r } ,
$$

and thus

$$
\begin{array} { r } { [ ( \begin{array} { c c c c } { \pm 1 } & & & { \vdots } \\ & { \ddots } & \\ & & { \vdots } \\ & { \cdots } & { \cdots } & { \vdots } \\ { \cdots } & { \cdots } & { \cdots } & { \vdots } \\ & { 0 } & & & { \vdots } \end{array} ) _ { F } \underset { G _ { 1 } } { \vdots } ] \underset { G _ { 1 } } { \sim } [ \begin{array} { c c c c } { \pm 1 } & & & { \vdots } \\ & { \ddots } & \\ & & { \vdots } \\ & { \cdots } & { \cdots } & { \vdots } \\ & & { 0 } & { \vdots } \\ & & & { \vdots } \end{array} ] _ { F } \underset { G _ { 2 } } { \vdots } ] _ { G _ { 1 } } . } \end{array}
$$

We denote

$$
\widetilde { G } _ { 1 } = \left[ \begin{array} { c c c c c } { { } } & { { } } & { { } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { \vdots } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { \pm 1 } } & { { \biggr ) _ { r - 1 } } } & { { \vdots } } & { { } } \\ { { } } & { { \cdots } } & { { \cdots } } & { { \cdots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { 0 } } & { { } } & { { \vdots } } & { { G _ { 1 } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \vdots } } \end{array} \right] ,
$$

$$
\widetilde { G } _ { 2 } = \left[ \begin{array} { c c c c c } { { } } & { { } } & { { } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { \vdots } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { \pm 1 } } & { { \scriptstyle \longmapsto } } & { { \vdots } } \\ { { } } & { { \cdots } } & { { \cdots } } & { { \cdots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { 0 } } & { { } } & { { \vdots } } & { { G _ { 2 } } } \\ { { } } & { { } } & { { } } & { { } } & { { \vdots } } & { { } } \end{array} \right] ,
$$

then by the result just proved above, $\widetilde { G _ { 1 } } \stackrel { c } { \sim } \widetilde { G _ { 2 } }$ . By recursions, we can finally get

$$
G _ { 1 } \stackrel { c } { \sim } G _ { 2 } .
$$

The Witt theorem gives another proof of the invariance of index $p$ . If

$$
\left[ \begin{array} { l l } { I _ { p } } & { 0 } \\ { 0 } & { - I _ { n - p } } \end{array} \right] \stackrel { c } { \sim } \left[ \begin{array} { l l } { I _ { p ^ { \prime } } } & { 0 } \\ { 0 } & { - I _ { n - p ^ { \prime } } } \end{array} \right] ,
$$

and $p > p ^ { \prime }$ , then

$$
\left[ \begin{array} { l l } { I _ { p - p ^ { \prime } } } & { 0 } \\ { 0 } & { - I _ { n - p } } \end{array} \right| \stackrel { c } { \sim } \left| \begin{array} { l l } { * } & \\ & { - I _ { n - p ^ { \prime } } } \end{array} \right] ,
$$

i.e., there exists a matrix $T \in G L ( n - p ^ { \prime } , \mathbf { C } )$ , such that

$$
\left[ \begin{array} { l l } { I _ { p - p ^ { \prime } } } & { 0 } \\ { 0 } & { - I _ { n - p } } \end{array} \right] = - T ^ { * } T .
$$

The (1,1) element of the given matrix is

$$
1 = - ( | t _ { i _ { 1 } } | ^ { 2 } + \cdot \cdot \cdot + | t _ { n - p ^ { \prime } } | ^ { 2 } ) ,
$$

which is a contradiction.

# 2.2.3 Similar Reduction to Canonical Forms under Orthogonal Transformation

For comparison, we list the canonical forms of Hermitian, conformal Hermitian matrices, real symmetric, and anti-symmetric matrices under unitary or orthogonal transformations in the Table 2.2. The content can be found in any standard textbook.

Table 2.2. $H , S$ and $K$ under unitary or orthogonal transformations   

<table><tr><td rowspan=1 colspan=2>Matrices</td><td rowspan=1 colspan=1>Canonical form</td></tr><tr><td rowspan=1 colspan=2>H*=H,λk∈R入1入00</td><td rowspan=1 colspan=1>If Xi is an eigenvalue of H, then :，w1≠O,s.t.Hwi=λiW1,(w1,wi)=1.{wi,Hwi&gt;= {wi,Xiwi&gt;=λ1.{wi,Hwi&gt;∈R=λi∈R.z∈{wi}-=Hzi∈{ω1}↓So,T ∈ U(n,C),s.t.T-1HTo = 入1  00H1where H = H1</td></tr><tr><td rowspan=1 colspan=2>H*=eiH,λk ∈Re-i0/2X1e-10/2λr00</td><td rowspan=2 colspan=1>Sis areal matrix,S&#x27;=S⇒Sis a Hermitian matrix.If 入i is an eigenvalue,then:w1 ∈R,s.t.Swi=λiW1,(w1,w1)= 1.Similarly,x∈{ω1}-=Sx∈{ω1}¹.Analogous, T ∈ O(n,R),s.t.T-1sTo = 入1 00 S1where S1 = S</td></tr><tr><td rowspan=1 colspan=1>S&#x27;=S,Xk∈R入1入r00</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=3>Kanti-symmetrical,iK is a Hermitian matrix,its eigenvalues are real.If 入1≠ Ois an eigenvalue of iK,then wi=u-iv≠0,K&#x27;=-K,λk&gt;0,                s.t.iK(u-iv)=λi(u-iv).2s=r                                (1)Kv=λiu,0  入1                                                            →-入1 0λi(u,v)=(v,Kv)=0.Sinceλi ≠ O,we have(u,v) = 0.0  入s                 From(1)and (2),we get u ≠ 0,v≠0.-入s  0                 Suppose: (u,u) = (v,v) = 1.On-ror                         Then:(u,Ku)=0,(u,Kv)=λ1,0  A                                (u,Kv)=0,(v,Ku)=-λ1.-A 0On-r                  Ifx ∈{u,v}-,then :whereA= diag{入1,λ2,.,λs}           Kx ∈{u,v}-.Thus, T ∈ O(n,R), s.t.0  入1T-1KT =  -入1 0K1where K=K1</td></tr></table>

Next, we consider Jordan canonical forms. Let us first recall the Jordan canonical form for a general real matrix $A \in M ( n , \mathbf { R } )$ . A Jordan canonical form viewed in real space is different from the Jordan canonical form viewed in complex space.

# 1. Elementary divisors in complex space

In complex space, the elementary divisor corresponding to a paired-complex conjugate eigenvalue $\alpha \pm \mathrm { i } \beta , \beta \neq 0$ is of the form

$$
[ \lambda - ( \alpha + \mathrm { i } \beta ) ] ^ { p } , \quad [ \lambda - ( \alpha - \mathrm { i } \beta ) ] ^ { p } .
$$

The corresponding Jordan blocks are

$$
\left[ \begin{array} { c c c c } { { \alpha + { \bf i } \beta } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { \alpha + { \bf i } \beta } } & { { \ddots } } & { { } } \\ { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { \alpha + { \bf i } \beta } } \end{array} \right] _ { p \times p } , \qquad \left[ \begin{array} { c c c c } { { \alpha - { \bf i } \beta } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { \alpha - { \bf i } \beta } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { \alpha + { \bf i } \beta } } \end{array} \right] _ { p \times p } ,
$$

The elementary divisor corresponding to a real eigenvalue $\gamma$ is of the form

$$
( \lambda - \gamma ) ^ { q } .
$$

Its Jordan block is

$$
\left[ \begin{array} { l l l l } { \gamma } & { 1 } & & & \\ & { \gamma } & { \ddots } & \\ & & { \ddots } & \\ & & & { \gamma } \end{array} \right] _ { q \times q } \sim ( \lambda - \gamma ) ^ { q } .
$$

# 2. Elementary divisor in real space

In real space, the elementary divisor corresponding to a paired complex conjugate eigenvalues $\alpha \pm \mathrm { ~ i ~ } \beta , ( \beta \neq 0 )$ is of the form

$$
[ \lambda ^ { 2 } - 2 \alpha \lambda + ( \alpha ^ { 2 } + \beta ^ { 2 } ) ] ^ { p } .
$$

Its Jordan block is

$$
\begin{array} { r } { \left[ \begin{array} { c c c c c c c c } { 0 } & { 1 } & & & & & & \\ { - ( \alpha ^ { 2 } + \beta ^ { 2 } ) } & { 2 \alpha } & { 1 } & & & & & \\ & { 0 } & { 1 } & & & & & \\ & & { - ( \alpha ^ { 2 } + \beta ^ { 2 } ) } & { 2 \alpha } & { 1 } & & & & \\ & & & & { \ddots } & & & \\ & & & & { \ddots } & & & & \\ & & & & & { 1 } & & \\ & & & & & & { 0 } & { 1 } \\ & & & & & & & { - ( \alpha ^ { 2 } + \beta ^ { 2 } ) } & { 2 \alpha } \end{array} \right] _ { 2 p \times 2 p } } \end{array}
$$

The elementary divisor and the Jordan block corresponding to a real eigenvalue $\gamma$ is the same as in complex space, i.e.,

$$
\left[ \begin{array} { l l l l } { \gamma } & { 1 } & & & \\ & { \gamma } & { \ddots } & \\ & & { \ddots } & \\ & & & { \gamma } \end{array} \right] _ { q \times q } \sim ( \lambda - \gamma ) ^ { q } .
$$

# 2.3 Symplectic Space

A symplectic vector space is a vector space $V$ equipped with a nondegenerate, skewsymmetric, bilinear form $\omega$ called the symplectic form.

Explicitly, a symplectic form is a bilinear form $\omega : V \times V \to \mathbf { R }$ that is

$1 ^ { \circ }$ Skew-symmetric: $\omega ( u , v ) = - ( v , u ) \ \forall u , v \in V$ .   
$2 ^ { \circ }$ Nondegenerate: if $\omega ( u , v ) = 0 \ \forall v \in V$ , then $u = 0$ .

Working in a fixed basis, $\omega$ can be represented by a matrix. The two conditions above imply that this matrix must be skew-symmetric and nons-singular. This is not the same as a symplectic matrix, which represents a symplectic transformation of the space.

# 2.3.1 Symplectic Space and Its Subspace

1. Comparison between symplectic and Euclidian space[Tre75,LM87,FQ91a,Wei77] In this section, we restrict ourselves to $\mathbf { R } ^ { 2 n }$ . The symbol $\Leftrightarrow$ , which stands for “if and only if”, will be widely adopted under $J$ orthogonality and $I$ Orthogonality.

Sympl. Structure $J$ -Sympl. Matrix Euclidian Structure $I$ -Unit Matrix

$$
{ \begin{array} { r l r l } & { [ x , y ] = x ^ { \prime } J y , } & & { \ ( x , y ) = x ^ { \prime } I y ; } \\ & { [ y , x ] = - [ x , y ] , } & & { \ ( y , x ) = ( x , y ) ; } \\ & { [ x , x ] = 0 , \ \forall x , } & & { \ ( x , x ) > 0 , \ \forall x \neq 0 ; } \\ & { [ x , y ] = ( x , J y ) . } & & { \ ( x , y ) = [ x , J ^ { - 1 } y ] . } \end{array} }
$$

$$
\begin{array} { r l r l } & { x \top y \Longleftrightarrow [ x , y ] = 0 \Longleftrightarrow y \top x , } & & { x \bot y \Longleftrightarrow ( x , y ) = 0 \Longleftrightarrow y \bot x . } \\ & { U \top V \Longleftrightarrow [ x , y ] = 0 , \forall x \in U , y \in V , } & & { U \bot V \Longleftrightarrow ( x , y ) = 0 , x \in U , y \in V . } \\ & { U \top V \Longleftrightarrow U \bot J V , } & & { U \bot V \Longleftrightarrow U \top J ^ { - 1 } V . } \end{array}
$$

Definition 3.1. $V ^ { \top } = \{ x \in { \bf R } ^ { 2 n } \mid [ x , y ] = 0 , \forall y \in V \} . V ^ { \bot } = \{ x \in { \bf R } ^ { 2 n } \mid ( x , y ) =$   
$0 , \forall y \in V \}$ .

By definition, we have $V ^ { \top } = ( J V ) ^ { \bot } , V ^ { \bot } = ( J ^ { - 1 } V ) ^ { \top }$ .

Proposition 3.2. $U \subset \mathbf { R } ^ { 2 n }$ , $V \subset \mathbf { R } ^ { 2 n }$ . Then,

$$
\begin{array} { r l } & { U \subset V \Longleftrightarrow U ^ { \top } \supset V ^ { \top } , \quad U \subset V \Longleftrightarrow U ^ { \bot } \supset V ^ { \bot } ; } \\ & { ( U \cap V ) ^ { \top } = U ^ { \top } + V ^ { \top } , \quad ( U \cap V ) ^ { \bot } = U ^ { \bot } + V ^ { \bot } ; } \\ & { ( U + V ) ^ { \top } = U ^ { \top } \cap V ^ { \top } , \quad ( U + V ) ^ { \bot } = U ^ { \bot } \cap V ^ { \bot } ; } \\ & { { \mathrm { d i m } } U + { \mathrm { d i m } } U ^ { \top } = 2 n , \quad { \mathrm { d i m } } U + { \mathrm { d i m } } U ^ { \bot } = 2 n ; } \\ & { U ^ { \top } = U , \quad \quad \quad \quad \quad \quad \quad \quad \quad U ^ { \bot \bot } = U ; } \\ & { { \exists U , U \cap U ^ { \top } \neq \{ 0 \} , \quad \quad \quad \quad \quad } U \cap U ^ { \bot } = \{ 0 \} ; } \\ & { U + U ^ { \top } \neq { \bf R } ^ { 2 n } , \quad \quad \quad \quad \quad \quad U + U ^ { \bot } = { \bf R } ^ { 2 n } . } \end{array}
$$

Definition 3.3. $U \subset \mathbf { R } ^ { 2 n }$ , define $U ^ { 0 } = U \cap U ^ { \top }$ , called as the radical of $U$ .

# 2. Special classes of subspaces[HW63,Tre75,LM87,Wei77]

$$
{ \begin{array} { l l l } { V ~ { \mathrm { d e g e n e r a t e ~ s u b s p a c e : } } ~ V ^ { 0 } } & { = } & { V \cap V ^ { \top } \not = 0 } \\ & & { \iff ~ \dim V { \mathrm { ~ i s } } ~ { \mathrm { ~ o d d } } . } \end{array} }
$$

$$
{ \begin{array} { r l } { V { \mathrm { ~ i s o t r o p i c ~ s u b s p a c e : ~ } } V } & { \subset V ^ { \mathsf { T } } } \\ & { \Longleftrightarrow V \cap V ^ { \mathsf { T } } = V ^ { 0 } = V } \\ & { \Longleftrightarrow [ x , y ] = 0 { \mathrm { ~ o n ~ } } V } \\ & { \Longrightarrow { \mathrm { ~ d i m ~ } } V \leq n } \\ & { \Longleftrightarrow V ^ { \mathsf { T } } { \mathrm { ~ c o i s o t r o p i c } } } \\ & { \Longleftrightarrow { \mathrm { ~ d i m ~ } } V = 1 . } \end{array} }
$$

$$
{ \begin{array} { r l } { V { \mathrm { ~ c o i s o t r o p i c ~ s u b s p a c e : ~ } } V ^ { \top } } & { \subset V } \\ & { \Longleftrightarrow V \cap V ^ { \top } = V ^ { 0 } = V ^ { \top } } \\ & { \Longleftrightarrow [ x , y ] = 0 { \mathrm { ~ o n ~ } } V ^ { \top } } \\ & { \Longrightarrow { \mathrm { ~ d i m ~ } } V \geq n } \\ & { \Longleftrightarrow V ^ { \top } { \mathrm { ~ i s o t r o p i c } } } \\ & { \Longleftrightarrow { \mathrm { ~ d i m ~ } } V = 2 n - 1 . } \end{array} }
$$

$$
{ \begin{array} { l l l } { V { \mathrm { ~ L a g r a n g i a n : ~ } } V ^ { \top } } & { = } & { V } \\ & { \iff } & { V { \mathrm { ~ i s ~ i s o t r o p i c ~ a n d ~ c o i s o t r o p i c } } } \\ & { \iff } & { V { \mathrm { ~ i s ~ i s o t r o p i c ~ a n d ~ d i m } } V = n } \\ & { \iff } & { V { \mathrm { ~ i s ~ c o i s o t r o p i c ~ a n d ~ d i m } } V = n } \\ & { \iff } & { V { \mathrm { ~ i s ~ c o i s o t r o p i c ~ a n d ~ d i m } } V = n } \\ & { \iff } & { V { \mathrm { ~ m a x i m a l l y ~ i s o t r o p i c } } } \\ & { \iff } & { V { \mathrm { ~ m i n i m a l l y ~ c o i s o t r o p i c } } } \end{array} }
$$

$$
{ \begin{array} { r l } { V { \mathrm { ~ n o n - d e g e n e r a t e : ~ } } V { \mathrm { ~ n V ~ } } } & { = \quad \{ 0 \} } \\ & { \Longleftrightarrow V + V ^ { \top } = \mathbf { R } ^ { 2 n } } \\ & { \Longleftrightarrow \quad [ x , y ] { \mathrm { ~ n o n - d e g e n e r a t e ~ o n ~ } } V } \\ & { \Longleftrightarrow \quad \operatorname { f f } \left[ x , y \right] = 0 { \mathrm { ~ } } \forall y \in V , { \mathrm { ~ t h e n ~ } } x = 0 } \\ & { \Longleftrightarrow V ^ { \top } { \mathrm { ~ n o n - d e g e n e r a t e } } } \\ & { \Longrightarrow { \mathrm { ~ d i m ~ } } V { \mathrm { ~ i s ~ e v e n } } . } \end{array} }
$$

(6) Coordinate subspaces.

Define $\nu = \{ 1 , 2 , \cdots , n \}$ with the natural order. If $\alpha = \{ i _ { 1 } , i _ { 2 } , \cdot \cdot \cdot , i _ { k } \} \subset \nu ( i _ { 1 }$ $< \cdots < i _ { k }$ ), the total number of $\alpha ^ { \prime } s$ is $2 ^ { n }$ . Denote $\widehat { \alpha } = \nu \backslash \alpha = \{ j _ { 1 } , \cdot \cdot \cdot , j _ { n - k } \} \ ( j$ $( j _ { 1 }$ $< \ldots < j _ { n - k } ) , \widehat { \nu } = \varnothing , \widehat { \alpha } \cup \alpha = \nu , \widehat { \alpha } \cap \alpha = \varnothing .$ .

Definition 3.4. Define a coordinate subspace $R _ { \alpha , \beta } = \{ e _ { i } , f _ { j } \} _ { i \in \alpha , j \in \beta }$ , where

$$
e _ { 1 } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] } , \cdots , e _ { n } = { \left[ \begin{array} { l } { 0 } \\ { \vdots } \\ { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] } , f _ { 1 } = { \left[ \begin{array} { l } { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \\ { \vdots } \\ { 0 } \end{array} \right] } , \cdots , f _ { n } = { \left[ \begin{array} { l } { 0 } \\ { \vdots } \\ { 0 } \\ { 0 } \\ { \vdots } \\ { 1 } \end{array} \right] } .
$$

The total number of coordinate subspaces $R _ { \alpha , \beta }$ is $2 ^ { 2 n }$

Problem 3.5. We have the following issues to address:

$1 ^ { \circ }$ Under what conditions about $\alpha , \beta$ is $R _ { \alpha , \beta }$ isotropic, coisotropic, Lagrangian? $2 ^ { \circ }$ Define $I _ { \alpha } = [ d _ { i } \delta _ { i j } ]$ , $d _ { i } = \left\{ \begin{array} { l l } { 1 , } & { i \in \alpha , } \\ { 0 , } & { i \in \widehat { \alpha } . } \end{array} \right.$

Proof. .

$$
\begin{array} { r l } & { I _ { \nu } = I _ { n } , \ I _ { \widehat { \nu } } = I _ { \otimes } = O _ { n } , \quad I _ { \alpha } ^ { 2 } = I _ { \alpha } , } \\ & { I _ { \alpha } I _ { \widehat { \alpha } } = O _ { n } , \quad I _ { \alpha } I _ { \beta } = I _ { \alpha \cap \beta } , \quad I _ { \alpha } + I _ { \widehat { \alpha } } = I , } \\ & { I _ { \alpha } + I _ { \beta } = I _ { \alpha \cap \beta } + I _ { \alpha \cup \beta } = I _ { \alpha \cup \beta } + I _ { \alpha } I _ { \beta } . } \end{array}
$$

The proof can be obtained.

$3 ^ { \circ }$ Show that the subspaces $D = \{ p _ { i } = \pm q _ { i } , i = 1 , 2 , \cdot \cdot \cdot , n \}$ are Lagrangian and transversal to all coordinate Lagrangian subspaces.

Theorem 3.6. Let $W$ be non-degenerate and $W = U { \textcircled { \mathrm { 1 } } } V$ , where $U \textcircled { \mathrm { ‰} } V$ stands for the $J$ -orthogonal sum. Then $U , V$ both are non-degenerate.

Proof. Let $x \in U$ such that $[ x , y ] = 0 , \forall y \in U .$ Then, from $U \subset V ^ { \top }$ , it follows that $[ x , z ] = 0$ , $\forall z \ \in \ V$ . Therefore, $[ x , w ] = 0$ , $\forall w \in W$ . By assumption, $W$ is non-degenerate, and so $x = 0$ . This shows $U$ is non-degenerate. Similarly, $V$ is nondegenerate too. -

Theorem 3.7. If $U$ is isotropic, then there exists a Lagrangian subspace $V \supset U$ .

Proof. Without loss of generality, we can assume that dim $U = k < n$ . Therefore, there exists a vector $a _ { k + 1 } \in U ^ { \top } \backslash U \neq \emptyset$ , $V = U + \{ a _ { k + 1 } \} \supset U ,$ $V$ is isotropic. $\blacktriangle$

By repeating this procedure, we can get a Lagrangian subspace $V \supset U$ .

Theorem 3.8. For a given Lagrangian subspace $U = \{ a _ { 1 } , a _ { 2 } , \cdot \cdot \cdot , a _ { n } \}$ , there exists another Lagrangian subspace $V = \{ b _ { 1 } , b _ { 2 } , \cdots , b _ { n } \}$ , such that

$$
\begin{array} { c } { { { \bf R } ^ { 2 n } = P _ { 1 } \mathbb { O } P _ { 2 } \mathbb { O } \cdot \cdot \cdot \mathbb { O } P _ { n } = U \dot { + } V , } } \\ { { { \bf \Pi } } } \\ { { P _ { i } = \{ a _ { i } , b _ { i } \} , [ a _ { i } , a _ { j } ] = [ b _ { i } , b _ { j } ] = 0 , [ a _ { i } , b _ { j } ] = \delta _ { i j } . } } \end{array}
$$

Proof. We proceed by induction with respect to dimension $n$ . For $n = 1$ , by nondegenerality of $\mathbf { R } ^ { 2 }$ , there is a vector $b _ { 1 }$ , satisfying $[ a _ { 1 } , b _ { 1 } ] = 1$ . Of course, $\{ b _ { 1 } \}$ is Lagrangian. Thus, this theorem is true for $n = 1$ .

Assume that for $n { - } 1$ , the theorem is true. Then, for $\mathbf { R } ^ { 2 n }$ $\mathbf { \Phi } ^ { \iota } , \{ a _ { 1 } \} \not \subset \{ a _ { 2 } , a _ { 3 } , \cdot \cdot \cdot , a _ { n } \}$ and so $\{ a _ { 2 } , a _ { 3 } , \cdot \cdot \cdot , a _ { n } \} ^ { \top } \backslash \{ a _ { 1 } \} ^ { \top } \neq \emptyset$ , there is a vector $b _ { 1 } \in \{ a _ { 2 } , a _ { 3 } , \cdot \cdot \cdot , a _ { n } \} ^ { \top } \ \backslash$ $\{ a _ { 1 } \} ^ { \top }$ , such that

$$
[ a _ { 1 } , b _ { 1 } ] = 1 , \quad [ a _ { 2 } , b _ { 1 } ] = \cdot \cdot \cdot = [ a _ { n } , b _ { 1 } ] = 0 .
$$

Set $P _ { 1 } = \{ a _ { 1 } , b _ { 1 } \}$ . By above subspace(5) and Theorem 3.6,

$$
\mathbf { R } ^ { 2 n } = P _ { 1 } \mathbb { O } P _ { 1 } ^ { \top } , \quad P _ { 1 } \cap P _ { 1 } ^ { \top } = \{ 0 \} ,
$$

dim $P _ { 1 } ^ { \top } = 2 ( n - 1 )$ , $\{ a _ { 2 } , a _ { 3 } , \cdot \cdot \cdot , a _ { n } \} \subset P _ { 1 } ^ { \top }$ is maximally isotropic in $P _ { 1 } ^ { \top }$ , i.e., a Lagrangian subspace of $P _ { 1 } ^ { \top }$ . By inductive assumption, there exists $b _ { 2 } , \cdots , b _ { n }$ and $\{ b _ { 2 } , \cdots , b _ { n } \}$ is Lagrangian space in $P _ { 1 } ^ { \top }$ . Moreover,

$$
[ a _ { i } , a _ { j } ] = [ b _ { i } , b _ { j } ] = 0 , \quad [ a _ { i } , b _ { j } ] = \delta _ { i j } , \quad i , j = 2 , \cdots , n .
$$

Therefore, for all $i , j$ , we have

$$
[ a _ { i } , a _ { j } ] = [ b _ { i } , b _ { j } ] = 0 , \quad [ a _ { i } , b _ { j } ] = \delta _ { i j } .
$$

Set $P _ { i } = \{ a _ { i } , b _ { i } \}$ , then $\mathbf { R } ^ { 2 n } = P _ { 1 } \mathbb { D } P _ { 2 } \mathbb { O } \cdot \cdot \cdot \mathbb { O } P _ { n }$

Theorem 3.9. Let $U , V$ be two Lagrangian subspaces, $U = \{ a _ { 1 } , a _ { 2 } , \cdot \cdot \cdot , a _ { n } \} , U \cap$ $V = \{ 0 \}$ . Then, there exists a unique base $b _ { 1 } , b _ { 2 } , \cdots , b _ { n }$ , such that $V = \{ b _ { 1 } , b _ { 2 } , \cdots ,$ , $b _ { n } \}$ , and

$$
[ a _ { i } , a _ { j } ] = [ b _ { i } , b _ { j } ] = 0 , \quad [ a _ { i } , b _ { j } ] = \delta _ { i j } .
$$

Proof. Similarly manner, by induction with respect to dimension $n$ , the proof can be obtained. -

Theorem 3.10. If $U$ is not isotropic, then there exists a non-degenerate subspace $N \subset$ $U , N \neq \{ 0 \}$ , such that

$$
U = U ^ { 0 } \mathbb { O } N , \quad U ^ { 0 } = U \cap U ^ { \top } .
$$

Proof. By assumption $U ^ { 0 } = \{ x \in U | [ x , y ] = 0 , \forall y \in U \} \neq U$ . Therefore, there is a subspace $N \subset U , N \neq \{ 0 \}$ , such that $N \cap U ^ { 0 } = \{ 0 \}$ and $U = N \dot { + } U ^ { 0 }$ .

Since $U ^ { 0 } \top U$ , of course $U ^ { 0 } \top N$ . If $x \in N$ and $[ x , y ] = 0 , \forall y \in N$ , then by $U ^ { 0 } \top N$ , we have $[ x , z ] = 0 , \forall z \in U ^ { 0 }$ i.e., $[ x , y ] = 0 , \forall y \in U$ . Thus, $x \in U ^ { 0 } \cap N = \{ 0 \}$ , and $x$ must be $= 0$ . Therefore, $N$ is non-degenerate. -

Theorem 3.11. Let $V _ { 1 } , V _ { 2 }$ be two disjoint isotropic subspaces. Then, there exist two Lagrangian subspaces $W _ { 1 } , W _ { 2 }$ that are disjoint. $W _ { 1 } \cap W _ { 2 } = \{ 0 \}$ such that $W _ { 1 } \supset$ $V _ { 1 }$ , $W _ { 2 } \supset V _ { 2 }$ .

$$
U = V _ { 1 } \dot { + } V _ { 2 } , U ^ { 0 } = U \cap U ^ { \top } = ( V _ { 1 } \dot { + } V _ { 2 } ) \cap ( V _ { 1 } \dot { + } V _ { 2 } ) ^ { \top } .
$$

$1 ^ { \circ }$ If $U$ is isotropic. Assume

$$
V _ { 1 } = \{ a _ { 1 } , \cdot \cdot \cdot , a _ { r } \} , \quad V _ { 2 } = \{ b _ { r + 1 } , \cdot \cdot \cdot , b _ { r + s } \} .
$$

By Theorem 3.7, there exists $V _ { 3 } = \{ a _ { r + s + 1 } , \cdot \cdot \cdot , a _ { n } \}$ , such that

$$
V _ { 1 } \dot { + } V _ { 2 } \dot { + } V _ { 3 } = \{ a _ { 1 } , \cdots , a _ { r } , b _ { r + 1 } , \cdots , b _ { r + s } , a _ { r + s + 1 } , \cdots , a _ { n } \}
$$

is Lagrangian. Moreover, by Theorem 3.8, there exist $b _ { 1 } , \cdot \cdot \cdot , b _ { r } , a _ { r + 1 } , \cdot \cdot \cdot , a _ { r + s }$ , $b _ { r + s + 1 } , \cdot \cdot \cdot , b _ { n } \in \mathbf { R } ^ { 2 n }$ , such that

$$
[ a _ { i } , a _ { j } ] = [ b _ { i } , b _ { j } ] = 0 , \quad [ a _ { i } , b _ { j } ] = \delta _ { i j } .
$$

Set $W _ { 1 } = \{ a _ { 1 } , \cdots , a _ { r } , a _ { r + 1 } , \cdots , a _ { r + s } , a _ { r + s + 1 } , \cdots , a _ { n } \} , \ : W _ { 2 } = \{ b _ { 1 } , \cdots , b _ { n } \} .$ Obviously, $W _ { 1 } , W _ { 2 }$ are Lagrangian and $W _ { 1 } \cap W _ { 2 } = \{ 0 \} , \ : V _ { 1 } \subset W _ { 1 } , \ : V _ { 2 } \subset W _ { 2 } .$

$2 ^ { \circ }$ If $U$ is not isotropic. Set $U _ { 1 } ^ { 0 } = V _ { 1 } \cap V _ { 2 } ^ { \top }$ , $U _ { 2 } ^ { 0 } = V _ { 2 } \cap V _ { 1 } ^ { \top }$ , then

$$
U ^ { 0 } = U _ { 1 } ^ { 0 } \dot { + } U _ { 2 } ^ { 0 } , \quad U _ { i } ^ { 0 } = V _ { i } \cap U ^ { 0 } , \quad i = 1 , 2 .
$$

Evidently,

$$
\begin{array} { r l } { U _ { i } ^ { 0 } } & { = V _ { i } \cap U ^ { 0 } = V _ { i } \cap U \cap U ^ { \top } } \\ & { = V _ { i } \cap ( V _ { 1 } \dotplus V _ { 2 } ) ^ { \top } = V _ { i } \cap ( V _ { 1 } ^ { \top } \cap V _ { 2 } ^ { \top } ) , \quad i = 1 , 2 . } \end{array}
$$

By assumption, $V _ { i } ( i = 1 , 2 )$ are isotropic, i.e., $V _ { i } \subset V _ { i } ^ { \top } ( i = 1 , 2 )$ . By the following Lemma 3.12,

$$
\begin{array} { r l } & { U _ { 1 } ^ { 0 } \dot { + } U _ { 2 } ^ { 0 } = V _ { 1 } \cap ( V _ { 1 } ^ { \top } \cap V _ { 2 } ^ { \top } ) \dot { + } V _ { 2 } \cap ( V _ { 1 } ^ { \top } \cap V _ { 2 } ^ { \top } ) } \\ & { ~ = ( V _ { 1 } \dot { + } V _ { 2 } ) \cap ( V _ { 1 } ^ { \top } + V _ { 2 } ^ { \top } ) } \\ & { ~ = U \cap U ^ { \top } = U ^ { 0 } . } \end{array}
$$

Take $N _ { i } \subset V _ { i } ( i = 1 , 2 )$ , such that $V _ { i } = U _ { i } ^ { 0 } \mathbb { O } N _ { i }$ .

Set $N = N _ { 1 } \dot { + } N _ { 2 }$ , then

$$
U = V _ { 1 } + V _ { 2 } = U _ { 1 } ^ { 0 } + N _ { 1 } + U _ { 2 } ^ { 0 } + N _ { 2 } = U ^ { 0 } + N .
$$

Similar to the proof of Theorem 3.10, we can see that $N$ is non-degenerate and $U = U ^ { 0 } \mathbb { O } N .$ . Of course, $N _ { i } = N \cap V _ { i } ( i = 1 , 2 )$ , and $N _ { 1 } \subset N \cap V _ { 1 }$ .

If $x \in N \cap V _ { 1 }$ , then $x = x _ { 1 } + x _ { 2 }$ , $x _ { 1 } \in N _ { 1 }$ , $x _ { 2 } \in N _ { 2 }$ . Moreover, by $x \in V _ { 1 }$ , we have $x _ { 2 } = x - x _ { 1 } \in V _ { 1 }$ . Thus, $x _ { 2 } \in V _ { 1 } \cap V _ { 2 } = \{ 0 \}$ , $x _ { 2 } = 0$ . This shows that $x = x _ { 1 } \in N _ { 1 }$ .

As $N$ is non-degenerate, $\mathbf { R } ^ { 2 n } = { \cal N } \mathbb { O } { \cal N } ^ { \top }$ , $U ^ { 0 } = U _ { 1 } ^ { 0 } + U _ { 2 } ^ { 0 } \subset N ^ { \top }$ . By $N = N _ { 1 } \dot { + }$ $N _ { 2 }$ and $N _ { 1 } , \ N _ { 2 }$ being isotropic, we know that $N _ { 1 } , \ N _ { 2 }$ both are maximal isotropic, i.e., Lagrangian in $N$ .

For the non-degenerate subspace $N ^ { \top }$ , since $U ^ { 0 } = U _ { 1 } ^ { 0 } + U _ { 2 } ^ { 0 } \subset N ^ { \top }$ is isotropic, applying results $1 ^ { \circ }$ of Theorem 3.11 , there exist two Lagrangian subspaces $\overline { { W _ { 1 } } }$ , $\overline { { W _ { 2 } } }$ , in $N ^ { \top }$ , such that $\overline { { W _ { i } } } ~ \supset ~ U _ { i } ^ { 0 } ( i = 1 , 2 )$ and $\overline { { { W } } } _ { 1 } \cap \overline { { { W } } } _ { 2 } = \{ 0 \}$ . Set $W _ { 1 } = \overline { { W _ { 1 } } } \dot { + }$ $N _ { 1 }$ , $W _ { 2 } = \overline { { { W _ { 2 } } } } \dot { + } N _ { 2 }$ . Then, $W _ { i } ( i = 1 , 2 )$ are Lagrangian in ${ \bf R } ^ { 2 n } ( i = 1 , 2 )$ and $V _ { i } \subset W _ { i } ( i = 1 , 2 )$ , $W _ { 1 } \cap W _ { 2 } = \{ 0 \}$ . $\blacktriangle$

Lemma 3.12. If $A \subset A _ { 1 } , B \subset B _ { 1 }$ , then

$$
{ \begin{array} { r l } { ( A + B ) \cap ( A _ { 1 } \cap B _ { 1 } ) \ = A \cap ( A _ { 1 } \cap B _ { 1 } ) + B \cap ( A _ { 1 } \cap B _ { 1 } ) } & { } \\ & { } \\ & { = A \cap B _ { 1 } + B \cap A _ { 1 } . } \end{array} }
$$

Proof. $( A + B ) \cap ( A _ { 1 } \cap B _ { 1 } ) \subset A \cap ( A _ { 1 } \cap B _ { 1 } ) + B \cap ( A _ { 1 } \cap B _ { 1 } )$ is trivial. Let $x \in ( A + B ) \cap ( A _ { 1 } \cap B _ { 1 } )$ . Since $x \in A + B$ , then exists a decomposition

$$
x = a + b , \quad a \in A \subset A _ { 1 } , \quad b \in B \subset B _ { 1 } .
$$

Since $x \in A _ { 1 } \cap B _ { 1 }$ , $a = x - b _ { 1 } \in B _ { 1 } , \ b = x - a \in A _ { 1 }$

Thus, $a \in A \cap B _ { 1 }$ , $b \in B \cap A _ { 1 }$ , i.e., $x = a + b \in A \cap B _ { 1 } + B \cap A _ { 1 }$

Lemma 3.13. Let U, V, $W \subset \mathbf { R } ^ { m }$ , $V \dot { + } W = \mathbf { R } ^ { m }$ . Define a linear projection $\pi _ { V } ^ { W }$ along $W$ into $V$ as $\pi _ { V } ^ { W } : \mathbf { R } ^ { m }  \mathbf { R } ^ { m }$ ,

$$
\pi _ { V } ^ { W } x = { \left\{ \begin{array} { l l } { x , } & { \forall x \in V , } \\ { 0 , } & { \forall x \in W . } \end{array} \right. }
$$

Then, $U \dot { + } W = \mathbf { R } ^ { m }$ , iff $\pi _ { V } ^ { W } : U \to V$ is non-singular and onto.

Proof. Assume $x \in U$ , $\pi _ { V } ^ { W } x = 0$ . From $V \dot { + } W = \mathbf { R } ^ { m }$ , it follows that there exists a decomposition

$$
x = v + w , \quad { \mathrm { w h e r e } } \quad v \in V { \mathrm { ~ } } a n d w \in W .
$$

Thus,

$$
0 = \pi _ { V } ^ { W } x = \pi _ { V } ^ { W } ( v + w ) = \pi _ { V } ^ { W } v + \pi _ { V } ^ { W } w = \pi _ { V } ^ { W } v = v .
$$

Then, $x = w \in W$ , i.e., $x \in U \cap W = \{ 0 \}$ . We get $x = 0$

Conversely, if $x \in U \cap W$ , then $x \in W$ , $x \in U$ . By the definition of $\pi$ , we have $\pi x = 0$ . $\pi : U \to V$ is non-singular and so $x = 0$ , i.e.,

$$
W \cap U = \{ 0 \} , \quad U + W = \mathbf { R } ^ { m } .
$$

Therefore, the lemma is completed.

Theorem 3.14. For every Lagrangian subspace $L$ in $\mathbf { R } ^ { 2 n }$ , there exists a coordinate Lagrangian subspace $R _ { \alpha , \widehat { \alpha } }$ transversal to $L$ , i.e., $\exists \alpha \subset \nu$ , such that $R _ { \alpha , \hat { \alpha } } + L = \mathbf { R } ^ { 2 n }$ .

Proof. Since $( R _ { \nu , 0 } \cap L ) \subset { \cal R } _ { \nu , 0 } , \exists \alpha \subset \nu$ , such that

$$
\begin{array} { r l } & { R _ { \alpha , 0 } \cap ( R _ { \nu , 0 } \cap L ) = \{ 0 \} , } \\ & { R _ { \alpha , 0 } + ( R _ { \nu , 0 } \cap L ) = R _ { \nu , 0 } . } \\ & { R _ { \nu , 0 } ^ { T } \stackrel { \mathrm { L a g . } } { = } R _ { \nu , 0 } \subset R _ { \alpha , \widehat { \alpha } } + L \stackrel { \mathrm { L a g . } } { = } R _ { \alpha , \widehat { \alpha } } ^ { T } + L ^ { \top } = ( R _ { \alpha , \widehat { \alpha } } \cap L ) ^ { \top } . } \end{array}
$$

Therefore,

$$
\begin{array} { r c l } { { R _ { \alpha , \widehat { \alpha } } \cap L } } & { { = } } & { { ( R _ { \alpha , \widehat { \alpha } } \cap R _ { \nu , 0 } ) \cap ( R _ { \nu , 0 } \cap L ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { R _ { \alpha , 0 } \cap ( R _ { \nu , 0 } \cap L ) = \{ 0 \} . } } \end{array}
$$

Then,

$$
R _ { \alpha , \widehat { \alpha } } + L = \mathbf { R } ^ { 2 n } .
$$

The theorem is proved.

# 3. Matrix representation of subspaces in $\mathbf { R } ^ { 2 n }$

$$
A = { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { \cdots } & { a _ { 1 k } } \\ { \vdots } & & { \vdots } \\ { a _ { 2 n , 1 } } & { \cdots } & { a _ { 2 n , k } } \end{array} \right] } = \left[ a _ { 1 } , a _ { 2 } , \cdots , a _ { k } \right] = { \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] } ,
$$

where $A \in M ( 2 n , k ) , a _ { i } \in M ( 2 n , 1 ) , A _ { j } \in M ( n , k ) .$ .

Definition 3.15. $A \in M ( 2 n , k )$ is non-singular, if rank $A = k$

Let $A \in M ( 2 n , k ) , B \in M ( 2 n , l )$ . Then, $[ A , B ] \in M ( 2 n , k + l )$ . If $[ A , B ]$ is non-singular, then both $A$ and $B$ are non-singular.

$G _ { 2 n , k } = \{ \mathrm { a l l ~ } $ $k$ -dim subspaces in $\mathbf { R } ^ { 2 n } \}$ , called as Grassmann manifold.

If $A \in M ( 2 n , k )$ is non-singular, we define $\{ A \} = \{ a _ { 1 } , \cdot \cdot \cdot , a _ { k } \}$ to be a $k$ -dim subspace in $\mathbf { R } ^ { 2 n }$ generated by $k$ column vectors $a _ { 1 } , \cdots , a _ { k }$ of $A$ .

Proposition 3.16. Let $A , B \in M ( 2 n , k )$ be non-singular. $\{ A \} = \{ B \}$ , iff $\exists Q \in$ $G L ( k )$ , such that $A Q = B$ , i.e.,

$$
\left[ \begin{array} { l } { A _ { 1 } Q } \\ { A _ { 2 } Q } \end{array} \right] = \left[ \begin{array} { l } { B _ { 1 } } \\ { B _ { 2 } } \end{array} \right] .
$$

Definition 3.17. Let $A , B \in M ( 2 n , k )$ . If there is a matrix $Q \in G L ( k )$ , and $A Q =$ $B$ , then we say that $A$ is equivalent to $B$ , denoted by $A \sim B$ .

Proposition 3.18. $G _ { 2 n , k }$ consists of equivalent classes of non-singular elements under $M ( 2 n , k )$ i.e.,

G2n,k ≈ {equivalent classes of non-singular elements under “ $\sim$ ” in $M ( 2 n , k ) \}$

Definition 3.19. $\Lambda _ { n } = \left\{ \begin{array} { l l } { \begin{array} { r l r l } \end{array} } \end{array} \right.$ all Lagrangian subspaces in ${ \bf R } ^ { 2 n } \} \subset G _ { 2 n , n }$ .

Definition 3.20. $A \ = \ \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] \ \in \ M ( 2 n , n )$ is called a symmetric pair of square matrices, if

$$
A ^ { \prime } J A = O _ { n } ,
$$

$A _ { 1 } ^ { \prime } A _ { 2 } - A _ { 2 } ^ { \prime } A _ { 1 } = O _ { n }$ $J = \left[ { \begin{array} { c c } { 0 } & { I _ { n } } \\ { - I _ { n } } & { 0 } \end{array} } \right] .$

Evidently, $A = { \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] }$ is a symmetric pair iff $A _ { 1 } ^ { \prime } A _ { 2 } \in S M ( n )$ , or $A _ { 2 } ^ { \prime } A _ { 1 } \in S M ( n )$ .   
All symmetric pairs of square matrices are denoted by $S M _ { 2 n , n }$ .

In particular, $A = { \left[ \begin{array} { l } { S } \\ { I } \end{array} \right] } \ \mathrm { o r } \ { \left[ \begin{array} { l } { I } \\ { S } \end{array} \right] } \in S M _ { 2 n , n } , \operatorname { i f f } S \in S M ( n ) .$

$$
A = \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] , \ | A _ { 1 } | \neq 0 , \quad A \in S M _ { 2 n , n } \ \Longleftrightarrow \ A _ { 2 } A _ { 1 } ^ { - 1 } \in S M ( n ) .
$$

Definition 3.21. Let $A , B \in M ( 2 n , n ) .$ $A$ is conjugate to $B$ if $A ^ { \prime } J B = I _ { n } . \ A$ is conformally conjugate to $B$ if $\exists \mu = \mu ( A , B ) \neq 0$ , such that $A ^ { \prime } J B = \mu I _ { n }$ .

Obviously, $A$ is conjugate to $B$ iff $- B$ is conjugate to $A ; A$ is conformally conjugate to $B$ iff $B$ is conformally conjugate to $A$ with $\mu ( B , A ) = - \mu ( A , B )$ .

# 2.3.2 Symplectic Group

Let

$$
{ \begin{array} { r l } & { A = { \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] } = [ a _ { 1 } , \cdots , a _ { n } ] \in M ( 2 n , n ) , } \\ & { B = { \left[ \begin{array} { l } { B _ { 1 } } \\ { B _ { 2 } } \end{array} \right] } = [ b _ { 1 } , \cdots , b _ { n } ] \in M ( 2 n , n ) , } \\ & { M = [ A , B ] = { \left[ \begin{array} { l l } { A _ { 1 } } & { B _ { 1 } } \\ { A _ { 2 } } & { B _ { 2 } } \end{array} \right] } = [ a _ { 1 } , \cdots , a _ { n } , b _ { 1 } , \cdots , b _ { n } ] \in M ( 2 n ) , } \\ & { _ { 3 } , \ \cdots \ \alpha \ \cap \ \cdots \ . } \end{array} }
$$

$$
\begin{array} { r l } & { \Longleftrightarrow A ^ { \prime } J A = O _ { n } = B ^ { \prime } J B , A ^ { \prime } J B = I _ { n } } \\ & { \Longleftrightarrow A _ { 1 } ^ { \prime } A _ { 2 } - A _ { 2 } ^ { \prime } A _ { 1 } = O _ { n } = B _ { 1 } ^ { \prime } B _ { 2 } - B _ { 2 } ^ { \prime } B _ { 1 } , A _ { 1 } ^ { \prime } B _ { 2 } - A _ { 2 } ^ { \prime } B _ { 1 } = I _ { n } } \\ & { \Longleftrightarrow a _ { i } ^ { \prime } J a _ { j } = b _ { i } ^ { \prime } J b _ { j } = 0 , a _ { i } ^ { \prime } J b _ { j } = \delta _ { i j } , } \end{array}
$$

i.e., $a _ { 1 } , \cdots , a _ { n } , { \bar { b } } _ { 1 } , \cdots , { \bar { b } } _ { n }$ is a symplectic basis

$$
\begin{array} { r l } & { \Longleftrightarrow A ^ { \prime } J A = O _ { n } = B ^ { \prime } J B , \exists \neq 0 , \mathrm { s . t . } A ^ { \prime } J B = \mu I _ { n } } \\ & { \Longleftrightarrow A _ { 1 } ^ { \prime } A _ { 2 } - A _ { 2 } ^ { \prime } A _ { 1 } = O _ { n } = B _ { 1 } ^ { \prime } B _ { 2 } - B _ { 2 } ^ { \prime } B _ { 1 } , A _ { 1 } ^ { \prime } B _ { 2 } - A _ { 2 } ^ { \prime } B _ { 1 } } \\ & { \qquad = \mu I _ { n } , \mu \neq 0 } \\ & { \Longleftrightarrow M ^ { \prime } = \left[ \begin{array} { l } { A _ { 1 } ^ { \prime } } & { A _ { 2 } ^ { \prime } } \\ { B _ { 1 } ^ { \prime } } & { B _ { 2 } ^ { \prime } } \end{array} \right] \in C S p ( 2 n ) } \\ & { \Longleftrightarrow \left[ \begin{array} { l } { A _ { 1 } ^ { \prime } } \\ { B _ { 1 } ^ { \prime } } \end{array} \right] , \mathrm { ~ \boxed { ~ A _ 2 ^ { \prime } } ~ } \mathrm { ~ c o v s y m o c e t i c ~ p a i r ~ s a n d ~ a r c ~ c o n f o r m a ~ } } \\ & { \Longleftrightarrow A _ { 1 } B _ { 1 } ^ { \prime } - B _ { 1 } A _ { 1 } ^ { \prime } = O _ { n } = A _ { 2 } B _ { 2 } ^ { \prime } - B _ { 2 } A _ { 2 } ^ { \prime } ; A _ { 1 } B _ { 2 } ^ { \prime } - B _ { 1 } A _ { 2 } ^ { \prime } } \\ & { \qquad = \mu I _ { n } , \mu \neq 0 . } \end{array}
$$

Proposition 3.22. If $M ^ { \prime } J M = J$ , then $M J M ^ { \prime } = J$ . Generally speaking, if $K ^ { 2 } =$ $\pm I$ , then $M ^ { \prime } K M = K$ , iff $M K M ^ { \prime } = K$ .

Proof. If $M ^ { \prime } K M = K$ , then $K = M ^ { - 1 ^ { \prime } } K M ^ { - 1 }$ ,

$$
K ^ { - 1 } = ( M ^ { - 1 ^ { \prime } } K M ^ { - 1 } ) ^ { - 1 } = M K ^ { - 1 } M ^ { \prime } .
$$

By assumption, $K ^ { 2 } = \pm I$ , and so $K ^ { - 1 } = \pm K$ . Therefore, $M K M ^ { \prime } = K$

If $M \in S p ( 2 n )$ , then $A$ is a symmetric pair, iff $M A$ is a symmetric pair; and $A$ is conjugate to $B$ , iff $M A$ is conjugate to $M B$ .

If $M \in C S p ( 2 n )$ , then $A$ is a symmetric pair iff $M A$ is a symmetric pair; $A$ is conformally conjugate to $B$ iff $M A$ is conformally conjugate to $M B$ .

$$
{ \begin{array} { l l l } { M } & { = } & { [ A , B ] \in O _ { 2 n } \Longleftrightarrow M ^ { \prime } M = I _ { 2 n } } \\ & { \qquad \Longleftrightarrow A ^ { \prime } A = B ^ { \prime } B = I _ { n } , A ^ { \prime } B = O _ { n } . } \\ { M } & { = } & { [ A , B ] \in U _ { n } = S p ( 2 n ) \cap O _ { 2 n } } \\ & { = } & { G L ( n , C ) \cap S p ( 2 n ) = G L ( n , C ) \cap O _ { 2 n } } \\ & { \Longleftrightarrow A ^ { \prime } J A = B ^ { \prime } J B = O _ { n } , A ^ { \prime } B = O _ { n } , A ^ { \prime } J B = A ^ { \prime } A = B ^ { \prime } B = I _ { n } . } \\ & { \Longleftrightarrow A { \mathrm { i s ~ n o n - s i n o u l a r ~ s v m m e t r i c ~ p a i r } } . A ^ { \prime } A = I _ { n } B = J ^ { - 1 } A } \end{array} }
$$

Theorem 3.23. Let $M$ be non-singular. $M \in C S p ( 2 n )$ iff

$$
M Z \in S M _ { 2 n \times n } , \quad \forall Z \in S M _ { 2 n \times n } , \quad Z n o n { - } s i n g u l a r .
$$

Proof. We only need to prove the sufficiency. Let $M = [ A , B ] = \left[ \begin{array} { l l } { A _ { 1 } } & { B _ { 1 } } \\ { A _ { 2 } } & { B _ { 2 } } \end{array} \right] .$

$1 ^ { \circ } \quad \mathrm { T a k e } Z = { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } \in S M _ { 2 n \times n } , \ M Z = [ A , B ] { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } = A .$ $\boldsymbol { M } \boldsymbol { Z } \in S \boldsymbol { M } _ { 2 n \times n }$ $( M Z ) ^ { \prime } J M Z = A ^ { \prime } J A = O$

$2 ^ { \circ }$ Take $Z = { \left[ \begin{array} { l } { O } \\ { I } \end{array} \right] } \in S M _ { 2 n \times n }$ , similarly, $B ^ { \prime } J B = 0$

$3 ^ { \circ }$ Take $Z = { \left[ \begin{array} { l } { S } \\ { I } \end{array} \right] } , S ^ { \prime } = S .$ , and so $Z \in S M _ { 2 n \times n }$ By $( M Z ) ^ { \prime } J M \bar { Z } = 0$ , we have

$$
\begin{array} { l l l } { { ( A S + B ) ^ { \prime } J ( A S + B ) \ = } } & { { S ^ { \prime } A ^ { \prime } J A S + B ^ { \prime } J B + S ^ { \prime } A ^ { \prime } J B + B ^ { \prime } J A S } } \\ { { } } & { { } } \\ { { \ } } & { { = \ S ^ { \prime } A ^ { \prime } J B + B ^ { \prime } J A S = O . } } \end{array}
$$

Let $C = A ^ { \prime } J B$ . Then, $S ^ { \prime } C = C ^ { \prime } S$ , $\forall S ^ { \prime } = S$ . Take $S = I$ . Then, $C ^ { \prime } = C , C S =$ $_ { S C }$ , $\forall S ^ { \prime } = S$ . This shows that $C$ must be $\mu I$ , i.e., $A ^ { \prime } J B = \mu I$ .

The $\mu \neq 0$ follows from $| M | \ne 0$ . In fact, if $\mu = 0$ , then $A ^ { \prime } J B = O$ . Hence, $A ^ { \prime } J A = A ^ { \prime } J B = 0$ . Thus, $A ^ { \prime } J [ A , B ] = 0$ . This leads to $A ^ { \prime } = 0$ , and therefore, $A$ is also equal to 0. This is a contradiction. Therefore, $M \in C S p ( 2 n )$ . -

Remark 3.24. If $C S = S C , \forall S ^ { \prime } = S$ , then $C = \mu I$ .

# 2.3.3 Lagrangian Subspaces

Theorem 3.25. $\{ A \} \in \Lambda _ { n } \Leftrightarrow A$ is a non-singular symmetric pair. $M \in S p ( 2 n )$ or $C S p ( 2 n )$ implies that $\{ A \} \in \Lambda _ { n } ,$ , iff ${ \cal M } \{ A \} \in \Lambda _ { n }$ .

Examples of Lagrangian subspaces: Coordinate Lagrangian subspaces[Arn89,Wei77,AM78,HW63] :

Rν,0 = Rν,ν = IO ! , in which $\left[ \begin{array} { l } { I } \\ { O } \end{array} \right]$ is a non-singular symmetric pair;   
R0,ν = Rν,ν  = OI ! , in which $\left[ \begin{array} { l } { O } \\ { I } \end{array} \right]$ is a non-singular symmetric pair;   
$R _ { \nu , { \widehat { \nu } } } = \left\{ I _ { \alpha , { \widehat { \alpha } } } \right\} \quad { \mathrm { i n ~ w h i c h } } \quad I _ { \alpha , { \widehat { \alpha } } } = { \left[ \begin{array} { l } { I _ { \alpha } } \\ { I _ { \widehat { \alpha } } } \end{array} \right] }$ is a non-singular symmetric pair.

Proposition 3.26. We have the following results:

$1 ^ { \circ }$ Let $\{ A \}$ be $k$ -dim, $\{ B \}$ be $l$ -dim. Then, $\{ A \} \subset \{ B \} ^ { \top }$ , iff $A ^ { \prime } J B = O _ { k \times l }$ . $2 ^ { \circ }$ Let $A , B$ be non-singular. Then, $\{ A \} \cap \{ B \} = \{ 0 \}$ , iff $[ A , B ]$ is non-singular. $3 ^ { \circ }$ I $f \dim \{ A \} = \dim \{ B \} = n$ , then $\{ A \} \cap \{ B \} = \{ 0 \}$ , iff

$$
\operatorname* { d e t } \left[ A , B \right] \neq 0 .
$$

$4 ^ { \circ }$ $\{ A \}$ is isotropic of $k – \mathrm { d i m } \Leftrightarrow A ^ { \prime } J A = O _ { k }$

$5 ^ { \circ }$ $\{ A \}$ is Lagrangian $\Leftrightarrow A ^ { \prime } J A = O _ { n }$

$6 ^ { \circ }$ $k$ -dimensional subspaces $\{ A \}$ is non-degenerate iff $| A ^ { \prime } J A | \neq 0 , k = 2 s$ , iff ∃ $B$ , such that $\{ B \} = \{ A \} , B ^ { \prime } J B = J _ { 2 s }$ .

$7 ^ { \circ }$ $\{ A \}$ is degenerate $\Leftrightarrow | A ^ { \prime } J A | = 0$

Theorem 3.7 to Theorem 3.14 can be restated in matrix language as follows:

Theorem 3.27. If $A ^ { \prime } J A = O _ { k }$ , $A$ is non-singular. Then, there exists $B \in M ( 2 n , n -$ $k$ ), such that $[ A , B ]$ is a non-singular symmetric pair.

Theorem 3.28. If $A \in M ( 2 n , n )$ is a non-singular symmetric pair, then there exists a matrix, $B \in M ( 2 n , n )$ , such that $[ A , B ] \in S p ( 2 n )$ .

Theorem 3.29. If $A , C \ \in \ M ( 2 n , n )$ are two non-singular symmetric pairs and det $[ A , C ] \neq 0$ , then there exists uniquely a non-singular symmetric pair $B$ such that $B \sim C$ and $[ A , B ] \in S p ( 2 n )$ .

Theorem 3.30. Let $A \in M ( 2 n , k )$ , $B \in M ( 2 n , l )$ , $A ^ { \prime } J A = O _ { k }$ , $B ^ { \prime } J B = O _ { l }$ , and $[ A , B ]$ be non-singular. Then, there exist $C , D$ , such that $[ A , C ]$ , $[ B , D ]$ are nonsingular symmetric pairs and det $[ A , C , B , D ] \neq 0$ .

Theorem 3.31. If $A = \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right]$ is a non-singular symmetric pair, then $\exists \alpha \subset \nu$ , such that

$$
\vert I _ { \widehat { \alpha } } A _ { 1 } + I _ { \alpha } A _ { 2 } \vert \neq 0 .
$$

Theorem 3.32. For two mutually transversal Lagrangian subspaces $\{ A \} , \{ B \}$ , there always exists a third Lagrangian subspace $\{ C \}$ , transversal to $\{ A \}$ and $\{ B \}$ .

Proof. Take $\{ a _ { 1 } , a _ { 2 } , \cdot \cdot \cdot , a _ { n } \} = \{ A \} , \{ B \} = \{ b _ { 1 } , b _ { 2 } , \cdot \cdot \cdot , b _ { n } \}$ , such that

$$
A ^ { \prime } J A = O , \quad B ^ { \prime } J B = O , \quad A ^ { \prime } J B = I _ { n } , \quad B ^ { \prime } J A = - I _ { n } .
$$

Set $C = A + B$ . Then,

$$
{ \begin{array} { l r l } { ( A + B ) ^ { \prime } J ( A + B ) } & { = } & { ( A ^ { \prime } + B ^ { \prime } ) J ( A + B ) } \\ & { } & { } \\ & { = } & { A ^ { \prime } J A + A ^ { \prime } J B + B ^ { \prime } J A + B ^ { \prime } J B = O ; } \end{array} }
$$

and

$$
{ \begin{array} { r l } & { \operatorname* { d e t } \left[ A , A + B \right] = \operatorname* { d e t } \left[ A , B \right] \neq 0 , } \\ & { } \\ & { \operatorname* { d e t } \left[ B , A + B \right] = \operatorname* { d e t } \left[ A , B \right] \neq 0 . } \end{array} }
$$

The theorem is proved.

Theorem 3.33. For any two Lagrangian subspaces $\{ A \} , \{ B \}$ there exists another Lagrangian subspace $\{ C \}$ , transversal to $\{ A \}$ and $\{ B \}$ .

Proof. Assume $U ^ { 0 } = \{ A , B \} \neq 0 .$ . Take

$$
\begin{array} { r l } & { \{ a _ { 1 } , \cdots , a _ { k } \} = \{ \overline { { A } } \} \subset \{ A \} , } \\ & { \{ \bar { b } _ { 1 } , \cdots , \bar { b } _ { k } \} = \{ \overline { { B } } \} \subset \{ B \} , \quad \{ c _ { 1 } , \cdots , c _ { n - k } \} = U ^ { 0 } , } \end{array}
$$

such that

$$
\begin{array} { l } { { \{ a _ { 1 } , \cdots , a _ { k } , c _ { 1 } , \cdots , c _ { n - k } \} = \{ A \} , } } \\ { { \ } } \\ { { \{ \bar { b } _ { 1 } , \cdots , \bar { b } _ { k } , c _ { 1 } , \cdots , c _ { n - k } \} = \{ B \} , } } \\ { { \ } } \\ { { \ } } \\ { { \left[ a _ { i } , a _ { j } \right] = 0 = [ \bar { b } _ { i } , \bar { b } _ { j } ] , } } \\ { { \ } } \\ { { \left[ a _ { i } , \bar { b } _ { j } \right] = \delta _ { i j } , \quad i , j = 1 , \cdots , k . } } \end{array}
$$

Set $C = \{ a _ { 1 } + \bar { b } _ { 1 } , \cdot \cdot \cdot , a _ { k } + \bar { b } _ { k } , d _ { 1 } , \cdot \cdot \cdot , d _ { n - k } \}$ , where

$$
\begin{array} { l } { { [ d _ { i } , d _ { j } ] = 0 , \quad [ d _ { i } , c _ { j } ] = \delta _ { i j } , } } \\ { { { } } } \\ { { { [ d _ { i } , a _ { j } ] = [ d _ { i } , \bar { b } _ { j } ] = 0 . } } } \end{array}
$$

Then, $\{ C \}$ is what we want to find out.

# 2.3.4 Special Types of $S p ( 2 n )$

Set $M = [ A , B ] = \left[ \begin{array} { c c } { A _ { 1 } } & { B _ { 1 } } \\ { A _ { 2 } } & { B _ { 2 } } \end{array} \right] \in S p ( 2 n )$ . The following are special types of $S p ( 2 n )$ .

$$
\begin{array} { c l } { { } } & { { M \in S p ( 2 n ) \cap O _ { 2 n } = U _ { n } } } \\ { { } } & { { { } } } \\ { { } } & { { \Longrightarrow M = [ A , J ^ { - 1 } A ] , \ A ^ { \prime } J A = O _ { n } , \ A ^ { \prime } A = I _ { n } . } } \end{array}
$$

$S p ( 2 n ) \ni M = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { B _ { 1 } } \end{array} \right] ,$ , which are diagonal blocks

$$
\Longrightarrow M = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { A _ { 1 } ^ { - 1 ^ { \prime } } } \end{array} \right] , A _ { 1 } \in G L ( n , { \bf R } ) .
$$

$$
S p ( 2 n ) \ni M = \left[ \begin{array} { c c } { { I } } & { { B _ { 1 } } } \\ { { O } } & { { B _ { 2 } } } \end{array} \right] \Longrightarrow M = \left[ \begin{array} { c c } { { I } } & { { S } } \\ { { O } } & { { I } } \end{array} \right] , S ^ { \prime } = S .
$$

$$
S p ( 2 n ) \ni M = \left[ \begin{array} { c c } { A _ { 1 } } & { O } \\ { A _ { 2 } } & { I } \end{array} \right] \Longrightarrow M = \left[ \begin{array} { c c } { I } & { O } \\ { S } & { I } \end{array} \right] , S ^ { \prime } = S .
$$

(III) Sp(2n) 
 M = Jα = Iα Iα−Iα Iα ! , α ⊂ ν, and symplectic substitution

# 1. Several special types

(1) $S p _ { 2 n } ( 0 )$ .

$$
S p _ { 2 n } ( 0 ) = S p _ { 2 n } \cap O _ { 2 n } = U _ { n } .
$$

Theorem 3.34. $M = \left[ A , B \right] \in S p _ { 2 n } ( 0 ) = U _ { n } \Leftrightarrow B = J ^ { - 1 } A , \ A ^ { \prime } A = I , \ A ^ { \prime } J A$   
$= O$ .

Proof. Evidently, if $A ^ { \prime } A = I$ , $A ^ { \prime } J A = O$ . Then, $[ A , J ^ { - 1 } A ] \in S p _ { 2 n } ( 0 )$ . Conversely,

$$
\begin{array}{c} \begin{array} { r l } & { M = [ A , B ] \in S p _ { 2 n } \Longrightarrow { A ^ { \prime } J A } = O , { A ^ { \prime } J B } = I . } \\ & { M = [ A , B ] \in O _ { 2 n } \Longrightarrow { A ^ { \prime } B } = O , { B ^ { \prime } B } = I . } \\ & { { A ^ { \prime } J A } = O } \\ & { { A ^ { \prime } B } = O } \end{array} \} \Longrightarrow { A ^ { \prime } ( J A + B ) } = O \quad  \\ & { { B ^ { \prime } J A } = - I } \\ & { B ^ { \prime } B = I \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \Longrightarrow { M ^ { \prime } ( J A + B ) } = O \Longrightarrow { J A } + B = O \Longrightarrow { B } = { J ^ { - 1 } A } . } \end{array}
$$

The theorem is proved.

Lemma 3.35. There exist polynomials $\varphi _ { n } ( A ) = \varphi _ { n } ( a _ { j k } ) , \psi _ { n } ( A ) = \psi _ { n } ( a _ { j k } )$ in $2 n \times$ $n$ variables $a _ { 1 1 } , \cdots , a _ { 2 n , n }$ with integer coefficients such that

$$
\operatorname* { d e t } \left[ A J ^ { \prime } A \right] = \operatorname* { d e t } { \left[ \begin{array} { l l } { A _ { 1 } } & { - A _ { 2 } } \\ { A _ { 2 } } & { A _ { 1 } } \end{array} \right] } = ( \varphi _ { n } ( A ) ) ^ { 2 } + ( \psi _ { n } ( A ) ) ^ { 2 } \geq 0 ,
$$

where

$$
A = \left[ \begin{array} { c c c } { a _ { 1 1 } } & { \cdot \cdot \cdot } & { a _ { 1 n } } \\ { \vdots } & { } & { \vdots } \\ { a _ { 2 n , 1 } } & { \cdot \cdot \cdot } & { a _ { 2 n , n } } \end{array} \right] .
$$

Proof.

$$
{ \begin{array} { r l } { { | \begin{array} { l l } { A _ { 1 } } & { - A _ { 2 } } \\ { A _ { 2 } } & { A _ { 1 } } \end{array} | } } & { = { | \begin{array} { l l } { A _ { 1 } + \mathrm { i } A _ { 2 } } & { - A _ { 2 } + \mathrm { i } A _ { 1 } } \\ { A _ { 2 } } & { A _ { 1 } } \end{array} | } } \\ & { \qquad = { | \begin{array} { l l } { A _ { 1 } + \mathrm { i } A _ { 2 } } & { - A _ { 2 } + \mathrm { i } A _ { 1 } - \mathrm { i } ( A _ { 1 } + \mathrm { i } A _ { 2 } ) } \\ { A _ { 2 } } & { A _ { 1 } - \mathrm { i } A _ { 2 } } \end{array} | } } \\ & { \qquad = { | \begin{array} { l l } { A _ { 1 } + \mathrm { i } A _ { 2 } } & { O } \\ { A _ { 2 } } & { A _ { 1 } - \mathrm { i } A _ { 2 } } \end{array} | } } \\ & { \qquad = ( A _ { 1 } + \mathrm { i } A _ { 2 } ) ( A _ { 1 } - \mathrm { i } A _ { 2 } ) } \\ & { \qquad = ( A _ { 1 } + \mathrm { i } A _ { 2 } ) ( { \overline { { A _ { 1 } + \mathrm { i } A _ { 2 } } } } ) } \\ & { \qquad = ( A _ { 1 } + \mathrm { i } A _ { 2 } ) ( { \overline { { A _ { 1 } + \mathrm { i } A _ { 2 } } } } ) } \\ & { \qquad = ( \mathrm { R e } | A _ { 1 } + \mathrm { i } A _ { 2 } ) { \mathrm { 2 } } + ( \mathrm { I m } | A _ { 1 } + \mathrm { i } A _ { 2 } | ) ^ { 2 } } \\ & { \qquad = ( \psi _ { n } ( A ) ) ^ { 2 } + ( \psi _ { n } ( A ) ) ^ { 2 } \geq 0 . } \end{array} }
$$

Therefore, the lemma is completed.

Theorem 3.36. $M \in S p _ { 2 n } ( 0 ) = U _ { n } \Rightarrow | M | = 1 .$ .

Proof. We will prove that

$$
\left. { \begin{array} { l } { M ^ { \prime } M = I \Longrightarrow | M | ^ { 2 } = 1 \Longrightarrow | M | = \pm 1 } \\ { { \mathrm { ~ \bf ~ B y ~ L e m m a ~ } } 3 . 3 5 , ~ M = [ A , J ^ { - 1 } A ] \Longrightarrow | M | \geq 0 } \end{array} } \right\} \Longrightarrow | M | = 1 .
$$

The proof can be obtained.

(2) $S p _ { 2 n }$ (I).

$M = \left[ { \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { B _ { 1 } } \end{array} } \right] , \ \mathrm { i n ~ w h i c h ~ d i a g o n a l ~ b l o c k s } \in G L ( n , \mathbf { R } ) ,$   
$M = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { A _ { 1 } ^ { - 1 ^ { \prime } } } \end{array} \right] , A _ { 1 } \in G L ( n , \mathbf { R } ) , | M | = | A _ { 1 } | | A _ { 1 } ^ { \prime } | ^ { - 1 } = 1 ,$   
${ \cal A } _ { 1 } \in G L ( n , { \bf R } ) \Longrightarrow { \cal A } _ { 1 } = T P , ~ T ^ { \prime } T = I _ { n } , ~ P ^ { \prime } = P > 0 ( \mathrm { p o s i t i v e ~ d e f i n i t } $ e),   
${ \bf R } ^ { 2 n } \ni \left[ \begin{array} { c } { { p } } \\ { { q } } \end{array} \right] \longrightarrow M \left[ \begin{array} { c } { { p } } \\ { { q } } \end{array} \right] = \left[ \begin{array} { c } { { A _ { 1 } p } } \\ { { ( A _ { 1 } ^ { - 1 } ) ^ { \prime } q } } \end{array} \right] \in { \bf R } ^ { 2 n } ,$   
$\begin{array} { r l } & { \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { A _ { 1 } ^ { - 1 ^ { \prime } } } \end{array} \right] = \left[ \begin{array} { l l } { T } & { O } \\ { O } & { T } \end{array} \right] \left[ \begin{array} { l l } { P } & { O } \\ { O } & { P ^ { - 1 } } \end{array} \right] , } \\ & { \left[ \begin{array} { l l } { T } & { O } \\ { O } & { T } \end{array} \right] \in O _ { n } \subset U _ { n } , } \end{array}$

where

$$
O _ { n } = \left\{ \left[ \begin{array} { c c } { { T } } & { { O } } \\ { { O } } & { { T } } \end{array} \right] , T ^ { \prime } T = I _ { n } \right\} = U _ { n } \cap G L ( n , { \bf R } ) = S p _ { 2 n } ( 0 ) \cap S p _ { 2 n } ( { \mathrm { I } } ) ,
$$

$$
\left\{ \left[ \begin{array} { l l } { P } & { O } \\ { O } & { P ^ { - 1 } } \end{array} \right] , P ^ { \prime } = P > 0 \right\} \cap S p _ { 2 n } ( 0 ) = \{ I _ { 2 n } \} .
$$

(3) Sp2n(II).

$$
\begin{array} { r l } & { S p _ { 2 n } ( \mathrm { I I } ) = \left\{ \left[ \begin{array} { l l } { I } & { S } \\ { O } & { I } \end{array} \right] , S ^ { \prime } = S \right\} } \\ & { \qquad \simeq S p _ { 2 n } ( \mathrm { I I } ^ { \prime } ) = \left\{ \left[ \begin{array} { l l } { I } & { O } \\ { S } & { I } \end{array} \right] , S ^ { \prime } = S \right\} , } \end{array}
$$

(4)

$$
\begin{array} { r l } & { S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } ) . } \\ & { S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } ) } \\ & { \quad = \left\{ \left[ \begin{array} { l l } { Q } & { Q S } \\ { O } & { Q ^ { \prime - 1 } } \end{array} \right] = \left[ \begin{array} { l l } { Q } & { O } \\ { O } & { Q ^ { \prime - 1 } } \end{array} \right] \left[ \begin{array} { l l } { I } & { S } \\ { O } & { I } \end{array} \right] , Q \in G L ( n , \mathbf { R } ) , S ^ { \prime } = S \right\} . } \\ & { M \in S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } ) \Longrightarrow | M | = 1 . } \\ & { S p _ { 2 n } ( \mathrm { I I } ) \cap S p _ { 2 n } ( 0 ) = S p _ { 2 n } ( \mathrm { I I } ^ { \prime } ) \cap S p _ { 2 n } ( 0 ) = \{ I \} . } \end{array}
$$

(5) Sp2n(III).

$$
J _ { \alpha } = \left[ \begin{array} { l l } { I _ { \widehat { \alpha } } } & { I _ { \alpha } } \\ { - I _ { \alpha } } & { I _ { \widehat { \alpha } } } \end{array} \right] , \quad J _ { \alpha } ^ { \prime } = J _ { \alpha } ^ { - 1 } = \left[ \begin{array} { l l } { I _ { \widehat { \alpha } } } & { - I _ { \alpha } } \\ { I _ { \alpha } } & { I _ { \widehat { \alpha } } } \end{array} \right] , \quad \alpha \subset \nu .
$$

In particular, $J _ { \nu } = J _ { 2 n } , \ J _ { 0 } = I _ { 2 n } , \ | J _ { \alpha } | = 1 $ . {Symplectic Substitution $\}$ is not a group. Total number of $J _ { \alpha } = 2 ^ { n }$ , total number of $\{ J _ { \alpha } , J _ { \alpha } ^ { \prime } \} = 2 ^ { n + 1 } - 1$ , and

$$
\left[ \begin{array} { l l } { I } & { O } \\ { - S } & { I } \end{array} \right] = J _ { 2 n } ^ { \prime } \left[ \begin{array} { l l } { I } & { S } \\ { O } & { I } \end{array} \right] J _ { 2 n } ,
$$

which is the bijection from $S p _ { 2 n } ( \mathrm { I I } )$ to $S p _ { 2 n } ( \mathrm { I I } ^ { \prime } )$ .

# 2. Some theorems about $S p ( 2 n )$

Theorem 3.37. If $\{ A \} , \{ B \} \in \Lambda _ { n }$ , then there exists $M \in S p ( 2 n )$ , such that $M A =$ $B$ . Moreover, $M \{ A \} = \{ B \}$ .

Proof. By Theorem 3.28, there exist $C , D \in M _ { 2 n , n }$ , such that

$$
[ A , C ] = M _ { A } \in S p ( 2 n ) , \quad [ B , D ] = M _ { B } \in S p ( 2 n ) .
$$

Set $M = M _ { B } M _ { A } ^ { - 1 }$ . Then, $M M _ { A } = M _ { B }$ , i.e., $M [ A , C ] = [ B , D ]$ . Therefore, $M A$ $= B$ .

Theorem 3.38. If $\{ A \} , \{ B \} \in \Lambda _ { n }$ , then there exists

$$
M \in S p _ { 2 n } ( 0 ) = U _ { n } = S p _ { 2 n } \cap O _ { 2 n } ,
$$

such that

$$
M \{ A \} = \{ B \} .
$$

Proof. From the procedure of Grass-Schmidt’s orthogonal normalization, we can get two matrices $C$ and $D$ of order $2 n \times n$ i.e., $C , D \in M ( 2 n , n )$ , such that

$$
\begin{array} { l l } { { \{ C \} = \{ A \} , } } & { { C ^ { \prime } J C = O , ~ C ^ { \prime } C = I . } } \\ { { \ } } & { { } } \\ { { \{ D \} = \{ B \} , } } & { { D ^ { \prime } J D = O , ~ D ^ { \prime } D = I . } } \end{array}
$$

Set $M _ { C } = [ C , J ^ { - 1 } C ] , M _ { D } = [ D , J ^ { \prime } D ]$ . Obviously,

$$
\begin{array} { r } { M _ { C } , M _ { D } \in S p _ { 2 n } ( 0 ) = U _ { n } . } \end{array}
$$

Set $M = M _ { D } M _ { C } ^ { - 1 }$ . Then, $M M _ { C } = M _ { D }$ , i.e.,

$$
M [ C , J ^ { - 1 } C ] = [ D , J ^ { \prime } D ] .
$$

Thus, $M C = D$ .

We obtain $M \{ C \} = \{ M C \} = \{ D \}$ , i.e., $M \{ A \} = \{ B \}$ .

Theorem 3.39. Let $G = C S p ( 2 n )$ , $S p ( 2 n )$ , or $S p _ { 2 n } ( 0 ) = U _ { n }$ . Then, the following action of $G$ on $\Lambda _ { n } : M \{ A \} = \{ M A \} ( A \in \Lambda _ { n }$ , $M \in G ,$ is

$1 ^ { \circ }$ Transitiv ${ \mathrm { ~ , ~ } } i . e . , \forall \{ A \} , \{ B \} \in \Lambda _ { n } , \exists M \in G ,$ , such that $M \{ A \} = \{ B \}$ . $2 ^ { \circ }$ If for any $\{ A \} \in \Lambda _ { n } , M \{ A \} = \{ A \}$ then $M = \pm I _ { 2 n }$ when $G = S p ( 2 n )$ or $S p _ { 2 n } ( 0 )$ ; and $M = \mu I _ { 2 n }$ when $G = C S p ( 2 n )$ .

Proof. $1 ^ { \circ }$ can be obtained by Theorem 3.37 and Theorem 3.38.

$\begin{array} { r } { \mathrm { 2 ^ { \circ } ~ } \mathrm { ~ A s s u m e ~ } M = \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] \cdot \mathrm { ~ T a k i n g ~ } \{ A \} = \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} , \left\{ \begin{array} { l } { O } \\ { I } \end{array} \right\} \in \Lambda _ { n } , 1 \mathrm { ~ a ~ n ~ } \Omega \times \left[ \begin{array} { l } { 0 } \\ { O } \end{array} \right] . } \end{array}$ respec-

$$
M \left\{ \begin{array} { c } { I } \\ { O } \end{array} \right\} = \left\{ \begin{array} { c } { I } \\ { O } \end{array} \right\} \quad \mathrm { a n d } \quad M \left\{ \begin{array} { c } { O } \\ { I } \end{array} \right\} = \left\{ \begin{array} { c } { O } \\ { I } \end{array} \right\} ,
$$

i.e., for some $Q \in G L ( n )$ ,

$$
\left[ \begin{array} { c c } { A } & { B } \\ { C } & { D } \end{array} \right] \left[ \begin{array} { c } { I } \\ { O } \end{array} \right] = \left[ \begin{array} { c } { A } \\ { C } \end{array} \right] = \left[ \begin{array} { c } { I } \\ { O } \end{array} \right] Q = \left[ \begin{array} { c } { Q } \\ { O } \end{array} \right] ,
$$

$$
{ \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } { \left[ \begin{array} { l } { O } \\ { I } \end{array} \right] } = { \left[ \begin{array} { l } { B } \\ { D } \end{array} \right] } = { \left[ \begin{array} { l } { O } \\ { I } \end{array} \right] } Q = { \left[ \begin{array} { l } { O } \\ { Q } \end{array} \right] } ,
$$

and so $B = C = O$ . Again, take $\{ A \} = \left\{ { \begin{array} { l } { I } \\ { P } \end{array} } \right\} , P ^ { \prime } = P .$ . Then, from the equality

$$
M \left\{ \begin{array} { l } { { I } } \\ { { P } } \end{array} \right\} = \left\{ \begin{array} { l } { { I } } \\ { { P } } \end{array} \right\} ,
$$

it follows that

$$
{ \left[ \begin{array} { l l } { A } & { O } \\ { O } & { D } \end{array} \right] } { \left[ \begin{array} { l } { I } \\ { P } \end{array} \right] } = { \left[ \begin{array} { l } { A } \\ { D P } \end{array} \right] } = { \left[ \begin{array} { l } { I } \\ { P } \end{array} \right] } Q = { \left[ \begin{array} { l } { Q } \\ { P Q } \end{array} \right] } ,
$$

for some $Q \in G L ( n )$ and $\forall P ^ { \prime } = P$ , i.e., $A = Q$ , and $D P = P Q = P A$ . Set $P = I , D = A$ . Then, we get

$$
A P = P A , \quad \forall P ^ { \prime } = P .
$$

This implies that $A = \mu I ( \mu \neq 0 )$ (since $| M | \ne 0 \}$ . Besides, if $M \in S p ( 2 n )$ or $S p _ { 2 n } ( 0 )$ then $\mu ^ { 2 } I = I$ , i.e., $\mu ^ { 2 } = 1$ . Therefore, we have $M = \pm I$ . -

Theorem 3.40. $\Lambda _ { n } \simeq U _ { n } / O _ { n } = S p _ { 2 n } ( 0 ) / S p _ { 2 n } ( 0 ) \cap S p _ { 2 n } ( \mathrm { I } ) ,$ or

$$
\varphi : U _ { n } / O _ { n } \longrightarrow \Lambda _ { n } , \quad \varphi ( M O _ { n } ) = M \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] , \quad M \in U _ { n } ,
$$

is a bijection from $U _ { n } / O _ { n }$ to $\Lambda _ { n }$ .

Proof. First, $\varphi$ is well-defined. In fact, if $M _ { 1 } O _ { n } = M _ { 2 } O _ { n }$ , or $M _ { 1 } \in M _ { 2 } O _ { n }$ , then $M _ { 1 } = M _ { 2 } \left[ \begin{array} { l l } { T } & { O } \\ { O } & { T } \end{array} \right] .$

$$
\begin{array} { l } { { \mathrm { o m e ~ T ^ { * } = T , } M _ { 1 } \left\{ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right\} \ = \ M _ { 2 } \left[ \begin{array} { c c } { { T } } & { { O } } \\ { { O } } & { { T } } \end{array} \right] \left[ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right] Q = M _ { 2 } \left[ \begin{array} { c } { { T } } \\ { { O } } \end{array} \right] Q } } \\ { { \ = \ M _ { 2 } \left[ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right] T Q = M _ { 2 } \left\{ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right\} . } } \end{array}
$$

It follows from the Theorem 3.38 that $\varphi$ is surjective. We will prove that $\varphi$ is injective.

$$
\mathrm { I f } ~ M _ { 1 } \left\{ \begin{array} { c } { I } \\ { O } \end{array} \right\} = M _ { 2 } \left\{ \begin{array} { c } { I } \\ { O } \end{array} \right\} , \mathrm { t h e n } ~ M _ { 2 } ^ { - 1 } M _ { 1 } \left\{ \begin{array} { c } { I } \\ { O } \end{array} \right\} = \left\{ \begin{array} { c } { I } \\ { O } \end{array} \right\} .
$$

$$
M = M _ { 2 } ^ { - 1 } M _ { 1 } = { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } \in S p _ { 2 n } ( 0 ) . \operatorname { T h e n } , M { \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} } = { \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} } ,
$$

$$
{ \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } = { \left[ \begin{array} { l } { A } \\ { C } \end{array} \right] } = { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } Q .
$$

Thus, $C = O$ .

$\left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] \in S p _ { 2 n } ( 0 )$ , by Theorem 3.34:

$$
{ \left[ \begin{array} { l } { B } \\ { D } \end{array} \right] } = J ^ { - 1 } { \left[ \begin{array} { l } { A } \\ { O } \end{array} \right] } = { \left[ \begin{array} { l l } { O } & { - I } \\ { I } & { O } \end{array} \right] } { \left[ \begin{array} { l } { A } \\ { O } \end{array} \right] } = { \left[ \begin{array} { l } { O } \\ { A } \end{array} \right] }
$$

and

$$
[ A ^ { \prime } , O ] \left[ \begin{array} { l } { A } \\ { O } \end{array} \right] = A ^ { \prime } A = I .
$$

This means that $M = \left[ \begin{array} { c c } { { A } } & { { O } } \\ { { O } } & { { A } } \end{array} \right] , A ^ { \prime } A = I \in O _ { n } .$

Theorem 3.41. $\Lambda _ { n } \simeq S p ( 2 n ) / S p _ { 2 n } ( \mathrm { I , I I } )$ , or the mapping

$$
\varphi : S p ( 2 n ) / S p _ { 2 n } ( \mathrm { I , I I } ) \longrightarrow \Lambda _ { n } , \quad \varphi ( M S p _ { 2 n } ( \mathrm { I I } ) ) = M \left[ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right] , M \in S p
$$

is a bijection.

Proof. If $M _ { 1 } S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } ) = M _ { 2 } S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } )$ , then $M _ { 1 } \in M _ { 2 } S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } )$ , i.e.,

$$
M _ { 1 } = M _ { 2 } \left[ { \begin{array} { l l } { Q } & { Q S } \\ { O } & { Q ^ { - 1 ^ { \prime } } } \end{array} } \right] \quad { \mathrm { f o r ~ s o m e ~ } } Q \in G L { \mathrm { ~ a n d ~ } } S \in S M ( n ) .
$$

Thus,

$$
\begin{array} { r c l } { { { \cal M } _ { 1 } \left\{ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right\} } } & { { = } } & { { { \cal M } _ { 2 } \left[ \begin{array} { c c } { { Q } } & { { Q S } } \\ { { O } } & { { Q ^ { - 1 } } ^ { \prime } } \end{array} \right] \left[ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right] P = { \cal M } _ { 2 } \left[ \begin{array} { c } { { Q } } \\ { { O } } \end{array} \right] P } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { { \cal M } _ { 2 } \left[ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right] Q P = { \cal M } _ { 2 } \left\{ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right\} . } } \end{array}
$$

This implies that $\varphi$ is well-defined.

By Theorem 3.37, we know that $\varphi$ is surjective.

Last, $\varphi$ is injective too. As a matter of fact, if $M _ { 1 } \left\{ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right\} = M _ { 2 } \left\{ \begin{array} { c } { { I } } \\ { { O } } \end{array} \right\}$ , then $M _ { 2 } ^ { - 1 } M _ { 1 } { \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} } = { \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} } .$

$$
M = M _ { 2 } ^ { - 1 } M _ { 1 } = { \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } ; \operatorname { t h e n } M { \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} } = { \left\{ \begin{array} { l } { I } \\ { O } \end{array} \right\} } ,
$$

$$
{ \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } = { \left[ \begin{array} { l } { A } \\ { C } \end{array} \right] } = { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } P = { \left[ \begin{array} { l } { P } \\ { O } \end{array} \right] } , { \mathrm { f o r ~ s o m e ~ } } P \in G L ( n ) .
$$

Thus, $C = O$ .

$$
\begin{array} { r } { M = \left[ \begin{array} { c c } { A } & { B } \\ { C } & { D } \end{array} \right] = \left[ \begin{array} { c c } { A } & { O } \\ { O } & { A ^ { - 1 ^ { \prime } } } \end{array} \right] \left[ \begin{array} { c c } { I } & { B _ { 1 } } \\ { O } & { D _ { 1 } } \end{array} \right] \in S p ( 2 n ) , } \end{array}
$$

where $B _ { 1 } = A ^ { - 1 } B , D _ { 1 } = A ^ { \prime } D$ . Since $M \in S p ( 2 n )$ and $\left[ \begin{array} { c c } { { A } } & { { O } } \\ { { O } } & { { { A ^ { \prime } } ^ { - 1 } } } \end{array} \right] \in S p ( 2 n ) ,$ $\left[ \begin{array} { l l } { I } & { B _ { 1 } } \\ { O } & { D _ { 1 } } \end{array} \right]$ must be symplectic too.

By definition, $\left[ \begin{array} { c c } { { I } } & { { B _ { 1 } } } \\ { { O } } & { { D _ { 1 } } } \end{array} \right] \in S p _ { 2 n } ( \mathrm { I I } )$ . Therefore, $M \in S p _ { 2 n } ( \mathrm { I } , \mathrm { I I } )$

# 2.3.5 Generators of $S p ( 2 n )$

Theorem 3.42. Every symplectic matrix $M$ can be decomposed as the multiplication of three kinds of special symplectic matrices

$$
M = M _ { 0 } M _ { 1 } M _ { 2 } ,
$$

where

$$
M _ { 0 } \in S p _ { 2 n } ( 0 ) , \quad M _ { 1 } \in S p _ { 2 n } ( \mathrm { I } ) , \quad M _ { 2 } \in S p _ { 2 n } ( \mathrm { I I } ) .
$$

Proof. Let $M = [ A , B ] \in S p _ { 2 n }$ ; then $\{ A \} \in \Lambda _ { n }$ . By Theorem 3.38, there exists $M _ { 0 } \in S p _ { 2 n } ( 0 ) = U _ { n }$ , such that

$$
\begin{array} { r l r } { A } & { = } & { M _ { 0 } \left[ \begin{array} { c } { I } \\ { O } \end{array} \right] Q = M _ { 0 } \left[ \begin{array} { c } { Q } \\ { O } \end{array} \right] } \\ & { = } & { M _ { 0 } \left[ \begin{array} { c c } { Q } & { O } \\ { O } & { Q ^ { \prime } { } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { c } { I } \\ { O } \end{array} \right] . } \end{array}
$$

Let

$$
\boldsymbol { B } _ { 1 } = \left[ \begin{array} { l l } { \boldsymbol { Q } } & { \boldsymbol { O } } \\ { \boldsymbol { O } } & { \boldsymbol { Q ^ { \prime } } ^ { - 1 } } \end{array} \right] ^ { - 1 } \boldsymbol { M } _ { 0 } ^ { - 1 } \boldsymbol { B } ,
$$

i.e.,

$$
B = M _ { 0 } \left[ \begin{array} { l l } { { Q } } & { { O } } \\ { { O } } & { { { Q ^ { \prime } } ^ { - 1 } } } \end{array} \right] \left[ \begin{array} { l } { { C _ { 1 } } } \\ { { C _ { 2 } } } \end{array} \right] .
$$

Thus,

$$
\begin{array} { r l } & { M = [ A , B ] } \\ & { \quad = \left[ M _ { 0 } \left[ \begin{array} { l l } { Q } & { O } \\ { O } & { Q ^ { \prime - 1 } } \end{array} \right] \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] , M _ { 0 } \left[ \begin{array} { l l } { Q } & { O } \\ { O } & { Q ^ { \prime - 1 } } \end{array} \right] \left[ \begin{array} { l } { C _ { 1 } } \\ { C _ { 2 } } \end{array} \right] \right] } \\ & { \quad = M _ { 0 } \left[ \begin{array} { l l } { Q } & { O } \\ { O } & { Q ^ { \prime - 1 } } \end{array} \right] \left[ \begin{array} { l l } { I } & { C _ { 1 } } \\ { O } & { C _ { 2 } } \end{array} \right] \in S p ( 2 n ) } \\ & { \quad = M _ { 0 } M _ { 1 } M _ { 2 } , } \end{array}
$$

$$
\begin{array} { r } { M _ { 1 } = \left[ \begin{array} { l l } { Q } & { O } \\ { O } & { { Q ^ { \prime } } ^ { - 1 } } \end{array} \right] \in S p _ { 2 n } ( \mathrm { I } ) , \quad M _ { 2 } = \left[ \begin{array} { l l } { I } & { C _ { 1 } } \\ { O } & { C _ { 2 } } \end{array} \right] \in S p _ { 2 n } ( \mathrm { I I } ) . } \end{array}
$$

Proposition 3.43. $| M | = 1$ , $\forall M \in S p ( 2 n )$ .

Theorem 3.44. The following decomposition of a symplectic matrix $M \in S p ( 2 n )$ is unique.

$$
\begin{array} { c } { { M = M _ { 0 } M _ { 1 } M _ { 2 } , } } \\ { { { } } } \\ { { M _ { 0 } \in S p _ { 2 n } ( 0 ) , M _ { 1 } = \left[ \begin{array} { l l } { { P } } & { { O } } \\ { { O } } & { { P ^ { - 1 } } } \end{array} \right] , P ^ { \prime } = P > 0 , M _ { 2 } \in S p _ { 2 n } ( \mathrm { I I } ) . } } \end{array}
$$

Proof. A non-singular matrix $Q \in G L ( n )$ can be uniquely decomposed as a multiplication of an orthogonal matrix $T$ and a positive definite matrix $P : Q = T P$ . By Theorem 3.42, we have a decomposition

$$
\begin{array} { r c l } { { { \cal M } ~ = ~ { \overline { { { \cal M } } } } _ { 0 } { \overline { { { \cal M } } } } _ { 1 } { \overline { { { \cal M } } } } _ { 2 } = { \overline { { { \cal M } } } } _ { 0 } \left[ \begin{array} { l l } { { Q } } & { { { \cal O } } } \\ { { { \cal O } } } & { { { Q ^ { \prime } } ^ { - 1 } } } \end{array} \right] { \overline { { { \cal M } } } } _ { 2 } } } \\ { { ~ } } & { { ~ } } \\ { { ~ = ~ { \overline { { { \cal M } } } } _ { 0 } \left[ \begin{array} { l l } { { T } } & { { { \cal O } } } \\ { { { \cal O } } } & { { T } } \end{array} \right] \left[ \begin{array} { l l } { { { \cal P } } } & { { { \cal O } } } \\ { { { \cal O } } } & { { { \cal P } ^ { - 1 } } } \end{array} \right] { \overline { { { \cal M } } } } _ { 2 } } } \\ { { ~ } } & { { ~ } } \\ { { ~ } } & { { ~ = ~ { \cal M } _ { 0 } { \cal M } _ { 1 } { \cal M } _ { 2 } , } } \end{array}
$$

where

$$
\begin{array} { l } { { { \cal M } _ { 0 } = \overline { { { \cal M } } } _ { 0 } \left[ \begin{array} { l l } { { { \cal T } } } & { { { \cal O } } } \\ { { { \cal O } } } & { { { \cal T } } } \end{array} \right] \in S p _ { 2 n } ( 0 ) , \quad { \cal M } _ { 2 } = \overline { { { \cal M } } } _ { 2 } \in S p _ { 2 n } ( \mathrm { I I } ) , } } \\ { { { \cal M } _ { 1 } = \left[ \begin{array} { l l } { { { \cal P } } } & { { { \cal O } } } \\ { { { \cal O } } } & { { { \cal P } ^ { - 1 } } } \end{array} \right] , \quad { \cal P } ^ { \prime } = { \cal P } > 0 . } } \end{array}
$$

We need to prove that such a decomposition is unique.

Suppose $M = M _ { 0 1 } M _ { 1 1 } M _ { 2 1 }$ is another decomposition, where

$$
M _ { 1 1 } = \left[ \begin{array} { l l } { P _ { 1 } } & { O } \\ { O } & { P _ { 1 } ^ { - 1 } } \end{array} \right] , \quad P _ { 1 } ^ { \prime } = P _ { 1 } > 0 , \quad M _ { 2 1 } = \left[ \begin{array} { l l } { I } & { S _ { 1 } } \\ { O } & { I } \end{array} \right] .
$$

By the equality $M _ { 0 } M _ { 1 } M _ { 2 } = M _ { 0 1 } M _ { 1 1 } M _ { 2 1 }$ , we have

$$
\begin{array} { c l } { { S p _ { 2 n } ( 0 ) \ni M _ { 0 1 } ^ { - 1 } M _ { 0 } ~ = ~ M _ { 1 1 } M _ { 2 1 } M _ { 2 } ^ { - 1 } M _ { 1 } ^ { - 1 } } } \\ { { } } & { { ~ = ~ \left[ \begin{array} { c c } { { P _ { 1 } } } & { { O } } \\ { { O } } & { { P _ { 1 } ^ { - 1 } } } \end{array} \right] \left[ \begin{array} { c c } { { I } } & { { S _ { 1 } } } \\ { { O } } & { { I } } \end{array} \right] \left[ \begin{array} { c c } { { I } } & { { - S } } \\ { { O } } & { { I } } \end{array} \right] \left[ \begin{array} { c c } { { P ^ { - 1 } } } & { { O } } \\ { { O } } & { { P } } \end{array} \right] } } \\ { { } } & { { ~ = ~ \left[ \begin{array} { c c } { { P _ { 1 } } } & { { O } } \\ { { O } } & { { P _ { 1 } ^ { - 1 } } } \end{array} \right] \left[ \begin{array} { c c } { { I } } & { { S _ { 1 } - S } } \\ { { O } } & { { I } } \end{array} \right] \left[ \begin{array} { c c } { { P ^ { - 1 } } } & { { O } } \\ { { O } } & { { P } } \end{array} \right] } } \\ { { } } & { { ~ = ~ \left[ \begin{array} { c c } { { P _ { 1 } P ^ { - 1 } } } & { { P _ { 1 } ( S _ { 1 } - S ) P } } \\ { { O } } & { { P _ { 1 } ^ { - 1 } P } } \end{array} \right] \in S p _ { 2 n } ( 0 ) . } } \end{array}
$$

Thus,

$$
{ \begin{array} { r l } { \left[ \begin{array} { c } { P _ { 1 } ( S _ { 1 } - S ) P } \\ { P _ { 1 } ^ { - 1 } P } \end{array} \right] } & { = \ J ^ { \prime } \left[ \begin{array} { c } { P _ { 1 } P ^ { - 1 } } \\ { O } \end{array} \right] } \\ & { = \ \left[ \begin{array} { c c } { O } & { - I } \\ { I } & { O } \end{array} \right] \left[ \begin{array} { c } { P _ { 1 } P ^ { - 1 } } \\ { O } \end{array} \right] } \\ & { = \ \left[ \begin{array} { c } { O } \\ { P _ { 1 } P ^ { - 1 } } \end{array} \right] . } \end{array} }
$$

Then, $P _ { 1 } ( S _ { 1 } - S ) P = O$ and $P _ { 1 } ^ { - 1 } P = P _ { 1 } P ^ { - 1 }$ , i.e., $S _ { 1 } = S$ and $P _ { 1 } ^ { 2 } = P ^ { 2 }$ . Therefore, $P _ { 1 } = P$ , since $P _ { 1 } , \ P$ are positive definite. It follows that, $M _ { 0 1 } ^ { - 1 } M _ { 0 } = I$ , i.e., $M _ { 0 } = M _ { 0 1 }$ . This is what we need to prove.

Theorem 3.45. If $M = \left[ \begin{array} { c c } { { A _ { 1 } } } & { { B _ { 1 } } } \\ { { A _ { 2 } } } & { { B _ { 2 } } } \end{array} \right] \in S p ( 2 n )$ with $\vert A _ { 1 } \vert \ne 0$ , then it can be decomposed as

$$
M = M _ { 2 ^ { \prime } } M _ { 1 } M _ { 2 } ,
$$

where $M _ { 2 ^ { \prime } } \in S p _ { 2 n } ( \mathrm { I I ^ { \prime } } ) , M _ { 1 } \in S p _ { 2 n } ( \mathrm { I } ) , M _ { 2 } \in S p _ { 2 n } ( \mathrm { I I } ) .$

This leads to $| M | = 1$

Proof. By Gauss elimination,

$$
\begin{array} { r l } & { \left[ \begin{array} { l l } { A _ { 1 } } & { B _ { 1 } } \\ { A _ { 2 } } & { B _ { 2 } } \end{array} \right] \left[ \begin{array} { l l } { I } & { - A _ { 1 } ^ { - 1 } B _ { 1 } } \\ { O } & { I } \end{array} \right] = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { A _ { 2 } } & { B _ { 2 } - A _ { 2 } A _ { 1 } ^ { - 1 } B _ { 1 } } \end{array} \right] , } \\ & { \left[ \begin{array} { l l } { I } & { O } \\ { - A _ { 2 } A _ { 1 } ^ { - 1 } } & { I } \end{array} \right] \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { A _ { 2 } } & { B _ { 2 } - A _ { 2 } A _ { 1 } ^ { - 1 } B _ { 1 } } \end{array} \right] = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { B _ { 2 } - A _ { 2 } A _ { 1 } ^ { - 1 } B _ { 1 } } \end{array} \right] . } \end{array}
$$

$M = [ A , B ] \in S p ( 2 n )$ , and so $A ^ { \prime } J B = I$ and $A ^ { \prime }$ is a symmetric pair, i.e.,

$$
A _ { 1 } ^ { \prime } B _ { 2 } - A _ { 2 } ^ { \prime } B _ { 1 } = I , \quad A _ { 2 } A _ { 1 } ^ { - 1 } \in S M .
$$

Thus,

$$
A _ { 1 } ^ { - 1 ^ { \prime } } { = } B _ { 2 } - A _ { 1 } ^ { - 1 ^ { \prime } } A _ { 2 } ^ { \prime } B _ { 1 } = B _ { 2 } - ( A _ { 2 } A _ { 1 } ^ { - 1 } ) ^ { \prime } B _ { 1 } = B _ { 2 } - A _ { 2 } A _ { 1 } ^ { - 1 } B _ { 1 } .
$$

Obvioualy,

$$
\begin{array} { r l } & { M _ { 1 } = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { B _ { 2 } - A _ { 2 } A _ { 1 } ^ { - 1 } B _ { 1 } } \end{array} \right] = \left[ \begin{array} { l l } { A _ { 1 } } & { O } \\ { O } & { A _ { 1 } ^ { - 1 ^ { \prime } } } \end{array} \right] \in S p _ { 2 n } ( \mathrm { I } ) , } \\ & { M _ { 2 ^ { \prime } } = \left[ \begin{array} { l l } { I } & { O } \\ { - A _ { 2 } A _ { 1 } ^ { - 1 } } & { I } \end{array} \right] ^ { - 1 } \in S p _ { 2 n } ( \mathrm { I I } ^ { \prime } ) , } \\ & { M _ { 2 } = \left[ \begin{array} { l l } { I } & { - A _ { 1 } ^ { - 1 } B _ { 1 } } \\ { O } & { I } \end{array} \right] ^ { - 1 } \in S p _ { 2 n } ( \mathrm { I I } ) , } \end{array}
$$

by which we get the decomposition $M = M _ { 2 ^ { \prime } } M _ { 1 } M _ { 2 }$ .

Theorem 3.46. Every symplectic matrix $M$ can be decomposed as

$$
M = M _ { 3 } M _ { 2 ^ { \prime } } M _ { 1 } M _ { 2 } ,
$$

where $M _ { 3 } \in S p _ { 2 n } ( \mathrm { I I I } ) , M _ { 2 ^ { \prime } } \in S p _ { 2 n } ( \mathrm { I I ^ { \prime } } ) , M _ { 1 } \in S p _ { 2 n } ( \mathrm { I } ) , M _ { 2 } \in S p _ { 2 n } ( \mathrm { I I } ) .$ , and it reduces $| M | = 1$ too.

Proof. It follows from that there exists $\alpha \subset \nu$ such that $\begin{array} { r } { J _ { \alpha } ^ { - 1 } \left[ \begin{array} { l l } { A _ { 1 } } & { B _ { 1 } } \\ { A _ { 2 } } & { B _ { 2 } } \end{array} \right] = } \end{array}$ $\left[ \begin{array} { l l } { C _ { 1 } } & { D _ { 1 } } \\ { C _ { 2 } } & { D _ { 2 } } \end{array} \right]$ with $| C _ { 1 } | \neq 0$ and Theorem 3.45.

# 2.3.6 Eigenvalues of Symplectic and Infinitesimal Matrices

Definition 3.47. A real polynomial $P _ { m } ( \lambda ) = a _ { 0 } \lambda ^ { m } + a _ { 1 } \lambda ^ { m - 1 } + \cdots + a _ { m }$ is called reflective if $P _ { m } ( \lambda ) = \lambda ^ { m } P _ { m } ( 1 / \lambda )$ .

It is easy to see that $P _ { m }$ is reflective if and only if $a _ { i } = a _ { m - i } ( i = 0 , \cdot \cdot \cdot , m )$ .

Lemma 3.48. We have the following results: $1 ^ { \circ }$ $Q ( \lambda ) = b _ { 0 } \lambda ^ { 2 } + b _ { 1 } \lambda + b _ { 2 }$ is reflective iff $b _ { 0 } = b _ { 2 }$ , i.e., $Q ( \lambda ) = b _ { 0 } ( \lambda - \alpha ) ( \lambda -$   
$1 / \alpha )$ . $2 ^ { \circ }$ $L ( \lambda ) = c _ { 0 } \lambda + c _ { 1 }$ is reflective iff $c _ { 0 } = c _ { 1 }$ , i.e., $L ( \lambda ) = c _ { 0 } ( \lambda + 1 )$ .

Property 3.49. We have the following properties:

$1 ^ { \circ }$ $P _ { 1 } , P _ { 2 }$ reflective $\Rightarrow P _ { 1 } \cdot P _ { 2 }$ reflective. $2 ^ { \circ }$ $P = P _ { 1 } \cdot P _ { 2 } , P , P _ { 1 }$ reflective $\Rightarrow P _ { 2 }$ reflective. $\begin{array} { l l } { { 3 ^ { \circ } } } & { { m = \displaystyle 2 n , P _ { m } \mathrm { ~ r e f l e c t i v e } \Rightarrow P _ { m } = \displaystyle \prod _ { i = 1 } ^ { n } Q _ { i } ( \lambda ) , Q _ { i } \mathrm { ~ r e f l e c t i v e ~ o f ~ o r d e r } 2 . } } \\ { { 4 ^ { \circ } } } & { { m = \displaystyle 2 n + 1 , P _ { m } \mathrm { ~ r e f l e c t i v e } \Rightarrow P _ { m } = L ( \lambda ) \displaystyle \prod _ { i = 1 } ^ { n } Q _ { i } ( \lambda ) , Q _ { i } , L \mathrm { ~ r e f l e c t } } } \end{array}$ tive of order 2 and 1, respectively.

Lemma 3.50. The characteristic polynomial of a symplectic matrix $M \in S p ( 2 n )$ , $P ( \lambda ) = | M - \lambda I |$ is reflective.

Theorem 3.51. [Arn89,AM78] $\lambda _ { 0 }$ is an eigenvalue of a symplectic matrix $M$ with multiplicity $k$ . Then, $\lambda _ { 0 } ^ { - 1 } , \overline { { \lambda } } _ { 0 } , \overline { { \lambda } } _ { 0 } ^ { - 1 }$ are also the eigenvalues of M with the same multiplicity. $I f \pm 1$ are the eigenvalues of $M$ , then their multiplicity is even.

Possible cases of distribution of eigenvalues of a symplectic matrix of order 4 are depicted in Fig. 3.1.

Definition 3.52. A real polynomial $P _ { 2 n } ( \lambda ) = a _ { 0 } \lambda ^ { 2 n } + a _ { 1 } \lambda ^ { 2 n - 1 } + \cdots + a _ { 2 n }$ is even if $P ( \lambda ) = P ( - \lambda )$ .

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0003_pages_0141-0210/auto/images/f5df43aa1397bac66297067461446fa11d9992ed896c5852606f05c39b7ea66f.jpg)  
Fig. 3.1. Distribution of Eigenvalues of a symplectic matrix of $S p ( 4 )$

Obviously, $P _ { 2 n } ( \lambda )$ is even iff $a _ { 2 i + 1 } = 0 ( i = 0 , 1 , \cdots , n - 1 )$ . Every even polynomial $P _ { 2 n } ( \lambda )$ can be rewritten in the following form

$$
P _ { 2 n } ( \lambda ) = a _ { 0 } \prod _ { i = 1 } ^ { n } ( \lambda ^ { 2 } - c _ { i } ) .
$$

Lemma 3.53. The characteristic polynomial of every infinitesimal symplectic matrix is even.

Theorem 3.54. $\left[ { \mathrm { A r n } } 8 9 , { \mathrm { A M } } 7 8 \right]$ If $\lambda _ { 0 }$ is an eigenvalue of on infinitesimal symplectic matrix $B$ with multiplicity $k _ { : }$ , then $- \lambda _ { 0 } , \overline { { \lambda } } _ { 0 }$ and $- \overline { { \lambda } } _ { 0 }$ are the eigenvalues of $B$ with the same multiplicity. If 0 is an eigenvalue of $B$ , then its multiplicity is even.

The possible cases of distribution of eigenvalues of an infinitesimal symplectic matrix of order 4 are depicted in Fig. 3.2.

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0003_pages_0141-0210/auto/images/a10c857e72ba5be41673f1cb4b22bd1fc01d4998493fde11bf58becf6022b2c9.jpg)  
Fig. 3.2. Distribution of eigenvalues of an infinitesimal symplectic matrix of $s p ( 4 )$

# 2.3.7 Generating Functions for Lagrangian Subspaces

Special cases

$$
\begin{array} { r l } & { L \ = \ \{ \begin{array} { l } { S } \\ { I } \end{array} \} = \{ [ \begin{array} { l } { p } \\ { q } \end{array} ] \in \mathbf { R } ^ { 2 n } \ : \bigg | \ ( p ^ { \prime } , q ^ { \prime } ) J \bigg [ \begin{array} { l } { S } \\ { I } \end{array} ] = O \} \ ( S ^ { \prime } = S ) } \\ & { \ = \ \{ [ \begin{array} { l } { p } \\ { q } \end{array} ] \in \mathbf { R } ^ { 2 n } \ : \bigg | \ ( p ^ { \prime } , q ^ { \prime } ) [ \begin{array} { c } { I } \\ { - S } \end{array} ] = O \} = \{ [ \begin{array} { l } { p } \\ { q } \end{array} ] \in \mathbf { R } ^ { 2 n } \ : \bigg | \ : p = S q \} } \\ & { = \ \{ [ \begin{array} { l } { p } \\ { q } \end{array} ] \in \mathbf { R } ^ { 2 n } \ : \bigg | \ : p = \frac { \partial \varphi } { \partial q } \} , } \end{array}
$$

where we define $\varphi ( q ) = \frac { 1 } { 2 } q ^ { \prime } S q$ , called as a generating function [Wei77,FWQW89,Fen95,Ge91] for $L$ .

Remark 3.55. There exists a generating function for Lagrangian subspace transversal to $R _ { \nu , 0 }$ or $R _ { 0 , \nu }$ .

Theorem 3.56. For a non-singular symmetric pair $A$ , there is $\alpha \subset \nu$ such that $\operatorname* { d e t } ( J _ { \widehat { \alpha } } ^ { - 1 } A ) _ { 2 } \neq 0$ and $\operatorname* { d e t } ( J _ { \alpha } ^ { - 1 } A ) _ { 1 } \neq 0$ , where $J _ { \alpha } ^ { - 1 } A$ and $J _ { \widehat { \alpha } } ^ { - 1 } A$ are non-singular symmetric pairs.

Proof. By Theorem 3.14, there exists $\alpha \subset \nu$ such that $\{ A \} \dot { + } \{ R _ { \alpha , \widehat { \alpha } } \} = { \bf R } ^ { 2 n }$ . This shows that the matrix $\left[ \begin{array} { l l } { I _ { \alpha } } & { A _ { 1 } } \\ { I _ { \widehat { \alpha } } } & { A _ { 2 } } \end{array} \right]$ is non-singular.

Multiplying by $J _ { \alpha } ^ { - 1 }$ , we have

$$
J _ { \alpha } ^ { - 1 } \left[ \begin{array} { c c } { I _ { \alpha } } & { A _ { 1 } } \\ { I _ { \widehat { \alpha } } } & { A _ { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { I _ { \widehat { \alpha } } } & { - I _ { \alpha } } \\ { I _ { \alpha } } & { I _ { \widehat { \alpha } } } \end{array} \right] \left[ \begin{array} { c c } { I _ { \alpha } } & { A _ { 1 } } \\ { I _ { \widehat { \alpha } } } & { A _ { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { O } & { ( J _ { \alpha } ^ { - 1 } A ) _ { 1 } } \\ { I } & { ( J _ { \alpha } ^ { - 1 } A ) _ { 2 } } \end{array} \right] .
$$

Therefore, $\operatorname* { d e t } \left( J _ { \alpha } ^ { - 1 } A \right) _ { 1 } \neq 0$ .

If replace $J _ { \alpha } ^ { - 1 }$ with $J _ { \widehat { \alpha } } ^ { - 1 }$ , then $\operatorname* { d e t } \left( J _ { \widehat { \alpha } } ^ { - 1 } A \right) _ { 2 } \neq 0$

For a general case, we have the following theorem:

Theorem 3.57. For every Lagrangian subspace $L = \{ A \} = \left\{ \begin{array} { c } { { A _ { 1 } } } \\ { { A _ { 2 } } } \end{array} \right\}$ , there exist an $\alpha \subset \nu$ and a generating function $\varphi$ , a quadratic form in $n$ -variables $\{ p _ { i } , q _ { j } \} _ { i \in \widehat { \alpha } , j \in \alpha }$ such that

$$
L = \left\{ \left( \begin{array} { l } { p } \\ { q } \end{array} \right) \in { \bf R } ^ { 2 n } \biggm | p _ { i } = \frac { \partial \varphi } { \partial q _ { i } } , i \in \alpha ; q _ { i } = - \frac { \partial \varphi } { \partial p _ { i } } , i \in \widehat { \alpha } \right\} .
$$

Proof. Taking $\alpha \subset \nu$ in Theorem 3.56, the matrix

$$
\left[ \begin{array} { l } { B _ { 1 } } \\ { B _ { 2 } } \end{array} \right] = { \cal B } = { \cal J } _ { \widehat { \alpha } } ^ { - 1 } { \cal A } = \left[ \begin{array} { l } { I _ { \alpha } A _ { 1 } - I _ { \widehat { \alpha } } A _ { 2 } } \\ { I _ { \widehat { \alpha } } A _ { 1 } + I _ { \alpha } A _ { 2 } } \end{array} \right]
$$

is Lagrangian with $| B _ { 2 } | \neq 0$ . Define

$$
\left[ \begin{array} { l } { u } \\ { v } \end{array} \right] = J _ { \widehat { \alpha } } ^ { - 1 } \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] = \left[ \begin{array} { l } { I _ { \alpha } p - I _ { \widehat { \alpha } } q } \\ { I _ { \widehat { \alpha } } p + I _ { \alpha } q } \end{array} \right] ;
$$

then,

$$
u _ { i } = \left\{ \begin{array} { l l } { p _ { i } , } & { i \in \alpha , } \\ { - q _ { i } , } & { i \in \widehat { \alpha } , } \end{array} \right. \quad v _ { i } = \left\{ \begin{array} { l l } { p _ { i } , } & { i \in \widehat { \alpha } , } \\ { q _ { i } , } & { i \in \alpha , } \end{array} \right.
$$

$$
\begin{array} { r l } & { [ p ^ { \prime } , q ^ { \prime } ] J \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] ^ { \prime } J _ { \widehat { \alpha } } ( J _ { \widehat { \alpha } } ^ { - 1 } J J _ { \widehat { \alpha } } ) J _ { \widehat { \alpha } } ^ { - 1 } \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] } \\ & { \qquad = \left[ J _ { \widehat { \alpha } } ^ { - 1 } \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] \right] ^ { \prime } J \left[ \begin{array} { l } { B _ { 1 } } \\ { B _ { 2 } } \end{array} \right] } \\ & { \qquad = \left[ u ^ { \prime } , \ v ^ { \prime } \right] J \left[ \begin{array} { l } { S } \\ { I } \end{array} \right] B _ { 2 } , } \end{array}
$$

where $S = B _ { 1 } B _ { 2 } ^ { - 1 } , S ^ { \prime } = S$ , and $J _ { \widehat { \alpha } } ^ { - 1 } = J _ { \widehat { \alpha } } ^ { \prime } \in S p ( 2 n )$ . Thus, if we define $\varphi ( v ) =$ 12 v Sv, then

$$
\begin{array} { r c l } { { L } } & { { = } } & { { \displaystyle \left\{ \left[ \begin{array} { l } { { p } } \\ { { q } } \end{array} \right] \in { \bf R } ^ { 2 n } \ : \left. \ : [ { p ^ { \prime } } , { q ^ { \prime } } ] J \right. \left[ \begin{array} { l } { { A _ { 1 } } } \\ { { A _ { 2 } } } \end{array} \right] = O \right\} = \left\{ \left[ \begin{array} { l } { { u } } \\ { { v } } \end{array} \right] \in { \bf R } ^ { 2 n } \ : \bigg \vert \ : [ u ^ { \prime } , v ^ { \prime } ] J \left[ \begin{array} { l } { { S } } \\ { { I } } \end{array} \right] = O \right. } } \\ { { } } & { { = } } & { { \displaystyle \left\{ \left[ \begin{array} { l } { { u } } \\ { { v } } \end{array} \right] \in { \bf R } ^ { 2 n } \ : \bigg \vert u = S v \right\} = \left\{ \left[ \begin{array} { l } { { u } } \\ { { v } } \end{array} \right] \in { \bf R } ^ { 2 n } \ : \bigg \vert u = \frac { \partial \varphi } { \partial v } \right\} } } \\ { { } } & { { = } } & { { \displaystyle \left\{ \left[ \begin{array} { l } { { p } } \\ { { q } } \end{array} \right] \in { \bf R } ^ { 2 n } \ : \bigg \vert \ : \left[ \begin{array} { l } { { p } } \\ { { q } } \end{array} \right] = J _ { \widehat { \alpha } } \left[ \begin{array} { l } { { u } } \\ { { v } } \end{array} \right] , u = \frac { \partial \varphi } { \partial v } \right\} } } \\ { { } } & { { = } } & { { \displaystyle \left\{ \left[ \begin{array} { l } { { p } } \\ { { q } } \end{array} \right] \in { \bf R } ^ { 2 n } \ : \bigg \vert \ : p _ { i } = \frac { \partial \varphi } { \partial q _ { i } } , i \in \alpha ; q _ { i } = - \frac { \partial \varphi } { \partial p _ { i } } , i \in \widehat { \alpha } \right\} . } } \end{array}
$$

Therefore, the theorem is completed.

# 2.3.8 Generalized Lagrangian Subspaces

In the previous sections, we have considered in detail the special symplectic space with the special symplectic structure

$$
\omega _ { J } ( x , y ) = \varphi _ { J } ( x , y ) = x ^ { \prime } J y , \quad J = \left[ \begin{array} { l l } { O } & { I } \\ { - I } & { O } \end{array} \right] .
$$

For every non-singular anti-symmetric matrix $K$ of order $2 n$ , $\omega _ { K } ( x , y ) = \varphi _ { K } ( x , y ) =$ $x ^ { \prime } K y$ is a symplectic structure on $\mathbf { R } ^ { 2 n }$ , and so $\left( \mathbf { R } ^ { 2 n } , \omega _ { K } \right)$ is also a symplectic space. Several previous results can be directly applied to this case. Here, we only give a few different theorems [FW91b,FWQW89] .

Definition 3.58. $\{ A \} ( \mathrm { o r } ~ A )$ is called as a $K$ -Lagrangian subspace, if $A ^ { \prime } K A \ =$ $0$ , and $A$ is non-singular.

Let us denote:

$$
\begin{array} { l } { { S p ( K , 2 n ) = \left\{ M \in M ( 2 n ) \mid M ^ { \prime } K M = K \right\} , } } \\ { { { } } } \\ { { C S p ( K , 2 n ) = \left\{ M \in M ( 2 n ) \mid M ^ { \prime } K M = \mu K , \mu \neq 0 \right\} . } } \end{array}
$$

Elements of $S p ( K , 2 n )$ or $C S p ( K , 2 n )$ are called as $K$ -symplectic matrices and conformally $K$ -symplectic matrices respectively.

Theorem 3.59. Let $M$ be non-singular.

$1 ^ { \circ }$ $M \in C S p ( K , 2 n )$ , iff $A \in \Lambda _ { n } ( K ) \Rightarrow M A \in \Lambda _ { n } ( K ) .$ $2 ^ { \circ }$ $M \in S p ( K , 2 n )$ , iff $( M A ) ^ { \prime } K ( M B ) = A ^ { \prime } K B$ or

$$
\varphi _ { k } ( M A , M B ) = \varphi _ { k } ( A , B ) , \quad \forall A , B \in \Lambda _ { n } ( K ) .
$$

$1 ^ { \circ } \quad \stackrel {   } { \Rightarrow } \ '$ al. We knsuch that ny non-, where etric matrix. Thus, $K$ $Q \in G L$ $K = Q ^ { \prime } J Q$ ${ \cal J } = \left( \begin{array} { l l } { { O } } & { { \dot { I } } } \\ { { - I } } & { { O } } \end{array} \right)$

$$
\begin{array} { r l } { A ^ { \prime } K A } & { = A ^ { \prime } Q ^ { \prime } J Q A = ( Q A ) ^ { \prime } J ( Q A ) , } \\ { ( M A ) ^ { \prime } K ( M A ) } & { = A ^ { \prime } M ^ { \prime } Q ^ { \prime } J Q ( M A ) } \\ & { = A ^ { \prime } Q ^ { \prime } Q ^ { \prime - 1 } M ^ { \prime } Q ^ { \prime } J Q M Q ^ { - 1 } Q A } \\ & { = ( Q A ) ^ { \prime } ( Q M Q ^ { - 1 } ) ^ { \prime } J ( Q M Q ^ { - 1 } ) ( Q A ) . } \\ { A \in \Lambda _ { n } ( K ) \Longrightarrow M A } & { \in \Lambda _ { n } ( K ) \Longleftrightarrow Q A \in \Lambda _ { n } ( J ) \Longrightarrow Q M Q ^ { - 1 } \in Q A \in \Lambda _ { n } ( J ) } \end{array}
$$

By Theorem 3.23, we get $Q M Q ^ { - 1 } \in C S p ( J )$ , i.e.,

$$
( Q M Q ^ { - 1 } ) ^ { \prime } J ( Q M Q ^ { - 1 } ) = \mu J , \mu \neq 0 .
$$

This leads to $M ^ { \prime } Q ^ { \prime } J Q M = \mu Q ^ { \prime } J Q$ , i.e., $M ^ { \prime } K M = \mu K$ .

$2 ^ { \circ }$ Similarly, we only need to prove the sufficiency. By $1 ^ { \circ }$ , we have $M ^ { \prime } K M =$ $\mu K , \mu \neq 0$ . Thus, $\forall A , B \in \Lambda _ { n } ( K )$ , we have

$$
A ^ { \prime } K B = \mu ^ { - 1 } A ^ { \prime } M ^ { \prime } K M B = \mu ^ { - 1 } A ^ { \prime } K B .
$$

Taking $A$ and $B \in \Lambda _ { n } ( K )$ such that $A ^ { \prime } K B \ne 0$ , we get $\mu = 1$ . Therefore,

$$
M ^ { \prime } K M = K .
$$

The theorem is proved.

Definition 3.60. Let $K _ { 1 }$ and $K _ { 2 }$ be two non-singular, anti-symmetric matrices of order $2 n$ . Define

$$
\begin{array} { r l } & { S p ( K _ { 1 } , K _ { 2 } ) = \left\{ M \in M ( 2 n ) \mid M ^ { \prime } K _ { 1 } M = K _ { 2 } \right\} , } \\ & { C S p ( K _ { 1 } , K _ { 2 } ) = \left\{ M \in M ( 2 n ) \mid \exists \mu \neq 0 , \mathrm { s . t . } M ^ { \prime } K _ { 1 } M = \mu K _ { 2 } \right\} . } \end{array}
$$

Remark 3.61. $S p ( K _ { 1 } , K _ { 2 } )$ and $C S p ( K _ { 1 } , K _ { 2 } )$ are not groups. However,

$$
\overline { { { S p } } } ( K _ { 2 } , K _ { 1 } ) = \overline { { { S p } } } ( J ) , \overline { { { C S p } } } ( K _ { 2 } , K _ { 1 } ) = \overline { { { C S p } } } ( J )
$$

have the same power. In fact, $\exists Q _ { 1 } , Q _ { 2 } \ \in \ G L$ , such that $K _ { 1 } \ = \ Q _ { 1 } ^ { \prime } J Q _ { 1 } , K _ { 2 } \ =$ $Q _ { 2 } ^ { \prime } J Q _ { 2 }$ ,

$$
M ^ { \prime } K _ { 2 } M = K _ { 1 } \Longleftrightarrow M ^ { \prime } Q _ { 2 } ^ { \prime } J Q _ { 2 } M = Q _ { 1 } ^ { \prime } J Q _ { 1 } ,
$$

i.e.,

$$
Q _ { 1 } ^ { - 1 ^ { \prime } } M ^ { \prime } Q _ { 2 } ^ { \prime } J Q _ { 2 } M Q _ { 1 } ^ { - 1 } = J .
$$

It is equivalent to $Q _ { 2 } M Q _ { 1 } ^ { - 1 } \in S p ( J )$ . Hence, the mapping: $M \in S p ( K _ { 2 } , K _ { 1 } ) \mapsto$ $Q _ { 2 } M Q _ { 1 } ^ { - 1 } \in S p ( J )$ is a one-to-one correspondence. It is also a one-to-one correspondence between $C S p ( K _ { 2 } , K _ { 1 } )$ and $C S p ( J )$ .

In addition, $M$ can be viewed as a mapping from $\Lambda _ { n } ( K _ { 2 } )$ to $\Lambda _ { n } ( K _ { 1 } )$ :

$$
M : \ \Lambda _ { n } ( K _ { 2 } ) \longmapsto \Lambda _ { n } ( K _ { 1 } ) , \ A \in \Lambda _ { n } ( K _ { 2 } ) \longmapsto M A \in \Lambda _ { n } ( K _ { 1 } ) .
$$

We have the following theorem similar to Theorem 3.23 and Theorem 3.59.

Theorem 3.62. Let $M$ be non-singular. Then, $1 ^ { \circ }$ $M \in C S p ( K _ { 2 } , K _ { 1 } )$ , iff $M A \in \Lambda _ { n } ( K _ { 1 } )$ , $\forall A \in \Lambda _ { n } ( K _ { 2 } )$ . $2 ^ { \circ }$ $M \in S p ( K _ { 2 } , K _ { 1 } )$ , iff $^ { * } ( M A ) ^ { \prime } K _ { 1 } ( M B ) = A ^ { \prime } K _ { 2 } B , \forall A , B \in \Lambda _ { n } ( K _ { 2 } ) .$

Proof. The proof is omitted, as it is similar to the proof of Theorem 3.59.

# Bibliography

[AM78] R. Abraham and J. E. Marsden: Foundations of Mechanics. Reading, MA: Addison-Wesley, Second edition, (1978).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[Art57] E. Artin: Geometrical Algebra. Interscience Publishers, New York, Second edition, (1957).   
[Car65] C. Carathe’odory: Calculus of Variation and Partial Differential Equations of First Order, Vol.I. Holden-Day, San Franscisco, (1965).   
[Fen95] K. Feng: Collected Works of Feng Kang. Volume I, II. National Defence Industry Press, Beijing, (1995).   
[FQ91] K. Feng and M.Z. Qin: Hamiltonian Algorithms for Hamiltonian Dynamical Systems. Progr. Natur. Sci., 1(2):105–116, (1991).   
[FW91] K. Feng and D.L. Wang: Symplectic Difference Schemes for Hamiltonian Systems in General Symplectic Structures. J. Comput. Math., 9(1):86–96, (1991).   
[FWQW89] K. Feng, H. M Wu, M.Z. Qin, and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[Ge91] Z. Ge: Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, (1991).   
[HW63] L.G. Hua and Z.X. Wan: Classical Groups. Shanghai Science and Technology Publishing House, in Chinese, Shanghai, (1963).   
[LM87] P. Libermann and C.M. Marle: Symplectic Geometry and Analytical Mechanics. Reidel pub. company, Boston, First edition, (1987).   
[Tre75] F. Treves: Pseudo-Differential Operator. Acad.Press, New York, First edition, (1975).   
[Wei77] A. Weinstein: Lectures on symplectic manifolds. In CBMS Regional Conference, 29. American Mathematical Society, Providence, RI, (1977).   
[Wey39] H. Weyl: The Classical Groups. Princeton Univ. Press, Princeton, Second edition, (1939).   
[Wey40] H. Weyl: The method of orthogonal projection in potential theory. Duke Math. J., 7:411–444, (1940).
