# Ernst Hairer Gerhard Wanner

# Solving Ordinary Differential Equations l

Stiffand Differential-Algebraic Problems

Second Revised Edition

# Springer Series in Computational Mathematics

Editorial Board R. Bank   
R.L. Graham   
J. Stoer   
R. Varga   
H. Yserentant

E. Hairer G. Wanner

# Solving Ordinary Differential Equations Il

Stiff and Differential-Algebraic Problems

Second Revised Edition With 137 Figures

Ernst Hairer   
Gerhard Wanner   
Universitéde Geneve   
Section de Mathématiques   
2-4 rue du Lievre   
1211 Geneve 4   
Switzerland   
Ernst.Hairer@unige.ch   
Gerhard.Wanner@unige.ch

ISSN 0179-3632 ISBN 978-3-540-60452-5 (hardcover) ISBN 978-3-642-05220-0 (s0ftcover) DOI 10.1007/978-3-642-05221-7 Springer Heidelberg Dordrecht London New York e-ISBN 978-3-642-05221-7

Library of Congress Control Number: 2009939073

Mathematics Subject Classification (2ooo): 65Lxx, 34A50 $^ ©$ Springer-Verlag Berlin Heidelberg 1991, 1996, Corrected printing 2oo2. First softcover printing 2010

This work is subject to copyright. Al rights are reserved, whether the whole or part of the material is concerned,specifically the rights of translation, reprinting,reuse of illustrations, recitation,broadcasting,reproduction on microfilm or in any other way,and storage in data banks. Duplication of this publication or parts thereof is permitted only under the provisions of the German Copyright Law of September 9,1965, in its current version, and permission for use must always be obtained from Springer. Violations are liable to prosecution under the German Copyright Law.

The use of general descriptive names, registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

Cover design: SPi Publisher Services

Printed on acid-free paper

Springer is part of Springer Science $+$ Business Media (www.springer.com)

# From the Preface to the First Edition

"Whatever regrets may be, we have done our best." (Sir Ernest Shackleton, turning back on 9 January 1909 at $8 8 ^ { \circ } 2 3 ^ { \circ }$ South.)

Brahms struggled for 2O years to write his first symphony. Compared to this, the 10 years we have been working on these two volumes may even appear short.

This second volume treats stiff differential equations and differential algebraic equations. It contains three chapters: Chapter IV on one-step (Runge-Kutta) methods for stiff problems, Chapter V on multistep methods for stiff problems,and Chapter VI on singular perturbation and differential-algebraic equations.

Each chapter is divided into sections. Usually the first sections of a chapter are of an introductory nature, explain numerical phenomena and exhibit numerical results. Investigations of a more theoretical nature are presented in the later sections of each chapter.

As in Volume I, the formulas, theorems, tables and figures are numbered consecutively in each section and indicate,in addition,the section number. In cross references to other chapters the (latin) chapter number is put first. References to the bibliography are again by “author” plus“year” in parentheses. The bibliography again contains only those papers which are discussed in the text and is in no way meant to be complete.

It is a pleasure to thank J. Butcher, G. Dahlquist, and S.P. Norsett (coauthor of Volume I) for their interest in the subject and for the numerous discussions we had with them which greatly inspired our work. Special thanks go to the participants of our seminar in Geneva, in particular Ch. Lubich,A. Ostermann and M. Roche, where all the subjects of this book have been presented and discussed over the years. Much help in preparing the manuscript was given by J. Steinig, Ch. Lubich and A. Ostermann who read and re-read the whole text and made innumerable corrections and suggestions for improvement. We express our sincere gratitude to them. Many people have seen particular sections and made invaluable suggestions and remarks: M. Crouzeix, P.Deuflhard, K. Gustafsson, G. Hall, W. Hundsdorfer, L. Jay, R. Jeltsch, J.P. Kauthen,H. Kraaijevanger,R. März, and O. Nevanlinna. .. Several pictures were produced by our children Klaudia Wanner and Martin Hairer, the one by drawing the other by hacking.

The m arvellous, perfect and never failing TEX program of D. Knuth allowed us to deliver a camera-ready manuscript to Springer Verlag, so that the book could be produced rapidly and at a reasonable price. We acknowledge with pleasure the numerous remarks of the planning and production group of Springer Verlag concerning fonts, style and other questions of elegance.

# Preface to the Second Edition

The preparation of the second edition alowed us to improve the first edition by rewriting many sections and by eliminating errors and misprints which have been discovered. In particular we have included new material on

methods with extended stability (Chebyshev methods) (Sect.IV.2);   
improved computer codes and new numerical tests for one- and multistep methods (Sects.IV.10 and V.5);   
new results on properties of error growth functions (Sects. IV.11 and IV.12);   
quasilinear differential equations with state-dependent mass matrix (Sect. VI.6).

We have completely reorganized the chapter on diffrential-algebraic equations by including three new sections on

index reduction methods (Sect. VII.2);   
half-explicit methods for index-2 systems (Sect. VII.6);   
symplectic methods for constrained Hamiltonian systems and backward error analysis on manifolds (Sect. VII.8).

Our sincere thanks go to many persons who have helped us with our work:

all readers who kindly drew our attention to several errors and misprints in the first edition, in particular C. Bendtsen,R. Chan, P. Chartier, T. Eirola, L. Jay, P. Kaps, J.-P. Kauthen, P. Leone, S. Maset, B. Owren, and L.F. Shampine;

-those who read preliminary versions of the new parts of this edition for their invaluable suggestions: M. Arnold, J. Cash, D.J. Higham, P. Kunkel, Chr. Lubich, A. Medovikov, A. Murua, A. Ostermann, and J. Verwer.

-the staff of the Geneva computing center and of the mathematics library for their constant help; the planning and production group of Springer-Verlag for numerous suggestions on presentation and style.

All figures have been recomputed and printed, together with the text, in Postscript. All computations and text processings were done on the SUN workstations of the Mathematics Department of the University of Geneva.

# Contents

# Chapter IV. Stiff Problems - One-Step Methods

IV.1 Examples of Stiff Equations ... 2

Chemical Reaction Systems .... 3   
Electrical Circuits 4   
Diffusion 6   
A “Stiff" Beam 8   
High Oscillations 11   
Exercises ， 11

# IV.2Stability Analysis for Explicit RK Methods ... 15

Stability Analysis for Euler's Method. 15   
Explicit Runge-Kutta Methods 16   
Extrapolation Methods 18   
Analysis of the Examples of IV.1 18   
Automatic Stiffness Detection 21   
Step-Control Stability 24   
A PI Step Size Control 28   
Stabilized Explicit Runge-Kutta Methods 31   
Exercises 37

# IV.3 Stability Function of Implicit RK-Methods ... 40

The Stability Function 40   
$A$ -Stability   
$L$ -Stability and $A ( \alpha )$ -Stability 44   
Numerical Results 46   
Stability Functions of Order $\geq s$ 47   
Padé Approximations to the Exponential Function 48   
Exercises 49

IV.4 Order Stars.... 51

Introduction 51   
Order and Stability for Rational Approximations 56   
Stability of Padé Approximations 58   
Comparing Stability Domains. 58   
Rational Approximations with Real Poles 61   
The Real-Pole Sandwich... 62   
Multiple Real-Pole Approximations 67   
Exercises 70

# IV.5 Construction of Implicit Runge-Kutta Methods .... 71

Gauss Methods 71   
Radau IA and Radau IIA Methods 72   
Lobatto IIIA, IIB and IIIC Methods 75   
The W -Transformation 77   
Construction of Implicit Runge-Kutta Methods . 83   
Stability Function 84   
Positive Functions 86   
Exercises ... 89

# IV.6Diagonally Implicit RK Methods .. 91

Order Conditions 91   
Stiffly Accurate SDIRK Methods 92   
The Stability Function .. 96   
Multiple Real-Pole Approximations with $R ( \infty ) { = } 0$ 98   
Choice of Method 99   
Exercises.. 100

IV.7 Rosenbrock-Type Methods... 102

Derivation of the Method 102   
Order Conditions... 104   
The Stability Function 108   
Construction of Methods of Order 4 108   
Higher Order Methods 111   
Implementation of Rosenbrock-Type Methods 111   
The“Hump” 113   
Methods with Inexact Jacobian (W -Methods) 114   
Exercises 117

# IV.8 Implementation of Implicit Runge-Kutta Methods ... 118

Reformulation of the Nonlinear System 118   
Simplified Newton Iterations 119   
The Linear System 121   
Step Size Selection 123   
Implicit Differential Equations 127   
An SDIRK-Code 128   
SIRK-Methods 128   
Exercises 130

IV.9 Extrapolation Methods ... 131

Extrapolation of Symmetric Methods 131   
Smoothing... 133   
The Linearly Implicit Mid-Point Rule 134   
Implicit and Linearly Implicit Euler Method 138   
Implementation 139   
Exercises.. 142

IV.10 Numerical Experiments ... 143

The Codes Used 143   
Twelve Test Problems 144   
Results and Discussion 152   
Partitioning and Projection Methods 160   
Exercises .. 165

# IV.11 Contractivity for Linear Problems .... 167

Euclidean Norms (Theorem of von Neumann) 168   
Error Growth Function for Linear Problems 169   
Small Nonlinear Perturbations 172   
Contractivity in $\| \cdot \| _ { \infty }$ and $\Vert \cdot \Vert _ { 1 }$ 175   
Study of the Threshold Factor 176   
Absolutely Monotonic Functions 178   
Exercises 179

# [V.12 B-Stability and Contractivity.... 180

One-Sided Lipschitz Condition 180   
$B$ -Stability and Algebraic Stability 181   
Some Algebraically Stable IRK Methods 183   
$A N$ -Stability ... 184   
Reducible Runge-Kutta Methods 187   
The Equivalence Theorem for $S$ -Irreducible Methods 188   
Error Growth Function 193   
Computation of $\varphi _ { B } ( x )$ 195   
Exercises ... 199

# [V.13 Positive Quadrature Formulas and B-Stable RK-Methods .. 201

Quadrature Formulas and Related Continued Fractions.. 201   
Number of Positive Weights... 203   
Characterization of Positive Quadrature Formulas 205   
Necessary Conditions for Algebraic Stability 206   
Characterization of Algebraically Stable Methods 209   
The “Equivalence”of $A$ - and $B$ -Stability 211   
Exercises 213

# [V.14 Existence and Uniqueness of IRK Solutions ... 215

Existence.. 215   
A Counterexample 217   
Influence of Perturbations and Uniqueness 218   
Computation of $\alpha _ { 0 } ( A ^ { - 1 } )$ 220   
Methods with Singular $A$ 222   
Lobatto IIC Methods 223   
Exercises. 223

IV.15 B-Convergence .. 225

The Order Reduction Phenomenon 225   
The Local Error ... 228   
Error Propagation.. 229   
$B$ -Convergence for Variable Step Sizes 230   
$B$ -Convergence Implies Algebraic Stability 232   
The Trapezoidal Rule.. 234   
Order Reduction for Rosenbrock Methods 236   
Exercises 237

# Chapter V. Multistep Methods for Stiff Problems

V.1Stability of Multistep Methods... 240

The Stability Region ，，， 240   
Adams Methods 242   
Predictor-Corrector Schemes 244   
Nystrom Methods 245   
BDF 246   
The Second Dahlquist Barrier 247   
Exercises 249

# V.2“Nearly” A-Stable Multistep Methods .... 250

$A ( \alpha )$ -Stability and Stiff Stability 250   
High Order $A ( \alpha )$ -Stable Methods 251   
Approximating Low Order Methods with High Order Ones .... 253   
A Disc Theorem 254   
Accuracy Barriers for Linear Multistep Methods 254   
Exercises 259

# V.3Generalized Multistep Methods .. 261

Second Derivative Multistep Methods of Enright . 261   
Second Derivative BDF Methods 265   
Blended Multistep Methods 266   
Extended Multistep Methods of Cash 267   
Multistep Collocation Methods 270   
Methods of “Radau” Type 273   
Exercises 275

# V.4Order Stars on Riemann Surfaces ... 279

Riemann Surfaces... 279   
Poles Representing Numerical Work 283   
Order and Order Stars .. 284   
The“Daniel and Moore Conjecture” 286   
Methods with Property $C$ 288   
General Linear Methods 290   
Dual Order Stars 295   
Exercises 297

# V.5Experiments with Multistep Codes .... 300

The Codes Used 300   
Exercises 304

# V.6One-Leg Methods and G-Stability 305

One-Leg(Multistep) Methods 305   
Existence and Uniqueness 306   
$G$ -Stability 307   
An Algebraic Criterion 309   
The Equivalence of $A$ -Stability and $G$ -Stability 310   
A Criterion for Positive Functions 313   
Error Bounds for One-Leg Methods 314   
Convergence of $A$ -Stable Multistep Methods 317   
Exercises 319

# V.7Convergence for Linear Problems .... 321

Difference Equations for the Global Error 321   
The Kreiss Matrix Theorem 323   
Some Applications of the Kreiss Matrix Theorem 326   
Global Error for Prothero and Robinson Problem 328   
Convergence for Linear Systems with Constant Coefficients 329   
Matrix Valued Theorem of von Neumann 330   
Discrete Variation of Constants Formula 332   
Exercises 337

# V.8Convergence for Nonlinear Problems .... 339

Problems Satisfying a One-Sided Lipschitz Condition 339   
Multiplier Technique 342   
Multipliers and Nonlinearities 346   
Discrete Variation of Constants and Perturbations 348   
Convergence for Nonlinear Parabolic Problems 349   
Exercises 354

# V.9Algebraic Stability of General Linear Methods ... 356

$G$ -Stability ， 356

Algebraic Stability.... 357   
AN -Stability and Equivalence Results 359   
Multistep Runge-Kutta Methods 362   
Simplifying Assumptions 363   
Quadrature Formulas 365   
Algebraically Stable Methods of Order 2s 366   
$B$ -Convergence 368   
Exercises 370

# Chapter VI. Singular Perturbation Problems and Index 1 Problems

VI.1 Solving Index 1 Problems 372

Asymptotic Solution of van der Pol's Equation 372   
The $\varepsilon$ -Embedding Method for Problems of Index 1 374   
State Space Form Method 375   
A Transistor Amplifier 376   
Problems of the Form $M u ^ { \prime } { = } \varphi ( u )$ 378   
Convergence of Runge-Kutta Methods 380   
Exercises 381

# VI.2 Multistep Methods 382

Methods for Index 1 Problems 382   
Convergence for Singular Perturbation Problems 383   
Exercises 387

# VI.3 Epsilon Expansions for Exact and RK Solutions.. 388

Expansion of the Smooth Solution 388   
Expansions with Boundary Layer Terms 389   
Estimation of the Remainder 391   
Expansion of the Runge-Kutta Solution 392   
Convergence of RK-Methods for Differential-Algebraic Systems 394   
Existence and Uniqueness of the Runge-Kutta Solution 397   
Influence of Perturbations .. 398   
Estimation of the Remainder in the Numerical Solution 399   
Numerical Confirmation 403   
Perturbed Initial Values 405   
Exercises 406

# VI.4 Rosenbrock Methods 407

Definition of the Method 407   
Derivatives of the Exact Solution 408   
Trees and Elementary Differentials 409   
Taylor Expansion of the Exact Solution 411   
Taylor Expansion of the Numerical Solution 412   
Order Conditions 415   
Convergence ... 416   
Stiffly Accurate Rosenbrock Methods 418   
Construction of RODAS,a Stiffly Accurate Embedded Method.. 420   
Inconsistent Initial Values 422   
Exercises.. 424

VI.5 Extrapolation Methods .. 426

Linearly Implicit Euler Discretization 426   
Perturbed Asymptotic Expansion 428   
Order Tableau .. 431   
Error Expansion for Singular Perturbation Problems 433   
Dense Output 438   
Exercises 441

VI.6 Quasilinear Problems 442

Example: Moving Finite Elements .. 442   
Problems of Index One .. 445   
Numerical Treatment of $C ( y ) y ^ { \prime } = f ( y )$ 446   
Extrapolation Methods 447   
Exercises 448

# Chapter VII. Differential-Algebraic Equations of Higher Index

VII.1 The Index and Various Examples ， 452

Linear Equations with Constant Coefficients 452   
Differentiation Index ... 454   
Differential Equations on Manifolds 457   
The Perturbation Index 459   
Control Problems.. 461   
Mechanical Systems 463   
Exercises.. 465

VII.2 Index Reduction Methods 46

Index Reduction by Differentiation 468   
Stabilization by Projection 470   
Differential Equations with Invariants 472   
Methods Based on Local State Space Forms 474   
Overdetermined Differential-Algebraic Equations 477   
Unstructured Higher Index Problems 478   
Exercises 480

# VII.3 Multistep Methods for Index 2 DAE .. 481

Existence and Uniqueness of Numerical Solution. . 482   
Influence of Perturbations 484   
The Local Error .. 485   
Convergence for BDF 486   
General Multistep Methods 489   
Solution of the Nonlinear System by Simplified Newton 490   
Exercises.. 491

# VII.4 Runge-Kutta Methods for Index 2 DAE 492

The Nonlinear System ... 492   
Estimation of the Local Error 494   
Convergence for the $\pmb { y }$ -Component 496   
Convergence for the $\pmb { z }$ -Component 497   
Collocation Methods. 498   
Superconvergence of Collocation Methods 500   
Projected Runge-Kutta Methods 502   
Summary of Convergence Results 504   
Exercises 505

# VII.5 Order Conditions for Index 2 DAE 506

Derivatives of the Exact Solution 506   
Trees and Elementary Differentials 507   
Taylor Expansion of the Exact Solution 508   
Derivatives of the Numerical Solution 510   
Order Conditions 512   
Simplifying Assumptions 514   
Projected Runge-Kutta Methods 515   
Exercises 518

# VII.6 Half-Explicit Methods for Index 2 Systems 519

Half-Explicit Runge-Kutta Methods 520   
Extrapolation Methods 525   
$\beta$ -Blocked Multistep Methods 527   
Exercises 529

# VII.7 Computation of Multibody Mechanisms ... 530

Description of the Model 530   
Fortran Subroutines 533   
Computation of Consistent Initial Values 535   
Numerical Computations 536   
A Stiff Mechanical System 541   
Exercises 542

# VII.8 Symplectic Methods for Constrained Hamiltonian Systems . 543

Properties of the Exact Flow 544   
First Order Symplectic Method 545   
SHAKE and RATTLE 548   
The Lobatto IIIA-IIB Pair 550   
Composition Methods 554   
Backward Error Analysis (for ODEs) 555   
Backward Error Analysis on Manifolds 559   
Exercises 562

# Appendix. Fortran Codes 565

Driver for the Code RADAU5 566   
Subroutine RADAU5 568   
Subroutine RADAUP 574   
Subroutine RODAS 574   
Subroutine SEULEX 575   
Problems with Special Structure 575   
Use of SOLOUT and of Dense Output 576

Bibliography 577

Symbol Index ... 605

Subject Index .. 607

# Chapter IV. Stiff Problems - One-Step Methods

This chapter introduces stiff (styv (Swedish first!), steif (German), stif (Islandic), stijf (Dutch), raide (French), rigido (Spanish), rigido (Portuguese),stiff (Italian), kankea (Finnish)， δóokαμπTo (Greek)，merev (Hungarian), rigid (Rumanian), tog (Slovenian),vrst (Serbo-Croatian), tuhy (Czecho-Slovakian), sztywny (Polish), jaik (Estonian),stiegrs (Latvian), standus (Lithuanian),stign (Breton), zurrun (Basque)， sert(Turkish)， xkecTky (Russian)，TBbpⅡ(Bulgarian), $\cos \theta \sin \theta$ (Vietnamese), ngumu (Swaheli) ...) differential equations. While the intuitive meaning of stiff is clear to all specialists, much controversy is going on about it's correct mathematical definition (see e.g. p.360-363 of Aiken (1985)). The most pragmatical opinion is also historically the first one (Curtiss & Hirschfelder 1952): stiff equations are equations where certain implicit methods, in particular BDF, perform better, usually tremendously better, than explicit ones. The eigenvalues of the Jacobian $\partial f / \partial y$ play certainly a role in this decision, but quantities such as the dimension of the system, the smoothness of the solution or the integration interval are also important (Sections IV.1 and IV.2).

