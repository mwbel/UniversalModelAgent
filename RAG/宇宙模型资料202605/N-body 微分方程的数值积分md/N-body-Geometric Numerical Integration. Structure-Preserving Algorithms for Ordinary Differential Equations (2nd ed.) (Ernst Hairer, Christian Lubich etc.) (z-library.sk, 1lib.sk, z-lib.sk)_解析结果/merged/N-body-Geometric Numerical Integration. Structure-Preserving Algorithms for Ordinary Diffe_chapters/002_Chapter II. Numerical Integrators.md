# Chapter II. Numerical Integrators

Afterhaving seen in Chap.I some simple numerical methods and avariety of numerical phenomena that they exhibited,we nowpresent more elaborateclassesof numerical methods.We start with Runge-Kutta and collocation methods,and we introduce discontinuous collocation methods,which cover essentiallyall high-order implicit Runge-Kutta methods of interest.We then treat partitioned Runge-Kutta methods and Nystrom methods,which can be applied to partitioned problems such asHamiltonian systems.Finallywe present composition and splitingmethods.

# II.1 Runge-Kutta and Collocation Methods

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/6a0873dbd1d07ad8dc58d98121c8049ba4378c690f6b6a7ab8ff804fdcdab72a.jpg)  
Fig.1.1.Carl David TolméRunge(left picture),born:30August 1856in Bremen(Germany), died:3January 1927inGotingen(Germany）. WilhelmMartinKutta(right picture),born:3November1867inPitschen,UpperSilesia (now Byczyna,Poland),died:25December1944inFurstenfeldbruck(Germany)

Runge-Kutta methods form an important class of methods for the integration of differential equations.A special subclass,the collocation methods,allows for a particularly elegant access to order,symplecticity and continuous output.

# II.1.1Runge-Kutta Methods

In this section,we treat non-autonomous systems offirst-order ordinary differential equations

$$
\dot { y } = f ( t , y ) , \qquad y ( t _ { 0 } ) = y _ { 0 } .
$$

Theintegration of this equation gives $\begin{array} { r } { y ( t _ { 1 } ) = y _ { 0 } + \int _ { t _ { 0 } } ^ { t _ { 1 } } f ( t , y ( t ) ) d t } \end{array}$ and replacing theintegral bythe trapezoidal rule,weobtain

$$
y _ { 1 } = y _ { 0 } + { \frac { h } { 2 } } { \big ( } f ( t _ { 0 } , y _ { 0 } ) + f ( t _ { 1 } , y _ { 1 } ) { \big ) } .
$$

Thisis theimplicit trapezoidal rule,which,inaddition toitshistorical importancefor computations in partial differential equations (Crank-Nicolson） and in A-stability theory (Dahlquist),played acrucial role even earlier in thediscovery of Runge-Kutta methods.It was the starting point ofRunge(1895）,who“predicted" theunknown $y _ { 1 }$ -valuetotherightbyan Eulerstep,and obtained the first of the following formulas (the second being theanalogous formula for themidpoint rule)

$$
\begin{array} { r l r l } & { k _ { 1 } = f ( t _ { 0 } , y _ { 0 } ) } & & { k _ { 1 } = f ( t _ { 0 } , y _ { 0 } ) } \\ & { k _ { 2 } = f ( t _ { 0 } + h , y _ { 0 } + h k _ { 1 } ) } & & { k _ { 2 } = f \bigl ( t _ { 0 } + \frac { h } { 2 } , y _ { 0 } + \frac { h } { 2 } k _ { 1 } \bigr ) } \\ & { y _ { 1 } = y _ { 0 } + \frac { h } { 2 } \bigl ( k _ { 1 } + k _ { 2 } \bigr ) } & & { y _ { 1 } = y _ { 0 } + h k _ { 2 } . } \end{array}
$$

Thesemethods have a nice geometric interpretation (which isillustrated in the first twopicturesof Fig.1.2 fora famousproblem,theRiccati equation):they consist ofpolygonal lines,which assume the slopes prescribed by the differential equation evaluated at previous points.

Ideaof Heun(19oo) and Kutta(19o1):compute several polygonal lines,each startingat $y _ { 0 }$ and assuming the various slopes $k _ { j }$ onportions of the integration interval, which are proportional to some given constants $a _ { i j }$ ;at the final point of each polygon evaluatea new slope $k _ { i }$ Thelast of these polygons,with constants $b _ { i }$ ,determines the numerical solution $y _ { 1 }$ (see the third picture ofFig.1.2).This idea leads to theclass of explicit Runge-Kutta methods,i.e.,formula(1.4) belowwith $a _ { i j } = 0$ for $i \leq j$ .

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/8098b19ecb63fcdfaacc1584a3e182e3ea3bf5de095ece7de48d2c299776adc7.jpg)  
Fig.1.2.Runge-Kutta methods for $\dot { y } = t ^ { 2 } + y ^ { 2 } ,$ $y _ { 0 } = 0 . 4 6$ , $h = 1$ dotted:exact solution

Much more important for our purposeare implicit Runge-Kut methods,introduced mainly in the work of Butcher(1963).

Defnito .1, Let $b _ { i } , a _ { i j }$ $i , j = 1 , \dots , s )$ be rea umbers ad let $\begin{array} { r } { c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } } \end{array}$ An $s$ -stageRunge-Kuttamethodisgiven by

$$
\begin{array} { r c l } { { k _ { i } } } & { { = } } & { { f \Big ( t _ { 0 } + c _ { i } h , y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } \Big ) , ~ i = 1 , \ldots , s } } \\ { { } } & { { } } & { { } } \\ { { y _ { 1 } } } & { { = } } & { { y _ { 0 } + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } . } } \end{array}
$$

Herewe allowa fullmatrix $( a _ { i j } )$ of non-zero coefficients.In this case,the slopes $k _ { i }$ canno longer be computed explicitly,and even do not necessarily exist.For example,for theproblem set-up ofFig.1.2 theimplicit trapezoidal rule has no solution.However,the implicit function theorem assures that,for sufficiently small $h$ ， the nonlinear system(1.4） for the values $k _ { 1 } , \dots , k _ { s }$ hasa locally unique solution close to $k _ { i } \approx f ( t _ { 0 } , y _ { 0 } )$

SinceButcher'swork,the coefficients are usuallydisplayedas follows:

$$
{ \begin{array} { r } { { \frac { c _ { 1 } } { c _ { 1 } } } { \Bigg | } { \frac { a _ { 1 1 } } { \cdots } } { \cdots } { \frac { a _ { 1 s } } { a _ { s } } } } \\ { { \vdots } } \\ { { \frac { c _ { s } } { b _ { 1 } } } { \Bigg | } { \frac { a _ { s } } { a _ { 1 } } } { \cdots } { \Bigg . } { \Bigg . } { \Bigg . } } \\ { { \Bigg . } { \Bigg \ } { \frac { b _ { 1 } } { b _ { 1 } } } { \cdots } { \Bigg . } { \Bigg . } } \end{array} } ,
$$

Definition1.2.ARunge-Kutta method(orageneral one-stepmethod) has order $p$ ， ifforall suficientlyregularproblems(1.1）the localerror $y _ { 1 } - y ( t _ { 0 } + h )$ satisfies

$$
y _ { 1 } - y ( t _ { 0 } + h ) = \mathcal { O } ( h ^ { p + 1 } ) \quad \mathrm { a s ~ } h  0 .
$$

Tocheck theorder ofa Runge Kutta method,one has to compute the Taylor series expansions of $y ( t _ { 0 } + h )$ and $y _ { 1 }$ around to $h = 0$ This leads to the following algebraic conditions for the coefficients for orders $1 , 2$ ,and3:

$$
\begin{array} { r l r } & { } & { \sum _ { i } b _ { i } = 1 \qquad \mathrm { f o r ~ o r d e r ~ 1 } ; } \\ & { \mathrm { i n ~ a d d i t i o n } } & { \sum _ { i } b _ { i } c _ { i } = 1 / 2 \qquad \mathrm { f o r ~ o r d e r ~ 2 } ; } \\ & { \mathrm { i n ~ a d d i t i o n } } & { \sum _ { i } b _ { i } c _ { i } ^ { 2 } = 1 / 3 } \\ & { \mathrm { a n d } } & { \sum _ { i , j } b _ { i } a _ { i j } c _ { j } = 1 / 6 \qquad \mathrm { f o r ~ o r d e r ~ 3 } . } \end{array}
$$

Forhigher orders,however,this problem represented a great challenge inthe first half of the 2Oth century.We shall present an elegant theory in Sect.III.1 which allows order conditions to bederived.

Among the methods seenup to now,the explicit and implicit Euler methods

$$
\frac { 0 } { 1 } \neq \frac { 1 \vert 1 } { 1 }
$$

areof order1,the implicit trapezoidal and midpoint rulesaswell as both methods ofRunge

$$
\begin{array}{c} \frac { 1 } { 1 \ | \ 1 / 2 \quad 1 / 2 } \quad \frac { 1 / 2 \ | \ 1 / 2 } { 1 / 1 } \quad \frac { 1 \ 1 / 1 } { 1 / 2 \ 1 / 2 } \quad \frac { 1 } { 1 / 1 } \quad \frac { 1 } { 1 / 2 \ 1 / 2 } \quad \frac { 1 / 2 } { 1 / 2 } \quad \frac { 1 } { 1 / 1 } \end{array}
$$

areof order 2.The most successful methods during more than halfacentury were the4th order methodsofKutta:

# II.1.2 Collocation Methods

The high speed computing machines make it possible to enjoy the advantagesof intricatemethods.(P.C.Hammer&J.W.Hollingsworth1955)

Collocation methods for ordinary differential equationshave their origin,once again,in the implicit trapezoidal rule（1.2):Hammer&Hollingsworth (1955)discovered that this method can be interpreted asbeing generated by a quadratic function“which agrees indirectionwiththat indicatedbythe differential equation at two points” $t _ { 0 }$ and $t _ { 1 }$ (see the picture totheright).This idea allows one to“see much-used methodsin a new light’and allowsvarious generalizations (Guillou& Soulé（1969),Wright(197O)).An interesting feature of collocationmethodsis that we not only get adiscrete set of approximations,but also a continuousapproximationtothe solution.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/385b966d9911de252bb749c40ce452dafaac76ff4e6112376bee7b361acef831.jpg)

