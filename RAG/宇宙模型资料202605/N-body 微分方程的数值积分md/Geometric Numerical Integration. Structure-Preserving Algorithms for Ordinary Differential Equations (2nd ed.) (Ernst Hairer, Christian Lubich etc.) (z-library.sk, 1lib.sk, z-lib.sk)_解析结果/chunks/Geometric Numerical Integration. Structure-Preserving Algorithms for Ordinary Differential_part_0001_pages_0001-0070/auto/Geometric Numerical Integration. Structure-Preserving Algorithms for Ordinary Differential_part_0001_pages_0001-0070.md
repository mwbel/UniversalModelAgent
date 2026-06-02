![](images/0dc4789619e3234dd293f0503c6b542ccad7cf060c27f02a256a2410a767ebed.jpg)

E.Hairer C. Lubich G.Wanner

# Geometric Numerical Integration

Structure-Preserving Algorithms for Ordinary Differential Equations

Second Edition

几何数值积分第2版

# 郑重声明

$\bullet$ 世界图书出版公司北京公司购权英文图书仅限在中国大陆销售，不得以任何方式销往中国大陆以外地区，一旦发现违规者，我公司将追究其法律责任，追偿其违规行为给本公司及合作方造成的经济损失。

●Thisreprint has beenauthorized by Springer Science & Business Media fordistribution in China Mainlandonlyand not for export therefrom.

# Ernst Hairer Christian Lubich Gerhard Wanner

# Geometric Numerical Integration

Structure-Preserving Algorithms for Ordinary Differential Equations

Second Edition

With I46 Figures

Ernst Hairer   
GerhardWanner   
Sectionde Mathematiques   
Universitede Geneve   
2-4rue du Lievre,C.P.64   
CH-121IGeneve4,Switzerland   
email:Ernst.Hairer $@$ math.unige.ch Gerhard.Wanner@math.unige.ch   
Christian Lubich   
Mathematisches Institut   
Universitat Tubingen   
AufderMorgenstelle10   
72076Tubingen,Germany   
email:Lubich@na.uni-tuebingen.de

ISSN 0179-3632 ISBN-1o 3-540-3o663-3Springer Berlin HeidelbergNew York ISBN-13 978-3-540-3o663-4Springer Berlin HeidelbergNew York ISBN-1O 3-540-430o3-2 ist EditionSpringer Berlin Heidelberg New York

Thiswork issubject tocopyright.Allrightsarereserved,whether thewholeorpart ofthematerial is concerned,seiiallyeghtsoaslaonringeuseofllutraoscitaionrosti reproductiononmicrofilmorinany otherwayand storageindata banks.Duplication ofthispublication orpartsthereof ispermitted only under theprovisions of theGerman Copyright Lawof September9, 1965,initscurrentversion,andpermission forusemust alwaysbeobtainedfrom Springer.Violationsare liable for prosecution under the German CopyrightLaw.

Theuseofgeneraldescriptivenames,registerednames,trademarks,etc.inthispublicationdoesnotimply evenintheabsence of aspecific statement,that such names areexempt from therelevant protective laws andregulations and therefore free for general use.

Reprint from English language edition:   
Geometric Numerical Integration:Structure-Preserving Algorithms forOrdinary Differential   
Equations Second Edition   
byE.Hairer,C.Lubich,G.Wanner   
Copyright $\circledcirc$ SpringerBerlin Heidelberg2002,2004,2006   
Springer Berlin Heidelberg isapart of Springer Science+Business Media   
AllRightsReserved

Thisreprint has been authorized by Springer Science& Business Media for distribution in ChinaMainlandonlyand not for export therefrom.

# 图书在版编目（CIP）数据

几何数值积分：第2版 $=$ Geometric Numerical Integration:Structure-Preserving  
Algorithms forOrdinaryDifferential Equations:英文/（瑞士）E.海尔（E.Hairer），  
（瑞士）C.卢比希（C.Lubich），（瑞士）G.万纳（G.Wanner）著.—影印本.一  
北京：世界图书出版公司北京公司，2016.10  
ISBN978-7-5192-1937-6

I. $\textcircled{1}$ 几…Ⅱ $\textcircled{1}$ E… $\textcircled{2}$ C.. $\textcircled{3}$ G…Ⅲ. $\textcircled{1}$ 几何积分论一英文 $\textcircled{2}$ 数值积分—英文IV. $\textcircled{1}$ 0177.8 $\textcircled{2}$ 0241.4

中国版本图书馆CIP数据核字（2016）第255266号

著者：E.Hairer,C.Lubich,G.Wanner  
责任编辑：刘慧高蓉  
装帧设计：任志远  
出版发行：世界图书出版公司北京公司  
地 址：北京市东城区朝内大街137号  
邮 编：100010话：010-64038355（发行） 64015580（客服）64033507（总编室）址：http://ww.wpchj.com.cn箱：wpcbjst@vip.163.com  
销 售：新华书店  
印 刷：三河市国英印务有限公司  
开 本： $7 1 1 \mathrm { m m } \times 1 2 4 5 \mathrm { m m }$ 1/24  
印 张：28  
字 数：537千  
版 次：2017年1月第1版 2017年1月第 $1$ 次印刷  
版权登记：01-2016-5267  
定价：120.00元

# 版权所有翻印必究

# Springer Series in Computational Mathematics

Editorial Board   
R.Bank   
R.L.Graham   
J.Stoer   
R.Varga   
H.Yserentant

# Preface to the First Edition

They throw geometry out the door,and it comes back through the window. (H.G.Forder,Auckland 1973,reading new mathematics at the age of 84)

The subject of this book is numerical methods that preserve geometric properties of theflowofadifferential equation:symplectic integrators for Hamiltonian systems, symmetric integrators forreversiblesystems,methodspreserving first integrals and numerical methods on manifolds,includingLie groupmethods and integrators for constrained mechanical systems,and methods for problemswith highly oscillatory solutions.Structure preservation-with itsquestionsas towhere,how,and what for -is the unifying theme.

Inthelast fewdecades,the theory of numerical methods for general (non-stiff andstiff)ordinary differential equationshasreachedacertainmaturity,and excellent general-purpose codes,mainly based onRunge-Kutta methods or linearmultistepmethods,have becomeavailable.The motivation for developing structurepreservingalgorithms for special classes of problems came independently from such different areas of research asastronomy,moleculardynamics,mechanics,theoretical physics,and numerical analysis aswell as from otherareas of both applied and puremathematics.It turned out that the preservation of geometric properties of the flownot only produces an improved qualitative behaviour,but alsoallows foramore accurate long-time integration than with general-purpose methods.

Animportant shift of view-point came about by ceasing to concentrate on the· numerical approximation ofa single solution trajectory and instead to consider a numerical method asadiscrete dynamical systemwhich approximatesthe flow of thedifferential equation-and so the geometry of phase space comes back again through thewindow.This view allowsa clearunderstanding of thepreservation of invariantsand of methods onmanifolds,ofsymmetryand reversibility ofmethods, andof the symplecticity of methodsand various generalizations.These subjectsare presented inChaptersIV throughVII of this book.ChaptersIthrough IIareofan introductory nature and present examples and numerical integrators together with important parts of the classical order theories and theirrecent extensions.Chapter VII dealswith questions of numerical implementationsand numerical merits of the various methods.

Itremains to explain the relationship between geometric properties of the numerical method and the favourable error propagation in long-time integrations.This

Backward error analysis Geometric integrators Long-time errors is doneusing the idea of backward error analysis,where the numerical one-step mapis interpreted as （almost) the flow ofamodified differential equation,which is constructed as an asymptotic series (Chapter IX).In this way,geometric properties ofthenumerical integrator translate into structure preservation on the level of the modified equations.Much insight and rigorous error estimates over long time intervalscan then beobtained by combiningthis backward error analysiswithKAM theoryand related perturbation theories.Thisis explained in ChaptersX through XI for Hamiltonian and reversible systems.Thefinal ChaptersXIII and XIV treat the numerical solution of differential equations with high-frequency oscillations and the long-time dynamics of multistep methods,respectively.

This book grew out of the lecture notes ofa course given by Ernst Hairer at theUniversity of Geneva duringthe academic year 1998/99.These lectureswere directed at studentsin the third and fourth year.Thereactions of studentsaswell as of many colleagues,who obtained the notes from the Web,encouraged us to elaborate our ideas to produce the present monograph.

Wewant to thank all those who have helped and encouraged us to prepare this book.Inparticular,Martin Hairer for hisvaluable help in installing computers and hisexpertisein Latex and Postscript,Jeff Cashand Robert Chan forreading the whole text and correcting countless scientifc obscurities and linguistic errors,Haruo Yoshida for making many valuable suggestions,Stephane Cirilli for preparing the filesforall thephotographs,and Bernard Dudez,the irreplaceable director of the mathematics library inGeneva.We arealso grateful to many friendsand colleagues forreading parts of the manuscript and for valuable remarks and discussions,in particular to AssyrAbdulle,Melanie Beck,Sergio Blanes,JohnButcher,MariPaz Calvo,BegonaCano,Philippe Chartier,David Cohen,PeterDeufhard,Stig Faltinsen,Francesco Fasso,Martin Gander,Marlis Hochbruck,Bulent Karasozen,WilhelmKaup,Ben Leimkuhler,PierreLeone,Frank Loose,Katina Lorenz,Robert McLachlan,AnderMurua,Alexander Ostermann,TruongLinh Pham,Sebastian Reich,Chus Sanz-Serna,Zaijiu Shang,Yifa Tang,MattWest,Will Wright.

Weare especially grateful toThanh-HaLe Thi and Dr.Martin Peters from Springer-Verlag Heidelberg forassistance,in particular for their helpin gettingmost ofthe original photographs from the Oberwolfach Archiveand from Springer New York,and for clarifyingdoubts concerningthe copyright.

# Preface to the Second Edition

Thefast development of the subject-and the fast development of the sales of the first edition of this book-has given the authors the opportunity to prepare this secondedition.First of all we have corrected several misprints and minor errors which wehave discovered orwhich have been kindly communicated tous by several readersand colleagues.Wecordially thankall ofthem for their helpand for theirinterest in ourwork.A majorpoint of confusion has been revealed by RobertMcLachlan in hisbook review in SIAMReviews.

Besides many details,which have improved the presentation throughout the book,there are the following major additions and changeswhich make the book about130 pages longer：

-amore prominent place of the Stormer-Verlet method in the exposition and the examples of the first chapter;   
-adiscussion of the Henon-Heiles model asan exampleof achaotic Hamiltonian system;   
-anew Sect.IV.9on geometric numerical linearalgebraconsideringdifferential equations on Stiefel and Grassmann manifolds and dynamical low-rank approximations;   
-anew improved composition method of order 10in Sect.V.3;   
-acharacterization ofB-series methods that conserve quadratic first integrals and acriterion for conjugate symplecticity in Sect.VI.8;   
-the section on volume preservation taken from Chap.VII to Chap.VI;   
-anextended and more coherent Chap.VII,renamed Non-Canonical Hamiltonian Systems,with more emphasis on therelationships between Hamiltonian systems onmanifolds and Poisson systems;   
-acompletelyreorganized and augmented Sect.VII.5ontherigid body dynamics andLie-Poisson systems;   
-anew Sect.VII.6on reduced Hamiltonianmodels of quantumdynamics and Poissonintegrators for their numerical treatment;   
-animproved step-size control forreversiblemethods in Sects.VII.3.2and IX.6;   
-extension of Sect.IX.5 onmodified equations of methods on manifolds to include constrained Hamiltonian systemsand Lie-Poisson integrators;   
-reorganization of Sects.IX.9and IX.1O;study of non-symplectic B-seriesmethodsthat haveamodified Hamiltonian,and counter-examples forsymmetricmethods showing linear growth in the energy error;   
-amore precise discussion of integrable reversible systems with new examples in Chap.XI;   
-extension ofChap.XIII on highly oscillatory problems to systemswith several constant frequenciesand to systemswith non-constant massmatrix;   
-anew Chap.XIV on oscillatory Hamiltonian systemswith time-or solutiondependent high frequencies,emphasizingadiabatic transformations,adiabatic invariants,and adiabatic integrators;   
-acompletely rewritten Chap.XV with more emphasis on linear multistep methodsfor second orderdifferential equations;acomplete backward error analysis includingparasitic modified differential equations;a study of the long-time stability and arigorous explanation of the long-time near-conservation ofenergyand angularmomentum.

Letus hope that this second revised edition will again meet good acceptance by our readers.

Genevaand Tubingen,October 2005

# Table of Contents

# I. Examples and Numerical Experiments..

I.1 First Problemsand Methods 1

I.1.1 TheLotka-VolterraModel I.1.2 First Numerical Methods.. 1.1.3 ThePendulum asa Hamiltonian System I.1.4 TheStormer-Verlet Scheme   
1.2 TheKepler Problem andtheOuter Solar System. 1.2.1 Angular Momentum and Kepler's Second Law I.2.2 Exact Integration of the Kepler Problem. 10 1.2.3 Numerical Integration of the Kepler Problem 12 1.2.4 The Outer Solar System   
1.3 TheHenon-HeilesModel.   
I.4 Molecular Dynamics 8   
1.5 Highly Oscillatory Problems 21 1.5.1 AFermi-Pasta-UlamProblem 21 1.5.2 Application of Classical Integrators. 23   
1.6 Exercises. 24