Stiff equations need new concepts of stability (A-stability, Sect.IV.3) and lead to mathematical theories on order restrictions (order stars, Sect.IV.4). Stiff equa-tions require implicit methods; we therefore focus in Sections IV.5 and IV.6 on implicit Runge-Kutta methods, in IV.7 on (semi-implicit) Rosenbrock methods and in IV.9 on semi-implicit extrapolation methods. The actual efcient implementation of implicit Runge-Kutta methods poses a number of problems which are discussed in Sect. IV.8. Section IV.10 then reports on some numerical experience for all these methods.

With Sections IV.11,IV.12 and IV.13 we begin with the discussion of contractivity ( $B$ -stability) for linear and nonlinear differential equations. The chapter ends with questions of existence and numerical stability of the implicit Runge-Kutta solutions (Sect.IV.14) and a convergence theory which is independent of the stiffness （ $B$ -convergence, Sect.IV.15).

# IV.1 Examples of Stiff Equations

... Around 1960, things became completely different and everyone became aware that the world was fullof stiff problems.

(G.Dahlquist in Aiken 1985)

Stiff equations are problems for which explicit methods don't work. Curtiss & Hirschfelder (1952) explain stiffness on one-dimensional examples such as

$$
y ^ { \prime } = - 5 0 ( y - \cos x ) .
$$

![](images/44294b653f8fe56307ca6a1026d21239ebc909df8a4d72ebc62f24fdf8a08795.jpg)  
Fig. 1.1. Solution curves of (1.1) with implicit Euler solution

![](images/b205967b69c4ec14316e380cdeb5f3881d567844de8882a7c1dd82e5365dad35.jpg)  
Fig.1.2.Explicit Euler for $y ( 0 ) = 0$ ， $h = 1 . 9 7 4 / 5 0$ and 1.875/50

Solution curves of Equation (1.1) are shown in Fig.1.1. There is apparently a smooth solution in the vicinity of $y \approx \cos x$ and all other solutions reach this one after a rapid “transient phase". Such transients are typical of stiff equations, but are neither suficient nor necessary. For example, the solution with initial value $y ( 0 ) =$ 1 (more precisely 2500/2501） has no transient. Fig.1.2 shows Euler polygons for the initial value $y ( 0 ) = 0$ and step sizes $h = 1 . 9 7 4 / 5 0$ (38 steps） and $h =$ 1.875/50 (40 steps)． We observe that whenever the step size is a litle too large (larger than 2/5O),the numerical solution goes too far beyond the equilibrium and violent oscillations occur.

Looking for better methods for differential equations such as (1.1),Curtiss and Hirschfelder discovered the BDF method (see Sect.III.1): the approximation $y \approx \cos x$ (i.e., $f ( x , y ) = 0 { \mathrm { . } }$ ） is only a crude approximation to the smooth solution, since the derivative of cos $\boldsymbol { x }$ is not zero. It is much better, for a given solution value $y _ { n }$ , to search for a point $y _ { n + 1 }$ where the slope of the vector field is directed towards $y _ { n }$ , hence

$$
{ \frac { y _ { n + 1 } - y _ { n } } { h } } = f ( x _ { n + 1 } , y _ { n + 1 } ) .
$$

This is the implicit Euler method. The dotted line in Fig.1.1 consists of three implicit Euler steps and demonstrates impressively the good stability property of this method. Equation (1.1) is thus apparently “stiff” in the sense of Curtiss and Hirschfelder.

Extending the above idea“by taking higher order polynomials to fit $y$ at a large number of points" then leads to the BDF methods.

# Chemical Reaction Systems

When the equations represent the behaviour of a system containing a number of fast and slow reactions,a forward integration of these equations becomes difficult. (H.H. Robertson 1966)

The following example of Robertson's (1966) has become very popular in numerical studies (Willoughby 1974):

$$
\begin{array} { c c c } { { A } } & { { \xrightarrow { 0 . 0 4 } } } & { { B } } \\ { { B + B } } & { { \xrightarrow { 3 \cdot 1 0 ^ { 7 } } } } & { { C + B } } \\ { { B + C } } & { { \xrightarrow { 1 0 ^ { 4 } } } } & { { A + C } } \end{array}
$$

which leads to the equations

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = - 0 . 0 4 y _ { 1 } + 1 0 ^ { 4 } y _ { 2 } y _ { 3 } \qquad } & & { y _ { 1 } ( 0 ) = 1 } \\ & { y _ { 2 } ^ { \prime } = } & { 0 . 0 4 y _ { 1 } - 1 0 ^ { 4 } y _ { 2 } y _ { 3 } - 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & & { y _ { 2 } ( 0 ) = 0 } \\ & { y _ { 3 } ^ { \prime } = } & & { 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & & { y _ { 3 } ( 0 ) = 0 . } \end{array}
$$

After a bad experience with explicit Euler just before,let's try a higher order method and a more elaborate code for this example: DOPRI5 (cf. Volume 1). The numerical solutions obtained for $y _ { 2 }$ with $R t o l = 1 0 ^ { - 2 }$ (209 steps) as well as with $R t o l = 1 0 ^ { - 3 }$ (205 steps） and $A t o l = 1 0 ^ { - 6 }$ : Rtol are displayed in Fig.1.3. Fig.1.4 presents the step sizes used by the code and also the local error estimates. There, all rejected steps are crossed out.

We observe that the solution $y _ { 2 }$ rapidly reaches a quasi-stationary position in the vicinity of $y _ { 2 } ^ { \prime } = 0$ ，which in the beginning $( y _ { 1 } = 1 , y _ { 3 } = 0 )$ is at $0 . 0 4 \approx$ $3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 }$ ,hence $y _ { 2 } \approx 3 . 6 5 \cdot 1 0 ^ { - 5 }$ ， and then very slowly goes back to zero again. The numerical method, however, integrates this smooth solution by thousands of apparently unnecessary steps. Moreover, the chosen step sizes are more or less independent of the chosen tolerance. Hence, they seem to be governed by stability rather than by precision requirements. It can also be seen that an implicit Runge-Kutta code (such as RADAU5 described in Sections IV.5 and IV.8) integrates this equation without any problem.

![](images/179eb916c6e4268de22d8a7a879d70ad54b8e2b574c84d3c8a4f3e14996478d8.jpg)  
Fig.1.3.Numerical solution for problem (1.4) with DOPRI5 and RADAU5

![](images/3c84e187f75a74b3933c539df18becbc972ea161ea81ddd140fc3390a41cb41d.jpg)  
Fig.1.4. Step sizes and local error estimates of DOPRI5, $T o l = 1 0 ^ { - 2 }$

# Electrical Circuits

This behavior is known, at least in part, to any experienced worker in the field. (G. Hall 1985)

One of the simplest nonlinear equations describing a circuit is van der Pol's equation (see Sect.I.16)

$$
\begin{array} { l l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } & { { ~ y _ { 1 } ( 0 ) = 2 } } \\ { { \qquad y _ { 2 } ^ { \prime } = \mu ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } \qquad y _ { 2 } ( 0 ) = 0 . } } \end{array}
$$

We have seen in Chapter $\mathbf { I I }$ that this equation is easily integrated for moderate values of $\mu$ . But we now choose $\mu = 5 0 0$ and suspect that the problem might become diffcult. It turns out that the period of the solution increases with $\mu$ We therefore rescale the solutions and introduce $t = x / \mu , z _ { 1 } ( t ) = y _ { 1 } ( x ) , z _ { 2 } ( t ) =$ $\mu y _ { 2 } ( x )$ . In the resulting equation the factor $\mu ^ { 2 }$ multiplies the entire second line of $f$ . Substituting again $y$ for $z , x$ for $t$ and $\mu ^ { 2 } = 1 / \varepsilon$ we obtain

![](images/779c1627d13137a0cdbd99853768482f5b9d20673573bd9b3d50786610e2a115.jpg)  
Fig.1.5. Numerical solution for DEABM at equation (1.5'), $R t o l = 1 0 ^ { - 2 }$ ， $A t o l = 1 0 ^ { - 7 }$

![](images/3fa6edff3026dd77967a4201f0ca269022ca5f52e4ea26de42e9fae1e74a75bb.jpg)  
Fig.1.6. Step sizes and orders for DEABM, $R t o l = 1 0 ^ { - 2 }$ ， $1 0 ^ { - 6 }$ ， $A t o l = 5 \cdot 1 0 ^ { - 8 }$

$$
\begin{array} { l l l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } & { { \mathrm { ~ o r ~ } } } & { { y _ { 1 } ^ { \prime } = y _ { 2 } } } \\ { { y _ { 2 } ^ { \prime } = \mu ^ { 2 } \big ( ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } \big ) } } & { { } } & { { \varepsilon y _ { 2 } ^ { \prime } = ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } . } } \end{array}
$$

The steady-state approximation (see Vol. I, Formula (I.16.5)) then becomes independent of $\mu$

Why not try a multistep code this time? For example the predictor-corrector Adams code DEABM of Shampine & Watts. Figures 1.5 and 1.6 show the numerical solution, the step sizes and the orders for the first 45O steps. Eventually the code stops with the message $I d i d = - 4$ ("the problem appears to be stiff"). The implicit Runge-Kutta code RADAU5 integrates over the same interval in 11 steps.

# Diffusion

Stalling numerical processes must be wrong. (A“golden rule”of Achi Brandt)

Another source of stiffness is the translation of diffusion terms by divided differences (method of lines, see Sect.I.1) into a large system of ODE's. We choose the Brusselator (see (16.12) of Sect.I.16) in one spatial variable $\boldsymbol { \mathscr { x } }$

$$
\begin{array} { l } { \displaystyle \frac { \partial u } { \partial t } = A + { u ^ { 2 } v } - ( B + 1 ) u + \alpha \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } \\ { \displaystyle \frac { \partial v } { \partial t } = B u - { u ^ { 2 } v } + \alpha \frac { \partial ^ { 2 } v } { \partial x ^ { 2 } } } \end{array}
$$

with $0 \leq x \leq 1 , A = 1 , B = 3 , \alpha = 1 / 5 0$ and boundary conditions

$$
\begin{array} { l l } { { u ( 0 , t ) = u ( 1 , t ) = 1 , } } & { { v ( 0 , t ) = v ( 1 , t ) = 3 , } } \\ { { u ( x , 0 ) = 1 + \sin ( 2 \pi x ) , } } & { { v ( x , 0 ) = 3 . } } \end{array}
$$

We replace the second spatial derivatives by finite differences on a grid of $N$ points $x _ { i } = i / ( N + 1 ) \ ( 1 \leq i \leq N ) , \Delta x = 1 / ( N + 1 )$ and obtain from (1.6)

$$
\begin{array} { r l } & { u _ { \iota } ^ { \prime } = 1 + u _ { \iota } ^ { 2 } v _ { i } - 4 u _ { i } + \displaystyle \frac { \alpha } { ( \Delta x ) ^ { 2 } } ( u _ { i - 1 } - 2 u _ { i } + u _ { \iota + 1 } ) , } \\ & { ~ v _ { i } ^ { \prime } = 3 u _ { \iota } - u _ { i } ^ { 2 } v _ { \iota } + \displaystyle \frac { \alpha } { ( \Delta x ) ^ { 2 } } ( v _ { \iota - 1 } - 2 v _ { i } + v _ { i + 1 } ) , } \\ & { u _ { 0 } ( t ) = u _ { N + 1 } ( t ) = 1 , \quad v _ { 0 } ( t ) = v _ { N + 1 } ( t ) = 3 , } \\ & { u _ { i } ( 0 ) = 1 + \sin ( 2 \pi x _ { \iota } ) , \quad v _ { \iota } ( 0 ) = 3 , \quad i = 1 , \ldots , N . } \end{array}
$$

Table 1.1. Results for (1.6'） with ODEX for $0 \leq t \leq 1 0$   

<table><tr><td>N</td><td>Tol</td><td>accepted steps</td><td>rejected steps</td><td>function calls</td></tr><tr><td>10</td><td>10-4</td><td>21</td><td>3</td><td>365</td></tr><tr><td>20</td><td>10-4</td><td>81</td><td>25</td><td>1138</td></tr><tr><td>30</td><td>10-4</td><td>167</td><td>45</td><td>2459</td></tr><tr><td>40</td><td>10-4</td><td>275</td><td>62</td><td>4316</td></tr><tr><td>40</td><td>10-2</td><td>266</td><td>59</td><td>3810</td></tr></table>

![](images/00d6478b51e868a690dfabc6e4b42bbe183fd281cf5759b2c882f7195b7771ee.jpg)  
Fig. 1.7. Solution $u ( x , t )$ of (1.6） with $N = 4 0$ using ODEX

![](images/eda88a7f7de679c61ece0dd4311e6d83af47d847a99ab0c99e0a9e40ef7e5553.jpg)  
Fig.1.8. Step size and order of ODEX at (1.6') with $N \approx 4 0$

This time we try the extrapolation code ODEX (see Volume I) and integrate over $0 \leq t \leq 1 0$ with $A t o l = R t o l = T o l$ . The number of necessary steps increases curiously with $N$ , as is shown in Table 1.1. Again, for $N$ large, the computing time is nearly independent of the desired tolerance, the computed solutions, however, differ considerably (see Fig.1.7). Even the smooth $1 0 ^ { - 4 }$ -solution shows curious stripes which are evidently unconnected with the behaviour of the solution. Fig.1.8 shows the extremely ragged step size and order changes which take place in this example.

We again have all the characteristics of a “stiff” problem,and the use of an implicit method promises better results. However, when applying such a method, one must carefully take advantage of the banded or sparse structure of the Jacobian matrix. Otherwise the numerical work involved in the linear algebra would increase with $N ^ { 3 }$ , precisely as the work for the explicit method ( $N ^ { 2 }$ for the number of steps and $N$ for the work per step).

# A "Stiff' Beam

Although it is common to talk about “stiff differential equations,” an equation per se is not stiff,a particular initial value problem for that equation may be stiff,in some regions,but the sizes of these regions depend on the initial values and the error tolerance. (C.W. Gear 1982)

Let us conclude our series of examples by a problem from mechanics: the motion of an elastic beam. We suppose the beam inextensible of length 1 and thin. So we neglect shearing forces and rotatory inertia. We further want to allow it arbitrarily large movements. Thus, the most natural coordinate system to use is the angle $\theta$ as a function of arc length $s$ and time $t$ .We further suppose the beam clamped at s=0 andaforce F=(F,F）acting at the free end $s \approx 1$ . The beam is then described by the equations

![](images/2a7e8fb87e8223bd42a8465e1a0fe247d1a2563abce150deb20a289da21ede81.jpg)

(Drawing by K. Wanner)

$$
x ( s , t ) = \int _ { 0 } ^ { s } \cos \theta ( \sigma , t ) d \sigma ,
$$

$$
y ( s , t ) = \int _ { 0 } ^ { s } \sin \theta ( \sigma , t ) d \sigma .
$$

In order to obtain the equations of motion for this problem, we apply Lagrange theory (Lagrange 1788). This requires that we form $L = T - U$ where $T$ is the kinetic and $U$ the potential energy. For the first of these we have simply

$$
T = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \Big ( ( \dot { x } ( s , t ) ) ^ { 2 } + ( \dot { y } ( s , t ) ) ^ { 2 } \Big ) d s .
$$

The potential energy is made up of energy from bending (depending on the curvature) and from exterior forces as follows:

$$
U = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } ( \theta ^ { \prime } ( s , t ) ) ^ { 2 } d s - F _ { x } ( t ) x ( 1 , t ) - F _ { y } ( t ) y ( 1 , t ) .
$$

Here dots and primes denote derivatives with respect to $t$ and $s$ respectively. The equations of motion are now obtained by a “trivial” calculation (we are grateful to our colleague J. Descloux for having shown us how this must be done!） using the Hamilton principle which leads to (see Exercise 2)

$$
\begin{array} { r l r } {  { \int _ { 0 } ^ { 1 } G ( s , \sigma ) \cos \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) \ddot { \theta } ( \sigma , t ) d \sigma } } \\ & { } & { = \theta ^ { \prime \prime } ( s , t ) + \cos \theta ( s , t ) F _ { y } ( t ) - \sin \theta ( s , t ) F _ { x } ( t ) \qquad \quad ( 1 , } \\ & { } & { \quad - \displaystyle \int _ { 0 } ^ { 1 } G ( s , \sigma ) \sin \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) ( \Dot { \theta } ( \sigma , t ) ) ^ { 2 } d \sigma , \quad 0 \le s \le 1 } \end{array}
$$

$$
\theta ( 0 , t ) = 0 , \qquad \theta ^ { \prime } ( 1 , t ) = 0
$$

where

$$
G ( s , \sigma ) = 1 - \operatorname* { m a x } ( s , \sigma )
$$

is Green's function for the problem $- w ^ { \prime \prime } ( s ) = g ( s )$ ， $w ^ { \prime } ( 0 ) = w ( 1 ) = 0$ . If we discretize the integrals with the help of the midpoint rule

$$
\int _ { 0 } ^ { 1 } { f ( \theta ( \sigma , t ) ) d \sigma } = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } f ( \theta _ { k } ) , \qquad \theta _ { k } = \theta \Big ( \big ( k - \frac { 1 } { 2 } \big ) \frac { 1 } { n } , t \Big ) , \qquad k = 1 , \ldots , n - 1 .
$$

Equations (1.10) become

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 1 } ^ { n } a _ { l k } \ddot { \theta } _ { k } = n ^ { 4 } \Big ( \theta _ { l - 1 } - 2 \theta _ { l } + \theta _ { l + 1 } \Big ) + n ^ { 2 } \Big ( \cos \theta _ { l } F _ { y } - \sin \theta _ { l } F _ { x } \Big ) } } \\ { { - \displaystyle \sum _ { k = 1 } ^ { n } g _ { l k } \sin ( \theta _ { l } - \theta _ { k } ) \dot { \theta } _ { k } ^ { 2 } , \qquad l = 1 , \dots , n } } \end{array}
$$

$$
\theta _ { 0 } = - \theta _ { 1 } , \qquad \theta _ { n + 1 } = \theta _ { n }
$$

where

$$
a _ { l k } = g _ { l k } \cos ( \theta _ { l } - \theta _ { k } ) , \qquad g _ { l k } = n + { \frac { 1 } { 2 } } - \operatorname * { m a x } ( l , k ) .
$$

Integration without preparation is frustration.

(Reverend Leon Sullivan)

Numerical integration of (1.10'） seems quite tedious, since the acceleration $\ddot { \theta }$ is only given implicitly. The computation of $\ddot { \theta } _ { k }$ requires the solution of a linear

system $A { \ddot { \theta } } = v$ . Due to the special structure of $A$ , this can be done efficiently, since with $B = \left( b _ { l k } \right) , b _ { l k } = g _ { l k } \sin ( \theta _ { l } - \theta _ { k } )$ , we have

$$
A + i B = \mathrm { d i a g } \Bigl ( e ^ { \imath \theta _ { 1 } } , \ldots , e ^ { \imath \theta _ { n } } \Bigr ) G \mathrm { d i a g } \Bigl ( e ^ { - \imath \theta _ { 1 } } , \ldots , e ^ { - \imath \theta _ { n } } \Bigr ) .
$$

The matrix $G = \left( g _ { l k } \right)$ has the beautiful inverse

$$
G ^ { - 1 } = \left( \begin{array} { c c c c c c } { { 1 } } & { { - 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { - 1 } } & { { 2 } } & { { - 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { 2 } } & { { - 1 } } \\ { { } } & { { } } & { { } } & { { - 1 } } & { { 3 } } \end{array} \right) ,
$$

a positive definite tridiagonal matrix (a natural coincidence: $G ^ { - 1 }$ represents the second order difference operator, and $G$ comes from the Green function for a second order integration problem). Now

$$
( A + i B ) ^ { - 1 } = C + i D = \mathrm { d i a g } \Big ( e ^ { i \theta _ { 1 } } , \ldots , e ^ { \imath \theta _ { n } } \Big ) G ^ { - 1 } \mathrm { d i a g } \Big ( e ^ { - i \theta _ { 1 } } , \ldots , e ^ { - \imath \theta _ { n } } \Big )
$$

and

$$
A C - B D = I , \quad A D + B C = 0
$$

lead to $A ^ { - 1 } = C + D C ^ { - 1 } D$ . We can also simplify the term $- \sum g _ { l k } \sin ( \theta _ { l } -$ $\theta _ { k } ) \dot { \theta } _ { k } ^ { 2 }$ ，which in vector notation is $- B \dot { \theta } ^ { 2 }$ ，with the formula $A ^ { - 1 } B = - D C ^ { - 1 }$ (from (1.17)). The accelerations $\ddot { \theta } _ { k }$ are now obtained from (1.10') as follows.

a)Let $v _ { l } = n ^ { 4 } \big ( \theta _ { l - 1 } - 2 \theta _ { l } + \theta _ { l + 1 } \big ) + n ^ { 2 } \big ( \cos \theta _ { l } F _ { y } - \sin \theta _ { l } F _ { x } \big ) ,$ b) Compute $w = D v + { \dot { \theta } } ^ { 2 }$ （ $D$ is bidiagonal);   
c) Solve the tridiagonal system $C u = w$ ，   
d) Compute $\ddot { \theta } = C v + D u$ .

