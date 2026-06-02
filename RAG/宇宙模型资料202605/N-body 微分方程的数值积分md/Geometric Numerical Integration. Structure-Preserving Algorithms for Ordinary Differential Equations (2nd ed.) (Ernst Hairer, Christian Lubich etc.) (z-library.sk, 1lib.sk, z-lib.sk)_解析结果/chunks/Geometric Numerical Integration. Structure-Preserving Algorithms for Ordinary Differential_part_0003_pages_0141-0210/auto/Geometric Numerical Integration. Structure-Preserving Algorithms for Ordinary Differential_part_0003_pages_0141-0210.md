The first few Bernoulli numbers are $B _ { 0 } = 1$ , $B _ { 1 } = - 1 / 2$ ， $B _ { 2 } = 1 / 6$ ， $B _ { 3 } = 0$ . Thedifferential equation(7.4) therefore becomes

$$
\dot { \Omega } = A ( t ) - \frac { 1 } { 2 } \left[ \Omega , A ( t ) \right] + \frac { 1 } { 1 2 } \left[ \Omega , \left[ \Omega , A ( t ) \right] \right] + \ldots ,
$$

which is nonlinear in $\Omega .$ Applying Picard fixed point iterationafter integration yields

$$
\begin{array} { r l } { ( t ) = \displaystyle \int _ { 0 } ^ { t } A ( \tau ) d \tau ~ - } & { \frac { 1 } { 2 } \displaystyle \int _ { 0 } ^ { t } \Bigl [ \int _ { 0 } ^ { \tau } A ( \sigma ) d \sigma , A ( \tau ) \Bigr ] d \tau } \\ & { +  \frac { 1 } { 4 } \int _ { 0 } ^ { t } \Bigl [ \int _ { 0 } ^ { \tau } \bigl [ \int _ { 0 } ^ { \sigma } A ( \mu ) d \mu , A ( \sigma ) \bigr ] d \sigma , A ( \tau ) \Bigr ] d \tau \quad  \quad ( 7 . } \\ & { +  \frac { 1 } { 1 2 } \int _ { 0 } ^ { t } \Bigl [ \int _ { 0 } ^ { \tau } A ( \sigma ) d \sigma , \Bigl [ \int _ { 0 } ^ { \tau } A ( \mu ) d \mu , A ( \tau ) \Bigr ] \Bigr ] d \tau + . . . } \end{array}
$$

whichis the so-called Magnus expansion.For smooth matrices $A ( t )$ theremainderin（7.5）is of size $\mathcal { O } ( t ^ { 5 } )$ so that the truncated seriesinserted into $Y ( t ) =$ $\exp \bigl ( \Omega ( t ) \bigr ) Y _ { 0 }$ givesan excellent approximation to the solution of（7.1） for small $t$ .

Numerical Methods Based on the Magnus Expansion. Iserles& Norset（1999) studythegeneral form of theMagnus expansion（7.5）,and they relate the iterated integralsand therational coefficientsin（7.5） to binary trees.Foranumerical integration of

$$
\dot { Y } = A ( t ) Y , \qquad Y ( t _ { 0 } ) = Y _ { 0 }
$$

(where $Y$ isamatrix or avector) they propose using $Y _ { n + 1 } = \exp ( h \Omega _ { n } ) Y _ { n }$ ,where $h \Omega _ { n }$ isasuitable approximation of $\Omega ( h )$ given by（7.5）with $A ( t _ { n } + \tau )$ instead of $A ( \tau )$ Of course,the Magnus expansion has to be truncated and the integrals have tobeapproximated by numerical quadrature.

Wefollow here the collocation approach suggested by Zanna(1999).The idea is toreplace $A ( t )$ locallybyan interpolation polynomial

$$
\widehat { A } ( t ) = \sum _ { i = 1 } ^ { s } \ell _ { i } ( t ) A ( t _ { n } + c _ { i } h ) ,
$$

and to solve $\dot { Y } = \widehat { A } ( t ) Y$ on $\left[ { { t _ { n } } , { t _ { n } } + h } \right]$ bythe use of the truncated series(7.5).

Theorem7.2.Consideraquadrature formula $( b _ { i } , c _ { i } ) _ { i = 1 } ^ { s }$ oforder $p \geq s$ andlet $Y ( t )$ and $Z ( t )$ be solutions of $Y = A ( t ) Y$ and $\dot { Z } = \widehat { A } ( t ) Z$ respectively,satisfying $Y ( t _ { n } ) = Z ( t _ { n } ) .$ Then, $Z ( t _ { n } + h ) - Y ( t _ { n } + h ) = \mathcal { O } ( h ^ { p + 1 } )$

Proof.We write the diffrential equation for $Z$ as $\dot { Z } = A ( t ) Z + \big ( \hat { A } ( t ) - A ( t ) \big ) Z$ and use the variation of constants formula to get

$$
Z ( t _ { n } + h ) - Y ( t _ { n } + h ) = \int _ { t _ { n } } ^ { t _ { n } + h } R ( t _ { n } + h , \tau ) \Big ( \widehat { A } ( \tau ) - A ( \tau ) \Big ) Z ( \tau ) d \tau .
$$

Applyingourquadratureformula to this integral gives zero asresult,and theremainder is of size ${ \mathcal { O } } ( h ^ { p + 1 } ) .$ Details of the proof are as for Theorem II.1.5. □

Example7.3.Asa first example,we use themidpoint rule $c _ { 1 } = 1 / 2$ ， $b _ { 1 } = 1$ .In this case the interpolation polynomial is constant,and themethod becomes

$$
Y _ { n + 1 } = \exp \left( h A ( t _ { n } + h / 2 ) \right) Y _ { n } ,
$$

which is of order 2.

Example7.4. The two-stage Gaussquadrature is given by $c _ { 1 , 2 } = 1 / 2 \pm { \sqrt { 3 } } / 6$ $b _ { 1 , 2 } = 1 / 2$ .Theinterpolationpolynomial is ofdegree oneand we have toapply （7.5）in order to get an approximation $Y _ { n + 1 }$ Sinceweare interestedina fourth orderapproximation,we can neglect the remainder term (indicated by $\cdot \cdot \cdot$ in (7.5)). Computing analytically the iterated integrals over products of $\ell _ { i } ( t )$ we obtain

$$
Y _ { n + 1 } = \exp \left( \frac { h } { 2 } ( A _ { 1 } + A _ { 2 } ) + \frac { \sqrt { 3 } h ^ { 2 } } { 1 2 } [ A _ { 2 } , A _ { 1 } ] \right) Y _ { n } ,
$$

where $A _ { 1 } = A ( t _ { n } + c _ { 1 } h )$ and $A _ { 2 } = A ( t _ { n } + c _ { 2 } h ) .$ This isa method of order four. The terms of（7.5）with triple integrals give $\mathcal { O } ( h ^ { 4 } )$ expressions,whose leading term vanishesbythe symmetry of the method(ExerciseV.7).Therefore,they need not beconsidered.

Theorem7.2allowsusto obtain methods ofarbitrarily high order.Astraightforwarduse of the expansion(7.5)yieldsan expression with alarge numberofcommutators.Munthe-Kaas&Owren（1999)andBlanes,Casas&Ros（20o0a)construct higher ordermethodswithareduced numberof commutators.For example,fororder6 the required number of commutators isreduced from 7 to 4.

Letus remark that all numerical methods of this section are of the form $Y _ { n + 1 } = \exp ( h \Omega _ { n } ) Y _ { n }$ where $\varOmega _ { n }$ is a linear combination of $A ( t _ { n } + c _ { i } h )$ and of their commutators.If $A ( t ) \in { \mathfrak { g } }$ for all $t$ ,thenalso $h \varOmega _ { n }$ lies in the Lie algebrag,so that the numerical solution stays in the Liegroup $G$ if $Y _ { 0 } \in G$ (thisisaconsequence ofLemma 6.4).

# IV.8 Lie Group Methods

Consideradifferential equation

$$
{ \dot { Y } } = A ( Y ) Y , \qquad Y ( 0 ) = Y _ { 0 }
$$

onamatrix Lie group $G$ Thismeans that $Y _ { 0 } ~ \in ~ G$ and that $A ( Y ) \in { \mathfrak { g } }$ forall $Y \in G$ .Since this isa special case ofdifferential equations onamanifold,projection methods(Sect.IV.4) aswell as methods based on local coordinates (Sect.IV.5)are well suited for their numerical treatment.Here we present further approaches which alsoyield approximations that lieon themanifold.

Allnumerical methods of this section can beextended inastraightforward way to non-autonomous problems $\dot { Y } = A ( t , Y ) Y$ with $A ( t , Y ) \in { \mathfrak { g } }$ forall $t$ andall $Y \in G$ Just to simplify the notation we restrict ourselves to the formulation (8.1).

# IV.8.1 Crouch-Grossman Methods

The discipline ofLie-group methods owesagreat deal to the pioneering work of Peter Crouch and his co-workers... (A.Iserles,H.Z.Munthe-Kaas,S.P.Ngrsett&A.Zanna2000)

Thenumerical approximation of explicit Runge-Kutta methods is obtained bya composition of the following two basic operations:(i)an evaluation of the vector field $f ( Y ) = A ( Y ) Y$ and (ii)acomputationof anupdate of theform $Y + h a f ( Z )$ Forexample,the left method of (II.1.3) consists of the following steps:evaluate $K _ { 1 } = f ( Y _ { 0 } )$ ;compute $Y _ { 1 } = Y _ { 0 } + h K _ { 1 }$ ;evaluate $K _ { 2 } = f ( Y _ { 1 } )$ ;compute $Y _ { 1 / 2 } =$ $Y _ { 0 } + { \frac { h } { 2 } } K _ { 1 }$ ;compute $\begin{array} { r } { Y _ { 1 } = Y _ { 1 / 2 } + \frac { h } { 2 } K _ { 2 } } \end{array}$

Inthe context of differential equations on Lie groups,these methods have the disadvantage that,even when $Y \in G$ and $Z \in G$ ,theupdate $Y + h a A ( Z ) Z$ isin general not in theLiegroup.Theidea ofCrouch&Grossman(1993) is toreplace the“update”operation with $\exp ( h a A ( Z ) ) Y .$

Definition 8.1. Let $b _ { i } , a _ { i j }$ $\iota , \jmath \ = \ 1 , \ldots , s )$ bereal numbers.An explicit $s$ -stage Crouch-Grossman method is given by

$$
\begin{array} { r l } & { Y ^ { ( i ) } \ = \ \exp ( h a _ { i , i - 1 } K _ { i - 1 } ) \times \ldots \times \exp ( h a _ { i 1 } K _ { 1 } ) Y _ { n } , \qquad K _ { i } = A ( Y ^ { ( i ) } ) , } \\ & { Y _ { n + 1 } \ = \ \exp ( h b _ { s } K _ { s } ) \times \ldots \times \exp ( h b _ { 1 } K _ { 1 } ) Y _ { n } . } \end{array}
$$

For example,themethod of Runge described above（ $s = 2$ , $a _ { 2 1 } = 1$ , $b _ { 1 } = b _ { 2 } =$ $1 / 2 )$ leadsto

$$
Y _ { n + 1 } = \exp \Bigl ( \frac { h } { 2 } K _ { 2 } \Bigr ) \exp \Bigl ( \frac { h } { 2 } K _ { 1 } \Bigr ) Y _ { n } ,
$$

where $K _ { 1 } = A ( Y _ { n } )$ and $K _ { 2 } = A \left( \exp ( h K _ { 1 } ) Y _ { n } \right)$ .

Byconstruction,the methods of Crouch-Grossman give rise to approximations $Y _ { n }$ which lieexactly on themanifold defined by theLie group.But what can besaid about their order of accuracy?

Theorem 8.2. Let $c _ { i } = \sum _ { j } a _ { i j } .$ ACrouch-Grossmanmethod has order $p \left( p \leq 3 \right) i f$ thefollowing order conditionsare satisfied:

$$
\begin{array} { r l r l } & { o r d e r 1 : } & & { \sum _ { i } b _ { i } = 1 } \\ & { o r d e r 2 : } & & { \sum _ { i } b _ { i } c _ { i } = 1 / 2 } \\ & { o r d e r 3 : } & & { \sum _ { i } b _ { i } c _ { i } ^ { 2 } = 1 / 3 } \\ & { } & & { \sum _ { i j } b _ { i } a _ { i j } c _ { j } = 1 / 6 } \\ & { } & & { \sum _ { i } b _ { i } ^ { 2 } c _ { i } + 2 \sum _ { i < j } b _ { i } c _ { i } b _ { j } = 1 / 3 . } \end{array}
$$

ProofAsinthe case of Runge-Kutta methods,theorder conditionscanbefound bycomparing the Taylor series expansions of the exact and the numerical solution. Inaddition to the conditions stated in the theorem,this leads torelations such as

$$
\sum _ { i } b _ { i } ^ { 2 } c _ { i } + 2 \sum _ { i < j } b _ { i } b _ { j } c _ { j } = \frac { 2 } { 3 } .
$$

Addingthis equation to（8.7)we find $2 \textstyle \sum _ { i j } b _ { i } c _ { i } b _ { j } = 1$ ,which is satisfied by(8.3) and(8.4).Hence,the relation (8.8)is alreadyaconsequence of the conditions stated in the theorem. □

Table8.1.Crouch-Grossman methods of order 3   

<table><tr><td>0 -1/24 17/24</td><td>-1/24 161/24 -6</td><td>0 3/4 17/24</td><td>3/4</td></tr><tr><td></td><td>1 -2/3 2/3</td><td></td><td>119/216 17/108 13/51 -2/3 24/17</td></tr></table>

