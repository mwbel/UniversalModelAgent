# Chapter 15. Structure Preserving Schemes for Birkhoff Systems

A universal symplectic structure for a Newtonian system including nonconservative cases can be constructed in the framework of Birkhoffian generalization of Hamiltonian mechanics. In this chapter, the symplectic geometry structure of Birkhoffian system is discussed, and the symplecticity of Birkhoffian phase flow is presented. Based on these properties, a way to construct symplectic schemes for Birkhoffian systems by the generating function method is explained[SSQS07],[SQ03] .

# 15.1 Introduction

Birkhoffian representation is a generalization of Hamiltonian representation, which can be applied to hadron physics, statistical mechanics, space mechanics, engineering, biophysics, etc. Santilli[San83a,San83b] . All conservative or nonconservative, self-adjoint or non self-adjoint, unconstrained or nonholonomic constrained systems always admit a Birkhoffian representation (Guo[GLSM01] and Santilli[San83b] ). In last 20 years, many researchers have studied Birkhoffian mechanics and obtained a series of results in integral theory, stability of motion, inverse problem, and algebraic and geometric description, etc.

Birkhoff’s equations are more complex than Hamilton’s equations, and the study of the computational methods of the former is also more complicated. There are no result on computational methods for Birkhoffian system before. In general, the known difference methods are not generally applicable to Birkhoffian system. A difference scheme used to solve Hamiltonian system should be Hamiltonian scheme (Hairer, Lubich and Wanner[HLW02] and Sanz-Serna and Calvo[SSC94] ), so a difference scheme to simulate Birkhoffian system should be a Birkhoffian scheme. However, the conventional difference schemes such as Euler center scheme, leap-frog scheme, etc., are not Birkhoffian schemes. So, a way to systematically construct a Birkhoffian scheme is necessary, and this is the main context in this chapter.