Thus the evaluation of (1.10') reduces to ${ \mathcal { O } } ( n )$ operations (instead of $\mathcal { O } ( n ^ { 3 } ) )$ .We choose the initial conditions

$$
\theta ( s , 0 ) = 0 , \qquad \dot { \theta } ( s , 0 ) = 0
$$

and apply the exterior forces

$$
F _ { x } = - \varphi ( t ) , \quad F _ { y } = \varphi ( t ) , \qquad \varphi ( t ) = \left\{ { 1 . 5 \cdot \sin ^ { 2 } t } \quad 0 \leq t \leq \pi \right.
$$

The resulting system of ODE's is then integrated for $0 \leq t \leq 5$ by the code DOP853 of Volume I, although strictly speaking, the code is of too high an order for such a problem. The results are summarized in Table 1.2.

We observe the same phenomenon as before, the number of necessary steps increases like $\mathcal { O } ( n ^ { 2 } )$ (the numerical work like $\mathcal { O } ( n ^ { 3 } ) )$ , and is more or less independent of the chosen tolerance. The numerical solution for $n = 4 0$ is displayed in Fig. 1.9. Only each 20th of the nearly 90o0 steps is drawn (otherwise the picture would just be completely black). The computed solution looks perfectly smooth and there is no apparent reason for the need of so many steps. In fact due to lack of stability, the numerical method produces small vibrations which are invisible for $T o l = 1 0 ^ { - 7 }$ ,and which force the integrator to such small step sizes. If we relax the high precision requirement, these oscillations become visible (Fig.1.10).

Table 1.2.Results for the beam (1.10） with DOP853   

<table><tr><td>m</td><td>Tol</td><td>accepted steps</td><td>rejected steps</td><td>function calls</td></tr><tr><td>.5 10 20</td><td>10-7 10-7 10-7</td><td>142 383 1397</td><td>35 26 273</td><td>2091 4884 19769</td></tr><tr><td>40 20 20 20</td><td>10-7 10-3 10-5 10-7</td><td>6913 1486 1967 1397</td><td>1347 450 266 273</td><td>97775 22784 26532 19769</td></tr></table>

# High Oscillations

Let us now choose slightly perturbed initial values in the beam equation (1.10). Instead of (1.18) we put

$$
\theta _ { 1 } = \ldots = \theta _ { n - 1 } = 0 , \theta _ { n } = 0 . 4 , \quad \dot { \theta } _ { 1 } = \ldots = \dot { \theta } _ { n } = 0 .
$$

This time, the correct solution for $n = 1 0$ of（1.10'） computed with $T o l = 1 0 ^ { - 6 }$ and more than 200O steps is displayed in Fig.1.11.

The solution is highly oscillatory, no damping wipes out the fast vibrations since the system is conservative. Hence also an implicit method, if required to follow all these oscillations, would need the same number of steps and there would of course be no advantage in using it. So we see that the decision whether a problem should be regarded as stiff or nonstiff ("... that is the question), may also depend on the chosen initial conditions. On the other hand, we shall see in Sect.IV.2 that whenever these high oscillations are not desired,implicit methods are a marvellous instrument for wiping them out.

# Exercises

1.(Curtiss & Hirschfelder 1952). “It is interesting to notice that this method of integration (the implicit Euler) may be used in either direction”. Integrate equation (1.1) backward with step size $- 0 . 5$ and initial value $y ( 1 . 5 ) = 0$ in three steps. Observe that the numerical solution remains stable and follows the smooth solution.

2. Derive the equations of motion(1.10) for the elastic beam from(1.8) and (1.9).

![](images/6416a5d7910f267093a40a63144e81780c4955fdfb9c151dafab49c1675b8da4.jpg)  
Fig.1.10. DOP853 on the beamwith $T o l = 0 . 0 0 7 5$ ，$n = 2 0$ ， every 5th step drawn.

![](images/7f0b85ca644c9ae00561fdd87e3bcb117896bfba4ae2a329cf452b8c933bc0c3.jpg)  
Fig.1.11. DOP853 on highly oscillatorybeam with $T o l = 0 . 0 0 0 0 0 1$ ，$n = 1 0$ ， every 4th step drawn.

Hint. If you want to avoid differentiation in function spaces, then discretize the beam as, say,

$$
x _ { j } = \Delta s \sum _ { k = 1 } ^ { j } \cos \theta _ { k } , \quad y _ { j } = \Delta s \sum _ { k = 1 } ^ { j } \sin \theta _ { k } , \quad j = 1 , \ldots , n , \Delta s = { \frac { 1 } { n } }
$$

$$
T = \frac { \Delta s } { 2 } \sum _ { \jmath = 1 } ^ { n } \left( \dot { x } _ { \jmath } ^ { 2 } + \dot { y } _ { \jmath } ^ { 2 } \right) = \frac { \Delta s } { 2 } \sum _ { \jmath = 1 } ^ { n } \dot { z } _ { \jmath } \dot { \bar { z } } _ { \jmath } , \qquad z _ { \jmath } = \Delta s \sum _ { k = 1 } ^ { \jmath } e ^ { \imath \theta _ { k } }
$$

$$
U = \frac { \Delta s } { 2 } \sum _ { j = 1 } ^ { n } \Bigl ( \frac { \theta _ { j } - \theta _ { j - 1 } } { \Delta s } \Bigr ) ^ { 2 } - F _ { x } \Delta s \sum _ { k = 1 } ^ { n } \cos \theta _ { k } - F _ { y } \Delta s \sum _ { k = 1 } ^ { n } \sin \theta _ { k } ,
$$

form the Lagrange function $L = T - U$ and apply $n$ -dimensional Lagrange theory (Lagrange (1788)，, Vol. II, Sect. VII and VIII, a very clear derivation can be found in Sommerfeld (1942), Vol. I, $\ S 3 6 )$

$$
{ \frac { d } { d t } } { \Bigl ( } { \frac { \partial L } { \partial { \dot { \theta } } _ { k } } } { \Bigr ) } - { \frac { \partial L } { \partial \theta _ { k } } } = 0
$$

or

$$
\sum _ { l = 1 } ^ { n } L _ { \dot { \theta } _ { k } \dot { \theta } _ { l } } \ddot { \theta } _ { l } = L _ { \theta _ { k } } - L _ { \dot { \theta } _ { k } t } - \sum _ { l = 1 } ^ { n } L _ { \dot { \theta } _ { k } \theta _ { l } } \dot { \theta } _ { l } .
$$

3.Apply an explicit code tothe Oregonator (Chapter I, Equation (16.15))

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = 7 7 . 2 7 \Big ( y _ { 2 } + y _ { 1 } \big ( 1 - 8 . 3 7 5 \times 1 0 ^ { - 6 } y _ { 1 } - y _ { 2 } \big ) \Big ) } \\ { y _ { 2 } ^ { \prime } = \frac { 1 } { 7 7 . 2 7 } ( y _ { 3 } - ( 1 + y _ { 1 } ) y _ { 2 } ) } \\ { y _ { 3 } ^ { \prime } = 0 . 1 6 1 ( y _ { 1 } - y _ { 3 } ) } \end{array}
$$

and study its performance.

4. a) Compute the equations of motion of the hanging rope (Fig.1.12) of length 1 by using the results of Exercise 2. The potential energy has to be replaced by

$$
U = - \int _ { 0 } ^ { 1 } x ( s , t ) d s .
$$

Result.

$$
\begin{array} { l l } { \displaystyle \int _ { 0 } ^ { 1 } G ( s , \sigma ) \cos \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) \ddot { \theta } ( \sigma , t ) d \sigma } & { ( 1 \cdot \frac 1 2 ) } \\ { \displaystyle } & { = - \int _ { 0 } ^ { 1 } G ( s , \sigma ) \sin \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) ( \dot { \theta } ( \sigma , t ) ) ^ { 2 } d \sigma - ( 1 - s ) \sin \theta ( s , t ) } \end{array}
$$

for $0 \leq s \leq 1$ , or, when discretized

$$
\sum _ { k = 1 } ^ { n } a _ { l k } \ddot { \theta } _ { k } = - \sum _ { k = 1 } ^ { n } b _ { l k } \dot { \theta } _ { k } ^ { 2 } - n \left( n + \frac { 1 } { 2 } - l \right) \sin \theta _ { l } .
$$

b) Do numerical computations with DOPRI5 or DOP853. Choose as initial po-sition a hanging rope in equilibrium which is then released at one end.

Hint. The hanging rope in equilibrium satisfies, in the usual coordinates,

$$
\int _ { x _ { 0 } } ^ { x _ { 1 } } { y \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } } } d x = \mathrm { m i n } \qquad \mathrm { w i t h } \qquad \int _ { x _ { 0 } } ^ { x _ { 1 } } { \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } } } d x = 1 ,
$$

which, using a Lagrange multiplier, becomes

$$
\int _ { x _ { 0 } } ^ { x _ { 1 } } ( y - \lambda ) \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } } d x = \mathrm { s t a t } .
$$

Applying (2.6) of Sect.I.2 yields $y - \lambda = K \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } }$ with solution

$$
y = \lambda + K { \mathrm { c o s h } } \Bigl ( { \frac { x + \alpha } { K } } \Bigr ) .
$$

Suitable choices of the parameters and change of coordinates $\ . \ K = 1 / 2 , \ \lambda =$ $- K \mathrm { c o s h } ( \alpha / K ) , x  y , y  - x )$ then lead to

$$
\theta ( s , 0 ) = \pi / 2 - \arctan ( \sinh ( 2 \alpha ) - 2 s ) .
$$

Result. DOP853 has computed the solution for $0 \leq t \leq 5$ ， $n = 6 0$ and $T o l =$ $1 0 ^ { - 5 }$ ， $\alpha = 0 . 6$ , in 203 steps (Fig.1.12). The number of steps increases here like $\mathcal { O } ( n )$ , so the rope is - evidently -- less stiff than the beam.

![](images/dfff1393fd4453400d84609edde6c638c97cbcc5c2fc6dec9a4bce70e60b2a7f.jpg)  
Fig.1.12. Movement of hanging rope, every step drawn

# IV.2Stability Analysis for Explicit RK Methods

... werden wir bei dem Anfangswertproblem hyperbolischer Gleichungen erkennen, dass die Konvergenz allgemein nur dann vorhanden ist, wenn die Verhältnisse der Gittermaschen in verschiedenen Richtungen gewissen Ungleichungen genuigen.

(Courant, Friedrichs & Lewy 1928)

The first analysis of instability phenomena and step size restrictions for hyperbolic equations was made in the famous paper of Courant, Friedrichs & Lewy (1928). Later,many authors undertook a stability analysis,very often independently,in order to explain the phenomena encountered in the foregoing section. An early and beautiful paper on this subject is Guillou & Lago (1961).

# Stability Analysis for Euler's Method

Let $\varphi ( x )$ be a smooth solution of $y ^ { \prime } = f ( x , y )$ . We linearize $f$ in its neighbourhood as follows

$$
y ^ { \prime } ( x ) = f { \bigl ( } x , \varphi ( x ) { \bigr ) } + { \frac { \partial f } { \partial y } } { \bigl ( } x , \varphi ( x ) { \bigr ) } { \bigl ( } y ( x ) - \varphi ( x ) { \bigr ) } + \ldots
$$

and introduce $y ( x ) - \varphi ( x ) = { \overline { { y } } } ( x )$ to obtain

$$
{ \overline { { y } } } ^ { \prime } ( x ) = { \frac { \partial f } { \partial y } } { \big ( } x , \varphi ( x ) { \big ) } \cdot { \overline { { y } } } ( x ) + \ldots = J ( x ) { \overline { { y } } } ( x ) + \ldots .
$$

As a first approximation we consider the Jacobian $J ( x )$ as constant and neglect the error terms. Omitting the bars we arrive at

$$
y ^ { \prime } = J y .
$$

If we now apply, say, Euler's method to (2.2'), we obtain

$$
y _ { m + 1 } = R ( h J ) y _ { m }
$$

with

$$
R ( z ) = 1 + z .
$$

The behaviour of (2.3) is studied by transforming $J$ to Jordan canonical form (see Sect.I.12). We suppose that $J$ is diagonalizable with eigenvectors $v _ { 1 } , \ldots , v _ { n }$ and write $y _ { 0 }$ in this basis as

$$
y _ { 0 } = \sum _ { i = 1 } ^ { n } \alpha _ { i } v _ { i } .
$$

Inserting this into (2.3) we obtain

$$
y _ { m } = \sum _ { i = 1 } ^ { n } \bigl ( R ( h \lambda _ { i } ) \bigr ) ^ { m } \alpha _ { \iota } \cdot v _ { i } ,
$$

where the $\lambda _ { i }$ are the corresponding eigenvalues (see also Exercises 1 and 2). Clearly $y _ { m }$ remains bounded for $m  \infty$ , if for all eigenvalues the complex number $z = h \lambda _ { i }$ lies in the set

$$
S = \left\{ z \in \mathbb { C } ; | R ( z ) | \leq 1 \right\} = \left\{ z \in \mathbb { C } ; | z - ( - 1 ) | \leq 1 \right\}
$$

which is the circle of radius 1 and centre $- 1$ . This leads to the explanation of the results encountered in Example (1.1). There we have $\lambda = - 5 0$ ,and $h \lambda \in S$ means that $0 \leq h \leq 2 / 5 0$ , in perfect accordance with the numerical observations.

# Explicit Runge-Kutta Methods

An explicit Runge-Kutta method (Sect.II.2, Formula (2.3)) applied to (2.2'） gives

$$
\begin{array} { r } { g _ { \imath } = y _ { m } + h J \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { \imath j } g _ { j } } \\ { y _ { m + 1 } = y _ { m } + h J \displaystyle \sum _ { j = 1 } ^ { s } b _ { \jmath } g _ { \jmath } \ : . } \end{array}
$$

Inserting ${ \mathit { g } } _ { \mathit { j } }$ repeatedly from the first line,this becomes

$$
y _ { m + 1 } = R ( h J ) y _ { m }
$$

where

$$
R ( z ) = 1 + z \sum _ { j } b _ { j } + z ^ { 2 } \sum _ { j , k } b _ { j } a _ { j k } + z ^ { 3 } \sum _ { j , k , l } b _ { j } a _ { j k } a _ { k l } + . . .
$$

is a polynomial of degree $\leq s$ ·

Definition 2.1. The function $R ( z )$ is called the stability function of the method. It can be interpreted as the numerical solution after one step for

$$
y ^ { \prime } = \lambda y , \qquad y _ { 0 } = 1 , \qquad z = h \lambda ,
$$

the famous Dahlquist test equation. The set

$$
S = \left\{ z \in \mathbb { C } \mathrm { ~ } ; \left| R ( z ) \right| \leq 1 \right\}
$$

is called the stability domain of the method.

Theorem 2.2. If the Runge-Kutta method is of order $p$ ,then

$$
R ( z ) = 1 + z + \frac { z ^ { 2 } } { 2 ! } + \ldots + \frac { z ^ { p } } { p ! } + \mathcal { O } ( z ^ { p + 1 } ) .
$$

Proof. The exact solution of (2.9) is $e ^ { z }$ and therefore the numerical solution $y _ { 1 } =$ $R ( z )$ must satisfy

$$
e ^ { z } - R ( z ) = \mathcal { O } ( h ^ { p + 1 } ) = \mathcal { O } ( z ^ { p + 1 } ) .
$$

Another argument is that the expressions in (2.8) appear in the order conditions for the“tall” tres $\tau , t _ { 2 1 } , t _ { 3 2 } , t _ { 4 4 } , t _ { 5 9 } , \ldots .$ (see Table 2.2 of Sect.I1.2,p.148). They are therefore equal to $1 / q !$ for $q \leq p$ □

![](images/68f82621a7c9622f9e31b2de6b8d05e5fc971de840db8f41c4e50071fb1b4505.jpg)  
Fig.2.1. Stability domains for explicit Runge-Kutta methods of order ${ \mathfrak { p } } = s$

![](images/773a2a6d253c9f21f9d2c990945ffc8a31d122f556604c422c7782f266d46c56.jpg)  
Fig.2.2. Stability domains for DOPRI methods

As a consequence, all explicit Runge-Kutta methods with $p = s$ possess the stability function

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 ! } } + . . . + { \frac { z ^ { s } } { s ! } } .
$$

The corresponding stability domains are represented in Fig.2.1.

The method of Dormand & Prince DOPRI5 (Sect.II.5, Table 5.2) is of order 5 with $s = 6$ (the 7th stage is for error estimation only). Here $R ( z )$ is obtained by direct computation. The result is

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + { \frac { z ^ { 3 } } { 6 } } + { \frac { z ^ { 4 } } { 2 4 } } + { \frac { z ^ { 5 } } { 1 2 0 } } + { \frac { z ^ { 6 } } { 6 0 0 } } .
$$

For DOP853 (Sect.II.5,Fig.5.3), $R ( z )$ becomes

$$
\begin{array} { c } { { R ( z ) = \displaystyle { \sum _ { j = 0 } ^ { 8 } \frac { z ^ { \prime } } { j ! } } + 2 . 6 9 1 6 9 2 2 0 0 1 6 9 1 \cdot 1 0 ^ { - 6 } z ^ { 9 } + 2 . 3 4 1 3 4 5 1 0 8 2 0 9 8 \cdot 1 0 ^ { - 7 } z ^ { 1 0 } } } \\ { { + 1 . 4 9 4 7 3 6 4 8 5 4 5 9 2 \cdot 1 0 ^ { - 8 } z ^ { 1 1 } + 3 . 6 1 3 3 2 4 5 7 8 1 2 8 2 \cdot 1 0 ^ { - 1 0 } z ^ { 1 2 } } } \end{array}
$$

The stability domains for these two methods are given in Fig. 2.2.

# Extrapolation Methods

The GBS-algorithm (see Sect.I1.9, Formulas (9.10), (9.13)) applied to $y ^ { \prime } = \lambda y$ ， $y ( 0 ) = 1$ leads with $z = H \lambda$ to

$$
\begin{array} { r l } & { \quad y _ { 0 } = 1 , \quad \quad y _ { 1 } = 1 + \frac { z } { n _ { _ { J } } } } \\ & { } \\ & { \quad y _ { i + 1 } = y _ { i - 1 } + 2 \frac { z } { n _ { _ { J } } } y _ { \imath } \qquad i = 1 , 2 , \ldots , n _ { j } } \\ & { } \\ & { \quad { \cal T } _ { \jmath ^ { \mathrm { I } } } = \frac { 1 } { 4 } ( y _ { n _ { \jmath } - 1 } + 2 y _ { n _ { \jmath } } + y _ { n _ { \jmath } + 1 } ) } \\ & { } \\ & { { \cal T } _ { j , k + 1 } = { \cal T } _ { \jmath , k } + \frac { { \cal T } _ { j , k } - { \cal T } _ { \jmath - 1 , k } } { ( n _ { j } / n _ { j - k } ) ^ { 2 } - 1 } . } \end{array}
$$

