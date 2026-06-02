# Chapter XIV. Oscillatory Differential Equations with Varying High Frequencies

Newaspects come into play when the high frequencies in an oscillatory system and their associated eigenspaces do not remain nearly constant,as in theprevious chapter,but change with time or depend onthe solution.Webegin by studying lineardifferential equations withatime-dependent skew-hermitianmatrix and then turnto nonlinear oscillatory mechanical systems with time-or solution-dependent frequencies.Our analysis uses canonical coordinate transforms that separate slow and fast motions and relate the fast oscillations to the skew-hermitian linear case.For thenumerical treatment we consider suitably constructed long-time-stepmethods ("adiabatic integrators")and multiple time-stepping methods.

# XIV.1LinearSystems with Time-Dependent Skew-Hermitian Matrix

Weconsider first-order lineardifferential equationswith a skew-hermitian matrix thatchanges slowly compared to the rapid oscillations in the solution,aproblem thathas attracted much attention in quantummechanics.We present asuitableclass ofnumerical methods,termed adiabatic integrators,which can take time steps that aresubstantially larger than the almost-periods of the oscillations.

# XIV.1.1 Adiabatic Transformationand AdiabaticInvariants

It comes from the greek aδLαβaTlxos,"which cannot be crossed".

..wearriveby analogyto the“adiabaticprinciple”used in Quantum andthen Classical Mechanics.Itis based upon the fact that the harmonic oscillator (and other simpledynamical systemsas itwas found later) submittedto slow variations of its parametersmodifies itsenergybut keeps itsaction(energydivided by frequency) constant.

As wecan see,the path from the word“adiabatic”used in thermodynamicsto the above"adiabatic principle”is tortuous and our greek colleagues arecertainlypuzzled by sentences such as“the changes in theadiabatic invariant due to[..] crossing”whichwe shall use later.

(J.Henrard 1993)

$$
\dot { y } ( t ) = \frac { 1 } { \varepsilon } Z ( t ) y ( t ) ,
$$

where $Z ( t )$ isareal skew-symmetric(or complex skew-hermitian）matrix-valued function with time derivatives bounded independently of the small parameter $\varepsilon$ . In quantum dynamics such equations arise with $Z ( t ) = - i H ( t )$ ,where thereal symmetric（or hermitian）matrix $H ( t )$ represents the quantum Hamiltonian operatorina discrete-level Schrodinger equation.We will also encounter real equations ofthis type in thetreatment ofoscillatory classical mechanical systemswith timedependent frequencies.Solutions oscillate with almost-periods $\sim \varepsilon$ ,while the systemmatrix changes on a slower time scale $\sim 1$

Transforming the Problem.We begin by looking fora time-dependent linear transformation

$$
\eta ( t ) = T _ { \varepsilon } ( t ) y ( t ) ,
$$

taking the system to the form

$$
\Dot { \eta } ( t ) = S _ { \varepsilon } ( t ) \eta ( t ) \quad \mathrm { ~ w i t h ~ } \quad S _ { \varepsilon } = \Dot { T } _ { \varepsilon } T _ { \varepsilon } ^ { - 1 } \Lt + \frac { 1 } { \varepsilon } T _ { \varepsilon } Z T _ { \varepsilon } ^ { - 1 } ,
$$

which is chosen such that $S _ { \varepsilon } ( t )$ is of smaller norm than the matrix $\scriptstyle { \frac { 1 } { \varepsilon } } Z ( t )$ of(1.1).

Remark1.1.A first ideaisto freeze $\boldsymbol { Z } ( t ) \approx \boldsymbol { Z } _ { * }$ over a time step and to choose the transformation

$$
\Gamma _ { \varepsilon } ( t ) = \exp \left( - \frac { t } { \varepsilon } Z _ { * } \right) \mathrm { y i e l d i n g } S _ { \varepsilon } ( t ) = \frac { 1 } { \varepsilon } \exp \left( - \frac { t } { \varepsilon } Z _ { * } \right) \left( Z ( t ) - Z _ { * } \right) \exp \left( \frac { t } { \varepsilon } Z _ { * } \right) ,
$$

This matrix function $S _ { \varepsilon } ( t )$ is highly oscillatoryand bounded in norm by $\mathcal { O } ( h / \varepsilon )$ for $| t - t _ { 0 } | \leq h$ ,if $Z _ { * } = Z ( t _ { 0 } + h / 2 ) ,$ Numerical integrators based on this transformationare given byLawson（1967）and more recentlybyHochbruck&Lubich (1999b), Iserles (2002,2004),and Degani & Schiff(2003).Reasonable accuracy still requires step sizes $h = { \mathcal { O } } ( \varepsilon )$ ingeneral; see also Exercise 3.In the above papers this transfomation has,however,been put to good use in situationswhere the timederivatives of thematrix inthedifferential equation havemuch smaller norm than the matrix itself.

Adiabatic Transformation.Inorder to obtainadifferential equation(1.3）with a uniformly bounded matrix $S _ { \varepsilon } ( t )$ we diagonalize

$$
Z ( t ) = U ( t ) i \Lambda ( t ) U ( t ) ^ { * }
$$

withareal diagonal matrix $\begin{array} { r } { \Lambda ( t ) = \mathrm { d i a g } \left( \lambda _ { j } ( t ) \right) } \end{array}$ and aunitary matrix $U ( t ) =$ $( u _ { 1 } ( t ) , \ldots , u _ { n } ( t ) )$ of eigenvectors depending smoothly on $t$ (possibly except where eigenvalues cross).We define $\eta ( t )$ bytheunitaryadiabatic transformation

$$
\eta ( t ) = \exp \left( - \frac { i } { \varepsilon } \Phi ( t ) \right) U ( t ) ^ { * } y ( t ) \quad \mathrm { w i t h } \quad \varPhi ( t ) = \mathrm { d i a g } \left( \phi _ { j } ( t ) \right) = \int _ { 0 } ^ { t } { \varLambda ( s ) d s } ,
$$

which represents the solution ina rotating frame of eigenvectors.Each component of $\eta ( t )$ isa coefficient in the eigenbasis representation of $y ( t )$ rotated inthecomplexplane by the negative phase.Such transformations have been in use in quantummechanics since the work of Born&Fock（1928）onadiabatic invariantsin Schrodinger equations,asdiscussed in the next paragraph.The transformation(1.4) yieldsa differential equation where the $\circeq$ -independent skew-hermitianmatrix

$$
W ( t ) = \dot { U } ( t ) ^ { * } U ( t )
$$

isframed by oscillatory diagonal matrices:

$$
\dot { \eta } ( t ) = \exp \left( - \frac { i } { \varepsilon } \varPhi ( t ) \right) W ( t ) \exp \left( \frac { i } { \varepsilon } \varPhi ( t ) \right) \eta ( t ) .
$$

Numerical integrators for（1.1） based on the transformation to the differential equation(1.5）with bounded,though highlyoscillatoryright-hand side,are given by Jahnke&Lubich（2003)andJahnke(2004a);see Sect.XIV.1.2.

Adiabatic Invariants.Possibly afteratime-dependent rephasing of the eigenvectors, $u _ { k } ( t ) \longrightarrow e ^ { i \alpha _ { k } ( t ) } u _ { k } ( t )$ ,wecan assume that ${ \dot { u } } _ { k } ( t )$ isorthogonal to $u _ { k } ( t )$ for all $t$ (Thisisautomatically satisfiedif $U ( t )$ isareal orthogonal matrix,asis the case for $Z ( t ) = - i H ( t )$ withareal symmetric matrix $H ( t )$ ）Wethen have the matrix $W = ( w _ { \jmath k } ) = ( \dot { u } _ { \jmath } ^ { * } u _ { k } )$ with zero diagonal.

After integration of both sides of the differential equation(1.5） from O to $t$ , partial integration of the terms on theright-hand sideyields for $j \neq k$ (terms for $j = k$ do not appear since $w _ { j j } = 0$ ）

$$
\begin{array} { r l } & { \displaystyle \int _ { 0 } ^ { t } \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } ( s ) - \phi _ { k } ( s ) \bigr ) \Bigr ) w _ { j k } ( s ) \eta _ { k } ( s ) d s } \\ & { \displaystyle = i \varepsilon \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } ( s ) - \bar { \phi } _ { k } ( s ) \bigr ) \Bigr ) \frac { w _ { j k } ( s ) \eta _ { k } ( s ) } { \lambda _ { j } ( s ) - \lambda _ { k } ( s ) } \Bigr | _ { 0 } ^ { t } } \\ & { \quad \displaystyle - i \varepsilon \int _ { 0 } ^ { t } \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } ( s ) - \phi _ { k } ( s ) \bigr ) \Bigr ) \frac { d } { d s } \frac { w _ { j k } ( s ) \eta _ { k } ( s ) } { \lambda _ { j } ( s ) - \lambda _ { k } ( s ) } d s . } \end{array}
$$

At this point, suppose that the eigenvalues $\lambda _ { j } ( t )$ are,for all $t$ ,separated fromeach other byapositivedistance $\delta$ independent of $\varepsilon$

$$
| \lambda _ { j } ( t ) - \lambda _ { k } ( t ) | \geq \delta \qquad { \mathrm { f o r ~ a l l ~ } } j \neq k .
$$

Then thereciprocals of theirdifferences and the coupling matrix $W ( t )$ arebounded independentlyof $\varepsilon$ ,asaretheir derivatives.Togetherwith the boundedness of $\dot { \eta }$ as implied by(1.5),this shows

$$
\eta ( t ) = \eta ( 0 ) + O ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

Thisresultisaversion of the quantum-adiabatic theorem of Born& Fock（1928) which states that the actions $| \eta _ { j } | ^ { 2 }$ (the energy in the $j$ thstate, $\langle \eta _ { j } u _ { j } , H \eta _ { j } u _ { j } \rangle =$ $\lambda _ { j } | \eta _ { j } | ^ { 2 }$ ,dividedbythe frequency $\lambda _ { j }$ ）remain approximately constant for times $t =$ $\mathcal { O } ( 1 )$ .Such functions $I ( y , t )$ that satisfy $I ( y ( t ) , t ) = I ( y ( 0 ) , 0 ) + \mathcal { O } ( \varepsilon )$ for $t =$ $\mathcal { O } ( 1 )$ along every $\mathcal { O } ( 1 )$ -bounded solution $y ( t )$ ofthe differential equation,arecalled adiabatic invariants.

Super-Adiabatic Transformations.Adiabatic invariants are obtained over longer time scales byrefining the transformation;see Lenard (1959)and Garrido (1964). Herewe show that the transformation matrix $T _ { \epsilon }$ of（1.2） can be constructed such that thematrix $S _ { \epsilon }$ inthe transformed differential equation(1.3)is of size $\mathcal { O } ( \varepsilon ^ { N } )$ . Letusmake the ansatz ofaunitary transformation matrix

$$
T _ { \varepsilon } ^ { ( N ) } = \exp \Bigl ( - \frac { i } { \varepsilon } \Phi \Bigr ) \exp ( - i \Phi _ { 1 } ) \exp ( \varepsilon X _ { 1 } ) \ldots \exp ( - i \varepsilon ^ { N - 1 } \Phi _ { N } ) \exp ( \varepsilon ^ { N } X _ { N } )
$$

withreal diagonal matrices $\varPhi _ { n } ( t )$ and complex skew-hermitian matrices $X _ { n } ( t )$ We find that $\begin{array} { r } { S _ { \varepsilon } = \frac { 1 } { \varepsilon } T _ { \varepsilon } Z T _ { \varepsilon } ^ { * } + T _ { \varepsilon } T _ { \varepsilon } ^ { * } } \end{array}$ is $\mathcal { O } ( \varepsilon )$ if and only if $X _ { 1 }$ and $\varLambda _ { 1 } : = \dot { \Phi } _ { 1 }$ satisfy

$$
{ \frac { 1 } { \varepsilon } } \Bigl ( \exp ( \varepsilon X _ { 1 } ) i \lambda \exp ( - \varepsilon X _ { 1 } ) - i \lambda \Bigr ) - i A _ { 1 } + W = \mathcal { O } ( \varepsilon ) ,
$$

orequivalently,if $X _ { 1 }$ and $\varLambda _ { 1 }$ solve the commutator equation

$$
[ i \varLambda , X _ { 1 } ] + i \varLambda _ { 1 } = W .
$$

This is solved by setting $i A _ { 1 }$ equal to the diagonal of $W$ and determining the offdiagonal entries $x _ { j k } ^ { ( 1 ) }$ of $X _ { 1 }$ from the scalar equations

$$
i ( \lambda _ { j } - \lambda _ { k } ) x _ { j k } ^ { ( 1 ) } = w _ { j k } , \qquad j \neq k ,
$$

which can be doneas longas the eigenvalues are separated.The diagonal of $X _ { 1 }$ is set to zero. Since $W$ is skew-hermitian,so is $X _ { 1 }$ Similarlyweobtainforhigher powers of $\boldsymbol { \varepsilon }$ theequations

$$
[ i \varLambda , X _ { n } ] + i \varLambda _ { n } = W _ { n - 1 } ,
$$

where thematrix $W _ { n - 1 }$ contains only previously constructed terms up to index $n { - } 1$ andderivativesup to order $\boldsymbol { n }$ andisskew-hermitian because $S _ { \varepsilon }$ isskew-hermitian. Inthiswaywe obtainaunitary transformation such that

$$
\eta ^ { ( N ) } ( t ) = T _ { \varepsilon } ^ { ( N ) } ( t ) y ( t ) \qquad \mathrm { s a t i s f i e s } \quad \dot { \eta } ^ { ( N ) } = \mathcal { O } ( \varepsilon ^ { N } ) .
$$

Weremark thattheaboveconstructionof $T _ { \varepsilon } ^ { ( N ) }$ is analogous totransformations in Hamiltonian perturbation theory;cf.Sect.X.2.

The differential equation (1.1)thus has adiabatic invariants over times $\mathcal { O } ( \varepsilon ^ { - N } )$ forarbitrary $N \geq 1$ ,andin fact even over exponentially long time intervals $t = \mathcal { O } ( e ^ { c / \varepsilon } )$ if the functions havea bounded analytic extension toacomplex strip, asisshownbyJoye&Pfister(1993)andNenciu(1993).The leadingtermin theexponentillysmalldeviationof $| \eta _ { j } ^ { ( N ) } ( t ) | ^ { 2 }$ intheoptimallytuncatedsupebtic basis hasbeenrigorouslymade explicitby Betz&Teufel(20o5a,20o5b),proving aconjecture by Berry (1990).

Avoided Crossing of Eigenvalues and Non-Adiabatic Transitions.To illustrate the effects ofaviolation of the separation condition（1.7),we consider the generic two-dimensional example studiedby Zener(1932),with thematrix

$$
{ \cal Z } ( t ) = - i \left( \begin{array} { c c } { { t } } & { { \delta } } \\ { { \delta } } & { { - t } } \end{array} \right) ,
$$

which has the eigenvalues $\pm i \sqrt { t ^ { 2 } + \delta ^ { 2 } }$ Theminimal distance of the eigenvalues is $2 \delta$ at $t = 0$ For $\delta = \mathcal { O } ( \sqrt { \varepsilon } )$ theadiabatic invariance（1.8） is no longervalid,and $\eta$ canundergo $\mathcal { O } ( 1 )$ changes in an $\mathcal { O } ( \delta )$ neighbourhoodof $t = 0$ ：anon-adiabatic transitioninphysical terminology.Thechanges in theadiabatic invariant due to the avoided crossing of eigenvalues are illustrated in Fig.1.1and can beexplained as follows.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0008_pages_0491-0560/auto/images/457d2823b7a3ffb4fcca190f5b6ff63c5d9a97dd144a3a275afe80e24801ddc4.jpg)  
Fig.1.1.Non-adiabatictransition: $| \eta _ { 1 } ( t ) | ^ { 2 }$ and $| \eta _ { 2 } ( t ) | ^ { 2 }$ as function of $t$ for $\varepsilon = 0 . 0 1$ and $\delta = 2 ^ { - 1 } , 2 ^ { - 3 } , 2 ^ { - 5 } , 2 ^ { - 7 }$ (increasingdarkness)

Near the avoided crossing,anew time scale $\tau = t / \delta$ isappropriate.The decomposition $Z ( t ) = U ( t ) i \varLambda ( t ) U ( t ) ^ { T }$ of the matrix yields

$$
\begin{array} { r l r } { U ( t ) = \widetilde { U } ( \tau ) } & { = } & { \left( \begin{array} { c c } { \cos \alpha ( \tau ) } & { - \sin \alpha ( \tau ) } \\ { \sin \alpha ( \tau ) } & { \cos \alpha ( \tau ) } \end{array} \right) , } \\ { A ( t ) / \delta = \widetilde { A } ( \tau ) } & { = } & { \left( \begin{array} { c c } { - \sqrt { \tau ^ { 2 } + 1 } } & { 0 } \\ { 0 } & { \sqrt { \tau ^ { 2 } + 1 } } \end{array} \right) , } \end{array}
$$

with $\begin{array} { r } { \alpha ( \tau ) = \frac { \pi } { 4 } - \frac { 1 } { 2 } } \end{array}$ arctan $( \tau )$ .We introduce therescaled matrices

