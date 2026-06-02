# Chapter 4. Symplectic Difference Schemes for Hamiltonian Systems

The canonicity of the phase flow for time-independent Hamiltonian systems is one of the most important properties. It ensures the preservation of phase areas and the phase volume. Thus, preserving the canonicity of transition of difference schemes from one time step to the next is also important in the numerical solutions of Hamiltonian systems. The goal of this chapter is to find some simple symplectic schemes, i.e., to identify which one, among the existing difference schemes, is symplectic.

# 4.1 Background

It is well known that Hamiltonian systems have many intrinsic properties: the preservation of phase areas of even dimension and the phase volume, the conservation laws of energy and momentum, and other symmetries.

# 4.1.1 Element and Notation for Hamiltonian Mechanics

Let $H$ be a smooth function of $2 n$ variables $p _ { 1 } , \cdots , p _ { n } , q _ { 1 } , \cdots , q _ { n } $ . Then, the Hamiltonian canonical systems are of the form :

$$
\dot { p } = - H _ { q } , \quad \dot { q } = H _ { p } ,
$$

where $p = ( p _ { 1 } , \cdots , p _ { n } ) ^ { \mathrm { T } }$ $q = ( q _ { 1 } , \cdots , q _ { n } ) ^ { \mathrm { T } }$ . Let $z = { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] }$ , and the standard symplectic matrix be:

$$
J = \left[ \begin{array} { c c } { { O } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { O } } \end{array} \right] ,
$$

where $I _ { n }$ is the $n \times n$ identity matrix, and $J$ has property $J ^ { - 1 } = J ^ { \prime } = - J$ . Then, system (1.1) can be written in a compact form:

$$
\dot { z } = J ^ { - 1 } H _ { z } ,
$$

where $H _ { z } = \left[ \begin{array} { l } { H _ { q } } \\ { H _ { p } } \end{array} \right] ; H$ is called the Hamiltonian function of the system. The phase flow of system (1.1) can be represented as $g _ { H } ^ { t }$ . According to the fundamental theorem of a Hamiltonian system, the solution of a canonical system is a one-parameter symplectic group $G _ { t }$ , denoted by $S p ( 2 n )$ . Therefore, symplectic geometry serves as the mathematical foundation of Hamiltonian mechanics. For simplicity, we consider only the classical phase space $\mathbf { R } ^ { 2 n } = \mathbf { R } _ { p } ^ { n } \times \mathbf { R } _ { q } ^ { n }$ , where $\mathbf { R } _ { p } ^ { n }$ is called the momentum space, and $\mathbf { R } _ { q } ^ { n }$ the configuration space. Locally, every $2 n$ -dimensional manifold is diffeomorphic to a neighborhood of a point on $\mathbf { R } ^ { 2 n }$ . The phase space $\mathbf { R } ^ { 2 n }$ is equipped with a standard symplectic structure defined by

$$
\omega _ { J } = \sum _ { i = 1 } ^ { n } \textrm { d } z _ { i } \wedge \textrm { d } z _ { n + i } = \sum _ { i = 1 } ^ { n } \textrm { d } p _ { i } \wedge \textrm { d } q _ { i } ,
$$

i.e., for each $z$ of $\mathbf { R } ^ { 2 n }$ , it is a bilinear antisymmetric form:

$$
\omega _ { J } ( \xi , \eta ) = \xi ^ { \prime } J \eta , \quad \forall ~ \xi , \eta \in T _ { z } \mathbf { R } ^ { 2 n } ,
$$

for each pair of tangent vector $\xi , \eta$ at point $z \in \ { \cal T } _ { z } { \bf R } ^ { 2 n }$ , where $J$ is the standard symplectic structure Equation (??).

Let $w : \mathbf { R } ^ { 2 n }  \mathbf { R } ^ { 2 n }$ be a differential mapping, $z \in \mathbf { R } ^ { 2 n } \to w ( z ) \in \mathbf { R } ^ { 2 n }$ ; the corresponding Jacobian matrix is denoted by

$$
\frac { \partial w } { \partial z } = \left[ \begin{array} { c c } { \frac { \partial w _ { 1 } } { \partial z _ { 1 } } } & { \cdots } & { \frac { \partial w _ { 1 } } { \partial z _ { 2 n } } } \\ { \vdots } & { \vdots } \\ { \frac { \partial w _ { 2 n } } { \partial z _ { 1 } } } & { \cdots } & { \frac { \partial w _ { 2 n } } { \partial z _ { 2 n } } } \end{array} \right] .
$$

The mapping $w$ induces, for each $z \in \mathbf { R } ^ { 2 n }$ , a linear mapping $w _ { * } ( z )$ from the tangent space at $z$ into the the tangent space at $w ( z )$ :

$$
\xi = ( \xi _ { 1 } , \cdot \cdot \cdot , \xi _ { 2 n } ) ^ { \prime } \longrightarrow w _ { * } \xi = { \frac { \partial w } { \partial z } } \xi .
$$

Each 2-form $w$ on $\mathbf { R } ^ { 2 n }$ also induces a 2-form $w ^ { \ast } \omega$ on $\mathbf { R } ^ { 2 n }$ by the formula

$$
w ^ { \ast } \omega ( \xi , \eta ) _ { z } \equiv \omega \left( \frac { \partial w } { \partial z } \xi , \frac { \partial w } { \partial z } \eta \right) _ { w ( z ) } .
$$

If $\omega ( \xi , \eta ) _ { z } = \xi A ( z ) \eta$ , $A ^ { \prime } ( z ) = - A ( z )$ , then $w ^ { * } \omega ( \xi , \eta ) = \xi B ( z ) \eta$ , i.e.,

$$
B ( z ) = \left[ \frac { \partial w } { \partial z } \right] ^ { \prime } A ( w ( z ) ) \left[ \frac { \partial w } { \partial z } \right] .
$$

Refer to Definition 4.7 from Chapter 1.

Definition 1.1 (Diff). A diffeomorphism (differentiable one to one onto mapping ) of $\mathbf { R } ^ { 2 n }$ is called a canonical transformation if $w$ preserves the standard symplectic structure. i.e., $w ^ { * } \omega _ { J } = \omega _ { J }$ ,

$$
{ \left[ \frac { \partial w } { \partial z } \right] } ^ { \prime } \boldsymbol { J } \left[ \frac { \partial w } { \partial z } \right] = \boldsymbol { J } ,
$$

i.e., Jacobian $\frac { \partial w } { \partial z }$ is a symplectic matrix for every $z$ .

Its geometric meaning is depicted in Fig. 1.1. According to the general theory of ODE, for each Hamiltonian system (1.1), there corresponds a one parameter group of diffeomophisms $g ^ { t }$ , at least locally in $t$ and $z$ , of $\mathbf { R } ^ { 2 n }$ such that

$$
g ^ { 0 } = \mathrm { i d } , \quad g ^ { t _ { 1 } + t _ { 2 } } = g ^ { t _ { 1 } } \cdot g ^ { t _ { 2 } } .
$$

![](../chunks/Symplectic Geometric Algorithms for Hamiltonian Systems, Kang Feng_Mengzhao Qin_part_0004_pages_0211-0280/auto/images/3ebccf897627727be76c50d7090b1711b0c57d1f21b5b6d6399cb1febe60dfe4.jpg)  
Fig. 1.1. Geometric meaning of preserving symplectic structure

# 4.1.2 Geometrical Meaning of Preserving Symplectic Structure $\omega$

If $z ( 0 )$ is taken as an initial value, then the solution of (1.1) can be written as

$$
z ( t ) = g ^ { t } z ( 0 ) .
$$

The basic property of a Hamiltonian system is that $g ^ { t }$ is a canonical transformation, i.e.,

$$
( g ^ { t } ) ^ { * } \omega _ { J } = \omega _ { J } ,
$$

for all $t$ . This leads to the following class of phase-area conservation law:

$$
\begin{array} { l } { { \displaystyle \int _ { g ^ { t } \sigma ^ { 2 } } \omega _ { J } = \int _ { \sigma ^ { 2 } } \omega _ { J } , \qquad \mathrm { e v e r y ~ 2 - c h a i n } \sigma ^ { 2 } \subset { \bf R } ^ { 2 n } , } } \\ { { \displaystyle \int _ { g ^ { t } \sigma ^ { 4 } } \omega _ { J } \wedge \omega _ { J } = \int _ { \sigma ^ { 4 } } \omega _ { J } \wedge \omega _ { J } , \qquad \mathrm { e v e r y ~ 4 - c h a i n } \sigma ^ { 4 } \subset { \bf R } ^ { 2 n } , \qquad } } \\ { { \displaystyle \qquad \cdots \qquad \cdots \qquad \cdots \qquad \cdots \qquad \cdots \qquad } } \\ { { \displaystyle \int _ { g ^ { t } \sigma ^ { 2 n } } \omega _ { J } \wedge \cdots \wedge \omega _ { J } = \int _ { \sigma ^ { 2 n } } \omega _ { J } \wedge \cdots \wedge \omega _ { J } , \quad \mathrm { e v e r y ~ 2 n } { \cdot } \mathrm { c h a i n } \sigma ^ { 2 n } \subset { \bf R } ^ { 2 n } , } } \end{array}
$$

where the last one is the Liouville’s phase-volume conservation law. Another class of conservation law is related to the energy and all the first integrals. A smooth function $\varphi ( x )$ is said to be a first integral if $\varphi ( g ^ { t } z ) = \varphi ( z )$ , for all $t , z$ . The latter is equivalent to the condition $\{ \varphi , H \} = 0$ ; $H$ usually represents the energy, which is a first integral of itself.

The above situations can be generalized. A symplectic structure in $\mathbf { R } ^ { 2 n }$ is specified by a non-degenerate, closed 2-form

$$
\omega _ { K } = \sum _ { i < j } K _ { i j } ( z ) { \bf d } z _ { i } \wedge { \bf d } z _ { j } ,
$$

i.e.,

$$
\omega _ { K } ( \xi , \eta ) _ { z } = { \frac { 1 } { 2 } } \xi ^ { \prime } K ( z ) \eta , \quad K ^ { \prime } ( z ) = - K ( z ) , \quad \operatorname * { d e t } K ( z ) \neq 0 .
$$

A differentiable mapping $w : \mathbb { R } ^ { 2 n } \to \mathbb { R } ^ { 2 n }$ called $K$ -symplectic, if $w ^ { * } \omega _ { K } = \omega _ { K }$ , i.e.,

$$
\left( \frac { \partial w } { \partial z } \right) ^ { \prime } K \bigl ( w ( z ) \bigr ) \frac { \partial w } { \partial z } = K ( z ) .
$$

The Darboux theorem establishes the equivalence between all symplectic structures. Every non-singular closed 2-form $\omega _ { K }$ can be brought to the standard form

$$
\sum _ { i < j } K _ { i j } ( z ) \textrm { d } z _ { i } \wedge \textrm { d } z _ { j } = \sum _ { i < j } \textrm { d } \omega _ { i } \wedge \textrm { d } w _ { n + j }
$$

locally by suitable coordinate transformation $z  w ( z )$ .

# 4.1.3 Some Properties of a Symplectic Matrix

From Subsection 2.3.2, a matrix $S$ of order $2 n$ is called a symplectic matrix if it satisfies:

$$
S ^ { \prime } J S = J ,
$$

where $S ^ { \prime }$ is the transpose of $S$ . All symplectic matrices form a symplectic group $S p ( 2 n )$ .

Definition 1.2. A matrix $B$ of order $2 n$ is called infinitesimal symplectic, if