Definition 1.3. Let $c _ { 1 } , \ldots , c _ { s }$ be distinct real numbers (usually $0 \leq c _ { i } \leq 1$ .The collocation polynomial $u ( t )$ isa polynomial of degree $s$ satisfying

$$
\begin{array} { l } { u ( t _ { 0 } ) = y _ { 0 } } \\ { \dot { u } ( t _ { 0 } + c _ { i } h ) = f \big ( t _ { 0 } + c _ { i } h , u ( t _ { 0 } + c _ { i } h ) \big ) , \quad i = 1 , \dots , s , } \end{array}
$$

and thenumerical solution of thecollocation method isdefined by $y _ { 1 } = u ( t _ { 0 } + h ) ,$ .

For $s = 1$ ,the polynomial has to beof the form $u ( t ) = y _ { 0 } + ( t - t _ { 0 } ) k$ with

$$
k = f ( t _ { 0 } + c _ { 1 } h , y _ { 0 } + h c _ { 1 } k ) .
$$

Weseethat theexplicit and implicit Euler methods and the midpoint rule are collocation methods with $c _ { 1 } = 0$ ， $c _ { 1 } = 1$ and $c _ { 1 } = 1 / 2$ ,respectively.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/3dedc4046007706c705bc72ec122bdc996b5ee5627d54bf1348acbaade7d80f0.jpg)  
Fig.1.3.Collocationsolutions for the Lotka-Volterra problem(I.1.1); $u _ { 0 } = 0 . 2$ , $v _ { 0 } = 3 . 3$ ; methodsof order2:foursteps with $h = 0 . 4$ method of order4:twostepswith $h = 0 . 8$ ; dotted: exact solution

For $s \ = \ 2$ and $c _ { 1 } ~ = ~ 0 , c _ { 2 } ~ = ~ 1$ we find,of course,the implicit trapezoidal rule.The choice of Hammer&Hollingsworth for thecollocation points is $c _ { 1 , 2 } = 1 / 2 \pm \sqrt { 3 } / 6$ ,theGaussian quadrature nodes (see the picture to the right).We will see that the correspondingmethod is of order 4.

In Fig.1.3we illustrate the collocation idea with these methods for the Lotka-Volterra problem (I.1.1).One can observe that,in spite oftheextremely large step sizes,themethodsarequite satisfactory.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/a52c1a73ac62e478e96462dbc82da14fe292252e401ef19971c8d09c53d017c5.jpg)

Theorem1.4(Guillou& Soulé1969,Wright1970).The collocationmethodof Definition1.3isequivalent to thes-stageRunge-Kuttamethod(1.4)withcoefficients

$$
a _ { i j } = \int _ { 0 } ^ { c _ { i } } \ell _ { j } ( \tau ) d \tau , \qquad b _ { i } = \int _ { 0 } ^ { 1 } \ell _ { i } ( \tau ) d \tau ,
$$

where $\ell _ { i } ( \tau )$ is theLagrangepolynomial $\begin{array} { r } { \ell _ { i } ( \tau ) = \prod _ { l \neq i } ( \tau - c _ { l } ) / ( c _ { i } - c _ { l } ) . } \end{array}$

ProofLet $u ( t )$ be thecollocation polynomial and define

$$
k _ { i } : = \dot { u } ( t _ { 0 } + c _ { i } h ) .
$$

BytheLagrangeinterpolation formula we have $\begin{array} { r } { \dot { u } ( t _ { 0 } + \tau h ) = \sum _ { j = 1 } ^ { s } k _ { j } \cdot \ell _ { j } ( \tau ) } \end{array}$ ,and by integration we get

$$
u ( t _ { 0 } + c _ { i } h ) = y _ { 0 } + h \sum _ { j = 1 } ^ { s } k _ { j } \int _ { 0 } ^ { c _ { i } } \ell _ { j } ( \tau ) d \tau .
$$

Inserted into (1.9) this gives thefirst formula of theRunge-Kuttaequation (1.4). Integration fromOto $^ { 1 }$ yields the second one. □

Theabove proof can also beread inreverse order.This shows thata Runge-Kutta method with coefficients given by(1.1O)can be interpreted asacollocation method.Since $\begin{array} { r } { \tau ^ { k - 1 } = \sum _ { j = 1 } ^ { s } c _ { j } ^ { k - 1 } \ell _ { j } ( \tau ) } \end{array}$ for $k = 1 , \ldots , s .$ therelations (1.10)are equivalent to the linear systems

$$
\begin{array} { l l } { { C ( q ) : \quad } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { c _ { i } ^ { k } } { k } , \quad k = 1 , \ldots , q , \mathrm { a l l } i } } \\ { { B ( p ) : \quad } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , \quad k = 1 , \ldots , p , } } \end{array}
$$

with $q = s$ and $p = s$ Whatisthe order ofaRunge-Kutta methodwhosecoefficients $b _ { i } , a _ { i j }$ aredetermined in thisway?

Compared to the enormous difficulties thatthe first explorers had inconstructing Runge-Kuttamethods of orders5and6,andalso compared to thediffcultalgebraic proofs of the first papers of Butcher,the following general theorem and its proof, discovered inthis formbyGuillou& Soulé(1969),are surprisingly simple.

Theorem1.5 (Superconvergence). If the condition $B ( p )$ holds for some $p \geq s ,$ thenthecollocationmethod(Definition1.3)hasorder $p$ Thismeans that the collocationmethod hasthe same orderastheunderlying quadratureformula.

Proof.We consider the collocation polynomial $u ( t )$ as the solution of a perturbed differential equation

$$
\dot { u } = f ( t , u ) + \delta ( t )
$$