The stability domains for the diagonal terms $T _ { 2 2 } , T _ { 3 3 } , T _ { 4 4 }$ , and $T _ { 5 5 }$ for the harmonic sequence

$$
\{ n _ { \jmath } \} = \{ 2 , 4 , 6 , 8 , 1 0 , . . . \}
$$

(the one which is used in ODEX) are displayed in Fig.2.3. We have also added those for the methods without the smoothing step (II.9.13c),which shows some difference for negative real eigenvalues.

# Analysis of the Examples of IV.1

The Jacobian for the Robertson reaction (1.3) is given by

$$
\left( \begin{array} { c c c } { { - 0 . 0 4 } } & { { 1 0 ^ { 4 } y _ { 3 } } } & { { 1 0 ^ { 4 } y _ { 2 } } } \\ { { 0 . 0 4 } } & { { - 1 0 ^ { 4 } y _ { 3 } - 6 \cdot 1 0 ^ { 7 } y _ { 2 } } } & { { - 1 0 ^ { 4 } y _ { 2 } } } \\ { { 0 } } & { { 6 \cdot 1 0 ^ { 7 } y _ { 2 } } } & { { 0 } } \end{array} \right)
$$

which in the neighbourhood of the equilibrium $y _ { 1 } = 1$ ， $y _ { 2 } = 0 . 0 0 0 0 3 6 5$ ， $y _ { 3 } = 0$ is

$$
\left( \begin{array} { c c c } { { - 0 . 0 4 } } & { { 0 } } & { { 0 . 3 6 5 } } \\ { { 0 . 0 4 } } & { { - 2 1 9 0 } } & { { - 0 . 3 6 5 } } \\ { { 0 } } & { { 2 1 9 0 } } & { { 0 } } \end{array} \right)
$$

with eigenvalues

![](images/ce2aa538e99391fe27daadcf4fbc118953c29ddbd0e3b130e69e4c36d754dbc6.jpg)  
Fig. 2.3. Stability domains for GBS extrapolation methods

$$
\lambda _ { 1 } = 0 , \quad \lambda _ { 2 } = - 0 . 4 0 5 , \quad \lambda _ { 3 } = - 2 1 8 9 . 6 .
$$

The third one produces stiffness. For stability we need (see the stability domain of DOPRI5 in Fig. 2.2) $- 2 1 9 0 h \ge - 3 . 3$ , hence $h \leq 0 . 0 0 1 5$ . This again confirms the numerical observations.

The Jacobian of example (1.6') (Brusselator reaction with diffusion) is a large $2 N \times 2 N$ matrix. It is composed of reaction terms and diffusion terms:

$$
J = \left( \begin{array} { c c } { \mathrm { d i a g } ( 2 u _ { i } v _ { \ i } - 4 ) } & { \mathrm { ~ } \mathrm { d i a g } ( u _ { i } ^ { 2 } ) } \\ { \mathrm { d i a g } ( 3 - 2 u _ { i } v _ { i } ) } & { \mathrm { ~ } \mathrm { d i a g } ( - u _ { i } ^ { 2 } ) } \end{array} \right) + \frac { \alpha } { ( \Delta x ) ^ { 2 } } \left( \begin{array} { c c } { K } & { 0 } \\ { 0 } & { K } \end{array} \right)
$$

where

$$
K = \left( \begin{array} { c c c c c c } { { - 2 } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { - 2 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { 1 } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { - 2 } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - 2 } } \end{array} \right) \ .
$$

The eigenvalues of $\kappa$ are known (see Sect.I.6,Formula (6.7b)), namely

$$
\mu _ { k } = - 4 { \left( \sin { \frac { \pi k } { 2 N + 2 } } \right) } ^ { 2 } ,
$$

and therefore the double eigenvalues of the right hand matrix in (2.16) are

$$
- \frac { 4 \alpha } { ( \Delta x ) ^ { 2 } } \Big ( \sin \frac { \pi k } { 2 N + 2 } \Big ) ^ { 2 } = - 4 \alpha \big ( N + 1 \big ) ^ { 2 } \Big ( \sin \frac { \pi k } { 2 N + 2 } \Big ) ^ { 2 } ,
$$

and are located between $- 4 \alpha ( N + 1 ) ^ { 2 }$ and O. Since this matrix is symmetric, its eigenvalues are wel conditioned and the first matrix on the right side of (2.16) with much smaller coefficients can be regarded as a small perturbation. Therefore the eigenvalues of $J$ in (2.16) will remain close to those of the unperturbed matrix and lie in a stripe neighbouring the interval $[ - 4 \alpha ( N + 1 ) ^ { 2 } , 0 ]$ . Numerical computations for $N = 4 0$ show for example that the largest negative eigenvalue of $J$ varies between $- 1 3 3 . 3$ and -134.9,while the unperturbed value is $- 4 \cdot 4 1 ^ { 2 } \cdot \sin ^ { 2 } ( 4 0 \pi / 8 2 ) / 5 0 = - 1 3 4 . 2 8$ ． Since most stability domains for ODEX end close to $- 5 . 5$ on the real axis (Fig.2.3), this leads for $N = 4 0$ to $h \leq 0 . 0 4$ and the number of steps must be $\geq 2 5 0$ (compare with Table 1.1).

In order to explain the behaviour of the beam equation, we linearize it in the neighbourhood of the solution ${ \theta } _ { k } = \dot { \theta } _ { k } = 0 , F _ { x } = \dot { F _ { y } } = 0$ . There (1.10') becomes

$$
G \ddot { \theta } = n ^ { 4 } \left( \begin{array} { c c c c c c } { { - 3 } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { - 2 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { 1 } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { - 2 } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - 1 } } \end{array} \right) \theta ,
$$

since for $\theta = 0$ we have $A = G$ and $B = 0$ . We now insert $G ^ { - 1 }$ from (1.16) and observe that the matrices involved are, with the exception of two elements, equal to $\pm K$ of (2.17). We therefore approximate (2.20) by

$$
\ddot { \theta } = - n ^ { 4 } K ^ { 2 } \theta .
$$

This second order equation was integrated in IV.1 as a first order system

$$
\left( \begin{array} { c } { \theta } \\ { \dot { \theta } } \end{array} \right) ^ { \cdot } = \left( \begin{array} { c c } { 0 } & { I } \\ { - n ^ { 4 } K ^ { 2 } } & { 0 } \end{array} \right) \left( \begin{array} { c } { \theta } \\ { \dot { \theta } } \end{array} \right) = E \left( \begin{array} { c } { \theta } \\ { \dot { \theta } } \end{array} \right) .
$$

By solving

$$
\left( \begin{array} { c c } { { 0 } } & { { I } } \\ { { - n ^ { 4 } K ^ { 2 } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { y } } \\ { { z } } \end{array} \right) = \lambda \left( \begin{array} { l } { { y } } \\ { { z } } \end{array} \right) ,
$$

we find that $\lambda$ is an eigenvalue of $E$ iff $\lambda ^ { 2 }$ is an eigenvalue of $- n ^ { 4 } K ^ { \tilde { 2 } 2 }$ .Thus Formula (2.18) shows that the eigenvalues of $E$ are situated on the imaginary axis between $- 4 n ^ { 2 } i$ and $+ 4 n ^ { 2 } i$ . We see from Fig.2.2 that the stability domain of DOP853 covers the imaginary axis between approximately $- 6 i$ and $+ 6 i$ . Hence for stability we need $h \leq 1 . 5 / n ^ { 2 }$ and the number of steps for the interval $0 \leq$ $t \leq 5$ must be larger than $\approx 1 0 n ^ { 2 } / 3$ . This,again,was observed in the numerical calculations (Table 1.2).

# Automatic Stiffness Detection

Neither is perfect, but even an imperfect test can be quite useful, as we can show from experience ... (L.F. Shampine 1977)

Explicit codes applied to stiff problems are apparently not very efficient and the remaining part of the book will be devoted to the construction of more stable algorithms. In order to avoid that an explicit code waste too much effort when encountering stiffness (and to enable a switch to a more suitable method), it is important that the code be equipped with a cheap means of detecting stiffness. The analysis of the preceding subsection demonstrates that, whenever a nonstiff code encounters stiffness, the product of the step size with the dominant eigenvalue of the Jacobian lies near the border of the stability domain. We shall show two manners of exploiting this observation to detect stiffness.

Firstly,we adapt the ideas of Shampine & Hiebert (1977) to the Dormand & Prince method of order 5(4), given in Table I.5.2. The method possesses an error estimator $e r r _ { 1 } = y _ { 1 } - \widehat { y } _ { 1 }$ which, in the nonstiff situation, is $\mathcal { O } ( h ^ { 5 } )$ . However in the stiff case,when the method is working near the border of the stability domain $S$ , the distance $d _ { 1 } = y _ { 1 } - y ( x _ { 0 } + h )$ to the smooth solution is approximately $d _ { \mathbf { \scriptscriptstyle 1 } } \approx R ( h J ) d _ { 0 }$ ,where $J$ denotes the Jacobian of the system, $R ( z )$ is the stability function of the method, and $d _ { 0 } = y _ { 0 } - y ( x _ { 0 } )$ . Here we have neglected the local error for an initial value on the smooth solution $y ( x )$ ．A similar formula, with $R$ replaced by $\widehat { R }$ , holds for the embedded method. The error estimator satisfies $e r r _ { 1 } \approx E ( h J ) d _ { 0 }$ with $E ( z ) = R ( z ) - \widehat { R } ( z )$ . The idea is now to search for a second error estimator $\widetilde { e r r } _ { 1 }$ (with $\widetilde { e r r } _ { 1 } \approx \widetilde { E } ( h J ) d _ { 0 } )$ such that

i) $| \widetilde { E } ( z ) | \leq \theta | E ( z ) |$ on $\partial S \cap \mathbb { C } ^ { - }$ with a small $\theta < 1$ ； ii) $\widetilde { e r r } _ { 1 } = \mathcal { O } ( h ^ { 2 } )$ for $h  0$ ·

Condition (i) implies that $\| \widetilde { e r r } _ { 1 } \| < \| e r r _ { 1 } \|$ when $h \lambda$ is near $\partial S$ (the problem is possibly stiff),and condition (ii) will lead to $\| \widetilde { e r r } _ { 1 } \| \gg \| e r r _ { 1 } \|$ for step sizes which are determined by accuracy requirements (when the problem is not stiff). If $\| \widetilde { e r r } _ { 1 } \| < \| e r r _ { 1 } \|$ occurs several times in succession (say 15 times) then a stiff code might be more efficient.

For the construction of $\widetilde { e r r } _ { 1 }$ we put $\widetilde { e r r } _ { 1 } = h ( d _ { 1 } k _ { 1 } + d _ { 2 } k _ { 2 } + . . . + d _ { s } k _ { s } )$ , where the $k _ { i } = f ( x _ { 0 } + c _ { \ i } h , g _ { i } )$ are the available function values of the method. The coefficients $d _ { \imath }$ are determined in such a way that

$$
\sum _ { i = 1 } ^ { s } d _ { i } = 0 , \qquad \sum _ { i = 1 } ^ { s } d _ { i } c _ { i } = 0 . 0 2
$$

(so that (ii) holds) and that $\theta$ in (i) is minimized.A computer search gave values which have been rounded to

$$
\begin{array} { r l } & { d _ { 1 } = - 0 . 0 8 5 3 6 , \quad d _ { 2 } = 0 . 0 8 8 , \quad d _ { 3 } = - 0 . 0 0 9 6 , } \\ & { d _ { 4 } = 0 . 0 0 5 2 , \quad d _ { 5 } = 0 . 0 0 5 7 6 , \quad d _ { 6 } = - 0 . 0 0 4 . } \end{array}
$$

The factor O.02 in (2.24) has been chosen such that $\theta$ in (i) is close to 0.3 on large parts of the border of $S$ ,but $\vert \widetilde { E } ( z ) / E ( z ) \vert$ soon becomes larger than 1 if $z$ approaches the origin.

In Fig. 2.4 we present the contour lines $| \widetilde { E } ( z ) / E ( z ) | = C o n s t \ : ( C o n s t = 4 , 2 , 1$ ， 0.5,0.3, 0.2,0.14,0.1) together with the stability domain of the method. A numerical experiment is illustrated in Fig.2.5. We applied the code DOPRI5 (see the Appendix to Volume I) to the van der Pol equation (1.5') with $\varepsilon = 0 . 0 0 3$ . The upper picture shows the first component of the solution, the second picture displays the quotient $\| \widetilde { e r r } _ { 1 } \| / \| e r r _ { 1 } \|$ for the three tolerances $T o l = 1 0 ^ { - 3 }$ ， $1 0 ^ { - 5 } , 1 0 ^ { - 7 }$ . The last picture is a plot of $h | \lambda | / 3 . 3$ where $h$ is the current step size and $\lambda$ the dominant eigenvalue of the Jacobian and 3.3 is the approximate distance of $\partial S$ to the origin.

![](images/6bbb4dc1df9d7cae18242618340b484e83ab40712d0fca1e30780abf1e8fecce.jpg)

A second possibility for detecting stiffness is to estimate directly the dominant eigenvalue of the Jacobian of the problem. If $v$ denotes an approximation to the corresponding eigenvector with $\{ \{ v \} \}$ sufficiently small then, by the mean value theorem,

$$
| \lambda | \approx { \frac { \| f ( x , y + v ) - f ( x , y ) \| } { \| v \| } }
$$

will be a good approximation to the leading eigenvalue. For the Dormand & Prince method (Table II.5.2) we have $c _ { 6 } = c _ { 7 } = 1$ . Therefore, a natural choice is

$$
\varrho = \frac { \| k _ { 7 } - k _ { 6 } \| } { \| g _ { 7 } - g _ { 6 } \| }
$$

where $k _ { i } = f ( x _ { 0 } + c _ { i } h , g _ { i } )$ are the function values of the current step. Both values, $g _ { 7 } = y _ { 1 }$ and $g _ { 6 }$ , approximate the exact solution $y ( x _ { 0 } + h )$ and it can be shown by Taylor expansion that $g _ { 7 } - g _ { 6 } = \mathcal { O } ( h ^ { 3 } )$ . This difference is thus sufficiently small, in general. The same argument also shows that $g _ { 7 } - g _ { 6 } = \widetilde { E } ( h J ) d _ { 0 }$ ，where $J$ is the Jacobian of the linearized differential equation and $\tilde { E } ( z )$ is a polynomial with subdegree 4. Hence, $g _ { 7 } - g _ { 6 }$ is essentially the vector obtained by 4 iterations of the power method applied to the matrix $h J$ . It will be a good approximation to the eigenvector corresponding to the leading eigenvalue. As in the above numerical experiment we applied the code DOPRI5 to the van der Pol equation (1.5'） with $\varepsilon = 0 . 0 0 3$ . Fig. 2.6 presents a plot of $h \varrho / 3 . 3$ where $h$ is the current step size and $\varrho$ the estimate (2.26). This is in perfect agreement with the exact values $h | \lambda | / 3 . 3$ (see third picture of Fig. 2.5).

![](images/e145daf6d476499eb7d7f6b75169547b6dbac0d2e82aeffdce2d14a137297be9.jpg)  
Fig. 2.5. Stiffness detection with DOPRI5

![](images/74a3ef128c2ada547c01b14f908378f4bffe46f4570da001b2b60052d43c566a.jpg)  
Fig. 2.6. Estimation of Lipschitz constant with DOPRI5

Further numerical examples have shown that the estimate (2.26) also gives satisfactory approximations of $| \lambda |$ when the dominant eigenvalue $\lambda$ is complex. However, if the argument of $\lambda$ is needed too, one can extend the power method as proposed by Wilkinson (1965, page 579). This has been elaborated by Sottas (1984) and Robertson (1987).

The two techniques above allow us to detect the regions where the step size is restricted by stability. In order to decide whether a stiff integrator will be more efficient,one has to compare the expense of both methods. Studies on this question have been undertaken in Petzold (1983), Sottas (1984) and Butcher (1990).

# Step-Control Stability

We now come to the explanation of another phenomenon encountered in Sect. IV.1, that of the ragged behaviour of the step size (e.g. Fig.1.4 or 1.8),a research initiated by G.Hall (1985/86) and continued by G. Hall & D.J. Higham (1988). Do there exist methods or stiff equations for which the step sizes $h _ { n }$ behave smoothly and no frequent step rejections appear?

We make a numerical study on the equation

$$
\begin{array} { r l r } & { \boldsymbol { y } _ { 1 } ^ { \prime } = - 2 0 0 0 \left( \quad \cos x \cdot \boldsymbol { y } _ { 1 } + \sin x \cdot \boldsymbol { y } _ { 2 } + 1 \right) \quad } & { \boldsymbol { y } _ { 1 } ( 0 ) = 1 } \\ & { \boldsymbol { y } _ { 2 } ^ { \prime } = - 2 0 0 0 \left( - \sin x \cdot \boldsymbol { y } _ { 1 } + \cos x \cdot \boldsymbol { y } _ { 2 } + 1 \right) \quad } & { \boldsymbol { y } _ { 2 } ( 0 ) = 0 } \end{array}
$$

for $0 \leq x \leq 1 . 5 7$ ，whose eigenvalues move slowly on a large circle from $- 2 0 0 0$ to $\pm 2 0 0 0 i$ . If we apply Fehlberg's method RKF5(4) (Table II.5.1) in local extrapolation mode (i.e.，we continue the integration with the higher order result） and DOPRI5 to this equation (with Euclidean error norm without scaling),we obtain the step size behaviour presented in Fig.2.7. There all rejected steps are crossed out (3 rejected steps for RKF5(4) and 104 for DOPRI5.

In order to explain this behaviour,we consider for $y ^ { \prime } = \lambda y$ (of course!） the numerical process

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } = R ( h _ { n } \lambda ) y _ { n } } } \\ { { \displaystyle e r r _ { n } = E ( h _ { n } \lambda ) y _ { n } } } \\ { { \displaystyle h _ { n + 1 } = h _ { n } \cdot \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { \alpha } } } \end{array}
$$

(where $e r r _ { n }$ is the estimated error, $E ( z ) = \widehat { R } ( z ) - R ( z )$ ， $\alpha = 1 / ( \widehat { p } + 1 )$ and $\widehat { p }$ is the order of $\widehat { R }$ ) as a dynamical system whose fixed points and stability we have to study. A possible safety factor ("fac” of formula (4.13) of Sect.II.4) can easily be incorporated into $T o l$ and does not affect the theory. The analysis simplifies if we introduce logarithms

$$
\eta _ { n } = \log | y _ { n } | , \qquad \chi _ { n } = \log h _ { n }
$$

so that (2.28) becomes

$$
\begin{array} { r l } & { \eta _ { n + 1 } = \log | R ( e ^ { \chi _ { n } } \lambda ) | + \eta _ { n } , } \\ & { \chi _ { n + 1 } = \alpha \Big ( \gamma - \log | E ( e ^ { \chi _ { n } } \lambda ) | - \eta _ { n } \Big ) + \chi _ { n } , } \end{array}
$$

where $\gamma$ is a constant. This is now a map $\mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ . Its fixed point $( \eta , \chi )$ satisfies

$$
| R ( e ^ { \chi } \lambda ) | = 1 ,
$$

![](images/204cb60bb5e9a21b0c6cc9691323b02416b8cf43902e34ed977f442f07518f4d.jpg)  
Fig. 2.7. Step sizes of RKF5(4) and DOPRI5 for (2.27)

which determines the step size $e ^ { x }$ so that the point $z = e ^ { x } \lambda$ must be on the border of the stability domain. Further

$$
\eta = \gamma - \log | E ( z ) |
$$

determines $\eta$ . Now the Jacobian of the map (2.30) at this fixed point becomes

$$
C = \frac { \partial ( \eta _ { n + 1 } , \chi _ { n + 1 } ) } { \partial ( \eta _ { n } , \chi _ { n } ) } = \left( \begin{array} { c c } { { 1 } } & { { u = \mathrm { R e } \left( \displaystyle \frac { R ^ { \prime } ( z ) } { R ( z ) } \cdot z \right) } } \\ { { - \alpha } } & { { 1 - \alpha v } } \end{array} \right) \qquad \begin{array} { l } { { u = \mathrm { R e } \left( \displaystyle \frac { R ^ { \prime } ( z ) } { R ( z ) } \cdot z \right) } } \\ { { v = \mathrm { R e } \left( \displaystyle \frac { E ^ { \prime } ( z ) } { E ( z ) } \cdot z \right) . } } \end{array}
$$

Proposition 2.3. The step-control mechanism is stable for $h \lambda = z$ on the boundary of the stability domain if and only if the spectral radius of $C$ in (2.32) satisfies

$$
\varrho ( C ) < 1 .
$$

We then call the method $S C$ -stable at $z$

The matrix $C$ is independent of the given differential equation and of the given tolerance. It is therefore a characteristic of the numerical method and the boundary of its stability domain. Let us study some methods of Sect.II.5. a) RKF4(5) (Table 5.1), $\alpha = 1 / 5$ ：

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + { \frac { z ^ { 3 } } { 6 } } + { \frac { z ^ { 4 } } { 2 4 } } + { \frac { z ^ { 5 } } { 1 0 4 } } , \quad E ( z ) = { \frac { z ^ { 5 } } { 7 8 0 } } - { \frac { z ^ { 6 } } { 2 0 8 0 } } .
$$

![](images/54553e8f38e90df7af204125a4f4ebcc0ab204b5435c8a8dd7774f87ed6cbee6.jpg)  
Fig. 2.8. Regions of step-control stability

b) DOPRI5 (Table 5.2), $\alpha = 1 / 5$ ：

