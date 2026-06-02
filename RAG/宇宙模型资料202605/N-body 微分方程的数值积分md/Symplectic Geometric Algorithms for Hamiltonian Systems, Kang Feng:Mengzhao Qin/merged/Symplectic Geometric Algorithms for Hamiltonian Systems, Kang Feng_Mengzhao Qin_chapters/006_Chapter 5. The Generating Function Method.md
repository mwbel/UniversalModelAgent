# Chapter 5. The Generating Function Method

This chapter discusses the construction of the symplectic difference schemes via generating function and their conservation laws.

# 5.1 Linear Fractional Transformation

Definition 1.1. Let $\alpha = \left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] \in G L ( 2 m )$ . A linear fractional transformation is defined by[Sie43,Hua44,FWQW89,Fen86]

$$
\sigma _ { \alpha } : { \cal M } ( m ) \longrightarrow { \cal N } ( m ) ,
$$

$$
M \longrightarrow N = \sigma _ { \alpha } ( M ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } ,
$$

under the transversality condition

$$
\left| C _ { \alpha } M + D _ { \alpha } \right| \neq 0 .
$$

$\alpha \in G L ( 2 m )$ , and the inverse $\alpha ^ { - 1 } = { \left[ \begin{array} { l l } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] }$

$$
\begin{array} { l c c } { { | C _ { \alpha } M + D _ { \alpha } | \neq 0 } } & { { i f f } } & { { | M C ^ { \alpha } - A ^ { \alpha } | \neq 0 , } } \\ { { } } & { { } } & { { } } \\ { { | A _ { \alpha } M + B _ { \alpha } | \neq 0 } } & { { i f f } } & { { | B ^ { \alpha } - M D ^ { \alpha } | \neq 0 . } } \end{array}
$$

Thus the linear fractional transformation $\sigma _ { \alpha }$ in (1.1) can be represented as

$$
\sigma _ { \alpha } ( M ) = ( M C ^ { \alpha } - A ^ { \alpha } ) ^ { - 1 } ( B ^ { \alpha } - M D ^ { \alpha } ) .
$$

Proof. From the relation

$$
\left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] \left[ \begin{array} { l l } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] = \left[ \begin{array} { l l } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] = I _ { 2 m } ,
$$

i.e.,

$$
\begin{array} { r l } & { A _ { \alpha } A ^ { \alpha } + B _ { \alpha } C ^ { \alpha } = A ^ { \alpha } A _ { \alpha } + B ^ { \alpha } C _ { \alpha } = I _ { m } , } \\ & { C _ { \alpha } B ^ { \alpha } + D _ { \alpha } D ^ { \alpha } = C ^ { \alpha } B _ { \alpha } + D ^ { \alpha } D _ { \alpha } = I _ { m } , } \\ & { A _ { \alpha } B ^ { \alpha } + B _ { \alpha } D ^ { \alpha } = A ^ { \alpha } B _ { \alpha } + B ^ { \alpha } D _ { \alpha } = O , } \\ & { C _ { \alpha } A ^ { \alpha } + D _ { \alpha } C ^ { \alpha } = C ^ { \alpha } A _ { \alpha } + D ^ { \alpha } C _ { \alpha } = O , } \end{array}
$$

we obtain the following identities:

$$
\begin{array} { r l } & { \left[ \begin{array} { c c } { I } & { - M } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] \left[ \begin{array} { c c } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] = \left[ \begin{array} { c c } { A ^ { \alpha } - M C ^ { \alpha } } & { B ^ { \alpha } - M D ^ { \alpha } } \\ { O } & { I } \end{array} \right] , } \\ & { \left[ \begin{array} { c c } { I } & { - M } \\ { A _ { \alpha } } & { B _ { \alpha } } \end{array} \right] \left[ \begin{array} { c c } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] = \left[ \begin{array} { c c } { A ^ { \alpha } - M C ^ { \alpha } } & { B ^ { \alpha } - M D ^ { \alpha } } \\ { I } & { O } \end{array} \right] . } \end{array}
$$

In addition, we have:

$$
\begin{array} { r l } & { \left[ \begin{array} { c c } { I } & { - M } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] = \left[ \begin{array} { c c } { I } & { O } \\ { C _ { \alpha } } & { I } \end{array} \right] \left[ \begin{array} { c c } { I } & { - M } \\ { O } & { C _ { \alpha } M + D _ { \alpha } } \end{array} \right] , } \\ & { \left[ \begin{array} { c c } { I } & { - M } \\ { A _ { \alpha } } & { B _ { \alpha } } \end{array} \right] = \left[ \begin{array} { c c } { I } & { O } \\ { A _ { \alpha } } & { I } \end{array} \right] \left[ \begin{array} { c c } { I } & { - M } \\ { O } & { A _ { \alpha } M + B _ { \alpha } } \end{array} \right] . } \end{array}
$$

Inserting (1.7) into (1.6), taking their determinate, we obtain

$$
\begin{array} { r l } & { | C _ { \alpha } M + D _ { \alpha } | | \alpha | ^ { - 1 } = | A ^ { \alpha } - M C ^ { \alpha } | , } \\ & { | A _ { \alpha } M + B _ { \alpha } | | \alpha | ^ { - 1 } = ( - 1 ) ^ { m } | B ^ { \alpha } - M D ^ { \alpha } | . } \end{array}
$$

Note that since $\alpha$ is a non-singular matrix, (1.3) is valid.

By (1.8), Equation (1.4) is well defined. The only remaining step is to verify the equation

$$
( M C ^ { \alpha } - A ^ { \alpha } ) ^ { - 1 } ( B ^ { \alpha } - M D ^ { \alpha } ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } ,
$$

i.e.,

$$
( B ^ { \alpha } - M D ^ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) = ( M C ^ { \alpha } - A ^ { \alpha } ) ( A _ { \alpha } M + B _ { \alpha } ) .
$$

Expanding it and using the conditions (1.5), we know that it holds.

Proposition 1.3. We have the following well-known relation

$$
( C ^ { \alpha } N + D ^ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) = I ,
$$

hence

$$
\left| C ^ { \alpha } N + D ^ { \alpha } \right| \neq 0 \quad i f \quad \left| C _ { \alpha } M + D _ { \alpha } \right| \neq 0 ,
$$

where $N = \sigma _ { \alpha } ( M )$ . Under the transversality condition (1.2), $\sigma _ { \alpha }$ has an inverse linear fractional transformation $\sigma _ { \alpha } ^ { - 1 } = \sigma _ { \alpha ^ { - 1 } }$ ,

$$
\begin{array} { r c l } { { { \cal M } = \sigma _ { \alpha ^ { - 1 } } ( N ) ~ = ~ ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } } } \\ { { } } & { { } } \\ { { } } & { { = ~ ( N C _ { \alpha } - A _ { \alpha } ) ^ { - 1 } ( B _ { \alpha } - N D _ { \alpha } ) . } } \end{array}
$$

Proof.

$$
\begin{array} { l l } { ( C ^ { \alpha } N + D ^ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) } \\ { = ( C ^ { \alpha } ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } + D ^ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) } \\ { = ( C ^ { \alpha } A _ { \alpha } + D ^ { \alpha } C _ { \alpha } ) M + C ^ { \alpha } B _ { \alpha } + D ^ { \alpha } D _ { \alpha } } \\ { = I } & { ( \mathrm { b y \ ( 1 . 5 ) } ) , } \end{array}
$$

which is (1.9). The first equation of (1.10) can be obtained from (1.4) and the second equation can be derived from (1.1).

Combining (1.2) and (1.3) together, we obtain the following four mutually equivalent transversality conditions:

$$
\begin{array} { r l } & { \left| C _ { \alpha } M + D _ { \alpha } \right| \neq 0 , } \\ & { \left| M C ^ { \alpha } - A ^ { \alpha } \right| \neq 0 , } \\ & { \left| C ^ { \alpha } N + D ^ { \alpha } \right| \neq 0 , } \\ & { \left| N C _ { \alpha } - A _ { \alpha } \right| \neq 0 , } \end{array}
$$

where

$$
\begin{array} { l } { { N = \sigma _ { \alpha } ( M ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } , } } \\ { { { } } } \\ { { M = \sigma _ { \alpha ^ { - 1 } } ( N ) = ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } . } } \end{array}
$$

Moreover, the linear fractional transformation $\sigma _ { \alpha }$ from $\{ M \in ~ M ( m ) ~ | ~ | C _ { \alpha } M + $ $D _ { \alpha } { \vert } \neq 0 \}$ to $\{ N \in M ( m ) \mid | C ^ { \alpha } N + D ^ { \alpha } | \neq 0 \}$ is 1-1 surjective.

# 5.2 Symplectic, Gradient Mapping and Generating Function

To study the symplectic structure and Hamiltonian system in $\mathbf { R } ^ { 2 n }$ phase space, we need $\mathbf { R } ^ { 4 n }$ symplectic structure as a product of $\mathbf { R } ^ { 2 n }$ space. Its symplectic structure comes from the product of original symplectic structure in $\mathbf { R } ^ { 2 n }$

$$
\widetilde { \Omega } = \sum _ { i = 1 } ^ { n } \mathbf { d } \widehat { z } _ { i } \wedge \mathbf { d } \widehat { z } _ { i + n } - \sum _ { i = 1 } ^ { n } \mathbf { d } z _ { i } \wedge \mathbf { d } z _ { i + n } ,
$$

where the corresponding matrix is given by ${ \widetilde { J } } _ { 4 n } ~ = ~ \left[ \begin{array} { c c } { { J _ { 2 n } } } & { { O } } \\ { { O } } & { { - J _ { 2 n } } } \end{array} \right]$ . We denote $\widetilde { \mathbf R } ^ { 4 n } = ( \mathbf R ^ { 4 n } , \widetilde { J } _ { 4 n } )$ .

On the other hand, $\mathbf { R } ^ { 4 n }$ has its standard symplectic structure:

$$
\Omega = \sum _ { i = 1 } ^ { 2 n }  { \mathbf { d } } w _ { i } \ \wedge \  { \mathbf { d } } \ \widehat { w } _ { i + 2 n } ,
$$

where $( w _ { 1 } , \cdot \cdot \cdot , w _ { 2 n } , \widehat { w } _ { 1 } , \cdot \cdot \cdot , \widehat { w } _ { 2 n } ) ^ { \mathrm { T } }$ represents its coordinate. The corresponding matrix is given by

$$
J _ { 4 n } = \left[ \begin{array} { c c } { { O } } & { { I _ { 2 n } } } \\ { { } } & { { } } \\ { { - I _ { 2 n } } } & { { O } } \end{array} \right] .
$$

We denote manifold ${ \bf R } ^ { 4 n } = ( { \bf R } ^ { 4 n } , J _ { 4 n } )$

Now we first review some notations and facts of the symplectic algebra. Every $4 n \times 2 n$ matrix of rank $2 n$ can be represented as:

$$
A = { \left[ \begin{array} { l } { A _ { 1 } } \\ { A _ { 2 } } \end{array} \right] } \in M ( 4 n , 2 n ) , \quad A _ { 1 } , A _ { 2 } \in M ( 2 n ) ,
$$

defines a $4 n$ -dim subspace $\{ A \}$ spanned by its $2 n$ column vectors. Evidently, $\{ A \} =$ $\{ B \}$ iff $\exists P \in G L ( 2 n )$ such that

$$
A P = B , \quad \mathrm { i . e . , } \quad \left[ \begin{array} { l } { A _ { 1 } P } \\ { A _ { 2 } P } \end{array} \right] = \left[ \begin{array} { l } { B _ { 1 } } \\ { B _ { 2 } } \end{array} \right] .
$$

A $2 n$ -dim subspace $\{ X \} = { \left\{ \begin{array} { l } { X _ { 1 } } \\ { X _ { 2 } } \end{array} \right\} }$ of $\mathbf { R } ^ { 4 n } , X _ { 1 } , X _ { 2 } \in M ( 2 n )$ , is a $J _ { 4 n }$ -Lagrangian, if

$$
X ^ { \mathrm { T } } J _ { 4 n } X = O ,
$$

i.e.,

$$
X _ { 1 } ^ { \mathrm { { T } } } X _ { 2 } - X _ { 2 } ^ { \mathrm { { T } } } X _ { 1 } = O \quad \mathrm { o r } \quad X _ { 1 } ^ { \mathrm { { T } } } X _ { 2 } \in S m ( 2 n ) .
$$

According to Siegel[Sie43] , we call such a $4 n \times 2 n$ matrix $X = { \left[ \begin{array} { l } { X _ { 1 } } \\ { X _ { 2 } } \end{array} \right] }$ a symmetric pair. Moreover, if $| X _ { 2 } | \neq 0$ , then $X _ { 1 } X _ { 2 } ^ { - 1 } = N \in S m ( 2 n )$ and $\left\{ \begin{array} { c } { { X _ { 1 } } } \\ { { X _ { 2 } } } \end{array} \right\} = \left\{ \begin{array} { c } { { N } } \\ { { I } } \end{array} \right\} .$ . Similarly, a $2 n$ -dim subspace $\{ Y \} = \left\{ \begin{array} { c } { { Y _ { 1 } } } \\ { { Y _ { 2 } } } \end{array} \right\}$ is ${ \tilde { J } } _ { 4 n }$ -Lagrangian, if

$$
{ \cal Y } ^ { \mathrm { T } } \tilde { { \cal J } } _ { 4 n } { \cal Y } = { \cal O } ,
$$

i.e.,

$$
Y _ { 1 } ^ { \mathrm { T } } J _ { 2 n } Y _ { 1 } = Y _ { 2 } ^ { \mathrm { T } } J _ { 2 n } Y _ { 2 } ,
$$

the $4 n \times 2 n$ matrix $Y = \left[ \begin{array} { c } { { Y _ { 1 } } } \\ { { Y _ { 2 } } } \end{array} \right]$ is called a symplectic pair. $| Y _ { 2 } | \neq 0$ implies $Y _ { 1 } Y _ { 2 } ^ { - 1 } =$ $M \in S p ( 2 n )$ , and $\left\{ \begin{array} { c } { { Y _ { 1 } } } \\ { { Y _ { 2 } } } \end{array} \right\} = \left\{ \begin{array} { c } { { M } } \\ { { I } } \end{array} \right\}$ .

Theorem 2.1. A transformation  Aα BαC D  ∈ GL(4n) carries every J˜ 4n-Lagrangian subspace into a $J _ { 4 n }$ -Lagrangian subspace if and only if $\alpha \in C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ i.e.,

$$
\alpha ^ { \mathrm { T } } J _ { 4 n } \alpha = \mu \tilde { J } _ { 4 n } , \quad f o r s o m e \ \mu = \mu ( \alpha ) \neq 0 .
$$

Proof. The “if” part is obvious, we need only to prove the “only if” part.

Taking $\alpha _ { 0 } \in S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ (which always exists), e.g., $\alpha _ { 0 } = \left[ \begin{array} { c c } { { \dot { J } _ { 2 n } } } & { { J _ { 2 n } } } \\ { { \frac { 1 } { 2 } I _ { 2 n } } } & { { \frac { 1 } { 2 } I _ { 2 n } } } \end{array} \right] ,$ we have

$$
C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } ) = C S p ( 4 n ) \cdot \alpha _ { 0 } .
$$

Therefore, it suffices to show that if $\alpha$ carries every $J _ { 4 n }$ - Lagrangian subspace into $J _ { 4 n }$ -Lagrangian subspace, then $\alpha \in C S p ( 4 n )$ , i.e.,

$$
\alpha ^ { \mathrm { T } } J _ { 4 n } \alpha = \mu J _ { 4 n } \quad \mathrm { f o r ~ s o m e } \mu \neq 0 .
$$

$1 ^ { \circ }$ Take the symmetric pair $\begin{array} { r } { X = \left[ \begin{array} { c } { I _ { 2 n } } \\ { O _ { 2 n } } \end{array} \right] } \end{array}$ . By assumption,

$$
\alpha X = { \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] } { \left[ \begin{array} { l } { I } \\ { O } \end{array} \right] } = { \left[ \begin{array} { l } { A _ { \alpha } } \\ { C _ { \alpha } } \end{array} \right] }
$$

is also a symmetric pair, i.e., $A _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } = O$ . Similarly, $B _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } = O$

$2 ^ { \circ }$ Take the symmetric pair $X = { \left[ \begin{array} { l } { S } \\ { I } \end{array} \right] } , S \in S m ( 2 n )$ . Then every

$$
\alpha X = { \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] } { \left[ \begin{array} { l } { S } \\ { I } \end{array} \right] } = { \left[ \begin{array} { l } { A _ { \alpha } S + B _ { \alpha } } \\ { C _ { \alpha } S + D _ { \alpha } } \end{array} \right] }
$$

is also a symmetric pair, i.e.,

$$
\begin{array} { r l } { O \ = \ ( \alpha X ) ^ { \mathrm { T } } J _ { 4 n } ( \alpha X ) } \\ { \ } & { \ = \ \big ( S ^ { \mathrm { T } } A _ { \alpha } ^ { \mathrm { T } } + B _ { \alpha } ^ { \mathrm { T } } , S ^ { \mathrm { T } } C _ { \alpha } ^ { \mathrm { T } } + D _ { \alpha } ^ { \mathrm { T } } \big ) \left[ \begin{array} { l l } { O } & { I } \\ { - I } & { O } \end{array} \right] \left[ \begin{array} { l } { A _ { \alpha } S + B _ { \alpha } } \\ { C _ { \alpha } S + D _ { \alpha } } \end{array} \right] } \\ { \ } & { \ = \ S ( A _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } ) S + S ( A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } ) } \\ { \ } & { \ - ( D _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } - B _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } ) S + B _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } } \\ { \ } & { \ = \ S ( A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } ) - ( A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } ) ^ { \mathrm { T } } S , \quad \forall S \in S m ( 2 n ) . } \end{array}
$$

Set $P = A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha }$ , then the above equation becomes

$$
S P = P ^ { \mathrm { T } } S , \quad \forall S \in S m ( 2 n ) .
$$

It follows that $P = \mu I$ , i.e.,

$$
A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } = \mu I .
$$

So

$$
\begin{array} { r l } { \alpha ^ { \mathrm { T } } J _ { 4 n } \alpha ~ = ~ \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] ^ { \mathrm { T } } \left[ \begin{array} { l l } { O } & { I } \\ { - I } & { O } \end{array} \right] \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] } & { } \\ { ~ = ~ \left[ \begin{array} { l l } { A _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } } & { A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } } \\ { B _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } } & { B _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } } \end{array} \right] } & { } \\ { ~ = ~ \mu \left[ \begin{array} { l l } { O } & { I } \\ { - I } & { O } \end{array} \right] = \mu J _ { 4 n } , } \end{array}
$$