$$
\begin{array} { r c l } { { \widetilde \Phi ( \tau ) } } & { { = } } & { { \displaystyle \int _ { 0 } ^ { \tau } \widetilde { \cal A } ( \sigma ) d \sigma = \displaystyle \Phi ( t ) / \delta ^ { 2 } , } } \\ { { \widetilde W ( \tau ) } } & { { = } } & { { \displaystyle \left( \frac { d } { d \tau } \widetilde { U } ( \tau ) ^ { T } \right) \widetilde { U } ( \tau ) = \displaystyle \frac { 1 } { 2 ( \tau ^ { 2 } + 1 ) } \left( \begin{array} { l l } { { 0 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) = \delta \cdot W ( t ) . } } \end{array}
$$

Note that the entries of $W ( t )$ havea sharp peak of height $( 2 \delta ) ^ { - 1 }$ at $t = 0$ The rescaled function $\widetilde { \eta } ( \tau ) = \eta ( t )$ isasolution of the differential equation

$$
\frac { d } { d \tau } \widetilde { \eta } ( \tau ) = \exp \left( - \frac { i \delta ^ { 2 } } { \varepsilon } \widetilde { \Phi } ( \tau ) \right) \widetilde { W } ( \tau ) \exp \left( \frac { i \delta ^ { 2 } } { \varepsilon } \widetilde { \Phi } ( \tau ) \right) \widetilde { \eta } ( \tau ) .
$$

For $\delta ^ { 2 } \leq \varepsilon$ and $| \tau | = | t / \delta | \leq 1$ ,thematrix on the right-hand sideis bounded of norm $\sim 1$ and has bounded derivativeswithrespect to $\gamma$ Thefunction $\overline { { \eta } } ( \tau )$ therefore changes itsvalue by an amount of size $\mathcal { O } ( 1 )$ in the interval $| \tau | \leq 1$ Wealsonote thatany numerical integrator using piecewise polynomial approximations of $W ( t )$ and hence of $W ( \tau )$ must take step sizes $\Delta \tau = h / \delta \ll 1$ ,i.e., $h \ll \delta$ .Onthe otherhand,the rescaling shows that the number of time steps needed to resolve the non-adiabatic transition uptoa specifiedaccuracy is independent of $\delta$ .

# XIV.1.2Adiabatic Integrators

Wediscuss symmetric long-time-step integrators fortherotating-frame differential equation(1.5） that describes skew-hermitiansystemsin adiabatic variables.The construction follows Jahnke&Lubich(2Oo3) andJahnke(2004a);see also Lorenz, Jahnke&Lubich（2005).

First-Order Integrators.We consider thedifferential equation (1.5)and integrate both sides from $t _ { n }$ to $t _ { n + 1 } = t _ { n } + h$ :

$$
\eta ( t _ { n + 1 } ) = \eta ( t _ { n } ) + \int _ { t _ { n } } ^ { t _ { n + 1 } } \exp \left( - \frac { i } { \varepsilon } \varPhi ( s ) \right) W ^ { \prime } ( s ) \exp \left( \frac { i } { \varepsilon } \varPhi ( s ) \right) \eta ( s ) d s ,
$$

where $W ( t )$ isan $\boldsymbol { \mathsf { \Sigma } }$ -independent matrix,continuouslydifferentiablein $t$ ,andthe real diagonal matrix of phases $\varPhi ( t )$ is given as the integral of $\begin{array} { r } { \Lambda ( t ) = \mathrm { d i a g } \left( \lambda _ { j } ( t ) \right) } \end{array}$ . In the applications, $W ( t )$ and $\varPhi ( t )$ are not given explicitly,but need to be computed usingnumerical differentiationand integration,respectively.For simplicity,wehere ignore this approximation and consider $W , \phi$ , $\varLambda$ asgiven time-dependent functions.

Since $\eta$ and $W$ havebounded derivatives,the following averaged version of the implicit midpoint rule hasalocal errorof $\mathcal { O } ( h ^ { 2 } )$ uniformly in $\succeq$ :1

$$
\eta _ { n + 1 } = \eta _ { n } + \int _ { t _ { n } } ^ { t _ { n + 1 } } \exp \Bigl ( - \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) W ( t _ { n + 1 / 2 } ) \exp \Bigl ( \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) d s \ \frac { 1 } { 2 } ( \eta _ { n + 1 } + \eta _ { n } )
$$

The problem then remains to compute the oscillatory integral.The integrand can be rewritten as

$$
E ( \varPhi ( s ) ) \circ W ( t _ { n + 1 / 2 } ) ,
$$

where $\circ$ denotes the entrywise product of matrices and

$$
E ( \varPhi ) = \left( e _ { j k } \right) \quad \mathrm { ~ w i t h ~ } \quad e _ { j k } = \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } - \phi _ { k } \bigr ) \Bigr ) .
$$

With a linear phase approximation (of an error $\mathcal { O } ( h ^ { 2 } )$ ）

$$
\Phi ( t _ { n + 1 / 2 } + \theta h ) \approx \varPhi ( t _ { n + 1 / 2 } ) + \theta h A ( t _ { n + 1 / 2 } ) ,
$$

theintegral is approximated by

$$
h E ( \varPhi ( t _ { n + 1 / 2 } ) ) \bullet \varPsi ( t _ { n + 1 / 2 } ) \bullet W ( t _ { n + 1 / 2 } )
$$

where $\boldsymbol { \mathcal { T } } ( t )$ isthematrix of integrated exponentialswith entries (we omit the argument $t$ ）

$$
\mathcal { T } _ { j k } = \int _ { - 1 / 2 } ^ { 1 / 2 } \exp \Bigl ( - \frac { i \theta h } { \varepsilon } ( \lambda _ { j } - \lambda _ { k } ) \Bigr ) d \theta = \mathrm { s i n c } \Bigl ( \frac { h } { 2 \varepsilon } ( \lambda _ { j } - \lambda _ { k } ) \Bigr ) .
$$

Theerror in the integral approximation comes solely from the linearphase approximationand is bounded by $\begin{array} { r } { \mathcal { O } \big ( h \cdot \frac { h ^ { 2 } } { \varepsilon } \cdot \frac { \varepsilon } { h } \big ) = \mathcal { O } ( h ^ { 2 } ) } \end{array}$ if the $\lambda _ { j }$ areseparated,because then the integral ${ \mathcal { I } } _ { j k }$ is of size $\begin{array} { r } { { \mathcal { O } } \left( \frac { \varepsilon } { h } \right) . } \end{array}$ Wethus obtain the followingaveraged implicit midpointrulewitha local errorof $\mathcal { O } ( h ^ { 2 } )$ uniformlyin $\boldsymbol { \varepsilon }$ :

$$
\begin{array} { r } { \eta _ { n + 1 } = \eta _ { n } + h \Big ( E ( \hat { \Phi } ( t _ { n + 1 / 2 } ) ) \bullet \mathcal { Z } ( t _ { n + 1 / 2 } ) \bullet W ( t _ { n + 1 / 2 } ) \Big ) \frac { 1 } { 2 } ( \eta _ { n + 1 } + \eta _ { n } ) . } \end{array}
$$

Ananalogue of the explicit midpoint rule is similarly constructed,and from the Magnus series (IV.7.5)of the solution we obtain the following averaged exponential midpoint rule,againwith an $\mathcal { O } ( h ^ { 2 } )$ local error uniformly in $\boldsymbol { \mathsf { E } }$ ：

$$
\eta _ { n + 1 } = \exp \left( { \hat { h } E ( \varPhi ( t _ { n + 1 / 2 } ) ) \bullet \varPsi ( t _ { n + 1 / 2 } ) \bullet W ( t _ { n + 1 / 2 } ) } \right) \eta _ { n } .
$$

Forskew-hermitian $W ( t )$ ,alsothematrix in(1.12）and(1.13）isskew-hermitian, and hence both of the above integrators preserve the Euclidean norm of $\eta$ exactly. Wesummarize the local error bounds for these methodsunder conditions that include the case of an avoided crossing of eigenvalues.

Theorem1.2 (Local Error).Suppose that for $t _ { 0 } \leq t \leq t _ { 0 } + h$ andall $j , k ,$

$$
| \lambda _ { j } ( t ) - \lambda _ { k } ( t ) | \geq \delta , \quad | \dot { \lambda } _ { j } ( t ) | \leq C _ { 0 } , \quad | \| W ( t ) \| \leq \frac { C _ { 1 } } { \delta } , \quad \| \dot { W } ( t ) \| \leq \frac { C _ { 2 } } { \delta ^ { 2 } }
$$

with $\delta > 0$ .Then,the localerrorofmethods(1.12)and(1.13)isboundedby

$$
\| \eta _ { 1 } - \eta ( t _ { 0 } + h ) \| \le C \frac { h ^ { 2 } } { \delta ^ { 2 } } \| \eta _ { 0 } \| .
$$

Theconstant $C$ is independent of $h , \varepsilon , \delta$ .

ProofThe result is obtained with the arguments and approximation estimates given above,taking in addition account of the dependence on $\delta$ . □

The local error contains smooth,non-oscillatory components which accumulate toaglobal error $\eta _ { n } - \eta ( t _ { n } ) = \mathcal { O } ( h )$ onbounded intervals if the eigenvaluesremain well separated.Using that in this case $\eta$ isconstant up to $\mathcal { O } ( \varepsilon )$ ,thiserrorbound can be improved to $\mathcal { O } ( \operatorname* { m i n } \{ \varepsilon , h \} )$ The integrators thus do not resolve the $\mathcal { O } ( \varepsilon )$ oscillations in $\eta$ forlarge step sizes $h \geq \varepsilon$ ,butlikeinJahnke&Lubich（2003）

theycan be combined with a(symmetric and scaling-invariant) adaptive step size strategy such that themethods followthe non-adiabatic transitions through avoided crossings of eigenvalueswith small stepsand take large steps elsewhere.

Wehereconsiderapplyingan integrating reversible step size controleras in Sect.VII.3.2 with the step size density function

$$
\sigma ( t ) = \left( \| W ( t ) \| ^ { 2 } + \alpha ^ { 2 } \right) ^ { - 1 / 2 }
$$

for a parameter $\alpha$ that can be interpreted as the ratio of theaccuracy parameter andthe maximum admissible step size.Choosing the Frobenius norm $\| W \| =$ (trace $W ^ { T } W ) ^ { 1 / 2 }$ ,wethen obtain the following version of Algorithm VIII.3.4, where $\mu$ istheaccuracyparameterand

$$
G ( t ) = - \frac { \dot { \sigma } ( t ) } { \sigma ( t ) } = \left( \| W ( t ) \| ^ { 2 } + \alpha ^ { 2 } \right) ^ { - 1 } \operatorname { t r a c e } \left( \dot { W } ( t ) ^ { T } W ( t ) \right) .
$$

Set $z _ { 0 } = 1 / \sigma ( t _ { 0 } )$ and,for $n \geq 0$

$$
\begin{array} { r c l } { { z _ { n + 1 / 2 } } } & { { = } } & { { z _ { n } + { \displaystyle \frac { \mu } { 2 } } G ( t _ { n } ) } } \\ { { h _ { n + 1 / 2 } } } & { { = } } & { { \displaystyle \mu / z _ { n + 1 / 2 } } } \\ { { t _ { n + 1 } } } & { { = } } & { { t _ { n } + h _ { n + 1 / 2 } } } \\ { { \eta _ { n } } } & { { \mapsto } } & { { \displaystyle \eta _ { n + 1 } ~ \mathrm { ~ b y ~ } ( 1 . 1 2 ) ~ \mathrm { o r ~ } ( 1 . 1 3 ) ~ \mathrm { w i t h ~ s t e p ~ s i z e ~ } h _ { n + 1 / 2 } } } \\ { { z _ { n + 1 } } } & { { = } } & { { \displaystyle z _ { n + 1 / 2 } + { \displaystyle \frac { \mu } { 2 } } G ( t _ { n + 1 } ) . } } \end{array}
$$

Weremark that the schemes(1.12)and(1.13)can be modified such that they use evaluations at $t _ { n }$ and $t _ { n + 1 }$ instead of $t _ { n + 1 / 2 }$ (Exercise 6).

Applying the above algorithmwith accuracy parameter $\mu = 0 . 0 1$ and $\alpha = 0 . 1$ totheproblemofFig.1.1with $\varepsilon = 0 . 0 1$ and $\delta = 2 ^ { - 1 } , 2 ^ { - 3 } , 2 ^ { - 5 } , 2 ^ { - 7 }$ yields the step size sequences shown in Fig.1.2.In each case the error at the end-point $t = 1$ was between $0 . 5 \cdot 1 0 ^ { - 3 }$ and $2 \cdot 1 0 ^ { - 3 }$ .

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0008_pages_0491-0560/auto/images/43b8f4c3a712a0c19f91a7dc78dcbe3e9172acc0c8238c5d358baea084272663.jpg)  
Fig.1.2.Non-adiabatic transition:step sizes as function of $t$ for $\varepsilon ~ = ~ 0 . 0 1$ and $\delta \ =$ $2 ^ { - 1 } , 2 ^ { - 3 } , 2 ^ { - 5 } , 2 ^ { - 7 }$ (increasingdarkness）

Second-Order Integrators.The $\mathcal { O } ( \varepsilon )$ oscillations in $\eta$ areresolved with step sizes upto $h \ = \ O ( { \sqrt { \varepsilon } } )$ for methods that give $\mathcal { O } ( h ^ { 2 } )$ accuracy uniformlyin $\varepsilon$ Such methods requirea quadraticphase approximation,and one needs further terms obtained from reinserting $\eta ( s )$ under theintegral in（1.iO）onceagainbythesame formula,thus yielding termswith iterated integrals (this procedure is known as the Neumann or Peano or Dyson expansion in different communities,cf.Iserles 2004), orbyincludingthe first commutatorin the Magnus expansion (IV.7.5).Symmetric second-order methods of both typesare constructed by Jahnke (2004a).

Caremust be taken in computing the arising oscillatory integrals.Iserles (2004) proposesand analysesFilon quadrature (after Filon,1928),whichisapplicable whenthemoments,i.e.,the integrals overproducts of oscillatory exponentials andpolynomials,areknownanalytically.Thisis not thecase,however,for all of theintegrals appearing in the second-order methods.The alternative chosen by Jahnke(2oo4a) is to use an expansion technique based on partial integration.The ideacan beillustrated on an integral suchas

$$
\int _ { 0 } ^ { 1 } \exp \Bigl ( \frac { i \alpha \theta h } { \varepsilon } \Bigr ) \cdot \exp \Bigl ( \frac { i \beta \theta ^ { 2 } h ^ { 2 } } { \varepsilon } \Bigr ) d \theta
$$

with $\alpha \neq 0$ Partial integration that integratesthe firstfactoranddifferentiates the second factoryieldsa boundary termandagainanintegral ofthe sametype,but nowwithanadditionalfactor $\begin{array} { r } { \mathcal { O } \big ( \frac { \varepsilon } { h } \cdot \frac { h ^ { 2 } } { \varepsilon } \big ) = \mathcal { O } ( h ) } \end{array}$ Usingthistechniquerepeatedly intheoscillatory integrals appearingin the second-order methods permitstoapproximate all of themup to $\mathcal { O } ( h ^ { 3 } )$ asneeded.WerefertoJahnke(20o4a) forthe precise formulation and error analysis of these second-order methods,which are complicated to formulate,but do not require substantially more computational work than the first-ordermethods described above,and just the same number of matrix evaluations.

Higher-Order Integrators.Integrators of general order $p \geq 1$ are obtained with a phaseapproximation bypolynomialsofdegree $p$ andby includingall termsof the Neumann orMagnus expansion for（1.5）withup to $p$ -foldintegrals.

# XIV.2Mechanical Systemswith Time-Dependent Frequencies

Westudy oscillatory mechanical systems with explicitly time-dependent frequencies,where the time-dependentHamiltonianis

$$
H ( p , q , t ) = { \frac { 1 } { 2 } } p ^ { T } M ( t ) ^ { - 1 } p + { \frac { 1 } { 2 \varepsilon ^ { 2 } } } q ^ { T } A ( t ) q + U ( q , t )
$$

with apositive definitemass matrix $M ( t )$ andapositive semi-definite stiffness matrixA(t）ofconstant rankwhosederivativesare bounded independentlyof $\boldsymbol { \varepsilon }$ .Such aHamiltonian describes oscillations ina mechanical system that at the same time exertsa driven motion onaslower time scale.We considermotions of bounded energy:

$$
H ( p ( t ) , q ( t ) , t ) \leq \mathrm { C o n s t } .
$$

Wetransform (2.1) toamoreamenable form bya seriesof linear time-dependent canonical coordinate transforms.The transformations turn the equations of motion intoaform that approximately separates the time scales.This makes theproblem moreaccessible to numerical discretization with large time steps and to the error analysis of multiple time-steppingmethods applieddirectlyto(2.1)in theoriginally given coordinates.

# XIV.2.1 Canonical Transformationto Adiabatic Variables

Bya series of canonical time-dependent linear transformations,which can all be donenumericallywith standard linearalgebra routines,we now take the Hamiltonian system(2.1）toa form fromwhich adiabatic invariantscan beread off and which will serve as the base camp for both the construction and error analysis of numerical methods.

Weintroduce the energy $E$ as theconjugate variableto time $t$ and extend the Hamiltonian to

$$
\widehat { H } ( p , E , q , t ) = H ( p , q , t ) + E .
$$

The canonicalequations ofmotion are then (the gradient $\nabla$ refers only to $q$ ）

$$
\begin{array} { r c l } { \dot { p } } & { = } & { - \displaystyle \frac { 1 } { \varepsilon ^ { 2 } } A ( t ) q - \nabla U ( q , t ) } \\ { \dot { q } } & { = } & { { \cal M } ( t ) ^ { - 1 } p } \end{array}
$$

along with $\dot { E } = - \partial H / \partial t$ and $t = 1$

Transforming theMassMatrix into the Identity Matrix.We change variables such that the mass matrix $M ( t )$ inthe kineticenergy part is replaced bythe identity. Witha smooth factorization

$$
\boldsymbol { M } ( t ) ^ { - 1 } = \boldsymbol { C } ( t ) \boldsymbol { C } ( t ) ^ { T } ,
$$

e.g.,froma Cholesky decomposition of $M ( t )$ ,wetransformto variables $( \widetilde { q } , t )$ by

$$
q = C ( t ) \widetilde { q } , \quad t = \widetilde { t } .
$$

Then,theconjugate momenta are given by (see Example VI.5.2)

$$
\left( \begin{array} { l } { \medskip \widetilde { p } } \\ { \widetilde { E } } \end{array} \right) = \left( \begin{array} { l l } { \medskip C } & { \dot { C } \widetilde { q } } \\ { 0 } & { 1 } \end{array} \right) ^ { T } \left( \begin{array} { l } { \medskip p } \\ { E } \end{array} \right) = \left( \begin{array} { c } { \medskip C ^ { T } p } \\ { \widetilde { q } ^ { T } \dot { C } ^ { T } p + E } \end{array} \right) .
$$

With the transformed matrix $\begin{array} { r c l } { A } & { = } & { C ^ { T } A C } \end{array}$ ,the Hamiltonian ${ \cal H } ( \widetilde { p } , E , \widetilde { q } , \widetilde { t } ) \ =$ $\hat { H } ( p , E , q , t )$ in thenew variables then takes the form(we omitalltildes)

$$
{ \cal H } ( p , E , q , t ) = \frac { 1 } { 2 } p ^ { T } p + \frac { 1 } { 2 \varepsilon ^ { 2 } } q ^ { T } { \cal A } ( t ) q - q ^ { T } \dot { C } ( t ) ^ { T } C ( t ) ^ { - T } p + U ( C ( t ) q , t ) + { \cal B } ( t ) \dot { C } ( t ) \dot { C } ( t ) ,
$$

Diagonalizing the Stiffness Matrix.We diagonalize the matrix $A ( t )$ in (2.5）,

$$
A ( t ) = Q ( t ) \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { \varOmega ( t ) ^ { 2 } } } \end{array} \right) Q ( t ) ^ { T }
$$

with the diagonal matrix $\Omega ( t ) = \mathrm { d i a g } ( \omega _ { j } ( t ) )$ of frequencies and an orthogonal matrix $Q ( t )$ ,which depends smoothlyon $t$ ifthe frequencies remain separated.The matrix $Q ( t )$ can be obtained as the product

$$
Q ( t ) = Q _ { 0 } ( t ) \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { Q _ { * } ( t ) } } \end{array} \right) ,
$$

where the transformation with $Q _ { 0 } ( t )$ takes $A ( t )$ to the block-diagonal form

$$
A ( t ) = Q _ { 0 } ( t ) \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { A _ { * } ( t ) } } \end{array} \right) Q _ { 0 } ( t ) ^ { T }
$$

and $Q _ { * } ( t )$ diagonalizes $A _ { * } ( t )$ Theeffect of an avoided crossing of frequencies is localized to $Q _ { * } ( t )$ ,which then can have large derivatives,whereas those of $Q _ { 0 } ( t )$ remainmoderatelybounded.The transformation

$$
q = Q ( t ) { \widehat { q } } , \quad t = { \widehat { t } }
$$

with the conjugate momenta

$$
\widehat { \boldsymbol { p } } = \boldsymbol { Q } ( t ) ^ { T } \boldsymbol { p } , \quad \widehat { \boldsymbol { E } } = \widehat { \boldsymbol { q } } ^ { T } \dot { \boldsymbol { Q } } ( t ) ^ { T } \boldsymbol { p } + \boldsymbol { E }
$$

yields the Hamiltonian in thenew variables $( \widehat { p } , \widehat { E } , \widehat { q } , \widehat { t } )$ as (we omit all hats)

$$
H = \frac { 1 } { 2 } { p ^ { T } } p + \frac { 1 } { 2 { \varepsilon } ^ { 2 } } { q ^ { T } } \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { \varOmega ( t ) ^ { 2 } } \end{array} \right) q + { q ^ { T } } K ( t ) { p } + U ( C ( t ) Q ( t ) { q } , t ) + E
$$

with

$$
K = { \binom { K _ { 0 0 } } { K _ { 1 0 } } } K _ { 0 1 } \Big ) = Q ^ { T } \dot { Q } - Q ^ { T } \dot { C } ^ { T } C ^ { - T } Q .
$$

