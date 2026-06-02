# Chapter XII. Dissipatively Perturbed Hamiltonian and Reversible Systems

Symplecticintegrators also show a favourablelong-timebehaviour when theyare applied to non-Hamiltonian perturbations ofHamiltonian systems.The same is true forsymmetric methods applied to non-reversible perturbations of reversible systems.In thischapter we study the behaviour of numerical integrators when theyare applied todissipative perturbations of integrablesystems,where only one invariant toruspersistsunder theperturbationand becomesweaklyattractive.The simplest exampleof suchasystemisVanderPol's equationwith small parameter,which has asingle limit cyclein contrast to the infinitely many periodic orbits of theunperturbed harmonic oscillator.

# XII.1 Numerical Experimentswith Van der Pol's Equation

One of the first such methods is the method of Van-der-Pol.[...] It should, however,benotedthatintheformulation givenby Van-der-Pol,approximation was effected by simple intuitive reasonings.

(N.N.Bogoliubov&Y.A.Mitropolski1961,p.10f.)

Consider Van der Pol'sequation

$$
\begin{array} { l } { { \dot { p } ~ = ~ - q + \varepsilon ( 1 - q ^ { 2 } ) p } } \\ { { \dot { q } ~ = ~ p } } \end{array}
$$

with small positive $\boldsymbol { \varepsilon }$ ,which isaperturbation of the harmonic oscillator.A symplectic change to polar coordinates $p = { \sqrt { 2 a } } \cos \theta , q = { \sqrt { 2 a } } \sin \theta$ puts the system into theform

$$
\begin{array} { r c l } { { \dot { a } } } & { { = } } & { { \varepsilon 2 a \cos ^ { 2 } \theta ( 1 - 2 a \sin ^ { 2 } \theta ) } } \\ { { } } & { { \dot { \theta } } } & { { = 1 + \varepsilon \cos \theta \sin \theta ( 1 - 2 a \sin ^ { 2 } \theta ) . } } \end{array}
$$

Since the angle $\theta$ evolves much faster than $a$ ,wemay expect that the averaged system,which replacesthe right-hand side functions by theirangularaverages,gives a good approximation:

$$
\begin{array} { l } { { \dot { a } { \bf \varphi } = \varepsilon a ( 1 - { \frac { 1 } { 2 } } a ) } } \\ { { \dot { \theta } { \bf \varphi } = { \bf \varphi } 1 . } } \end{array}
$$

Approximatingbytheaveraged equationis the“methodof Van-der-Pol”cited above,andthebeliefinthe long-timevalidity of suchanapproximation isthe averagingprinciple.Theaverageddifferential equation for $a$ hasanunstable equilibrium atzero,and an asymptotically stable equilibrium at $a ^ { * } = 2$ Theaveraged system therefore has the circle $\{ a ^ { * } = 2 , \theta \in \mathbb { R }$ mod $2 \pi \}$ asanattractive limit cycle.This suggests that the original Vander Pol equation hasa nearbylimitcycle,which is indeed the case.

