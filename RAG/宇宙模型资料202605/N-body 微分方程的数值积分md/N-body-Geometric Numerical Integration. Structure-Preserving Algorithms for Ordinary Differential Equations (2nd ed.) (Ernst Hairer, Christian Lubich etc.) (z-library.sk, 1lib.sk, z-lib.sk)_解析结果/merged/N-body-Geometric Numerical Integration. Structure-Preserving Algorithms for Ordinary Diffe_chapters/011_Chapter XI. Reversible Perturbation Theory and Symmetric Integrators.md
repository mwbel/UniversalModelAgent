# Chapter XI. Reversible Perturbation Theory and Symmetric Integrators

Thereis a very close similarity between the behaviour of solutions of reversible systemsand that of Hamiltonian ones.

(M.B.Sevryuk 1986,p.3)

Numerical experiments indicate that symmetric methods applied to integrableand near-integrablereversible systemsshare similarpropertiesto symplectic methods appliedto(near-)integrable Hamiltonian systems:linear error growth,long-time near-conservation of first integrals,existence of invariant tori.The present chaptergivesa theoretical explanation of the good long-time behaviour ofsymmetric methods.Theresultsand techniques are largely analogous to those of theprevious chapter-theextent of theanalogymay indeedbe seenas the mostsurprisingfeature of this chapter.

# XI.1 Integrable Reversible Systems

Weconsider a system of differential equations ona domain of $\mathbb { R } ^ { m } \times \mathbb { R } ^ { n }$ ,

$$
\begin{array} { r c l } { { \dot { u } } } & { { = } } & { { f ( u , v ) } } \\ { { \dot { v } } } & { { = } } & { { g ( u , v ) , } } \end{array}
$$

which is reversible with respecttothe involution $( u , v ) \mapsto ( u , - v ) ;$ forall $( u , v )$ ,

$$
\begin{array} { r l r } { f ( u , - v ) } & { = } & { - f ( u , v ) } \\ { g ( u , - v ) } & { = } & { g ( u , v ) . } \end{array}
$$

From Sect.V.1 werecall that the time- $t$ flow $\varphi _ { t }$ ofareversible system isareversible map:

$$
\varphi _ { t } ( u , v ) = ( { \widehat u } , { \widehat v } ) \qquad \mathrm { i m p l i e s } \qquad \varphi _ { t } ^ { - 1 } ( u , - v ) = ( { \widehat u } , - { \widehat v } ) \ .
$$

A coordinate transform $u = \mu ( x , y )$ ， $v = \nu ( x , y )$ issaid topreserve reversibilityif therelations

$$
\begin{array} { r l r } { \mu ( x , - y ) } & { = } & { \mu ( x , y ) } \\ { \nu ( x , - y ) } & { = } & { - \nu ( x , y ) } \end{array}
$$

hold for all $( x , y ) .$ This implies that every reversible system（1.1）writtenin the new variables $( x , y )$ isagainreversible,and that every reversiblemap $( u , v ) \mapsto ( \widehat { u } , \widehat { v } )$ expressed in the variables $( x , y )$ again becomes a reversible map $( x , y ) \mapsto ( { \widehat { x } } , { \widehat { y } } )$ Conversely,(1.3) is necessary for these properties.

ForHamiltonian systems,complete integrability istiedto theexistenceofa symplectic transformation to action-angle variables;see Sect.X.1.Forreversible systems,we take the existence of a reversibility-preserving transformation to such variablesas the definition of integrability.

Definition1.1.Thesystem (1.1) iscalledanintegrablereversiblesystemif,for everypoint $( u _ { 0 } , v _ { 0 } ) \ \in \mathbb { R } ^ { m } \times \mathbb { R } ^ { n }$ in the domain of $( f , g )$ ,thereexist a function $\omega = ( \omega _ { 1 } , \ldots , \omega _ { n } ) : D \to \mathbb { R } ^ { n }$ andadiffeomorphism

$$
\psi = ( \mu , \nu ) : D \times \mathbb { T } ^ { n } \to U \subset \mathbb { R } ^ { m } \times \mathbb { R } ^ { n } : ( a , \theta ) \mapsto ( u , v )
$$

(with $D$ and $U$ open sets in $\mathbb { R } ^ { m }$ and $\mathbb { R } ^ { m } \times \mathbb { R } ^ { n }$ ,respectively,and $( u _ { 0 } , v _ { 0 } ) \in U )$ ， which preserves reversibility and transforms thesystem(1.1）to the form

$$
\begin{array} { l } { { \dot { a } ~ = ~ 0 } } \\ { { \dot { \theta } ~ = ~ \omega ( a ) . } } \end{array}
$$

Wespeak ofareal-analytic integrablereversible systemifallthe functionsappearinginthe above definition are real-analytic.

Example1.2 (MotioninaCentral Field).In ExamplesX.1.2andX.1.10we constructed action-angle variablesviaaseriesof transformations

$$
\left( \begin{array} { l } { q _ { 1 } , p _ { 2 } } \\ { p _ { 1 } , q _ { 2 } } \end{array} \right) \stackrel { ( { \bf X } , 1 . 5 ) } { \longrightarrow } \left( \begin{array} { l } { r , p _ { \varphi } } \\ { \varphi , p _ { r } } \end{array} \right) \stackrel { ( { \bf X } . 1 . 6 ) } { \longrightarrow } \left( \begin{array} { l } { H , L } \\ { y _ { 1 } , y _ { 2 } } \end{array} \right) \stackrel { ( { \bf X } . 1 . 1 5 ) } { \longrightarrow } \left( \begin{array} { l } { H , L } \\ { \theta _ { 1 } , \theta _ { 2 } } \end{array} \right) ~ .
$$

Itis easily verified that all these transformationspreservereversibility.They transform the reversible system

$$
\begin{array} { l } { { \dot { q } } _ { 1 } = p _ { 1 } , \quad { \dot { p } } _ { 2 } = - q _ { 2 } V ^ { \prime } ( r ) / r } \\ { { \dot { q } } _ { 2 } = p _ { 2 } , \quad { \dot { p } } _ { 1 } = - q _ { 1 } V ^ { \prime } ( r ) / r } \end{array}
$$

(with $r = \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } )$ to the form

$$
\begin{array} { l } { { \displaystyle { \dot { H } } = 0 , \quad { \dot { L } } = 0 } } \\ { { \displaystyle { \dot { \theta } _ { 1 } } = { \frac { 2 \pi } { T } } , \quad { \dot { \theta } _ { 2 } } = { \frac { \varPhi } { T } } } } \end{array}
$$

with $T = T ( H , L )$ and $\varPhi = \varPhi ( H , L )$ given by(X.1.12)and(X.1.13).

As the following result shows,itis not incidental that theabove transformations preserve reversibility.

Theorem1.3.InthesituationoftheArnold-Liouville theorem,TheoremX.1.6,let the first integrals $F _ { 1 } , \ldots , F _ { d }$ ofthecompletely integrableHamiltonian systembe suchthatall $F _ { i }$ areeven functions ofthe second halfofthe arguments:

$$
F _ { i } ( u , v ) = F _ { i } ( u , - v ) \qquad ( i = 1 , \ldots , d ) .
$$

Suppose that $\partial { \cal F } _ { 1 } / \partial u , \ldots , \partial { \cal F } _ { d } / \partial u$ are linearly independent everywhere (on $\bigcup \{ M _ { x } : x \in B \}$ )except possibly ona set that has no interior points.Further, assume thatforevery $x \in B$ there existsu such that $( u , 0 ) \in M _ { x } .$ Then,thetransformation $\psi : ( a , \theta ) \mapsto ( u , v )$ toaction-angle variablesas given by Theorem X.1.6 preservesreversibility.

Proof.Theresult followsby tracing theproofsofLemmaX.1.1,Theorem X.1.4 and Theorem X.1.6.