$$
R ( z ) = \sec ( 2 . 1 3 ) , ~ E ( z ) = { \frac { 9 7 } { 1 2 0 0 0 0 } } z ^ { 5 } - { \frac { 1 3 } { 4 0 0 0 0 } } z ^ { 6 } + { \frac { 1 } { 2 4 0 0 0 } } z ^ { 7 }
$$

c) RKF5(4) (Table 5.1, with local extrapolation), $\alpha = 1 / 5$ ：

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + { \frac { z ^ { 3 } } { 6 } } + { \frac { z ^ { 4 } } { 2 4 } } + { \frac { z ^ { 5 } } { 1 2 0 } } + { \frac { z ^ { 6 } } { 2 0 8 0 } }
$$

d) HIHA5 (Method of Higham & Hall,see Table 2.1 below), $\alpha = 1 / 5$ ：

$$
\begin{array} { l } { { \displaystyle R ( z ) = 1 + z + \frac { z ^ { 2 } } { 2 } + \frac { z ^ { 3 } } { 6 } + \frac { z ^ { 4 } } { 2 4 } + \frac { z ^ { 5 } } { 1 2 0 } + \frac { z ^ { 6 } } { 1 4 4 0 } \ : , } } \\ { { \displaystyle E ( z ) = - \frac { 1 } { 1 2 0 0 } z ^ { 5 } + \frac { 1 } { 2 4 0 0 } z ^ { 6 } + \frac { 1 } { 1 4 4 0 0 } z ^ { 7 } } } \end{array}
$$

The corresponding stability domains are represented in Fig.2.8. There, the regions of the boundary, for which $\varrho ( C ) < 1$ is satisfied,are represented as thick lines. It can be observed that the phenomena of Fig.2.7,as well as those of Sect. IV.1, are nicely verified.

DOP853. The step size control of the code DOP853 (Volume I) is slightly more complicated. It is based on a “stretched” error estimator (see Sect.II.1O) and, for the test equation $y ^ { \prime } = \lambda y$ , it is equivalent to replacing $| E ( z ) |$ of (2.30) by

$$
| E ( z ) | = \frac { | E _ { 5 } ( z ) | ^ { 2 } } { \sqrt { | E _ { 5 } ( z ) | ^ { 2 } + 0 . 0 1 \cdot | E _ { 3 } ( z ) | ^ { 2 } } } ,
$$

where $E _ { 3 } ( z ) = \widehat { R } _ { 3 } ( z ) - R ( z ) , E _ { 5 } ( z ) = \widehat { R } _ { 5 } ( z ) - R ( z )$ ,and $\widehat { R } _ { 3 } ( z ) , \widehat { R } _ { 5 } ( z )$ are the stability functions of third and fifth order embedded methods, respectively. The above analysis is still valid if the expression $v$ of (2.32) is replaced by the derivative

<table><tr><td>0</td><td colspan="6"></td></tr><tr><td>2-91-3１-23-5</td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1-8</td><td>0</td><td>38</td><td></td><td></td><td></td></tr><tr><td></td><td>91</td><td>27</td><td>78</td><td>8</td><td></td><td></td></tr><tr><td></td><td>500</td><td>100</td><td>125</td><td>125</td><td></td><td></td></tr><tr><td>1</td><td>11 1</td><td>27</td><td>1</td><td>36</td><td>5</td><td></td></tr><tr><td></td><td>20</td><td>20</td><td></td><td></td><td>125</td><td></td></tr><tr><td>1</td><td>12</td><td>0</td><td>2</td><td>4</td><td>96</td><td>48</td></tr><tr><td></td><td></td><td></td><td>27</td><td></td><td>125</td><td></td><td></td></tr><tr><td>y1</td><td>R</td><td>0</td><td>32</td><td>43</td><td>96</td><td>5-481-24</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td>1</td></tr><tr><td>?</td><td></td><td>0</td><td>2</td><td>15</td><td>2</td><td></td><td>10</td></tr></table>

of $\log | E ( e \boldsymbol { x } \lambda ) |$ with respect to $\chi$ , which is

$$
v = 2 v _ { 5 } - \frac { v _ { 5 } | E _ { 5 } ( z ) | ^ { 2 } + 0 . 0 1 v _ { 3 } | E _ { 3 } ( z ) | ^ { 2 } } { | E _ { 5 } ( z ) | ^ { 2 } + 0 . 0 1 | E _ { 3 } ( z ) | ^ { 2 } } ,
$$

where $v _ { 5 } = \mathrm { R e } \left( z E _ { 5 } ^ { \prime } ( z ) / E _ { 5 } ( z ) \right)$ and $v _ { 3 } = \mathrm { R e } \left( z E _ { 3 } ^ { \prime } ( z ) / E _ { 3 } ( z ) \right)$ . Since $| { \cal E } ( z ) | =$ ${ \mathcal { O } } ( | z | ^ { 8 } )$ for $| z | \to 0$ , we have to use the value $\alpha = 1 / 8$ in (2.32). The regions of $S C$ -stability are shown in Fig.2.8.

SC-Stable Dormand and Prince Pairs of Order 5. We see from Fig.2.8 that the method DOPRI5 is not $S C$ -stable at the intersection of the real axis with the boundary of the stability region. We are therefore interested in finding 5(4)-th order explicit Runge-Kutta pairs from the family of Dormand & Prince (198O) with larger regions of $S C$ -stability.

Requiring the simplifying assumption (I.5.15),Algorithm 5.2 of Sect.II.5 yields a class of Runge-Kutta methods with $c _ { 3 } , c _ { 4 } , c _ { 5 }$ as free parameters. Higham & Hall (199o) have made an extensive computer search for good choices of these parameters in order to have a reasonable size of the stability domain,large parts of $S C$ -stability and a small 6th order error constant. It turned out that the larger one wants the region of $S C$ -stability, the larger the error constant becomes. A compromise choice between Scylla and Charybdis,which in addition yields nice rational coefficients, is given by $c _ { 3 } = 1 / 3$ ， $c _ { 4 } = 1 / 2$ and $c _ { 5 } = 3 / 5$ . This then leads to the method of Table 2.1 which has satisfactory stability properties as can be seen from Fig. 2.8.

# A PI Step Size Control

We saw that it was an I-controler ... and a control-man knows that PI is always better than I ..

(K. Gustafsson, June 1990)

In 1986/87 two students of control theory attended a course of numerical analysis at the University of Lund. The outcome of this contact was the idea to resolve the above instability phenomena in stiff computations by using the concept of “PID control'(Gustafsson,Lundh & Soderlind 1988). The motivation for PID control, a classic in control theory (Callender,Hartree & Porter 1936) is as follows:

Suppose we have a continuous-time control problem where $\theta ( t )$ is the departure, at time $t$ , of a quantity to be controlled from its normal value. Then one might suppose that

$$
{ \dot { \theta } } ( t ) = C ( t ) - m \theta ( t )
$$

where $C ( t )$ denotes the effect of the control and the term $- m \theta ( t )$ represents a self-regulating effect such as $\mathbf { \sp { 6 6 } _ { 2 } }$ vessel in a constant temperature bath". The most simple assumption for the control would be

$$
- { \dot { C } } ( t ) = n _ { 1 } \theta ( t )
$$

which represents, say, a valve opened or closed in dependence of $\theta$ . The equations (2.39) and (2.40) together lead to

$$
{ \ddot { \theta } } + m { \dot { \theta } } + n _ { 1 } \theta = 0
$$

which, for $n _ { 1 } > 0$ ， $m > 0$ , is always stable. If, however, we assume (more realis-tically) that our system has some time-lag, we must replace (2.40) by

$$
- { \dot { C } } ( t ) = n _ { 1 } \theta ( t - T )
$$