We decompose also

$$
\begin{array} { r } { p = \binom { p _ { 0 } } { p _ { 1 } } , \quad q = \binom { q _ { 0 } } { q _ { 1 } } } \end{array}
$$

according to the blocks in(2.6) and refer to $q _ { 0 }$ and $q _ { 1 }$ （ $p _ { 0 }$ and $p _ { 1 }$ astheslowand fast positions (slow and fast momenta),respectively.With the energy bound (2.2) wehave

$$
p _ { 1 } = \mathcal { O } ( 1 ) , \quad q _ { 1 } = \mathcal { O } ( \varepsilon ) .
$$


<!-- chunk 0009: pages 561-630 -->
Rescaling Positions and Momenta.We transform

$$
q _ { 0 } = \check { q } _ { 0 } , \quad q _ { 1 } = \varepsilon ^ { 1 / 2 } \varOmega ^ { - 1 / 2 } \check { q } _ { 1 } , \quad t = \check { t }
$$

with the conjugate momenta

$$
\check { p } _ { 0 } = p _ { 0 } , \quad \check { p } _ { 1 } = \varepsilon ^ { 1 / 2 } \Omega ^ { - 1 / 2 } p _ { 1 } , \quad \check { E } = - \frac { 1 } { 2 } \check { q } _ { 1 } ^ { T } \varepsilon ^ { 1 / 2 } \Omega ^ { - 3 / 2 } \dot { \Omega } p _ { 1 } + E .
$$

In the new variables,the Hamiltonian becomes (we omit the haceks on all variables)

$$
\begin{array} { l l l } { H } & { = } & { \displaystyle \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( t ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( t ) q _ { 1 } } \\ & {  } & {  + q ^ { T } \check { K } ( t ) p + U ( T ( t ) q , t ) + E } \end{array}
$$

with

$$
\begin{array} { r c l } { { \check { K } } } & { { = } } & { { \left( \begin{array} { c c } { { K _ { 0 0 } } } & { { \varepsilon ^ { - 1 / 2 } K _ { 0 1 } \varOmega ^ { 1 / 2 } } } \\ { { \varepsilon ^ { 1 / 2 } \varOmega ^ { - 1 / 2 } K _ { 1 0 } } } & { { \varOmega ^ { - 1 / 2 } K _ { 1 1 } \varOmega ^ { 1 / 2 } + \frac { 1 } { 2 } \varOmega ^ { - 1 } \dot { \varOmega } } } \end{array} \right) } } \\ { { \cal T } } & { { = } } & { { \left( T _ { 0 } \mid \varepsilon ^ { 1 / 2 } T _ { 1 } \right) = \left( \begin{array} { c c } { { T _ { 0 0 } } } & { { \varepsilon ^ { 1 / 2 } T _ { 0 1 } } } \\ { { T _ { 1 0 } } } & { { \varepsilon ^ { 1 / 2 } T _ { 1 1 } } } \end{array} \right) = C Q \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { \varepsilon ^ { 1 / 2 } \varOmega ^ { - 1 / 2 } } } \end{array} \right) . } } \end{array}
$$

Eliminating theSingular Block.Wenextremove the $\mathcal { O } ( \varepsilon ^ { - 1 / 2 } )$ off-diagonal block in $\dot { K }$ bythecanonical transformation

$$
- p _ { 1 } = - \overline { { p } } _ { 1 } + \varepsilon ^ { 1 / 2 } \Omega ^ { - 1 / 2 } K _ { 0 1 } ^ { T } q _ { 0 } , \quad q _ { 0 } = \overline { { q } } _ { 0 } , \quad t = \bar { t }
$$

with the conjugate variables

$$
\tilde { \tau } _ { 1 } = q _ { 1 } , \quad \overline { { { p } } } _ { 0 } = p _ { 0 } + \varepsilon ^ { 1 / 2 } K _ { 0 1 } \Omega ^ { - 1 / 2 } q _ { 1 } , \quad \overline { { { E } } } = E + \varepsilon ^ { 1 / 2 } q _ { 0 } ^ { T } \frac { d } { d t } \big ( K _ { 0 1 } \Omega ^ { - 1 / 2 } \big ) q _ { 1 }
$$

Inthese coordinates,theHamiltonian takes the form (we omit all bars)

$$
\begin{array} { r c l } { H } & { = } & { \displaystyle \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( t ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( t ) q _ { 1 } } \\ & & { \displaystyle + q ^ { T } L ( t ) p + \frac { 1 } { 2 } q ^ { T } S ( t ) q + U ( T ( t ) q , t ) + E } \end{array}
$$

with the lower block-triangular matrix

$$
\begin{array} { l c l } { { { \cal L } } } & { { = } } & { { \left( \begin{array} { c c } { { L _ { 0 0 } } } & { { 0 } } \\ { { \varepsilon ^ { 1 / 2 } L _ { 1 0 } } } & { { L _ { 1 1 } } } \end{array} \right) } } \\ { { } } & { { = } } & { { \left( \begin{array} { c c } { { K _ { 0 0 } } } & { { 0 } } \\ { { \varepsilon ^ { 1 / 2 } \Omega ^ { - 1 / 2 } ( K _ { 1 0 } + K _ { 0 1 } ^ { T } ) } } & { { \varOmega ^ { - 1 / 2 } K _ { 1 1 } \varOmega ^ { 1 / 2 } + \frac { 1 } { 2 } \varOmega ^ { - 1 } \ddot { \varOmega } } } \end{array} \right) } } \end{array}
$$

and the symmetric matrix

$$
S = \left( \begin{array} { c c } { { \ S _ { 0 0 } } } & { { \varepsilon ^ { 1 / 2 } S _ { 0 1 } } } \\ { { \varepsilon ^ { 1 / 2 } S _ { 1 0 } } } & { { \varepsilon S _ { 1 1 } } } \end{array} \right) ,
$$

where

$$
\begin{array} { l } { { S _ { 0 0 } = - K _ { 0 1 } K _ { 0 1 } ^ { T } , } } \\ { { S _ { 0 1 } = S _ { 1 0 } ^ { T } = - K _ { 0 0 } K _ { 0 1 } \Omega ^ { - 1 / 2 } } } \\ { { \phantom { S _ { 0 0 } = - K _ { 0 1 } \Omega ^ { - 1 / 2 } ( \Omega ^ { 1 / 2 } K _ { 1 1 } ^ { T } \Omega ^ { - 1 / 2 } + \frac { 1 } { 2 } \Omega ^ { - 1 } \dot { \Omega } ) - \frac { d } { d t } \big ( K _ { 0 1 } \Omega ^ { - 1 / 2 } \big ) , } } } \\ { { S _ { 1 1 } = \Omega ^ { - 1 / 2 } ( - K _ { 1 0 } K _ { 0 1 } = K _ { 0 1 } ^ { T } K _ { 1 0 } ^ { T } + K _ { 0 1 } ^ { T } K _ { 0 1 } ) \Omega ^ { - 1 / 2 } , } } \end{array}
$$

Wenote that with the energy bound(2.2）we now have

$$
p _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } ) , \quad q _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } ) .
$$

Equations of Motion.Thedifferential equationsnow take the form

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { f _ { 0 } ( p , q , t ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + g _ { 0 } ( q , t ) } \\ { \left( \frac { \dot { p } _ { 1 } } { \dot { q } _ { 1 } } \right) } & { = } & { \frac { 1 } { \varepsilon } \left( \begin{array} { c c } { 0 } & { - \varOmega ( t ) } \\ { \varOmega ( t ) } & { 0 } \end{array} \right) \left( \frac { p _ { 1 } } { q _ { 1 } } \right) + \left( \begin{array} { c c } { \dot { f } _ { 1 } ( p , q , t ) } \\ { g _ { 1 } ( q , t ) } \end{array} \right) } \end{array}
$$

with the functions bounded uniformly in $\succ$ ，

$$
\binom { f _ { 0 } } { f _ { 1 } } = - L ( t ) p - \bar { S } ( t ) q - T ( t ) ^ { T } \nabla U ( T ( t ) q , t ) , \quad \binom { g _ { 0 } } { g _ { 1 } } = L ( t ) ^ { T } q .
$$

Thematrix in thesystem is diagonalized byaconstant unitary matrix:with

$$
{ \it \Delta } { \it \Gamma } = \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c } { { I } } & { { I } } \\ { { - i I } } & { { i I } } \end{array} \right)
$$

wehave

$$
\left( \begin{array} { c c } { { 0 } } & { { - \Omega ( t ) } } \\ { { \Omega ( t ) } } & { { 0 } } \end{array} \right) = { \cal T } \left( \begin{array} { c c } { { i \Omega ( t ) } } & { { \cdot \quad 0 } } \\ { { 0 } } & { { - i \Omega ( t ) } } \end{array} \right) { \cal T } ^ { * } .
$$

Remark.Action-angle variables $p _ { 1 , j } = \sqrt { a _ { j } } \cos \theta _ { j }$ ${ q _ { 1 , j } = \sqrt { a _ { j } } \sin \theta _ { j } }$ for the harmonic oscillators would now put the Hamiltonianinto theform $H = \textstyle { \frac { 1 } { \varepsilon } } \omega ( t ) \cdot a +$ $G ( a , \theta , p _ { 0 } , q _ { 0 } , t )$ ,which could be studied further using averaging techniques,that is, using coordinate transforms that reduce the dependence on the angles in the Hamiltonian;see Neishtadt (1984) for averaging out up to an exponentially small remainderinthe case ofa single high frequency.The first-order averaging transformmight bedone numerically (cf.the formulasin Sect.XII.2),but the higher-order transformsinvolve increasingly higherderivatives of the functions involved and thereforebecome impractical from the numerical viewpoint.For systemswith several frequencies the averaging transforms require multi-dimensional integrals which are expensive to compute.For our numerical purposes we therefore continue diferently, adaptingthe adiabatic transformation of Sect.XIV.1.1.

TheSystemin Adiabatic Variables.Let thediagonal phase matrix be givenas

$$
\varPhi ( t ) = \int _ { t _ { 0 } } ^ { t } A ( s ) d s \quad \mathrm { ~ w i t h ~ } A ( t ) = \left( \begin{array} { c c } { \varOmega ( t ) } & { 0 } \\ { 0 } & { - \varOmega ( t ) } \end{array} \right) .
$$

Ourfinal transformation follows (1.4) and sets

$$
\eta = \varepsilon ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi ( t ) \right) \varGamma ^ { \ast } \left( \begin{array} { c } { p _ { 1 } } \\ { q _ { 1 } } \end{array} \right) .
$$

The factor $\varepsilon ^ { - 1 / 2 }$ is chosen forconvenience sothat (2.12)implies

$$
\eta = \mathcal { O } ( 1 ) .
$$

Weremark thatup to nowalltransformationswere invariant underrescaling $\varepsilon \longrightarrow \sigma \varepsilon$ and $A ( t ) \longrightarrow \sigma ^ { 2 } A ( t )$ ,buthere we havechosen to giveup this invariance in favourof (2.17).Note that $\eta$ is of the form

$$
\eta = \varepsilon ^ { - 1 / 2 } { \cal T } ^ { * } \left( { \pi \atop \rho } \right) = { \frac { \varepsilon ^ { - 1 / 2 } } { \sqrt { 2 } } } \left( { \pi + i \rho \atop \pi - i \rho } \right)
$$

with real vectors $\pi , \rho$ satisfying

$$
\pi + i \rho = \exp \Bigl ( - \frac { i } { \varepsilon } \int _ { t _ { 0 } } ^ { t } \varOmega ( s ) d s \Bigr ) ( p _ { 1 } + i q _ { 1 } ) .
$$

Wedenote the inverse transformas

$$
\left( { \begin{array} { c } { p _ { 1 } } \\ { q _ { 1 } } \end{array} } \right) = \varepsilon ^ { 1 / 2 } \left( { \begin{array} { c } { P _ { 1 } ( t ) } \\ { Q _ { 1 } ( t ) } \end{array} } \right) \eta \quad { \mathrm { ~ w i t h ~ } } \quad \left( { \begin{array} { c } { P _ { 1 } ( t ) } \\ { Q _ { 1 } ( t ) } \end{array} } \right) = T \exp \left( { \frac { i } { \varepsilon } } \varPhi ( t ) \right) .
$$

