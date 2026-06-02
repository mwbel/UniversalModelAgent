# Chapter X. Hamiltonian Perturbation Theory and Symplectic Integrators

Perturbation theoryisin fact an outgrowth of thenecessity todetermine the orbitswith ever greater accuracy.Thisproblem can besolved today, butinwhat is for the theoreticianarather disappointingway.With modern calculating machines,one is now ableto compute directlyresults even moreaccurately than those provided byperturbation theory.

(J.Moser 1978)

...allows computer prediction of planetary positions far more accurate (bybrute computation） than anything providedby classical perturbation theory.Inavery real sense,one of themost exhalted of human endeavors, goingback to the priests of Babylonand before,has been taken over by themachine. （S.Sternberg 1969)

In this chapter we study the long-time behaviour of symplectic integrators,combiningbackward error analysisand the perturbation theory of integrable Hamiltonian systems.

backward   
modified erroranal. numerical   
problem solution numerical method error？ original exact problem solution perturbation theory ierror？ 1   
approximate approximate problem solution

During the18th and 19th centuries,scientists struggled for the integration of complicated problems of dynamics,with the main aim of solving them analytically by "quadrature".But only fewproblems could be treated successfully in thisway.In cases where the original problem could not be solved,much effort was put into replacing itbyan integrableapproximateproblem,byusinganddevelopingperturbation theory.Thereby,aricharsenal ofvery ingenuous theorieshas beendiscovered since the 19th century.

In the1960s and 197Os,the enormousprogress of“calculating machines”and numerical software allowedmany of the original problems to be solved with extreme accuracy,so that for the first time numerical integration methods superseded analytical perturbation methods in the computations ofcelestial mechanics(see theabove citations).Since then,the further increasein computing speed has allowed problems tobetreated on larger and larger time scales,where huge amounts of errors areaccumulated and need to be understood and controlled.In the spirit of backward error analysis,thesenumerical errorsare interpretedas thoseofamodified problem,for the study of which perturbation theory is once again the appropriate tool.

# X.1 Completely Integrable Hamiltonian Systems

Integrable Hamiltonian systemswere originally of interest because their equations of motion can be solved analytically.Their interest in the present context lies in the fact that their flow is simply uniform motion on a Cartesian product of circles and straight lines insuitable coordinates,and that manyphysical systemscan be viewed as perturbations of integrable systems.

# X.1.1 Local Integration by Quadrature

M.Liouvillea fait voir qu’il fallait que toutes lescombinaisons $( \alpha , \beta )$ desintegrales trouvees fussent nulles. (E.Bour1855）

One of the great dreams of 18th and 19th century analytical mechanics was to solve theequations of motion of mechanical systems by“quadrature”,that is,using only evaluations and inversions of functions and calculating integrals ofknown functions. Inthis spirit,Newton's（1687)equations ofmotion of Kepler's two-body problem weresolved by Joh.Bernoulli(1710)and Newton(1713),see Sect.I.2.2.Euler's (1760) solution of the problem of the attraction of aparticle by two fixed centres, andLagrange's（1766) study of motion ofa particle ina field with one attracting centreand under an additional constant force were amongthe important achievementsof the 18th century.The three-bodyproblem,however,resistedall efforts aimingatan integration by quadrature,and though it continued todoso,thisproblemspurred thedevelopment of extremely useful mathematical theories ofamuch widerscope throughout the 19th century,from Poisson to Poincarévia Hamilton,Jacobi,Liouville,to name buta few of the most eminent mathematicians contributing to analytical mechanics.

Consider the Hamiltonian system

$$
\dot { p } = - \frac { \partial H } { \partial q } ( p , q ) , \quad \dot { q } = \frac { \partial H } { \partial p } ( p , q ) ,
$$

with $d$ degrees of freedom: $( p , q ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ We trytofindasymplectic transformation $( p , q ) \mapsto ( x , y )$ ,such that the system hasamore amenable formin thenew coordinates.In particular,thisis the case if the Hamiltonian expressed in the new variables,

$$
H ( p , q ) = K ( x ) ,
$$

does not depend on $_ y$ .Since $\begin{array} { l } { { \frac { \partial K } { \partial y } } \equiv 0 } \\ { . } \end{array}$ ,thetransformedsystemthen becomes (recall the conservation of the Hamiltonian form of the differential equations under symplectic transformations,Theorem VI.2.8)

$$
\dot { x } = 0 , \dot { y } = \omega ( x ) ,
$$

with $\begin{array} { r } { \omega ( x ) = \frac { \partial K } { \partial x } ( x ) . } \end{array}$ This is readilyintegated:

$$
x ( t ) = x _ { 0 } \ , \quad y ( t ) = y _ { 0 } + \omega ( x _ { 0 } ) t \ .
$$

Aswerecall from Sect.VI.5,a symplectic transformation $( p , q ) \mapsto ( x , y )$ canbe constructed viaageneratingfunction $S ( x , q )$ by the equations

$$
y = { \frac { \partial S } { \partial x } } ( x , q ) _ { \ast } \quad p = { \frac { \partial S } { \partial q } } ( x , q ) .
$$

If $( p _ { 0 } , q _ { 0 } )$ and $( x _ { 0 } , y _ { 0 } )$ arerelatedby(1.4),andif $\partial ^ { 2 } S / \partial x \partial q$ is invertible at $( x _ { 0 } , q _ { 0 } )$ ， then the equations(1.4)definea symplectic transformation between neighbourhoods of $( p _ { 0 } , q _ { 0 } )$ and $( x _ { 0 } , y _ { 0 } )$ .

The equation(1.2)together with the second equation of(1.4） giveapartial differential equation for $S$ ,theHamilton-Jacobiequation

$$
H \Bigl ( \frac { \partial S } { \partial q } ( x , q ) , q \Bigr ) = K ( x ) .
$$

If $S ( x , q )$ isa solution of such an equation (for some function $\boldsymbol { \kappa }$ ,then（1.3）shows that $x _ { i } = F _ { i } ( p , q )$ ( $i = 1 , \ldots , d )$ as given implicitly by the second equation of(1.4), arefirst integrals of the Hamiltonian system(1.1).Moreover,these functions $F _ { i }$ are ininvolution,which means that their Poisson brackets vanish pairwise:

$$
\{ F _ { i } , F _ { j } \} = 0 , \quad i , j = 1 , \ldots , d .
$$

This is an immediate consequence of the definition $\left\{ F , G \right\} = \nabla F ^ { T } J ^ { - 1 } \nabla G$ ofthe Poisson bracket and of the symplecticity of the transformation (the left upper block of $J ^ { - 1 }$ is $_ 0$ ).

Conversely,itwasrealized byBour(1855) andLiouville(1855)thataHamiltonian system having $d$ first integralsin involution can locally be transformed to the form(1.3）by“quadrature".This observationis based on the following completion resultand its proof.

Lemma 1.1 (Liouville Lemma). Let $F _ { 1 } , \ldots , F _ { d }$ be smooth real-valued functions, definedinaneighbourhoodof $( p _ { 0 } , q _ { 0 } ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ Suppose that these functions arein involution(i.e.,all Poisson brackets $\{ F _ { i } , F _ { j } \} = 0$ ),andthat their gradients are linearly independentat $( p _ { 0 } , q _ { 0 } )$ Then,thereexist smoothfunctions $G _ { 1 } , \ldots , G _ { d } ,$ defined on some neighbourhoodof $( p _ { 0 } , q _ { 0 } )$ ,suchthat

$$
( F _ { 1 } , . . . . , F _ { d } , G _ { 1 } , . . . , G _ { d } ) : ( p , q ) \mapsto ( x , y ) { \mathrm { \it ~ i s ~ a ~ s y m p l e c t i c ~ t r a n s f o r m a t i o n . } }
$$

Proof.Let $F = ( F _ { 1 } , \dots , F _ { d } ) ^ { T } .$ The linear independence of the gradients $\nabla F _ { i }$ implies that there are $d$ columns of the $d \times 2 d$ Jacobian $\partial { \cal F } / \partial ( p , q )$ that form an invertible $d { \times } d$ submatrix.After some suitable symplectic transformations (see Exercise1) wemay assumewithout loss of generality that $F _ { p } = \partial F / \partial p$ isinvertible.By the implicit function theorem,we can then locally solve $x = F ( p , q )$ for $p$ :

$$
p = P ( x , q ) \mathrm { w i t h \ p a r t i a l \ d e r i v a t i v e s } P _ { x } = F _ { p } ^ { - 1 } , P _ { q } = - F _ { p } ^ { - 1 } F _ { q } .
$$

The condition that the $F _ { i }$ areininvolution,reads in matrix notation

$$
F _ { p } F _ { q } ^ { T } - F _ { q } F _ { p } ^ { T } = 0 .
$$

Multiplyingthisequation with $F _ { p } ^ { - 1 }$ from the left and with $F _ { p } ^ { - T }$ from the right, we obtain

$$
- P _ { q } ^ { T } + P _ { q } = 0 ,
$$

so that $P _ { q } = \partial P / \partial q$ issymmetric.By the Integrability Lemma VI.2.7, $P ( x , q )$ is thus locally the gradient with respect to $q$ ofsome function $S ( x , q )$ （which is constructedbyquadrature).Moreover $\begin{array} { r } { \frac { \partial ^ { 2 } S } { \partial x \partial q } = P _ { x } = F _ { p } ^ { - 1 } } \end{array}$ is invertible.Theequations(1.4) define a symplectic transformation $( p , q ) \mapsto ( x , y )$ ,and by construction $x = F ( p , q )$ □

If,ina Hamiltonian system with $d$ degrees of freedom,we can find $d$ independent first integralsin involution $H \ = \ F _ { 1 } , F _ { 2 } , \ldots , F _ { d }$ ,thenLemma1.1yields asymplectic change of coordinates,constructed by quadrature,which transforms (1.1) locally to(1.2)with $K ( x _ { 1 } , \ldots , x _ { d } ) = x _ { 1 }$

Example1.2. Consider the Hamiltonian of motion in a central field,

$$
\begin{array} { r } { H = \frac { 1 } { 2 } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) + V ( r ) \quad \mathrm { ~ f o r ~ } r = \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } , } \end{array}
$$

with a potential $V ( r )$ thatisdefinedand smooth for $r > 0$ .TheKeplerproblem corresponds to the special case $V ( r ) = - 1 / r$ ,and the perturbed Kepler problem to $V ( r ) = - 1 / r - \mu / ( 3 r ^ { 3 } )$ Changing to polar coordinates (see Example VI.5.2）

$$
{ \binom { q _ { 1 } } { q _ { 2 } } } = { \binom { r \cos \varphi } { r \sin \varphi } } \ , \quad { \binom { p _ { r } } { p _ { \varphi } } } = { \binom { \cos \varphi } { - r \sin \varphi } } \ \sin \varphi \ { \binom { p _ { 1 } } { p _ { 2 } } } \ ,
$$

this becomes

$$
H ( p _ { r } , p _ { \varphi } , r , \varphi ) = \frac { 1 } { 2 } \Big ( p _ { r } ^ { 2 } + \frac { p _ { \varphi } ^ { 2 } } { r ^ { 2 } } \Big ) + V ( r ) .
$$

The system has the angular momentum $L = p _ { \varphi }$ asa first integral, since $H$ does not depend on $\varphi$ .Clearly, $\{ H , L \} = 0$ everywhere.The gradients of $H$ and $L$ are linearly independent unless both $p _ { r } = 0$ and $p _ { \varphi } ^ { 2 } = r ^ { 3 } V ^ { \prime } ( r )$ Byinserting $p _ { \varphi } ^ { 2 } =$ $2 r ^ { 2 } ( H - V ( r ) )$ andeliminating $r$ this becomes a condition of the form $\alpha ( H , L ) = 0$ , which for the Kepler problemreads explicitly $L ^ { 2 } ( 1 + 2 H L ^ { 2 } ) = 0 .$ The conditions ofLemma 1.1 are thus satisfied on thedomain

$$
M = \{ ( p _ { r } , p _ { \varphi } , r , \varphi ) \ ; \ r > 0 , \alpha ( H , L ) \neq 0 \} .
$$

The equations $\begin{array} { r } { x _ { 1 } = H = \frac { 1 } { 2 } ( p _ { r } ^ { 2 } + p _ { \varphi } ^ { 2 } / r ^ { 2 } ) + V ( r ) , x _ { 2 } = 1 } \end{array}$ $x _ { 2 } = L = p _ { \varphi }$ can be solved for

$$
p _ { r } = \pm \sqrt { 2 ( H - V ( r ) ) - L ^ { 2 } / r ^ { 2 } } , \quad p _ { \varphi } = L ,
$$

and $p _ { r } = \partial S / \partial r$ ， $p _ { \varphi } = \partial S / \partial \varphi$ with

$$
S ( H , L , r , \varphi ) = L \varphi \pm \int _ { r _ { 0 } } ^ { r } \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } d \rho .
$$

Theconjugate variables are

$$
\begin{array} { l } { { y _ { 1 } ~ = ~ { \displaystyle \frac { \partial S } { \partial H } } = \pm \int _ { r _ { 0 } } ^ { r } { \displaystyle \frac { 1 } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } } d \rho } , } \\ { { y _ { 2 } ~ = ~ { \displaystyle \frac { \partial S } { \partial L } } = \varphi \mp \int _ { r _ { 0 } } ^ { r } { \displaystyle \frac { L / \rho ^ { 2 } } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } } d \rho . } } \end{array}
$$

This defines (locally) the transformation $( p _ { r } , p _ { \varphi } , r , \varphi ) \mapsto ( x _ { 1 } , x _ { 2 } , y _ { 1 } , y _ { 2 } ) .$ In these variables,the equations of motion read $\dot { x } _ { 1 } = 0$ , $x _ { 2 } = 0$ , ${ \dot { y } } _ { 1 } = 1$ ， $y _ { 2 } = 0$ Overany time interval where $p _ { r } ( t )$ doesnot change sign,solutions therefore satisfy

$$
\begin{array} { r } { t _ { 1 } - t _ { 0 } = \pm \int _ { r ( t _ { 0 } ) } ^ { r ( t _ { 1 } ) } \frac { 1 } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho , } \\ { \varphi ( t _ { 1 } ) - \varphi ( t _ { 0 } ) = \pm \int _ { r ( t _ { 0 } ) } ^ { r ( t _ { 1 } ) } \frac { L / \rho ^ { 2 } } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho . } \end{array}
$$

# X.1.2 Completely Integrable Systems

Lemma 1.1 appears asapowerful tool foran explicit solution by quadrature.However,because of itspurely local nature this lemma does not tell usanythingabout thedynamicsof the system.Thiswasnot aconcern atLiouville's time,but the first rigorous non-integrability results by Poincaré（1892) put adefinite end to the hope of being eventually able to construct explicit analytic solutions of most equations of motion by quadrature,and shifted theinterest tounderstanding theglobal,qualitativebehaviour of dynamical systems.

Lemma 1.1can beglobalizedbyaprocedure similar toanalytic continuation if the conditions of the following definition are satisfied.

Definition1.3.A Hamiltonian systemwith Hamiltonian $H : M  \mathbb { R }$ $M$ anopen subset of $\mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ ）iscalled completely integrableif thereexistsmooth functions $F _ { 1 } = H , F _ { 2 } , \dots , F _ { d } : M \to \mathbb { R }$ with the following properties:

1） $F _ { 1 } , \ldots , F _ { d }$ arein involution (i.e.,all $\{ F _ { i } , F _ { j } \} = 0$ on $M$ . 2）The gradients of $F _ { 1 } , \ldots , F _ { d }$ arelinearlyindependentatevery pointof $M$ . 3）The solution trajectories of the Hamiltonian systems with Hamiltonian $F _ { i }$ $i =$ $1 , \ldots , d )$ exist forall timesand remain in $M$

Obviously,all the Hamiltonian systems with Hamiltonian $F _ { i }$ $i = 1 , \ldots , d )$ are thencompletely integrable,and so therewill benomathematical reasonto further distinguish $H = F _ { 1 }$ .Wenote thatcondition(1）ofDefinition1.3impliesthatall $F _ { j }$ arefirst integrals of the Hamiltonian systemwith Hamiltonian $F _ { i } ,$ and that theflows $\varphi _ { t } ^ { [ i ] }$ of theseHamiltoniansystemscommute: $\varphi _ { t } ^ { [ i ] } \circ \varphi _ { s } ^ { [ j ] } = \varphi _ { s } ^ { [ j ] } \circ \varphi _ { t } ^ { [ i ] }$ forall $i , j$ and all $t , s \in \mathbb { R }$ ;seeLemmaVII.3.2.

For $x = ( x _ { i } ) \in \mathbb { R } ^ { d }$ wedefine the level set

$$
M _ { x } = \{ ( p , q ) \in M ; \ F _ { i } ( p , q ) = x _ { i } \ { \mathrm { ~ f o r ~ } } i = 1 , \ldots , d \} .
$$

Theorem1.4. Suppose that $F _ { 1 } , \dots , F _ { d } : M \to \mathbb { R }$ satisfy the conditions of Definition1.3.Assume that $M _ { x }$ isconnected(andnon-empty)for al $x$ inaneighbourhood of $\boldsymbol { x } _ { 0 } \in \mathbb { R } ^ { d }$ .Then,onsome neighbourhood $B$ of $x _ { 0 }$ ,thereexistsasymplectic and surjective mapping

$$
e : B \times \mathbb { R } ^ { d } \to \bigcup _ { x \in B } M _ { x } : ( x , y ) \mapsto ( p , q ) \in M _ { x }
$$

that linearizes,forall $i = 1 , \ldots , d$ theflow $\varphi _ { t } ^ { [ i ] }$ ofthesystemwithHamiltonian $F _ { i }$

$$
\begin{array} { r } { { i f } ( p , q ) = e ( x , y ) , \quad t h e n \quad \varphi _ { t } ^ { [ i ] } ( p , q ) = e ( x , y + t e _ { i } ) , } \end{array}
$$

where $e _ { i } = ( 0 , \ldots , 1 , \ldots , 0 ) ^ { T }$ is the ith unit vector of $\mathbb { R } ^ { d }$ .

Since $e$ is symplectic, $e$ isalocal diffeomorphism.Itslocal inverse isa transformation as constructed inLemma 1.1.However, $( p , q )$ canhave countablymany discretely lying pre-images $( x , y )$ ,sothat $e ^ { - 1 }$ becomesa multi-valued function. The situation is analogous to that of the complex exponential and logarithm.The following example illustrates that thisanalogy is not incidental.

Example1.5.Considerthe harmonic oscillator,i.e., $d = 1$ and $\begin{array} { r } { H ( p , q ) = \frac 1 2 ( p ^ { 2 } + } \end{array}$ $q ^ { 2 }$ ).For $\begin{array} { r } { x = { \frac { 1 } { 2 } } r ^ { 2 } } \end{array}$ ,wehave $e ( x , y ) = ( r \cos y , r \sin y ) ,$

ProofofTheorem1.4.Wefix $( p _ { 0 } , q _ { 0 } ) \in M _ { x _ { 0 } }$ ,andinaneighbourhood $U$ of $( p _ { 0 } , q _ { 0 } )$ weconsiderasymplectic transformation

$$
\ell = ( F _ { 1 } , \dots , F _ { d } , G _ { 1 } , \dots , G _ { d } ) : ( p , q ) \mapsto ( x , y )
$$

as constructed in Lemma 1.1.We have $\ell ( p _ { 0 } , q _ { 0 } ) = ( x _ { 0 } , y _ { 0 } )$ where we may assume $y _ { 0 } = 0 .$ Toevery $v = ( v _ { i } ) \in \mathbb { R } ^ { d }$ we associate the Hamiltonian

$$
F _ { v } = v _ { 1 } F _ { 1 } + \ldots + v _ { d } F _ { d }
$$

andnotethat,becauseofthecommutativityofthefows $\varphi _ { t } ^ { [ i ] }$ ,theflow of the system with Hamiltonian $F _ { v }$ equals

$$
\varphi _ { t v } = \varphi _ { t v _ { 1 } } ^ { [ 1 ] } \circ \ldots \circ \varphi _ { t v _ { d } } ^ { [ d ] } .
$$

In the neighbourhood $U$ of $( p _ { 0 } , q _ { 0 } )$ ,the systemwith Hamiltonian $F _ { v }$ is transformed underthe symplectic mapping $\ell$ to

$$
\dot { x } = 0 , \quad \dot { y } = v .
$$

Hence,the following diagram commutes for $( p , q ) \in U$ and forsufficiently small $t v$

$$
\begin{array} { r l r } { ( p , q ) } & { { } \longrightarrow } & { \varphi _ { t v } ( p , q ) } \\ { \Big \downarrow \ell } & { { } } & { \Big \uparrow \ell ^ { - 1 } } \\ { ( x , y ) } & { { } \longrightarrow } & { ( x , y + t v ) } \end{array}
$$

Wenow construct $e$ byextending this diagram toarbitrary tu:

$$
\begin{array} { r l r } { ( p , q ) \quad } & { { } \longrightarrow } & { \varphi _ { y } ( p , q ) } \\ { { \hat { \Bigg \uparrow } } \ell ^ { - 1 } \quad } & { { } } & { } \\ { ( x , 0 ) \quad } & { { } \longleftarrow \quad } & { ( x , y ) } \end{array}
$$

That is,we define on $B \times \mathbb { R } ^ { d }$ (with $B$ aneighbourhood of $x _ { 0 }$ on which $\ell ^ { - 1 } ( x , 0 )$ is defined)

$$
e ( x , y ) = \varphi _ { y } \bigl ( \ell ^ { - 1 } ( x , 0 ) \bigr ) .
$$

For $( x , y )$ near some fixed $( \widehat { x } , \widehat { y } )$ ,we have by(1.10)with $y - \hat { y }$ and $\hat { y }$ instead of $y$ and $t v$ that

$$
e ( x , y ) = \varphi _ { \hat { y } } ( \ell ^ { - 1 } ( x , y - \widehat { y } ) ) \ ,
$$

which shows that $e$ issymplectic,being locally the composition of symplectic transformations.Theproperty(1.9)isobvious fromthedefinition of $e$ and from the comfows mutativity of the flows $\varphi _ { t } ^ { [ i ] }$ ,we have $e ( x , y ) \in M _ { x }$ $\varphi _ { t } ^ { [ i ] }$ Since foral $\ell ^ { - 1 } ( x , 0 ) \in M _ { x }$ $( x , y )$ and $M _ { x }$ is invariant under the

Itremains to show that $e : \{ x \} \times \mathbb { R } ^ { d } \to M _ { x }$ is surjective for every $x$ near $x _ { 0 }$ .Let $( \widehat { \boldsymbol { p } } , \widehat { \boldsymbol { q } } )$ beanarbitrary point on $M _ { x }$ Byassumption,there existsapath on $M _ { x }$ connecting $\ell ^ { - 1 } ( x , 0 )$ and $( \widehat { \boldsymbol { p } } , \widehat { \boldsymbol { q } } )$ .Moreover,by(1.10)andby the compactness of the path,there is a $\delta > 0$ such that,for every $( p , q )$ on this path,the mapping $y \mapsto \varphi _ { y } ( p , q )$ isadiffeomorphism between the ball $\| y \| < \delta$ andaneighbourhoodof $( p , q )$ on $M _ { x }$ .Therefore, $( \widehat { p } , \widehat { q } )$ can bereached from $\ell ^ { - 1 } ( x , 0 )$ byafinite composition of maps:

$$
( { \widehat { p } } , { \widehat { q } } ) = \varphi _ { y ^ { ( m ) } } \circ . . . \circ \varphi _ { y ^ { ( 1 ) } } ( \ell ^ { - 1 } ( x , 0 ) ) = \varphi _ { \widehat { y } } ( \ell ^ { - 1 } ( x , 0 ) ) = e ( x , { \widehat { y } } ) \ ,
$$

where $\widehat { y } = y ^ { ( 1 ) } + \ldots + y ^ { ( m ) }$ onceagainbythecommutativityoftheflows $\varphi _ { t } ^ { [ i ] }$ □

Illustration of the Liouville Transform.We illustrate the above construction at a simpleexample,thependulum(I.1.12）withHamiltonian $H = p ^ { 2 } / 2 - \cos q .$ The first coordinate is $x = H ( p , q )$ ,afirst integral.The secondcoordinate $y$ is,following (1.11),thetime $t$ whichis necessary to reach the point $( p , q )$ from an initial line, which we assume at $q = 0$ Thenwehave(Fig.1.1left) $d p d q = d H d t$ (because

$$
d p \frac { 1 ^ { p } } { \left[ \begin{array} { c c c c c } { d q } & { \cdots } & { \mathbf { \hat { ( A ) } } } & { \mathbf { \hat { ( A ) } } } & { \mathbf { \hat { ( C ) } } } & { \mathbf { \hat { ( B ) } } } & { \mathbf { \Huge \Huge d } ^ { \mathrm { ~ 2 ~ } } } & { \cdots } & { \mathbf { \Huge ( C ) } } \\ { d q ^ { \mathrm { ~ 2 ~ } } \cdots \cdots \sum _ { \mathbf { \hat { 2 } } } } & { \cdots } & { d H \frac { 1 ^ { \mathrm { ~ ~ 2 ~ } } } { \left[ \begin{array} { c c c c c } { d t } & { \cdots } & { \cdots } & { \mathbf { \Huge ( B ) } } & { \mathbf { \Huge d } ^ { \mathrm { ~ 2 ~ } } } & { \cdots } & { \mathbf { \Huge ( C ) } } \\ { d t } & { \cdots } & { \mathbf { \Huge ( C ) } } & { \mathbf { \Huge d } ^ { \mathrm { ~ 2 ~ } } } & { \cdots } & { \mathbf { \Huge d } ^ { \mathrm { ~ 2 ~ } } } \end{array} \right] } } \end{array} \right] }
$$

Fig.1.1.Liouvilleand action-angle coordinate transforms

of $d q \ = \ H _ { p } d t$ and $d H = H _ { p } d p )$ We see again that we have area preservation, because the symplecticity of theflow preserves thisproperty for all times.This symplectic change ofcoordinates $( p , q ) \mapsto ( x , y )$ isillustrated inFig.1.2,which transforms theproblem（A） toa much simpler form(B）withuniform horizontal movement.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0006_pages_0351-0420/auto/images/ad67da2f38da5a41c0664e84dfc202b32541d72e9f9eab03881b248ffd7d287d.jpg)  
Fig.1.2.Liouvilleand action-angle coordinates illustratedat thependulumproblem

Weare not yet completely satisfied,however,because the orbits have periods $g = g ( H )$ whichare not all the same.We thereforeappenda second transform by putting $\begin{array} { r } { \theta = \frac { 2 \pi } { g } \cdot t } \end{array}$ (seepicture(C)inFig.1.1andFig.1.2),which forcesallperiods intoaProcrustean bed of length $2 \pi$ Areapreservation $d a d \theta = d H d$ tnowrequires that $2 \pi d a = g ( H ) d H$ ,which isadifferential equation between $a$ and $H .$ Thenew coordinates $( a , \theta )$ aretheaction-angle variablesand we see that they transform the phase space into $D \times \mathbb { T } ^ { 1 }$ where $D \subset \mathbb { R } ^ { 1 }$ Weagain have horizontal movement,but this time the speed depends on $\boldsymbol { a }$ Thegeneral existence forcompletely integrable systemswill be proved in Theorem 1.6below.

# X.1.3Action-Angle Variables

Weshow here that,under the hypotheses ofLiouville's theorem,we can findsymplectic coordinates $( \mathbb { I } , \varphi )$ such that the first integrals $\mathbf { F }$ depend onlyon I,and $\varphi$ are angular coordinates on the torus $M _ { \mathrm { f } }$ ,

(V.I.Amold1989,p.279)

Weare now in the position to prove the main result of this section,which establishes asymplecticchange ofcoordinates to the so-called action-angle variables,such that $d$ firstintegrals of acompletely integrable system depend only on the actions,and theanglesaredefined globally mod $2 \pi$ (provided the level sets of the frst integrals arecompact).This isknown as the Arnold-Liouville theorem;cf.Arnold（1963, 1989),Arnold,Kozlov&Neishtadt（1997;Ch.4,Sect.2.1),Jost(1968).Here and in the following,