$$
\begin{array} { r } { J B + B ^ { \prime } J = O . } \end{array}
$$

All infinitesimal symplectic matrices form a Lie algebra with commutation operation $[ A , B ] = A B - B A$ , denoted as $s p ( 2 n )$ . $s p ( 2 n )$ is the Lie algebra of the Lie group $S p ( 2 n )$ . We have the following well-known proposition[FWQ90] , which can be found in Chapter 2. Here, we omit the proof.

Proposition 1.3. det $S = 1$ , if $S \in S p ( 2 n )$ .

Proposition 1.4. $S ^ { - 1 } = - J S ^ { \prime } J = J ^ { - 1 } S ^ { \prime } J , i f S \in S p ( 2 n ) .$

Proposition 1.5. $S J S ^ { \prime } = J ,$ , if $S \in S p ( 2 n )$ .

ition 1.6. Let $\boldsymbol { S } = \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] , \boldsymbol { A } , \boldsymbol { B } , \boldsymbol { C } , \boldsymbol { D }$ be an $n \times n$ matrix; then $S \in$ $S p ( 2 n )$

$$
\begin{array} { r l } { A B ^ { \prime } - B A ^ { \prime } = O , } & { C D ^ { \prime } - D C ^ { \prime } = O , \quad A D ^ { \prime } - B C ^ { \prime } = I , } \\ { A ^ { \prime } C - C ^ { \prime } A = O , } & { B ^ { \prime } D - D ^ { \prime } B = O , \quad A ^ { \prime } D - C ^ { \prime } B = I . } \end{array}
$$

Proposition 1.7. Matrices

$$
\left[ \begin{array} { c c } { \boldsymbol { I } } & { \boldsymbol { B } } \\ { \boldsymbol { O } } & { \boldsymbol { I } } \end{array} \right] , \quad \left[ \begin{array} { c c } { \boldsymbol { I } } & { \boldsymbol { O } } \\ { \boldsymbol { D } } & { \boldsymbol { I } } \end{array} \right]
$$

are symplectic, iff $B ^ { \prime } = B , D ^ { \prime } = D$ .

Proposition 1.8. Matrices

$$
{ \left[ \begin{array} { l l } { A } & { O } \\ { O } & { D } \end{array} \right] } \in S p ( 2 n ) , \quad i f f A = ( D ^ { \prime } ) ^ { - 1 } .
$$

Proposition 1.9. Matrices

$$
\begin{array} { r } { S = M ^ { - 1 } N \in S p ( 2 n ) , \quad i f f M J M ^ { \prime } = N J N ^ { \prime } . } \end{array}
$$

Proposition 1.10. Matrices

$$
\left[ \begin{array} { c c } { { Q } } & { { I - Q } } \\ { { - ( I - Q ) } } & { { Q } } \end{array} \right] \in S p ( 2 n ) , \quad i f f Q ^ { 2 } = Q , \quad Q ^ { \prime } = Q .
$$

Proposition 1.11. If $B \in s p ( 2 n )$ , then $\exp \left( B \right) \in S p ( 2 n )$ .

Proposition 1.12. If $B \in s p ( 2 n )$ , and $\vert I + B \vert \ne 0$ , then $F = ( I + B ) ^ { - 1 } ( I - B ) \in$ $S p ( 2 n )$ , the $B$ Cayley transform of $B$ .

Proposition 1.13. If $B \in s p ( 2 n )$ , then $( B ^ { 2 m } ) ^ { \prime } J = J ( B ^ { 2 m } ) ,$ .

Proposition 1.14. If $B \in s p ( 2 n )$ , then $( B ^ { 2 m + 1 } ) ^ { \prime } J = - J ( B ^ { 2 m + 1 } ) .$ .

Proposition 1.15. If $f ( x )$ is an even polynomial, and $B \in s p ( 2 n )$ , then $f ( B ^ { \prime } ) J =$ $J f ( B )$ .

Proposition 1.16. If $g ( x )$ is an odd polynomial, and $B \ \in \ s p ( 2 n )$ , then $g ( B ) \ \in$ $s p ( 2 n )$ , i.e.,

$$
g ( B ^ { \prime } ) J + J g ( B ) = O .
$$

# 4.2 Symplectic Schemes for Linear Hamiltonian Systems

A Hamiltonian system (1.1 ) is called linear, if the Hamiltonian is a quadratic form of $z$ :

$$
H ( z ) = \frac { 1 } { 2 } z ^ { \prime } C z , \quad C ^ { \prime } = C ,
$$

and $J$ is a standard antisymmetric matrix:

$$
J = \left[ \begin{array} { c c } { { O } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { O } } \end{array} \right] , \quad J ^ { \prime } = - J = J ^ { - 1 } , \quad \operatorname* { d e t } J = 1 .
$$

Then, the canonical system (1.1), (1.3) become:

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = B z , \quad B = J ^ { - 1 } C , \quad C ^ { \prime } = C ,
$$

where $B = J ^ { - 1 } C$ is infinitesimal symplectic. The solution of (1.1 ) is:

$$
z ( t ) = g ^ { t } z ( 0 ) , \quad g ^ { t } = \exp { ( t B ) } ,
$$

where $g ^ { t }$ , as the exponential transformation of infinitesimal symplectic $t B$ , is symplectic (Proposition 1.11 ).

Consider now a quadratic form $F ( z ) = \frac { 1 } { 2 } z ^ { \prime } A z$ . The Poisson bracket of two quadratic forms $H , F$ is also a quadratic form:

$$
\{ H , F \} = \frac { 1 } { 2 } z ^ { \prime } ( A J C - C J A ) z .
$$

Theorem 2.1. The condition for the quadratic form $F$ to be an invariant integral of the linear Hamiltonian (2.1) can be expressed in any one of the following equivalent ways:

$$
F \big ( ( \exp { ( t J ^ { - 1 } C ) } ) z \big ) \equiv F ( z ) ,
$$

$$
\{ H , F \} = 0 ,
$$

$$
\big ( \exp { ( t J ^ { - 1 } C ) } \big ) ^ { \prime } A \big ( \exp { ( t J ^ { - 1 } C ) } \big ) = A ,
$$

$$
A J C = C J A .
$$

# 4.2.1 Some Symplectic Schemes for Linear Hamiltonian Systems

Some types of the symplectic schemes for system (1.1 ) are proposed[Fen85] , the first of which is called the time-centered Euler schemes (or midpoint Euler)

$$
{ \frac { z ^ { n + 1 } - z ^ { n } } { \tau } } = B { \frac { z ^ { n + 1 } + z ^ { n } } { 2 } } .
$$

The transition $z ^ { n } \to z ^ { n + 1 }$ is given by

$$
z ^ { n + 1 } = F _ { \tau } z ^ { n } , F _ { \tau } = \phi \Big ( - { \textstyle \frac { \tau } { 2 } } B \Big ) , \phi ( \lambda ) = { \textstyle \frac { 1 - \lambda } { 1 + \lambda } } ,
$$

where $F _ { \tau }$ is a Cayley transformation of the infinitesimal symplectic $- \frac { \tau } { 2 } B$ , and is symplectic according to Proposition 1.12.

The second scheme we consider is the staggered explicit scheme for a separable Hamiltonian. For a separable Hamiltonian $H ( p , q ) = U ( p ) + V ( q )$ ,

$$
H ( p , q ) = { \frac { 1 } { 2 } } [ p ^ { \prime } , q ^ { \prime } ] S { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } = { \frac { 1 } { 2 } } p ^ { \prime } U p + { \frac { 1 } { 2 } } q ^ { \prime } V q = U ( p ) + V ( q ) ,
$$

where

$$
S = \left[ \begin{array} { l l } { { U } } & { { O } } \\ { { O } } & { { V } } \end{array} \right] .
$$

$U ^ { \prime } = U$ is positive definite and $V ^ { \prime } = V$ , the canonical Equation (1.1), becomes:

$$
\frac { \mathrm { d } p } { \mathrm { d } t } = - V _ { q } , \quad \frac { \mathrm { d } q } { \mathrm { d } t } = U _ { p } .
$$

The staggered explicit scheme is:

$$
\begin{array} { l } { { \frac { 1 } { \tau } ( p ^ { n + 1 } - p ^ { n } ) = - V _ { q } ^ { n + \frac { 1 } { 2 } } , } } \\ { { \frac { 1 } { \tau } \left( q ^ { n + \frac { 1 } { 2 } + 1 } - q ^ { n + \frac { 1 } { 2 } } \right) = U _ { p } ^ { n + 1 } . } } \end{array}
$$

$p ^ { \mathrm { T } } s$ are defined at integer time $t = n \tau$ , and $q ^ { \mathrm { T } } s$ at half-integer times $t = \left( n + \frac { 1 } { 2 } \right) \tau$ . The transition

$$
w ^ { n } = \left[ \begin{array} { c } { { p ^ { n } } } \\ { { q ^ { n + \frac { 1 } { 2 } } } } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { { p ^ { n + 1 } } } \\ { { q ^ { n + \frac { 1 } { 2 } + 1 } } } \end{array} \right] = w ^ { n + 1 }
$$

is given by the following:

$$
\boldsymbol { w } ^ { n + 1 } = \boldsymbol { F } _ { \tau } \boldsymbol { w } ^ { n } ,
$$

where

