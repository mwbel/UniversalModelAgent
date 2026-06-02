CHAPTER 4

# ELECTROMAGNETISM AND DIFFERENTIAL FORMS

Theether trembledat hisagitations In a manner so familiar that I only need to say, In accordance with Clerk Maxwell's six equations It tickled peoples‘optics far away. You can feel the way it's done, You may trace them as they rundy by dy less dβ by dz is equal KdX/dt..

While the curl of (X,Y, Z) is the minus d/dt of the vector (a, b,c):

From The Revolution of the Corpuscle, written by A.A.Robb   
(to the tune of The Interfering Parrott)   
for a dinner of the research students of the Cavendish Laboratory in the days of the old mathematics.

This chapter is all Track 2. It is needed as preparation for \$\$14.5 and 14.6 (computation of curvature using differential forms) and for Chapter 15 (Bianchi identities and boundary of a boundary),but is not needed for the rest of the book.

# \$4.1. EXTERIOR CALCULUS

Stacks of surfaces, individually or intersecting to make “honeycombs,”"egg crates,” and other such structures ("differential formns"), give unique insight into the geometry of electromagnetism and gravitation.However, such insight comes at some cost in time.Therefore, most readers should skip this chapter and later material that depends on it during a first reading of this book.

Analytically speaking, differential forms are completely antisymmetric tensors; pictorially speaking, they are intersecting stacks of surfaces. The mathematical formalism for manipulating differential forms with ease,called “exterior calculus,” is summarized concisely in Box 4.l; its basic features are illustrated in the rest of this chapter by rewriting electromagnetic theory in its language. An effective way to tackle this chapter might be to(l) scan Box 4.l to get the flavor of the formalism; (2) read the rest of the chapter in detail; (3) restudy Box 4.l carefully; (4) get practice in manipulating the formalism by working the exercises.\*

# Box 4.1 DIFFERENTIAL FORMS AND EXTERIOR CALCULUS IN BRIEF

The fundamental definitions and formulas of exterior calculus are summarized here for ready reference. Each item consists of a general statement (at left of page) plus a leading application (at right of page). This formalism is applicable not only to spacetime, but also to more general geometrical systems (see heading of each section). No attempt is made here to demonstrate the internal consistency of the formalism, nor to derive it from any set of definitions and axioms. For a systematic treatment that does so, see, e.g., Spivak (l965),or Misner and Wheeler (1957).

# A. Algebra l (applicable to any vector space)

1. Basis 1-forms.

a. Coordinate basis $\pmb { \omega } ^ { j } = \pmb { d x } ^ { j }$ $( j$ tells which 1-form, not which component). b. General basis $\omega ^ { j } = L _ { \boldsymbol { k } ^ { \prime } } ^ { j } d \boldsymbol { x } ^ { \boldsymbol { k } ^ { \prime } }$ .

An application

Simple basis l-forms for analyzing Schwarzschild geometry around static spherically symmetric center of attraction:

$$
\begin{array} { r l } & { \pmb { \omega } ^ { 0 } = ( 1 - 2 m / r ) ^ { 1 / 2 } \pmb { d } t ; } \\ & { \pmb { \omega } ^ { 1 } = ( 1 - 2 m / r ) ^ { - 1 / 2 } \pmb { d } r ; } \\ & { \pmb { \omega } ^ { 2 } = r \pmb { d } \theta ; } \\ & { \pmb { \omega } ^ { 3 } = r \sin \theta \pmb { d } \phi . } \end{array}
$$

2.General p-form (or p-vector) is a completely antisymmetric tensor of rank $( \boldsymbol { \mathsf { \Sigma } } _ { p } ^ { 0 } )$ [or $\left( _ { 0 } ^ { p } \right) ]$ . It can be expanded in terms of wedge products (see $\ S 3 . 5$ and exercise 4.12):

$$
\begin{array} { c } { { \pmb { \alpha } = \displaystyle \frac { 1 } { p ! } \alpha _ { i _ { 1 } i _ { 2 } \ldots i _ { p } } \pmb { \omega } ^ { i _ { 1 } } \wedge \pmb { \omega } ^ { i _ { 2 } } \wedge \cdot \cdot \cdot \wedge \pmb { \omega } ^ { i _ { p } } } } \\ { { \equiv \alpha _ { | i _ { 1 } i _ { 2 } \ldots i _ { p } | } \pmb { \omega } ^ { i _ { 1 } } \wedge \pmb { \omega } ^ { i _ { 2 } } \wedge \cdot \cdot \cdot \wedge \pmb { \omega } ^ { i _ { p } } . } } \end{array}
$$

(Note: Vertical bars around the indices mean sum-

mation extends only over $i _ { 1 } < i _ { 2 } < \ldots < i _ { p } . )$

Two applications Energy-momentum l-form is of type $\pmb { \alpha } = \alpha _ { i } \pmb { \omega } ^ { i }$ or

$$
p = - E d t + p _ { x } d x + p _ { y } d y + p _ { z } d z .
$$

Faraday is a 2-form of type $\beta = \beta _ { \vert \mu \nu \vert } \omega ^ { \mu } \wedge \omega ^ { \nu }$ or in flat spacetime

$$
\begin{array} { l } { F = - E _ { z } d t \wedge d x - E _ { y } d t \wedge d y - E _ { z } d t \wedge d z } \\ { \qquad + B _ { z } d y \wedge d z + B _ { y } d z \wedge d x + B _ { z } d x \wedge d y } \end{array}
$$

3. Wedge product.

All familiar rules of addition and multiplication hold,such as

$$
\begin{array} { c } { { ( a \pmb { \alpha } + b \pmb { \beta } ) \wedge \gamma = a \pmb { \alpha } \wedge \gamma + b \pmb { \beta } \wedge \pmb { \gamma } , } } \\ { { ( \pmb { \alpha } \wedge \pmb { \beta } ) \wedge \pmb { \gamma } = \pmb { \alpha } \wedge ( \pmb { \beta } \wedge \pmb { \gamma } ) \equiv \pmb { \alpha } \wedge \pmb { \beta } \wedge \gamma , } } \end{array}
$$

except for a modified commutation law between a $p$ form $\pmb { \alpha }$ and a $q$ form $\pmb { \beta }$ ：

$$
\begin{array} { r } { \frac { \alpha } { p } \wedge \beta = ( - 1 ) ^ { p q } \beta \wedge \frac { \alpha } { p } . } \end{array}
$$

Applications to $^ { I }$ -forms ${ \pmb { a } } , { \pmb { \beta } }$ ：

$$
\begin{array} { c } { { \pmb { \alpha } \wedge \beta = - \pmb \beta \wedge \pmb \alpha , \qquad \pmb \alpha \wedge \pmb \alpha = 0 ; } } \\ { { \pmb \alpha \wedge \pmb \beta = ( \alpha _ { j } \pmb \omega ^ { j } ) \wedge ( \beta _ { k } \pmb \omega ^ { k } ) = \alpha _ { j } \beta _ { k } \pmb \omega ^ { j } \wedge \pmb \omega ^ { k } } } \\ { { = \displaystyle \frac { 1 } { 2 } ( \alpha _ { j } \beta _ { k } - \beta _ { j } \alpha _ { k } ) \pmb \omega ^ { j } \wedge \pmb \omega ^ { k } . } } \end{array}
$$

4. Contraction of p-form on p-vector.

$$
\begin{array} { r l } & { \quad ^ { \circ } p ^ { \prime } \circ ^ { \prime } } \\ & { = \alpha _ { | i _ { 1 } \dots i _ { p } | } A ^ { | j _ { 1 } \dots j _ { p } | } \langle { \underline { { \omega } } } ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge \omega ^ { i _ { p } } , \pmb { e } _ { j _ { 1 } } \wedge \cdot \cdot \cdot \wedge \pmb { e } _ { j _ { p } } \rangle } \\ & { \qquad [ \equiv \delta _ { j _ { 1 } \dots j _ { p } } ^ { i _ { 1 } \dots i _ { p } } \mathrm { ~ ( s e e ~ e x e r c i s e s ~ 3 . 1 3 ~ a n d ~ 4 . 1 2 ) ] ~ } } \\ & { = \alpha _ { | i _ { 1 } \dots i _ { p } | } A ^ { i _ { 1 } \dots i _ { p } } . } \end{array}
$$

Four applications

a. Contraction of a particle's energy-momentum 1-form ${ \pmb p } = p _ { \alpha } { \pmb \omega } ^ { \alpha }$ with 4-velocity $\pmb { \mu } = \pmb { u } ^ { \alpha } \pmb { \mathcal { e } } _ { \alpha }$ of observer (a 1-vector):

$$
- \langle p , u \rangle = - p _ { \alpha } u ^ { \alpha } = { \mathrm { e n e r g y ~ o f ~ p a r t i c l e } } .
$$

b.Contraction of Faraday 2-form F with bivector δP > △P [where δP = (dP/d>_)△λ1 and △P = $( d \mathcal { P } / d \lambda _ { 2 } ) \varDelta \lambda _ { 2 }$ are two infinitesimal vectors in a 2-surface $\mathcal { P } ( \lambda _ { 1 } , \lambda _ { 2 } )$ ,and the bivector represents the surface element they span] is the magnetic flux $\boldsymbol { \varPhi } = \langle \boldsymbol { F } , \delta \mathcal { P }$ $\wedge \ 4 \mathcal { P } \rangle$ through that surface element.

c. More generally, a $p$ -dimensional parallelepiped with vectors $a _ { 1 } , a _ { 2 } , \ldots , a _ { p }$ for legs has an oriented volume described by the “simple"p-vector a1 ^ a2 ^ . ap (oriented because interchange of two legs changes its sign). An egg-crate type of structure with walls made from the hyperplanes of $p$ different 1-forms $\pmb { \sigma } ^ { 1 }$ ，

$\pmb { \sigma } ^ { 2 } , \ldots , \pmb { \sigma } ^ { p }$ is described by the“simple" $p$ -form $\pmb { \sigma } ^ { 1 }$ $\wedge \sigma ^ { 2 } \wedge \ . . . \wedge \ \sigma ^ { p }$ The number of cells of $\pmb { \sigma } ^ { 1 } \wedge$ $\sigma ^ { 2 } \wedge \dots \wedge \sigma ^ { p }$ sliced through by the infinitesimal $p$ -volume $a _ { 1 } \wedge a _ { 2 } \wedge \dots \wedge a _ { p }$ is

$$
\langle \pmb { \sigma } ^ { 1 } \wedge \pmb { \sigma } ^ { 2 } \wedge \dots \wedge \pmb { \sigma } ^ { p } , \pmb { a } _ { 1 } \wedge \pmb { a } _ { 2 } \wedge \dots \wedge \pmb { a } _ { p } \rangle .
$$

d. The Jacobian determinant of a set of p functions $f ^ { k } ( x ^ { 1 } , \ldots , x ^ { n } )$ with respect to $p$ of their arguments is

$$
{ \begin{array} { r } { \left. d f ^ { 1 } \wedge d f ^ { 2 } \wedge \ \cdot \ \cdot \ \wedge \ d f ^ { p } , { \frac { \partial { \mathcal { S } } } { \partial x ^ { 1 } } } \wedge { \frac { \partial { \mathcal { S } } } { \partial x ^ { 2 } } } \wedge \ \cdot \ \cdot \ \wedge \ { \frac { \partial { \mathcal { P } } } { \partial x ^ { p } } } \right. } \\ { = \operatorname* { d e t } { \left\| \left( { \frac { \partial f ^ { k } } { \partial x ^ { j } } } \right) \right\| } \equiv { \frac { \partial ( f ^ { 1 } , f ^ { 2 } , \cdot \ \cdot \ , f ^ { p } ) } { \partial ( x ^ { 1 } , x ^ { 2 } , \cdot \ . \ . \ , x ^ { p } ) } } . } \end{array} }
$$

5. Simple forms.

a. A simple $p$ -form is one that can be written as a wedge product of $p$ 1-forms:

$$
\underset { p } { \pmb \sigma } = \underset { \ b { \alpha } } { \pmb \alpha } \wedge \underset { \ b { \beta } } { \pmb \beta } \wedge \underset { \ast \ b { \cdots } } { \cdot \cdot \cdot } \wedge \underset { \ b { \gamma } } { \pmb \gamma } .
$$

b. A simple $p$ -form $\pmb { \alpha } \wedge \pmb { \beta } \wedge \dots \wedge \pmb { \gamma }$ is represented by the intersecting families of surfaces of ${ \pmb { a } } , { \pmb { \beta } } , \dots , { \pmb { \gamma } }$ (egg-crate structure) plus a sense of circulation (orientation).

Applications:

a. In four dimensions (e.g.,spacetime) all O-forms, 1- forms,3-forms,and 4-forms are simple. A 2-form $\pmb { F }$ is generally a sum of two simple forms, e.g., $\pmb { F } =$ $- e d t \wedge d x + h d y \wedge d z$ it is simple if and only if $\pmb { F } \wedge \pmb { F } = 0$

b. A set of 1-forms ${ \pmb { a } } , { \pmb { \beta } } , \dots , { \pmb { \gamma } }$ is linearly dependent (one a linear combination of the others） if and only if

$$
\alpha \wedge \beta \wedge \dots \wedge \gamma = 0
$$

(egg crate collapsed).

# B. Exterior Derivative (applicable to any “differentiable manifold," with or without metric)

1. d produces a $( p + 1 )$ -form do from a $p$ -form $\pmb { \sigma }$

2. Effect of $\pmb { d }$ is defined by induction using the

Box 4.1 (continued)

(Chapter 2） definition of $\pmb { d f }$ and $f$ a function (0- form), plus

$$
\begin{array} { c } { { d ( \underline { { { \alpha } } } \wedge \underline { { { \beta } } } ) = d \alpha \wedge \beta + ( - 1 ) ^ { p } \alpha \wedge d \beta , } } \\ { { { } } } \\ { { d ^ { 2 } = d d = 0 . } } \end{array}
$$

Two applications

$$
d ( \alpha \wedge d \beta ) = d \alpha \wedge d \beta .
$$

For the $p$ -form $\pmb { \phi }$ ,with

$$
\phi = \phi _ { \mid i _ { 1 } . . . i _ { p } \mid } d x ^ { i _ { 1 } } \wedge . . . \wedge d x ^ { i _ { p } } ,
$$

one has (alternative and equivalent definition of $\pmb { d } \phi$ ）

$$
d \phi = d \phi _ { | i _ { 1 } . . . i _ { p } | } \wedge d x ^ { i _ { 1 } } \wedge \cdot \cdot \cdot \wedge d x ^ { i _ { p } } .
$$

# C. Integration (applicable to any “differentiable manifold," with or without metric)

# 1. Pictorial interpretation.

Text and pictures of Chapter 4 interpret $\scriptstyle \int \pmb { \alpha }$ (integral of specified l-form $\pmb { \alpha }$ along specified curve from specified starting point to specified end point) as “number of $\pmb { \alpha }$ -surfaces pierced on that route"; similarly, they interpret $\textstyle \int \phi$ (integral of specified 2-form $\pmb { \phi }$ over specified bit of surface on which there is an assigned sense of circulation or “orientation") as “number of cells of the honeycomb-like structure $\pmb { \phi }$ cut through by that surface”; similarly for the egg-crate-like structures that represent 3- forms; etc.

2. Computational rules for integration. To evaluate $\scriptstyle \int \pmb { \alpha }$ ,the integral of a $p$ -form

$$
\alpha = \alpha _ { | i _ { 1 } . . . i _ { p } | } ( x ^ { 1 } , . . . , x ^ { n } ) d x ^ { i _ { 1 } } \wedge . . . \wedge d x ^ { i _ { p } } ,
$$

over a $p$ -dimensional surface, proceed in two steps.

a. Substitute a parameterization of the surface,

$$
x ^ { k } ( \lambda ^ { 1 } , \ldots , \lambda ^ { p } )
$$

into $\pmb { \alpha }$ ,and collect terms in the form

$$
\alpha = a ( \lambda ^ { j } ) d \lambda ^ { 1 } \wedge . . . \wedge d \lambda ^ { p }
$$

(this is $\pmb { \alpha }$ viewed as a $\pmb { p }$ form in the $p$ -dimensional surface);

b. Integrate

$$
\int \alpha = \int a ( \lambda ^ { j } ) d \lambda ^ { 1 } d \lambda ^ { 2 } \dots d \lambda ^ { p }
$$

using elementary definition of integration.

Example: See equations (4.12) to (4.14).

3. The differential geometry of integration. Calculate $\scriptstyle \int \pmb { \alpha }$ for a $p$ -form $\pmb { \alpha }$ as follows.

a. Choose the $p$ -dimensional surface $\mathcal { S }$ over which to integrate.

b. Represent $s$ by a parametrization giving the generic point of the surface as a function of the parameters, $\mathcal { P } ( \lambda ^ { 1 } , \lambda ^ { 2 } , \dots \lambda ^ { p } )$ .This fixes the orientation. The same function with $\lambda ^ { 1 }  \lambda ^ { 2 }$ ， $\mathcal { P } ( \lambda ^ { 2 } , \lambda ^ { 1 } , \dots , \lambda ^ { p } )$ ,describes a different (i.e., oppositely oriented) surface, $- \mathcal { S } _ { }$

c. The infinitesimal parallelepiped

$$
\left( { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { 1 } } } A \lambda ^ { 1 } \right) \wedge \left( { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { 2 } } } A \lambda ^ { 2 } \right) \wedge \ \cdots \wedge \ \left( { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { p } } } A \lambda ^ { p } \right)
$$