Both the Birkhoffian and Hamiltonian systems are usually of finite dimensional (Arnold[Arn89] and Marsden and Ratiu[MR99] ), infinite dimension system has not been proposed before. The algebraic and geometric profiles of finite dimensional Birkhoffian systems are described in local coordinates, and general nonautonomous Hamiltonian systems are considered as autonomous Birkhoffian systems (Santilli[San83b] ). Symplectic schemes are systematically developed for standard Hamiltonian systems and for general Hamiltonian systems on the Poisson manifold, which belong to autonomous and semi-autonomous Birkhoffian systems (Feng and Wang[FW91bandFW91a] and Feng and $\mathrm { Q i n } ^ { \left[ \mathrm { F Q 8 7 } \right] } ;$ . So, in this chapter, we just discuss the nonautonomous Birkhoffian system in detail. Thereby, Einstein’s summation convention is used.

In Section 15.2, Birkhoffian systems are sketched out via variational self-adjointness, with which we shows the relationship between Birkhoffian and Hamiltonian systems more essentially and directly. Then the basic geometrical properties of Birkhoffian systems are presented. In Section 15.3, the definitions of $\widetilde K ( z )$ -Lagrangian submanifolds is extended to $\widetilde K ( z , t )$ -Lagrangian submanifolds with parameter $t$ . Then the relationship between symplectic mappings and gradient mappings are discussed. In Section 15.4, the generating functions for the phase flow of the Birkhoffian systems are constructed and the method to simulate Birkhoffian systems by symplectic schemes of any order is given. Section 15.5 contains an illustrating example. Schemes of order one, two, and four are derived for the linear damped oscillator. In the last Section 15.6, numerical experiments are given.

# 15.2 Birkhoffian Systems

The generalization of Hamilton’s equation is given by

$$
\left( \frac { \partial F _ { j } } { \partial z _ { i } } - \frac { \partial F _ { i } } { \partial z _ { j } } \right) \frac { \mathrm { d } z _ { i } } { \mathrm { d } t } - \left( \frac { \partial B ( z , t ) } { \partial z _ { i } } + \frac { \partial F ( z , t ) } { \partial t } \right) = 0 , \quad i , j = 1 , 2 , \cdots , 2 n ,
$$

where the following abbreviations

$$
K _ { i j } = \frac { \partial F _ { j } } { \partial z _ { i } } - \frac { \partial F _ { i } } { \partial z _ { j } } , \quad K = ( K _ { i j } ) _ { i , j = 1 , \cdots , 2 n }
$$

are further used. Following the terminology suggested by Santilli $\left[ \mathsf { S a n 8 3 b } \right]$ , this is called Birkhoff’s equation or Birkhoffian system under some additional assumptions. The function $B ( z , t )$ is called the Birkhoffian function because of certain physical difference with Hamiltonian. Also, the $F _ { i }$ $( i = 1 , 2 , \cdots , 2 n )$ are Birkhoffian functions. A representation of Newton’s equations via Birkhoff’s equation is called a Birkhoffian representation.

Definition 2.1. Birkhoff’s equations (2.1) are called autonomous when the functions $F _ { i }$ and $B$ are independent of the time variable. In this case, the equations are of the simple form

$$
K _ { i j } ( z ) \frac { \mathrm { d } z _ { j } } { \mathrm { d } t } - \frac { \partial B ( z ) } { \partial z _ { i } } = 0 .
$$

They are called semi-autonomous when the functions $F _ { i }$ do not depend explicitly on time. In this case, the equations have the more general form

$$
K _ { i j } ( z ) \frac { \mathrm { d } z _ { j } } { \mathrm { d } t } - \frac { \partial B ( z , t ) } { \partial z _ { i } } = 0 .
$$

They are called nonautonomous when both the functions $F _ { i }$ and $B$ explicitly dependent on time. Then, the equations read as follow:

$$
K _ { i j } ( z , t ) \frac { \textrm { d } z _ { j } } { \textrm { d } t } - \frac { \partial B ( z , t ) } { \partial z _ { i } } - \frac { \partial F _ { i } ( z , t ) } { \partial t } = 0 .
$$

They are called regular when the functional determinant is unequal to zero in the region considered, i.e.,

$$
\begin{array} { r } { \operatorname* { d e t } { ( K _ { i j } ) ( \widetilde { \bf R e } ) } \neq 0 , } \end{array}
$$

otherwise, degenerate.

Given an arbitrary analytic and regular first-order system

$$
K _ { i j } ( z , t ) \frac { \mathrm { d } z _ { i } } { \mathrm { d } t } + \mathcal { D } _ { i } ( z , t ) = 0 , \quad i = 1 , 2 , \cdot \cdot \cdot , 2 n ,
$$

which is self-adjoint if and only if it satisfies the following conditions in $\widetilde { \mathrm { R e } } ^ { * }$ for i, j = 1, 2,  , 2n[AH75] :

$$
\begin{array} { r l } & { K _ { i j } + K _ { j i } = 0 , } \\ & { \frac { \partial K _ { i j } } { \partial z _ { k } } + \frac { \partial K _ { j k } } { \partial z _ { i } } + \frac { \partial K _ { k i } } { \partial z _ { j } } = 0 , } \\ & { \frac { \partial K _ { i j } } { \partial t } = \frac { \partial D _ { i } } { \partial z _ { j } } - \frac { \partial D _ { j } } { \partial z _ { i } } . } \end{array}
$$

We now simply introduce the geometric significance of the condition of variational self-adjointness [MP91,SVC95] . Here the region considered is a star-shaped region $\widetilde { \mathrm { R e } } ^ { * }$ of points of $R \times T ^ { * } M , T ^ { * } M$ the cotangent space of the $M$ , $M$ a $2 n$ -dimensional manifold. The geometric significance of self-adjointness condition (2.5) is the integrability condition for a 2-form to be an exact symplectic form.

Consider first the case for which $K _ { i j } = K _ { i j } ( z )$ . Given a symplectic structure written as the 2-form in local coordinates

$$
\Omega = \sum _ { i , j = 1 } ^ { 2 n } K _ { i j } ( z , t ) \operatorname { d } z _ { i } \wedge \operatorname { d } z _ { j } .
$$

One of the fundamental properties of symplectic form is that $\mathrm { d } \Omega = 0$ . Because the exact character of 2-form implies that

$$
\Omega = \mathrm { d } ( F _ { i } \mathrm { d } z _ { i } ) ,
$$

this geometric property is fully characterized by the first two equations of the condition (2.5); i.e., the 2-form (2.6) describes the geometrical structure of the autonomous case (2.2) of the Birkhoff’s equations, it even sketches out the geometric structure of the semi-autonomous case.

For the case $K _ { i j } ~ = ~ K _ { i j } ( z , t )$ , the full set of condition (2.5) must be considered. The corresponding geometric structure can be better expressed by transition of the symplectic geometry on the cotangent bundle $T ^ { * } M$ with local coordinates $z _ { i }$ to the contact geometry on the manifold $R \times T ^ { * } M$ with local coordinates $\widetilde { z } _ { i }$ $( i = 0 , 1 , 2 , \cdots , 2 n )$ , $\widetilde { z } _ { 0 } \doteq t ^ { [ \mathrm { S a n } 8 3 \mathrm { b } ] }$ ". More general formulations of an exact contact "2-form exist, although it is now referred to as a $( 2 n { + } 1 )$ -dimensional space,

$$
\widehat { \Omega } = \sum _ { i , j = 0 } ^ { 2 n } \widehat { K } _ { i j } \mathrm { d } \widetilde { z } _ { i } \wedge \mathrm { d } \widetilde { z } _ { j } = \Omega + 2 \mathcal { D } _ { i } \mathrm { d } z _ { i } \wedge \mathrm { d } t ,
$$

where

$$
\begin{array} { r l } & { \widehat { K } = \left[ \begin{array} { l l } { 0 } & { - \mathcal { D } ^ { \mathrm { T } } } \\ { \mathcal { D } } & { K } \end{array} \right] , \quad \mathcal { D } = ( \mathcal { D } _ { 1 } , \cdot \cdot \cdot , \mathcal { D } _ { 2 n } ) ^ { \mathrm { T } } . } \end{array}
$$

If the contact form is also of the exact type,

$$
\begin{array} { r } { \widehat { \Omega } = \mathbf { d } \big ( \widetilde { F } _ { i } \mathbf { d } \widetilde { z } _ { i } \big ) , \quad \widetilde { F } _ { i } = \left\{ \begin{array} { l l } { - B , } \\ { F _ { i } , } \end{array} \right. } \end{array}
$$

the geometric meaning of the condition of the self-adjointness is then the integrability condition for the exact contact structure (2.7). Here $B$ can be calculated from

$$
- \frac { \partial B } { \partial z _ { i } } = \mathcal { D } _ { i } + \frac { \partial F _ { i } } { \partial t }
$$

for

$$
\frac { \partial } { \partial z _ { j } } \bigg ( D _ { i } + \frac { \partial \ F _ { i } } { \partial t } \bigg ) = \frac { \partial } { \partial z _ { i } } \bigg ( D _ { j } + \frac { \partial F _ { j } } { \partial t } \bigg ) .
$$

All the above discussion can be expressed via the following property.

Theorem 2.2 (Self-Adjointness of Birkhoffian System). For a general nonautonomous first-order system (2.4), a necessary and sufficient condition for self-adjointness in $\widetilde { \mathrm { R e } } ^ { * }$ of points of ${ \bf R } \times T _ { * } { \bf R } ^ { 2 n }$ is that it is of the Birkhoffian type, i.e., the following representation holds for $i , j = 1 , 2 , \cdots , 2 n$ ,

$$
K _ { i j } ( z , t ) \frac { \mathrm { d } z _ { i } } { \mathrm { d } t } + \mathcal { D } _ { i } ( z , t ) = \bigg ( \frac { \partial F _ { j } } { \partial z _ { i } } - \frac { \partial F _ { i } } { \partial z _ { j } } \bigg ) \frac { \mathrm { d } z _ { i } } { \mathrm { d } t } - \bigg ( \nabla B ( z , t ) + \frac { \partial F ( z , t ) } { \partial t } \bigg ) .
$$

Remark 2.3. The functions $F _ { i }$ and $B$ can be calculated according to the rules [AH75]

$$
\begin{array} { l } { \displaystyle { F _ { i } = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } z _ { j } \cdot K _ { j i } ( \lambda z , t ) { \bf d } \lambda , } } \\ { \displaystyle { B = \int _ { 0 } ^ { 1 } z _ { i } \cdot \Big ( \mathscr { D } _ { i } + \frac { \partial { F _ { i } } } { \partial { t } } \Big ) ( \lambda z , t ) { \bf d } \lambda . } } \end{array}
$$

Due to the self-adjointness of Birkhoff’s equations, the phase flow of the system (2.8) conserves the symplecticity

$$
\frac { \mathrm { d } } { \mathrm { d } t } \Omega = \frac { \mathrm { d } } { \mathrm { d } t } ( K _ { i j } \mathrm { d } z _ { i } \wedge \mathrm { d } z _ { j } ) = 0 .
$$

So denoting the phase flow of the Equation (2.8) with $( \widehat { z } , \widehat { t } )$ yields

$$
K _ { i j } ( \widehat { z } , \widehat { t } ) { \bf d } \widehat { z } _ { i } \wedge { \bf d } \widehat { z } _ { j } = K _ { i j } ( z , t ) { \bf d } z _ { i } \wedge { \bf d } z _ { j } ,
$$

respectively the algebraic representation

$$
\frac { \partial \widehat { z } } { \partial z } ^ { \mathrm { T } } K ( \widehat { z } , \widehat { t } ) \frac { \partial \widehat { z } } { \partial z } = K ( z , t ) .
$$

In the latter, the algorithm preserving this geometric property of the phase flow in discrete space will be constructed.

# 15.3 Generating Functions for $K ( z , t )$ -Symplectic Mappings

In this section, general $K ( z , t )$ -symplectic mappings and their relationships with the gradient mappings and their generating functions are considered [FW91b,FW91a,FQ87] .

Definition 3.1. Let denote

$$
\begin{array} { r l } & { J _ { 2 n } = \left[ \begin{array} { c c } { O } & { I _ { n } } \\ { - I _ { n } } & { O } \end{array} \right] , \quad J _ { 4 n } = \left[ \begin{array} { c c } { O } & { I _ { 2 n } } \\ { - I _ { 2 n } } & { O } \end{array} \right] , \quad \widetilde { J } _ { 4 n } = \left[ \begin{array} { c c } { J _ { 2 n } } & { O } \\ { O } & { - J _ { 2 n } } \end{array} \right] , } \\ & { \widetilde { K } ( \widehat { z } , z , t , t _ { 0 } ) = \left[ \begin{array} { c c } { K ( \widehat { z } , t ) } & { O } \\ { O } & { - K ( z , t _ { 0 } ) } \end{array} \right] . } \end{array}
$$

Then a $2 n$ -dimensional submanifold $L \subset \mathbf { R } ^ { 4 n }$

$$
L = \left\{ \left[ \begin{array} { c } { { \widehat z } } \\ { { z } } \end{array} \right] \in R ^ { 4 n } \ | \ z = z ( x , t _ { 0 } ) , \ \widehat z = \widehat z ( x , t ) , \ x \in U \subset { \bf R } ^ { 2 n } , \ \mathrm { ~ o ~ r ~ } \ \xi = 2 \right\} .
$$

is called a $J _ { 4 n }$ - or $\widetilde { J } _ { 4 n }$ - or $\widetilde { K } ( \widehat { z } , z , t , t _ { 0 } )$ -Lagrangian submanifold if it holds

$$
( T _ { x } L ) ^ { \mathrm { T } } J _ { 4 n } ( T _ { x } L ) = 0 , \quad ( T _ { x } L ) ^ { \mathrm { T } } \widetilde { J } _ { 4 n } ( T _ { x } L ) = 0
$$

or

$$
( T _ { x } L ) ^ { \mathrm { T } } \widetilde { K } ( \widehat { z } , z , t , t _ { 0 } ) ( T _ { x } L ) = 0 ,
$$

where $T _ { x } L$ is the tangent space to $L$ at $x$ .

Definition 3.2. The mapping with parameters $t$ and $t _ { 0 }$ is $z \ \to \ { \widehat z } \ = \ g ( z , t , t _ { 0 } ) \ :$ $\mathbf { R } ^ { 2 n } \mathbf { \Lambda } \to \mathbf { \Lambda } \mathbf { R } ^ { 2 n }$ is called a canonical map or a gradient map or a $K ( z , t )$ -symplectic map if its graph

$$
\Gamma _ { g } = \left\{ { \left[ \begin{array} { l } { { \widehat { z } } } \\ { z } \end{array} \right] } \in \mathbf { R } ^ { 4 n } \mid { \widehat { z } } = g ( z , t , t _ { 0 } ) , z = z \in \mathbf { R } ^ { 2 n } \right\}
$$

is a ${ { J } _ { 4 n } } \mathrm { . }$ - or $\widetilde { J } _ { 4 n }$ - or $\widetilde { K } ( \widehat { z } , z , t , t _ { 0 } )$ -Lagrangian submanifold.

For differentiable mappings, there exists an equivalent definition for the $K$ - symplecticness, which is also useful for difference schemes.

Definition 3.3. A differentiable mapping $g : M \to M$ is $K ( z , t )$ -symplectic if

$$
\frac { \partial g } { \partial z } ^ { \mathrm { T } } K \bigl ( g ( z , t , t _ { 0 } ) , t \bigr ) \frac { \partial g } { \partial z } = K ( z , t _ { 0 } ) .
$$

A difference scheme approximating the Birkhoffian system (2.8) with step size $\tau$

$$
z ^ { k + 1 } = g ^ { k } ( z ^ { k } , t _ { k } + \tau , t _ { k } ) , \quad k \geqslant 0
$$

is called a $K$ -symplectic scheme, if $g ^ { k }$ is $K$ -symplectic for every $k$ , i.e.,

$$
\frac { \partial g ^ { k } } { \partial z ^ { k } } ^ { \mathrm { T } } K ( z ^ { k + 1 } , t ^ { k + 1 } ) \frac { \partial g ^ { k } } { \partial z ^ { k } } = K ( z ^ { k } , t ^ { k } ) .
$$

The graph of the phase flow of the Birkhoffian system (2.8) is $g ^ { t } ( z , t _ { 0 } ) ~ =$ $g ( z , t , t _ { 0 } )$ which is a $\widetilde { K } ( \widehat { z } , z , t , t _ { 0 } )$ -Lagrangian submanifold for

$$
g _ { z } ^ { t } ( z , t _ { 0 } ) ^ { \mathrm { T } } K \bigl ( g ^ { t } ( z , t _ { 0 } ) , t \bigr ) g _ { z } ^ { t } ( z , t _ { 0 } ) = K ( z , t _ { 0 } ) .
$$

Similarly, the graph of the phase flow of standard Hamiltonian system is a $\widetilde { J } _ { 4 n }$ - Lagrangian submanifold.

Consider the nonlinear transformation with two parameters $t$ and $t _ { 0 }$ from $\mathrm { R } ^ { 4 n }$ to itself,

$$
\begin{array} { r l r } & { } & { \boldsymbol { \alpha } ( t , t _ { 0 } ) : \left[ \begin{array} { c } { \widehat { z } } \\ { z } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { \widehat { w } } \\ { w } \end{array} \right] = \left[ \begin{array} { c } { \alpha _ { 1 } ( \widehat { z } , z , t , t _ { 0 } ) } \\ { \alpha _ { 2 } ( \widehat { z } , z , t , t _ { 0 } ) } \end{array} \right] , } \\ & { } & { \boldsymbol { \alpha } ^ { - 1 } ( t , t _ { 0 } ) : \left[ \begin{array} { c } { \widehat { w } } \\ { w } \end{array} \right] \longrightarrow \left[ \begin{array} { c } { \widehat { z } } \\ { z } \end{array} \right] = \left[ \begin{array} { c } { \alpha ^ { 1 } ( \widehat { w } , w , t , t _ { 0 } ) } \\ { \alpha ^ { 2 } ( \widehat { w } , w , t , t _ { 0 } ) } \end{array} \right] . } \end{array}
$$

Let denote the Jacobian of $\alpha$ and its inverse by

$$
\alpha _ { * } ( { \widehat { z } } , z , t , t _ { 0 } ) = { \left[ \begin{array} { l l } { A _ { \alpha } } & { B _ { \alpha } } \\ { C _ { \alpha } } & { D _ { \alpha } } \end{array} \right] } , \quad \alpha _ { * } ^ { - 1 } ( { \widehat { w } } , w , t , t _ { 0 } ) = { \left[ \begin{array} { l l } { A ^ { \alpha } } & { B ^ { \alpha } } \\ { C ^ { \alpha } } & { D ^ { \alpha } } \end{array} \right] } .
$$

Let $\alpha$ be a diffeomorphism from $\mathrm { R } ^ { 4 n }$ to itself, then it follows that $\alpha$ carries every $\widetilde { K }$ -Lagrangian submanifold into a $J _ { 4 n }$ -Lagrangian submanifold, if and only if $\alpha _ { * } ^ { \dot { \mathrm { T } } } J _ { 4 n } \alpha _ { * } = \tilde { K }$ , i.e.,

$$
\left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] ^ { \mathrm { T } } \left[ \begin{array} { c c } { { J _ { 2 n } } } & { { O } } \\ { { O } } & { { - J _ { 2 n } } } \end{array} \right] \left[ \begin{array} { c c } { { A _ { \alpha } } } & { { B _ { \alpha } } } \\ { { C _ { \alpha } } } & { { D _ { \alpha } } } \end{array} \right] = \left[ \begin{array} { c c } { { { \cal K } ( \widehat { z } , t ) } } & { { O } } \\ { { O } } & { { - { \cal K } ( z , t _ { 0 } ) } } \end{array} \right] .
$$