with defect $\delta ( t ) : = \dot { u } ( t ) - f \big ( t , u ( t ) \big ) ,$ Subtracting(1.1） from(1.12）we get after linearization that

$$
\dot { u } ( t ) - \dot { y } ( t ) = \frac { \partial f } { \partial y } \Big ( t , y ( t ) \Big ) \Big ( u ( t ) - y ( t ) \Big ) + \delta ( t ) + r ( t ) ,
$$

where,for $t _ { 0 } \leq t \leq t _ { 0 } + h$ ,theremainder $\boldsymbol { r } ( t )$ is of size $\mathcal { O } \big ( | | u ( t ) - y ( t ) | | ^ { 2 } \big ) =$ $O ( h ^ { 2 s + 2 } )$ byLemma1.6below.Thevariation of constants formula(seee.g.,Hairer, Ngrsett&Wanner(1993),p.66) thenyields

$$
y _ { 1 } - y ( t _ { 0 } + h ) = u ( t _ { 0 } + h ) - y ( t _ { 0 } + h ) = \int _ { t _ { 0 } } ^ { t _ { 0 } + h } { R ( t _ { 0 } + h , s ) \Big ( \delta ( s ) + r ( s ) \Big ) d s } ,
$$

where $R ( t , s )$ istheresolvent of the homogeneous part of the differential equation(1.13),i.e.,the solution of the matrix differential equation $\partial R ( t , s ) / \partial t =$ $A ( t ) R ( t , s )$ ， $R ( s , s ) = I$ with $A ( t ) = \partial f / \partial y ( t , y ( t ) )$ Theintegral over $R ( t _ { 0 } +$ $h , s ) r ( s )$ givesa $O ( h ^ { 2 s + 3 } )$ contribution.The main idea now is toapply the quadratureformula $( b _ { i } , c _ { i } ) _ { i = 1 } ^ { s }$ to the integral over $g ( s ) = R ( t _ { 0 } + h , s ) \delta ( s )$ because the defect $\delta ( s )$ vanishes at the collocation points $t _ { 0 } + c _ { i } h$ for $i = 1 , \dots , s$ ,thisgives zeroas the numerical result.Thus,the integral is equal to the quadrature error,which is bounded by $h ^ { p + 1 }$ timesa bound of the $\boldsymbol { p }$ th derivative of the function $g ( s )$ This derivative isbounded independentlyof $h$ ,becausebyLemma 1.6allderivatives of thecollcation polynomial are bounded uniformlyas $h  0$ Since,anyway, $p \leq 2 s$ ,weget $y _ { 1 } - y ( t _ { 0 } + h ) = \mathcal { O } ( h ^ { p + 1 } )$ from (1.14). □

Lemma1.6.Thecollocation polynomial $u ( t )$ is an approximation of order s to the exact solution of(1.1)onthewhole interval,i.e.,

$$
\| u ( t ) - y ( t ) \| \le C \cdot h ^ { s + 1 } \qquad f o r \quad t \in [ t _ { 0 } , t _ { 0 } + h ]
$$

and for sufficiently small $h$ .

Moreover,thederivativesof $u ( t )$ satisfy for $t \in [ t _ { 0 } , t _ { 0 } + h ]$

$$
\| u ^ { ( k ) } ( t ) - y ^ { ( k ) } ( t ) \| \le C \cdot h ^ { s + 1 - k } \qquad f o r \quad k = 0 , \ldots , s .
$$

Proof. The collocation polynomial satisfies

$$
\dot { u } ( t _ { 0 } + \tau h ) = \sum _ { i = 1 } ^ { s } f \Bigl ( t _ { 0 } + \bar { c } _ { i } h , u ( t _ { 0 } + c _ { i } h ) \Bigr ) \ell _ { i } ( \tau ) ,
$$

while the exact solution of (1.1) satisfies

$$
\dot { y } ( t _ { 0 } + \tau h ) = \sum _ { i = 1 } ^ { s } f \Big ( t _ { 0 } + c _ { i } h , y ( t _ { 0 } + c _ { i } h ) \Big ) \ell _ { i } ( \tau ) + h ^ { s } \underline { { E } } ( \tau , h ) ,
$$

where the interpolation error $E ( \tau , h )$ is bounded by $\operatorname* { m a x } _ { t \in [ t _ { 0 } , t _ { 0 } + h ] } \| y ^ { ( s + 1 ) } ( t ) \| / s !$ anditsderivatives satisfy

$$
\| E ^ { ( k - 1 ) } ( \tau , h ) \| \le \operatorname* { m a x } _ { t \in [ t _ { 0 } , t _ { 0 } + h ] } \frac { \| y ^ { ( s + 1 ) } ( t ) \| } { ( s - k + 1 ) ! } .
$$

Thisfollows from the fact that,byRolle's theorem,thedifferentiated polynomial $\begin{array} { r } { \sum _ { i = 1 } ^ { s } f \big ( t _ { 0 } + c _ { i } h , y ( t _ { 0 } + c _ { i } h ) \big ) \ell _ { i } ^ { ( k - 1 ) } ( \tau ) } \end{array}$ can beinterpretedastheinterpolation polynomialof $h ^ { k - 1 } y ^ { ( k ) } ( t _ { 0 } + \tau h )$ at $s - k + 1$ points lying in $[ t _ { 0 } , t _ { 0 } + h ]$ Integrating thedifference of the above two equations gives

$$
y ( t _ { 0 } + \tau h ) - u ( t _ { 0 } + \tau h ) = h \sum _ { i = 1 } ^ { s } \Delta f _ { i } \int _ { 0 } ^ { \tau } \ell _ { i } ( \sigma ) d \sigma + h ^ { s + 1 } \int _ { 0 } ^ { \tau } E ( \sigma , h ) d \sigma
$$

with $\begin{array} { r } { \varDelta f _ { i } = f \big ( t _ { 0 } + c _ { i } h , y ( t _ { 0 } + c _ { i } h ) \big ) - f \big ( t _ { 0 } \ddag c _ { i } h , u ( t _ { 0 } + c _ { i } h ) \big ) , } \end{array}$ Usinga Lipschitz condition for $f ( t , y )$ ,thisrelation yields

$$
\operatorname* { m a x } _ { t \in [ t _ { 0 } , t _ { 0 } + h ] } \| y ( t ) - u ( t ) \| \leq h C L \operatorname* { m a x } _ { t \in [ t _ { 0 } , t _ { 0 } + h ] } \| y ( t ) - u ( t ) \| + C o n s t \cdot h ^ { s + 1 } ,
$$

implying the statement（1.15)for suficiently small $h > 0$ .

The proof of the second statement follows from

$$
\Big ( y ^ { ( k ) } ( t _ { 0 } + \tau h ) - u ^ { ( k ) } ( t _ { 0 } + \tau h ) \Big ) = h \sum _ { i = 1 } ^ { s } \varDelta f _ { i } \ell _ { i } ^ { ( k - 1 ) } ( \tau ) + h ^ { s + 1 } \varSigma ^ { ( k - 1 ) } ( \tau , h ^ { ( k ) } ( t _ { 0 } + \tau h ) )
$$

by using aLipschitz condition for $f ( t , y )$ and the estimate(1.15).

# II.1.3 Gaussand Lobatto Collocation

Gauss Methods.If we take $c _ { 1 } , \ldots , c _ { s }$ as the zeros of the sth shifted Legendre polynomial

$$
\frac { d ^ { s } } { d x ^ { s } } \Big ( x ^ { s } ( x - 1 ) ^ { s } \Big ) ,
$$

theinterpolatory quadrature formula has order $p = 2 s$ ,andbyTheorem 1.5,the Runge-Kutta (orcollocation） method based on these nodes has the same order $2 s$ For $s = 1$ weobtain the implicit midpoint rule.The Runge-Kutta coefficients for $s = 2$ （themethodofHammer&Hollingsworth 1955）and $s = 3$ are given in Table1.1.Theproof of the orderproperties for general $s$ wasasensational resultof Butcher(1964a).At that time these methodswereconsidered,at least by the editors ofMath.ofComput.,tobepurelyacademicwithoutany practical value;5years later their $A$ -stabilitywasdiscovered,12yearslatertheir $B$ -stability,and25years latertheir symplecticity.Thus,of all thepapersinissueNo.85ofMath.ofComput., the one most important to us is the one for which publication was the most difficult.

Table1.1.Gauss methods of order4 and 6   

<table><tr><td>1-21-2 √3 6 +</td><td>14 1 √ + 6</td><td>4 √ 6 1</td><td colspan="2"></td></tr><tr><td>√15</td><td>1-2 5 2</td><td>1 2 √15</td><td>5</td><td>√15</td></tr><tr><td>1 10 112</td><td>3 √15 ×</td><td>2</td><td>15 36</td><td>30 √15</td></tr><tr><td>1 V15</td><td>24 √15</td><td></td><td>5 36</td><td>24</td></tr><tr><td>3 X 10</td><td>X 30</td><td>2 √15 + 15</td><td></td><td>5</td></tr><tr><td></td><td>5 18</td><td>4</td><td></td><td>36 5</td></tr></table>

Radau Methods.Radau quadrature formulas have the highest possible order, $2 s - 1$ ,amongquadratureformulaswith either $c _ { 1 } = 0$ or $c _ { s } = 1 ,$ Thecorrespondingcollocation methods for $c _ { s } = 1$ arecalled Radau IIA methods.Theyplayan important rolein the integration of stiff differential equations(see Hairer&Wanner (1996),Sect.IV.8).However,they lack both symmetryandsymplecticity,properties thatwill be the subjects of laterchapters in this book.

Lobatto IIA Methods.Lobatto quadrature formulas have the highest possible orderwith $c _ { 1 } = 0$ and $c _ { s } = 1$ Under these conditions,the nodes must be the zeros of

$$
{ \frac { d ^ { s - 2 } } { d x ^ { s - 2 } } } \Bigl ( x ^ { s - 1 } ( x - 1 ) ^ { s - 1 } \Bigr )
$$

and the quadrature order is $p = 2 s - 2$ .The corresponding collocation methods are called,for historical reasons,Lobatto IA methods.For $s = 2$ we have the implicit trapezoidal rule.The coefficients for $s = 3$ and $s = 4$ are given in Table 1.2.

Table1.2.Lobatto IIIA methods of order 4and 6   

<table><tr><td rowspan="5">0 0</td><td></td></tr><tr><td>112 2 113 1 2</td></tr><tr><td>1 6 3</td></tr><tr><td>6 1 23 1 6</td></tr><tr><td>6</td></tr><tr><td>0 0</td><td>0 -1+√5</td></tr><tr><td>5-√5 11+√5</td><td>25-√5 25-13√5</td></tr><tr><td>10 120</td><td>120</td></tr><tr><td>5+√5 11-√5</td><td>120 120 25+√5</td></tr><tr><td>25+13√5 120 120</td><td>-1-√5</td></tr><tr><td>10 1</td><td>120 120</td></tr><tr><td>5 1</td><td>5 1</td></tr><tr><td>12 12</td><td>12 12</td></tr><tr><td>12 5</td><td>12 1</td></tr><tr><td>12</td><td>12</td></tr></table>

# II.1.4 Discontinuous Collocation Methods

Collocation methodsallow,aswe have seen above,a very elegant proof of their orderproperties.By similar ideas,theyalsoadmit strikinglysimpleproofs for their $A$ -and $B$ -stabilityaswellas for symplecticity,our subject in Chap.VI.However, notall method classes are ofcollocation type.It is therefore interesting todefine a modification of the collocation idea,which allows us to extend all the above proofs tomuch wider classesof methods.Thisdefinitionwill also lead,later,to important classesofpartitioned methods.

Definition 1.7. Let $c _ { 2 } , \ldots , c _ { s - 1 }$ bedistinct real numbers (usually $0 \leq c _ { i } \leq 1$ ,andlet $b _ { 1 } , b _ { s }$ betwoarbitraryreal numbers.The correspondingdiscontinuous collocation method is then defined viaapolynomial ofdegree $s - 2$ satisfying

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/aa828b44a813d2b85b0ecacc16be78d1c8b61bfe8edaf88617a96fd5e473f1fb.jpg)

$$
\begin{array} { r l r } & { u ( t _ { 0 } ) = y _ { 0 } - h b _ { 1 } \big ( \dot { u } ( t _ { 0 } ) - f ( t _ { 0 } , u ( t _ { 0 } ) ) \big ) } & { \quad \mathrm { ~ } ^ { \mathrm { e } _ { 0 } } , \quad \quad \mathrm { ~ } ^ { \mathrm { ~ } t _ { 0 } ( \dot { } \tau \dot { u } / \tau ^ { a } ) } } \\ & { \dot { u } ( t _ { 0 } + c _ { i } h ) = \check { f } \big ( t _ { 0 } + c _ { i } h , u ( t _ { 0 } + c _ { i } h ) \big ) , } & { \dot { u } = 2 , \dot { v } \dot { v } \dot { v } - 1 , } \\ & { y _ { 1 } = u ( t _ { 1 } ) - h b _ { s } \big ( \dot { u } ( t _ { 1 } ) - f ( t _ { 1 } , u ( t _ { 1 } ) ) \big ) . } & \end{array}
$$

The figure gives a geometric interpretation of the correction term in the first and third formulas of(1.18).Themotivation for this definitionwill becomeclear in the proof of Theorem 1.9 below.Our first result shows that discontinuous collocation methods are equivalent to implicit Runge-Kutta methods.

Theorem1.8.ThediscontinuouscollocationmethodofDefinition1.7isequivalent toans-stageRunge-Kutta method(1.4）with coefficients determined by $c _ { 1 } = 0$ , $c _ { s } = 1$ ,and

$$
\begin{array} { l } { { a _ { i 1 } = b _ { 1 } , \qquad a _ { i s } = 0 \qquad f o r \ i = 1 , \ldots , s , } } \\ { { C ( s - 2 ) \qquad a n d \qquad B ( s - 2 ) , } } \end{array}
$$

with theconditions $C ( q )$ and $B ( p )$ of(1.11).

Proof.Asintheproof of Theorem1.4weput $i = 2 , \ldots , s - 1 )$ sothat $\begin{array} { r } { \dot { u } ( t _ { 0 } + \tau h ) = \sum _ { j = 2 } ^ { s - 1 } k _ { j } { \cdot } \ell _ { j } ( \tau ) } \end{array}$ $k _ { i } : = \dot { u } ( t _ { 0 } + c _ { i } h )$ bytheLagrangeinerpolaion (this time for formula.Here, $\ell _ { j } ( \tau )$ correspondsto $c _ { 2 } , \ldots , c _ { s - 1 }$ andisapolynomial ofdegree $s { - 3 }$ . Byintegration and using thedefinition of $u ( t _ { 0 } )$ weget

$$
\begin{array} { l } { { u ( t _ { 0 } + c _ { i } h ) ~ = ~ u ( t _ { 0 } ) + h \displaystyle \sum _ { j = 2 } ^ { s - 1 } k _ { j } \int _ { 0 } ^ { c _ { i } } \ell _ { j } ( \tau ) d \tau } } \\ { { ~ = ~ y _ { 0 } + h b _ { 1 } k _ { 1 } + h \displaystyle \sum _ { j = 2 } ^ { s - 1 } k _ { j } \left( \int _ { 0 } ^ { c _ { i } } \ell _ { j } ( \tau ) d \tau - b _ { 1 } \ell _ { j } ( 0 ) \right) } } \end{array} ,
$$

with $k _ { 1 } = f ( y _ { 0 } )$ Inserted into(1.18)this givesthe first formulaofthe Runge-Kutta equation (1.4）with $\begin{array} { r } { a _ { i j } = \int _ { 0 } ^ { c _ { i } } \ell _ { j } ( \tau ) d \tau - b _ { 1 } \ell _ { j } ( 0 ) , } \end{array}$ As for collocation methods,one checksthat the $a _ { i j }$ areuniquely determined by the condition $C ( s - 2 ) .$ Theformula for $y _ { 1 }$ is obtained similarly. □

Table1.3.Survey of discontinuous collocation methods   

<table><tr><td>type</td><td>characteristics</td><td>promineni examples</td></tr><tr><td>b1=0,b=0 b=0，bs≠0 b1≠0,bs=0 b≠0,b≠0</td><td>（s-2)-stage collocation （s-1)-stage with ais =0 (s-1)-stage with aii=b1 s-stage withai1=b1,aig=0</td><td>Gauss,Radau IIA,Lobatto IIIA methods ofButcher（1964b） Radau IA,Lobatto IIIC LobattoIIIB</td></tr></table>

If $b _ { 1 } = 0$ in Definition 1.7,the entire first columnin the Runge-Kutta tableau vanishes,so that the first stage can beremoved,which leadstoan equivalent method with $s - 1$ stages.Similarly,if $b _ { s } = 0$ ,wecan remove the last stage.Therefore,we haveall classes ofmethods,which are“continuouseither to theleft,orto theright, or on both sides,as special cases in our definition.

In the case where $b _ { 1 } = b _ { s } = 0$ ,the discontinuous collocation method (1.18) is equivalent to the $\left( s - 2 \right)$ -stagecollocation method based on $c _ { 2 } , \ldots , c _ { s - 1 }$ (see Table 1.3).The methodswith $b _ { s } = 0$ but $b _ { 1 } \neq 0$ ,which include theRadau IAand

Table1.4.Lobatto IIIBmethods of order 4and 6   

<table><tr><td rowspan="2" colspan="3"></td><td rowspan="2"></td><td rowspan="2">0</td><td></td><td>-1-√5 24</td><td rowspan="2">-1+√5</td></tr><tr><td>12</td><td></td></tr><tr><td rowspan="2">0</td><td rowspan="2"></td><td></td><td rowspan="2">0</td><td>5-√5 10</td><td>1</td><td>25+√5</td><td>25-13√5</td><td rowspan="2">0</td></tr><tr><td></td><td></td><td>12</td><td>120</td><td>120</td></tr><tr><td rowspan="2">1</td><td>1</td><td></td><td rowspan="2">0</td><td>5+√5</td><td>1</td><td>25+13√5</td><td>25-√5</td><td rowspan="2">0</td></tr><tr><td></td><td>1</td><td>10</td><td>12</td><td>120</td><td>120</td></tr><tr><td rowspan="2">1</td><td>1</td><td></td><td rowspan="2">0</td><td></td><td>1</td><td>11-√5</td><td></td><td rowspan="2">0</td></tr><tr><td>6</td><td>5</td><td>1</td><td></td><td></td><td>11+√5</td></tr><tr><td rowspan="2"></td><td></td><td>2</td><td rowspan="2"></td><td rowspan="2"></td><td>12</td><td>24</td><td>24</td><td></td></tr><tr><td>1</td><td>1</td><td>1</td><td>5 12</td><td>5</td><td>12</td></tr></table>

Lobatto IIIC methods,are of interest for the solution of stiff differential equations (Hairer&Wanner 1996).The methods with $b _ { 1 } = 0$ but $b _ { s } \neq 0$ ,introduced by Butcher(1964a,1964b),are of historical interest.Theywere thought tobe computationally attractive,because their last stageis explicit.In thecontext of geometric integration,much moreimportant are methods forwhich both $b _ { 1 } \neq 0$ and $b _ { s } \neq 0$

Lobatto IIIBMethods(Table 1.4).We consider the quadrature formulaswhose nodes are the zeros of(1.17).We have $c _ { \mathrm { I } } = 0$ and $c _ { s } = 1$ Based on $c _ { 2 } , \ldots , c _ { s - 1 }$ and $b _ { 1 } , b _ { s }$ we consider the discontinuous collocation method.This class of methods is calledLobatto IIB (Ehle 1969),and itplaysan important roleingeometric integration in conjunction with theLobatto IIIA methods of Sect.II.1.3(see TheoremIV.2.3andTheoremVI.4.5).Thesemethodsare of order $2 s - 2$ as the following result shows.

Theorem1.9 (Superconvergence). The discontinuous collcation method ofDefinition1.7 hasthe sameorderastheunderlyingquadrature formula.

Proof.We follow the lines of the proof of Theorem1.5.With the polynomial $u ( t )$ ofDefinition 1.7,and with thedefect

$$
\delta ( t ) : = \dot { u } ( t ) - f \big ( t , u ( t ) \big )
$$

weget(1.13)after linearization.Thevariation ofconstants formula then yields

$$
\begin{array} { r l } { u ( t _ { 0 } + h ) - y ( t _ { 0 } + h ) } & { = \ R ( t _ { 0 } + h , t _ { 0 } ) \big ( u ( t _ { 0 } ) - y _ { 0 } \big ) } \\ & { + \ \displaystyle \int _ { t _ { 0 } } ^ { t _ { 0 } + h } R ( t _ { 0 } + h , s ) \Big ( \delta ( s ) + r ( s ) \Big ) \ d s , } \end{array}
$$

which corresponds to(1.14)if $u ( t _ { 0 } ) = y _ { 0 }$ .Asaconsequence ofLemma1.10below (with $k = 0$ ）,theintegral over $R ( t _ { 0 } + h , s ) r ( s )$ givesa ${ \mathcal { O } } ( h ^ { 2 s - 1 } )$ contribution. Since the defect $\delta ( t _ { 0 } + c _ { i } h )$ vanishes only for $i = 2 , \ldots , s - 1$ ,anapplication of the quadrature formula to $R ( t _ { 0 } + h , s ) \delta ( s )$ yields $h b _ { 1 } R ( t _ { 0 } + h , t _ { 0 } ) \delta ( t _ { 0 } ) + h b _ { s } \delta ( t _ { 0 } + h )$ in addition to thequadrature error,which is ${ \mathcal { O } } ( h ^ { p + 1 } ) .$ Collecting terms suitably,we obtain

$$
\begin{array} { l } { { u ( t _ { 1 } ) - h b _ { s } \delta ( t _ { 1 } ) - y ( t _ { 1 } ) ~ = ~ R ( t _ { 1 } , t _ { 0 } ) \big ( u ( t _ { 0 } ) + h b _ { 1 } \delta ( t _ { 0 } ) - y _ { 0 } \big ) } } \\ { { { } } } \\ { { + { \cal O } ( h ^ { p + 1 } ) + { \cal O } ( h ^ { 2 s - 1 } ) , } } \end{array}
$$

which,after using the definitions of $u ( t _ { 0 } )$ and $u ( t _ { 1 } )$ ,proves $y _ { 1 } - y ( t _ { 1 } ) = \mathcal { O } ( h ^ { p + 1 } ) +$ ${ \mathcal { O } } ( h ^ { 2 s - 1 } )$ . □

Lemma1.10.Thepolynomial $u ( t )$ ofthe discontinuous collocation method(1.18) satisfies for $t \in [ t _ { 0 } , t _ { 0 } + h ]$ andfor sufficiently small $h$

$$
\| u ^ { ( k ) } ( t ) - y ^ { ( k ) } ( t ) \| \le C \cdot h ^ { s - 1 - k } \qquad f o r \quad k = 0 , \ldots , s - 2 ,
$$

Proof.Theproof isessentially the sameasthat forLemma 1.6.In the formulas for $\dot { u } ( t _ { 0 } + \tau h )$ and $\dot { y } ( t _ { 0 } + \tau h )$ ,thesum hasto be taken from $i = 2$ to $i = s - 1$ . Moreover,all $h ^ { s }$ become $h ^ { s - 2 }$ .In（1.16)one has an additional term

$$
y _ { 0 } - u ( t _ { 0 } ) = h b _ { 1 } \big ( \dot { u } ( t _ { 0 } ) - f ( t _ { 0 } , u ( t _ { 0 } ) ) \big ) ,
$$

which,however,is just an interpolation error of size $\mathcal { O } ( h ^ { s - 1 } )$ and can beincluded in $C o n s t \cdot h ^ { s - 1 }$ . □

# II.2Partitioned Runge-Kutta Methods

Someinteresting numerical methods introduced in Chap.I (symplectic Euler and theStormer-Verlet method） do not belong to the class of Runge-Kutta methods. They are important examples of so-called partitioned Runge-Kutta methods.Inthis section we considerdifferential equations in the partitioned form

$$
\dot { y } = f ( y , z ) , \qquad \dot { z } = g ( y , z ) ,
$$

where $y$ and $z$ may be vectors of different dimensions.

# II.2.1Definitionand First Examples

Theidea isto take two different Runge-Kutta methods,and to treat the $y$ -variables with the first method $( a _ { i j } , b _ { i } )$ ,andthe $z$ -variableswith thesecond method $( \widehat { a } _ { i j } , \widehat { b } _ { i } )$ .

Definition 2.1.Let $b _ { i } , a _ { i j }$ and $\widehat { b } _ { i } , \widehat { a } _ { i j }$ be thecoefficients of two Runge-Kutta methods.Apartitioned Runge-Kutta method for the solution of(2.1) is given by

$$
\begin{array} { r c l } { { k _ { i } } } & { { = } } & { { \displaystyle f \Big ( y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } , z _ { 0 } + h \sum _ { j = 1 } ^ { s } \widehat { a } _ { i j } \ell _ { j } \Big ) , } } \\ { { \ell _ { i } } } & { { = } } & { { \displaystyle g \Big ( y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } , z _ { 0 } + h \sum _ { j = 1 } ^ { s } \widehat { a } _ { i j } \ell _ { j } \Big ) , } } \\ { { y _ { 1 } } } & { { = } } & { { \displaystyle y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } , \qquad z _ { 1 } = z _ { 0 } + h \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } \ell _ { i } . } } \end{array}
$$