$$
F _ { \tau } = \left[ \begin{array} { c c } { \boldsymbol { I } } & { \boldsymbol { O } } \\ { - \boldsymbol { \tau } \boldsymbol { U } } & { \boldsymbol { I } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { c c } { \boldsymbol { I } } & { - \boldsymbol { \tau } \boldsymbol { V } } \\ { \boldsymbol { O } } & { \boldsymbol { I } } \end{array} \right] ,
$$

as the product of two symplectic matrices, is symplectic (Proposition 1.7 ), and the scheme has second order of accuracy.

# 4.2.2 Symplectic Schemes Based on Pade Approximation ´

We know that the trajectory $z ( t ) = g ^ { t } z _ { 0 }$ is the solution satisfying the initial condition $z ( 0 ) = z _ { 0 }$ . In a linear system, $g ^ { t }$ coincides with its own Jacobian. One might asks how to approximate to of exp $( t B )$ . This can be simply described in terms of Pade rational ´ approximation $[ \mathrm { F W Q 9 0 } , \mathrm { Q i n } 8 9 ]$ . Here, we consider the rational approximation to $\exp \left( x \right)$ defined by

$$
\exp { ( x ) } \sim \frac { n _ { l m } ( x ) } { d _ { l m } ( x ) } = g _ { l m } ( x ) ,
$$

where

$$
\begin{array} { c } { { n _ { l m } ( x ) = \displaystyle \sum _ { k = 0 } ^ { m } \frac { ( l + m - k ) ! m ! } { ( l + m ) ! k ! ( m - k ) ! } x ^ { k } , \nonumber } } \\ { { d _ { l m } ( x ) = \displaystyle \sum _ { k = 0 } ^ { l } \frac { ( l + m - k ) ! l ! } { ( l + m ) ! k ! ( l - k ) ! } ( - x ) ^ { k } . } } \end{array}
$$

For each pair of nonnegative integers $l$ and $m$ , the Taylor series expansion of $\frac { n _ { l m } ( x ) } { d _ { l m } ( x ) }$ about the origin point is:

$$
\exp \left( x \right) - \frac { n _ { l m } ( x ) } { d _ { l m } ( x ) } = o ( | x | ^ { m + l + 1 } ) , \quad | x | \longrightarrow 0 ,
$$

and the resulting $( l + m )$ -th order Pade approximation of ´ $\exp \left( x \right)$ is denoted by $g _ { l m }$

Theorem 2.2. Let $B$ be an infinitesimal symplectic; then, for sufficiently small $| t |$ , $g _ { l m } ( t B )$ is symplectic iff $l = m$ , i.e., $g _ { l l } ( x )$ is the $( l , l )$ diagonal Pade approximant to ´ $\exp \left( x \right)$ .

Proof. Sufficiency. Let $n _ { l l } ( x ) = f ( x ) + g ( x )$ , $d _ { l l } = f ( x ) - g ( x )$ , where $f ( x )$ is an even polynomial, $g ( x )$ is an odd one. In order to prove $g _ { t t } ( t B ) \in S p ( 2 n )$ , we only need to verify Proposition 1.9 .

$$
\bigl ( f ( t B ) + g ( t B ) \bigr ) J \bigl ( f ( t B ) + g ( t B ) \bigr ) ^ { \prime } = \bigl ( f ( t B ) - g ( t B ) \bigr ) J \bigl ( f ( t B ) - g ( t B ) \bigr ) ^ { \prime } .
$$

By Propositions 1.15 and 1.16, the L.H.S of Equation (2.18) is:

$$
\bigl ( f ( t B ) + g ( t B ) \bigr ) J \bigl ( f ( t B ^ { \prime } ) + g ( t B ^ { \prime } ) \bigr ) = \bigl ( f ( t B ) + g ( t B ) \bigr ) \bigl ( f ( t B ) - g ( t B ) \bigr ) J .
$$

Similarly for the R.H.S of Equation (2.18), we have:

$$
\bigl ( f ( t B ) - g ( t B ) \bigr ) J \bigl ( f ( t B ^ { \prime } ) - g ( t B ^ { \prime } ) \bigr ) = \bigl ( f ( t B ) - g ( t B ) \bigr ) \bigl ( f ( t B ) + g ( t B ) \bigr ) J .
$$

Comparing Equations (2.19) and (2.20) completes the proof of the “if” part of the theorem.

The “only if” part. Without loss of generality, we may take $l > m$ . We only need to notice that in Equation (2.18), the order of the polynomial on the right hand is higher than that on the left hand.

From Theorem 2.2, we can obtain a sequence of symplectic difference schemes based on the diagonal $( k , k )$ Pade table. In Table 2.1, the element of l-th row, m-th column is ´ denoted by $( l , m )$ . For the (1,1) approximation (i.e., $l = 1 , m = 1 \AA$ ), we have the Euler centered scheme

$$
\begin{array} { l } { { \displaystyle z ^ { n + 1 } = z ^ { n } + \frac { \tau B } { 2 } ( z ^ { n } + z ^ { n + 1 } ) , } } \\ { { \displaystyle F _ { \tau } ^ { ( 1 , 1 ) } = \phi ^ { ( 1 , 1 ) } ( \tau B ) , } } \\ { { \displaystyle \phi ^ { ( 1 , 1 ) } ( \lambda ) = \frac { 1 + \frac { \lambda } { 2 } } { 1 - \frac { \lambda } { 2 } } . } } \end{array}
$$

This scheme has second order accuracy.

For the (2,2) Pade approximation, we have: ´

$$
z ^ { n + 1 } = z ^ { n } + \frac { \tau B } { 2 } ( z ^ { n } + z ^ { n + 1 } ) + \frac { \tau ^ { 2 } B ^ { 2 } } { 1 2 } ( z ^ { n } - z ^ { n + 1 } ) ,
$$

whose transition is

$$
\begin{array} { c } { { F _ { \tau } ^ { ( 2 , 2 ) } = \phi ^ { ( 2 , 2 ) } ( \tau B ) , } } \\ { { \phi ^ { ( 2 , 2 ) } ( \lambda ) = \displaystyle \frac { 1 + \frac { \lambda } { 2 } + \frac { \lambda ^ { 2 } } { 1 2 } } { 1 - \frac { \lambda } { 2 } + \frac { \lambda ^ { 2 } } { 1 2 } } . } } \end{array}
$$

This scheme has fourth order accuracy.

For the (3,3) approximation, we have:

$$
z ^ { n + 1 } = z ^ { n } + \frac { \tau B } { 2 } ( z ^ { n } + z ^ { n + 1 } ) + \frac { \tau ^ { 2 } B ^ { 2 } } { 1 0 } ( z ^ { n } - z ^ { n + 1 } ) + \frac { \tau ^ { 3 } B ^ { 3 } } { 1 2 0 } ( z ^ { n } + z ^ { n + 1 } ) .
$$

$$
F _ { \tau } ^ { ( 3 , 3 ) } = \phi ^ { ( 3 , 3 ) } ( \tau B ) , \quad \phi ^ { ( 3 , 3 ) } ( \lambda ) = \frac { 1 + \displaystyle { \frac { \lambda } { 2 } } + \frac { \lambda ^ { 2 } } { 1 0 } + \frac { \lambda ^ { 3 } } { 1 2 0 } } { 1 - \displaystyle { \frac { \lambda } { 2 } } + \frac { \lambda ^ { 2 } } { 1 0 } - \displaystyle { \frac { \lambda ^ { 3 } } { 1 2 0 } } } .
$$

This scheme has sixth order accuracy.

For the (4,4) approximation, we have:

$$
\begin{array} { r c l } { { z ^ { n + 1 } } } & { { = } } & { { z ^ { n } + { \displaystyle \frac { \tau B } { 2 } } ( z ^ { n } + z ^ { n + 1 } ) + { \displaystyle \frac { 3 \tau ^ { 2 } B ^ { 2 } } { 2 8 } } ( z ^ { n } - z ^ { n + 1 } ) } } \\ { { } } & { { } } & { { + { \displaystyle \frac { \tau ^ { 3 } B ^ { 3 } } { 8 4 } } ( z ^ { n } + z ^ { n + 1 } ) + { \displaystyle \frac { \tau ^ { 4 } B ^ { 4 } } { 1 6 8 0 } } ( z ^ { n } - z ^ { n + 1 } ) , } } \\ { { } } & { { } } & { { } } \\ { { { \cal F } _ { \tau } ^ { ( 4 , 4 ) } } } & { { = } } &  { \phi ^ { ( 4 , 4 ) } ( \tau B ) , \quad \phi ^ { ( 4 , 4 ) } ( \lambda ) = { \displaystyle \frac { 1 + \frac { \lambda } { 2 } + { \displaystyle \frac { 3 \lambda ^ { 2 } } { 2 8 } } + { \displaystyle \frac { \lambda ^ { 3 } } { 8 4 } } + { \displaystyle \frac { \lambda ^ { 4 } } { 1 6 8 0 } } } { 1 - \frac { \lambda } { 2 } + { \displaystyle \frac { 3 \lambda ^ { 2 } } { 2 8 } } - { \displaystyle \frac { \lambda ^ { 3 } } { 8 4 } } + { \displaystyle \frac { \lambda ^ { 4 } } { 1 6 8 0 } } } . } } \end{array}
$$

This scheme has eighth order accuracy.

Theorem 2.3. The difference schemes

$$
z ^ { n + 1 } = g _ { l l } ( \tau B ) z ^ { k } , \quad l = 1 , 2 , \cdot \cdot \cdot
$$

for a linear Hamiltonian system (2.1) are symplectic of $2 l$ -th order accuracy .

.1. Pad´e approximation table   

<table><tr><td>1 m</td><td colspan="2">0</td><td colspan="2"></td><td colspan="8">2 3</td></tr><tr><td></td><td colspan="3"></td><td colspan="4"></td><td colspan="7">4</td></tr><tr><td rowspan="2">0</td><td rowspan="2">1</td><td colspan="2"></td><td colspan="2"></td><td colspan="5"></td><td colspan="5"></td></tr><tr><td>1 1-x</td><td></td><td>1 3</td><td></td><td colspan="3">1</td><td>1</td><td colspan="3"></td></tr><tr><td rowspan="2"></td><td colspan="2"></td><td colspan="3">1-x+</td><td colspan="3">x² x 1-x+ 2 6</td><td colspan="2">1-x+</td><td colspan="3">m4 2 2 + 2 6 24</td></tr><tr><td colspan="2">1+x</td><td></td><td colspan="2">x</td><td colspan="2"></td><td colspan="3"></td><td colspan="5"></td></tr><tr><td colspan="2"></td><td>中 1+ 1</td><td></td><td>1+ 3 2 x</td><td></td><td>3x x x</td><td colspan="2">x 1+ 4</td><td>1+</td><td colspan="2">4 3²</td><td colspan="2">5 x 24</td></tr><tr><td>2</td><td colspan="2">m²</td><td>x² 2x</td><td colspan="2">1 一 3 6 x²</td><td colspan="2"></td><td>4 4 24</td><td colspan="2"></td><td>5</td><td colspan="2">10 15 120</td></tr><tr><td></td><td>1+x+ 2 1</td><td>1+ 3 + 6 x 1- 3</td><td></td><td>x 1+ 2 12 × x 的</td><td></td><td>1+ 3 x2 x</td><td>2x + 20 5</td><td>x²</td><td>1+</td><td colspan="2">x² X 3 +</td><td>30</td><td>x R4</td></tr><tr><td colspan="2">1+x+ 3</td><td>3x 8 1+</td><td>x² x 1+ + +</td><td>1- 2 + 12 3x</td><td>3x² 2</td><td></td><td colspan="2">5 20 60 2 2</td><td>1-</td><td colspan="2">+ 30 3 20</td><td></td><td>+ 360 x 2</td><td></td></tr><tr><td></td><td>2 6 1 2 2 +</td><td>4 4 1- x 4</td><td>24</td><td>5 1- + 5</td><td>20 60 2x x² 20</td><td>x 1- 2</td><td>2 +</td><td>10 x² x</td><td>+ 120</td><td>1+ 4x</td><td>7 + 14 x²</td><td></td><td>X 210 43</td><td>84</td></tr><tr><td colspan="2">+x+ 4</td><td>4 3x² 24 + 1 + + + 24 5 10</td><td>2 04 + + 15 120</td><td>2x + + 3 20 30</td><td>x² x</td><td>+ 2 +</td><td>4x + +</td><td>x² 4x</td><td>x4</td><td>x</td><td>3x²</td><td></td><td>x</td><td>x4</td></tr><tr><td colspan="2"></td><td></td><td>1- 5</td><td>1-</td><td>X</td><td>360 3</td><td></td><td>3 22</td><td></td><td>210 840 2</td><td>2</td><td>+ 28</td><td>+ + 84</td><td>1680</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td>+</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td>7</td><td></td><td></td><td></td><td></td><td>3x²</td><td>2</td><td>2</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td>3</td><td>30</td><td></td><td>+</td><td></td><td>1</td><td>X +</td><td></td><td>+</td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>210</td><td>2</td><td>28</td><td>84</td><td>1680</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2"></td><td></td></table>

# 4.2.3 Generalized Cayley Transformation and Its Application

Definition 2.4. A matrix $B$ is called non-exceptional, if

$$
\operatorname* { d e t } \left( I + B \right) \neq 0 .
$$

Let $B$ be non-exceptional; let us introduce a matrix $S$ by

$$
I + S = 2 ( I + B ) ^ { - 1 } ,
$$

whose inversion is

$$
I + B = 2 ( I + S ) ^ { - 1 } .
$$

Therefore $S$ is non-exceptional, and we have the Cayley transformation $\left[ \mathrm { F W Q 9 0 } \right]$ :

$$
S = ( I - B ) ( I + B ) ^ { - 1 } = ( I + B ) ^ { - 1 } ( I - B ) ,
$$

and

$$
B = ( I - S ) ( I + S ) ^ { - 1 } = ( I + S ) ^ { - 1 } ( I - S ) .
$$

Let $A$ be an arbitrary matrix. The equation

$$
S ^ { \prime } A S = A
$$

expresses the condition that the substitution of $S$ into both variables $z , w$ leaves invariant the bilinear form $z ^ { \prime } A w$ .

Lemma 2.5. [Wey39] If the non-exceptional matrices $B$ and $S$ are connected by (2.32) and (2.33), and $A$ is an arbitrary matrix, then

$$
S ^ { \prime } A S = A
$$

iff

$$
B ^ { \prime } A + A B = O .
$$

Proof. Taking the transpose of (2.33), we obtain

$$
B ^ { \prime } ( I + S ^ { \prime } ) = I - S ^ { \prime } .
$$

Right multiplying by $A S$ on both sides, and from (2.35), we obtain

$$
A ( S - I ) = B ^ { \prime } A ( S + I ) .
$$

Right multiplying by $( S + I ) ^ { - 1 }$ again on both sides, we obtain

$$
- A B = B ^ { \prime } A .
$$

Conversely, by assuming (2.36) and right multiplying the transposed equation

$$
S ^ { \prime } ( I + B ^ { \prime } ) = I - B ^ { \prime }
$$

of (2.33) by $A$ on both sides, we have

$$
S ^ { \prime } A ( I - B ) = A ( I + B ) ,
$$

which yields (2.35) on post-multiplication by $( I + B ) ^ { - 1 }$

Let $\phi ( \lambda ) = ( 1 - \lambda ) / ( 1 + \lambda )$ ; then the Cayley transform of $B$ is denoted by $\phi ( B ) = ( I + B ) ^ { - 1 } / ( I - B )$ . By taking successively $A = J$ and $A = A ^ { \prime }$ in Lemma 2.5, this lemma is proved.

Theorem 2.6. The Cayley Transform of a non-exceptional infinitesimal symplectic (symplectic) matrix is a non-exceptional symplectic (infinitesimal symplectic) matrix. If $B = J ^ { - 1 } C , C ^ { \prime } = C , B \in s p ( 2 n ) , \operatorname * { d e t } \left( I + \tau B \right) \neq 0 , A ^ { \prime } = A ,$ , then

$$
\left( \phi ( \tau B ) \right) ^ { \prime } A \left( \phi ( \tau B ) \right) = A
$$

iff

$$
B ^ { \prime } A + A B = O .
$$

In other words, a quadratic form $F ( z ) = { \frac { 1 } { 2 } } z ^ { \prime } A z$ is invariant under the symplectic transformation $\phi ( \tau B )$ iff $F ( z )$ is an invariant integral of the Hamiltonian system (2.1).

Theorem 2.7. $[ \mathrm { F W Q 9 0 } ]$ Let $\psi ( \lambda )$ be a function of a complex variable $\lambda$ , satisfying: $1 ^ { \circ }$ $\psi ( \lambda )$ is analytic with real coefficients in a neighborhood $D$ of $\lambda = 0$ . $2 ^ { \circ }$ $\psi ( \lambda ) \psi ( - \lambda ) = 1$ in $D$ . $3 ^ { \circ }$ $\psi _ { \lambda } ( 0 ) \neq 0$ . Let $A , B$ be matrices of order $2 n$ . Then,

$$
{ \big ( } \psi ( \tau B ) { \big ) } ^ { \prime } A { \big ( } \psi ( \tau B ) { \big ) } = A ,
$$

for all $\tau$ with sufficient small $| \tau |$ , iff

$$
B ^ { \prime } A + A B = O .
$$

We call these $\psi ( \lambda )$ the generalized Cayley transformation.

Proof. Condition $2 ^ { \circ }$ implies $\psi ^ { 2 } ( 0 ) \neq 0$ . Thus, $\boldsymbol { \psi } ( 0 ) \neq 0$ , if

$$
{ \big ( } \psi ( \tau B ) { \big ) } ^ { \prime } A { \big ( } \psi ( \tau B ) { \big ) } = A ,
$$

for all $\tau$ with $| \tau |$ sufficiently small. Then, differentiating both sides of the above equation with respect to $\tau$ , we get

$$
B ^ { \prime } \big ( \psi _ { \lambda } ( \tau B ) \big ) ^ { \prime } A \psi ( \tau B ) + \big ( \psi ( \tau B ) \big ) ^ { \prime } A B \psi _ { \lambda } ( \tau B ) = O .
$$

Setting $\tau = 0$ , it becomes

$$
( B ^ { \prime } A + A B ) \psi ( 0 ) \psi _ { \lambda } ( 0 ) = O .
$$

From condition $3 ^ { \circ }$ , we get

$$
B ^ { \prime } A + A B = O .
$$

Conversely, if $B ^ { \prime } A + A B = 0$ , then it is not difficult to verify that the equations

$$
\psi _ { \lambda } ( \tau B ^ { \prime } ) A = A \psi _ { \lambda } ( \tau B ) , \quad \psi ( \tau B ^ { \prime } ) A = A \psi ( - \tau B )
$$

hold good for any analytic function $\psi$ . From condition $2 ^ { \circ }$ , it follows that

$$
\psi _ { \lambda } ( \lambda ) \psi ( - \lambda ) - \psi ( \lambda ) \psi _ { \lambda } ( - \lambda ) = 0 .
$$

Therefore,

$$
\begin{array} { r l } & { \frac { \textnormal { d } } { \textnormal { d } \tau } \big ( \psi ( \tau B ) ^ { \prime } A \psi ( \tau B ) \big ) } \\ & { \ = \frac { \textnormal { d } } { \textnormal { d } \tau } \big ( \psi ( \tau B ^ { \prime } ) A \psi ( \tau B ) \big ) } \\ & { \ = B ^ { \prime } \psi _ { \lambda } ( \tau B ^ { \prime } ) A \psi ( \tau B ) + \psi ( \tau B ^ { \prime } ) A B \psi _ { \lambda } ( \tau B ) } \\ & { \ = B ^ { \prime } A \psi _ { \lambda } ( - \tau B ) \psi ( \tau B ) + A B \psi _ { \lambda } ( - \tau B ) \psi ( \tau B ) } \\ & { \ = ( B ^ { \prime } A + A B ) \psi _ { \lambda } ( - \tau B ) \psi ( \tau B ) = O , } \end{array}
$$

$$
\psi ( \tau B ^ { \prime } ) A \psi ( \tau B ) = \psi ( 0 ) A \psi ( 0 ) = A \psi ^ { 2 } ( 0 ) = A .
$$

The proof is completed.

By taking successively $A = J$ and $A ^ { \prime } = A$ in Theorem 2.8 and using (2.3) – (2.6), we obtain the following theorems.

Theorem 2.8. Take $| \tau |$ sufficiently small so that $\tau B$ has no eigenvalue at the pole of the function $\phi ( \lambda )$ in Theorem 2.7. Then, $\psi ( \tau B ) \in S p ( 2 n )$ iff $B \in \mathop { s p } ( 2 n )$ . Let $B = J ^ { - 1 } C , C ^ { \prime } = C , A ^ { \prime } = A$ ; then,

$$
\psi ( \tau J ^ { - 1 } C ) ^ { \prime } A \psi ( \tau J ^ { - 1 } C ) = A ,
$$

iff

$$
A J C = C J A .
$$

In other words, a quadratic form $F ( z ) = \frac { 1 } { 2 } z ^ { \prime } A z$ 12 z Az, is invariant under the symplectic transformation $\psi ( \tau B )$ , iff $F ( z )$ is an invariant integral of the system (2.1).

The transformation $\phi ( \tau B )$ based on Theorem 2.7 includes exponential transformation $\exp ( \tau B )$ , Cayley transformation $\scriptstyle \psi ( - \tau B / 2 )$ , and diagonal Pade transforma- ´ tion as special cases. Taking $\phi ( \lambda )$ in Theorem 2.7 as a rational function, then necessarily $\begin{array} { r } { \psi ( \lambda ) = \frac { P ( \lambda ) } { P ( - \lambda ) } } \end{array}$ , $P ( \lambda )$ is a polynomial, and is often normalized by setting $P ( 0 ) = 1$ , $P ^ { \prime } ( 0 ) \neq 0$ .

Theorem 2.9. Let $P ( \lambda )$ be a polynomial $P ( 0 ) = 1$ , $P ^ { \prime } ( 0 ) \neq 0$ , and

$$
\exp \left( \lambda \right) - \frac { P ( \lambda ) } { P ( - \lambda ) } = O \left( | \lambda | ^ { 2 k + 1 } \right) .
$$

Then,

$$
P ( - \tau B ) z ^ { m + 1 } = P ( \tau B ) z ^ { m } ,
$$

i.e.,

$$
z ^ { m + 1 } = \frac { P ( \tau B ) } { P ( - \tau B ) } z ^ { m }
$$

is a symplectic scheme of order $2 k$ for a linear system (2.1). This difference scheme and the original system (2.1) have the same set of quadratic invariants.

In order to find the approximate $\frac { P ( x ) } { P ( - x ) }$ to $\exp \left( x \right)$ , we may express $\exp ( x )$ in various rational fraction ways. The following are examples:

$$
\begin{array} { l l l } { \exp { ( x ) } \sim \displaystyle \frac { n u ( x ) } { n \displaystyle u ( - x ) } = \frac { d _ { l l } ( - x ) } { d _ { l l } ( x ) } . } & { ( 2 ) } & { \exp { ( x ) } \sim \displaystyle \frac { 1 } { 2 } g _ { l m } ( x ) \cdot \frac { 1 } { 2 } g _ { m l } ( x ) . } \\ { \exp { ( x ) } = \displaystyle \frac { 1 + \operatorname { t a n h } \frac { x } { 2 } } { 1 - \operatorname { t a n h } \frac { x } { 2 } } . } & { ( 4 ) } & { \exp { ( x ) } = \frac { \mathrm { e } ^ { \frac { x } { 2 } } } { \mathrm { e } ^ { - \frac { x } { 2 } } } . } \\ { \exp { ( x ) } = \displaystyle \frac { \frac { 1 } { 2 } ( 1 + \mathrm { e } ^ { x } ) } { \frac { 1 } { 2 } ( 1 + \mathrm { e } ^ { - x } ) } . } \end{array}
$$

Each denominator and numerator in the above expressions can be expanded about the origin in Taylor series. The first term of the approximation gives the function $\psi ( x ) \stackrel { \smile } { = } \big ( 1 + { \frac { x } { 2 } } \big ) \big / \big ( 1 - { \frac { x } { 2 } } \big )$ , which yields the Euler centered scheme. Keeping $m ( > 1 )$ terms in the expansions for both the denominator and numerator, we will get a function $\psi ( x )$ that will extend the Euler centered schemes. The schemes obtained in this way are all symplectic; however, the order of accuracy of the first and third schemes is higher than that of the last two kinds. For example, if in the formula (5) the first three terms of the expansions of the denominator and numerator are retained, then the 4-th order symplectic scheme is obtained. However, the same kind of truncation gives 6-th order schemes from (1) and (3).

# 4.3 Symplectic Difference Schemes for a Nonlinear Hamiltonian System

For a nonlinear Hamiltonian system, we give some simple symplectic difference schemes.

Centered Euler scheme. For Equation (1.3), we give Euler centered schemes [Fen85] :

$$
\frac { 1 } { \tau } ( z ^ { m + 1 } - z ^ { m } ) = J ^ { - 1 } H _ { z } \left( \frac { z ^ { m + 1 } + z ^ { m } } { 2 } \right) ,
$$

where the mapping $F _ { \tau } \colon z ^ { m } \to z ^ { m + 1 }$ is nonlinear. By differentiation,

$$
\frac { \partial z ^ { m + 1 } } { \partial z ^ { m } } = I + \tau J ^ { - 1 } H _ { z z } \left( \frac { z ^ { m + 1 } + z ^ { m } } { 2 } \right) \left( \frac { 1 } { 2 } \frac { \partial z ^ { m + 1 } } { \partial z ^ { m } } + \frac { 1 } { 2 } I \right) ,
$$

where $H _ { z z } \left( \frac { z ^ { m + 1 } + z ^ { m } } { 2 } \right)$ is the Hessian matrix of the function $H ( z )$ at point $z =$ $\frac { z ^ { m + 1 } + z ^ { m } } { 2 }$ , and 1 $\frac { \partial z ^ { m + 1 } } { \partial z ^ { m } }$ is the Jacobian matrix of $F _ { \tau }$ . We have

$$
F _ { \tau } = \left[ I - \frac { \tau } { 2 } J ^ { - 1 } H _ { z z } \Big ( \frac { z ^ { m + 1 } + z ^ { m } } { 2 } \Big ) \right] ^ { - 1 } \left[ I + \frac { \tau } { 2 } J ^ { - 1 } H _ { z z } \Big ( \frac { z ^ { m + 1 } + z ^ { m } } { 2 } \Big ) \right] .
$$

When $z$ remains bounded and by taking $\tau$ to be sufficiently small, we can keep the infinitesimally symplectic matrix $\frac { \tau } { 2 } J ^ { - 1 } H _ { z z } \left( \frac { z ^ { m + 1 } + z ^ { m } } { 2 } \right)$ non-exceptional. Then, $F _ { \tau }$ as a Cayley transform is symplectic. Thus, all the conservation laws for phase areas remain true. However, unlike the linear case, the first integral $\phi ( x )$ including $H$ itself are not conserved exactly. Indeed, it satisfies conservation law only nearby:

$$
\varphi ( z ^ { m + 1 } ) = \varphi ( z ^ { m } ) \mod { o ( \tau ^ { 3 } ) } .
$$

Property 3.1. Let $f ( z ) = { \frac { 1 } { 2 } } z ^ { \prime } B z$ be a conservation law for the Hamiltonian system (1.3). Then, it is also a conservation law of the Euler centered scheme for system (1.3).

Proof.

$$
\begin{array} { r l } & { \Big \langle B ( z ^ { k + 1 } + z ^ { k } ) , \frac { z ^ { k + 1 } - z ^ { k } } { \tau } \Big \rangle } \\ & { \quad = \Big \langle B ( z ^ { k + 1 } + z ^ { k } ) , J ^ { - 1 } H _ { z } \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) \Big \rangle } \\ & { \quad = \Big \langle ( z ^ { k + 1 } + z ^ { k } ) , B J ^ { - 1 } H _ { z } \Big ( \frac { z ^ { k + 1 } + z ^ { k } } { 2 } \Big ) \Big \rangle = 0 , } \end{array}
$$