Conversely, $\alpha ^ { - 1 }$ carries every $J _ { 4 n }$ -Lagrangian submanifold into a $\widetilde { K }$ -Lagrangian submanifold.

Theorem 3.4. Let $M \in \mathbf { R } ^ { 2 n \times 2 n }$ , $\alpha$ given as in (3.1), and define a fractional transformation

$$
\sigma _ { \alpha } : { \mathcal { M } } \longrightarrow { \mathcal { M } } , \quad M \longrightarrow N = \sigma _ { \alpha } ( M ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 }
$$

under the transversality condition $| C _ { \alpha } M + D _ { \alpha } | \neq 0 .$ . Then the following four conditions are mutually equivalent:

$$
\begin{array} { l l } { { | C _ { \alpha } M + D _ { \alpha } | \neq 0 , } } & { { | M C ^ { \alpha } - A ^ { \alpha } | \neq 0 , } } \\ { { \ } } & { { \ } } \\ { { | C ^ { \alpha } N + D ^ { \alpha } | \neq 0 , } } & { { | N C _ { \alpha } - A _ { \alpha } | \neq 0 . } } \end{array}
$$

The proof is direct and simple, so it is omitted here.

Theorem 3.5. Let $\alpha$ be defined as in (3.1). Let $z  { \widehat { z } } = g ( z , t , t _ { 0 } )$ be a $K ( z , t )$ - symplectic mapping in some neighborhood $\widetilde { \mathcal { R } }$ of $\mathbf { R } ^ { 2 n }$ with Jacobian $g _ { z } ( z , t , t _ { 0 } ) =$ $M ( z , t , t _ { 0 } )$ . If $M$ satisfies the transversality condition in $\widetilde { \mathcal { R } }$

$$
\begin{array} { r } { \left| C _ { \alpha } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } ) M ( z , t , t _ { 0 } ) + D _ { \alpha } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } ) \right| \neq 0 , } \end{array}
$$

then there uniquely exists in $\widetilde { \mathcal { R } }$ a gradient mapping $w \to \widehat { w } = f ( w , t , t _ { 0 } )$ with Jacobian $f _ { w } ( w , t , t _ { 0 } ) = N ( w , t , t _ { 0 } )$ and a uniquely defined scalar generating function $\phi ( w , t , t _ { 0 } )$ , such that

$$
f ( w , t , t _ { 0 } ) = \phi _ { w } ( w , t , t _ { 0 } ) ,
$$

$$
\begin{array} { r c l } { { \alpha _ { 1 } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } ) } } & { { = } } & { { f \big ( \alpha _ { 2 } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } \big ) , t , t _ { 0 } \big ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \phi _ { w } \big ( \alpha _ { 2 } \big ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } \big ) , t , t _ { 0 } \big ) , } } \end{array}
$$

and

$$
\begin{array} { r } { N = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } , } \\ { M = ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } . } \end{array}
$$

Proof. Under the transformation $\alpha$ , the image of the graph $\boldsymbol { { \Gamma } } _ { g }$ is

$$
\boldsymbol \alpha ( { \Gamma } _ { g } ) = \left\{ \left[ \begin{array} { l } { \widehat w } \\ { w } \end{array} \right] \in { \mathbf { R } } ^ { 4 n } \mid \left[ \begin{array} { l } { \widehat w = \alpha _ { 1 } \big ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } \big ) } \\ { w = \alpha _ { 2 } \big ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } \big ) } \end{array} \right] \right\} .
$$

Inequality (3.2) implies

$$
\left| \frac { \partial w } { \partial z } \right| = \left| \frac { \partial \alpha _ { 2 } } { \partial \widehat { z } } \cdot \frac { \partial \widehat { z } } { \partial z } + \frac { \partial \alpha _ { 2 } } { \partial z } \right| = \left| C _ { \alpha } M + D _ { \alpha } \right| \neq 0 ,
$$

so $w = \alpha _ { 2 } \big ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } \big )$ is invertible, the inverse function is denoted by $z =$ $z ( w , t , t _ { 0 } )$ . Set

$$
\begin{array} { r } { \widehat { w } = f ( w , t , t _ { 0 } ) = \alpha _ { 1 } \big ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } \big ) | _ { z = z ( w , t , t _ { 0 } ) } , } \end{array}
$$

then

$$
N = \frac { \partial f } { \partial w } = \bigg ( \frac { \partial \alpha _ { 1 } } { \partial \hat { z } } \frac { \partial g } { \partial z } + \frac { \partial \alpha _ { 1 } } { \partial z } \bigg ) \bigg ( \frac { \partial z } { \partial w } \bigg ) = ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } .
$$

Notice that the tangent space to $\alpha ( T _ { g } )$ at $z$ is

$$
T _ { z } \big ( \boldsymbol { \alpha } ( \boldsymbol { r _ { g } } ) \big ) = \left[ \begin{array} { l } { \frac { \partial \widehat { w } } { \partial z } } \\ { \frac { \partial w } { \partial z } } \end{array} \right] = \left[ \begin{array} { l } { A _ { \boldsymbol { \alpha } } \boldsymbol { M } + B _ { \boldsymbol { \alpha } } } \\ { C _ { \boldsymbol { \alpha } } \boldsymbol { M } + D _ { \boldsymbol { \alpha } } } \end{array} \right] .
$$

It can be concluded that $\alpha \left( T _ { g } \right)$ is a $J _ { 4 n }$ -Lagrangian submanifold for

$$
\begin{array} { r l } & { T _ { z } \big ( \alpha ( T _ { g } ) \big ) ^ { \mathrm { T } } J _ { 4 n } T _ { z } \big ( \alpha ( T _ { g } ) \big ) } \\ & { \quad = \big ( ( A _ { \alpha } M + B _ { \alpha } ) ^ { \mathrm { T } } , ( C _ { \alpha } M + D _ { \alpha } ) ^ { \mathrm { T } } \big ) J _ { 4 n } \left[ \begin{array} { l } { A _ { \alpha } M + B _ { \alpha } } \\ { C _ { \alpha } M + D _ { \alpha } } \end{array} \right] } \\ & { \quad = ( M ^ { \mathrm { T } } , I ) \alpha _ { * } ^ { \mathrm { T } } J _ { 4 n } \alpha _ { * } \Big [ \begin{array} { l } { M } \\ { I } \end{array} \Big ] = ( M ^ { \mathrm { T } } , I ) \widetilde { K } \Big [ \begin{array} { l } { M } \\ { I } \end{array} \Big ] = 0 . } \end{array}
$$

$$
( A _ { \alpha } M + B _ { \alpha } ) ^ { \mathrm { T } } ( C _ { \alpha } M + D _ { \alpha } ) - ( C _ { \alpha } M + D _ { \alpha } ) ^ { \mathrm { T } } ( A _ { \alpha } M + B _ { \alpha } ) = 0 ,
$$

i.e., $N ~ = ~ ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 }$ is symmetric. This implies that $\widehat { w } =$ $f ( w , t , t _ { 0 } )$ is a gradient mapping. By the Poincare lemma, there is a scalar function ´ $\phi ( w , t , t _ { 0 } )$ such that

$$
f ( w , t , t _ { 0 } ) = \phi _ { w } ( w , t , t _ { 0 } ) .
$$

Consider the construction of $f ( w , t , t _ { 0 } )$ and $z ( w , t , t _ { 0 } )$ . Since $z ( w , t , t _ { 0 } ) \circ \alpha _ { 2 } ( g ( z , t , t _ { 0 } )$ $z , t , t _ { 0 } ) \equiv z$ , substituting $w = \alpha _ { 2 } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } )$ in (3.4) and (3.5) yields Equation (3.3). -

Theorem 3.6. $f ( w , t , t _ { 0 } )$ obtained in Theorem 3.5 is also the solution of the following implicit equation:

$$
\begin{array} { r } { \alpha ^ { 1 } \big ( f ( w , t , t _ { 0 } ) , w , t , t _ { 0 } \big ) = g \big ( \alpha ^ { 2 } ( f ( w , t , t _ { 0 } ) , w , t , t _ { 0 } ) , t , t _ { 0 } \big ) . } \end{array}
$$

Theorem 3.7. Let $\alpha$ be defined as in Theorem 3.5, let $w \to \widehat { w } = f ( w , t , t _ { 0 } )$ be $a$ gradient mapping in some neighborhood $\widetilde { \mathcal { R } }$ of $\mathbf { R } ^ { 2 n }$ with Jacobian $f _ { w } ( w , t , t _ { 0 } ) =$ $N ( w , t , t _ { 0 } )$ . If $N$ satisfies in $\widetilde { \mathcal { R } }$ the condition

$$
\begin{array} { r } { \left| C ^ { \alpha } \big ( f ( w , t , t _ { 0 } ) , w , t , t _ { 0 } \big ) N ( w , t , t _ { 0 } ) + D ^ { \alpha } \big ( f ( w , t , t _ { 0 } ) , w , t , t _ { 0 } \big ) \right| \neq 0 , } \end{array}
$$

then in $\widetilde { \mathcal { R } }$ there uniquely exists a $K ( z , t )$ -symplectic mapping $z  \widehat { z } = g ( z , t , t _ { 0 } )$ with Jacobian $g ( z , t , t _ { 0 } ) = M ( z , t , t _ { 0 } )$ such that

$$
\begin{array} { r l r } { \alpha ^ { 1 } ( f ( w , t , t _ { 0 } ) , w , t , t _ { 0 } ) } & { = } & { g ( \alpha ^ { 2 } ( f ( w , t , t _ { 0 } ) , w , t , t _ { 0 } ) , t , t _ { 0 } ) , } \\ { M } & { = } & { ( A ^ { \alpha } N + B ^ { \alpha } ) ( C ^ { \alpha } N + D ^ { \alpha } ) ^ { - 1 } , } \\ { N } & { = } & { ( A _ { \alpha } M + B _ { \alpha } ) ( C _ { \alpha } M + D _ { \alpha } ) ^ { - 1 } . } \end{array}
$$

Remark 3.8. The proofs of Theorems 3.6 and 3.7 are similar to that of Theorem 3.5 and are omitted here. Similar to Theorem 3.6, the function $g ( z , t , t _ { 0 } )$ is the solution of the implicit equation

