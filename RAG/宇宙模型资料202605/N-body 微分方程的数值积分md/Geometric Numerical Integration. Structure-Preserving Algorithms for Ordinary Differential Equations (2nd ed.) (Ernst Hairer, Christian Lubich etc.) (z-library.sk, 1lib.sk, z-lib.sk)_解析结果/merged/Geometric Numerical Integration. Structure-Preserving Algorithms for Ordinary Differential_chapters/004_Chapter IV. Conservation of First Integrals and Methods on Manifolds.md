# Chapter IV. Conservation of First Integrals and Methods on Manifolds

Thischapter deals with the conservation of invariants (first integrals) by numerical methods,and with numerical methods for differential equations on manifolds.Our investigation will follow two directions.We first investigate which of the methods introduced in Chap.I conserve invariants automatically.We shall see that mostof themconserve linear invariants,a few of them quadratic invariants,and none of themconserves cubic or general nonlinear invariants.We then construct new classes ofmethods,which are adapted to known invariantsandwhich force the numerical solution to satisfy them.In particular,we study projection methodsand methods based on local coordinates of the manifold defined by the invariants.We discuss in some detail the case where the manifold isaLie group.Finally,we consider differential equations on manifolds with orthogonality constraints,which often arise innumerical linear algebra.

# IV.1 Examples ofFirst Integrals

Jenomme integrale uneequation $u = C o n s t$ tellequesa differentielle $d u = 0$ soit verifiee identiquement parle systeme des equations differentielles proposees... (C.G.J.Jacobi 1840,p.350)

We consider differential equations

$$
\dot { y } = f ( y ) ,
$$

where $y$ is a vector or possibly a matrix.

Definition1.1.A non-constant function $I ( y )$ is calledafirst integralof(1.1)if

$$
I ^ { \prime } ( y ) f ( y ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } y .
$$

This implies that every solution $y ( t )$ of（1.1） satisfies $I ( y ( t ) ) = I ( y _ { 0 } ) = C o n s t .$ Synonymouslywith“first integral",the terms invariant or conservedquantity or constant of motion are also used.

In Chap.Iwe have seen many examples of differential equationswith invariants. Forexample,theLotka-Volterraproblem(I.1.1） has $I ( u , v ) = \ln u - u + 2 \ln v - v$ asfirst integral.Thependulumequation(I.1.13)has $H ( p , q ) = p ^ { 2 } / 2 - \cos q ,$ and the Kepler problem(I.2.2) has two first integrals,namely $H$ and $\scriptstyle { \mathcal { L } }$ of (1.2.3) and (I.2.4).

Example1.2 (Conservation of the Total Energy).Hamiltoniansystemsareof the form

$$
\dot { p } = - H _ { q } ( p , q ) , \qquad \dot { q } = H _ { p } ( p , q ) ,
$$

where $H _ { q } = \nabla _ { q } H = \left( \partial H / \partial q \right) ^ { T }$ and $H _ { p } = \nabla _ { p } H = \left( \partial H / \partial p \right) ^ { T }$ are the column vectors of partial derivatives.The Hamiltonian function $H ( p , q )$ isa first integral. This follows at once from $H ^ { \prime } ( p , q ) = ( \partial H / \partial p , \partial H / \partial q )$ and

$$
\frac { \partial H } { \partial p } \Bigl ( - \frac { \partial H } { \partial q } \Bigr ) ^ { T } + \frac { \partial H } { \partial q } \Bigl ( \frac { \partial H } { \partial p } \Bigr ) ^ { T } = 0 .
$$

Example1.3 (Conservation of the Total Linear and Angular Momentumof N-Body Systems).We considera system of $N$ particles interacting pairwise with potential forceswhich depend on the distances of the particles.This is formulated asaHamiltonian system with total energy(I.4.1), viz.,

$$
H ( p , q ) = { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { N } { \frac { 1 } { m _ { i } } } p _ { i } ^ { T } p _ { i } + \sum _ { i = 2 } ^ { N } \sum _ { j = 1 } ^ { i - 1 } V _ { i j } \Bigl ( \lVert q _ { i } = q _ { j } \rVert \Bigr ) ~ .
$$

Here $q _ { i } , p _ { i } \in \mathbb R ^ { 3 }$ represent the position and momentum of the $i$ th particleofmass $m _ { i }$ ,and $V _ { i j } ( r )$ ( $i > j$ ）isthe interaction potential between the $\boldsymbol { \imath }$ thand $\jmath$ thparticle. The equations of motion read

$$
\dot { q } _ { i } = \frac { 1 } { m _ { i } } p _ { i } , \dot { p } _ { i } = \sum _ { j = 1 } ^ { N } \nu _ { i j } ( q _ { i } - q _ { j } )
$$

where,for $i > j$ ,we have $\nu _ { i j } = \nu _ { j i } = - V _ { i j } ^ { \prime } ( r _ { i j } ) / r _ { i j }$ with $r _ { i j } = | | q _ { i } - q _ { j } | |$ ,and $\nu _ { i i }$ is   
$\nu _ { i i } = 0 .$ Thnec $\begin{array} { r } { P = \sum _ { i = 1 } ^ { N } p _ { i } } \end{array}$ $\begin{array} { r } { L = \sum _ { i = 1 } ^ { N } q _ { i } \times p _ { i } } \end{array}$ $\nu _ { i j } = \nu _ { j i }$

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \sum _ { i = 1 } ^ { N } p _ { i } = \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } \nu _ { i j } ( q _ { i } - q _ { j } ) = 0 } \\ { \displaystyle \frac { d } { d t } \sum _ { i = 1 } ^ { N } q _ { i } \times p _ { i } = \sum _ { i = 1 } ^ { N } \frac { 1 } { m _ { i } } p _ { i } \times p _ { i } + \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } q _ { i } \times \nu _ { i j } ( q _ { i } - q _ { j } ) = 0 . } \end{array}
$$

Example1.4 (Conservation of Mass in Chemical Reactions).Suppose that three substances A,B, $C$ undergo a chemical reaction such as1

$$
{ \begin{array} { r l r l } { A } & { \xrightarrow { 0 . 0 4 } } & { B } & & { { \mathrm { ( s l o w ) } } } \\ { B + B } & { \xrightarrow { 3 \cdot 1 0 ^ { 7 } } } & { C + B } & & { { \mathrm { ( v e r y ~ f a s t ) } } } \\ { B + C } & { \xrightarrow { 1 0 ^ { 4 } } } & { A + C } & & { { \mathrm { ( f a s t ) } } . } \end{array} }
$$

Wedenote the masss (or concentrations)of the substances $A$ ， $B$ , $C$ by $y _ { 1 }$ ， $y _ { 2 }$ y3， respectively.Bythe mass action law this leads to the equations

$$
\begin{array} { r l r l r } { \mathrm { A } : } & { { } \quad } & { \dot { y } _ { 1 } = - 0 . 0 4 y _ { 1 } + 1 0 ^ { 4 } y _ { 2 } y _ { 3 } } & { { } } \\ { \mathrm { B } : } & { { } \quad } & { \dot { y } _ { 2 } = { } } & { { } 0 . 0 4 y _ { 1 } - 1 0 ^ { 4 } y _ { 2 } y _ { 3 } - 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } } \\ { \mathrm { C } : } & { { } \quad } & { \dot { y } _ { 3 } = } & { { } } & { 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } } \end{array}
$$

Wesee that $\dot { y } _ { 1 } + \dot { y } _ { 2 } + \dot { y } _ { 3 } = 0$ ,hence the total mass $I ( y ) = y _ { 1 } + y _ { 2 } + y _ { 3 }$ isan invariant of the system.

Aswas noted by Shampine(1986),such linear invariants are generallyconservedbynumerical integrators.

Theorem1.5(Conservation of Linear Invariants).All explicit and implicit Runge-Kuttamethodsconserve linear invariants.Partitioned Runge-Kutta methods(Il.2.2)conserve linear invariantsif $b _ { i } = { \hat { b } } _ { i }$ forall $i$ ,oriftheinvariantdepends only onpor only on $q$ .

ProofLet $I ( y ) = d ^ { 1 } y$ witha constant vector $d$ ,sothat $d ^ { \varPsi } f ( y ) = 0$ forall $_ y$ Inthe case of Runge-Kutta methods we thus have $d ^ { 2 } k _ { i } = 0$ ,and consequently $d ^ { L } y _ { 1 } = d ^ { L } y _ { 0 } + h d ^ { L } \left( \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } \right) = d ^ { L } y _ { 0 } .$ Thestatementforpartitionedmethodsis proved similarly. □

Next we consider differential equations of the form

$$
{ \dot { Y } } = A ( Y ) Y ,
$$

where $Y$ canbeavector or a matrix (not necessarily asquarematrix).We then have the followingresult.

Theorem 1.6.1f $A ( Y )$ is skew-symmetric forall $Y$ (i.e., $A ^ { I ^ { \prime } } = - A$ ),thenthe quadraticfunction $I ( Y ) = Y ^ { T } Y$ isaninvariant.Inparticular,iftheinitialvalue $Y _ { 0 }$ consists of orthonormal columns(i.e., $Y _ { 0 } ^ { T } Y _ { 0 } = I$ ),thenthecolumns ofthe solution $Y ( t )$ of(1.3)remain orthonormal forall t.

ProofThe derivative of $I ( Y )$ is $I ^ { \prime } ( Y ) H ~ = ~ Y ^ { T } H + H ^ { T } Y ,$ Thus,we have $I ^ { \prime } ( Y ) f ( Y ) = I ^ { \prime } ( Y ) ( A ( Y ) Y ) = Y ^ { \nu } A ( Y ) Y + Y ^ { T } A ( Y ) ^ { T } Y$ forall $Y$ whichvanishes,because $A ( Y )$ isskew-symmetric.This proves the statement. □

Example1.7(RigidBody).Themotion ofa freerigid body,whose centreofmass isat the origin,is described by the Euler equations

$$
\begin{array} { r l r } { \dot { y } _ { 1 } = a _ { 1 } y _ { 2 } y _ { 3 } , \quad } & { { } \quad a _ { 1 } = ( I _ { 2 } - I _ { 3 } ) / ( I _ { 2 } I _ { 3 } ) } \\ { \dot { y } _ { 2 } = a _ { 2 } y _ { 3 } y _ { 1 } , \quad } & { { } \quad a _ { 2 } = ( I _ { 3 } - I _ { 1 } ) / ( I _ { 3 } I _ { 1 } ) } \\ { \dot { y } _ { 3 } = a _ { 3 } y _ { 1 } y _ { 2 } , \quad } & { { } \quad a _ { 3 } = ( I _ { 1 } - I _ { 2 } ) / ( I _ { 1 } I _ { 2 } ) } \end{array}
$$

where the vector $\begin{array} { r c l } { y } & { = } & { ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) ^ { T } } \end{array}$ represents the angular momentum in the body frame,and $I _ { 1 } , I _ { 2 } , I _ { 3 }$ arethe principal moments of inertia (Euler（1758b);see Sect.VII.5 fora detailed description.This problemcan bewritten as