# [.Numerical Integrators.. 27

II.1 Runge-Kutta and Collocation Methods 27.

II.1.1 Runge-Kutta Methods..... 28   
II.1.2 Collocation Methods 30   
II.1.3 Gauss and Lobatto Collocation. 34   
II.1.4 Discontinuous Collocation Methods 35

[I.2 Partitioned Runge-Kutta Methods. 38

II.2.1 Definition and First Examples 38   
1I.2.2 Lobatto IIIA-IIIBPairs 40   
II.2.3 Nystrom Methods 41

I1.3 TheAdjoint of aMethod 42

II.4 Composition Methods.. 43

I1.5 Splitting Methods 47

II.6 Exercises. 50

# II.Order Conditions,Trees and B-Series. 51

III.1 Runge-Kutta OrderConditionsand B-Series 51   
III.1.1 Derivation of the Order Conditions 51   
III.1.2 B-Series. 56   
III.1.3 Composition of Methods. 59   
III.1.4 Composition of B-Series 61   
III.1.5 The Butcher Group 64   
III.2 OrderConditions for Partitioned Runge-Kutta Methods 66   
III.2.1 Bi-Coloured Trees and P-Series.. 66   
II.2.2 OrderConditions for Partitioned Runge-Kutta Methods 68   
IIL.2.3 OrderConditionsfor Nystrom Methods 69   
III.3 Order Conditions for Composition Methods 71   
III.3.1 Introduction 71   
III.3.2 The General Case. 73   
II.3.3 Reduction of the Order Conditions 75   
III.3.4Order Conditions for SplittingMethods 80   
III.4 TheBaker-Campbell-Hausdorff Formula 83   
III.4.1Derivative of the Exponential and Its Inverse 83   
III.4.2TheBCHFormula. 84   
III.5 Order Conditions via the BCHFormula 87   
III.5.1 Calculus ofLie Derivatives.. 87   
I1.5.2 LieBracketsand Commutativity 89   
III.5.3 Splitting Methods. 91   
II.5.4Composition Methods 92   
III.6 Exercises. 95

# IV.Conservation of First Integrals and Methods on Manifolds 97

IV.1 Examples of First Integrals 97   
IV.2 Quadratic Invariants 101   
IV.2.1 Runge-Kutta Methods. 101   
IV.2.2 Partitioned Runge-Kutta Methods 102   
IV.2.3 Nystrom Methods 104   
IV.3 Polynomial Invariants 105   
IV.3.1The Determinant asaFirst Integral 105   
IV.3.2Isospectral Flows 107   
IV.4 Projection Methods 109   
IV.5 Numerical MethodsBased on Local Coordinates 113   
IV.5.1 Manifoldsand the Tangent Space. 114   
IV.5.2Differential Equations on Manifolds 115   
IV.5.3Numerical Integrators on Manifolds 116   
IV.6 Differential Equations on Lie Groups 118   
IV.7 Methods Based on theMagnus Series Expansion 121   
IV.8 Lie Group Methods.. 123   
IV.8.1Crouch-Grossman Methods 124   
IV.8.2Munthe-KaasMethods 125   
IV.8.3Further Coordinate Mappings... 128   
IV.9 Geometric Numerical Integration Meets Geometric Numerical   
Linear Algebra. 131   
IV.9.1 Numerical Integration on the StiefelManifold 131   
IV.9.2 Differential Equations on the Grassmann Manifold....135   
IV.9.3 Dynamical Low-Rank Approximation 137   
IV.10 Exercises. 139

# V.Symmetric Integration and Reversibility 143

V.1 Reversible Differential Equationsand Maps 143   
V.2 Symmetric Runge-Kutta Methods. 146   
V.2.1 Collocation and Runge-Kutta Methods. 146   
V.2.2 Partitioned Runge-Kutta Methods 148   
V.3 Symmetric Composition Methods. 149   
V.3.1 Symmetric Composition of First Order Methods 150   
V.3.2 Symmetric Composition of Symmetric Methods 154   
V.3.3 Effective Order and Processing Methods 158   
V.4 Symmetric Methods on Manifolds. 161   
V.4.1 Symmetric Projection 161   
V.4.2 Symmetric MethodsBased on Local Coordinates.. 166   
V.5 Energy-Momentum Methods and DiscreteGradients. 171   
V.6 Exercises. 176

# VI.Symplectic Integration of Hamiltonian Systems 179

VI.1 Hamiltonian Systems 180   
VI.1.1Lagrange's Equations 180   
VI.1.2Hamilton's Canonical Equations 181   
VI.2 Symplectic Transformations 182   
VI.3 FirstExamples of Symplectic Integrators 187   
VI.4 Symplectic Runge-Kutta Methods 191   
VI.4.1Criterion of Symplecticity 191   
VI.4.2 Connection Between Symplectic and Symmetric   
Methods 194   
VI.5 Generating Functions 195   
VI.5.1 Existence of Generating Functions 195   
VI.5.2 Generating Function for Symplectic Runge-Kutta   
Methods 198   
VI.5.3 TheHamilton-Jacobi Partial Differential Equation....200   
VI.5.4Methods Based on Generating Functions 203   
VI.6 Variational Integrators. 204   
VI.6.1 Hamilton's Principle 204   
VI.6.2 Discretization of Hamilton's Principle. 206   
VI.6.3 Symplectic Partitioned Runge-Kutta Methods   
Revisited. 208   
VI.6.4Noether's Theorem 210   
VI.7 Characterization of Symplectic Methods .212   
VI.7.1 B-Series Methods Conserving Quadratic First Integrals 212   
VI.7.2 Characterization of Symplectic P-Series(and B-Series）217   
VI.7.3 IrreducibleRunge-Kutta Methods. 220   
VI.7.4 Characterization of Irreducible Symplectic Methods...222   
VI.8 Conjugate Symplecticity. 222   
VI.8.1Examples and OrderConditions. 223   
VI.8.2Near Conservation of Quadratic First Integrals 225   
VI.9 Volume Preservation 227   
VI.10 Exercises 233

# VII.Non-Canonical Hamiltonian Systems 237

# VIL.7Exercises.. 301

# VIII.Structure-Preserving Implementation. 303

VIII.1Dangers of Using Standard Step Size Control 303   
VIII.2Time Transformations 306   
VIII.2.1 Symplectic Integration 306   
VIII.2.2 Reversible Integration 309   
VIII.3 Structure-Preserving Step Size Control. 310   
VIII.3.1 Proportional,Reversible Controllers 310   
VIIL.3.2 Integrating,ReversibleControllers 314   
VIII.4Multiple Time Stepping 316   
VIII.4.1 Fast-Slow Spliting:theImpulse Method 317   
VIII.4.2Averaged Forces. 319   
VIII.5Reducing Rounding Errors 322   
VIII.6Implementation of Implicit Methods 325   
VII.6.1 Starting Approximations 326   
VIII.6.2 Fixed-Point Versus Newton Iteration 330   
VIII.7Exercises 335

# [X.Backward Error Analysisand Structure Preservation 337

IX.1 Modified Differential Equation-Examples. 337   
IX.2 Modified Equations of Symmetric Methods 342   
IX.3 Modified Equations of Symplectic Methods. 343   
IX.3.1Existence of aLocal Modified Hamiltonian 343   
IX.3.2Existence of aGlobal Modified Hamiltonian 344   
IX.3.3Poisson Integrators.. 347   
IX.4 Modified Equations of SplittingMethods 348   
IX.5 Modified Equations of Methods on Manifolds 350   
IX.5.1Methods on Manifolds and First Integrals. 350   
IX.5.2Constrained Hamiltonian Systems 352   
IX.5.3Lie-Poisson Integrators. 354   
IX.6 Modified Equations for Variable Step Sizes 356   
IX.7 Rigorous Estimates-Local Error 358   
IX.7.1 Estimation of the Derivatives of the Numerical Solution 360   
IX.7.2Estimation of the Coefficients of the Modified Equation 362   
IX.7.3Choice of $N$ and the Estimation of the Local Error....364   
IX.8 Long-Time Energy Conservation. 366   
IX.9 Modified Equationin Terms of Trees 369   
IX.9.1B-Series of theModified Equation 369   
IX.9.2 Elementary Hamiltonians 373   
IX.9.3 Modified Hamiltonian 375   
IX.9.4 First Integrals Close to the Hamiltonian 375   
IX.9.5Energy Conservation:Examples and Counter-Examples379   
IX.10 Extension to Partitioned Systems 381   
IX.10.1 P-Series of theModified Equation 381   
IX.10.2 ElementaryHamiltonians 384   
IX.11Exercises. 386

# 【 Hamiltonian Perturbation Theory and Symplectic Integrators.....389

X.1 CompletelyIntegrable HamiltonianSystems 390

X.1.1 Local Integration by Quadrature 390   
X.1.2 Completely Integrable Systems 393   
X.1.3 Action-AngleVariables 397   
X.1.4 Conditionally Periodic Flows .399   
X.1.5 TheToda Lattice-an Integrable System .402   
X.2 Transformations in the Perturbation Theory for Integrable   
Systems.. 404   
X.2.1 TheBasic Scheme of Classical Perturbation Theory...405   
X.2.2 Lindstedt-Poincare Series 406   
X.2.3 Kolmogorov's Iteration 410   
X.2.4 Birkhoff Normalization Near an Invariant Torus 412   
X.3 Linear Error Growth and Near-Preservation of First Integrals...413   
X.4 Near-Invariant Tori on ExponentiallyLong Times.. 417   
X.4.1 Estimates of Perturbation Series. 417   
X.4.2 Near-Invariant Tori of Perturbed Integrable Systems...421   
X.4.3 Near-Invariant Tori of Symplectic Integrators .422   
X.5 Kolmogorov's Theorem on Invariant Tori. 423   
X.5.1Kolmogorov's Theorem. 423   
X.5.2KAMTori under Symplectic Discretization 428   
X.6 Invariant Tori of Symplectic Maps.. 430   
X.6.1 AKAMTheorem forSymplectic Near-IdentityMaps.431   
X.6.2 Invariant Tori of Symplectic Integrators 433   
X.6.3Strongly Non-Resonant Step Sizes 433   
X.7 Exercises. .434

# XI.Reversible Perturbation Theory and Symmetric Integrators.......437

XI.1 Integrable Reversible Systems 437   
XI.2 Transformations in Reversible Perturbation Theory 442   
XI.2.1The Basic Scheme of Reversible Perturbation Theory..443.   
XI.2.2 Reversible Perturbation Series 444   
XI.2.3 ReversibleKAM Theory. 445   
XI.2.4Reversible Birkhoff-Type Normalization 447   
XI.3 Linear Error Growth and Near-Preservation of First Integrals...448   
XI.4 Invariant Tori under Reversible Discretization .451   
XI.4.1Near-Invariant Toriover ExponentiallyLong Times...451   
XI.4.2AKAM Theorem forReversibleNear-IdentityMaps.451   
XI.5 Exercises.. .453

# XI.Dissipatively Perturbed Hamiltonian and Reversible Systems......455

XII.1 Numerical Experimentswith Van der Pol's Equation 455   
XII.2 Averaging Transformations 458   
XII.2.1The Basic Scheme of Averaging 458   
XI.2.2 Perturbation Series. 459   
XII.3Attractive Invariant Manifolds. ..460   
XII.4Weakly Atractive Invariant Tori of Perturbed Integrable Systems 464   
XII.5 WeaklyAttractive Invariant Tori ofNumericalIntegrators......465   
XII.5.iModified Equations of Perturbed Differential Equations 466   
XII.5.2 Symplectic Methods 467   
XII.5.3 Symmetric Methods. 469   
XII.6Exercises. 469

# XIII.Oscillatory Differential Equations with Constant High Frequencies.471

XIII.1Towards Longer Time Steps in Solving Oscillatory Equations   
ofMotion.. .471   
XIII.1.1 TheStormer-Verlet Methodvs.Multiple Time Scales.472   
XIII.1.2 Gautschi'sand Deuflhard's Trigonometric Methods...473   
XIII.1.3 TheImpulseMethod .475   
XIII.1.4 TheMollified ImpulseMethod. 476   
XIII.1.5 Gautschi's Method Revisited 477   
XIII.1.6 Two-Force Methods. 478   
XIII.2ANonlinearModel ProblemandNumerical Phenomena.. 478   
XIII.2.1 TimeScalesintheFermi-Pasta-UlamProblem. .479   
XIII.2.2 Numerical Methods. 481   
XIII.2.3 Accuracy Comparisons 482   
XIII.2.4 Energy Exchange between StiffComponents 483   
XIII.2.5 Near-Conservation of Total and Oscillatory Energy....484   
XIII.3 Principal Terms of theModulated Fourier Expansion .486   
XIII.3.1 Decomposition of the Exact Solution 486   
XIII.3.2 Decomposition of the Numerical Solution 488   
XIII.4 Accuracy and Slow Exchange 490   
XIII.4.1 Convergence Properties on Bounded Time Intervals...490   
XIII.4.2 Intra-Oscillatory and Oscillatory-Smooth Exchanges..494   
XIII.5Modulated Fourier Expansions 496   
XII.5.1 Expansion of the Exact Solution 496   
XIII.5.2 Expansion of the Numerical Solution 498   
XIII.5.3 Expansion of the Velocity Approximation 502   
XIII.6 Almost-Invariants of the Modulated Fourier Expansions 503   
XIII.6.1 The Hamiltonian of the Modulated Fourier Expansion.503   
XIII.6.2 AFormal Invariant Close to theOscillatory Energy...505   
XIII.6.3 Almost-Invariants of the Numerical Method.. 507   
XIII.7 Long-Time Near-Conservation of Total and Oscillatory Energy.510   
XIII.8Energy Behaviourof the Stormer-Verlet Method .513   
XII1.9 Systems with Several Constant Frequencies 516   
XIII.9.1 Oscillatory Energies and Resonances .517   
XIII.9.2 Multi-Frequency Modulated Fourier Expansions... .519   
XIII.9.3 Almost-Invariants of the Modulation System .521   
XIII.9.4 Long-Time Near-Conservation of Total and   
Oscillatory Energies 524   
XIII.10 Systems with Non-Constant Mass Matrix. .526   
XIII.11 Exercises. .529

# XIV. Oscillatory Differential Equations with Varying High Frequencies..531

XIV.1Linear Systems with Time-Dependent Skew-Hermitian Matrix..531   
XIV.1.1 Adiabatic Transformationand Adiabatic Invariants....531   
XIV.1.2 Adiabatic Integrators 536   
XIV.2 Mechanical Systemswith Time-Dependent Frequencies 539   
XIV.2.1 Canonical TransformationtoAdiabatic Variables 540   
XIV.2.2 Adiabatic Integrators. 547   
XIV.2.3 Error Analysisof theImpulse Method. 550   
XIV.2.4 Error Analysis of the Mollified Impulse Method 554   
XIV.3 Mechanical Systems with Solution-Dependent Frequencies.....555   
XIV.3.1 Constraining Potentials. 555   
XIV.3.2 TransformationtoAdiabatic Variables 558   
XIV.3.3 Integrators in Adiabatic Variables 563   
XIV.3.4 Analysis ofMultiple Time-Stepping Methods 564   
XIV.4 Exercises.. 564

# KV.Dynamics of Multistep Methods 567

XV.1 Numerical Methods and Experiments 567   
XV.1.1 Linear MultistepMethods 567   
XV.1.2 MultistepMethods for Second Order Equations.. 569   
XV.1.3 Partitioned MultistepMethods 572   
XV.2 The Underlying One-Step Method. 573   
XV.2.1 Strictly Stable Multistepmethods 573   
XV.2.2 Formal Analysis for Weakly StableMethods 575   
XV.3 Backward Error Analysis. 576   
XV.3.1 Modified Equation for Smooth Numerical Solutions...576   
XV.3.2 ParasiticModified Equations .579   
XV.4 Can Multistep Methods be Symplectic？ 585   
XV.4.1Non-Symplecticity of the UnderlyingOne-Step Method585   
XV.4.2 Symplecticity in the Higher-Dimensional Phase Space.587   
XV.4.3Modified Hamiltonian of Multistep Methods 589   
XV.4.4Modified Quadratic First Integrals 591   
XV.5 Long-Term Stability 592   
XV.5.1 Role ofGrowth Parameters 592   
XV.5.2 Hamiltonian of the Full Modified System 594   
XV.5.3 Long-Time Bounds for Parasitic Solution Components 596   
XV.6 Explanation of the Long-Time Behaviour. 600   
XV.6.1 Conservation of Energy and Angular Momentum 600   
XV.6.2Linear Error Growth for Integrable Systems. 601   
XV.7 Practical Considerations 602   
XV.7.1 Numerical Instabilities and Resonances 602   
XV.7.2 Extension to Variable Step Sizes 605   
XV.8 Multi-Value orGeneralLinearMethods 609   
XV.8.1Underlying One-Step Method and Backward Error   
Analysis 609   
XV.8.2 Symplecticity and Symmetry 611   
XV.8.3 Growth Parameters 614   
XV.9 Exercises. 615

Bibliography 617

Index.. 637

# Chapter I. Examples and Numerical Experiments

Thischapter introduces some interesting examples of differential equations and illustrates different types of qualitative behaviour of numerical methods.Wedeliberatelyconsider only very simple numerical methods of orders1and 2toemphasize thequalitative aspects of the experiments.The same effects(on adifferent scale) occurwith more sophisticated higher-order integration schemes.The experiments presented here should serveasamotivation for the theoretical and practical investigations of later chapters.Thereader is encouraged to repeat the experiments or to invent similar ones.

# I.1 First Problems and Methods

Numerical applications of the case of two dependent variables are not easily obtained. (A.J.Lotka 1925,p.79)

Ourfirst problems,theLotka-Volterra model and thependulum equation,are differential equations in two dimensions and showalready many interesting geometric properties.Our first methodsare various variants of the Euler method,themidpoint rule,and the Stormer-Verletscheme.

# I.1.1 TheLotka-Volterra Model

Westart with anequation from mathematical biologywhich models the growth of animal species.Ifareal variable $u ( t )$ istorepresent the number of individuals ofa certain species at time $t$ ,the simplest assumption about its evolution is $d u / d t = u \cdot \alpha .$ , where $\alpha$ isthereproduction rate.Aconstant $\alpha$ leads to exponential growth.Inthe case of more species living together,the reproduction rates will also depend on thepopulation numbers of the other species.For example,for two specieswith $u ( t )$ denoting the number of predators and $v ( t )$ thenumber of prey,aplausible assumptionismadebytheLotka-Volterramodel

$$
\begin{array} { r } { \dot { u } = u ( v - 2 ) } \\ { \dot { v } = v ( 1 - u ) , } \end{array}
$$

where the dots on $u$ and $\upsilon$ stand for differentiationwith respect to time.(We have chosen the constants2and $^ { 1 }$ in（1.1）arbitrarily.)A.J.Lotka（1925,Chap.VIII)used

![](images/f979493c656c6fb111c9b2491b3051c3e1258a6222ce62640458d483a0d27456.jpg)  
Fig.1.1.Vector field,exact flow,and numerical flow for theLotka-Volterra model(1.1)

thismodel tostudy parasiticinvasion of insect species,and,withits help,V.Volterra （1927)explained curious fishingdata from theupper Adriatic Sea followingWorld WarI.

