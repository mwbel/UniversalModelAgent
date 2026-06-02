# Chapter VI. Symplectic Integration of Hamiltonian Systems

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/24c4d4be25ac6b26ac9856512684dba9e08e807435504f2a26038729293ee2ab.jpg)  
Fig.0.1.SirWilliamRowan Hamilton,born:4August 1805in Dublin,died:2 September 1865.Famous for research in optics,mechanics,and for the invention of quaternions

Hamiltonian systems form the most important class of ordinary differential equations in the context ofGeometric Numerical Integration'.An outstanding property ofthese systemsis the symplecticity of theflow.As indicated inthe following diagram,

Ordinary Differential Equations ofmotion canonical (Lagrange) ↑ (Hamilton)   
Variational Principles Generating Functions 1storder Partial DE   
(Lagrange,Hamilton） （Hamilton-Jacobi）

Hamiltonian theory operatesinthree different domains (equations of motion,partial differential equationsand variational principles）which areall interconnected.Each of these viewpoints,which we will study one after the other,leads to the construction of methods preserving the symplecticity.

# VI.1 Hamiltonian Systems

Hamilton'sequations appeared first,among thousands of other formulas,and inspired by previous research in optics,in Hamilton(1834).Their importance was immediatelyrecognized by Jacobi,whostressed and extended the fundamental ideas, sothat,acouple ofyearslater,all the long history of research ofGalilei,Newton, Eulerand Lagrange,was,in thewords of Jacobi(1842),“to beconsidered as an introduction".The next mile-stonesin the exposition of the theory were the monumental three volumes of Poincaré(1892,1893,1899)oncelestial mechanics,Siegel's “Lectures on Celestial Mechanics”(1956),English enlarged edition by Siegel& Moser（1971）,and the influential book ofV.I.Arnold（1989;first Russianedition 1974).Beyond that,Hamiltoniansystems became fundamental inmany branches of physics.One such area,the dynamics of particle accelerators,actuallymotivated the construction of the first symplectic integrators (Ruth 1983).

# VI.1.1Lagrange's Equations

Equations différentielles pour la solution detous les problemes de Dynamique. (J.-L.Lagrange 1788)

The problem of computing the dynamics ofgeneral mechanical systems began with Galilei(published 1638)and Newton’s Principia (1687).The latter allowed one to reduce the movement of free mass points (the“mass points"being such planetsas Mars or Jupiter) to the solution of differential equations (see Sect.I.2）.But the movement ofmore complicated systems such as rigid bodies or bodies attached to each other by rods or spring, were the subject of long and difficult developments,untilLagrange（1760,1788） found an elegant way of treating such problems in general.

We suppose that the position of a mechanical system with $d$ degrees of freedom is described by $q = ( q _ { 1 } , \ldots , q _ { d } ) ^ { T }$ as generalized coordinates(thiscanbeforexample Cartesian coordinates,angles,arc lengths along acurve,etc.).The theory is then built upon two pillars,namely an expression

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/a73a1a36a983a18e072977fa8797177f8cd5e64d004a479002f770d2fd370df7.jpg)  
Joseph-Louis Lagrangel

$$
T = T ( q , \dot { q } )
$$

whichrepresents the kineticenergy(and which isoften of the form $\textstyle { \frac { 1 } { 2 } } { \dot { q } } ^ { T } M ( q ) { \dot { q } }$ where $M ( q )$ issymmetric and positive definite),andbya function

$$
U = U ( q )
$$

representing thepotential energy.Then,after denotingby

$$
L = T - U
$$

thecorresponding Lagrangian,the coordinates $q _ { 1 } ( t ) , \ldots , q _ { d } ( t )$ obeythe differential equations

$$
\frac { d } { d t } \biggl ( \frac { \partial L } { \partial \dot { q } } \biggr ) = \frac { \partial L } { \partial q } ,
$$

which constitute the Lagrangeequations of the system.A numerical (or analytical) integration of these equations allows one to predict the motion of any such system from given initial values(“Ce sont ces équations qui serviront a determiner lacourbe decrite par lecorps $M$ et savitesse a chaque instant";Lagrange 176O,p.369).

Example1.1.Fora masspoint of mass $m$ in $\mathbb { R } ^ { 3 }$ with Cartesian coordinates $x =$ $( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { T }$ wehave $T ( \dot { x } ) = m ( \dot { x } _ { 1 } ^ { 2 } + \dot { x } _ { 2 } ^ { 2 } + \dot { x } _ { 3 } ^ { 2 } ) / 2$ We suppose the point to move ina conservative force field $F ( x ) = - \nabla U ( x )$ Then,the Lagrange equations(1.4) become $m { \ddot { x } } = F ( x )$ ,which isNewton's second law.The equations(I.2.2） for the planetary motionareprecisely of this form.

Example 1.2 (Pendulum).For themathematical pendulum of Sect.I.1we take the angle $\alpha$ ascoordinate.The kinetic and potential energies are given by $T = m ( { \dot { x } } ^ { 2 } +$ $\dot { y } ^ { 2 } ) / 2 = m \ell ^ { 2 } \dot { \alpha } ^ { 2 } / 2$ and $U = m g y = - m g \ell \cos \alpha$ ,respectively,sothattheLagrange equations become $- m g \ell \sin \alpha - m \ell ^ { 2 } \ddot { \alpha } = 0$ orequivalently $\begin{array} { r } { \ddot { \alpha } + \frac { g } { \ell } \sin \alpha = 0 } \end{array}$

# VI.1.2 Hamilton's Canonical Equations

Andiese Hamiltonsche Form der Differentialgleichungen werden die ferneren Untersuchungen,welche den Kern dieser Vorlesung bilden, anknupfen;das Bisherige ist als Einleitungdazu anzusehen.

(C.G.J.Jacobi 1842,p.143)

Hamilton（1834）simplified the structure ofLagrange'sequationsand turned them intoa form that hasremarkable symmetry,by

·introducing Poisson's variables,the conjugatemomenta

$$
p _ { k } = { \frac { \partial L } { \partial { \dot { q } } _ { k } } } ( q , { \dot { q } } ) \qquad { \mathrm { f o r } } \quad k = 1 , \dots , d ,
$$

· considering the Hamiltonian

$$
H : = p ^ { T } \dot { q } - L ( q , \dot { q } )
$$

as a function of $p$ and $q$ ,i.e.,taking $H = H ( p , q )$ obtained by expressing $\dot { q }$ asa function of $p$ and $q$ via (1.5).

Here itis,of course,required that(1.5）defines,for every $q$ ,acontinuously differentiable bijection ${ \dot { q } }  p$ Thismapiscalled theLegendretransform.

Theorem1.3.Lagrange'sequations(1.4)areequivalent to Hamilton'sequations

$$
\dot { p } _ { k } = - \frac { \partial H } { \partial q _ { k } } ( p , q ) , \qquad \dot { q } _ { k } = \frac { \partial H } { \partial p _ { k } } ( p , q ) , \qquad k = 1 , . . . , d .
$$

Proof.The definitions(1.5)and(1.6) for themomenta $p$ and for the Hamiltonian $H$ imply that

$$
\begin{array} { r c l } { \displaystyle \frac { \partial H } { \partial \boldsymbol { p } } } & { = } & { \displaystyle \boldsymbol { \dot { q } } ^ { T } + \boldsymbol { p } ^ { T } \frac { \partial \dot { \boldsymbol { q } } } { \partial \boldsymbol { p } } - \frac { \partial L } { \partial \dot { \boldsymbol { q } } } \frac { \partial \dot { \boldsymbol { q } } } { \partial \boldsymbol { p } } = \boldsymbol { \dot { q } } ^ { T } , } \\ { \displaystyle \frac { \partial H } { \partial \boldsymbol { q } } } & { = } & { \boldsymbol { p } ^ { T } \frac { \partial \dot { \boldsymbol { q } } } { \partial \boldsymbol { q } } - \frac { \partial L } { \partial \boldsymbol { q } } - \frac { \partial L } { \partial \dot { \boldsymbol { q } } } \frac { \partial \dot { \boldsymbol { q } } } { \partial \boldsymbol { q } } = - \frac { \partial L } { \partial \boldsymbol { q } } . } \end{array}
$$

TheLagrange equations(1.4) are therefore equivalent to(1.7).

Case of Quadratic $\mathbf { x } .$ In the case that $\begin{array} { r } { T = \frac { 1 } { 2 } \dot { q } ^ { L } M ( q ) \dot { q } } \end{array}$ is quadratic,where $M ( q )$ isasymmetricand positive definite matrix,we have,fora fixed $q$ , $p = M ( q ) \dot { q }$ ,so thatthe existence of theLegendre transform is established.Further,byreplacing the variable $\dot { q }$ by $M ( q ) ^ { - 1 } p$ in the definition (1.6)of $H ( p , q )$ ,we obtain

$$
\begin{array} { l } { { H ( p , q ) ~ = ~ p ^ { T } M ( q ) ^ { - 1 } p - L \bigl ( q , M ( q ) ^ { - 1 } p \bigr ) } } \\ { { ~ } } \\ { { ~ = ~ p ^ { T } M ( q ) ^ { - 1 } p - \displaystyle { \frac { 1 } { 2 } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q ) = \displaystyle { \frac { 1 } { 2 } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q ) , } } \end{array}
$$

and the Hamiltonianis $H = T + U$ ,which isthe total energyofthemechanical system.

In Chap.Iwe have seen several examples of Hamiltonian systems,e.g.,the pendulum (I.1.13),the Kepler problem(1.2.2),the outersolar system (I.2.12),etc.In the followingwe consider Hamiltoniansystems(1.7)where the Hamiltonian $H ( p , q )$ is arbitrary,and so not necessarily related toa mechanical problem.

# VI.2 Symplectic Transformations

Thename“complex group”formerly advocatedbymeinallusion to line complexes,...has become more and more embarrassing through collisionwith the word“complex”in the connotation ofcomplex number.I therefore propose toreplace itby the Greek adjective"symplectic."

(H.Weyl(1939),p.165)

Afirstproperty ofHamiltonian systems,already seenin Example1.2ofSect.IV.1, is that the Hamiltonian $H ( p , q )$ isafirst integral of thesystem(1.7).Inthis section weshall study another important property-thesymplecticity of its flow.The basic objects tobe studiedare two-dimensional parallelograms lying in $\mathbb { R } ^ { 2 d }$ Wesuppose the parallelogram to bespanned by two vectors

$$
\xi = \binom { \xi ^ { p } } { \xi ^ { q } } , \qquad \eta = \binom { \eta ^ { p } } { \eta ^ { q } }
$$

inthe $( p , q )$ space $\xi ^ { p }$ , $\xi ^ { q }$ , $\eta ^ { p }$ , $\eta ^ { q }$ arein $\mathbb { R } ^ { d }$ as

$$
P \equiv \{ t \xi + s \eta | 0 \leq t \leq 1 , 0 \leq s \leq 1 \} .
$$

In the case $d = 1$ weconsider the orientedarea

$$
\operatorname { o r . a r e a } \left( P \right) = \operatorname * { d e t } { \left( \begin{array} { l l } { \xi ^ { p } } & { \eta ^ { p } } \\ { \xi ^ { q } } & { \eta ^ { q } } \end{array} \right) } = \xi ^ { p } \eta ^ { q } = \xi ^ { q } \eta ^ { p }
$$

(seeleft picture ofFig.2.1).In higher dimensions,we replace this by the sum of the orientedareasoftheprojections of $P$ onto the coordinateplanes $( p _ { i } , q _ { i } )$ ,i.e.,by

$$
\omega ( \xi , \eta ) : = \sum _ { i = 1 } ^ { d } \operatorname* { d e t } { \left( \begin{array} { l l } { \xi _ { i } ^ { p } } & { \eta _ { i } ^ { p } } \\ { \xi _ { i } ^ { q } } & { \eta _ { i } ^ { q } } \end{array} \right) } = \sum _ { i = 1 } ^ { d } ( \xi _ { i } ^ { p } \eta _ { i } ^ { q } - \xi _ { i } ^ { q } \eta _ { i } ^ { p } ) .
$$

This defines a bilinear map acting on vectors of $\mathbb { R } ^ { 2 d }$ ,which will play acentral role forHamiltonian systems.In matrix notation,this map has the form

$$
\omega ( \xi , \eta ) = \xi ^ { T } \mathcal { J } \eta \qquad \mathrm { w i t h } \qquad \mathcal { J } = \left( \begin{array} { l l } { 0 } & { J } \\ { - I } & { 0 } \end{array} \right)
$$

where $I$ is the identity matrix of dimension $d$

Definition 2.1.A linear mapping $A : \mathbb { R } ^ { 2 d }  \mathbb { R } ^ { 2 d }$ is called symplectic if

$$
A ^ { T } J A = J
$$

or,equivalently,if $\omega ( A \xi , A \eta ) = \omega ( \xi , \eta )$ forall $\xi , \eta \in \mathbb { R } ^ { 2 d }$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/a3d838c207711b1eea879e8c4ff4740bef17fe249f861e95cd5b1213b321fc62.jpg)  
Fig.2.1.Symplecticity (area preservation)ofalinear mapping

In the case $d = 1$ where the expression $\omega ( \xi , \eta )$ represents the area of theparallelogram $P$ ,symplecticity ofa linearmapping $A$ istherefore the area preservation of $A$ (see Fig.2.1).In the general case（ $d > 1$ ),symplecticity means that the sum of the oriented areas of the projections of $P$ onto $( p _ { i } , q _ { i } )$ is the sameas that for the transformed parallelograms $A ( P )$

Wenow turn our attention to nonlinear mappings.Differentiable functions can belocally approximated by linear mappings.This justifies the following definition.

Definition2.2.Adifferentiablemap $g : U \to \mathbb { R } ^ { 2 d }$ (where $U \subset \mathbb { R } ^ { 2 d }$ is an open set) iscalled symplecticif the Jacobian matrix $g ^ { \prime } ( p , q )$ iseverywhere symplectic,i.e.,if

$$
\begin{array} { r } { g ^ { \prime } ( p , q ) ^ { T } J g ^ { \prime } ( p , \bar { q } ) = J \qquad \mathrm { o r } \qquad \omega ( g ^ { \prime } ( p , q ) \xi , g ^ { \prime } ( p , q ) \eta ) = \omega ( \xi , \eta ) . } \end{array}
$$

Let us give a geometric interpretation of symplecticity for nonlinear mappings. Considera2-dimensional sub-manifold $M$ ofthe $2 d$ -dimensional set $U$ andsuppose that itis given as theimage $M = \psi ( K )$ ofa compact set $K \subset \mathbb { R } ^ { 2 }$ ,where

$\psi ( s , t )$ isacontinuously differentiable function.The manifold $M$ can then be consideredasthe limit of aunion of smallparallelograms spanned by the vectors

$$
{ \frac { \partial \psi } { \partial s } } ( s , t ) d s \qquad { \mathrm { a n d } } \qquad { \frac { \partial \psi } { \partial t } } ( s , t ) d t .
$$

For one such parallelogram we consider (asabove) the sum over the oriented areas of its projections onto the $( p _ { i } , q _ { i } )$ plane.We then sum over all parallelograms of the manifold.In the limit this gives the expression

$$
\Omega ( M ) = \iint _ { K } \omega \left( { \frac { \partial \psi } { \partial s } } ( s , t ) , { \frac { \partial \psi } { \partial t } } ( s , t ) \right) d s d t .
$$

The transformation formula fordouble integrals implies that $\Omega ( M )$ isindependent of theparametrization $\psi$ of $M$

Lemma 2.3.If themapping $g : U \to \mathbb { R } ^ { 2 d }$ is symplectic on $U$ ,then it preserves the expression $\Omega ( M )$ i.e.,

$$
\Omega ( g ( M ) ) = \Omega ( M )
$$

holdsforall2-dimensionalmanifolds $M$ thatcanberepresentedas the image ofa continuouslydifferentiablefunction $\psi$ .

ProofThe manifold $g ( M )$ can be parametrized by $g \circ \psi$ We have

$$
\varOmega \big ( g ( M ) \big ) = \int \int _ { K } \omega \bigg ( \frac { \partial ( g \circ \psi ) } { \partial s } ( s , t ) , \frac { \partial ( g \circ \psi ) } { \partial t } ( s , t ) \bigg ) d s d t = \varOmega ( M ) ,
$$

because ${ ( g \circ \psi ) ^ { \prime } ( s , \xi ) = g ^ { \prime } \bigl ( \psi ( s , t ) \bigr ) \psi ^ { \prime } ( s , t ) }$ and $g$ is a symplectic transformation.□

For $d = 1$ , $M$ isalreadyasubset of $\mathbb { R } ^ { 2 }$ andwe choose $K \ = \ M$ with $\psi$ the identity map.In this case, $\Omega ( M ) = \textstyle \iint _ { M } d s d t$ represents the area of $M .$ Hence, Lemma 2.3 states that all symplectic mappings (also nonlinear ones) are area preserving.

Weare now able to prove the main result of thissection.We use the notation $y = ( p , q )$ ,andwewrite theHamiltonian system(1.7)inthe form

$$
\dot { y } = J ^ { - 1 } \nabla H ( y ) ,
$$

where $J$ is the matrix of (2.3)and $\nabla H ( y ) = H ^ { \prime } ( y ) ^ { \cal I }$

Recall that the ffow $\varphi _ { t } : U \to \mathbb { R } ^ { 2 d }$ of a Hamiltonian system is the mapping that advances the solution by time $t$ ,i.e., $\varphi _ { t } ( p _ { 0 } , q _ { 0 } ) = ( p ( t , p _ { 0 } , q _ { 0 } ) , q ( t , p _ { 0 } , q _ { 0 } ) )$ ,where $p ( t , p _ { 0 } , q _ { 0 } )$ ， $q ( t , p _ { 0 } , q _ { 0 } )$ isthe solution of the system corresponding to initial values $p ( 0 ) = p _ { 0 }$ , $q ( 0 ) = q _ { 0 }$ .

Theorem 2.4 (Poincaré 1899).Let $H ( p , q )$ beatwice continuously differentiable function on $U \subset \mathbb { R } ^ { 2 d }$ Then,foreachfixedt,theflow $\varphi _ { t }$ isasymplectictransformationwhereveritisdefined.

Proof.The derivative $\partial \varphi _ { t } / \partial y _ { 0 }$ (with $y _ { 0 } ~ = ~ ( p _ { 0 } , q _ { 0 } ) )$ isa solution of the variationalequationwhich,forthe Hamiltonian system(2.5),isof the form $\dot { \psi } =$ $J ^ { - 1 } \nabla ^ { 2 } H \left( \varphi _ { t } ( y _ { 0 } ) \right) \varPsi ,$ where $\nabla ^ { 2 } H ( p , q )$ is the Hessian matrix of $H ( p , q ) ( \nabla ^ { 2 } H ( p , q )$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/1f971769db4f595c55722dce08ce8db704abc2b50c6295c8f330cb752b2c6044.jpg)  
Fig.2.2.Area preservation of theflow of Hamiltonian systems

issymmetric).We therefore obtain

$$
\begin{array} { r l } & { \frac { 1 } { t } \Big ( \Big ( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) ^ { T } J \left( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \right) \Big ) = \Big ( \frac { d } { d t } \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) ^ { T } J \left( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \right) + \Big ( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) ^ { T } J \left( \frac { d } { d t } \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \right) } \\ & { \ = \Big ( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) ^ { T } \nabla ^ { 2 } H \big ( \varphi _ { t } ( y _ { 0 } ) \big ) J ^ { - T } J \Big ( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) + \Big ( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) ^ { T } \nabla ^ { 2 } H \big ( \varphi _ { t } ( y _ { 0 } ) \big ) \Big ( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \Big ) = } \end{array}
$$

because $J ^ { T } \equiv - J$ and $J ^ { - T } { \boldsymbol { J } } = - I .$ Since the relation

$$
\left( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \right) ^ { T } J \left( \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } \right) = J
$$

is satisfied for $t = 0$ $\varphi _ { 0 }$ is theidentitymap),itissatisfied forall $t$ and all $( p _ { 0 } , q _ { 0 } )$ ， aslong as the solution remains in the domain ofdefinition of $H$ □

Example2.5.We illustrate this theoremwith the pendulum problem(Example1.2) using the normalization $m = \ell = g = 1$ Wehave $q = \alpha$ ， $p = \alpha$ ,andtheHamiltonian is given by

$$
H ( p , q ) = p ^ { 2 } / 2 - \cos q .
$$

Fig.2.2 shows level curves of this function,and it also illustrates the area preservationof theflowt.Indeed,byTheorem2.4andLemma2.3,theareasof $A$ and $\varphi _ { t } ( A )$ aswell as those of $B$ and $\varphi _ { t } ( B )$ are the same,although their appearance is completely different.

Wenext showthat symplecticity of the flowisa characteristic property for Hamiltonian systems.Wecall adifferential equation $\dot { y } = f ( y )$ locally Hamiltonian, ifforevery $y _ { 0 } \in U$ there exists a neighbourhood where $f ( y ) = J ^ { - 1 } \nabla H ( y )$ for some function $H$

Theorem 2.6.Let $f : U \to \mathbb { R } ^ { 2 d }$ becontinuously differentiable.Then, $\dot { y } = f ( y )$ is locallyHamiltonianifandonlyifitsflow $\varphi _ { t } ( y )$ issymplectic for all $y \in U$ and for all sufficientlysmall $t$

Proof.Thenecessity follows fromTheorem2.4.We thereforeassume that theflow $\varphi _ { t }$ issymplectic,and we have toprove the local existence of a function $H ( y )$ such that $f ( y ) = J ^ { - 1 } \nabla H ( y )$ Differentiating（2.6）and using the fact that $\partial \varphi _ { t } / \partial y _ { 0 }$ isa solution of the variational equation $\dot { \Psi } = f ^ { \prime } \big ( \varphi _ { t } ( y _ { 0 } \big ) \big ) \varPsi$ we obtain

$$
{ \frac { \mathbf { \xi } _ { t } ^ { \prime } } { t } } ( ( { \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } } ) ^ { T } J ( { \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } } ) ) = ( { \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } } ) ( f ^ { \prime } ( \varphi _ { t } ( y _ { 0 } ) ) ^ { T } J + J f ^ { \prime } ( \varphi _ { t } ( y _ { 0 } ) ) ) ( { \frac { \partial \varphi _ { t } } { \partial y _ { 0 } } } ) =
$$

Putting $t = 0$ ,it follows from $J = - J ^ { T }$ that $J f ^ { \prime } ( y _ { 0 } )$ isa symmetric matrix for all $y _ { 0 }$ TheIntegrabilityLemma2.7below showsthat $J f ( y )$ can be written as the gradient of a function $H ( y )$ □

Thefollowing integrability condition for the existence of apotential was already knownto EulerandLagrange (seee.g.,Euler'sOpera Omnia,vol.19.p.2-3,or Lagrange(1760),p.375）.

Lemma 2.7 (Integrability Lemma). Let $D \subset \mathbb { R } ^ { n }$ be openand $f : D  \mathbb { R } ^ { n }$ be continuouslydifferentiable,andassume that theJacobian $f ^ { \prime } ( y )$ issymmetric forall $y \in \mathcal { D }$ Then,forevery $y _ { 0 } \in \mathcal { D }$ thereexistsaneighbourhoodanda function $H ( y )$ suchthat

$$
f ( y ) = \nabla H ( y )
$$

onthisneighbourhood.Inotherwords,thedifferential form $f _ { 1 } ( y ) d y _ { 1 } + \ldots +$ $f _ { n } ( y ) d y _ { n } = d H$ isatotal differential.

Proof.Assume $y _ { 0 } = 0$ ,andconsideraball around $y _ { 0 }$ which is contained in $D$ .On this ball wedefine

$$
H ( y ) = \int _ { 0 } ^ { 1 } y ^ { T } f ( t y ) d t + C o n s t .
$$

Differentiation with respect to $y _ { k }$ ,and using the symmetry assumption $\partial f _ { i } / \partial y _ { k } =$ $\partial f _ { k } / \partial y _ { i }$ yields

$$
\frac { \partial H } { \partial y _ { k } } ( y ) = \int _ { 0 } ^ { 1 } \left( f _ { k } ( t y ) + y ^ { T } \frac { \partial f } { \partial y _ { k } } ( t y ) t \right) d t = \int _ { 0 } ^ { 1 } \frac { d } { d t } \Big ( t f _ { k } ( t y ) \Big ) d t = f _ { k } ( y ) ,
$$

which proves the statement.

For $D = \mathbb { R } ^ { 2 d }$ or for star-shaped regions $\boldsymbol { D }$ ,the above proof shows that the function $H$ ofLemma 2.7isglobally defined.Hence the Hamiltonian of Theorem 2.6 isalso globally defined in thiscase.This remainsvalid for simplyconnected sets $\mathcal { D }$ .Acounter-example,which shows that the existence of a global Hamiltonian in Theorem2.6is not true for general $D$ is given in Exercise 6.

Animportant property of symplectic transformations,which goes back to Jacobi （1836,“TheoremX"),is that they preservetheHamiltoniancharacterofthedifferentialequation.Such transformations have been termed canonical since the 19th century.The nexttheorem shows that canonical and symplectic transformations are the same.

Theorem 2.8.Let $\psi : U \to V$ bea change of coordinates such that $\psi$ and $\psi ^ { - 1 }$ arecontinuouslydifferentiable functions.If $\psi$ issymplectic,theHamiltoniansystem $\dot { y } = J ^ { - 1 } \nabla H ( y )$ becomes in thenew variables $z = \psi ( y )$

$$
\dot { z } = J ^ { - 1 } \nabla K ( z ) \qquad w i t h \qquad K ( z ) = H ( y ) .
$$

Conversely,if $\psi$ transforms every Hamiltonian systemtoanother Hamiltoniansystemvia(2.8),then $\psi$ issymplectic.

Proof. Since $\dot { z } = \psi ^ { \prime } ( y ) \dot { y }$ and $\psi ^ { \prime } ( y ) ^ { \cal I } \nabla K ( z ) = \nabla H ( y )$ ,theHamiltonian system $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) } \end{array}$ becomes

$$
\dot { z } = \psi ^ { \prime } ( y ) J ^ { - 1 } \psi ^ { \prime } ( y ) ^ { T } \nabla K ( z )
$$

in the new variables.It is equivalent to (2.8)if

$$
\psi ^ { \prime } ( y ) J ^ { - 1 } \psi ^ { \prime } ( y ) ^ { T } = J ^ { - 1 } .
$$

Multiplying this relation from the right by $\psi ^ { \prime } ( y ) ^ { - T }$ and from the left by $\psi ^ { \prime } ( y ) ^ { - 1 }$ and then taking its inverseyields $J = \psi ^ { \prime } ( y ) ^ { T } J \psi ^ { \prime } ( y )$ ,which shows that(2.10)is equivalenttothe symplecticity of $\psi$ .

