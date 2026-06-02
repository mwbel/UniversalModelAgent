# Chapter 14. Lee-Variational Integrator

In the 1980s, Lee proposed an energy-preserving discrete mechanics with variable time steps by taking time (discrete) as a dynamical variable [Lee82,Lee87] . On the other hand, motivated by the symplectic property of Lagrangian mechanics, a version of discrete Lagrangian mechanics has been developed and variational integrators that preserve discrete symplectic 2-form have been obtained [MPS98,MV91,Ves88,Ves91a,WM97] , but variational integrators obtained in this way fix the time steps and consequently, they are not energy-preserving in general.

Obviously, energy-preserving discrete mechanics and variational integrators are more preferable, since solutions of the Euler–Lagrange equations of conservative continuous systems are not only symplectic but also energy-preserving. To attain this goal, we should study some discrete mechanics with discrete energy conservation and symplectic variational integrators. Recently, Kane, Marsden, and Ortiz have employed appropriate time steps to conserve a defined energy and developed what they called symplectic energy-momentum-preserving variational integrators in [KMO99] . Although their approach is more or less related to Lee’s discrete mechanics, the discrete energypreserving condition is not derived by the variational principle.

# 14.1 Total Variation in Lagrangian Formalism

The purpose of this section is to generalize or improve the above mentioned approaches as well as to explore the relations among discrete total variation, Lee’s discrete mechanics, and Kane–Marsden–Ortiz integrators. We will present a discrete total variation calculus with variable time steps and a discrete mechanics that is discretely symplectic, energy-preserving and has the correct continuous limit. In fact, this discrete variation calculus and mechanics is a generalization of Lee’s discrete mechanics in symplectic-preserving sense and can derive directly the variational symplecticenergy-momentum integrators of Kane, Marsden, and Ortiz.

# 14.1.1 Variational Principle in Lagrangian Mechanics

Before beginning this section, we will recall very briefly the ordinary variational principle in Lagrangian mechanics for later use. Suppose $Q$ denotes the extended configuration space with coordinates $( t , q ^ { i } )$ and $Q ^ { ( 1 ) }$ the first prolongation of $Q$ with

coordinates $( t , q ^ { i } , \dot { q } ^ { i } ) ^ { [ \mathrm { O l v } 9 3 ] }$ . Here $t$ denotes time and $q ^ { i } ( i = 1 , 2 , \cdot \cdot \cdot , n )$ denote the positions. Consider a Lagrangian $L \colon Q ^ { ( 1 ) } \to \mathbb { R }$ . The corresponding action functional is defined by

$$
S ( q ^ { i } ( t ) ) = \int _ { a } ^ { b } L ( t , q ^ { i } ( t ) , \dot { q } ^ { i } ) \mathrm { d } t ,
$$

where $q ^ { i } ( t )$ is a $C ^ { 2 }$ curve in $Q$ .

Hamilton’s principle seeks a curve $q ^ { i } ( t )$ denoted by $C _ { a } ^ { b }$ with endpoints $a$ and $b$ , for which the action functional $S$ is stationary under variations of $q ^ { i } ( t )$ with fixed endpoints. Let

$$
V = \phi ^ { i } ( t , q ) \frac { \partial } { \partial q ^ { i } }
$$

be a vertical vector field on $Q$ , here $q = ( q ^ { 1 } , \cdots , q ^ { n } )$ . By a vertical vector field we mean a vector field on $Q$ which does not involve terms of form $\xi ( t , q ) \frac { \partial } { \partial t }$ , for example, time $t$ does not undergo variation.

Let $F ^ { \varepsilon }$ be the flow of $V$ , i.e., a one-parameter group of transformations on $Q :$ $F ^ { \varepsilon } ( t , q ^ { i } ) = ( \tilde { t } , \tilde { q } ^ { i } )$ .

$$
\begin{array} { c } { { \tilde { t } ~ = ~ t , } } \\ { { \tilde { q } ^ { i } ~ = ~ g ^ { i } ( \varepsilon , t , q ) , } } \end{array}
$$

where

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , t , q ) = \phi ^ { i } ( t , q ) : = \delta q ^ { i } ( t ) .
$$

In other words, the deformation (1.3) – (1.4) transforms the curve $q ^ { i } ( t )$ into a family of curves $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ in $Q$ denoted by $C _ { \varepsilon _ { a } } ^ { b }$ which are determined by

$$
\begin{array} { r c l } { { \displaystyle \tilde { t } ~ = ~ t , } } \\ { { \tilde { q } ^ { i } ~ = ~ g ^ { i } ( \varepsilon , t , q ( t ) ) . } } \end{array}
$$

Thus, we obtain a (sufficiently small) set of curves $\mathcal { C } _ { \varepsilon _ { a } } ^ { b }$ around $ { \mathcal { C } } _ { a } ^ { b }$ . Corresponding to athis set of curves there is a set of Lagrangian and action functionals

$$
S ( q ^ { i } ( t ) ) \longrightarrow S ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) ) = \int _ { a } ^ { b } L ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) ) \mathrm { d } \tilde { t } .
$$

Now, we can calculate the variation of $S$ at $q ( t )$ as follows:

$$
\begin{array} { l } { \delta S = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } S ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) ) } \\ { = \left. \int _ { a } ^ { b } \left[ \left( \frac { \partial L } { \partial q ^ { i } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } ^ { i } } \right) \phi ^ { i } \right] \mathrm { d } t + \frac { \partial L } { \partial \dot { q } ^ { i } } \phi ^ { i } \right| _ { a } ^ { b } . } \end{array}
$$

For the fixed endpoints, $\phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0$ , the requirement of Hamilton’s principle, $\delta S = 0$ , yields the Euler–Lagrange equation for $q ( t )$

$$
{ \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } = 0 .
$$

If we drop the requirement of $\phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0$ , we can naturally obtain the Lagrangian 1-form on $Q ^ { ( 1 ) }$ from the second term in (1.9):

$$
\theta _ { L } = \frac { \partial L } { \partial \dot { q } ^ { I } } { \bf d } q ^ { i } ,
$$

where $\mathrm { d } q ^ { i }$ are dual to $\frac { \partial } { \partial q ^ { j } } , { \bf d } q ^ { i } \biggl ( \frac { \partial } { \partial q ^ { j } } \biggr ) = \delta _ { j } ^ { i }$ . Furthermore, it can be proved that the solution of (1.10) preserves the Lagrangian 2-form

$$
\omega _ { L } : = \mathrm { d } \theta _ { L } .
$$

On the other hand, introducing the Euler–Lagrange 1-form

$$
E ( q ^ { i } , \dot { q } ^ { i } ) = \left\{ \frac { \partial L } { \partial q ^ { i } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } ^ { i } } \right\} \mathrm { d } q ^ { i } ,
$$

the nilpotency of ${ \mathrm { d } }$ leads to

$$
\mathrm { d } E ( q ^ { i } , \dot { q } ^ { i } ) + \frac { \mathrm { d } } { \mathrm { d } t } \omega _ { L } = 0 ,
$$

namely, the necessary and sufficient condition for symplectic structure preserving is that the Euler–Lagrange 1-form is closed[GLW01a,GLWW01,GW03] .

# 14.1.2 Total Variation for Lagrangian Mechanics

Consider a general vector field on $Q$

$$
V = \xi ( t , q ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , q ) \frac { \partial } { \partial q ^ { i } } ,
$$

here $q = ( q ^ { 1 } , \cdots , q ^ { n } )$ . Let $F ^ { \varepsilon }$ be the flow of $V$ . The variations of $( t , q ^ { i } ) \in Q$ are described in such a way

$$
( t , q ^ { i } ) \longrightarrow F ^ { \varepsilon } ( t , q ^ { i } ) = ( \tilde { t } , \tilde { q } ^ { i } ) ,
$$

where

$$
\tilde { t } = f ( \varepsilon , t , q ) , \quad \tilde { q } ^ { i } = g ^ { i } ( \varepsilon , t , q )
$$

with

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big | _ { \varepsilon = 0 } f ( \varepsilon , t , q ) = \xi ( t , q ) : = \delta t , \quad \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big | _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , t , q ) = \phi ^ { i } ( t , q ) : = \delta q ^ { i } .
$$

The dcurves (1.17) transfdenoted by a curve , determi $q ^ { i } ( t )$ $Q$ denoted by $ { \mathcal { C } } _ { a } ^ { b }$ into a set of $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ $Q$ $\mathcal { C } _ { \varepsilon _ { \tilde { a } } } ^ { \tilde { b } }$

$$
\tilde { t } = f ( \varepsilon , t , q ( t ) ) , \quad \tilde { q } ^ { i } = g ^ { i } ( \varepsilon , t , q ( t ) ) .
$$

Before calculating the total variation of $S$ , we will introduce the first-order prolongation of $V$ denoted as $\mathrm { p r } ^ { 1 } V$

$$
\mathrm { p r } ^ { 1 } V = \xi ( t , q ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , q ) \frac { \partial } { \partial q ^ { i } } + \alpha ^ { i } ( t , q , \dot { q } ) \frac { \partial } { \partial \dot { q } ^ { i } } ,
$$

here

$$
\alpha ^ { i } ( t , q , \dot { q } ) = D _ { t } \phi ^ { i } ( t , q ) - \dot { q } ^ { i } D _ { t } \xi ( t , q ) ,
$$

where $D _ { t }$ denotes the total derivative with respect to $t$ , for example,

$$
D _ { t } \phi ^ { k } ( t , q ^ { i } ) = \phi _ { t } ^ { k } + \phi _ { q ^ { i } } ^ { k } \dot { q } ^ { i } , \quad \phi _ { t } ^ { k } = \frac { \partial \phi ^ { k } } { \partial t } .
$$

For prolongations of the vector field and the related formulae, refer to $[ \mathrm { O l v 9 3 } ]$

Now, we let us calculate the total variation of $S$ straightforwardly:

$$
\begin{array} { r l } { \delta S = } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } S ( \bar { \theta } ^ { + } ( \varepsilon , \tilde { t } ) ) - \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \int _ { \partial _ { \varepsilon } } ^ { \tilde { t } } \Big [ \bar { \epsilon } \big ( \bar { t } , \bar { \varphi } ^ { + } , \tilde { t } \big ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) \Big ) \mathrm { d } \tilde { t } } \\ { = } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \int _ { a } ^ { \tilde { t } } L \Big ( \bar { t } , \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) \Big ) \frac { \mathrm { d } \tilde { t } } { \mathrm { d } \tilde { t } } \mathrm { d } t \ \qquad \ \bar { \hat { \varepsilon } } \bar { t } = f ( \varepsilon , t , q ( t ) ) \big ) } \\ { = } & { \int _ { a } ^ { \tilde { y } } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } L \Big ( \bar { t } , \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) \Big ) \mathrm { d } t + \int _ { a } ^ { b } L ( t , q ^ { i } ( t ) , i ^ { * } ( t ) ) D _ { i } \xi \mathrm { d } t } \\ { = } & { \int _ { a } ^ { \tilde { y } } \Big [ \frac { \partial L } { \partial \varepsilon } \varepsilon + \frac { \partial L } { \partial \tilde { t } } \bar { \varphi } ^ { i } + \frac { \partial L } { \partial \tilde { t } ^ { i } } ( D _ { i } \phi ^ { i } - \bar { q } ^ { i } D _ { i } \xi ) \Big ] \mathrm { d } t + \int _ { a } ^ { b } L D _ { i } \xi \mathrm { d } t } \\ { = } &  \int _ { a } ^ { \tilde { y } } \Big [ \Big ( \frac { \partial L } { \partial \tilde { t } } + \frac { \partial L } { \mathrm { d } \varepsilon } \Big ( \frac  \partial L  \end{array}
$$

Here we have made use of (1.18), (1.20), (1.21) and

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \frac { \mathrm { d } \tilde { t } } { \mathrm { d } t } = \frac { \mathrm { d } } { \mathrm { d } t } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \tilde { t } = D _ { t } \xi .
$$

If $\xi ( a , q ( a ) ) = \xi ( b , q ( b ) ) = 0$ and $\phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0$ , the requirement of $\delta S = 0$ yields the equation from $\xi$ , the variation along the base manifold, i.e., the time.

$$
{ \frac { \partial L } { \partial t } } + { \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \dot { q } } ^ { i } - L \right) = 0 ,
$$

and the Euler–Lagrange equation from $\phi ^ { i }$ , the variation along the fiber, i.e., the configuration space,

$$
{ \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } = 0 .
$$

Here $\xi$ and $\phi ^ { i }$ are regarded as independent components of total variation. However, there is another decomposition for the independent components, i.e., the vertical and horizontal variations; see Remark1.2 below.

If $L$ does not depend on $t$ explicitly, i.e., $L$ is conservative, $\frac { \partial L } { \partial t } = 0$ , then (1.23) becomes the energy conservation law

$$
\frac { \mathrm { d } } { \mathrm { d } t } H = 0 , H : = \Bigl ( \frac { \partial L } { \partial \dot { q } ^ { i } } \dot { q } ^ { i } - L \Bigr ) .
$$

By expanding the left-hand side of (1.25), we obtain

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \dot { q } } ^ { i } - L \right) = - \left( { \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } \right) { \dot { q } } ^ { i } .
$$

Thus, for a conservative $L$ , energy conservation is a consequence of Euler–Lagrange equation. This agrees with Noether theorem which states that the characteristic of an infinitesimal symmetry of the action functional $S$ is that of a conservation law for the Euler–Lagrange equation. For a conservative $L$ , $\frac { \partial } { \partial t }$ is an infinitesimal symmetry of the action functional $S$ , and its characteristic is $- \dot { q } ^ { i }$ . From Noether theorem, there exits a corresponding conservation law in the characteristic form

$$
- \left( { \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } \right) { \dot { q } } ^ { i } = 0 .
$$

If we drop the requirement

$$
\xi ( a , q ( a ) ) = \xi ( b , q ( b ) ) = 0 , \phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0 ,
$$

we can define the extended Lagrangian 1-form on $Q ^ { ( 1 ) }$ from the second term in (1.22)

$$
\vartheta _ { L } : = \left( L - { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \dot { q } } ^ { i } \right) { \mathsf { d } } t + { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \mathsf { d } } q ^ { i } .
$$

Suppose $g ^ { i } ( t , v _ { q ^ { i } } )$ is a solution of (1.24) depending on the initial condition $v _ { q ^ { i } } \in Q ^ { ( 1 ) }$ . Restricting $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ to the solution space of (1.24) and using the same method $\mathrm { i n } ^ { \mathrm { [ M P S 9 8 ] } }$ , it can be proved that the extended symplectic 2-form is preserved:

$$
( \mathrm { p r } ^ { 1 } g ^ { i } ) ^ { * } \Omega _ { L } = \Omega _ { L } , \quad \Omega _ { L } : = \mathrm { d } \vartheta _ { L } ,
$$

where $\operatorname { p r } ^ { 1 } g ^ { i } ( s , v _ { q ^ { i } } ) = { \Big ( } s , g ^ { i } ( s , v _ { q ^ { i } } ) , { \frac { \mathrm { d } } { \mathrm { d } s } } g ^ { i } ( s , v _ { q ^ { i } } ) { \Big ) }$ denotes the first-order prolonga-$g ^ { i } ( s , v _ { q ^ { i } } ) ^ { [ \mathrm { O l v } 9 3 ] }$

Remark 1.1. If $\xi$ in (1.15) is independent of $q$ , the deformations in (1.17) are called fiber-preserving. In this case, the domain of definition of $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ only depends on the deformations in (1.17). While in the general case, the domain of definition of $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ depends on not only the deformations in (1.17) but also on $q ^ { i } ( t )$ .

Remark 1.2. Using the identity

$$
\frac { \partial L } { \partial t } + \frac { \mathrm { d } } { \mathrm { d } t } \left( \frac { \partial L } { \partial \dot { q } ^ { i } } \dot { q } ^ { i } - L \right) = - \left( \frac { \partial L } { \partial q ^ { i } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } ^ { i } } \right) \dot { q } ^ { i } ,
$$

the Equation (1.22) becomes

$$
\delta S = \int _ { a } ^ { b } \left( { \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } \right) ( \phi ^ { i } - \xi { \dot { q } } ^ { i } ) \mathrm { d } t + \left[ { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } ( \phi ^ { i } - \xi { \dot { q } } ^ { i } ) \right] { \Big | } _ { a } ^ { b } + ( L \xi ) { \Big | } _ { a } ^ { b } .
$$