Following the numerical experiment ofHairer&Lubich(1999),we solve the equation（1.1） with two initial values, $( p _ { 0 } , q _ { 0 } ) = ( 0 , 1 . 3 )$ and $( p _ { 0 } , q _ { 0 } ) = ( 0 , 2 . 7 )$ , andwith three numerical methods:the non-symplectic explicit and implicit Euler methods,and thesymplectic Eulermethod.Allof them have order1.The numerical resultsaredisplayedin Fig.1.1.For large stepsizes(compared to theperturbation parameter $\varepsilon$ ）,thenon-symplectic methods give a completelywrongnumerical solution,whereas that of thesymplecticmethod isqualitativelycorrect.Forsmaller step sizes,the numerical solutions of the non-symplectic methodsalso show a limit cycle.

Forthe moment we explain these observations by"simple intuitive reasonings”, thatis,by theaveragingprincipleand formal backward erroranalysis.The rigorous treatment isdeveloped in thecourse of thischapter inamore general framework of perturbed integrable systems.

Foradifferential equation

$$
\dot { y } = f ( y ) + \varepsilon g ( y ) ,
$$

the numerical solution $y _ { n }$ obtained by the explicit Euler method is the(formally) exact solution of amodified differential equation

$$
\begin{array} { r } { \dot { \boldsymbol { \tilde { y } } } = \boldsymbol { f } ( \boldsymbol { \tilde { y } } ) + \varepsilon \boldsymbol { g } ( \boldsymbol { \tilde { y } } ) = \frac { 1 } { 2 } h \boldsymbol { f ^ { \prime } } ( \boldsymbol { \tilde { y } } ) \boldsymbol { f } ( \boldsymbol { \tilde { y } } ) + \mathcal { O } ( h ^ { 2 } + \varepsilon h ) , } \end{array}
$$

Forthe Van der Pol equation in the above coordinates,the averaged modified equation becomes

$$
\begin{array} { r } { \dot { \tilde { a } } = h \tilde { a } + \varepsilon \tilde { a } ( 1 - \frac { 1 } { 2 } \tilde { a } ) + \dots . } \end{array}
$$

which has approximately $\tilde { a } = 2 + 2 h / \varepsilon$ asanequilibrium.Hence,the limitcycleofthe numerical solution of theexplicit Euler method has approximateradius $2 \sqrt { 1 + h / \varepsilon }$ (Fig.1.1）which is far from the correct value unless $h \ll \varepsilon$ .

The implicit Euler discretization isadjoint to the explicit Euler method.Therefore,its modified differential equation is as above with $h$ replaced by $- h$ Inthis case,theradius of thelimit cycle is approximately $2 { \sqrt { 1 - h / \varepsilon } }$ (for $h < \varepsilon$ ),which againagreesverywellwith thepictures ofFig.1.1.

Forthesymplectic Eulermethod,themodified differential equation for Van der Pol's equation is

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0007_pages_0421-0490/auto/images/be2bd9d01dd762c6086c97567efd0279fe342bcf0f1355d0ae3c0fe28126b86e.jpg)  
Fig.1.1.Numerical experimentswith Van der Pol's equation (1.1), $\varepsilon = 0 . 0 5$

$$
\begin{array} { l } { { \dot { \widetilde { p } } ~ = ~ - \widetilde { q } + \varepsilon ( 1 - \widetilde { q } ^ { 2 } ) \widetilde { p } + \frac 1 2 h \widetilde { p } + O ( h ^ { 2 } + \varepsilon h ) } } \\ { { \dot { \widetilde { q } } ~ = ~ \widetilde { p } - \frac 1 2 h \widetilde { q } + O ( h ^ { 2 } + \varepsilon h ) . } } \end{array}
$$

Here,the modified differential equation for theunperturbed harmonic oscillator is Hamiltonian(Theorem IX.3.1),and so all $\varepsilon$ -independent termsin theaveraged modified equation vanish:

$$
\int _ { 0 } ^ { 2 \pi } { \frac { \partial H _ { j } } { \partial \theta } } ( a , \theta ) d \theta = 0 .
$$

Therefore,theradius of the limit cycleis of size $2 + \mathcal { O } ( h )$ in accordance with Fig.1.1.

# XI1.2 Averaging Transformations

Leprobleme des oscillations non lineairesa actuellement une grande importance dans les domaines les plus divers de la technique et dela physique.Parmi les methodes analytiques d'étude des oscillationsnon linéaires,lamethode asymptotique de developpement en serie parrapportaun parametre petit est particulierement efficace.Touteune série demonographiespubliees en 1930-1938 par N.Krylov et N.Bogolioubov tant en russe qu'en francais ont eté consacréesa cette question,malheureusement ces ouvrages sont devenus aujourd'hui desraretés bibliographiques.Parailleurslesmethodes exposees ont étélargement developpeesdepuis. (N.Bogolioubov&I.Mitropolski 1962,prefaceala traduction francaise)

In this section we consider rather general perturbations of integrable systems.We studytransformations that eliminate the dependence on the anglesin the perturbation functions,upto arbitrary powers of the small perturbation parameter.The construction and properties of these“averaging”transformationsare obtained by a slight extension of the arguments in Sections X.2 and XI.2.

# XI.2.1 The Basic Scheme of Averaging

Asin Sections X.2.1 and XI.2.1,we consider perturbations of an integrable system written in action-angle variables:

$$
\begin{array} { r l r } { \dot { a } } & { = } & { \varepsilon r ( a , \theta ) } \\ { \dot { \theta } } & { = } & { \omega ( a ) + \varepsilon \rho ( a , \theta ) } \end{array}
$$

where $\varepsilon$ isasmall parameterand $T , \rho$ arereal-analyticinaneighbourhood of $\{ a ^ { * } \} \times$ $\mathbb { T } ^ { d }$ Unlikethesituation of the previouschapters,wedo not imposeconditions that make theangular average

$$
\overline { { r } } ( a ) = \frac { 1 } { ( 2 \pi ) ^ { d } } \int _ {  { \mathbb { T } } ^ { d } } r ( a , \theta ) d \theta
$$

vanishidentically.We look fora transformation to newvariables $( b , \varphi )$ ,of the form

$$
\begin{array} { l } { { a \ = \ b + \varepsilon s ( b , \varphi ) } } \\ { { \theta \ = \ \varphi + \varepsilon \sigma ( b , \varphi ) , } } \end{array}
$$

which eliminates thedependence on theangles in the $\mathcal { O } ( \varepsilon )$ terms of(2.1）:

$$
\begin{array} { l } { \dot { b } = \varepsilon m ( b ) + { \mathcal O } ( \varepsilon ^ { 2 } ) } \\ { \dot { \varphi } = \omega ( b ) + \varepsilon \mu ( b ) + { \mathcal O } ( \varepsilon ^ { 2 } ) . } \end{array}
$$

This is just aminor modification of the problem in Sect.XI.2.1.The equations that sand $\sigma$ mustsatisfy,differfrom(XI.2.5)and(XI.2.6)onlyin thattheright-hand side $r ( b , \varphi )$ of(XI.2.5) is replaced by $r ( b , \varphi ) - m ( b )$ ,viz.,

$$
\begin{array} { l } { { \displaystyle \frac { \partial s } { \partial \varphi } ( b , \varphi ) \omega ( b ) = r ( b , \varphi ) - m ( b ) } } \\ { { \displaystyle \frac { \partial \sigma } { \partial \varphi } ( b , \varphi ) \omega ( b ) = \rho ( b , \varphi ) + \omega ^ { \prime } ( b ) s ( b , \varphi ) - \mu ( b ) . } } \end{array}
$$

Necessary conditions for solvability are now

$$
m ( b ) = \overline { { { r } } } ( b ) \ , \quad \mu ( b ) = \overline { { { \rho } } } ( b ) \ ,
$$

where the second equation corresponds to the choice ${ \overline { { s } } } ( b ) = 0$ In other words,the leading terms in (2.4) are the angular averages of the perturbations in (2.1).

The equations (2.5),(2.6) are solvable for $b ~ = ~ b ^ { * }$ if $\omega ( b ^ { * } )$ satisfies the diophantine condition (X.2.4).The“ultraviolet cutoff”argument of the proof ofLemmaX.2.1 then shows that(2.4） holds uniformly as longas the solution remainsin theball $\lVert b - b ^ { * } \rVert \leq c \lvert \log \varepsilon \rvert ^ { - \nu - 1 }$ ,withasufficiently small constant $c$ Thismay hold overavery long time interval if the equation $\boldsymbol { b } = \varepsilon m ( \boldsymbol { b } )$ hasastable equilibrium in that ball.

# XII.2.2 Perturbation Series

Asin Sections X.2.2and XI.2.2,theabove construction extends to arbitrary finite orderin $\uplus$ Atransformation of the form(XI.2.9),which eliminates theanglesinall terms up to order $\varepsilon ^ { N - 1 }$ ,issought for:

$$
\begin{array} { r l r } { \dot { b } } & { = } & { \varepsilon m _ { 1 } ( b ) + \varepsilon ^ { 2 } m _ { 2 } ( b ) + \ldots + \varepsilon ^ { N - 1 } m _ { N - 1 } ( b ) + \varepsilon ^ { N } r _ { N } ( b , \varphi ) } \\ { \dot { \varphi } } & { = } & { \omega ( b ) + \varepsilon \mu _ { 1 } ( b ) + \varepsilon ^ { 2 } \mu _ { 2 } ( b ) + \ldots + \varepsilon ^ { N - 1 } \mu _ { N - 1 } ( b ) + \varepsilon ^ { N } \rho _ { N } ( b , \varphi ) . } \end{array}
$$

The equations determining the transformation are a slight modification of(XI.2.11) and(XI.2.12):on the right-hand side of(XI.2.11), $p _ { j } ( b , \varphi )$ isreplaced by thedifference $p _ { j } ( b , \varphi ) - m _ { j } ( b )$ ,with $m _ { j } ( b ) = \overline { { p } } _ { j } ( b )$ Wethen have the following variant of LemmasX.2.1 and XI.2.1.

Lemma2.1.Let theright-hand side functions of(2.1) bereal-analytic ina neighbourhood of $\{ b ^ { * } \} \times \mathbb { T } ^ { d }$ Suppose that $\omega ( b ^ { * } )$ satisfies the diophantine condition (X.2.4)with exponent v.For any fixed $N \geq 2$ ,therearepositiveconstants $\varepsilon _ { 0 } , c , C$ such that thefollowing holdsfor $| \varepsilon | \leq \varepsilon _ { 0 }$ :thereexistsareal-analyticchangeof coordinates $( a , \theta ) \mapsto ( b , \varphi )$ whichtransforms(2.1）to(2.8)with

$$
\begin{array} { r l } & { \| m _ { j } ( b ) \| \leq C / \delta ^ { j - 1 } \mathrm { , } \quad \quad \| \mu _ { j } ( b ) \| \leq C / \delta ^ { j - 1 } } \\ & { \| r _ { N } ( b , \varphi ) \| \leq C / \delta ^ { N - 1 } \mathrm { , } \quad \| \rho _ { N } ( b , \varphi ) \| \leq C / \delta ^ { N - 1 } } \end{array} \quad \begin{array} { r l } & { f o r \quad \| b - b ^ { * } \| \leq \delta \mathrm { , } } \\ & { f o r \quad \| b - b ^ { * } \| \leq \delta \mathrm { , } } \end{array}
$$

where

$$
\delta = c | \log \varepsilon | ^ { - \nu - 1 } .
$$

Moreover,thetransformationis $\mathcal { O } ( \varepsilon )$ -closetotheidentity: $\| ( a , \theta ) - ( b , \varphi ) \| \leq C \varepsilon$ holdsfor $( a , \theta )$ and $( b , \varphi )$ relatedbytheabovecoordinate transform,for $\| b - b ^ { * } \| \leq$ $\delta$ andfor $\varphi$ inan $\boldsymbol { \varepsilon }$ -independentcomplexneighbourhoodof $\mathbb { T } ^ { d }$ .

The constants $\varepsilon _ { 0 } , c , C$ dependon $N , d , \gamma , \nu$ andonboundsof $\boldsymbol { \omega }$ , $\gamma _ { i }$ ponacomplexneighbourhoodof $\{ b ^ { * } \} \times \mathbb { T } ^ { d }$ .

Proof. The proof usesagain the ultraviolet cutoff argument of the proof of LemmaX.2.1.This makesall the functions $s _ { i } , \sigma _ { i } , m _ { i } , \mu _ { i }$ real-analyticin $b$ for $\| b - b ^ { * } \| \leq$ $2 \delta$ andof $\varphi$ inan $\boldsymbol { \varepsilon }$ -independent complex neighbourhoodof $\mathbb { T } ^ { d }$ Thepowers of $\delta$ in thedenominators of the estimates come from the presence of terms $\partial s _ { j } / \partial b$ ， $\partial \sigma _ { j } / \partial b$ in $p _ { i } ( b , \varphi )$ and $\pi _ { i } ( b , \varphi )$ of(XI.2.11） and(XI.2.12）and from Cauchy'sestimates applied to $s _ { j }$ , $\sigma _ { j }$ on $\| b - b ^ { * } \| \leq 2 \delta$ . □

# XII.3Attractive Invariant Manifolds

Theorems on invariant manifolds formapshavebeen proved many times formanydifferent settings.The firstresultswere obtained byHadamard （1901）andPerron(1929).[...]Ouraimwastoderiveaglobal invariant manifoldresultwith conditionsthat areeasy toverify fortheapplications inmind. （K.Nipp&D.Stoffer1992）

Inthis section we give results on the existence and properties of attractive invariantmanifolds of maps,with avery explicit handling ofconstants.These resultsare duetoKirchgraber,Lasagni,Nipp& Stoffer（1991）and Nipp& Stoffer（1992). Theywill allowus tounderstand the weakly attractive closed curves that we observed in Sect.XI.1.Beyond that particular example,theseresultsare extremely useful for studying the long-time behaviour of numerical discretizations inagreat variety ofapplications;seeNipp&Stoffer（1995,1996)and Lubich（2001）and references therein,and also Stuart&Humphries(1996) forarelated invariantmanifold theorem and itsuse inanalyzing the dynamics of numerical integrators for non-conservative problems.

Consideramap $\phi : X \times Y \to X \times Y$ defined on the Cartesian product ofa Banach space $X$ anda closed bounded subset $Y$ ofanother Banach space.We write $\boldsymbol { \varPhi } ( x , y ) = ( \widehat { x } , \widehat { y } )$ with

$$
\begin{array} { r } { \widehat { \boldsymbol { x } } \ = \ \boldsymbol { x } + \boldsymbol { f } ( \boldsymbol { x } , \boldsymbol { y } ) } \\ { \widehat { \boldsymbol { y } } \ = \ \boldsymbol { g } ( \boldsymbol { x } , \boldsymbol { y } ) . } \end{array}
$$

We assume that $f$ and $g$ are Lipschitz bounded.with Lipschitz constants $L _ { x x }$ , $L _ { x y }$ and $L _ { y x }$ , $L _ { y y }$ with respect to $x$ , $y$ .If these Lipschitz constantsare sufficiently small, then the map $\phi$ hasanattractive invariant manifold.More precisely,thereis the followingresult,stated without proofby Kirchgraber,Lasagni,Nipp& Stoffer（1991） and provedinamore general settingbyNipp& Stoffer(1992).

Theorem3.1.In the above situation,if

$$
L _ { x x } + L _ { y y } + 2 \sqrt { L _ { x y } L _ { y x } } < 1 ,
$$

thenthereexistsafunction $s : X \to Y$ ,whichisLipschitzboundedwiththeconstant $\lambda = 2 L _ { y x } / ( 1 - L _ { x x } - L _ { y y } )$ ,such that

$$
\mathcal { M } = \left\{ ( x , s ( x ) ) : x \in X \right\} \ i s \ i n { \nu } a r i a n t \ u n d e r \ \varPhi .
$$

$\mathcal { M }$ attractsorbits of $\phi$ withtheatractivityfactor $\rho = \lambda L _ { x y } + L _ { y y } < 1$ ,thatis, $\| \widehat { y } - s ( \widehat { x } ) \| \leq \rho \| y - s ( x ) \|$ holdsforall $( x , y ) \in X \times Y$ .

Proof.(a)We search fora function $s : X \to Y$ such that for $( \widehat { x } , \widehat { y } ) = \varPhi ( x , y )$ ,the relation $y = s ( x )$ implies also ${ \widehat { y } } = s ( { \widehat { x } } )$ Foran arbitrary function $\sigma : X  Y$ , we first study which relation holds between $\overrightharpoon { x }$ and $\hat { y }$ if $y = \sigma ( x )$ Towrite $\widehat { y }$ as a function of $\overrightharpoon { x }$ ,weneed a bijective correspondence between $x$ and $\widehat { x }$ via the first equation of(3.1).Bythe Banach fixed-point theorem,the equation

$$
\widehat { x } = x + f ( x , \sigma ( x ) ) \mathrm { ~ h a s ~ a ~ u n i q u e ~ s o l u t i o n ~ } x = u _ { \sigma } ( \widehat { x } )
$$

forevery ${ \mathcal { X } } \in X$ if $x \mapsto f ( x , \sigma ( x ) )$ isacontraction.This is thecase if $o$ hasthe Lipschitz constant $\lambda$ and

$$
L _ { x x } + L _ { x y } \lambda < 1 .
$$

We then obtain ${ \widehat { y } } = { \widehat { \sigma } } ( { \widehat { x } } )$ from the following scheme:

$$
\begin{array} { l c l } { { x = u _ { \sigma } ( \widehat { x } ) \quad } } & { { \longleftarrow } } & { { \widehat { x } } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \vphantom { \int _ { \sigma } \int _ { x } \prod _ { j = 1 } ^ { x } \prod _ { j = 1 } ^ { j } \prod _ { i = j } ^ { j } \prod _ { j = i } ^ { j } \prod _ { j = j } ^ { j } \prod _ { i = j + 1 } ^ { j } } } } \\ { { } } & { { } } & { { } } \\ { { y = \sigma ( x ) \quad } } & { { \longrightarrow \quad } } & { { \widehat { y } = g ( x , y ) } } \end{array}
$$

That is,we set $\boldsymbol { \hat { y } } = \boldsymbol { \hat { \sigma } } ( \boldsymbol { \hat { x } } ) = g ( u _ { \sigma } ( \boldsymbol { \hat { x } } ) , \sigma ( u _ { \sigma } ( \boldsymbol { \hat { x } } ) ) ) .$ By construction, $( \widehat { x } , \widehat { y } ) = \varPhi ( x , y ) .$ Undercondition(3.3）,the function $u _ { \sigma } : X \to X$ isLipschitz bounded by $\mu =$ $1 / ( 1 - L _ { x x } - L _ { x y } \lambda )$ .Consequently,the function $\widehat { \sigma } : X  Y$ is Lipschitz bounded by $( L _ { y x } + L _ { y y } \lambda ) \mu .$ The condition that the transformed function $\widehat { \sigma }$ is again Lipschitz boundedby the same $\lambda$ as $\sigma$ ,thereforereads

$$
\frac { L _ { y x } + L _ { y y } \lambda } { 1 - L _ { x x } - L _ { x y } \lambda } \leq \lambda ,
$$

orequivalently,

$$
L _ { x y } \lambda ^ { 2 } - ( 1 - L _ { x x } - L _ { y y } ) \lambda + L _ { y x } \le 0 .
$$

Under condition (3.2),there existsanon-emptyreal interval of values $\lambda$ satisfying thisquadratic inequality.In particular,(3.4） then holds for

$$
\lambda = \frac { 2 L _ { y x } } { 1 - L _ { x x } - L _ { y y } } .
$$

(This is close to thesmallestpossible valueof $\lambda$ if $2 \sqrt { L _ { x y } L _ { y x } } \ll 1 - L _ { x x } - L _ { y y } . )$ It is easily checked that (3.2)and (3.5) imply (3.3).

Underconditions (3.3)and(3.4),the transformation $H : \sigma \mapsto { \widehat { \sigma } }$ ,which is called aHadamardgraph transform,mapsthe setof functions

$$
S = \{ \sigma : X \to Y | \ \sigma { \mathrm { ~ i s ~ L i p s c h i t z ~ b o u n d e d ~ b y ~ } } \lambda \}
$$

into itself,i.e.,

$$
H : S \to S : \sigma \mapsto { \widehat { \sigma } } .
$$

3 $S$ is a closed subset of $C ( X , Y )$ ,theBanach space of continuous functions from $X$ to the bounded closed set $Y$ ,equipped with the supremum norm $\| \sigma \| _ { \infty } =$ $\operatorname { s u p } _ { x \in X } \| \sigma ( x ) \|$ If $H$ isacontraction,then the Banach fixed-point theorem tells usthat there isa unique function $s \in S$ with $\overline { { s } } = \ s$ By construction,this means that if $( { \widehat x } , { \widehat y } ) \ = \ \varPhi ( x , y )$ and $y ~ = ~ s ( x )$ ,thenalso ${ \widehat { \boldsymbol { y } } } = ~ { \boldsymbol { s } } ( { \widehat { \boldsymbol { x } } } )$ Thegraph ${ \mathcal { M } } = \{ ( x , s ( x ) ) : x \in X \}$ isthenan invariant manifold for themap $\phi$ .

（b）We now show that $H$ isalready a contraction under condition (3.2).Let $\sigma _ { 0 } , \sigma _ { 1 }$ be two arbitrary functions in $S$ ,and ${ \widehat { x } } \in X$ .With $x _ { i } = u _ { \sigma _ { i } } ( \widehat { x } )$ ,

$$
\begin{array} { r l } & { \| H \sigma _ { 1 } ( \widehat { x } ) - H \sigma _ { 0 } ( \widehat { x } ) \| = \| g ( x _ { 1 } , \sigma _ { 1 } ( x _ { 1 } ) ) - g ( x _ { 0 } , \sigma _ { 0 } ( x _ { 0 } ) ) \| } \\ & { \le \| g ( x _ { 1 } , \sigma _ { 1 } ( x _ { 1 } ) ) - g ( x _ { 1 } , \sigma _ { 0 } ( x _ { 1 } ) ) \| + \| g ( x _ { 1 } , \sigma _ { 0 } ( x _ { 1 } ) ) - g ( x _ { 0 } , \sigma _ { 0 } ( x _ { 0 } ) ) \| } \\ & { \le L _ { y y } \| \sigma _ { 1 } - \sigma _ { 0 } \| _ { \infty } + ( L _ { y x } + L _ { y y } \lambda ) \| x _ { 1 } - x _ { 0 } \| . } \end{array}
$$

Bydefinition, $\widehat { x } = x _ { i } + f ( x _ { i } , \sigma _ { i } ( x _ { i } ) )$ for $i = 0 , 1$ Subtracting these two equations yieldssimilarly

$$
\begin{array} { r l } & { \| x _ { 1 } - x _ { 0 } \| \leq \| f ( x _ { 1 } , \sigma _ { 1 } ( x _ { 1 } ) ) - f ( x _ { 0 } , \sigma _ { 0 } ( x _ { 0 } ) ) \| } \\ & { \leq \| f ( x _ { 1 } , \sigma _ { 1 } ( x _ { 1 } ) ) - f ( x _ { 1 } , \sigma _ { 0 } ( x _ { 1 } ) ) \| + \| f ( x _ { 1 } , \sigma _ { 0 } ( x _ { 1 } ) ) - f ( x _ { 0 } , \sigma _ { 0 } ( x _ { 0 } ) ) \| } \\ & { \leq L _ { x y } \| \sigma _ { 1 } - \sigma _ { 0 } \| _ { \infty } + \left( L _ { x x } + \bar { L } _ { x y } \lambda \right) \| x _ { 1 } - x _ { 0 } \| _ { * } } \end{array}
$$

Hence,

$$
\left\| x _ { 1 } - x _ { 0 } \right\| \leq \frac { L _ { x y } } { 1 - L _ { x x } - L _ { x y } \lambda } \left\| \sigma _ { 1 } - \sigma _ { 0 } \right\| _ { \infty } .
$$

Combining both inequalitiesand recalling(3.4),we obtain

$$
\begin{array} { r } { \| H \sigma _ { 1 } - H \sigma _ { 0 } \| _ { \infty } \leq ( L _ { y y } + \lambda L _ { x y } ) \| \sigma _ { 1 } - \sigma _ { 0 } \| _ { \infty } . } \end{array}
$$

Since the inequality

$$
L _ { y y } + \lambda L _ { x y } < 1
$$

is satisfied by the $\lambda$ of (3.5)under condition (3.2), $H$ is indeed acontraction.

(c) It remains to show that the invariant manifold $\mathcal { M }$ isattractive.With $( { \widehat { x } } , { \widehat { y } } ) =$ $\varPhi ( x , y )$ ,wewrite

$$
\begin{array} { l } { \widehat { y } - s ( \widehat { x } ) = g ( x , y ) - s ( x + f ( x , y ) ) } \\ { = \Big ( g ( x , y ) - g ( x , s ( x ) ) \Big ) + \Big ( s ( x + f ( x , s ( x ) ) ) - s ( x + f ( x , y ) ) \Big ) . } \end{array}
$$

Here we used the identity

$$
s ( x + f ( x , s ( x ) ) ) = \widehat { s } ( x + f ( x , s ( x ) ) ) = g ( x , s ( x ) ) ,
$$

which holds because $\hat { s } = s$ and by construction of the Hadamard transform.It follows that

$$
\begin{array} { r } { \left\| \widehat { y } - s ( \widehat { x } ) \right\| \leq ( L _ { y y } + \lambda L _ { x y } ) \left\| y - s ( x ) \right\| , } \end{array}
$$

which together with (3.6)yields theresult.

Next we study the effect of aperturbation of the map on the invariant manifold.

Theorem 3.2. Consider maps $\phi _ { 0 }$ , $\phi _ { 1 } : X \times Y \to X \times Y$ both ofwhich satisfy the conditions ofTheorem3.1with the same Lipschitz constants $L _ { x x } , L _ { x y } , L _ { y x } , L _ { y y }$ Let $s _ { 0 }$ and $s _ { 1 }$ bethefunctions definingthe attractive invariant manifolds $\mathcal { M } _ { 0 }$ and $\mathcal { M } _ { \mathrm { 1 } } ,$ respectively.Ifthebound

$$
| | \Phi _ { 1 } ( x , y ) - \varPhi _ { 0 } ( x , y ) | | \leq \delta ~ f o r ~ ( x , y ) \in \mathcal { M } _ { 0 }
$$

holds in the norm $\| ( x , y ) \| = \lambda \| x \| + \| y \|$ on $X \times Y$ ,then

$$
\| s _ { 1 } ( x ) - s _ { 0 } ( x ) \| \leq { \frac { \delta } { 1 - \rho } } ~ f o r ~ x \in X .
$$

(Here $\lambda$ and $\rho$ aredefinedas in Theorem3.1.)

Proof.The proof is similar topart (b) of the previousproof.Let ${ \vec { x } } \in X .$ For $i =$ $0 , 1$ ,wehave $s _ { i } ( { \widehat x } ) = g _ { i } ( x _ { i } , s _ { i } ( x _ { i } ) )$ with $x _ { i }$ defined by the equation $\widehat { x } = x _ { i } +$ $f _ { i } ( x _ { i } , s _ { i } ( x _ { i } ) )$ Weestimate

$$
\begin{array} { r l } { \| s _ { 1 } ( \widehat { x } ) - s _ { 0 } ( \widehat { x } ) \| } & { \leq \ \| g _ { 1 } ( x _ { 1 } , s _ { 1 } ( x _ { 1 } ) ) - g _ { 1 } ( x _ { 1 } , s _ { 0 } ( x _ { 1 } ) ) \| } \\ & { \mp \ \| g _ { 1 } ( x _ { 1 } , s _ { 0 } ( x _ { 1 } ) ) - g _ { 1 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) \| } \\ & { + \ \| g _ { 1 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) - g _ { 0 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) \| } \\ & { \leq \ L _ { y y } \| \bar { s } _ { 1 } - s _ { 0 } \| _ { \infty } + ( L _ { y x } + L _ { y y } \lambda ) \| x _ { 1 } - x _ { 0 } \| } \\ & { + \ \| g _ { 1 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) - g _ { 0 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) \| } \end{array}
$$

and in the same way

$$
\begin{array} { r l } { \| x _ { 1 } - x _ { 0 } \| } & { \leq \| f _ { 1 } ( x _ { 1 } , s _ { 1 } ( x _ { 1 } ) ) - f _ { 1 } ( x _ { 1 } , s _ { 0 } ( x _ { 1 } ) ) \| } \\ & { + \ \| f _ { 1 } ( x _ { 1 } , s _ { 0 } ( x _ { 1 } ) ) - f _ { 1 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) \| } \\ & { + \ \| f _ { 1 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) - f _ { 0 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) \| } \\ & { \leq \ L _ { x y } \| s _ { 1 } - s _ { 0 } \| _ { \infty } + ( L _ { x x } + L _ { x y } \lambda ) \| x _ { 1 } - x _ { 0 } \| } \\ & { + \ \| f _ { 1 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) - f _ { 0 } ( x _ { 0 } , s _ { 0 } ( x _ { 0 } ) ) \| _ { * } } \end{array}
$$

Inserting the second bound into the first one and using(3.4) and the assumed bound on $\phi _ { 1 } - \phi _ { 0 }$ gives

$$
\begin{array} { r } { \| s _ { 1 } - s _ { 0 } \| _ { \infty } \leq ( L _ { y y } + \lambda L _ { x y } ) \| s _ { 1 } - s _ { 0 } \| _ { \infty } + \delta , } \end{array}
$$

which implies the result.

# XII.4WeaklyAttractiveInvariant Tori ofPerturbed IntegrableSystems

Weassume that the perturbation is dissipative such that one torus persists underthe perturbation and gets attractive.

Ouranalysis is done by themethod ofaveraging.Theproblem of this sectionisclassical,seee.g.Bogoliubov&Mitropolski（196l）,Kirchgraber &Stiefel(1978). (D.Stoffer 1998)

Inthe example of the Van der Pol equation,we have seen that only one of the periodic orbits of the harmonic oscillator persists under the small nonlinear perturbation and becomes an attractive limit cycle.More generally,we consider perturbations of integrable systems

$$
\begin{array} { r l r } { \dot { a } } & { = } & { \varepsilon r ( a , \theta ) } \\ { \dot { \theta } } & { = } & { \omega ( a ) + \varepsilon \rho ( a , \theta ) } \end{array}
$$

where(locally） just one invariant torus survives theperturbationand attracts nearby solutions.Using the results of the two previous sections,it will be shown that this situation occurs if,at some point $a ^ { * }$ where the frequencies $\omega _ { i } ( a ^ { * } )$ are diophantine, the angular average $\overline { { { r } } } ( a ^ { * } )$ issmall and its Jacobian matrix

$$
A = \overline { r } ^ { \prime } ( a ^ { * } )
$$

has all eigenvalues with negative real part.

The following theorem isa slight modification of aresult of Stoffer(1998).Early versions of it are much older;see the citations above.The origins of the problem can betraced back tothework ofVanderPol(1927)and Krylov&Bogoliubov(1934).

Herewe assume the following: $\omega ( a ^ { * } )$ satisfies the diophantine condition (X.2.4) with exponent $\nu$ .Theperturbation functions $r ( a , \theta )$ and $\rho ( a , \theta )$ arereai-analytic ona fixed complex neighbourhood of $\{ a ^ { * } \} \times \mathbb { T } ^ { d }$ and bounded independentlyof $\boldsymbol { \varepsilon }$ (though they may depend on $\boldsymbol { \varepsilon }$ ).Insomenorm $\| \cdot \|$ on ${ \mathbb R } ^ { d }$ and its induced matrix norm,the bounds

$$
\begin{array} { r } { \| \overline { { r } } ( a ^ { * } ) \| \le C | \log \varepsilon | ^ { - 2 ( \nu + 1 ) } } \\ { \| e ^ { t A } \| \le e ^ { - t \alpha } \quad \mathrm { ~ f o r ~ } t > 0 } \end{array}
$$

hold with some constants $C$ and $\alpha > 0$ .

Theorem4.1.Undertheaboveconditions,for sufficiently small $\varepsilon > 0$ ,thesystem (4.1) has an invariant torus $T _ { \varepsilon }$ which attracts an $\mathcal { O } ( | \log \varepsilon | ^ { - \nu - 1 } )$ -neighbourhoodof $\{ a ^ { * } \} \times \mathbb { T } ^ { d }$ withan exponential rate proportional to $\boldsymbol { \varepsilon }$ .

Proof.TheproofcombinesLemma2.1 and Theorem 3.1.Forconveniencewe assume $a ^ { * } = 0$ in thefollowing.Lemma 2.1（with $N \ = \ 3$ ）givesusachangeof coordinates $( a , \theta ) \mapsto ( b , \varphi )$ ， $\mathcal { O } ( \varepsilon )$ -closeto theidentity,such that for $\vert \vert \boldsymbol { b } \vert \vert \leq \delta$ with $\delta = c | \log \varepsilon | ^ { - \nu - 1 }$ of (2.9）,

$$
\begin{array} { r l r } { \dot { b } } & { = } & { \varepsilon m _ { 1 } ( b ) + \varepsilon ^ { 2 } m _ { 2 } ( b ) + \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } ) } \\ { \dot { \varphi } } & { = } & { \omega ( b ) + \varepsilon \mu _ { 1 } ( b ) + \varepsilon ^ { 2 } \mu _ { 2 } ( b ) + \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } ) . } \end{array}
$$

Since $m _ { 1 } ( b ) = \overline { { { r } } } ( b ) = A b + \mathcal { O } ( \delta ^ { 2 } )$ by(4.2),this system isof the form

$$
\begin{array} { l } { { \dot { b } } } \\ { { \dot { \theta } } } \end{array} = \varepsilon { \cal A } b + { \mathcal O } ( \varepsilon \delta ^ { 2 } )
$$

Similarly,the corresponding variational equation is of the form

$$
\left( \begin{array} { c } { \dot { B } } \\ { \dot { \phi } } \end{array} \right) = \left( \begin{array} { c c } { \varepsilon A + \mathcal { O } ( \varepsilon \delta ) } & { \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } ) } \\ { \mathcal { O } ( 1 ) } & { \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } ) } \end{array} \right) \left( \begin{array} { c } { B } \\ { \varPhi } \end{array} \right) .
$$