is tangent to the surface. The number of cells of $\pmb { \alpha }$ it slices is

$$
\begin{array} { r } { \left. \alpha , \frac { \partial \mathcal { P } } { \partial \lambda ^ { 1 } } \wedge \ \cdot \ \cdot \ \wedge \ \frac { \partial \mathcal { P } } { \partial \lambda ^ { p } } \right. \ \varDelta \lambda ^ { 1 } \cdot \ . \ . \ \varDelta \lambda ^ { p } . } \end{array}
$$

This number changes sign if two of the vectors $\partial \mathcal { P } / \partial \lambda ^ { k }$ are interchanged, as for an oppositely oriented surface.

d. The above provides an interpretation motivating the definition

$$
\begin{array} { r } { \int \alpha \equiv \int \int \cdots \int \left. \alpha , \frac { \partial \mathcal { S } } { \partial \lambda ^ { 1 } } \wedge \frac { \partial \mathcal { S } } { \partial \lambda ^ { 2 } } \wedge \ \cdots \wedge \frac { \partial \mathcal { S } } { \partial \lambda ^ { p } } \right. } \\ { d \lambda ^ { 1 } d \lambda ^ { 2 } \ldots d \lambda ^ { p } . } \end{array}
$$

This definition is identified with the computational rule of the preceding section (C.2） in exercise 4.9.

Integrate a gradient df along a curve, $\mathcal { P } ( \lambda )$ from ${ \mathcal { P } } ( 0 )$ to ${ \mathcal { P } } ( 1 )$ ：

$$
\begin{array} { l } { { \displaystyle { \int } d f = \int _ { 0 } ^ { 1 } \langle d f , d \phi ^ { \rho } / d \lambda \rangle d \lambda = \int _ { \cdot } ^ { 1 } \left( d f / d \lambda \right) d \lambda } } \\ { { \displaystyle ~ = f [ \mathcal { O } ( 1 ) ] - f [ \mathcal { P } ( 0 ) ] . } } \end{array}
$$

e. Three different uses for symbol “d': First, lightface $d$ in explicit derivative expressions such as

# Box 4.1 (continued)

$d / d a$ ,or $d f / d a$ or $d \tilde { \mathscr { P } } / d a$ .neither numerator nor denominator alone has any meaning, but only the full string of symbols.Second, lightface $d$ inside an integral sign; e.g., Sfda. This is an instruction to perform integration,and has no meaning whatsoever without an integral sign; $^ { * 6 } \mathrm { f } \ldots d . \ldots ^ { 3 }$ ’ lives as an indivisible unit. Third, sans-serif $\pmb { d }$ e.g., $\pmb { d }$ alone, or $d f ,$ or da. This is an exterior derivative,which converts a $p$ -form into a $( p + 1 )$ -form. Sometimes lightface $^ { d }$ is used for the same purpose. Hence, $^ { d }$ alone, or $d f ,$ or $d x$ ,is always an exterior derivative unless coupled to an $\textstyle \int$ sign (second use),or coupled to a / sign (first use).

4. The generalized Stokes theorem (see Box 4.6).

a. Let $\partial \mathcal { V }$ be the closed $p$ -dimensional boundary of a $( p + 1 )$ -dimensional surface $\mathcal { V }$ Let $\pmb { \sigma }$ be a $p$ -form defined throughout $\mathcal { V }$

Then

$$
\boxed { \int _ { \mathcal { T } ^ { \prime } } d \sigma = \int _ { \partial \mathcal { V } } \sigma }
$$

[integral of $p$ -form $\pmb { \sigma }$ over boundary $\partial \mathcal { V }$ equals integral of $( p + 1 )$ -form dg over interior $\mathcal { V } ]$ b. For the sign to come out right, orientations of $\mathcal { V }$ and $\partial \mathcal { V }$ must agree in this sense: choose coordinates $y ^ { 0 } , y ^ { 1 } , \ldots , y ^ { p }$ on a portion of $\mathcal { V }$ ， with $y ^ { 0 }$ specialized so $y ^ { 0 } \leq 0$ in $\mathcal { V }$ and $y ^ { 0 } = 0$ at the boundary $\partial \mathcal { V }$ ； then the orientation

$$
\frac { \partial \mathcal { P } } { \partial y ^ { 0 } } \wedge \frac { \partial \mathcal { P } } { \partial y ^ { 1 } } \wedge ~ . ~ . ~ . ~ \wedge \frac { \partial \mathcal { P } } { \partial y ^ { p } }
$$

for $\mathcal { V }$ demands the orientation

$$
{ \frac { \partial { \mathcal { P } } } { \partial y ^ { 1 } } } \wedge \dots \wedge { \frac { \partial { \mathcal { P } } } { \partial y ^ { p } } }
$$

for $\partial \mathcal { V }$

c. Note: For a nonorientable surface,such as a Mobius strip, where a consistent and continuous choice of orientation is impossible, more intricate mathematics is required to give a definition of $" \partial ^ { , }$ for which the Stokes theorem holds.

Applications: Includes as special cases all integral theorems for surfaces of arbitrary dimension in spaces of arbitrary dimension, with or without metric, generalizing all versions of theorems of Stokes and Gauss. Examples:

a. $\mathcal { V }$ a curve, $\partial \mathcal { V }$ its endpoints, ${ \pmb \sigma } = f$ a 0-form (function):

$$
\int _ { \mathcal { V } } \ d f = \int _ { 0 } ^ { 1 } \left( d f / d \lambda \right) d \lambda = \int _ { \partial \mathcal { V } } f = f ( 1 ) - f ( 0 ) .
$$

b. $\mathcal { V }$ a 2-surface in 3-space, $\partial \mathcal { V }$ its closed-curve boundary, $\pmb { \nu }$ a l-form; translated into Euclidean vector notation, the two integrals are

$$
\int _ { \mathcal { V } } \ d \pmb { v } = \int _ { \mathcal { V } } \ ( \pmb { \nabla } \times \pmb { \nu } ) \cdot d \pmb { S } ; \int _ { \partial \mathcal { V } } \pmb { v } = \int _ { \partial \mathcal { V } } \pmb { \nu } \cdot d \pmb { l } .
$$

c. Other applications in $\ S \ S .$ ,20.2,20.3，20.5，and exercises 4.10,4.11, 5.2,and below.

D. Algebra I (applicable to any vector space with metric)

1. Norm of a p-form.

$$
\begin{array} { r } { | | \pmb { \alpha } | | ^ { 2 } \equiv \alpha _ { | i _ { 1 } . . . i _ { p } | } \alpha ^ { i _ { 1 } . . . i _ { p } } . } \end{array}
$$

Two applications: Norm of a 1-form equals its squared length, $| | { \pmb { \alpha } } | | ^ { 2 } = { \pmb { \alpha } } \cdot { \pmb { \alpha } }$ Norm of electromagnetic 2-form Or Faraday: $\| \pmb { F } | ^ { 2 } = B ^ { 2 } - E ^ { 2 }$

2. Dual of a p-form.

a. In an $\pmb { n }$ -dimensional space, the dual of a $p$ -form $\pmb { \alpha }$ is the $( n - p )$ -form $^ * { \pmb { \alpha } }$ ，with components

$$
( ^ { \ast } \alpha ) _ { k _ { 1 } \ldots k _ { n - p } } = \alpha ^  \{ i _ { 1 } \ldots i _ { p } \ : \epsilon _ { i _ { 1 } \ldots i _ { p } k _ { 1 } \ldots k _ { n - p } } .
$$

b. Properties of duals:

$$
{ \begin{array} { r l } & { * * \alpha = ( - 1 ) ^ { p - 1 } \alpha { \mathrm { ~ i n ~ } } \mathfrak { s p a c e t i m e } ; } \\ & { \alpha \wedge { ^ * \alpha } = | | \alpha | | ^ { 2 } \varepsilon { \mathrm { ~ i n ~ g e n e r a l } } . } \end{array} }
$$

c. Note: the definition of $\pmb { \varepsilon }$ (exercise 3.13) entails choosing an orientation of the space,i.e.,deciding which orthonormal bases (l） are“righthanded"and thus (2) have $\pmb { \varepsilon } ( \pmb { e } _ { 1 } , \ldots , \pmb { e } _ { n } ) = + 1$

Applications

a. For $f$ a 0-form, $\mathbf { \nabla } ^ { * } f = f \bar { \pmb \varepsilon }$ and $\begin{array} { r } { \mathcal { f } f d ( \mathrm { v o l u m e } ) = \mathcal { f } ^ { * } f . } \end{array}$ b. Dual of charge-current 1-form J is charge-current 3-form $^ { * } J$ The total charge $Q$ in a 3-dimensional hypersurface region $s$ is

$$
Q ( \mathcal { S } ) = \int _ { \mathcal { S } } \mathbf { \Psi } ^ { * } \mathbf { J } .
$$

Conservation of charge is stated locally by ${ \pmb d } ^ { * } { \pmb J } = 0$ Stokes' Theorem goes from this differential conservation law to the integral conservation law,

$$
0 = \int _ { \mathcal { V } } \mathbf { \nabla } d ^ { * } \mathbf { J } = \int _ { \partial \mathcal { T } } \mathbf { \nabla } ^ { * } \mathbf { J } .
$$

This law is of most interest when $\partial ^ { \aa } \mathcal { V } = \mathcal { S } _ { 2 } - \mathcal { S } _ { 1 }$ consists of the future $\mathcal { S } _ { 2 }$ and past $\mathcal { S } _ { 1 }$ boundaries of a spacetime region, in which case it states $Q ( \mathcal { S } _ { 2 } ) =$ $\boldsymbol { Q } ( \mathcal { S } _ { 1 } )$ ； see exercise 5.2.

c. Dual of electromagnetic field tensor $\pmb { F } =$ Faraday is ${ \pmb F } =$ Maxwell. From the ${ d ^ { * } } F = 4 \pi ^ { * } J$ Maxwell equation, find $\begin{array} { r } { 4 \pi Q = 4 \pi \int _ { \mathcal { S } } \ast \pmb { J } = \int _ { \mathcal { S } } \pmb { d } ^ { \ast } \pmb { F } = \int _ { \partial \mathcal { S } } \ast \pmb { F } . } \end{array}$

3.Simple forms revisited.

a. The dual of a simple form is simple.

b. Egg crate of $^ * { \pmb { \sigma } }$ is perpendicular to egg crate of $\pmb { \sigma } = \pmb { \alpha } \wedge \pmb { \beta } \wedge \dots \wedge \pmb { \mu }$ in this sense:

(l） pick any vector $\pmb { \nu }$ lying in intersection of surfaces of $\pmb { \sigma }$

$$
( \langle \alpha , V \rangle = \langle \beta , V \rangle = \dots = \langle \mu , V \rangle = 0 ) ;
$$

(2） pick any vector W lying in intersection ofsurfaces of ${ \ast } _ { \sigma }$ ；

(3）then $v$ and $\pmb { w }$ are necessarily perpendicular: $\pmb { V } \cdot \pmb { W } = 0$

Example: $\sigma = 3 \mathrm { ~ } d t$ is a simple l-form in spacetime.

a. ${ } ^ { * } \sigma = - 3 \ d x \ \wedge$ dy $\wedge$ dz is a simple 3-form.

b. General vector in surfaces of $\pmb { \sigma }$ is

$$
\pmb { \nu } = V ^ { x } \pmb { e } _ { x } + V ^ { y } \pmb { e } _ { y } + V ^ { z } \pmb { e } _ { z } .
$$

c. General vector in intersection of surfaces of ${ \ast } _ { \sigma }$ is

$$
\pmb { W } = \pmb { W } ^ { t } \pmb { e } _ { t } .
$$

# \$4.2. ELECTROMAGNETIC 2-FORM AND LORENTZ FORCE

The electromagnetic field tensor, Faraday $= F ,$ is an antisymmetric second-rank tensor (i.e.,2-form). Instead of expanding it in terms of the tensor products of basis 1-forms,

$$
{ \cal F } = { \cal F } _ { \alpha \beta } d x ^ { \alpha } \otimes d x ^ { \beta } ,
$$

the exterior calculus prefers to expand in terms of antisymmetrized tensor products ("exterior products,” exercise 4.1):

$$
{ \pmb F } = \frac { 1 } { 2 } F _ { \alpha \beta } { \pmb d } x ^ { \alpha } \wedge { \pmb d } x ^ { \beta } ,
$$

$$
d x ^ { \alpha } \wedge d x ^ { \beta } \equiv d x ^ { \alpha } \otimes d x ^ { \beta } - d x ^ { \beta } \otimes d x ^ { \alpha } .
$$

Electromagnetic 2-form expressed in terms of exterior products

Any 2-form (antisymmetric, second-rank tensor) can be so expanded. The symbol $^ { 6 6 } { \wedge } ^ { 5 9 }$ is variously called a“wedge,”a “hat,” or an “exterior product sign”； and $d x ^ { \alpha } \wedge d x ^ { \beta }$ are the“basis 2-forms”of a given Lorentz frame (see $\ S 3 . 5$ ,exercise 3.12, and Box 4.1).

There is no simpler way to illustrate this 2-form representation of the electromagnetic field than to consider a magnetic field in the $x$ -direction:

$$
\begin{array} { r } { F _ { y z } = - F _ { z y } = B _ { x } , } \\ { F = B _ { z } \pmb { d } \gamma \wedge \pmb { d } z . } \end{array}
$$

The 1-form ${ \pmb d \gamma } = \pmb { \mathrm { g r a d } } _ { \mathcal { Y } }$ is the set of surfaces (actually hypersurfaces) $y = 1 8$ (all $t , x , z ) , y = 1 9 ( { \mathrm { a l l } } t , x , z ) , y = 2 0 ( { \mathrm { a l l } } t , x , z ) ,$ , etc.; and surfaces uniformly interpolated between them. Similarly for the 1-form $\pmb { d z }$ .The intersection between these two sets of surfaces produces a honeycomb-like structure.That structure becomes a $^ { \mathfrak { s o } }$ -form” when it is supplemented by instructions (see arrows in Figure 4.l) that give a“sense of circulation” to each tube of the honeycomb (order of factors in the “wedge product” of equation 4.2;dy ^ $d z = - d z \wedge d y )$ .The 2-form $\pmb { F }$ in the example differs from this “basis 2-form”dy ^ $\pmb { d } z$ only in this respect, that where dy ^ dz had one tube, the field 2-form has $B _ { \varepsilon }$ tubes.

When one considers a tubular structure that twists and turns on its way through spacetime.one must have more components to describe it.The 2-form for the general electromagnetic field can be written as

$$
\begin{array} { l } { { F = E _ { x } d x \wedge d t + E _ { y } d y \wedge d t + E _ { z } d z \wedge d t + B _ { x } d y \wedge d z } } \\ { { \qquad + \ B _ { y } d z \wedge d x + B _ { z } d x \wedge d y } } \end{array}
$$

A 2-form as a honeycomb of tubes with a sense of circulation

(6 components,6 basis 2-forms).

A l-form is a machine to produce a number out of a vector (bongs of a bell as the vector pierces successive surfaces).A 2-form is a machine to produce a number out of an oriented surface (surface with a sense of circulation indicated on it: Figure 4.1, lower right). The meaning is as clear here as it is in elementary magnetism:

A 2-form as a machine to produce a number out of an oriented surface

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/503975ddcde280194f7bb6fbfaa0c926fec5ec3b1fdd447428fa87a16385b51f.jpg)  
Figure 4.1. Construction of the 2-form for the electromagnetic field $F = B _ { z } d y \wedge d z$ out of the l-forms dy and $\pmb { d z }$ by“wedge multiplication”(formation of honeycomb-like structure with sense of circulation indicated by arrows),A 2-form is a“machine to construct a number out of an oriented surface”(illustrated by sample surface enclosed by arrows at lower right;number of tubes intersected by this surface is

$$
\int _ { \mathrm { ( t h i s s u r f a c e ) } } { \overline { { F } } } = 1 8 ; \qquad \quad \cdots \quad -
$$

Faraday's concept of“magnetic flux").This idea of 2-form machinery can be connected to the“tensoras-machine”idea of Chapter 3 as follows.The shape of the oriented surface over which one integrates $\pmb { F }$ does not matter, for small surfaces.All that affects $\textstyle \int F$ is the area of the surface,and its orientation. Choose two vectors, $\pmb { u }$ and ${ \pmb v } _ { \pmb { \imath } }$ that lie in the surface. They form two legs of a parallelogram,whose orientation $\omega$ followed by $\pmb { \nu }$ and area are embodied in the exterior product u $\wedge \ v$ Adjust the lengths of $\pmb { u }$ and $\pmb { \nu }$ so their parallelogram, ${ \pmb u } \wedge { \pmb v } ,$ has the same area as the surface of integration. Then

F=SF=F(u, machinery idea [machinery idea of.this chapter Lof Chapter 3

Exercise:derive this result,for an infinitesimal surface u^ ${ \pmb v }$ and for general $\pmb { F } ,$ using the formalism of Box 4.1.

the number of Faraday tubes cut by that surface. The electromagnetic 2-form $\pmb { F }$ or Faraday described by such a“tubular structure”(suitably abstracted; Box 4.2) has a reality and a location in space that is independent of all coordinate systems and all artificial distinctions between “electric” and “magnetic” fields. Moreover, those tubes provide the most direct geometric representation that anyone has ever been able to give for the machinery by which the electromagnetic field acts on a charged particle. Take a particle of charge $^ e$ and 4-velocity

$$
\pmb { \mu } = \frac { d x ^ { \alpha } } { d \tau } \pmb { e } _ { \alpha } .
$$

Let this particle go through a region where the electromagnetic field is described by the 2-form

$$
F = B _ { x } d y \wedge d z
$$

of Figure 4.1. Then the force exerted on the particle (regarded as a l-form) is the contraction of this 2-form with the 4-velocity (and the charge);

Lorentz force as contraction of electromagnetic 2-form with particle's 4-velocity

$$
\pmb { \dot { p } } = d \pmb { p } / d \tau = e \pmb { F } ( \pmb { u } ) \equiv e \langle \pmb { F } , \pmb { u } \rangle ,
$$

as one sees by direct evaluation, letting the two factors in the 2-form act in turn on the tangent vector ${ \pmb u }$ ：

$$
\begin{array} { r l } & { \pmb { \dot { p } } = e B _ { x } \langle \pmb { d } y \wedge \pmb { d } z , \pmb { u } \rangle } \\ & { \quad = e B _ { x } \{ \pmb { d } y \langle \pmb { d } z , \pmb { u } \rangle - \pmb { d } z \langle \pmb { d } y , \pmb { u } \rangle \} } \\ & { \quad = e B _ { x } \{ \pmb { d } y \langle \pmb { d } z , \pmb { u } ^ { z } \pmb { e } _ { z } \rangle - \pmb { d } z \langle \pmb { d } y , \pmb { u } ^ { y } \pmb { e } _ { y } \rangle \} } \end{array}
$$

or

$$
{ \dot { p } } _ { \alpha } d x ^ { \alpha } = e B _ { x } u ^ { z } d y - e B _ { x } u ^ { y } d z .
$$

Comparing coeffcients of the separate basis l-forms on the two sides of this equa-tion, one sees reproduced allthe detail of the Lorentz force exerted by the magnetic field $B _ { x }$

$$
\begin{array} { l } { \displaystyle { \dot { p } _ { y } = \frac { d p _ { y } } { d \tau } = e B _ { x } \frac { d z } { d \tau } , } } \\ { \displaystyle { \dot { p } _ { z } = \frac { d p _ { z } } { d \tau } = - e B _ { x } \frac { d y } { d \tau } . } } \end{array}
$$

By simple extension of this line of reasoning to the general electromagnetic field, one concludes thatthe time-rate ofchange ofmomentum(1-form)is equal to the charge multiplied by the contraction of the Faraday with the 4-velocity.Figure 4.2 illustrates pictorially how the 2-form, $\pmb { F } ,$ serves as a machine to produce the l-form, $\pmb { \dot { p } }$ ,out of the tangent vector, eu.

# BoX 4.2 ABSTRACTING A 2-FORM FROM THE CONCEPT OF ‘HONEYCOMB-LIKE STRUCTURE." IN 3-SPACE AND IN SPACETIME

Open up a cardboard carton containing a dozen bottles,and observe the honeycomb structure of intersecting north-south and east-west cardboard separators between the bottles. That honeycomb structure of “tubes”("channels for bottles"） is a fairly apt illustration of a 2-form in the context of everyday 3-space.It yields a number (number of tubes cut) for each choice of smooth element of 2-surface slicing through the three-dimensional structure. However, the intersecting cardboard separators are rather too specific. All that a true 2-form can ever give is the number of tubes sliced through, not the “shape”of the tubes. Slew the carton around on the floor by $4 5 ^ { \circ }$ . Then half the separators run NW-SE and the other half run NE-SW,but through a given bit of 2-surface fixed in 3-space the count of tubes is unchanged. Therefore,one should be careful to make the concept of tubes in the mind's eye abstract enough that one envisages direction of tubes (vertical in the example) and density of tubes,but not any specific location or orientation for the tube walls.Thus all the following representations give one and the same 2-form, $\pmb { \sigma }$ ：

$$
\begin{array} { l } { { \pmb \sigma = B \pmb d x \wedge \pmb d y ; } } \\ { { \pmb \sigma = B ( 2 \pmb d x ) \wedge \left( \frac { 1 } { 2 } \pmb d y \right) } } \end{array}
$$

(NS cardboards spaced twice as close as before;   
EW cardboards spaced twice as wide as before);

$$
\sigma = B \ : d \left( { \frac { x - y } { \sqrt { 2 } } } \right) \wedge d \left( { \frac { x + y } { \sqrt { 2 } } } \right)
$$

(cardboards rotated through $4 5 ^ { \circ }$ ）；

$$
\pmb { \sigma } = B \frac { \alpha \pmb { d } x + \beta \pmb { d } y } { ( \alpha \delta - \beta \gamma ) ^ { 1 / 2 } } \wedge \frac { \gamma \pmb { d } x + \delta \pmb { d } y } { ( \alpha \delta - \beta \gamma ) ^ { 1 / 2 } }
$$

(both orientation and spacing of“cardboards” changing from point to point,with all four

functions, $\alpha , \beta , \gamma ,$ ,and δ,depending on position).

What has physical reality,and constitutes the real geometric object, is not any one of the l-forms just encountered individually, but only the 2-form $\pmb { \sigma }$ itself.This circumstance helps to explain why in the physical literature one sometimes refers to “tubes of force”and sometimes to “lines of force." The two terms for the same structure have this in common, that each yields a number when sliced by a bit of surface. The line-of-force picture has the advantage of not imposing on the mind any specific structure of “sheets of cardboard"; that is, any specifc decomposition of the 2-form into the product of l-forms. However, that very feature is also a disadvantage, for in a calculation one often finds it useful'to have a well-defined representation of the2-form as the wedge product of l-forms. Moreover, the tube picture,abstract though it must be if it is to be truthful, also has this advantage, that the orientation of the elementary tubes (sense of circulation as indicated by arrows in Figures 4.l and 4.5, for example) lends itself to ready visualization.Let the “walls” of the tubes therefore remain in all pictures drawn in this book as a reminder that 2-forms can be built out of 1-forms;but let it be understood here and hereafter how manyfold are the options for the individual l-forms!

Turn now from three dimensions to four, and find that the concept of “honeycomb-like structure” must be made still more abstract. In three dimensions the arbitrariness of the decomposition of the 2-form into l-forms showed in the slant and packing of the “cardboards,”but had no effect on the verticality,of the “channels for the bottles” ("direction of Faraday lines of force or tubes of force"); not so in four dimensions,or at least not in the generic case in four dimensions.

In special cases, the story is almost as simple in four dimensions as in three. An example of a special case is once again the 2-form ${ \pmb \sigma } = B { \pmb d } { \pmb x }$ ^ dy,with all the options for decomposition into l-forms that have already been mentioned, but with every option giving the same “direction” for the tubes.If the word “direction” now rises in status from “tube walls unpierced by motion in the direction of increasing $z ^ { \dag }$ to “tube walls unpierced either by motion in the direction of increasing $z$ ，or by motion in the direction of increasing t,or by any linear combination of such motions,” that is a natural enough consequence of adding the new dimension.Moreover, the same simplicity prevails for an electromagnetic plane wave.For example,let the wave be advancing in the $z$ -direction,and let the electric polarization point in the $x$ -direction; then for a monochromatic wave,one has

$$
E _ { x } = B _ { y } = E _ { 0 } \cos \omega ( z \mathrm { ~ . ~ . ~ } t ) = - F _ { 0 1 } = F _ { 3 1 } ,
$$

and all components distinct from these equal zero. Faraday is

$$
\begin{array} { r l r } {  { \pmb { F } = F _ { 0 1 } \pmb { d t } \wedge \pmb { d x } + F _ { 3 1 } \pmb { d z } \wedge \pmb { d x } } } \\ & { } & { = E _ { 0 } \cos \omega ( z - t ) \pmb { d ( z - t ) } \wedge \pmb { d x } , } \end{array}
$$

which is again representable as a single wedge product of two l-forms.

Not so in general! The general 2-form in four dimensions consists of six distinct wedge products,

$$
\begin{array} { r } { \pmb { F } = F _ { 0 1 } \pmb { d t } \wedge \pmb { d x } + F _ { 0 2 } \pmb { d t } \wedge \pmb { d y } + \cdot \cdot \cdot } \\ { + F _ { 2 3 } \pmb { d y } \wedge \pmb { d z } . } \end{array}
$$

It is too much to hope that this expression will reduce in the generic case to a single wedge product of two l-forms ("simple"2-form). It is not even

true that it will. It is only remarkable that it can be reduced from six exterior products to two (details in exercise 4.1); thus,

$$
{ \pmb F } = { \pmb \eta } ^ { 1 } \wedge { \pmb \xi } ^ { 1 } + { \pmb \eta } ^ { 2 } \wedge { \pmb \xi } ^ { 2 } .
$$

Each product $\pmb { \eta } ^ { i } \wedge \pmb { \xi } ^ { i }$ individually can be visualized as a honeycomb-like structure like those depicted in Figures 4.1, 4.2,4.4,and 4.5. Each such structure individually can be pictured as built out of intersecting sheets (l-forms), but with such details as the tilt and packing of these l-forms abstracted away. Each such structure individually gives a number when sliced by an element of surface. What counts for the 2-form $\pmb { F } ,$ however, is neither the number of tubes of ${ \pmb { \eta } } ^ { 1 } \wedge { \pmb \xi } ^ { 1 }$ cut by the surface, nor the number of tubes of $\pmb { \eta } ^ { 2 } \wedge \bar { \xi } ^ { 2 }$ cut by the surface, but only the sum of the two. This sum is what is referred to in the text as the “number of tubes of $\pmb { F } ^ { \ast }$ cut by the surface. The contribution of either wedge product individually is not well-defined, for a simple reason: the decomposition of a six-wedge-product object into two wedge products, miraculous though it seems, is actually far from unique (details in exercise 4.2).

In keeping with the need to have two products of l-forms to represent the general 2-form note that the vanishing of $\pmb { d } \pmb { F }$ ("no magnetic charges") does not automatically imply that $d ( \pmb { \eta } ^ { 1 } \wedge \pmb { \xi } ^ { 1 } )$ or $d ( \pmb { \eta } ^ { 2 } \land \pmb { \xi } ^ { 2 } )$ separately vanish. Note also that any spacelike slice through the general 2-form $\pmb { F }$ (reduction from four dimensions to three) can always be represented in terms of a honeycomb-like structure ("simple”2-form in three dimensions; Faraday's picture of magnetic tubes of force).

Despite the abstraction that has gone on in seeing in all generality what a 2-form is, there is no bar to continuing to use the term“honeycomb-like structure”in a broadened sense to describe this object; and that is the practice here and hereafter.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/3f55682e01f2c80c4af3487f0b3b0f30fd8c7440d81e8a10c56f4427003e857b.jpg)  
Figure 4.2. The Faraday or 2-form $\pmb { F }$ of the electromagnetic fleld is a machine to produce a l-form (the time-rate of change of momentum $\pmb { \dot { \rho } }$ of a charged particle) out of a tangent vector (product of charge $^ e$ of the particle and its 4-velocity u). In spacetime the general 2-form is the “superposition” (see Box 4.2) of two structures like that ilustrated at the topof this diagram,the tubes of the first being tilted and packed as indicated,the tubes of the second being tilted in another direction and having a different packing density.

# $\ S 4 . 3$ .FORMS ILLUMINATE ELECTROMAGNETISM,AND ELECTROMAGNETISM ILLUMINATES FORMS

All electromagnetism allows itself to be summarized in the language of 2-forms, honeycomb-like“structures”(again in the abstract sense of “structure”of Box 4.2) of tubes filling all spacetime,as well when spacetime is curved as when it is flat. In brief, there are two such structures,one Faraday $= { \pmb { F } } ,$ the other Maxwell $= ^ { * } { \pmb { F } } ,$ each dual ("perpendicular,”the only place where metric need enter the discussion) to the other,each satisfying an elementary equation:

$$
\pmb { d } \pmb { F } = 0
$$

("no tubes of Faraday ever end") and

$$
{ d ^ { * } F } = 4 \pi ^ { * } J
$$

("the number of tubes of Maxwell that end in an elementary volume is equal to the amount of electric charge in that volume"). To see in more detail how this machinery shows up in action,look in turn at: (l) the definition of a 2-form; (2) the appearance of a given electromagnetic field as Faraday and as Maxwell; (3) the Maxwell structure for a point-charge at rest; (4) the same for a point-charge in motion; (5)the nature of the field of a charge that moves uniformly except during a brief instant of acceleration; (6) the Faraday structure for the field of an oscillating dipole; (7) the concept of exterior derivative; (8) Maxwel's equations in the language of forms; and (9) the solution of Maxwell's equations in flat spacetime, using a 1-form $\pmb { A }$ from which the Liénard-Wiechert 2-form $\pmb { F }$ can be calculated via ${ \pmb F } = \pmb { d A }$

Preview of key points in electromagnetism

A 2-form,as illustrated in Figure 4.l, is a machine to construct a number (net number of tubes cut") out of any “oriented 2-surface”(2-surface with “sense of circulation” marked on it):

A 2-form as machine for number of tubes cut

$$
\left( \begin{array} { l } { \mathrm { n u m b e r } } \\ { \mathrm { o f ~ t u b e s } } \\ { \mathrm { c u t } } \end{array} \right) = \int _ { \mathrm { s u r f a c e } } \pmb { F } .
$$

For example,let the 2-form be the one ilustrated in Figure 4.1

$$
{ \pmb F } = B _ { x } \pmb d y \wedge \pmb d z ,
$$

Number of tubes cut calculated in one example

and let the surface of integration be the portion of the surface of the 2-sphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = a ^ { 2 }$ ， $t =$ constant, bounded between $\theta = 7 0 ^ { \circ }$ and $\theta = 1 1 0 ^ { \circ }$ and between $\varphi = 0 ^ { \circ }$ and $\varphi = 9 0 ^ { \circ }$ ("Atlantic region of the tropics"). Write

$$
\begin{array} { c } { y = a \sin \theta \sin \varphi , } \\ { z = a \cos \theta , } \\ { { \pmb { d \gamma } = a ( \cos \theta \sin \varphi d \theta + \sin \theta \cos \varphi d \varphi ) , } } \\ { { \pmb { d z } = - a \sin \theta d \pmb { d \theta } , } } \\ { { \pmb { d \gamma } \wedge { \pmb { d z } = a ^ { 2 } \sin ^ { 2 } \theta \cos \varphi d \theta \wedge d \varphi . } } } \end{array}
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/26161009f3d9fbf0fafb06034d764bf49997adce8992a61501eb9c1b46d114f2.jpg)  
Figure 4.3. Spacelike slices through Faraday,the electromagnetic 2-form,a geometric object, a honeycombof tubes that pervades allspacetime ("honeycomb”in the abstract sense spelled out more precisely in $\mathtt { B o x } 4 . 2$ ). The surfaces inthe drawingdo not look likea2-form (honeycomb),because the second familyof surfaces making up the honeycomb extends in the spatial direction that is suppressd from the drawing. Diagram

A shows one spacelike slice through the 2-form (time increases upwards in the diagram).In diagram B,a projection of the 2-form on this spacelike hypersurface gives the Faraday tubes of magnetic force inthis three-dimensional geometry (if the suppressed dimension were restored,the tubes would be tubes, not channels between lines). Diagram C shows another spacelike slice (hypersurface of simultaneity for an observer in a different Lorentz frame). Diagram D shows the very different pattern of magnetic tubes in this reference system. The demand that magnetic tubes of force shall not end $( \nabla \cdot \pmb { \cal B } = 0 )$ ,repeated over and over for every spacelike slice through Faraday,gives everywhere the result $\hat { \boldsymbol { \mathrm { o } } } \pmb { { \cal B } } / \hat { \eta } t = - \bar { \boldsymbol { \nabla } } \times \pmb { { \cal E } }$ Thus (magnetostatics) $^ +$ (covariance) (magnetodynamics). Similarly--see Chapters 17 and 21- (geometrostatics) $^ +$ (covariance) $\twoheadrightarrow$ (geometrodynamics).

The structure $d \theta \wedge d \theta$ looks like a “collapsed egg-crate”(Figure l.4, upper right) and has zero content, a fact formally evident from the vanishing of $\alpha \wedge \beta =$ $- \beta \wedge \alpha$ when $\pmb { \alpha }$ and $\pmb { \beta }$ are identical. The result of the integration,assuming constant $B _ { x } ,$ is

$$
\int _ { _ \mathrm { \small s u r f a c e } } { \pmb { F } } = a ^ { 2 } B _ { x } \int _ { _ { 7 0 ^ { \circ } } } ^ { 1 1 0 ^ { \circ } } \sin ^ { 2 } \theta d \theta \int _ { _ { 0 ^ { \circ } } } ^ { 9 0 ^ { \circ } } \cos \varphi d \varphi
$$

It is not so easy to visualize a pure electric field by means of its 2-form $\pmb { F }$ (Figure 4.4,left) as it is to visualize a pure magnetic field by means of its 2-form $\pmb { F }$ (Figures 4.1,4.2, 4.3). Is there not some way to treat the two fields on more nearly the same footing? Yes,construct the 2-form $\ast _ { F }$ (Figure 4.4,right) that is dual ("perpendicular"; Box 4.3；exercise 3.14) to $\pmb { F } .$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/574b356ca8f0536af433616f9dee9809e23ec68bc758f809d33b27245afcca99.jpg)  
Figure 4.4. The Faraday structure

$$
{ \cal F } = \frac { 1 } { 2 } F _ { \mu \nu } \ d x ^ { \mu } \wedge \ d x ^ { \nu } = \frac { 1 } { 2 } F _ { 0 1 } d t \wedge \ d x + \frac { 1 } { 2 } F _ { 1 0 } d x \wedge \ d t = E _ { x } d x \wedge \ d t
$$

associated with an electric field in the $_ { x }$ -direction,and the dual("perpendicular") Maxwel honeycomblike 2-form

$$
\mathbf { \ { * } } F = { \frac { 1 } { 2 } } * F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } = { ^ { \circ } F } _ { 2 3 } d x ^ { 2 } \wedge d x ^ { 3 } = F ^ { 0 1 } d x ^ { 2 } \wedge d x ^ { 3 } = F _ { 1 0 } d x ^ { 2 } \wedge d x ^ { 3 } = E _ { x } d y \wedge d z .
$$

Represent in geometric form the field of a point-charge of strength $e$ at rest at the origin. Operate in flat space with spherical polar coordinates:

$$
\begin{array} { c } { { d s ^ { 2 } = . - d \tau ^ { 2 } = g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } } } \\ { { = - d t ^ { 2 } + d r ^ { 2 } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \varphi ^ { 2 } . } } \end{array}
$$

The electric field in the $r .$ direction being $E _ { r } = e / r ^ { 2 }$ ,it follows that the 2-form $\pmb { F }$ Or Faraday is

$$
F = \frac { 1 } { 2 } F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } = - E _ { r } d t \wedge d r = - \frac { e } { r ^ { 2 } } d t \wedge d r .
$$

Its dual, according to the prescription in exercise 3.14, is Maxwell:

Pattern of tubes in dual structure Mexwell for point-charge at rest

$$
M a x w e I I = { ^ { * } F } = e \sin \theta d \theta \wedge d \varphi ,
$$

as illustrated in Figure 4.5.

Take a tour in the positive sense around a region of the surface of the sphere illustrated in Figure 4.5. The number of tubes of $\ast _ { F }$ encompassed in the route will be precisely

$$
{ \binom { \mathrm { n u m b e r } } { \mathrm { o f ~ t u b e s } } } = e { \binom { \mathrm { s o l i d } } { \mathrm { a n g l e } } } .
$$

The whole number of tubes of $\ast _ { F }$ emergent over the entire sphere will be $ 4 \pi e .$ in conformity with Faraday's picture of tubes of force.

# Box 4.3 DUALITY OF 2-FORMS IN SPACETIME

Given a general 2-form (containing six exterior or wedge products)

$$
\pmb { F } = E _ { x } \pmb { d } x \wedge \pmb { d } t + E _ { y } \pmb { d } y \wedge \pmb { d } t + \cdot \cdot \cdot + B _ { z } \pmb { d } x \wedge \pmb { d } y ,
$$

one gets to its dual ("perpendicular") by the prescription

$$
{ } ^ { * } F = - B _ { x } d x \wedge d t - \cdot \cdot \cdot + E _ { y } d z \wedge d x + E _ { z } d x \wedge d y .
$$

# Duality Rotations

Note that the dual of the dual is the negative of the original 2-form; thus

$$
{ } ^ { * * } F = - E _ { x } d x \wedge d t - \cdot \cdot \cdot - B _ { z } d x \wedge d y = - F .
$$

In this sense \* has the same property as the imaginary number $i ; \ * *  = i i = - 1$ Thus one can write

$$
e ^ { * \alpha } = \cos \alpha + { } ^ { * } \sin \alpha .
$$

This operation, applied to $\pmb { F } ,$ carries attention from the generic 2-form in its simplest representation (see exercise 4.1)

$$
\pmb { F } = E _ { x } \pmb { d } x \wedge \pmb { d } t + B _ { x } \pmb { d } y \wedge \pmb { d } z
$$

to another“duality rotated electromagnetic feld"

$$
e ^ { * \alpha } F = ( E _ { x } \cos \alpha - B _ { x } \sin \alpha ) d x \wedge d t + ( B _ { x } \cos \alpha + E _ { x } \sin \alpha ) d y \wedge d z .
$$

If the original field satisfied Maxwel's empty-space field equations,so does the new field.With suitable choice of the “complexion” $\pmb { \alpha }$ , one can annul one of the two wedge products at any chosen point in spacetime and have for the other

$$
( B _ { x } { } ^ { 2 } + E _ { x } { } ^ { 2 } ) ^ { 1 / 2 } d y \wedge d z .
$$

Field of a point-charge in motion

How can one determine the structure of tubes associated with a charged particle moving at a uniform velocity? First express $\yen 5$ in rectangular coordinates moving with the particle (barred coordinates in this comoving “rocket” frame of reference; unbarred coordinates will be used later for a laboratory frame of reference). The relevant steps can be listed:

$$
{ } ^ { * } F = e \sin \bar { \theta } d \bar { \theta } \wedge d \overline { { \varphi } } = - e ( d \cos \bar { \theta } ) \wedge d \overline { { \varphi } } ;
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/6ded1404acf9edcfdd001d4faace4d03e76b5ca5a9e4ab16185c4cbb942f844c.jpg)  
Figure 4.5. The field of $2 \cdot \mathrm { f o r m s } M a x w e I I = { } ^ { \ast } F = e \sin \theta d \theta \wedge d \phi$ that describes the electromagnetic field of a charge $_ e$ at rest at the origin.This picture is actually the intersection of $\yen 5$ with a 3-surface of constant time t; i.e.,the time direction is suppressed from the picture.

$$
\overline { { \varphi } } = \arctan \frac { \overline { { y } } } { \overline { { x } } } ; \qquad { \pmb d } \overline { { \varphi } } = \frac { \overline { { x } } \pmb { d } \overline { { y } } - \overline { { y } } \pmb { d } \overline { { x } } } { \overline { { x } } ^ { 2 } + \overline { { y } } ^ { 2 } } ;
$$

$$
\cos \theta = \frac { \overline { { z } } } { \overline { { r } } } ; \qquad - d ( \cos \theta ) = \frac { - d \overline { { z } } } { \overline { { r } } } + \frac { \overline { { z } } } { \overline { { r } } ^ { 3 } } ( \overline { { x } } d \overline { { x } } + \overline { { y } } d \overline { { y } } + \overline { { z } } d \overline { { z } } ) ;
$$

(d） combine to find

$$
{ } ^ { * } F = ( e / \overline { { r } } { } ^ { 3 } ) ( \overline { { x } } d / \overline { { y } } \wedge d / \overline { { z } } + \overline { { y } } d / \overline { { z } } \wedge d / \overline { { x } } + \overline { { z } } d / \overline { { x } } \wedge d / \overline { { y } } )
$$

(electromagnetic field of point charge in a comoving Cartesian system; spherically symmetric). Now transform to laboratory coordinates:

$$
\frac { 1 } { \sqrt { 1 - \beta ^ { 2 } } } = \cosh \alpha , ~ \frac { \beta } { \sqrt { 1 - \beta ^ { 2 } } } = \sinh \alpha
$$

$$
\left\{ \begin{array} { l } { { \overline { { t } } = t \cosh \alpha - x \sinh \alpha , } } \\ { { \overline { { x } } = - t \sinh \alpha + x \cosh \alpha , } } \\ { { \overline { { y } } = y \qquad \overline { { z } } = z ; } } \end{array} \right.
$$

$$
\overline { { { r } } } = [ ( x \cosh \alpha - t \sinh \alpha ) ^ { 2 } + y ^ { 2 } + z ^ { 2 } ] ^ { 1 / 2 } ;
$$

$$
\begin{array} { c } { { ^ { * } F = ( e / \bar { r } ^ { 3 } ) [ ( x \cosh \alpha - t \sinh \alpha ) \ / d \gamma \wedge d z + \gamma \ d z \wedge } } \\ { { ( \cosh \alpha \ d x - \sinh \alpha \ d t ) + z ( \cosh \alpha \ d x - \sinh \alpha \ d t ) \wedge \ d y ] ; } } \end{array}
$$

(d) compare with the general dual 2-form,

$$
\begin{array} { r l } & { ^ { * } F = E _ { z } { \bf { \em d } } \mathrm { \large / } { \mathrm {  ~ \wedge ~ } } { \bf { \it d } } z + E _ { y } { \bf { \em d } } z \mathrm {  ~ \wedge ~ } { \bf { \it d } } x + E _ { z } { \bf { \em d } } x \mathrm {  ~ \wedge ~ } { \bf { \it d } } y } \\ & { \qquad + B _ { x } { \bf { \em d } } t \mathrm {  ~ \wedge ~ } { \bf { \it d } } x + B _ { y } { \bf { \em d } } t \mathrm {  ~ \wedge ~ } { \bf { \it d } } y + B _ { z } { \bf { \em d } } t \mathrm {  ~ \wedge ~ } { \bf { \it d } } z ; } \end{array}
$$

and get the desired individual field components

$$
\begin{array} { r l r l } & {  E _ { x } = ( e / \overline { r } ^ { 3 } ) ( x \cosh \alpha - t \sinh \alpha ) , \quad } & { B _ { x } = 0 , } \\ & {  E _ { y } = ( e / \overline { r } ^ { 3 } ) ) ^ { \prime } \cosh \alpha , \quad } & { B _ { y } = - ( e / \overline { r } ^ { 3 } ) z \sinh \alpha ,  } \\ & {  \vphantom { ( e / \overline { r } ^ { 3 } ) }  E _ { z } = ( e / \overline { r } ^ { 3 } ) z \cosh \alpha ,  } & & { B _ { z } = ( e / \overline { r } ^ { 3 } ) y \sinh \alpha . } \end{array}
$$

One can verify that the invariants

$$
\begin{array} { l } { { B ^ { 2 } - E ^ { 2 } = \displaystyle \frac { 1 } { 2 } F _ { \alpha \beta } F ^ { \alpha \beta } , } } \\ { { { } } } \\ { { E \cdot B = \displaystyle \frac { 1 } { 4 } F _ { \alpha \beta } { } ^ { * } F ^ { \alpha \beta } } } \end{array}
$$

have the same value in the laboratory frame as in the rocket frame,as required. Note that the honeycomb structure of the differential form is not changed when one goes from the rocket frame to the laboratory frame. What changes is only the mathematical formula that describes it.

# \$4.4.RADIATION FIELDS

The Maxwel structure of tubes associated with a charge in uniform motion is more remarkable than it may seem at first sight, and not only because of the Lorentz contraction of the tubes in the direction of motion. The tubes arbitrarily far away move on in military step with the charge on which they center, despite the fact that there is no time for information“emitted” from the charge“right now” to get to the faraway tube “right now.” The structure of the faraway tubes “right now” must therefore derive from the charge at an earlier moment on its uniform-motion, straight-line trajectory. This circumstance shows up nowhere more clearly than in what happens to the field in consequence of a sudden change, in a short time $\pmb { A } \tau$ from one uniform velocity to another uniform velocity (Figure 4.6). The tubes have the standard patterns for the two states of motion, one pattern within a sphere of radius $r ,$ ，the other outside that sphere,where $r$ is equal to the lapse of time ("cm of light-travel time") since the acceleration took place. The necessity for the two patterns to fit together in the intervening zone, of thickness $\varDelta r = \varDelta \tau$ ,forces the field there to be multiplied up by a“stretching factor,” proportional to $r .$ This factor is responsible for the well-known fact that radiative forces fall off inversely only as the first power of the distance (Figure 4.6).

When the charge continuously changes its state of motion, the structure of the electromagnetic field, though based on the same simple principles as those illustrated in Figure 4.6, nevertheless looks more complex. The following is the Faraday 2-form for the field of an electric dipole of magnitude $p _ { 1 }$ oscillating up and down paralel to the $z$ -axis:

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0002_pages_0071-0140/auto/images/b0fc137f55ea69873815b93d4b12a50bf008d0117e9b0dae94307807a703e1f8.jpg)  
Figure 4.6. Mechanism of radiation. J. J. Thomson's way to understand why the strength of an electromagnetic wave falls only as the inverse first power of distance $r$ and why the amplitude of the wave varies (for low velocities） as $\sin \theta$ (maximum in the plane perpendicular to the line of acceleration). The charge was moving to the left at uniform velocity.Far away from it,the lines of force continue to move as if this uniform velocity were going to continue forever (Coulomb field of point-charge in slow motion).However, closer up the field is that of a point-change moving to the right with uniform velocity $\scriptstyle 1 / r ^ { 2 }$ dependence of strength upon distance). The change from the one field patern to another is confined to a shell of thickness $\pmb { \mathscr { s } } _ { \tau }$ Iocated at a distance $r$ from the point of acceleration (amplification of field by “stretching factor" $r \sin \theta \ \varDelta \beta / \varDelta \tau$ ；see text). We thank C.Teitelboim for the construction of this diagram.

$$
\begin{array} { r l } & { \underbrace { [ 2 \cos \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } \right) } _ { \mathrm { g i v e s ~ } E _ { r } } d r \wedge d t + \underbrace { \sin \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } - \frac { \omega ^ { 2 } } { r } \right) } _ { \mathrm { g i v e s ~ } E _ { \theta } } r d \theta \wedge d t } \\ & { \underbrace { + \sin \theta \left( \frac { - i \omega } { r ^ { 2 } } - \frac { \omega ^ { 2 } } { r } \right) } _ { \mathrm { g i v e s ~ } B _ { \phi } } d r \wedge r d \theta ] \} } \end{array}
$$

and the dual 2-form Maxwell $= ^ { \ast } F$ is

$$
{ } ^ { * } F = - B _ { x } d x \wedge d t - \cdot \cdot \cdot + E _ { x } d y \wedge d z + \cdot \cdot \cdot = \mathrm { r e a l } _ { \mathrm { ~ \tiny ~ h ~ } }
$$

$$
[ \sin \theta \left( { \frac { - i \omega } { r ^ { 2 } } } - { \frac { \omega ^ { 2 } } { r } } \right) \mathbf { \mathscr { d } } t \wedge r \sin \theta \ \mathbf { \mathscr { d } } \phi
$$

$$
\begin{array} { r l } & { \underbrace { + \ 2 \cos \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } \right) r \ d \theta \wedge r \sin \theta \ d \phi } _ { \mathrm { g i v e s ~ } E _ { r } } } \\ & { + \ \sin \theta \left( \frac { 1 } { r ^ { 3 } } - \frac { i \omega } { r ^ { 2 } } - \frac { \omega ^ { 2 } } { r } \right) r \sin \theta \ d \phi \wedge \ d r ] \} . } \end{array}
$$