$$
\left( \begin{array} { c } { { \dot { y } _ { 1 } } } \\ { { \dot { y } _ { 2 } } } \\ { { \dot { y } _ { 3 } } } \end{array} \right) \equiv \left( \begin{array} { c c c } { { 0 } } & { { y _ { 3 } / I _ { 3 } } } & { { - y _ { 2 } / I _ { 2 } } } \\ { { - y _ { 3 } / I _ { 3 } } } & { { 0 } } & { { y _ { 1 } / I _ { 1 } } } \\ { { y _ { 2 } / I _ { 2 } } } & { { - y _ { 1 } / I _ { 1 } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { y _ { 1 } } } \\ { { y _ { 2 } } } \\ { { y _ { 3 } } } \end{array} \right) ,
$$

which isof the form(1.3)with a skew-symmetricmatrix $A ( Y )$ ByTheorem1.6, $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ is an invariant.A second quadratic invariant is

$$
H ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) = \frac { 1 } { 2 } \Big ( \frac { y _ { 1 } ^ { 2 } } { I _ { 1 } } + \frac { y _ { 2 } ^ { 2 } } { I _ { 2 } } + \frac { y _ { 3 } ^ { 2 } } { I _ { 3 } } \Big ) ,
$$

which represents the kinetic energy.

Inspired bythe coverpage ofMarsden& Ratiu(1999),wepresent in Fig.1.1 the sphere with some of the solutions of(1.4） corresponding to $I _ { 1 } = 2 , I _ { 2 } = 1$ and $I _ { 3 } = 2 / 3$ .Theylie onthe intersection of the sphere with the ellipsoid given by $H ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) = C o n s t .$ In the left picture we have included the numerical solution(3O steps) obtained by the implicit midpoint rule with step size $h = 0 . 3$ and initial value $y _ { 0 } = ( \cos ( 1 . 1 ) , 0 , \sin ( 1 . 1 ) ) ^ { T } .$ It stays exactly on a solution curve.This follows from the fact thatthe implicit midpoint rule preserves quadratic invariants exactly(Sect.IV.2).

Forthe explicit Euler method (right picture of Fig.1.1,320 steps with $h =$ 0.05and the same initial value)we see that the numerical solution shows a wrong qualitative behaviour(it should lie on a closed curve).The numerical solution even driftsaway from the sphere.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/dd00daa3233ef9aa865addc93bdaf1931119cf127d38e3008aa91a987c0a182a.jpg)  
Fig.1.1.Solutions of the Euler equations(1.4） for the rigid body

# IV.2 Quadratic Invariants

Quadratic invariants appear often in applications.Examples are the conservation law of angularmomentumin $N$ -bodysystems(Example1.3),theitwc invariantsof therigid bodymotion(Example 1.7）,and the invariant $Y ^ { T } Y$ of Theorem 1.6.We thereforeconsiderdifferential equations(1.1）and quadratic functions

$$
Q ( y ) = y ^ { T } C y ,
$$

where $C$ is asymmetric squarematrix.It is an invariant of(1.1) if $y ^ { T } C f ( y ) = 0$ for all $y$

# IV.2.1 Runge-Kutta Methods

Weshall give acomplete characterization of Runge-Kutta methodswhich automatically conserve allquadratic invariants.We first of all consider the Gausscollocation methods.

Theorem2.1.TheGaussmethodsofSect.II.1.3(collocationbasedontheshifted Legendrepolynomials) conservequadratic invariants.

ProofLet $u ( t )$ be the collocation polynomial of the Gauss methods (Definition II.1.3). Since $\begin{array} { r } { \frac { d } { d t } Q \big ( u ( t ) \big ) \ = \ 2 u ( t ) ^ { T } C \dot { u } ( t ) } \end{array}$ ,it followsfrom $u ( t _ { 0 } ) ~ = ~ y _ { 0 }$ and $u ( t _ { 0 } + h ) = y _ { 1 }$ that

$$
y _ { 1 } ^ { T } C y _ { 1 } - y _ { 0 } ^ { T } C y _ { 0 } = 2 \int _ { t _ { 0 } } ^ { t _ { 0 } + h } u ( t ) ^ { T } C { \dot { u } } ( t ) d t .
$$

The integrand $u ( t ) ^ { T } C \dot { u } ( t )$ isapolynomial of degree $2 s - 1$ ,whichisintegrated without error by the $s$ -stageGaussianquadrature formula.Ittherefore follows from the collocation condition

$$
u ( t _ { 0 } + c _ { i } h ) ^ { T } C \dot { u } ( t _ { 0 } + c _ { i } h ) = u ( t _ { 0 } + c _ { i } h ) ^ { T } C f \big ( u ( t _ { 0 } + c _ { i } h ) \big ) = 0
$$

that the integral in (2.2) vanishes.

Since the implicit midpoint rule is the special case $s = 1$ of the Gauss methods, thepreceding theorem explains its good behaviour for the rigid body simulationin Fig1.1.

Theorem2.2 (Cooper1987).Ifthecoefficientsofa Runge-Kutta methodsatisfy

$$
b _ { i } a _ { i j } + b _ { j } a _ { j i } = b _ { i } b _ { j } \qquad f o r a l l i , j = 1 , \ldots , s ,
$$

thenitconservesquadratic invariants.2

Proof.The proof is thesameas that forB-stability,givenindependentlybyBurrage &Butcher and Crouzeix in 1979(see Hairer&Wanner(1996),Sect.IV.12).

The relation $\begin{array} { r } { y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } } \end{array}$ of Definition II.1.1 yields

$$
y _ { 1 } ^ { T } C y _ { 1 } = y _ { 0 } ^ { T } C y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } ^ { T } C y _ { 0 } + h \sum _ { j = 1 } ^ { s } b _ { j } y _ { 0 } ^ { T } C k _ { j } + h ^ { 2 } \sum _ { i , j = 1 } ^ { s } b _ { i } b _ { j } k _ { i } ^ { T } C k _ { j } .
$$

We then write $k _ { i } ~ = ~ f ( Y _ { i } )$ with $\begin{array} { r } { Y _ { i } \ = \ y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } } \end{array}$ The main idea is to compute $y _ { 0 }$ from this relation and to insert it into the central expressions of(2.4). Thisyields (using the symmetryof $C$ )

$$
^ T _ { 1 } C y _ { 1 } = y _ { 0 } ^ { T } C y _ { 0 } + 2 h \sum _ { i = 1 } ^ { s } b _ { i } Y _ { i } ^ { T } C f ( Y _ { i } ) + h ^ { 2 } \sum _ { i , j = 1 } ^ { s } \left( b _ { i } b _ { j } - b _ { i } a _ { i j } - b _ { j } a _ { j i } \right) k _ { i } ^ { T } C
$$