Equations（1.1）constitute an autonomous system of differential equations.In general,we write such a system inthe form

$$
\dot { y } = f ( y ) ~ .
$$

Every $y$ representsa point in the phase space,inequation(1.1） above $y = ( u , v )$ is in the phase plane $\mathbb { R } ^ { 2 }$ .Thevector-valued function $f ( y )$ represents avectorfield which,at any point of the phase space,prescribes the velocity(directionand speed) of the solution $y ( t )$ that passes through that point (see the first picture of Fig.1.1).

FortheLotka-Volterra model,we observe that the systemcycles through three stages:（1） the prey population increases;(2) the predator population increases by feeding on theprey;(3) the predator population diminishes due to lack of food.

Flowofthe System.A fundamental concept isthe flow over time $t$ Thisisthe mappingwhich,toanypoint $y _ { 0 }$ inthe phase space,associates the value $y ( t )$ ofthe solution with initial value $y ( 0 ) = y _ { 0 } .$ Thismap,denoted by $\varphi _ { t }$ ,isthusdefined by

$$
\varphi _ { t } ( y _ { 0 } ) = y ( t ) \quad { \mathrm { ~ i f ~ } } \quad y ( 0 ) = y _ { 0 } .
$$

The second picture of Fig.1.1 shows the results of three iterations of $\varphi _ { t }$ （with $t =$ 1.3)for theLotka-Volterraproblem,forasetof initial values $y _ { 0 } = ( u _ { 0 } , v _ { 0 } )$ forming ananimal-shaped set $A$ .1

Invariants.Ifwe divide the two equations of(1.1) by each other,we obtainasingle equation between the variables $u$ and $\boldsymbol { v }$ Afterseparation ofvariableswe get

$$
0 = { \frac { 1 - u } { u } } { \dot { u } } - { \frac { v - 2 } { v } } { \dot { v } } = { \frac { d } { d t } } I ( u , v )
$$

where

$$
I ( u , v ) = \ln u - u + 2 \ln v - v ,
$$

so that $I ( u ( t ) , v ( t ) ) = C o n s t$ forall $t$ We call the function $I$ an invariant of the system(1.1).Everysolutionof(1.1）thuslies ona level curve of(1.4).Someof these curvesare drawn in thepictures of Fig.1.1.Since the level curves are closed, all solutions of(1.1) are periodic.

# I.1.2First Numerical Methods

Explicit Euler Method.The simplest of all numerical methods for the system(1.2) is the method formulated by Euler(1768),

$$
y _ { n + 1 } = y _ { n } + h f ( y _ { n } ) .
$$

It uses aconstant step size $h$ to compute,one after the other,approximations $y _ { 1 }$ , $y _ { 2 }$ , $y _ { 3 } , . . .$ to the values $y ( h )$ ， $y ( 2 h )$ , $y ( 3 h )$ ， $\cdot \cdot \cdot$ of the solution starting from a given initialvalue $y ( 0 ) = y _ { 0 }$ Themethod iscalled theexplicit Eulermethod,because the approximation $y _ { n + 1 }$ is computed using an explicit evaluation of $f$ at thealready known value $y _ { n }$ Suchaformula representsamapping

$$
\varPhi _ { h } : y _ { n } \mapsto y _ { n - 1 } ,
$$

which wecallthe discrete or numerical flow.Some iterations of the discrete flow for theLotka-Volterra problem（1.1）（with $h = 0 . 5$ )arerepresented in the third picture ofFig.1.1.

Implicit EulerMethod.Theimplicit Eulermethod

$$
y _ { n + 1 } = y _ { n } + h f ( y _ { n + 1 } ) ,
$$

isknown for itsall-dampingstability properties.In contrast to (1.5),the approximation $y _ { n + 1 }$ isdefined implicitlyby(1.6),and the implementationrequires the numerical solution of a nonlinear system of equations.

Implicit Midpoint Rule. Taking the mean of $y _ { n }$ and $y _ { n + 1 }$ in theargument of $f$ ,we get the implicit midpointrule

$$
y _ { n + 1 } = y _ { n } + h f { \biggl ( } { \frac { y _ { n } + y _ { n + 1 } } { 2 } } { \biggr ) } .
$$

Itisasymmetricmethod,which means thatthe formula is left unaltered after exchanging $y _ { n }  y _ { n + 1 }$ and $h  - h$ (more on symmetric methods in Chap.V).

Symplectic EulerMethods.For partitioned systems

$$
\begin{array} { r } { \dot { u } = a ( u , v ) } \\ { \dot { v } = b ( u , v ) , } \end{array}
$$

