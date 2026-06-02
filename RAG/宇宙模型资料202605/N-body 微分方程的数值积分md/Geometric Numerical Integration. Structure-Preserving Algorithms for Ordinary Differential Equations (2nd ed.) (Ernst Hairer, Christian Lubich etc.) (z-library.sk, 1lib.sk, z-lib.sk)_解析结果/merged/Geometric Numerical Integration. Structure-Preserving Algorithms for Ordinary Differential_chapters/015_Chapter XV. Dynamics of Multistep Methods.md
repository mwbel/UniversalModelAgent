# Chapter XV. Dynamics of Multistep Methods

Multistep methodsare the basis of importantcodes for nonstiff differential equations(Adamsmethods)and for stiff problems(BDF methods).We study here their applicability to long-time integrations of Hamiltonian or reversible systems.

This chapter starts with numerical experiments which illustrate that the longtimebehaviour of classical multistep methods isin general disappointing.They eitherbehave as non-symplectic and non-symmetric one-step methods,or theyexhibitundesired instabilities(parasitic solutions).Certain multistep methods forsecondorder equations orpartitioned multistepmethods,however,haveamuch better long-time behaviour.They are promisingmethods,because ina constant step size mode they can be easily implemented,and high order can be obtained with one function evaluation per step.We characterize such methods by studying their underlyingone-step method,their symplecticity,their conservation properties,as wellas their long-term stability.

# XV.1 Numerical Methods and Experiments

Wepresent the numerical methods treated in this chapter,and in numerical experimentswe look at their behaviour on Hamiltonian systems.

# XV.1.1LinearMultistep Methods

For first order systems of differential equations $\dot { y } = f ( y )$ ,linear multistep methods aredefinedbytheformula

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } f ( y _ { n + j } ) ,
$$

where $\alpha _ { j } , \beta _ { j }$ arereal parameters, $\alpha _ { k } \neq 0$ ,and $| \alpha _ { 0 } | + | \beta _ { 0 } | > 0$ Foran application ofthis formula we needa starting procedurewhich,inaddition to an initial value $y ( t _ { 0 } ) = y _ { 0 }$ ,provides approximations $y _ { 1 } , \ldots , y _ { k - 1 }$ to $y ( t _ { 0 } + h ) , \dotsc , y ( t _ { 0 } + ( k - 1 ) h ) .$ Theapproximations $y _ { n }$ to $y ( t _ { 0 } + n h )$ for $n \geq k$ can then be computed recursively from(1.1).In the case $\beta _ { k } = 0$ we have an explicit method,otherwise itis implicit and the numerical solution $y _ { n + k }$ has to be computed iteratively.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/b3058f513b89779dc7d506de631664dfb3e9e2312711f79c222ee0917c1c898d.jpg)  
Germund Dahlquist1

Since thefundamental work of Dahlquist （1956)itiscommon todenotethe generating polynomials of the coefficients by

$$
\rho ( \zeta ) \equiv \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta ^ { j } , \qquad \sigma ( \zeta ) = \sum _ { j = 0 } ^ { k } \beta _ { j } \zeta ^ { j } .
$$

For the classical theory of multistep methods we refer the reader to Chap.IIIof Hairer, Norsett&Wanner(1993).We just recall some important definitions.

Order.A multistep method has order $r$ if, when applied with exact starting values to the problem $\dot { y } = t ^ { q }$ ( $0 \leq q \leq r$ ),it integrates the problem without error.This is equivalent tothe requirement that

$$
\rho ( e ^ { h } ) - h \sigma ( e ^ { h } ) = \mathcal { O } ( h ^ { r + 1 } ) \qquad \mathrm { f o r } \quad h \to 0 .
$$

Stability.Method(1.1）is stable if,whenapplied to $y ~ = ~ 0$ ,ityields for all $y _ { 0 } , \ldots , y _ { k - 1 }$ abounded numerical solution.Thisis equivalent to the requirement thatthe polynomial $\rho ( \zeta )$ satisfies the root condition,i.e.,all roots of $\rho ( \zeta ) = 0$ satisfy $| \zeta | \le 1$ ,andthoseon theunit circle are simpleroots.The methodis called strictly stable,ifall rootsareinside the unit circle with theexception of $\zeta = 1$

Convergence.If a multistep method is stable and of order $r \geq 1$ ,itis convergent of order $r$ forall sufficiently smooth problems.This means that,assuming starting approximationswith an error bounded by $\mathcal { O } ( h ^ { r } )$ ,theglobal error satisfies $y _ { n } -$ $y ( t _ { 0 } + n h ) = \mathcal { O } ( h ^ { r } )$ oncompact intervals $n h \le { \cal T }$ ..

Symmetry.If the coefficients ofamultistep formula(1.1） satisfy

$$
\alpha _ { k - j } = - \alpha _ { j } , \qquad \beta _ { k - j } = \beta _ { j } \qquad \mathrm { f o r ~ a l l } ~ j ,
$$

thenthe method iscalled symmetric.Condition (1.3) implies that for every zero $\zeta$ of $\rho ( \zeta )$ also its inverse $\zeta ^ { - 1 }$ isazero.Hence,forstable symmetric methods all zeros of $\bar { \rho } ( \zeta )$ are simple and lie on the unit circle.

Example1.1.Weconsider the pendulum equation (I.1.13),and weapply the followingmultistepmethods:the2-step explicit Adams method

$$
y _ { n + 2 } = y _ { n + 1 } + h \Big ( \frac 3 2 f _ { n + 1 } - \frac 1 2 f _ { n } \Big ) ,
$$

the2-step backward diferentiation formula (BDF)

$$
{ \frac { 3 } { 2 } } y _ { n + 2 } - 2 y _ { n + 1 } + { \frac { 1 } { 2 } } y _ { n } = h f _ { n + 2 } ,
$$

and the (2-step) symmetric explicit midpoint rule

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/deb21da6077deedfdc82cee4fe06206e5bb8da7d7a806798a117737a2778e9f3.jpg)  
Fig.1.1.Solutions of thependulum problem(I.1.13);explicit Adams with step size $h =$ 0.5,initial value $( p _ { 0 } , q _ { 0 } ) = ( 0 , 0 . 7 )$ BDFwith step size $h = 0 . 5$ ,initialvalue $( p _ { 0 } , q _ { 0 } ) =$ $( 0 , 0 . 9 5 )$ ;explicit midpoint rulewith $h = 0 . 4$ and initialvalue $( p _ { 0 } , q _ { 0 } ) = ( 1 . 1 , 0 )$

$$
y _ { n + 2 } = y _ { n } + 2 h f _ { n + 1 } .
$$

Forall methodswe take $y _ { 1 } = y _ { 0 } + h f _ { 0 }$ as the approximation for $y ( t _ { 0 } + h )$ The resultsof the first 108 stepsare shown in Fig.1.1.We observe that the first two methods,as expected,behave similarly as the explicit and implicit Euler method (thenumerical solutionspiralseitheroutwardsorinwards).Thiswill be rigorously explainedinSect.XV.2.1below.However,asmight notbeexpected,thesymmetric method(1.6)does notbehave like the implicit midpoint rule(cf.Fig.I.1.4),it shows undesired increasing oscillations (parasitic solutions).

After this negative experience with classical multistep methods,the obvious question is:are there multistep methods which havea long-time behaviour that is comparable to symplectic and/or symmetric one-step methods?

# XV.1.2 Multistep Methods for Second Order Equations

Many important Hamiltonian systems are second order differential equations

$$
{ \ddot { y } } = f ( y ) ,
$$

where the force $f$ isindependent of the velocity $\dot { y }$ Introducing the new variable alitepewiet ,weobtain the system , $\dot { v } = f ( y )$ offirst order equations.Ifwe apply $\begin{array} { r } { \rho ^ { * } ( \zeta ) = \sum _ { j = 0 } ^ { k ^ { * } } \alpha _ { j } ^ { * } \zeta ^ { j } } \end{array}$ and （=∑isteget

$$
\sum _ { j = 0 } ^ { k ^ { * } } \alpha _ { j } ^ { * } y _ { n + j } = h \sum _ { j = 0 } ^ { k ^ { * } } \beta _ { j } ^ { * } v _ { n + j ; } \qquad \sum _ { j = 0 } ^ { k ^ { * } } \alpha _ { j } ^ { * } v _ { n + j } = h \sum _ { j = 0 } ^ { k ^ { * } } \beta _ { j } ^ { * } f ( y _ { n + j } ) .
$$

An elimination of the $\boldsymbol { v }$ variables thenyields

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y _ { n + j } = h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } f ( y _ { n + j } ) ,
$$

where $k = 2 k ^ { * }$ ， $\rho ( \zeta ) = \rho ^ { * } ( \zeta ) ^ { 2 }$ and $\sigma ( \zeta ) = \sigma ^ { * } ( \zeta ) ^ { 2 }$ We consider here methods （1.8）whichdo not necessarily originate from amultistepmethod for first order equations,and we denote the generating polynomials of the coefficients $\alpha _ { j }$ and $\beta _ { j }$ againby $\rho ( \zeta )$ and $\sigma ( \zeta )$ Fromtheclassical theory(see Sect.III.1Oof Hairer,Norsett &Wanner 1993)we recall the followingdefinitions and results.

Order.A method(1.8)has order $r$ if its generating polynomials satisfy

$$
\rho ( e ^ { h } ) - h ^ { 2 } \sigma ( e ^ { h } ) = \mathcal { O } ( h ^ { r + 2 } ) \qquad \mathrm { f o r } \quad h \to 0 .
$$

Stability.Method(1.8) is stable if all zeros of thepolynomial $\rho ( \zeta )$ satisfy $| \zeta | \le 1$ ， andthose on the unit circle are at most double zeros.Observe that for methods originatingfrom(1.1）all zerosaredouble.Themethod iscalled strictly stable,if all zeros are inside the unit circle with the exception of $\zeta = 1$

Convergence.If amultistep method(1.8) is stable,of order $r \geq 1$ and if the starting valuesare accurate enough,the global error satisfies $y _ { n } - y ( t _ { 0 } + n h ) = \mathcal { O } ( h ^ { r } )$ on compact intervals $n h \le T$ .

SymmetryIfthecoefficientsof(1.8)satisfy

$$
\alpha _ { k - j } = \alpha _ { j } , \qquad \beta _ { k - j } = \beta _ { j } \qquad \mathrm { f o r ~ a l l } ~ j ,
$$

then themethod issymmetric.Again,for every zero $\zeta$ of $\rho ( \zeta )$ thevalue $\zeta ^ { - 1 }$ isalso a zero.Hence,stable symmetric methods have all zeros of $\rho ( \zeta )$ on the unit circle and they are at most of multiplicity two.

Dahlquist(1956) noticed that double zeros of $\rho ( \zeta )$ on the unit circle can lead to anexponential error growth.Lambert&Watson（1976)analyzedindetail the application of(1.8)to the linear test equation $\ddot { y } = - \omega ^ { 2 } y .$ They found thatwith symmetricmethods forwhich $\rho ( \zeta )$ does not have double roots on the unit circle other than $\zeta = 1$ ,thenumerical solution remainsclose toaperiodic orbit(forsufficiently small stepsizes).For example,theStormer-Verlet method $y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } f _ { n }$ satisfies this property for $0 < h \omega < 2$ (see Sect.I.5.2).The study of thelong-time behaviour of symmetric methods(1.8)was then put forward by the article of Quinlan&Tremaine(199o),wherean excellent performance for simulations of the outer solar system is reported.

Example1.2.We consider the Keplerproblem (I.2.2）with initial values(I.2.11) and eccentricity $e = 0 . 2$ .Weapply the following three methods with constant step size $h = 0 . 0 1$ on the interval of length $2 \pi \cdot 1 0 ^ { 5 }$ (i.e., $1 0 ^ { 5 }$ periods):

$$
\begin{array} { r l } & { y _ { n + 4 } - 2 y _ { n + 3 } + y _ { n + 2 } = h ^ { 2 } \Big ( \cfrac { 7 } { 6 } f _ { n + 3 } - \cfrac { 5 } { 1 2 } f _ { n + 2 } + \cfrac { 1 } { 3 } f _ { n + 1 } - \cfrac { 1 } { 1 2 } f _ { n } \Big ) } \\ & { y _ { n + 4 } - 2 y _ { n + 2 } + y _ { n } = h ^ { 2 } \Big ( \cfrac { 4 } { 3 } f _ { n + 3 } + \cfrac { 4 } { 3 } f _ { n + 2 } + \cfrac { 4 } { 3 } f _ { n + 1 } \Big ) } \\ & { y _ { n + 4 } - 2 y _ { n + 3 } + 2 y _ { n + 2 } - 2 y _ { n + 1 } + y _ { n } = h ^ { 2 } \Big ( \cfrac { 7 } { 6 } f _ { n + 3 } - \cfrac { 1 } { 3 } f _ { n + 2 } + \cfrac { 7 } { 6 } f _ { n + 1 } \Big ) . } \end{array}
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/e8240c0dc1fce402b89c6029b359aed0926c99b94742947980e780371df65363.jpg)  
Fig.1.2.Error in the total energy for the three linear multistep methods of Example1.2 appliedtothe Keplerproblemwith $e = 0 . 2$

All three methodsare of order $r = 4$ method(A)isstrictlystable,whereasmethods (B）and(C)are symmetric.For method(B） the $\rho$ -polynomial hasadoublerootat $\zeta = - 1$ ,formethod (C) it doesnot havedoubleroots other than1.Startingvalues $y _ { 1 } , y _ { 2 }$ ,and $y _ { 3 }$ arecomputedveryaccuratelywithahigh-orderRunge-Kuttamethod.

Theerror in the total energy isplotted forall three methodsin Fig.1.2.On thefirst1O periods,all methodsbehave similarlyand noerror growth isobserved. Beyond this interval,method（A）showsa linearerror growth（as itis thecase for non-symplecticand non-symmetric one-stepmethods),method(B) has an exponential error growth,and formethod(C) the errorremains bounded ofsize $\mathcal { O } ( h ^ { 4 } )$ on thewhole interval of integration.One of the aims of this chapter is to explain the excellent long-time behaviour of method(C).

Stabilized Version of(1.8).Due to the double zeros (of modulus one) of the characteristic polynomial of thedifferenceequation $\sum _ { j } \alpha _ { j } y _ { n + j } = 0$ ,we have an undesired propagation of rounding errors (especially for long-time integrations）.To overcome this difficulty,wesplit the characteristic polynomial $\rho ( \zeta )$ into

$$
\rho ( \zeta ) = \rho _ { A } ( \zeta ) \cdot \rho _ { B } ( \zeta ) ,
$$

such that each polynomial

$$
\rho _ { A } ( \zeta ) = \sum _ { j = 0 } ^ { k _ { A } } \alpha _ { j } ^ { ( A ) } \zeta ^ { j } , \qquad \rho _ { B } ( \zeta ) = \sum _ { j = 0 } ^ { k _ { B } } \alpha _ { j } ^ { ( B ) } \zeta ^ { j }
$$

hasonly simple roots of modulus one. Introducing the new variable $h v _ { n } : =$ $\sum _ { j } \alpha _ { j } ^ { ( A ) } y _ { n + j }$ ,therecurrencerelation（1.8) becomes equivalent to

$$
\sum _ { j = 0 } ^ { k _ { A } } \alpha _ { j } ^ { ( A ) } y _ { n + j } = h v _ { n ; } \qquad \sum _ { j = 0 } ^ { k _ { B } } \alpha _ { j } ^ { ( B ) } v _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } f _ { n + j } .
$$

Thisformula,which for the Stormer-Verlet scheme correspondsto the one-step formulation(I.1.17),ismuch better suited for an implementation.If the splitting issuch that $\rho _ { A } ^ { \prime } ( 1 ) = 1$ ,thediscretization(1.12）isconsistent with the first order partitioned system $\dot { y } = v , \dot { v } = f ( y )$

# XV.1.3PartitionedMultistep Methods

Motivated by the stabilized version(1.12）of multistep methods for second order equations,letus consider general partitioned systems ofdifferential equations

$$
\dot { y } = f ( y , v ) , \qquad \dot { v } = g ( y , v ) ,
$$

where,needless tosay, $y$ and $v$ maybe vectors.Theideaistoapply differentmultistepmethodsto different components.We thus get

$$
\sum _ { j = 0 } ^ { k } { \alpha } _ { j } ^ { ( A ) } y _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } ^ { ( A ) } f _ { n + j ; } \qquad \sum _ { j = 0 } ^ { k } { \alpha } _ { j } ^ { ( B ) } v _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } ^ { ( B ) } g _ { n + j } ,
$$

where $f _ { n } = f ( y _ { n } , v _ { n } )$ and $g _ { n } = g ( y _ { n } , v _ { n } ) .$ We can take the same $k$ for both methods without loss of generality,if we abandon theassumption $| \alpha _ { 0 } | + | \beta _ { 0 } | > 0$

Such a method is of order $T$ ,ifboth methodsare of order $\boldsymbol { r } _ { * }$ It is stable (strictly stable,symmetric, $\cdot \cdot \cdot$ ),if both methodsare stable (strictly stable,symmetric,...).

Example 1.3. For our next experiment we use the symmetric methods

$$
\begin{array} { r l } { : } & { { } \quad y _ { n + 3 } - y _ { n + 2 } + y _ { n + 1 } - y _ { n } = h ( f _ { n + 2 } + f _ { n + 1 } ) } \\ { : } & { { } \quad v _ { n + 3 } - v _ { n + 1 } = 2 h g _ { n + 2 } . } \end{array}
$$

Both methods are of order 2,and their $\rho$ -polynomials $\rho _ { A } ( \zeta ) = ( \zeta - 1 ) ( \zeta ^ { 2 } + 1 )$ and $\rho _ { B } ( \zeta ) = ( \zeta - 1 ) ( \zeta + 1 )$ do not have common zeros with the exception of $\zeta = 1$ .