The condition （2.3） together with the assumption $y ^ { \scriptscriptstyle T } C f ( y ) = 0$ ,which states that $y ^ { T } C y$ isaninvariantof(ly $y _ { 1 } ^ { \prime } C y _ { 1 } = y _ { 0 } ^ { T } C y _ { 0 }$ □

Thecriterion (2.3) is very restrictive.One finds that among all collocation and discontinuous collocation methods (Definition II.1.7) only the Gauss methods satisfythis criterion (Exercise 6).On the other hand,itispossible to construct other high-order Runge-Kutta methods satisfying(2.3).The key for such aconstruction is the $W$ -transformation(see Hairer&Wanner(1996),Sect.IV.5),which is exploited in the articles of Sun(1993a)and Hairer&Leone(2000).

# IV.2.2Partitioned Runge-Kutta Methods

Wenext consider partitioned Runge-Kutta methods for systems $\begin{array} { r } { \dot { \boldsymbol { y } } ~ = ~ \boldsymbol { f } \left( \boldsymbol { y } , z \right) } \end{array}$ , $\dot { z } = g ( y , z )$ Usually such methods cannot conserve general quadratic invariants (Exercise 4).We therefore concentrate on quadratic invariants of the form

$$
Q ( y , z ) = y ^ { T } D z ,
$$

where $\mathcal { D }$ isamatrix of the appropriate dimensions.Observe that the angular momentum of $N$ -bodysystems(Example1.3) isofthisform.

Theorem2.3 (Sun 1993b).The Lobatto IIA-IIIBpair conservesall quadratic invariantsoftheform(2.5).Inparticular,thisistruefortheStormer-Verletscheme (seeSect.II.2.2）.

Proof.Let $u ( t )$ and $\boldsymbol { v } ( t )$ be the(discontinuous)collocation polynomials of the Lobatto IIIA and Lobatto IIIBmethods,respectively (see Sect.II.2.2).Inanalogy to theproof of Theorem 2.1we have

$$
\begin{array} { r l r } {  { Q \big ( u ( t _ { 0 } + h ) , v ( t _ { 0 } + h ) \big ) - Q \big ( u ( t _ { 0 } ) , v ( t _ { 0 } ) \big ) } } \\ & { } & { \quad = \int _ { t _ { 0 } } ^ { t _ { 0 } + h } \Big ( Q \big ( \dot { u } ( t ) , v ( t ) \big ) + Q \big ( \dot { u } ( t ) , \dot { v } ( t ) \big ) \Big ) d t . } \end{array}
$$

Since $u ( t )$ is ofdegree $s$ and $v ( t )$ ofdegree $s - 2$ ,theintegrand of(2.6)isapolynomial ofdegree $2 s - 3$ .Hence,an application of theLobatto quadrature yields the exact result.Using the fact that $Q ( y , z )$ isan invariant of the differential equation, ie., $Q \big ( f ( y , z ) , z \big ) + Q \big ( y , g ( y , z ) \big ) \equiv 0$ ,we thus obtain for the integralin (2.6)

$$
h b _ { 1 } Q \big ( u ( t _ { 0 } ) , \delta ( t _ { 0 } ) \big ) + h b _ { s } Q \big ( u ( t _ { 0 } + h ) , \delta ( t _ { 0 } + h ) \big ) ,
$$

where $\delta ( t ) = \dot { v } ( t ) - g \big ( u ( t ) , v ( t ) \big )$ denotes the defect.It now follows from $u ( t _ { 0 } ) =$ $y _ { 0 }$ , $u ( t _ { 0 } + h ) = y _ { 1 }$ (definition ofLobatto IIIA）and from $v ( t _ { 0 } ) = z _ { 0 } - h b _ { 1 } \delta ( t _ { 0 } )$ , $v ( t _ { 0 } + h ) \ = \ z _ { 1 } + h b _ { s } \delta ( t _ { 0 } + h )$ (definition of Lobatto IIB）that $Q ( y _ { 1 } , z _ { 1 } ) \textrm { -- }$ $Q ( y _ { 0 } , z _ { 0 } ) = 0$ ,which proves the theorem. □

Exchanging the roleof the IIIA and IIB methodsalso leads toan integrator thatpreservesquadratic invariants of the form(2.5).The followingcharacterization extends Theorem 2.2to partitioned Runge-Kutta methods.

Theorem2.4.If thecoefficientsofapartitionedRunge-Kutta method(I1.2.2)satisfy

$$
\begin{array} { l } { { b _ { i } \widehat a _ { i j } + \widehat b _ { j } a _ { j i } = b _ { i } \widehat b _ { j } f o r i , j = 1 , \ldots , s , } } \\ { { b _ { i } = \widehat b _ { i } f o r i = 1 , \ldots , s , } } \end{array}
$$

then itconserves quadratic invariants of the form(2.5).

Ifthepartitioneddifferentialequationisofthespecialform $\dot { y } = f ( z )$ ， $\dot { z } = g ( y )$ , thencondition(2.7)alone impliesthat invariants oftheform(2.5) are conserved.

Proof.The proof is nearly identical to that of Theorem2.2.Insteadof(2.4)we get

$$
y _ { 1 } ^ { T } D z _ { 1 } = y _ { 0 } ^ { T } D z _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } ^ { T } D z _ { 0 } + h \sum _ { j = 1 } ^ { s } \widehat { b } _ { j } y _ { 0 } ^ { T } D \ell _ { j } + h ^ { 2 } \sum _ { i , j = 1 } ^ { s } b _ { i } \widehat { b } _ { j } k _ { i } ^ { T } D \ell _ { j }
$$

Denoting by $( Y _ { i } , Z _ { i } )$ theargumentsof $k _ { i } = f ( Y _ { i } , Z _ { i } )$ and $\ell _ { i } = g ( Y _ { i } , Z _ { i } )$ thesame trickas in theproof ofTheorem2.2 gives

$$
\begin{array} { r l } { y _ { 1 } ^ { T } D z _ { 1 } \ = \ y _ { 0 } ^ { T } D z _ { 0 } \ + \ h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } f ( Y _ { i } , Z _ { i } ) ^ { T } D Z _ { i } + h \displaystyle \sum _ { j = 1 } ^ { s } \widehat { b } _ { j } Y _ { j } ^ { T } D g ( Y _ { j } , Z _ { j } ) } \\ { \displaystyle + \ h ^ { 2 } \displaystyle \sum _ { i , j = 1 } ^ { s } ( b _ { i } \widehat { b } _ { j } - b _ { i } \widehat { a } _ { i j } - \widehat { b } _ { j } a _ { j i } ) k _ { i } ^ { T } D \ell _ { j } . } \end{array}
$$

Since(2.5)isaninvariant,wehave $f ( y , z ) ^ { T } D z + y ^ { T } D g ( y , z ) = 0$ forall $_ y$ and $z$ Consequently,the twoconditions (2.7)and(2.8)imply $y _ { 1 } ^ { \prime } D z _ { 1 } = y _ { 0 } ^ { T } D z _ { 0 }$ .

For the special case where $f$ depends only on $\scriptscriptstyle \mathcal { L }$ and $g$ onlyon $y$ ,theassumption $f ( z ) ^ { T } D z + y ^ { T } D g ( y ) = 0$ (forall $y , z$ impliesthat $f ( z ) ^ { \prime } D z = - y ^ { T } D g ( y ) =$ Const.Therefore,condition (2.8)is no longer necessary for the proof of the statement. □

# IV.2.3Nystrom Methods

An important class of partitioned differential equations is $y = z$ , $\dot { z } = g ( y )$ or equivalently,

$$
\ddot { y } = g ( y ) .
$$

Manyexamples ofChap.Iare of this form,in particular the $N$ -bodyproblemof Example1.3forwhich theangular momentumisaquadratic first integral.Nystrom methods (Definition II.2.3),

$$
\begin{array} { l } { { \displaystyle \ell _ { i } ~ = ~ g \Big ( y _ { 0 } + c _ { i } h \dot { y } _ { 0 } + h ^ { 2 } \sum _ { j = 1 } ^ { s } a _ { i j } \ell _ { j } \Big ) , } } \\ { { \displaystyle y _ { 1 } ~ = ~ y _ { 0 } + h \dot { y } _ { 0 } + h ^ { 2 } \sum _ { i = 1 } ^ { s } \beta _ { i } \ell _ { i } , ~ \dot { y } _ { 1 } ~ = ~ \dot { y } _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } \ell _ { i } , } } \end{array}
$$

areadapted to the numerical solution of(2.1O) and itisinteresting toinvestigate which methods within this class can conserve quadratic invariants.

Theorem2.5.Ifthecoefcientsof theNystrommethod(2.11) satisfy

$$
\begin{array} { c } { { \beta _ { i } ~ = ~ b _ { i } ( 1 - c _ { i } ) ~ f o r ~ i = 1 , \ldots , s , } } \\ { { { } } } \\ { { b _ { i } ( \beta _ { j } - a _ { i j } ) ~ = ~ b _ { j } ( \beta _ { i } - a _ { j i } ) ~ f o r ~ i , j = 1 , \ldots , s , } } \end{array}
$$

thenitconservesall quadraticinvariants ofthe form $y ^ { T } D \dot { y }$ .

Proof. The quadratic form $Q ( y , \dot { y } ) = y ^ { T } D \dot { y }$ isafirstintegral of(2.10)if and only if

$$
{ \dot { y } } ^ { T } D { \dot { y } } + { y } ^ { T } D g ( y ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } y , { \dot { y } } \in \mathbb { R } ^ { n } .
$$

This implies that $D$ is skew-symmetric and that $y ^ { T } D g ( y ) = 0$

In the samewayas for theproofs of Theorems2.2 and 2.4we now compute $y _ { 1 } ^ { \prime } D { \dot { y } } _ { 1 }$ using the formulas of (2.11） and we substitute $y _ { 0 }$ by $Y _ { i } - c _ { i } h { \dot { y } } _ { 0 } -$ $h ^ { 2 } \sum _ { j } a _ { i j } \ell _ { j }$ where $Y _ { i }$ denotes the argument of $g$ in (2.11). This yields

$$
\begin{array} { r c l } { { } } & { { } } & { { y _ { 1 } ^ { T } D \dot { y } _ { 1 } ~ = ~ y _ { 0 } ^ { T } D \dot { y } _ { 0 } + h \dot { y } _ { 0 } ^ { T } D \dot { y } _ { 0 } + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } Y _ { i } ^ { T } D \ell _ { i } } } \\ { { } } & { { } } & { { ~ + ~ h ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { s } \beta _ { i } \ell _ { i } ^ { T } D \dot { y } _ { 0 } + h ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } ( 1 - c _ { i } ) \dot { y } _ { 0 } ^ { T } D \ell _ { i } } } \\ { { } } & { { } } & { { ~ + ~ h ^ { 3 } \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } ( \beta _ { j } - a _ { i j } ) \ell _ { j } ^ { T } D \ell _ { i } . } } \end{array}
$$

Using the skew-symmetry of $D$ and $Y _ { i } ^ { T } D \ell _ { i } = Y _ { i } ^ { T } D g ( Y _ { i } ) = 0$ ,condition (2.12) implies the conservation property $y _ { 1 } ^ { T } D \dot { y } _ { 1 } = y _ { 0 } ^ { T } D \dot { y } _ { 0 }$ .

Remark2.6(Composition Methods).Ifamethod $\phi _ { h }$ conserves quadratic invariants(e.g.,themid-pointruleby Theorem2.1or the Stormer-Verlet schemeby Theo-$\mathrm { r e m } 2 . 3$ oraNystrom method of Theorem 2.5),then so does thecomposition method

$$
\varPsi _ { h } = \varPhi _ { \gamma _ { s } h } \circ \dots \circ \varPhi _ { \gamma _ { 1 } h } .
$$

This obvious property is one of the most important motivations for considering composition methods.

# IV.3Polynomial Invariants

Weconsider two classes of problems with polynomial invariants for degree higher than two.First,we treat linear problems forwhich thedeterminant of the resolvent is aninvariant,and we show that (partitioned)Runge-Kutta methods cannot conserve themautomatically.Second,we study isospectral flows.

# IV.3.1The Determinant asaFirst Integral

We consider quasi-linear problems

$$
{ \dot { Y } } = A ( Y ) Y , \qquad Y ( 0 ) = Y _ { 0 }
$$

matrix where $Y$ $A = ( a _ { i j } ) _ { i , j = 1 } ^ { n }$ and $A ( Y )$ are b $n \times n$ matrices.In the following we denote the trace of a $\textstyle A = \sum _ { i = 1 } ^ { n } a _ { i i }$

Lemma 3.1.If trace $A ( Y ) = 0$ for all $Y$ ,then $g ( Y ) : = \operatorname* { d e t } Y$ is an invariant of thematrixdifferential equation(3.1).

Proof.It followsfrom

$$
\operatorname* { d e t } \bigl ( Y + \varepsilon A Y \bigr ) = \operatorname* { d e t } \bigl ( I + \varepsilon A \bigr ) \operatorname* { d e t } Y = \bigl ( 1 + \varepsilon \operatorname { t r a c e } A + \mathcal { O } ( \varepsilon ^ { 2 } ) \bigr ) \operatorname* { d e t } Y
$$

that $g ^ { \prime } ( Y ) ( A Y ) = \operatorname { t r a c e } A { \cdot } \operatorname* { d e t } Y$ (thisistheAbel-Liouville-Jacobi-Ostrogradskii identity).Hence,thedeterminant $g ( Y ) = \operatorname* { d e t } Y$ isaninvariant ofthedifferential equation（3.1）if trace $A ( Y ) = 0$ forall $Y$ . □

Since $\operatorname { d e t } Y$ represents the volume of the parallelepiped generated by the columns of the matrix $Y$ ,theconservation of the invariant $g ( Y ) = \operatorname* { d e t } Y$ isrelated tovolumepreservation.This topicwillbe furtherdiscussed in Sect.VI.9.Here,we consider det $Y$ asapolynomial invariant of degree $_ { n }$ ,andwe investigatewhether Runge-Kutta methodscan automatically conserve this invariant for $n \geq 3 .$ Thekey lemma for this study is the following.

Lemma 3.2 (Feng Kang $\&$ Shang Zai-jiu 1995).Let $R ( z )$ beadifferentiable functiondefinedina neighbourhoodof $z = 0$ and assume that $R ( 0 ) = 1$ and $R ^ { \prime } ( 0 ) = 1$ Then,wehave for $n \geq 3$

detR(A)=1 for all $n \times n$ matrices $A$ satisfying traceA=0,

ifandonlyif $R ( z ) = \exp ( z )$

Proof.The“ifpart follows fromLemma 3.1,because forconstant $A$ the solution of $Y = A Y$ , $Y ( 0 ) = I$ is given by $Y ( t ) = \exp ( { A t } )$

For theproof of the“only if”part,weconsider diagonal matrices of the form $A = \mathrm { d i a g } ( \mu , \nu , - ( \mu + \nu ) , 0 , \dots , 0 )$ ,which have trace $A = 0$ ,and forwhich

$$
R ( A ) = \mathrm { d i a g } \Big ( R ( \mu ) , R ( \nu ) , R ( - ( \mu + \nu ) ) , R ( 0 ) _ { \nu } . . . . , R ( 0 ) \Big ) .
$$

The assumptions $R ( 0 ) = 1$ and (3.2) imply

$$
R ( \mu ) R ( \nu ) R ( - ( \mu + \nu ) ) = 1
$$

forall $\mu , \nu$ close to0.Putting $\nu = 0$ ,this relation yields $R ( \mu ) R ( - \mu ) = 1$ forall $\mu$ , and therefore(3.3) can bewritten as