and so

$$
\langle B z ^ { k } , z ^ { k } \rangle = \langle B z ^ { k + 1 } , z ^ { k + 1 } \rangle .
$$

The proof is proved.

The last equation comes from the conservation law of original system.

Remark 3.2. As Euler centered schemes, high-order schemes constructed by the diagonal element in the Pade table preserve all quadratic first integrals of the original ´ Hamiltonian system.

It is worth to point out that the trapezoidal scheme:

$$
\frac { 1 } { \tau } \left( z ^ { m + 1 } - z ^ { m } \right) = J ^ { - 1 } \frac { 1 } { 2 } \left( H _ { z } ( z ^ { m + 1 } ) + H _ { z } ( z ^ { m } ) \right)
$$

is non-symplectic, because the transition

$$
F _ { \tau } = \left[ I - \frac { \tau } { 2 } J ^ { - 1 } H _ { z z } ( z ^ { m + 1 } ) \right] ^ { - 1 } \left[ I + \frac { \tau } { 2 } J ^ { - 1 } H _ { z z } ( z ^ { m } ) \right]
$$

is non-symplectic in general. By a nonlinear transformation [Dah59,QZZ95] ,

$$
\xi ^ { k } = \rho ( z ^ { k } ) = z ^ { k } + \frac { h } { 2 } f ( z ^ { k } ) , \quad \xi ^ { k + 1 } = \rho ( z ^ { k + 1 } ) = z ^ { k + 1 } + \frac { h } { 2 } f ( z ^ { k + 1 } ) ,
$$