According to (1.18), $\phi ^ { i } = \delta q ^ { i }$ should be regarded as the total variation of $q ^ { i } , \delta q ^ { i } =$ $\delta _ { V } q ^ { i } + \delta _ { H } q ^ { i }$ , since the variation of $t$ also induces the variation of $q ^ { i }$ , denoted as $\delta _ { H } q ^ { i }$ , the horizontal variation of $q ^ { i }$ . Substituting $\xi = \delta t$ in (1.18), the horizontal variation of $q ^ { i }$ should be $\delta _ { H } q ^ { i } = \xi \dot { q } ^ { i }$ , and consequently $\phi ^ { i } - \xi \dot { q } ^ { i }$ is interpreted as vertical variation $\delta _ { V } q ^ { i }$ , i.e., the variation of $q ^ { i } ( t )$ at the moment $t$ (for e.g., $\mathrm { s e e } ^ { \left[ \mathrm { C H } 5 3 \right] } ,$ . Therefore, the first two terms in (1.32) come from vertical variation $\delta _ { V } q ^ { i }$ and the last term comes from horizontal variation $\delta t$ . The horizontal variation of $S$ with respect to the horizontal variation $\delta _ { H } q ^ { i } = \xi \dot { q } ^ { i }$ gives rise to the identity (1.31).

# 14.1.3 Discrete Mechanics and Variational Integrators

In this subsection, by calculus of discrete total variations, we will develop a discrete Lagrangian mechanics, which includes the boundary terms in Lee’s discrete mechanics that give rise to the discrete version of symplectic preserving. The discrete variation calculus is mainly analog to Lee’s idea that time (discrete) is regarded as a dynamical variable, i.e., the time steps are variable[Lee82,Lee87] . The vertical part of this discrete variation calculus is similar to the one $\mathrm { i n } ^ { [ \mathrm { K M O 9 9 , M V 9 1 , V e s 8 8 , V e s 9 1 a , W \bar { M } 9 7 } ] }$ . Using this calculus for discrete total variations we naturally derive the Kane–Marsden–Ortiz integrators.

We use $Q \times Q$ to denote the discrete version of the first prolongation for the extended configuration space $Q$ . A point $( t _ { 0 } , q _ { 0 } ; t _ { 1 } , q _ { 1 } ) \in Q \times Q ^ { \ 1 }$ , corresponds to a tangent vector $\frac { q _ { 1 } - q _ { 0 } } { t _ { 1 } - t _ { 0 } }$ . A discrete Lagrangian is defined to be $\mathbb { L } : Q \times Q \to \mathbb { R }$ and the corresponding action as

$$
\mathbb { S } = \sum _ { k = 0 } ^ { N - 1 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) .
$$

The discrete variational principle in total variation is to extremize $\mathbb { S }$ for variations of both $q _ { k }$ and $t _ { k }$ with fixed end points $( t _ { 0 } , q _ { 0 } )$ and $( t _ { N } , q _ { N } )$ . This discrete variational principle determines a discrete flow $\Phi : Q \times Q \to Q \times Q$ by

$$
\Phi ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) = ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) .
$$

Here $( t _ { k + 1 } , q _ { k + 1 } )$ are calculated from the following discrete Euler–Lagrange equation, i.e., the variational integrator, and the discrete energy conservation law (for conservative L)

$$
( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) + ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) = 0 ,
$$

and

$$
\begin{array} { r l } & { ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) + D _ { 3 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) ( t _ { k } - t _ { k - 1 } ) } \\ & { - \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) + \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) = 0 , } \end{array}
$$

for all $k \in \{ 1 , 2 , \cdots , N - 1 \}$ . Here $D _ { i }$ denotes the partial derivative of $\mathbb { L }$ with respect to the $i$ -th argument. The Equation (1.35) is the discrete Euler–Lagrange equation. The Equation (1.36) is the discrete energy conservation law for a conservative $\mathbb { L }$ . The integrator $( 1 . 3 5 ) - ( 1 . 3 6 )$ is the Kane–Marsden–Ortiz integrator.

Using the discrete flow $\Phi$ , the Equations (1.35) and (1.36) become

$$
\begin{array} { r } { ( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } \circ \Phi + ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } = 0 , } \\ { ( ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } - \mathbb { L } ) \circ \Phi + D _ { 3 } \mathbb { L } + \mathbb { L } = 0 , } \end{array}
$$

respectively. If $( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L }$ and $( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } - \mathbb { L }$ are invertible, the Equations (1.37) and (1.38) determine the discrete flow $\Phi$ under the consistency condition

$$
( ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } - \mathbb { L } ) ^ { - 1 } \circ ( D _ { 3 } \mathbb { L } + \mathbb { L } ) = ( ( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } ) ^ { - 1 } \circ ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } .
$$

Now, we will prove that the discrete flow $\Phi$ preserves a discrete version of the extended Lagrange 2-form $\Omega _ { L }$ . As in continuous case, we will calculate $\mathrm { d } \mathbb { S }$ for variations with variable end points.

$$
\begin{array} { r l } &  \begin{array} { r l } &  \mathrm { d } \mathcal { E } ( \xi , \theta , \eta ^ { * } , \theta , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ \end{array} \end{array}
$$

$$
\begin{array} { r l } {  { \sum _ { i = 1 } ^ { N - 1 } L ( \{ k _ { i } , q _ { i } , q _ { i } , \} , \phi _ { i \neq 1 } ) ( - \delta \{ k _ { i } \} ) \Big ( \delta + \sum _ { i = 1 } ^ { N } \mathcal { L } \{ ( k _ { i - 1 } , q _ { i - 1 } , t _ { i } , q _ { i } ) \} \delta \{ k _ { i } \} } } \\ &  + \sum _ { i = 1 } ^ { N - 1 } ( D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i + 1 } \} ) ( \delta + k _ { i } ) \mathbb { \} ) } \\ & { = \sum _ { i = 1 } ^ { N } ( D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i + 1 } \} ) ( \delta + k _ { i } ) } \\ & { + D _ { i } L ( \{ k _ { i - 1 } , q _ { i } , t _ { i } , q _ { i } \} ) ( \delta - k _ { i } - \{ k _ { i } \} ) ) \delta _ { \emptyset \mathcal { K } } } \\ & { + \sum _ { i = 1 } ^ { N } ( D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i + 1 } \} ) ( \delta + k _ { i + 1 } - \{ k _ { i } \} ) } \\ & { + D _ { i } L ( \{ k _ { i - 1 } , q _ { i - 1 } , t _ { i } , q _ { i } \} ) ( \delta - k _ { i } - \{ k _ { i } \} ) ) } \\ & { + D _ { i } L ( \{ k _ { i - 1 } , q _ { i - 1 } , t _ { i } , q _ { i } \} ) ( \delta - k _ { i } - \{ k _ { i } \} ) \delta ( k _ { i } - \delta ) ) ( \delta \{ k _ { i } \} } \\ & { + D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i } \} ) ( \delta - k _ { i } ) \delta _ { \emptyset \mathcal { K } } } \\ & { + D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i } \} ) ( \delta - k _ { i } ) \delta _ { \emptyset \mathcal { K } } + D _ { i } \{ ( k _ { i } , q _ { i - 1 } , q _ { i } ) \} \delta _ { \mathcal { K } } } \\ &  + D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i } \} ) ( \delta - k _ \end{array}
$$

We can see that the last four terms in (1.40) come from the boundary variations. Based on the boundary variations, we can define two 1-forms on $Q \times Q$

$$
\begin{array} { r l } & { \theta _ { \mathbb { L } } ^ { - } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) } \\ & { = ( D _ { 1 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ) \mathrm { d } t _ { k } } \\ & { \quad + D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \theta _ { \mathbb { L } } ^ { + } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) } \\ & { = ( D _ { 3 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) + \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ) \mathrm { d } t _ { k + 1 } } \\ & { \quad + D _ { 4 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k + 1 } , } \end{array}
$$

having employed the notations in $\left[ \mathrm { M P S 9 8 } \right]$ . We regard the pair $( \theta _ { \mathbb { L } } ^ { - } , \theta _ { \mathbb { L } } ^ { + } )$ as the discrete version of the extended Lagrange 1-form $\vartheta _ { \mathbb { L } }$ defined in (1.29).

Now, we parameterize the solutions of the discrete variational principle by the initial condition $( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } )$ and restrict $\mathbb { S }$ to that solution space. Then Equation (1.40) becomes

$$
\begin{array} { r l } & { \mathrm { d } \mathbb { S } \big ( t _ { 0 } , q _ { 0 } , \cdot \cdot \cdot , t _ { N } , q _ { N } \big ) \cdot \big ( \delta t _ { 0 } , \delta q _ { 0 } , \cdot \cdot \cdot , \delta t _ { N } , \delta q _ { N } \big ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } \big ( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } \big ) \cdot \big ( \delta t _ { 0 } , \delta q _ { 0 } , \cdot \delta t _ { 1 } , \delta q _ { 1 } \big ) } \\ & { \quad + \theta _ { \mathbb { L } } ^ { + } \big ( t _ { N - 1 } , q _ { N - 1 } , t _ { N } , q _ { N } \big ) \cdot \big ( \delta t _ { N - 1 } , \delta q _ { N - 1 } , \delta t _ { N } , \delta q _ { N } \big ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } \big ( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } \big ) \cdot \big ( \delta t _ { 0 } , \delta q _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } \big ) } \\ & { \quad + \big ( \Phi ^ { N - 1 } \big ) ^ { * } \theta _ { \mathbb { L } } ^ { + } \big ( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } \big ) \big ( \delta t _ { 0 } , \delta q _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } \big ) . } \end{array}
$$

From (1.43), we obtain

$$
\begin{array} { r } { \mathtt { d } \mathbb { S } = \theta _ { \mathbb { L } } ^ { - } + ( \Phi ^ { N - 1 } ) ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

The Equation (1.44) holds for arbitrary $N > 1$ . By taking $N = 2$ , we get

$$
\begin{array} { r } { \mathrm { d } \mathbb { S } = \theta _ { \mathbb { L } } ^ { - } + \Phi ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

By exterior differentiation of (1.45), we obtain

$$
\Phi ^ { * } ( { \bf d } \theta _ { \mathbb { L } } ^ { + } ) = - { \bf d } \theta _ { \mathbb { L } } ^ { + } .
$$

From the definition of $\theta _ { \mathbb { L } } ^ { - }$ and $\theta _ { \mathbb { L } } ^ { + }$ , we know that

$$
\theta _ { \mathbb { L } } ^ { - } + \theta _ { \mathbb { L } } ^ { + } = { \bf d } \left( \mathbb { L } ( t _ { k + 1 } - t _ { k } ) \right) .
$$

By exterior differentiation of (1.47), we obtain $1 \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - }$ . Define

$$
\Omega _ { \mathbb { L } } \equiv { \bf d } \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - } .
$$

Finally, we have shown that the discrete flow $\Phi$ preserves the discrete extended Lagrange 2-form $\Omega _ { \mathbb { L } }$

$$
\Phi ^ { * } ( \Omega _ { \mathbb { L } } ) = \Omega _ { \mathbb { L } } .
$$

Now, the variational integrator (1.35), the discrete energy conservation law (1.36), and the discrete extended Lagrange 2-form $\Omega _ { \mathbb { L } }$ converge to their continuous counterparts as $t _ { k + 1 } \to t _ { k } , t _ { k - 1 } \to t _ { k }$ .

Consider a conservative Lagrangian $L ( q , \dot { q } )$ . For simplicity, we choose the discrete Lagrangian as

$$
\mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) = L \left( q _ { k } , \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) .
$$

The variational integrator (1.35) becomes

$$
\frac { \partial L } { \partial q _ { k } } ( q _ { k } , \Delta _ { t } q _ { k } ) - \frac { 1 } { t _ { k + 1 } - t _ { k } } \left( \frac { \partial L } { \partial \Delta _ { t } q _ { k } } ( q _ { k } , \Delta _ { t } q _ { k } ) - \frac { \partial L } { \partial \Delta _ { t } q _ { k - 1 } } ( q _ { k - 1 } , \Delta _ { t } q _ { k - 1 } ) \right) = 0 ,
$$

where $\Delta _ { t } q _ { k } = \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } }$ qk+1 − qk , Δtqk 1 = $\Delta _ { t } q _ { k - 1 } = \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } }$

It is easy to see that, as $t _ { k + 1 } \to t _ { k }$ , $t _ { k - 1 } \to t _ { k }$ , the Equation (1.51) converges to

$$
\frac { \partial L } { \partial q _ { k } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } _ { k } } = 0 .
$$

The discrete energy conservation law (1.36) becomes

$$
{ \frac { E _ { k + 1 } - E _ { k } } { t _ { k + 1 } - t _ { k } } } = 0 ,
$$

where

$$
\begin{array} { l } { { \displaystyle E _ { k + 1 } = \frac { \partial L } { \partial \Delta _ { t } q _ { k } } \Delta _ { t } q _ { k } - L \left( q _ { k } , \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) , } } \\ { { \displaystyle E _ { k } = \frac { \partial L } { \partial \Delta _ { t } q _ { k - 1 } } \Delta _ { t } q _ { k - 1 } - L \left( q _ { k - 1 } , \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) . } } \end{array}
$$

The Equation (1.53) converges to

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \frac { \partial L } { \partial { \dot { q } } _ { k } } } { \dot { q } } _ { k } - L \right) = 0
$$

as $t _ { k + 1 } \to t _ { k }$ , $t _ { k - 1 } \to t _ { k }$ .

Now, we will consider the discrete extended Lagrange 2-form $\Omega _ { \mathbb { L } }$ defined by (1.48). By discretization of (1.50), the discrete extended Lagrange 1-form $\theta _ { \mathbb { L } } ^ { + }$ defined in (1.42) becomes

$$
\theta _ { \mathbb { L } } ^ { + } = \left( L ( q _ { k } , \Delta _ { t } q _ { k } ) - \frac { \partial L } { \partial \Delta _ { t } q _ { k } } \Delta _ { t } q _ { k } \right) { \mathrm { d } } t _ { k + 1 } + \frac { \partial L } { \partial \Delta _ { t } q _ { k } } { \mathrm { d } } q _ { k + 1 } .
$$

From (1.55), we can deduce that $\theta _ { \mathbb { L } } ^ { + }$ converges to the continuous Lagrangian 1-form $\vartheta _ { L }$ defined by (1.29) as $t _ { k + 1 } \to t _ { k } , t _ { k - 1 } \to t _ { k }$ . Thus, we obtain

$$
\Omega _ { \mathbb { L } } = \mathbf { d } \theta _ { \mathbb { L } } ^ { + } \longrightarrow \mathrm { d } \vartheta _ { L } = \Omega _ { L } , \quad t _ { k + 1 } \longrightarrow t _ { k } , \quad t _ { k - 1 } \longrightarrow t _ { k } .
$$

In general, the variational integrator (1.35) with fixed time steps does not exactly conserve the discrete energy, and the computed energy will not have secular variation $\left[ \mathrm { G M 8 8 } , \mathrm { S S C 9 4 } \right]$ . In some cases, such as in discrete mechanics proposed by Lee in $\mathrm { [ L e e 8 2 , L e e 8 7 ] }$ , the integrator (1.35) is required to conserve the discrete energy (1.36) by varying the time steps. In other words, the steps can be chosen according to (1.36) so that the integrator (1.35) conserves the discrete energy (1.36). The resulting integrator also conserves the discrete extended Lagrange 2-form $\mathrm { d } \theta _ { \mathbb { L } } ^ { + }$ . This fact had not been discussed in Lee’s discrete mechanics.

Example 1.3. Let us consider an example. For the classical Lagrangian

$$
L ( t , q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { 2 } - V ( q ) ,
$$

we choose the discrete Lagrangian $\mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } )$ as

$$
\mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) = \frac { 1 } { 2 } \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) ^ { 2 } - V \left( \frac { q _ { k + 1 } - q _ { k } } { 2 } \right) .
$$

The discrete Euler–Lagrange equation (1.35) becomes

$$
\left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } - \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) + \frac { V ^ { \prime } ( \bar { q } _ { k } ) ( t _ { k + 1 } - t _ { k } ) + V ^ { \prime } ( \bar { q } _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) } { 2 } = 0 ,
$$

which preserves the Lagrange 2-form

$$
\begin{array} { r } { \left( \frac { 1 } { t _ { k + 1 } - t _ { k } } + \frac { t _ { k + 1 } - t _ { k } } { 4 } V ^ { \prime \prime } ( \bar { q } _ { k } ) \right) { \mathrm { d } { q } _ { k + 1 } } \wedge { \mathrm { d } { q } _ { k } } , } \end{array}
$$

where $\bar { q } _ { k } = \frac { q _ { k } + q _ { k + 1 } } { 2 }$ , $\bar { q } _ { k - 1 } = \frac { q _ { k - 1 } + q _ { k } } { 2 }$ .

If we take fixed variables $t _ { k + 1 } - t _ { k } = t _ { k } - t _ { k - 1 } = h$ , then (1.59) becomes

$$
{ \frac { q _ { k + 1 } - 2 q _ { k } + q _ { k - 1 } } { h ^ { 2 } } } + { \frac { V ^ { \prime } ( { \bar { q } } _ { k } ) + V ^ { \prime } ( { \bar { q } } _ { k - 1 } ) } { 2 } } = 0 ,
$$

which preserves the Lagrange 2-form