$$
R ( \mu ) R ( \nu ) = R ( \mu + \nu ) \qquad { \mathrm { f o r ~ a l l ~ } } \mu , \nu { \mathrm { ~ c l o s e ~ t o ~ } } 0 .
$$

This functional equation can only be satisfied by the exponential function.Thisis seenas follows:from(3.4）we have

$$
{ \frac { R ( \mu + \varepsilon ) - R ( \mu ) } { \varepsilon } } = R ( \mu ) { \frac { R ( \varepsilon ) - R ( 0 ) } { \varepsilon } } .
$$

Taking the limit $\varepsilon  0$ we obtain $R ^ { \prime } ( \mu ) = R ( \mu )$ ,because $R ^ { \prime } ( 0 ) = 1 .$ Thisimplies $R ( \mu ) = \exp ( \mu )$ □

Theorem3.3.For $n \geq 3$ ,noRunge-Kutta method can conserveall polynomial invariants ofdegree $_ { n }$ ,

Proof.Itis sufficient to consider linear problems $\dot { Y } = A Y$ with constant matrix $A$ satisfying trace $A = 0$ ,sothat $g ( Y ) = \operatorname* { d e t } Y$ isapolynomial invariant of degree $n$ .Applyinga Runge-Kutta method to such adifferential equation yields $Y _ { 1 } ~ =$ $R ( h A ) Y _ { 0 }$ ,where

$$
R ( z ) = 1 + z b ^ { T } ( I - z A ) ^ { - 1 } \mathbb { 1 }
$$

$( b ^ { T } = ( b _ { 1 } , \dots , b _ { s } )$ ， $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T }$ and $\mathbf { \mathcal { A } } \mathbf { \mathcal { \mathbf { \Phi } } } = \mathbf { \Phi } ( a _ { i j } )$ is the matrix of Runge-Kutta coefficients） is the so-called stability function.It is seen to be rational. ByLemma 3.2 itis therefore not possible that det $R ( h A ) ~ = ~ 1$ forall $A$ with trace $A = 0$ . □

This negativeresult motivates the search for new methods which can conserve polynomialinvariants(see Sects.IV.4,IV.8 and VI.9).Weconsider here another interestingclass of problemswith polynomial invariants of degree higher than two.

# IV.3.2 Isospectral Flows

Suchflowsare created byamatrixdifferential equation

$$
{ \dot { L } } = [ B ( L ) , L ] , \qquad L ( 0 ) = L _ { 0 }
$$

where $L _ { 0 }$ isa given symmetric matrix, $B ( L )$ isskew-symmetric for all $\mathcal { L }$ ,and $\left[ B , L \right] = B L - L B$ is the commutator of $B$ and $L .$ Many interesting problems can bewritten in this form.We just mention the Toda system,thecontinuous realization ofQR-type algorithms,projected gradient flows,and inverse eigenvalue problems (seeChu(1992)andCalvo,Iserles&Zanna(1997) forlong listsofreferences).

Lemma 3.4(Lax1968,Flaschka 1974).Let $L _ { 0 }$ be symmetric and assume that $B ( L )$ isskew-symmetricforall $\mathcal { L }$ Then,thesolution $L ( t )$ of(3.5)isa symmetric matrix,anditseigenvaluesare independentof $t$ .

Proof.The symmetry of $L ( t )$ follows from the fact that the commutator ofa skewsymmetric with asymmetric matrix givesa symmetric matrix.

To prove thesospectralityoftheflow,wedefine $U ( t )$ by

$$
{ \dot { U } } = B \big ( { \boldsymbol { L } } ( t ) \big ) U , \qquad U ( 0 ) = I .
$$

Then,we have $( d / d t ) ( U ^ { - 1 } L U ) ~ = ~ U ^ { - 1 } ( \dot { L } = B L + L B ) U ~ = ~ 0$ and hence $U ( t ) ^ { - 1 } L ( t ) U ( t ) = L _ { 0 }$ forall $t$ ,sothat $L ( t ) ~ = ~ U ( t ) L _ { 0 } U ( t ) ^ { - 1 }$ is the solution of(3.5).This proves the result. □

Note that, since $B ( L )$ is skew-symmetric,thematrix $U ( t )$ of (3.6) is orthogonal by Theorem 1.6.

Lema4oeactes $\begin{array} { r } { \operatorname* { d e t } ( L - \lambda I ) = \sum _ { i = 0 } ^ { n } a _ { i } \lambda ^ { i } } \end{array}$ and hence the coefficients $a _ { i }$ alsoare independent of $t$ These coefficients areall polynomial invariants(e.g., $a _ { 0 } ~ = ~ \operatorname* { d e t } L$ ， $a _ { n - 1 } ~ = ~ \pm \mathrm { t r a c e } { \cal L } )$ Because of Theorem3.3 there is no hopethat Runge-Kutta methodsappliedto（3.5） canconserve these invariantsautomatically for $n \geq 3$ .

Isospectral Methods.Theproof ofLemma 3.4,however,suggests an interesting approach for the numerical solution of(3.5).For $n = 0 , 1 , \ldots$ we solve numerically

$$
\begin{array} { r } { \dot { U } = B ( U L _ { n } U ^ { T } ) U , \qquad U ( 0 ) = I } \end{array}
$$

and we put $L _ { n + 1 } = \hat { U } L _ { n } \hat { U } ^ { T }$ ,where $\hat { U }$ is the numerical approximation $\widehat { U } \approx U ( h )$ after one step (cf.Calvo,Iserles $\&$ Zanna 1999).If $B ( L )$ is skew-symmetric for all matrices $L$ ,then $U ^ { T } U$ isaquadratic invariant of(3.7)and the methods of Sect.IV.2 will produce an orthogonal $\hat { U }$ .Consequently, $L _ { n + 1 }$ and $L _ { n }$ have exactly the same eigenvalues,and theyremainsymmetric.

Diele,Lopez $\&$ Politi（1998） suggest theuse of the Cayley transform $U =$ $( I - Y ) ^ { - 1 } ( I + Y ) ,$ which transforms (3.7)into

$$
\begin{array} { r } { \dot { Y } = \frac { 1 } { 2 } ( I - Y ) B \big ( U L _ { n } U ^ { T } \big ) ( I + Y ) , \qquad Y ( 0 ) = 0 , } \end{array}
$$

and the orthogonality of $U$ into the skew-symmetry of $Y$ (see Lemma 8.8 below). Since all (also explicit)Runge-Kutta methods preserve the skew-symmetry of $Y$ , whichisalinear invariant,this yieldsanapproach toexplicit isospectral methods.

Connection with theQR Algorithm.Ina diversion from the main theme of this section,we nowshowtherelationshipof the flowof(3.5)with theQRalgorithm for thesymmetric eigenvalue problem.Starting fromareal symmetric matrix $A _ { 0 }$ ,the basic $\mathcal Q R$ algorithm(without shifts） computesa sequence of orthogonally similar matrices $A _ { 1 } , A _ { 2 } , A _ { 3 } , \ldots$ ,expected toconverge towardsadiagonal matrix carrying theeigenvalues of $A _ { 0 }$ Iteratively for $k = 0 , 1 , 2 , . . . ,$ one computes the QR decomposition of $A _ { k }$ :

$$
\boldsymbol { A } _ { k } = \boldsymbol { Q } _ { k } \boldsymbol { R } _ { k }
$$

with $Q _ { k }$ orthogonal, $\scriptstyle R _ { k }$ upper triangular (the decomposition becomes unique if the diagonal elements of $R _ { k }$ are taken positive).Then, $A _ { k + 1 }$ is obtained by reversing the order of multiplication:

$$
\boldsymbol { A } _ { k + 1 } = \boldsymbol { R } _ { k } \boldsymbol { Q } _ { k } .
$$

Itisan easy exercise to show that $Q ( k ) = Q _ { 0 } Q _ { 1 } \ldots Q _ { k - 1 }$ is the matrix in the orthogonal similarity transformation between $A _ { 0 }$ and $A _ { k }$ ：

$$
A _ { k } = Q ( k ) ^ { T } A _ { 0 } Q ( k )
$$

and the same matrix $Q ( k )$ is the orthogonal factor inthe QR decomposition of $A _ { 0 } ^ { k }$

$$
A _ { 0 } ^ { k } = Q ( k ) R ( k ) .
$$

Consider now,foran arbitraryreal function $f$ defined on the eigenvalues ofareal symmetricmatrix $L _ { 0 }$ ,theQRdecomposition

$$
\exp ( t f ( L _ { 0 } ) ) = Q ( t ) R ( t )
$$

anddefine

$$
\boldsymbol { L } ( t ) : = \boldsymbol { Q } ( t ) ^ { T } \boldsymbol { L } _ { 0 } \boldsymbol { Q } ( t ) .
$$

Therelations(3.8)and(3.9)then show that for integer times $t \ = \ k$ ,thematrix $\exp \bigl ( f ( L ( k ) ) \bigr ) = Q ( k ) ^ { T } \exp \bigl ( f ( L _ { 0 } ) \bigr ) Q ( k )$ coincides with the kth matrix in the QR algorithmstarting from $A _ { 0 } = \exp ( f ( L _ { 0 } ) )$ ：

$$
\exp ( f ( L ( k ) ) ) = A _ { k } ~ .
$$

Now,how isall thisrelated tothesystem(3.5）？Differentiating(3.11)asinthe proofofLemma 3.4showsthat $L ( t )$ solves adifferential equation of the form $\dot { L } =$ $[ B , L ]$ with the skew-symmetricmatrix $B = - Q ^ { T } Q$ Atfirst sight,however, $B$ isa function of $t$ ,notof $\mathcal { L }$ .Ontheother hand,differentiationof(3.1O)yields (omiting theargument $t$ where it is clear from the context)

$$
f ( L _ { 0 } ) Q R = f ( L _ { 0 } ) \exp ( t f ( L _ { 0 } ) ) = \exp ( t f ( L _ { 0 } ) ) f ( L _ { 0 } ) = \dot { Q } R + Q \dot { R } ,
$$

and since $f ( L ) = Q ^ { T } f ( L _ { 0 } ) Q$ by (3.11), this becomes

$$
f ( L ) = Q ^ { T } \dot { Q } + \dot { R } R ^ { - 1 } .
$$

Herethe left-handside isasymmetricmatrix,and theright-hand sideis thesumofa skew-symmetric and an upper triangular matrix.It follows that the skew-symmetric matrix $B = - Q ^ { T } Q$ is given by

$$
B ( L ) = f ( L ) _ { + } - f ( L ) _ { + } ^ { T } ,
$$

where $f ( L ) _ { + }$ denotes the part of $f ( L )$ above the diagonal. Hence, $L ( t )$ is the solution of an autonomous system(3.5)with askew-symmetric $B ( L )$

For $f ( x ) = x$ and assuming $L _ { 0 }$ symmetricand tridiagonal,the flow of(3.5)with (3.13)isknownas the Toda flow.TheQR iterates $A _ { 0 } = \exp ( L _ { 0 } )$ ， $A _ { 1 }$ , $A _ { 2 } , \ldots$ ofthe exponential of $L _ { 0 }$ are seen to be equal to the exponentials of the solution $L ( t )$ of theToda equationsat integer times: $A _ { k } = \exp ( L ( k ) )$ ,adiscovery of Symes(1982). Aninteresting connection of the Toda equationswith a mechanical system will be discussed in Sect.X.1.5.

For $f ( x ) = \log x$ ,theabove arguments show that theQR iteration itself,starting fromapositive definite symmetric tridiagonal matrix,is the evaluation $A _ { k } = L ( k )$ atinteger times of a solution $L ( t )$ of thedifferential equation (3.5）with $B$ given by(3.13).This relationshipwas explored ina series ofpapers byDeift,Li,Nanda &Tomei（1983,1989,1993).

Notwithstanding the mathematical beauty of thisrelationship,it must beremarked that thepractical QRalgorithm(with shiftsand deflation) followsadifferent path.

# IV.4 Projection Methods

Und bist du nicht willig,so brauch ich Gewalt.

(J.W.Goethe,Der Erlkonig)

Suppose we have an $( n - m )$ -dimensional submanifold of $\mathbb { R } ^ { n }$ ,

$$
M = \{ y \ ; \ g ( y ) = 0 \}
$$

$g : \mathbb { R } ^ { n }  \mathbb { R } ^ { m } ,$ ,andadifferential equation $\dot { y } = f ( y )$ with the property that

$$
y _ { 0 } \in \mathcal { M } \qquad \mathrm { i m p l i e s } \qquad y ( t ) \in \mathcal { M } \ \mathrm { f o r ~ a l l } \ t .
$$

Wewant to emphasize that this assumption isweaker than the requirement that all components $g _ { i } ( y )$ of $g ( y )$ areinvariantsin the sense of Definition 1.1.In fact, assumption (4.2) is equivalent to $g ^ { \prime } ( y ) f ( y ) = 0$ for $y \in \mathcal { M }$ ,whereas Definition 1.1 requires $g ^ { \prime } ( y ) f ( y ) = 0$ forall $y \in \mathbb { R } ^ { n }$ In the situation of(4.2）we call $g ( y )$ aweak invariant,and we say that $\dot { y } = f ( y )$ isadifferential equation on the manifold $\mathcal { M }$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/3ab983124389e89445a7eb01c309f34259d42181794874fbc060395c3a7c3626.jpg)  
Fig.4.1.The implicit midpoint rule applied to thedifferential equation(4.3).Thepicture shows the numerical values for $q _ { 1 } ^ { 2 } + \dot { q } _ { 2 } ^ { 2 }$ obtained with step size $h = 0 . 1$ （thick line）and $h = 0 . 0 5$ (thin line)

Example 4.1. Consider the pendulum equation written in Cartesian coordinates:

$$
\begin{array} { r l } { \dot { q } _ { 1 } = p _ { 1 } , \quad } & { { } \dot { p } _ { 1 } = - q _ { 1 } \lambda , } \\ { \dot { q } _ { 2 } = p _ { 2 } , \quad } & { { } \dot { p } _ { 2 } = - 1 - q _ { 2 } \lambda , } \end{array}
$$

where $\lambda = ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } - q _ { 2 } ) / ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) .$ One can check by differentiation that $q _ { 1 } p _ { 1 } +$ $q _ { 2 } p _ { 2 }$ (orthogonality of the position and velocity vectors) isan invariant in the sense of Definition 1.1.However, $q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 }$ (length of the pendulum)is only aweak invariant. Theexperiment of Fig.4.1 shows that even methodswhich conserve quadratic first integrals(cf.Sect.IV.2) do not conserve the quadraticweak invariant $q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } .$ No numerical method thatisallowed to evaluate the vectorfield $f ( y )$ outside $\mathcal { M }$ can beexpected to conserve weak invariants exactly.Thisis one of the motivations for considering the methods of this and the subsequent sections.