$\alpha \in G L ( 4 n )$ implies $\mu \neq 0$ .

The inverse matrix of $\alpha$ is denoted by $\alpha ^ { - 1 } = { \left[ \begin{array} { l l } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] }$ . By (2.3), we have

$$
\begin{array} { l l } { { A _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } = \mu J , } } & { { A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } = O , } } \\ { { B _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } = O , } } & { { B _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } = - \mu J , } } \\ { { } } & { { A ^ { \alpha } = \mu ^ { - 1 } J C _ { \alpha } ^ { \mathrm { T } } , } } \\ { { C ^ { \alpha } = - \mu ^ { - 1 } J D _ { \alpha } ^ { \mathrm { T } } , } } & { { D ^ { \alpha } = \mu ^ { - 1 } J B _ { \alpha } ^ { \mathrm { T } } . } } \end{array}
$$

Theorem 2.2. Let  Aα BαC D  ∈ CSp(J˜ 4n, J4n). The linear fractional transformation ${ \sf r } _ { \alpha } \colon \{ M \in S p ( 2 n ) \mid  C _ { \alpha } M + D _ { \alpha }  \neq 0 \}  \{ N \in S m ( 2 n ) \mid  C ^ { \alpha } N + D ^ { \alpha }  \neq 0 \}$ $0 \}$ is one to one and onto.

Proof. From above we know that $| C _ { \alpha } M + D _ { \alpha } | \neq 0$ , iff $\vert C ^ { \alpha } N + D ^ { \alpha } \vert \neq 0 .$ Now we need only to prove $M \in S p ( 2 n )$ iff $N = \sigma _ { \alpha } ( M ) \in S m ( 2 n )$ . It is derived from direct calculation, since $N \in S m ( 2 n )$ iff

$$
\left( ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } \right) ^ { \mathrm { T } } = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } ,
$$

$$
( M ^ { \mathrm { T } } A _ { \alpha } ^ { \mathrm { T } } + B _ { \alpha } ^ { \mathrm { T } } ) ( C _ { \alpha } ^ { \mathrm { T } } M ^ { \mathrm { T } } + D _ { \alpha } ) = ( M ^ { \mathrm { T } } C _ { \alpha } ^ { \mathrm { T } } + D _ { \alpha } ^ { \mathrm { T } } ) ( A _ { \alpha } M + B _ { \alpha } ) .
$$

Expanding and combining them together, we obtain

$$
\begin{array} { r l } { O = } & { M ^ { \mathrm { T } } ( A _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } ) M + B _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } } \\ & { + M ^ { \mathrm { T } } ( A _ { \alpha } ^ { \mathrm { T } } D _ { \alpha } - C _ { \alpha } ^ { \mathrm { T } } B _ { \alpha } ) + ( B _ { \alpha } ^ { \mathrm { T } } C _ { \alpha } - D _ { \alpha } ^ { \mathrm { T } } A _ { \alpha } ) M } \\ { = } & { M ^ { \mathrm { T } } J M - J , } \end{array}
$$

then (2.4) holds, iff $M \in S p ( 2 n )$ .

Definition 2.3. A mapping $w \to { \widehat { w } } = f ( w ) : \mathbf { R } ^ { 2 n } \to \mathbf { R } ^ { 2 n }$ is called a gradient, if its Jacobian $N ( w ) = f _ { w } ( w ) \in S p ( 2 n )$ everywhere.

Definition 2.4. A $2 n$ -dim submanifold $U$ of $\mathbf { R } ^ { 4 n }$ is a $\widetilde { J } _ { 4 n }$ -Lagrangian submanifold or $J _ { 4 n }$ -Lagrangian submanifold if its tangent plane $T _ { z } U$ at $z$ for any $z \in U$ is a $4 n$ tangent space of $\widetilde { J } _ { 4 n }$ -Lagrangian subspace or $J _ { 4 n }$ -Lagrangian subspace.

For a symplectic mapping $z  { \widehat { z } } = g ( z )$ , the graph[Fen86,FWQW89,Ge91]

$$
\Gamma _ { g } = \mathrm { g r } ( g ) : = \left\{ \left[ \begin{array} { c } { { { \widehat z } } } \\ { { z } } \end{array} \right] \in { \bf R } ^ { 4 n } \ | \ { \widehat z } = g ( z ) , \ z \in { \bf R } ^ { 2 n } \right\}
$$

is always a $\widetilde { J } _ { 4 n }$ -Lagrange submanifold. For every gradient mapping $w \to \widehat { w } = f ( w )$ , its graph

$$
\Gamma _ { f } = \mathrm { g r } ( f ) : = \left\{ { \left[ \begin{array} { l } { \widehat { w } } \\ { w } \end{array} \right] } \in \mathbf { R } ^ { 4 n } \mid { \widehat { w } } = f ( w ) , w \in \mathbf { R } ^ { 2 n } \right\}
$$

is always a $J _ { 4 n }$ -Lagrange submanifold.

Let $\alpha = \left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$ , it defines a linear fractional transformation

$$
{ \left[ \begin{array} { l } { \widehat { w } } \\ { w } \end{array} \right] } = \alpha { \left[ \begin{array} { l } { \widehat { z } } \\ { z } \end{array} \right] } , \quad { \left[ \begin{array} { l } { \widehat { z } } \\ { z } \end{array} \right] } = \alpha ^ { - 1 } { \left[ \begin{array} { l } { \widehat { w } } \\ { w } \end{array} \right] } ,
$$

$$
\begin{array} { r } { \widehat { w } = A _ { \alpha } \widehat { z } + B _ { \alpha } z , \quad \widehat { z } = A ^ { \alpha } \widehat { w } + B ^ { \alpha } w , } \\ { w = C _ { \alpha } \widehat { z } + D _ { \alpha } z , \quad z = C ^ { \alpha } \widehat { w } + D ^ { \alpha } w . } \end{array}
$$

Theorem 2.5. Let $\alpha \in C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ . Let $z \ \to \ { \widehat { z } } \ = \ g ( z ) \ : \ \mathbf { R } ^ { 2 n } \ \to \ \mathbf { R } ^ { 2 n }$ be $a$ canonical mapping with Jacobian $M ( z ) = g _ { z } ( z ) \in S p ( 2 n )$ satisfying (1.2) in (some neighborhood of) $\mathbf { R } ^ { 2 n }$ . Then there exists a gradient mapping $w \to \widehat { w } = f ( w )$ in (some neighborhood of) $\mathbf { R } ^ { 2 n }$ with Jacobian $N ( w ) = f _ { w } ( w ) \in S m ( 2 n )$ and a scalar function —generating function— $\phi ( w )$ (depending on $\alpha$ and $g$ ) such that

$$
\begin{array} { r l } & { 1 ^ { \circ } \quad f ( w ) = \nabla \phi ( w ) ; } \\ & { 2 ^ { \circ } \quad A _ { \alpha } g ( z ) + B _ { \alpha } z = f ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) = \nabla \phi ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) ; } \\ & { 3 ^ { \circ } \quad N = \sigma _ { \alpha } ( M ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } , } \\ & { \quad M = \sigma _ { \alpha ^ { - 1 } } ( N ) = ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } ; } \\ & { 4 ^ { \circ } \quad \Gamma _ { f } = \alpha ( \Gamma _ { g } ) , \ \Gamma _ { g } = \alpha ^ { - 1 } ( \Gamma _ { f } ) . } \end{array}
$$

Proof. Under the linear transformation $\alpha$ , the image of $\Gamma _ { g }$ is

$$
\alpha ( \Gamma _ { g } ) = \left\{ \left[ \begin{array} { c } { { \widehat { w } } } \\ { { w } } \end{array} \right] \in \mathbf { R } ^ { 4 n } \mid \widehat { w } = A _ { \alpha } g ( z ) + B _ { \alpha } z , w = C _ { \alpha } g ( z ) + D _ { \alpha } z \right\} .
$$

Since $\Gamma _ { g }$ is a ${ \tilde { J } } _ { 4 n }$ -Lagrangian submanifold and $\alpha \in C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ , the tangent plane of $\alpha ( \Gamma _ { g } )$ defined by

$$
\left\{ \begin{array} { l } { { A _ { \alpha } M ( z ) + B _ { \alpha } } } \\ { { C _ { \alpha } M ( z ) + D _ { \alpha } } } \end{array} \right\}
$$

is a $J _ { 4 n }$ -Lagrangian subspace. So $\alpha ( \Gamma _ { g } )$ is a $J _ { 4 n }$ -Lagrangian submanifold. By assumption, $| C _ { \alpha } M + D _ { \alpha } | \neq 0$ , and by the implicit function theorem, $w = C _ { \alpha } g ( z ) +$ $D _ { \alpha } z$ is invertible and its inverse is denoted by $z = z ( w )$ . Set:

$$
\widehat { w } = f ( w ) = ( A _ { \alpha } g ( z ) + B _ { \alpha } z ) \mid _ { z = z ( w ) } = A _ { \alpha } g ( z ( w ) ) + B _ { \alpha } z ( w ) ,
$$

obviously, such a $f ( w )$ satisfies the identity

$$
A _ { \alpha } g ( z ) + B _ { \alpha } z \equiv f ( C _ { \alpha } g ( z ) + D _ { \alpha } z ) .
$$

The Jacobian of $f ( w )$ is

$$
\begin{array} { l } { { { \cal N } ( w ) ~ = ~ f _ { w } ( w ) = { \displaystyle \frac { \partial \widehat { w } } { \partial w } } = { \displaystyle \frac { \partial \widehat { w } } { \partial z } } = { \displaystyle \frac { \partial \widehat { w } } { \partial z } } \Big ( { \displaystyle \frac { \partial w } { \partial z } } \Big ) ^ { - 1 } } } \\ { { ~ = ~ ( A _ { \alpha } M ( z ) + B _ { \alpha } ) ( C _ { \alpha } M ( z ) + D _ { \alpha } ) ^ { - 1 } = \sigma _ { \alpha } ( M ( z ) ) . } } \end{array}
$$

By Theorem 2.2 it is symmetric. So $f ( w )$ is a gradient map. By the Poincare lemma, ´ there exists a scalar function $\phi ( w )$ , such that

$$
f ( w ) = \nabla \phi ( w ) .
$$

In addition, we have

$$
\Gamma _ { f } = \left\{ \left[ \begin{array} { l } { \widehat { w } } \\ { w } \end{array} \right] \in \mathbf { R } ^ { 4 n } \mid \widehat { w } = f ( w ) = A _ { \alpha } g ( z ( w ) ) + B _ { \alpha } z ( w ) \right\} = \alpha ( \Gamma _ { g } ) .
$$

Therefore, the theorem is completed.

This theorem tells us that for a fixed $\alpha$ , the corresponding symplectic mapping determines only one gradient mapping with accuracy up to a constant factor.

Theorem 2.6. Let $\alpha \in C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ . Let $\phi ( w )$ be a scalar function and $w  \widehat { w } =$ $f ( w ) = \nabla \phi ( w )$ be its induced gradient mapping and $N ( w ) = f _ { w } ( w ) = \phi _ { w w } ( w )$ , the Hessian matrix of $\phi ( w )$ , satisfy (1.13) in (some neighborhood of) $\mathbf { R } ^ { 2 n }$ . Then, there exists a canonical map $z  { \widehat { z } } = g ( z )$ with Jacobian $\begin{array} { r } { M ( z ) = g _ { z } ( z ) } \end{array}$ satisfying (1.11) such that

By the way, we can get the original symplectic mapping, if $f ( w )$ or $\phi ( w )$ is obtained from Theorem 2.5.

# 5.3 Generating Functions for the Phase Flow

Consider the Hamiltonian system

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J _ { 2 n } ^ { - 1 } \nabla H ( z ) , \quad z \in \mathbf { R } ^ { 2 n } ,
$$

where $H ( z )$ is a Hamiltonian function. Its phase flow is denoted as $g ^ { t } ( z ) = g ( z , t ) =$ $g _ { H } ( z , t )$ , being a one-parameter group of canonical maps, i.e.,

$$
g ^ { 0 } = \mathrm { i d e n t i t y } , \quad g ^ { t _ { 1 } + t _ { 2 } } = g ^ { t _ { 1 } } \circ g ^ { t _ { 2 } } ,
$$

and if $z _ { 0 }$ is taken as an initial condition, then $z ( t ) = g ^ { t } ( z _ { 0 } )$ is the solution of (3.1) with the initial value $z _ { \mathrm { 0 } }$ .

Theorem 3.1. Let $\alpha \in C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ . Let $z  { \widehat { z } } = g ( z , t )$ be the phase flow of the Hamiltonian system (3.1) and $M _ { 0 } \in S p ( 2 n )$ . Set $G ( z , t ) = g ( M _ { 0 } z , t )$ with Jacobian $M ( z , t ) = G _ { z } ( z , t )$ . It is a time-dependent canonical map. If $M _ { 0 }$ satisfies the transversality condition (1.2), i.e.,

$$
| C _ { \alpha } M _ { 0 } + D _ { \alpha } | \neq 0 ,
$$

then there exists, for sufficiently small $| t |$ and in (some neighborhood of) $\mathbf { R } ^ { 2 n }$ , a timedependent gradient map $w \to \widehat { w } = f ( w , t )$ with Jacobian $N ( w , t ) = f _ { w } ( w , t ) \in$ $S m ( 2 n )$ satisfying the transversality condition (1.13) and a time-dependent generating function $\phi _ { \alpha , H } ( w , t ) = \phi ( w , t )$ , such that

$$
\begin{array} { r l } { { 1 } ^ { \circ } } & { f ( w , t ) = \nabla \phi ( w , t ) . } \\ { { 2 } ^ { \circ } } & { \frac { \partial } { \partial t } \phi ( w , t ) = - \mu H ( A ^ { \alpha } \nabla \phi ( w , t ) + B ^ { \alpha } w ) . } \\ { { 3 } ^ { \circ } } & { A _ { \alpha } G ( z , t ) + B _ { \alpha } z \equiv f ( C _ { \alpha } G ( z , t ) + D _ { \alpha } z , t ) \equiv \nabla \phi ( C _ { \alpha } G ( z , t ) + D _ { \alpha } z , t ) \delta } \\ { { 4 } ^ { \circ } } & { N = \sigma _ { \alpha } ( M ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } , } \\ & { M = \sigma _ { \alpha ^ { - 1 } } ( N ) = ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } . } \end{array}
$$

(3.4) is the most general Hamilton–Jacobi equation for the Hamiltonian system (3.1) with the linear transformation $\alpha$ .

Proof. Since $g ( z , t )$ is differentiable with respect to $z$ and $t$ , so is $G ( z , t )$ . Condition (3.2) implies that for sufficiently small $| t |$ and in some neighborhood of $\mathbf { R } ^ { 2 n }$ ,

$$
\left| C _ { \alpha } M ( z , t ) + D _ { \alpha } \right| \neq 0 .
$$

Thus, by Theorem 2.5, there exists a time-dependent gradient map $\widehat { w } = f ( w , t )$ , such that it satisfies (3.2) and (3.6).

Set:

$$
\begin{array} { r } { \overline { { H } } ( w , t ) \ = \ - \mu H ( \widehat { z } ) \big | _ { \widehat { z } = A ^ { \alpha } \widehat { w } ( w , t ) + B ^ { \alpha } w } } \\ { \ = \ - \mu H ( A ^ { \alpha } \widehat { w } ( w , t ) + B ^ { \alpha } w ) . } \end{array}
$$

Consider the differential 1-form

$$
\begin{array} { r } { \omega ^ { 1 } = \displaystyle \sum _ { i = 1 } ^ { 2 n } \widehat { w } _ { i } \mathtt { d } w _ { i } + \overline { { H } } ( w , t ) \mathtt { d } t , \quad \mathrm { t h e n } } \\ { \mathtt { d } \omega ^ { 1 } = \displaystyle \sum _ { i , j = 1 } ^ { 2 n } \frac { \partial \widehat { w } _ { i } } { \partial w _ { j } } \mathtt { d } w _ { j } \wedge \mathtt { d } w _ { i } + \displaystyle \sum _ { i = 1 } ^ { 2 n } \frac { \partial \widehat { w } _ { i } } { \partial t } \mathtt { d } t \wedge \mathtt { d } w _ { i } + \displaystyle \sum _ { i = 1 } ^ { 2 n } \frac { \partial \overline { { H } } } { \partial w _ { i } } \mathtt { d } w _ { i } \wedge \mathtt { d } t } \\ { = \displaystyle \sum _ { i < j } \Big ( \frac { \partial \widehat { w } _ { i } } { \partial w _ { j } } - \frac { \partial \widehat { w } _ { j } } { \partial w _ { i } } \Big ) \mathtt { d } w _ { j } \wedge \mathtt { d } w _ { i } + \displaystyle \sum _ { i = 1 } ^ { 2 n } \Big ( \frac { \partial \widehat { w } _ { i } } { \partial t } - \frac { \partial \overline { { H } } } { \partial w _ { i } } \Big ) \mathtt { d } t \wedge \mathtt { d } w _ { i } . } \end{array}
$$

Since $N ( w , t ) = f _ { w } ( w , t ) = \frac { \partial \widehat { w } } { \partial w }$ is symmetric, the first term of (3.9) is zero.

Notice that $\widehat { z } = G ( z , t ) = \overset { } { g } ( M _ { 0 } z , t )$ ,

$$
\frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = \frac { \mathrm { d } ~ g ( M _ { 0 } z , t ) } { \mathrm { d } ~ t } = J ^ { - 1 } \nabla { \cal H } ( G ( z , t ) ) .
$$

So $G ( z , t )$ is the solution of the following initial-value problem:

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = J ^ { - 1 } \nabla H ( \widehat { z } ) , } \\ { \widehat { z } ( 0 ) = M _ { 0 } z . } \end{array} \right.
$$

Therefore, from the equations

$$
\widehat { w } = A _ { \alpha } G ( z , t ) + B _ { \alpha } z , \quad w = C _ { \alpha } G ( z , t ) + D _ { \alpha } z ,
$$

it follows that

$$
\frac { \mathrm { d } \widehat { w } } { \mathrm { d } t } = A _ { \alpha } J ^ { - 1 } \nabla H ( \widehat { z } ) , ~ \frac { \mathrm { d } w } { \mathrm { d } t } = C _ { \alpha } J ^ { - 1 } \nabla H ( \widehat { z } ) .
$$