$$
\left( { \frac { 1 } { h } } + { \frac { h } { 4 } } V ^ { \prime \prime } ( { \bar { q } } _ { k } ) \right) { \mathrm { d } } q _ { k + 1 } \wedge { \mathrm { d } } q _ { k } .
$$

# 14.1.4 Concluding Remarks

We have presented the calculus of total variation problem for discrete mechanics with variable time steps referring to continuous mechanics in this section. Using the calculus for discrete total variations, we have proved that Lee’s discrete mechanics is symplectic and derived Kane–Marsden–Ortiz integrators. It is well known that an energy-preserving variational integrator is a more preferable and natural candidate of approximations for conservative Euler–Lagrange equation, since the solution of conservative Euler–Lagrange equation is not only symplectic but also energy-preserving.

As is mentioned, Kane–Marsden–Ortiz integrators are related closely to the discrete mechanics proposed by Lee[Lee82,Lee87] . In Lee’s discrete mechanics, the difference equations are the same as Kane–Marsden–Ortiz integrators. However, Lee’s difference equations are solved as boundary value problems, while Kane–Marsden–Ortiz integrators are solved as initial value problems.

Finally, it should be mentioned that in very recent works[GLW01a,GLWW01,GW03] , two of the authors (HYG and KW) and their collaborators have presented a difference discrete variational calculus and the discrete version of Euler–Lagrange cohomology for vertical variation problems in both Lagrangian and Hamiltonian formalism for discrete mechanics and field theory. In their approach, the difference operator with fixed step-length is regarded as an entire geometric object. The advantages of this approach have already been seen in the last subsection in the course of taking continuous limits although the difference operator $\Delta _ { t }$ in (1.50) is of variable step-length. This approach may be generalized to the discrete total variation problems.

# 14.2 Total Variation in Hamiltonian Formalism

We present a discrete total variation calculus in Hamiltonian formalism in this section. Using this discrete variation calculus and generating function for flows of Hamiltonian systems, we derive symplectic-energy integrators of any finite order for Hamiltonian systems from a variational perspective. The relationship between the symplectic integrators derived directly from the Hamiltonian systems and the variationally derived symplectic-energy integrators is explored.

# 14.2.1 Variational Principle in Hamiltonian Mechanics

Let us begin by recalling the ordinary variational principle in Hamiltonian formalism. Suppose $Q$ denotes the configuration space with coordinates $q ^ { i }$ , and $T ^ { * } Q$ the phase space with coordinates $( q ^ { i } , p ^ { i } ) ( i = 1 , 2 , \cdots , n )$ . Consider a Hamiltonian $H : T ^ { * } Q $ $\mathbb { R }$ . The corresponding action functional is defined by

$$
S ( ( q ^ { i } ( t ) , p ^ { i } ( t ) ) ) = \int _ { a } ^ { b } ( p ^ { i } \cdot q ^ { i } - H ( q ^ { i } , p ^ { i } ) ) \operatorname { d } t ,
$$

where $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ is a $C ^ { 2 }$ curve in phase space $T ^ { * } Q$ .

The variational principle in Hamiltonian formalism seeks the curves $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ for which the action functional $S$ is stationary under variations of $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ with fixed end points. We will first define the variation of $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ .

Let

$$
V = \sum _ { i = 1 } ^ { n } \phi ^ { i } ( { \bf q } , { \bf p } ) \frac { \partial } { \partial q ^ { i } } + \sum _ { i = 1 } ^ { n } \psi ^ { i } ( { \bf q } , { \bf p } ) \frac { \partial } { \partial p ^ { i } } ,
$$

be a vector field on $T ^ { * } Q$ , here $\pmb q = ( q ^ { 1 } , \cdot \cdot \cdot , q ^ { n } ) , \pmb { p } = ( p ^ { 1 } , \cdot \cdot \cdot , p ^ { n } )$ . For simplicity, we will use Einstein convention and omit the summation notation $\displaystyle \sum$ in the following.

Let us denote the flow of $V$ by $F ^ { \varepsilon } : F ^ { \varepsilon } ( \pmb { q } , \pmb { p } ) = ( \tilde { \pmb { q } } , \tilde { \pmb { p } } )$ , which is written in components as

$$
\begin{array} { r } { \tilde { q } ^ { i } = f ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) , } \\ { \tilde { p } ^ { i } = g ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) , } \end{array}
$$

where $( { \pmb q } , { \pmb p } ) \in T ^ { * } Q$ and

$$
\begin{array} { r l } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } f ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) = \phi ^ { i } ( \pmb { q } , \pmb { p } ) , } \\ & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) = \psi ^ { i } ( \pmb { q } , \pmb { p } ) . } \end{array}
$$

Let $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ be a curve in $T ^ { * } Q$ . The transformation (2.3) and (2.4) transforms $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ into a family of curves

$$
\left( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) \right) = \left( f ^ { i } ( \varepsilon , \pmb { q } ( t ) , \pmb { p } ( t ) ) , g ^ { i } ( \varepsilon , \pmb { q } ( t ) , \pmb { p } ( t ) ) \right) .
$$

Next, we will define the variation of $\left( q ^ { i } ( t ) , p ^ { i } ( t ) \right)$ :

$$
\delta \bigl ( q ^ { i } ( t ) , p ^ { i } ( t ) \bigr ) = : \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big | _ { \varepsilon = 0 } \bigl ( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) \bigr ) = \bigl ( \phi ^ { i } ( q , p ) , \psi ^ { i } ( q , p ) \bigr ) .
$$

Next, we will calculate the variation of $S$ at $\left( q ^ { i } ( t ) , p ^ { i } ( t ) \right)$ as follows:

$$
\begin{array} { r l } { \delta S } & { = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } S \Big ( \big ( \bar { q } ^ { i } ( t ) , \bar { p } ^ { i } ( t ) \big ) \Big ) } \\ & { = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } S \Big ( \big ( f ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) , g ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) \big ) \Big ) } \\ & { = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } \int _ { a } ^ { b } \bigg ( g ^ { i } \Big ( \varepsilon , q ( t ) , p ( t ) \Big ) \frac { \mathrm { d } } { \mathrm { d } t } f ^ { i } \Big ( \varepsilon , q ( t ) , p ( t ) \Big ) } \\ & { \quad - H \Big ( f ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) , g ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) \Big ) \bigg ) \mathrm { d } t } \\ & { = \int _ { a } ^ { b } \bigg [ \Big ( \bar { q } ^ { i } - \frac { \partial H } { \partial p ^ { i } } \Big ) \psi ^ { i } + \Big ( - \bar { p } ^ { i } - \frac { \partial H } { \partial q ^ { i } } \Big ) \phi ^ { i } \bigg ] \mathrm { d } t + p ^ { i } \phi ^ { i } \bigg | _ { a } ^ { b } . } \end{array}
$$

If $\phi ^ { i } \bigl ( \pmb { q } ( a ) , \pmb { p } ( a ) \bigr ) \phi ^ { i } \bigl ( \pmb { q } ( b ) , \pmb { p } ( b ) \bigr ) = 0$ , the requirement of $\delta S = 0$ yields the Hamilton equation for $\left( q ^ { i } ( t ) , p ^ { i } ( t ) \right)$ :

$$
\dot { q } ^ { i } = \frac { \partial H } { \partial p ^ { i } } , ~ \dot { p } ^ { i } = - \frac { \partial H } { \partial q ^ { i } } .
$$

If we drop the requirement of $\phi ^ { i } \big ( { \pmb q } ( a ) , { \pmb p } ( a ) \big ) \phi ^ { i } \big ( { \pmb q } ( b ) , { \pmb p } ( b ) \big ) \ = \ 0$ , we can naturally obtain the canonical 1-form on $T ^ { * } Q$ from the second term in (2.6): $\theta = p ^ { i } \mathrm { d } q ^ { i }$ . Furthermore, restricting $\left( ( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) ) \right)$ to the solution space of (2.7), we can prove that the solution of (2.7) preserves the canonical 2-form $\omega = \mathbf { d } \theta _ { L } = \mathbf { d } p ^ { i } \wedge \mathbf { d } q ^ { i }$ .

On the other hand, it is not necessary to restrict $\left( ( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) ) \right)$ to the solution space of (2.7). Introducing the Euler–Lagrange 1-form

$$
E ( q ^ { i } , p ^ { i } ) = \Big ( \dot { q } ^ { i } - \frac { \partial H } { \partial p ^ { i } } \Big ) { \bf d } p ^ { i } + \Big ( - \dot { p } ^ { i } - \frac { \partial H } { \partial q ^ { i } } \Big ) { \bf d } q ^ { i } ,
$$

the nilpotency of $d$ leads to

$$
\mathrm { d } E ( q ^ { i } , p ^ { i } ) + \frac { \mathrm { d } } { \mathrm { d } t } \omega = 0 ,
$$

namely, the necessary and sufficient condition for symplectic structure preserving is that the Euler–Lagrange 1-form (2.8) is closed[GLW01a,GLWW01,GLW01b,GW03] .

Based on the above-given variational principle in Hamiltonian formalism and using the ideas of discrete Lagrange mechanics[Ves88,Ves91b,MPS98,WM97] , we can develop a natural version of discrete Hamilton mechanics with fixed time steps and derive symplectic integrators for Hamilton canonical equations from a variational perspective[GLWW01] .

However, the symplectic integrators obtained in this way are not energy-preserving, in general, because of its fixed time steps[GM88] . An energy-preserving symplectic integrator is a more preferable and natural candidate of approximations for conservative Hamilton equations since the solution of conservative Hamilton equations is not only symplectic but also energy-preserving. To attain this goal, we use variable time steps and a discrete total variation calculus developed in [Lee82,Lee87,KMO99,CGW03] . The basic idea is to construct a discrete action functional with variable time steps and then apply a discrete total variation calculus. In this way, we can derive symplectic integrators and their associated energy conservation laws. These variationally derived symplectic integrators are two-step integrators. If we take fixed time steps, the resulting integrators are equivalent to the symplectic integrators derived directly from the Hamiltonian systems in some special cases.

# 14.2.2 Total Variation in Hamiltonian Mechanics

In order to discuss total variation in Hamiltonian formalism, we will work with extended phase space $\mathbb { R } \times T ^ { * } Q$ with coordinates $( t , q ^ { i } , p ^ { i } )$ . Here $t$ denotes time. For details, see $\left[ { \mathrm { A r n } } 8 9 , { \mathrm { G P S } } 0 2 \right]$ . By total variation, we refer to variations of both $( q ^ { i } , p ^ { i } )$ and $t$ . Consider a vector field on $\mathbb { R } \times T ^ { * } Q$ ,

$$
V = \xi ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial q ^ { i } } + \psi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial p ^ { i } } .
$$

Let $F ^ { \varepsilon }$ be the flow of $V$ . For $( t , q ^ { i } , p ^ { i } ) \in \mathbb { R } \times T ^ { * } Q$ , we have $F ^ { \varepsilon } ( t , q ^ { i } , p ^ { i } ) = ( \tilde { t } , \tilde { q } ^ { i } , \tilde { p } ^ { i } )$ :

$$
\begin{array} { l } { { \tilde { t } _ { \mathbf { \lambda } } = h ( \varepsilon , t , \pmb { q } , \pmb { p } ) , } } \\ { { \tilde { q } ^ { i } = f ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) , } } \\ { { \tilde { p } ^ { i } = g ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) , } } \end{array}
$$

where

$$
\begin{array} { r l } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } h ( \varepsilon , t , \pmb { q } , \pmb { p } ) = \xi ( t , \pmb { q } , \pmb { p } ) , } \\ & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } f ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) = \phi ^ { i } ( t , \pmb { q } , \pmb { p } ) , } \\ & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) = \psi ^ { i } ( t , \pmb { q } , \pmb { p } ) . } \end{array}
$$

The transformation $( 2 . 1 1 ) - ( 2 . 1 3 )$ transforms a curve $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ into a family of curves $( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) )$ determined by

$$
\begin{array} { l } { { \tilde { t } = h \big ( \varepsilon , t , \pmb { q } ( t ) , \pmb { p } ( t ) \big ) , } } \\ { { \tilde { q } ^ { i } = f ^ { i } \big ( \varepsilon , t , \pmb { q } ( t ) , \pmb { p } ( t ) \big ) , } } \\ { { \tilde { p } ^ { i } = g ^ { i } \big ( \varepsilon , t , \pmb { q } ( t ) , \pmb { p } ( t ) \big ) . } } \end{array}
$$

Suppose we can solve (2.17) for $t : t = h ^ { - 1 } ( \varepsilon , \tilde { t } )$ . Then,

$$
\begin{array} { l } { { \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) = f ^ { i } ( \varepsilon , h ^ { - 1 } ( \varepsilon , \tilde { t } ) , \pmb { q } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) , \pmb { p } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) ) , } } \\ { { \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) = f ^ { i } ( \varepsilon , h ^ { - 1 } ( \varepsilon , \tilde { t } ) , \pmb { q } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) , \pmb { p } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) ) . } } \end{array}
$$

Before calculating the variation of $S$ directly, we will first consider the first-order prolongation of $V$ ,

$$
\mathrm { p r } ^ { 1 } V = \xi ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial { \pmb q } ^ { i } } + \psi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial p ^ { i } } + \alpha ^ { i } ( t , { \pmb q } , { \pmb p } , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial { \pmb q } ^ { i } } + \beta ^ { i } ( t , { \pmb q } , { \pmb p } , { \pmb { \dot { q } } } , { \pmb { \dot { p } } } ) \frac { \partial } { \partial \vec { p } ^ { i } } ,
$$

where $\mathrm { p r } ^ { 1 } V$ denotes the first-order prolongation of $V$ and

$$
\begin{array} { l } { { \alpha ^ { i } ( t , { \pmb q } , { \pmb p } , { \dot { \pmb q } } , { \dot { \pmb p } } ) = D _ { t } \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) - { \dot { q } ^ { i } } D _ { t } \xi \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) , } } \\ { { \beta ^ { i } ( t , { \pmb q } , { \pmb p } , { \dot { \pmb q } } , { \dot { \pmb p } } ) = D _ { t } \psi ^ { i } ( t , { \pmb q } , { \pmb p } ) - { \dot { p } ^ { i } } D _ { t } \xi \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) , } } \end{array}
$$

where $D _ { t }$ denotes the total derivative. For example,

$$
D _ { t } \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) = \phi _ { t } ^ { i } + \phi _ { q } \dot { \pmb q } + \phi _ { \pmb p } \dot { \pmb p } .
$$

For prolongation of vector field and formulae (2.23) and (2.24), refer to $[ \mathrm { O l v 9 3 } ]$ .

Now, let us calculate the variation of $S$ directly as follows:

$$
\begin{array} { l } { { \delta S ~ = ~ \left. { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } } \right| _ { \varepsilon = 0 } S \big ( ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) ) \big ) } } \\ { { { } ~ = ~ \left. { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } } \right| _ { \varepsilon = 0 } \int _ { \tilde { a } } ^ { \tilde { b } } \Big ( \big ( \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) { \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) - H \big ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) \Big ) \mathrm { d } \tilde { t } } } \end{array}
$$

$$
\begin{array} { r l } { \ } & { = \ \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \int _ { a } ^ { b } \Big ( \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) - H \big ( ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) \frac { \mathrm { d } \tilde { t } } { \mathrm { d } t } + t } \\ & { \qquad \big ( \tilde { t } = h ( \varepsilon , i , q ( t ) , p ( t ) ) \big ) } \\ { \ } & { = \ \int _ { a } ^ { b } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \Big ( \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) - H \big ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) \Big ) \mathrm { d } t } \\ & { \ + \ \int _ { a } ^ { b } \big ( p ^ { i } ( t ) \dot { q } ^ { i } ( t ) - H \big ( q ^ { i } ( t ) , p ^ { j } ( t ) \big ) \big ) D _ { \varepsilon } \xi \mathrm { d } t } \\ { \ } & { = \ \int _ { a } ^ { b } \Big [ \Big ( \frac { \mathrm { d } } { \mathrm { d } t } H \big ( q ^ { i } ( t ) , p ^ { i } ( t ) \big ) \Big ) \xi + \Big ( - \tilde { p } ^ { i } - \frac { \partial { H } } { \partial q ^ { i } } \Big ) \dot { \varphi } ^ { i } + \Big ( \dot { q } ^ { i } - \frac { \partial { H } } { \partial p ^ { i } } \Big ) \psi ^ { i } \Big ] \mathrm { d } t } \\ & { \ + [ p ^ { i } \dot { q } ^ { i } - H ( { q } ^ { i } , p ^ { i } ) \xi ] _ { * } ^ { b } . } \end{array}
$$

In (2.25), we have used (2.14)and the fact

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \frac { \mathrm { d } \tilde { t } } { \mathrm { d } t } = \frac { \mathrm { d } } { \mathrm { d } t } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \tilde { t } = D _ { t } \xi .
$$

In (2.26), we have used the prolongation formula (2.23).

