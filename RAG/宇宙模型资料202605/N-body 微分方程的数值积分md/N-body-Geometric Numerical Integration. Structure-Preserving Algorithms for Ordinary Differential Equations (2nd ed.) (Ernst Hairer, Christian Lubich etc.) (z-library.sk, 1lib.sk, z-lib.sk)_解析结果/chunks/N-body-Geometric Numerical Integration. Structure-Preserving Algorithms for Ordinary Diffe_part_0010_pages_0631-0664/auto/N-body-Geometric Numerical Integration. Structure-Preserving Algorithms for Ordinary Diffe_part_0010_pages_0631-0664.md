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