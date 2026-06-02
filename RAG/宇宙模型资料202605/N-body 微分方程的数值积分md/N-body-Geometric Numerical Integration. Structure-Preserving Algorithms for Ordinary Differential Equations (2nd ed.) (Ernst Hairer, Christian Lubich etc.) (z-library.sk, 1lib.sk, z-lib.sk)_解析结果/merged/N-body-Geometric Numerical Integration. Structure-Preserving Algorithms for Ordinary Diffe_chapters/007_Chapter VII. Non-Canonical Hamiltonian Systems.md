# Chapter VII. Non-Canonical Hamiltonian Systems

Wediscuss theoretical properties and the structure-preserving numerical treatment ofHamiltonian systems on manifoldsand ofthe closelyrelated classof Poisson systems.We present numerical integrators for problems from classical and quantum mechanics.

# VII.1 Constrained Mechanical Systems

Constrained mechanical systems form an important class of differential equations onmanifolds.Their numerical treatment has been extensively investigated in the context of differential-algebraic equationsandisdocumented inmonographslike thatofBrenan,Campbell&Petzold（1996),Eich-Soellner&Fuhrer（1998),Hairer, Lubich&Roche（1989),andChap.VIIofHairer&Wanner（1996).Weconcentrate hereon thesymmetryand/or symplecticity of such numerical integrators.

# VII.1.1 Introduction and Examples

Considera mechanical system described by position coordinates $q _ { 1 } , \ldots , q _ { d }$ ,and suppose that the motion is constrained to satisfy $g ( q ) = 0$ where $g : \mathbb { R } ^ { d }  \mathbb { R } ^ { m }$ with $m < d$ Let $T ( q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { T } M ( q ) \dot { q }$ betheetic $U ( q )$ its potential energy,and put

$$
L ( q , \dot { q } ) = T ( q , \dot { q } ) - U ( q ) - g ( q ) ^ { T } \lambda ,
$$

where $\lambda = ( \lambda _ { 1 } , \ldots , \lambda _ { m } ) ^ { T }$ consists of Lagrange multipliers.The Euler-Lagrange equation of the variational problem for $\textstyle \int _ { 0 } ^ { t } L ( q , { \dot { q } } ) d t$ is then given by

$$
\frac { d } { d t } \Bigl ( \frac { \partial L } { \partial \dot { q } } \Bigr ) - \frac { \partial L } { \partial q } = 0 .
$$

Writenasafirst order differential equation weget

$$
\begin{array} { c } { { \dot { q } ~ = ~ v } } \\ { { M ( q ) \dot { v } ~ = ~ f ( q , v ) - G ( q ) ^ { T } { \lambda } } } \\ { { 0 ~ = ~ g ( q ) , } } \end{array}
$$

where $\begin{array} { r } { \boldsymbol { f } ( \boldsymbol { q } , \boldsymbol { v } ) = - \frac { \partial } { \partial \boldsymbol { q } } \big ( M ( \boldsymbol { q } ) \boldsymbol { v } \big ) \boldsymbol { v } + \nabla _ { \boldsymbol { q } } T ( \boldsymbol { q } , \boldsymbol { v } ) - \nabla _ { \boldsymbol { q } } U ( \boldsymbol { q } ) } \end{array}$ and $\begin{array} { r } { G ( q ) = \frac { \partial g } { \partial q } ( q ) . } \end{array}$

Example1.1 (Spherical Pendulum).We denote by $q _ { 1 } , q _ { 2 } , q _ { 3 }$ the Cartesian coordinates of apoint with mass $m$ thatis connected with a massless rod of length $\ell$ tothe origin.The kinetic and potential energies are $\begin{array} { r } { T = \frac { m } { 2 } ( \dot { q } _ { 1 } ^ { 2 } + \dot { q } _ { 2 } ^ { 2 } + \dot { q } _ { 3 } ^ { 2 } ) } \end{array}$ and $U = m g q _ { 3 }$ ,respectively,and the constraint is the fixed length of therod.Wethus get the system

$$
\begin{array} { c c l } { { \dot { q } _ { 1 } ~ = ~ v _ { 1 } } } & { { m \dot { v } _ { 1 } ~ = ~ - 2 q _ { 1 } \lambda } } & { { } } \\ { { \dot { q } _ { 2 } ~ = ~ v _ { 2 } } } & { { m \dot { v } _ { 2 } ~ = ~ - 2 q _ { 2 } \lambda } } & { { } } \\ { { \dot { q } _ { 3 } ~ = ~ v _ { 3 } } } & { { m \dot { v } _ { 3 } ~ = ~ - m g - 2 q _ { 3 } \lambda } } & { { } } \\ { { 0 ~ \equiv ~ q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } - \ell ^ { 2 } . } } & { { } } \end{array}
$$

Thephysical meaning of $\lambda$ is the tension in the rod which maintains the constant distance of the mass point from the origin.

Existence and Uniqueness of the Solution.A standard approach for studying theexistence of solutions of differential-algebraic equations is to differentiate the constraintsuntil an ordinary differential equationisobtained.Differentiating the constraint in(1.2) twicewith respect to time yields

$$
0 = G ( q ) { \boldsymbol v } \qquad { \mathrm { a n d } } \qquad 0 = g ^ { \prime \prime } ( q ) ( { \boldsymbol v } , { \boldsymbol v } ) + G ( q ) { \dot { \boldsymbol v } } ,
$$

The equation for $\dot { v }$ in（1.2）together with the second relation of(1.4） constitute a linear system for $\dot { v }$ and $\lambda$ ,

$$
\binom { M ( q ) } { G ( q ) } \begin{array} { c } { { G ( q ) ^ { T } } } \\ { { 0 } } \end{array} \biggr ) \binom { \dot { v } } { \lambda } = \biggl ( \begin{array} { c } { { f ( q , v ) } } \\ { { - g ^ { \prime \prime } ( q ) ( v , v ) } } \end{array} \biggr ) .
$$

Throughout this chapter we require the matrix appearing in（1.5)tobe invertible for $q$ closeto the solution we arelooking for. This then allowsus to express $\dot { v }$ and $\lambda$ as functions.of $( q , v )$ Notice that thematrixin(1.5）is invertiblewhen $G ( q )$ has full rank and $M ( q )$ isinvertibleon $\ker G ( q ) = \{ h \mid G ( q ) h = 0 \}$

Weare now able to discuss the existence of a solution of(1.2).First of all, observe that the initial values $q _ { 0 } , v _ { 0 } , \lambda _ { 0 }$ cannotbe arbitrarily chosen.They haveto satisfy the first relation of(1.4）and $\lambda _ { 0 } = \lambda ( q _ { 0 } , v _ { 0 } )$ ,where $\lambda ( q , v )$ isobtained from (1.5).In the case that $q _ { 0 } , v _ { 0 } , \lambda _ { 0 }$ satisfy these conditions,we call them consistent initial values.Furthermore,every solution of(1.2) has to satisfy

$$
\dot { q } = v , \qquad \dot { v } = \dot { v } ( q , v ) ,
$$

where $\dot { v } ( q , v )$ isthe function obtained from(1.5).Itisknown from standard theory ofordinary differential equations that(1.6) has locallyaunique solution.This solution $( q ( t ) , v ( t ) )$ togetherwith $\lambda ( t ) : = \lambda ( q ( t ) , v ( t ) )$ satisfies(1.5) by construction, and hence also the two differential equations of(1.2).Integrating the second relation of(1.4)twice and using the fact that the integration constants vanish for consistent initialvalues,proves also the remaining relation $0 = g ( q )$ for this solution.

Formulationasa Differential Equationona Manifold.Wedenote by

$$
\mathcal { Q } = \{ q ; g ( q ) = 0 \}
$$

the configuration manifold,on which the positions $q$ are constrained to lie.The tangent space at $q \in \mathcal { Q }$ is $T _ { q } \mathcal { Q } = \{ v$ ; $G ( q ) v = 0 \}$ .Theequations (1.6) define thus adifferential equation on the manifold

$$
T \mathcal { Q } = \{ ( q , v ) ; q \in \mathcal { Q } , v \in T _ { q } \mathcal { Q } \} = \{ ( q , v ) ; g ( q ) = 0 , G ( q ) v = 0 \} ,
$$

the tangent bundleof $\mathcal { Q }$ .Indeed,wehavejustshownthatforinitial values $( q _ { 0 } , v _ { 0 } ) \in$ $\begin{array} { r } { T \mathcal { Q } } \end{array}$ (i.e.,consistent initial values)the problems(1.6)and(1.2)are equivalent,so that the solutions of(1.6） stay on $T \mathcal { Q }$ ,

Reversibility. The system (1.2）and the corresponding differential equation (1.6) arereversible with respect to the involution $\rho ( q , v ) ~ = ~ ( q , - v )$ ,if $f ( q , - v ) ~ =$ $f ( q , v )$ This followsat once from ExampleV.1.3,because the solution $\dot { v } ( q , v )$ of （1.5）satisfies $\dot { v } ( q , - v ) = \dot { v } ( q , v )$

Forthe numerical solution of differential-algebraic equations“index reduction” isavery popular technique.Thismeans that instead ofdirectly treating the problem（1.2）one numerically solves thedifferential equation（1.6）on themanifold $\mathcal { M }$ Projectionmethods(Sect.IV.4）aswellasmethodsbased on local coordinates (Sect.IV.5）aremuch in use.If oneis interested ina correct simulation of thereversible structureofthe problem,thesymmetric methods of Sect.V.4canbe applied.Here we do not repeat these approaches for thisparticular situation,instead weconcentrate on the symplectic integration of constrained systems.

# VII.1.2 Hamiltonian Formulation

InSect.VI.1 we have seen that,for unconstrained mechanical systems,the equationsof motion become more structured if we use the momentum coordinates $\begin{array} { r } { p = \frac { \partial L } { \partial \dot { q } } = M ( q ) \dot { q } } \end{array}$ in placeof the velocity coordinates $v = q$ Let us do the same forthe constrained system(1.2).As in theproof of Theorem VI.1.3we obtain the equivalent system

$$
\begin{array} { l l l } { \dot { q } } & { = } & { H _ { p } ( p , q ) } \\ { \dot { p } } & { = } & { - H _ { q } ( p , q ) - G ( q ) ^ { T } \lambda } \\ { 0 } & { = } & { g ( q ) , } \end{array}
$$

where

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q )
$$

is the total energy of the system; $H _ { p }$ and $H _ { q }$ denote the column vectors of partial derivatives.Differentiating theconstraint in(1.9) twice with respect to time,we get

$$
\begin{array} { l } { { 0 \nonumber = G ( q ) H _ { p } ( p , q ) , } } \\ { { 0 \nonumber = \displaystyle { \frac { \partial } { \partial q } \Bigl ( G ( q ) H _ { p } ( p , q ) \Bigr ) H _ { p } ( p , q ) - G ( q ) H _ { p p } ( p , q ) \Bigl ( H _ { g } ( p , q ) + G ( q ) ^ { T } \lambda \Bigr ) } , } } \end{array}
$$

and assuming the matrix

$$
G ( q ) H _ { p p } ( p , q ) G ( q ) ^ { T } \qquad \mathrm { i s ~ i n v e r t i b l e } ,
$$

equation(1.12)permits us to express $\lambda$ in terms of $( p , q )$

Formulation asa Differential Equation onaManifold. Inserting the so-obtained function $\lambda ( p , q )$ into(1.9） givesa differential equation for $( p , q )$ on the manifold

$$
\mathcal { M } = \{ ( p , q ) ; g ( q ) = 0 , G ( q ) H _ { p } ( p , q ) = 0 \} .
$$

Aswewill now see,thismanifold hasa differential-geometric interpretation as thecotangent bundle of the configuration manifold $\mathcal { Q } \ = \ \{ q : g ( q ) \ = \ 0 \}$ The Lagrangian fora fixed $q \in \mathcal { Q }$ isa function on the tangent space $T _ { q } \mathcal { Q }$ ,i.e., $L ( q , \cdot ) : T _ { q } \mathcal { Q } \to \mathbb { R }$ Its(Frechet) derivative evaluated at $\dot { q } \in \mathcal { I } _ { q } \mathcal { Q }$ istherefore a linearmapping $d _ { \dot { q } } L ( q , \dot { q } ) : T _ { q } \mathcal { Q } \to \mathbb { R }$ ,orin other terms, $d _ { \dot { q } } L ( q , \dot { q } )$ is in the cotangent space $T _ { q } ^ { * } \mathcal { Q }$ Sincethedualityissuch that $\begin{array} { r } { \langle d _ { \dot { q } } L ( q , \dot { q } ) , v \rangle = \frac { \partial L } { \partial \dot { q } } ( q , \dot { q } ) v } \end{array}$ for $v \in \mathcal { I } _ { q } \mathcal { Q }$ condition (1.13) ensures that the Legendre transform $\dot { q } \mapsto p = d _ { \dot { q } } L ( q , \dot { q } )$ isan invertible transformation between $T _ { q } \mathcal { Q }$ and $T _ { q } ^ { * } \mathcal { Q }$ .Wecan therefore consider $T _ { q } ^ { \scriptscriptstyle * } \mathcal { Q }$ as a subspace of $\mathbb { R } ^ { d }$ if every $p \in T _ { q } ^ { * } \mathcal { Q }$ is identified with $\begin{array} { r } { \frac { \partial L } { \partial \dot { q } } ( q , \dot { q } ) ^ { T } = M ( q ) \dot { q } \in \mathbb { R } ^ { d } } \end{array}$ for the unique $\dot { q } \in T _ { q } \mathcal { Q }$ forwhich $p = d _ { \dot { q } } L ( q , \dot { q } )$ holds.With this identification,

$$
T _ { q } ^ { * } \mathcal { Q } = \{ M ( q ) \dot { q } ; \dot { q } \in T _ { q } \mathcal { Q } \} ,
$$

and the duality is given by $\langle p , v \rangle = p ^ { T } v$ for $p \in \mathcal { I } _ { q } ^ { \ast \mathcal { Q } }$ and $v \in \mathcal { I } _ { q } \mathcal { Q }$ We thus have $p = M ( q ) \dot { q } \in T _ { q } ^ { * } \mathcal { Q }$ ifand only if $\dot { q } = M ( q ) ^ { - 1 } p = H _ { p } ( p , q ) \in T _ { q } \mathcal { Q }$ Since the tangent space at $q \in \mathcal { Q }$ is $T _ { q } \mathcal { Q } = \{ \dot { q } ; G ( q ) \dot { q } = 0 \}$ ,weobtain that

$$
p \in T _ { q } ^ { * } \mathcal { Q } \qquad \mathrm { i f ~ a n d ~ o n l y ~ i f } \qquad G ( q ) H _ { p } ( p , q ) = 0 .
$$

Denoting by $T ^ { \ast } \mathcal { Q } = \{ ( p , q ) ; q \in \mathcal { Q } , p \in T _ { q } ^ { \ast } \mathcal { Q } \}$ the cotangent bundle of $\mathcal { Q }$ ,we thus see that the constraint manifold $\mathcal { M }$ of（1.14）equals

$$
\mathcal { M } \equiv T ^ { \ast } \mathcal { Q } .
$$

Theconstrained Hamiltonian system(1.9）with Hamiltonian(1.1O) can thus be viewed asadifferential equation on the cotangent bundle $\tau ^ { * } \mathcal { Q }$ of the configurationmanifold $\mathcal { Q }$

Inthe followingwe consider the system (1.9)-(1.12)with(1.13) where $H ( p , q )$ isanarbitrary smooth function.Theconstraint manifoldis then still given by(1.14). The existence and uniqueness of the solution of(1.9)can be discussed as before.

Reversibility.Itisreadilychecked that thesystem(1.9) is reversible if $H ( - p , q ) =$ $H ( p , q ) .$ This is always satisfied fora Hamiltonian(1.10).

Preservationof the Hamiltonian.Differentiation of $H ( p ( t ) , q ( t ) )$ with respect to timeyields

$$
- H _ { p } ^ { T } H _ { q } - H _ { p } ^ { T } G ^ { T } \lambda + H _ { q } ^ { T } H _ { p }
$$

with all expressions evaluated at $( p ( t ) , q ( t ) )$ The first and the last terms cancel, and the central term vanishes because $G H _ { p } = 0$ on the solution manifold. Consequently,the Hamiltonian $H ( p , q )$ is constant along solutions of (1.9).

Symplecticity of theFlow.Since the flow of the system(1.9)is a transformation on $\mathcal { M }$ ,itsderivative isa mapping between the corresponding tangent spaces.In agreement with DefinitionVI.2.2we call amap $\varphi : \mathcal { M }  \mathcal { M }$ symplectic if,for every $x = ( p , q ) \in M$ ,

$$
\begin{array} { r } { \xi _ { 1 } ^ { T } \varphi ^ { \prime } ( x ) ^ { T } J \varphi ^ { \prime } ( x ) \xi _ { 2 } = \xi _ { 1 } ^ { T } J \xi _ { 2 } \qquad \mathrm { ~ f o r ~ a l l ~ } \xi _ { 1 } , \xi _ { 2 } \in T _ { x } \mathcal { M } . } \end{array}
$$

If $\varphi$ isactually defined and continuouslydifferentiablein an open subset of $\mathbb { R } ^ { 2 d }$ that contains $\mathcal { M }$ ,then $\varphi ^ { \prime } ( x )$ intheabove formula is just theusual Jacobian matrix. Otherwise,some care is necessaryin the interpretation of(1.16): $\varphi ^ { \prime }$ is the tangent mapgiven by the directional derivative $\varphi ^ { \prime } ( x ) \xi : = ( d / d \tau ) | _ { \tau = 0 } \varphi ( \gamma ( \tau ) )$ for $\xi \in \mathbf { \Xi }$ $T _ { x } { \mathcal { M } }$ where $\gamma$ is a path on $\mathcal { M }$ with $\gamma ( 0 ) = x$ ， ${ \dot { \gamma } } ( 0 ) = \xi .$ Theexpression $\xi _ { 1 } ^ { T } \varphi ^ { \prime } ( x ) ^ { T }$ in(1.16)should then be interpreted as $( \varphi ^ { \prime } ( x ) \xi _ { 1 } ) ^ { T }$

Theorem 1.2.Let $H ( p , q )$ and $g ( q )$ betwicecontinuously differentiable.Theflow $\varphi _ { t } : \mathcal { M }  \mathcal { M }$ ofthesystem(1.9)isthena symplectic transformationon $\mathcal { M }$ i.e.,it satisfies(1.16).

ProofWe let $x = ( p , q )$ ,so that thesystem(1.9) becomes $\dot { x } = J ^ { - 1 } ( \nabla H ( x ) +$ $\begin{array} { r } { \sum _ { i } \lambda _ { i } ( x ) \nabla g _ { i } ( x ) \big ) , } \end{array}$ where $\lambda _ { i } ( x )$ and $g _ { i } ( x )$ are the components of $\lambda ( x )$ and $g ( x )$ , and $\lambda ( x )$ isthe function obtained from(1.12).The variational equation of this system,satisfied by thedirectional derivative $\varPsi = \varphi _ { t } ^ { \prime } ( x _ { 0 } ) \xi$ ,with $x _ { 0 } = ( p _ { 0 } , q _ { 0 } )$ ,reads

$$
\dot { \psi } = J ^ { - 1 } \Big ( \nabla ^ { 2 } H ( x ) + \sum _ { i = 1 } ^ { m } \lambda _ { i } ( x ) \nabla ^ { 2 } g _ { i } ( x ) + \sum _ { i = 1 } ^ { m } \nabla g _ { i } ( x ) \nabla \lambda _ { i } ( x ) ^ { T } \Big ) \varPsi .
$$

Adirect computation,analogous tothat in theproof of Theorem VI.2.4,yields for $\xi _ { 1 } , \xi _ { 2 } \in T _ { x } { \mathcal { M } }$

$$
\begin{array} { r } { \frac { d } { \vert t \vert } \bigg ( \xi _ { 1 } ^ { T } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) ^ { T } \mathcal { J } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) \xi _ { 2 } \bigg ) = \dots = \sum _ { i = 1 } ^ { m } \xi _ { 1 } ^ { T } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) ^ { T } \nabla g _ { i } ( x ) \nabla \lambda _ { i } ( x ) ^ { T } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) } \\ { - \displaystyle \sum _ { i = 1 } ^ { m } \xi _ { 1 } ^ { T } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) ^ { T } \nabla \lambda _ { i } ( x ) \nabla g _ { i } ( x ) ^ { T } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) \xi _ { 2 } . ~ ( 1 ; \lambda _ { i } ) } \end{array}
$$

Since $g _ { i } \big ( \varphi _ { t } ( x _ { 0 } ) \big ) = 0$ for $x _ { 0 } \in \mathcal { M }$ ,we have $\nabla g _ { i } ( x ) ^ { T } \varphi _ { t } ^ { \prime } ( x _ { 0 } ) \xi _ { 2 } = 0$ and the same for $\xi _ { 1 }$ ,sothat the expression in（1.17)vanishes.This proves the symplecticity of the flowon $\mathcal { M }$ □

Differentiating the constraint in（1.9） twiceand solving for theLagrangemultiplier from(1.12）(thisprocedureisknownas“index reduction”of thedifferentialalgebraicsystem)yieldsthe differential equation

$$
\dot { \boldsymbol { q } } = \boldsymbol { H _ { p } } ( \boldsymbol { p } , \boldsymbol { q } ) , \qquad \dot { \boldsymbol { p } } = - \boldsymbol { H _ { q } } ( \boldsymbol { p } , \boldsymbol { q } ) - \boldsymbol { G } ( \boldsymbol { q } ) ^ { T } \boldsymbol { \lambda } ( \boldsymbol { p } , \boldsymbol { q } ) ,
$$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0004_pages_0211-0280/auto/images/985831e4bb6fdf974c378ef5e565e304f1dac6f04b6b98cb46095947665d0ed0.jpg)  
Fig.1.1.Numerical solutionof thesymplecticEulermethodappliedto(1.18)with $H ( p , q ) =$ $\textstyle { \frac { 1 } { 2 } } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } + p _ { 3 } ^ { 2 } ) + q _ { 3 }$ ， $g ( q ) = q _ { 1 } ^ { 2 } + \hat { q } _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } - 1$ (spherical pendulum)；initial value $q _ { \complement } =$ $( 0 , \sin ( 0 . 1 ) , - \cos ( 0 . 1 ) )$ ， $p _ { 0 } = ( 0 . 0 6 , 0 , 0 )$ stepsize $h = 0 . 0 0 3$ for method"sE”(without projection）and $h = 0 . 0 3$ for method"sEproj"(with projection）

where $\lambda ( p , q )$ is obtained from(1.12).If we solve this systemwith the symplectic Eulermethod （implicit in $p$ explicitin $q$ ),thequalitativebehaviour of the numerical solutionisnot correct.Aswas observed by Leimkuhler&Reich(1994),there isalinear error growth in the Hamiltonianand alsoa drift from the manifold $\mathcal { M }$ (method“sE”in Fig.1.1).The explanation for thisbehaviouris the fact that(1.18) isno longera Hamiltonian system.If we combine the symplectic Euler applied to（1.18）with an orthogonal projection onto $\mathcal { M }$ （method“sEproj"）,the resultimproves considerably but the linear error growth in the Hamiltonian is not eliminated. Thisnumerical experiment illustrates that"index reduction”is not compatible with symplectic integration.

# VII.1.3A Symplectic First Order Method

Weextend the symplectic Euler method to Hamiltonian systems with constraints. We integrate the $p$ -variablebytheimplicitandthe $q$ -variablebytheexplicitEuler method.This gives

$$
\begin{array} { r l } & { \widehat { p } _ { n + 1 } \ = \ p _ { n } - h \left( H _ { q } ( \widehat { p } _ { n + 1 } , q _ { n } ) + G ( q _ { n } ) ^ { T } \lambda _ { n + 1 } \right) } \\ & { q _ { n + 1 } \ = \ q _ { n } + \ h H _ { p } ( \widehat { p } _ { n + 1 } , q _ { n } ) } \\ & { \qquad 0 \ = \ g ( q _ { n + 1 } ) . } \end{array}
$$

The numerical approximation $( \widehat { p } _ { n + 1 } , q _ { n + 1 } )$ satisfies the constraint $g ( q ) = 0$ ,but not $G ( q ) H _ { p } ( p , q ) = 0 .$ Toget an approximation $( p _ { n + 1 } , q _ { n + 1 } ) \in \mathcal { M }$ ,weappend the projection

$$
\begin{array} { r } { p _ { n + 1 } \ = \ \widehat { p } _ { n + 1 } - h G ( q _ { n + 1 } ) ^ { T } \mu _ { n + 1 } } \\ { 0 \ = \ G ( q _ { n + 1 } ) H _ { p } ( p _ { n + 1 } , q _ { n + 1 } ) . } \end{array}
$$

Let us discuss some basic properties of this method.

Existence and Uniqueness of the Numerical Solution.Inserting the definition of $q _ { n + 1 }$ from the second line of(1.19) into $0 = g ( q _ { n + 1 } )$ givesanonlinearsystem for $\widehat { p } _ { n + 1 }$ and $h \lambda _ { n + 1 }$ Due to the factor $h$ in front of $H _ { p } ( \widehat { p } _ { n + 1 } , q _ { n } )$ ,theimplicit function theorem cannot be directly applied to prove existence and uniqueness of thenumerical solution.We therefore write this equation as

$$
0 = g ( q _ { n + 1 } ) = g ( q _ { n } ) + \int _ { 0 } ^ { 1 } G \big ( q _ { n } + \tau ( q _ { n + 1 } - q _ { n } ) \big ) ( q _ { n + 1 } - q _ { n } ) d \tau .
$$

Wenowuse $g ( q _ { n } ) ~ = ~ 0$ ,insert the definition of $q _ { n + 1 }$ from the second line of (1.19)and divide by $h$ Togetherwith the first lineof(1.19)thisyields the system $F ( { \widehat { p } } _ { n + 1 } , h \lambda _ { n + 1 } , h ) = 0$ with

$$
F ( p , \nu , h ) = \left( \begin{array} { c } { { p - p _ { n } + h H _ { q } ( p , q _ { n } ) + G ( q _ { n } ) ^ { T } \nu } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } G \big ( q _ { n } + \tau h H _ { p } ( p , q _ { n } ) \big ) H _ { p } ( p , q _ { n } ) d \tau \ \qquad } } \end{array} \right) .
$$

Since $( p _ { n } , q _ { n } ) \in \mathcal { M }$ with $\mathcal { M }$ from (1.14),we have $F ( p _ { n } , 0 , 0 ) = 0 .$ Furthermore,

$$
\frac { \partial F } { \partial ( p , \nu ) } ( p _ { n } , 0 , 0 ) = \left( \begin{array} { c c } { { I } } & { { G ( q _ { n } ) ^ { T } } } \\ { { G ( q _ { n } ) H _ { p p } ( p _ { n } , q _ { n } ) } } & { { 0 } } \end{array} \right) ,
$$

and thismatrixisinvertible by(1.13).Consequently,anapplicationof theimplicit function theorem proves that the numerical solution $\left( \widehat { p } _ { n + 1 } , h \lambda _ { n + 1 } \right)$ (and hence also $q _ { n + 1 } )$ existsand is locally unique forsufficiently small $h$ ,

The projection step(1.20)constitutes anonlinear system for $p _ { n + 1 }$ and $h \mu _ { n + 1 }$ to which the implicit function theorem can be directly applied.

Convergence of Order1.The aboveuse of theimplicit function theoremyields the rough estimates

$$
\widehat { p } _ { n + 1 } = p _ { n } + \mathcal { O } ( h ) , \quad h \lambda _ { n + 1 } = \mathcal { O } ( h ) , \quad h \mu _ { n + 1 } = \mathcal { O } ( h ) ,
$$

which,together with the equations (1.19) and(1.20),give

$$
q _ { n + 1 } = q ( t _ { n + 1 } ) + \mathcal { O } ( h ^ { 2 } ) , \quad p _ { n + 1 } = p ( t _ { n + 1 } ) - G \big ( q ( t _ { n + 1 } ) \big ) ^ { T } \nu + \mathcal { O } ( h ^ { 2 } ) ,
$$

where $( p ( t ) , q ( t ) )$ is the solution of(1.9) passing through $( p _ { n } , q _ { n } ) \in \mathcal { M }$ at $t = t _ { n }$ . Inserting these relations into the second equation of(1.2O) we get

$$
0 = G \big ( q ( t ) \big ) H _ { p } \big ( p ( t ) , q ( t ) \big ) + G \big ( q ( t ) \big ) H _ { p p } \big ( p ( t ) , q ( t ) \big ) G \big ( q ( t ) \big ) ^ { T } \nu + \mathcal { O } ( h ^ { 2 } )
$$

at $t = t _ { n + 1 }$ .Since $G \big ( q ( t ) \big ) H _ { p } \big ( p ( t ) , q ( t ) \big ) = 0 ,$ it followsfrom(1.13) that $\nu =$ $O ( h ^ { 2 } ) .$ The local error is therefore of size $\mathcal { O } ( h ^ { 2 } )$ .

Theconvergence proof now follows standard arguments,because the methodis amapping $\phi _ { h } : { \mathcal { M } } \to { \mathcal { M } }$ onthe solution manifold.We consider the solutions $( p _ { n } ( t ) , q _ { n } ( t ) )$ of（1.9)passing through the numerical values $( p _ { n } , q _ { n } ) \in \mathcal { M }$ at $t =$ $t _ { n }$ ,we estimate the difference of two successive solutions in terms of the local error at $t _ { n }$ ,andwe sum up the propagated errors (see Fig.3.2 of Sect.II.3 in Hairer, Nprsett&Wanner（1993)）.This proves that theglobal error satisfies $p _ { n } - p ( t _ { n } ) =$ $\mathcal { O } ( h )$ and $q _ { n } - q ( t _ { n } ) = \mathcal { O } ( h )$ aslongas $t _ { n } = n h \leq C o n s t$ .

Symplecticity.We first study the mapping $( p _ { n } , q _ { n } ) \mapsto ( { \widehat { p } } _ { n + 1 } , q _ { n + 1 } )$ defined by (1.19),and we consider $\lambda _ { n + 1 }$ asa function $\lambda ( p _ { n } , q _ { n } )$ Differentiation with respect to $( p _ { n } , q _ { n } )$ yields

$$
\binom { I + h H _ { q p } ^ { T } } { - h H _ { p p } }  \begin{array} { c } { 0 } \\ { ( \frac { \partial ( \widehat { p } _ { n + 1 } , q _ { n + 1 } ) } { \partial ( p _ { n } , q _ { n } ) } ) = ( \begin{array} { c c } { I - h G ^ { T } \lambda _ { p } } & { S - h G ^ { T } \lambda _ { q } } \\ { 0 } & { I + h H _ { q p } } \end{array} ) , } \end{array}
$$

where $S = - h H _ { q q } - h \lambda ^ { \varPsi } g _ { q q }$ is a symmetric matrix,theexpressions $H _ { q p }$ , $H _ { p p }$ , $H _ { q q } , G$ are evaluated at $( \widehat { p } _ { n + 1 } , q _ { n } )$ ,and $\lambda$ , $\lambda _ { p }$ , $\lambda _ { q }$ at $( p _ { n } , q _ { n } )$ Acomputation,identical tothatof theproof ofTheoremVI.3.3,yields

$$
\begin{array} { r } { \underbrace { ^ { \prime } \partial ( \widehat { p } _ { n + 1 } , q _ { n + 1 } ) } _ { \partial ( p _ { n } , q _ { n } ) } \Big ) ^ { T } J \left( \frac { \partial ( \widehat { p } _ { n + 1 } , q _ { n + 1 } ) } { \partial ( p _ { n } , q _ { n } ) } \right) = \left( \begin{array} { c c } { 0 } & { I - h \lambda _ { p } ^ { T } G } \\ { - I + h G ^ { T } \lambda _ { p } } & { h ( G ^ { T } \lambda _ { q } - \lambda _ { q } ^ { T } G ) } \end{array} \right) } \end{array}
$$

We multiply thisrelation fromthe left by $\xi _ { 1 } \in \mathcal { T } _ { ( p _ { n } , q _ { n } ) } \mathcal { M }$ and from the right by $\xi _ { 2 } \in \mathsf { \Delta } I _ { ( p _ { n } , q _ { n } ) } \mathcal { M } .$ With the partitioning $\xi = ( \xi _ { p } , \xi _ { q } )$ wehave $G ( q _ { n } ) \xi _ { q , j } = 0$ for $j = 1 , 2$ so that the expression reduces to $\xi _ { 1 } ^ { I } \cdot J \xi _ { 2 }$ Thisproves the symplecticity condition（1.16)forthemapping $( p _ { n } , q _ { n } ) \mapsto ( { \widehat { p } } _ { n + 1 } , q _ { n + 1 } )$

Similarly,theprojectionstep $( \widehat { p } _ { n + 1 } , q _ { n + 1 } ) \mapsto ( p _ { n + 1 } , q _ { n + 1 } )$ of(1.20) gives