Since $\frac { \mathrm { d } \widehat { w } } { \mathrm { d } t } = \frac { \partial \widehat { w } } { \partial w } \frac { \mathrm { d } w } { \mathrm { d } t } + \frac { \partial \widehat { w } } { \partial t }$ , combining these equations, we obtain

$$
\frac { \partial \widehat { w } } { \partial t } = \left( A _ { \alpha } - \frac { \partial \widehat { w } } { \partial w } C _ { \alpha } \right) J ^ { - 1 } \nabla H ( \widehat { z } ) .
$$

On the other hand,

$$
\begin{array} { r l } { \nabla _ { w } \overline { { H } } ( w , t ) ~ = ~ \left( \overline { { H } } _ { w } ( w , t ) \right) ^ { \mathrm { T } } = \mu \Big ( - { H } _ { \widehat { z } } \cdot \Big ( A ^ { \alpha } \frac { \partial \widehat { w } } { \partial w } + B ^ { \alpha } \Big ) \Big ) ^ { \mathrm { T } } } \\ { = ~ - \mu \Big ( ( B ^ { \alpha } ) ^ { \mathrm { T } } + \Big ( \frac { \partial \widehat { w } } { \partial w } \Big ) ^ { \mathrm { T } } ( A ^ { \alpha } ) ^ { \mathrm { T } } \Big ) \nabla H ( \widehat { z } ) } \\  { ~ = ~ \left( A _ { \alpha } J ^ { - 1 } - \frac { \partial \widehat { w } } { \partial w } C _ { \alpha } J ^ { - 1 } \right) \nabla H ( \widehat { z } ) ~ } & { \big ( \mathrm { b y ~ } ( 2 . 5 ) ~ \mathrm { a n d } ~ N \in S m ( 2 n ) \big ) } \\ { { ~ = ~ \frac { \partial \widehat { w } } { \partial t } . } } \end{array}
$$

So $1 \omega ^ { 1 } = 0$ . By Poincare lemma, there exists, in some neighborhood of ´ $\mathbf { R } ^ { 2 n + 1 }$ , a scalar function $\phi ( w , t )$ , such that

$$
\omega ^ { 1 } = \widehat { w } \mathrm { d } w + \overline { { H } } \mathrm { d } t = \mathrm { d } \phi ( w , t ) ,
$$

i.e.,

$$
\begin{array} { r l } & { f ( w , t ) = \nabla _ { w } \phi ( w , t ) , } \\ & { \displaystyle \frac { \partial } { \partial t } \phi ( w , t ) = - \mu H \big ( A ^ { \alpha } \nabla _ { w } \phi _ { \alpha , H } ( w , t ) + B ^ { \alpha } w \big ) . } \end{array}
$$

Therefore, the theorem is completed.

Examples of generating functions are:

$$
\begin{array} { l l } { { \alpha = \left[ \begin{array} { c c c c } { { O } } & { { O } } & { { - I _ { n } } } & { { O } } \\ { { I _ { n } } } & { { O } } & { { O } } & { { O } } \\ { { O } } & { { O } } & { { O } } & { { I _ { n } } } \\ { { O } } & { { I _ { n } } } & { { O } } & { { O } } \end{array} \right] , } } & { { \mu = 1 , \quad M _ { 0 } = J , \quad \left| C _ { \alpha } M _ { 0 } + D _ { \alpha } \right| \ne 0 ; } } \\ { { w = \left[ \begin{array} { c } { { q } } \\ { { \hat { q } } } \end{array} \right] , } } & { { \phi = \phi ( { q } , \hat { q } , t ) ; } } \\ { { \widehat w = \left[ \begin{array} { c } { { - p } } \\ { { \hat { p } } } \end{array} \right] = \left[ \begin{array} { c } { { \phi _ { q } } } \\ { { \phi _ { \hat { q } } } } \end{array} \right] , } } & { { \phi _ { t } = - H ( \phi _ { \hat { q } } , \hat { q } ) . } } \end{array}
$$

This is the generating function and H.J. equation of the first kind.

$$
\begin{array} { r l } & { \alpha = \left[ \begin{array} { l l l } { O } & { O } & { - I _ { n } } & { O } \\ { O } & { - I _ { n } } & { O } & { O } \\ { O } & { O } & { O } & { I _ { n } } \\ { I _ { n } } & { O } & { O } & { O } \end{array} \right] , \quad \mu = 1 , ~ M _ { 0 } = I , ~ | C _ { \alpha } M _ { 0 } + D _ { \alpha } | \neq 0 ; } \\ & { w = \left[ \begin{array} { l } { q } \\ { \hat { p } } \end{array} \right] , \quad \quad \quad \quad \quad \quad \quad \quad \phi = \phi ( q , \hat { p } , t ) ; } \\ & { \hat { w } = - \left[ \begin{array} { l } { p } \\ { \hat { q } } \end{array} \right] = \left[ \begin{array} { l } { \phi _ { q } } \\ { \phi _ { \hat { p } } } \end{array} \right] , \quad \quad \quad \quad \quad \phi _ { t } = - H ( \hat { p } , - \phi _ { \hat { p } } ) . } \end{array}
$$

This is the generating function and H.J. equation of the second kind.

$$
\begin{array} { r l r l } & { \alpha = \left[ \begin{array} { l l } { - J _ { 2 n } } & { J _ { 2 n } } \\ { \frac { 1 } { 2 } I _ { 2 n } } & { \frac { 1 } { 2 } I _ { 2 n } } \end{array} \right] , \quad } & & { \mu = 1 , \quad M _ { 0 } = I , \quad | C _ { \alpha } M _ { 0 } + D _ { \alpha } | \ne 0 ; } \\ & { w = \frac { 1 } { 2 } ( z + \widehat { z } ) , \quad } & & { \phi = \phi ( w , t ) ; } \\ & { \widehat { w } = J ( z - \widehat { z } ) = \nabla \phi , \quad } & & { \phi _ { t } = - H \Bigl ( w - \frac { 1 } { 2 } J ^ { - 1 } \nabla \phi \Bigr ) . } \end{array}
$$

This is the Poincare’s generating function ´ $[ \mathrm { W e i } 7 2 ]$ and H.J. equation.

If the Hamiltonian function $H ( z )$ depends analytically on $z$ then we can derive the explicit expression of the corresponding generating function via recursions .

Theorem 3.2. Let $H ( z )$ depend analytically on $z$ . Then $\phi _ { \alpha , H } ( w , t )$ is expressible as a convergent power series in $t$ for sufficiently small $| t |$ , with recursively determined coefficients:

$$
\begin{array} { r c l } { { \displaystyle \phi ( w , t ) ~ = ~ \sum _ { k = 0 } ^ { \infty } \phi ^ { ( k ) } ( w ) t ^ { k } , } } \\ { { \displaystyle \phi ^ { ( 0 ) } ( w ) ~ = ~ \frac { 1 } { 2 } w ^ { \mathrm { T } } N _ { 0 } w , ~ N _ { 0 } = ( A _ { \alpha } M _ { 0 } + B _ { \alpha } ) ( C _ { \alpha } M _ { 0 } + D _ { \alpha } ) ^ { - 1 } , } } \\ { { \displaystyle \phi ^ { ( 1 ) } ( w ) ~ = ~ - \mu ( \alpha ) H ( E _ { 0 } w ) , } } \\ { { E _ { 0 } ~ = ~ A ^ { \alpha } N _ { 0 } + B ^ { \alpha } = M _ { 0 } ( C _ { \alpha } M _ { 0 } + D _ { \alpha } ) ^ { - 1 } . } } \end{array}
$$

If $k \geq 1$ ,

$$
\begin{array} { r c l } { \displaystyle \phi ^ { ( k + 1 ) } ( w ) ~ = } & { \displaystyle - \frac { \mu ( \alpha ) } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { \tiny i _ { 1 } , \cdots , i _ { m } = 1 \atop j _ { l } \geq 1 } ^ { 2 n } \sum _ { \tiny j _ { l } \geq 1 } { H _ { z _ { i _ { 1 } } , \cdots , z _ { i _ { m } } } ( E _ { 0 } w ) } } \\ { \displaystyle } & & { \displaystyle \cdot ( A ^ { \alpha } \nabla \phi ^ { ( j _ { 1 } ) } ) _ { i _ { 1 } } , \cdot \cdot \cdot , ( A ^ { \alpha } \nabla \phi ^ { ( j _ { m } ) } ) _ { i _ { m } } , } \end{array}
$$

where $H _ { z _ { i _ { 1 } } , \cdots , z _ { i _ { m } } } ( E _ { 0 } w )$ is the $m$ -th partial derivative of $H ( z )$ w.r.t. $z _ { i _ { 1 } } , \cdots , z _ { i _ { m } }$ , ievaluated at $z = E _ { 0 } w$ and $\left( A ^ { \alpha } \nabla \phi ^ { ( j _ { l } ) } ( w ) \right) _ { i _ { l } }$ is the $i _ { l }$ m-th component of the column vector $A ^ { \alpha } \nabla \phi ^ { ( j _ { l } ) } ( w )$ .

Proof. Under our assumption, the generating function $\phi _ { \alpha , H } ( w , t )$ depends analytically on $w$ and $t$ in some neighborhood of $\mathbf { R } ^ { 2 n }$ and for small $| t |$ . Expand it as a power series as follows:

$$
\phi ( w , t ) = \sum _ { k = 0 } ^ { \infty } \phi ^ { ( k ) } ( w ) t ^ { k } .
$$

Differentiating it with respect to $w$ and $t$ , we get

$$
\begin{array} { r c l } { { \displaystyle \nabla \phi ( w , t ) ~ = ~ \sum _ { k = 0 } ^ { \infty } \nabla \phi ^ { ( k ) } ( w ) t ^ { k } , } } \\ { { \displaystyle \frac { \partial } { \partial t } \phi ( w , t ) ~ = ~ \sum _ { k = 0 } ^ { \infty } ( k + 1 ) t ^ { k } \phi ^ { ( k + 1 ) } ( w ) . } } \end{array}
$$

By (3.15),

$$
\nabla \phi ^ { ( 0 ) } ( w ) = \nabla \phi ( w , 0 ) = f ( w , 0 ) = N _ { 0 } w .
$$

So we can take $\phi ^ { ( 0 ) } ( w ) = \frac { 1 } { 2 } w ^ { \mathrm { T } } N _ { 0 } w$ . We denote ${ \cal E } _ { 0 } = A ^ { \alpha } N _ { 0 } + B ^ { \alpha } .$ . Then

$$
A ^ { \alpha } \nabla \phi ( w , t ) + B ^ { \alpha } w = E _ { 0 } w + \sum _ { k = 1 } ^ { \infty } A ^ { \alpha } \nabla \phi ^ { ( k ) } ( w ) t ^ { k } .
$$

Substitutes it in $H \big ( A ^ { \alpha } \nabla \phi ( w , t ) + B ^ { \alpha } w \big )$ and expanding at $z = E _ { 0 } w$ , we get

$$
\begin{array} { r l } & { H ( A ^ { \alpha } \nabla \phi ( w , t ) + B ^ { \alpha } w ) } \\ & { \quad = H \left( { E _ { 0 } w } + \displaystyle \sum _ { k = 1 } ^ { \infty } A ^ { \alpha } \nabla \phi ^ { ( k ) } ( w ) t ^ { k } \right) } \\ & { \quad = H ( { E _ { 0 } w } ) + \displaystyle \sum _ { m = 1 } ^ { \infty } \frac { 1 } { m ! } \sum _ { i _ { 1 } , \cdots , i _ { m } = 1 } ^ { 2 n } \sum _ { j _ { 1 } , \cdots , j _ { m } = 1 } ^ { \infty } t ^ { j _ { 1 } + \cdots + j _ { m } } H _ { z _ { i _ { 1 } } , \cdots , z _ { i _ { m } } } } \end{array}
$$

$$
\begin{array} { c } { { \underbrace { \phantom { \left( L ^ { \alpha } \right) } m = 1 } m ! \bigcup _ { i _ { 1 } , \cdots , i _ { m } = 1 } j _ { 1 } , \cdots , j _ { m } = 1 } } \\ { { \cdot ( E _ { 0 } w ) ( A ^ { \alpha } \nabla \phi ^ { \left( j _ { 1 } \right) } ( w ) ) _ { i _ { 1 } } \cdot \cdot \cdot ( A ^ { \alpha } \nabla \phi ^ { \left( j _ { m } \right) } ( w ) ) _ { i _ { m } } } } \end{array}
$$

$$
= H ( E _ { 0 } w ) + \sum _ { m = 1 } ^ { \infty } { \frac { 1 } { m ! } } \sum _ { { i _ { 1 } , \cdots , i _ { m } } = 1 } ^ { 2 n } \sum _ { k \geq m } t ^ { k } \sum _ { { j _ { 1 } + \cdots + j _ { m } } = k j _ { l } \geq 1 } H _ { z _ { i _ { 1 } } , \cdots , z _ { i _ { m } } }
$$

$$
\cdot ( E _ { 0 } w ) ( A ^ { \alpha } \nabla \phi ^ { ( j _ { 1 } ) } ( w ) ) _ { i _ { 1 } } \cdot \cdot \cdot ( A ^ { \alpha } \nabla \phi ^ { ( j _ { m } ) } ( w ) ) _ { i _ { m } }
$$

$$
\begin{array} { r l } & { = H ( E _ { 0 } w ) + \displaystyle \sum _ { k = 1 } ^ { \infty } t ^ { k } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { \substack { i _ { 1 } , \cdots , i _ { m } = 1 j _ { 1 } + \cdots + j _ { m } = k j _ { l } \geq 1 } } ^ { 2 n } H _ { z _ { i _ { 1 } } , \cdots , z _ { i _ { m } } } } \\ & { \quad \cdot ( E _ { 0 } w ) ( A ^ { \alpha } \nabla \phi ^ { ( j _ { 1 } ) } ) _ { i _ { 1 } } \cdot \cdot \cdot ( A ^ { \alpha } \nabla \phi ^ { ( j _ { m } ) } ) _ { i _ { m } } . } \end{array}
$$

Substituting this formula into the R.H.S. of (3.4), and (3.5) into the L.H.S. of (3.4), then comparing the coefficients of $t ^ { k }$ on both sides, we obtain the recursions Equations (3.13) and (3.14).

In the next section when we use generating functions $\phi _ { \alpha , H }$ to construct difference schemes we always assume $M _ { 0 } = I$ . For the sake of convenience, we restate Theorem 3.1 and Theorem 3.2 as follows.

Theorem 3.3. Let $\alpha \in C S p ( \tilde { J } _ { 4 n } , J _ { 4 n } )$ . Let $z  { \widehat { z } } = g ( z , t )$ be the phase flow of the Hamiltonian system (3.1) with Jacobian $M ( z , t ) = g _ { z } ( z , t )$ . If

$$
| C _ { \alpha } + D _ { \alpha } | \neq 0 ,
$$

then there exists, for sufficiently small $| t |$ and in (some neighborhood of) $\mathbf { R } ^ { 2 n }$ , a timedependent gradient map $w \to \widehat { w } = f ( w , t )$ with Jacobian $N ( w , t ) = f _ { w } ( w , t ) \in$ $S m ( 2 n )$ satisfying the transversality condition (1.13) and a time-dependent generating function $\phi _ { \alpha , H } ( w , t ) = \phi ( w , t )$ such that

$$
\begin{array} { r l } & { f ( w , t ) = \nabla \phi ( w , t ) ; } \\ & { \frac { \partial \phi } { \partial t } = - \mu H ( A ^ { \alpha } \nabla \phi ( w , t ) + B ^ { \alpha } w ) ; } \\ & { A _ { \alpha } g ( z , t ) + B _ { \alpha } z \equiv f ( C _ { \alpha } g ( z , t ) + D _ { \alpha } z , t ) } \\ & { \qquad \equiv \nabla \phi ( C _ { \alpha } g ( z , t ) + D _ { \alpha } z , t ) ; } \\ & { N = \sigma _ { \alpha } ( M ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } ; } \\ & { M = \sigma _ { \alpha ^ { - 1 } } ( N ) = ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } . } \end{array}
$$

Theorem 3.4. Let $H ( z )$ depend analytically on $z$ . Then $\phi _ { \alpha , H } ( w , t )$ is expressible as a convergent power series in t for sufficiently small $| t |$ , with the recursively determined coefficients:

$$
\begin{array} { l l } { \displaystyle \phi ( w , t ) ~ = ~ \sum _ { k = 0 } ^ { \infty } \phi ^ { ( k ) } ( w ) t ^ { k } ; } \\ { \displaystyle \phi ^ { ( 0 ) } ( w ) ~ = ~ \frac { 1 } { 2 } w ^ { \mathrm { T } } N _ { 0 } w , } & { N _ { 0 } = ( A _ { \alpha } + B _ { \alpha } ) ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } ; } \\ { \displaystyle \phi ^ { ( 1 ) } ( w ) ~ = ~ - \mu ( \alpha ) H ( E _ { 0 } w ) , } & { E _ { 0 } = ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } . } \end{array}
$$

If $k \geq 1$ ,

$$
\begin{array} { r c l } { \displaystyle \phi ^ { ( k + 1 ) } ( w ) ~ = } & { \displaystyle - \frac { \mu ( \alpha ) } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { \tiny i _ { 1 } , \cdots , i _ { m } = 1 } ^ { 2 n } \sum _ { \tiny j _ { 1 } + \cdots + j _ { m } = k } H _ { z _ { i _ { 1 } } , \cdots , z _ { i _ { m } } } ( E _ { 0 } w ) } \\ { \displaystyle } & & { \displaystyle \cdot ( A ^ { \alpha } \nabla \phi ^ { ( j _ { 1 } ) } ) _ { i _ { 1 } } \cdot \cdot \cdot ( A ^ { \alpha } \nabla \phi ^ { ( j _ { m } ) } ) _ { i _ { m } } . } \end{array}
$$

# 5.4 Construction of Canonical Difference Schemes

In this section, we consider the construction of canonical difference schemes for the Hamiltonian system (3.1). By Theorem 3.1, for a given time-dependent scalar function $\psi ( w , t ) : \mathbf { R } ^ { 2 n } \times \mathbf { R }  \mathbf { R }$ , we can get a time-dependent canonical map $\tilde { g } ( z , t )$ . If $\psi ( w , t )$ approximates some generating function $\phi _ { \alpha , H } ( w , t )$ of the Hamiltonian system (3.1), then $\tilde { g } ( z , t )$ approximates the phase flow $g ( z , t )$ . Then, fixing $t$ as a time step, we can get a difference scheme —the canonical difference scheme—whose transition from one time-step to the next is canonical. By Theorem 3.4, the generating functions $\phi ( w , t )$ can be expressed as a power series. So a natural way to approximate $\phi ( w , t )$ is to take the truncation of the series. More precisely, we have:

Theorem 4.1. Using Theorems 3.3 and 3.4, for sufficiently small $\tau > 0$ as the timestep, we define

$$
\psi ^ { ( m ) } ( w , \tau ) = \sum _ { i = 0 } ^ { m } \phi ^ { ( i ) } ( w ) \tau ^ { i } , \quad m = 1 , 2 , \cdot \cdot \cdot .
$$

Then the gradient mapping

$$
w  \widehat { w } = \widetilde { f } ( w , \tau ) = \nabla \psi ^ { ( m ) } ( w , \tau )
$$

defines an implicit canonical difference scheme $z = z ^ { k } \to z ^ { k + 1 } = { \widehat { z } }$

$$
A _ { \alpha } z ^ { k + 1 } + B _ { \alpha } z ^ { k } = \nabla \psi ^ { ( m ) } ( C _ { \alpha } z ^ { k + 1 } + D _ { \alpha } z ^ { k } , \tau )
$$

of m-th order of accuracy.

Proof. Since $\psi ^ { ( m ) } ( w , 0 ) = \phi ( w , 0 )$ , so $\psi _ { w w } ^ { ( m ) } ( w , 0 ) = \phi _ { w w } ( w , 0 ) = f _ { w } ( w , 0 ) =$ $N ( w , 0 )$ satisfies the transversality condition (1.13), i.e., $\lvert C ^ { \alpha } N ( w , 0 ) + D ^ { \alpha } \rvert \ne 0$ . Thus for sufficiently small $\tau$ and in some neighborhood of $\mathbf { R } ^ { 2 n }$ , $N ^ { ( m ) } ( w , \tau ) ~ =$ $\psi _ { w w } ^ { ( m ) } ( w , \tau )$ satisfies the transversality condition (1.13), i.e., $\left| C ^ { \alpha } N ^ { ( m ) } ( w , \tau ) + D ^ { \alpha } \right| \neq$ 0. By Theorem 4.1, the gradient mapping $w  \widehat { w } = \widetilde { f } ( w , \tau ) = \nabla \psi ^ { ( m ) } ( w , \tau )$ defines implicitly a time-dependent canonical mapping $z  { \widehat { z } } = \widetilde { g } ( z , \tau )$ by the equation

$$
A _ { \alpha } \widehat { z } + B _ { \alpha } z = \nabla \psi ^ { ( m ) } ( C _ { \alpha } \widehat { z } + D _ { \alpha } z , \tau ) .
$$

Thus, the equation

$$
A _ { \alpha } z ^ { k + 1 } + B _ { \alpha } z ^ { k } = \nabla \psi ^ { ( m ) } ( C _ { \alpha } z ^ { k + 1 } + D _ { \alpha } z ^ { k } , \tau )
$$

is an implicit canonical difference scheme.

Since $\psi ^ { ( m ) } ( w , \tau )$ is the $m$ -th order approximation to $\phi ( w , \tau )$ , so is $\tilde { f } ( w , \tau ) =$ $\nabla \psi ^ { ( m ) } ( w , \tau )$ to $f ( w , \tau )$ , it follows that the canonical difference scheme given by (4.3) is of $m$ -th order of accuracy. $\blacktriangle$

Therefore, for every $\alpha \in C S p ( \widetilde { J } _ { 4 n } , J _ { 4 n } )$ , we can construct a series of symplectic schemes for arbitrary order accuracy.

Examples of the canonical difference scheme:

Type (I). Constructing symplectetic scheme by the first kind of the generating function. From Theorem 3.2, as $\mu = 1$ ,

$$
\begin{array} { r l } { \phi ^ { ( 0 ) } ( w ) } & { = \frac { 1 } { 2 } w ^ { T } N _ { 0 } w , \quad \mathscr { N } _ { 0 } = \left( A _ { 0 } + B _ { \alpha } \right) ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } , } \\ { \phi ^ { ( 1 ) } ( w ) } & { = - H ( E _ { \alpha } w ) , \quad E _ { 0 } = ( C _ { \alpha } + D _ { \alpha } ) ^ { - 1 } , } \\ { \phi ^ { ( 2 ) } ( w ) } & { = \frac { 1 } { 2 } ( \nabla H ) ^ { T } A ^ { \alpha } \nabla _ { 0 } ^ { T } ( \nabla H ) ( E _ { \alpha } w ) , } \\ { \phi ^ { ( 3 ) } ( w ) } & { = - \frac { 1 } { 3 } ( \nabla H ) ^ { T } A ^ { \alpha } \nabla _ { 0 } \nabla w ^ { ( 0 ) } ) - \frac { 1 } { 6 } ( A ^ { \alpha } \nabla _ { 0 } ^ { ( \alpha ) } ) ^ { 1 } ) ^ { T } H _ { \alpha \alpha } ( A ^ { \alpha } \nabla _ { 0 } ^ { ( 1 ) } ) } \\ & { = - \frac { 1 } { 6 } ( \nabla H ) ^ { T } A ^ { \alpha } ( E _ { 0 } ^ { T } H _ { \alpha } A ^ { \alpha } E _ { 0 } ^ { T } \nabla H + E _ { 0 } ^ { T } H _ { \alpha } \cdot E _ { 0 } A ^ { \alpha } ) ^ { T } \nabla H ) } \\ & { \quad - \frac { 1 } { 6 } ( \nabla H ) ^ { T } E _ { 0 } A ^ { \alpha } \nabla H _ { \alpha } A ^ { \alpha } E _ { 0 } ^ { T } \nabla H } \\ & { = - \frac { 1 } { 6 } ( \nabla H ) ^ { T } \nabla ^ { T } A ^ { \alpha } E _ { 0 } ^ { T } H _ { \alpha } ( A ^ { \alpha } E _ { 0 } ^ { T } \nabla ^ { T } H } \\ & { \quad + ( \nabla H ) ^ { T } E _ { 0 } A ^ { \alpha } \nabla H _ { \alpha } A ^ { \alpha } E _ { 0 } ^ { T } \nabla H ) } \end{array}
$$

Here we use the matrix notation instead of the component notation in Theorem 3.4. $H _ { z z }$ denotes the Hessian matrix of $H$ , and all derivatives of $H$ are evaluated at $z =$ $E _ { 0 } w$ .

Type (II). Constructing symplectetic scheme by the second kind of the generating function

$$
\begin{array} { r l } & { \boldsymbol { \alpha } = \left[ \begin{array} { c c c c } { \boldsymbol { O } } & { \boldsymbol { O } } & { - I _ { n } } & { \boldsymbol { O } } \\ { \boldsymbol { O } } & { - I _ { n } } & { \boldsymbol { O } } & { \boldsymbol { O } } \\ { \boldsymbol { O } } & { \boldsymbol { O } } & { \boldsymbol { O } } & { I _ { n } } \\ { I _ { n } } & { \boldsymbol { O } } & { \boldsymbol { O } } & { \boldsymbol { O } } \end{array} \right] , \quad \boldsymbol { \alpha } ^ { \mathrm { T } } = \boldsymbol { \alpha } ^ { - 1 } = \left[ \begin{array} { c c c c } { \boldsymbol { O } } & { \boldsymbol { O } } & { \boldsymbol { O } } & { I _ { n } } \\ { \boldsymbol { O } } & { - I _ { n } } & { \boldsymbol { O } } & { \boldsymbol { O } } \\ { - I _ { n } } & { \boldsymbol { O } } & { \boldsymbol { O } } & { \boldsymbol { O } } \\ { \boldsymbol { O } } & { \boldsymbol { O } } & { I _ { n } } & { \boldsymbol { O } } \end{array} \right] . } \\ & { \boldsymbol { w } = \left[ \begin{array} { c } { \boldsymbol { q } } \\ { \widehat { \boldsymbol { p } } } \end{array} \right] , \quad \widehat { \boldsymbol { w } } = - \left[ \begin{array} { c } { \boldsymbol { p } } \\ { \widehat { \boldsymbol { q } } } \end{array} \right] , } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle N _ { 0 } = - \Bigm [ \begin{array} { c c } { { \cal O } } & { { \cal I } } \\ { { \cal I } } & { { \cal O } } \end{array} \Bigm ] , \quad E _ { 0 } = \Bigm [ \begin{array} { c c } { { \cal O } } & { { \cal I } } \\ { { \cal I } } & { { \cal O } } \end{array} \Bigm ] , \quad A ^ { \alpha } E _ { 0 } ^ { \mathrm { T } } = - \Bigm [ \begin{array} { c c } { { \cal O } } & { { \cal O } } \\ { { \cal I } } & { { \cal O } } \end{array} \Bigm ] , } } \\ { { \displaystyle \phi ^ { ( 1 ) } ( w ) = - { \cal H } ( \widehat { p } , q ) , } } \\ { { \displaystyle \phi ^ { ( 2 ) } ( w ) = - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } ( H _ { q _ { i } } H _ { p _ { i } } ) ( \widehat { p } , q ) , } } \\ { { \displaystyle \phi ^ { ( 3 ) } ( w ) = - \frac { 1 } { 6 } \sum _ { i , j = 1 } ^ { n } ( H _ { p _ { i } p _ { j } } H _ { q _ { i } } H _ { q _ { j } } + H _ { q _ { i } q _ { j } } H _ { p _ { i } } H _ { p _ { j } } + H _ { q _ { i } p _ { j } } H _ { p _ { i } } H _ { q _ { j } } ) . } } \end{array}
$$

where $H ( z ) = H ( p _ { 1 } , \cdots , p _ { n } , q _ { 1 } , \cdots , q _ { n } ) , H _ { z _ { i } } = { \frac { \partial H } { \partial z _ { i } } } .$

a. The first order scheme.

$$
\psi ^ { ( 1 ) } ( w , \tau ) = \phi ^ { ( 0 ) } ( w ) + \tau \phi ^ { ( 1 ) } ( w ) .
$$

The equation $\widehat { w } = \nabla \psi ^ { ( 1 ) } ( w , \tau )$ defines a first order canonical difference scheme

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - \tau H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) , } \\ { q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + \tau H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) , } \end{array} \right. \quad i = 1 , \cdots , n . } \end{array}
$$

When $H$ is separable, $H = U ( p ) + V ( q )$ . So

$$
H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) = V _ { q _ { i } } ( q ^ { k } ) , \quad H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) = U _ { p _ { i } } ( p ^ { k + 1 } ) .
$$

At this time, (4.4) becomes

$$
\left\{ \begin{array} { l l } { p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - \tau V _ { q _ { i } } ( q ^ { k } ) , } \\ { q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + \tau U _ { p _ { i } } ( p ^ { k + 1 } ) , } \end{array} \right. \quad i = 1 , \cdots , n .
$$

Evidently, (4.4) is an explicit difference scheme of 1-st order of accuracy. If we set $q$ ’s at half-integer times $t = \big ( k + \frac 1 2 \big ) \tau$ , then (4.4) becomes

$$
\left\{ \begin{array} { l l } { p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - \tau V _ { q _ { i } } ( q ^ { k + \frac { 1 } { 2 } } ) , } \\ { q _ { i } ^ { k + \frac { 1 } { 2 } + 1 } = q _ { i } ^ { k + \frac { 1 } { 2 } } + \tau U _ { p _ { i } } ( p ^ { k + 1 } ) , } \end{array} \right. \quad i = 1 , \cdots , n .
$$

(4.6) is a staggered explicit scheme of 2-nd order accuracy.

b. The second order scheme.

$$
\psi ^ { ( 2 ) } ( w , \tau ) = \psi ^ { ( 1 ) } ( w ) + \tau ^ { 2 } \phi ^ { ( 2 ) } ( w ) .
$$

The induced gradient map is

$$
\boldsymbol { \widehat { w } } = \nabla _ { \boldsymbol { w } } \psi ^ { ( 2 ) } = - \left[ \begin{array} { l } { \boldsymbol { \widehat { p } } } \\ { \boldsymbol { q } } \end{array} \right] - \tau \left[ \begin{array} { l } { \nabla _ { \boldsymbol { q } } H } \\ { \nabla _ { \boldsymbol { p } } H } \end{array} \right] - \frac { \tau ^ { 2 } } { 2 } \left[ \begin{array} { l } { \nabla _ { \boldsymbol { q } } \Big ( \sum _ { i = 1 } ^ { n } H _ { q _ { i } } H _ { p _ { i } } \Big ) } \\ { \nabla _ { \boldsymbol { p } } \Big ( \sum _ { i = 1 } ^ { n } H _ { q _ { i } } H _ { p _ { i } } \Big ) } \end{array} \right] .
$$

So the second order scheme is

$$
\left\{ \begin{array} { l l } { \displaystyle p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - \tau H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) - \frac { \tau ^ { 2 } } { 2 } \Big ( \sum _ { j = 1 } ^ { n } H _ { q _ { j } } H _ { p _ { j } } \Big ) _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) , } & \\ { \displaystyle q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + \tau H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) + \frac { \tau ^ { 2 } } { 2 } \Big ( \sum _ { j = 1 } ^ { n } H _ { q _ { j } } H _ { p _ { j } } \Big ) _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) , } & \end{array} \right. \quad i = 1 , \cdots , n
$$

This scheme is already implicit even when $H ( z )$ is separable.

c. The third order scheme is

$$
\begin{array} { r l } { p _ { i } ^ { k + 1 } \ = \ } & { p _ { i } ^ { k } - \tau H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) - \displaystyle \frac { \tau ^ { 2 } } { 2 } \sum _ { j = 1 } ^ { n } \big ( H _ { q _ { j } } H _ { p _ { j } } \big ) _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) } \\ & { \quad - \displaystyle \frac { \tau ^ { 3 } } { 6 } \sum _ { l , j = 1 } ^ { n } \big ( H _ { p \nu _ { j } } H _ { q _ { l } } H _ { q _ { j } } + H _ { q _ { i } q _ { j } } H _ { p _ { l } } H _ { p _ { j } } + H _ { p \imath q _ { j } } H _ { q _ { l } } H _ { p _ { j } } \big ) _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } ) , } \\ { q _ { i } ^ { k + 1 } \ = \ } & { q _ { i } ^ { k } + \tau H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) + \displaystyle \frac { \tau ^ { 2 } } { 2 } \sum _ { j = 1 } ^ { n } \big ( H _ { q _ { j } } H _ { p _ { j } } \big ) _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) } \\ & { \quad + \displaystyle \frac { \tau ^ { 3 } } { 6 } \sum _ { l , j = 1 } ^ { n } \big ( H _ { p \imath p _ { j } } H _ { q _ { l } } H _ { q _ { j } } + H _ { q \imath q _ { j } } H _ { p _ { l } } H _ { p _ { j } } + H _ { p \imath q _ { j } } H _ { q _ { l } } H _ { p _ { j } } \big ) _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } ) , } \end{array}
$$

where $i = 1 , \cdots , n$ .

Type (III). Constructing symplectetic scheme by Poincare type generating function ´

$$
\begin{array} { r l } & { \alpha = \left[ \begin{array} { l l } { - { \mathcal J } _ { { 2 3 } } } & { { \mathcal J } _ { { 2 3 } } } \\ { \frac { 1 } { 2 } { \mathcal J } _ { { 2 3 } } } & { \frac { 1 } { 2 } { \mathcal J } _ { { 2 1 } } } \end{array} \right] , ~ \alpha ^ { - 1 } = \left[ \begin{array} { l l } { \frac { 1 } { 2 } { \mathcal J } _ { { 2 0 } } } & { { \mathcal J } _ { { 2 1 } } } \\ { \frac { 1 } { 2 } { \mathcal J } _ { { 2 1 } } } & { { \mathcal J } _ { { 2 1 } } } \end{array} \right] , } \\ & { w = \frac { 1 } { 2 } ( \xi + \xi ) , ~ { \widehat { w } } = { \mathcal J } ( z - \xi ) , } \\ & { \mathcal { N } _ { { 4 0 } } = 0 , ~ { \mathcal { E } } _ { { 1 1 } } = { \mathcal { I } } , ~ A ^ { \alpha } { \mathcal { E } } _ { { 1 1 } } ^ { \top } + { \mathcal { E } } _ { { 4 1 } } A ^ { \alpha \mathcal { T } } = 0 , } \\ & { { \phi } ^ { ( 0 ) } = { \phi } ^ { ( 2 ) } = { \phi } ^ { ( 4 ) } = 0 , ~ } \\ & { { \phi } ^ { ( 1 ) } ( w ) = - { \mathcal { H } } \Big ( \frac { 1 } { 2 } ( \xi + \xi ) \Big ) , } \\ & { { \phi } ^ { ( 4 ) } ( w ) = \frac { 1 } { 2 4 } ( \nabla H ) ^ { \mathcal { T } } { \mathcal { H } } _ { z z } , { \mathcal { N } } H , } \\ & { { \phi } ^ { ( 0 ) } ( w , \tau ) = - \tau H , ~ } \\ & { { \psi } ^ { ( 4 ) } ( w , \tau ) = - \tau H + \frac { 3 } { 2 4 } ( \nabla H ) ^ { \Gamma } { \mathcal { H } } _ { z z } { \mathcal { N } } H . } \end{array}
$$

a. The second order scheme is

$$
J ( z - \widehat { z } ) = \widehat { w } = \nabla _ { w } \psi ^ { ( 2 ) } ( w , t ) = - \tau \nabla H \Big ( \frac { 1 } { 2 } ( z + \widehat { z } ) \Big ) ,
$$

i.e.,

$$
z ^ { k + 1 } = z ^ { k } + \tau J ^ { - 1 } \nabla H \Big ( \frac { 1 } { 2 } ( z ^ { k + 1 } + z ^ { k } ) \Big ) .
$$

It is centered Euler scheme.

b. The 4-th order scheme is

$$
\begin{array} { r } { J ( z - \widehat { z } ) = \widehat { w } = \nabla _ { w } \psi ^ { ( 4 ) } ( w , t ) = - \tau \nabla H \Big ( \frac { 1 } { 2 } ( z + \widehat { z } ) \Big ) + \frac { \tau ^ { 3 } } { 2 4 } \nabla _ { z } \big ( ( \nabla H ) ^ { \mathrm { T } } J H _ { z z } J \nabla H \big ) , } \end{array}
$$

i.e.,