Together with $\begin{array} { r } { e = E + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( t ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( t ) q _ { 1 } } \end{array}$ and unaltered $p _ { 0 } , q _ { 0 } , t$ thisyields a canonical transformation $( p _ { 0 } , \pi , e , q _ { 0 } , \rho , t ) \mapsto ( p _ { 0 } , p _ { 1 } , E , q _ { 0 } , q _ { 1 } , t )$ TheHamiltonianreads in these variables

$$
\begin{array} { r } { H = \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + q ^ { T } L ( t ) p + \frac { 1 } { 2 } q ^ { T } S ( t ) q + U ( T ( t ) q , t ) + e , } \end{array}
$$

where on the right-hand side the components $p _ { 1 } , q _ { 1 }$ are expressed in terms of $\eta$ and $\pi , \rho$ by(2.20) and(2.18).The equations of motion now become

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { f _ { 0 } ( p , q , t ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + g _ { 0 } ( q , t ) } \\ { \dot { \eta } } & { = } & { \varepsilon ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi ( t ) \right) T ^ { * } \left( \begin{array} { c } { f _ { 1 } ( p , q , t ) } \\ { g _ { 1 } ( q , t ) } \end{array} \right) } \end{array}
$$

with $p _ { 1 } , q _ { 1 }$ expressed in terms of $\eta$ by(2.20).Written out,the differential equations for $p _ { 0 } , q _ { 0 }$ read

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { - L _ { 0 0 } p _ { 0 } - S _ { 0 0 } q _ { 0 } - T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } , t ) - \varepsilon S _ { 0 1 } Q _ { 1 } \eta } \\ & & { - T _ { 0 } ^ { T } \Big ( \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) - \nabla U ( T _ { 0 } q _ { 0 } , t ) \Big ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + L _ { 0 0 } ^ { T } q _ { 0 } + \varepsilon L _ { 1 0 } ^ { T } Q _ { 1 } \eta . } \end{array}
$$

Thematrix multiplying $\eta$ aftersubstituting the expressions $f _ { 1 }$ and $g _ { 1 }$ in the differential equation for $\eta$ becomes,apart from the oscillatory exponentials,

$$
\begin{array} { r c l } { W } & { = } & { { \cal { T } } ^ { * } \left( \begin{array} { c c } { - { \cal { L } } _ { 1 1 } } & { - \varepsilon { \cal { S } } _ { 1 1 } } \\ { 0 } & { { \cal { L } } _ { 1 1 } ^ { T } } \end{array} \right) { \cal { T } } ^ { } \quad - } \\ & { = } & { - { \frac { 1 } { 2 } } \left( \begin{array} { c c } { { \cal { L } } _ { 1 1 } - { \cal { L } } _ { 1 1 } ^ { T } } & { { \cal { L } } _ { 1 1 } + { \cal { L } } _ { 1 1 } ^ { T } } \\ { { \cal { L } } _ { 1 1 } + { \cal { L } } _ { 1 1 } ^ { T } } & { { \cal { L } } _ { 1 1 } - { \cal { L } } _ { 1 1 } ^ { T } } \end{array} \right) - { \frac { i \varepsilon } { 2 } } \left( \begin{array} { c c } { - { \cal { S } } _ { 1 1 } } & { { \cal { S } } _ { 1 1 } } \\ { - { \cal { S } } _ { 1 1 } } & { { \cal { S } } _ { 1 1 } } \end{array} \right) , } \end{array}
$$

which has adiagonal of size ${ \mathcal { O } } ( \varepsilon ) .$ The equation for $\eta$ then reads

$$
\begin{array} { r l } & { \dot { \eta } ~ = ~ \mathrm { e x p } \left( - \frac { i } { \varepsilon } \Phi ( t ) \right) W ( t ) \mathrm { e x p } \left( \frac { i } { \varepsilon } \Phi ( t ) \right) \eta } \\ & { \qquad = P _ { 1 } ^ { \ast } \left( L _ { 1 0 } p _ { 0 } + S _ { 1 0 } \bar { q } _ { 0 } + T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) \right) . } \end{array}
$$

Thematrix multiplying $\eta$ isbounded independentlyof $\varepsilon$ ,but highly oscillatory.Note that thecoordinate transforms leadingto(2.21),(2.23)are linearand can becarried outby standard numerical linearalgebra routines.

Adiabatic Invariants.We suppose that the eigenfrequencies $\omega _ { j } ( t )$ remain separated andbounded away from O:there are $\delta > 0$ and $c > 0$ such that for any pair $\omega _ { j } ( t )$ and $\omega _ { k } ( t )$ with $j \neq k ( j , k = 1 , \ldots , m )$ ,the lower bounds

$$
| \omega _ { j } ( t ) - \omega _ { k } ( t ) | \geq \delta , \quad \ \omega _ { j } ( t ) \geq c
$$