$$
\frac { \partial ( p _ { n + 1 } , q _ { n + 1 } ) } { \partial ( \widehat { p } _ { n + 1 } , q _ { n + 1 } ) } \equiv \left( \begin{array} { c c } { { I - h G ^ { T } \mu _ { \widehat { p } } } } & { { S - h G ^ { T } \mu _ { \widehat { q } } } } \\ { { 0 } } & { { I } } \end{array} \right) ,
$$

where $\mu _ { n + 1 }$ of(1.20)isconsideredasa function of $( \widehat { p } _ { n + 1 } , q _ { n + 1 } )$ ,and $S \ =$ $- h \mu ^ { T } g _ { q q }$ Thisis formallythesameas(1.21）with $H \equiv 0$ Consequently,the symplecticity conditionis also satisfied for this mapping.As acomposition of two symplectic transformations,the numerical flow of our first ordermethod is therefore also symplectic.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0004_pages_0211-0280/auto/images/c6f4de01610efba06408a35c9299bf705e1ef1319f441d0fca97bce8394a7c4e.jpg)  
Fig.1.2.Spherical pendulum problem solved with the symplectic Euler method(1.19)- （1.20)and withtheimplicit Euler method;initial value $q _ { 0 } ~ = ~ ( \sin ( 1 . 3 ) , 0 , \cos ( 1 . 3 ) )$ $p _ { 0 } = ( 3 \cos ( 1 . 3 ) , 6 . 5 , - 3 \sin ( 1 . 3 ) )$ stepsize $h = 0 . 0 1$

Numerical Experiment.Consider the equations(1.3) for the spherical pendulum. Foramass $m = 1$ theycoincide with the Hamiltonian formulation.Figure 1.2 (upper picture） shows the numerical solution (vertical coordinate $q _ { 3 }$ overmany periodsobtained bymethod(1.19)-(1.2O).We observearegular qualitatively correct behaviour.For theimplicit Eulermethod(i.e.,theargument $q _ { n }$ isreplacedwith $q _ { n + 1 }$ in(1.19)) the numerical solution,obtained with the same step size and the same initial values,is less satisfactory.Alreadyafter one periodthe solution deteriorates and the pendulum loses energy.

# VII.1.4 SHAKE and RATTLE

The numerical method(1.19)-(1.20) isonly of order1and it is not symmetric.An algorithm that is of order2,symmetricand symplecticwas originally considered for separableHamiltonians

$$
H ( p , q ) = \frac { 1 } { 2 } p ^ { T } M ^ { - 1 } p + U ( q )
$$

with constant mass matrix $M$ Notice that in this casewe are concernedwith a second order differential equation $M \ddot { q } = - U _ { q } ( q ) - G ( q ) ^ { \cal T } \lambda$ with $g ( q ) = 0$ .

SHAKE.Ryckaert,Ciccotti& Berendsen（1977） propose themethod

$$
\begin{array} { r c l } { { q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } } } & { { = } } & { { - h ^ { 2 } M ^ { - 1 } \big ( U _ { q } ( q _ { n } ) + G ( q _ { n } ) ^ { T } \lambda _ { n } \big ) } } \\ { { } } & { { } } & { { } } \\ { { 0 } } & { { = } } & { { g ( q _ { n + 1 } ) } } \end{array}
$$

forcomputationsin molecular dynamics.Itis a straightforward extension of the Stormer-Verlet scheme(I.1.15).The $p$ -components,not used in therecursionare approximatedby $p _ { n } = M ( q _ { n + 1 } - q _ { n - 1 } ) / 2 h$

RATTLE.The three-term recursion (1.23）may lead toan accumulation of roundoff errors,and areformulation asa one-step method isdesirable.Using the same procedure asin(I.1.17)we formally get

$$
\begin{array} { r l r } {  { p _ { n + 1 / 2 } = p _ { n } - \frac { h } { 2 } \bigl ( U _ { q } ( q _ { n } ) + G ( q _ { n } ) ^ { T } \lambda _ { n } \bigr ) } } \\ & { } & { q _ { n + 1 } = q _ { n } + h M ^ { - 1 } p _ { n + 1 / 2 } , \qquad 0 = g ( q _ { n + 1 } ) } \\ & { } & { \bar { p } _ { n + 1 } = p _ { n + 1 / 2 } - \frac { \displaystyle h } { \displaystyle 2 } \bigl ( U _ { q } ( q _ { n + 1 } ) + G ( q _ { n + 1 } ) ^ { T } \lambda _ { n + 1 } \bigr ) . } \end{array}
$$

The difficulty with this formulation is that $\lambda _ { n + 1 }$ is not yet available at this step (it is computed together with $q _ { n + 2 }$ ).Asaremedy,Andersen(1983) suggests replacing thelast line in(1.24) with a projection step similar to(1.20)

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n + 1 } ~ = ~ p _ { n + 1 / 2 } - \displaystyle \frac { h } { 2 } \big ( U _ { q } ( q _ { n + 1 } ) + G ( q _ { n + 1 } ) ^ { T } \mu _ { n } \big ) } } \\ { { } } & { { } } & { { 0 ~ = ~ G \big ( q _ { n + 1 } \big ) M ^ { - 1 } p _ { n + 1 } . } } \end{array}
$$

Thismodification,calledRATTLE,has thefurtheradvantage that thenumerical approximation $( p _ { n + 1 } , q _ { n + 1 } )$ lies on the solution manifold $\mathcal { M }$ Thesymplecticityof thisalgorithm has been established byLeimkuhler& Skeel(1994).

Extension to General Hamiltonians.As observed independently by Jay(1994) andReich(1993),theRATTLE algorithmcan be extended togeneral Hamiltonians as follows:for consistent values $( p _ { n } , q _ { n } ) \in \mathcal { M }$ define

$$
\begin{array} { r c l } { \displaystyle p _ { n + 1 / 2 } ~ = ~ p _ { n } - \frac { h } { 2 } \big ( H _ { q } ( p _ { n + 1 / 2 } , q _ { n } ) + G ( q _ { n } ) ^ { T } \lambda _ { n } \big ) } \\ { \displaystyle q _ { n + 1 } ~ = ~ q _ { n } + \frac { h } { 2 } \big ( H _ { p } ( p _ { n + 1 / 2 } , q _ { n } ) + H _ { p } ( p _ { n + 1 / 2 } , q _ { n + 1 } ) \big ) } \\ { \displaystyle ~ 0 ~ = ~ g ( q _ { n + 1 } ) } \\ { \displaystyle p _ { n + 1 } ~ = ~ p _ { n + 1 / 2 } - \frac { h } { 2 } \big ( H _ { q } ( p _ { n + 1 / 2 } , q _ { n + 1 } ) + G ( q _ { n + 1 } ) ^ { T } \mu _ { n } \big ) } \\ { \displaystyle ~ 0 ~ = ~ G ( q _ { n + 1 } ) H _ { p } ( p _ { n + 1 } , q _ { n + 1 } ) . } \end{array}
$$

Thefirst three equations of(1.26)arevery similarto(1.19) and the last two equations to (1.20).The existence of (locally）unique solutions $( p _ { n + 1 / 2 } , q _ { n + 1 } , \lambda _ { n } )$ and $( p _ { n + 1 } , \mu _ { n } )$ cantherefore be proved in the same way.Notice also that this method givesa numerical solution that stays exactly on the solution manifold $\mathcal { M }$

Theorem1.3.Thenumericalmethod(1.26)issymmetric,symplectic,andconvergent of order two.

Proof.Although this theorem is the special case $s = 2$ of Theorem 1.4,we outline its proof.We will see that the convergence result is easier to obtain for $s = 2$ than for the general case.

Ifwe add to(1.26) the consistency conditions $g ( q _ { n } ) = 0$ , $G ( q _ { n } ) H _ { p } ( p _ { n } , q _ { n } ) =$ Oofthe initial values,thesymmetry of the method follows at once by exchanging $h  - h$ , $p _ { n + 1 }  p _ { n }$ , $q _ { n + 1 }  q _ { n }$ ,and $\lambda _ { n }  \mu _ { n } .$ The symplecticity can be proved asfor(1.19)-(1.20)bycomputing the derivative of $( p _ { n + 1 } , q _ { n + 1 } )$ with respect to $( p _ { n } , q _ { n } )$ ,andbyverifyingthecondition(1.16).Thisdoesnot seemto be simpler thanthe symplecticity proof ofTheorem1.4.

Theimplicit function theoremapplied tothe two subsystems of(1.26)shows

$$
p _ { n + 1 / 2 } = p _ { n } + \mathcal { O } ( h ) , \quad h \lambda = \mathcal { O } ( h ) , \quad p _ { n + 1 } = p _ { n + 1 / 2 } + \mathcal { O } ( h ) , \quad h \mu = \mathcal { O } ( h ) ,
$$

and,insertedinto(1.26）,yields

$$
q _ { n + 1 } = q ( t _ { n + 1 } ) + \mathcal { O } ( h ^ { 2 } ) , \quad p _ { n + 1 } = p ( t _ { n + 1 } ) - G \big ( q ( t _ { n + 1 } ) \big ) ^ { T } \nu + \mathcal { O } ( h ^ { 2 } ) .
$$

Convergence of order one follows therefore in the same way as for method(1.19)- (1.20).Since the order of a symmetric method is always even,this implies convergence of order two. □

Aneasy way of obtaining high order methods for constrained Hamiltonian systemsisbycomposition(Reich 1996a).Method(1.26)isan idealcandidateas basic integrator for compositions of the form (V.3.2).The resulting integrators are symmetric,symplectic,of high order,and yield a numerical solution that stays on the manifold $\mathcal { M }$ .

# VII.1.5 The Lobatto IIIA - IIB Pair

Another possibility for obtaining high order symplectic integrators for constrained Hamiltonian systems is by the use of partitioned Runge-Kutta or discontinuous collocation methods.We consider the system (1.9)and we search for polynomials $u ( t )$ ofdegree $s$ ， $w ( t )$ ofdegree $s - 1$ ,and $v ( t )$ ofdegree $s - 2$ such that

$$
u ( t _ { n } ) = q _ { n } , \qquad v ( t _ { n } ) = p _ { n } - h b _ { 1 } \delta ( t _ { n } )
$$

with the defect

$$
{ \delta ( t ) = \dot { v } ( t ) + H _ { q } \big ( { v ( t ) , u ( t ) } \big ) + G \big ( { u ( t ) } \big ) ^ { T } w ( t ) }
$$

and,using theabbreviation $t _ { n , i } = t _ { n } + c _ { i } h$ ，

$$
\begin{array} { r l r } { \dot { \iota } ( t _ { n , i } ) { \bf \Phi } = } & { { \cal H } _ { p } \big ( v ( t _ { n , i } ) , u ( t _ { n , i } ) \big ) , \quad i = 1 , \dots , s } & { ( 1 . 2 ) } \\ { \dot { v } ( t _ { n , i } ) { \bf \Phi } = } & { - { \cal H } _ { q } \big ( v ( t _ { n , i } ) , u ( t _ { n , i } ) \big ) - G \big ( u ( t _ { n , i } ) \big ) ^ { T } w ( t _ { n , i } ) , \quad i = 2 , \dots , s - 1 } & \\ { { \bf \Phi } 0 { \bf \Phi } = g \big ( u ( t _ { n , i } ) \big ) , \quad i = 1 , \dots , s . } & \end{array}
$$

If these polynomials exist,the numerical solution is defined by

$$
\begin{array} { c } { q _ { n + 1 } = u ( t _ { n } + h ) , \qquad p _ { n + 1 } = v ( t _ { n } + h ) - h b _ { s } \delta ( t _ { n } + h ) } \\ { 0 = G ( q _ { n + 1 } ) H _ { p } ( p _ { n + 1 } , q _ { n + 1 } ) . } \end{array}
$$

Why Discontinuous Collocation Based on Lobatto Quadrature? At a first glance(Theorem VI.4.2) it seems natural to consider collocation methods based on Gaussian quadrature forthe entire system.This,however,has thedisadvantage that thenumerical solution does not satisfy $g ( q _ { n + 1 } ) = 0$ Toachieve this requirement, $t _ { n } + h$ has to be one of the collocation points,i.e.,we must have $c _ { s } = 1$ Unfortunately,none of the collocation or discontinuous collocation methods with $c _ { s } = 1$ is symplectic (see Exercise IV.6).We therefore turn our attention to partitioned methods,and we treat only the $q$ -component byacollocation method satisfying $c _ { s } = 1$ To satisfy the s conditions $g ( u ( t _ { n , i } ) ) = 0$ of（1.29）there are only $s - 1$ freeparameters $w ( t _ { n } )$ , $w ( t _ { n } + c _ { 2 } h ) , \dots , w ( t _ { n } + c _ { s - 1 } h )$ available.Aremedyistochoose $c _ { 1 } = 0$ so that the first condition $g ( u ( t _ { n } ) ) = 0$ isautomatically verified.Encouragedby TheoremVI.4.5weare thusled to considertheLobatto nodesin therole ofthe $c _ { i }$ .Theuse of thepartitioned Lobatto IIIA-IB pair for the treatment of constrained Hamiltonian systems has been suggested by Jay (1994,1996).

Existence and Uniqueness of the Numerical Solution. The polynomial $u ( t )$ of degree $s$ isuniquely determined by $u ( t _ { n } ) = q _ { n }$ and $\dot { u } ( t _ { n , i } ) = : Q _ { i }$ $i = 1 , \ldots , s )$ ， thepolynomial $v ( t )$ ofdegree $s - 2$ is uniquely determined by $v ( t _ { n , i } ) = : P _ { i }$ $i =$ $1 , \ldots , s - 1 )$ ,andthepolynomial $w ( t )$ ofdegree $s - 1$ isuniquely determined by $h w ( t _ { n , i } ) ~ = : \ A _ { i }$ $\ i = 1 , \ldots , s$ .Notice that thevalue $\varLambda _ { s }$ is only involved in (1.30)and not in(1.27)-(1.29).For thenonlinearsystem(1.27)-(1.29)we therefore consider

$$
X = ( \dot { Q } _ { 1 } , \dots , \dot { Q } _ { s } , P _ { 1 } , \dots , P _ { s - 1 } , \lambda _ { 1 } , \dots , \lambda _ { s - 1 } )
$$

asindependent variables,and we write the system as $F ( X , h ) = 0 $ The function $F$ is composed of the $s$ conditions for $\dot { u } ( t _ { n , i } )$ ,of the definition of $\boldsymbol { v } ( t _ { n } )$ (divided by $b _ { 1 }$ ）andthe $s \gets 2$ conditions for $\dot { v } ( t _ { n , i } )$ (multiplied by $h$ ）,andfinallyofthe $s - 1$ equations $0 ~ = ~ g \big ( u ( t _ { n , i } ) \big )$ for $i = 2 , \dots , s$ (divided by $h$ ).Observethat $0 = g \big ( u ( t _ { n } ) \big )$ isautomatically satisfied by the consistency of $( p _ { n } , q _ { n } )$ We note that $P _ { s } = v ( t _ { n } + h )$ and ${ \dot { P } } _ { i } = h { \dot { v } } ( t _ { n , i } )$ are linear combinations of $P _ { 1 } , \ldots , P _ { s - 1 }$ with coefficients independent of the step size $h$

Thefunction $F ( X , h )$ is well-defined for $h$ inaneighbourhood of $0$ For the first twoblocks this isevident,for thelast one it follows from the identity

$$
\frac { 1 } { h } g \big ( u ( t _ { n , i } ) \big ) = \int _ { 0 } ^ { c _ { i } } G \big ( u ( t _ { n } + \theta h ) \big ) \dot { u } ( t _ { n } + \theta h ) d \theta
$$

using the fact that ${ \dot { u } } ( t _ { n } + \theta h )$ isa linear combination of $Q _ { i }$ for $\ i = 1 , \dots , s .$ With thevalues

$$
X _ { 0 } = \left( H _ { p } ( p _ { n } , q _ { n } ) , \dots , H _ { p } ( p _ { n } , q _ { n } ) , p _ { n } , \dots , p _ { n } , 0 , \dots , 0 \right)
$$

we have that $F ( X _ { 0 } , 0 ) = 0$ ,because the values $( p _ { n } , q _ { n } )$ are assumed to be consistent.In view of an application of the implicit function theorem we compute

$$
\frac { \partial F } { \partial X } ( X _ { 0 } , 0 ) = \left( \begin{array} { c c c } { { I \otimes I } } & { { - D \otimes H _ { p p } } } & { { 0 } } \\ { { 0 } } & { { B \otimes I } } & { { I \otimes G ^ { T } } } \\ { { A \otimes G } } & { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $H _ { p p }$ , $G$ are evaluated at $\left( p _ { n } , q _ { n } \right)$ ,and $A , B , D$ are matrices of dimension $( s - 1 ) \times s$ , $( s - 1 ) \times ( s - 1 )$ and $s \times ( s - 1 )$ respectively thatdepend only on the Lobatto quadratureand not on the differential equation.For example,the matrix $B$ represents the linear mapping

$$
\big ( P _ { 1 } , \ldots , P _ { s - 1 } \big ) \mapsto \big ( \dot { P } _ { 1 } + b _ { 1 } ^ { - 1 } P _ { 1 } , \dot { P } _ { 2 } , \ldots , \dot { P } _ { s - 1 } \big ) .
$$

This mappingis invertible,because the values on theright-hand sideuniquely determine the polynomial $\upsilon ( t )$ ofdegree $s - 2$ .

Block Gaussian elimination thenshows that (1.31) is invertible ifand only if the matrix

$$
A D B ^ { - 1 } \otimes G H _ { p p } G ^ { T } \qquad \mathrm { i s ~ i n v e r t i b l e } .
$$

Because of(1.13) it remains to show that $A D B ^ { - 1 }$ isinvertible.

To achieve this without explicitly computing the matrices $A , B , D$ ,weapply the method to the problem where $p$ and $q$ are of dimension one, $H ( p , q ) = p ^ { 2 } / 2$ ,and $g ( q ) = q$ Assuming $h = 1$ weget

$$
\begin{array} { l } { { u ( 0 ) = 0 , \qquad v ( 0 ) = - b _ { 1 } \bigl ( \dot { v } ( 0 ) + w ( 0 ) \bigr ) } } \\ { { \dot { u } ( c _ { i } ) = v ( c _ { i } ) \qquad \mathrm { f o r } i = 1 , \ldots , s } } \\ { { \dot { v } ( c _ { i } ) = - w ( c _ { i } ) \qquad \mathrm { f o r } i = 2 , \ldots , s - 1 } } \\ { { 0 = u ( c _ { i } ) \qquad \mathrm { f o r } i = 1 , \ldots , s , } } \end{array}
$$

which is equivalent to

$$
\begin{array} { r } { \left( \begin{array} { c c c } { I } & { - D } & { 0 } \\ { 0 } & { B } & { I } \\ { A } & { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c } { ( \Dot { u } ( c _ { i } ) ) _ { i = 1 } ^ { s } } \\ { ( v ( c _ { i } ) ) _ { i = 1 } ^ { s - 1 } } \\ { ( w ( c _ { i } ) ) _ { i = 1 } ^ { s - 1 } } \end{array} \right) = \left( \begin{array} { c } { 0 } \\ { 0 } \\ { 0 } \end{array} \right) , } \end{array}
$$

because $H _ { p p } ( p , q ) = 1$ and $G ( q ) = 1$ Since $u ( t )$ isa polynomial of degree $s$ , the last equation of (1.32) implies that $u ( t ) = C \prod _ { j = 1 } ^ { \circ } ( t - c _ { j } ) .$ Bythe second relation the polynomial ${ \dot { u } } ( t ) - v ( t )$ ,whichis of degree $s - 1$ ,vanishesat $s$ points. Hence, $v ( t ) \equiv \dot { u } ( t )$ ,which ispossible only if $C = 0$ ,because the degree of $v ( t )$ is $s - 2$ .Consequently,thelinearsystem(1.33) has only the trivial solution,so that the matrixin（1.33）and hence also $A D B ^ { - 1 }$ isinvertible.

The implicit function theorem applied to $F ( X , h ) = 0$ shows that the nonlinear system (1.27)-(1.30) possesses a locally unique solution for suficiently small step sizes $h$ Using the free parameter $\varLambda _ { s } = h w ( t _ { n } + h )$ ,afurther application of the implicit function theorem,this time to thesmallsystem(1.3O),proves the existence and local uniqueness of $p _ { n + 1 }$

Theorem 1.4.Let $( b _ { i } , c _ { i } ) _ { i = 1 } ^ { s }$ betheweightsand nodes oftheLobatto quadrature (c.f.(II.1.17)).Themethod(1.27)-(1.29)-(1.30)issymmetric,symplectic,andsuperconvergent oforder $2 s - 2$ .

Proof.Symmetry.To the formulas(1.27)-(1.29)-(1.30)weadd theconsistency relations $g ( q _ { n } ) ~ = ~ 0$ , $G ( q _ { n } ) H _ { p } ( p _ { n } , q _ { n } ) \ = \ 0$ Thenwe exchange $( t _ { n } , p _ { n } , q _ { n } ) \ $ $( t _ { n + 1 } , p _ { n + 1 } , q _ { n + 1 } )$ and $h  - h$ Since $b _ { 1 } = b _ { s }$ and $c _ { s + 1 - i } = 1 - c _ { i }$ for theLobatto quadrature,the resulting formulas are equivalent to the original method(see also the proof of Theorem V.2.1).

Symplecticity.We fix $\xi _ { 1 } , \xi _ { 2 } \in \mathfrak { I } _ { ( p _ { n } , q _ { n } ) } \mathcal { M }$ we put $x _ { n } = ( p _ { n } , q _ { n } ) ^ { 1 } ,$ and we consider the bilinear mapping

$$
\Big . \Big . \Big . \Big > \Big ( \frac { \partial p _ { n + 1 } } { \partial x _ { n } } , \frac { \partial q _ { n + 1 } } { \partial x _ { n } } \Big ) = \xi _ { 1 } ^ { T } \bigg ( \Big ( \frac { \partial q _ { n + 1 } } { \partial x _ { n } } \Big ) ^ { T } \Big ( \frac { \partial p _ { n + 1 } } { \partial x _ { n } } \Big ) - \Big ( \frac { \partial p _ { n + 1 } } { \partial x _ { n } } \Big ) ^ { T } \Big ( \frac { \partial q _ { n + 1 } } { \partial x _ { n } } \Big ) \bigg ) \xi _ { 2 } .
$$

The symplecticity of the transformation $( p _ { n } , q _ { n } ) \mapsto ( p _ { n + 1 } , q _ { n + 1 } )$ on the manifold $\mathcal { M }$ is then expressed by the relation

$$
Q \Big ( \frac { \partial p _ { n + 1 } } { \partial x _ { n } } , \frac { \partial q _ { n + 1 } } { \partial x _ { n } } \Big ) = Q \Big ( \frac { \partial p _ { n } } { \partial x _ { n } } , \frac { \partial q _ { n } } { \partial x _ { n } } \Big ) .
$$

Wenow follow closelytheproof of Theorem IV.2.3.Weconsider thepolynomials $u ( t ) , v ( t ) , w ( t )$ ofthe method(1.27)-(1.29)-(1.30) as functions of $t$ and $x _ { n } = ( p _ { n } , q _ { n } )$ ,andwe compute

$$
\begin{array} { l } { \displaystyle Q \Big ( \frac { \partial v ( t _ { n + 1 } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n + 1 } ) } { \partial x _ { n } } \Big ) ~ = ~ Q \Big ( \frac { \partial v ( t _ { n } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n } ) } { \partial x _ { n } } \Big ) } \\ { \displaystyle ~ = ~ \int _ { t _ { n } } ^ { t _ { n + 1 } } \frac { d Q } { d t } \Big ( \frac { \partial v ( t ) } { \partial x _ { n } } , \frac { \partial u ( t ) } { \partial x _ { n } } \Big ) d t . } \end{array}
$$

Since $u ( t )$ isapolynomial of degree $s$ and $v ( t )$ ofdegree $s - 2$ ,theintegrand in (1.35)isapolynomial in $t$ ofdegree $2 s - 3 .$ Itis thus integrated without error by the Lobatto quadrature.By definition thesepolynomials satisfy the differential equation attheinteriorcollocation points.Therefore,it follows from(1.17) that

$$
\frac { d Q } { d t } \Big ( \frac { \partial v ( t _ { n , i } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n , i } ) } { \partial x _ { n } } \Big ) = 0 \qquad \mathrm { f o r ~ } i = 2 , \dots , s = 1 ,
$$

and that

$$
\frac { d Q } { d t } \Big ( \frac { \partial v ( t _ { n , i } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n , i } ) } { \partial x _ { n } } \Big ) = Q \Big ( \frac { \partial \delta ( t _ { n , i } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n , i } ) } { \partial x _ { n } } \Big ) \quad \mathrm { f o r ~ \ } i = 1 \mathrm { a n d } i = s
$$

Applying theLobatto quadrature to the integral in（1.35）thusyields

$$
h b _ { 1 } Q \Big ( \frac { \partial \delta ( t _ { n } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n } ) } { \partial x _ { n } } \Big ) + h b _ { s } Q \Big ( \frac { \partial \delta ( t _ { n + 1 } ) } { \partial x _ { n } } , \frac { \partial u ( t _ { n + 1 } ) } { \partial x _ { n } } \Big ) ,
$$

and the symplecticity relation(1.34） follows in the sameway asin theproofof Theorem IV.2.3.

Superconvergence.This is the most difficult part of theproof.We remark that superconvergence of Runge-Kutta methods fordifferential-algebraic systems of index 3 hasbeenconjecturedbyHairer,Lubich&Roche(1989),anda firstproof hasbeen obtained by Jay(1993) forcollocationmethods.In his thesisJay(1994）provessuperconvergence fora more general class of methods,including the Lobatto IIIA-IIIBpair,usinga“rooted-tree-type”theory.Asketch of thatvery elaborateproof ispublishedinJay(1996).Using the idea of discontinuous collocation,the elegant proof forcollocationmethods can now be extended to cover theLobatto IIIA-IIB pair.In the followingwe explain how the local error can be estimated.

We consider the polynomials $u ( t ) , v ( t ) , w ( t )$ defined in (1.27)-(1.29)-(1.30), and we define defects $\mu ( t ) , \delta ( t ) , \theta ( t )$ asfollows:

$$
\begin{array} { r l r } { \dot { u } ( t ) \ = \ } & { { } H _ { p } \big ( v ( t ) , u ( t ) \big ) + \mu ( t ) } & { } \\ { \dot { v } ( t ) \ = \ } & { { } - H _ { q } \big ( v ( t ) , u ( t ) \big ) - G \big ( u ( t ) \big ) ^ { T } w ( t ) + \delta ( t ) } & { } \\ { 0 \ = \ g \big ( u ( t ) \big ) + \theta ( t ) . } & { } \end{array}
$$

Bydefinition of the method we have

$$
\begin{array} { l l } { { \mu ( t _ { n } + c _ { i } h ) = 0 , } } & { { \quad i = 1 , \dots , s } } \\ { { \delta ( t _ { n } + c _ { i } h ) = 0 , } } & { { \quad i = 2 , \dots , s - 1 } } \\ { { \theta ( t _ { n } + c _ { i } h ) = 0 , } } & { { \quad i = 1 , \dots , s . } } \end{array}
$$

Welet ${ \boldsymbol { q } } ( t ) , { \boldsymbol { p } } ( t ) , \lambda ( t )$ be the exact solution of（1.9)satisfying $q ( t _ { n } ) = q _ { n }$ ，, $p ( t _ { n } ) =$ $p _ { n }$ ,andwe considerthedifferences

$$
\Delta u ( t ) = u ( t ) - q ( t ) , \quad \Delta v ( t ) = v ( t ) - p ( t ) , \quad \Delta w ( t ) = w ( t ) - \lambda ( t ) .
$$

Subtracting(1.9) from (1.36)we getby linearization that

$$
\begin{array} { l } { \dot { \Delta u } = a _ { 1 1 } ( t ) \Delta u + a _ { 1 2 } ( t ) \Delta v + \mu ( t ) } \\ { \dot { \Delta v } = a _ { 2 1 } ( t ) \Delta u + a _ { 2 2 } ( t ) \Delta v + a _ { 2 3 } ( t ) \Delta w + \delta ( t ) , } \end{array}
$$

where $a _ { 1 2 } ( t ) = H _ { p p } ( p ( t ) , q ( t ) )$ ,andwhere the other $a _ { i j } ( t )$ are given by similar expressions.We have suppressed quadratic and higher order terms to keep the presentation as simple as possible.They do not influence the convergence result.To eliminate $\varDelta w$ in(1.38),we differentiate the algebraic relations in(1.9)and（1.36) twice,andwe subtract them.This yields

$$
\begin{array} { r l } { 0 } & { = \ F ( t , \mu ( t ) ) + b _ { 1 } ( t ) \varDelta { u } + b _ { 2 } ( t ) \varDelta { v } + \varDelta ( t ) \varDelta { w } } \\ { } & { + \ G \bigl ( u ( t ) \bigr ) H _ { p p } \bigl ( v ( t ) , u ( t ) \bigr ) \delta ( t ) + G \bigl ( u ( t ) \bigr ) \dot { \mu } ( t ) + \ddot { \theta } ( t ) , } \end{array}
$$

where $F ( t , \mu )$ , $B ( t )$ ， $b _ { 1 } ( t )$ , $b _ { 2 } ( t )$ are functions depending on $p ( t )$ ， $q ( t )$ ， $\lambda ( t )$ , $u ( t )$ , $v ( t )$ ， $w ( t )$ ,andwhere $F ( t , 0 ) = 0$ and $B ( t ) \approx G ( q _ { n } ) H _ { p p } ( p _ { n } , q _ { n } ) G ( q _ { n } ) ^ { \scriptscriptstyle 1 } ,$ Because ofourassumption（1.13）wecan extract $\varDelta w$ from this relation,and we insert it into (1.38).In thiswaywe geta lineardifferential equation for $\varDelta u , \varDelta v$ ,which can be solvedby the“variation of constants”formula.Using $\varDelta u ( t _ { n } ) = 0$ (by(1.27)）,the solution $\Delta v ( t _ { n } + h )$ is seento be of the form

$$
\begin{array} { l } { \Delta v ( t _ { n } + h ) = R _ { 2 2 } ( t _ { n } + h , t _ { n } ) \Delta v ( t _ { n } ) + \displaystyle \int _ { t _ { n } } ^ { t _ { n } + h } \Big ( R _ { 2 1 } ( t _ { n } + h , t ) \mu ( t ) } \\ { \displaystyle \qquad + \ R _ { 2 2 } ( t _ { n } + h , t ) \Big ( \delta ( t ) + \widetilde { F } ( t , \mu ( t ) ) + c _ { 1 } ( t ) \ddot { \mu } ( t ) } \\ { \displaystyle \qquad + \ C ( t ) \Big ( G \big ( u ( t ) \big ) H _ { p p } \big ( v ( t ) , u ( t ) \big ) \delta ( t ) + \ddot { \theta } ( t ) \Big ) \Big ) \Big ) d t , } \end{array}
$$

where $R _ { 2 1 }$ and $R _ { 2 2 }$ are thelower blocks of the resolvent,and $\check { F } , c _ { 1 } , C$ are functions asbefore.To prove that thelocal error of the $p$ -component

$$
p _ { n + 1 } - p ( t _ { n } + h ) = \Delta v ( t _ { n } + h ) - h b _ { s } \delta ( t _ { n } + h )
$$

is of size $\mathcal { O } ( h ^ { 2 s - 1 } )$ ,wefirst integrate byparts those expressions in（1.39)which containaderivative.For example,

$$
\int _ { t _ { n } } ^ { t _ { n + 1 } } a ( t ) \dot { \mu } ( t ) d t = a ( t ) \mu ( t ) \Big | _ { t _ { n } } ^ { t _ { n + 1 } } - \int _ { t _ { n } } ^ { t _ { n + 1 } } \dot { a } ( t ) \mu ( t ) d t = \mathcal { O } ( h ^ { 2 s - 1 } ) ,
$$

because $\mu ( t _ { n } ) = \mu ( t _ { n } + h ) = 0$ by(1.37)andan application of theLobatto quadrature tothe integral at theright-hand side gives zero as result withaquadrature error of size ${ \mathcal { O } } ( h ^ { 2 s - 1 } ) .$ Similarly,integratingbypartstwiceyields

$$
\begin{array} { r c l } { \displaystyle \int _ { t _ { n } } ^ { t _ { n + 1 } } a ( t ) \ddot { \theta } ( t ) d t \ = \ } & { \displaystyle a ( t ) \dot { \theta } ( t ) \Big | _ { t _ { n } } ^ { t _ { n + 1 } } - \dot { a } ( t ) \theta ( t ) \Big | _ { t _ { n } } ^ { t _ { n + 1 } } + \int _ { t _ { n } } ^ { t _ { n + 1 } } \ddot { a } ( t ) \theta ( t ) d t } \\ { \displaystyle } & { = \ } & { \displaystyle a ( t _ { n + 1 } ) \dot { \theta } ( t _ { n + 1 } ) - a ( t _ { n } ) \dot { \theta } ( t _ { n } ) + O ( h ^ { 2 s - 1 } ) . } \end{array}
$$