Methods of this typewere originallyproposedbyHoferin 1976and byGriepentrogin1978 forproblemswith stiffand nonstiff parts(seeHairer,Norsett&Wanner (1993),Sect.II.15).Their importance for Hamiltoniansystems (see the examples of Chap.I) hasbeen discovered only in the last decade.

Aninteresting example is the symplectic Eulermethod (I.1.9),where the implicit Euler method $b _ { 1 } = 1 , a _ { 1 1 } = 1$ iscombined with the explicit Euler method $\widehat { b } _ { 1 } \ = \ 1 , \widehat { a } _ { 1 1 } \ = \ 0$ .The Stormer-Verlet method(I.1.17) isof the form(2.2）with coefficients given in Table 2.1.

The theory of Runge-Kutta methods can beextended ina straightforward manner to partitioned methods.Since (2.2) is a one-step method $( y _ { 1 } , z _ { 1 } ) = \varPhi _ { h } ( y _ { 0 } , z _ { 0 } )$ ， theDefinition 1.2of the order applies directly.Considering problems $\dot { y } ~ = ~ f ( y )$ ， $\dot { z } = g ( z )$ without any coupling terms,we see that the order of(2.2)cannot exceed $\operatorname* { m i n } ( p , { \widehat { p } } )$ ,where $p$ and $\widehat { p }$ are theorders of the two methods.

Conditions for Order Two.Expanding the exact solution of(2.1) and the numerical solution(2.2)into Taylor series,we see that the methodis of order2if the coupling conditions

$$
\begin{array} { r l r } { \sum _ { i j } b _ { i } \widehat { a } _ { i j } = 1 / 2 , } & { { } } & { \sum _ { i j } \widehat { b } _ { i } a _ { i j } = 1 / 2 } \end{array}
$$

aresatisfied inaddition to theusual Runge-Kutta order conditions for order2.The method of Table2.1 satisfiestheseconditions,anditistherefore of order2.Wealso remark that(2.3) isautomatically satisfied bypartitioned methodsthatarebased on the same quadrature nodes,i.e.,

$$
c _ { i } = { \widehat { c } } _ { i } \qquad { \mathrm { f o r ~ a l l ~ } } i
$$

where,as usual, $c _ { i } = \textstyle \sum _ { j } a _ { i j }$ and $\begin{array} { r } { \widehat { c } _ { i } = \sum _ { j } \widehat { a } _ { i j } . } \end{array}$

Conditions forOrder Three.The conditions for order threealready becomequite complicated,unless(2.4) is satisfied.In this case,we obtain the additional conditions

$$
\begin{array} { r } { \sum _ { i j } b _ { i } \widehat { a } _ { i j } c _ { j } = 1 / 6 , \qquad \sum _ { i j } \widehat { b } _ { i } a _ { i j } c _ { j } = 1 / 6 . } \end{array}
$$

Theorder conditions for higher order will be discussed in Sect.III.2.2.It turns out that the number of coupling conditions increases very fast with order,and the proofs forhigh orderare often very cumbersome.There is,however,avery elegant proof of the order for the partitioned method which is the most important one in connection with"geometric integration”,aswe shall see now.

# II.2.2 Lobatto IIIA-IIIB Pairs

Thesemethods generalize the Stormer-Verletmethod toarbitrary order.Indeed,the leftmethod ofTable2.1is thetrapezoidal rule,which is theLobatto IIA method with $s = 2$ ,andthemethod totheright isequivalent to the midpoint ruleand,apart from the values of the $c _ { i }$ ,is theLobatto IIIB method with $s = 2$ Sun（1993b）and Jay（1996)discovered that for general $s$ the combination of the Lobatto IA and IIB methods are suitable for Hamiltonian systems.The coefficients of themethods for $s = 3$ aregiven in Table 2.2.Using theidea of discontinuous collocation,we giveadirect proof of the order for this pair of methods.