hold for all $t$ underconsideration.Under condition (2.24） the right-hand side $r ( t )$ inthedifferential equation for $\eta$ consists only of oscillatory terms,up to $\mathcal { O } ( \varepsilon )$ (No smooth terms larger than $\mathcal { O } ( \varepsilon )$ arise because the matrix $W$ hasa diagonal of size $\mathcal { O } ( \varepsilon )$ ）Itthen followsbypartial integration that

$$
\int _ { 0 } ^ { t } r ( s ) d s = \mathcal { O } ( \bar { \varepsilon } ) ~ \mathrm { f o r } ~ t \leq \mathrm { C o n s t . } ,
$$

andasin（1.6）we then obtain

$$
\eta ( t ) = \eta ( 0 ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

The functions defined by

$$
I _ { j } = | \eta _ { j } | ^ { 2 } \qquad ( j = 1 , \ldots , m )
$$

are thusadiabatic invariants:

$$
I _ { j } ( t ) = I _ { j } ( 0 ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

Starting fromaHamiltonian system (2.1),where the mass matrix equals the identity andthestifnessmatrixislreadyagonalwefindtat $I _ { j }$ is the action (energy divided by frequency)

$$
I _ { j } ( t ) = \frac { 1 } { \omega _ { j } ( t ) } \left( \frac { 1 } { 2 } p _ { j } ( t ) ^ { 2 } + \frac { \omega _ { j } ( t ) ^ { 2 } } { 2 \varepsilon ^ { 2 } } q _ { j } ( t ) ^ { 2 } \right) ,
$$

which fora constant frequency $\omega _ { j }$ becomes aconstant multiple of the oscillatory energyconsidered in Sect.XIII.9.

The Slow Limit System.As $\varepsilon  0$ ,the evolution of the slow variables $p _ { 0 } , q _ { 0 }$ is governed by the equations

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { - L _ { 0 0 } ( t ) p _ { 0 } - S _ { 0 0 } ( t ) q _ { 0 } - T _ { 0 } ( t ) ^ { T } \nabla U ( T _ { 0 } ( t ) q _ { 0 } , t ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + L _ { 0 0 } ( t ) ^ { T } q _ { 0 } } \end{array}
$$

which is the system with the time-dependent Hamiltonian

$$
H _ { 0 } ( p _ { 0 } , q _ { 0 } , t ) = \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + q _ { 0 } ^ { T } L _ { 0 0 } ( t ) p _ { 0 } + \frac { 1 } { 2 } q _ { 0 } ^ { T } S _ { 0 0 } ( t ) q _ { 0 } + U ( T _ { 0 } ( t ) q _ { 0 } , t ) .
$$

Weconclude this subsection with a simple illustration of the above procedure.

Example2.1 (Harmonic oscillator with slowly varying frequency).For the scalar second-orderdifferential equation

$$
\ddot { q } + \frac { \omega ( t ) ^ { 2 } } { \varepsilon ^ { 2 } } q = 0 ,
$$

where $\omega ( t )$ isboundedaway fromOand hasaderivative bounded independently of $\boldsymbol { \mathsf { E } }$ ,theabove transformations simplify considerably.TheHamiltonian in the original variables isalready of the form

$$
H = \frac { 1 } { 2 } p ^ { 2 } + \frac { 1 } { 2 } \frac { \omega ( t ) ^ { 2 } } { \varepsilon ^ { 2 } } q ^ { 2 } ,
$$

and hencethe first two transformations are not needed at all,and there are no slow variables $p _ { 0 } , q _ { 0 }$ .Therescaling transformation yieldstheHamiltonian(2.1O)in the form

$$
H = \frac { \omega ( t ) } { 2 \varepsilon } \check { p } ^ { 2 } + \frac { \omega ( t ) } { 2 \varepsilon } \check { q } ^ { 2 } + \frac { 1 } { 2 } \frac { \ddot { \omega } ( t ) } { \omega ( t ) } \check { p } \check { q } .
$$

With the adiabatic transformation (2.19）we thus represent the solution as

$$
\sqrt { \frac { \varepsilon } { \omega ( t ) } } \dot { q } ( t ) + i \sqrt { \frac { \omega ( t ) } { \varepsilon } } q ( t ) = \exp \Bigl ( \frac { i } { \varepsilon } \int _ { t _ { 0 } } ^ { t } \omega ( s ) d s \Bigr ) \zeta ( t ) ,
$$

where $\zeta = \pi + i \rho$ solves the differential equation

$$
\dot { \zeta } ( t ) = - \frac { 1 } { 2 } \frac { \dot { \omega } ( t ) } { \omega ( t ) } \exp \Bigl ( - \frac { 2 i } { \varepsilon } \int _ { t _ { 0 } } ^ { t } \omega ( s ) d s \Bigr ) \zeta ( t )
$$

and satisfies $\zeta ( t ) = \zeta ( t _ { 0 } ) { \bigl ( } 1 + { \mathcal { O } } ( \varepsilon ) { \bigr ) }$ for $t = \mathcal { O } ( 1 ) .$ (In theabove notation,we have n=e-1/（））Thectin

$$
I ( t ) = \frac { 1 } { \omega ( t ) } \left( \frac { 1 } { 2 } { \dot { q } } ( t ) ^ { 2 } + \frac { \omega ( t ) ^ { 2 } } { 2 \varepsilon ^ { 2 } } q ( t ) ^ { 2 } \right)
$$

isanadiabatic invariant.

# XIV.2.2Adiabatic Integrators

Asimple long-time-step integrator for the oscillatory mechanical system with timedependent Hamiltonian(2.1） nowreadsas follows:

-Solve the slow limit system(2.29) for $p _ { 0 } , q _ { 0 }$ ,e.g.,bytheStormer-Verlet method.   
-Keep the adiabatic variable $\eta$ constant at its initial value.

Underthecondition of bounded energy (2.1) and the frequency separation condition (2.24）,the error in $\eta$ isthen $\mathcal { O } ( \varepsilon )$ overintervals $t \leq$ Const.by(2.26).The difference between the solutions of(2.21）and the limit equation (2.29)is bounded by $O ( \varepsilon ^ { 2 } )$ for $t \leq \mathrm { C o n s t . }$ ,ascan be shown by forming the difference of the equations,integrating,estimating the integral of the extra terms by $\mathcal { O } ( \varepsilon ^ { 2 } )$ using（2.26）and partial integration,and applying the Gronwall inequality.In the original variables $p , q$ of (2.1) this yieldsan error $\mathcal { O } ( \varepsilon ^ { 2 } )$ in the positions and $\mathcal { O } ( \varepsilon )$ in the momenta.

Morerefined integratorsare needed for two independent reasons:

1. to keep control of $\eta$ on subintervals where the frequencies are not well separated andwhere $\eta$ may thusdeviate from its near-constant value; 2.to obtain higher order of approximation on intervals with separated frequencies.

Wesimplify the following presentation by assuming that the potential $U$ is quadratic:

$$
U ( q , t ) = \frac { 1 } { 2 } q ^ { T } G ( t ) q ,
$$

withasymmetric matrix $G ( t )$ depending smoothly on $t$ .We leave the required modifications for general $U$ to theinterested reader.Alternatively,themethodwith $U = 0$ canbe used in the splittingapproach of Sect.XIV.2.3below.

Anadiabatic integratoras described in Sect.XIV.1.2 can be extended to(2.23) and combined with a symmetric splittng between the weakly coupled systems (2.21)and(2.23):we beginwith a symplectic Euler half-step for $p _ { 0 } , q _ { 0 }$ (denoting the time levels by superscripts),

$$
\begin{array} { r c l } { { p _ { 0 } ^ { 1 / 2 } } } & { { = } } & { { p _ { 0 } ^ { 0 } - { \displaystyle \frac { h } { 2 } } \Bigl ( { \cal L } _ { 0 0 } p _ { 0 } ^ { 1 / 2 } + ( S _ { 0 0 } + T _ { 0 } ^ { T } G T _ { 0 } ) q _ { 0 } ^ { 0 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \qquad + \varepsilon \bigl ( S _ { 0 1 } + T _ { 0 } ^ { T } G T _ { 1 } \bigr ) Q _ { 1 } ^ { - } \eta ^ { 0 } \Bigr ) } } \\ { { } } & { { } } & { { } } \\ { { q _ { 0 } ^ { 1 / 2 } } } & { { = } } & { { q _ { 0 } ^ { 0 } + { \displaystyle \frac { h } { 2 } } \Bigl ( p _ { 0 } ^ { 1 / 2 } + { \cal L } _ { 0 0 } ^ { T } q _ { 0 } ^ { 0 } + \varepsilon { \cal L } _ { 1 0 } ^ { T } { \mathcal Q } _ { 1 } ^ { - } \eta ^ { 0 } \Bigr ) . } } \end{array}
$$

Here the matrix functions $L _ { 0 0 }$ , $L _ { 1 0 }$ ， $S _ { 0 0 }$ ， $S _ { 0 1 }$ ， $T _ { 0 }$ , $T _ { 1 }$ are evaluated at $t _ { 1 / 2 } = t _ { 0 } +$ $h / 2$ ,and $\mathcal { Q } _ { 1 } ^ { - }$ is theaverage of the oscillatory function $Q _ { 1 }$ of (2.20)over the halfstep,

$$
\mathcal { Q } _ { 1 } ^ { - } \approx \frac { 2 } { h } \int _ { t _ { 0 } } ^ { t _ { 1 } / 2 } Q _ { 1 } ( t ) d t ,
$$

obtained witha linear approximation of the phase $\varPhi ( t )$ and analytic computation of theintegral.We thenmakea fullstep for $\eta$ with Eq.(2.23) like in(1.12)，

$$
\begin{array} { r c l } { \eta ^ { 1 } } & { = } & { \eta ^ { 0 } + \hbar \Big ( E ( \phi ) \bullet \mathcal { Z } \bullet W \Big ) \frac { 1 } { 2 } ( \eta ^ { 1 } + \eta ^ { 0 } ) } \\ & & { \qquad - \hbar \mathcal { P } _ { 1 } ^ { * } \Big ( L _ { 1 0 } p _ { 0 } ^ { 1 / 2 } + ( S _ { 1 0 } + T _ { 1 } ^ { T } G T _ { 0 } ) q _ { 0 } ^ { 1 / 2 } \Big ) , } \end{array}
$$

where again all matrix functionsare evaluated at $t _ { 1 / 2 }$ ,and $\mathcal { P } _ { 1 }$ is the linear-phase approximation to the average

$$
\mathcal { P } _ { 1 } \approx \frac { 1 } { h } \int _ { t _ { 0 } } ^ { t _ { 1 } } P _ { 1 } ( t ) d t .
$$

Thematrix $W$ is as in (2.22),but with $S _ { 1 1 }$ replaced by $S _ { 1 1 } + T _ { 1 } ^ { T } G T _ { 1 } .$ The stepis completedbyahalf-step for $p _ { 0 } , q _ { 0 }$ with the adjoint symplectic Euler method:

$$
\begin{array} { r c l } { { p _ { 0 } ^ { 1 } } } & { { = } } & { { p _ { 0 } ^ { 1 / 2 } - \displaystyle \frac { h } { 2 } \Big ( { \cal L } _ { 0 0 } p _ { 0 } ^ { 1 / 2 } + ( { \cal S } _ { 0 0 } + T _ { 0 } ^ { T } { \cal G } T _ { 0 } ) q _ { 0 } ^ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \varepsilon \big ( { \cal S } _ { 0 1 } + T _ { 0 } ^ { T } { \cal G } T _ { 1 } \big ) { \cal Q } _ { 1 } ^ { + } \eta ^ { 1 } \Big ) } } \\ { { } } & { { } } & { { } } \\ { { q _ { 0 } ^ { 1 } } } & { { = } } & { { q _ { 0 } ^ { 1 / 2 } + \displaystyle \frac { h } { 2 } \Big ( p _ { 0 } ^ { 1 / 2 } + { \cal L } _ { 0 0 } ^ { T } q _ { 0 } ^ { 1 } + \varepsilon { \cal L } _ { 1 0 } ^ { T } { \cal Q } _ { 1 } ^ { + } \eta ^ { 1 } \Big ) , } } \end{array}
$$

where thematrix functions are still evaluated at $t _ { 1 / 2 }$ ,and $\mathcal { Q } _ { 1 } ^ { + }$ approximates the averageof $Q _ { 1 }$ over the second half-step.

We now give local error bounds for this integrator,under conditions that include thecase of an avoided crossing of frequencies.

Theorem2.2.Suppose that the functionsin(2.1） are smooth and the frequencies satisfy(2.24)withminimal distance $\delta > 0$ for $t _ { 0 } \le t \le t _ { 0 } + h$ andthe orthogonalmatrix $Q _ { * } ( t )$ of(2.7),which diagonalizesthe nonsingular part ofthe stiffness matrix,hasderivativesbounded by $\dot { Q } _ { * } ( t ) = \mathcal { O } ( \delta ^ { - 1 } )$ , $\ddot { Q } _ { * } ( t ) = \mathcal { O } ( \delta ^ { - 2 } )$ Assume furthertheenergybound(2.2)fortheinitialvalues.Then,the localerrorofmethod (2.30)-(2.32)is bounded by

$$
\begin{array} { r c l } { { p _ { 0 } ^ { 1 } - p _ { 0 } ( t _ { 0 } + h ) } } & { { = } } & { { \mathcal { O } ( h ^ { 3 } / \delta ^ { 2 } ) + \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ^ { 2 } ) } } \\ { { q _ { 0 } ^ { 1 } - q _ { 0 } ( t _ { 0 } + h ) } } & { { = } } & { { \mathcal { O } ( h ^ { 3 } / \delta ) + \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ^ { 2 } ) } } \\ { { \eta ^ { 1 } - \eta ( t _ { 0 } + h ) } } & { { = } } & { { \mathcal { O } ( h ^ { 2 } / \delta ^ { 2 } ) . } } \end{array}
$$

Theconstantssymbolizedby $\mathcal { O }$ do not depend on $\varepsilon$ ， $h ,$ and $\delta$

Proof.(a) Under the given conditions we have

$$
\begin{array} { r l } & { K _ { 0 0 } = \mathcal { O } ( 1 ) , K _ { 0 1 } = \mathcal { O } ( 1 ) , K _ { 1 0 } = \mathcal { O } ( 1 ) , K _ { 1 1 } = \mathcal { O } ( \delta ^ { - 1 } ) , \mathrm { a n d } } \\ & { } \\ & { \dot { K } _ { 0 0 } = \mathcal { O } ( 1 ) , \dot { K } _ { 0 1 } = \mathcal { O } ( \delta ^ { - 1 } ) , \dot { K } _ { 1 0 } = \mathcal { O } ( \delta ^ { - 1 } ) , \dot { K } _ { 1 1 } = \mathcal { O } ( \delta ^ { - 2 } ) } \end{array}
$$

This yields the bounds

$$
L _ { 0 0 } , L _ { 1 0 } , S _ { 0 0 } , S _ { 1 1 } = O ( 1 )
$$

and similarly for theirderivatives,and

$$
\begin{array} { r } { L _ { 1 1 } , S _ { 0 1 } , S _ { 1 0 } = \mathcal { O } ( \delta ^ { - 1 } ) , \quad \dot { L } _ { 1 1 } , \dot { S } _ { 0 1 } , \dot { S } _ { 1 0 } = \mathcal { O } ( \delta ^ { - 2 } ) , } \end{array}
$$

and hence also

$$
W = { \mathcal O } ( \delta ^ { - 1 } ) , \quad \dot { W } = { \mathcal O } ( \delta ^ { - 2 } ) .
$$

So we have from theenergy boundandthediferentialequation(2.23)for $\eta$

$$
\eta = \mathcal { O } ( 1 ) , \quad \dot { \eta } = \mathcal { O } ( \delta ^ { - 1 } ) .
$$

From thedifferential equations(2.21） for $p _ { 0 } , q _ { 0 }$ we conclude

$$
\ddot { p } _ { 0 } = \mathcal { O } ( \delta ^ { - 1 } ) + \mathcal { O } ( \varepsilon \delta ^ { - 2 } ) , \ddot { q } _ { 0 } = \mathcal { O } ( \varepsilon \delta ^ { - 1 } ) .
$$

(b)To study the local error in $\eta$ ,weintegrate（2.23）from $t _ { 0 }$ to $t _ { 0 } { + } h$ and compare with the corresponding term in(2.31）:

$$
\begin{array} { r l } & { \displaystyle \int _ { t _ { 0 } } ^ { t _ { 0 } + h } P _ { 1 } ^ { * } ( t ) \Big ( \bar { L } _ { 1 0 } p _ { 0 } + ( \bar { S } _ { 1 0 } + T _ { 1 } ^ { T } G T _ { 0 } ) q _ { 0 } \Big ) ( t ) d t } \\ & { \displaystyle - h \mathcal { P } _ { 1 } ^ { * } \Big ( \bar { L } _ { 1 0 } ( t _ { 1 / 2 } ) p _ { 0 } ^ { 1 / 2 } \neq ( S _ { 1 0 } + T _ { 1 } ^ { T } G T _ { 0 } ) ( t _ { 1 / 2 } ) q _ { 0 } ^ { 1 / 2 } \Big ) } \\ & { \displaystyle = \mathcal { O } ( h ^ { 2 } / \delta ^ { 2 } ) , } \end{array}
$$

where we have used the above bounds and the error estimate for the linear phase approximationin the average of $P _ { 1 } ( t )$ ,cf.Sect. XIV.1.2,

$$
\mathcal { P } _ { 1 } - \frac { 1 } { h } \int _ { t _ { 0 } } ^ { t _ { 1 } } P _ { 1 } ( t ) d t = \mathcal { O } ( h / \delta ) .
$$

Combining this estimatewith the error bound of the adiabatic midpoint rule for the homogeneous equation as given in Theorem1.2 yields thestated error bound for $\eta _ { \mathrm { 1 } }$

(c）The error bound for the components $p _ { 0 } , q _ { 0 }$ comes about by combining error bounds for the Stormer-Verlet method(which require the bounds for ${ \ddot { p } } _ { 0 } , { \ddot { q } } _ { 0 } )$ and the estimates

$$
\begin{array} { l } { \displaystyle \int _ { t _ { 0 } } ^ { t _ { 0 } + h / 2 } \varepsilon ( S _ { 0 1 } + T _ { 0 } ^ { T } G T _ { 1 } ) Q _ { 1 } \eta ( t ) d t - \frac { h } { 2 } \varepsilon \big ( S _ { 0 1 } + T _ { 0 } ^ { T } G T _ { 1 } \big ) ( t _ { 1 / 2 } ) Q _ { 1 } ^ { - } \eta ^ { 0 } } \\ { = \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ^ { 2 } ) } \end{array}
$$

and

$$
\int _ { t _ { 0 } } ^ { t _ { 0 } + h / 2 } \varepsilon L _ { 1 0 } ^ { T } Q _ { 1 } \eta ( t ) d t - \frac { h } { 2 } \varepsilon L _ { 1 0 } ( t _ { 1 / 2 } ) \mathcal { Q } _ { 1 } ^ { - } \eta ^ { 0 } = \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ) ,
$$

and the same estimates for the second half-step.See also Exercise7 fora similar situation.

In the case of well-separated eigenvalues,the global error on bounded time intervals is thus bounded by $\mathcal { O } ( h ^ { 2 } ) + \mathcal { O } ( h \varepsilon )$ in $\psi _ { 0 } , q _ { 0 }$ for $t \leq$ Const.and by $\mathcal { O } ( h )$ in $\eta$ Inthe original variables $p , q$ of(2.1）,this thenyieldsan error

$$
q _ { n } - q ( t _ { n } ) = { \mathcal O } ( h ^ { 2 } ) + { \mathcal O } ( h \varepsilon ) , \quad p _ { n } - p ( t _ { n } ) = { \mathcal O } ( h ) \quad \mathrm { ~ f o r ~ } t _ { n } \le \mathrm { C o n s t . }
$$

Withanadaptive step size strategyasin Sect.XIV.1.2,itisagain possible to follow $\eta$ through non-adiabatic transitions nearavoided crossings of eigenvalues.

Ahigher-order scheme with a global errorof $\mathcal { O } ( h ^ { 2 } )$ in $\eta -$ in the situation ofseparated eigenvalues-isobtained byreplacingtheupper line in(2.31）bya second-orderadiabatic integratoras discussed in Sect.XIV.1.2,leaving the last term in(2.31） unaltered.In the original variables $p , q$ of(2.1）,theerror is then $\mathcal { O } ( h ^ { 2 } )$ bothin positionsand(fast and slow)momenta.The error is even $\mathcal { O } ( \varepsilon h ^ { 2 } )$ in thefast positions $q _ { \perp }$ of(2.8）,which oscillate with an amplitude $\mathcal { O } ( \varepsilon )$ Werefer to Lorenz, Jahnke&Lubich (2oo5) for theparticular case of second-order differential equations $\ddot { q } + \varepsilon ^ { - 2 } A ( t ) q = 0$ withapositive definite matrix $\boldsymbol A ( t )$ ,

# XIV.2.3 Error Analysis of the Impulse Method

Thetransformation to adiabatic variables of Sect.XIV.2.1 also gives new insight into the error behaviour of multiple time stepping methods such as the impulse or mollified impulse method discussed in SectionsVIII.4 and XIII.1,which do not usecoordinate transforms inthemethod formulation.These methodsare of interest when the eigendecompositions needed inadiabatic integrators are computationally more expensive than doing many small stepswith the fast subsystem,and when evaluations of thepotential force are so costly that the computational work for the fast subsystem becomes irrelevant.We consider the splitting

$$
H = H ^ { \mathrm { f a s t } } + H ^ { \mathrm { s l o w } }
$$

of the Hamiltonian (2.3)with

$$
\begin{array} { r c l } { { H ^ { \mathrm { f a s t } } ( p , E , q , t ) } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } p ^ { T } M ( t ) ^ { - 1 } p + \frac { 1 } { 2 \varepsilon ^ { 2 } } q ^ { T } A ( t ) q + { \bar { E } } } } \\ { { } } & { { } } & { { } } \\ { { H ^ { \mathrm { s l o w } } ( p , E , q , t ) } } & { { = } } & { { \displaystyle U ( q , t ) . } } \end{array}
$$

The impulse method is given as the composition of the exact flows of the subsystems (see SectionsVIII.4 and XIII.1.3):

$$
\varPhi _ { h } = \varphi _ { h / 2 } ^ { \mathrm { s l o w } } \circ \varphi _ { h } ^ { \mathrm { f a s t } } \circ \varphi _ { h / 2 } ^ { \mathrm { s l o w } } ,
$$

whereweare interested intaking long time steps $h \geq c \varepsilon$ (with a positive constant c). The equations of motion of the slow subsystem,

$$
\dot { p } = - \nabla U ( q , t ) , \quad \dot { q } = 0 , \quad \dot { t } = 0 ,
$$

are solved trivially by

$$
\widehat { \boldsymbol { p } } = \boldsymbol { p } - \frac { h } { 2 } \nabla U ( \boldsymbol { q } , t ) , \quad \widehat { \boldsymbol { q } } = \boldsymbol { q } , \quad \widehat { t } = t .
$$

Incontrast,the fastsubsystem needsto be integrated approximately,e.g.,bymany small substepswith the Stormer-Verlet methodin the originalvariables $( p , q )$ orby one step of themethod(2.30)-(2.32)with $G = 0$ inadiabatic variables $( p _ { 0 } , q _ { 0 } , \eta )$ Inthe following we ignore the error resulting from this additional approximation and study the splitting method with exact flows.

Theerror behaviour of this method can be understood with the help of the transformation toadiabatic variablesof Sect.XIV.2.1.The impulsemethod in theadiabaticvariables $p 0 , q _ { 0 } , \eta$ is obtained by splitting the differential equations(2.21)and (2.23).The fast subsystemisobtained by simply putting $U = 0$ in these equations, and the slow subsystemreads

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { - T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) , \quad \dot { q } _ { 0 } = 0 } \\ { \dot { \eta } } & { = } & { - P _ { 1 } ^ { * } T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) } \end{array}
$$

alongwith $\dot { t } = 0$ ,sothat theargument inall thematrices is frozenat the initial time. Here $P _ { 1 } ( t )$ and $Q _ { 1 } ( t )$ areagain the highly oscillatory matrix functions of(2.20). Since $Q _ { 1 } P _ { 1 } ^ { * } = 0$ wehave $Q _ { 1 } \eta = \mathrm { C o n s t }$ ,and therefore,inthesevariablestheflow $\varphi _ { h / 2 } ^ { \mathrm { s l o w } }$ is he mapping given by

$$
\begin{array} { r c l } { { \widehat { p } _ { 0 } } } & { { = } } & { { p _ { 0 } - \displaystyle \frac { h } { 2 } T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t _ { 0 } ) , \widehat { q } _ { 0 } = q _ { 0 } } } \\ { { } } & { { } } & { { } } \\ { { \widehat { \eta } } } & { { = } } & { { \eta - \displaystyle \frac { h } { 2 } P _ { 1 } ^ { * } T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t _ { 0 } ) , } } \end{array}
$$

where the matrices ， , , areevaluated at .In the impulse method, the anotherapplicatiho abovvalueeufoeit $\varphi _ { h / 2 } ^ { \mathrm { s l o w } }$ $\varphi _ { h } ^ { \mathrm { t a s t } }$ which isfllowed by

Adisturbing feature in(2.33) is the appearance of theparticular value $P _ { 1 } ( t _ { 0 } )$ of thehighly oscillatory function instead of theaverage $\mathcal { P } _ { 1 }$ as in (2.31).

Wenow consider the error propagation for $\eta$ in the case of well-separated frequencies.Recall that the exact solution then satisfies $\eta ( t ) ~ = ~ \eta ( 0 ) + \mathcal { O } ( \varepsilon )$ for $t \leq$ Const.For ease of presentation we consider a constant step size $h$ ,

Lemma2.3.Assumetheenergybound(2.2)fortheinitialvalues.Ifthefrequencies $\omega _ { j } ( t )$ remainseparated fromeach other,then the result after $^ { u }$ steps satisfies,for $n h \leq T \leq C o n s t .$ ，

$$
\eta _ { n } = \eta _ { 0 } + \sigma _ { n } + \mathcal { O } ( \varepsilon ) ,
$$

where

$$
\| \sigma _ { n } \| \leq C \kappa \quad w i t h \quad \kappa = \operatorname* { m a x } _ { 0 \leq n h \leq T } \operatorname* { m a x } _ { k } \Big \| h \sum _ { j = 0 } ^ { n } \mathrm { e x p } \Big ( \frac { i } { \varepsilon } \phi _ { k } ( t _ { j } ) \Big ) \Big \| .
$$

Proof.We have $\eta _ { n } ~ = ~ \eta _ { h } ( t _ { n } )$ ,where $\eta _ { h } ( t )$ solves the differential equation with impulses,

$$
\dot { \eta } _ { h } = \exp \left( - \frac { i } { \varepsilon } \varPhi \right) W \exp \left( \frac { i } { \varepsilon } \varPhi \right) \eta _ { h } + r + \sum _ { j } \varDelta \eta _ { j } \delta _ { j } .
$$

Here $W ( t )$ is the matrix (2.22)appearing in (2.23),and

$$
\begin{array} { r } { r ( t ) = - P _ { 1 } ^ { * } ( t ) \big ( L _ { 1 0 } ( t ) p _ { 0 , h } ( t ) + S _ { 0 1 } ( t ) q _ { 0 , h } ( t ) \big ) } \end{array}
$$

with $p _ { 0 , h } ( t )$ , $q _ { 0 , h } ( t )$ denoting the piecewise constant functions that take the values ofthe numerical solution.Furtherwe have

$$
\varDelta \eta _ { j } = - h P _ { 1 } ( t _ { j } ) ^ { \ast } T _ { 1 } ( t _ { j } ) ^ { T } \nabla U \big ( T _ { 0 } ( t _ { j } ) q _ { 0 , j } + \varepsilon T _ { 1 } ( t _ { j } ) Q _ { 1 } ( t _ { j } ) \eta _ { j } , t _ { j } \big ) ,
$$

the expression on the right-hand side of (2.33).and $\delta _ { j }$ isaDirac impulse located at $t _ { j } .$ It follows that,for $t = n h$ ,

$$
\begin{array} { r l l } { \mathrm { \Pi } _ { \mathfrak { i } } - \eta _ { 0 } } & { = } & { \eta _ { h } ( t _ { n } ) - \eta _ { h } ( 0 ) } \\ & { = } & { \displaystyle \int _ { 0 } ^ { t } \exp \left( - \frac { \dot { \iota } } { \varepsilon } \varPhi ( s ) \right) W ( s ) ^ { - } \exp \left( \frac { \dot { \iota } } { \varepsilon } \varPhi ( s ) \right) \eta _ { h } ( s ) d s + \int _ { 0 } ^ { t } r ( s ) d s + \sigma } \end{array}
$$

where $\sigma _ { n }$ is the trapezoidal sum of the terms on the right-hand side of (2.33):

$$
\sigma _ { n } = - h \sum _ { j = 0 } ^ { n } { { ^ { \prime } P _ { 1 } } ( t _ { j } ) ^ { * } T _ { 1 } } ( t _ { j } ) ^ { T } \nabla U \big ( T _ { 0 } ( t _ { j } ) q _ { 0 , j } + \varepsilon T _ { 1 } ( t _ { j } ) Q _ { 1 } ( t _ { j } ) \eta _ { j } , t _ { j } \big ) .
$$

Theprimeonthesumindicatesthatthefirstandlasttermare takenwiththefactor $\textstyle { \frac { 1 } { 2 } }$ . Usingpartial integrationas in（1.6）,we obtain

$$
\int _ { 0 } ^ { t } \exp \Bigl ( - \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) W ( s ) \exp \Bigl ( \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) \eta _ { h } ( s ) d s = \mathcal { O } ( \varepsilon ) ,
$$

and by partial integration as in (2.25),

$$
\int _ { 0 } ^ { t } r ( s ) d s = { \mathcal { O } } ( \varepsilon ) .
$$

This shows (2.34).A partial summation in (2.36),summingup the oscillatory terms $P _ { 1 } ( t _ { j } )$ and differencing the smoother other terms,then yields(2.35). □

The size of $\boldsymbol { \kappa }$ of(2.35)depends on possible resonances between the step size and thefrequencies,yielding $\boldsymbol { \kappa }$ between $\mathcal { O } ( h )$ and ${ \mathcal { O } } ( 1 ) .$ For the error of the method we have the following.

Theorem2.4.Assume theenergy bound(2.2)fortheinitialvalues.Ifthefrequencies $\omega _ { j } ( t )$ remainseparatedfromeachother,thentheerroroftheimpulsemethod aftern steps with step size $h \geq c \varepsilon$ satisfies

$$
\begin{array} { r c l } { { p _ { n } - p ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( \kappa ) } } \\ { { q _ { n } - q ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( h ^ { 2 } ) + { \mathcal { O } } ( \varepsilon \kappa ) . } } \end{array}
$$

Theconstants symbolized by $\mathcal { O }$ do not depend on $\boldsymbol { \varepsilon }$ , $h$ andnwith $n h \le \mathrm { C o n s t }$

Proof The error of size $\mathcal { O } ( \kappa )$ in $\eta$ immediately implies an error of size $\mathcal O ( \kappa )$ in the actions $\begin{array} { r } { I _ { j } = \frac { 1 } { 2 } | \eta _ { j } | ^ { 2 } } \end{array}$ ,andan error of ${ \mathcal { O } } ( \kappa )$ in the fast momenta $p _ { 1 }$ andof $\mathcal { O } ( \varepsilon \kappa )$ in the fast positions $q _ { 1 }$ of(2.9);recall the transformation (2.16)and the rescaling.In the slow components $p _ { 0 } , q _ { 0 }$ themethod isaperturbed variantof the Stormer-Verlet method.The contribution of the perturbations $\varepsilon T _ { 1 } Q _ { 1 } \eta$ to the error is of size $\mathcal { O } ( \varepsilon \kappa )$ Thisis seen byapplying the simple lemma belowwith $y = ( p _ { 0 } , q _ { 0 } )$ and

$$
d _ { n } = \left( { - h T _ { 0 } ( t _ { n } ) ^ { T } \nabla ^ { 2 } U ( T _ { 0 } ( t _ { n } ) q _ { 0 , n } , t _ { n } ) \varepsilon T _ { 1 } ( t _ { n } ) Q _ { 1 } ( t _ { n } ) \eta _ { n } } \right) + \mathcal { O } ( h ^ { 2 } \varepsilon )
$$

and using partial summation of the $d _ { n }$ ,summing up the oscillatory terms $Q _ { 1 } ( t _ { n } )$ and differencingthe other terms. □

Lemma 2.5.Let $\bar { \varPhi } _ { h } ( y ) = y + h F _ { h } ( y )$ bea one-step method where $F _ { h }$ hasLipschitz constant $L$ .Considerthemethodandaperturbation,

$$
y _ { n + 1 } = \varPhi _ { h } ( y _ { n } ) \qquad a n d \qquad \widetilde { y } _ { n + 1 } = \varPhi _ { h } ( \widetilde { y } _ { n } ) + d _ { n } ,
$$

withthesame starting values $y _ { 0 } = y _ { 0 }$ .Then,thedifferenceisboundedby

$$
\left\| \widetilde { y } _ { n } - y _ { n } \right\| \leq e ^ { n h L } , \operatorname* { m a x } _ { 0 \leq k \leq n - 1 } \left\| \sum _ { j = 0 } ^ { k } d _ { j } \right\| .
$$

ProofThe result follows from

$$
\widetilde { y } _ { n } - y _ { n } = h \sum _ { j = 0 } ^ { n - 1 } \bigl ( F _ { h } ( \widetilde { y } _ { n } ) - F _ { h } ( y _ { n } ) \bigr ) + \sum _ { j = 0 } ^ { n - 1 } d _ { j }
$$

with the discrete Gronwall inequality.

# XIV.2.4 ErrorAnalysis of the Mollified ImpulseMethod

The problem with possible step-size resonances can be greatly alleviated by the mollified impulse method (see Sect.XII.1.4) where the potential $U ( q , t )$ isreplaced bya modified potential ${ \overline { { U } } } ( q , t ) .$ A good choice is

$$
\overline { { U } } ( \boldsymbol { q } , t ) = U ( \boldsymbol { A } ( t ) \boldsymbol { q } , t ) \quad \mathrm { ~ w i t h ~ } \ \boldsymbol { A } ( t ) = C ( t ) Q ( t ) \left( \begin{array} { c c } { I } & { 0 } \\ { 0 } & { S ( t ) } \end{array} \right) Q ( t ) ^ { T } C ( t ) ^ { - 1 }
$$

with $C$ and $Q$ of(2.4) and (2.6），and

$$
{ \mathcal { S } } ( t ) = \mathrm { s i n c } \left( { \frac { h } { \varepsilon } } { \mathcal { \Omega } } ( t ) \right) = { \frac { 1 } { 2 h } } \int _ { - h } ^ { h } \mathrm { e x p } \left( \pm { \frac { i s } { \varepsilon } } { \mathcal { \Omega } } ( t ) \right) d s .
$$

Acalculation shows that itreplaces (2.33)by

$$
\begin{array} { r c l } { { \widehat { p } _ { 0 } } } & { { = } } & { { p _ { 0 } - \displaystyle \frac { h } { 2 } T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } \mathcal { Q } _ { 1 } \eta , t _ { 0 } ) , \quad \widehat { q } _ { 0 } = q _ { 0 } } } \\ { { } } & { { } } & { { } } \\ { { \widehat { \eta } } } & { { = } } & { { \eta - \displaystyle \frac { h } { 2 } \mathcal { P } _ { 1 } ^ { * } T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } \mathcal { Q } _ { 1 } \eta , t _ { 0 } ) , } } \end{array}
$$

withmatrix functions evaluated at $t _ { 0 }$ ,where $\mathcal { P } _ { 1 } ( t )$ and $\mathcal { Q } _ { 1 } ( t )$ are the linear-phase approximationsto theaverage over the interval $\lfloor t - h , t + h \rfloor$ of $P _ { 1 }$ and $Q _ { 1 }$ ,respectively,

$$
\begin{array} { l } { \displaystyle \mathcal { P } _ { 1 } ( t ) = \mathcal { S } ( t ) P _ { 1 } ( t ) = \frac { 1 } { 2 h } \int _ { t - h } ^ { t + h } P _ { 1 } ( s ) d s + \mathcal { O } ( h ) } \\ { \displaystyle \mathcal { Q } _ { 1 } ( t ) = \mathcal { S } ( t ) Q _ { 1 } ( t ) = \frac { 1 } { 2 h } \int _ { t - h } ^ { t + h } Q _ { 1 } ( s ) d s + \mathcal { O } ( h ) . } \end{array}
$$

Therefore,(2.34) and(2.36) hold with the highly oscillatory $P _ { 1 } ( t _ { j } )$ replaced by the averages $\mathcal { P } _ { 1 } ( t _ { j } )$ Usingapartial summation in(2.36)and noting that,for $t = n h \leq$ Const.,

$$
\left\| h \sum _ { j = 1 } ^ { n } \mathcal { P } _ { 1 } ( t _ { j } ) \right\| = \left\| \int _ { 0 } ^ { t } P _ { 1 } ( s ) d s \right\| + \mathcal { O } ( h ) = \mathcal { O } ( \varepsilon ) + \mathcal { O } ( h ) ,
$$

we obtain an estimate

$$
\eta _ { n } = \eta _ { 0 } + O ( h )
$$

instead of the corresponding bound(2.34）with(2.35).This eliminates the bad effect of step size resonances (large $\boldsymbol { \kappa }$ ）onthe propagationin the fastvariables over bounded time intervals $t \leq$ Const.(though not on longer intervals,as we know from Chap.XIII).The more harmless effect of step size resonances on the slow variables, as visible in the term $\mathcal { O } ( \varepsilon \kappa )$ in Theorem 2.4,is likewise reduced to $\mathcal { O } ( \varepsilon h )$ Wethus obtain the following improvement over the error bounds in Theorem 2.4.

Theorem2.6.Assumetheenergybound(2.2)for theinitialvalues.Ifthefrequencies $\omega _ { j } ( t )$ remain separatedfromeachother,thentheerror of theabovemollified impulsemethodafter $n$ stepswith step size $h \geq c \varepsilon$ satisfies

$$
\begin{array} { r c l } { { p _ { n } - p ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( h ) } } \\ { { q _ { n } - q ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( h ^ { 2 } ) . } } \end{array}
$$

Theconstants symbolized by $\mathcal { O }$ do notdepend on $\boldsymbol { \varepsilon }$ ， $h$ andnwith $n h \leq \mathrm { C o n s t }$

Adirect implementation of thismethod requires just the same matrix decompositions that are needed for the integrators inadiabatic variables.Itis thenreasonable touseone step of the adiabatic integrator of Sect.XIV.2.2 for solvingthe fast subsystem overa timestep.

Analternative is tocompute the average $\boldsymbol { A } ( t )$ by smalltime steps from thelinear differential equation with the Hamiltonian $H ^ { \mathrm { f a s t } }$ ,asformulated in Sect.XIII.1.4. The method described here thencorresponds to (XIII.1.18)with $c = 1$

# XIV.3Mechanical Systems with Solution-Dependent Frequencies

We²consider the Hamiltonian

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q ) + { \frac { 1 } { \varepsilon ^ { 2 } } } V ( q )
$$

with a strong potential ${ \mathcal { E } } ^ { - 2 } V ( q )$ that penalizes some directions of motion.Analytical studiesof thisproblemweredonebyRubin&Ungar（1957),Takens(1980),and Bornemann(1998).Inanalternative approach to theseworks,we here describea transformation of the problem toadiabatic variables.This gives new insight into the solution behaviour and can be used as the starting point for the construction of longtime-step integrators.Italso enables us to analyse the error of multiple time-stepping methods.

# XIV.3.1 Constraining Potentials

Weconsider the Hamiltonian(3.1）,where $M ( q )$ isasymmetric positive definite mass matrix depending smoothly on the positions $q \in \mathbb { R } ^ { n }$ , $U$ isasmooth potential, and theconstraining potential is assumed to satisfy the following:

The smooth function $V : D \subset \mathbb { R } ^ { n } \longrightarrow \mathbb { R }$ attainsits minimumvalueOona $d$ -dimensional manifold $\nu \subset \mathbb { R } ^ { n }$ ,

$$
\mathcal V = \{ q \in D \mid V ( q ) = \operatorname* { m i n } V = 0 \} .
$$

Ina neighourhood of $\nu$ ,thepotential $V$ isstrongly convex along directions nontangential to $\nu$ ,that is,there exists $\alpha > 0$ such that for $q \in \mathcal V$ ,theHessian $\nabla ^ { 2 } V ( q )$ satisfies

$$
v ^ { T } \nabla ^ { 2 } V ( q ) v \geq \alpha \cdot v ^ { T } M ( q ) v
$$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0009_pages_0561-0630/auto/images/543b6ef1f7c18d3b28cfd6fcc86fab3bba0c8ae7c615bd41dfc3ef84ff2cb5e3.jpg)

for all vectors $\boldsymbol { v }$ in the $M ( q )$ -orthogonalcomplementof thetangent space $T _ { q } \nu$

Welet $m = n - d$ be the number of independent constraints that locally describe themanifold $\nu$ .

Example 3.1 (Chain of Stiff Springs).The position of $m + 1$ mass points in a plane,arranged in a chain connected by stiff springs with spring constants $\alpha _ { i } ^ { 2 } / \varepsilon ^ { 2 }$ ,is determined by the Cartesiancoordinates of the first mass point and by m anglesi and the elongations $d _ { i }$ ofthe $\boldsymbol { n }$ springs.The constraining potential is

$$
V = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } \alpha _ { i } ^ { 2 } d _ { i } ^ { 2 } ,
$$

and the constraint manifold is described by $d _ { 1 } = \dots = d _ { m } = 0$ corresponding to non-elongated springs.The frequencies of the vibrationsin such achain depend on theangles.

In the above example we have,in the coordinates givenby the anglesand elongations,apotential $V$ of theform

$$
V ( q ) = \frac { 1 } { 2 } q _ { 1 } ^ { T } A ( q _ { 0 } ) q _ { 1 }
$$

for $q = ( q _ { 0 } , q _ { 1 } ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { m }$ ,with a positive definite matrix $A ( q _ { 0 } )$ .The manifold of constraints is here simply $\mathcal { V } = \mathbb { R } ^ { d } \times 0$ Asthe following lemma shows,thisis already the general situation in suitable local coordinates.

Lemma3.2.Underconditions(3.2)-(3.3),thereexistsasmoothlocal changeof coordinates $q = \chi ( y )$ suchthat

$$
V ( q ) = \frac { 1 } { 2 } y _ { 1 } ^ { T } A ( y _ { 0 } ) y _ { 1 } ~ j o r ~ q = \chi ( y )
$$

with $\boldsymbol { y } = \left( y _ { 0 } , y _ { 1 } \right)$ near $_ 0$ in $\mathbb { R } ^ { d } \times \mathbb { R } ^ { m }$ ,where $A ( y _ { 0 } )$ is $a$ symmetricpositivedefinite $m \times m$ matrix.

Proof.Ina first step,we choose local coordinates $q = \psi ( x )$ with $\boldsymbol { x } = \left( \boldsymbol { x } _ { 0 } , \boldsymbol { x } _ { 1 } \right)$ near $_ 0$ in $\mathbb { R } ^ { d } \times \mathbb { R } ^ { m }$ ,such that $q = \psi ( x ) \in \mathcal { V }$ ifand only if $x _ { 1 } = 0 .$ In these coordinates, denoting ${ \hat { V } } ( x ) = V ( q )$ for $q = \psi ( x )$ ,we then have

$$
\widehat { V } ( x _ { 0 } , 0 ) = 0 , \quad \nabla \widehat { V } ( x _ { 0 } , 0 ) = 0
$$

by(3.2）,and

$$
A ( x _ { 0 } ) : = \nabla _ { x _ { 1 } } ^ { 2 } \widehat { V } ( x _ { 0 } , 0 ) \quad \mathrm { i s ~ p o s i t i v e ~ d e f n i t e }
$$

by(3.3).We now change coordinates by the near-identity transformation

$$
y _ { 0 } = x _ { 0 } , \quad y _ { 1 } = \mu ( x ) x _ { 1 }
$$

where thereal factor $\mu ( x )$ (near1for $x _ { 1 }$ near $0$ is to be chosen such that

$$
\frac 1 2 y _ { 1 } ^ { T } A ( y _ { 0 } ) y _ { 1 } = \widehat { V } ( x _ { 0 } , x _ { 1 } ) .
$$

Since the right-hand side equals

$$
\widehat { V } ( x _ { 0 } , x _ { 1 } ) - \widehat { V } ( x _ { 0 } , 0 ) - x _ { 1 } ^ { T } \nabla \widehat { V } ( x _ { 0 } , 0 ) = \frac { 1 } { 2 } x _ { 1 } ^ { T } A ( x _ { 0 } ) x _ { 1 } + r ( x )
$$

with $r ( x ) = \mathcal { O } ( \| x _ { 1 } \| ^ { 3 } )$ ,the choice

$$
\mu ( x ) = \sqrt { 1 + \frac { 2 r ( x ) } { x _ { 1 } ^ { T } A ( x _ { 0 } ) x _ { 1 } } }
$$

does the trick.

Weremark thatLemma3.2couldbeobtainedasacorollary to theMorse lemma, forwhichwerefer to Abraham&Marsden（1978)and Crouzeix&Rappaz(1989).

The change to the local coordinates $\boldsymbol { x } = \left( \boldsymbol { x } _ { 0 } , \boldsymbol { x } _ { 1 } \right)$ such that $V ( q ) = 0$ if and only if $x _ { 1 } = 0$ for $q = \psi ( x )$ isnot numerically constructive from the mere knowledge ofanexpression for the potential $V _ { \ast }$ However,in many situations the manifold $\nu$ can be described by constraints $g ( q ) = 0$ ,and $x _ { \mathrm { 1 } } = g$ can then be extended toa full setofcoordinates.The above transformation from $x$ to $y$ canbe done numerically. In theusual way,the transformation $q = \chi ( y )$ of the position coordinates extends to acanonical transformation by setting $p _ { y } = \chi ^ { \prime } ( y ) ^ { T } p$ for the conjugate momenta; seeExample VI.5.2.

Solutions of(3.1） arein general oscillatorywith frequencies of siz $c \sim \varepsilon ^ { - 1 }$ Thereexist,however,special solutions having arbitrarily many time derivatives bounded independently of $\succeq$ ,which forarbitrary $N \geq 1$ stay $\mathcal { O } ( \varepsilon ^ { N } )$ close toa manifold $\mathcal { V } ^ { \varepsilon , N }$ that has a distance $\mathcal { O } ( \varepsilon )$ to $V$ SeeLubich(1993),where also implicit Runge-Kutta methods for the approximation of the smooth solutions are studied.In thissectionwe are,however,interested in approximating general oscillatory solutions of bounded energy.

# XIV.3.2 Transformationto Adiabatic Variables

We start froma Hamiltonian (3.1) incoordinates $( p , q )$ where the constraining potential isalreadyof theform(3.4)for $q = ( q _ { 0 } , q _ { 1 } )$ Wenote that forasystem of bounded energy,we then have $q _ { 1 } = { \mathcal { O } } ( \varepsilon )$

Wenowperformaseries of canonical transformations that take the Hamiltonian intoaform that is better suited fora direct numerical treatmentand for theerroranalysis of multiple time-stepping methods.The transformations are similar to those for the time-dependent case treated in Sect.XIV.2.1,but here theyappear ina permuted order.

Transforming the Stiffness Matrix into the Identity.We write the Cholesky decomposition of the stiffness matrix as

$$
A ( q _ { 0 } ) = C ( q _ { 0 } ) ^ { - T } C ( q _ { 0 } ) ^ { - 1 }
$$

and change to variables

$$
q _ { 0 } = \widetilde { q } _ { 0 } , q _ { 1 } = C ( \widetilde { q } _ { 0 } ) \widetilde { q } _ { 1 }
$$

along with the conjugate momenta

$$
\widetilde { p } _ { 0 } = p _ { 0 } + \Big ( \frac { \partial } { \partial \widetilde { q } _ { 0 } } C ( \widetilde { q } _ { 0 } ) \widetilde { q } _ { 1 } \Big ) ^ { T } p _ { 1 } , \quad \widetilde { p } _ { 1 } = C ( \widetilde { q } _ { 0 } ) ^ { T } p _ { 1 } .
$$

With the transformed mass matrix $\boldsymbol { \bar { M } } ( \boldsymbol { \tilde { q } } ) = \boldsymbol { B } ( \boldsymbol { \tilde { q } } ) \boldsymbol { M } ( \boldsymbol { \tilde { q } _ { 0 } } , \boldsymbol { C } ( \boldsymbol { \tilde { q } _ { 0 } } ) \boldsymbol { \tilde { q } _ { 1 } } ) \boldsymbol { B } ( \boldsymbol { \tilde { q } } ) ^ { T }$ (for the matrix $B ( { \widehat { q } } )$ that transforms $\widetilde { p } = B ( \widetilde { q } ) p )$ and the potential $\begin{array} { r } { \boldsymbol { U } ( \widetilde { \boldsymbol { q } } ) = \boldsymbol { U } ( \widetilde { q } _ { 0 } , \boldsymbol { C } ( \widetilde { q } _ { 0 } ) \widetilde { q } _ { 1 } ) } \end{array}$ , theHamiltonian takes the simplified form (we omit alltildes)

$$
H = \frac { 1 } { 2 } { p } ^ { T } M ( q ) ^ { - 1 } p + \frac { 1 } { 2 { \varepsilon } ^ { 2 } } q _ { 1 } ^ { T } q _ { 1 } + U ( q ) .
$$

Eliminating Off-Diagonal Blocks in the Mass Matrix. We write the mass matrix $M ( q )$ as

$$
M = \left( \begin{array} { c c } { { M _ { 0 0 } } } & { { M _ { 0 1 } } } \\ { { M _ { 1 0 } } } & { { M _ { 1 1 } } } \end{array} \right) .
$$

With $G ( \overline { { { q } } } _ { 0 } ) = - M _ { 0 0 } ( \overline { { { q } } } _ { 0 } , 0 ) ^ { - 1 } M _ { 0 1 } ( \overline { { { q } } } _ { 0 } , 0 )$ ,we transform

$$
q _ { 0 } = \overline { { { q } } } _ { 0 } + G ( \overline { { { q } } } _ { 0 } ) \overline { { { q } } } _ { 1 } , \quad q _ { 1 } = \overline { { { q } } } _ { 1 } ,
$$

with the conjugate momenta

$$
\overline { { p } } _ { 0 } = p _ { 0 } + \bigg ( \frac { \partial } { \partial \overline { { q } } _ { 0 } } G ( \overline { { q } } _ { 0 } ) \overline { { q } } _ { 1 } \bigg ) ^ { T } p _ { 0 } , \quad \overline { { p } } _ { 1 } = p _ { 1 } + G ( \overline { { q } } _ { 0 } ) ^ { T } p _ { 0 } .
$$

Thiscanonical change ofvariables eliminates $M _ { 0 1 }$ and $M _ { 1 0 }$ in the transformed mass matrix $\boldsymbol { M } ( \boldsymbol { q } _ { 0 } , 0 )$ and keeps the Schur complement on the block diagonal:with the symmetric positive definite matrices

$$
\overline { { { M } } } _ { 0 } ( \overline { { { q } } } _ { 0 } ) = M _ { 0 0 } ( \overline { { { q } } } _ { 0 } , 0 ) , \quad \overline { { { M } } } _ { 1 } ( \overline { { { q } } } _ { 0 } ) = \left( M _ { 1 1 } - M _ { 1 0 } M _ { 0 0 } ^ { - 1 } M _ { 0 1 } \right) ( \overline { { { q } } } _ { 0 } , 0 ) ,
$$

thetransformation puts the Hamiltonian into theform(we omit all bars)

$$
\begin{array} { r c l } { { \cal H } } & { { \equiv } } & { { \displaystyle { \frac { 1 } { 2 } } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + \frac { 1 } { 2 } p _ { 1 } ^ { T } M _ { 1 } ( q _ { 0 } ) ^ { - 1 } p _ { 1 } + \frac { 1 } { 2 \varepsilon ^ { 2 } } q _ { 1 } ^ { T } q _ { 1 } } } \\ { { } } & { { } } & { { \displaystyle { + \frac { 1 } { 2 } p ^ { T } R ( q ) p + U ( q _ { 0 } + G ( q _ { 0 } ) q _ { 1 } , q _ { 1 } ) } } } \end{array}
$$

where $R$ is asmooth matrix-valued function satisfying

$$
R ( q _ { 0 } , 0 ) = 0 .
$$

Diagonalizing theMassMatrix oftheFast Variables.Wediagonalize

$$
M _ { 1 } ( q _ { 0 } ) = Q ( q _ { 0 } ) \Omega ( q _ { 0 } ) ^ { - 2 } Q ( q _ { 0 } ) ^ { T }
$$

with the diagonal matrix $\varOmega ( q _ { 0 } ) = \mathrm { d i a g } ( \omega _ { j } ( q _ { 0 } ) )$ of frequencies and an orthogonal matrix $Q ( q _ { 0 } )$ ,which depends smoothly on $q _ { 0 }$ if the frequenciesare separated.We transform

$$
q _ { 0 } = \widehat { q } _ { 0 } , q _ { 1 } = Q ( \widehat { q } _ { 0 } ) \widehat { q } _ { 1 }
$$

with the conjugate momenta

$$
\widehat { p } _ { 0 } = p _ { 0 } + \bigg ( \frac { \partial } { \partial \widehat { q } _ { 0 } } Q ( \widehat { q } _ { 0 } ) \widehat { q } _ { 1 } \bigg ) ^ { T } p _ { 1 } , \quad \widehat { p } _ { 1 } = Q ( \widehat { q } _ { 0 } ) ^ { T } p _ { 1 } .
$$

Thematrix

$$
\boldsymbol { Y } ( \boldsymbol { \widehat { q } } ) = \Big ( \frac { \partial } { \partial \widehat { q _ { 0 } } } \boldsymbol { Q } ( \widehat { q _ { 0 } } ) \boldsymbol { \widehat { q } } _ { 1 } \Big ) ^ { T } \boldsymbol { Q } ( \widehat { q _ { 0 } } )
$$

is of size $\mathcal { O } ( \widehat { q } _ { 1 } )$ butitis this expression which may become large near avoided crossings of eigenvalues.We consider the associated matrix

$$
\begin{array} { r } { X ( \widehat { q } ) = \left( \begin{array} { c c } { 0 } & { X _ { 0 1 } } \\ { X _ { 1 0 } } & { X _ { 1 1 } } \end{array} \right) = \left( \begin{array} { c c } { 0 } & { - M _ { 0 } ^ { - 1 } Y } \\ { - Y ^ { T } M _ { 0 } ^ { - 1 } } & { Y ^ { T } M _ { 0 } ^ { - 1 } Y } \end{array} \right) . } \end{array}
$$

With amatrix $\widehat { R } ( \widehat { q } )$ satisfying(3.7),which isasumof the appropriately transformed previous matrix $R$ and the above matrix $X$ ,theHamiltonianin the newvariables $( \widehat { p } , \widehat { q } )$ becomes (we omit all hats）

$$
\begin{array} { r l r } { H } & { = } & { \frac { 1 } { 2 } { p } _ { 0 } ^ { T } M _ { 0 } ( { q } _ { 0 } ) ^ { - 1 } { p } _ { 0 } + \frac { 1 } { 2 } { p } _ { 1 } ^ { T } \Omega ( { q } _ { 0 } ) ^ { 2 } { p } _ { 1 } + \frac { 1 } { 2 { \varepsilon } ^ { 2 } } { q } _ { 1 } ^ { T } { q } _ { 1 } } \\ & { } & { \mathrm + \frac { 1 } { 2 } { p } ^ { T } R ( { q } ) { p } + U ( { q } _ { 0 } + G Q ( { q } _ { 0 } ) { q } _ { 1 } , Q ( { q } _ { 0 } ) { q } _ { 1 } ) . } \end{array}
$$

RescalingPositionsandMomenta.Wechangeto rescaled fast variables

$$
q _ { 0 } = \check { q } _ { 0 } , ~ q _ { 1 } = \varepsilon ^ { 1 / 2 } \varOmega ( \check { q } _ { 0 } ) ^ { 1 / 2 } \check { q } _ { 1 }
$$

(note that $q _ { 1 } = \mathcal { O } ( \varepsilon )$ implies $\check { q } _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } ) )$ with the conjugate momenta

$$
\check { p } _ { 0 } \equiv p _ { 0 } + \varepsilon ^ { 1 / 2 } \Big ( { \frac { \partial } { \partial \check { q } _ { 0 } } } \varOmega ( \check { q } _ { 0 } ) ^ { 1 / 2 } \check { q } _ { 1 } \Big ) ^ { T } p _ { 1 } , \quad \check { p } _ { 1 } = \varepsilon ^ { 1 / 2 } \varOmega ( \check { q } _ { 0 } ) ^ { 1 / 2 } p _ { 1 } .
$$

In thenew variables,the Hamiltonian becomes(we omit the haceks onall variables)

$$
\begin{array} { r c l } { { H } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 } } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } { \varOmega } ( q _ { 0 } ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } { \varOmega } ( q _ { 0 } ) q _ { 1 } } } \\ { { } } & { { } } & { { \displaystyle { + \frac { 1 } { 2 } } p ^ { T } R ( q ) p + U ( T ( q _ { 0 } ) q ) , } } \end{array}
$$

where

$$
T = \Big ( T _ { 0 } \ \big \vert \ \varepsilon ^ { 1 / 2 } T _ { 1 } \Big ) = \left( \begin{array} { c c } { I } & { \varepsilon ^ { 1 / 2 } G Q \varOmega ^ { 1 / 2 } } \\ { 0 } & { \varepsilon ^ { 1 / 2 } Q \varOmega ^ { 1 / 2 } } \end{array} \right)
$$

and $R ( q )$ isa symmetric matrix of the form

$$
R ( q ) = \left( \begin{array} { c c } { { R _ { 0 0 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } & { { \varepsilon ^ { - 1 / 2 } R _ { 0 1 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } \\ { { \varepsilon ^ { - 1 / 2 } R _ { 1 0 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } & { { \varepsilon ^ { - 1 } R _ { 1 1 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } \end{array} \right)
$$

with smooth functions $R _ { i j }$ satisfying $R _ { i j } ( q _ { 0 } , 0 ) = 0$ Therefore,the expression ${ \scriptstyle { \frac { 1 } { 2 } } } p ^ { T } R ( q ) p$ can berewritten in the form

$$
\begin{array} { r c l } { \frac { 1 } { 2 } \boldsymbol { p } ^ { T } \boldsymbol { R } ( \boldsymbol { q } ) \boldsymbol { p } } & { = } & { \boldsymbol { \varepsilon } ^ { 1 / 2 } \boldsymbol { c } ( \boldsymbol { p } _ { 0 } , \boldsymbol { q } _ { 0 } ) ^ { T } \boldsymbol { q } _ { 1 } + \boldsymbol { p } _ { 1 } ^ { T } \boldsymbol { L } ( \boldsymbol { p } _ { 0 } , \boldsymbol { q } _ { 0 } ) ^ { T } \boldsymbol { q } _ { 1 } } \\ & & { + } & { \boldsymbol { \varepsilon } ^ { - 1 / 2 } \boldsymbol { \tau } ( \boldsymbol { p } _ { 1 } , \boldsymbol { p } _ { 1 } , \boldsymbol { q } _ { 1 } ; \boldsymbol { p } _ { 0 } , \boldsymbol { q } _ { 0 } ) + \rho ( \boldsymbol { p } , \boldsymbol { q } ) , } \end{array}
$$

withavector $c$ ,amatrix $L$ ,afunction $\tau$ that is trilinear in $p _ { 1 } , p _ { 1 } , q _ { 1 }$ ,andaremainder ofsize $\rho ( p , q ) = { \mathcal O } ( \varepsilon ^ { 2 } )$ for $p _ { 1 } , q _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ whosepartial derivatives with respect to $p _ { 1 } , q _ { 1 }$ are ofsize $\mathcal { O } ( \varepsilon ^ { 3 / 2 } )$ ,and with respect to $p _ { 0 } , q _ { 0 }$ ofsize $\mathcal { O } ( \varepsilon ^ { 2 } )$ ,

Equations of Motion.The differential equations now take the form

$$
\begin{array} { r c l } { { \dot { p } _ { 0 } } } & { { = } } & { { \displaystyle - \nabla _ { q _ { 0 } } \left( \frac { 1 } { 2 } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + U ( q _ { 0 } , 0 ) \right) } } \\ { { } } & { { } } & { { \displaystyle - \nabla _ { q _ { 0 } } \left( \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \mathcal { Q } ( q _ { 0 } ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \mathcal { Q } ( q _ { 0 } ) q _ { 1 } \right) + f _ { 0 } ( p , q ) } } \\ { { \dot { q } _ { 0 } } } & { { = } } & { { \displaystyle M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + g _ { 0 } ( p , q ) } } \\ { { \left( \begin{array} { c } { { \dot { p } _ { 1 } } } \\ { { \dot { q } _ { 1 } } } \end{array} \right) } } & { { = } } & { { \displaystyle \frac { 1 } { \varepsilon } \left( \begin{array} { c c } { { 0 } } & { { - \mathcal { Q } ( q _ { 0 } ) } } \\ { { \mathcal { Q } ( q _ { 0 } ) } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { p _ { 1 } } } \\ { { q _ { 1 } } } \end{array} \right) + \left( \begin{array} { c } { { f _ { 1 } ( p , q ) } } \\ { { g _ { 1 } ( p , q ) } } \end{array} \right) } } \end{array}
$$

with the functions

$$
\begin{array} { r c l } { { \left( \begin{array} { c } { { f _ { 0 } } } \\ { { f _ { 1 } } } \end{array} \right) } } & { { = } } & { { - \nabla _ { q } \left( \frac 1 2 p ^ { T } R ( q ) p + U ( T ( q _ { 0 } ) q ) - U ( q _ { 0 } , 0 ) \right) } } \\ { { } } & { { } } & { { } } \\ { { \left( \begin{array} { c } { { g _ { 0 } } } \\ { { g _ { 1 } } } \end{array} \right) } } & { { = } } & { { R ( q ) p . } } \end{array}
$$

We note the magnitudes $f _ { 0 } = \mathcal { O } ( \varepsilon )$ , $g _ { 0 } = \mathcal { O } ( \varepsilon )$ and $f _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ , $g _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ inthecase of separated eigenfrequencies,where the diagonalizationis smooth with bounded derivatives.By(3.11）we have(omittingthearguments $p _ { 0 } , q _ { 0 }$ in $c , L , I ^ { \prime }$ ）

$$
\begin{array} { r l r } { f _ { 1 } } & { = } & { - \varepsilon ^ { 1 / 2 } c - L p _ { 1 } + \varepsilon ^ { - 1 / 2 } a ( p _ { 1 } , p _ { 1 } ; p _ { 0 } , q _ { 0 } ) - \varepsilon ^ { 1 / 2 } T _ { 1 } ^ { T } \nabla U ( q _ { 0 } , 0 ) + { \mathcal O } ( \varepsilon ^ { 3 / 2 } ) } \\ { g _ { 1 } } & { = } & { L ^ { T } q _ { 1 } + \varepsilon ^ { - 1 / 2 } b ( p _ { 1 } , q _ { 1 } ; p _ { 0 } , q _ { 0 } ) + { \mathcal O } ( \varepsilon ^ { 3 / 2 } ) \qquad ( \partial _ { \tau } \partial _ { q _ { 0 } } q _ { 0 } ) + { \mathcal O } ( \varepsilon ^ { 3 / 2 } ) , } \end{array}
$$

where the functions $a$ and $b$ are bilinear in their first twoarguments.

TheSystemin Adiabatic Variables.We finally leave the canonical framework and transformtoadiabaticvariables as in(2.16).Alongasolution $( p ( t ) , q ( t ) )$ ofthe system (3.12)we consider the diagonal phase matrix $\varPhi ( t )$ defined by

$$
\dot { \Phi } = \Lambda ( q _ { 0 } ) \mathrm { w i t h } \Lambda ( q _ { 0 } ) = \left( \begin{array} { c c } { { \Omega ( q _ { 0 } ) } } & { { 0 } } \\ { { 0 } } & { { - \Omega ( q _ { 0 } ) } } \end{array} \right) .
$$

With the constant unitary matrix $\varGamma$ of(2.14），which diagonalizes the matrix in (3.12),we introduce theadiabatic variables

$$
\eta = \varepsilon ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi \right) \bar { \varGamma } ^ { \ast } \left( \begin{array} { c } { { p _ { 1 } } } \\ { { q _ { 1 } } } \end{array} \right)
$$

and denote the inverse transform as

$$
\binom { p _ { 1 } } { q _ { 1 } } = \varepsilon ^ { 1 / 2 } \binom { p _ { 1 } } { Q _ { 1 } } \eta = \varepsilon ^ { 1 / 2 } { \cal { T } } \exp \Big ( \frac { i } { \varepsilon } \Phi \Big ) \eta .
$$

The differential equations (3.12) for $p _ { 1 } , q _ { 1 }$ then turn into

$$
\dot { \eta } = \dot { \varepsilon } ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi \right) \varGamma ^ { * } \left( { \begin{array} { c } { f _ { 1 } } \\ { g _ { 1 } } \end{array} } \right) = \varepsilon ^ { - 1 / 2 } P _ { 1 } ^ { * } f _ { 1 } + \varepsilon ^ { - 1 / 2 } Q _ { 1 } ^ { * } g _ { 1 }
$$

with the arguments $( p _ { 0 } , \varepsilon ^ { 1 / 2 } P _ { 1 } \eta , q _ { 0 } , \varepsilon ^ { 1 / 2 } Q _ { 1 } \eta )$ in the functions $f _ { 1 } , g _ { 1 } .$ Inserting the expressions for $f _ { 1 }$ and $g _ { \mathrm { 1 } }$ from(3.13),we obtain as in(2.22) and(2.23),with

$$
W = - \frac { 1 } { 2 } \left( \begin{array} { c c } { { L - L ^ { T } } } & { { L + L ^ { T } } } \\ { { L + L ^ { T } } } & { { L - L ^ { T } } } \end{array} \right) ,
$$

thedifferential equation

$$
\begin{array} { r c l } { \dot { \eta } } & { = } & { \displaystyle \exp ( - \frac { i } { \varepsilon } \varPhi ) W ( p _ { 0 } , q _ { 0 } ) \exp ( \frac { i } { \varepsilon } \varPhi ) \eta } \\ & & { +  \exp ( - \frac { i } { \varepsilon } \varPhi ) L ^ { * } ( ^ { a ( P _ { 1 } \eta , P _ { 1 } \eta ; p _ { 0 } , q _ { 0 } ) } _ { b ( P _ { 1 } \eta , Q _ { 1 } \eta ; p _ { 0 } , q _ { 0 } ) } ) } \\ & & { -  P _ { 1 } ^ { * } ( c ( p _ { 0 } , q _ { 0 } ) + T _ { 1 } ( q _ { 0 } ) ^ { T } \nabla U ( q _ { 0 } , 0 ) ) + r } \end{array}
$$

with the remainder $r ( p _ { 0 } , q _ { 0 } , P _ { 1 } \eta , Q _ { 1 } \eta ) = \mathcal { O } ( \varepsilon ) .$

Adiabatic Invariants.Fora solutionwith bounded energy,both $p _ { 1 } ( t )$ and $q _ { 1 } ( t )$ in (3.12)are of size $\mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ and hence

$$
\eta ( t ) = \mathcal { O } ( 1 ) .
$$

Wenow integrate both sides of the above differential equation from Oto $t$ The integral of the terms in (3.19)is $\mathcal { O } ( \varepsilon )$ ,asisseen bypartial integration since $P _ { 1 } ^ { * } ( t )$ is oscillatory with an $\mathcal { O } ( \varepsilon )$ integral and $p _ { 0 } , q _ { 0 }$ havebounded derivatives.

Wenow suppose that the eigenfrequencies $\omega _ { j } ( t ) : = \omega _ { j } ( q _ { 0 } ( t ) )$ remain separated and bounded away from $_ 0$ thereisaconstant $\delta > 0$ such that for any pair $\omega _ { j } ( t )$ and $\omega _ { k } ( t )$ with $j \neq k$ ,thelower bounds

$$
| \omega _ { j } ( t ) - \omega _ { k } ( t ) | \geq \delta , \quad \ \omega _ { j } ( t ) \geq \frac { \delta } { 2 }
$$

hold for all $t$ underconsideration.In this situation,asin Sect.XIV.2.1,the integral from0to $t$ of the term(3.17） is bounded by $\mathcal { O } ( \varepsilon )$ ,since the matrix $W$ has zero diagonal.

Itremains to study the term(3.18）with the bilinear functions $^ a$ and $b$ This termhas only oscillatory components if the following non-resonance condition is satisfied:for all $j , k , l$ andall combinations of signs,

$$
| \omega _ { j } ( t ) \pm \omega _ { k } ( t ) \pm \omega _ { l } ( t ) | \geq \delta
$$

with a positive $\delta$ independent of $\boldsymbol { \varepsilon } .$ In this case,also the integral over the term(3.18) is of size $\mathcal { O } ( \varepsilon )$ ,andwe obtain

$$
\eta ( t ) = \eta ( 0 ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

If condition (3.21) is weakened torequiring thatfor all $j , k , l = 1 , \ldots , m$

$$
\omega _ { j } ( t ) \pm \omega _ { k } ( t ) \pm \omega _ { l } ( t ) \ \mathrm { h a s ~ a ~ f i n i t e ~ n u m b e r ~ o f ~ a t ~ m o s t ~ s i m p l e ~ z e r o s }
$$

inthe considered time interval,then the estimate deteriorates to (see Exercise1)

$$
\eta ( t ) = \eta ( 0 ) + { \cal O } ( \varepsilon ^ { 1 / 2 } ) \mathrm { f o r } t \leq \mathrm { C o n s t } .
$$

Theactions

$$
I _ { j } = | \eta _ { j } | ^ { 2 } \qquad ( j = 1 , \ldots , m )
$$

are thus adiabatic invariants:

$$
I _ { j } ( t ) = I _ { j } ( 0 ) + \mathcal { O } ( \varepsilon ) \mathrm { f o r } t \leq \mathrm { C o n s t } .
$$

in case of (3.22),andupto $\mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ in case of (3.24).

The Slow System.Since the oscillatory energy equals

$$
\frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( q _ { 0 } ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( q _ { 0 } ) q _ { 1 } = \sum _ { j = 1 } ^ { m } I _ { j } \omega _ { j } ( q _ { 0 } ) ,
$$

thedifferential equations (3.12)fortheslow variables $p _ { 0 } , q _ { 0 }$ become,up to $\mathcal { O } ( \varepsilon )$

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { \displaystyle - \nabla _ { g _ { 0 } } \Big ( \frac { 1 } { 2 } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + U ( q _ { 0 } , 0 ) \Big ) - \sum _ { j = 1 } ^ { m } I _ { j } \nabla _ { q _ { 0 } } \omega _ { j } ( q _ { 0 } ) } \\ { \dot { q } _ { 0 } } & { = } & { \displaystyle M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } . } \end{array}
$$

Compared with the constrained system with Hamiltonian ${ \scriptstyle { \frac { 1 } { 2 } } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q )$ on the configuration manifold $\nu$ ,the slow motion is thus driven by the additional potential $\textstyle \sum _ { j = 1 } ^ { m } I _ { j } \omega _ { j } ( q _ { 0 } )$ depending on the actions $I _ { j }$ See alsoRubin&Ungar (1957), Takens(198O),and Bornemann (1998) for different derivationsand discussions ofthe correction potential.

Avoided Crossing of Frequencies and Takens Chaos.If the distance $\delta$ of frequenciesin(3.2o) becomes so small at apoint $q _ { 0 } ( t )$ that $\delta ^ { 2 } \ \leq \varepsilon$ ,thentherecan again occur $\mathcal { O } ( 1 )$ changesin adiabatic invariants $I _ { j }$ ,asinthe Zener example of Sect.XIV.1.1.In the present situation of solution-dependent frequencies,however, the level to which $I _ { j }$ jumpsafter the avoided crossing,depends very sensitively on the slow solution variables $q _ { 0 } ( t )$ through the terms $\exp ( \pm \frac { i } { \varepsilon } \Phi )$ in (3.17).In turn,the slow motion of $\mathit { p } _ { 0 } , q _ { 0 }$ afterthe avoided crossing depends on the new values of $I _ { j }$ through(3.27).The effect is that the slow motion depends very sensitively on perturbations of the initial values in the case of an avoided crossing;see Takens(1980). The indeterminacy of the slow motion in the limit $\varepsilon \to 0$ istermed Takens chaos by Bornemann（1998）.

# XIV.3.3 Integratorsin Adiabatic Variables

Along-time-step integrator for the oscillatory mechanical system with Hamiltonian (3.1)can now be obtained as follows:

Solve the slow system(3.27)intandem with applyinganadiabatic integrator (see Sect.XIV.1.2) toasimplified equation for theadiabatic variables,

$$
\dot { \eta } = \exp \Bigl ( - \frac { i } { \varepsilon } \Phi \Bigr ) W \exp \Bigl ( \frac { i } { \varepsilon } \Phi \Bigr ) \eta ,
$$

where $W$ is given by(3.16)withasimplified matrix $L :$ with $v _ { 0 } = M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 }$ ,let

$$
L ( p _ { 0 } , q _ { 0 } ) = - \Omega ( q _ { 0 } ) ^ { 1 / 2 } \left. \frac { d } { d \tau } \right| _ { \tau = 0 } Q ( q _ { 0 } + \tau v _ { 0 } ) ^ { T } Q ( q _ { 0 } ) \Omega ( q _ { 0 } ) ^ { - 1 / 2 } .
$$

Thismatrix $L$ captures the principal terms,coming from the matrix $X _ { 0 1 }$ in (3.8）, whichare responsible fora change of theadiabatic invariants dueto anavoided crossing as long as the frequency separation condition (3.2O) holdswith apossibly $\boldsymbol { \mathsf { E } }$ -dependent $\delta \gg \varepsilon$ ,e.g.,with $\delta \sim \varepsilon ^ { 1 / 2 }$ where $O ( 1 )$ changes occur in the adiabatic invariants.Because of the Takens chaos,itcannot beexpected that such an integrator yieldsagood approximation to“the”solution,butthe method can approximate analmost-solution (havinga small defectin the differential equations）that passes through the avoided crossing zone,and itdetects the change of adiabatic invariants. The properties of integrators of this type are currently under investigation (Lorenz &Lubich 2006).

Further we refer to Jahnke(2O03,2Oo4b) for theconstruction and analysis of adiabatic integrators for mixed quantum-classical molecular dynamics,where similarlyanonlinearcoupling of slow and fast,oscillatory motions occurs.

# XIV.3.4 Analysis of Multiple Time-SteppingMethods

The errorbehaviour of the impulseandmolified impulsemethod applied toan oscillatory Hamiltonian system(3.1）withwell-separated frequenciescan beanalysed intheadiabaticvariables in the samewayaswedidin Sections XIV.2.3and XIV.2.4 for the case of time-dependent frequencies.Analogous formulas and the same conclusions hold;essentially we need to replace the argument $t$ by $q _ { 0 }$ in the appearing functions.However,their behaviour in the situation ofan avoided crossingwith Takenschaos is presently not understood.

# XIV.4 Exercises

1.Show that

$$
\int _ { 0 } ^ { t } \exp \Big ( \frac { i } { \varepsilon } \phi ( s ) \Big ) d s = \mathcal { O } ( \varepsilon ^ { 1 / ( m + 1 ) } )
$$

if $\lambda : = \dot { \phi }$ has finitely many zeros of orderatmost $m$ in the interval $[ 0 , t ]$

Hint:Use the methodof stationary phase;see,e.g.,Olver(1974) or van der Corput (1934).

2.Show that the adiabatic variables $\eta ( t )$ of（1.4）remain approximately constant also in the following cases of non-separated eigenvalues:

（a）amultiple eigenvalue $\lambda _ { j } ( t )$ of constant multiplicity $m$ forall $t$ and the orthogonal basis $v _ { j , 1 } ( t ) , \ldots , v _ { j , m } ( t )$ ofthe corresponding eigenspace chosen such that the derivatives $\dot { v } _ { j , l } ( t )$ areorthogonal to the eigenspace forall $t$ ;

(b)acrossing of eigenvalues, $\lambda _ { j } ( t _ { * } ) = \lambda _ { k } ( t _ { * } )$ with $\dot { \lambda } _ { j } ( t _ { * } ) \neq \dot { \lambda } _ { k } ( t _ { * } )$ ,forwhich theeigenvectors are smooth functions of $t$ inaneighbourhood of $t _ { * }$ ;seealso Born&Fock（1928） for crossingswhere $\lambda _ { j } ~ - ~ \lambda _ { k }$ can have zeros of higher multiplicity.

3.Let the differential equation（1.1） with smooth skew-hermitian $Z ( t )$ be transformed locally over $[ t _ { 0 } , t _ { 0 } + h ]$ to $\begin{array} { r } { z ( t ) = \exp ( - \frac { t } { \varepsilon } Z _ { * } ) y ( t ) } \end{array}$ ,sothat

$$
\dot { z } = \frac { 1 } { \varepsilon } \exp ( - \frac { t } { \varepsilon } Z _ { * } ) \left( Z ( t ) - Z _ { * } \right) \exp ( \frac { t } { \varepsilon } Z _ { * } ) z
$$

with $Z _ { * } = Z ( t _ { 0 } + h / 2 ) $ Consider the averaged midpoint rule

$$
z _ { 1 } = z _ { 0 } + \frac { 1 } { \varepsilon } \int _ { 0 } ^ { h } \exp ( - \frac { s } { \varepsilon } Z _ { \star } ) \left( \widetilde { Z } ( s ) - Z _ { \star } \right) \exp ( \frac { s } { \varepsilon } Z _ { \star } ) d s \ \frac { 1 } { 2 } ( z _ { 0 } + z _ { 1 } ) ,
$$

where $Z ( t )$ is thequadratic interpolation polynomial through $Z ( t _ { 0 } )$ , $Z _ { * }$ , $Z ( t _ { 1 } )$ . Show that the local error $z _ { 1 } - z ( t _ { 1 } )$ is of size $\mathcal { O } ( h ^ { 4 } / \varepsilon ^ { 2 } )$ ,whichis $\mathcal { O } ( h ^ { 2 } )$ only for $h = { \mathcal { O } } ( \varepsilon )$ .Explainwhy the error bound cannot be improved to $\mathcal { O } ( h ^ { 2 } )$ for $h = \mathcal { O } ( \varepsilon ^ { \alpha } )$ with $\alpha < 1$ .

Hint:See the proofs of Theorems2.1(i）and 3.1 in Hochbruck& Lubich (1999b),cf.alsoIserles(2004).

4.In the situation of the previous exercise,let $U$ beaunitary matrix of eigenvectorsof $Z _ { * }$ ,andlet $\tilde { D } ( t )$ be the diagonal matrix containing the diagonal entries of ${ \cal U } ^ { * } \big ( \tilde { Z } ( t ) - Z _ { * } \big ) { \cal U } .$ Findamodification of the above averaged midpoint rule by terms that use only $\bar { D } ( t )$ ,such that the local error is $\mathcal { O } ( h ^ { 2 } )$ for $h \leq \varepsilon ^ { 3 / 4 }$ if the eigenvalues of $Z _ { * }$ areallseparatedbyadistance $\delta$ independent of $\varepsilon$ .

5.Compare the error behaviour of the averaged midpoint rules (1.12) and (4.1) nearthe avoided crossing of the eigenvalues in the Zener matrix(1.9).

6.Formulate symmetric modifications of the adiabatic integrators(1.12）and (1.13)that use function evaluations at the grid points $t _ { n }$ and $t _ { n + 1 }$ instead of $t _ { n + 1 / 2 }$

7.Consider the differential equation $\dot { y } = f ( y ) + g ( t )$ with a smooth function $f ( y )$ anda function $g ( t ) = \mathcal { O } ( 1 )$ with $\dot { g } ( t ) = \mathcal { O } ( \delta ^ { - 1 } )$ with respect toa small parameter $\delta .$ Forthe modified midpoint rule

$$
y _ { 1 } = y _ { 0 } + h f \Big ( \frac { y _ { 0 } + y _ { 1 } } { 2 } \Big ) + \int _ { t _ { 0 } } ^ { t _ { 1 } } g ( t ) d t ,
$$

showthat the localerror satisfies $y _ { 1 } - y ( t _ { 1 } ) = \mathcal { O } ( h ^ { 3 } / \delta )$

8.Write theHamiltonian system(XIII.9.2)in adiabatic variables and relate this tc thefirst terms of the modulated Fourier expansion.

9.Compare the impulse method of Sect.XIV.2.3 with the method based on the splitting

$$
H = { \Big ( } { \frac { 1 } { 2 } } p ^ { T } M ( t ) ^ { - 1 } p + { \frac { 1 } { 2 \varepsilon ^ { 2 } } } q ^ { T } A ( t ) q { \Big ) } + { \Big ( } U ( q , t ) + E { \Big ) } .
$$

10.Show that Theorem2.6 remainsvalid for thechoice ${ \mathbfcal { S } } ( t ) = 0$ in(2.37）.This correspondsto the projection to the constraint manifold in the mollified impulse methodasproposed by Izaguirre,Reich&Skeel(1999).