$$
\mathbb { T } ^ { d } = \mathbb { R } ^ { d } / 2 \pi \mathbb { Z } ^ { d } = \{ ( \theta _ { 1 } \bmod { 2 \pi } , \ldots , \theta _ { d } \bmod { 2 \pi } ) ; \theta _ { i } \in \mathbb { R } \}
$$

denotes the standard $d$ -dimensional torus.

Theorem 1.6 (Arnold-Liouville Theorem).Let $F _ { 1 } , \dots , F _ { d } ~ ; ~ M \to \mathbb { R }$ befirst integralsofacompletely integrable systemasin Definition1.3.Suppose that the levelsets $M _ { x }$ (see(1.8)) are compact and connected for all $x$ inaneighbourhood of $x _ { 0 } \in \mathbb { R } ^ { d }$ .Then,thereareneighbourhoods $B$ of $x _ { 0 }$ and $\mathcal { D }$ of $_ 0$ in ${ \mathbb R } ^ { d }$ suchthat thefollowing holds:

(i）Forevery $x \in B$ ,thelevelset $M _ { x }$ isa $d$ -dimensionaltorusthatisinvariant undertheflowofthe systemwith Hamiltonian $F _ { i }$ $i = 1 , \ldots , d ,$ ).

(ii)Thereexistsabijective symplectic transformation

$$
\psi : D \times \mathbb { T } ^ { d } \longrightarrow \bigcup _ { x \in B } M _ { x } \subset \mathbb { R } ^ { d } \times \mathbb { R } ^ { d } : ( a , \theta ) \longmapsto ( p , q )
$$

suchthat $( F _ { i } \circ \psi ) ( a , \theta )$ depends only on a,i.e.,

$$
F _ { i } ( p , q ) = f _ { i } ( a ) \quad f o r \quad ( p , q ) = \psi ( a , \theta ) \qquad ( i = 1 , \dots , d )
$$

with functions $f _ { i } : D \to \mathbb { R }$ .