![](images/a14bfb7be88540d822b1f4aad06152eac37123520dd1e6b6e8540231c2e04e8a.jpg)  
Fig.1.2.Solutions of the Lotka-Volterra equations(1.1） (step sizes $h = 0 . 1 2$ initialvalues $( 2 , 2 )$ for the explicit Euler method, $( 4 , 8 )$ forthe implicit Euler method, $( 4 , 2 )$ and $( 6 , 2 )$ for the symplectic Euler method)

suchas the problem(1.1),we consider also partitioned Euler methods

$$
\begin{array} { r l } & { u _ { n + 1 } = u _ { n } + h a ( u _ { n } , v _ { n + 1 } ) \quad \mathrm { ~ o r ~ } \quad u _ { n + 1 } = u _ { n } + h a ( u _ { n + 1 } , v _ { n } ) } \\ & { v _ { n + 1 } = v _ { n } + h b ( u _ { n } , v _ { n + 1 } ) , \quad \mathrm { ~ o r ~ } \quad v _ { n + 1 } = v _ { n } + h b ( u _ { n + 1 } , v _ { n } ) , } \end{array}
$$

whichtreat one variablebythe implicitand the other variableby the explicitEuler method.In viewofan important propertyof thismethod,discovered byde Vogelaere (1956)and to be discussed in Chap.VI,we call them symplectic Euler methods.

Numerical Example for theLotka-Volterra Problem.Our first numerical experimentshows thebehaviour of thevariousnumerical methods applied to theLotka-Volterra problem.Inparticular,weare interested inthe preservationof theinvariant $I$ over long times.Fig.1.2 plotsthe numerical approximations of the first 125 steps with the above numerical methods applied to（1.I）,all with constant step sizes.We observe that the explicit and implicit Euler methods show wrong qualitative behaviour.The numerical solution either spirals outwards or inwards.The symplectic. Eulermethod (implicit in $u$ and explicit in $v$ however,givesa numerical solution that lies apparently onaclosed curveas does the exact solution.Note that thecurves of the numerical and exact solutions do not coincide.

# I.1.3The Pendulum asa Hamiltonian System

Agreat deal of attention in this book will be addressed to Hamiltonian problems, and our next exampleswill be of this type.These problemsare of the form

$$
\dot { p } = - H _ { q } ( p , q ) , \qquad \dot { q } = H _ { p } ( p , q ) ,
$$

where the Hamiltonian $H ( p _ { 1 } , \dots , p _ { d } , q _ { 1 } , \dots q _ { d } )$ represents the total energy; $q _ { i }$ are the position coordinates and $p _ { i }$ themomenta for $i = 1 , \ldots , d$ ,with $d$ thenumberof

degrees of freedom; $H _ { p }$ and $H _ { q }$ are the vectors of partial derivatives.One verifies easily by differentiation (see Sect.IV.1) that,along the solution curves of(1.10),

$$
H ( p ( t ) , q ( t ) ) = ( \gamma _ { O n S t } ,
$$

i.e.,theHamiltonianisan invariant ora first integral.Moredetailsabout Hamiltonian systems and their derivation from Lagrangian mechanicswill be given in Sect.VI.1.

Pendulum. The mathematical pendulum (mass $m = 1$ , massless rod of length $\ell \ = \ 1$ ，gravitational acceleration $g = 1$ ）isasystem with one degree of freedom having the Hamiltonian

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { 2 } - \cos q ,
$$

![](images/a00bf95b299246332366b864f1d1e5e930fe3444b8e51c8fa76cc37d48b89413.jpg)

so that the equations of motion(1.10) become

$$
\dot { p } = - \sin q , \qquad \dot { q } = p .
$$

Since thevector feld(1.13)is $2 \pi$ -periodicin $q$ itis natural to consider $q$ asavariable on the circle $S ^ { 1 } .$ Hence,the phase space of points $( p , q )$ becomes thecylinder $\mathbb { R } \times S ^ { 1 } .$ Fig.1.3 shows some level curves of $H ( p , q ) .$ By(1.11),the solution curves of the problem(1.13) lie on such level curves.

![](images/3c3bcfff00cd9d373ec258de63fc2a7f1ba532a62238ba6439f306fe68f8776e.jpg)  
Fig.1.3.Exact and numerical flow for the pendulum problem(1.13);step sizes $h = t = 1$

AreaPreservation.Figure 1.3（first picture）illustrates that the exact flow ofa Hamiltonian system(1.1O)is area preserving.This can be explained as follows:the derivative of the flow $\varphi _ { t }$ withrespect to initial values $( p , q )$ ,

$$
\varphi _ { t } ^ { \prime } ( p , q ) = \frac { \partial \big ( p ( t ) , q ( t ) \big ) } { \partial ( p , q ) } ,
$$

satisfies the variational equation ²

$$
\phi _ { t } ^ { \prime } ( p , q ) = \left( \begin{array} { c c } { { - H _ { p q } } } & { { - H _ { q q } } } \\ { { H _ { p p } } } & { { H _ { q p } } } \end{array} \right) \varphi _ { t } ^ { \prime } ( p , q ) ,
$$

where the second partial derivatives of $H$ areevaluatedat $\varphi _ { t } ( p , q )$ Inthe case of onedegree of freedom（ $d = 1$ ),asimple computation shows that

$$
\frac { d } { d t } \operatorname* { d e t } \varphi _ { t } ^ { \prime } ( p , q ) = \frac { d } { d t } \Big ( \frac { \partial p ( t ) } { \partial p } \frac { \partial q ( t ) } { \partial q } - \frac { \partial p ( t ) } { \partial q } \frac { \partial q ( t ) } { \partial p } \Big ) = . . . . = 0 .
$$

Since $\varphi _ { 0 }$ is the identity,this implies $\operatorname* { d e t } \varphi _ { t } ^ { \prime } ( p , q ) = 1$ forall $t$ ,which means that the flow $\varphi _ { t } ( p , q )$ isan area-preservingmapping.

Thelast two pictures of Fig.1.3 show numerical flows.The explicit Euler method is clearly seen nottopreservearea but the symplectic Eulermethod is(this will be proved in Sect.VI.3).One of the aims of'geometric integration'is the study of numerical integrators that preserve such types of qualitative behaviour of the exact flow.

![](images/6ba452de74af458f19ed71163d1d7d4c784ea315e166c9aa76fd886e8b9d5ba1.jpg)  
Fig.1.4.Solutions of thependulum problem（1.13)；explicit Euler with step size $h = 0 . 2$ ， initialvalue $( p _ { 0 } , q _ { 0 } ) = ( 0 , 0 . 5 )$ symplectic Eulerwith $h = 0 . 3$ and initialvalues $q _ { 0 } = 0$ , $p _ { 0 } = 0 . 7 , 1 . 4 , 2 . 1$ ;Stormer-Verletwith $h = 0 . 6$

Numerical Experiment.We applythe above numerical methods to the pendulum equations(see Fig.1.4）.Similar to the computations for theLotka-Volterra equations,we observe that the numerical solutions of the explicit Euler and of the implicitEulermethod (not drawn in Fig.1.4） spiral either outwards or inwards.The symplectic Euler method shows the correct qualitative behaviour,but destroys the left-right symmetry of theproblem.The Stormer-Verlet scheme,whichwediscuss next,works perfectly even with doubled step size.

![](images/7d3786d6f5ce024154491d9d2c95408d9bc4dba3e742f1155c6edb97a80f268e.jpg)  
Fig.1.5.Carl Stormer(left picture),born:3September 1874in Skien(Norway),died:13August 1957. Loup Verlet(right picture),born:24May1931in Paris

# I.1.4The Stormer-Verlet Scheme

Theabove equations(1.13) for the pendulumare of the form

$$
{ \begin{array} { r l r l r l } & { { \dot { p } } = f ( q ) } & & { \quad { \mathrm { ~ o r ~ } } \quad { \ddot { q } } = f ( q ) } \\ & { { \dot { q } } = p } \end{array} }
$$

which is the important special case of a second order differential equation.The most natural discretization of（1.14）is

$$
q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } = h ^ { 2 } f ( q _ { n } ) ,
$$

whichis just obtained byreplacing the second derivativein(1.14)by the central second-orderdifference quotient.This basic method,or its equivalent formulation givenbelow,iscalledtheStormermethodinastronomy,theVerletmethod³inmoleculardynamics,the leap-frogmethodinthecontext of partial differential equations, andit has further names inotherareas (see Hairer,Lubich&Wanner(2Oo3),p.402). C.Stormer (19o7)used higher-order variants for numerical computations concerningtheaurora borealis.L.Verlet（1967）proposed thismethod for computations in moleculardynamics,where it has becomeby farthemostwidelyused integration scheme.

Geometrically,the Stormer-Verlet methodcan beseenasproduced by parabolas,which in the points $t _ { n }$ possess the right second derivative $f ( q _ { n } )$ (seeFig.1.6 to the left).But we can also think of polygons,which possess the right slope in the midpoints(Fig.1.6to the right).

![](images/163ba1c0a33202cd06df1bfdeae6a3f8063f068050293fb244671c84c9544c75.jpg)  
Fig.1.6.Illustration for the Stormer-Verlet method

Approximations to thederivative $p = \dot { q }$ are simply obtained by

$$
p _ { n } = { \frac { q _ { n + 1 } - q _ { n - 1 } } { 2 h } } \quad \quad { \mathrm { a n d } } \quad \quad p _ { n + 1 / 2 } = { \frac { q _ { n + 1 } - q _ { n } } { h } } ,
$$

One-Step Formulation.The Stormer-Verlet method admitsaone-step formulation which is useful for actual computations.The value $q _ { n }$ together with the slope $p _ { n }$ and the second derivative $f ( q _ { n } )$ ,allat $t _ { n }$ ,uniquelydetermine theparabolaand hence also the approximation $\left( p _ { n + 1 } , q _ { n + 1 } \right)$ at $t _ { n + 1 } .$ Writing(1.15)as $p _ { n + 1 / 2 } - p _ { n - 1 / 2 } =$ $h f ( q _ { n } )$ and using $p _ { n + 1 / 2 } + p _ { n - 1 / 2 } = 2 p _ { n } ,$ wegetby elimination of either $p _ { n + 1 / 2 }$ orpn-1/2 the formulae

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n + 1 / 2 } ~ = ~ p _ { n } + \displaystyle \frac { h } { 2 } ~ f ( q _ { n } ) } } \\ { { } } & { { } } & { { q _ { n + 1 } ~ = ~ q _ { n } + h p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } ~ = ~ p _ { n + 1 / 2 } + \displaystyle \frac { h } { 2 } ~ f ( q _ { n + 1 } ) } } \end{array}
$$

which is an explicit one-step method $\phi _ { h } : ( q _ { n } , p _ { n } ) \longmapsto ( q _ { n + 1 } , p _ { n + 1 } )$ for the corresponding first order system of(1.14). If one isnot interested in the values $p _ { n }$ ofthe derivative,the firstand third equationsin (1.17) can be replaced by

$$
\begin{array} { r } { p _ { n + 1 / 2 } = p _ { n - 1 / 2 } + h f ( q _ { n } ) . } \end{array}
$$

# I.2 TheKepler Problemand the Outer Solar System

Iawoke as if from sleep,anew light broke on me. (J.Kepler;quoted fromJ.L.E.Dreyer,Ahistoryofastronomy,1906,Dover1953,p.391)

Oneof the great achievementsin the history of science was the discovery of the lawsof J.Kepler(16o9),based on manyprecisemeasurements of the positions-of Marsby Tycho Braheand himself.Theplanetsmoveinelliptic orbitswith the sun at one of the foci(Kepler's first law)

$$
r = { \frac { d } { 1 + e \cos \varphi } } = a - a e \cos E ,
$$

(where $a \quad =$ greataxis, $e \quad =$ eccentricity, $\begin{array} { r l } { b } & { { } = } \end{array}$ $a { \sqrt { 1 - e ^ { 2 } } }$ ， $d = b { \sqrt { 1 - e ^ { 2 } } } = a ( 1 - e ^ { 2 } )$ , $E = \operatorname { e c } .$ centricanomaly, $\varphi =$ trueanomaly).

Newton (Principia 1687)then explained this motion by his general law of gravitational attraction （proportional to $1 / r ^ { 2 }$ )andtherelation between forcesand acceleration(the“Lex II'of the Principia).This then opened the way for treating arbitrarycelestial motions by solvingdifferential equations.

![](images/b26a557064e211c584098e905881f733983cbd1550f270fc3924de2a84da83a0.jpg)

Two-Body Problem.For computing the motion of two bodies which attract each other,we choose one of the bodies as the centre of our coordinate system;the motion will then stay ina plane (Exercise 3)and we can use two-dimensional coordinates $q \ = \ ( q _ { 1 } , q _ { 2 } )$ forthe position of the second body.Newton's laws,with asuitable normalization,then yield the followingdifferential equations

$$
\ddot { q } _ { 1 } = - \frac { q _ { 1 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } ; \qquad \ddot { q } _ { 2 } = - \frac { q _ { 2 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } .
$$

This is equivalent toa Hamiltonian system with the Hamiltonian

$$
H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = \frac { 1 } { 2 } \left( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } \right) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } , \qquad p _ { i } = \ddot { q } _ { i } .
$$

# 1.2.1 Angular Momentumand Kepler's Second Law

The system hasnot only the total energy $H ( p , q )$ asafirstintegralbutalsothe angularmomentum

$$
L ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = q _ { 1 } p _ { 2 } - q _ { 2 } p _ { 1 } .
$$

Thiscan bechecked by differentiationand isnothing other than Kepler's second law,which says that the ray $F M$ sweeps equal areas in equal times (see the litle picture at the beginning of Sect.I.2).

Abeautiful geometric justification of this law is due to I.Newton4(Principia （1687),BookI,figure forTheoremI).Theidea istoapplythe Stormer-Verlet scheme(1.15） to the equations(2.2）(see Fig.2.1).Byhypothesis,the diagonal of the parallelogram $q _ { n - 1 } q _ { n } q _ { n + 1 }$ ,whichis $\left( q _ { n + 1 } - q _ { n } \right) - \left( q _ { n } - q _ { n - 1 } \right) \ =$ $q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } = C o n s t \cdot f ( q _ { n } )$ ,points towards the sun $S$ Therefore,the altitudes of the triangles $q _ { n - 1 } q _ { n } S$ and $q _ { n + 1 } q _ { n } S$ are equal.Since they have the common base $q _ { n } S$ ,they also haveequal areas.Hence

$$
\operatorname* { d e t } ( q _ { n - 1 } , q _ { n } - q _ { n - 1 } ) = \operatorname* { d e t } ( q _ { n } , q _ { n + 1 } - q _ { n } )
$$

and by passing to the limit $h  0$ we see that $\operatorname* { d e t } ( q , p ) = C o n s t .$ This is (2.4).

![](images/b971014a5d1d803acefe0d11b3f9997ed4870ddbaaa8be94d867bd66eb0d4ad3.jpg)  
Fig.2.1.ProofofKepler'sSecondLaw(left);facsimilefromNewton’sPrincipia (right)

Wehave not only an elegant proof for this invariant,but wealso see that the Stormer-Verlet schemepreserves thisinvariant forevery $h > 0$ .

# 1.2.2Exact Integration of the Kepler Problem

Pour voir présentement que cette courbe $A B C$ ...est toujours une SectionConique,ainsique Mr.Newton I'a suppose,pag.55.Coroll.I.sans le demontrer;ily faut bienplusd'adresse: （Joh.Bernoulli1710,p.475）

Itis now interesting,inversely to the procedureof Newton,toprove that any solution of(2.2)follows either an elliptic,parabolic or hyperbolic arc and to describe the solutionsanalytically.Thiswas first done by Joh.Bernoulli(171o,full of sarcasm against Newton),and byNewton(1713,second edition of the Principia,without mentioningaword about Bernoulli).

By(2.3)and(2.4),every solution of(2.2) satisfies the two relations

$$
\frac { 1 } { 2 } \left( \dot { q } _ { 1 } ^ { 2 } + \dot { q } _ { 2 } ^ { 2 } \right) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } = H _ { 0 \ast } ~ q _ { 1 } \dot { q } _ { 2 } - q _ { 2 } \dot { q } _ { 1 } = L _ { 0 } ,
$$