0

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/2fcd10fb90909a6ddbdee32d6546c7b4239ecb6bad0892979f99aca0187c6ee0.jpg)  
Fig.1.3.Three versions of the methods(1.15）applied with step size $h = 5 0$ （days）to the outersolarsystem.For method(B)only the numerical orbits of Jupiterand Saturn are plotted. Thetime intervals are given in units of $1 0 0 0 0$ days

Wechoose the outer solar systemwith thedataas described in Sect.I.2.4,and weapply the methods in three versions:（i)as partitioned method(AB),where the positions are treated bymethod (A） and thevelocities by method(B);(ii) method (A）isapplied to all components;(iii） method(B） isapplied to all components. Thenumerical resultsare shown in Fig.1.3.Whereas theindividual methods show instabilitieson rather short time intervals,the partitioned method givesa correct picture evenwith a large step size $h = 5 0$

# XV.2 The UnderlyingOne-Step Method

Much insight into the long-time behaviour of multistep methods can be gained by relating their numerical solution toone-step methods.This thenallows foran application of the considerations of the preceding sections.

# XV.2.1 Strictly Stable Multistep methods

Itwasa surprising result when Kirchgraber(1986)proved that strictly stable multistepmethodsare essentially equivalent to one-step methods.Although this one-step methodis“quiteexotic”(Eirola&Nevanlinna1988),itisthekeyforabetterunderstanding of thedynamics of strictly stable methods.

Theorem2.1 (Kirchgraber 1986). Considera strictly stable linear multistep method(1.1)appliedwithasufficiently small stepsize $h$ .Then,thereexistsa onestepmethod $\phi _ { h }$ such that for starting approximations computed by $y _ { j } = \varPhi _ { h } ^ { \jmath } ( y _ { 0 } )$ ， $j = 1 , \ldots , k - 1 ,$ thenumericalsolutionof(1.1) isidenticaltothat obtainedby the one-step method,i.e., $y _ { n + 1 } = \varPhi _ { h } ( y _ { n } )$ forall $n \geq 0$

Proof.The ideais toreformulate themultistepmethod(1.1）in suchaway that the InvariantManifoldTheorem of Sect.XII.3canbeapplied.Tokeepthenotationas simple aspossible,let us consider the case $k = 3$ .

We writethe method in the form

$$
\left( { \begin{array} { c } { y _ { n + 3 } } \\ { y _ { n + 2 } } \\ { y _ { n + 1 } } \end{array} } \right) = \left( { \begin{array} { c c c } { - a _ { 2 } } & { - a _ { 1 } } & { - a _ { 0 } } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} } \right) \left( { \begin{array} { c } { y _ { n + 2 } } \\ { y _ { n + 1 } } \\ { y _ { n } } \end{array} } \right) + h \left( { \begin{array} { c } { F _ { h } ( y _ { n } , y _ { n + 1 } , y _ { n + 2 } ) } \\ { 0 } \\ { 0 } \end{array} } \right)
$$

with $a _ { i } = \alpha _ { i } / \alpha _ { k }$ ,andwe transform the appearing matrix $A$ to Jordan canonical form $J = T ^ { - 1 } A T .$ We thus get

$$
Z _ { n + 1 } \equiv \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { d _ { \mathrm { { 1 1 } } } } } & { { d _ { \mathrm { { 1 2 } } } } } \\ { { 0 } } & { { d _ { { 2 1 } } } } & { { d _ { { 2 2 } } } } \end{array} \right) Z _ { n } + h G ( Z _ { n } ) , \qquad \bar { Z } _ { n } = { \cal T } ^ { - 1 } \left( \begin{array} { c } { { y _ { n + 2 } } } \\ { { y _ { n + 1 } } } \\ { { y _ { n } } } \end{array} \right) .
$$

Since themethodis strictly stable,1 isa simple eigenvalue of $A$ ,andallother eigenvalues are less than 1in modulus.Consequently,the matrix $D = \left( d _ { i j } \right)$ satisfies

$\| D \| < 1$ inasuitable norm.Partitioning $Z _ { n } = ( \xi _ { n } , \eta _ { n } ) ^ { { \scriptscriptstyle T } }$ into its first component $\xi _ { n }$ and the rest (collected in $\eta _ { n }$ ),wesee that(2.2）is of the form(XI.3.1）with $L _ { x x } , L _ { x y } , L _ { y x }$ ofsize $\mathcal { O } ( h )$ ,and $L _ { y y } = \| D \| < 1 .$ TheoremXII.3.1thusyields the existence ofa function $\eta = s ( \xi )$ such that the manifolds

$$
\mathcal { N } _ { h } = \Big \{ \left( \begin{array} { c } { \xi } \\ { s ( \xi ) } \end{array} \right) ; \xi \in \mathbb { R } ^ { d } \Big \} \qquad \mathrm { a n d } \qquad \mathcal { M } _ { h } = \Big \{ T \left( \begin{array} { c } { \xi } \\ { s ( \xi ) } \end{array} \right) ; \xi \in \mathbb { R } ^ { d } \Big \}
$$

areinvariant under the mappings(2.2） and(2.1),respectively.The function $s ( \xi )$ is Lipschitz continuous with constant $\lambda = { \mathcal { O } } ( h )$ .

Since the first column of $T$ ,whichis the eigenvector corresponding to the eigenvalue $1$ of $A$ ,is given by $( 1 , 1 , 1 ) ^ { T }$ ,the last component of $T \left( { \xi } \atop { s ( \xi ) } \right)$ satisfies $y = \xi + g ( \xi )$ where $g ( \xi )$ isLipschitz continuous with constant ${ \mathcal { O } } ( h )$ BytheBanach fixed-point theorem this equation has a unique solution $\xi = r ( y ) .$ Consequently,the manifold $\mathcal { M } _ { h }$ can be parametrized in terms of $y$ as

$$
\mathcal { M } _ { h } = \big \{ ( \varPsi _ { h } ( y ) , \varPhi _ { h } ( y ) , y ) ^ { T } ; y \in \mathbb { R } ^ { d } \big \} .
$$

Its invarianceunder(2.1) implies that

$$
\begin{array} { r } { \mathrm {  { ~ \mathcal { F } ~ } } _ { h } ( \widehat { y } ) \mathrm {  { ~ \cal { F } ~ } } _ { h } ( \widehat { y } ) = \left( \begin{array} { c c c } { - a _ { 2 } } & { - a _ { 1 } } & { - a _ { 0 } } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} \right) \left( \begin{array} { l } { \varPsi _ { h } ( y ) } \\ { \varPhi _ { h } ( y ) } \\ { y } \end{array} \right) + h \left( \begin{array} { c } { F _ { h } ( y , \varPhi _ { h } ( y ) , \varPsi _ { h } ( y ) ) } \\ { 0 } \\ { 0 } \end{array} \right) } \end{array}
$$

and consequently $\widehat { y } = \varPhi _ { h } ( y )$ and $\varPhi _ { h } ( \widehat { y } ) = \varPsi _ { h } ( y )$ ,sothat $\varPsi _ { h } ( y ) = \varPhi _ { h } ^ { 2 } ( y )$ This holdsforall $y$ ,and thusproves the statement of the theorem. □

Example2.2.Fora scalarlinearproblem $\dot { y } = \lambda y$ ,theapplication ofamultistep method yieldsadifference equation withcharacteristicpolynomial $\rho ( \zeta ) - h \lambda \sigma ( \zeta )$ Denoting its zeros by $\zeta _ { 1 } ( h \lambda ) , \ldots , \zeta _ { k } ( h \lambda )$ ,where $\zeta _ { 1 } ( 0 ) = 1$ and $| \zeta _ { j } ( 0 ) | < 1$ for $j \geq 2$ ,the numerical solution can be written as (assuming distinct $\zeta _ { j } ( h \lambda )$ ）

$$
y _ { n } = c _ { 1 } \zeta _ { 1 } ^ { n } ( h \lambda ) + c _ { 2 } \zeta _ { 2 } ^ { n } ( h \lambda ) + . . . + c _ { k } \zeta _ { k } ^ { n } ( h \lambda ) .
$$

The coefficients $c _ { 1 } , \ldots , c _ { k }$ depend on $h \lambda$ andaredetermined by the starting approximations $y _ { 0 } , \ldots , y _ { k - 1 } .$ Inthis situation theunderlying one-step method is the mapping $y _ { 0 } \mapsto \zeta _ { 1 } ( h \lambda ) y _ { 0 } .$ Observethat $\zeta _ { 1 } ( z )$ isin general not a rational function as weare used to with Runge-Kutta methods.

Remark2.3 (Asymptotic Phase).For arbitrary $y _ { 0 } , y _ { 1 } , \dotsc , y _ { k - 1 }$ close to the exact solution,there exists $y _ { 0 } ^ { * }$ such that the multistep solution $\left\{ y _ { n } \right\}$ and the one-step solution $\left\{ y _ { n } ^ { * } \right\}$ ,givenby ${ \boldsymbol y } _ { n + 1 } ^ { * } = \Phi _ { h } ( { \boldsymbol y } _ { n } ^ { * } )$ ,approach exponentially fast,i.e.,

$$
\| y _ { n } - y _ { n } ^ { * } \| \leq C o n s t \cdot \rho ^ { n } \qquad { \mathrm { f o r ~ a l l ~ } } n \geq 0
$$

with some $\rho$ satisfying $0 < \rho < 1$ (seeExercise XII.3).This is due to the attractivity of the invariant manifold $\mathcal { M } _ { h }$ Aproof isgiveninStoffer(1993),and itisbasedon techniques of Nipp $\&$ Stoffer(1992).Thisresult explainswhy strictly stable linear multistep methods have the same long-time behaviour as one-step methods.

Inthecontext of“geometric numerical integration”weare mainly interested in symplectic and/or symmetric methodswhich,for linear problems,are characterized by the condition $\zeta _ { 1 } ( - z ) \zeta _ { 1 } ( z ) \equiv 1$ (seeSect.VI.4.2).This,however,is only possible forsymmetric multistep methods(Exercise1）which cannot be strictly stable.

# XV.2.2Formal Analysis forWeaklyStableMethods

Theproof and the statement of Theorem2.1 break down as soon asat least one root of $\rho ( \zeta )$ ,different from1,hasmodulus one.Moreover,Example2.2 shows that we cannot expectaproperty like（2.3）with $\rho < 1$ Allwecan hopeforisto find an underlyingone-stepmethod asa formal series in $h$ Surprisingly,this providesalot ofinsight into the long-timedynamics ofweakly stable multistep methods.

Theorem2.4.Considera linearmultistepmethod(1.1),andassume that $\zeta = 1$ is asinglerootof $\rho ( \zeta ) = 0$ .Thenthereexistsauniqueformal expansion

$$
\bar { \phi } _ { h } ( y ) = y + h d _ { 1 } ( y ) + h ^ { 2 } d _ { 2 } ( y ) + \ldots .
$$

suchthat

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } \varPhi _ { h } ^ { j } ( y ) = h \sum _ { j = 0 } ^ { k } \beta _ { j } f \bigl ( \varPhi _ { h } ^ { j } ( y ) \bigr ) ,
$$

whereidentity isunderstood inthe sense offormal powerseries in $h$

If themultistepmethod is oforder $T$ ,thenalsotheunderlyingone-stepmethod isoforder $r$ ,i.e., $\varPhi _ { h } ( y ) - \varphi _ { h } ( y ) = \mathcal { O } ( h ^ { r + 1 } ) ,$

The formal series for $\varPhi _ { h } ( y )$ is called“step-transition operator”in the Chinese literature(seee.g.,Feng(1995),page274).Wecall it“underlying one-stepmethod". Notice that this theoremdoes not requireany stability assumption.

Proof.Expanding $ { \varPhi } _ { h } ^ { \ j } ( y )$ and $f \left( \varPhi _ { h } ^ { \jmath } ( y ) \right)$ into powers of $h$ ,a comparison of thecoefficientsyields

$$
\begin{array} { r l } & { \rho ^ { \prime } ( 1 ) d _ { 1 } ( y ) \ = \ \sigma ( 1 ) f ( y ) } \\ & { \rho ^ { \prime } ( 1 ) d _ { 2 } ( y ) \ = \ - \frac { \rho ^ { \prime \prime } ( 1 ) } { 2 } d _ { 1 } ^ { \prime } ( y ) d _ { 1 } ( y ) + \sigma ^ { \prime } ( 1 ) f ^ { \prime } ( y ) d _ { 1 } ( y ) } \\ & { \rho ^ { \prime } ( 1 ) d _ { j } ( y ) \ = \ \dots , } \end{array}
$$

where the three dots represent known functions depending on derivatives of $f ( y )$ and on $d _ { i } ( y )$ with $i < j$ Since $\rho ^ { \prime } ( 1 ) \neq 0$ byassumption,unique coefficient functionsd;（y）are obtained recursively.The statement on the order follows fromthe fact that the exact flow $\varphi _ { h } ( y )$ hasadefect $\mathcal { O } ( h ^ { r + 1 } )$ in the multistep formula. □

Thecomputation of the previous proof shows that the series (2.4) isa B-series. This follows rigorously from the results of Sect.II.1.4.Whereas the B-series representation of Runge-Kutta methods converges for sufficiently small $h$ ,thisisin general not the case for(2.4);see the next example.

Example2.5.Considera consistent two-step method

$$
\alpha _ { 2 } y _ { n + 2 } + \alpha _ { 1 } y _ { n + 1 } + \alpha _ { 0 } y _ { n } = h \big ( \beta _ { 2 } f _ { n + 2 } + \beta _ { 1 } f _ { n + 1 } + \beta _ { 0 } f _ { n } \big ) ,
$$

andapply itto thesimple system $\dot { y } = f ( t ) , \dot { t } = 1 .$ The $y$ -component of the underlying one-step method then takesthe form

$$
\varPhi _ { h } ( t _ { 0 } , y _ { 0 } ) = y _ { 0 } + \sum _ { j \geq 1 } h ^ { j } a _ { j } f ^ { ( j - 1 ) } ( t _ { 0 } ) .
$$

Putting $f ( t ) = e ^ { t }$ yields

$$
A ( \zeta ) = \sum _ { j \geq 1 } a _ { j } \zeta ^ { j - 1 } = \frac { \beta _ { 2 } e ^ { 2 \zeta } + \beta _ { 1 } e ^ { \zeta } + \beta _ { 0 } } { \alpha _ { 2 } ( 1 + e ^ { \zeta } ) + \alpha _ { 1 } } .
$$

for the generating function of the coefficients $a _ { j }$ Sincethis function has finite poles, theradius of convergence of $A ( \zeta )$ isfinite.Therefore,the radius of convergence ofthe series (2.6) has to be zero as soon as $f ^ { ( j ) } ( t _ { 0 } )$ behaves like $j ! \mu \kappa ^ { \mathcal { I } }$ （thisis typically thecase foranalytic functions).Independent of the fact whether themethod is strictly stable or not,the series (2.6) usually does not converge.

Both,Theorem 2.1 and Theorem 2.4,extend ina straightforward manner to partitioned multistep methods(1.14).To get analogous results for multistep methods (1.8)for second order differential equations,one has to introduce an approximation forthe velocity $v = { \dot { y } } .$ Thiswillbeexplained inmoredetail in Sect.XV.3below.

# XV.3Backward Error Analysis

Thebackward error analysis for multistep methods (Hairer 1999) is presented in two steps:

·for“smooth”numerical solutions (obtained by the underlying one-step method);   
·for the general case.

Theidealized situation of no parasitic terms gives already much insight into conservationproperties of the method (see Sect.XV.4).The study of the general case is, however,necessary for getting estimates for the parasitic solutions(Sect.XV.5）,so thatrigorous statements on the long-time behaviour are possible.

# XV.3.1 Modified Equation for Smooth Numerical Solutions

Theformal backward erroranalysis ofChap.IX couldbe directlyapplied to the underlying one-stepmethod ofSect.XV.2.2.However,due to thenon-convergenceof the series for $\varPhi _ { h } ( y )$ ,difficulties may ariseas soon as rigorous estimates are desired. Weprefer to derive the modified differential equationdirectly from the multistep formula and thus avoid the use of the underlying one-step method.

Theorem 3.1.Considera linear multistepmethod(1.1),andassumethat $\rho ( 1 ) = 0$ and $\rho ^ { \prime } ( 1 ) = \sigma ( 1 ) \neq 0$ Then there exist unique $h$ -independentfunctions $f _ { j } ( y )$ such that,forevery truncationindex $N$ ,every solution of

$$
\dot { y } = f ( y ) + h f _ { 2 } ( y ) + h ^ { 2 } f _ { 3 } ( y ) + \ldots + h ^ { N - 1 } f _ { N } ( y )
$$

satisfies

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y ( t + j h ) = h \sum _ { j = 0 } ^ { k } \beta _ { j } f { \big ( } y ( t + j h ) { \big ) } + { \mathcal O } ( h ^ { N + 1 } ) .
$$

If themultistepmethodisoforder $r$ ,then $f _ { j } ( y ) = 0 f o r 2 \leq j \leq r .$ If themethod is symmetric,then $f _ { j } ( y ) = 0$ forall even $j$ ,sothat themodifiedequation(3.1) hasan expansion in even powers of $h$

Proof.Using theLiederivative $( D _ { i } g ) ( y ) = g ^ { \prime } ( y ) f _ { i } ( y )$ (with $f _ { 1 } ( y ) = f ( y ) )$ and $D = D _ { 1 } + h D _ { 2 } + h ^ { 2 } D _ { 3 } + . . . ,$ thesolutionof(3.1）withinitial value $y ( t ) = y$ satisfies $y ( t + j h ) = e ^ { j h D } y + \mathcal O ( h ^ { N + 1 } )$ and $f ( y ( t + j h ) ) = e ^ { j h D } f ( y ) + { \mathcal { O } } ( h ^ { N + 1 } )$ (by Taylor expansion).We thus have

$$
\rho ( e ^ { h D } ) y = h \sigma ( e ^ { h D } ) f ( y ) + \mathcal { O } ( h ^ { N + 1 } ) .
$$

With the expansion $x \sigma ( e ^ { x } ) / \rho ( e ^ { x } ) = 1 + \mu _ { 1 } x + \mu _ { 2 } x ^ { 2 } + . . .$ this becomes

$$
\dot { y } = ( 1 + \mu _ { 1 } h D + \mu _ { 2 } h ^ { 2 } D ^ { 2 } + . . . ) f ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

A comparison with (3.1) yields $f _ { 1 } ( y ) = f ( y )$ ,and

$$
f _ { j } ( y ) = \sum _ { l \geq 1 } \mu _ { l } \sum _ { j _ { 1 } + \ldots + j _ { l } = j - 1 } \left( D _ { j _ { 1 } } \ldots D _ { j _ { l } } f \right) ( y )
$$

for $j \geq 2$ ,whichuniquelydefines the functions $f _ { j } ( y )$ in a recursive manner.

Lemma 3.2. If $f ( y )$ is analyticandbounded by $M$ in $B _ { R } ( y _ { 0 } )$ ,thenwe have

$$
\left\| f _ { j } ( y ) \right\| \leq \mu M \bigg ( \frac { \eta M j } { R } \bigg ) ^ { j - 1 } \qquad f o r \qquad \| y - y _ { 0 } \| \leq R / 2 ,
$$

where $\mu$ and $\eta$ depend only onthecoefficients $\alpha _ { j } , \beta _ { j }$ ofthemultistep method.

Proof.The estimate(3.6)isobtained asintheproofof TheoremIX.7.5.We just sketch the main idea in the notation used there.With $\delta = R / ( 2 ( J - 1 ) )$ wehave $\| f _ { j } \| _ { j } \le \delta b _ { j }$ ,where the generating function $\begin{array} { r } { b ( \zeta ) = \sum _ { j \geq 1 } b _ { j } \zeta ^ { j } } \end{array}$ of the $b _ { j }$ satisfies

$$
b ( \zeta ) = \frac { M \zeta } { \delta } \Big ( 1 + \sum _ { l \geq 1 } | \mu _ { l } | \ : b ( \zeta ) ^ { l } \Big ) .
$$

By the implicit function theorem, $b ( \zeta )$ isanalyticand boundedinadiscof radius $c \delta / M$ centred at the origin（ $c$ isapositive constant depending only on the coefficients of themultistepmethod).The estimate (3.6) then follows from Cauchy's inequalitiesasin theproof of Theorem IX.7.5. □

Itisremarkable that,although the Taylor series of the underlying one-step method generally diverges,the coefficient functions of themodifieddifferential equation satisfy the same estimate asfor Runge-Kutta methods.This enablesus toproveananalogue of Theorem IX.7.6which,for one-stepmethods,isthe main ingredient for exponentially small error estimates.One can prove that for suitably chosen $N = N ( h )$ and for $h \leq h _ { 0 } / 4$ with $h _ { 0 } = R / ( e \eta M )$ ,the solution of (3.1) satisfies

$$
\Big | \Big | \sum _ { j = 0 } ^ { k } \alpha _ { j } y ( t + j h ) - h \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( y ( t + j h ) \big ) \Big | \Big | \leq h \gamma M e ^ { - h _ { 0 } / h } ,
$$

where $\gamma$ depends only on the multistep formula.Theproof of thisstatement is similartothat ofTheoremIX.7.6.Weskipdetailsand referto Hairer(1999).

Forstrictly stable multistepmethods,Theorem 2.1 together with the Invariant Manifold Theorem XII.3.2 thusimply that theunderlyingone-stepmethod is exponentially close to the exact solution of the truncated modified equation.The parasitic solution terms are rapidly damped out by the property(2.3) of asymptoticphase.The sameconclusions as for one-step methods can therefore be drawn.

Forsymmetric methods the situation is not so simple.One has to study the parasitic solution components to get information on the long-time behaviour of the numerical solution of(1.1). The basic techniqueswill be prepared in Sect.XV.3.2.

Partitioned MultistepMethods.The extension of the modified differential equation tomethods(1.14) is straightforward.There exist functions $f _ { j } ( y , v )$ and $g _ { j } ( y , v )$ such that the exact solution of

$$
\begin{array} { l } { { \dot { y } = f ( y , v ) + h f _ { 2 } ( y , v ) + . . . + h ^ { N - 1 } f _ { N } ( y , v ) } } \\ { { \dot { v } = g ( y , v ) + h g _ { 2 } ( y , v ) + . . . + h ^ { N - 1 } g _ { N } ( y , v ) } } \end{array}
$$

satisfies the multistep formula(1.14)uptoadefect of size ${ \mathcal { O } } ( h ^ { N + 1 } ) .$ The coefficient functions can be computed by comparing（3.7）to

$$
\begin{array} { l } { { \dot { y } = ( 1 + \mu _ { 1 } ^ { ( A ) } h D + \mu _ { 2 } ^ { ( A ) } h ^ { 2 } D ^ { 2 } + . . . . ) f ( y , v ) + \mathcal { O } ( h ^ { N } ) } } \\ { { \dot { v } = ( 1 + \mu _ { 1 } ^ { ( B ) } h D + \mu _ { 2 } ^ { ( B ) } h ^ { 2 } D ^ { 2 } + . . . ) g ( y , v ) + \mathcal { O } ( h ^ { N } ) , } } \end{array}
$$

where the real numbers $\mu _ { j } ^ { ( A ) }$ and $\mu _ { j } ^ { ( B ) }$ are given by $x \sigma ^ { ( A ) } ( e ^ { x } ) / \rho ^ { ( A ) } ( e ^ { x } ) = 1 +$ $\mu _ { 1 } ^ { ( A ) } x + \mu _ { 2 } ^ { ( A ) } x ^ { 2 } + \ldots$ and by $x \sigma ^ { ( B ) } ( e ^ { x } ) / \rho ^ { ( B ) } ( e ^ { x } ) = 1 + \mu _ { 1 } ^ { ( B ) } x + \mu _ { 2 } ^ { ( B ) } x ^ { 2 } + . . . ,$ , respectively.The Lie operator is defined by $D = D _ { 1 } + h D _ { 2 } + h ^ { 2 } D _ { 3 } + . . . ,$ where $( D _ { j } \psi ) ( y , v ) = \varPsi _ { y } ( y , v ) f _ { j } ( y , v ) + \varPsi _ { z } ( y , v ) g _ { j } ( y , v )$ ,and itcorresponds tothe time derivative of solutions of(3.7).

Multistep Methods for Second Order Differential Equations.The method(1.8) for differential equations $\ddot { y } = f ( y )$ canbe treatedina similarway.In the absence ofderivative approximations we get a modified differential equation of the second order

$$
\ddot { y } = f ( y ) + h f _ { 2 } ( y , \dot { y } ) + \ldots + h ^ { N - 1 } f _ { N } ( y , \dot { y } ) ,
$$

where the perturbation terms also depend on $\dot { y } .$ Its exact solution satisfies the multisteprelation（1.8）up toa defect of size $\mathcal { O } ( h ^ { N + 2 } )$ ,if（3.9)is equivalent to

$$
\ddot { y } = ( 1 + \mu _ { 1 } h D + \mu _ { 2 } h ^ { 2 } D ^ { 2 } + \ldots ) f ( y ) + \mathcal { O } ( h ^ { N } ) ,
$$

where $x ^ { 2 } \sigma ( e ^ { x } ) / \rho ( e ^ { x } ) ~ = ~ 1 + \mu _ { 1 } x + \mu _ { 2 } x ^ { 2 } + . . . .$ ,andthe timederivativeis given by the Lie operator $D = D _ { 1 } + h D _ { 2 } + h ^ { 2 } D _ { 3 } + \ldots$ with $( D _ { 1 } \varPsi ) ( y , \dot { y } ) =$ $\varPsi _ { y } ( y , \dot { y } ) \dot { y } + \varPsi _ { \dot { y } } ( y , \dot { y } ) f ( y )$ and $( D _ { j } \varPsi ) ( y , \dot { y } ) = \varPsi _ { \dot { y } } ( y , \dot { y } ) f _ { j } ( y , \dot { y } )$ for $j \geq 2 .$ Acomparison of equal powers of $h$ in(3.9）and(3.1O) uniquelydefines the coefficient functions $f _ { j } ( y , \dot { y } )$ .

Ifthemultistep method(1.8) is complemented witha difference formula for approximations of the derivative $v = \dot { y }$ at grid points,

$$
v _ { n } = \frac { 1 } { h } \sum _ { j = - l } ^ { l } \delta _ { j } y _ { n + j } ,
$$

we get an additional modified differential equation

$$
v = ( 1 + \nu _ { 1 } h D + \nu _ { 2 } h ^ { 2 } D ^ { 2 } + \ldots ) \dot { y } .
$$

The coefficients $\nu _ { j }$ are given by $x ^ { - 1 } \delta ( e ^ { x } ) = 1 + \nu _ { 1 } x + \nu _ { 2 } x ^ { 2 } + . . . .$ where $\begin{array} { r } { \delta ( \zeta ) = \sum _ { j = - l } ^ { l } \delta _ { j } \zeta ^ { j } . } \end{array}$ For given $y$ ,thisrelationgivesaformalonetoonecorrespon dence between $\upsilon$ and $\dot { y }$ Consequently,thedifferential equation(3.1O）combined with(3.12)can beconsidered asafirst order differential system for thevariables $y$ and $\boldsymbol { U }$ .

# XV.3.2 Parasitic Modified Equations

In practice,due to the necessity of starting approximations $y _ { 1 } , \ldots , y _ { k - 1 }$ ,the numerical solution of amultistep method does not lie onasolution of(3.1).Formethods, where initial perturbations are not damped out sufciently fast (cf.property (2.3) ofasymptotic phase),an additional investigation is therefore needed for the study of the propagation of perturbations in the starting approximations.Letus start with twoillustrating numerical experiments.

Example 3.3.Consider the explicit,linear 3-step method

$$
y _ { n + 3 } - y _ { n + 2 } + y _ { n + 1 } - y _ { n } = h ( f _ { n + 2 } + f _ { n + 1 } ) ,
$$

with characteristic polynomial $\rho ( \zeta ) = ( \zeta - 1 ) ( \zeta ^ { 2 } + 1 )$ ,and apply it to thependulum equation (I.1.13).Fora better illustration of the propagation of errorswe consider starting approximations $y _ { 1 } , y _ { 2 }$ that arerather far from the exact solution passing through $y _ { 0 }$ Theresult is shown in Fig.3.1.Weobserve that the numerical solution doesnot lie on one smooth curve,but on four curves,and every fourth solution approximation is on the same curve.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/c3e74e9b790d2621f1b38448375957f316fc511fc776443357ff628cc4151c64.jpg)  
Fig.3.1.Numerical solution of(3.13)applied to thependulumequation.The initial approximations $y _ { 0 } = ( 1 . 9 , 0 . 4 )$ , $y _ { 1 } = ( 1 . 7 , 0 . 2 )$ , $y _ { 2 } = ( 2 . 1 , 0 )$ areindicated by black bullets;the solution points $y _ { 3 } , y _ { 7 } , y _ { 1 1 } , \dots$ ingrey

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/457ad2b00ca1d668ecce1a0fca42847b94f00ae1a5a8774408a2113de94e6f51.jpg)  
Fig.3.2.Numerical solution of the explicit midpoint rule(3.14） applied to thependulum equation.The initial approximations $y _ { 0 } = ( 1 . 9 , 0 . 4 )$ , $y _ { 1 } = ( 1 . 7 , 0 . 2 )$ areindicated by black bullets;the solution points $y _ { 2 } , y _ { 4 } , y _ { 6 } , \ldots$ in grey

Thisexample shows an unexpected good long-time behaviour.Although the startingapproximationsare farfromasmooth solution,the distanceof the numerical approximations toa smooth solution curve does not increase.This is,however, not the typical situation as can be seen from our next experiment.

Example 3.4.We consider the explicit midpoint rule

$$
y _ { n + 2 } - y _ { n } = 2 h f _ { n + 1 } ,
$$

which has $\rho ( \zeta ) = ( \zeta - 1 ) ( \zeta + 1 )$ ascharacteristic polynomial.This time,the numerical solution(see Fig.3.2)lies ontwosmooth curves.Incontrast to theprevious example,anunacceptable linear growth ofthe perturbationscan be observed.

Tobeable to explain this behaviour of the multistep solutions,we complement theanalysis of the modified equation for smooth numerical solutionswith so-called parasiticmodified equations.This theory has been developedbyHairer(1999) for first order differential equations,and extended to second order systems byHairer& Lubich(2004).

Consider a stable,symmetric multistepmethod(1.1） and denote the zeros of its characteristic polynomial $\rho ( \zeta )$ by $\zeta _ { 1 } = 1$ （principal root） and $\zeta _ { 2 } , \ldots , \zeta _ { k }$ (parasitic roots).We then enumerate the set of all finite products,

$$
\left\{ \zeta _ { \ell } \right\} _ { \ell \in \mathcal { T } } = \Big \{ \zeta = \zeta _ { 1 } ^ { m _ { 1 } } \cdot . . . . \cdot \zeta _ { k } ^ { m _ { k } } ; m _ { j } \geq 0 \Big \} = \big \{ \zeta _ { 1 } , . . . , \zeta _ { k } , \zeta _ { k + 1 } , . . . , \big \} ,
$$

Itis $\{ 1 , i , - i , - 1 \}$ formethod(3.13）and $\{ 1 , - 1 \}$ for the explicit midpoint rule (3.14).The set of subscripts $\mathcal { L }$ can be finite or infinite.We let $\mathcal { Z } ^ { \ast } = \mathcal { I } \backslash \{ 1 \}$ ,and we denote by $\mathcal { T } _ { N } ^ { * }$ and $\mathcal { I } _ { N }$ thefinite subsets of elements which,in the representation (3.15),have $\sum _ { j } m _ { j } < N$ .

Motivated by the previous examplesand by representations of the asymptotic expansion of the global error ofweakly stable multistep methods (see for example Sect.III.9ofHairer,Nprsett&Wanner,1993),we aimatwriting the general solution $y _ { n }$ of themultistep method(1.1）in the form

$$
y _ { n } = y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h ) ,
$$

where $y ( t )$ and $z _ { \ell } ( t )$ aresmooth functions (with derivatives bounded independently of $h$ ).The followingresult extends Theorem 3.1.

Theorem3.5.Considera stable,consistent,and symmetric multistepmethod(1.1). Forevery truncation index $ { N _ { \mathrm { ~ \scriptsize ~ \geq ~ 2 ~ } } }$ ，therethenexist $h$ -independentfunctions $f _ { \ell , j } ( y , \mathbf z ^ { * } )$ with $\mathbf { z } ^ { \ast } = ( z _ { \ell } ) _ { \ell = 2 } ^ { k }$ such that for every solution of

$$
\begin{array} { r l r } & { \dot { y } = f _ { 1 , 1 } ( y , \mathbf { z } ^ { * } ) + h f _ { 1 , 2 } ( y , \mathbf { z } ^ { * } ) + . . . . + h ^ { N - 1 } f _ { 1 , N } ( y , \mathbf { z } ^ { * } ) } \\ & { \dot { z } _ { \ell } = f _ { \ell , 1 } ( y , \mathbf { z } ^ { * } ) + h f _ { \ell , 2 } ( y , \mathbf { z } ^ { * } ) + . . . . + h ^ { N - 1 } f _ { \ell , N } ( y , \mathbf { z } ^ { * } ) } & { f o r ~ 2 \le \ell \le k } \\ & { z _ { \ell } = h f _ { \ell , 2 } ( y , \mathbf { z } ^ { * } ) + . . . + h ^ { N } f _ { \ell , N + 1 } ( y , \mathbf { z } ^ { * } ) } & { f o r ~ \bar { \ell } > k } \\ & { z _ { \ell } = 0 ~ f o r ~ \ell \notin \mathcal { T } _ { N } } \end{array}
$$

with initial values $z _ { \ell } ( 0 ) = \mathcal { O } ( h ) f o r 2 \leq \ell \leq k ,$ thefunction

$$
x ( t ) = y ( t ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { t / h } z _ { \ell } ( t )
$$

satisfies

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } x ( t + j h ) = h \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( x ( t + j h ) \big ) + { \cal O } ( h ^ { N + 1 } ) .
$$

For $\mathbf { z } ^ { * } = 0$ thedifferential equationfor $y$ isthesameasthatofTheorem3.1.The solutions of(3.17) satisfy $z _ { \ell } ( t ) = \overline { { z _ { j } } } ( t )$ whenever $\zeta _ { \ell } = \overline { { \zeta _ { j } } }$ andthis relation holds fortheinitial values.Moreover $z _ { \ell } ( t ) = \mathcal { O } ( h ^ { m + 1 } )$ onboundedtimeintervalsif $\zeta _ { \ell }$ isaproduct ofno fewer than $m \geq 2$ rootsof $\rho ( \zeta )$

Proof.We let $z _ { 1 } ( t ) : = y ( t )$ and insert the finite sum(3.18)into(3.19).This yields

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 0 } ^ { k } \alpha _ { j } x ( t + j h ) ~ = ~ \sum _ { j = 0 } ^ { k } \alpha _ { j } \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { ( t + j h ) / h } e ^ { j h D } z _ { \ell } ( t ) } } \\ { { ~ = ~ \displaystyle \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { t / h } \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta _ { \ell } ^ { j } e ^ { j h D } z _ { \ell } ( t ) ~ = ~ \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { t / h } \rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } ( t ) , } } \end{array}
$$

where,asusual, $\mathcal { D }$ represents differentiation with respect to time.We then expand $f \left( \boldsymbol { x } ( t ) \right)$ intoa Taylor series around $y ( t )$ ,

$$
\begin{array} { r c l } { f ( \boldsymbol { x } ( t ) ) } & { = } & { \displaystyle \sum _ { m \ge 0 } \frac { 1 } { m ! } f ^ { ( m ) } ( \boldsymbol { y } ( t ) ) \Big ( \sum _ { \ell _ { 1 } \in \mathcal { Z } ^ { * } } \zeta _ { \ell _ { 1 } } ^ { t / h } z _ { \ell _ { 1 } } ( t ) , \ldots , \sum _ { \ell _ { m } \in \mathcal { Z } ^ { * } } \zeta _ { \ell _ { m } } ^ { t / h } z _ { \ell _ { m } } ( t ) \Big ) } \\ & { = } & { \displaystyle \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { t / h } \sum _ { m \ge 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( \boldsymbol { y } ( t ) ) \big ( z _ { \ell _ { 1 } } ( t ) , \ldots , z _ { \ell _ { m } } ( t ) \big ) . } \end{array}
$$

This gives,as above,

$$
\begin{array} { l l } { { } } & { { \displaystyle \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( x ( t + j h ) \big ) } } \\ { { } } & { { = \displaystyle \sum _ { \ell \in \mathbb { Z } } \zeta _ { \ell } ^ { t / h } \sigma ( \zeta \ell e ^ { h D } ) \displaystyle \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta , \ell } f ^ { ( m ) } \big ( y ( t ) \big ) \big ( z _ { \ell _ { 1 } } ( t ) , . . . , z _ { \ell _ { m } } ( t ) \big ) . } } \end{array}
$$

Comparing coefficients of $\boldsymbol { \zeta } _ { \ell } ^ { t / h }$ for $\ell \in \mathcal { L } _ { N }$ in (3.19) thus yields

$$
\rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = h \sigma ( \zeta _ { \ell } e ^ { h D } ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { { \bar { \zeta } } _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) ( z _ { \ell _ { 1 } } , \ldots , z _ { \ell _ { m } } )
$$

(for $\ell = 1$ and $m = 0$ the sum isunderstood to include the term $f ( y )$ ).With the expansion $x \sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } ) = \mu _ { \ell , 0 } + \mu _ { \ell , 1 } x + \mu _ { \ell , 2 } x ^ { 2 } + . . . .$ for $1 \le \ell \le k$ ,where $\zeta _ { \ell }$ isasimple root of $\rho ( \zeta )$ ,this equation becomes

$$
\dot { z } _ { \ell } = \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \tilde { \zeta } _ { \ell _ { 1 } } . . . \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \big ( z _ { \ell _ { 1 } } , . . . , z _ { \ell _ { m } } \big ) ,
$$

and with $\sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } ) = \mu _ { \ell , 0 } + \mu _ { \ell , 1 } x + \mu _ { \ell , 2 } x ^ { 2 } + \dots .$ for $\ell > k$ ,where $\rho ( \zeta _ { \ell } ) \neq 0$ ,

$$
z _ { \ell } = h \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } , . . . \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \big ( z _ { \ell _ { 1 } } , . . . , z _ { \ell _ { m } } \big ) ,
$$

Intheusual way(elimination of the first and higher derivativesby the differential equationsand by the differentiated thirdrelation of(3.17)) thisallowsus to define recursively the functions $f _ { \ell , j } ( y , \mathbf z ^ { * } )$ ,

From this construction processit follows that on bounded time intervalswe have $z _ { \ell } ( t ) = \mathcal { O } ( h )$ forall $\ell \geq 2$ ,and $z _ { \ell } ( t ) = \mathcal { O } ( h ^ { m + 1 } )$ if $\zeta _ { \ell }$ isa product of no fewer than $m \geq 2$ rootsof $\rho ( \zeta )$ In(3.2O)and in the above construction of the coefficient functions $f _ { \ell , j } ( y , \mathbf z ^ { * } )$ we have neglected terms that contain at least $N$ factors $z _ { j } .$ This gives rise to the $\mathcal { O } ( h ^ { N + 1 } )$ term in (3.19). □

Initial values $y ( 0 )$ ， $z _ { \ell } ( 0 ) , \ell = 2 , \ldots , k$ ,for the system(3.17)are obtained from thestarting approximations $y _ { 0 } , \ldots , y _ { k - 1 }$ via therelation

$$
y _ { j } = y ( j h ) + \sum _ { \ell \in \mathcal { T } ^ { * } } \zeta _ { \ell } ^ { j } z _ { \ell } ( j h ) , \quad j = 0 , 1 , \dots , k - \backslash 1 .
$$

For $h = 0$ thisrepresentsa linear Vandermonde system for $y ( 0 )$ , $z _ { \ell } ( 0 )$ TheImplicitFunction Theorem thus proves the local existence ofa solution of(3.24) for sufficiently small step sizes $h$ .If $y _ { j } , j = 2 , \ldots , k$ approximatea solution $y _ { e x } ( t )$ of $\dot { y } = f ( y )$ withanerror $\mathcal { O } ( h ^ { s } )$ (with $s \leq r + 1$ ,where $T$ is the order of the method), then $y ( 0 ) - y _ { e x } ( 0 ) = \mathcal { O } ( h ^ { s } )$ and $z _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } )$ for $\ell = 2 , \ldots , k$ .

Therepresentation (3.16) of the numerical solution and the (principal and parasitic)modified equations (3.17)will be themain ingredients for the study of longterm stability of multistepmethods in Sect.XV.5.An extension of the previous theoremtopartitioned multistepmethodsis more or less straightforward.We leave the details asan exercise for thereader.

Multistep Methods for Second Order Differential Equations.A completely analogousresult can be proved for stable,symmetric multistepmethods(1.8)appliedto $\ddot { y } = f ( y )$ .Weagain denote the zeros of $\rho ( \zeta )$ by $\zeta _ { 1 } = 1$ and $\zeta _ { \ell } , \ell = 2 , \ldots , q$ Notice,however,that $\zeta _ { 1 } = 1$ isalwaysa double zero,and the others can be simple ordouble zeros of $\rho ( \zeta )$ ,andthat $q \leq k$ Weconsider the index sets $\mathcal { L }$ , $\boldsymbol { \mathcal { L } ^ { * } }$ , $\mathcal { I } _ { N }$ ,and $\mathcal { T } _ { N } ^ { * }$ asin (3.15).

Theorem 3.6.Consider a stable,consistent,and symmetric multistepmethod(1.8). Forevery truncation index $N \geq 2$ ，there then exist $h$ -independent functions $f _ { \ell , j } ( y , \dot { y } , \mathbf z ^ { * } )$ (where ${ \mathbf z } ^ { \ast }$ denotes the vectorcollectingas elements $z _ { \ell } , \dot { z } _ { \ell }$ if $\zeta _ { \ell }$ is $a$ doubleroot,and $z _ { \ell }$ if $\zeta _ { \ell }$ is $\alpha$ simpleroot of $\rho ( \zeta )$ )suchthat foreverysolutionof

$$
\begin{array} { l l } { \ddot { y } } & { = \ f _ { 1 , 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + h f _ { 1 , 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N - 1 } f _ { 1 , N } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad ( 3 . } \\ { \ddot { z } _ { \ell } } & { = \ f _ { \ell , 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N - 1 } f _ { \ell , N } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad i f \ \rho ( \zeta _ { \ell } ) = \rho ^ { \prime } ( \zeta _ { \ell } ) = 0 } \\ { \dot { z } _ { \ell } } & { = \ h f _ { \ell , 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N } f _ { \ell , N + 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad \ i f \ \rho ( \zeta _ { \ell } ) = 0 , \rho ^ { \prime } ( \zeta _ { \ell } ) \neq } \\ { z _ { \ell } } & { = \ h ^ { 2 } f _ { \ell , 3 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N + 1 } f _ { \ell , N + 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad \ i f \ \rho ( \zeta _ { \ell } ) \neq 0 } \\ { z _ { \ell } } & { = \ 0 \qquad f o r \ \ell \notin \mathcal { X } _ { N } } \end{array}
$$

with initial values $z _ { \ell } ( 0 ) = \mathcal O ( h ) f o r 2 \le \ell \le q$ thefunction

satisfies

$$
x ( t ) = y ( t ) + \sum _ { \ell \in \mathbb { Z } ^ { \star } } \zeta _ { \ell } ^ { t / h } z _ { \ell } ( t )
$$

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } x ( t + j h ) \stackrel { } { = } h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( x ( t + j h ) \big ) + { \mathcal O } ( h ^ { N + 2 } ) .
$$

For $\mathbf { z } ^ { * } = 0$ thedifferential equation for $y$ is the same as in(3.9).The solutions of (3.25）satisfy $z _ { \ell } ( t ) = \overline { { z _ { j } } } ( t )$ whenever $\zeta _ { \ell } = \zeta _ { j }$ andthisrelationholdsfortheinitial values.Moreover, $z _ { \ell } ( t ) = \mathcal { O } ( h ^ { m + 2 } )$ on boundedtime intervalsif $\zeta _ { \ell }$ is aproduct of no fewerthan $m \geq 2$ rootsof $\rho ( \zeta )$ .

Proof.Incompleteanalogytotheproof ofTheorem3.5we obtain

$$
\rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = h ^ { 2 } \sigma ( \zeta _ { \ell } e ^ { h D } ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { { \zeta _ { \ell _ { 1 } } . . . \zeta _ { \ell _ { m } } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) ( z _ { \ell _ { 1 } } , . . . . , z _ { \ell _ { m } } )
$$

which differs from (3.21） only in the factor $h ^ { 2 }$ .Depending on whether $\zeta _ { \ell }$ is adouble,a simple,or nota zero of $\rho ( \zeta )$ ,weexpand $x ^ { 2 } \sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } )$ or $x \sigma ( \zeta e e ^ { x } ) / \rho ( \zeta e e ^ { x } )$ or $\sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } )$ intoa series of powers of $x$ ,andwedenote its coefficients by $\mu _ { \ell , j } .$ This then yields

$$
\ddot { z } _ { \ell } = \Bigl ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + \ldots \Bigr ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \bigl ( z _ { \ell _ { 1 } } , \ldots , z _ { \ell _ { m } } \bigr ) ,
$$

if $\rho ( \zeta _ { \ell } ) = \rho ^ { \prime } ( \zeta _ { \ell } ) = 0$ ,but $\rho ^ { \prime \prime } ( \zeta _ { \ell } ) \neq 0$ (in particular for $\ell = 1$ and $\zeta _ { 1 } = 1$ ）,

$$
\dot { z } _ { \ell } = h \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } , . . . \zeta _ { r _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \big ( z _ { \ell _ { 1 } } , . . . , z _ { \ell _ { m } } \big ) ,
$$

if $\rho ( \zeta _ { \ell } ) = 0$ ,but $\rho ^ { \prime } ( \zeta _ { \ell } ) \neq 0$ ,and

$$
z _ { \ell } = \bar { h } ^ { 2 } \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } . . . \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) ( z _ { \ell _ { 1 } } , . . . . , z _ { \ell _ { m } } \Big ) ,
$$

if $\rho ( \zeta _ { \ell } ) \neq 0 ,$ Therest of the proof is identical to that of Theorem 3.5.

For the system of modified equations(3.25）we need initial values $y ( 0 ) , \dot { y } ( 0 )$ , $z _ { \ell } ( 0 ) , \dot { z } _ { \ell } ( 0 )$ if $\zeta _ { \ell }$ isa double root of $\rho ( \zeta )$ ,and $z _ { \ell } ( 0 )$ if $\zeta _ { \ell }$ isa simpleroot.These initial values can be obtained from the starting approximations $y _ { 0 } , \ldots , y _ { k - 1 }$ via the relation (3.24）.

Lemma 3.7.Considera stable,symmetricmultistepmethod(1.8) oforder $r$ and let the starting approximations $y _ { 0 } , \ldots , y _ { k - 1 }$ satisfy $y _ { j } - y _ { e x } ( j h ) = \mathcal { O } ( h ^ { s } )$ with $2 \leq s \leq r + 2$ .Thenthereexist(locally)unique initial values for thesystem(3.25) such that its solution exactly satisfies(3.24).

These initial values satisfy $z _ { \ell } ( 0 ) = { \overline { { z _ { j } } } } ( 0 )$ if $\zeta _ { \ell } = \zeta _ { j }$ and

$$
\begin{array} { r l } & { y ( 0 ) - y _ { e x } ( 0 ) = \mathcal { O } ( h ^ { s } ) , \quad h \dot { y } ( 0 ) - h \dot { y } _ { e x } ( 0 ) = \mathcal { O } ( h ^ { s } ) , } \\ & { z _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } ) , \quad h \dot { z } _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } ) \qquad i f \zeta _ { \ell } i s a d o u b l e r o o t , } \\ & { z _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } ) , \qquad i f \zeta _ { \ell } i s a s i m p l e r o o t . } \end{array}
$$