If $\xi { \big ( } a , \pmb { q } ( a ) , \pmb { p } ( a ) { \big ) } = \xi { \big ( } b , \pmb { q } ( b ) , \pmb { p } ( b ) { \big ) } = 0$ and $\phi ^ { i } \bigl ( a , \pmb { q } ( a ) , \pmb { p } ( a ) \bigr ) = \phi ^ { i } \bigl ( b , \pmb { q } ( b ) , \pmb { p } ( b ) \bigr )$ $= 0$ , the requirement of $\delta S = 0$ yields the Hamilton canonical equation

$$
\dot { q } ^ { i } = \frac { \partial H } { \partial p ^ { i } } , \quad \dot { p } ^ { i } = - \frac { \partial H } { \partial q ^ { i } }
$$

from the variation $\phi ^ { i } , \psi ^ { i }$ and the energy conservation law

$$
\frac { \mathrm { d } } { \mathrm { d } t } H ( q ^ { i } , p ^ { i } ) = 0
$$

from the variation $\xi$ . Since

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } H ( q ^ { i } , p ^ { i } ) = { \frac { \partial H } { \partial q ^ { i } } } \cdot q ^ { i } + { \frac { \partial H } { \partial p ^ { i } } } \cdot p ^ { i } ,
$$

we can very well see that the energy conservation law (2.28) is a natural consequence of the Hamilton canonical Equation (2.27).

If we drop the requirement

$$
\begin{array} { l } { { \displaystyle \xi \big ( a , \pmb { q } ( a ) , \pmb { p } ( a ) \big ) = \xi \big ( b , \pmb { q } ( b ) , \pmb { p } ( b ) \big ) = 0 , } } \\ { { \displaystyle \phi ^ { i } \big ( a , \pmb { q } ( a ) , \pmb { p } ( a ) \big ) = \phi ^ { i } \big ( b , \pmb { q } ( b ) , \pmb { p } ( b ) \big ) = 0 , } } \end{array}
$$

we can define the extended canonical 1-form on $\mathbb { R } \times T ^ { * } Q$ from the second term in (2.26)

$$
\theta = p ^ { i } \mathrm { d } q ^ { i } - H ( q ^ { i } , p ^ { i } ) \mathrm { d } t .
$$

Furthermore, restricting $\left( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) \right)$ to the solution space of (2.27), we can prove that the solution of (2.27) preserves the extended canonical 2-form

$$
\omega = \mathbf { d } \theta = \mathbf { d } p ^ { i } \wedge \mathbf { d } q ^ { i } - \mathbf { d } H ( q ^ { i } , p ^ { i } ) \wedge \mathbf { d } t
$$

by using the same method i $\mathrm { | ^ { [ M P S 9 8 ] } }$ .

# 14.2.3 Symplectic-Energy Integrators

In this section, we will develop a discrete version of total variation in Hamiltonian formalism. Using this discrete total variation calculus, we will derive symplectic-energy integrators.

Let

$$
L ( q ^ { i } , p ^ { i } , \dot { q } ^ { i } , \dot { p } ^ { i } ) = p ^ { i } \dot { q } ^ { i } - H ( q ^ { i } , p ^ { i } )
$$

be a function from $\mathbb { R } \times T ( T ^ { * } Q )$ to $\mathbb { R }$ . Here $L$ does not depend on $t$ explicitly.

We use $P \times P$ for the discrete version $\mathbb { R } \times T ( T ^ { * } Q )$ . Here $P$ is the discrete version of $\mathbb { R } \times T ^ { * } Q$ . A point $\left( t _ { 0 } , \pmb { q } _ { 0 } , \pmb { p } _ { 0 } ; t _ { 1 } , \pmb { q } _ { 1 } , \pmb { p } _ { 1 } \right) \in P \times P$ corresponds to a tangent vector

$$
\biggl ( { \frac { q _ { 1 } - q _ { 0 } } { t _ { 1 } - t _ { 0 } } } , { \frac { p _ { 1 } - p _ { 0 } } { t _ { 0 } - t _ { 0 } } } \biggr ) .
$$

For simplicity, the vector symbols $\pmb q = ( q ^ { 1 } , \cdots , q ^ { n } )$ and $\pmb { p } = ( p ^ { 1 } , \cdots , p ^ { n } )$ are used throughout this section. A discrete $L$ is defined to be $\mathbb { L } : P \times P \to \mathbb { R }$ and the corresponding discrete action as

$$
S = \sum _ { k = 0 } ^ { N - 1 } \mathbb { L } ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) ,
$$

where $t _ { 0 } ~ = ~ a , t _ { N } ~ = ~ b$ . The discrete variational principle in total variation is to extremize $S$ for variations of both ${ \pmb q } _ { k } , { \pmb p } _ { k }$ and $t _ { k }$ holding the end points $\left( t _ { 0 } , \pmb q _ { 0 } , \pmb p _ { 0 } \right)$ and $\left( t _ { N } , \pmb q _ { N } , \pmb p _ { N } \right)$ fixed. This discrete variational principle determines a discrete flow $\Phi : P \times P \to P \times P$ by

$$
\Phi ( t _ { k - 1 } , \pmb { q } _ { k - 1 } , \pmb { p } _ { k - 1 } , t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } ) = ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } ) .
$$

Here, $( t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } )$ for all $k \in ( 1 , 2 , \cdots , N - 1 )$ are found from the following discrete Hamilton canonical equation

$$
\begin{array} { r l } & { ( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , p _ { k } , t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 } ) + ( t _ { k } - t _ { k - 1 } ) D _ { 5 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , p _ { k - 1 } , t _ { k } , q _ { k } , p _ { k } ) = 0 , } \\ & { ( t _ { k + 1 } - t _ { k } ) D _ { 3 } \mathbb { L } ( t _ { k } , q _ { k } , p _ { k } , t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 } ) + ( t _ { k } - t _ { k - 1 } ) D _ { 6 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , p _ { k - 1 } , t _ { k } , q _ { k } , p _ { k } ) = 0 } \end{array}
$$

and the discrete energy conservation law

$$
\begin{array} { r } { ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) + ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } \big ( t _ { k - 1 } , \pmb { q } _ { k - 1 } , \pmb { p } _ { k - 1 } , \pmb { q } _ { k - 1 } \big ) } \\ { - \mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) + \mathbb { L } \big ( t _ { k - 1 } , \pmb { q } _ { k - 1 } , \pmb { p } _ { k - 1 } , t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } \big ) = 0 . } \end{array}
$$

$D _ { i }$ denotes the partial derivative of $\mathbb { L }$ with respect to the $i$ th argument. Equation (2.33) is the discrete Hamilton canonical equation (variational integrator). Equation (2.34) is the discrete energy conservation law associated with (2.33). Unlike the continuous case, the variational integrator (2.33) does not satisfy (2.34) for arbitrarily given $t _ { k + 1 }$ in general. Therefore, we need to solve (2.33) and (2.34) simultaneously with $q _ { k + 1 } , p _ { k + 1 }$ and $t _ { k + 1 }$ taken as unknowns.

Now, we will prove that the discrete flow determined by (2.33) and (2.34) preserves a discrete version of the extended Lagrange 2-form $\omega$ defined in (2.30) so that we call (2.33) and (2.34) a symplectic-energy integrator. We will do this directly from the variational point of view, consistent with the continuous case[MPS98] .

As in the continuous case, we will calculate $\mathrm { d } S$ for variations with varied end points.

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathrm { S i g } \{ q _ { 1 } , q _ { 2 } , p _ { 2 } , \cdots , t _ { N } , q _ { N - 1 } , ( p _ { N - 1 } , q _ { N - 1 } , q _ { N - 1 } , q _ { N - 1 } , \cdots , q _ { N } , p _ { N - 1 } , q _ { N } , q _ { N - 1 } , \cdots , q _ { N } , q _ { N - 1 } , q _ { N } , \cdots ) } \\ & { - \displaystyle \sum _ { k = 1 } ^ { N } ( \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k } + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k } + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k } - \int _ { 0 } ^ { T } [ \Phi ( q _ { k } ) \Phi _ { k - 1 } ] \Phi _ { k } ) \Big ) \Big \} \Phi _ { k } } \\ & { - \displaystyle \sum _ { k = 1 } ^ { N } \Big ( \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k } ) + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k + 1 } + \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k - 1 } ) \Phi _ { k } \Big ) \Big ) \Phi _ { k } } \\ & { + \displaystyle \sum _ { k = 1 } ^ { N } ( \partial _ { k } [ q _ { k } ] \Phi _ { k } \Big ) \Big ) \Big \{ \Phi _ { k } + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k - 1 } - \Phi _ { k } \Big \} + \sum _ { k = 1 } ^ { N } \frac { 1 } { | q _ { k } | } \Phi _ { k } \Big ) \Big ( \Phi _ { k + 1 } - \partial _ { k } [ q _ { k } ] \Phi _ { k - 1 } \Big ) } \\ & { - \displaystyle \sum _ { k = 1 } ^ { N } ( \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k - 1 } - q _ { k } ) + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k - 1 } \Big ) \Phi _ { k } - \cdots ) \Phi _ { k } } \\ &  - \displaystyle \sum _ { k = 1 } ^ { N } ( \mathcal { P } _ { k } [ \Phi ( q _ { k } ) ] \Big ( \Phi ( q _ { k - 1 } , \cdots , q _ { N } ) \ \end{array} \end{array}
$$

where $\pmb { v } _ { k } = \left( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \right) ( k = 0 , 1 , \cdots , N - 1 )$ . We can see that the last six terms in (2.35) come from the boundary variations. Based on the boundary variations, we can define two 1-forms on $P \times P$ ,

$$
\begin{array} { r c l } { \theta _ { \mathbb { L } } ^ { - } ( \pmb { v } _ { k } ) } & { = } & { D _ { 2 } \mathbb { L } ( \pmb { v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } \pmb { q } _ { k } + D _ { 3 } \mathbb { L } ( \pmb { v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } \pmb { p } _ { k } } \\ & & { + D _ { 1 } \mathbb { L } ( \pmb { v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( \pmb { v } _ { k } ) \mathrm { d } t _ { k } } \end{array}
$$

and

$$
\begin{array} { r c l } { \theta _ { \mathbb { L } } ^ { + } ( { \pmb v } _ { k } ) } & { = } & { D _ { 5 } \mathbb { L } ( { \pmb v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } { \pmb q } _ { k + 1 } + D _ { 6 } \mathbb { L } ( { \pmb v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } { \pmb p } _ { k + 1 } } \\ & & { + D _ { 4 } \mathbb { L } ( { \pmb v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( { \pmb v } _ { k } ) \mathrm { d } t _ { k + 1 } . } \end{array}
$$

Here, we have used the notation in [MPS98] . We regard the pair $( \theta _ { \mathbb { L } } ^ { - } , \theta _ { \mathbb { L } } ^ { + } )$ as being the discrete version of the extended canonical 1-form $\theta$ defined in (2.29).

Now, we will parametrize the solutions of the discrete variational principle by $( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } )$ , and restrict $S$ to that solution space. Then, Equation (2.35) becomes

$$
\begin{array} { r l } & { \mathrm { d } S ( t _ { 0 } , q _ { 0 } , p _ { 0 } , \cdots , t _ { N } , q _ { N } , p _ { N } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \cdots , \delta t _ { N } , \delta q _ { N } , \delta p _ { N } ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } ( t _ { 0 } , q _ { 0 } , p _ { 0 } , t _ { 1 } , q _ { 1 } , p _ { 1 } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } , \delta p _ { 1 } ) } \\ & { \quad + \theta _ { \mathbb { L } } ^ { + } ( t _ { N - 1 } , q _ { N - 1 } , p _ { N - 1 } , t _ { N } , q _ { N } , p _ { N } ) \cdot ( \delta t _ { N - 1 } , \delta q _ { N - 1 } , \delta p _ { N - 1 } , \delta t _ { N } , \delta q _ { N } , \delta p _ { N } ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } ( t _ { 0 } , q _ { 0 } , p _ { 0 } , t _ { 1 } , q _ { 1 } , p _ { 1 } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } , \delta p _ { 1 } ) } \\ & { \quad + ( \Phi ^ { N - 1 } ) ^ { * } \theta _ { \mathbb { L } } ^ { + } ( t _ { 0 } , q _ { 0 } , p _ { 0 } , t _ { 1 } , q _ { 1 } , p _ { 1 } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } , \delta p _ { 1 } ) . } \end{array}
$$

From (2.38), we can obtain

$$
\begin{array} { r } { \mathtt { d } S = \theta _ { \mathbb { L } } ^ { - } + ( \Phi ^ { N - 1 } ) ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

The Equation (2.39) holds for arbitrary $N > 1$ . Taking $N = 2$ , we obtain

$$
\begin{array} { r } { \mathtt { d } S = \theta _ { \mathbb { L } } ^ { - } + \Phi ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

By exterior differentiation of (2.40), we obtain

$$
\Phi ^ { * } ( { \bf d } \theta _ { \mathbb { L } } ^ { + } ) = - { \bf d } \theta _ { \mathbb { L } } ^ { - } .
$$

From the definition of $\theta _ { \mathbb { L } } ^ { - }$ and $\theta _ { \mathbb { L } } ^ { + }$ , we know that

$$
\begin{array} { r } { \theta _ { \mathbb { L } } ^ { - } + \theta _ { \mathbb { L } } ^ { + } = \mathrm { d } \mathbb { L } . } \end{array}
$$

By exterior differentiation of (2.42), we obtain ${ \bf d } \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - }$ . Define

$$
\omega _ { \mathbb { L } } \equiv { \bf d } \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - } .
$$

Finally, we have shown that the discrete flow $\Phi$ preserves the discrete extended canonical 2-form $\omega _ { \mathbb { L } }$ :

$$
\begin{array} { r } { \Phi ^ { * } ( \omega _ { \mathbb { L } } ) = \omega _ { \mathbb { L } } . } \end{array}
$$

We can now call the coupled difference system (2.33) and (2.34) a symplecticenergy integrator in the sense that it satisfies the discrete energy conservation law (2.34) and preserves the discrete extended canonical 2-form $\omega _ { \mathbb { L } }$ .

To illustrate the above-mentioned discrete total variation calculus, we present an example. We choose $\mathbb { L }$ in (2.31) as

$$
\mathbb { L } ( t _ { k } , q _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } ) = \pmb { p } _ { k + 1 / 2 } \frac { \pmb { q } _ { k + 1 } - \pmb { q } _ { k } } { t _ { k + 1 } - t _ { k } } - H ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) ,
$$

where

$$
{ \pmb p } _ { k + 1 / 2 } = \frac { { \pmb p } _ { k } + { \pmb p } _ { k + 1 } } { 2 } , \qquad { \pmb q } _ { k + 1 / 2 } = \frac { { \pmb q } _ { k } + { \pmb q } _ { k + 1 } } { 2 } .
$$

Using (2.33), we can obtain the corresponding discrete Hamilton equation

$$
\begin{array} { l } { \displaystyle \frac { { \bf q } _ { k + 1 } - { \bf q } _ { k - 1 } } { 2 } - \frac { 1 } { 2 } \bigg ( ( t _ { k + 1 } - t _ { k } ) \frac { \partial H } { \partial { \bf p } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial H } { \partial { \bf p } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) = 0 , } \\ { \displaystyle \frac { { \bf p } _ { k + 1 } - { \bf p } _ { k - 1 } } { 2 } + \frac { 1 } { 2 } \bigg ( ( t _ { k + 1 } - t _ { k } ) \frac { \partial H } { \partial { \bf q } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial H } { \partial { \bf q } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) \bigg ) = 0 . } \end{array}
$$

where $\begin{array} { r } { { \pmb p } _ { k - 1 / 2 } = \frac { { \pmb p } _ { k } + { \pmb p } _ { k - 1 } } { 2 } , \quad { \pmb q } _ { k - 1 / 2 } = \frac { { \pmb q } _ { k } + { \pmb q } _ { k - 1 } } { 2 } } \end{array}$ .

Using (2.34), we can obtain the corresponding discrete energy conservation law

$$
H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) = H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) .
$$

The symplectic-energy integrator (2.46) and (2.47) preserves the discrete 2-form:

$$
\frac { 1 } { 2 } \big ( \mathrm { d } \pmb { p } _ { k } \wedge \mathrm { d } \pmb { q } _ { k + 1 } + \mathrm { d } \pmb { p } _ { k + 1 } \wedge \mathrm { d } \pmb { q } _ { k } \big ) - H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) \wedge \Big ( \frac { \mathrm { d } t _ { k } + \mathrm { d } t _ { k + 1 } } { 2 } \Big ) .
$$

If we take fixed time steps $t _ { k + 1 } - t _ { k } = h \left( h \right.$ is a constant), then (2.46) becomes

$$
\begin{array} { l } { \displaystyle \frac { { \pmb q } _ { k + 1 } - { \pmb q } _ { k - 1 } } { 2 h } = \frac { 1 } { 2 } \bigg ( \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) \bigg ) , } \\ { \displaystyle \frac { { \pmb p } _ { k + 1 } - { \pmb p } _ { k - 1 } } { 2 h } = - \frac { 1 } { 2 } \bigg ( \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) \bigg ) . } \end{array}
$$