$$
z ^ { k + 1 } = z ^ { k } + \tau J ^ { - 1 } \nabla H \left( { \frac { 1 } { 2 } } ( z ^ { k + 1 } + z ^ { k } ) \right) - { \frac { \tau ^ { 3 } } { 2 4 } } J ^ { - 1 } \nabla _ { z } \left( ( \nabla H ) ^ { \mathrm { T } } J H _ { z z } J \nabla H \right) \left( { \frac { 1 } { 2 } } ( z ^ { k + 1 } + z ^ { k } ) \right)
$$

It is not difficult to show that the generating function $\phi ( w , t )$ of type (III) is odd in $t$ . Hence, Theorem 4.1 leads to a family of canonical difference schemes of arbitrary even order accuracy.

Theorem 4.2. Let $\alpha = \left[ \begin{array} { c c } { { - J _ { 2 n } } } & { { J _ { 2 n } } } \\ { { \frac { 1 } { 2 } I _ { 2 n } } } & { { \frac { 1 } { 2 } I _ { 2 n } } } \end{array} \right] .$ For sufficiently small $\tau > 0$ as the timestep, we define

$$
\psi ^ { ( 2 m ) } ( w , \tau ) = \sum _ { i = 1 } ^ { m } \phi ^ { ( 2 i - 1 ) } ( w ) \tau ^ { 2 i - 1 } , \quad m = 1 , 2 , \cdots .
$$

Then the gradient map

$$
w \longrightarrow \widehat { w } = \tilde { f } ( w , \tau ) = \nabla \psi ^ { ( 2 m ) } ( w , \tau )
$$

defines implicitly canonical difference schemes $z = z ^ { k } \to z ^ { k + 1 } = { \widehat { z } } ,$

$$
z ^ { k + 1 } = z ^ { k } - J ^ { - 1 } \nabla \psi ^ { ( 2 m ) } \Big ( \frac { 1 } { 2 } ( z ^ { k + 1 } + z ^ { k } ) , \tau \Big )
$$

of $2 m$ -th order of accuracy. The case $m = 1$ is the Euler centered scheme.

Remark 4.3. We have following diagram commutes:

phase flow gradient transf. generating function

$$
\begin{array} { l c l } { { g ( z , t ) \xrightarrow { \alpha } } } & { { f ( w , t ) \xrightarrow { \nabla \phi } \phi ( w , t ) } } \\ { { \downarrow } } & { { } } & { { } } \\ { { \begin{array} { l } { { \begin{array} { r l r l } { { \begin{array} { r l r l r l } { \begin{array} { r l r l r l } { \begin{array} { r l r l r l } { \rho ( z , t ) \xrightarrow { \alpha } } & { f ( w , t ) } & { \overbrace { \nabla \phi } } & { } & { \phi ( w , t ) } & { } \\ { \qquad } & { } & { \qquad } & { } & { } \end{array} } } \\ { { g ^ { m } ( z , t ) \underbrace { \qquad \alpha ^ { - 1 } } } & { \overbrace { f } ( w , t ) \underbrace { \qquad \nabla \psi } } & { } & { \psi ( w ) } \end{array} } } } \end{array} } } } \end{array} \} _ { { o } ( t ^ { m + 1 } ) } } \\ { { g ^ { m } ( z , t ) \underbrace { \qquad \alpha ^ { - 1 } } } } & { { \widetilde { f } ( w , t ) \xrightarrow [ { \qquad \nabla \psi } ] { \begin{array} { r l r l } { \nabla \psi } & { } & { } & { } \\ { \qquad } & { } & { } \end{array} } } } \end{array} \end{array}
$$

# 5.5 Further Remarks on Generating Function

Now we want to construct unconditional Hamiltonian algorithms, i.e., they are symplectic for all Hamiltonian systems.

First we consider the one-leg weighted Euler schemes , i.e.,

$$
\widehat { z } = E _ { H , c } ^ { s } z : \quad \widehat { z } = z + s J H _ { z } ( c \widehat { z } + ( 1 - c ) z ) ,
$$

with real number $c$ being unconditionally symplectic if and only if $c = \frac { 1 } { 2 }$ , which corresponds to the centered Euler scheme

$$
\widehat { z } = z + s J H _ { z } \Big ( \frac { \widehat { z } + z } { 2 } \Big ) .
$$

These simple propositions illustrate a general situation: apart from some very rare exceptions, the vast majority of conventional schemes are non-symplectic. However, if we allow $c$ in (5.1) to be a real matrix of order $2 n$ , we get a far-reaching generalization: (5.1) is symplectic iff

$$
\boldsymbol c = \frac { 1 } { 2 } ( I _ { 2 n } + J _ { 2 n } { \boldsymbol B } ) , \quad { \boldsymbol B } ^ { \mathrm { T } } = { \boldsymbol B } , \quad \boldsymbol c ^ { \mathrm { T } } \boldsymbol J + J \boldsymbol c = { \boldsymbol J } .
$$

The simplest and important cases are[FQ91] :

$$
\begin{array} { l l l } { { C : \quad } } & { { c = \frac { 1 } { 2 } I _ { 2 n } , } } & { { \widehat { z } = z + s J H _ { z } \Big ( \frac { \widehat { z } + z } { 2 } \Big ) } } \\ { { \ } } & { { } } & { { } } \\ { { P : \quad } } & { { c = \left( \begin{array} { l l } { { I } } & { { O } } \\ { { O } } & { { O } } \end{array} \right) , } } & { { \widehat { p } } } & { { = p - s H _ { q } ( \widehat { p } , q ) , } } \\ { { \ } } & { { } } & { { \widehat { q } } } & { { = q + s H _ { p } ( \widehat { p } , q ) , } } \\ { { \ } } & { { } } & { { } } \\ { { Q : \quad } } & { { c = \left( \begin{array} { l l } { { O } } & { { O } } \\ { { O } } & { { I } } \end{array} \right) , } } & { { \widehat { p } } } & { { = p - s H _ { q } ( p , \widehat { q } ) , } } \\ { { \ } } & { { } } & { { \widehat { q } } } & { { = q + s H _ { p } ( p , \widehat { q } ) . } } \end{array}
$$

For $H ( p , q ) = \phi ( p ) + \psi ( q )$ , the above schemes $P$ and $Q$ reduce to explicit schemes. A matrix $\alpha$ of order $4 n$ is called a Darboux matrix if

$$
\begin{array} { l l } { { \alpha ^ { \mathrm { T } } J _ { 4 n } \alpha = \tilde { J } _ { 4 n } , } } & { { } } \\ { { J _ { 4 n } = \left( \begin{array} { c c } { { O } } & { { - I _ { 2 n } } } \\ { { I _ { 2 n } } } & { { O } } \end{array} \right) , } } & { { \tilde { J } _ { 4 n } = \left( \begin{array} { c c } { { J _ { 2 n } } } & { { O } } \\ { { O } } & { { - J _ { 2 n } } } \end{array} \right) , } } \\ { { \alpha = \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) , } } & { { \alpha ^ { - 1 } = \left( \begin{array} { c c } { { a _ { 1 } } } & { { b _ { 1 } } } \\ { { c _ { 1 } } } & { { d _ { 1 } } } \end{array} \right) . } } \end{array}
$$

Every Darboux matrix induces a (linear) fractional transform between symplectic and symmetric matrices

$$
\begin{array} { r l } & { S p ( 2 n ) \longrightarrow S m ( 2 n ) , } \\ { \sigma _ { \alpha } : } & { \quad \sigma _ { \alpha } ( S ) = ( a S + b ) ( c S + d ) ^ { - 1 } = A \quad \mathrm { f o r } \quad | c S + d | \ne 0 } \end{array}
$$

with the inverse transform $\sigma _ { \alpha } ^ { - 1 } = \sigma _ { \alpha ^ { - 1 } }$

$$
\sigma _ { \alpha } ^ { - 1 } : \quad \begin{array} { r l } & { S m ( 2 n ) \longrightarrow S p ( 2 n ) , } \\ & { \sigma _ { \alpha } ^ { - 1 } ( A ) = ( a _ { 1 } A + b _ { 1 } ) ( c _ { 1 } A + d _ { 1 } ) ^ { - 1 } = S \quad \mathrm { f o r } \quad | c _ { 1 } A + d _ { 1 } | \ne 0 , } \end{array}
$$

where $S p ( 2 n ) = \{ S \in G L ( 2 n , { \bf R } ) \mid S ^ { \mathbb { T } } J _ { 2 n } S = J _ { 2 n } \}$ is the group of symplectic matrices.

The above mechanism can be extended to generally non-linear operators on ${ \bf R } _ { 2 n }$ . Let totally symplectic operators be denoted by $S p D _ { 2 n }$ , and $s y m m ( 2 n )$ the totality of symmetric operators (not necessary one-one). Every $f \in s y m m ( 2 n )$ corresponds, at least locally, to a real function $\phi$ (unique up to a constant) such that $f$ is the gradient of $\phi : f ( w ) = \nabla \phi ( w )$ , where $\nabla \phi ( w ) = ( \phi _ { w _ { 1 } } ( w ) , \cdot \cdot \cdot , \phi _ { w _ { 2 n } } ( w ) ) = \phi _ { w } ( w )$ . Then we have

$$
\begin{array} { r l } & { \sigma _ { \alpha } : \quad S p D _ { 2 n } \longrightarrow s y m m \left( 2 n \right) , } \\ & { \sigma _ { \alpha } ( g ) = ( a \circ g + b ) \circ ( c \circ g + d ) ^ { - 1 } = \nabla \phi \quad \mathrm { f o r } \quad | c g _ { z } + d | \ne 0 } \end{array}
$$

or alternatively

$$
a g ( z ) + b z = ( \nabla \phi ) \big ( c g ( z ) + d z \big ) ,
$$

where $\phi$ is called the generating function of Darboux type $\alpha$ for the symplectic operator $g$ .[FQ91] Then

$$
\begin{array} { r l } & { \sigma _ { \alpha } ^ { - 1 } : \quad s y m m ( 2 n ) \longrightarrow S p D _ { 2 n } , } \\ & { \sigma _ { \alpha } ^ { - 1 } ( \nabla \phi ) = ( a _ { 1 } \circ \nabla \phi + b _ { 1 } ) \circ ( c _ { 1 } \circ \nabla \phi + d _ { 1 } ) ^ { - 1 } = g , } \\ & { \quad \quad \quad \mathrm { f o r } \quad | c _ { 1 } \phi _ { w w } + d _ { 1 } | \ne 0 } \end{array}
$$

or alternatively

$$
a _ { 1 } \nabla \phi ( w ) + b _ { 1 } ( w ) = g ( c _ { 1 } \nabla \phi ( w ) + d _ { 1 } w ) ,
$$

where $g$ is called the symplectic operator of Darboux type $\alpha$ for the generating function $\phi$ .

For the study of symplectic difference scheme, we may narrow down the class of Darboux matrices to the subclass of normal Darboux matrices, i.e., those satisfying $a + b = 0$ , $c + d = I _ { 2 n }$ . The normal Darboux matrices $\alpha$ can be characterized as

$$
\begin{array} { r l } { \alpha = \left( \begin{array} { c c } { a } & { b } \\ { c } & { d } \end{array} \right) = \left( \begin{array} { c c } { J } & { - J } \\ { c } & { I - c } \end{array} \right) , \quad c = \frac { 1 } { 2 } ( I + J B ) , \quad B ^ { \mathrm { T } } = B , } & { } \\ & { \alpha ^ { - 1 } = \left( \begin{array} { c c } { a _ { 1 } } & { b _ { 1 } } \\ { c _ { 1 } } & { d _ { 1 } } \end{array} \right) = \left( \begin{array} { c c } { ( c - I ) J } & { I } \\ { c J } & { I } \end{array} \right) . } \end{array}
$$

The fractional transform induced by a normal Darboux matrix establishes a 1-1 correspondence between symplectic operators near identity and symmetric operators near nullity. Then the determinantal conditions could be taken for granted. Those $B$ ’s listed in section 5 correspond to the most important normal Darboux matrices. For every Hamiltonian $H$ with its phase flow $e _ { H } ^ { t }$ and for every normal Darboux matrix $\alpha$ , we get the generating function $\phi ( w , t ) \stackrel {  } { = } \phi _ { H } ^ { t } ( w ) = \phi _ { H , \alpha } ^ { t } ( w )$ of normal Darboux type $\alpha$ for the phase flow of $H$ by

$$
\nabla \phi _ { H , \alpha } ^ { t } = ( J e _ { H } ^ { t } - J ) \circ ( c e _ { H } ^ { t } + I - c ) ^ { - 1 } \quad \mathrm { f o r ~ s m a l l } ~ | t | .
$$

$\phi _ { H , \alpha } ^ { t }$ satisfies the Hamilton–Jacobi equation

$$
\frac { \partial } { \partial t } \phi ( w , t ) = - H ( w + a _ { 1 } \nabla \phi ( w , t ) ) = - H ( w + c _ { 1 } \nabla \phi ( w , t ) )
$$

and can be expressed by Taylor series in $| t |$ :

$$
\phi ( w , t ) = \sum _ { k = 1 } ^ { \infty } \phi ^ { ( k ) } ( w ) t ^ { k } , \quad | t | \mathrm { s m a l l e n o u g h } .
$$

The coefficients can be determined recursively