ProofWe scale the derivatives by $h$ ,andconsider $y ( 0 )$ , $h \dot { y } ( 0 )$ , $z _ { \ell } ( 0 )$ and $h z _ { \ell } ( 0 )$ as unknowns in the system (3.24),where $y ( t )$ and $z _ { \ell } ( t )$ areasolution of(3.25）.For $h = 0$ alinear,confluent Vandermondesystemis obtained.Sincethisisaninvertible matrix,the Implicit Function Theorem provesthe statement. □

# XV.4 CanMultistep Methods be Symplectic?

Readers might beastonished to find aquestion mark in the title.Thereason is that we shall present two definitions of symplecticity ofmultistep methods applied toa Hamiltonian system

$$
\dot { p } = - H _ { q } ( p , q ) , \qquad \dot { q } = H _ { p } ( p , q ) .
$$

Oneworks in thephase space of the exact flow,the other ina higher dimensional space.But which one is suitable?We further show that certain multistep methods canpreserve energy overlong times,even if they are not symplectic.

# XV.4.1 Non-Symplecticity of the Underlying One-Step Method

A conjecture due to FengKang.

(Y.-F.Tang 1993)

Anatural definition of symplecticity consists of the requirement that the underlying one-step method(Theorem2.4)be symplectic.Thismeans that the (truncated) modified equation(3.1） isHamiltonian.Unfortunately,we havethe followingnegative result.

Theorem4.1 (Tang1993).Theunderlyingone-stepmethodofa consistent linear multistepmethod(1.1) cannotbesymplectic.

Proof.We show that the firstperturbation term in the modified equation (3.1) is in general not Hamiltonian.From(3.4）weknow that $f _ { r + 1 } ( y ) = \mu _ { r } ( D _ { 1 } ^ { r } f ) ( y )$ which (omitting the non-zero error constant $\mu _ { r }$ ）isgiven by

$$
\sum _ { \tau \in T , | \tau | = r + 1 } \alpha ( \tau ) F ( \tau ) ( y ) = | \tau | ! \sum _ { \tau \in T , | \tau | = r + 1 } \frac { 1 } { \sigma ( \tau ) } b ( \tau ) F ( \tau ) ( y )
$$

with $b ( \tau ) = 1 / \gamma ( \tau )$ for $| \tau | = r + 1$ (Theorem III.1.3 and(III.1.27)).Suppose nowthat(4.2) is Hamiltonian forall separable Hamiltonian vector fields $f ( y ) =$ $J ^ { - 1 } \nabla H ( y )$ TheoremIX.10.4 then implies

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } u , v \in T { \mathrm { ~ w i t h ~ } } | u | + | v | = r + 1 .
$$

This,however,isin contradiction with

$$
\frac { 1 } { \gamma ( u \circ v ) } + \frac { 1 } { \gamma ( v \circ u ) } = \frac { 1 } { \gamma ( u ) } \cdot \frac { 1 } { \gamma ( v ) } ,
$$

which isa consequence of TheoremVI.7.6(because the exact solution isa symplectictransformationand,asaB-series,hascoefficients $a ( \tau ) = 1 / \gamma ( \tau ) )$ . □

Asimilarnegativeresult holdsfora much largerclass of integrationmethods. Forexample,itisproved by Hairer&Leone（1998)that,amongtheclassofonelegmethods(see(4.7) below）,only the implicit mid-point rule issymplectic(in the sense that the underlying one-step method is symplectic).

PartitionedLinearMultistepMethods.Weknowat least onesymplectic method ofthe form(1.14).It is thesymplectic Euler method(VI.3.1),which combines the implicit and the explicit Euler methods.However,we do not have betterwithin the class of partitioned multistep methods as is shownin the next theorem.

Theorem4.2.If theunderlying one-stepmethodofaconsistent,partitionedlinear multistepmethod(1.14) issymplecticforall separable Hamiltoniansystems,then its order satisfies $r \leq 1$

Proof.Suppose that the order of themethodis $r \geq 2$ By(3.8）,the dominant perturbation terminthemodified differential equationis $\mu _ { r } ^ { ( A ) } h ^ { r } ( D _ { 1 } ^ { r } f ) ( y , z )$ forthe $y$ -component and $\mu _ { r } ^ { ( B ) } h ^ { r } ( D _ { 1 } ^ { r } g ) ( y , z )$ for the $z$ component (atleastoneoftheco efficients $\mu _ { r } ^ { ( A ) } / \gamma ( \tau )$ $\mu _ { r } ^ { ( A ) }$ $\tau \in T P _ { p } , | \tau | = r + 1$ and $\mu _ { r } ^ { ( B ) }$ is non-zero).ThisisaP-serieswithcoeficients and $b ( \tau ) = \mu _ { r } ^ { ( B ) } / \gamma ( \tau )$ if $\tau \in T P _ { q } , | \tau | = r + 1$ $b ( \tau ) =$ If theunderlying one-stepmethod is symplectic(i.e.,the modified differential equationislocallyHamiltonian),TheoremIX.1O.4 impliesthat

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \quad \mathrm { f o r } \quad u \in T P _ { p } , v \in T P _ { q } , | u | + | v | = r + 1 .
$$

Taking for $u \in \mathcal { I } ^ { \prime } P _ { p }$ the tree with one vertex,and for $v \in \mathop { \cal { I } } { \cal { I } } { \cal { I } } _ { q } ^ { \prime }$ anarbitrary treewith $| \boldsymbol { v } | = \boldsymbol { r }$ condition(4.3)gives the first relation of

$$
\frac { \mu _ { r } ^ { ( A ) } } { ( r + 1 ) \gamma ( v ) } + \frac { \mu _ { r } ^ { ( B ) } r } { ( r + 1 ) \gamma ( v ) } = 0 , \qquad \frac { \mu _ { r } ^ { ( B ) } } { ( r + 1 ) \gamma ( v ) } + \frac { \mu _ { r } ^ { ( A ) } r } { ( r + 1 ) \gamma ( v ) } = 0 .
$$

Exchanging the colour of the vertices gives the second relation.This contradicts our assumption $r \geq 2$ . □

If we restrict our considerations to Hamiltonian systems with

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } C p + c ^ { T } p + U ( q ) ,
$$

where the kinetic energy isat most quadraticin $p$ ,wecan find symplectic,partitionedmultistepmethods oforder two.Indeed,thecombination of the trapezoidal rulewith the explicitmidpoint rule

$$
p _ { n + 1 } - p _ { n } = - \frac { h } { 2 } \Big ( \nabla U ( q _ { n + 1 } ) + \nabla U ( q _ { n } ) \Big ) , \quad q _ { n + 1 } - q _ { n - 1 } = 2 h \big ( C p _ { n } + c \big )
$$

hasthe Stormer-Verlet method asunderlying one-step method.Thisis seen as follows:since theHamiltonianis separable,formula(VI.3.4）yields thefirst formula of(4.5).The second relation is a consequence of $q _ { n + 1 } - q _ { n } + h ( C p _ { n + 1 / 2 } + c )$ and $p _ { n + 1 / 2 } + p _ { n - 1 / 2 } = 2 p _ { n }$ ,and uses the linearity of $H _ { p } ( p , q )$ .

Also for this special class of Hamiltonian systemswecannot achieve high order and symplecticity at the same time.

Theorem4.3.If the underlyingone-stepmethodofaconsistent,partitioned linear multistepmethod(1.14)issymplecticforall Hamiltoniansystemswith Hamiltonian oftheform(4.4),thenitsordersatisfies $r \leq 2$ .

Proof.Thebeginningis thesameasthat for Theorem 4.2.Welet $r \geq 2$ be the order of themethod (A)so that $\mu _ { r } ^ { ( A ) } \neq 0$ Insteadof(4.3)wenowhavetouse

$$
b ( u \circ \circ v ) - b ( v \circ \circ u ) = 0 \qquad { \mathrm { f o r } } \quad u , v \in T N _ { p } , | u | + | v | = r ,
$$

whichalso follows from Theorem IX.10.4.Takingfor $u \in T N _ { p }$ the tree with one vertex,and for $v \in \mathop { I N _ { p } }$ anarbitrary treewith $| \boldsymbol { v } | = r - 1$ ,condition （4.6） gives the relation

$$
\frac { \mu _ { r } ^ { ( A ) } ( r - 1 ) } { 2 ( r + 1 ) \gamma ( v ) } - \frac { \mu _ { r } ^ { ( A ) } } { r ( r + 1 ) \gamma ( v ) } = 0 ,
$$

which is contradictory for $r > 2$ ,because $\mu _ { r } ^ { ( A ) } \neq 0$

Remark4.4.We believethatthestatement ofTheorem4.3remainstrue,ifwe restrict our considerationto Hamiltonian functions（4.4）with $c = 0$ and invertible matrix $C$ .Sincemultistepmethods(1.8) for second orderdifferential equations can beconverted intopartitioned multistep methods,this then implies that methods（1.8) cannot be symplectic unless the order satisfies $r \leq 2$ ,

# XV.4.2 Symplecticity intheHigher-Dimensional PhaseSpace

Wepresent herea second approach for thedefinition of symplecticity of multistep methods (more precisely,of one-legmethods).It ismuch inspired by the $G$ -stability theoryofDahlquist(1975)for thestudy of stiffdifferential equations.

Tosimplify the nonlinear stability theory of linear multistep methods(1.1), Dahlquist(1975) introduced the so-called one-legmethods,which aredefined by therelation

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y _ { n + j } \stackrel { } { = } h f \Big ( \sum _ { j = 0 } ^ { k } \beta _ { j } y _ { n + j } \Big ) ,
$$

where the normalization $\begin{array} { r } { \sigma ( 1 ) = \sum _ { j } \beta _ { j } = 1 } \end{array}$ isassumed.In fact,thereisa close relationship between thenumerical solution of（4.7）and（1.1）,and their long-time behaviour is the same(see Sect.V.6of Hairer $\&$ Wanner,1996).In the following we consider the super-vectors $Y _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ collecting $k$ consecutive approximations of the solution.

Definition 4.5.Let $G$ beaninvertible symmetric matrix of dimension $k$ A $k$ -step multistep or one-leg method is called $G$ -symplecticif

$$
Y _ { n + 1 } ^ { T } \left( G \otimes S \right) Y _ { n + 1 } = Y _ { n } ^ { T } \left( G \otimes S \right) Y _ { n } ,
$$

whenever thedifferential equation $\dot { y } = f ( y )$ has $y ^ { T } S y$ as invariant (with symmetric $S$ ),i.e.,the vectorfield satisfies $y ^ { T } S f ( y ) = 0$ forall $y$ .

Itisof course also possible to express this definition in terms ofdifferential forms.As a consequence ofLemma VI.4.1 the conservation of quadratic first integralsis equivalent to symplecticity(Bochev& Scovel 1994).

Incontrast to the negative results of Sect.XV.4.1,there exist a lot of $G$ - symplecticmethods.We have the followingresult.

Theorem4.6(Eirola&Sanz-Serna 1992).Every irreduciblesymmetric one-leg method(4.7）is $G$ -symplecticforsomematrix $G$ ,

Proof.Werecall that aone-legmethod is irreducible if thegeneratingpolynomials $\rho ( \zeta )$ and $\sigma ( \zeta )$ have no common zeros.

Construction of $G$ .Thesymmetry relation (1.3) implies $\rho ( 1 / \zeta ) = - \zeta ^ { - k } \rho ( \zeta )$ and $\sigma ( 1 / \zeta ) = \zeta ^ { - k } \sigma ( \zeta )$ Consequently,thepolynomial $\rho ( \zeta ) \sigma ( \omega ) + \rho ( \omega ) \sigma ( \zeta )$ vanishes for $\omega = 1 / \zeta$ ,and contains the factor $\zeta \omega - 1$ We thendefine $G$ by

$$
\frac { 1 } { 2 } \big ( \rho ( \zeta ) \sigma ( \omega ) + \rho ( \omega ) \sigma ( \zeta ) \big ) = ( \zeta \omega - 1 ) \sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { i - 1 } \omega ^ { j - 1 } .
$$

The matrix $G$ obtained in this way is symmetric.

Regularity of $G$ .Applying the geometric seriesweget

$$
\sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { i - 1 } \omega ^ { j - 1 } = - \frac { 1 } { 2 } \big ( \rho ( \zeta ) \sigma ( \omega ) \mp \rho ( \omega ) \sigma ( \zeta ) \big ) \big ( 1 + \zeta \omega + \zeta ^ { 2 } \omega ^ { 2 } + . . . . \big ) ,
$$

wherethe identity holds as formal power series.Suppose that thematrix $G$ isnot invertible.Then there existsa vector $u = ( u _ { 0 } , u _ { 1 } , \ldots , u _ { k - 1 } ) ^ { T }$ suchthat $G u =$ 0.Weformallyreplace the appearances of $\omega ^ { \mathcal { I } - 1 }$ with $u _ { j - 1 }$ for $j \ \leq \ k$ andwith zerofor $j > k .$ This gives an identity of the form $0 = \rho ( \zeta ) a ( \zeta ) + \sigma ( \zeta ) b ( \zeta )$ with polynomials $a ( \zeta )$ and $b ( \zeta )$ of degree at most $k - 1$ ,and we get a contradiction with the irreducibility of the method.

$G$ -Symplecticity.Wenextreplacein(4.9) $S ^ { i _ { \omega } , j }$ with $y _ { n + i } ^ { T } S y _ { n + j } .$ Together with （4.7） thisyields

$$
h \Bigl ( \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n + i } \Bigr ) ^ { T } S f \Bigl ( \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n + i } \Bigr ) = Y _ { n + 1 } ^ { T } ( G \otimes S ) Y _ { n + 1 } - Y _ { n } ^ { T } ( G \otimes S ) Y _ { n } ,
$$

where $Y _ { n } = ( y _ { n } , \dots , y _ { n + k - 1 } ) ^ { T } .$ This proves (4.8)for all functions $f ( y )$ satisfying $y ^ { T } S f ( y ) = 0$ □

Example 4.7.We consider the explicit midpoint rule(1.6),which is alsoa one-leg method,andthe3-stepmethod(3.13).By Theorem 4.6the one-legversionsare $G$ -symplectic.Following the constructive proof of this theorem we find

$$
G = { \left( \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right) } \qquad { \mathrm { a n d } } \qquad G = { \left( \begin{array} { l l l } { 0 } & { 1 } & { 1 } \\ { 1 } & { - 2 } & { 1 } \\ { 1 } & { 1 } & { 0 } \end{array} \right) } \ ,
$$

respectively.We apply both methodsto twoclosely related Hamiltoniansystems, namely the pendulum equation with $H ( p , q ) = p ^ { 2 } / 2 - \cos q$ and aperturbed problemwith $H ( p , q ) = p ^ { 2 } / 2 - \cos q ( 1 - p / 6 )$ ,and we study the preservation of the

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/e90f4b15b808b690bf78b42692d6084f3cc2664e4541a37a36de064d268d2c7d.jpg)  
Fig.4.1.Numerical Hamiltonian $H ( p _ { n } , q _ { n } ) - H ( p _ { 0 } , q _ { 0 } )$ of the explicit mid-pointruleand the 3-stepmethod(3.13),applied withstepsize $h = 0 . 0 1$ tothe pendulum problem $\quad ( H ( p , q ) =$ $p ^ { 2 } / 2 - \cos q )$ and toaperturbed problem $( H ( p , q ) = p ^ { 2 } / 2 - \cos q ( 1 - \stackrel { \triangledown } { p } / 6 ) )$ ontheinterval $[ 0 , 1 1 0 0 ]$ (only every 131st stepis drawn)

Hamiltonian (see Fig.4.1).The result is somewhat surprising.The midpoint rule behaveswellfor theperturbed problem,but showsa linearerror growth in the Hamiltonian for thependulumproblem.Onthe other side,theweakly stable 3-stepmethod behaveswell for thependulum equation (which is in agreement with the stable behaviour ofFig.3.1),but hasan exponential error growth for the perturbed problem. Notice that different scalesare used in the four pictures.

Theabove example illustrates that $G$ -symplecticity ofanumerical methodis notsufficient fora good long-time behaviour.Itis necessary to getunder control the parasitic solution components.

# XV.4.3Modified Hamiltonian of Multistep Methods

After the negative results of Sect.XV.4.1,we are fortunately also able toprove positiveresults concerning the near conservation of the Hamiltonian.

Theorem4.8.Fora symmetric,consistent linearmultistep method(1.1) oforder $r$ appliedto $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) } \end{array}$ ,thereexistsa seriesoftheform

$$
\widetilde H ( y ) = H ( y ) + h ^ { r } H _ { r + 1 } ( y ) + h ^ { r + 2 } H _ { r + 3 } ( y ) + \dots ,
$$

whichisaformalfirst integral of themodifiedequation(3.1)without truncation.

Proof.With $\rho ( e ^ { x } ) / ( x \sigma ( e ^ { x } ) ) = 1 + \gamma _ { r } x ^ { r } + \gamma _ { r + 2 } x ^ { r + 2 } + . . . .$ it follows from (3.3) that the solution of the modified differential equation satisfies