Now, we will explore the relationship between (2.49) and the midpoint integrator for the Hamiltonian system

$$
\begin{array} { l } { { \displaystyle { \dot { \pmb q } } ~ = ~ { \frac { \partial { \cal H } } { \partial { \pmb p } } } , } } \\ { { \displaystyle { \dot { \pmb p } } ~ = ~ - { \frac { \partial { \cal H } } { \partial { \pmb q } } } . } } \end{array}
$$

The midpoint symplectic integrator for (2.50) is

$$
\begin{array} { r c l } { \displaystyle \frac { { \pmb q } _ { k + 1 } - { \pmb q } _ { k } } { h } } & { = } & { \displaystyle \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) , } \\ { \displaystyle \frac { { \pmb p } _ { k + 1 } - { \pmb p } _ { k } } { h } } & { = } & { \displaystyle - \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) . } \end{array}
$$

Replacing $k$ by $k - 1$ in (2.51), we obtain

$$
\begin{array} { r c l } { \displaystyle \frac { { \pmb q } _ { k } - { \pmb q } _ { k - 1 } } { h } ~ = ~ \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) , } \\ { \displaystyle \frac { { \pmb p } _ { k } - { \pmb p } _ { k - 1 } } { h } ~ = ~ - \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) . } \end{array}
$$

Adding (2.52) to (2.51) results in (2.49). Therefore, if we use (2.51) to obtain $\pmb { p } _ { k } , \pmb { q } _ { k }$ , the two-step integrator (2.49) is equivalent to the midpoint integrator (2.51). However, the equivalence does not hold in general. For example, choose $\mathbb { L }$ in (2.31) as

$$
\mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) = \pmb { p } _ { k } \frac { \pmb { q } _ { k + 1 } - \pmb { q } _ { k } } { t _ { k + 1 } - t _ { k } } - H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) ,
$$

and take fixed time steps $t _ { k + 1 } - t _ { k } = h$ . Then (2.33) becomes

$$
\begin{array} { l } { \displaystyle \frac { { \bf q } _ { k + 1 } - { \bf q } _ { k } } { h } ~ = ~ \frac { 1 } { 2 } \Big ( \frac { \partial H } { \partial p } \big ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial p } \big ( { \bf q } _ { k - 1 / 2 } , { \bf p } _ { k - 1 / 2 } \big ) \Big ) , } \\ { \displaystyle \frac { { \bf p } _ { k } - { \bf p } _ { k - 1 } } { h } ~ = ~ - \frac { 1 } { 2 } \Big ( \frac { \partial H } { \partial { \bf q } } \big ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial { \bf q } } \big ( { \bf q } _ { k - 1 / 2 } , { \bf p } _ { k - 1 / 2 } \big ) \Big ) . } \end{array}
$$

The integrator (2.54) is a two-step integrator which preserves $\mathrm { d } p _ { k } \wedge \mathrm { d } q _ { k + 1 } .$ . In this case, we cannot find an one-step integrator which is equivalent to (2.54). In conclusion, using discrete total variation calculus, we have derived two-step symplectic-energy integrators. When taking fixed time steps, some of them are equivalent to one-step integrators derived directly from the Hamiltonian system while the others do not have this equivalence.

# 14.2.4 High Order Symplectic-Energy Integrator

In this subsection, we will develop high order symplectic-energy integrators by using the generating function of the flow of the Hamiltonian system

$$
\dot { { \pmb z } } = J \nabla H ( { \pmb z } ) ,
$$

where

$$
\begin{array} { r } { \boldsymbol { z } = ( \pmb { p } , \pmb { q } ) ^ { \mathrm { T } } , \qquad \boldsymbol { J } = \biggl ( \begin{array} { c c } { O } & { - I } \\ { I } & { O } \end{array} \biggr ) . } \end{array}
$$

Let us first recall the generating function with normal Darboux matrix of a symplectic transformation. For details, see Chapters 5 and 6, or [Fen86,FWQW89] .

Suppose $\alpha$ is a $4 n \times 4 n$ nonsingular matrix with the form

$$
\alpha = \left( \begin{array} { c c } { { A } } & { { B } } \\ { { C } } & { { D } } \end{array} \right) ,
$$

where $A , B , C$ and $D$ are both $2 n \times 2 n$ matrices.

We denote the inverse of $\alpha$ by

$$
\alpha ^ { - 1 } = \left( \begin{array} { c c } { { A _ { 1 } } } & { { B _ { 1 } } } \\ { { C _ { 1 } } } & { { D _ { 1 } } } \end{array} \right) ,
$$

where $A _ { 1 } , B _ { 1 } , C _ { 1 }$ and $D _ { 1 }$ are both $2 n \times 2 n$ matrices. We know that a $4 n \times 4 n$ matrix $\alpha$ is a Darboux matrix if

$$
\alpha ^ { \mathrm { T } } J _ { 4 n } \alpha = \widetilde { J } _ { 4 n } ,
$$

where

$$
\begin{array} { r } { J _ { 4 n } = \left( \begin{array} { c c } { O } & { - I _ { 2 n } } \\ { I _ { 2 n } } & { O } \end{array} \right) , \quad \tilde { J } _ { 4 n } = \left( \begin{array} { c c } { J _ { 2 n } } & { O } \\ { O } & { - J _ { 2 n } } \end{array} \right) , \quad J _ { 2 n } = \left( \begin{array} { c c } { O } & { - I _ { n } } \\ { I _ { n } } & { O } \end{array} \right) , } \end{array}
$$

where $I _ { n }$ is an $n \times n$ identity matrix and $I _ { 2 n }$ is a $2 n \times 2 n$ identity matrix.

Every Darboux matrix induces a fractional transform between symplectic and symmetric matrices

$$
{ \begin{array} { r l } & { \sigma _ { \alpha } : S p ( 2 n ) \longrightarrow S m ( 2 n ) , } \\ & { \sigma _ { \alpha } = ( A S + B ) ( C S + D ) ^ { - 1 } = M , \quad { \mathrm { f o r } } \quad S \in S p ( 2 n ) , { \mathrm { ~ d e t } } ( C S + D ) \neq 0 } \end{array} }
$$

with the inverse transform $\sigma _ { \alpha } ^ { - 1 } = \sigma _ { \alpha _ { - 1 } }$

$$
\begin{array} { l } { { \sigma _ { \alpha } ^ { - 1 } : \ S m ( 2 n ) \longrightarrow S p ( 2 n ) , } } \\ { { \sigma _ { \alpha } = ( A _ { 1 } M + B _ { 1 } ) ( C _ { 1 } M + D _ { 1 } ) ^ { - 1 } = S , } } \end{array}
$$

where $S p ( 2 n )$ is the group of symplectic matrices and $S m ( 2 n )$ the set of symmetric matrices.

We can generalize the above discussions to nonlinear transformations on $\mathbb { R } ^ { 2 n }$ . Let us denote the set of symplectic transformations on $\mathbb { R } ^ { 2 n }$ by $S p D _ { 2 n }$ and the set of symmetric transformations (i.e., transformations with symmetric Jacobian) on $\mathbb { R } ^ { 2 n }$ by $S y m m ( 2 n )$ . Every $f \in S y m m ( 2 n )$ corresponds, at least locally, to a real function $\phi$ (unique to a constant) such that $f$ is the gradient of $\phi$ ,

$$
f ( { \pmb w } ) = \nabla \phi ( { \pmb w } ) ,
$$

where $\nabla \phi ( { \pmb w } ) = \left( \phi _ { w _ { 1 } } ( { \pmb w } ) , \cdots , \phi _ { w _ { 2 n } } ( { \pmb w } ) \right)$ and ${ \pmb w } = ( w _ { 1 } , w _ { 2 } , \cdot \cdot \cdot , w _ { 2 n } )$

Then, we have

$$
\begin{array} { r l } & { \sigma _ { \alpha } : S p D _ { 2 n } \longrightarrow S y m m ( 2 n ) , } \\ & { \sigma _ { \alpha } = ( A \circ g + B ) \circ ( C \circ g + D ) ^ { - 1 } = \nabla \phi , \mathrm { f o r } g \in S p D _ { 2 n } , \mathrm { d e t } ( C g _ { z } + D ) \neq 0 } \end{array}
$$

or alternatively

$$
A g ( \pmb { z } ) + B \pmb { z } = ( \nabla \phi ) ( C g ( \pmb { z } ) + D \pmb { z } ) ,
$$

where $\circ$ denotes the composition of transformation and the $2 n \times 2 n$ constant matrices $A , B , C$ and $D$ are regarded as linear transformations. $g _ { z }$ denotes the Jacobian of symplectic transformation $g$ .

Let $\phi$ be the generating function of Darboux type $\alpha$ for symplectic transformation $g$ .

Conversely, we have

$$
\begin{array} { r l } & { \frac { - 1 } { \alpha } : S y m m \left( 2 n \right) \longrightarrow S p D _ { 2 n } , } \\ & { \frac { - 1 } { \alpha } ( \nabla \phi ) = \left( A _ { 1 } \circ \nabla \phi + B _ { 1 } \right) \circ ( C _ { 1 } \circ \nabla \phi + D _ { 1 } ) ^ { - 1 } = g , \mathrm { f o r } \mathrm { d e t } ( C _ { 1 } \phi _ { w w } + D _ { 1 } ) \ne 0 , } \end{array}
$$

or alternatively

$$
A _ { 1 } \nabla \phi ( \pmb { w } ) + B _ { 1 } \pmb { w } = g \big ( C _ { 1 } \nabla \phi ( \pmb { w } ) + D _ { 1 } \pmb { w } \big ) ,
$$

where $g$ is called the symplectic transformation of Darboux type $\alpha$ for the generating function $\phi$ .

For the study of integrators, we will restrict ourselves to normal Darboux matrices, i.e., those satisfying $A + B = 0 , C + D = I _ { 2 n }$ . The normal Darboux matrices can be characterized as

$$
\alpha = \left( \begin{array} { c c } { { J _ { 2 n } } } & { { - J _ { 2 n } } } \\ { { E } } & { { I _ { 2 n } - E } } \end{array} \right) , \quad E = \frac { 1 } { 2 } ( I _ { 2 n } + J _ { 2 n } F ) , \quad F ^ { \mathrm { T } } = F ,
$$

and

$$
\alpha ^ { - 1 } = \left( \begin{array} { c c } { { ( E - I _ { 2 n } ) J _ { 2 n } } } & { { I _ { 2 n } } } \\ { { E J _ { 2 n } } } & { { I _ { 2 n } } } \end{array} \right) .
$$

The fractional transform induced by a normal Darboux matrix establishes a oneone correspondence between symplectic transformations near identity and symmetric transformations near nullity.

For simplicity, we will take $F = 0$ , then $E = \frac { 1 } { 2 } I _ { 2 n }$ and

$$
\begin{array} { r } { \alpha = \left( \begin{array} { c c } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } I _ { 2 n } } & { \frac { 1 } { 2 } I _ { 2 n } } \end{array} \right) . } \end{array}
$$

Now, we will consider the generating function of the flow of (2.55) and denote it by $e _ { H } ^ { t }$ . The generating function $\phi ( { \pmb w } , t )$ for the flow $e _ { H } ^ { t }$ of Darboux type (2.60) is given by

$$
\nabla \phi = { \bigl ( } J _ { 2 n } \circ e _ { H } ^ { t } - J _ { 2 n } { \bigr ) } \circ { \Bigl ( } { \frac { 1 } { 2 } } e _ { H } ^ { t } + { \frac { 1 } { 2 } } I _ { 2 n } { \Bigr ) } ^ { - 1 } , \quad { \mathrm { ~ f o r ~ s m a l l ~ } } \quad | t | ,
$$

where $\phi ( { \pmb w } , t )$ satisfies the Hamilton–Jacobi equation

$$
\frac { \partial } { \partial t } \phi ( { \pmb w } , t ) = - H \Big ( { \pmb w } + \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ( { \pmb w } , t ) \Big )
$$

and can be expressed by Taylor series in $t$ ,

$$
\phi ( { \pmb w } , t ) = \sum _ { k = 1 } ^ { \infty } \phi ^ { k } ( { \pmb w } ) t ^ { k } , \quad \mathrm { f o r ~ s m a l l } \quad | t | .
$$

The coefficients $\phi ^ { k } ( w )$ can be determined recursively as

$$
\begin{array} { l l l } { \phi ^ { 1 } ( { \pmb w } ) } & { = } & { \displaystyle - H ( { \pmb w } ) , } \\ { \phi ^ { k + 1 } ( { \pmb w } ) } & { = } & { \displaystyle \frac { - 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { \stackrel { { . . . } } { j _ { 1 } } + . . . + j _ { m } = k } D ^ { m } H \bigg ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { 1 } } , \cdots , \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { m } } \bigg ) , } \\ & & { \quad \quad \quad \quad \quad \quad j _ { l } \geq 1 } \end{array}
$$

where $k \geq 1$ , and we use the notation of the $m$ -linear form

$$
\begin{array} { l } { { \displaystyle D ^ { m } H \Big ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { 1 } } , \cdot \cdot \cdot , \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { m } } \Big ) } \ ~ } \\ { { \displaystyle ~ : = \sum _ { i _ { 1 } , \cdot \cdot \cdot , i _ { m } = 1 } ^ { 2 n } H _ { z _ { i _ { 1 } } \cdot \cdot \cdot \cdot z _ { i _ { m } } } ( z ) \Big ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { 1 } } ( { \pmb w } ) \Big ) _ { i _ { 1 } } \cdot \cdot \cdot \Big ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { m } } ( { \pmb w } ) \Big ) _ { i _ { m } } } . } \end{array}
$$

From (2.61), we can see that the phase flow $\widehat { \pmb z } : = e _ { H } ^ { t } \pmb { z }$ satisfies

$$
J _ { 2 n } ( { \widehat { z } } - z ) = \nabla \phi \Bigl ( \frac { { \widehat { z } } - z } { 2 } \Bigr ) = \sum _ { j = 1 } ^ { \infty } t ^ { j } \nabla \phi ^ { j } \Bigl ( \frac { { \widehat { z } } + z } { 2 } \Bigr ) .
$$

Now, we will choose $\mathbb { L }$ in (2.31) as

$$
\mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) = \pmb { p } _ { k + 1 / 2 } \frac { \pmb { q } _ { k + 1 } - \pmb { q } _ { k } } { t _ { k + 1 } - t _ { k } } - \psi ^ { m } ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) ,
$$

where

$$
\psi ^ { m } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) = \sum _ { j = 1 } ^ { m } t ^ { j } \phi ^ { j } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) .
$$

The corresponding symplectic-energy integrator (2.33) and (2.34) is

$$
\frac {  { \mathbf { \ell } } _ { k + 1 } -  { \mathbf { q } } _ { k - 1 } } { 2 } - \frac { 1 } { 2 }  { \left( ( t _ { k + 1 } - t _ { k } ) \frac { \partial \psi ^ { m } } { \partial p } ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial \psi ^ { m } } { \partial p } ( \pmb { q } _ { k - 1 / 2 } , \pmb { p } _ { k - 1 / 2 } ) \right) } = 0
$$

$$
\begin{array} { r l } & { \displaystyle \longrightarrow - \frac { 1 } { 2 } \Big [ \big ( t _ { k + 1 } - t _ { k } \big ) \frac { 1 } { \partial { \pmb p } } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { 1 } { \partial { \pmb p } } ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } ) \Big ] = 0 } \\ & { \displaystyle \qquad \overset { , . . . } { \longrightarrow } + \frac { 1 } { 2 } \bigg ( ( t _ { k + 1 } - t _ { k } ) \frac { \partial \psi ^ { m } } { \partial { \pmb q } } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial \psi ^ { m } } { \partial { \pmb q } } ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } ) \bigg ) = 0 } \\ & { \displaystyle \qquad \psi ^ { m } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) = \psi ^ { m } ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } ) , } \end{array}
$$

which satisfies the discrete extended canonical 2-form

$$
\frac { 1 } { 2 } ( \mathrm { d } p _ { k } \wedge \mathrm { d } q _ { k + 1 } + \mathrm { d } p _ { k + 1 } \wedge \mathrm { d } q _ { k } ) - \psi ^ { m } ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) \wedge \Big ( \frac { \mathrm { d } t _ { k } + \mathrm { d } t _ { k + 1 } } { 2 } \Big ) .
$$

The integrator (2.68) is a two-step symplectic-energy integrator with $2 m$ -th order of accuracy.

# 14.2.5 An Example and an Optimization Method

In this subsection, we will see an example. We will take the Hamiltonian as

$$
H ( q , p ) = { \frac { 1 } { 2 } } p ^ { 2 } + { \frac { 1 } { 2 } } ( q ^ { 4 } - q ^ { 2 } ) ,
$$