Theserelationsand condition(4.3) imply that,for sufficiently small $\varepsilon$ and forany fixed $\tau > 0$ ,thetime- $\tau$ flow of（4.1）maps the strip $D = \{ ( b , \varphi ) : \| b \| \leq \frac { 1 } { 2 } \delta , \varphi \in$ $\mathbb { T } ^ { d } \}$ into itself,and the following bounds hold for the derivatives of the solution with respect to the initial values:

$$
\begin{array} { r l r } { \displaystyle \left\| \frac { \partial b ( \tau ) } { \partial b ( 0 ) } \right\| \le L _ { b b } = e ^ { - \tau \varepsilon \alpha } + \mathcal { O } ( \varepsilon \delta ) , } & { \displaystyle \left\| \frac { \partial b ( \tau ) } { \partial \varphi ( 0 ) } \right\| \le L _ { b \varphi } = \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } ) } & \\ { \displaystyle \left\| \frac { \partial \varphi ( \tau ) } { \partial b ( 0 ) } \right\| \le L _ { \varphi b } = \mathcal { O } ( 1 ) , } & { \displaystyle \left\| \frac { \partial \varphi ( \tau ) } { \partial \varphi ( 0 ) } - I \right\| \le L _ { \varphi \varphi } = \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } ) . } & \end{array}
$$

