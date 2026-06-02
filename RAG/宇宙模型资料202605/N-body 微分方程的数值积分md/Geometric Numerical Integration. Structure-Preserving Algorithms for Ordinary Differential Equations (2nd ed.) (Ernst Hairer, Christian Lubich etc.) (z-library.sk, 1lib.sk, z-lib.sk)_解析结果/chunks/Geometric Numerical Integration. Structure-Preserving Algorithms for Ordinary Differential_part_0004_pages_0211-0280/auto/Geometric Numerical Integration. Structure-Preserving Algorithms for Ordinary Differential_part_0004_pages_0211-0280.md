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

![](images/a95c5d2da558fff02c6db157ceef074e63648745b525dfb392ab31c14be580ac.jpg)  
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

![](images/68b98f3c2596387b294cfc41a4949cd296aa57774ddf5f06f2f3bf8ab951c5c0.jpg)  
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

![](images/1475c1070eef68cd9ac45a0a92046f36c844d1ca87e41be3e20163cb9b9eb315.jpg)  
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

![](images/eb7db4f551c884a56c20c431f68c6b4a2fbf6539ab92c2196fd5d42a165bc8b2.jpg)  
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

![](images/c931c56486061949bc61180896d701f88407c6f1c86cdfd5998ec1425cb7b93c.jpg)  
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

![](images/0fa4ab23aaa51e5d17055ac120ecfa57f6e75ee4eeff4a32a091da45a362f263.jpg)

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

![](images/985831e4bb6fdf974c378ef5e565e304f1dac6f04b6b98cb46095947665d0ed0.jpg)  
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

![](images/c6f4de01610efba06408a35c9299bf705e1ef1319f441d0fca97bce8394a7c4e.jpg)  
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

![](images/830f3acc6dc106abd777b43bc018013b142fb3d9be7c1980054416539b0cf72d.jpg)  
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