where $q$ and $p$ are scalars.

Corresponding to (2.70) the discrete Lagrangian (2.31) is chosen as

$$
\mathbb { L } \big ( t _ { k } , q _ { k } , p _ { k } , t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 } \big ) = p _ { k + 1 / 2 } \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } - \frac { 1 } { 2 } \big ( q _ { k + 1 / 2 } ^ { 4 } - q _ { k + 1 / 2 } ^ { 2 } \big ) .
$$

The corresponding symplectic-energy integrator (2.33) and (2.34) become

$$
\begin{array} { r l r } & { \frac { q _ { k + 1 } - q _ { k - 1 } } { 2 } - \frac { 1 } { 2 } ( ( t _ { k + 1 } - t _ { k } ) p _ { k + 1 / 2 } + ( t _ { k } - t _ { k - 1 } ) p _ { k - 1 / 2 } ) = 0 , } & { ( 2 . 7 \times \frac { 1 } { 2 } ) } \\ & { \frac { p _ { k + 1 } - p _ { k - 1 } } { 2 } + \frac { 1 } { 2 } ( ( t _ { k + 1 } - t _ { k } ) ( 2 q _ { k + 1 / 2 } ^ { 3 } - q _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) ( 2 q _ { k - 1 / 2 } ^ { 3 } - q _ { k - 1 / 2 } ) ) = 0 , } & \\ & { \frac { 1 } { 2 } p _ { k + 1 / 2 } ^ { 2 } + \frac { 1 } { 2 } ( q _ { k + 1 / 2 } ^ { 4 } - q _ { k + 1 / 2 } ^ { 2 } ) = \frac { 1 } { 2 } p _ { k - 1 / 2 } ^ { 2 } + \frac { 1 } { 2 } ( q _ { k - 1 / 2 } ^ { 4 } - q _ { k - 1 / 2 } ^ { 2 } ) , } & \end{array}
$$

where ${ t _ { k - 1 } , q _ { k - 1 } , p _ { k - 1 } }$ and $t _ { k } , q _ { k } , p _ { k }$ are given and $t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 }$ are unknowns.

In the following numerical experiment, we will use a robust optimization method suggested in $\left[ { \mathrm { K M O 9 } } { \bar { 9 } } \right]$ to solve (2.72). Concretely, let

$$
\begin{array} { r l } & { \quad A = \frac { q _ { k + 1 } - q _ { k - 1 } } { 2 } - \frac { 1 } { 2 } \Big ( ( t _ { k + 1 } - t _ { k } ) p _ { k + 1 / 2 } + ( \stackrel {  } { t _ { k } } - t _ { k - 1 } ) p _ { k - 1 / 2 } \Big ) , } \\ & { \quad B = \frac { p _ { k + 1 } - p _ { k - 1 } } { 2 } + \frac { 1 } { 2 } \Big ( ( t _ { k + 1 } - t _ { k } ) ( 2 q _ { k + 1 / 2 } ^ { 3 } - q _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) ( 2 q _ { k - 1 / 2 } ^ { 3 } - q _ { k - 1 / 2 } ) \Big ) , } \\ & { \quad C = \frac { 1 } { 2 } p _ { k + 1 / 2 } ^ { 2 } + \frac { 1 } { 2 } ( q _ { k + 1 / 2 } ^ { 4 } - q _ { k + 1 / 2 } ^ { 2 } ) - \frac { 1 } { 2 } p _ { k - 1 / 2 } ^ { 2 } - \frac { 1 } { 2 } ( q _ { k - 1 / 2 } ^ { 4 } - q _ { k - 1 / 2 } ^ { 2 } ) . } \end{array}
$$

Then, we will minimize the quantity

$$
F = A ^ { 2 } + B ^ { 2 } + C ^ { 2 }
$$

![](images/e2b288f67fcabe806081dbef8ba6dab35afa65f0dcebbccecd54263c28c377ab.jpg)  
Fig. 2.1. The orbits calculated by (2.72), (2.74) left plot $q _ { 0 } = 0 . 7 7$ , $p _ { 0 } = 0$ and right plot $q _ { 0 } = 0 . 9 9$ , $p _ { 0 } = 0$

![](images/729025c504697de64300c080d6625bcc95c2d0e31f7113488a33eab46924e6c7.jpg)  
Fig. 2.2. The energy evaluation by (2.72), (2.74) left plot $q _ { 0 } = 0 . 7 7$ , $p _ { 0 } = 0$ and right plot $q _ { 0 } = 0 . 9 9$ , $p _ { 0 } = 0$

over $q _ { k + 1 } , p _ { k + 1 }$ and $t _ { k + 1 }$ under the constraint $t _ { k + 1 } > t _ { k }$ . This constraint guarantees that no singularities occur in choosing time steps.

We will compare (2.72) with the following integrator with fixed time steps:

$$
\begin{array} { r l } & { \frac { q _ { k + 1 } - q _ { k - 1 } } { 2 h } - \frac { 1 } { 2 } ( p _ { k + 1 / 2 } + p _ { k - 1 / 2 } ) = 0 , } \\ & { \frac { p _ { k + 1 } - p _ { k - 1 } } { 2 h } + \frac { 1 } { 2 } \big ( ( 2 q _ { k + 1 / 2 } ^ { 3 } - q _ { k + 1 / 2 } ) + ( 2 q _ { k - 1 / 2 } ^ { 3 } - q _ { k - 1 / 2 } ) \big ) = 0 . } \end{array}
$$

In our numerical experiment, we use two initial conditions $q _ { 0 } = 0 . 7 7 , p _ { 0 } = 0 , t =$ 0 and $q _ { 0 } = 0 . 9 9 , p _ { 0 } = 0 , t = 0 .$ . To obtain $q _ { 1 }$ and $p _ { 1 }$ , we apply the midpoint integrator with $t _ { 1 } = 0 . 1$ . In Fig. 2.1, the orbits calculated by (2.72) and (2.74) are shown for the two initial conditions. The two orbits in each initial condition are almost indistinguishable. In Fig.2.2, we plot the evolution of the energy $H ( q _ { k + 1 / 2 } , p _ { k + 1 / 2 } )$ for both (2.72) and (2.74). The oscillating curve is for (2.74) and the lower line for (2.72). For more numerical examples, see $\left[ \mathrm { K M O 9 9 } \right]$ in the Lagrangian setting. In principle, the results $\mathrm { i n } ^ { \mathrm { [ K M O 9 9 ] } }$ apply to the Hamiltonian setting in the present method as well taking ${ \frac { q _ { k + 1 } - q _ { k } } { h } } = p _ { k + 1 / 2 } .$ . The purpose is to develop a discrete total variation calculus in the Hamiltonian setting and obtain the symplectic-energy integrators. The comprehensive implementation of the obtained integrators is not the subject of present and will be a topic for future research.

# 14.2.6 Concluding Remarks

We will develop a discrete total variation calculus in Hamiltonian formalism in this subsection. This calculus provides a new method for constructing structure-preserving integrators for Hamiltonian system from a variational point of view. Using this calculus, we will derive the energy conservation laws associated with integrators. The coupled integrators are two-step integrators and preserve a discrete version of the extended canonical 2-form. If we take fixed time steps, the resulting integrators are equivalent to the symplectic integrators derived directly from the Hamiltonian systems only in special cases. Thus, new two-step symplectic integrators are variationally obtained. Using generating function method, we will also obtain higher order symplectic-energy integrators.

In principle, our discussions can be generalized to multisymplectic Hamiltonian system

$$
M z _ { t } + K z _ { x } = \nabla _ { x } H ( z ) , \quad z \in \mathbb { R } ^ { n } ,
$$

where $M$ and $K$ are skew-symmetric matrices on $\mathbb { R } ^ { n } ( n \geq 3 )$ and $S : R ^ { n } \to R$ is a smooth function $[ \mathrm { B r i 9 7 } , \mathrm { B D 0 1 } ]$ . We call the above-mentioned system a multisymplectic Hamiltonian system, since it possesses a multisymplectic conservation law

$$
\frac { \partial } { \partial t } \omega + \frac { \partial } { \partial x } \kappa = 0 ,
$$

where $\omega$ and $\kappa$ are the presymplectic forms

$$
\omega = \frac { 1 } { 2 } \mathsf { d } z \wedge M \mathsf { d } z , \quad \kappa = \frac { 1 } { 2 } \mathsf { d } z \wedge K \mathsf { d } z .
$$

The constructed action functional is

$$
S = \int { \Bigl ( } { \frac { 1 } { 2 } } z ^ { \operatorname { T } } ( M z _ { t } + K z _ { x } ) - H ( z ) { \Bigr ) } \mathrm { d } x \wedge \mathrm { d } t .
$$

Performing total variation on (2.77), we can obtain the multisymplectic Hamiltonian system (2.75), the corresponding local energy conservation law

$$
\frac { \partial } { \partial t } \Bigl ( S ( z ) - \frac { 1 } { 2 } z ^ { \mathrm { T } } K z _ { x } \Bigr ) + \frac { \partial } { \partial x } \Bigl ( \frac { 1 } { 2 } z ^ { \mathrm { T } } K z _ { t } \Bigr ) = 0 ,
$$

and the local momentum conservation law

$$
\frac { \partial } { \partial t } \Big ( \frac { 1 } { 2 } z ^ { \mathrm { T } } M z _ { x } \Big ) + \frac { \partial } { \partial x } \Big ( S ( z ) - \frac { 1 } { 2 } z ^ { \mathrm { T } } M z _ { t } \Big ) = 0 .
$$

In the same way, we can develop a discrete total variation in the multisymplectic form and obtain multisymplectic-energy-momentum integrators. This will be discussed in detail in Chapter 16.


<!-- chunk 0010: pages 631-700 -->
# 14.3 Discrete Mechanics Based on Finite Element Methods

Now, we will consider mechanics based on finite element methods. Let us go back to the variation problem of the action factional (1.1). The finite element method is an approximate method for solving the variation problem. Instead of solving the variation problem in the space $\textstyle { \mathcal { C } } ^ { 2 } ( [ a , b ] )$ , the finite element method solves the problem in a subspace $V _ { h ^ { m } } ( [ a , b ] )$ of $ { \mathcal { C } } ^ { 2 } ( [ a , b ] )$ . $V _ { h ^ { m } } ( [ a , b ] )$ consists of piecewise $m$ -degree polynomials interpolating the curves $q ( t ) \in \mathcal { C } ^ { 2 } ( [ a , b ] )$ .

# 14.3.1 Discrete Mechanics Based on Linear Finite Element

First, let us consider the piecewise linear interpolation. Given a partition of $[ a , b ]$

$$
a = t _ { 0 } < t _ { 1 } < \cdot \cdot \cdot < t _ { k } < \cdot \cdot \cdot < t _ { N - 1 } < t _ { n } = b ,
$$

the intervals $I _ { k } = [ t _ { k } , t _ { k + 1 } ]$ are called elements. $h _ { k } = t _ { k + 1 } - t _ { k } . V _ { h } ( [ a , b ] )$ consists of piecewise linear function interpolating $q ( t )$ at $( t _ { k } , q _ { k } ) ( k = 0 , 1 , \cdots , N )$ . Now, we will derive the expressions of $q _ { h } ( t ) \in V _ { h } ( [ a , b ] )$ . First, we will construct the basis functions $\varphi _ { k } ( t )$ , which are piecewise linear functions on $[ a , b ]$ satisfying $\varphi _ { k } ( t _ { i } ) =$ $\delta _ { k } ^ { i }$ $( i , k = 0 , 1 , \cdots , N )$ .

$$
\begin{array} { r l } & { \varphi _ { 0 } ( t ) = \left\{ \begin{array} { l l } { \displaystyle 1 - \frac { t - t _ { 0 } } { h _ { 0 } } , } & { t _ { 0 } \leq t \leq t _ { 1 } ; } \\ { \displaystyle 0 , } & { \mathrm { o t h e r w i s e } ; } \end{array} \right. } \\ & { \varphi _ { N } ( t ) = \left\{ \begin{array} { l l } { \displaystyle 1 + \frac { t - t _ { N } } { h _ { N - 1 } } , } & { t _ { N - 1 } \leq t \leq t _ { N } ; } \\ { \displaystyle 0 , } & { \mathrm { o t h e r w i s e } ; } \end{array} \right. } \end{array}
$$

and for $k = 1 , 2 , \cdots , N - 1$ ,

$$
\varphi _ { k } ( t ) = \left\{ \begin{array} { l l } { 1 + \frac { t - t _ { k } } { h _ { k - 1 } } , } & { t _ { k - 1 } \leq t \leq t _ { k } ; } \\ { 1 - \frac { t - t _ { k } } { h _ { k } } , } & { t _ { k } \leq t \leq t _ { k + 1 } ; } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

Using these basis functions, we obtain the expression $q _ { h } \in V _ { h } ( [ a , b ] )$ :

$$
q _ { h } ( t ) = \sum _ { k = 0 } ^ { N } q _ { k } \varphi _ { k } ( t ) .
$$

In the space $V _ { h } ( [ a , b ] )$ , the action functional (1.1) becomes

$$
S { \big ( } ( t , q _ { h } ( t ) ) { \big ) } \ = \ \int _ { a } ^ { b } L ( t , q _ { h } ( t ) , { \dot { q } } _ { h } ( t ) ) \mathrm { d } t
$$

$$
\begin{array} { r l } { = } & { { } \displaystyle \sum _ { k = 0 } ^ { N - 1 } \int _ { t _ { k } } ^ { t _ { k + 1 } } L \left( t , \displaystyle \sum _ { i = 0 } ^ { N } ( q _ { i } \varphi _ { i } ( t ) , \frac { \mathrm { d } } { \mathrm { d } t } \sum _ { i = 0 } ^ { N } ( q _ { i } \varphi _ { i } ( t ) ) \right) \mathrm { d } t } \\ { = } & { { } \displaystyle \sum _ { k = 0 } ^ { N - 1 } \mathbb { L } \big ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } \big ) \big ( { t _ { k + 1 } - t _ { k } } \big ) , } \end{array}
$$

where

$$
\begin{array} { r c l } { \mathbb { L } \big ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } \big ) } & { = } & { \displaystyle \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } L \left( t , \sum _ { i = 0 } ^ { N } ( q _ { i } \varphi _ { i } ( t ) , \frac { \mathrm { d } } { \mathrm { d } t } \sum _ { i = 0 } ^ { N } ( q _ { i } \varphi _ { i } ( t ) ) \right) \mathrm { d } t } \\ & { = } & { \displaystyle \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } L \left( t , \sum _ { i = k } ^ { k + 1 } ( q _ { i } \varphi _ { i } ( t ) , \frac { \mathrm { d } } { \mathrm { d } t } \sum _ { i = k } ^ { k + 1 } ( q _ { i } \varphi _ { i } ( t ) ) \right) \mathrm { d } t . } \end{array}
$$

Therefore, restricting to the subspace $V _ { h } ( [ a , b ] )$ of $\textstyle { \mathcal { C } } ^ { 2 } ( [ a , b ] )$ , the original variational problem reduces to the extremum problem of the function (3.4) in $q _ { k }$ $k =$ $0 , 1 , \cdots , N )$ . Note that (3.4) is one of the discrete actions (1.33). Thus, what remains to be done is just to perform the same calculation on (3.4) as on (1.33). We can then obtain the discrete Euler–Lagrange equation (1.35) which preserves the discrete Lagrange 2-form (1.48). Therefore, discrete mechanics based on finite element methods consists of two steps: first, use finite element methods to obtain a kind of discrete Lagrangian, second, use the method of Veselov mechanics to obtain the variational integrators.

Let us consider the previous example again. For the classical Lagrangian (1.57), we choose the discrete Lagrangian $\mathbb { L } ( \bar { t _ { k } } , q _ { k } , \bar { t } _ { k + 1 } , q _ { k + 1 } )$ as

$$
\begin{array} { r l } & { \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) } \\ & { = \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } \left( \frac { 1 } { 2 } \left( \frac { \mathrm { d } } { \mathrm { d } t } \sum _ { i = 0 } ^ { N } ( q _ { i } \varphi _ { i } ( t ) ) \right) ^ { 2 } - V \left( \underset { i = 0 } { \overset { N } { \sum } } ( q _ { i } \varphi _ { i } ( t ) ) \right) \right) \mathrm { d } t } \\ & { = \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } \left( \frac { 1 } { 2 } \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) ^ { 2 } - V \left( \frac { t _ { k + 1 } - t } { t _ { k + 1 } - t _ { k } } q _ { k } + \frac { t - t _ { k } } { t _ { k + 1 } - t _ { k } } q _ { k + 1 } \right) \right) \mathrm { d } t } \\ & { = \frac { 1 } { 2 } \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) ^ { 2 } - F ( q _ { k } , q _ { k + 1 } ) , } \end{array}
$$

where