Anatural approach to the numerical solution of differential equations on manifoldsis byprojection(seee.g.,Hairer&Wanner(1996),Sect.VII.2,Eich-Soellner &Fuhrer(1998),Sect.5.3.3).

Algorithm4.2 (Standard Projection Method).Assume that $y _ { n } \in M$ Onestep $y _ { n } \mapsto y _ { n + 1 }$ isdefined asfollows(seeFig.4.2):

Compute $\widetilde { y } _ { n + 1 } = \varPhi _ { h } ( y _ { n } )$ where $\varPhi _ { h }$ isanarbitrary one-stepmethodapplied to $\dot { y } = f ( y )$ ; ·project the value $y _ { n + 1 }$ onto themanifold $\mathcal { M }$ to obtain $y _ { n + 1 } \in \mathcal { M }$ .

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/45c8fba811bd1f8752061b61f7a550893f53ef01596e7bfc5de0414f2299480a.jpg)  
Fig.4.2.Illustration of the standard projection method

For $y _ { n } \in { \mathcal { M } }$ thedistance of $\widetilde { y } _ { n + 1 }$ to themanifold $\mathcal { M }$ is of the size of the local error,i.e., ${ \mathcal { O } } ( h ^ { p + 1 } )$ Therefore,the projection does not deteriorate the convergence orderof themethod.

For the computation of $y _ { n + 1 }$ we have to solve the constrained minimization problem

$$
\| y _ { n + 1 } - { \widetilde { y } } _ { n + 1 } \| \to \operatorname* { m i n } \qquad \mathrm { s u b j e c t ~ t o } \qquad g ( y _ { n + 1 } ) = 0 .
$$

In thecase of the Euclidean norm,astandard approach is to introduceLagrange multipliers $\lambda = ( \lambda _ { 1 } , \ldots , \lambda _ { m } ) ^ { I }$ and toconsider theLagrange function ${ \mathcal { L } } ( y _ { n + 1 } , \lambda ) =$ $\lVert y _ { n + 1 } - \widetilde { y } _ { n + 1 } \rVert ^ { 2 } / 2 - g ( y _ { n + 1 } ) ^ { T } \lambda .$ The necessary condition $\partial \mathcal { L } / \partial y _ { n + 1 } = 0$ then leads tothe system

$$
\begin{array} { r c l } { { y _ { n + 1 } } } & { { = } } & { { \widetilde { y } _ { n + 1 } + g ^ { \prime } ( \widetilde { y } _ { n + 1 } ) ^ { T } \lambda } } \\ { { 0 } } & { { \stackrel { , } { = } } } & { { g ( y _ { n + 1 } ) . } } \end{array}
$$

We have replaced $y _ { n + 1 }$ with $y _ { n + 1 }$ in the argument of $g ^ { \prime } ( y )$ in order to save some evaluations of $g ^ { \prime } ( y ) .$ Inserting the first relation of(4.5)into the second gives a nonlinear equation for $\lambda$ ,which can be efficiently solved by simplified Newton iterations:

$$
\begin{array} { r } { \varDelta \lambda _ { i } = - \Bigl ( g ^ { \prime } ( \widetilde { y } _ { n + 1 } ) g ^ { \prime } ( \widetilde { y } _ { n + 1 } ) ^ { T } \Bigr ) ^ { - 1 } g \Bigl ( \widetilde { y } _ { n + 1 } + g ^ { \prime } ( \widetilde { y } _ { n + 1 } ) ^ { T } \lambda _ { i } \Bigr ) , \qquad \lambda _ { i + 1 } = \lambda _ { i } + g ^ { \prime } ( \widetilde { y } _ { n + 1 } ) ^ { T } \lambda _ { i } . } \end{array}
$$

For the choice $\lambda _ { 0 } \stackrel { \_ } { = } 0$ the first increment $\varDelta \lambda _ { 0 }$ is of size $\mathcal { O } ( h ^ { p + 1 } )$ ,so that the convergenceisusually extremely fast.Often,one simplified Newton iteration is suficient.

Example4.3.Asa first exampleweconsider the perturbed Keplerproblem (see Exercise I.12）with Hamiltonian function

$$
\begin{array} { l } { { H ( p , q ) ~ = ~ { \displaystyle { \frac { 1 } { 2 } } } \left( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } \right) - { \displaystyle { \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } } } } } \\ { { ~ - ~ { \displaystyle { \frac { 0 . 0 0 5 } { 2 \sqrt { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 } } } } } , } } \end{array}
$$

and initial values $q _ { 1 } ( 0 ) ~ = ~ 1 - e , ~ q _ { 2 } ( 0 ) ~ = ~ 0 ,$ $p _ { 1 } ( 0 ) = 0$ , $p _ { 2 } ( 0 ) = \sqrt { ( 1 + e ) / ( 1 - e ) }$ (eccentricity $e = 0 . 6$ )ontheinterval $0 \leq t \leq 2 0 0 .$ The exact solution (plotted to the right) is approximately anelipse that rotates slowly around one of its foci.For this problem we knowtwo first integrals:the Hamiltonian function $H ( p , q )$ and the angular momentum $L ( p , q ) = q _ { 1 } p _ { 2 } - q _ { 2 } p _ { 1 }$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/8d39391d14a72f9dcafd8629e76dbc90a2f06387c41998fcdc0699e271f1f37f.jpg)

Weapply theexplicit Euler method and the symplectic Euler method (I.1.9), both with constant step size $h ~ = ~ 0 . 0 3$ Theresult is shown inFig.4.3.The numerical solution of the explicit Euler method (without projection）iscompletely wrong.The projection onto the manifold $\{ H ( p , q ) = H ( p _ { 0 } , q _ { 0 } ) \}$ improves the numerical solution,but it stillhasa wrongqualitative behaviour.Only projection onto both invariants, $H ( p , q ) = C o n s t$ and $L ( p , q ) = C o n s t$ gives the correct behaviour.The symplectic Euler method already shows the correct behaviour without anyprojections (see Chap.IX for an explanation).Surprisingly,aprojection onto $H ( p , q ) = C o n s t$ destroys this behaviour,the numerical solution approaches the centreand the simplified Newton iterationsfail to converge beyond $t = 2 5 . 2 3$ Projection onto both invariants re-establishes the correct behaviour.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/89e5ff192ff966d56cfe19ea6b7f3cc866d645d0a94cb2afcb2ae6b99b25857e.jpg)  
Fig.4.3.Numerical solutions obtained withand without projections

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/ef8b86cddd2ce6988ef847c387b6b2a1a7e53b924de2073c1e233cc43f7116a3.jpg)  
Fig.4.4.Explicit Euler method with projections applied to the outer solar system,step size $h = 1 0$ (days）,interval $0 \leq t \leq 2 0 0 0 0 0$

Example4.4 (Outer Solar System).Having encountered excellent experience with projections onto $H$ and $L$ forthe perturbed Kepler problem(Example4.3), letusapplythe same idea toamorerealisticproblem incelestial mechanics.We consider the outer solar system as described in Sect.I.2.The numerical solution ofthe explicit Euler method applied with constant step size $h = 1 0$ ,oncewith projection onto $H ~ = ~ C o n s t$ and once with projection onto $H ~ = ~ C o n s t$ and $L = C o n s t$ $\begin{array} { r } { L ( p , q ) = \sum _ { i = 1 } ^ { N } q _ { i } \times p _ { i } } \end{array}$

Eulermethod without projections,see Fig.I.2.4),but the orbit of Neptune becomes evenworse.There is no doubt that thisproblem contains a structure which cannot becorrectly simulated by methods that only preserve the total energy $H$ and the angularmomentum $L$