Hence,for suficiently small $\varepsilon$ ，

$$
\begin{array} { r } { L _ { \varphi \varphi } + L _ { b b } + 2 \sqrt { L _ { \varphi b } L _ { b \varphi } } \le e ^ { - \tau \varepsilon \alpha / 2 } < 1 . } \end{array}
$$

Theorem 3.1(and Exercise1）used with $\varphi , b$ in the roles of $x , y$ now shows that the time- $\tau$ flow has an attractive invariant torus $\{ ( s ( \varphi ) , \varphi ) : \varphi \in \mathbb { T } ^ { d } \}$ ,where $s :  { \mathbb { T } ^ { d } } \to$ $\{ \| b \| \leq \frac 1 2 \delta \}$ is Lipschitz bounded by $\lambda = 2 L _ { b \varphi } / ( 1 - L _ { \varphi \varphi } - L _ { b b } ) = \mathcal { O } ( \varepsilon ^ { s } / \delta ^ { 2 } )$ . This invariant torus attracts orbits of the time- $\tau$ flowmapin the strip $D$ with the attractivity factor $\lambda L _ { \varphi b } + L _ { b b } \leq e ^ { - \tau \varepsilon \alpha / 2 } .$ As Exercise2 shows,the torus is actually invariant for the differential equation (4.1). □

# XII.5Weakly Attractive Invariant Tori ofNumerical Integrators

Does the attractive invariant torus ofTheorem 4.l persistunder numerical discretizationoftheperturbed integrable system?This questionwas first studied by Stoffer （1998)who worked directlywith thediscrete equations in hisanalysis.Herewe take uptheapproach of Hairer&Lubich(1999)where theproblem was studied by combiningbackward error analysisand perturbation theory,similar to what wasdone in thetwo preceding chapters.