（a）For $\boldsymbol { F } _ { i }$ satisfying（1.7）and atpointswhere the Jacobianmatrix $\partial F / \partial u$ is invertible,the construction of the local symplectic transformation $\ell = ( F _ { 1 } , \dots , F _ { d } ,$ $G _ { 1 } , \dots , G _ { d } ) : ( u , v ) \mapsto ( x , y )$ shows that the generating function $S ( x , v )$ becomes oddin $\upsilon$ when the integration constant is chosen such that $S ( x , 0 ) = 0 \quad$ By(X.1.4）， this implies that $\ell$ preserves reversibility.Acontinuity argument used together with the essential uniqueness of the transformation $\ell$ (seeExercise X.3)does away with the exceptional pointswhere $\partial F / \partial u$ issingular.

(b)In Theorem X.1.4,the construction of $e ( x , y ) = \varphi _ { y } ( \ell ^ { - 1 } ( x , 0 ) ) = : ( u , v )$ is such that

$$
e ( x , - y ) \equiv \varphi _ { - y } ( \ell ^ { - 1 } ( x , 0 ) ) = ( u , - v ) .
$$

This holds because by assumption the reference point on $M _ { x }$ can be chosen as $\ell ^ { - 1 } ( x , 0 ) \ = \ ( u _ { 0 } , 0 )$ forsome $u _ { 0 }$ ,and because $\varphi _ { \pm , y }$ isthe time $\pm 1$ fow of the Hamiltonian system with Hamiltonian $y _ { 1 } F _ { 1 } + \ldots + y _ { d } F _ { d }$ Condition（1.7） implies thatthis isareversible system,which in turn yieldsthat $e$ preserves reversibilityas stated above.

(c)The transformation in the proof of Theorem X.1.6 is of the form $a = w ( x )$ ， $y = W ( x ) \theta$ (with invertible $W ( x ) = w ^ { \prime } ( x ) )$ and hence preserves reversibility. $\sqsupset$

Example 1.4.We now present an example with onedegree of freedomwhere Theorem 1.3does not apply.In fact,all conditions are satisfied except that for some $\boldsymbol { x }$ there is no $u$ such that $( u , 0 ) \in M _ { x }$ .Weconsider the Hamiltonian

$$
H ( u , v ) = ( v ^ { 2 } - 1 ) ^ { 2 } + \int _ { 0 } ^ { u } s ( s + 1 ) ^ { 4 } d s .
$$

Its level sets are shown in the picture to the right.Forenergy values such that the level curve does not intersect the $_ { u }$ -axis,Theorem1.3does notapply even though $H ( u , v )$ satisfies (1.7). For these energy values the system isan integrable Hamiltoniansystem,but not an integrablereversible system.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/0dd6e6fd9da430fd4533c23ac19cf5e22348052731d2a069689b4de548818007.jpg)

Example1.5(Motion in a Central Field,Continued).All the assumptions of Theorem 1.3are satisfied for $F _ { 1 } = H$ ， $F _ { 2 } = L = p _ { 1 } q _ { 2 } - p _ { 2 } q _ { 1 }$ if we take the symplectic coordinates $\boldsymbol { u } = ( q _ { 1 } , p _ { 2 } )$ and $\boldsymbol { v } = ( - p _ { 1 } , q _ { 2 } )$ .

The condition(1.7)is also satisfied with $F _ { 1 } = H$ , $F _ { 2 } = L ^ { 2 }$ $L \neq 0$ asalways) forthe choices $u = ( p _ { 1 } , p _ { 2 } )$ and $v = ( q _ { 1 } , q _ { 2 } )$ ,or $\boldsymbol { u } = \left( q _ { 1 } , q _ { 2 } \right)$ and $v = ( - p _ { 1 } , - p _ { 2 } )$ However,in these situations,Theorem 1.3cannotbeapplied,because theredoesnot exist $u$ such that $( u , 0 ) \in M _ { x }$ .