$$
\begin{array} { r c l } { { \phi ^ { ( 1 ) } ( w ) ~ = ~ - { \cal H } ( w ) , } } & { { \mathrm { a n d ~ f o r } ~ k \ge 0 , ~ a _ { 1 } = ( c - I ) J ; } } \\ { { \phi ^ { ( k + 1 ) } ( w ) ~ = ~ \displaystyle \frac { - 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \cdot \sum _ { { j _ { 1 } + j _ { 2 } + \cdots + j _ { m } } = k \atop j _ { l } \ne 1 } D ^ { m } { \cal H } ( w ) } } \\ { { } } & { { } } & { { \cdot \big ( ( a _ { 1 } \nabla \phi ^ { ( j _ { 1 } ) } ( w ) , \cdot \cdot \cdot , a _ { 1 } \nabla \phi ^ { ( j _ { m } ) } ( w ) \big ) , } } \end{array}
$$

where we use the notation of the $m$ -linear form

$$
\begin{array} { r l } & { D ^ { m } H ( w ) ( a _ { 1 } \nabla \phi ^ { ( j _ { 1 } ) } ( w ) , \cdot \cdot \cdot , a _ { 1 } \nabla \phi ^ { ( j _ { m } ) } ( w ) ) } \\ & { : = \displaystyle \sum _ { i _ { 1 } , \cdots , i _ { m } = 1 } ^ { 2 n } H _ { z _ { i _ { 1 } } \cdots z _ { i _ { m } } } ( w ) ( a _ { 1 } \nabla \phi ^ { ( j _ { 1 } ) } ( w ) ) _ { i _ { 1 } } \cdot \cdot \cdot ( a _ { 1 } \nabla \phi ^ { ( j _ { m } ) } ( w ) ) _ { i _ { m } } . } \end{array}
$$

By (5.9), the phase flow $\widehat { z } = e _ { H } ^ { t } z$ satisfies

$$
\begin{array} { l } { { \displaystyle \widehat { z } - z ~ } = ~ - J \nabla \phi _ { H , \alpha } ^ { t } \big ( c \widehat { z } + ( I - c ) z \big ) } \\ { ~ = ~ - \displaystyle \sum _ { j = 1 } ^ { \infty } t ^ { j } J \nabla \phi ^ { ( j ) } \big ( c \widehat { z } + ( I - c ) z \big ) . } \end{array}
$$

Let $\psi ^ { s }$ be a truncation of $\phi _ { H , \alpha } ^ { s }$ up to a certain power, e.g., $s ^ { m }$ . Using the inverse transformation $\sigma _ { \alpha } ^ { - 1 }$ , we obtain the symplectic operator

$$
g ^ { s } = \sigma _ { \alpha } ^ { - 1 } ( \nabla \psi ^ { s } ) , \quad \left| s \right| \mathrm { s m a l l \ e n o u g h } ,
$$

which depends on $s , H , \alpha$ (or equivalently $B$ ) and the mode of truncation. It is a symplectic approximation to the phase flow $e _ { H } ^ { s }$ and can serve as the transition operator of a symplectic difference scheme for the Hamiltonian system (3.1)

$$
z \longrightarrow \widehat { z } = g ^ { s } z : \quad \widehat { z } = z - J \nabla \psi ^ { s } ( c \widehat { z } + ( I - c ) z ) , \quad c = \frac { 1 } { 2 } ( I + J B ) .
$$

Thus, using the technique of the phase flow generating functions, we have constructed, for every $H$ and every normal Darboux matrix, a hierarchy of symplectic schemes by truncation. The simple symplectic schemes (5.4) correspond to the lowest truncation.

# 5.6 Conservation Laws

The conservation laws we refer to here[FQ91,FW91a,GF88,Ge91] have two meanings. As it is well known, the Hamiltonian system (3.1) itself has first integrals which are conserved in time evolution, e.g., the Hamiltonian is always a first integral. Hence, the first question is how many first integrals of Hamiltonian system (3.1) can be preserved by symplectic algorithms. The second question is whether or not there exist their own first integrals in case the original first integrals can not be preserved by symplectic algorithms.

We first consider preservation of the first integrals of Hamiltonian systems by symplectic algorithms. The detailed discussion is referred to references[FQ91,Fen93b,GF88,Wan94] .

Consider the Hamiltonian system

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { J } \nabla H ( \boldsymbol { z } ) .
$$

Suppose

$$
\widehat z = g _ { H } ^ { s } ( z )
$$

is a symplectic algorithm. Under a symplectic transformation $z = S ( y )$ , system (6.1) can be transformed into

$$
\frac { \mathrm { d } \boldsymbol { y } } { \mathrm { d } t } = \boldsymbol { J } \nabla \tilde { H } ( \boldsymbol { y } ) ,
$$

where $\tilde { H } ( y ) = H ( S ( y ) )$ and scheme (5.6) can be transformed into

$$
{ \widehat { y } } = S ^ { - 1 } \circ g _ { H } ^ { s } \circ S ( y ) .
$$

On the other hand, the algorithm $g ^ { s }$ can be applied to system (6.3) directly and the corresponding scheme is

$$
\widehat { y } = g _ { \tilde { H } } ^ { s } ( y ) .
$$

Naturally, one can ask if (6.4) and (6.5) are the same. This introduces the following concept.

Definition 6.1. A symplectic algorithm $g ^ { s }$ is invariant under the group $G$ of symplectic transformations, or $G$ -invariant, for Hamiltonian $H$ if

$$
S ^ { - 1 } \circ g _ { H } ^ { s } \circ S = g _ { H \circ S } ^ { s } , \quad \forall S \in G ;
$$

$g ^ { s }$ is symplectic invariant for Hamiltonian $H$ , if

$$
S ^ { - 1 } g _ { H } ^ { s } \circ S = g _ { H \circ S } ^ { s } , \quad \forall S \in S p ( 2 n ) .
$$

In practice, the second case is more common. Generally speaking, numerical algorithms depend on the coordinates, i.e., they are locally represented. But many numerical algorithms may be independent of the linear coordinate transformations.

Theorem 6.2. [FW91a,GF88,Coo87] Suppose $F$ is a first integral of the Hamiltonian system (6.1) and $e _ { F } ^ { t }$ is the corresponding phase flow. Then $F$ is conserved up to a constant by the symplectic algorithm $g _ { H } ^ { s }$ ,

$$
F \circ g _ { H } ^ { s } = F + c , \quad c \ i s a c o n s t a n t
$$

if and only if $g _ { H } ^ { s }$ is $e _ { F } ^ { t }$ -invariant.

Proof. We first assume that the symplectic algorithm $g _ { H } ^ { s }$ is $e _ { F } ^ { t }$ -invariant, i.e.,

$$
e _ { F } ^ { - t } \circ g _ { H } ^ { s } \circ e _ { F } ^ { t } = g _ { H \circ e _ { F } ^ { t } } ^ { s } , \quad \forall t \in \mathbf { R } .
$$

Since $F$ is a first integral of the Hamiltonian system (6.1) with the Hamiltonian $H , H$ is also the first integral of the Hamiltonian system (5.6) with the Hamiltonian $F$ , i.e.,

$$
H \circ e _ { F } ^ { t } = H .
$$

It follows from (5.6) and (6.8) that

$$
e _ { F } ^ { - t } \circ g _ { H } ^ { s } \circ e _ { F } ^ { t } = g _ { H } ^ { s } ,
$$

$$
e _ { F } ^ { t } = ( g _ { H } ^ { s } ) ^ { - 1 } \circ e _ { F } ^ { t } \circ g _ { H } ^ { s } .
$$

Differentiating (6.9) with respect to $t$ at point 0 and noticing that

$$
\left. \frac { \mathrm { d } e _ { F } ^ { t } } { \mathrm { d } t } \right| _ { t = 0 } = J \nabla F ,
$$

we get

$$
J \nabla F = ( g _ { H } ^ { s } ) _ { * } ^ { - 1 } J \nabla F \circ g _ { H } ^ { s } .
$$

Since $g _ { H } ^ { s }$ is symplectic, i.e.,

$$
( g _ { H } ^ { s } ) _ { * } ^ { - 1 } J = J ( g _ { H } ^ { s } ) _ { * } ^ { \mathrm { T } } ,
$$

we have

$$
J \nabla F = J ( g _ { H } ^ { s } ) _ { * } ^ { \mathrm { T } } \nabla F \circ g _ { H } ^ { s } = J \nabla ( F \circ g _ { H } ^ { s } ) ,
$$

then

$$
\nabla F = ( g _ { H } ^ { s } ) _ { * } ^ { \mathrm { T } } \nabla F \circ g _ { H } ^ { s } = \nabla ( F \circ g _ { H } ^ { s } ) .
$$

It follows that

$$
F \circ g _ { H } ^ { s } = F + c .
$$

We now assume that $F$ is conserved by $g _ { H } ^ { s }$ , i.e., (6.6) is valid. Then noticing that the phase flows of the vector fields $J \nabla F$ and $( g _ { H } ^ { s } ) _ { * } ^ { - 1 } J \nabla F \circ g _ { H } ^ { s }$ are $e _ { F } ^ { t }$ and $( g _ { H } ^ { s } ) ^ { - 1 } \circ$ $e _ { F } ^ { t } \circ g _ { H } ^ { s }$ respectively, we can get (5.6) similarly, i.e., $g _ { H } ^ { s }$ is $e _ { F } ^ { t }$ -invariant.

Symplectic invariant algorithms are invariant under the symplectic group $S p ( 2 n )$ and hence invariant under the phase flow of any quadratic Hamiltonian. $\blacktriangle$

Corollary 6.3. Symplectic invariant algorithms for Hamiltonian systems preserve all quadratic first integrals of the original Hamiltonian systems up to a constant.

If a symplectic scheme has a fixed point, i.e., there is a point $z$ such that $g _ { H } ^ { s } ( z ) = z$ , then the constant $c = 0$ and the first integral is conserved exactly. Since linear schemes always have the fix point 0, we have the following result.

Corollary 6.4. Linear symplectic invariant algorithms for linear Hamiltonian systems preserve all quadratic first integrals of the original Hamiltonian systems.

Example 6.5. Centered Euler scheme and symplectic Runge–Kutta methods are symplectic invariants. Hence they preserve all quadratic first integrals of system (6.1) up to a constant.

Example 6.6. Explicit symplectic scheme (4.5), and other explicit symplectic schemes (2.1) – (2.4) considered in Chapter 8 are invariant under the linear symplectic transformations of the form diag $( A ^ { - \mathrm { T } } , A )$ , $A \in G L ( n )$ . Thus they preserve angular momentum $p ^ { \mathrm { T } } B q$ of the original Hamiltonian systems, since their infinitesimal symplectic matrices are $\mathrm { d i a g } ( - B ^ { \mathrm { T } } , B ) , B \in g l ( n )$ .

In fact, these results can be improved. Symplectic Runge–Kutta methods preserve all quadratic first integrals of system (6.1) exactly. For generating function methods, we have the following result[FW91a,GF88,FQ87] .

Theorem 6.7. Let $g _ { H , \alpha } ^ { s }$ be a symplectic method constructed by the generating function method with the Darboux type $\alpha .$ . If $F ( z ) = { \frac { 1 } { 2 } } z ^ { \mathrm { T } } A z$ , $A \in S m ( 2 n )$ , is a quadratic first integral of the Hamiltonian system (6.1) and

$$
A J B - B J A = O ,
$$

then $F ( z )$ is conserved by $g _ { H , \alpha } ^ { s }$ , i.e.,

$$
F ( { \widehat { z } } ) = F ( z ) , o r F \circ g _ { H , \alpha } ^ { s } = F .
$$

For $B = O$ , i.e., the case of centered symplectic difference schemes, (6.12) is always valid. So all centered symplectic difference schemes preserve all quadratic first integrals of the Hamiltonian system (6.1) exactly.

Proof. Since $F ( z )$ is the first integral of system (6.1),

$$
\frac { 1 } { 2 } \widehat { z } ^ { \mathrm { T } } A \widehat { z } = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z , \quad \widehat { z } = e _ { H } ^ { t } .
$$

It can be rewritten as

$$
\frac 1 2 ( \widehat z + z ) ^ { \mathrm { T } } A ( \widehat z - z ) = 0 , \quad \widehat z = e _ { H } ^ { t } .
$$

From (6.12), it follows that

$$
\frac { 1 } { 2 } \big ( J B ( \widehat { z } - z ) \big ) ^ { \mathrm { T } } A ( \widehat { z } - z ) = \frac { 1 } { 4 } ( \widehat { z } - z ) ^ { \mathrm { T } } \big ( A J B - B J A \big ) ( \widehat { z } - z ) = 0 , \quad \forall \widehat { z } , z \in { \bf R } ^ { 2 n } .
$$

Combining it with (6.14), we have

$$
\begin{array} { r } { \left( c \widehat { z } + ( I - c ) z \right) ^ { \mathrm { T } } A ( \widehat { z } - z ) = 0 . } \end{array}
$$

Using (5.13), it becomes

$$
\left( c { \widehat { z } } + ( I - c ) z \right) ^ { \mathrm { T } } A J \sum _ { j = 1 } ^ { \infty } t ^ { j } \nabla \phi ^ { ( j ) } \left( c { \widehat { z } } + ( I - c ) z \right) = 0 .
$$

From this, we get

$$
w ^ { \mathrm { T } } A J \nabla \phi ^ { ( j ) } ( w ) = 0 , \quad \forall j \geq 1 , \quad \forall w \in \mathbf { R } ^ { 2 n } .
$$

Taking $\boldsymbol { w } = c \boldsymbol { \widehat { z } } + ( \boldsymbol { I } - c ) \boldsymbol { z }$ , where

$$
\widehat { \boldsymbol { z } } = g _ { H , \alpha } ^ { s } \boldsymbol { z } = \boldsymbol { z } - J \nabla \psi ^ { ( m ) } \big ( c \widehat { \boldsymbol { z } } + ( I - c ) \boldsymbol { z } \big ) = \boldsymbol { z } - \sum _ { j = 1 } ^ { m } s ^ { j } J \nabla \phi ^ { ( j ) } \big ( c \widehat { \boldsymbol { z } } + ( I - c ) \boldsymbol { z } \big ) ,
$$

we have

$$
w ^ { \mathrm { T } } A ( \widehat { z } - z ) = - \sum _ { j = 1 } ^ { m } s ^ { j } w ^ { \mathrm { T } } A J \nabla \phi ^ { ( j ) } ( w ) = - A J \nabla \psi ( w ) = 0 ,
$$

since

$$
\begin{array} { r c l } { { w ^ { \mathrm { T } } A ( \widehat z - z ) ~ = ~ \frac { 1 } { 2 } \widehat z ^ { \mathrm { T } } A \widehat z - \frac { 1 } { 2 } z ^ { \mathrm { T } } A z + \frac { 1 } { 2 } ( \widehat z - z ) ^ { \mathrm { T } } ( A J B - B J A ) ( \widehat z - z ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = ~ \frac { 1 } { 2 } \widehat z ^ { \mathrm { T } } A \widehat z - \frac { 1 } { 2 } z ^ { \mathrm { T } } A z . } } \end{array}
$$

Therefore, the theorem is completed.

We list some of the most important normal Darboux matrices $c$ , the type matrices $B$ , together with the corresponding form of symmetric matrices $A$ of the conserved quadratic invariants $F ( z ) = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z$ :

$$
{ \begin{array} { r l r l r l } & { c = I - c = { \frac { 1 } { 2 } } I , } & & { B = O , } & & { A { \mathrm { ~ a r b i t r a r y } } , } \\ & { c = { \left( \begin{array} { l l } { I _ { n } } & { O } \\ { O } & { O } \end{array} \right) } , } & & { B = { \left( \begin{array} { l l } { O } & { - I _ { n } } \\ { - I _ { n } } & { O } \end{array} \right) } , } & & { b { \mathrm { ~ a r b i t r a r y } } ; } \\ & { c = { \left( \begin{array} { l l } { O } & { O } \\ { O } & { I _ { n } } \end{array} \right) } , } & & { B = { \left( \begin{array} { l l } { O } & { I _ { n } } \\ { I _ { n } } & { O } \end{array} \right) } , } & & { { \mathrm { ~ m o m e m u n m } } } \end{array} }
$$

$$
= { \frac { 1 } { 2 } } { \left( \begin{array} { l l } { ~ I _ { n } ~ } & { \pm I _ { n } } \\ { \mp I _ { n } ~ } & { ~ I _ { n } } \end{array} \right) } , ~ B = \mp I _ { 2 n } , ~ A = { \left( \begin{array} { l l } { ~ a } & { ~ b } \\ { ~ - b } & { ~ a } \end{array} \right) } , { \mathrm { H e r m i t i a n t y p e } } .
$$

$$
\begin{array} { r } { c = \frac { 1 } { 2 } \bigg ( \begin{array} { c c } { I } & { \pm I } \\ { \pm I } & { O } \end{array} \bigg ) , \quad B = \pm \bigg ( \begin{array} { c c } { I _ { n } } & { O } \\ { O } & { - I _ { n } } \end{array} \bigg ) , A = \bigg ( \begin{array} { c c } { a } & { b } \\ { - b } & { - a } \end{array} \bigg ) , \enspace b ^ { \mathrm { T } } = - b . } \end{array}
$$

Apart from the first integrals of the original Hamiltonian systems, a linear symplectic algorithm has its own quadratic first integrals. For the linear Hamiltonian system

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = L z , \quad L = J A \in s p ( 2 n )
$$

with a quadratic Hamiltonian $H ( z ) = \frac { 1 } { 2 } z ^ { \mathrm { T } } A z$ , $A ^ { \mathrm { T } } = A$ , let us denote its linear symplectic algorithm by

$$
{ \widehat { z } } = g _ { H } ^ { s } ( z ) = G ( s , A ) z , \quad G \in S p ( 2 n ) .
$$

Let us assume that the scheme (6.16) is of order $r$ . Then $G ( s )$ has the form

$$
\begin{array} { l } { G ( s ) = I + s L ( s ) , } \\ { L ( s ) = L + \displaystyle \frac { s } { 2 ! } L ^ { 2 } + \displaystyle \frac { s ^ { 2 } } { 3 ! } L ^ { 3 } + \cdots + \displaystyle \frac { s ^ { r - 1 } } { r ! } L ^ { r } + O ( s ^ { r } ) . } \end{array}
$$

For sufficiently small time step size $s$ , $G ( s )$ can be represented as

$$
G ( s ) = e ^ { s \widetilde { L } ( s ) } , \quad \widetilde { L } ( s ) = L + O ( s ^ { r } ) , \quad \widetilde { L } ( s ) \in s p ( 2 n ) .
$$

So (6.16) becomes

$$
{ \widehat { z } } = e ^ { s { \widetilde { L } } ( s ) } z .
$$

This is the solution $z ( t )$ of the linear Hamiltonian system

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = \widetilde { L } ( s ) z , \quad \widetilde { L } ( s ) \in s p ( 2 n ) ,
$$

with the initial value $z ( 0 ) = z ^ { 0 }$ evaluated at time $s$ . The symplectic numerical solution

$$
z ^ { k } = G ^ { k } ( s ) z ^ { 0 } = e ^ { k s { \widetilde { L } } ( s ) } z ^ { 0 }
$$

is just the solution of system (6.17) at discrete points $k s , k = 0 , \pm 1 , \pm 2 , \cdot \cdot \cdot .$ . Hence, for sufficiently small $s$ , scheme (6.16) corresponds to a perturbed linear Hamiltonian system (6.17) with the Hamiltonian

$$
\widetilde { H } ( z , s ) = \frac { 1 } { 2 } \big ( z , J ^ { - 1 } \widetilde { L } ( s ) z \big ) = \frac { 1 } { 2 } z ^ { \mathrm { T } } J ^ { - 1 } L z + O ( s ^ { r } ) = H ( z ) + O ( s ^ { r } ) .
$$

It is well-known that the linear Hamiltonian system has $n$ functionally independent quadratic first integrals. So does the scheme (6.15). The following

$$
\widetilde { H } _ { i } ( z , s ) = \frac { 1 } { 2 } z ^ { \mathrm { T } } J ^ { - 1 } \widetilde { L } ^ { 2 i - 1 } ( s ) z , \quad i = 1 , 2 , \cdots , n
$$

are the first integrals of the perturbed system (6.17), therefore, of scheme (6.16), which approximate the first integrals of system (6.15)

$$
H _ { i } ( z ) = { \frac { 1 } { 2 } } z ^ { \mathrm { T } } J ^ { - 1 } L ^ { 2 i - 1 } z , \quad i = 1 , 2 , \cdots , n
$$

up to $O ( s ^ { r } )$ . Another group of first integrals of (6.16) is

$$
\widehat { H } _ { i } ( z , s ) = z ^ { \mathrm { T } } J ^ { - 1 } G ^ { i } ( s ) z , \quad i = 1 , 2 , \cdots , n .
$$

They can be checked easily. The first one is[FW94]

$$
\begin{array} { l l l } { { \widehat { H } _ { 1 } ( z , s ) } } & { { = } } & { { z ^ { \mathrm { T } } J ^ { - 1 } G ( s ) z = z ^ { \mathrm { T } } J ^ { - 1 } ( I + s L ( s ) ) z } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { s z ^ { \mathrm { T } } J ^ { - 1 } L ( s ) z = 2 s H ( z ) + O ( s ^ { 3 } ) . } } \end{array}
$$

# 5.7 Convergence of Symplectic Difference Schemes

We considered Hamiltonian systems

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J H z , \quad z \in U \subset { \bf R } ^ { 2 n } .
$$

In this section, we shall prove that all symplectic schemes for Hamiltonian systems constructed by generating functions are convergent, if $\tau  0$ .

A normal Darboux matrix, which will be introduced in the next chapter, has the form

$$
\begin{array} { l } { { \alpha = \left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] = \left[ \begin{array} { c c } { { J } } & { { - J } } \\ { { \cfrac { 1 } { 2 } ( I + J B ) } } & { { \cfrac { 1 } { 2 } ( I - J B ) } } \end{array} \right] , } } \\ { { \alpha ^ { - 1 } = \left[ \begin{array} { c c } { { A ^ { \alpha } } } & { { B ^ { \alpha } } } \\ { { C ^ { \alpha } } } & { { D ^ { \alpha } } } \end{array} \right] = \left[ \begin{array} { c c } { { \frac { 1 } { 2 } ( J B J - J ) } } & { { I } } \\ { { \cfrac { 1 } { 2 } ( J B J + J ) } } & { { I } } \end{array} \right] , } } \end{array}
$$

which defines a linear transformation in the product space $\mathbf { R } ^ { 2 n } \times \mathbf { R } ^ { 2 n }$ :

$$
\begin{array} { r } { \left[ \begin{array} { c c } { \widehat { w } } \\ { w } \end{array} \right] = \alpha \left[ \begin{array} { c c } { \widehat { z } } \\ { z } \end{array} \right] , \quad \left[ \begin{array} { c c } { \widehat { z } } \\ { z } \end{array} \right] = \alpha ^ { - 1 } \left[ \begin{array} { c c } { \widehat { w } } \\ { w } \end{array} \right] , } \end{array}
$$

i.e.,

$$
\widehat { w } = J \widehat { z } - J z , \quad w = \frac { 1 } { 2 } \big ( I + J B \big ) \widehat { z } + \frac { 1 } { 2 } \big ( I - J B \big ) z , \quad B ^ { \mathrm { T } } = B .
$$

Let $z  { \widehat { z } } = g ( z , t )$ be the phase flow of the Hamiltonian systems (5.7); it is a time dependent canonical map. There exist, for sufficiently small $| t |$ and in (some neighborhood of) $\mathbf { R } ^ { 2 n }$ , a time-dependent gradient map $w \to \widehat { w } = f ( w , t )$ with Jacobian $f _ { w } ( w , t ) \in S m ( 2 n )$ (i.e.,everywhere symmetric) and a time-dependent generating function $\phi = \phi _ { \alpha , H }$ , such that

$$
\begin{array} { r } { f ( w , t ) = \nabla \phi _ { \alpha , H } ( w , t ) , \quad A _ { \alpha } g ( z , t ) + B _ { \alpha } z = \nabla \phi ( C _ { \alpha } g ( z , t ) + D _ { \alpha } z , t ) . } \end{array}
$$

On the other hand, for a given time-dependent scalar function $\psi ( w , t ) : \mathbb { R } ^ { 2 n } \times \mathbb { R } \to$ $\mathbf { R }$ , we can obtain a time-dependent canonical map $\widetilde { g } ( z , t )$ . If $\psi ( w , t )$ approximates the generating function $\phi _ { \alpha , H } ( w , t )$ of the Hamiltonian system (5.7), then $\widetilde { g } ( z , t )$ approximates the phase flow $g ( z , t )$ . For sufficiently small $\tau > 0$ "as the time step, define

$$
\phi ^ { ( m ) } = \sum _ { k = 1 } ^ { m } \phi ^ { ( k ) } ( w ) \tau ^ { k } ,
$$

where $\phi ^ { ( 1 ) } ( w ) = - H ( w )$ , and for $k \geq 0 , A ^ { \alpha } = \frac { 1 } { 2 } ( J B J - J )$ ,

$$
\begin{array} { r c l } { \displaystyle \phi ^ { ( k + 1 ) } ( w ) ~ = } & { \displaystyle \frac { - 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { i _ { 1 } , \cdots , i _ { n } = 1 \atop i _ { 1 } \cdots i _ { n } = k } ^ { 2 n } H z _ { i _ { 1 } } \cdot \cdot \cdot z _ { i _ { m } } ( w ) } \\ & & { \cdot \sum _ { j _ { 1 } + \cdots + j _ { m } = k } \left( A ^ { \alpha } \nabla \phi ^ { ( j _ { 1 } ) } ( w ) \right) _ { i _ { 1 } } \cdot \cdot \cdot \left( A ^ { \alpha } \nabla \phi ^ { ( j m ) } ( w ) \right) _ { i _ { m } } . } \end{array}
$$

Then, $\psi ^ { ( m ) } ( w , \tau )$ is the $m$ -th approximation of $\phi _ { \alpha , H } ( w , \tau )$ , and the gradient map,

$$
\boldsymbol { w } \longrightarrow \widehat { \boldsymbol { w } } = \widetilde { \boldsymbol { f } } ( \boldsymbol { w } , \tau ) = \nabla \psi ^ { ( m ) } ( \boldsymbol { w } , \tau ) .
$$

Define a canonical map $z  { \widehat { z } } = { \widetilde { g } } ( z , \tau )$ implicitly by equation

$$
A _ { \alpha } \widehat { z } + B _ { \alpha } z = ( \nabla \psi ^ { ( m ) } ) ( C _ { \alpha } \widehat { z } + D _ { \alpha } z , z ) .
$$

The implicit canonical difference scheme of $m$ -th order accuracy

$$
z = z ^ { k } \longrightarrow { \widehat z } = z ^ { k + 1 } = { \widetilde g } ( z ^ { k } , \tau ) ,
$$

for system (5.7) is obtained.

For the sake of simplicity, we denote $\smash { \widetilde { g } _ { \tau } ( z ) = \widetilde { g } ( z , \tau ) }$ . Then

$$
\widetilde g _ { 0 } ( z ) = z , \quad \frac { \mathrm { d } ^ { i } \widetilde g _ { \tau } ( z ) } { \mathrm { d } \tau ^ { i } } \Big | _ { \tau = 0 } = \frac { \mathrm { d } ^ { i } g _ { \tau } ( z ) } { \mathrm { d } \tau ^ { i } } \Big | _ { \tau = 0 } ,
$$

where $g _ { \tau } ( z )$ is the phase flow of $g ( z , \tau )$ .

Theorem 7.1. If $H$ is analytical in $U \subset \mathbf { R } ^ { 2 n }$ , then the scheme (7.9) is convergent with m-th order accuracy[CHMM78,QZ93] .

Proof. For the step-forward operator $\widetilde { g } _ { \tau }$ , we set

$$
z _ { 1 } = \widetilde { g } _ { \tau } ( z ) , z _ { 2 } = \widetilde { g } _ { \tau } ( z _ { 1 } ) , \ : \cdot \cdot , z _ { k } = \widetilde { g } _ { \tau } ( z _ { k - 1 } ) ,
$$

we have $z ^ { k } = \widetilde { g } _ { \tau } ^ { k }$

"First, we prove that the convergence holds locally. We begin by showing that for any $z _ { \mathrm { 0 } }$ , the iterations are defined for $\widetilde { z } _ { t / k } ^ { n }$ $( n \leq k )$ , if $t$ is sufficiently small. Indeed, in the neighborhood of $z _ { 0 }$ , $\widetilde g _ { \tau } ( z ) = z + o ( \tau )$ , thus, if $\widetilde { g } _ { \frac { t } { k } } ^ { l } ( z ) \left( l = 1 , 2 , \cdots , n - 1 \right)$ is defined for $z$ in the neighborhood of $z _ { \mathrm { 0 } }$ ,

$$
\begin{array} { l } { { \widetilde { g } _ { \frac { t } { k } } ^ { n } ( z ) - z ~ = ~ \left( \widetilde { g } _ { \frac { t } { k } } ^ { n } ( z ) - \widetilde { g } _ { \frac { t } { k } } ^ { n - 1 } ( z ) \right) + \left( \widetilde { g } _ { \frac { t } { k } } ^ { n - 1 } ( z ) - \widetilde { g } _ { \frac { t } { k } } ^ { n - 2 } ( z ) \right) + \cdot \cdot \cdot + \left( \widetilde { g } _ { \frac { t } { k } } ^ { \ : } ( z ) - z \right) } } \\ { { ~ = ~ \underbrace { o \Big ( \frac { t } { k } \Big ) + \cdot \cdot \cdot + o \Big ( \frac { t } { k } \Big ) } _ { n } = o ( t ) . } } \end{array}
$$

which is small and independent of $k$ for sufficiently small $t$ $t . \mathrm { S o } \widetilde { g } _ { t / k } ^ { n } \left( n \leq k \right)$ is defined and remains in $U _ { z _ { 0 } }$ for $z$ near $z _ { 0 }$ .

Since $H$ is analytical, for any $z _ { 1 } , z _ { 2 } \in U _ { z _ { 0 } }$ , there exists a constant $C$ , such that

$$
\begin{array} { r } { \| J H _ { z } ( z _ { 1 } ) - J H _ { z } ( z _ { 2 } ) \| \leq \| J \| \| H _ { z } ( z _ { 1 } ) - H _ { z } ( z _ { 2 } ) \| \leq C \| z _ { 1 } - z _ { 2 } \| . } \end{array}
$$

Let $F ( t ) = \| g ( z _ { 1 } , t ) - g ( z _ { 2 } , t ) \|$ , where $g ( z _ { i } , t ) = z _ { i } + \int _ { 0 } ^ { t } J H _ { z } ( g ( z _ { i } , s ) ) \mathrm { d } s ( i = 1 , 2 ) ,$

$$
\begin{array} { r c l } { F ( t ) } & { = } & { \displaystyle \left\| \int _ { 0 } ^ { t } J H _ { z } \big ( g ( z _ { 1 } , s ) \big ) \mathrm { d } s - \int _ { 0 } ^ { t } J H _ { z } \big ( g ( z _ { 2 } , s ) \big ) \mathrm { d } s + z _ { 1 } - z _ { 2 } \right\| } \\ & { \leq } & { \displaystyle \| z _ { 1 } - z _ { 2 } \| + C \int _ { 0 } ^ { t } F ( s ) \mathrm { d } s , } \end{array}
$$

using Gronwall inequality, we have

$$
\begin{array} { r l } & { \quad F ( t ) = \| g ( z _ { 1 } , t ) - g ( z _ { 2 } , t ) \| \leq e ^ { C | t | } \| z _ { 1 } - z _ { n } \| , } \\ & { g _ { t } ( z ) - \widetilde { g } _ { \frac { t } { k } } ^ { k } = \ g _ { \frac { t } { k } } ^ { k } ( z ) - \widetilde { g } _ { \frac { t } { k } } ^ { k } } \\ & { \quad \quad = \ g _ { \frac { t } { k } } ^ { k - 1 } g _ { \frac { t } { k } } ( z ) - g _ { \frac { t } { k } } ^ { k - 1 } \widetilde { g } _ { \frac { t } { k } } ( z ) + g _ { \frac { t } { k } } ^ { k - 2 } g _ { \frac { t } { k } } ( y _ { 1 } ) } \\ & { \quad \quad - g _ { \frac { t } { k } } ^ { k - 2 } \widetilde { g } _ { \frac { t } { k } } ( y _ { 1 } ) + \cdots + g _ { \frac { t } { k } } ^ { k - 1 } g _ { \frac { t } { k } } ( y _ { l - 1 } ) } \\ & { \quad \quad \quad - g _ { \frac { t } { k } } ^ { k - 1 } \widetilde { g } _ { \frac { t } { k } } ( y _ { l - 1 } ) + \cdots + g _ { \frac { t } { k } } ^ { k } ( y _ { k - 1 } ) - \widetilde { g } _ { \frac { t } { k } } ( y _ { k - 1 } ) , } \end{array}
$$

where $y _ { l } = \widetilde { g } _ { \frac { t } { k } } ^ { l } \left( z \right)$ . Then we have

$$
\begin{array} { r l } { \displaystyle \| g _ { t } ( z ) - \widetilde { g } _ { \frac { t } { k } } ^ { k } ( z ) \| } & { \le \displaystyle \sum _ { e = 1 } ^ { k } \exp \Big ( \frac { C \Big | k - l | t | } { k } \Big ) \| g _ { \frac { t } { k } } \big ( y _ { l - 1 } \big ) - \widetilde { g } _ { \frac { t } { k } } \big ( y _ { l - 1 } \big ) \| } \\ & { \le k \exp \big ( C | t | \big ) o \Big ( \frac { t } { k } \Big ) ^ { m } \longrightarrow 0 , \quad \mathrm { i f } k \longrightarrow \infty . } \end{array}
$$

Here, we use consistent supposition $g _ { \tau } ( z ) - \widetilde { g } _ { \tau } ( z ) = o ( \tau ) ^ { m }$ .

Now, we assume that $g ( z , t )$ "is defined for $0 \leq t \leq T$ . We shall show that $\widetilde { g } _ { \frac { t } { k } } ^ { k }$ converges to $g ( z , t )$ . By the above proof and domain compactness, if $N$ kis large enough, $g _ { \frac { t } { N } } = \operatorname* { l i m } _ { k \to \infty } \widetilde { g } _ { \frac { t } { k } N } ^ { k }$ uniformly convergent on a neighborhood of the curve $t  g _ { t } ( z )$ . N k→Thus, for $0 \leq t \leq T$ , $g _ { t } ( z ) = g _ { \frac { t } { N } } ^ { N } = \operatorname * { l i m } _ { k  \infty } ( \widetilde { g } _ { \frac { t } { k } N } ^ { k } ) ^ { N } ( z )$ . By the uniformity of $t$ , $g _ { t } ( z ) = \operatorname* { l i m } _ { k  \infty } \widetilde { g } _ { \frac { t } { k } } ^ { k } ( z )$ .

kFrom this proof, one can see that if $H$ is not analytical but $H _ { z }$ satisfies the local Lipschitz condition, then the scheme (7.9) is convergent with order $m = 1$ . -

# 5.8 Symplectic Schemes for Nonautonomous System

We consider the following system of canonical equations:

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } p _ { i } } { \mathrm { d } t } = - \frac { \partial H } { \partial q _ { i } } , } \\ { \displaystyle \frac { \mathrm { d } q _ { i } } { \mathrm { d } t } = \frac { \partial H } { \partial p _ { i } } , \qquad i = 1 , 2 , \cdots , n } \end{array}
$$