# $\ S 4 . 5$ . MAXWELL'S EQUATIONS

The general 2-form $\pmb { F }$ is written as a superposition of wedge products with a factor $^ { \frac { 1 } { 2 } , }$

$$
F = \frac { 1 } { 2 } F _ { \mu \nu } d x ^ { \mu } \wedge d x ^ { \nu } ,
$$

because the typical term appears twice, once as $F _ { x y } \ d x . \wedge d y$ and the second time as $F _ { y x } \pmb { d y } \wedge \pmb { d x }$ with $F _ { y x } = - F _ { x y }$ and dy $\bigwedge d x = - d x \wedge d y .$

If differentiation ("taking the gradient”; the operator $\pmb { d }$ ） produced out of a scalar a l-form,it is also true that differentiation (again the operator $\pmb { d } ,$ but now generally known under Cartan's name of “exterior differentiation"） produces a 2-form out of the general 1-form; and applied to a 2-form produces a 3-form; and applied to a 3-form produces a 4-form,the form of the highest order that spacetime will accommodate. Write the general $f$ form as

$$
\phi = \frac { 1 } { f ! } \phi _ { \alpha _ { 1 } \alpha _ { 2 } \ldots \alpha _ { f } } d x ^ { \alpha _ { 1 } } \wedge d x ^ { \alpha _ { 2 } } \wedge \cdot \cdot \cdot \wedge d x ^ { \alpha _ { f } }
$$

where the coefficient $\phi _ { \alpha _ { 1 } \alpha _ { 2 } \dots \alpha _ { f } }$ ,like the wedge product that follows it,isantisymmetric under interchange of any two indices.Then the exterior derivative of $\pmb { \phi }$ is

$$
d \phi \equiv \frac { 1 } { f ! } \frac { \partial \phi _ { \alpha _ { 1 } \alpha _ { 2 } \ldots \alpha _ { f } } } { \partial x ^ { \alpha _ { 0 } } } d x ^ { \alpha _ { 0 } } \wedge d x ^ { \alpha _ { 1 } } \wedge d x ^ { \alpha _ { 2 } } \wedge \cdots \wedge d x ^ { \alpha _ { f } } .
$$

Take the exterior derivative of Faraday according to this rule and find that it vanishes, not only for the special.case of the dipole oscillator,but also for a general electromagnetic field. Thus, in the coordinates appropriate for a local Lorentz frame, one has

$$
\begin{array} { l } { d F = d ( E _ { x } d x \wedge d t + \cdot \cdot \cdot + B _ { x } d y \wedge d z + \cdot \cdot \cdot ) } \\ { \ } \\ { = \left( { \frac { \partial E _ { x } } { \partial t } } d t + { \frac { \partial E _ { x } } { \partial x } } d x + { \frac { \partial E _ { x } } { \partial y } } d y + { \frac { \partial E _ { x } } { \partial z } } d z \right) \wedge d x \wedge d t } \\ { \ } \\ { \qquad + \cdot \cdot \cdot ( 5 \ \mathrm { m o r e \ s u c h \ s e t s \ o f \ 4 \ t e r m s \ e a c h } ) \cdot \cdot \cdot . . } \end{array}
$$

Note that such a term as dy $\wedge$ dy $\wedge \ d z$ is automatically zero("collapse of egg-crate cell when stamped $\left. \mathsf { o n } ^ { \mathsf { \pmb { \mathsf { \imath } } } } \right.$ ). Collect the terms that do not vanish and find

$$
\begin{array} { c } { { d F = \left( \displaystyle \frac { \partial B _ { x } } { \partial x } + \displaystyle \frac { \partial B _ { y } } { \partial y } + \displaystyle \frac { \partial B _ { z } } { \partial z } \right) d x \wedge d y \wedge d z } } \\ { { \ } } \\ { { + \left( \displaystyle \frac { \partial B _ { x } } { \partial t } + \displaystyle \frac { \partial E _ { z } } { \partial y } - \displaystyle \frac { \partial E _ { y } } { \partial z } \right) d t \wedge d y \wedge d z } } \\ { { \ } } \\ { { + \left( \displaystyle \frac { \partial B _ { y } } { \partial t } + \displaystyle \frac { \partial E _ { z } } { \partial z } - \displaystyle \frac { \partial E _ { z } } { \partial x } \right) d t \wedge d z \wedge d x } } \\ { { \ } } \\ { { + \left( \displaystyle \frac { \partial B _ { z } } { \partial t } + \displaystyle \frac { \partial E _ { y } } { \partial x } - \displaystyle \frac { \partial E _ { z } } { \partial y } \right) d t \wedge d x \wedge d y . } } \end{array}
$$

Each term in this expression is familiar from Maxwell's equations

$$
\mathrm { d i v } \pmb { B } = \nabla \cdot \pmb { B } = 0
$$

and

$$
\operatorname { c u r l } E = \nabla \times E = - \dot { B } .
$$

Each vanishes, and with their vanishing Faraday itself is seen to have zero exterior derivative:

$$
\begin{array} { r } { { \pmb d } { \pmb F } = 0 . } \end{array}
$$

In other words,“Faraday is a closed 2-form”;“the tubes of $\pmb { F }$ nowhere come to an end.”

A similar calculation gives for the exterior derivative of the dual 2-form Maxwell the result

$$
\begin{array} { r l } & { d ^ { * } F = d ( - B _ { x } d x \wedge d t - \cdots + E _ { x } d y \wedge d z + \cdots ) } \\ & { \qquad = \left( \frac { \partial E _ { x } } { \partial x } + \frac { \partial E _ { y } } { \partial y } + \frac { \partial E _ { z } } { \partial z } \right) d x \wedge d y \wedge d z } \\ & { \qquad + \left( \frac { \partial E _ { x } } { \partial t } - \frac { \partial B _ { z } } { \partial y } + \frac { \partial B _ { y } } { \partial z } \right) d t \wedge d y \wedge d z } \\ & { \qquad + \ \cdots } \end{array}
$$

$$
\begin{array} { r l } & { = 4 \pi ( \rho \ d x \wedge d y \wedge d z } \\ & { \quad - J _ { x } \ d t \wedge d y \wedge d z } \\ & { \quad - J _ { y } \ d t \wedge d z \wedge d x } \\ & { \quad - J _ { z } \ d t \wedge d x \wedge d y ) = 4 \pi ^ { \ast } J ; } \end{array}
$$

$$
d ^ { * } F = 4 \pi ^ { * } J .
$$

Faraday structure: tubes nowhere end

Maxwell structure: density of tube endings given by charge-current 3-form


<!-- chunk 0003: pages 141-210 -->
Duality:the only place in electromagnetism where metric must enter

In empty space this exterior derivative, too, vanishes; there Maxwell is a closed 2-form; the tubes of $^ { * } F ,$ like the tubes of $\pmb { F } ,$ nowhere come to an end.

In a region where charge is present, the situation changes. Tubes of Maxwell take their origin in such a region.The density of endings is described by the 3-frm ${ \boldsymbol { \mathsf { A } } } = { \boldsymbol { \mathsf { I } } } =$ charge,a “collection of eggcrate cells” collected along bundles of world lines.

The two equations

$$
\pmb { d } \pmb { F } = 0
$$

and

$$
{ \pmb d } ^ { * } { \pmb F } = 4 \pi ^ { * } { \pmb J }
$$

summarize the entire content of Maxwel's equations in geometric language. The forms $\pmb { F } =$ Faraday, and ${ \pmb { F } } =$ Maxwell, can be described in any coordinates one pleases-or in a language (honeycomb and egg-crate structures) free of any reference whatsoever to coordinates. Remarkably, neither equation makes any reference whatsoever to metric. As Hermann Weyl was one of the most emphatic in stressing (see also Chapters 8 and 9),the concepts of form and exterior derivative are metricfree. Metric made an appearance only in one place,in the concept of duality ("perpendicularity"） that carried attention from $\pmb { F }$ to the dual structure ${ \pmb { \imath } } _ { \pmb { F } }$

# $\ S 4 . 6$ . EXTERIOR DERIVATIVE AND CLOSED FORMS

The words “honeycomb” and “egg crate” may have given some feling for the geometry that goes with electrodynamics. Now to spell out these concepts more clearly and illustrate in geometric terms,with electrodynamics as subject matter, what it means to speak of “exterior differentiation.”Marching around a boundary, yes; but how and why and with what consequences?It is helpful to return to functions and l-forms, and see them and the 2-forms Faraday and Maxwelland the 3-form charge as part of an ordered progression (see Box 4.4). Two-forms are seen in this box to be of two kinds:(l） a special 2-form,known as a“closed”2-form,which has the property that as many tubes enter a closed 2-surface as emerge from it (exterior derivative of 2-form zero; no 3-form derivable from it other than the trivial zero 3-form!)； and (2) a general 2-form, which sends across a closed 2-surface a non-zero net number of tubes,and therefore permits one to define a nontrivial 3-form ("exterior derivative of the 2-form"),which has precisely as many egg-crate cells in any closed 2-surface as the net number of tubes of the 2-form emerging from that same closed 2-surface (generalization of Faraday's concept of tubes of force to the world of spacetime,curved as well as flat).

(continued on page 120)

# Box 4.4 THE PROGRESSION OF FORMS AND EXTERIOR DERIVATIVES

# O-Form or Scalar, $f$

An example in the context of 3-space and Newtonian physics is temperature, $T ( x , y , z )$ ,and in the context of spacetime, a scalar potential, $\phi ( t , x , y , z )$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/ee62465b2bf45a21130f9c4b8c5909504b23dcc8c8bb566c6a85557d1326ec10.jpg)

# From Scalar to 1-Form

Take the gradient or “exterior derivative”of a scalar $f$ to obtain a special l-form, $\gamma = d f .$ Comments: (a) Any additive constant included in $f$ is erased in the process of differentiation; the quantity $n$ in the diagram at the left is unknown and irrelevant.(b) The 1-form $\pmb { \gamma }$ is special in the sense that surfaces in one region“mesh”with surfaces in a neighboring region ("closed 1-form"). (c) Line integral $f _ { \ddot { G } } ^ { \dot { c } \dot { \beta } }$ df is independent of path for any class of paths equivalent to one another under continuous deformation.(d) The 1-form is a machine to produce a number ("bongs of bell as each successive integral surface is crossed) out of a displacement (approximation to concept of a tangent vector).

# General 1-Form $\beta = \beta _ { \alpha } d x ^ { \alpha }$

This is a pattern of surfaces,as illustrated in the diagram at the right; i.e.,a machine to produce a number ("bongs of bell"; $\langle \pmb { \beta } , \pmb { \mu } \rangle )$ out of a vector. A l-form has a reality and position in space independent of all choice of coordinates. Surfaces do not ordinarily mesh. Integral $\int \pmb { \beta }$ around indicated closed loop does not give zero("more bongs than antibongs").

# From 1-Form to 2-Form $\xi = d \beta = { \frac { \partial \beta _ { \alpha } } { \partial x ^ { \mu } } } d x ^ { \mu } \wedge d x ^ { \alpha }$

$\pmb { \xi }$ is a pattern of honeycomb-like cells,with a direction of circulation marked on each,so stationed that the number of cells encompassed in the dotted closed path is identical 'to the net contribution (excess of bongs over antibongs) for the same path in the diagram of $\pmb { \beta }$ above.The“exterior derivative” is defined so this shall be so; the generalized Stokes theorem codifies it. The word “exterior" comes from the fact that the path goes around the periphery of the region under analysis. Thus the 2-form is a machine to get a number (number of tubes, $\langle \pmb { \xi } , \pmb { u } \wedge \pmb { v } \rangle )$ out of a bit of surface $( u \wedge v )$ that has a sense of circulation indicated upon it.The 2-form thus defined is special in this sense: a rubber sheet “supported around its edges” by the dotted curve or any other closed curve is crossed by the same number of tubes when: (a) it bulges up in the middle; (b) it is pushed down in the middle; (c) it experiences any other continuous deformation. The Faraday or 2-form $\pmb { F }$ of electromagnetism, always expressible as ${ \pmb F } = \pmb { d } { \pmb A }$ $( A = 4$ -potential,a 1-form), also has always this special property ("conservation of tubes").

# 0-Form to 1-Form to 2-Form? No!

Go from scalar $f$ to 1-form $\gamma = d f$ The next step to a 2-form $\pmb { \alpha }$ is vacuous.The net contribution of the line integral $\scriptstyle { \int } \gamma$ around the dotted closed path is automatically zero. To reproduce that zero result requires a zero 2-form. Thus $\alpha = d \gamma = d d f$ has to be the zero 2-form. This result is a special instance of the general result ${ \pmb d } { \pmb d } = 0$

Again,this is a honeycomb-like structure,and again a machine to get a number (number of tubes, $\langle \pmb { \sigma } , \pmb { u } \wedge \pmb { v } \rangle )$ out of a surface $( u \wedge v )$ that has a sense of circulation indicated on it. It is general in the sense that the honeycomb structures in one region do not ordinarily mesh with those in a neighboring region. In consequence,a closed 2-surface, such as the box-like surface indicated by dotted lines at the right,is ordinarily crossed by a non-zero net number of tubes. The net number of tubes emerging from such a closed surface is,however,exactly zero when the 2-form is the exterior derivative of a 1-form.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/d54e9d79ac79cde60327a04a52e2ef535eb1258b1502624275ca2cce0e2656da.jpg)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/b713679a6cd6f16d2c20df51b2c0a1b43812ee45d5d3c7b7c3e51fbb8f373692.jpg)

# From 2-Form to 3-Form ${ \pmb \mu } = { \pmb d } { \pmb \sigma } = \frac { \partial \sigma _ { | \alpha \beta | } } { \partial x ^ { \gamma } } { \pmb d } x ^ { \gamma } \wedge { \pmb d } x ^ { \alpha } \wedge { \pmb d } x ^ { \beta } ,$ where $d x ^ { \gamma } \wedge d x ^ { \alpha } \wedge d x ^ { \beta } \equiv 3 ! d x ^ { [ \gamma } \otimes d x ^ { \alpha } \otimes d x ^ { \beta ] }$

This egg-crate type of structure is a machine to get a number (number of cells $\langle { \pmb \mu } , { \pmb u } \wedge { \pmb v } \wedge { \pmb w } \rangle )$ from a volume (volume $u \wedge v \wedge$ w within which one counts the cels). A more complete diagram would provide each cell and the volume of integration itself with an indicator of orientation (analogous to the arrow of circulation shown for cells of the 2-form). The contribution of a given cell to the count of cells is $+ 1$ or $^ { - 1 }$ ,according as the orientation indicators have same sense or opposite sense. The number of egg-crate cells of $\pmb { \mu } = \pmb { d \sigma }$ in any given volume (such as the volume indicated by the dotted lines） is tailored to give precisely the same number as the net number of tubes of the 2-form o (diagram above) that emerge from that volume (generalized Stokes theorem). For electromagnetism, the exterior derivative of Faraday or 2-form $\pmb { F }$ gives a null 3-form, but the exterior derivative of Maxwel or 2-form $\ast _ { F }$ gives 4π times the 3-form \*J of charge:

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/e6b3df8130b63c3680992c6d13e1ef80681a3bc44c5c0704f9626dc53fb874c1.jpg)

$$
\begin{array} { c } { { { } ^ { * } J = \rho ~ d x ~ \wedge ~ d y ~ \wedge ~ d z - J _ { z } ~ d t ~ \wedge ~ d y ~ \wedge ~ d z } } \\ { { - ~ J _ { y } ~ d t ~ \wedge ~ d z ~ \wedge ~ d x - J _ { z } ~ d t ~ \wedge ~ d x ~ \wedge ~ d y . } } \end{array}
$$

# From 1-Form to 2-Form to 3-Form? No!

Starting with a 1-form (electromagnetic 4-potential). construct its exterior derivative. the 2-form $\boldsymbol { F } = d \boldsymbol { A } \left( F a r a d a y \right)$ .The tubes in this honeycomb-like structure never end. So the number of tube endings in any elementary volume,and with it the 3-form ${ \pmb d } { \pmb F } = { \pmb d } { \pmb d } { \pmb A }$ ,is automatically zero. This is another example of the general result that ${ \pmb d } { \pmb d } = 0$

# From 2-Form to 3-Form to 4-Form? No!

Starting with 2-form $\yen 5$ (Maxwell),construct its exterior derivative, the 3-form $4 \pi ^ { * } J$ ，The cells in this egg-crate type of structure extend in a fourth dimension ("hypertube"). The number of these hypertubes that end in any elementary 4-volume,and with it the 4-form

$$
d ( 4 \pi \sp * J ) = d d \sp * F ,
$$

is automatically zero, still another example of the general result that ${ \pmb d } { \pmb d } = 0$ This result says that

$$
d ^ { * } J = \left( { \frac { \partial \rho } { \partial t } } + { \frac { \partial J _ { z } } { \partial x } } + { \frac { \partial J _ { y } } { \partial y } } + { \frac { \partial J _ { z } } { \partial z } } \right) d t \wedge d x \wedge d y \wedge d z = 0
$$

("law of conservation of charge"). Note:

$$
d x ^ { \alpha } \wedge d x ^ { \beta } \wedge d x ^ { \gamma } \wedge d x ^ { \delta } \equiv 4 ! d x ^ { [ \alpha } \otimes d x ^ { \beta } \otimes d x ^ { \gamma } \otimes d x ^ { \delta ] } .
$$

This implies dt ^ dx ^ dy $\wedge \ d z = \varepsilon$

This four-dimensional "super-egg-crate" type structure is a machine to get a number (number of cells, $\langle \pmb { \tau } , \pmb { n } \wedge \pmb { u } \wedge \pmb { v } \wedge \pmb { w } \rangle ,$ ）from a 4-volume $\pmb { \eta } \wedge \pmb { \ u } \wedge \pmb { \ v } \wedge \pmb { w } .$

# From 4-Form to 5-Form? No!

Spacetime, being four-dimensional, cannot accommodate five-dimensional egg-crate structures.At least two of the $\pmb { d x ^ { \mu } 5 }$ in

$$
d x ^ { \alpha } \wedge d x ^ { \beta } \wedge d x ^ { \gamma } \wedge d x ^ { \delta } \wedge d x ^ { \varepsilon }
$$

must be the same; so, by antisymmetry of $^ { 6 6 } \wedge$ ,” this “basis 5-form” must vanish.

# Results of Exterior Differentiation, Summarized

<table><tr><td>0-form 1-form 2-form 3-form 4-form 5-form?</td><td rowspan="8">f df ddf=0 No!</td><td rowspan="8">A F = dA dF = ddA三0</td><td></td></tr><tr><td>*F 4 *J = d*F</td></tr><tr><td>d(4π *J)= dd*F三0</td><td>U 4</td></tr><tr><td></td><td>T = dv</td></tr><tr><td></td><td></td></tr><tr><td></td><td>dT三0 du三o</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

# New Forms from Old by Taking Dual (see exercise 3.14)

Dual of scalar $f$ is 4-form: ${ } ^ { * } f = f d x ^ { 0 } \wedge d x ^ { 1 } \wedge d x ^ { 2 } \wedge d x ^ { 3 } = f \varepsilon .$

Dual of 1-form $\pmb { J }$ is 3-form: ${ } ^ { * } J = J ^ { 0 } d x ^ { 1 } \wedge d x ^ { 2 } \wedge d x ^ { 3 } - J ^ { 1 } d x ^ { 2 } \wedge d x ^ { 3 } \wedge d x ^ { 0 }$ + J² dx ∧ dx° > dx1 - J³ dx° ∧ dx1 > dx².

Dual of 2-form $\pmb { F }$ is 2-form: ${ } ^ { * } F = F ^ { | \alpha \beta | } \varepsilon _ { \alpha \beta | \mu \nu | } d x ^ { \mu } \wedge d x ^ { \nu }$ ，where

$$
F ^ { \alpha \beta } = \eta ^ { \alpha \lambda } \eta ^ { \beta \delta } F _ { \lambda \delta } .
$$

Dual of 3-form $\pmb { \kappa }$ is 1-form: ${ } ^ { * } K = K ^ { 0 1 2 } d x ^ { 3 } - K ^ { 1 2 3 } d x ^ { 0 } + K ^ { 2 3 0 } d x ^ { 1 } - K ^ { 3 0 1 } d x ^ { 2 } ,$ where $K ^ { \alpha \beta \gamma } = \eta ^ { \alpha \mu } \eta ^ { \beta \nu } \eta ^ { \gamma \lambda } K _ { \mu \nu \lambda }$

Dual of 4-form $\pmb { L }$ is a scalar: ${ \cal L } = { \cal L } _ { 0 1 2 3 } d x ^ { 0 } \wedge d x ^ { 1 } \wedge d x ^ { 2 } \wedge d x ^ { 3 }$ ${ } ^ { * } L = L ^ { 0 1 2 3 } = - L _ { 0 1 2 3 }$

Note 1: This concept of duality between one form and another is to be distinguished from the concept of duality between the vector basis ${ \pmb e } _ { { \pmb \alpha } }$ and the $I$ -form basis $\pmb { \omega } ^ { \pmb { \alpha } }$ of a given frame. The two types of duality have nothing whatsoever to do with each other!

Note 2: In spacetime,the operation of taking the dual, applied twice,leads back to the original form for forms of odd order,and to the negative thereof for forms of even order. In Euclidean 3-space the operation reproduces the original form, regardless of its order.

# Duality Plus Exterior Differentiation

Start with scalar $\phi$ .Its gradient $\pmb { d } \phi$ is a l-form. Take its dual, to get the 3-form $\yen 60$ Take its exterior derivative,to get the 4-form ${ \pmb d } ^ { * } { \pmb d } \phi$ . Take its dual, to get the scalar $\square \phi \equiv - ^ { * } d ^ { * } d \phi$ . Verify by index manipulations that Q as defined here is the wave operator; i.e., in any Lorentz frame, $\nabla \phi = \phi _ { , \alpha } { } ^ { , \alpha } = - ( \partial ^ { 2 } \phi / \partial t ^ { 2 } ) + \nabla ^ { 2 } \phi$

Start with $I$ -form A. Get 2-form ${ \pmb F } = { \pmb d } { \pmb A }$ . Take its dual ${ } ^ { \ast } F = { } ^ { \ast } d A$ ,also a 2-form. Take its exterior derivative,obtaining the 3-form $\pmb { d } ^ { \ast } \pmb { F }$ (has value $4 \pi ^ { \bullet } J$ in electromagnetism). Take its dual, obtaining the 1-form $^ { * } d ^ { * } F = { } ^ { * } d ^ { * } d A = 4 \pi J$ ("Wave equation for electromagnetic 4-potential"). Reduce in index notation to

$$
F _ { \mu \nu } ^ { \quad , \nu } = A _ { \nu , \mu } ^ { \quad , \nu } - A _ { \mu , \nu } ^ { \quad , \nu } = 4 \pi J _ { \mu } .
$$

[More in Flanders (1963) or Misner and Wheeler (1957); see also exercise 3.17.]

# \$4.7. DISTANT ACTION FROM LOCAL LAW

Differential forms are a powerful tool in electromagnetic theory,but full power requires mastery of other tools as well. Action-at-a-distance techniques ("Green's functions,”“propagators") are of special importance.Moreover,the passage from Maxwell field equations to electromagnetic action at a distance provides a preview of how Einstein's local equations will reproduce (approximately) Newton's $1 / r ^ { 2 }$ law.

In flat spacetime and in a Lorentz coordinate system, express the coordinates of particle $\pmb { A }$ as a function of its proper time $\pmb { \alpha }$ ,thus:

$$
a ^ { \mu } = a ^ { \mu } ( \alpha ) , \frac { d a ^ { \mu } } { d \alpha } = \dot { a } ^ { \mu } ( \alpha ) , \frac { d ^ { 2 } a ^ { \mu } } { d \alpha ^ { 2 } } = \ddot { a } ^ { \mu } ( \alpha ) .
$$

Dirac found it helpful to express the distribution of charge and current for a particle of charge $^ e$ following such a motion as a superposition of charges that momentarily

flash into existence and then flash out of existence.Any such flash has a localization in space and time that can be written as the product of four Dirac delta functions [see,for example, Schwartz (1950-195l),Lighthill (1958):

World line of charge regarded as succession of flash-on, flash-off charges

$$
\delta ^ { 4 } ( x ^ { \mu } - a ^ { \mu } ) = \delta [ x ^ { 0 } - a ^ { 0 } ( \alpha ) ] \delta [ x ^ { 1 } - a ^ { 1 } ( \alpha ) ] \delta [ x ^ { 2 } - a ^ { 2 } ( \alpha ) ] \delta [ x ^ { 3 } - a ^ { 3 } ( \alpha ) ] .
$$

Here any single Dirac function $\delta ( x )$ ("symbolic function”;“distribution”；“limit of a Gauss error function” as width is made indefinitely narrow and peak indefinitely high,with integrated value always unity) both (l) vanishes for $x \neq 0$ ,and (2) has the integral $\textstyle \int _ { - \infty } ^ { + \infty } \delta ( x ) d x = 1$ .Described in these terms,the density-current vector for the particle has the value ("superposition of flashes")

$$
J ^ { \mu } = e \int \delta ^ { 4 } [ x ^ { \nu } - a ^ { \nu } ( \alpha ) ] \dot { a } ^ { \mu } ( \alpha ) d \alpha .
$$

The density-current (4.34) drives the electromagnetic feld, $\pmb { F } .$ Write ${ \pmb F } = \pmb { d A }$ to satisfy automatically half of Maxwel's equations $( d F = d d A \equiv 0$ ：

$$
F _ { \mu \alpha } = \frac { \partial A _ { \alpha } } { \partial x ^ { \mu } } - \frac { \partial A _ { \mu } } { \partial x ^ { \alpha } } .
$$

In flat space,the remainder of Maxwel's equations $( d ^ { * } F = 4 \pi ^ { * } J$ ）become

$$
{ \frac { { \partial } F _ { \mu } ^ { \ \nu } } { { \partial } x ^ { \nu } } } = 4 \pi J _ { \mu }
$$

or

$$
\frac { \partial } { \partial x ^ { \mu } } \frac { \partial A ^ { \nu } } { \partial x ^ { \nu } } - \eta ^ { \nu \alpha } \frac { \partial ^ { 2 } A _ { \mu } } { \partial x ^ { \nu } \partial x ^ { \alpha } } = 4 \pi J _ { \mu } .
$$

Make use of the freedom that exists in the choice of 4-potentials $A ^ { \nu }$ to demand

$$
{ \frac { \partial A ^ { \nu } } { \partial x ^ { \nu } } } = 0
$$

(Lorentz gauge condition; see exercise 3.17). Thus get

$$
\Pi A _ { \mu } = - 4 \pi J _ { \mu } .
$$

The electromagnetic wave equation

The density-current being the superposition of “flashes,” the effect $( A )$ of this density-current can be expressed as the superposition of the effects $\boldsymbol { \varepsilon }$ of elementary flashes; thus

$$
A ^ { \mu } ( x ) = \int E [ x - a ( \alpha ) ] \dot { a } ^ { \mu } ( \alpha ) d \alpha ,
$$

The solution of the wave equation

where the"elementary effect” $E$ ("kernel";“Green's function")satisfies the equation

$$
\begin{array} { r } { \boxed { \ d } E ( x ) = - 4 \pi \delta ^ { 4 } ( x ) . } \end{array}
$$

One solution is the “half-advanced-plus-half-retarded potential,"”

$$
E ( x ) = \delta ( \eta _ { \alpha \beta } x ^ { \alpha } x ^ { \beta } ) .
$$

It vanishes everywhere except on the backward and forward light cones, where it has equal strength. Normally more useful is the retarded solution,

$$
R ( x ) = { \left\{ \begin{array} { l l } { 2 E ( x ) } & { \quad { \mathrm { i f ~ } } x ^ { 0 } > 0 , } \\ { 0 } & { \quad { \mathrm { i f ~ } } x ^ { 0 } < 0 , } \end{array} \right. }
$$

which is obtained by doubling (4.41) in the region of the forward light cone and nullifying it in the region of the backward light cone.All electrodynamics (Coulomb forces,Ampere's law, electromagnetic induction,radiation) follows from the simple expression (4.39) for the vector potential [see,e.g.,Wheeler and Feynman (1945) and (1949),also Rohrlich (1965)j.

# EXERCISES

# Exercise 4.1. GENERIC LOCAL ELECTROMAGNETIC FIELD EXPRESSED IN SIMPLEST FORM

In the laboratory Lorentz frame,the electric field is $\pmb { { \cal E } }$ ，the magnetic field B.Special cases are: (l) pure electric field $( B = 0 )$ ;(2) pure magnetic field $( E = 0 )$ ; and (3)“radiation field” or“null field”( $E$ and $\pmb { B }$ equal in magnitude and perpendicular in direction). All cases other than (l),(2),and (3) are“generic.”In the generic case,calculate the Poynting density of flow of energy ${ E \times B / 4 \pi }$ and the density of energy $( E ^ { 2 } + B ^ { 2 } ) / 8 \pi$ Define the direction of a unit vector $\pmb { n }$ and the magnitude of a velocity parameter $\pmb { \alpha }$ by the ratio of energy flow to energy density:

$$
n \operatorname { t a n h } 2 \alpha = \frac { 2 E \times B } { E ^ { 2 } + B ^ { 2 } } .
$$

View the same electromagnetic field in a rocket frame moving in the direction of $\pmb { n }$ with the velocity parameter $\pmb { \alpha }$ (not $\mathtt { 2 } \alpha$ ； factor2 comes in because energy flow and energy density are components, not of a vector,but of a tensor). By employing the formulas for a Lorentz transformation (equation 3.23),or otherwise,show that the energy flux vanishes in the rocket frame,with the consequence that $\bar { E }$ and $\bar { \pmb B }$ are parallel. No one can prevent the Z-axis from being put in the direction common to $\widetilde { E }$ and $\widetilde { B } .$ Show that with this choice of direction, Faraday becomes

$$
{ \pmb F } = \vec { E } _ { z } { \pmb d } \overline { { { z } } } \wedge { \pmb d } \overline { { { t } } } + \vec { B } _ { z } { \pmb d } \overline { { { x } } } \wedge { \pmb d } \overline { { { y } } }
$$

(only two wedge products needed to represent the generic local field; “canonical representation”;valid in one frame,valid in any frame).

# Exercise 4.2. FREEDOM OF CHOICE OF 1-FORMS IN CANONICAL REPRESENTATION OF GENERIC LOCAL FIELD

Deal with a region so smallthat the variation of the field from place to place can be neglected. Write Faraday in canonical representation in the form

$$
{ \pmb F } = { \pmb d } p _ { I } \wedge { \pmb d } q ^ { I } + { \pmb d } p _ { I I } \wedge { \pmb d } q ^ { I I } ,
$$

where $p _ { A }$ $\boldsymbol { \mathcal { A } } = \boldsymbol { I }$ or $\boldsymbol { { \mathit { I I } } }$ ）and $q ^ { A }$ are scalar functions of position in spacetime. Define a “canonical transformation” to new scalar functions of position $p _ { \bar { A } }$ and $q ^ { \bar { A } }$ by way of the “equation of transformation”

$$
p _ { A } \ : d q ^ { A } = d S + p _ { \bar { A } } \ : d q ^ { \bar { A } } ,
$$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0003_pages_0141-0210/auto/images/6899e3106ab3823a6cd2f0c9c22b91470a92e2950ac63598ec4e9ac1366182be.jpg)  
Figure 4.7. Some simple types of l-forms compared and contrasted.

where the“generating function” $s$ of the transformation is an arbitrary function of the $q ^ { A }$ and the $q ^ { \bar { A } }$ ：

$$
d S = ( \hat { \sigma } S / \hat { \partial } q ^ { A } ) d q ^ { A } + ( \hat { \sigma } S / \partial q ^ { \bar { A } } ) d q ^ { \bar { A } } .
$$

(a) Derive expressions for the two $p _ { A }$ 's and the two $\boldsymbol { p _ { \vec { A } } } ^ { * } \boldsymbol { s }$ in terms of $s$ by equating coefficients of $\bar { d q ^ { I } } , d q ^ { I I } , d q ^ { I } . d q ^ { \bar { \pi } }$ individually on the two sides of the equation of transformation.

(b) Use these expressions for the $\vec { p _ { A } } ^ { \prime } \vec { s }$ and $p _ { \vec { A } } { } ^ { * }$ to show that ${ \pmb F } = { \pmb d } p _ { A } \wedge { \pmb d } q ^ { A }$ and $\pmb { \bar { F } } =$ $d p _ { \overline { { { A } } } } \wedge d q ^ { \overline { { { A } } } }$ ,ostensibly different,are actually expressions for one and the same 2-form in terms of alternative sets of l-forms.

# Exercise 4.3. A CLOSED OR CURL-FREE 1-FORM IS A GRADIENT

Given a l-form $\pmb { \sigma }$ such that $\pmb { d \sigma } = 0$ ，show that $\pmb { \sigma }$ can be expressed in the form $\pmb { \sigma } = \pmb { d } f ,$ where $f$ is some scalar. The l-form $\pmb { \sigma }$ is said to be “curl-free,” a narrower category of l-form than the“rotation-free”l-form of the next exercise (expressble as $\sigma = h \mathop { } \mathbf { d } f$ ,and it in turn is narrower (see Figure 4.7) than the category of“l-forms with rotation”(not expressible in the form $\sigma = h \ : d f .$ ).When the l-form $\pmb { \sigma }$ is expressed in terms of basis l-forms $\pmb { d } x ^ { \alpha }$ ， multiplied by corresponding components ${ \pmb \sigma } _ { \pmb { \alpha } }$ ，show that “curl-free”implies ${ \mathfrak { o } } _ { [ \alpha , \beta ] } = 0$

# ExerciSe 4.4. CANONICAL EXPRESSION FOR A ROTATION-FREE 1-FORM

In three dimensions a rigid body turning with angular velocity $\omega$ about the $z$ -axis has components of velocity $v _ { y } = \omega x$ ,and $v _ { x } = - \omega y$ The quantity curl $\pmb { \nu } = \pmb { \nabla } \times \pmb { \nu }$ has $z$ -component equal to $z _ { \omega }$ ,and all other components equal to zero.Thus the scalar product of $\pmb { \nu }$ and curl $\mathbf { \nu } _ { \mathbf { \nu } } ^ { \mathbf { \nu } } \mathbf { \nu } _ { \mathbf { \nu } } ^ { \mathbf { \nu } }$ vanishes:

$$
v _ { [ i , j } v _ { k ] } = 0 .
$$

The same concept generalizes to four dimensions,

$$
{ } \begin{array} { r } { v _ { [ \alpha , \beta } v _ { \gamma ] } = 0 . } \end{array}
$$

and lends itself to expression in coordinate-free language,as the requirement that a certain 3-form must vanish:

$$
d v \wedge v = 0 .
$$

Any 1-form $\pmb { v }$ satisfying this condition is said to be“rotation-free.”Show that a l-form is rotation-free if and only if it can be written in the form

$$
v = h \ d f ,
$$

where $h$ and $f$ are scalar functions of position (the“Frobenius theorem").

Exercise 4.5. FORMS ENDOWED WITH POLAR SINGULARITIES

List the principal results on how such forms are representable,such as

$$
\pmb { \mathcal { O } } _ { 1 } = \frac { \pmb { d S } } { S } \wedge \pmb { \psi } _ { 1 } + \pmb { \theta } _ { 1 } ,
$$

and the conditions under which each applies [for the meaning and answer to this exercise, see Lascoux (1968)].

# ExerciSe 4.6. THE FIELD OF THE OSCILLATING DIPOLE

Verify that the expressions given for the electromagnetic field of an oscillating dipole in equations (4.23) and (4.24) satisfy $\pmb { d } \pmb { F } = 0$ everywhere and ${ \pmb d } ^ { * } { \pmb F } = 0$ everywhere except at the origin.

# Exercise 4.7. THE 2-FORM MACHINERY TRANSLATED INTO TENSOR MACHINERY

This exercise is stated at the end of the legend caption of Figure 4.l.

# Exercise 4.8. PANCAKING THE COULOMB FIELD

Figure 4.5 shows a spacelike slice, $t =$ const,through the Maxwellof a point-charge at rest. By the following pictorial steps, verify that the electric-field lines get compressed into the transverse direction when viewed from a moving Lorentz frame: (l) Draw a picture of an equatorial slice $\theta = \pi / 2$ ；t,r,Φvariable) through $M a x w e I I = { ^ { * } F } .$ (2) Draw various spacelike slices,corresponding to constant time in various Lorentz frames,through the resultant geometric structure.(3) Interpret the intersection of Maxwell $= ^ { \ast } F$ with each Lorentz slice in the manner of Figure 4.3.

# ExerciSe 4.9. COMPUTATION OF SURFACE INTEGRALS

In Box 4.1 the definition

$$
\int \alpha = \int \ldots \int \left. \alpha , { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { 1 } } } \wedge \ldots \wedge { \frac { \partial { \mathcal { P } } } { \partial \lambda ^ { p } } } \right. d \lambda ^ { 1 } \ldots d \lambda ^ { p }
$$

is given for the integral of a $\pmb { p }$ form $\pmb { \alpha }$ over a $p$ -surface $\mathcal { P } ( \lambda ^ { 1 } , \ldots , \lambda ^ { p } )$ in $\pmb { n }$ -dimensional space. From this show that the following computational rule (also given in Box 4.l) works: (l) substitute the equation for the surface,

$$
x ^ { k } = x ^ { k } ( \lambda ^ { 1 } , \ldots , \lambda ^ { p } ) ,
$$

into $\pmb { \alpha }$ and collect terms in the form

$$
\alpha = a ( \lambda ^ { 1 } , \ldots , \lambda ^ { p } ) d \lambda ^ { 1 } \wedge \ \cdots \ \wedge \ d \lambda ^ { p } ;
$$

(2) integrate

$$
\int \alpha = \int . \cdot \cdot \int a ( \lambda ^ { 1 } , . . . , \lambda ^ { p } ) d \lambda ^ { 1 } . . . d \lambda ^ { p }
$$

using the elementary definition of integration.

# Exercise 4.1O. WHITAKER'S CALUMOID,OR，THE LIFE OF A LOOP

Take a closed loop, bounding a 2-dimensional surface S.It entraps a certain flux of Faraday $\begin{array} { r } { \pmb { \phi } _ { p } = \int _ { s } \pmb { F } } \end{array}$ ("magnetic tubes") and a certain flux of Maxwell $\begin{array} { r } { \pmb { \phi } _ { \pmb { \mu } } = \int _ { s } \pmb { * } \pmb { F } } \end{array}$ ("electric tubes").

(a) Show that the fluxes $\phi _ { \pmb { F } }$ and $\tilde { \phi } _ { y }$ depend only on the choice of loop,and not on the choice of the surface $s$ bounded by the loop,if and only if $d F = d ^ { * } F = 0$ (no magnetic charge;no electric charge). Hint: use generalized Stokes theorem, Boxes 4.l and 4.6.

(b) Move the loop in space and time so that it continues to entrap the same two fluxes. Move it forward a little more here,a litte less there,so that it continues to do so. In this way trace out a 2-dimensional surface ("calumoid"; see E.T. Whitaker 1904) $\boldsymbol { \mathcal { P } } = \boldsymbol { \mathcal { P } } ( \boldsymbol { a } , \boldsymbol { b } )$ ； $x ^ { \mu } = x ^ { \mu } ( a , b )$ . Show that the elementary bivector in this surface, $\pmb { \Sigma } = \partial \pmb { \mathcal { P } } / \partial a \wedge \partial \pmb { \mathcal { P } } / \partial b$ satisfies $\langle \pmb { F } , \pmb { \Sigma } \rangle = 0$ and $\langle { } ^ { * } F , { \pmb { \Sigma } } \rangle = 0$

(c) Show that these differential equations for $x ^ { \mu } ( a , b )$ can possess a solution, with given initial condition $x ^ { \mu } = x ^ { \mu } ( a , 0 )$ for the initial location of the loop,if $\pmb { d } \pmb { F } = 0$ and ${ \pmb d } ^ { * } { \pmb F } = 0$ (no magnetic charge,no electric charge).

(d) Consider a static,uniform electric field $\pmb { F } = - \pmb { E } _ { z }$ dt ^ dx. Solve the equations, $\langle \pmb { F } , \pmb { \Sigma } \rangle = 0$ and $\langle { } ^ { * } F , { \pmb { \Sigma } } \rangle = 0$ to find the equation $\mathcal { P } ( a , b )$ for the most general calumoid. [Answer: $y = y ( a )$ ， $z = z ( a )$ ， $x = x ( b )$ ， $t = t ( b ) . ]$ Exhibit two special cases:(i)a calumoid thatlies entirely ina hypersurface of constant time [loop moves at infinite velocity;analogous to super-light velocity of point of crossing for two blades of a pair of scissors]; (ii) a calumoid whose loop remains forever at rest in the $t , x , y , z$ Lorentz frame.

# ExerciSe 4.11. DIFFERENTIAL FORMS AND HAMILTONIAN MECHANICS

Consider a dynamic system endowed with two degrees of freedom.For the definition of this system as a Hamiltonian system (special case:here the Hamiltonian is independent of time),one needs(l) a definition of canonical variables (see Box 4.5) and (2) a knowledge of the Hamiltonian $H$ as a function of the coordinates $q ^ { 1 } , q ^ { 2 }$ and the canonically conjugate momenta ${ \pmb p } _ { 1 } , { \pmb p } _ { 2 }$ .To derive the laws of mechanics,consider the five-dimensional space of $p _ { 1 } , p _ { 2 } , q ^ { 1 } , q ^ { 2 }$ ，and $t ,$ and a curve in this space leading from starting values of the five coordinates(subscript $\pmb { A }$ ）to final values (subscript $\pmb { B }$ ,and thevalue

$$
I = \int _ { A } ^ { B } p _ { 1 } d q ^ { 1 } + p _ { 2 } d q ^ { 2 } - H ( p , q ) d t = \int _ { A } ^ { B } \omega
$$

of the integral $I$ taken along this path. The difference of the integral for two“neighboring”paths enclosing a two-dimensional region $s$ ，according to the theorem of Stokes (Boxes 4.1 and 4.6),is

$$
\delta I = \oint _ { \mathcal { I } } \omega = \int _ { s } d \omega .
$$

The principle of least action (principle of “extremal history") states that the representative point of the system must travel along a route in the five-dimensional manifold (route with tangent vector $d \mathcal { P } / d t$ ）such that the variation vanishes for this path: i.e.,

$$
{ \pmb d } { \pmb \omega } ( . . . , d \mathcal { P } / d t ) = 0
$$

(2-form dw with a single vector argument supplied,and other slot left unfilled,gives the l-form in 5-space that must vanish).This fixes only the direction of $d \mathscr { P } / d t$ ; its magnitude can be normalized by requiring $\langle d t , d \vartheta / d t \rangle = 1$

(a) Evaluate dw from the expression $\pmb { \omega } = p _ { j } \pmb { d q } ^ { j } - H \pmb { d t }$ (b)Set $d \vartheta / d t = \dot { q } ^ { j } ( \partial \vartheta / \partial q ^ { j } ) + \dot { p } _ { j } ( \partial \vartheta / \partial p _ { j } ) + \dot { l } ( \partial \vartheta ^ { \prime } / \partial t ) .$ ,and expand $d \pmb { \omega } ( . \dots , d \hat { \mathscr { P } } / d t ) = 0$ in terms of the basis $\{ d p _ { j } , d q ^ { k } , d t \}$

# Box 4.5 METRIC STRUCTURE AND HAMILTONIAN OR "SYMPLECTIC STRUCTURE" COMPARED AND CONTRASTED

<table><tr><td></td><td>Metric structure</td><td>Symplectic structure</td></tr><tr><td>1.Physical application</td><td>Geometry of spacetime</td><td>Hamiltonian mechanics</td></tr><tr><td>2.Canonical structure</td><td>+dxdx+dyd + d: d:</td><td>(.....)=“ds²&quot;= -didi = dp△ dq² + dp△ dq²</td></tr><tr><td>3.Nature of&quot;metric&quot;</td><td>Symmetric</td><td>Antisymmetric</td></tr><tr><td>4.Name for given coordinate system and any other set of four coordinates in which metric has same form</td><td>Lorentz coordinate system</td><td>System of“canonically&quot;(or “dynamically&quot;) conjugate coordinates</td></tr><tr><td>5.Field equation for this metric</td><td>Rμvaβ=O (zero Riemann curvaiure;flat spacetime)</td><td>d0 =0 (&quot;closed 2-form&quot;; condition automatically satisfied by expression above).</td></tr><tr><td>6.The four-dimensional manifold</td><td>Spacetime</td><td>Phase space</td></tr><tr><td>7.Coordinate-free description of the structure of this manifold</td><td>Riemann = 0</td><td>d0 = 0</td></tr><tr><td>8.Canonical coordinates distinguished from other coordinates (allowable but less simple)</td><td>Make metric take above form (item 2)</td><td>Make metric take above form (item 2)</td></tr></table>

(c) Show that this five-dimensional equation can be written in the 4-dimensional phase space of $\{ q ^ { j } , p _ { k } \}$ as

$$
\begin{array} { r } { \pmb { \mathcal { O } } ( . \dots , d \pmb { \mathcal { P } } / d t ) = \pmb { d H } , } \end{array}
$$

where $\pmb { \mathcal { o } }$ is the 2-form defined in Box 4.5.

(d) Show that the components of $\pmb { \mathcal { O } } ( . \dots , d \pmb { \mathcal { P } } / d t ) = \pmb { d H }$ in the $\{ q ^ { j } , p _ { k } \}$ coordinate system are the familiar Hamilton equations.Note that this conclusion depends only on the form assumed for $\pmb { \mathcal { o } }$ ，so that one also obtains the standard Hamilton equations in any other phase-space coordinates $\{ \overline { { q } } ^ { j } , \overline { { p } } _ { k } \}$ ("canonical variables") for which

$$
\mathcal { O } = d \bar { p _ { 1 } } \wedge d \bar { q } ^ { 1 } + d \bar { p _ { 2 } } \wedge d \bar { q } ^ { 2 } .
$$

# Exercise 4.12. SYMMETRY OPERATIONS AS TENSORS

We define the meaning of square and round brackets enclosing a set of indices as follows:

$$
V _ { ( \alpha _ { 1 } . . . \alpha _ { p } ) } \equiv \frac { 1 } { p ! } { \cal { S } } V _ { \alpha _ { \pi _ { 1 } } . . . \alpha _ { \pi _ { p } } } , \qquad V _ { [ \alpha _ { 1 } . . . \alpha _ { p } ] } \equiv \frac { 1 } { p ! } { \cal { \Sigma } } ( - 1 ) ^ { \pi } V _ { \alpha _ { \pi _ { 1 } } . . . \alpha _ { \pi _ { p } } } ,
$$

# Box 4.6 BIRTH OF STOKES' THEOREM

Central to the mathematical formulation of electromagnetism are the theorems of Gauss (taken up in Chapter 5) and Stokes. Both today appear together as one unity when expressed in the language of forms. In earlier times the unity was not evident. Everit (l970) recals the history of Stokes’ theorem: “The Smith’s Prize paper set by [G.C.] Stokes [Lucasian Professor of Mathematics] and taken by Maxwell in [February] 1854...

5. Given the centre and two points of an elipse,and the length of the major axis, find its direction by a geometrical construction.

6.Integrate the differential equation

$$
( a ^ { 2 } - x ^ { 2 } ) d y ^ { 2 } + 2 x y d y d x + ( a ^ { 2 } - y ^ { 2 } ) d x ^ { 2 } = 0 .
$$

Has it a singular solution?

7. In a double system of curves of double curvature,a tangent is always drawn at the variable point $P$ ；shew that, as $P$ moves away from an arbitrary fixed point $\boldsymbol { Q }$ it must begin to move along a generating line of an elliptic cone having $\boldsymbol { Q }$ for vertex in order that consecutive tangents may ultimately intersect, but that the conditions of the problem may be impossible.

8.If $X , ~ Y , ~ Z$ be functions of the rectangular co-ordinates $x , y , z , d S$ an element of any limited surface, $l , m , n$ the cosines of the inclinations of the normal at $d S$ to the axes,ds'an element of the bounding line,shew that

$$
\begin{array} { c l l } { \iint \left\{ l \left( \frac { d Z } { d y } - \frac { d Y } { d z } \right) + m \left( \frac { d X } { d z } - \frac { d Z } { d x } \right) + n \left( \frac { d Y } { d x } - \frac { d X } { d y } \right) \right\} d S } \\ { \qquad = \int \left( X \frac { d x } { d s } + Y \frac { d y } { d s } + Z \frac { d z } { d s } \right) d s , } \end{array}
$$

the differential coefficients of $X , Y , Z$ being partial,and the single integral being taken all round the perimeter of the surface

marks the first appearance in print of the formula connecting line and surface integrals now known as Stokes’ theorem. This was of great importance to Maxwell's development of electromagnetic theory. The earliest explicit proof of the theorem appears to be that given in a letter from Thomson to Stokes dated July 2, 1850." [Quoted in Campbell and Garnett (1882), p.186-187.]

Here the sum is taken over all permutations $\pi$ of the numbers $1 , 2 , \ldots , p$ and $( - 1 ) ^ { \pi }$ is $+ 1$ or $^ { - 1 }$ depending on whether the permutation is even or odd.The quantity $V$ may have other indices,not shown here,besides the set of $\pmb { p }$ indices $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { p } ,$ but only this set of indices is affected by the operations described here. The numbers $\pi _ { 1 } , \pi _ { 2 } , \ldots , \pi _ { p }$ are the numbers $1 , 2 , \ldots , p$ rearranged according to the permutation $\pi$ $( \mathsf { C a s e s } p = 2$ ,3 were treated in exercise 3.l2.)We therefore have machinery to convert any rank $\boldsymbol { p }$ te nsor with components Va1.ap into a new tensor with components

$$
[ A I t ( V ) ] _ { \mu _ { 1 } . . . \mu _ { p } } = V _ { [ \mu _ { 1 } . . . \mu _ { p } ] } .
$$

Since this machinery Alt is linear,it can be viewed as a tensor which,given suitable arguments $\pmb { u } , \pmb { v } , \dots , \pmb { w } , \pmb { \alpha } , \pmb { \beta } , \dots , \pmb { \gamma }$ produces a number

$$
u ^ { \mu } v ^ { \nu } \ldots w ^ { \lambda } \alpha _ { [ \mu } \beta _ { \nu } \ldots \gamma _ { \lambda ] } .
$$

(a) Show that the components of this tensor are

$$
( { \pmb A } { \pmb I } { \pmb t } ) _ { \beta _ { 1 } . . . \beta _ { p } } { } ^ { \alpha _ { 1 } . . . \alpha _ { p } } = ( p ! ) ^ { - 1 } \delta _ { \beta _ { 1 } . . . \beta _ { p } } ^ { \alpha _ { 1 } . . . \alpha _ { p } }
$$

(Note: indices of δ are almost never raised or lowered,so this notation leads to no confusion.)

where

Note that the demonstration,and therefore these component values, are corrct in any frame.

(b)Sowforaleti"("ceelyis $A _ { \alpha _ { 1 } . . . \alpha _ { p } } = A _ { [ \alpha _ { 1 } . . . \alpha _ { p } ] }$ that

$$
{ \begin{array} { r l } & { { \frac { 1 } { p ! } } A _ { \alpha _ { 1 } \dots \alpha _ { p } } \delta _ { \gamma _ { 1 } \dots \gamma _ { p } \gamma _ { p + 1 } \dots \gamma _ { p + q } } ^ { \alpha _ { 1 } \dots \alpha _ { p } \beta _ { 1 } \dots \beta _ { q } } } \\ & { \qquad = \quad \sum _ { \alpha _ { 1 } < \alpha _ { 2 } < \dots < \alpha _ { p } } A _ { \alpha _ { 1 } \dots \alpha _ { p } } \delta _ { \gamma _ { 1 } \dots \dots \dots \dots \dots \gamma _ { p + q } } ^ { \alpha _ { 1 } \dots \alpha _ { p } \beta _ { 1 } \dots \beta _ { q } } } \\ & { \qquad \equiv A _ { | \alpha _ { 1 } \dots \alpha _ { p } | } \delta _ { \gamma _ { 1 } \dots \dots \dots \dots \gamma _ { p + q } } ^ { \alpha _ { 1 } \dots \alpha _ { p } \beta _ { 1 } \dots \beta _ { q } } . } \end{array} }
$$

The final line here introduces the convention that a summation over indices enclosed between vertical bars includes only terms with those indices in increasing order. Show,consequently or similarly,that

$$
\delta _ { \gamma _ { 1 } \ldots \ldots \ldots \ldots \gamma _ { p } } ^ { \alpha _ { 1 } \ldots \alpha _ { p } \beta _ { 1 } \ldots \beta _ { q } } \delta _ { | \beta _ { 1 } \ldots \beta _ { q } | } ^ { \mu _ { 1 } } = \delta _ { \gamma _ { 1 } \ldots \ldots \ldots \ldots \ldots \gamma _ { p + q } } ^ { \alpha _ { 1 } \ldots \alpha _ { p } \mu _ { 1 } \ldots \mu _ { q } } .
$$

(c) Define theexterior("wedge") product ofanytwoalternating tensors by

$$
( \alpha \wedge \beta ) _ { \lambda _ { 1 } . . . \lambda _ { p + q } } = \delta ^ { \mu _ { 1 } . . . \mu _ { p } } _ { \lambda _ { 1 } . . . \lambda _ { p } \lambda _ { p + 1 } . . . \lambda _ { p + q } } \alpha _ { | \mu _ { 1 } . . . \mu _ { p } | } \beta _ { | \nu _ { 1 } . . . \nu _ { q } | } ;
$$

and similarly

$$
( \pmb { U } \wedge \pmb { V } ) ^ { \lambda _ { 1 } \ldots \lambda _ { p + q } } = \delta ^ { \lambda _ { 1 } \ldots \lambda _ { p } \lambda _ { p + 1 } \ldots \lambda _ { p + q } } U ^ { | \mu _ { 1 } \ldots \mu _ { p } | } V ^ { | \nu _ { 1 } \ldots \nu _ { q } | } .
$$

Show that this implies equation (3.45b). Establish the associative law for this product rule by showing that

$$
\begin{array} { l } { { \{ ( \pmb { \alpha } \wedge \pmb { \beta } ) \wedge \pmb { \gamma } \} _ { \sigma _ { 1 } . . . \sigma _ { p + q + \tau } } } } \\ { { = \delta ^ { \lambda _ { 1 } . . . \lambda _ { p } \mu _ { 1 } . . . \mu _ { q } \nu _ { 1 } . . . \nu _ { r \alpha _ { | \lambda _ { 1 } . . . \lambda _ { p } | } } \beta _ { | \mu _ { 1 } . . . \mu _ { q } | } \gamma _ { | \nu _ { 1 } . . . \nu _ { r } | } } } } \\ { { = \{ \pmb { \alpha } \wedge ( \pmb { \beta } \wedge \pmb { \gamma } ) \} _ { \sigma _ { 1 } . . . \sigma _ { p + q + \tau } } ; } } \end{array}
$$

and show that this reduces to the 3-form version of Equation (3.45c) when ${ \pmb \alpha } , { \pmb \beta }$ and $\pmb { \gamma }$ are all 1-forms.

(d) Derive the following formula for the components of the exterior product of $p$ vectors

$$
\begin{array} { r l r } & { } & { ( \pmb { u } _ { 1 } \wedge \pmb { u } _ { 2 } \wedge \dots \wedge \pmb { u } _ { p } ) ^ { \alpha _ { 1 } \dots \alpha _ { p } } = \delta _ { \mu \dots \pmb { \nu } } ^ { \alpha _ { 1 } \dots \alpha _ { p } } ( u _ { 1 } ) ^ { \mu } \cdot \cdot \cdot ( u _ { p } ) ^ { \nu } } \\ & { } & { \qquad = p ! u _ { 1 } ^ { \quad [ \alpha _ { 1 } } u _ { 2 } ^ { \alpha _ { 2 } } \cdot \cdot \cdot \cdot u _ { p } ^ { \alpha _ { p } ] } } \\ & { } & { \qquad = \delta _ { \mathrm { ~ 1 ~ 2 ~ } \dots \pmb { p } } ^ { \alpha _ { 1 } \alpha _ { 2 } \dots \alpha _ { p } } \operatorname* { d e t } \{ ( u _ { \mu } ) ^ { \lambda } \} . } \end{array}
$$