$$
( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \dot { y } = J ^ { - 1 } \nabla H ( y ) + \mathcal { O } ( h ^ { N } ) ,
$$

where,due to the symmetry of themethod,only odd derivatives of $y ( t )$ appear.We multiply both sideswith $\dot { y } ^ { T } J$ sothat theright-hand side becomes the total derivative $\begin{array} { r } { \frac { d } { d t } H ( y ) } \end{array}$ Ontheleft-hand sidewenote ${ \dot { y } } ^ { T } J { \dot { y } } \ = \ 0$ ， $\begin{array} { r } { \dot { y } ^ { T } J y ^ { ( 3 ) } = \frac { d } { d t } \big ( \dot { y } ^ { T } J \ddot { y } \big ) } \end{array}$ and similarly for higherderivatives

$$
\dot { y } ^ { T } J y ^ { ( 2 m + 1 ) } = \frac { d } { d t } \Bigl ( \dot { y } ^ { T } J y ^ { ( 2 m ) } - \dot { y } ^ { T } J y ^ { ( 2 m - 1 ) } + \ldots \pm y ^ { ( m ) T } J y ^ { ( m + 1 ) } \Bigr ) .
$$

Wethus obtaina time derivative of an expression inwhich the appearing derivatives can be substituted as functions of $y$ via the modified differential equation (3.1). Altogether this yields

$$
- \frac { d } { d t } \Bigl ( h ^ { r } H _ { r + 1 } ( y ) + h ^ { r + 2 } H _ { r + 3 } ( y ) + \ldots \Bigr ) = \frac { d } { d t } H ( y ) + { \cal O } ( h ^ { N } ) .
$$

which proves the statement.

The statement of the previous theorem is somewhat surprising.The underlying one-step method,although not symplectic,nearly conserves theHamiltonian for general $H ( y )$ (notevenreversibility isrequired).Thisindicatesthat thecondition (IX.9.2O)can be satisfied for all trees also by non-symplectic methods.

Forpartitioned multistep methodswe do not know of a similar resultunless if werestrict our consideration to Hamiltonians of the form (4.4).In this case we are concerned with multistep methods for second order differential equations.

Theorem4.9.Forasymmetric,consistentlinear multistepmethod(1.8)oforder $r$ appliedto $\ddot { y } = - \nabla U ( y )$ ,thereexistsa seriesoftheform

$$
\widetilde { H } ( y , \dot { y } ) = \frac { 1 } { 2 } \dot { y } ^ { T } \dot { y } + U ( y ) + h ^ { r } H _ { r + 1 } ( y , \dot { y } ) + h ^ { r + 2 } H _ { r + 3 } ( y , \dot { y } ) + \dots ,
$$

whichisaformalfirst integralofthemodifiedequation(3.9)without truncation.

Proof.Theproofisvery similarto thatoftheprevioustheorem.Weexpand $\rho ( e ^ { x } ) / ( x ^ { 2 } \sigma ( e ^ { x } ) ) = 1 + \gamma _ { r } x ^ { r } + \gamma _ { r + 2 } x ^ { r + 2 } + . . . ,$ and similar to(3.10) we obtain

$$
( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \ddot { y } = - \nabla U ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

This time we multiply both sides with ${ \dot { y } } ^ { T } .$ Theright-hand side becomes the total derivative $\begin{array} { r l } { \frac { d } { d t } { U } ( y ) } \end{array}$ and for the left-hand side we use $\begin{array} { r } { \dot { y } ^ { T } \ddot { y } = \frac { d } { d t } ( \dot { y } ^ { T } \dot { y } ) } \end{array}$ and for higher even-orderderivatives

$$
{ \dot { y } } ^ { T } y ^ { ( 2 m ) } = { \frac { d } { d t } } \Bigl ( { \dot { y } } ^ { T } y ^ { ( 2 m - 1 ) } - { \ddot { y } } ^ { T } y ^ { ( 2 m - 2 ) } + \ldots \pm { \frac { 1 } { 2 } } y ^ { ( m ) T } y ^ { ( m ) } \Bigr ) .
$$

Integrating and substituting second and higher derivatives of $_ y$ via the modified differential equation(3.9) yields the desired formal first integral close to the Hamiltonian of the system. □

The formal first integral (4.13） does not depend on how approximationsto the derivative $v = \dot { y }$ are obtained.If the derivativeat grid points is numerically computed with the formula (3.11),then one can use the one-to-one correspondence (3.12)to express the coeffcient functions of the modified differential equation in termsof $y$ and $\boldsymbol { v }$ .

# XV.4.4Modified Quadratic First Integrals

Symplectic one-step methods exactly preservequadratic first integrals(Sect.IV.2).   
Thisis not true for the underlying one-step method of symmetric multistep methods.   
However,aswe shall proveinthis section,it nearly preserves such first integrals.

Theorem4.10.Let $Q ( y ) = y ^ { T } C y$ (with $a$ symmetricmatrix $C$ )beafirst integral of $\dot { y } = f ( y )$ Forasymmetric,consistent linearmultistepmethod $( I , I )$ oforderr, therethenexistsaseriesoftheform

$$
\widetilde Q ( y ) = y ^ { T } C y + h ^ { r } Q _ { r + 1 } ( y ) + h ^ { r + 2 } Q _ { r + 3 } ( y ) + \dots ,
$$

whichisaformalfirst integralofthemodifiedequation(3.1)without truncation.

Proof.We multiply(4.11)with $y ^ { T } C$ und thus obtain

$$
y ^ { T } C ( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \dot { y } = y ^ { T } C f ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

Since $y ^ { \scriptscriptstyle T } C y$ isafirst integral,the termon theright-hand side vanishes.For the terms ontheleft-handside we notice that $\begin{array} { r } { y ^ { T } C \dot { y } = \frac { 1 } { 2 } \frac { d } { d t } ( y ^ { T } C y ) } \end{array}$ and that

$$
y ^ { T } C y ^ { ( 2 m + 1 ) } = { \frac { d } { d t } } { \Big ( } y ^ { T } C y ^ { ( 2 m ) } - { \dot { y } } ^ { T } C y ^ { ( 2 m - 1 ) } + \ldots \pm { \frac { 1 } { 2 } } y ^ { ( m ) T } C y ^ { ( m ) } { \Big ) } .
$$

Asin the proofs of Sect.XV.4.3 we now deduce the statement.

Asimilarresult holds for second orderdifferential equationsand methods(1.8). Thisconcerns for example the total angular momentum in $N$ -bodysystems.

Theorem4.11.Supposethat $\ddot { y } = f ( y )$ has $L ( y , \dot { y } ) = y ^ { T } E \dot { y }$ as first integral,i.e., $E$ isskew-symmetric and $y ^ { T } E f ( y ) = 0$ Forasymmetric,consistent linearmultistep method(1.8)of order $r$ ,therethenexistsa seriesof theform

$$
\tilde { L } ( y , \dot { y } ) = y ^ { T } E \dot { y } + h ^ { r } L _ { r + 1 } ( y , \dot { y } ) + h ^ { r + 2 } L _ { r + 3 } ( y , \dot { y } ) + \dots ,
$$

whichisa formal first integralofthemodifiedequation(3.9)without truncation.

Proof.Multiplying(4.14)with $y ^ { T } E$ gives

$$
y ^ { T } E ( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \ddot { y } = y ^ { T } E f ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

The term at theright vanishes.Since $\mathcal { L }$ isaskew-symmetricmatrix,we have for the terms tothe leftthat $\begin{array} { r } { y ^ { T } E \ddot { y } = \frac { d } { d t } y ^ { T } E \dot { y } } \end{array}$ and that

$$
y ^ { T } E y ^ { ( 2 m + 2 ) } = { \frac { d } { d t } } { \Big ( } y ^ { T } E y ^ { ( 2 m + 1 ) } - { \dot { y } } ^ { T } D y ^ { ( 2 m ) } + \ldots \pm y ^ { ( m ) T } E y ^ { ( m + 1 ) } { \Big ) } .
$$

Thisyields the statement as in the previous proofs.

Remark 4.12.Noticing that the underlying one-step method of a symmetric multistepmethod can beexpressed asa formal B-series(cf.Sect.XV.2.2),it follows from(4.17)that the modified first integral of Theorem 4.10is of the form(VI.8.6). ByTheorem VI.8.5 theunderlying one-stepmethod is thereforeconjugate toasymplectic integrator.

Asimilarresult holds for symmetric methods(1.8) complemented witha symmetric derivative approximation(3.11).The variables $\upsilon$ and $\dot { y }$ are related via(3.12) having an expansion in even powers of $h$ Substituting $\dot { y } = \dot { y } ( y , v )$ of thisrelation intothe modified first integral(4.18),we obtainan expression of the form(VI.8.11). Here,the elementary differentials correspond to the system $y = v$ , $\dot { v } = f ( y )$ ( $v$ has tobe identified with $z$ ).TheoremVI.8.8combinedwith Theorem4.11provesthat the underlying one-step method is conjugate to a symplectic integrator.

# XV.5Long-TermStability

Theresults of Sects.XV.4.3 and XV.4.4 imply the nearconservation of the total energy and oftheangular momentum in $N$ -bodyproblems for numerical solutions oftheunderlying one-step method of multistep methods.This,however,isof no valueas longas theparasitic solutions of themultistep method are not under control. Thepresent section is devoted to the study of the stability of numerical solutions overlong time intervals.

# XV.5.1 RoleofGrowth Parameters

Theanalysis of this section isbased on the representation

$$
y _ { n } = y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h )
$$

of the numerical solution of a multistep method (cf.formula (3.16)).

LinearMultistepMethodsforFirstOrderEquations.By Theorem3.5 theparasitic components $z _ { \ell }$ (for $2 \leq \ell \leq k$ ）arethe solution ofadifferential equation which,by(3.22),isof theform

$$
\dot { z } _ { \ell } = \mu _ { \ell } f ^ { \prime } ( y ) z _ { \ell } + \ldots .
$$

This is just the variational equation of $\dot { y } = f ( y )$ scaled by

$$
\mu _ { \ell } = \frac { \sigma ( \zeta _ { \ell } ) } { \zeta _ { \ell } \rho ^ { \prime } ( \zeta _ { \ell } ) } ,
$$

whichis the so-called growth parameter as introduced by Dahlquist (1959)and motivated there bya linear stability analysis (see Exercise5).

Weshallillustrate at the examples of Sect.XV.3.2 that the study of the truncated equation(5.2)gives alreadyalot of insight into the long-time behaviour ofmultistep methods.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/3d393701d05b794dbbbcd0cfd81767020909e9b9dd7ba66813e6ebecf1f8d239.jpg)  
Fig.5.1.First component of the solution of the pendulum equation(grey） together with the Euclidean norm of the solution $v ( t )$ of the scaled variational equation (5.4)

Example 5.1.For the pendulum equation,the truncated equation (5.2) is

$$
\left( { \begin{array} { c } { { \dot { y } } _ { 1 } } \\ { { \dot { y } } _ { 2 } } \end{array} } \right) = \left( { \begin{array} { c } { { y _ { 2 } } } \\ { { - \sin y _ { 1 } } } \end{array} } \right) , \qquad \left( { \begin{array} { c } { { \dot { v } } _ { 1 } } \\ { { \dot { v } } _ { 2 } } \end{array} } \right) = \mu \left( { \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - \cos y _ { 1 } } } & { { 0 } } \end{array} } \right) \left( { \begin{array} { c } { { v _ { 1 } } } \\ { { v _ { 2 } } } \end{array} } \right) .
$$

Wefix initial valuesas $y ( 0 ) = ( 1 . 9 , 0 . 4 ) ^ { T }$ and $v ( 0 ) = ( 0 . 1 , 0 . 1 ) ^ { I } .$ Figure5.1 shows the solution component $y _ { 1 } ( t )$ in grey,and the Euclidean norm of $v ( t )$ as solidblack line,once for $\mu = - 1$ and once for $\mu = 0 . 5$ Wenotice that the function $v ( t )$ remains small and bounded for $\mu = - 0 . 5$ ,andthat it increases linearly for $\mu = - 1$

Thisagreesperfectlywith the observations ofFigs.3.1 and 3.2,because the method (3.13) has growth parameter $\mu _ { \ell } = - 0 . 5$ for the roots $\zeta _ { \ell } = \pm i$ ,whereas the explicit midpoint rule(3.14）has $\mu _ { \ell } = - 1$ for $\zeta _ { \ell } = - 1$

Thesame analysis for partitioned multistep methods allows one to better understand thebehaviourof thedifferentmethodsinFig.1.3.The leadingtermof the parasitic modified equations depends on whether $\boldsymbol { \mathscr { Q } }$ isaroot of bothpolynomials $\rho _ { A } ( \zeta )$ and $\rho _ { B } ( \zeta )$ ,oronly ofone of them.Thisisvery similar to the situation encountered with multistepmethods for second orderdifferential equations which we treat next.

LinearMultistep Methods for Second Order Equations.Theorem 3.6 tellsus that the modified equation for the parasitic components $\boldsymbol { \mathcal { Z } } \boldsymbol { \ell }$ depends on the multiplicity of the root $\zeta _ { \ell }$ Considera stable,symmetric method(1.8)for $\ddot { y } = f ( y ) .$ If $\zeta _ { \ell }$ isa double rootof $\rho ( \zeta )$ ,formula(3.29)yields

$$
\ddot { z } _ { \ell } = \mu _ { \ell } f ^ { \prime } ( y ) \dot { z } _ { \ell } + . . . . , \mu _ { \ell } = \frac { 2 \sigma ( \zeta _ { \ell } ) } { \zeta _ { \ell } ^ { 2 } \rho ^ { \prime \prime } ( \zeta _ { \ell } ) } ,
$$

where we have not written terms containingat least two factors $z _ { j } .$ If $\zeta _ { \ell }$ isasingle root of $\rho ( \zeta )$ ,weget from(3.30） that

$$
\dot { z } _ { \ell } = h \mu _ { \ell } f ^ { \prime } ( y ) z _ { \ell } + \ldots , \qquad \mu _ { \ell } = \frac { \sigma ( \zeta _ { \ell } ) } { \zeta _ { \ell } \rho ^ { \prime } ( \zeta _ { \ell } ) } .
$$

Thereisan enormous difference between the parasitic modified equations corresponding todouble or single rootsof $\rho ( \zeta ) .$ Equation (5.5) is the complete analogue of(5.2)and,as before,the long-time behaviouris hardlypredictableand strongly depends on the growth parameter.For single roots,however,we are concernedwith afirstorder differential equation(5.6) havinganadditional factor $\hbar$ asbonus.For theanalysis of Sects.XV.5.2 and XV.5.3itis important to have only singleroots.

Definition 5.2.A symmetric multistep method (1.8） for second order differential equationsiscalleds-stableif,apart fromthedoublerootat $1$ ,all zeros of $\rho ( \zeta )$ are simple and ofmodulus one.

The linearized parasitic modified equations give much insight into the long-time behaviour of multistep methods.To get rigorous estimes over long times,however, furtherconsiderationsare necessary.A partial result is given byCano&Sanz-Serna （1998)for multistep methods(1.8）applied to equations $\ddot { y } = f ( y )$ with periodic exact solution.There,the first terms of the asymptotic error expansion for the global errorarecomputed,and their growthasa function of time is studied.We shall follow theapproachof Hairer&Lubich（2Oo4）who exploit theHamiltonian structureof second order differential equations.

# XV.5.2Hamiltonian of theFullModified System

Intheremainder of this section we restrict our consideration to s-stable,irreducible linearmultistepmethods

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } q _ { n + j } = - h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } \nabla U ( q _ { n + j } ) ,
$$

applied to Hamiltonian systemswritten as

$$
\ddot { q } = - \nabla U ( q ) ,
$$

where $U ( q )$ is assumed to be real-analytic in the considered region.

Thekey toprovinglong-time error estimates is the observation that much of the Hamiltonian structureis conserved in themodified equations(3.25).Theresults and techniques of this subsectionare closely related to those of Sect.XIII.6.3developed fornumerical methods for oscillatory differential equations.

We let ${ \bf z } = ( z _ { \ell } ) _ { \ell \in \mathcal { T } _ { N } }$ and define $\mathcal { U } ( \mathbf { z } )$ as

$$
\mathcal { U } ( \mathbf { z } ) = U ( z _ { 0 } ) + \sum _ { m \geq 1 } \frac { 1 } { m ! } \sum _ { \zeta _ { \boldsymbol { \kappa } _ { 1 } } , \ldots , \zeta _ { \boldsymbol { \epsilon } _ { m } } = 1 } U ^ { ( m ) } ( z _ { 0 } ) ( z _ { \boldsymbol { \ell } _ { 1 } } , \ldots , z _ { \boldsymbol { \ell } _ { m } } ) ,
$$

where the secondsumisoverallindices $\ell _ { 1 } \in \mathcal { L } _ { N } ^ { * } , \ldots , \ell _ { m } \in \mathcal { L } _ { N } ^ { * }$ with $\zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = 1$ (using the notation of Sect.XV.3.2).Since theroots of $\rho ( \zeta )$ ,differentfrom $\zeta _ { 1 } = 1$ arecomplex and appear in pairs(Exercise 3),also the functions $z _ { \ell }$ appearinpairs. It is convenient touse the notation $z _ { - \ell } = z _ { j }$ if $\zeta _ { \ell } = \zeta _ { j }$ .

It follows from (3.28)with $f ( q ) = - \nabla U ( q )$ that every solution of the truncated modified equation(3.25) satisfies

$$
\rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = - h ^ { 2 } \sigma ( \zeta _ { \ell } e ^ { h D } ) \nabla _ { z _ { - \ell } } \mathcal { U } ( \mathbf { z } ) + \mathcal { O } ( h ^ { N + 2 } )
$$

(for all $\ell \in \mathcal { L }$ aslongas

$$
y \in K , \quad \| { \dot { y } } \| \leq M , \quad \| z _ { \ell } \| \leq \delta { \mathrm { ~ f o r ~ } } 1 < \ell < k ,
$$

where $K$ isacompact subset of the domain of analyticity of $U ( q )$ ， $M > 0$ some bound on the derivative,and $0 < \delta = { \mathcal { O } } ( h )$ isasufficiently small constant (note that this implies $\| z _ { \ell } \| \le \delta$ forall $\ell \in \mathcal { T } ^ { * }$ if $h$ issufficiently small, cf.thealgebraic relations of (3.25)).

Forease of presentation,we assume for the moment that $\sigma ( \zeta _ { \ell } ) \neq 0$ forall $\ell \in \mathcal { I } _ { N }$ (we know that this holds for $1 \le \ell < k$ ,because the method is irreducible). Weapply the operator $\sigma ^ { - 1 } ( \zeta _ { \ell } e ^ { h D } )$ to both sides of(5.10)and divide by $h ^ { 2 }$

$$
h ^ { - 2 } \Big ( { \frac { \rho } { \sigma } } \Big ) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = - \nabla _ { z \_ \ell } \mathcal { U } ( \mathbf { z } ) + \mathcal { O } ( h ^ { N } ) .
$$

We then multiply with $\dot { z } _ { - \ell } ^ { T }$ , sum over all $ { \ell } \in  { \mathcal { L } } _ { N }$ ,and thus obtain

$$
h ^ { - 2 } \sum _ { \ell \in \mathcal { T } _ { N } } \dot { z } _ { - \ell } ^ { T } \Big ( \frac { \rho } { \sigma } \Big ) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } + \frac { d } { d t } \mathcal { U } ( \mathbf { z } ) = \mathcal { O } ( h ^ { N } ) .
$$

Wenow show that also the first expression on the left-hand side isa total derivative ofa function depending on $\mathbf { z }$ and its time derivatives.Forthiswe note that

$$
\left( { \frac { \rho } { \sigma } } \right) ( \zeta \ell e ^ { i x } ) = \sum _ { j \geq 0 } c _ { \ell , j } x ^ { j } \qquad { \mathrm { w i t h ~ } } r e a l { \mathrm { ~ c o e f f i c i e n t s } } \quad c _ { \ell , j } = ( - 1 ) ^ { j } c _ { - \ell , j } .
$$

This holds because the symmetry of the multistep method yields $( \rho / \sigma ) ( 1 / \zeta ) =$ $( \rho / \sigma ) ( \zeta )$ and hence,for real $x$ ， $( \rho / \sigma ) ( \zeta _ { \ell } e ^ { i x } ) = ( \rho / \sigma ) ( \zeta _ { \ell } e ^ { i x } ) = { \overline { { ( \rho / \sigma ) ( \zeta _ { \ell } e ^ { i x } ) } } }$ . Withtheexpansion（5.14）we obtain

$$
\left( \frac { \rho } { \sigma } \right) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = \sum _ { j = 0 } ^ { N + 1 } c _ { \ell , j } ( - i h ) ^ { j } z _ { \ell } ^ { ( j ) } + \mathcal { O } ( h ^ { N + 2 } ) .
$$

Tostudy(5.13）weapplytherelation (4.12) for thereal function $y = z _ { 1 }$ and for $z _ { \ell }$ corresponding to $\zeta _ { \ell } = - 1$ ,while for thecomplex-valued functions $z = z _ { \ell }$ ,with complex conjugate $z = z _ { - \ell }$ ,weuse

$$
\begin{array} { l } { { \displaystyle \mathrm { R e } ^ { \frac { \cdot } { z } T } z ^ { ( 2 m ) } = \mathrm { R e } \frac { d } { d t } \Big ( \dot { \bar { z } } ^ { T } z ^ { ( 2 m - 1 ) } - \ddot { \bar { z } } ^ { T } z ^ { ( 2 m - 2 ) } + . . . \pm \frac { 1 } { 2 } ( \bar { z } ^ { ( m ) } ) ^ { T } z ^ { ( m ) } \Big ) } \ ~ } \\ { { \displaystyle \mathrm { I m } \ddot { \bar { z } } ^ { T } z ^ { ( 2 m + 1 ) } = \mathrm { I m } \frac { d } { d t } \Big ( \dot { \bar { z } } ^ { T } z ^ { ( 2 m ) } = \ddot { \bar { z } } ^ { T } z ^ { ( 2 m - 1 ) } + . . . \mp ( \bar { z } ^ { ( m ) } ) ^ { T } z ^ { ( m + 1 ) } \Big ) } . } \end{array}
$$

Together with(5.15) theserelations show that the terms

$$
{ \dot { z } } _ { - \ell } ^ { T } \Bigl ( { \frac { \rho } { \sigma } } \Bigr ) ( { \zeta } _ { \ell } e ^ { h D } ) z _ { \ell } + { \dot { z } } _ { \ell } ^ { T } \Bigl ( { \frac { \rho } { \sigma } } \Bigr ) ( { \zeta } _ { - \ell } e ^ { h D } ) z _ { - \ell }
$$

$$
= \sum _ { j = 0 } ^ { N + 1 } c _ { \ell , j } 2 \operatorname { R e } \left( ( - i h ) ^ { j } \vec { z } _ { \ell } ^ { \ : T } z _ { \ell } ^ { ( j ) } \right) + \mathcal { O } ( h ^ { N + 2 } )
$$

giveatotal derivative(upto theremainder term).Hence the left-hand sideof(5.13) can be written asthe time derivative ofa function whichdepends on $z _ { \ell }$ , $\ell \in \mathcal { L } _ { N }$ ,and ontheir derivatives.Usingthe modified equation(3.25）we eliminate all $z _ { \ell }$ correspondingto $\zeta _ { \ell }$ with $\rho ( \zeta _ { \ell } ) \neq 0$ andtheirderivatives,the firstand higherderivatives of $z _ { \ell }$ (for $1 < \ell < k$ ),and the second and higher derivatives of $y = z _ { 1 }$ Wethus get afunction

$$
\mathcal { H } ( y , \dot { y } , \mathbf { z ^ { * } } ) = H _ { 0 } ( y , \dot { y } , \mathbf { z ^ { * } } ) + . . . . + h ^ { N - 1 } H _ { N - 1 } ( y , \dot { y } , \mathbf { z ^ { * } } )
$$

$\mathbf { z } ^ { * } = ( z _ { \ell } ) _ { \ell = 2 } ^ { k - 1 }$ ,such that

$$
\frac { d } { d t } \mathcal { H } \big ( y ( t ) , \dot { y } ( t ) , { \mathbf z } ^ { * } ( t ) \big ) = \mathcal { O } ( h ^ { N } ) ,
$$

alongsolutions of.(3.25） that stayina set defined by(5.11).The function $\mathcal { H }$ is therefore an almost-invariant of the system (3.25).

If,however, $\sigma ( \zeta )$ does havea zero $\zeta _ { \ell }$ ,then we omit the corresponding term from the sum in (5.13).Hence the term $\dot { z } _ { - \ell } ^ { \varDelta } \nabla _ { z _ { - \ell } } \mathcal { U } ( \mathbf { z } )$ ismissing from $( d / d t ) \mathcal { U } ( \mathbf { z } )$ and musttherefore be compensated in theremainder term.Since $\zeta _ { \ell }$ isa product of no fewer than two zeros of $\rho ( \zeta )$ ,it follows from(3.31）and from $\mu _ { \ell , 0 } = 0$ that $z _ { \ell } =$ $\mathcal { O } ( h ^ { 3 } \delta ^ { 2 } )$ ,aslong as $\| z _ { j } \| \leq \delta$ for $1 < j < k$ Wefurtherhave $\nabla _ { z _ { - } } \mathcal { U } ( \mathbf { z } ) = \mathcal { O } ( \delta ^ { 2 } )$ ， so that theremainder termin（5.17）isaugmented by $\mathcal { O } ( h ^ { 3 } \delta ^ { 4 } )$ .

Wesummarize theabove considerations(Hairer&Lubich 2oo4)as follows.

Theorem5.3.Every solution of the truncatedmodifiedequation(3.25) satisfies, withH from(5.16),

$$
\begin{array} { r } { \mathcal { H } \big ( y ( t ) , \dot { y } ( t ) , { \mathbf z } ^ { * } ( t ) \big ) = \mathcal { H } \big ( y ( 0 ) , \dot { y } ( 0 ) , { \mathbf z } ^ { * } ( 0 ) \big ) + \mathcal { O } ( t h ^ { N } ) + \mathcal { O } ( t h ^ { 3 } \delta ^ { 4 } ) } \end{array}
$$

aslongas the solution stays in the set definedby(5.11).Moreover,

$$
\begin{array} { r } { \mathcal { H } \big ( y , \dot { y } , \mathbf { z } ^ { * } \big ) = H ( y , \dot { y } ) + \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( h \delta ^ { 2 } ) . } \end{array}
$$

The closeness to the Hamiltonian $H ( y , \dot { y } ) = \textstyle { \frac { 1 } { 2 } } \| \dot { y } \| ^ { 2 } + U ( y )$ follows also directly from the above construction.For $\mathbf { z } ^ { \ast } = \mathbf { 0 }$ wehave $\mathcal { H } ( y , \dot { y } , 0 ) = \bar { H } ( y , \dot { y } )$ , where $\bar { H }$ is themodified energy from Theorem 4.9.

We willuse Theorem5.3in SectionXV.6.1to infer the long-timenear-conservation of the Hamiltonian along numerical solutions.Before that we need to bound the parasitic components.

# XV.5.3Long-Time Bounds for Parasitic Solution Components

Themodified equations have further almost-invariantswhich are close to the squares ofthe norms of the parasitic components that correspond to the roots of $\rho ( \zeta )$ We derive them here and use them to show that allparasitic solution components remain small oververy long times.The techniquesused in this subsectionare similar to thosein Sects.XIII.6 and XIII.7.

We consider $\ell$ with $1 < \ell < k$ forwhich $\zeta _ { \ell }$ is a simple root of $\rho ( \zeta )$ and $\sigma ( \zeta _ { \ell } ) \neq$ O.The dominant term on the left-hand side of(5.12)is $- c _ { \ell , 1 } i h ^ { - 1 } \dot { z } _ { \ell } .$ Since

$$
\frac { d } { d t } \| \boldsymbol { z } _ { \ell } \| ^ { 2 } = \boldsymbol { z } _ { - \ell } ^ { T } \dot { \boldsymbol { z } } _ { \ell } + \boldsymbol { z } _ { \ell } ^ { T } \dot { \boldsymbol { z } } _ { - \ell } ,
$$

we multiply (5.12) with $z _ { - \ell } ^ { T }$ and the corresponding equation for $\zeta _ { - \ell }$ with $z _ { \ell } ^ { T }$ ,and weform the difference,so that the dominant term on the left-hand side becomes $\begin{array} { r } { - c _ { \ell , 1 } i h ^ { - 1 } \frac { d } { d t } \| z _ { \ell } \| ^ { 2 } } \end{array}$ (note $c _ { - \ell , 1 } = - c _ { \ell , 1 } ,$ .Dividing by $- c _ { \ell , 1 } i h ^ { - 1 }$ gives

$$
\begin{array} { r l } & { \frac { i } { c _ { \ell , 1 } h } \Big ( z _ { - \ell } ^ { T } \frac { \rho } { \sigma } ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } - z _ { \ell } ^ { T } \frac { \rho } { \sigma } ( \zeta _ { - \ell } e ^ { h D } ) z _ { - \ell } \Big ) } \\ & { \qquad = \frac { i h } { c _ { \ell , 1 } } \Big ( - z _ { - \ell } ^ { T } \nabla _ { z _ { - \ell } } \mathcal { U } ( { \bf z } ) + z _ { \ell } ^ { T } \nabla _ { z _ { \ell } } \mathcal { U } ( { \bf z } ) \Big ) . } \end{array}
$$

Wefirst estimate theright-hand expression.Since

$$
\nabla _ { z _ { - \ell } } \mathcal { U } ( \mathbf { z } ) = \nabla ^ { 2 } U ( z _ { 0 } ) z _ { \ell } + \mathcal { O } ( \delta ^ { 2 } ) ,
$$

aslong as (5.11）is satisfied,we obtain from the symmetry of the Hessian that the right-hand side of(5.21)isof size $\mathcal { O } ( h \delta ^ { 3 } )$ Thedominant $\mathcal { O } ( h \delta ^ { 3 } )$ termis present onlyif $\zeta _ { - \ell }$ can be written as the product of two roots of $\rho ( \zeta )$ other than 1.If this is not the case,the expression (5.21) is of size $\mathcal { O } ( h \delta ^ { 4 } )$

Usingthe expansion (5.15)on the left-hand side of(5.21)and therelations (for $z = z _ { \ell }$ ）

$$
\begin{array} { l } { { \mathrm { R e } \overline { { { z } } } ^ { T } z ^ { ( 2 m + 1 ) } = \mathrm { R e } \displaystyle \frac { d } { d t } \Big ( \overline { { { z } } } ^ { T } z ^ { ( 2 m ) } - \frac { \div ^ { T } } { \overline { { { z } } } } z ^ { ( 2 m - 1 ) } \cdots \mp \frac { 1 } { 2 } ( \overline { { { z } } } ^ { ( m ) } ) ^ { T } z ^ { ( m ) } \Big ) } } \\ { { \mathrm { I m } \overline { { { z } } } ^ { T } z ^ { ( 2 m + 2 ) } = \mathrm { I m } \displaystyle \frac { d } { d t } \Big ( \overline { { { z } } } ^ { T } z ^ { ( 2 m + 1 ) } - \overline { { { z } } } ^ { T } z ^ { ( 2 m ) } + \ldots \pm ( \overline { { { z } } } ^ { ( m ) } ) ^ { T } z ^ { ( m + 1 ) } \Big ) } } \end{array}
$$

weobtain that(5.21) is,up to $\mathcal { O } ( h ^ { N } )$ ,thetotalderivativeofafunctiondepending on $\mathbf { z }$ and itsderivatives.

By construction the dominant termis $\frac { d } { d t } \left| \right| z _ { \ell } \left| \right| ^ { 2 } ,$ The following terms have at least one more power of $h$ andat least one derivativewhich by(3.25）gives rise to an additional factor $h$ .Eliminating higher derivativeswith the help of(3.25),we arrive ata function of the form

$$
\displaystyle { \mathcal { K } _ { \ell } ( y , \dot { y } , \mathbf { z } ^ { * } ) = \| z _ { \ell } \| ^ { 2 } + h ^ { 2 } K _ { \ell , 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + . . . + h ^ { N - 1 } K _ { \ell , N - 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) } .
$$

Aswe haveseen,its total derivativeis of size $\mathcal { O } ( h \delta ^ { 3 } )$ orsmaller.We summarize these considerations in the following theorem.

Theorem5.4.Alongevery solution of thetruncated modifedequation(3.25) the function $\boldsymbol { \mathcal { K } } _ { \ell } ( y , \dot { y } , \mathbf { z } ^ { * } )$ satisfiesfor $1 < \ell < k$

$$
\begin{array} { r } { K _ { \ell } \big ( y ( t ) , \dot { y } ( t ) , \mathbf { z } ^ { * } ( t ) \big ) = K _ { \ell } \big ( y ( 0 ) , \dot { y } ( 0 ) , \mathbf { z } ^ { * } ( 0 ) \big ) + \mathcal { O } ( t h ^ { N } ) + \mathcal { O } ( t h \delta ^ { 3 } ) } \end{array}
$$

aslongasthe solutionstaysinthe set defined by(5.11).Theseconderror termis replacedby $\mathcal { O } ( t h \delta ^ { 4 } )$ ifno rootof $\rho ( \zeta )$ otherthan $^ { 1 }$ is theproduct oftwo other roots. Moreover,

$$
\begin{array} { r } { \mathcal { K } _ { \ell } \big ( y , \dot { y } , \mathbf { z } ^ { * } \big ) = \| z _ { \ell } \| ^ { 2 } + \mathcal { O } ( h ^ { 2 } \delta ^ { 2 } ) . } \end{array}
$$

Thisresult allows us to write the numerical solution ina form that is suitable for deriving long-time error estimates.Let us first collect the necessary assumptions:

（A1）the multistep method(5.7) is symmetric, $s$ -stable,andof order $T$ ;   
（A2）the potential function $U ( q )$ of(5.8)is defined and analytic in an open neighbourhood of acompact set $K$ ;   
（A3）the starting approximations $q _ { 0 } , \ldots , q _ { k - 1 }$ are such that the initial values for (3.25）obtained from Lemma 3.7 satisfy $y ( 0 ) \in K$ , $\| \dot { \boldsymbol { y } } ( 0 ) \| ~ \le ~ M$ ,and $\| z _ { \ell } ( 0 ) \| \le \delta / 2$ for $1 < \ell < k$ ;   
（A4）the numerical solution $\left\{ q _ { n } \right\}$ stays for $0 \leq n h \leq T$ in a compact set $K _ { 0 }$ which hasapositive distance to the boundary of $K$

Theorem5.5 (Hairer&Lubich2004).Assume(A1)-(A4).Forsufficiently small $h$ and $\delta$ and forafixedtruncation index $N$ (large enough such that $h ^ { N } = { \mathcal O } ( \delta ^ { 4 } ) ,$ , thereexist functions $y ( t )$ and $z _ { \ell } ( t )$ onan intervaloflength

$$
T = { \cal O } ( ( h \delta ) ^ { - 1 } )
$$

such that

· $q _ { n } = y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h )$ for0≤nh≤T;   
·onevery subinterval $| j h , ( j + 1 ) h )$ thefunctions $y ( t ) , z _ { \ell } ( t )$ area solution of the system（3.25）；   
the functions $y ( t ) , z _ { \ell } ( t )$ have jump discontinuities of size $\mathcal { O } ( h ^ { N + 2 } )$ at thegrid points $j h$   
$\| z _ { \ell } ( t ) \| \leq \delta$ for $0 \leq t \leq T .$

Ifno root of $\rho ( \zeta )$ other than $^ { 1 }$ isthe product of two other roots,all theseestimates arevalidonanintervalof length $T = { \cal O } ( ( h \delta ^ { 2 } ) ^ { - 1 } )$

Proof. To define the functions $y ( t )$ , $z _ { \ell } ( t )$ on the interval $[ j h , ( j + 1 ) h )$ we consider the $k$ consecutive numerical solution values $q _ { \lambda } , q _ { \lambda + 1 } , . . . , q _ { \lambda + k - 1 } .$ Wecompute initialvalues for(3.25)accordingtoLemma3.7,andwe let $y ( t ) , z _ { \ell } ( t )$ be a solution of (3.25)on $[ j h , ( j + 1 ) h ) .$ Because their defect is $\mathcal { O } ( h ^ { N } )$ and $\mathcal { O } ( h ^ { N + 1 } )$ ,respectively, such a construction yields jump discontinuities of size $\mathcal { O } ( h ^ { N + 2 } )$ at the grid points.

Itfollows from Theorem5.4 that $\mathcal { K } _ { \ell } ( y ( t ) , \dot { y } ( t ) , \mathbf { z } ^ { * } ( t ) )$ remains constant up to an error of size $\mathcal { O } ( h ^ { 2 } \delta ^ { 3 } )$ on the interval $\left| j h , ( j + 1 ) h \right.$ Taking into account the jump discontinuities,we find that

$$
\begin{array} { r } { K _ { \ell } ( y ( t ) , \dot { y } ( t ) , { \mathbf z } ^ { * } ( t ) ) \le K _ { \ell } ( y ( 0 ) , \dot { y } ( 0 ) , { \mathbf z } ^ { * } ( 0 ) ) + C _ { 1 } t h \delta ^ { 3 } + C _ { 2 } t h ^ { N + 1 } } \end{array}
$$

as longas $\| z _ { \ell } ( t ) \| \leq \delta .$ By（5.24）this then implies

$$
\| z _ { \ell } ( t ) \| ^ { 2 } \leq \| z _ { \ell } ( 0 ) \| ^ { 2 } + C _ { 1 } t h \delta ^ { 3 } + C _ { 2 } t h ^ { N + 1 } + C _ { 3 } h ^ { 2 } \delta ^ { 2 } .
$$

The assumption $\| z _ { \ell } ( t ) \| ~ \le ~ \delta$ iscertainly satisfied as long as $C _ { 1 } t h \delta \ \leq \ 1 / 4$ , $C _ { 2 } t h ^ { N + 1 } \leq \delta ^ { 2 } / 4$ ,and $C _ { 3 } h ^ { 2 } \leq 1 / 4$ sothat theright-hand sideof（5.26)is bounded by $\delta ^ { 2 }$ This proves not only the estimate for $| | z _ { \ell } ( t ) | |$ ,but at the same time it guaranteesrecursively that the above construction of the functions $y ( t ) , z _ { \ell } ( t )$ is feasible. $\boxed { \begin{array} { r l } \end{array} }$

Notice that forinitial values computed bya sufficiently accurate one-step method the constant $\delta$ can be chosen as small as $\mathcal { O } ( h ^ { r + 2 } )$ where $r$ is the order ofthemultistepmethod (cf.Lemma 3.7).The above estimatesare thereforevalid onvery long time intervals.

Example5.6.To illustrate the long-time behaviour of the parasitic terms $z _ { \ell }$ we consider the pendulum equation $q = - \sin q$ ,andwe apply the symmetricmultistep methods(B)and(C) of Example1.2.For method (C),the starting values are chosen farfrom a smooth solution,so that the propagation of the parasitic termsin the numerical solution can be better observed.We compute the velocity approximation by

$$
v _ { n } = { \frac { h } { 1 2 } } \Big ( 8 ( q _ { n + 1 } - q _ { n - 1 } ) - ( q _ { n + 2 } - q _ { n - 2 } ) \Big ) .
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/eacb69580dbd7f43a8ba97d06ad7261ca22218e30b6a03238035d2ca9c57662e.jpg)  
Fig.5.2.Stable propagation of perturbations in the starting values for method(C)of Example 1.2;initial values are $q _ { 0 } = 1 . 1 4 1$ $q _ { 1 } = 1 . 1 5 8$ , $q _ { 2 } = 1 . 1 7 8$ and $q _ { 3 } = 1 . 2 0 6$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/59ad34f059343e1d5853b59b4b92c65fdcc5a13205a1afa2a328a36120342f22.jpg)  
Fig.5.3.Unstable propagation of perturbations in thestartingvalues,for method(B)of Example1.2;initial valuesare $q _ { 0 } = 1 . 1 4 7$ $q _ { 1 } = 1 . 1 8 3$ , $q _ { 2 } = 1 . 2 5 5$ ,and $q _ { 3 } = 1 . 2 8 6$

Figure 5.2 shows the numerical solution $( q _ { n } , v _ { n } )$ for $n \geq 2$ Thevalues for $n =$ $2 , 3 , 4 , 5$ areindicated by larger black bullets.The parasitic roots of method (C)are $\pm i$ andboth are simple.The numerical solution is therefore of the form

$$
q _ { n } = y ( n h ) + i ^ { n } z _ { 1 } ( n h ) + ( - i ) ^ { n } { \overline { { z _ { 1 } ( n h ) } } } + ( - 1 ) ^ { n } z _ { 2 } ( n h ) .
$$

One observesin Fig.5.2 that the functions $z _ { j } ( t )$ not only remain boundedand small, butthey stay essentiallyconstant over theconsidered interval.This shouldbecompared to Fig.3.1,where the parasitic functions $z _ { j } ( t )$ are bounded,but not constant.

Method(B) hasa double parasitic root at $^ { - 1 }$ and,therefore,is not $s$ -stable. Its numerical solution behaves like $q _ { n } = y ( n h ) + ( - 1 ) ^ { n } z ( n h )$ InFig.5.3every second approximation is drawnin grey.One sees that the numerical solution stays on two smooth curves $y ( t ) + z ( t )$ and $y ( t ) - z ( t )$ which,however,do not remain close to each other.

# XV.6 Explanation of the Long-Time Behaviour

The bounds on the parasitic solution components of Sect.XV.5.3 allow us to get rigorousstatements on the long-time behaviour of multistep methods(5.7)for second orderdifferential equations.Thefollowingresultsaretaken fromHairer&Lubich (2004).We do not know of similar results for multistep methods (1.1).

# XV.6.1 Conservation of Energy and Angular Momentum

Theenergyconservationis now a directconsequence ofTheorems 5.3and 5.5.We shall use the representation of $q _ { n }$ in terms of functions $y ( t ) , z _ { \ell } ( t )$ as in Theorem 5.5. Taking intoaccount the jumpdiscontinuities of these functions,Theorem5.3 yields

$$
\begin{array} { r } { \mathcal { H } ( y ( t ) , \dot { y } ( t ) , \mathbf { z } ^ { * } ( t ) ) = \mathcal { H } ( y ( 0 ) , \dot { y } ( 0 ) , \mathbf { z } ^ { * } ( 0 ) ) + \mathcal { O } ( t h ^ { 3 } \delta ^ { 4 } ) + \mathcal { O } ( t h ^ { N + 1 } ) . } \end{array}
$$

Wehave $\delta = \mathcal { O } ( h ^ { r + 1 } )$ if the starting approximations are computed by a $r$ th.order one-step method.If $N$ ischosen sufficiently large,this together with(5.19) implies

$$
\begin{array} { r } { H ( y ( t ) , \dot { y } ( t ) ) = H ( y ( 0 ) , \dot { y } ( 0 ) ) + { \mathcal O } ( h ^ { p } ) \qquad \mathrm { f o r } \quad 0 \le t \le T = { \mathcal O } ( h ^ { - p - 2 } ) . } \end{array}
$$

If the velocity approximation $\begin{array} { r } { p _ { n } \ = \ v _ { n } } \end{array}$ is given bya $r$ thorderfinitedifference formula(3.11),it follows from Theorem5.5 that $p _ { n } = { \dot { y } } ( n h ) + { \mathcal { O } } ( h ^ { r } )$ provided the truncation index $N$ issufficiently large.Thisproves the following result,and explains the excellent long-time behaviour of method(C)in Fig.1.2.

Theorem6.1(Total Energy).Foraproblem $\ddot { q } ~ = ~ - \nabla U ( q )$ with total energy $H ( p , q ) = { \textstyle \frac { 1 } { 2 } } p ^ { 1 } p + U ( q )$ ,thenumerical solutionofan s-stable symmetric multistepmethod(5.7)oforder $r$ satisfies

$$
H ( q _ { n } , p _ { n } ) = H ( q _ { 0 } , p _ { 0 } ) + { \mathcal O } ( h ^ { r } ) \qquad f o r \quad n h \leq h ^ { - r - 2 } .
$$

Ifnorootof $\rho ( \zeta )$ other than $1$ isaproduct of two other roots,the statement holds onintervalsoflength $O ( h ^ { - 2 r - 3 } )$ □

Weassume next that thedifferential equation $\ddot { q } = - \nabla U ( q )$ hasa quadratic first integral of the form $L ( q , \dot { q } ) = \dot { q } ^ { T } A q$ (e.g.,the angular momentumin $N$ -body problems).Thismeans that $A$ is skew-symmetric and $\nabla U ( q ) ^ { T } A q = 0$ Thelast equation can also be interpreted as the invariance relation $U ( e ^ { \tau A } q ) = U ( q ) .$ This property implies for $\mathcal { U } ( \mathbf { z } )$ givenby（5.9），that $\mathcal { U } ( e ^ { \tau A } \mathbf { z } ) = \mathcal { U } ( \mathbf { z } )$ (here $e ^ { \tau { \cal A } } \mathbf { z } =$ $( e ^ { \tau A } z _ { \ell } ) _ { \ell \in \mathcal { T } } )$ Along solutions ${ \bf z } ( t )$ of themodified equations (5.10)we therefore haveup to terms of size $\mathcal { O } ( h ^ { N } )$

$$
= \frac { d } { d \tau } \Big | _ { \tau = 0 } \mathcal { U } ( e ^ { \tau A } \mathbf { z } ) = \sum _ { \ell \in \cal Z } z _ { - \ell } ^ { T } A \nabla _ { z = \ell } \mathcal { U } ( \mathbf { z } ) = \sum _ { \ell \in \cal Z } h ^ { - 2 } z _ { - \ell } ^ { T } A \left( \frac { \rho } { \sigma } \right) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } ( \mathbf { z } ) .
$$

If $\sigma ( \zeta )$ hasaroot $\zeta _ { \ell }$ ,then the correspondingtermis omitted from the last sum,leadingtoa remainder term which in the worst case is $\mathcal { O } ( h ^ { 3 } \delta ^ { 4 } )$ ,asinTheorem5.3.Like intheprevious proofs,the last sumis,for skew-symmetric $A$ ,the total derivative of afunction

$$
\mathcal { L } ( y , \dot { y } , \mathbf { z } ^ { * } ) = L _ { 0 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + . . . + h ^ { N - 1 } L _ { N - 1 } ( y , \ddot { y } , \mathbf { z } ^ { * } )
$$

which satisfies(under the same assumptions as in Theorem5.3)

$$
\begin{array} { r } { \mathcal { L } \big ( y ( t ) , \dot { y } ( t ) , { \mathbf { z } ^ { * } ( t ) } \big ) = \mathcal { L } \big ( y ( 0 ) , \dot { y } ( 0 ) , { \mathbf { z } ^ { * } ( 0 ) } \big ) + \mathcal { O } ( t h ^ { 3 } \delta ^ { 4 } ) + \mathcal { O } ( t h ^ { N + 1 } ) } \end{array}
$$

and

$$
\begin{array} { r } { \mathcal { L } \big ( y , \dot { y } , \mathbf { z } ^ { * } \big ) = L ( y , \dot { y } ) + \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \delta ^ { 2 } / h ) . } \end{array}
$$

Wetherefore obtain the following result.

Theorem 6.2 (Angular Momentum). Let $L ( q , \dot { q } ) = \dot { q } ^ { T } A q$ beafirst integral of $\ddot { q } = - \nabla U ( q )$ Thenumerical solution ofan $s$ -stablesymmetricmultistepmethod (5.7)of order $\tau$ thensatisfies

$$
L ( q _ { n } , p _ { n } ) = L ( q _ { 0 } , p _ { 0 } ) + \mathcal { O } ( h ^ { r } ) \qquad f o r \quad n h \leq h ^ { - r - 2 } .
$$

Ifnoroot of $\rho ( \zeta )$ other than1is $^ a$ product oftwootherroots,the statement holds onintervalsoflength $O ( h ^ { - 2 r - 3 } )$ . □

# XV.6.2Linear ErrorGrowth for Integrable Systems

The differential equation $\ddot { q } = - \nabla U ( q )$ writtenas $\dot { q } \ = \ v$ , $\dot { \boldsymbol { v } } = - \nabla U ( \boldsymbol { q } ) .$ is reversible with respect to the involution $v \mapsto - v$ Assumethat itisalsoan integrable system in the sense of Definition XI.1.1,and denote by $a \ = \ I ( q , v )$ theaction variables,and by $\omega ( a )$ the frequences of the system.

By Theorem 5.5,the numerical solution can be written as $q _ { n } ~ = ~ y ( n h ) ~ +$ $\begin{array} { r } { \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h ) } \end{array}$ ,where (at least locally) $y ( t )$ is thesolutionofamodifeddifferential equation (first equation of (3.25))

$$
\ddot { y } = f _ { 0 , 0 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + h f _ { 0 , 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) \stackrel { } { + } \dots + h ^ { N - 1 } f _ { 0 , N - 1 } ( y , \dot { y } , \mathbf { z } ^ { * } )
$$

which,for $\mathbf { z } ^ { * } = 0$ becomes the reversible modified differential equation (3.9).Since $z _ { j } ( t ) = O ( \delta )$ (see Theorem5.5)and since $\mathbf { z } ^ { \ast }$ appears at least quadratically in(6.2), this equation isa $\mathcal { O } ( \delta ^ { 2 } )$ perturbation of (3.9).We are nowin the position toapply theresultsofLemma XI.2.1and Theorem XI.3.1.Theadditional (non-reversible) perturbation of size $\mathcal { O } ( \delta ^ { 2 } )$ in the differential equation (6.2) produces an error term of size $\mathcal { O } ( t \delta ^ { 2 } )$ in the action variables and of size $\mathcal { O } ( t ^ { 2 } \delta ^ { 2 } )$ in the angle variables.If $\delta = \mathcal { O } ( h ^ { r + 1 } )$ ,these terms are negligible with respect to those already appearingin Theorem XI.3.1.The errorsdue to the jumpdiscontinuities(Theorem 5.5） are also negligible.We have thus proved the following statement.

Theorem6.3.Consider applying the $s$ -stablesymmetricmultistepmethod(5.7)of order $r$ toan integrablereversible system $\ddot { q } = - \nabla U ( q )$ with real-analytic potential $U$ Supposethat $\omega ^ { \ast } \in \mathbb { R } ^ { d }$ satisfiesthediophantinecondition(X.2.4).Then, there exist positive constants $C , c$ and $h _ { 0 }$ such that the following holdsforall stepsizes $\textit { h } \leq \ h _ { 0 }$ :everynumerical solution $( q _ { n } , v _ { n } )$ startingwith frequencies $\omega _ { 0 } = \omega ( I ( q _ { 0 } , v _ { 0 } ) )$ suchthat $\lVert \omega _ { 0 } - \omega ^ { * } \rVert \leq c \lvert \log h \rvert ^ { - \nu - 1 }$ satisfies

$$
\begin{array} { r c l } { \| ( q _ { n } , v _ { n } ) - ( q ( t ) , v ( t ) ) \| } & { \leq } & { C t h ^ { r } } \\ { \| I ( q _ { n } , v _ { n } ) - I ( q _ { 0 } , v _ { 0 } ) \| } & { \leq } & { C h ^ { r } } \end{array} \qquad f o r \quad 0 \leq t = n h \leq h ^ { - r } .
$$

Theconstants $h _ { 0 } , c , C$ depend on $d , \gamma , \nu$ and on bounds ofthepotential.

# XV.7 Practical Considerations

In computationswith multistep methods one can observe resonance phenomena,if relatively large step sizesare used.Thisand theuse of variable step sizes are the subject of this section.

# XV.7.1 Numerical Instabilities and Resonances

Soon after Quinlan and Tremaine's methods were published,however, AlarToomre discovered a disturbing feature of the methods,...

(G.D.Quinlan 1999)

It isa simple task to derive multistep methods of high order.Consider,for example, methods of the form (1.8) for second order differential equations $\ddot { y } = f ( y )$ Their orderis determined by thecondition(1.9).Wechoose arbitrarily $\rho ( \zeta )$ such that $\zeta = 1$ isa double zero and the stability condition is satisfied.Condition (1.9)then gives

$$
\sigma ( \zeta ) = \rho ( \zeta ) / \log ^ { 2 } \zeta + \mathcal { O } \bigl ( ( \zeta - 1 ) ^ { r } \bigr ) .
$$

Expanding theright-hand expressionintoa Taylor seriesat $\zeta = 1$ and truncating suitably,thisyields thecorresponding $\sigma$ polynomial. If we take

$$
\rho ( \zeta ) = ( \zeta - 1 ) ^ { 2 } ( \zeta ^ { 6 } + \zeta ^ { 4 } + \zeta ^ { 3 } + \zeta ^ { 2 } + 1 ) ,
$$

Table7.1.Symmetric multistep methods for second order problems; $k = 8$ and order $r = 8$   

<table><tr><td colspan="3"></td><td colspan="2">SY8B</td><td colspan="2">SY8C</td></tr><tr><td>i</td><td>αi</td><td>SY8 12096β</td><td>αi</td><td>120960β</td><td>ai</td><td>8640β</td></tr><tr><td rowspan="4">0 1 2</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td></td><td>17671</td><td>0</td><td>192481</td><td></td><td>13207</td></tr><tr><td>2</td><td>-23622</td><td>0</td><td>6582</td><td></td><td>-8934</td></tr><tr><td>0</td><td>61449 -50516</td><td>-1/2 -1</td><td>816783 -156812</td><td>0 0</td><td>42873 -33812</td></tr></table>

wegetin thisway Method SY8of Table 7.1,a method proposedby Quinlan& Tremaine(199o) for computationsincelestial mechanics.All methods of Table7.1 are8-stepmethods,of order8,and symmetric,i.e.,the relations $\alpha _ { i } = \alpha _ { k - i }$ and $\beta _ { i } = \beta _ { k - i }$ aresatisfied.Therefore,we present the coefficients only for $i \le k / 2$ .

These methods give approximations $y _ { n }$ tothe solution of the differential equation.Ifalsoderivative approximations are needed,weget thembyfinitedifferences, e.g.,for the 8th order methodsof Table7.1we use

$$
\begin{array} { r } { \dot { y } _ { n } = \frac { 1 } { 8 4 0 h } \Big ( 6 7 2 ( y _ { n + 1 } - y _ { n - 1 } ) - 1 6 8 ( y _ { n + 2 } - y _ { n - 2 } ) \Big . \qquad } \\ {  \qquad + 3 2 ( y _ { n + 3 } - y _ { n - 3 } ) - 3 ( y _ { n + 4 } - y _ { n - 4 } ) \Big ) . } \end{array}
$$

Weapply thismethod to the Keplerproblem(I.2.2),oncewith eccentricity $e = 0$ and oncewith $e = 0 . 2$ ,andinitialvalues(I.2.11),such thattheperiodoftheexact solution is $2 \pi$ Starting approximationsare computed accuratelywithahigh order Runge-Kutta method.We apply Method SY8with many different step sizesranging from $2 \pi / 3 0$ to $2 \pi / 9 5$ ,and we plotinFig.7.1 themaximumerror of the total energy asa function of $2 \pi / h$ (where $h$ denotes the step size).We see that in general the error decreaseswith the step size,but there isan extremely large error for $h \approx 2 \pi / 6 0$ . For $e \neq 0$ ,furtherpeakscan beobservedat integralmultiplesof5and6.Itisour aimtounderstand this behaviour.

Instabilities.We put $z = q _ { 1 } + \ i q _ { 2 }$ ,sothatthe Keplerproblem becomes

$$
\ddot { z } = \psi ( | z | ) z , \qquad \psi ( r ) = - r ^ { - 3 } ,
$$

and we choose initial values such that $z ( t ) = e ^ { \ i t }$ is a circular motion (eccentricity $e = 0$ ).Thenumerical solution of(1.8）isthereforedefinedbytherelation

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } z _ { n + j } = h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } \psi ( | z _ { n + j } | ) z _ { n + j } .
$$

Approximating $\psi ( | z _ { n + j } | )$ with $\psi ( 1 ) = - \omega ^ { 2 }$ ,wegeta linear recurrence relation with characteristic polynomial

$$
S ( \omega h , \zeta ) = \rho ( \zeta ) + \omega ^ { 2 } h ^ { 2 } \sigma ( \zeta ) .
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/eba4afd5087cba56b5e16feb3b9e80de01521d2288d83999672eceb749736b66.jpg)  
Fig.7.1.Maximumerrorin the total energy during the integration of 25ooorbits of the Kepler problemasa function of the number of steps per period

Theprincipal roots of $S ( \omega h , \zeta ) = 0$ satisfy $\zeta _ { 1 } ( \omega h ) \approx e ^ { i \omega h }$ and $\zeta _ { 2 } ( \omega h ) \approx e ^ { - i \omega h }$ , andwehave|S(wh）|=1forall $\mathcal { I }$ and for sufficiently small $h$ ,because the method issymmetric(Exercise2).As a consequence of $| \zeta _ { 1 } ( \omega h ) | = 1$ ,thevalues $\widehat { z } _ { n } : =$ $\zeta _ { 1 } ( \omega h ) ^ { n }$ arenot only a solution of the linear recurrence relation,but also of the nonlinearrelation(7.3).Ouraim is to study the stability of this numerical solution. Wetherefore consideraperturbed solution

$$
z _ { n } = \zeta _ { 1 } ( \omega h ) ^ { n } \big ( 1 + u _ { n } \big ) .
$$

Using $\begin{array} { r } { | z _ { n } | = 1 + \frac { 1 } { 2 } ( u _ { n } + \overline { { u } } _ { n } ) + \mathcal { O } ( | u _ { n } | ^ { 2 } ) } \end{array}$ and neglecting thequadratic and higher order terms of $\left| u _ { n } \right|$ in the relation（7.3）,we get

$$
\sum _ { j = 0 } ^ { k } ( \alpha _ { j } + \omega ^ { 2 } h ^ { 2 } \beta _ { j } ) \zeta _ { 1 } ( \omega h ) ^ { j } u _ { n + j } = \frac { h ^ { 2 } } { 2 } \psi ^ { \prime } ( 1 ) \sum _ { j = 0 } ^ { k } \beta _ { j } \zeta _ { 1 } ( \omega h ) ^ { j } \big ( u _ { n + j } + \overline { { u } } _ { n + j } \big ) .
$$

Considering alsothecomplex conjugate of thisrelation,and eliminating $u _ { n + j }$ ,we obtaina linearrecurrencerelation for $u _ { n }$ -with characteristic polynomial

$$
S ( \omega h , \zeta _ { 1 } ( \omega h ) \zeta ) \cdot S ( \omega h , \zeta _ { 1 } ( \omega h ) ^ { - 1 } \zeta ) + \mathcal { O } ( h ^ { 2 } ) .
$$

Forsmall $h$ ,its zeros are close to $\zeta _ { 1 } ( \omega h ) ^ { - 1 } \zeta _ { j }$ and $\zeta _ { 1 } ( \omega h ) \zeta _ { l } .$ If two of these zeros collapse,the $\mathcal { O } ( h ^ { 2 } )$ termsin(7.4） can producea root of modulus larger than one, sothat instability occurs.Thisis the case,if two roots $\zeta _ { j }$ , $\zeta _ { l }$ of $\rho ( \zeta ) = 0$ satisfy $\zeta _ { j } \zeta _ { l } ^ { - 1 } \approx \zeta _ { 1 } ^ { 2 } \approx e ^ { 2 i \omega h }$ ,or

$$
\theta _ { j } - \theta _ { l } = \frac { 4 \pi } { N } ,
$$

where $\zeta _ { j } = e ^ { 2 \theta _ { j } }$ and $h = 2 \pi / N$

For theMethod SY8 of Table7.1,thespurious zeros of $\rho ( \zeta )$ have arguments $\pm 4 \pi / 5 , \pm 2 \pi / 5$ ,and $\pm 2 \pi / 6$ With $\theta _ { j } = 2 \pi / 5$ and $\theta _ { l } = 2 \pi / 6$ ,the condition (7.5) gives $N = 6 0$ asacandidate for instability.This explains the experiment ofFig.7.1 for $e = 0$ Astudy of the stability of orbitswith eccentricity $e \neq 0$ (seeQuinlan

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/71bf1f4464c0192b6680122bb469f30fc09f60544279a6e3cc996a226e5348c8.jpg)  
Fig.7.2.Maximumerrorin the total energyduring theintegration of 25oo orbits of the Kepler problemasa function of thenumber ofstepsperperiod

1999)shows that instabilities can also occur when $4 \pi / N$ isreplaced with $2 q \pi / N$ $\mathbf { \Phi } _ { q } = 2 , 3 , \ldots )$ in therelation(7.5）.

Toavoid these instabilities as faras possible,Quinlan(1999) constructed symmetric multistep methods,where the spurious roots of $\rho ( \zeta ) = 0$ arewell spread out on the unit circle and far from $\zeta = 1$ Asaresult he proposes Method SY8B ofTable7.1.The same experimentasaboveyieldstheresultsofFig.7.2.The $\rho$ polynomial ofMethodSY8Bis

$$
\rho ( \zeta ) = ( \zeta - 1 ) ^ { 2 } \big ( \zeta ^ { 6 } + 2 \zeta ^ { 5 } + 3 \zeta ^ { 4 } + 3 . 5 \zeta ^ { 3 } + 3 \zeta ^ { 2 } + 2 \zeta + 1 \big ) ,
$$

and the $\theta _ { j }$ of the spurious roots are $\pm 2 \pi / 2 . 2 7 8$ , $\pm 2 \pi / 3 . 3 5 3$ ,and $\pm 2 \pi / 4 . 6 7 8$ The condition(7.5） is satisfied only for $N \leq 2 3 . 6 7 $ which implies that no instability occurs for $e = 0$ in the region of the experiment of Fig.7.2.

Toillustratethe importance of high order methods,we included in Fig.7.2 the results of the second order partitioned multistep method(1.15).

# XV.7.2Extension to Variable Step Sizes

Variable step size multistep methods for second order differential equations ${ \ddot { y } } =$ $f ( y )$ are of the form

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } ) y _ { n + j } = h _ { n + k - 1 } ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } ) f ( y _ { n + j } ) ,
$$

where the coefficients $\alpha _ { j }$ and $\beta _ { j }$ are allowed to depend on the step sizes $h _ { n } , \ldots$ , $h _ { n + k - 1 }$ ,moreprecisely,on theratios $h _ { n + 1 } / h _ { n } , \ldots , h _ { n + k - 1 } / h _ { n + k - 2 } ,$ Theyyield approximations $y _ { n }$ to $y ( t _ { n } )$ ona variable grid given by $t _ { n + 1 } = t _ { n } + h _ { n }$ Sucha method isoforder $r$ (cf.formula(1.9））,if

$$
\sum _ { i = 0 } ^ { k } \alpha _ { j } ( h _ { n , \cdots } , h _ { n + k - 1 } ) y ( t _ { n + j } ) = h _ { n + k - 1 } ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } ( h _ { n , \cdots } , h _ { n + k - 1 } ) \ddot { y } ( t _ { n + j } )
$$

forall polynomials $y ( t )$ ofdegree $\leq r + 1 .$ It is stable,if the $\rho$ -polynomialwith coefficients $\alpha _ { j } ( h , \ldots , h )$ (constant step size） satisfies the stability condition of Sect.XV.1.2(seeTheoremII.5.7ofHairer,Ngrsett&Wanner（1993）andCano &Duran(2003a)）.

All methods of Sect.XV.7.1 can be extended to symmetric,variable step size integrators.This hasbeen discovered by Cano&Duran(2Oo3b).Forclarity of notationwe let $\widetilde { \alpha } _ { j } , \beta _ { j }$ $\mathbf { \phi } _ { j } = 0 , \ldots , k )$ be the coefficients of such a fixed step size method. Cano $\&$ Duran propose putting

$$
\beta _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } ) = \frac { h _ { n } } { h _ { n + k - 1 } } \widetilde { \beta } _ { j } ,
$$

and to determine $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ such that symmetry and order $k - 2$ (for arbitrary step sizes）are achieved.We also suppose(7.7),butwedetermine the coefficients $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ such that (7.6) holds forall polynomials $y ( t )$ of degree $\le ~ k$ .Thisuniquely determines these coeficients whenever $h _ { n } > 0 , \ldots$ $h _ { n + k - 1 } > 0$ (Vandermonde type system)and gives the following properties.

Lemma7.1.Foreven $k$ ，let $( \widetilde { \alpha } _ { j } , \widetilde { \beta } _ { j } )$ definea symmetric,stable $k$ -stepmethod (1.8）oforder $k$ ,andconsider thevariable step sizemethod givenby(7.7）and $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ such that(7.6)holds forall polynomials $_ y$ satisfying $\deg y \leq$ $k$ Thismethodextendsthefixedstep sizeformula,i.e.,

$$
\alpha _ { j } ( h , \ldots , h ) = \widetilde { \alpha } _ { j } , \qquad \beta _ { j } ( h , \ldots , h ) = \widetilde { \beta } _ { j } ,
$$

itsatisfiesthesymmetry relations

$$
\begin{array} { c } { { \alpha _ { j } ( h _ { n } , . . . , h _ { n + k - 1 } ) ~ = ~ \alpha _ { k - j } ( h _ { n \pm k = 1 } , . . . , h _ { n } ) } } \\ { { { h } _ { n + k - 1 } ^ { 2 } \beta _ { j } ( h _ { n } , . . . , h _ { n + k - 1 } ) ~ = ~ h _ { n } ^ { 2 } \beta _ { k - j } ( h _ { n + k - 1 } , . . . , h _ { n } ) , } } \end{array}
$$

and it isof order $k - 1$ forarbitrarystepsizes.Moreover,itbehaves likeamethod oforder $k$ if $h _ { n + 1 } = h _ { n } { \big ( } 1 + { \mathcal { O } } ( h _ { n } ) { \big ) }$ uniformly in $n$

Proof.Therelation (7.8) for $\beta _ { j }$ follows at once from(7.7）,and for $\alpha _ { j }$ itisaconsequenceof the uniquenessof the solution ofthe linear system for the $\alpha _ { j }$

The second condition of(7.9） follows directly from(7.7）and from the symmetryof theunderlying fixed step size method $\beta _ { k - j } = \beta _ { j }$ forall $\jmath$ ).Inserting （7.7）into （7.6）,replacing $y ( t )$ with $y ( t _ { n + k } + t _ { n } - t )$ ,and reversing the order of $h _ { n } , \ldots , h _ { n + k - 1 }$ yields

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } ( h _ { n + k - 1 } , \ldots , h _ { n } ) y ( t _ { n + k - j } ) = h _ { n } h _ { n + k - 1 } \sum _ { j = 0 } ^ { k } \widetilde { \beta } _ { j } \ddot { y } ( t _ { n + k - j } ) .
$$

Using $\beta _ { k - j } = \beta _ { j }$ this shows that $\alpha _ { k - j } ( h _ { n + k - 1 } , . . . , h _ { n } )$ satisfies exactly the same linear systemas $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ ,sothatalso the firstrelationof(7.9)is verified.

Bydefinition,thevariable step sizemethod isat least of order $k - 1$ Under the assumption $h _ { n + 1 } = h _ { n } { \big ( } 1 + { \mathcal { O } } ( h _ { n } ) { \big ) }$ the defect in(7.6)is of the form

$$
h _ { n } ^ { k + 1 } D ( h _ { n } , \ldots , h _ { n + k - 1 } ) = h _ { n } ^ { k + 1 } D ( h _ { n } , \ldots , h _ { n } ) + { \mathcal O } ( h _ { n } ^ { k + 2 } )
$$

forall sufficiently smooth $y ( t )$ Since the constant step size method is of order $k$ , theexpression $D ( h _ { n } , \ldots , h _ { n } )$ is of size $\mathcal { O } ( h _ { n } )$ ,so that we observe convergence of order $k$ . □

Thesymmetry relation(7.9） has the following interpretation:if the approximations $y _ { n } , \ldots , y _ { n + k - 1 }$ used with step sizes $h _ { n } , \ldots , h _ { n + k - 1 }$ yield $y _ { n + k }$ ,thenthe values $y _ { n + k } , \ldots , y _ { n + 1 }$ appliedwith $h _ { n + k - 1 } , \ldots , h _ { n }$ yield $y _ { n }$ asaresult （since the only on coefficients $h _ { n + k - 1 } ^ { 2 }$ $\alpha _ { j }$ and thesameresultisobtainedwith only depend on step sizeratios and the multistep formula $- h _ { n + k - 1 } , \ldots , - h _ { n } ) .$ Thisisthe analogue of the definition of symmetry for one-step methods.

Forobtaininga good long-time behaviour,the stepsizesalso have to be chosen inasymmetricand reversible way (see Sect.VII.3).One possibility isto take step sizes

$$
h _ { n + k - 1 } = \frac { \varepsilon } { 2 } \Big ( \sigma ( y _ { n + k - 1 } ) + \sigma ( y _ { n + k } ) \Big ) ,
$$

where $\varepsilon > 0$ ,and $\sigma ( y )$ is a given positive monitor function.This condition is an implicit equation for $h _ { n + k - 1 }$ ,because $y _ { n + k }$ dependson $h _ { n + k - 1 } .$ It has to be solved iteratively.Notice,however,that foran explicitmultistepformula no further force evaluations are necessaryduring this iteration.Such achoice of the step sizeguarantees that whenever $h _ { n + k - 1 }$ is chosen when stepping from $y _ { n } , \ldots , y _ { n + k - 1 }$ with $h _ { n } , \ldots , h _ { n + k - 2 }$ to $y _ { n + k }$ ,the step size $h _ { n }$ ischosen when stepping backwards from $y _ { n + k } , \ldots , y _ { n + 1 }$ with $h _ { n + k - 1 } , \ldots , h _ { n + 1 }$ to $y _ { n }$

Implementation.For given initial values $y _ { 0 } , \dot { y } _ { 0 }$ ,the starting approximations $y _ { 1 }$ ， $\cdots , y _ { k - 1 }$ should be computed accurately (forexample,bya high-orderRunge-Kutta method） with step sizes satisfying(7.1O).The solution of the scalar nonlinearequation（7.1O）has to be donecarefullyin order toreduce the overhead of the method.In our code we use $h _ { n + k - 1 } : = h _ { n + k - 2 } ^ { 2 } / h _ { n + k - 3 }$ as predictor,and we apply modified Newton iterationswith thederivativeapproximated by finitedifferences.

The coefficients $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ have to becomputed anewin every iteration.We use the basis

$$
p _ { i } ( t ) = \prod _ { j = 0 } ^ { i - 1 } ( t - t _ { n + j } ) _ { \ast } \qquad i = 0 , \dots , k
$$

for the polynomials of degree $\le \ k$ in(7.6).This leads toa linear triangular system for $\alpha _ { 0 } , \ldots , \alpha _ { k }$ Asnoticed by Cano&Duran(20o3b),thecoefficients $p _ { i } ( t _ { j } )$ and $\ddot { p } _ { i } ( t _ { j } )$ can be obtained efficiently from the recurrence relations

$$
\begin{array} { r l } { p _ { 0 } ( t ) = 1 , \quad } & { p _ { i + 1 } ( t ) = ( t - t _ { i } ) p _ { i } ( t ) } \\ { \dot { p } _ { 0 } ( t ) = 0 , \quad } & { \dot { p } _ { i + 1 } ( t ) = ( t - t _ { i } ) \dot { p } _ { i } ( t ) + p _ { i } ( t ) } \\ { \ddot { p } _ { 0 } ( t ) = 0 , \quad } & { \ddot { p } _ { i + 1 } ( t ) = ( t - t _ { i } ) \ddot { p } _ { i } ( t ) + 2 \dot { p } _ { i } ( t ) . } \end{array}
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/8e83bddd30fc52f67ee122def73b11fdf26a0ee184d88a119335cc14599b3012.jpg)  
Fig.7.3.Maximumerrorinthe total energyduring theintegrationof 25oOorbits of the Kepler problemasa function of the number of stepsper period

During the iterations for the solution of the nonlinear equation(7.1O) only the values of $p _ { i } ( t _ { n + k } )$ have to beupdated.

Numerical Experiment.Werepeat the experiment of Fig.7.1 with the method SY8,but this time in the variable step size version and with $\sigma ( y ) = \| y \| ^ { 2 }$ asstep sizemonitor.We have computed 25oO periods of the Kepler problem with eccentricity $e = 0 . 2$ ,andwehaveplottedinFig.7.3 themaximal error in theHamiltonian asafunction of the number of steps per period (for a comparison we have also included the result of the fixed step sizeimplementation).Similar to(7.2） we use approximations $\dot { y } _ { n }$ thatare the derivative of the interpolation polynomial passing through $y _ { n } , y _ { n \pm 1 } , y _ { n \pm 2 } , . . .$ such that the correct order is obtained.The computationis stopped when the error exceeds $1 0 ^ { - 2 }$ .

Asexpected,the errorissmaller for the variablestep size version,and it is seen that the peaks due to numerical resonances are now much less although they are notcompletely removed.Forlarge step sizes,the performance deteriorates,but this isnota seriousproblem,because these methods are recommended only for high accuracy computations.

It should be remarked that the overhead,due to the computation of the coefficients $\alpha _ { j }$ and the solution of the nonlinearequation(7.1O),is rather high.Therefore, theuse of variable step sizes is recommended only when force evaluations $f ( y )$ are expensive or when constant step sizesare not appropriate.Cano&Duran（2003b) reportan excellent performance of symmetric,variable step size multistep methods forcomputations of the outer solar system.

Despite the resonances and instabilities,then,symmetric methods can stillbea better choice than Stormer methods forlong integrations of planetaryorbits provided that the user isaware of the dangers.

(G.D.Quinlan 1999)

# XV.8Multi-Value or General Linear Methods

General linear methodsisa class of integration methods that coversRunge-Kutta aswell as multistep methods.It is therefore of interest to study which of the results onthe long-time behaviour can be extended.

So-called multi-value or general linearmethodsare defined by $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ where

$$
\begin{array} { l c l } { { Y _ { n + 1 } } } & { { = } } & { { D Y _ { n } + h B f ( U _ { n + 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { U _ { n + 1 } } } & { { = } } & { { C Y _ { n } + h A f ( U _ { n + 1 } ) } } \end{array}
$$

with $f ( U _ { n + 1 } ) = \left( f ( u _ { n + 1 } ^ { 1 } ) , \ldots , f ( u _ { n + 1 } ^ { s } ) \right) ^ { T }$ for $U _ { n + 1 } = \left( u _ { n + 1 } ^ { 1 } , \ldots , u _ { n + 1 } ^ { s } \right) ^ { T } ,$ and $Y _ { n } = ( y _ { n } ^ { 1 } , \dots , y _ { n } ^ { k } ) .$ Weuseasloppy notation inthe sense that the matrices $D , B , \ldots$ should be replaced with $\cal D \otimes \cal I , \cal B \otimes \cal I , . . .$ .Foracomputation,a starting procedure $S _ { h }$ anda finishing procedure $F _ { h }$ ,which extracts the numerical approximation $y _ { n }$ from $Y _ { n } ,$ haveto beadded(seeFig.8.1）.Weassume theexistence ofavector $e$ such thatwith $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T }$

$$
D e = e , \qquad C e = 1 1
$$

holds (preconsistency conditions). The vector $Y _ { n }$ is then an approximation to $e y ( t _ { n } )$ (more precisely to $e \otimes y ( t _ { n } )$ ).

ForRunge-Kutta methods, $D = \mathbf { \tau } ( 1 )$ isthe one-dimensional identity, $B \ =$ $( b _ { 1 } , \dots , b _ { s } )$ , $C = \mathbb { I }$ ,and $A$ is theusual Runge-Kutta matrix.For multistep methods, wehave $Y _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ ,and $\mathcal { D }$ isthe $k \times k$ matrix with characteristic polynomial $\rho ( \zeta )$ asin(2.1）.Foradetailed treatment of general linearmethodswe referthe reader to Chap.4of themonograph of Butcher(1987),and to Chap.III.8 ofHairer,Norsett&Wanner（1993).

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/a617c7f9bf9720f3b801b9269991d7ed4e179b887367c015ac3bb49485ff5d0a.jpg)  
Fig.8.1.Illustration of a multi-value method $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ with starting procedure $S _ { h }$ and finishing procedure $F _ { h }$

# XV.8.1 Underlying One-Step Method and Backward Error Analysis

Inanalogy to multistepmethods,amethod(8.1) iscalled strictly stable,if all eigenvalues of $D$ areinside the unit circle with the exception of the single eigenvalue $\zeta = 1$ .AnextensionofKirchgraber'sresult(Theorem2.1) to strictly stable general linearmethodsis given by Stoffer(1993).

Theorem8.1.Considerastrictly stable general linear method $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ anda finishing procedure $y _ { n } = F _ { h } ( Y _ { n } ) = d ^ { \cal { L } } Y _ { n } +$ $\mathcal { O } ( h )$ Assume that(8.2) and $d ^ { T } e = 1$ hold.

(i)Then there exist a unique one-step method $\varPhi _ { h } ( y )$ and a unique starting procedure $S _ { h } ( y )$ such that $G _ { h } \circ S _ { h } = S _ { h } \circ \phi _ { h }$ and $F _ { h } \circ S _ { h } = I d$ hold.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0009_pages_0561-0630/auto/images/f763688748fb569b8f8c9073cc4820df3956e06dda0b6587ab9d29013384e74c.jpg)

(ii)The manifold $\mathcal { M } _ { h } \ = \ \{ S _ { h } ( y ) ; y \in \mathbb { R } ^ { d } \}$ is invariant under $G _ { h } ,$ anditis exponentiallyattractive.

Proof.Since themethod isstrictlystable,thereexistsamatrix $_ { x }$ such that

$$
\begin{array} { r } { T ^ { - 1 } D T = \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { D _ { 0 } } \end{array} \right) \qquad \mathrm { w i t h } \quad \left. D _ { 0 } \right. < 1 , } \end{array}
$$

and $T e _ { 1 } = e$ (where $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T } )$ .Theproof closely followsthat of Theorem 2.1.With the transformation $( \xi _ { n } , \eta _ { n } ) ^ { I } \ = Z _ { n } = { T } ^ { - 1 } Y _ { n }$ ,thegeneral linear method（8.1） becomes

$$
\left( \begin{array} { c } { \xi _ { n + 1 } } \\ { \eta _ { n + 1 } } \end{array} \right) = \left( \begin{array} { c } { \xi _ { n } } \\ { D _ { 0 } \eta _ { n } } \end{array} \right) + h T ^ { - 1 } B f ( U _ { n + 1 } ) .
$$

with $U _ { n + 1 } = C T Z _ { n } + h A f ( U _ { n + 1 } ) .$ Asbefore,TheoremXII.3.1canbeapplied and yields the existence of an atractive manifold $\mathcal { N } _ { h } = \{ ( \xi , s ( \xi ) ) ; \xi \in \mathbb { R } ^ { d } \}$ ,whichis invariant underthemapping(8.3).We now invert the restriction of $F _ { h }$ onto the manifold ${ \mathcal { N } } _ { h } .$ Due to $d ^ { 2 } e = 1$ and $T e _ { 1 } = e$ ,wehave for $Z = Z ( \xi ) = \left( \xi , s ( \xi ) \right) ^ { T }$ that

$$
y = F _ { h } \big ( T Z ( \xi ) \big ) = d ^ { T } T Z ( \xi ) + \ldots = \xi + g ( \xi ) ,
$$

where $g ( \xi )$ isLipschitz continuous with constant $\mathcal { O } ( h )$ Bythe Banach fixed-point theorem the equation(8.4) has a unique solution $\xi = r ( y )$ Putting

$$
S _ { h } ( y ) = T Z \big ( r ( y ) \big ) = T \left( { r ( y ) } \atop { s \big ( r ( y ) \big ) } \right) ,
$$

wehave found the unique starting procedure satisfying $F _ { h } \circ S _ { h } \ : = \ : I d$ and $T ^ { - 1 } S _ { h } ( y ) \in { \mathcal { N } } _ { h } .$ Wefinally define $\phi _ { h } = F _ { h } \circ G _ { h } \circ S _ { h }$ and $\mathcal { M } _ { h } = \{ T Z \} , Z \in \mathcal { N } _ { h } \}$ , sothatall statements of the theoremareverified. □

Itis our aim to extend the concept of an underlying one-step method to nearly all(includingweakly stable) general linear methods.

Theorem8.2.Considera general linear method(8.1),and assume that $\zeta ~ = ~ 1$ isasingle eigenvalue of the propagation matrix $D$ Furthermore,let $G _ { h } ( Y )$ and $F _ { h } ( Y ) = d ^ { T } Y + \ldots$ have expansions in powers of $h$ andassume that(8.2)and $d ^ { T } e = 1$ hold.Then there exist auniqueformal one-stepmethod

$$
\Phi _ { h } ( y ) = y + h d _ { 1 } ( y ) + h ^ { 2 } d _ { 2 } ( y ) + \dots .
$$

andaunique formal startingprocedure

$$
S _ { h } ( y ) = e y + h S _ { 1 } ( y ) + h ^ { 2 } S _ { 2 } ( y ) + \dots ,
$$

such that formally $G _ { h } \circ S _ { h } = S _ { h } \circ \phi _ { h }$ and $F _ { h } \circ S _ { h } = I d$ hold.

Proof.Expanding $S _ { h } \left( \varPhi _ { h } ( y ) \right)$ and $G _ { h } ( S _ { h } ( y ) )$ into powers of $h$ ,acomparison of the coefficients yields

$$
e d _ { j } ( y ) + ( I - D ) S _ { j } ( y ) = \ldots ,
$$

wherearight-hand side depends on known functions and on $d _ { i } ( y ) , S _ { i } ( y )$ with $i < j$ . Similarly,the condition $F _ { h } \big ( S _ { y } ( y ) \big ) = y$ leadsto

$$
d ^ { T } S _ { j } ( y ) = \cdots .
$$

Due to the fact that $\zeta = 1$ isa single eigenvalue of $\mathcal { D }$ ,and that $d ^ { 1 } e \neq 0$ ,thesystem (8.5)-(8.6)uniquely determines $d _ { j } ( y )$ and $S _ { j } ( y )$ . □

Backward ErrorAnalysis forSmooth Numerical Solutions.The formal analysisof Chap.IX can bedirectly applied to theunderlying one-stepmethod of Theorem8.2.Thisyieldsa modified differential equation,but only for the smooth numerical solution (cf.Sect.XV.3.1).Notice that this modified equationdepends on the choice of the finishing procedure $F _ { h }$

# XV.8.2Symplecticity and Symmetry

Before givingaprecise meaning to thesymplecticityand symmetry of general linear methods,we establish the following lemma.

Lemma 8.3.Fora general linearmethod $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ we considertwo different finishing procedures $y _ { n } = F _ { h } ( Y _ { n } )$ and $\widehat { y } _ { n } = \widehat { F } _ { h } ( Y _ { n } )$

$$
\begin{array} { r c l } { { \widehat { y } _ { 0 } \quad \displaystyle \longrightarrow \quad \widehat { \Phi } _ { h } \quad \ } } & { { \widehat { y } _ { 1 } \quad \displaystyle \longrightarrow \quad \widehat { \Phi } _ { h } \quad } } & { { \widehat { y } _ { 2 } \quad \displaystyle \stackrel { \widehat { \Phi } _ { h } } { \longrightarrow } \quad \cdots } } \\ { { \widehat { S } _ { h } \left\downarrow \right. \widehat { F } _ { h } } } & { { \displaystyle \uparrow \widehat { F } _ { h } } } & { { \displaystyle \uparrow \widehat { F } _ { h } } } \\ { { Y _ { 0 } \quad \displaystyle \longrightarrow \quad \widehat { G } _ { h } \quad \displaystyle \longrightarrow \quad Y _ { 1 } \quad \displaystyle \xrightarrow [ { { G } _ { h } } ] { G _ { h } } \quad Y _ { 2 } \quad \displaystyle \xrightarrow [ { G } ] { G _ { h } } \quad \cdots } } \\ { { S _ { h } \left\uparrow \right. F _ { h } } } & { { \displaystyle \downarrow \ F _ { h } } } & { { \displaystyle \downarrow \ F _ { h } } } \\ { { y _ { 0 } \quad \displaystyle \longrightarrow \quad y _ { 1 } \quad \displaystyle \longrightarrow \quad y _ { 1 } \quad \displaystyle \longrightarrow \quad y _ { 2 } \quad \displaystyle \xrightarrow [ { \Phi } ] { \Phi _ { h } } \quad \displaystyle } } & { { \displaystyle \cdots } } \end{array}
$$

The two corresponding one-step methods $\varPhi _ { h } ( y )$ and $\widehat { \varPhi } _ { h } ( y )$ (given by Theorem8.2)are then conjugate to each other,i.e,

$$
\alpha _ { h } ^ { - 1 } \circ \varPhi _ { h } \circ \alpha _ { h } = \widehat { \Phi } _ { h } \qquad w i t h \qquad \alpha _ { h } = F _ { h } \circ \widehat { S } _ { h } .
$$


<!-- chunk 0010: pages 631-664 -->
Proof.The equations involving the underlying one-step methods or the starting procedures have to beunderstood in the senseof formal series.By Theorem8.2we have $S _ { h } ( y ) = e y + \mathcal { O } ( h )$ and also $\widehat { S } _ { h } ( y ) = e y + \mathcal { O } ( h ) .$ Itthus follows from $F _ { h } \circ S _ { h } = I d$ that $\alpha _ { h } ( y )$ is ${ \mathcal { O } } ( h )$ -closetothe identityand therefore invertible. □

The transformation $\alpha _ { h }$ in the phase space is $\mathcal { O } ( h )$ -close to the identity.The relation $\alpha _ { h } ^ { - 1 } \circ \varPhi _ { h } ^ { n } \circ \alpha _ { h } = \varPhi _ { h } ^ { n }$ ichisseeef.7o that the numerical solutions of $\phi _ { h }$ and $\widehat { \varPhi } _ { h }$ remain ${ \mathcal { O } } ( h )$ -close forall times.This means that the long-time behaviour of bothmethodsis exactlythe same.

Consequently,fora given general linear method $G _ { h }$ ,it is sufficient to require symplecticity or symmetry for one finishing procedure only.

Definition8.4 (Symplecticity）.A general linear method $G _ { h }$ iscalled symplectic if there exists a finishing procedure $F _ { h }$ such that the underlying one-step method $\varPhi _ { h }$ of Theorem 8.2 is symplectic,i.e., $\varPhi _ { h } ^ { \prime } ( y ) ^ { T } J \varPhi _ { h } ^ { \prime } ( y ) = J$ in the sense of formal series.

Thestudy of symplecticity of linearmultistepmethods(Sect.XV.4.1)wasrather disappointing.Wecould not find one linear multistepmethod whose underlying onestepmethod is symplectic.For general linear methods,some necessary conditions for the symplecticity of the underlying one-step method are known which are hard tosatisfy(Hairer&Leone 1998).For themoment,no symplectic general linear method(not equivalent toa one-step method) is known,and we conjecture that such amethod does not exist,even in the class of partitioned general linear methods (treating the $p$ and $q$ variables bydifferent methods).

After the disappointing non-existence conjecture of symplectic multi-value methods,we turn our attention to symmetric methods.We know from the previous chaptersthat forreversibleHamiltonian systems,thelong timebehaviour of symmetric one-step methodscan be as good as that for symplectic methods.There are several definitions of symmetric general linear methods in the literature.However,they areeither tailored to very special situations(e.g.,Hairer,Nprsett&Wanner 1993), ortheydo not allow the proof of results that areexpectedto hold for symmetric methods.

Definition8.5 (Symmetry).A general linear method $G _ { h }$ iscalled symmetricif there exists a finishing procedure $F _ { h }$ such that the underlying one-step method $\phi _ { h }$ of Theorem 8.2 is symmetric,i.e., $\bar { \boldsymbol { \phi } } _ { - h } ( y ) = \bar { \boldsymbol { \phi } } _ { h } ^ { - 1 } ( y )$ in the sense of formal series.

Example8.6.Consider the trapezoidal method in the role of $G _ { h }$ and the explicit Euler method with step size $- \gamma h$ as finishing procedure:

$$
\begin{array} { r l } { G _ { h } : } & { { } \quad Y _ { n + 1 } = Y _ { n } + { \frac { h } { 2 } } { \Big ( } f ( Y _ { n } ) + f ( Y _ { n + 1 } ) { \Big ) } } \\ { F _ { h } : } & { { } \quad y _ { n + 1 } = Y _ { n + 1 } - \gamma h f ( Y _ { n + 1 } ) } \end{array}
$$

The corresponding starting procedure and underlying one-step methods are then the implicit Eulermethod and the following2-stageRunge-Kutta method:

$$
{ \begin{array} { r l } { S _ { h } : } & { \quad Y _ { n } = y _ { n } + \gamma h f ( Y _ { n } ) } \\ { \quad } & { \quad { \mathrm { ~ } } } \\ { \Phi _ { h } : } & { \quad { \mathrm { R u n g e - K u t t a ~ m e t h o d } } } \end{array} } \quad \begin{array} { r l } { \gamma } & { \gamma } \\ { 1 + \gamma \ \left. \begin{array} { c c } { 1 / 2 + \gamma } & { 1 / 2 } \\ { 1 / 2 + \gamma \ 1 / 2 - \gamma } \end{array} \right. } \end{array} 
$$

Themethod $\phi _ { h }$ issymmetric only for $\gamma = 0$ ,for $\gamma = 1 / 2$ ,andfor $\gamma = - 1 / 2$ . Thisexample demonstrates that the symmetry of the underlying one-step method strongly depends on the finishing procedure.

Onthe other hand,this example shows that the 2-stage Runge-Kutta method issymmetric in the sense of Definition 8.5 forall $\gamma$ (because it is conjugate to the trapezoidal rule).Itis not symmetric accordingto the definition of Chap.V.

AUseful Criterion for Symmetry.Definition 8.5israther impractical for verifying thesymmetry of a givengeneral linear method.We give herealgebraicconditions for the coefficients $A , B , C , D$ ofageneral linear method(8.1),which are sufficient for the method to be symmetric.We assume that the finishing procedure $y _ { n + 1 } =$ $F _ { h } ( Y _ { n + 1 } )$ is given by

$$
y _ { n + 1 } = \widetilde { D } Y _ { n + 1 } + h \widetilde { B } f ( V _ { n + 1 } ) , \qquad V _ { n + 1 } = \widetilde { C } Y _ { n + 1 } + h \widetilde { A } f ( V _ { n + 1 } ) ,
$$

in complete analogy to method(8.1).

Lemma 8.7 (AdjointMethod).Let $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ bethegeneral linearmethod givenby $A , B , C , D$ (withinvertible $\mathcal { D }$ ), $y _ { n + 1 } = F _ { h } ( Y _ { n + 1 } )$ thefinishing procedure givenby $A , \tilde { B } , \tilde { C } , \tilde { D }$ anddenote by $\varPhi _ { h }$ itsunderlying one-step method.Then,the underlying one-stepmethod of

$$
\begin{array} { l l l l l } { { G _ { h } ^ { * } : } } & { { \quad A ^ { * } = C D ^ { - 1 } B - A , } } & { { B ^ { * } = D ^ { - 1 } B , } } & { { C ^ { * } = C D ^ { - 1 } , } } & { { D ^ { * } = D ^ { - 1 } } } \\ { { F _ { h } ^ { * } : } } & { { \quad \widetilde { A } ^ { * } = - \widetilde { A } , } } & { { \widetilde { B } ^ { * } = - \widetilde { B } , } } & { { \widetilde { C } ^ { * } = \widetilde { C } , } } & { { \widetilde { D } ^ { * } = \widetilde { D } } } \end{array}
$$

is the adjoint method $\bar { \varPhi } _ { h } ^ { * } = \bar { \varPhi } _ { - h } ^ { - 1 }$ of $\phi _ { h }$

Proof.Substituting $h  - h$ and $Y _ { n + 1 }  Y _ { n }$ in (8.1)yields

$$
U _ { n + 1 } = C Y _ { n + 1 } - h A f ( U _ { n + 1 } ) , \qquad Y _ { n } = D Y _ { n + 1 } - h B f ( U _ { n + 1 } ) .
$$

Extracting $Y _ { n + 1 }$ from the second relation and inserting it into the first gives

$$
\begin{array} { r l } & { U _ { n + 1 } = C D ^ { - 1 } Y _ { n } + h ( C D ^ { - 1 } B - A ) f ( U _ { n + 1 } ) } \\ & { Y _ { n + 1 } = D ^ { - 1 } Y _ { n } + h D ^ { - 1 } B f ( U _ { n + 1 } ) , } \end{array}
$$

which is exactly method $G _ { h } ^ { * } .$ The same replacements in the finishing procedure

$$
V _ { n + 1 } = \widetilde { C } Y _ { n } - h \widetilde { A } f ( V _ { n + 1 } ) , \qquad y _ { n } = \widetilde { D } Y _ { n } - h \widetilde { B } f ( V _ { n + 1 } )
$$

and in the diagram of Theorem 8.2 prove the statement.

Theorem8.8.Ifthereexistan invertible matrix $Q$ (satisfying $Q e = e$ withegiven by(8.2))and apermutation matrix $P$ such that

$$
\begin{array} { l l } { { P ^ { - 1 } A P ~ = ~ C D ^ { - 1 } B - A , } } & { { ~ Q ^ { - 1 } B P ~ = ~ D ^ { - 1 } B , } } \\ { { P ^ { - 1 } C Q ~ = ~ C D ^ { - 1 } , } } & { { ~ Q ^ { - 1 } D Q ~ = ~ D ^ { - 1 } , } } \end{array}
$$

thenthe general linearmethod $( 8 , I )$ issymmetric.

Proof.Weconsiderthe change of variables $Y _ { n } = Q { \hat { Y } } _ { n }$ , $U _ { n } = P \bar { U } _ { n }$ in the method (8.1）.Since $P$ isa permutation matrix,we have $f ( P U ) = P f ( U )$ ,sothat the method becomes

$$
\begin{array} { r } { P \widehat { U } _ { n + 1 } = C Q \widehat { Y } _ { n } + h A P f ( \widehat { U } _ { n + 1 } ) , \qquad Q \widehat { Y } _ { n + 1 } = D Q \widehat { Y } _ { n } + h B P f ( \widehat { U } _ { n + 1 } ) . } \end{array}
$$

The assumption (8.9) implies that this method is the same as the adjoint method ofLemma 8.7.Takinga finishing procedure $F _ { h }$ in such a way that $y _ { n + 1 } =$ $F _ { h } ( Q { \widehat { Y } } _ { n + 1 } )$ is identical to the finishing procedure $y _ { n + 1 } = F _ { h } ^ { * } ( { \widehat { Y } } _ { n + 1 } )$ of theadjoint method (i.e., $\bar { B } = 0$ and $\bar { D }$ such that $\tilde { D } Q = \tilde { D }$ weobtain $\phi _ { h } ^ { * } = \phi _ { h }$ This proves the statement. □

The sufficient condition of Theorem8.8 reduces tothe known criteria forclassical methods.Let us give some examples:

ForRunge-Kutta methods we have $D = ( 1 )$ , $B = b ^ { T }$ a rowvector,and $C = 1 1$ With $Q = ( 1 )$ and $P$ the permutation matrix that inverts the elements of a vector, weget

$$
b ^ { T } \boldsymbol { P } = b ^ { T } , \qquad \boldsymbol { P } \boldsymbol { A } \boldsymbol { P } = \mathbb { 1 } b ^ { T } - \boldsymbol { A } ,
$$

which is the same (V.2.4).

Multistep methods in their formas general linear methods(Sect.XV.8) satisfy the condition of Theorem 8.8if

$$
\alpha _ { i } = - \alpha _ { k - i } , \qquad \beta _ { i } = \beta _ { k - i } .
$$

Onecan take for $P$ and $Q$ thepermutation matrices (inverting the elements ofa vector)of dimension $k + 1$ and $k$ ,respectively.

# XV.8.3 Growth Parameters

Forarigorous study of the long-time behaviour of general linear methods it is not sufficient to investigate smooth numerical solutions.One has to get bounds on the parasitic solution components,which are present when one considers the general linearmethod without any startingand finishing procedure.This is certainlydifficult, asitis formultistep methods(1.1).We restrict here our analysis to the linearized parasitic modified equation.

The eigenvalues of the matrix $D$ in(8.1)will play the role of the zeros of $\rho ( \zeta )$ in (1.1).We denote them by $\zeta _ { 1 } = 1$ and $\zeta _ { 2 } , \ldots , \zeta _ { k }$ ,andwe assume that they are simple and of modulus one.Motivated by theanalysis for multistep methodswewrite the approximations $Y _ { n }$ as

$$
Y _ { n } = Y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } Z _ { \ell } ( n h )
$$

with smooth functions $Y ( t )$ and $Z _ { \ell } ( t ) .$ Theindex set $\mathcal { L } ^ { \ast }$ has the samemeaning as in Sect.XV.3.2.We insert (8.11)into(8.1） and compare coefficients of $\zeta _ { \ell } ^ { n } .$ This gives with $t = n h$

$$
\begin{array} { r c l } { { } } & { { } } & { { Y ( t + h ) ~ = ~ D Y ( t ) + h B f \big ( C Y ( t ) \big ) + { \mathcal O } ( h ^ { 2 } ) } } \\ { { } } & { { } } & { { \zeta _ { \ell } Z _ { \ell } ( t + h ) ~ = ~ D Z _ { \ell } ( t ) + h B f ^ { \prime } \big ( C Y ( t ) \big ) C Z _ { \ell } ( t ) + { \mathcal O } ( h ^ { 2 } ) . } } \end{array}
$$

To getan amenable form of the modified equations we write the vectors $Y ( t ) , Z _ { \ell } ( t )$ in the basis of eigenvectors of $\mathcal { D }$ ,which we denote by $w _ { 1 } = e$ and $w _ { 2 } , \ldots , w _ { k }$

$$
Y ( t ) = \sum _ { j = 1 } ^ { k } y _ { j } ( t ) w _ { j } , \qquad Z _ { \ell } ( t ) = \sum _ { j = 1 } ^ { k } z _ { \ell , j } ( t ) w _ { j } ,
$$

Inserted into(8.12) and expanded intoa series of $h$ yields

$$
\dot { y } _ { 1 } = f ( y _ { 1 } ) + \mathcal { O } ( h ) ,
$$

andalgebraicrelationsof theform $y _ { j } ( t ) = \mathcal { O } ( h )$ for $j \ \geq \ 2$ Similarly,we get algebraicrelations for $z _ { \ell , j } ( t ) = \mathcal { O } ( h )$ if $j \neq \ell$ andthe function $z _ { \ell } ( t ) : = z _ { \ell , \ell } ( t )$ satisfies

$$
\dot { z } _ { \ell } = \mu _ { \ell } f ^ { \prime } ( y _ { 1 } ) z _ { \ell } + O ( h ) \qquad \mathrm { w i t h } \qquad \mu _ { \ell } = \zeta _ { \ell } ^ { - 1 } w _ { j } ^ { * } B C w _ { j } ,
$$

where $w _ { j } ^ { \ast }$ is the left eigenvector of $D$ corresponding to the eigenvalue $\zeta _ { \ell } .$ Thisisin perfectanalogytothe computations of Sect.XV.5.1.

Thisanalysis can be extended straightforwardly to partitioned general linear methods,wheredifferent methods are applied to thecomponents $y$ and $\upsilon$ ofapartitioneddifferential equation.Unfortunately,wedonotknow ofany results that would extend those of Sect.XV.6to generallinear methods.

# XV.9 Exercises

1. Let $\zeta _ { 1 } ( z )$ be the principal root of the characteristic equation $\rho ( \zeta ) - z \sigma ( \zeta ) = 0$ . Prove that for irreducible multistep methodsthe condition $\zeta _ { 1 } ( - z ) \zeta _ { 1 } ( z ) \equiv 1$ （in a neighbourhood of $z = 0$ ）isequivalent toth、symmetry of themethod.

2.(Lambert&Watson 1976).Prove that stable,symmetric linear multistepmethods(1.8) for second orderdifferential equations,for which the polynomial $\rho ( \zeta )$ has only simple zeros(with the exception of $\zeta = 1$ ),hasanon-vanishing interval of periodicity,i.e.,theroots $\zeta _ { i } ( z )$ of $\rho ( \zeta ) - z ^ { 2 } \sigma ( \zeta ) = 0$ satisfy $| \zeta _ { i } ( i y ) | = 1$ forsufficiently small real $y$

Hint.Simple roots cannot Ieave the unit circleunder small perturbations of $y$

3.Considerasymmetric,s-stable multistep method (1.8).If it is irreducible (no common factors of $\rho ( \zeta )$ and $\sigma ( \zeta )$ ),then $k$ is even.Hence $\rho ( - 1 ) \neq 0$ .

4.Using TheoremXII.3.2,prove that the underlying one-step methodofastrictly stable $r$ thorderlinearmultistepmethod has order $r$ .

5.(Dahlquist 1959).Consider the linear problem $\dot { y } = \lambda y$ and apply asymmetric linearmultistep method(1.1） asin Example2.2.Prove that for $t = n h$ and $h \to 0$ ,

$$
\zeta _ { j } ^ { n } ( \lambda h ) \approx \zeta _ { j } ^ { n } e ^ { \mu _ { j } \lambda t } ,
$$

where $\mu _ { j }$ is the growth parameter.

6.Considera general linear method(8.1).If there exist an invertiblesymmetric matrix $G$ and a diagonal matrix $\varLambda$ such that

$$
\begin{array} { r } { M = \left( \begin{array} { c c } { D ^ { T } G D - G } & { D ^ { T } G B - C ^ { T } A } \\ { B ^ { T } G D - A C } & { B ^ { T } G B - A ^ { T } A - A A } \end{array} \right) = 0 , } \end{array}
$$

then the method is $G$ -symplectic.

Hint.Adapt the proof of Burrage& Butcher for $B$ -stability(seeHairer&Wanner(1996),page 358).

7.ARunge-Kutta method can be considered as a general linear method with $D =$ (1）， $C = \mathbb { 1 }$ .Provethat thecondition (9.1）is equivalent tothe symplecticity condition of Chap.VI.

8.Extend the definition of $G$ -symplecticitytopartitioned general linear methods, and prove that the condition

$$
M = \left( \begin{array} { c c } { { D ^ { T } G \widehat { D } - G } } & { { D ^ { T } G \widehat { B } - C ^ { T } A } } \\ { { B ^ { T } G \widehat { D } - A \widehat { C } } } & { { B ^ { T } G \widehat { B } - A ^ { T } A - A \widehat { A } } } \end{array} \right) = 0
$$

implies that the method is $G$ -symplectic.

9.Construct general linear methods of order $r > 2$ ,forwhich all growth parametersare positive.Find such methods,which have a smaller degree of implicitness than symmetric one-step methods of the same order.

0.WriteaMaple program that checks thecoeffcientsof Table7.1.Afterdefining rho: $\scriptstyle = \rho ( z )$ ,usethe instructions $>$ sigma taylor(rho/(log(z)\*log(z)),z=1,8）; $>$ factor（expand(convert(sigma,polynom)））;

11.Construct partitioned general linear methods which are symmetric,explicit,of high order,and forwhich the matrices $D$ and $\widehat { D }$ have distinct eigenvalues (with theexception of1).Comparedtomultistepmethods,smallerdimensions of the matrices $D$ and $\widehat { D }$ arepossible.

Bibliography

R.Abraham&J.E.Marsden,FoundationsofMechanics,2nded.,Benjamin/CummingsPublishingCompany,Reading,Massachusetts,1978./XIV.3]   
L.Abia&J.M.Sanz-Serna,PartitionedRunge-Kuttamethodsfor separable Hamiltonian problems,Math.Comput.60(1993)617-634.[VI.7],[IX.10]   
M.J.Ablowitz&J.F.Ladik,Anonlineardiffrenceschemeand inversescattering,Studiesin Appl.Math.55(1976)213-229.[VI1.4]   
M.P.Allen&D.J.Tildesley,ComputerSimulationofLiquids,ClarendonPress,Oxford,1987. [1.4]   
H.C.Andersen,Ratle:a"velocity"versionoftheShakealgorithm formoleculardynamics calculations,J.Comput.Phys.52(1983)24-34.[VII.1]   
V.I.Arnold,Smalldenominatorsandproblemsofstabilityofmotioninclassicalandcelestial mechanics,RussianMath.Surveys18(1963)85-191.[1.1]   
V.I.Arnold,SurlageometriedifferentielledesgroupesdeLiededimensioninfinieetses applicationsal'hydrodynamiquedesfluidesparfaites,Ann.Inst.Fourier16(1966)319- 361.[VI.9]   
V.I.Arnold,MathematicalMethodsofClassicalMechanics,Springer-Verlag,NewYork, 1978,secondedition1989.[V1],[VI.2],[V.5],[X.1],[X.7]   
V.I.Arnold,V.V.Kozlov&A.I.Neishtadt,Mathematical AspectsofClassicalandCelestial Mechanics,Springer,Berlin,1997.[X.1]   
U.Ascher&S.Reich,Onsomedifficultiesinintegratinghighlyoscillatory Hamiltoniansystems,inComputational MolecularDynamics,Lect.NotesComput.Sci.Eng.4,Springer Berlin,1999,281-296.[V.4]   
A.Aubry&P.Chartier,Pseudo-symplecticRunge-Kuttamethods,BIT38(1998)439-461. [X.7]   
H.F.Baker,Alternantsandcontinuousgroups,Proc.ofLondonMath.Soc.3(1905)24-47. [111.4]   
M.H.Beck,A.Jackle,G.A.Worth&H.-D.Meyer,Themulticonfigurationtime-dependent Hartree(MCTDH)method:A highlyefficient algorithmforpropagatingwavepackets, Phys.Rep0rts324(2000)1-105.[IV.9].[VII.6]   
G.Benettin,A.M.Cherubini&F.Fasso,Achanging-chart symplectic algorithmforrigid bodiesandother Hamiltoniansystemsonmanifolds,SIAMJ.Sci.Comput.23(2001) 1189-1203.[VI1.4]   
G.Benettin,L.Galgani&A.Giorgilli,Poincare'snon-existence theoremand classical perturbation theory fornearlyintegrable Hamiltoniansystems,Advancesin nonlinear dynamicsand stochastic processes(Florence,1985) World Sci.Publishing,Singapore, 1985,1-22.[X.2]   
G.Benettin,L.Galgani&A.Giorgili.Realization of holonomicconstraintsandfreezing of highfrequencydegreesoffreedominthelightofclassicalperturbationtheory.PartI, Comm.Math.Phys.113(1987)87-103.(XI/I.6]   
G.Benettin,L.Galgani&A.Giorgilli,Realizationof holonomicconstraintsand freezing ofhighfrequencydegreesoffreedominthelightofclassicalperturbationtheory.I, Commun.Math.Phys.121(1989)557-601.[XII.9]   
G.Benettin,L.Galgani,A.Giorgilli&J.-MStrelcyn,AproofofKolmogorov'stheorem oninvarianttoriusingcanonicaltransformationsdefinedbytheLiemethod,IlNuovo Cimento79B(1984)201-223./X.5]   
G.Benettin&A.Giorgilli,OntheHamiltonian interpolationofneartotheidentitysymplecticmappingswithapplicationtosymplecticintegrationalgorithms,J.Statist.Phys.74 (1994)1117-1143.[IX.3],[IX.7],[IX.8]   
B.J.Berne,Moleculardynamicsinsystemswithmultipletimescales:referencesystempropagatoralgorithms,inComputationalMolecular Dynamics:Challenges,Methods,Ideas (P.Deufhard etal.,eds.).Springer,Berlin1999,297-318.[XII.1]   
Joh.Bernouli,Problemeinversedesforcescentrales,extraitdelareponsedeMonsieur BermoulliaMonsieurHerman,Mem.del'Acad.R.desSciencesdeParis(1710)p.521, OperaOmniaI,p.470-480.[1.2]   
M.BerryHistoriesofadiabaticquantumtransitions,Proc.Royal Soc.LondonA429(1990) 61-72.[XIV.1]   
VBetz&S.Teufel,Precisecoupling termsinadiabatic quantumevolution,Ann.Henri Poincare6(2005)217-246.[XIV.1]   
V.Betz&S.Teufel,Precisecouplingtermsinadiabaticquantumevolution:thegenericcase, Comm.Math.Phys.,toappear(2005).[X/V.11   
J.J.Biesiadecki&R.DkelDangersofmultipletimestepmethods,J.Comput.Pys.109 （1993)318-328.[1.4].[VII.4].[XI.1]   
G.D.Birkhoff,RelativityandModernPhysicsHarvardUniv.Press,Cambridge,Mas923. [1.6]   
G.D.Birkhoff,Dynamical Systems,AMs,Providence,R.I.,1927.[X.2]   
S.Blanes,Highordernumericalintegratorsfordiffrentialequationsusingcompositionand processingoflow ordermethods,Appl.Num.Math.(2001)289-306.[V.3]   
S.Blanes&F.Casas,Onthenecessityofnegativecoeffcientsforoperatorsplittng shemes oforder higherthantwo,Appl.Num.Math.54(2005)23-37.[I1.3]   
S.BlanesFCas&RosSmpecticnegtosihocessinggeneraldyA J.Sci.Comput.21(1999)149-161./V.3]   
S.Blanes,F.Casas&J.Ros,Improved high orderintegratorsbasedonthe Magnusexpansion,BIT40(2000a)434-450.[IV.7]   
S.Blanes,F.Casas&J.Ros,Processingsymplecticmethodsfornear-integrableHamiltonian systems,CelestialMech.Dynam.Astronom.77(200ob)17-35.[V.3]   
S.Blanes&P.C.Moan,Practical symplecticpartitionedRunge-KuttaandRunge-Kutta-Nystrommethods,J.Comput.Appl.Math.142(2002)313-330.[V.3]   
P.B.Bochev&C.Scovel,Onquadraticinvariantsand symplecticstructure,BIT34(1994) 337-345.[VI.4],[XV.4]   
N.Bogolioubov&I.Mitropolski,LesMethodesAsymptotiquesenTheoriedesOscillations NonLineaires,Gauthier-Villars,Paris,962.[l.2]   
N.N.Bogolubov&YitroposkyAsmpoticeodsintheeoryofonLinear Oscillations,Hindustan PublishingCorp.,Delhi,1961.[XIl.1]   
J.F.Bonnans&J.Laurent-Varin,Computationoforderconditions for symplecticpartitionedRunge-Kuttashemeswithapplicationtotimalcontrol,umer.athoap pear(2006).[VI.10]   
M.Bom&V.Fock,Beweis desAdiabatensatzes,Zeitschr.f.Physik 51(1928)165-180. [XIV.1],[XIV.4]   
F.Bornemann,HomogenizationinTimeofSingularly Perturbed Mechanical Systems. SpringerLNM1687(1998).[X/V.3]   
EBour,L'integrationdesequationsdiffrentiellesdelamecaniqueanalytiqueJ.Math PuresetAppliquees20(1855)185-200.[X.1]   
K.E.Brenan,S.L.Campbell&L.R.Petzold,NumericalSolutionof Initial-ValueProblems inDifferential-gebraicEquations,assicsinAppl.ath.,A,Piladelphia,996. [IV.10]   
T.J.Bridges&S.Reich,ComputingLyapunovexponentsona Stiefelmanifold,PhysicaD 156(2001)219-238.[IV.9],[IV.10]   
Ch.Brouder,Runge-Kutamethodsandrenormalization,Euro.Phys.J.C12(20o)521- 534.[II.1]   
Ch.Brouder,TreesRenormalizationandDifferentialEquations,BI44(2004)425-438. [II.1]   
C.J.Budd&.Diggott,Geometricintegrationanditspplications,HandbookofNumer icalAnalysisXI(2003)35-139.[VII.2]   
O.Buneman,Time-reversiblediferenceprocedures,J.Comput.Physics1(1967)517-535. [V.1]   
C.Burnton&R.Scherer,Gauss-Runge-Kutta-Nystrommethods,BIT38(1998)12-21. [V1.10]   
K.Burrage&J.C.Butcher,StabilitycriteriaforimplicitRunge-Kuttamethods,AMJ. Numer.Anal.16(1979)46-57.[V1.4]   
J.C.ButcherCoeficientsforthestudyofRunge-Kuttaintegrationprocesses,J.Autral. Math.Soc.3(1963)185-201.[II.1]   
J.C.Butcher,ImplicitRunge-Kutaprocesses,Math.Comput.18(1964a)50-64.[I.1]   
J.C.Butcher,Integrationprocesses basedonRadau quadratureformulas,Math.Comput.18 (1964b)233-244.[II.1]   
J.C.ButcherTheefctiveoderofRunge-KutamethodsinJLl.orrs,ed,Proceedingsof ConferenceontheNumerical Solution of Differential Equations,LectureNotes in Math. 109(1969)133-139.[V.3]   
J.C.Butcher,Analgebraic theoryofintegrationmethods,Math.Comput.26(1972)79-106. [II.1],[III.3]   
J.C.Butcher,The Numerical AnalysisofOrdinary Diffrential Equations.Runge-Kuttaand GeneralLinearethods,JohnWiley&ons,Cichester,987.[.O],[II],[V7], [XV.8]   
J.C.Butcher,Orderandeffctiveorder,Appl.Numer.Math.28(1998)179-191.[V.3]   
J.C.Butcher&J.M.Sanz-Serna,ThenumberofconditionsforaRunge-Kuttamethodto haveeffectiveorderp,Appl.Numer.Math.22(1996)103-111.[1I.1],[V.3]   
J.C.Butcher&G.Wanner,Runge-Kuttamethods:somehistorical notes,Appl.Numer. Math.22(1996)113-151.[II.1]   
M.P.Calvo,Highorderstartingiteratesforimplicit Runge-Kuttamethods:an improvementforvariable-stepsymplectic integrators,IMAJ.Numer.Anal.22(2002)153-166. [VIII.6]   
M.P.Calvo&E.Hairer,Accuratelong-termintegrationofdynamicalsystems,Appl.Numer. Math.18(1995a)95-105.[X.3]   
M.P.Calvo&E.Hairer,Further reductioninthenumberofindependentorderconditions for symplectic,explicitPartitionedRunge-KutaandRunge-Kutta-Nystrommethods,Appl. Numer.Math.18(1995b)107-114.[III.3]   
M.P.Calvo,A.Iserles&A.Zanna,Numerical solutionofisospectral flows,Math.Comput.66(1997)1461-1486.[IV.3]   
M.P.CalvoA.Iserles&A.Zanna,Conservativemethodsfor theToda latticeequations, IMAJ.Numer.Anal.19(1999)509-523.[IV.3]   
M.P.Calvo,.A.Lpe-rcos&JMnSenaVriblestepimplementationofe metricintegrators,Appl.Numer.Math.28(1998)1-6.[VIII.2]   
M.P.CalvoAMurua&JManSera,odifiedequationsforODEsContea Mathematics172(1994)63-74.[IX.9]   
M.P.Calvo&J.M.Sanz-Serna,Variablestepsforsymplecticintegrators,In:Numerical Analysis1991(Dundee,1991),3448,PitmanRes.NotesMath.Ser.260,1992.[VIII.1] M.P.Calvo&J.M.Sanz-Serna,Thedevelopmentofvariable-stepsymplecticintegrators,with applicationtothe two-bodyproblem,SIAMJ.Sci.Comput.14(1993)936-952.[V.3], [X.3] M.P.Calvo&J.M.Sanz-Serna,Canonical B-series,Numer.Math.67(1994) 161-175. [VI.7] J.Candy&W.Rozmus,AsymplecticintegrationalgorithmforseparableHamiltonianfunctions,J.Comput.Phys.92(1991)230-256.[I15] B.Cano&A.Duran,Analysisofvariable-stepsizelinearmultistepmethodswith special emphasisonsymmetricones,Math.Comp.72(2003)1769-1801.[XV.7] B.Cano&A.Duran,Atechnique toconstructsymmetricvariable-stepsizelinear multistep methodsforsecond-ordersystems,Math.Comp.72(2003)1803-1816.[XV.7] B.Cano&J.M.Sanz-Serna,Errorgrowthinthenumerical integrationofperiodicorbits bymultistepmethods,withapplicationtoreversiblesstems,IMAJ.Numer.Anal.18 （1998)57-75.[XV.5] R.Car&M.Parrinello,Unifiedapproachformoleculardynamicsanddensity-functional theory,Phys.Rev.Lett.55(1985)2471-2474.[IV.9] JR.Cash,Aclass of implicit Runge-Kuta methodsforthenumerical integrationofstif ordinarydifferentialequations,J.Assoc.Comput.Mach.22(1975) 504-511.[I1.3] A.CayleyOnthetheoryoftheanalyticformscalledtrees,Phil.MagazineXII(1857)172-   
176.[1I1.6] E.Celledoni&A.Iserles,Methods for theapproximation ofthematrixexponential ina Lie-algebraicsetting,IMAJ.Numer.Anal.21(2001) 463-488.[IV.8] R.P.K.Chan,OnsymmetricRunge-Kuttamethodsof high order,Computing45(1990)301-   
309.[VI.10] P.J.Channell&J.C.Scovel,IntegratorsforLie-Poissondynamical systems,Phys.D50 （1991)80-88.[VII.5] P.J.Channell&J.C.Scovel,SymplecticintegrationofHamiltoniansystems,Nonlinearity3 (1990)231-259.[VI.5] S.Chaplygin,Anewcaseofmotionofa heavy rigid bodysupported inonepoint (Russian), MoscovPhys.Sect.10,vol.2（1901）./X.1] P.Chartier,E.Faou&A.Murua,Analgebraicapproachtoinvariantpreservingintegrators:thecaseofquadraticandHamiltonianinvariants,Preprint,Februaryoo5.[Vi.7], [VI.8],[IX.9] M.T.Chu,Matrixdifferentialequations:acontinuous realizationprocessfor linearalgebra problems,NonlinearAnal.18(1992)1125-1146.[IV.3] S.Cirilli,E.Hairer&B.Leimkuhler,AsymptoticerroranalysisoftheadaptiveVerletmethod, BIT39(1999)25-33.[VIIIL.3] A.Clebsch,UeberdiesimultaneIntegration linearerpartiellerDifferentialgleichungen, CrelleJournalf.d.reineu.angew.Math.65(1866)257-268./VI1.3] D.Cohen,Analysisandnumericaltreatmentofhighlyoscillatorydiffrentialequations,DoctoralThesis,Univ.Geneva,2004.[XIIl.10] D.CohenConservationpropertiesofnumericalintegratorsforhighlyoscilatoryHamiltoniansystems,Report,2Oo5.ToappearinIMAJ.Numer.Anal.[XIII.10] D.Cohen,E.Hairer&Ch.Lubich,Modulated Fourierexpansionsof highlyoscillatorydifferentialequations,Found.Comput.Math.3(2003)327-345.[XIII.6] D.Cohen,E.Hairer&Ch.Lubich,Numericalenergyconservationformulti-frequencyoscillatorydifferentialequations,Report,2Oo4.ToappearinBIT.[Xll.9] G.J.Cooper,StabilityofRunge-Kuttamethodsfortrajectoryproblems,IMAJ.Numer. Anal.7(1987)1-13.[IV.2] J.G.vanderCorput,ZurMethodederstationarenPhase,I.Einfache Integrale,Compos.Math.1(1934)15-38.[XIV.4] M.Creutz&A.Gocksch,Higher-order hybridMonteCarloalgorithms,Phys.Rev.Lett.63 (1989)9-12. [II.4]   
P.E.Crouch&R.GrossmanNumericalintegrationofordinarydiffrentialequationson manifolds，J.NonlinearSci.3(1993)1-33.[IV.8]   
M.Crouzeix,SurlaBtabilitedesméthodesdeunge-Kutaumer.Math32(1979)75 82.[VI.4]   
M.Crouzeix&J.Rappaz,OnNumerical Approximationinifurcation Theory,Masson Paris,1989.[XIV.3]   
G.DahlquistConvergenceandstabilityinthenumericalintegrationofordinarydifferential equations,Math.Scand.4(1956)33-53.[XV.1]   
G.Dahlquist,Stabilityanderror boundsinthe numerical integrationofordinarydiferential equations,Trans.oftheRoyalInstofTechn.ockholm,weden,N.30(1959)87pp. [XV.5],[XV.9]   
G.Dahlquist,Erroranalysisforaclassofmethodsforstiffnonlinearinitialvalueproblems, NumericalAnalysis,Dundee1975,LectureNotesinMath.506(1975)60-74.V1.8], [XV.4]   
G.Darboux,SurleproblemedePfaff,extrait BulletindesSciencesmath.etastron.2eserie, vol.VI(1882):Gauthier-Villars,Paris,1882.[VII.3]   
I.Degani&J.SchiffRCMs:RightcorrectionMagnusseriesapproachfor integrationof linearordinarydifferentialequationswithhighlyoscilltorysolution,Report,Weian Inst.Science,Rehovot,20o3.[XIV.1]   
P.Deift,IntegrableHamiltoniansystems,inP.Deift(ed.)etal.Dynamicalsytemsand probabilisticmethodsinpartial differential equations.AMSLect.Appl.Math.31(1996) 103-138.[X.1]   
P.Deift,L.C.Li&C.Tomei,Mairixfactorizationsandintegrablesystems,Comm.Pure Appl.Math.42(1989)443-521.[IV.3]   
P.Deift,L.C.Li&C.Tomei,Symplecticaspectsofsomeeigenvaluealgorithms,inA.S.Fokas &V.E.Zakharov(eds.),ImportantDevelopmentsinSolitonTheory,Springer1993. [IV.3]   
P.DeiftT.Nanda&C.TomeiOrdinarydiferentialequationsandthesymmetriceigenvalue problem,SIAMJ.Numer.Anal.20(1983)1-22.[IV.3]   
P.Deuflhard,A study ofextrapolationmethods based onmultistep schemes without parasitic solutions,Z.angew.Math.Phys.30(1979)177-189.[XIL.i],[XIII.2]   
L.Dieci&T.Eirola,Onsmoothdecompositionsofmatrices,SAMJ.MatrixAnal.Appl.20 (1999)800-819.[IV.9]   
L.Dieci,R.D.ussell&E.S.vanVleckUnitaryintegratorsandapplicationstoontinuou orthonormalization techniques,SIAMJ.Numer.Anal.31(1994)261-281.[IV.9]   
L.Dieci,R.D.Russell&E.S.vanVleck.OnthecomputationofLyapunovexponentsfor continuousdynamicalsystems,SIAMJ.Numer.Anal.34(1997)402-423.[IV.9],[IV.10]   
F.Diele,L.Lopez&R.Peluso,TheCayleytransforminthenumerical solutionofunitary differentialsystems,Adv.Comput.Math.8(1998)317-334.[IV.8]   
F.Diele,L.Lopez&T.PolitiOnestepsemi-explicitmethodsbasedontheCayleytransform forsolvingisospectralfows,J.Comput.Appl.Math.89(1998)219-223.[IV.3]   
P.A.M.Dirac,NoteonexchangephenomenaintheThomastom,Proc.CambridgePhil.Soc. 26(1930)376-385.[IV.9],[VII.6]   
P.A.M.Dirac,GeneralizedHamiltoniandynamics,Can.J.Math.2(1950)129-148.[Vl.7]   
VDruskin&L.Knizhnerman,Krylovsbspaceapproximationofegenpairsandmatix functionsinexactandcomputerarithmetic,Numer.LinearAlgebraAppl.2(1995)205- 217.[XIII.1]   
A.Dullweber,B.Leimkuhler&R.McLachlan,Symplecticsplitingmethodsforrigid body moleculardynamics,J.Chem.Phys.107,No.15(1997)5840-5851.[VI1.4],[V.5]   
W.E,Analysisofteterogenousulisalemetdfodnarydiffenaletions, Comm.Math.Sci.1(2003)423-436./VIII.4]   
A.Edelman,T.A.Arias&S.T.Smith,Thegeometryofalgorithmswithorthogonalityconstraints,SIAMJ.MatrixAnal.Appl.20(1998)303-353.[IV.9]   
B.L.Ehle,OnPadéapproximations totheexponential functionand A-stablemethodsfor the numericalsolutionofinitialvaueproblems,ResearchReportCR2010(969),Dept AACS,Univ.ofWaterloo,Ontario,Canada.[I1.1]   
E.Eich-Soeller&C.Fuhrer,NumericalMethodsinMultibodyDynamics,B.G.Teubner Stuttgart,1998.[IV.4],[VII.1]   
T.Eirola,AspectsofbackwarderroranalysisofnumericalODE's,J.Comp.Appl.Math.45 （1993),65-73.[IX.1]   
T.Eirola&O.NevanlinnaWhatdomultistepmethodsapproximate?Numer.Math.5 (1988)559-569.[XV.2]   
T.Eirola&J.M.Sanz-Serna,Conservationof integralsandsymplecticstructureintheintegrationofdifferentialequationsbymultistepmethods,Numer.Math.61(1992)281-290. XV.4]   
L.H.Eliasson,Absolutely convergent seriesexpansionsfor quasiperiodic motions,Math Phys.Electron.J.2,No.4,Paper4,33p.（1996）.[X.2]   
K.Engg&S.FaltinsenNumerical integrationofLie-Poissonsystemswhilepreserving coadjoint orbitsandenergy,SIAMJ.Numer.Anal.39(2001)128-145.[VII.5]   
B.Engquist&Y.Tsai,Heterogeneousmultiscalemethodsforstiffordinarydiferentialequations,Math.Comp.74(2005)1707-1742.[VIII.4]   
Ch.Engstler&ChLubich,Multirateextrapolationmethodsfordifferentialequations with differenttimescales,Computing58(1997)173-185.[VII1.4]   
L.Euler,Recherchessurlaconnoissancemecaniquedescorps,Histoiredel'AcadRoalede Berlin,AnnéeMDCCLVII,Tom.XIV,p.131-153.OperaOmnia Ser.2,Vol.8,p.178- 199.[VI1.5]   
L.Euler,Dumouvementderotationdescorpssolidesautourd'unaxevariable,Hist.de 1'Acad.RoyaledeBerlin,Tom.14,AnneeMDCCLVII,154–193.OperaOmniaSer.II, Vol.8,200-235.[IV.1]   
L.Euler,Probleme:uncorps étant attire en raison reciproque carreedes distances vers deux pointsfixesdonnes,trouver lescas ou lacourbe decriteparcecorpsseraalgebrique, Memoiresde'AcademiedeBerlin for1760,pub.1767,228-249.X.1]   
L.Euler,TheoriamotuscorporumsolidorumseurigidorumRostochiietGrypiswaldiae A.F.Rose,MDCCLXV.OperaOmniaSer.2.Vol.3-4.[VII.5]   
L.Euler,InstitutionumCalculi Integralis,VolumenPrimum,OperaOmnia,Vol.XI.[1.1]   
E.Faou,E.Hairer&T-L.Pam,Energyconservationwithnon-symplecticmethods:exam plesandcounter-examples,submitted forpublication.[1X.9]   
E.Faou&Ch.Lubich,APoissonintegratorfor Gaussianwavepacketdynamics,Report 2004.ToappearinComp.Vis.Sci.[VI1.4],[VI1.6]   
F.Fasso,ComparisonofsliingagorihmsfortherigidbodyJ.Comput.Phys189（2003) 527-538.[VI1.5]   
K.Feng,OndiferenceshemesandsmplecticgeometryProceedingsofthe5-thInten. Symposiumondiferentialgeometry&differentialequations,August1984，Beijing (1985)42-58.[VI.3]   
K.Feng,Diffencesemesformilanalisandsmplecticometry.omp Math.4（1986)279-289.[VI.5]   
K.Feng,Formalpowerseriesandnumericalalgorithmsfordynamicalsystems.InProceedingsofinterationalcoferenceonsientificcomputation,Hangzhou,China,Eds.Tony Chan&Zhong-CiShi,SeriesonAppl.Math.1(1991)28-35.{IX.1]   
K.Feng,CollectedWorks(I),NationalDefenseIndustryPressBeijing995.[XV.2]   
K.Feng&Z.hang,Volume-preservingalgorithmsforource-freedynamicalsystems,Numer.Math.71(1995)451-463.[IV.3]   
K.Feng,H..Wu,M.-Z.Qin&D.L.WangConstructionofcanonicaldiferencehemes forHamiltonian formalismvia generatingfunctions,J.Comp.Math.7(1989)71-96. [V1.5]   
E.Fermi,J.Pasta&S.Ulam,Studiesofnonlinearproblems,LosAlamosReportNo.LA-1940（1955),laterpublishedinE.Fermi:CollectedPapers(Chicago1965),andLect Appl.Math.15,143(1974).[1.5]   
B.Fiedler&J.heurle,Discetizationofmolinicbitpidforinandinisible chaos,Mem.Amer.Math.Soc.119,no.5701996.[IX.1]   
C.M.Field&FW.Nijhoff,AnoteonmodifiedHamiltoniansfornumericalintegrations admittinganexactinvariant,Nonlinearity16(2003)1673-1683.[IX.11]   
L.N.G.Filon,Onaquadraturefomulafortrigonometricintegralsroc.oyalSoc.Edin burgh49(1928)38-47.[XIV.1]   
H.Flaschka,TheTodalattie.II.Existenceofintegrals,Phys.Rev.B9(1974)1924-1925. [Iv.3]   
J.Ford,TheFermiastaUamproblem:paradoxtursdiscoveryhysicsReports213 (1992)271-310.[1.5]   
E.Forest,Canonicalintegratorsas trackingcodes,AIPConferenceProceedings184(1989) 1106-1136.[II.4]   
E.Forest,Sixth-orderLiegroupintegrators,J.Comput.Physics99(1992)209-213.[V.3]   
E.Forest&R.D.Ruth,Fourth-ordersymplecticintegration,Phys.D43(199)105-117. [11.5]   
J.Frenkel,WaveMechanicsAdvanedGeneralheory,arendonPress,Oxford934 [IV.9],[VII.6]   
L.Galgani,A.Giorgili,A.Martinoli&S.Vanzini,Ontheproblemofenergyequipartition forlargesystemsoftheFermi-Pasta-Ulamtype:analyticalandnumericalestimates, PhysicaD59(1992),334-348.[1.5]   
M.J.GanderAnosiralingintegratorfortheLotkaVolteraequationIVterian4 (1994)21-28.[VII.7]   
B.Garcia-AchlaJne&Ree,timetepetodsfoilla diferentialequations,SIAMJ.Sci.Comput.20(1999)930-963.{VIIl4],[XI.1], [X1II.2],[X1I1.4]   
L.M.Garrido,Generalizedadiabaticinvariance,J.Math.Phys.5(1964)355-362.[XIV.1]   
W.Gautschi,Numericalintegrationofordinarydifferentialequationsbasedontrigonometric polynomials,Numer.Math.3(1961)381-397.[XII.1]   
Z.Ge&JE.MarsdenLie-PoissonHamilton-JacobitheoryandLie-Poissonintegators, Phys.Lett.A133(1988)134139.[VII.5],[IX.9]   
C.W.Gear&D.R.WelsMultiratelinearmultistepmethods，BIT24(1984)484-502. [VIII.4]   
W.Gentzsch&A.Schluter,UbereinEinschritverfahrenmitzyklischerSchrittweitenanderungzurLosungparabolischerDiferentialgleichungen,ZAMM58(1978), T415-T416.[II.4]   
S.Gill,Aprocessfoetepbtepintegaonofdifealeionsintic digitalcomputingmachine,Proc.CambridgePhilos.Soc.47(1951)95-108.[II.1], [VII.5]   
A.Giorgilli&U.Locatelli,Kolmogorovtheoremandclassicalperturbationtheory,Z. Angew.Math.Phys.48(1997)220-261.[X.2]   
B.Gladman,MDuncan&J.CandySymplecticintegratorsfor long-termintegrationsin celestialmechanics,CelestialMechanicsandDynamicalAstronomy52(1991)221-240. [VIII.1]   
D.Goldman&.Japer,Nderopeatorspliinsemesandnonreversiblestems, SIAMJ.Numer.Anal.33（1996)349-367.IIl.3]   
G.H.Golub&C.FVanLontriputationsndedition,oHoisUivss BaltimoreandLondon,1989.[1V.4]   
O.Gonzalez,TimeintegrationanddisreteHamiltoniansstems,J.NonlinearSci6(1996) 449-467.[V.5]   
O.Gonzalez,D.J.Hgham&A..Stuart,Qualitativepropertiesofmodifiedequations.MA J.Numer.Anal.19(1999)169-190.[1X.5]   
O.Gonzalez&J.C.Simo,Onthestabilityofsymplecticandenergy-momentumalgorithms fornonlinear Hamiltoniansystemswithsymmetry,Comput.MethodsAppl.Mech.Eng. 134(1996)197-222.[V.5]   
D.N.Goryachev,Onthemotionofaheavyrigidbodywithanimmobilepointofsupportin thecase $A = B = 4 C$ (Russian),MoscovMath.Collect.21(1899)431-438.1X.1]   
W.B.GraggRepeatedetrapoationtothelimitinthenumericalsolutionofodiarydif ferential equations,Thesis,Univ.ofCalifornia;seealsoAMJ.Numer.Anal.2(1965) 384-403.V.1]   
D.F.Griffiths&J.M.Sanz-Serna,Onthescopeofthemethodofmodifiedequations,AM J.Sci.Stat.Comput.7(1986)994-1008.[IX.1]   
V.Grimm&MHochbruck,Erroranalysisofexponentialintegratorsforoscillatoryscondorderdifferentialequations,Preprint,2o5.[X11.4]   
W.Grobner,DieLiereihenundihreAnwendungenVEBDeutscherVerlagderWiss.,Berlin 1960,2nd ed.1967.[I1.5]   
H.Grubmuller,H.Heler,A.Windemuth&K.Schulten,GeneralizedVerletalgorithmforef ficientmoleculardynamicssimulations with long-rangeinteractions,Mol.Sim.6(1991) 121-142.[VIII.4],[XIII.1]   
A.Guillou&JL.Soulé,La resolutionnumeriquedesproblemes diffrentielsaux conditionsinitialespardesmethodesdecollocation.Rev.Francaise Informat.Recherche Opfationnelle3(1969)Ser.R-3,17-44.[I.1]   
M.Gunther&P.Rentrop,MultirateROWmethodsand latencyof electriccircuits.Appl. Numer.Math.13(1993)83-102.[VIII.4]   
F.Gustavson,OnconstructingformalintegralsofaHamiltoniansystemnearanequilibrium point,Astron.J.71(1966)670-686.[1.3]   
J.Hadamard,url'iteratioetlssoltionmoiquesdeeqtiondiffereniellsull. Soc.Math.France29(1901)224-228.[XI.3]   
W.W.HagerungeKutamethodsinoimalontrolandthetransformedadointstem, Numer.Math.87(2000)247-282.[VI.10]   
E.Hairer,Backwardanalysisofnumerical integratorsandsymplecticmethods,Annalsof NumericalMathematics1(1994)107-132.[VI.7]   
E.Hairer,Variabletimestepintegrationwithsymplecticmethods,Appl.Numer.Math.25 （1997)219-227.[VIII.2]   
E.Hairer,Backwarderoranalysisformultistepmethods,Numer.Math84(1999)199-232. [IX.9],[XV.3]   
E.Hairer,Symmetricprojection methodsfordifferentialequationsonmanifolds,BIT40 (2000)726-734.[V.4]   
EHairer,Geometricintegrationofordinarydiffrentialequationsonmanifolds,BI41 （2001)996-1007.[V.4]   
E.Hairer,GlobalmodifiedHamiltonianforconstrainedsymplecticintegrators,Numer.Math. 95(2003)325-336.[IX.5]   
E.Hairer&M.Hairer,GniCodes-Matlabprograms forgeometricnumerical integration In:Frontiersinumericalanalysis(Durhm,O2),SpringerBerlin,Universitext(2003), 199-240.[VIII.6]   
E.Hairer&P.Leone,Order barriersforsymplecticmulti-value methods.In:Numerical analysis1997,Proc.of the17thDundeeBiennial Conference,June24-27,1997,D.F. Grifiths,D.J.Higham&G.A.Watson(eds.），PitmanResearch NotesinMathematics Series380(1998),133-149.[XV.4],[XV.8]   
E.Hairer&P.Leone,SomepropertiesofsymplecticRunge-Kutamethods,New ZealandJ. ofMath.29(2000)169-175.[IV.2]   
E.Hairer&Ch.Lubich,Thelifespanofbackwarderroranalysisfornumericalintegratos, Numer.Math.76(1997),pp.441-462.Erratum:http://www.unige.ch/math/folks/hairer/ [IX.7],[X.5]   
E.Hairer&Ch.Lubich,Invarianttori ofdissipativelyperturbed Hamiltoniansystemsunder symplecticdiscretization,Appl.Numer.Math.29(1999)57-71.[XI.1],[.5]   
E.Hairer&Ch.Lubich,Asymptoticexpansionsandbackwardanalysisfornumerical integrators,Dymcsogoith(neapolis,997)ol.th.l1 Springer,New York(2000)91-106.[IX.1)   
E.Hairer&Ch.LubichLong-timeenergyonsevationofnumericalmethodsforoilltory differentialequations,SAMJ.Numer.Anal.38(200a)414-441.[XIl.1],[X11I.2], [XIII.5],[XII1.7]   
E.Hairer&Ch.LubichEnergyconservationbyStormer-typenumericalintegrators,in: G.F.Griffiths,G.A.Watson (eds.),Numerical Analysis1999,CRCPressLLC(2000b) 169-190.[XII.8]   
E.Hairer&Ch.Lubich,Symmetric multistepmethodsoverlong times,Numer.Math.97 （2004)699-723.[XV.3],[XV.5],[XV.6]   
E.Hairer,Ch.Lubich&M.Roche,Thenumerical solutionofdifferential-algebraic systems byRunge-Kuttamethods,LectureNotesinMath.1409,Springer-Verlag,1989.[V1.1]   
E.Hairer,ChLubich&GWanner,Geometricnumerical integrationilustrated bythe Stormer-Verletmethod,ActaNumerica(2003)399-450.[1.1]   
E.Hairer,S.P.Norsett&G.Wanner,SolvingOrdinaryDifferential EquationsI.Nonstiff Problems,2ndedition,SpringerSeriesinComputationalMathematics8,pringerBerlin, 1993.[II.1]   
E.Hairer&G.oderlind,Explicit,imereversibledapivestepsizecontrol,ubmidfor publication,2004.[VII.3],[IX.6]   
E.Hairer&DStoffer,Reversiblelong-termintegrationwithvariablestepsizes,AMJ.Sci. Comput.18(1997)257-269.[VIII.3]   
E.Hairer&G.Wanner,Onthe Butchergroupandgeneralmulti-valuemethods,Computing 13（1974)1-15.[III.1]   
E.Hairer&GWannerSolvingOrdinaryDierentialEquationsI.StiffandDiffrential AlgebraicProblems,2ndedition,SpringerSeriesinComputational Mathematics14 Springer-VerlagBerlin1996.[I.1],[I.O],[IV.2],[IV.4],[IV.5],[IV.9],[V10],[.4] [VI.10].[VII.1]VI.][X.5][.][V4[9]   
E.Hairer&GWannerAnalysisbyItsHstory2ndprinting,UndergraduateTextsinthematics,Springer-VerlagNewYork,997.[X.7]   
M.Hall,jr,AbasisforfreeLieringsandhighercommutatorsinfreegroups,Proc.Amer Math.Soc.1(1950)575-581.[III.3]   
SirW.R.Hamilton,Onageneralmethodindynamics;bywhich thestudyofthemotionsofall freesystems ofattractingorrepellingpointsisreducedtothesearchanddifferentiation ofonecentralrelation,orcharacteristicfunction,Phil.Trans.Roy.Soc.PartIIfor834 247-308；ath.Papers,Vol.II3-161.[V.1],[V5]   
P.C.Hammer&JWHollingsworthTrapezoidalmethodsofapproximatingolutionsofdif ferential equations,MTAC9(1955) 92-96.[II.1]   
E.J.Haug,ComputeridedKinematicsandDynamicsofMechanicalSytemsVoume: BasicMethods,Allyn&Bacon,Boston,1989.[VI.5]   
FHausdorff,DiesymbolischeExponentialformelinderGruppentheorie,Berichteder SachsischenAkad.derWissensch.58(1906)19-48.[II1.4]   
A.Hayli,Leproblemedes $N$ corpsdansunchamp exterieurapplication a l'évolution dynamiquedesamas ouverts-1,BulletinAstronomique2(1967) 67-89.[Vl.4]   
R.B.Hayward,OnaDirectMethodofetimatingVelocitiesAccelerations,andallsimilar QuantitieswithespecttoAesmoveablennySpacewithApplicationCaidge Phil.Trans.vol.X(read1856,publ.1864)1-20.[VII.5]   
E.J.Hellerimeependentaproachtomiclassicaldyamics,J.Chem.Phys.62(1975) 1544-1555.[VII.6]   
E.J.HellerTimedependentvriationalapprochtomiclassicaldynamics,J.Chmys. 64(1976)63-73.[VII.6]   
M.Henon&C.Heiles,Theapplicabilityofthethirdintegralofmotion:somenumerical experiments,Astron.J.69(1964)73-79.[1.3]   
J.Henrard,heiticintinicalicsmicoted,ees. Vol.2,Springer,Berlin(1993)117-235.[XIV.1]   
P.HenriciiscreteVariableethodsinOrdinaryiffrentialEquationJohnWiley& Sons,Inc.,New York1962.[VI/.5]   
J.Hersch,Contributiona lamethodeauxdiffrences,Z.angew.Math.Phys.9a(1958)129- 180.[XIII.1]   
K.Heun,NeueMethodezurapproximativenIntegrationderDiferentialgleichungeneiner unabhangigen Veranderlichen,Zeitschr.furMath.u.Phys.45(1900)23-38.[.1]   
D.J.Higham,Tme-stepinandpreevingothogonality,37(1997)2436.[V.9]   
N.J.Higham,TheaccuracyoffloatingpointsummationAMJ.SciComut.14（1993) 783-799.[VII1.5]   
M.Hochbruck&Ch.Lubich,OnKrylovsubspaceapproximationstothematrixexponential operator,SIAMJ.Numer.Anal.34(1997)1911-1925.[XIII.1]   
M.Hochbruck&Ch.Lubich,AGautschi-typemethodforoscillatorysecond-orderdiferentialequations,Numer.Math.83(1999a)403-426.[VIII.4],[XIII.1],[XII.2],[XIII.4]   
M.Hochruck&Ch.Lubich,Exponentialintegratorsforquantum-classicalmoleculardynamics,BIT39(1999b)620-645.[VII.4],[XIV.1],XV.4]   
THolder,B.Leimkuhler&SReich,Explicitvariablestep-sizeandtime-reversibleintegration,Appl.Numer.Math.39(2001)367-377.[VIII.3]   
H.Hopf,UberdieTopologiederGruppen-MannigfaltigkeitenundihreVerallgemeinerungen Ann.ofMath.42(1941)22-52.III.1]   
W.Huan&B.Leimkuher,headaptiveVerletmethodAJ.SciComput.18(1997) 239-256.[VIII.2],[VII.3]   
P.Hut,J.Makino&S.McMilln,Buildingabeteleapfrog,Astrophys.J.443(1995)9 L96.[VIII.3]   
K.J.In'tHout,Anew interpolationprocedureforadaptingRunge-Kuttamethodstodelay differential equations,BIT32(1992) 634-649.[VIII.6]   
A.Iserles,SolvinglinearodinarydiffrentialequationsbyexponentalsofiteratedmmutatorsNumer.Math.45（1984)183-199.[11.4]   
A.IserlesOntheglobalerorofdiscretizaionmedsforighloilatorydinarydif. ferential equations,BIT42(2002)561-599.[XIV.1]   
A.IserlesOnhemethodofeumannseriesforhighlyoscillatoryequations,I44（2004) 473-488.[XIV.1]   
A.Iserles,H.Z.Munthe-Kaas,S.P.Nrset&A.Zanna,Lie-groupmethods,ActaNumerica (2000)215-365.[IV.8]   
A.Iserles&S.P.NrsettOnthesolutionoflineardifferentialequationsinLiegroups,R. Soc.Lond.Philos.Trans.Ser.AMath.Phys.Eng.Sci.357(199)983-1019.(IV.7], [IV.10]   
A.Iserles&S.P.Norsett,Onthenumerical quadratureof highly-oscillatingintegralsl: Fourier transforms,IMAJ.Numer.Anal.24(2004)365-39i.[XIV.1]   
T.Itoh&K.Abe,Hamiltonian-conservingdiscretecanonicalequations basedonvariational differencequotients,J.Comput.Phys.76(1988)85-102.[V.5]   
J.A.Izaguirre,S.Reich&R.D.elLongertimestepsformoleculardynamicsJ.Cem. Phys.110（1999)9853-9864.[X1I.1],[XIV.4]   
C.G.J.JacobiUberdejenigenrobemederechaniknwecheneineraftefucioneistirtundiberdieTheoriederStorungen,manuseriptfrom836or837,published posthumelyinWerke,vol.5,217-395.[V1.2] C.G.J.JacobUbedieReduktionderntegationderrtiellenDifentalgeicungener sterOrdnungzwischenirgendeinerZahl Variablenaufdie Integration eines einzigen Systemes gewohnlicherDifferentialgleichungen,CrelleJournalf.d.reineu.angew.Math   
17（1837)97-162；K.Weierstrassed.,C.G.J.Jacobi'sGesammelteWerke,vol.4,pp.   
57-127.[VI.5] C.G.J.Jacobi,LettreadresseeaM.lePreésidentdel'AcademiedesSciences,LiouvilleJ. math.puresetappl.5（1840)350-355:Werke,vol.5,pp.3-189.[IV.1] C.G.J.Jacobi,VorlesungenuberDynamik(1842-43),Reimer,Berlin1884.[VI.1],[V1.5], [VI.6],[VI.10] C.G.J.Jacobi,Nova methodusaequationesdifferentialespartialesprimiordini inter numerumvariabiliumquemcunquepropositasintegrandi,publishedposthumlyinCrelle Journalf.d.reineu.angew.Math.60(1861)1-181;Werke,vol.5,pp.3-189.[II.5], [VII.2],[VII.3] T.Jahnke,NumerischeVerfahrenfurfastadabatischeQuantendynamik,DoctoralThesis, Univ.Tubingen,2003.[XIV.3] T.Jahnke,Long-time-stepintegratorsforlmost-adiabaticquantumdynamicsAMJ.Sci. Comput.25(2004a)2145-2164.[XIV.1] T.Jahnke,Along-time-step method for quantum-classical molecular dynamics,Report,   
2004b.[XIV.3] TJahnke&Ch.Lubich,Numerical integratorsforquantumdynamicsclosetotheadiabatic limit,Numer.Math.94(2003).289-314.XIV.1] L.Jay,Colloconmethodsfordifretial-lgebiceqaionsfindex3,umer.ath65 （1993)407-421.[VII.1] LJayRungueofoeetebci plications toHmiltonanssemsesisNo2658,994,UnivGeneve.] L.Jay,SymplecticpartitionedRunge-KutamethodsforconstrainedHamiltoniansystems, SIAMJ.Numer.Anal.33(1996)368-387.[II.2],[VII.1] L.Jay,SpecializedRunge-Kutamethodsforindex2diffrentialalgebraicequations,Math. Comp.(2005）,toappear.[IV.9] R.Jost,Winkel-undWirkungsvariablefurallemeinemechanischeSysteme,HelvPhys.Acta   
41(1968)965-968.[X.1] A.Joye&C.-E.Pfister,Superadiabaticevolutionandadiabatictransitionprobability betweentwonondegeneratelevelsisolatedinthespectrum,J.Math.Phys.34(1993)454   
479.[XIV.1] W.Kahan,Furtherremarksonreducing truncationerrors,Comm.ACM8(1965)40. [VIII.5] W.Kahan&R.-C.LiCompositionconstantsforraisingtheordersofunconventional schemesforordinarydiferentialequations,Math.Comput.66(1997)i089-1099.[V3], [V.6] B.KarasozenPoissonintegratorsath.Comp.odelling40(2004)1225-244[VIl.4] TKato,urbionrorirosegerrlin8[l.] J.Kepler,Astronomia novaooyn6seu Physica celestis,traditiacommentariis de motibusstellaeMartis,exobservationibusG.V.TychonisBrahe,Prague16o9.[I.2] H.Kinoshita,H.Yoshida&H.Nakai,Symplecticintegratorsandtheirapplicationtodynam ical astronomy,Celest.Mech.&Dynam.Astr.50(1991)59-71.[V.3] U.Kirchgraber,Multi-stepmethodsareessentially one-stepmethods,Numer.Math.48 （1986)85-90.[XV.2] U.Kirchgraber,F.LasagniK.Nipp&D.Stofer,Qntheapplicationofinvariantmanifold theory,inprticulartonumericalnalysis,nternat.er.umer.ath97irkhuer Basel,1991,189-197.[XII.3] U.Kirchgraber&E.tiefel,MethodenderanalytischenStorungsrechnungundihreAwendungen,Teubner,Suttgart,978.[X1.4]   
F.Klein,ElementarmathematikvomhoherenStandpunkteaus.TeilI:Arithmetik,Algebra,Analysis,usgearbeitetvonE.HellingerTubner,Leipig,9o8；Vierteuage DieGrundlehrenetematischenWiseshatenand4prngerVerlagin 1933,reprinted1968.[VI.5]   
FKlein&A.ommerfeld,TheoriedesKreisels,Leipig897.[Vl.5]   
O.Koch&h.ich,ymicllowkroimion,reprint.[V.9]   
A.N.Kolmogorov,Onconservationofconditionallyperiodicmotionsunder smallpturbationsoftheHamiltonian,Dokl.Akad.NaukSSSR98(1954)527-530.[X.2],[X.5]   
A.N.KolmogorovGeneral theory ofdynamicalsystemsandclassical mechanics,Proc.Int. Congr.Math.Amsterdam1954,Vol.1,315-333.[X.2],[X.5]   
P.V.Koselef,iverchofectinegtringtereb tionalgorithmsandclassicalmechanics,FieldsInst.Commun.10(1996)103-120.[V.3]   
S.Kovalevskaya(Kowalevski),Sur leproblemedelarotationd'uncorps solideautourd'un point fixe,ActaMath.12(1889)177-232.[X.1]   
V.V.KozlovtegrabilityndnoninegrabilityinHamilonanmechanicsUspekhi t. Nauk 38(1983)3-67.[X.1]   
D.KreimerOntheHopflgebrastructureofperturbativequantumfieldtheory,Adv.eor. Math.Phys.2(1998)303-334.[III.1]   
N.M.Krylov&N.N.Bogoliubov,Applicationdesmethodesdelamecaniquenon lineairea latheoriedesoscillationsstationnaires,Editiondel'AcademiedesSciencesdelaR.S.S. dUkraine,1934.[X1.4]   
W.Kutta,BeitragzurnaherungsweisenIntegrationtotalerDifferentialgleichungen,Zeitschr. furMath.u.Phys.46(1901)435-453.[II.1]   
R.A.LaBudde&D.Greenspan,iscretemechanics-generaltreatment,J.Comut.hys. 15(1974)134-167.[V.5]   
R.A.LaBudde&D.Greenspan,Energyand momentumconservingmethodsofarbitrary orderfor thenumericalintegrationofequations ofmotion.PartsIandI,Numer.Math. 25(1976)323-346and26(1976)1-26.[V.5]   
M.P.Laburta,StartingalgorithmsforIRKmethods,J.Comput.Appl.Math.83(1997)269- 288.[VIII.6]   
M.P.Laburta,ConstructionofstartingalgorithmsfortheRK-Gaussmethods,J.Comput. Appl.Math.90(1998)239-261.[VIII.6]   
J.-L.Lagrange,Applicationsdelamethodeexposéedans lememoireprecedentalasolution dedifferentsproblemesdedynamique,1760,OeuvresVol.1,365-468.[VI.1],[VI.2]   
J.L.Lagrange,Recherches surlemouvementd'uncorpsquiestattireversdeuxcentresfixes （1766),(Euvres,tomeII,Gauthier-Villars,Paris868,67-124.[X.1]   
J.-L.Lagrange,Mecaniqueanalytique,Paris1788.[Vl.1]   
J.D.Lambert&I.A.Watson,Symmetricmultistepmethodsforperiodicinitialvalueproblems,J.Inst.Maths.Applics.18(1976)189-202.[XV.1],[XV.9]   
C.LanczosTheVariationalPrinciplesofMechanicsUniversityofTorontoress,oront 1949.(Fourth edition1970).[VI.6]   
P.S.Laplace,Traite demecaniquecelesteIl,1799,seeEuvresI,p.183.[1.6]   
F.M.Lasagni,CanonicalRunge-Kuttamethods,ZAMP39(1988) 952-953.[VI.4],[VI.5], [VI.7]   
J.D.LawsonGeneralizedRunge-KuttaprocessesforstablesystemswithlargeLipschitzconstants,SIAMJ.Numer.Anal.4(1967)372-380.[XIV.1]   
P.D.Lax,Integralsofnonlinearequationsofevolutionandsolitarywaves,Commun.ure Appl.Math.21(1968)467-490.[IV.3]   
B.Leimkuhler&S.Reich,SymplecticintegrationofconstrainedHamiltoniansystems,Math. Comp,63(1994)589-605.[VII.1]   
B.Leimkuhler&S.Reich,Areversibleaveragingintegratorformultipletime-scaledynamics,J.Comput.Phys.171(2001)95-114.[VII1.4] D.Lmmnuui &S.nuinn,ounuung IumuuununDynumues,Camuiuge ivunugiapus Un AppliedandComputational Mathematics14,CambridgeUniversityPress,Cambridge   
2004.[VI.3] B.J.Leimkuhler&R.D.Skeel.Symplecticnumerical integrators inconstrained Hamiltonian systems,J.Comput.Phys.112(1994)117-125.[VI.1] A.Lenard,Adiabaticinvariancetoallorders,AnnPhys.6(1959)261-276.[XV.1] P.Leone,Symplecticityand SymmetryofGeneral Integration Methods,These,Sectionde Mathematiques,UniversitedeGeneve,20oo.[VI.8] T.Levi-CivitaSurlaesolutionqualitativeduproblemerestreintdestroiscorps,ActaMath   
30(1906)305-327.[VIII.2] T.Levi-Civita,Surlaregularisationduproblemedes troiscorps,Acta Math.42(1920)99-   
144.[VIII.2] D.Lewis&J.C.SimoConservingalgorithmsforthedynamicsofHamiltoniansystemson Liegroups,J.NonlinearSci.4（1994)253-299.[IV.8],[V.5] D.Lewis&J.C.Simo.ConservingalgorihmsfortheN-dimensionalrigidbody,FieldsInst. Com.10(1996)121-139.[V.5] S.Lie,ZuriederognstorAar88,r.6es Christiania1888;GesammelteAbh.vol.5,p.553-557.[VII.2],[VIl.3] J.Liouville,Noteal'occasiondumemoireprecedent(deM.E.Bour),J.Math.Pureset Appliquees20(1855)201-202.[X.1] L.Lopez&T.Politi,ApplicationsofiheCayleyapproach inthenumericalsolutionofmatrix diferentialsystemsonquadraticgroupsAppl.Numer.Math.36(20o1)35-55.[V.8] M.A.L6pez-Marcos,J.M.Sanz-Serna&R.D.Skeel,Cheapenhancementofsymplecticintegrators,Numericalanalysis1995Dundee),itmanRes.NotesMath.Ser.344Long man,Harlow,1996,107-122.[V.3) K.Lorenz,T.Jahnke&Ch.LubichAdiabaticintegratorsforhighlyoscilatorysecondorder lineardiferentialequationswithtime-varyingeigendecomposition,BI45(2005)91-   
115.[XIV.1].[XIV.2] A.J.Lotka,TheElementsofPhysical Biology，Williams&Wilkins,Baltimore,1925. Reprinted1956underthetitleElementsofmathematical biologybyDover,New York.[.1] Ch.LubichIntegrationofstiffmechanicalsystemsbyRunge-Kuttamethods,Z.Angew. Math.Phys.44(1993)1022-1053./XIV.3] Ch.Lubich,Ondynamicsand bifurcationsofnonlinear evolutionequationsunder numericaldiscretization,inErgodicTheory,Analysis,and Efficient SimulationofDynamical Systems(B.Fiedler,ed.),Springer,Berlin,2001,469-500.{XII.3] Ch.Lubich,Avariationalsplitingintegratorforquantummoleculardynamics,Appl.Numer. Math.48(2004)355-368.[VII.4] Ch.LubichOnialproimtioinummeclraic,th   
74(2005)765-779.[VII.6] R.MacKay,Someaspects ofthedynamicsofHamiltoniansystems,in:D.S.Broomhead& A.Iserles,eds.,TheDynamicsofNumericsandtheNumericsofDynamics,Clarendon Press,Oxford,1992,137-193.[V1.6] S.Maeda,Canonical structureand symmetriesfor discretesystems,Math.Japonica25 (1980)405-420.[VI.6] S.Maeda,Lagrangianformulationofdiscretesstemsandconceptofdifferencespaceath. Japonica 27(1982)345-356.[VI.6] W.MagnusOntheexponentialsolutionofdiffrentialequationsforalinearopeator Comm.PureAppl.Math.VII(1954)649-673.[IV.7] G.Marchuk,Someapplicationsofspliting-upmethodstothesolutionofmahematical physicsproblems,AplikaceMatematiky13(1968)103-132.[I1.5] J.E.Marsden,S.Pekarsky&S.ShkollerDiscreteEuler-PoincareandLie-Poissonequations, Nonlinearity12（1999)1647-1662.[VII.5]   
J.E.Marsden&T.S.Ratiu,Introductionto Mechanicsand Symmetry.A Basic Exposition ofClassicalMechanical Systems,Secondedition,TextsinAppliedMathematics17, Springer-Verlag,NewYork,1999.[IV.1]   
J.E.Marsden&MWest,Discretemechanicsandvariationalintegrators,ActaNumerica10 (2001)1-158.[VI.6]   
A.D.McLachlan,Avariationalsolutionofthetime-dependentSchrodingerequationol. Phys.8(1964)39-44.[VII.6]   
R.I.McLachlanExplicitLie-PossonintegrationandtheEulerequations,Phys.vett. 71(1993)3043-3046.[VII.4],[VII.5]   
R.I.McLachan,Onthenumericalintegrationofodinarydifferentialequationsbysmeic compositionmethods,SIAMJ.Sci.Comput.16(1995)151-168.[I1.4],[I.5],[I.3], [V.3],[V.6]   
R.I.McLachlan,Compositionmethodsinthepresenceofsmallprameters,B35(1995b) 258-268./V.3]   
R1.McLaclnorelectictegraointegaogidl Mechanics10,J.E.Marsden,G.W.Patrick&W.F.hadwick,eds.，Amer.Mathoc.. Providence,R.I.(1996)141-149.[V.3]   
R.I.McLachlan,FeaturedreviewofGeometricNumericalIntegrationbyE.HairerC.Lubich,andG.Wanner,SIAMReview45(2003)817-821.[VII.5]   
R.I.McLachlan&P.Atela,Theaccuracyofsymplecticintegrators,Nonlinearity5(1992) 541-562.[V.3]   
R.I.McLachlan&G.R.W.Quispel,Splitingmethods,Acta Numerica11(20o2)341-434. [VII.4]   
R.IMcLaclasel&oerictegtiinge dients,Philos.Trans.R.Soc.Lond.,Ser.A,357(1999)1021-1045.[V.5]   
R.I.McLachlan&Covel,qivintstrinedsmlecticinegraionJ. Sci.5(1995)233-256.[VII.5]   
R.I.McLachlan&A.ZannaThediscreteMoserVeselovalgorithmforthefreerigidbody revisited,Found.Comput.ath.5(2005)87-123.[V.5],[I.1]   
R.J.Y.McLeod&J.n-SernaGeomtricallydeiveddiffrencefomulaefortenumer icalintegrationoftrajectoryproblems,IAJ.umer.Anal.2(1982)35737.[Il.2]   
V.L.Mehrmann,TheAutonomousLinearQuadraticControlProblem.TheoryandNumerical Solution,LectureNotesinControlandInformationSciences,Springer-Verlag,erlin 1991.[IV.9]   
R.H.MersonAnoperational methodforthesudyofintegrationprocesses,Proc.Symp DataProcessing,WeaponsResearchEstablisment,SaisburyAustralia(957)1to 110-25.[II.1]   
A.MessiahQuantumMechanicsDoverPubl1999(reprintofthetwo-volumeeditionpublishedbyWiley,1961-1962).[VII.6]   
S.Miesbach&H.J.eschmpecticasefowpproimationfortenmericaltegra tionofcanonicalsystems,Numer.Math.61(1992)501-521.[VL.5]   
P.C.MoanOnigorousmodifiduationsfordisetizationsofDEseport,0o..7]   
O.MgllerQuasidouble-precisioninfoatingpointaddition,BIT5(1965)37-50and251- 255.[VII.5]   
A.Morbidelli&A.Giorgilli,SuperexponentialstabilityofKAMToriJ.Stat.Phys.78(1995) 1607-1617.[X.2]   
J.Moser,ReviewMR20-4066,Math.Rev.,1959.[X.5]   
J.Moser,Oninvariantcurvesofarea-preservingmappingsofanannulus,Nachr.Akad.Wiss Gottingen,II.ath.-Phys.Kl.1962,1-20.[X.5]   
J.Moser,LecturesonHamiltoniansystems,Mem.Am.Math.Soc.81(1968)1-60.[IX.3]   
J.Moser,tableandRandomotionsinDynamicalSystemsAnnalsofMathematicstudies.No.77.Princeton UniversityPress,1973.[X1.2] 一anintegrable system,Dyn.Syst.，Theor.Appl.,Battelle Seattle 1974Renc.,Lect. NotesPhys.38(1975)467-497.[X.1]   
J.Moser,Isthe solarsystemstable?,Mathematical Intelligencer1(1978)65-71.[X.0]   
I.Moser&A.P.Veselov,Discreteversionsofsome classical integrable systemsandfactorizationofmatrixpolynomials,Commun.Math.Phys.139(1991) 217-243.[VI1.5]   
H.Munthe-Kaas,Lie Butcher theoryfor Runge-Kuta methods,BIT35(1995)572-587. [IV.8]   
H.Munthe-Kaas,Runge-Kutta methodsonLiegroups,BIT38(1998)92-11.[IV.8]   
H.Munthe-Kaas,High orderRunge-Kuttamethodsonmanifolds,J.Appl.Num.Maths.29 (1999)115-127.[IV.8]   
H.Munthe-Kaas&B.Owren,ComputationsinafreeLiealgebra,Phil.Trans.Royal Soc.A 357(1999)957-981.IV.7]   
A.Murua.Metodos simplecticos desarrollablesen $P$ -series,Doctoral Thesis,Univ.Valladolid,1994.[IX.3]   
A.Murua,Onorder conditionsforpartitionedsymplectic methods,SIAMJ.Numer.Anal. 34(1997)2204-2211.[IX.11]   
A.Murua,Formalseriesandnumerical integrators,Part I:Systems ofODEsandsymplectic integrators,Appl.Numer.Math.29（1999)221-251.[IX.11]   
A.Murua&J.M.Sanz-Serna,Order conditionsfor numerical integratorsobtained bycomposingsimpler integrators,Philos.Trans.Royal Soc.London,ser.A357(1999)1079- 1100.[I.],[.3],[V.3]   
A.I.Neishtadt,The separation of motions insystemswith rapidly rotatingphase,J.Appl. Math.Mech.48(1984)133-139.[X/V.2]   
N.N.Nekhoroshev,Anexponential estimateof the time of stability of nearly-integrable Hamiltoniansystems,Russ.Math.Surveys32(1977)1-65.[X.2],[X.4]   
N.N.Nekhoroshev,Anexponentialestimateofthe timeof stability of nearly-integrable Hamiltoniansystems.II.(Russian),Tr.Semin.Im.I.G.Petrovskogo5(1979)5-50.[X.4]   
G.Nenciu,Linearadiabatic theory.Exponentialestimates,Commun.Math.Phys.152(1993) 479-496.[XIV.1]   
P.Nettesheim & S.Reich,Symplectic multiple-time-stepping integrators forquantumclassical moleculardynamics,inP.Deuflhard etal.(eds.),Computational Molecular Dynamics:Challenges,Methods,Ideas,Springer,Berlin1999,412-420.[VII.4]   
I.Newton,Philosophiae Naturalis Principia Mathematica,Londini anno MDCLXXXVII, 1687.[I.2],[VI.1],[X.1]   
I.Newton,SecondeditionofthePrincipia,1713.[1.2],[X.1]   
K.Nipp&D.Stoffer,Attractive invariant manifoldsfor maps:existencesmoothnessand continuousdependenceonthe map,Research ReportNo.92-11,SAM,ETH Zurich, 1992.[X1I.3]   
K.Nipp&D.Stoffer,Invariantmanifoldsandglobalerrorestimatesofnumericalintegration schemesapplied to stiffsystems of singular perturbationtype.I:RK-methods,Numer. Math.70(1995)245-257.[XII.3]   
K.Nipp&DStoerInvariantmanifoldsandglobalerroresimatesofnumericalintegrationschemes appliedtostiffsystems of singularperturbation type.II:Linear multistep methods,Numer.Math.74(1996)305-323.[XIi.3]   
E.NoetherInvariante Variationsprobleme,achr.Aad.Wiss.Gottingen,Math.s.K. (1918)235-257.[VI.6]   
E.J.Nystrom,Ueberdienumerische Integration vonDifferentialgleichungen,Acta Soc.Sci. Fenn.50(1925)1-54.[I.2]   
E.Oja,Neuralnetworks,principalomponentsandsubspaces,Int.J.NeuralSyst.1(989) 61-68.[IV.9]   
D.Okunbor&R.D.Skeel,Explicit canonical methodsfor Hamiltoniansystems,Math. Comp.59(1992)439-455.[VI.4]   
D.I.Okunbor&R.Dkel,CanonicalRunge-Kutta-Nystrommethodsofordersfiveand six,J.Comp.Appl.Math.51(1994)375-382.[V.3]   
F.W.J.Olver,Asymptoticsand Special Functions,Academic Press,1974.[XIV.4]   
P.J.Olver,ApplicationsofLieGroupstoDiferential Equation,Graduate TextsinMathematics107,Springer-Verlag,NewYork,1986./1V.6]   
B.Owren&A.Marthinsen,Runge-Kutta methodsadapted tomanifoldsand basedonrigid frames,BIT39(1999)116-142.[IV.8]   
B.Owren&A.Marthinsen,Integrationmethodsbasedoncanonicalcoordinatesofthesecondkind,Numer.Math87(2001)763-790[V.8]   
A.M.Perelomov,Selected topicsonclassical integrablesystemsTroisiemecycledela physique,expandedversionof lecturesdeliveredinMay1995.V.2]   
OPerronUberStabilitat undasymptotisches VerhaltenderLosungeneinesSystems endlicherDiffrenzengleichungen,J.ReineAngew.Math.161(1929)41-64.[Xil.3]   
A.D.Perry&S.WigginsKAMtoriarevery sticky:Rigorous lowerboundsontheimeto moveawayfromaninvariant Lagrangian toruswith linearflow,PhysicaD71(1994) 102-121.[X.2]   
H.Poincare,LesMethodesNouvelesdelaMecaniqueCeleste,TomeI,Gauthier-Villars, Paris,1892.[VI.1],[X.1].[X.2]   
H.Poincare,LesMethodesNouvellesdelaMecaniqueCeleste,TomeIl,GauthierVills, Paris,1893.[VL1],[X.2]   
H.Poincare.LesMethodesNouvellsdelaMecaniqueCelesteTomeIIl,Gauthiers-Villrs, Paris,1899.[VI.1],[VI.2]   
L.Poinsot,Theorienouvelledelarotationdescorps,Paris834.[V.5]   
S.D.Poisson,Surla variationdesconstantesarbitrairesdans lesquestionsdemecanique,J. del'EcolePolytechniquevol.8,15ecahier(1809)266-344.[VI.2]   
B.vander Pol,Forcedoscillationsinasystemwithnon-linear resistance,Phil.Mag.3, (1927),65-80;Papersvol.I,361-376.[XI1.4]   
J.Poschel,Nekhoroshevestimatesforquasi-convexHamiltoniansystems,MathZ.213 (1993)187-216./X.2]   
FA.Potra&W.C.Rheinboldt,Onthenumerical solutionof Euler-Lagrangeequations, Mech.Struct.&Mech.19(1991)1-18.//V.5]   
M.-Z.Qin&W-J.ZhuVlume-preservingsemesndnmericaleprimentsomut Math.Appl.26(1993)33-42.VI.9]   
G.D.QuinlanResoancesandisabiliesinsmmetriculistepmedsert999, available on http://xx.lanl.gov/abs/astro-ph/9901136[XV.7]   
G.D.Quinlan&S.Tremaine,Symmetricmultistepmethodsforthenumerical integrationof planetaryorbits,Astron.J.100(1990)1694-1700.[XV.1],[XV.7]   
G.R.W.Quispel,Volume-preservingintegratorsPhysLett.A206(1995)260.[V.9]   
S.Reich,Symplectic integrationofconstrained Hamiltoniansystems byRunge-Kuttamethods,Techn.Report93-13(1993),Dept.Comput.Sci.,Univ.ofBritish Columbia.[VI1.1]   
S.Reich,Numerical integrationof thegeneralized Euler equations,Techn.Report93-20 (1993).Dept.Comput.Sci.,Univ.of British Columbia.{VI1.4]   
S.Reich,Momentumconservingsymplecticintegrators,Phys.D76(1994)375-383.[VI1.5]   
S.Reich,Symplectic integration ofconstrained Hamiltonian systems by compositionmethods,SIAMJ.Numer.Anal.33(1996a)475-491.[VII1].[IX.5]   
S.Reich,Encingeergyoseingmehods,6(1996b)122134.[V.5]   
S.Reich,Backwarderroranalysis for numerical integrators,SIAMJ.Numer.Anal.36 （1999)1549-1570.[VII.2],[IX.5],[IX.7]   
J.R.Rice,Split Runge-Kuttamethodfor simultaneous equations,J.Res.Nat.Bur.Standards 64B(1960)151-170.[VIII.4]   
H.Rubin&P.Ungar,Motionunderastrongconstrainingforce,Comm.PureAppl.Math. 10(1957)65-87.[XIV.3]   
C.Runge,UeberdienumerischeAuflosung vonDiffrentialgleichungen,Math.Ann.46 (1895)167-178.[II.1]   
H.Russmann,Onoptimalestimatesforthesolutionsoflinearpartialdifferentialequations offrstorderwithconstantcoefcientsonthetorus,Dyn.Syst.,Theor.Appl.,Battelle Seattle1974Renc.,Lect.NotesPhys.38(1975)598-624.[X.4]   
H.Russmann,Onoptimalestimatesforthesolutionsoflineardiffrenceequations onthe circle,Celest.Mech.14(1976)33-37.[X.4]   
R.D.Ruth,Acanonical integration technique,IEEE Trans.Nuclear Science NS-30(1983) 2669-2671.[II.5],[VI1],[VI.3],[IX.1]   
J.-P.Ryckaert,G.Ciccoti&H.J.C.Berendsen,Numerical integrationofthecartesianequationsofmotionofasystemwithconstraints:moleculardynamics ofn-alkanes,J.Comput.Phys.23(1977)327-341.[VII.1],[XIII.1]   
P.Saha&S.Tremaine,Symplectic integratorsforsolarsystemdynamicsAstron.J.104 (1992)1633-1640.[V.3]   
S.Saito,H.Sugiura&T.MitsuiButcher'ssimplifingassumptionforsymplecticintegrators, BIT32(1992)345-349.[IV.10]   
J.Sand,Methodsforstartingiterationschemesforimplicit Runge-Kuttaformulae,Computationalordinarydifferential equations(London,989),Inst.Math.Appl.Conf.Ser.New Ser.,39,OxfordUniv.Press,NewYork,1992,115-126.[VII.6]   
J.M.Sanz-Serna,Runge-Kutta schemesforHamiltoniansystems,BIT28(1988)877-883. [VI.4]   
J.M.Sanz-Serna,SymplecticintegratorsforHamiltonianproblems:anoverview,Acta Numerica1（1992)243-286.[IX.1]   
J.M.Sanz-Serna,AnunconventionalsymplecticintegratorofW.Kahan,Appl.Numer.Math 16(1994)245-250.[VII.4]   
J.M.Sanz-Serna&L.Abia,Orderconditionsforcanonical Runge-Kuttaschemes,SIAMJ. Numer.Anal.28(1991)1081-1096.[IV.10]   
J.M.Sanz-Serna&M.P.Calvo,Numerical HamiltonianProblems,Chapman&HallLondon,1994.[VI.3]I.6]   
R.Scherer.A noteonRadauandLobattoformulaeforO.D.E:s,BIT17(1977)235-238. [11.3]   
T.Schlick,Somefailuresandsuccessesoflong-timestepapproaches tobiomolecularsimulations,inComputationalMolecularDynamics:Challenges,Methods,Ideas(P.Deufhard etal.,eds.）,Springer,Berlin1999,227-262.[XI.1]   
M.B.Sevryuk,Reversiblesystems,LectureNotesinMathematics,1211.Springer-Verlag, 1986.[XI.0]   
L.F.Shampine,ConservationlawsandthenumericalsolutionofODEs,Comp.Maths.Appls. 12B(1986)1287-1296.[IV.1]   
Z.Shang,Generatingfunctionsforvolume-preservingmappingsand Hamilton-Jacobiequationsforsource-freedynamicalsystems,Sci.ChinaSer.A37(1994a)1172-1188.[VI.9]   
Z.Shang,Constructionofvolume-preservingdifferenceschemesforsource-freesystems via generatingfunctions,J.Comput.Math.12(1994b)265-272.[VI.9]   
Z.Shang,KAMtheoemofsymplecticalgorithmsforHamiltoianstems,Numer.ath83 （1999)477-496.[X.6]   
Z.Shang,Resonantand Diophantinestepsizesincomputinginvariant tori of Hamiltonian systems,Nonlinearity13(2000)299-308.[X.6]   
Q.Sheng,Solvinglinearpartialdifferentialequationsbyexponentialsplitting,IMAJ.Numer.Anal.9（1989)199-212.[I1.3]   
C.L.Siegel&J.K.Moser,Lectures on Celestial Mechanics,Grundlehrend.math.Wiss. vol.i87,Springer-Verlag1971;First Germanedition:C.L.Siegel,Vorlesungenuber Himmelsmechanik,Grundlehrenvol.85,Springer-Verlag,1956.[VI.1],[VI.5],[V.6]   
J.C.Simo&N.TarnowThediscreteenergy-momentummethod.Conservinglgorithmsfor nonlinearelastodynamics,Z.Angew.Math.Phys.43(1992)757-792.[V.5] symplecticschemesfor nonlineardynamics,Comput.MethodsAppl.Mech.Eng.100 (1992)63-116.[V.5]   
H.D.Simon&H.Zha,Low rank matrixapproximationusing the Lanczos bidiagonalization process with applications,SIAMJ.Sci.Comput.21(2000)2257-2274.[IV.9]   
R.D.Skeel&C.W.Gear,Doesvariablestepsizerunasymplecticintegrator?,PhysicaD60 (1992)311-313.[VIII.2]   
M.Sofroniou&GSpaletta,Derivationofsymmetricompositionconstantsforsmetric integrators,J.ofOptimization Methodsand Software(2004)toappear.[V.3]   
A.Sommerfeld,Mechanics(Lectureson Theoretical Physics,vol.I),irstGermaned94, English transl.byM.O.Stern,Acad.Press.[VI.5]   
S.Sternberg,CelestialMechanics,BenjaminNew York,1969.[X.0]   
E.Stiefel,insfelderndFepalelimusinnimesionalenMnigaligeiten Comment.Math.Helv.8(1935)305-353.[IV.9]   
H.J.Stettelyisofizaionoforrinryeretalutioin ger-Verlag，Berlin97[.3].[.4],[V.][V2]   
D.StofferOnevesiblendnoicalinegraionmethoseportN Zurich,1988.[V.1]   
D.Stoffer,VariablestepsforreversibleintegrationmethodsComputing55(1995)1-22. [VIII.2],[VII.3]   
D.Stoffer,General linearmethods:connection to onestepmethodsand invariantcurves, Numer.Math.64(1993)395-407.[XV.2]   
D.Stoffer,Onthequalitativebehaviourofsymplecticintegrators.II:Perturbed integrable systems,J.Math.Anal.Appl.217(1998)521-545.[XII.4]   
C.StormerSurlestrajectoiresdescorpuscules electrises,Arch.ci.phys.nat.Gnevevol. 24(1907)5-18,113-158,221-247.[I.1]   
G.Strang,Ontheconstructionandcomparisonofdiffrenceschemes,AMJ.Numer. Anal.5（1968)506-517.[II.5]   
W.B.Streett,D.J.Tildesley&GSaville,Mulipletimestepmethods inmoleculardyamics Mol.Phys.35(1978)639-648.[VII.4]   
A.M.Stuart&AR.Humphries,Dynamical SystemsandNumerical Analysis,Cambidge UniversityPress,Cambridge,1996.[XI1.3]   
G.Sun,ConstructionofhighodersymplecticRunge-KuttaMethods,J.Comput.Math11 （1993a)250-260.[IV.2]   
G.Sun,SymplecticparitionedRunge-Kutamethods,J.Comput.ath.11(1993b)365-72. [11.2],[v.2]   
G.Sun,A simplewayconstructingsymplecticRunge-Kutta methods,J.Comput.Math.18 (2000)61-68.[VI.10]   
K.F.Sundman,MemoiresurleproblemedestroiscorpsActaMath.36(1912)105-179. [VIII.2]   
Y.B.Suris,Ontheconservationofthesymplecticstructureinthenumericalsolutionof Hamiltoniansystems(inRussian),In:Numerical SolutionofOrdinary ierentialEquations,ed.S.S.Filippov,KeldyshInstituteofAppliedMathematics,URAcademyof Sciences,Moscow,1988,148-160.[Vl.4]   
Y.B.Suris,Thecanonicity ofmappings generated by Runge-Kutt typemethods when integratingthe systems $\ddot { x } = - \partial U / \partial x$ Zh.Vychisl.Mat.iMat.Fiz.29,202-211(in Russian);sameasU.S.S.R.Comput.Maths.Phys.29(1989)138-144.[VI.41   
Y.B.SurisHamiltonianmethodsof Runge-Kuttatypeandtheir variationalinterpetation (inRussian),Math.Model.2（1990)78-87.[V1.6]   
Y.B.Suris,PartitionedRunge-KuttamethodsasphasevolumepreservingintegratorsPhys. Lett.A220(1996)63-69.[VI.9]   
Y.B.Suris,Integrablediscretizationsforlatticesystems:localequationsofmotionandtheir Hamiltonianproperties,Rev.Math.Phys.11(1999)727-822.[VI.2]   
Y.B.Suris,heProblemofntegrablescretization:HamiltonianApproch,rogresin Mathematics219,Birkhauser,Basel,2003.X.]   
G.J.Sussman&J.Wisdom,Chaoticevolutionofthesolarsystem,Science257(1992)56-62. [1.2]   
M.Suzuki,Fractaldecomposition ofexponentialoperators withapplicationstomany-body theoriesandMonteCarlosimulationsPhys.LettA146(1990)319-323.[Il.4],[I.5]   
MSuzukiealthoyoffrctalpthntegalswithpplicaiotmandyi andstatisticalphysics,J.Math.Phys.32(1991)400-407.III.3]   
M.Suzuki,General theoryofhigher-orderdecompositionofexponentialoperatorsandsymplecticintegrators,Phys.Lett.A165(1992)387-395.[I1.5],[V.6]   
M.Suzuki,Quantum MonteCarlomethodsandgeneraldecompositiontheoryofexponential operatorsandsymplecticintegrators,PhysicaA205(1994) 65-79.[V.3]   
M.Suzuki&K.Umeno,Higher-orderdecomposition theory ofexponential operators and itsapplicationsto QMCand nonlinear dynamics,In:Computer Simulation Studiesin Condensed-eryicsVInuMonter(eds.）ringerroceingin Physics76(1993)74-86.[V.3]   
W.W.Symes,TheQRalgorithmandscatteringforthefinitenonperiodicTodalattice,PhyicaD4(1982)275-280.[IV.3]   
F.Takens,Motionundertheinfluenceofastrongconstrainingforce,Globaltheory ofdynamicalsystems,Proc.int.Conf.,Evanston/Il.1979,SpringerLNM819(1980)425-445. [XIV.3]   
Y.-F.Tang,Thesymplecticityofmuli-stepmethods,ComputersMath.Applic.25(1993)83- 90.[XV.4]   
Y.-F.Tang,Formal energyofasymplecticschemeforHamiltoniansystemsanditsapplications(I）,ComputersMath.Applic.27(1994)31-39.[IX.3]   
Y.F.Tang,V.M.Perez-Garcia&L.Vazquez,SymplecticmethodsfortheAblowitz-Ladik model,Appl.Math.Comput.82(1997)17-38.[VII.4]   
B.Thaler,Visual Quantum Mechanics.Selectedtopics with computer-generatedanimations ofquantum-mechaicalpenomena.rnger-OS,ewYorkoo.[I.6   
W.Thirring,Lehrbuchderthematischenhysik1,Sprnger-Verlag,977.[X.5]   
M.Toda,Waves innonlinearlatice,Progr.Theor.Phys.Suppl.45(1970)174-20o.[X.1]   
J.Touma&J.Wisdom,Lie-Poissonintegratorsforrigidbodydynamicsinthesolarsystem, Astron.J.107(1994)1189-1202.[VII.5]   
H.F.Trotter,Ontheproduct ofsemi-groupsofoperators,Proc.Am.Math.Soc.10(1959) 545-551. [II.5]   
M.Tuckerman,B.J.Bene&G.J.Martyna,Reversiblemultipletimescalemoleculardnamics,J.Chem.Phys.97(1992)1990-2001.[VIII.4],[XIII.1]   
V.S.Varadarajan,LieGroups,LielgebrasandTheirRepresentations,rentice-Hal,Engle woodCliffs,NewJersey,1974[III.4],[IV.6],[IV.8]   
L.Verlet,Computer"experiments"onclassicalfluids.1.Thermodynamicalpropertiesof Lennard-Jonesmolecules,PhysicalReview159(1967)98-103.[1.1],[XI.1]   
A.P.Veselov,Integrablesytemwithdiscretetimeanddifferenceoperators,Funsional. Anal.iPrilozhen.22(1988)1-13,96;transl.inFunct.Anal.Appl.22(1988)83-93. [V1.6]   
A.P.Veselov,Integrablemaps,Russ.Math.Surv.46(1991)1-51.[VI.6]   
R.deVogelaere,Methodsofintegrationwhichpreservethecontacttransformationproperty oftheHamiltonianequations,ReportNo.4,DeptMath.Univ.ofNotreDame,Notre Dame,Ind.(1956)[I.1],[VI.3]   
VVolterra,Variazioniefuttuazionidelnumerod'individuiinspecieanimaliconiventi, Mem.R.Comitatotalassograficoitaliano,CXXXI,1927;Opere5,p.1-111.[1.1]   
J.Waldvogel&F.Spirig,Chaotic motionin Hil'slunar problem,In:A.E.RoyandB.A. Steves,eds.FromNewtontoChaos:ModernTechniquesfor UnderstandingandCoping with Chaosin $N$ -BodyDynamical Systems(NATOAdv.Sci.Inst.Ser.BPhys.,336, PlenumPress,NewYork,1995).[ViI.2]   
G.Wanner,Runge-Kuta-methods withexpansion inevenpowersofh,Computing11(1973) 81-85.[1I.3],[V.2]   
R.A.Wehage&E.J.Haug,Generalized coordinatepartitioningfordimensionreduction in analysisofconstraineddynamicsystems,J.Mechanical Design 104(1982)247-255. [Iv.5]   
J.M.Wendlandt&J.E.Marsden,Mechanical integratorsderivedfromadiscretevariational principle,PhysicaD106(1997)223-246.[VI.6]   
H.Weyl,The Cassical Groups,Princeton UnivPress,Princeton,939.[V]   
H.Weyl,Themethodoforthogonalprojectioninpotential theory,DukeMath.J.7(1940) 411-444.[VI.9]   
J.H.Wilinson,Erroralysisoffoting-pntcmputation,umer.ath2(960)19 340.[IX.0]   
J.Wisdom&M.Holman,SymplecticmapsfortheN-body problem,Astron.J.102(1991) 1528-1538.[V.3]   
J.Wisdom,M.Holman&J.Touma,Symplecticcorrectors,inIntegrationAlgorithmsand ClassicalMechanics10,J.E.Marsden,G.W.Patrick&W.F.Shadwick,eds.,Amer.Math. Soc.,Providence,R.I.(1996)217-244.[V.3]   
K.Wright,Some relationships between implicit Runge-Kutta,collcationand LanczosT methods,and their stabilityproperties,BIT10(1970)217-227.[II.1]   
K.Wright,Diffrential equations for theanalytic singular value decomposition ofamatrix, Numer.Math.63(1992)283-295.[IV.9]   
W.Y.Yan,U.Helmke&J.B.Moore,GlobalanalysisofOja'sflowforneuralnetworks,IEEE Trans.NeuralNetw.5(1994)674-683.[IV.9]   
H.Yoshida,Constructionofhigher ordersymplectic integrators,Phys.Lett.A150(1990) 262-268.[I.4],[II.5],[I.4],[I.5],[V3]   
H.Yoshida,Recentprogressinthetheoryandapplicationofsymplecticintegrators,Celestial Mech.Dynam.Astronom.56(1993)27-43.[IX.1],[1X.4].[IX.8]   
A.Zanna,Collocationandrelaxedcollocationforthe Ferand theMagnusexpansions,SIAM J.Numer.Anal.36(1999)1145-1182.[IV.7],[IV.10]   
A.Zanna,K.Engg&H.Z.Munthe-Kaas,Adjoint andselfadjoint Lie-groupmethods,BIT41 (2001)395-421.[V.4],[V.6]   
K.Zare&V.Szebehely,Timetransformationsintheextendedphase-space,CelestialMechanics11(1975)469-482.[VIII.2]   
C.Zener,Non-adiabatic crossing ofenergy levels,Proc.Royal Soc.London,Ser.A137 (1932)696-702.[XIV.1]   
S.L.Ziglin,The ABC-flowisnot integrable for $A = B$ ,Funktsional.Anal.iPrilozhen.30 (1996)80-81;transl.in Funct.Anal.Appl.30(1996)137-138.[VI.9]

Index

ABCflow228   
Abel-Liouville-Jacobi-Ostrogradskii   
identity105,228   
Ablowitz-Ladik model 273   
action integral205   
action-anglevariables397   
adaptive Verletmethod 309   
adiabatic integrator 547   
adiabaticinvariants 531,533,545.562   
adiabatic transformations 531,532   
adjoint method 42,145,342,613   
-ofcollocation method146   
-ofRunge-Kutta method147   
-quadraticinvariants176   
adjoint operator83   
angularmomentum 9,98,100,101,276,   
591,601   
areapreservation5,6,183,184,188   
Argon crystal19   
Arnold-Liouville theorem397   
attractiveinvariant manifold 460,574,610   
attractive invariant torus464   
-of numerical integrator467   
averaged forces 319   
averaging   
-basic scheme458   
-perturbation series459   
averaging principle 456   
avoided crossing 535.563   
B-series 51,56,57,212,223,575   
-composition61   
-symplectic217,219   
backward error analysis 337,576   
-formal337   
-rigorous360   
BCHformula 83,84.348   
-symmetric86   
Bernoulli numbers 84,122   
bi-coloured trees 66   
$B _ { \infty }$ -series72   
Birkhoff normalization   
-Hamiltonian 412   
-reversible 447   
$B ( p )$ 32   
Butcher group 64372   
Butcher product75,212   
canonical 186   
-equations of motion 181   
-form267   
-Poisson structure 254   
-transformation 186   
canonical coordinates of aLie group   
-firstkind129   
-second kind 129   
Casimir function257,267,283   
Cayley transform107,128   
centralfeld392,400,438,440   
characteristic lines 262   
Choleski decomposition154   
coadjoint orbit287   
collocationmethods 27,30,122   
-discontinuous 35,247   
-symmetric146   
collocation polynomial30   
commutator118   
-matrix83   
compensated summation 323   
complete systems 263   
completely integrable393   
composition   
-ofB-series61   
-ofRunge--Kutta methods59   
composition methods43,45,50,92,105,   
190,333   
$\rho$ -compatibility145   
-localerror 150   
-oforder2 150   
-oforder4 152,155   
-of order6 153,156   
-oforder8 157   
638 Index   
-oforder10158   
orderconditions71,75,80   
-symmetric149   
-symmetric-symmetric154   
-with symmetricmethod154   
conditionally periodic flow399   
configuration manifold 239   
conjugatemomenta181   
conjugate symplecticity 222,225,592   
conservation   
-ofarea5,183   
-ofenergy98,172,366,484,512,600   
-oflinearinvariants99   
-ofmass98   
-ofmomentum172.600   
-ofquadraticinvariants101,102,212,   
214,216   
-ofvolume227   
conserved quantity97   
consistent initial values238   
constant direction of projection165   
constrained Hamiltonian systems239,   
258   
constrained mechanical systems 237   
continuous output326   
coordinates   
-generalized180   
cotangent bundle240   
$C ( q )$ 32   
Crouch-Grossman methods124   
-order conditions124   
d'Alembert principle 259   
Darboux-Lie theorem 261,265,266,272   
degrees of freedom5   
diagonally implicit Runge-Kuttamethods   
-symmetric147   
differentialequations2   
-Hamilton-Jacobi200   
-Hamiltonian4,180   
-highly oscillatory21   
-modified337   
-onLie groups118   
-onmanifolds115,239   
partial,linear262   
-reversible143   
-second order7,41,216,332   
differential equations on manifolds   
- $\rho$ -compatibility145   
differential form186   
differential-algebraic equations140.237   
diophantine frequencies406   
Dirac-Frenkel variational principle138,   
259,295   
DIRK methods   
-symmetric147   
discontinuous collocation 35,247   
discrete Euler-Lagrange equations206   
discreteLagrangian206   
discretemomenta206   
discrete-gradient methods 171.174   
dissipative systems455   
distinguished functions 266   
divergence-free vector fields 227   
eccentricity 9   
effective order   
-of composition methods158   
EI150   
elementary differentials 52,53,66   
elementary Hamiltonian 373,384   
elementary weights55   
energy   
-oscillatory479,484,505,510,517,524   
-total182,479,484,510,524   
energyconservation366,379,510.524,   
600   
energyexchange483,490,494   
energy-momentummethods171   
-for $N$ -bodysystems173   
equistage approximation 329   
erroranalysis   
-backward337   
errorgrowth   
-linear413,414,448   
-ofrounding errors324   
Eulerequations275,277,279   
Eulermethod   
-Lie126   
-explicit3   
-implicit3   
-symplectic4,48,189,230,242,270   
Euler parameters281   
Euler-Lagrange equations181,205,237   
-discrete206   
explicit symmetric methods148   
exponential map120   
Fermi-Pasta-Ulamproblem 21,479   
filter function481   
first integrals5,97,211,375   
-long-timenear-preservation 413,448   
quadratic 212,591   
fixed-point iteration330   
flow2   
-discrete3   
-exact2,49,200   
-isospectral107   
numerical3,49   
-Poisson 261,265   
frequencies399   
-diophantine406   
Frobenius norm132   
G-symplectic587   
Gaussmethods 34,101,333   
-symmetric147   
-symplectic192   
Gaussian wavepacket296   
Gautschi-typemethods473,477   
general linear methods 609   
-strictly stable609   
-symmetric611   
-weakly stable610   
generalized coordinate partitioning117   
generatingfunctions195,197,201,204,   
288,344   
forpartitioned RK methods199   
forRunge-Kuttamethods198   
geometrical numerical algebra 131   
${ \mathrm { G L } } ( n )$ ,general lineargroup119   
${ \mathfrak { g l } } ( n )$ ,Liealgebraof $n \times n$ matrices 119   
Grassmann manifold 131,135   
growth parameter 592,614   
Henon-Heiles problem380   
Hall set78   
Hamilton's principle204,205   
Hamilton-Jacobi equation 200,391   
Hamiltonian4,181,257   
-elementary373,384   
-global186   
-local185.234   
-modified343,375   
Hamiltonian perturbation theory 389,404   
-basic scheme405   
-Birkhoff normalization412   
-KAMtheory410,423   
-perturbation series406   
Hamiltonian systems4,180   
-constrained 239,258,289   
-integrable390   
-non-canonical237   
-perturbed integrable404   
harmonic oscillator   
-varyingfrequency 546   
heavytop283   
Henon-Heiles model 15   
Hopf algebra65   
picncnanon JUJ,JZJ   
implicit midpointrule3,34,190,192,   
223,270   
-averaged 537   
symmetry145   
-symplecticity 190   
impulsemethod317,475,550   
-mollified476   
index reduction 239,241   
inertia ellipsoid275   
integrability lemma186   
integrable systems601   
-Hamiltonian390   
-reversible437   
invariant manifold 574   
-attractive460,574,610   
invariant torus 397,423   
-long-time near-preservation 422,451   
-ofnumericalintegrator433,453,467   
-ofreversible map451   
-of symplectic map431   
-weakly attractive 464   
invariants2,5,97   
-adiabatic 531,533,545,562   
-linear99   
-polynomial105   
-quadratic101   
-weak109   
involution   
-first integrals in 391   
irreducible   
-Runge-Kutta methods 220   
isospectral fow107,403   
isospectral methods107   
iteration   
-fixed-point330   
-Newton-type331

Jacobi identity 118,255

KAMtheory   
-Hamiltonian 410,423   
-reversible445   
-reversible near-identitymap451   
-symplectic near-identity map431   
KAMtorus   
-sticky412   
Keplerproblem8,25,46,111,150,234, 416,603   
-perturbed12,26,304   
Kepler's second law9   
kernel   
-of processing methods158

kinetic energy180,237   
Kolmogorov'siteration410   
Kolmogorov's theorem423   
Lagrange equations181   
Lagrangemultipliers111,132,237,279   
Lax pair403   
leap-frog method7   
left-invariant289   
Legendre transform181   
-discrete206   
Leibniz'rule 255   
Lennard-Jones potential19   
Liealgebras118,286   
Liebracket 89,118,261   
-differential operators89   
Liederivative 87,348,362   
-ofB-series 370   
-ofP-series382   
Lie group methods 123,351   
-symmetric169   
Liegroups118   
-quadratic128   
Lie midpoint rule127   
Lieoperator261   
Lie-Euler method126   
Lie-Poisson reduction 289   
Lie-Poisson systems 274,286   
Lie-Trotter splitting47   
Lindstedt-Poincare series406   
linearerrorgrowth12,413,414,448,601   
linear multistepmethods   
-weakly stable575   
linear stability23   
Liouville lemma392   
Liouville's theorem 227   
LobattoIIA-IIB pair102,192,210,   
247,352,386   
Lobatto IIA methods34,377   
-symmetric147   
Lobatto IIA-IIB pair40   
LobattoIIBmethods37,377,449   
-symmetric147   
Lobatto IIIS235   
Lobatto quadrature247   
local coordinates113   
-existence of numerical solution167   
-symmetric methods166   
local error29   
-of composition methods 150,176   
long-time behaviour   
-symmetricintegrators437,455   
-symplectic integrators 389,455   
long-timeenergy conservation366   
Lorenz problem176   
Lotka-Volterraproblem1,24,175,257,   
270,271,273,340   
low-rank approximation137   
Lyapunov exponents131   
Magnus series121   
manifold of rank kmatrices131   
manifolds109,114,239,267   
-symmetric methods161   
-symplectic 258   
Marchuk splitting47   
matrixcommutator 83   
matrix exponential 120   
matrix Lie groups 118   
mechanical systems555   
-constrained 237,258   
merging product75   
methods based on local coordinates166   
methods onmanifolds 97,350   
-symmetric161   
midpoint rule123   
-explicit569,580   
-implicit3,34,190,192,223,270   
-Lie127   
-modified171   
modified differential equation337   
B-series369   
constrained Hamiltonian system 352   
first integrals351   
-Lie group methods351   
-Lie-Poisson integrators354   
methods onmanifolds350   
-P-series381   
perturbed differential equation 466   
Poisson integrators 347   
-reversiblemethods343   
-splitting methods348   
-symmetric methods342   
-symplectic methods 343   
-trees369   
-variable steps356   
modified equation   
-parasitic579   
modified Hamiltonian 343,375,589   
-global344,353   
modified midpoint rule171   
modulated Fourier expansion 496   
-exact solution486,496   
-Hamiltonian503   
-multi-frequency519   
-numerical solution488,498   
molecular dynamics18   
mollifiedimpulsemethod 476,554   
momenta181   
-conjugate181   
-discrete206   
moments of inertia 100   
momentum   
-angular9,98,100,101,173   
-linear98,173   
momentum conservation 600   
Moser-Veselovalgorithm 281   
multi-force methods 478   
multi-value methods 609   
-symmetric611   
multiple time scales 472,479   
multiple time stepping 316,475   
multirate methods316   
multistep methods567   
-backward error analysis 576   
G-symplectic587   
-partitioned572   
second order equations 569   
strictly stable 568,573   
-symmetric568,570   
-symplectic585   
-variable step sizes605   
Munthe-Kaasmethods125   
$N$ -bodysystem 13,98   
-energy-momentummethods 173   
Newton-type iteration 331   
Noether'stheorem210   
non-resonant frequencies406   
non-resonant stepsize433,498,511   
Nystrommethods41,69,96,104   
-symplectic194   
${ \mathrm { O } } ( n )$ ,orthogonal group 119   
one-leg methods587   
one-stepmethod 8,29,187   
-underlying573,609   
optimal control 235   
order29   
-ofatree53,67   
-of symmetric local coordinates 167   
-of symmetric projection 162   
order conditions   
-compositionmethods71,75,80.93,94   
-Crouch-Grossman methods 124   
-Nystrom methods69   
-partitionedRKmethods 39,69   
-processingmethods159   
-RKmethods 29,51,56,58   
-splitting methods 80,92   
-symmetriccomposition 155   
-symmetrized177   
ordered subtrees 60   
ordered trees 60   
orientedarea 183   
oriented free trees 388   
orthogonal matrices 118   
orthogonality constraints 131   
oscillatory differential equations 21,471,   
531   
oscillatory energy 22,479,484,505,510,   
517,524   
outer solar system 8,13,112   
P-series 68,214   
-symplectic 217,219   
parametrization   
-tangent space117   
partial differential equations   
-linear262   
partitioned Runge-Kutta methods38,   
102,148   
-diagonally implicit149   
-symmetric 148   
-symplectic193,208,231   
partitioned systems3,66   
pendulum4,5,110,181,185,188,367,   
396,593   
-double233   
-spherical 238,254   
-stiffspring526   
perturbation series   
-averaging459   
-Hamiltonian406   
-reversible444   
perturbation theory   
-dissipative455   
-Hamiltonian 389,404   
-reversible437   
phase space 2   
Poincare cut16   
Poisson   
-bracket 255,257   
-flow261,265   
-integrators270,272,300   
-maps268   
-systems 254,257,297   
Poisson structures265   
-canonical 254   
-general256   
polardecomposition 134   
polynomial invariants 105   
potential energy 181,237   
precession 12,26   
processing   
-ofcomposition methods 158   
-order conditions 159   
projection   
-symplectic259   
projection methods 109,351   
-standard110   
-Stiefel manifolds 133   
-symmetric161   
-symmetric non-reversible 166   
pseudo-inverse ofamatrix 116   
pseudo-symplectic methods 436   
QRalgorithm108   
QRdecomposition 134   
quadratic invariants 101   
-near conservation 225   
quadratic Lie groups 128   
quantumdynamics 293   
quasi-periodic flow 399   
quaternions 281   
r-RESPA method318,475   
Radau methods34   
rank $k$ matrixmanifold131   
RATTLE245,280,352,388   
resonance   
-numerical 482,485,602   
resonance module517   
reversibility239,311   
-of symmetric local coordinates 168   
-of symmetric projection 163   
reversiblemaps143,144   
reversible methods 343   
reversible perturbation theory 437   
-basic scheme 443   
Birkhoffnormalization447   
KAM theory445   
-perturbation series444   
reversible systems143   
-integrable437   
-perturbed integrable 442   
reversible vector fields 144   
$\rho$ -compatibilitycondition 145   
$\rho$ -reversible143   
-maps144   
-vector field143   
Riccati equation134   
rigidbody99,163,274,280,288,441   
449   
-Hamiltonian theory278

Rodrigues formula 141   
rooted trees53   
rounding error322   
Runge-Kutta methods 27,28,101,311, 325,333   
三 $\rho$ compatibility 145   
一 additive50 adjointmethod 147 implicit29   
-irreducible 220   
-partitioned 38,148   
-symmetric 146   
-symplectic 191,231   
Runge-Lenz-Pauli vector26

s-stable 594   
Schrodinger equation 293   
-nonlinear273   
semiclassical dynamics293   
separable partitionedsystems 231   
SHAKE 245   
simplifying assumptions 96   
sinc function 473,481   
singular value decomposition133   
$\operatorname { S L } ( n )$ ,speciallinear group119,130   
${ \mathfrak { s l } } ( n )$ ,speciallinearLiealgebra119   
smalldenominators406   
$\operatorname { S O } ( n )$ ,special orthogonal group 119   
${ \mathfrak { s o } } ( n )$ ,skew-symmetric matrices 119   
spherical pendulum 238,254   
splitting   
-fast-slow317   
-Lie-Trotter47   
-Marchuk47   
-of ordered tree370   
-Strang47,230   
splittingmethods47,48,91,193,252,   
270,284,298,348   
1 $\rho$ -compatibility145   
-negative steps82   
-of higher order82   
-order conditions80   
$\operatorname { S p } ( n )$ ,symplectic group 119   
${ \mathfrak { s p } } ( n )$ ,symplecticLiealgebra119   
stability   
-linear23   
-long-term 592   
stability function194   
starting approximations326   
-order327   
step size control   
integrating,reversible 314,357,449   
538

proportional,reversible310,313,356, 449 -standard303 -structure-preserving310 step size function 308,311 Stiefel manifold131 Stormer-Verlet scheme7,9,39,48,189, 270,318,349,386,472,586 -asclassical limit300 -as composition method148 -as Nystrommethod41 -as processing method159 -as splitting method48 asvariational integrator 208 energy conservation 368,513 linearerror growth414 symmetry42,145 symplecticity48,190 variable stepsize308,309,312,313, 315 Strangsplitting47,230,315,348 structure constants286 submanifold109 -symplectic259 subtrees -ordered60 summation -compensated323 superconvergence32,37,250 Suzuki'sfractals45,46,153 switching lemma76 symmetric collocation methods 146,176 symmetric composition94 -offirst ordermethods150 -of symmetric methods150,154 symmetric composition methods149 -oforder6156 -oforder8157 -oforder10158 symmetric Lie group methods169 symmetricmethods3,42,143,144,342, 612 -explicit148 -symmetric composition154 symmetric methods on manifolds161 symmetric projection161 -existence of numerical solution 162 -non-reversible166 symmetric Runge-Kutta methods146, 176 symmetric splitting method177 symmetrized order conditions177 symmetry 289,311,613

-ofGauss methods147   
-ofLobatto147   
-of symmetric local coordinates 168   
symmetrycoefficient 57,67,72   
symplectic 183,196,241   
-B-series217   
-maps268   
-P-series217   
-projection259   
-submanifold 258.295   
symplectic Eulermethod4,48,189,193,   
230,242,270,340,346,349,383   
-assplitting method48   
-energy conservation 368   
-variable step size307   
symplectic methods187,612   
-asvariational integrators207   
-based on generating functions203   
-irreducible 222   
-Nystrom methods194   
partitioned Runge-Kutta methods193,   
208   
-Runge-Kutta methods191   
-variable step size306   
symplecticsubmanifold 259   
symplecticity 244,585   
Takens chaos563   
tangent bundle239   
tangent space 114,120   
-parametrization117,134   
$\theta$ method147   
-adjoint148   
three-body problem321,390   
time transformation306,356   
time-reversible methods144   
Toda flow109   
Toda lattice402,414,440,449   
total differential 186,196   
totalenergy9,18,21,98,479,484510,   
524,600   
transformations   
-adiabatic 531,532   
-averaging 458   
-canonical 186   
-reversibility preserving438   
-symplectic182,183,196,241   
trapezoidalrule 28,194,223,312   
trees51,217,369   
-bi-coloured66   
-equivalence class384   
-ordered60   
-oriented free388   
-rooted 53   
$\infty$ -trees 72   
trigonometric methods 473   
triplejump 44,46,153   
trueanomaly9   
two-bodyproblem 9,25   
two-force methods 478

underlying one-step method 573,609

Vander Pol'sequation 455   
variational integrators 204   
variational problem 205,237   
variational splitting 271   
vectorfields2   
-divergence-free 227   
-reversible143,144   
Verletmethod7,39,48,189,270,318,   
472,513   
-adaptive309   
Verlet-Imethod 318,475   
volumepreservation105,113,227,231   
volume-preserving integrators228   
weak invariants109   
work-precisiondiagrams150,153,156,   
157,334,336,482,604,605,608   
$W$ -transformation 235

Document generated by Anna's Archive around 2023-2024 as part of the DuXiu collection (https://annas-blog.org/duxiu-exclusive.html).

Imageshavebeen lossesyembedded.InformationabouttheoriginalfilecanbefoundinPDFattachments.Somestats (moreinthe PDF attachments):

"filename": "NDA5NDIxMzkuemlw", "filename_decoded": "40942139.zip", "filesize": 88252410, "md5": "bd528c5e501c4056949dce90386b795c", "header_md5": "bd925c52d0d865996ac4b3817d9cfd5c", "sha1": "0f05049345967ac3d0759bf19d69467c04827fe1", "sha256": "8cee576d491a782214937d43b3e570d7f89f41df084f34b62c288ed97953ee4d", "crc32": 1327794179,   
"zip_password": ", "uncompressed_size": 110168428,   
"pdg_dir_name:"\u255du25\u2551\u256\u2569\u00b2\u2553\u256\u2557\u00b\u2556\u2553\256\u250c\u2562\u25a\u25   
91\u00b5_40942139", "pdg_main_pages_found": 644, "pdg_main_pages_max": 644, "total_pages": 663, "total_pixels": 2831739552, "pdf_generation_missing_pages": false   
}