$$
F ( q _ { k } , q _ { k + 1 } ) = { \frac { 1 } { t _ { k + 1 } - t _ { k } } } \int _ { t _ { k } } ^ { t _ { k + 1 } } V \left( { \frac { t _ { k + 1 } - t } { t _ { k + 1 } - t _ { k } } } q _ { k } + { \frac { t - t _ { k } } { t _ { k + 1 } - t _ { k } } } q _ { k + 1 } \right) \mathrm { d } t .
$$

The discrete Euler–Lagrange equation (1.35) becomes

$$
\begin{array} { r l } & { \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } - \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) + \frac { \partial F ( q _ { k } , q _ { k + 1 } ) } { \partial q _ { k } } ( t _ { k + 1 } - t _ { k } ) } \\ & { + \frac { \partial F ( q _ { k - 1 } , q _ { k } ) } { \partial q _ { k } } ( t _ { k } - t _ { k - 1 } ) = 0 , } \end{array}
$$

which preserves the Lagrange 2-form

$$
\left( \frac { 1 } { t _ { k + 1 } - t _ { k } } + ( t _ { k + 1 } - t _ { k } ) \frac { \partial ^ { 2 } F ( q _ { k } , q _ { k + 1 } ) } { \partial q _ { k } \partial q _ { k + 1 } } \right) \mathbf { d } q _ { k + 1 } \wedge \mathbf { d } q _ { k } .
$$

Again, if we take fixed time steps $t _ { k + 1 } - t _ { k } = t _ { k } - t _ { k - 1 } = h$ , (3.8) becomes

$$
\frac { q _ { k + 1 } - 2 q _ { k } + q _ { k - 1 } } { h ^ { 2 } } + \frac { \partial F ( q _ { k } , q _ { k + 1 } ) } { \partial q _ { k } } + \frac { \partial F ( q _ { k - 1 } , q _ { k } ) } { \partial q _ { k } } = 0 ,
$$

which preserves the Lagrange 2-form

$$
\left( \frac { 1 } { h } + h \frac { \partial ^ { 2 } F ( q _ { k } , q _ { k + 1 } ) } { \partial q _ { k } \partial q _ { k + 1 } } \right) \textrm { d } q _ { k + 1 } \wedge \textrm { d } q _ { k } .
$$

Suppose $q _ { k }$ is the solution of (3.8) and $q ( t )$ is the solution of

$$
\frac { \mathrm { d } ^ { 2 } q } { \mathrm { d } t ^ { 2 } } + \frac { \partial V ( q ) } { \partial q } = 0 ,
$$

then from the convergence theory of finite element methods $[ \mathrm { C i a } 7 8 , \mathrm { F e n } 6 5 ]$ , we have

$$
\| q ( t ) - q _ { h } ( t ) \| \leq C h ^ { 2 } ,
$$

where $\parallel \cdot \parallel$ is the $L ^ { 2 }$ norm. $q _ { h } ( t ) = \sum _ { k = 0 } ^ { N } q _ { k } , \ h = \operatorname* { m a x } _ { k } \{ h _ { k } \}$ and $C$ is a constant independent of $h$ .

If we use midpoint numerical integration formula in (3.7), we obtain

$$
{ \begin{array} { r l } { F ( q _ { k } , q _ { k + 1 } ) } & { = { \frac { 1 } { t _ { k + 1 } - t _ { k } } } \int _ { t _ { k } } ^ { t _ { k + 1 } } V \left( { \frac { t _ { k + 1 } - t } { t _ { k + 1 } - t _ { k } } } q _ { k } + { \frac { t - t _ { k } } { t _ { k + 1 } - t _ { k } } } q _ { k + 1 } \right) \mathrm { d } t } \\ & { \approx v \left( { \frac { q _ { k } + q _ { k + 1 } } { 2 } } \right) . } \end{array} }
$$

In this case, (3.8) is the same as (1.59). We can also use trapezoid formula or Simpson formula and so on to integrate (3.7) numerically and obtain another kind of discrete Lagrangian.

# 14.3.2 Discrete Mechanics with Lagrangian of High Order

Now, we will consider piecewise quadratic polynomial interpolation, which will result in a kind of discrete Lagrangian of high order. To this aim, we add an auxiliary node $t _ { k + \frac 1 2 }$ to each element $I _ { k } = [ t _ { k } , t _ { k + 1 } ]$ . There are two kinds of quadratic basis functions: $\phi _ { k } ( t )$ for nodes $t _ { k }$ and $\phi _ { k + \frac 1 2 } ( t )$ for $t _ { k + \frac 1 2 }$ that satisfy

$$
\begin{array} { l l } { { \phi _ { k } ( t _ { i } ) = \delta _ { i } ^ { k } , } } & { { \phi _ { k } \left( t _ { i + \frac { 1 } { 2 } } \right) = 0 , } } \\ { { \phi _ { k + \frac { 1 } { 2 } } \left( t _ { i + \frac { 1 } { 2 } } \right) = \delta _ { i } ^ { k } , } } & { { \phi _ { k + \frac { 1 } { 2 } } ( t _ { i } ) = 0 , \quad i , k = 0 , 1 , \cdots , N . } } \end{array}
$$

We have the basis functions as follows:

$$
\begin{array} { r l } & { \phi _ { 0 } ( t ) = \left\{ \begin{array} { l l } { \Big ( \frac { 2 ( t - t _ { 0 } ) } { h _ { 0 } } - 1 \Big ) \Big ( \frac { t - t _ { 0 } } { h _ { 0 } } - 1 \Big ) , } & { t _ { 0 } \leq t \leq t _ { 1 } ; } \\ { 0 , } & { \mathrm { o t h e r w i s e } ; } \end{array} \right. } \\ & { \phi _ { N } ( t ) = \left\{ \begin{array} { l l } { \Big ( \frac { 2 ( t _ { N } - t ) } { h _ { N - 1 } } - 1 \Big ) \Big ( \frac { t _ { N } - t } { h _ { N - 1 } } - 1 \Big ) , } & { t _ { N - 1 } \leq t \leq t _ { N } ; } \\ { 0 , } & { \mathrm { o t h e r w i s e } ; } \end{array} \right. } \end{array}
$$

and for $k = 1 , 2 , \cdots , N - 1$ ,

$$
\begin{array} { r } { \phi _ { k } ( t ) = \left\{ \begin{array} { l l } { \left( \frac { 2 ( t _ { k } - t ) } { h _ { k - 1 } } - 1 \right) \left( \frac { t _ { k } - t } { h _ { k - 1 } } - 1 \right) , } & { t _ { k - 1 } \leq t \leq t _ { k } ; } \\ { \left( \frac { 2 ( t - t _ { k } ) } { h _ { k } } - 1 \right) \left( \frac { t - t _ { k } } { h _ { k } } - 1 \right) , } & { t _ { k } \leq t \leq t _ { k + 1 } ; } \\ { 0 , } & { \mathrm { o t h e r w i s e } ; } \end{array} \right. } \end{array}
$$

and for $k = 0 , 1 , \cdots , N - 1$ ,

$$
\phi _ { k + \frac { 1 } { 2 } } ( t ) = \left\{ \begin{array} { l l } { 4 \frac { t - t _ { k } } { h _ { k } } \left( 1 - \frac { t - t _ { k } } { h _ { k } } \right) , } & { t _ { k } \leq t \leq t _ { k + 1 } ; } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

Using these basis functions, we will construct subspace $V _ { h ^ { 2 } } ( [ a , b ] )$ of $\textstyle { \mathcal { C } } ^ { 2 } ( [ a , b ] )$ :

$$
q _ { h ^ { 2 } } ( t ) = \sum _ { k = 0 } ^ { N } q _ { k } \phi _ { k } ( t ) + \sum _ { k = 0 } ^ { N - 1 } q _ { k + \frac { 1 } { 2 } } \phi _ { k + \frac { 1 } { 2 } } ( t ) , \quad q _ { h ^ { 2 } } ( t ) \in V _ { h ^ { 2 } } ( [ a , b ] ) .
$$

In the space $V _ { h ^ { 2 } } ( [ a , b ] )$ , the action functional (1.1) becomes

$$
\begin{array} { r c l } { S \big ( ( t , q _ { h ^ { 2 } } ( t ) ) \big ) } & { = } & { \displaystyle \int _ { a } ^ { b } L \big ( t , q _ { h ^ { 2 } } ( t ) , \dot { q } _ { h ^ { 2 } } ( t ) \big ) \mathrm { d } t } \\ & { = } & { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \int _ { t _ { k } } ^ { t _ { k + 1 } } L \big ( t , q _ { h ^ { 2 } } ( t ) , \dot { q } _ { h ^ { 2 } } ( t ) \big ) \mathrm { d } t } \\ & { = } & { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \mathbb { L } \big ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } \big ) \big ( t _ { k + 1 } - t _ { k } \big ) , } \end{array}
$$

where

$$
\mathbb { L } \big ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } \big ) = \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } L \big ( t , q _ { h ^ { 2 } } ( t ) , \dot { q } _ { h ^ { 2 } } ( t ) \big ) \mathrm { d } t .
$$

For the discrete action (3.17), we have

$$
\begin{array} { l } { { { 1 5 ( g _ { 0 , \phi _ { 1 } } , \phi _ { 1 } , \dots , \phi _ { g _ { N - 1 } - \cdot + \cdot + \cdot + \cdot } , \beta _ { g _ { N - 1 } } ) , \ ( g _ { 1 , \phi _ { 0 } } , \phi _ { 2 , \phi _ { 1 } } , \delta _ { 1 0 } , \dots , \phi _ { g _ { N - 1 } - \cdot + \cdot } , \delta _ { g _ { N } } ) , } } } \\ { { { 1 5 ( g _ { 1 , \phi _ { 1 } } , \dots , \phi _ { 1 } ) } } } \\ { { { - \sum _ { s = 1 } ^ { N } ( D _ { z } \Delta ( w _ { 1 } ) \delta \phi _ { i } - D _ { \cdot } \Delta ( w _ { 1 } ) \delta \phi _ { i } + \underline { { { \delta } } } _ { 1 } ( w _ { 1 } ) \delta \phi _ { i } ) , } } } \\ { { { - \sum _ { s = 1 } ^ { N - 1 } ( D _ { z } \Delta ( w _ { 1 } ) \delta \phi _ { i } ) , \ ( D _ { z } \Delta ( w _ { 1 } ) \delta \phi _ { i + \cdot + } ) ( D _ { z } \Delta ( w _ { 1 } ) \delta \phi _ { i - \cdot + } ) ( \delta _ { i + \cdot - 1 } - l _ { k } ) ) } } } \\ { { { - \sum _ { s = 1 } ^ { N } ( D _ { z } \Delta ( w _ { 1 } ) \delta \phi _ { i + \cdot } ) \ } } } \\ { { { - \sum _ { s = 1 } ^ { N } D _ { z } \Delta ( w _ { 1 } ) \delta \phi _ { i - \cdot + \cdot } \delta _ { i + \cdot \cdot + } ) \delta \phi _ { i + \cdot + \cdot } ) , } } } \\ { { { + \sum _ { s = 1 } ^ { N } D _ { z } \Delta ( w _ { 1 } ) \delta \{ l _ { k } - l _ { k - 1 } \} , \ \delta \phi _ { k } , } } } \\  { { - \sum _ { s = 1 } ^ { N } ( D _ { z } \Delta ( w _ { 1 } ) \delta \{ l _ { k - 1 } - l _ { k } \} + \mathcal { D } _ { \cdot } \Delta ( w _ { 1 - \cdot + \cdot } ) ( \delta _ { l _ { k } } - l _ { k - 1 } ) \delta \mu _ { k } } } \\   - \sum _ { s = 1 } ^ { N - 1 } D _ { z } \Delta ( w _ { 1 } ) \delta \{ l _ { k - 1 } - l _ { k } \} + D _ { \cdot } \Delta ( w _  \end{array}
$$

where $w _ { k } = \left( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } \right) \left( k = 0 , 1 , \cdots , N - 1 \right)$ . From (3.19), we obtain the discrete Euler–Lagrange equation

$$
\begin{array} { r l } & { D _ { 2 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 5 } \mathbb { L } ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) = 0 , } \\ & { D _ { 3 } \mathbb { L } ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } ) = 0 , } \\ & { D _ { 3 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , q _ { k - 1 + \frac { 1 } { 2 } } , t _ { k } , q _ { k } ) = 0 . } \end{array}
$$

From (3.21) and (3.22), we can solve for $q _ { k + \frac 1 2 }$ and $\scriptstyle q _ { k - 1 + { \frac { 1 } { 2 } } }$ respectively, then substitute them into (3.20) and finally solve for $q _ { k + 1 }$ . Therefore, the discrete Euler– Lagrange equation $( 3 . 2 0 ) - ( 3 . 2 2 )$ determines a discrete flow

$$
\begin{array} { r l } & { \Psi : M \times M \longrightarrow M \times M , } \\ & { \Psi ( t _ { k - 1 } , q _ { k _ { 1 } } , t _ { k } , q _ { k } ) = ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) . } \end{array}
$$

From (3.19), we can define two 1-forms

$$
\begin{array} { r } { \Theta _ { \mathbb { L } } ^ { v - } ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } ) = D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k } , } \end{array}
$$

and

$$
\begin{array} { r } { \Theta _ { \mathbb { L } } ^ { v + } ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } ) = D _ { 5 } \mathbb { L } ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k + 1 } . } \end{array}
$$

Using the same method as before, we can prove that

$$
\Psi ^ { * } ( { \sf d } \Theta _ { \mathbb { L } } ^ { v + } ) = - { \sf d } \Theta _ { \mathbb { L } } ^ { v - } .
$$

From the definition of $\theta _ { \mathbb { L } } ^ { v - }$ and $\Theta _ { \mathbb { L } } ^ { v + }$ , we have

$$
\begin{array} { r } { \Theta _ { \mathbb { L } } ^ { v - } + \Theta _ { \mathbb { L } } ^ { v + } = \mathtt { d } \big ( ( t _ { k + 1 } - t _ { k } ) L \big ) - D _ { 3 } L \big ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } \big ) \mathtt { d } q _ { k + \frac { 1 } { 2 } } . } \end{array}
$$

From (3.21), we obtain $D _ { 3 } { \cal L } ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } ) = 0 .$ . Thus

$$
\begin{array} { r } { \Theta _ { \mathbb { L } } ^ { v - } + \Theta _ { \mathbb { L } } ^ { v + } = { \mathrm { d } } ( ( t _ { k + 1 } - t _ { k } ) L ) , } \end{array}
$$

which means

$$
\begin{array} { r } { \mathrm { d } \Theta _ { \mathbb { L } } ^ { v + } = - \mathrm { d } \Theta _ { \mathbb { L } } ^ { v - } . } \end{array}
$$

From (3.23) and (3.25), we arrive at

$$
\Psi ^ { \ast } ( \Omega _ { \mathbb { L } } ^ { v } ) = \Omega _ { \mathbb { L } } ^ { v } ,
$$

$\Omega _ { \mathbb { L } } ^ { v } = \mathrm { d } \theta _ { \mathbb { L } } ^ { v + }$

For the classical Lagrangian (1.57), from (3.16) and (3.18), we obtain

$$
\begin{array} { l } { \mathbb { L } \big ( t _ { k } , q _ { k } , q _ { k + \frac { 1 } { 2 } } , t _ { k + 1 } , q _ { k + 1 } \big ) } \\ { = \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } \left( \frac { 1 } { 2 } \big ( \dot { q } _ { h ^ { 2 } } ( t ) \big ) ^ { 2 } - V \big ( q _ { h ^ { 2 } } ( t ) \big ) \right) \mathrm { d } t } \\ { = \frac { 1 } { 2 } \left( \frac { 1 } { 3 } a ^ { 2 } ( t _ { k + 1 } ^ { 2 } + t _ { k } t _ { k + 1 } + t _ { k } ^ { 2 } ) + a b ( t _ { k } + t _ { K + 1 } ) + b ^ { 2 } \right) } \\ { \quad - G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) , } \end{array}
$$

where

$$
\begin{array} { l } { { a = \displaystyle \frac { 4 } { h _ { k } ^ { 2 } } \big ( q _ { k } + q _ { k + 1 } - 2 q _ { k + \frac { 1 } { 2 } } \big ) , } } \\ { { \displaystyle b = \frac { 1 } { h _ { k } ^ { 2 } } \big ( 4 ( t _ { k } + t _ { k + 1 } ) q _ { k + \frac { 1 } { 2 } } - ( 3 t _ { k } + t _ { k + 1 } ) q _ { k + 1 } - ( t _ { k } + 3 t _ { k + 1 } ) q _ { k } \big ) , } } \end{array}
$$

and

$$
G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) = \frac { 1 } { t _ { k + 1 } - t _ { k } } \int _ { t _ { k } } ^ { t _ { k + 1 } } V \bigl ( q _ { k } f _ { k } ( t ) + q _ { k + 1 } f _ { k + 1 } ( t ) + q _ { k + \frac { 1 } { 2 } } f _ { k + \frac { 1 } { 2 } } ( t ) \bigr ) \mathrm { d } t .
$$