Totheother integrals in（1.39） we apply the Lobatto quadrature directly.Since $R _ { 2 2 } ( t _ { n + 1 } , t _ { n + 1 } )$ is theidentity,this gives

$$
\begin{array} { r l r } {  { p _ { n + 1 } - p ( t _ { n + 1 } ) = R _ { 2 2 } ( t _ { n + 1 } , t _ { n } ) \Big ( \varDelta v ( t _ { n } ) + h b _ { 1 } \delta ( t _ { n } ) \Big ) } } \\ & { } & { + \tilde { C } ( t _ { n + 1 } ) \Big ( h b _ { s } G \big ( u ( t _ { n + 1 } ) \big ) H _ { p p } \big ( v ( t _ { n + 1 } ) , u ( t _ { n + 1 } ) \big ) \delta ( t _ { n + 1 } ) + \dot { \theta } ( t _ { n + 1 } ) } \\ & { } & { + \tilde { C } ( t _ { n } ) \Big ( h b _ { 1 } G \big ( u ( t _ { n } ) \big ) H _ { p p } \big ( v ( t _ { n } ) , u ( t _ { n } ) \big ) \delta ( t _ { n } ) - \dot { \theta } ( t _ { n } ) \Big ) + \mathcal { O } ( h ^ { 2 s - 1 } ) } \end{array}
$$

where $\begin{array} { r } { \dot { C } ( t ) = R ( t _ { n + 1 } , t ) C ( t ) } \end{array}$ Theterm $\Delta v ( t _ { n } ) + h b _ { 1 } \delta ( t _ { n } )$ vanishes by (1.27), and differentiationof thealgebraicrelation in（1.36)yields

$$
0 = G { \big ( } u ( t ) { \big ) } { \Big ( } H _ { p } { \big ( } v ( t ) , u ( t ) { \big ) } + \mu ( t ) { \Big ) } + { \dot { \theta } } ( t ) .
$$

Asaconsequence of(1.27),(1.37)and the consistency of the initial values $( p _ { n } , q _ { n } )$ this gives

$$
\begin{array} { l l l } { \dot { \theta } ( t _ { n } ) } & { = } & { - G ( q _ { n } ) H _ { p } ( p _ { n } - h b _ { 1 } \delta ( t _ { n } ) , q _ { n } ) } \\ & { = } & { h b _ { 1 } G ( q _ { n } ) H _ { p p } ( p _ { n } , q _ { n } ) \delta ( t _ { n } ) + { \mathcal O } \big ( h ^ { 2 } \delta ( t _ { n } ) ^ { 2 } \big ) } \\ & { = } & { h b _ { 1 } G \big ( u ( t _ { n } ) \big ) H _ { p p } \big ( v ( t _ { n } ) , u ( t _ { n } ) \big ) \delta ( t _ { n } ) + { \mathcal O } \big ( h ^ { 2 } \delta ( t _ { n } ) ^ { 2 } \big ) . } \end{array}
$$

Using(1.30)we getin the same way

$$
\dot { \bar { g } } ( t _ { n + 1 } ) , = - h b _ { s } G \bigl ( u ( t _ { n + 1 } ) \bigr ) H _ { p p } \bigl ( v ( t _ { n + 1 } ) , u ( t _ { n + 1 } ) \bigr ) \delta ( t _ { n + 1 } ) + \mathcal { O } \bigl ( h ^ { 2 } \delta ( t _ { n + 1 } ) \bigr )
$$

These estimates together show that the local error（1.41） is of size $O ( h ^ { 2 s - 1 } ) +$ ${ \mathcal O } \left( h ^ { 2 } \delta ( t ) ^ { 2 } \right) .$ Thedefect $\delta ( t )$ vanishesat $s - 2$ points in the interval $[ t _ { n } , t _ { n + 1 } ]$ ,so that $\delta ( t ) = \mathcal { O } ( h ^ { s - 2 } )$ for $t \in [ t _ { n } , t _ { n + 1 } ]$ (forarigorous proof of this statement one hastoapply the techniquesof theproof of Theorem II.1.5).Therefore we obtain $p _ { n + 1 } - p ( t _ { n + 1 } ) = \mathcal { O } ( h ^ { 2 s - 2 } )$ ,andby the symmetry of themethod also $\mathcal { O } ( h ^ { 2 s - 1 } )$ .

Inanalogyto(1.39),the variation of constants formula yieldsalso an expression for the local error $q _ { n + 1 } - q ( t _ { n + 1 } ) \ = \ \Delta u ( t _ { n + 1 } )$ One only has to replace $R _ { 2 1 }$ and $R _ { 2 2 }$ with the upper blocks $R _ { 1 1 }$ and $R _ { 1 2 }$ of the resolvent.Using $R _ { 1 2 } ( t _ { n + 1 } , t _ { n + 1 } ) ~ = ~ 0$ ,weprove in the same way that the local error of the $q$ component is of size $\mathcal { O } ( h ^ { 2 s - 1 } )$ .

Theestimation of the global erroris obtainedin the same way as for the first ordermethod(1.19)-(1.20).Since thealgorithmisamapping $\phi _ { h } : { \mathcal { M } } \to { \mathcal { M } }$ on the solutionmanifold,itis not necessary to followthe technicallydiffcult proofs in the context of differential-algebraic equations.Summingup the propagated local errors proves that the global error satisfies $p _ { n } - p ( t _ { n } ) = \mathcal { O } ( h ^ { 2 s - 2 } )$ and $q _ { n } - q ( t _ { n } ) =$ $\mathcal { O } ( h ^ { 2 s - 2 } )$ as longas $t _ { n } = n h \leq C o n s t$ □

# VII.1.6 Splitting Methods

Whenconsidering splitingmethods for constrained mechanical systems,it should beborne in mind that such systems are differential equations on manifolds(see

Sect.VII.1.2).Splitting methods should therefore be based on a decomposition $f ( y ) = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y )$ ,whereboth $f ^ { [ i ] } ( y )$ are vector fields on the same manifoldas $f ( y ) .$ Letusconsider here the Hamiltonian system(1.9）with Hamiltonian

$$
H ( p , q ) = H ^ { [ 1 ] } ( p , q ) + H ^ { [ 2 ] } ( p , q ) .
$$

The manifold for this differential equation is

$$
\mathcal { M } = \{ ( p , q ) \mid g ( q ) = 0 , G ( q ) H _ { p } ( p , q ) = 0 \} .
$$

Notice that (1.9）,when $H$ is simply replaced with $H ^ { [ i ] }$ ,is notagood candidate for splitting methods:the existence of a solutionis not guaranteed,and if the solution exists it need not stay on the manifold $\mathcal { M }$ .The following lemma indicates how splitting methods should be applied.

Lemma1.5.Considera Hamiltonian(1.42),afunction $g ( q )$ with $G ( q ) = g ^ { \prime } ( q )$ and letthe manifold $\mathcal { M }$ begivenby(1.43).1f(1.13)holdsandif

$$
G ( q ) H _ { p } ^ { [ i ] } ( p , q ) = 0 \qquad f o r a l l \ ( p , q ) \in \mathcal { M } ,
$$

thenthesystem

$$
\begin{array} { l } { \dot { q } \ = \ H _ { p } ^ { [ i ] } ( p , q ) } \\ { \dot { p } \ = \ - H _ { q } ^ { [ i ] } ( p , q ) - G ( q ) ^ { T } \lambda } \\ { 0 \ = \ G ( q ) H _ { p } ( p , q ) } \end{array}
$$

definesadifferential equationonthemanifold $\mathcal { M }$ ,anditsflowisasymplectic transformationon $\mathcal { M }$

Proof.Differentiation of the algebraic relation in(1.45）with respect to time,and replacing $\dot { q }$ and $\dot { p }$ with their differential equations,yields an explicit relation for $\lambda = \lambda ( p , q )$ (asaconsequence of(1.13)).Hence,a unique solution of(1.45) exists locally if $G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) = 0 .$ Theassumption(1.44) implies $\begin{array} { r } { \frac { d } { d t } g \bigl ( q ( t ) \bigr ) = 0 . } \end{array}$ This togetherwith thealgebraicrelation of（1.45）guarantees that for $( p _ { 0 } , q _ { 0 } ) \in \mathcal { M }$ the solution stays on the manifold $\mathcal { M }$ Thesymplecticity of the flow isproved as for Theorem 1.2. □

Suppose now that the Hamiltonian $H ( p , q )$ of(1.9)can be split as in (1.42), where both $H ^ { [ i ] } ( p , q )$ satisfy(1.44).Wedenoteby $\varphi _ { t } ^ { [ i ] }$ the flow ofthe system(1.45). IftheseflowscaneomputedalyticayteLieoteltig $\varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h } ^ { [ 1 ] }$ and the Strang splittingh/2 $\varphi _ { h / 2 } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h / 2 } ^ { [ 1 ] }$ /2yield first and second order numerical integrators,respectively.Considering more general compositionsas in(I.5.6)and using thecoefficients proposed in Sect.V.3,methods of high orderareobtained.They give numerical approximationslying on the manifold $\mathcal { M }$ ,andtheyaresymplectic(also symmetric if the splitting iswell chosen).

For the important special case where

$$
H ( p , q ) = T ( p , q ) + U ( q )
$$

isthe sum of the kinetic and potential energies,both summands satisfy assumption (1.44).This givesa natural splitting that is often used in practice.

Example1.6 (Spherical Pendulum).We normalizeall constants to1(cf.Example1.1）and we consider the problem(1.9)with

$$
H ( p , q ) = { \textstyle \frac { 1 } { 2 } } \big ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } + p _ { 3 } ^ { 2 } \big ) + q _ { 3 } , \qquad g ( q ) = { \textstyle \frac { 1 } { 2 } } \big ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } - 1 \big ) .
$$

We split the Hamiltonianas $H ^ { [ 1 ] } ( p , q ) = { \textstyle \frac { 1 } { 2 } } \big ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } + p _ { 3 } ^ { 2 } \big )$ and $H ^ { [ 2 ] } ( p , q ) = q _ { 3 } ,$ and we solve（1.45）with initial values on the manifold

$$
\mathcal { M } = \{ ( p , q ) | q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } - 1 = 0 , p _ { 1 } q _ { 1 } + p _ { 2 } q _ { 2 } + p _ { 3 } q _ { 3 } = 0 \} .
$$

The kinetic energy $H ^ { [ 1 ] } ( p , q )$ leads to the system

$$
\dot { \boldsymbol { q } } = \boldsymbol { p } , \qquad \dot { \boldsymbol { p } } = - \boldsymbol { q } \lambda , \qquad \boldsymbol { q } ^ { T } \boldsymbol { p } = 0 ,
$$

which gives $\lambda = p _ { 0 } ^ { T } p _ { 0 }$ ,so that the flow $\varphi _ { t } ^ { [ 1 ] }$ is just aplanar rotationaround the origin.The potential energy $H ^ { [ 2 ] } ( p , q )$ leadsto

$$
\dot { q } = 0 , \qquad \dot { p } = - ( 0 , 0 , 1 ) ^ { T } = q \lambda , \qquad q ^ { T } p = 0 .
$$

The flow keeps $q ( t )$ constant and changes $p ( t )$ linearlywith time.Spliting methodsgive simple,explicit and symplectic time integrators for this problem.

# VII.2 Poisson Systems

Thissection is devoted to an interesting generalization of Hamiltonian systems, where $J ^ { - 1 }$ in(VI.2.5）isreplaced withanonconstant matrix $B ( y )$ Such structureswereintroduced by SophusLie(1888)and are today called Poisson systems. Theyresult,in particular,from Hamiltonian systems on manifolds written in noncanonical coordinates.Ina first subsection,however,we discuss the Poisson structure of Hamiltonian systemsin canonical form.

# VII.2.1 Canonical Poisson Structure

quelques remarques sur la plus profonde decouverte de M.Poisson, maisqui,jecrois,n'a pas éte biencomprise ni parLagrange,ni par les nombreux géometresqui l'ont citee,ni par son auteur lui-méme.

(C.G.J.Jacobi 1840,p.350)

Thederivative ofa function $F ( p , q )$ along theflowofa Hamiltonian system

$$
\dot { p } = - \frac { \partial H } { \partial q } ( p , q ) , \qquad \dot { q } = \frac { \partial H } { \partial p } ( p , q ) ,
$$

is givenby(Liederivative,see (III.5.3))

$$
{ \frac { d } { d t } } F { \big ( } p ( t ) , q ( t ) { \big ) } = \sum _ { i = 1 } ^ { d } { \Big ( } { \frac { \partial F } { \partial p _ { i } } } { \dot { p } } _ { i } + { \frac { \partial F } { \partial q _ { i } } } { \dot { q } } _ { i } { \Big ) } = \sum _ { i = 1 } ^ { d } { \Big ( } { \frac { \partial F } { \partial q _ { i } } } { \frac { \partial H } { \partial p _ { i } } } - { \frac { \partial F } { \partial p _ { i } } } { \frac { \partial H } { \partial q _ { i } } } { \Big ) } .
$$

Thisremarkably symmetric structure motivates the following definition.

Definition2.1.The (canonical) Poisson bracket of two smooth functions $F ( p , q )$ and $G ( p , q )$ is the function

$$
\{ F , G \} = \sum _ { i = 1 } ^ { d } \Bigl ( \frac { \partial F } { \partial q _ { i } } \frac { \partial G } { \partial p _ { i } } - \frac { \partial F } { \partial p _ { i } } \frac { \partial G } { \partial q _ { i } } \Bigr ) ,
$$

or in vector notation $\{ F , G \} ( y ) = \nabla F ( y ) ^ { T } J ^ { - 1 } \nabla G ( y )$ ,where $y = ( p , q )$ and $\boldsymbol { J }$ is the matrix of(VI.2.3).

ThisPoisson bracket is bilinear,skew-symmetric $\{ F , G \} = - \{ G , F \}$ it satisfiestheJacobiidentity(Jacobi1862,Werke5,p.46)

$$
\{ \{ F , G \} , H \} + \{ \{ G , H \} , F \} + \{ \{ H , F \} , G \} = 0
$$

(notice the cyclic permutations among $F , G , H )$ ,andLeibniz'rule

$$
\{ F \cdot G , H \} = F \cdot \{ G , H \} + G \cdot \{ F , H \} .
$$

These formulas are obtained ina straightforward manner from standard rules of calculus (see also Exercise 1).

With this notation,the Lie derivative (2.2) becomes

$$
{ \frac { d } { d t } } F { \big ( } y ( t ) { \big ) } = \{ F , H \} ( y ( t ) ) .
$$

It follows that a function $I ( p , q )$ isafirst integral of(2.1) ifand only if

$$
\{ I , H \} = 0 .
$$

If we take $F ( y ) = y _ { i }$ themapping that selects the $i$ thcomponent of $y$ ,wesee that theHamiltonian system (2.1) or(V1.2.5), $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) } \end{array}$ ,can bewritten as

$$
\dot { y } _ { i } = \{ y _ { i } , H \} , \quad \dot { \ i } = 1 , \ldots , 2 d .
$$

Poisson's DiscoveryAt the beginning of the19th centurythe hope of beingableto integrate a given system of differential equationsby analytic formulas faded moreand more,and the energy of researchers went to the construction of,at least,first integrals.In this enthusiasm,Jacobi declared the subsequent result to be“Poisson's deepest discovery”(see citation) and his own identity,developed for its proof,a"gravissimum Theorema”.

Theorem 2.2 (Poisson 1809).1f $I _ { 1 }$ and $I _ { 2 }$ arefirst integrals,thentheir Poisson bracket $\{ I _ { 1 } , I _ { 2 } \}$ is againafirst integral.

Proof. This follows at once from the Jacobi identitywith $F ^ { \prime } = I _ { 1 }$ and $G = I _ { 2 }$ □

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0004_pages_0211-0280/auto/images/830f3acc6dc106abd777b43bc018013b142fb3d9be7c1980054416539b0cf72d.jpg)  
Simeon Denis Poisson

# VII.2.2 General Poisson Structures

...the general concept ofa Poisson manifold should be credited to SophusLie in his treatise on transformation groups... (J.E.Marsden&T.S.Ratiu1999)

Wenow come to the announced generalization of Definition 2.1 of the canonical Poisson bracket,invented byLie(1888).Indeed,many proofs of properties ofHamiltonian systemsrely uniquely on the bilinearity,the skew-symmetry and theJacobi identity of the Poisson bracket,but not on the special structure of (2.3).So theidea is,more generally,tostartwith a smooth matrix-valued function $B ( y ) = \left( b _ { i j } ( y ) \right)$ and to set

$$
\left\{ F , G \right\} ( y ) = \sum _ { i , j = 1 } ^ { n } { \frac { \partial F ( y ) } { \partial y _ { i } } } b _ { i j } ( y ) { \frac { \partial G ( y ) } { \partial y _ { j } } }
$$

(or more compactly $\{ F , G \} ( y ) = \nabla F ( y ) ^ { T } B ( y ) \nabla G ( y ) ) .$

Lemma2.3.Thebracketdefinedin(2.8)is bilinear,skew-symmetricandsatisfies Leibniz'rule(2.5)aswellastheJacobiidentity(2.4)ifand onlyif

$$
b _ { i j } ( y ) = - b _ { j i } ( y ) \qquad f o r \ : a l l \ : i , j
$$

andforall $i , j , k$ (notice the cyclic permutations among $i , j , k )$

$$
\sum _ { l = 1 } ^ { n } \Bigl ( { \frac { \partial b _ { i j } ( y ) } { \partial y _ { l } } } b _ { l k } ( y ) + { \frac { \partial b _ { j k } ( y ) } { \partial y _ { l } } } b _ { l i } ( y ) + { \frac { \partial b _ { k i } ( y ) } { \partial y _ { l } } } b _ { l j } ( y ) \Bigr ) = 0 .
$$

Proof.Themain observationisthat condition(2.1O)is the Jacobi identity for the special choice of functions $F = y _ { i }$ ， $G = y _ { j }$ ， $H = y _ { k }$ because of

$$
\{ y _ { i } , y _ { j } \} = b _ { i j } ( y ) .
$$