and the trapezoidal scheme can be transformed into a symplectic Euler centered scheme

$$
\xi ^ { k } + \xi ^ { k + 1 } = z ^ { k } + z ^ { k + 1 } + { \frac { h } { 2 } } { \big ( } f ( z ^ { k } ) + f ( z ^ { k + 1 } ) { \big ) } .
$$

Applying (3.2) to the above formula, we get

$$
\xi ^ { k } + \xi ^ { k + 1 } = z ^ { k } + z ^ { k + 1 } + z ^ { k + 1 } - z ^ { k } = 2 z ^ { k + 1 } .
$$

By taking zk+1 = $z ^ { k + 1 } = { \frac { \xi ^ { k } + \xi ^ { k + 1 } } { 2 } }$ in the second equation of (3.3), we obtain

$$
\xi ^ { k + 1 } = \frac { \xi ^ { k } + \xi ^ { k + 1 } } { 2 } + \frac { h } { 2 } f \left( \frac { \xi ^ { k } + \xi ^ { k + 1 } } { 2 } \right) ,
$$

i.e.,

$$
\xi ^ { k + 1 } = \xi ^ { k } + h f \left( \frac { \xi ^ { k } + \xi ^ { k + 1 } } { 2 } \right) ,
$$

which is a Euler centered scheme.

Theorem 3.3. The trapezoidal scheme (3.2) preserves the following symplectic structure[WT03] :

$$
J + \frac { h ^ { 2 } } { 4 } H _ { z z } ( z ) J H _ { z z } ( z ) ,
$$

i.e.,

$$
\left( \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } \right) ^ { \prime } \left( J + \frac { h ^ { 2 } } { 4 } H _ { z z } ( z ^ { k + 1 } ) J H _ { z z } ( z ^ { k + 1 } ) \right) \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } = J + \frac { h ^ { 2 } } { 4 } H _ { z z } ( z ^ { k } ) J H _ { z z } ( z ^ { k } )
$$

Proof. The proof can be easily obtained by direct calculation using nonlinear transform of (3.3) to (1.7).

Remark 3.4. For the canonical system with general separable Hamiltonian, $H ( p , q ) =$ $U ( p ) + V ( q )$ , and we have

$$
\begin{array} { c } { \displaystyle \frac { \mathrm { d } q } { \mathrm { d } t } = - V _ { q } ( q ) , \quad \displaystyle \frac { \mathrm { d } p } { \mathrm { d } t } = U _ { p } ( p ) , } \\ { \displaystyle \frac { 1 } { \tau } \left( p ^ { m + 1 } - p ^ { m } \right) = - V _ { q } ( q ^ { m + \frac { 1 } { 2 } } ) , } \\ { \displaystyle \frac { 1 } { \tau } \left( q ^ { m + 1 + \frac { 1 } { 2 } } - q ^ { m + \frac { 1 } { 2 } } \right) = U _ { p } ( p ^ { m + 1 } ) . } \end{array}
$$

The transition $F _ { \tau } : [ \begin{array} { c } { { p ^ { m } } } \\ { { q ^ { m + \frac { 1 } { 2 } } } } \end{array} ]  [ \begin{array} { c } { { p ^ { m + 1 } } } \\ { { q ^ { m + 1 + \frac { 1 } { 2 } } } } \end{array} ]$ has the Jacobian:

$$
F _ { \tau } = \left[ \begin{array} { c c } { { I } } & { { O } } \\ { { - \tau M } } & { { I } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { c c } { { I } } & { { - \tau L } } \\ { { O } } & { { I } } \end{array} \right] .
$$

From Proposition 1.7, it is symplectic, but with $M = U _ { p p } ( p ^ { m + 1 } )$ , $L = V _ { q q } ( q ^ { m + \frac { 1 } { 2 } } )$ .

Property 3.5. Let $f ( p , q ) = p ^ { \prime } B q$ be a conservation law of (3.5). Then, $( p ^ { k + 1 } ) ^ { \prime } B q ^ { k + \frac { 3 } { 2 } }$ $= ( p ^ { k } ) ^ { \prime } B q ^ { k + \frac { 1 } { 2 } }$ is a conservation law of the difference scheme (3.6) also.

Proof. Indeed, because $f ( p , q )$ is a conservation law of the original Hamiltonian system

$$
\big ( B p , U _ { p } ( p ) \big ) = 0 , \quad \big ( B q , V _ { q } ( q ) \big ) = 0 ,
$$

we get

$$
\left( \frac { q ^ { k + \frac { 3 } { 2 } } - q ^ { k + \frac { 1 } { 2 } } } { \tau } , B p ^ { k + 1 } \right) = \left( U _ { p } ( p ^ { k + 1 } ) , B p ^ { k + 1 } \right) = 0 ,
$$

$$
\left( \frac { p ^ { k + 1 } - p ^ { k } } { \tau } , B q ^ { k + \frac { 1 } { 2 } } \right) = \left( V _ { q } ( q ^ { k + \frac { 1 } { 2 } } ) , B q ^ { k + \frac { 1 } { 2 } } \right) = 0 .
$$

Subtracting the two equations above, we get

$$
( B p ^ { k + 1 } , q ^ { k + \frac { 3 } { 2 } } ) = ( B p ^ { k } , q ^ { k + \frac { 1 } { 2 } } ) .
$$

The proof can be obtained.

# 4.4 Explicit Symplectic Scheme for Hamiltonian System

The oldest and simplest difference scheme is the explicit Euler method. Usually, it is not symplectic for general Hamiltonian systems. It is interesting to ask: under what condition of Hamiltonian systems, can the explicit Euler method become symplectic? In fact, the explicit Euler scheme should be the phase flow of a system (i.e., exact solution) to be symplectic. Most of the important Hamiltonian systems can be decomposed into the sum of these simple systems. Then, the composition of the Euler method acting on these systems yields a symplectic method, which is also explicit. These systems are called symplectically separable. So classical separable Hamiltonian systems are symplectically separable. In this section, we will prove that any polynomial Hamiltonian is symplectically separable.

# 4.4.1 Systems with Nilpotent of Degree 2

For a Hamiltonian system (1.3), the oldest and simplest is the explicit Euler scheme:

$$
\widehat { z } = E _ { H } ^ { \tau } z : = z + \tau J H _ { z } ( z ) ,
$$

where $E _ { H } ^ { \tau } = 1 + \tau J H _ { z }$ . Usually, the scheme (4.1) is non-symplectic. However, it is symplectic for a specific kind of Hamiltonian system, called a system with nilpotent of degree 2.

Definition 4.1. [FW98] A Hamiltonian system is nilpotent of degree 2 if it satisfies

$$
J H _ { z z } ( z ) J H _ { z } ( z ) = 0 , \quad \forall z \in \mathbf { R } ^ { 2 n } .
$$

Evidently, $H ( p , q ) = \phi ( p )$ or $H ( p , q ) = \psi ( q )$ , which represents inertial flow and stagnant flow, are nilpotent of degree 2 since for ${ \cal H } ( p , q ) = \phi ( p )$ ,

$$
H _ { z z } ( z ) J H _ { z } ( z ) = \left[ \begin{array} { c c } { \phi _ { p p } } & { O } \\ { O } & { O } \end{array} \right] \left[ \begin{array} { c c } { O } & { - I } \\ { I } & { O } \end{array} \right] \left[ \begin{array} { c } { \phi _ { p } } \\ { O } \end{array} \right] = \left[ \begin{array} { c c } { \phi _ { p p } } & { O } \\ { O } & { O } \end{array} \right] \left[ \begin{array} { c } { O } \\ { \phi _ { p } } \end{array} \right] = O ( \phi _ { p } ) .
$$

and for $H ( p , q ) = \psi ( q )$ ,

$$
H _ { z z } ( z ) J H _ { z } ( z ) = { \left[ \begin{array} { l l } { O } & { O } \\ { O } & { \psi _ { q q } } \end{array} \right] } { \left[ \begin{array} { l l } { O } & { - I } \\ { I } & { O } \end{array} \right] } { \left[ \begin{array} { l } { O } \\ { \psi _ { q } } \end{array} \right] } = { \left[ \begin{array} { l l } { O } & { O } \\ { O } & { \psi _ { q q } } \end{array} \right] } { \left[ \begin{array} { l } { - \psi _ { q } } \\ { O } \end{array} \right] } = O .
$$

Theorem 4.2. If $H$ is nilpotent of degree 2, then the explicit Euler scheme $E _ { H } ^ { \tau }$ is the exact phase flow of the Hamiltonian system, and hence symplectic.

Proof. Let $z = z ( 0 )$ . From the condition (4.2), it follows that

$$
\ddot { z } ( t ) = \frac { \mathrm { d } } { \mathrm { d } t } J H _ { z } ( z ( t ) ) = ( J H _ { z } ( z ( t ) ) ) _ { z } \dot { z } ( t ) = J H _ { z z } ( z ( t ) ) J H _ { z } ( z ( t ) ) = 0 ,
$$

and therefore,

$$
\dot { z } ( t ) = \dot { z } ( 0 ) = J H _ { z } ( z ( 0 ) ) .
$$

Hence,

$$
z ( t ) = z ( 0 ) + t J H _ { z } ( z ( 0 ) ) = z + t J H _ { z } ( z ) = E _ { H } ^ { t } ( z ) .
$$

This is just the explicit Euler scheme $E _ { H } ^ { t }$ . This shows that for such a system, the explicit Euler scheme $E _ { H } ^ { \tau }$ is the exact phase flow, and therefore symplectic. $\blacktriangle$

Theorem 4.3. Let $\phi ( u ) : \mathbf { R } ^ { n } \to \mathbf { R }$ be a function on $n$ variables $u$ , $\phi ( u ) = \phi ( u _ { 1 } ,$ , $u _ { 2 } , \cdots , u _ { n } )$ . Let $C _ { n \times 2 n } = ( A , B )$ be a linear transformation from $\mathbf { R } ^ { 2 n }$ to $\mathbf { R } ^ { n }$ . Then, the Hamiltonian $H ( z ) = \phi ( C z )$ satisfies

$$
J H _ { z z } ( z ) J H _ { z } ( z ) = O , \quad \forall \phi , z ,
$$

iff

$$
C J C ^ { \mathrm { T } } = O .
$$

Proof. Since

$$
J H _ { z z } ( z ) J H _ { z } ( z ) = J C ^ { \mathrm { T } } \phi _ { u u } ( C J C ^ { \mathrm { T } } \phi _ { u } ( C z ) ) ,
$$

the sufficient condition is trivial.

We now prove the necessity. If

$$
J H _ { z z } ( z ) J H _ { z } ( z ) = O , \quad \forall \phi , z ,
$$

then from (4.5) it follows that

$$
\begin{array} { r } { J C ^ { \mathrm { T } } \phi _ { u u } ( C z ) ( J C ^ { \mathrm { T } } \phi _ { u } ( C z ) = O , \quad \forall \phi , z . } \end{array}
$$

Especially take $\phi ( u ) = \frac { 1 } { 2 } u ^ { \mathrm { T } } u$ , then

$$
J C ^ { \mathrm { T } } C J C ^ { \mathrm { T } } C z = O , \quad \forall z ,
$$

i.e.,

$$
J C ^ { \mathrm { T } } C J C ^ { \mathrm { T } } C = O .
$$

Left multiplying by $C$ and right multiplying $J C ^ { \mathrm { T } }$ by this equation, we get:

$$
( C J C ^ { \mathrm { T } } ) ^ { 3 } = O .
$$

The anti-symmetry of $C J C ^ { \mathrm { { T } } }$ implies $C J C ^ { \mathrm { T } } = O$ .

Lemma 4.4. Let $C = ( A , B )$ ; then $C J C ^ { \mathrm { T } } = O$ , if and only if $A B ^ { \mathrm { T } } = B A ^ { \mathrm { T } }$ .

Theorem 4.5. For any Hamiltonian system:

$$
H ( z ) = H ( p , q ) = \phi ( C z ) = \phi ( A p + B q ) , \quad A B ^ { \mathrm { T } } = B A ^ { \mathrm { T } } ,
$$

where $\phi ( u )$ is any $n$ variable function. The explicit Euler method

$$
\widehat { z } = E _ { H } ^ { \tau } z = E _ { \phi } ^ { \tau } z = z + \tau J H _ { z } ( z ) = z + \tau J C ^ { \mathrm { T } } \phi _ { u } ( C z )
$$

is the exact phase flow, i.e.,

$$
e _ { \phi } ^ { \tau } : = E _ { \phi } ^ { \tau } = 1 + \tau J H _ { z } = 1 + \tau J C ^ { \mathrm { T } } \phi _ { u } \circ C ,
$$

hence, $E _ { \phi } ^ { \tau }$ is symplectic.

# 4.4.2 Symplectically Separable Hamiltonian Systems

Definition 4.6. $\mathrm { [ F W 9 8 , F Q 9 1 ] }$ Hamiltonian $H ( z )$ is separable, if

$$
H ( z ) = \sum _ { i = 1 } ^ { m } H _ { i } ( z ) , \quad H _ { i } ( z ) = \phi _ { i } ( C _ { i } z ) = \phi ( A _ { i } p + B _ { i } q ) ,
$$

where $\phi _ { i }$ are functions of $n$ variables and ${ \cal C } _ { i } ~ = ~ ( A _ { i } , B _ { i } )$ satisfies the condition $A _ { i } B _ { i } ^ { \mathrm { T } } = B _ { i } A _ { i } ^ { \mathrm { T } }$ $( i = 1 , \cdots , m )$ ). Obviously, we have the following proposition.

Proposition 4.7. A linear combination of a symplectic separable Hamiltonian is symplectically separable.

For a symplectically separable Hamiltonian (4.6), the explicit composition scheme

$$
\begin{array} { l l l } { g _ { H } ^ { \tau } } & { = } & { E _ { m } ^ { \tau } \circ E _ { m - 1 } ^ { \tau } \circ \cdot \cdot \cdot \circ E _ { 2 } ^ { \tau } \circ E _ { 1 } ^ { \tau } } \\ & { : = } & { E _ { H _ { m } } ^ { \tau } \circ E _ { H _ { m - 1 } } ^ { \tau } \circ \cdot \cdot \cdot \circ E _ { H _ { 2 } } ^ { \tau } \circ E _ { H _ { 1 } } ^ { \tau } } \end{array}
$$

is symplectic and of order 1. As a matter of fact:

$$
\begin{array} { r l } { F _ { H _ { 2 } } ^ { \prime } \circ F _ { H _ { 1 } } ^ { \prime } } & { = \phantom { \iota } ( 1 + \tau J H _ { 2 , z } ) \circ ( 1 + \tau J H _ { 1 , z } ) } \\ & { = \phantom { \iota } 1 + \tau J H _ { 2 , z } + \tau J H _ { 1 , z } + O ( \tau ^ { 2 } ) } \\ & { = \phantom { \iota } 1 + \tau J ( H _ { 2 , z } + H _ { 1 , z } ) + O ( \tau ^ { 2 } ) , } \\ { g _ { H } ^ { \prime } } & { = \phantom { \iota } F _ { m } ^ { \prime } \circ F _ { m - 1 } ^ { \prime } \circ \cdots \circ F _ { 2 } ^ { \prime } \circ F _ { 1 } ^ { \prime } } \\ & { = \phantom { \iota } ( 1 + \tau J H _ { m , z } ) \circ \Big ( 1 + \tau J \displaystyle \sum _ { i = 1 } ^ { m - 1 } H _ { i , z } + O ( \tau ^ { 2 } ) \Big ) } \\ & { = \phantom { \iota } 1 + \tau J \displaystyle \sum _ { i = 1 } ^ { m } H _ { i , z } + O ( \tau ^ { 2 } ) } \\ & { = \phantom { \iota } 1 + \tau J H _ { z } + O ( \tau ^ { 2 } ) . } \end{array}
$$

The symplecticity of $g _ { H } ^ { \tau }$ follows from the fact that symplectic maps on $\mathbf { R } ^ { 2 n }$ form a group under composition.

Similarly,

$$
g _ { H } ^ { \tau } = E _ { 1 } ^ { \tau } \circ E _ { 2 } ^ { \tau } \circ \cdot \cdot \cdot \circ E _ { m - 1 } ^ { \tau } \circ E _ { m } ^ { \tau }
$$

is symplectic and of order 1.

More discussion on how to construct separable schemes with high order is provided in Chapter 8.

Example 4.8. The Hamiltonian [FW98,FQ91]

$$
H _ { k } ( p , q ) = \sum _ { i = 0 } ^ { k - 1 } \cos { \left( p \cos { \frac { 2 \pi \mathrm { i } } { k } } + q \sin { \frac { 2 \pi \mathrm { i } } { k } } \right) }
$$

with $k$ -fold rotational symmetry in a phase plane[2,4] are not separable in the conventional sense if $k \neq 1 , 2 , 4$ . Otherwise they are symplectically separable, since every term $\cos \left( p \cos { \frac { 2 \pi { \mathrm { i } } } { k } } + q \sin { \frac { 2 \pi { \mathrm { i } } } { k } } \right)$ is nilpotent of degree 2 according to Theorem 4.3. For example, for $k = 3$ ,

$$
\begin{array} { r c l } { { H _ { 3 } ( p , q ) ~ = ~ \cos p + \cos \left( p \cos { \frac { 2 \pi } { 3 } } + q \sin { \frac { 2 \pi } { 3 } } \right) + \cos \left( p \cos { \frac { 4 \pi } { 3 } } + q \sin { \frac { 4 \pi } { 3 } } \right) } } \\ { { } } & { { } } \\ { { { } } } & { { = ~ \cos p + \cos \left( { \frac { 1 } { 2 } } p - { \frac { \sqrt { 3 } } { 2 } } q \right) + \cos \left( - { \frac { 1 } { 2 } } p - { \frac { \sqrt { 3 } } { 2 } } q \right) , } } \end{array}
$$

and the explicit symplectic schemes of order 1 are

$$
\begin{array} { r l r } {  { q ^ { 1 } \ = \ q - \frac { 1 } { 2 } \tau \sin ( \frac { 1 } { 2 } p + \frac { \sqrt { 3 } } { 2 } q ) , } } \\ & { } & \\ { p ^ { 1 } \ = \ p + \frac { \sqrt { 3 } } { 2 } \tau \sin ( \frac { 1 } { 2 } p + \frac { \sqrt { 3 } } { 2 } q ) , } \\ & { } & \\ { q ^ { 2 } \ = \ q ^ { 1 } - \frac { 1 } { 2 } \tau \sin ( \frac { 1 } { 2 } p ^ { 1 } - \frac { \sqrt { 3 } } { 2 } q ^ { 1 } ) , } \\ & { } & \\ { \hat { p } \ = \ p ^ { 1 } - \frac { \sqrt { 3 } } { 2 } \tau \sin ( \frac { 1 } { 2 } p - \frac { \sqrt { 3 } } { 2 } q ) , } \\ & { } & \\ { \hat { q } \ = \ q ^ { 2 } - \tau \sin \hat { p } . } \end{array}
$$

Using the composition theory discussed in Chapter 8 , we can construct an explicit symplectic scheme with higher order accuracy.

# 4.4.3 Separability of All Polynomials in $\mathbf { R } ^ { 2 n }$

Theorem 4.9. [FW98] Every monomial $x ^ { n - k } y ^ { k }$ of degree $n$ in 2 variables $x$ and $y$ , $n \leq 2$ , $0 \leq k \leq n$ can be expanded as a linear combination of $n + 1$ terms:

$$
\{ ( x + y ) ^ { n } , ( x + 2 y ) ^ { n } , \cdot \cdot \cdot , ( x + 2 ^ { n - 1 } y ) ^ { n } , x ^ { n } , y ^ { n } \} .
$$

Proof. Using binomial expansion,

$$
( x + y ) ^ { n } = x ^ { n } + \mathbf { C } _ { n } ^ { 1 } x ^ { n - 1 } y ^ { 1 } + \mathbf { C } _ { n } ^ { 2 } x ^ { n - 2 } y ^ { 2 } + \cdot \cdot \cdot + \mathbf { C } _ { n } ^ { n - 2 } x ^ { 2 } y ^ { n - 2 } + \mathbf { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } + y ^ { n } y ^ { 1 } .
$$

Define

$$
{ \begin{array} { r c l } { P _ { 1 } ( x , y ) : } & { = } & { ( x + y ) ^ { n } - x ^ { n } - y ^ { n } } \\ & & { = } & { \mathbf { C } _ { n } ^ { 1 } x ^ { n - 1 } y ^ { 1 } + \mathbf { C } _ { n } ^ { 2 } x ^ { n - 2 } y ^ { 2 } + \cdot \cdot \cdot + \mathbf { C } _ { n } ^ { 2 } x ^ { 2 } y ^ { n - 2 } + \mathbf { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } , } \end{array} }
$$

which is separable, and the right side consists of mixed terms; $P _ { 1 }$ is a linear combination of 3 terms $( x + y ) ^ { n } , x ^ { n }$ , and $y ^ { n }$ .

$$
\begin{array} { r l } & { \mathfrak { p } _ { 1 } ( x , 2 y ) = 2 \mathrm { C } _ { n } ^ { 1 } x ^ { n - 1 } y ^ { 1 } + 2 ^ { 2 } \mathrm { C } _ { n } ^ { 2 } x ^ { n - 2 } y ^ { 2 } + \cdot \cdot \cdot + 2 ^ { n - 2 } \mathrm { C } _ { n } ^ { 2 } x ^ { 2 } y ^ { n - 2 } + 2 ^ { n - 1 } \mathrm { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } , } \\ & { P _ { 1 } ( x , 1 y ) = 2 \mathrm { C } _ { n } ^ { 1 } x ^ { n - 1 } y ^ { 1 } + 2 \mathrm { C } _ { n } ^ { 2 } x ^ { n - 2 } y ^ { 2 } + \cdot \cdot \cdot + 2 \mathrm { C } _ { n } ^ { 2 } x ^ { 2 } y ^ { n - 2 } + 2 \mathrm { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } . } \end{array}
$$

Define

$$
\begin{array} { r c l } { { P _ { 2 } ( x , y ) : ~ = ~ P _ { 1 } ( x , 2 y ) - 2 P _ { 1 } ( x , y ) } } \\ { { } } & { { ~ = ~ ( 2 ^ { 2 } - 2 ) \mathrm { C } _ { n } ^ { 2 } x ^ { n - 2 } y ^ { 2 } + \cdot \cdot \cdot + ( 2 ^ { n - 2 } - 2 ) \mathrm { C } _ { n } ^ { 2 } x ^ { 2 } y ^ { n - 2 } } } \\ { { } } & { { } } & { { ~ + ( 2 ^ { n - 1 } - 2 ) \mathrm { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } , } } \end{array}
$$

which is separable in 4 terms $( x + y ) ^ { n } , ( x + 2 y ) ^ { n } , x ^ { n }$ , and $y ^ { n }$ .

$$
\begin{array} { r l } & { P _ { 3 } ( x , y ) = P _ { 2 } ( x , 2 y ) - 2 ^ { 2 } P _ { 2 } ( x , y ) } \\ & { \qquad = ( 2 ^ { 3 } - 2 ^ { 2 } ) ( 2 ^ { 3 } - 2 ) \mathrm { C } _ { n } ^ { 3 } x ^ { n - 3 } y ^ { 3 } + \cdots + ( 2 ^ { n - 2 } - 2 ^ { 2 } ) ( 2 ^ { n - 2 } - 2 ) \mathrm { C } _ { n } ^ { 2 } x ^ { 2 } y ^ { n - 1 } } \\ & { \qquad + ( 2 ^ { n - 1 } - 2 ^ { 2 } ) ( 2 ^ { n - 1 } - 2 ) \mathrm { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } , } \end{array}
$$

which is separable in 5 terms $( x + y ) ^ { n } , ( x + 2 y ) ^ { n } , ( x + 2 ^ { 2 } y ) ^ { n } , x ^ { n }$ , and $y ^ { n }$ . Define:

$$
\begin{array} { r c l } { { P _ { n - 2 } ( x , y ) : ~ = ~ P _ { n - 3 } ( x , 2 y ) - 2 ^ { n - 3 } P _ { n - 3 } ( x , y ) } } \\ { { } } & { { } } \\ { { } } & { { = ~ ( 2 ^ { n - 2 } - 2 ^ { n - 3 } ) \cdot \cdot \cdot ( 2 ^ { n - 2 } - 2 ) \mathrm { C } _ { n } ^ { 2 } x ^ { 2 } y ^ { n - 2 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { + ( 2 ^ { n - 1 } - 2 ^ { n - 3 } ) \cdot \cdot \cdot ( 2 ^ { n - 1 } - 2 ) \mathrm { C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } , } } \end{array}
$$

which is separable in $n$ terms $( x + y ) ^ { n } , ( x + 2 y ) ^ { n } , \cdot \cdot \cdot , ( x + 2 ^ { n - 3 } y ) ^ { n } ,$ $x ^ { n }$ , and $y ^ { n }$ Finally, we get:

$$
\begin{array} { r c l } { { P _ { n - 1 } ( x , y ) } } & { { = } } & { { P _ { n - 2 } ( x , 2 y ) - 2 ^ { n - 2 } P _ { n - 2 } ( x , y ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { ( 2 ^ { n - 1 } - 2 ^ { n - 2 } ) ( 2 ^ { n - 1 } - 2 ^ { n - 3 } ) \cdot \cdot \cdot ( 2 ^ { n - 1 } - 2 ) { \bf C } _ { n } ^ { 1 } x ^ { 1 } y ^ { n - 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \gamma _ { n - 1 } x ^ { 1 } y ^ { n - 1 } , \quad \gamma _ { n - 1 } \neq 0 . } } \end{array}
$$

The separable $n + 1$ terms are $( x + y ) ^ { n } , ( x + 2 y ) ^ { n } , \cdot \cdot \cdot$ , $( x + 2 ^ { n - 2 } y ) ^ { n }$ , $x ^ { n }$ , and $y ^ { n }$ . Hence, the mixed term $x y ^ { n - 1 }$ is separable into $n + 1$ terms. Then, from the separability of $P _ { n - 2 } ( x , y )$ and $x y ^ { n - 1 }$ , we know that $x ^ { 2 } y ^ { n - 2 }$ is separable into $n + 1$ terms. Similarly, $x ^ { 3 } y ^ { n - 3 } , x ^ { 4 } y ^ { n - 4 } , \cdot \cdot \cdot , x ^ { n - 2 } y ^ { 2 }$ , and $x ^ { n - 1 } y$ is separable into $n + 1$ terms. $\blacktriangle$

Remark 4.10. We can also work with the following formulae:

$$
\begin{array} { c } { { \frac 1 2 ( x + y ) ^ { 2 m + 1 } + \frac 1 2 ( x - y ) - x ^ { 2 m + 1 } } } \\ { { = \textstyle ( 2 _ { m + 1 } x ^ { 2 m - 1 } y ^ { 2 } + \textstyle ( \Sigma _ { 2 m + 1 } ^ { 4 } x ^ { 2 m - 3 } y ^ { 4 } + \cdots + \textstyle ( \Sigma _ { 2 m + 1 } ^ { 2 m } x y ^ { 2 m } , } } \\ { { \frac 1 2 ( x + y ) ^ { 2 m + 1 } - \frac 1 2 ( x - y ) ^ { 2 m + 1 } - y ^ { 2 m + 1 } } } \\ { { = \textstyle \mathrm { C _ { 2 m + 1 } ^ { 2 } } x ^ { 2 m } y + \textstyle \mathrm { C _ { 2 m + 1 } ^ { 2 } } x ^ { 2 m - 2 } y ^ { 3 } + \cdots + \textstyle \mathrm { C _ { 2 m + 1 } ^ { 2 m - 1 } } x ^ { 2 } y ^ { 2 m - 1 } , } } \\ { { \frac 1 2 ( x + y ) ^ { 2 m } + \frac 1 2 ( x - y ) ^ { 2 m } - x ^ { 2 m } - y ^ { 2 m } } } \\ { { = \textstyle \mathrm { C _ { 2 m } ^ { 2 } } x ^ { 2 m - 2 } y ^ { 2 } + \textstyle \mathrm { C _ { 2 m } ^ { 4 } } x ^ { 2 m - 4 } y ^ { 4 } + \cdots + \textstyle \mathrm { C _ { 2 m } ^ { 2 } } x ^ { 2 } y ^ { 2 m - 2 } , } } \\ { { \frac 1 2 ( x + y ) ^ { 2 m } - \frac 1 2 ( x - y ) ^ { 2 m } } } \\ { { = \textstyle \mathrm { C _ { 2 m } ^ { 2 } } x ^ { 2 m - 1 } y + \textstyle \mathrm { C _ { 2 m } ^ { 2 } } x ^ { 2 m - 3 } y ^ { 3 } + \cdots + \textstyle \mathrm { C _ { 2 m } ^ { 2 m - 1 } } x y ^ { 2 m - 1 } , } } \\ { { = \textstyle \mathrm { C _ { 2 m } ^ { 2 } } x ^ { 2 m - 1 } y + \textstyle \mathrm { C _ { 2 m } ^ { 2 } } x ^ { 2 m - 3 } y ^ { 3 } + \cdots + \textstyle \mathrm { C _ { 2 m } ^ { 2 m - 1 } } x y ^ { 2 m - 1 } , } } \end{array}
$$

by means of elimination to get more economic expansions, e.g.,

$$
x y = { \frac { 1 } { 2 } } ( x + y ) ^ { 2 } - { \frac { 1 } { 2 } } x ^ { 2 } - { \frac { 1 } { 2 } } y ^ { 2 } = { \frac { 1 } { 4 } } ( x + y ) ^ { 2 } - { \frac { 1 } { 4 } } ( x - y ) ^ { 2 } .
$$

Theorem 4.11. Every polynomial $P ( x , y )$ of degree n in variables $p$ and $q$ can be expanded as $n + 1$ terms $P _ { 1 } ( x , y ) , P _ { 2 } ( x , y ) , \cdot \cdot \cdot , P _ { n - 1 } ( x , y ) , P _ { n } ( x ) , P _ { n + 1 } ( y )$ , where each $P _ { i } ( u )$ is a polynomial of degree $n$ in one variable or more. Generally, every polynomial $P ( p , q )$ can be expanded as

$$
P ( p , q ) = \sum _ { i = 1 } ^ { m } P _ { i } ( a _ { i } p + b _ { i } q ) , \quad m \leq n + 1 ,
$$

where $P _ { i } ( u )$ are polynomials of degree n in one variable.

Theorem 4.12. Every monomial in $2 n$ variables is of the form

$$
f ( p , q ) = ( p _ { 1 } ^ { m _ { 1 } - k _ { 1 } } q _ { 1 } ^ { k _ { 1 } } ) ( p _ { 2 } ^ { m _ { 2 } - k _ { 2 } } q _ { 2 } ^ { k _ { 2 } } ) \cdot \cdot \cdot ( p _ { n } ^ { m _ { n } - k _ { n } } q _ { n } ^ { k _ { n } } )
$$

and can be expanded as a linear combination of the terms in the form:

$\phi ( A p + B q ) = ( a _ { 1 } p _ { 1 } + b _ { 1 } q _ { 1 } ) ^ { m _ { 1 } } ( a _ { 2 } p _ { 2 } + b _ { 2 } q _ { 2 } ) ^ { m _ { 2 } } \cdot \cdot \cdot ( a _ { n } p _ { n } + b _ { n } q _ { n } ) ^ { m _ { n } } ,$ where $\phi ( u ) \subsetneq \phi ( u _ { 1 } , \cdot \cdot \cdot , u _ { n } ) = u _ { 1 } ^ { m _ { 1 } } u _ { 2 } ^ { m _ { 2 } } \cdot \cdot \cdot u _ { n } ^ { m _ { n } }$ is the monomial in n with total degree $m = \sum _ { i = 1 } ^ { \cdot } m _ { i }$ and with degree $m _ { i }$ in variable $u _ { i }$ . $A$ and $B$ are diagonal matrices of order $n$ :

$$
A = \left( \begin{array} { l l l l } { a _ { 1 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { a _ { 2 } } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { a _ { n } } \end{array} \right) , \quad B = \left( \begin{array} { l l l l } { b _ { 1 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { b _ { 2 } } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { b _ { n } } \end{array} \right) ,
$$

which automatically satisfies $A B ^ { \mathrm { T } } = B A ^ { \mathrm { T } }$ . The elements $a _ { i } , b _ { i }$ can be chosen as integers.

Theorem 4.13. Every polynomial $P ( p _ { 1 } , q _ { 1 } , \cdots , p _ { n } , q _ { n } )$ of degree $m$ in $2 n$ variables can be expanded as [FW98]

$$
P ( \boldsymbol { p } , \boldsymbol { q } ) = \sum _ { i = 1 } ^ { m } P _ { i } ( \boldsymbol { A } _ { i } \boldsymbol { p } + \boldsymbol { B } _ { i } \boldsymbol { q } ) ,
$$

where each $P _ { i }$ is a polynomial of degree m in $n$ variables, and $A _ { i }$ , $B _ { i }$ are diagonal matrices (satisfying $A _ { i } B _ { i } ^ { \mathrm { T } } = B _ { i } A _ { i } ^ { \mathrm { T } }$ ). Thus, for polynomial Hamiltonian, the symplectic explicit Euler composite schemes of order $1 , 2$ , or and 4 can be easily constructed.

# 4.5 Energy-conservative Schemes by Hamiltonian Difference

Now, we consider energy-conservative schemes by Hamiltonian differencing, which was first proposed by A.J. Chorin[CHMM78] , and later considered by K. Feng[Fen85] .

However, these schemes are not symplectic. For simplicity, we illustrate the cases only when $n = 2$ . Let $z = z ^ { m } , \bar { z } = z ^ { m + 1 }$ .

$$
\begin{array} { l c l } { { \displaystyle \frac { 1 } { \tau } ( \bar { p } _ { 1 } - p _ { 1 } ) ~ = ~ - \frac { 1 } { \bar { q } _ { 1 } - q _ { 1 } } \{ H ( p _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) \} , } }  \\ { { \displaystyle \frac { 1 } { \tau } ( \bar { p } _ { 2 } - p _ { 2 } ) ~ = ~ - \frac { 1 } { \bar { q } _ { 2 } - q _ { 2 } } \{ H ( \bar { p } _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , \bar { q } _ { 2 } ) - H ( \bar { p } _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , q _ { 2 } ) \} , } } \\ { { \displaystyle \frac { 1 } { \tau } ( \bar { q } _ { 1 } - q _ { 1 } ) ~ = ~ \frac { 1 } { \bar { p } _ { 1 } - p _ { 1 } } \{ H ( \bar { p } _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , q _ { 2 } ) \} , } } \\ { { \displaystyle \frac { 1 } { \tau } ( \bar { q } _ { 2 } - q _ { 2 } ) ~ = ~ \frac { 1 } { \bar { p } _ { 2 } - p _ { 2 } } \{ H ( \bar { p } _ { 1 } , \bar { p } _ { 2 } , \bar { q } _ { 1 } , \bar { q } _ { 2 } ) - H ( \bar { p } _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , \bar { q } _ { 2 } ) \} . } } \end{array}
$$

By addition and cancellation, we have energy conservation for the arbitrary Hamiltonian $H ( \bar { p } _ { 1 } , \bar { p } _ { 2 } , \bar { q } _ { 1 } , \bar { q } _ { 2 } ) = H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } )$ .

Since the proposed energy conservative schemes based on Hamiltonian differencing only have the first order accuracy, $\mathrm { Q i n } ^ { \mathrm { [ Q i n 8 7 ] } }$ first proposed another more symmetric form in 1987, which possesses the second order accuracy. Independently, Itoh and Abe[IA88] also proposed the same schemes in 1988.

For simplicity, we consider only the case $n = 2$ , and the following difference schemes are given:

$$
\begin{array} { r l } { \frac { p _ { 1 1 } } { 1 6 } = - \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , p _ { 2 } , q _ { 3 } , q _ { 2 } ) } { \Delta q } - \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , \bar { p } , \bar { q } , \bar { q } , \bar { q } ) } { 1 6 } - \frac { H ( p _ { 1 } , \bar { p } , \bar { q } , \bar { q } , \bar { q } ) } { \Delta q } - \frac { H ( p _ { 1 } , \bar { p } , \bar { q } , \bar { q } , \bar { q } ) } { \Delta q } } & { } \\ { - \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , p _ { 3 } , q _ { 3 } , q _ { 3 } ) } { \Delta q } - \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H ( p _ { 2 } , \bar { q } , \bar { q } , \bar { q } , \bar { q } ) } { 1 6 } - \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 3 } ) } { \Delta p } , } & { } \\ { - \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , p _ { 3 } , q _ { 1 } , q _ { 2 } ) } { \Delta p } + \frac { H ( p _ { 1 } , p _ { 2 } , \bar { q } , \bar { q } , \bar { q } , \bar { q } ) } { 1 6 } + \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , \bar { p } , \bar { q } , \bar { q } , \bar { q } ) } { \Delta p } } & { } \\  \frac { q _ { 1 } } { 1 6 } = \frac { 1 } { 4 } \frac { H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H ( p _ { 1 } , p _ { 2 } , q _ { 3 } , q _ { 2 } ) } { \Delta p } + \frac { 1 } { 4 } \frac  H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) - H  \end{array}
$$