with Hamiltonian function $H ( p _ { 1 } , p _ { 2 } , \cdot \cdot \cdot , p _ { n } , q _ { 1 } , q _ { 2 } , \cdot \cdot \cdot , q _ { n } , t )$ . This is a nonautonomous Hamiltonian system. This approach, which is applied particularly to nonautonomous system, is to consider the time $t$ as an additional dependent variable. Now we can choose a parameter $\tau$ as a new independent variable. The original problem therefore becomes one of finding $q _ { 1 } , \cdots , q _ { n }$ with $t$ as a function of an independent variable $\tau$ . Hence, we set the coordinate $q _ { i }$ by adding $t = q _ { n + 1 }$ .

The corresponding phase space must have $2 n + 2$ dimensions, $z = ( p _ { 1 } , p _ { 2 } , \cdots , p _ { n }$ , $h , q _ { 1 } , q _ { 2 } , \cdots , q _ { n } , t )$ , here $t$ and $h$ being merely alternative notations for $q _ { n + 1 }$ and $p _ { n + 1 }$ . The new momentum $h$ associated with the time $t$ is, as its physical interpretation, the negative of the total energy. We call this new space the extended phase space.

An advantage of adding another degree of freedom to the analysis is that the system now resembles an autonomous system $\left[ \mathsf { A r n 8 9 , Q i n 9 6 , G o n 9 6 } \right]$ with $2 n + 2$ degree freedom, because its Hamiltonian is not an explicit function of $\tau$ .

In the extended phase space, (8.1) becomes

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J \nabla K ( z ) , \quad J = J _ { 2 n + 2 } = \left[ \begin{array} { c c } { O } & { - J _ { 2 n + 1 } } \\ { J _ { 2 n + 1 } } & { O } \end{array} \right] ,
$$

where $K ( z ) = h + H ( p _ { 1 } , p _ { 2 } , \cdot \cdot \cdot , p _ { n } , q _ { 1 } , q _ { 2 } , \cdot \cdot \cdot , q _ { n } , t )$ , which we call the “extended Hamiltonian function”. We write (8.2) in another form

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } p _ { i } } { \mathrm { d } \tau } = - \frac { \partial H } { \partial q _ { i } } , \quad \frac { \mathrm { d } q _ { i } } { \mathrm { d } \tau } = \frac { \partial H } { \partial p _ { i } } , \quad i = 1 , 2 , \cdots , } \\ { \displaystyle \frac { \mathrm { d } p _ { n + 1 } } { \mathrm { d } \tau } = - \frac { \partial H } { \partial q _ { n + 1 } } , } \\ { \displaystyle \frac { \mathrm { d } q _ { n + 1 } } { \mathrm { d } \tau } = 1 . } \end{array}
$$

Equation (8.4) shows that our normalized parameter now becomes equal to $q _ { n + 1 }$ , which is the time $t$ . The Equation (8.3) is the original canonical equation. The last Equation (8.5) gives the law according to which the negative of the total energy, $p _ { n + 1 }$ , changes with the time.

The general form of the canonical Equation (8.2) has great theoretical advantages. It shows the role of conservative system in a new light. We notice that after adding the time $t$ to the mechanical variables, every system becomes conservative. The extended Hamiltonian function $k$ does not depend on variable $\tau$ explicitly and thus our system is a conservative system in the extended phase space. The method of generating function plays a central role in the construction of symplectic schemes. In [Fen86] a constructive general theory of generating function roughly reads as follows. Let a normal Darboux matrix be

$$
\begin{array} { l } { { \alpha = \left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] = \left[ \begin{array} { c c } { { J } } & { { - J } } \\ { { } } & { { } } \\ { { \frac 1 2 ( I + J B ) } } & { { \frac 1 2 ( I - J B ) } } \end{array} \right] , \quad B ^ { \mathrm { T } } = B , } } \\ { { \alpha ^ { - 1 } = \left[ \begin{array} { c c } { { A ^ { \alpha } } } & { { B ^ { \alpha } } } \\ { { C ^ { \alpha } } } & { { D ^ { \alpha } } } \end{array} \right] = \left[ \begin{array} { c c } { { \frac 1 2 ( J B J - J ) } } & { { I } } \\ { { } } & { { } } \\ { { \frac 1 2 ( J B J + J ) } } & { { I } } \end{array} \right] . } } \end{array}
$$

Define a linear transformation in product space ${ \bf R } ^ { 2 n + 2 } \times { \bf R } ^ { 2 n + 2 }$ by

$$
\left[ \begin{array} { c } { \widehat { w } } \\ { w } \end{array} \right] = \alpha \left[ \begin{array} { c } { \widehat { z } } \\ { z } \end{array} \right] , \quad \left[ \begin{array} { c } { \widehat { z } } \\ { z } \end{array} \right] = \alpha ^ { - 1 } \left[ \begin{array} { c } { \widehat { w } } \\ { w } \end{array} \right] ,
$$

i.e.,

$$
\widehat { w } = J \widehat { z } - J z , \quad w = \frac { 1 } { 2 } ( I + J B ) \widehat { z } + \frac { 1 } { 2 } ( I - J B ) z , \quad B ^ { \mathrm { T } } = B .
$$

Let $z  \widehat { z } = g ( z , \tau )$ be the phase flow of the Hamiltonian system (8.2). It is a time-dependent canonical map. There exists, for a sufficiently small $\tau$ and in (some neighborhood of) $\mathbf { R } ^ { 2 n + 2 }$ , a time-dependent gradient mapping $w \to \widehat { w } = f ( w , \tau )$ with Jacobian $f _ { w } ( w , t ) \in S m ( 2 n + 2 )$ (i.e., symmetric everywhere) and a time-dependent generating function $\phi = \phi _ { \alpha , K } ( w , \tau )$ , such that

$$
\begin{array} { l } { \displaystyle \frac { \partial \phi } { \partial \tau } = - K \big ( A ^ { \alpha } \nabla \phi ( w ) + B ^ { \alpha } w \big ) , } \\ { \displaystyle f ( w , \tau ) = \nabla \phi _ { \alpha , K } ( w , \tau ) , } \\ { \displaystyle A _ { \alpha } g ( z , t ) + B _ { \alpha } z \equiv ( \nabla \phi ) \big ( C _ { \alpha } g ( z , t ) + D _ { a } z , t \big ) . } \end{array}
$$