where

$$
\begin{array} { r l } & { f _ { k } ( t ) = \left( \frac { 2 ( t - t _ { k } ) } { h _ { k } } - 1 \right) \left( \frac { t - t _ { k } } { h _ { k } } - 1 \right) , } \\ & { f _ { k + 1 } ( t ) = \left( \frac { 2 ( t _ { k + 1 } - t ) } { h _ { k } } - 1 \right) \left( \frac { t _ { k + 1 } - t } { h _ { k } } - 1 \right) , } \\ & { f _ { k + \frac { 1 } { 2 } } ( t ) = 4 \frac { t - t _ { k } } { h _ { k } } \left( 1 - \frac { t - t _ { k } } { h _ { k } } \right) . } \end{array}
$$

For the discrete Lagrangian (3.27), the discrete Euler–Lagrange equations (3.20) – (3.22) become

$$
\begin{array} { r l } & { a _ { 1 } q _ { k - 1 } + a _ { 2 } q _ { k } + a _ { 3 } q _ { k + 1 } + a _ { 4 } q _ { k - \frac { 1 } { 2 } } + a _ { 5 } q _ { k + \frac { 1 } { 2 } } - d _ { 1 } h _ { k } - d _ { 2 } h _ { k - 1 } = 0 , } \\ & { - \frac { 8 } { 3 h _ { k } ^ { 2 } } \big ( q _ { k } + q _ { k + 1 } - 2 q _ { k + \frac { 1 } { 2 } } \big ) - \frac { \partial G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } } = 0 , } \\ & { - \frac { 8 } { 3 h _ { k - 1 } ^ { 2 } } \big ( q _ { k - 1 } + q _ { k } - 2 q _ { k - 1 + \frac { 1 } { 2 } } \big ) - \frac { \partial G ( q _ { k - 1 } , q _ { k - 1 + \frac { 1 } { 2 } } , q _ { k } ) } { \partial q _ { k - 1 + \frac { 1 } { 2 } } } = 0 , } \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle { \mathrm {  ~ \psi ~ } _ { 1 } = \frac { 1 } { 3 } \frac { 1 } { h _ { k - 1 } } , \quad \boldsymbol { a } _ { 2 } = \frac { 7 } { 3 } \left( \frac { 1 } { h _ { k - 1 } } + \frac { 1 } { h _ { k } } \right) , \quad \boldsymbol { a } _ { 3 } = \frac { 1 } { 3 } \frac { 1 } { h _ { k } } , } } \\ { \displaystyle { \mathrm {  ~ \psi ~ } _ { 4 } = - \frac { 8 } { 3 } \frac { 1 } { h _ { k - 1 } } , \mathrm {  ~ \psi ~ } _ { 6 } = - \frac { 8 } { 3 } \frac { 1 } { h _ { k } } , \mathrm {  ~ \psi ~ } _ { d } } = \frac { \partial G ( \boldsymbol { q } _ { k } , \boldsymbol { q } _ { k + \frac { 1 } { 2 } } , \boldsymbol { q } _ { k + 1 } ) } { \partial q _ { k } } , \mathrm {  ~ \psi ~ } _ { d } _ { 2 } = \frac { \partial G ( \boldsymbol { q } _ { k - 1 } , \boldsymbol { q } _ { k - 1 + \frac { 1 } { 2 } } , \boldsymbol { q } _ { k } ) } { \partial q _ { k } } . } \end{array}
$$

The solution of (3.28) – (3.30) preserves the Lagrange 2-form

$$
\left( \frac { 1 } { 3 h _ { k } } - h _ { k } \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k } \partial q _ { k + 1 } } - M \right) \mathrm { d } q _ { k } \wedge \mathrm { d } q _ { k + 1 } ,
$$

where

$$
{ \cal M } = \frac { \left( \displaystyle \frac { 1 6 } { 3 h _ { k } } + h _ { k } \displaystyle \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } \partial q _ { k } } \right) \left( \displaystyle \frac { 1 6 } { 3 h _ { k } } + h _ { k } \displaystyle \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } \partial q _ { k } } \right) } { \left( \displaystyle \frac { 3 2 } { 3 h _ { k } } - h _ { k } \displaystyle \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } ^ { 2 } } \right) } .
$$

If we take the fixed time steps $h _ { k - 1 } = h _ { k } = h$ , then $( 3 . 2 8 ) - ( 3 . 3 0 )$ become

$$
\begin{array} { l } { \displaystyle \frac { q _ { k - 1 } - 8 q _ { k - \frac { 1 } { 2 } } + 1 4 q _ { k } - 8 q _ { k + \frac { 1 } { 2 } } + q _ { k + 1 } } { 3 h ^ { 2 } } - \mathbf { d } _ { 1 } h _ { k } - \mathbf { d } _ { 2 } h _ { k - 1 } = 0 , } \\ { \displaystyle - \frac { 8 } { 3 h ^ { 2 } } \big ( q _ { k } + q _ { k + 1 } - 2 q _ { k + \frac { 1 } { 2 } } \big ) - \frac { \partial G \big ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } \big ) } { \partial q _ { k + \frac { 1 } { 2 } } } = 0 , } \\ { \displaystyle - \frac { 8 } { 3 h ^ { 2 } } \big ( q _ { k - 1 } + q _ { k } - 2 q _ { k - 1 + \frac { 1 } { 2 } } \big ) - \frac { \partial G \big ( q _ { k - 1 } , q _ { k - 1 + \frac { 1 } { 2 } } , q _ { k } \big ) } { \partial q _ { k - 1 + \frac { 1 } { 2 } } } = 0 , } \end{array}
$$

which preserve

$$
\left( \frac { 1 } { 3 h } - h \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k } \partial q _ { k + 1 } } - M \right) \mathrm { d } q _ { k } \wedge \mathrm { d } q _ { k + 1 } ,
$$

where

$$
M = \frac { \left( \frac { 1 6 } { 3 h _ { k } } + h \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } \partial q _ { k } } \right) \left( \frac { 1 6 } { 3 h _ { k } } + h \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } \partial q _ { k } } \right) } { \left( \frac { 3 2 } { 3 h } - h \frac { \partial ^ { 2 } G ( q _ { k } , q _ { k + \frac { 1 } { 2 } } , q _ { k + 1 } ) } { \partial q _ { k + \frac { 1 } { 2 } } ^ { 2 } } \right) } .
$$

Suppose $q _ { k }$ is the solution of $( 3 . 2 8 ) - ( 3 . 3 0 )$ and $q ( t )$ is the solution of (3.10), then from the convergence theory of finite element methods [Cia78,Fen65] , we have

$$
\| q ( t ) - q _ { h ^ { 2 } } ( t ) \| \leq C h ^ { 3 } ,
$$

where

$$
q _ { h ^ { 2 } } ( t ) = \sum _ { k = 0 } ^ { N } q _ { k } \phi _ { k } ( t ) + \sum _ { k = 0 } ^ { N - 1 } q _ { k + \frac { 1 } { 2 } } \phi _ { k + \frac { 1 } { 2 } } ( t ) ,
$$

$h = \operatorname* { m a x } _ { k } \{ h _ { k } \}$ and $C$ is a constant independent of $h$ .

# 14.3.3 Time Steps as Variables

In the above section, the time steps $t _ { k }$ play the role of parameters. They are determined beforehand according to some requirements. In fact, we can also regard $t _ { k }$ as variables and the variation of the discrete action with respect to $t _ { k }$ yields the discrete energy conservation law. This fact was first observed by Lee[Lee82,Lee87] . The symplecticity of the resulting integrators was investigated in $\{ \dot { \mathrm { C G W } } 0 3 , \mathrm { K M O } 9 9 \}$ . These results are also applied to the discrete mechanics based on finite element methods.

We regard $t _ { k }$ as variables and calculate the variation of the discrete action (1.33) as follows:

$$
\begin{array} { r l r } {  { \mathbb { d } \mathbb { B } ( t _ { 0 } , q _ { 0 } , \cdots , t _ { N } , q _ { N } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \cdots , \delta t _ { N } , \delta q _ { N } ) } } \\ & { = \frac { \mathbf { d } } { \mathbb { d } \varepsilon } \Big | _ { \ L { \varepsilon } = \mathbb { S } } ( | t _ { 0 } + \varepsilon \delta t _ { 0 } , q _ { 0 } + \varepsilon \delta q _ { 0 } , \cdots , t _ { N } + \varepsilon \delta \delta t _ { N } , q _ { N } + \varepsilon \delta q _ { N } ) } \\ & { = \sum _ { k = 1 } ^ { N - 1 } [ D _ { 2 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 4 } \mathbb { L } ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) ] \delta q _ { k } } \\ & { + \sum _ { k = 1 } ^ { N - 1 } [ D _ { 1 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 3 } \mathbb { L } ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) + L ( w _ { k - 1 } ) - L ( w _ { k } ) ] \delta t _ { k } } \\ & { + D _ { 2 } \mathbb { L } ( w _ { 0 } ) ( t _ { 1 } - t _ { 0 } ) \delta q _ { 0 } + D _ { 4 } \mathbb { L } ( w _ { N - 1 } ) ( t _ { N } - t _ { N - 1 } ) \delta q _ { N } } \\ & { + [ D _ { 1 } L ( w _ { 0 } ) ( t _ { 1 } - t _ { 0 } ) - L ( w _ { 0 } ) ] \delta t _ { 0 } } \\ & { + [ D _ { 3 } \mathbb { L } ( w _ { N - 1 } ) ( t _ { N } - t _ { N - 1 } ) + L ( w _ { N - 1 } ) ] \delta t _ { N } , } & { ( 3 . 3 7 ) } \end{array}
$$

where $w _ { k } = \left( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } \right) ( k = 0 , 1 , \cdot \cdot \cdot , N - 1 )$ , so that we have the discrete energy evolution equation from the variation $\delta q _ { k }$

$$
D _ { 2 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 4 } \mathbb { L } ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) = 0 ,
$$

and the discrete energy evolution equation from the variation $\delta t _ { k }$

$$
D _ { 1 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 3 } L ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) + L ( w _ { k - 1 } ) - L ( w _ { k } ) = 0 ,
$$

which is a discrete version of (1.23). For a conservative $L$ , (3.39) becomes the discrete energy conservation law.

From the boundary terms in (3.37), we can define two 1-forms

$$
\begin{array} { r } { \theta _ { \mathbb { L } } ^ { - } ( w _ { k } ) = ( D _ { 1 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( w _ { k } ) ) \mathrm { d } t _ { k } + D _ { 2 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k } , } \end{array}
$$

and

$$
\begin{array} { r } { \theta _ { \mathbb { L } } ^ { + } ( w _ { k } ) = ( D _ { 3 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + \mathbb { L } ( w _ { k } ) ) \mathrm { d } t _ { k + 1 } + D _ { 4 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k + 1 } . } \end{array}
$$

These two 1-forms are the discrete version of the extended Lagrange 1-form (1.29).

Unlike the continuous case, the solution of (3.38) does not satisfy (3.39) in general. Therefore, we must solve (3.38) and (3.39) simultaneously. Using the same method in the above section, we can show that the coupled integrator

$$
\begin{array} { r l } & { D _ { 2 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 4 } \mathbb { L } ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) = 0 , } \\ & { D _ { 1 } \mathbb { L } ( w _ { k } ) ( t _ { k + 1 } - t _ { k } ) + D _ { 3 } L ( w _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) + L ( w _ { k - 1 } ) - L ( w _ { k } ) = 0 , } \end{array}
$$

preserves the extended Lagrange 2-form $\omega _ { \mathbb { L } } = \mathrm { d } \theta _ { \mathbb { L } } ^ { + }$ .

For the discrete Lagrangian (3.6), (3.42) becomes

$$
\begin{array} { l } { \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } - \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) + \frac { \partial F ( w _ { k } ) } { \partial q _ { k } } h _ { k } + \frac { \partial F ( w _ { k - 1 } ) } { \partial q _ { k } } h _ { k - 1 } = 0 , } \\ { \frac { 1 } { 2 } \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) ^ { 2 } + F ( w _ { k } ) - \frac { \partial F ( w _ { k } ) } { \partial t _ { k } } h _ { k } } \\ { = \frac { 1 } { 2 } \left( \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) ^ { 2 } + F ( w _ { k - 1 } ) + \frac { \partial F ( w _ { k - 1 } ) } { \partial t _ { k } } h _ { k - 1 } . } \end{array}
$$

For the kind of high order discrete Lagrangian, we can obtain similar formulae.

# 14.3.4 Conclusions

Recently, it has been proved [GLWW01] that the symplectic structure is preserved not only on the phase flow but also on the flow with respect to symplectic vector fields as long as certain cohomological condition is satisfied in both continuous and discrete cases. This should be able to be extended to the cases in this chapter.

# Bibliography

[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[BD01] T. J. Bridges and G. Derks: The symplectic evans matrix, and the instability of solitary waves and fonts. Arch. Rat. Mech. Anal, 156:1–87, (2001).   
[Bri97] T. J. Bridges: Multi-symplectic structures and wave propagation. Math. Proc. Cam. Phil. Soc., 121:147–190, (1997).   
[CGW03] J. B. Chen, H.Y. Guo, and K. Wu: Total variation in Hamiltonian formalism and symplectic-energy integrators. J. of Math. Phys., 44:1688–1702, (2003).   
[CH53] R. Courant and D. Hilbert: Methods of Mathematical Physics. Interscience, New York, Second edition, (1953).   
[Cia78] D. G. Ciarlet: The Finite Element for Elliptic Problem. North-Holland, Amsterdam, First edition, (1978).   
[Fen65] K. Feng: Difference schemes based on variational principle. J. of appl. and comput. math.in chinese, 2(4):238–262, (1965).   
[Fen86] K. Feng: Difference schemes for Hamiltonian formalism and symplectic geometry. J. Comput. Math., 4:279–289, (1986).   
[FWQW89] K. Feng, H. M. Wu, M.Z. Qin, and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[GLW01a] H. Y. Guo, Y. Q. Li, and K. Wu: A note on symplectic algorithms. Commun.Theor. Phys., 36:11–18, (2001).   
[GLW01b] H. Y. Guo, Y. Q. Li, and K. Wu: On symplectic and multisymplectic structures and their discrete version in Lagrange formalism. Commun.Theor. Phys., 35:703–710, (2001).   
[GLWW01] H. Y. Guo, Y. Q. Li, K. Wu, and S. K. Wang: Difference discrete variational principle, Euler-Lagrange cohomology and symplectic, multisymplectic structures. arXiv: math-ph/0106001, (2001).   
[GM88] Z. Ge and J. E. Marsden: Lie–Poisson–Hamilton–Jacobi theory and Lie–Poisson integrators. Physics Letters A, pages 134–139, (1988).   
[GPS02] H. Goldstein, C. Pole, and J. Safko: Classical Mechanics. Addison Wesley, New York, Third edition, (2002).   
[GW03] H. Y. Guo and K. Wu: On variations in discrete mechanics and field theory. J. of Math. Phys., 44:5978–6044, (2003).   
[KMO99] C. Kane, J. E. Marsden, and M. Ortiz: Symplectic-energy-momentum preserving variational integrators. J. of Math. Phys., 40:3353–3371, (1999).   
[Lag88] J. L. Lagrange: Mecanique Analytique ´ , 2 vols. Gauthier-Villars et fils, Paris, 4-th edition, 1888-89, (1781)   
[Lee82] T. D. Lee: Can time be a discrete dynamical variable? Phys.Lett.B, 122:217–220, (1982).   
[Lee87] T. D. Lee: Difference equations and conservation laws. J. Stat. Phys., 46:843–860, (1987).   
[MPS98] J. E. Marsden, G.P. Patrick, and S. Shloller: Multi-symplectic geometry, variational integrators, and nonlinear PDEs. Communications in Mathematical Physics, 199:351–395, (1998).   
[MV91] J. Moser and A. P. Veselov: Discrete versions of some classical integrable systems and factorization of matrix polynomials. Communications in Mathematical Physics, 139:217– 243, (1991).   
[Olv93] P. J. Olver: Applications of Lie Groups to Differential Equations. GTM 107. Springer-Verlag, Berlin, Second edition, (1993).   
[SSC94] J. M. Sanz-Serna and M. P. Calvo: Numerical Hamiltonian Problems. AMMC 7. Chapman & Hall, London, (1994).   
[Ves88] A. P. Veselov: Integrable discrete-time systems and difference operators. Funkts. Anal. Prilozhen, 22:1–33, (1988).   
[Ves91a] A. P. Veselov: Integrable Lagrangian correspondences and the factorization of matrix polynomials. Funkts. Anal. Prilozhen, 25:38–49, (1991).   
[Ves91b] A. P. Veselov: Integrable maps. Russian Math. Surveys, 46:1–51, (1991).   
[WM97] J. Wendlandt and J. Marsden: Mechanical integrators derived from a discrete variational principle. Physica D, 106:223–246, (1997).