Crouch& Grossman(1993)present several solutions of the system (8.3)-(8.7), oneofwhich is given in theleft array of Table8.1.Theconstruction of higher order Crouch-Grossman methodsisvery complicated(...any attempt to analyze algorithmsof order greater than three will bevery complex,...",Crouch& Grossman, 1993）.

The theory of order conditions forRunge-Kutta methods(Sect.III.1) has been extended to Crouch-Grossman methods by Owren&Marthinsen(1999).It turns out that the order conditions for classical Runge-Kutta methods form a subset of those forCrouch-Grossmanmethods.The first new condition is(8.7).Fora method of order4,thirteenconditions (including those of Theorem 8.2） have to be satisfied. Solving these equations,Owren&Marthinsen（1999)constructa4th order method with $s = 5$ stages.

# IV.8.2 Munthe-Kaas Methods

Thesemethodsweredeveloped ina series of papersby Munthe-Kaas(1995,1998, 1999).The main motivation behind the first of these paperswas to developa theoryofRunge-Kutta methods inacoordinate-free framework.Afterattempts that ledto new order conditions (as for the Crouch-Grossman methods),Munthe-Kaas (1999)had the idea to write the solution as $Y ( t ) = \exp ( \varOmega ( t ) ) Y _ { 0 }$ and to solve numerically the differential equation for $\Omega ( t )$ .Itsounds awkward to replace the differential equation(8.1） bya more complicated one.However,the nonlinear invariants $g ( Y ) = 0$ of（8.1）defining theLie groupare replaced with linear invariants $g ^ { \prime } ( I ) ( \varOmega ) = 0$ defining theLiealgebra,and we know from Sect.IV.1 that essentially all numerical methods automaticallyconserve linear invariants.

It follows from the proof of Theorem 7.1 that the solution of (8.1) can be written as $Y ( t ) = \exp ( \varOmega ( t ) ) Y _ { 0 }$ ,where $\boldsymbol { \mathcal { Q } } ( t )$ is the solution of $\begin{array} { r } { \dot { \Omega } = d \exp _ { \Omega } ^ { - 1 } \big ( A \big ( Y ( t ) \big ) \big ) } \end{array}$ ， $\varOmega ( 0 ) = 0$ Since itisnot practical towork with the operator $d \exp _ { \Omega } ^ { - 1 }$ ,we truncate the series(7.3) suitably and consider the differential equation

$$
\dot { \Omega } = A \big ( \exp ( \varOmega ) Y _ { 0 } \big ) + \sum _ { k = 1 } ^ { q } \frac { B _ { k } } { k ! } \operatorname { a d } _ { \varOmega } ^ { k } \Big ( A \big ( \exp ( \varOmega ) Y _ { 0 } \big ) \Big ) , \qquad \varOmega ( 0 ) = 0 .
$$

This leads to the following method.

Algorithm8.3(Munthe-Kaas1999).Considertheproblem(8.1)with $A ( Y ) \in { \mathfrak { g } }$ for $Y \in G$ Assume that $Y _ { n }$ lies in the Lie group $G$ Then,the step $Y _ { n } \mapsto Y _ { n + 1 }$ is definedasfollows:

consider thedifferentialequation(8.9)with $Y _ { n }$ insteadof $Y _ { 0 } ,$ andapplyaRunge-Kuttamethod(explicit or implicit) to get anapproximation $\Omega _ { 1 } \approx \Omega ( h )$ , thendefine thenumerical solution by $Y _ { n + 1 } = \exp ( \varOmega _ { 1 } ) Y _ { n }$

Before analyzing this algorithm,we emphasize its close relationshipwith Algorithm5.3.In fact,ifwe identify theLiealgebragwith $\mathbb { R } ^ { k }$ (where $k$ is thedimension ofthevector spaceg）,the mapping $\psi ( \Omega ) = \exp ( \Omega ) Y _ { n }$ isa local parametrization of the Lie group $G$ (seeLemma 6.4).Apart from the truncation of the series in (8.9), Algorithm8.3isa special caseof Algorithm5.3.

Important properties of the Munthe-Kaas methods are given in the next two theorems.

Theorem 8.4.Let $G$ bea matrix Lie groupandgits Liealgebra.If $A ( Y ) \in { \mathfrak { g } }$ for $Y \in G$ andif $Y _ { 0 } \in G$ ,thenthe numerical solutionof the Lie groupmethodof Algorithm8.3 liesin $G$ i.e., $Y _ { n } \in G$ forall $n = 0 , 1 , 2 , \ldots$

Proof.Itis sufficient toprove that for $Y _ { 0 } ~ \in ~ { \cal { G } }$ the numerical solution $\Omega _ { 1 }$ ofthe Runge-Kutta method applied to （8.9) lies ing.Since theLie bracket $\left\lfloor \Omega , A \right\rfloor$ isan operation ${ \mathfrak { g } } \times { \mathfrak { g } } \to { \mathfrak { g } }$ ,and since $\exp ( \Omega ) Y _ { 0 } \in G$ for $\mathcal { Q } \in \mathfrak { g }$ ,theright-hand expression of（8.9）is in $\mathfrak { g }$ for $\mathcal { B } \in \mathfrak { g }$ Hence,(8.9)isadifferential equation on thevector spacegwith solution $\mathcal { Q } ( t ) \in \mathfrak { g }$ Alloperationsina Runge-Kutta method give resultsin g,so that the numerical approximation $\Omega _ { 1 }$ also lies in g. □

Theorem8.5.If theRunge-Kuttamethodisof(classical) order $p$ andifthe truncation index in(8.9) satisfies $q \ \geq \ p - 2$ thenthemethodofAlgorithm8.3isof orderp.

Proof.For sufficiently smooth $A ( Y )$ we have $\Omega ( t ) = t A ( Y _ { 0 } ) + \mathcal { O } ( t ^ { 2 } )$ , $Y ( t ) =$ $Y _ { 0 } + \mathcal { O } ( t )$ and $[ \Omega ( t ) , A ( Y ( t ) ) ] = \mathcal { O } ( t ^ { 2 } )$ This implies that ad $\mathbf { \Sigma } _ { \Omega ( t ) } ^ { k } ( A ( Y ( t ) ) ) =$ $\mathcal { O } ( t ^ { k + 1 } )$ ,sothatthetruncationof theseriesin(8.9)inducesanerrorofsize $\mathcal { O } ( h ^ { q + 2 } )$ for $| t | \leq h$ Hence,for $q + 2 \geq p$ thistruncation does not affect the order of convergence. □

The most simpleLie group method is obtained if we take the explicit Euler method as basic discretization and $q = 0$ in (8.9). This leads to the so-called Lie-Eulermethod

$$
Y _ { n + 1 } = \exp { \left( h A ( Y _ { n } ) \right) } Y _ { n } .
$$

Thisis also a special case of the Crouch-Grossman methods of Definition 8.1.

Taking the implicit midpoint ruleas the basic discretization and again $q = 0$ in (8.9),we obtainthe Liemidpoint rule

$$
Y _ { n + 1 } = \exp ( \varOmega ) Y _ { n } , \qquad \varOmega = h A \big ( \exp ( \varOmega / 2 ) Y _ { n } \big )
$$

This is an implicit equation in $\varOmega$ and has tobe solved by fixed point iteration or by Newton-typemethods.

Example8.6.We take the coefficientsof the right arrayof Table8.1.They give rise to 3rd orderMunthe-Kaas and 3rd orderCrouch-Grossmanmethods.Weapply both methodswith the large step size $h = 0 . 3 5$ to thesystem(1.5）which isalready of the form (8.1).Observe that $Y _ { 0 }$ isavector in $\mathbb { R } ^ { 3 }$ and not amatrix,but allresults of this section remain valid for this case.For the computation of the matrix exponential we usethe Rodrigues formula(Exercise17).The numerical results （first 1Ooo steps)are shown in Fig.8.1.We see that the numerical solution stays on the manifold(sphere), buton the sphere the qualitative behaviour is not correct.A similar behaviour could be observed for projection methods (the orthogonal projection consists simply in dividing the approximation $\bar { Y } _ { n + 1 }$ byitsnorm) and by the methods based on local coordinates.

Crouch-Grossman methods and Munthe-Kaas methods are very similar.If they arebased on the same set of Runge-Kutta coefficients,both methodsuse s evaluations of thematrix $A ( Y )$ The Crouch-Grossman methods require in general the computation of $s ( s + 1 ) / 2$ matrix exponentials,whereas the Munthe-Kaas methods require only $s$ ofthem.On the other hand,Munthe-Kaas methods need also the computations of a certain number of commutators which increases with $q$ in (8.9). Insuch acomparison one has to take into account that every classical Runge-Kutta method definesa Munthe-Kaasmethod of the same order,but Crouch-Grossman methods of high order are verydifficultto obtain,and need more stages for the same order(if $p \geq 4$ ).

![](images/89609677d7357ca0ef2cff7ce3b209fb85231dc2069b33529002a9202dc3ce3a.jpg)  
Fig.8.1.Solutions of theEulerequations(1.4)for therigid body

# IV.8.3Further Coordinate Mappings

ThemethodsofAlgorithm 8.3are based on the local parametrization $\psi ( \Omega ) = $ $\exp ( \Omega ) Y _ { n }$ .ForallLie groups,this isadiffeomorphism between theLie groupand thecorrespondingLie algebra.Are there other,computationallymore efficient parametrizations that can be used in special situations?

TheCayley Transform.Lie groups of the form

$$
G = \{ Y \mid Y ^ { T } P Y = P \} ,
$$

where $P$ isagiven constant matrix,arecalled quadratic Lie groups.The correspondingLiealgebraisgiven by $\mathfrak { g } = \{ \Omega \ | \ P \Omega + \Omega ^ { I } P = 0 \} .$ Theorthogonal group ${ \mathrm { O } } ( n )$ and the symplectic group $\operatorname { S p } ( n )$ are prominent special cases (see Table6.1).For such groups we have the following analogue of Lemma 6.4.

Lemma 8.7.ForaquadraticLiegroup $G$ ,theCayley transform

$$
\mathrm { c a y } \Omega = ( I - \Omega ) ^ { - 1 } ( I + \Omega )
$$

maps elements ofginto $G .$ Moreover,itisalocaldifeomorphismnear $\Omega = 0$

Proof.For $\Omega \in { \mathfrak { g } }$ (i.e., $P \Omega + \Omega ^ { T } P = 0$ wehave $P ( I + \varOmega ) = ( I - \varOmega ) ^ { I } P$ and also $P ( I - \Omega ) ^ { - 1 } = ( I + \Omega ) ^ { - I } P .$ For $Y = ( I - \Omega ) ^ { - 1 } ( I + \Omega )$ thisimmediately implies $Y ^ { T } P Y = P$ □

Theuse ofthe Cayley transform forthe numerical integration ofdifferential equations on Lie groups has been proposed by Lewis $\&$ Simo（1994）andDiele, Lopez&Peluso(1998) for theorthogonal group,andbyLopez&Politi(2001) for general quadratic groups.Itis based onthe followingresult,which isan adaptation ofLemma III.4.1andLemma II.4.2to theCayleytransform.

Lemma8.8.Thederivativeofcay $\varOmega$ is given by

$$
\left( \frac { d } { d \Omega } \mathrm { c a y } \bar { \Omega } \right) \bar { H } = \left( d \mathrm { c a y } _ { \bar { \Omega } } ( \bar { H } ) \right) \mathrm { c a y } \bar { \Omega } ,
$$

where

$$
d \operatorname { c a y } _ { \Omega } ( H ) = 2 ( I - \Omega ) ^ { - 1 } H ( I + \Omega ) ^ { - 1 } .
$$

For the inverse of $d$ cay $\varOmega$ wehave

$$
d \mathrm { c a y } _ { \Omega } ^ { - 1 } ( H ) = \frac { 1 } { 2 } ( I - \Omega ) H ( I + \Omega ) .
$$

Proof.By the usual rules of calculus we obtain

$$
\left( \frac { d } { d \Omega } \mathrm { c a y } \Omega \right) H = ( I - \Omega ) ^ { - 1 } H ( I - \Omega ) ^ { - 1 } ( I + \Omega ) + ( I - \Omega ) ^ { - 1 } H ,
$$

andasimplealgebraic manipulation proves the statements.

The numerical approach for solving(8.1）in the case of quadratic Lie groups isanadaptation of theAlgorithm8.3.We considerthe local parametrization $Y =$ $\psi ( \Omega ) = \mathrm { c a y } ( \Omega ) Y _ { n }$ ,and we apply one step ofa numerical methodto thedifferential equation ${ \dot { \boldsymbol { \mathcal { R } } } } = { \dot { \boldsymbol { d } } }$ cay $\mathring { \Omega } ^ { \boldsymbol { A } } \big ( \mathrm { c a y } ( \Omega ) Y _ { n } \big )$ which,by(8.14),is equivalent to

$$
\dot { \Omega } = \frac { 1 } { 2 } ( I - \Omega ) A \Big ( \mathrm { c a y } ( \Omega ) Y _ { n } \Big ) ( I + \Omega ) .
$$

Thisequation replaces (8.9)inthe Algorithm 8.3.Since no truncation of an infinite seriesis necessary here,thisapproach isa special case ofAlgorithm5.3.

Canonical Coordinates of the Second Kind.Fora basis $\{ C _ { 1 } , C _ { 2 } , \ldots , C _ { d } \}$ of theLie algebra g the coordinates $z _ { 1 } , \dots , z _ { d }$ of the local parametrization $\psi ( z ) =$ $\textstyle \exp \left( \sum _ { i = 1 } ^ { d } z _ { i } C _ { i } \right)$ of the Lie group $G$ arecalledcanonicalcoordinatesofthefirst kind.Herewe are interested in the parametrization

$$
\psi ( z ) = \exp \bigl ( z _ { 1 } C _ { 1 } \bigr ) \exp \bigl ( z _ { 2 } C _ { 2 } \bigr ) \cdot \ldots \cdot \exp \bigl ( z _ { d } C _ { d } \bigr ) ,
$$

and we call $\boldsymbol { z } = ( z _ { 1 } , \ldots , z _ { d } ) ^ { T }$ canonical coordinates ofthe second kind(Varadarajan1974).The use of these coordinates in connection with the numerical solution of differential equations on Lie groups has been promoted by Celledoni $\&$ Iserles （2001）andOwren $\&$ Marthinsen (2oOl).Theidea behind this choice is that,due to a sparse structure of the $C _ { i }$ ,thecomputation of $\exp ( z _ { 1 } C _ { 1 } ) , \ldots , \exp ( z _ { d } C _ { d } )$ maybe much cheaper than the computation of $\textstyle \exp ( \sum _ { i } z _ { i } C _ { i } )$ .

With the change of coordinates $y \equiv \psi ( z )$ ,thedifferential equation (8.1） becomes $\psi ^ { \prime } ( z ) \dot { z } = A \big ( ( \psi ( z ) \big ) \psi ( z )$ ,which is equivalent to

$$
\begin{array} { l } { { \displaystyle { \cal A } \big ( \psi ( z ) \big ) ~ = ~ \sum _ { i = 1 } ^ { d } \dot { z } _ { i } ~ \mathrm { e x p } ( z _ { 1 } C _ { 1 } ) \mathrel { \mathop : } \ldots \hat { \displaystyle } \exp ( z _ { i - 1 } C _ { i - 1 } ) } } \\ { { \phantom { \displaystyle { \cal A } \big ( \psi ( z ) \big ) ~ } : C _ { i } \mathrel { \mathop : } \exp ( - z _ { i - 1 } C _ { i - 1 } ) \mathrel { \mathop : } \ldots \mathrel { \mathop : } \exp ( - z _ { 1 } C _ { 1 } ) } } \\ { { \phantom { \displaystyle { \cal A } \big ( \psi ( z ) \big ) ~ } = ~ \sum _ { i = 1 } ^ { d } \dot { z } _ { i } \big ( F _ { 1 } \circ \ldots \circ F _ { i - 1 } \big ) C _ { i } , } } \end{array}
$$

where we use the notation $F _ { j } C = \exp ( z _ { j } C _ { j } ) C \exp ( - z _ { j } C _ { j } )$ for the linear operator $F _ { j } : { \mathfrak { g } } \to { \mathfrak { g } }$ ;seeExercise 12.We need to compute ${ \dot { z } } _ { 1 } , \dots , { \dot { z } } _ { d }$ from(8.16）,and this willusually beacomputationallyexpensive task.However,for several Liealgebras and forwell chosen bases thiscan bedonevery efficiently.Thecrucial idea is the following:we let $\widehat { F } _ { j }$ bedefined by

$$
\widehat { F } _ { j } C _ { i } = \left\{ \begin{array} { l l } { F _ { j } C _ { i } \quad } & { \mathrm { i f } i > j } \\ { C _ { i } \quad } & { \mathrm { i f } i \leq j , } \end{array} \right.
$$

andwe assume that

$$
\bigl ( F _ { 1 } \circ \dots \circ F _ { i - 1 } \bigr ) C _ { i } = \bigl ( \widehat { F } _ { 1 } \circ \dots \circ \widehat { F } _ { i - 1 } \bigr ) C _ { i } , \qquad i = 2 , \ldots , d .
$$

Under thisassumption,we have $\begin{array} { r } { \big ( F _ { 1 } \circ \dots \circ F _ { i - 1 } \big ) C _ { i } = \big ( \widehat { F } _ { 1 } \circ \dots \circ \widehat { F } _ { i - 1 } \big ) C _ { i } = } \end{array}$ : $\big ( \widehat { F } _ { 1 } \circ \dots \circ \widehat { F } _ { d - 1 } \big ) C _ { i }$ andtherelation(8.16) becomes

$$
\left( \widehat { F } _ { 1 } \circ \dots \circ \widehat { F } _ { d - 1 } \right) \Big ( \sum _ { i = 1 } ^ { d } \dot { z } _ { i } C _ { i } \Big ) = A \big ( \psi ( z ) \big ) .
$$

In the situations which we have in mind,the operators $\hat { F } _ { j }$ canbeefficiently inverted, and Algorithm 5.3 can be applied to the solution of(8.1).

Themain difficulty of usingthis coordinate transform is to find asuitable orderingofa basis such that condition (8.18)is satisfied.The following lemma simplifies this task.Weuse the notation $\begin{array} { r } { C = \sum _ { k = 1 } ^ { d } \alpha _ { k } ( C ) C _ { k } . } \end{array}$ $\alpha _ { k } ( C )$ forthe coefficient in the representation

Lemma 8.9.Let $\{ C _ { 1 } , \ldots , C _ { d } \}$ beabasisof theLiealgebrag.Iffor every pair $j < i$ andfor $k < j$ wehave

$$
\alpha _ { k } ( F _ { j } C _ { i } ) \neq 0 \qquad \Longrightarrow \qquad F _ { \ell } C _ { k } = C _ { k } \quad f o r \ \ell \ s a t i s f y i n g \ k \leq \ell < j ,
$$

thentherelation(8.18) holds forall $i = 2 , \ldots , d$

Proof.Wewrite $\begin{array} { r } { \widehat { F } _ { i - 1 } C _ { i } = F _ { i - 1 } C _ { i } = \sum _ { k } \alpha _ { k } ( F _ { i - 1 } C _ { i } ) C _ { k } } \end{array}$ It follows from the definitionof $\widehat { F } _ { j }$ and from(8.20) that $( \widehat { F } _ { i - 2 } \circ \widehat { F } _ { i - 1 } ) C _ { i } = ( F _ { i - 2 } \circ F _ { i - 1 } ) C _ { i } .$ Arepeated application of this argument proves the statement. □

Owren&Marthinsen(2oo1） have studied Lie algebras that admita basis satisfying（8.18）forall $\scriptscriptstyle \mathcal { L }$ We present here one of their examples.

Example 8.10 (Special Linear Group).Consider the differential equation (8.1) on the Lie group $\mathrm { S L } ( n ) = \{ Y \mid$ det $Y = 1 \}$ ,i.e.,the matrix $A ( Y )$ liesin ${ \mathfrak { s l } } ( n ) =$ $\{ A \mid \operatorname { t r a c e } A = 0 \}$ $i \neq j$ and $D _ { i } = e _ { i } e _ { i } ^ { I } - e _ { i + 1 } e _ { i + 1 } ^ { I }$ Asabasis of theLie algebra for $1 \leq i < n$ ${ \mathfrak { s l } } ( n )$ (here, we choose $e _ { i } = ( 0 , \ldots , 1 , \ldots , 0 ) ^ { 1 }$ $E _ { i j } = e _ { i } e _ { j } ^ { { \scriptscriptstyle T } }$ for denotes the vectorwhose only non-zero element is in the $i$ th position).Following Owren&Marthinsen(2Oo1)we order the elements of this basisas

$$
\begin{array} { r l } & { E _ { 1 2 } < \ldots < E _ { 1 n } < E _ { 2 3 } < \ldots < E _ { 2 n } < \ldots < E _ { n - 1 , n } } \\ & { \qquad < E _ { 2 1 } < \ldots < E _ { n 1 } < E _ { 3 2 } < \ldots < E _ { n 2 } < \ldots < E _ { n , n - 1 } } \\ & { \qquad < D _ { 1 } < \ldots < D _ { n - 1 } . } \end{array}
$$

With the use ofLemma 8.9one can check ina straightforward way that the relation （8.18）is satisfied.In nearly all situations $\alpha _ { k } ( F _ { j } C _ { i } ) = 0$ for $k < j < i$ ,sothat （8.18)represents an empty condition.Consequently,the $\dot { z } _ { i }$ can be computed from (8.19).Due to the sparsity of the matrices $E _ { i j }$ and $D _ { i }$ ,the computation of $\widehat { F } _ { i } ^ { - 1 }$ can bedonevery efficiently.

# IV.9 Geometric Numerical Integration Meets Geometric Numerical LinearAlgebra

Thepersistent use of orthogonal transformations isa hallmark of numerical linear algebra.Correspondingly,manifoldsincorporating orthogonality constraints play animportant role all over this field;see Edelman,Arias& Smith（1998）onthe geometry ofalgorithmswith orthogonality constraints.Inaddition tothe orthogonal group ${ \mathrm { O } } ( n )$ ,themanifolds of primary interest are:

$\nu _ { n , k }$ ,theStiefel manifold of $n \times k$ matriceswith $k$ orthonormal columns,   
$\mathcal { G } _ { n , k }$ ,，the Grassmann manifold of orthogonal projections of $\mathbb { R } ^ { n }$ onto $k$ -dimensional subspaces,and   
$\mathcal { M } _ { k } ^ { m \times n }$ themanifold of $m \times n$ matrices of rank $k$ whichisrelatedtootogonal transformations via the singularvalue decomposition and arelated decomposition discussed below.

# IV.9.1 Numerical Integration on the Stiefel Manifold

The original motivation for Stiefel Manifolds (in Stiefel 1935）was the topological problem, whethera manifold $\mathcal { M }$ can possess $k$ everywhere linearly independent continuous vector fields.The problem,which had been solved for the case $k =$ 1,wasmuch harder for $k > 1$ Inordertoattack thisquestion,Stiefel introduced ‘his'manifold

$$
\mathcal { V } _ { n , k } = \{ Y \in \mathbb { R } ^ { n \times k } | Y ^ { T } Y = I \} ,
$$

asanauxiliary tool for thedefinition ofwhat later becameknownas the Stiefel-Whitneyclasses6.

Here,we are interested in computations on these manifolds for their own,with many applications,as for example the computation ofLyapunov exponents of differential equations;see Exercise22as well asBridges&Reich(2Oo1) and Dieci,Russell&vanVleck(1997). There are also many cases where orthogonality constraints concern only some of thevariables inadifferential equation.In moleculardynamics,for example,such orthogonality constraints arisein the Car-Parrinello approach toabinitio moleculardynamics(Car&Parrinello 1985)and in themulticonfiguration time-dependent Hartreemethod of quantummoleculardynamics(Beck,Jackle,Worth&Meyer 2000).

![](images/8614f5d3a7629a93d63957166e6b3110839990fa178ebcbf1c6258999f4f1b0d.jpg)  
Eduard Stiefel5

Tangentand Normal Space.Wechoosea fixed matrix $Y$ in the Stiefel manifold $\mathcal { V } = \mathcal { V } _ { n , k } .$ Then the tangent space （5.4）at $Y \in \nu$ consists of the matrices $Z$ such that $( Y + \varepsilon Z ) ^ { I } ( Y + \varepsilon Z )$ remains $I$ for $\varepsilon  0 .$ Differentiating we obtain

$$
T _ { Y } \mathcal { V } = \{ Z \in \mathbb { R } ^ { n \times k } | Z ^ { T } Y + Y ^ { T } Z = 0 \} ,
$$

i.e., $Y ^ { T } ~ Z$ is skew-symmetric.Thisrepresents $\textstyle { \frac { 1 } { 2 } } k ( k + 1 )$ conditions, thus $T _ { Y } \nu$ is of dimension $n k - { \textstyle \frac { 1 } { 2 } } k ( k + 1 )$

Fordefining the normal space,we use the standard Euclidean inner product on $\mathbb { R } ^ { n \times k }$ ,i.e.,

$$
\begin{array} { r } { \langle A , B \rangle = \operatorname { t r a c e } ( A ^ { T } B ) = \sum _ { i j } a _ { i j } b _ { i j } , } \end{array}
$$

whose corresponding norm is the Frobenius norm

$$
\begin{array} { r } { \| A \| _ { F } = \sqrt { \sum _ { i j } a _ { i j } ^ { 2 } } . } \end{array}
$$

Then the normal space at $Y$ is given by

$$
N _ { Y } \mathcal { V } = \left\{ K \in \mathbb { R } ^ { n \times k } \mid K \perp T _ { Y } \mathcal { V } \right\} = \left\{ Y S \mid S \right.
$$

To show this,weobserve thattheorthogonality $Y S \perp T _ { Y } \mathcal { V }$ follows from $\langle Y S , Z \rangle =$ trace $\langle S Y ^ { T } Z \rangle = \langle S , Y ^ { T } Z \rangle$ and thefact that any symmetric matrix $A$ isorthogonal toany skew-symmetric matrix $B$ Adimension count (the matrix $S$ has $\textstyle { \frac { 1 } { 2 } } k ( k + 1 )$ free elements)now shows us that the space defined in(9.5) fills the entire orthogonal complementof $I Y V$ .

Orthogonality-Preserving Runge-Kutta Methods.Suppose now that we have to solveadifferential equation $Y = F ( Y )$ ona Stiefel manifold $\nu$ Theorthogonality constraints $Y ^ { T } Y = I$ arepreserved,if thederivative $F ( Y )$ liesin the tangent space $T \gamma V$ ,i.e.,if $F ( Y ) ^ { \prime } Y + Y ^ { T } F ( Y ) = 0$ ,forevery $Y ~ \in ~ \nu$ (weak invariants,see Sect.IV.4).In the (exceptional) case where they are in fact true invariants,i.e.,if $F ( Y ) ^ { T } Y + Y ^ { T } F ( Y ) = 0$ forall $Y \in \mathbb { R } ^ { n \times k }$ ,thenthe orthogonalityconstraintsare quadratic,and are thereforepreserved exactlyby theimplicit Runge-Kuttamethods of Sect.IV.2.1,in particular the Gauss methods.These methods give numerical solutions on the Stiefel manifold,but use function evaluations outside the manifold.

Inthegeneral case of onlyweak invariants,a standard approach for enforcing orthogonality istheintroduction of Lagrange multipliers,which can be interpreted asartificial forces in the direction of the normal space keeping the solutions on the manifold.Due to the structure of $N _ { Y } \nu$ (see(9.5)),the problem becomes here

$$
\begin{array} { r } { \dot { Y } = F ( Y ) + Y \varLambda , \quad Y ^ { T } Y = I } \end{array}
$$

witha symmetric Lagrange multiplier matrix $\varLambda \in \mathbb { R } ^ { k \times k }$ ;see also Exercise 10. Anynumerical method fordifferential-algebraic equations can nowbeapplied,e.g., appropriateRunge-Kutta methodsasinChap.VI and Sect.VII.4 ofHairer&Wanner(1996).A symmetric adaptation of Gauss methods to such problems is given by Jay(2005）.

Belowwe shall study in great detail mechanical systems with constraints (see Sect.VII.1).In the case of orthogonality constraints,such problemscan be treated successfullywithLobatto IIIA-IIIB partitionedRunge-Kutta methods,which inaddition to orthogonality preserve other important geometric properties such as reversibilityand symplecticity.

![](images/f66ff074a4db339cf74fcd15fa7be9974b6565a553031f3579353226361ef2ff.jpg)  
Fig.9.1.Projection onto the Stiefel manifold using the singular value decomposition

Projection Methods.If we want to use the projection method of Algorithm 4.2,we haveto perform,after every integration step,theprojection (4.4),which requires to find forany given matrix $\widetilde { Y }$ amatrix $Y \in \mathcal { V }$ with

$$
\| Y - { \tilde { Y } } \| _ { F } \to \operatorname* { m i n } .
$$

This projection can be obtained as follows:if $Y$ isnot in $\nu$ (but close),then its column vectors $y _ { 1 } , \ldots , y _ { k }$ willhave normsdifferent from 1and/or their angles will not be right angles.These quantities determine an ellipsoid,ifwe require that thesevectorsrepresent conjugate diameters8(see Fig.9.1(a)).This ellipsoid is then transformed to principal axes in $\mathbb { R } ^ { k }$ byan orthogonal map $U ^ { T }$ （picture（b)）).We let $O _ { 1 } , \ldots , O _ { k }$ bethe length of these axes.If the coordinates are nowdivided by $\sigma _ { i }$ ， then the ellipsoid becomes the unit sphere and the vectors $U ^ { T } { \widetilde { y } } _ { i }$ become orthonormalvectors $U ^ { T } y _ { i } .$ These vectors,when transformed back with $U$ ,liein $\nu$ andare theprojection wewere searching for (picture (c)).For a proof of the optimality,see Exercise 21.

Connectionwith the Singular Value Decomposition.We have by construction that $\begin{array} { r } { U ^ { T } y _ { i } = \Sigma ^ { - 1 } U ^ { T } \widetilde { y } _ { i } } \end{array}$ where $\varSigma = \mathrm { d i a g } ( \sigma _ { 1 } , \dots \sigma _ { k } ) .$ If we finally map these vectors by anorthogonal matrix $V$ to the unit base,we see that $V \Sigma ^ { - 1 } U ^ { T } Y = I$ ,or

$$
\boldsymbol { \widetilde { Y } } = \boldsymbol { U } \boldsymbol { \Sigma } \boldsymbol { V } ^ { T }
$$

which is the singular value decomposition of $\hat { Y }$ This connection allows us to use standard software for our calculations.The projected matrix is then $Y = U V ^ { I }$ .

Remark 1.When the differential equation possesses some symmetry (see the next chapter),then thesymmetricprojectionalgorithm V.4.1ispreferable to be used instead.

Remark 2.Theabove procedure isequivalentto the one proposed by D.Higham (1997):the orthogonal projection is the first factor of the polardecomposition $\dot { Y } =$ $Y R$ (where $Y$ has orthonormal columnsand $R$ issymmetric positivedefinite).The equivalence is seen from the polar decomposition $Y = ( U V ^ { T } ) ( V \Sigma V ^ { T } ) .$ Arelated procedure,where the first factor of the $Q R$ decomposition of $\tilde { Y }$ isused instead of thatof thepolardecomposition,isproposed in DieciRussell&vanVleck（1994).

Tangent Space Parametrization.For the applicationof the methods of Sect.IV.5,inparticular Subsection IV.5.3,to the case of Stiefel manifolds,we have to find the formulas for the projection (5.8) (see the wrap figure).

Forafixed $Y$ ,let $Y + Z$ be an arbitrary matrix in $Y + T _ { Y } \mathcal { V }$ ,forwhich we search the projection $\psi _ { Y } ( Z )$ to $\nu$ Because of the structure of $N _ { Y } \nu$ （see(9.5)),we have that

![](images/3ccc5179ddd3dbebbaa71885e8b29b6a7c03c443196a6023bff72cbc1c10d576.jpg)

$$
\psi _ { Y } ( Z ) = Y + Z + Y S
$$

isa local parametrization of $\nu$ ,if $S$ is symmetric and if $\psi _ { Y } ( Z ) ^ { T } \psi _ { Y } ( Z ) = I .$ This condition,when multiplied out,shows that $S$ hasto bea solution of the algebraic Riccati equation

$$
S ^ { 2 } + 2 S + S Y ^ { T } Z + Z ^ { T } Y S + Z ^ { T } Z = 0 .
$$

Observe that for $k = 1$ ,where the Stiefel manifold reduces to the unit sphere in $\mathbb { R } ^ { n }$ ,theequation(9.1O)is a scalar quadratic equation and can be easily solved.For $k > 1$ ,itcanbe solved iteratively usingthescheme (e.g.,starting with $S _ { 0 } = 0$ ）

$$
( I + Z ^ { T } Y ) S _ { n } + S _ { n } ( I + Y ^ { T } Z ) = - Z ^ { T } Z - S _ { n - 1 } ^ { 2 } .
$$

Usinga Schur decomposition $Y ^ { T } Z = Q ^ { T } R Q$ (where $Q$ is orthogonal and $R$ upper triangular),theelementsof $Q S _ { n } Q ^ { T }$ can be computed successively starting from the leftuppercorner.Werefer to themonograph ofMehrmann（1991） foradetailed discussion of the solution of linear and algebraic Riccati equations.

Next,we compute for the matrix $F ^ { \prime }$ its orthogonal projection $P _ { Y } ( F )$ to $I _ { Y } \nu$ , i.e.,by(9.5）,we have to finda symmetricmatrix $\bar { S }$ such that $P _ { Y } ( F ) = F - Y S$ . The tangent condition $P _ { Y } ( F ) ^ { T } Y + Y ^ { T } P _ { Y } ( F ) = 0$ leadsto $\widetilde { S } = ( F ^ { T } Y + Y ^ { T } F ) / 2$ so that

$$
P _ { Y } ( F ) = F - \frac { 1 } { 2 } \big ( Y F ^ { T } Y + Y Y ^ { T } F \big ) .
$$

With the parametrization $\psi _ { Y } ( Z )$ of(9.9)the transformed differential equation, when projected to the tangent space,yields

$$
\dot { Z } = P _ { Y } F \big ( \psi _ { Y } ( Z ) \big ) ,
$$

incomplete analogy to (5.9).The numerical solution of(9.12）requires,for every function evaluation,the solution of the Riccati equation (9.1O)and the computation ofa projection onto the tangent space,each needing $\mathcal { O } ( n k ^ { 2 } )$ operations.Compared with theprojection method,the overhead(i.e.,the computationapartfrom theevaluation of $F ( Y )$ ismore expensive,buttheapproach described here hastheadvantage thatall evaluations of $F$ areexactly on themanifold $\nu$ .

# IV.9.2 Differential Equations on the Grassmann Manifold

TheGrassmann manifold is obtained from the Stiefel manifold by identifying matricesin $\mathcal { V } _ { n , k }$ thatspan the same subspace (see Fig.9.2(a)).Since any two such matrices result from each other byright multiplication with an orthogonal $k \times k$ matrix,theresulting manifold is the quotient manifold

$$
\mathcal { G } _ { n , k } = \mathcal { V } _ { n , k } / \mathrm { O } ( k ) .
$$

Anequivalence class $[ Y ] \in { \mathcal { G } } _ { n , k }$ defines an orthogonal projection $P = Y Y ^ { T }$ of rank $k$ ,and conversely,every orthogonal basis of therange of $P$ yieldsarepresentative $Y \in \mathcal { V } _ { n , k } .$ We can thus view the Grassmann manifold as

$$
{ \mathcal G } _ { n , k } = \Big \{ P \Big | \begin{array} { l } { P \mathrm { ~ i s ~ a n ~ o r t h o g o n a l ~ p r o j e c t i o n ~ o n t o } } \\ { \mathrm { ~ a ~ } k { \mathrm { - } } \mathrm { d i m e n s i o n a l ~ s u b s p a c e ~ o f } \mathbb { R } ^ { n } } \end{array} \Big \} .
$$

![](images/42cf7cb01f5bf471fa640467621ea415e3619e11c132da9d68cef68dc83d59ae.jpg)  
Fig.9.2.Integration of adifferential equation on the Grassmann manifold

The Tangent Space.The map $Y \mapsto P = Y Y ^ { T }$ from $\mathcal { V }  \mathcal { G }$ has the tangent map （derivative）9

$$
T _ { Y } \mathcal { V }  T _ { P } \mathcal { G } : \delta { Y } \mapsto \delta { P } = \delta { Y } { Y } ^ { T } + { Y } \delta { Y } ^ { T } ,
$$

andwewish to apply all the methods for $I Y V$ from the arsenal of the preceding section to problems in $T _ { P } \mathcal { G }$ .However,the dimension of $\scriptstyle { \mathcal { I } } _ { P } { \mathcal { G } }$ isby $\textstyle { \frac { 1 } { 2 } } k ( k - 1 )$ lower than the dimension of $I _ { Y } \mathcal { V } .$ Thisdifference is the dimension ofO（ $k$ )andalso of ${ \mathfrak { s o } } ( k )$ ,thevector space of skew-symmetric $k \times k$ matrices.The key idea is now the following:if we replace the condition from (9.2), $Y ^ { T } \delta Y$ skew-symmetric,by $Y ^ { T } \delta Y = 0$ ,thenweremoveprecisely the superfluousdegrees offreedom.Indeed, theextended tangent map

$$
T _ { Y } \mathcal { V }  T _ { P } \mathcal { G } \times \mathfrak { s o } ( k ) : \quad \delta Y \mapsto ( \delta Y Y ^ { T } + Y \delta Y ^ { T } , Y ^ { T } \delta Y )
$$

is anisomorphism,since it is readily seen to have zero nul-space and the dimensions of the vector spaces agree.The tangent space is thus characterized as

$$
\begin{array} { r } { T _ { P } \mathcal { G } = \{ \delta P = \delta Y Y ^ { T } + Y \delta Y ^ { T } \mid Y ^ { T } \delta Y = 0 \} , } \end{array}
$$

andevery $\partial P \in T _ { P } \mathcal { G }$ corresponds toa unique $\delta Y$ with $Y ^ { T } \delta Y = 0$ Note that this condition on $\delta Y$ does not depend on the representative $Y$ of $[ Y ]$

Differential Equations.Consider nowa differential equation on $\mathcal { G }$ ，

$$
{ \dot { P } } = G ( P ) ,
$$

withavector field $G$ on $\mathcal { G }$ .Thecondition $G ( P ) \in T _ { P } { \mathcal { G } }$ means,since the tangent map(9.15)is onto,that there exists for $P = Y Y ^ { T }$ avector $F ( Y )$ suchthat

$$
G ( P ) = F ( Y ) Y ^ { T } + Y F ( Y ) ^ { T } \qquad \mathrm { w i t h } \qquad F ^ { T } Y + Y ^ { T } F = 0
$$

i.e., $F ( Y ) \in { \mathcal { T } } _ { Y } \mathcal { V } .$ However,froma given initial position $Y$ ,therearemany $F$ which produce the same movement $G$ of the subspace represented by $P$ (see Fig.9.2 (b)).By (9.16),themovement of $Y$ becomes unique if we require that this movement is orthogonal to the subspace (see Fig.9.2 (c)),

$$
{ \cal Y } ^ { T } \dot { \cal Y } = 0 .
$$

Multiplying the derivative ${ \dot { P } } = { \dot { Y } } Y ^ { T } + Y { \dot { Y } } ^ { T }$ with $Y ^ { T }$ from the left,we obtain, under condition (9.20), $Y ^ { T } P = Y ^ { T }$ and,by (9.18)and (9.19), $Y = Y F ^ { T } Y + F$ or

$$
\begin{array} { r } { \dot { Y } = ( I - Y Y ^ { T } ) F ( Y ) . } \end{array}
$$

Geometrically,this means that the vector $F ( Y )$ ,which could be chosen arbitrarily in $T _ { Y } \nu$ ,isprojected to the orthogonal complement of the subspace spanned by $Y$ or $P = Y Y ^ { T } ,$ Thederivative $\dot { Y }$ in（9.21） is independent of the particular choice of $F$

Equation(9.21）isadifferential equation on the Stiefel manifold $\nu$ that can be solved numerically by the methods described in the previous subsection.

Example9.1 (Oja Flow).A basic example arises in neural networks (Oja 1989): solutions on $\nu _ { n , k }$ ofthedifferential equation

$$
\dot { Y } = ( I - Y Y ^ { T } ) A Y
$$

with a constant symmetric positive definite matrix $A \in \mathbb { R } ^ { n \times n }$ tend to an orthogonal basis of an invariant subspace of $A$ as $t \to \infty$ (Yan,Helmke&Moore1994).

Anaive comparison of this equation with (9.21）would lead to $F ( Y ) = A Y$ ,but this function does not satisfy the tangent condition $F ^ { I } Y + Y ^ { I } F = 0$ from(9.19). So we use the fact that $( I - Y Y ^ { T } ) ^ { 2 } = I - Y Y ^ { T }$ and set $F ( Y ) = ( I - Y Y ^ { T } ) A Y$ With this, $G ( P )$ from (9.18)and(9.19) becomes

$$
\begin{array} { r } { \dot { P } = ( I - P ) A P + P A ( I - P ) . } \end{array}
$$

Wehaveobtainedtheresult that equation (9.22）can beviewedasa differential equation on the Grassmann manifold $\mathcal { G } _ { n , k }$

However,for the numerical integration it is more practical to work with (9.22).

# IV.9.3Dynamical Low-Rank Approximation

Low-rank approximation of large matrices isa basic model reduction technique in manyapplication areas,such as image compression and latent semantic indexingin information retrieval;see forexample Simon& Zha(2OoO).Here,we consider the task of computing lowrank approximations to matrices $A ( t ) \in \mathbb { R } ^ { m \times n }$ depending smoothlyon $t$ Atanytime $t$ ,abest approximationto $A ( t )$ ofrank $k$ isamatrix $X ( t )$ in the manifold $\mathcal { M } _ { k } = \mathcal { M } _ { k } ^ { m \times n }$ of rank- $k$ matrices that satisfies

$$
X ( t ) \in \mathcal { M } _ { k } \quad \mathrm { ~ s u c h ~ t h a t ~ } \quad \| X ( t ) = A ( t ) \| _ { F } = \operatorname* { m i n } !
$$

Theproblem is solved bya singular value decomposition of $A ( t )$ ,truncatingall singularvalues after the $f ^ { * }$ largest ones.When thematrix is so large thatacomplete singular value decomposition isnot feasible,a standard approach to obtain an approximate solution is based on theLanczos bidiagonalization process with $A ( t )$ ,as discussed in Simon& Zha(2000).

FollowingKoch&Lubich(2Oo5),we here consider instead thelow-rank approximation $Y ( t ) \in \mathcal { M } _ { k }$ determined from thecondition that forevery $t$ thederivative $Y ( t )$ ,whichis in the tangent space $T _ { Y } ( t ) \mathcal { M } _ { k }$ ,bechosenas

$$
\dot { Y } ( t ) \in T _ { Y ( t ) } \mathcal { M } _ { k } \quad \mathrm { ~ s u c h ~ t h a t ~ } \quad \| \dot { Y } ( t ) - \dot { A } ( t ) \| _ { F } = \operatorname* { m i n } !
$$

Thisiscomplemented with an initial condition,ideally $Y ( t _ { 0 } ) = X ( t _ { 0 } ) .$ Forgiven $Y ( t )$ ,thederivative $Y ( t )$ isobtained bya linear projection,though ontoa solutiondependentvector space.Problem(9.25）yieldsadifferential equationon $\mathcal { M } _ { k }$ We will see that with a suitable factorization of rank- $k$ matrices,we obtaina system ofdifferential equations for the factors that iswell-suited for numerical integration. Thedifferential equations contain only the increments $\dot { A } ( t )$ ,whichmaybemuch sparser than the full data matrix $A ( t )$

Koch&Lubich（2005）show that $Y ( t )$ yieldsaquasi-optimal approximation onintervalswherea good smooth approximation exists.It must be noted,however, that the best rank- $k$ approximation $X ( t )$ mayhave discontinuities,which cannot be captured in $Y ( t )$ .Thisisalready seen from theexample of findinga rank-1 approximation to $\mathrm { d i a g } ( e ^ { - t } , e ^ { t } )$ ,where startingfrom $t _ { 0 } < 0$ yields $X ( t ) = Y ( t ) =$ $\mathrm { d i a g } ( e ^ { - t } , 0 )$ for $t < 0$ ,but $Y ( t ) = \mathrm { d i a g } ( e ^ { - t } , 0 )$ and $X ( t ) = \mathrm { d i a g } ( 0 , e ^ { t } )$ for $t > 0$

The best approximation $X ( t )$ hasa discontinuity at $t = 0$ ,caused by acrossing of singular values ofwhich one is insideand the other one outside theapproximation. Analgorithmicremedyistorestart(9.25）atregular intervals.

Incontrast to（9.24）,theapproach(9.25) extendsimmediately to thelow-rank approximation of solutions of matrix differential equations ${ \mathit { \Pi } } _ { { \mathit { A } } } ~ = ~ F ( A )$ Here, $A ( t )$ in(9.25) is simplyreplacedby theapproximation $F ( Y ( t ) )$ ,which yieldsthe minimum-defect low-rank approximation $Y ( t )$ bychoosing

$$
\dot { Y } \in T _ { Y } \mathcal { M } _ { k } \quad \mathrm { ~ s u c h ~ t h a t ~ } \quad \| \dot { Y } - F ( Y ) \| _ { F } = \operatorname* { m i n } !
$$

Anapproach of this type is of common use inquantumdynamics,where the physicalmodel reduction of the multivariate Schrodinger equation by the analogue of (9.26)isknown as the Dirac-Frenkel time-dependent variational principle,after Dirac（1930)and Frenkel（1934)；seealsoBeck,Jackle,Worth&Meyer（2000) and Sect.VII.6.

Decompositions of Rank $k$ MatricesandofTheir TangentMatrices.Everyreal rank- $k$ matrix of dimension $m \times n$ can be written in the form

$$
\boldsymbol { Y } = \boldsymbol { U } \boldsymbol { S } \boldsymbol { V } ^ { T }
$$

where $U \in \mathcal { V } _ { m , k }$ and $V \in \mathcal { V } _ { n , k }$ have orthonormal columns,and $S \in \mathbb { R } ^ { k \times k }$ is nonsingular.The singular value decomposition yields $S$ diagonal,but here we do notassume a special form of $S$ .Therepresentation （9.27) is not unique:replacing $U$ by $\tilde { U } = U P$ and $V$ by $\bar { V } = V Q$ with orthogonal matrices $P , Q \in \operatorname { O } ( k )$ and correspondingly $S$ by $S = P ^ { T } S Q .$ yields the samematrix $\begin{array} { r } { Y = U S V ^ { T } = \widetilde { U } \widetilde { S } V ^ { T } . } \end{array}$

Asa substitute for the non-uniqueness in (9.27),we use-as in the previous subsection $-$ aunique decomposition in the tangent space.Every tangent matrix $\delta Y \in T _ { Y } \mathcal { M } _ { k }$ at $Y = U S V ^ { T }$ is of the form (see Exercise 23)

$$
\delta Y = \delta U S V ^ { T } + U \delta S V ^ { T } + U S \delta V ^ { T } ,
$$

where $\delta S \in \mathbb { R } ^ { k \times k }$ and $\begin{array} { r } { \delta U \in { \cal { I } } _ { U } ^ { } \mathcal { V } _ { m , k } , \ \delta V \in { \cal { I } } _ { V } ^ { } \mathcal { V } _ { n , k } . } \end{array}$ Conversely, $\partial S , \partial U , \partial V$ are uniquelydetermined by $\delta Y$ ifwe impose the orthogonality constraints

$$
\begin{array} { r } { { U ^ { T } \delta U = 0 , } \quad { V ^ { T } \delta V = 0 . } } \end{array}
$$

Equations (9.28)and(9.29) yield

$$
\begin{array} { r l } & { \delta S = U ^ { T } \delta Y V , } \\ & { \delta U = ( I - U U ^ { T } ) \delta Y V S ^ { - 1 } , } \\ & { \delta V = ( I - V V ^ { T } ) \delta Y ^ { T } U S ^ { - T } . } \end{array}
$$

Formulas (9.28)and(9.30) establish an isomorphism between the subspace

$$
\left\{ ( \delta S , \delta U , \delta V ) \in \mathbb { R } ^ { k \times k } \times \mathbb { R } ^ { m \times k } \times \mathbb { R } ^ { n \times k } \big \vert U ^ { T } \delta U = 0 , V ^ { T } \delta V = 0 \right\}
$$

and the tangent space $T _ { Y } \mathcal { M } _ { k }$

Differential Equations for the Factors.The minimization condition (9.25）is equivalent to the orthogonal projection of $A ( t )$ onto the tangent space $T _ { Y ( t ) } \mathcal { M } _ { k }$ find $\dot { Y } \in T _ { Y } \mathcal { M } _ { k }$ (we omit the argument $t$ satisfying

$$
\langle \dot { Y } - \dot { A } , \delta Y \rangle = 0 \quad \mathrm { f o r \ a l l } \delta Y \in T _ { Y } \mathcal { M } _ { k } ,
$$

with the Frobenius inner product $\langle A , B \rangle = \operatorname { t r a c e } ( A ^ { T } B )$ With this formulation we derive differential equations for the factors in the representation (9.27).

Theorem9.2.For $Y = U S V ^ { T } \in \mathcal { M } _ { k }$ with nonsingular $S \in \mathbb { R } ^ { k \times k }$ andwith $U \in \mathbb { R } ^ { m \times k }$ and $V \in \mathbb { R } ^ { n \times k }$ havingorthonormalcolumns,condition(9.25)or(9.31) isequivalent to $\dot { Y } = \dot { U } S V ^ { T } + U \dot { S } V ^ { T } + U S \dot { V } ^ { T } ,$ where

$$
\begin{array} { r c l } { \dot { S } } & { = } & { U ^ { T } \dot { A } V } \\ { \dot { U } } & { = } & { ( I - U U ^ { T } ) \dot { A } V S ^ { - 1 } } \\ { \dot { V } } & { = } & { ( I - V V ^ { T } ) \dot { A } ^ { T } U S ^ { - T } . } \end{array}
$$

Proof.For $u \in \mathbb { R } ^ { m } , v \in \mathbb { R } ^ { n }$ and $B \in \mathbb { R } ^ { m \times n }$ ,we use theidentity

$$
\langle u v ^ { T } , B \rangle = u ^ { T } B v .
$$

In view of(9.29)we require ${ \cal U } ^ { T } { \cal \dot { U } } = { \cal V } ^ { T } { \cal \dot { V } } = 0$ along the solution trajectory inorder   
to define auniquerepresentation of $\dot { Y }$ We first substitute $\delta Y = u _ { i } v _ { j } ^ { T }$ ,for $i , j =$   
$1 , \ldots , k$ ,in(9.31）,where $u _ { i }$ , $v _ { j }$ denote the columns of $U , V$ ,respectively.Thisisof   
thnd si $\partial U = \partial V = 0$ $\delta S .$ wwywe ${ \dot { S } } = U ^ { T } { \dot { A } } V .$ $\begin{array} { r } { \delta Y = \sum _ { j = 1 } ^ { k } \delta u s _ { i j } v _ { j } ^ { T } , i = 1 , . . . , k } \end{array}$   
$\delta u \in \mathbb { R } ^ { n }$ $U$ isarbitrarywith 11 ewisefor $\begin{array} { r } { \delta Y = \sum _ { j = 1 } ^ { k } u _ { j } s _ { j i } \delta v ^ { T } } \end{array}$ ${ \cal U } ^ { T } \delta u = 0$ ,weobtain the stated differential equation with $V ^ { T } \delta v = 0$ thedifereri $V$

Thedifferential equations(9.32）arecloselyrelated todifferential equations for othersmooth matrix decompositions,inparticular the smooth singularvaluedecomposition;see,e.g.,Dieci&Eirola（1999)andWright（1992).Unlikethedifferential equations for singular values given there,the equations(9.32) have no singularities at points where singular values of $Y ( t )$ coalesce.

Fortheminimum-defectlow-rank approximation(9.26)of amatrixdifferential equation ${ \dot { A } } = F ( A )$ ,we just need to replace $\dot { A }$ by $F ( Y )$ for $Y = U S V ^ { T }$ in the differential equations (9.32).

Thematrices $U ( t )$ and $V ( t )$ evolve on Stiefel manifolds.Thedifferential equations(9.32) can thusbe solved numerically by themethods discussed in Sect.IV.9.1.

# IV.10 Exercises

1.Prove that the symplectic Euler method (I.1.9) conservesquadratic invariants of the form (2.5).Explain the“0”entries of Table(I.2.1).

2.Prove that under condition (2.3)a Runge-Kutta method preserves all invariants of theform $I ( y ) = y ^ { I } C y + d ^ { I } y + c$

3.Prove that an $s$ -stagediagonally implicit Runge-Kutta method(i.e., $a _ { i j } = 0$ for $i < j$ )satisfies the condition (2.3)ifand onlyif it is equivalent toacomposition $\phi _ { b _ { s } h } \circ \dots \circ \phi _ { b _ { 1 } h }$ based on the implicit midpointrule.

4.Prove the followingstatements:a) If a partitioned Runge-Kutta method conserves general quadratic invariants $p ^ { T } C p + 2 p ^ { T } D q + q ^ { T } E q$ ,then each of the twoRunge-Kutta methods has to conserve quadratic invariants separately.

b) If both methods, $\left\{ { { b } _ { i } } , { { a } _ { i j } } \right\}$ and $\{ \widehat { b } _ { i } , \widehat { a } _ { i j } \}$ areirreducible,satisfy(2.3)and if (2.7)-(2.8) hold,then we have $b _ { i } = \hat { b } _ { i }$ and $a _ { i j } = \overrightarrow { a } _ { i j }$ for all $i , j$ .

5.Prove that the Gauss methods are the only collocation methods satisfying(2.3). Hint.Use the ideas of the proof ofLemma13.9in Hairer&Wanner(1996).

6.Discontinuous collocation methods with either $b _ { 1 } ~ \neq ~ 0$ or $b _ { s } \neq 0$ (Definition II.1.7) cannot satisfy the criterion (2.3).

7.(Sanz-Serna& Abia 1991,Saito,Sugiura&Mitsui 1992).The condition (2.3) actsas simplifyingassumption for the order conditions ofRunge-Kutta methods.Assume that the order conditions are satisfied for the trees $u$ and $\boldsymbol { v }$ .Prove thatit is satisfied for $u \circ v$ ifandonlyifitissatisfied for $\upsilon \circ u$ and that it is automatically satisfied for trees of the form $u \circ u$

Remark. $u \circ v$ denotes the Butcher product introduced in Sect.VI.7.2.

8.If $L _ { 0 }$ isasymmetric,tridiagonal matrix that is sufficiently close to $\varLambda =$ $\mathrm { d i a g } ( \lambda _ { 1 } , \ldots , \lambda _ { n } )$ ,where $\lambda _ { 1 } > \lambda _ { 2 } > . . . > \lambda _ { n }$ are the eigenvalues of $L _ { 0 }$ ,then the solution of(3.5）with $B ( L ) = L _ { + } - L _ { + } ^ { T }$ converges exponentially fast to the diagonal matrix $\varLambda$ Hence,the numerical solution of(3.5） givesanalgorithm for the computation of the eigenvalues of the matrix $L _ { 0 }$

Hint.Let $\beta _ { 1 } , \ldots , \beta _ { n }$ betheentries in the diagonal of $L$ ,and $\alpha _ { 1 } , \ldots , \alpha _ { n - 1 }$ those in the subdiagonal. Assume that $| \beta _ { k } ( 0 ) - \lambda _ { k } | \le R / 3$ and $| \alpha _ { k } ( 0 ) | \le R$ with some sufficiently small $R$ Prove that $\beta _ { k } ( t ) - \beta _ { k + 1 } ( t ) \geq \mu - R$ and $| \alpha _ { k } ( t ) | \leq R e ^ { - ( \mu - R ) t }$ forall $t \geq 0$ ,where $\mu = \operatorname* { m i n } _ { k } ( \lambda _ { k } - \lambda _ { k + 1 } ) > 0$

9.Elaborate Example4.5 for the special case where $Y$ isamatrix of dimension 2.In particular,showthat(4.6) isthe same as (4.5),and check the formulas for thesimplified Newton iterations.

10.(Brenan,Campbell& Petzold (1996)，Sect.2.5.3).Consider the differential equation $\dot { y } = f ( y )$ with known invariants $g ( y ) = C o n s t$ and assume that $g ^ { \prime } ( y )$ hasfull rank.Provebydifferentiation of theconstraints that,for initial values satisfying $g ( y _ { 0 } ) = 0$ ,thesolution of the differential-algebraic equation (DAE)

$$
\begin{array} { l c l } { { \dot { y } } } & { { = } } & { { f ( y ) + g ^ { \prime } ( y ) ^ { T } \mu } } \\ { { 0 } } & { { = } } & { { g ( y ) } } \end{array}
$$

alsosolvesthediferentialequation $\dot { y } = f ( y )$

Remark.Most methods for DAEs(e.g.,stiffly accurate Runge-Kuta methods orBDF methods) lead to numerical integrators that preserve exactly theconstraints $g ( y ) = 0$ Thedifference from theprojection method of Sect.IV.4is that here the internal stages also satisfy theconstraint.

11.Prove that $\mathrm { S L } ( n )$ isaLie group of dimension $n ^ { 2 } - 1$ ,and that ${ \mathfrak { s l } } ( n )$ is its Lie algebra(see Table6.1 for thedefinitionsof $\mathrm { S L } ( n )$ and ${ \mathfrak { s l } } ( n ) )$

12.Let $G$ beamatrix Lie group and $\mathfrak { g }$ itsLiealgebra.Prove that for $Y \in G$ and $A \in { \mathfrak { g } }$ wehave $Y A Y ^ { - 1 } \in { \mathfrak { g } }$

Hint.Consider the path $\gamma ( t ) = Y \alpha ( t ) Y ^ { - 1 }$

13.Consider a problem $Y = A ( Y ) Y$ ,forwhich $A ( Y ) \in \mathfrak { s o } ( n )$ whenever $Y \in$ ${ \mathrm { O } } ( n )$ ,butwhere $A ( Y )$ isan arbitrary matrix for $Y \not \in \mathrm { O } ( n )$ a)Prove that $Y _ { 0 } \in \mathrm { O } ( n )$ implies $Y ( t ) \in \mathrm { O } ( n )$ forall $t$ . b)Show by acounter-example that the numerical solution of the implicit midpoint rule does not necessarily stay in ${ \mathrm { O } } ( n )$

14.(FengKang& Shang Zai-jiu 1995).Let $R ( z ) = ( 1 + z / 2 ) / ( 1 - z / 2 )$ bethe stability function of the implicit midpoint rule.Prove that for $A \in { \mathfrak { s l } } ( 3 )$ we have

$$
\begin{array} { r } { \operatorname* { d e t } R ( h A ) = 1 \quad \Leftrightarrow \quad \operatorname* { d e t } A = 0 . } \end{array}
$$

15.(Iserles& Ngrsett 1999).Introducing $y _ { 1 } = y$ and $y _ { 2 } = y$ ,write the problem

$$
\ddot { y } + t y = 0 , \qquad y ( 0 ) = 1 , \qquad \dot { y } ( 0 ) = 0
$$

inthe form(7.6).Then apply thenumerical method of Example7.4with different step sizes on the interval $0 \leq t \leq 1 0 0$ .Compare the result with that obtainedby fourth order classical(explicit or implicit)Runge-Kutta methods.

Remark.If $A ( t )$ in(7.6）（or $A ( t , y )$ in(8.1))are much smoother than the solution $y ( t )$ ,thenLie groupmethodsareusuallysuperiortostandard integrators, because Lie group methods approximate $A ( t )$ ,whereas standard methods approximate the solution $y ( t )$ bypolynomials.

16.Deduce the BCH formula from the Magnus expansion (IV.7.5).

Hint.For constant matrices $A$ and $B$ consider the matrix function $A ( t )$ defined by $A ( t ) = B$ for $0 \leq t \leq 1$ and $A ( t ) = A$ for $1 \le t \le 2$

17.(Rodrigues formula,seeMarsden&Ratiu(1999),page291).Prove that

$$
\arg ( \varOmega ) = I \sb { + } \frac { \sin \alpha } { \alpha } \varOmega \sb { + } \frac { 1 } { 2 } \Bigl ( \frac { \sin ( \alpha / 2 ) } { \alpha / 2 } \Bigr ) \sp 2 \varOmega \sp 2 \quad \mathrm { f o r } \quad \varOmega \stackrel { \ldots } { = } \left( \begin{array} { c c c } { 0 } & { - \omega _ { 3 } } & { \omega _ { 2 } } \\ { \omega _ { 3 } } & { 0 } & { - \omega _ { 1 } } \\ { - \omega _ { 2 } } & { \omega _ { 1 } } & { 0 } \end{array} \right)
$$

where $\alpha = \sqrt { \omega _ { 1 } ^ { 2 } + \omega _ { 2 } ^ { 2 } + \omega _ { 3 } ^ { 2 } } ,$ This formula allows foran efficient implementation of the Lie group methods in O(3).

18.The solution of $Y = A ( Y ) Y , Y ( 0 ) = Y _ { 0 }$ isgiven by $Y ( t ) = \exp \bigl ( \varOmega ( t ) \bigr ) Y _ { 0 }$ ， where $\boldsymbol { \Omega } ( t )$ solves the differential equation (8.9).Compute the first terms of the $t$ -expansionof $\boldsymbol { \Omega } ( t )$

Result. $\begin{array} { r } { \Omega ( t ) \ = \ t A ( Y _ { 0 } ) + \frac { t ^ { 2 } } { 2 } A ^ { \prime } ( Y _ { 0 } ) A ( Y _ { 0 } ) Y _ { 0 } \ + \frac { t ^ { 3 } } { 6 } \big ( A ^ { \prime } ( Y _ { 0 } ) ^ { 2 } A ( Y _ { 0 } ) Y _ { 0 } ^ { 2 } \ + \quad } \end{array}$ $A ^ { \prime } ( Y _ { 0 } ) A ( Y _ { 0 } ) ^ { 2 } Y _ { 0 } + A ^ { \prime \prime } ( Y _ { 0 } ) ( A ( Y _ { 0 } ) Y _ { 0 } , A ( Y _ { 0 } ) Y _ { 0 } ) - { \textstyle { \frac { 1 } { 2 } } } \left\lfloor A ( Y _ { 0 } ) , A ^ { \prime } ( Y _ { 0 } ) A ( Y _ { 0 } ) Y _ { 0 } \right\rfloor )$

19.Consider the 2-stage Gauss method of order $p = 4$ In the corresponding Lie groupmethod,eliminate the presence of $\mathcal { Q }$ in $[ \Omega , A ]$ byiteration,and neglect higher order commutators.Show that this leads to

$$
\begin{array} { l } { \displaystyle \Omega _ { 1 } = h \Big ( \frac 1 4 A _ { 1 } + \Big ( \frac 1 4 - \frac { \sqrt { 3 } } 6 \Big ) A _ { 2 } \Big ) - \frac { h ^ { 2 } } 2 \Big ( - \frac 1 { 1 2 } + \frac { \sqrt { 3 } } { 2 4 } \Big ) [ A _ { 1 } , A _ { 2 } ] } \\ { \displaystyle \Omega _ { 2 } = h \Big ( \Big ( \frac 1 4 + \frac { \sqrt { 3 } } 6 \Big ) A _ { 1 } + \frac 1 4 A _ { 2 } \Big ) - \frac { h ^ { 2 } } 2 \Big ( \frac 1 { 1 2 } + \frac { \sqrt { 3 } } { 2 4 } \Big ) [ A _ { 1 } , A _ { 2 } ] } \\ { \displaystyle y _ { 1 } = \exp \Big ( { \hat { h } \Big ( \frac 1 2 A _ { 1 } + \frac 1 2 A _ { 2 } \Big ) - \hat { h } ^ { 2 } \frac { \sqrt { 3 } } { 1 2 } } [ A _ { 1 } , A _ { 2 } ] \Big ) y _ { 0 , } } \end{array}
$$

where $A _ { i } = A ( Y _ { i } )$ and $Y _ { i } = \exp ( \varOmega _ { i } ) y _ { 0 } .$ Prove that this isaLiegroupmethod oforder4.Is itsymmetric?

20.In Zanna(1999)aLie group method similar to that of Exercise 19 is presented. Theonly difference isthat the coefficients $( - 1 / 1 2 + { \sqrt { 3 } } / 2 4 )$ and $( 1 / 1 2 +$ $\sqrt { 3 } / 2 4 )$ inthe formulas for $\Omega _ { 1 }$ and $\Omega _ { 2 }$ are replaced with $( - 5 / 7 2 + \sqrt { 3 } / 2 4 )$ and : $( 5 / 7 2 + { \sqrt { 3 / 2 4 } } )$ ,respectively.Is there anerror somewhere?Are bothmethods of order4?

21.Show that for given $\bar { Y }$ the solution of problem （9.7）is $Y ~ = ~ U V ^ { T }$ where $Y = U \Sigma V ^ { T }$ is the singular value decomposition of $\bar { Y }$

Hint.Since $\| U S V ^ { I } \| _ { F } = \| S \| _ { F }$ holds for all orthogonal matrices $U$ and $V$ , it is sufficient toconsider the case $\boldsymbol { Y } = ( \boldsymbol { \Sigma } , 0 ) ^ { T }$ with $\Sigma = \mathrm { d i a g } ( \sigma _ { 1 } , \dots , \sigma _ { k } ) ,$ Prove that $\begin{array} { r } { \| ( \Sigma , 0 ) ^ { T } - Y \| _ { F } ^ { 2 } \geq \sum _ { i = 1 } ^ { k } ( \sigma _ { i } - 1 ) ^ { 2 } } \end{array}$ for allmatrices $Y$ satisfying $Y ^ { T } Y = I$

22.Show that the solution of the matrix differential equation $\dot { Y } = A ( t ) Y$ on $\mathbb { R } ^ { n \times k }$ with initial values $Y _ { 0 } \in \mathcal { V } _ { n , k }$ ,can be decomposed as

$$
Y ( t ) = U ( t ) S ( t ) , \qquad \mathrm { w h e r e } ~ U ( t ) \in \mathcal { V } _ { n , k } , ~ S ( t ) \in \mathbb { R } ^ { k \times k }
$$

satisfy the differential equations

$$
\dot { S } = U ^ { T } A U S , \qquad \dot { U } = ( I - U U ^ { T } ) A U
$$

with initial values $S _ { 0 } = I$ , $U _ { 0 } = Y _ { 0 }$

Remark:These differential equations can be used for the computation ofLyapunov exponents as an alternative to thedifferential equations discussed in Bridges&Reich(20o1)and Dieci,Russell&vanVleck(1997).

23.Consider the map ${ \mathrm { G L } } ( k ) \times \mathcal { V } _ { m , k } \times \mathcal { V } _ { n , k } \longrightarrow { \mathcal { M } } _ { k }$ that associates to $( S , U , V )$ the rank- $k$ matrix $Y = U S V ^ { T } .$ Showthattheextendedtangentmap

$$
\begin{array} { r l } & { \mathbb { R } ^ { k \times k } \times T _ { U } \mathcal { V } _ { m , k } \times T _ { V } \mathcal { V } _ { n , k } \to T _ { Y } \mathcal { M } _ { k } \times \mathfrak { s o } ( k ) \times \mathfrak { s o } ( k ) } \\ & { ( \delta S , \delta U , \delta V ) \mapsto ( \delta U S V ^ { T } + U \delta S V ^ { T } + U S \delta V ^ { T } , U ^ { T } \delta U , V ^ { T } \delta V ) } \end{array}
$$

is an isomorphism.

24.Let $A ( t ) \ \in \mathbb { R } ^ { n \times n }$ besymmetric and depend smoothly on $t$ Show that the solution $P ( t ) \in \mathcal { G } _ { n , k }$ of the dynamical low-rank approximation problem on the Grassmann manifold,

$$
\dot { P } \in T _ { P } \mathcal { G } _ { n , k } \qquad \mathrm { w i t h } \quad \| \dot { P } - \dot { A } \| _ { F } = \operatorname* { m i n } \{ ,
$$

is given as $P = Y Y ^ { T }$ where $\mathcal { Y } \in \mathcal { V } _ { n , k }$ solves thedifferential equation

$$
\begin{array} { r } { \dot { Y } = ( I - Y Y ^ { T } ) \dot { A } Y . } \end{array}
$$

# Chapter V. Symmetric Integration and Reversibility

Symmetric methods of thischapter and symplectic methods of the next chapter play acentral role in the geometric integration of differential equations.We discuss reversible differential equationsand reversible maps,and we explain how symmetric integratorsarerelated to them.We study symmetric Runge-Kuttaand composition methods,and we show how standard approaches for solvingdifferential equations onmanifolds can be symmetrized.A theoretical explanation of the excellent longtimebehaviour of symmetric methodsappliedto reversibledifferential equations will be given in Chap.XI.

# V.1Reversible Differential Equationsand Maps

Conservative mechanical systems have the property that inverting the initial direction of the velocity vector and keeping the initial position does not change the solutiontrajectory,itonly invertsthedirection ofmotion.Such systemsare“reversible. We extend this notion to more general situations.

Definition 1.1. Let $\rho$ beaninvertible linear transformation in the phase space of $\dot { y } = f ( y ) .$ Thisdifferential equationand the vector field $f ( y )$ are called $\rho$ -reversible if

$$
\rho f ( y ) = - f ( \rho y ) \qquad { \mathrm { f o r ~ a l l ~ } } y .
$$

![](images/55a3cd8d55787aa8a5a618b4fdc0c27e12a1b345fd0cae9779afc7c68d4b315a.jpg)  
Fig.1.1.Reversible vector field(left picture)and reversible map(right picture)

This propertyis illustrated inthe left picture ofFig.I.1.For $\rho$ -reversibledifferential equations the exact flow $\varphi _ { 1 } ( y )$ satisfies

$$
\rho \circ \varphi _ { t } = \varphi _ { - t } \circ \rho = \varphi _ { t } ^ { - 1 } \circ \rho
$$

(see the picture to the right in Fig.1.1).The right identity isa consequence of the group property $\varphi _ { t } \circ \varphi _ { s } = \varphi _ { t + s }$ ,andtheleftidentityfollowsfrom

$$
\begin{array} { r c l } { \displaystyle \frac { d } { d t } \big ( \rho \circ \varphi _ { t } \big ) ( y ) } & { = } & { \rho f \Big ( \varphi _ { t } ( y ) \Big ) = - f \Big ( \big ( \rho \circ \varphi _ { t } \big ) ( y ) \Big ) } \\ { \displaystyle \frac { d } { d t } \big ( \varphi _ { - t } \circ \rho \big ) ( y ) } & { = } & { - f \Big ( \big ( \varphi _ { - t } \circ \rho \big ) ( y ) \Big ) , } \end{array}
$$

because allexpressions of(1.2) satisfy the same differential equation with the same initialvalue $( \rho \circ \varphi _ { 0 } ) ( y ) = ( \varphi _ { 0 } \circ \rho ) ( y ) = \rho y .$ Formula (1.2)motivates the following definition.

Definition1.2.Amap $\varPhi ( y )$ is called $\rho$ -reversibleif

$$
\rho \circ \varPhi = \varPhi ^ { - 1 } \circ \rho .
$$

Example1.3.Animportant example is the partitioned system

$$
\dot { u } = f ( u , v ) , \qquad \dot { v } = g ( u , v ) ,
$$

where $f ( u , - v ) = - f ( u , v )$ and $g ( u , - v ) = g ( u , v ) ,$ Here,the transformation $\rho$ is given by $\rho ( u , v ) = ( u , - v )$ Ifwecallavectorfieldoramapreversible(without specifyingthe transformation p),we mean thatitis $\rho$ -reversiblewiththisparticular .All second order differential equations $\ddot { u } = g ( u )$ written as ${ \dot { u } } = v$ ， $\dot { v } = g ( u )$ $\rho$   
arereversible.Asafirstimplication ofreversibility onthedynamicswemention the following fact:if $u$ and $\boldsymbol { v }$ arescalar,and if（1.3）isreversible,thenanysolution that crosses the $_ u$ -axistwiceisperiodic(Exercise5,seealso the solution of the pendulum problem in Fig.I.1.4).

Itisnatural to search for numerical methods that produceareversible numerical flowwhen theyare applied toareversibledifferential equation.We then expect the numerical solution to have long-time behaviour similar to that of the exact solution; seeChap.XI for more precise statements.It turns out that the $\rho$ -reversibilityofa numerical one-step method is closely related to the concept of symmetry.

Thus themethod is theoreticallysymmetrical or reversible,aterminology wehave never seen applied elsewhere. (P.C.Hammer&J.W.Hollingsworth1955)

Definition1.4.A numerical one-step method $\varPhi _ { h }$ is called symmetric or timereversible,ifitsatisfies

$$
\varPhi _ { h } \circ \varPhi _ { - h } = i d \qquad \mathrm { o r ~ e q u i v a l e n t l y } \qquad \varPhi _ { h } = \varPhi _ { - h } ^ { - 1 } .
$$

With the Definition II.3.1of theadjoint method (i.e., $\bar { \Phi } _ { h } ^ { * } = \bar { \Phi } _ { - h } ^ { - 1 }$ ),thecondition forsymmetryreads $\varPhi _ { h } = \varPhi _ { h } ^ { * } .$ Amethod $y _ { 1 } = \varPhi _ { h } ( y _ { 0 } )$ is symmetric if exchanging $y _ { 0 }  y _ { 1 }$ and $h  - h$ leaves themethodunaltered.In Chap.Iwe havealready encountered the implicit midpoint rule (I.1.7)and the Stormer-Verlet scheme(I.1.17), both of which aresymmetric.Many more symmetric methodswill be givenin the following sections.

Theorem1.5.Ifanumerical method,applied toa $\rho$ -reversibledifferentialequation,satisfies

$$
\rho \circ \varPhi _ { h } = \varPhi _ { - h } \circ \rho ,
$$

then the numerical flow $\phi _ { h }$ isa $\rho$ -reversiblemapifandonlyif $\phi _ { h }$ isasymmetric method.

Proof.Asaconsequence of(1.4) the numerical flow $\phi _ { h }$ is -reversibleifand only if $\Phi _ { - h } \circ \rho = \varPhi _ { h } ^ { - 1 } \circ \rho$ Since $\rho$ isaninvertibletrasoatioisisqaletto the symmetry of the method $\phi _ { h }$ □

Similarly,it isalso true thatasymmetric method is $\rho$ -reversibleifandonlyif the $\rho$ -compatibilitycondition（1.4）holds.

Compared to the symmetry of themethod,condition(1.4） ismuch lessrestrictive.It is automatically satisfiedbymost numerical methods.Let usbriefly discuss thevalidityof(1.4) fordifferentclassesofmethods.

·Runge-Kutta methods (explicit or implicit) satisfy(1.4)without any restriction other than(1.1）onthevector field(Stoffer 1988).Letus illustrate the proofwith the explicit Euler method $\Phi _ { h } ( y _ { 0 } ) = y _ { 0 } + h f ( y _ { 0 } )$

$$
( \rho \circ \varPhi _ { h } ) ( y _ { 0 } ) = \rho y _ { 0 } + h \rho f ( y _ { 0 } ) = \rho y _ { 0 } - h f ( \rho y _ { 0 } ) = \varPhi _ { - h } ( \rho y _ { 0 } ) .
$$

·Partitioned Runge-Kutta methodsapplied toapartitioned system(1.3) satisfy the condition(1.4)if $\rho ( u , v ) = \left( \rho _ { 1 } ( u ) , \rho _ { 2 } ( v ) \right)$ with invertible $\rho _ { 1 }$ and $\rho _ { 2 }$ Theproof is thesameas for Runge-Kutta methods.Notice that the mapping $\rho ( u , v ) = ( u , - v )$ ofExample 1.3is of thisspecial form.

Compositionmethods.If twomethods $\phi _ { h }$ and $\psi _ { h }$ satisfy (1.4）,then so does the adjoint $\Phi _ { h } ^ { * }$ and the composition $\phi _ { h } \circ \psi _ { h }$ Consequently,the composition methods (3.1）and(3.2） below,which composeabasicmethod $\phi _ { h }$ and its adjoint with different step sizes,have the property(1.4) provided the basic method $\phi _ { h }$ hasit.

Splittingmethods are based on a splitting $\dot { y } = f ^ { \left[ 1 \right] } \left( y \right) + f ^ { \left[ 2 \right] } \left( y \right)$ ofthe differential fows equation.If both vector fields, $\varphi _ { h } ^ { [ 1 ] }$ and $\varphi _ { h } ^ { [ 2 ] }$ $f ^ { [ 1 ] } ( y )$ and $f ^ { [ 2 ] } ( y )$ ,satisfy(1.1）,thentheirexact the property(1.4).

Fordifferential equations on manifoldswe haveto assume that $\rho$ maps $\mathcal { M }$ to $\mathcal { M }$ .Otherwise,condition（1.1） does not make sense.For the projection method ofAlgorithm IV.4.2 with orthogonal projection onto the manifold we have:if thebasicmethod satisfies（1.4）and if $\rho$ isanorthogonal matrix,then it satisfies (1.4)as well.This follows from the fact that the tangent and normal spaces satisfy

$T _ { \rho y } \mathcal { M } = \rho T _ { y } \mathcal { M }$ and $N _ { \rho y } M = \rho ^ { - T } N _ { y } { \mathcal { M } }$ ,respectively.A similar result holds formethods based on local coordinates,if the local parametrizationiswell chosen.For example,this is the caseif $\rho \psi ( z )$ is the parametrization at $\rho y _ { 0 }$ whenever $\psi ( z )$ is the parametrization at $y _ { 0 }$

# V.2 Symmetric Runge-Kutta Methods

Wegive a characterization of symmetric methods of Runge-Kutta type and mention some important examples.

# V.2.1 Collocation and Runge-Kutta Methods

Symmetric collocation methodsare characterized by the symmetry of the collocation points with respect to the midpoint of the integration step.

Theorem2.1. Theadjointmethodofa collocationmethod(Definition I.1.3)based on $c _ { 1 } , \ldots , c _ { s }$ is a collocation method based on $c _ { 1 } ^ { * } , \ldots , c _ { s } ^ { * }$ ,where

$$
c _ { i } ^ { * } = 1 - c _ { s + 1 - i } .
$$

In thecase that $c _ { i } = 1 - c _ { s + 1 - i }$ forall $i$ ,thecollocationmethodis symmetric.

Theadjoint method of a discontinuous collocation method (Definition II.1.7) basedon $b _ { 1 } , b _ { s }$ and $c _ { 2 } , \ldots , c _ { s - 1 }$ isadiscontinuous collocation method based on $b _ { 1 } ^ { * } , b _ { s } ^ { * }$ and $c _ { 2 } ^ { * } , \ldots , c _ { s - 1 } ^ { * }$ ,where

$$
b _ { 1 } ^ { * } = b _ { s } , b _ { s } ^ { * } = b _ { 1 } a n d c _ { i } ^ { * } = 1 - c _ { s + 1 - i } .
$$

Inthe case that $b _ { 1 } = b _ { s }$ and $c _ { i } = 1 - c _ { s + 1 - i }$ forall $i$ ,thediscontinuous collocation methodissymmetric.

![](images/be01240ca2ca180fffc3b0eacfa30b63d80a6bd423db88333f50c7b2edcfa30d.jpg)  
Fig.2.1.Symmetry of collocation methods

Proof.Exchanging $( t _ { 0 } , y _ { 0 } )  ( t _ { 1 } , y _ { 1 } )$ and $h  - h$ in thedefinition of acollocation method we get $u ( t _ { 1 } ) = y _ { 1 }$ ， ${ \dot { u } } ( t _ { 1 } - c _ { i } h ) = f { \big ( } t _ { 1 } - c _ { i } h , u ( t _ { 1 } - c _ { i } h ) { \big ) }$ ,and $y _ { 0 } = u ( t _ { 1 } - h )$ Inserting $t _ { 1 } = t _ { 0 } + h$ thisyields the collocation method based on $c _ { i } ^ { * }$ of(2.1）.Observe that the $c _ { i } ^ { * }$ canbearbitrarily permuted.For discontinuous collocation methods the proof is similar. □

Thepreceding theorem immediatelyyields the following result.

Corollary2.2.TheGauss formulas(Table II.1.I),aswell as theLobattoIIIA(TableII.1.2)andLobattoIIIBformulas(TableII.1.4) aresymmetric integrators. □

Theorem2.3 (Stetter1973,Wanner 1973).Theadjoint method ofans-stage Runge-Kutta method(II.1.4) isagain an s-stage Runge-Kutta method.Its coeffcientsare given by

$$
a _ { i j } ^ { * } = b _ { s + 1 - j } - a _ { s + 1 - i , s + 1 - j } , \qquad b _ { i } ^ { * } = b _ { s + 1 - i } .
$$

$$
a _ { s + 1 - i , s + 1 - j } + a _ { i j } = b _ { j } \qquad f o r \ : a l l \ : i , j ,
$$

thentheRunge-Kuttamethod(II.1.4)issymmetric.2

ProofExchanging $y _ { 0 }  y _ { 1 }$ and $h  - h$ in theRunge-Kutta formulas yields

$$
k _ { i } = f { \Big ( } y _ { 0 } + h \sum _ { j = 1 } ^ { s } ( b _ { j } - a _ { i j } ) k _ { j } { \Big ) } , \qquad y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } .
$$

Since the values $\begin{array} { r } { \sum _ { j = 1 } ^ { \circ } ( b _ { j } - a _ { i j } ) = 1 - c _ { i } } \end{array}$ appearinreverseorderereplace $k _ { i }$ by $k _ { s + 1 - i }$ in(2.5),and then we substitute allindices $i$ and $j$ by $s + 1 - i$ and $s + 1 - j$ , respectively.This proves(2.3).

The assumption (2.4)implies $a _ { i j } ^ { * } = a _ { i j }$ and $b _ { i } ^ { * } = b _ { i }$ ,sothat $\varPhi _ { h } ^ { * } = \varPhi _ { h }$

Explicit Runge-Kutta methods cannot fulfill condition(2.4)with $i = j$ ,anditis notdifficult to see that no explicit Runge-Kutta can be symmetric(Exercise2).Let ustherefore turn our attention to diagonally implicit Runge-Kuttamethods(DIRK), forwhich $a _ { i j } = 0$ for $i < j$ ,butwith diagonal elements that can be non-zero.In this case condition(2.4） becomes

$$
a _ { i j } = b _ { j } = b _ { s + 1 - j } \quad \mathrm { f o r ~ } i > j , \qquad a _ { j j } + a _ { s + 1 - j , s + 1 - j } = b _ { j } .
$$

TheRunge-Kutta tableau of such amethod is thus of the form (e.g.,for $s = 5$ ）

$$
\begin{array} { c } { { c _ { 1 } } } \\ { { c _ { 2 } } } \\ { { c _ { 3 } } } \\ { { 1 - c _ { 2 } } } \\ { { 1 - c _ { 1 } \left| \begin{array} { c c c c c } { { a _ { 1 1 } } } & { { } } & { { } } & { { } } & { { a _ { 1 4 } } } \\ { { b _ { 1 } } } & { { a _ { 2 2 } } } & { { } } & { { } } & { { } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { a _ { 3 3 } } } & { { } } & { { } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { a _ { 4 4 } } } & { { } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { b _ { 2 } } } & { { a _ { 5 5 } } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { b _ { 2 } } } & { { b _ { 1 } } } \end{array} \right| } } \end{array}
$$

with $a _ { 3 3 } = b _ { 3 } / 2$ ， $a _ { 4 4 } = b _ { 2 } - a _ { 2 2 }$ ,and $a _ { 5 5 } = b _ { 1 } - a _ { 1 1 } . $ If one of the $b _ { i }$ vanishes, then the corresponding stage does not influence the numerical result.This stage can therefore be suppressed,so that the method is equivalent to one with fewer stages. Ournext result shows that methods(2.7） can be interpreted as the composition of $\theta$ -methods,which aredefinedas

$$
\bar { \Phi } _ { h } ^ { \theta } ( y _ { 0 } ) = y _ { 1 } , \qquad \mathrm { w h e r e } \qquad y _ { 1 } = y _ { 0 } + h f \bigl ( ( 1 - \theta ) y _ { 0 } + \theta y _ { 1 } \bigr ) .
$$

Observe that the adjoint of the $\theta$ -method is =-.

Theorem2.4.A diagonally implicit Runge-Kuttamethod satisfying the symmetry condition(2.4) and $b _ { i } \neq 0$ isequivalenttoacomposition of $\theta$ -methods

$$
\phi _ { b _ { 1 } h } ^ { \alpha _ { 1 } * } \circ \varPhi _ { b _ { 2 } h } ^ { \alpha _ { 2 } * } \circ \dots \circ \varPhi _ { b _ { 2 } h } ^ { \alpha _ { 2 } } \circ \varPhi _ { b _ { 1 } h } ^ { \alpha _ { 1 } } ,
$$

where $\alpha _ { i } = \left. a _ { i i } \right/ b _ { i }$

ProofSince the $\theta$ -methodisaRunge-Kuttamethodwith tableau

$$
\frac { \theta \mid \theta } { \mid 1 }
$$

this follows from the discussionin Sect.III.1.3.We have used +1- $\boldsymbol { \Phi } _ { b _ { s + 1 - i } h } ^ { \alpha _ { s + 1 - i } } = \boldsymbol { \Phi } _ { b _ { i } h } ^ { \alpha _ { i } * }$ which holds,because $b _ { s + 1 - i } = b _ { i }$ and $\alpha _ { s + 1 - i } = 1 - \alpha _ { i }$ by (2.6). □

A more detailed discussion of such methods is therefore postponed to Sect.V.3 onsymmetric composition methods.

# V.2.2Partitioned Runge-Kutta Methods

Applying partitioned Runge-Kutta methods (II.2.2)to general partitioned systems

$$
\dot { y } = f ( y , z ) , \qquad \dot { z } = g ( y , z ) ,
$$

itisobvious that for their symmetry both Runge-Kutta methods have to be symmetric(because $\dot { y } = f ( y )$ and $\dot { z } = g ( z )$ are special cases of(2.1O)).The proof of the following resultis identical to that of Theorem 2.3and therefore omitted.

Theorem2.5.Ifthecoefcientsof both Runge-Kuttamethods $b _ { i } , a _ { i j }$ and $\widehat { b } _ { i } , \widehat { a } _ { i j }$ satisfythecondition(2.4),thenthepartitionedRunge-Kuttamethod(II.2.2)issymmetric. □

Asaconsequence of this theorem we obtain that the Lobatto IIIA-IIB pair (see Sect.II.2.2)and,in particular,the Stormer-Verlet schemeare symmetric integrators.

Aninteresting feature of partitioned Runge-Kutta methods is the possibility of havingexplicit,symmetric methodsforproblems of the form

$$
\begin{array} { r } { \dot { y } = f ( z ) , \qquad \dot { z } = g ( y ) . } \end{array}
$$

Second order differential equations $\ddot { y } = g ( y )$ ,written in theform $\dot { y } = z , \dot { z } = g ( y )$ havethis structure,and alsoall Hamiltonian systemswith separable Hamiltonian $H ( p , q ) = T ( p ) + V ( q )$ It is not possible toget explicit symmetric integrators with non-partitioned Runge-Kutta methods (Exercise 2).

The Stormer-Verlet method(Table II.2.1) applied to(2.11) reads

$$
\begin{array} { r c l } { { } } & { { } } & { { z _ { 1 / 2 } ~ = ~ z _ { 0 } + { \displaystyle \frac { h } { 2 } } g ( y _ { 0 } ) } } \\ { { } } & { { } } & { { y _ { 1 } ~ = ~ y _ { 0 } + h f ( z _ { 1 / 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { z _ { 1 } ~ = ~ z _ { 1 / 2 } + { \displaystyle \frac { h } { 2 } } g ( y _ { 1 } ) } } \end{array}
$$

and is the composition $\boldsymbol { \Phi } _ { h / 2 } ^ { * } \circ \boldsymbol { \Phi } _ { h / 2 }$ where

$$
{ \left( \begin{array} { l } { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right) } = \varPhi _ { h } \left( { \begin{array} { l } { y _ { 0 } } \\ { z _ { 0 } } \end{array} } \right) , \qquad { \begin{array} { l } { y _ { 1 } = y _ { 0 } + h f ( z _ { 1 } ) } \\ { z _ { 1 } = z _ { 0 } + h g ( y _ { 0 } ) } \end{array} }
$$

is the symplectic Euler method and

$$
{ \left( \begin{array} { l } { y _ { 1 } } \\ { z _ { 1 } } \end{array} \right) } = \varPhi _ { h } ^ { * } \left( { \begin{array} { l } { y _ { 0 } } \\ { z _ { 0 } } \end{array} } \right) , \qquad { \begin{array} { l } { y _ { 1 } = y _ { 0 } + h f ( z _ { 0 } ) } \\ { z _ { 1 } = z _ { 0 } + h g ( y _ { 1 } ) } \end{array} }
$$

itsadjoint.All these methodsare obviously explicit.How can they be extended to higher order?Theidea isto consider partitioned Runge-Kutta methods based on diagonally implicit methods such as in(2.7).If $a _ { i i } \cdot \widehat { a } _ { i i } = 0$ ,then one component ofthe $\textit { i }$ thstageis given explicitlyand,dueto thespecial structure of(2.11),the othercomponent is also obtainedina straightforward manner.In order to achieve $a _ { i i } \cdot \widehat { a } _ { i i } = 0$ witha symmetric partitioned method,we have to assume that $s$ ,the number of stages,is even.

Theorem2.6.ApartitionedRunge-Kuttamethod,basedontwodiagonallyimplicit methods satisfying $a _ { i i } \cdot \widehat { a } _ { i i } = 0$ and(2.4） with $b _ { i } \neq 0$ and $\hat { b _ { i } } \neq 0$ ,isequivalent toacompositionof $\phi _ { b _ { i } h }$ "and $\boldsymbol { \phi } _ { b , h } ^ { * }$ with $\phi _ { h }$ and $\boldsymbol { \Phi } _ { h } ^ { * }$ given by(2.12）and (2.13). respectively. □

Forexample,the partitioned method

$$
\begin{array} { r } { \left| \begin{array} { l l l l l l l } { 0 } & & & & & & \\ { b _ { 1 } } & { b _ { 2 } } & & & & & \\ { b _ { 1 } } & { b _ { 2 } } & { 0 } & & & & \\ { b _ { 1 } } & { b _ { 2 } } & { 0 } & & & & \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 2 } } & { b _ { 1 } } & & \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 2 } } & { b _ { 1 } } & & \end{array} \right| \quad \frac { \widehat { b } _ { 1 } } { \widehat { b } _ { 1 } } \quad \widehat { b } _ { 2 } \quad \widehat { b } _ { 2 } \quad 0 } \end{array}
$$

satisfies the assumptions of the preceding theorem.Since the methods have identical stages,the numerical result only depends on $\widehat { b } _ { 1 }$ ， $b _ { 1 } + b _ { 2 }$ , $\widehat { b } _ { 2 } + \widehat { b } _ { 3 }$ , $b _ { 3 } + b _ { 4 }$ and $b _ { 4 }$ Therefore,we can assume that $\widehat { b } _ { i } \ = \ b _ { i }$ and the method is equivalent tothe composition $\phi _ { b _ { 1 } h } ^ { * } \circ \phi _ { b _ { 2 } h } \circ \phi _ { b _ { 2 } h } ^ { * } \circ \phi _ { b _ { 1 } h } .$

# V.3Symmetric Composition Methods

InSect.II.4 the idea of compositionmethods is introduced,and a systematic way ofobtaining high-ordermethods is outlined.These methods,based on(II.4.4)or on (II.4.5),turn out to besymmetric,but they require too manystages.A theory of order conditions for general composition methods is developed in Sect.II.3.Here,we applythis theory to theconstruction of high-ordersymmetric methods.We mainly follow two lines.

·Symmetric composition offirst order methods.

$$
\varPsi _ { h } = \varPhi _ { \alpha _ { s } h } \circ \varPhi _ { \beta _ { s } h } ^ { * } \circ \dots \circ \varPhi _ { \beta _ { 2 h } } ^ { * } \circ \varPhi _ { \alpha _ { 1 } h } \circ \varPhi _ { \beta _ { 1 } h } ^ { * } ,
$$

where $\phi _ { h }$ isanarbitrary first order method.Inordertomake thismethod symmetric,we assume $\alpha _ { s } = \beta _ { 1 }$ , $\alpha _ { s - 1 } = \beta _ { 2 }$ ,etc.

·Symmetric composition ofsymmetric methods.

$$
\varPsi _ { h } = \varPhi _ { \gamma _ { s } h } \circ \varPhi _ { \gamma _ { s - 1 } h } \circ . . . \circ \varPhi _ { \gamma _ { 2 } h } \circ \varPhi _ { \gamma _ { 1 } h } ,
$$

where $\phi _ { h }$ is a symmetric second order method and $\gamma _ { s } = \gamma _ { 1 }$ , $\gamma _ { s - 1 } = \gamma _ { 2 }$ ,etc.

# V.3.1 Symmetric Composition ofFirst Order Methods

Because ofLemma3.2below,everymethod(3.2) isaspecial case ofmethod(3.1). Inthis subsectionweconcentrate on methods that are of the form (3.1） but not of the form (3.2）.

Forconstructingmethods(3.1） of a certain order,one has to solve the system ofnonlinear equations given in Theorem II.3.14(see also Example III.3.15).The symmetry assumption on the coefficients considerably simplifies this system.

Theorem3.1.Ifthecoeffcientsofmethod(3.1） satisfy $\alpha _ { s + 1 - i } = \beta _ { i }$ foralli,then it issufficient to consider thosetreeswith odd $\| \tau \|$ .

Proof.Thisisaconsequence of Theorem II.3.2(themaximal order of symmetric methodsiseven).Infact,if theconditionfororder1issatisfied,itisautomatically oforder2.If,inaddition,theconditions for order3are satisfied,itisautomatically of order4,etc. □

Itmay come asa surprise that the popular leapfrog...can be beaten,but only slightly. （R.I.McLachlan 1995)

MethodsofOrder2.Theonlyremainingconditionforodertwois $\scriptstyle \sum _ { k = 1 } ^ { s } ( \alpha _ { k } +$ $\beta _ { k } ) = 1$ ,and,for $s = 1$ ,thesymmetryrequirementleadsto $\Phi _ { h / 2 } \circ \Phi _ { h / 2 } ^ { * }$ Depending on the choice of $\phi _ { h }$ ,thismethodis equivalent to themidpointrule,thetrapezoidal rule,ortheStormer-Verlet scheme,all very famousand frequently used.However, McLachlan (1995）discovered that the case $s = 2$ can be slightly more advantageous.We obtain

$$
\varPhi _ { \alpha h } \circ \varPhi _ { ( 1 / 2 - \alpha ) h } ^ { * } \circ \varPhi _ { ( 1 / 2 - \alpha ) h } \circ \varPhi _ { \alpha h } ^ { * } ,
$$

where $\alpha$ isafreeparameter,which canserve for clever tuning.

Minimizing the Local Error of Composition Methods.Subtracting the $B _ { \infty }$ - seriesof the numerical and the exact solutions (see Sect.III.3.2),we obtain

![](images/2bd87ff01103559bd5e38d6f4bcc4689d14d1ebeef98acb113eefa955999d937.jpg)  
Fig.3.1.The error functions $\left| q _ { i } ( \alpha ) \right|$ defined in(3.5) (left picture).Work-precision diagrams fortheKepler problem(asin Fig.II.4.4)and formethod(3.3）with $\alpha = 0 . 2 5$ (Stormer-Verlet), $\alpha = 0 . 1 9 3 2$ (McLachlan）,and $\alpha = 0 . 2 2$ “IE":method $\varPhi _ { h }$ treats position by implicit Euler,velocity byexplicitEuler;“El":method $\varPhi _ { h }$ treats position byexplicit Euler,velocity byimplicit Euler

$$
\bar { \psi } _ { h } ( y ) - \varphi _ { h } ( y ) = h ^ { p + 1 } \sum _ { \| \tau \| = p + 1 } \frac { 1 } { \sigma ( \tau ) } \Bigl ( a ( \tau ) - { \bf e } ( \tau ) \Bigr ) { \cal F } ( \tau ) ( y ) + \mathcal { O } ( h ^ { p + 2 } ) .
$$

Assuming that the basic method has an expansion $\begin{array} { r } { \Phi _ { h } ( y ) = y + h f ( y ) + h ^ { 2 } d _ { 2 } ( y ) + } \end{array}$ $h ^ { 3 } d _ { 3 } ( y ) + \ldots ,$ we obtain formethod(3.3),similarto(II.3.3),thelocalrro

$$
\begin{array} { r l } & { h ^ { 3 } \Big ( q _ { 1 } ( \alpha ) d _ { 3 } ( y ) + q _ { 2 } ( \alpha ) \big ( d _ { 2 } ^ { \prime } f \big ) ( y ) + q _ { 3 } ( \alpha ) \big ( f ^ { \prime } d _ { 2 } \big ) ( y ) } \\ & { \qquad + \frac { 1 } { 2 } q _ { 4 } ( \alpha ) \big ( f ^ { \prime \prime } ( f , f ) \big ) ( y ) + q _ { 5 } ( \alpha ) \big ( f ^ { \prime } f ^ { \prime } f \big ) ( y ) \Big ) + \mathcal { O } ( h ^ { 4 } ) , } \end{array}
$$

which contains one term for each of the 5trees $\tau \in { \mathcal { T } } _ { \infty }$ with $| | \tau | | = 3$ The $q _ { i } ( \alpha )$ are the polynomials

$$
\begin{array} { l } { { q _ { 1 } ( \alpha ) = \displaystyle \frac { 1 } { 4 } \big ( 1 - 6 \alpha + 1 2 \alpha ^ { 2 } \big ) , \qquad q _ { 2 } ( \alpha ) = \displaystyle \frac { 1 } { 4 } \big ( - 1 + 6 \alpha - 8 \alpha ^ { 2 } \big ) , \ } } \\ { { q _ { 3 } ( \alpha ) = - \alpha ^ { 2 } , \qquad q _ { 4 } ( \alpha ) = \displaystyle \frac { 1 } { 6 } \big ( 1 - 6 \alpha + 6 \alpha ^ { 2 } \big ) , \qquad q _ { 5 } ( \alpha ) = \frac { 1 } { 3 } q _ { 1 } ( \alpha ) , } } \end{array}
$$

which areplotted inthe left picture of Fig.3.1.Ifweallowarbitrary basicmethods andarbitraryproblems,all elementarydifferentialsinthe local errorare independent,and there is no overall optimal value for $\alpha$ We see that the modulus of $q _ { 1 } ( \alpha )$ and $q _ { 2 } ( \alpha )$ areminimal for $\alpha = 1 / 4$ ,which is precisely the value corresponding toa double application of $\phi _ { h / 2 } \circ \phi _ { h / 2 } ^ { * }$ withhalvedstepsize.Butthevalues $\left| q _ { 3 } ( \alpha ) \right|$ and $\left| q _ { 4 } ( \alpha ) \right|$ become smaller with decreasing $\alpha$ (close to $\alpha = 1 / 4$ .McLachlan(1995) thereforeminimizes some norm of the error(see Exercise 4)and arrives at the value $\alpha = 0 . 1 9 3 2$ .

Inthenumerical experiment of Fig.3.1weapplymethod(3.3)with three differentvalues of $\alpha$ totheKepler problem(withdataasin Fig.II.4.4and the symplectic Euler method for $\varPhi _ { h }$ .Once we treat the position variable by the implicit Euler methodand thevelocity variableby the explicit Eulermethod (central picture),and once the other way round(right picture).We notice that the methodwhich is best in one case is worst in the other.

This simple experiment shows that choosing the free parameters of the method byminimizing some arbitrary measure of the error coefficients isproblematic.For higher ordermethods there are many more expressions in the dominating term of thelocalerror(for example:29 terms for $| | \tau | | = 5$ ).Thecorresponding functions $q _ { i }$ givealot of information on thelocal error,and they indicate theregion of parametersthat produce good methods.But,unless more information is known about the problem(second orderdifferential equation,nearly integrable systems),one usually minimizes,for orders of8or1O,just the maximal values of the $\alpha _ { i } , \beta _ { i }$ or $\gamma _ { i }$ （Kahan &Li1997).

MethodsofOrder4.Theorem3.1and ExampleI1.3.15give3conditions for order4.Therefore,we put $s = 3$ in (3.1) and assume symmetry $\beta _ { 1 } = \alpha _ { 3 }$ , $\beta _ { 2 } = \alpha _ { 2 }$ , and $\beta _ { 3 } = \alpha _ { 1 } .$ This leads to the conditions

$$
\alpha _ { 1 } \mp \alpha _ { 2 } \mp \alpha _ { 3 } = \frac { 1 } { 2 } , \qquad \alpha _ { 1 } ^ { 3 } + \alpha _ { 2 } ^ { 3 } + \alpha _ { 3 } ^ { 3 } = 0 , \qquad ( \alpha _ { 3 } ^ { 2 } - \bar { \alpha } _ { 1 } ^ { 2 } ) ( \alpha _ { 1 } + \alpha _ { 2 } ) = 0 .
$$

Sincewith $\alpha _ { 1 } + \alpha _ { 2 } = 0$ orwith $\alpha _ { 1 } + \alpha _ { 3 } = 0$ the first two of these equations are not compatible,the unique solution of this systemis

$$
\alpha _ { 1 } = \alpha _ { 3 } = \frac { 1 } { 2 \left( 2 - 2 ^ { 1 / 3 } \right) } , \quad \alpha _ { 2 } = - \frac { 2 ^ { 1 / 3 } } { 2 \left( 2 - 2 ^ { 1 / 3 } \right) } .
$$

We observe that $\beta _ { i } = \alpha _ { i }$ for all $i .$ Therefore, $\phi _ { \alpha _ { i } h } \circ \phi _ { \beta _ { i } h } ^ { * }$ can be grouped together in (3.1)and we have obtained a method of type(3.2),which isactually method(II.4.4) with $p = 2$ .

Again,the solutionswith the minimal number of stages do not give the best methods (remember the good performance of Suzuki's fourth order method (II.4.5) inFig.II.4.4),sowe look for 4thordermethodswith largers.McLachlan(1995) hasconstructed a method for $s = 5$ with particularly small error terms and nice coefficients

$$
\begin{array} { l l } { { \beta _ { 1 } = \alpha _ { 5 } = \displaystyle \frac { 1 4 - \sqrt { 1 9 } } { 1 0 8 } , } } & { { \alpha _ { 1 } = \beta _ { 5 } = \displaystyle \frac { 1 4 6 + 5 \sqrt { 1 9 } } { 5 4 0 } , } } \\ { { \beta _ { 2 } = \alpha _ { 4 } = \displaystyle \frac { - 2 3 - 2 0 \sqrt { 1 9 } } { 2 7 0 } , } } & { { \alpha _ { 2 } = \beta _ { 4 } = \displaystyle \frac { - 2 + 1 0 \sqrt { 1 9 } } { 1 3 5 } , \quad \beta _ { 3 } = \alpha _ { 3 } = \displaystyle \frac { 1 } { 5 } , } } \end{array}
$$

which he recommends“for all uses".

InFig.3.2 we compare the numerical performances of allthese methods on our already well-known example in both variants (implicit-explicit and vice-versa).We see that the best methods in one picture may be worsein the other.For comparison, theresults are surrounded by“ghosts in grey"representing good formulae from the next lower (order2)and the next higher (order6)class of methods.

Methods Tuned for Special Problems.In the casewhere one isapplyingaspecial method toaspecial problem(e.g.,to second orderdifferential equations or tosmall perturbations of integrable systems),more spectacular gains of efficiency are possible.For example,Blanes&Moan(2oo2） have constructed thefollowing fourth ordermethodwith $s = 6$

![](images/ec5fded7394de723dfea57651797cb60f28d32b58a1d4ddba70f7283c70b3f3b.jpg)  
Fig.3.2.Work-precisiondiagrams formethodsoforder4asinFig.3.1;3j:theTripleJump (II.4.4)；“su":method(I.4.5）of Suzuki；“ml":McLachlan(3.6)；“bm:method(3.7)；in grey:neighbouring order methods Stormer/Verlet (order2)and $p 6 \ : s 9$ (order 6)

which,when correctly applied to second order differential equations (right picture ofFig.3.2) exhibits excellent performance.

Further methods,adapted to the integration of second order differential equations,have been constructedbyForest（1992),McLachlan&Atela(1992),Calvo &Sanz-Serna(1993),Okunbor& Skeel(1994),andMcLachlan(1995).Another important situation,which allowsa tuning of the parameters,are near-integrable systems such as the perturbed two-body motion (e.g.,the outer solar system consideredinChap.I).If the differential equation can be split into $\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y )$ , where $\dot { y } = f ^ { [ 1 ] } ( y )$ is exactly integrableand $f ^ { [ 2 ] } ( y )$ issmall compared to $f ^ { [ 1 ] } ( y )$ , specialintegrators should be used.Werefer to Kinoshita,Yoshida&Nakai(1991), Wisdom&Holman(1991),Saha&Tremaine（1992),andMcLachlan（1995b)for moredetailsand for the parameters of such integrators.

MethodsofOrder6.ByTheorem3.1andExampleIII.3.12amethod(3.1) hasto satisfy9conditions for order 6.It turns out that these order conditions have already a solution with $s = 7$ ,but all known solutions with $s \leq 8$ are equivalent tomethods of type (3.2).With order6we are apparently close to the point where the enormous simplifications of the order conditionsdue to Theorem 3.3 below startto outperform the freedom of choosing different values for $\alpha _ { i }$ and $\beta _ { i }$ We therefore continue our discussion by considering only the special case (3.2).

# V.3.2Symmetric Composition of SymmetricMethods

Theintroduction of more symmetries into the method simplifies considerably the orderconditions.These simplificationscan be bestunderstood with a sortof"Choleski decomposition"of symmetric methods(Murua& Sanz-Serna 1999).

Lemma3.2.For everysymmetricmethod $\varPhi _ { h } ( y )$ thatadmits anexpansion inpowersof $h$ ,thereexists $\widehat { \varPhi } _ { h } ( y )$ suchthat

$$
\begin{array} { r } { \varPhi _ { h } ( y ) = \bigl ( \widehat { \varPhi } _ { h / 2 } \circ \widehat { \varPhi } _ { h / 2 } ^ { * } \bigr ) ( y ) . } \end{array}
$$

Proof.Since $\begin{array} { r } { \Phi _ { h } ( y ) = y + \mathcal { O } ( h ) } \end{array}$ is close to the identity,the existence of a unique method $\bar { \phi } _ { h } ( y ) = y + h d _ { 1 } ( y ) + h ^ { 2 } d _ { 2 } ( y ) + . . .$ satisfying $\bar { \varPhi } _ { h } = \widehat { \varPhi } _ { h / 2 } \circ \widehat { \varPhi } _ { h / 2 }$ follows from Taylor expansion and from acomparison of like powers of $h$

If $\varPhi _ { h } ( y )$ is symmetric,we have inaddition

$$
\varPhi _ { h } = \varPhi _ { - h } ^ { - 1 } = \widehat { \varPhi } _ { - h / 2 } ^ { - 1 } \circ \widehat { \varPhi } _ { - h / 2 } ^ { - 1 } ,
$$

$\widehat { \varPhi } _ { h / 2 } = \widehat { \varPhi } _ { - h / 2 } ^ { - 1 } = \widehat { \varPhi } _ { h / 2 } ^ { * }$ $\widehat { \varPhi } _ { h }$

Welet $\phi _ { h }$ beasymmetric method,and we consider the composition

$$
\varPsi _ { h } = \varPhi _ { \gamma _ { s } h } \circ \dots \circ \varPhi _ { \gamma _ { 2 } h } \circ \varPhi _ { \gamma _ { 1 } h } .
$$

Using the method $\widehat { \Phi } _ { h }$ ofLemma 3.2,this composition method is equivalentto (3.1) （ $\phi _ { h }$ replacedwith $\widehat { \varPhi } _ { h }$ )with

$$
\alpha _ { i } = \beta _ { i } = \frac { \gamma _ { i } } { 2 } .
$$

Theorem3.3.Forcompositionmethods(3.8) with symmetric $\phi _ { h }$ it is sufficient to considertheorderconditionsofTheoremII.3.14for $\tau \in \mathcal { H }$ whereall verticesof $\tau$ have odd indices.

Proof.If $i ( \tau )$ is even,itfollows from $\alpha _ { k } = \beta _ { k }$ and from(III.3.11) that

$$
a _ { s } ( \tau ) = a _ { s - 1 } ( \tau ) = \ldots = a _ { 1 } ( \tau ) = a _ { 0 } ( \tau ) = 0 .
$$

Since $\mathbf { e } ( \tau ) = 0$ forsuch trees,the corresponding order condition is automatically satisfied.Any other vertexwithaneven indexcan bebrought to therootbyapplying theSwitching Lemma III.3.8. □

Afterthis reduction,only7conditions survive for order6 from the trees displayed in Example III.3.12.A further reduction in the numberof orderconditions is achieved byassumingsymmetriccoefcients in method(3.8),i.e.,

$$
\gamma _ { s + 1 - j } = \gamma _ { j } \qquad { \mathrm { f o r ~ a l l } } ~ j .
$$

Thisimplies that the overall method $\psi _ { h }$ is symmetric,so that the order conditions for treeswith an even $| | \tau | |$ need not be considered.This proves the followingresult.

![](images/34374408ee0293f43b45aed8550817656b1074054f92c69fff1112bfdac01dda.jpg)  
Fig.3.3.Symmetric Composition of SymmetricMethodsupto order 10

Theorem3.4.Forcompositionmethods(3.8)with symmetric $\varPhi _ { h }$ satisfying(3.10), itissuffcientto considerthe order conditions for $\tau \in \mathcal { H }$ where all vertices of $\tau$ have odd indicesandwhere $\| \tau \|$ isodd. □

Figure3.3 shows theremaining orderconditions formethodsup to order10.We seethat for order6 thereremain only4conditions,much less than the166 thatwe started with(Theorem II.3.6).

Example3.5.Therule of(II.3.14) leads tothefollowing conditionsforsymmetric composition of symmetric methods:   

<table><tr><td>8 Order2: ① M =1 k=1</td><td></td></tr><tr><td>Order4: ③</td><td>8 1 M 3 =0 k=1</td></tr><tr><td>Order6: ⑤</td><td>S S k 2 M 2 3 1 =0 Ye =0 C 3 k=1 k=1 =1</td></tr><tr><td>Order8: ?</td><td>8 8 k m 2 M =0 / 2 re =0 2 k=1 =1</td></tr><tr><td>s M 3 k=1</td><td>k M k k 4 3 Ye 0 Ye) =0. 2 &gt; =1 m=1 k=1 e=1</td></tr></table>

Here,similar to Example II.3.15,a prime attached toasummation symbol indicates that the last term $y _ { \ell } ^ { i }$ is takenas $\gamma _ { \ell } ^ { i } / 2$

Methods ofOrder4.Themethods(II.4.4)and(II.4.5)are both of the form(3.8), and those with $p = 2$ yieldmethodsof order4.We have seen in the experiment ofFig.II.4.4that the method(II.4.5）yieldsmore precise approximations;seealso Fig.3.2.Wedo notknow ofany 4thordermethod of type(3.2) that is significantly better than method (3.1） with coefficients (3.6).

Methods of Order 6.Ifwe search fora minimal stage solution of the four equations for order 6,we apparently need four free parameters $\gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 } , \gamma _ { 4 }$ ;then $\gamma _ { 5 }$ , $\gamma _ { 6 }$ , $\gamma _ { 7 }$ aredeterminedby symmetry.Equation $\textcircled{1}$ gives $\gamma _ { 4 } = 1 - 2 ( \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } )$ So we end up with three equations for the three unknowns $\gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 }$ Anumerical search for this problem produces three solutions,the best of which has been discoveredbymanyauthors,inparticularbyYoshida(199O),andisasfollows:

Y1=77= 0.78451361047755726381949763 p6s7Y2=γ6= 0.23557321335935813368479318Y3=Y5=-1.17767998417887100694641568Y4= 1.31518632068391121888424973

Usingcomputer algebra,Koseleff（1996）proves that the nonlinear system for $\gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 }$ hasnot more than three real solutions.

Similar to the situation for order 4,whererelaxing the minimal number of stages allowed a significant increase of performance,we also might expect to obtain better methodsof order6inthisway.McLachlan(1995)increases $s$ bytwo and constructs good methods with small error coeffcients.By minimizing $\operatorname* { m a x } _ { i } | \gamma _ { i } |$ ,Kahan&Li （1997)obtain the following excellent method3

![](images/adb22d4efdec2bf18092ee0d3c75f70511f7923db5be67929b4d349a40281ccc.jpg)  
This method produces,with a comparable number of total steps,errorswhich are typically smaller than those of method (3.11).Numerical results of these two methods are given in Fig.3.4.

![](images/ad4dd7be5eeafcda386b6cbae4c297cdc4d8044ef728b584baf7ee8b2a8f9446.jpg)  
Fig.3.4.Work-precisiondiagrams for methodsof order6 for the Keplerproblem asin Fig.3.1；“7":method $p 6 . s 7$ of（3.11）:“9":method $p 6 s 9$ of(3.12）；in grey:neighbouring ordermethods(3.6)(order 4)and $p 8 s 1 7$ (order8)

Methods of Order8.For order8,Fig.3.3 represents 8equations to solve.This indicates that the minimal value of $s$ is15.Anumerical search for solutions $\gamma _ { 1 } , \ldots , \gamma _ { 8 }$ ofthese equations produces hundreds of solutions.We choose among all these the solution with the smallest $\operatorname* { m a x } ( | \gamma _ { i } | )$ Thecoefficients,which were originally given bySuzuki&Umeno(1993),Suzuki(1994),andlaterbyMcLachlan(1995),areas follows:

=715= 0.74167036435061295344822780   
$\gamma _ { 2 } = \gamma _ { 1 4 } = - 0 . 4 0 9 1 0 0 8 2 5 8 0 0 0 3 1 5 9 3 4$ 99730010 p8s15   
Y3=Y13= 0.19075471029623837995387626   
$\gamma _ { 4 } = \gamma _ { 1 2 } = - 0 . 5 7 3 8 6 ^ { * } 2 4 7 1 1 1 6 0 8 ^ { * } 2 ^ { * } 2 6 6 6 5 6 ^ { * } 3 8 7 7 3$   
$\gamma _ { 5 } = \gamma _ { 1 1 } =$ 0.29906418130365592384446354   
$\gamma _ { 6 } = \gamma _ { 1 0 } =$ 0.33462491824529818378495798   
$\gamma _ { 7 } = \gamma _ { 9 }$ 三 0.31529309239676659663205666   
Y8=-0.79688793935291635401978884

Byputting $s = 1 7$ we obtain one degree of freedom in solving the equations.This allows an improvement on the foregoing method.The best known solution,slightly better thanamethodofMcLachlan(1995),hasbeen foundbyKahan&Li（1997) and is given by

![](images/3a550148ac84123043f83b5d551c3549a5e3bd8a90ac9ab24d8e620dbb0657d7.jpg)  
Numerical results,in the same style as above,are giveninFig.3.5.

![](images/8674596bc50f11dc4ebcf1ebd5b273e4b5bfd944f1e816d358ea637a71520e9b.jpg)  
Fig.3.5.Work-precision diagramsformethods oforder8 for the Keplerproblemasin Fig.3.1；“15":method $p 8$ s15of(3.13）；“17":method $p 8$ $s 1 7$ of（3.14）；in grey:neighbouring ordermethods $p 6 \ : s 9$ (order 6)and $p 1 0 s 3 5$ (order 10)

Methodsof Order10.Thefirst methods of order10 weregivenbyKahan&Li （1997）with $s = 3 1$ and $s = 3 3$ ,which could be improved on after some nights of computer search (seemethod(V.3.15)of the first edition).A significantly improved method for $s = 3 5$ (seeFig.3.5foracomparisonwith eighth ordermethods) has in the meantime been found by Sofroniou & Spaletta (2004):

$\gamma _ { 1 } = \gamma _ { 3 5 } =$ 0.07879572252168641926390768 $\gamma _ { 2 } = \gamma _ { 3 4 } =$ 0.31309610341510852776481247 Y3=733= 0.02791838323507806610952027 $\gamma _ { 4 } = \gamma _ { 3 2 } = - 0 . 2 2 9 5 9 2 8 4 1 5 9 3 9 0 / 0 9 4 1 5 1 2 1 3 4 0$ $\begin{array} { r l } { \gamma _ { 5 } = \gamma _ { 3 1 } = } & { { } \cup . 1 9 9 9 0 \angle { \mathsf { U } } 0 . 1 9 / ( \ 1 0 4 8 0 3 1 ( 4 0 5 0 8 0 } \end{array}$ 0.13096206107716486317465686 $\gamma _ { 6 } = \gamma _ { 3 0 } = - 0 . 2 6 9 / 3 3 4 0 5 6 5 4 5 1 0 / 1 4 3 4 4 6 0 9 7 3 \qquad \quad$ p10s35 $\gamma _ { 7 } = \gamma _ { 2 9 } =$ 0.07497334315589143566613711 $\gamma _ { 8 } = \gamma _ { 2 8 } =$ 0.11199342399981020488957508 $\begin{array} { r l } { \gamma _ { 9 } = \gamma _ { 2 7 } = } & { { } \cup . 3 6 6 1 3 3 4 4 9 5 4 6 \mathrm { 2 2 6 } / 5 1 . 1 9 3 1 4 8 } \end{array}$ 12 $\gamma _ { 1 0 } = \gamma _ { 2 6 } = - 0 . 3 9 9 1 0 5 0 3 0 1 3 6 0 3 5 8 9 ( 8 / 8 0 2 9 6$ 81 $\gamma _ { 1 1 } = \gamma _ { 2 5 } =$ 0.10308739852747107731580277 $\begin{array} { r l } { \gamma _ { 1 2 } = \gamma _ { 2 4 } = } & { { } \cup . 4 1 4 4 3 0 8 ( . 3 9 5 0 8 9 0 2 3 ( 8 2 0 / 0 4 1 2 } \end{array}$ $\gamma _ { 1 3 } = \gamma _ { 2 3 } = - 0 . 0 0 4 8 6 6 3 6 0 5 8 3 1 3 5 2 6 1 / 6 2 1 9 5 6 6$ $\gamma _ { 1 4 } = \gamma _ { 2 2 } = - 0 . 3 9 2 0 3 3 3 5 3 / 0 8 6 3 9 9 0 6 4 4 8 0 8 1 9 4$ $\gamma _ { 1 5 } = \gamma _ { 2 1 } =$ 0.05194250296244964703718290 $\gamma _ { 1 6 } = \gamma _ { 2 0 } =$ 0.05066509075992449633587434 $\gamma _ { 1 7 } = \gamma _ { 1 9 } =$ 0.04967437063972987905456880 $\gamma _ { 1 8 } =$ 0.04931773575959453791768001

# V.3.3Effective Order and Processing Methods

There has recently been arevival of interest in the concept of"effective order". （J.C.Butcher 1998)

The concept of effective orderwas introduced by Butcher(1969）with the aim of constructing 5th order explicit Runge-Kutta methods with5 stages.The idea is to search foracomputationally efficientmethod $K _ { h }$ such that with a suitable $\chi _ { h }$ ,

$$
\varPsi _ { h } = \chi _ { h } \circ K _ { h } \circ \chi _ { h } ^ { - 1 }
$$

has an order higher than that of $K _ { h }$ Themethod $K _ { h }$ is called the kernel,and $\chi _ { h }$ can beinterpreted asatransformation in the phase space,close to the identity.Because of

$$
\varPsi _ { h } ^ { N } = \chi _ { h } \circ K _ { h } ^ { N } \circ \chi _ { h } ^ { - 1 } ,
$$

an implementation of $\psi _ { h }$ over $N$ steps with constant step size $h$ has the same computational efficiency as $K _ { h } .$ The computation of $\chi _ { h } ^ { - 1 }$ has only to bedone once at the beginning of the integration,and $\chi _ { h }$ has to be evaluated only at output points,which can be performed on another processor.In the article Lopez-Marcos,Sanz-Serna& Skeel(1996)the notion of preprocessing for the step $\chi _ { h } ^ { - 1 }$ and postprocessing for $\chi _ { h }$ isintroduced.

Example3.6 (Stormer-Verlet as Processed Symplectic EulerMethod).Considerasplit differential equation,let $\varPhi _ { h } ^ { \left[ L T \right] } = \varphi _ { h } ^ { \left[ 2 \right] } \circ \varphi _ { h } ^ { \left[ 1 \right] }$ be the Lie-Trotter formula or symplectic Euler method (see Sect..5)and $\phi _ { h } ^ { [ S ] } = \varphi _ { h / 2 } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h / 2 } ^ { [ 1 ] }$ theStrang splitting or Stormer-Verlet scheme.Asa consequence of the group property of the exact flow,we have

$$
\bar { \phi } _ { h } ^ { [ S ] } = \varphi _ { h / 2 } ^ { [ 1 ] } \circ \varPhi _ { h } ^ { [ L T ] } \circ \varphi _ { - h / 2 } ^ { [ 1 ] } = \chi _ { h } \circ \varPhi _ { h } ^ { [ L T ] } \circ \chi _ { h } ^ { - 1 }
$$

with Xh=h/2 Hence,applying theLie-Trotter formula with processing yieldsa second order approximation.

Since the use of geometric integrators requires constant step sizes,it is quite natural that Butcher's idea of effective order has beenrevived in this context.A systematic search forprocessed composition methods started with the works of Wisdom,Holman&Touma（1996),McLachlan（1996),andBlanes,Casas&Ros（1999, 2000b).

Letus explain the technique of processing in the situation where the kernel $K _ { h }$ isasymmetriccomposition

$$
K _ { h } = \varPhi _ { \gamma _ { s } h } \circ \dots \circ \varPhi _ { \gamma _ { 2 } h } \circ \varPhi _ { \gamma _ { 1 } h } \qquad ( \gamma _ { s + 1 - \ i } = \gamma _ { i } \mathrm { ~ f o r ~ a l l ~ } i )
$$

ofasymmetric method $\phi _ { h }$ .We suppose that the processor is of the form

$$
\chi _ { h } = \varPhi _ { \delta _ { r } h } \circ \dots \circ \varPhi _ { \delta _ { 2 } h } \circ \varPhi _ { \delta _ { 1 } h } ,
$$

suchthatits inverseisgivenby(usethesymetry $\varPhi _ { h } ^ { - 1 } = \varPhi _ { - h }$

$$
\chi _ { h } ^ { - 1 } = \varPhi _ { - \delta _ { 1 } h } \circ \varPhi _ { - \delta _ { 2 } h } \circ \dots \circ \varPhi _ { - \delta _ { r } h } .
$$

Order Conditions.Thecomposite method $\varPsi _ { h } = \chi _ { h } \circ K _ { h } \circ \chi _ { h } ^ { - 1 }$ is of the form $\psi _ { h } = \phi _ { \varepsilon _ { 2 r + s } h } \circ \dots \circ \phi _ { \varepsilon _ { 2 h } \circ \phi _ { \varepsilon _ { 1 } h } }$ with

$$
( \varepsilon _ { 2 r + s } , . . . , \varepsilon _ { 2 } , \varepsilon _ { 1 } ) = ( \delta _ { r , r } . . . , \delta _ { 1 s } \gamma _ { s } , . . . , \gamma _ { 1 } , - \delta _ { 1 } , . . . , - \delta _ { r } ) .
$$

Theorem 3.3 thus tels us that only the order conditions corresponding to $\tau \in \mathcal { H }$ whose vertices have odd indices,have to be considered.Unfortunately,the sequence $\{ \varepsilon _ { i } \}$ of(3.20)does not satisfy the symmetry relation (3.1O),unless all $\delta _ { i }$ vanish. However,ifwe require

$$
\chi _ { - h } ( y ) = \chi _ { h } ( y ) + \mathcal { O } ( h ^ { p + 1 } ) ,
$$

we see that $\chi _ { h } ^ { - 1 } ( y ) = \chi _ { h } ^ { * } ( y ) + \mathcal { O } ( h ^ { p + 1 } ) ,$ and the method $\varPsi _ { h } = \chi _ { h } \circ K _ { h } \circ \chi _ { h } ^ { - 1 }$ is symmetric up to terms of order $O ( h ^ { p + 1 } )$ Consequently,the reduction of Theorem3.4 isvalid,sothat fororder $p$ only the trees of Fig.3.3 have to be considered.

Forthe first tree of Example 3.5 the order condition is

$$
1 = \sum _ { k = 1 } ^ { 2 r + s } \varepsilon _ { k } = \sum _ { k = 1 } ^ { s } \gamma _ { k } ,
$$

and we see that this isacondition on the kernel $K _ { h }$ only.Similarly,forodd $\textit { i }$ we have

$$
0 = \sum _ { k = 1 } ^ { 2 r + s } \varepsilon _ { k } ^ { i } = \sum _ { k = 1 } ^ { s } \gamma _ { k } ^ { i } ,
$$

so that also the trees $\textcircled{3}$ , $\textcircled{5}$ , $\textcircled{7} , \cdots$ give conditions on $K _ { h }$ and cannot be influenced bytheprocessor.We next consider the trees of Example 3.5with three vertices, whose order condition is

$$
0 = \sum _ { k = 1 } ^ { 2 r + s } \varepsilon _ { k } ^ { i } \sum _ { \ell = 1 } ^ { k } \varepsilon _ { \ell } ^ { j } \sum _ { m = 1 } ^ { k } \varepsilon _ { m } ^ { q } .
$$

Wesplit the sums according to the partitioning into $\delta _ { i } , \gamma _ { i } , - \delta _ { i }$ in (3.20），andwe denote the expressionsappearingin Example 3.5by $a ( \tau )$ and those corresponding to $\chi _ { h }$ and $\chi _ { h } ^ { - 1 }$ by $b ( \tau )$ and $b ^ { - 1 } ( \tau )$ ,respectively.Using the abbreviations $\tau _ { i }$ forthe treewith one vertex labelled $\textit { i }$ , $\tau _ { \lambda j }$ forthe tree with two vertices labelled $\boldsymbol { i }$ (theroot） and $j$ ,andby $\tau _ { i j q }$ the trees with three vertices labelled $\textit { i }$ (root), $\mathcal { I }$ and $q$ (verticesthat aredirectly connected to the root),this yields

$$
\begin{array} { l } { { 0 ~ = ~ b ^ { - 1 } ( \tau _ { i j q } ) + a ( \tau _ { i } ) b ^ { - 1 } ( \tau _ { j } ) b ^ { - 1 } ( \tau _ { q } ) + a ( \tau _ { i j } ) b ^ { - 1 } ( \tau _ { q } ) } } \\ { { \ ~ + ~ a ( \tau _ { i q } ) b ^ { - 1 } ( \tau _ { j } ) + a ( \tau _ { i j q } ) + b ( \tau _ { i } ) b ^ { - 1 } ( \tau _ { j } ) b ^ { - 1 } ( \tau _ { q } ) } } \\ { { \ ~ + ~ b ( \tau _ { i } ) b ^ { - 1 } ( \tau _ { j } ) a ( \tau _ { q } ) + b ( \tau _ { i } ) a ( \tau _ { j } ) b ^ { - 1 } ( \tau _ { q } ) + b ( \tau _ { i } ) a ( \tau _ { j } ) a ( \tau _ { q } ) } } \\ { { \ ~ + ~ b ( \tau _ { i j } ) b ^ { - 1 } ( \tau _ { q } ) + b ( \tau _ { i j } ) a ( \tau _ { q } ) + b ( \tau _ { i q } ) b ^ { - 1 } ( \tau _ { j } ) + b ( \tau _ { i q } ) a ( \tau _ { j } ) + b ( \tau _ { i j q } ) . } } \end{array} \nonumber
$$

Howcan we simplify this longexpression?First of all,we imagine $K _ { h }$ to be the identity (either $s = 0$ orall $\gamma _ { i } = 0$ ,sothat $\bar { \psi } _ { h } = \chi _ { h } \circ \chi _ { h } ^ { - 1 }$ becomes the identity.In this situation,the terms involving $a ( \tau )$ are not present in (3.23),and we obtain

$$
0 = b ^ { - 1 } ( \tau _ { i j q } ) + b ( \tau _ { i } ) b ^ { - 1 } ( \tau _ { j } ) b ^ { - 1 } ( \tau _ { q } ) + b ( \tau _ { i j } ) b ^ { - 1 } ( \tau _ { q } ) + b ( \tau _ { i q } ) b ^ { - 1 } ( \tau _ { j } ) + b ( \tau _ { i j } ) b ^ { - 1 } ( \tau _ { j } ) + b ( \tau _ { i j } ) b ^ { - 1 } ( \tau _ { i } )
$$

Wecan thusremoveall termsin (3.23） that do not containa factor $a ( \tau )$ Nowobserve that by(3.21）, $\chi _ { h } ( y )$ aswell as $\chi _ { h } ^ { - 1 } ( y )$ havean expansion in even powers of $h$ .Therefore, $b ( \tau )$ and $b ^ { - 1 } ( \tau )$ vanish forall $\tau$ with odd $| | \tau | |$ Formula(3.23) thus simplifiesconsiderablyandyields

$$
\begin{array} { l } { { 0 = a ( \tau _ { 3 1 1 } ) + 2 b ( \tau _ { 3 1 } ) a ( \tau _ { 1 } ) , } } \\ { { } } \\ { { 0 = a ( \tau _ { 5 1 1 } ) + 2 b ( \tau _ { 5 1 } ) a ( \tau _ { 1 } ) , } } \\ { { 0 = a ( \tau _ { 3 1 3 } ) + b ( \tau _ { 3 1 } ) a ( \tau _ { 3 } ) + b ( \tau _ { 3 3 } ) a ( \tau _ { 1 } ) . } } \end{array}
$$

A similar computation for the last tree in Example3.5 gives (in an obvious notation)

$$
0 = a ( \tau _ { 3 1 1 1 1 } ) + 4 b ( \tau _ { 3 1 } ) a ( \tau _ { 1 } ) ^ { 3 } + 4 b ( \tau _ { 3 1 1 1 } ) a ( \tau _ { 1 } ) .
$$

Since $\begin{array} { r } { a ( \tau _ { 1 } ) = \sum _ { i = 1 } ^ { s } \gamma _ { i } = 1 , } \end{array}$ theodi)d preted as conditions on the processor,namely on $b ( \tau _ { 3 1 } )$ $b ( \tau _ { 5 1 } )$ and $b ( \tau _ { 3 1 1 1 } )$ We alreadyhave $a ( \tau _ { 3 } ) = 0$ from(3.22),and an application of the SwitchingLemma III.3.8gives $b ( \tau _ { 3 3 } ) = \textstyle { \frac { 1 } { 2 } } \left( b ( \tau _ { 3 } ) ^ { 2 } - b ( \tau _ { 6 } ) \right) .$ Theterm $b ( \tau _ { 3 } )$ vanishes by(3.21） and $b ( \tau _ { 6 } ) = 0$ isaconsequence of theproof of Theorem 3.3.Therefore(3.26) isequivalentto $a ( \tau _ { 3 1 3 } ) = 0$ We summarize our computation in the following theorem.

Theorem3.7.Theprocessing method $\varPsi _ { h } = \chi _ { h } \circ K _ { h } \circ \chi _ { h } ^ { - 1 }$ isoforderp $p \leq 8 ,$ ，if the coefficients $\gamma _ { i }$ ofthekernel satisfy theconditions oftheleftcolumninExample3.5,i.e.,3conditionsfororder6,and5conditionsfororder8; ·the coefficients $\delta _ { i }$ oftheprocessoraresuchthat(3.21） holds(4conditionsfor order6,and8conditionsfororder8),andinadditioncondition(3.24)fororder 6,and(3.24),(3.25),(3.27)fororder8are satisfied. □

Remark 3.8.Although we have presented the computations only for $p \leq 8$ ,the result is general.All trees $\tau \in \mathcal { H }$ ,which are not of the form $\tau = u \circ \textcircled { 1 }$ give rise to conditions on the kernel $\displaystyle { K _ { h } }$ (fora similar result in the context of Runge-Kuttamethods see Butcher& Sanz-Serna(1996)).The remaining conditions have tobe satisfied by the coefficients of the processor.Due to thereduced number of orderconditions,itis relatively easy to construct high order kernels.However,the difficulty in constructinga suitable processor increases rapidlywith the order.

Theapplication of the processing technique is two-fold.A first possibilityis to take one of the high-order composition methods of the form (3.2),e.g.,one of thosepresented in Sect.V.3.2,and to exploit the freedomin the coefficients of the processortomake the error constants smaller.

Anotherpossibilityis to start from thebeginningand to constructamethod $K _ { h }$ with coefficients satisfying only the conditions of Theorem 3.7.Methods of effective order6and 8 have been constructed in thiswaybyBlanes(2001).

# V.4Symmetric Methods on Manifolds

Numerical methodsfordifferential equations on manifolds have been introduced inSections IV.4and IV.5.The presented algorithmsare in general not symmetric. We discuss here suitable symmetric modifications which often have an improved long-time behaviour.We consideradifferential equation

$$
\dot { y } = f ( y ) , \qquad f ( y ) \in T _ { y } \mathcal { M }
$$

onamanifold $\mathcal { M }$ ,and we assume that the manifold is either givenas the zero set of afunction $g ( y )$ orbymeans of asuitable parametrization $y = \varphi ( z )$

# V.4.1 Symmetric Projection

Dueto the projection at the end of an integration step,the standard projection method(AlgorithmIV.4.2) isnot symmetric (see Fig.IV.4.2).In order to make the overall algorithm symmetric,one hasto applya kind of“inverseprojection”at the beginning ofeach integration step.This idea hasfirstbeenused by Ascher&Reich (1999)to enforce conservation ofenergy,and it has been applied inmore general contexts byHairer(2000).

Algorithm4.1 (Symmetric Projection Method).Assume that $y _ { n } \in M$ Onestep $y _ { n } \mapsto y _ { n + 1 }$ isdefinedasfollows(seeFig.4.1,rightpicture):

$\widetilde { y } _ { n } = y _ { n } + G ( y _ { n } ) ^ { T } \mu$ where $g ( y _ { n } ) = 0$ (perturbation step);   
$\widetilde { y } _ { n + 1 } = \Phi _ { h } ( \widetilde { y } _ { n } )$ (symmetric one-step method applied to $\dot { y } = f ( y )$ );   
$y _ { n + 1 } = \widetilde { y } _ { n + 1 } + G ( y _ { n + 1 } ) ^ { T } \mu$ with $\mu$ suchthat $g ( y _ { n + 1 } ) = 0$ (projection step).

Here, $G ( y ) ~ = ~ g ^ { \prime } ( y )$ denotes the Jacobian of $g ( y )$ Itis important to takea symmetric method in the second step,and the same vector $\mu$ in the perturbation and projection steps.

![](images/4858eaf331c333e4f589c8ee68c80baf2baf095bc67d15b435e483036cb970f7.jpg)  
Fig.4.1.Standard projection (left picture) compared tosymmetric projection (right)

Existence of the Numerical Solution. The vector $\mu$ and the numerical approximation $y _ { n + 1 }$ areimplicitlydefined by

$$
\begin{array} { r } { F ( h , y _ { n + 1 } , \mu ) = \left( { { y } _ { n + 1 } } - { { \varPhi } _ { h } } \big ( { { y } _ { n } } + G ( { { y } _ { n } } ) ^ { T } \mu \big ) - G ( { { y } _ { n + 1 } } ) ^ { T } \mu \right) = 0 . } \end{array}
$$

Since $F ( 0 , y _ { n } , 0 ) = 0$ and since

$$
\frac { \partial F } { \partial ( y _ { n + 1 } , \mu ) } \big ( 0 , y _ { n } , 0 \big ) = \left( \begin{array} { c c } { { I } } & { { - 2 G ( y _ { n } ) ^ { T } } } \\ { { G ( y _ { n } ) } } & { { 0 } } \end{array} \right)
$$

is invertible (provided that $G ( y _ { n } )$ has full rank),anapplication of the implicit function theorem proves the existence of the numerical solution for sufficiently small step size $h$ .The simple structure of the matrix(4.3）can also be exploited foran efficient solution of the nonlinear system(4.2） using simplified Newton iterations. If the basic method $\phi _ { h }$ isitself implicit,the nonlinearsystem(4.2)should be solved in tandem with $\widetilde { y } _ { n + 1 } = \Phi _ { h } ( \widetilde { y } _ { n } )$

Order.Forastudy of the local error we let $y _ { n } : = y ( t _ { n } )$ bea value on the exact solution $y ( t )$ of(4.1).If the basic method $\varPhi _ { h }$ is of order $p$ ,i.e.,if $y ( t _ { n } + h ) -$ $\varPhi _ { h } \bigl ( y ( t _ { n } ) \bigr ) = \ O ( h ^ { p + 1 } )$ wehave $F ( h , y ( t _ { n + 1 } ) , 0 ) = \mathcal { O } ( h ^ { p + 1 } ) .$ Compared to (4.2） theimplicit function theorem yields

$$
y _ { n + 1 } - y ( t _ { n + 1 } ) = \mathcal { O } ( h ^ { p + 1 } ) \qquad \mathrm { a n d } \qquad \mu = \mathcal { O } ( h ^ { p + 1 } ) .
$$

This proves that the symmetric projection method of Algorithm 4.1 has the same orderas the underlying one-step method $\phi _ { h }$

Symmetry of the Algorithm.Exchanging $h  - h$ and $y _ { n }  y _ { n + 1 }$ in the Algorithm4.1yields

$$
\begin{array} { r l } & { \widetilde { y } _ { n } = y _ { n + 1 } + G ( y _ { n + 1 } ) ^ { T } \mu , \qquad g ( y _ { n + 1 } ) = 0 , } \\ & { \widetilde { y } _ { n + 1 } = \varPhi _ { - h } ( \widetilde { y } _ { n } ) , } \\ & { y _ { n } = \widetilde { y } _ { n + 1 } + G ( y _ { n } ) ^ { T } \mu , \qquad g ( y _ { n } ) = 0 . } \end{array}
$$

Theauxiliary variables $\mu$ , $y _ { n }$ ,and $y _ { n + 1 }$ canbearbitrarily renamed.Ifwe replace themwith $- \mu$ , $y _ { n + 1 }$ ,and $y _ { n }$ ,respectively,we get the formulas of the original algorithm provided that the method $\phi _ { h }$ ofthe intermediate step is symmetric.This proves the symmetry of thealgorithm.

Various modifications of the perturbation and projection steps are possible without destroyingthe symmetry.For example,one can replace the arguments $y _ { n }$ and $y _ { n + 1 }$ in $G ( y )$ with $( y _ { n } + y _ { n + 1 } ) / 2$ Itmight be advantageous to use aconstant direction,i.e., $\widetilde { y } _ { n } = y _ { n } + A ^ { L } \mu , \ y _ { n + 1 } = \widetilde { y } _ { n + 1 } + A ^ { L } \mu$ with aconstant matrix $A$ Inthis case thematrix $G ( y ) A ^ { T }$ has to be invertible along the solution in order to guarantee theexistence of the numerical solution.

Reversibility. From Theorem1.5weknow thatsymmetry alonedoes not imply the $\rho$ -reversibilityof the numericalflow.Themethod mustalso satisfythecompatibilitycondition(1.4).It is straightforward to check that this condition is satisfied if the integrator $\phi _ { h }$ of theintermediate step of Algorithm4.1 satisfies (1.4)and,in addition,

$$
\rho G ( y ) ^ { T } = G ( \rho y ) ^ { T } \sigma
$$

holdswith some constant invertible matrix $O$ Inmany interesting situations we have $g ( \rho y ) = \sigma ^ { - T } g ( y )$ with a suitable $\sigma$ ,sothat（4.4） followsbydifferentiation if $\rho \rho ^ { T } = I .$ Similarly,when aprojection with constant direction $y = \widetilde { y } + A ^ { T } \mu$ is applied,the matrix $A$ has to satisfy $\rho A ^ { T } = A ^ { T } \sigma$ fora suitably chosen invertible matrix $o$ (seethe experiment of Example4.4below).

Example 4.2. Let us consider the equations of motion ofa rigid body as described inExample IV.1.7.They constitutea differential equation on the manifold

$$
\mathcal { M } = \{ ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) | y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1 \} ,
$$

and it is $\rho$ -reversiblewith respectto $\rho ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) = ( - y _ { 1 } , y _ { 2 } , y _ { 3 } )$ ,andalsowith respect to $\rho ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) = ( y _ { 1 } , - y _ { 2 } , y _ { 3 } )$ and $\rho ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) = ( y _ { 1 } , y _ { 2 } , - y _ { 3 } )$ Fora numerical simulation we take $I _ { 1 } = 2$ , $I _ { 2 } ~ = ~ 1$ ， $I _ { 3 } = 2 / 3$ ,andtheinitial value $y _ { 0 } = ( \cos ( 0 . 9 ) , 0 , \sin ( 0 . 9 ) )$ Weapply the trapezoidal rule(II.1.2）with the large stepsize $h = 1$ in three different versions.

The upper picture ofFig.4.2 shows the result ofadirectapplication of the trapezoidal rule.The numerical solution lies apparentlyonaclosed curve,but it does not lie exactly on themanifold $\mathcal { M }$ .This can be seen as follows: the trapezoidal rule $\varPhi _ { h } ^ { T }$ is conjugate to the implicit midpoint rule $\varPhi _ { h } ^ { M }$ viaa half-step of the explicit Euler methodXh/2.In facttherelations

![](images/841c526ba3fc8462082291a83c5a3ac0e85e7187fc190c187d7926cbc7a3aff3.jpg)  
Fig.4.2.Numerical simulation of the rigid body equations.The three picturescorrespond toadirect application(upper),to the standard projection (lower left),and to the symmetric projection (lower right) of the trapezoidal rule:5Ooo stepswith step size $h = 1$

$$
\begin{array} { r } { \varPhi _ { h } ^ { T } = \chi _ { h / 2 } ^ { * } \circ \chi _ { h / 2 } \qquad \mathrm { a n d } \qquad \varPhi _ { h } ^ { M } = \chi _ { h / 2 } \circ \chi _ { h / 2 } ^ { * } } \end{array}
$$

hold,so that

$$
\begin{array} { r l r l r } { \Phi _ { h } ^ { T } = \chi _ { h / 2 } ^ { - 1 } \circ \Phi _ { h } ^ { M } \circ \chi _ { h / 2 } } & { } & { \mathrm { a n d } } & { } & { ( \Phi _ { h } ^ { T } ) ^ { N } = \chi _ { h / 2 } ^ { - 1 } \circ ( \Phi _ { h } ^ { M } ) ^ { N } \circ \chi _ { h / 2 } . } \end{array}
$$

Consequently,the trajectory of the trapezoidal rule is obtained from the trajectory ofthe midpoint rulebya simple change of coordinates.On the other hand,the numerical solution of the midpoint rule lies exactly on a solution curve because it conserves quadratic invariants(Theorem IV.2.1).

Usingstandard orthogonal projection(AlgorithmIV.4.2）we obviously obtaina numerical solution lying on the manifold $\mathcal { M }$ Butaswe can see from thelowerleft picture ofFig.4.2,it doesnotremainnearaclosed curveand converges toa fixed point.The lower right picture shows that the use of the symmetric orthogonal projection(Algorithm 4.1） recovers the property of remainingnear the closed solution curve.

# Example 4.3 (Numerical Experiment with Constant Direction of Projection).

Weconsider the pendulum equation in Cartesian coordinates (see Example IV.4.1),

$$
\begin{array} { l l } { { \dot { q } _ { 1 } = p _ { 1 } , \quad } } & { { \dot { p } _ { 1 } = - q _ { 1 } \lambda , } } \\ { { \dot { q } _ { 2 } = p _ { 2 } , \quad } } & { { \dot { p } _ { 2 } = - 1 - q _ { 2 } \lambda } } \end{array}
$$

with $\lambda = ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } - q _ { 2 } ) / ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) .$ This isaproblem on the manifold

$$
\mathcal { M } = \big \{ ( q _ { 1 } , q _ { 2 } , p _ { 1 } , p _ { 2 } ) \mid q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } = 1 , q _ { 1 } p _ { 1 } + q _ { 2 } p _ { 2 } = 0 \big \} .
$$

Itis $\rho$ -reversiblewith respect to $\rho ( q _ { 1 } , q _ { 2 } , p _ { 1 } , p _ { 2 } ) = ( q _ { 1 } , q _ { 2 } , - p _ { 1 } , - p _ { 2 } )$ and also with respect to $\rho ( q _ { 1 } , q _ { 2 } , p _ { 1 } , p _ { 2 } ) = ( - q _ { 1 } , q _ { 2 } , p _ { 1 } , - p _ { 2 } )$

Weapply two kinds of symmetric projection methods.First,we consider an orthogonal projection onto $\mathcal { M }$ as in Algorithm4.1.Second,we project parallel to coordinate axes.More precisely,we fix thefirst components in position and velocity if the angleof thependulum isclose toOor $\pi$ (vertical projection in the picture to the right),and we fix the second components if the angle is close to $\pm \pi / 2$ (horizontal projection). The regions where the direction of projection changes,are overlapping.

![](images/9974f77439a63c5674d15b1a9d0ba5b826af18cf526b8abc3f3caf41814cfe53.jpg)

Wenotice in Fig.4.3 that for the orthogonal projection method theenergy errorremains bounded,and thisisalso true for integrations over much longer time intervals.Thisisinagreementwith the observation of Chap.I,wheresymmetric methods showed an excellent long-time behaviour when applied to reversible differential equations.

![](images/d12d45da280159afa3cc0aacdefa2daa1b31ef4960c451e1b3234260fe5a5343.jpg)  
Fig.4.3.Global errorin the total energy for two different projection methods-orthogonal andcoordinateprojection-with thetrapezoidal ruleasbasic integrator.Initial values for the position are $( \cos 0 . 8 , - \sin 0 . 8 )$ (leftpicture）and(cosO.8,sinO.8）（right picture）; zero initial values in the velocity;stepsizes are $h = 0 . 1$ (solid)and $h = 0 . 0 5$ (thindashed)

For the coordinate projection, however,we observea bounded energy error only forthe initial value that is close to equilibrium (no change in the direction of the projection is necessary).As soon as the direction has to be changed (right picture ofFig.4.3)a linear drift in the energy error becomesvisible.Hence,care has to be takenwith the choice of the projection.For an explanation of this phenomenon we refertoChap.IX on backward erroranalysis and toChap.XI on perturbation theory of reversible mappings.

![](images/c0267d0d570e5e98ba913744fa43263806c3cb99deeac93d120d0868862b525b.jpg)  
Fig.4.4.Global error in the total energyfor a symmetricprojectionmethod violating(1.4). Initial values for the position are （cos $0 . 8 , - \sin 0 . 8$ and $( 0 , 0 )$ for thevelocitystep sizes are $h = 0 . 1$ (solid）and $h = 0 . 0 5$ （thindashed）

Example4.4 (A Symmetric but Non-Reversible Projection Method).Weconsider thependulum equationas in Example4.3.This time,however,weapplya projection $\widetilde { y } _ { n } = y _ { n } + A ^ { T } \mu , \ y _ { n + 1 } = \widetilde { y } _ { n + 1 } + A ^ { T } \mu$ with

$$
A = { \left( \begin{array} { l l l l } { \varepsilon } & { 1 } & { 0 } & { 0 } \\ { \varepsilon } & { 0 } & { 0 } & { 1 } \end{array} \right) } , \qquad \varepsilon = 0 . 2 .
$$

For $\varepsilon = 0$ thiscorresponds to the vertical projection used in Example 4.3.For $\varepsilon \neq 0$ there is no matrix $O$ such that $\rho A ^ { T } \equiv A ^ { T } \sigma$ holds for one of the mappings $\rho$ thatmake theproblem $\rho$ -reversible.Hencecondition(1.4）isviolated,and the method is thus not $\rho$ -reversible.The initial valuesarechosen such that $g ^ { \prime } ( y ) A ^ { \prime }$ is invertible and well-conditioned along the solution.Although the projection direction need not bechanged during the integration and the method is symmetric,the long time behaviouris disappointingas shown in Fig.4.4.This experiment illustrates that condition(1.4)is also important fora qualitatively correct simulation.

# V.4.2Symmetric Methods Based on Local Coordinates

Numerical methods fordifferential equations on manifolds that are based on local coordinates(AlgorithmIV.5.3）arein general not symmetric.For example,ifwe consider the parametrization (IV.5.8) with respect to the tangent space at $y _ { 0 }$ ,theadjoint method would be parametrized by the tangent space at $y _ { 1 }$ Wecan circumvent this difficulty by the followingalgorithm (Hairer 2001).

Algorithm 4.5 (SymmetricLocal Coordinates Approach).Assume that $y _ { n } \in M$ andthat $\psi _ { a }$ isalocal parametrization of $\mathcal { M }$ satisfying $\psi _ { a } ( 0 ) = a$ (closeto $y _ { n }$ ). Onestep $y _ { n } \mapsto y _ { n + 1 }$ isdefined as follows(see Fig.4.5):

find $z _ { n }$ (close toO) such that $\psi _ { \alpha } ( z _ { n } ) = y _ { n } ,$ $\boldsymbol { z } _ { n + 1 } = \boldsymbol { \varPhi } _ { h } ( \boldsymbol { z } _ { n } )$ (symmetric one-step methodapplied to(IV.5.7);   
? $y _ { n + 1 } = \psi _ { a } ( z _ { n + 1 } )$ ;   
chooseaintheparametrization such that $z _ { n } + z _ { n + 1 } = 0$ .

Itisimportanttoremark thattheparametrization $y = \psi _ { a } ( z )$ is in general changed in every step.

![](images/3599031853e0315068535ea859a3aa20f82da78ed0c55e252fb05454e8bcf235.jpg)  
Fig.4.5.Symmetric use of local tangent space parametrization

Thisalgorithmis ilustrated inFig.4.5 for thetangent spaceparametrization (IV.5.8),given by

$$
\psi _ { a } ( z ) = a + Q ( a ) z + g ^ { \prime } ( a ) ^ { T } u _ { a } ( z ) ,
$$

where the columns of $Q ( a )$ form an orthogonal basis of $\mathbf { \Delta } T _ { a } \mathbf { \mathcal { M } }$ and the function $u _ { a } ( z )$ is such that $\psi _ { a } ( z ) \in { \mathcal { M } }$ It satisfies $u _ { a } ( 0 ) = 0$ and $u _ { a } ^ { \prime } ( 0 ) = 0$ .

Existenceof theNumerical Solution.InAlgorithm4.5thevalues $a \in \mathcal { M }$ and $z _ { n }$ are implicitly determined by

$$
F ( h , z _ { n } , a ) = { \binom { z _ { n } + \varPhi _ { h } ( z _ { n } ) } { \psi _ { a } ( z _ { n } ) - y _ { n } } } = 0 ,
$$

and the numerical solution is then explicitly given by $y _ { n + 1 } = \psi _ { a } \big ( \varPhi _ { h } ( z _ { n } ) \big ) .$ For moreclarity we also use here the notation $\psi ( z , a ) = \psi _ { a } ( z ) .$ If the parametrization $\psi ( z , a )$ isdifferentiable,we have

$$
\frac { \partial F } { \partial ( z _ { n } , a ) } ( 0 , 0 , y _ { n } ) = \left( \begin{array} { c c } { 2 I } & { 0 } \\ { \frac { \partial \psi } { \partial z } ( 0 , y _ { n } ) } & { \frac { \partial \psi } { \partial a } ( 0 , y _ { n } ) } \end{array} \right) .
$$

Since $\psi ( z , a ) \in \mathcal { M }$ forall $z$ and $a \in \mathcal { M }$ ,thederivative with respect to $a$ lies $\psi ( z , a )$ $\frac { \partial \psi } { \partial a } ( 0 , y _ { n } )$ $\mathcal { I } _ { y _ { n } } \mathcal { M }$ $\mathbb { R } ^ { d } \times T _ { y _ { n } } \mathcal { M }$ $d$   
implicit function theorem thus proves the existence of a numerical solution $( z _ { n } , a )$   
close to $( 0 , y _ { n } ) .$ In the case where $\psi _ { a } ( z )$ is given by(4.6),thematrix

$$
\frac { \partial \psi } { \partial a } ( 0 , a ) = I - g ^ { \prime } ( a ) ^ { T } \big ( g ^ { \prime } ( a ) g ^ { \prime } ( a ) ^ { T } \big ) ^ { - 1 } g ^ { \prime } ( a )
$$

isa projection onto the tangent space $\mathbf { \Delta } _ { T _ { a } , M }$ and satisfies the above assumptions provided that $g ^ { \prime } ( a )$ has full rank.

Order.We let $y _ { n } : = y ( t _ { n } )$ be a value on the exact solution $y ( t )$ of(4.1).Then we fix $a \in \mathcal { M }$ as follows:we replace theupper part ofthedefinition(4.7)of with $z _ { n } + \varphi _ { h } ^ { ( z ) } ( z _ { n } )$ where $\varphi _ { t } ^ { ( z ) }$ denoteso for $z ( t )$ equivalent to(4.1).The above considerations show that such an $a$ exists; let us call it $a ^ { * }$ .If $\phi _ { h }$ isof order $p$ ,we then have $F \bigl ( h , z ( t _ { n } ) , a ^ { * } \bigr ) \ = \ \mathcal { O } ( h ^ { p + 1 } )$ . Anapplication of the implicit function theorem thus gives $z _ { n } - z ( t _ { n } ) = \mathcal { O } ( h ^ { p + 1 } )$ ， implying $\widetilde { z } _ { n + 1 } - z ( t _ { n + 1 } ) = \mathcal { O } ( h ^ { p + 1 } )$ ,and finallyalso $y _ { n + 1 } - y ( t _ { n + 1 } ) = \mathcal { O } ( h ^ { p + 1 } )$ . This proves order $p$ forthemethod definedby Algorithm4.5.

Symmetry. Exchanging $h  - h$ and $y _ { n }  y _ { n + 1 }$ inAlgorithm4.5yields

$$
\psi _ { a } ( z _ { n } ) = y _ { n + 1 } , \quad \widetilde { z } _ { n + 1 } = \varPhi _ { - h } ( z _ { n } ) , \quad y _ { n } = \psi _ { a } ( \widetilde { z } _ { n + 1 } ) , \quad z _ { n } + \widetilde { z } _ { n + 1 } = 0 .
$$

If we also exchange the auxiliary variables $z _ { n }$ and $z _ { n + 1 }$ and if we use the symmetry of the basic method $\phi _ { h }$ ,weregain the original formulas.This proves the symmetry ofthealgorithm.Again variouskinds ofmodifications are possible.For example, the condition $z _ { n } + z _ { n + 1 } = 0$ can be replaced with $z _ { n } + \widetilde { z } _ { n + 1 } = \chi ( h , z _ { n } , \widetilde { z } _ { n + 1 } ) .$ If $\chi ( - h , v , u ) = \chi ( h , u , v )$ ,thesymmetry ofAlgorithm4.5isnot destroyed.

Reversibility.Ingeneral,wecannot expect themethodofAlgorithm4.5tosatisfy the $\rho$ -compatibilitycondition(1.4),whichisneeded for $\rho$ -reversibility.However,if the parametrization is suchthat

$$
\rho \psi _ { a } ( z ) = \psi _ { \rho a } ( \sigma z ) \qquad \mathrm { f o r ~ s o m e ~ i n v e r t i b l e } \quad \sigma ,
$$

we shall show that the compatibilitycondition(1.4） holds.We first prove that fora $\rho$ -reversibleproblem $\dot { y } = f ( y )$ thedifferential equation (IV.5.7),writenas $\dot { z } = F _ { a } ( z )$ ,is $O$ -reversible in the sense that $\sigma F _ { a } ( z ) = - F _ { \rho a } ( \sigma z )$ This follows from $\rho \psi _ { a } ^ { \prime } ( z ) ~ = ~ \psi _ { \rho a } ^ { \prime } ( \sigma z ) \sigma$ (which is seenby diferentiation of (4.9)）and from $f ( \psi _ { \rho a } ( \sigma z ) ) = - \rho f { \bigl ( } \psi _ { a } ( z ) { \bigr ) }$ because

$$
\psi _ { a } ^ { \prime } ( z ) F _ { a } ( z ) = f { \big ( } \psi _ { a } ( z ) { \big ) } \quad \Longrightarrow \quad \psi _ { \rho a } ^ { \prime } ( \sigma z ) \sigma F _ { a } ( z ) = - f { \big ( } \psi _ { \rho a } ( \sigma z ) { \big ) } ,
$$

If the basic method $\phi _ { h }$ satisfies $\sigma \circ \varPhi _ { h } = \varPhi _ { - h } \circ \sigma$ when applied to $\dot { z } = F _ { a } ( z )$ (e.g., forallRunge-Kutt methods),the formulasofAlgorithm4.5satisfy

$$
\begin{array} { r l } & { \rho y _ { n } = \rho \psi _ { a } ( z _ { n } ) = \psi _ { \rho a } ( \sigma z _ { n } ) , \qquad \sigma \widetilde { z } _ { n + 1 } = \Phi _ { - h } ( \sigma z _ { n } ) , } \\ & { \psi _ { \rho a } ( \sigma \widetilde { z } _ { n + 1 } ) = \rho \psi _ { a } ( \widetilde { z } _ { n + 1 } ) = \rho y _ { n + 1 } , \qquad \sigma z _ { n } + \sigma \widetilde { z } _ { n + 1 } = 0 . } \end{array}
$$

This proves that,starting with $\rho y _ { n }$ and a negative step size $- h$ ,theAlgorithm4.5 produces $\rho y _ { n + 1 }$ ,where $y _ { n + 1 }$ isjust the result obtained with initial value $y _ { n }$ and step size $h$ But this is nothing other than the $\rho$ -compatibilitycondition（1.4）for Algorithm4.5.

In order to verify condition (4.9) for the tangent space parametrization (4.6),we write it as $\psi _ { a } ( Z ) = a + Z + N ( Z )$ ,where $Z$ is an arbitrary element of the tangent space $\mathbf { \Delta } T _ { a } \mathbf { \mathcal { M } }$ and $N ( Z )$ isorthogonal to $T _ { a } { \mathcal { M } }$ such that $\psi _ { a } ( Z ) \in \mathcal { M }$ Since $\rho T _ { a } { \mathcal { M } } = T _ { \rho a } { \mathcal { M } }$ and since,for a $\rho$ satisfying $\rho \rho ^ { T } = I$ ,thevector $\rho N ( Z )$ isorthogonal to $\mathit { T _ { \rho a } } \mathcal { M }$ ,wehave $\rho \psi _ { a } ( Z ) = \psi _ { \rho a } ( \rho Z ) .$ This proves（4.9) for the tangent spaceparametrization ofamanifold.

Example 4.6.Werepeated theexperiment of Example4.2with Algorithm IV.5.3, using tangent space parametrizationand the trapezoidal ruleas basic integrator,and compared it to the symmetrized version of Algorithm 4.5.We were surprised to see thatboth algorithms worked equally well and gavea numerical solution lying near aclosed curve.An explanation is given in Exercise11.There it is shown that for the special situation where $\mathcal { M }$ isasphere,the standard algorithm isalsosymmetric for the trapezoidal rule.Letus therefore modify the problem slightly.

![](images/555b1e478600fa439dcd9656bb54ff3d7b75df68a1af8796d29ac47eb91f9eab.jpg)  
Fig.4.6.Numerical simulation of therigid body equations;standard use of tangent space parametrization with the trapezoidal ruleas basic method (left picture)and its symmetrized version(right picture);5OoO stepswith step size $h = 0 . 4$

Weconsider the rigid body equations(IV.1.4)asadifferential equation on the manifold

$$
\mathcal { M } = \Big \{ ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) \Big | \frac { y _ { 1 } ^ { 2 } } { I _ { 1 } } + \frac { y _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { y _ { 3 } ^ { 2 } } { I _ { 3 } } = C o n s t \Big \}
$$

with parametersand initial dataasin Example4.2,andweapplythestandard and the symmetrized method based on tangent space parametrization.Theresultis shown inFig.4.6.In both cases the numerical solution lies on themanifold(by definition ofthemethod),but only the'symmetric method hasacorrectlong-timebehaviour.

Symmetric Lie Group Methods.We turn our attention to particular problems

$$
{ \dot { Y } } = A ( Y ) Y , \qquad Y ( 0 ) = Y _ { 0 } ,
$$

where $A ( Y )$ is in the Liealgebra gwhenever $Y$ is in the corresponding Lie group $G$ Theexact solution then evolves on the manifold $G$ Munthe-Kaas methods (Sect.IV.8.2）are in general not symmetric,evenif theunderlyingRunge-Kutta method issymmetric.Thisisdue totheunsymmetricuse of thelocal coordinates $\begin{array} { r } { Y = \exp ( \varOmega ) Y _ { 0 } . } \end{array}$ However,accidentally,theLie groupmethod based on the implicit midpoint rule

$$
Y _ { n + 1 } = \exp ( \varOmega ) Y _ { n } , \qquad \varOmega = h A \big ( \exp ( \varOmega / 2 ) Y _ { n } \big )
$$

is symmetric.This can be seen as usual by exchanging $h  - h$ and $Y _ { n }  Y _ { n + 1 }$ （andalso $\Omega  - \Omega$ fortheauxiliary variable).Numerical computationswith the rigid body equations(considered asa problem on the sphere) shows an excellent long-time behaviour for this method similar to that of theright picturein Fig.4.6.In contrast to the implicit midpoint rule(I.1.7),the numerical solution of(4.12)does not lie exactly on the ellipsoid(4.1O）;seeExercise 12.

For the construction of further symmetric Lie group methods we can apply the ideasofAlgorithm4.5.Aslocal parametrizationwechoose

$$
\begin{array} { r } { \psi _ { U } ( \Omega ) = \exp ( \Omega ) U , } \end{array}
$$

where $U = \exp ( \Theta ) Y _ { n }$ plays the role of the midpoint on the manifold.We put $Z _ { n } =$ $- \Theta$ sothat $\psi _ { U } ( Z _ { n } ) = Y _ { n }$ With this starting value $Z _ { n }$ weapply any symmetric Runge-Kutta method to the differential equation

$$
\dot { \Omega } = A \big ( \psi _ { U } ( \Omega ) \big ) + \sum _ { k = 1 } ^ { q } \frac { B _ { k } } { k ! } \mathrm { a d } _ { \Omega } ^ { k } \Big ( A \big ( \psi _ { U } ( \Omega ) \big ) \Big ) , \qquad \Omega ( 0 ) = - \theta ,
$$

(cf.(IV.8.9))and thus obtain ${ \bar { Z } } _ { n + 1 }$ According to Algorithm 4.5, $\Theta$ isimplicitly determined by the condition $Z _ { n } + \bar { Z } _ { n + 1 } = 0$ ,and the numerical approximation is obtained from

$$
Y _ { n + 1 } = \psi _ { U } ( \widetilde { Z } _ { n + 1 } ) = \exp ( \widetilde { Z } _ { n + 1 } ) \exp ( \Theta ) Y _ { n } = \exp ( 2 \Theta ) Y _ { n } .
$$

Themethod obtained in this way isidentical to Algorithm2of Zanna,Engg& Munthe-Kaas (2Oo1).With the coeficients of the 2-stage Gaussmethod(Table II.1.1）and with $q = 1$ in（4.14）we thus get

$$
\begin{array} { r l r } {  { \mathcal { D } _ { 1 } = - h \frac { \sqrt { 3 } } { 6 } \Big ( A _ { 2 } - \frac { 1 } { 2 } [ \varOmega _ { 2 } , A _ { 2 } ] \Big ) , \qquad \mathcal { Q } _ { 2 } = h \frac { \sqrt { 3 } } { 6 } \Big ( A _ { 1 } - \frac { 1 } { 2 } [ \varOmega _ { 1 } , A _ { 1 } ] \Big ) } } \\ & { } & { { \displaystyle Y _ { n + 1 } = \exp \big ( 2 \theta \big ) Y _ { n } = \exp \Big ( \frac { h } { 2 } \big ( A _ { 1 } + A _ { 2 } \big ) - \frac { h } { 4 } \big ( [ \varOmega _ { 1 } , A _ { 1 } ] + [ \varOmega _ { 2 } , A _ { 2 } ] \big ) \Big ) Y _ { n } , } } \end{array}
$$

where $A _ { i } = A \big ( \exp ( \varOmega _ { i } ) \exp ( \theta ) Y _ { n } \big ) .$ This isa symmetric Lie group method of order four.We can reduce the number of commutators by replacing $\Omega _ { i }$ intheright-hand expressionwith itsdominating term.Thisyields

$$
\begin{array} { l } { { \Omega _ { 1 } = - h \displaystyle \frac { \sqrt { 3 } } { 6 } A _ { 2 } + \displaystyle \frac { h ^ { 2 } } { 2 4 } [ A _ { 1 } , A _ { 2 } ] , \displaystyle \qquad \Omega _ { 2 } = h \displaystyle \frac { \sqrt { 3 } } { 6 } A _ { 1 } - \displaystyle \frac { h ^ { 2 } } { 2 4 } [ A _ { 1 } , A _ { 2 } ] } } \\ { { { \cal Y } _ { n + \bar { 1 } } = \displaystyle \exp \Big ( \displaystyle \frac { h } { 2 } \big ( A _ { 1 } + A _ { 2 } \big ) - h ^ { 2 } \displaystyle \frac { \sqrt { 3 } } { 1 2 } [ A _ { 1 } , A _ { 2 } ] \Big ) { \cal Y } _ { n } } } \end{array}
$$

(cf.Exercise IV.19).Although we have neglected terms of size $\mathcal { O } ( h ^ { 4 } )$ ,themethod remains of order four,because the orderof symmetric methods isalways even.

Forany linear invertible transformation $\rho$ ,theparametrization(4.13） satisfies

$$
\rho \psi _ { U } ( \varOmega ) = \rho \exp ( \varOmega ) U = \exp ( \rho \varOmega \rho ^ { - 1 } ) \rho U = \psi _ { \rho U } ( \sigma U )
$$

with $\sigma \Omega = \rho \Omega \rho ^ { - 1 } .$ Hence(4.9) holds true.Ifthe problem(4.11)is $\rho$ -reversible,i.e., $\rho A ( Y ) = - A ( \rho Y ) \rho$ ,thenthe truncated differential equation (4.14）is $\sigma$ -reversible forallchoices of the truncation indexq.Moreover,after the simplificationsthat lead tomethod（4.15）,the $\rho$ -compatibilitycondition(1.4)isalsosatisfied.

Thefollowing variant isalso proposed in Zanna,Engg&Munthe-Kaas (2001). Instead of computing $\Theta$ from therelation $Z _ { n } + { \bar { Z } } _ { n + 1 } = 0$ , $\Theta$ is determined by

$$
Z _ { n } + \widetilde { Z } _ { n + 1 } = h \sum _ { i = 1 } ^ { s } e _ { i } \Big ( A _ { i } - \frac { 1 } { 2 } [ \Omega _ { i } , A _ { i } ] + . . . \Big ) .
$$

If the coefficients satisfy $e _ { s + 1 - i } ~ = ~ - e _ { i }$ this modification gives symmetric Lie group methods.

# V.5Energy-Momentum Methodsand Discrete Gradients

Conventional numerical methods,when applied to theordinarydifferentialequations of motion ofclassical mechanics,conserve thetotal energy andangular momentum only to the order of the truncation error.Since these constants of motion play acentral role in mechanics,itisagreat advantage to beable toconserve them exactly.

(R.A.LaBudde&D.Greenspan1976)

This section is concerned with numerical integrators for the equations of motion ofclassical mechanicswhich conserve both the total energyand angular momentum.Their construction is related to the concept of discrete gradients.The methodsconsidered are symmetric,which isincidental but useful:in our view their good long-time behaviourisaconsequence of their symmetry (and reversibility) more than of their exact conservation properties;see thedisappointing behaviour of thenon-symmetric energy-and momentum-conserving projection methodin ExampleIV.4.4.

AModified Midpoint Rule.Considerfirst a singleparticle of mass $m$ in $\mathbb { R } ^ { 3 }$ , with position coordinates $q ( t ) \in \mathbb { R } ^ { 3 }$ ,moving inacentral force field with potential $U ( q ) = V ( \left| | q | \right| )$ (e.g., $V ( r ) = - 1 / r$ in theKepler problem).With themomenta $p ( t ) = m \dot { q } ( t )$ ,the equations of motion read

$$
\dot { q } = \frac { 1 } { m } p , \dot { p } = - \nabla U ( q ) = - V ^ { \prime } ( \lVert q \rVert ) \frac { q } { \lVert q \rVert } .
$$

Constants of motion are the total energy $H ~ = ~ T ( p ) + U ( q )$ ,with $T ( p ) \ =$ $\| p \| ^ { 2 } / ( 2 m )$ and theangularmomentum $\scriptstyle { L = q \times p }$

$$
{ \frac { d } { d t } } ( { \boldsymbol { q } } \times { \boldsymbol { p } } ) = { \dot { { \boldsymbol { q } } } } \times { \boldsymbol { p } } + { \boldsymbol { q } } \times { \dot { \boldsymbol { p } } } = { \frac { 1 } { m } } { \boldsymbol { p } } \times { \boldsymbol { p } } - V ^ { \prime } ( \left\| { \boldsymbol { q } } \right\| ) { \frac { 1 } { \left\| { \boldsymbol { q } } \right\| } } { \boldsymbol { q } } \times { \boldsymbol { q } } = 0 ~ .
$$

Weknow from Sect.IV.2 that the implicit midpoint rule conserves the quadratic invariant $\scriptstyle { L = q \times p }$ ,andTheoremIV.2.4(orasimple direct calculation)shows that $L$ remains actuallyconserved byanymodification of the form

$$
\begin{array} { l c l } { { q _ { n + 1 } } } & { { = } } & { { q _ { n } + { \displaystyle \frac { h } { m } } p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { \mathrm { w i t h } } } \\ { { p _ { n + 1 } } } & { { = } } & { { p _ { n } - \kappa h \nabla U ( q _ { n + 1 / 2 } ) } } \end{array} \quad \begin{array} { l c l } { { } } & { { p _ { n + 1 / 2 } = { \frac { 1 } { 2 } } ( p _ { n } + p _ { n + 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { ~ q _ { n + 1 / 2 } = { \frac { 1 } { 2 } } ( q _ { n } + q _ { n + 1 } ) } } \end{array}
$$

where $\kappa$ isanarbitraryreal number.Simo,Tarnow&Wong（1992）introduce thisadditional parameter $\kappa$ and determine it so that the total energy is conserved: $H ( p _ { n + 1 } , q _ { n + 1 } ) \ = \ H ( p _ { n } , q _ { n } )$ With the notation $F _ { n + 1 / 2 } ~ = ~ - \nabla U ( q _ { n + 1 / 2 } ) ~ =$ $- V ^ { \prime } ( \| q _ { n + 1 / 2 } \| ) / \| q _ { n + 1 / 2 } \| \cdot q _ { n + 1 / 2 }$ we have

$$
T ( p _ { n + 1 } ) = T ( p _ { n } + \kappa h F _ { n + 1 / 2 } ) = T ( p _ { n } ) + \frac { \kappa h } { m } p _ { n + 1 / 2 } ^ { T } F _ { n + 1 / 2 } ,
$$

and hence the condition for conservation of the total energy $H = T + U$ becomes

$$
\kappa \frac { h } { m } p _ { n + 1 / 2 } ^ { T } F _ { n + 1 / 2 } = U ( q _ { n } ) - U ( q _ { n + 1 } ) .
$$

This givesareasonablemethodevenif $p _ { n + 1 / 2 } ^ { T } F _ { n + 1 / 2 }$ is arbitrarilyclose to zero. This is seen as follows: let $\sigma = - \kappa V ^ { \prime } ( \vert \vert q _ { n + 1 / 2 } \vert \vert ) / \vert \vert q _ { n + 1 / 2 } \vert \vert$ sothat $\kappa F _ { n + 1 / 2 } =$ $\sigma q _ { n + 1 / 2 } .$ Theabove condition for energy conservation then reads

$$
\sigma \frac { h } { m } p _ { n + 1 / 2 } ^ { T } q _ { n + 1 / 2 } = V ( \left\| q _ { n } \right\| ) - V ( \left\| q _ { n + 1 } \right\| ) ,
$$

where we note further that

$$
\begin{array} { r l } & { \frac { h } { m } p _ { n + 1 / 2 } ^ { T } q _ { n + 1 / 2 } = ( q _ { n + 1 } - q _ { n } ) ^ { T } \frac { 1 } { 2 } ( q _ { n + 1 } + q _ { n } ) } \\ & { \qquad = \frac { 1 } { 2 } \big ( \| q _ { n + 1 } \| ^ { 2 } = \| q _ { n } \| ^ { 2 } \big ) = \big ( \| q _ { n + 1 } \| - \| q _ { n } \| \big ) \frac { 1 } { 2 } \big ( \| q _ { n + 1 } \| + \| q _ { n } \| \big ) . } \end{array}
$$

These formulas give

$$
\sigma = - \frac { V ( | | q _ { n + 1 } | | ) - V ( | | q _ { n } | | ) } { | | q _ { n + 1 } | | - | | q _ { n } | | } \frac { 1 } { \frac { 1 } { 2 } \big ( | | q _ { n + 1 } | | + | | q _ { n } | | \big ) } ,
$$

with which method (5.1) becomes

$$
\begin{array} { l } { q _ { n + 1 } ~ = ~ q _ { n } + \displaystyle \frac { h } { m } p _ { n + 1 / 2 } } \\ { p _ { n + 1 } ~ = ~ p _ { n } - h \displaystyle \frac { V ( | | q _ { n + 1 } | | ) - V ( | | q _ { n } | | ) } { | | q _ { n + 1 } | | - | | q _ { n } | | } \displaystyle \frac { q _ { n + 1 / 2 } } { \frac { 1 } { 2 } \big ( | | q _ { n + 1 } | | + | | q _ { n } | | \big ) } . } \end{array}
$$

Thisisa second-order symmetric method which conserves the total energy and the angular momentum.It evaluates only the potential $U ( q ) = V ( \| q \| )$ Theforce $\begin{array} { r } { - \nabla U ( q ) = - V ^ { \prime } ( \| q \| ) \frac { q } { \| q \| } } \end{array}$ isapproximatedbyfinitedifferences.

Theenergy-and momentum-conserving method (5.3) first appeared in LaBudde &Greenspan (1974).The method (5.1） or (5.3) is the starting point for extensions inseveral directions to other problems of mechanics and other methods;see Simo,

Tarnow&Wong(1992),Simo&Tarnow（1992）,Lewis&Simo(1994,1996),Gonzalez& Simo (1996),Gonzalez (1996),and Reich(1996b).In the followingwe considera direct generalization to systems of particles,also given inLaBudde& Greenspan (1974).

AnEnergy-MomentumMethod forN-Body Systems. We considera systemof $N$ particles interacting pairwise with potential forces which depend on the distances betweentheparticles.AsinExample IV.1.3,thisis formulatedasaHamiltonian systemwith total energy

$$
H ( p , q ) = { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { N } { \frac { 1 } { m _ { i } } } p _ { i } ^ { T } p _ { i } + \sum _ { i = 2 } ^ { N } \sum _ { j = 1 } ^ { i - 1 } V _ { i j } \Bigl ( \lVert q _ { i } - q _ { j } \rVert \Bigr ) .
$$

Asan extension of method (5.3),we consider the following method (where we now write the time step number asa superscript for notational convenience)

$$
\begin{array} { l } { { q _ { i } ^ { n + 1 } = q _ { i } ^ { n } + \displaystyle \frac { h } { m _ { i } } p _ { i } ^ { n + 1 / 2 } } } \\ { { \displaystyle p _ { i } ^ { n + 1 } = p _ { i } ^ { n } + h \sum _ { j = 1 } ^ { N } \sigma _ { i j } \left( q _ { i } ^ { n + 1 / 2 } - q _ { j } ^ { n + 1 / 2 } \right) } } \end{array}
$$

where $\begin{array} { r } { p _ { i } ^ { n + 1 / 2 } = \frac { 1 } { 2 } ( p _ { i } ^ { n } + p _ { i } ^ { n + 1 } ) , q _ { i } ^ { n + 1 / 2 } = \frac { 1 } { 2 } ( q _ { i } ^ { n } + q _ { i } ^ { n + 1 } ) , } \end{array}$ and for $i > j$

$$
\sigma _ { i j } = \sigma _ { j i } = - \frac { V _ { i j } ( r _ { i j } ^ { n + 1 } ) - V _ { i j } ( r _ { i j } ^ { n } ) } { r _ { i j } ^ { n + 1 } - r _ { i j } ^ { n } } \frac { 1 } { \frac { 1 } { 2 } ( r _ { i j } ^ { n } + r _ { i j } ^ { n + 1 } ) }
$$

with $r _ { i j } ^ { n } = \| q _ { i } ^ { n } - q _ { j } ^ { n } \| .$ and $\sigma _ { i i } = 0 .$ This method has the following properties.

Theorem5.1(LaBudde&Greenspan1974).Themethod(5.5）with(5.6）isa Sem $\begin{array} { r } { P = \sum _ { i = 1 } ^ { N } p _ { i } , } \end{array}$ i=1Pi,the total angularmomentumL= $\begin{array} { r } { L = \sum _ { i = 1 } ^ { N } q _ { i } \times p _ { i } , } \end{array}$ energy $H$ ,

Proof.A comparison of (5.6) with the equations of motion shows that the method isoforder2.Similar to the continuous case(Example IV.1.3), the conservation oflinear and angular momentum is obtained asa consequence of the symmetry $o _ { i j } = \sigma _ { j i }$ forall $i , j .$ For thelinear momentum we have

$$
\sum _ { i = 1 } ^ { N } p _ { i } ^ { n + 1 } = \sum _ { i = 1 } ^ { N } p _ { i } ^ { n } + h \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } \sigma _ { i j } \left( q _ { i } ^ { n + 1 / 2 } - q _ { j } ^ { n + 1 / 2 } \right) = \sum _ { i = 1 } ^ { N } p _ { i } ^ { n } .
$$

For the proof of the conservation of the angular momentum we observe that the firstequationof（5.5)togethrwith $p _ { i } ^ { n + 1 / 2 } = \frac { 1 } { 2 } ( p _ { i } ^ { n + 1 } + p _ { i } ^ { n } )$ yields

$$
\left( q _ { i } ^ { n + 1 } - q _ { i } ^ { n } \right) \times \left( p _ { i } ^ { n + 1 } + p _ { i } ^ { n } \right) = 0
$$

for all $i$ Thesecondequatioof5.5tei $q _ { i } ^ { n + 1 / 2 } = \frac { 1 } { 2 } ( q _ { i } ^ { n + 1 } + q _ { i } ^ { n } )$ gives

$$
\sum _ { i = 1 } ^ { N } ( q _ { i } ^ { n + 1 } + q _ { i } ^ { n } ) \times \left( p _ { i } ^ { n + 1 } - p _ { i } ^ { n } \right) = 0 ,
$$

because $\sigma _ { i j } = \sigma _ { j i }$ andt terefore $\begin{array} { r } { \sum _ { i , j = 1 } ^ { N } \sigma _ { i j } \ : q _ { i } ^ { n + 1 / 2 } \times q _ { j } ^ { n + 1 / 2 } = 0 . } \end{array}$ =0.Adding thesum over $i$ of(5.7)totheequation（5.8)provesthestatement $\begin{array} { r l r } { \sum _ { i = 1 } ^ { N } q _ { i } ^ { n + 1 } \times p _ { i } ^ { n + 1 } = } \end{array}$ $\textstyle \sum _ { i = 1 } ^ { N } q _ { i } ^ { n } \times p _ { i } ^ { n }$

howe h $T ( p ) =$ $\begin{array} { r } { \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } m _ { i } ^ { - 1 } p _ { i } ^ { T } p _ { i } } \end{array}$ $n + 1$

$$
\begin{array} { r } { T ( p ^ { n + 1 } ) \ = \ T ( p ^ { n } ) + \displaystyle \sum _ { i = 1 } ^ { N } ( \frac { h } { m _ { i } } p _ { i } ^ { n + 1 / 2 } ) ^ { T } \displaystyle \sum _ { j = 1 } ^ { N } \sigma _ { i j } \left( q _ { i } ^ { n + 1 / 2 } - q _ { j } ^ { n + 1 / 2 } \right) } \\ { \ = \ T ( p ^ { n } ) + \displaystyle \sum _ { i = 1 } ^ { N } \displaystyle \sum _ { j = 1 } ^ { N } \sigma _ { i j } \left( q _ { i } ^ { n + 1 } - q _ { i } ^ { n } \right) ^ { T } \left( q _ { i } ^ { n + 1 / 2 } - q _ { j } ^ { n + 1 / 2 } \right) . } \end{array}
$$

Using once more the symmetry $\sigma _ { i j } = \sigma _ { j i }$ ,the double sum reduces to

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \displaystyle \sum _ { i = 1 } ^ { N } \displaystyle \sum _ { j = 1 } ^ { N } \sigma _ { i j } \left( \left( q _ { i } ^ { n + 1 } - q _ { j } ^ { n + 1 } \right) = \left( q _ { i } ^ { n } - q _ { j } ^ { n } \right) \right) ^ { T } \frac { 1 } { 2 } \Big ( \left( q _ { i } ^ { n + 1 } - q _ { j } ^ { n + 1 } \right) + \left( q _ { i } ^ { n } - q _ { j } ^ { n } \right) } \\ & { \quad \quad = \displaystyle \sum _ { i = 2 } ^ { N } \displaystyle \sum _ { j = 1 } ^ { i - 1 } \sigma _ { i j } \frac { 1 } { 2 } \Big ( \left( r _ { i j } ^ { n + 1 } \right) ^ { 2 } - \left( r _ { i j } ^ { n } \right) ^ { 2 } \Big ) . } \end{array}
$$

On the other hand,thechange in thepotential energy is

$$
U ( q ^ { n + 1 } ) - U ( q ^ { n } ) = \sum _ { i = 2 } ^ { N } \sum _ { j = 1 } ^ { i - 1 } \left( V _ { i j } ( r _ { i j } ^ { n + 1 } ) - V _ { i j } ( r _ { i j } ^ { n } ) \right) ,
$$

and hence (5.6)yields the conservation of the total energy $H = T + U$

Discrete-GradientMethods.The methods(5.3)and(5.5)are ofthe form

$$
y _ { n + 1 } = y _ { n } + h \overline { { B } } ( y _ { n + 1 } , y _ { n } ) \overline { { \nabla } } H ( y _ { n + 1 } , y _ { n } )
$$

where $B ( \widehat { y } , y )$ isaskew-symmetric matrix forall ${ \widehat { y } } , y$ ,and $\nabla H ( \widehat { y } , y )$ isadiscrete gradient of $H$ ,that is,acontinuous function of $( \widehat { y } , y )$ satisfying

$$
\begin{array} { l } { \overline { { \nabla } } H ( \widehat { y } , y ) ^ { T } ( \widehat { y } - y ) = H ( \widehat { y } ) - H ( y ) } \\ { \overline { { \nabla } } H ( y , y ) = \nabla H ( y ) . } \end{array}
$$

The symmetry of the methods isseen from the properties $\overline { { B } } ( \widehat { y } , y ) = \overline { { B } } ( y , \widehat { y } )$ and $\overline { { \nabla } } H ( \widehat { y } , y ) \ = \nabla H ( y , \widehat { y } )$ Forexample,formethod(5.3）we have,with $y = ( p , q )$ and $\widehat { \boldsymbol { y } } = ( \widehat { \boldsymbol { p } } , \widehat { \boldsymbol { q } } )$ ，

$$
\begin{array} { r } { \overline { { B } } ( \widehat { y } , y ) = \left( \begin{array} { c c } { 0 } & { - I _ { 3 } } \\ { I _ { 3 } } & { 0 } \end{array} \right) \quad \mathrm { ~ a n d ~ } \quad \overline { { \nabla } } H ( \widehat { y } , y ) = \left( \begin{array} { c c } { \frac { 1 } { 2 } ( \widehat { p } + p ) } & \\ { \sigma ( \widehat { q } , q ) \frac { 1 } { 2 } ( \widehat { q } + q ) } \end{array} \right) } \end{array}
$$

where $\sigma ( \widehat { q } , q )$ is given by the expression (5.2)with $( \widehat { q } , q )$ in place of $( q _ { n + 1 } , q _ { n } )$ or by the corresponding limit as $\| { \widehat { q } } \| \to \| q |$

Thediscrete-gradient method(5.9) is consistent with the differential equation

$$
\dot { y } = B ( y ) \nabla H ( y )
$$

with the skew-symmetric matrix $B ( y ) = { \overline { { B } } } ( y , y ) .$ This system conserves $H$ ,since

$$
\frac { d } { d t } H ( y ) = \nabla H ( y ) ^ { T } \dot { y } = \nabla H ( y ) ^ { T } B ( y ) \nabla H ( y ) = 0 ,
$$

and,aswas noted by Gonzalez(1996)and McLachlan,Quispel&Robidoux (1999), $H$ is also conserved by method (5.9).

Theorem5.2.Thediscrete-gradientmethod(5.9) conserves the invariant $H$ ofthe system(5.11）.

Proof.The definitions (5.1O) ofa discrete gradient and of the method(5.9) give

$$
\begin{array} { r l } { H ( y _ { n + 1 } ) - H ( y _ { n } ) \ = \ \overline { { \nabla } } H ( y _ { n + 1 } , y _ { n } ) ^ { T } ( y _ { n + 1 } - y _ { n } ) } & { } \\ { \ } & { = \ h \overline { { \nabla } } H ( y _ { n + 1 } , y _ { n } ) ^ { T } \overline { { B } } ( y _ { n + 1 } , y _ { n } ) \overline { { \nabla } } H ( y _ { n + 1 } , y _ { n } ) = 0 \ , } \end{array}
$$

where thelastequalityfollows fromthe skew-symmetry of $\overline { { B } } ( y _ { n + 1 } , y _ { n } )$

Example5.3.TheLotka-Volterra system(I.1.1) canbewrittenas

$$
\left( \begin{array} { c } { \dot { u } } \\ { \dot { v } } \end{array} \right) = \left( \begin{array} { c c } { 0 } & { - u v } \\ { u v } & { 0 } \end{array} \right) \nabla H ( u , v )
$$

with the invariant $H ( u , v ) = \ln u - u + 2 \ln v - v$ of(I.1.4).Possible choices ofa discretegradient are the coordinate increment discrete gradient (Itoh&Abe1988)

$$
\overline { { \nabla } } H ( \widehat { u } , \widehat { v } ; u , v ) = \left( \frac { H ( \widehat { u } , v ) - H ( u , v ) } { \widehat { u } - u } \right)
$$

and the midpoint discrete gradient (Gonzalez 1996)

$$
\overline { { \nabla } } H ( \widehat { y } , y ) = \nabla H ( \overline { { y } } ) + \frac { H ( \widehat { y } ) - H ( y ) - \nabla H ( \overline { { y } } ) ^ { T } \varDelta y } { \| \varDelta y \| ^ { 2 } } \varDelta y
$$

with $\overline { { { y } } } = \frac { 1 } { 2 } ( \widehat { y } + y )$ and $\Delta y = { \widehat { y } } - y$ In contrast to (5.12),the discrete gradient (5.13)yieldsasymmetric discretization.

Asystematic study of discrete-gradient methods is given in Gonzalez (1996) andMcLachlan,Quispel&Robidoux（1999).

# V.6Exercises

1.Prove that (after asuitable permutation of the stages)the condition $c _ { s + 1 - i } =$ $1 - c _ { i }$ (forall $\textit { \textbf { l } }$ ）isalso necessary foracollocation method tobe symmetric.

2.Prove that explicit Runge-Kutta methods cannot be symmetric.

Hint.If a one-step method applied to $\dot { y } = \lambda y$ yields $y _ { 1 } = R ( h \lambda ) y _ { 0 }$ then,a necessary condition for thesymmetry ofthe method is $R ( z ) R ( - z ) = 1$ forall complex $z$ .

3.Consider an irreducible diagonally implicit Runge-Kutta method (irreducible inthe sense of Sect.VI.7.3).Prove that the condition (2.4) is necessary for the symmetry of.the method.No permutation of the stages hasto be performed.

4.LetΦh=h $\varPhi _ { h } = \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] }$ where $\varphi _ { t } ^ { [ i ] }$ represents the exact fow of $\dot { y } = f ^ { ( i ) } ( y )$ In the situation of TheoremII.3.17 prove that the local error(3.4) of the composition method（3.3)hasthe form

$$
h ^ { 3 } \Big ( \frac { 1 } { 2 4 } ( 6 \alpha - 1 ) \big [ D _ { 2 } , [ D _ { 2 } , D _ { 1 } ] \big ] + \frac { 1 } { 1 2 } ( 1 - 6 \alpha + 6 \alpha ^ { 2 } ) \big [ D _ { 1 } , [ D _ { 1 } , D _ { 2 } ] \big ] \Big ) { \cal I } d ( y ) ,
$$

where,as usual, $D _ { i } g ( y ) = g ^ { \prime } ( y ) f ^ { [ i ] } ( y )$ Thevalue $\alpha = 0 . 1 9 3 2$ is found by minimizing the expression $( 6 \alpha - 1 ) ^ { 2 } + 4 ( 1 - 6 \alpha + 6 \alpha ^ { 2 } ) ^ { 2 }$ (McLachlan 1995）.

5.For the linear transformation $\rho ( p , q ) = ( - p , q )$ ,considera $\rho$ -reversibleproblem （1.3）with scalar $\boldsymbol { p }$ and $q$ Prove that every solution which crosses the $q$ -axis twiceis periodic.

6.Prove that if a numerical method conserves quadratic invariants (IV.2.1),then so does its adjoint.

7.For the numerical solution of $\dot { y } = A ( t ) y$ consider themethod $y _ { n } \mapsto y _ { n + 1 }$ defined by $y _ { n + 1 } = z ( t _ { n } + h )$ ,where $z ( t )$ is the solution of

$$
\dot { z } = \widehat { A } ( t ) z , \qquad z ( t _ { n } ) = y _ { n } ,
$$

and $\mathbf { \boldsymbol { A } } ( t )$ is theinterpolationpolynomialbasedonsymmetric nodes $c _ { 1 } , \ldots , c _ { s }$ ， i.e., $c _ { s + 1 - i } + c _ { i } = 1$ forall $i$

a)Prove that this method is symmetric.

b)Show that $y _ { n + 1 } = \exp ( \varOmega ( h ) ) y _ { n }$ holds,where $\Omega ( h )$ has an expansion in odd powers of $h$ .This justifies the omission of the termsinvolvingtriple integrals inExampleIV.7.4.

8.If $\phi _ { h }$ stands for the implicit midpointrule,what are the Runge-Kutta coefficients of the composition method (3.8)?The general theory of Sect.II.1 gives threeorderconditions for order4(those forthe trees of order2and4areautomatically satisfiedbythesymmetryof themethod).Arethey compatiblewith thetwo conditions ofExample3.5?

9.Makea numerical comparison of our favourite composition methods $p 6 s 9$ $p 8 s 1 7$ ,and $p 1 0 s 3 5$ for the Lorenz problem

$$
\begin{array} { l l l } { { y _ { 1 } ^ { \prime } = - \sigma ( y _ { 1 } - y _ { 2 } ) } } & { { y _ { 1 } ( 0 ) = 1 0 } } & { { \sigma = 1 0 } } \\ { { y _ { 2 } ^ { \prime } = - y _ { 1 } y _ { 3 } + r y _ { 1 } - y _ { 2 } } } & { { y _ { 2 } ( 0 ) = - 2 0 } } & { { r = 2 8 } } \\ { { y _ { 3 } ^ { \prime } = y _ { 1 } y _ { 2 } - b y _ { 3 } } } & { { y _ { 3 } ( 0 ) = 2 0 } } & { { b = 8 / 3 } } \end{array}
$$

![](images/de6c89126723e68bf923286bf2bcb72109e557a3757c8fb37a368aee0e8d824c.jpg)  
Fig.6.1.Comparison of various composition methodsappliedto the Lorenz equations

with exact solution

by composing for $0 \leq t \leq 1$ thesecond order symmetric splitting scheme (see Kahan&Li1997)which,for the time-stepping $y _ { i } \mapsto Y _ { i }$ ,is given by

$$
\begin{array} { l c l } { { } } & { { } } & { { { \displaystyle Y _ { 1 } - y _ { 1 } } = \frac { h } { 2 } \big ( - \sigma ( y _ { 1 } + Y _ { 1 } - y _ { 2 } - Y _ { 2 } ) \big ) } } \\ { { } } & { { } } & { { { \displaystyle Y _ { 2 } - y _ { 2 } } = \frac { h } { 2 } \big ( - y _ { 1 } Y _ { 3 } - Y _ { 1 } y _ { 3 } + r y _ { 1 } + r Y _ { 1 } - y _ { 2 } - Y _ { 2 } \big ) } } \\ { { } } & { { } } & { { { \displaystyle Y _ { 3 } - y _ { 3 } } = \frac { h } { 2 } \big ( y _ { 1 } Y _ { 2 } + Y _ { 1 } y _ { 2 } - b y _ { 3 } - b Y _ { 3 } \big ) . } } \end{array}
$$

Thismethod requires,for each step,the solution ofa linear system only.The results are shown in Fig.6.1.

10.Symmetrized order conditions (Suzuki 1992).Prove that for methods (3.8)of order fourwith $\gamma _ { i }$ satisfying（3.10）

$$
\sum _ { k = 1 } ^ { s } \gamma _ { k } ^ { 3 } \Big ( { \sum _ { \ell = 1 } ^ { k } } ^ { \prime } \gamma _ { \ell } \Big ) ^ { 2 } = 0 \qquad \Longleftrightarrow \qquad \sum _ { k = 1 } ^ { s } \gamma _ { k } ^ { 3 } \Big ( { \sum _ { \ell = 1 } ^ { k } } ^ { \prime } \gamma _ { \ell } \Big ) \Big ( ^ { \prime } \sum _ { \ell = k } ^ { s } \gamma _ { \ell } \Big ) = 0 .
$$

The prime after (before)a sum sign indicates that the term with highest (lowest)index isdivided by 2.Prove also that the order conditions given in Suzuki （1992) for order $p \leq 8$ areequivalent to those of Example 3.5.Is thisalso true $p = 1 0$

Hint.Use onsike $\begin{array} { r } { \sum _ { \ell = 1 } ^ { k ^ { \prime } } \gamma _ { \ell } = 1 - \overset { \prime } { \sum } _ { \ell = k } ^ { s } \gamma _ { \ell } . } \end{array}$

11. Let $\mathcal { M } = \left\{ ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) | y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1 \right\}$ and consider for $a \in \mathcal { M }$ the tangent space parametrization

$$
\psi _ { a } ( z ) = a + z + a u _ { a } ( z ) ,
$$

where,for $z \in T _ { a } { \mathcal { M } }$ ,thereal value $u _ { a } ( z )$ isdetermined by therequirement $\psi _ { a } ( z ) \in \mathcal { M }$ ProvethatAlgorithmIV.5.3,with the trapezoidalruleintherole of $\phi _ { h }$ ,isasymmetric method.

Hint.Since $z$ is a linear combination of $a$ and $\psi _ { a } ( z )$ ,itisuniquelydetermined by $\boldsymbol { a } ^ { x } \boldsymbol { z }$ (which is zero）and $\psi _ { a } ( z ) ^ { \cal T } z$

12.(Zanna,Engg&Munthe-Kaas2Oo1).Verify numerically that theLiegroup method(4.12) based on the implicit midpoint rule doesnot conserve general quadratic first integrals.One canconsider the rigid body equations in the form (IV.1.5).

# Chapter VI. Symplectic Integration of Hamiltonian Systems

![](images/24c4d4be25ac6b26ac9856512684dba9e08e807435504f2a26038729293ee2ab.jpg)  
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

![](images/a73a1a36a983a18e072977fa8797177f8cd5e64d004a479002f770d2fd370df7.jpg)  
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

![](images/a3d838c207711b1eea879e8c4ff4740bef17fe249f861e95cd5b1213b321fc62.jpg)  
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

![](images/1f971769db4f595c55722dce08ce8db704abc2b50c6295c8f330cb752b2c6044.jpg)  
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

![](images/1f14c6bb77912a668894ebc73594033d8e0bb665da27761b6250f0992f9d95e9.jpg)  
Feng Kang2

is symplectic whenever the method is applied to a smooth Hamiltonian system.

![](images/eb34f1f782bc672700b885c39a37e38e3f3fdb22586a8574c63d50cba6843c9f.jpg)  
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