where the constants $H _ { 0 }$ and $L _ { 0 }$ aredetermined by the initial values.Usingpolar coordinates $q _ { 1 } = r \cos \varphi$ , $q _ { 2 } = r \sin \varphi$ ,thissystem becomes

$$
{ \frac { 1 } { 2 } } \left( { \dot { r } } ^ { 2 } + r ^ { 2 } { \dot { \varphi } } ^ { 2 } \right) - { \frac { 1 } { r } } = H _ { 0 } , \qquad r ^ { 2 } \dot { \varphi } = L _ { 0 } .
$$

Forits solution weconsider $r$ as a function of $\varphi$ and write $\begin{array} { r } { \dot { r } = \frac { d r } { d \varphi } \cdot \dot { \varphi } . } \end{array}$ The elimination of $\dot { \varphi }$ in(2.6）then yields

$$
{ \frac { 1 } { 2 } } \left( \left( { \frac { d r } { d \varphi } } \right) ^ { 2 } + r ^ { 2 } \right) { \frac { L _ { 0 } ^ { 2 } } { r ^ { 4 } } } - { \frac { 1 } { r } } = H _ { 0 } .
$$

In this equation we use the substitution $r = 1 / u$ ， $d r = - d u / u ^ { 2 }$ which gives (with $\prime = d / d \varphi$ ）

$$
\frac { 1 } { 2 } ( u ^ { \prime 2 } + u ^ { 2 } ) - \frac { u } { L _ { 0 } ^ { 2 } } - \frac { H _ { 0 } } { L _ { 0 } ^ { 2 } } = 0 .
$$

This isa“Hamiltonian”for the system

$$
u ^ { \prime \prime } + u = { \frac { 1 } { d } } \quad \mathrm { i . e . , } \quad u = { \frac { 1 } { d } } + c _ { 1 } \cos \varphi + c _ { 2 } \sin \varphi = { \frac { 1 + e \cos ( \varphi - \varphi ^ { * } ) } { d } }
$$

where $d = L _ { 0 } ^ { 2 }$ and the constant $e$ becomes,from (2.7),

$$
e ^ { 2 } = 1 + 2 H _ { 0 } L _ { 0 } ^ { 2 }
$$

(byExercise7,the expression $1 + 2 H _ { 0 } L _ { 0 } ^ { 2 }$ is non-negative).This is precisely formula (2.1).The angle $\varphi ^ { * }$ isdetermined by the initial values $r _ { 0 }$ and $\varphi _ { 0 }$ .Equation (2.1) represents an elliptic orbit with eccentricity $e$ for $H _ { 0 } < 0$ (seeFig.2.2,dotted line), aparabola for $H _ { 0 } = 0$ ,andahyperbolafor $H _ { 0 } > 0$ .

Finally,we must determine the variables $\boldsymbol { r }$ and $\varphi$ as functions of $t$ With the relation (2.8)and $r = 1 / u$ ,the second equation of(2.6) gives

$$
\frac { d ^ { 2 } } { \left( 1 + e \cos ( \varphi - \varphi ^ { \ast } ) \right) ^ { 2 } } d \varphi = L _ { 0 } d t
$$

which,afteranelementary,butnoteasy,integration,representsanimplicitequation for $\varphi ( t )$

![](images/ce60f4ec881a29b5dbeb510e7aaa4b303d9c35f40519c1b76d0c89202511d4cf.jpg)  
Fig.2.2.Numerical solutions of the Kepler problem (eccentricity $e ~ = ~ 0 . 6$ indots:exact solution)

# 1.2.3Numerical Integration of the Kepler Problem

Forthe problem(2.2）we choose,with $0 \leq e < 1$ ,theinitial values

$$
q _ { 1 } ( 0 ) = 1 - e , \quad q _ { 2 } ( 0 ) = 0 , \quad \dot { q } _ { 1 } ( 0 ) = 0 , \quad \dot { q } _ { 2 } ( 0 ) = \sqrt { \frac { 1 + e } { 1 - e } } .
$$

This implies that $H _ { 0 } = - 1 / 2$ , $L _ { 0 } = \sqrt { 1 - e ^ { 2 } }$ , $d = 1 - e ^ { 2 }$ and $\varphi ^ { * } = 0$ Theperiod of the solution is $2 \pi$ (Exercise5).Fig.2.2 shows some numerical solutions for the eccentricity $e = 0 . 6$ compared to the exact solution.After our previous experience, it isno longera surprise that the explicit Euler method spirals outwards and gives a completelywronganswer.Forthe other methods we takeastep size1OO times larger in order to“see something".We see that the nonsymmetric symplectic Euler method distorts the ellipse,and that all methods exhibita precession effect,clockwise for Stormer-Verlet and symplectic Euler,anti-clockwise for the implicit midpoint rule. Thesame behaviour occurs for the exact solution of perturbed Keplerproblems (Exercise 12)and has occupied astronomers for centuries.

Ournext experiment(Fig.2.3） studies the conservation of invariantsand the global error.Themain observationis that the errorinthe energy grows linearly for the explicit Euler method,and itremains boundedand small(no secular terms) for thesymplectic Euler method.The global error,measured in the Euclideannorm, showsaquadratic growth for the explicit Euler compared toa linear growth for thesymplectic Euler.As indicated in Table2.1 theimplicit midpointruleand the Stormer-Verletscheme behave similarto the symplectic Euler,but havea smaller error dueto their higher order.We remark that the angularmomentum $L ( p , q )$ isexactlyconserved by thesymplectic Euler,theStormer-Verlet,and theimplicit midpoint rule.

![](images/ca33a2bf16b816d57ab4dbaa71566faea7e78bb694fdba1479a48875591a8ce7.jpg)  
Fig.2.3.Energy conservation and global error for the Kepler problem

Table2.1.Qualitative long-time behaviour for theKepler problem; $t$ is time, $h$ the step size   

<table><tr><td>method</td><td>errorin H</td><td>error inL</td><td>global error</td></tr><tr><td>explicit Euler</td><td>O（th）</td><td>(th）</td><td>O(t²h)</td></tr><tr><td>symplectic Euler</td><td>O(h）</td><td>0</td><td>（th）</td></tr><tr><td>implicitmidpoint</td><td>O(h²）</td><td>0</td><td>O(th²)</td></tr><tr><td>Stormer-Verlet</td><td>O（h²）</td><td>0</td><td>O(th²)</td></tr></table>

# I.2.4 The Outer Solar System

Theevolution of the entire planetary system has been numericallyintegrated foratime spanofnearly 1oomillionyears.Thiscalculation confirms that the evolution of the solar system as a wholeis chaotic,...

(G.J.Sussman&J.Wisdom1992)

Wenext apply our methods to the system which describes the motion of the five outerplanetsrelative to the sun.This system has been studied extensively byastronomers.The problem isa Hamiltonian system (1.10)（ $N$ -bodyproblem)with

$$
H ( p , q ) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { 5 } \frac { 1 } { m _ { i } } p _ { i } ^ { T } p _ { i } - G \sum _ { i = 1 } ^ { 5 } \sum _ { j = 0 } ^ { i - 1 } \frac { m _ { i } m _ { j } } { \| q _ { i } - q _ { j } \| } .
$$

Here $p$ and $q$ are the supervectors composed by the vectors $p _ { i } , q _ { i } \in \mathbb { R } ^ { 3 }$ (momenta and positions),respectively.Thechosen units are:masses relativeto the sun,so that thesun hasmass1.We have taken

$$
m _ { 0 } = 1 . 0 0 0 0 0 5 9 7 6 8 2
$$

to takeaccount of the inner planets.Distances are in astronomical units $( 1 \left[ \mathrm { A . U . } \right] = $ 14959787O[km]),timesin earth days,and the gravitational constant is

$$
G = 2 . 9 5 9 1 2 2 0 8 2 8 6 \cdot 1 0 ^ { - 4 } .
$$

The initial values for the sun are taken as $q _ { 0 } ( 0 ) = ( 0 , 0 , 0 ) ^ { 1 }$ and $\dot { \boldsymbol { q } } _ { 0 } ( 0 ) = ( 0 , 0 , 0 ) ^ { T } .$ All other data (masses of the planetsand the initial positionsand initial velocities)aregivenin Table2.2.The initial datais taken from“AhnertsKalender fur Sternfreunde 1994",Johann AmbrosiusBarth Verlag1993,and they correspond to September5,1994at0h00.6

Table2.2.Data for the outersolar system   

<table><tr><td rowspan=1 colspan=1>planet</td><td rowspan=1 colspan=1>mass</td><td rowspan=1 colspan=1>initial position</td><td rowspan=1 colspan=1>initial velocity</td></tr><tr><td rowspan=1 colspan=1>Jupiter</td><td rowspan=1 colspan=1>m1=0.000954786104043</td><td rowspan=1 colspan=1>-3.5023653-3.8169847-1.5507963</td><td rowspan=1 colspan=1>0.00565429-0.00412490-0.00190589</td></tr><tr><td rowspan=1 colspan=1>Saturn</td><td rowspan=1 colspan=1>m2=0.000285583733151</td><td rowspan=1 colspan=1>9.0755314-3.0458353-1.6483708</td><td rowspan=1 colspan=1>0.001683180.004835250.00192462</td></tr><tr><td rowspan=1 colspan=1>Uranus</td><td rowspan=1 colspan=1>m3=0.0000437273164546</td><td rowspan=1 colspan=1>8.3101420-16.2901086-7.2521278</td><td rowspan=1 colspan=1>0.003541780.001371020.00055029</td></tr><tr><td rowspan=1 colspan=1>Neptune</td><td rowspan=1 colspan=1>m4=0.0000517759138449</td><td rowspan=1 colspan=1>11.4707666-25.7294829-10.8169456</td><td rowspan=1 colspan=1>0.002889300.001145270.00039677</td></tr><tr><td rowspan=1 colspan=1>Pluto</td><td rowspan=1 colspan=1>m5=1/(1.3.108）</td><td rowspan=1 colspan=1>-15.5387357-25.2225594-3.1902382</td><td rowspan=1 colspan=1>0.00276725-0.00170702-0.00136504</td></tr></table>

![](images/808b3dfbd3a8560f988602d39677b2698c4d2b51240ae013679c144be7e87fa6.jpg)  
Fig.2.4.Solutions of the outer solar system

To this system we apply the explicit and implicit Euler methods with step size $h = 1 0$ thesymplectic Euler and the Stormer-Verlet method with much larger step sizes $h = 1 0 0$ and $h = 2 0 0$ ,repectively,all overa timeperiodof 200000 days.The numerical solution (see Fig.2.4）behaves similarly to that forthe Kepler problem.With the explicit Euler method theplanets have increasing energy,they spiral outwards, Jupiter approaches Saturn which leaves theplane of the two-body motion.With the implicit Euler method the planets (first Jupiter and then Saturn)

fall into the sunand are thrown far away.Both the symplectic Euler method and the Stormer-Verlet scheme show the correct behaviour.Anintegration overa much longer time of say several million years does not deteriorate this behaviour.Letus remark thatSussman&Wisdom(1992) have integratedtheouter solar systemwith special geometric integrators.

# I.3The Henon-HeilesModel

..because:(1）itis analytically simple;this makes the computation of thetrajectorieseasy;(2)at the same time,itis sufficiently complicated to give trajectorieswhich are far from trivial. (Henon&Heiles1964）

TheHenon-Heiles model was created for describing stellar motion,followed for a verylong time,inside the gravitational potential $U _ { 0 } ( r , z )$ ofagalaxywithcylindrical symmetry(Henon&Heiles 1964).Exterisivenumerical experimentations should helpto answer the question,if thereexists,besides theknown invariants $H$ and $L$ , athird invariant.Despite endless tentatives of analytical calculations during many decades,sucha formula had not been found.

Afterareduction of the dimension,a Hamiltonian in twodegrees of freedom of theform

$$
H ( p , q ) = { \frac { 1 } { 2 } } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) + U ( q )
$$

isobtained and the questionis,if such an equation hasa second invariant.Here, Henon and Heiles put aside the astronomical origin of the problem and choose

$$
U ( q ) = \frac { 1 } { 2 } ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) + q _ { 1 } ^ { 2 } q _ { 2 } - \frac { 1 } { 3 } q _ { 2 } ^ { 3 }
$$

(see citation).The potential $U$ isrepresented inFig.3.1.When $U$ approaches $\textstyle { \frac { 1 } { 6 } }$ ,the level curves of $U$ tend toan equilateral triangle,whose vertices are saddle points of $U .$ The corresponding system

![](images/eb0e63819e8a0c402825778deef29348eae82c1479c19bd5dd8223bf0a59c728.jpg)  
Fig.3.1.Potentialof theHenon-HeilesModelandasolution

![](images/3543500487d3610984a5128a428bd5c4b33a85c6f77af27fafb989aac380a055.jpg)  
Fig.3.2.Poincare cuts for $q _ { 1 } = 0 , p _ { 1 } > 0$ of the Henon-HeilesModel for $\begin{array} { r } { H = \frac { 1 } { 1 2 } } \end{array}$ (6 orbits,left)and $\begin{array} { r } { H = \frac { 1 } { 8 } } \end{array}$ (1orbit,right）

![](images/8774bd47cd62afd1030e0900d91a363b045095246206dbe12323ec307215708a.jpg)  
Fig.3.3.Poincaré cuts for numerical methods,one orbit each;explicit Euler (left),implicit Euler(right).Same initial data as in Fig.3.2

$$
\ddot { q } _ { 1 } = - q _ { 1 } - 2 q _ { 1 } q _ { 2 } , \qquad \ddot { q } _ { 2 } = - q _ { 2 } - q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 }
$$

has solutions with nontrivial properties.For given initial values with $H ( p _ { 0 } , q _ { 0 } ) < \frac { 1 } { 6 }$ and $q _ { 0 }$ inside the triangle $U \leq \frac { 1 } { 6 }$ ,the solution stays there and moves somehowlike amass point gliding on this surface (see Fig.3.1,right).

PoincaréCuts.Wefix first theenergy $H _ { 0 }$ and put $q _ { 1 0 } = 0$ Then for any point $P _ { 0 } = ( q _ { 2 0 } , p _ { 2 0 } )$ ,we obtain $p _ { 1 0 }$ from (3.1)as $p _ { 1 0 } = \sqrt { 2 H _ { 0 } - 2 U _ { 0 } - p _ { 2 0 } ^ { 2 } }$ ,wherewe choose thepositiveroot.We then follow the solution until it hits again the surface $q _ { 1 } = 0$ in the positive direction $p _ { 1 } > 0$ and obtainapoint $P _ { 1 } = ( q _ { 2 1 } , p _ { 2 1 } )$ ;inthe same way we compute $P _ { 2 } = ( q _ { 2 2 } , p _ { 2 2 } )$ ,etc.For the same initial values as in Fig.3.1 and with $\begin{array} { r } { H _ { 0 } = \frac { 1 } { 1 2 } } \end{array}$ ,the solution for $0 \leq t \leq 3 0 0 0 0 0$ gives $4 6 8 6 5$ Poincarecuts whichareall displayedinFig.3.2(left).They seem to lie exactly onacurve,as do theorbits for5other choices of initial values.This picture thus shows“convincing evidence"for the existence ofa second invariant,for which Gustavson(1966) has deriveda formal expansion,whose first termsrepresent perfectly these curves.

![](images/14d0fcca30639e49ac8b342a015b6716b82ec46cc968e86f7e4794d80c75aa59.jpg)  
Fig.3.4.Global error of numerical methods for nearly quasiperiodicand for chaotic solutions; same initial data asin Fig.3.2

“Butherecomes the surprise”(Henon-Heiles,p.76):Fig.3.2 shows to the right the same picture in the $\left( q _ { 2 } , p _ { 2 } \right)$ plane forasomewhat higher Energy $\begin{array} { r } { H = \frac { 1 } { 8 } } \end{array}$ The motion turnscompletely to chaosand all hope forasecond invariant disappears. Actually,Gustavson's series does not converge.

Numerical Experiments.We nowapply numerical methods,the explicit Euler method to the low energy initial values $\begin{array} { r } { H = \frac { 1 } { 1 2 } } \end{array}$ (Fig.3.3,left),and the implicit Eulermethod to the high energyinitial values(Fig.3.3,right),both methodswitha very small step size $h = 1 0 ^ { - 5 }$ Aswe already expect from ourprevious experiences, theexplicit Euler method tends to increase the energy and turns order intochaos, while the implicit Euler method tendstodecrease itand turns chaos into order.The Stormer-Verlet method(not shown) behaves as the exact solution even for step sizes as large as $h = 1 0 ^ { - 1 }$ ,

In ournext experimentwe study the global error(see Fig.3.4),once for thecase of thenearly quasiperiodic orbit（ $H = \textstyle { \frac { 1 } { 1 2 } }$ ）and once for the chaotic one( $H = \textstyle { \frac { 1 } { 8 } }$ ), both for the explicit Euler,the symplectic Euler,and the Stormer-Verlet scheme. Itmay come asa surprise,that only in the first case we have the same behaviour (linear orquadratic growth) as in Fig.2.3 for the Kepler problem.In the second case ( $H = \textstyle { \frac { 1 } { 8 } }$ )theglobal error growsexponentially forall methods,and the explicit Euler method isworst.

Studyof aMapping.Thepassage fromapoint $P _ { i }$ to the next one $P _ { i + 1 }$ (asexplained forthe left picture of Fig.3.2)can beconsidered asa mapping $\varPhi : P _ { i } \mapsto$ $P _ { i + 1 }$ and the sequence of points $P _ { 0 } , P _ { 1 } , P _ { 2 } , \ldots$ are just the iterates of this mapping. Thismappingisrepresentedforthetwoenergy levels $H = \textstyle { \frac { 1 } { 1 2 } }$ and $H \ = \ { \textstyle \frac { 1 } { 8 } }$ in Fig.3.5and its study allowsto better understand thebehaviour of the orbits.We see no significant difference between the two cases,simply for larger $H$ thedeformationsare more violent and correspond to larger eigenvalues of the Jacobian of $\phi .$ In both cases we have seven fixed points,which correspond to periodic solutions of the system(3.3).Four of themare stableand lieinsidethewhite islands ofFig.3.2.

![](images/247b477cafac3f341fb38df08f0621bb87a0a10611d0b2d621fe659702b06c03.jpg)  
Fig.3.5.The Poincaremap $\varPhi : P _ { 0 }  P _ { 1 }$ fortheHenon-Heiles Model

# I.4 Molecular Dynamics

Wedonot need exact classical trajectories todo this,but must laygreat emphasis on energyconservationas being of primary importance for this reason. (M.P.Allen&D.J.Tildesley1987)

Molecular dynamics requires the solution of Hamiltonian systems(1.1O),where the otalenergy is given by

$$
H ( p , q ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } \frac { 1 } { m _ { i } } p _ { i } ^ { T } p _ { i } + \sum _ { i = 2 } ^ { N } \sum _ { j = 1 } ^ { i - 1 } V _ { i j } \Bigl ( \lVert q _ { i } - q _ { j } \rVert \Bigr ) ,
$$

and $V _ { i j } ( r )$ are given potential functions.Here. $q _ { i }$ and $p _ { i }$ denote the positions and momenta of atoms and $m _ { i }$ istheatomicmassof theithatom.Weremark that the outer solar system (2.12)is such an $N$ -bodysystemwith $V _ { i j } ( r ) = - G m _ { i } m _ { j } / r .$ In moleculardynamics the Lennard-Jones potential

$$
V _ { i j } ( r ) = 4 \varepsilon _ { i j } \bigg ( \Big ( \frac { \sigma _ { i j } } { r } \Big ) ^ { 1 2 } - \Big ( \frac { \sigma _ { i j } } { r } \Big ) ^ { 6 } \bigg )
$$

isverypopular（ $\varepsilon _ { i j }$ and $\sigma _ { i j }$ are suitable constants depending on the atoms). This potential has an absolute minimum atdistance $r = \sigma _ { i j } \sqrt { 2 }$ The forcedue to thispotential strongly repels theatoms when they are closer than this value, and they atract each other when they are farther away.

![](images/981ba1e67a3420f8a6126b5bc217aa8dc5adaffdb763fe60b9c2791d46da2d7e.jpg)

Numerical Experiments with a Frozen Argon Crystal.AsinBiesiadecki& Skeel（1993）weconsider the interaction of seven argon atoms in aplane,where six of themare arranged symmetricallyaroundacentreatom. Asamathematical model we take theHamiltonian（4.1） with $N = 7$ ， $m _ { i } = m = 6 6 . 3 4 \cdot 1 0 ^ { - 2 7 }$ [kg],

![](images/293b615784e06d861fa13e39cf5fe4a9d56bedb44ee9a35f2baec9b1c3cdab86.jpg)

$$
\varepsilon _ { i j } = \varepsilon = 1 1 9 . 8 k _ { B } [ { \bf J } ] , \qquad \sigma _ { i j } = \sigma = 0 . 3 4 1 [ { \mathrm { n m } } ] ,
$$

where $k _ { B } = 1 . 3 8 0 6 5 8 \cdot 1 0 ^ { - 2 3 } \ : [ \mathrm { J / K } ]$ isBoltzmann'sconstant (see Allen& Tildesley (1987),page 21).Asunits for our calculations we take masses in $\left[ \mathrm { k g } \right]$ ,distances in nanometers $\left( 1 [ \mathrm { n m } ] \right) = 1 0 ^ { - 9 } [ \mathrm { m } ] ,$ ,and times in nanoseconds(1 [nsec] $= 1 0 ^ { - 9 }$ [sec]). Initialpositions (in [nm])and initial velocities (in[nm/nsec]) are given in Table4.1. They are chosen such that neighbouring atoms have a distance that is close to the onewith lowest potential energy,and such that the total momentum is zero and therefore the centre of gravitydoes not move.Theenergy at the initial position is $H ( p _ { 0 } , q _ { 0 } ) \approx - 1 2 6 0 . 2 k _ { B }$ [J].

Forcomputations in molecular dynamics one is usually not interested in the trajectories of the atoms,but one aimsat macroscopic quantities such as temperature, pressure,internal energy,etc.Here we consider the total energy,givenby the Hamiltonian,and the temperaturewhich can be calculated from the formula(see Allen&

Table 4.1.Initial values for the simulation ofa frozen argon crystal   

<table><tr><td rowspan=1 colspan=1>atom</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>position</td><td rowspan=1 colspan=1>0.000.00</td><td rowspan=1 colspan=1>0.020.39</td><td rowspan=1 colspan=1>0.340.17</td><td rowspan=1 colspan=1>0.36-0.21</td><td rowspan=1 colspan=1>-0.02-0.40</td><td rowspan=1 colspan=1>-0.35-0.16</td><td rowspan=1 colspan=1>-0.310.21</td></tr><tr><td rowspan=1 colspan=1>velocity</td><td rowspan=1 colspan=1>-30-20</td><td rowspan=1 colspan=1>50-90</td><td rowspan=1 colspan=1>-70-60</td><td rowspan=1 colspan=1>9040</td><td rowspan=1 colspan=1>8090</td><td rowspan=1 colspan=1>-40100</td><td rowspan=1 colspan=1>-80-60</td></tr></table>

![](images/fc9cddb7eada1e699af05f44f63559c5c70f50a0af375d859f2140c5ffed92d1.jpg)  
Fig.4.1.Computed total energyand temperature of the argon crystal

Tildesley (1987),page 46)

$$
T = \frac { 1 } { 2 N k _ { B } } \sum _ { i = 1 } ^ { N } m _ { i } \| \dot { q } _ { i } \| ^ { 2 } .
$$

Weapplytheexplicit and symplectic Euler methodsand alsothe Verlet method tothisproblem.Observe that foraHamiltonian such as（4.1）allthreemethods areexplicit,and all of them need only one force evaluation per integration step.In Fig.4.1 we present the numerical results of our experiments.The integrations are done over an interval of length O.2[nsec].The stepsizes are indicated in femtoseconds $( 1 \ : [ \mathrm { f s e c } ] = 1 0 ^ { - 6 }$ [nsec]).

The two upper pictures show the values $\left( H ( p _ { n } , q _ { n } ) - H ( p _ { 0 } , q _ { 0 } ) \right) / k _ { B }$ asa function oftime $t _ { n } = n h .$ Forthe exact solution,this value isprecisely zero forall times. Similarto earlierexperimentswe see that the symplectic Eulermethodis qualitativelycorrect,whereas the numerical solution of the explicit Euler method,although computed witha much smaller step size,is completely useless (see the citation at thebeginning of this section).TheVerlet method is qualitatively correctand gives much more accurate results than the symplectic Euler method (we shall see later thattheVerletmethod isof order2).The two computationswith theVerletmethod showthat the energy errordecreasesbya factor of4if the step sizeisreduced by a factor of 2 (second order convergence).

Thetwo lower pictures ofFig.4.1 show the numerical values of the temperature difference $T - T _ { 0 }$ with $T$ given by（4.3）and $T _ { 0 } \approx 2 2 . 7 2 [ ]$ K](initialtemperature). Incontrast to thetotal energy,thisisnot anexact invariant,but for ourproblemit fuctuates around aconstant value.The explicit Euler method gives wrongresults, butthe symplectic Eulerand the Verlet methods show thedesired behaviour.This timeareduction of the step size does not reduce the amplitude of the oscillations, which indicates that the fluctuation of the exact temperature is of the same size.

# I.5Highly Oscillatory Problems

Inthis section we discuss a system with almost-harmonic high-frequency oscillations.We show numerical phenomena of methods applied with step sizes that are not small compared to the period of the fastest oscillations.

# I.5.1A Fermi-Pasta-Ulam Problem

...dealing with the behavior of certain nonlinearphysical systems where thenon-linearityis introducedasaperturbation toaprimarily linearproblem.The behaviorof thesystems istobestudied fortimes whicharelong compared to the characteristic periods of the corresponding linear problems. (E.Fermi,J.Pasta,S.Ulam1955)

Inthe early1950sMANIAC-I had justbeencompleted and satpoised foran attack on significant problems....Fermi suggested that itwould behighly instructive to integrate the equations ofmotion numerically for ajudiciously chosen,one-dimensional, harmonic chain of mass points weaklyperturbed by nonlinear forces. (J.Ford 1992)

Theproblem ofFermi,Pasta&Ulam（1955）isa simplemodel for simulations in statistical mechanicswhich revealed highly unexpected dynamical behaviour.We considera modification consisting of a chain of $_ { 2 m }$ mass points,connected with alternating soft nonlinearand stiff linear springs,and fixed at theend points (see Galgani,Giorgill,Martinoli&Vanzini(1992)andFig.5.1).Thevariables $q _ { 1 } , \ldots , q _ { 2 m }$ $q _ { 0 } = q _ { 2 m + 1 } = 0$ ）stand for the displacements of the mass points,and $p _ { i } = { \dot { q } } _ { i }$ for their velocities.The motion is described byaHamiltoniansystem with total energy

![](images/cdaa40818d54c7a4c906b91cf955f57946df0be896d56d8dfed3128fa9de0395.jpg)  
Fig.5.1.Chain with alternating soft nonlinear and stiff linear springs

$$
H ( p , q ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } ( p _ { 2 i - 1 } ^ { 2 } + p _ { 2 i } ^ { 2 } ) + \frac { \omega ^ { 2 } } { 4 } \sum _ { i = 1 } ^ { m } ( q _ { 2 i } - q _ { 2 i - 1 } ) ^ { 2 } + \sum _ { i = 0 } ^ { m } ( q _ { 2 i + 1 } - q _ { 2 i } ) ^ { 4 } ,
$$

where $\omega$ isassumed to be large.It is quite natural to introduce the new variables

![](images/ad55b58c16440a5884248bdd653567d251004a95154fbf1b11ff2f16f1068e21.jpg)  
Fig.5.2.Exchange of energyin the exact solution of the Fermi-Pasta-Ulam model.The picture to theright is an enlargement of the narrow rectangle in the left-hand picture

$$
\begin{array} { r l r } { x _ { 0 , i } \ = \ \big ( q _ { 2 i } + q _ { 2 i - 1 } \big ) / \sqrt { 2 } , } & { } & { x _ { 1 , i } \ = \ \big ( q _ { 2 i } - q _ { 2 i - 1 } \big ) / \sqrt { 2 } , } \\ { y _ { 0 , i } \ = \ \big ( p _ { 2 i } + p _ { 2 i - 1 } \big ) / \sqrt { 2 } , } & { } & { y _ { 1 , i } \ = \ \big ( p _ { 2 i } - p _ { 2 i - 1 } \big ) / \sqrt { 2 } , } \end{array}
$$

where $x _ { 0 , i }$ $i = 1 , \ldots , m )$ representsa scaled displacement of the $i$ th stiff spring, $x _ { 1 , i }$ a scaled expansion (or compression） of the $i$ thstiffspring,and $y _ { 0 , i } , y _ { 1 , i }$ their velocities(or momenta).With this change of coordinates,the motion in the new variablesisagaindescribed bya Hamiltonian system,with

$$
\begin{array} { r c l } { \displaystyle H ( y , x ) ~ = ~ \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } \left( y _ { 0 , i } ^ { 2 } + y _ { 1 , i } ^ { 2 } \right) + \frac { \omega ^ { 2 } } { 2 } \sum _ { i = 1 } ^ { m } x _ { 1 , i } ^ { 2 } + \frac { 1 } { 4 } \Big ( ( x _ { 0 , 1 } - x _ { 1 , 1 } ) ^ { 4 } + } \\ { \displaystyle \quad + \sum _ { i = 1 } ^ { m - 1 } \left( x _ { 0 , i + 1 } - x _ { 1 , i + 1 } - x _ { 0 , i } - x _ { 1 , i } \right) ^ { 4 } + ( x _ { 0 , m } + x _ { 1 , m } ) ^ { 4 } \Big ) . } \end{array}
$$

Besidesthefactthat theequations ofmotionareHamiltonian,sothatthe totalenergy isexactly conserved,they havea further interesting feature.Let

$$
I _ { j } ( x _ { 1 , j } , y _ { 1 , j } ) = \frac { 1 } { 2 } \big ( y _ { 1 , j } ^ { 2 } + \omega ^ { 2 } x _ { 1 , j } ^ { 2 } \big )
$$

denote the energy of the $\mathcal { I }$ th stiff spring.It turnsout that there isan exchange of energy between the stiff springs,but the total oscillatory energy $\textit { I } = \textit { I } _ { 1 } + \ldots +$ $I _ { m }$ remains close to a constant value,in fact, $I { \big ( } ( x ( t ) , y ( t ) ) = I { \big ( } ( x ( 0 ) , y ( 0 ) { \big ) } +$ $\mathcal { O } ( \omega ^ { - 1 } )$ .Foranillustration of this property,we choose $m = 3$ (asin Fig.5.1）, $\omega = 5 0$ ,

$$
x _ { 0 , 1 } ( 0 ) = 1 , \quad y _ { 0 , 1 } ( 0 ) = 1 , \quad x _ { 1 , 1 } ( 0 ) = \omega ^ { - 1 } , \quad y _ { 1 , 1 } ( 0 ) = 1 ,
$$

and zero for the remaining initial values.Fig.5.2 displays the energies $I _ { 1 } , I _ { 2 } , I _ { 3 }$ ofthestiff springs together with the total oscillatory energy $I = I _ { 1 } + I _ { 2 } + I _ { 3 }$ asa function of time.The solution has beencomputed verycarefully with high accuracy, so that thedisplayed oscillationscan be considered as exact.

# I.5.2 Application of Classical Integrators

Which of themethods of theforegoing sections produce qualitatively correctapproximations when the product of the step size $h$ with the high frequency $\boldsymbol { \omega }$ isrelativelylarge？

Linear Stability Analysis.To get an idea of the maximum admissible step size, weneglect the quartic term in the Hamiltonian (5.2),so that thedifferential equation splitsintothe two-dimensional problems $\dot { y } _ { 0 , i } = 0$ , ${ \dot { x } } _ { 0 , i } = y _ { 0 , i }$ and

$$
\dot { y } _ { 1 , i } = - \omega ^ { 2 } x _ { 1 , i } , \quad \dot { x } _ { 1 , i } = y _ { 1 , i } .
$$

Omitting the subscripts,the solution of(5.4) is

$$
{ \binom { y ( t ) } { \omega x ( t ) } } = { \binom { \cos \omega t } { \sin \omega t } } \quad { \cos \omega t } \quad ) { \binom { y ( 0 ) } { \omega x ( 0 ) } } .
$$

Thenumerical solution ofaone-stepmethod applied to(5.4)yields

$$
\left( \begin{array} { c } { { y _ { n + 1 } } } \\ { { \omega x _ { n + 1 } } } \end{array} \right) = M ( h \omega ) \left( \begin{array} { c } { { y _ { n } } } \\ { { \omega x _ { n } } } \end{array} \right) ,
$$

and the eigenvalues $\lambda _ { i }$ of $M ( h \omega )$ determine the long-time behaviour of the numerical solution.Stability(i.e.,boundednessof the solution of(5.5))requires the eigenvalues to be less than or equal to one in modulus.For the explicit Euler method wehave $\lambda _ { 1 , 2 } = 1 \pm i h \omega$ ,so that the energy ${ \cal I } _ { n } = ( y _ { n } ^ { 2 } + \omega ^ { 2 } x _ { n } ^ { 2 } ) / 2$ increasesas $( 1 + h ^ { 2 } \omega ^ { 2 } ) ^ { n / 2 } .$ Forthe implicit Euler method we have $\lambda _ { 1 , 2 } = ( 1 \pm i h \omega ) ^ { - 1 }$ ,and theenergy decreasesas $( 1 + h ^ { 2 } \omega ^ { 2 } ) ^ { - n / 2 } $ Forthe implicit midpointrule,the matrix $M ( h \omega )$ isorthogonal and therefore $I _ { n }$ isexactlypreserved forall $h$ and forall times.Finally,for thesymplecticEulermethodand for the Stormer-Verletscheme we have

$$
\begin{array} { r } { H ( h \omega ) = \left( \begin{array} { c c } { 1 } & { - h \omega } \\ { h \omega } & { 1 - h ^ { 2 } \omega ^ { 2 } } \end{array} \right) , \quad M ( h \omega ) = \left( \begin{array} { c c } { 1 - \frac { h ^ { 2 } \omega ^ { 2 } } 2 } & { - \frac { h \omega } 2 \left( 1 - \frac { h ^ { 2 } \omega ^ { 2 } } 4 \right) } \\ { \frac { h \omega } 2 } & { 1 - \frac { h ^ { 2 } \omega ^ { 2 } } 2 } \end{array} \right) } \end{array}
$$

respectively.For both matrices,the characteristicpolynomial is $\lambda ^ { 2 } - ( 2 - h ^ { 2 } \omega ^ { 2 } ) \lambda + 1 ,$ so that the eigenvalues are ofmodulus one ifand onlyif $| h \omega | \leq 2$ .

Numerical Experiments.We apply several methods to the Fermi-Pasta-Ulam （FPU）problem,with $\omega = 5 0$ and initial dataasgivenin Sect.I.5.1.Theexplicit andimplicit Euler methods givecompletelywrong solutions even for very small stepsizes.Fig.5.3presents the numerical results for $H$ ， $I$ , $I _ { 1 }$ ， $I _ { 2 }$ , $I _ { 3 }$ obtained with theimplicit midpoint rule,thesymplectic Euler,and the Stormer-Verlet scheme. For the small step size $h = 0 . 0 0 1$ all methods give satisfactory results,although the energy exchangeis notreproduced accurately overlong times.The Hamiltonian $H$ andthe total oscillatory energy $I$ arewell conserved over much longer time intervals.The larger step size $h = 0 . 0 3$ has been chosen such that $h \omega = 1 . 5$ isclose to the stability limit of the symplectic Eulerand the Stormer-Verlet methods.The values of $H$ and $I$ are still bounded over very long time intervals,but the oscillations do not represent the true behaviour.Moreover, the averagevalue of $I$ isno longer close to1,as it is for the exact solution.These phenomena call foran explanation, and for numerical methods with an improved behaviour (see Chap.XIII).

![](images/b8c4ae458658078cea557c4bf93279799995ce8e62d2c9a2b5d6fee17dc20184.jpg)  
Fig.5.3.Numerical solution for theFPU problem(5.2）with dataasin Sect.I.5.1,obtained withthe implicit midpointrule(left),symplectic Euler(middle),and Stormer-Verlet scheme (right);the upper pictures use $h = 0 . 0 0 1$ ,the lower pictures $h = 0 . 0 3$ thefirst four pictures show the Hamiltonian $H - 0 . 8$ and theoscillatory energies $I _ { 1 } , I _ { 2 } , I _ { 3 } , I ;$ the last two pictures only show $I _ { 2 }$ andI

# I.6 Exercises

1.Show that theLotka-Volterra problem(1.1)inlogarithmicscale,i.e.,byputting $p = \log u$ and $q = \log v$ ,becomesa Hamiltonian system with the function(1.4) asHamiltonian (see Fig.6.1).

![](images/2fb25c0ca6aa77ecf7b6a8a3c936904f22c2dae41f089ac032ede0b6af3da850.jpg)  
Fig.6.1.Areapreservationin logarithmic scale of theLotka-Volterraflow

2.Apply the symplectic Euler method(or the implicit midpoint rule) to problems such as

$$
{ \binom { \dot { u } } { \dot { v } } } = { \binom { ( v - 2 ) / v } { ( 1 - u ) / u } } \psi \qquad { \binom { \dot { u } } { \dot { v } } } = { \binom { u ^ { 2 } v ( v - 2 ) } { v ^ { 2 } u ( 1 - u ) } }
$$

with various initial conditions.Both problems have the same first integral (1.4) astheLotka-Volterra problem and therefore their solutionsare also periodic. Dothe numerical solutions also show this behaviour?

3.Ageneral two-body problem (sun and planet) is givenby the Hamiltonian

$$
H ( p , p _ { S } , q , q _ { S } ) = \frac { 1 } { 2 M } p _ { S } ^ { T } p _ { S } + \frac { 1 } { 2 m } p ^ { T } p - \frac { G m M } { \| q - q _ { S } \| } ,
$$

where $q _ { S } , q \in \mathbb { R } ^ { 3 }$ are the positions of the sun (mass $M$ and the planet (mass $_ { f } / \iota$ ), $p _ { S } , p \in \mathbb { R } ^ { 3 }$ are their momenta,and $G$ is the gravitational constant.

a)Prove:in heliocentric coordinates $Q : = q - q s$ ,the equations of motion are

$$
\ddot { Q } = - G ( M + m ) { \frac { Q } { \lVert Q \rVert ^ { 3 } } } .
$$

b)Prove that ${ \begin{array} { r } { { \frac { d } { d t } } { \big ( } Q ( t ) \times Q ( t ) { \big ) } = 0 } \end{array} }$ ,sothat $Q ( t )$ stays for all times $t$ in the plane $E = \{ q ; d ^ { T } q = 0 \}$ where $d = Q ( 0 ) \times \dot { Q } ( 0 )$ .

Conclusion.The coordinates corresponding toa basis in $E$ satisfy the twodimensional equations (2.2).

4.In polar coordinates,the two-body problem (2.2) becomes

$$
\ddot { r } = - V ^ { \prime } ( r ) \qquad \mathrm { w i t h } \qquad V ( r ) = { \frac { L _ { 0 } ^ { 2 } } { 2 r ^ { 2 } } } - { \frac { 1 } { r } }
$$

which is independent of $\varphi$ Theangle $\varphi ( t )$ can beobtained by simple integration from $\dot { \varphi } ( t ) = L _ { 0 } / r ^ { 2 } ( t )$ .

5.Compute the period of the solution of the Kepler problem (2.2) and deduce fromtheresult Kepler's“third law”.

Hint.ComparingKepler's second law(2.6)with the area of the elipse gives ${ \scriptstyle \frac { 1 } { 2 } } L _ { 0 } T = a b \pi .$ Thenapply(2.7).The result is $T = 2 \pi ( 2 \vert { \cal H } _ { 0 } \vert ) ^ { - 3 / 2 } = 2 \pi a ^ { 3 / 2 }$

6.Deduce Kepler's first Ilaw from (2.2) by the elegant method ofLaplace(1799). Hint.Multiplying(2.2)with(2.5）gives

$$
L _ { 0 } \ddot { q } _ { 1 } = \frac { d } { d t } \Bigl ( \frac { q _ { 2 } } { r } \Bigr ) , \qquad L _ { 0 } \ddot { q } _ { 2 } = \frac { d } { d t } \Bigl ( - \frac { q _ { 1 } } { r } \Bigr ) ,
$$

and after integration $\begin{array} { r } { L _ { 0 } \dot { q } _ { 1 } = \frac { q _ { 2 } } { r } + B } \end{array}$ ， $\begin{array} { r } { L _ { 0 } \dot { q } _ { 2 } = - \frac { q _ { 1 } } { r } + A } \end{array}$ ,where $A$ and $B$ are integration constants.Then eliminate $\dot { q } _ { 1 }$ and $\dot { q } _ { 2 }$ bymultiplying these equations by $q _ { 2 }$ and $- q _ { 1 }$ respectivelyand by subtracting them.Theresult isaquadratic equation in $q _ { 1 }$ and $q _ { 2 }$

7.Whatever the initial values for the Kepler problem are, $1 + 2 H _ { 0 } L _ { 0 } ^ { 2 } \ge 0$ holds. Hence,the value $e$ iswell defined by(2.9).

Hint. $L _ { 0 }$ is thearea of theparallelogram spanned by the vectors $q ( 0 )$ and ${ \dot { q } } ( 0 )$

8.Implementation of the Stormer-Verlet scheme.Explain why the use of the onestepformulation(1.17）isnumericallymore stablethan that of the two-term recursion (1.15).

9.Runge-Lenz-Pauli vector. Prove that the function

$$
A ( p , q ) = \left( \begin{array} { c } { { p _ { 1 } } } \\ { { p _ { 2 } } } \\ { { 0 } } \end{array} \right) \times \left( \begin{array} { c c } { { 0 } } \\ { { 0 } } \\ { { q _ { 1 } p _ { 2 } - q _ { 2 } p _ { 1 } } } \end{array} \right) = \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } \left( \begin{array} { c } { { q _ { 1 } } } \\ { { q _ { 2 } } } \\ { { 0 } } \end{array} \right)
$$

isafirst integral of the Kepler problem,i.e., $A \big ( p ( t ) , q ( t ) \big ) \ = \ C o n s t$ along solutionsof theproblem.However,itisnota first integral of theperturbed Kepler problem of Exercise12.

10.Add acolumn to Table 2.1 which shows the long-time behaviour of theerror in the Runge-Lenz-Pauli vector (see Exercise 9) for the various numerical integrators.

11.For the Kepler problem,eliminate $( p _ { 1 } , p _ { 2 } )$ from the relations ${ \cal H } ( p , q ) = C o n s t$ , $L ( p , q ) ~ = ~ C o n s t$ and $A ( p , q ) ~ = ~ C o n s t$ Thisgivesa quadratic relation for $( q _ { 1 } , q _ { 2 } )$ and proves that the solution lies onan ellipse,a parabola,or on a hyperbola.

12.Study numerically the solution of the perturbed Kepler problem with Hamiltonian

$$
H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = \frac { 1 } { 2 } \left( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } \right) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } - \frac { \mu } { 3 \sqrt { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 } } } ,
$$

where $\mu$ isa positive or negative small number.Among others,this problem describes themotion ofa planet in the Schwarzschild potential for Einstein's general relativity theory7.You will observe a precession of the perihelion,which,applied to the orbit ofMercury,represented the historically first verification of Einstein’s theory (seee.g.,Birkhoff 1923,p.261-264).

![](images/367faa04ca35585f142ded582c7fa3e42e6e29afe19b1697149082a985d64e6b.jpg)

The precession can also be expressed analytically:the equation for $u = 1 / r$ as a function of $\varphi$ ,correspondingto(2.8),here becomes

$$
u ^ { \prime \prime } + u = \frac { 1 } { d } + \mu u ^ { 2 } ,
$$

where $d = L _ { 0 } ^ { 2 } .$ Now compute the derivative of this solution with respect to $\mu$ ， at $\mu = 0$ and $\boldsymbol { u } = ( 1 + e \cos ( \varphi - \varphi ^ { * } ) ) / d$ after one period $t = 2 \pi$ This leadsto $\eta = \mu ( e / d ^ { 2 } ) \cdot 2 \pi \sin \varphi$ (see the small picture).Then,for small $\mu$ ,theprecession afterone period is

$$
\Delta \varphi = \frac { 2 \pi \mu } { d } .
$$

# Chapter II. Numerical Integrators

Afterhaving seen in Chap.I some simple numerical methods and avariety of numerical phenomena that they exhibited,we nowpresent more elaborateclassesof numerical methods.We start with Runge-Kutta and collocation methods,and we introduce discontinuous collocation methods,which cover essentiallyall high-order implicit Runge-Kutta methods of interest.We then treat partitioned Runge-Kutta methods and Nystrom methods,which can be applied to partitioned problems such asHamiltonian systems.Finallywe present composition and splitingmethods.

# II.1 Runge-Kutta and Collocation Methods

![](images/6a0873dbd1d07ad8dc58d98121c8049ba4378c690f6b6a7ab8ff804fdcdab72a.jpg)  
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

![](images/8098b19ecb63fcdfaacc1584a3e182e3ea3bf5de095ece7de48d2c299776adc7.jpg)  
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

![](images/385b966d9911de252bb749c40ce452dafaac76ff4e6112376bee7b361acef831.jpg)

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

![](images/3dedc4046007706c705bc72ec122bdc996b5ee5627d54bf1348acbaade7d80f0.jpg)  
Fig.1.3.Collocationsolutions for the Lotka-Volterra problem(I.1.1); $u _ { 0 } = 0 . 2$ , $v _ { 0 } = 3 . 3$ ; methodsof order2:foursteps with $h = 0 . 4$ method of order4:twostepswith $h = 0 . 8$ ; dotted: exact solution

For $s \ = \ 2$ and $c _ { 1 } ~ = ~ 0 , c _ { 2 } ~ = ~ 1$ we find,of course,the implicit trapezoidal rule.The choice of Hammer&Hollingsworth for thecollocation points is $c _ { 1 , 2 } = 1 / 2 \pm \sqrt { 3 } / 6$ ,theGaussian quadrature nodes (see the picture to the right).We will see that the correspondingmethod is of order 4.

In Fig.1.3we illustrate the collocation idea with these methods for the Lotka-Volterra problem (I.1.1).One can observe that,in spite oftheextremely large step sizes,themethodsarequite satisfactory.

![](images/a52c1a73ac62e478e96462dbc82da14fe292252e401ef19971c8d09c53d017c5.jpg)

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

![](images/aa828b44a813d2b85b0ecacc16be78d1c8b61bfe8edaf88617a96fd5e473f1fb.jpg)

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

![](images/d0b52597b1829decc6ae57b37f8bd31226db489c637062a577ca6fa2e17b8e7f.jpg)  
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

![](images/1ee4a15ad8d75a145eb785474d4f29b093e2e83551d317227e46005e1f58cedb.jpg)  
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

![](images/5ba6c0bf6cbf39acef9cc8103833a09c8bcc66e8d7c0ddd3ddd9f2c3a173820a.jpg)  
Fig.4.2.The TripleJumpof order 4and itsiterates of orders6and8

Example 4.3(Suzuki'sFractals).If one desires methodswith smallervalues of $\gamma _ { i }$ ,onehasto increaseseven more.Forexample,for $s = 5$ the best solution of （4.2) has the sign structure $+ + - + +$ with $\gamma _ { 1 } = \gamma _ { 2 }$ (see Exercise 7).This leads to （Suzuki 1990)

$$
\gamma _ { 1 } = \gamma _ { 2 } = \gamma _ { 4 } = \gamma _ { 5 } = \frac { 1 } { 4 - 4 ^ { 1 / ( p + 1 ) } } , \qquad \gamma _ { 3 } = - \frac { 4 ^ { 1 / ( p + 1 ) } } { 4 - 4 ^ { 1 / ( p + 1 ) } } .
$$

The repetition of this algorithm for $p = 2 , 4 , 6 , \ldots$ leads toa fractal structure of the step points(see Fig.4.3）.

![](images/6870fc6058ca7bf5fa1fa6de094abdf7dc28135a4a168e6a5a8bc09c91eec55d.jpg)  
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

![](images/5ac09ca5abe08cb8258ffd6563b2bfc0cccf0296200cb6eacc93f4d89143666f.jpg)  
Fig.4.4.Numerical results of the Triple Jumpand Suzuki step sequences (grey symbols) compared to optimal methods(black symbols）

# I.5Splitting Methods

Thesplitting idea yieldsan approach that is completely different from Runge-Kutta methods.One decomposes the vector field into integrable piecesand treats them separately.

![](images/26e04ba8915ec025bd61050f06cc353eece2a6f2df924d3c8f3faa525e811ac8.jpg)  
Fig.5.1.A splitting ofa vector field

Weconsideranarbitrary system $\dot { y } = f ( y )$ in $\mathbb { R } ^ { n }$ ,and suppose that thevector fieldis"split”as(see Fig.5.1）

$$
\dot { y } = f ^ { [ 1 ] } ( y ) + f ^ { [ 2 ] } ( y ) .
$$

Ifthen,byceeactfos $\varphi _ { t } ^ { [ 1 ] }$ and $\varphi _ { t } ^ { [ 2 ] }$ of the systems $\dot { y } = f ^ { [ 1 ] } ( y )$ and $\dot { y } = f ^ { [ 2 ] } ( y )$ can becalculated explicitly,wecan,froma given initial value $y _ { 0 }$ ,first solve the first system to obtain a value $y _ { \mathrm { I / 2 } }$ ,andfrom thisvalueintegrate the second system to obtain $y _ { 1 } .$ Inthiswaywe have introduced the numerical methods

![](images/cbd8202a5ad6cafd20bf0a7d1980849c2b8aa9bd8093c3bf59222648d8992b24.jpg)

where one is the adjoint of the other.These formulas are often called the $L i e \mathrm { - }$ Trtel $( \varphi _ { h } ^ { [ 1 ] } \circ \varphi _ { h } ^ { [ 2 ] } ) ( y _ { 0 } ) =$ ）（y0）= $\varphi _ { h } ( y _ { 0 } ) + \mathcal { O } ( h ^ { 2 } )$ ,so that both methods give approximations of order $^ { 1 }$ to the solution of(5.1).Another idea is to use a symmetric version and put

![](images/701b7c06d9aa159a409e8c0589bc030895d921d9cb03b7d79235f13e09afb6d3.jpg)

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

![](images/c0795e63e506e81f3f80713d412d04eab4d91a26c98ab59b354a81e230290809.jpg)  
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

# Chapter III. Order Conditions,Treesand B-Series

Inthis chapter we present acompact theory of the order conditions of the methodspresented in Chap.II, in particular Runge-Kutta methods,partitioned Runge-Kuttamethods,and composition methods by using the notion of rooted trees and B-series.These ideas lead to algebraic structureswhich haverecently found interestingapplications inquantum field theory.The chapter terminateswith the Baker-Campbell-Hausdorff formula,which allowsanother access to the order properties ofcomposition and splitting methods.

Someparts of this chapter are rather short,but nevertheless self-contained.For more detailed presentations werefer to the monographs of Butcher(1987),of Hairer, Ngrsett&Wanner(1993）,andofHairer&Wanner(1996).Readersmainlyinterested in geometric properties of numerical integrators may continue with ChaptersIV,VorVI beforereturningtothe technically moredifficult jungleof trees.

# III.1Runge-Kutta Order Conditions and B-Series

Even the standard notation has been found to be too heavy indealingwith fourthand higher order processes,... (R.H.Merson 1957）

Inthis section we derive the order conditions of Runge-Kutta methods by comparing the Taylor series of the exact solution of（1.1）with that of thenumerical solution.The computation ismuch simplified,first by consideringan autonomous system of equations(Gill 1951),and second,by the use of rooted trees (connected graphswithout cycles and a distinguished vertex;Merson 1957).The theory has beendeveloped by Butcherin theyears 1963-72(seeButcher(1987),Sect.30)and byHairer&Wannerin1973-74（seeHairer,Ngrsett&Wanner（1993)SectionsII.2 andII.12).Herewe give new simplified proofs.

# III.1.1 Derivation of the Order Conditions

We consider an autonomous problem

$$
\dot { y } = f ( y ) , \qquad y ( t _ { 0 } ) = y _ { 0 } ,
$$

where $f : \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ issufficientlydifferentiable.Aproblem $\dot { \boldsymbol { y } } = \boldsymbol { f } ( t , \boldsymbol { y } )$ can be brought into this form by appending the equation $i = 1$ .We develop the subsequent theory in four steps.