Example4.5 (Volume Preservation). Consider the matrix differential equation $\dot { Y } = A ( Y ) Y$ ,wheretrace $A ( Y ) = 0$ forall $Y$ Weknow fromLemma 3.1 that $g ( Y ) = \operatorname* { d e t } Y$ isaninvariant which cannot beautomaticallyconserved by Runge-Kutta methods.Here,we show howwe can enforce this invariant by projection.Let $Y _ { n + 1 }$ bethenumerical approximation obtained withan arbitrary one-step method. WeconsiderteFrobenius norm $\| Y \| _ { F } = \sqrt { \textstyle \sum _ { i , j } | y _ { i j } | ^ { 2 } }$ for measuring the distance tothemanifold $\{ Y \colon g ( Y ) = 0 \}$ .Using $g ^ { \prime } ( Y ) ( A Y ) = \operatorname { t r a c e } A \operatorname* { d e t } Y$ (see the proof ofLemma 3.1）with $A$ chosen such that the product $A Y$ contains only one non-zero element,the projection step (4.5）is seen to become(Exercise9)

$$
Y _ { n + 1 } = \widetilde { Y } _ { n + 1 } + \mu \widetilde { Y } _ { n + 1 } ^ { - T }
$$

with the scalar $\mu ~ = ~ \lambda \operatorname* { d e t } Y _ { n + 1 }$ .This leads to the scalar nonlinear equation $\operatorname* { d e t } \left( Y _ { n + 1 } + \mu Y _ { n + 1 } ^ { - T } \right) = \operatorname* { d e t } Y _ { n }$ forwhichsimplifedNewtonteatioseoe

$$
\operatorname* { d e t } \Bigl ( \widetilde { Y } _ { n + 1 } + \mu _ { i } \widetilde { Y } _ { n + 1 } ^ { - T } \Bigr ) \Bigl ( 1 + ( \mu _ { i + 1 } - \mu _ { i } ) \operatorname { t r a c e } \bigl ( ( \widetilde { Y } _ { n + 1 } ^ { T } \widetilde { Y } _ { n + 1 } ) ^ { - 1 } \bigr ) \Bigr ) = \mathrm { d e t } Y _ { n } .
$$

If the $Q R$ -decomposition_of $Y _ { n + 1 }$ is available from the computation of det $\widetilde { Y } _ { n + 1 }$ the value of $\mathrm { t r a c e } \big ( ( Y _ { n + 1 } ^ { T } Y _ { n + 1 } ) ^ { - 1 } \big )$ canbecomputedeffcientlywith $\mathcal { O } ( n ^ { 3 } / 3 )$ fops (seee.g.,Golub $\&$ VanLoan (1989),Sect.5.3.9).

The above projection is preferable to $Y _ { n + 1 } = c Y _ { n + 1 }$ where $c \in \mathbb { R }$ ischosen such that $\operatorname* { d e t } Y _ { n + 1 } = \operatorname* { d e t } Y _ { n }$ .This latter projectionis alreadyil-conditioned for diagonal matriceswith entriesthat differby several magnitudes.

Asaconclusion to the above numerical experiments we see that a projection can give excellent results,but can also destroy the good long-time behaviour of the solutionifapplied inappropriately.If theoriginal methodalready preservessome structure,thenprojection toa subset of invariantsmay destroy the good long-time behaviour.Animportantmodification forreversible differential equations(symmetricprojections)will be presented in Sect.V.4.1.

# IV.5Numerical Methods Based on Local Coordinates

Asecond importantclass ofmethods for the numerical treatment ofdifferential equations on manifolds uses local coordinates.Before explaining the ideas,we find it appropriate to discuss in more detail manifoldsand differential equations on manifolds.

# IV.5.1Manifolds and the Tangent Space

InSect.IV.4 we assumed that locally (inaneighbourhood $U$ of $a \in \mathbb { R } ^ { n }$ )amanifold is given by constraints,i.e.,

$$
{ \mathcal { M } } = \{ y \in U \ ; \ g ( y ) = 0 \} ,
$$

where $g : U \to \mathbb { R } ^ { m }$ isdifferentiable, $g ( a ) = 0$ ,and $g ^ { \prime } ( a )$ has full rank $_ { f l }$ .

Here,we use local parameters to characterizea manifold.Let $\psi : V \to \mathbb { R } ^ { n }$ be differentiable（ $V \subset \mathbb { R } ^ { n - m }$ isaneighbourhood of $_ 0$ ), $\psi ( 0 ) = \alpha$ ,and assume that $\psi ^ { \prime } ( 0 )$ has full rank $n - m .$ Then,amanifold is locally given by

$$
{ \mathcal { M } } = \{ y = \psi ( z ) ; z \in V \}
$$

provided that $V$ issufficiently small,so that $\psi : V \to \psi ( V )$ is bijective with continuous inverse.The variables $z$ arecalled parametersorlocal coordinatesof themanifold.

Asanexample,consider the unit sphere which,in the form (5.1),is given by the function $g ( y _ { 1 } , y _ { 2 } , y _ { 3 } ) = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } - 1 ,$ Thereare many possible choices of local coordinates.Away from the equator (i.e., $y _ { 3 } = 0$ ,wecan take $z = ( z _ { 1 } , z _ { 2 } ) ^ { T } : =$ $( y _ { 1 } , y _ { 2 } ) ^ { T }$ and $\psi ( z ) = \left( z _ { 1 } , z _ { 2 } , \pm \sqrt { 1 - z _ { 1 } ^ { 2 } - z _ { 2 } ^ { 2 } } \right) ^ { l } .$ Alternatively，we can consider away from the north and south poles (i.e., $y _ { 1 } = y _ { 2 } = 0$ , $y _ { 3 } = \pm 1$ ).

Thetangent toacurve (or the tangent plane to a surface） isanaffine space passing through the contact point $a \in \mathcal { M }$ It isconvenient to place the origin at $a$ , sothatwe obtaina vector space.More precisely,fora manifold $\mathcal { M }$ we define the tangent spaceat $a \in \mathcal { M }$ as

Lemma5.1.If themanifold $\mathcal { M }$ is given by(5.1）,where $g : U  \mathbb { R } ^ { m }$ isdifferentiable, $g ( a ) = 0$ ,and $g ^ { \prime } ( a )$ has full rank ${ a n }$ ,thenwehave

$$
T _ { a } { \mathcal { M } } = \ker g ^ { \prime } ( a ) = \{ v \in \mathbb { R } ^ { n } | g ^ { \prime } ( a ) v = 0 \} .
$$

f $\mathcal { M }$ is given by(5.2）,where $\psi : V \to \mathbb { R } ^ { n }$ isdifferentiable, $\psi ( 0 ) = a ,$ and $\psi ^ { \prime } ( 0 )$ hasfull rank $n - m$ ,thenwehave

$$
T _ { a } { \mathcal { M } } = \operatorname { I m } \psi ^ { \prime } ( 0 ) = \{ \psi ^ { \prime } ( 0 ) w | w \in \mathbb { R } ^ { n - m } \} .
$$

Proof.a)Forapath $\gamma ( t )$ satisfying $\gamma ( 0 ) = a$ and $g ( \gamma ( t ) ) = 0$ it followsbydifferentiation that $g ^ { \prime } ( a ) \dot { \gamma } ( 0 ) = 0$ Consequently,we have $T _ { a } { \mathcal { M } } \subset \ker g ^ { \prime } ( a )$

Consider now the function $F ( t , u ) = g ( a + t v + g ^ { \prime } ( a ) ^ { T } u ) .$ Wehave $F ( 0 , 0 ) = 0$ andan invertible $\partial F / \partial u ( 0 , 0 ) = g ^ { \prime } ( a ) g ^ { \prime } ( a ) ^ { T }$ ,so that by the implicit function theorem therelation $F ( t , u ) = 0$ can be solved locally for $u = u ( t ) .$ If $v \in \ker g ^ { \prime } ( a )$ , it follows that $\dot { u } ( 0 ) = 0$ ,and thepath $\gamma ( t ) = a + t v + g ^ { \prime } ( a ) ^ { T } u ( t )$ satisfies all requirements of(5.3),so that also $T _ { a } { \mathcal { M } } \supset \ker g ^ { \prime } ( a )$

b)Assume $\mathcal { M }$ tobe givenby(5.2).Foranarbitrary $\eta : ( - \varepsilon , \varepsilon )  \mathbb { R } ^ { m }$ satisfying $\eta ( 0 ) = 0$ ,thepath $\gamma ( t ) = \psi { \bigl ( } \eta ( t ) { \bigr ) }$ liesin $\mathcal { M }$ andsatisfies $\dot { \gamma } ( 0 ) \doteq \psi ^ { \prime } ( 0 ) \dot { \eta } ( 0 ) .$ This proves $\operatorname { I m } \psi ^ { \prime } ( 0 ) \subset T _ { a } { \mathcal { M } }$

The assumption on the rank of $\psi ^ { \prime } ( 0 )$ implies that,aftera reordering of the components,we have $\psi ( z ) = ( \psi _ { 1 } ( z ) , \psi _ { 2 } ( z ) ) ^ { T }$ ,where $\psi _ { 1 } ( z )$ isalocal diffeomorphism(by the inverse function theorem).We show that every smooth path $\gamma ( t )$ in $\mathcal { M }$ can be written as $\gamma ( t ) = \psi ( \eta ( t ) )$ with some smooth $\eta ( t )$ .This thenimplies $T _ { a } { \mathrm { , } } M \subset { \mathrm { I m } } \psi ^ { \prime } ( 0 )$ Toprove this we split $\gamma ( t ) = ( \gamma _ { 1 } ( t ) , \gamma _ { 2 } ( t ) ) ^ { T }$ according to the partitioning of $\psi$ ,andwedefine $\eta ( t ) = \psi _ { 1 } ^ { - 1 } \big ( \gamma _ { 1 } ( t ) \big ) .$ Sincefor $\gamma ( t ) \in \mathcal { M }$ thesecond part $\gamma _ { 2 } ( t )$ is uniquely determined by $\gamma _ { 1 } ( t )$ ,this proves $\gamma ( t ) = \psi { \bigl ( } \eta ( t ) { \bigr ) }$ □

The proof of the preceding lemma shows the equivalence of the representations(5.1)and (5.2）of manifoldsin $\mathbb { R } ^ { n }$ .Let $\mathcal { M }$ be given by (5.1）,and assume that the columns of $Q$ form an orthogonal basis of $\mathbf { \Delta } T _ { a } \mathbf { \mathcal { M } }$ .Asin part (a) of the proof ofLemma 5.1 the condition $g ( a +$ $Q z + g ^ { \prime } ( a ) ^ { T } u ) = 0$ defines locally (close to $z = 0$ afunction $u ( z )$ which satisfies $u ( 0 ) =$ 0and $u ^ { \prime } ( 0 ) = 0$ .Hence,the manifold $\mathcal { M }$ is also givenby(5.2)with thefunction $\psi ( z ) = a + Q z + g ^ { \prime } ( a ) ^ { T } u ( z ) .$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/aba6776240cda2498950d1ba6f72d56a91cc48823683a151bedab3ae8ecfbdd9.jpg)

On the other hand, let $\mathcal { M }$ be given by(5.2).Part (b) of the proof ofLemma5.1 shows that $y = \psi ( z )$ can bepartitioned into $y _ { 1 } = \psi _ { 1 } ( z )$ and $y _ { 2 } = \psi _ { 2 } ( z )$ ,where $\psi _ { 1 }$ is alocal diffeomorphism.Consequently, $\mathcal { M }$ is also given by(5.1）with $g ( y ) =$ $y _ { 2 } - \psi _ { 2 } \big ( \psi _ { 1 } ^ { - 1 } \big ( y _ { 1 } \big ) \big )$ .

# IV.5.2Differential Equations on Manifolds

InSect.IV.4 we introduced differential equations on amanifold as problems satisfying(4.2）.With the help ofLemma5.1weare now inaposition tocharacterize such problemswithout knowledge of the solutions.

Theorem5.2. Let $\mathcal { M }$ beasubmanifoldof $\mathbb { R } ^ { n }$ Theproblem $\dot { y } = f ( y )$ isadifferentialequation onthe manifold $\mathcal { M }$ (i.e.,it satisfies(4.2)) ifand onlyif

$$
f ( y ) \in T _ { y } { \mathcal { M } } \qquad f o r a l l y \in { \mathcal { M } } .
$$

Proof.The necessity of(5.6) follows fromthe definition of $\mathcal { I } _ { y } \mathcal { M }$ ,because the exact solution of the differential equation lies in $\mathcal { M }$ and has $f ( y )$ asderivative.

Toprove the sufficiency,we assume(5.6)and let $\mathcal { M }$ be locally,near $y _ { 0 }$ ,begiven byaparametrization $y = \psi ( z )$ as in(5.2).We try to write the solution of $\dot { y } = f ( y )$ ， $y ( 0 ) = y _ { 0 } = \psi ( z _ { 0 } )$ as $y ( t ) = \psi ( z ( t ) ) .$ Ifthis isat all possible,then $z ( t )$ must satisfy

$$
\psi ^ { \prime } ( z ) \dot { z } = f { \big ( } \psi ( z ) { \big ) }
$$

which,byassumption(5.6)and the second part ofLemma5.1,is equivalent to

$$
\dot { z } = \psi ^ { \prime } ( z ) ^ { + } f \big ( \psi ( z ) \big ) ,
$$

where $A ^ { + } = ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ denotes the pseudo-inverse of a matrix with fullcolumn rank.Conversely,define $z ( t )$ as the solution of(5.7）with $z ( 0 ) = z _ { 0 }$ ,which isknown to exist locally in $t$ bythe standard existence and uniqueness theory of ordinary differential equations on $\mathbb { R } ^ { m }$ .Then $y ( t ) = \psi ( z ( t ) )$ is the solution of $\dot { y } = f ( y )$ with $y ( 0 ) = y _ { 0 }$ Hence,the solution $y ( t )$ remains in $\mathcal { M }$ . □

Weremark that the sufficiency proof of Theorem 5.2only requires the function $f ( y )$ to bedefined on $\mathcal { M }$ Due to the equivalence of $\dot { y } = f ( y )$ with（5.7） the problemis transportedto the space of local coordinates.The standard local theory for ordinary differential equations on an Euclidean space (existence and uniqueness of solutions,...) can thus be extended ina straightforward way to differential equations on manifolds,i.e., $\dot { y } = f ( y )$ with $f : \mathcal { M }  \mathbb { R } ^ { n }$ satisfying（5.6）.

# IV.5.3 Numerical Integrators on Manifolds

Whereas the projection methods of Sect.IV.4 require the function $f ( y )$ ofthedifferentialequationtobedefined inaneighbourhoodof $\mathcal { M }$ (seeFig.4.2）,thenumerical methods of this section evaluate $f ( y )$ onlyon the manifold $\mathcal { M }$ The ideais toapply thenumerical integrator in the parameter space rather than in the space where $\mathcal { M }$ is embedded.

Algorithm5.3(Local Coordinates Approach).Assume that $y _ { n } \in \mathcal { M }$ andthat $\psi$ isa local parametrization of $\mathcal { M }$ satisfying $\psi ( z _ { n } ) = y _ { n }$ Onestep $y _ { n } \mapsto y _ { n + 1 }$ is definedasfollows(seeFig.5.1):

Compute $\boldsymbol { z } _ { n + 1 } = \boldsymbol { \varPhi } _ { h } ( \boldsymbol { z } _ { n } )$ ,theresultofthemethod $\phi _ { h }$ applied to (5.7); define the numerical solutionby $y _ { n + 1 } = \psi ( z _ { n + 1 } )$

Itis importanttoremarkthattheparametrization $y = \psi ( z )$ can bechangedat every step.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/417d2d54773aa21b93f1a0ac36ac68b43241b482a5a8ff94ba9978bfa821e132.jpg)  
Fig.5.1.The numerical solution of differential equations on manifoldsvia local coordinates

Asindicatedat thebeginningof Sect.IV.5.1,there are many possble choices of local coordinates.Consider thependulum equation of Example 4.1,where $\mathcal { M } =$ $\{ ( q _ { 1 } , q _ { 2 } , p _ { 1 } , p _ { 2 } ) | q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } = 1 , q _ { 1 } p _ { 1 } + q _ { 2 } p _ { 2 } = 0 \} .$ A standard parametrization here is $q _ { 1 } = \sin \alpha$ , $q _ { 2 } = - \cos \alpha$ , $p _ { 1 } = \omega \cos \alpha$ ,and $p _ { 2 } = \omega \sin \alpha .$ In the new coordinates $( \alpha , \omega )$ the problem becomes simply $\dot { \alpha } = \omega$ , $\omega = - \sin \alpha .$ Other typical choices are theexponential map $\psi ( Z ) = \exp ( Z )$ fordifferential equations on Lie groups,and theCayley transform $\psi ( Z ) = ( I - Z ) ^ { - 1 } ( I + Z )$ forquadratic Lie groups.This will bestudiedin more detail in Sect.IV.8 below.Here we discuss two commonly used choices which do not use a special structure of the manifold.

Generalized Coordinate Partitioning,We assume that the manifold is given by (5.1).If $g : \mathbb { R } ^ { n } \to \mathbb { R } ^ { m }$ hasa Jacobian with full rank $m$ at $y = a$ ,wecan find a partitioning $y = ( y _ { 1 } , y _ { 2 } )$ ,suchthat $\partial g / \partial y _ { 2 } ( a )$ isinvertible.In this case we can choose thecomponents of $y _ { 1 }$ aslocal coordinates.The function $y = \psi ( z )$ is then given by $y _ { 1 } = z$ and $y _ { 2 } = \psi _ { 2 } ( z )$ ,where $\psi _ { 2 } ( z )$ isimplicitlydefined by $g ( z , \psi _ { 2 } ( z ) ) = 0$ . Thisapproach has been promotedbyWehage&Haug（1982)in the contextofconstrainedmechanical systems,and the partitioningis found by Gaussian elimination with full pivotingapplied to the matrix $g ^ { \prime } ( a )$ .Anotherway of finding the partitioning is by the use of the QR decomposition with column change.

Tangent Space Parametrization. Let the manifold $\mathcal { M }$ begiven by(5.1），and collect the vectors ofan orthogonal basis of $\mathbf { \Delta } _ { T _ { a } , M }$ in the matrix $Q$ We then consider theparametrization

$$
\psi _ { a } ( z ) = a + Q z + g ^ { \prime } ( a ) ^ { T } u ( z ) ,
$$

where $u ( z )$ is defined by $g ( \psi _ { a } ( z ) ) = 0$ ,exactlyasinthe discussionafter the proof ofLemma5.1.Differentiating（5.8)yields

$$
\big ( Q + g ^ { \prime } ( a ) ^ { T } u ^ { \prime } ( z ) \big ) \dot { z } = \dot { y } = f ( y ) = f \big ( \psi _ { a } ( z ) \big ) .
$$

Since $Q ^ { T } Q = I$ and $g ^ { \prime } ( a ) Q = 0$ ,thisrelationisequivalent tothediffrential equation

$$
\dot { z } = Q ^ { T } f \left( \psi _ { a } ( z ) \right) ,
$$

which corresponds to (5.7).If we apply anumerical method to (5.9),every function evaluation requires the projection of an element of the tangent space onto themanifold.Thisprocedureis illustrated inFig.5.1,and was originallyproposedbyPotra& Rheinboldt(1991） for the solution of the Euler-Lagrange equations of constrained multibody systems(see also Hairer&Wanner(1996),p.476).

# IV.6 Differential Equations on Lie Groups

Theorem 1.6andLemma 3.1areparticu-Iar cases of amore general result which can beconveniently formulated with theconcept ofLiegroups and Lie algebras (see Olver (1986)andVaradarajan (1974) foran introduction to these subjects).

ALiegroup isa group $G$ which isadifferentiable manifold,and for which the productisadifferentiable mapping $G \times G \to G$ Werestrict our considerations to matrix Lie groups,that is,Lie groups which are subgroupsof ${ \mathrm { G L } } ( n )$ ,thegroup of invertible $n \times n$ matrices with the usual matrix product as the group operation.

Example6.1.An important exampleof a Lie group is the group

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/53bf3aa1028c605873e131ba5dd411a61ddf60f5127fd006168e309f72c45af3.jpg)  
Marius Sophus Lie3

$$
{ \mathrm { O } } ( n ) = \left\{ Y \in { \mathrm { G L } } ( n ) \mid Y ^ { T } Y = I \right\}
$$

of all orthogonal matrices.Itis the zero setof $g ( Y ) = Y ^ { T } Y - I ,$ ,where we consider $g$ asamapping from the set of all $n \times n$ matrices(i.e., $\mathbb { R } ^ { n \cdot n }$ tothe set of all symmetric matrices (whichcan beidentifed with $\mathbb { R } ^ { n ( n + 1 ) / 2 }$ .Thederivative $g ^ { \prime } ( Y )$ is surjective for $Y \in \mathrm { O } ( n )$ ,because forany symmetricmatrix $K$ the choice $H =$ $Y K / 2$ solves the equation $g ^ { \prime } ( Y ) H = K .$ Therefore,the matrix $g ^ { \prime } ( Y )$ has fullrank (cf.(5.1））so that ${ \mathrm { O } } ( n )$ definesadifferentiable manifold of dimension $n ^ { 2 } - n ( n +$ $1 ) / 2 = n ( n - 1 ) / 2$ Theset ${ \mathrm { O } } ( n )$ is alsoa group with unit element $\mathcal { L }$ (the identity）. Since the matrix multiplication isa differentiablemapping, ${ \mathrm { O } } ( n )$ isaLie group.

Table 6.1 lists further prominent examples.The matrix $J$ appearing in thedefinitionof the symplectic group is the matrix determining the symplectic structure on $\nparallel \nparallel ^ { n }$ (see Sect.VI.2).

As the following lemma shows,the tangent space ${ \mathfrak { g } } = { \mathfrak { I } } _ { I } G$ at theidentity $\mathcal { I }$ of amatrix Lie group $G$ is closed under forming commutators of its elements.This makesganalgebra,theLiealgebraof theLie group $G$

Lemma 6.2(Lie BracketandLie Algebra).Let $G$ beamatrix Lie group and let ${ \mathfrak { g } } = { \mathfrak { L } } _ { I } G$ bethetangent spaceatthe identity.TheLie bracket(orcommutator)

$$
[ A , B ] = A B - B A
$$

definesan operation ${ \mathfrak { g } } \times { \mathfrak { g } } \to { \mathfrak { g } }$ whichis bilinear,skew-symmetric( $\left[ A , B \right] =$ $- [ B , A ] )$ ,andsatisfiestheJacobiidentity

$$
\left[ A , \left[ B , C \right] \right] + \left[ C , \left[ A , B \right] \right] + \left[ B , \left[ C , A \right] \right] = 0 .
$$

Table 6.1. Some matrix Lie groups and their corresponding Lie algebras   

<table><tr><td rowspan=1 colspan=1>Liegroup</td><td rowspan=1 colspan=1>Liealgebra</td></tr><tr><td rowspan=1 colspan=1>GL（n）={{Y|detY≠0}general linear group</td><td rowspan=1 colspan=1>g（(n）={A|arbitrary matrix}Liealgebra ofnXnmatrices</td></tr><tr><td rowspan=1 colspan=1>SL（n）={{Y|detY=1}special linear group</td><td rowspan=1 colspan=1>5[(n）={A|trace(A)=0}special linearLiealgebra</td></tr><tr><td rowspan=1 colspan=1>O（n）={{Y|YTY=I}orthogonal group</td><td rowspan=1 colspan=1>50(n）={A|AT+A=0}skew-symmetric matrices</td></tr><tr><td rowspan=1 colspan=1>sO(n）={{Y∈O(n）|detY=1}special orthogonal group</td><td rowspan=1 colspan=1>50(n）={A丨AT+A=0}skew-symmetricmatrices</td></tr><tr><td rowspan=1 colspan=1>Sp(n）={{Y|YTJY=J}symplectic group</td><td rowspan=1 colspan=1>sp(n）={A|JA+ATJ=0}</td></tr></table>

Proof.By definition of the tangent space,for $A , B \in { \mathfrak { g } }$ ,thereexistdifferentiable paths $\alpha ( t ) , \beta ( t )$ ( $| t | < \varepsilon )$ in $G$ such that $\alpha ( t ) = I + t A ( t )$ withacontinuous function $A ( t )$ with $A ( 0 ) = A$ ,andsimilarly $\beta ( t ) = I + t B ( t )$ with $B ( 0 ) = B .$ Nowconsider the path $\gamma ( t )$ in $G$ defined by

$$
\begin{array} { r } { \gamma ( t ) = \alpha ( \sqrt { t } ) \beta ( \sqrt { t } ) \alpha ( \sqrt { t } ) ^ { - 1 } \beta ( \sqrt { t } ) ^ { - 1 } , \quad t \geq 0 . } \end{array}
$$

An elementary computation then yields

$$
\gamma ( t ) = I + t [ A , B ] + o ( t ) .
$$

With the extension $\gamma ( t ) = \gamma ( - t ) ^ { - 1 }$ fornegative $t$ ,thisisadifferentiablepath in $G$ satisfying $\gamma ( 0 ) = I$ and $\dot { \gamma } ( 0 ) = [ A , B ]$ Hence $[ A , B ] \in { \mathfrak { g } }$ by definition of the tangent space.The properties of theLie bracket can beverified inastraightforward way. □

Example 6.3. Consider again the orthogonal group ${ \mathrm { O } } ( n )$ Since the derivative of $g ( Y ) = Y ^ { T } Y - I$ at the identity is $g ^ { \prime } ( I ) H = I ^ { T } H + H ^ { T } I = H + H ^ { T }$ it follows fromthe firstpart ofLemma5.1 that theLiealgebracorrespondingto ${ \mathrm { O } } ( n )$ consists ofall skew-symmetricmatrices.Theright column ofTable6.1 gives theLie algebras of the other Lie groups listed there.

Thefollowing basic lemma shows that the exponential map yieldsa local parametrization of theLie groupnear the identity,with theLiealgebra (a linear space) asthe parameter space.

Lemma6.4 (Exponential Map).Consideramatrix Liegroup $G$ andits Liealgebrag.The matrix exponential isamap

$$
\exp : { \mathfrak { g } } \to G ,
$$

i.e.,for $A \in { \mathfrak { g } }$ wehave $\exp ( A ) \in G .$ Moreoverexpisalocaldiffeomorphismin $a$ neighbourhoodof $A = 0$ .

Proof.For $A \in { \mathfrak { g } }$ ,it follows from the definition of the tangent space ${ \mathfrak { g } } = T _ { I } G$ that there exists adifferentiable path $\alpha ( t )$ in $G$ satisfying $\alpha ( 0 ) = I$ and ${ \dot { \alpha } } ( 0 ) = A$ .For afixed $Y \in G$ ,thepath $\gamma ( t ) : = \alpha ( t ) Y$ isin $G$ and satisfies $\gamma ( 0 ) = Y$ and ${ \dot { \gamma } } ( 0 ) =$ $A Y$ Consequently, $A Y \in T _ { Y } G$ and $Y = A Y$ defines adifferential equation on the manifold $G$ .The solution $Y ( t ) = \exp ( { t A } )$ is therefore in $G$ forall $t$ .

Since $\exp ( H ) - \exp ( 0 ) = H + \mathcal { O } ( H ^ { 2 } )$ ,the derivative of the exponential map at $A = 0$ isthe identity,and it follows from the inverse function theorem that expis alocal diffeomorphismcloseto $A = 0$ . □

Theproof ofLemma 6.4 shows that fora matrix Lie group $G$ the tangent space at $Y \in G$ has the form

$$
T _ { Y } { \cal G } = \{ A Y ~ | ~ A \in \mathfrak { g } \} .
$$

ByTheorem5.2,differential equations ona matrixLie group(considered asa manifold)can therefore bewritten as

$$
\dot { Y } = A ( Y ) Y
$$

where $A ( Y ) \in { \mathfrak { g } }$ forall $Y \in G .$ The following theorem summarizes this discussion, and extendsthe statements of Theorem1.6and Lemma3.1tomoregeneral matrix Lie groups.

Theorem 6.5. Let $G$ beamatrix Liegroup and $\mathfrak { g }$ itsLie algebra.If $A ( Y ) \in { \mathfrak { g } }$ for all $Y \in G$ andif $Y _ { 0 } \in G$ ,thenthe solutionof(6.4) satisfies $Y ( t ) \in G$ forall $t$ □

If inaddition $A ( Y ) \in { \mathfrak { g } }$ for all matrices $Y$ ,andif

$$
G = \{ Y \mid g ( Y ) = C o n s t \}
$$

is one of theLie groups of Table6.1,then $g ( Y )$ isan invariant of the differential equation (6.4) in the sense of Definition 1.1.

# IV.7 Methods Based on the Magnus Series Expansion

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0002_pages_0071-0140/auto/images/51ba8753b276c4b87319de624479f6f9bc0439ff2435d02b9aa5b4f34e419b39.jpg)  
WilhelmMagnus4

Before we discuss the numerical solution of differentialequations(6.4)onLie groups,let us give an explicit formula for the solution of linear matrix differential equations

$$
\begin{array} { r } { \dot { Y } = A ( t ) Y . } \end{array}
$$

No assumption on the matrix $A ( t )$ ismade for the moment (apart from continuous dependence on $t$ .For the scalar case,the solution of(7.1）with $Y ( 0 ) = Y _ { 0 }$ is given by

$$
Y ( t ) = \exp \Bigl ( \int _ { 0 } ^ { t } A ( \tau ) d \tau \Bigr ) Y _ { 0 } .
$$

Also in the case where the matrices $A ( t )$ and $\textstyle \int _ { 0 } ^ { t } A ( \tau ) d \tau$ commute,(7.2)is the solutionof (7.1).In the general non-commutative case

we follow the approach ofMagnus (1954)andwe search foramatrix function $\boldsymbol { \Omega } ( t )$ such that

$$
Y ( t ) = \exp \bigl ( \varOmega ( t ) \bigr ) Y _ { 0 }
$$

solves(7.1).The main ingredient for the solution will be the inverse of thederivative of the matrix exponential.It has beenstudied in Sect.II.4,Lemma III.4.2,and is givenby

$$
d \exp _ { \Omega } ^ { - 1 } ( H ) = \sum _ { k \geq 0 } \frac { B _ { k } } { k ! } \mathsf { a d } _ { \Omega } ^ { k } ( H ) ,
$$

where $B _ { k }$ are the Bernoulli numbers,and ad $\Omega ( A ) = [ \Omega , A ] = \Omega A - A \Omega$ isthe adjoint operator introduced in (III.4.1).

Theorem7.1 (Magnus1954).The solution ofthedifferentialequation(7.1) canbe written as $Y ( t ) = \exp ( \varOmega ( t ) ) Y _ { 0 }$ with $\boldsymbol { \Omega } ( t )$ definedby

$$
\dot { \Omega } = d \exp _ { \Omega } ^ { - 1 } \bigl ( A ( t ) \bigr ) , \qquad \Omega ( 0 ) = 0 .
$$

As longas $\| \boldsymbol { \Omega } ( t ) \| < \pi$ ,theconvergenceofthe $d \exp _ { \Omega } ^ { - 1 }$ expansion(7.3) is assured.

Proof.Comparing the derivativeof $Y ( t ) = \exp ( \varOmega ( t ) ) Y _ { 0 }$ ,

$$
\dot { Y } ( t ) = \left( \frac { d } { d \varOmega } \exp \varOmega ( t ) \right) \dot { \varOmega } ( t ) Y _ { 0 } = \left( d \exp _ { \varOmega ( t ) } \bigl ( \dot { \varOmega } ( t ) \bigr ) \right) \exp \bigl ( \varOmega ( t ) \bigr ) Y _ { 0 } ,
$$

with（7.1）we obtain $A ( t ) \ = \ d \exp _ { \Omega ( t ) } \big ( \hat { \Omega } ( t ) \big )$ Applying the inverse operator $\boldsymbol { d } \exp _ { \Omega } ^ { - 1 }$ tothisrelationyieldsthediferential equation(7.4)for $\boldsymbol { \Omega } ( t )$ Thestatement on the convergence isa consequence of Lemma III.4.2. □


<!-- chunk 0003: pages 141-210 -->
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

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/89609677d7357ca0ef2cff7ce3b209fb85231dc2069b33529002a9202dc3ce3a.jpg)  
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

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/8614f5d3a7629a93d63957166e6b3110839990fa178ebcbf1c6258999f4f1b0d.jpg)  
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

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/f66ff074a4db339cf74fcd15fa7be9974b6565a553031f3579353226361ef2ff.jpg)  
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

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/3ccc5179ddd3dbebbaa71885e8b29b6a7c03c443196a6023bff72cbc1c10d576.jpg)

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

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0003_pages_0141-0210/auto/images/42cf7cb01f5bf471fa640467621ea415e3619e11c132da9d68cef68dc83d59ae.jpg)  
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