Table2.2.Coefficientsof the3-stageLobattoIIA-IB pair   

<table><tr><td>0 1/2</td><td>0 0 0 5/24 1/3 -1/24</td><td>0 1/2</td><td>1/6 -1/6 | 0 1/6 1/3 0</td></tr><tr><td>1</td><td>1/6 2/3 1/6</td><td>1 1/6</td><td>5/6 0</td></tr><tr><td></td><td>1/6 2/3 1/6</td><td></td><td>1/6 2/3 1/6</td></tr></table>

Theorem2.2.Thepartitioned Runge-Kutta methodcomposedof thes-stage Lobatto IIA andthes-stageLobattoIIBmethod,isoforder $2 s - 2$ ..

ProofLet $c _ { 1 } = 0 , c _ { 2 } , \ldots , c _ { s - 1 } , c _ { s } = 1$ and $b _ { 1 } , \ldots , b _ { s }$ be the nodes and weights of theLobatto quadrature.The partitioned Runge-Kutta method based on the Lobatto IIIA-IIIB pair can be interpreted as the discontinuous collocation method

$$
\begin{array} { r l } & { u ( t _ { 0 } ) = y _ { 0 } } \\ & { v ( t _ { 0 } ) = z _ { 0 } - h b _ { 1 } \big ( \dot { v } ( t _ { 0 } ) - g ( u ( t _ { 0 } ) , v ( t _ { 0 } ) ) \big ) } \\ & { \dot { u } ( t _ { 0 } + c _ { i } h ) = f \big ( u ( t _ { 0 } + c _ { i } h ) , v ( t _ { 0 } + c _ { i } h ) \big ) , \qquad i = 1 , \dots , s } \\ & { \dot { v } ( t _ { 0 } + c _ { i } h ) = g \big ( u ( t _ { 0 } + c _ { i } h ) , v ( t _ { 0 } + c _ { i } h ) \big ) , \qquad i = 2 , \dots , s - 1 } \\ & { y _ { 1 } = u ( t _ { 1 } ) } \\ & { z _ { 1 } = v ( t _ { 1 } ) - h b _ { s } \big ( \dot { v } ( t _ { 1 } ) - g ( u ( t _ { 1 } ) , v ( t _ { 1 } ) ) \big ) , } \end{array}
$$

where $u ( t )$ and $v ( t )$ arepolynomials of degree $s$ and $s - 2$ ,respectively.This is seen asin the proofsof Theorem 1.4and Theorem 1.8.The superconvergence (order $2 s \textrm { -- } 2 )$ isobtained with exactly the same proof as for Theorem 1.9,where the functions $u ( t )$ and $y ( t )$ have to be replaced with $( u ( t ) , v ( t ) ) ^ { T }$ and $( y ( t ) , z ( t ) ) ^ { T } ,$ etc.Instead ofLemma 1.10 weuse the estimates (for $t \in [ t _ { 0 } , t _ { 0 } + h ] )$

$$
\begin{array} { r l } & { \| u ^ { ( k ) } ( t ) - y ^ { ( k ) } ( t ) \| \ \leq \ c \cdot h ^ { s - k } \quad \mathrm { f o r } \quad k = 0 , \ldots , s , } \\ & { \| v ^ { ( k ) } ( t ) - z ^ { ( k ) } ( t ) \| \ \leq \ c \cdot h ^ { s - 1 - k } \quad \mathrm { f o r } \quad k = 0 , \ldots , s - 2 , } \end{array}
$$

which can be proved by following the lines of the proofsofLemma 1.6and Lemma 1.10. □

# I1.2.3Nystrom Methods

Dabis jetzt die direkte Anwendung der Rungeschen Methode auf den wichtigen Fall von Differentialgleichungen zweiter Ordnung nicht behandeltwar... (E.J.Nystrom1925)

Second-order differential equations

$$
\ddot { \boldsymbol y } = \boldsymbol g ( t , \boldsymbol y , \dot { \boldsymbol y } )
$$

forman important class of problems.Most of the differential equationsin Chap.I are of this form (e.g.,theKeplerproblem,the outer solar system,problems in moleculardynamics).This ismainlydue to Newton's law that forces areproportional tosecond derivatives(acceleration). Introducing a new variable $z = y$ forthe first derivative,the problem(2.7) becomes equivalent to the partitioned system

$$
\dot { y } = z , \qquad \dot { z } = g ( t , y , z ) .
$$

A partitioned Runge-Kutta method (2.2)applied to this system yields

$$
\begin{array} { l } { { k _ { i } ~ = ~ z _ { 0 } + h { \displaystyle \sum _ { j = 1 } ^ { s } } \hat { a } _ { i j } \ell _ { j } , } } \\ { { \ell _ { i } ~ = ~ g \Big ( t _ { 0 } + c _ { i } h , ~ y _ { 0 } + h { \displaystyle \sum _ { j = 1 } ^ { s } } a _ { i j } k _ { j } , z _ { 0 } + h { \displaystyle \sum _ { j = 1 } ^ { s } } \hat { a } _ { i j } \ell _ { j } \Big ) , } } \\ { { y _ { 1 } ~ = ~ y _ { 0 } + h { \displaystyle \sum _ { i = 1 } ^ { s } } b _ { i } k _ { i } , ~ z _ { 1 } ~ = ~ z _ { 0 } + h { \displaystyle \sum _ { i = 1 } ^ { s } } \hat { b } _ { i } \ell _ { i } . } } \end{array}
$$

Ifwe insert the formula for $k _ { i }$ into the others,we obtain Definition 2.3 with

$$
\overline { { { a } } } _ { i j } = \sum _ { k = 1 } ^ { s } a _ { i k } \widehat { a } _ { k j } , \qquad \overline { { { b } } } _ { i } = \sum _ { k = 1 } ^ { s } b _ { k } \widehat { a } _ { k i } .
$$

Definition 2.3.Let $c _ { i } , b _ { i } , \overline { { a } } _ { i j }$ and $\widehat { b } _ { i } , \widehat { a } _ { i j }$ bereal coefficients.A Nystrommethod for the solution of(2.7) is given by

$$
\begin{array} { l } { { \displaystyle \ell _ { i } ~ = ~ g \Big ( t _ { 0 } + c _ { i } h , ~ y _ { 0 } + c _ { i } h \ddot { y } _ { 0 } + h ^ { 2 } \sum _ { j = 1 } ^ { s } \overline { { { a } } } _ { i j } \ell _ { j } , \dot { y } _ { 0 } + h \sum _ { j = 1 } ^ { s } \overline { { { a } } } _ { i j } \ell _ { j } \Big ) , } } \\ { { \displaystyle y _ { 1 } ~ = ~ y _ { 0 } + h \dot { y } _ { 0 } + h ^ { 2 } \sum _ { i = 1 } ^ { s } \overline { { { b } } } _ { i } \ell _ { i } , ~ \qquad \dot { y } _ { 1 } ~ = ~ \dot { y } _ { 0 } + h \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } \ell _ { i } . } } \end{array}
$$