# XII.5.1Modified Equations of Perturbed Differential Equations

Below we need to use backward error analysis for the numerical solution of a perturbed differential equation

$$
\begin{array} { r } { \dot { y } = f ( y ) + \varepsilon g ( y , \varepsilon ) , \qquad y ( 0 ) = y _ { 0 } } \end{array}
$$

with real-analytic functions $f$ and $g$ and small parameter $\succeq$ .Weconsider applying a one-step method $y _ { 1 } = \varPhi _ { h } ^ { \varepsilon } ( y _ { 0 } )$ oforder $p \geq 1$ with step size $h > 0$ Theassociated modified differential equations constructed in Chap.IXare then of the form

$$
\dot { \widetilde { y } } = \widetilde { f } ( \widetilde { y } ) + \varepsilon \widetilde { g } ( \widetilde { y } , \varepsilon ) , \qquad \widetilde { y } ( 0 ) = y _ { 0 }
$$

with suitably truncated series

$$
\begin{array} { r c l } { { } } & { { } } & { { \widetilde f ( y ) ~ = ~ f ( y ) + h ^ { p } f _ { p + 1 } ( y ) + . . . . + h ^ { N - 1 } f _ { N } ( y ) } } \\ { { } } & { { } } & { { \widetilde g ( y , \varepsilon ) ~ = ~ g ( y , \varepsilon ) + h ^ { p } g _ { p + 1 } ( y , \varepsilon ) + . . . . + h ^ { N - 1 } g _ { N } ( y , \varepsilon ) , } } \end{array}
$$