Thevariables $( a , \theta ) \ = \ ( a _ { 1 } , \ldots , a _ { d } , \theta _ { 1 }$ mod $2 \pi , \ldots , \theta _ { d }$ mod $2 \pi$ ）arecalled action-anglevariables.

Remark 1.7.If thelevel sets $M _ { x }$ arenot compact,then theproof of Theorem1.6 showsthat $M _ { x }$ isdiffeomorphic toa Cartesian product of circles and straight lines $\mathbb { T } ^ { k } \times \mathbb { R } ^ { d - k }$ forsome $k < d$ ,andthereisa bijective symplectic transformation $( a , \theta ) \mapsto ( p , q )$ between $D \times ( \mathbb { T } ^ { k } \times \mathbb { R } ^ { d - k } )$ andaneighbourhood $\bigcup \{ M _ { x } : x \in B \}$ of $M _ { x _ { 0 } }$ such that the first integrals again depend only on $a$

Remark 1.8.If the Hamiltonian is real-analytic,then the proof shows thatalso the transformationtoaction-anglevariablesisreal-analytic.

ProofofTheorem1.6.(a)WereturntoTheorem1.4.For $x \in B$ ,weconsider the set

$$
\begin{array} { r } { T _ { x } = \left\{ y \in \mathbb { R } ^ { d } ; e ( x , y ) = e ( x , 0 ) \right\} . } \end{array}
$$

Since $e$ is locallyadiffeomorphism,foreveryfixed $y _ { 0 } \invarGamma _ { x _ { 0 } }$ there exists a unique smooth function $\eta$ defined on aneighbourhoodof $\scriptstyle { \mathcal { X } } 0$ ,suchthat $\eta ( x _ { 0 } ) = y _ { 0 }$ and $\eta ( x ) \in T _ { x }$ for $_ { x }$ near $x _ { 0 }$ .Inparticular, $T _ { x }$ isadiscrete subset of $\mathbb { R } ^ { d }$ By（1.9）, for $y \in \mathcal { I } _ { x }$ wehave $e ( x , y + v ) = e ( x , v )$ forall $\boldsymbol { v } \in \mathbb { R } ^ { d }$ .Therefore, $T _ { x }$ isa subgroup of $\mathbb { R } ^ { d }$ ,i.e.,with $y , v \in I _ { x } ^ { \prime }$ also $y + v \in I _ { x }$ and $- y \in I _ { x } .$ It then follows (see Exercise 4） that $\varGamma _ { x }$ isagrid,generated by $k \leq d$ linearly independent vectors $g _ { 1 } ( x ) , \ldots , g _ { k } ( x ) \in \mathbb { R } ^ { d }$

$$
\Gamma _ { x } = \{ m _ { 1 } g _ { 1 } ( x ) + . . . . + m _ { k } g _ { k } ( x ) ; m _ { i } \in \mathbb { Z } \} .
$$

Weextend $g _ { 1 } ( x ) , \ldots , g _ { k } ( x )$ toabasis $g _ { 1 } ( x ) , \ldots , g _ { d } ( x )$ of $\mathbb { R } ^ { d }$ Then, $e$ inducesa diffeomorphism

$$
\begin{array} { r c l } { \mathbb { T } ^ { k } \times \mathbb { R } ^ { d - k } } & { \to } & { M _ { x } } \\ { ( \theta _ { 1 } , \dots , \theta _ { k } , \tau _ { k + 1 } , \dots , \tau _ { d } ) } & { \mapsto } & { e \Big ( x , \displaystyle \sum _ { i = 1 } ^ { k } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( x ) + \displaystyle \sum _ { j = k + 1 } ^ { d } \tau _ { j } g _ { j } ( x ) \Big ) . } \end{array}
$$

If $M _ { x }$ is compact,then necessarily $k = d$ and $M _ { x }$ isa torus.The above map then becomes the bijection

$$
\mathbb { T } ^ { d } \to M _ { x } : \theta \mapsto e \Big ( x , \sum _ { i = 1 } ^ { d } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( x ) \Big ) ~ .
$$

(b)Next we show that $g _ { i } ( x )$ is the gradient of some function $U _ { i } ( x )$ Fornotational convenience,we omit the subscript $i$ and consideradifferentiable function $g$ with

$$
e ( x , g ( x ) ) = e ( x , 0 ) , \qquad x \in B ,
$$

or equivalently,

$$
\ell \circ e ( x , g ( x ) ) = ( x , 0 ) , \qquad x \in B .
$$

Differentiating thisrelation gives （with $I$ the $d$ -dimensional identity)

$$
A \left( \begin{array} { c } { { I } } \\ { { g ^ { \prime } ( x ) } } \end{array} \right) = \left( \begin{array} { l } { { I } } \\ { { 0 } } \end{array} \right)
$$

where $A$ is the Jacobian matrix of $\ell \circ e$ at $( x , g ( x ) )$ Wethushave

$$
( I ~ g ^ { \prime } ( x ) ^ { T } ) A ^ { T } J A \left( ~ \begin{array} { c } { { I } } \\ { { g ^ { \prime } ( x ) } } \end{array} \right) = ( I ~ 0 ) J \left( ~ \begin{array} { c } { { I } } \\ { { 0 } } \end{array} \right) = 0 .
$$

Since $\ell \circ e$ isa symplectic transformation,we have $A ^ { T } J A = J$ ,and hence the above equation reduces to

$$
g ^ { \prime } ( x ) ^ { T } - g ^ { \prime } ( x ) = 0 .
$$

BytheIntegrabilityLemmaVI.2.7,thereisafunction $U$ such that $g ( x ) = \nabla U ( x ) .$ We may assume $U ( x _ { 0 } ) = 0$

(c)The resultof(b)allowsus to extend the bijection of (a） toa symplectic transformation.For this,we consider the generating function

$$
S ( x , \theta ) = \sum _ { i = 1 } ^ { d } { \frac { \theta _ { i } } { 2 \pi } } U _ { i } ( x ) .
$$

With $u ( x ) = \left( U _ { 1 } ( x ) , . . . , U _ { d } ( x ) \right)$ ,the mixed second derivative of $S$ is

$$
S _ { x \theta } ( x , \theta ) = \frac { 1 } { 2 \pi } u _ { x } ( x ) = \frac { 1 } { 2 \pi } \Big ( g _ { 1 } ( x ) , . . . , g _ { d } ( x ) \Big ) ,
$$

which is invertible because of the linear independence of the $g _ { i }$ Theequations

$$
a = \frac { \partial S } { \partial \theta } = \frac { 1 } { 2 \pi } u ( x ) , \quad y = \frac { \partial S } { \partial x } = \sum _ { i = 1 } ^ { d } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( x )
$$

definea bijective symplectic transformation (for some neighbourhood $D$ of $0$ ,and possiblywith areduced neighbourhood $B$ of $x _ { 0 }$ )

$$
\beta : D \times \mathbb { R } ^ { d } \to B \times \mathbb { R } ^ { d } : ( a , \theta ) \mapsto ( x , y ) = \left( f ( a ) , \sum _ { i = 1 } ^ { d } \frac { \theta _ { i } } { 2 \pi } g _ { i } ( f ( a ) ) \right)
$$

where $x = f ( a )$ is the inverse map of $\begin{array} { r } { a = \frac { 1 } { 2 \pi } u ( x ) . } \end{array}$ We now define

$$
\widehat { \psi } = e \circ \beta : D \times \mathbb { R } ^ { d } \to \bigcup _ { x \in B } M _ { x } .
$$

Byconstruction,this mapis smooth and symplectic,and such that $f _ { i } ( a ) = x _ { i } =$ $F _ { i } ( p , q )$ for $( p , q ) = \widehat { \psi } ( a , \theta )$ ItissurjectivebyTheorem1.4.By part (a) of this proof,it becomes injectivewhen the $\theta _ { i }$ aretaken mod $2 \pi$ ,thusyieldinga transformation $\psi$ defined on $D \times  { \mathbb { T } } ^ { d }$ with the stated properties. □

# X.1.4 Conditionally Periodic Flows

Animmediate and important consequence of Theorem 1.6 is the following.

Corollary 1.9.Inthe situationofTheorem1.6,consider thecompletely integrable systemwith Hamiltonian $H = F _ { 1 }$ Intheaction-anglevariables $( a , \theta )$ ,theHamiltonianequationsbecome

$$
\dot { a } _ { i } = 0 , \quad \dot { \theta } _ { i } = \omega _ { i } ( a ) \qquad ( i = 1 , \ldots , d )
$$

with $\omega _ { i } ( a ) = \partial K / \partial a _ { i } ( a )$ where $K ( a ) = H ( p , q ) f o r ( p , q ) = \psi ( a , \theta ) .$

Theflow ofadifferential system

$$
\begin{array} { r l r } { \Dot { \theta } = \omega , } & { { } } & { \omega = ( \omega _ { i } ) \in \mathbb { R } ^ { d } } \end{array}
$$

on the torus $\mathbb { T } ^ { d }$ is called conditionally periodic with frequencies $\omega _ { i }$ Theflow is periodic if there exist integers $k _ { i }$ such that for anytwo frequencies the relation $\omega _ { i } / \omega _ { j } =$ $k _ { i } / k _ { j }$ holds.Otherwise,theflowiscalled quasi-periodic.In particular,the latter occurs when the frequencies are rationally independent,or non-resonant:the only integers $k _ { i }$ with $k _ { 1 } \omega _ { 1 } + \ldots + k _ { d } \omega _ { d } = 0$ are $k _ { 1 } = \ldots = k _ { d } = 0$ Fornonresonant frequencies,itiswell known（seeArnold(1989),p.287）that everytrajectory $\{ \theta ( t ) : t \in \mathbb { R } \}$ is dense on the torus $\mathbb { T } ^ { d }$ anduniformly distributed.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0006_pages_0351-0420/auto/images/b87f4113ee78594f9f1fb1dd23718137ac8c956c34b81aa67ac873cd05e912ff.jpg)

Example1.10.We takeupagain the example ofmotion inacentral field,Example1.2.For given $H$ and $\mathcal { L }$ ,wenow assume that

$$
\{ r > 0 ; 2 ( H - V ( r ) ) - L ^ { 2 } / r ^ { 2 } > 0 \} = [ r _ { 0 } , r _ { 1 } ]
$$

isanon-empty interval and thederivatives of $2 ( H - V ( r ) ) - L ^ { 2 } / r ^ { 2 }$ are nonvanishingat $r _ { 0 }$ , $r _ { 1 }$ .By(1.7）,themotion from $r _ { 0 }$ to $\tau _ { 1 }$ andback again takesa time $T$ and runs through anangle $\phi$ which are given by

$$
\begin{array} { r c l } { { T } } & { { = } } & { { 2 \displaystyle \int _ { r _ { 0 } } ^ { r _ { 1 } } \frac { 1 } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho , } } \\ { { \Phi } } & { { = } } & { { 2 \displaystyle \int _ { r _ { 0 } } ^ { r _ { 1 } } \frac { L / \rho ^ { 2 } } { \sqrt { 2 ( H - V ( \rho ) ) - L ^ { 2 } / \rho ^ { 2 } } } d \rho . } } \end{array}
$$

Note that $r _ { 0 }$ , $r _ { 1 }$ , $T$ ， $\boldsymbol { \Phi }$ are functions of $H$ and $\mathcal { L }$ .The solution is periodic if $\boldsymbol { \Phi }$ is arational multipleof $2 \pi$ Thisoccursfor theKeplerproblem,where $\phi = 2 \pi$ and where $T = 2 \pi / ( - 2 H ) ^ { 3 / 2 }$ (for $H < 0$ )depends onlyon $H$ ;see Exercise I.5.

Wenow construct action-angle variables and compute the frequencies of the system.We begin by constructing the mapping $e ( x , y )$ asdefined by（1.11）forthe variables $x = ( x _ { 1 } , x _ { 2 } ) = ( H , L )$ and $y \ = \ ( y _ { 1 } , y _ { 2 } )$ of(1.6）.Foragiven $( x , y )$ ， weconsider $( x , 0 )$ andwe fix $( p , q )$ with $p = ( p _ { r } , p _ { \varphi } )$ and $q = ( r , \varphi )$ such that $\ell ( p , q ) = ( x , 0 )$ ,e.g.,by choosing $r = r _ { 0 }$ , $\varphi = 0$ ， $p _ { r } = 0$ , $p _ { \varphi } = L .$ Themapping $e ( x , y )$ isdefinedby the flowat time $t = 1$ corresponding to the Hamiltonian

$$
F _ { y } = y _ { 1 } H + y _ { 2 } L = y _ { 1 } \Big ( { \textstyle \frac { 1 } { 2 } } ( p _ { r } ^ { 2 } + p _ { \varphi } ^ { 2 } / r ^ { 2 } ) + V ( r ) \Big ) + y _ { 2 } p _ { \varphi } ,
$$

i.e.,by the solution at $t = 1$ of

$$
\begin{array} { l } { { \displaystyle { \dot { p } } _ { r } = - y _ { 1 } \frac { p _ { \varphi } ^ { 2 } } { r ^ { 3 } } - y _ { 1 } V ^ { \prime } ( r ) ~ , \quad { \dot { p } } _ { \varphi } = 0 } } \\ { { \displaystyle { \dot { r } } = y _ { 1 } p _ { r } ~ , \quad { \dot { \varphi } } = y _ { 1 } \frac { p _ { \varphi } } { r ^ { 2 } } + y _ { 2 } . } } \end{array}
$$

If we denote the flow of the original system with Hamiltonian $H ( p _ { r } , p _ { \varphi } , r , \varphi )$ by $\varphi _ { t }$ ,thenwe have

$$
e ( x , y ) = \varphi _ { y _ { 1 } } ( 0 , L , r _ { 0 } , 0 ) + ( 0 , 0 , 0 , y _ { 2 } ) ^ { T }
$$

with the last component taken modulo $2 \pi$ Hence,the values of $y$ satisfying $e ( x , y ) = e ( x , 0 )$ are

$$
y = m _ { 1 } g _ { 1 } ( x ) + m _ { 2 } g _ { 2 } ( x )
$$

with integers $m _ { 1 } , m _ { 2 }$ and

$$
g _ { 1 } = \left( { \begin{array} { c } { T } \\ { - \varPhi } \end{array} } \right) , g _ { 2 } = \left( { \begin{array} { c } { 0 } \\ { 2 \pi } \end{array} } \right) .
$$

Weknow fromtheproof ofTheorem1.6that $g _ { 1 }$ and $g _ { 2 }$ are the gradients of functions $U _ { 1 } ( H , L )$ and $U _ { 2 } ( H , L )$ ,respectively.Clearly, $U _ { 2 } = 2 \pi L .$ The expression for $U _ { 1 }$ is lessexplicit.With theconstruction of the Integrability Lemma VI.2.7,this function isobtained byquadrature,inaneighbourhood of $( H _ { 0 } , L _ { 0 } )$ ,as

$$
\begin{array} { r } { U _ { 1 } ( H , L ) = \displaystyle \int _ { 0 } ^ { 1 } \Big ( \left( H - H _ { 0 } \right) T ( H _ { 0 } + s ( H - H _ { 0 } ) , L _ { 0 } + s ( L - L _ { 0 } ) ) = } \\ { ( L - L _ { 0 } ) \varPhi ( H _ { 0 } + s ( H - H _ { 0 } ) , L _ { 0 } + s ( L - L _ { 0 } ) ) \Big ) d s \ . } \end{array}
$$

(For the Kepler problem, $T = 2 \pi / ( - 2 H ) ^ { 3 / 2 }$ , $\phi = 0$ mod $2 \pi$ ,and hence $U _ { 1 } =$ $2 \pi / { \sqrt { - 2 H } } .$ )For the action variableswe thus obtain

$$
a _ { 1 } = \frac { 1 } { 2 \pi } U _ { 1 } ( H , L ) , \quad a _ { 2 } = L .
$$

Theangle variablesaregiven by $\begin{array} { r } { y = \frac { 1 } { 2 \pi } ( \theta _ { 1 } g _ { 1 } + \theta _ { 2 } g _ { 2 } ) } \end{array}$ ,i.e.,

$$
\theta _ { 1 } = y _ { 1 } \frac { 2 \pi } { T } , \theta _ { 2 } = y _ { 2 } + y _ { 1 } \frac { \Phi } { T } .
$$

Writing the total energy $H = K ( a _ { 1 } , L )$ if $a _ { 1 }$ isgiven bythe above formula,we obtain,bydifferentiation of the identity $2 \pi a _ { 1 } = U _ { 1 } ( K ( a _ { 1 } , L ) , L )$ ,

$$
2 \pi = \frac { \partial U _ { 1 } } { \partial H } \frac { \partial K } { \partial a _ { 1 } } , \quad 0 = \frac { \partial U _ { 1 } } { \partial H } \frac { \partial K } { \partial a _ { 2 } } + \frac { \partial U _ { 1 } } { \partial L }
$$

and hence the frequencies

$$
\omega _ { 1 } = \frac { \partial K } { \partial a _ { 1 } } = \frac { 2 \pi } { T } , \omega _ { 2 } = \frac { \partial K } { \partial a _ { 2 } } = \frac { \varPhi } { T } .
$$


<!-- chunk 0007: pages 421-490 -->
# X.1.5The Toda Lattice-an IntegrableSystem

Ourmethodis based on the realization that the Toda latice belongs to aclass of evolution equationswhich can be studied,and in some cases solved,byutilization ofacertain associated eigenvalueproblem.

(H.Flaschka 1974)

Classical examples of integrable systems from mechanics include Kepler's problem (Newton 1687/1713,Joh.Bernoulli 171O),theplanarmotion ofa point mass attracted by two fixedcentres(Euler176O),Kepler'sprobleminahomogeneous force field (Lagrange 1766 solved thisas the limit of the previous problem when one centreisatinfinity）,variousspinning tops(Euler 1758b,Lagrange1788,Kovalevskaya 1889,Goryachev 1899and Chaplygin 1901）,anumberof integrablecases of the motion ofarigidbody inafluid,themotionofpoint vorticesintheplane.Werefer toArnold,Kozlov&Neishtadt（1997）and Kozlov（1983） for interestingaccounts oftheseproblemsand for furtherreferences.

Herewe consider the celebrated example of the Toda latticewhich was the startingpoint fora hugeamount ofwork onintegrable systems in the last few decades, with fascinating relationships to soliton theory inpartial differential equations(most notably theKorteweg-deVries equation)and to eigenvaluealgorithms ofNumerical Analysis;see Deift(1996) for an account of these developments.

The Toda lattice(or chain)is asystem of particles on a line interacting pairwise withexponential forces.Such systemswere studied by Toda(1970)as discretemodelsfornonlinearwavepropagation.The motion isdetermined bytheHamiltonian

$$
H ( p , q ) = \sum _ { k = 1 } ^ { n } \Bigl ( { \frac { 1 } { 2 } } p _ { k } ^ { 2 } + \exp ( q _ { k } - q _ { k + 1 } ) \Bigr ) .
$$

Twotypes of boundary conditions have found particular attention in the literature:

(i) periodic boundary conditions: $q _ { n + 1 } = q _ { 1 }$ ; (ii)put formally $q _ { n + 1 } = + \infty$ ,sothat the term $\exp ( q _ { n } - q _ { n + 1 } )$ does not appear. Itwas found by Henon,Flaschkaand independently Manakov in1974 that the periodicToda systemis integrable.Moser(1975) thengavea detailed study of the non-periodic case (ii).

Flaschka（1974）introduced new variables

$$
\begin{array} { r } { a _ { k } = - \frac 1 2 p _ { k } \mathrm { ~ , ~ } b _ { k } = \frac 1 2 \exp \left( \frac 1 2 ( q _ { k } - q _ { k + 1 } ) \right) . } \end{array}
$$

(Take $b _ { n } = 0$ incase （ii)).Alongasolution $( p ( t ) , q ( t ) )$ of the Toda system,the corresponding functions $( a ( t ) , b ( t ) )$ satisfy the differential equations

$$
\dot { a } _ { k } = 2 ( b _ { k } ^ { 2 } - b _ { k - 1 } ^ { 2 } ) , \quad \dot { b } _ { k } = b _ { k } ( a _ { k + 1 } - a _ { k } )
$$

(with $a _ { n + 1 } = a _ { 1 }$ in case (i), $b _ { n } = 0$ in case (ii)). With the matrices

$$
\begin{array} { r l } { \boldsymbol { L } } & { = \left( \begin{array} { l l l l l } { a _ { 1 } } & { b _ { 1 } } & & & & { b _ { n } } \\ { b _ { 1 } } & { a _ { 2 } } & { b _ { 2 } } & & & \\ { b _ { 2 } } & { a _ { 3 } } & { b _ { 3 } } & & & \\ & & { \ddots } & { \ddots } & { \ddots } & & \\ & & & { b _ { n - 2 } } & { a _ { n - 1 } } & { b _ { n - 1 } } \end{array} \right) , } \\ { \boldsymbol { B } } & { = \boldsymbol { B } ( \boldsymbol { L } ) } & { = \left( \begin{array} { l l l l l } { 0 } & { b _ { 1 } } & & & & \\ { - b _ { 1 } } & { 0 } & { b _ { 2 } } & & & \\ { - b _ { 2 } } & { 0 } & { b _ { 3 } } & & & \\ & { - b _ { 2 } } & { 0 } & { b _ { 3 } } & & \\ & & & { \ddots } & { \ddots } & { \ddots } \\ & & & & { - b _ { n - 2 } } & { 0 } & { b _ { n - 1 } } \end{array} \right) , } \end{array}
$$

thedifferential equationscan bewrittenin theLaxpairform

$$
\dot { L } = B L - L B .
$$

Thissystem hasan isospectral flow,that is,alongany solution $L ( t )$ of(1.18）the eigenvalues do not depend on $t$ ；seeLemmaIV.3.4.Theeigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { n }$ of $L$ aretherefore first integralsof the Toda system.Theyare independent and turnout tobein involution,inaneighbourhood ofeverypointwhere the $\lambda _ { i }$ areall different;see Exercise6.Hence,the Toda lattice isacompletely integrable system.Its Hamiltonian can be written as

$$
H = \sum _ { k = 1 } ^ { n } \left( 2 a _ { k } ^ { 2 } + 4 b _ { k } ^ { 2 } \right) = 2 \operatorname { t r a c e } L ^ { 2 } = 2 \sum _ { i = 1 } ^ { n } \lambda _ { i } ^ { 2 } .
$$

Weconclude this section with a numerical example for the periodic Toda lattice. We choose $n = 3$ and the initial conditions $p _ { 1 } ~ = - 1 . 5$ , $p _ { 2 } = 1$ ， $p _ { 3 } ~ = ~ 0 . 5$ and $q _ { 1 } = 1$ , $q _ { 2 } = 2$ , $q _ { 3 } = - 1$ Weapplytothe systemwith Hamiltonian（1.17）the symplectic second-order Stormer-Verlet method and the non-symplectic classical fourth-order Runge-Kutta method with two different step sizes.Theleft pictures of Fig.1.3 show the numerical approximations to the eigenvalues,and theright pictures thedeviations of the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \lambda _ { 3 }$ along the numerical solution from their initial values.Clearly,the eigenvalues are not invariants of the numerical schemes. However,Fig.1.3illustrates that the eigenvalues along the numerical solution remainclose to their correctvalues over very long time intervals for the symplectic method,whereas theydrift off forthe non-symplectic method.

Anexplanation of the long-time near-preservation of the first integrals of completely integrable systemsby symplectic methodswill be given in the following sections,usingbackward error analysisand theperturbation theory forintegrable Hamiltonian systems.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/9326626c5350140a768c04c10ecdd0ca76443ad7dd74cd706828c7419f4a34df.jpg)  
Fig.1.3.Numerically obtained eigenvalues (left pictures)and errors in the eigenvalues (right pictures) for the step sizes $h = 0 . 1$ (dotted) and $h = 0 . 0 5$ (solid line)

# X.2 Transformations in the Perturbation Theory for Integrable Systems

Probleme général de la Dynamique.Nous sommes donc conduit a nous proposer leprobleme suivant:Etudier les quations canoniques

$$
{ \frac { d x _ { i } } { d t } } = { \frac { d \mathrm { F } } { d y _ { i } } } , \qquad { \frac { d y _ { i } } { d t } } = - { \frac { d \mathrm { F } } { d x _ { i } } } ,
$$

ensupposant que la fonctionF peut se developper suivant les puissances d'unparametre tres petit $\mu$ delamaniere suivante:

$$
\mathrm { F } = \mathrm { F } _ { 0 } + \mu \mathrm { F } _ { 1 } + \mu ^ { 2 } \mathrm { F } _ { 2 } + \ldots ,
$$

en supposant de plus que $\mathrm { ~ F _ { 0 } ~ }$ ne depend que des $x$ etest independant des $y$ ;etque $\mathrm { F } _ { 1 } , \mathrm { F } _ { 2 } , \ldots$ sont des fonctions periodiquesde période $2 \pi$ par rapportaux $_ { g }$ （H.Poincaré1892,p.32f.）

Considera small perturbation ofacompletely integrableHamiltonian.In actionanglevariables $( a , \theta )$ on $D \times  { \mathbb { T } } ^ { d }$ $\mathcal { D }$ an open subset of $\mathbb { R } ^ { d }$ ）,this takes the form

$$
H ( a , \theta ) = H _ { 0 } ( a ) + \varepsilon H _ { 1 } ( a , \theta ) ,
$$

where $\varepsilon$ isasmall parameter.Weassume that $H _ { 0 }$ and $H _ { 1 }$ arereal-analytic,and that theperturbation $H _ { 1 }$ (which maydepend also on $\succeq$ ）isbounded byaconstant ona complex neighbourhood of $D \times  { \mathbb { T } } ^ { d }$ thatisindependent of $\boldsymbol { \varepsilon }$ No other restriction shallbe imposed onthe perturbation.

For theunperturbed system（ $\varepsilon = 0$ )we have seen that the motion is conditionally periodic on invariant tori $\{ a \ = \ \mathrm { c o n s t . } , \theta \ \in \ \mathbb { T } ^ { d } \} .$ Perturbation theory aims at an understanding of the flow ofthe perturbed system.The basic toolsare symplectic coordinate transformationswhich take the system to a form that allows the longtimebehaviour(perpetually,or over time scaleslargecompared to $\varepsilon ^ { - 1 }$ of solutions ofthe system(certain solutions,orall solutions with initial values in some ball) to be read off.There are different transformations that provide answers to these problems. The emphasis in this section will be on the construction of suitable transformations, not on the technical but equally important aspects of obtaining estimates for them.

Themethods in Poincare'sMethodes Nouvelles form the nowclassical part of perturbation theory,butthetheoriesofBirkhoff,Siegel,Kolmogorov/Arnold/Moser (KAM)and Nekhoroshev inthe 2Oth century have become“classics”in theirown right.

# X.2.1 The Basic Scheme of Classical Perturbation Theory

In the spirit of the preceding section,one might search for a symplectic change of coordinates $( a , \theta ) \mapsto ( b , \varphi )$ closeto the identity suchthat theperturbed Hamiltonian written in the new variables $( b , \varphi )$ depends onlyon $^ { b }$ ,ormoremodestly,depends onlyon $b$ up toaremainder term of order $\mathcal { O } ( \varepsilon ^ { N } )$ witha large $N > 1$ ,ortobegin evenmoremodestly,with $N = 2$ Wesearch foragenerating function

$$
S ( b , \theta ) = b \cdot \theta + \varepsilon S _ { 1 } ( b , \theta )
$$

where·symbolizes the Euclidean product of vectorsin $\mathbb { R } ^ { d }$ and $S _ { 1 }$ is $2 \pi$ -periodic in $\theta$ .Naively,werequire that thesymplectic transformationdefined by

$$
a = \frac { \partial S } { \partial \theta } ( b , \theta ) , \quad \varphi = \frac { \partial S } { \partial b } ( b , \theta )
$$

be such that the order- $\boldsymbol { \varepsilon }$ term in the expansion of the Hamiltonian in the new variables, $K ( b , \varphi ) = H ( a , \theta )$ , $K ( b , \varphi ) = H _ { 0 } ( b ) + \varepsilon K _ { 1 } ( b , \varphi ) + \ldots .$ depends only on $b$ . Since

$$
H ( a , \theta ) = H { \Big ( } b + \varepsilon { \frac { \partial S _ { 1 } } { \partial \theta } } ( b , \theta ) , \theta { \Big ) } = H _ { 0 } ( b ) + \varepsilon { \Big \{ } \omega ( b ) \cdot { \frac { \partial S _ { 1 } } { \partial \theta } } ( b , \theta ) + H _ { 1 } ( b , \theta ) { \Big \} } + \varepsilon H _ { 2 } ( b ) .
$$

with the vector of frequencies

$$
\omega ( b ) = \frac { \partial H _ { 0 } } { \partial b } ( b ) ,
$$

the function $S _ { 1 }$ must satisfy thepartial differential equation

$$
\omega ( b ) \cdot \frac { \partial S _ { 1 } } { \partial \theta } ( b , \theta ) + H _ { 1 } ( b , \theta ) = \overline { { H } } _ { 1 } ( b )
$$

fora function $H _ { 1 }$ that does not depend on $\theta$ Since $S _ { 1 }$ is required to be $2 \pi$ -periodic in $\theta$ ,thefunction $H _ { 1 }$ must equal the average of $H _ { 1 }$ over the angles:

$$
\overline { { { H } } } _ { 1 } ( b ) = \frac { 1 } { ( 2 \pi ) ^ { d } } \int _ { \mathbb { T } ^ { d } } H _ { 1 } ( b , \theta ) d \theta .
$$

Equation(2.2)isthe basic equation of Hamiltonian perturbation theory.From the Fourier series of $S _ { 1 }$ and $H _ { 1 }$ ，

$$
S _ { 1 } ( b , \theta ) = \sum _ { k \in \mathbb { Z } ^ { d } } s _ { k } ( b ) e ^ { i k \cdot \theta } { _ \ast } \quad H _ { 1 } ( b , \theta ) \equiv \sum _ { k \in \mathbb { Z } ^ { d } } h _ { k } ( b ) e ^ { i k \cdot \theta }
$$

weobtain a formal solution of (2.2） by comparing Fourier coefficients: $s _ { 0 } ( b )$ is arbitraryand

$$
s _ { k } ( b ) = - \frac { h _ { k } ( b ) } { i k \cdot \omega ( b ) } , \qquad k \neq 0 .
$$

Atthispoint,however,weare struckby theproblemofsmalldenominators.Forany values of the frequencies $\omega _ { j } ( b )$ ,thedenominator $k \cdot \omega ( b ) = k _ { 1 } \omega _ { 1 } ( b ) + \ldots + k _ { d } \omega _ { d } ( b )$ becomes arbitrarily small for some $k = ( k _ { 1 } , \ldots , k _ { d } ) \in \mathbb { Z } ^ { d }$ ,and even vanishes if the frequenciesare rationally dependent.

Foraperturbation where only finitely many Fourier coefficients $h _ { k }$ arenonzero,the construction above excludes onlya finite number of resonant frequencies (i.e.,those with $k \cdot \omega ( b ) = 0$ fora $k \in  { \mathbb { Z } ^ { d } }$ with $h _ { k } \neq 0$ )andsmall neighbourhoods around them.For $\omega ( b )$ outside these neighbourhoods and for $\varphi$ onacomplex neighbourhood of $\mathbb { T } ^ { d }$ ,we obtain for the Hamiltonian in the new variables

$$
K ( b , \varphi ) = H _ { 0 } ( b ) + \varepsilon \overline { { { H } } } _ { 1 } ( b ) + \mathcal { O } ( \varepsilon ^ { 2 } ) .
$$

In the general case,we can approximate the perturbation $H _ { 1 }$ upto $\mathcal { O } ( \varepsilon ^ { 2 } )$ bya trigonometric polynomial.For analytic $H _ { 1 }$ ,theFourier coefficients $h _ { k }$ decayexponentiallywith $\begin{array} { r } { | k | = \sum _ { i } | k _ { i } | } \end{array}$ and hence therequired degree $m$ of theapproximating trigonometric polynomial grows logarithmicallywith $\varepsilon$ ,i.e., $m \sim | \log \varepsilon |$

As $\varepsilon  0$ ,theremainder term isunder control only for those frequencies $\omega = \omega ( b )$ forwhich the exponentially decaying Fourier coefficients $h _ { k }$ of the perturbationdecay faster than the denominators $i k \cdot \omega$ with growing $| k |$ This iscertainly thecase for frequenciessatisfying Siegel’'sdiophantine condition(or strong nonresonance condition,as itis sometimescalled)

$$
| \boldsymbol { k } \cdot \boldsymbol { \omega } | \geq \gamma | \boldsymbol { k } | ^ { - \nu } , \qquad \boldsymbol { k } \in \mathbb { Z } ^ { d } , \boldsymbol { k } \neq 0
$$

for some positive constants $\gamma$ , $\nu$ (Hereagain, $\begin{array} { r } { | k | = \sum _ { i } | k _ { i } | ) . } \end{array}$ If $\nu > d - 1$ thesetof frequencies ina fixed ball that do not satisfy(2.4) hasLebesgue measure bounded by Const. $\gamma$ (Exercise5).Therefore,almostall frequencies satisfy(2.4） for some $\gamma > 0$ However,forany $\gamma$ and $\nu$ ,thecomplementary set is open and dense in $\mathbb { R } ^ { d }$

# X.2.2Lindstedt-Poincaré Series

pour que la methode de M.Lindstedt soit applicable,soit sous sa forme primitive,soit sous celle que je lui ai ensuite donnee,il faut qu'en premiere approximation lesmoyens mouvementsne soient liesparaucune relation linéairea coefficients entiers;...

Il semble donc permis de conclure que les séries(..)ne convergent pas. Toutefois le raisonnement qui précedene suffit pas pour établir ce point avec une rigueur complete. （H.Poincare1893,pp.vi,103.）

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/a0eae888894e40163a0b954f3cd4d83070b79258a6684a1cd97a910f0e3cc1b7.jpg)  
Fig.2.1.Henri Poincaré(left),born:29April 1854inNancy(France),died:17July1912 inParis;AndersLindstedt(right),born:27June 1854in Sundborn (Sweden),died:1939. Reproduced with permission of Bibl.Math.Univ.Geneve

Theabove construction is extended without any additional difficulty toarbitrary finite order in $\boldsymbol { \varepsilon }$ .Thegenerating functionisnow sought in theform

$$
S ( b , \theta ) = b \cdot \theta + \varepsilon S _ { 1 } ( b , \theta ) + \varepsilon ^ { 2 } S _ { 2 } ( b , \theta ) + . . . , 4 \varepsilon ^ { N - 1 } S _ { N - 1 } ( b , \theta )
$$

and,as before,the requirement that the first $N$ terms in the $\varepsilon$ -expansion of the Hamiltonian in the new variables beindependent of the angles,leads viaa Taylor expansion of the Hamiltonian to equations of the form (2.2) for $S _ { 1 } , \ldots , S _ { N - 1 }$ ：

$$
\omega ( b ) \cdot \frac { \partial S _ { j } } { \partial \theta } + K _ { j } ( b , \theta ) = \overline { { K } } _ { j } ( b )
$$

where $K _ { 1 } = H _ { 1 }$ ,

$$
K _ { 2 } = { \frac { 1 } { 2 } } { \frac { \partial ^ { 2 } H _ { 0 } } { \partial a ^ { 2 } } } \left( { \frac { \partial S _ { 1 } } { \partial \theta } } , { \frac { \partial S _ { 1 } } { \partial \theta } } \right) + { \frac { \partial H _ { 1 } } { \partial a } } \cdot { \frac { \partial S _ { 1 } } { \partial \theta } } ,
$$

andin general, $K _ { j }$ isasum of terms

$$
\frac { 1 } { i ! } \frac { \partial ^ { i } H _ { k _ { 0 } } } { \partial a ^ { i } } \left( \frac { \partial S _ { k _ { 1 } } } { \partial \theta } , . . . , \frac { \partial S _ { k _ { i } } } { \partial \theta } \right) ~ \mathrm { w i t h } ~ k _ { 0 } + k _ { 1 } + . . . . + k _ { i } = j .
$$

The function $K _ { j }$ denotesagain theangular average of $K _ { j } .$ These equations can be formally solved in the case of rationally independent frequencies.The Hamiltonian in the new variablesis then

$$
K ( b , \varphi ) = H _ { 0 } ( b ) + \varepsilon \overline { { { K } } } _ { 1 } ( b ) + \varepsilon ^ { 2 } \overline { { { K } } } _ { 2 } ( b ) + \ldots + \varepsilon ^ { N - 1 } \overline { { { K } } } _ { N - 1 } ( b ) + \varepsilon ^ { N } R _ { N } ( b , \theta ) .
$$

The possible convergence of the series for $N  \infty$ isadelicate issue that was notresolved conclusively by Poincaré(1893） in hischapter on“Divergence des sériesde M.Lindstedt".If for some $b ^ { * }$ ,theseries(2.5）together with itspartial derivatives converged as $N  \infty$ ,then $\{ b = b ^ { * } , \varphi \in \mathbb { T } ^ { d } \}$ wouldbeaninvariant torusof theperturbed Hamiltonian system.However,itwas not until Kolmogorov (1954) that the existence of invariant tori-fordiophantine frequencies-was found, usinga different construction.A direct proof of the convergence of the series of classical perturbation theory for diophantine frequencies was obtained only in 1988 byEliasson (published in 1996);also see Giorgilli&Locatelli(1997)and references therein.

Nevertheless,already the truncated series (2.5)leads inarather simple way to strong conclusions about the flow over long time scales when itis combined with the idea of approximating the Hamiltonian bya trigonometricpolynomial:the“ultravioletcut-of”,an idea brieflyaddressedby Poincare(1893),p.98f.,andtaken to itsfull bearingbyArnold(1963)in hisproof of theKAM theorem.We formulatea lemma fora fixed truncation index $N$ Here, $\omega _ { \varepsilon , N } ( b )$ denotes the derivative of the truncated series(2.7）with respect to $b$

Lemma 2.1. Suppose that $\omega ( b ^ { * } )$ satisfies thediophantine condition (2.4).For any fixed $N \geq 2$ ,therearepositiveconstants $\varepsilon _ { 0 } , c , C$ suchthat the following holdsfor $\varepsilon \le \varepsilon _ { 0 }$ :thereexistsareal-analyticsymplecticchangeofcoordinates $( a , \theta ) \mapsto ( b , \varphi )$ such that every solution $( b ( t ) , \varphi ( t ) )$ oftheperturbed systeminthenewcoordinates, startingwith $\| b ( 0 ) - b ^ { * } \| \leq c \| \log \varepsilon | ^ { - \nu - 1 }$ satisfies

$$
\begin{array} { r l } & { \| b ( t ) - b ( 0 ) \| \le C t \varepsilon ^ { N } ~ f o r ~ t \le \varepsilon ^ { - N + 1 } , } \\ & { \| \varphi ( t ) - \omega _ { \varepsilon , N } ( b ( 0 ) ) t - \varphi ( 0 ) \| \le C ( t ^ { 2 } + t | \log \varepsilon | ^ { \nu + \bar { 1 } } ) \varepsilon ^ { N } ~ f o r ~ t ^ { 2 } \le \varepsilon ^ { - \widetilde { N } + 1 } . } \end{array}
$$

Moreover,the transformationis $\mathcal { O } ( \varepsilon )$ -closetotheidentity: $\| ( a , \theta ) - ( b , \varphi ) \| \leq C \varepsilon$ holds for $( a , \theta )$ and $( b , \varphi )$ relatedbytheabovecoordinatetransform,for $\vert \vert b - b ^ { * } \vert \vert \leq$ $c | \log \varepsilon | ^ { - \nu - 1 }$ andfor $\varphi$ inan $\boldsymbol { \varepsilon }$ -independentcomplexneighbourhoodof $\mathbb { T } ^ { d }$

Theconstants $\varepsilon _ { 0 } , c , C$ depend on $N , d , \gamma , \nu$ and on bounds of $H _ { 0 }$ and $H _ { 1 }$ on $a$ complexneighbourhoodof $\{ b ^ { * } \} \times \mathbb { T } ^ { d }$ .

Proof.Using therelations(2.3)and theiranalogues for(2.6),itisastraightforward but somewhat tedious exercise to show that at the given particular $b ^ { * }$ ,thefunctions $K _ { j } ( b ^ { * } , \cdot )$ ， $S _ { j } ( b ^ { * } , \cdot )$ areallanalytic on the same complex neighbourhood of $\mathbb { T } ^ { d }$ ,and thattheremainder termis boundedby

$$
\vert R _ { N } ( b ^ { * } , \theta ) \vert \le C = C ( N , d , \gamma , \nu )
$$

forall $\theta$ in acomplex neighbourhood of $\mathbb { T } ^ { d }$ which is independent of $\succeq$ Here, $C$ depends in addition on the bound of $H _ { 1 }$ ona complex neighbourhood of $\{ b ^ { * } \} \times \mathbb { T } ^ { d }$ , orwhat amountsto the same by Cauchy'sestimates,on bounds ofthe exponential decay of the Fourier coefficients $h _ { k }$ of $H _ { 1 }$ .(Incase of doubt,see also Sect.X.4 for explicit estimates.）

Assume first that $H _ { 1 } ( b , \theta )$ isatrigonometricpolynomial in $\theta$ ofdegree $m$ Then $K _ { j }$ ， $S _ { j }$ are trigonometricpolynomials of degree $j m$ Since $| k \cdot \omega ( b ) | \geq | k \cdot \omega ( b ^ { * } ) | -$ $| k | ( \operatorname* { m a x } \| \omega ^ { \prime } \| ) \| b - b ^ { * } \|$ ,thereisa $\delta > 0$ such that

$$
\begin{array} { r } { | k \cdot \omega ( b ) | \geq \frac { 1 } { 2 } \gamma | k | ^ { - \nu } \quad \mathrm { f o r } \quad \| b - b ^ { * } \| \leq \delta , | k | \leq N m . } \end{array}
$$

Thisnumber $\delta$ is proportional to $\gamma ( N m ) ^ { - \nu - 1 } .$ Consequently,since the construction involves only the trigonometric polynomials $K _ { j }$ , $S _ { j }$ of degree up to $N m$ ,theabove estimate for theremainder term $R _ { N }$ holdsalso for $\| b - b ^ { * } \| \leq \delta .$ Toapproximate ageneral analytic $H _ { 1 }$ by trigonometric polynomials up to $\mathcal { O } ( \varepsilon ^ { N } )$ ,wemust choose thedegree $_ { m }$ proportional to $\lvert \log \varepsilon ^ { N } \rvert$ With the choice $\delta = c ( N ^ { 2 } | \log \varepsilon | ) ^ { - \nu - 1 }$ , forasufficiently small $c > 0$ independent of $\boldsymbol { \varepsilon }$ （and $N$ ),theabove bound forthe remainder $R _ { N } ( b , \theta )$ is thenvalid for $b$ in the complex ball $\| b - b ^ { * } \| \leq 2 \delta$ and for $\varphi$ inacomplex neighbourhood of $\mathbb { T } ^ { d }$ (which depends only on $N$ ).ByCauchy's estimates,this implies

$$
\left\| \frac { \partial R _ { N } } { \partial \theta } ( b , \theta ) \right\| \leq C _ { \epsilon } , \quad \left\| \frac { \partial R _ { N } } { \partial b } ( b , \theta ) \right\| \leq \frac { C } { \delta }
$$

for $\| b - b ^ { * } \| \leq \delta$ and $\theta \in  { \mathbb { T } } ^ { d }$ Hence,as long as $\| b ( t ) - b ^ { * } \| \leq \delta$ ,the Hamiltonian differential equations are of the form

$$
\dot { \mathbf { \xi } } = - \frac { \partial K } { \partial \varphi } = - \varepsilon ^ { N } \frac { \partial R _ { N } } { \partial \theta } \frac { \partial \theta } { \partial \varphi } = \mathcal { O } ( \varepsilon ^ { N } ) , \quad \dot { \varphi } = \frac { \partial K } { \partial b } = \omega _ { \varepsilon , N } ( b ) + \mathcal { O } ( \varepsilon ^ { N } / \delta ) .
$$

This implies the result.

Hence,the tori $\{ b ~ = ~ b ( 0 ) , ~ \varphi ~ \in ~ \mathbb { T } ^ { d } \}$ arenearly invariant overa time scale $\varepsilon ^ { - N + 1 }$ andtheflowisclosetoaquasiperiodicflowover timesbounded bythe square root of $\varepsilon ^ { - N + 1 } .$ Lemma2.1isjustapreliminary tomoresubstantialresults (which hold under appropriateadditional conditions):invariant toricarryingaquasiperiodic flowwith diophantine frequencies persist under small Hamiltonian perturbations (Kolmogorov 1954);every solution of the perturbed system remainsclose, within a positive power of $\varepsilon$ ,to some torus over times that are exponentially long in a negative power of $\xi$ (Nekhoroshev 1977);solutions starting close to an invariant toruswith diophantine frequencies stay within twice the initial distance over time intervals that are exponentially long ina negativepower of the distance (Perry& Wiggins 1994)or even exponentially long in the exponential of the inverse of the distance（Morbidelli&Giorgilli1995).

The symplectic transformations of this subsection were constructed using the mixed-variable generating function $S ( b , \theta )$ Aswas pointed out for example by Benetin,Galgani& Giorgilli（1985),rigorousestimatesfor theremainder terms are often obtained inasimpler way using the Liemethod,which involves constructingthe near-identity symplectic transformation as the time- $\boldsymbol { \varepsilon }$ flow ofsome auxiliary Hamiltonian system witha suitablydefined Hamiltonian $\chi ( b , \varphi )$ Asbefore,the condition that the Hamiltonian ${ \cal H } ( a , \theta ) = { \cal K } ( b , \varphi )$ should depend on $\varphi$ onlyin higher-order terms,leadsto equations of the form (2.2),now for $\chi$ instead of $S _ { 1 }$ We will use such a construction in the following subsection.

# X.2.3Kolmogorov's Iteration

Itiseasy to grasp the meaning of Theorem1 formechanics.Itindicates thatan $s$ -parametricfamily ofconditionallyperiodicmotions[...]cannot, underconditions(3）and(4)[here:(2.4)and(2.9)],disappearasaresult ofasmall change in theHamilton function $H$ .

Inthis note we confine ourselves to the construction of the transformation. (A.N.Kolmogorov 1954)

For the completely integrable Hamiltonian $H _ { 0 } ( a )$ ,thephase space is foliated into invariant tori parametrized by $\boldsymbol { a }$ Wenow fix one such torus $\{ a = a ^ { * } , \theta \in  { \mathbb { T } } ^ { d } \}$ with strongly diophantine frequencies $\omega = \omega ( a ^ { * } )$ Without loss of generality,wemay assume $a ^ { * } = 0$ .Thisparticular torusisinvariantunderthe flowof everyHamiltonian $H ( a , \theta )$ forwhich the linear terms in the Taylor expansion with respect to $a$ at $0$ are independentof $\theta$

$$
\begin{array} { r } { H ( a , \theta ) = c + \omega \cdot a + \frac { 1 } { 2 } a ^ { T } M ( a , \theta ) a } \end{array}
$$

with $c \in \mathbb { R }$ ， $\omega \in \mathbb { R } ^ { d }$ ,andareal symmetric $d \times d$ -matrix $M ( \alpha , \theta )$ analytic in its arguments.Since the Hamiltonian equationsare of the form

$$
\dot { a } = \mathcal { O } ( \Vert a \Vert ^ { 2 } ) , \quad \dot { \theta } = w + \mathcal { O } ( \Vert a \Vert ) ,
$$

thetorus $\{ a = 0 , \ \theta \in  { \mathbb { T } } ^ { d } \}$ isinvariant and the flow on it is quasi-periodic with frequencies $\boldsymbol { \omega }$ .

Consider now an analytic perturbation of such a Hamiltonian: $H ( a , \theta ) + \varepsilon G ( a , \theta )$ witha small $\boldsymbol { \varepsilon }$ .Kolmogorov(1954）found anear-identity symplectic transformation $( a , \theta ) \mapsto ( \widetilde { a } , \theta )$ ,constructed by an iterativeprocedure,such that the perturbed Hamiltonian in the new variablesisagain of the form（2.8）with the same $\omega$ ,and hence has the invariant torus $\{ \widetilde { \boldsymbol { a } } = 0 , \ \widetilde { \boldsymbol { \theta } } \in \mathbb { T } ^ { d } \}$ carryingaquasi-periodic flow with thefrequencies of the unperturbed system.This holds under the conditions that $\omega$ satisfies thediophantine condition (2.4),and that theangularaverage

$$
\overline { { { M } } } _ { 0 } : = \frac { 1 } { ( 2 \pi ) ^ { d } } \int _ { \mathbb { T } ^ { d } } M ( 0 , \theta ) d \theta \quad \mathrm { ~ i s ~ a n ~ i n v e r t i b l e ~ m a t r i x . }
$$

Herewe describe the iterative construction of this symplectic transformation.The proof of convergence of the iteration will be given in Sect.X.5.

Weconstruct a symplectic transformation $( a , \theta ) \mapsto ( b , \varphi )$ asthe time- $\boldsymbol { \varepsilon }$ flowof anauxiliary Hamiltonian of the form

$$
\chi ( b , \varphi ) = \xi \cdot \varphi + \chi _ { 0 } ( \varphi ) + \sum _ { i = 1 } ^ { d } b _ { i } \chi _ { i } ( \varphi ) \ ,
$$

where $\xi \in \mathbb { R } ^ { d }$ is a constant vector,and $\chi _ { 0 } , \chi _ { 1 } , \ldots , \chi _ { d }$ are $2 \pi$ -periodic functions. (Quadraticand higher-order terms in $b$ playno role in the constructionand are thereforeomitted right at the outset.) The old and new coordinatesare thenrelated by

$$
a = b + \varepsilon \frac { \partial \chi } { \partial \varphi } ( b , \varphi ) + { \cal O } ( \varepsilon ^ { 2 } ) , \quad \theta = \varphi - \varepsilon \frac { \partial \chi } { \partial b } ( b , \varphi ) + { \cal O } ( \varepsilon ^ { 2 } ) .
$$

We insert this into

$$
\begin{array} { l } { \displaystyle H ( a , \theta ) + \varepsilon G ( a , \theta ) = c + \omega \cdot b + \frac 1 2 b ^ { T } M ( b , \varphi ) b } \\ { + \varepsilon \left\{ \omega \cdot \frac { \partial \chi } { \partial \varphi } ( b , \varphi ) + b ^ { T } M ( b , \varphi ) \frac { \partial \chi } { \partial \varphi } ( b , \varphi ) + G ( b , \varphi ) \right\} + \mathcal { O } ( \varepsilon \| b \| ^ { 2 } ) + \mathcal { O } ( \varepsilon ^ { 2 } ) . } \end{array}
$$

Wenow require that the term in curly brackets be $C o n s t + O ( \| b \| ^ { 2 } ) .$ Writingdown the Taylor expansion

$$
G ( b , \varphi ) = G _ { 0 } ( \varphi ) + \sum _ { i = 1 } ^ { d } b _ { i } G _ { i } ( \varphi ) + b ^ { T } Q ( b , \varphi ) b
$$

and inserting the above ansatz for $\chi$ ,this condition becomes

$$
\begin{array} { r } { \omega \cdot \displaystyle \frac { \partial \chi _ { 0 } } { \partial \varphi } ( \varphi ) + \displaystyle \sum _ { i = 1 } ^ { d } b _ { i } \left( \omega \cdot \frac { \partial \chi _ { i } } { \partial \varphi } ( \varphi ) + u _ { i } ( \varphi ) + v _ { i } ( \varphi ) \right) } \\ { + G _ { 0 } ( \varphi ) + \displaystyle \sum _ { i = 1 } ^ { d } b _ { i } G _ { i } ( \varphi ) = C o n s t . , } \end{array}
$$

where $\boldsymbol { u } = ( u _ { 1 } , \ldots , u _ { d } ) ^ { T }$ and $\boldsymbol { v } = ( v _ { 1 } , \ldots , v _ { d } ) ^ { T }$ are defined by

$$
\begin{array} { l } { { \displaystyle u ( \varphi ) = M ( 0 , \varphi ) \xi , } } \\ { { \displaystyle v ( \varphi ) = M ( 0 , \varphi ) \frac { \partial \chi _ { 0 } } { \partial \varphi } ( \varphi ) . } } \end{array}
$$

The condition is fulfilled if

$$
\begin{array} { l } { \displaystyle \omega \cdot \frac { \partial \chi _ { 0 } } { \partial \varphi } ( \varphi ) + G _ { 0 } ( \varphi ) = \overline { { G } } _ { 0 } } \\ { \displaystyle \omega \cdot \frac { \partial \chi _ { i } } { \partial \varphi } ( \varphi ) + u _ { i } ( \varphi ) + v _ { i } ( \varphi ) + G _ { i } ( \varphi ) \equiv \overline { { u } } _ { i } + \overline { { v } } _ { i } + \overline { { G } } _ { i } } \\ { \displaystyle \overline { { u } } _ { i } + \overline { { v } } _ { i } + \overline { { G } } _ { i } = 0 \qquad ( i = 1 , \ldots , d ) . } \end{array}
$$

Herethe barsagain denote angular averages.Note that equations(2.14),(2.15）are of the form (2.2).Equation (2.14) determines $\chi _ { 0 }$ and hence $v = ( v _ { 1 } , \ldots , v _ { d } ) ^ { T }$ by (2.13).Equations (2.16) then give $\overline { { u } } = ( \overline { { u } } _ { 1 } , \ldots , \overline { { u } } _ { d } ) ^ { T } .$ By(2.12）,we need

$$
\overline { { u } } = \overline { { M } } _ { 0 } \xi \mathrm { ~ , ~ }
$$

which determines $\xi$ uniquely because $\overline { { M } } _ { 0 }$ isassumed to be invertible.Equation （2.12）then yields $\boldsymbol { u } = ( u _ { 1 } , \ldots , u _ { d } ) ^ { T } .$ Finally,(2.15） determines $\chi _ { 1 } , \ldots , \chi _ { d }$ ,and the construction of $\chi ( b , \varphi )$ iscomplete.In the new variables $( b , \varphi )$ ,theperturbed Hamiltonian then takes the form

$$
\begin{array} { r } { H ( a , \theta ) + \varepsilon G ( a , \theta ) = \widehat { c } + \omega \cdot b + \frac { 1 } { 2 } b ^ { T } \widehat { M } ( b , \varphi ) b + \varepsilon ^ { 2 } \widehat { G } ( b , \varphi ) } \end{array}
$$

with unchanged frequencies $\omega$ and with $\widehat { M } ( b , \varphi ) = M ( b , \varphi ) + { \mathcal O } ( { \varepsilon } ) .$ Theperturbation to the form (2.8) isthus reduced from $O ( \varepsilon )$ to $\mathcal { O } ( \varepsilon ^ { 2 } )$ The iteration of this procedure turns outto be convergent,see Sect.X.5.This finally yieldsasymplectic change of coordinates that transforms theperturbed Hamiltonian to the form (2.8). The perturbed system thus has an invariant torus carryingaquasi-periodic flow with frequencies $\omega - \mathrm { a }$ KAMtorus,asitisnamedafterKolmogorov,ArnoldandMoser.

# X.2.4Birkhoff Normalization Near an Invariant Torus

KAM tori are very sticky. (A.D.Perry&S.Wiggins1994)

In this subsection we describe a transformation studied by Poschel(1993)and Perry &Wiggins(1994)forsystemswith Hamiltonian in theKolmogorov form(2.8) ina neighbourhood of the invariant torus $\{ a = 0 , \ \theta \in \mathbb { T } ^ { d } \}$ This transformation isan analogue ofa transformation of Birkhoff(1927)for Hamiltoniansystems nearan elliptic stationary point.

The symplectic change of coordinates $( a , \theta ) \mapsto ( b , \varphi )$ considered here transformsa Hamiltonian (2.8）with diophantine frequencies $\omega$ tothe form $H ( a , \theta ) =$ $K _ { N } ( b ) + \mathcal { O } ( \lVert b \rVert ^ { N } )$ forarbitrary $N$ ,ormoreprecisely,theHamiltonianin the new variables, $H _ { N } ( b , \varphi ) = H ( a , \theta )$ ,isoftheform

$$
H _ { N } ( b , \varphi ) = \omega \cdot b + Z _ { N } ( b ) + R _ { N } ( b , \varphi )
$$

with $Z _ { N } ( b ) = \mathcal { O } ( \| b \| ^ { 2 } )$ and $R _ { N } ( b , \varphi ) = \mathcal { O } ( \| b \| ^ { N } )$ (Wehave taken the irrelevant constant term in (2.8） $c = 0$ .）Theequations of motion then take the form

$$
\dot { b } = \mathcal { O } ( \lVert b \rVert ^ { N } ) , \quad \dot { \varphi } = \omega + \mathcal { O } ( \lVert b \rVert ) .
$$

Therefore,in these variables $\{ b = 0 , \varphi \in \mathbb { T } ^ { d } \}$ is an invariant torus,and for sufficientlysmall $r$ ,

$$
\| b ( 0 ) \| \le r \quad \mathrm { ~ i m p l i e s ~ } \quad \| b ( t ) \| \le 2 r \mathrm { ~ f o r ~ } t \le C _ { N } r ^ { - N + 1 } .
$$

A judicious choice of $N$ evenyields time intervals that are exponentially long ina negative power of $_ { r }$ on which solutions starting at a distance $_ { r }$ stay within twice the initialdistance(Perry&Wiggins1994).Motionaway fromthe toruscan thusbe onlyveryslow.

Thenormal form(2.18)isconstructed iteratively.Each iterationstepis very similar to the procedurein Sect.X.2.1,where now the distance to the torus plays the roleof the small parameter.Considera Hamiltonian

$$
H ( a , \theta ) = \omega \cdot a + Z ( a ) + R ( a , \theta )
$$

where $Z ( a ) ~ = ~ { \cal O } ( | | a | | ^ { 2 } )$ and $R ( a , \theta ) \ = \ \mathcal { O } ( \| a \| ^ { k } )$ forsome $k \geq 2$ in acomplex neighbourhood of $\{ 0 \} \times  { \mathbb { T } } ^ { d }$ Weconstruct a symplecticchange of coordinates $( a , \theta ) \mapsto ( b , \varphi )$ viaagenerating function $b \cdot \theta + S ( b , \theta )$ as

$$
a = b + { \frac { \partial S } { \partial \theta } } ( b , \theta ) , \quad \varphi = \theta + { \frac { \partial S } { \partial b } } ( b , \theta ) .
$$

Weexpand (omiting the arguments $( 6 , \theta )$ in $\partial S / \partial \theta$ and $\partial H / \partial a$ ）

$$
\begin{array} { r c l } { { H \Big ( b + \displaystyle \frac { \partial S } { \partial \theta } , \theta \Big ) } } & { { = } } & { { H ( b , \theta ) + \displaystyle \frac { \partial H } { \partial a } \cdot \displaystyle \frac { \partial S } { \partial \theta } + { \cal Q } ( b , \theta ) } } \\ { { } } & { { = } } & { { \displaystyle \omega \cdot b + { \cal Z } ( b ) + \left\{ R ( b , \theta ) + \displaystyle \frac { \partial H } { \partial a } \cdot \displaystyle \frac { \partial S } { \partial \theta } \right\} + { \cal Q } ( b , \theta ) , } } \end{array}
$$

where $| Q ( b , \theta ) | \leq$ Const. $\| \partial S / \partial \theta \| ^ { 2 }$ Since $\partial H / \partial b = \omega + \mathcal { O } ( \Vert b \Vert )$ ,we can make theexpression incurly brackets independent of $\theta$ upto $O ( \left| \left| b \right| \right| ^ { k + 1 } )$ bydetermining $S$ from the equation of the form (2.2):

$$
\omega \cdot \frac { \partial S } { \partial \theta } ( b , \theta ) + R ( b , \theta ) = \overline { { { R } } } ( b ) .
$$

For diophantine frequencies $\boldsymbol { \omega }$ ,weobtain $S ( \boldsymbol { b } , \boldsymbol { \theta } ) = \mathcal { O } ( \| \boldsymbol { b } \| ^ { k } )$ ona (reduced） complex neighbourhood of $\{ 0 \} \times  { \mathbb { T } } ^ { d }$ from the corresponding estimate for $R ( b , \theta ) .$ It follows that the above symplectic transformation with generating function $\boldsymbol { b } \cdot \boldsymbol { \theta } + \boldsymbol { S } ( \boldsymbol { b } , \boldsymbol { \theta } )$ is well-defined for small $\| \boldsymbol { b } \|$ ,and the Hamiltonian inthe newvariables, ${ \widehat { H } } ( b , \varphi ) =$ $H ( a , \theta )$ ,becomes

$$
\widehat { H } ( b , \varphi ) = \omega \cdot b + \widehat { Z } ( b ) + \widehat { R } ( b , \varphi )
$$

with $\widehat Z ( b ) = Z ( b ) + \overline { { R } } ( b )$ and

$$
\widehat { R } ( b , \varphi ) = \Big ( \frac { \partial H } { \partial a } ( b , \theta ) - \omega \Big ) \cdot \frac { \partial S } { \partial \theta } ( b , \theta ) + Q ( b , \theta ) = \mathcal { O } ( \| b \| ^ { k + 1 } ) ,
$$

so that the order in $b$ oftheremainder term isaugmented by1.The procedure can beiterated,but unlikethe iteration of the preceding subsection,this iteration is in general divergent.Nevertheless,a suitable finite terminationyieldsremainder terms that areexponentially small inapositive power of $r$ for $\left\| \ b \right\| \leq r ,$ byarguments similarto those of Sect.X.4.

# X.3Linear Error Growth and Near-Preservation of First Integrals

Intheremaining part of thischapterwe study the long-time behaviour of symplectic discretizations of integrableand near-integrable Hamiltonian systems.Whilehere wewill beconcerned with general symplectic methods,it should be noted that some integrableproblemsadmit integrable discretizations;see Suris(2003).

Inthis section we are concerned with the error growth of symplectic numerical methodsand their approximatepreservation of first integrals.Apreliminary analysis oflinear error growth for the Keplerproblemwas first given byCalvo&Sanz-Serna （1993).Using backwarderroranalysisandKAM theory,Calvo&Hairer（1995a) thenshowed linear error growth of symplectic methods applied tointegrable systemswhen the frequencies at the initial value satisfy a diophantine condition(2.4). Here we give such a result under milder conditions on the initial values,combining backward error analysis and Lemma 2.1.We derive alsoa first result on the longtimenear-preservation of all first integrals,which will be extended to exponentially long times in Sections X.4.3andX.5.2（under stronger assumptions on the starting values),and perpetually in Sect.X.6(only fora Cantor set of step sizes).

Figure3.1 illustrates the linear error growth of the symplectic Stormer-Verlet method,as opposed to the quadratic error growth for the classical fourth-order Runge-Kutta method,on the example of the Toda latice.The samenumber of function evaluations wasused for both methods.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/7e367fd3bbe31575f5d9359171039fd3a0194089db3db1150b88b51a91005f90.jpg)  
Fig.3.1.Euclidean norm of the global error for the Stormer-Verlet scheme(stepsize $h =$ 0.02)and the classical Runge-Kutta method of order 4（step size $h = 0 . 0 8$ appliedtothe Toda lattice with $n = 3$ and initial values as in Fig.1.3

Weconsider a completely integrable Hamiltonian system (usually not given in action-anglevariables)

$$
\dot { p } = - \frac { \partial H } { \partial q } ( p , q ) , \dot { q } = \frac { \partial H } { \partial p } ( p , q )
$$

andapplyto itasymplectic numerical method with step size $h$ ,yieldinganumerical solution sequence $( p _ { n } , q _ { n } )$ Weassumethat theHamiltonianisreal-analyticand that theconditions of theArnold-Liouville theorem,Theorem1.6,arefulfilled.Consider thesymplectic transformation $( p , q ) = \psi ( a , \theta )$ toaction-angle variables.We denote theinverse transformationas

$$
( a , \theta ) = \left( I ( p , q ) , \theta ( p , q ) \right) ,
$$

Werecall that the components $I _ { 1 } , \ldots , I _ { d }$ of $I = ( I _ { i } )$ are first integrals ofthe system: $I ( p ( t ) , q ( t ) ) = I ( p _ { 0 } , q _ { 0 } )$ for all $t .$ In theaction-angle variables,the Hamiltonian is $\mathcal { H } ( \boldsymbol { a } ) = H ( p , q )$ ,andwe denote the frequencies

$$
\omega ( a ) = { \frac { \partial { \mathcal { H } } } { \partial a } } ( a ) .
$$

We consider thisin a neighbourhood of some $\boldsymbol { a } ^ { * } \in \mathbb { R } ^ { d }$

Theorem3.1.Consider applyinga symplectic numerical integrator oforder $p$ to thecompletely integrable Hamiltonian system(3.1).Suppose that $\omega ( a ^ { * } )$ satisfies thediophantine condition (2.4).Then,there exist positive constants $C , c$ and $h _ { 0 }$ suchthat thefollowing holds forall step sizes $h \leq h _ { 0 }$ :everynumerical solution startingwith $\| I ( p _ { 0 } , q _ { 0 } ) - a ^ { * } \| \leq c | \log h | ^ { - \nu - 1 }$ satisfies

$$
\begin{array} { r l r } & { \| ( p _ { n } , q _ { n } ) - ( p ( t ) , q ( t ) ) \| \ \leq C t h ^ { p } } & { \mathrm { \it ~ f o r ~ t = n h \leq h ^ { - p } ~ } . } \\ & { \| I ( p _ { n } , q _ { n } ) - I ( p _ { 0 } , q _ { 0 } ) \| \ \leq C h ^ { p } } & \end{array}
$$

Theconstants $h _ { 0 } , c , C$ dependon $d , \gamma , \nu$ ,onboundsofthereal-analytic Hamiltonian $H$ onacomplex neighbourhood of thetorus $\{ ( p , q ) ; I ( p , q ) = a ^ { * } \} ,$ and on the numericalmethod.

Proof.(a)In theaction-anglevariables $( a , \theta )$ ,the exactflowis given as

$$
a ( t ) = a ( 0 ) , \quad \theta ( t ) = \omega ( a ( 0 ) ) t + \theta ( 0 ) .
$$

ByTheorem IX.3.1 (and Theorem IX.1.2),the truncated modified equationof the numerical method is Hamiltonian withl

$$
\widetilde H ( p , q ) = H ( p , q ) + h ^ { p } H _ { p + 1 } ( p , q ) + \ldots + h ^ { r } H _ { { \bar { r } } + 1 } ( p , q ) .
$$

Wechoose $r = 2 p$ ,andwe denote by $( \widetilde { p } ( t ) , \widetilde { q } ( t ) )$ the solution of the modified equationswith initial values $( p _ { 0 } , q _ { 0 } )$ Inthevariables $( a , \theta )$ ,themodified Hamiltonian becomes $\tilde { H } ( p , q ) = \mathcal { \mathcal { H } } ( a , \theta )$ with

$$
\begin{array} { r } { \mathcal { \widetilde { H } } ( a , \theta ) = \mathcal { H } ( a ) + \varepsilon \mathcal { G } _ { h } ( a , \theta ) , } \end{array}
$$

where $\varepsilon = h ^ { p }$ and the perturbation function $\mathcal { G } _ { h }$ is bounded independentlyof $h$ on a complex neighbourhood of $\{ a ^ { * } \} \times \mathbb { T } ^ { d }$ ByLemma2.1with $\varepsilon = h ^ { p }$ and $N \geq 3$ , there isasymplectic change of coordinates $\mathcal { O } ( h ^ { p } )$ -closeto theidentity,such that the solution of the modified equation in the new variables $( b , \varphi )$ is of the form

$$
\begin{array} { r l r } & { \widetilde b ( t ) = \widetilde b ( 0 ) + \mathcal O ( t h ^ { p N } ) , } & \\ & { \widetilde \varphi ( t ) = \omega _ { h } \widetilde ( b ( 0 ) ) t + \widetilde \varphi ( 0 ) + \mathcal O ( t h ^ { p N - 1 } + t ^ { 2 } h ^ { p N } ) } & { \quad \mathrm { f o r ~ } t \leq h ^ { - p } , } \end{array}
$$

with $\omega _ { h } ( b ) = \omega ( b ) + \mathcal { O } ( h ^ { p } ) .$ Theconstants symbolized by the $\mathcal { O }$ -notationare independent of $h$ ,of $t \leq h ^ { - p }$ andof $( b ( 0 ) , \widetilde { \varphi } ( 0 ) )$ with $| \tilde { b } ( 0 ) - a ^ { * } | \leq c | \log h | ^ { - \nu - 1 }$ Since the transformation between the variables $( a , \theta )$ and $( b , \varphi )$ is $\mathcal { O } ( h ^ { p } )$ close to theidentity,it follows that theflow of the modified equations in the variables $( a , \theta )$ satisfies

$$
\begin{array} { r l r } & { \widetilde { a } ( t ) = \widetilde { a } ( 0 ) + { \mathcal O } ( h ^ { p } ) , } & { \quad \mathrm { f o r ~ } 1 \leq t \leq h ^ { - p } , } \\ & { \widetilde { \theta } ( t ) = \omega ( \widetilde { a } ( 0 ) ) t + \widetilde { \theta } ( 0 ) + t e _ { h } + { \mathcal O } ( h ^ { p } ) } & { \quad \mathrm { f o r ~ } 1 \leq t \leq h ^ { - p } , } \end{array}
$$

where $e _ { h } = \omega _ { h } ( b ( 0 ) ) - \omega ( \widetilde { a } ( 0 ) ) = \mathcal { O } ( h ^ { p } )$ yields the dominant contribution to the error.Bycomparisonwith(3.4） and since $\tilde { a } ( t ) = I ( \tilde { p } ( t ) , \tilde { q } ( t ) )$ ,thedifference between the exact solution and the solution of the modified equation therefore satisfies

$$
\begin{array} { r l r } & { ( \widetilde { p } ( t ) , \widetilde { q } ( t ) ) - ( p ( t ) , q ( t ) ) = { \mathcal O } ( t h ^ { p } ) } & \\ & { I ( \widetilde { p } ( t ) , \widetilde { q } ( t ) ) - I ( p _ { 0 } , q _ { 0 } ) = { \mathcal O } ( h ^ { p } ) } & \end{array} \quad \mathrm { f o r ~ } 1 \leq t \leq h ^ { - p } .
$$

The same bounds for $t \leq 1$ follow by standard error estimates.

(b)Itremainsto bound the difference between the solution of the modified equation and the numerical solution.By construction of the modified equation with $r = 2 p$ andby comparisonwith (3.6),one step of the method is of the form

$$
b _ { n + 1 } = b _ { n } + \mathcal { O } ( h ^ { r + 1 } ) , \quad \varphi _ { n + 1 } = \omega _ { h } ( b _ { n } ) h + \varphi _ { n } + \mathcal { O } ( h ^ { r + 1 } ) .
$$

It follows that for $t = n h$ ,

$$
b _ { n } = \widetilde { b } ( t ) + \mathcal { O } ( t h ^ { r } ) , \quad \varphi _ { n } = \widetilde { \varphi } ( t ) + \mathcal { O } ( t ^ { 2 } h ^ { r } ) .
$$

For $t \leq h ^ { - p }$ and $r = 2 p$ ,wehave $t h ^ { r } \leq h ^ { p }$ .Hence the difference between the numerical solutionand the solution of the modified equationsin the original variables $( p , q )$ is bounded by

$$
\begin{array} { r l r l } & { ( p _ { n } , q _ { n } ) = ( \widetilde p ( t ) , \widetilde q ( t ) ) = { \mathcal O } ( t h ^ { p } ) } & & { \mathrm { f o r ~ } t = n h \le h ^ { - p } , } \\ & { I ( p _ { n } , q _ { n } ) - I ( \widetilde p ( t ) , \widetilde q ( t ) ) = { \mathcal O } ( h ^ { p } ) } \end{array}
$$

Together with the bound of part (a) this gives the result.

Remark 3.2.Thelinear error growth holdsalsowhen the symplectic method is appliedtoaperturbed integrable systemwithaperturbation parameter $\varepsilon$ bounded bya positive power of the step size: $\varepsilon \le K h ^ { \alpha }$ forsome $\alpha > 0$ Theproof of this generalization isthe sameasabove,except that possiblya larger $N$ isrequired in usingLemma 2.1.

Example3.3(Linear Error Growth forthe Kepler Problem).From Example1.10weknow that for the Kepler problem the frequencies(1.16) do not satisfythediophantinecondition(2.4).Neverthelesswe observedalinear errorgrowth forsymplectic methodsin the experimentsof Fig.I.2.3(seealso Table I.2.1).This canbe explained as follows:in action-angle variables the Hamiltonian of the Keplerproblemis $\mathcal { H } ( a _ { 1 } , a _ { 2 } )$ ,where $a _ { 2 } ~ = ~ L$ isthe angular momentum.Since the angularmomentum isa quadratic invariant that is exactly conserved by symplecticintegrators such as symplectic partitioned Runge-Kutta methods,the modified Hamiltonian

$$
\begin{array} { r } { \mathcal { \widetilde { H } } ( a , \theta ) = \mathcal { H } ( a _ { 1 } , a _ { 2 } ) + \varepsilon \mathcal { G } _ { h } ( a _ { 1 } , a _ { 2 } , \theta _ { 1 } ) } \end{array}
$$

doesnot depend on the angle variable $\theta _ { 2 }$ (seeCorollary IX.5.3).Asin theproof of Lemma 2.1we average out the angle $\theta _ { 1 }$ up to a certain power of $\succeq$ Since we are concerned here with one degree of freedom,the diophantine condition is trivially satisfied,and we can conclude as in Theorem 3.1.

# X.4 Near-Invariant Tori on Exponentially Long Times

Werefine theresults for the classical perturbation series of Sect.X.2.2 to yield locallyintegrable behaviour,uptoexponentiallysmall deviations,over time intervals thatare exponentially long ina power of the small perturbationparameter.We then combine thisresult with backward error analysis to show the near-preservation of invariant tori over exponentially long times ina negative power of the step size for symplectic integrators.We begin with the necessary technical estimates.

# X.4.1Estimates of Perturbation Series

Wewill estimate the coefcients of theperturbation series (2.5),which requires a bound for the solution of (2.6).We use the following notation: for $\rho > 0$ andwith $\| \cdot \|$ themaximum normon $\mathbb { R } ^ { d }$ ,

$$
U _ { \rho } = \{ \theta \in \mathbb { T } ^ { d } + i \mathbb { R } ^ { d } \ ; \ \| \mathrm { I m } \theta \| < \rho \}
$$

denotes the complex extension of the $d$ -dimensional torus $\mathbb { T } ^ { d }$ of width $\rho$ Fora bounded analytic function $F$ on $U _ { \rho }$ ,wewrite

$$
\| F \| _ { \rho } = \operatorname* { s u p } _ { \theta \in U _ { \rho } } \left| F ( \theta ) \right| , \quad \left\| \frac { \partial F } { \partial \theta } \right\| _ { \rho } = \sum _ { j = 1 } ^ { d } \Bigl \| \frac { \partial F } { \partial \theta _ { j } } \Bigr \| _ { \rho } .
$$

Following Arnold (1963),we prove the following bounds for the solution of the basic partial differential equation（2.2）.

Lemma 4.1. Suppose $\omega \in \mathbb { R } ^ { d }$ satisfies thediophantine condition(2.4).Let $G$ be $a$ boundedreal-analytic functionon $U _ { \rho }$ andlet $\overline { { G } }$ denote the averageof $G$ over $\mathbb { T } ^ { d }$ . Then,the equation

$$
\omega \cdot { \frac { \partial F } { \partial \theta } } + G = { \overline { { G } } }
$$

hasauniquereal-analyticsolution $F$ on $U _ { \rho }$ with zero average $\overline { { F } } = 0$ Forevery positive $\delta < \operatorname* { m i n } ( \rho , 1 )$ ， $F ^ { \prime }$ isbounded on $U _ { \rho - \bar { \delta } }$ by

$$
\| F \| _ { \rho - \delta } \leq \kappa _ { 0 } \delta ^ { - \alpha + 1 } \| G \| _ { \rho } , \quad \quad \left\| \frac { \partial F } { \partial \theta } \right\| _ { \rho - \delta } \leq \kappa _ { 1 } \delta ^ { - \alpha } \| G \| _ { \rho } ,
$$

Russmann(1975,1976) has shown that the estimates hold with the optimal exponent $\alpha = \nu + 1$ andwith $\kappa _ { 0 } = 2 ^ { d + 1 - \nu } { \sqrt { ( 2 \nu ) ! } }$ and $\kappa _ { 1 } = 2 ^ { d - \nu } \sqrt { ( 2 \nu + 2 ) ! } .$ This optimal value of $\alpha$ would yield slightlymore favourable estimates inthe following, but here we content ourselves with the simpler result given above.

ProofofLemma 4.1.We have the Fourier series,convergent on the complex extension $\| \operatorname { I m } \theta \| < \rho$ ,

$$
G ( \theta ) - \overline { { { G } } } = \sum _ { k \neq 0 } g _ { k } e ^ { i k \cdot \theta } , F ( \theta ) = \sum _ { k } f _ { k } e ^ { i k \cdot \theta }
$$

with Fourier coefficients $f _ { 0 } = F = 0$ and

$$
f _ { k } = - \frac { g _ { k } } { i k \cdot \omega } \mathrm { f o r } k \in \mathbb { Z } ^ { d } , k \neq 0 .
$$

By Cauchy’s estimates, $| g _ { k } | \le M e ^ { - | k | \rho }$ with $M = \| G - { \overline { { G } } } \| _ { \rho } \leq 2 \| G \| _ { \rho }$ and $\begin{array} { r } { | k | = \sum | k _ { i } | . } \end{array}$ It follows with (2.4) that

$$
\begin{array} { r c l } { \displaystyle \| F \| _ { \rho - \delta } } & { \le } & { \displaystyle \sum _ { k } | f _ { k } | e ^ { | k | ( \rho - \delta ) } \le \frac { M } { \gamma } \sum _ { k } | k | ^ { \nu } e ^ { - | k | \delta } , } \\ { \displaystyle \left\| \frac { \partial F } { \partial \theta } \right\| _ { \rho - \delta } } & { \le } & { \displaystyle \sum _ { k } | f _ { k } | \cdot | k | e ^ { | k | ( \rho - \delta ) } \le \frac { M } { \gamma } \sum _ { k } | k | ^ { \nu + 1 } e ^ { - | k | \delta } , } \end{array}
$$

Itremains to bound the right-hand sums.We use the inequality $x ^ { \nu } / \nu ! \leq e ^ { x }$ with $x = | k | \delta / 2$ toobtain

$$
\sum _ { k } | k | ^ { \nu } e ^ { - | k | \delta } \leq 2 ^ { \nu } \delta ^ { - \nu } \nu ! \sum _ { k } e ^ { - | k | \delta / 2 } .
$$

The last sum is bounded by

$$
\sum _ { k } e ^ { - | k | \delta / 2 } = \left( 1 + 2 \sum _ { j = 1 } ^ { \infty } e ^ { - j \delta / 2 } \right) ^ { d } = \left( { \frac { 1 + e ^ { - \delta / 2 } } { 1 - e ^ { - \delta / 2 } } } \right) ^ { d } \leq ( 8 \delta ^ { - 1 } ) ^ { d } .
$$

Takentogether,theabove inequalities yield the stated bound for $\| F \| _ { \rho - \delta } .$ Thebound for the derivative is obtained in the sameway,with $\nu$ replacedby $\nu + 1$ , □

The coefficients of the perturbation series (2.5)are bounded as follows.

Lemma 4.2.Let $H _ { 0 }$ ， $H _ { 1 }$ bereal-analyticand bounded by $M$ on the complex $r$ -- neighbourhood $B _ { r } ( b ^ { * } )$ of $b ^ { \ast } \in \mathbb { R } ^ { d }$ andon $B _ { r } ( b ^ { * } ) \times U _ { \rho }$ ,respectively.Suppose that $\omega ( b ^ { * } ) = ( \partial H _ { 0 } / \partial a ) ( b ^ { * } )$ satisfiesthe diophantine condition (2.4).Then,the coefficientsoftheperturbation series(2.5)arebounded by

$$
\left\| \frac { \partial S _ { j } } { \partial \theta } ( b ^ { * } , \cdot ) \right\| _ { \rho / 2 } \leq C _ { 0 } ( C _ { 1 } j ^ { \alpha } ) ^ { j - 1 }
$$

forall $j ~ \geq ~ 0$ Here $C _ { 0 } ~ = ~ 2 r$ and $C _ { 1 } \ = \ 1 2 8 ( \kappa _ { 1 } M / r \rho ^ { \alpha } ) ^ { ; 2 }$ with $\alpha$ and $\kappa _ { 1 }$ of Lemma4.1.

Proof.Werecall from Sect.X.2.2 that $S _ { j }$ isdetermined by(2.6),where $K _ { 1 } = H _ { 1 }$ and for $j \geq 2$ ,

$$
\begin{array} { r c l } { { \displaystyle K _ { j } } } & { { = } } & { { \displaystyle \sum _ { i = 2 } ^ { j } \sum _ { k _ { 1 } + \ldots + k _ { i } = j } \frac { 1 } { i ! } \frac { \partial ^ { i } H _ { 0 } } { \partial a ^ { i } } \left( \frac { \partial S _ { k _ { 1 } } } { \partial \theta } , \ldots , \frac { \partial S _ { k _ { i } } } { \partial \theta } \right) } } \\ { { } } & { { } } & { { \displaystyle + \sum _ { i = 1 } ^ { j - 1 } \sum _ { k _ { 1 } + \ldots + k _ { i } = j - 1 } \frac { 1 } { i ! } \frac { \partial ^ { i } H _ { 1 } } { \partial a ^ { i } } \left( \frac { \partial S _ { k _ { 1 } } } { \partial \theta } , \ldots , \frac { \partial S _ { k _ { i } } } { \partial \theta } \right) . } } \end{array}
$$

Wefix an index,say $J$ ,set $\delta = \rho / ( 2 J )$ andabbreviate

$$
\| K _ { k } \| _ { j } = \| K _ { k } ( b ^ { * } , \cdot ) \| _ { \rho - j \delta }
$$

and similarly for $\partial S _ { k } / \partial \theta .$ By(2.6)andLemma4.1,we have

$$
\Bigl \| \frac { \partial S _ { j } } { \partial \theta } \Bigr \| _ { j } \le \kappa _ { 1 } \delta ^ { - \alpha } \| K _ { j } \| _ { j - 1 } .
$$

We use the Cauchy estimate

$$
\Big | \frac { 1 } { i ! } \frac { \partial ^ { i } H _ { 0 } } { \partial a ^ { i } } ( v _ { 1 } , \dots , v _ { i } ) \Big | \leq \frac { M } { r ^ { i } } \left| v _ { 1 } \right| \cdot \dots \cdot \left| v _ { i } \right| ,
$$

where $| \cdot |$ denotes the sum norm on $\mathbb { C } ^ { d }$ ,andbound $| | \cdot | | _ { j - 1 }$ by $| | \cdot | | _ { k }$ for $k \le j - 1$ We thus obtain from theabove formula for $K _ { j }$

$$
\begin{array} { r c l } { \| K _ { j } \| _ { j - 1 } } & { \le } & { \displaystyle \sum _ { i = 2 } ^ { j } \displaystyle \sum _ { k _ { 1 } + \ldots + k _ { i } = j } \frac { M } { r ^ { i } } \left\| \frac { \partial S _ { k _ { 1 } } } { \partial \theta } \right\| _ { k _ { 1 } } , \ldots \times \left\| \frac { \partial S _ { k _ { i } } } { \partial \theta } \right\| _ { k _ { i } } } \\ & & { \displaystyle + \sum _ { i = 1 } ^ { j - 1 } \displaystyle \sum _ { k _ { 1 } + \ldots + k _ { i } = j - 1 } \frac { M } { r ^ { i } } \left\| \frac { \partial S _ { k _ { 1 } } } { \partial \theta } \right\| _ { k _ { 1 } } , \ldots \times \left\| \frac { \partial S _ { k _ { i } } } { \partial \theta } \right\| _ { k _ { i } } . } \end{array}
$$

Combining the two bounds yields

$$
\frac { 1 } { r } \left\| \frac { \partial S _ { j } } { \partial \theta } \right\| _ { j } \leq \beta _ { j } ,
$$

where,with $\mu = ( M / r ) ( \kappa _ { 1 } / \delta ^ { \alpha } )$ ,wehave $\beta _ { 1 } = \mu$ and recursively for $j \geq 2$ ,

$$
\beta _ { j } = \mu \sum _ { i = 2 } ^ { j } \sum _ { k _ { 1 } + \ldots + k _ { i } = j } \beta _ { k _ { 1 } } \cdot \ldots \cdot \beta _ { k _ { i } } + \mu \sum _ { i = 1 } ^ { j - 1 } \sum _ { k _ { 1 } + \ldots + k _ { i } = j - 1 } \beta _ { k _ { 1 } } \cdot \ldots \cdot \beta _ { k _ { i } } .
$$

Multiplying this equation with $\zeta ^ { \mathcal { I } }$ and summing over $j$ ,we see that the generating function $\begin{array} { r } { b ( \zeta ) = \sum _ { j = 1 } ^ { \infty } \beta _ { j } \zeta ^ { j } } \end{array}$ is given implicitlyby

$$
b ( \zeta ) = \mu \zeta = \mu \left( \frac { 1 } { 1 - b ( \zeta ) } - 1 - b ( \zeta ) \right) + \mu \zeta \left( \frac { 1 } { 1 - b ( \zeta ) } - 1 \right) ,
$$

or explicitly,ftersolvingthequadraticequation,by

$$
b ( \zeta ) = \frac { 1 } { 2 } \frac { 1 } { 1 + \mu } - \sqrt { \frac { 1 } { 4 } \Big ( \frac { 1 } { 1 + \mu } \Big ) ^ { 2 } - \frac { \mu } { 1 + \mu } \zeta } .
$$

Hence, $b ( \zeta )$ is analytic on the disc $| \varsigma | < 1 / ( 4 \mu ( 1 + \mu ) )$ ,and is there bounded by $1 / ( 2 ( 1 + \mu ) )$ For $\mu \geq 1$ ,Cauchy'sestimateyields

$$
\begin{array} { r } { \| \partial S _ { j } / \partial \theta \| _ { j } \leq r \beta _ { j } \leq 2 r ( 8 \mu ^ { 2 } ) ^ { j - 1 } . } \end{array}
$$

(For the uninteresting case $\mu \leq 1$ thebound is $2 r \cdot 8 ^ { \jmath - 1 }$ ）For $j = J$ thisalmost gives the stated result upon inserting thedefinition of $\mu$ ,but with an exponent $2 \alpha$ instead of $\alpha$ Thiscan bereduced to $\alpha$ if in the above proof $\delta$ ischosenas $\delta _ { 1 } = \rho / 4$ inthe first step and in the other steps as $\delta _ { j } = \rho / ( 4 J )$ Thisleadstoamorecomplicated quadratic equation where now $b ( \zeta )$ isanalytic for $| \zeta | \le ( C _ { 1 } J ^ { \alpha } ) ^ { - 1 }$ Weomit the details of this refinement of the proof. □

For the remainder term in (2.7） we then obtain the following bound.

Lemma4.3.InthesituationofLemma4.2,with $r \leq 1$ andfor $C _ { 1 } N ^ { \alpha } \leq 1 / ( 2 \varepsilon ) ,$

$$
\| R _ { N } ( b ^ { * } , \cdot ) \| _ { \rho / 2 } \leq 4 M r \Bigl ( \frac { 4 C _ { 1 } } { r } N ^ { \alpha } \Bigr ) ^ { N } .
$$

Proof.Theremainder term $R _ { N }$ in（2.7）isa sum of terms

$$
\frac { 1 } { i ! } \frac { \partial ^ { i } H _ { k _ { 0 } } } { \partial a ^ { i } } \left( Q _ { k _ { 1 } } , . . . , Q _ { k _ { i } } \right) \quad \mathrm { f o r } \ k _ { 0 } + k _ { 1 } + . . . + k _ { i } = N ,
$$

where

$$
{ \cal Q } _ { k } = \frac { \partial S _ { k } } { \partial \theta } + \varepsilon \frac { \partial S _ { k + 1 } } { \partial \theta } + \ldots + \varepsilon ^ { N - k - 1 } \frac { \partial S _ { N - 1 } } { \partial \theta } .
$$

As long as $C _ { 1 } N ^ { \alpha } \leq 1 / ( 2 \varepsilon )$ ,wehave,byLemma4.2,

$$
\begin{array} { r l r } {  { \| Q _ { k } ( b ^ { * } , \cdot ) \| _ { \rho / 2 } \le \sum _ { j = k } ^ { N - 1 } \varepsilon ^ { ( j - k ) } C _ { 0 } ( C _ { 1 } j ^ { \alpha } ) ^ { j } } } \\ & { \le } & { C _ { 0 } \displaystyle \sum _ { j = k } ^ { N - 1 } 2 ^ { - ( j - k ) } \Big ( \frac { j } { N } \Big ) ^ { \alpha j } ( C _ { 1 } N ^ { \alpha } ) ^ { k } \le 2 C _ { 0 } ( C _ { 1 } N ^ { \alpha } ) ^ { k } . } \end{array}
$$

This implies

$$
\left\| \frac { 1 } { i ! } \frac { \partial ^ { i } H _ { k _ { 0 } } } { \partial a ^ { i } } \left( Q _ { k _ { 1 } } , \ldots , Q _ { k _ { i } } \right) ( b ^ { * } , \cdot ) \right\| _ { \rho / 2 } \leq \frac { M } { r ^ { i } } 2 C _ { 0 } ( C _ { 1 } N ^ { \bar { \alpha } } ) ^ { N }
$$

for $k _ { 0 } + k _ { 1 } + \ldots + k _ { i } = N$ (Thisboundisalso validwhenanargument different from $b ^ { * }$ appears in the derivatives of $H _ { 0 }$ and $H _ { 1 }$ ,asisneeded for the remainder termsin the Taylor expansion.) Estimating the number of such expressions by

$$
2 \sum _ { i = 1 } ^ { N } { \binom { N + i - 1 } { i } } \leq 2 \sum _ { i = 0 } ^ { 2 N - 1 } { \binom { 2 N - 1 } { i } } = 2 ^ { 2 N }
$$

yields theresult.

# X.4.2Near-Invariant Tori of Perturbed Integrable Systems

The following result extends Lemma2.1 to exponentially long times for sufficiently small values of the perturbation parameter.

Theorem4.4.Let $H _ { 0 }$ , $H _ { 1 }$ bereal-analyticonthecomplex $r$ -neighbourhood $B _ { r } ( b ^ { * } )$ of $b ^ { * } \in \mathbb { R } ^ { d }$ andon $B _ { r } ( b ^ { * } ) \times U _ { \rho }$ ,respectively,with $r \leq 1$ and $\rho \leq 1$ Suppose that $\omega ( b ^ { * } ) = ( \partial H _ { 0 } / \partial a ) ( b ^ { * } )$ satisfiesthediophantinecondition(2.4).Therearepositive constants $\varepsilon _ { 0 }$ , $c _ { 0 }$ , $C$ suchthat thefollowing holds forevery positive $\beta \leq 1$ andfor $\varepsilon \le \varepsilon _ { 0 }$ :thereexistsareal-analytic symplecticchangeofcoordinates $( a , \theta ) \mapsto ( b , \varphi )$ such that every solution $( b ( t ) , \varphi ( t ) )$ oftheperturbed systeminthenew coordinates, startingwith $\| b ( 0 ) - b ^ { * } \| \leq c _ { 0 } \varepsilon ^ { 2 \beta }$ satisfies

$$
\begin{array} { r } { \| b ( t ) - b ( 0 ) \| \le C t \exp ( - c  { \varepsilon } ^ { - \beta / \alpha } ) \quad f o r \quad t \le \exp ( \frac { 1 } { 2 } c  { \varepsilon } ^ { - \beta / \alpha } ) . } \end{array}
$$

Here, $\alpha = \nu + d + 1$ and $c = ( 1 6 C _ { 1 } e / r ) ^ { - 1 / \alpha }$ with $C _ { 1 }$ ofLemma4.2.Moreover, thetransformationissuch that $f o r \left( a , \theta \right)$ and $( 6 , \varphi )$ relatedbytheabovecoordinate transform,

$$
\| a - b \| \leq C \varepsilon \quad f o r \quad \| b - b ^ { * } \| \leq c _ { 0 } \varepsilon ^ { 2 \beta } , \varphi \in U _ { \rho / 2 } ,
$$

The thresholds $\xi _ { 0 }$ and $c _ { 0 }$ are such that $\varepsilon _ { 0 } ^ { 2 , 3 }$ isinversely proportional to $\gamma C _ { 1 } ^ { 2 }$ and $c _ { 0 }$ is proportional to $\gamma C _ { 1 } ^ { 2 }$

Remark4.5.Theorem4.4isa local result,showing that for $b _ { 0 }$ near $b ^ { * }$ thetori $\{ b = b _ { 0 } , \ \varphi \in \mathbb { T } ^ { d } \}$ arenearly invariant,up to exponentially small deviations,over exponentially longtimes.Nekhoroshev（1977,1979） has shown the global result, undera“steepness condition”which is in particular satisfed for convex Hamiltonians,that for sufficiently small $\varepsilon$ everysolutionof theperturbed Hamiltonian system satisfies,for some positive constants $A , B < 1$ (proportional to the inverse of the square of the dimension),

$$
\| a ( t ) - a ( 0 ) \| \leq \varepsilon ^ { B } \quad { \mathrm { ~ f o r ~ } } t \leq \exp ( \varepsilon ^ { - A } ) .
$$

Remark4.6.Theconstant $C _ { 1 }$ inLemma 4.2and constantsin similar estimates of Hamiltonian perturbation theory are very large,with the consequence that theresults onthe long-time behaviour derived from them are meaningful,inarigorous sense, onlyfor extremely small values of theperturbation parameter $\varepsilon$ Nevertheless,apart fromtheir pure theoretical interest these results are of value as they describe the behaviour to be expected if one presupposes that the constants obtained from the worst-case estimations are unduly pessimistic fora given problem,as is typically thecase.

ProofofTheorem4.4.TheproofcombinesLemmas4.2and4.3withtheproofof Lemma2.1.Anappropriate choice of the truncation indices $N$ and $m$ then gives the exponential estimates.

Asinthe proof ofLemma2.1,we approximate $H _ { 1 } ( b , \theta )$ byatrigonometric polynomial of order $m$ in $\theta$ Theerror of this approximation is bounded by $\mathcal { O } ( e ^ { - m \rho / 2 } )$ on $B _ { r } ( b ^ { * } ) \times U _ { \rho / 2 }$ ,whichis $\mathcal { O } ( e ^ { - N } )$ for the choice $m = 2 N / \rho$ made below.By thearguments of theproof ofLemma2.1,the estimates ofLemmas 4.2and 4.3（for $\gamma$ replaced by $\gamma / 2$ ,which increases $C _ { 1 }$ to $4 C _ { 1 }$ arethenvalid in $O ( ( j m ) ^ { - \alpha } )$ and $\mathcal { O } ( ( N m ) ^ { - \alpha } )$ neighbourhoods of $b ^ { * }$ forasufficiently small constant $c ^ { * }$ andwith $C _ { 2 } = 1 6 C _ { 1 } / r$ ,

$$
\begin{array} { r l } { \displaystyle \left\| \frac { \partial S _ { j } } { \partial \theta } ( b , \theta ) \right\| \le C _ { 0 } \bigl ( 4 C _ { 1 } j ^ { \alpha } \bigr ) ^ { j - 1 } } & { \quad \mathrm { f o r } \quad \| b - b ^ { * } \| \le c ^ { * } ( j m ) ^ { - \alpha } , \theta \in U _ { \rho / 2 } , } \\ { \displaystyle | R _ { N } ( b , \theta ) | \le 4 M r \big ( C _ { 2 } N ^ { \alpha } \big ) ^ { N } } & { \quad \mathrm { f o r } \quad \| b - b ^ { * } \| \le c ^ { * } ( N m ) ^ { - \alpha } , \theta \in U _ { \rho / 2 } , } \end{array}
$$

Wenow consider the symplectic change of variables $( a , \theta ) \mapsto ( b , \varphi )$ defined by the generating function $S ( b , \theta )$ TheHamiltonian equationsin thevariables $( b , \varphi )$ are thenof the form,for $\lVert b - b ^ { * } \rVert \leq c ^ { * } ( N m ) ^ { - \alpha }$ ,

$$
\begin{array} { l } { \displaystyle { \dot { b } = - \frac { \partial K } { \partial \varphi } ( b , \varphi ) = - \varepsilon ^ { N } \frac { \partial R _ { N } } { \partial \theta } \frac { \partial \theta } { \partial \varphi } = \mathcal { O } ( \varepsilon ^ { N } ( C _ { 2 } N ^ { \alpha } ) ^ { N } ) } } \\ { \displaystyle { \dot { \varphi } = \frac { \partial K } { \partial b } ( b , \varphi ) = \omega _ { \varepsilon , N } ( b ) + \mathcal { O } ( ( N m ) ^ { \alpha } \cdot \varepsilon ^ { N } ( C _ { 2 } N ^ { \alpha } ) ^ { N } ) . } } \end{array}
$$

Choosing $m = 2 N / \rho$ and $N$ such that $C _ { 2 } N ^ { \alpha } = 1 / ( e \varepsilon ^ { \beta } )$ gives

$$
\begin{array} { r c l l } { \dot { b } } & { = } & { \mathcal { O } ( \exp ( - c \varepsilon ^ { - \beta / \alpha } ) ) } \\ { \dot { \varphi } } & { = } & { \omega _ { \varepsilon , N } ( b ) + \mathcal { O } ( \varepsilon ^ { - 2 \beta } \exp ( - c \varepsilon ^ { - \beta / \alpha } ) ) } \end{array} \quad \begin{array} { r c l } { \mathrm { ~ f o r ~ } } & { \| b - b ^ { * } \| \leq c _ { 0 } \varepsilon ^ { 2 \beta } } \\ { \mathrm { ~ f o r ~ } } & { \| b - b ^ { * } \| \leq c _ { 0 } \varepsilon ^ { 2 \beta } } \end{array}
$$

with $c = ( C _ { 2 } e ) ^ { - \alpha }$ ,which yields the result.

# X.4.3Near-Invariant Tori of Symplectic Integrators

Wereturn to the situation of Sect.X.3and applya symplectic numerical method to theintegrableHamiltonian system(3.1）with(3.2) and(3.3).

Theorem4.7.Consider applying a symplectic numerical integrator oforder $p$ tothereal-analytic completely integrable Hamiltonian system(3.1).Suppose that $\omega ( a ^ { * } )$ satisfies thediophantinecondition(2.4).Then,there existpositive constants $c _ { 0 } , c , C$ and $h _ { 0 }$ such that the following holds forall step sizes $\textit { h } \leq \ h _ { 0 }$ and for all $\mu \leq \operatorname* { m i n } ( p , \alpha )$ with $\alpha = \nu + d + 1$ ：every numerical solution startingwith $\| I ( p _ { 0 } , q _ { 0 } ) - a ^ { * } \| \leq c _ { 0 } h ^ { 2 \mu }$ satisfies

$$
\begin{array} { r } { \| I ( p _ { n } , q _ { n } ) - I ( p _ { 0 } , q _ { 0 } ) \| \le C h ^ { p } ~ f o r ~ n h \le \exp ( c h ^ { - \mu / \alpha } ) . } \end{array}
$$

The constants $h _ { 0 } , c _ { 0 } , c , C$ depend on $d , \gamma , \nu$ ,onboundsofthereal-analytic Hamiltonian $H$ onacomplex neighbourhood of the torus $\{ ( p , q ) ; I ( p , q ) = a ^ { * } \}$ andon thenumericalmethod.

ProofThe proof is obtained by following the arguments of theproof of Theorem3.1.Instead ofLemma2.1,nowTheorem4.4isapplied to themodified Hamiltonian system(3.5）with $\varepsilon = h ^ { p } .$ This gives achange of coordinates $( a , \theta ) \mapsto ( b , \varphi )$ $\mathcal { O } ( h ^ { p } )$ -close to theidentity,suchthatinthe newvariables,thesolution $( b ( t ) , \widetilde { \varphi } ( t ) )$ of(3.5） satisfies

$$
\begin{array} { r } { \widetilde b ( t ) = b _ { 0 } + \mathcal { O } ( \exp ( - c h ^ { - \mu / \alpha } ) ) \quad \mathrm { ~ f o r ~ } \ t \leq \exp ( c h ^ { - \mu / \alpha } ) . } \end{array}
$$

Onthe other hand,using theexponentially small boundofTheoremIX.7.6,together with Theorem4.4 and the arguments of part (b)of theproof of Theorem3.1,yields forthe numerical solution in the new variables

$$
b _ { n } = \widetilde b ( t ) + \mathcal { O } ( \exp ( - c h ^ { - \mu / \alpha } ) ) \quad \mathrm { ~ f o r ~ } t = n h \leq \exp ( c h ^ { - \mu / \alpha } ) .
$$

Together with $a _ { n } - b _ { n } = O ( h ^ { p } )$ this gives the result.

Remark 4.8.When the symplecticmethod is applied toaperturbed integrable systemasin Theorem4.4,then thesameargumentyields for $\| I ( p _ { 0 } , q _ { 0 } ) - a ^ { * } \| \leq c _ { 0 } \eta ^ { 2 \beta }$ with $\eta = \operatorname* { m a x } ( \varepsilon , h ^ { p } )$ and $\beta \leq 1$ thebound

$$
\| I ( p _ { n } , q _ { n } ) - I ( p _ { 0 } , q _ { 0 } ) \| \leq C \eta ~ \mathrm { f o r } ~ t \leq \exp ( c \eta ^ { - \beta / \alpha } ) .
$$

# X.5 Kolmogorov's Theorem on Invariant Tori

(Theproof of this theoremwaspublishedin Dokl.Akad.Nauk SSSR98 (1954),527-530[MR16,924],but theconvergencediscussion does not seemconvincingtothe reviewer.）Thisveryinteresting theorem would implythat for ananalytic canonical systemwhich is close toan integrable one,all solutions but a set of small measure lie on invariant tori.

(J.Moser 1959)

Itwasacelebrated discovery by Kolmogorov(1954） that invariant tori carryinga conditionally periodic flowwith diophantine frequencies persist under small perturbations of the Hamiltonian.Together with the extensions and refinements by Arnold (1963),Moser (1962）and later authors,Kolmogorov'sresult formswhat isnow known as KAM theory.Here we givea proof of Kolmogorov's theoremand use itin studying the long-time behaviour of symplectic numerical methods applied to perturbed integrablesystems.

# X.5.1Kolmogorov's Theorem

InSect.X.2.3we have already given Kolmogorov's transformationwhich reduces thesizeofaperturbation toaHamiltonian of the form(2.8) from $\mathcal { O } ( \varepsilon )$ to $O ( E ^ { 2 } ) ,$ at leastfornally.The iteration of that procedure is convergent and yields the following result.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/03678104fa06073dbe09e6bc03339b94928c1a1a299ecb019a8548ec1fec6c4c.jpg)

Theorem5.1 (Kolmogorov 1954).Considerareal-analytic Hamiltonian $H ( a , \theta )$ , definedforainaneighbourhoodof $0 \in \mathbb { R } ^ { d }$ and $\theta \in  { \mathbb { T } } ^ { d } ,$ forwhichthelinearization at $a ^ { * } = 0$ does not depend on the angles:

$$
\begin{array} { r } { H ( a , \theta ) = c + \omega \cdot a + \frac { 1 } { 2 } a ^ { T } M ( a , \theta ) a . } \end{array}
$$

Suppose that $\omega \in \mathbb { R } ^ { d }$ satisfies thediophantine condition (2.4),viz.,

$$
| \boldsymbol { k } \cdot \boldsymbol { \omega } | \geq \gamma | \boldsymbol { k } | ^ { - \nu } \mathrm { ~ \it ~ { ~ f o r ~ } ~ \boldsymbol { k } \in \mathbb { Z } ^ { d } , \boldsymbol { k } \neq 0 , }
$$

and that the angular average $M _ { 0 }$ of $M ( 0 , \cdot )$ isan invertible $d \times d$ matrix:

$$
\begin{array} { r } { \| \overline { { M } } _ { 0 } v \| \geq \mu \| v \| \quad f o r \quad v \in \mathbb R ^ { d } , } \end{array}
$$

with positive constants $\gamma , \nu , \mu .$ Let $H _ { \varepsilon } ( a , \theta ) ~ = ~ H ( a , \theta ) + \varepsilon G ( a , \theta )$ be $\boldsymbol { a }$ realanalyticperturbationof $H ( a , \theta )$ Then,thereexists $\varepsilon _ { 0 } > 0$ suchthat forevery $\succeq$ with $| \varepsilon | \leq \varepsilon _ { 0 }$ thereisananalytic symplectictransformation $\psi _ { \epsilon } : ( b , \varphi ) \mapsto ( a , \theta )$ , $\mathcal { O } ( \varepsilon )$ closeto the identityanddependinganalytically on $\succ$ ,whichputstheperturbed Hamiltonian back totheform

$$
\begin{array} { r } { H _ { \varepsilon } ( a , \theta ) = c _ { \varepsilon } + \omega \cdot b + \frac { 1 } { 2 } b ^ { T } M _ { \varepsilon } ( b , \varphi ) b { \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } f o r } \quad ( a , \theta ) = \psi _ { \varepsilon } ( b , \varphi ) . } \end{array}
$$

Theperturbed systemthereforehastheinvariant torus $\{ b = 0 , \varphi \in \mathbb { T } ^ { d } \}$ carryinga quasi-periodicflowwiththesame frequencies $\boldsymbol { \omega }$ astheunperturbedsystem.

(Thethreshold $\varepsilon _ { 0 }$ dependson $d , \nu , \gamma , \mu$ andon boundsof $H$ and $G$ onacomplexneighbourhoodof $\left\{ 0 \right\} \times  { \mathbb { T } } ^ { d } .$ ）

Of particular interest is the case when $H ( a , \theta ) = H _ { 0 } ( a )$ is independent of $\theta$ , sothat we are considering perturbations of an integrable system.In this case,the theoremshows thatallinvariant tori with frequencies $\omega ( a ) = \partial H _ { 0 } / \partial a ( a )$ satisfying （5.2）and with invertible Hessian $\partial ^ { 2 } H _ { 0 } / \partial a ^ { 2 } ( a )$ persist under small perturbations andareonly slightlydeformed.

Kolmogorov(1954） stated the theorem and formulated the iteration of SectionX.2.3,but did not give thedetails of the convergence estimates.Arnold(1963） gavea first complete proof of the theorem for perturbed integrable systems,usinga construction based on the“ultra-violetcutoff”(cf.Lemma 2.1）which yields a single transformation simultaneously forall frequencies satisfying the diophantine condition(2.4),incontrast toKolmogorov's iteration which yields adifferent transformationforevery choice of diophantine frequencies.However,Arnold'stransformation isno longer analytic in theperturbationparameterε.Moser(1962）showed that the analyticity of the Hamiltoniancan bereplaced bydifferentiability of sufficiently high order.Full proofs of Kolmogorov's theorem alonghis original construction were published by Thirring(1977)(forareduced model problem) and by Benettin, Galgani,Giorgilli& Strelcyn（1984).

AsinRemark4.6,apracticaldifficultywith Theorem5.1isthat the theoretically obtained threshold $\div 0$ is very small.The proof below requires $\varepsilon _ { 0 } \leq \delta _ { 0 } ^ { \mathrm { o } \alpha }$ with $\alpha = \nu + d + 1$ ofLemma4.1,where $\delta _ { 0 }$ isinversely proportional to $\nu$ Thispessimistic estimate of the threshold can be somewhat improved by first reducing the perturbation ofanintegrable Hamiltonian system viaaperturbation series expansionas in theproof ofTheorem 4.4and thenapplyingKolmogorov'stheorem tothe remainder of the truncated perturbation series.

Theproof of Theorem5.1uses iterativelythe following lemma,which refers tothetransformation constructed in Sect.X.2.3.Similarto Sect.X.4weuse the notation

$$
\| G \| _ { \rho } = \operatorname* { s u p } \{ | G ( a , \theta ) | ; \| a \| < \rho , \ \| \mathrm { I m } \theta \| < \rho \}
$$

forabounded analytic function $G$ on $W _ { \rho } : = B _ { \rho } ( 0 ) \times U _ { \rho }$ ,whereagain $B _ { \rho } ( 0 )$ isthe complex ball of radius $\rho$ around Oand $U _ { \rho }$ is the complex extension of $\mathbb { T } ^ { d }$ ofwidth $\boldsymbol { \rho }$ Thesame notation is used for vector-and matrix-valued functions,in which case the underlying norm on $\mathbb { C } ^ { d }$ or $\mathbb { C } ^ { d \times d }$ is themaximumnorm or itsinduced matrix norm, respectively.

Lemma5.2. Inthe situationofSect. $X . 2 . 3$ andundertheconditionsofTheorem5.1, supposethat $H$ and $G$ arereal-analyticandboundedon $W _ { \rho }$ Then,thereexists $\delta _ { 0 } >$ Osuch thatthefollowing bounds hold forKolmogorov'stransformationwhenever $0 < \delta \le \delta _ { 0 }$

$$
\begin{array} { r l } { i f } & { \| \varepsilon G \| _ { \rho } \leq \delta ^ { 5 \alpha } , \quad t h e n \quad \| \varepsilon ^ { 2 } \widehat { G } \| _ { \rho - \delta } \leq ( \frac { 1 } { 2 } \delta ) ^ { 5 \alpha } } \\ & { a n d \quad \| \varepsilon \nabla \chi \| _ { \rho - \delta } \leq \delta ^ { 3 \alpha } , \quad \| \widehat { M } - M \| _ { \rho - \delta } \leq \delta ^ { 2 \alpha } , } \end{array}
$$

where $\alpha = \nu + d + 1$ Thethreshold $\delta _ { 0 }$ depends only on $d , \nu , \gamma , \mu$ and on $\| H \| _ { \rho }$

Proof.We estimate the terms arising in the construction of Kolmogorov's transformation of Sect.X.2.3.For brevity wedenote $\| \cdot \| _ { j } = \| \cdot \| _ { \rho - j \delta / 4 }$ for $j = 0 , 1 , 2 , 3 , 4$ .

（a)The transformation $( b , \varphi ) \mapsto ( a , \theta )$ is constructed such that $( a , \theta ) = y ( \varepsilon )$ , where $y ( t )$ is the solution of $\dot { y } = J ^ { - 1 } \nabla \chi ( y )$ with $y ( 0 ) = ( b , \varphi )$ Suppose for the momentthat

$$
\begin{array} { r } { \| \varepsilon \nabla \chi \| _ { 3 } \leq \frac { 1 } { 4 } \delta . } \end{array}
$$

Let $( b , \varphi ) \in W _ { \rho - \delta } .$ Then, $\| y ( t ) - y ( 0 ) \| \leq \frac { 1 } { 4 } \delta$ for $0 \leq t \leq \varepsilon$ ,and in particular $\begin{array} { r } { \| ( a , \theta ) - ( b , \varphi ) \| \leq \frac { 1 } { 4 } \delta . } \end{array}$ Wedefine

$$
\begin{array} { r c l } { \varepsilon ^ { 2 } R ( b , \varphi ) } & { : = } & { \Big ( a - b + \varepsilon \frac { \partial \chi } { \partial \varphi } ( b , \varphi ) , \ \theta - \varphi - \varepsilon \frac { \partial \chi } { \partial b } ( b , \varphi ) \Big ) } \\ & { = } & { y ( \varepsilon ) - y ( 0 ) - \varepsilon J ^ { - 1 } \nabla \chi ( y ( 0 ) ) } \end{array}
$$

and note

$$
\begin{array} { r } { \| R _ { \star } ^ { \prime } \boldsymbol { b } , \varphi ) \| \leq \frac { 1 } { 2 } \displaystyle \operatorname* { m a x } _ { 0 \leq t \leq \varepsilon } \| \ddot { y } ( t ) \| \leq \frac { 1 } { 2 } \| J ^ { - 1 } \nabla ^ { 2 } \chi \ J ^ { - 1 } \nabla \chi \| _ { 3 } } \end{array}
$$

so that

$$
\begin{array} { r } { \| R \| _ { 4 } \leq \frac { 1 } { 2 } \| \nabla ^ { 2 } \chi \| _ { 3 } \| \nabla \chi \| _ { 3 } . } \end{array}
$$

(b)Tracing the construction of Sect.X.2.3,we find by Taylor expansion of $H ( a , \theta )$ that the new matrix is

$$
\widehat { M } ( b , \varphi ) = M ( b , \varphi ) + \varepsilon L ( b , \varphi )
$$

with

$$
L ( b , \varphi ) = \sum _ { i = 1 } ^ { d } \left( \frac { \partial M } { \partial a _ { i } } \frac { \partial \chi } { \partial \varphi _ { i } } - \frac { \partial M } { \partial \theta _ { i } } \frac { \partial \chi } { \partial b _ { i } } \right) ( b , \varphi ) + P ( b , \varphi ) + Q ( b , \varphi )
$$

where $P ( 6 , \varphi )$ is symmetric with

$$
b ^ { T } P ( b , \varphi ) b = b ^ { T } \big ( M ( b , \varphi ) - M ( 0 , \varphi ) \big ) \frac { \partial \chi } { \partial \varphi }
$$

and where $Q ( b , \varphi )$ is given by(2.11).Itfollows that

$$
\begin{array} { r } { \| \widehat { M } - M \| _ { 4 } \leq 2 \varepsilon ( \| \nabla M \| _ { 4 } \| \nabla \chi \| _ { 4 } + \| \nabla ^ { 2 } G \| _ { 4 } ) . } \end{array}
$$

From the construction of $\widehat { G }$ wealso findby simpleestimates of Taylorremainders

$$
\begin{array} { r } { \| \widehat { G } \| _ { 4 } \leq \| \nabla H \| _ { 3 } \| R \| _ { 4 } + \| \nabla G \| _ { 3 } \| \nabla \chi \| _ { 4 } + \| \nabla ^ { 2 } H \| _ { 3 } \| \nabla \chi \| _ { 4 } ^ { 2 } . } \end{array}
$$

(c)UsingLemma 4.1in theequations (2.12)-(2.16) defining $\chi$ of(2.10）,we obtainfirst

$$
\left\| \chi _ { 0 } \right\| _ { 1 } \leq \kappa _ { 0 } \delta ^ { - \alpha + 1 } \| G _ { 0 } \| _ { 0 } , \quad \left\| \frac { \partial \chi _ { 0 } } { \partial \varphi } \right\| _ { 1 } \leq \kappa _ { 1 } \delta ^ { - \alpha } \| G _ { 0 } \| _ { 0 }
$$

and by a second application of that lemma,for $i = 1 , \ldots , d$

$$
\| \chi _ { t } \| _ { 2 } \leq \kappa _ { 0 } \delta ^ { - \alpha + 1 } \left( \| u \| _ { 1 } + \| v \| _ { 1 } + \| G _ { i } \| _ { 1 } \right)
$$

where,by construction of $u$ and $\boldsymbol { v }$

$$
\| v \| _ { 1 } \leq \| M \| _ { 1 } \left\| { \frac { \partial \chi _ { 0 } } { \partial \varphi } } \right\| _ { 1 } , \quad \| u \| _ { 1 } \leq \| M \| _ { 1 } \mu ^ { - 1 } \Big ( \| v \| _ { 1 } + \sum _ { j = 1 } ^ { d } \| G _ { j } \| _ { 1 } \Big ) .
$$

It then follows by Cauchy'sestimates that

$$
\| \nabla \chi \| _ { 3 } \leq C \delta ^ { - 2 \alpha } \| G \| _ { 0 } , \qquad \| \nabla ^ { 2 } \chi \| _ { 3 } \leq C \delta ^ { - 2 \alpha - 1 } \| G \| _ { 0 } ,
$$

(d)Combining the estimates (5.6)-(5.9) and using once more Cauchy'sestimatesto bound derivatives of $H$ and $G$ yields

$$
\begin{array} { r l } { \| \varepsilon ^ { 2 } \widehat { G } \| _ { \rho - \delta } } & { \le \ C \delta ^ { - 4 \alpha - 1 } \| \varepsilon G \| _ { \rho } ^ { 2 } } \\ { \| \varepsilon \nabla \chi \| _ { \rho - \delta } } & { \le \ C \delta ^ { - 2 \alpha } \| \varepsilon G \| _ { \rho } } \\ { \| \widehat { M } - M \| _ { \rho - \delta } } & { \le \ C \delta ^ { - 2 \alpha - 3 } \| \varepsilon G \| _ { \rho } . } \end{array}
$$

All this holdsunder the condition (5.5).By (5.9),this condition is satisfiedif $\| \varepsilon G \| _ { \rho } \leq \delta ^ { 5 \alpha }$ and $\delta \leq \delta _ { 0 }$ withasufficiently small $\delta _ { 0 }$ (Tracing the above constants shows that δneeds tobeinversely proportionalto1 ,orinversely proportional to $\nu$ )Thisyieldsthestated bounds. □

Proofof Theorem5.1.Kolmogorov'siteration yieldssequences

$$
\begin{array} { l } { { G ^ { ( 0 ) } = G , G ^ { ( 1 ) } , G ^ { ( 2 ) } , \dots } } \\ { { M ^ { ( 0 ) } = M , M ^ { ( 1 ) } , M ^ { ( 2 ) } , \dots } } \\ { { \chi ^ { ( 0 ) } , \chi ^ { ( 1 ) } , \chi ^ { ( 2 ) } , \dots . } } \end{array}
$$

ByLemma5.2theysatisfy,providedthat $\| \varepsilon G \| _ { \rho } = \delta ^ { 5 \alpha }$ with $\delta \le \delta _ { 0 }$ ,

$$
\begin{array} { r l r } { \Vert \varepsilon ^ { 2 ^ { j } } G ^ { ( j ) } \Vert _ { \rho ^ { ( j ) } } } & { \le ~ ( 2 ^ { - j } \delta ) ^ { 5 \alpha } } & \\ & { } & \\ { \Vert M ^ { ( j + 1 ) } - M ^ { ( j ) } \Vert _ { \rho ^ { ( j ) } } } & { \le ~ ( 2 ^ { - j } \delta ) ^ { 2 \alpha } } & \\ & { } & \\ { \Vert \varepsilon ^ { 2 ^ { j } } \nabla \chi ^ { ( j ) } \Vert _ { \rho ^ { ( j ) } } } & { \le ~ ( 2 ^ { - j } \delta ) ^ { 3 \alpha } } & \end{array}
$$

where $\rho ^ { ( j ) } = \rho - ( 1 + \textstyle { \frac { 1 } { 2 } } + \ldots + 2 ^ { - j } ) \delta > \frac { 1 } { 2 } \rho$ forall $j .$ Note that (5.11） implies that the inverse of $M ^ { ( j ) }$ isbounded by $2 \mu ^ { - 1 }$ forall $j$ ,so that the iterative use of Lemma5.2is justified.Thetime $\varepsilon ^ { 2 , \prime }$ flow of $\chi ^ { ( j ) }$ is a symplectic transformation $\sigma _ { \varepsilon } ^ { ( j ) }$ ,which by (5.12)satisfies

$$
\begin{array} { r } { \| \sigma _ { \varepsilon } ^ { ( j ) } - \mathrm { i d } \| _ { \rho / 2 } \leq ( 2 ^ { - j } \delta ) ^ { 3 \alpha } . } \end{array}
$$

The composed transformation

$$
\psi _ { \varepsilon } ^ { ( j ) } : = \sigma _ { \varepsilon } ^ { ( 0 ) } \circ \sigma _ { \varepsilon } ^ { ( 1 ) } \circ \dots \circ \sigma _ { \varepsilon } ^ { ( j ) }
$$

is constructed such that

$$
H ( \psi _ { \varepsilon } ^ { ( j - 1 ) } ( b , \varphi ) ) = c ^ { ( j ) } + \omega \cdot b + b ^ { T } M ^ { ( j ) } ( b , \varphi ) b + \varepsilon ^ { 2 ^ { j } } G ^ { ( j ) } ( b , \varphi ) .
$$

By (5.13),the sequence $\psi _ { \varepsilon } ^ { ( j ) } ( \boldsymbol { b } , \varphi )$ converges uniformly on $W _ { \rho / 2 } \times ( - \varepsilon _ { 0 } , \varepsilon _ { 0 } )$ toa limit $\psi _ { \varepsilon } ( b , \varphi )$ ByWeierstrass'theorem, $\psi _ { \varepsilon } ( b , \varphi )$ isanalyticin $( b , \varphi , \varepsilon )$ (and in any further parameters on which $M$ and $G$ might possibly depend analytically).Since $\psi _ { \varepsilon }$ depends analytically on $\boldsymbol { \mathsf { E } }$ and $\psi _ { 0 } = \mathrm { i d }$ ,it followsthat $\psi _ { \varepsilon }$ is $\mathcal { O } ( \varepsilon )$ -close tothe identity on $W _ { \rho / 2 }$ By(5.10) and (5.14),the transformed Hamiltonian $H \circ \psi _ { \varepsilon }$ isof the desired form (5.4). □

# X.5.2KAM Tori under Symplectic Discretization

Considera Hamiltonian system

$$
\dot { p } = - \frac { \partial { \mathcal H } } { \partial q } ( p , q ) , \quad \ddot { q } = \frac { \partial { \mathcal H } } { \partial p } ( p , q ) ,
$$

for which,in suitable coordinates $( a , \theta )$ ,the Hamiltonian ${ \mathcal { H } } ( p , q ) ~ = ~ H ( a , \theta ) +$ $\varepsilon G ( a , \theta )$ satisfies theconditions of Theorem 5.1.Kolmogorov's.theorem yieldsa transformationto variables $( b , \varphi )$ in terms of which

$$
\begin{array} { r } { \mathcal { H } ( p , q ) = \omega \cdot b + \frac { 1 } { 2 } b ^ { T } M _ { \varepsilon } ( b , \varphi ) b , } \end{array}
$$

so that the torus ${ \mathcal { T } } _ { \omega } = \{ b = 0 , \ \varphi \in  { \mathbb { T } } ^ { d } \}$ is invariant and the flow on itis quasiperiodic with frequencies $\omega$

Forasymplectic integrator of order $p$ appliedto(5.15）,backward analysisgives amodified Hamiltonian $\mathcal { H } ( p , q )$ which is an $\mathcal { O } ( h ^ { p } )$ perturbation of $\mathcal { H } ( p , q )$ ：

$$
\widetilde { \mathcal { H } } ( p , q ) = \omega \cdot b + \textstyle { \frac { 1 } { 2 } } b ^ { T } M _ { \varepsilon } ( b , \varphi ) b + \hbar ^ { p } \widetilde { G } ( b , \varphi ) .
$$

Kolmogorov's theoremcan be applied once more,yieldingan invariant torus $\bar { \mathcal { T } } _ { \omega }$ of the modified Hamiltonian ${ \mathcal { H } } ( p , q )$ which again carries a quasi-periodic flow with frequencies $\omega$ .Combined with the exponentially small estimates ofbackwardanalysisfor the difference between numerical solutions and the flow of the modified Hamiltoniansystem,this gives the following result of Hairer&Lubich（1997).

Theorem5.3.Intheabove situation,forasymplecticintegratoroforder $p$ used withsufficiently small step size $h$ ，thereisamodified Hamiltonian $\mathcal { H }$ with aninvariant torus $\widetilde { T } _ { \omega }$ carryinga quasi-periodic flowwith frequencies $\boldsymbol { \omega }$ , $\mathcal { O } ( h ^ { p } )$ close tothe invariant torus $\scriptstyle { { \mathcal { T } } _ { \omega } }$ ofthe original Hamiltonian $\mathcal { H }$ ，suchthatthedifference between any numerical solution $( p _ { n } , q _ { n } )$ starting on the torus $\bar { \mathcal { T } } _ { \omega }$ and the solution $( p ( t ) , q ( t ) )$ ofthemodified Hamiltonian system with the same starting valuesremainsexponentially small in $1 / h$ over exponentially long times:

$$
\begin{array} { r } { \vert \vert ( p _ { n } , q _ { \bar { n } } ) - ( \widetilde { p } ( t ) , \widetilde { q } ( t ) ) \vert \vert \le C e ^ { - \kappa / h } ~ f o r ~ t = n h \le e ^ { \kappa / h } . } \end{array}
$$

The constants $C$ and $\boldsymbol { \scriptscriptstyle  { ering } }$ areindependent of $n , h , \varepsilon$ (forh,esufficientlysmall)andof the initial value $( p _ { 0 } , q _ { 0 } ) \in \mathcal { T } _ { \omega }$ .

Proof.(a)Forsufficiently small $h$ Kolmogorov's theoremappliedto（5.16)yieldsa change of coordinates $( b , \varphi ) \mapsto ( c , \psi ) , O ( h ^ { p } )$ close to the identity,which transforms themodified Hamiltonianto the form

$$
\begin{array} { r } { \widetilde { \mathcal { H } } ( p , q ) = \omega \cdot c + \frac { 1 } { 2 } c ^ { T } M _ { \varepsilon , h } ( c , \psi ) c , } \end{array}
$$

with the invariant torus ${ \mathcal { T } } _ { \omega } = \{ c = 0 , \ \psi \in  { \mathbb { T } } ^ { d } \} .$ The correspondingdiferential equations read in these coordinates

$$
\dot { \boldsymbol c } = \boldsymbol u ( \boldsymbol c , \psi ) , \qquad \dot { \psi } = \boldsymbol \omega + v ( \boldsymbol c , \psi )
$$

where $u ( c , \psi ) = \mathcal { O } ( \| c \| ^ { 2 } )$ and $v ( c , \psi ) = \mathcal { O } ( \| c \| )$ ,and similarly for thederivatives $\partial u / \partial c = \mathcal { O } ( | | c | | )$ , $\partial u / \partial \psi = \mathcal { O } ( | | c | | ^ { 2 } )$ ,and $\partial v / \partial c = \mathcal { O } ( 1 )$ ， $\partial v / \partial \psi = \mathcal { O } ( | | c | | )$ . The constants in these $\mathcal { O }$ -termsare independentof $h$ and $\varepsilon$ Let $( c ( t ) , \psi ( t ) )$ and $( \widehat { c } ( t ) , \psi ( t ) )$ be two solutions of (5.17) such that $\| c ( t ) \| \leq \beta$ $\| \widehat { c } ( t ) \| \le \beta$ $\beta$ sufficiently small） for all $t$ under consideration.Then,an argument based on Gronwall's lemma shows that their difference is bounded overatime interval $0 \leq t \leq 1 / \beta$ by

$$
\begin{array} { r } { \| c ( t ) - \widehat { c } ( t ) \| \le C \left( \| c ( 0 ) - \widehat { c } ( 0 ) \| + \beta \| \psi ( 0 ) - \widehat { \psi } ( 0 ) \| \right) } \\ { \| \psi ( t ) - \widehat { \psi } ( t ) \| \le C \left( t \| c ( 0 ) - \widehat { c } ( 0 ) \| + \| \psi ( 0 ) - \widehat { \psi } ( 0 ) \| \right) , } \end{array}
$$

for some constant $C$ that does not depend on $\beta$ ， $h$ or $\succ$ .

(b) In the following we denote $\boldsymbol { y } ~ = ~ ( p , q )$ for brevity,and more specifically, $y _ { n }$ denotes the numerical solution starting from any $y _ { 0 }$ on the torus $\bar { \tau _ { \omega } }$ ,i.e.,the $c$ -coordinateof $y _ { 0 }$ vanishes: $c _ { 0 } ~ = ~ 0$ We denote by $ { \mathcal { Y } } ( t , s , z )$ the solution of the modified Hamiltonian system with initial value $y ( s , s , z ) = z$ andmorebriefly $\tilde { y } ( t ) = \tilde { y } ( t , 0 , y _ { 0 } )$ the solution starting from $y _ { 0 }$ ByTheoremIX.7.6,thelocal error ofbackward error analysis at $t _ { j } = j h$ isbounded by

$$
\| y _ { j } - \widetilde { y } ( t _ { j } , t _ { j - 1 } , y _ { j - 1 } ) \| \le \delta : = C o n s t . h e ^ { - 3 \kappa / h }
$$

for some constant $\kappa$ aslongas $y _ { j }$ remains in a compact subset of the domain of analyticityof $\mathcal { H }$ We further denote the $c$ -coordinatesof $y _ { n }$ ， $y ( t )$ and $\mathbb { y } ( t , t _ { j } , y _ { j } )$ by $c _ { n }$ ， $c ( t )$ and $\overrightarrow { c } ( t , t _ { j } , y _ { j } )$ ,respectively.Toapply theerrorpropagation estimate(5.18), weassume that

$$
\| \widetilde c ( t , t _ { j } , y _ { j } ) \| \le \beta \quad \mathrm { ~ f o r ~ } t _ { j } \le t \le 1 / \beta
$$

and for all $j$ satisfying $t _ { j } = j h \le 1 / \beta$ Thisassumption willbe justified by induction later,and the value of $\beta$ will be specifiedin(5.21） below.By(5.18）we thus obtain the bound

$$
\begin{array} { r } { \vert \vert \widetilde { y } ( t , t _ { j } , y _ { j } ) - \widetilde { y } ( t , t _ { j - 1 } , y _ { j - 1 } ) \vert \vert \le C \left( 1 + ( t - t _ { j } ) \right) \delta \quad \ \mathrm { ~ f o r ~ } t _ { j } \le t \le 1 / \beta . } \end{array}
$$

Summing up from $j = 1$ to $\boldsymbol { n }$ gives for $t _ { n } \leq t \leq 1 / \beta$ (and $t > 2$ ）

$$
\begin{array} { r l r } {  { \| \widetilde { y } ( t , t _ { n } , y _ { n } ) - \widetilde { y } ( t ) \| \le \sum _ { j = 1 } ^ { n } C ( 1 + ( t - t _ { j } ) ) \delta \le C h ^ { - 1 } \delta ( t _ { n } + t t _ { n } - t _ { n } ^ { 2 } / 2 ) } } \\ & { } & \\ & { } & { < C h ^ { - 1 } \delta t ^ { 2 } \le C h ^ { - 1 } \delta / \beta ^ { 2 } , \qquad ( 5 . } \end{array}
$$

We now set

$$
\beta = ( 2 C h ^ { - 1 } \delta ) ^ { 1 / 3 } ,
$$

sothat $C h ^ { - 1 } \delta / \beta ^ { 2 } = \beta / 2$ ,and weobtain thedesired estimate from(5.20)by putting $t = t _ { n }$

(c)We still have to justify the assumption (5.19).Thiswill be done by induction. For $j = 0$ nothing needs to be shown,because $\widetilde { c } ( t , 0 , y _ { 0 } ) = \widetilde { c } ( t ) \equiv 0$ asaconsequence of the fact that $y ( t )$ stays on the invariant torus ${ \mathcal { T } } _ { \omega } = \{ c = 0 , \ \psi \in  { \mathbb { T } } ^ { d } \} .$ Suppose nowthat（5.19） holds for $j \leq n$ It then follows from（5.20）that

$$
\| \widetilde c ( t , t _ { n } , y _ { n } ) \| < C h ^ { - 1 } \delta / \beta ^ { 2 } = \beta / 2 \quad \quad \mathrm { f o r } \quad t _ { n } \le t \le 1 / \beta
$$

(again because of ${ \widetilde c } ( t ) \equiv 0$ ).Consequently we also have

$$
\| c _ { n + 1 } \| \leq \| c _ { n + 1 } - \widetilde c ( t _ { n + 1 } , t _ { n } , y _ { n } ) \| + \| \widetilde c ( t _ { n + 1 } , t _ { n } , y _ { n } ) \| < \delta + \beta / 2 \leq \beta ,
$$

provided that $h$ is sufficiently small so that $\delta \le \beta / 2$ Bycontinuity, $c ( t , t _ { n + 1 } , y _ { n + 1 } )$ is bounded by $\beta$ onanon-empty interval $\lfloor t _ { n + 1 } , T _ { n + 1 } \rfloor .$ The computation of part（b) showsthat $\| \widetilde c ( t , t _ { n + 1 } , y _ { n + 1 } ) \| \le \beta / 2$ on this interval.Hence, ${ \cal T } _ { n + 1 }$ can beincreased until $T _ { n + 1 } \geq 1 / \beta$ Thisproves theestimate(5.19) for $j = n + 1$ □

# X.6Invariant Tori of Symplectic Maps

In the preceding section,backward error analysis combined with Kolmogorov's theoremhas shown that a symplectic integratorapplied toa Hamiltonian systemwith KAMtori possesses tori that are near-invariant,upto exponentially small terms, overexponentially long times in the inverse of the step size.Toobtain truly invariant tori,we needadiscreteKAMtheorem forperturbationsof integrable near-identity mapsdepending on a small parameter,the step size.Such aresult wasrecently obtainedby Shang(1999,2Ooo),who gavea discrete Arnold-type construction.Here, weuse instead adiscrete-time version of Kolmogorov's iteration.This establishes theexistence of invariant tori of symplectic integrators applied to integrable Hamiltonian systems orto near-integrable systemswith KAMtori,fora Cantor set of non-resonant step sizes.

# X.6.1AKAMTheorem for Symplectic Near-Identity Maps

Weconsidera discrete-time analogue of the situation in Sections X.2.3andX.5.1 andconstruct the correspondingversion of Kolmogorov's iteration.Consider the symplectic map $\sigma _ { h } : ( a , \theta ) \mapsto ( { \widehat { a } } , { \widehat { \theta } } )$ for $^ { a }$ near $0 \in \mathbb { R } ^ { d }$ , $\theta \in  { \mathbb { T } } ^ { d }$ defined by

$$
{ \widehat { a } } = a - h { \frac { \partial S } { \partial { \widehat { \theta } } } } ( a , { \widehat { \theta } } ) , \quad { \widehat { \theta } } = \theta + h { \frac { \partial S } { \partial a } } ( a , { \widehat { \theta } } )
$$

where $h$ isa small parameter (the step size),and $S : B _ { r } ( 0 ) \times  { \mathbb { T } } ^ { d } \to  { \mathbb { R } }$ isareal-analytic generating function.If $S ( \boldsymbol { a } , \widehat { \boldsymbol { \theta } } )$ has the form(cf.(2.8)）

$$
\begin{array} { r } { S ( \alpha , \widehat { \theta } ) = c + \omega \cdot a + \frac { 1 } { 2 } a ^ { T } M ( a , \widehat { \theta } ) a , } \end{array}
$$

then the associated symplectic map is of the form

$$
\widehat { a } = a + \mathcal { O } ( h \| a \| ^ { 2 } ) , \quad \widehat { \theta } = \theta + h \omega + \mathcal { O } ( h \| a \| ) .
$$

Hence,the torus $\{ a = 0 , \ \theta \in  { \mathbb { T } } ^ { d } \}$ is invariant,and onitthe map $O _ { h }$ reducesto rotation by $h \omega$ ，

Consider now an analytic perturbation of such a generating function: $S ( a , \theta ) +$ $\varepsilon R ( a , { \widehat { \theta } } )$ withasmall $\varepsilon$ Weconstruct a near-identity symplectic change of coordinates,via an iterativeprocedure similarto Kolmogorov's iteration of Sect.X.2.3, such that the generating function of the perturbed symplectic map in the new variables is again of the form(6.2）with the same $\omega$ ,andhence theperturbed map hasan invariant torus on which itis conjugate to rotation by $h \omega$ This holdsif $h \omega$ satisfies the following diophantine condition (cf.(2.4)):

$$
\left| \frac { 1 - e ^ { - i k \cdot h \omega } } { h } \right| \geq \gamma ^ { * } | k | ^ { - \nu ^ { * } } ~ \mathrm { f o r } ~ k \in \mathbb { Z } ^ { d } , k \neq 0 ,
$$

for some positive constants $\gamma ^ { * } , \nu ^ { * }$ ；andif the angular average $\textstyle { M _ { 0 } }$ of $M ( 0 , \cdot )$ is invertible:

$$
\lVert \overline { { M } } _ { 0 } v \rVert \geq \mu ^ { * } \lVert v \rVert \mathrm { ~ f o r ~ } v \in \mathbb { R } ^ { d }
$$

forapositive constant $\mu ^ { * } .$ Asin Sect.X.2.3,we construct a symplectic transformation $( a , \theta ) \mapsto ( b , \varphi )$ asthe time- $\sf { \varepsilon }$ flowofanauxiliaryHamiltonian of the form (2.10),viz.,

$$
\chi ( b , \varphi ) = \xi \cdot \varphi + \chi _ { 0 } ( \varphi ) + \sum _ { i = 1 } ^ { d } b _ { i } \chi _ { i } ( \varphi )
$$

where $\xi \in \mathbb { R } ^ { d }$ is aconstant vector,and $\chi _ { 0 } , \chi _ { 1 } , \ldots , \chi _ { d }$ are $2 \pi$ -periodic functions. Wethen consider the map conjugate to the perturbed map $( a , \theta ) \mapsto ( { \widehat { a } } , { \widehat { \theta } } )$ generated by $S ( a , { \widehat { \theta } } ) + \varepsilon R ( a , { \widehat { \theta } } )$ :

$$
\begin{array} { r l r } { ( a , \theta ) } & { { } \longrightarrow } & { ( \widehat { a } , \widehat { \theta } ) } \\ { \uparrow \quad } & { { } } & { \downarrow } \\ { ( b , \varphi ) } & { { } } & { ( \widehat { b } , \widehat { \varphi } ) } \end{array}
$$

Weconstruct $\chi$ insuchaway that theabove composed symplecticmapis generated by $S ( b \widehat \varphi ) + \varepsilon ^ { 2 } R ( b , \widehat \varphi )$ with $\tilde { S }$ of the form(6.2）and both $\check { S }$ and $\bar { R }$ real-analyticand bounded independently of $\succeq$ andof $h$ with (6.3).The map $( b , \varphi ) \mapsto ( { \widehat { b } } , { \widehat { \varphi } } )$ is then of theform

$$
\widehat { b } = b + \mathcal { O } ( h \| b \| ^ { 2 } ) + \mathcal { O } ( h \varepsilon ^ { 2 } ) , \widehat { \varphi } = \varphi + \hbar \omega + \mathcal { O } ( h \| b \| ) + \mathcal { O } ( h \varepsilon ^ { 2 } ) .
$$

Asan elementary calculation shows,this holdsif $\chi$ satisfies for all $( 6 , \widehat { \varphi } )$ with $b$ near0,∈Td

$$
\frac { \langle b , \widehat \varphi \rangle - \chi ( b , \widehat \varphi - h \omega ) } { h } + b ^ { T } \ M ( b , \widehat \varphi ) \ \frac { \partial \chi } { \partial \varphi } ( b , \widehat \varphi - h \omega ) + R ( b , \widehat \varphi ) = C _ { h } + \mathcal { O } ( \| b \| _ { \infty } ) ,
$$

where $C _ { h }$ does not depend on $( b , \hat { \varphi } )$ and $\varepsilon$ Writing down the Taylor expansion

$$
R ( b , \widehat { \varphi } ) \equiv R _ { 0 } ( \widehat { \varphi } ) + \sum _ { i = 1 } ^ { d } b _ { i } R _ { i } ( \widehat { \varphi } ) + \mathcal { O } ( \| b \| ^ { 2 } )
$$

and inserting the above ansatz for $\chi$ ,this condition becomes fulfilled if,with $u ( { \widehat { \varphi } } ) =$ $M ( 0 , \widehat { \varphi } ) \xi$ and $\begin{array} { r } { v ( \widehat { \varphi } ) = M ( 0 , \widehat { \varphi } ) ( \partial \chi _ { 0 } / \partial \varphi ) ( \widehat { \varphi } - h \omega ) , } \end{array}$

$$
\begin{array} { r l r } {  { \frac { \chi _ { 0 } ( \widehat \varphi ) - \chi _ { 0 } ( \widehat \varphi - h \omega ) } { h } + R _ { 0 } ( \widehat \varphi ) = \overline { { R } } _ { 0 } } } \\ & { } & { \qquad k i ( \widehat \varphi ) - \chi _ { i } ( \widehat \varphi - h \omega ) } \\ & { } & { \qquad h ^ { \prime } } \\ & { } & { \overline { { u } } _ { i } + \overline { { v } } _ { i } + \overline { { R } } _ { i } = 0 \qquad ( i = 1 , \cdots , d ) } \end{array}
$$

wherethe barsagain denoteangularaverages.Wenote

$$
\frac { \chi _ { 0 } ( \widehat \varphi ) - \chi _ { 0 } ( \widehat \varphi - h \omega ) } { h } = \sum _ { k } \frac { 1 - e ^ { - i k \cdot h \omega } } { h } \chi _ { 0 , k } e ^ { i k \cdot \widehat \varphi } ,
$$

where $\chi _ { 0 , k }$ are the Fourier coefficients of $\chi _ { 0 }$ .Under the diophantine condition (6.3), Equation (6.5) is thus solved like(2.14) under condition (2.4).Equations (6.6)are ofthe same type.The above system is then solved in thesameway as(2.12)-(2.16), yielding that the perturbed map in the new coordinates, $( b , \varphi ) \mapsto ( { \widehat { b } } , { \widehat { \varphi } } )$ isgenerated by

$$
\begin{array} { r } { S ^ { ( 1 ) } ( b , \widehat { \varphi } ) \equiv c ^ { ( 1 ) } + \omega \cdot b + \frac { 1 } { 2 } b ^ { T } M ^ { ( 1 ) } ( b , \widehat { \varphi } ) b + \varepsilon ^ { 2 } R ^ { ( 1 ) } ( b , \widehat { \varphi } ) } \end{array}
$$

with unchanged frequencies $\boldsymbol { \omega }$ andwith $M ^ { ( 1 ) } ( b , \widehat { \varphi } ) = M ( b , \widehat { \varphi } ) + \mathcal { O } ( \varepsilon ) .$ The perturbation tothe form(6.2）isthusreduced from $\mathcal { O } ( \varepsilon )$ to ${ \mathcal { O } } ( \varepsilon ^ { 2 } ) .$ By the same arguments asin theproof of Theorem5.1itis shown that the iteration of thisprocedure converges.This proves the followingdiscrete-time version of Kolmogorov’stheorem.

Theorem6.1.Considerareal-analyticfunction $S ( a , \widehat { \theta } )$ oftheform(6.2）with(6.4）， definedonaneighbourhoodof $\left\{ 0 \right\} \times  { \mathbb { T } } ^ { d } .$ Let $| h | < h _ { 0 }$ $h _ { 0 }$ so small that $( 6 . I )$ is $a$ weil-defined map)and suppose that hw satisfies(6.3).

Let $S _ { \varepsilon } ( a , \widehat { \theta } ) = S ( a , \theta ) + \varepsilon R ( a , \widehat { \theta } )$ beananalyticperturbationof $S ( a , \theta )$ ,generatinga symplecticmap $\sigma _ { h , \epsilon } : ( a , \theta ) \longmapsto ( { \widehat { a } } , { \widehat { \theta } } )$ via(6.1）with $S _ { \varepsilon }$ inplace of $S$ ,

Then,thereexists $\varepsilon _ { 0 } > 0$ such that for every $\boldsymbol { \varepsilon }$ with $| \varepsilon | < \varepsilon _ { 0 }$ ,there is ananalytic formly in symplectictransformation $h$ satifyig(6.3)dnalyticin $\psi _ { h , \epsilon } : ( b , \varphi ) \mapsto ( a , \theta )$ $\boldsymbol { \mathrm { \Sigma } }$ such that $\mathcal { O } ( \varepsilon )$ $\psi _ { h , \varepsilon } ^ { - 1 } \circ \sigma _ { h , \varepsilon } \circ \psi _ { h , \varepsilon } : ( b , \varphi ) \mapsto $ closeto the identity uni-$( \widehat { b } , \widehat { \varphi } )$ isgenerated,via(6.1），byfuntion $S _ { h , \varepsilon } ^ { * } ( b , \widehat { \varphi } )$ whichisagainof theform (6.2）,i.e.,

$$
\begin{array} { r } { S _ { h , \varepsilon } ^ { * } ( b , \widehat { \varphi } ) = c _ { h , \varepsilon } + \omega \cdot b + \frac { 1 } { 2 } b ^ { T } M _ { h , \varepsilon } ( b , \widehat { \varphi } ) b . } \end{array}
$$

Theperturbed map $O h , \varepsilon$ thereforehasan invariant torus onwhich it isconjugate to rotationby $h \omega$ .

(Thethreshold $\varepsilon _ { 0 }$ dependsonlyon $d , \nu ^ { * } , \gamma ^ { * } , \mu ^ { * }$ and on boundsof $S$ and $R$ ona complexneighbourhoodof $\left\{ 0 \right\} \times  { \mathbb { T } } ^ { d } .$ ） □

# X.6.2 Invariant Tori of Symplectic Integrators

Asa direct consequence of Theorem 6.1 we obtain the following result on invariant toriofsymplectic integratorsapplied toKAMsystems.

Theorem6.2.Applya symplectic integratoroforderptoaperturbedintegrable systemwitha KAMtorus $\mathcal { T } _ { \omega }$ whichcarriesa quasi-periodicflowwithdiophantine frequencies $\omega$ Then,if the step size $h$ issufficiently small and satisfies the strong non-resonance condition(6.3),the numerical method hasan invariant torus ${ { T } _ { \omega , h } }$ $\mathcal { O } ( h ^ { p } )$ -closeto $T _ { \omega }$ ,onwhichit isconjugate to rotation by $h \omega$

ProofTheorem6.1 appliesdirectly,with $\varepsilon = h ^ { p }$ ,to the above situation.Here, the generating function $S ( \boldsymbol { a } , \boldsymbol { \tilde { \theta } } )$ of the time- $h$ flow $\varphi _ { h }$ of the Hamiltonian system with the KAMtorus $T _ { \omega }$ is of the form(6.2）in thevariables $( a , \theta )$ obtained by Kolmogorov's theorem.The matrix $M ( \boldsymbol { a } , \tilde { \boldsymbol { \theta } } )$ in (6.2) then differs from the corresponding matrix of(2.8）by ${ \mathcal { O } } ( h )$ ,sothat(5.3) implies (6.4).Finally,thegenerating function of the numerical one-step map $\phi _ { h }$ isan $\mathcal { O } ( h ^ { p } )$ -perturbation $S ( a , { \widehat { \theta } } ) + h ^ { p } R ( a , { \widehat { \theta } } ) . \varPi$

# X.6.3 Strongly Non-Resonant Step Sizes

Theorem 6.2 leaves us with an interesting question: if $\omega \in \mathbb { R } ^ { d }$ is a vector of frequenciesthat satisfies the diophantine condition(2.4),then which step sizes $h$ satisfy the non-resonance condition (6.3)?Here we give a lemma in the spirit of results by Shang(2OoO).It shows that the probability of picking an $h \in ( 0 , h _ { 0 } )$ satisfying （6.3）tends to1as $h _ { 0 } \to 0$ .

Lemma6.3. Suppose $\omega \in \mathbb { R } ^ { d }$ satisfes (2.4),and let $h _ { 0 } ~ > ~ 0$ Forany choice of positive $\gamma ^ { * }$ and $\nu ^ { * }$ ,theset

$$
Z ( h _ { 0 } ) = \{ h \in ( 0 , h _ { 0 } ) \ ; \ h \ d o e s \ n o t s a t i s f y \ ( 6 . 3 ) \}
$$

is open and dense in $( 0 , h _ { 0 } ) .$ If $\gamma ^ { * } \leq \gamma$ and $\nu ^ { * } > \nu + d + r$ with $r > 1 ,$ thenthe Lebesgue measureof $Z ( h _ { 0 } )$ isboundedby

$$
\mathrm { m e a s u r e } \left( Z ( h _ { 0 } ) \right) \le C \frac { \gamma ^ { * } } { \gamma } h _ { 0 } ^ { r + 1 }
$$

where $C$ depends onlyon $d , \nu , \nu ^ { * }$ and $\vert \vert \omega \vert \vert$

Proof.Itisclear from the definition that $Z ( h _ { 0 } )$ is open and dense in $( 0 , h _ { 0 } )$ It remains to prove the estimate of the Lebesgue measure.Forevery $k \in  { \mathbb { Z } ^ { d } }$ and $| h | \leq h _ { 0 }$ ,there exists an integer $l = l ( k , h )$ such that

$$
| 1 - e ^ { - i { \boldsymbol { k } } \cdot { \hbar } \omega } | \geq { \frac { 2 } { \pi } } | { \boldsymbol { k } } \cdot { \hbar } \omega - 2 \pi { \boldsymbol { l } } | = { \frac { 2 } { \pi } } | { \boldsymbol { k } } \cdot \omega | \cdot \left| { \boldsymbol { h } } - { \frac { 2 \pi l } { | { \boldsymbol { k } } \cdot \omega | } } \right| ,
$$

For this $\it l$ wemusthave,bythetriangle inequality,

$$
2 \pi | l | \leq \pi + | k | h _ { 0 } \| \omega \| ,
$$

so that in case $l \neq 0$

$$
{ \frac { 1 } { | k | } } \leq { \frac { h _ { 0 } \| \omega \| } { 2 \pi ( | l | - { \frac { 1 } { 2 } } ) } } \cdotp
$$

On the other hand, $l = 0$ yields

$$
\left| { \frac { 1 - e ^ { - i { \boldsymbol { k \cdot h } } \omega } } { h } } \right| \geq { \frac { 2 } { \pi } } | { \boldsymbol { k \cdot \omega } } | \geq { \frac { 2 } { \pi } } \gamma | { \boldsymbol { k } } | ^ { - \nu }
$$

which implies $h \notin Z ( h _ { 0 } ) .$ Hence, $h$ can bein $Z ( h _ { 0 } )$ only if there exist $k \in  { \mathbb { Z } ^ { d } }$ ， $k \neq 0$ andaninteger $l \neq 0$ such that

$$
\begin{array} { r c l } { \left| h - \displaystyle \frac { 2 \pi l } { | k \cdot \omega | } \right| } & { \le } & { \displaystyle \frac { \pi } { 2 } \frac { | h | } { | k \cdot \omega | } \frac { \gamma ^ { * } } { | k | ^ { \nu ^ { * } } } \le \frac { \pi } { 2 } | h | \frac { | k | ^ { \nu } } { \gamma } \frac { \gamma ^ { * } } { | k | ^ { \nu ^ { * } } } } \\ & { \le } & { \displaystyle \frac { \pi } { 2 } \frac { \gamma ^ { * } } { \gamma } | k | ^ { \nu + r - \nu ^ { * } } \left( \frac { \| \omega \| } { 2 \pi } \frac { 1 } { | l | - \frac { 1 } { 2 } } \right) ^ { r } h _ { 0 } ^ { r + 1 } . } \end{array}
$$

It follows that

$$
\mathrm { ~ e a s u r e } \left( Z ( h _ { 0 } ) \right) \le 2 \sum _ { k \ne 0 } \sum _ { l \ne 0 } \frac { \pi } { 2 } \frac { \gamma ^ { * } } { \gamma } \vert k \vert ^ { \nu + r - \nu ^ { * } } \left( \frac { \Vert \omega \Vert } { 2 \pi } \frac { 1 } { \vert l \vert - \frac { 1 } { 2 } } \right) ^ { r } h _ { 0 } ^ { r + 1 } ,
$$

which yields the stated result.

# X.7 Exercises

1. Let $R$ bea $d \times 2 d$ matrix of rank $d$ Show that there exists a symplectic $2 d \times 2 d$ matrix $A$ such that $R A = ( P , Q )$ with an invertible $d \times d$ matrix $P$

Hint.Consider first the case $d = 2$ and then reduce the general situation toa sequence of transformations for that case.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/8421e37479f80a2856f4be7f35fd5716a5ec19e6e99085765e41eb29c354ba4e.jpg)  
Fig.7.1.Numerically obtained eigenvalues(left pictures)and errors in theeigenvalues (right pictures)for the step sizes $h = 0 . 1$ (dotted）and $h = 0 . 0 5$ (solid line)

2.The transformation $( x , y ) \mapsto ( x , y + d ( x , y ) )$ issymplectic if and only if the partial derivatives of $d$ satisfy $d _ { x } = d _ { x } ^ { T }$ ， $d _ { y } = 0$

3.In the situation of Lemma 1.1,if $( F _ { 1 } , \ldots , F _ { d } , \bar { G } _ { 1 } , \ldots , \bar { G } _ { d } ) ^ { T }$ is another such symplectic transformation,then there existsa smooth function $W$ depending onlyon ${ \boldsymbol { x } } = ( x _ { 1 } , \dots , x _ { d } )$ such that, for $x _ { j } = F _ { j } ( p , q )$ ,

$$
\widetilde { G } _ { i } ( p , q ) - G _ { i } ( p , q ) = { \frac { \partial W } { \partial x _ { i } } } ( x ) .
$$

Hint.Use the previous exercise.

4.Show that every discrete subgroup of $\mathbb { R } ^ { d }$ isa grid,generated by $k \leq d$ linearly independent vectors.

Solution.See e.g.Arnold(1989),Sect.10D.

5.Show the following bound of the Lebesgue measure of non-diophantine frequencies (Arnold 1963):for any bounded domain $\Omega \subset \mathbb { R } ^ { d }$ ,

measure $\{ \omega \in \Omega ; \omega$ does not satisfy (2.4) with $\nu \geq d \} \leq C ( d , \varOmega ) \gamma .$

Hint.Fora fixed $k$ ,decompose $\omega = \omega _ { 0 } + \alpha k / | k |$ with $\boldsymbol { \omega } _ { 0 } \boldsymbol { \cdot } \boldsymbol { k } = 0$ .

6.Show that the eigenvalues $\lambda _ { j }$ of thematrix $L$ of the Toda system are first integrals in involution.

Hint.For $P _ { \lambda } = \operatorname* { d e t } ( \lambda I - L )$ ,show that $\{ P _ { \lambda } , P _ { \mu } \} = 0$ for all $\lambda , \mu$ .

7.Werepeat the experiment of Fig.1.3with the Stormer-Verlet scheme,where wekeep the initial values for the $q$ -variables,butchange theinitial values for the $p$ -variablesto $p _ { 1 } = p _ { 2 } = p _ { 3 } = 0 .$ The numerical results,given in Fig.7.1, arequalitativelydifferent from those in Fig.1.3.The errorsbehavemore like $h c ( t h )$ rather than $h ^ { 2 } c ( t )$ Wedo not understand this behaviour;do you?

8.Show that fora non-symplectic numerical method,thereisat worst quadratic error growthintimewhen it isapplied toanintegrable Hamiltoniansystem.

9.Consider anumerical integrator of order $p$ (i.e., $\varPhi _ { h } ( y ) = \varphi _ { h } ( y ) + \mathcal { O } ( h ^ { p + 1 } ) )$ , and assume that

$$
\Phi _ { h } ^ { \prime } ( y ) ^ { T } J \Phi _ { h } ^ { \prime } ( y ) = J + { \mathcal O } ( h ^ { q + 1 } )
$$

with $q > p$ ,whenthemethod isappliedtoaHamiltoniansystem.Prove that undertheassumptions ofTheorem 3.1 theglobal errorbehaves for $t = n h$ like

$$
y _ { n } - y ( t ) = \mathcal { O } ( t h ^ { p } ) + \mathcal { O } ( t ^ { 2 } h ^ { q } ) ,
$$

and the action variables like

$$
I ( y _ { n } ) - I ( y _ { 0 } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( t h ^ { q } ) .
$$

Remark.Methods satisfying theassumptions of this exercise are called pseudosymplectic of order $( p , q )$ (Aubry&Chartier 1998).Pseudo-symplectic methodsbehave like symplectic methods on time intervals of length $\mathcal { O } ( h ^ { p - q } )$

10.Using the theory ofB-series,in particularTheoremVI.7.4,derive the conditions for the coefficients of a Runge-Kutta method such that itis pseudo-symplectic oforder $p ( q )$ .Provethat there exist explicit,pseudo-symplectic Runge-Kutta methods of order $( 2 , 4 )$ with3 stages.