On the other hand, for a given time-dependent scalar function $\psi ( w , t ) : \mathbf { R } ^ { 2 n + 2 } \times \mathbf { R } $ $\mathbf { R }$ , we can get a time-dependent canonical map $\widetilde g ( z , \tau )$ . If $\psi ( w , \tau )$ approximates the generating function $\phi _ { \alpha , K } ( \boldsymbol { w } , \tau )$ "of the Hamiltonian system (8.2), $\widetilde { g } ( z , t )$ approximates the phase flow $g ( z , t )$ .

For a sufficiently small $s > 0$ as the time-step, define

$$
\psi ^ { ( m ) } = \sum _ { k = 1 } ^ { m } \phi ^ { ( k ) } ( w ) s ^ { k } ,
$$

where

$$
\phi ^ { ( 1 ) } ( w ) = - K ( w ) , ~ A ^ { \alpha } = \frac { 1 } { 2 } ( J B J - J ) .
$$

For $k \geq 0$

$$
\begin{array} { l } { \displaystyle \phi ^ { ( k + 1 ) } ( w ) ~ = ~ \frac { - 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { i _ { 1 } , \cdots , i _ { m } = 1 } ^ { 2 n } K _ { z _ { i _ { 1 } } \cdots z _ { i _ { m } } } ( w ) } \\ { \displaystyle \quad \cdot \sum _ { j _ { 1 } + \cdots + j _ { m } = k } ^ { \prime } \left( A ^ { \alpha } \nabla \phi ^ { ( j _ { 1 } ) } ( w ) \right) _ { i _ { 1 } } \cdots \left( A ^ { \alpha } \nabla \phi ^ { ( j _ { m } ) } ( w ) \right) _ { i _ { m } } . } \end{array}
$$

Then $\psi ^ { ( m ) } ( w , s )$ is the $m$ -th approximation of $\phi _ { \alpha , K } ( \boldsymbol { w } , s )$ , and the gradient mapping

$$
\begin{array} { r } { \left. w \longrightarrow \widehat { w } = \widetilde { f } ( w , s ) = \nabla \psi ^ { ( m ) } ( w , s ) \right. } \end{array}
$$

defines a canonical map $z  { \widehat { z } } = { \widetilde { g } } ( z , s )$ implicitly by equation

$$
A _ { \alpha } \widehat { z } + B _ { \alpha } z = ( \nabla \psi ^ { ( m ) } ) ( C _ { \alpha } \widehat { z } + D _ { \alpha } z , s ) .
$$

An implicit canonical difference scheme

$$
z = z ^ { k } \longrightarrow { \widehat z } = z ^ { k + 1 } = { \widetilde g } ( z ^ { k } , s ) ,
$$

for system (8.2) is obtained $[ 0 \mathrm { i n } 9 6 ]$ , and this scheme is of $m$ -th order of accuracy.

Let $B = 0$

$$
\phi ^ { ( 1 ) } ( w ) = - K ( w ) , \phi ^ { ( 2 ) } = \phi ^ { ( 4 ) } = 0 , \phi ^ { ( 3 ) } = \frac { 1 } { 2 4 } ( \nabla K ) ^ { \top } J K _ { z z } J \nabla K .
$$

We have a scheme of second order:

$$
\begin{array} { r l } & { J ( \widehat { z } - z ) = \widehat { w } = \nabla \phi ^ { ( 2 ) } ( w , s ) = - s \nabla K \Big ( \frac { \widehat { z } + z } { 2 } \Big ) , } \\ & { \ : \ : } \\ & { \ : \ : z ^ { k + 1 } = z ^ { k } + s J \nabla K \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) , } \\ & { \ : p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - s H _ { q _ { i } } \Big ( \frac { p ^ { k + 1 } + p ^ { k } } { 2 } , \frac { q ^ { k + 1 } + q ^ { k } } { 2 } , \frac { t ^ { k + 1 } + t ^ { k } } { 2 } \Big ) , } \\ & { \ : \ : q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + s H _ { p _ { i } } \Big ( \frac { p ^ { k + 1 } + p ^ { k } } { 2 } , \frac { q ^ { k + 1 } + q ^ { k } } { 2 } , \frac { t ^ { k + 1 } + t ^ { k } } { 2 } \Big ) , } \\ & { \ : \ : h ^ { k + 1 } = h ^ { k } - s H _ { t } \Big ( \frac { p ^ { k + 1 } + p ^ { k } } { 2 } , \frac { q ^ { k + 1 } + q ^ { k } } { 2 } , \frac { t ^ { k + 1 } + t ^ { k } } { 2 } \Big ) , } \\ & { \ : t ^ { k + 1 } = t ^ { k } + s . } \end{array}
$$

This is the time-centered Euler scheme.

Scheme of the fourth order:

$$
\begin{array} { r l } & { J ( z ^ { k + 1 } - z ^ { k } ) = \nabla \phi ^ { ( 4 ) } \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) = - s \nabla K \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) J \nabla K \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) } \\ & { \qquad + \frac { s ^ { 3 } } { 2 4 } \nabla _ { z } \big ( ( \nabla K ) ^ { \mathrm { T } } J K _ { z z } J \nabla K \big ) , } \\ & { z ^ { k + 1 } = z ^ { k } + s J \nabla K \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) - \frac { s ^ { 3 } } { 2 4 } J \nabla _ { z } \big ( ( \nabla K ) ^ { \mathrm { T } } J K _ { z z } J \nabla K \big ) , } \end{array}
$$

i.e.,

$$
p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - s H _ { q _ { i } } \Big ( \frac { p ^ { k + 1 } + p ^ { k } } { 2 } , \frac { q ^ { k + 1 } + q ^ { k } } { 2 } , \frac { t ^ { k + 1 } + t ^ { k } } { 2 } \Big )
$$

$$
- \frac { s ^ { 3 } } { 2 4 } ( H _ { p _ { j } p _ { l } q _ { i } } H _ { q _ { j } } H _ { q _ { l } } + 2 H _ { p _ { j } p _ { l } } H _ { q _ { j } q _ { i } } H _ { q _ { l } } - 2 H _ { q _ { j } p _ { l } q _ { i } } H _ { p _ { j } } H _ { q _ { l } }
$$

$$
\nonumber - 2 H _ { q _ { j } p _ { l } } H _ { p _ { j } q _ { i } } H _ { q _ { l } } - 2 H _ { q _ { j } p _ { l } } H _ { p _ { j } } H _ { q _ { l } q _ { i } } + 2 H _ { q _ { j } q _ { l } } H _ { p _ { l } q _ { i } } H _ { p _ { j } } + H _ { q _ { j } q _ { l } q _ { i } } H _ { p _ { l } } H _ { p _ { j } }
$$

$$
- 2 H _ { q _ { j } q _ { i } } H _ { p _ { j } t } - 2 H _ { q _ { j } } H _ { p _ { j } q _ { i } t } + 2 H _ { p _ { j } q _ { i } } H _ { q _ { j } t } + 2 H _ { p _ { j } } H _ { q _ { j } q _ { i } t } + H _ { q _ { i } t t } ) ,
$$

$$
q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + s H _ { p _ { j } } \Big ( \frac { p ^ { k + 1 } + p ^ { k } } { 2 } , \frac { q ^ { k + 1 } + q ^ { k } } { 2 } , \frac { t ^ { k + 1 } + t ^ { k } } { 2 } \Big )
$$

$$
+ \frac { s ^ { 3 } } { 2 4 } ( H _ { p _ { j } p _ { l } p _ { i } } H _ { q _ { j } } H _ { q _ { l } } + 2 H _ { p _ { j } p _ { l } } H _ { q _ { j } p _ { i } } H _ { q _ { l } } - 2 H _ { q _ { j } p _ { l } p _ { i } } H _ { p _ { j } } H _ { q _ { l } }
$$

$$
- 2 H _ { q _ { j } p _ { l } } H _ { p _ { j } p _ { i } } H _ { q _ { l } } - 2 H _ { q _ { j } p _ { l } } H _ { p _ { j } } H _ { q _ { l } p _ { i } } + 2 H _ { q _ { j } p _ { l } } H _ { p _ { l } q _ { i } } H _ { p _ { j } } + H _ { q _ { j } q _ { l } p _ { i } } H 
$$

$$
- 2 H _ { q _ { j } p _ { i } } H _ { p _ { j } t } - 2 H _ { q _ { j } } H _ { p _ { j } p _ { i } t } + 2 H _ { p _ { j } p _ { i } } H _ { q _ { j } t } + 2 H _ { p _ { j } } H _ { q _ { j } p _ { i } t } + H _ { p _ { i } t t } ) ,
$$

$$
h ^ { k + 1 } = h ^ { k } - s H _ { t } \Big ( \frac { p ^ { k + 1 } + p ^ { k } } { 2 } , \frac { q ^ { k + 1 } + q ^ { k } } { 2 } , \frac { t ^ { k + 1 } + t ^ { k } } { 2 } \Big )
$$

$$
- \frac { s ^ { 3 } } { 2 4 } ( H _ { p _ { j } p _ { l } t } H _ { q _ { j } } H _ { q _ { l } } + 2 H _ { p _ { j } p _ { l } } H _ { q _ { j } t } H _ { q _ { l } } - 2 H _ { q _ { j } p _ { l } t } H _ { p _ { j } } H _ { q _ { l } }
$$

$$
\begin{array} { r } { - 2 H _ { q _ { j } p _ { l } } H _ { p _ { j } t } H _ { q _ { l } } - 2 H _ { q _ { j } p _ { l } } H _ { p _ { j } } H _ { q _ { l } t } + 2 H _ { q _ { j } q _ { l } } H _ { p _ { l } t } H _ { q _ { l } } + H _ { q _ { j } q _ { l } t } H _ { p _ { l } } H _ { p _ { j } } } \end{array}
$$

$$
\begin{array} { r l } & { \quad - 2 H _ { q _ { j } t } H _ { p _ { j } t } - 2 H _ { q _ { j } } H _ { p _ { j } t t } + 2 H _ { p _ { j } t } H _ { q _ { j } t } + 2 H _ { p _ { j } } H _ { q _ { i } t } + H _ { t t t } ) , } \\ & { \quad } \\ & { { t } ^ { k + 1 } = { t } ^ { k } + { s } . } \end{array}
$$

Let

$$
\boldsymbol { B } = - \left[ \begin{array} { c c } { \boldsymbol { O } } & { \boldsymbol { I } } \\ { \boldsymbol { I } } & { \boldsymbol { O } } \end{array} \right] , \quad \boldsymbol { w } = \left[ \begin{array} { c } { \boldsymbol { \widehat { p } } } \\ { \boldsymbol { q } } \end{array} \right] .
$$

We have

$$
\begin{array} { r l } & { \phi ^ { ( 1 ) } = - K ( w ) , } \\ & { \phi ^ { ( 2 ) } = - \frac { 1 } { 2 } ( K _ { q _ { i } } K _ { p _ { i } } ) ( w ) , } \\ & { \phi ^ { ( 3 ) } = - \frac { 1 } { 6 } ( K _ { p _ { j n } } K _ { q _ { j } } K _ { q _ { i } } + K _ { q _ { i } q _ { i } } K _ { p _ { j } } K _ { p _ { i } } + K _ { q _ { j n } } K _ { p _ { j } } K _ { q _ { i } } ) ( w ) , \quad \mathrm { o r } } \\ & { \phi ^ { ( 2 ) } = - \frac { 1 } { 2 } ( H _ { q _ { i } } H _ { p _ { j } } + H _ { t } ) ( w ) , } \\ & { \phi ^ { ( 3 ) } = - \frac { 1 } { 6 } ( H _ { p _ { j n } } H _ { q _ { i } } H _ { q _ { i } } + H _ { q _ { i } } H _ { q _ { j n } } H _ { p _ { j } } + H _ { q _ { i } } H _ { p _ { t } t } } \\ & { \qquad + H _ { q _ { i } q _ { i } } H _ { p _ { j } } H _ { p _ { i } } + 2 H _ { p _ { j } } H _ { q _ { i } } + H _ { t \ell } ) . } \end{array}
$$

Scheme of the first order

$$
\begin{array} { l } { { p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - s H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) , } } \\ { { \ } } \\ { { q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + s H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) , } } \\ { { \ } } \\ { { h ^ { k + 1 } = h ^ { k } - s H _ { t } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) , } } \\ { { \ } } \\ { { t ^ { k + 1 } = t ^ { k } + s . } } \end{array}
$$

Scheme of the second order

$$
\begin{array} { l } { p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - s H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) - \cfrac { s ^ { 2 } } { 2 } ( H _ { q _ { i } t } + H _ { q _ { j } q _ { i } } H _ { p _ { j } } + H _ { q _ { j } } H _ { p _ { j } q _ { i } } ) ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) } \\ { q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + s H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) + \cfrac { s ^ { 2 } } { 2 } ( H _ { p _ { i } t } + H _ { q _ { j } p _ { i } } H _ { p _ { j } } + H _ { q _ { j } } H _ { p _ { j } p _ { i } } ) ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) } \\ { { h } ^ { k + 1 } = h ^ { k } - s H _ { t } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) - \cfrac { s ^ { 2 } } { 2 } ( H _ { t t } + H _ { q _ { j } t } H _ { p _ { j } } + H _ { q _ { j } } H _ { p _ { j } t } ) ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) , } \\ { { t } ^ { k + 1 } = t ^ { k } + s . } \end{array}
$$

Scheme of the third order

$$
\begin{array} { r l } & { p _ { i } ^ { k + 1 } = p _ { i } ^ { k } - s H _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) - \frac { s ^ { 2 } } { 2 } ( H _ { q _ { i } t } + H _ { q _ { j } q _ { i } } H _ { p _ { j } } + H _ { q _ { j } } H _ { p _ { j } q _ { i } } ) } \\ & { \qquad \cdot ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) - \frac { s ^ { 3 } } { 6 } ( H _ { t t } + 2 H _ { p _ { j } } H _ { q _ { j } t } + H _ { q _ { l } } H _ { p _ { t } t } + H _ { p _ { j } p _ { l } } H _ { q _ { j } } H _ { q _ { i } } } \\ & { \qquad + H _ { q _ { l } } H _ { q _ { j } p _ { l } } H _ { p _ { j } } + H _ { q _ { j } q _ { l } } H _ { p _ { j } } H _ { p _ { l } } ) _ { q _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) , } \\ & { q _ { i } ^ { k + 1 } = q _ { i } ^ { k } + s H _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) + \frac { s ^ { 2 } } { 2 } ( H _ { p _ { i } t } + H _ { q _ { j } p _ { i } } H _ { p _ { j } } + H _ { q _ { j } } H _ { p _ { j } p _ { i } } ) } \\ & { \qquad \cdot ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) + \frac { s ^ { 3 } } { 6 } ( H _ { t t } + 2 H _ { p _ { i } } H _ { e _ { i } t } + H _ { e _ { i } } H _ { n } . _ { n } H _ { n } . } \end{array}
$$

$$
+ H _ { q \imath } H _ { q _ { j } p \imath } H _ { p _ { j } } + H _ { q _ { j } q \imath } H _ { p _ { j } } H _ { p \imath } ) _ { p _ { i } } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } )
$$

$$
h ^ { k + 1 } = h ^ { k } - s H _ { t } ( p ^ { k + 1 } , q ^ { k } , t ^ { k } ) - \frac { s ^ { 2 } } { 2 } ( H _ { t t } + H _ { q _ { j } t } H _ { p _ { j } } + H _ { q _ { j } } H _ { p _ { j } t } )
$$

$$
\cdot \left( p ^ { k + 1 } , q ^ { k } , t ^ { k } \right) - \frac { s ^ { 3 } } { 6 } ( H _ { t t } + 2 H _ { p _ { j } } H _ { q _ { j } t } + H _ { q _ { l } } H _ { p _ { l } t } + H _ { p _ { j } p _ { l } } H _ { q _ { j } } H _ { q _ { l } }
$$

# Bibliography

[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[CHMM78] A. Chorin, T. J. R. Huges, J. E. Marsden, and M. McCracken: Product formulas and numerical algorithms. Comm. Pure and Appl. Math., 31:205–256, (1978).   
[Coo87] G. J. Cooper: Stability of Runge–Kutta methods for trajectory problems. IMA J. Numer. Anal., 7:1–13, (1987).   
[Fen86] K. Feng: Difference schemes for Hamiltonian formalism and symplectic geometry. J. Comput. Math., 4:279–289, (1986).   
[Fen93b] K. Feng: Symplectic, contact and volume preserving algorithms. In Z.C Shi and T. Ushijima, editors, Proc.1st China-Japan conf. on computation of differential equationsand dynamical systems, pages 1–28. World Scientific, Singapore, (1993).   
[FQ91] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FW91] K. Feng and D.L. Wang: A Note on Conservation Laws of Symplectic Difference Schemes for Hamiltonian Systems. J. Comput. Math., 9(3):229–237, (1991).   
[FW94] K. Feng and D.L. Wang: Dynamical systems and geometric construction of algorithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS Vol 163, pages 1–32. AMS, (1994).   
[FWQW89] K. Feng, H. M. Wu, M.Z. Qin, and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[Ge91] Z. Ge: Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, (1991).   
[GF88] Z. Ge and K. Feng: On the Approximation of Linear Hamiltonian Systems. J. Comput. Math., 6(1):88–97, (1988).   
[Gon96] O. Gonzalez: Time integration and discrete Hamiltonian systems. J. Nonlinear. Sci., 6:449–467, (1996).   
[Hua44] L. K. Hua: On the theory of automorphic function of a matrix I, II. Amer. J. Math., 66:470–488, (1944).   
[LL99] L. D. Landau and E. M. Lifshitz: Mechanics, Volume I of Course of Theoretical Physics. Corp. Butterworth, Heinemann, New York, Third edition, (1999).   
[Qin96] M.Z. Qin: Symplectic difference schemes for nonautonomous Hamiltonian systemes. Acta Applicandae Mathematicae, 12(3):309–321, (1996).   
[Qin97a] M. Z. Qin: A symplectic schemes for the PDEs. AMS/IP studies in Advanced Mathemateics, 5:349–354, (1997).   
[QZ93] M. Z. Qin and W. J. Zhu: A note on stability of three stage difference schemes for ODE’s. Computers Math. Applic., 25:35–44, (1993).   
[Sie43] C.L. Siegel: Symplectic geometry. Amer. J. Math., 65:1–86, (1943).   
[Wan94] D. L. Wang: Some acpects of Hamiltonian systems and symplectic defference methods. Physica D, 73:1–16, (1994).   
[Wei72] A. Weinstein: The invariance of Poincares´ generating function for canonical transformations. Inventiones Math., 16:202–213, (1972).