where the functions $f _ { j }$ are independent of $\varepsilon , h , N$ ,whereas the functions $g _ { j }$ are allowed todepend on $\boldsymbol { \mathsf { E } }$ Thefollowingadapts TheoremIX.7.6totheabove situation.

Theorem 5.1. Let $f ( y ) + \varepsilon g ( y , \varepsilon )$ be real-analytic(inyand $\boldsymbol { E }$ )andboundedby $M$ for $y \in B _ { 2 R } ( y _ { 0 } )$ andforall complex $^ { \circ }$ with $| \varepsilon | \leq \varepsilon _ { 0 }$ Let thecoefficients ofthe Taylor series(in $h$ )ofthe numerical method be analyticin $B _ { R } ( y _ { 0 } )$ with bounds (IX.7.5)for $| \varepsilon | \leq \varepsilon _ { 0 }$ .Then,thereexists $h _ { 0 } > 0$ (proportionalto $R / M$ ),suchthat for $h \leq h _ { 0 } / 4$ andfor $N = N ( h )$ thelargest integerwith $h N \leq h _ { 0 }$ ，thedifference between the numerical solution $y _ { 1 } = \varPhi _ { h } ^ { \varepsilon } ( y _ { 0 } )$ and theexact solution $\varphi _ { N , t } ^ { \varepsilon } ( y _ { 0 } )$ ofthe truncatedmodifiedequation(5.2)-(5.3) satisfies

$$
\begin{array} { r } { \| \varPhi _ { h } ^ { \varepsilon } ( y _ { 0 } ) - \widetilde { \varphi } _ { N , h } ^ { \varepsilon } ( y _ { 0 } ) \| \leq C h e ^ { - h _ { 0 } / h } , } \end{array}
$$

Thefunctions $\scriptstyle f$ and $\bar { g }$ of(5.3)are real-analytic in $B _ { R } ( y _ { 0 } )$ with

$$
\| \widetilde { f } ( y ) - f ( y ) \| \le C h ^ { p } , \quad \| \widetilde { g } ( y , \varepsilon ) - g ( y , \varepsilon ) \| \le C h ^ { p }
$$

for $y \in B _ { R / 2 } ( y _ { 0 } )$ and $\vert \varepsilon \vert \leq \varepsilon _ { 0 }$ Theconstants $C$ areindependentof $h \leq h _ { 0 } / 4$ and $| \varepsilon | \leq \varepsilon _ { 0 }$

Proof.The exponentially small estimate for $\Phi _ { h } ^ { \varepsilon } ( y _ { 0 } ) - \varphi _ { N , h } ^ { \varepsilon } ( y _ { 0 } )$ is that of TheoremIX.7.6applied to the differential equation(5.1).The $\mathcal { O } ( h ^ { p } )$ bound for $f ( y ) -$ $f ( y )$ istheestimate(IX.7.14) applied to $\dot { y } = f ( y )$ Byapplying that estimate to (5.1),a bound of the same type is obtained for $( f ( y ) + \varepsilon { \widetilde { g } } ( y , \varepsilon ) ) - ( f ( y ) + \varepsilon g ( y ) )$ , uniformly forall complex $\boldsymbol { \varepsilon }$ in the complex disk $| \varepsilon | \leq \varepsilon _ { 0 }$ Foranyfixed $y \in$ $B _ { R / 2 } ( y _ { 0 } )$ ,thedifference

$$
\begin{array} { r } { \langle y , \varepsilon \rangle - g ( y , \varepsilon ) = \frac { 1 } { \varepsilon } \left( [ ( \widetilde f ( y ) + \varepsilon \widetilde g ( y , \varepsilon ) ) - ( f ( y ) + \varepsilon g ( y , \varepsilon ) ) ] - [ \widetilde f ( y ) - f ( y ) ] \right) } \end{array}
$$

is ananalytic function of $\boldsymbol { \varepsilon }$ in the complex disk $| \varepsilon | \leq \varepsilon _ { 0 }$ ,whichis boundedby $\mathcal { O } ( h ^ { p } )$ for $| \varepsilon | = \varepsilon _ { 0 }$ Bythe maximum principle,the same bound then holds for $| \varepsilon | \leq \varepsilon _ { 0 }$ . $\sqhookrightarrow$

# XI1.5.2 Symplectic Methods

Weapply a symplectic integrator with step size $h$ toareal-analytic perturbed integrable Hamiltonian system in coordinates $( p , q )$ ,