For the important special case $\ddot { y } = g ( t , y )$ ,where the vector field does not depend on the velocity,the coefficients $\hat { a } _ { i j }$ need not be specified.ANystrom method is oforder $p$ if $y _ { 1 } - y ( t _ { 0 } + h ) = \mathcal { O } ( h ^ { p + 1 } )$ and $\dot { y } _ { 1 } - \dot { y } ( t _ { 0 } + h ) = \mathcal { O } ( h ^ { p + 1 } ) .$ Itis not sufficient to consider $y _ { 1 }$ alone.The order conditionswill be discussed in Sect.III.2.3.

Notice that the Stormer-Verlet scheme(I.1.17) isa Nystrommethod for problems of the form $\ddot { y } = g ( t , y )$ Wehave $s = 2$ and thecoefficients are $c _ { 1 } = 0 , c _ { 2 } = 1$ ， $\overline { { a } } _ { 1 1 } = \overline { { a } } _ { 1 2 } = \overline { { a } } _ { 2 2 } = 0$ , $\overline { { a } } _ { 2 1 } = 1 / 2$ , $b _ { 1 } = 1 / 2$ , $\bar { b } _ { 2 } = 0$ ,and $\hat { b } _ { 1 } = \hat { b } _ { 2 } = 1 / 2$ With $\begin{array} { r } { q _ { n + 1 / 2 } = q _ { n } + \frac { h } { 2 } v _ { n + 1 / 2 } } \end{array}$ the step $( q _ { n - 1 / 2 } , v _ { n - 1 / 2 } ) \longmapsto ( q _ { n + 1 / 2 } , v _ { n + 1 / 2 } )$ of (L.1.17) becomes a one-stage Nystrom method with $c _ { 1 } = 1 / 2$ , $\overline { { a } } _ { 1 1 } = 0$ , $\overline { { b } } _ { 1 } = \widehat { b } _ { 1 } = 1$ .

# II.3The Adjoint of a Method

Weshall seein Chap.V that symmetric numerical methods have many importantproperties.The key for understandingsymmetry isthe concept of the adjoint method.

The flow $\varphi _ { t }$ of an autonomous differential equation

$$
\dot { y } = f ( y ) , \qquad y ( t _ { 0 } ) = y _ { 0 }
$$

satisfies $\varphi _ { - t } ^ { - 1 } = \varphi _ { t } .$ Thispropertyisnotingeneral,aredbytheoeeap $\phi _ { h }$ ofanumerical method.Anillustration ispresented in the upper picture of Fig.3.1(a),where we see that the one-step map $\phi _ { h }$ for the explicit Euler method isdifferent from the inverseof $\Phi _ { - h }$ ,which istheimplicit Eulermethod.

Definition3.1.Theadjointmethod $\varPhi _ { h } ^ { * }$ ofamethod $\phi _ { h }$ is the inverse map of the original method with reversed time step $- h$ ,i.e.,

$$
\varPhi _ { h } ^ { * } : = \varPhi _ { - h } ^ { - 1 }
$$

(see Fig.3.1(b)）.In other words, $y _ { 1 } = \varPhi _ { h } ^ { * } ( y _ { 0 } )$ is implicitly defined by $\bar { \Phi } _ { - h } ( y _ { 1 } ) =$ $y _ { 0 }$ Amethod forwhich $\Phi _ { h } ^ { * } = \Phi _ { h }$ is called symmetric.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/d0b52597b1829decc6ae57b37f8bd31226db489c637062a577ca6fa2e17b8e7f.jpg)  
Fig.3.1.Definition and properties of theadjoint method

Theconsideration of adjoint methods evolved independently from the study of symmetricintegrators(Stetter(1973),p.125,Wanner(1973))and fromtheaimof constructing and analyzing stiff integrators from explicit ones(Cash（1975）calls them“the backwardversion”which were the first example of mono-implicit methodsand Scherer(1977)calls them“reflected methods").

Theadjoint method satisfies the usual properties such as $( \varPhi _ { h } ^ { * } ) ^ { * } = \varPhi _ { h }$ and $\Phi _ { h } \circ$ $\varPsi _ { h } ) ^ { * } \ = \ \varPsi _ { h } ^ { * } \circ \varPhi _ { h } ^ { * }$ for any two one-step methods $\phi _ { h }$ and $\psi _ { h }$ .Theimplicit Euler method is theadjoint of the explicit Eulermethod.The implicit midpoint ruleis symmetric(see the lower picture of Fig.3.1(a)),and the trapezoidal rule and the Stormer-Verletmethod are alsosymmetric.

The following theorem shows that the adjoint method has the same order as the original method,and,withapossible sign change,also the same leading error term.

Theorem 3.2.Let $\varphi _ { t }$ be theexactflowof(3.1)and let $\varPhi _ { h }$ be a one-step method of orderp satisfying

$$
\Phi _ { h } ( y _ { 0 } ) = \varphi _ { h } ( y _ { 0 } ) + C ( y _ { 0 } ) h ^ { p + 1 } + \mathcal { O } ( h ^ { p + 2 } ) .
$$

Theadjoint method $\boldsymbol { \varPhi } _ { h } ^ { * }$ then has the same order pandwe have

$$
\begin{array} { r } { \Phi _ { h } ^ { * } ( y _ { 0 } ) = \varphi _ { h } ( y _ { 0 } ) + ( - 1 ) ^ { p } C ( y _ { 0 } ) h ^ { p + 1 } + \mathcal { O } ( h ^ { p + 2 } ) . } \end{array}
$$

Ifthemethodissymmetric,its(maximal) orderiseven.

ProofTheideaoftheproof isexhibitedindrawing(c）ofFig.3.1.Fromagiven initial value $y _ { 0 }$ wecompute $\varphi _ { h } ( y _ { 0 } )$ and $y _ { 1 } = \varPhi _ { h } ^ { * } ( y _ { 0 } )$ ,whosedifference $e ^ { * }$ isthe local error of $\phi _ { h } ^ { * } .$ This error is then“projected back”by $\Phi _ { - h }$ tobecome $e$ Wesee that $- e$ is the local error of $\phi _ { - h }$ ,i.e.,by hypothesis (3.3),

$$
e \equiv ( - 1 ) ^ { p } C ( \varphi _ { h } ( y _ { 0 } ) ) h ^ { p + 1 } + \mathcal { O } ( h ^ { p + 2 } ) .
$$

Since $\varphi _ { h } ( y _ { 0 } ) = y _ { 0 } + \mathcal { O } ( h )$ and $e = ( I + { O } ( h ) ) e ^ { * } ,$ it follows that

$$
e ^ { * } = ( - 1 ) ^ { p } C ( y _ { 0 } ) h ^ { p + 1 } + \mathcal { O } ( h ^ { p + 2 } )
$$

which proves (3.4).The statement forsymmetric methodsisan immediate consequence of this result,because $\varPhi _ { h } = \varPhi _ { h } ^ { * }$ implies $C ( y _ { 0 } ) = ( - 1 ) ^ { p } C ( y _ { 0 } )$ ,andtherefore $C ( y _ { 0 } )$ can be different from zero only for even $p$ . □

# II.4 Composition Methods

Theidea of composing methods has some tradition in several variants:composition ofdifferent Runge-Kutta methods with the same step size leading to the Butcher group,which is treated in Sect.III.1.3;cyclic composition of multistepmethods for breaking the“Dahlquist barrier”(see Stetter（1973）,p.216);composition oflow orderRunge-Kutta methods for increasing stability for stiff problems(Gentzsch& Schluter(1978),Iserles(1984)).In the following,we consider the composition ofa givenbasic one-stepmethod(and,eventually,itsadjointmethod)withdifferent step sizes.The aimisto increase the orderwhilepreserving some desirable properties of the basic method.This idea has mainly been developed in the papers of Suzuki (1990),Yoshida(1990),and McLachlan(1995).

Let $\phi _ { h }$ bea basic method and $\gamma _ { 1 } , \dots , \gamma _ { s }$ real numbers. Then we call its composition with step sizes $\gamma _ { 1 } h , \gamma _ { 2 } h , \ldots , \gamma _ { s } h ,$ i.e.,

$$
\varPsi _ { h } = \varPhi _ { \gamma _ { s } h } \circ \dots \circ \varPhi _ { \gamma _ { 1 } h } ,
$$

the corresponding composition method (see Fig.4.1(a)).

Theorem4.1.Let $\phi _ { h }$ bea one-stepmethodof orderp.If

$$
\begin{array} { r c l } { { \gamma _ { 1 } + . . . + \gamma _ { s } } } & { { = ~ 1 } } \\ { { \gamma _ { 1 } ^ { p + 1 } + . . . + \gamma _ { s } ^ { p + 1 } } } & { { = ~ 0 , } } \end{array}
$$

thenthecompositionmethod(4.1)isat least oforder $p + 1$ .

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/1ee4a15ad8d75a145eb785474d4f29b093e2e83551d317227e46005e1f58cedb.jpg)  
Fig.4.1.Composition of method $\varPhi _ { h }$ with three step sizes

Proof.Theproof ispresented inFig.4.1(b)for $s = 3 .$ It isverysimilartotheproof ofTheorem 3.2.Byhypothesis

$$
\begin{array} { l } { { e _ { 1 } = C ( y _ { 0 } ) \cdot \gamma _ { 1 } ^ { p + 1 } h ^ { p + 1 } + { \mathcal O } ( h ^ { p + 2 } ) } } \\ { { e _ { 2 } = C ( y _ { 1 } ) \cdot \gamma _ { 2 } ^ { p + 1 } h ^ { p + 1 } + { \mathcal O } ( h ^ { p + 2 } ) } } \\ { { e _ { 3 } = C ( y _ { 2 } ) \cdot \gamma _ { 3 } ^ { p + 1 } h ^ { p + 1 } + { \mathcal O } ( h ^ { p + 2 } ) . } } \end{array}
$$

We have,as before, $y _ { i } = y _ { 0 } + O ( h )$ and $E _ { i } = ( I + \mathcal { O } ( h ) ) e _ { i }$ for all $i$ and obtain, for $\sum \gamma _ { i } = 1$ ，

$$
y _ { 0 } ) - \varPsi _ { h } ( y _ { 0 } ) = E _ { 1 } + E _ { 2 } + E _ { 3 } = C ( y _ { 0 } ) ( \gamma _ { 1 } ^ { p + 1 } + \gamma _ { 2 } ^ { p + 1 } + \gamma _ { 3 } ^ { p + 1 } ) h ^ { p + 1 } + \mathcal { O } ( h ^ { p + 2 } )
$$