From the above first two equations, we have:

$$
\frac { 1 } { 2 } ( H ( \bar { p } _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , q _ { 2 } ) + H ( \bar { p } _ { 1 } , \bar { p } _ { 2 } , \bar { q } _ { 1 } , \bar { q } _ { 2 } ) ) = \frac { 1 } { 2 } ( H ( p _ { 1 } , \bar { p } _ { 2 } , q _ { 1 } , \bar { q } _ { 2 } ) + H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) ) .
$$

From the last two equations, we have:

$$
\frac { 1 } { 2 } ( H ( \bar { p } _ { 1 } , \bar { p } _ { 2 } , \bar { q } _ { 1 } , \bar { q } _ { 2 } ) + H ( p _ { 1 } , \bar { p } _ { 2 } , q _ { 1 } , \bar { q } _ { 2 } ) = \frac { 1 } { 2 } ( H ( \bar { p } _ { 1 } , p _ { 2 } , \bar { q } _ { 1 } , q _ { 2 } ) + H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) ) .
$$

Combining these equations, we observe that these schemes have exact conservation of the Hamiltonian $H$ . Further research about conservative energy scheme can be referred in recent studies[WWM08] .

# Bibliography

[Car65] C. Carathe’odory: Calculus of Variation and Partial Differential Equations of First Order, Vol.1. Holden-Day, San Franscisco, (1965).   
[CHMM78] A. Chorin, T. J. R. Huges, J. E. Marsden, and M. McCracken: Product formulas and numerical algorithms. Comm. Pure and Appl. Math., 31:205–256, (1978).   
[Dah59] G. Dahlquist: Stability and error bounds in the numerical integration of ordinary differential equations. Trans. of the Royal Inst. of Techn., Stockholm, Sweden, 130:87, (1959).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FQ91] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FW98] K. Feng and D.L. Wang: On variation of schemes by Euler. J. Comput. Math., 16:97– 106, (1998).   
[FWQ90] K. Feng, H.M. Wu, and M.Z. Qin: Symplectic Difference Schemes for Linear Hamiltonian Canonical Systems. J. Comput. Math., 8(4):371–380, (1990).   
[IA88] T. Itoh and K. Abe: Hamiltonian-conserving discrete canonical equations based on variational difference quotients. J. Comp. Phys., 76:85–102, (1988).   
[Men84] C.R. Menyuk: Some properties of the discrete Hamiltonian method. Physica $D$ , 11:109–129, (1984).   
[Qin87] M. Z. Qin: A symplectic scheme for the Hamiltonian equations. J. Comput. Math., 5:203–209, (1987).   
[Qin89] M. Z. Qin: Cononical difference scheme for the Hamiltonian equation. Mathematical Methods and in the Applied Sciences, 11:543–557, (1989).   
[QZZ95] M. Z. Qin, W. J. Zhu, and M. Q. Zhang: Construction of symplectic of a three stage difference scheme for ODEs. J. Comput. Math., 13:206–210, (1995).   
[Wey39] H. Weyl: The Classical Groups. Princeton Univ. Press, Princeton, Second edition, (1939).   
[WT03] D. L. Wang and H. W. Tam: A symplectic structure preserved by the trapezoidal rule. J. of Phys. Soc. of Japan, 72(9):2193–2197, (2003).   
[WWM08] Y. S. Wang, B. Wang, and M. Z.Qin: Local structure-preserving algorithms for partial differential equations. Science in China (Series A), 51(11):2115–2136, (2008).