$$
\begin{array} { r l } { \dot { p } \ = \ - \displaystyle \frac { \partial H } { \partial q } ( p , q ) + \varepsilon k ( p , q ) } & { { } } \\ { \dot { q } \ = \ \displaystyle } & { { } \displaystyle \frac { \partial H } { \partial p } ( p , q ) + \varepsilon \ell ( p , q ) . } \end{array}
$$

Weassume that theunperturbed system（ $\varepsilon ~ = ~ 0$ ）isacompletely integrablesystemwhich satisfies the conditions of the Arnold-Liouville theorem,TheoremX.1.6. Hence,there existsa transformation to action-angle variables for the

$$
i n t e g r a b l e s y s t e m : ~ ( p , q ) \mapsto ( a , \theta ) ~ \mathrm { b y ~ T h e o r e m ~ X . 1 . 6 } .
$$

Thischange of coordinates transforms the integrable system to the equations $\dot { a } = 0$ , $\dot { \theta } = \omega ( a )$ ,and it transforms(5.4)toa system(4.1),for whichwe assume(4.2),(4.3) and the diophantine condition（X.2.4）with exponent $\nu$ for $\omega ( a ^ { * } )$ Thefollowing theoremisavariant of resultsin Stoffer(1998）and Hairer $\&$ Lubich （1999).It showsthat for symplectic methods,the invariant torus persistsunderavery mild restriction on the step size.For non-symplectic methods,this would require step sizes $h$ with $h ^ { p } \ll \varepsilon$ (see Exercise5).

