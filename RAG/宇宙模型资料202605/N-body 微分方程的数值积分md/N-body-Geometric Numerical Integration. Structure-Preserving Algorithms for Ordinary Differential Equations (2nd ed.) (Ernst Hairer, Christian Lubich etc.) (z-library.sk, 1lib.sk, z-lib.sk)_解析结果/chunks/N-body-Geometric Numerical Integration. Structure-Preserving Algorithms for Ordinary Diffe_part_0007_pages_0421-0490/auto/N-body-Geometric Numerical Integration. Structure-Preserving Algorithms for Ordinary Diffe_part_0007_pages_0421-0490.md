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

![](images/9326626c5350140a768c04c10ecdd0ca76443ad7dd74cd706828c7419f4a34df.jpg)  
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

![](images/a0eae888894e40163a0b954f3cd4d83070b79258a6684a1cd97a910f0e3cc1b7.jpg)  
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

![](images/7e367fd3bbe31575f5d9359171039fd3a0194089db3db1150b88b51a91005f90.jpg)  
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

![](images/03678104fa06073dbe09e6bc03339b94928c1a1a299ecb019a8548ec1fec6c4c.jpg)

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

![](images/8421e37479f80a2856f4be7f35fd5716a5ec19e6e99085765e41eb29c354ba4e.jpg)  
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

![](images/0dd6e6fd9da430fd4533c23ac19cf5e22348052731d2a069689b4de548818007.jpg)

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

![](images/096362ac9250b877cbcde63cb95184127a94324a9663bf0f487b117c9274575b.jpg)  
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

![](images/97d2011f20f261df29329d0f942fb58797c7111fbbe8474d5f8d740213068178.jpg)  
Fig.3.1.Numerical Hamiltonian of Example1.4 for twodifferent initial values

Forthe Toda lattice example,Figures3.2and 3.3illustrate thelong-time conservation of the first integralsand the linear error growth,respectively,of theLobatto IIB method.

Theorem3.1 togetherwith Examples1.7and1.8also explainsthegood behaviourof symmetric (in fact,reversible) integrators on the rigid body equations which weobserved inChap.V(Figs.V.4.2andV.4.6).

Variable Step Sizes:Proportional,Reversible Controllers.Asa consequence of thebackward erroranalysis of TheoremIX.6.1 the statement（3.1）canbeextended straightforwardly to proportional step size controllers as discussed in Sect.VI.3.1. Under the assumption of Theorem 3.1with $h$ and $h _ { 0 }$ replaced by $\varepsilon$ and $\varepsilon _ { 0 }$ onehas

$$
\begin{array} { r l } { \| ( u _ { n } , v _ { n } ) - ( u ( t _ { n } ) , v ( t _ { n } ) ) \| \leq C t _ { n } \varepsilon ^ { p } } & { \quad \mathrm { f o r } t _ { n } \leq \varepsilon ^ { - p } . } \\ { \| I ( u _ { n } , v _ { n } ) - I ( u _ { 0 } , \bar { v } _ { 0 } ) \| \leq C \varepsilon ^ { p } } & { \quad \mathrm { f o r } t _ { n } \leq \varepsilon ^ { - p } . } \end{array}
$$

The grid $\left\{ \ t _ { n } \right\}$ isdeterminedbythe methodandsatisfies $t _ { n + 1 } = t _ { n } + \varepsilon s ( u _ { n } , v _ { n } , \varepsilon )$

Variable Step Sizes: Integrating,Reversible Controllers.We apply thebackward erroranalysisof TheoremIX.6.2.Themodified equation(IX.6.14)reducesto

![](images/07d6abd1a150f66f939d64cea48e61d293d7c189f3de30a203e980352f1f2500.jpg)  
Fig.3.2.Numerically obtained eigenvalues(left picture）and errors in the eigenvalues(right picture）of the 3-stageLobatto IIIB scheme (step size $h = 0 . 1$ applied tothe Toda lattice with the data of Sect.X.1.5

![](images/6237ac3a15a1ee2e8b03d9b8408ec579396dbef9fd18630a7035841d5fe674ea.jpg)  
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

![](images/be2bd9d01dd762c6086c97567efd0279fe342bcf0f1355d0ae3c0fe28126b86e.jpg)  
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

# Chapter XIII. Oscillatory Differential Equations with Constant High Frequencies

Thischapter dealswith numerical methods for second-order differential equations with oscillatory solutions.These methods are designed to requirea new complete function evaluation only after a time step over one or many periodsof the fastest oscillations in the system.Various such methods have been proposed in the literaturesomeof them decadesago,some very recently.motivated by problems from moleculardynamics,astrophysics and nonlinear wave equations.For these methods itis not obvious what implications geometric properties like symplecticity or reversibilityhaveonthe long-time behaviour,e.g.,onenergy conservation.The backward erroranalysisof Chap.IX,which was the backbone of theresults of the three precedingchapters,is no longer applicable when the product of the step sizewith the highest frequency is not small,which is the situation of interest here.The“exponentiallysmall"remainder terms are now only $\mathcal { O } ( 1 ) !$ Fordifferential equationswhere thehigh frequencies of the oscillations remain nearly constant along the solution, asubstitutefor thebackward erroranalysis ofChap.IXis given by themodulated Fourier expansions of the exact and the numerical solutions.Among other properties,theypermitustounderstand the numerical long-timeconservation of the total and oscillatory energies(or the failure ofconserving energy incertain cases).It turns out,symmetry of the methods is still essential, but symplecticity plays norole in the analysis and in the numerical experiments,and new conditions of anapparently non-geometric nature come into play.

# XIII.1 Towards Longer Time Steps in Solving Oscillatory Equations of Motion

Dynamical systems with multiple time scales pose a major problem in simulations because the small time steps required for stable integration of the fast motions lead to large numbers of time steps required for the observation of slow degrees of freedomand thus to the need to compute alarge number of forces.

(M.Tuckerman,B.J.Berne&G.J.Martyna1992)

We describe numerical methods that have been proposed for solving highly oscillatory second-orderdifferential equationswith fewer force evaluations than are neededby standard integrators like the Stormer-Verletmethod.We present the ideas