$$
\alpha _ { 1 } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } ) = f ( \alpha _ { 2 } ( g ( z , t , t _ { 0 } ) , z , t , t _ { 0 } ) , z , t , t _ { 0 } ) .
$$

# 15.4 Symplectic Difference Schemes for Birkhoffian Systems

In Section 15.2, it is indicated that for a general Birkhoffian system, there exists the common property that its phase flow is symplectic. With the result in the last section, symplectic schemes for Birkhoffian systems are constructed by approximating the generating functions.

Birkhoff’s phase flow is denoted by $g ^ { t } ( z , t _ { 0 } )$ and it is a one-parameter group of $K ( z , t )$ -symplectic mappings at least local in $z$ and $t$ , i.e., $g ^ { t _ { 0 } } =$ identity, $g ^ { t _ { 1 } + t _ { 2 } } =$ $g ^ { t _ { 1 } } \circ g ^ { t _ { 2 } }$ . Here $z$ is taken as an initial value when $t = t _ { 0 }$ , and $\widehat { z } ( z , t , t _ { 0 } ) = g ^ { t } ( z , t _ { 0 } ) =$ $g ( t ; z , t _ { 0 } )$ is the solution of the Birkhoffian system (2.8).

Theorem 4.1. Let α be defined as in Theorem 3.5. Let $z \longrightarrow \widehat { z } = g ^ { t } ( z , t _ { 0 } )$ be the phase flow of the Birkhoffian system (2.8), $M ( t ; z , t _ { 0 } ) = g _ { z } ( t ; z , t _ { 0 } )$ is its Jacobian. At some initial point $z$ , i.e., $t = t _ { 0 }$ , $\widehat { z } = z$ , if

$$
| C _ { \alpha } ( z , z , t _ { 0 } , t _ { 0 } ) + D _ { \alpha } ( z , z , t _ { 0 } , t _ { 0 } ) | \ne 0 ,
$$

then for sufficiently small $| t - t _ { 0 } |$ and in some neighborhood of $z \in \mathbf { R } ^ { 2 n }$ there exists $a$ gradient mapping $w  \widehat { w } = f ( w , t , t _ { 0 } )$ with symmetric Jacobian $f _ { w } ( w , t , t _ { 0 } ) =$ $N ( w , t , t _ { 0 } )$ and a uniquely determined scalar generating function $\phi ( w , t , t _ { 0 } )$ such that

$$
\begin{array} { r l } { f ( \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) } & { = \phi _ { w } ( \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) , } \\ { \frac { \partial } { \partial t } \phi _ { w } ( \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) } & { = A ( \phi _ { w } ( \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) , \boldsymbol { w } , \phi _ { w w } ( \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) , \boldsymbol { t } _ { 0 } ) , } \\ { A \big ( \hat { \boldsymbol { w } } , \boldsymbol { w } , \frac { \partial \hat { \boldsymbol { w } } } { \partial \boldsymbol { w } } , \boldsymbol { t } _ { 0 } \big ) } & { = \tilde { A } \big ( \hat { z } ( \boldsymbol { w } , \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) , z ( \hat { w } , \boldsymbol { w } , t , \boldsymbol { t } _ { 0 } ) , \frac { \partial \hat { w } } { \partial \boldsymbol { w } } , \boldsymbol { t } _ { 0 } \big ) , } \\ { \tilde { A } \big ( \hat { z } , z , \frac { \partial \hat { \boldsymbol { w } } } { \partial \boldsymbol { w } } , \boldsymbol { t } _ { 0 } \big ) } & { = \frac { 1 } { \mathrm { d } t } \tilde { w } ( \hat { z } , z , t , \boldsymbol { t } _ { 0 } ) - \frac { \partial \hat { w } } { \partial w } \frac { \mathrm { d } } { \mathrm { d } t } w ( \hat { z } , z , t , \boldsymbol { t } _ { 0 } ) } \\ & { = \Big ( A _ { \alpha } - \frac { \partial \hat { w } } { \partial w } C _ { \alpha } \Big ) K ^ { - 1 } D ( \hat { z } , t ) + \frac { \partial \alpha _ { 1 } } { \partial t } - \frac { \partial \hat { w } } { \partial w } \frac { \partial \alpha _ { 2 } } { \partial t } , } \\ { \alpha _ { 1 } ( g ( t ; z , t _ { 0 } ) , z , t , \boldsymbol { t } _ { 0 } ) } & { = f ( \alpha _ { 1 } ( g ( t ; , z _ { t 0 } ) , z , t , \boldsymbol { t } _ { 0 } ) , t _ { 0 } ) } \\ & { = \phi _ { w } ( \alpha _ { 2 } ( \boldsymbol { t } ( z ; t _ { 0 } ) , z , t _ { 0 } ) , t _ { 0 } ) } \\ &  = \phi _ { w } ( \alpha _ { 1 } ( H ) + B _ { \alpha } ) ( C _ { \alpha } \boldsymbol { u } + D _  \ \end{array}
$$

Proof. $M ( t ; z , t _ { 0 } )$ is differentiable with respect to $z$ and $t$ . Condition (4.1) guarantees that for sufficiently small $| t - t _ { 0 } |$ and for $\widehat { z }$ in some neighborhood of $z \in \mathrm { R } ^ { 2 n }$ , there is

$$
\left| C _ { \alpha } ( \widehat { z } , z , t , t _ { 0 } ) M ( t ; z , t _ { 0 } ) + D _ { \alpha } ( \widehat { z } , z , t , t _ { 0 } ) \right| \neq 0 .
$$

Additionally, the Birkhoffian phase flow is a symplectic mapping; therefore, by Theorem 3.5, there exists a time-dependent gradient map $\widehat { w } = f ( w , t , t _ { 0 } )$ and a scalar function $\phi ( w , t , t _ { 0 } )$ , such that

$$
f ( w , t , t _ { 0 } ) = \phi _ { w } ( w , t , t _ { 0 } ) , \quad \frac { \partial f ( w , t , t _ { 0 } ) } { \partial t } = \frac { \partial \phi _ { w } ( w , t , t _ { 0 } ) } { \partial t } .
$$

Notice that $\widehat { z } = g ( t ; z , t _ { 0 } )$ is the solution of the following initial-value problem;

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } = K ^ { - 1 } ( \widehat { z } , t ) \Big ( \nabla B + \displaystyle \frac { \partial F } { \partial t } \Big ) ( \widehat { z } , t ) , } \\ { \widehat { z } | _ { t = t _ { 0 } } = z , } \end{array} \right.
$$

therefore, from the equation in (3.2), it follows that

$$
\begin{array} { r l } & { \frac { \mathrm { d } \widehat { w } } { \mathrm { d } t } = \frac { \partial \widehat { w } } { \partial \widehat { z } } \cdot \frac { \mathrm { d } \widehat { z } } { \mathrm { d } t } + \frac { \partial } { \partial t } \alpha _ { 1 } ( \widehat { z } , z , t , t _ { 0 } ) = A _ { \alpha } K ^ { - 1 } \Big ( \nabla B + \frac { \partial F } { \partial t } \Big ) + \frac { \partial \alpha _ { 1 } } { \partial t } , } \\ & { \frac { \mathrm { d } w } { \mathrm { d } t } = C _ { \alpha } K ^ { - 1 } \Big ( \nabla B + \frac { \partial F } { \partial t } \Big ) + \frac { \partial \alpha _ { 2 } } { \partial t } , } \end{array}
$$

so

$$
\frac { \partial \widehat { w } } { \partial t } = \frac { \mathrm { d } \widehat { w } } { \mathrm { d } t } - \frac { \partial \widehat { w } } { \partial t } \frac { \mathrm { d } w } { \mathrm { d } t } = \bigg ( A _ { \alpha } - \frac { \partial \widehat { w } } { \partial t } C _ { \alpha } \bigg ) K ^ { - 1 } \bigg ( \nabla B + \frac { \partial F } { \partial t } \bigg ) + \frac { \partial \alpha _ { 1 } } { \partial t } - \frac { \partial \widehat { w } } { \partial w } \frac { \partial \alpha _ { 2 } } { \partial t } .
$$

Since $\frac { \partial \widehat { w } } { \partial w } \neq 0$ , so $w = w ( \widehat { w } , t )$ exists and is solvable in $( \widehat { w } )$ , but it cannot be solved explicitly from the transformation $\alpha$ and $\alpha ^ { - 1 }$ , we have

$$
\hat { \mathcal { A } } \bigg ( \widehat { z } , z , \frac { \partial \widehat { w } } { \partial w } , t , t _ { 0 } \bigg ) = \frac { \partial \widehat { w } } { \partial t } ,
$$

and the Equations (4.4) and (4.5). Then, from (4.6), the Equation (4.3) follows.

According to[FW91b,FW91a,FQ87] , we can easily construct symplectic difference schemes of any order for the autonomous or semi-autonomous Birkhoffian systems. Because of the simplicity of the ordinary geometry structure, the transformation $\alpha$ in (3.1) needed in these cases is independent of the parameter $t$ , accordingly

$$
\begin{array} { r l } { \displaystyle \frac { \partial \widehat { w } } { \partial t } \ = \ \frac { { \mathrm { d } } \widehat { w } } { { \mathrm { d } } t } - \frac { \partial \widehat { w } } { \partial t } \frac { { \mathrm { d } } w } { { \mathrm { d } } t } = \Big ( A _ { \alpha } - \frac { \partial \widehat { w } } { \partial t } C _ { \alpha } \Big ) K ^ { - 1 } \nabla B } & { } \\ { \displaystyle = \ - \Big ( B ^ { \alpha \mathrm { T } } + \Big ( \frac { \partial \widehat { w } } { \partial w } ^ { \mathrm { T } } \Big ) A ^ { \alpha \mathrm { T } } \Big ) \nabla _ { z } B } & { } \\ { \displaystyle = \ - B _ { w } \big ( \widehat { z } ( \widehat { w } , w ) \big ) \quad \big ( \mathrm { o r \ } = - B _ { w } \big ( \widehat { z } ( \widehat { w } , w ) , t \big ) \big ) . } \end{array}
$$

Therefore, the corresponding Birkhoffian system is completely a Hamiltonian system

$$
\frac { \partial \phi ( w , t ) } { \partial t } = - B \big ( \widehat { z } ( \phi _ { w } , w ) \big ) , \quad \frac { \partial \phi ( w , t , t _ { 0 } ) } { \partial t } = - B \big ( \widehat { z } ( \phi _ { w } , w ) , t \big )
$$

in the autonomous and semi-autonomous case, respectively.