Theorem5.2.Letasymplecticnumerical integratoroforderpbeapplied toaperturbedintegrable Hamiltoniansystem(5.4）which satisfiesthe conditions stated above.Then,thereexist $\varepsilon _ { 0 } > 0$ and $c _ { 0 } > 0$ such that,for $0 < \varepsilon \le \varepsilon _ { 0 }$ andfor step sizes $h > 0$ satisfying

$$
h ^ { p } \leq c _ { 0 } | \log \varepsilon | ^ { - \kappa }
$$

with $\kappa = \operatorname* { m a x } ( \nu + d + 1 , p )$ ,thenumerical method hasanattractive invariant torus $\mathcal { I } _ { \epsilon , h }$ Thistorusis $\mathcal { O } ( h ^ { p } )$ closeto the invariant torus $\boldsymbol { \mathit { \Delta } } _ { \mathcal { L } _ { \mathcal { E } } }$ of(5.4).It attracts an $\mathcal { O } ( | \log \varepsilon | ^ { - 2 \kappa } )$ neighbourhoodwithanexponential rateproportional to $\boldsymbol { \varepsilon }$ ,uniformly in $h$

Remark5.3.Theexponent $\nu + d + 1$ comesfromLemmaX.4.1.Itcould bereduced to $\nu + 1$ byusingRüssmann'sestimatesinplace of that lemma;cf.the remarkafter Lemma X.4.1.

ProofofTheorem5.2.The proof combinesbackward error analysis(Theorem IX.3.1and Theorem5.1),perturbation theory(TheoremX.4.4and Lemma2.1), and the invariant manifold theorem(Theorem 3.1).

(a)We begin by considering the symplectic method applied to the integrable Hamiltonian system(5.4）with $\varepsilon = 0 .$ This leads us back to the questions ofChap.X. Weuse backward erroranalysisand recall(Theorem IX.3.1) that the modified equation is again Hamiltonian and an $\mathcal { O } ( h ^ { p } )$ perturbation of the integrable system,both inthe $( p , q )$ andthe $( a , \theta )$ variables.We transform variables forthe

modifiedequationof theintegrable system: $( a , \theta ) \mapsto ( \widetilde { a } , \widetilde { \theta } )$ by Theorem X.4.4, with $h ^ { p }$ in the role of the perturbation parameter.By (X.4.1) with $N$ proportional to $| \log \varepsilon |$ ,andby condition(5.5）withasufficiently small $c _ { 0 }$ ,themodified equations in these variables become

$$
\begin{array} { r l r l } & { \dot { \tilde { a } } = \mathcal { O } ( \varepsilon ^ { 3 } ) } & & { \mathrm { f o r } \quad \| \tilde { a } - a ^ { * } \| \leq c ^ { * } | \log \varepsilon | ^ { - 2 \kappa } , } \\ & { \dot { \tilde { \theta } } = \widetilde { \omega } ( \tilde { a } ) + \mathcal { O } ( \varepsilon ^ { 3 } ) } & & { \mathrm { f o r } \quad \| \tilde { a } - a ^ { * } \| \leq c ^ { * } | \log \varepsilon | ^ { - 2 \kappa } , } \end{array}
$$

with $\tilde { \omega } ( \tilde { a } ) = \omega ( \tilde { a } ) + { \cal O } ( h ^ { p } ) .$ Moreover,the transformation $( a , \theta ) \mapsto ( \widetilde { a } , \theta )$ is $\mathcal { O } ( h ^ { p } )$ close to the identity.

(b)The modified equations of the perturbed system,written in the $( \tilde { a } , \theta )$ variables,become

$$
\begin{array} { r l r } { \dot { \tilde { a } } = \varepsilon \widetilde { r } ( \tilde { a } , \tilde { \theta } ) + { \mathcal O } ( \varepsilon ^ { 3 } ) } & { \quad \mathrm { f o r } \quad \| \tilde { a } - a ^ { * } \| \leq c ^ { * } | \log \varepsilon | ^ { - 2 \kappa } , } \\ { \dot { \tilde { \theta } } = \widetilde { \omega } ( \tilde { a } ) + \varepsilon \widetilde { \rho } ( \tilde { a } , \tilde { \theta } ) + { \mathcal O } ( \varepsilon ^ { 3 } ) } & { } \end{array}
$$

where $\widetilde { r } ( \widetilde { a } , \widetilde { \theta } ) = r ( \widetilde { a } , \widetilde { \theta } ) + \mathcal { O } ( h ^ { p } )$ and $\widetilde { \rho } ( \widetilde { \boldsymbol { a } } , \widetilde { \boldsymbol { \theta } } ) = \rho ( \widetilde { \boldsymbol { a } } , \widetilde { \boldsymbol { \theta } } ) + \mathcal { O } ( h ^ { p } )$ by Theorem 5.1. Consider now these equations with the $\mathcal { O } ( \varepsilon ^ { 3 } )$ termsdropped.We change variables forthe

modifiedequation of theperturbed system: $( \widetilde { a } , \widetilde { \theta } ) \mapsto ( \widetilde { b } , \widetilde { \varphi } )$ byLemma 2.1.

(Note Exercise4with $\widetilde { \omega } ( a ^ { * } ) = \omega ( a ^ { * } ) + \mathcal { O } ( h ^ { p } )$ and (5.5).）The system(5.6) is transformed to the form of(4.4),

$$
\begin{array} { l } { \dot { \widetilde { b } } } \\ { \dot { \widetilde { b } } } \\ { \dot { \widetilde { \varphi } } } \\ { \dot { \widetilde { \varphi } } } \end{array} = \varepsilon \widetilde { m } ( \widetilde { b } ) + \mathcal { O } ( \varepsilon ^ { 3 } / \delta ^ { 2 } )
$$

with $\delta = c ^ { * } | \log \varepsilon | ^ { - 2 \kappa }$ ,and where $\widetilde { m } ( \bar { b } ) = \overline { { \widetilde { r } } } ( \bar { b } ) + \mathcal { O } ( \varepsilon / \delta ) = \overline { { r } } ( \widetilde { b } ) + \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \varepsilon / \delta )$ , and also the Jacobian of $\scriptstyle { \overline { { m } } }$ at $a ^ { * }$ is close to that of $r$ so that it satisfies again(4.3), atleast with $\alpha$ replaced by $\alpha / 2 .$ Inthe samewayas intheproof ofTheorem4.1and with the same Lipschitz constants as in(4.5）,we now obtain an attractive invariant torus of the modified equation of the perturbed system.The time- $h$ flowof this equation is an exponentially small（in $1 / h$ )Lipschitzperturbation of thenumerical one-stepmap,so that under condition（5.5）itisan $\mathcal { O } ( \varepsilon ^ { 3 } )$ perturbation.Therefore, Theorem 3.1 yieldsaninvariant torus $T _ { \varepsilon , h }$ ofthe numerical method.

(c) It remains to bound the distance between the tori $T _ { \varepsilon , h }$ and $T _ { \varepsilon }$ Werecall that $\mathcal { T } _ { \varepsilon }$ was obtained bya transformation of the

$$
p e r t u r b e d s y s t e m : ( a , \theta ) \mapsto ( b , \varphi ) \ \mathfrak { b y } \operatorname { L e m m a } 2 . 1 ,
$$

which puts (4.1) into the form(4.4).We thushave the transformations

$$
\begin{array} { c c c c c c } { { ( a , \theta ) } } & { { { } } } & { { { \stackrel { \varepsilon } { \longrightarrow } } } } & { { { } } } & { { { ( b , \varphi ) } } } \\ { { } } & { { { } } } & { { { } } } & { { { } } } & { { { } } } \\ { { h ^ { p } \coprod } } \\ { { } } & { { { } } } & { { { } } } & { { { } } } & { { { } } } \\ { { ( { \widetilde { a } , \widetilde { \theta } } ) } } & { { { } } } & { { { \stackrel { \varepsilon } { \longrightarrow } } } } & { { { } } } & { { { ( { \widetilde { b } , \widetilde { \varphi } } ) } } } \end{array}
$$

where the symbols $h ^ { p }$ and $\boldsymbol { \varepsilon }$ indicate that the transformationis $\mathcal { O } ( h ^ { p } )$ or $\mathcal { O } ( \varepsilon )$ close totheidentity.By the construction ofLemma 2.1,the composed transformation $( b , \varphi ) \mapsto ( { \widehat { b } } , { \widehat { \varphi } } )$ is $\mathcal { O } ( h ^ { p } )$ close to the identity and moreover,the right-hand sides of （4.4）and（5.7）differ by ${ \mathcal { O } } ( \varepsilon h ^ { p } ) .$ Theorem3.2（with $\rho = e ^ { - \varepsilon \tau \alpha / 2 }$ now shows that the functions $s _ { \epsilon , h }$ and $s _ { \varepsilon }$ defining $T _ { \varepsilon , h }$ and $T _ { \varepsilon }$ ,respectively,differby $\mathcal { O } ( h ^ { p } )$ This yields the desired distance bound. □

# XI1.5.3Symmetric Methods

Aresult analogous tothe theorem of the previous subsection holds for reversible methodsapplied toperturbed reversible systems

$$
\begin{array} { r } { \dot { u } \ = \ f ( u , v ) + \varepsilon k ( u , v ) } \\ { \dot { v } \ = \ g ( u , v ) + \varepsilon \ell ( u , v ) } \end{array}
$$

where theunperturbedsystem（ $\varepsilon = 0$ )isareal-analytic integrablereversiblesystem. If theperturbed system,written in action-angle variables of the unperturbed system, satisfiesthe conditions ofTheorem4.1,thenareversibleanalogue ofTheorem5.2 holds,where the terms"symplectic”and“Hamiltonian”are simply replaced by“reversible".The proofremains the same,workingwith the reversible analogues of the results used for the Hamiltonian case.

# XII.6 Exercises

1.Inthe situation ofthe invariantmanifold theorem,Theorem 3.1,supposein addition that $f$ and $g$ are $\alpha$ -periodicin $x \colon f ( x + \alpha , y ) = f ( x , y )$ , $g ( x + \alpha , y ) =$ $g ( x , y )$ forall $x \in X$ ， $y \in Y$ Show that in this case the function $s$ defining the invariantmanifold isalso $\alpha$ -periodic. Hint.The Hadamard transformmaps $\alpha$ -periodic functions to $\alpha$ -periodicfunctions.   
2.Show that if the time $\gamma$ flowmap $\phi = \varphi _ { \tau }$ ofadifferential equation has an attractiveinvariantmanifold $\mathcal { M }$ ,andifthe flow $\varphi _ { t }$ mapsadomain of attractivity of $\mathcal { M }$ under $\phi$ into itself for everyreal $t$ ,then $\mathcal { M }$ isalso invariant under the flow $\varphi _ { t }$ foreveryreal $t$ . Hint.Write $\varphi _ { t } = \varPhi ^ { n } \circ \varphi _ { t } \circ \varPhi ^ { - n }$ and use the attractivity of $\mathcal { M }$ for $n \to \infty$ .

3.Prove that in the situationof Theorem 3.1,iterates $( x _ { n + 1 } , y _ { n + 1 } ) = \varPhi ( x _ { n } , y _ { n } )$ have theproperty ofasymptoticphase(Nipp $\&$ Stoffer 1992):there exists asequence $( \widetilde { x } _ { n } , \widetilde { y } _ { n } )$ of iterates onthe invariant manifold,i.e.,with $( { \widetilde { x } } _ { n + 1 } , { \widetilde { y } } _ { n + 1 } ) =$ $\Phi ( \widetilde { x } _ { n } , \widetilde { y } _ { n } )$ and $\widetilde { y } _ { n } = s ( \widetilde { x } _ { n } )$ ,such that forall $n \geq 0$ ,

$$
\begin{array} { l } { \| x _ { n } - \widetilde { x } _ { n } \| \leq c \| y _ { n } - s ( x _ { n } ) \| } \\ { \| y _ { n } - \widetilde { y } _ { n } \| \leq ( 1 + \lambda c ) \| y _ { n } - s ( x _ { n } ) \| , } \end{array}
$$

where $c = \lambda / ( 1 - \lambda \lambda ^ { * } )$ with $\lambda = 2 L _ { y x } / ( 1 - L _ { x x } - L _ { y y } )$ of(3.5）and $\lambda ^ { * } = 2 L _ { x y } / ( 1 - L _ { x x } - L _ { y y } )$ Note that $\| y _ { n } - s ( x _ { n } ) \| \leq \rho ^ { n } \| y _ { 0 } - s ( x _ { 0 } ) \|$

Hint. Consider he segsences $( \widetilde { x } _ { n } ^ { ( k ) } , \widetilde { y } _ { n } ^ { ( k ) } )$ defined by $\widetilde { x } _ { k } ^ { ( k ) } = x _ { k }$ =xk,yk $\widetilde { y } _ { k } ^ { ( k ) } = s ( x _ { k } )$ and $( \widetilde { x } _ { n + 1 } ^ { ( k ) } , \widetilde { y } _ { n + 1 } ^ { ( k ) } ) \ = \ \varPhi ( \widetilde { x } _ { n } ^ { ( k ) } , \widetilde { y } _ { n } ^ { ( k ) } )$ for $n = k - 1 , \ldots , 1 , 0$ Showthat for fixed $_ { n }$ ,thesequence ${ ( x _ { n } ^ { ( k ) } }$ ）（ $k \geq n$ ）isaCauchysequence.

4.Show thatLemma 2.1 holds unchanged if the diophantinecondition (X.2.4)for $\omega ( a ^ { * } )$ isweakened to $\omega ( a ^ { * } ) = \omega ^ { * } + \mathcal { O } ( \delta ^ { 2 } )$ with $\omega ^ { \ast }$ satisfying(X.2.4）.

5.In the situation of Theorem 5.2,show that every numerical integrator of order $p$ has an attractive invariant torus if $h ^ { p } \ll \varepsilon .$ This torus is $\mathcal { O } ( h ^ { p } / \varepsilon )$ close to the invariant torus of the continuous system.