If equation(2.4）is developed for the bracket (2.8),one obtains terms containing second orderpartial derivatives-these cancel due to the symmetry of the Jacobi identity-and terms containing first order partial derivatives;for the latterwe may assume $F , G , H$ to be linear combinations of $y _ { i }$ ， $y _ { j }$ ， $y _ { k }$ ,so we are back to (2.10). Thedetails of this proof are left as an exercise(see Exercise1).

Definition 2.4.If thematrix $B ( y )$ satisfiestheproperties ofLemma2.3,formula (2.8)issaid to represent a(general) Poisson bracket.The correspondingdifferential system

$$
\dot { y } = B ( y ) \nabla H ( y ) ,
$$

isaPoisson system.We continue to call $H$ aHamiltonian,

Thesystem(2.12） can again bewrittenin the bracket formulation(2.7).The formula(2.6)fortheLiederivativeremainsalsovalid,asisseen immediatelyfrom thechain rule and the definition of the Poisson bracket.Choosing $F = H$ this showsin particular that the Hamiltonian $H$ isafirst integral for general Poisson systems.

Definition2.5.Afunction $C ( y )$ is calleda Casimirfunction of the Poissonsystem (2.12）,if

$$
\nabla C ( y ) ^ { T } B ( y ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } y .
$$

ACasimir functionisafirst integral of every Poisson system with structure matrix $B ( y )$ ,whatever the Hamiltonian $H ( y )$ is.

Example2.6.TheLotka-Volterra equations of Sect.I.1.1canbewriten as

$$
\binom { \dot { u } } { \dot { v } } = \binom { 0 } { - u v } \stackrel { u v } { 0 } \nabla H ( u , v ) ,
$$

where $H ( u , v ) = u - \ln u + v - 2 \ln v$ isthe invariant (I.1.4).This is of the form (2.12)with a matrix that is skew-symmetric and satisfies the identity (2.10).

Higher dimensional Lotka-Volterra systems can also havea Poisson structure (see,e.g.,Perelomov(1995)and Suris(1999)).For example,thesystem

$$
\dot { y } _ { 1 } = y _ { 1 } ( y _ { 2 } + y _ { 3 } ) , \quad \dot { y } _ { 2 } = y _ { 2 } ( y _ { 1 } - y _ { 3 } + 1 ) , \quad \dot { y } _ { 3 } = y _ { 3 } ( y _ { 1 } + y _ { 2 } + 1 )
$$

can be written as

$$
\left( \begin{array} { c } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) = \left( \begin{array} { c c c } { 0 } & { y _ { 1 } y _ { 2 } } & { y _ { 1 } y _ { 3 } } \\ { - y _ { 1 } y _ { 2 } } & { 0 } & { - y _ { 2 } y _ { 3 } } \\ { - y _ { 1 } y _ { 3 } } & { y _ { 2 } y _ { 3 } } & { 0 } \end{array} \right) \nabla H ( y )
$$

with $H ( y ) = - y _ { 1 } + y _ { 2 } + y _ { 3 } + \ln y _ { 2 } - \ln y _ { 3 } .$ Again onecan check by direct computation that（2.10) is satisfied.

In contrast to the structure matrix $J ^ { - 1 }$ ofHamiltonian systems in canonical form,the matrix $B ( y )$ of(2.12）need not be invertible.All odd-dimensional skewsymmetric matrices are singular,and sois the matrix $B ( y )$ of(2.14).In this case, thevector $v ( y ) = ( - 1 / y _ { 1 } , - 1 / y _ { 2 } , 1 / y _ { 3 } ) ^ { T }$ satisfies $v ( y ) ^ { \boldsymbol { \imath } } B ( y ) = 0 .$ Since $v ( y ) =$ $\nabla C ( y )$ with $C ( y ) = - \ln y _ { 1 } - \ln y _ { 2 } + \ln y _ { 3 }$ thefunction $C ( y )$ isaCasimir function.

# VII.2.3 Hamiltonian Systems on Symplectic Submanifolds

Animportant motivation for studying Poisson systemsis given by Hamiltonian problems expressed in non-canonical coordinates.

Example 2.7 (Constrained Mechanical Systems). Consider the system（1.9 writtenas thedifferential equation

$$
\dot { x } = J ^ { - 1 } \Big ( \nabla H ( x ) + \sum _ { i = 1 } ^ { m } \lambda _ { i } ( x ) \nabla g _ { i } ( x ) \Big )
$$

on themanifold $\mathcal { M } = \{ x ; c ( x ) = 0 \}$ with $\boldsymbol { c } ( \boldsymbol { x } ) = \bigl ( g ( \boldsymbol { q } ) , G ( \boldsymbol { q } ) H _ { p } ( p , \boldsymbol { q } ) \bigr ) ^ { \perp }$ and $x = ( p , q ) ^ { T }$ (see(1.14)).As in the proof of Theorem 1.2, $\lambda _ { i } ( x )$ and $g _ { i } ( x )$ arethe components of $\lambda ( x )$ and $g ( x )$ ,and $\lambda ( x )$ isthe function obtained from(1.12).We use $y \in \mathbb { R } ^ { 2 ( d - m ) }$ aslocal coordinates of themanifold $\mathcal { M }$ via the transformation

$$
x = \chi ( y ) .
$$

Inthese coordinates,the differential equation (2.15)becomes,with $X ( y ) = \chi ^ { \prime } ( y )$ ,

$$
X ( y ) \dot { y } = J ^ { - 1 } \Big ( \nabla H \big ( \chi ( y ) \big ) + \sum _ { i = 1 } ^ { m } \lambda _ { i } \big ( \chi ( y ) \big ) \nabla g _ { i } \big ( \chi ( y ) \big ) \Big ) .
$$

Wemultiply this equation from the leftwith $X ( y ) ^ { T } J$ and note that the columns of $X ( y )$ ,which are tangent vectors,are orthogonal tothe gradients $\nabla g _ { i }$ of the constraints.Thisyields

$$
X ( y ) ^ { T } J X ( y ) \dot { y } = X ( y ) ^ { T } \nabla H \big ( \chi ( y ) \big ) .
$$

Byassumption(1.13)the matrix $X ( y ) ^ { T } J X ( y )$ is invertible.This is seenas follows: $X ( y ) ^ { \mathit { 1 } } J X ( y ) v \ = \ 0$ implies $J X ( y ) v \ = \ c ^ { \prime } ( x ) ^ { I } w$ forsome $w$ （ $x \ = \ x ( y ) )$ .By $c ( x ( y ) ) = 0$ and $c ^ { \prime } ( x ) X ( y ) = 0$ weget $c ^ { \prime } ( x ) J ^ { - 1 } c ^ { \prime } ( x ) ^ { I } w = 0$ It then follows from the structure of $c ^ { \prime } ( x )$ and from（1.13） that $w = 0$ and hence also $v = 0$ .

With $B ( y ) = \left( X ( y ) ^ { T } J X ( y ) \right) ^ { - 1 }$ and $K ( y ) = H ( \chi ( y ) )$ ,the above equation for $\dot { y }$ thus becomes the Poisson system $\begin{array} { r } { \dot { y } = B ( y ) \nabla K ( y ) . } \end{array}$ Thematrix $B ( y )$ isskewsymmetricand satisfies(2.1O),see Theorem 2.8 below orExercise11.

Moregenerally,considera symplectic submanifold $\mathcal { M }$ of $\mathbb { R } ^ { 2 d }$ ,thatis,amanifold forwhich the symplectic two-form²

$$
\omega _ { x } ( \xi _ { 1 } , \xi _ { 2 } ) = ( J \xi _ { 1 } , \xi _ { 2 } ) \qquad \mathrm { f o r } \quad \xi _ { 1 } , \xi _ { 2 } \in T _ { x } \mathcal { M }
$$

(with $( \cdot , \cdot )$ denoting the Euclideaninnerproducton $\mathbb { R } ^ { 2 d }$ )isnon-degenerateforevery $x \in \mathcal { M } :$ for $\xi _ { 1 }$ in the tangent space $\mathbf { \xi } _ { T } \mathbf { \mathcal { M } }$ ,

$$
\omega _ { x } ( \xi _ { 1 } , \xi _ { 2 } ) = 0 \mathrm { f o r \ a l l } \xi _ { 2 } \in T _ { x } { \cal M } \mathrm { i m p l i e s } \xi _ { 1 } = 0 .
$$

In local coordinates $x = \chi ( y )$ ,thiscondition is equivalent to the invertibility of thematrix $X ( y ) ^ { \prime \prime } J X ( y )$ with $X ( y ) = \chi ^ { \prime } ( y )$ ,sinceevery tangent vector at $x =$ $\chi ( y )$ is of theform $\xi = X ( y ) \eta$ and $X ( y )$ has linearly independent columns.A manifold defined by constraints, $\mathcal { M } = \{ x \in \mathbb { R } ^ { 2 d } | c ( x ) = 0 \}$ issymplectic if the matrix $c ^ { \prime } ( x ) J ^ { - 1 } c ^ { \prime } ( x ) ^ { 1 }$ isinvertible for every $x \in \mathcal { M }$ (see the argument at the end ofthe previous example).This condition can be restated as saying that the matrix $\left( \{ c _ { i } , c _ { j } \} ( x ) \right)$ of canonical Poisson brackets of the constraint functions is invertible.

We consider the reduction of the Hamiltonian system to the symplectic submanifold $\mathcal { M }$ ,which determines solution curves $t \mapsto x ( t ) \in \mathcal { M }$ by the equations

$$
\bigl ( J \dot { x } - \nabla H ( x ) , \xi \bigr ) = 0 \qquad \mathrm { f o r ~ a l l ~ } \xi \in T _ { x } \mathcal { M } .
$$

With the interpretation $\begin{array} { r } { ( \nabla H ( x ) , \xi ) = H ^ { \prime } ( x ) \xi = \left. \frac { d } { d t } \right| _ { t = 0 } H ( \gamma ( t ) ) } \end{array}$ asadirectional derivative alongapath $\gamma ( t ) \in \mathcal { M }$ with $\gamma ( 0 ) = x$ and ${ \dot { \gamma } } ( 0 ) = \xi$ ,itissufficient that the Hamiltonian $H$ isdefined and differentiable on the manifold $\mathcal { M }$ Equation (2.17)can also be expressed as

$$
\omega _ { x } ( \dot { x } , \xi ) = H ^ { \prime } ( x ) \xi \qquad \mathrm { f o r \ a l l ~ } \xi \in T _ { x } \mathcal { M } ,
$$

aformulation thatis susceptible to further generalization;cf.Marsden&Ratiu (1999),Chap.5.4,and Exercise 2.Choosing $\xi \ = \dot { x }$ we obtain $0 = H ^ { \prime } ( x ) { \dot { x } } =$ $\textstyle { \frac { d } { d t } } H ( x ( t ) )$ and hencethe Hamiltonianisconservedalong solutions.

Notethat for $\mathcal { M }$ ofExample2.7,the formulation(2.17）isequivalent to the equations of motion(2.15) of the constrained mechanical system.It corresponds to d'Alembert'sprinciple ofvirtual variations in constrained mechanics;see Arnold (1989),p.92.In quantum mechanics the Hamiltonian reduction (2.17) toa manifold(in that case,a submanifold of theHilbert space $L ^ { 2 } ( \mathbb { R } ^ { N } , \mathbb { R } ^ { 2 } )$ instead of $\mathbb { R } ^ { 2 d }$ ) isknownasthe Dirac-Frenkel time-dependentvariational principleandis thebasictool for deriving reduced models of the many-body Schrodinger equation;see Sect.VII.6 foran example.Fromanumerical analysis viewpoint,(2.17)can also be viewed as a Galerkin method on the solution-dependent tangent space $T _ { x } { \mathcal { M } } .$

In terms of the symplectic projection $P ( x ) : \mathbb { R } ^ { 2 d } \longrightarrow T _ { x } { \mathcal { M } }$ for $x \in \mathcal { M }$ ,defined bydetermining $P ( x ) v \in T _ { x } { \mathcal { M } }$ for $v \in \mathbb { R } ^ { 2 d }$ from the condition

$$
\begin{array} { r } { ( J P ( x ) v , \xi ) = ( J v , \xi ) \qquad \mathrm { ~ f o r ~ a l l ~ } \quad \xi \in T _ { x } \mathcal { M } , } \end{array}
$$

formula(2.17)can bereformulatedas the differential equation on $\mathcal { M }$ ,

$$
\begin{array} { r } { \dot { x } = P ( x ) J ^ { - 1 } \nabla H ( x ) . } \end{array}
$$

In coordinates $x = \chi ( y )$ ,and again with $X ( y ) = \chi ^ { \prime } ( y )$ ,formula (2.17) becomes

$$
X ( y ) ^ { T } \Big ( J X ( y ) \dot { y } - \nabla H ( \chi ( y ) ) \Big ) = 0 ,
$$

and with

$$
B ( \boldsymbol { y } ) = \left( \boldsymbol { X } ( \boldsymbol { y } ) ^ { T } \mathcal { I } \boldsymbol { X } ( \boldsymbol { y } ) \right) ^ { - 1 } \qquad \mathrm { a n d } \qquad \boldsymbol { K } ( \boldsymbol { y } ) = \boldsymbol { H } ( \boldsymbol { \chi } ( \boldsymbol { y } ) ) ,
$$

we obtain the differential equation

$$
\begin{array} { r } { \dot { y } = B ( y ) \nabla K ( y ) . } \end{array}
$$

Theorem2.8.Fora Hamiltoniansystem(2.17)ona symplectic submanifold $\mathcal { M }$ , theequivalent diffrential equation in local coordinates,(2.22) with(2.21),isa Poissonsystem.

Proof. In coordinates,the symplectic projection is given by

$$
\begin{array} { r } { P ( x ) = X ( y ) B ( y ) X ( y ) ^ { T } \mathcal { J } \qquad \mathrm { f o r } \quad x = \chi ( y ) \in \mathcal { M } , } \end{array}
$$

since for every tangent vector $\xi = X ( y ) \eta$ we have by (2.21),

$$
( J X B X ^ { T } J v , X \eta ) = ( X ^ { T } J X B X ^ { T } J v , \eta ) = ( X ^ { T } J v , \eta ) = ( J v , X \eta ) .
$$

Fromthe decomposition $\mathbb { R } ^ { 2 d } = P ( x ) \mathbb { R } ^ { 2 d } \oplus ( I - P ( x ) ) \mathbb { R } ^ { 2 d }$ we obtain,bytheimplicit function theorem,acorresponding spliting inaneighbourhoodof themanifold $\mathcal { M }$ in $\mathbb { R } ^ { 2 d }$ ,

$$
v = x + w \quad \mathrm { w i t h } x \in \mathcal { M } , P ( x ) w = 0 .
$$

This permitsus to extend smooth functions $F ( y )$ toa neighbourhood of $\mathcal { M }$ by setting

$$
{ \widehat { F } } ( v ) = F ( y ) \quad { \mathrm { ~ f o r ~ } } v = x + w \ { \mathrm { ~ w i t h ~ } } x = \chi ( y ) , \ P ( x ) w = 0 .
$$

Wethen havefor the derivative $\widehat { F } ^ { \prime } ( x ) = \widehat { F } ^ { \prime } ( x ) P ( x )$ for $x \in \mathcal { M }$ and hence for its transpose,the gradient, $\nabla \widehat F ( x ) = P ( x ) ^ { T } \nabla \widehat F ( x ) .$ Moreover,by the chain rule we have $\nabla F ( y ) = X ( y ) ^ { T } \nabla F ( x )$ for $x = \chi ( y )$ Forthecanonical bracketthis gives, at $x = \chi ( y )$ ，

$$
\begin{array} { r c l } { { \{ \widehat { F } , \widehat { G } \} _ { \mathrm { c a n } } ( x ) } } & { { = } } & { { \nabla \widehat { F } ( x ) ^ { T } P ( x ) J ^ { - 1 } P ( x ) ^ { T } \nabla \widehat { G } ( x ) } } \\ { { } } & { { = } } & { { \nabla F ( y ) ^ { T } B ( y ) \nabla G ( y ) = \{ F , G \} ( y ) , } } \end{array}
$$

and hence the required properties of the bracket defined by $B ( y )$ follow from the corresponding properties of the canonical bracket. □

# VII.3The Darboux-Lie Theorem

Theorem 2.8 also shows that a Hamiltonian system without constraints becomes a Poisson system in non-canonical coordinates.Interestingly,a converse also holds: everyPoisson system can locally be written in canonical Hamiltonian form after asuitable change ofcoordinates.Thisresult isa special case of theDarboux-Lie Theorem.Itsproofwas the result of several important papers:Jacobi'stheory of simultaneous linear partial differential equations(Jacobi 1862),theworks by Clebsch(1866)and Darboux (1882） on Pfaffian systems,and,finally,thepaper ofLie (1888).We shall now retrace this development.Our first tool is a result on the commutativity of Poisson flows.

# VII.3.1 Commutativity of Poisson Flows and Lie Brackets

Theelegant formula(2.6) for theLiederivative is valid for general Poisson systems with the vector field $f ( y ) = B ( y ) \nabla H ( y )$ of(2.12).Acting on a function $F : \mathbb { R } ^ { n } $ $\mathbb { R }$ ,theLieoperator(III.5.2)becomes

$$
{ D F } = \nabla F ^ { T } f = \nabla F ^ { T } B ( y ) \nabla H = \{ F , H \}
$$

andisagainthePoisson bracket.Thisobservationisthekey forthefollowing lemma,which shows an interesting connection between the Lie bracket and the Poisson bracket.

Lemma3.1.Let twosmoothHamiltonians $H ^ { \left[ 1 \right] } ( y )$ and $H ^ { [ 2 ] } ( y )$ be given.

$$
\begin{array} { r } { \begin{array} { c c l } { { { \it I f } } } & { { D _ { 1 } } } & { { i s ~ t h e ~ L i e ~ o p e r a t o r ~ o f } } \\ { { a n d } } & { { D _ { 2 } } } & { { i s ~ t h e ~ L i e ~ o p e r a t o r ~ o f } } \\ { { t h e n } } & { { [ D _ { 1 } , D _ { 2 } ] } } & { { i s ~ t h e ~ L i e ~ o p e r a t o r ~ o f } } \end{array} \begin{array} { r } { { B ( y ) \nabla H ^ { [ 1 ] } } } \\ { { B ( y ) \nabla H ^ { [ 2 ] } , } } \end{array} } \end{array}
$$

(notice,onceagain,that the indicesland2 havebeenreversed).

Proof.After some clever permutations,the Jacobi identity(2.4)can be written as

$$
\left\{ \{ F , H ^ { [ 2 ] } \} , H ^ { [ 1 ] } \right\} - \left\{ \{ F , H ^ { [ 1 ] } \} , H ^ { [ 2 ] } \right\} = \left\{ F , \{ H ^ { [ 2 ] } , H ^ { [ 1 ] } \} \right\} .
$$

By(3.1)this is nothing other than $D _ { 1 } D _ { 2 } F _ { \mathrm { ~ - ~ } } D _ { 2 } D _ { 1 } F = [ D _ { 1 } , D _ { 2 } ] F .$

Lemma3.2.Considertwo smooth Hamiltonians $H ^ { [ 1 ] } ( y )$ and $H ^ { \left[ 2 \right] } ( y )$ onan open connected set $U$ ,with $D _ { 1 }$ and $D _ { 2 }$ the corresponding Lie operators and $\varphi _ { s } ^ { [ 1 ] } ( y )$ and $\varphi _ { t } ^ { [ 2 ] } ( y )$ thecorrespondingflows.Then,ifthematrix $B ( y )$ isinvertible,thefollowing areequivalentin $U$ :

$$
\begin{array} { r l } { ( i ) } & { \{ H ^ { [ 1 ] } , H ^ { [ 2 ] } \} = C o n s t ; } \\ { ( i i ) } & { [ D _ { 1 } , D _ { 2 } ] = 0 ; } \\ { ( i i i ) } & { \varphi _ { t } ^ { [ 2 ] } \circ \varphi _ { s } ^ { [ 1 ] } = \varphi _ { s } ^ { [ 1 ] } \circ \varphi _ { t } ^ { [ 2 ] } . } \end{array}
$$

Theconclusions ${ } ^ { * } ( i ) \Rightarrow ( i i ) \Leftrightarrow ( i i i )$ "alsoholdforanon-invertible $B ( y )$


<!-- chunk 0005: pages 281-350 -->
Proof.ThisisobtainedbycombiningLemma II.5.4andLemma3.1.We need theinvertibilityof $B ( y )$ to conclude that $\{ H ^ { [ 1 ] } , H ^ { [ 2 ] } \} ~ = ~ C o n s t$ followsfrom $B ( y ) \nabla \{ H ^ { [ 1 ] } , H ^ { [ 2 ] } \} = 0$ □

# VII.3.2 Simultaneous Linear Partial Differential Equations

If two functions $F ( y )$ and $G ( y )$ aregiven,formula(2.8）determines a function $h ( y ) = \{ F , G \} ( y )$ bydifferentiation.We now ask the inversequestion:Given functions $G ( y )$ and $h ( y )$ canwefinda function $F ( y )$ such that $\{ F , G \} ( y ) = h ( y ) ?$ Thisproblem representsa first order linearpartial differential equation for $F _ { \cdot }$ Sowe are led to the following problem,which we first discuss in two dimensions.

One Equation. Given functions $a ( y _ { 1 } , y _ { 2 } )$ $b ( y _ { 1 } , y _ { 2 } )$ , $h ( y _ { 1 } , y _ { 2 } )$ ,find all solutions $F ( y _ { 1 } , y _ { 2 } )$ satisfying

$$
a ( y _ { 1 } , y _ { 2 } ) \frac { \partial F } { \partial y _ { 1 } } + b ( y _ { 1 } , y _ { 2 } ) \frac { \partial F } { \partial y _ { 2 } } = h ( y _ { 1 } , y _ { 2 } ) .
$$

This equation is,for any point $( y _ { 1 } , y _ { 2 } )$ ,a linear relation between thepartial deriyatives of $F ^ { ' }$ ,butdoes not determine them individually.Thereis one direction, however,where thederivative isuniquely determined,namely that of thevector $\boldsymbol { n } = \left( a ( y _ { 1 } , y _ { 2 } ) , b ( y _ { 1 } , y _ { 2 } ) \right)$ ,since the left-hand side of equation(3.4)is thedirectionalderivative ${ \frac { \partial F } { \partial n } } .$ Tlis characteristic lines(see left picture of Fig.3.1).Ifwe parametrize them withaparameter $t$ ,we can compute $y _ { 1 } ( t )$ , $y _ { 2 } ( t )$ aswell as $F ( t ) = F \big ( y _ { 1 } ( t ) , y _ { 2 } ( t ) \big )$ as solutions of the following ordinary differential equations

$$
\dot { y } _ { 1 } = a ( y _ { 1 } , y _ { 2 } ) , \qquad \dot { y } _ { 2 } = b ( y _ { 1 } , y _ { 2 } ) , \qquad \dot { F } = h ( y _ { 1 } , y _ { 2 } ) .
$$

The initial values ${ ( y _ { 1 } ( 0 ) , y _ { 2 } ( 0 ) ) }$ can be chosen on an arbitrary curve $\gamma$ (which must betransversal to the characteristic lines)and the values $F | _ { \gamma }$ can be arbitrarily prescribed.The solution $F ( y _ { 1 } , y _ { 2 } )$ of(3.4)is then created by thecurves(3.5）wherever thecharacteristic lines go (right picture ofFig.3.1).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/75e7ebaf5abe3cfac3cc79887e003b1ad7b3ca71110065bd5aee710fe10c630a.jpg)  
Fig.3.1.Characteristic lines and solution ofa first order linear partial differential equation

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/664d757df2dad7557e2c5017d6f3ce2b054e56b44af2a05b83ce78edfd4e55ce.jpg)  
Fig.3.2.Characteristic surfaces of two first order linear partial differential equations

For one equation in $n$ dimensions,the initial values $\left( y _ { 1 } ( 0 ) , \ldots , y _ { n } ( 0 ) \right)$ canbe freelychosen onamanifold of dimension $n - 1$ (e.g.,the subspace orthogonal to the characteristic line passing through a given point),and $F ^ { \prime }$ can bearbitrarilyprescribed onthis manifold.This guarantees the existence of $n - 1$ independent solutions in theneighbourhood of a given point.Here,independent means that the gradients of these functions are linearly independent.

Two Simultaneous Equations. Two simultaneous equations of dimension two are trivial.We therefore suppose $y = ( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ and two equations of the form

$$
\begin{array} { r l } & { a _ { 1 } ^ { [ 1 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 1 } } + a _ { 2 } ^ { [ 1 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 2 } } + a _ { 3 } ^ { [ 1 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 3 } } = h _ { 1 } ( y ) , } \\ & { a _ { 1 } ^ { [ 2 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 1 } } + a _ { 2 } ^ { [ 2 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 2 } } + a _ { 3 } ^ { [ 2 ] } ( y ) \displaystyle \frac { \partial F } { \partial y _ { 3 } } = h _ { 2 } ( y ) } \end{array}
$$

foran unknown function $F ( y _ { 1 } , y _ { 2 } , y _ { 3 } )$ Thissystem can also be written as $D _ { 1 } F =$ $h _ { 1 } , D _ { 2 } F ^ { \prime } = h _ { 2 }$ ,where $D _ { i }$ denotes the Lie operator corresponding to the vector field $a ^ { [ i ] } ( y )$ Here,we havetwodirectional derivatives prescribed,namely $\frac { \partial F } { \partial n _ { 1 } }$ and $\frac { \partial F } { \partial n _ { 2 } }$ where $n _ { i } = a ^ { [ i ] } ( y )$ (seeFig.3.2).Therefore,we will have to follow both directions and,insteadof(3.5),wewill have two sets of ordinary differential equations

$$
\begin{array} { r l r l r l r l } & { \dot { y } _ { 1 } = a _ { 1 } ^ { [ 1 ] } ( y ) , } & & { \dot { y } _ { 2 } = a _ { 2 } ^ { [ 1 ] } ( y ) , } & & { \dot { y } _ { 3 } = a _ { 3 } ^ { [ 1 ] } ( y ) , } & & { \dot { F } = h _ { 1 } ( y ) } \\ & { \dot { y } _ { 1 } = a _ { 1 } ^ { [ 2 ] } ( y ) , } & & { \dot { y } _ { 2 } = a _ { 2 } ^ { [ 2 ] } ( y ) , } & & { \dot { y } _ { 3 } = a _ { 3 } ^ { [ 2 ] } ( y ) , } & & { \dot { F } = h _ { 2 } ( y ) . } \end{array}
$$

If we prescribe $F$ ona curve that is orthogonal to ${ \boldsymbol { n } } _ { 1 }$ and $_ { n 2 }$ ,and ifwe follow the solutions of(3.7）,we obtain the function $F$ ontwo 2-dimensional surfaces $S _ { 1 }$ and $S _ { 2 }$ containing the prescribed curve.Continuing from $S _ { 1 }$ along the second flow and from $S _ { 2 }$ along the firstflow,we may beledto the same point,but nothing guarantees that the obtained values for $F$ areidentical.To geta well-defined $F ^ { \prime }$ ,additional assumptions on the differential operators and on the inhomogeneities have to be made.

Thefollowing theorem,which is due to Jacobi (1862),hasbeen extended byClebsch (1866),who created the theory of completesystems("vollstandige

Systeme").These papers contained long analytic calculations with myriades of formulas.The wonderful geometric insight is mainly due to Sophus Lie.

Theorem 3.3.Let $\boldsymbol { D } _ { 1 } , \dots , \boldsymbol { D } _ { m }$ be $_ { m }$ $m < n$ lineardifferentialoperatorsin $\mathbb { R } ^ { n }$ correspondingto vectorfelds $a ^ { [ 1 ] } ( y ) , \ldots , a ^ { [ m ] } ( y )$ and suppose that these vectors arelinearly independent for $y = y _ { 0 } .$ 1f

$$
[ D _ { i } , D _ { j } ] = 0 \qquad f o r a l l i , j ,
$$

then the homogeneous system

$$
D _ { i } F = 0 \qquad f o r \ i = 1 , \ldots , m
$$

possesses(ina neighbourhood of $y _ { 0 }$ ） $n - m$ solutions for which the gradients $\nabla F ( y _ { 0 } )$ are linearly independent.

Furthermore,theinhomogeneoussystemofpartialdiffrentialequations

$$
D _ { i } F = h _ { i } \qquad f o r \ i = 1 , \dots , m
$$

possessesaparticular solution ina neighbourhood of $y _ { 0 }$ ，ifandonlyifinaddition to(3.8）the functions $h _ { 1 } ( y ) , \ldots , h _ { m } ( y )$ satisfytheintegrabilityconditions

$$
D _ { i } h _ { j } = D _ { j } h _ { i } \qquad f o r \mathop { a l l } i , j .
$$

Proof(a)Let $V$ denote the space of vectors in ${ \mathbb { R } } ^ { n }$ that are orthogonal to $a ^ { [ 1 ] } ( y _ { 0 } )$ ， $\cdots , a ^ { [ m ] } ( y _ { 0 } )$ ,and consider the $( n - m )$ -dimensional manifold $\mathcal { M } = y _ { 0 } + V .$ We then extend an arbitrary smooth function $F : \mathcal { M }  \mathbb { R }$ toaneighbourhood of $y _ { 0 }$ by

$$
F \Bigl ( \varphi _ { t _ { m } } ^ { [ m ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Bigr ) = F \bigl ( y _ { 0 } + v \bigr ) .
$$

Noticethat(t1，.,tm,U）→y= $( t _ { 1 } , \dots , t _ { m } , v ) \mapsto y = \varphi _ { t _ { m } } ^ { [ m ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v )$ defines alocaldiffeomorphism between neighbourhoods of $0$ and $y _ { 0 }$ Since the application of the operator $D _ { m }$ to(3.10)corresponds toadifferentiation with respect to and the expression $F \bigl ( \varphi _ { t _ { m } } ^ { [ m ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \bigr )$ is independent of $t _ { m }$ by (3.10), we get $D _ { m } F ( y ) = 0$ ToproveDFyfo<irsteoageteoho in(3.1) $\varphi _ { t _ { i } } ^ { [ i ] }$ is in the left-most position.

(b)The necessity of (3.9) followsimmediately from $D _ { i } h _ { j } ~ = ~ D _ { i } D _ { j } F ~ = ~ $ $D _ { j } D _ { i } F ^ { \prime } = D _ { j } h _ { i } .$ Forgiven $h _ { i }$ satisfying(3.9)we define $F ( y )$ ina neighbourhood of $y _ { 0 }$ (i.e.,for small $t _ { 1 } , \ldots , t _ { m }$ and small $\boldsymbol { v }$ )by

$$
\begin{array} { l } { \displaystyle F \Big ( \varphi _ { t _ { m } } ^ { [ m ] } \circ _ { \nu , \dots , 0 } \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) = \int _ { 0 } ^ { t _ { 1 } } h _ { 1 } \Big ( \varphi _ { t } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d t } \\ { \displaystyle \quad + \dots + \int _ { 0 } ^ { t _ { m } } h _ { m } \Big ( \varphi _ { t } ^ { [ m ] } \circ \varphi _ { t _ { m - 1 } } ^ { [ m - 1 ] } \circ _ { \nu , \dots } \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d t , } \end{array}
$$

andweprove that it isa solution of the system $D _ { i } F = h _ { i }$ for $i = 1 , \ldots , m .$ Since only the last integral depends on $t _ { m }$ ,weimmediatelygetbydifferentiationwith respect to $t _ { m }$ that $D _ { m } F = h _ { m }$ For the computation of $D _ { i } F$ wedifferentiate with it integral gives respect to $t _ { i }$ Thefirst $h _ { i } ( \varphi _ { t _ { i } } ^ { [ i ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) )$ $i - 1$ integrals are independent of anthederivatiefthein $t _ { i }$ .The derivative of the integralsgives

$$
\begin{array} { r l r } {  { ^ { \rho t _ { j } } D _ { i } h _ { j } \Big ( \varphi _ { t } ^ { [ j ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d t = \int _ { 0 } ^ { t _ { j } } D _ { j } h _ { i } \Big ( \varphi _ { t } ^ { [ j ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) d \tau } } \\ & { } & { = h _ { i } \Big ( \varphi _ { t _ { j } } ^ { [ j ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) - h _ { i } \Big ( \varphi _ { t _ { j - 1 } } ^ { [ j - 1 ] } \circ \dots \circ \varphi _ { t _ { 1 } } ^ { [ 1 ] } ( y _ { 0 } + v ) \Big ) } \end{array}
$$

for $j = i + 1 , \dots , m .$ Summing up,this proves $D _ { i } F = h _ { i } .$

# VII.3.3 Coordinate Changes and the Darboux-Lie Theorem

Theemphasis here is to simplifya given Poisson structure as much as possible by a coordinate transformation.We change from coordinates $y _ { 1 } , \ldots , y _ { n }$ to $\widetilde { y } _ { 1 } ( y ) , \dots , \widetilde { y } _ { n } ( y )$ with continuously differentiable functions andan invertible Jacobian $A ( y ) = \partial \widetilde { y } / \partial y ,$ , and we denote $\widetilde F ( \widetilde y ) : = F ( y )$ and $\widetilde G ( \widetilde y ) : =$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/fc653d630ace0da2aed89cf014b9c536fa8b4d828dd7c243f1fb277265cdfd4e.jpg)  
Fig.3.3.New coordinates ina Poisson system

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/2c4810bcf9efe411d690f095250efa9e46df05de5c66acdb54a42441e8b005cc.jpg)  
Jean Gaston Darboux

$G ( y )$ (seeFig.3.3).The Poisson structure aswell as the Poisson flow on one space willbecome another Poisson structure and flow on the other space by simply applying the chain rule:

$$
\sum _ { i , j } \frac { \partial F ( y ) } { \partial y _ { i } } b _ { i j } ( y ) \frac { \partial G ( y ) } { \partial y _ { j } } = \sum _ { i , j , k , l } \frac { \partial \widetilde { F } ( \widetilde { y } ) } { \partial \widetilde { y } _ { k } } \frac { \partial \widetilde { y } _ { k } } { \partial y _ { i } } b _ { i j } \big ( y ( \widetilde { y } ) \big ) \frac { \partial \widetilde { y } _ { l } } { \partial y _ { j } } \frac { \partial \widetilde { G } ( \widetilde { y } ) } { \partial \widetilde { y } _ { l } } .
$$

This is another Poisson structure with

$$
\widetilde { b } _ { k l } = \{ \widetilde { y } _ { k } , \widetilde { y } _ { l } \} \qquad \mathrm { o r } \qquad \widetilde { B } ( \widetilde { y } ) = A ( y ) B ( y ) A ( y ) ^ { T } .
$$

The same structure matrix is obtained if the Poisson system(2.12) is written in these newcoordinates (Exercise5).

Since $A$ isinvertible,the structure matrices $B$ and $\bar { B }$ have the same rank.We nowwant to obtain the simplest possible form for $\bar { B }$

Theorem3.4(Darboux 1882,Lie1888).Suppose that thematrix $B ( y )$ defines a Poisson bracket and is of constant rank $n - q \ = \ 2 m$ in $a$ neighbourhoodof $y _ { 0 } \in \mathbb { R } ^ { n } .$ Then,there exist functions $P _ { 1 } ( y ) , \dots , P _ { m } ( y )$ , $Q _ { 1 } ( y ) , \ldots , Q _ { m } ( y )$ ,and $C _ { 1 } ( y ) , \ldots , C _ { q } ( y )$ satisfying

$$
\begin{array} { l l l } { { \{ P _ { i } , P _ { j } \} = 0 } } & { { \{ P _ { i } , Q _ { j } \} = - \delta _ { i j } } } & { { \{ P _ { i } , C _ { l } \} = 0 } } \\ { { \{ Q _ { i } , P _ { j } \} = \delta _ { i j } } } & { { \{ Q _ { i } , Q _ { j } \} = 0 } } & { { \{ Q _ { i } , C _ { l } \} = 0 } } \\ { { \{ C _ { k } , P _ { j } \} = 0 } } & { { \{ C _ { k } , Q _ { j } \} = 0 } } & { { \{ C _ { k } , C _ { l } \} = 0 } } \end{array}
$$

onaneighbourhood of $y _ { 0 }$ The gradientsof $P _ { i } , Q _ { i } , C _ { k }$ are linearly independent, sothat $y \mapsto \left( P _ { i } ( y ) , Q _ { i } ( y ) , C _ { k } ( y ) \right)$ constitutesa local change of coordinates to canonical form.

The functions $C _ { 1 } ( y ) , \ldots , C _ { q } ( y )$ arecalleddistinguishedfunctions (ausgezeichneteFunktionen）by Lie.

Proof.We followLie'soriginal proof.Similarideas,andthe same notation,are alsopresent in Darboux'spaper.The proof proceeds in several steps,satisfying the conditions of(3.13),from one line tothe next,by solvingsystems of linear partial differential equations.

(a)If all $b _ { i j } ( y _ { 0 } ) = 0$ ,the constant rank assumption implies $b _ { i j } ( y ) = 0$ ina neighbourhood of $y _ { 0 }$ Wethus have $m = 0$ and all coordinates $C _ { i } ( y ) = y _ { i }$ are Casimirs.

（b)If there exist $i , j$ with $b _ { i j } ( y _ { 0 } ) \neq 0$ ,weset $Q _ { 1 } ( y ) = y _ { i }$ andwe determine $P _ { 1 } ( y )$ asthe solution of the linearpartial differential equation

$$
\{ Q _ { 1 } , P _ { 1 } \} = 1 .
$$

Because of $b _ { i j } ( y _ { 0 } ) \neq 0$ theassumption of Theorem 3.3is satisfied and thisyields the existence of $P _ { 1 }$ .We next consider the homogeneous system

$$
\{ Q _ { 1 } , F \} = 0 \qquad \mathrm { a n d } \qquad \{ P _ { 1 } , F \} = 0
$$

ofpartial differential equations.ByLemma 3.2and(3.14） theLie operatorscorrespondingto $Q _ { 1 }$ and $P _ { 1 }$ commute,sothatbyTheorem3.3 the system(3.15）has $n - 2$ independent solutions $F _ { 3 } , \ldots , F _ { n }$ Their gradients together with thoseof $Q _ { 1 }$ and $P _ { 1 }$ formabasis of $\mathbb { R } ^ { n }$ Wetherefore can change coordinates from $y _ { 1 } , \ldots , y _ { n }$ to $Q _ { 1 } , P _ { 1 } , F _ { 3 } , \ldots , F _ { n }$ （mapping $y _ { 0 }$ to $\scriptstyle { y _ { 0 } }$ ).In these coordinates the first two rows and the first two columns of the structure matrix $\hat { B } ( \widetilde { y } )$ have the required form.

(c）If $b _ { i j } ( \widetilde { y } _ { 0 } ) = 0$ for all $i , j \geq 3$ ,wehave $m = 1$ (similar to step(a)） and the coordinates $F _ { 3 } , \ldots , F _ { n }$ are Casimirs.

(d) If there exist $i \geq 3$ and $j \geq 3$ with $\hat { b } _ { i j } ( \widetilde { y } _ { 0 } ) \neq 0$ ,weset $Q _ { 2 } = F _ { i }$ andwe determine $P _ { 2 }$ fromthe inhomogeneous system

$$
\{ Q _ { 1 } , P _ { 2 } \} = 0 , \quad \{ P _ { 1 } , P _ { 2 } \} = 0 , \quad \{ Q _ { 2 } , P _ { 2 } \} = 1 .
$$

Theinhomogeneities satisfy (3.9),and the Lie operators corresponding to $Q _ { 1 }$ , $P _ { 1 }$ , $Q _ { 2 }$ commute (byLemma3.2).Theorem 3.3provesthe existence of such a $P _ { 2 }$ .We then consider the homogeneous system

$$
\{ Q _ { 1 } , F \} = 0 , \quad \{ P _ { 1 } , F \} = 0 , \quad \{ Q _ { 2 } , F \} = 0 , \quad \{ P _ { 2 } , F \} = 0
$$

andapply oncemore Theorem 3.3.We get $n - 4$ independent solutions,which we denote again $F _ { 5 } , \ldots , F _ { n }$ Asin part(b）of the proofwe get new coordinates $Q _ { 1 } , P _ { 1 } , Q _ { 2 } , P _ { 2 } , F _ { 5 } , \ldots , F _ { n }$ ,forwhich thefirst fourrowsand columns of the structurematrix are canonical.

(e)The proof now continues by repeating steps (c) and (d) until the structure matrix has thedesired form. □

Corollary3.5(CasimirFunctions).InthesituationofTheorem3.4thefunctions $C _ { 1 } ( y ) , \ldots , C _ { q } ( y )$ satisfy

$$
\{ C _ { i } , H \} = 0 \qquad f o r a l l s m o o t h H .
$$

Proof.Theorem3.4 statesthat $\nabla C _ { i } ( y ) ^ { T } B ( y ) \nabla H ( y ) = 0$ ,when $H ( y )$ is one of the functions $P _ { j } ( y ) , Q _ { j } ( y )$ or $C _ { j } ( y )$ However,thegradients of these functions forma basis of ${ \mathbb { R } } ^ { n }$ Consequently, $\nabla C _ { i } ( y ) ^ { T } B ( y ) = 0$ and(3.16)is satisfied forall differentiable functions $H ( y )$ □

This property implies that all Casimir functions are first integrals of(2.12)whatever $H ( y )$ is.Consequently，(2.12）is (closeto $y _ { 0 }$ ）adifferential equation on the manifold

$$
{ \mathcal { M } } = \{ y \in U \mid C _ { i } ( y ) = C o n s t _ { i } , i = 1 , . . . , m \} .
$$

Corollary 3.6 (Transformation to Canonical Form).Denote the transformation ofTheorem3.4by $\boldsymbol { z } = \boldsymbol { \vartheta } ( y ) = \left( P _ { i } ( y ) , Q _ { i } ( y ) , C _ { k } ( y ) \right)$ With this changeof coordinates,the Poissonsystem $\dot { y } = B ( y ) \nabla H ( y )$ becomes

$$
\dot { z } = B _ { 0 } \nabla K ( z ) \qquad w i t h \qquad B _ { 0 } = \left( \begin{array} { r r } { { J ^ { - 1 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $K ( z ) = H ( y )$ Writing ${ z } = ( p , q , c )$ ,this systembecomes

$$
\dot { p } = - K _ { q } ( p , q , c ) , \qquad \dot { q } = K _ { p } ( p , q , c ) , \qquad \dot { c } = 0 .
$$

Proof. The transformed differential equation is

$$
\dot { z } = \vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T } \nabla K ( z ) \qquad \mathrm { w i t h } \qquad y = \vartheta ^ { - 1 } ( z ) ,
$$

and Theorem3.4 states that $\vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T } = B _ { 0 } ,$

# VII.4 Poisson Integrators

Before discussing geometric numerical integrators,we show that many important properties of Hamiltonian systems in canonical formremain valid for systems

$$
\begin{array} { r } { \dot { y } = B ( y ) \nabla H ( y ) , } \end{array}
$$

where $B ( y )$ represents a Poisson bracket.

# VII.4.1 Poisson Maps and Symplectic Maps

Wehave already seen that the Hamiltonian $H ( y )$ isafirst integral of(4.1).We shall showhere that the flow of(4.1) satisfiesaproperty closely related to symplecticity.

Definition 4.1.A transformation $\varphi : U \to \mathbb { R } ^ { n }$ (where $U$ is an open set in $\mathbb { R } ^ { n }$ )is calledaPoissonmapwith respect to the bracket (2.8),ifits Jacobian matrix satisfies

$$
\varphi ^ { \prime } ( y ) B ( y ) \varphi ^ { \prime } ( y ) ^ { T } = B \big ( \varphi ( y ) \big ) .
$$

Anequivalent condition is that forall smooth real-valued functions $F , G$ defined on $\varphi ( U )$ ,

$$
\{ F \circ \varphi , G \circ \varphi \} ( y ) = \{ F , G \} { \bigl ( } \varphi ( y ) { \bigr ) } ,
$$

asis seen by the chain rule and choosing $F , G$ asthe coordinate functions.It is clear from this condition that the composition of Poisson maps is again a Poisson map.Acomparison with (3.12) shows that Poisson maps leave the structurematrix invariant.

For the canonical symplectic structure,where $B ( y ) = J ^ { - 1 }$ ,condition (4.2） is equivalenttothe symplecticity ofthe transformation $\varphi ( y )$ Thiscan be seen by takingthe inverse of both sides of(4.2),and by multiplying the resulting equation with $\varphi ^ { \prime } ( y )$ from the right and with $\varphi ^ { \prime } ( y ) ^ { T }$ from the left.Alsoin the situation of a Hamiltonian system(2.17）ona symplectic submanifold $\mathcal { M }$ ,where $B ( y )$ is the structure matrix of the differential equationincoordinates $y$ asinTheorem2.8,condition (4.2)is equivalent to symplecticity in the sense of preserving the symplectic twoform(2.16) on the tangent space,as in(1.16):

Definition 4.2.A map $\psi : \mathcal { M }  \mathcal { M }$ ona symplectic manifold $\mathcal { M }$ is called symplecticif forevery $x \in \mathcal { M }$ ,

$$
\omega _ { \psi ( x ) } \left( \psi ^ { \prime } ( x ) \xi _ { 1 } , \psi ^ { \prime } ( x ) \xi _ { 2 } \right) = \omega _ { x } ( \xi _ { 1 } , \xi _ { 2 } ) \qquad { \mathrm { f o r ~ a l l } } \quad \xi _ { 1 } , \xi _ { 2 } \in T _ { x } { \mathcal { M } } .
$$

A near-identity map $\psi : \mathcal { M }  \mathcal { M }$ is symplectic ifandonly if theconjugatemap $\varphi$ in local coordinates $x = \chi ( y )$ ,with $\varphi ( y )$ givenby $\psi ( x ) = \chi ( \varphi ( y ) )$ for $x = \chi ( y )$ , isa Poisson map for the structure matrix of(2.21), $B ( y ) = ( X ( y ) ^ { T } J X ( y ) ) ^ { - 1 }$ with $X ( y ) = X ^ { \prime } ( y )$ This holds because $\psi ^ { \prime } ( x ) \xi = X ( \varphi ( y ) ) \varphi ^ { \prime } ( y ) \eta$ for $x = \chi ( y )$ and $\xi = X ( y ) \eta$ ,and because (4.2) is equivalent to $\varphi ^ { \prime } ( y ) ^ { T } X ( \varphi ( y ) ) ^ { T } J X ( \varphi ( y ) ) \varphi ^ { \prime } ( y ) =$ $X ( y ) ^ { T } J X ( y )$

Theorem 4.3.1f $B ( y )$ isthe structurematrix ofaPoisson bracket,then theflow $\varphi _ { t } ( y )$ ofthedifferential equation(4.1)isa Poissonmap.

Proof.（a)For $B ( y ) = J ^ { - 1 }$ thisis exactly the statement of Theorem VI.2.4 on the symplecticity of the flow of Hamiltonian systems.This result can be extended ina straightforwardway tothematrix $B _ { 0 }$ of(3.18).

(b)For the general case consider the change of coordinates $z = \vartheta ( y )$ which transforms(4.1）tocanonical form(Theorem 3.4),i.e., $\vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T } = B _ { 0 }$ and $\dot { z } = B _ { 0 } \nabla K ( z )$ with $K ( z ) = H ( y )$ (Corollary 3.6).Denoting theflows of(4.1)and $\dot { z } = B _ { 0 } \nabla K ( z )$ by $\varphi _ { t } ( y )$ and $\psi _ { t } ( z )$ ,respectively,we have $\psi _ { t } ( \vartheta ( y ) ) = \vartheta \big ( \varphi _ { t } ( y ) \big )$ and by the chain rule $\psi _ { t } ^ { \prime } \big ( \vartheta ( y ) \big ) \vartheta ^ { \prime } ( y ) = \vartheta ^ { \prime } \big ( \varphi _ { t } ( y ) \big ) \varphi _ { t } ^ { \prime } ( y ) .$ Inserting this relation into $\psi _ { t } ^ { \prime } ( z ) B _ { 0 } \psi _ { t } ^ { \prime } ( z ) ^ { T } = B _ { 0 }$ ,which follows from(a),proves the statement.

Adirect proof,avoidingtheuse of Theorem 3.4,is indicated in Exercise6.

FromTheorems2.8and4.3and theremarkafterDefinition4.2wenote the following.

Corollary4.4. Theflow ofa Hamiltoniansystem(2.17)ona symplectic submanifoldissymplectic.

Theinverse of Theorem 4.3isalso true.Itextends Theorem VI.2.6 fromcanonically symplectic transformationsto Poisson maps.

Theorem4.5.Let $f ( y )$ and $B ( y )$ becontinuously differentiable on an open set $U \subset \mathbb { R } ^ { m }$ and assume that $B ( y )$ representsa Poisson bracket (Definition 2.4). Then, $\dot { y } = f ( y )$ islocallyof theform(4.1),ifandonlyif

itsflow $\varphi _ { t } ( y )$ respects the Casimirsof $B ( y )$ ,i.e., $C _ { i } ( \varphi _ { t } ( y ) ) = C o n s t$ and its flow isaPoisson map for all $y \in U$ andforallsufficiently small t.

ProofThenecessity followsfromCorollary3.5and fromTheorem4.3.For the proof of suffciency we apply the change of coordinates $( u , c ) = \vartheta ( y )$ ofTheorem3.4,which transforms $B ( y )$ intocanonical form(3.18).Wewrite thedifferential equation ${ \dot { y } } = f ( y )$ in the new variables as

$$
\dot { u } = g ( u , c ) , \qquad \dot { c } = h ( u , c ) .
$$

Ourfirst assumption expresses the fact that the Casimirs,which are the components of $c$ ,arefirst integrals of this system.Consequently,we have $h ( u , c ) \equiv 0$ The secondassumption implies that theflow of（4.5）isaPoissonmap for $B _ { 0 }$ of(3.18). Writing downexplicitly the blocks of condition (4.2),we see that this is equivalent to the symplecticity of the mapping $u _ { 0 } \mapsto u ( t , u _ { 0 } , c _ { 0 } )$ ,with $c _ { 0 }$ asaparameter. FromTheorem VI.2.6we thus obtain the existence ofa function $K ( u , c )$ such that $g ( u , c ) = J ^ { - 1 } \nabla _ { u } K ( u , c ) .$ Notice that for flows depending smoothly ona parameter, theHamiltonian also depends smoothly on it.Consequently,the vector field(4.5) is of the form $B _ { 0 } \nabla K ( u , c )$ Transforming back to the original variableswe obtain $f ( y ) = B ( y ) \nabla H ( y )$ with $H ( y ) = K ( \vartheta ( y ) )$ (see Corollary 3.6). □

# VII.4.2 Poisson Integrators

The preceding theorem shows that“beingaPoisson map and respecting the Casimirs” is characteristic for the flow of a Poisson system.This motivates the following definition.

Definition 4.6.A numerical method $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ isaPoisson integrator for the structure matrix $B ( y )$ ,if the transformation $y _ { 0 } \mapsto y _ { 1 }$ respects the Casimirs and if it isaPoisson map whenever the method is applied to (4.1).

Observe that for a Poisson integrator one has to specify the class of structure matrices $B ( y )$ .Amethod will never beaPoisson integrator forall possible $B ( y )$ .

Example 4.7.The symplectic Euler method reads

$$
\ l _ { n + 1 } = u _ { n } + h u _ { n + 1 } v _ { n } H _ { v } ( u _ { n + 1 } , v _ { n } ) , \quad v _ { n + 1 } = v _ { n } - h u _ { n + 1 } v _ { n } H _ { u } ( u _ { n + 1 } , v _ { n } )
$$

fortheLotka-Volterra problem(2.13).It produces an excellent long-time behaviour (Fig.4.1,left picture).We shall show that this isaPoissonintegrator forall separable Hamiltonians $H ( u , v ) = K ( u ) + L ( v ) .$ For this we compute the Jacobian of the map $( u _ { n } , v _ { n } ) \mapsto ( u _ { n + 1 } , v _ { n + 1 } )$ ，

$$
{ \binom { 1 - h v _ { n } H _ { v } } { h v _ { n } ( H _ { u } + u _ { n + 1 } H _ { u u } ) } } \quad { \overset { 0 } { 1 } } { \bigg ( } { \frac { \partial ( u _ { n + 1 } , v _ { n + 1 } ) } { \partial ( u _ { n } , v _ { n } ) } } { \bigg ) } = { \binom { 1 } { 0 } } \quad \quad h u _ { n + 1 } ( H _ { v } + v _ { n } H _ { v v } )
$$

(theargument of thepartial derivatives of $H$ is $\left( u _ { n + 1 } , v _ { n } \right)$ everywhere),and we checkina straightforward fashion thevalidity of(4.2).Adifferent proof,using differential forms,is givenin Sanz-Serna(1994) fora special choiceof $H ( u , v )$ . Similarly,the adjoint of thesymplectic Euler method isa Poisson integrator,and sois their composition-the Stormer-Verlet scheme.Composition methods based onthis scheme yield high order Poisson integrators,because the composition of Poisson mapsis againa Poisson map.

The implicit midpoint rule,though symplectic whenapplied to canonical Hamiltonian systems,turns out not to bea Poisson map for the structure matrix $B ( u , v )$ of (2.13).Figure 4.1(right picture) shows that the numerical solution does not remain nearaclosed curve.

Itisadifcult task to construct Poisson integrators for general Poissonsystems; cf.the overview by Karasozen (2oo4).First of all,for non-constant $B ( y )$ condition(4.2）isno longera quadratic first integral of the problem augmented by its variational equation (see Sect.VI.4.1).Secondly,the Casimir functions can be arbitraryand weknow that only linear and quadratic first integralscan be conserved automatically(Chap.IV).Therefore,Poisson integratorswill have to exploit special structures of the particular problem.

SplittingMethods.Considera（general） Poisson system $\dot { y } = B ( y ) \nabla H ( y )$ and suppose that the Hamiltonian permits a decomposition as $H ( y ) = H ^ { [ 1 ] } ( y ) + \ldots +$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/281cb5f50771a756a88176691abd042384986d0219a20717d427cd84caadcfd8.jpg)  
Fig.4.1.Numerical solutions of theLotka-Volterr equations (2.13) (step size $h = 0 . 2 5$ , whichisverylargecomparedtotheperiodofthesolution;ooOsteps;initialvalues $( 4 , 2 )$ and $( 6 , 2 )$ for all methods)

$H ^ { [ m ] } ( y )$ ,such that the individual systems $\dot { y } = B ( y ) \nabla H ^ { [ i ] } ( y )$ can be solved exactly.The flow of these subsystemsisa Poisson map and automaticallyrespects theCasimirs,and so does their composition.McLachlan (1993),Reich (1993),and McLachlan&Quispel(2oo2) present several interesting examples.

Example 4.8.In the previous example of aLotka-Volterra equationwith separable Hamiltonian $H ( u , v ) = K ( u ) + L ( v )$ ,thesystemswith Hamiltonian $K ( u )$ and $L ( v )$ canbe solved explicitly.Since theflow of each of the subsystems is aPoisson map,so is their composition.Combininga half-step with $L$ afull stepwith $K$ ， and againa half-stepwith $L$ ,wethusobtain the followingVerlet-like second-order Poisson integrator:

$$
\begin{array} { r c l } { u _ { n + 1 / 2 } } & { = } & { \exp \bigl ( \frac { h } { 2 } v _ { n } \nabla L ( v _ { n } ) \bigr ) u _ { n } } \\ { v _ { n + 1 } } & { = } & { \exp \bigl ( - h u _ { n + 1 / 2 } \nabla K ( u _ { n + 1 / 2 } ) \bigr ) v _ { n } } \\ { u _ { n + 1 } } & { = } & { \exp \bigl ( \frac { h } { 2 } v _ { n + 1 } \nabla L ( v _ { n + 1 } ) \bigr ) u _ { n + 1 / 2 } . } \end{array}
$$

In the setting of Hamiltonian systems ona manifold,the splittingapproach can be formulated in the following way.

Variational Splitting.Considera Hamiltoniansystem(2.17) ona symplectic manifold $\mathcal { M }$ ,anduse a splitting $H = H ^ { [ 1 ] } + H ^ { [ 2 ] }$ of the Hamiltonian in the following algorithm:

1. Let $x _ { n } ^ { + } \in \mathcal { M }$ be the solution at time $h / 2$ of the equation for $_ { x }$

$$
( J { \dot { x } } - \nabla H ^ { [ 1 ] } ( x ) , \xi ) = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \xi \in T _ { x } { \mathcal { M } }
$$

with initial value $x ( 0 ) = x _ { n }$

2.Let $x _ { n + 1 } ^ { - }$ be the solution at time $h$ of

$$
( J { \dot { x } } - \nabla H ^ { [ 2 ] } ( x ) , \xi ) = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \xi \in T _ { x } { \mathcal { M } }
$$

with initial value $x ( 0 ) = x _ { n } ^ { + }$

3. Take $x _ { n + 1 }$ as the solution at time $h / 2$ of (4.7) with initialvalue $x ( 0 ) = x _ { n + 1 } ^ { - }$

Splitting algorithms for Hamiltonian systems on manifolds have been studied by Dullweber,Leimkuhler&McLachlan（1997）and Benettin,Cherubini& Fasso (2001)in the context of rigid body dynamics;see Sect.VII.5.Lubich (2004) and Faou&Lubich(2Oo4) have studied the above splitting method for applications in quantum moleculardynamics;see Sect.VII.6 for an example.

ByTheorem 2.8,the substeps 1.-3.written incoordinates $x = \chi ( y )$ are Poisson systems $\dot { y } = B ( y ) \nabla K ^ { [ i ] } ( y )$ with $K ^ { [ i ] } ( y ) = H ^ { [ i ] } ( \chi ( y ) )$ ,butthe algorithm itself isindependent of the choice of coordinates.Since the substeps are exact flows of Hamiltonian systems on the manifold $\mathcal { M }$ ,theircomposition yieldsa symplectic map.In the coordinates $y$ thesubsteps are the exact flows of Poisson systems,and hence their composition yieldsa Poisson map.

Poisson Integrators and Symplectic Integrators.Generally we note the followingcorrespondence,which rephrases the remark on symplectic mapsand Poisson mapsafterDefinition 4.2.Itapplies in particularto thesymplectic integratorsfor constrained mechanics of Sect.VII.1.

Lemma4.9.Anintegrator $x _ { 1 } = \varPsi _ { h } ( x _ { 0 } )$ fora Hamiltonian system (2.17)on a manifold $\mathcal { M }$ issymplecticifandonlyif the integratorwritten inlocalcoordinates, $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ corresponding to a coordinate map $x = \chi ( y )$ ,isaPoissonintegrator forthe structure matrix $B ( y )$ of(2.21).

# VII.4.3Integrators Based on the Darboux-Lie Theorem

If weexplicitly know a transformation $z ~ = ~ \vartheta ( y )$ that brings the system $\dot { y } =$ $B ( y ) \nabla H ( y )$ to canonical form (asin Corollary 3.6),wecanproceed as follows:compute $z _ { n } = \vartheta ( y _ { n } )$ ;applyasymplectic integrator to the transformed system $\dot { z } ~ = ~ B _ { 0 } \nabla K ( z )$ （ $B _ { 0 }$ is thematrix(3.18）and $K ( z ) \ = \ H ( y ) )$ whichyields $z _ { n + 1 } = \varPsi _ { h } ( z _ { n } )$ ;computefinally $y _ { n + 1 }$ from $z _ { n + 1 } = \vartheta ( y _ { n + 1 } ) .$ Thisyields a Poisson integratorby the followinglemma.

Lemma 4.10.Let $\boldsymbol { z } = ( u , c ) = \boldsymbol { \vartheta } ( y )$ bethetransformationof Theorem 3.4.Supposethat the integrator $\varPhi _ { h } ( y )$ takestheform

$$
\varPsi _ { h } ( z ) = \left( \begin{array} { c } { \varPsi _ { h } ^ { 1 } ( u , c ) } \\ { c } \end{array} \right)
$$

in the new variables $z = ( u , c )$ .Then, $\varPhi _ { h } ( y )$ isaPoisson integratorifandonlyif $u \mapsto \varPsi _ { h } ^ { 1 } ( u , c )$ isasymplectic integrator for everyc.

Proof. The integrator $\varPhi _ { h } ( y )$ is Poisson for the structure matrix $B ( y )$ ifand only if $\varPsi _ { h } ( z )$ is Poisson for the matrix $B _ { 0 }$ of(3.18);see Exercise 7.By assumption, $\varPsi _ { h } ( z )$ preserves the Casimirs of $B _ { 0 }$ .Theidentity

$$
\varPsi _ { h } ^ { \prime } ( z ) B _ { 0 } \varPsi _ { h } ^ { \prime } ( z ) ^ { T } = \left( \begin{array} { c c } { A J ^ { - 1 } A ^ { T } } & { 0 } \\ { 0 } & { 0 } \end{array} \right)
$$

with $A = \partial \varPsi _ { h } ^ { 1 } / \partial u$ proves the statement.

Notice that the transformation $\vartheta$ hasto be global in the sense that it has to be thesame for all integration steps.Otherwiseadegradationin performance,similar tothatof the experiment inExampleV.4.3,has to beexpected.

Example 4.11.Asa first illustration consider theLotka-Volterra system (2.13). Applyingthe transformation $\vartheta ( u , v ) = ( \ln u , \ln v ) = ( p , q )$ ,thissystem becomes canonicallyHamiltonian with

$$
K ( p , q ) = - H ( u , v ) = - H ( e ^ { p } , e ^ { q } ) .
$$

Ifweapply the symplectic Euler method to this Hamiltonian system,and if we transform back to the original variables,we obtain the method

$$
\begin{array} { r l } & { u _ { n + 1 } ~ = ~ u _ { n } \exp \bigl ( h v _ { n } H _ { v } ( u _ { n + 1 } , v _ { n } ) \bigr ) , } \\ & { v _ { n + 1 } ~ = ~ v _ { n } \exp \bigl ( - h u _ { n + 1 } H _ { u } ( u _ { n + 1 } , v _ { n } ) \bigr ) . } \end{array}
$$

Incontrast to themethod ofExample4.7,(4.9)isalsoaPoisson integrator for(2.13) if $H ( u , v )$ is not separable.If we compose a step with step size $h / 2$ of the symplecticEuler method with itsadjoint method,thenwe obtain again,in the case ofa separable Hamiltonian,the method (4.6).

Example 4.12 (Ablowitz-Ladik Discrete Nonlinear Schrodinger Equation). Aninteresting space discretization of the nonlinear Schrodinger equation is the Ablowitz-Ladikmodel

$$
i \dot { y } _ { k } + \frac { 1 } { \Delta x ^ { 2 } } \big ( y _ { k + 1 } - 2 y _ { k } + y _ { k - 1 } \big ) + \lvert y _ { k } \rvert ^ { 2 } \big ( y _ { k + 1 } + y _ { k - 1 } \big ) = 0 ,
$$

which we consider under periodic boundary conditions $y _ { k + N } = y _ { k }$ （ $\varDelta x = 1 / N$ ). Itiscompletely integrable(Ablowitz-Ladik1976)and,aswe shall see below,it isa Poisson system with noncanonical Poisson bracket.Splitting the variables into real and imaginaryparts, $y _ { k } = u _ { k } + i v _ { k }$ ,weobtain

$$
\begin{array} { r c l } { \dot { u } _ { k } } & { = } & { \displaystyle - \frac { 1 } { \Delta x ^ { 2 } } \big ( v _ { k + 1 } - 2 v _ { k } + v _ { k - 1 } \big ) - \big ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } \big ) \big ( v _ { k + 1 } + v _ { k - 1 } \big ) } \\ { \dot { v } _ { k } } & { = } & { \displaystyle \frac { 1 } { \Delta x ^ { 2 } } \big ( u _ { k + 1 } - 2 u _ { k } + u _ { k - 1 } \big ) + \big ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } \big ) \big ( u _ { k + 1 } + u _ { k - 1 } \big ) . } \end{array}
$$

With $u = ( u _ { 1 } , \dotsc , u _ { N } )$ , $v = ( v _ { 1 } , \ldots , v _ { N } )$ this system can be writen as

$$
\left( \begin{array} { c } { \dot { u } } \\ { \dot { v } } \end{array} \right) = \left( \begin{array} { c c } { 0 } & { - D ( u , v ) } \\ { D ( u , v ) } & { 0 } \end{array} \right) \left( \begin{array} { c } { \nabla _ { u } H ( u , v ) } \\ { \nabla _ { v } H ( u , v ) } \end{array} \right) ,
$$

where $D = \mathrm { d i a g } ( d _ { 1 } , \dots , d _ { N } )$ is thediagonal matrix with entries

$$
d _ { k } ( u , v ) = 1 + \Delta x ^ { 2 } \big ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } \big ) ,
$$

and the Hamiltonian is

$$
H ( u , v ) = \frac { 1 } { \varDelta x ^ { 2 } } \sum _ { l = 1 } ^ { N } \Bigl ( u _ { l } u _ { l - 1 } + v _ { l } v _ { l - 1 } \Bigr ) - \frac { 1 } { \varDelta x ^ { 4 } } \sum _ { l = 1 } ^ { N } \ln \bigl ( 1 + \varDelta x ^ { 2 } ( u _ { l } ^ { 2 } + v _ { l } ^ { 2 } ) \bigr ) .
$$

Wethus getaPoisson system (the conditions ofLemma 2.3are directly verified). Thereare many possibilities to transform thissystem to canonical form.Tang, Pérez-Garcia&Vazquez（1997)propose the transformation

$$
p _ { k } = \frac { 1 } { \varDelta x \sqrt { 1 + \varDelta x ^ { 2 } v _ { k } ^ { 2 } } } \arctan \Bigl ( \frac { \varDelta x } { \sqrt { 1 + \varDelta x ^ { 2 } v _ { k } ^ { 2 } } } \cdot u _ { k } \Bigr ) , \qquad q _ { k } = v _ { k } ,
$$

forwhich the inversecanbecomputedinastraightforward way.Here,we suggest the transformation

$$
\begin{array} { l } { { p _ { k } = u _ { k } \sigma \big ( \varDelta x ^ { 2 } ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } ) \big ) } } \\ { { q _ { k } = v _ { k } \sigma \big ( \varDelta x ^ { 2 } ( u _ { k } ^ { 2 } + v _ { k } ^ { 2 } ) \big ) } } \end{array} \qquad \mathrm { w i t h } \qquad \sigma ( x ) = \sqrt { \frac { \ln ( 1 + x ) } { x } } ,
$$

which treats the variables more symmetrically.Itsinverseis

$$
\left. \begin{array} { l } { { u _ { k } = p _ { k } \tau \bigl ( \varDelta x ^ { 2 } ( p _ { k } ^ { 2 } + q _ { k } ^ { 2 } ) \bigr ) } } \\ { { v _ { k } = q _ { k } \tau \bigl ( \varDelta x ^ { 2 } ( p _ { k } ^ { 2 } + q _ { k } ^ { 2 } ) \bigr ) } } \end{array} \right. \qquad \mathrm { w i t h } \qquad \tau ( x ) = \frac { \exp { x } - 1 } { x } .
$$

Both transformations takethe system(4.1O) to canonical form.For the transformation(4.11）the Hamiltonianin thenewvariablesis

$$
\begin{array} { c } { { \displaystyle ( p , q ) = \frac { 1 } { \varDelta x ^ { 2 } } \sum _ { l = 1 } ^ { N } \tau \bigl ( \varDelta x ^ { 2 } ( p _ { l } ^ { 2 } + q _ { l } ^ { 2 } ) \bigr ) \tau \bigl ( \varDelta x ^ { 2 } ( p _ { l - 1 } ^ { 2 } + q _ { l - 1 } ^ { 2 } ) \bigr ) \Bigl ( p _ { l } p _ { l - 1 } + q _ { l } q _ { l - 1 } \Bigr ) } } \\ { { - \displaystyle \frac { 1 } { \varDelta x ^ { 2 } } \sum _ { l = 1 } ^ { N } ( p _ { l } ^ { 2 } + q _ { l } ^ { 2 } ) . } } \end{array}
$$

Applying standard symplectic schemes to this Hamiltonian yields Poisson integrators for(4.10）.

# VII.5 Rigid Body Dynamicsand Lie-Poisson Systems

..these topics,which,after all,have occupied workers in geometric mechanicsformanyyears. （R.McLachlan 2003）

Animportant Poisson system is given by Euler's famous equations for the motionof arigidbody(see left picture ofFig.5.1）,forwhichwe recall the history and derivation and present various structure-preserving integrators.Euler's equationsare aparticular case ofLie-Poisson systems,which result from areduction process of Hamiltonian systems on a Lie group.

# VI1.5.1 Historyof theEuler Equations

“Lesujet que jeme propose detraiterici,est dela derniere importance dansla Mecanique;&j'ai deja faitplusieurs efforts pourlemetre dans tout son jour.Mais,quoiquele calcul ait assesbienreussi,&que j’ai decouvert desformules analytiques.,leur application étoit pourtant assujettieades difficultes qui $\mathbf { m } ^ { \prime }$ ontparu presque toutafait insurmontables. Or,depuis que j'ai developé les principes de la conoissance mecanique des corps,la belle propriete des trois axes principaux dont chaque corps est doué,m’a enfin mis en état de vaincre toutes ces difficultés,..

(Euler1758b,p.154)

Agreat challenge forEuler were his effortsto establish amathematical analysis for themotion ofarigid body.Due tothe factthat sucha bodycan haveanarbitrary shape and mass distribution (see left picture of Fig.5.2),and that therotation axis canarbitrarily movewith time,theproblemisdifficultand Euler struggled formany years(all these articlesare collected in OperaOmnia,Ser.II,Vols.7and 8).The breakthroughwas enabled bythediscovery thatany body,ascomplicatedasmaybe itsconfiguration,reduces toan inertia ellipsoid with three principal axesand three numbers,the principal moments of inertia(Euler 1758a;see themiddle pictureof Fig.5.2 and the citation).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/8ee9f0d7c83432acf66bcb394669596405b4c2f2967219038991797e6c0400eb.jpg)  
Fig.5.1.Left picture:first publication of the Euler equations in Euler(1758b).Right picture: principal axesas eigenvectors inLagrange（1788)

TheInertia Ellipsoid.We choose a moving coordinate system connected to the body $B$ andwe consider motions of the bodywhere the origin is fixed.By another ofEuler's famous theorems,any such motion isinfinitesimallyarotation around an axis.Werepresent therotationaxisof the body bythedirectionofavector $\omega$ and the speed of rotation bythe length of $\omega$ .Thenthevelocity of amass point $x$ of $\boldsymbol { B }$ is given by the exterior product

$$
v = \omega \times x = { \left( \begin{array} { l } { \omega _ { 2 } x _ { 3 } = \omega _ { 3 } x _ { 2 } } \\ { \omega _ { 3 } x _ { 1 } - \omega _ { 1 } x _ { 3 } } \\ { \omega _ { 1 } x _ { 2 } - \omega _ { 2 } x _ { 1 } } \end{array} \right) } = { \left( \begin{array} { l l l } { 0 } & { - \omega _ { 3 } } & { \omega _ { 2 } } \\ { \omega _ { 3 } } & { 0 } & { - \omega _ { 1 } } \\ { - \omega _ { 2 } } & { \omega _ { 1 } } & { 0 } \end{array} \right) } { \left( \begin{array} { l } { { \bar { x } } _ { 1 } } \\ { { \bar { x } } _ { 2 } } \\ { { \bar { x } } _ { 3 } } \end{array} \right) }
$$

(orthogonal to $\omega$ orthogonal to $_ { x }$ ,and of length $\| { \boldsymbol { \omega } } \| \cdot \| { \boldsymbol { x } } \| \cdot \sin \gamma$ see the left picture ofFig.5.2).Thekinetic energyisobtained byintegratingtheenergy of themass

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/847ebebca93ad6ce67aed064593ada51e8299a5433c2e707f110c87ed6659309.jpg)  
Fig.5.2.Arigid bodyrotatingarounda variableaxis (left);thecorresponding inertiaellipsoid (middle); the corresponding angular momentum (right)

points $d m$ over the body

$$
\begin{array} { l } { T = \displaystyle \frac 1 2 \int _ { B } \| \omega \times x \| ^ { 2 } d m } \\ { = \displaystyle \frac 1 2 \int _ { B } \left( ( \omega _ { 2 } x _ { 3 } - \omega _ { 3 } x _ { 2 } ) ^ { 2 } \mp ( \omega _ { 3 } x _ { 1 } - \omega _ { 1 } x _ { 3 } ) ^ { 2 } \mp ( \omega _ { 1 } x _ { 2 } - \omega _ { 2 } x _ { 1 } ) ^ { 2 } \right) d m . } \end{array}
$$

If this is multiplied out,one obtains

$$
T = { \frac { 1 } { 2 } } \omega ^ { T } \theta \omega , \mathrm { w h e r e } \theta _ { i i } = \int _ { B } ( x _ { k } ^ { 2 } + x _ { \ell } ^ { 2 } ) d m , \theta _ { i k } = - \int _ { B } x _ { i } x _ { k } d m , ( i \neq k , \pm k ) \in \Omega ,
$$

Euler(1758a) showed,by endlesstrigonometric transformations,that there exist principal axes ofthe body in which this expression takes the form

$$
T = \frac { 1 } { 2 } \Big ( I _ { 1 } \omega _ { 1 } ^ { 2 } + I _ { 2 } \omega _ { 2 } ^ { 2 } + I _ { 3 } \omega _ { 3 } ^ { 2 } \Big ) .
$$

Thiswas historically the first transformation of such a3 $\times$ 3quadraticformtodiagonalform.Later,Lagrange(1788)discovered that theseaxeswere the eigenvectorsof thematrix $\Theta$ and themoments of inertia $I _ { k }$ thecorresponding eigenvalues(without calling them so,see the right picture of Fig.5.1).

TheAngular Momentum.The firstlaw ofNewton'sPrincipia states that themomentum $v \cdot m$ ofamasspoint remainsconstant in the absence of exterior forces. Thecorresponding quantity for rotational motion is the angular momentum,i.e., the exterior product $x \times v$ times the mass.Integrating over the body we obtain,with (5.1）,

$$
\boldsymbol { y } = \int _ { \boldsymbol { B } } ( \boldsymbol { x } \times \boldsymbol { v } ) d m = \int _ { \boldsymbol { B } } \bigl ( \boldsymbol { x } \times ( \boldsymbol { \omega } \times \boldsymbol { x } ) \bigr ) d m .
$$

If this ismultiplied out,the matrix $\Theta$ appears again and one obtains the surprising result(due to Poinsot 1834）

$$
y = \theta \omega , \qquad \mathrm { o r , i n t h e \ p r i n c i p a l ~ a x e s \ c o o r d i n a t e s , } \qquad y _ { k } = I _ { k } \omega _ { k } .
$$

Sucharelation is familiar from the theory of conjugate diameters (Apollonius,Book II,Prop.VI):the angular momentum isa vector orthogonal to theplane of vectors conjugateto $\omega$ (see theright picture of Fig.5.2）.

TheEuler Equations.Euler’s paper(1758a),on his discovery of the principal axes, isimmediately followed byEuler(1758b),where hederives hisequations for the motion ofa rigid body by long,doubtful and often criticized calculations,repeated ina litle less doubtful manner in Euler'smonumental treatise(1765).Beauty and elegance,not only of the result,butalso of the proof,isdue to Poinsot(1834）and Hayward（1856).ItismasterlydescribedbyKlein&Sommerfeld（1897),andin Chapter6of Arnold(1989).

From now on we choose the coordinate system,movingwith the body,such that theinertia tensor remainsdiagonal.Wealsowatch themotion of thebody from a coordinate system stationary in the space.The transformation ofavector $x \in \mathbb { R } ^ { 3 }$ in thebody frame4,to thecorresponding $\widetilde { x } \in \mathbb R ^ { 3 }$ in the stationary frame,isdenoted by

$$
\widetilde { x } = Q ( t ) x .
$$

Thematrix $Q ( t )$ is orthogonal and describes the motion of the body: for $x = e _ { i }$ we see that the columns of $Q ( t )$ are the coordinates of the body's principal axes in the stationaryframe.

Theanalogousstatement to Newton's first lawforrotational motion is:inthe absence ofexterior angular forces,the angular momentum $\bar { y }$ seenfromthefixed coordinate system,isaconstant vector5.Thissamevector $y$ seen from themoving frame,whichatany instancerotateswith the body around thevector $\boldsymbol { \omega }$ ,rotatesin the opposite direction.Therefore we have from (5.1),by changing the signs of $\boldsymbol { \omega }$ , thederivatives

$$
\begin{array} { r } { \left( \begin{array} { c } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) = \left( \begin{array} { c c c } { 0 } & { \omega _ { 3 } } & { - \omega _ { 2 } } \\ { - \omega _ { 3 } } & { 0 } & { \omega _ { 1 } } \\ { \omega _ { 2 } } & { - \omega _ { 1 } } & { 0 } \end{array} \right) \left( \begin{array} { c } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right) . } \end{array}
$$

If we insert $\omega _ { k } = y _ { k } / I _ { k }$ from (5.6),we obtain

$$
\left( { \begin{array} { c } { { \dot { y } _ { 1 } } } \\ { { \dot { y } _ { 2 } } } \\ { { \dot { y } _ { 3 } } } \end{array} } \right) = \left( { \begin{array} { c c c } { { 0 } } & { { y _ { 3 } / I _ { 3 } } } & { { - y _ { 2 } / I _ { 2 } } } \\ { { - y _ { 3 } / I _ { 3 } } } & { { 0 } } & { { y _ { 1 } / I _ { 1 } } } \\ { { y _ { 2 } / I _ { 2 } } } & { { - y _ { 1 } / I _ { 1 } } } & { { 0 } } \end{array} } \right) { \binom { y _ { 1 } } { y _ { 3 } } } = \left( { \begin{array} { c } { { ( I _ { 3 } ^ { - 1 } - I _ { 2 } ^ { - 1 } ) y _ { 3 } y _ { 2 } } } \\ { { ( I _ { 1 } ^ { - 1 } - I _ { 3 } ^ { - 1 } ) y _ { 1 } y _ { 3 } } } \\ { { ( I _ { 2 } ^ { - 1 } - I _ { 1 } ^ { - 1 } ) y _ { 2 } y _ { 1 } } } \end{array} } \right)
$$

or,byrearranging theproducts theotherwayround,

$$
\begin{array} { r } { \left( \begin{array} { l } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) = \left( \begin{array} { c c c } { 0 } & { - y _ { 3 } } & { y _ { 2 } } \\ { y _ { 3 } } & { 0 } & { - y _ { 1 } } \\ { - y _ { 2 } } & { y _ { 1 } } & { 0 } \end{array} \right) \left( \begin{array} { l } { y _ { 1 } / I _ { 1 } } \\ { y _ { 2 } / I _ { 2 } } \\ { y _ { 3 } / I _ { 3 } } \end{array} \right) , } \end{array}
$$

$C ( y ) = \textstyle { \frac { 1 } { 2 } } \sum _ { k = 1 } ^ { 3 } y _ { k } ^ { 2 }$ iand $\begin{array} { r } { H ( y ) = \frac { 1 } { 2 } \sum _ { k = 1 } ^ { 3 } I _ { k } ^ { - 1 } y _ { k } ^ { 2 } } \end{array}$ Theseare the two quadratic invariants ofChap.IV.The first represents the length of the constant angular momentum $\bar { y }$ in the orthogonal body frame,and the second represents the energy(5.4).

Computation of the Position Matrix $Q ( t )$ Once we have solved the Euler equationsfor $y ( t )$ ,we obtain the rotation vector $\omega ( t )$ by(5.6).Itremains to find thematrix $Q ( t )$ which gives the position of our rotating body.We know that the columns of thematrix $Q$ ,seen in the stationary frame,correspond tothe unit vectors $e _ { i }$ in the bodyframe.Theserotate,by(5.1),with the velocity

$$
\Bigl ( \omega \times e _ { 1 } , \omega \times e _ { 2 } , \omega \times e _ { 3 } \Bigr ) = \left( \begin{array} { c c c } { { 0 } } & { { - \omega _ { 3 } } } & { { \omega _ { 2 } } } \\ { { \omega _ { 3 } } } & { { 0 } } & { { - \omega _ { 1 } } } \\ { { - \omega _ { 2 } } } & { { \omega _ { 1 } } } & { { 0 } } \end{array} \right) = W .
$$

We thus obtain $\dot { Q }$ ,therotational velocity expressed inthe stationary frame,by the back transformation (5.7):

$$
{ \dot { Q } } = Q W \qquad { \mathrm { o r } } \qquad Q ^ { T } { \dot { Q } } = W .
$$

Thisisadifferential system for $Q$ which,because $W$ is skew-symmetric,preserves the orthogonality of $Q .$ The problem is solved $-$ intheory.

# VII.5.2 Hamiltonian Formulation of Rigid Body Motion

Inorder to openthedoor for efficient numericalalgorithms,we treat therigid body asaconstrainedHamiltonian system.

Position Variables.Theposition of therigid bodyat time $t$ isdetermined,inview of(5.7),byathree-dimensional orthogonal matrix $Q ( t )$ The constraints to be respected are thus $Q ^ { I } Q - I = 0$ .

Kinetic Energy.Asin(5.12),we associate with $Q$ and $\dot { Q }$ the skew-symmetric matrix $W = Q ^ { T } \dot { Q }$ whose entries $\omega _ { k }$ ,arrangedasin(5.11),determine thekinetic energy by(5.4）:

$$
T = { \frac { 1 } { 2 } } \big ( I _ { 1 } \omega _ { 1 } ^ { 2 } + I _ { 2 } \omega _ { 2 } ^ { 2 } + I _ { 3 } \omega _ { 3 } ^ { 2 } \big ) .
$$

Forany diagonal matrix $D = \mathrm { d i a g } ( d _ { 1 } , d _ { 2 } , d _ { 3 } )$ we observe

$$
\mathrm { t r a c e } ( W D W ^ { T } ) = ( d _ { 2 } + d _ { 3 } ) { \omega } _ { 1 } ^ { 2 } + ( d _ { 3 } + d _ { 1 } ) { \omega } _ { 2 } ^ { 2 } + ( d _ { 1 } + d _ { 2 } ) { \omega } _ { 3 } ^ { 2 } .
$$

Therefore,with

$$
I _ { 1 } = d _ { 2 } + d _ { 3 } , I _ { 2 } = d _ { 3 } + d _ { 1 } , I _ { 3 } = d _ { 1 } + d _ { 2 } \mathrm { o r } d _ { k } = \int _ { \cal B } x _ { k } ^ { 2 } d m \ ,
$$

（note that $d _ { k } \ > \ 0$ forall bodiesthat have interior points),we obtain the kinetic energyas

$$
T = { \frac { 1 } { 2 } } \operatorname { t r a c e } \left( W D W ^ { T } \right) .
$$

Inserting $W = Q ^ { T } Q$ ,wehave

$$
T = { \frac { 1 } { 2 } } \operatorname { t r a c e } { ( Q ^ { T } \dot { Q } D \dot { Q } ^ { T } Q ) } = { \frac { 1 } { 2 } } \operatorname { t r a c e } { ( \dot { Q } D \dot { Q } ^ { T } ) } ,
$$

since $Q$ is an orthogonal matrix.

ConjugateVariables.We now have anexpression for thekinetic energy in termsof derivatives of position coordinates and are able to introduce the conjugate momenta

$$
P = \partial T / \partial { \dot { Q } } = { \dot { Q } } D .
$$

If we suppose to have,inaddition to $T$ ,apotential $U ( Q ) ,$ we get the Hamiltonian

$$
H ( P , Q ) = \textstyle { \frac { 1 } { 2 } } \operatorname { t r a c e } { \big ( } P D ^ { - 1 } P ^ { T } { \big ) } + U ( Q ) .
$$

LagrangeMultipliers.The constraints are given by the orthogonality of $\boldsymbol { \mathcal { Q } }$ ,i.e.,the equation $g ( Q ) = Q ^ { T } Q - I = 0 ,$ Since thismatrix is always symmetric,this consists of $\frac { 1 } { 2 } n ( n + 1 ) = 6$ independent algebraic conditions,calling for six Lagrangemultipliers.If the expression $G ( Q ) ^ { \tau } \lambda$ in(1.9)is actually computed, it turns out that this term becomes the product $Q \varLambda$ ,where the sixLagrange multipliersare arranged in a symmetric matrix $\varLambda$ ;seealso formula(IV.9.6).Thus,theconstrainedHamiltonian system(1.9）reads in our case,with $\nabla U = \left( \partial U / \partial Q _ { i j } \right)$ ，

$$
\begin{array} { r c l } { { \dot { Q } } } & { { = } } & { { P D ^ { - 1 } } } \\ { { \dot { P } } } & { { = } } & { { - \nabla U ( Q ) - Q \Lambda \qquad \mathrm { ( \nabla { A } \ s y m m e t r i c ) } } } \\ { { 0 } } & { { = } } & { { Q ^ { T } Q - I . } } \end{array}
$$

Reduction to theEuler Equations.The key idea is to introduce thematrix

$$
Y = Q ^ { T } P = Q ^ { T } \dot { Q } D = W D = \left( \begin{array} { c c c } { { 0 } } & { { - d _ { 2 } \omega _ { 3 } } } & { { d _ { 3 } \omega _ { 2 } } } \\ { { d _ { 1 } \omega _ { 3 } } } & { { 0 } } & { { - d _ { 3 } \omega _ { 1 } } } \\ { { - d _ { 1 } \omega _ { 2 } } } & { { d _ { 2 } \omega _ { 1 } } } & { { 0 } } \end{array} \right) ,
$$

where the $\omega _ { k }$ can be further expressed in terms of theangularmomenta $y _ { k } = I _ { k } \omega _ { k }$ Using the notation skew $( A ) = { \textstyle { \frac { 1 } { 2 } } } ( A - A ^ { \mathit { 1 } } )$ we see,with(5.13）,that

$$
Y - Y ^ { T } = 2 \operatorname { s k e w } \left( Y \right) = \left( { \begin{array} { c c c } { 0 } & { - y _ { 3 } } & { y _ { 2 } } \\ { y _ { 3 } } & { 0 } & { - y _ { 1 } } \\ { - y _ { 2 } } & { y _ { 1 } } & { 0 } \end{array} } \right)
$$

contains just the angularmomenta.Moreover, $\mathcal Ḋ P Ḍ$ isskew-symmetric.By（5.18 thederivative of $Y$ is seen to be

$$
\dot { Y } = \dot { Q } ^ { T } P + Q ^ { T } \dot { P } = D ^ { - 1 } P ^ { T } P - Q ^ { T } \nabla U ( Q ) - A = D ^ { - 1 } Y ^ { T } Y - Q ^ { T } \nabla U ( Q )
$$

Taking the skew-symmetric part of this equation,the symmetric matrix $\varLambda$ drops out and we obtain

$$
\operatorname { s k e w } \left( { \dot { Y } } \right) = \operatorname { s k e w } \left( D ^ { - 1 } Y ^ { T } Y \right) = \operatorname { s k e w } \left( Q ^ { T } \nabla U ( Q ) \right) .
$$

These are,for $U = 0$ ,precisely the above Euler equations,obtained a second time.

# VII.5.3RigidBody Integrators

Foranumerical simulation of rigid bodymotions,one can either solve theconstrained Hamiltonian system(5.18）,or one can solve the differential equation (5.21） for theangular momentum $Y ( t )$ in tandem with the equation (5.12） for $Q ( t )$ We consider the following approaches:(I) an eficient application of the RATTLEalgorithm(1.26),and (II) various splitting methods.

# I)RATTLE

Weapply the symplectic RATTLE algorithm(1.26) to the system(5.18),and rewrite the formulas in terms of the variables $Y$ and $Q$ Thisapproach has been proposed anddeveloped independentlybyMcLachlan&Scovel(1995)andReich(1994).

Anapplication of theRATTLE algorithm(1.26)to the system(5.18)yields

$$
\begin{array} { r l r } { \quad } & { P _ { 1 / 2 } = \ b _ { 0 } - \cfrac { h } { 2 } \nabla U ( Q _ { 0 } ) - \cfrac { h } { 2 } Q _ { 0 } \varLambda _ { 0 } } & \\ { \quad } & { Q _ { 1 } = \ Q _ { 0 } + h P _ { 1 / 2 } D ^ { - 1 } , \quad \ Q _ { 1 } ^ { T } Q _ { 1 } = I } & { ( 5 . } \\ { \quad } & { P _ { 1 } = \ P _ { 1 / 2 } - \cfrac { h } { 2 } \nabla U ( Q _ { 1 } ) - \cfrac { h } { 2 } Q _ { 1 } \varLambda _ { 1 } , \quad } & { Q _ { 1 } ^ { T } P _ { 1 } D ^ { - 1 } + D ^ { - 1 } P _ { 1 } ^ { T } Q _ { 1 } = 0 , } \end{array}
$$

where both $\varLambda _ { 0 }$ and $\varLambda _ { 1 }$ are symmetric matrices.We let $Y _ { 0 } = Q _ { 0 } ^ { \prime } P _ { 0 }$ , $Y _ { 1 } = Q _ { 1 } ^ { \prime } P _ { 1 }$ , and ${ \cal Z } ~ = ~ Q _ { 0 } ^ { I } P _ { 1 / 2 } D ^ { - 1 }$ Wemultiplythe first relation of(5.22）by $Q _ { 0 } ^ { T }$ ,thelast relation by $Q _ { 1 } ^ { I }$ ,andwe eliminate the symmetric matrices $\varLambda _ { 0 }$ and $\varLambda _ { 1 }$ by taking the skew-symmetric parts of the resulting equations.The orthogonality of $Q _ { 0 } ^ { I } Q _ { 1 } =$ $I + h Z$ implies $h Z ^ { T } Z = - ( Z + Z ^ { T } )$ ,which can thenbeused to simplify the last relation.Altogether thisresults in the following algorithm.

Algorithm5.1. Let $Q _ { 0 }$ be orthogonal and $D Y _ { 0 }$ be skew-symmetric.One step $( Q _ { 0 } , Y _ { 0 } ) \mapsto ( Q _ { 1 } , Y _ { 1 } )$ ofthemethod then readsasfollows:

-find $Z$ suchthat $I + h Z$ is orthogonal and

$$
\mathrm { s k e w } \left( Z D \right) = \mathrm { ~ s k e w } \left( Y _ { 0 } \right) - \frac h 2 \mathrm { ~ s k e w } \left( Q _ { 0 } ^ { T } \nabla U ( Q _ { 0 } ) \right) ,
$$

-compute $Q _ { 1 } = Q _ { 0 } ( I + h Z )$

-compute $Y _ { 1 }$ suchthat $D Y _ { 1 }$ is skew-symmetric and

$$
\begin{array} { r } { \mathbf { k e w } \left( Y _ { 1 } \right) = \mathbf { s k e w } \left( Z D \right) - \mathbf { s k e w } \left( ( Z + Z ^ { T } ) D \right) - \frac { h } { 2 } \mathbf { s k e w } \left( Q _ { 1 } ^ { T } \nabla U ( Q _ { 1 } ) \right) . } \end{array}
$$

The second step is explicit,and the third steprepresentsa linear equation for the elementsof $Y _ { 1 }$

Computation of the First Step.We write for the knownpart of equation(5.23)

$$
\operatorname { s k e w } \left( Y _ { 0 } \right) - { \frac { h } { 2 } } \operatorname { s k e w } \left( Q _ { 0 } ^ { T } \nabla U ( Q _ { 0 } ) \right) = { \left( \begin{array} { l l l } { 0 } & { - \alpha _ { 3 } } & { \alpha _ { 2 } } \\ { \alpha _ { 3 } } & { 0 } & { - \alpha _ { 1 } } \\ { - \alpha _ { 2 } } & { \alpha _ { 1 } } & { 0 } \end{array} \right) } = A
$$

and have to solve

$$
\begin{array} { r } { \frac { 1 } { 2 } ( Z D - D Z ^ { T } ) = A , \quad ( I + h Z ^ { T } ) ( I + h Z ) = I , \quad \frac { 1 } { 2 } ( Z D + D Z ^ { T } ) = S } \end{array}
$$

(the trick was to add the last equation with $S$ anunknown symmetric matrix).Elimination gives $Z = ( A + S ) D ^ { - 1 }$ and $Z ^ { T } = D ^ { - 1 } ( S - A )$ Both inserted into the second equation lead to a Riccati equation for $S$ .There exist effcient algorithms forsuchproblems;see thereferencein Sect.IV.5.3andadetailed explanation in McLachlan& Zanna（2005).

Remark 5.2 (Moser-Veselov Algorithm).An independent accessto the above formulasisgiveninaremarkablepaperbyMoser&Veselov(1991),bytreating therigid bodythrougha discretizedvariational principle,similarto the ideasof Sect.VI.6.2.TheequivalenceisexplainedbyMcLachlan& Zanna（2oo5),followingasuggestion ofB.Leimkuhlerand S.Reich.

Quaternions(Euler Parameters).An efficient implementation of the above algorithmrequires suitablerepresentations of orthogonal matrices,and theuse of quaternionsisa standard approach.

Afterhaving revolutionized Lagrangian mechanics (see Chapt.VI),Hamilton struggled for years to generalize complex analysis to three dimensions.Hefinally achieved his dream,however not in three dimensions,but infour,and founded in 1843the theory of quaternions.

Foran introduction to quaternions(whose coefficients are sometimes called Eulerparameters)werefer to Sects.IV.2and IV.3 ofKlein(19o8),and fortheir usein numerical simulations to Sects.9.3and 11.3of Haug(1989).Quaternions can be written as $\begin{array} { r } { e = e _ { 0 } + i e _ { 1 } + j e _ { 2 } + k e _ { 3 } . } \end{array}$ wheremultiplication isdefined via the relations $i ^ { 2 } = j ^ { 2 } = k ^ { 2 } = - 1$ , $i j = k$ , $j k = i$ ， $k i = j$ and $j i = - k$ , $k j = - i$ , $i k = - j .$ The product of two quaternions $e \cdot f$ (written in matrix notation）is

$$
\begin{array} { r } { ( e _ { 0 } + i e _ { 1 } + j e _ { 2 } + k e _ { 3 } ) \quad = \quad \left( \begin{array} { l l l } { e _ { 0 } } & { < e _ { 1 } } & { - e _ { 2 } } & { - e _ { 3 } } \\ { e _ { 1 } ^ { > } } & { e _ { 0 } } & { < e _ { 3 } } & { e _ { 2 } } \\ { e _ { 2 } } & { e _ { 0 } } & { \ldots } & { e _ { 1 } } \\ { e _ { 3 } } & { e _ { 1 } ^ { > } } & { e _ { 2 } } \end{array} \right) \quad \left( \begin{array} { l } { f _ { 0 } } \\ { f _ { 1 } } \\ { f _ { 2 } } \\ { f _ { 3 } } \end{array} \right) } \end{array}
$$

Wesee(in grey）thatin dimensions $1 , 2 , 3$ appearsa skew-symmetric matrix $E$ whose structureis familiar to us.This part of thematrix changes sign if the two factorsare permuted.

Animportant discovery,for three dimensional applications of the quaternions, is the following:ifa quaternion $p$ isa3-vector (i.e.,has $p _ { 0 } = 0$ ),then $p ^ { \prime } = e \cdot p \cdot \overline { { e } }$ is a3-vector,too,and themap $p \mapsto p ^ { \prime }$ isdescribed by thematrix

$$
Q ( e ) = \| e \| ^ { 2 } I + 2 e _ { 0 } E + 2 E ^ { 2 } , \qquad E = \left( \begin{array} { c c c } { { 0 } } & { { - e _ { 3 } } } & { { e _ { 2 } } } \\ { { e _ { 3 } } } & { { 0 } } & { { - e _ { 1 } } } \\ { { - e _ { 2 } } } & { { e _ { 1 } } } & { { 0 } } \end{array} \right)
$$

where $\overline { { e } } = e _ { 0 } - i e _ { 1 } - j e _ { 2 } - k e _ { 3 }$ and $\| e \| ^ { 2 } = e \cdot \overline { { e } } = e _ { 0 } ^ { 2 } + e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 } .$

Lemma5.3.1f $\| e \| = 1$ ，then thematrix $Q ( e )$ isorthogonal.Every orthogonal matrixwithdet $Q = 1$ canbewritten in this form.We have $Q ( e ) Q ( f ) = Q ( e f )$ so thatthemultiplication oforthogonalmatrices corresponds tothemultiplication of quaternions.

Geometrically,thematrix $Q$ effectsa rotation around theaxis $\varepsilon = ( e _ { 1 } , e _ { 2 } , e _ { 3 } ) ^ { T }$ with rotation angle $\varphi$ whichsatisfies $\tan ( \varphi / 2 ) = \lVert \varepsilon \rVert / e _ { 0 }$ .

Proof.Thecondition $Q ^ { \cal I } Q = I$ can be verified directly using $E ^ { I } = - E$ and $E ^ { 3 } = - ( e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 } ) E .$ Thereciprocal statement isafamous theorem of Euler;it is based onthe fact that $\boldsymbol { \varepsilon }$ is an eigenvector of $Q$ ,which in dimension $3 \times 3$ always exists.The formula for $Q ( e ) Q ( f )$ follows from $e \cdot f \cdot p \cdot { \overline { { f } } } \cdot { \overline { { e } } } = ( e \cdot f ) \cdot p \cdot ( { \overline { { e \cdot f } } } )$

The geometric property follows from the virtues of the exterior product,because by （5.1） the matrix $Q$ mapsavector $x$ to

$$
x + 2 e _ { 0 } \varepsilon \times x + 2 \varepsilon \times ( \varepsilon \times x ) .
$$

This consists in arectangular mouvement in a plane orthogonal to $\succeq$ ；first vertical to $x$ by anamount $2 e _ { 0 } \left\| \boldsymbol { \varepsilon } \right\|$ (times the distance of $x$ ), then parallel to $x$ byan amount $2 \| \varepsilon \| ^ { 2 }$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/971edbc10aafd00d3f0538e4cc11fcbbf4c17e17cec4572ab70e39ca9eafa59e.jpg)

Applying Pythagoras'Theoremas $( 2 e _ { 0 } \| \varepsilon \| ) ^ { 2 } + ( 2 \| \varepsilon \| ^ { 2 } - 1 ) ^ { 2 } = 1$ it turns out that the map is norm preserving if $e _ { 0 } ^ { 2 } + \| \varepsilon \| ^ { 2 } = 1 .$ Theangle $\varphi / 2$ ,whose tangens can be seen to be $\lVert \varepsilon \rVert / e _ { 0 }$ ,isanangle at the circumference of thecircle for the rotation angle $\varphi$ at the center. □

Foran efficient implementation of Algorithm 5.1werepresent the orthogonal matrices $Q _ { 0 }$ , $Q _ { 1 }$ ,and $I + h Z$ byquaternions.This reduces the dimension of the systems,and step2 becomesa simple multiplication of quaternions.For solving the nonlinear system of step 1,we let $I + h Z \ = \ Q ( e )$ With the values of $\alpha _ { i }$ from(5.24）and with skew $( h Z D ) = 2 e _ { 0 }$ skew $( E D ) + 2$ skew $( E ^ { 2 } D )$ ,theequation (5.23）becomes

$$
\binom { h \alpha _ { 1 } } { h \alpha _ { 2 } } \ = \ 2 e _ { 0 } \left( \begin{array} { l } { I _ { 1 } e _ { 1 } } \\ { I _ { 2 } e _ { 2 } } \\ { I _ { 3 } e _ { 3 } } \end{array} \right) \ + \ 2 \left( \begin{array} { l } { ( I _ { 3 } - I _ { 2 } ) e _ { 2 } e _ { 3 } } \\ { ( I _ { 1 } - I _ { 3 } ) e _ { 3 } e _ { 1 } } \\ { ( I _ { 2 } - I _ { 1 } ) e _ { 1 } e _ { 2 } } \end{array} \right) ,
$$

which,together with $e _ { 0 } ^ { 2 } + e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 } = 1 ,$ represent four quadratic equations for fourunknowns.We solve them veryquickly byafew fixed-point iterations:update successively $e _ { i }$ fromtheith equationof(5.27）and then $e _ { 0 }$ from the normalizationcondition.AFortran subroutineRATORI for thisalgorithmisavailableon the homepage $<$ http://www.unige.ch/\~hairer>.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0005_pages_0281-0350/auto/images/cd5423210dbd62fe69b18c59fd89effec7c867e520fdb76cde62999dc5f6ae87.jpg)  
Fig.5.3.Numerical solutions of the rigid body equations；without/with gravitation, with/without symmetry.Initial values $y _ { 1 0 } = 0 . 2 , y _ { 2 0 } = 1 . 0 , y _ { 3 0 } = 0 . 4 ;$ initial position of $Q _ { 0 }$ determined by the quatenion $e _ { 0 } = 0 . 4 , e _ { 1 } = 0 . 2 , e _ { 2 } = 0 . 4 , e _ { 3 } = 0 . 8$ ;moments ofinertia $I _ { 1 } ~ = ~ 0 . 5$ , $I _ { 2 } ~ = ~ 0 . 8 5$ (0.5in the symmetric case), $I _ { 3 } ~ = ~ 1 ;$ stepsize $h = 0 . 1$ , integration interval $0 \leq t \leq 3 0$

Conservation ofCasimir and Hamiltonian. Itis interesing to note that,in the absence ofapotential,the Algorithm5.1 preserves exactly theCasimir $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ and,more surprisingly,also the Hamiltonian $\begin{array} { r } { \frac { 1 } { 2 } ( y _ { 1 } ^ { 2 } / I _ { 1 } + y _ { 2 } ^ { 2 } / I _ { 2 } + y _ { 3 } ^ { 2 } / I _ { 3 } ) } \end{array}$ Thiscan beseen as follows:without any potential we have skew $( Y _ { 0 } ) =$ skew（ $Z D )$ and skew $( Y _ { 1 } ) = - \operatorname { s k e w } \left( Z ^ { l ^ { \prime } } D \right)$ ,so that thevectors $( y _ { 1 0 } , y _ { 2 0 } , y _ { 3 0 } ) ^ { T }$ and $( y _ { 1 1 } , y _ { 2 1 } , y _ { 3 1 } ) ^ { T }$ are equal to $u + v$ and $u - v$ ,respectively,where $u$ and $\boldsymbol { v }$ are the vectors of the righthand side of(5.27).Since $u$ and $\boldsymbol { v }$ are orthogonal,we have $\| u + v \| = \| u - v \|$ , which proves the conservation of the Casimir.

To prove the conservation of the Hamiltonian,we first multiply therelation （5.27）with $G = \mathrm { d i a g } ( 1 / \sqrt { I _ { 1 } } , 1 / \sqrt { I _ { 2 } } , 1 / \sqrt { I _ { 3 } } )$ ,and then apply the same arguments. Thevectors $G u$ and $G v$ are still orthogonal.

Example5.4(Force-FreeandHeavy Top).WepresentinFig.5.3thenumerical solutions $y _ { i }$ obtained by the above algorithm.In the case of the heavy top,weassume the centre of gravity to be $( 0 , 0 , 1 )$ inthebody frame,and assumethat the third coordinate of the stationary frame isvertical.The potential energy due to gravity is then given by $U ( Q ) = q _ { 3 3 }$ and,expressedbyquaternions (5.26),itis $U = e _ { 0 } ^ { 2 } \mathrm { ~ - ~ }$ $e _ { 1 } ^ { 2 } - e _ { 2 } ^ { 2 } + e _ { 3 } ^ { 2 }$

# (II) Spliting Methods

Asbefore we consider the differential equation(5.21） for theangular momenta in thebody $y _ { 1 } , y _ { 2 } , y _ { 3 }$ together with the differential equation(5.12） for the rotation matrix $Q$ .Anobvious splitting in the presence of a potential is

$$
\varphi _ { h / 2 } ^ { U } \circ \varPhi _ { h } ^ { T } \circ \varphi _ { h / 2 } ^ { U } ,
$$

where $\varphi _ { t } ^ { U }$ represents the exactffow of

$$
\dot { Q } = 0 , \qquad \mathrm { s k e w } ( \dot { Y } ) = - \mathrm { s k e w } ( Q ^ { T } \nabla U ( Q ) ) ,
$$

and $\varPhi _ { h } ^ { T }$ is asuitable numerical approximation of the system corresponding to kinetic energyonly,i.e.,without any potential $U ( Q )$ The use of splitting techniques forrigidbodydynamicswasproposedbyTouma&Wisdom（1994),McLachlan（1993),Reich（1994）,andDullweber,Leimkuhler&McLachlan（1997).Fasso (2003)presentsa careful study and comparison of variousways of splitting the kinetic energy.

Computation of $\varPhi _ { h } ^ { i } .$ Wedo this bysplitting once again,by letting several moments ofinertia tending to infinity (and the corresponding $\omega _ { i }$ tending to zero).In order to avoid formal difficultieswith infinite denominators,we write the system (5.10) togetherwith(5.12)in the form

$$
\begin{array} { r l } { \left( \begin{array} { c } { \dot { y } _ { 1 } } \\ { \dot { y } _ { 2 } } \\ { \dot { y } _ { 3 } } \end{array} \right) } & { = \begin{array} { c c c } { \left( \begin{array} { c c c } { 0 } & { - y _ { 3 } } & { y _ { 2 } } \\ { y _ { 3 } } & { 0 } & { - y _ { 1 } } \\ { - y _ { 2 } } & { y _ { 1 } } & { 0 } \end{array} \right) } \end{array} \left( \begin{array} { c } { T _ { y _ { 1 } } ( y ) } \\ { T _ { y _ { 2 } } ( y ) } \\ { T _ { y _ { 3 } } ( y ) } \end{array} \right) } \\ { \dot { Q } } & { = Q \left( \begin{array} { c c c } { 0 } & { - T _ { y _ { 3 } } ( y ) } & { T _ { y _ { 2 } } ( y ) } \\ { T _ { y _ { 3 } } ( y ) } & { 0 } & { - T _ { y _ { 1 } } ( y ) } \\ { - T _ { y _ { 2 } } ( y ) } & { T _ { y _ { 1 } } ( y ) } & { 0 } \end{array} \right) , } \end{array}
$$

where $T ( y ) = { \textstyle \frac { 1 } { 2 } } ( y _ { 1 } ^ { 2 } / I _ { 1 } + y _ { 2 } ^ { 2 } / I _ { 2 } + y _ { 3 } ^ { 2 } / I _ { 3 } )$ is the kinetic energy,and $T _ { y _ { i } } ( y )$ denote partialderivatives.

Three Rotations Splitting.An obvious splitting of the kinetic energy is

$$
T ( y ) = R _ { 1 } ( y ) + R _ { 2 } ( y ) + R _ { 3 } ( y ) , \qquad R _ { i } ( y ) = y _ { i } ^ { 2 } / ( 2 I _ { i } ) ,
$$

which results in the numerical method

$$
\begin{array} { r } { \varPhi _ { h } ^ { T } = \varphi _ { h / 2 } ^ { R _ { 3 } } \circ \varphi _ { h / 2 } ^ { R _ { 2 } } \circ \varphi _ { h } ^ { R _ { 1 } } \circ \varphi _ { h / 2 } ^ { R _ { 2 } } \circ \varphi _ { h / 2 } ^ { R _ { 3 } } , } \end{array}
$$

where $\varphi _ { t } ^ { R _ { i } }$ istheeactofi $T ( y )$ replaced by $R _ { i } ( y )$ Theflow $\varphi _ { t } ^ { R _ { 1 } }$ is easily obtained: $y _ { 1 }$ remains constant and the second and third equation in (5.29)boil down to the harmonic oscillator.We obtain

$$
y ( t ) = S ( \alpha t ) y ( 0 ) , \qquad Q ( t ) = Q ( 0 ) S ( \alpha t ) ^ { T }
$$

with $\alpha = y _ { 1 } ( 0 ) / I _ { 1 }$ and the rotation matrix

$$
\begin{array} { r } { S ( \theta ) = \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { \sin \theta } \\ { 0 } & { - \sin \theta } & { \cos \theta } \end{array} \right) . } \end{array}
$$

Similarsimple formulas are obtained for the exact flows corresponding to $R _ { 2 }$ and $R _ { 3 }$

Symmetric $^ +$ Rotation Spliting.Itis often advantageous,inparticular foranearly symmetric body（ $I _ { 1 } \approx I _ { 2 }$ ,toconsiderthespliting

$$
T ( y ) = R ( y ) + S ( y ) , \quad R ( y ) = \Big ( \frac { 1 } { I _ { 1 } } - \frac { 1 } { I _ { 2 } } \Big ) \frac { y _ { 1 } ^ { 2 } } { 2 } , \quad S ( y ) = \frac { 1 } { 2 } \Big ( \frac { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { y _ { 3 } ^ { 2 } } { I _ { 3 } } \Big ) \frac { y _ { 3 } ^ { 2 } } { 2 } .
$$

and the corresponding numerical integrator

$$
\varPhi _ { h } ^ { T } = \varphi _ { h / 2 } ^ { R } \circ \varphi _ { h } ^ { S } \circ \varphi _ { h / 2 } ^ { R } .
$$

The exact flow $\varphi _ { t } ^ { R }$ is the same as(5.32) with $I _ { 1 } ^ { - 1 }$ replaced by $I _ { 1 } ^ { - 1 } - I _ { 2 } ^ { - 1 } .$ Theflow ofthesymmetricforce-free top $\varphi _ { t } ^ { S }$ possessessimpleaalyticmulastoehe first picture of Fig.5.3):we observea precession of $y$ with constant speed around a coneandarotation of thebodyaround $\omega$ with constant speed.Therefore

$$
y ( t ) = B ( \beta t ) y ( 0 ) , \qquad Q ( t ) = Q ( 0 ) A ( t ) B ( \beta t ) ^ { T } ,
$$

where $\beta = ( I _ { 3 } ^ { - 1 } - I _ { 2 } ^ { - 1 } ) y _ { 3 } ( 0 )$ ,and

$$
\mathrm { l } ( t ) = \exp { \left( \frac { t } { I _ { 2 } } { \left( \begin{array} { c c c } { 0 } & { - y _ { 3 } ( 0 ) } & { y _ { 2 } ( 0 ) } \\ { y _ { 3 } ( 0 ) } & { 0 } & { - y _ { 1 } ( 0 ) } \\ { - y _ { 2 } ( 0 ) } & { y _ { 1 } ( 0 ) } & { 0 } \end{array} \right) } \right) } , \quad B ( \theta ) = \left( - \sin \theta \quad \cos \theta \quad 0 \right)
$$

This canalso be checked directly by differentiation.

Similar to the previous algorithmitis advantageous to usearepresentation of theappearing orthogonal matrices by quaternions.The correspondence between the orthogonal rotation matrices appearing in(5.32)and(5.33)and their quaternions is, inaccordancewithLemma5.3,the following:

$$
\begin{array} { r l } { S ( \theta ) ^ { T } } & { { }  \quad \cos ( \theta / 2 ) + i \sin ( \theta / 2 ) } \\ { B ( \theta ) ^ { T } } & { { } \Longleftrightarrow \quad \cos ( \theta / 2 ) + k \sin ( \theta / 2 ) } \\ { A ( t ) } & { { } \Longleftrightarrow \quad \cos ( \vartheta / 2 ) + a ^ { - 1 } \sin ( \vartheta / 2 ) \big ( i y _ { 1 } ( 0 ) + j y _ { 2 } ( 0 ) + k y _ { 3 } ( 0 ) \big ) , } \end{array}
$$

where $a = \sqrt { y _ { 1 } ( 0 ) ^ { 2 } + y _ { 2 } ( 0 ) ^ { 2 } + y _ { 3 } ( 0 ) ^ { 2 } }$ and $\vartheta = a t / I _ { 2 }$ Thematrix multiplicationsin thealgorithm can therefore bedone very efficiently.A Fortran subroutine QUATER forthe“symmetric $^ +$ rotationsplitting”algorithmisavailable on the homepage $<$ http://www.unige.ch/\~hairer>.

# VII.5.4Lie-Poisson Systems

In Sect.VII.5.1 we have seen that the reduction of the equations of motion of the rigidbody leads to the Poissonsystem(5.1O）witha structurematrix whose entries arelinear functions.Here we consider more general Poisson systems

$$
\dot { y } = B ( y ) \nabla H ( y ) ,
$$

where the structure matrix $B ( y )$ depends linearly on $y$ ,i.e.,

$$
b _ { i j } ( y ) = \sum _ { k = 1 } ^ { n } C _ { j i } ^ { k } y _ { k } \qquad { \mathrm { f o r ~ } } i , { \hat { y } } = 1 , { \mathrm { e } } { \mathrm { : } } s { \mathrm { : } } s = 1 ,
$$

Suchsystems,calledLie-Poisson systems,areclosely related to differential equations on thedual ofLiealgebras;seeMarsden&Ratiu(1999),Chaps.13and14, foran in-depth discussion of this theory.

RecallthataLiealgebra isavector spacewithabracketwhich isanti-symmetric and satisfies the Jacobiidentity (Sect.IV.6).Let $E _ { 1 } , \ldots , E _ { n }$ bea basis ofa vector space,and definea bracket by

$$
[ E _ { i } , E _ { j } ] = \sum _ { k = 1 } ^ { n } C _ { i j } ^ { k } E _ { k }
$$

with $C _ { i j } ^ { k }$ from(5.35).Ifre $B ( y )$ of (5.35) isskew-symmetricand satisfies(2.1O),then this bracket makes the vector spaceaLie algebra (the verificationisleftasexercise)Theient $C _ { i j } ^ { k }$ arecalledstructureonstantsofthe Liealgebra.Conversely,if westart fromaLiealgebrawith bracket given by(5.36), then the matrix $B ( y )$ defined by(5.35）is the structurematrix of aPoisson bracket.

LetgbeaLiealgebra witha basis $E _ { 1 } , \ldots , E _ { n }$ andlet ${ \mathfrak { g } } ^ { * }$ be the dual of the Lie algebra,i.e.,thevectorspace ofallinear forms $Y : { \mathfrak { g } }  \mathbb { R }$ Thedualityiswritten as $\langle Y , X \rangle$ for $Y \in { \mathfrak { g } } ^ { * }$ and $X \in { \mathfrak { g } }$ Wedenote by $F _ { 1 } , \ldots , F _ { n }$ the dual basis defined by $\langle F _ { i } , E _ { j } \rangle = \delta _ { i j }$ ,theKronecker $\delta$ ，

Theorem5.5.Let $y = ( y _ { 1 } , \ldots , y _ { n } ) ^ { T } \in \mathbb { R } ^ { n }$ $\mathfrak { g }$ bea Lie algebra with basis wessoeiate $\begin{array} { r } { Y = \sum _ { j = 1 } ^ { n } y _ { j } F _ { j } \in \mathfrak { g } ^ { * } } \end{array}$ $E _ { 1 } , \ldots , E _ { n }$ satisfying（5.36）.To andweconsidera Hamiltonian6 $H ( y ) = H ( Y )$

Then,thePoissonsystem $\dot { y } = B ( y ) \nabla H ( y )$ with $B ( y )$ givenby(5.35)isequivalentto thefollowingdifferentialequation on thedual ${ \mathfrak { g } } ^ { * }$ :

$$
\langle \dot { Y } , X \rangle = \langle Y , [ H ^ { \prime } ( Y ) , X ] \rangle \qquad f o r a l l \ X \in { \mathfrak { g } } ,
$$

whereH'(Y)=∑-1 H（E

Proof.Differentiating $H ( y ) = H ( Y )$ with respect to $y _ { i }$ gives

$$
\frac { \partial H ( y ) } { \partial y _ { i } } = \langle F _ { i } , H ^ { \prime } ( Y ) \rangle \qquad \mathrm { a n d } \qquad H ^ { \prime } ( Y ) = \sum _ { j = 1 } ^ { n } \frac { \partial H ( y ) } { \partial y _ { j } } E _ { j } .
$$

Herewe have used the identification $( { \mathfrak { g } } ^ { * } ) ^ { * } = { \mathfrak { g } }$ ,because $H ^ { \prime } ( Y )$ isactuallyan elementof $( { \mathfrak { g } } ^ { * } ) ^ { * } .$ With this formula for $H ^ { \prime } ( Y )$ we are able tocompute

$$
\left. Y , [ H ^ { \prime } ( Y ) , E _ { i } ] \right. = \left. Y , \sum _ { j = 1 } ^ { n } { \frac { \partial H ( y ) } { \partial y _ { j } } } \left[ E _ { j } , E _ { i } \right] \right. = \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } { \frac { \partial H ( y ) } { \partial y _ { j } } } C _ { j i } ^ { k } \left. Y , E _ { k } \right.
$$

wherewe have used (5.36).Since $\langle \dot { Y } , E _ { i } \rangle = \dot { y } _ { i }$ and $\langle Y , E _ { k } \rangle = y _ { k }$ ,this shows that thedifferential equation （5.37）is equivalent to

$$
\dot { y } _ { \bar { \imath } } = \sum _ { j = 1 } ^ { n } \biggl ( \sum _ { k = 1 } ^ { n } C _ { j i } ^ { k } y _ { k } \biggr ) \frac { \partial H ( y ) } { \partial y _ { j } } ,
$$

which is nothing more than $\dot { y } = B ( y ) \nabla H ( y )$ with $B ( y )$ from (5.35）.

Weremark that (5.37) can bereformulated as

$$
{ \dot { Y } } = \operatorname { a d } _ { H ^ { \prime } ( Y ) } ^ { * } Y ,
$$

where $\operatorname { a d } _ { A } ^ { * }$ is theadjoint of the operator ad $_ A ( X ) = \lfloor A , X \rfloor$

Equation (5.37） is similar inappearance to the Lie bracket equation $\dot { L } \ =$ $[ A ( L ) , L ] = \operatorname { a d } _ { A ( L ) } L$ of Sect.IV.3.2.When $\mathfrak { g }$ is theLiealgebra of amatrix Lie group $G$ ,then solutions of that equationare of the form $L ( t ) = \operatorname { A d } _ { U ( t ) } L _ { 0 }$ where

$$
\mathbf { A d } _ { U } \mathbf { \boldsymbol { X } } = U \mathbf { \boldsymbol { X } } U ^ { - 1 } ;
$$

see the proof of LemmaIV.3.4.Similarly,for the solutionof(5.37)wehave the following.

Theorem 5.6.Consideramatrix Liegroup $G$ withLiealgebrag.Then,the solution $Y ( t ) \in { \mathfrak { g } } ^ { * }$ of(5.37)with initial value $Y _ { 0 } \in \mathfrak { g } ^ { * }$ isgiven by

$$
\langle Y ( t ) , X \rangle = \langle Y _ { 0 } , U ( t ) ^ { - 1 } X U ( t ) \rangle \qquad f o r a l l ~ X \in \mathfrak { g } ,
$$

where $U ( t ) \in G$ satisfies

$$
\dot { U } = - H ^ { \prime } ( Y ( t ) ) U , \quad U ( 0 ) = I .
$$

Equation (5.39) can be written as

$$
\begin{array} { r } { Y ( t ) = \operatorname { A d } _ { U ( t ) ^ { - 1 } } ^ { * } Y _ { 0 } , } \end{array}
$$

where $\mathrm { A d } _ { U - 1 } ^ { * }$ is the adjoint of $\mathrm { A d } _ { U - 1 }$ The solution $Y ( t )$ of（5.37)thus lies on the coadjoint orbit

$$
Y ( t ) \in \{ \mathbf { A d } _ { U - 1 } ^ { * } Y _ { 0 } ; U \in G \} .
$$

In coordinates $\begin{array} { r } { Y = \sum _ { j = 1 } ^ { n } y _ { j } F _ { j } } \end{array}$ , we note $y _ { j } = \langle Y _ { 0 } , U ( t ) ^ { - 1 } E _ { j } U ( t ) \rangle .$

Proof.Differentiating the ansatz (5.39) for the solution we obtain

$$
\begin{array} { l l l } { \langle \dot { Y } , X \rangle } & { = } & { \langle Y _ { 0 } , - U ^ { - 1 } \dot { U } U ^ { - 1 } X U + U ^ { - 1 } X \dot { U } \rangle } \\ & { = } & { \langle Y _ { 0 } , U ^ { - 1 } [ X , \dot { U } U ^ { - 1 } ] U \rangle = \langle Y , [ X , \dot { U } U ^ { - 1 } ] \rangle , } \end{array}
$$

where we have used (5.39) in the first and the last equation.This shows that (5.37) is satisfied with the choice $U U ^ { - 1 } = - H ^ { \prime } ( Y )$

Example 5.7 (Rigid Body).The Lie group corresponding to the rigid bodyis SO(3)with the Lie algebra ${ \mathfrak { s o } } ( 3 )$ of skew-symmetric $3 \times 3$ matrices,with the basis

$$
E _ { 1 } = \left( { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 0 } \end{array} } \right) , \quad E _ { 2 } = \left( { \begin{array} { c c c } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \end{array} } \right) , \quad E _ { 3 } = \left( { \begin{array} { c c c } { 0 } & { - 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) .
$$

If we let $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { T }$ be the coordinates of $X \in { \mathfrak { s o } } ( 3 )$ ,thenwe have $X v =$ $x \times v$ forall $\boldsymbol { v } \in \mathbb { R } ^ { 3 }$ Sincefor $U \in \mathrm { S O } ( 3 )$ ,

$$
U ^ { - 1 } X U v = U ^ { - 1 } ( x \times U v ) = U ^ { - 1 } x \times v ,
$$

the vector $U ^ { - 1 } x$ consists of the coordinates of $U ^ { - 1 } X U \in { \mathfrak { s o } } ( 3 )$

Let $y = ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) ^ { T }$ be the coordinates of $Y \in { \mathfrak { s o } } ( 3 ) ^ { * }$ with respect to the dual basis of $E _ { 1 } , E _ { 2 } , E _ { 3 }$ .Since

$$
\langle Y , U ^ { - 1 } X U \rangle = \Big \langle \sum _ { j = 1 } ^ { 3 } y _ { j } F _ { j } , \sum _ { i = 1 } ^ { 3 } ( U ^ { - 1 } x ) _ { i } E _ { i } \Big \rangle = y ^ { T } U ^ { - 1 } x = ( U y ) ^ { T } x ,
$$

the coordinates of $\operatorname { A d } _ { U ^ { - 1 } } Y$ are given by the vector $\ U y .$ Therefore,the coordinates of the coadjoint orbit of $Y$ lieona sphere of radius $\lVert y \rVert$ .The conservation of the coadjoint orbit thus reduces here to the preservation of the Casimir $C ( y ) = y _ { 1 } ^ { 2 } +$ $y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$

Lie-Poisson integrators seem to be have first beenconsidered by Ge&Marsden (1988),who extend the construction of symplectic methods by generating functions toLie-Poisson systems.Channel & Scovel（1991） propose an implementation of these methods based on a coordinatization of the group by the exponential map.

McLachlan （1993）proposes integrators based on spliting the Hamiltonian and illustrates this approach for various examples ofLie-Poisson systems.Whenapplicable,such splittingintegrators yield Poisson integrators that preserve the coadjoint orbits,since they are composed of exact flows ofLie-Poisson systems.

Engg& Faltinsen (2oo1） propose to solve numerically the Lie-Poisson system (5.34)by applying Lie groupintegrators suchas those of Sect.IV.8 to thedifferential equation (5.4O) with(5.39).Thisapproach keeps the solution on the coadjoint orbit byconstruction,but itdoes not,ingeneral,giveaPoisson integrator.

# VII.5.5 Lie-Poisson Reduction

Thereduction of the Hamiltonian equations of motion of the free rigid body to theEuler equations isan instance of a general reduction process from Hamiltonian systems with symmetry on aLie group toLie-Poisson systems,which we now describe;cf.Marsden&Ratiu(1999),Chap.13,forapresentation inamoreabstract framework and for an historical account.

Let us assume that the Lie group $G$ isasubgroup of ${ \mathrm { G L } } ( n )$ givenby

$$
G = \{ Q ; g _ { i } ( Q ) = 0 , i = 1 , \ldots , m \} ,
$$

and consider a Hamiltonian system on $G$ ,

$$
\begin{array} { l l } { \displaystyle \dot { P } ~ = ~ - \nabla _ { Q } H ( P , Q ) - \sum _ { i = 1 } ^ { m } \lambda _ { i } \nabla _ { Q } g _ { i } ( Q ) , \qquad \displaystyle \dot { Q } = \nabla _ { P } H ( P , Q ) } \\ { \displaystyle 0 ~ = ~ g _ { i } ( Q ) , \quad i = 1 , . . . , m , } \end{array}
$$

where $P , Q$ are square matrices,and $\nabla _ { Q } H = \left( \partial H / \partial Q _ { i j } \right) .$ This is of the form discussed in Sect.VII.1.2.In regionswhere thematrix

$$
\left( \frac { \partial ^ { 2 } H ( P , Q ) } { \partial P ^ { 2 } } \left( \nabla _ { Q } g _ { i } ( Q ) , \nabla _ { Q } g _ { j } ( Q ) \right) \right) _ { i , j = 1 } ^ { m } \qquad \mathrm { i s ~ i n v e r t i b l e } ,
$$

theLagrange parameters $\lambda _ { i }$ can be expressed in terms of $P$ and $Q$ (cf.formula (1.13)).Hence,aunique solution exists locally provided the initial values $( P _ { 0 } , Q _ { 0 } )$ are consistent,i.e., $g _ { i } ( Q _ { 0 } ) = 0$ and

$$
\begin{array} { r } { g _ { i } ^ { \prime } ( Q _ { 0 } ) \Big ( \nabla _ { P } H ( P _ { 0 } , Q _ { 0 } ) \Big ) = \operatorname { t r a c e } \Big ( \nabla _ { Q } g _ { i } ( Q _ { 0 } ) ^ { T } \nabla _ { P } H ( P _ { 0 } , Q _ { 0 } ) \Big ) = 0 , } \end{array}
$$

or equivalently, $Q _ { 0 } \in G$ and $\nabla _ { P } H ( P _ { 0 } , Q _ { 0 } ) \in T _ { Q _ { 0 } } G$

Wenow assume that the Hamiltonian $H$ is quadratic in $P$ Aswe have seen in Sect.VII.1.2,the equations(5.43）can be viewed asa differential equationon the cotangent bundle $T ^ { \ast } G = \{ ( P , Q ) ; Q \in G , P \in T _ { Q } ^ { \ast } G \}$ where the cotangent space $T _ { Q } ^ { * G }$ isidentified with asubspace of matrices such that

$$
{ \cal P } \in T _ { Q } ^ { * } G \qquad \mathrm { i f ~ a n d ~ o n l y ~ i f } \qquad \nabla _ { P } H ( P , Q ) \in T _ { Q } G .
$$

Withthis identification,theduality beween $T _ { Q } ^ { * G }$ and $T _ { Q } G$ is given by thematrix inner product

$$
\langle P , V \rangle = \operatorname { t r a c e } \left( P ^ { T } V \right) \quad { \mathrm { ~ f o r ~ } } P \in T _ { Q } ^ { * } G , V \in T _ { Q } G .
$$

Wecall the Hamiltonianleft-invariant,if

$$
H ( U ^ { T } P , U ^ { - 1 } Q ) = H ( P , Q ) \qquad { \mathrm { ~ f o r ~ a l l ~ } } U \in G .
$$

In this case we have $H ( P , Q ) = H ( Q ^ { I } P , I ) $ and by differentiatingwe obtain $\nabla _ { P } H ( P , Q ) = Q \nabla _ { P } H ( Q ^ { I } P , I )$ By(5.45）and since $T _ { Q } G = \{ Q X ; X \in \mathfrak { g } \}$ with the Liealgebra $ { \mathfrak { g } } = T _ { I } G$ (cf.Sect.IV.6),this relation implies

$$
{ \cal P } \in T _ { Q } ^ { * } { \cal G } \qquad \mathrm { i f ~ a n d ~ o n l y ~ i f } \qquad { \cal Q } ^ { T } { \cal P } \in T _ { I } ^ { * } { \cal G } = \mathfrak { g } ^ { * } .
$$

Now $H ( P , Q )$ depends,for $( P , Q ) \in T ^ { * } G$ ,only on the product $Y = Q ^ { T } P \in { \mathfrak { g } } ^ { * }$ ， and wewrite7 $H ( P , Q ) = H ( Y )$ witha function $\boldsymbol { H } : \mathfrak { g } ^ { * }  \mathbb { R }$

Left-invariant Hamiltonian systems can be reduced toa Lie-Poisson system of half the dimension byaprocessthat generalizes the derivation of the Euler equations for the rigid body.

Theorem5.8.Considera Hamiltoniansystem(5.43）ona matrix Liegroup $G$ witha left-invariantquadratic Hamiltonian $H ( P , Q ) = H ( Y )$ for $Y = Q ^ { T } P .$ 1f $( P ( t ) , Q ( t ) ) \in T ^ { * } G$ isasolutionofthesystem(5.43),then $Y ( t ) = Q ( t ) ^ { T } P ( t ) \in \mathfrak { g } ^ { * }$ solvesthedifferentialequation(5.37).

Proof.Itisconvenient for the proof (though not necessary,see the lines following（2.17)）to extend the Hamiltonian $H : { \mathfrak { g } } ^ { * } \ \to \ \mathbb { R }$ toa function of arbitrarymatrices $Y$ bysetting $H ( Y ) ~ = ~ H ( I I Y )$ ,where $\boldsymbol { { \mathit { 1 } } } \boldsymbol { { \mathit { 1 } } }$ is the projection onto ${ \mathfrak { g } } ^ { * }$ given by $\langle I I Y , X \rangle = ( Y , X )$ forall $X ~ \in ~ { \mathfrak { g } }$ ,with the matrix inner product $( Y , X ) = \operatorname { t r a c e } \left( Y ^ { T } X \right)$ .

where Wefirst compute thederivatives of $Q ^ { T } P = Y$ nd $H ( P , Q ) = H ( Y ) = H ( I I Y ) = H ( y )$ $\begin{array} { r } { \pi Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } . } \end{array}$ Since $y _ { j } = \langle \varPi Q ^ { T } P , E _ { j } \rangle = ( Q ^ { T } P , E _ { j } )$ ,it follows from $\nabla _ { A }$ trace $( A ^ { T } B ) = B$ that

$$
7 p H ( P , Q ) = \sum _ { j = 1 } ^ { d } \frac { \partial H ( y ) } { \partial y _ { j } } \nabla _ { P } y _ { j } = \sum _ { j = 1 } ^ { d } \frac { \partial H ( y ) } { \partial y _ { j } } \nabla _ { P } \operatorname { t r a c e } \left( P ^ { T } Q E _ { j } \right) = Q H ^ { \prime } ( Y )
$$

where $\begin{array} { r } { H ^ { \prime } ( Y ) = \sum _ { j = 1 } ^ { d } \frac { \partial H ( y ) } { \partial y _ { j } } E _ { j } \in \mathfrak { g } } \end{array}$ HEj∈gasinTheorem5.5.Using theidentityyj= trace $( P ^ { T } Q E _ { j } ) = \operatorname { t r a c e } { ( Q ^ { T } P E _ { j } ^ { T } ) }$ we get ina similar way

$$
\nabla _ { Q } H ( P , Q ) = P H ^ { \prime } ( Y ) ^ { T } .
$$

Consequently,the differential equations(5.43) become

$$
\dot { P } = - P H ^ { \prime } ( Q ^ { T } P ) ^ { T } - \sum _ { i = 1 } ^ { m } \lambda _ { i } \nabla _ { Q } g _ { i } ( Q ) , \qquad \dot { Q } = Q H ^ { \prime } ( Q ^ { T } P ) .
$$

The product rule $\dot { \boldsymbol { Y } } = \dot { \boldsymbol { Q } } ^ { T } \boldsymbol { P } + \boldsymbol { Q } ^ { T } \dot { \boldsymbol { P } }$ for $Y = Q ^ { T } P$ thus yields

$$
\dot { Y } = \bar { H ^ { \prime } } ( Y ) ^ { T } Y - Y \bar { H ^ { \prime } } ( Y ) ^ { T } - \sum _ { i = 1 } ^ { m } \lambda _ { i } Q ^ { T } \nabla _ { Q } g _ { i } ( Q ) .
$$

For $X \in { \mathfrak { g } }$ ,wenow exploit the properties

$$
\begin{array} { r l } & { \left. Q ^ { T } \nabla _ { Q } g _ { i } ( Q ) , X \right. = \left. \nabla _ { Q } g _ { i } ( Q ) , Q X \right. = 0 \qquad \mathrm { ( b e c a u s e ~ } Q X \in T _ { Q } G ) } \\ & { \left. [ H ^ { \prime } ( Y ) ^ { T } , Y ] , X \right. = \operatorname { t r a c e } \big ( \big ( Y ^ { T } H ^ { \prime } ( Y ) - H ^ { \prime } ( Y ) Y ^ { T } \big ) X \big ) } \\ & { \qquad = \operatorname { t r a c e } \big ( Y ^ { T } \big ( H ^ { \prime } ( Y ) X - X H ^ { \prime } ( Y ) \big ) \big ) = \left. Y , [ H ^ { \prime } ( Y ) , X ] \right. } \end{array}
$$

Since $Y ( t ) \in { \mathfrak { g } } ^ { * }$ for all $t$ ,this gives the equation (5.37).

Reduced Systemand Reconstruction.Combining Theorems5.8and5.5,we have reduced the Hamiltonian system(5.43)to the Lie-Poissonsystem for $\ b { y } ( t ) \in \mathbb { R } ^ { d }$ ,

$$
\begin{array} { r } { \dot { y } = B ( y ) \nabla H ( y ) , } \end{array}
$$

of half the dimension.To recover the full solution $( P ( t ) , Q ( t ) ) \in T ^ { * } G$ ,wemust solve this system alongwith

$$
\begin{array} { r } { { \dot { Q } } = Q H ^ { \prime } ( Y ) , \quad P = Q ^ { - T } Y } \end{array}
$$

where $\begin{array} { r } { Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } \in \mathfrak { g } ^ { * } . } \end{array}$

Poisson Structures.The Poisson bracket on $\mathbb { R } ^ { d }$ defined by $B ( y )$ is still closely relatedtothecanonical Poissonbracketon $\mathbb { R } ^ { 2 n ^ { 2 } } .$ Considerleft-invariantreal-valued functions $K , L$ on ${ \boldsymbol { \mathbf { \mathit { T } } } } ^ { * } { \boldsymbol { \mathbf { \mathit { G } } } }$ Thesecan be viewed as functions on $T ^ { * } G / G = { \mathfrak { g } } ^ { * } \subset$ Rnxn,

$$
K ( P , Q ) = K ( Y ) \mathrm { f o r } Y = Q ^ { T } P .
$$

(Aswe did previously in this section,we use the same symbol for these functions.） Via the projection $\pi : \mathbb { R } ^ { n \times n }  \mathfrak { g } ^ { * }$ used in the above proof,we can extend $K ( Y ) = K ( \varPi Y )$ toarbitrary $n \times n$ matrices $Y$ ,and via theaboverelationtoa left-invariant function $K ( P , Q )$ on $\mathbb { R } ^ { n \times n } \times \mathbb { R } ^ { n \times n }$ ,on which we have the canonical Poisson bracket

$$
\{ K , L \} _ { \mathrm { c a n } } = \sum _ { k , l = 1 } ^ { n } \Big ( \frac { \partial K } { \partial Q _ { k l } } \frac { \partial L } { \partial P _ { k l } } - \frac { \partial K } { \partial P _ { k l } } \frac { \partial L } { \partial Q _ { k l } } \Big ) .
$$

On the other hand,we can view $K$ asa function on $\mathbb { R } ^ { d }$ by choosing coordinates on ${ \mathfrak { g } } ^ { * }$ ,

$$
K ( y ) = K ( Y ) \quad { \mathrm { ~ f o r ~ } } Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } \in { \mathfrak { g } } ^ { * } .
$$

On $\mathbb { R } ^ { d }$ wehavethePoissonbracketdefined bythestructure matrix $B ( y )$ ,

$$
\{ K , L \} = \sum _ { i , j = 1 } ^ { d } \frac { \partial K } { \partial y _ { i } } b _ { i j } \frac { \partial L } { \partial y _ { j } } .
$$

Lemma5.9.Forleft-invariant functions $\begin{array} { r } { Q ^ { T } P = Y = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } \in \mathfrak { g } ^ { * } } \end{array}$ $K , L$ asdescribed above,we have for

$$
\{ K , L \} ( y ) = \langle Y , [ L ^ { \prime } ( Y ) , K ^ { \prime } ( Y ) ] \rangle = \{ K , L \} _ { \mathrm { c a n } } ( P , Q )
$$

where K()=∑(）Eg

Proof.Thefirstequality follows from theidentity

$$
b _ { i j } ( y ) = \left. Y , [ E _ { j } , E _ { i } ] \right. ,
$$

which isa direct consequence of the definition (5.35)with (5.36).For the second equality,therelations (5.48)and(5.49) for $K$ and $L$ yield

$$
\begin{array} { r c l } { \{ K , L \} _ { \mathrm { c a n } } ( P , Q ) } & { = } & { \mathrm { t r a c e } \left( K ^ { \prime } ( Y ) Y ^ { T } L ^ { \prime } ( Y ) - K ^ { \prime } ( Y ) ^ { T } Y L ^ { \prime } ( Y ) ^ { T } \right) } \\ & { = } & { \mathrm { t r a c e } \left( K ^ { \prime } ( Y ) Y ^ { T } L ^ { \prime } ( Y ) - L ^ { \prime } ( Y ) Y ^ { T } K ^ { \prime } ( Y ) \right) } \\ & { = } & { \mathrm { t r a c e } \left( Y ^ { T } [ L ^ { \prime } ( Y ) , K ^ { \prime } ( Y ) ] \right) = \left. Y , [ L ^ { \prime } ( Y ) , K ^ { \prime } ( Y ) ] \right. , } \end{array}
$$

which is the result.

Discrete Lie-Poisson Reduction.Considera symplectic integrator

$$
( P _ { 1 } , Q _ { 1 } ) = \varPhi _ { h } ( P _ { 0 } , Q _ { 0 } ) \qquad \mathrm { o n } \ T ^ { * } G
$$

forthe left-invariant Hamiltonian system (5.43),and suppose that the method preserves the left-invariance:if $\phi _ { h } ( P _ { 0 } , Q _ { 0 } ) = ( P _ { 1 } , Q _ { 1 } )$ ,then

$$
\begin{array} { r } { \varPhi _ { h } ( U ^ { T } P _ { 0 } , U ^ { - 1 } Q _ { 0 } ) = ( U ^ { T } P _ { 1 } , U ^ { - 1 } Q _ { 1 } ) \mathrm { ~ f o r ~ a l l ~ } U \in G . } \end{array}
$$

Forexample,this is satisfied by theRATTLEalgorithm.Themethod then induces a one-stepmap

$$
Y _ { 1 } = \varPsi _ { h } ( Y _ { 0 } ) \qquad { \mathrm { o n ~ } } \mathfrak { g } ^ { * }
$$

bysetting $Y _ { 1 } = Q _ { 1 } ^ { \prime } P _ { 1 }$ for $( P _ { 1 } , Q _ { 1 } ) = \varPhi _ { h } ( P _ { 0 } , Q _ { 0 } )$ with $Q _ { 0 } ^ { I } P _ { 0 } = Y _ { 0 }$ Thisisa numerical integrator for(5.37),and inthe coordinates $y = ( y _ { j } )$ with respect to the basis $( F _ { j } )$ of ${ \mathfrak { g } } ^ { * }$ this gives amap

$$
y _ { 1 } = \psi _ { h } ( y _ { 0 } ) \qquad \mathrm { o n } ~ \mathbb { R } ^ { d } ,
$$

which isanumerical integrator for the Poisson system (5.52).

Example5.10.For therigid body,applyingthe RATTLE algorithm to theconstrained Hamiltonian system (5.18）yields theintegrator for the Euler equations discussed in Sect.VII.5.3.By the followingresult thisisaPoisson integrator.

Theorem 5.11.1f $\varPhi _ { h } ( P , Q )$ isasymplecticand left-invariant integrator for(5.43), thenitsreduction $\psi _ { h } ( y )$ isa Poisson map.

ProofWewrite $\psi _ { h }$ as the composition

$$
\psi _ { h } : \mathbb { R } ^ { d } \xrightarrow { \xi } T ^ { * } G \xrightarrow { \phi _ { h } } T ^ { * } G \xrightarrow { \eta } \mathbb { R } ^ { d }
$$

were $\eta = ( \eta _ { j } )$ iste unetic $\eta _ { j } ( P , Q ) = y _ { j }$ for $\begin{array} { r } { Q ^ { T } P = \sum _ { j = 1 } ^ { d } y _ { j } F _ { j } } \end{array}$ and $\xi$ $\eta$ $\eta \circ \xi = \operatorname { i d }$   
$K , L$ on $\mathbb { R } ^ { d }$ we then have for $( P , Q ) = \xi ( y )$ ,usingLemma5.9intheouter equalities   
and the symplecticity of $\phi _ { h }$ in themiddle equality,

$$
\begin{array} { r c l } { [ K \circ \psi _ { h } , L \circ \psi _ { h } \} ( y ) } & { = } & { \{ K \circ \eta \circ \varPhi _ { h } , L \circ \eta \circ \varPhi _ { h } \} _ { \mathrm { c a n } } ( P , Q ) } \\ & { = } & { \{ K \circ \eta , L \circ \eta \} _ { \mathrm { c a n } } \big ( \varPhi _ { h } ( P , Q ) \big ) = \{ K , L \} \big ( \psi _ { h } ( y ) \big ) . } \end{array}
$$

This equation states that $\psi _ { h }$ is a Poisson map.

Asimilar reduction inadiscrete Lagrangian framework is studied byMarsden, Pekarsky&Shkoller（1999).

Thereduced numerical maps $\psi _ { h }$ and $\psi _ { h }$ have further structure-preserving properties:they preserve the Casimirs and the co-adjoint orbits.Thiswill be shown in Sect.IX.5.3with the help of backward error analysis.

# VII.6 Reduced Models of Quantum Dynamics

Toincorporate quantum effects in molecular dynamics simulations,computations aredonewith models that are intermediate between classical moleculardynamicsbased on Newton'sequations of motion and full quantum dynamics described bythe $N$ -particle Schrodinger equation.Thedirect computational treatment of the latteris not feasible because of its high dimensionality.These intermediate modelsareobtained by the Hamiltonian reduction(2.17） froman infinite-dimensional Hilbert space to an appropriately chosen manifold.In chemical physics,thisreductionisknownas the Dirac-Frenkel time-dependent variational principle.We illustrate this procedure for the case where the quantum-mechanical wave function isapproximated byacomplex Gaussian as proposed by Heller(1975).It turns out that the resulting ordinary differential equations have a Poisson structure,which wasrecently described by Faou&Lubich(2Oo4).Followingthat paper,we derive astructure-preserving explicit integrator for Gaussian wavepackets,which tends to theStormer-Verletmethod in theclassical limit.

# VII.6.1 Hamiltonian Structure of the Schrodinger Equation

The introduction of wave mechanics stands..as Schrodinger's monument and aworth one. (From Schrodinger's obituary inTheTimes1961:quoted from http://www-groups.dcs.st-and.ac.uk/history/Mathematicians/Schrodinger.html)

The time-dependent $\mathcal { N }$ -body Schrodinger equation reads (see,e.g.,Messiah (1999) and Thaller (2000))

$$
i \varepsilon { \frac { \partial { \psi } } { \partial t } } = H { \psi }
$$

for the wave function $\psi ~ = ~ \psi ( x , t )$ depending on the spatial variables $x =$ $( x _ { 1 } , \ldots , x _ { N } )$ with $x _ { k } \in \mathbb { R } ^ { d }$ (e.g.,with $d = 1$ or3in the partition）and the time $t \in \mathbb { R } .$ The squared absolute value $| \psi ( x , t ) | ^ { 2 }$ represents the joint probability density for $N$ particles to beat the positions $\mathcal { L } _ { 1 } , \ldots , \mathcal { L } _ { N }$ attime $t .$ In(6.1）, $\boldsymbol { \varepsilon }$ isa(small) positive number representing the scaled Planck constant and $i$ is thecomplex imaginary unit.The Hamiltonian operator $H$ iswritten

$$
H = T + V
$$

with the kinetic and potential energy operators

$$
T = - \sum _ { k = 1 } ^ { N } \frac { \varepsilon ^ { 2 } } { 2 m _ { k } } \varDelta _ { x _ { k } } \quad \mathrm { a n d } \quad V = V ( x ) ,
$$

where $m _ { k } > 0$ isa particle mass and $\varDelta _ { x _ { k } }$ the Laplacianin the variable $\boldsymbol { x } _ { k } \in \mathbb { R } ^ { d }$ , and where the real-valued potential $V$ acts asa multiplication operator $( V \phi ) ( x ) =$ $V ( x ) \phi ( x )$ .Underappropriate conditionson $V$ （boundedness of $V$ issufficient, butbynomeans necessary）,the operator $H$ is thena self-adjoint operator on thecomplex Hilbert space $L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { C } )$ with domain ${ \cal D } ( H ) = { \cal D } ( T ) = \{ \phi \in$ $L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { C } )$ $T \phi \in L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { C } ) \}$ ;see Sect.V.5.3ofKato(1980).

We separate thereal and imaginary parts of $\psi = v + i w \in L ^ { 2 } ( \mathbb R ^ { d N } , \mathbb C )$ ,the complexHilbert space ofLebesgue square-integrable functions.Thefunctions $v$ and $w$ arethus functions in thereal Hilbert space $L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { R } )$ .We denote the complex inner product by $\langle \cdot , \cdot \rangle$ and the real inner product by $( \cdot , \cdot )$ .The $L ^ { 2 }$ normswill be simply denoted by $\| \cdot \|$

As $H$ isareal operator,formula(6.1） can bewritten

$$
\begin{array} { r c l } { { \varepsilon \dot { v } } } & { { = } } & { { H w , } } \\ { { \varepsilon \dot { w } } } & { { = } } & { { - H v , } } \end{array}
$$

orequivalently,with the canonical structure matrix

$$
J = \left( \begin{array} { c c } { 0 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right)
$$

and the Hamiltonian function (we use the same symbol $H$ as for the operator)

$$
H ( v , w ) = \frac { 1 } { 2 } \langle \psi , H \psi \rangle = \frac { 1 } { 2 } ( v , H v ) + \frac { 1 } { 2 } ( w , H w )
$$

for $\psi = v + i w$ in the domain of the operator $H$ .This becomes the canonica Hamiltonian system

$$
\left( \begin{array} { l } { \dot { v } } \\ { \dot { w } } \end{array} \right) = \varepsilon ^ { - 1 } J ^ { - 1 } \nabla H ( v , w ) .
$$

Note that the real multiplication with $J$ corresponds to the complex multiplication with the imaginary unit $i$ .The flow of this system preserves the canonical symplectic two-form

$$
\omega ( \xi _ { 1 } , \xi _ { 2 } ) = ( J \xi _ { 1 } , \xi _ { 2 } ) , \qquad \xi _ { 1 } , \xi _ { 2 } \in L ^ { 2 } ( \mathbb { R } ^ { d N } , \mathbb { R } ) ^ { 2 } .
$$

# VII.6.2 TheDirac-Frenkel Variational Principle

Fordealingwith atoms involvingmany electrons the accurate quantum theory,involvinga solution of thewave equation in many-dimensional space,is far too complicated to bepracticable.One must therefore resort toapproximate methods. (P.A.M.Dirac 1930)

Reduced models of the Schrodinger equation are obtained by restricting theequation toanapproximationmanifold $\mathcal { M }$ via (2.17),viz.,

$$
\begin{array} { r } { ( \varepsilon J \dot { \boldsymbol { u } } - \nabla H ( \boldsymbol { u } ) , \boldsymbol { \xi } ) = 0 \qquad \mathrm { f o r ~ a l l } \quad \boldsymbol { \xi } \in T _ { \boldsymbol { u } } \mathcal { M } , } \end{array}
$$

or equivalently in complex notation for $u = ( v , w ) ^ { T } = v + i w ,$

$$
\begin{array} { r } { \mathrm { { R e } } \left. \varepsilon i \dot { u } - H u , \xi \right. = 0 \qquad \mathrm { { f o r \ a l l } } \quad \xi \in T _ { u } \mathcal { M } . } \end{array}
$$

Taking thereal part can be omitted if the tangent space $\boldsymbol { T _ { u } } \boldsymbol { M }$ is complex linear. Equation(6.5）（usuallywithout thereal part） isknown astheDirac-Frenkel timedependentvariational principle,afterDirac（193O)andFrenkel （1934)；seealso McLachlan（1964),Heller（1976),Beck,Jackle,Worth&Meyer(2000),and references therein.

Wechoose a (local) coordinate map $u = \chi ( y )$ of $\mathcal { M }$ and denote its derivative $X _ { \mathbb { C } } ( y ) = V ( y ) + i W ( y ) = \chi ^ { \prime } ( y )$ or in the real setting as $X = { \binom { V } { W } } .$ Denoting by $X ^ { T }$ theadjoint of $X$ withrespect to the real inner product $( \cdot , \cdot )$ ,we thus obtain

$$
\varepsilon X ( y ) ^ { T } J X ( y ) \dot { y } = X ( y ) ^ { T } \nabla _ { u } H ( \chi ( y ) ) .
$$

With $X _ { \mathbb { C } } ^ { * }$ denoting the adjoint of $X _ { \mathbb { C } }$ with respect to the complex inner product $\langle \cdot , \cdot \rangle$ , wenote $X _ { \mathbb { C } } ^ { * } X _ { \mathbb { C } } = ( V ^ { T } V + W ^ { T } W ) + i ( V ^ { T } W - W ^ { T } V ) = X ^ { T } X - i X ^ { T } J X$ and hence

$$
X ^ { T } J X = - \mathrm { I m } X _ { \mathbb { C } } ^ { * } X _ { \mathbb { C } } .
$$

Lemma 6.1.If $x _ { u } M$ isacomplex linear space forevery $u \in \mathcal { M }$ ,then $\mathcal { M }$ is $^ a$ symplectic submanifoldof $L ^ { 2 } ( \mathbb { R } ^ { N } , \mathbb { R } ) ^ { 2 }$ ,thatis,the symplectic two-form(6.3)is non-degenerate on $\boldsymbol { x } _ { u } \boldsymbol { \mathcal { M } }$ for all $u \in \mathcal { M }$ Expressedin coordinates,

$$
X ( y ) ^ { T } J X ( y ) \ i s \ i n \nu e r t i b l e f o r \ a l l \ y .
$$

Proof.Wefix $u = x ( y ) \in \mathcal { M }$ and omit the argument $y$ in the following. Since $T _ { u } { \mathcal { M } } = \mathop { \mathrm { R a n g e } } ( X _ { \mathbb { C } } )$ iscomplex linear byassumption,there existsa real linear mapping $L : \mathbb { R } ^ { m }  \mathbb { R } ^ { m }$ such that $i X _ { \mathbb { C } } \eta = X _ { \mathbb { C } } L \eta$ forall $\eta \in \mathbb { R } ^ { m } .$ This implies

$$
J X = X L \quad { \mathrm { a n d } } \quad L ^ { 2 } = - \operatorname { I d }
$$

and hence $X ^ { T } J X = X ^ { T } X L$ which is invertible.

Approximation properties of the Dirac-Frenkel variational principlecan beobtained fromthe interpretationas the orthogonal projection $\begin{array} { r } { \dot { u } = P _ { \perp } ( u ) \frac { 1 } { i \varepsilon } H u . } \end{array}$ which corresponds to taking the imaginary part in (6.5),as opposed to the symplectic projectionin(6.4）whichcorrespondsto thereal part.SeeLubich (2oo5) foranearoptimality result forapproximation on the manifold.

# VII.6.3 Gaussian Wavepacket Dynamics

Wedevelopa new approach to semiclassical dynamicswhich exploits the factthat extended wavefunctions for heavyparticles (orparticles inharmonicpotentials)may be decomposed into time-dependent wave packets,which spread minimally and which execute classical or nearly classicaltrajectories.AGaussian form for the wave packetsisassumed and equations of motion are derived for the parameters characterizing the Gaussian. (E.J.Heller1975)

Thevariational Gaussian wavepacket dynamics of Heller（1976) is obtained by choosing the manifold $\mathcal { M }$ in(6.5）as consisting of complex Gaussians.For ease ofpresentation we restrict our attention in the following to the one-particle case $N = 1$ （the extension to $N > 1$ isstraightforward;cf.Heller（1976）and Faou& Lubich(2004)).Herewe have

$$
\mathcal { M } = \{ u = \chi ( y ) \in L ^ { 2 } ( \mathbb { R } ^ { d } , \mathbb { C } ) : y = ( p , q , \alpha , \beta , \gamma , \delta ) \in \mathbb { R } ^ { 2 d + 4 } \mathrm { ~ w i t h ~ } \beta > 0 \}
$$

with

$$
\Big ( \chi ( y ) \Big ) ( x ) = \exp \Big ( \frac { i } { \varepsilon } \big ( ( \alpha + i \beta ) | x - q | ^ { 2 } + p \cdot ( x - q ) + \gamma + i \delta \big ) \Big ) ,
$$

where $| \cdot |$ and·stand for the Euclidean norm and inner product on $\mathbb { R } ^ { d }$ Theparameters $q$ and $p$ represent the average position and momentum,respectively:for $u = \chi ( y )$ with $\boldsymbol { y } = ( p , q , \alpha , \beta , \gamma , \delta )$ and $\lVert u \rVert = 1$ ,adirect calculation shows that

$$
q = \langle u , x u \rangle = \int _ { \mathbb { R } ^ { d } } x | u ( x ) | ^ { 2 } d x , \qquad p = \langle u , - i \varepsilon \nabla u \rangle .
$$

Theparameter $\beta > 0$ determines thewidth of the wavepacket.The tangent space $T _ { u } \mathcal { M } \subset L ^ { 2 } ( \mathbb { R } ^ { d } , \mathbb { C } )$ at a given point $u = \chi ( y ) \in \mathcal { M }$ is $( 2 d + 4 )$ -dimensional and is made of the elements of $L ^ { 2 } ( \mathbb { R } ^ { d } , \mathbb { C } )$ written as

$$
{ \frac { i } { \varepsilon } } { \Bigl ( } ( A + i B ) | x - q | ^ { 2 } + ( P - 2 ( \alpha + i \beta ) Q ) \cdot ( x - q ) - p \cdot Q + C + i D { \Bigr ) } u
$$

with arbitrary $( P , Q , A , B , C , D ) ^ { T } \in \mathbb { R } ^ { 2 d + 4 } .$ Wenote that $x _ { u } M$ is complex linear, and $u \in T _ { u } { \mathcal { M } } .$ Bychoosing $\xi = i u$ in(6.5),this yields $( d / d t ) \| u \| ^ { 2 } = 2 \operatorname { R e } \left. \dot { u } , u \right. =$ O and hence the preservation of the squared $L ^ { 2 }$ normof $u = \chi ( y )$ ,which is given by

$$
\begin{array} { l l l } { { I ( y ) } } & { { = } } & { { \displaystyle \| u \| ^ { 2 } = \int _ { \mathbb R ^ { d } } \lvert u ( x ) \rvert ^ { 2 } d x } } \\ { { } } & { { = } } & { { \displaystyle \int _ { \mathbb R ^ { d } } \exp \left( - \frac 2 { \varepsilon } \bigl ( \beta \lvert x - q \rvert ^ { 2 } + \delta \bigr ) \right) d x = \exp \left( - \frac { 2 \delta } { \varepsilon } \right) \left( \frac { \pi \varepsilon } { 2 \beta } \right) ^ { d / 2 } . } } \end{array}
$$

The physically reasonable situation is $\| u \| ^ { 2 } = 1$ ,which corresponds to the interpretation of $\vert u ( x ) \vert ^ { 2 }$ asaprobability density.

With these preparations we have the following result of Faou&Lubich (2004).

Theorem6.2. TheHamiltonianreductionoftheSchrodingerequationtotheGaussian wavepacket manifold $\mathcal { M }$ of(6.7)-(6.8)yieldsthePoissonsystem

$$
\dot { y } = B ( y ) \nabla K ( y )
$$

where,for $y = ( p , q , \alpha , \beta , \gamma , \delta ) \in \mathbb { R } ^ { 2 d + 4 }$ with $\beta > 0$ ,andwith $1 _ { d }$ denoting the $d$ -dimensionalidentity,

$$
B ( y ) = \frac { 1 } { I ( y ) } \left( \begin{array} { c c c c c c } { 0 } & { - 1 _ { d } } & { 0 } & { 0 } & { - p } & { 0 } \\ { 1 _ { d } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \frac { 4 \beta ^ { 2 } } { \epsilon d } } & { 0 } & { - \beta } \\ { 0 } & { 0 } & { - \frac { 4 \beta ^ { 2 } } { \epsilon d } } & { 0 } & { \beta } & { 0 } \\ { p ^ { T } } & { 0 } & { 0 } & { - \beta } & { 0 } & { \frac { d + 2 } { 4 } \varepsilon } \\ { 0 } & { 0 } & { \beta } & { 0 } & { - \frac { d + 2 } { 4 } \varepsilon } & { 0 } \end{array} \right)
$$

definesaPoissonstructure,andfor $u = \chi ( y )$ ，

$$
K ( y ) = \langle u , H u \rangle = K _ { T } ( y ) + K _ { V } ( y )
$$

isthetotalenergywithineticndpotentialpts

$$
K _ { T } ( y ) = I ( y ) \left( \frac { | p | ^ { 2 } } { 2 m } + \frac { \varepsilon d } { 2 m } \frac { \alpha ^ { 2 } + \beta ^ { 2 } } { \beta } \right) = \langle u , T u \rangle
$$

and

$$
K _ { V } ( y ) = \int _ { \mathbb { R } ^ { d } } V ( x ) \exp \Big ( - \frac { 2 } { \varepsilon } \big ( \beta | x - q | ^ { 2 } + \delta \big ) \Big ) d x = \langle u , V u \rangle .
$$

Both $K ( y )$ and $I ( y )$ arefirstintegralsofthe system.

Proofsi $y$ is $\begin{array} { r } { \varepsilon X ( y ) ^ { T } J X ( y ) \dot { y } = \frac { 1 } { 2 } \nabla K ( y ) . } \end{array}$ Wenote (6.6)and

$$
X _ { \mathbb { C } } ( y ) = \frac { i } { \varepsilon } \left( x - q , - 2 a ( x - q ) - p , | x - q | ^ { 2 } , i | x - q | ^ { 2 } , 1 , i \right) u
$$

where $a = \alpha + \ i \beta$ and $u = \chi ( y )$ in the complex seting.Using the calculus of Gaussian integrals,we compute

$$
\small \begin{array} { r } { \zeta ^ { T } ( y ) J X ( y ) = \displaystyle { \frac { 1 } { 2 } } I ( y ) \left( \begin{array} { c c c c c c } { 0 } & { 1 _ { d } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { - 1 _ { d } } & { 0 } & { 0 } & { \frac { d p } { 2 \beta } } & { 0 } & { \frac { 2 p } { \varepsilon } } \\ { 0 } & { 0 } & { 0 } & { - \frac { \varepsilon d ( d + 2 ) } { 8 \beta ^ { 2 } } } & { 0 } & { - \frac { d } { 2 \beta } } \\ { 0 } & { - \frac { d p ^ { T } } { 2 \beta } } & { \frac { \varepsilon d ( d + 2 ) } { 8 \beta ^ { 2 } } } & { 0 } & { \frac { d } { 2 \beta } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - \frac { d } { 2 \beta } } & { 0 } & { - \frac { 2 } { \varepsilon } } \\ { 0 } & { - \frac { 2 p ^ { T } } { \varepsilon } } & { \frac { d } { 2 \beta } } & { 0 } & { \frac { 2 } { \varepsilon } } & { 0 } \end{array} \right) , } \end{array}
$$

and inversion yields the differential equation with $B ( y ) = ( 2 \varepsilon X ^ { T } ( y ) J X ( y ) ) ^ { - 1 }$ as stated.The system isa Poisson system by Theorem 2.8.

Assuming $I ( y ) = \| u \| ^ { 2 } = 1$ ,weobserve thatthedifferential equationsfor the average position and momentum, $q$ and $p$ ,read

$$
\begin{array} { r } { \dot { q } = p / m , \qquad \dot { p } = - \langle u , \nabla V u \rangle } \end{array}
$$

for $u = \chi ( y )$ and $\boldsymbol { y } = ( p , q , \alpha , \beta , \gamma , \delta ) ,$ We then note $\langle u , \nabla V u \rangle \to \nabla V ( q )$ as $\varepsilon  0$ Thedifferential equations for $q$ and $p$ thus tend to Newtonian equations of motion in the classical limit $\varepsilon  0$ ：

$$
\dot { q } = p / m , \qquad \dot { p } = - \nabla V ( q ) .
$$

It will be useful to consider also scaled variables

$$
\widehat { \boldsymbol { y } } = \left( \boldsymbol { p } , \boldsymbol { q } , \alpha , \widehat { \beta } , \gamma , \widehat { \delta } \right) \in \mathbb { R } ^ { 2 d + 4 } \qquad \mathrm { w i t h } \quad \widehat { \beta } = \frac { \beta } { \varepsilon } , \widehat { \delta } = \frac { \delta } { \varepsilon } .
$$

Herewe have

$$
\dot { \widehat { \boldsymbol { y } } } = \widehat { \boldsymbol { B } } ( \widehat { \boldsymbol { y } } ) \nabla \widehat { \boldsymbol { K } } ( \widehat { \boldsymbol { y } } )
$$

where the structure matrix $\widehat { B } ( \widehat { y } )$ is independent of $\boldsymbol { \varepsilon }$ and where $\widehat { K } ( \widehat { \boldsymbol { y } } )$ depends regularlyon $\varepsilon \geq 0$

# VII.6.4 A Splitting Integrator for Gaussian Wavepackets

With the natural splitting $H = T + V$ into kineticand potential energy,we now consider the variational splittingintegrator(4.7)-(4.8),which here becomes the following.

1.We define $u _ { n } ^ { + }$ in $\mathcal { M }$ as the solution at time $h / 2$ of the equation for $u$ ,

$$
\langle i \varepsilon { \dot { u } } - V u , \xi \rangle = 0 \mathrm { ~ f o r ~ a l l ~ } \xi \in T _ { u } { \mathcal { M } }
$$

with initial value $u ( 0 ) = u _ { n } \in \mathcal { M }$

2.We define $u _ { n + 1 } ^ { - }$ as the solution at time $h$ of

$$
\langle i \varepsilon { \dot { u } } - T u , \xi \rangle = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \xi \in T _ { u } { \mathcal { M } }
$$

with initial value $u ( 0 ) = u _ { n } ^ { + }$

3. Then $u _ { n + 1 }$ is te solution at time $h / 2$ of (6.18) with initial value $u ( 0 ) = u _ { n + 1 } ^ { - }$

By Theorem 6.2,the substeps in thedefinition of this splitting method writen in the coordinates $\boldsymbol { y } = ( p , q , \alpha , \beta , \gamma , \delta )$ are the exact flows $\varphi _ { h / 2 } ^ { V }$ and $\varphi _ { h } ^ { T }$ of the Poisson systems

$$
\dot { \boldsymbol { y } } = B ( \boldsymbol { y } ) \nabla K _ { V } ( \boldsymbol { y } ) \quad \mathrm { ~ a n d ~ } \quad \dot { \boldsymbol { y } } = B ( \boldsymbol { y } ) \nabla K _ { T } ( \boldsymbol { y } ) .
$$

Note that both equations preserve the $L ^ { 2 }$ norm of $u = \chi ( y )$ ,which we assume to be 1 in the following.

Most remarkably,these equations can be solved explicitly.Let us consider first the equations (6.19).They are written,for $a = \alpha + i \beta$ and $c = \gamma + i \delta$ ,as

$$
\left\{ \begin{array} { r c l l c l } { \dot { q } } & { = } & { p / m , } & { } & { \begin{array} { r c l l c r } { \dot { a } } & { = } & { - 2 a ^ { 2 } / m , } & { } & { } \\ { \dot { \hat { c } } } & { = } & { \left( \frac { 1 } { 2 } | p | ^ { 2 } + i \varepsilon d a \right) / m , } \end{array} } \end{array} \right.
$$

with initial values $y _ { 0 } = ( p _ { 0 } , q _ { 0 } , a _ { 0 } , c _ { 0 } )$ corresponding to $u _ { 0 } = \chi ( y _ { 0 } ) .$ They have the solution

$$
q ( t ) = q _ { 0 } + \frac { t } { m } p _ { 0 } , \qquad p ( t ) = p _ { 0 } , \qquad a ( t ) = \frac { a _ { 0 } } { 1 + 2 a _ { 0 } t / m } ,
$$

and

$$
c ( t ) = c _ { 0 } + t \frac { | p _ { 0 } | ^ { 2 } } { 2 m } + \frac { i \varepsilon d } 2 \log \left( 1 + \frac { 2 a _ { 0 } t } m \right) ,
$$

Let usnow consider the equations (6.18).Taking into account the fact that the potential $V$ isreal,theseequations arewritten

$$
\begin{array} { r l r } & { \dot { p } = - \langle { u } , \nabla { V } { u } \rangle , \quad } & { \dot { q } = 0 , } \\ & { \dot { \alpha } = - \frac { 1 } { 2 d } \langle { u } , \Delta { V } { u } \rangle , \quad } & { \dot { \beta } = 0 , } \\ & { \dot { \gamma } = - \langle { u } , { V } { u } \rangle + \frac { \epsilon } { 8 \beta } \langle { u } , \Delta { V } { u } \rangle , \quad } & { \dot { \delta } = 0 , } \end{array}
$$

with the $L ^ { 2 }$ inner products

$$
\langle u , W u \rangle = \int _ { \mathbb { R } ^ { d } } W ( x ) \exp { \Big ( } - { \frac { 2 } { \varepsilon } } { \big ( } \beta | x - q | ^ { 2 } + \delta { \big ) } { \Big ) } d x
$$

for $W = V , \nabla V , \Delta V .$ Asthe $L ^ { 2 }$ inner products in the equations for $p$ , $\alpha$ , $\gamma$ depend onlyon $q , \beta , \delta$ which are constant along this trajectory,these equations can be solved til $\varPhi _ { h } = \varphi _ { h / 2 } ^ { V } \circ \varphi _ { h } ^ { T } \circ \varphi _ { h / 2 } ^ { V }$   
Thisgives thefollowingalgorithm(Faou&Lubich 2004).

Algorithm6.3(Gaussian Wavepacket Integrator).A stepfrom time $t _ { n }$ to $t _ { n + 1 }$ starting fromthe Gaussian wavepacket $u _ { n } = \chi ( p _ { n } , q _ { n } , \alpha _ { n } , \beta _ { n } , \gamma _ { n } , \delta _ { n } )$ proceedsas follows:

1.With $\langle W \rangle _ { n } = \langle u _ { n } , W u _ { n } \rangle$ given by(6.22)for $W = V , \nabla V , \Delta V$ compute

$$
\begin{array} { r c l } { { p _ { n + 1 / 2 } } } & { { = } } & { { p _ { n } - { \displaystyle \frac { h } { 2 } } \langle \nabla V \rangle _ { n } } } \\ { { } } & { { } } & { { } } \\ { { \alpha _ { n } ^ { + } } } & { { = } } & { { \alpha _ { n } - { \displaystyle \frac { h } { 4 d } } \langle \Delta V \rangle _ { n } } } \\ { { } } & { { } } & { { } } \\ { { \gamma _ { n } ^ { + } } } & { { = } } & { { \gamma _ { n } + { \displaystyle \frac { h \varepsilon } { 1 6 \beta _ { n } } } \langle \Delta V \rangle _ { n } . } } \end{array}
$$

2.From the values $p _ { n + 1 / 2 }$ ， $a _ { n } ^ { + } = \alpha _ { n } ^ { + } + i \beta _ { n }$ and $c _ { n } ^ { + } = \gamma _ { n } ^ { + } + i \delta _ { n }$ compute $q _ { n + 1 }$ ， $a _ { n + 1 } ^ { - } = \alpha _ { n + 1 } ^ { - } + i \beta _ { n + 1 } ,$ and $c _ { n + 1 } ^ { - } = \gamma _ { n + 1 } ^ { - } + i \delta _ { n + 1 } \nu i a$

$$
\begin{array} { r c l } { { q _ { n + 1 } } } & { { = } } & { { q _ { n } + { \displaystyle \frac { h } { m } } p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { } } \\ { { \dot { a } _ { n + 1 } ^ { - } } } & { { = } } & { { { \displaystyle a _ { n } ^ { + } } \Big / \Big ( 1 + { \displaystyle \frac { 2 h } { m } } a _ { n } ^ { + } \Big ) } } \\ { { } } & { { } } & { { } } \\ { { c _ { n + 1 } ^ { - } } } & { { = } } & { { c _ { n } ^ { + } + { \displaystyle \frac { i \varepsilon d } { 2 } } \log \Big ( 1 + { \displaystyle \frac { 2 h } { m } } a _ { n } ^ { + } \Big ) . } } \end{array}
$$

3.Compute $p _ { n + 1 } , \alpha _ { n + 1 } , \gamma _ { n + 1 } f r o m$

$$
\begin{array} { r c l } { \displaystyle p _ { n + 1 } } & { = } & { \displaystyle p _ { n + 1 / 2 } - \frac { h } { 2 } \langle \nabla V \rangle _ { n + 1 } } \\ { \displaystyle \alpha _ { n + 1 } } & { = } & { \displaystyle \alpha _ { n + 1 } ^ { - } - \frac { h } { 4 d } \langle \varDelta V \rangle _ { n + 1 } } \\ { \gamma _ { n + 1 } } & { = } & { \displaystyle \gamma _ { n + 1 } ^ { - } + \frac { h \varepsilon } { 1 6 \beta _ { n + 1 } } \langle \varDelta V \rangle _ { n + 1 } . } \end{array}
$$

Let us collect properties of this algorithm.

Theorem6.4.The splittingschemeofAlgorithm6.3isanexplicit,symmetric, second-order numerical methodforGaussianwavepacketdynamics(6.11)-(6.13). ItisaPoissonintegratorforthe structurematrix(6.12),andit preservestheunit $L ^ { 2 }$ normof the wavepackets: $\| u _ { n } \| = 1$ forall $_ { n }$ .

Inthe limit $\varepsilon  0$ ,theposition andmomentum approximations $q _ { n }$ , $p _ { n }$ ofthis methodtendtothoseobtainedbyapplyingthe Stormer-Verletmethodtotheassociatedclassical mechanical system(6.15).

Thestatement for $\varepsilon  0$ follows directly from theequations for $_ { p _ { n + 1 / 2 } }$ ， $q _ { n + 1 }$ $p _ { n + 1 }$ and from noting $\langle \nabla V \rangle _ { n } \to \nabla V ( q _ { n } )$

Inview of the small parameter $\boldsymbol { \varepsilon }$ ,thediscussion of the order of the method requires morecare.Here it isuseful toconsider the integrator in the scaled variables $\boldsymbol { \widehat { y } } = ( p , q , \alpha , \beta / \varepsilon , \gamma , \delta / \varepsilon )$ of(6.16).Since the differential equation(6.17) contains $\in$ onlyasaregularperturbation parameter,after $_ { n }$ steps of the splitting integrator we havethe $\varepsilon$ -uniformerrorbound

$$
{ \widehat { y } } _ { n } - { \widehat { y } } ( t _ { n } ) = O ( h ^ { 2 } ) ,
$$

where the constants symbolized by the $O$ -notationare independentof $\boldsymbol { \varepsilon }$ andof $n$ and $h$ with $n h \leq$ Const.For the approximation of the absolute values of the Gaussian wavepackets thisyields

$$
\left| \left| u _ { n } \right| ^ { 2 } - | u ( t _ { n } ) | ^ { 2 } \right| = O ( h ^ { 2 } ) ,
$$

but the approximation of the phases is only such that

$$
\| u _ { n } - u ( t _ { n } ) \| = O ( h ^ { 2 } / \varepsilon ) .
$$

Wereferto Faou $\&$ Lubich(2oo4）for the formulation of the correspondingalgorithmfor $N > 1$ particles,for further properties such as the exact conservation oflinear and angular momentum and the long-time near-conservation of the total energy $\{ u _ { n } , H u _ { n } \}$ ,and for numerical experiments.

# VII.7 Exercises

1.Prove that the Poisson bracket (2.8) satisfies the Jacobi identity(2.4) for all functions $F , G , H$ ,ifand onlyif it satisfies(2.4) for thecoordinate functions $y _ { i } , y _ { j } , y _ { k }$

Hint(F.Engel,inLie'sGesammelteAbh.vol.5,p.753).IftheJacobi identityis writtenasin(3.3）,we see that there are no second partial derivatives of $F ^ { \prime }$ (the lefthand sideisaLie bracket,theright-hand sidehasno second derivativesof $F$ anyway).Other permutations show the same result for $G$ and $H$ .

2.For $x$ in an open subset of $\mathbb { R } ^ { m }$ ,let $A ( x ) = { \bigl ( } a _ { i j } ( x ) { \bigr ) }$ bean invertible skewsymmetric $m \times m$ -matrix,with

$$
{ \frac { \partial a _ { i j } } { \partial x _ { k } } } + { \frac { \partial a _ { k i } } { \partial x _ { j } } } + { \frac { \partial a _ { j k } } { \partial x _ { i } } } = 0 \qquad { \mathrm { f o r ~ a l l ~ } } i , j , k .
$$

（a）Show that $B ( x ) = A ( x ) ^ { - 1 }$ satisfies(2.1O)and hence definesa Poisson bracket.   
(b) Generalize Theorem 2.8 to Hamiltonian equations(2.18)with the two-form $\omega _ { x } ( \xi _ { 1 } , \xi _ { 2 } ) = \xi _ { 1 } ^ { I } A ( x ) \xi _ { 2 }$ ,   
Remark.Condition(7.1） says that $\omega$ isa closed differential form.

3.Solve the following first order partial differential equation:

$$
3 { \frac { \partial F } { \partial y _ { 1 } } } + 2 { \frac { \partial F } { \partial y _ { 2 } } } - 5 { \frac { \partial F } { \partial y _ { 3 } } } = 0 .
$$

Result. $f ( 2 y _ { 1 } - 3 y _ { 2 } , 5 y _ { 2 } + 2 y _ { 3 } )$

4.Find two solutions of the homogeneous system

$$
3 \frac { \partial F } { \partial y _ { 1 } } + \frac { \partial F } { \partial y _ { 2 } } - 2 \frac { \partial F } { \partial y _ { 3 } } - 5 \frac { \partial F } { \partial y _ { 4 } } = 0 , \qquad 2 \frac { \partial F } { \partial y _ { 1 } } - \frac { \partial F } { \partial y _ { 2 } } - 3 \frac { \partial F } { \partial y _ { 4 } } = 0 ,
$$

such that their gradients are linearly independent.

5.Consider a Poisson system $\dot { y } = B ( y ) \nabla H ( y )$ andachange of coordinates $z ~ = ~ \vartheta ( y )$ Prove that inthe new coordinates the system isof the form $\dot { z } = \bar { B } ( z ) \nabla K ( z )$ ,where $\bar { B } ( z ) = \vartheta ^ { \prime } ( y ) B ( y ) \vartheta ^ { \prime } ( y ) ^ { T }$ (cf.formula (3.12))and $K ( z ) = H ( y )$ .

6.Givean elementary proof of Theorem4.3.

Hint.Define $\delta ( t ) : = \varphi _ { t } ^ { \prime } ( y ) B ( y ) \varphi _ { t } ^ { \prime } ( y ) ^ { T } \ - \ B \big ( \varphi _ { t } ( y ) \big )$ Using the variational equation for(4.1） prove that $\delta ( t )$ is the solution of a homogeneous linear differential equation.Therefore, $\delta ( 0 ) = 0$ implies $\delta ( t ) = 0$ forall $t$ .

7. Let $z = \vartheta ( y )$ bea transformation taking the Poisson system $\dot { y } = B ( y ) \nabla H ( y )$ to $\dot { z } = \tilde { B } ( z ) \nabla K ( z )$ Prove that $\varPhi _ { h } ( y )$ isa Poisson integrator for $B ( y )$ if and onlyif $\varPsi _ { h } ( z ) = \vartheta \circ \varPhi _ { h } \circ \vartheta ^ { - 1 } ( z )$ isaPoisson integrator for $\bar { B } ( z )$ ,

8.Let $B$ beaskew-symmetric but otherwise arbitrary constant matrix,and consider the Poisson system $\dot { y } = B \nabla H ( y )$ Prove that every symplectic Runge-Kutta method isa Poisson integrator for such asystem. Hint.Transform $B$ toblock-diagonal form.

9.(M.J.Gander 1994).Consider theLotka-Volterra equation (2.13) with separable Hamiltonian $H ( u , v ) = K ( u ) + L ( v ) ,$ Prove that

$$
u _ { n + 1 } = u _ { n } + h u _ { n } v _ { n } H _ { v } ( u _ { n } , v _ { n } ) , \quad v _ { n + 1 } = v _ { n } - h u _ { n + 1 } v _ { n } H _ { u } ( u _ { n + 1 } , v _ { n } )
$$

is a Poisson integrator for this system.

10.Find a change of coordinates that transforms the Lotka-Volterra system (2.14) intoaHamiltonian system (in canonical form).Following the approach of Example 4.11constructPoisson integrators forthis system.

11.Prove that the matrix $B ( y )$ ofExample2.7definesaPoisson bracket,by showingthat the bracketis givenasDirac's bracket(Dirac 1950)

$$
\{ F , G \} = \{ { \widehat F } , { \widehat G } \} - \textstyle \sum _ { i , j } \{ { \widehat F } , c _ { i } \} \gamma _ { i j } \{ c _ { j } , { \widehat G } \} .
$$

Here $F$ and $G$ are functions of $_ y$ , $\hat { F }$ and $\widehat { G }$ are smooth functions of $x$ satisfying $\widehat { F } ( x ( y ) ) \ : = \ : F ( y )$ and $G ( \chi ( y ) ) = G ( y )$ ， $c _ { i } ( x )$ aretheconstraintfunctions defining the manifold $\mathcal { M }$ ,and $\gamma _ { i j }$ are theentries of the inverse of thematrix $\left( \left\{ c _ { i } , c _ { j } \right\} \right)$ ThePoisson bracket to the left in（7.2） correspondsto $B ( y )$ and those totheright are thecanonical brackets evaluatedat $x = \chi ( y )$ Replacing $\hat { F } ( x )$ by $\begin{array} { r } { \widehat { F } ( x ) + \sum _ { k } \mu _ { k } ( x ) c _ { k } ( x ) } \end{array}$ with $\mu _ { k } ( x )$ such that $\{ \widehat { F } , c _ { k } \} = 0$ on $\mathcal { M }$ eliminates the sumin(7.2)and proves the Jacobi identity for $B ( y )$ .