which shows that under conditions(4.2） the $O ( h ^ { p + 1 } )$ -termvanishes.

Example 4.2 (The TripleJump).Equations (4.2) have no real solution for odd $p$ Therefore,the order increase is only possible for even $p$ In thiscase,the smallest $s$ which allows asolution is $s = 3$ .We then have some freedom for solving the two equations.If we impose symmetry $\gamma _ { 1 } = \gamma _ { 3 }$ ,thenwe obtain(Creutz&Gocksch 1989,Forest1989,Suzuki 1990,Yoshida1990)

$$
\gamma _ { 1 } = \gamma _ { 3 } = \frac { 1 } { 2 - 2 ^ { 1 / ( p + 1 ) } } , \qquad \gamma _ { 2 } = - \frac { 2 ^ { 1 / ( p + 1 ) } } { 2 - 2 ^ { 1 / ( p + 1 ) } } .
$$

This procedure can be repeated:we start with asymmetric method of order 2,apply （4.4）with $p = 2$ to obtain order3;due to the symmetry ofthe $\gamma$ 'sthisnewmethod isin fact of order4(see Theorem 3.2).With this newmethod werepeat(4.4)with $p = 4$ and obtainasymmetric 9-stage compositionmethod of order6,thenwith $p = 6$ a27-stage symmetric composition method of order8,and so on.One obtains inthiswayanyorder,however,at the price ofa terrible zig-zagofthe step points (see Fig.4.2）.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/5ba6c0bf6cbf39acef9cc8103833a09c8bcc66e8d7c0ddd3ddd9f2c3a173820a.jpg)  
Fig.4.2.The TripleJumpof order 4and itsiterates of orders6and8

Example 4.3(Suzuki'sFractals).If one desires methodswith smallervalues of $\gamma _ { i }$ ,onehasto increaseseven more.Forexample,for $s = 5$ the best solution of （4.2) has the sign structure $+ + - + +$ with $\gamma _ { 1 } = \gamma _ { 2 }$ (see Exercise 7).This leads to （Suzuki 1990)

$$
\gamma _ { 1 } = \gamma _ { 2 } = \gamma _ { 4 } = \gamma _ { 5 } = \frac { 1 } { 4 - 4 ^ { 1 / ( p + 1 ) } } , \qquad \gamma _ { 3 } = - \frac { 4 ^ { 1 / ( p + 1 ) } } { 4 - 4 ^ { 1 / ( p + 1 ) } } .
$$

The repetition of this algorithm for $p = 2 , 4 , 6 , \ldots$ leads toa fractal structure of the step points(see Fig.4.3）.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/6870fc6058ca7bf5fa1fa6de094abdf7dc28135a4a168e6a5a8bc09c91eec55d.jpg)  
Fig.4.3.Suzuki's“fractal"composition methods

Compositionwith the AdjointMethod.Ifwe replace the composition (4.1) by the moregeneral formula

$$
\varPsi _ { h } = \varPhi _ { \alpha _ { s } h } \circ \varPhi _ { \beta _ { s } h } ^ { * } \circ \dots \circ \varPhi _ { \beta _ { 2 } h } ^ { * } \circ \varPhi _ { \alpha _ { 1 } h } \circ \varPhi _ { \beta _ { 1 } h } ^ { * } ,
$$

the condition for order $p + 1$ becomes,byusing theresult (3.4) anda similar proof as above,

$$
\begin{array} { r l r } { \beta _ { 1 } + \alpha _ { 1 } + \beta _ { 2 } + . . . . + \beta _ { s } + \alpha _ { s } = 1 } & { } & \\ { ( - 1 ) ^ { p } \beta _ { 1 } ^ { p + 1 } + \alpha _ { 1 } ^ { p + 1 } + ( - 1 ) ^ { p } \beta _ { 2 } ^ { p + 1 } + . . . + ( - 1 ) ^ { p } \beta _ { s } ^ { p + 1 } + \alpha _ { s } ^ { p + 1 } = 0 , } & { } & \end{array}
$$

Thisallows an order increase for odd $p$ aswell.In particular,we see at once the solution $\alpha _ { 1 } = \beta _ { 1 } = 1 / 2$ for $p = s = 1$ ,which turns every consistent one-step method of order 1 intoa second-order symmetric method

$$
\varPsi _ { h } = \varPhi _ { h / 2 } \circ \varPhi _ { h / 2 } ^ { * } .
$$

Example 4.4.If $\phi _ { h }$ is the explicit (resp.implicit) Euler method, then $\psi _ { h }$ in(4.8） becomes the implicit midpoint (resp.trapezoidal) rule.

Example4.5.In a second-order problem $\dot { q } ~ = ~ p$ ， $\dot { p } ~ = ~ g ( q )$ ,if $\phi _ { h }$ isthe symplectic Euler method,which discretizes $q$ bythe implicit Euler and $p$ bytheexplicit Euler method,then the composed method $\varPsi _ { h }$ in（4.8）is the Stormer-Verlet method (I.1.17).

ANumerical Example.To demonstrate the numerical performance of theabove methods,we choose the Kepler problem (I.2.2） with $e = 0 . 6$ and the initial values from(I.2.11).As integrationintervalwechoose[O,7.5],a bit more than one revolution.Theexact solution is obtainedby carefully evaluating the integral (I.2.10), which gives

$$
\varphi = 8 . 6 7 0 0 2 6 3 2 3 1 4 2 8 1 4 9 5 1 5 9 1 0 8 8 2 8 5 5 2 ,
$$

with the help of which we compute $r$ ， $\dot { \varphi }$ ， $\dot { r }$ from(I.2.8)and(I.2.6).This gives

Asthe basic method weuse the Verlet scheme and compare in Fig.4.4 the performances of the composition sequences of the Triple Jump (4.4)and those of Suzuki (4.5)fora large number of different equidistant basic step sizes and for orders $p = 4 , 6 , 8 , 1 0 , 1 2$ Eachbasic step is then divided into $3 , 9 , 2 7 , 8 1 , 2 4 3$ respectively 5,25,125,625,3125 composition stepsand the maximal final error iscompared with the total number of function evaluations in double logarithmic scales.For each method and order,all thepoints lieasymptotically ona straight linewith slope $- p$ Therefore,theoretically,a higher order method will become superior when the precision requirements become sufficiently high.But we see that for orders 10 and 12 these“break even points”are far beyond any precision of practical interest,after some40or50digits.We also observe that the wild zig-zag of the Triple Jump(4.4) isa more serious handicap than the enormous number of small steps of the Suzuki sequence(4.5).

Forlater reference we have also included,in black symbols,theresults obtained bythetwomethods(V.3.11) and(V.3.13)oforders6and8,respectively,whichwill be the outcome of amore elaborate order theory of Chap.III.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/5ac09ca5abe08cb8258ffd6563b2bfc0cccf0296200cb6eacc93f4d89143666f.jpg)  
Fig.4.4.Numerical results of the Triple Jumpand Suzuki step sequences (grey symbols) compared to optimal methods(black symbols）

# I.5Splitting Methods

Thesplitting idea yieldsan approach that is completely different from Runge-Kutta methods.One decomposes the vector field into integrable piecesand treats them separately.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/26e04ba8915ec025bd61050f06cc353eece2a6f2df924d3c8f3faa525e811ac8.jpg)  
Fig.5.1.A splitting ofa vector field

Weconsideranarbitrary system $\dot { y } = f ( y )$ in $\mathbb { R } ^ { n }$ ,and suppose that thevector fieldis"split”as(see Fig.5.1）

$$
\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y ) .
$$

Ifthen,byceeactfos $\varphi _ { t } ^ { [ 1 ] }$ and $\varphi _ { t } ^ { [ 2 ] }$ of the systems $\dot { y } = f ^ { [ 1 ] } ( y )$ and $\dot { y } = f ^ { [ 2 ] } ( y )$ can becalculated explicitly,wecan,froma given initial value $y _ { 0 }$ ,first solve the first system to obtain a value $y _ { \mathrm { I / 2 } }$ ,andfrom thisvalueintegrate the second system to obtain $y _ { 1 } .$ Inthiswaywe have introduced the numerical methods

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/cbd8202a5ad6cafd20bf0a7d1980849c2b8aa9bd8093c3bf59222648d8992b24.jpg)

where one is the adjoint of the other.These formulas are often called the $L i e \mathrm { - }$ Trtel $( \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } ) ( y _ { 0 } ) =$ ）（y0）= $\varphi _ { h } ( y _ { 0 } ) + \mathcal { O } ( h ^ { 2 } )$ ,so that both methods give approximations of order $^ { 1 }$ to the solution of(5.1).Another idea is to use a symmetric version and put

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/701b7c06d9aa159a409e8c0589bc030895d921d9cb03b7d79235f13e09afb6d3.jpg)

whichisknown asthe Strang splitting1 (Strang 1968),and sometimesas the MarchuksplitngMaruk968)Breakingui3) $\varphi _ { h } ^ { [ 2 ] } = \varphi _ { h / 2 } ^ { [ 2 ] } \circ \varphi _ { h / 2 } ^ { [ 2 ] }$ we sethateStrang spliting $\varPhi _ { h } ^ { \left[ S \right] } = \varPhi _ { h / 2 } \circ \varPhi _ { h / 2 } ^ { * }$ is the composition of the Lie-Trotter method and itsadjoint with halved step sizes.The Strang spliting formula is therefore symmetric and of order 2 (see (4.8)).

Example 5.1 (The Symplectic Eulerand the Stormer-Verlet Schemes).Supposewe havea Hamiltoniansystem with separable Hamiltonian $H ( p , q ) = T ( p ) +$ $U ( q )$ .Weconsider this as the sum of two Hamiltonians,the first one depending only on $p$ ,the second one only on $q .$ The corresponding Hamiltonian systems

$$
\begin{array} { l l l l l } { { \dot { p } = 0 } } & { { \quad \mathrm { ~ a n d ~ } \quad } } & { { \dot { p } = - U _ { q } ( q ) } } \\ { { \ddot { q } = T _ { p } ( p ) } } & { { \quad \mathrm { ~ a n d ~ } \quad } } & { { \dot { q } = 0 } } \end{array}
$$

can be solved without problem to yield

$$
\begin{array} { r l } & { p ( t ) = p _ { 0 } } \\ & { q ( t ) = q _ { 0 } + t T _ { p } ( p _ { 0 } ) \qquad \mathrm { ~ a n d ~ } \qquad p ( t ) = p _ { 0 } - t U _ { q } ( q _ { 0 } ) } \\ & { q ( t ) = q _ { 0 } + t T _ { p } ( p _ { 0 } ) } \end{array}
$$