Example1.6 (Toda Lattice).Consider the Toda lattice of Sect.X.1.5.The eigenvalues of the matrix $L$ arefirst integralsin involution.With the symplectic coordinates $( u , v ) = ( q , - p )$ theHamiltonian system corresponding to(X.1.17） satisfies thereversibility conditions(1.2).However,since $v _ { 1 } + \ldots + v _ { n }$ isa first integral of this system,it is not possible to connect $( u , v )$ with $( u , - v )$ ona level set $M _ { x }$ ,and Theorem1.3cannot be applied.

Fortunately,ascan beseenin Fig.1.1,the Toda lattice containsmany more symmetries.With periodic boundary conditions itis,for example, $\rho$ -reversible(i.e., $\rho f ( y ) = - f ( \rho y )$ , $y = ( p , q ) ^ { \tau }$ ,see the discussion in Chap.V)with

$$
\rho = { \binom { S } { 0 } } \quad { \stackrel { 0 } { = } } { S } \quad \quad { \bar { S } } = { \left( \begin{array} { l l } { \quad } & { 1 } \\ { 1 } & { } \end{array} \right) } ,
$$

where $S$ inversesthe components ofavector.To bringthe system tothe form(1.1） withavector field satisfying（1.2）,we transform $S$ (and hence $\rho$ ）todiagonal form andcollect the variables corresponding to the eigenvalues $+ \perp$ and $- 1$ in $u$ and $\boldsymbol { v }$ , respectively(see Exercise1）.This givesthe（symplectic) coordinates

$$
\begin{array} { r c l } { { u _ { k } ~ = ~ \frac { 1 } { \sqrt { 2 } } \Big ( p _ { k } + p _ { n - k + 1 } \Big ) , ~ } } & { { u _ { n - k + 1 } ~ = ~ \frac { 1 } { \sqrt { 2 } } \Big ( q _ { k } - q _ { n - k + 1 } \Big ) , } } \\ { { v _ { k } ~ = ~ \frac { 1 } { \sqrt { 2 } } \Big ( q _ { k } + q _ { n - k + 1 } \Big ) , ~ } } & { { v _ { n - k + 1 } ~ \equiv ~ \frac { 1 } { \sqrt { 2 } } \Big ( p _ { n - k + 1 } - p _ { k } \Big ) , } } \end{array}
$$

for $k = 1 , \ldots , n / 2$ (if $n$ is even; for odd $n = 2 \ell + 1$ ,（1.8)holds for $k = 1 , \ldots , \ell$ and in addition we have $u _ { \ell + 1 } = p _ { \ell + 1 }$ and $v _ { \ell + 1 } = q _ { \ell + 1 }$ ).

In the following we restrict our considerations to the case $n = 3$ ,andwe show thatallassumptions of Theorem 1.3are satisfied,so thatwe havean integrable reversible system.For $n = 3$ ,thenewvariablesare

$$
\begin{array} { l l l l } { { u _ { 1 } = \displaystyle \frac { 1 } { \sqrt { 2 } } \Big ( p _ { 1 } + p _ { 3 } \Big ) , } } & { { \quad u _ { 2 } = p _ { 2 } , } } & { { \quad u _ { 3 } = \displaystyle \frac { 1 } { \sqrt { 2 } } \Big ( q _ { 1 } - q _ { 3 } \Big ) , } } \\ { { v _ { 1 } = \displaystyle \frac { 1 } { \sqrt { 2 } } \Big ( q _ { 1 } + q _ { 3 } \Big ) , } } & { { \quad v _ { 2 } = q _ { 2 } , } } & { { \quad v _ { 3 } = \displaystyle \frac { 1 } { \sqrt { 2 } } \Big ( p _ { 3 } - p _ { 1 } \Big ) , } } \end{array}
$$

and the expressions $a _ { k }$ and $b _ { k }$ of Sect.X.1.5become

$$
\begin{array} { l l l } { { a _ { 1 } = - { \displaystyle \frac { 1 } { 2 \sqrt 2 } } \Big ( u _ { 1 } - v _ { 3 } \Big ) , } } & { { } } & { { b _ { 1 } = { \displaystyle \frac { 1 } { 2 } } \exp \Big ( { \textstyle \frac { 1 } { 2 } } \Big ( { \textstyle \frac { 1 } { \sqrt 2 } } \big ( v _ { 1 } + u _ { 3 } \big ) - v _ { 2 } \Big ) \Big ) , } } \\ { { a _ { 2 } = - { \displaystyle \frac { 1 } { 2 } } u _ { 2 } , } } & { { } } & { { b _ { 2 } = { \displaystyle \frac { 1 } { 2 } } \exp \Big ( { \textstyle \frac { 1 } { 2 } } \Big ( v _ { 2 } - { \textstyle \frac { 1 } { \sqrt 2 } } \big ( v _ { 1 } - u _ { 3 } \big ) \Big ) \Big ) , } } \\ { { a _ { 3 } = - { \displaystyle \frac { 1 } { 2 \sqrt 2 } } \Big ( u _ { 1 } + v _ { 3 } \Big ) , } } & { { } } & { { b _ { 3 } = { \displaystyle \frac { 1 } { 2 } } \exp \Big ( { \textstyle \frac { 1 } { \sqrt 2 } } u _ { 3 } \Big ) . } } \end{array}
$$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/096362ac9250b877cbcde63cb95184127a94324a9663bf0f487b117c9274575b.jpg)  
Fig.1.1.Three projections of the solution of the Toda lattice equations $( n = 3$ withinitial valuesasin Fig.X.1.3

One sees that $b _ { 1 } ^ { 2 } + b _ { 2 } ^ { 2 }$ and $a _ { 1 } b _ { 2 } ^ { 2 } + a _ { 3 } b _ { 1 } ^ { 2 }$ are even functions of $v _ { \cdot }$ so that all coefficients ofthecharacteristic polynomial of thematrix $L$

$$
\begin{array} { c } { { \langle \lambda \rangle = - \lambda ^ { 3 } + ( a _ { 1 } + a _ { 2 } + a _ { 3 } ) \lambda ^ { 2 } - ( a _ { 1 } a _ { 2 } + a _ { 2 } a _ { 3 } + a _ { 3 } a _ { 1 } - b _ { 1 } ^ { 2 } - b _ { 2 } ^ { 2 } - b _ { 3 } ^ { 2 } ) \lambda + } } \\ { { { } } } \\ { { ( a _ { 1 } a _ { 2 } a _ { 3 } - a _ { 1 } b _ { 2 } ^ { 2 } - a _ { 2 } b _ { 3 } ^ { 2 } - a _ { 3 } b _ { 1 } ^ { 2 } + 2 b _ { 1 } b _ { 2 } b _ { 3 } ) . } } \end{array}
$$

are even in $\boldsymbol { v }$ .This implies that also the eigenvalues of $L$ areeven functions of $\boldsymbol { v }$ ,so that（1.7）is satisfied.

It remains to prove that for fixed $x$ ,i.e.,for given real eigenvalues of $\mathcal { L }$ ,thepoint $( u _ { 0 } , v _ { 0 } )$ corresponding to $p ( 0 ) , q ( 0 )$ can be connected with an element of the form $( u , 0 ) \in \mathbb { R } ^ { 6 }$ without leaving the level set $M _ { x }$ Equivalently,we haveto find such a path for which the corresponding coefficients of the characteristic polynomial $\chi ( \lambda )$ takegiven values.For given $v ( t )$ thisyields a system of three nonlinear equations for $u ( t ) \in \mathbb { R } ^ { 3 }$ .For the eigenvalues corresponding to the initial values $p ( 0 ) , q ( 0 )$ used inFig.X.1.3,we put $v ( t ) = v _ { 0 } t$ for $1 \geq t \geq 0$ andwecheck numericallywith apath-followingalgorithm that such a connection is possible.

Example1.7 (Rigid Body Equations on theUnit Sphere).Wereconsider an examplethat hasaccompaniedusall theway through Chapters IV,V,and VII.5:the rigid body equations(IV.1.4),here considered asdifferential equations on theunit sphere.Weassume $I _ { 3 } < I _ { 1 } , I _ { 2 }$ forthe inertia,which implies thatany solution startingwith $y _ { 3 } ( 0 ) > 0$ willhave $y _ { 3 } ( t ) > 0$ forall $t$ We consider the equations in the neighbourhood of such a solution.We can then choose $u = y _ { 1 }$ ， $v = y _ { 2 }$ ascoordinates on the upper half-sphere $\{ y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1 , y _ { 3 } > 0 \} .$ This gives the reversible system

$$
\begin{array} { r } { \dot { u } \ = \ \left. a _ { 1 } v \sqrt { 1 - { u ^ { 2 } } - v ^ { 2 } } \right. } \\ { \dot { v } \ = \ \left. a _ { 2 } u \sqrt { 1 - { u ^ { 2 } } - v ^ { 2 } } \right. } \end{array}
$$

with $a _ { 1 } = ( I _ { 2 } - I _ { 3 } ) / I _ { 2 } I _ { 3 } > 0$ and $a _ { 2 } = ( I _ { 3 } - I _ { 1 } ) / I _ { 3 } I _ { 1 } < 0$ ,which has $H =$ $u ^ { 2 } / I _ { 1 } + v ^ { 2 } / I _ { 2 } + ( 1 - u ^ { 2 } - v ^ { 2 } ) / I _ { 3 } = a _ { 2 } u ^ { 2 } - a _ { 1 } v ^ { 2 } + I _ { 3 } ^ { - 1 }$ as an invariant.We introduce polar coordinates $u = r \cos \varphi , v = r \sin \varphi$ andexpress $r$ asa function of $H$ and $\varphi$ :

$$
r = \sqrt { \frac { I _ { 3 } ^ { - 1 } - H } { a _ { 1 } \sin ^ { 2 } \varphi - a _ { 2 } \cos ^ { 2 } \varphi } } .
$$

This leaves us with differential equations

$$
\dot { H } = 0 , \dot { \varphi } = \gamma ( H , \varphi ) ,
$$

where $\gamma$ is even in $\varphi$ and has no zeros.The timeneeded torunthroughanangle $\varphi$ is

$$
\tau ( H , \varphi ) = \int _ { 0 } ^ { \varphi } \frac { 1 } { \gamma ( H , \phi ) } d \phi , \qquad \mathrm { a n d } \qquad \omega ( H ) = \frac { 2 \pi } { \tau ( H , 2 \pi ) }
$$

is the frequency.With $\theta = \omega ( H ) \tau ( H , \varphi )$ we then have

$$
\dot { H } = 0 , \dot { \theta } = \omega ( H ) .
$$

The transformation from $( u , v )$ in the open unit disc (except the origin） to $( H , \theta ) \in$ $( 0 , I _ { 3 } ^ { - 1 } ) \times \mathbb { T }$ isadiffeomorphism that preservesreversibility.This shows that the rigidbodyequations(1.9)arean integrablereversiblesystem.

Example1.8(Rigid Body Equations in $\mathbb { R } ^ { 3 }$ ).Wenow considerthe rigid body equations(IV.1.4） in the ambient space $\mathbb { R } ^ { 3 }$ ,rather than on the unit sphere.The system then has the invariants $H = y _ { 1 } ^ { 2 } / I _ { 1 } + y _ { 2 } ^ { 2 } / I _ { 2 } + y _ { 3 } ^ { 2 } / I _ { 3 }$ and $K = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ , and itis reversible with respect to thepartition $u \ = \ ( y _ { 1 } , y _ { 3 } )$ and $\ v \ = \ y _ { 2 }$ Inthe case $I _ { 3 } ~ < ~ I _ { 1 } , I _ { 2 }$ we can again restrict our attention to $y _ { 3 } > 0$ Wethen write $y _ { 3 } = \sqrt { K - y _ { 1 } ^ { 2 } - y _ { 2 } ^ { 2 } }$ and introduce polar coordinates $y _ { 1 } = r \cos \varphi$ , $y _ { 2 } = r \sin \varphi$ Asabove,we express $\tau$ asa function of $H , K$ and $\varphi$ (this just requires replacing $I _ { 3 } ^ { - 1 }$ with $K / I _ { 3 }$ in theabove formula for $r$ )and weobtaindifferentialequations

$$
\dot { H } = 0 , ~ \dot { K } = 0 , ~ \dot { \varphi } = \gamma ( H , K , \varphi )
$$

with $\gamma$ evenin $\varphi$ and without zeros.In the sameway as above,this is transformed to

$$
\dot { H } = 0 , \quad \dot { K } = 0 , \quad \dot { \theta } = \omega ( H , K ) .
$$

The transformation $( ( y _ { 1 } , y _ { 3 } ) , y _ { 2 } ) \mapsto ( ( H , K ) , \theta )$ preservesreversibility.The rigid body equations (IV.1.4)are thusan integrablereversible system.Note that this time the dimensions differ.

# XI.2Transformationsin Reversible Perturbation Theory

We consider perturbations of an integrable reversible system such that the perturbed systemisstill reversible.Thistakes the form

$$
\begin{array} { r } { \dot { a } \ = \qquad \varepsilon r ( a , \theta ) } \\ { \dot { \theta } \ = \ \omega ( a ) + \varepsilon \rho ( a , \theta ) } \end{array}
$$

where $\varepsilon$ isa small parameter,and $r$ is an odd function of $\theta$ and $\rho$ is an even function of $\theta$ :

$$
\begin{array} { r l r } { r ( a , - \theta ) } & { = } & { - r ( a , \theta ) } \\ { \rho ( a , - \theta ) } & { = } & { \rho ( a , \theta ) . } \end{array}
$$

Similar to Sect.X.2 for Hamiltonian perturbation theory,we study coordinate transformations that change(2.1） to reversible systemswhich $-$ invarious ways-look closer toan integrable systeminaction-anglevariablesthan(2.1).

# XI.2.1 The Basic Scheme of Reversible Perturbation Theory

We look foratransformation between neighbourhoods of $\{ a _ { 0 } \} \times \mathbb { T } ^ { n }$ ，

$$
\begin{array} { l } { { a = b + \varepsilon s ( b , \varphi ) } } \\ { { { \theta = \varphi + \varepsilon \sigma ( b , \varphi ) , } } } \end{array}
$$

which preserves reversibility and hence has $s$ evenin $\boldsymbol { \varphi }$ and $O$ oddin $\varphi$ ,such that thetransformed systemisof theform

$$
\begin{array} { l } { \dot { b } = \mathcal { O } ( \varepsilon ^ { 2 } ) } \\ { \dot { \varphi } = \omega ( b ) + \varepsilon \mu ( b ) + \mathcal { O } ( \varepsilon ^ { 2 } ) . } \end{array}
$$

Inserting(2.3) into (2.1）gives the system

$$
\left\{ \left( { \begin{array} { c c } { I } & { 0 } \\ { 0 } & { I } \end{array} } \right) + \varepsilon \left( { \begin{array} { c c } { \partial s / \partial b } & { \partial s / \partial \varphi } \\ { \partial \sigma / \partial b } & { \partial \sigma / \partial \varphi } \end{array} } \right) \right\} \left( { \begin{array} { c } { b } \\ { \dot { \varphi } } \end{array} } \right) = \left( { \begin{array} { c } { \varepsilon r ( a , \theta ) } \\ { \omega ( a ) + \varepsilon \rho ( a , \theta ) } \end{array} } \right)
$$

with $( a , \theta )$ from (2.3).Inverting the matrix on the left-hand side and expanding in powers of $\boldsymbol { \varepsilon }$ ,itisseen that (2.4) requires that $s , \sigma$ satisfy the equations

$$
\begin{array} { l } { { \displaystyle \frac { \partial s } { \partial \varphi } ( b , \varphi ) \omega ( b ) = r ( b , \varphi ) } } \\ { { \displaystyle \frac { \partial \sigma } { \partial \varphi } ( b , \varphi ) \omega ( b ) = \rho ( b , \varphi ) + \omega ^ { \prime } ( b ) s ( b , \varphi ) - \mu ( b ) . } } \end{array}
$$

Anecessary condition for the solvability of(2.5) is that the angular average of $r$ vanishes:

$$
{ \overline { { r } } } ( b ) = 0 \ , \qquad { \mathrm { w h e r e } } \quad { \overline { { r } } } ( b ) = { \frac { 1 } { ( 2 \pi ) ^ { n } } } \int _ { \mathbb { T } ^ { n } } r ( b , \varphi ) d \varphi \ .
$$

In the Hamiltonian case this condition was satisfied because $T$ wasagradient with respectto $\boldsymbol { \varphi }$ .Here,in thereversible case,thisissatisfied because $r$ isan odd function of $\varphi$ .

If(2.7) holds,then (2.5)can be solved by Fourier series expansion in the same wayaswe solved(X.2.2),provided that the frequencies $\omega _ { 1 } ( b ) , \ldots , \omega _ { n } ( b )$ arenonresonant.Of course,there is again the same problem of small denominators as in the Hamiltonian case.Equations (2.6) are solved in the same way as (2.5),upon setting

$$
\mu ( b ) = \overline { { { \rho } } } ( b ) + \omega ^ { \prime } ( b ) \overline { { { s } } } ( b ) . 
$$

Since $\tau$ is odd in $\varphi$ ,the solution $s$ of（2.5） becomes even in $\varphi$ Itisdetermined uniquely onlyup toa constant:we are still freeto choose the angular average ${ \overline { { s } } } ( b )$ . If $\omega ^ { \prime } ( b )$ hasrank $_ { n }$ ,wemay actually choose ${ \overline { { s } } } ( b )$ such that $\mu ( b ) = 0$ results from (2.8).Since theright-hand side of(2.6)is even in $\varphi$ ,thesolution $o$ of(2.6) becomes odd in $\varphi$ ifwe choose $\overline { { \sigma } } ( b ) = 0$ .

# XI.2.2Reversible Perturbation Series

The above construction extends to arbitrary finite order in $\varepsilon$ .The transformation is now sought forin the form

$$
\begin{array} { l } { { a = b + \varepsilon s _ { 1 } ( b , \varphi ) + \varepsilon ^ { 2 } s _ { 2 } ( b , \varphi ) + . . . + \varepsilon ^ { N - 1 } s _ { N - 1 } ( b , \varphi ) } } \\ { { \nonumber } } \\ { { \theta = \varphi + \varepsilon \sigma _ { 1 } ( b , \varphi ) + \varepsilon ^ { 2 } \sigma _ { 2 } ( b , \varphi ) + . . . + \varepsilon ^ { N - 1 } \sigma _ { N - 1 } ( b , \varphi ) } } \end{array}
$$

with $s _ { j }$ evenin $\varphi$ and $\sigma _ { j }$ odd in $\varphi$ to preserve reversibility.This transformation is to be chosen such that the system in the new variables is of the form

$$
\begin{array} { r l r } { \dot { b } } & { = } & { \varepsilon ^ { N } r _ { N } ( b , \varphi ) } \\ { \dot { \varphi } } & { = } & { \omega _ { \varepsilon , N } ( b ) + \varepsilon ^ { N } \rho _ { N } ( b , \varphi ) } \end{array}
$$

with $\omega _ { \varepsilon , N } ( b ) = \omega ( b ) + \varepsilon \mu _ { 1 } ( b ) + \ldots + \varepsilon ^ { N - 1 } \mu _ { N - 1 } ( b )$ andwith $r _ { N } ( b , \varphi )$ odd in $\varphi$ and $\rho _ { N } ( b , \varphi )$ evenin $\varphi$ ,andwithall these functions bounded independentlyof $\varepsilon$ .

Inserting the transformation into (2.1）and expandingin powers of $\boldsymbol { \varepsilon }$ ,itisseen that the functions $s _ { j }$ and $\sigma _ { j }$ must satisfy equations of the form of(2.5),(2.6):

$$
\begin{array} { l } { { \displaystyle \frac { \partial s _ { j } } { \partial \varphi } ( b , \varphi ) \omega ( b ) = p _ { j } ( b , \varphi ) } } \\ { { \displaystyle \frac { \partial \sigma _ { j } } { \partial \varphi } ( b , \varphi ) \omega ( b ) = \pi _ { j } ( b , \varphi ) + \omega ^ { \prime } ( b ) s _ { j } ( b , \varphi ) - \mu _ { j } ( b ) } } \end{array}
$$

where $p _ { j } , \pi _ { j }$ aregiven byexpressions thatdepend linearly on higher-orderderivatives of $r , \rho$ and polynomially on the functions $s _ { i } , \sigma _ { i }$ with $\textit { i } < \textit { j }$ and on their first-orderderivatives.Using therules

$$
{ \left( \begin{array} { l l } { \operatorname { e v e n } } & { \operatorname { o d d } } \\ { \operatorname { o d d } } & { \operatorname { e v e n } } \end{array} \right) } { \left( \begin{array} { l } { \operatorname { o d d } } \\ { \operatorname { e v e n } } \end{array} \right) } = { \left( \begin{array} { l } { \operatorname { o d d } } \\ { \operatorname { e v e n } } \end{array} \right) }
$$

and

$$
{ \frac { \partial \mathrm { e v e n } } { \partial \varphi } } = \mathrm { o d d } \ , \qquad { \frac { \partial \mathrm { o d d } } { \partial \varphi } } = \mathrm { e v e n } \ ,
$$

itis found that $p _ { j }$ is odd in $\varphi$ and $\pi _ { j }$ isevenin $\varphi$ forall $\jmath$ Fornon-resonant frequencies $\omega ( b )$ ,theequations (2.11),(2.12)can thereforebe solved with $s _ { j }$ even in $\varphi$ , $\sigma _ { j }$ oddin $\varphi$ .If $\omega ^ { \prime } ( b )$ is invertible,we can obtain $\mu _ { j } ( b ) = 0$ forall $j$ .

Beyond these formal calculations,there is the following reversible analogue of LemmaX.2.1in theHamiltoniancase.Thisresult is obtained bythe same“ultravioletcut-off”argumentas the earlierresult.

Lemma2.1.Lettheright-hand sidefunctionsof(2.1) bereal-analytic inaneighbourhoodof $\{ b ^ { * } \} \times \mathbb { T } ^ { n }$ and satisfy(2.2).Suppose that $\omega ( b ^ { * } )$ satisfies the diophantine condition (X.2.4).Forany fixed $N \geq 2$ ,thereare positive constants $\varepsilon _ { 0 } , c , C$ suchthat the following holds for $\varepsilon \ \leq \ \varepsilon _ { 0 }$ ：thereexistsareal-analytic reversibility-preservingchange of coordinates $( a , \theta ) \mapsto ( b , \varphi )$ such that every solution $( b ( t ) , \varphi ( t ) )$ oftheperturbed systemin the new coordinates,startingwith $\lVert b ( 0 ) - b ^ { * } \rVert \leq c \lvert \log \varepsilon \rvert ^ { - \nu - 1 } ,$ satisfies

$$
\begin{array} { r l } & { \| b ( t ) - b ( 0 ) \| \le C t \varepsilon ^ { N } ~ f o r ~ t \le \varepsilon ^ { - N + 1 } \mathrm { , } } \\ & { \| \varphi ( t ) - \omega _ { \varepsilon , N } ( b ( 0 ) ) t - \varphi ( 0 ) \| \le C ( t ^ { 2 } + t | \log \varepsilon | ^ { \nu + 1 } ) \varepsilon ^ { N } ~ f o r } \end{array}
$$

Moreover,thetransformationis $\mathcal { O } ( \varepsilon )$ -closetotheidentity: $\| ( a , \theta ) - ( b , \varphi ) \| \leq C \varepsilon$ holdsfor $( a , \theta )$ and $( \boldsymbol { b } , \varphi )$ relatedbytheabovecoordinate transform,for $\vert \vert b - b ^ { \ast } \vert \vert \leq$ $c | \log \varepsilon | ^ { - \nu - 1 }$ andfor $\varphi$ inan $\varepsilon$ -independentcomplexneighbourhoodof $\mathbb { T } ^ { n }$ ,

Theconstants $\varepsilon _ { 0 } , c , C$ dependon $N , n , \gamma , \nu$ and on bounds of $\boldsymbol { \omega }$ , $r _ { i }$ , $\rho$ onacomplexneighbourhoodof $\{ b ^ { * } \} \times \mathbb { T } ^ { n }$ □

Theequations determining the coefficient functions of the perturbation series areoftheform towhichLemmaX.4.1applies.Therefore,that lemmaisagain the tool for estimating the terms in theperturbation series,similarto Sect.X.4.1.This yieldsareversibleanalogue ofTheoremX.4.4 showingnear-invariance of tori (up toexponentiallysmall termsin anegativepower of $\varepsilon$ overtimeintervalsthatare exponentially large in anegative power of $\varepsilon$ ,with the same exponents $\alpha , \beta$ asin Theorem X.4.4.

# XI.2.3ReversibleKAM Theory

Foranintegrablereversible system,justas foran integrableHamiltonian system, thephase space is foliated into invariant tori on which the flow isconditionally periodic.We fix one such torus $\{ a = a ^ { * } , \theta \in \mathbb { T } ^ { n } \}$ with diophantine frequencies $\omega _ { 1 } , \ldots , \omega _ { n } .$ Forconvenience we may assume $a ^ { * } = 0 \in \mathbb { R } ^ { m } .$ Thistorus is invariant under the flow of systems of the form $\dot { a } = \mathcal { O } ( \| a \| ^ { 2 } )$ , $\theta = \omega + O ( \left. a \right. )$ ,orwritten more explicitly,

$$
\begin{array} { l } { \dot { \boldsymbol { a } } ~ = ~ \frac { 1 } { 2 } \boldsymbol { a } ^ { T } \boldsymbol { K } ( \boldsymbol { a } , \theta ) \boldsymbol { a } } \\ { \dot { \theta } ~ = ~ \omega + M ( \boldsymbol { a } , \theta ) \boldsymbol { a } . } \end{array}
$$

Here, $K = [ K _ { 1 } , \ldots , K _ { m } ]$ where each $K _ { i } ( a , \theta )$ isasymmetric $m \times m$ matrix, and $M ( a , \theta )$ isan $n \times m$ matrix.Thefirst equation isto be interpreted as $\dot { a } _ { i } =$ $\frac { 1 } { 2 } a ^ { 2 } K _ { i } ( a , \theta ) a$ for the components $i = 1 , \ldots , m$ Consider now aperturbation of thissystem:

$$
\begin{array} { l } { \dot { \alpha } \ = \ \frac 1 2 { a } ^ { T } K ( { a } , \theta ) { a } + \varepsilon r ( { a } , \theta ) } \\ { \dot { \theta } \ = \ \omega + M ( { a } , \theta ) { a } + \varepsilon \rho ( { a } , \theta ) . } \end{array}
$$

For the reversible case,i.e.,for $K$ and $r$ oddin $\theta$ andfor $M$ and $\rho$ evenin $\theta$ , weconstruct a sequence of reversibility-preserving transformations in the spiritof Kolmogorov's transformation of Sect.X.2.3,which transform(2.14） back to the form (2.13) in the newvariables,showing the persistence of an invariant torus with frequencies $\omega _ { i }$ under small reversible perturbations ofthe system.This holdsagain under the diophantine condition (X.2.4）on $\boldsymbol { \omega }$ andadditionally under the condition that the angular average $M _ { 0 }$ of $M$ at $a = 0$ hasrank $\textit { n }$ Aresult of this typeareversibleKAMtheorem $-$ wasshownbyMoser（1973）,Chap.V,inadifferent setting.See also Sevryuk(1986) for further results in that direction.

We look fora transformation of the form

$$
\begin{array} { l } { a \ = \ b + \varepsilon \Big ( s ( \varphi ) + S ( \varphi ) b \Big ) } \\ { \theta \ = \ \varphi + \varepsilon \sigma ( \varphi ) } \end{array}
$$

with an $m \times m$ matrix $S ( \varphi )$ Preservingreversibility requires that $s$ and $S$ areeven functions and $\sigma$ is odd.Higher-order terms in $b$ playno roleand are therefore omitted fromthe beginning.We insert this into(2.14) and obtain

$$
\begin{array} { r l } { \dot { b } ~ = ~ \frac { 1 } { 2 } \dot { b } ^ { T } K ( b , \varphi ) b + \varepsilon \Big \{ { r ( 0 , \varphi ) - \frac { \partial s } { \partial \varphi } ( \varphi ) \omega } } & { } \\ & { \mathrm { ~ \ } + \frac { \partial r } { \partial b } ( 0 , \varphi ) b - \frac { \partial s } { \partial \varphi } ( \varphi ) M ( 0 , \varphi ) b - \frac { \partial } { \partial \varphi } \Big ( S ( \varphi ) b \Big ) \omega + s ( \varphi ) ^ { T } K ( 0 , \varphi ) b \Big \} } \\ & { \mathrm { ~ \ } + { \mathcal O } ( \varepsilon ^ { 2 } ) + { \mathcal O } ( \varepsilon \| b \| ^ { 2 } ) } \end{array}
$$

$$
\begin{array} { l } { \displaystyle \dot { \varphi } ~ = ~ \omega + M ( b , \varphi ) b } \\ { \displaystyle \quad + \varepsilon \Big \{ \rho ( 0 , \varphi ) - \frac { \partial \sigma } { \partial \varphi } ( \varphi ) \omega + M ( 0 , \varphi ) s ( \varphi ) \Big \} + \mathcal { O } ( \varepsilon ^ { 2 } ) + \mathcal { O } ( \varepsilon \| b \| ) . } \end{array}
$$

Werequire that the terms in curly brackets vanish.This holds if the following equationsare satisfied (the last equation is written component-wise for notational clarity）:

$$
\begin{array} { l } { \displaystyle \frac { \partial s } { \partial \varphi } ( \varphi ) \boldsymbol { \omega } = r ( 0 , \varphi ) } \\ { \displaystyle \frac { \partial \boldsymbol { \sigma } } { \partial \varphi } ( \varphi ) \boldsymbol { \omega } = \rho ( 0 , \varphi ) + M ( 0 , \varphi ) s ( \varphi ) } \\ { \displaystyle \frac { \partial S _ { i j } } { \partial \varphi } ( \varphi ) \boldsymbol { \omega } = \frac { \partial r _ { i } } { \partial b _ { j } } ( \varphi ) - \sum _ { k } \frac { \partial s _ { i } } { \partial \varphi _ { k } } ( \varphi ) M _ { k j } ( 0 , \varphi ) + \sum _ { k } s _ { k } ( \varphi ) K _ { i , k j } ( 0 , \varphi ) . } \end{array}
$$

Since $r$ is odd in,the first equation can be solved for $s$ evenin $4$ ,uniquelyuptoa constant,the angularaverage $\overline { s }$ Since theangularaverage of $M$ is assumed to be of full rank $n , { \overline { { s } } }$ can be chosen such that the angular average of the right-hand side of the equation for $o$ becomes zero.Since theright-hand side is even,the equation can then be solved uniquely for an odd $o$ .The equations for $S$ havean odd right-hand side and can therefore be solved for an even $S$

In this way,the perturbation to the form(2.13) isreduced from $\mathcal { O } ( \varepsilon )$ to $\mathcal { O } ( \varepsilon ^ { 2 } )$ , Bythe same argumentsas in the Hamiltonian case（see Sect.X.5）,the iteration of thisprocedureis seen to be convergent.This finally yieldsachange ofcoordinates thatpreservesreversibilityandtransforms theperturbed system(2.14)back to the form(2.13).We summarize thisin the following theorem,whichis thereversible analogue ofKolmogorov's Theorem X.5.1.

Theorem2.2.Considerareal-analytic reversible system(2.13).Suppose that $\omega \in$ $\mathbb { R } ^ { n }$ satisfies thediophantine condition(X.2.4),and that the angularaverageof $M ( 0 , \cdot )$ isan $n \times m$ matrixofrank n.Let(2.14) beareal-analyticreversible perturbationofthesystem(2.13).Then,thereexists $\varepsilon _ { 0 } ~ > ~ 0$ (which depends on the perturbation functionsonly througha boundoftheir norms ona complexneighbourhoodof $\{ 0 \} \times \mathbb { T } ^ { n } .$ suchthatforevery $^ { \circ }$ with $| \varepsilon | \leq \varepsilon _ { 0 }$ ,thereisareal-analytic transformation $\psi _ { \varepsilon } : ( b , \varphi ) \mapsto ( a , \theta )$ , $\mathcal { O } ( \varepsilon )$ closeto the identity and depending analyticallyon $\in$ ,whichpreservesreversibilityandputstheperturbed systembackto theform(2.13)in thenewvariables: $b = \mathcal { O } ( \vert \vert b \vert \vert ^ { 2 } )$ , $\begin{array} { r } { \Dot { \varphi } = \omega + \mathcal { O } ( \lVert b \rVert ) . } \end{array}$ Theperturbed systemthereforehasthe invariant torus $\{ b = 0 , \varphi \in \mathbb { T } ^ { n } \}$ carrying aquasi-periodic flowwiththe same frequencies $\boldsymbol { \omega }$ astheunperturbedsystem. □

# XI.2.4ReversibleBirkhoff-TypeNormalization

Weshow that,in the situation of diophantine frequencies $\boldsymbol { \omega }$ ,thereisareversibilitypreserving transformation that takesa reversible system of the form(2.13) to the form

$$
\begin{array} { l l } { \dot { b } ~ = ~ r _ { k } ( b , \varphi ) } \\ { \dot { \varphi } ~ = ~ \omega + \zeta _ { k } ( b ) + \rho _ { k } ( b , \varphi ) \quad \quad } & { \mathrm { w i t h } \quad r _ { k } , \rho _ { k } = { \mathcal O } ( \| b \| ^ { k } ) } \end{array}
$$

forarbitrary $k \geq 2$ ,where $\zeta _ { k } = \overline { { \rho } } _ { 1 } + \ldots + \overline { { \rho } } _ { k - 1 }$ with the bars denoting angular averages and with $\rho _ { 1 } ( b , \varphi ) = M ( b , \varphi ) b .$ Thisimpliesagain that the invariant torus is“very sticky": $\| b ( 0 ) \| \le \delta$ implies $\| b ( t ) \| \leq 2 \delta$ for $t \le C _ { k } \delta ^ { - k + 1 }$ Asin the Hamiltonian case,a suitable choice of $k$ would evenyield time intervals exponentiallylongina negative power of $\delta$ during which solutions stay within twice the initial distance $\delta$ .

The transformation to the normal form (2.17)is constructed recursively.Suppose thatin some variables $( a , \theta )$ we have,for some $k \geq 2$ ，

$$
\begin{array} { l l } { { \dot { a } ~ = ~ r _ { k - 1 } ( a , \theta ) } } \\ { { \dot { \theta } ~ = ~ \omega + \zeta _ { k - 1 } ( a ) + \rho _ { k - 1 } ( a , \theta ) ~ } } \end{array} \qquad \mathrm { w i t h } \quad r _ { k - 1 } , \rho _ { k - 1 } = \mathcal { O } ( \lVert a \rVert ^ { k - 1 } ) .
$$

Note,for $k = 2$ we have $r _ { 1 } = \mathcal { O } ( \| a \| ^ { 2 } )$ by(2.13).We search fora transformation

$$
\begin{array} { l l } { a ~ = ~ b + s ( b , \varphi ) } \\ { \theta ~ = ~ \varphi + \sigma ( b , \varphi ) } \end{array} \qquad \mathrm { w i t h } \quad s , \sigma = { \mathcal O } ( \lVert b \rVert ^ { k - 1 } ) ,
$$

(and $s = \mathcal { O } ( \| b \| ^ { 2 } )$ for $k = 2$ )thatpreservesreversibility,ia $s$ even in $\varphi$ and $\boldsymbol { \mathcal { O } }$ odd in $\varphi$ ,andissuch that (2.17) holds.Inserting thetransformationinto the above differential equation shows that thisisindeedachieved if $s , \sigma$ solve the following system ofthe form(2.5),(2.6):

$$
\begin{array} { l } { \displaystyle \frac { \partial s } { \partial \varphi } ( b , \varphi ) \omega = { r } _ { k - 1 } ( b , \varphi ) } \\ { \displaystyle \frac { \partial \sigma } { \partial \varphi } ( b , \varphi ) \omega = { \rho } _ { k - 1 } ( b , \varphi ) + \zeta _ { k - 1 } ^ { \prime } ( b ) s ( b , \varphi ) - { \mu } _ { k } ( b ) . } \end{array}
$$

Choosing $\overline { { s } } ( b ) = 0$ leads to $\mu _ { k } = \rho _ { k - 1 }$ and gives (2.17) with $\zeta _ { k } = \zeta _ { k - 1 } + \overline { \rho } _ { k - 1 } .$

# XI.3Linear Error Growthand Near-Preservation of First Integrals

Wenow study the error behaviour of reversible methodsapplied tointegrablereversible systems.Recallfrom Theorem V.1.5 that symmetricmethodsare reversible underthecompatibilitycondition(V.1.4).We giveananalogue of Theorem X.3.1 ontheerror behaviour of symplectic methodsapplied to integrable Hamiltonian systems.We consideran integrablereversible system（1.1） (usually not givenin action-anglevariables)andlet $( u , v ) = \psi ( a , \theta )$ bethereversibility-preserving transformation to action-anglevariables.The inverse transformationisdenoted as

$$
( a , \theta ) = \left( I ( u , v ) , \Theta ( u , v ) \right) .
$$

The following is the reversibleanalogue of Theorem X.3.1.

Theorem3.1.Considerapplyingareversiblenumerical integratoroforderptothe integrablereversible system(1.1）withreal-analyticright-hand side.Suppose that $\omega ( a ^ { * } )$ satisfies thediophantinecondition(X.2.4).Then,thereexistpositiveconstants $C , c$ and $h _ { 0 }$ such that the followingholds forall step sizes $h \leq h _ { 0 }$ :every numerical solution starting with $\| I ( u _ { 0 } , v _ { 0 } ) - a ^ { * } \| \leq c | \log h | ^ { - \nu - 1 }$ satisfies

$$
\begin{array} { l l } { \| ( u _ { n } , v _ { n } ) - ( u ( t ) , v ( t ) ) \| \leq C t h ^ { p } } & { } \\ { \| I ( u _ { n } , v _ { n } ) - I ( u _ { 0 } , v _ { 0 } ) \| \leq C h ^ { p } } & { } \end{array} f o r \ t = n h \leq h ^ { - p } .
$$

The constants $h _ { 0 } , c , C$ depend on $\gamma , \nu$ of(X.2.4),on thedimensions,onbounds of thereal-analytic functions $f , g$ onacomplexneighbourhood of thetorus $\{ ( u , v ) :$ $I ( u , v ) = a ^ { * } \}$ andon the numericalmethod.

Proof.Theproof ofTheoremX.3.1reliedon TheoremIX.3.1andLemmaX.2.1. Usingtheirreversible analogues Theorem IX.2.3andLemma 2.1 with the same arguments gives the above result for the reversible case. □

Remark 3.2.Asin theanalogous remark for the Hamiltoniancase,theerrorbounds ofTheorem 3.1 also hold when the reversible method isapplied toaperturbed integrable system withaperturbationparameter $\varepsilon$ bounded by a positive power of the step size: $\varepsilon \leq K h ^ { \alpha }$ for some $\alpha > 0$

Weconsider the Hamiltonian system of Example1.4and apply the symmetric butnon-symplectic Lobatto IIIB method with step size $h = 0 . 0 1$ In the left picture ofFig.3.1we choose the initial value $( u _ { 0 } , v _ { 0 } ) = ( 0 , 1 . 5 )$ for which the level curve of the Hamiltonian is symmetric with respect to the $u$ -axisand the system isan integrablereversible system.The good conservation of the Hamiltonianisinagreement with Theorem 3.1.In theright picture we choose $( u _ { 0 } , v _ { 0 } ) = ( 0 , 0 . 3 )$ whose level curve is the fat line in the picture ofExample 1.4which does not intersect the $u$ -axis. Sincein this situationwedo not havean integrable reversible system,Theorem3.1 cannot be applied and we cannot expect good energy conservation.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/97d2011f20f261df29329d0f942fb58797c7111fbbe8474d5f8d740213068178.jpg)  
Fig.3.1.Numerical Hamiltonian of Example1.4 for twodifferent initial values

Forthe Toda lattice example,Figures3.2and 3.3illustrate thelong-time conservation of the first integralsand the linear error growth,respectively,of theLobatto IIB method.

Theorem3.1 togetherwith Examples1.7and1.8also explainsthegood behaviourof symmetric (in fact,reversible) integrators on the rigid body equations which weobserved inChap.V(Figs.V.4.2andV.4.6).

Variable Step Sizes:Proportional,Reversible Controllers.Asa consequence of thebackward erroranalysis of TheoremIX.6.1 the statement（3.1）canbeextended straightforwardly to proportional step size controllers as discussed in Sect.VI.3.1. Under the assumption of Theorem 3.1with $h$ and $h _ { 0 }$ replaced by $\varepsilon$ and $\varepsilon _ { 0 }$ onehas

$$
\begin{array} { r l } { \| ( u _ { n } , v _ { n } ) - ( u ( t _ { n } ) , v ( t _ { n } ) ) \| \leq C t _ { n } \varepsilon ^ { p } } & { \quad \mathrm { f o r } t _ { n } \leq \varepsilon ^ { - p } . } \\ { \| I ( u _ { n } , v _ { n } ) - I ( u _ { 0 } , \bar { v } _ { 0 } ) \| \leq C \varepsilon ^ { p } } & { \quad \mathrm { f o r } t _ { n } \leq \varepsilon ^ { - p } . } \end{array}
$$

The grid $\left\{ \ t _ { n } \right\}$ isdeterminedbythe methodandsatisfies $t _ { n + 1 } = t _ { n } + \varepsilon s ( u _ { n } , v _ { n } , \varepsilon )$

Variable Step Sizes: Integrating,Reversible Controllers.We apply thebackward erroranalysisof TheoremIX.6.2.Themodified equation(IX.6.14)reducesto

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/07d6abd1a150f66f939d64cea48e61d293d7c189f3de30a203e980352f1f2500.jpg)  
Fig.3.2.Numerically obtained eigenvalues(left picture）and errors in the eigenvalues(right picture）of the 3-stageLobatto IIIB scheme (step size $h = 0 . 1$ applied tothe Toda lattice with the data of Sect.X.1.5

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0007_pages_0421-0490/auto/images/6237ac3a15a1ee2e8b03d9b8408ec579396dbef9fd18630a7035841d5fe674ea.jpg)  
Fig.3.3.Euclidean norm of the global errorfor the3-stage Lobatto IIIB scheme(step size $h = 0 . 1$ )appliedtotheToda latticewith $n = 3$ and initial valuesas in Fig.3.2

$$
\dot { y } = f ( y ) , \qquad \dot { z } = z G ( y )
$$

for $\varepsilon = 0$ .Since $\boldsymbol { G } ( y ) = - \big ( \boldsymbol { \sigma } ( y ) \big ) ^ { - 1 } \nabla \boldsymbol { \sigma } ( y ) ^ { T } \boldsymbol { f } ( y )$ with an analytic step size function $\sigma ( y )$ ,thefunction $( y , z ) \mapsto z \sigma ( y )$ isafirst integral of(3.3）.Suppose now that $\dot { y } = f ( y )$ istheintegrablereversible system(1.1).Thismeans that there exists areversibility preservingdiffeomorphism $y = \psi ( a , \theta )$ transforming the system to action-anglevariables.Thediffeomorphism

$$
\binom { y } { z } = \widehat { \psi } ( a , A , \theta ) = \left( { \psi } ( a , \theta ) \right)
$$

is thenalsoreversibility preserving if $\sigma ( u , - v ) = \sigma ( u , v )$ ,and it transforms(3.3)to

$$
\dot { a } = 0 , \qquad \dot { A } = 0 , \qquad \dot { \theta } = \omega ( a ) .
$$

If the basic method of the algorithm (IX.6.9) isreversible and if $\sigma ( u , - v ) = \sigma ( u , v )$ holds,themodifiedequation (IX.6.14) isareversibleperturbation of(3.3).Consequently,Theorem 3.1 yields the statement (3.2) also for integratingstep size controllers.Since $A : = z \sigma ( u , v )$ isanactionvariable,we haveinaddition that

$$
| z _ { n } \sigma ( u _ { n } , v _ { n } ) - z _ { 0 } \sigma ( u _ { 0 } , v _ { 0 } ) | \leq C \varepsilon ^ { 2 }
$$

for $t _ { n } \le \varepsilon ^ { - p }$ Notice that the transformation (2.9）is $\mathcal { O } ( \varepsilon ^ { p } )$ -closetothe identity forthevariables $a$ and $\theta$ ,butonly $\mathcal { O } ( \varepsilon ^ { 2 } )$ -closefor $A$ This result proves that the integrating step size controller is as robust as the proportional controller. It also explains theexcellent long-time behaviour observedinFigs.VII.3.2and VIII.3.3.

# XI.4Invariant Tori under Reversible Discretization

In this section we study the question as to how invariant tori ofreversible systems arepreserved under discretization of the system byreversible numerical methods. Wegive reversible analogues ofTheoremsX.5.3andX.6.1.

# XI.4.1Near-Invariant Tori over Exponentially Long Times

Weconsiderareversiblesystem(1.1） which in suitable coordinates takes the perturbed form (2.14).Under theconditionsof thereversibleKAMtheorem,Theo-$\mathrm { r e m } 2 . 2$ ,this system has an invariant toruscarryingaquasi-periodic flow with frequencies $\omega$ for sufficiently small $\varepsilon .$ Consider now areversible numerical integrator applied to thissystem.By the same argumentsasin Sect.X.5.2,using thereversible KAMtheorem 2.2in place ofKolmogorov's Theorem X.5.1,we obtain the followinganalogue of TheoremX.5.3,which states the existence of a torussuch that numerical solutions starting on this torus remain exponentially close to a quasiperiodic flow on that torus over exponentially long times in $1 / h$ .

Theorem4.1. Intheabovesituation,forareversiblenumericalmethodoforder $p$ usedwith sufficiently small step size $h$ ,thereisamodifiedreversible systemwithan invariant torus $\bar { \mathcal { T } } _ { \omega }$ carryinga quasi-periodic flowwith frequencies $\omega$ ， $\mathcal { O } ( h ^ { p } )$ close totheinvariant torus $\mathcal { I } _ { \omega }$ oftheoriginal reversible system,such thatthedifference between any numerical solution $( u _ { n } , v _ { n } )$ starting onthe torus $\ddot { \tau _ { \omega } }$ and the solution $( \pi ( t ) , \pi ( t ) )$ ofthemodified Hamiltonian systemwiththe same startingvalues remainsexponentially small in $1 / h$ overexponentially long times:

$$
\begin{array} { r } { \| ( u _ { n } , v _ { n } ) - ( \widetilde u ( t ) , \widetilde v ( t ) ) \| \le C e ^ { - \kappa / h } ~ f o r ~ t = n h \le e ^ { \kappa / h } . } \end{array}
$$

The constants $C$ and $\boldsymbol { \kappa }$ areindependentofh,(forh,εsufficientlysmall)andofthe initialvalue $( u _ { 0 } , v _ { 0 } ) \in \mathcal { T } _ { \omega }$ . □

The case ofinitial values lying close to,but noton $\bar { \tau _ { \omega } }$ ,canagainbetreatedbya reversible analogueof TheoremX.4.7.

# XI.4.2A KAMTheoremforReversible Near-IdentityMaps

Toobtain truly invariant tori,weneedadiscreteanalogueof thereversibleKAM theorem,which isderived in this subsection.Thisresult canalso be viewedas the reversible analogueof TheoremX.6.1.It establishes the existenceof invariant tori ofreversible integrators,but as in the symplectic case,only fora Cantor set of nonresonant step sizes.

Amap $\boldsymbol { \varPhi } : ( a , \theta ) \mapsto ( \widehat { a } , \widehat { \theta } )$ has the invariant torus $\{ a = 0 , \theta \in \mathbb { T } ^ { n } \}$ ,andreduces on this torus to rotation by $h \omega$ （ $h$ areal parameterand $\omega \in \mathbb { R } ^ { n }$ ),when itis of the form (cf.(2.13))

$$
\begin{array} { r c l } { { \widehat { a } } } & { { = } } & { { a + \frac { 1 } { 2 } h a ^ { T } K ( a , \theta ) a } } \\ { { } } & { { } } & { { \widehat { \theta } ~ = ~ \theta + h \omega + h M ( a , \theta ) a . } } \end{array}
$$

Here, $K = [ K _ { 1 } , \ldots , K _ { m } ]$ where each $K _ { i } ( a , \theta )$ isasymmetric $m \times m$ matrix,and $M ( a , \theta )$ isan $n \times m$ matrix.The expression in the first equation is again to be interpreted as $a ^ { 2 } K _ { i } ( a , \theta ) a$ for the components $i = 1 , \ldots , m$ .

Anecessary condition for the above map $\boldsymbol { \Phi }$ to bereversible with respect to the involution $\left( a , \theta \right) \mapsto \left( a , - \theta \right) ,$ cf.Definition V.1.2, is seen to be

$$
\begin{array} { c } { { K ( 0 , - \theta ) ~ = ~ - K ( 0 , \theta - h \omega ) ~ } } \\ { { { \cal M } ( 0 , - \theta ) ~ = ~ { \cal M } ( 0 , \theta - h \omega ) . } } \end{array}
$$

Consider now a perturbed map

$$
\begin{array} { r l } & { \widehat { \boldsymbol { a } } \mathrm { ~  ~ \psi ~ } = \boldsymbol { a } + \frac { 1 } { 2 } h \boldsymbol { a } ^ { T } \boldsymbol { K } ( \boldsymbol { a } , \theta ) \boldsymbol { a } + h \boldsymbol { \varepsilon } \boldsymbol { r } ( \boldsymbol { a } , \theta ) } \\ & { \widehat { \boldsymbol { \theta } } \mathrm { ~  ~ \psi ~ } = \boldsymbol { \theta } + h \boldsymbol { \omega } + h \boldsymbol { M } ( \boldsymbol { a } , \theta ) \boldsymbol { a } + h \boldsymbol { \varepsilon } \rho ( \boldsymbol { a } , \theta ) } \end{array}
$$

where $r$ and $\rho$ ,which like $K$ and $M$ areassumed real-analytic,might depend analyticallyalsoon $h$ and $\varepsilon$ .Reversibility of this map implies,bydirect computation, that inaddition to (4.2),the following equations are satisfiedup toan error $\mathcal { O } ( h \varepsilon )$

$$
\begin{array} { r c l } { { r ( 0 , - \theta ) ~ = ~ - r ( 0 , \theta = h \omega ) } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \displaystyle \frac { \partial r } { \partial a } ( 0 , - \theta ) ~ = ~ - \frac { \partial r } { \partial a } ( 0 , \theta ) } } \\ { { } } & { { } } & { { ~ \displaystyle \rho ( 0 , - \theta ) ~ = ~ \rho ( 0 , \theta - h \omega ) - h M ( 0 , \theta - h \omega ) r ( 0 , \theta - h \omega ) . } } \end{array}
$$

Similarto Sect.XI.2.3,we construct a reversibility-preservingnear-identity transformation of coordinates $( a , \theta ) \mapsto ( b , \varphi )$ such that the above map $\phi _ { h , \varepsilon }$ in thenew variablesis of the form(4.3）with theperturbation termsreduced from $\mathcal { O } ( \varepsilon )$ to $\mathcal { O } ( \varepsilon ^ { 2 } )$ Similar to Sect.X.6.1,this ispossibleif $h \omega$ satisfies the diophantine condition(X.6.3）andif theangular average $M _ { 0 }$ of $M ( 0 , \cdot )$ hasrank $n$ .

We look for the transformation in the form (2.15).The functions defining this transformation must satisfy the following equations,cf.(2.16):

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \frac { s ( \varphi + h \omega ) - s ( \varphi ) } { h } ~ = ~ r ( 0 , \varphi ) } } \\ { { } } & { { } } & { { \displaystyle \frac { \sigma ( \varphi + h \omega ) - \sigma ( \varphi ) } { h } ~ = ~ \rho ( 0 , \varphi ) + M ( 0 , \varphi ) s ( \varphi ) } } \\ { { } } & { { } } & { { \displaystyle \frac { S _ { i j } ( \varphi + h \omega ) - S _ { i j } ( \varphi ) } { h } ~ = ~ \frac { \partial r _ { i } } { \partial b _ { j } } ( \varphi ) - { \displaystyle \sum _ { k } \frac { \partial s _ { i } } { \partial \varphi _ { k } } } ( \varphi ) M _ { k j } ( 0 , \varphi ) } } \\ { { } } & { { } } & { { ~ + { \displaystyle \sum _ { k } s _ { k } ( \varphi ) } K _ { i , k j } ( 0 , \varphi ) . } } \end{array}
$$

Under theconditions(X.6.3),(X.6.4) these equationscan be solved by Fourier expansion,in the same way as theanalogous equations in SectionsX.6.1 and XI.2.3, and the map in the variables $( 6 , \varphi )$ becomes of the form

$$
\begin{array} { r l } & { \widehat { b } \ = \ b + \frac { 1 } { 2 } h b ^ { T } K ( b , \varphi ) b + { \cal O } ( h \varepsilon \| b \| ^ { 2 } ) + { \cal O } ( h \varepsilon ^ { 2 } ) } \\ & { \widehat { \varphi } \ = \ \varphi + h \omega + h M ( b , \varphi ) b + { \cal O } ( h \varepsilon \| b \| ) + { \cal O } ( h \varepsilon ^ { 2 } ) . } \end{array}
$$

We still need to know that the change of variables $( a , \theta ) \mapsto ( b , \varphi )$ preserves reversibility,i.e.,that $s$ and $S$ are even functions of $\varphi$ and $o$ isan odd function of $\varphi$ .Thisis indeedaconsequence of (4.2）and (4.4).(Wemaymodify $r$ and $\rho$ such that(4.4) holds exactly,at the expense of introducing additional $\mathcal { O } ( h ^ { 2 } \varepsilon ^ { 2 } )$ perturbations in (4.3).)Let us show this property for $s$ TheFouriercoefficients $s _ { k }$ of $s$ must satisfy

$$
{ \frac { e ^ { i k \cdot h \omega } - 1 } { h } } s _ { k } = r _ { k } .
$$

Since (4.4) implies $r _ { - k } = - r _ { k } e ^ { - i k \cdot h \omega }$ for all $k$ ,it follows that $s _ { - k } = s _ { k }$ ,and hence $s$ is an even function of $\varphi$ Similarly itis shown that $S$ is even and $\sigma$ is odd.

Insummary,we have founda transformation $\mathcal { O } ( \varepsilon )$ close to the identity,which transforms thereversible map(4.3) toareversiblemap(4.6),thusreducing theperturbation terms from $\mathcal { O } ( \varepsilon )$ to $O ( \varepsilon ^ { 2 } )$ The iteration of this procedure can again be shownto be convergent.This finallyyieldsa transformation to coordinates in terms ofwhich theperturbed mapis back in the form(2.13）.In this way we obtain the following discrete analogue of Theorem2.2orreversibleanalogue of Theorem X.6.1.

Theorem4.2. Considera real-analytic reversiblemap $\phi _ { h , \epsilon }$ ofthe form(4.3）,defined onaneighbourhoodof $\{ 0 \} \times \mathbb { T } ^ { n }$ ,with $0 \in \mathbb { R } ^ { m }$ Supposethat hw satisfies the diophantine condition(X.6.3),and that theangularaverage of $M ( 0 , \cdot )$ hasrank $_ { n }$ . Then,there exists $\varepsilon _ { 0 } > 0$ such that forevery $\boldsymbol { \varepsilon }$ with $| \varepsilon | < \varepsilon _ { 0 }$ ,thereisareal-analytic transformation $\psi _ { h , \varepsilon } : ( b , \varphi ) \mapsto ( a , \theta )$ ，whichpreservesreversibilityandis $\mathcal { O } ( \varepsilon )$ closeto theidentity uniformly in $h$ satisfying(X.6.3)andisanalytic in is again of teform(.1): $\succeq$ suchthat $\psi _ { h , \varepsilon } ^ { - 1 } \circ \varPhi _ { h , \varepsilon } \circ \psi _ { h , \varepsilon } : ( b , \varphi ) \mapsto ( \widehat { b } , \widehat { \varphi } )$ $\hat { b } = b + \mathcal { O } ( \| b \| ^ { 2 } )$ $\begin{array} { r } { \widehat { \varphi } = \varphi + h \omega + \mathcal { O } ( \| b \| ) . } \end{array}$ Theperturbedmap $\phi _ { h , \varepsilon }$ therefore hasaninvariant torus on whichit isconjugate torotationby hw. □

Asin the analogous situation of Sect.X.6.2,Theorem 4.2appliesdirectly,with $\varepsilon = h ^ { p }$ ,tothe situationwhereareversible numerical method of order $p$ isused todiscretize an integrable reversible system,or more generally,a reversible systemwitha KAM toruswith diophantine frequencies $\boldsymbol { \omega }$ Here（4.1）correspondsto thetime- $h$ flowof thereversible system,and(4.3) represents the numerical map. Thisestablishes theexistence of invariant tori forreversible integrators,inperfect analogytothe symplectic counterpart Theorem X.6.2.

Concerning condition(X.6.3)wereferback to Sect.X.6.3,where it is shown that this condition is satisfied fora Cantor set of step sizes $h$ if $\omega$ satisfies thediophantine condition (X.2.4).

# XI.5 Exercises

1.This exercise shows that reversibility with respect to the particular involution $( u , v ) \mapsto ( u , - v )$ is not as special as it might seem at first glance.

（a） If the system $\dot { y } = f ( y )$ is $\rho$ -reversible(i.e., $f ( \rho y ) = - \rho f ( y ) )$ ,thenthe transformed system $\dot { z } = T ^ { - 1 } f ( T z )$ is $\sigma$ -reversiblewith $\sigma = T ^ { - 1 } \rho T$ (b)Every linear involution（ $\rho ^ { 2 } = I$ ）issimilar toa diagonal matrixwithentries $\pm 1$ .

2.Consider the Toda lattice equationswith anarbitrary number $n$ ofdegrees of freedom and with periodic boundary conditions.

（a）Find all linear involutions $\rho$ for which the system is $\rho$ -reversible. （b)Study for which $\rho$ the eigenvalues of the matrix $\mathcal { L }$ are even functions of $v$ (c) Investigate (numerically）the set of initial values for which all theassumptionsof Theorem 1.3are satisfied for some involution $\rho$ . Hint.Generalize the discussion for $n = 3$ in the Example 1.6.

3.Areversible system of the form

$$
\begin{array} { l } { \dot { \alpha } ~ = ~ 0 } \\ { \dot { \theta } ~ = ~ \omega ( { a } , \theta ) } \end{array}
$$

with $\omega$ aneven function of $\theta \in \mathbb { T } ^ { n } .$ also hasa foliation of invariant tori.Considerreversible perturbations of such systems like in (2.1）and search fora reversibility-preserving transformation(2.3) that takes theperturbed system to theform

$$
\begin{array} { l } { \dot { b } = \mathcal { O } ( \varepsilon ^ { 2 } ) } \\ { \ddot { \varphi } = \omega ( b , \varphi ) + \varepsilon \mu ( b , \varphi ) + \mathcal { O } ( \varepsilon ^ { 2 } ) } \end{array}
$$

with $\mu$ evenin $\varphi$ .Writedown the partial differential equations that the transformation must satisfy and discuss (sufficient) conditions for their solvability.

4.Thetorus $\{ a = 0 , \theta \in \mathbb { T } ^ { n } \}$ isinvariant and carriesa conditionally periodic flow with frequencies $\boldsymbol { \omega }$ forreversible systems of the form $\dot { a } = \mathcal { O } ( \left| \left| a \right| \right| )$ ， $\dot { \theta } =$ $\omega + \mathcal { O } ( \left| \left| a \right| \right| )$ ,which ismore general than(2.13) in the differential equation for $a$ . Discuss the difficulties that arise in trying to transformareversible perturbation ofsuch a system back to this form.

5.Applyan arbitrary(non-symmetric)Runge-Kutta method of even order $p = 2 k$ toanintegrablereversible system.Prove that under the assumptions of Theo-$\mathrm { r e m } 3 . 1$ theglobal error behaves for $t = n h$ like

$$
y _ { n } - y ( t ) = \mathcal { O } ( t h ^ { p } ) + \mathcal { O } ( t ^ { 2 } h ^ { p + 1 } ) ,
$$

and the action variables like

$$
I ( y _ { n } ) - I ( y _ { 0 } ) = \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( t h ^ { p + 1 } ) .
$$