and the stability of the process may be destroyed. This is precisely the same effect as the instability of Equation (17.6) of Sect.II.17 and is discussed similarly. In order to preserve stability, one might replace (2.40') by

$$
- { \dot { C } } ( t ) = n _ { 1 } \theta ( t - T ) + n _ { 2 } { \dot { \theta } } ( t - T )
$$

or even by

$$
\begin{array} { r } { - \dot { C } ( t ) = n _ { 1 } \theta ( t - T ) + n _ { 2 } \dot { \theta } ( t - T ) + n _ { 3 } \ddot { \theta } ( t - T ) . } \end{array}
$$

Here, the first term on the right hand side represents the “Integral feedback” $( I )$ ， the second term“Proportional feedback” $( P )$ and the last term is the “Derivative feedback” $( D )$ .The $P$ -term especially increases the constant $m$ in (2.41), thus adds extra friction to the equation. It is thus natural to expect that the system becomes more stable. The precise tuning of the parameters $n _ { 1 } , n _ { 2 } , n _ { 3 }$ is, however, a long task of analytic study and practical experience.

In order to adapt the continuous-time model (2.40") to our situation, we replace

$$
\begin{array} { r l } & { C ( t ) \longleftrightarrow \log h _ { n } \quad \mathrm { ( t h e ~ ^ { * } c o n t r o l ~ v a r i a b l e ^ { * } ) } } \\ & { \theta ( t ) \longleftrightarrow \log | e r r _ { n } | - \log T o l \quad \mathrm { ( t h e ~ ^ { * } d e v i a t i o n " ) } } \end{array}
$$

and replace derivatives in $t$ by differences. Then the formula (see (2.28))

$$
h _ { n + 1 } = h _ { n } \cdot \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { n _ { 1 } } ,
$$

which is

$$
- \bigl ( \log h _ { n + 1 } - \log h _ { n } \bigr ) = n _ { 1 } \bigl ( \log | e r r _ { n } | - \log T o l \bigr ) ,
$$

corresponds to (2.40). The $P I$ -control (2.40") would read

$$
\begin{array} { r l } & { - ( \log h _ { n + 1 } - \log h _ { n } ) = n _ { 1 } ( \log | e r r _ { n } | - \log T o l ) } \\ & { \qquad + n _ { 2 } \big ( ( \log | e r r _ { n } | - \log T o l ) - ( \log | e r r _ { n - 1 } | - \log T o l ) \big ) , } \end{array}
$$

or when resolved,

$$
h _ { n + 1 } = h _ { n } \cdot \bigg ( \frac { T o l } { | e r r _ { n } | } \bigg ) ^ { n _ { 1 } } \bigg ( \frac { | e r r _ { n - 1 } | } { | e r r _ { n } | } \bigg ) ^ { n _ { 2 } } .
$$

In order to perform a theoretical analysis of this new algorithm we again choose the problem $y ^ { \prime } = \lambda y$ and have as in (2.28)

$$
\begin{array} { r l } & { y _ { n + 1 } = R ( h _ { n } \lambda ) y _ { n } } \\ & { e r r _ { n } = E ( h _ { n } \lambda ) y _ { n } } \\ & { h _ { n + 1 } = h _ { n } \cdot \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { n _ { 1 } } \left( \frac { \left| e r r _ { n - 1 } \right| } { | e r r _ { n } | } \right) ^ { n _ { 2 } } } \\ & { = h _ { n } \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { \alpha } \left( \frac { | e r r _ { n - 1 } | } { T o l } \right) ^ { \beta } } \end{array}
$$

where $\alpha = n _ { 1 } + n _ { 2 } , \beta = n _ { 2 }$ . With the notation (2.29) this process becomes

$$
\begin{array} { r l } & { \eta _ { n + 1 } = \log | R ( e ^ { \chi _ { n } } \lambda ) | + \eta _ { n } } \\ & { \chi _ { n + 1 } = \chi _ { n } - \alpha \log | E ( e ^ { \chi _ { n } } \lambda ) | - \alpha \eta _ { n } + \beta \log | E ( e ^ { \chi _ { n - 1 } } \lambda ) | + \beta \eta _ { n - 1 } + \gamma } \end{array}
$$

with some constant $\gamma$ .This can be considered as a map $\left( \eta _ { n } , \chi _ { n } , \eta _ { n - 1 } , \chi _ { n - 1 } \right)$ $ ( \eta _ { n + 1 } , \chi _ { n + 1 } , \eta _ { n } , \chi _ { n } )$ . At a fixed point $( \eta , \chi )$ , which again satisfies (2.31), the Jacobian is given by

$$
\widetilde C = \frac { \partial ( \eta _ { n + 1 } , \chi _ { n + 1 } , \eta _ { n } , \chi _ { n } ) } { \partial ( \eta _ { n } , \chi _ { n } , \eta _ { n - 1 } , \chi _ { n - 1 } ) } = \left( \begin{array} { c c c c } { { 1 } } & { { u } } & { { 0 } } & { { 0 } } \\ { { - \alpha } } & { { 1 - \alpha v } } & { { \beta } } & { { \beta v } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \end{array} \right)
$$

with $u$ and $v$ as in (2.32). A numerical study of the spectral radius $\varrho ( \widetilde { C } )$ with $\alpha =$ $1 / p$ (where $p$ is the exponent of $h$ of the leading term in the error estimator), $\beta =$ 0.08 along the boundary of the stability domains of the above RK-methods shows an impressive improvement (see Fig.2.9) as compared to the standard algorithm of Fig.2.8. The only exception is DOP853,which becomes unstable close to the real axis, whereas it was $S C$ -stable for $\beta = 0$ . For this method,the value $\beta = 0 . 0 4$ is more suitable.

![](images/0d68f8297eaa9ddddd1c7766cc3385bd3467feafeeac0f5d92ecf5f1190be4a5.jpg)  
Fig.2.9.Regions of step-control stability with stabilization factor $\beta = 0 . 0 8$

The step size behaviour of DOPRI5 with the new strategy ( $\beta = 0 . 1 3 )$ applied to the problem (1.6'） is compared in Fig.2.10 to the undamped step size control （ ${ \bf \nabla } \cdot \beta = 0 )$ . The improvement needs no comment. In order to make the difference clearly visible,we have chosen an extra-large tolerance $A t o l = R t o l = 8 \cdot 1 0 ^ { - 2 }$ ： With $\beta = 0 . 1 3$ the numerical solution becomes smooth in the time-direction. The zig-zag error in the $\boldsymbol { x }$ -direction represents the eigenvector corresponding to the largest eigenvalue of the Jacobian and its magnitude is below Atol.

Man sieht dass selbst der frommste Mann nicht allen Leuten gefallen kann. (W. Busch, Kritik des Herzens 1874)

Study for small $h$ . For the non-stiff case the new step size strategy may be slightly less efficient. In order to understand this,we assume that $| e r r _ { n } | \approx C h _ { n } ^ { p }$ so that (2.43c) becomes

$$
h _ { n + 1 } = h _ { n } \bigg ( \frac { T o l } { C h _ { n } ^ { p } } \bigg ) ^ { \alpha } \bigg ( \frac { C h _ { n - 1 } ^ { p } } { T o l } \bigg ) ^ { \beta }
$$

or, by taking logarithms,

$$
\log h _ { n + 1 } + ( p \alpha - 1 ) \log h _ { n } - p \beta \log h _ { n - 1 } = ( \alpha - \beta ) \log \Big ( \frac { T \alpha l } { C } \Big ) .
$$

This is a linear diference equation with characteristic equation

$$
\lambda ^ { 2 } + ( p \alpha - 1 ) \lambda - p \beta = 0 ,
$$

the roots of which govern the response of the system to variations in $C$ . Obviously, the choice $\alpha = 1 / p$ and $\beta = 0$ would be most perfect by making both roots equal to zero; but this is just the classical step size control. We therefore have to compromise by choosing $\alpha$ and $\beta$ such that (2.45) remains stable for large parts of the stability boundary and at the same time keeping the roots of (2.47) significantly smaller than one. A fairly good choice, found by Gustafsson (1991) after some numerical computations,is

![](images/c0d0ae93f6408ac119ea904985ea89fdbbdb3a9654a2300a9f26b105237309e7.jpg)  
Fig.2.10. Numerical solution of (1.6'） with $T o l = 8 \cdot 1 0 ^ { - 2 }$

$$
\alpha \approx 0 . 7 / p , \qquad \beta \approx 0 . 4 / p .
$$

# Stabilized Explicit Runge-Kutta Methods

For many problems, usually not very stiff,of large dimension, and with eigenvalues known to lie in a certain region, explicit methods with large stability domains can be very eficient. We consider here methods with extended stability domains along the negative real axis,which are, therefore, especially suited for the time integration of systems of parabolic PDEs. An excellent survey article with additional details and references is Verwer (1996).

Our problem is to find, for a given $s$ , a polynomial of the form $R ( z ) = 1 + z +$ $a _ { 2 } z ^ { 2 } + \ldots + a _ { s } z ^ { s }$ such that the corresponding stability domain is, in the direction of the negative axis,as large as possible. The main ingredient for these methods are the Chebyshev polynomials (Chebyshev 1854)

$$
T _ { s } ( x ) = \cos ( s \operatorname { a r c c o s } x )
$$

$$
T _ { s } ( x ) = 2 x T _ { s - 1 } ( x ) - T _ { s - 2 } ( x ) , \qquad T _ { 0 } ( x ) = 1 , \quad T _ { 1 } ( x ) = x
$$

![](images/726ed458e22466eaaff95e505359eeb6686084376d1e14b8b4e9a917207c5ffe.jpg)  
Fig.2.11. Shifted Chebyshev polynomial $T _ { 9 } ( 1 + z / 8 1 )$ and its zeros

![](images/0aac40a98abe2196c466757db4eeb23ff4de1daddbdf6324cd3e786ffbfc8e31.jpg)  
Fig.2.12. Stability domains for shifted Chebyshev polynomials (s = 2,3,4,5) (dots represent limiting case $s \to \infty$ , see Exercise 8 below)

![](images/64ba04b03ce6c92845c4a26a2014f94645dd6bd04ed7d609e8eb5e970857ae48.jpg)  
Fig.2.13.Stability domains for damped Chebyshev stability functions, $\varepsilon = 0 . 0 5$

which remain for $- 1 \leq x \leq 1$ between $- 1$ and $+ 1$ and among these polynomials have the largest possible derivative $T _ { s } ( 1 ) = s ^ { 2 }$ (A.A. Markov 1890). Therefore, one must set (Saul'ev 1960, Saul'ev's postgraduate student Yuan Chzao Din 1958, Franklin 1959,Guillou & Lago 1961)

$$
\begin{array} { r } { \hat { R } _ { s } ( z ) = T _ { s } ( 1 + z / s ^ { 2 } ) } \end{array}
$$

so that $R _ { s } ( 0 ) = 1$ ， $R _ { s } ^ { \prime } ( 0 ) = 1$ , and $| R _ { s } ( z ) | \leq 1$ for $- 2 s ^ { 2 } \leq z \leq 0$ (see Fig. 2.11). In particular we have

$$
\begin{array} { r l } & { R _ { 1 } ( z ) = 1 + z } \\ & { R _ { 2 } ( z ) = 1 + z + \frac { 1 } { 8 } z ^ { 2 } } \\ & { R _ { 3 } ( z ) = 1 + z + \frac { 4 } { 2 7 } z ^ { 2 } + \frac { 4 } { 7 2 9 } z ^ { 3 } } \\ & { R _ { 4 } ( z ) = 1 + z + \frac { 5 } { 3 2 } z ^ { 2 } + \frac { 1 } { 1 2 8 } z ^ { 3 } + \frac { 1 } { 8 1 9 2 } z ^ { 4 } } \\ & { R _ { 5 } ( z ) = 1 + z + \frac { 4 } { 2 5 } z ^ { 2 } + \frac { 2 8 } { 3 1 2 5 } z ^ { 3 } + \frac { 1 6 } { 7 8 1 2 5 } z ^ { 4 } + \frac { 1 6 } { 9 7 6 5 6 2 5 } z ^ { 5 } \ . } \end{array}
$$

whose stability domains are represented in Fig. 2.12.

Damping. In the points where $T _ { s } ( 1 + z / s ^ { 2 } ) = \pm 1$ , there is no damping at all of the higher frequencies and the stability domain has zero width. We therefore choose a small $\varepsilon > 0$ ,say $\varepsilon = 0 . 0 5$ , and put (already suggested by Guillou & Lago 1961)

$$
R _ { s } ( z ) = \frac { 1 } { T _ { s } ( w _ { 0 } ) } T _ { s } ( w _ { 0 } + w _ { 1 } z ) , \quad w _ { 0 } = 1 + \frac { \varepsilon } { s ^ { 2 } } , \quad w _ { 1 } = \frac { T _ { s } ( w _ { 0 } ) } { T _ { s } ^ { \prime } ( w _ { 0 } ) } .
$$

These polynomials oscillate between approximately $1 - \varepsilon$ and $- 1 + \varepsilon$ and again satisfy $R _ { s } ( z ) = 1 + z + \mathcal { O } ( z ^ { 2 } )$ . The stability domains become a bit shorter (by $( 4 \varepsilon / 3 ) s ^ { 2 } )$ , but the boundary is in a safe distance from the real axis (see Fig. 2.13).

Lebedev's Realization. Our next problem is to find Runge-Kutta methods which realize these stability polynomials. A first idea, mentioned by Saul'ev (1960) and Guillou & Lago (1961), is to write

$$
R _ { s } ( z ) = \prod _ { \ i = 1 } ^ { s } ( 1 + \delta _ { \ i } z ) \qquad \mathrm { w h e r e } \quad \delta _ { i } = - \frac { 1 } { z _ { i } } , \quad z _ { \ i } \mathrm { ~ r o o t s ~ o f ~ } R ( z )
$$

and to represent the RK method as the composition of explicit Euler steps

$$
g _ { 0 } : = y _ { 0 } , \qquad g _ { \iota } : = g _ { \iota - 1 } + h \delta _ { \iota } f ( g _ { \iota - 1 } ) , \quad ( i = 1 , 2 , \ldots , s ) , \qquad y _ { 1 } : = g _ { s } .
$$

A disadvantage here is the fact that for the first of these roots,which in absolute value is much smaller than the others, we shall have a very large Euler step, which is surely not good. Lebedev's idea (Lebedev 1989,1994) is therefore to group the roots symmetrically two-by-two together and to represent the corresponding quadratic factor

$$
( 1 + \delta _ { i } z ) ( 1 + \delta _ { i } ^ { \prime } z ) = ( 1 + 2 \alpha _ { \iota } z + \beta _ { \iota } z ^ { 2 } )
$$

by a two-stage scheme

$$
\begin{array} { r l } & { \qquad g _ { \iota } : = g _ { i - 1 } + h \alpha _ { \iota } f ( g _ { \iota - 1 } ) } \\ & { \qquad g _ { i + 1 } ^ { \star } : = g _ { i } + h \alpha _ { i } f ( g _ { \iota } ) } \\ & { \qquad g _ { \iota + 1 } : = g _ { i + 1 } ^ { \star } - h \alpha _ { i } \gamma _ { i } \big ( f ( g _ { i } ) - f ( g _ { \iota - 1 } ) \big ) } \\ & { \qquad = g _ { i + 1 } ^ { \star } - \gamma _ { \iota } \big ( ( g _ { i + 1 } ^ { \star } - g _ { i } ) - ( g _ { i } - g _ { i - 1 } ) \big ) } \end{array}
$$

which produces (2.54) if $\beta _ { i } = \alpha _ { \iota } ^ { 2 } ( 1 - \gamma _ { \iota } )$ . This halves nearly the largest Euler step size and allows also complex conjugate pairs of roots. The expression $( g _ { i + 1 } ^ { \star } - g _ { i } ) -$ $\left( g _ { \ i } - g _ { \ i - 1 } \right) \approx h ^ { 2 } \alpha _ { \ i } ^ { 2 } y ^ { \prime \prime }$ can be used for error estimations and step size selections. For odd $s$ , there remains one single root which gives rise to an Euler step (2.53).

Best Ordering. Some attention is now necessary for the decision in which order the roots shall be used (Lebedev & Finogenov 1976). This is done by two requirements: firstly, the quantities

$$
S _ { \jmath } = \operatorname* { m a x } _ { z } | 1 + \delta _ { 1 } z | \prod _ { \imath = 1 } ^ { \jmath } | 1 + 2 \alpha _ { \imath } z + \beta _ { \imath } z ^ { 2 } | ,
$$

which express the stability of the internal stages,must be $\leq 1$ (here, the max is taken over real $z$ in the stability interval of the method). Secondly, the quantities

$$
Q _ { j } = \operatorname * { m a x } _ { z } \prod _ { i = \jmath + 1 } ^ { s } | 1 + 2 \alpha _ { \iota } z + \beta _ { i } z ^ { 2 } | ,
$$

which describe the propagation of rounding errors,must be as small as possible. These conditions, evaluated numerically for the case $s = 9$ , lead to the ordering indicated in Fig.2.11.

Second Order Methods. If the stability polynomial is a second order approximation to $e ^ { z }$ ,i.e., if

$$
R _ { s } ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + a _ { 3 } z ^ { 3 } + \ldots + a _ { s } z ^ { s }
$$

then it can be seen from (2.8) that any corresponding Runge-Kutta scheme is also of second order for nonlinear problems. Analytic expressions, in terms of an elliptic integral, for such optimal polynomials have been obtained by Lebedev & Medovikov (1994). Their stability region reaches to $- 0 . 8 2 1 8 4 2 \cdot s ^ { 2 }$ for $s \gg 1$ Their practical computation is usually done numerically (Remez 1957, Lebedev 1995).For example,in the case $s = 9$ and for a damping factor $\varepsilon = 0 . 0 1 5$ ，we obtain the roots

$$
\begin{array} { r l } & { z _ { 9 } = - 6 4 . 6 4 2 3 8 3 8 9 , \quad z _ { 8 } = - 6 0 . 6 7 4 7 9 3 4 7 , \quad z _ { 7 } = - 5 3 . 2 1 6 9 5 4 8 8 , } \\ & { z _ { 6 } = - 4 3 . 1 6 5 2 7 0 1 0 , \quad z _ { 5 } = - 3 1 . 7 2 4 7 1 6 9 9 , \quad z _ { 4 } = - 2 0 . 2 5 4 7 4 1 6 3 , } \\ & { z _ { 3 } = - 1 0 . 0 5 5 4 5 9 3 8 , \quad z _ { 2 , 1 } = - 1 . 3 0 5 9 6 1 6 6 \pm i \cdot 1 . 3 4 0 4 7 5 1 7 } \end{array}
$$

The corresponding stability polynomials,which are stable for $- 6 5 . 1 5 \leq z \leq 0$ ,the stability domain, and the best ordering are shown in Fig. 2.14. We see that we now have a pair of complex roots.

Lebedev's computer code,called DUMKA, incorporates the formulas of the above type with automatic selection of $h$ and $s$ in a wide range.

![](images/918c85c618d7fb17239ad04801b79447436e84e70e9d2134284e1f92f62bea73.jpg)  
Fig. 2.14. Second order Zolotarev approximation with stability domain

Numerical Example. As an illustration, the method corresponding to (2.55) and (2.57) has been applied to problem (1.6'). Theory predicts stability for approximately $h \leq 6 5 . 1 5 / 1 3 5 = 0 . 4 8 2 6$ . The leftmost picture of Fig.2.15 is computed with $h = 0 . 4 8 8 6 5$ ,which is a little too large and produces instability. The middle picture is produced by the code DUMKA with $T o l = 3 \cdot 1 0 ^ { - 3 }$

![](images/d6e5d95076891699c553cafb1bd4f467228c69da7692e41cc54cbf2659208e94.jpg)  
Fig.2.15. Problem (1.6): Lebedev9, $h = 0 . 4 8 8 6 5$ (left), DUMKA (middle),RKC (right) (all internal stages drawn)

The Approach of van der Houwen & Sommeijer. An elegant idea for a second realization has been found by van der Houwen & Sommeijer (198O): apply scaled and shifted Chebyshev polynomials and use the three-term recusion formula (2.49') for defining the internal stages. We therefore, following Bakker (1973), set

$$
R _ { s } ( z ) = a _ { s } + b _ { s } T _ { s } ( w _ { 0 } + w _ { 1 } z ) \qquad w _ { 0 } = 1 + \varepsilon / s ^ { 2 } , \varepsilon \approx 0 . 1 5 .
$$

The conditions for second order

$$
R _ { s } ( 0 ) = 1 , \quad R _ { s } ^ { \prime } ( 0 ) = 1 , \quad R _ { s } ^ { \prime \prime } ( 0 ) = 1
$$

lead to

$$
w _ { 1 } = \frac { T _ { s } ^ { \prime } ( w _ { 0 } ) } { T _ { s } ^ { \prime \prime } ( w _ { 0 } ) } , \qquad b _ { s } = \frac { T _ { s } ^ { \prime \prime } ( w _ { 0 } ) } { ( T _ { s } ^ { \prime } ( w _ { 0 } ) ) ^ { 2 } } , \qquad a _ { s } = 1 - b _ { s } T _ { s } ( w _ { 0 } ) ,
$$

with damping $a _ { s } + b _ { s } \approx 1 - \varepsilon / 3$ (see Ex.9). We now put for the internal stages

$$
R _ { j } ( z ) = a _ { \jmath } + b _ { \jmath } T _ { j } ( w _ { 0 } + w _ { 1 } z ) \qquad j = 0 , 1 , \ldots , s - 1 .
$$

It has been discovered by Sommeijer (see Sommeijer & Verwer 198O), that these $R _ { j } ( z )$ can, for $j \geq 2$ , be approximations of second order at certain points $\boldsymbol { x } _ { 0 } + \boldsymbol { c } _ { j } \boldsymbol { h }$ if

$$
R _ { \ j } ( 0 ) = 1 , \quad R _ { \ j } ^ { \prime } ( 0 ) = c _ { \ j } , \quad R _ { \ j } ^ { \prime \prime } ( 0 ) = c _ { \ j } ^ { 2 }
$$

which gives

$$
R _ { j } ( z ) - 1 = b _ { j } \big ( T _ { j } ( w _ { 0 } + w _ { 1 } z ) - T _ { j } ( w _ { 0 } ) \big ) , \qquad b _ { j } = \frac { T _ { j } ^ { \prime \prime } ( w _ { 0 } ) } { ( T _ { j } ^ { \prime } ( w _ { 0 } ) ) ^ { 2 } } .
$$

The three-term recurrence relation (2.49') now leads to

$$
R _ { j } ( z ) - 1 = \mu _ { j } ( R _ { j - 1 } ( z ) - 1 ) + \nu _ { j } ( R _ { j - 2 } ( z ) - 1 ) + \kappa _ { j } \cdot z \cdot ( R _ { j - 1 } ( z ) - a _ { j - 1 } )
$$

where

$$
\mu _ { j } = \frac { 2 b _ { j } w _ { 0 } } { b _ { j - 1 } } , \quad \nu _ { j } = \frac { - b _ { j } } { b _ { j - 2 } } , \quad \kappa _ { j } = \frac { 2 b _ { j } w _ { 1 } } { b _ { j - 1 } } , \qquad j = 2 , 3 , \ldots , s .
$$

This formula allows, in the case of a nonlinear differential system, to define the scheme

$$
\begin{array} { l r } { { g _ { 0 } - y _ { 0 } = 0 , } } \\ { { g _ { 1 } - y _ { 0 } = \kappa _ { 1 } h f ( g _ { 0 } ) , } } \\ { { g _ { j } - y _ { 0 } = \mu _ { j } ( g _ { j - 1 } - y _ { 0 } ) + \nu _ { j } ( g _ { j - 2 } - y _ { 0 } ) + \kappa _ { j } h f ( g _ { j - 1 } ) - a _ { j - 1 } \kappa _ { j } h f ( g _ { 0 } ) , } } \end{array}
$$

which, being of second order for $y ^ { \prime } { = } \lambda y$ , is of second order for nonlinear equations too (again because of (2.8)). For $j = 1$ only first order is possible and $\kappa _ { 1 }$ can be chosen freely. Sommeijer & Verwer (1980) suggest to put

$$
b _ { 0 } = b _ { 2 } , b _ { 1 } = b _ { 2 } \mathrm { w h i c h g i v e s } \kappa _ { 1 } = c _ { 1 } = \frac { c _ { 2 } } { T _ { 2 } ^ { \prime } ( w _ { 0 } ) } \approx \frac { c _ { 2 } } { 4 } .
$$

Fig. 2.16 shows, for $s \approx 9$ as usual, the functions $R _ { s } ( z )$ and $R _ { j } ( z ) , j = 2 , . . . , s -$ 1 together with the stability domain of $R _ { s } ( z )$ (the“Venus of Willendorf"） in exactly the same frame as Lebedev's Zolotarev polynomial of Fig. 2.14. We see that the stability domain becomes a little shorter, but we have closed analytic expres-sions and a smoother behaviour of the $c _ { i } \mathrm { ^ { \circ } } \mathbf { s }$ (see Fig.2.15,right). Allinternal stages satisfy $| R _ { j } ( z ) | \leq 1$ , and the method can be seen to possess a satisfactory numerical stability (see Verwer,Hundsdorfer & Sommeijer 199O). The above formulas have been implemented in a research code RKC ("Runge-Kutta-Chebyshev") by Sommeijer (1991). As can be seen from Fig.2.15, it performs well for equation (1.6'). More numerical results shall be reported in Sect. IV.10.

![](images/7dacc8adaf2e93e845220c003f9c80f79042aa6c0490df962ac8bac5c8895963.jpg)  
Fig. 2.16. Stability function and domain for RKC method, $s = 9$ ， $\varepsilon = 0 . 1 5$

Combined Approach of Abdulle & Medovikov. Recent research and a code ROCK4 are presented in: A. Abdulle, Fourth order Chebyshev methods with recurrence relation, to appear in SIAM J. Sci. Comput. 2002.

# Exercises

1. Prove that Runge-Kutta methods are invariant under linear transformations $y =$ $T z$ (i.e., if one applies the method to $y \prime = f ( x , y )$ and to $z ^ { \prime } = T ^ { - 1 } f ( x , T z )$ with initial values satisfying $y _ { 0 } = T z _ { 0 }$ , then we have $y _ { 1 } = T z _ { 1 }$ )

2. Consider the differential equation $y ^ { \prime } = A y$ and a numerical solution given by $y _ { n + 1 } = R ( h A ) y _ { n }$ . Suppose that $R ( z )$ is $A$ -stable,i.e., it satisfies

$$
| R ( z ) | \leq 1 \qquad { \mathrm { f o r } } \qquad { \mathrm { R e ~ } } z \leq 0 ,
$$

and show, by transforming $A$ to Jordan canonical form, that

a) if $y ^ { \prime } = A y$ is stable, then $\{ y _ { n } \}$ is bounded; b）if $y ^ { \prime } = A y$ is asymptotically stable, then $y _ { n } \to 0$ for $n \to \infty$ ·

3. (Optimal stability for hyperbolic problems,van der Houwen (1968),(1977), p.99): Given $m$ ，find a polynomial $\begin{array} { r } { R _ { m } ( z ) = 1 + z + . . } \end{array}$ . of degree $m + 1$ such that $| R ( i y ) | \leq 1$ for $- \beta \leq y \leq \beta$ with $\beta$ as large as possible.

Result. The solution (Sonneveld & van Leer 1985) is given by

$$
R _ { m } ( z ) = \frac { 1 } { 2 } V _ { m - 1 } ( \zeta ) + V _ { m } ( \zeta ) + \frac { 1 } { 2 } V _ { m + 1 } ( \zeta ) , \quad \zeta = \frac { z } { m }
$$

where $V _ { m } ( \zeta ) = i ^ { m } T _ { m } ( \zeta / i )$ are the Chebyshev polynomials with positive coefficients. $R _ { m } ( i y )$ is stable for $- m \leq y \leq m$ . The first $R _ { m }$ are (see Abramowitz & Stegun, p. 795)

$$
\begin{array} { l r } { { R _ { 1 } ( z ) = 1 + \zeta + \zeta ^ { 2 } } } & { { \zeta = \frac { z } { m } } } \\ { { \ } } & { { R _ { 2 } ( z ) = 1 + 2 \zeta + 2 \zeta ^ { 2 } + 2 \zeta ^ { 3 } } } \\ { { \ } } & { { R _ { 3 } ( z ) = 1 + 3 \zeta + 5 \zeta ^ { 2 } + 4 \zeta ^ { 3 } + 4 \zeta ^ { 4 } } } \\ { { \ } } & { { R _ { 4 } ( z ) = 1 + 4 \zeta + 8 \zeta ^ { 2 } + 1 2 \zeta ^ { 3 } + 8 \zeta ^ { 4 } + 8 \zeta ^ { 5 } } } \end{array}
$$

Similar as for Chebyshev polynomials, they satisfy the recurrence relation $R _ { m + 1 } = 2 \zeta R _ { m } + R _ { m - 1 } ( m \geq 2 )$ . Their stability domains are given in Fig. 2.17.

![](images/520f94074a509b1989999f2507b664b9fdb51e1831fa882d8e89e6a149ded4fa.jpg)  
Fig.2.17. Stability domains for hyperbolic approximations

4． Linearize the rope equation (1.24) in the neighbourhood of $\theta = \dot { \theta } = 0$ and make a stability analysis. Re-obtain Lagrange's equation (I.6.2) from the linearized equation with the coordinate transformation

$$
\begin{array} { r } { \boldsymbol { y } = \left( \begin{array} { l l l l l } { 1 } & & & & \\ { 1 } & { 1 } & & & \\ { 1 } & { 1 } & { 1 } & & \\ { : } & { \vdots } & { \vdots } & { \ddots } \end{array} \right) \boldsymbol \theta , \qquad \boldsymbol \theta = \left( \begin{array} { l l l l l } { 1 } & & & & \\ { - 1 } & { 1 } & & & \\ & { - 1 } & { 1 } & & \\ & & { \ddots } & { \ddots } \end{array} \right) \boldsymbol y . } \end{array}
$$

5.Fig.2.18 shows the numerical results of the classical 4th order Runge-Kutta method with equidistant steps over $0 \leq t \leq 5$ for the beam problem(1.7)-(1.20) with $n \approx 8$ . Explain the result with the help of Fig.2.1.

![](images/6cedcfcc18332dfd240b797084a53f939767e1197597b52671f654b2ac055dda.jpg)  
Fig. 2.18. Classical Runge-Kutta method (constant step sizes) on the beam problem

6.For theexample of Exercise 5,the explicit Euler method,although converging for $h \to 0$ , is never stable (see Fig. 2.19). Why?

7. Let $\lambda$ be an eigenvalue of the two-dimensional left upper submatrix of $\widetilde { C }$ in (2.45) (matrix $C$ of (2.32)) and denote its analytic continuation as eigenvalue of $\widetilde { C }$ by $\lambda ( \beta )$ . Prove that

a)If $\operatorname { R e } \lambda \neq 0$ , then for some $y \in \mathbb { R }$

$$
\lambda ( \beta ) = \lambda \cdot \left( 1 - \frac { \beta } { \alpha } \left( 1 - \mathrm { R e } \lambda \right) + i \beta y + \mathcal { O } ( \beta ^ { 2 } ) \right) .
$$

This shows that $| \lambda ( \beta ) | < | \lambda |$ for small $\beta > 0$ if $\mathrm { R e } \lambda < 1$

b)If $\lambda$ and $\mu$ are two distinct real eigenvalues of the above mentioned submatrix,then

$$
\lambda ( \beta ) = \lambda \cdot \Big ( 1 - \frac { \beta } { \alpha } \left( 1 - \frac { 1 } { \lambda } \right) ^ { 2 } \frac { 1 } { \lambda - \mu } + \mathcal { O } ( \beta ^ { 2 } ) \Big ) .
$$

![](images/eb9de4faf6c1d46465baefc721fd0f662b23e2b694beaf5dcced1f77c2f0b83a.jpg)  
Fig. 2.19.Explicit Euler on the beam problem (every 5Oth step dran)

Hint. Write the characteristic polynomial of $\widetilde { C }$ in the form

$$
\operatorname* { d e t } ( \lambda I - \widetilde { C } ) = \lambda \big ( \lambda p ( \lambda ) + \beta q ( \lambda ) \big ) ,
$$

where $p ( \lambda ) = \operatorname* { d e t } ( \lambda I - C )$ is the characteristic polynomial of $C$ , and differentiate with respect to $\beta$ ·

8. Show that for the Chebyshev stability functions (2.5O) we have

$$
\operatorname* { l i m } _ { s  \infty } R _ { s } ( z ) = \cos ( \sqrt { - 2 z } ) .
$$

Hint. Insert $\operatorname { a r c c o s } ( 1 - x ^ { 2 } / 2 ) \approx x$ into (2.49) and (2.50). The corresponding stability domain is indicated by dotted lines in the last picture of Fig.2.12.

9. Show (for example with the help of(2.49') that for the Chebyshev polynomials

$$
T _ { s } ^ { \prime } ( 1 ) = s ^ { 2 } , \qquad T _ { s } ^ { \prime \prime } ( 1 ) = \frac { s ^ { 2 } ( s ^ { 2 } - 1 ) } { 3 }
$$

and obtain asymptotic values (for $\varepsilon \to 0$ )for $w _ { 1 } , b _ { s } , a _ { s }$ , the damping factor and the stability interval of the Bakker polynomials (.58).

10.(Cross-shaped stability domains). For $- 1 \leq \varphi \leq 1$ we put $z = - b \pm \sqrt { a ( \varphi - 1 ) + b ^ { 2 } }$ ,so that $z$ moves on a cross $- 2 b \leq$ $z \le 0$ and $z = - b \pm i y$ . Thus (an idea of Lebedev)

$$
R _ { 2 s } ( z ) = T _ { s } ( \varphi ( z ) )
$$

![](images/3292bde8540e7a77b9d13a6e25915b65271f9b427c4eeac63a55865a6d2bd91f.jpg)

is a stability function for eigenvalues on crosses (as, e.g., for the PLATE problem). Determine $a$ in dependence of $b$ from the condition $R ^ { \prime } ( 0 ) = 1$ and find the maximal value for $y$

Result. $R _ { 2 s } ( z ) = T _ { s } ( 1 + z / s ^ { 2 } + z ^ { 2 } / ( 2 b s ^ { 2 } ) )$ ； $y _ { \mathrm { { m a x } } } = { \sqrt { 4 b s ^ { 2 } - b ^ { 2 } } } .$

# IV.3Stability Function of Implicit RK-Methods

I didn't like all these“strong”，“perfect",“absolute”，“general-ized",“super”,“hyper”,“complete” and so on in mathematical definitions,I wanted something neutral; and having been impres-sed by David Young's “property $A ^ { \ast }$ ,I chose the term“A-stable”.

(G. Dahlquist, in 1979)

There are at least two ways to combat stiffness. One is to design a better computer, the other, to design a better algorithm.

(H.Lomax in Aiken 1985)

Methods are called $A$ -stable if there are no stability restrictions for $y ^ { \prime } { = } \lambda y$ ， $\mathrm { R e } \lambda <$ O and $h > 0$ . This concept was introduced by Dahlquist (1963) for linear multistep methods,but also applied to Runge-Kutta processes. Ehle (1968) and Axelsson (1969) then independently investigated the $A$ -stability of implicit Runge-Kutta methods and proposed new classes of $A$ -stable methods. A nice paper of Wright (1970) studied collocation methods.

# The Stability Function

We start with the implicit Euler method. This method, $y _ { 1 } = y _ { 0 } + h f ( x _ { 1 } , y _ { 1 } )$ ,applied to Dahlquist's equation $y ^ { \prime } = \lambda y$ becomes $y _ { 1 } = y _ { 0 } + h \lambda y _ { 1 }$ which, after solving for $y _ { 1 }$ ， gives

$$
y _ { 1 } = R ( h \lambda ) y _ { 0 } \quad { \mathrm { w i t h } } \quad R ( z ) = { \frac { 1 } { 1 - z } } .
$$

This time, the stability domain is the exterior of the circle with radius 1 and centre $+ 1$ . The stability domain thus covers the entire negative half-plane and a large part of the positive half-plane as well. The implicit Euler method is very stable.

Proposition 3.1. The s-stage implicit Runge-Kutta method

$$
\begin{array} { l l } { { g _ { \imath } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } ) \quad } } & { { i = 1 , \ldots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } ) \quad } } & { { } } \end{array}
$$

applied to $y ^ { \prime } = \lambda y$ yields $y _ { 1 } = R ( h \lambda ) y _ { 0 }$ with

$$
\begin{array} { c } { R ( z ) = 1 + z b ^ { T } ( I - z A ) ^ { - 1 } \mathbb { 1 } , } \\ { b ^ { T } = ( b _ { 1 } , \dots , b _ { s } ) , \quad A = ( a _ { \iota _ { \mathcal { I } } } ) _ { i , \jmath = 1 } ^ { s } , \quad \mathbb { 1 } = ( 1 , \dots , 1 ) ^ { T } . } \end{array}
$$

Remark. As in Definition 2.1, $R ( z )$ is called the stability function of Method (3.1).

Proof. Equation (3.1a) with $f ( x , y ) = \lambda y$ ， $z = h \lambda$ becomes a linear system for the computation of $g _ { 1 } , \ldots , g _ { s }$ . Solving this and inserting into (3.1b) leads to (3.2).

Another useful formula for $R ( z )$ is the following (Stetter 1973,Scherer 1979):

Proposition 3.2. The stability function of(3.1) satisfies

$$
R ( z ) = { \frac { \operatorname* { d e t } \left( I - z A + z \Im b ^ { T } \right) } { \operatorname* { d e t } \left( I - z A \right) } } .
$$

Proof. Applying (3.1) to (2.9) yields the linear system

$$
\left( \begin{array} { l l } { I - z A } & { 0 } \\ { - z b ^ { T } } & { 1 } \end{array} \right) \left( \begin{array} { l } { g } \\ { y _ { 1 } } \end{array} \right) = y _ { 0 } \left( \begin{array} { l } { \Im } \\ { 1 } \end{array} \right) .
$$

Cramer's rule (Cramer 1750) implies that the denominator of $R ( z )$ is $\operatorname* { d e t } ( I -$ $z A )$ ，and its numerator

$$
\operatorname* { d e t } { \binom { I - z A \quad \mathbb { 1 } } { - z b ^ { T } \quad 1 } } = \operatorname* { d e t } { \binom { I - z A + z \mathbb { 1 } b ^ { T } \quad 0 } { - z b ^ { T } \quad 1 } } = \operatorname* { d e t } { \big ( } I - z A + z \mathbb { 1 } b ^ { T } { \big ) } .
$$

![](images/26bb08d9c2088e57c909eb667fc8d27767ec2f098dfc756e9d5c1b08141a0ee5.jpg)  
Fig.3.1. Stability domains for implicit Runge-Kutta methods

The stability functions for the methods of Sect.II.7 are presented in Table 3.1. The corresponding stability domains are displayed in Fig.3.1.

We see that for implicit methods $R ( z )$ becomes a rational function with numerator and denominator of degree $\leq s$ . We write

$$
R ( z ) = \frac { P ( z ) } { Q ( z ) } , \qquad \deg P = k , \quad \deg Q = j .
$$

Table 3.1. Stability functions for implicit Runge-Kutta methods of Sect. I1.7   

<table><tr><td></td><td>Method</td><td>R(z)</td></tr><tr><td>a)</td><td>0-method (I1.7.2)</td><td>1+z(1-0) 1-z0</td></tr><tr><td>b)</td><td>implicit Euler (II.7.3)</td><td>1 1-z</td></tr><tr><td>c）</td><td>implicit midpoint (I1.7.4) } trapezoidal rule (I1.7.5)</td><td>1+z/2 1-x/2</td></tr><tr><td>d）</td><td>Hammer-Hollingsworth (II.7.6)</td><td>1+4z/6+x²/6 1-x/3</td></tr><tr><td>e)</td><td>SDIRK order 3 (Table II.7.2)</td><td>1+z(1-2γ)+x²(1/2-2γ+γ²) （1-Y2）</td></tr><tr><td>f</td><td>Hammer-Hollingsw. 4 (Table II.7.3)} Lobatto IIIA, order 4 (Table II.7.7)</td><td>1+z/2+z²/12 1-x/2+z²/12</td></tr><tr><td>g）</td><td>Kuntzm.-Butcher 6 (Table I1.7.4)</td><td>1+z/2+z²/10+x³/120 1-z/2+z²/10-z³/120</td></tr><tr><td>h)</td><td>Butcher&#x27;s Lobatto 4 (Table I1.7.6)</td><td>1+3z/4+z²/4+ z³/24 1-z/4</td></tr><tr><td>i)</td><td>Butcher&#x27;s Lobatto 6 (Table II.7.6)</td><td>1+2z/3+z²/5+x³/30+z4/360 1-z/3+z²/30</td></tr><tr><td>j）</td><td>Radau IIA, order 5 (Table II.7.7)</td><td>1+2z/5+z²/20 1-3x/5+3z²/20-z/60</td></tr></table>

If the method is of order $p$ ,then

$$
e ^ { z } - R ( z ) = C z ^ { p + 1 } + { \mathcal O } ( z ^ { p + 2 } ) \qquad { \mathrm { f o r ~ } } z \to 0
$$

(see Theorem 2.2). The constant $C$ is usually $\neq 0$ . If not, we increase $p$ in (3.5) until $C$ becomes $\neq 0$ . We then call $R ( z )$ a rational approximation to $e ^ { z }$ of order $p$ and $C$ its error constant.

# A-Stability

We observe that some methods are stable on the entire left half-plane $\mathbb { C } ^ { - }$ .This is precisely the set of eigenvalues,where the exact solution of (2.9) is stable too (Sect.I.13, Theorem 13.1). A desirable property for a numerical method is that it preserves this stability property.

Definition 3.3 (Dahlquist 1963). A method, whose stability domain satisfies

$$
S \supset \mathbb { C } ^ { - } = \{ z ; \quad \mathrm { R e } z \leq 0 \} ,
$$

is called A-stable.

A Runge-Kutta method with (3.4) as stability function is $A$ -stable if and only if

$$
| R ( i y ) | \leq 1 \qquad { \mathrm { f o r ~ a l l ~ r e a l ~ } } y
$$

and

$$
R ( z ) \mathrm { i s ~ a n a l y t i c ~ f o r ~ } \mathrm { R e } z < 0 .
$$

This follows from the maximum principle applied to $\mathbb { C } ^ { - }$ .By a slight abuse of language, we also call $R ( z )$ $A$ -stable in this case (or, as many authors say, $\ " A \ –$ acceptable", Ehle 1968).

Condition (3.6) alone means stability on the imaginary axis and may be called $I$ -stability. It is equivalent to the fact that the polynomial

$$
E ( y ) = | Q ( i y ) | ^ { 2 } - | P ( i y ) | ^ { 2 } = Q ( i y ) Q ( - i y ) - P ( i y ) P ( - i y )
$$

satisfies

$$
E ( y ) \geq 0 \qquad { \mathrm { f o r ~ a l l ~ } } y \in \mathbb { R } .
$$

Proposition 3.4. $E ( y )$ ， defined by (3.8), is an even polynomial of degree ≤ $2 \operatorname* { m a x } ( \deg P , \deg Q )$ .1f $R ( z )$ is an approximation of order $p$ ，then

$$
E ( y ) = \mathcal { O } ( y ^ { p + 1 } ) \qquad f o r \ y \to 0 .
$$

Proof. Taking absolute values in (3.5) gives

$$
| e ^ { z } \vert - \frac { | P ( z ) \vert } { | Q ( z ) | } = \mathcal { O } ( z ^ { p + 1 } ) .
$$

Putting $z = i y$ and using $\left\{ e ^ { \imath y } \right\} = 1$ leads to

$$
| Q ( i y ) | - | P ( i y ) | = \mathcal { O } ( y ^ { p + 1 } ) .
$$

The result now follows from

$$
E ( y ) = ( | Q ( i y ) | + | P ( i y ) | ) ( | Q ( i y ) | - | P ( i y ) | ) .
$$

Examples 3.5.For the implicit midpoint rule, the trapezoidal rule, the Hammer & Hollingsworth, the Kuntzmann & Butcher and Lobatto IIIA methods (c,f, g of Table 3.1） we have $\textstyle E ( y ) \equiv 0$ since $Q ( z ) = P ( - z )$ ．This also follows from Proposition 3.4 because $p = 2 j$ . A straightforward computation shows that (3.7) is satisfied, hence these methods are $A$ -stable.

For methods d, h, i of Table 3.1 we have $\deg P > \deg Q$ and the leading coefficient of $E$ is negative. Therefore (3.9) cannot be true for $y  \infty$ and these methods are not $A$ -stable.

For the Radau IIA method of order 5 (case j) we obtain $E ( y ) = y ^ { 6 } / 3 6 0 0$ and by inspection of the zeros of $Q ( z )$ the method is seen to be $A$ -stable.

For the two-stage SDIRK method (case e) $E ( y )$ becomes

$$
E ( y ) = ( \gamma - 1 / 2 ) ^ { 2 } ( 4 \gamma - 1 ) y ^ { 4 } .
$$

Thus the method is $A$ -stable for $\gamma \geq 1 / 4$ ． The 3rd order method is $A$ -stable for $\gamma = ( 3 + \sqrt { 3 } ) / 6$ , but not for $\gamma = ( 3 - \sqrt { 3 } ) / 6$ (see Fig.3.1).

The following general result explains the $I .$ stability properties of the foregoing examples.

Proposition 3.6. $A$ rational function (3.4) of order $p \geq 2 j - 2$ is $I$ -stable if and only if $| R ( \infty ) | \leq 1$ ，

Proof. $| R ( \infty ) | \leq 1$ implies $k \leq j$ . By Proposition 3.4, $E ( y )$ must be of the form $K \cdot y ^ { 2 \mathcal { I } }$ . By letting $y  \infty$ in (3.6) and (3.9), we see that $| R ( \infty ) | \leq 1$ is equivalent to $K \geq 0$ ： □

# $\pmb { L }$ -Stability and $A ( \alpha )$ -Stability

The trapezoidal rule for the numerical integration of first-order ordinary differential equations is shown to possess, for a certain type of problem,an undesirable property. (A.R.Gourlay 1970)

$A$ -stability is not the whole answer to the problem of stiff equations. (R.Alexander 1977)

Some of the above methods seem to be optimal in the sense that the stability region coincides exactly with the negative half-plane. This property is not as desirable as it may appear, since for a rational function

$$
\operatorname* { l i m } _ { z \to - \infty } R ( z ) = \operatorname* { l i m } _ { z \to \infty } R ( z ) = \operatorname* { l i m } _ { z = i y , y \to \infty } R ( z ) .
$$

The latter must then be 1 in modulus,since $| R ( i y ) | = 1$ for all real $y$ . This means that for $z$ close to the real axis with a very large negative real part, $| R ( z ) |$ is, although $< 1$ ,very close to one. As a consequence, stiff components in (2.6) are damped out only very slowly. We demonstrate this with the example

$$
y ^ { \prime } = - 2 0 0 0 ( y - \cos x ) , \qquad y ( 0 ) = 0 , \qquad 0 \leq x \leq 1 . 5 ,
$$

which is the same as (1.1),but with increased stiffness. The numerical results for the trapezoidal rule are compared to those of implicit Euler in Fig.3.2. The implicit Euler damps out the transient phase much faster than the trapezoidal rule. It thus appears to be a desirable property of a method that $| R ( z ) |$ be much smaller than 1 for $z  - \infty$

Definition 3.7 (Ehle 1969). A method is called $L$ -stable if it is $A$ -stable and if in addition

$$
\operatorname* { l i m } _ { z \to \infty } R ( z ) = 0 .
$$

![](images/ed181cd056c8c6963a8ca3fea569aed72d3586cc76de3a39c88e5d5fa3533a19.jpg)  
Fig.3.2. Trapezoidal rule versus implicit Euler on (3.11)

Among the methods of Table 3.1,the implicit Euler, the SDIRK method (e) with $\gamma = ( \bar { 2 } \pm \sqrt { 2 } ) / 2$ , as well as the Radau IIA formula (j) are $I$ -stable.

Proposition 3.8. If an implicit Runge-Kutta method with nonsingular $A$ satisfies one of the following conditions:

$$
\begin{array} { r } { a _ { s , } = b _ { _ { \jmath } } \quad j = 1 , \ldots , s , } \\ { a _ { \imath 1 } = b _ { 1 } \quad i = 1 , \ldots , s , } \end{array}
$$

then $R ( \infty ) = 0$ . This makes $A$ -stable methods $I$ -stable.

Proof. By (3.2)

$$
R ( \infty ) = 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 }
$$

and (3.13) means that $A ^ { T } e _ { s } = b$ where $e _ { s } = ( 0 , \ldots , 0 , 1 ) ^ { T }$ . Therefore $R ( \infty ) =$ $1 - e _ { s } ^ { T } \mathbb { 1 } = 1 - 1 = 0$ . In the case of (3.14) use $A e _ { \mathbf { 1 } } = \mathbb { 1 } b _ { \mathbf { 1 } }$ □

Methods satisfying (3.13） are called stiffly accurate (Prothero & Robinson 1974).They are important for the solution of singularly perturbed problems and for differential-algebraic equations (see Chapters VI and VII).

The definition of $A$ -stability is on the one hand too weak,as we have just seen, and on the other hand too strong in the sense that many methods which are not so bad at all are not $A$ -stable. The following definition is a little weaker and will be specially useful in the chapter on multistep methods.

Definition 3.9 (Widlund 1967). A method is said to be $A ( \alpha )$ -stable if the sector

$$
S _ { \alpha } = \{ z ; | \arg ( - z ) | < \alpha , \ z \neq 0 \}
$$

![](images/c2ed8a7632c0180941d178ec772ef86dfe09fcc626e026e134727cf692177ec3.jpg)

is contained in the stability region.

Forexaplethedaoimati $R _ { 0 3 } ( z ) = \left( 1 - z + { \frac { z ^ { 2 } } { 2 ! } } - { \frac { z ^ { 3 } } { 3 ! } } \right) ^ { - }$ 1 (see (3.29) below) is $A ( \alpha )$ -stable for $\alpha \leq 8 8 . 2 3 ^ { \circ }$

# Numerical Results

To show the effects of good stability properties on the stiff examples of Sect.IV.1, we choose the 3-stage Radau IIA formula (Table 5.6 of Sect.IV.5) which, as we have seen, is A-stable, $L$ -stable and of reasonably high order. It has been coded (Subroutine RADAU5 of the Appendix) and the details of this program will be discussed later (Sect.IV.8). This program integrates all the examples of Sect.IV.1 in a couple of steps and the plots of Fig.1.3 and Fig.1.5 show a clear difference.

The beam equation(1.10'） with $n = 4 0$ is integrated, with $R t o l = A t o l = 1 0 ^ { - 3 }$ (absolute) and smooth initial values,in 28 steps (Fig.3.3).

![](images/a65f68a655c68040adca3ac6a897419a1865fa0664a13ed2b025f4b1e8840c86.jpg)  
Fig. 3.3. RADAU5 on the beam (1.10'), every step drawn

![](images/20234a7e89dd745d4b68204318dd52f3ffb9a6e046c04fdecbec2bbef10cf479.jpg)  
Fig.3.4. RADAU5 on oscillatory beam with large Tol (107 steps,all drawn)

Since the Radau5 formula is $I$ -stable, the stability domain also covers the imaginary axis and large parts of the right half-plane $\mathbb { C } ^ { + }$ . This means that high oscillations of the true solution may be damped by the numerical method. This effect, sometimes judged undesirable (B. Lindberg (1974): “dangerous property ..."),may also be welcome to suppress uninteresting oscillations. This is demonstrated by applying RADAU5 with very large tolerance ( $\mathbf { \nabla } \cdot R t o l = A t o l = 1$ ）to the beam equation (1.10'） with $n = 1 0$ and the perturbed initial value $\theta _ { n } ( 0 ) = 0 . 4$ Here, the high oscillations soon disappear and the numerical solution becomes perfectly smooth (Fig.3.4). If, however, the tolerance requirement is increased, the program is forced to follow all the oscillations and the picture remains the same as in Fig. 1.11.

# Stability Functions of Order $\geq s$

Consider rational functions $R ( z ) = P ( z ) / Q ( z )$ ，where $Q ( 0 ) = 1$ , and both $P ( z )$ and $Q ( z )$ are polynomials of degree at most $s$ . If $R ( z )$ is an approximation of $e ^ { z }$ of order $\geq s$ , then is follows from (3.5) that

$$
e ^ { z } Q ( z ) = P ( z ) + C _ { 1 } z ^ { s + 1 } + C _ { 2 } z ^ { s + 2 } + \dots .
$$

Consequently, the polynomial $P ( z )$ and also the error constants $C _ { 1 } , C _ { 2 } , \ldots$ are uniquely determined in terms of the coefficients of $Q ( z )$ . For

$$
Q ( z ) = q _ { 0 } + q _ { 1 } z + q _ { 2 } z ^ { 2 } + . . . + q _ { s } z ^ { s } , \qquad q _ { 0 } = 1
$$

an expansion of $e ^ { z } Q ( z )$ into powers of $z$ yields

$$
\begin{array} { c } { { P ( z ) = q _ { 0 } + z \displaystyle \left( \frac { q _ { 0 } } { 1 ! } + \frac { q _ { 1 } } { 0 ! } \right) + z ^ { 2 } \displaystyle \left( \frac { q _ { 0 } } { 2 ! } + \frac { q _ { 1 } } { 1 ! } + \frac { q _ { 2 } } { 0 ! } \right) } } \\ { { + \ldots + z ^ { s } \displaystyle \left( \frac { q _ { 0 } } { s ! } + \frac { q _ { 1 } } { ( s - 1 ) ! } + \ldots + \frac { q _ { s } } { 0 ! } \right) , } } \end{array}
$$

and for the error constants

$$
\begin{array} { l } { { C _ { 1 } = \displaystyle \frac { q _ { 0 } } { ( s + 1 ) ! } + \frac { q _ { 1 } } { s ! } + \ldots + \frac { q _ { s - 1 } } { 2 ! } + \frac { q _ { s } } { 1 ! } } } \\ { { C _ { 2 } = \displaystyle \frac { q _ { 0 } } { ( s + 2 ) ! } + \frac { q _ { 1 } } { ( s + 1 ) ! } + \ldots + \displaystyle \frac { q _ { s - 1 } } { 3 ! } + \frac { q _ { s } } { 2 ! } . } } \end{array}
$$

The Polynomial $M ( { \pmb x } )$ . With help of the polynomial

$$
M ( x ) = q _ { s } + q _ { s - 1 } { \frac { x } { 1 ! } } + q _ { s - 2 } { \frac { x ^ { 2 } } { 2 ! } } + \ldots + q _ { 0 } { \frac { x ^ { s } } { s ! } }
$$

the formulas for $Q ( z )$ and $P ( z )$ become more symmetric. We have

$$
\begin{array} { l } { { Q ( z ) = M ^ { ( s ) } ( 0 ) + M ^ { ( s - 1 ) } ( 0 ) z + . . . + M ( 0 ) z ^ { s } } } \\ { { P ( z ) = M ^ { ( s ) } ( 1 ) + M ^ { ( s - 1 ) } ( 1 ) z + . . . + M ( 1 ) z ^ { s } , } } \end{array}
$$

and the error constants are given by

$$
C _ { 1 } = \int _ { 0 } ^ { 1 } M ( x ) d x , \qquad \quad C _ { 2 } = \int _ { 0 } ^ { 1 } ( 1 - x ) M ( x ) d x .
$$

For the stability function of collocation methods we have the following nice result.

Theorem 3.10 (K. Wright 1970, S.P. Norsett 1975). The stability function of the collocation method based on the points $c _ { 1 } , c _ { 2 } , \ldots , c _ { s }$ is given by $R ( z ) =$ $P ( z ) / Q ( z )$ ， where $Q ( z )$ and $P ( z )$ are the polynomials of (3.22) and (3.23), respectively, with $M ( x ) ~ g i \nu e n ~ b y$

$$
M ( x ) = { \frac { 1 } { s ! } } \prod _ { \ i = 1 } ^ { s } ( x - c _ { \ i } ) .
$$

Proof (Ngrsett & Wanner 1979). We assume $x _ { 0 } = 0 , h = 1 , \lambda = z , y _ { 0 } = 1$ and let $u ( x )$ be the collocation polynomial. Since $u ^ { \prime } ( x ) - z u ( x )$ is a polynomial of degree $s$ which vanishes at the collocation points, there are constants $K _ { 0 }$ and $\kappa$ such that

$$
u ^ { \prime } ( x ) - z u ( x ) = K _ { 0 } M ( x ) \qquad { \mathrm { o r } } \qquad \bigl ( 1 - { \frac { D } { z } } \bigr ) u ( x ) = K M ( x )
$$

with the polynomial $M ( x )$ of (3.25) ( $D$ denotes the differentiation operator). Expanding $( 1 - D / z ) ^ { - 1 }$ into a geometric series yields

$$
u ( x ) = K \Big ( 1 + \frac { D } { z } + \frac { D ^ { 2 } } { z ^ { 2 } } + \ldots + \frac { D ^ { s } } { z ^ { s } } \Big ) M ( x ) ,
$$

because $M ^ { ( j ) } ( x ) \equiv 0$ for $j > s$ .From $u ( 1 ) = R ( z ) u ( 0 )$ we have the relation $R ( z ) = u ( 1 ) / u ( 0 )$ ,which leads to (3.22) and (3.23). □

# Padé Approximations to the Exponential Function

Comme cela est souvent le cas en ce qui concerne les découvertes scientifiques, leur inventeur n'est pas H. Padé.

(C. Brezinski 1984, Euvres de H. Padé, p. 5)

Padé approximations (Padé 1892) are rational functions which, for a given degree of the numerator and the denominator, have highest order of approximation. Their origin lies in the theory of continued fractions and they played a fundamental role in Hermite's (1873) proof of the transcendency of $e$

These optimal approximations can be obtained for the exponential function $e ^ { z }$ from (3.22) and (3.23) by the following idea (Padé 1899): choose $M ( x )$ such that in (3.22) and (3.23) as many terms as possible involving high powers of $z$ become zero, i.e.,

$$
M ( x ) = \frac { x ^ { k } ( x - 1 ) ^ { \jmath } } { ( k + j ) ! } ;
$$

then $M ^ { ( i ) } ( 0 ) = 0$ for $i = 0 , \ldots , k - 1$ and $M ^ { ( \imath ) } ( 1 ) = 0$ for $i = 0 , \ldots , j - 1$

Theorem 3.11. The $( k , j )$ -Padé approximation to $e ^ { z }$ is given by

$$
R _ { k j } ( z ) = { \frac { P _ { k j } ( z ) } { Q _ { k j } ( z ) } }
$$

where

$$
\begin{array} { l } { { P _ { k j } ( z ) = 1 + \displaystyle \frac { k } { j + k } z + \displaystyle \frac { k ( k - 1 ) } { ( j + k ) ( j + k - 1 ) } \cdot \displaystyle \frac { z ^ { 2 } } { 2 ! } + . . . + \displaystyle \frac { k ( k - 1 ) . . . 1 } { ( j + k ) . . . ( j + 1 ) } \cdot \displaystyle \frac { z ^ { k } } { k ! } } } \\ { { Q _ { k j } ( z ) = 1 - \displaystyle \frac { j } { k + j } z + \displaystyle \frac { j ( j - 1 ) } { ( k + j ) ( k + j - 1 ) } \cdot \displaystyle \frac { z ^ { 2 } } { 2 ! } - . . . + ( - 1 ) ^ { j } \displaystyle \frac { j ( j - 1 ) . . . 1 } { ( k + j ) . . . ( k + 1 ) } \cdot \displaystyle \frac { z ^ { j } } { j ! } } } \\ { { = P _ { j k } ( - z ) , } } \end{array}
$$

with error

$$
e ^ { z } - R _ { k j } ( z ) = ( - 1 ) ^ { \jmath } \frac { j ! k ! } { ( j + k ) ! ( j + k + 1 ) ! } z ^ { \jmath + k + 1 } + { \mathcal O } ( z ^ { \jmath + k + 2 } ) .
$$

It is the unique rational approximation to $e ^ { z }$ of order $j + k$ ， such that the degrees of numerator and denominator are $k$ and $j$ , respectively.

Table 3.2. Padé approximations for $e ^ { z }$   

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1+1</td><td rowspan=1 colspan=1>1+2+321</td></tr><tr><td rowspan=1 colspan=1>11-z</td><td rowspan=1 colspan=1>1+21-</td><td rowspan=1 colspan=1>1+2+1221-</td></tr><tr><td rowspan=1 colspan=1>11-2+2</td><td rowspan=1 colspan=1>1+22+2112</td><td rowspan=1 colspan=1>122！12+1心1-2</td></tr><tr><td rowspan=2 colspan=1>15   美1-z+</td><td rowspan=1 colspan=1>1+2</td><td rowspan=2 colspan=1>1+2+1江1021-2+ 32      1 3-</td></tr><tr><td rowspan=1 colspan=1>12    132！云3</td></tr></table>

Proof. Inserting (3.28) into (3.22)and (3.23) gives the formulas for $P _ { k _ { \mathcal { I } } } ( z ) , Q _ { k _ { \mathcal { I } } } ( z )$ and (3.3O). The uniqueness is a consequence of the fact that the $( j ^ { - } + k )$ -degree polynomial $M ( x )$ of (3.21) must have a zero of multiplicity $k$ at $x = 0$ ,and one of multiplicity $j$ at $x \approx 1$ □

Table 3.2 shows the first Padé approximations to $e ^ { z }$ . We observe that the stabil-ity function of many methods of Table 3.1 are Padé approximations. The diagonal Padé approximations are those with $k = j$

# Exercises

1. Let $R ( z )$ be the stability function of (3.1) and $R ^ { * } ( z )$ the stability function of its adjoint method (see Sect. I.8). Prove that

$$
R ^ { * } ( z ) = \left( R ( - z ) \right) ^ { - 1 } .
$$

2. Consider an implicit Runge-Kutta method of order $p \geq s$ with nonsingular $A$ ， distinct $c _ { i }$ and non-zero $b _ { i }$ . Show

a)If $C ( s )$ and $c _ { s } = 1$ then (3.13);   
b) If $D ( s )$ and $c _ { 1 } = 0$ then (3.14).

In both cases the stability function satisfies $R ( \infty ) = 0$ ·

(For the definition of the assumptions $C ( s )$ and $D ( s )$ see Sect. IV.5).

3． Show that collocation methods can only be $L$ -stable if $\mathcal { M } ( 1 ) = 0$ ,i.e., if one of the $c ^ { * } s$ ,usually $c _ { s }$ , equals 1.

4. (Padé (1899), see also Lagrange (1776)). Show that the continued fraction

$$
e ^ { x } = 1 + { \cfrac { x } { 1 - { \cfrac { x } { 2 } } + { \cfrac { { \frac { 1 } { 1 \cdot 3 } } { 4 } } { 1 + { \cfrac { { \frac { 1 } { 3 \cdot 5 } } { 1 + { \cfrac { { \frac { 1 } { 5 \cdot 7 } } { 1 + { \cfrac { x ^ { 2 } } { 4 } } } } } } { 1 + { \cfrac { { \frac { 1 } { 7 \cdot 9 } } { 1 + \ddots } } } } } } } } } } 
$$

leads to the diagonal Padé approximations for $e ^ { x }$

Hint. Compute the first partial fractions. If you don't succeed in finding a general proof, read Sect. IV.5.

5．The trapezoidal rule

$$
\frac { 0 } { 1 } \textcircled { 1 / 2 } \frac { 0 } { 1 / 2 }
$$

satisfies $a _ { s i } = b _ { i }$ ，but not $R ( \infty ) = 0$ . Why doesn't this contradict Proposition 3.8?

6. Show that

$$
\begin{array} { l } { y _ { 1 } = y _ { 0 } + h f ( y _ { 0 } + \theta ( y _ { 1 } - y _ { 0 } ) ) } \\ { y _ { 1 } = y _ { 0 } + h ( 1 - \theta ) f ( y _ { 0 } ) + h \theta f ( y _ { 1 } ) } \end{array}
$$

are both nonlinear extensions of the $\theta$ -method. Find others.

7. The composition of a step of the $\theta$ -method with step-size $\alpha h$ , followed by a $\theta ^ { \prime }$ -method with step-size $( 1 - 2 \alpha ) h$ and again a $\theta$ -method with step-size $\alpha h$ leads to

$$
R ( z ) = \Big ( \frac { 1 + \alpha z ( 1 - \theta ) } { 1 - \alpha z \theta } \Big ) ^ { 2 } \Big ( \frac { 1 + ( 1 - 2 \alpha ) z ( 1 - \theta ^ { \prime } ) } { 1 - ( 1 - 2 \alpha ) z \theta ^ { \prime } } \Big )
$$

Show that this method, for $\theta ^ { \prime } = 1 - \theta$ , is of order 2 if $\alpha = 1 - \sqrt { 2 } / 2$ and strongly $A$ -stable (i.e., $A$ -stable and $| R ( \infty ) | < 1 )$ for $\theta > 1 / 2$ . The authors Muller, Prohl, Rannacher & Turek(1994) call this method “fractional $\theta$ method" and use it successfully for computations of the incompressible Navier-Stokes equations.

Mein hochgeehrter Lehrer, der vor wenigen Jahren verstorbene Geheime Hofrath Gauss in Gottingen,pflegte in vertraulichem Gespräche häufig zu äussern, die Mathematik sei weit mehr eine Wissenschaft fur das Auge als eine fir das Ohr. Was das Auge mit einem Blicke sogleich übersieht...

(J.F Encke 1861, publ. in Kronecker's Werke, Vol. 5, page 391)

Order stars, discovered by searching for a better understanding of the stability properties of the Padé approximations to $e ^ { z }$ (Wanner, Hairer & Ngrsett 1978), offered nice and unexpected access to many other results: the “second barrier’ of Dahlquist, the Daniel & Moore conjecture, highest possible order with real poles, comparison of stability domains (Jeltsch & Nevanlinna 1981,1982),order bounds for hyperbolic or parabolic difference schemes (e.g., Iserles & Strang 1983, Iserles & Williamson 1983, Jeltsch 1988).

# Introduction

When I wrote my book in 1971 I wanted to draw “relative stability domains",but curious stars came out from the ploter. I thought of an error in the program and I threw them away ...

(C.W. Gear, in 1979)

We present in Fig.4.1 the stabilitydomains forthePadéapproximations $R _ { 3 3 } , R _ { 2 4 }$ ， $R _ { 1 5 } , R _ { 0 6 }$ of Theorem 3.12,which are all 6th order approximations to $\exp ( z )$ .It can be observed that $R _ { 3 3 }$ and $R _ { 2 4 }$ are nicely $A$ -stable. The other two are not, $R _ { 1 5 }$ violates (3.6) and $R _ { 0 6 }$ violates (3.7). After some meditation on these and similar figures, trying to obtain a better understanding of these phenomena, one is finally led to

Definition 4.1. The set

$$
A = \left\{ z \in \mathbb { C } \ ; \ | R ( z ) | > | e ^ { z } | \right\} = \left\{ z \in \mathbb { C } \ ; \ | q ( z ) | > 1 \right\}
$$

where $q ( z ) = R ( z ) / e ^ { z }$ ,is called the order star of $R$

The order star does not compare $| R ( z ) |$ to 1,as does the stability domain, but to the exact solution $| e ^ { z } | = e ^ { x }$ and it is hoped that this might give more information. As we always assume that the coefficients of $R ( z )$ are real, the order star is symmetric with respect to the real axis. Furthermore, since $\left| e ^ { \imath y } \right| = 1$ ， $A$ is the complementary set of the stability domain $S$ on the imaginary axis. Therefore we have from (3.6) and (3.7):

![](images/40ff5c4015188dd835575b4e35d32b5e2ce273d02192c108b432b7c1060decd6.jpg)  
Fig. 4.1. Stability domains for Padé approximations

Lemma 4.2. $R ( z )$ is $I$ -stable if and only if (i） $A \cap i \mathbb { R } = \emptyset$ ·   
Further, $R ( z )$ is $A$ -stable if and only if (i) and (ii) all poles of $R ( z )$ $\risingdotseq$ poles of $q ( z ) )$ lie in the positive half plane $\mathbb { C } ^ { + }$

Fig.4.2 shows the order stars corresponding to the functions of Fig.4.1. These order stars show a nice and regular behaviour: there are $j$ black “fingers” to the right, each containing a pole of $R _ { k j }$ , and $k$ white“fingers"to the left, each containing a zero. Exactly two boundary curves of $A$ tend to infinity near to the imaginary axis. These properties are a consequence of the following three Lemmas.

Lemma 4.3. If $R ( z )$ is an approximation to $e ^ { z }$ of order $\mathfrak { p }$ ,i.e.,if

$$
e ^ { z } - R ( z ) = C z ^ { p + 1 } + \mathcal { O } ( z ^ { p + 2 } )
$$

![](images/b993829742e18f9360cb2e06941dfce6015da60c919b9b2cd24f5fc9cbf21a7f.jpg)  
Fig.4.2. Order stars for Padé approximations

with $C \neq 0$ , then, for $z  0$ ， $A$ behaves like $a$ “star”with $p + 1$ sectors of equal width $\pi / ( p + 1 )$ ， separated by $p + 1$ similar “white" sectors ofthe complementary set. The positive real axis is inside a black sector iff $C < 0$ and inside a white sector ff $C > 0$

Proof. Dividing the error formula (4.2) by $e ^ { z }$ gives

$$
\frac { R ( z ) } { e ^ { z } } = 1 - C z ^ { p + 1 } + \mathcal { O } ( z ^ { p + 2 } ) .
$$

Thus the value $R ( z ) / e ^ { z }$ surrounds the point 1 as often as $z ^ { p + 1 }$ surrounds the origin, namely $p + 1$ times. So, $R ( z ) / e ^ { z }$ is $p + 1$ times alternatively inside or outside the unit circle. It lies inside for small positive real $z$ whenever $C > 0$ □