Eulertod9ss Denotingtheflowsofthesetwosystems by $\varphi _ { t } ^ { I }$ $\varphi _ { h } ^ { 1 } \circ \varphi _ { h } ^ { U } .$ and $\varphi _ { t } ^ { U }$ Furthermore,theadjoitof we see that the symplectic thesymplectcEulermethod is $\varphi _ { h } ^ { ( ) } \circ \varphi _ { h } ^ { \prime }$ andbyExample4.5theVerletheis $\varphi _ { h / 2 } ^ { U } \circ \varphi _ { h } ^ { \prime } \circ \varphi _ { h / 2 } ^ { U }$ theStrangsplittng(5.3).AnticipatingtheresultsofChap.VI,the flows $\varphi _ { h } ^ { L }$ and $\varphi _ { h } ^ { U }$ arebothymplecticsoatiosndinethoo symplectic maps is againsymplectic,this gives an elegant proof ofthe symplecticity ofthe“symplectic”Eulermethod and theVerlet scheme.

General Splitting Procedure.In a similar way to the general idea of compositionmethods (4.6),wecan formwith arbitrary coefficients $a _ { 1 } , b _ { 1 } , a _ { 2 } , \dots , a _ { m } , b _ { m }$ (where,eventually, $a _ { 1 }$ or $b _ { m }$ ,or both,are zero)

$$
\varPsi _ { h } = \varphi _ { b _ { m } h } ^ { [ 2 ] } \circ \varphi _ { a _ { m } h } ^ { [ 1 ] } \circ \varphi _ { b _ { m - 1 } h } ^ { [ 2 ] } \circ \dots \circ \varphi _ { a _ { 2 } h } ^ { [ 1 ] } \circ \varphi _ { b _ { 1 } h } ^ { [ 2 ] } \circ \varphi _ { a _ { 1 } h } ^ { [ 1 ] }
$$

and try to increase the order of the scheme by suitably determining the free coefficients.An early contribution to this subject is the article of Ruth (1983),where,for the specialcase（5.4）,amethod(5.6）of order3with $m = 3$ is constructed.Forest &Ruth（199O)andCandy&Rozmus（1991）extend Ruth'stechnique and construct methods of order 4.One of their methods is just (4.1)with $\gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 }$ givenby（4.4） $( p = 2$ and $\varPhi _ { h }$ from(5.3).A systematic study of such methods started with the articles of Suzuki (1990,1992)and Yoshida(1990).

Aclose connection between the theories of splitting methods (5.6) and of compositionmethods(4.6) wasdiscovered byMcLachlan(1995).Indeed,if we put β=a1 and break uph $\varphi _ { b _ { 1 } h } ^ { [ 2 ] } = \varphi _ { \alpha _ { 1 } h } ^ { [ 2 ] } \circ \varphi _ { \beta _ { 1 } h } ^ { [ 2 ] }$ (group property of the exact flow) wherea1 is givenin （5.8),furth $\varphi _ { a _ { 2 } h } ^ { [ 1 ] } = \varphi _ { \beta _ { 2 } h } ^ { [ 1 ] } \circ \varphi _ { \alpha _ { 1 } h } ^ { [ 1 ] }$ and so on(cf.Fig.5.2）,we see,using（5.2）,that $\psi _ { h }$ of（5.6）is identical with $\psi _ { h }$ of（4.6）,where

$$
\begin{array} { r } { \varPhi _ { h } = \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } \qquad \mathrm { s o ~ t h a t } \qquad \varPhi _ { h } ^ { \ast } = \varphi _ { h } ^ { [ 2 ] } \circ \varphi _ { h } ^ { [ 1 ] } . } \end{array}
$$

Anecessary and sufficient condition for the existence of $\alpha _ { i }$ and $\beta _ { i }$ satisfying（5.8） is that $\sum a _ { i } = \sum b _ { i }$ ,which is the consistency condition anyway formethod (5.6).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/c0795e63e506e81f3f80713d412d04eab4d91a26c98ab59b354a81e230290809.jpg)  
Fig.5.2.Equivalence of spliting and composition methods

Combining Exact and Numerical Flows.Itmay happen that the differential equation $\dot { y } = f ( y )$ can be split accordingto (5.1）,such that only the flow of,say, $\dot { y } = f ^ { [ 1 ] } ( y )$ can be computed exactly.If $f ^ { [ 1 ] } ( y )$ constitutes the dominant part of thevector field,it is natural to search forintegrators that exploit thisinformation. The above interpretation of splitting methods as composition methods allows us to construct such integrators.We just consider

$$
\varPhi _ { h } = \varphi _ { h } ^ { [ 1 ] } \circ \varPhi _ { h } ^ { [ 2 ] } , \qquad \varPhi _ { h } ^ { * } = \varPhi _ { h } ^ { [ 2 ] * } \circ \varphi _ { h } ^ { [ 1 ] }
$$

asthebasisofose $f ^ { [ 1 ] } ( y )$ ,and $\varPhi _ { h } ^ { [ 2 ] }$ isei $\varphi _ { t } ^ { [ 1 ] }$ is te exact flow of $\dot { y } = f ^ { [ 2 ] } ( y )$ Since $\phi _ { h }$ $\dot { y } =$ of (5.9)is consistent with (5.1),theresultingmethod(4.6) has thedesired high order. It is given by

$$
\varPsi _ { h } = \varphi _ { \alpha _ { s } h } ^ { [ 1 ] } \circ \Phi _ { \alpha _ { s } h } ^ { [ 2 ] } \circ \Phi _ { \beta _ { s } h } ^ { [ 2 ] * } \circ \varphi _ { ( \beta _ { s } + \alpha _ { s - 1 } ) h } ^ { [ 1 ] } \circ \Phi _ { \alpha _ { s - 1 } h } ^ { [ 2 ] } \circ \circ \Phi _ { \beta _ { 1 } h } ^ { [ 2 ] * } \circ \varphi _ { \beta _ { 1 } h } ^ { [ 1 ] } .
$$

Notice that elacing $\varphi _ { t } ^ { [ 2 ] }$ withalow-order aproxmation $\varPhi _ { t } ^ { [ 2 ] }$ in (56)woud not retainthedefeosi $\varPhi _ { t } ^ { [ 2 ] }$ does not satisfy the goup property.

Splitting into Morethan Two Vector Fields.Consideradifferential equation

$$
\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y ) + \ldots + f ^ { [ N ] } ( y ) ,
$$

where we assume that the flows $\varphi _ { t } ^ { [ j ] }$ of the individual problems $\dot { y } = f ^ { [ j ] } ( y )$ can becomputed exactly.In this case there are manypossibilities for extending(5.6) andforwritingthemethodaacompositionof Thismakes itdifficult to find optimal compositions of high order.A simpleand efficient way is toconsider the first-order method

$$
\boldsymbol { \varPhi } _ { h } = \boldsymbol { \varphi } _ { h } ^ { [ 1 ] } \circ \boldsymbol { \varphi } _ { h } ^ { [ 2 ] } \circ \dots \circ \boldsymbol { \varphi } _ { h } ^ { [ N ] }
$$

together with its adjoint as the basis of the composition (4.6).Without any additional effort this yieldsspliting methods for(5.11) of arbitrary highorder.

# II.6 Exercises

1.Compute all collocation methods with $s = 2$ asa function of $c _ { 1 }$ and $c _ { 2 }$ Which of themare of order3,which of order4?

2.Prove that the collocation solution plotted in the right picture ofFig.1.3 is composed of arcs of parabolas.

3.Let $b _ { 1 } = b _ { 4 } = 1 / 8$ ， $c _ { 2 } ~ = ~ 1 / 3$ ， $c _ { 3 } = 2 / 3$ ,and consider the corresponding discontinuous collocation method.Determine its order and find the coefficients ofthe equivalent Runge-Kutta method.

4.Show that each of the symplectic Euler methods in (I.1.9) is the adjoint of the other.

5.(Additive Runge-Kutta methods).Let $b _ { i } , a _ { i j }$ and $b _ { i } , \hat { a } _ { i j }$ be the coefficients of twoRunge-Kutta methods.An additive Runge-Kutta method for the solution of $\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y )$ is given by

$$
\begin{array} { r c l } { { } } & { { } } & { { k _ { i } ~ = ~ f ^ { [ 1 ] } \displaystyle \Bigl ( y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } \Bigr ) + f ^ { [ 2 ] } \Bigl ( y _ { 0 } + h \sum _ { j = 1 } ^ { s } \widehat { a } _ { i j } k _ { j } \Bigr ) } } \\ { { } } & { { } } & { { y _ { 1 } ~ = ~ y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i \cdot } } } \end{array}
$$

Show that thiscan be interpreted as a partitioned Runge-Kutta method (2.2) applied to

$$
\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( z ) , \qquad \dot { z } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( z )
$$

with $y ( 0 ) = z ( 0 ) = y _ { 0 } .$ Notice that $y ( t ) = z ( t )$

6.Let $\phi _ { h }$ denote the Stormer-Verlet scheme,and consider the composition

$$
\Phi _ { \gamma _ { 2 k + 1 } h } \circ \varPhi _ { \gamma _ { 2 k } h } \circ . . . \circ \varPhi _ { \gamma _ { 2 h } \circ } \varPhi _ { \gamma _ { 1 } h }
$$

with $\gamma _ { 1 } = . . . = \gamma _ { k } = \gamma _ { k + 2 } = . . . = \gamma _ { 2 k + 1 } .$ Compute $\gamma _ { 1 }$ and $\gamma _ { k + 1 }$ such thatthe composition givesamethod of order 4.For several differential equations (pendulum,Kepler problem) study the global error of aconstant step size implementation asa function of $k$ .

7.Consider thecomposition method(4.1）with $s \ : = \ : 5$ ， $\gamma _ { 5 } ~ = ~ \gamma _ { 1 }$ ,and $\gamma _ { 4 } ~ = ~ \gamma _ { 2 }$ Among the solutions of

$$
2 \gamma _ { 1 } + 2 \gamma _ { 2 } + \gamma _ { 3 } = 1 , \qquad 2 \gamma _ { 1 } ^ { 3 } + 2 \gamma _ { 2 } ^ { 3 } + \gamma _ { 3 } ^ { 3 } = 0
$$

find the one that minimizes $| 2 \gamma _ { 1 } ^ { 5 } + 2 \gamma _ { 2 } ^ { 5 } + \gamma _ { 3 } ^ { 5 } |$

Remark.This property motivates the choice of the $\gamma _ { i }$ in (4.5).