Fortheinverse relationwe note that (2.9) is Hamiltonian forall $K ( z )$ if and only if(2.10） holds. □

# VI.3First Examplesof Symplectic Integrators

Since symplecticity is a characteristic propertyof Hamiltonian systems(Theorem2.6), itisnatural to search for numerical methods that share this property.Pioneering work on symplectic integration isdue tode Vogelaere (1956),Ruth(1983),and FengKang(1985). Books on the now well-developed subject are Sanz-Serna&Calvo（1994）andLeimkuhler &Reich(2004).

Definition 3.1.A numerical one-step method is called symplecticif the one-step map

$$
y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/1f14c6bb77912a668894ebc73594033d8e0bb665da27761b6250f0992f9d95e9.jpg)  
Feng Kang2

is symplectic whenever the method is applied to a smooth Hamiltonian system.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/eb34f1f782bc672700b885c39a37e38e3f3fdb22586a8574c63d50cba6843c9f.jpg)  
Fig.3.1.Area preservation of numerical methods for the pendulum;same initial sets as in Fig.2.2；first ordermethods(left column）: $h = \pi / 4$ second ordermethods(rightcolumn）: $h = \pi / 3$ ;dashed:exact flow

Example3.2.Weconsider thependulum problem of Example 2.5with the same initialsetsasinFig.2.2.Weapply sixdifferent numerical methods to this problem: theexplicit Eulermethod(I.1.5), the symplectic Euler method (I.1.9),and the implicit Euler method(I.1.6),as well as the second order method of Runge (II.1.3) (theright one),the Stormer-Verlet scheme(I.1.17),and the implicit midpoint rule (I.1.7).For two sets of initial values $( p _ { 0 } , q _ { 0 } )$ we compute several steps with step size $h = \pi / 4$ forthe first ordermethods,and $h = \pi / 3$ forthe second order methods. Oneclearly observesin Fig.3.1that theexplicit Euler,the implicit Eulerand the second order explicit method of Runge are not symplectic (not areapreserving).We shall provebelow that the other methodsare symplectic.A different proof of their symplecticity(using generating functions)will be given in Sect.VI.5.

Inthefollowing we show the symplecticity of various numerical methods from ChaptersIand IIwhen they are applied to the Hamiltonian system inthe variables $\boldsymbol { y } = ( p , q )$ ,

$$
\begin{array} { r l } { \dot { p } = - H _ { q } ( p , q ) \qquad } & { { } \mathrm { o r ~ e q u i v a l e n t l y } \qquad \dot { y } = J ^ { - 1 } \nabla H ( y ) , } \\ { \dot { q } = } & { { } H _ { p } ( p , q ) \qquad } \end{array}
$$

where $H _ { p }$ and $H _ { q }$ denote the column vectors of partial derivatives of the Hamiltonian $H ( p , q )$ with respect to $p$ and $q$ ,respectively.

Theorem3.3 (deVogelaere1956).Theso-called symplectic Eulermethods(1.1.9)

$$
\begin{array} { r l r l } & { p _ { n + 1 } = p _ { n } - h H _ { q } ( p _ { n + 1 } , q _ { n } ) } & & { p _ { n + 1 } = p _ { n } - h H _ { q } ( p _ { n } , q _ { n + 1 } ) } \\ & { q _ { n + 1 } = q _ { n } + h H _ { p } ( p _ { n + 1 } , q _ { n } ) } & & { q _ { n + 1 } = q _ { n } + h H _ { p } ( p _ { n } , q _ { n + 1 } ) } \end{array}
$$

aresymplectic methods of order1.

Proof.We consider only the method to the left of (3.1).Differentiation with respect to $( p _ { n } , q _ { n } )$ yields

$$
\left( \begin{array} { c c } { { I + h H _ { q p } ^ { T } } } & { { 0 } } \\ { { - h H _ { p p } } } & { { I } } \end{array} \right) \left( \frac { \partial ( p _ { n + 1 } , q _ { n + 1 } ) } { \partial ( p _ { n } , q _ { n } ) } \right) = \left( \begin{array} { c c } { { I } } & { { - h H _ { q q } } } \\ { { 0 } } & { { I + h H _ { q p } } } \end{array} \right) ,
$$

where the matrices $H _ { q p } , H _ { p p } , \ldots .$ of partialderivativesareall evaluatedat $( p _ { n + 1 } , q _ { n } )$ Ti $\frac { \partial ( p _ { n + 1 } , q _ { n + 1 } ) } { \partial ( p _ { n } , q _ { n } ) }$ $\begin{array} { r } { \frac { \partial ( p _ { n + 1 } , q _ { n + 1 } ) } { \partial ( p _ { n } , q _ { n } ) } \Big ) ^ { L } J \Big ( \frac { \partial ( p _ { n + 1 } , q _ { n + 1 } ) } { \partial ( p _ { n } , q _ { n } ) } \Big ) = J . } \end{array}$

Themethods(3.1） are implicit for general Hamiltonian systems.For separable $H ( p , q ) = T ( p ) + U ( q )$ ,however,both variants turn outtobeexplicit.Itisinterestingtomention that there are more general situationswhere the symplectic Euler methods are explicit.If,fora suitable ordering of the components,

$$
{ \frac { \partial H } { \partial q _ { i } } } ( p , q ) \quad { \mathrm { d o e s ~ n o t ~ d e p e n d ~ o n ~ } } p _ { j } { \mathrm { ~ f o r ~ } } j \geq i ,
$$

then the left method of(3.1） is explicit,and the componentsof $p _ { n + 1 }$ can be computed oneafter the other.If,forapossibly different ordering of the components,

$$
{ \frac { \partial H } { \partial p _ { i } } } ( p , q ) \quad { \mathrm { d o e s ~ n o t ~ d e p e n d ~ o n ~ } } q _ { j } { \mathrm { ~ f o r ~ } } j \geq i ,
$$

thentherightmethod of(3.1)is explicit.As anexample consider theHamiltonian

$$
H ( p _ { r } , p _ { \varphi } , r , \varphi ) = \frac { 1 } { 2 } \Big ( p _ { r } ^ { 2 } + r ^ { - 2 } p _ { \varphi } ^ { 2 } \Big ) - r \cos \varphi + ( r - 1 ) ^ { 2 } ,
$$

which models a springpendulum in polar coordinates.For the ordering $\varphi < r$ condition(3.2) is fulfilled,and for the inverse ordering $r < \varphi$ condition (3.3).Consequently,both symplectic Eulermethodsareexplicit for this problem.Themethods remainexplicit if theconditions(3.2）and(3.3） hold for blocks of componentsinstead of single components.

Weconsider next the extension of the Stormer-Verlet scheme (I.1.17),considered in TableII.2.1.

Theorem3.4.TheStormer-Verlet schemes(1.1.17)

$$
\begin{array} { r l } { \displaystyle p _ { n + 1 / 2 } = } & { { } p _ { n } - \frac { h } { 2 } H _ { q } ( p _ { n + 1 / 2 } , q _ { n } ) } \\ { \displaystyle q _ { n + 1 } = q _ { n } + \frac { h } { 2 } \Big ( H _ { p } ( p _ { n + 1 / 2 } , q _ { n } ) + H _ { p } ( p _ { n + 1 / 2 } , q _ { n + 1 } ) \Big ) } \\ { \displaystyle p _ { n + 1 } = } & { { } p _ { n + 1 / 2 } = \frac { h } { 2 } H _ { q } ( p _ { n + 1 / 2 } , q _ { n + 1 } ) } \end{array}
$$

and

$$
\begin{array} { r c l } { { q _ { n + 1 / 2 } ~ = ~ q _ { n } + \displaystyle \frac { h } { 2 } H _ { q } ( p _ { n } , q _ { n + 1 / 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { p _ { n + 1 } ~ = ~ p _ { n } - \displaystyle \frac { h } { 2 } \Big ( H _ { p } ( p _ { n } , q _ { n + 1 / 2 } ) + H _ { p } ( p _ { n + 1 } , q _ { n + 1 / 2 } ) \Big ) } } \\ { { } } & { { } } & { { ~ q _ { n + 1 } ~ = ~ q _ { n + 1 / 2 } + \displaystyle \frac { h } { 2 } H _ { q } ( p _ { n + 1 } , q _ { n + 1 / 2 } ) } } \end{array}
$$

are symplectic methods of order 2.

Proof.This is an immediate consequenceof the fact that the Stormer-Verlet scheme is the composition of the two symplectic Euler methods(3.1).Order 2 follows from its symmetry. □

We note that the Stormer-Verlet methods(3.4)and (3.5) are explicit for separable problems and for Hamiltonians that satisfy both conditions(3.2) and(3.3).

Theorem3.5.The implicit midpointrule

$$
y _ { n + 1 } = y _ { n } + h J ^ { - 1 } \nabla H \big ( ( y _ { n + 1 } + y _ { n } ) / 2 \big )
$$

isa symplecticmethod of order 2.

Proof.Differentiation of(3.6)yields

$$
\Big ( I - \frac { h } { 2 } J ^ { - 1 } \nabla ^ { 2 } H \Big ) \Big ( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \Big ) = \Big ( I + \frac { h } { 2 } J ^ { - 1 } \nabla ^ { 2 } H \Big ) .
$$

Againitis straightforwardtoverify that $\begin{array} { r } { \big ( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \big ) ^ { T } \mathcal { J } \big ( \frac { \partial y _ { n + 1 } } { \partial y _ { n } } \big ) = \mathcal { J } . } \end{array}$ Due to its symmetry,the midpoint rule is known to be of order2(see Theorem I.3.2). □

Thenext two theorems area consequence of the fact that the composition of symplectic transformations isagain symplectic.They are also used to prove the existence of symplectic methods of arbitrarily high order,and to explainwhy the theory of composition methods ofChapters II and III is so important for geometric integration.

Theorem 3.6.Let $\phi _ { h }$ denotethesymplectic Eulermethod(3.1).Then,thecompositionmethod(II.4.6)issymplecticforeverychoiceof theparameters $\alpha _ { i } , \beta _ { i }$

$\widehat { \varPhi } _ { h }$ issymplectic and symmetric(e.g.，the implicit midpoint rule orthe Stormer-Verlet scheme),then thecompositionmethod(V.3.8)is symplectic too.□

Theorem3.7.Assume that the Hamiltonian is given by $H ( y ) = H _ { 1 } ( y ) + H _ { 2 } ( y )$ ， and considerthesplitting

$$
\dot { y } = J ^ { - 1 } \nabla H ( y ) = J ^ { - 1 } \nabla H _ { 1 } ( y ) + J ^ { - 1 } \nabla H _ { 2 } ( y ) .
$$

The splitting method(I.5.6) is then symplectic.

# VI.4Symplectic Runge-Kutta Methods

Thesystematic study of symplectic Runge-Kutta methods started around 1988,and acomplete characterization has been found independently byLasagni(1988)（using theapproach of generating functions）,and by Sanz-Serna(1988)and Suris（1988) (usingthe ideas of theclassical papers of Burrage&Butcher(1979) andCrouzeix (1979)onalgebraic stability).

# VI.4.1Criterion of Symplecticity

Wefollow the approach of Bochev& Scovel(1994),which is based on the following important lemma.

Lemma4.1.ForRunge-Kutta methodsand forpartitioned Runge-Kuttamethods thefollowing diagram commutes:

$$
\begin{array} { r l r } { \dot { y } = f ( y ) , ~ y ( 0 ) = y _ { 0 } \quad } & { \Longrightarrow \quad } & { \dot { y } = f ( y ) , ~ y ( 0 ) = y _ { 0 } } \\ & { } & { \dot { \varPsi } = f ^ { \prime } ( y ) \varPsi , ~ \varPsi ( 0 ) = I } \\ { \quad \quad } & { } & { \left\lfloor m e t h o d \right. } \\ & { } & { \left\{ y _ { n } \right\} \quad } & { \longrightarrow \quad } & { \{ y _ { n } , \varPsi _ { n } \} } \end{array}
$$

(horizontal arrowsmeana differentiation with respect to $_ { y _ { 0 } }$ ).Therefore,thenumericalresult $y _ { n } , \psi _ { n } ,$ obtained fromapplyingthemethodtotheproblemaugmentedby itsvariational equation,isequalto thenumerical solutionfor $\dot { y } = f ( y )$ augmented byitsderivative $\varPsi _ { n } = \partial y _ { n } / \partial y _ { 0 }$ .

Proof.The result is proved by implicit differentiation.Letus illustrate this for the explicit Eulermethod

$$
y _ { n + 1 } = y _ { n } + h f ( y _ { n } ) .
$$

Weconsider $y _ { n }$ and $y _ { n + 1 }$ as functions of $y _ { 0 }$ ,and we differentiate with respect to $y _ { 0 }$ theequationdefining the numerical method.Forthe Eulermethod this gives

$$
{ \frac { \partial y _ { n + 1 } } { \partial y _ { 0 } } } = { \frac { \partial y _ { n } } { \partial y _ { 0 } } } + h f ^ { \prime } ( y _ { n } ) { \frac { \partial y _ { n } } { \partial y _ { 0 } } } ,
$$

which is exactly the relation that we get from applying the method to the variational equation.Since $\partial y _ { 0 } / \partial y _ { 0 } = I$ wehave $\partial y _ { n } / \partial y _ { 0 } = \varPsi _ { n }$ forall $_ { n }$ , □

Themain observation nowis that the symplecticity condition (2.6) is aquadratic first integral of the variational equation:we write the Hamiltonian system together with its variational equation as

$$
\dot { y } = J ^ { - 1 } \nabla H ( y ) , \qquad \dot { \psi } = J ^ { - 1 } \nabla ^ { 2 } H ( y ) \varPsi .
$$

It follows from


<!-- chunk 0004: pages 211-280 -->
$$
( J ^ { - 1 } \nabla ^ { 2 } H ( y ) \varPsi ) ^ { T } J \varPsi + \varPsi ^ { T } J ( J ^ { - 1 } \nabla ^ { 2 } H ( y ) \varPsi ) = 0
$$

(see also the proof of Theorem 2.4） that $\varPsi ^ { T } J \varPsi$ isa quadratic first integral of the augmented system(4.1).

Therefore,every Runge-Kutta method that preserves quadratic first integrals,is asymplecticmethod.FromTheoremIV.2.1andTheoremIV.2.2we thus obtain the following results.

Theorem 4.2. TheGausscollocationmethods ofSect.II.1.3are symplectic.

Theorem4.3.IfthecoefcientsofaRunge-Kuttamethod satisfy

$$
b _ { i } a _ { i j } + b _ { j } a _ { j i } = b _ { i } b _ { j } \qquad f o r a l l ~ i , j = 1 , \ldots , s ,
$$

then it is symplectic.

Similarto thesituationin TheoremV.2.4,diagonally implicit,symplectic Runge-Kutta methods are composition methods.

Theorem4.4.Adiagonally implicit Runge-Kuttamethod satisfyingthe symplecticitycondition(4.2）and $b _ { i } \neq 0$ isequivalent tothecomposition

$$
\varPhi _ { b , h } ^ { M } \circ . \dots \circ \varPhi _ { b _ { 2 } h } ^ { M } \circ \varPhi _ { b _ { 1 } h } ^ { M } ,
$$

where $\Phi _ { h } ^ { M }$ standsfortheimplicitmidpointrule.

Proof.For $i = j$ condition（4.2）gives $a _ { i i } = b _ { i } / 2$ and,togetherwith $a _ { j i } = 0$ (for $i > j$ ),implies $a _ { i j } = b _ { j } .$ This proves the statement. □

Theassumption $ { \mathbf { \hat { b } } } _ { i } \neq 0$ isnot restrictive in the sense that for diagonally implicitRunge-Kutta methods satisfying (4.2） the internal stages corresponding to $b _ { i } = 0$ ”do not influence the numerical result and can be removed.

Tounderstand the symplecticity of partitioned Runge-Kutta methods,we write the solution $\psi$ of the variational equation as

$$
\varPsi = \left( \begin{array} { l } { \varPsi ^ { p } } \\ { \varPsi ^ { q } } \end{array} \right) .
$$

Then,the Hamiltoniansystem together with itsvariational equation(4.1） isa partitioned systemwith variables $( p , \varPsi ^ { p } )$ and $\left( q , \varPsi ^ { q } \right)$ Everycomponentof

$$
\psi ^ { T } J \bar { \psi } = ( \bar { \psi } ^ { p } ) ^ { T } \bar { \psi } ^ { q } - ( \bar { \psi } ^ { q } ) ^ { T } \bar { \psi } ^ { p }
$$

isoftheform(IV.2.5),sothat TheoremIV.2.3andTheoremIV.2.4yield the following results.

Theorem4.5.TheLobattoIlIA-IBpairisasymplecticmethod.

Theorem4.6.Ifthecoeffcientsofapartitioned Runge-Kutmethod(Il.2.2)satisfy

$$
\begin{array} { l } { b _ { i } \widehat { a } _ { i j } + \widehat { b } _ { j } a _ { j i } = b _ { i } \widehat { b } _ { j } \qquad f o r \ i , j = 1 , \dots , s , } \\ { b _ { i } = \widehat { b } _ { i } \qquad f o r \ i = 1 , \dots , s , } \end{array}
$$

then it issymplectic.

If theHamiltonian isof theform $H ( p , q ) = T ( p ) + U ( q )$ ,i.e.,it is separable, thenthecondition(4.3)alone implies the symplecticity of thenumerical flow. □

Wehave seen in Sect.V.2.2 that within the class of partitioned Runge-Kutta methods itis possible toget explicit,symmetric methods for separable systems ${ \dot { y } } =$ $f ( z )$ , $\dot { z } ~ = ~ g ( y )$ Asimilar result holds for symplectic methods.However,asin Theorem V.2.6,such methods are not more general than composition or splitting methodsasconsidered in Sect.II.5.Thishas first been observed by Okunbor& Skeel(1992).

Theorem4.7.Considera partitioned Runge-Kuttamethod basedontwo diagonally implicit methods(i.e., $a _ { j i } = \overline { { a } } _ { j i } = 0$ for $i > j$ ),assume $a _ { i i } \cdot \widehat { a } _ { i i } = 0$ forall i,andapply it toa separable Hamiltonian systemwith $H ( p , q ) = T ( p ) + U ( q )$ 1f (4.3)holds,thenthenumerical result isthe sameas that obtained fromthe splitting method(11.5.6).

By(l.5.8),sucha method isequivalent toa composition of symplectic Euler steps.

ProofWe first notice that the stage values $k _ { i } = f ( Z _ { i } )$ (for $i$ with $b _ { i } = 0$ and $\ell _ { i } = g ( Y _ { i } )$ (for $i$ with $\widehat { b } _ { i } = 0$ donot influence the numerical solution and can be removed.This yieldsascheme with non-zero $b _ { i }$ and $\widehat { b } _ { i }$ ,but with possibly non-square matrices $( a _ { i j } )$ and $( \widehat { a } _ { i j } )$

Since the method is explicit for separable problems,one of thereduced matrices $( a _ { i j } )$ or $\left( \widehat { a } _ { i j } \right)$ hasarow consisting only of zeros.Assume that itis the first row of $( a _ { i j } )$ ,sothat $a _ { 1 j } = 0$ forall $j .$ The symplecticity condition thus implies $\widehat { a } _ { i 1 } = \widehat { b } _ { 1 } \neq$ $0$ forall $i \geq 1$ ,and $a _ { i 1 } = b _ { 1 } \neq 0$ for $i \geq 2$ Thisthenyields $\hat { a } _ { 2 2 } \neq 0$ ,because otherwise the first two stages of（ $\hat { a } _ { i j }$ )would be identical and one could be removed. By our assumption we get $a _ { 2 2 } = 0$ ， $\widehat { a } _ { i 2 } = \widehat { b } _ { 2 } \neq 0$ for $i \geq 2$ ,and $a _ { i 2 } = b _ { 2 }$ for $i \geq 3$ . Continuing this procedure we see that the method becomes

$$
\begin{array} { r } { \ldots \circ \varphi _ { \hat { b } _ { 2 } \hbar } ^ { [ 2 ] } \circ \varphi _ { b _ { 2 } \hbar } ^ { [ 1 ] } \circ \varphi _ { \hat { b } _ { 1 } \hbar } ^ { [ 2 ] } \circ \varphi _ { b _ { 1 } \hbar } ^ { [ 1 ] } , } \end{array}
$$

wherella and $\varphi _ { t } ^ { [ 2 ] }$ aretheeacf $T ( p )$ and $U ( q )$ ,respectively. □

Thenecessty of theconditions of Theorem 4.3and Theorem4.6for symplectic (partitioned) Runge-Kutta methodswill be discussedat the end of thischapterin Sect.VI.7.4.

A second order differential equation $\ddot { y } = g ( y )$ ,augmented by its variational equation,isagain of thisspecial form.Furthermore,the diagram ofLemma 4.1 commutes forNystrommethods,so that TheoremIV.2.5yieldsthe followingresult originally obtained by Suris(1988,1989).

Theorem4.8.IfthecoefficientsofaNystrommethod(IV.2.11) satisfy

$$
\begin{array} { c } { { \beta _ { i } = b _ { i } ( 1 - c _ { i } ) f o r i = 1 , \ldots , s , } } \\ { { { } } } \\ { { b _ { i } ( \beta _ { j } - a _ { i j } ) = b _ { j } ( \beta _ { i } - a _ { j i } ) f o r i , j = 1 , \ldots , s , } } \end{array}
$$

thenitis symplectic.

# VI.4.2 Connection Between Symplectic and Symmetric Methods

There exist symmetric methods that are not symplectic,and there exist symplectic methodsthat are not symmetric.For example,the trapezoidal rule

$$
y _ { 1 } = y _ { 0 } + { \frac { h } { 2 } } { \Big ( } f ( y _ { 0 } ) + f ( y _ { 1 } ) { \Big ) }
$$

issymmetric,but it does not satisfy the condition (4.2） for symplecticity.In fact, thisis true of all Lobatto IIIA methods(see Example II.2.2).On the other hand,any composition $\phi _ { \gamma _ { 1 } h } \circ \phi _ { \gamma _ { 2 } h }$ $\gamma _ { 1 } + \gamma _ { 2 } = 1$ ）ofsymplectic methodsissymplectic but symmetric onlyif $\gamma _ { 1 } = \gamma _ { 2 }$

However,for (non-partitioned) Runge-Kutta methods and for quadratic Hamiltonians $\begin{array} { r } { H ( y ) = \frac { 1 } { 2 } y ^ { T } C y } \end{array}$ （ $C$ isasymmetric real matrix),where the corresponding system(2.5)islinear,

$$
\begin{array} { r } { \dot { y } = J ^ { - 1 } C y , } \end{array}
$$

we shall see that both concepts are equivalent.

ARunge-Kutta method,applied with step size $h$ toalinear system $\dot { y } = L y$ ,is equivalentto

$$
y _ { 1 } = R ( h L ) y _ { 0 } ,
$$

where the rational function $R ( z )$ is given by

$$
R ( z ) = 1 + z b ^ { T } ( I - z A ) ^ { - 1 } \mathbb { 1 } ,
$$

$A = ( a _ { i j } )$ ， $b ^ { T } = ( b _ { 1 } , \ldots , b _ { s } )$ ,and $\mathbb { I } ^ { T } = ( 1 , \dots , 1 )$ The function $R ( z )$ is called thestability function of the method,and itis familiartous from thestudy of stiff differential equations(see e.g.,Hairer $\&$ Wanner(1996),Chap.IV.3).

Fortheexplicit Euler method,the implicit Eulermethodand the implicit midpoint rule,the stability function $R ( z )$ is given by

$$
1 + z , \qquad { \frac { 1 } { 1 - z } } , \qquad { \frac { 1 + z / 2 } { 1 - z / 2 } } .
$$

Theorem4.9.ForRunge-Kuttamethodsthefollowing statementsareequivalent:

·themethod issymmetric for linear problems $\dot { y } = \mathcal { L } y$ ·themethod issymplectic for problems(4.7)withsymmetric $C$ , ·thestability function satisfies $R ( - z ) R ( z ) = 1$ forall complex $z$ .

Proof.The method $y _ { 1 } = R ( h L ) y _ { 0 }$ is symmetric,ifandonly if $y _ { 0 } = R ( - h L ) y _ { 1 }$ holds forall initial values $y _ { 0 }$ But this is equivalent to $R ( - h L ) R ( h L ) = I .$

Since $\varPhi _ { h } ^ { \prime } ( y _ { 0 } ) = \underline { { R } } ( h L )$ ,symplecticityof themethod for the problem(4.7) is defined by $R ( h J ^ { - 1 } C ) ^ { T } J R ( h J ^ { - 1 } C ) = J .$ For $R ( z ) = P ( z ) / Q ( z )$ thisisequivalent to

$$
P ( h J ^ { - 1 } C ) ^ { T } J P ( h J ^ { - 1 } C ) = Q ( h J ^ { - 1 } C ) ^ { T } J Q ( h J ^ { - 1 } C ) .
$$

By the symmetry of $C$ thematrix $L : = J ^ { - 1 } C$ satisfies $L ^ { T } J = - J L$ and hence also $( L ^ { k } ) ^ { T } { \cal J } = { \cal J } ( - L ) ^ { k }$ for $k = 0 , 1 , 2 , \ldots .$ Consequently,(4.10)is equivalent to

$$
P ( - h J ^ { - 1 } C ) P ( h J ^ { - 1 } C ) = Q ( - h J ^ { - 1 } C ) Q ( h J ^ { - 1 } C ) ,
$$

which is nothing other than $R ( - h J ^ { - 1 } C ) R ( h J ^ { - 1 } C ) = I .$

# VI.5 Generating Functions

...bywhich the study of themotions of all free systems ofattracting or repellingpoints isreduced to the search and differentiation of one central relation,or characteristic function. (W.R.Hamilton 1834)

Professor Hamilton hat...das merkwurdige Resultat gefunden,dass... sichdie Integralgleichungen derBewegung...sammtlich durch die partiellen Differentialquotienten einer einzigen Function darstellen lassen.

(C.G.J.Jacobi 1837)

Weenter here the second heaven of Hamiltonian theory,the realm of partial differential equations and generating functions.The starting point of this theory was thediscovery of Hamilton that themotion of thesystem iscompletely described bya“characteristic”function $S$ ,andthat $S$ isthesolution ofa partial differential equation,nowcalled the Hamilton-Jacobidifferentialequation.

Itwasnoticed later,especially by Siegel (see Siegel&Moser 1971,\$3),that sucha function $S$ is directly connected to any symplectic map.It received the name generatingfunction.

# VI.5.1 Existence of Generating Functions

Wenow considera fixed Hamiltonian systemanda fixed time interval and denote by the column vectors $p$ and $q$ theinitialvalues $p _ { 1 } , \ldots , p _ { d }$ and $q _ { 1 } , \ldots , q _ { d }$ at $t _ { 0 }$ ofa trajectory.Thefinalvalues at $t _ { 1 }$ arewritten as $P$ and $Q$ We thus haveamapping $( p , q ) \mapsto ( P , Q )$ which,as we know,is symplectic on an open set $U$ .

Thefollowing results are conveniently formulated in the notation of differential forms.Fora function $F$ wedenote by $d { \cal F } = { \cal F } ^ { \prime }$ its(Frechet）derivative.We denote by $d q = ( d q _ { 1 } , \ldots , d q _ { d } ) ^ { T }$ thederivative of thecoordinate projection $( p , q ) \mapsto q$ .

Theorem 5.1.Amapping $\varphi : ( p , q ) \mapsto ( P , Q )$ issymplecticifandonly ifthere exists locallyafunction $S ( p , q )$ suchthat

$$
P ^ { T } d Q - p ^ { T } d q = d S .
$$

Thismeans that $P ^ { I } \ d Q - p ^ { T }$ dqisatotal differential.

Proof.We split the Jacobian of $\varphi$ into the natural $2 \times 2$ block matrix

$$
\frac { \partial ( P , Q ) } { \partial ( p , q ) } = \left( \begin{array} { l l } { { P _ { p } } } & { { P _ { q } } } \\ { { Q _ { p } } } & { { Q _ { q } } } \end{array} \right) ,
$$

Inserting this into (2.6)and multiplying out shows that the three conditions

$$
P _ { p } ^ { T } Q _ { p } = Q _ { p } ^ { T } P _ { p } , \qquad P _ { p } ^ { T } Q _ { q } - I = Q _ { p } ^ { T } P _ { q } , \qquad Q _ { q } ^ { T } P _ { q } = P _ { q } ^ { T } Q _ { q }
$$

are equivalent tosymplecticity.We now insert $d Q = Q _ { p } d p + Q _ { q } d q$ into the lefthand side of(5.1）and obtain

$$
\left( P ^ { T } Q _ { p } , P ^ { T } Q _ { q } - p ^ { T } \right) \left( \begin{array} { c } { { d p } } \\ { { d q } } \end{array} \right) = \left( \begin{array} { c c } { { Q _ { p } ^ { T } P } } \\ { { Q _ { q } ^ { T } P - p } } \end{array} \right) ^ { T } \left( \begin{array} { c } { { d p } } \\ { { d q } } \end{array} \right) .
$$

Toapplythe IntegrabilityLemma2.7,wejust haveto verifythe symmetryof the Jacobian of the coefficient vector,

$$
\left( { \begin{array} { l l } { Q _ { p } ^ { T } P _ { p } } & { Q _ { p } ^ { T } P _ { q } } \\ { Q _ { q } ^ { T } P _ { p } - I } & { Q _ { q } ^ { T } P _ { q } } \end{array} } \right) + \sum _ { i } P _ { i } { \frac { \partial ^ { 2 } Q _ { i } } { \partial ( p , q ) ^ { 2 } } } .
$$

Since the Hessians of $Q _ { i }$ aresymmetricanyway,itisimmediatelyclear that the symmetry of the matrix (5.3)is equivalent to the symplecticity conditions (5.2).□

Reconstruction of the Symplectic Map from $S$ .Up to now we have considered all functions as depending on $p$ and $q$ The essential idea now is to introduce new coordinates;namely（5.1）suggestsusing $z = ( q , Q )$ instead of $y = ( p , q )$ Thisisa well-defined local change of coordinates $y = \psi ( z )$ if $p$ can be expressed in terms of the coordinates $( q , Q )$ ,whichispossiblebytheimplicitfunctiontheoremif $\frac { \partial Q } { \partial p }$ is invertible.Abusing our notation we again write $S ( q , Q )$ forthe transformed function $S ( \psi ( z ) )$ Then,by comparing the coefficients of $\begin{array} { r } { d S = \frac { \partial S ( q , Q ) } { \partial q } d q + \frac { \partial S ( q , Q ) } { \partial Q } d Q } \end{array}$ with(5.1）,we arrive at3

$$
P = { \frac { \partial S } { \partial Q } } ( q , Q ) , \qquad p = - { \frac { \partial S } { \partial q } } ( q , Q ) .
$$

If the transformation $( p , q ) \mapsto ( P , Q )$ is symplectic,then it can be reconstructed from the scalar function $S ( q , Q )$ bytherelations (5.4).By Theorem5.1the converse isalso true:any sufficiently smooth and nondegenerate function $S ( q , Q )$ "generates"via(5.4)a symplecticmapping $( p , q ) \mapsto ( P , Q ) .$ This gives us a powerful tool forcreating symplectic methods.

Mixed-Variable Generating Functions.Another often useful choice of coordinates for generating symplectic maps are the mixed variables $( P , q )$ Forany continuouslydifferentiablefunction $\widehat { S } ( P , q )$ we clearly have $\begin{array} { r } { d \widehat { S } = \frac { \partial S } { \partial P } d P + \frac { \partial S } { \partial q } d q . } \end{array}$ On the other hand,since $d ( P ^ { I } Q ) = P ^ { I } d Q + Q ^ { I } d P$ ,thesymplecticity condition (5.1) can be rewritten as $Q ^ { T } d P + p ^ { I } d q = d ( Q ^ { I } P - S )$ forsome function $S .$ It therefore follows from Theorem5.1 that theequations

$$
Q = { \frac { \partial { \widehat { S } } } { \partial P } } ( P , q ) , \qquad p = { \frac { \partial { \widehat { S } } } { \partial q } } ( P , q )
$$

define (locally)asymplecticmap $( p , q ) \mapsto ( P , Q )$ if $\partial ^ { 2 } \vec { S } / \partial P \partial q$ is invertible.

Example 5.2.Let $Q = \chi ( q )$ bea change of position coordinates.With the generating function $\widehat { S } ( P , q ) = P ^ { T } \chi ( q )$ weobtainvia(5.5)an extension toa symplectic mapping $( p , q ) \mapsto ( P , Q ) .$ Theconjugate variables are thus related by $p = \chi ^ { \prime } ( q ) ^ { T } P .$

Mappings Closeto the Identity.Wearemainly interested in the situationwhere themapping $( p , q ) \mapsto ( P , Q )$ isclose to the identity.In this case,the choices $( p , Q )$ or $( P , q )$ or $( ( P + p ) / 2 , ( Q + q ) / 2 )$ of independent variables are convenient and lead to the following characterizations.

Lemma 5.3.Let $( p , q ) \mapsto ( P , Q )$ beasmoothtransformation,close totheidentity. $\boldsymbol { { t } }$ issymplecticifand onlyifone of thefollowingconditionsholds locally:

· $Q ^ { T } d P + p ^ { I } d q = d ( P ^ { I } q + S ^ { 1 } )$ for some function $S ^ { 1 } ( P , q )$ ; · $P ^ { T } d Q + q ^ { T } d p = d ( p ^ { L } Q - S ^ { 2 } )$ for some function $S ^ { 2 } ( p , Q )$ · $( Q - q ) ^ { T } d ( P + p ) - ( P - p ) ^ { T } d ( Q + q ) = 2 d S ^ { 3 }$ forsomefunction $S ^ { 3 } \big ( ( P + p ) / 2 , ( Q + q ) / 2 \big ) .$

Proof.The firstcharacterization follows from the discussion before formula(5.5)if weput $S ^ { 1 }$ such that $P ^ { T } q + S ^ { 1 } = \widehat { S } = Q ^ { T } P - S .$ For the second characterization we use $d ( p ^ { T } q ) = p ^ { T } d q + q ^ { T } d p$ and the same arguments as before.The last one follows from the fact that (5.1) is equivalent to $( Q - q ) ^ { T } d ( P + p ) - ( P - p ) ^ { T } d ( Q + q ) =$ $d \big ( ( P + p ) ^ { I } ( Q - q ) - 2 S \big )$ □

The generating functions $S ^ { 1 }$ , $S ^ { 2 }$ ,and $S ^ { 3 }$ have been chosen such that we obtain theidentity mappingwhen they arereplaced with zero.Comparing the coefficient functions of $d q$ and $d P$ inthefirstcharacterizationofLemma5.3,weobtain

$$
p = P + \frac { \partial S ^ { 1 } } { \partial q } ( P , q ) , \qquad Q = q + \frac { \partial S ^ { 1 } } { \partial P } ( P , q ) .
$$

Whatever the scalar function $S ^ { 1 } ( P , q )$ is,therelation(5.6)defines a symplectic transformation $( p , q ) \mapsto ( P , Q )$ For $S ^ { 1 } ( P , q ) : = h H ( P , q )$ we recognize the symplectic Euler method(I.1.9).This isanelegant proof of the symplecticity of this method.The second characterization leads to the adjoint of the symplectic Euler method.

The thirdcharacterization ofLemma5.3can bewrittenas

$$
\begin{array} { c } { P = { } p - { \partial _ { 2 } S ^ { 3 } \big ( ( P + p ) / 2 , ( Q + q ) / 2 \big ) } , } \\ { Q = { } q + { \partial _ { 1 } S ^ { 3 } \big ( ( P + p ) / 2 , ( Q + q ) / 2 \big ) } , } \end{array}
$$

which,for $S ^ { 3 } = h H$ ,isnothing other than the implicit midpoint rule(I.1.7) applied toaHamiltonian system.We haveused the notation $\partial _ { 1 }$ and $\partial _ { 2 }$ for the derivative with respect to the first and second argument,respectively.The system (5.7) can also be written in compact formas

$$
Y = y + J ^ { - 1 } \nabla S ^ { 3 } \big ( ( Y + y ) / 2 \big ) ,
$$

where $Y = ( P , Q )$ ， $y = ( p , q )$ , $S ^ { 3 } ( w ) = S ^ { 3 } ( u , v )$ with $w = ( u , v )$ ,and $J$ is the matrix of(2.3).

# VI.5.2 Generating Function for Symplectic Runge-Kutta Methods

Wehave just seen that all symplectic transformations can be written in terms of generating functions.What are these generating functions for symplectic Runge-Kutta methods?The followingresult,proved by Lasagni inan unpublished manuscript (with the same title as the note Lasagni(1988)）,givesan alternative proof for Theorem4.3.

Theorem5.4.Suppose that

$$
b _ { i } a _ { i j } + b _ { j } a _ { j i } = b _ { i } b _ { j } \quad f o r \ : a l l \ : \ : i , j
$$

(seeTheorem4.3).Then,the Runge-Kutta method

$$
\begin{array} { r l r } { P = p - h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } H _ { q } ( P _ { i } , Q _ { i } ) , } & { { } } & { P _ { i } = p - h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } H _ { q } ( P _ { j } , Q _ { j } ) , } \\ { Q = q + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } H _ { p } ( P _ { i } , Q _ { i } ) , } & { { } } & { Q _ { i } = q + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } H _ { p } ( P _ { j } , Q _ { j } ) } \end{array}
$$

can be written as(5.6)with

$$
S ^ { 1 } ( P , q , h ) = h \sum _ { i = 1 } ^ { s } b _ { i } H ( P _ { i } , Q _ { i } ) = h ^ { 2 } \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { i j } H _ { q } ( P _ { i } , Q _ { i } ) ^ { T } H _ { p } ( P _ { j } , Q _ { j } ) .
$$

Proof.We first differentiate $S ^ { 1 } ( P , q , h )$ with respect to $q$ Using the abbreviations $H [ i ] = H ( P _ { i } , Q _ { i } )$ ， $H _ { p } [ i ] = H _ { p } ( P _ { i } , Q _ { i } ) , \dots$ ,weobtain

$$
\begin{array} { r c l } { { \displaystyle \frac { \partial } { \partial q } \left( \sum _ { i } b _ { i } H [ i ] \right) } } & { { = } } & { { \displaystyle \sum _ { i } b _ { i } H _ { p } [ i ] ^ { T } \left( \frac { \partial p } { \partial q } - h \sum _ { j } a _ { i j } \frac { \partial } { \partial q } H _ { q } [ j ] \right) } } \\ { { } } & { { } } & { { + } } & { { \displaystyle \sum _ { i } b _ { i } H _ { q } [ i ] ^ { T } \left( I + h \sum _ { j } a _ { i j } \frac { \partial } { \partial q } H _ { p } [ j ] \right) . } } \end{array}
$$

With

$$
0 = \frac { \partial p } { \partial q } - h \sum _ { j } b _ { j } \frac { \partial } { \partial q } H _ { q } [ j ]
$$

(this isobtainedbydifferentiating the firstrelation of(5.1O),Leibniz'rule

$$
\frac { \partial } { \partial q } \big ( H _ { q } [ i ] ^ { T } H _ { p } [ j ] \big ) = H _ { q } [ i ] ^ { T } \frac { \partial } { \partial q } H _ { p } [ j ] + H _ { p } [ j ] ^ { T } \frac { \partial } { \partial q } H _ { q } [ i ]
$$

and the condition (5.9)therefore yield the first relation of

$$
\frac { \partial S ^ { 1 } ( P , q , h ) } { \partial q } = h \sum _ { i } b _ { i } H _ { q } [ i ] , \qquad \frac { \partial S ^ { 1 } ( P , q , h ) } { \partial P } = h \sum _ { i } b _ { i } H _ { p } [ i ] .
$$

Thesecond relation is proved in the same way.This shows that the Runge-Kutta formulas (5.10) are equivalent to(5.6). □

Itisinterestingto note that,whereas Lemma 5.3 guarantees the local existence ofa generating function $S ^ { 1 }$ ,theexplicit formula(5.11）shows that forRunge-Kutta methods thisgenerating function is globally defined.Thismeans that it iswelldefined in the sameregionwhere the Hamiltonian $H ( p , q )$ isdefined.

Theorem5.5.ApartitionedRunge-Kuttamethod(I.2.2),satisfyingthe symplecticityconditions (4.3)and(4.4),isequivalent to(5.6)with

$$
S ^ { 1 } ( P , q , h ) = h \sum _ { i = 1 } ^ { s } b _ { i } H ( P _ { i } , Q _ { i } ) - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } b _ { i } \widehat { a } _ { i j } H _ { q } ( P _ { i } , Q _ { i } ) ^ { T } H _ { p } ( P _ { j } , Q _ { j } ) .
$$

IftheHamiltonianis of the form $H ( p , q ) = T ( p ) + U ( q )$ ,i.e.,it is separable, thenthecondition(4.3)aloneimpliesthatthemethodisoftheform(5.6)with

$$
S ^ { \mathrm { i } } ( P , q , h ) = h \sum _ { i = 1 } ^ { s } \Big ( b _ { i } U ( Q _ { i } ) + \widehat { b } _ { i } T ( P _ { i } ) \Big ) - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } b _ { i } \widehat { a } _ { i j } U _ { q } ( Q _ { i } ) ^ { T } T _ { p } ( P _ { j } , ) .
$$

Proof.This isastraightforward extension of the proof of the previous theorem.

# VI.5.3The Hamilton-Jacobi Partial Differential Equation

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0004_pages_0211-0280/auto/images/a95c5d2da558fff02c6db157ceef074e63648745b525dfb392ab31c14be580ac.jpg)  
C.G.J. Jacobi4

We now return to the above construction of $S$ forasymplectic transformation $( p , q ) \mapsto$ $( P , Q )$ (seeTheorem5.1).This time,however,we imagine the point $P ( t ) , Q ( t )$ to move in theflow of the Hamiltonian system (1.7).We wish to determine asmooth generating function $S ( \boldsymbol { q } , \boldsymbol { Q } , t )$ ,now also depending on $t$ ,which generatesvia(5.4)thesymplectic map $( p , q ) \mapsto ( P ( t ) , Q ( t ) )$ of the exact flow of the Hamiltonian system.

In accordance with equation (5.4）we have to satisfy

$$
\begin{array} { c } { { P _ { i } ( t ) = \displaystyle \frac { \partial S } { \partial Q _ { i } } \big ( q , Q ( t ) , t \big ) , } } \\ { { { } } } \\ { { p _ { i } = \displaystyle - \frac { \partial S } { \partial q _ { i } } \big ( q , Q ( t ) , t \big ) . } } \end{array}
$$

Differentiating the secondrelation with respect to $t$ yields

$$
\begin{array} { l } { { \displaystyle 0 = \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial t } \big ( q , Q ( t ) , t \big ) + \sum _ { j = 1 } ^ { d } \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial Q _ { j } } \big ( q , Q ( t ) , t \big ) \cdot \dot { Q } _ { j } ( t ) } } \\ { { \displaystyle ~ = \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial t } \big ( q , Q ( t ) , t \big ) + \sum _ { j = 1 } ^ { d } \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial Q _ { j } } \big ( q , Q ( t ) , t \big ) \cdot \frac { \partial H } { \partial P _ { j } } \big ( P ( t ) , Q ( t ) \big ) } } \end{array}
$$

where we have inserted the second equation of(1.7) for ${ \dot { Q } } _ { j } .$ Then,using the chain rule,this equation simplifies to

$$
{ \frac { \partial } { \partial q _ { i } } } \left( { \frac { \partial S } { \partial t } } + H \Bigl ( { \frac { \partial S } { \partial Q _ { 1 } } } , \ldots , { \frac { \partial S } { \partial Q _ { d } } } , Q _ { 1 } , \ldots , Q _ { d } \Bigr ) \right) = 0 .
$$

This motivates the following surprisingly simple relation.

Theorem5.6.If $S ( \boldsymbol { q } , Q , t )$ isasmooth solutionof thepartial differentialequation

$$
{ \frac { \partial S } { \partial t } } + H \Bigl ( { \frac { \partial S } { \partial Q _ { 1 } } } , \dots , { \frac { \partial S } { \partial Q _ { d } } } , Q _ { 1 } , \dots , Q _ { d } \Bigr ) = 0
$$

withinitialvaluessatisfying $\begin{array} { r } { \frac { \partial S } { \partial q _ { i } } ( q , q , 0 ) + \frac { \partial S } { \partial Q _ { i } } ( q , q , 0 ) = 0 } \end{array}$ and if thematrix $\left( \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial Q _ { j } } \right)$ is invertible,then themap $( p , q ) \mapsto \left( P ( t ) , Q ( t ) \right)$ defined by (5.12)is theflow $\varphi _ { t } ( p , q )$ ofthe Hamiltonian system(1.7).

Proof.The invertibility of thematrix $\Bigl ( \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial Q _ { j } } \Bigr )$ and the implicit function theorem implythatthe mapping $( p , q ) \longmapsto \bigl ( P ( t ) , Q ( t ) \bigr )$ iswell-definedby (5.12),and,by differentiation,that(5.13)istrueaswell.

Since,by hypothesis, $S ( \boldsymbol { q } , \boldsymbol { Q } , t )$ isa solution of (5.16),the equations (5.15) andhencealso(5.14） aresatisfied.Subtracting(5.13) and(5.14),and once again usingthe invertibility of the matrix $\Big ( \frac { \partial ^ { 2 } S } { \partial q _ { i } \partial Q _ { j } } \Big ) \ ,$ we seethat necessarily ${ \dot { Q } } ( t ) =$ $H _ { p } \left( P ( t ) , Q ( t ) \right) .$ This proves the validity of the second equation of the Hamiltonian system (1.7).

The first equation of(1.7)is obtained as follows:differentiate the first relation of（5.12）with respect to $t$ and the Hamilton-Jacobi equation(5.16) with respect to $Q _ { i }$ ,then eliminatethe term $\frac { \partial ^ { 2 } S } { \partial Q _ { i } \partial t }$ Using $Q ( t ) = H _ { p } { \big ( } P ( t ) , Q ( t ) { \big ) }$ ,this leads in a straightforward way to $P ( t ) = - H _ { q } \bigl ( P ( t ) , Q ( t ) \bigr ) .$ The condition on the initial values of $S$ ensures that $( P ( 0 ) , Q ( 0 ) ) = ( p , q )$ . □

Inthehands of Jacobi(1842),thisequation turned into a powerful tool for the analytic integration of manydifficult problems.Onehas,in fact,to findasolution of(5.16)which contains sufficiently many parameters.Thisis often possible with themethod of separation of variables.An example ispresented in Exercise11.

Hamilton-Jacobi Equation for $S ^ { 1 }$ ， $S ^ { 2 }$ ,and $S ^ { 3 }$ We now express the Hamilton-Jacobidifferential equationinthe coordinatesused inLemma 5.3.In thesecoordinates itisalsopossible to prescribeinitial values for $S$ at $t = 0$ ,

Fromtheproof ofLemma 5.3we know that the generating functionsin the variables $( q , Q )$ and $( P , q )$ arerelated by

$$
S ^ { 1 } ( P , q , t ) = P ^ { T } ( Q - q ) - S ( q , Q , t ) .
$$

Weconsider $P , q , t$ asindependentvariables,and we differentiate thisrelationwith respectto $t$ Using the first relation of(5.12) thisgives

$$
\frac { \partial S ^ { 1 } } { \partial t } ( P , q , t ) = P ^ { T } \frac { \partial Q } { \partial t } - \frac { \partial S } { \partial Q } ( q , Q , t ) \frac { \partial Q } { \partial t } - \frac { \partial S } { \partial t } ( q , Q , t ) = - \frac { \partial S } { \partial t } ( q , Q , t ) .
$$

Differentiating（5.17)with respect to $P$ yields

$$
\frac { \partial S ^ { 1 } } { \partial P } ( P , q , t ) = Q - q + P ^ { T } \frac { \partial Q } { \partial P } - \frac { \partial S } { \partial Q } ( q , Q , t ) \frac { \partial Q } { \partial P } = Q - q .
$$

Inserting $\begin{array} { r } { \frac { \partial S } { \partial Q } = P } \end{array}$ and $\begin{array} { r } { Q = q + \frac { \partial S ^ { \bot } } { \partial P } } \end{array}$ into the Hamilton-Jacobi equation (5.16)we areled to the equation of the followingtheorem.

Theorem5.7.If $S ^ { 1 } ( P , q , t )$ isasolution ofthepartial differentialequation

$$
\frac { \partial S ^ { 1 } } { \partial t } ( P , q , t ) = H \Big ( P , q + \frac { \partial S ^ { 1 } } { \partial P } ( P , q , t ) \Big ) , \qquad S ^ { 1 } ( P , q , 0 ) = 0 ,
$$

then the mapping $( p , q ) \mapsto ( P ( t ) , Q ( t ) )$ definedby(5.6),istheexactflowof the Hamiltonian system(1.7).

Proof.Whenever themapping $( p , q ) \mapsto ( P ( t ) , Q ( t ) )$ can bewritenas(5.12）with a function $S ( \boldsymbol { q } , Q , t )$ ,andwhen theinvertibilityassumptionof Theorem5.6 holds, theproof is done by the above calculations.Since our mapping,for $t = 0$ ,reduces to the identity and cannot be written as(5.12),we give a direct proof.

Let $S ^ { 1 } ( P , q , t )$ begiven by the Hamilton-Jacobi equation (5.18),and assume that $( p , q ) \mapsto ( P , Q ) = ( P ( t ) , Q ( t ) )$ is the transformation given by(5.6).Differentiation of the first relation of（5.6)with respect to time $t$ and using（5.18）yields5

$$
\stackrel { \prime } { \cal I } + \frac { \partial ^ { 2 } S ^ { 1 } } { \partial P \partial q } ( P , q , t ) \Big ) \dot { P } = - \frac { \partial ^ { 2 } S ^ { 1 } } { \partial t \partial q } ( P , q , t ) = - \Big ( \bar { \cal I } + \frac { \partial ^ { 2 } S ^ { 1 } } { \partial P \partial q } ( P , q , t ) \Big ) \frac { \partial H } { \partial Q } ( P , q , t ) .
$$

Differentiation of the second relation of(5.6)gives

$$
\begin{array} { l } { \displaystyle { \dot { Q } = \frac { \partial ^ { 2 } S ^ { 1 } } { \partial t \partial P } ( P , q , t ) + \frac { \partial ^ { 2 } S ^ { 1 } } { \partial P ^ { 2 } } ( P , q , t ) \dot { P } } } \\ { \displaystyle { \ = \ \frac { \partial H } { \partial P } ( P , Q ) + \frac { \partial ^ { 2 } S ^ { 1 } } { \partial P ^ { 2 } } ( P , q , t ) \Big ( \frac { \partial H } { \partial Q } ( P , Q ) + \dot { P } \Big ) . } } \end{array}
$$

Consequently, $\begin{array} { r } { \dot { P } ~ = ~ - \frac { \partial H } { \partial Q } ( P , Q ) } \end{array}$ and $\begin{array} { r } { \boldsymbol { Q } \ = \ \frac { \partial H } { \partial \boldsymbol { P } } ( \boldsymbol { P } , \boldsymbol { Q } ) } \end{array}$ ,so that $\big ( P ( t ) , Q ( t ) \big ) \ =$ $\varphi _ { t } ( p , q )$ isthe exact flow of the Hamiltonian system. □

Writing the Hamilton-Jacobi differential equation inthe variables $( P + p ) / 2$ , $( Q + q ) / 2$ gives the following formula.

Theorem5.8. Assume that $S ^ { 3 } ( u , v , t )$ is a solution of

$$
\frac { \partial S ^ { 3 } } { \partial t } ( u , v , t ) = H \Big ( u - \frac { 1 } { 2 } \frac { \partial S ^ { 3 } } { \partial v } ( u , v , t ) , v + \frac { 1 } { 2 } \frac { \partial S ^ { 3 } } { \partial u } ( u , v , t ) \Big )
$$

with initial condition $S ^ { 3 } ( u , v , 0 ) = 0$ Then,theexact flow $\varphi _ { t } ( p , q )$ ofthe Hamiltonian system(1.7) satisfes the system(5.7).

Proof.As in theproof of Theorem5.7,one considers the transformation $( p , q ) \mapsto$ $\left( P ( t ) , Q ( t ) \right)$ defined by(5.7),and thenchecks bydifferentiation that $\left( P ( t ) , Q ( t ) \right)$ isa solution of the Hamiltonian system(1.7). □

Writing $w = ( u , v )$ and using the matrix $J$ of(2.3),the Hamilton-Jacobi equation(5.19) can also be written as

$$
\frac { \partial S ^ { 3 } } { \partial t } ( w , t ) = H \Big ( w + \frac { 1 } { 2 } J ^ { - 1 } \nabla S ^ { 3 } ( w , t ) \Big ) , \qquad S ^ { 3 } ( w , 0 ) = 0 .
$$

The solution of (5.20) is anti-symmetric in $t$ ,i.e.,

$$
S ^ { 3 } ( w , - t ) = - S ^ { 3 } ( w , t ) .
$$

This can be seen as follows:let $\varphi _ { t } ( w )$ be theexact flow of the Hamiltonian system $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) , } \end{array}$ Because of(5.8）， $S ^ { 3 } ( w , t )$ isdefined by

$$
{ \varphi } _ { t } ( w ) - w = J ^ { - 1 } \nabla S ^ { 3 } \big ( ( { \varphi } _ { t } ( w ) + w ) / 2 , t \big ) .
$$

Replacing $t$ with $- t$ and then $w$ with $\varphi _ { t } ( w )$ we get from $\varphi _ { - t } \mathopen { } \mathclose \bgroup \left( \varphi _ { t } ( t ) \aftergroup \egroup \right) = w$ that

$$
w - \varphi _ { t } ( w ) = J ^ { - 1 } \nabla S ^ { 3 } \big ( ( w + \varphi _ { t } ( w ) ) / 2 , - t \big ) .
$$

Hence $S ^ { 3 } ( w , t )$ and $- S ^ { 3 } ( w , - t )$ are generating functions of the same symplectic transformation.Since generating functions are unique up to an additive constant (because $d S = 0$ implies $S = \mathcal { C } o n s t )$ ,theanti-symmetry(5.21） follows from the initial condition $S ^ { 3 } ( w , 0 ) = 0$ .

# VI.5.4 Methods Based on Generating Functions

To construct symplectic numerical methods of high order,Feng Kang(1986),Feng Kang,Wu,Qin&Wang（1989)and Channell&Scovel（1990)proposedcomputing anapproximate solution of the Hamilton-Jacobi equation.For this one insertsthe ansatz

$$
S ^ { 1 } ( P , q , t ) = t G _ { 1 } ( P , q ) + t ^ { 2 } G _ { 2 } ( P , q ) + t ^ { 3 } G _ { 3 } ( P , q ) + . . .
$$

into (5.18),and compares like powers of $t$ Thisyields

$$
\begin{array} { l } { { G _ { 1 } ( P , q ) ~ = ~ H ( P , q ) , } } \\ { { G _ { 2 } ( P , q ) ~ = ~ \frac { 1 } { 2 } \Bigl ( \frac { \partial H } { \partial P } \frac { \partial \bar { H } } { \partial q } \Bigr ) ( P , q ) , } } \\ { { G _ { 3 } ( P , q ) ~ = ~ \frac { 1 } { 6 } \Bigl ( \frac { \partial ^ { 2 } H } { \partial P ^ { 2 } } \Bigl ( \frac { \partial H } { \partial q } \Bigr ) ^ { 2 } + \frac { \partial ^ { 2 } H } { \partial P \partial q } \frac { \partial H } { \partial P } \frac { \partial H } { \partial q } + \frac { \partial ^ { 2 } H } { \partial q ^ { 2 } } \Bigl ( \frac { \partial H } { \partial P } \Bigr ) ^ { 2 } \Bigr ) ( P , q ) . } } \end{array}
$$

Ifwe use the truncated series

$$
S ^ { 1 } ( P , q ) = h G _ { 1 } ( P , q ) + h ^ { 2 } G _ { 2 } ( P , q ) + . . . + h ^ { r } G _ { r } ( P , q )
$$

and insert it into(5.6),the transformation $( p , q ) \mapsto ( P , Q )$ defines a symplectic onestepmethod of order $\tau$ SymplecticityfollowsatoncefromLemma5.3andorder $r$ isaconsequence of the fact that the truncation of $S ^ { 1 } ( P , q )$ introduces aperturbation ofsize $\mathcal { O } ( h ^ { r + 1 } )$ in（5.18）.Weremark that for $r \geq 2$ themethods obtained require thecomputation of higher derivatives of $H ( p , q )$ ,and for separableHamiltonians $H ( p , q ) = T ( p ) + U ( q )$ theyare no longer explicit (compared to the symplectic Euler method (3.1)).

Thesame approach applied to the third characterization ofLemma5.3yields

$$
S ^ { 3 } ( w , h ) = h G _ { 1 } ( w ) + h ^ { 3 } G _ { 3 } ( w ) + . . . + h ^ { 2 r - 1 } G _ { 2 r - 1 } ( w ) ,
$$

where $G _ { 1 } ( w ) = H ( w )$ ,

$$
G _ { 3 } ( w ) \equiv \frac { 1 } { 2 4 } \nabla ^ { 2 } H ( w ) \Big ( J ^ { - 1 } \nabla H ( w ) , J ^ { - 1 } \nabla H ( w ) \Big ) ,
$$

and further $G _ { j } ( w )$ can be obtained by comparing like powers of $h { : }$ in (5.20).In this waywe get symplectic methods of order $_ { 2 r }$ .Since $S ^ { 3 } ( w , h )$ has an expansion in odd powers of $h$ ,theresultingmethod is symmetric.

TheApproachofMiesbach&Pesch.Withtheaimofavoidinghigherderivatives oftheHamiltonian inthe numerical method,Miesbach&Pesch（1992）propose considering generating functions of the form

$$
S ^ { 3 } ( w , h ) = h \sum _ { i = 1 } ^ { s } b _ { i } H \Big ( w + h c _ { i } J ^ { - 1 } \nabla H ( w ) \Big ) ,
$$

and to determine the free parameters $b _ { i } , c _ { i }$ in such a way that the function of(5.23) agreeswith the solution of the Hamilton-Jacobi equation (5.20)up toacertain order. For $b _ { s + 1 - i } = b _ { i }$ and $c _ { s + 1 - i } = - c _ { i }$ this function satisfies $S ^ { 3 } ( w , - h ) = - S ^ { 3 } ( w , h )$ , sothat the resulting method is symmetric.A straightforward computation shows that ityieldsamethod of order4if

$$
\sum _ { i = 1 } ^ { s } b _ { i } = 1 , \qquad \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 2 } = { \frac { 1 } { 1 2 } } .
$$

For $s = 3$ ,these equations are fulfilled for $b _ { 1 } = b _ { 3 } = 5 / 1 8$ , $b _ { 2 } = 4 / 9$ , $c _ { 1 } = - c _ { 3 } =$ $\sqrt { 1 5 } / 1 0$ ,and $c _ { 2 } = 0$ .Since the function $S ^ { 3 }$ of(5.23) has to be inserted into (5.20), thesemethods still need second derivatives of the Hamiltonian.

# VI.6 Variational Integrators

Athird approach to symplectic integrators comes from using discretized versions ofHamilton's principle,which determines the equations of motion from a variational problem.Thisroute hasbeentakenby Suris(199O),MacKay(1992）and ina series of papers by Marsdenand coauthors,see the review by Marsden& West (2oo1） and references therein.Basic theoretical properties were formulated byMaeda(1980,1982)and Veselov(1988,1991）inanon-numericalcontext.

# VI.6.1Hamilton's Principle

Ours,according toLeibniz,isthe best of all possible worlds,and the laws ofnature can therefore be described in terms of extremal principles. (C.L.Siegel&J.K.Moser1971,p.1)

Manscheint dies Princip fruher...unbemerkt gelassen zu haben.   
Hamilton ist der erste,dervon diesem Principausgegangen ist. (C.G.J.Jacobi 1842,p.

Hamilton gave an improved mathematical formulation of a principle whichwaswell established by the fundamental investigations of Euler andLagrange;the integration process employed by him was likewise knowntoLagrange.The name“Hamilton'sprinciple",coined by Jacobi, wasnot adopted by the scientists of the last century.It came into use, however,through the textbooksofmorerecent date.

(C.Lanczos 1949,p.114)

Lagrange'sequations of motion(1.4）can be viewed as the Euler-Lagrange equations forthe variational problem of extremizing the action integral

$$
S ( q ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } L ( q ( t ) , \dot { q } ( t ) ) d t
$$

among all curves $q ( t )$ that connect two given points $q _ { 0 }$ and $q _ { 1 }$ :

$$
q ( t _ { 0 } ) = q _ { 0 } , \quad q ( t _ { 1 } ) = q _ { 1 } .
$$

In fact,assuming $q ( t )$ tobeextremal and considering a variation $\boldsymbol { q } ( t ) + \varepsilon \delta \boldsymbol { q } ( t )$ with the same end-points,i.e.,with $\delta q ( t _ { 0 } ) = \delta q ( t _ { 1 } ) = 0$ gives,usingapartial integration,

$$
= { \frac { d } { d \varepsilon } } { \Big | } _ { \varepsilon = 0 } S ( q + \varepsilon \delta q ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } \left( { \frac { \partial L } { \partial q } } \delta q + { \frac { \partial L } { \partial { \dot { q } } } } \delta { \dot { q } } \right) d t = \int _ { t _ { 0 } } ^ { t _ { 1 } } \left( { \frac { \partial L } { \partial q } } - { \frac { d } { d t } } { \frac { \partial L } { \partial { \dot { q } } } } \right) \delta q
$$

which leadsto(1.4).The principle that the motion extremizes the action integral is knownas Hamilton'sprinciple.

We now consider the action integral asa function of $( q _ { 0 } , q _ { 1 } )$ ,for the solution $q ( t )$ oftheEuler-Lagrange equations（1.4）with these boundaryvalues(this exists uniquely locallyat least if $q _ { 0 } , q _ { 1 }$ aresufficiently close),

$$
S ( q _ { 0 } , q _ { 1 } ) = \int _ { t _ { 0 } } ^ { t _ { 1 } } L ( q ( t ) , \dot { q } ( t ) ) d t .
$$

The partial derivative of $S$ with respect to $q _ { 0 }$ is,again using partial integration,

$$
\begin{array} { l } { { \displaystyle { \frac { \partial S } { \partial q _ { 0 } } } } ~ = ~ \int _ { t _ { 0 } } ^ { t _ { 1 } } \left( { \frac { \partial L } { \partial q } } { \frac { \partial q } { \partial q _ { 0 } } } + { \frac { \partial L } { \partial { \dot { q } } } } { \frac { \partial { \dot { q } } } { \partial q _ { 0 } } } \right) d t } \\ { ~ = ~ { \displaystyle { \frac { \partial L } { \partial { \dot { q } } } } } { \frac { \partial q } { \partial q _ { 0 } } } { \displaystyle { \Big | _ { t _ { 0 } } ^ { t _ { 1 } } } } + \int _ { t _ { 0 } } ^ { t _ { 1 } } \left( { \frac { \partial L } { \partial q } } - { \frac { d } { d t } } { \frac { \partial L } { \partial { \dot { q } } } } \right) { \frac { \partial q } { \partial q _ { 0 } } } d t = - { \displaystyle { \frac { \partial L } { \partial { \dot { q } } } } } ( q _ { 0 } , { \dot { q } } _ { 0 } ) } \end{array}
$$

with $\dot { q } _ { 0 } = \dot { q } ( t _ { 0 } )$ ,where thelast equality follows from(1.4)and(6.2).In view of the definition(1.5) of the conjugatemomenta, $p = \partial L / \partial { \dot { q } }$ ,thelast termissimply $- p _ { 0 }$ Computing $\partial S / \partial q _ { 1 } = p _ { 1 }$ inthe sameway,we thus obtain for the differential of $S$

$$
d S = { \frac { \partial S } { \partial q _ { 1 } } } d q _ { 1 } + { \frac { \partial S } { \partial q _ { 0 } } } d q _ { 0 } = p _ { 1 } d q _ { 1 } - p _ { 0 } d q _ { 0 }
$$

whichis the basic formula forsymplecticity generating functions (see(5.1) above), obtained hereby workingwiththeLagrangian formalism.

# VI.6.2Discretization of Hamilton's Principle

Discrete-time versions of Hamilton's principle are of mathematical interest in their ownright,seeMaeda(1980,1982),Veselov(1991) and references therein.Here they areconsidered with the aim of deriving orunderstanding numerical approximation schemes.The discretized Hamilton principle consists of extremizing,for given $q _ { 0 }$ and $q _ { N }$ ,thesum

$$
S _ { h } ( \{ q _ { n } \} _ { 0 } ^ { N } ) = \sum _ { n = 0 } ^ { N - 1 } L _ { h } ( q _ { n } , q _ { n + 1 } ) .
$$

Wethink ofthediscreteLagrangian $L _ { h }$ asan approximation

$$
L _ { h } ( q _ { n } , q _ { n + 1 } ) \approx \int _ { t _ { n } } ^ { t _ { n + 1 } } L ( q ( t ) , \dot { q } ( t ) ) d t ,
$$

where $q ( t )$ isthesolution of the Euler-Lagrange equations（1.4）with boundary values $q ( t _ { n } ) = q _ { n }$ ， $q ( t _ { n + 1 } ) ~ = ~ q _ { n + 1 }$ If equality holdsin(6.6),thenitisclear from the continuous Hamilton principle that the exact solution values $\{ q ( t _ { n } ) \}$ of the Euler-Lagrange equations（1.4） extremize the action sum $S _ { h }$ Beforewe turn to concrete examples of approximations $L _ { h }$ ,wecontinue with the general theory which is analogous to the continuous case.

Therequirement $\partial S _ { h } / \partial q _ { n } \ = \ 0$ foranextremumyields the discrete Euler-Lagrange equations

$$
\frac { \partial L _ { h } } { \partial y } ( q _ { n - 1 } , q _ { n } ) + \frac { \partial L _ { h } } { \partial x } ( q _ { n } , q _ { n + 1 } ) = 0
$$

for $n = 1 , \ldots , N - 1$ ,where the partial derivatives refer to $L _ { h } = L _ { h } ( x , y ) .$ This givesathree-term difference scheme for determining $q _ { 1 } , \ldots , q _ { N - 1 }$

We now set

$$
S _ { h } ( q _ { 0 } , q _ { N } ) = \sum _ { n = 0 } ^ { N - 1 } L _ { h } ( q _ { \cdot } , q _ { n + 1 } )
$$

where $\left\{ q _ { n } \right\}$ isa solution of the discrete Euler-Lagrange equations (6.7）with the boundaryvalues $q _ { 0 }$ and $q N$ With(6.7） the partial derivativesreduce to

$$
\frac { \partial S _ { h } } { \partial q _ { 0 } } = \frac { \partial L _ { h } } { \partial x } ( q _ { 0 } , q _ { 1 } ) , ~ \frac { \partial S _ { h } } { \partial q _ { N } } = \frac { \partial L _ { h } } { \partial y } ( q _ { N - 1 } , q _ { N } ) .
$$

Weintroduce thediscretemomenta viaadiscreteLegendre transformation,

$$
p _ { n } = - \frac { \partial L _ { h } } { \partial x } ( q _ { n } , q _ { n + 1 } ) \ .
$$

The above formulaand(6.7) for $n = N$ then yield

$$
d S _ { h } = p _ { N } d q _ { N } - p _ { 0 } d q _ { 0 } .
$$

If(6.8)defines a bijection between $p _ { n }$ and $q _ { n + 1 }$ forgiven $q _ { n }$ ,thenwe obtaina one-stepmethod $\begin{array} { r } { \phi _ { h } : ( p _ { n } , q _ { n } ) \mapsto ( p _ { n + 1 } , q _ { n + 1 } ) } \end{array}$ by composing the inverse discreteLegendre transform,a step with the discrete Euler-Lagrange equations,and the discrete Legendre transformation as shown in the diagram:

$$
\begin{array} { r l r } { ( q _ { n } , q _ { n + 1 } ) \quad } & { \stackrel { ( 6 . 7 ) } { \longrightarrow } } & { \quad ( q _ { n + 1 } , q _ { n + 2 } ) } \\ { ( 6 . 8 ) \prod \quad } & { \quad } & { \stackrel { \prod } { \longrightarrow } ( 6 . 8 ) } \\ { ( p _ { n } , q _ { n } ) \quad } & { \quad } & { ( p _ { n + 1 } , q _ { n + 1 } ) } \end{array}
$$

The method is symplectic by(6.9)and Theorem5.1.A short-cutinthe computation is obtainedby noting that(6.7)and(6.8)（for $n + 1$ instead of $^ { n }$ )imply

$$
p _ { n + 1 } = { \frac { \partial L _ { h } } { \partial y } } ( q _ { n } , q _ { n + 1 } ) \ ,
$$

which yields the scheme

$$
( p _ { n } , q _ { n } ) \stackrel { ( 6 . 8 ) } { \longrightarrow } ( q _ { n } , q _ { n + 1 } ) \stackrel { ( 6 . 1 0 ) } { \longrightarrow } ( p _ { n + 1 } , q _ { n + 1 } ) .
$$

Let us summarize these considerations,which can be found in Maeda (198o),Suris (1990),Veselov(1991) and MacKay(1992).

Theorem6.1.Thediscrete Hamiltonprinciplefor(6.5) givesthediscrete Euler-Lagrange equations (6.7) and the symplectic method

$$
p _ { n } = - \frac { \partial L _ { h } } { \partial x } ( q _ { n } , q _ { n + 1 } ) , \quad p _ { n + 1 } = \frac { \partial L _ { h } } { \partial y } ( q _ { n } , q _ { n + 1 } ) .
$$

These formulas also show that $L _ { h }$ isagenerating function (5.4) for the symplecticmap $( p _ { n } , q _ { n } ) \mapsto ( p _ { n + 1 } , q _ { n + 1 } ) .$ Conversely,since every symplectic method hasagenerating function(5.4),itcan be interpreted as resulting from Hamilton’s principlewith the generating function(5.4）as thediscreteLagrangian.Theclasses ofsymplecticintegrators and variational integratorsare therefore identical.

Wenow turnto simpleexamples of variational integratorsobtained bychoosing adiscrete Lagrangian $L _ { h }$ with(6.6).

Example6.2 (MacKay 1992). Choose $L _ { h } ( q _ { n } , q _ { n + 1 } )$ byapproximating $q ( t )$ of (6.6)as the linear interpolant of $q _ { n }$ and $q _ { n + 1 }$ andapproximating the integral by thetrapezoidal rule.This gives

$$
L _ { h } ( q _ { n } , q _ { n + 1 } ) = { \frac { h } { 2 } } L \Bigl ( q _ { n } , { \frac { q _ { n + 1 } - q _ { n } } { h } } \Bigr ) + { \frac { h } { 2 } } L \Bigl ( q _ { n + 1 } , { \frac { q _ { n + 1 } - q _ { n } } { h } } \Bigr )
$$

and hence the symplectic scheme,with $v _ { n + 1 / 2 } = ( q _ { n + 1 } - q _ { n } ) / h$ forbrevity,

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n } ~ = ~ \displaystyle { \frac { 1 } { 2 } \frac { \partial L } { \partial \dot { q } } ( q _ { n } , v _ { n + 1 / 2 } ) + \frac { 1 } { 2 } \frac { \partial L } { \partial \dot { q } } ( q _ { n + 1 } , v _ { n + 1 / 2 } ) - \frac { h } { 2 } \frac { \partial L } { \partial q } ( q _ { n } , v _ { n + 1 / 2 } ) } } } \\ { { } } & { { } } & { { { } } } \\  { \dot { \displaystyle { \it \gamma _ { n + 1 } } } ~ = ~ \displaystyle { \frac { 1 } { 2 } \frac { \partial L } { \partial \dot { q } } ( q _ { n } , v _ { n + 1 / 2 } ) + \frac { 1 } { 2 } \frac { \partial L } { \partial \dot { q } } ( q _ { n + 1 } , v _ { n + 1 / 2 } ) + \frac { h } { 2 } \frac { \partial L } { \partial q } ( q _ { n + 1 } , v _ { n + 1 / 2 } ) . } } \end{array}
$$

Foramechanical Lagrangian $\begin{array} { r } { L ( q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { T } M \dot { q } - U ( q ) } \end{array}$ this reduces to the Stormer-Verletmethod

$$
\begin{array} { r c l } { { } } & { { } } & { { M v _ { n + 1 / 2 } ~ = ~ p _ { n } + \displaystyle \frac { 1 } { 2 } h F _ { n } } } \\ { { } } & { { } } & { { q _ { n + 1 } ~ = ~ q _ { n } + h v _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } ~ \equiv ~ M v _ { n + 1 / 2 } + \displaystyle \frac { 1 } { 2 } h F _ { n + 1 } } } \end{array}
$$

where $F _ { n } = - \nabla U ( q _ { n } ) .$ Inthiscase,the discrete Euler-Lagrange equations (6.7) become the familiar second-difference formula $M ( q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } ) = h ^ { 2 } F _ { n } .$

Example6.3(Wendlandt&Marsden 1997).Approximatingtheintegral in(6.6 insteadbythemidpoint rule gives

$$
L _ { h } ( q _ { n } , q _ { n + 1 } ) = h L \Bigl ( \frac { q _ { n + 1 } + q _ { n } } { 2 } , \frac { q _ { n + 1 } - q _ { n } } { h } \Bigr ) .
$$

This yields the symplectic scheme,with the abbreviations $q _ { n + 1 / 2 } = ( q _ { n + 1 } + q _ { n } ) / 2$ and $v _ { n + 1 / 2 } = ( q _ { n + 1 } - q _ { n } ) / h ,$

$$
\begin{array} { r c l } { { p _ { n } = \displaystyle \frac { \partial { \cal L } } { \partial \dot { q } } ( q _ { n + 1 / 2 } , v _ { n + 1 / 2 } ) - \displaystyle \frac { h } { 2 } \displaystyle \frac { \partial { \cal L } } { \partial q } ( q _ { n + 1 / 2 } , v _ { n + 1 / 2 } ) } } \\ { { } } & { { } } \\ { { p _ { n + 1 } = \displaystyle \frac { \partial { \cal L } } { \partial \dot { q } } ( q _ { n + 1 / 2 } , v _ { n + 1 / 2 } ) + \displaystyle \frac { h } { 2 } \displaystyle \frac { \partial { \cal L } } { \partial q } ( q _ { n + 1 / 2 } , v _ { n + 1 / 2 } ) . } } \end{array}
$$

For $L ( q , \dot { q } ) = \textstyle { \frac { 1 } { 2 } } \dot { q } ^ { T } M \dot { q } - U ( q )$ this becomes the implicit midpoint rule

$$
\begin{array} { r c l } { { } } & { { } } & { { M v _ { n + 1 / 2 } \ = \ p _ { n } + \frac { 1 } { 2 } h F _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { q _ { n + 1 } \ = \ q _ { n } + h v _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } \ = \ M v _ { n + 1 / 2 } + \frac { 1 } { 2 } h F _ { n + 1 / 2 } } } \end{array}
$$

with $F _ { n + 1 / 2 } = - \nabla U \big ( \frac { 1 } { 2 } \big ( q _ { n + 1 } + q _ { n } \big ) \big ) .$

# VI.6.3Symplectic Partitioned Runge-Kutta Methods Revisited

Toobtain higher-ordervariational integrators,Marsden&West(2Oo1）consider the discrete Lagrangian

$$
L _ { h } ( q _ { 0 } , q _ { 1 } ) = h \sum _ { i = 1 } ^ { s } b _ { i } L \big ( u ( c _ { i } h ) , \dot { u } ( c _ { i } h ) \big )
$$

where $u ( t )$ is the polynomial of degree s with $u ( 0 ) = q _ { 0 }$ ， $u ( h ) = q _ { 1 }$ which extremizes theright-hand side.They then show that the correspondingvariational integrator can berealizedasapartitioned Runge-Kutta method.We here consider the slightly more general case

$$
L _ { h } ( q _ { 0 } , q _ { 1 } ) = h \sum _ { i = 1 } ^ { s } b _ { i } L ( Q _ { i } , \dot { Q } _ { i } )
$$

where

$$
Q _ { i } = q _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } \dot { Q } _ { j }
$$

and the ${ \dot { Q } } _ { i }$ are chosen to extremize the above sum underthe constraint

$$
q _ { 1 } = q _ { 0 } + h . \sum _ { i = 1 } ^ { s } b _ { i } { \dot { Q } } _ { i } .
$$

Weassume that all the $b _ { i }$ are non-zero and that their sum equals 1.Note that(6.14) is the special case of(6.15) where the $a _ { i j }$ and $b _ { i }$ are integrals (II.1.10)ofLagrange polynomials as for collocation methods.

WithaLagrange multiplier $\lambda = ( \lambda _ { 1 } , \ldots , \lambda _ { d } )$ forthe constraint,the extremality conditions obtained by differentiating (6.15）with respect to ${ \dot { Q } } _ { j }$ for $j = 1 , \dotsc , s ,$ , read

$$
\sum _ { i = 1 } ^ { s } b _ { i } \frac { \partial L } { \partial q } ( Q _ { i } , \dot { Q } _ { i } ) h a _ { i j } + b _ { j } \frac { \partial L } { \partial \dot { q } } ( Q _ { j } , \dot { Q } _ { j } ) = b _ { j } \lambda .
$$

With the notation

$$
\dot { P } _ { i } = \frac { \partial L } { \partial q } ( Q _ { i } , \dot { Q } _ { i } ) , P _ { i } = \frac { \partial L } { \partial \dot { q } } ( Q _ { i } , \dot { Q } _ { i } )
$$

this simplifies to

$$
b _ { j } P _ { j } = b _ { j } \lambda - h \sum _ { i = 1 } ^ { s } b _ { i } a _ { i j } \dot { P } _ { i } .
$$

The symplectic method of Theorem 6.1 now becomes

$$
{ \begin{array} { r c l } { { p _ { 0 } } } & { { = } } & { { \displaystyle - { \frac { \partial L _ { h } } { \partial x } } ( q _ { 0 } , q _ { 1 } ) } } \\ { { } } & { { = } } & { { \displaystyle - h \sum _ { i = 1 } ^ { s } b _ { i } { \dot { P } } _ { i } \Bigl ( I + h \sum _ { j = 1 } ^ { s } a _ { i j } { \frac { \partial { \dot { Q } } _ { j } } { \partial q _ { 0 } } } \Bigr ) - h \sum _ { j = 1 } ^ { s } b _ { j } P _ { j } { \frac { \partial { \dot { Q } } _ { j } } { \partial q _ { 0 } } } } } \\ { { } } & { { = } } & { { \displaystyle - h \sum _ { i = 1 } ^ { s } b _ { i } { \dot { P } } _ { i } + \lambda _ { \mathrm { { s } } } } } \end{array} }
$$

In the last equality we use (6.17)and $\begin{array} { r } { h \sum _ { j } b _ { j } \partial Q _ { j } / \partial q _ { 0 } = - I } \end{array}$ which follows from differentiating the constraint.In the same way we obtain

$$
p _ { 1 } = { \frac { \partial L _ { h } } { \partial y } } ( q _ { 0 } , q _ { 1 } ) = \lambda .
$$

Putting these formulas together,we see that $( p _ { 1 } , q _ { 1 } )$ result from applyingapartitionedRunge-Kuttamethod to theLagrange equations(1.4）writtenasadifferentialalgebraicsystem

$$
\dot { p } = \frac { \partial L } { \partial q } ( q , \dot { q } ) , p = \frac { \partial L } { \partial \dot { q } } ( q , \dot { q } ) .
$$

Thatis

$$
\begin{array} { r l r l } & { p _ { 1 } = p _ { 0 } + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \dot { P } _ { i } , } & & { q _ { 1 } = q _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } \dot { Q } _ { i } , } \\ & { P _ { i } = p _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } \widehat a _ { i j } \dot { P } _ { j } , } & & { Q _ { i } = q _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } \dot { Q } _ { j } , } \end{array}
$$

with $\widehat { a } _ { i j } = b _ { j } - b _ { j } a _ { j i } / b _ { i }$ sothat thesymplecticity condition (4.3) is fulfilled,and with $P _ { i } , Q _ { i } , \dot { P } _ { i } , \dot { Q } _ { i }$ related by(6.16).Since equations(6.16)are of the same form as (6.18),the proof of Theorem 1.3 shows that they are equivalent to

$$
\dot { P } _ { i } = - \frac { \partial H } { \partial q } ( P _ { i } , Q _ { i } ) , \dot { Q } _ { i } = \frac { \partial H } { \partial p } ( P _ { i } , Q _ { i } )
$$

with the Hamiltonian $H = p ^ { T } \dot { q } - L ( q , \dot { q } )$ of (1.6).We have thus proved the following,which is similarin spirit to aresult of Suris (1990).

Theorem6.4. The variational integrator with the discrete Lagrangian(6.15）is equivalentto the symplecticpartitionedRunge-Kuttamethod(6.19),(6.20) applied totheHamiltonian systemwith the Hamiltonian(1.6). □

In particular,as noted byMarsden&West(2oo1),choosingGaussianquadrature in(6.14） gives the Gauss collocation method applied to the Hamiltonian system, whileLobatto quadrature gives the Lobatto IIIA-IIIB pair.

# VI.6.4Noether's Theorem

enthalt SatzIalle in Mechaniku.s.w.bekannten Satzeübererste Integrale. （E.Noether 1918)

Wenow return to the subject of Chap.IV,i.e.,the existence of first integrals,but here in the context of Hamiltonian systems.E.Noether found the surprisingresult thatcontinuoussymmetries in theLagrangian lead to such first integrals.We givein thefollowingaversion of her“Satz I",specialized to our needs,witha particularly shortproof.

Theorem6.5 (Noether 1918).Considera systemwith Hamiltonian $H ( p , q )$ and Lagrangian $L ( q , \dot { q } )$ Suppose $\{ g _ { s } : s \in \mathbb { R } \}$ isaone-parameter group of transformations( $g _ { s } \circ g _ { r } = g _ { s + r }$ which leaves theLagrangian invariant:

$$
L ( g _ { s } ( q ) , g _ { s } ^ { \prime } ( q ) \dot { q } ) = L ( q , \dot { q } ) \quad f o r a l l s a n d a l l ( q , \dot { q } ) .
$$

Let $a ( q ) = ( d / d s ) | _ { s = 0 } g _ { s } ( q )$ bedefinedas thevectorfield with flow $g _ { s } ( q )$ .Then

$$
I ( p , q ) = p ^ { T } a ( q )
$$

isafrst integral ofthe Hamiltonian system.

Example6.6.Let $G$ beamatrix Lie group with Liealgebra g(seeSect.IV.6).Suppose $L ( Q q , Q \dot { q } ) = L ( q , \dot { q } )$ forall $Q \in G$ .Then $p ^ { T } A q$ isa firstintegral for every $A \in { \mathfrak { g } }$ .(Take $g _ { s } ( q ) = \exp ( s A ) q .$ ）Forexample, $G = S O ( n )$ yields conservation of angularmomentum.

Weprove Theorem6.5byusing thediscrete analogue,which readsas follows.

Theorem6.7.Suppose the one-parametergroup of transformations $\{ g _ { s } : s \in \mathbb { R } \}$ leaves thediscrete Lagrangian $L _ { h } ( q _ { 0 } , q _ { 1 } )$ invariant:

$$
L _ { h } ( g _ { s } ( q _ { 0 } ) , g _ { s } ( q _ { 1 } ) ) = L _ { h } ( q _ { 0 } , q _ { 1 } ) ~ f o r ~ a l l ~ s ~ a n d ~ a l l ~ ( q _ { 0 } , q _ { 1 } ) .
$$

Then(6.22)isafrstintegralofthemethod $( 6 . I I )$ i.e., $p _ { n + 1 } ^ { T } a ( q _ { n + 1 } ) = p _ { n } ^ { T } a ( q _ { n } )$

Proof.Differentiating(6.23)with respect to $s$ gives

$$
0 = \frac { d } { d s } \Big \vert _ { s = 0 } L _ { h } ( g _ { s } ( q _ { 0 } ) , g _ { s } ( q _ { 1 } ) ) = \frac { \partial L _ { h } } { \partial x } ( q _ { 0 } , q _ { 1 } ) a ( q _ { 0 } ) + \frac { \partial L _ { h } } { \partial y } ( q _ { 0 } , q _ { 1 } ) a ( q _ { 1 } ) .
$$

By (6.11) this becomes $0 = - p _ { 0 } ^ { I } a ( q _ { 0 } ) + p _ { 1 } ^ { I } a ( q _ { 1 } ) .$

Theorem 6.5 now follows by choosing $L _ { h } = S$ of (6.3)and noting (6.4)and

$$
\begin{array} { l } { S ( q ( t _ { 0 } ) , q ( t _ { 1 } ) ) \ = \ \displaystyle \int _ { t _ { 0 } } ^ { t _ { 1 } } L \big ( q ( t ) , \dot { q } ( t ) \big ) d t } \\ { \displaystyle \ = \ \int _ { t _ { 0 } } ^ { t _ { 1 } } L \Big ( g _ { s } ( q ( t ) ) , \frac { d } { d t } g _ { s } ( q ( t ) ) \Big ) d t = S \Big ( g _ { s } ( q ( t _ { 0 } ) ) , g _ { s } ( q ( t _ { 1 } ) ) } \end{array}
$$

Theorem 6.7 has the appearance of givinga rich source of frst integrals for symplectic methods.However,it mustbe noted that,unlike the case ofthe exact flow mapin theabove formula,theinvariance(6.21） of theLagrangian $L$ does not in generalimply theinvariance（6.23）of thediscreteLagrangian $L _ { h }$ of the numerical method.A noteworthy exception arises for linear transformations $g _ { s }$ asinExample6.6,forwhich Theorem6.7yields the conservation of quadratic first integrals $p ^ { T } A q$ ,suchas angularmomentum,by symplectic partitioned Runge-Kutta methods -apropertywealready know from Theorem IV.2.4.ForHamiltonian systemswith anassociatedLagrangian $\begin{array} { r } { L ( q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { T } M \dot { q } - U ( q ) } \end{array}$ allfirstintegralsoriginating fromNoether'sTheorem are quadratic(see Exercise 13).

# VI.7 Characterization of Symplectic Methods

Upto now in this chapter,we have presented sufficient conditions for the symplecticity of numerical integrators (usuallyin terms of certain coefficients).Here,we will prove necessary conditions for symplecticity,i.e.,answer the question as to which methodsare not symplectic.It will turn out that the suficient conditions of Sect.VI.4,underan irreducibility condition on the method,are also necessary.The main tool is the Taylor series expansion of the numerical flow $y _ { 0 } \mapsto \varPhi _ { h } ( y _ { 0 } )$ ,which weassume to beaB-series(ora P-series).

# VI7.1B-Series Methods Conserving Quadratic First Integrals

Thenumerical solution of a Runge-Kutta method (II.1.4) can be written asa B-series

$$
y _ { 1 } = B ( a , y _ { 0 } ) = y _ { 0 } + \sum _ { \tau \in T } { \frac { h ^ { | \tau | } } { \sigma ( \tau ) } } a ( \tau ) F ( \tau ) ( y _ { 0 } )
$$

with coefficients $a ( \tau )$ given by

$$
a ( \tau ) = \sum _ { i = 1 } ^ { s } b _ { i } \mathbf { g } _ { i } ( \tau ) \qquad \mathrm { f o r } \quad \tau \in T
$$

(see (III.1.16) and Sect.III.1.2).Our aim is to express the suffcient condition for the exact conservation of quadratic first integrals(which is the same as for symplecticity）in terms of the coefficients $a ( \tau )$ For thiswe multiply(4.2)by $\mathbf { g } _ { i } ( u ) \cdot \mathbf { g } _ { j } ( v )$ (where $u = [ u _ { 1 } , \dots , u _ { m } ]$ and $v = \left\lfloor v _ { 1 } , \ldots , v _ { l } \right\rfloor$ are treesin $T$ andwesum over all $\textit { i }$ and $j .$ Using（III.1.13）and the recursion（III.i.15) thisyields

$$
\sum _ { i = 1 } ^ { s } b _ { i } \mathbf { g } _ { i } ( u \circ v ) + \sum _ { j = 1 } ^ { s } b _ { j } \mathbf { g } _ { j } ( v \circ u ) = \Bigl ( \sum _ { i = 1 } ^ { s } b _ { i } \mathbf { g } _ { i } ( u ) \Bigr ) \Bigl ( \sum _ { j = 1 } ^ { s } b _ { j } \mathbf { g } _ { j } ( v ) \Bigr ) ,
$$

where we have used the Butcher product (see,e.g.,Butcher (1987),Sect.143)

$$
u \circ v = [ u _ { 1 } , _ { \ast } , . . . , u _ { m } , v ] , \qquad v \circ u = [ v _ { 1 } , _ { \ast } , . . . , v _ { l } , u ]
$$

(comparealso Definition II.3.7andFig.7.1 below).Because of(7.2),this implies

$$
a ( u \circ v ) + a ( v \circ u ) = a ( u ) \cdot a ( v ) \qquad { \mathrm { f o r } } \quad u , v \in T .
$$

Wenow forget that theB-series(7.1） has beenobtained froma Runge-Kutta method,and we ask the following question:is the condition(7.4） sufficient fora B-seriesmethod defined by(7.1） to conserve exactly quadratic first integrals (and to be symplectic)?The next theorem shows that thisis indeed true,and weshall see later that condition(7.4) isalso necessary(cf.Chartier,Faou&Murua 2005).

Theorem7.1. Considera $B$ -seriesmethod $\begin{array} { r c l } { \displaystyle \varPhi _ { h } ( y ) } & { = } & { { B ( a , y ) } } \end{array}$ andproblems $\dot { y } = f ( y )$ having $Q ( y ) = y ^ { T } C y$ (with symmetricmatrix $C$ )asfirst integral.

Ifthecoefficients $a ( \tau )$ satisfy(7.4),thenthemethodexactly conserves $Q ( y )$ and it issymplectic.

Proof.a) Under the assumptions of the theorem we shall prove in part (c) that

$$
B ( a , y ) ^ { T } C B ( a , y ) = y ^ { T } C y + \sum _ { u , v \in T } { \frac { h ^ { | u | + | v | } } { \sigma ( u ) \sigma ( v ) } } m ( u , v ) . F ( u ) ( y ) ^ { T } C F ( v ) ( y )
$$

with $m ( u , v ) = a ( u ) \cdot a ( v ) - a ( u \circ v ) - a ( v \circ u ) .$ Condition (7.4) is equivalent to $m ( u , v ) = 0$ and thus implies the exact conservation of $Q ( y ) = y ^ { T } C y .$

To prove symplecticity of the method it is suffcient to show that the diagram of Lemma 4.1 commutes for general B-series methods.This isseen by differentiating theelementary differentialsand by comparing them with those forthe augmented system (Exercise 8).Symplecticity of the method thus followsas in Sect.VI.4.1 formthefact that thesymplecticityrelationisaquadratic first integral of theaugmented system.

b)Since $Q ( y ) = y ^ { T } C y$ isa first integral of $\dot { y } = f ( y )$ ,we have $y ^ { T } C f ( y ) = 0$ forall $_ y$ Differentiating $m$ times this relation with respect to $y$ yields

$$
\sum _ { j = 1 } ^ { m } k _ { j } ^ { T } C f ^ { ( m - 1 ) } ( y ) \bigl ( k _  1 , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot , \cdot \cdot , \cdot , \cdot \cdot , \cdot \cdot , \cdot \cdot , \cdot \cdot , \cdot \cdot , \cdot \cdot , \cdot \cdot , \cdot \cdot \cdot , \cdot \cdot \cdot , \cdot \cdot \cdot , \cdot \cdot \cdot \cdot , \cdot \cdot \cdot \cdot \cdot , \cdot \cdot \cdot \cdot \cdot \cdot \cdot , \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot
$$

Putting $k _ { j } = F ( \tau _ { j } ) ( y )$ we obtain the formula

$$
{ } ^ { T } C F ( [ \tau _ { 1 } , \dots , \tau _ { m } ] ) ( y ) = - \sum _ { j = 1 } ^ { m } F ( \tau _ { j } ) ( y ) ^ { T } C F ( [ \tau _ { 1 } , \dots , \tau _ { j - 1 } , \bar { \tau } _ { j + 1 } , \dots , \bar { \tau } _ { m } ] ) ( y ) ,
$$

which can alsobe written in the form

$$
y ^ { T } C \frac { F ( \tau ) ( y ) } { \sigma ( \tau ) } = - \sum _ { u , v \in T , v \circ u = \tau } \frac { F ( u ) ( y ) ^ { T } } { \sigma ( u ) } C \frac { F ( v ) ( y ) } { \sigma ( v ) } .
$$

c)With(7.1) the expression $y _ { 1 } ^ { \scriptscriptstyle T } C y _ { 1 }$ becomes

$$
\begin{array} { r c l } { { \displaystyle { \cal B } ( a , y ) ^ { T } C B ( a , y ) } } & { { = } } & { { y ^ { T } C y + 2 y ^ { T } C \displaystyle { \sum _ { \tau \in { \cal T } } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } } a ( \tau ) { \cal F } ( \tau ) ( y ) } } \\ { { } } & { { + } } & { { \displaystyle { \sum _ { u , v \in { \cal T } } \frac { h ^ { | u | + | v | } } { \sigma ( u ) \sigma ( v ) } a ( u ) a ( v ) { \cal F } ( u ) ( y ) ^ { T } C { \cal F } ( v ) ( y ) . } } } \end{array}
$$

Since $C$ is symmetric,formula(7.6) remains true if we sum over trees $u , v$ such that $u \circ v = \tau$ Inserting both formulasinto the sum over $\tau$ leads directly to (7.5). □

Extensionto P-Series.Allthe previousresults can be extended to partitioned methods.To find the correct conditions on the coefficients of theP-series,weuse the fact that the numerical solution of apartitioned Runge-Kutta method(II.2.2)isaP-series

$$
\begin{array} { r } { \mathbf { \rho } _ { g _ { 1 } } ^ { p _ { 1 } } \Big ) = { \binom { P _ { p } \left( \bar { a } , ( p _ { 0 } , q _ { 0 } ) \right) } { P _ { q } \left( a , ( p _ { 0 } , q _ { 0 } ) \right) } } = { \binom { p _ { 0 } } { q _ { 0 } } } + { \binom { \sum _ { u \in T P _ { p } } \frac { \hbar ^ { | u | } } { \sigma ( u ) } a \left( u \right) F \left( u \right) \left( p _ { 0 } , q _ { 0 } \right) } { \sum _ { v \in T P _ { q } } \frac { \hbar ^ { | v | } } { \sigma ( v ) } a \left( v \right) F \left( v \right) \left( p _ { 0 } , q _ { 0 } \right) } } } \end{array}
$$

with coefficients $a ( \tau )$ given by

$$
a ( \tau ) = \left\{ \begin{array} { l l } { \sum _ { i = 1 } ^ { s } b _ { i } \phi _ { i } ( \tau ) } & { \quad \mathrm { f o r } \quad \tau \in T P _ { p } } \\ { \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } \phi _ { i } ( \tau ) } & { \quad \mathrm { f o r } \quad \tau \in T P _ { q } } \end{array} \right.
$$

(seeTheorem II.2.4).Weassume here that the elementary differentials $F ( \tau ) ( p , q )$ originate fromapartitioned sytem

$$
\dot { p } = f _ { 1 } ( p , q ) , \quad \dot { q } = f _ { 2 } ( p , q ) ,
$$

such asthe Hamiltonian system(1.7).This time we multiply(4.3) by $\phi _ { i } ( u ) \cdot \phi _ { j } ( v )$ (where $u = [ u _ { 1 } , \ldots , u _ { m } ] _ { p } \in \mathit { T P } _ { p }$ and $v = [ v _ { 1 } , \dots , v _ { l } ] _ { q } \in \mathit { T P } _ { q } ,$ andwe sum over all $i$ and $j$ Using the recursion(III.2.7) this yields

$$
\sum _ { i = 1 } ^ { s } b _ { i } \phi _ { i } ( u \circ v ) + \sum _ { j = 1 } ^ { s } \widehat { b } _ { j } \phi _ { j } ( v \circ u ) = \Big ( \sum _ { i = 1 } ^ { s } b _ { i } \phi _ { i } ( u ) \Big ) \Big ( \sum _ { j = 1 } ^ { s } \widehat { b } _ { j } \phi _ { j } ( v ) \Big ) ,
$$

where $\boldsymbol { u } \circ \boldsymbol { v } = [ u _ { 1 } , \ldots , u _ { m } , v ] _ { p }$ and $v \circ u = [ v _ { 1 } , \ldots , v _ { l } , u ] _ { q } .$ Because of（7.8）,this implies therelation

$$
a ( u \circ v ) + a ( v \circ u ) = a ( u ) \cdot a ( v ) \qquad { \mathrm { f o r } } \quad u \in T P _ { p } , \ v \in T P _ { q } .
$$

Since $\phi _ { i } ( \tau )$ is independent of the colour of therootof $\tau$ ,condition(4.4)implies

$a ( \tau )$ is independent of the colour of the root of T.

Theorem7.2.Considera $P$ -seriesmethod $( p _ { 1 } , q _ { 1 } ) = \varPhi _ { h } ( p _ { 0 } , q _ { 0 } )$ given by (7.7), andaproblem(7.9) having $Q ( p , q ) = p ^ { T } E$ q as first integral.

i) If the coefficients $a ( \tau )$ satisfy(7.11)and(7.12),themethodexactlyconserves $Q ( p , q )$ anditissymplectic for general Hamiltonian systems(1.7).

ii) If the coefficients $a ( \tau )$ satisfy only (7.11),themethod exactly conserves $Q ( p , q )$ forproblemsofthe form $\dot { p } = f _ { 1 } ( q )$ ， $\dot { q } = f _ { 2 } ( p )$ ,anditissymplecticfor separable Hamiltonian systems where $H ( p , q ) = T ( p ) + U ( q )$

Proof.Thisis very similar to that of Theorem7.1.If $Q ( p , q ) = p ^ { T } E q$ isa first integral of(7.9),we have $f _ { 1 } ( p , q ) ^ { \cal I } E q + p ^ { \cal I } E f _ { 2 } ( p , q ) = 0$ forall $p$ and q.Differentiating $m$ timeswith respect to $p$ and $n$ timeswith respect to $q$ yields

$$
\begin{array} { l } { { \displaystyle 0 ~ = ~ D _ { p } ^ { m } D _ { q } ^ { n } f _ { 1 } ( p , q ) \big ( k _ { 1 } , \dots , k _ { m } , \ell _ { 1 } , \dots , \ell _ { n } \big ) ^ { T } E q } } \\ { { ~ + ~ p ^ { T } E D _ { p } ^ { m } D _ { q } ^ { n } f _ { 2 } ( p , q ) \big ( k _ { 1 } , \dots , k _ { m } , \ell _ { 1 } , \dots , \ell _ { n } \big ) } } \\ { { ~ + ~ \displaystyle \sum _ { j = 1 } ^ { n } D _ { p } ^ { m } D _ { q } ^ { n - 1 } f _ { 1 } ( p , q ) \big ( k _ { 1 } , \dots , k _ { m } , \ell _ { 1 } , \dots , \ell _ { j - 1 } , \ell _ { j + 1 } , \dots , \ell _ { n } \big ) ^ { T } E \ell _ { j } } } \\ { { ~ + ~ \displaystyle \sum _ { i = 1 } ^ { m } k _ { i } ^ { T } E D _ { p } ^ { m - 1 } D _ { q } ^ { n } f _ { 2 } ( p , q ) \big ( k _ { 1 } , \dots , k _ { i - 1 } , k _ { i + 1 } , \dots , k _ { m } , \ell _ { 1 } , \dots , \ell _ { n } \big ) . } } \end{array}
$$

Putting $k _ { i } = F ( u _ { i } ) ( p , q )$ with $u _ { i } \in \textit { T } P _ { p }$ , $\ell _ { j } = F ( v _ { j } ) ( p , q )$ with $v _ { j } \in T P _ { q } , \tau _ { p } =$ $\vert u _ { 1 } , \dotsc , u _ { m } , v _ { 1 } , \dotsc , v _ { n } \vert _ { p }$ and $\tau _ { q } = [ u _ { 1 } , \dots , u _ { m } , v _ { 1 } , \dots , v _ { n } ] q ,$ we obtain as in part (b)of theproof of Theorem 7.1that

$$
\begin{array} { r l } & { \displaystyle \frac { F ( \tau _ { p } ) ( p , q ) ^ { T } } { \sigma ( \tau _ { p } ) } E q + p ^ { T } E \frac { F ( \tau _ { q } ) ( p , q ) } { \sigma ( \tau _ { q } ) } } \\ & { = \displaystyle \sum _ { u \circ v = \tau _ { p } } \frac { F ( u ) ( p , q ) ^ { T } } { \sigma ( u ) } E \frac { F ( v ) ( p , q ) } { \sigma ( v ) } + \displaystyle \sum _ { v \circ u = \tau _ { q } } \frac { F ( u ) ( p , q ) ^ { T } } { \sigma ( u ) } E \frac { F ( v ) ( p , q ) } { \sigma ( v ) } , } \end{array}
$$

where the sums are over $u \in \mathcal { I } \mathcal { P } _ { p }$ and $v \in T P _ { q }$

With(7.7) the expression $p _ { 1 } ^ { T } E q _ { 1 }$ becomes

$$
\begin{array} { r l } & { P _ { p } ( a , ( p , q ) ) ^ { T } E P _ { q } ( a , ( p , q ) ) \ : = \ : p ^ { T } E q } \\ & { + \displaystyle \sum _ { u \in T P _ { p } } \frac { h ^ { | u | } } { \sigma ( u ) } a ( u ) F ( u ) ( p , q ) ^ { T } E q + \displaystyle p ^ { T } E \sum _ { v \in T P _ { q } } \frac { h ^ { | v | } } { \sigma ( v ) } a ( v ) F ( v ) ( p , q ) } \\ & { + \displaystyle \sum _ { u \in T P _ { p } , v \in T P _ { q } } \frac { h ^ { | u | + | v | } } { \sigma ( u ) \sigma ( v ) } a ( u ) a ( v ) F ( u ) ( p , q ) ^ { T } E F ( v ) ( p , q ) . } \end{array}
$$

Condition(7.12)implies that $a ( \tau _ { p } ) = a ( \tau _ { q } )$ for the trees in(7.14).Since also $| \tau _ { p } | =$ $| \tau _ { q } |$ and $\sigma ( \tau _ { p } ) = \sigma ( \tau _ { q } )$ ,two corresponding terms inthe sums of the second line in(7.15) can be jointly replaced by the use of(7.14).Asinpart(c)of the proofof Theorem7.1 this together with(7.11） then yields

$$
\begin{array} { r } { P _ { p } ( { a } , ( p , q ) ) ^ { T } E P _ { q } ( { a } , ( p , q ) ) = p ^ { T } E q , } \end{array}
$$

which proves the conservation of quadratic first integrals $p ^ { T } E q$ Symplecticity followsasbefore,becausethediagram ofLemma4.1alsocommutes for generalPseriesmethods.

For the proof of statement (ii) we notice that $f _ { 1 } ( q ) ^ { \scriptscriptstyle T } E q + p ^ { \scriptscriptstyle T } E f _ { 2 } ( p ) = 0$ implies that $f _ { 1 } ( q ) ^ { T } E q = 0$ and $p ^ { T } E f _ { 2 } ( p ) = 0$ vanish separately.Instead of（7.14) we thus have two identities:the term $F ( \tau _ { p } ) ( p , q ) ^ { T } E q / \sigma ( \tau _ { p } )$ becomes equal to the first sum in(7.14）,and $p ^ { T } E F ( \tau _ { q } ) ( p , q ) / \sigma ( \tau _ { q } )$ to the second sum.Consequently, the previous argumentation can be applied without the condition $a ( \tau _ { p } ) = a ( \tau _ { q } )$ □

Second Order Differential Equations.We next consider partitioned systems of theparticular form

$$
\dot { p } = f _ { 1 } ( q ) , \qquad \dot { q } = C p + c ,
$$

where $C$ isamatrix and $c$ avector.Since problems of this type are second orderdifferential equations $\ddot { q } = C f _ { 1 } ( q )$ ,partitioned Runge-Kutta methods become equivalent to Nystrom methods(see Sects.II.2.3andIV.2.3).

Animportant special case are Hamiltonian systems

$$
\dot { p } = - \nabla U ( q ) , \qquad \dot { q } = C p + c
$$

(or,equivalently, $\ddot { q } = - C \nabla U ( q ) ) .$ They correspond to Hamiltonian functions

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } C p + c ^ { T } p + U ( q ) ,
$$

where the kinetic energy is at most quadratic in $p$ (here, $C$ is usually symmetric).

InaP-seriesrepresentation ofthenumerical solution,manyelementarydifferentialsvanish identically.Only those trees have to beconsidered,whose neighbouring verticeshavedifferent colour(theproblemis separable)andwhosewhitevertices have at most one $\mathsf { s o n } ^ { 6 }$ (second component is linear).We denote this set of trees by

$$
T N _ { p } = \Big \{ \tau \in \tau P _ { p } \Big | \begin{array} { c } { \mathrm { n e i g h b o u r i n g ~ v e r t i c e s ~ o f ~ } \tau \mathrm { ~ h a v e ~ d i f f e r e n t ~ c o l o u r } } \\ { \mathrm { ~ w h i t e ~ v e r t i c e s ~ o f ~ } \tau \mathrm { ~ h a v e ~ a t ~ m o s t ~ o n e ~ s o n } } \end{array} \Big \} ,
$$

and we let $\because N _ { q }$ be the corresponding subset of ${ \cal T } { \cal P } _ { q }$

The same procedure as for partitioned methods permits us to write the symplecticitycondition of Theorem 4.8 in terms ofthecoefficients $a ( \tau )$ of the P-series. Assuming $a ( \circ ) = a ( \circ ) = 1$ thetwoconditions of（4.5）lead to

$$
a ( \circ \circ u ) + a ( u \circ \circ ) = a ( u ) a ( \circ ) \qquad { \mathrm { f o r ~ } } u \in T N _ { p }
$$

$$
\begin{array} { r l r } & { a ( \circ \circ v ) - a ( u \circ \circ v ) = a ( \circ \circ u ) a ( v ) - a ( v \circ \circ u ) } & { \mathrm { f o r ~ } u , v \in T \Lambda } \\ & { \circ \ : \mathrm { w e ~ u s e ~ t h e ~ a b b r e v i a t i n g ~ n o t a t i o n ~ } } & { \big \langle \overset { v } { \underset { \mathcal { Y } } { \mathcal { Y } } } \big \rangle } \\ & { u \circ \circ v = u \circ ( \circ \circ v ) = [ u _ { 1 } , \ldots , u _ { m } , [ v ] _ { q } ] _ { p } } & { \big ( \overset { n } { \underset { \mathcal { Y } } { \mathcal { Y } } } \big ) } \end{array}
$$

if $u = [ u _ { 1 } , \ldots , u _ { m } ] _ { p } .$ Notice that for $u , v \in T N _ { p }$ ,thetrees $u \circ \circ$ , $u \circ \circ v$ and $v \circ \circ u$ arein $T N _ { p }$ ,and $\circ \circ u$ isin $T N _ { q }$

Theorem7.3. Considera $P$ -seriesmethod(7.7) fordifferentialequations(7.16) having $Q ( p , q ) = p ^ { T } E q$ asfirst integral.

If the coefficients $a ( \tau )$ satisfy(7.20)and(7.21),the method exactly conserves $Q ( p , q )$ andit issymplecticforHamiltoniansystems with $H ( p , q )$ oftheform(7.18).

Proof.Since the elementary differentials $F ( \tau ) ( p , q )$ vanish identically for $\tau \not \in { }$ $T N _ { p } \cup T N _ { q }$ ,wecanarbitrarily define $a ( \tau )$ for trees outside $T N _ { p } \cup T N _ { q }$ withoutchanging the method (throughout this proofwe implicitly assume that for the considered trees neighbouringvertices havedifferent colour).We shall do this in suchaway that（7.11） holds.

Consider first the tree $u \circ \circ v$ Thereis exactly one vertex between the roots of $u$ and $\boldsymbol { v }$ Making thisvertex to the root gives the tree $[ u , v ] _ { q }$ which is not in $T N _ { q }$ We define for $u , v \in T N _ { p }$

$$
a ( [ u , v ] _ { q } ) : = a ( u ) a ( \circ \circ v ) - a ( u \circ \circ v ) .
$$

Condition(7.21） shows that $a ( | u , v | _ { q } )$ is independent of permuting $u$ and $\boldsymbol { v }$ andis thuswell-defined.For trees that are neither in $T N _ { p } \cup T N _ { q }$ nor of the form $[ u , v ] _ { q }$ with $u , v \in T N _ { p }$ welet $a ( \tau ) = 0$ This extension of $a ( \tau )$ implies that condition （7.11)holds forall trees,andpart(ii）ofTheorem7.2yieldsthe statement.Notice that for problems ${ \dot { p } } = f _ { 1 } ( q )$ ， ${ \dot { q } } = f _ { 2 } ( p )$ only trees,for which neighbouring vertices havedifferent colour,are relevant. □

# VI.7.2 Characterization of Symplectic P-Series (and B-Series)

Acharacterization of symplecticB-series was first obtained by Calvo& Sanz-Serna (1994).We also consider P-serieswith various important special situations.

Theorem7.4.Considera $P$ -seriesmethod(7.7)appliedtoa generalpartitioned differential equation(7.9).Equivalent are:

1）thecoefficients $a ( \tau )$ satisfy(7.11） and(7.12),   
2）quadraticfirst integralsoftheform $Q ( p , q ) = p ^ { T } E q$ areexactly conserved,   
3)themethod is symplecticfor general Hamiltonian systems(1.7).

Proof.Theimplication(1)=(2) follows frompart(i)ofTheorem7.2,(2)=(3)isa consequence ofthe fact that the symplecticitycondition isaquadratic firstintegral of thevariational equation (see the proof of Theorem 7.2).The remaining implication $( 3 ) \Rightarrow ( 1 )$ will be proved in the following two steps.

a)We fix two trees $u \in \textit { T } { \cal P } _ { p }$ and $v \in \mathsf { \Gamma } T { \cal P } _ { q }$ ,andwe constructa(polynomial) Hamiltonian such that the transformation(7.7） satisfies

$$
\Big ( \frac { \partial ( p _ { 1 } , q _ { 1 } ) } { \partial p _ { 0 } ^ { 1 } } \Big ) ^ { T } J \Big ( \frac { \partial ( p _ { 1 } , q _ { 1 } ) } { \partial q _ { 0 } ^ { 2 } } \Big ) = C \Big ( a ( u \circ v ) + a ( v \circ u ) - a ( u ) \cdot a ( v ) \Big )
$$

with $C \neq 0$ (here, $p _ { 0 } ^ { 1 }$ denotes the first component of $p _ { 0 }$ ,and $q _ { 0 } ^ { 2 }$ the second component of $q _ { 0 }$ ).Thesymplecticity of(7.7) implies that the expressionin(7.23) vanishes, so that condition(7.11） has to be satisfied.

Forgiven $u \in T _ { \mathfrak { p } }$ and $v \in T { \cal P } _ { q }$ wedefine the Hamiltonian as follows:to the branches of $u \circ v$ weattach the numbers $3 , \ldots , | u | + | v | + 1$ such that the branch between the roots of ${ \boldsymbol u }$ and $v$ islabelledby3.Then,theHamiltonianisa sum of asmany termsasvertices inthe tree.The summand correspondingtoavertex isa product containing the factor $p ^ { j }$ (resp. $q ^ { j }$ ）ifanupwardleavingbranch‘ $j ^ { \prime \prime }$ isdirectly connectedwithablack(resp.white)vertex,and the factor $q ^ { i }$ (resp. $p ^ { i }$ ）ifthevertex itself is black(resp.white)and the downward leavingbranch has label“i.Finally, the factors $q ^ { 2 }$ and $p ^ { 1 }$ areincluded in the terms corresponding to the roots of $u$ and $\upsilon$ ,respectively.For the exampleofFig.7.1we have

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0004_pages_0211-0280/auto/images/68b98f3c2596387b294cfc41a4949cd296aa57774ddf5f06f2f3bf8ab951c5c0.jpg)  
Fig.7.1.Illustration of the Hamiltonian(7.24)

$$
H ( p , q ) = q ^ { 2 } q ^ { 3 } q ^ { 4 } p ^ { 5 } + p ^ { 1 } p ^ { 3 } p ^ { 7 } p ^ { 8 } + p ^ { 4 } p ^ { 6 } \pm q ^ { 5 } + q ^ { 6 } + q ^ { 7 } + q ^ { 8 } .
$$

Thecomponents $F ^ { 2 } ( \tau ) ( p , q )$ of theelementary differentials corresponding to theHamiltonian system(with the Hamiltonianconstructed above) satisfy

$$
\begin{array} { r c l } { { F ^ { 2 } ( u \circ v ) ( p , q ) } } & { { = } } & { { ( - 1 ) ^ { \delta ( u \circ v ) } \sigma ( u \circ v ) \cdot p ^ { 1 } , } } \\ { { } } & { { } } & { { F ^ { 1 } ( v \circ u ) ( p , q ) } } & { { = } } & { { ( - 1 ) ^ { \delta ( v \circ u ) } \sigma ( v \circ u ) \cdot q ^ { 2 } , } } \\ { { } } & { { } } & { { F ^ { 3 } ( u ) ( p , q ) } } & { { = } } & { { ( - 1 ) ^ { \delta ( u ) } \sigma ( u ) \cdot q ^ { 2 } } } \\ { { } } & { { } } & { { F ^ { 3 } ( v ) ( p , q ) } } & { { = } } & { { ( - 1 ) ^ { \delta ( v ) } \sigma ( v ) \cdot p ^ { 1 } , } } \end{array}
$$

and forall other trees $\tau \in \mathit { T P }$ and components $i$ wehave

$$
\frac { \partial { \cal F } ^ { i } ( \tau ) } { \partial p ^ { 1 } } ( 0 , 0 ) = \frac { \partial { \cal F } ^ { i } ( \tau ) } { \partial q ^ { 2 } } ( 0 , 0 ) = 0 .
$$

I ${ \mathfrak { n } } ( 7 . 2 5 ) , \delta ( \tau )$ counts the number of black vertices of $\tau$ ,andthe symmetrycoefficient $\sigma ( \tau )$ isthat of(III.2.3).For example, $\sigma ( u ) = 1$ and $\sigma ( v ) = 2$ for thetrees of Fig.7.1.Theverificationof(7.25)is straightforward.Thecoefficient $( - 1 ) ^ { \delta ( \tau ) }$ isdue to the minus sign in the first part of theHamiltonian system(1.7),and the symmetry coefficient $\sigma ( \tau )$ appearsin exactly the samewayas inthemultidimensional Taylor formula.Due to the zero initial values,no elementary differential other than those of(7.25） give rise to non-vanishing expressions in(7.23).Consider for example the second component of $F ( \tau ) ( p , q )$ foratree $\tau \in \textit { T P } _ { p }$ Sincewe are concerned with the Hamiltonian system(1.7),this expression starts with a derivative of $H _ { q ^ { 2 } }$ ， Therefore,itcontributes to（7.23）at $p _ { 0 } = q _ { 0 } = 0$ only if it contains the factor $H _ { q ^ { 2 } q ^ { 3 } q ^ { 4 } p ^ { 5 } }$ (forthe example ofFig.7.1).This in turn implies thepresence of factors $H _ { p ^ { 3 } . . . } , H _ { p ^ { 4 } . . . }$ and $H _ { q ^ { 5 } \cdots } .$ Continuing this line ofreasoning,we find that $F ^ { 2 } ( \tau ) ( p , q )$ contributes to(7.23）at $p _ { 0 } = q _ { 0 } = 0$ onlyif $\tau = u \circ v$ With similar argumentswe seethat only theelementarydifferentials of(7.25)have to be considered.Wenow insert(7.25) into (7.7),and we compute its derivatives with respect to $p ^ { 1 }$ and $q ^ { 2 }$ 、 This then yields（7.23）with $C = ( - 1 ) ^ { \delta ( u ) + \delta ( v ) } h ^ { | u | + | v | }$ ,and completes theproof concerning condition（7.11).

b)Thenecessity of condition(7.12) is seen similarly.We fixa tree $\tau \in \textit { T P } _ { p }$ andwe let $\overline { { \tau } } \in T P _ { q }$ be the tree obtained from $\tau$ by changing the colour of the root. Wethen attach the numbers $3 , \ldots , | \tau | + 1$ to the branches of $\tau$ andwe definea Hamiltonianasabove but,different fromadding the factors $q ^ { 2 }$ and $p ^ { 1 }$ ,weinclude thefactor $p ^ { 1 } q ^ { 2 }$ to the term corresponding to the root.For the tre $\tau = u$ ofFig.7.1 thisyields

$$
H ( p , q ) = p ^ { 1 } q ^ { 2 } q ^ { 3 } p ^ { 4 } + p ^ { 3 } p ^ { 5 } + q ^ { 4 } + q ^ { 5 } .
$$

With this Hamiltonian we get

$$
\begin{array} { r c l } { { F ^ { 2 } ( \tau ) ( p , q ) } } & { { = } } & { { ( - 1 ) ^ { \delta ( \tau ) } \sigma ( \tau ) \cdot p ^ { 1 } , } } \\ { { F ^ { 1 } ( \overline { { { \tau } } } ) ( p , q ) } } & { { = } } & { { ( - 1 ) ^ { \delta ( \tau ) } \sigma ( \tau ) \cdot q ^ { 2 } , } } \end{array}
$$

andtheseare the only elementary differentials contributing tothe left-hand expression of(7.23).We thus get

$$
\Bigl ( { \frac { \partial ( p _ { 1 } , q _ { 1 } ) } { \partial p _ { 0 } ^ { 1 } } } \Bigr ) ^ { T } J \Bigl ( { \frac { \partial ( p _ { 1 } , q _ { 1 } ) } { \partial q _ { 0 } ^ { 2 } } } \Bigr ) = ( - 1 ) ^ { \delta ( \tau ) } h ^ { \left[ \tau \right] } \Bigl ( a ( \tau ) - a ( \tau ) \Bigr ) ,
$$

which completes the proof of Theorem 7.4.

Theorem7.5.Considera $P$ -seriesmethod(7.7)appliedtoaseparablepartitioned differential equation ${ \dot { p } } = f _ { 1 } ( q )$ , ${ \dot { q } } = f _ { 2 } ( p )$ Equivalent are:

1）the coefficients $a ( \tau )$ satisfy(7.11）,   
2）quadraticfirst integrals of theform $Q ( p , q ) = p ^ { T } E _ { 4 }$ areexactly conserved,   
3)themethodissymplecticforseparable Hamiltonians $H ( p , q ) = T ( p ) + U ( q )$

ProofThe implications(1)=(2)=(3） followasbefore from part(ii) of Theorem7.2.Theremaining implication (3)→(1） is a consequence of the fact that the Hamiltonianconstructed in part(a)of theproof ofTheorem 7.4is separable,when $u$ and $v$ haveno neighbouring vertices of the same colour. □

Theorem7.6.Considera $B$ -seriesmethod(7.1)for $\dot { y } = f ( y )$ Equivalent are: 1）the coefficients $a ( \tau )$ satisfy(7.4), 2）quadraticfirst integralsof the form $Q ( y ) = y ^ { T } C y$ areexactly conserved, 3)themethodis symplecticforgeneral Hamiltonian systems $\dot { y } = J ^ { - 1 } \nabla H ( y )$

Proof.Theimplications(1)⇒(2)=(3） follow from Theorem 7.1.Theremaining implication(3)=(1)followsfrom Theorem7.4,becauseaB-serieswithcoeffcients $a ( \tau ) , \tau \in T$ ,applied toapartitioned differential equation,canalwaysbeinterpreted asaP-series(Definition II.2.1),where $a ( \tau ) : = a ( \varphi ( \tau ) )$ for $\tau \in \mathit { \Delta } I P$ and $\varphi : T P $ $T$ isthe mapping that forgets the colouring of the vertices.This follows from the factthat

$$
\begin{array} { r } { \boldsymbol { \alpha } ( \tau ) \boldsymbol { F } ( \tau ) ( \boldsymbol { y } ) = \left( \begin{array} { l } { \sum _ { u \in T P _ { p } , \varphi ( u ) = \tau } \boldsymbol { \alpha } ( u ) \boldsymbol { F } ( u ) ( p , q ) } \\ { \sum _ { v \in T P _ { q } , \varphi ( v ) = \tau } \boldsymbol { \alpha } ( v ) \boldsymbol { F } ( v ) ( p , q ) } \end{array} \right) } \end{array}
$$

for $\tau \in { \cal I }$ ,because $\alpha ( u ) \cdot \sigma ( u ) = \alpha ( v ) \cdot \sigma ( v ) = { \bf e } ( \tau ) \cdot | \tau | ! .$ Here, $y = ( p , q )$ ,the elementarydifferentials $F ( \tau ) ( y )$ are those of Definition II.1.2,whereas $F ( u ) ( p , q )$ and $F ( v ) ( p , q )$ are those of Table III.2.1. □

Theorem7.7.Consider a $P$ -seriesmethod(7.7)appliedtothespecialpartitioned system(7.16).Equivalent are:

1）the coefficients $a ( T )$ satisfy (7.20） and(7.21),   
2）quadratic first integrals of the form $Q ( p , q ) = p ^ { T } E q$ areexactly conserved,   
3）themethodis symplecticfor Hamiltonian systems of theform(7.17).

Proof.The implications(1)=(2)=(3) follow from Theorem 7.3.Theremaining implication (3)=(1) can be seenas follows.

Condition (7.2O) isaconsequence of the the proof of Theorem 7.4,because for $u \in T N _ { p }$ and $v = \circ$ theHamiltonian constructed there is of the form(7.18).

Toprovecondition (7.21）we have to modify slightly thedefinition of $H ( p , q )$ . Wetake $u , v \in \textit { T N } _ { p }$ and define the polynomial Hamiltonian as follows:to the branches of $u \circ \circ v$ we attach the numbers $3 , \ldots , | u | + | v | + 2 .$ The Hamiltonian is thenasum of asmany terms asvertices in the tree.The summandsare defined as in theproof of Theorem7.4with the only exception that to the termscorresponding to the rootsof $u$ and $v$ weinclude the factors $q ^ { 2 }$ and $q ^ { 1 }$ ,respectively,insteadof $q ^ { 2 }$ and $p ^ { 1 } .$ This givesa Hamiltonian of theform（7.18),for which the expression

$$
\Big ( \frac { \partial ( p _ { 1 } , q _ { 1 } ) } { \partial q _ { 0 } ^ { 1 } } \Big ) ^ { T } J \Big ( \frac { \partial ( p _ { 1 } , q _ { 1 } ) } { \partial q _ { 0 } ^ { 2 } } \Big )
$$

becomes equal to

$$
a ( u ) a ( \circ \circ v ) - a ( u \circ \circ v ) - a ( \circ \circ u ) a ( v ) + a ( v \circ \circ u )
$$

uptoanonzero constant.By symplecticity,(7.26)is zero so that also(7.27) has to vanish.This proves thevalidity ofcondition(7.21）. □

# VI.7.3Irreducible Runge-Kutta Methods

Weare now able to study towhatextent theconditions of Theorem 4.3and Theorem4.6are also necessary for symplecticity.Consider firstthe2-stage method

$$
{ \frac { 1 / 2 } { 1 / 2 } } \left| { \begin{array} { c c } { \alpha } & { 1 / 2 - \bar { \alpha } } \\ { \beta } & { 1 / 2 - \beta } \\ { 1 / 2 } & { 1 / 2 } \end{array} } \right. .
$$

The solution of the corresponding Runge-Kutta system (II.1.4） is given by $k _ { 1 } =$ $k _ { 2 } = k$ ,where $k = f ( y _ { 0 } + k / 2 )$ ,and hence $y _ { 1 } = y _ { 0 } + h k$ Whateverthevalues of $\alpha$ and $\beta$ are,the numerical solution of the Runge-Kutta method isidentical to that of theimplicit midpoint rule,so that it defines asymplectic transformation.However, the condition (4.2） is only satisfied for $\alpha = \beta = 1 / 4$ .

Definition 7.8. Two stages $i$ and $j$ ofaRunge-Kutta method(II.1.4) are said to be equivalent foraclass $( \mathcal { P } )$ of initial value problems,iffor everyproblem in $( { \mathcal { P } } )$ and forevery sufficiently small step sizewe have $k _ { i } = k _ { j }$ （ $k _ { i } = k _ { j }$ and $\ell _ { i } = \ell _ { j }$ for partitionedRunge-Kutta methods(II.2.2)).

Themethod iscalled irreduciblefor $( { \mathcal { P } } )$ if it does not have equivalent stages. Itiscalled ireducibleifitisirreducibleforall sufficiently smoothinitial value problems.

Foramore amenablecharacterization of irreducible Runge-Kutta methods,we introduce an ordering on $T$ (and on $T P$ )，andwe consider the following $s \times \infty$ matrices

$\varPhi _ { \mathrm { R K } } = \bigl ( \phi ( \tau ) ; \tau \in T \bigr )$ with entries $\phi _ { i } ( \tau ) = \mathbf { g } _ { i } ( \tau )$ given by (II.1.13),7   
$\begin{array} { r } { \Phi _ { \mathrm { P R K } } = ( \phi ( \tau ) ; \tau \in T P _ { p } ) = ( \phi ( \tau ) ; \tau \in T P _ { q } ) } \end{array}$ with entries $\phi _ { i } ( \tau )$ given by (III.2.7); observe that $\phi _ { i } ( \tau )$ does not depend on the colour of the root,   
$\begin{array} { r } { \begin{array} { r } { \Phi _ { \mathrm { P R K } } ^ { * } = ( \phi ( \tau ) ; \tau \in T P _ { p } ^ { * } ) = ( \phi ( \tau ) ; \tau \in T P _ { q } ^ { * } ) } \end{array} } \end{array}$ where $T P _ { p } ^ { * }$ (resp. $T P _ { q } ^ { * }$ istheset of trees in $T { \cal P } _ { p }$ (resp. $T P _ { q }$ )whose neighbouring vertices have different colours.

Lemma7.9 (Hairer1994).ARunge-Kuttamethodis irreducibleifandonlyifthe matrix $\boldsymbol { \varPhi } _ { \mathrm { R K } }$ has full rank s.

Apartitioned Runge-Kuttamethodis irreducibleifandonlyifthematrixRK hasfull rank s.

Apartitioned Runge-Kuttamethodisirreduciblefor separableproblems $\dot { p } =$ $f _ { 1 } ( q )$ , ${ \dot { q } } = f _ { 2 } ( p )$ ifand onlyifthematrix $\boldsymbol { \varPhi } _ { \mathrm { P R K } } ^ { * }$ has full rank s.

Proof.If thestages $i$ and $j$ are equivalent,it follows from the expansion

$$
k _ { i } = \sum _ { \tau \in T } \frac { h ^ { | \tau | } } { \sigma ( \tau ) } \phi _ { i } ( \tau ) F ( \tau ) ( y _ { 0 } )
$$

(seetheproof of Theorem III.1.4）and from the independency of the elementary differentials（Exercise II.3）that $\phi _ { i } ( \tau ) = \phi _ { j } ( \tau )$ forall $\tau \in T$ Hence,therows $i$ and $j$ of the matrix $\varPhi _ { \mathrm { R K } }$ areidentical.The analogous statement for partitioned Runge-Kutta methodsfollows from TheoremII.2.4and Exercise III.6.Thisproves thesufficiency of the“fullrank”condition.

We prove its necessityonly for partitioned Runge-Kuta methodsapplied to sep  
arableproblems(the other situationscan be treated similarly).For separable prob-$T P _ { p } ^ { * } \cup T P _ { q } ^ { * }$ iwgth $( i , j )$ $i \neq j$   
$\tau \in \textit { T P } _ { p } ^ { * }$ such that $\phi _ { i } ( \tau ) \neq \phi _ { j } ( \tau ) .$ Consequently,a certain finite linear combina  
tion of the columns of $\boldsymbol { \Phi } _ { \mathrm { P R K } } ^ { * }$ has distinct elements,i.e.,there exist vectors $\xi \in \mathbb { R } ^ { \infty }$   
(only finitely many non zero elements）and $\eta \in \mathbb R ^ { s }$ with $\Phi _ { \mathrm { P R K } } ^ { * } \xi = \eta$ and $\eta _ { i } \neq \eta _ { j }$   
for $i \neq j$ Due to the fact that $\phi _ { i } ( [ \tau _ { 1 } , \dots , \tau _ { m } ] ) = \phi _ { i } ( [ \tau _ { 1 } ] ) \cdots \cdot \phi _ { i } ( [ \tau _ { m } ] )$ ,thecom  
ponentwise product of two columns of $\phi _ { \mathrm { P R K } } ^ { * }$ is again a column of $\phi _ { \mathrm { P R K } } ^ { * }$ Continuing   
thisargumentation and observing that $( 1 , \dots , 1 ) ^ { T }$ isa column of $\boldsymbol { \varPhi } _ { \mathrm { P R K } } ^ { * }$ ,weobtain   
amatrix $X$ such that $\begin{array} { r } { \varPhi _ { \mathrm { P R K } } ^ { * } X = ( \eta _ { i } ^ { \jmath - 1 } ) _ { i , j = 1 } ^ { s } } \end{array}$ isaVandermonde matrix.Since the $\eta _ { i }$   
are distinct,the matrix $\phi _ { \mathrm { P R K } } ^ { * }$ has tobe of full rank $s$ ： $\sqcap$

# VI.7.4 Characterization of Irreducible Symplectic Methods

The necessity of the condition (4.2) for symplectic Runge-Kutta methodswas first statedbyLasagni(1988).Abia& Sanz-Serna(1993)extended hisproof to partitioned methods.We follow here the ideas of Hairer(1994).

Theorem7.10.An irreducible Runge-Kuttamethod(II.1.4) issymplecticifand onlyifthecondition(4.2) holds.

AnirreduciblepartitionedRunge-Kuttamethod(I.2.2) issymplecticifandonly iftheconditions(4.3) and(4.4) hold.

ApartitionedRunge-Kuttamethod,irreducibleforseparableproblems,issymplecticforseparable Hamiltonians $H ( p , q ) = T ( p ) + U ( q )$ ifand onlyifthecondition(4.3) holds.

ProofThe“if'part ofall three statementshasbeenproved in Theorem4.3and Theorem4.6.Weprove the“only ifpart forpartitioned Runge-Kuta methods applied to general Hamiltonian systems (the other two statements can be obtained in the same way).

We consider the $s \times s$ matrix $M$ with entries $m _ { i j } = b _ { i } { \widehat a } _ { i j } + { \widehat b } _ { j } a _ { j i } - b _ { i } { \widehat b } _ { j } .$ The computationleading to formula(7.11） shows that for $u \in T P _ { p }$ and $v \in T P _ { q }$

$$
\phi ( u ) ^ { T } M \phi ( v ) = a ( u \circ v ) + a ( v \circ u ) - a ( u ) \cdot a ( v )
$$

holds.Dueto the symplecticity of the method,this expression vanishes and we obtain

$$
\Phi _ { \mathrm { P R K } } ^ { T } M \Phi _ { \mathrm { P R K } } = 0 ,
$$

where $\varPhi _ { \mathrm { P R K } }$ isthematrix ofLemma 7.9.Anapplication of this lemma then yields $M = 0$ ,which proves the necessity of(4.3).

For the vector $d$ with components $\begin{array} { r } { d _ { i } = b _ { i } - \widehat { b } _ { i } } \end{array}$ weget $d ^ { T } \Phi _ { \mathrm { P R K } } = 0$ ,andwe deduce from Lemma7.9 that $d = 0$ ,sothat (4.4) isalso seen to be necessary. $\sqsupset$

# VI.8 Conjugate Symplecticity

Thesymplecticity requirement may be too strongifwe are interested in a correct long-time behaviour of a numerical integrator.Stoffer(1988) suggestsconsidering methods that are not necessarily symplectic but conjugate to a symplectic method.

Definition 8.1. Two numerical methods $\phi _ { h }$ and $\psi _ { h }$ aremutuallyconjugate,if there existsa global change of coordinates $x h$ ,suchthat

$$
\tilde { \varPhi } _ { h } = \chi _ { h } ^ { - 1 } \circ \varPsi _ { h } \circ \chi _ { h } .
$$

Weassume that $\chi _ { h } ( y ) = y + \mathcal { O } ( h )$ uniformly for $_ y$ varying inacompact set.

Foranumerical solution $y _ { n + 1 } ~ = ~ \varPhi _ { h } ( y _ { n } )$ ,lyinginacompact subset of the phasespace,the transformed values $z _ { n } = \chi _ { h } ( y _ { n } )$ constitute a numerical solution $z _ { n + 1 } = \varPsi _ { h } ( z _ { n } )$ of the second method.Since $y _ { n } - z _ { n } = \mathcal { O } ( h )$ ,bothnumerical solutions have the same long-time behaviour,independently of whether one method sharescertain properties (e.g.,symplecticity)with the other.

# VI.8.1 Examples and Order Conditions

Themost prominent pair of conjugate methods are the trapezoidal and midpoint rules.Their conjugacy has been originally exploited by Dahlquist(1975) in an investigation on nonlinear stability.

If we denote by $\varPhi _ { h } ^ { E }$ and $\varPhi _ { h } ^ { I }$ theexplicitand implicit Euler methods,respectively, then the trapezoidalrule $\varPhi _ { h } ^ { I }$ andtheimplicit midpointrule $\Phi _ { h } ^ { M }$ can be written as

$$
\begin{array} { r } { \varPhi _ { h } ^ { T } = \varPhi _ { h / 2 } ^ { I } \circ \varPhi _ { h / 2 } ^ { E } , \qquad \varPhi _ { h } ^ { M } = \varPhi _ { h / 2 } ^ { E } \circ \varPhi _ { h / 2 } ^ { I } } \end{array}
$$

(seFg8.1).hishows $\bar { \varPhi } _ { h } ^ { T } = \chi _ { h } ^ { - 1 } \bar { \varPhi } _ { h } ^ { M } \chi _ { h }$ with $\chi _ { h } = \varPhi _ { h / 2 } ^ { E }$ implying tat the trapezoidal and midpoint rulesare mutually conjugate.The change ofcoordinates, which transforms the numerical solution of one method to that of the other,is $\mathcal { O } ( h )$ close to the identity.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0004_pages_0211-0280/auto/images/1475c1070eef68cd9ac45a0a92046f36c844d1ca87e41be3e20163cb9b9eb315.jpg)  
Fig.8.1.Conjugacy of the trapezoidal ruleand the implicit midpoint rule

In fact,wecandoeven better.If we let $\varPhi _ { h / 2 }$ be the square root of $\Phi _ { h } ^ { M }$ (i.e., $\varPhi _ { h / 2 } \circ \varPhi _ { h / 2 } = \varPhi _ { h } ^ { M }$ seeLemmaV3.2）tenweaveig8

$$
\bar { p } _ { h } ^ { T } = ( \varPhi _ { h / 2 } ^ { E } ) ^ { - 1 } \circ \varPhi _ { h } ^ { M } \circ \varPhi _ { h / 2 } ^ { E } = ( \varPhi _ { h / 2 } ^ { E } ) ^ { - 1 } \circ \varPhi _ { h / 2 } \circ \varPhi _ { h / 2 } \circ \varPhi _ { h / 2 } \circ \varPhi _ { h / 2 } ^ { - 1 } \circ \varPhi _ { h / 2 } ^ { E }
$$

ape $\chi _ { h } = \varPhi _ { h / 2 } ^ { - 1 } \circ \varPhi _ { h / 2 } ^ { E }$ $\varPhi _ { h / 2 }$ $\varPhi _ { h / 2 } ^ { E }$ transformation $\chi _ { h }$ is $\mathcal { O } ( h ^ { 2 } )$ -closetotheidentity.This showsthatforevery numerical solution of the trapezoidal rule there exists a numerical solution of themidpoint rulewhichremains $\mathcal { O } ( h ^ { 2 } )$ -close aslongasit stays ina compact set.A single trajectoryof the non-symplectic trapezoidal rule therefore behavesverymuch the same asatrajectory of'the symplectic implicit midpoint rule.

AStudy via B-Series.An investigation of Runge-Kutta methods,conjugate to asymplectic method,leadsus to the followingweaker requirement:we say that a numerical method $\varPhi _ { h }$ isconjugatetoa symplecticmethod $\psi _ { h }$ uptoorder $r$ ,ifthere existsa transformation $\chi _ { h } ( y ) = y + \mathcal { O } ( h )$ such that

$$
\Phi _ { h } ( h ) = \bigl ( \chi _ { h } ^ { - 1 } \circ \varPsi _ { h } \circ \chi _ { h } \bigr ) ( y ) + \mathcal { O } ( h ^ { r + 1 } ) .
$$

This implies thatthe error of such amethod behaves as the superposition of the error ofasymplectic method of order $p$ with that of a non-symplectic method of order $r$

Inthe following we assume thatall methods consideredas wellas the conjugacy mapping $\chi _ { h }$ can be represented asB-series

$$
\varPhi _ { h } ( y ) = B ( a , y ) , \qquad \varPsi _ { h } ( y ) = B ( b , y ) , \qquad \chi _ { h } ( y ) = B ( c , y ) .
$$

Using the composition formula(II.1.38)of B-series,condition (8.2) becomes

$$
( a c ) ( \tau ) = ( c b ) ( \tau ) \qquad \mathrm { f o r } \quad | \tau | \leq r .
$$

The following resultsare taken from the thesis of P.Leone (2000).

Theorem 8.2.Let $\varPhi _ { h } ( y ) = B ( a , y )$ represent anumericalmethod of order2. a) $\scriptstyle { i t }$ isalways conjugate to a symplectic method up to order3. $b ) \mathop { I t }$ is conjugatetoasymplecticmethoduptoorder4,ifandonly if

$$
a ( \bullet , \dot { \pmb { \gamma } } ) - 2 a ( \bullet , \dot { \pmb { \gamma } } ) = 0 , ~ a ( \pmb { \updownarrow } , \pmb { \updownarrow } ) - 2 a ( \bullet , \dot { \pmb { \gamma } } ) = 0 .
$$

Here,we use theabbreviation $a ( u , v ) = a ( u ) \cdot a ( v ) = a ( u \circ v ) - a ( v \circ u ) .$

Proof.The condition (8.4) allowsus to express $b ( \tau )$ asa function of $a ( u )$ for $| u | \leq$ $| \tau |$ andof $c ( v )$ for $| v | \leq | \tau | - 1$ (usethe formulas ofExampleIII.1.11).All we have to do is to check the symplecticity conditions $b ( u , v ) = 0$ for $| u | + | v | \leq r$ (see Theorem 7.6).

Since the method $\phi _ { h }$ is of order2,we obtain $b ( \bullet ) = 1$ and $b ( \pmb { \zeta } ) = 1 / 2$ We arbitrarilyfix $c ( \bullet ) = 0$ ,sothat the symplecticity condition $b ( \bullet , \pmb { \zeta } ) = 0$ becomes $2 c ( \tilde { \mathcal { J } } ) = a ( \bullet , \tilde { \mathcal { J } } ) .$ Defining $c ( \tilde { \mathbb { Z } } )$ by this relation proves statement (a).

Fororder 4,the three symplecticity conditions $b ( \bullet , \underline { { { \sf V } } } ) ~ = ~ b ( \bullet , \underline   { \sf ( \bf { \lfloor \bullet \rfloor } \} \} } ) ~ =$ $b ( 2 , 2 ) = 0$ have to be fulfilled.One of themcan be satisfiedbydefining suitably $c ( \mathbb { V } ) + c ( [ [ { \circ } ] ] )$ ;the other two conditions are then equivalent to(8.5). $\sqcap$

Theorem8.3.Let $\begin{array} { r } { \varPhi _ { h } ( y ) = B ( a , y ) } \end{array}$ representanumericalmethod of order4.Itis conjugateto $a$ symplecticmethoduptoorder5,ifandonlyif

$$
\begin{array} { c } { { a ( \bullet , { \big Y } ) _ { \substack { \scriptstyle \gamma - 2 a ( \bullet , { \big Y } ) = 0 , \qquad a ( \bullet , { \bigvee } ) - 3 a ( \bullet , { \bigvee } ) + 3 a ( \bullet , { \big Y } ) = 0 , } } } } \\ { { a ( \underline { { { \boldsymbol \gamma } } } , { \bigvee } ) - a ( \bullet , { \bigvee } ) - 2 a ( \underline { { { \boldsymbol \gamma } } } , { \big Y } ) + 3 a ( \bullet , { \big Y } ) = 0 . } } \end{array}
$$

Proof.The ideaof the proof isthe same as in the preceding theorem.The verificationisleft asanexercise forthereader. □

Example8.4.A direct computation shows that for the Lobatto IIIB method with $s \ = \ 3$ wehave $a ( f , \mathbb { V } ) = 1 / 1 4 4$ and $a ( u , v ) = 0$ forall other pairs with $| u | + | v | = 5$ Theorem 8.3 thereforeproves that thismethod isnotconjugate to asymplectic methodupto order5.

For the Lobatto IIIA method with $s ~ = ~ 3$ we obtain $a ( \pmb { \zeta } , \pmb { \bigtriangledown } ) = - 1 / 1 4 4$ , $a ( \pmb { \zeta } , [ [ \bullet ] ] ) = - 1 / 2 8 8$ ,and $a ( u , v ) = 0$ for theremaining pairs with $| u | + | v | = 5$ . Thistime the conditions of Theorem 8.3are fulfilled,so that theLobatto IIIA method with $s = 3$ isconjugate toa symplectic method upto order 5at least.

# VI.8.2 Near Conservation of Quadratic First Integrals

Wehavealreadymet in Sect.VI.4.1acloserelationship between symplecticity and theconservation of quadratic first integrals.The aim of this section isto showa similar connection between conjugate symplecticity and the near conservation of quadratic first integrals.This has first beenobserved and proved by Chartier,Faou &Murua(2oo5)using the algebra of rooted trees.

Let $Q ( y ) = y ^ { T } C y$ (with symmetric matrix $C$ ）beaquadratic first integral of $\dot { y } = f ( y )$ ,and assume that $\varPhi _ { h } ( y )$ is conjugatetoa method $\varPsi _ { h } ( y )$ that exactly conservesquadratic first integrals(e.g.,symplecticRunge-Kuttamethods).Thismeans that $y _ { n + 1 } = \varPhi _ { h } ( y _ { n } )$ satisfies

$$
\chi _ { h } ( y _ { n + 1 } ) ^ { T } C \chi _ { h } ( y _ { n + 1 } ) = \chi _ { h } ( y _ { n } ) ^ { T } C \chi _ { h } ( y _ { n } ) ,
$$

and the expression ${ \bar { Q } } ( y ) = \chi _ { h } ( y ) ^ { T } C \chi _ { h } ( y )$ is exactly conserved by the numerical solution of $\varPhi _ { h } ( y )$ If ${ \chi _ { h } ( y ) = B ( c , y ) }$ isaB-series,this is of the form

$$
\widetilde { Q } ( y ) = \sum _ { \tau , \vartheta \in T \cup \{ \vartheta \} } h ^ { | \tau | + | \vartheta | } \beta ( \tau , \vartheta ) F ( \tau ) ( y ) ^ { T } C F ( \vartheta ) ( y ) ,
$$

where $F ( 0 ) ( y ) = y$ and $| \emptyset | = 0$ for the empty tree,and $\beta ( \emptyset , \emptyset ) = 1$ We have thefollowing criterion for conjugate symplecticity,where all formulas have to be interpreted in the sense of formal series.

Theorem 8.5.Assume that aone-step method $\varPhi _ { h } ( y ) = B ( a , y )$ leaves(8.6)invariant forall problems ${ \dot { y } } = f ( y )$ having $Q ( y ) = y ^ { T } C y$ asfirst integral.

Then,itisconjugate toasymplectic integrator $\varPsi _ { h } ( z )$ ,i.e.,thereexistsatransformation $z = \chi _ { h } ( y ) = B ( c , y )$ such that $\varPsi _ { h } ( z ) = \chi _ { h } \circ \varPhi _ { h } \circ \chi _ { h } ^ { - 1 } ( z )$ ,orequivalently, $\varPsi _ { h } ( z ) = B ( c ^ { - 1 } a c , z )$ issymplectic.

Proof.Theideaisto search foraB-series $B ( c , y )$ such that the expression (8.6） becomes

$$
\boldsymbol { \widetilde { Q } } ( \boldsymbol { y } ) = \boldsymbol { B } ( \boldsymbol { c } , \boldsymbol { y } ) ^ { T } \boldsymbol { C } \boldsymbol { B } ( \boldsymbol { c } , \boldsymbol { y } ) ,
$$

Themapping $z = \chi _ { h } ( y ) = B ( c , y )$ then provides a change of variables such that the original first integral $Q ( z ) = z ^ { T } C z$ is invariant in the new variables.By Theorem7.6 this then implies that $\psi _ { h }$ issymplectic.

ByLemma 8.6 below,the expression(8.6) can be written as

$$
\widetilde { Q } ( y ) = y ^ { T } C \Bigl ( y + \sum _ { \theta \in T } h ^ { | \theta | } \eta ( \theta ) F ( \theta ) ( y ) \Bigr ) ,
$$

where $\eta ( \theta ) = 0$ for $| \theta | < r$ ,if the perturbationin (8.6) is of size $\mathcal { O } ( h ^ { r } )$ Using the samelemma oncemore,we obtain

$$
\begin{array} { l } { { \displaystyle B ( c , y ) ^ { T } C B ( c , y ) ~ = ~ y ^ { T } C \left( y + 2 \sum _ { \ell \in T } \frac { h ^ { | \theta | } } { \sigma ( \theta ) } c ( \theta ) F ( \theta ) ( y ) \right) } } \\ { { \displaystyle ~ + ~ y ^ { T } C \left( \sum _ { \theta \in T } \Bigl ( \frac { h ^ { | \theta | } } { \sigma ( \theta ) } \sum _ { \tau , \vartheta \in T } \frac { \sigma ( \theta ) \kappa _ { \tau , \vartheta } ( \theta ) } { \sigma ( \tau ) \sigma ( \vartheta ) } c ( \tau ) c ( \vartheta ) F ( \theta ) ( y ) \right) , } } \end{array}
$$

Acomparison of the coeficientsin(8.7)and(8.8) uniquely defines $c ( \theta )$ inarecursive manner.We have $c ( \theta ) = 0$ for $| \theta | < r$ ,so that the transformation $z = B ( c , y )$ is $\mathcal { O } ( h ^ { r } )$ close to the identity. □

The previous proof is based on the following result.

Lemma 8.6.Let $Q ( y ) = y ^ { T } C y$ (with symmetric matrix $C$ )beafirst integral of $\dot { y } = f ( y )$ Then,foreverypairoftrees $\tau , \vartheta \in T$ wehave

$$
F ( \tau ) ( y ) ^ { T } C F ( \vartheta ) ( y ) = y ^ { T } C \Big ( \sum _ { \theta \in T } \kappa _ { \tau , \vartheta } ( \theta ) F ( \theta ) ( y ) \Big ) .
$$

Thissumisfiniteandonly over trees satisfying $| \theta | = | \tau | + | \vartheta | .$

Proof.Bydefinitionofafirst integral we have $y ^ { \prime } C f ( y ) = 0$ forall $y$ Differentiation with respect to $y$ gives

$$
f ( y ) ^ { T } C k + y ^ { T } C f ^ { \prime } ( y ) k = 0 \qquad { \mathrm { f o r ~ a l l ~ } } k .
$$

Putting $k = F ( \vartheta ) ( \boldsymbol { y } )$ ,this proves the statement for $\gamma = \cdot$

Differentiating once more yields

$$
( f ^ { \prime } ( y ) \ell ) ^ { T } C k + \ell ^ { T } C f ^ { \prime } ( y ) k + y ^ { T } C f ^ { \prime \prime } ( y ) ( k , \ell ) = 0 .
$$

Putting $\ell = f ( y )$ and using(8.9）,we get the statement for $\tau = \zeta$ With $\ell =$ $F ( \tau _ { 1 } ) ( y )$ we obtain the statement for $\tau = \left[ \tau _ { 1 } \right]$ provided that itisalready proved for $\tau _ { 1 }$ Weneedafurtherdifferentiationtogeta similarstatement for ${ \tau } = [ { \tau } _ { 1 } , { \tau } _ { 2 } ]$ ,etc. The proof concludes by induction on the order of $\tau$ . □

Partitioned Methods.This criterion for conjugate symplecticity can be extended topartitioned P-seriesmethods.For partitioned problems

$$
\dot { p } = f _ { 1 } ( p , q ) , \qquad \dot { q } = f _ { 2 } ( p , q )
$$

we consider first integrals of the form $L ( p , q ) = p ^ { T } E q$ ,where $E$ is anarbitrary constant matrix.If $\Phi _ { h } ( p , q )$ is conjugate toa method that exactly conserves $L ( p , q )$ , then itwill conserveamodified first integral of theform

$$
\widetilde { L } ( p , q ) = \sum _ { \tau \in T P _ { p } \cup \{ \vartheta _ { p } \} , \vartheta \in T P _ { q } \cup \{ \vartheta _ { q } \} } h ^ { | \tau | + | \vartheta | } \beta ( \tau , \vartheta ) F ( \tau ) ( p , q ) ^ { T } E F ( \vartheta ) ( p , q ) ,
$$

where $\beta ( \emptyset _ { p } , \emptyset _ { q } ) = 1 , F ( \emptyset _ { p } ) ( p , q ) = p , F ( \emptyset _ { q } ) ( p , q ) = q .$ We first extendLemma 8.6 to the new situation.

Lemma 8.7.Let $L ( p , q ) = p ^ { T } E q$ beafirstintegralof(8.1O).Then,forevery pair oftrees $\tau \in \mathit { T P } _ { p } , \vartheta \in \mathit { T P } _ { q } ,$ wehave

$$
\begin{array} { r } { F ( \tau ) ( p , q ) ^ { T } E F ( \vartheta ) ( p , q ) \ = \ p ^ { T } E \Big ( \displaystyle \sum _ { \theta \in T P _ { q } } \kappa _ { \tau , \vartheta } ( \theta ) F ( \theta ) ( p , q ) \Big ) } \\ { \displaystyle + \ \Big ( \displaystyle \sum _ { \theta \in T P _ { p } } \kappa _ { \tau , \vartheta } ( \theta ) F ( \theta ) ( p , q ) \Big ) ^ { T } E q . } \end{array}
$$

These sumsarefinite and only over trees satisfying $| \theta | = | \tau | + | \vartheta | .$

Proof.Since $L ( p , q ) \ = \ p ^ { T } E q$ isafirst integral of the differential equation,we have $f _ { 1 } ( p , q ) ^ { T } E q + p ^ { T } E f _ { 2 } ( p , q ) = 0$ forall $p$ and $q$ Asin the proof ofLemma8.6 thestatement follows from differentiation of thisrelation. □

Theorem 8.8.Assume that apartitioned one-step method $\begin{array} { r } { \varPhi _ { h } ( p , q ) = P ( a , ( p , q ) ) } \end{array}$ leaves $( 8 . I I )$ invariant forall problems(8.10) having $L ( p , q ) \ = \ p ^ { T } E q$ asfirst integral.

Thenitis conjugate toasymplectic integrator $\varPsi _ { h } ( u , v )$ ,i.e.,thereisatransformation $( u , v ) = \chi _ { h } ( p , q ) = P ( c , ( p , q ) )$ suchthat $\varPsi _ { h } ( u , v ) = \chi _ { h } \circ \varPhi _ { h } \circ \chi _ { h } ^ { - 1 } ( u , v ) .$ , orequivalently, ${ \varPsi } _ { h } ( u , v ) = P ( c ^ { - 1 } a c , ( u , v ) )$ issymplectic.

ProofWesearch foraP-series $P ( c , ( p , q ) ) = \left( P _ { p } ( c , ( p , q ) ) , P _ { q } ( c , ( p , q ) ) \right) ^ { T }$ such that the expression(8.11） can be written as

$$
\widetilde L ( p , q ) = P _ { p } ( c , ( p , q ) ) ^ { T } E P _ { q } ( c , ( p , q ) ) .
$$

Asin theproof of Theorem 8.5 themapping $( u , v ) = \chi _ { h } ( p , q ) = P ( c , ( p , q ) )$ then provides the searched change of variables.

UsingLemma 8.7 the expression (8.11) becomes

$$
( p , q ) = p ^ { T } E \Big ( q + \sum _ { \theta \in \mathit { T P } _ { q } } h ^ { | \theta | } \eta ( \theta ) F ( \theta ) ( p , q ) \Big ) + \Big ( \sum _ { \theta \in \mathit { T P } _ { p } } h ^ { | \theta | } \eta ( \theta ) F ( \theta ) ( p , q ) \Big ) ^ { T } E q ^ { T } ( \theta ) ,
$$

Also $P _ { p } ( c , ( p , q ) ) ^ { I } E P _ { q } ( c , ( p , q ) )$ can be written in such a form,and acomparison of the coefficients yields the coefficients $c ( \tau )$ of the P-series $P ( c , ( p , q ) )$ inarecursivemanner.We again have that $P ( c , ( p , q ) )$ is $\mathcal { O } ( h ^ { r } )$ close to the identity,if the perturbation in(8.11） is of size $\mathcal { O } ( h ^ { r } )$ □

The statement of Theorem 8.8 remains true in the class of second order differential equations $\ddot { q } = f _ { 1 } ( q )$ ,i.e., ${ \dot { p } } = f _ { 1 } ( p )$ ， ${ \dot { q } } = p$ .

# VI.9Volume Preservation

Theflow $\varphi _ { t }$ ofa Hamiltonian system preserves volume in phase space:for every bounded open set $\Omega \subset \mathbb { R } ^ { 2 d }$ and for every $t$ for which $\varphi _ { t } ( y )$ exists forall $y \in \mathcal { S } 2$ ,

$$
\mathrm { v o l } ( \varphi _ { t } ( \Omega ) ) = \mathrm { v o l } ( \Omega ) \ ,
$$

where $\begin{array} { r } { \operatorname { v o l } ( \Omega ) = \int _ { \Omega } d y . } \end{array}$ Thisidentity isoftenreferred toasLiouville'stheorem.It isaconsequence of the transformation formula for integralsand the fact that

$$
\operatorname* { d e t } { \frac { \partial \varphi _ { t } ( y ) } { \partial y } } = 1 \qquad { \mathrm { f o r ~ a l l ~ } } t { \mathrm { ~ a n d ~ } } y ,
$$

which follows directly from the symplecticityand $\varphi _ { 0 } = \mathrm { i d }$ Thesame argument showsthat every symplectic transformation,and in particular every symplectic integratorapplied toa Hamiltonian system,preserves volume in phase space.

Moregenerally than forHamiltoniansystems,volume ispreserved by the flow ofdifferential equations with a divergence-free vector field:

Lemma9.1.Theflowofadifferentialequation $\dot { y } = f ( y )$ in $\mathbb { R } ^ { n }$ is volume-preserving ifand only if $\mathrm { d i v } f ( y ) = 0$ forall $y$ .

Proof. Thederivative $\begin{array} { r } { Y ( t ) = \frac { \partial \varphi _ { t } } { \partial y } ( y _ { 0 } ) } \end{array}$ is the solutionofthevariationalequation

$$
\dot { Y } = A ( t ) Y , \quad Y ( 0 ) = I ,
$$

with the Jacobian matrix $A ( t ) = f ^ { \prime } ( y ( t ) )$ at $y ( t ) = \varphi _ { t } ( y _ { 0 } )$ From theproof of Lemma IV.3.1weobtain theAbel-Liouville-Jacobi-Ostrogradskii identity

$$
{ \frac { d } { d t } } \operatorname* { d e t } Y = \operatorname { t r a c e } A ( t ) \cdot \operatorname* { d e t } Y .
$$

Note that here trace $A ( t ) = \operatorname { d i v } f ( y ( t ) ) .$ Hence, $\operatorname* { d e t } Y ( t ) = 1$ for all $t$ if and only if $\mathrm { d i v } f ( y ( t ) ) = 0$ forall $t$ Sincethisisvalid forallchoices of initial values $y _ { 0 }$ ,the result follows. □

Example9.2 (ABC Flow).This flow,named after the threeindependent authors Arnold,Beltramiand Childress,is given by the equations

$$
\begin{array} { r } { \dot { x } = A \sin z + C \cos y } \\ { \dot { y } = B \sin x + A \cos z } \\ { \dot { z } = C \sin y + B \cos x } \end{array}
$$

and hasall diagonal elementsof $f ^ { \prime }$ identically zero.Itis thereforevolume preserving.InArnold(1966,p.347) it appeared ina footnoteasanexampleofaflowwith rotfparallel to $f$ ,thusviolatingArnold'scondition for the existence of invariant tori (Arnold 1966,p.346).Itwas therefore expected to possess interesting chaotic properties and has since then been the object of many investigations showing their non-integrability(seee.g.,Ziglin(1996)).We illustrateinFig.9.1 the action of this flowby transforming,inavolume preserving manner,a ball in $\mathbb { R } ^ { 3 }$ We see that, very soon,the set is strongly squeezed in one direction and dilated in two others. The solutions thus depend ina very sensitive way on the initial values.

Volume-Preserving Numerical Integrators.The question arises as to whether volume-preserving integrators can be constructed for every differential equation withvolume-preservingflow.Already for linearproblems,Lemma IV.3.2 shows thatno standard method can be volume-preserving for dimension $n \geq 3$ Nevertheless,positive answerswere foundbyQin& Zhu(1993),Shang(1994a,1994b), Feng& Shang(1995)andQuispel（1995).Inthefollowingwe present the approach ofFeng& Shang（1995).Thekeyis the followingresultwhich generalizesand reinterpretsaconstruction ofH.Weyl(1940) for $n = 3$ .

Theorem9.3(Feng&Shang1995).Everydivergence-freevectorfeld $f : \mathbb { R } ^ { n } $ $\mathbb { R } ^ { n }$ can be writtenas the sum of $n - 1$ vectorfields

$$
f = f _ { 1 , 2 } + f _ { 2 , 3 } + \ldots + f _ { n - 1 , n }
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0004_pages_0211-0280/auto/images/eb7db4f551c884a56c20c431f68c6b4a2fbf6539ab92c2196fd5d42a165bc8b2.jpg)  
Fig.9.1.Volume preservingdeformation of the ball of radius1,centred at theorigin,by the ABCflow; $A = 1 / 2$ , $B = C = 1$

whereeach $f _ { k , k + 1 }$ isHamiltonian in thevariables $( y _ { k } , y _ { k + 1 } )$ :thereexist functions $H _ { k , k + 1 } : \mathbb { R } ^ { n }  \mathbb { R }$ suchthat

$$
\boldsymbol { f } _ { k , k + 1 } = ( 0 , . . . , 0 , - \frac { \partial H _ { k , k + 1 } } { \partial y _ { k + 1 } } , \frac { \partial H _ { k , k + 1 } } { \partial y _ { k } } , 0 , . . . , 0 ) ^ { T } ,
$$

Proof. In terms of thecomponents of $\boldsymbol { f } ~ = ~ ( f _ { 1 } , \ldots , f _ { n } ) ^ { T }$ ,the functions $H _ { k , k + 1 }$ must satisfy the equations

$$
\begin{array} { r c l } { \displaystyle f _ { 1 } = - \frac { \partial H _ { 1 , 2 } } { \partial y _ { 2 } } , \quad \displaystyle f _ { 2 } = \frac { \partial H _ { 1 , 2 } } { \partial y _ { 1 } } - \frac { \partial H _ { 2 , 3 } } { \partial y _ { 3 } } , \ldots { } _ { \boldsymbol { v } } } \\ { \displaystyle f _ { n - 1 } = \frac { \partial H _ { n - 2 , n - 1 } } { \partial y _ { n - 2 } } - \frac { \partial H _ { n - 1 , n } } { \partial y _ { n } } , \quad \displaystyle f _ { n } = \frac { \partial H _ { n - 1 , n } } { \partial y _ { n - 1 } } . } \end{array}
$$

We thus set

$$
H _ { 1 , 2 } = - \int _ { 0 } ^ { y _ { 2 } } f _ { 1 } d y _ { 2 }
$$

andfor $k = 2 , \ldots , n - 2$

$$
H _ { k , k + 1 } = \int _ { 0 } ^ { y _ { k + 1 } } \Bigl ( \frac { \partial H _ { k - 1 , k } } { \partial y _ { k - 1 } } = f _ { k } \Bigr ) d y _ { k + 1 } .
$$

It remains to construct $H _ { n - 1 , n }$ from the last two equations.We see byinduction that for $k \leq n - 2$ ,

$$
{ \frac { \partial ^ { 2 } H _ { k , k + 1 } } { \partial y _ { k } \partial y _ { k + 1 } } } = - \Bigl ( { \frac { \partial f _ { 1 } } { \partial y _ { 1 } } } + \ldots + { \frac { \partial f _ { k } } { \partial y _ { k } } } \Bigr ) ,
$$

andhence theintegrabilityconditionfor $H _ { n - 1 , n }$

$$
\frac { \partial } { \partial y _ { n - 1 } } \Big ( \frac { \partial H _ { n - 2 , n - 1 } } { \partial y _ { n - 2 } } - f _ { n - 1 } \Big ) = \frac { \partial f _ { n } } { \partial y _ { n } } ~ ,
$$

reduces to the condition $\operatorname { d i v } f = 0$ ,which is satisfied byassumption. $H _ { n - 1 , n }$ can thus be constructed as

$$
H _ { n - 1 , n } = \int _ { 0 } ^ { y _ { n } } \left( { \frac { \partial H _ { n - 2 , n - 1 } } { \partial y _ { n - 2 } } } - f _ { n - 1 } \right) d y _ { n } + \int _ { 0 } ^ { y _ { n - 1 } } f _ { n } | _ { y _ { n } = 0 } d y _ { n - 1 } ,
$$

which completes the proof.

The above construction also shows that

$$
f _ { k , k + 1 } = ( 0 , . . . , 0 , f _ { k } + g _ { k } , - g _ { k + 1 } , 0 , \ldots , 0 )
$$

with

$$
g _ { k + 1 } = \int _ { 0 } ^ { y _ { k + 1 } } \left( { \frac { \partial f _ { 1 } } { \partial y _ { 1 } } } + . . . . + { \frac { \partial f _ { k } } { \partial y _ { k } } } \right) d y _ { k + 1 }
$$

for $1 \leq k \leq n - 2$ ,and $g _ { 1 } = 0$ and $g _ { n } = - f _ { n }$

With the decomposition ofLemma9.3at hand,a volume-preservingalgorithm isobtained by applyinga splitting method with symplectic substeps.For example, asproposed by Feng& Shang(1995),a second-order volume-preservingmethod is obtained by Strang splittingwith symplectic Euler substeps:

$$
\varphi _ { h } \approx \varPhi _ { h } = \varPhi _ { h / 2 } ^ { [ 1 , 2 ] * } \circ . . . \circ \varPhi _ { h / 2 } ^ { [ n - 1 , n ] * } \circ \varPhi _ { h / 2 } ^ { [ n - 1 , n ] } \circ . . . \circ \varPhi _ { h / 2 } ^ { [ 1 , 2 ] }
$$

where $\Phi _ { h / 2 } ^ { [ k , k + 1 ] }$ is asymplecticEulerstepoflength $h / 2$ applied to the system with right-hand side $f _ { k , k + 1 }$ ,and $^ *$ denotes theadjoint method.In this method,one step $\widehat { y } = \varPhi _ { h } ( y )$ is computed component-wise,ina Gauss-Seidel-like manner,as

$$
\begin{array} { l r } { { \overline { { { y } } } _ { 1 } ^ { \beta } = y _ { 1 } + \displaystyle \frac { h } { 2 } f _ { 1 } ( \overline { { { y } } } _ { 1 } , y _ { 2 } , \ldots , y _ { n } ) } } \\ { { \overline { { { y } } } _ { k } = y _ { k } + \displaystyle \frac { h } { 2 } f _ { k } ( \overline { { { y } } } _ { 1 } , \ldots , \overline { { { y } } } _ { k } , y _ { k + 1 } , \ldots , y _ { n } ) + \displaystyle \frac { h } { 2 } g _ { k } | _ { y _ { k } } ^ { \overline { { y } } _ { k } } } } & { { \mathrm { f o r } } ~ k = 2 , \ldots , n - 1 }  \\ { { \overline { { { y } } } _ { n } = y _ { n } + \displaystyle \frac { h } { 2 } f _ { n } ( \overline { { { y } } } _ { 1 } , \ldots , \overline { { { y } } } _ { n - 1 } , y _ { n } ) } } & { { \scriptstyle ( 9 . 4 } } \end{array}
$$

wit $\textrm { h } g _ { k } | _ { y _ { k } } ^ { \overline { { y } } _ { k } } = g _ { k } ( \overline { { y } } _ { 1 } , \ldots , \overline { { y } } _ { k } , y _ { k + 1 } , \ldots , y _ { n } ) - g _ { k } ( \overline { { y } } _ { 1 } , \ldots , \overline { { y } } _ { k - 1 } , y _ { k } , \ldots , y _ { n } ) ,$ and

$$
\begin{array} { l r } { { \widehat { y } _ { n } = \overline { { y } } _ { n } + \displaystyle \frac { h } { 2 } f _ { n } ( \overline { { y } } _ { 1 } , \ldots , \widehat { y } _ { n } ) } } \\ { { } } \\ { { \widehat { y } _ { k } = \overline { { y } } _ { k } + \displaystyle \frac { h } { 2 } f _ { k } ( \overline { { y } } _ { 1 } , \ldots , \overline { { y } } _ { k } , \widehat { y } _ { k + 1 } , \ldots , \widehat { y } _ { n } ) - \displaystyle \frac { h } { 2 } \overline { { y } } _ { k } | \widehat { \frac { y _ { k } } { y _ { k } } } \quad \mathrm { f o r } \ k = n - 1 , \ldots , 2 } } \\ { { } } \\ { { \widehat { y } _ { 1 } = \overline { { y } } _ { 1 } + \displaystyle \frac { h } { 2 } f _ { 1 } ( \overline { { y } } _ { 1 } , \widehat { y } _ { 2 } , \ldots , \widehat { y } _ { n } ) } } & { { } } \\ { { } } \end{array}
$$

with $\overline { { g } } _ { k } | _ { \overline { { y } } _ { k } } ^ { y _ { k } } \ = \ g _ { k } ( \overline { { y } } _ { 1 } , . . . , \overline { { y } } _ { k - 1 } , \widehat { y } _ { k } , . . . , \widehat { y } _ { n } ) - g _ { k } ( \overline { { y } } _ { 1 } , . . . , \overline { { y } } _ { k } , \widehat { y } _ { k + 1 } , . . . , \widehat { y } _ { n } )$ The methodisone-dimensionally implicit in general,but becomesexplicit in theparticular case where $\partial f _ { k } / \partial y _ { k } = 0$ forall $k$ .

Separable Partitioned Systems.Forproblems of the form

$$
\dot { y } = f ( z ) , \qquad \dot { z } = g ( y )
$$

with $y \in \mathbb { R } ^ { m }$ , $z \in \mathbb { R } ^ { n }$ ,thescheme(9.4)becomes the symplectic Eulermethod,(9.5) itsadjoint,and itscomposition theLobatto IIIA-IIIB extension of the Stormer-Verletmethod.Since symplectic explicit partitioned Runge-Kutta methods are compositions ofsymplectic Euler steps(TheoremVI.4.7),this observationproves that suchmethods are volume-preserving for systems(9.6).This fact was obtained by Suris(1996)bya direct calculation,without interpreting the methodsas compositionmethods.The question arises as to whether more symplectic partitioned Runge-Kutta methods are volume-preserving for systems (9.6).

Theorem9.4.Every symplectic Runge-Kutta methodwith atmost two stagesis volume-preserving forsystems(9.6) ofarbitrary dimension.

Proof.(a) The ideais to consider the Hamiltoniansystem with

$$
H ( u , v , y , z ) = u ^ { T } f ( z ) + v ^ { T } g ( y ) ,
$$

where $( u , v )$ are the conjugate variables to $( y , z ) .$ This system is of the form

$$
\begin{array} { c c } { { \dot { y } ~ = ~ f ( z ) ~ } } & { { ~ \dot { u } ~ = ~ - g ^ { \prime } ( y ) ^ { T } v } } \\ { { { \dot { z } } ~ = ~ g ( y ) ~ } } & { { ~ \dot { v } ~ = ~ - f ^ { \prime } ( z ) ^ { T } u . } } \end{array}
$$

Applying the Runge-Kutta method to this augmented system does not change the numerical solution for $( y , z )$ Forsymplecticmethodsthematrix

$$
\Big ( \frac { \partial ( y _ { 1 } , z _ { 1 } , u _ { 1 } , v _ { 1 } ) } { \partial ( y _ { 0 } , z _ { 0 } , u _ { 0 } , v _ { 0 } ) } \Big ) = M = \left( \begin{array} { c c } { R } & { 0 } \\ { S } & { T } \end{array} \right)
$$

satisfies $M ^ { I ^ { \prime } } J M = J$ which implies $R T ^ { T } = I .$ Below we shall show that $\operatorname* { d e t } T =$ det $R _ { * }$ This yields det $R = 1$ which implies that the method is volume preserving.

(b)One-stagemethods.The only symplectic one-stage method is the implicit midpoint rule forwhich $R$ and $T$ are computed as

$$
\begin{array} { l } { \displaystyle \left( I - \frac { h } { 2 } E _ { 1 } \right) R = I + \frac { h } { 2 } E _ { 1 } } \\ { \displaystyle \left( I + \frac { h } { 2 } E _ { 1 } ^ { T } \right) T = I - \frac { h } { 2 } E _ { 1 } ^ { T } , } \end{array}
$$

where $E _ { 1 }$ isthe Jacobian of the system (9.6) evaluated at the internal stage value. Since

$$
E _ { 1 } = \left( \begin{array} { c c } { { 0 } } & { { f ^ { \prime } ( z _ { 1 / 2 } ) } } \\ { { g ^ { \prime } ( y _ { 1 / 2 } ) } } & { { 0 } } \end{array} \right) ,
$$

a similarity transformation with the matrix $\boldsymbol { D } \ = \ \mathrm { d i a g } ( I , - I )$ takes $E _ { 1 }$ to $- E _ { 1 }$ Hence,the transformed matrix satisfies

$$
\left( I - { \frac { h } { 2 } } E _ { 1 } ^ { T } \right) ( D ^ { - 1 } T D ) = I + { \frac { h } { 2 } } E _ { 1 } ^ { T } .
$$

A comparison with (9.9) and the use of $\operatorname* { d e t } X ^ { T } = \operatorname* { d e t } X$ provesdet $R = \operatorname* { d e t } T$ for themidpointrule.

(c)Two-stage methods.Applyinga two-stage implicit Runge-Kutta method to 9.7)yields

$$
\left( \begin{array} { c c } { I - h a _ { 1 1 } E _ { 1 } } & { - h a _ { 1 2 } E _ { 2 } } \\ { - h a _ { 2 1 } E _ { 1 } } & { I - h a _ { 2 2 } E _ { 2 } } \end{array} \right) \left( \begin{array} { c } { R _ { 1 } } \\ { R _ { 2 } } \end{array} \right) = \left( \begin{array} { c } { I } \\ { I } \end{array} \right) ,
$$

where $R _ { i }$ is the derivative of the $( y , z )$ components of the ith stage with respect to $( y _ { 0 } , z _ { 0 } )$ ,and $E _ { i }$ is the Jacobian of the system(9.6)evaluated at theith internal stage value.From the solution ofthis system the derivative $R$ of(9.8） is obtained as

$$
R = I + ( b _ { 1 } E _ { 1 } , b _ { 2 } E _ { 2 } ) \binom { I - h a _ { 1 1 } E _ { 1 } } { - h a _ { 2 1 } E _ { 1 } } \stackrel { - h a _ { 1 2 } E _ { 2 } } { I - h a _ { 2 2 } E _ { 2 } } \binom { I } { I } .
$$

Withthedeterminantidentity

$$
t e t ( U ) \operatorname * { d e t } ( X - W U ^ { - 1 } V ) = \operatorname * { d e t } \left( \begin{array} { c c } { { U } } & { { V } } \\ { { W } } & { { X } } \end{array} \right) = d e t ( X ) \operatorname * { d e t } ( U - V X ^ { - 1 } W )
$$

which is seen by Gaussian elimination,this yields

$$
\operatorname* { d e t } { R } = \frac { \operatorname* { d e t } \bigl ( I \otimes I - h ( ( A - 1 | b ^ { T } ) \otimes I ) E \bigr ) } { \operatorname* { d e t } \bigl ( I \otimes I - h ( A \otimes I ) E \bigr ) } ,
$$

where $A$ and $b$ collect the Runge-Kutta coefficients,and $\boldsymbol { E } =$ blockdiag $( E _ { 1 } , E _ { 2 } )$ . For $D ^ { - 1 } T D$ we get the same formula with $\boldsymbol { E }$ replaced by $E ^ { T } ,$ If $A$ is an arbitrary $2 \times 2$ matrix,it follows from block Gaussian elimination that

$$
\operatorname* { d e t } \bigl ( I \otimes I - h ( A \otimes I ) E \bigr ) = \operatorname* { d e t } \bigl ( I \otimes I - h ( A \otimes I ) E ^ { T } \bigr ) ,
$$

which then proves $\begin{array} { r } { \operatorname* { d e t } R = \operatorname* { d e t } T . } \end{array}$ Notice that the identity(9.11） is no longer true ingeneral if $A$ is of dimension larger than two. □

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0004_pages_0211-0280/auto/images/c931c56486061949bc61180896d701f88407c6f1c86cdfd5998ec1425cb7b93c.jpg)  
Fig.9.2.Volume preservation ofGauss methods applied to(9.12)with $h = 0 . 8$

Wearecurious to see whether Theorem9.4 remains valid for symplectic Runge-Kutta methods with more than two stages.For this we apply the Gauss methodswith $s = 2$ and $s = 3$ to theproblem

$$
\dot { x } = \sin z , \qquad \dot { y } = \cos z , \qquad \dot { z } = \sin y + \cos x
$$

with initial value $( 0 , 0 , 0 )$ .Weshow inFig.9.2 thedeterminant of thederivative of thenumerical flow asa function of time.Only the two-stage method isvolumepreservingforthisproblemwhich isinagreement with Theorem 9.4.

# VI.10 Exercises

1.Let $\alpha$ and $\beta$ bethe generalized coordinates of thedouble pendulum,whose kineticand potential energies are

$$
\begin{array} { l } { { \displaystyle , \begin{array} { l } { { \cal T } = \frac { m _ { 1 } } { 2 } ( \dot { x } _ { 1 } ^ { 2 } + \dot { y } _ { 1 } ^ { 2 } ) + \frac { m _ { 2 } } { 2 } ( \dot { x } _ { 2 } ^ { 2 } + \dot { y } _ { 2 } ^ { 2 } ) } } \\ { { \cal U } = m _ { 1 } g y _ { 1 } + m _ { 2 } g y _ { 2 } . } \end{array} } \nonumber \end{array}
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0004_pages_0211-0280/auto/images/0fa4ab23aaa51e5d17055ac120ecfa57f6e75ee4eeff4a32a091da45a362f263.jpg)

Determine the generalized momenta of the corresponding Hamiltonian system.

2.Anon-autonomous Hamiltonian system is given bya time-dependent Hamiltonian function $H ( p , q , t )$ and the differential equations

$$
\dot { p } = - H _ { q } ( p , q , t ) , \dot { q } = H _ { p } ( p , q , t ) .
$$

Verify that these equations together with $\dot { e } = - H _ { t } ( p , q , t )$ and $\dot { t } = 1$ are the canonical equations for the extended Hamiltonian ${ \cal { H } } ( \widetilde { p } , \widetilde { q } ) = { \cal { H } } ( p , q , t ) + e$ with $\widetilde { p } = ( p , e )$ and $\widetilde { \boldsymbol { q } } = \left( \boldsymbol { q } , t \right)$ .

3.Prove that a linear transformation $A : \mathbb { R } ^ { 2 }  \mathbb { R } ^ { 2 }$ is symplectic,if and only if det $A = 1$ .

4.Consider the transformation $( r , \varphi ) \mapsto ( p , q )$ ,defined by

$$
p = \psi ( r ) \cos \varphi , \qquad q = \psi ( r ) \sin \varphi .
$$

Forwhich function $\psi ( r )$ isitasymplectic transformation?

5.Prove that the definition (2.4) of $\Omega ( M )$ does not depend on the parametrization $\varphi$ ,i.e.,theparametrization $\psi = \varphi \circ \alpha$ ,where $\alpha$ isadiffeomorphismbetween suitable domains of $\mathbb { R } ^ { 2 }$ ,leadsto the sameresult.

6.On the set $U = \left\{ ( p , q ) ; p ^ { 2 } + q ^ { 2 } > 0 \right\}$ consider thedifferential equation

$$
\binom { \dot { p } } { \dot { q } } = \frac { 1 } { p ^ { 2 } + q ^ { 2 } } \binom { p } { q } .
$$

Prove that

a)its flow is symplectic everywhere on $U$ ；

b)onevery simply-connected subset of $U$ thevectorfield(10.1)isHamiltonian (with $H ( p , q ) = - \mathrm { I m } \log ( p + i q ) + C o n s t )$ ;

c)it is not possible tofinda differentiable function $H : U  \mathbb { R }$ such that (10.1) isequal to $J ^ { - 1 } \nabla H ( p , q )$ forall $( p , q ) \in U$ .

Remark.The vector field(10.1) is locally(but not globally）Hamiltonian.

7.(Burnton&Scherer 1998).Prove that all members of the one-parameter family ofNystrom methods of order ${ } ^ { 2 s }$ ,constructed in Exercise III.9,are symplectic and symmetric.

8.Prove that the statement ofLemma 4.1remains truefor methods thatare formallydefinedbyaB-series, $\varPhi _ { h } ( y ) = B ( a , y )$ .

9.Compute the generating function $S ^ { 1 } ( P , q , h )$ ofasymplectic Nystrommethod applied to $\ddot { q } = U ( q )$ .

10.Find the Hamilton-Jacobi equation (cf.Theorem5.7) for the generating function $S ^ { 2 } ( p , Q )$ ofLemma5.3.

11.(Jacobi'smethodfor exact integration).Supposewe haveasolution $S ( q , Q , t , \alpha )$ of theHamilton-Jacobiequation (5.16),depending on $d$ parameters $\alpha _ { 1 } , \ldots , \alpha _ { d }$ such that the matrix $\Big ( \frac { \partial ^ { 2 } S } { \partial \alpha _ { i } \partial Q _ { j } } \Big )$ isinvertible.Since this matrix is the Jacobian of the system

$$
{ \frac { \partial S } { \partial \alpha _ { i } } } = 0 \qquad i = 1 , \ldots , d ,
$$

this system determines a solution path $Q _ { 1 } , \ldots , Q _ { q }$ which is locally unique.In possession of an additional parameter (and,including the partial derivatives with respect to $t$ ,anadditional row and column in the Hessian matrix condition),we can also determine $Q _ { j } ( t )$ as function of $t$ .Applythismethod tothe Keplerproblem(I.2.2）inpolarcoordinates,where,with the generalized momenta $p _ { r } = { \dot { r } } , p _ { \varphi } = r ^ { 2 } { \dot { \varphi } } .$ theHamiltonian becomes

$$
H = { \frac { 1 } { 2 } } \left( p _ { r } ^ { 2 } + { \frac { p _ { \varphi } ^ { 2 } } { r ^ { 2 } } } \right) - { \frac { M } { r } }
$$

and the Hamilton-Jacobi differential equation (5.16)is

$$
S _ { t } + \frac { 1 } { 2 } \big ( S _ { r } \big ) ^ { 2 } + \frac { 1 } { 2 r ^ { 2 } } \big ( S _ { \varphi } \big ) ^ { 2 } = \frac { M } { r } = 0 .
$$

Solve this equation by the ansatz $S ( t , r , \varphi ) = \theta _ { 1 } ( t ) + \theta _ { 2 } ( r ) + \theta _ { 3 } ( \varphi )$ (separation ofvariables).

Result.One obtains

$$
S = \int \sqrt { 2 \alpha _ { 1 } r ^ { 2 } + 2 M r - \alpha _ { 2 } ^ { 2 } } { \frac { d r } { r } } + \alpha _ { 2 } \varphi - \alpha _ { 1 } t .
$$

Putting,e.g., $\partial S / \partial \alpha _ { 2 } = 0$ ,weobtain $\begin{array} { r } { \varphi = \arcsin \frac { M r - \alpha _ { 2 } ^ { 2 } } { \sqrt { M ^ { 2 } + 2 \alpha _ { 1 } \alpha _ { 2 } ^ { 2 } } r } } \end{array}$ byevaluating anelementary integral.This,whenresolved for $r$ ,leads to theelliptic movement ofKepler (Sect.I.2.2).This method turned out to be most effective forthe exact integration of difficult problems.With the same ideas,just more complicated inthecomputations,Jacobi solves in“lectures”24 through 30of(Jacobi1842) theKepler motion in $\mathbb { R } ^ { 3 }$ ,thegeodesics of ellipsoids (his greatest triumph),the motionwith two centres of gravity,and provesa theorem ofAbel.

12.(Chan's Lobatto IISmethods.）Show that there exists a one-parameterfamily ofsymplectic,symmetric（and $A$ -stable)Runge-Kuttamethods of order $2 s - 2$ based on Lobatto quadrature(Chan 199O).A special case of thesemethodscan beobtained by takingthearithmeticmean of theLobatto IIIA andLobatto IIIB method coefficients(Sun 2000). Hint.Use the $W$ -transformation(seeHairer&Wanner(1996),p.77)byputting $X _ { s , s - 1 } = - X _ { s - 1 , s }$ anarbitrary constant.

13.Fora Hamiltonian system with associated Lagrangian $L ( q , \dot { q } ) = \textstyle { \frac { 1 } { 2 } } \dot { q } ^ { T } M \dot { q } -$ $U ( q )$ ,showthat every firstintegral $I ( p , q ) = p ^ { T } a ( q )$ resulting from Noether's Theorem hasa linear $a ( q ) = A q + c$ with skew-symmetric $M A$ . Hint.(a) Itis sufficient to consider the case $M = I$ . （b）Showthat $\boldsymbol { a ^ { \prime } } ( \boldsymbol { q } )$ is skew-symmetric. (c）Let $\begin{array} { r } { a _ { i j } ( q ) = \frac { \partial a _ { i } } { \partial q _ { j } } ( q ) } \end{array}$ Using the symmetry of the Hessian of each component $a _ { i } ( \boldsymbol q )$ ,show that $a _ { i j } ( q )$ does not depend on $q _ { i } , q _ { j }$ ,and is at most linear in theremaining components $q _ { k }$ .With the skew-symmetryof $a ^ { \prime } ( q )$ ,conclude that $a ^ { \prime } ( q ) = C o n s t$

14.Consider the unconstrained optimal control problem

$$
\begin{array} { r l } & { C \big ( q ( T ) \big ) \ \to \ \operatorname* { m i n } } \\ & { \dot { q } ( t ) = f \big ( q ( t ) , u ( t ) \big ) , \quad q ( 0 ) = q _ { 0 } } \end{array}
$$

on the interval $[ 0 , T ]$ ,where the control function is assumed to be continuous. Provethat first-order necessary optimality conditions can be written as

$$
\begin{array} { r l r l } & { \dot { q } ( t ) \ = \ \nabla _ { p } H \big ( p ( t ) , q ( t ) , u ( t ) \big ) , \ } & & { q ( 0 ) \ = \ q _ { 0 } } \\ & { \dot { p } ( t ) \ = \ - \nabla _ { q } H \big ( p ( t ) , q ( t ) , u ( t ) \big ) , \ } & & { p ( T ) \ = \ \nabla _ { q } C \big ( q ( T ) \big ) } \\ & { \ 0 \ = \ \nabla _ { u } H \big ( p ( t ) , q ( t ) , u ( t ) \big ) , \ } \end{array}
$$

where the Hamiltonian is given by

$$
H ( p , q , u ) = p ^ { T } f ( q , u )
$$

(weassume that the Hessian $\nabla _ { u } ^ { 2 } H ( p , q , u )$ is invertible,sothat the thirdrelation of（10.4）defines $u$ asa function of $( p , q )$ ).

Hint.Consider a slightly perturbed control function $u ( t ) + \varepsilon \delta u ( t )$ ,andlet $q ( t ) + \varepsilon \delta q ( t ) + \mathcal { O } ( \varepsilon ^ { 2 } )$ be the corresponding solution of the differential equation in(10.3).With the function $p ( t )$ of（10.4）we then have

$$
C ^ { \prime } { \bigl ( } q ( T ) { \bigr ) } \delta q ( T ) = \int _ { 0 } ^ { T } { \frac { d } { d t } } { \Bigl ( } p ( t ) ^ { T } \delta q ( t ) { \Bigr ) } d t = \int _ { 0 } ^ { T } p ( t ) ^ { T } f _ { u } { \bigl ( } \ldots { \bigr ) } \delta u ( t ) d t .
$$

Thealgebraic relation of(1o.4) then follows fromthe fundamental lemma of variational calculus.

15.ARunge-Kutta discretization of the problem(10.3）is

$$
\begin{array} { r } { C ( q _ { N } )  ~ { \mathrm { m i n } } } \\ { q _ { n + 1 } = q _ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Q _ { n i } , U _ { n i } ) } \\ { Q _ { n i } = q _ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Q _ { n j } , U _ { n j } ) } \end{array}
$$

with $n = 0 , \ldots , N - 1$ and $h = T / N .$ Weassume $b _ { i } \neq 0$ forall $i .$ Introducing suitable Lagrange multipliers for the constrained minimization problem（10.5), prove that there exist $p _ { n } , P _ { n i }$ such that the optimal solution of(10.5） satisfies (Hager 2000)

$$
\begin{array} { r l } & { q _ { n + 1 } = q _ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } \nabla _ { p } H ( P _ { n i } , Q _ { n i } , U _ { n i } ) } \\ & { \quad Q _ { n i } = q _ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } \nabla _ { p } H ( P _ { n j } , Q _ { n j } , U _ { n j } ) } \\ & { p _ { n + 1 } = p _ { n } = h \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } \nabla _ { q } H ( P _ { n i } , Q _ { n i } , U _ { n i } ) } \\ & { \quad P _ { n i } = p _ { n } - h \sum _ { j = 1 } ^ { s } \widehat { a } _ { i j } \nabla _ { q } H ( P _ { n j } , Q _ { n j } , U _ { n j } ) } \\ & { \quad \quad 0 = \nabla _ { u } H ( P _ { n i } , Q _ { n i } , U _ { n i } ) } \end{array}
$$

with $p _ { N } = \nabla _ { q } C ( q _ { N } )$ and given initial value $q _ { 0 }$ ,where the coefficients $\widehat { b } _ { i }$ and $\widehat { a } _ { i j }$ are determined by

$$
\widehat { b } _ { i } = b _ { i } , \qquad b _ { i } \widehat { a } _ { i j } + \widehat { b } _ { j } a _ { j i } = b _ { i } \widehat { b } _ { j } .
$$

Consequently,(1O.6)can be considered as a symplectic discretization of (10.4);   
see Bonnans $\&$ Laurent-Varin (2006).

16.(Hager 200O).For an explicit $s$ -stageRunge-Kuttamethod oforder $p = s$ and $b _ { i } \neq 0$ ,consider the partitioned Runge-Kutta method with additional coefficients $\widehat { b } _ { i }$ and $\widehat { a } _ { i j }$ defined by(10.7).Prove the following:

a)For $p = s = 3$ ,thepartitionedmethod isof order3ifand onlyif $c _ { 3 } = 1$ . b)For $p = s = 4$ ,thepartitioned method isof order4without any restriction