Remark 4.2. Because of the forcing term in (2.1), the Hamilton–Jacobi equation for the generating function $\phi ( w , t , t _ { 0 } )$ cannot directly be derived, but instead the Hamilton–Jacobi equation (4.3) for $\phi _ { w } ( w , t , t _ { 0 } )$ can be easily derived. Assume the generating function $\phi _ { w } ( w , t , t _ { 0 } )$ can be expanded as a convergent power series in $t$

$$
\phi _ { w } ( w , t , t _ { 0 } ) = \sum _ { k = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { k } \phi _ { w } ^ { ( k ) } \left( w , t _ { 0 } \right) .
$$

Lemma 4.3. The $k$ -th order total derivative of $\mathcal { A }$ defined as in Theorem 4.1 with respect to $t$ can be described as

$$
\begin{array} { r l } { D _ { t } ^ { k } A = } & { \partial _ { \varphi _ { \infty } } A \Big ( \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \Big ) + \partial _ { \varphi _ { \infty } } A \Big ( \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \Big ) } \\ & { + \partial _ { t } \partial _ { \varphi _ { \infty } } A \Big ( \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i - 1 ) + i } \Big ) + \partial _ { t } \partial _ { \varphi _ { \infty } } A \Big ( \displaystyle \sum _ { i = 1 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - 1 - i ) } } \\ & { + \displaystyle \sum _ { m = 0 } ^ { \infty } C _ { k } ^ { k - m } \displaystyle \sum _ { i = 0 } ^ { \infty } C _ { k - m } ^ { m - n } \displaystyle \sum _ { i = 1 } ^ { k - m - n } \displaystyle \sum _ { i = 1 } ^ { \infty } \displaystyle \sum _ { i = 1 } ^ { \infty } \phi _ { \infty } ^ { ( k ) } \partial _ { \varphi _ { \infty } } \partial _ { \varphi _ { \infty } } ^ { m } \partial _ { s } ^ { m } A } \\ & { \cdot \Big ( \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \cdot \cdot \cdot \cdot \cdot \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \cdot \cdot \cdot \cdot } \\ & { \cdot \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \cdot \cdot \cdot \cdot \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \cdot } \\ & { \cdot \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \cdot \cdot \cdot \displaystyle \sum _ { i = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { i } \phi _ { \infty } ^ { ( k - i ) } \cdot \cdot } \end{array}
$$

then at the point of $t = t _ { 0 }$ , the total derivative of $\mathcal { A }$ is as

$$
\begin{array} { r l } { \displaystyle D _ { t } ^ { k } \mathcal { A } _ { t _ { 0 } } } & { = \ \partial _ { \phi _ { w } } \mathcal { A } _ { t _ { 0 } } \phi _ { w } ^ { ( k ) } + \partial _ { \phi _ { w w } } \mathcal { A } _ { t _ { 0 } } \phi _ { w w } ^ { ( k ) } } \\ & { \quad + \partial _ { t } \partial _ { \phi _ { w } } \mathcal { A } _ { t _ { 0 } } \phi _ { w } ^ { ( k - 1 ) } + \partial _ { t } \partial _ { \phi _ { w } w } \mathcal { A } _ { t _ { 0 } } \phi _ { w w } ^ { ( k - 1 ) } } \\ &  \quad + \displaystyle \sum _ { m = 0 } ^ { k } \mathrm { C } _ { k } ^ { m } \displaystyle \sum _ { n = 1 } ^ { k - m } \sum _ { l = 1 } ^ { k - m - n } \sum _ { \stackrel { h _ { 1 } + \ldots + h _ { n } } { (  \begin{array} { l } { h _ { 1 } + \cdots + h _ { n } } \\ { \psi _ { 1 } + \cdots + j _ { l } = k - m } \end{array}   } \partial _ { \phi _ { w } } ^ { n } \partial _ { \phi _ { w } } ^ { l } \partial _ { t } ^ { m } \mathcal { A } _ { t _ { 0 } } } \\ & { \quad  + ( \phi _ { w } ^ { ( h _ { 1 } ) } , \cdots , \phi _ { w } ^ { ( h _ { n } ) } , \phi _ { w w } ^ { ( j _ { 1 } ) } , \cdots , \phi _ { w w } ^ { ( j _ { l } ) } ) , } \end{array}
$$

where $\mathcal { A } _ { t _ { 0 } } = \mathcal { A } ( \phi _ { w } ^ { ( 0 ) } , w , \phi _ { w w } ^ { ( 0 ) } , t _ { 0 } , t _ { 0 } )$

By means of the representations of the total derivative of $\mathcal { A }$ , the following results are proved.

Theorem 4.4. Let $\mathcal { A }$ and $\alpha$ be analytic. Then the generating function $\phi _ { w \alpha , \mathcal { A } } ( w , t , t _ { 0 } )$ $\mathbf { \Psi } = \phi _ { w } ( w , t , t _ { 0 } )$ can be expanded as a convergent power series in t for sufficiently small $| t - t _ { 0 } |$

$$
\phi _ { w } ( w , t , t _ { 0 } ) = \sum _ { k = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { k } \phi _ { w } ^ { ( k ) } ( w , t _ { 0 } ) ,
$$

and $\phi _ { w } ^ { ( k ) }$ ( $k \geq 0 )$ ), can be recursively determined by the following equations

$$
\begin{array} { r c l } { { \phi _ { w } ^ { ( 0 ) } ( w , t _ { 0 } ) } } & { { = } } & { { f ( w , t _ { 0 } , t _ { 0 } ) , } } \\ { { \phi _ { w } ^ { ( 1 ) } ( w , t _ { 0 } ) } } & { { = } } & { { \displaystyle \mathcal { A } \bigl ( \phi _ { w } ^ { ( 0 ) } , w , \phi _ { w w } ^ { ( 0 ) } , t _ { 0 } , t _ { 0 } \bigr ) , } } \\ { { \phi _ { w } ^ { k + 1 } ( w , t _ { 0 } ) } } & { { = } } & { { \displaystyle \frac { 1 } { ( k + 1 ) ! } D _ { t } ^ { k } \mathcal { A } \bigl ( \phi _ { w } ^ { ( 0 ) } , w , \phi _ { w w } ^ { ( 0 ) } , t _ { 0 } , t _ { 0 } \bigr ) . } } \end{array}
$$

Proof. Differentiating Equation (4.9) with respect to $w$ and $t$ , we derive

$$
\begin{array} { r c l } { { \phi _ { w w } ( w , t , t _ { 0 } ) } } & { { = } } & { { \displaystyle \sum _ { k = 0 } ^ { \infty } ( t - t _ { 0 } ) ^ { k } \phi _ { w w } ^ { ( k ) } ( w , t _ { 0 } ) , } } \\ { { \displaystyle \frac { \partial } { \partial t } \phi _ { w } ( w , t , t _ { 0 } ) } } & { { = } } & { { \displaystyle \sum _ { k = 0 } ^ { \infty } ( k + 1 ) ( t - t _ { 0 } ) ^ { k } \phi _ { w } ^ { ( k + 1 ) } ( w , t _ { 0 } ) . } } \end{array}
$$

By Equation (4.2),

$$
\phi _ { w } ^ { 0 } ( w , t _ { 0 } ) = \phi _ { w } ( w , t _ { 0 } , t _ { 0 } ) = f ( w , t _ { 0 } , t _ { 0 } ) .
$$

Substituting Equations (4.9) and (4.13) in $\mathcal { A } \Big ( \widehat { w } , w , \frac { \partial \widehat { w } } { \partial w } , t , t _ { 0 } \Big )$ , and expanding $\mathcal { A }$ in $t = t _ { 0 }$ , we get

$$
\begin{array} { r c l } { { \displaystyle { \cal A } ( \phi _ { w } , w , \phi _ { w w } , t , t _ { 0 } ) } } & { { = } } & { { \displaystyle { \cal A } ( f ( w , t _ { 0 } , t _ { 0 } ) , w , f _ { w } ( w , t _ { 0 } , t _ { 0 } ) , t _ { 0 } , t _ { 0 } ) } } \\ { { } } & { { } } & { { \displaystyle { + \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ! } ( t - t _ { 0 } ) ^ { k } D _ { t } ^ { k } { \cal A } ( \phi _ { w } ^ { ( 0 ) } , w , \phi _ { w w } ^ { ( 0 ) } , t _ { 0 } , t _ { 0 } ) . } } } \end{array}
$$

Using Equation (4.3) and comparing (4.15) with (4.14), we get (4.11) and (4.12). -

In the autonomous and semi-autonomous case, $\mathcal { A }$ is replaced by the Birkhoffian $B$ , which makes it much easier to expand the generating functions $\phi$ . With Theorems 3.5 and 3.7, the relationship between the Birkhoffian phase flow and the generating function $\phi ( w , t , t _ { 0 } )$ is established. With this result, $K ( z , t )$ -symplectic difference schemes can be directly constructed.

Theorem 4.5. Let $\mathcal { A }$ and $\alpha$ be analytic. For sufficiently small time-step $\tau > 0$ , take

$$
\psi _ { w } ^ { ( m ) } ( w , t _ { 0 } + \tau , t _ { 0 } ) = \sum _ { i = 0 } ^ { m } \tau ^ { i } \phi _ { w } ^ { ( i ) } ( w , t _ { 0 } ) , \quad m = 1 , 2 , \cdots ,
$$

where $\phi _ { w } ^ { ( i ) }$ are determined by Equations (4.10) – (4.12).

Then, $\psi _ { w } ^ { ( m ) } ( w , t _ { 0 } + \tau , t _ { 0 } )$ defines a $K ( z , t )$ -symplectic difference scheme $z = z ^ { k } $ $z ^ { k + 1 } = \widehat { z }$ ,

$$
\alpha _ { 1 } ( z ^ { k + 1 } , z ^ { k } , t _ { k + 1 } , t _ { k } ) = \psi _ { w } ^ { ( m ) } \big ( \alpha _ { 2 } ( z ^ { k + 1 } , z ^ { k } , t _ { k + 1 } , t _ { k } ) , t _ { k + 1 } , t _ { k } \big )
$$

of m-th order of accuracy.

Proof. Let be $N = \phi _ { w w } ( w _ { 0 } , t _ { 0 } , t _ { 0 } ) = \psi _ { w w } ^ { ( m ) } ( w _ { 0 } , t _ { 0 } , t _ { 0 } )$ and $w _ { 0 } = \alpha ( z , z , t _ { 0 } , t _ { 0 } )$ then Theorem 3.7 yields $\vert C ^ { \alpha } N + D ^ { \alpha } \vert$ , because of

$$
| C _ { \alpha } ( z , z , t _ { 0 } , t _ { 0 } ) + D _ { \alpha } ( z , z , t _ { 0 } , t _ { 0 } ) | \ne 0 .
$$

Thus, for sufficiently small $\tau$ and in some neighborhood of $w _ { 0 }$ , there exists

$$
| C ^ { \alpha } N ^ { ( m ) } ( w , t _ { 0 } + \tau , t _ { 0 } ) + D ^ { \alpha } | \neq 0 ,
$$

where

$$
N ^ { ( m ) } ( w , t _ { 0 } + \tau , t _ { 0 } ) = \psi _ { w w } ^ { ( m ) } ( w , t _ { 0 } + \tau , t _ { 0 } ) .
$$

By Theorem 3.7, $\psi _ { w } ^ { ( m ) } ( w , t _ { 0 } + \tau , t _ { 0 } )$ defines a $K ( z , t )$ -symplectic mapping which is expressed in (3.3). Therefore, Equation (4.16) determines a $m$ -th order $K ( z , t )$ - symplectic difference scheme for the Birkhoffian system (2.8). -

# 15.5 Example

In this section, an example illustrates how to obtain schemes preserving the symplectic structure for a nonconservative system expressed in Birkhoffian representation. Consider the linear damped oscillator

$$
\ddot { r } + \nu \dot { r } + r = 0 .
$$

We introduce a gradient function $p$ satisfying $p = { \dot { r } }$ , then a Birkhoffian representation of (5.1) is given by

$$
\left[ \begin{array} { c c } { { 0 } } & { { - \mathrm { e } ^ { \nu t } } } \\ { { \mathrm { e } ^ { \nu t } } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c } { { \begin{array} { c } { { \dot { r } } } \\ { { \dot { p } } } \end{array} } } \end{array} \right] = \left[ \begin{array} { c } { { \begin{array} { c } { { \nu \mathrm { e } ^ { \nu t } p + \mathrm { e } ^ { \nu t } r } } \\ { { \mathrm { e } ^ { \nu t } p } } \end{array} } } \end{array} \right] .
$$

The structure and functions are

$$
\begin{array} { l } { { \displaystyle K = \left[ \begin{array} { c c } { { 0 } } & { { - { \mathrm e } ^ { \nu t } } } \\ { { { \mathrm e } ^ { \nu t } } } & { { 0 } } \end{array} \right] , \quad } } & { { \displaystyle K ^ { - 1 } = \left[ \begin{array} { c c } { { 0 } } & { { { \mathrm e } ^ { - \nu t } } } \\ { { - { \mathrm e } ^ { - \nu t } } } & { { 0 } } \end{array} \right] , } } \\ { { \displaystyle F = \left[ \begin{array} { c } { { \displaystyle \frac { 1 } { 2 } { \mathrm e } ^ { \nu t } p } } \\ { { \displaystyle - \frac { 1 } { 2 } { \mathrm e } ^ { \nu t } r } } \end{array} \right] , \quad } } & { { \displaystyle B = \frac { 1 } { 2 } { \mathrm e } ^ { \nu t } ( r ^ { 2 } + r p + p ^ { 2 } ) , } } \end{array}
$$

and the energy function reads as follows:

$$
H ( q , p ) = { \frac { 1 } { 2 } } ( q ^ { 2 } + p ^ { 2 } ) - \nu p ^ { 2 } .
$$

The Euler midpoint scheme (or one-step Gauss–Runge–Kutta method) for the system (5.2), which can be derived via the discrete Lagrange–d’Alembert principle[MW01] , reads as follows:

$$
\begin{array} { l } { \frac { q _ { k + 1 } - q _ { k } } { \tau } = \frac { p _ { k + 1 } + p _ { k } } { 2 } , } \\ { \frac { p _ { k + 1 } - p _ { k } } { \tau } = - \nu \frac { p _ { k + 1 } + p _ { k } } { 2 } - \frac { q _ { k + 1 } + q _ { k } } { 2 } , } \end{array}
$$

and hence,

$$
\left[ \begin{array} { c } { q _ { k + 1 } } \\ { p _ { k + 1 } } \end{array} \right] = \frac { 1 } { \Delta } \left[ \begin{array} { c c } { - \tau ^ { 2 } + 2 \nu \tau } & { 4 \tau } \\ { - 4 \tau } & { - \tau ^ { 2 } - 2 \nu \tau + 4 } \end{array} \right] \left[ \begin{array} { c } { q _ { k } } \\ { p _ { k } } \end{array} \right] ,
$$

where $\Delta = \tau ^ { 2 } + 2 \nu \tau + 4$ , is not a $K ( z , t )$ -symplectic scheme.

Now, let the transformation $\alpha$ in (3.1) be

$$
\begin{array} { l l } { { \widehat { Q } = \mathrm { e } ^ { \nu t } \widehat { p } - \mathrm { e } ^ { \nu t _ { 0 } } p , } } & { { \widehat { P } = \widehat { q } - q , } } \\ { { Q = \frac { 1 } { 2 } ( \widehat { q } + q ) , } } & { { P = \displaystyle - \frac { 1 } { 2 } ( \mathrm { e } ^ { \nu t } \widehat { p } + \mathrm { e } ^ { \nu t _ { 0 } } p ) , } } \end{array}
$$

where the Jacobian of $\alpha$ is

$$
\begin{array} { r } { \alpha _ { * } = \left[ \begin{array} { c c c c } { 0 } & { \mathrm { e } ^ { \nu t } } & { 0 } & { - \mathrm { e } ^ { \nu t _ { 0 } } } \\ { 1 } & { 0 } & { - 1 } & { 0 } \\ { \frac { 1 } { 2 } } & { 0 } & { \frac { 1 } { 2 } } & { 0 } \\ { 0 } & { - \frac { 1 } { 2 } \mathrm { e } ^ { \nu t } } & { 0 } & { - \frac { 1 } { 2 } \mathrm { e } ^ { \nu t _ { 0 } } } \end{array} \right] . } \end{array}
$$

The inverse transformation is

$$
\begin{array} { l l } { { { \widehat { q } } = \frac { 1 } { 2 } { \widehat { P } } + Q , } } & { { { \widehat { p } } = \frac { 1 } { 2 } \mathbf { e } ^ { - \nu t } { \widehat { Q } } - \mathbf { e } ^ { - \nu t } P , } } \\ { { { q } = - \frac { 1 } { 2 } { \widehat { P } } + Q , } } & { { p = - \frac { 1 } { 2 } \mathbf { e } ^ { \nu t _ { 0 } } { \widehat { Q } } - \mathbf { e } ^ { - \nu t _ { 0 } } P , } } \end{array}
$$

and

$$
\alpha _ { * } ^ { - 1 } = \left[ { \begin{array} { c c c c } { 0 } & { { \frac { 1 } { 2 } } } & { 1 } & { 0 } \\ { { \frac { 1 } { 2 } } \mathrm { e } ^ { - \nu t } } & { 0 } & { 0 } & { - \mathrm { e } ^ { - \nu t } } \\ { 0 } & { - { \frac { 1 } { 2 } } } & { 1 } & { 0 } \\ { - { \frac { 1 } { 2 } } \mathrm { e } ^ { - \nu t _ { 0 } } } & { 0 } & { 0 } & { - \mathrm { e } ^ { - \nu t _ { 0 } } } \end{array} } \right] .
$$

Consequently, using (5.5), (5.6) and (5.2), we derive

$$
\begin{array} { r l } & { \frac { \mathrm { d } \widehat { w } } { \mathrm { d } t } = \left[ \begin{array} { c } { \nu \epsilon ^ { \nu t } \widehat { p } + \mathrm { e } ^ { \nu t } \dot { \widehat { p } } } \\ { \dot { \widehat { q } } } \end{array} \right] = \left[ \begin{array} { c } { - \mathrm { e } ^ { \nu t } \widehat { q } } \\ { \widehat { p } } \end{array} \right] = \left[ \begin{array} { c } { - \frac { 1 } { 2 } \mathrm { e } ^ { \nu t } \widehat { P } - \mathrm { e } ^ { \nu t } Q } \\ { \frac { 1 } { 2 } \mathrm { e } ^ { - \nu t } \widehat { Q } - \mathrm { e } ^ { - \nu t } P } \end{array} \right] , } \\ & { \frac { \mathrm { d } w } { \mathrm { d } t } = \left[ \begin{array} { c } { \frac { 1 } { 4 } \mathrm { e } ^ { - \nu t } \widehat { Q } - \frac { 1 } { 2 } \mathrm { e } ^ { - \nu t } P } \\ { \frac { 1 } { 4 } \mathrm { e } ^ { \nu t } \widehat { P } + \frac { 1 } { 2 } \mathrm { e } ^ { \nu t } Q } \end{array} \right] . } \end{array}
$$

Simple calculations (for $m = 0 , 1$ ) yields,

$$
\begin{array} { r l r } & { \phi _ { w } ^ { ( 0 ) } = \left[ \begin{array} { l } { \widehat { Q } } \\ { \widehat { P } } \end{array} \right] \Big \vert _ { t = t _ { 0 } } = \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] , } & \\ & { \phi _ { w } ^ { ( 1 ) } = \frac { \mathrm { d } \widehat { w } } { \mathrm { d } t } \Big \vert _ { t = t _ { 0 } } - \phi _ { w w } ^ { ( 0 ) } \frac { \mathrm { d } w } { \mathrm { d } t } \Big \vert _ { t = t _ { 0 } } = \left[ \begin{array} { l } { - \mathrm { e } ^ { \nu t _ { 0 } } Q } \\ { - \mathrm { e } ^ { - \nu t _ { 0 } } P } \end{array} \right] . } & \end{array}
$$

Set $\widehat { w } = \phi _ { w } ^ { ( 0 ) } + \phi _ { w } ^ { ( 1 ) } \tau$ , so the first order scheme for the system (5.2) reads as follows:

$$
\begin{array} { r l } & { \frac { q _ { k + 1 } - q _ { k } } { \tau } = \mathrm { e } ^ { - \nu t _ { k + 1 } } \frac { \mathrm { e } ^ { \nu t _ { k + 1 } } p _ { k * 1 } + \mathrm { e } ^ { \nu t _ { k } } p _ { k } } { 2 } , } \\ & { \frac { \mathrm { e } ^ { \nu t _ { k + 1 } } p _ { k + 1 } - \mathrm { e } ^ { \nu t _ { k } } p _ { k } } { \tau } = - \mathrm { e } ^ { \nu t _ { k } } \frac { q _ { k + 1 } + q _ { k } } { 2 } , } \end{array}
$$

and hence

$$
\left[ \begin{array} { c } { q _ { k + 1 } } \\ { p _ { k + 1 } } \end{array} \right] = \frac { 1 } { \Delta } \left[ \begin{array} { c c } { 4 - \tau ^ { 2 } } & { 4 \tau } \\ { - 4 \tau \mathrm { e } ^ { - \nu \tau } } & { ( 4 - \tau ^ { 2 } ) \mathrm { e } ^ { - \nu \tau } } \end{array} \right] \left[ \begin{array} { c } { q _ { k } } \\ { p _ { k } } \end{array} \right] ,
$$

where $\Delta = 4 + \tau ^ { 2 }$ . The transition matrix denoted by $A$ satisfies

$$
A ^ { \mathrm { T } } \left[ \begin{array} { c c } { 0 } & { - \mathrm e ^ { \nu t _ { k + 1 } } } \\ { \mathrm e ^ { \nu t _ { k + 1 } } } & { 0 } \end{array} \right] A = \left[ \begin{array} { c c } { 0 } & { - \mathrm e ^ { \nu t _ { k } } } \\ { \mathrm e ^ { \nu t _ { k } } } & { 0 } \end{array} \right] .
$$

Then, consider the transformation $\alpha$ in (3.1) to be

$$
\begin{array} { l l } { { \widehat { Q } = \mathrm { e } ^ { \nu t / 2 } \widehat { p } - \mathrm { e } ^ { \nu t _ { 0 } / 2 } p , } } & { { \widehat { P } = - \mathrm { e } ^ { \nu t / 2 } \widehat { q } + \mathrm { e } ^ { \nu t _ { 0 } / 2 } q , } } \\ { { } } & { { Q = \frac { 1 } { 2 } ( \mathrm { e } ^ { \nu t / 2 } \widehat { q } + \mathrm { e } ^ { \nu t _ { 0 } / 2 } q ) , } } & { { P = - \frac { 1 } { 2 } ( \mathrm { e } ^ { \nu t } \widehat { p } + \mathrm { e } ^ { \nu t _ { 0 } } p ) . } } \end{array}
$$

The Jacobian of $\alpha$ is

$$
\alpha _ { * } = \left[ \begin{array} { c c c c } { { 0 } } & { { \mathrm { e } ^ { \nu t / 2 } } } & { { 0 } } & { { - \mathrm { e } ^ { \nu t _ { 0 } / 2 } } } \\ { { - \mathrm { e } ^ { \nu t / 2 } } } & { { 0 } } & { { \mathrm { e } ^ { \nu t _ { 0 } / 2 } } } & { { 0 } } \\ { { \frac { 1 } { 2 } \mathrm { e } ^ { \nu t / 2 } } } & { { 0 } } & { { \frac { 1 } { 2 } \mathrm { e } ^ { \nu t _ { 0 } / 2 } } } & { { 0 } } \\ { { 0 } } & { { - \frac { 1 } { 2 } \mathrm { e } ^ { \nu t } } } & { { 0 } } & { { - \frac { 1 } { 2 } \mathrm { e } ^ { \nu t _ { 0 } } } } \end{array} \right]
$$

and the inverse

$$
\alpha _ { * } ^ { - 1 } = \left[ { \begin{array} { c c c c } { 0 } & { { \frac { 1 } { 2 } } } & { 1 } & { 0 } \\ { { \frac { 1 } { 2 } } \mathbf { e } ^ { - \nu t } } & { 0 } & { 0 } & { - \mathbf { e } ^ { - \nu t } } \\ { 0 } & { - { \frac { 1 } { 2 } } } & { 1 } & { 0 } \\ { - { \frac { 1 } { 2 } } \mathbf { e } ^ { - \nu t _ { 0 } } } & { 0 } & { 0 } & { - \mathbf { e } ^ { - \nu t _ { 0 } } } \end{array} } \right] .
$$

Direct calculation yields the scheme of second order

$$
\begin{array} { r l } & { \frac { \mathrm { e } ^ { \nu t _ { k + 1 } / 2 } q _ { k + 1 } - \mathrm { e } ^ { \nu t _ { k } / 2 } q _ { k } } { \tau } = \frac { \mathrm { e } ^ { \nu t _ { k + 1 } / 2 } p _ { k + 1 } + \mathrm { e } ^ { \nu t _ { k } / 2 } p _ { k } } { 2 } + \nu \frac { \mathrm { e } ^ { \nu t _ { k + 1 } / 2 } q _ { k + 1 } + \mathrm { e } ^ { \nu t _ { k } / 2 } q _ { k } } { 4 } , } \\ & { \frac { \mathrm { e } ^ { \nu t _ { k + 1 } / 2 } p _ { k + 1 } - \mathrm { e } ^ { \nu t _ { k } / 2 } p _ { k } } { \tau } = \frac { \mathrm { e } ^ { \nu t _ { k + 1 } / 2 } q _ { k + 1 } + \mathrm { e } ^ { \nu t _ { k } / 2 } q _ { k } } { 2 } - \nu \frac { \mathrm { e } ^ { \nu t _ { k + 1 } / 2 } p _ { k + 1 } + \mathrm { e } ^ { \nu t _ { k } / 2 } p _ { k } } { 4 } , } \end{array}
$$

and hence,

$$
\left[ \begin{array} { l } { q _ { k + 1 } } \\ { p _ { k + 1 } } \end{array} \right] = \frac { \mathrm { e } ^ { - \nu \tau / 2 } } { \Delta } \left[ \begin{array} { c c } { w _ { 1 } } & { - 1 6 \tau } \\ { 1 6 \tau } & { w - 2 } \end{array} \right] \left[ \begin{array} { l } { q _ { k } } \\ { p _ { k } } \end{array} \right] ,
$$

where $\Delta = \nu ^ { 2 } \tau ^ { 2 } - 4 \tau ^ { 2 } - 1 6$ ,

$$
w _ { 1 } = - 1 6 - 8 \nu \tau - \nu ^ { 2 } \tau ^ { 2 } + 4 \tau ^ { 4 } , \quad w _ { 2 } = - 1 6 + 8 \nu \tau - \nu ^ { 2 } \tau ^ { 2 } + 4 \tau ^ { 2 } .
$$

Abbreviating the matrix $\frac { \mathrm { e } ^ { - \nu \tau / 2 } } { \Delta _ { - } } ( * )$ in (5.8) by $M ( \tau )$ , then by composition $[ \mathrm { Y o s 9 0 } , \mathrm { Q Z 9 2 } ]$ we have the scheme of order four

$$
\left[ \begin{array} { l } { q _ { k + 1 } } \\ { p _ { k + 1 } } \end{array} \right] = M ( c _ { 1 } \tau ) M ( c _ { 2 } \tau ) M ( c _ { 1 } \tau ) \left[ \begin{array} { l } { q _ { k } } \\ { p _ { k } } \end{array} \right] ,
$$

where

$$
c _ { 1 } = \frac { 1 } { 2 - 2 ^ { 1 / 3 } } , \quad c _ { 2 } = \frac { - 2 ^ { 1 / 3 } } { 2 - 2 ^ { 1 / 3 } } .
$$

If take $m = 2$ , we have

$$
\phi _ { w } ^ { ( 2 ) } = 0 .
$$

Now take $m = 3$ ,

$$
\begin{array} { r l } { \phi _ { w } ^ { ( 3 ) } ~ = ~ \frac { 1 } { 3 ! } \frac { \partial } { \partial t } \Bigl \{ \frac { \partial } { \partial t } \Bigl ( \frac { \mathrm { d } \widetilde { w } } { \mathrm { d } t } \Bigr ) + \frac { \partial } { \partial \widetilde { w } } \Bigl ( \frac { \mathrm { d } \widetilde { w } } { \mathrm { d } t } \Bigr ) \frac { \partial \widetilde { w } } { \partial t } - \frac { \partial \widetilde { w } } { \partial w } \frac { \partial } { \partial \widetilde { w } } \Bigl ( \frac { \mathrm { d } w } { \mathrm { d } t } \Bigr ) \frac { \partial \widetilde { w } } { \partial t } } & { } \\ { ~ } & { - \frac { \partial \widetilde { w } } { \partial w } \frac { \partial } { \partial t } \Bigl ( \frac { \mathrm { d } w } { \mathrm { d } t } \Bigr ) - \frac { \partial } { \partial t } \Bigl ( \frac { \partial \widetilde { w } } { \partial w } \Bigr ) \frac { \mathrm { d } w } { \mathrm { d } t } \Bigr \} . } \end{array}
$$

For equation $\ddot { q } + \nu \dot { q } + q = 0$ , 3rd derivatives of $\phi$ in time $t = t _ { 0 }$ , only one term to appear, i.e.,

$$
- \frac { \partial } { \partial t } \bigg ( \frac { \partial \widetilde { w } } { \partial w } \bigg ) \frac { \partial } { \partial \widetilde { w } } \bigg ( \frac { { \mathrm { d } } w } { { \mathrm { d } } t } \bigg ) \frac { \partial \widetilde { w } } { \partial t } .
$$

Simple calculation yields

$$
\begin{array} { r l } { \phi _ { \omega } ^ { ( 3 ) } | _ { t = t _ { 0 } } = } & { - \frac { 1 } { 6 } \left| \begin{array} { l l } { - 1 } & { - \frac { \nu } { 2 } } \\ { - \frac { \nu } { 2 } } & { - 1 } \end{array} \right| \left| \begin{array} { l l } { \frac { 1 } { 8 } } & { - \frac { \nu } { 8 } } \\ { - \frac { \nu } { 8 } } & { \frac { 1 } { 4 } } \end{array} \right| \left| \begin{array} { l } { - \frac { \nu } { 2 } P - Q } \\ { - \frac { \nu } { 2 } Q - P } \end{array} \right| } \\ & { = } & { - \frac { 1 } { 6 } \left| \begin{array} { l } { \Big ( - \frac { 1 } { 4 } + \frac { 1 } { 1 6 } \nu ^ { 2 } \Big ) \Big ( Q + \frac { \nu P } { 2 } \Big ) } \\ { \Big ( - \frac { 1 } { 4 } + \frac { 1 } { 1 6 } \nu ^ { 2 } \Big ) \Big ( \frac { \nu Q } { 2 } + P \Big ) } \end{array} \right| } \\ & { = } & { \left| \begin{array} { l } { \Big ( \frac { \nu ^ { 2 } } { 2 } - 2 \Big ) Q + \Big ( \frac { \nu ^ { 2 } } { 2 } - 2 \Big ) \frac { \nu } { 2 } P } \\ { \Big ( \frac { \nu ^ { 2 } } { 2 } - 2 \Big ) P + \Big ( \frac { \nu ^ { 2 } } { 2 } - 2 \Big ) \frac { \nu } { 2 } Q } \end{array} \right| , } \end{array}
$$

we get 4-th order symmetrical symplectic scheme: $\widetilde { w } = \phi _ { w } ^ { ( 1 ) } \Delta t + \phi _ { w } ^ { ( 3 ) } \Delta t ^ { 2 }$ , i.e.,

$$
\begin{array} { r l } { \frac { e ^ { \pi t _ { k + 1 } / 2 } g _ { k + 1 } - e ^ { \pi t _ { k } / 2 } g _ { k } } { 7 } } & { = \frac { e ^ { \pi t _ { k + 1 } / 2 } g _ { k + 1 } + e ^ { \pi t _ { k } / 2 } g _ { k } } { 2 } + \nu \frac { e ^ { \pi t _ { k + 1 } / 2 } g _ { k + 1 } } { 4 } + \nu \frac { e ^ { \pi t _ { k + 1 } / 2 } g _ { k + 1 } } { 4 } } \\ & { \quad + \tau ^ { 2 } \frac { 1 } { 2 4 \times 4 } \Big [ \Big ( \frac { p ^ { 2 } } { 2 } - 2 \Big ) \Big ( e ^ { \pi t _ { k + 1 } / 2 } p _ { k + 1 } + e ^ { \pi t _ { k } / 2 } p _ { k } \Big ) } \\ & { \quad + \Big ( \frac { p ^ { 2 } } { 2 } - 2 \Big ) \frac { \nu } { 2 } \Big ( e ^ { \nu t _ { k + 1 } / 2 } \theta _ { k + 1 } + e ^ { \pi t _ { k } / 2 } g _ { k } \Big ) \Big ] , } \\ { \frac { e ^ { \pi t _ { k + 1 } / 2 } p _ { k + 1 } - e ^ { \pi t _ { k } / 2 } p _ { k } } { 7 } } & { = \frac { e ^ { \pi t _ { k + 1 } / 2 } g _ { k + 1 } + e ^ { \pi t _ { k } / 2 } g _ { k } } { 2 } - \nu \frac { e ^ { \pi t _ { k + 1 } / 2 } p _ { k + 1 } } { 4 } + e ^ { \pi t _ { k } / 2 } g _ { k } } \\ & { \quad - \tau ^ { 2 } \frac { 1 } { 2 4 \times 4 } \Big [ \Big ( \frac { p ^ { 2 } } { 2 } - 2 \Big ) \Big ( e ^ { \pi t _ { k + 1 } / 2 } g _ { k + 1 } + e ^ { \pi t _ { k } / 2 } g _ { k } \Big ) } \\ & { \quad + \Big ( \frac { p ^ { 2 } } { 2 } - 2 \Big ) \frac { \nu } { 2 } \Big ( e ^ { \nu t _ { k + 1 } / 2 } p _ { k + 1 } + e ^ { \pi t _ { k } / 2 } p _ { k } \Big ) \Big ] . } \end{array}
$$

This method is easily extended to more general ODEs such as

$$
\left\{ \begin{array} { l l } { \dot { p } + \beta ^ { \prime } ( t ) p + V ( q , t ) = 0 , } \\ { \dot { q } - G ( p , t ) = 0 . } \end{array} \right.
$$

Remark 5.1. The derived schemes (5.7), (5.8), and (5.9) are $K ( z , t )$ -symplectic, i.e., for $\tau > 0$ and $k \leq 0$ they satisfy the Birkhoffian condition

$$
\mathbf { e } ^ { \nu t _ { k + 1 } } \mathrm { ~ d } q _ { k + 1 } \wedge \mathrm { d } p _ { k + 1 } = \mathrm { e } ^ { \nu t _ { k } } \mathrm { ~ d } q _ { k } \wedge \mathrm { d } p _ { k } .
$$

# 15.6 Numerical Experiments

In this section, we present numerical results for the linear damped oscillator (5.1), resp., (5.2) using the derived $K ( z , t )$ -symplectic schemes (5.7), (5.8), and (5.9) of order one, two, and four, respectively. Further, we use Euler’s midpoint scheme (5.4), which is not $K ( z , t )$ -symplectic but shows convenient numerical results[MW01] , and further Euler’s explicit scheme for comparison.

In the presented figures, the initial values are always chosen as $q ( 0 ) \ = \ 1$ , $p ( 0 ) = \dot { q } ( 0 ) = - 1$ , and the time interval is from 0 to 25. There are only small differences in the behavior of the different schemes choosing other initial values. The actual error, $\mathrm { e r r } = |$ approximate solution - true solution|, is computed with step size $\tau = 0 . 2$ . Using different step sizes, the schemes always show the same quality, which is emphasized by representing the results in a double logarithmic scale using step sizes $\tau = 0 . 0 1$ , 0.02, 0.05, 0.1, 0.2, 0.5. The orbits are computed with step size $\tau = 0 . 0 5$ .

The first comparison is given between scheme (5.7) and Euler’s explicit scheme both are of order one. For smaller $\nu$ , i.e., $0 \leq \nu \leq 1 . 3$ scheme (5.7) is better, and for $\nu > 1 . 3$ Euler’s explicit scheme is better. The second comparison is given between scheme (5.8) and Euler’s midpoint scheme (5.4) both are of order two. For $0 \leq \nu \leq$ 0.5 both schemes show the same behavior, for $0 . 5 < \nu < 2 . 8$ scheme (5.8) is better, where the most advantage is around $\nu = 2$ , and for $2 . 8 \leq \nu$ Euler’s midpoint scheme behaves better. The third comparison is given between scheme (5.9) of order four and scheme (5.8) of order two. Both schemes have the same structure preserving property, and therefore the higher order scheme (5.9) shows a clear superiority over the twoorder scheme. These differences between the discussed schemes are illustrated by the error curves (Figs. 6.1 and 6.4).

For the energy function (5.3), the comparisons of the energy error $H$ , between the different schemes are also done in double logarithmic scales (Figs. 6.5 and 6.8). The result shows that the dominance is not clear between scheme (5.7) and Euler’s explicit scheme while scheme (5.8) is always better than Euler’s midpoint scheme for growing $\nu$ , even for $\nu \ge 2 . 8$ . Scheme (5.9) keeps its superiority in the comparisons.

The comparisons also show that it is possible for different schemes obtained from different transformation $\alpha$ , that different quantities are preserved. This point is proved to be true in the generating function method for Hamiltonian systems (see Feng et $\mathrm { a l } ^ { \mathrm { [ F W 9 1 b , F W 9 1 a ] } } )$ . The extension to application in Birkhoffian systems will also be studied in a prospective paper.

![](images/7cb5ea6aca02628c73fd9f9e729497b79415b22ead76db6b44434cbb1cf579a5.jpg)  
Fig. 6.1. Error comparison between the different schemes for $\nu = 0 . 6$

![](images/ed0c561d27f2c4a6171c8a9f6bce59f3867dd0031070a53c103116aebed60554.jpg)  
Fig. 6.2. Error comparison between the different schemes for $\nu = 1 . 3$

![](images/e956999c586d9ade01ca7f5c6e2026387d1e57176a90791da97499285666c1a6.jpg)  
Fig. 6.3. Error comparison between the different schemes for $\nu = 1 . 9$

![](images/7c39a60056b8e3f1d2d5717975a51403a1e91ee2083d723c485006c09ec5e7cf.jpg)  
Fig. 6.4. Error comparison between the different schemes for $\nu = 2 . 8$

![](images/2511560f356552d76447ba27438f56b8a8d3af9c99d2fb414a5a2771a845439c.jpg)  
Fig. 6.5. Energy error comparison between the different schemes for $\nu = 0 . 6$

![](images/7e50c1f8f6ef038e86496df9688967417526ea50909023b2c3ecee8f076da882.jpg)  
Fig. 6.6. Energy error comparison between the different schemes for $\nu = 1 . 3$

![](images/d5a144037b8044bb5398c46bbf122fb84b455854519e2f03656208f5a78c3ff9.jpg)  
Fig. 6.7. Energy error comparison between the different schemes for $\nu = 1 . 9$

![](images/81e2156548d3162a62e87d5be5ea71a9b94661db985ae46696e23ecbb77a2c30.jpg)  
Fig. 6.8. Energy error comparison between the different schemes for $\nu = 2 . 8$

# Bibliography

[AH75] R.W. Atherton and G.M. Homsy: On the existence and formulation of variational principles for nonlinear differential equations. Studies in Applied Mathematics, LIV(1):1531– 1551, (1975).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FW91a] K. Feng and D.L. Wang: A Note on conservation laws of symplectic difference schemes for Hamiltonian systems. J. Comput. Math., 9(3):229–237, (1991).   
[FW91b] K. Feng and D.L. Wang: Symplectic difference schemes for Hamiltonian systems in general symplectic structure. J. Comput. Math., 9(1):86–96, (1991).   
[GLSM01] Y.X. Guo, S.K. Luo, M. Shang, and F.X. Mei: Birkhoffian formulations of nonholonomic constrained systems. Reports on Mathematical Physics, 47:313–322, (2001).   
[HLW02] E. Hairer, Ch. Lubich, and G. Wanner: Geometric Numerical Integration. Number 31 in Springer Series in Computational Mathematics. Springer-Verlag, Berlin, (2002).   
[MP91] E. Massa and E. Pagani: Classical dynamics of non-holonomic systems : a geometric approach. Annales de l’institut Henri Poincar (A) Physique thorique, 55(1):511–544, (1991).   
[MR99] J. E. Marsden and T. S. Ratiu: Introduction to Mechanics and Symmetry. Number 17 in Texts in Applied Mathematics. Springer-Verlag, Berlin, second edition, (1999).   
[MW01] J. E. Marsden and M. West: Discrete mechanics and variational integrators. Acta Numerica, 10:357–514, (2001).   
[QZ92] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[San83a] R.M. Santilli; Foundations of Theoretical Mechanics I. Springer-Verlag, New York, Second edition, (1983).   
[San83b] R.M. Santilli: Foundations of Theoretical Mechanics II. Springer-Verlag, New York, Second edition, (1983).   
[SQ03] H. L. Su and M. Z. Qin: Symplectic schemes for Birkhoffian system. Technical Report arXiv: math-ph/0301001, (2003).   
[SSC94] J. M. Sanz-Serna and M. P. Calvo: Numerical Hamiltonian Problems. AMMC 7. Chapman & Hall, London, (1994).   
[SSQS07] H. L. Su, Y.J. Sun, M. Z. Qin, and R. Scherer: Symplectic schemes for Birkhoffian system. Inter J of Pure and Applied Math, 40(3):341–366, (2007).   
[SVC95] W. Sarlet, A. Vandecasteele, and F. Cantrijn: Derivations of forms along a map: The framework for time-dependent second-order equations. Diff. Geom. Appl., 5:171–203, (1995).   
[Yos90] H. Yoshida: Construction of higher order symplectic integrators. Physics Letters A, 150:262–268, (1990).
