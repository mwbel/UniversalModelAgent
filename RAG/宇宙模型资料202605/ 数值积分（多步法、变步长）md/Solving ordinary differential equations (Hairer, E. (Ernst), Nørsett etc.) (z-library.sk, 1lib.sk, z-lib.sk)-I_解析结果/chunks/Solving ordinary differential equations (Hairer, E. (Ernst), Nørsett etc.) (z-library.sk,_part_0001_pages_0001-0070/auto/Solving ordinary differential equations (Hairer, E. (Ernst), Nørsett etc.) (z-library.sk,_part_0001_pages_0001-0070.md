E.Hairer S.P.Norsett G.Wanner

# Solving Ordinary Differential Equations I

Nonstiff Problems

![](images/1e219142e2b4c22c22c8d742c675b422c1668436822a499a55dfafa44a1020d2.jpg)

# Springer Series in Computational Mathematics

8

Editorial Board

R.L. Graham, Murray Hill J. Stoer, Wurzburg R. Varga, Cleveland

Digitized by the Internet Archive in 2022 with funding from Kahle/Austin Foundation

E. Hairer S.P. Norsett G. Wanner

$$
\begin{array} { l } { \mathsf { S o l v i n g O r d i n a n y } } \\ { \mathsf { D i f f e r e n t i a l } } \\ { \mathsf { E q u a t i o n s I } } \\ { \mathsf { N o n s i i f f e r o b l e m s } } \end{array}
$$

With 105 Figures

Ernst Hairer

Gerhard Wanner

Université de Geneve, Section de Mathématiques, C.P. 240, CH-1211 Geneve 24, Switzerland

Syvert Paul Norsett   
Department of Numerical Mathematics,   
University of Trondheim,NTH   
N-7034 Trondheim,Norway

Hairer, E.

Solving ordinary differential equations

ISBN 3-540-17145-2 Springer-Verlag Berlin Heidelberg NewYork ISBN0-387-17145-2Springer-Verlag NewYork Berlin Heidelberg

This work is subject to copyright. All rights are reserved, whether the whole or part of thematerial isconcerned,specifically those of translation,reprinting,re-use of illustrations,broadcasting,reproduction by photocopying machine or similar means, and storage in data banks. Under S 54 of the German Copyright Law where copies are made for other than privateuse,a fee ispayable to“Verwertungsgeselschaft Wort", Munich.

# Preface

"So far as I remember, I have never seen an Author's Preface which had any purpose but one-to furnish reasons for the publication of the Book."   
（Mark Twain）

"Gauss' dictum,"when a building is completed no one should beable to see any trace of the scaffolding,"is often used by mathematicians as an excuse for neglecting the motivation behind their own work and the history of their field.Fortunately, the opposite sentiment is gaining strength,and numerous asides in this Essay show to which side go my sympathies."

(B.B. Mandelbrot, 1982)

This gives us a good occasion to work out most of the book until the next year."

(the Authors ina letter,dated Oct.29,1980,to Springer Verlag)

There are two volumes, one on non-stiff equations, now finished, the second on stiff equations, in preparation. The first volume has three chapters, one on classical mathematical theory,one on Runge-Kutta and extrapolation methods, and one on multistep methods. There is an Appendix containing some Fortran codes which we have written for our numerical examples.

Each chapter is divided into sections. Numbers of formulas, theorems, tables and figures are consecutive in each section and indicate,in addition, the section number, but not the chapter number. Cross references to other chapters are rare and are stated explicitly. The end of a proof is denoted by "QED"(quod erat demonstrandum). Since this becomes somewhat ridiculous when there is no proof at all or when the proof precedes the statement of the theorem, we wrote NED"(nihil erat demonstrandum) in these cases. References to the Bibliography are by "Author" plus "year"in parentheses.The Bibliography makes no attempt at being complete; we have listed mainly the papers which are discussed in the text.

Finally, we want to thank all those who have helped and encouraged us to prepare this book. The marvellous "Minisymposium" which G. Dahlquist organized in Stockholm in 1979 gave us the first impulse for writing this book. J. Steinig and Chr. Lubich have read the whole manuscript very carefully and have made extremely valuable mathematical and linguistical suggestions. We also thank J.P. Eckmann for his troff software with the help of which the whole manuscript has been printed. For preliminary versions we had

used textprocessing programs written by R. Menk. Thanks also to the staff of the Geneva computing center for their help. All computer plots have been done on their beautiful HP plotter. Last but not least,we would like to acknowledge the agreable collaboration with the planning and production group of Springer-Verlag.

# Contents

# Chapter I. Classical Mathematical Theory

1.1. Terminology I.2. The Oldest Differential Equations 1 Newton..   
Leibniz ·... Variational Calculus 7 Clairaut .... 8 I.3. Equations Solvable by Quadrature and Elementary Functions ........ 10 Equation with separable variable.. 10 Inees iaation 100 Second order equations 11 Exercises ........ 12 I.4. Linear Differen tial Equations s · · . 15 aationwistatciients 15 Exercises 18 I.5. Equations with Weak Singularities 20 Linear equations   
Nonlinear equations   
Exercises......   
I.6. S ys tems of Equations   
Pone I.7. A General Exis tence Theorem   
Convergence of Euler's method   
Existence theorem of Peano   
Exercises   
1.8EteeeUsineMesanlerie 41 Taylor series 43 Convergence prof.. = s 44 Recursive computation of Taylor coefficients 45 Exercises 47 I.9. Existence Theory for Systems of Equations Vector notation...   
Subordinate matrix norms   
Picard iteration for systems   
Exercises. .........\*\*.-...\*.\*...\*...\*\*.....\*\*\*.\*\*\* · 1.10. Differential Inequalities S.   
Introduction

The fundamental theorems 55   
Estimations using one-sided Lipschitz conditions   
Exercises   
I.11. Systems of Linear Differential Equations... 63   
The Wronskia.n... 64   
The Abel-Liouville-Jacobi-Ostrogradskii identity 65   
Inhomogeneous linear equations 66   
Exercises 66   
I.12. Systems with Constant Coefficients 69   
Linearization 69   
Diagonalization 69   
The Schur decomposition 70   
Numerical computations 72   
The Jordan canonica fom 74   
Exercises .\*........................................ 78   
1.13. Stability 81   
Introduction 81   
The Routh-Hurwitz criterion 82   
Computational considerations 86   
Liapunov functions 87   
Stability of nonlinear systems.. 89   
Stability of non-autonomous systems 90   
Exercises... 91   
I.14. Derivatives with Respect to Parameters and Initial Values 94   
The derivative with respect to a parameter 95   
Derivatives with respect to initial values 97   
The nonlinear variation-of-constants formula 98   
Exercises .... 100   
I.15. Boundary Value and Eigenvalue Problems 101   
Boundary value problems 101   
Sturm-Liouville eigenvalue problems ..... 103   
Exercises..... 106   
I.16. Periodic Solutions, Limit Cycles, Strange Attractors 107   
Van der Pol's equation 107   
Existence proof (Poincare sections) s o · 107   
Steady-state approximations for e large 109   
Asymptotic solutions for e small 110   
Chemical reactions (The Brusselator) 111   
Limit cycles in higher dimensions, Hopf bifurcation .............. 113   
Stragene aumactrsdes 117   
Exercises... 123

# Chapter II. Runge-Kutta and Extrapolation Methods

I1.1. The First Runge-Kutta Methods 130   
General formulation of Runge-Kutta methods 132   
Discussion of methods of order 4 133

Contents ix

"Optimal" formulas 137   
Numerical example 139   
Exercises 140

I.2. Order Conditions for RK Methods 142

The derivatives of the true solution 144   
Conditions for order 3 144   
Trees and elementary differentials 144   
The Taylor expansion of the true solution 146   
Faa di Bruno's formula 148   
The derivatives of the numerical solution 150   
The order conditions 153   
Exercises 154

# [I.3. Error Estimation and Convergence for RK Methods 156

Rigorous error bounds 156   
The principal error term 158   
Estimation of the global error 159   
Exercises 163

# II.4. Practical Error Estimation and Step Size Selection 165

Richardson extrapolation 165   
Automatic step size control 166   
Embedded RK formulas 167   
The formula of Dormand and Prince 171   
Numerical study of the step-control mechanism 172   
Numerical comparison of 4th-order methods 174   
Exercises.... 174

I1.5. Further Questions of Practical Computation 176

Dense output 176   
Continuous embedded formulas 179   
Implicit output 180   
Discontinuous equations 180   
Starting step-size 182   
Numerical computation of derivatives with respect to initial values   
and parameters 183   
Exercises 184

# I1.6. Explicit RK-Methods of Higher Order 185

The Butcher barriers 6 stage, 5th order processes 8 # n 185 186   
7 stage, 6th order processes 188   
Further Butcher barriers 189   
A 10-th order formula 189   
Embedded formulas of high order 193   
A numerical example 196   
Exercises 196

II.7. Implicit Runge-Kutta Methods 199

Introduction .·· . 199   
Existence of numerical solution 201   
The methods of Kuntzmann and Butcher of order 2s 203   
IRK methods based on Lobatto quadrature 204   
IRK as collocation methods 206   
Exercises 209

I1.8. Asymptotic Expansion of the Global Error 211

The local error 211   
The global error 211   
Examples 213   
Variable h 213   
Negative h 214   
Properties of the adjoint method 215   
Symmetric methods 216   
Exercises 217

I1.9. Extrapolation Methods 219

Definition of the method 219   
The Aitken-Neville algorithm 221   
Rational extrapolation 221   
A numerical example 222   
Extrapolation with symmetric methods 223   
The Gragg or GBS method 224   
The smoothing step 225   
Numerical algorithm and example 226   
Asymptotic expansion for odd indices 226   
Existence of explicit RK methods of arbitrary order 228   
Order and step size control 228   
Numerical study of the combined step size and order control 231   
Exercises 232

II.10. Numerical Comparisons 236

Numerical resuits 238   
A discontinuous ex ample 239   
Conclusion 241

II.11. Composition of B-Series 242

Composition of RK methods 242   
B-series 243   
Order conditions for RK methods 247   
Butcher's "effective order" 247   
Exercises 248

I1.12. Higher Derivative Methods 250

Collocation methods 251   
Obreschkoff methods 253   
Fehlberg methods 254   
General theory of order conditions 256   
Exercises 258

# I1.13. Numerical Methods for Second Order Differential Equations.... 260

=

Thederieveof theexact soluton 262   
The derivatives of the numerical solution 265   
The order conditions 267   
On the construction of Nystrom methods 268   
Global convergence 270   
Implementation of Nystrom methods 271   
An extrapolation method for $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ 271   
Numerical comparisons 273   
Higher order systems 274   
Exercises 275   
I1.14. P-Series for Partitioned Ordinary Differential Equations 276   
Derivatives of the exact solution, P-trees 277   
P-series 280   
RK-methods violating (1.9) 282   
Fehlberg methods 283   
Nystrom methods 283   
Exercises.. 285   
II.15. Delay Differential Equations 286   
Existence 286   
Constant step size methods for constant delay 288   
Variable step size methods. 289   
Characteristic values of exponential solutions 290   
Stability....... 291   
An example from population dynamics 292   
Infectious disease modellng 294   
An example from enzyme kinetics 295   
A mathematical model in immunology 297   
Integro-differential equations 299   
Exercises 300

# Chapter III. Multistep Methods and General Linear Methods

III.1. Classical Linear Multistep Formulas 304   
Explicit Adams methods 305   
Implicit Adams methods 306   
Recurrence relations for the $\boldsymbol { \gamma } _ { i }$ 308   
Explicit Nystrom methods 309   
Milne-Simpson methods 310   
Methods based on differentiation (BDF) 311   
Exercises 313   
I11.2. Local Error and Order Conditions 315   
Local error of a multistep method 315   
The rder oeeo 由 b 317   
Irreducible methods \* + ± 321   
The Peano kernel of a multistep method 322   
Exercises 324   
III.3. Stability and the First Dablquist Barrier 326   
Stability of the BDF-formulas 328   
Highest attainable order of stable multistep methods 331   
Exercises 335   
III.4. Convergence of Multistep Metbods 340   
Formulation as one-step method 342   
Proof of convergence 344   
Exercises ..... 345   
III.5. Variable Step Size Multis tep Methods 347   
Variable step size Adams methods 347   
Recurrence relations $g _ { j _ { c } } ( n ) , \Phi _ { j } ( n )$ and $\Phi _ { j } ^ { * } ( n )$ 349   
Variable step size BDF-formulas 350   
General variable step size methods and their order 351   
Stability 352   
Convergence 357   
Exercises 359

III.6. Nordsieck Methods 360

Equivalence with multistep methods 363   
Implicit Adams methods 368   
BDF-methods 369   
Exercises 370

# III.7. Implementation and Numerical Comparisons 372

Step size and order selection 372   
Some available codes 374   
Numerical comparisons 378   
A partial differential equation 381

III.8. General Linear Methods 385

A general integration procedure 386   
Examples of method (8.4) 386   
Stability and order 391   
Convergence 394   
Order conditions for general linear methods 396   
Construction of general linear methods 399   
Exercises 401

III.9. As ymptotic Expansion of the Global Error 403

An instructive example 403   
Asymptotic expansion for strictly stable methods (8.4) 405   
Weakly stable methods 409   
The adjoint method 412   
Symmetric methods 415   
Exercises 416

# III.10. Multistep Methods for Second Order Differential Equations 418

The first methods 419   
Stormer's problem 420   
Higher order methods 421   
General formulation 424   
The stability condition 424   
A one-step formulation of method (10.19) 425   
Consistency and convergence 426   
Asymptotic formula for the global error 428   
An order barrier for stable methods (10.19) 429   
Rounding errors 430   
Exercises 430

# Appendix. Fortran Codes

1. Dopri5 433   
2. Dopri8 435   
3. Odex 440   
4. Odex2 443

Contents xii

5.Doprin 447   
6. Retard,Store and Ylag 450

Bibliograpby 455

Symb...x.. 473

Subject Index 475

# CHAPTER I CLASSICAL MATHEMATICAL THEORY

"... halte ich es immer fur besser, nicht mit dem Anfang anzufangen, der immer das Schwerste ist." (B.Riemann copied this from F.Schiller into his notebook)

This first chapter contains the classical theory of differential equations,which we judge useful and important for a profound understanding of numerical processes and phenomena. It will also be the occasion of presenting interesting examples of differential equations and their properties.

We first retrace in Sections I.2-I.6 the historical development of classical integration methods by series expansions, quadrature and elementary functions, from the beginning (Newton and Leibniz) to the era of Euler and Lagrange. The next part (Sections I.7-I.14) deals with theoretical properties of existence， uniqueness， stability， continuity and differentiability of the solutions. This theory was initiated by Cauchy in 1824 and then developed to perfection mainly during the next ioo years. We close with a brief account of boundary value problems, periodic solutions, limit cycles and strange attractors (Sections I.15 and I.16).

# 1.1. Terminology

A differential equation of the first order is an equation of the form

$$
y ^ { \prime } = f \left( x , y \right)
$$

with a given function $f \left( x , y \right)$ . A function $y \left( x \right)$ is called a solution of this equation if for all $x$ ，

$$
y ^ { \prime } ( x ) = f \left( x , y ( x ) \right) .
$$

It was observed very early by Newton, Leibniz and Euler that the solution usually contains a free parameter, so that it is only uniquely determined when an initial value

$$
y ( x _ { 0 } ) = y _ { 0 }
$$

is prescribed. Cauchy's existence and uniqueness proof of this fact will be discussed in Section I.7. Differential equations arise in many applications. We shall see in Section I.2 how the first equations arose

in mechanics, and in Section I.3 how some of them can be solved explicitly.

A differential equation of the second order for $y$ is of the form

$$
y ^ { \prime \prime } = f \left( x , y , y \right) .
$$

Here, the solution usually contains two parameters and is only uniquely determined by two initial values

$$
y \left( x _ { 0 } \right) = y _ { 0 } \ \cdot \ \cdot \qquad y ^ { \prime } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } \ .
$$

Equations of the second order can rarely be solved explicitly (see I.3). For their numerical solution, as wel as for theoretical investigations, one usually sets $y _ { 1 } ( x ) { : = } y \left( x \right)$ ， $y _ { 2 } ( x ) { : = } y ^ { \prime } ( x )$ ， so that Equation (1.4) becomes

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = y _ { 2 } } & & { y _ { 1 } ( x _ { 0 } ) = y _ { 0 } } \\ & { y _ { 2 } ^ { \prime } = f \left( x , y _ { 1 } , y _ { 2 } \right) } & & { y _ { 2 } ( x _ { 0 } ) = y _ { 0 } ^ { \prime } . } \end{array}
$$

This is an example of a first order system of differential equations， of dimension $_ { n }$ (see Sections I.6 and 1.9),

$$
y _ { 1 } ^ { \prime } = f _ { 1 } ( x , y _ { 1 } , . . . , y _ { n } ) \qquad y _ { 1 } ( x _ { 0 } ) = y _ { 1 0 }
$$

$$
y _ { n } ^ { \prime } = f _ { n } ( x , y _ { 1 } , . . . , y _ { n } ) \qquad y _ { n } ( x _ { 0 } ) = y _ { n 0 } .
$$

Most of the theory of this book is devoted to the solution of the initial value problem for the system (1.6). At the end of the 19th century (Peano (1890)） it became customary to introduce the vector notation

$$
y = \left( y _ { 1 } , , . . . , y _ { n } \right) ^ { T } , f = \left( f _ { 1 } , . . . , f _ { n } \right) ^ { T }
$$

so that (1.6) becomes $y \prime = f \left( x , y \right)$ , which is again the same as (1.1), but now with y and $f$ interpreted as vectors.

Another possibility for the second order equation (1.4), instead of transforming it into a system $( 1 . 4 ^ { \circ } )$ , is to develop methods specially adapted to second order equations (Nystrom methods). This will be done in special sections of this book. Nothing prevents us, of course, from considering (1.4) as a system of second order equations of dimension n.

If, however， the initial conditions (1.5) are replaced by something like $y \left( x _ { 0 } \right) { = } a$ ， $y \left( x _ { 1 } \right) = b$ ， i.e.， when the conditions deter-mining the particular solution are not all specified at the same point $x _ { 0 }$ , we speak of a boundary value problem. The theory of the existence of a solution and of its numerical computation is here much more complicated. We give some exam ples in Section I.15.

Finally, a problem of the type

$$
{ \frac { \partial u } { \partial t } } = f \left( t , u , { \frac { \partial u } { \partial x } } \ , \ { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } \right)
$$

for an unknown function $u \left( t , x \right)$ of two independent variables will be called a partial differential equation. We can also deal with partial differential equations of higher order, with problems in three or four independent variables, or with systems of partial differential equations. Very often, initial value problems for partial differential equations can conveniently be transformed into a system of ordinary differential equations, for example with finite difference or finite ele-ment approximations in the variable $x$ . In this way, the equation

$$
{ \frac { \partial u } { \partial t } } = a ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

would become

$$
\frac { d u _ { i } } { d t } = \frac { a ^ { 2 } } { { \Delta x } ^ { 2 } } ( u _ { i + 1 } { - 2 u _ { i } } { + u _ { i - 1 } } ) \ .
$$

This is called "Rothe's method" (Rothe (1930)), or the "method of lines". We shall see in Section I.6 that this connection is very com-mon since the work of Lagrange.

# I.2. The oldest differential equations

So zum Beispiel die Aufgabe der umgekehrten Tangentenmethode, von welcher auch Descartes eingestand, dass er sie nicht in seiner Gewalt habe. (Leibniz, 27. Aug 1676) ... et on sait que Ies seconds Inventeurs n'ont pas de droit a 'Invention. (Newton, 29 mai 1716) Il ne paroist point que M. Newton ait eu avant moy la characteristique & 'algorithme infinitesimal.. (Leibniz) And by these words he acknowledged that he had not yet found the reduction of problems to differential equations. (Newton)

# Newton

Differential equations are as old as differential calculus. Newton considered them in his treatise on differential calculus (Newton (1671)） and discussed their solution by integration and by series expansion. One of the first examples of a first order equation treated by Newton (see Newton (1671), Problema II, Solutio Casus II, Ex.I) was

$$
y ^ { \prime } = 1 - 3 x + y + x ^ { 2 } + x y .
$$

For each value $x$ and y， such an equation prescribes the derivative $y ^ { \prime }$ of the solutions. We thus obtain a vector field, which, for this particular equation, is sketched in Figure 2.1. (So, contrary to the belief of many people, vector fields existed long before Van Gogh). The solutions are the curves which respect these prescribed directions everywhere.

Newton discusses the solution of this equation by means of infinite series, whose terms he obtains recursively (" .. & ils se jettent sur les series, ou M. Newton m'a precede sans dificulte; mais, Leibniz). The first term

$$
y ~ = 0 + \cdot \cdot \cdot
$$

is the initial value for $x = 0$ . Inserting this into the differential equation (2.1) he obtains

$$
y ^ { \prime } = 1 + \cdots
$$

which, integrated, gives

Sit Equatio 1-3x+y+xx+xy,cujus Terminog:

r- 3x+xx non affectos Relatd Quantitate difpofitos vides in lateralem Seriem primo loco，& reliquos y & x y in finiftra Columnd.

$$
\begin{array} { r l } &  \begin{array} { r } { + \ldots } \\ { + \ s } \\ { \left\lfloor \frac { \textstyle + x } { \textstyle + x - x x + \frac { 1 } { 3 } x ^ { 3 } - \frac { \tau } { 6 } x ^ { 4 } + \frac { 1 } { 3 0 } x ^ { 3 } ; \ \& \& } { \textstyle \mathcal { E } \mathrm { c } } \end{array} \right\} } \\ &  \begin{array} { r } { \frac { \textstyle + x y } { \textstyle \frac { \textstyle + x + x x - x ^ { 3 } + x ^ { 5 } + \frac { \tau } { 3 } x ^ { 4 } - \frac { \tau } { 6 } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 6 } ; \ \& \mathcal { E } \mathrm { c } } { \textstyle \frac { \textstyle + x - x y } { \textstyle \frac { \textstyle + x + x y } { \textstyle \frac { \textstyle + x + x y } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle \delta } { \delta } } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 6 } } } } } } } } } } \\  \frac { \textstyle + x - x x + x x - x ^ { 3 } + \frac { \tau } { 3 } x ^ { 3 } + \frac { \tau } { 3 } x ^ { 4 } - \frac { \frac { \tau } { \textstyle + x } x ^ { 5 } + \frac { \tau } { 3 0 } x ^ { 5 } ; \ \mathcal { E } \mathrm { c } . } } \\ { \eta = \left| + x - x x + \frac { 1 } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \textstyle + x } { \textstyle \frac { \delta } { \textstyle \delta } } x ^ { 9 } } } } } } + \frac { \tau } { 4 0 } x ^ { 5 } - \frac { \tau } { \textstyle \frac { \mathrm { 1 } } { \textstyle + x } } x ^ { 6 } ; \ \& \mathcal { E } \mathrm { c } . } \end{array}  } \end{array} } \end{\right|array}
$$

Nuno:

![](images/a72b7444f3b77ee5331509ab8a8fa2745168b0e14bb9b5e3f0e1cea0f2e9161a.jpg)  
Figure 2.1. a) Correct solution vs. approximate solution, b) vector field, c) various solution curves of Equation (2.1)

$$
y = x + \cdots .
$$

Again, from (2.1), we now have

$$
y ^ { \prime } = 1 - 3 x + x + \cdot \cdot \cdot = 1 - 2 x + \cdot \cdot \cdot
$$

and by integration

$$
y = x - x ^ { 2 } + \cdots ,
$$

The next round gives

$$
y ^ { \prime } = 1 - 2 x + x ^ { 2 } + \cdot \cdot \cdot , \qquad y = x - x ^ { 2 } + { \frac { x ^ { 3 } } { 3 } } + \cdot \cdot \cdot .
$$

Continuing this process, he finally arrives at

$$
y \ = x - x x + \frac { 1 } { 3 } x ^ { 3 } - \frac { 1 } { 6 } x ^ { 4 } + \frac { 1 } { 3 0 } x ^ { 5 } - \frac { 1 } { 4 5 } x ^ { 6 } \ , \ \& c \ .
$$

an approximation which, neglecting higher order terms, is plotted in Figure 2.1 together with the correct solution. It can be seen that the approximation is close only for small values of $x$ . For more examples see Exercises 11-13 of Section I.3.

# Leibniz

The second inventor of calculus, Leibniz, was led to differential equations around 1676 by the consideration of geometrical problems such as the inverse tangent problem (Leibniz (1693)): a curve $y \left( x \right)$ is required whose tangent AB is given, say everywhere of constant length $\alpha$ (Figure 2.2). This leads to

$$
y \prime = - \frac { y } { b } = - \frac { y } { \sqrt { a ^ { 2 } - y ^ { 2 } } } \ ,
$$

a first order diferential equation. Leibniz was inspired by a silver pocket watch ("horologio portatili suae thecae argentae") $B$ which is pulled on the table by a watch-chain $A B$ of length $^ a$ and he remarks proudly that none of the best scientists had been able to solve the problem before. It is interesting to note that Leibniz, in order to justify his differential equation (2.3) for the pocket-watch, imagined very small straight movements of the watch (Figure 2.3)， which can today be interpreted as Euler's method for the numerical solution of (2.3). The curious fact that differential equations were originally obtained just by the "inverse procedure" to "Euler polygons", has often occurred in history. A second example for this is the variational calculus.

![](images/50dcf2fe60efc84d31e81303f0a9f6284fea030aac9b53efe3c2c89c1a82b30e.jpg)  
Figures 2.2 and 2.3. Illustrations from Leibniz and Kowalewski

# Variational Calculus

In 1696 Johann Bernouli invited the brightest mathematicians of the world ("Profundioris in primis Mathesos cultori, Salutem!") to solve the brachystochrone (shortest time) problem, mainly in order to fault his brother Jacob, from whom he expected a wrong solution. The problem istofinda curve $y \left( x \right)$ connecting two points $P _ { 0 } , P _ { 1 }$ such that a point gliding on this curve under gravitation reaches $P _ { \mathrm { ~ 1 ~ } }$ in the shortest time possible. In order to solve his problem, Joh. Bernoul (1697b) imagined thin layers of homogeneous media and knew from optics (Fermat’s principle) that a light ray with speed $\nu$ obeying the law of Snellius

$$
\mathrm { s i n } \alpha = K \nu
$$

passes through in the shortest time. Since the speed is known to be proportional to the square root of the falen height, he obtains, by passing to thinner and thinner layers,

$$
\sin \alpha = \frac { 1 } { \sqrt { 1 + { y ^ { \prime } } ^ { 2 } } } = K \sqrt { 2 g \left( y - h \right) } \ ,
$$

a differential equation of the first order.

The solutions of (2.4) can be shown to be cycloids (see Exercise 7 of Section I.3). Jacob, in his reply, aiso furnished a solution, much less elegant but unfortunately correct, and in turn invited his brother Johann to solve a couple of new problems. Jacob's method (see Figure 2.4) was something like today's (inverse) "finite element" method and led to the famous work of Euler (1744), which gives the general solution of the problem

![](images/a450bd88f3e294c2b0a3f69b31f925ebae19ba28a3e068460276017a42685ac1.jpg)  
Figure 2.4. Solutions of the variational problem (Joh. Bernoulli, Jac. Bermoul-,Euler)

$$
\begin{array} { l } { x _ { 1 } } \\ { \displaystyle \int f \left( x , y , y \right) d x \ = \mathrm { m i n } } \\ { x _ { 0 } } \end{array}
$$

with the help of the differential equation of the second order

$$
f _ { y ^ { \prime } y ^ { \prime } } y ^ { \prime \prime } + f _ { y ^ { \prime } y } y ^ { \prime } + f _ { y ^ { \prime } x } - f _ { y } = 0 ,
$$

and treated 100 variational problems in detail. Equation (2.5), in the special case where $f$ does not depend on $\bar { \bar { \mathbf { \Lambda } } }$ , can be integrated to give

$$
f - f _ { y ^ { \prime } } y ^ { \prime } = K .
$$

Euler's original proof used polygons in order to establish Equation (2.5). Only the ideas of Lagrange, in 1755 at the age of 19, led to the proof which is today the usual one (Funk (1962)， p.6-9, 16-19, Goldstine (1980),p.110). Euler (1756) then gave, in honour of Lagrange, the name "Variational calculus" to the whole subject ("..tamen gloria primae inventionis acutissimo Geometrae Taurinensi La Grange erat reservata").

# Clairaut

A class of equations with interesting properties was found by Clairaut (see Clairaut (1734), Probleme II). He was motivated by the movement of a rectangular wedge (see Figure 2.5), which led him to differential equations of the form

$$
y - x y \prime + f \left( y \prime \right) = 0 .
$$

This was the first implicit differential equation and possesses the particularity that not only the lines $y = C x - f \left( C \right)$ are solutions, but also their enveloping curves (see Exercise 10 of Section I.3). An example is shown in Figure 2.6 with $f \left( C \right) { = } 5 ( C ^ { 3 } { - } C ) / 2$

![](images/b286dcdd0eb41586d6c09bee731d0777877a3d1f951db79807f2180a3ed08a93.jpg)  
Figure 2.5. Ilustration from Clairaut (1734)

![](images/5db3198e01da160141692d87fef94bc3ba883ab00e4d8ca4ac96bedf715b2902.jpg)  
Figure 2.6. Solutions of a Clairaut differential equation

Since the equation is of the third degree in $y ^ { \prime } { } _ { j }$ ,a given initial value may allow up to three different solution lines. Furthermore, where a line touches an enveloping curve, the solution may be continued either along the line or along the curve. There is thus a huge variety of different possible solution curves. Today we explain this curiosity by the fact that at these points no Lipschitz condition is satisfied (see also Ince (1944), p. 538-539).

# 1.3. Equations solvable by quadrature and elementary functions

We now discuss some of the simplest types of equations, which can be solved by the computation of integrals.

The equation with separable variables

$$
y ^ { \prime } = f \left( x \right) g \left( y \right) .
$$

Dividing by $g \left( y \right)$ and integrating we obtain the solution (Leibniz 1691, in a leter to Huygens)

$$
\begin{array} { r } { \int \frac { d y } { g \left( y \right) } = \int f \left( x \right) d x + C \ . } \end{array}
$$

A special example of this is the linear equation $y \ ^ { \prime } { = } f \left( x \right) y$ ，which possesses the solution

$$
\begin{array} { r } { y \left( x \right) = C R \left( x \right) , \qquad R \left( x \right) = \exp ( \int f \left( x \right) d x ) . } \end{array}
$$

The inhomogeneous linear equation

$$
y ^ { \prime } = f \left( x \right) y + g \left( x \right) ,
$$

Here, the substitution $y \left( x \right) = c \left( x \right) R \left( x \right)$ leads to $c \ ^ { \prime } ( x \ ) { = } g \left( x \right) / R \ \left( x \right)$ (Joh. Bernoulli (1697)). One thus obtains the solution

$$
y \left( x \right) = R \left( x \right) \left( \intop _ { x _ { 0 } } ^ { x } \frac { g \left( s \right) } { R \left( s \right) } d s + C \right) .
$$

# Total differential equations

An equation of the form

$$
P \left( x , y \right) + Q \left( x , y \right) y ^ { \prime } = 0
$$

is found to be im mediately solvable if

$$
\frac { \partial P } { \partial y } = \frac { \partial Q } { \partial x } .
$$

One can then find by integration a function $F \left( x , y \right)$ such that

$$
\frac { \partial F } { \partial x } = P , \frac { \partial F } { \partial y } = Q .
$$

Therefore (3.4) becomes $\frac { d } { d x } F \left( x \ , \ y \left( x \right) \right) = 0$ ，with the solutions expressed by $F \left( x \ , \ y \left( x \ \right) \right) { = } C$ . For the case when (3.5) is not satisfied, Clairaut and Euler investigated the multiplication of (3.4) by a suitablefactor $M \left( x , y \right)$ ，which sometimes allowsthe equation $M P + M Q y ^ { \prime } { = } 0$ to satisfy (3.5).

# Second order equations

Even more than for first order equations, the solution of second order equations by integration is very seldom possible. Besides linear equations with constant coefficients, whose solutions for the second order case were already known to Newton, several tricks of reduction are possible, as for example the following:

For a linear equation

$$
y \prime \prime = a ( x ) y \prime + b ( x ) y
$$

we make the substitution

$$
\begin{array} { r } { y \ = \exp ( \int p \left( \boldsymbol { x } \right) d \boldsymbol { x } ) \ . } \end{array}
$$

The derivatives of this function contain only derivatives of $p$ of lower order

$$
\begin{array} { r } { y ^ { \prime } = p \exp ( \int p \left( x \right) d x ) , \qquad y ^ { \prime \prime } = [ p ^ { 2 } + p ^ { \prime } ] \exp ( \int p \left( x \right) d x ) } \end{array}
$$

so that the insertion of this into the differential equation,after division by y, leads to a lower order equation

$$
p ^ { 2 } + p ^ { \prime } = a ( x ) p + b ( x )
$$

which, however, is nonlinear (Riccati (1723), Euler (1728)).

If the equation is independent of $y \ , \ y \ ^ { \prime \prime } { = } f \left( x \ , \ y \ \right)$ , it is natural to put $y ^ { \prime } { = } \nu$ which gives $\scriptstyle \nu ^ { \prime } = f \ ( x \ , \ \nu )$

An important case is that of equations independent of x :

$$
y \prime \prime = f \left( y , y \right) .
$$

Here we consider $y ^ { \prime }$ as function of y ${ \mathrm { : ~ } } y ^ { \prime } { = } p \left( y \right)$ . Then the chain rule gives $y \ ^ { \prime \prime } { = } p \ ^ { \prime } p { = } f \ ( y \ , \ p )$ ，which is a first order equation. When the function $p ( y )$ has been found, it remains to integrate $y ^ { \prime } { = } p \left( y \right)$ ,which is an equation of type (3.1) (Riccati (1712): 'Per liberare la premessa formula dalle seconde differenze.., chiamo $p$ la sunnormale BF..", see also Euler (1769), Problema 96, p.33).

The investigation of all possible differential equations which can be integrated by analytical methods was begun by Euler. His results have been collected, in more than 800 pages, in Volumes XXIl and

XXII of Euler's Opera Omnia. For a more recent discussion see Ince (1944)，p.16-61. An irreplaceable document on this subject is the book of Kamke (1942). It contains, besides a description of the solu-tion methods and general properties of the solutions, a systematically ordered list of more than 15oo differential equations with their solu-tions and references to the literature.

The computations, even for very sim ple looking equations, soon become very complicated and one quickly began to understand that elementary solutions would not always be possible. It was Liouville (1841) who gave the first proof of the fact that certain equations, such as $y ^ { \prime } { = } x ^ { 2 } { + } y ^ { 2 }$ ,cannot be solved in terms of elementary functions. Therefore, in the 19th century mathematicians became more and more interested in general existence theorems and in numerical methods for the computation of the solutions.

# Exercises

1. Compute with Newton's method further solutions of (2.1), e.g. satisfying y $( 0 ) { = } 0 . 1$ ， $y \left( 0 \right) { = } 0 . 2$ ， $y \left( 0 \right) { = } 0 . 3$ , and draw them.

2. Solve Newton's equation (2.1) by quadrature.

3. Solve Leibniz' equation (2.3) in terms of elementary functions. Hint: The integral for y might cause trouble. Use the substitution $a ^ { 2 } - y ^ { 2 } = u ^ { 2 }$ ， $- y d y = u d u$

4. Solve and draw the solutions of $y ^ { \prime } { = } f \left( y \right)$ where

$$
f \left( y \right) = { \sqrt { \left| y \right| } } .
$$

5. Solve the master-and-dog problem: a dog runs with speed $w$ in the direction of his master, who walks with speed $\nu$ along the y -axis. This leads to the diferential equation

$$
x y ^ { \prime \prime } = { \frac { \nu } { w } } \left( 1 + { y ^ { \prime } } ^ { 2 } \right) ^ { 1 / 2 } .
$$

6. Solve the equation $m y \ ^ { \prime \prime } { = } { - } k / y ^ { 2 }$ ， which describes a body falling according to Newton's law of gravitation.

7. Verify that the cycloid

$$
x - x _ { 0 } = R \left( \tau - \sin \tau \right) , \quad y - h = R \left( 1 - \cos \tau \right) , \quad R = \frac { 1 } { 4 g K ^ { 2 } } 
$$

satisfies the differential equation (2.4) for the brachystochrone problem. Solving (2.4) in a forward manner， one arrives after some sim plifications at the integral

$$
\int { \left( \frac { y } { 1 - y } \right) } ^ { 1 / 2 } d y ,
$$

which is com puted by the substitution $y = ( \sin t ) ^ { 2 }$

8. Show that the differential equation

$$
x + y y ^ { \prime } = y ^ { \prime } { \sqrt { x ^ { 2 } + y ^ { 2 } - 1 } }
$$

possesses the solutions $2 a y = a ^ { 2 } + 1 - x ^ { 2 }$ for all $^ { a }$ . Sketch these curves and find yet another solution of the equation (from Lagrange (1774)， p.7, which was written to explain the "Clairaut phenomenon").

9. Reduce the "Bernoulli equation” (Jac. Bernoulli (1695)) $y ^ { \prime } + f \left( x \right) y = g \left( x \right) y ^ { n }$ , with the help of the coordinate transformation $z ( x ) = ( y ( x ) ) ^ { q }$ and a suitable choice of $q$ ， to a linear equation (Leibniz, Acta Erud. 1696, p.145, Joh. Bernouli (1697)).

10.Verify that the envelope of the solutions $y = C x - f \left( C \right)$ of the Clairaut equation (2.7) is given in parametric representation by

$$
\begin{array} { l } { { x \left( p \right) = f ^ { \prime } \left( p \right) } } \\ { { y \left( p \right) = p f ^ { \prime } \left( p \right) - f \left( p \right) . } } \end{array}
$$

Show that this envelope is also a solution of (2.7) and calculate it for $f \left( C \right) { = } 5 { \left( C ^ { 3 } { - } C \right) } / 2$ (cf. Figure 2.6).

11.(Newton (1671)， "Problema II, Solutio particulare"). Solve the total differential equation

$$
3 x ^ { 2 } - 2 a x + a y - 3 y ^ { 2 } y ^ { \prime } + a x y ^ { \prime } = 0 .
$$

Solution given by Newton: $x ^ { 3 } - a x ^ { 2 } + a x y - y ^ { 3 } = 0$ . Observe that he missed the arbitrary integration constant $C$

12.(Newton (1671)). Solve the equations

$$
\begin{array} { r l } & { \mathrm { a ) } y ^ { \prime } = 1 + \displaystyle \frac { y } { a } + \frac { x y } { a ^ { 2 } } + \frac { x ^ { 2 } y } { a ^ { 3 } } + \frac { x ^ { 3 } y } { a ^ { 4 } } \mathrm { , ~ } \& c . } \\ & { \mathrm { b ) } y ^ { \prime } = - 3 x + 3 x y + y ^ { 2 } - x y ^ { 2 } + y ^ { 3 } - x y ^ { 3 } + y ^ { 4 } - x y ^ { 4 } + 6 x ^ { 2 } y } \\ & { \qquad - 6 x ^ { 2 } + 8 x ^ { 3 } y - 8 x ^ { 3 } + 1 0 x ^ { 4 } y - 1 0 x ^ { 4 } \mathrm { , ~ } \& c . } \end{array}
$$

Results given by Newton:

$$
\begin{array} { r l } { { \mathrm { a ) } } } & { { y = x + \displaystyle \frac { x ^ { 2 } } { 2 a } + \frac { x ^ { 3 } } { 2 a ^ { 2 } } + \frac { x ^ { 4 } } { 2 a ^ { 3 } } + \frac { x ^ { 5 } } { 2 a ^ { 4 } } + \frac { x ^ { 6 } } { 2 a ^ { 5 } } \ , \ \& c . } } \\ { { \mathrm { b ) } } } & { { y = \displaystyle - \frac { 3 } { 2 } x ^ { 2 } - 2 x ^ { 3 } - \frac { 2 5 } { 8 } x ^ { 4 } - \frac { 9 1 } { 2 0 } x ^ { 5 } - \frac { 1 1 1 } { 1 6 } x ^ { 6 } - \frac { 3 6 7 } { 3 5 } x ^ { 7 } \ , \ \& c . } } \end{array}
$$

13.(Newton). Solve Equation (2.1) with another initial value $y \left( 0 \right) = 1$ Newton's result: $y = 1 + 2 x + x ^ { 3 } + \frac { 1 } { 4 } x ^ { 4 } + \frac { 1 } { 4 } x ^ { 5 }$ ，&c.

14.(Cauchy (1824)). Show that the family $y = C \ ( x + C ) ^ { 2 }$ satisfies the differential equation $( y \prime ) ^ { 3 } { = } 8 y ^ { 2 } { - } 4 x y y \prime$ .Find yet another solution which is not included in this family (see Figure 3.1). Answer: $y = - { \frac { 4 } { 2 7 } } x ^ { 3 }$

![](images/44bfe2b0b36590637941fea1b10ad402c2756ab28b4a3d976a35032a8a33e875.jpg)  
Figure 3.1. Solution family of Cauchy's example in Exercise 14

# I.4 Linear differential equations

Lisez Euler, lisez Euler, c'est notre maftre a tous (Laplace)

Following in the footprints of Euler (1743), we want to understand the general solution of $n$ -th order linear differential equations. We say that the equation

$$
L \left( y \right) : = a _ { 0 } ( x ) y ^ { \left( n \right) } + a _ { 1 } ( x ) y ^ { \left( n - 1 \right) } + \cdot \cdot \cdot + a _ { n } ( x ) y = 0
$$

with given functions $a _ { 0 } ( x ) , \dots , a _ { n } ( x )$ is homogeneous. If $_ \pi$ solutions ${ \boldsymbol { \mathfrak { u } } } _ { 1 } ( { \boldsymbol { x } } ) \ , \ \cdot \ \cdot \ , { \boldsymbol { \mathfrak { u } } } _ { n } ( { \boldsymbol { x } } )$ of (4.1) are known, then any linear combination

$$
y ( x ) = C _ { 1 } u _ { 1 } ( x ) + \cdot \cdot \cdot + C _ { n } u _ { n } ( x )
$$

with constant coeficients $c _ { 1 } , \ldots , c _ { n }$ is also a solution of (4.1). This is due to the fact that all derivatives of y appear only linearly in (4.1).

# Equations with constant coefficients

Let us first consider the special case

$$
y ^ { ( n ) } ( x ) = 0 ~ .
$$

This can be integrated once to give $y ^ { ( n - 1 ) } ( x ) { = } C _ { 1 }$ ，then $y ^ { ( n - 2 ) } ( x ) { = } C _ { 1 } x + C _ { 2 } ;$ etc.Replacing at theend the arbitrary constants $C _ { i }$ by new ones, we finally obtain

$$
y \left( x \right) = C _ { 1 } x ^ { n - 1 } + C _ { 2 } x ^ { n - 2 } + \cdot \cdot \cdot + C _ { n } .
$$

Thus there are n "free parameters" in the "general solution" of (4.3). Euler's intuition, after some more examples, also expected the same result for the general equation (4.1). This fact, however, only became completely clear many years later.

We now treat the general equation with constant coefficients,

$$
y ^ { ( n ) } + { A _ { 1 } } y ^ { ( n - 1 ) } + \cdot \cdot \cdot + { A _ { n } } y \ = 0 .
$$

Our problem is to find a basis of $n$ linearly independent solutions $u _ { 1 } ( x ) , \ldots , u _ { n } ( x )$ . To this end, Euler's inspiration was guided by the transformation (3.6),(3.7) above: if $a \left( x \right)$ and $b \left( x \right)$ are constants, we assume $p$ constant in (3.7) so that $p ^ { \prime }$ vanishes, and we obtain the quadratic equation $p ^ { 2 } { = } a p + b$ For any root of this equation, (3.6) then becomes $y = e ^ { p x }$ . In the general case we thus assume $y = e ^ { p x }$ with an unknown constant $\boldsymbol { p }$ , so that (4.4) leads to the characteristic equation

$$
p ^ { n } + { \cal A } _ { 1 } p ^ { n - 1 } + \cdots + { \cal A } _ { n } = 0 .
$$

If the roots $\rho _ { 1 } , . . . , p _ { n }$ of Equation (4.5) are distinct, all solutions of (4.4) are given by

$$
y \left( x \right) = C _ { 1 } e ^ { p _ { 1 } x } + \cdot \cdot \cdot + C _ { n } e ^ { p _ { n } x } \ .
$$

It is curious to see that the "brightest mathematicians of the world" struggled for many decades to find this solution，which appears so trivial to today's students.

A difficulty arises with the solution (4.6) when (4.5) does not possess $n$ distinct roots. Consider, with Euler, the example

$$
y ^ { \prime \prime } - 2 q y ^ { \prime } + q ^ { 2 } y = 0 \ .
$$

Here $p = q$ is a double root of the corresponding characteristic equation. If we set

$$
y \ = e ^ { q x } u ,
$$

(4.7) becomes $\scriptstyle { u } ^ { \prime \prime } = 0$ , which brings us back to (4.3). So the general solution of (4.7) is given by $y \left( x \right) = e ^ { 4 x } \left( C _ { 1 } x + C _ { 2 } \right)$ (see also Exercise 5 below). After some more examples of this type, one sees that the transformation (4.8) effects a shift of the characteristic polynomial, so minating with that if $q$ is a root of multiplicity $\dots + B u ^ { ( k + 1 ) } + C u ^ { ( k ) } = 0$ $k$ ， we obtain for u an equation ter- Therefore

$$
e ^ { q x } ( C _ { 1 } x ^ { k - 1 } + \cdot \cdot \cdot + C _ { k } )
$$

gives us $k$ independent solutions.

Finally， for a pair of complex roots $p = \alpha \pm i \beta$ the solutions $e ^ { ( \alpha + i \beta ) x } , \stackrel { \cdot } { e } ^ { ( \alpha - i \beta ) x }$ can be replaced by the real functions

$$
e ^ { \mathrm { \normalfont ~ a x } } ( C _ { 1 } { \cos } \beta x + C _ { 2 } { \sin } \beta x ) \ .
$$

The study of the inhomogeneous equation

$$
L \left( y \right) = f \left( x \right)
$$

was begun in Euler (1750), p.13. We mention from this work the case where $f \left( x \right)$ is a polynomial, say for example the equation

$$
A y \ ^ { \prime \prime } + B y \ ^ { \prime } + C y \ = a x ^ { 2 } + b x \ + c .
$$

Here Euler puts $y \left( x \right) = E x ^ { 2 } + F x + G + \nu \left( x \right)$ . Inserting this into (4.10) and eliminating all possible powcrs of $\mathcal { \kappa }$ , one obtains

$$
\begin{array} { c } { { C E \ = \ a , ~ C F + 2 B E \ = b , ~ C G \ + B F + 2 A E \ = c , } } \\ { { { } } } \\ { { A \nu ^ { \prime \prime } + B \nu ^ { \prime } + C \nu \ = 0 , } } \end{array}
$$

This allows us, when $c$ is different from zero, to compute $E , F$ and $G$ and we observe that the general solution of the inhomogeneous equation is the sum of a particular solution of it and of the general solution of the corresponding homogeneous equation. This is also true in the general case and can be verified by trivial linear algebra.

The above method of searching for a particular solution with the help of unknown coefficients also works similarly if $f \left( x \right)$ is com posed of exponential, sine, or cosine functions and is often called the "fast method". We see with pleasure that it was historically the first method to be discovered.

# Variation of constants

The general treatment of the inhomogeneous equation

$$
a _ { 0 } ( x ) y ^ { ( n ) } + \cdot \cdot \cdot + a _ { n } ( x ) y = f \left( x \right)
$$

is due to Lagrange (1775) (".. par une nouvelle methode aussi simple qu'on puisse le desirer.", see also Lagrange (1788), seconde partie, Sec.V.) We assume known n independent solutions ${ \mathfrak { u } } _ { 1 } ( x ) , \ldots , { \mathfrak { u } } _ { n } ( x )$ of the homogeneous equation. We then set, in extension of the method employed for (3.2), instead of (4.2)

$$
y ( x ) = c _ { 1 } ( x ) u _ { 1 } ( x ) + \cdot \cdot \cdot + c _ { n } ( x ) u _ { n } ( x )
$$

with unknown functions $c _ { i } ( x )$ ("method of variation of constants"). We have to insert (4.12) into (4.11) and thus compute the first derivative

$$
y ^ { \prime } = \sum _ { i } c _ { i } ^ { \prime } u _ { i } + \sum _ { i } c _ { i } \boldsymbol { u } _ { i } ^ { \prime } \ .
$$

If we continue blindly to differentiate in this way, we soon obtain complicated and useless formulas. Therefore Lagrange astutely requires the first term to vanish and puts

$$
\sum _ { i } c _ { i } ^ { \prime } \boldsymbol { \mathsf { u } } _ { i } ^ { \phantom { \dagger } } = 0 \qquad \quad j = 0 , \mathrm { t h e n } \quad j = 1 , \ldots , n - 2 .
$$

Then repeated differentiation of $y$ ， with continued elimination of the undesired terms (4.13), gives

$$
\begin{array} { c } { { y ^ { \prime } = \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } } u _ { i } ^ { \prime } \ , \quad \cdots \quad , \ y ^ { ( n - 1 ) } = \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } ( n - 1 ) } \ , } } \\ { { \phantom { x ^ { \prime } = } y ^ { ( n ) } = \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } } u _ { i } ^ { ( n - 1 ) } + \sum _ { i } ^ { } c _ { i } ^ { \phantom { * } } u _ { i } ^ { ( n ) } \ . } } \end{array}
$$

If we insert this into (4.11)， we observe wonderful cancellations due to the fact that the $u _ { i } ( x )$ satisfy the homogeneous equation, and finally obtain, together with (4.13),

$$
\left( \begin{array} { c c c } { { u _ { 1 } } } & { { \cdots } } & { { u _ { n } } } \\ { { u _ { 1 } ^ { \prime } } } & { { \cdots } } & { { u _ { n } ^ { \prime } } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { u _ { 1 } ^ { \left( n - 1 \right) } } } & { { \cdots } } & { { u _ { n } ^ { \left( n - 1 \right) } } } \end{array} \right) \left( \begin{array} { c } { { c _ { 1 } ^ { \prime } } } \\ { { c _ { 2 } ^ { \prime } } } \\ { { \vdots } } \\ { { c _ { n } ^ { \prime } } } \end{array} \right) = \left( \begin{array} { c } { { 0 } } \\ { { \vdots } } \\ { { 0 } } \\ { { f \left( x \right) / a _ { 0 } ( x ) } } \end{array} \right) .
$$

This is a linear system, whose determinant is called the "Wronskian" and whose solution yields $c _ { 1 } ^ { \prime } ( x ) , \ldots , c _ { n } ^ { \prime } ( x )$ and after integration, $c _ { 1 } ( x ) , \ldots , c _ { n } ( x ) .$

Much more insight into this formula will be possible in Section I.11.

# Exercises

1. Find the solution "huius aequationis differentialis quarti gradus" $a ^ { 4 } y ^ { ( 4 ) } + y = 0 , ~ a ^ { 4 } y ^ { ( 4 ) } - y = 0$ ;solve the equation "septimi gradus" $y ^ { ( 7 ) } + y ^ { ( 5 ) } + y ^ { ( 4 ) } + \bar { y } ^ { ( 3 ) } + \bar { y } ^ { ( 2 ) } + y = 0$ (Euler (1743),Ex.4,5,6).

2. Solve by Euler's method j $\prime \prime - 3 y \prime - 4 y = \cos x$ ， $y \ ^ { \prime \prime } { + } y = \cos x$

Hint: in the first case the particular solution can be searched for in the form E cosx $+ F$ sinx . This, however, does not work in the second case because of resonance. Here one puts $E x \cos x + F x$ sinx just as in the solution of (4.7).

3. Find the solution of

$$
y ^ { \prime \prime } - 3 y ^ { \prime } - 4 y \ = g \left( x \right) \ , \quad g \left( x \right) = \left\{ \begin{array} { l l } { \cos ( x ) } & { 0 \leq x \leq \frac { \pi } { 2 } } \\ { } & { } \\ { 0 } & { \frac { \pi } { 2 } \leq x \ . } \end{array} \right.
$$

such that $y \left( 0 \right) { = } y ^ { \prime } ( 0 ) { = } 0$

a) by using the solution of Exercise 2, b) by the method of Lagrange (variation of constants).

4. (Reduction of the order if one solution is known). Suppose that a nonzero solution $\boldsymbol { \mathfrak { u } } _ { 1 } ( \boldsymbol { x } )$ of

$$
y ^ { \prime \prime } + a _ { 1 } ( x ) y ^ { \prime } + a _ { 2 } ( x ) y ~ = 0
$$

is known. Show that a second independent solution can be found by putting ${ } ^ { u } { } _ { 2 } ( x ) { = } c ( x ) u _ { 1 } ( x ) .$

5. Treat the case of multiple characteristic values (4.7) by consider-ing them as a limiting case $P _ { 2 } {  } \ : P _ { 1 }$ and using the solutions

$$
u _ { 1 } ( x ) = e ^ { p _ { 1 } x } \ , u _ { 2 } ( x ) = \operatorname * { l i m } _ { p _ { 2 }  p _ { 1 } } { \frac { e ^ { p _ { 2 } x } - e ^ { p _ { 1 } x } } { p _ { 2 } - p _ { 1 } } } = { \frac { \partial e ^ { p _ { 1 } x } } { \partial p _ { 1 } } } \ , { \mathrm { e t c . } }
$$

(d'Alembert-(1748), p.284: "Enfin, si les valeurs de $p$ & de $p ^ { \prime }$ sont egales， au lieu de les supposer telles, on supposera $p = a + \alpha$ ， $p ^ { \prime } { = } a - { \alpha }$ , α etant quantite infiniment petite...").

# I.5. Equations with weak singularities

Many equations occuring in applications possess singularities， i.e., points at which the function $f \left( x , y \right)$ of the differential equation becomes infinite. We study in some detail the classical treatment of such equations, since numerical methods, which will be discussed later in this book, often fail at the singular point and work badly in its close neighbourhood.

As a first example, consider the equation

$$
y ^ { \prime } = \frac { q + b x } { x } y , q \neq 0
$$

with a singularity at $x = 0$ . Its solution, using the method of separation of variables (3.1), is

$$
y \left( x \right) = C x ^ { q } e ^ { b x } = C \left( x ^ { q } + b x ^ { q + 1 } + \cdots \right) .
$$

These solutions are plotted in Figure 5.1 for different values of $q$ and show the fundamental difference in the behaviour of the solutions in dependence of $q$

![](images/3408b9c0d6315586992a1f29b6f0f1ef848289b2d4b2ce8a71d63cb26f5650bc.jpg)  
Figure 5.1. Solutions of (5.1) for $b = 1 , q = 3 / 2 , q = 1 / 2 , q = - 1 / 2$

# Linear equations

Euler started a systematic study of equations with singularities. He asked which type of equation of the second order can be conveniently solved by a series as in (5.2) (Euler (1769), Problema 122, p.177,". quas commode per series resolvere licet $\therefore \prime )$ . He found the equation

$$
x ^ { 2 } ( a + b x ) y ^ { n } + x ( c + e x ) y ^ { \prime } + ( f + g x ) y ~ = 0 ~ .
$$

Let us put

$$
y ~ = ~ \sum _ { i = 0 } ^ { \infty } A _ { i } x ^ { q + i } ~ , ~ A _ { ~ 0 } \neq 0
$$

and insert this, similarly to Newton's procedure (2.2), into (5.3). We thereby observe' that the powers $x ^ { 2 }$ and $x$ which are multiplied by $y ^ { \prime \prime }$ and $y ^ { \prime }$ ， respectively， just re-establish what has been lost by the differentiations and obtain

$$
\begin{array} { c c } { { q ( q - 1 ) a + q c + f } } & { { = 0 } } & { { ( 5 . 5 ) } } \\ { { { } } } & { { { } } } \\ { { { [ ( q + i ) ( q + i - 1 ) a + ( q + i ) c + f ] A _ { i } } } } & { { ( 5 . 5 ) } } \\ { { { } } } & { { { } } } \\ { { { } } } & { { = - [ ( q + i - 1 ) ( q + i - 2 ) b + ( q + i - 1 ) e + g ] A _ { i - 1 } } } \end{array}
$$

for $i = 1 , 2 , 3 , \cdots$ . Equation (5.5a) is called the index equation and determines, for $^ a$ different from zero, two characteristic roots - in decreasing order - $q _ { 1 }$ and $q _ { 2 }$ . For each of these, with $\boldsymbol { A } _ { \textup { 0 } }$ arbitrary, (5.5b) then allows the recursive computation of $A _ { 1 } , A _ { 2 }$ ,etc. For the radius of convergence of the series obtained see Exercise 8 below. We thus obtain two linearly independent solutions $u _ { 1 } ( x ) , u _ { 2 } ( x )$ of the differential equation, just what we require (see I.4). There is, however, a case in which the second solution causes trouble, namely when the coefficient of $A _ { i }$ in (5.5b) becomes zero for some i, i.e., when ${ q _ { 1 } - q _ { 2 } }$ is an integer ("Problema 123"). In this case, on the inspiration of some acrobatic heuristics (Euler (1769), p.150: " quod $x ^ { 0 } / 0$ aequivaleat ipsi logx.")， Euler has the idea of searching for the second solution with the help of

$$
u _ { 2 } ( x ) = u _ { 1 } ( x ) \log x + \sum _ { i = 0 } ^ { \infty } { A _ { i } } ^ { ( 2 ) } x ^ { q _ { 2 } + i } \ ,
$$

The insertion of this into (5.3) then allows him to compute the coefficients ${ A _ { i } } ^ { ( 2 ) }$ An example for this case is given in Exercise 1.

Later, Euler (1778) remarked that the recursion formula (5.5b) becomes particularly elegant, if one starts from the differential equation

$$
x \left( 1 - x \right) y ^ { \prime \prime } + \left( c - ( a + b + 1 ) x \right) y ^ { \prime } - a b y \ = 0
$$

instead of from (5.3). Here, the above method leads to

$$
\begin{array} { r c l } { { q \left( q - 1 \right) + c q = 0 \ , \quad } } & { { q _ { 1 } = 0 \ , \quad } } & { { q _ { 2 } = 1 - c \ , } } \\ { { } } & { { } } & { { } } \\ { { A _ { i + 1 } = \frac { \left( a + i \right) \left( b + i \right) } { \left( c + i \right) \left( 1 + i \right) } A _ { i } \quad } } & { { \mathrm { f o r } q _ { 1 } = 0 \ . } } \end{array}
$$

The resulting solutions, later named hypergeometric functions, became particularly famous throughout the 19th century with the work of Gauss (1812).

More generally， the above method works in the case of a differential equation

$$
x ^ { 2 } y ^ { \prime \prime } + x a ( x ) y ^ { \prime } + b ( x ) y = 0 \quad \quad
$$

where $a \left( x \right)$ and $b ( x )$ are regular analytic functions. One then says that O is a regular or weak singular point. Similarly, we say that the equation $( x - x _ { 0 } ) ^ { 2 } y \prime \prime + ( x - x _ { 0 } ) a ( x ) y \prime + b ( x ) y = 0$ possesses the regular singular point $\varepsilon _ { \mathrm { ~ 0 ~ } }$ . In this case solutions can be obtained by the use of algebraic singularities $( x - x _ { 0 } ) ^ { q }$

Finally, we also want to study the behaviour at infinity for an equation of the form

$$
a ( x ) y ^ { \prime \prime } + b ( x ) y ^ { \prime } + c ( x ) y ~ = 0 ~ .
$$

For this, we use the coordinate transformation $t = 1 / x$ ， $z \left( t \right) { \stackrel { } { = } } y \left( x \right)$ which yields

$$
t ^ { 4 } a \left( \frac { 1 } { t } \right) z ^ { \prime \prime } + \left( 2 t ^ { 3 } a \left( \frac { 1 } { t } \right) - t ^ { 2 } b \left( \frac { 1 } { t } \right) \right) z ^ { \prime } + c \left( \frac { 1 } { t } \right) z \ = 0 \ .
$$

$\infty$ is called a regular singular point of (5.10a) if O is a regular singular point of (5.10b). For examples see Exercise 9.

# Nonlinear Equations

"Der Mathematiker weiss sich ohnedies beim Auftreten von singularen Stellen gegebenenfalls leicht zu helfen."

(K. Heun, 1900)

The above method sometimes allows one to obtain, also for nonlinear equations, if not the complete series of the solution, at least a couple of terms.

EXEMPLUM: let us see what happens if we try to solve the classical brachystochrone problem (2.4) by a series solution. We suppose $h = 0$ and the initial value $y \left( 0 \right) { = } 0$ . We write the equation as

$$
{ y ^ { \prime } } ^ { 2 } = { \frac { L } { y } } - 1 \qquad \mathrm { o r } \qquad { y y ^ { \prime } } ^ { 2 } + y = L \quad .
$$

At the initial point $y \left( 0 \right) = 0 , y ^ { \prime }$ becomes infinite and most numerical methods would fail. We search for a solution of the form $\begin{array} { r } { y = \boldsymbol { A } _ { \mathrm { \scriptsize ~ 0 } } x ^ { q } . } \end{array}$ This gives in (5.11) $q ^ { 2 } A \ _ { 0 } ^ { 3 } x ^ { 3 q - 2 } { + } A \ _ { 0 } x ^ { q } = L$ . Due to the initial value we have that $y \left( x \right)$ becomes negligible for small values of $x$ . We thus set the first term equal to $L$ and obtain $3 q - 2 = 0$ and $q ^ { 2 } A \begin{array} { l } { { 3 } } \\ { { 0 } } \end{array} = L$ .So

$$
u \left( x \right) = \left( \frac { 9 L x ^ { 2 } } { 4 } \right) ^ { 1 / 3 }
$$

is a first approximate solution. The idea is now to use (5.12) just to escape from the initial point with a small $x$ , and then to continue the solution with any numerical step-by-step procedure from the later chapters.

A more refined approximation could be tried in the form $y = \boldsymbol { A } _ { 0 } x ^ { q } + \boldsymbol { A } _ { 1 } x ^ { q + r } .$ This gives with (5.11)

$$
q ^ { 2 } A _ { 0 } ^ { ~ 3 } x ^ { 3 q - 2 } + q ( 3 q + 2 r ) A _ { 0 } ^ { ~ 2 } A _ { 1 } x ^ { 3 q + r - 2 } + A _ { 0 } x ^ { q } + \cdot \cdot \cdot = L ~ .
$$

We use the second term to neutralize the third one, which gives $3 q + r - 2 = q$ or $r = q = 2 / 3$ and $5 q ^ { 2 } A _ { 0 } A _ { 1 } = - 1 .$ Therefore

$$
\nu \left( x \right) = \left( \frac { 9 L x ^ { 2 } } { 4 } \right) ^ { 1 / 3 } - \left( \frac { 9 ^ { 2 } x ^ { 4 } } { 4 ^ { 2 } L \ : \varsigma ^ { 3 } } \right) ^ { 1 / 3 }
$$

is a better approximation. The following numerical results illustrate the utility of the approximations (5.12) and (5.13) compared with the correct solution $y \left( x \right)$ from I.3, Exercise 7, with $L = 2$ ：

$x = 0 . 1 0$ y(x)=0.342839 $u \left( x \right) = 0 . 3 5 5 6 8 9$ $\scriptstyle \nu ( x ) = 0 . 3 4 3 0 3 8$   
$x = 0 . 0 1$ y(x)=0.076042 $u \left( x \right) = 0 . 0 7 6 6 3 1$ $\scriptstyle \nu ( x ) = 0 . 0 7 6 0 4 4$

# Exercises

1. Compute the general solution of the equation $x ^ { 2 } y ~ ^ { \prime \prime } { + } x y ~ ^ { \prime } { + } g x ^ { \prime \prime } y = 0$ with $g$ constant (Euler (1769), Problema 123, Exem plum 1).

2. Apply the  method of Euler to the Bessel equation $x ^ { 2 } y ^ { \prime \prime } + x y ~ ^ { \prime } + ( x ^ { 2 } - g ^ { 2 } ) y = 0$ Sketch the solutions obtained for $g = 2 / 3$ and $g = 1 0 / 3$

3. Compute the solutions of the equations $x ^ { 2 } y ~ ^ { \prime \prime } { - } 2 x y ~ ^ { \prime } { + } y { = } 0$ ， $x ^ { 2 } y ~ ^ { \prime \prime } { - } 3 x y ~ ^ { \prime } { + } 4 y = 0$ Equations of this type are often called Euler's or even Cauchy's equation. Its solution， however, was already known to Joh. Bernoulli.

4. (Euler (1769), Probl.123, Exempl. 2). Let

$$
y \left( x \right) = \int _ { 0 } ^ { 2 \pi } \left( \sin ^ { 2 } { s } + x ^ { 2 } \cos ^ { 2 } { s } \right) ^ { 1 / 2 } d s
$$

be the perimeter of the ellipse with axes 1 and $x < 1$

a) Verify that $y \left( x \right)$ satisfies the differential equation

$$
x ( 1 { - } x ^ { 2 } ) y ^ { \prime \prime } - ( 1 { + } x ^ { 2 } ) y ^ { \prime } + x y = 0 .
$$

b) Compute the solutions of this equation.

c) Show that the coordinate change $x ^ { 2 } = t$ ， $y \left( x \right) = z \left( t \right)$ transforms (5.14) to a hypergeometric equation (5.7).

Hint. The computations for a) lead to the integral

$$
\begin{array} { l } { { \displaystyle { \int _ { 0 } ^ { 2 \pi } \frac { 1 - 2 \cos ^ { 2 } s + q ^ { 2 } \cos ^ { 4 } s } { \left( 1 - q ^ { 2 } \cos ^ { 2 } s \right) ^ { 3 / 2 } } d s } } , } \end{array} \qquad q ^ { 2 } = 1 - x ^ { 2 }
$$

which must be shown to be zero. Develop this into a power series in $q ^ { 2 }$

5. Try to solve the equation

$$
x ^ { 2 } y ^ { \prime \prime } + ( 3 x - 1 ) y ^ { \prime } + y \ = 0
$$

with the help of a series (5.4) and study its convergence.

6. Find a series of the type

$$
y = A _ { 0 } x ^ { q } + A _ { 1 } x ^ { q + s } + A _ { 2 } x ^ { q + 2 s } + \cdot \cdot \cdot
$$

which solves the nonlinear "Emden-Fowler equation" of astrophysics $( x ^ { 2 } y \ ) ^ { \prime } + y ^ { 2 } x ^ { - 1 / 2 } { = } 0$ in the neighbourhood of $x = 0$

7. Approximate the solution of Leibniz's equation (2.3) in the neigh-bourhood of the singular initial value $y \left( 0 \right) = a$ by a function of the type $y \left( x \right) { = } a - C x ^ { q }$ . Compare the result with the correct solution of Exercise 3 of I.3.

8. Show that the radius of convergence of series (5.4) is given by

$$
\mathrm { i } ) \quad r = | \frac { a } { b } | \qquad \mathrm { i i } ) \quad r = 1
$$

for the coefficients given by (5.5) and (5.9), respectively.

9. Show that the point $\infty$ is a regular singular point for the hyper-geometric equation (5.7), but not for the Bessel equation of Exercise 2.

10. Consider the initial value problem

$$
y ^ { \prime } = \frac { \lambda } { x } y + g ( x ) , \qquad y ( 0 ) = 0 .
$$

a) Prove that for $\lambda \le 0$ the problem (5.15) possesses a unique soiution for $x \ge 0$

b) If $g \left( x \right)$ is $k$ -times differentiable and $\lambda \le 0$ ， then the solution $y \left( x \right)$ is $( k + 1 )$ )-times differentiable for $x \geq 0$ and we have

$$
y ^ { ( j ) } ( 0 ) = \left( 1 { - } \frac { \lambda } { j } \right) ^ { - 1 } g ^ { ( j - 1 ) } ( 0 ) ~ , ~ j = 1 , 2 , \cdots ~ .
$$

# 1.6. Systems of equations

# Lagrange

The first systems of equations appear in the work of Lagrange (1759). One of the earliest interests of Lagrange was the propagation of sound. Starting from the insuficiency of Newton's approach, he attempted to explain the propagation of sound from known resuits in elasticity. Thus, if we suppose the medium to be a sequence of mass points and denote by $y _ { 1 } ( t ) , y _ { 2 } ( t ) , y _ { 3 } ( t ) , . .$ their displacements from the equilibrium positions (Figure 6.1), we have from Hooke's law of elasticity

$$
\begin{array} { l } { y _ { 1 } ^ { \prime \prime } = K ^ { 2 } ( - 2 y _ { 1 } + y _ { 2 } ) } \\ { y _ { 2 } ^ { \prime \prime } = K ^ { 2 } ( y _ { 1 } - 2 y _ { 2 } + y _ { 3 } ) } \\ { \cdot \cdot \cdot } \\ { y _ { n } ^ { \prime \prime } = K ^ { 2 } ( y _ { n - 1 } - 2 y _ { n } ) \enspace . } \end{array}
$$

This is a system of $n$ linear differential equations. Throughout this section we shall use $t$ for the independent variable (time), in order to avoid confusion with the space variable $x$ of the corresponding partial differential equation. Lagrange observed that the same equations appear, when d'Alembert's (1748) equation

$$
{ \frac { \partial ^ { 2 } u } { { \partial t } ^ { 2 } } } = a ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

for the vibrating string (cordis vibrantibus) is modeled by a finite number of mass points attched to a string without mass (Figure 6.1).

![](images/5d54ac7890a580b787d196d00aa2724f0b7898e59548713d86538ff3338945f1.jpg)

![](images/b44d563dd69cfee7955c02c5c4a08a7b888784918cf41c6aa7fadc4bc097cb88.jpg)  
Figure 6.1. Model for sound propagation, vibrating and hanging string

Another example treated by Lagrange ((1762)， Nr. 36), was that of mass points attached to a hanging string (Figure 6.1). Here the tension in the string becomes greater in the upper part of the string and we have the following equations of movement

$$
\begin{array} { l } { y _ { 1 } ^ { \prime \prime } = K ^ { 2 } ( - y _ { 1 } + y _ { 2 } ) } \\ { y _ { 2 } ^ { \prime \prime } = K ^ { 2 } ( y _ { 1 } - 3 y _ { 2 } + 2 y _ { 3 } ) } \\ { y _ { 3 } ^ { \prime \prime } = K ^ { 2 } ( 2 y _ { 2 } - 5 y _ { 3 } + 3 y _ { 4 } ) } \end{array}
$$

$$
y _ { n } ^ { \prime \prime } = K ^ { 2 } ( ( n - 1 ) y _ { n - 1 } - ( 2 n - 1 ) y _ { n } ) ,
$$

In all these examples, of course, the deviations $y _ { i }$ are supposed to be "infinitely" small, so that linear models are realistic.

Using a notation which came into use only a century later, we write these equations in the form

$$
y _ { i } ^ { \prime \prime } = \sum _ { j = 1 } ^ { n } \alpha _ { i j } y _ { j } \qquad ( i = 1 , \ldots , n ) \ ,
$$

which represents a system of 2nd order linear equations with constant coefficients.Lagrange solves System (6.3) by puting $\boldsymbol { y } _ { i } ^ { \phantom { } } = \boldsymbol { c } _ { i } ^ { \phantom { } } e ^ { p \boldsymbol { \tau } }$ ，which leads to

$$
{ p ^ { 2 } c _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } c _ { j } } \qquad ( i = 1 , \dots , n )
$$

so that $p ^ { 2 }$ must be an eigenvalue of the matrix A and $\boldsymbol { c } = ( c _ { 1 } , . . . , c _ { n } ) ^ { T }$ the corresponding eigenvector. We see here the first appearance of an eigenvalue problem and also the first use of the "method of lines" for the wave equation.

Lagrange ((1762), Nr.30) then explains that the equations (6.4) are solved by computing $c _ { 2 } / c _ { 1 } , \ldots , c _ { n } / c _ { 1 }$ as functions of $p$ from $n - 1$ equations and by inserting these results into the last one. This leads to a polynomial of degree n (in fact, the characteristic polynomial) to rodth for $p ^ { 2 }$ aWoutusi2tins $y _ { i } ^ { ( j ) } { = } c _ { i } ^ { ( j ) } \mathrm { e x p } ( { \pm } p _ { j } \varepsilon )$ of these.

A complication arises when the characteristic polynomial possesses multiple roots. In this case, Lagrange (in his famous Mecanique Analytique, Lagrange (1788)， seconde partie, sect.VI, No.7) affirms the presence of "secular" terms similar to the formulas following (4.8). This， however, is not completely true, as became clear only a century later (see e.g. Weierstrass (1858), p.243: ". um bei dieser Gelegenheit einen Irrtum zu berichtigen, der sich in der Lagrange'schen Theorie der kleinen Schwingungen, sowie in allen spateren mir bekannten Darstellungen derselben, findet."). We therefore postpone this subject to Section I.12.

We close this section by solving Equations (6.1) in detail, since the results obtained are of particular importance (Lagrange (1759)). The corresponding eigenvalue problem (6.4) becomes in this case $p ^ { 2 } c _ { 1 } { = } K ^ { 2 } ( - \dot { 2 } c _ { 1 } { + } c _ { 2 } )$ ， ${ p ^ { 2 } c _ { i } = } K ^ { 2 } ( c _ { i - 1 } { - 2 } c _ { i } { + } c _ { i + 1 } )$ for $i = 2 , \ldots , n - 1$ and $p ^ { 2 } c _ { n } = K ^ { 2 } ( c _ { n - 1 } - 2 \bar { c } _ { n } )$ We introduce $p ^ { 2 } / K ^ { 2 } + 2 = q$ ,so that

$$
c _ { j + 1 } - q c _ { j } + c _ { j - 1 } = 0 ~ , ~ c _ { 0 } = 0 ~ , ~ c _ { n + 1 } = 0 ~ .
$$

This means that the $c _ { i }$ are the solutions of a difference equation and therefore $\scriptstyle c _ { j } = A a ^ { j } + B b ^ { j }$ where a and $^ b$ are the roots of the corresponding characteristic equation $z ^ { 2 } - q z + 1 = 0$ , hence

$$
a + b = q , a b = 1 ,
$$

The condition ${ c _ { 0 } } \mathrm { { = } } 0$ of (6.5),which means $A + B = 0$ ，shows that $c _ { j } ^ { } = a _ { } ( a ^ { j } - b ^ { j } )$ with $A \neq 0$ Thesecondcondition $c _ { n + 1 } = 0$ ,or equivalently $( a / b ) ^ { n + 1 } = 1$ , implies together with $a b = 1$ that

$$
a \ = \ \exp \left( { \frac { k \pi i } { n + 1 } } \right) \ , \qquad b \ = \ \exp \left( { \frac { - k \pi i } { n + 1 } } \right)
$$

for some $k = 1 , \ldots , n .$ Thus we obtain

$$
\begin{array} { l } { { q _ { k } ~ = 2 \cos \displaystyle \frac { \pi k } { n + 1 } ~ , \quad k = 1 \ldots , n ~ , } } \\ { { \displaystyle p _ { k } ^ { 2 } = 2 { \bf K } ^ { 2 } \biggl ( \cos \displaystyle \frac { \pi k } { n + 1 } - 1 \biggr ) = - 4 { \bf K } ^ { 2 } \biggl ( \sin \displaystyle \frac { \pi k } { 2 n + 2 } \biggr ) ^ { 2 } ~ . } } \end{array}
$$

Finally, Euler's formula from 1740, $e ^ { i x } - e ^ { - i x } = 2 i \sin x$ (".. si familiere aujourd'hui aux Geometres") gives for the eigenvectors (with $A = - i / 2$ ）

$$
\begin{array} { r } { c _ { j } ^ { \mathbf { \Upsilon } ( k ) } = \sin \frac { j k \pi } { n + 1 } , \qquad j , k = 1 , \ldots , n . } \end{array}
$$

Since the $p _ { k }$ are purely imaginary, we also use for $\mathrm { e x p } ( \pm p _ { k } t )$ the "familiere" formula and obtain finally the general solution

$$
y _ { j } ( t ) = \sum _ { k = 1 } ^ { n } \sin { \frac { j k \pi } { n + 1 } } ( a _ { k } \cos r _ { k } t + b _ { k } \sin r _ { k } t ) , \quad r _ { k } = 2 K \sin { \frac { \pi k } { 2 n + 2 } } .
$$

Lagrange then observed after some lengthy calculations， which are today seen by using the orthogonality relations

$$
\sum _ { l = 1 } ^ { n } \sin { \frac { l j \pi } { n + 1 } } \sin { \frac { l k \pi } { n + 1 } } = \left\{ \begin{array} { l l } { { 0 } } & { { j \neq k } } \\ { { \displaystyle { \frac { n + 1 } { 2 } } } } & { { j = k } } \end{array} \right. \quad \quad j , k = 1 , \ldots , n
$$

that

$$
\begin{array} { l } { { a _ { k } = \displaystyle \frac { 2 } { n + 1 } \sum _ { j = 1 } ^ { n } \sin \displaystyle \frac { k j \pi } { n + 1 } y _ { j } ( 0 ) ~ , } } \\ { { b _ { k } = \displaystyle \frac { 1 } { r _ { k } } \displaystyle \frac { 2 } { n + 1 } \sum _ { j = 1 } ^ { n } \sin \displaystyle \frac { k j \pi } { n + 1 } y _ { j } ^ { \prime } ( 0 ) } } \end{array}
$$

are determined by the initial positions and velocities of the mass points. He also studied the case where $n$ , the number of mass points, tends to infinity (so that, in the formula for $r _ { k }$ ， sinx can be replaced by $x$ ) and stood, 50 years before Fourier, at the portal of Fourier series theory. "Mit welcher Gewandtheit, mit welchem Aufwande analytischer Kunstgriffe er auch den ersten Theil dieser Untersuchung durchfuhrte, so liess der Uebergang vom Endlichen zum Unendlichen doch viel zu wuinschen iubrig..."(Riem ann (1854)).

# Fourier

J'ajouterai que le livre de Fourier a une importance capitale dans I'histoire des mathematiques. (H. Poincare, 1893)

The first first order systems were motivated by the problem of heat conduction (Biot 1804, Fourier (1807)). Fourier imagined a rod to be a sequence of molecules, whose temperatures we denote by $y _ { i }$ , and deduced from a law of Newton that the energy which a particle passes to its neighbours is proportional to the difference of their temperatures, i.e., ${ \boldsymbol { y } } _ { i - 1 } - { \boldsymbol { y } } _ { i }$ to the left and ${ \boldsymbol { y } } _ { i + 1 } - { \boldsymbol { y } } _ { i }$ to the right ("Lorsque deux molecules d'un méme solide sont extremement voisines et ont des temperatures inégales, la molecule plus echauffee comm unique a celle qui 'est moins une quantite de chaleur exactement exprimee par le produit formé de la duree de l'instant, de la difference extremement petite des temperatures, et d'une certaine fonction de la distance des molecules"). This long sentence means, in formulas, that the total gain of energy of the $i - t h$ molecule is expressed by

$$
y _ { i } ^ { \prime } = K ^ { 2 } ( y _ { i - 1 } - 2 y _ { i } + y _ { i + 1 } ) ~ , ~ 
$$

or, in general

$$
y _ { i } ^ { \prime } = \sum _ { j = 1 } ^ { n } a _ { i j } y _ { i } \qquad i = 1 , \ldots , n .
$$

a first order system with constant coefficients.

By putting $y _ { i } { = } c _ { i } e ^ { p \tau }$ , we now obtain the eigenvalue problem

$$
p c _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } c _ { j } \qquad i = 1 , \dots , n \ .
$$

If we suppose tke rod cooled to zero at both ends $\left( y _ { 0 } \mathrm { = } y _ { n + 1 } \mathrm { = } 0 \right)$ ,we can use Lagrange eigenvectors from above and obtain the solution

$$
y _ { j } ( t ) = \sum _ { k = 1 } ^ { n } \sin { \frac { j k \pi } { n + 1 } } a _ { k } \exp ( - w _ { k } t ) ~ , ~ w _ { k } = 4 K ^ { 2 } \biggl ( \sin { \frac { \pi k } { 2 n + 2 } } \biggr ) ^ { 2 } ~ .
$$

By taking n larger and larger, Fourier arrived from (6.10) (hence: by the inverse "method of lines") at his famous heat equation

$$
{ \frac { \partial u } { \partial t } } = a ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

which was the origin of Fourier series theory.

# Exercises

1. Verify that, if $u \left( x \right)$ is sufficiently differentiable,

$$
{ \frac { u ( x - 8 ) - 2 u ( x ) + u ( x + 8 ) } { 8 ^ { 2 } } } = u ^ { \prime \prime } ( x ) + { \frac { 8 ^ { 2 } u ^ { ( 4 ) } ( x ) } { 1 2 } } + { \bf O } ( 8 ^ { 4 } ) .
$$

Hint: use Taylor series expansion for $u \left( x + 8 \right)$ and $u \left( x - 8 \right)$ . This relation establishes the connection between (6.10) and (6.14) as well as between (6.1) and the wave equation.

2. Solve Equation (6.2) for $n = 2$ and $n = 3$ by using the device of Lagrange described above (1762) and discovering naturally the characteristic polynomial of the matrix .

3. Solve the first order system (6.11) with initial values $y _ { i } ( 0 ) = ( - 1 ) ^ { i }$ ， where the matrix A is the same as in Exercise 2 and draw the solutions. Physically, this equation would represent a string with weights hanging, say, in honey.

4. Find the first terms of the development at the singular point $x = 0$ of the following system of nonlinear equations

$$
{ \begin{array} { r l } { x ^ { 2 } y ^ { \prime \prime } + 2 x y ^ { \prime } = 2 y z ^ { 2 } + { \mathsf { A } } x ^ { 2 } y ( y ^ { 2 } - 1 ) } & { \qquad y ( 0 ) { \ = } 0 } \\ { x ^ { 2 } z ^ { \prime \prime } = z ( z ^ { 2 } { - } 1 ) + x ^ { 2 } y ^ { 2 } z } & { \qquad z ( 0 ) { = } 1 } \end{array} }
$$

where 入 is a constant parameter. Equations (6.15) are the Euler equations for the variational problem

$$
I = \int _ { \stackrel { \{ } 0 \} { \displaystyle 0 } } ^ { \infty } \left( { z ^ { \prime } } ^ { 2 } + \frac { { x ^ { 2 } } { y ^ { \prime } } ^ { 2 } } { 2 } + \frac { ( z ^ { 2 } - 1 ) ^ { 2 } } { 2 x ^ { 2 } } + { y ^ { 2 } } { z ^ { 2 } } + \frac { \lambda } { 4 } { x ^ { 2 } } ( { y ^ { 2 } } - 1 ) ^ { 2 } \right) d x ,
$$

$$
y \left( \infty \right) = 1 , z \left( \infty \right) = 0
$$

which gives the mass of a "monopole" in nuclear physics (see 't Hooft (1974)).

# I.7. A general existence theorem

We now enter a new era for our subject, more theoretical than the preceding one. It was inaugurated by the work of Cauchy, who was not as fascinated by long numerical calculations as was， say, Euler, but merely a fanatic for perfect mathem atical rigour and exact-ness. He criticized in the work of his predecessors the use of infinite series and other infinite processes without taking much account of error estimates or convergence results. He therefore established around 1820 a convergence theorem for the polygon method of Euler and, some 15 years later, for the power series method of Newton (see Section I.8). Beyond the estimation of errors, these results also allow the statement of general existence theorems for the solutions of arbitrary differential equations ("d'une equation différentielle quelconque")，whose solutions were only known before in a very few cases. A second important consequence is to provide results about the uniqueness of the solution, which allow one to conclude that the computed solution (numerically or analytically) is the only one with the same initial value and that there are no others. Only then we are allowed to speak of the solution of the problem.

His very first proof has recently been discovered on fragmentary notes (Cauchy (1824)), which were never published in Cauchy's lifetime (did his notes not satisfy the Minister of education?: ".. mais que le second professeur, M. Cauchy, n'a présente que des feuilles qui n'ont pu satisfaire la commission, et qu’il a éte jusqu'a present impossible de l'amener a se rendre au voeu du Conseil et a exécuter la decision du Ministre").

# Convergence of Euler's method

Let us now, with bared head and trembling knees, follow the ideas of this historical proof. We formulate it in a way which generalizes directly to higher dimensional systems.

Starting with the one-dimensional differential equation

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y \left( X \right) = ?
$$

we make use of the method explained by Euler (1768) in the last section of his "Institutiones Calculi Integralis" (Caput VII, p.424), i.e. we consider a subdivision of the interval of integration

$$
x _ { 0 } , x _ { 1 } , \ldots , x _ { n - 1 } , x _ { n } = X
$$

and replace in each subinterval the solution by the first term of its Taylor series

$$
\begin{array} { r } { y _ { 1 } - y _ { 0 } = ( x _ { 1 } - x _ { 0 } ) f ( x _ { 0 } , y _ { 0 } ) } \\ { y _ { 2 } - y _ { 1 } = ( x _ { 2 } - x _ { 1 } ) f ( x _ { 1 } , y _ { 1 } ) } \end{array}
$$

$$
y _ { n } - y _ { n - 1 } = ( x _ { n } - x _ { n - 1 } ) f \left( x _ { n - 1 } , y _ { n - 1 } \right) .
$$

For the subdivision above we also use the notation

$$
\textit { h } = ( h _ { 0 } , h _ { 1 } , \ldots , h _ { n - 1 } )
$$

where $n _ { i } = x _ { i + 1 } - x _ { i }$ . If we connect $y _ { 0 }$ and $y _ { 1 } , y _ { 1 }$ and $y _ { 2 } , \ldots$ etc by straight lines we obtain the Euler polygon

$$
y _ { h } ( x ) = y _ { i } + ( x - x _ { i } ) f ( x _ { i } , y _ { i } ) ~ \mathrm { f o r } ~ x _ { i } { \le } x { \le } x _ { i + 1 } ~ .
$$

Lemma 7.1. A ssume that $\mid f \mid$ is bounded by A on

$$
D \ = \Big \{ ( x , y ) | x _ { 0 } { \le } x { \le } X , | y { - } y _ { 0 } | { \le } b \Big \} \ .
$$

1f $X ^ { - x } _ { 0 } { \le } { b } / A$ then the numerical solution $( x _ { i } , y _ { i } )$ given by (7.3), remains in $D$ for every subdivision (7.2) and we have

$$
| \ y _ { h } ( x ) - y _ { 0 } | \ \leq \ A \cdot | x - x _ { 0 } | ,
$$

$$
\mid y _ { h } ( x ) - ( y _ { 0 } + ( x - x _ { 0 } ) f ( x _ { 0 } , y _ { 0 } ) ) \mid \le \mathtt { e } \cdot \mid x - x _ { 0 } \mid
$$

$$
\begin{array} { r } { i f \left( x , y \right) - f \left( x _ { 0 } , y _ { 0 } \right) \mid \ \leq \ \epsilon \quad o n \ D . } \end{array}
$$

Proof: Both inequalities are obtained by adding up the lines of (7.3) and using the triangle inequality. (7.4) then shows immediately that for A $( x - x _ { 0 } ) \le b$ the polygon remains in $D$ . QED.

Our next problem is to obtain an estimate for the change of $y _ { h } ( x )$ ， when the initial value $y _ { 0 }$ is changed: let $ { { ^ z _ { 0 } } }$ be another initial value and compute

$$
z _ { 1 } - z _ { 0 } = ( x _ { 1 } { - } x _ { 0 } ) f ( x _ { 0 } , z _ { 0 } ) .
$$

We need an estim ate for $\left| z _ { 1 } - y _ { 1 } \right| .$ Subtracting (7.6) from the first line of (7.3) we obtain

$$
z _ { 1 } - y _ { 1 } = z _ { 0 } - y _ { 0 } + ( x _ { 1 } - x _ { 0 } ) \bigg ( f \left( x _ { 0 } , z _ { 0 } \right) - f \left( x _ { 0 } , y _ { 0 } \right) \bigg ) \ .
$$

This shows that we need an estimate for $f \left( x _ { 0 } , z _ { 0 } \right) - f \left( x _ { 0 } , y _ { 0 } \right)$ If we suppose

$$
\mid f \left( x , z \right) - f \left( x , y \right) \mid \ \leq \ L \ \vert z - y \mid
$$

we obtain

$$
\left| z _ { 1 } - y _ { 1 } \right| \ \leq \ ( 1 + ( x _ { 1 } - x _ { 0 } ) L \ ) \left| z _ { 0 } - y _ { 0 } \right| \ .
$$

Lemma 7.2. For a fixed subdivision h let $y _ { h } ( x )$ and $z _ { h } ( x )$ be the Euler potygons corresponding to the initial values $y _ { \mathrm { ~ 0 ~ } } a n d \textit { z } _ { \mathrm { ~ 0 ~ } }$ , respectivety. 1f

$$
\begin{array} { r } { \displaystyle \mid \frac { \partial f } { \partial y } ( x , y ) \mid \le L } \end{array}
$$

in a convex region which contains $( x \ , y _ { h } ( x ) )$ and $( x \ , \ z _ { h } ( x ) )$ for au $x _ { 0 } \leq x \leq X$ ,then

$$
\mid z _ { h } \left( x \right) - y _ { h } \left( x \right) \mid \ \le \ e ^ { L \left( x - x _ { 0 } \right) } \vert z _ { 0 } - y _ { 0 } \vert .
$$

Proof: (7.9) implies (7.7), (7.7) implies (7.8), (7.8) implies (Matth.1.2)

$$
\left| z _ { 1 } - y _ { 1 } \right| \ \leq \ e ^ { L \left( x _ { 1 } - x _ { 0 } \right) } | z _ { 0 } - y _ { 0 } | .
$$

If we repeat the same argument for $z _ { 2 } - y _ { 2 } , \ z _ { 3 } - y _ { 3 }$ ，and so on, we finally obtain (7.10). QED.

Remark: Condition (7.7) is called a "Lipschitz condition". It was Lipschitz (1876) who rediscovered the theory (footnote in the paper of Lipschitz: "L'auteur ne connait pas évidemment les travaux de Cauchy.") and advocated the use of (7.7) instead of the more stringent hypothesis (7.9). Lipschitz's proof is also explained in the classical work of Picard (1891-96), Vol.II, Chap.XI, Sec.I.

If the subdivision (7.2) is refined more and more, so that

$$
\vert h \vert : = \operatorname* { m a x } _ { i = 0 , . . , n - 1 } h _ { i } \to 0 ,
$$

we expect that the Euler polygons converge to a solution of (7.1). Indeed, we have

Theorem 7.3. Let $f \left( x , y \right)$ be continuous, and $\mid f \mid$ be bounded by A and satisfy the Lipschitz condition (7.7) on

$$
\textit { D } = \left\{ ( x , y ) \ : | \ : x \ : _ { 0 } { \le } x { \le } X \ : , \ : | y { - } y \ : _ { 0 } | { \le } b \right\} .
$$

$I f X - x _ { 0 } { \leq } b / A$ , then we have:

a)For $| h   \mathrm { ~ 0 ~ }$ the Euler polygons $y _ { h } \left( x \right)$ converge uniformly to a continu-ous function $\Phi ( x )$   
b） $\Phi ( x )$ is continuously differentiable and is a solution of (7.1） on $x _ { 0 } { \le } x \le X$ ，   
c) There exists no other solution of (7.1) on xo≤ x ≤X .

Proof: a) Take an $\epsilon > 0$ . Since $f$ is uniformly continuous on the compact set $D$ , there exists a $\delta > 0$ such that

$$
| { u } _ { 1 } - { u } _ { 2 } | \ \leq \ 8 \qquad \mathrm { a n d } \qquad | { \nu } _ { 1 } - { \nu } _ { 2 } | \ \leq \ A \ \ 8
$$

imply

$$
\mid f ( u _ { 1 } , \nu _ { 1 } ) - f ( u _ { 2 } , \nu _ { 2 } ) \mid \leq \epsilon .
$$

Suppose now that the subdivision (7.3) satisfies

$$
| x _ { i + 1 } - x _ { i } | \ \leq \ 8 , \mathrm { i . e . } | h | \ \leq \ 8 .
$$

We first study the effect of adding new mesh-points. In a first step, we consider a subdivision $h \left( 1 \right)$ ，which is obtained by adding new points only to the frst subinterval. It follows from (7.5) (applied to this first subinterval) that for the new refined solution $y _ { h ( 1 ) } ( x _ { 1 } )$ we have the estimate $| y _ { h ( 1 ) } ( x _ { 1 } ) - y _ { h } ( x _ { 1 } ) | \leq \epsilon | x _ { 1 } - x _ { 0 } |$ Since the subdivisions $h$ and $h \left( 1 \right)$ are identical on $x _ { 1 } \leq x \leq X$ we can apply Lem ma 7.2 to obtain

$$
\mid y _ { h ( 1 ) } ( x ) - y _ { h } ( x ) \mid \leq e ^ { L ( x - x _ { 1 } ) } ( x _ { 1 } - x _ { 0 } ) \in ~ \mathrm { f o r } ~ x _ { 1 } \leq x \leq X .
$$

We next add further points to the subinterval $( x _ { 1 } , x _ { 2 } )$ and denote the new subdivision by $h \left( 2 \right)$ . In the same way as above this leads to

$$
\mid y _ { h ( 2 ) } ( x _ { 2 } ) - y _ { h ( 1 ) } ( x _ { 2 } ) \mid \le \mathtt { e } \mid x _ { 2 } - x _ { 1 } \mid
$$

and

$$
\mid y _ { h ( 2 ) } ( x ) - y _ { h ( 1 ) } ( x ) \mid \le e ^ { L ( x - x _ { 2 } ) } ( x _ { 2 } { - } x _ { 1 } ) \epsilon ~ \mathrm { f o r } ~ x _ { 2 } \le x \le X .
$$

The entire situation is sketched in Figure 7.1. If we denote by $\hat { h }$ the final refinement, we obtain for xi< x ≤xi +1

$$
\begin{array} { r l r } {  { \mid y _ { \hat { h } } ( x ) - y _ { h } ( x ) \mid } } \\ & { \le } & { \epsilon ( e ^ { L ( x - x _ { 1 } ) } ( x _ { 1 } { - } x _ { 0 } ) + \cdot \cdot \cdot + e ^ { L ( x - x _ { i } ) } ( x _ { i } { - } x _ { i - 1 } ) ) + \epsilon ( x - x _ { i } ) } \\ & { \le } & { \epsilon \int e ^ { L ( x - s ) } d s = \frac { \epsilon } { L } ( e ^ { L ( x - x _ { 0 } ) } - 1 ) ~ . } \\ & { } & { x _ { 0 } } \end{array}
$$

![](images/9098fbb71cbed06160f8a4db6ea02f7ebb1590a9d0a62f16d9e8c3d1c4888285.jpg)  
Figure 7.1. Lady Windermere's Fan (O. Wilde (1892))

If we now have two different subdivisions h and $\mathbf { \Pi } _ { \hat { h } } ^ { \tilde { h } }$ ，which both satisfy (7.12)， we introduce a third subdivision which is a refinement of both subdivisions (just as is usually done in proving the existence of Riemann's integral)，and apply (7.13) twice. Wc then obtain from (7.13) by the triangle inequality

$$
\mid y _ { h } ( x ) - y _ { \bar { h } } ( x ) \mid \leq 2 \frac { \epsilon } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) .
$$

For $\epsilon > 0$ small enough, this becomes arbitrarily small and shows the uniform convergence of the Euler polygons to a continuous function $\phi ( x )$

b) Let

$$
\begin{array} { r l } & { \epsilon ( \mathfrak { d } ) { : = } \mathrm { s u p } \Bigg \{ \vert \begin{array} { l } { f \left( u _ { 1 } , \nu _ { 1 } \right) - f \left( u _ { 2 } , \nu _ { 2 } \right) \vert } \\ { \vert u _ { 1 } - u _ { 2 } \vert \le \mathfrak { d } \ , \vert \nu _ { 1 } - \nu _ { 2 } \vert \le A \mathfrak { d } \ , ( u _ { i } , \nu _ { i } ) \in D \Bigg \} } \end{array} } \end{array}
$$

be the modulus of continuity. If $\mathcal { L }$ belongs to the subdivision $h$ then we obtain from (7.5) (replace $( x _ { 0 } , y _ { 0 } )$ by $( x \ , y _ { h } ( x \ ) )$ and $x$ by $x + 8$ ）

$$
\mid y _ { h } \left( x + \ S \right) - y _ { h } \left( x \right) - \ S f \left( x , y _ { h } \left( x \right) \right) \mid \le \mathtt { e } \left( \ S \right) \ S \ .
$$

Passing to the limit $| h _ { \mathbf { \alpha } } | _ {  \mathrm { ~ 0 ~ } }$ we get

$$
\mid \Phi ( x + \mathfrak { d } ) - \Phi ( x ) - \mathfrak { d } f \left( x , \Phi ( x ) \right) \mid \le \mathfrak { e } \left( \mathfrak { d } \right) \mathfrak { d } \ .
$$

Since $\epsilon ( \delta ) \to 0$ for $\delta \to ~ 0$ ， this proves the differentiability of $\Phi ( x )$ and $\Phi ^ { \prime } ( x ) { = } f \left( x , \Phi ( x ) \right)$

c) Let $\Psi ( x )$ be a second solution of (7.1) and suppose that the subdivision $^ h$ satisfies (7.12). We then denote by $y _ { h } ^ { ~ ( i ) } ( x )$ the Euler polygon to the initial value $( x _ { i } , \psi ( x _ { i } ) )$ (it is defined for $x _ { i } \leq x \leq X$ ). It follows from

$$
\psi ( x ) = \psi ( x _ { i } ) + \intop _ { x _ { i } } ^ { x } f \left( s , \psi ( s ) \right) d s
$$

and (7.11) that

$$
| \Psi ( x ) - y _ { h } ^ { ( i ) } ( x ) | \leq \epsilon | x - x _ { i } | \mathrm { ~ f o r ~ } x _ { i } \leq x \leq x _ { i + 1 } .
$$

Using Lemma 7.2 we deduce in the same way as in part a) that

$$
| \Psi ( x ) - y _ { h } ( x ) | \leq \frac { \epsilon } { L } \biggl ( e ^ { L \left( x - x _ { 0 } \right) } - 1 \biggr ) \ ,
$$

Passing to the limits $\lvert h \rvert \to 0$ and $\epsilon  0$ we obtain $| \psi ( x ) - \phi ( x ) | \leq 0$ ， proving uniqueness. QED.

Theorem 7.3 is a local existence - and uniqueness - result. However, if we interpret the endpoint of the solution as a new initial value, we can apply Theorem 7.3 again and continue the solution. Repeating this procedure we obtain

Theorem 7.4. Assume U to be an open set in $\mathbb { R } ^ { 2 }$ and let $f$ and af /dy be continuous on $U$ . Then, for every $( x _ { 0 } , y _ { 0 } ) \in U$ ， there exists a unique solution of (7.1)， which can be continued up to the boundary of $U$ (in both directions).

Proof: Clearly, Theorem 7.3 can be rewritten to give a local existence - and uniqueness - result for an interval $( X \ , \ x _ { 0 } )$ to the left of $x _ { 0 }$ . The rest follows from the fact that every point in $U$ has a neighbourhood which satisfies the assum ptions of Theorem 7.3. QED.

It is interesting to mention that Formula (7.13) for $\mid \hat { h _ { \mathbf { \alpha } } } \mid _ {  \mathbf { \alpha } 0 }$ gives the following error estimate

$$
| ~ y ( x ) - y _ { h } ( x ) ~ | \leq ~ { \frac { \epsilon } { L } } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right)
$$

for the Euler polygon ( $\left| h \right. \left| \leq 8 \right|$ ).Here $y \left( x \right)$ stands for the exact solution of (7.1). The next theorem refines the above estimates for the case that $f \left( x , y \right)$ is also differentiable with respect to $x$ ·

Theorem 7.5. Suppose that in a neighbourhood of the solution

$$
\mid f \mid \le A , \mid \frac { \partial f } { \partial y } \mid \le L , \mid \frac { \partial f } { \partial x } \mid \le M .
$$

W e then have the following error estimate for the Euler polygons:

$$
\left| ~ y \left( x \right) - y _ { h } ( x ) \right| \le ~ { \frac { M + A L } { L } } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) \cdot \left| h ~ \right| ~ ,
$$

provided that $\left| h \right|$ is sufficiently small.

Proof: For $\vert u _ { 1 } - u _ { 2 } \vert \leq \vert h \vert$ and $| \nu _ { 1 } - \nu _ { 2 } | { \leq A }$ $\left| h \right|$ we obtain, due to the differentiability of $f$ , the estimate

$$
\mid f \left( u _ { 1 } , \nu _ { 1 } \right) - f \left( u _ { 2 } , \nu _ { 2 } \right) \mid \ \leq \ \left( M + A L \right) \mid h \mid
$$

instead of (7.11). When we insert this amount for $\epsilon$ into (7.16), we obtain the given result. QED.

The estimate (7.18) shows that the global error of Euler's method is proportional to the maximal step size $\left| h \right| .$ Thus, for an accuracy of, say， three decimal digits, we would need about a thousand steps; a precision of six digits will normally require a million steps etc. We see thus that the present method is not recom mended for computations of high precision. In fact, the main subject of Chapter II will be to find methods which converge faster.

# Existence theorem of Peano

Si a est un complexe d'ordre n , et $^ b$ un nombre reel, alors on peut determiner $b ^ { \prime }$ et $f$ ,ou $b ^ { \prime }$ est une quantite plus grande que $b$ ,et $f$ est un signe de fonction qui a chaque nombre de I'intervalle de $b \ a \ b ^ { \prime }$ fait correspondre un complexe (en d'autres mots, $f t$ est un complexe fonction de la variable reelle t , definie pour toutes les valeurs de l'intervalle $\left( b , b \right) )$ ； la valeur de $f t$ pour $\scriptstyle t = b$ est a ; et dans tout l'intervalle $( b , b ^ { \prime } )$ cette fonction $f t$ satisfait a l'équation différentielle donnee.   
(Original version of Peano's Theorem)

The Lipschitz condition (7.7) is a crucial tool in the proof of (7.10) and finally of the Convergence Theorem. If we completely abandon condition (7.7) and only require that $f \left( x , y \right)$ be continuous, the convergence of the Euler polygons is no longer guaranteed.

An exam ple, plotted in Figure 7.2, is given by the equation

$$
y ^ { \prime } = 4 { \biggl ( } \operatorname { s i g n } ( y ) \left| y \right| ^ { 1 / 2 } + \operatorname { m a x } ( 0 , x - { \frac { | y | } { x } } ) \cdot \cos ( { \frac { \pi \log x } { \log 2 } } ) { \biggr ) }
$$

with $y \left( 0 \right) { = } 0$ . It has been constructed such that

$$
\begin{array} { r l r } & { f \left( h , 0 \right) = 4 h \left( - 1 \right) ^ { i } } & { \mathrm { f o r } \quad h = 2 ^ { - i } \ , } \\ & { f \left( x , y \right) = 4 \mathrm { s i g n } ( y ) \cdot \left| y \right| ^ { 1 / 2 } } & { \mathrm { f o r } \ \left| y \right| \geq x ^ { 2 } \ . } \end{array}
$$

There is an infinity of solutions for this initial value, some of which are plotted in Figure 7.2. The Euler polygons converge for $h = 2 ^ { - i }$ and even i to the maximal solution $y = 4 x ^ { 2 }$ ,and for odd $i$ to $y = - 4 x ^ { 2 }$ For other sequences of $h$ all intermediate solutions can be obtained as well.

![](images/0206b1eae4b64112104b6a1d8be2d4793de08209d21ba59c0d512ba561fc08f6.jpg)  
Figure 7.2. Solution curves and Euler polygons for Equation (7.19)

Theorem 7.6. (Peano (1890)). Let $f \left( x , y \right)$ be continuous and $\mid f \mid$ be bounded by A on

$$
D \ = \ \left\{ ( x , y ) | x _ { 0 } { \le } x \le X \ , | y - y _ { 0 } | \ { \le } \ b \right\} \ .
$$

1f $X ^ { - x } _ { 0 } { \le } { b } / A$ ， then there is a subsequence of the sequence of the Euler polygons which converges to a solution of the differential equation.

The original proof of Peano is, in its crucial part on the conver-gence result, very brief and not clear to unexperienced readers such as we. Arzela (1895)，who took up the subject again, explains his ideas in more detail and emphasizes the need for an equicontinuity of the sequence. The proof usually given nowadays (for what has become the theorem of Arzela-Ascoli), was only introduced later (see e.g. Perron (1918), Hahn (1921), p.303) and is sketched as follows:

Proof: Let

$$
\nu _ { 1 } ( x ) ~ , ~ \nu _ { 2 } ( x ) ~ , ~ \nu _ { 3 } ( x ) , \cdot \cdot \cdot
$$

be a sequence of Euler polygons for decreasing step sizes. It follows from (7.4) that for fixed $x$ this sequence is bounded. We choose a sequence of numbers $r _ { 1 } , r _ { 2 } , r _ { 3 } , . .$ dense in the interval $( x _ { 0 } , X )$ . There is now a subsequence of (7.20) which converges for $\boldsymbol { x } - \boldsymbol { r } _ { 1 }$ (Bolzano-Weierstrass), say

$$
\nu _ { 1 } ^ { ~ ( 1 ) } ( x ) ~ , ~ \nu _ { 2 } ^ { ~ ( 1 ) } ( x ) ~ , ~ \nu _ { 3 } ^ { ~ ( 1 ) } ( x ) ~ , ~ \cdot \cdot \cdot
$$

We next select a subsequence of (7.21) which converges for $\boldsymbol { x } = \boldsymbol { r } _ { 2 }$

$$
\nu _ { 1 } ^ { \ ( 2 ) } ( x ) \ , \quad \nu _ { 2 } ^ { \ ( 2 ) } ( x ) \ , \quad \nu _ { 3 } ^ { \ ( 2 ) } ( x ) \ , \ \cdots
$$

and so on. Then take the "diagonal" sequence

$$
\nu _ { 1 } ^ { \ ( 1 ) } ( x ) \ , \quad \nu _ { 2 } ^ { \ ( 2 ) } ( x ) \ , \quad \nu _ { 3 } ^ { \ ( 3 ) } ( x ) \ , \ \cdot \ \cdot \ 
$$

which, apart from a finite number of terms, is a subscquence of all these sequences, and thus converges for all $r _ { i }$ . Finally, with the estimate

$$
| \nu _ { n } ^ { ( n ) } ( x ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) | \leq A ~ | x - r _ { j } |
$$

(see (7.4))， which expresses the equicontinuity of the sequence, we obtain

$$
\begin{array} { r l } & { \vert \nu _ { n } ^ { ( n ) } ( x ) - \nu _ { m } ^ { ( m ) } ( x ) \vert } \\ & { \leq \vert \nu _ { n } ^ { ( n ) } ( x ) - \nu _ { n } ^ { ( n ) } ( r _ { j } ) \vert + \vert \nu _ { n } ^ { ( n ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) \vert } \\ & { \phantom { = } + \vert \nu _ { m } ^ { ( m ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( x ) \vert } \\ & { \leq 2 A \vert x - r _ { j } \vert + \vert \nu _ { n } ^ { ( n ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) \vert \ . } \end{array}
$$

For fixed $\epsilon > 0$ we then choose a finite subset $R$ of $\{ \boldsymbol { r } _ { 1 }$ ， $r _ { 2 } , \ldots \}$ satisfying $\operatorname* { m i n } \{ | x - r _ { j } | \vert r _ { j } \in R \ , \ x _ { 0 } { \le } x \le X \} { \le } \epsilon / A$ and secondly we choose $N$ such that

$$
| \nu _ { n } ^ { ( n ) } ( r _ { j } ) - \nu _ { m } ^ { ( m ) } ( r _ { j } ) | \leq \ e \quad \mathrm { ~ f o r ~ } \ n , m \geq N \quad \mathrm { a n d ~ } \ r _ { j } \in { \cal R } .
$$

This shows the uniform convergence of (7.23). In the same way as in part b) of the proof of Theorem 7.3 it follows that the limit function is a solution of (7.1). One only has to add an $\mathbf { O } ( \mid h \mid )$ -term in (7.14), if $x$ is not a subdivision point. QED.

# Exercises

1. Apply Euler's method with constant step size $x _ { i + 1 } - x _ { i } = 1 / n$ to the differential equation $y ^ { \prime } { = } k y$ ， $y \left( 0 \right) = 1$ and obtain a classical approxi-mation for the solution $y \left( 1 \right) = e ^ { k } .$ Give an estimate of the error.

2. Apply Euler's method with constant step size to

$$
\begin{array} { l l } { { ) } } & { { y ^ { \prime } = y ^ { 2 } , \qquad y ( 0 ) = 1 , \qquad y ( \displaystyle \frac { 1 } { 2 } ) = ? } } \\ { { ) } } & { { y ^ { \prime } = x ^ { 2 } + y ^ { 2 } , \qquad y ( 0 ) = 0 , \quad y ( \displaystyle \frac { 1 } { 2 } ) = ? } } \end{array}
$$

Make rigorous error estimates using Theorem 7.4 and compare these estimates with the actual errors. The main difficulty is to find a suitable region in which the estimates of Theorem $7 . 4 \ \mathrm { h o l d }$ ， without making the constants $A \ , \ L \ , \ M$ too large and, at the same time,ensuring that the solution curves remain inside this region (see also I.8, Exercise 3).

3. Prove the result: if the differential equation $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 }$ with $f$ continuous, possesses a unique solution, then the Euler polygons converge to this solution.

4. "There is an elementary proof of Peano's existence theorem" (Walter (1971)). Suppose that A is a bound for $\mid f$ 1. Then the sequence

$$
y _ { i + 1 } = y _ { i } + h \operatorname* { m a x } \{ f \left( x , y \right) \mid x _ { i } \leq x \leq x _ { i + 1 } , y _ { i } - 3 A h \leq y \leq y _ { i } + A h \}
$$

converges for all continuous $f$ to a (the maximal) solution. Try to prove this. Unfortunately， this proof does not extend to systems of equations, unless they are "quasimonotone" (see Section I.10, Exercise 3).

# 1.8. Existence Theory using Iteration Methods and Taylor series

A second access to existence theory is possible with the help of an iterative refinement of approximate solutions. The first appearances of the idea are very old. For instance many examples of this type can be found in the work of Lagrange, above all in his astronomical calculations. Let us consider here the following illustrative example of a Riccati equation

$$
y ^ { \prime } = x ^ { 2 } + y + 0 . 1 y ^ { 2 } ~ , ~ y ( 0 ) = 0 ~ .
$$

Due to the presence of the quadratic term, there is no elementary solution. A very natural idea is therefore to neglect this term，which in fact is very small at the beginning,and to solve for the moment

$$
y _ { 1 } ^ { \prime } = x ^ { 2 } + y _ { 1 } ~ , ~ y _ { 1 } ( 0 ) = 0 ~ .
$$

This gives, with the help of Formula (3.3), a first solution

$$
y _ { 1 } ( x ) = 2 e ^ { x } - ( x ^ { 2 } + 2 x + 2 ) \ .
$$

With the help of this solution, we now know more about the initially neglected term $0 . 1 y ^ { 2 } ;$ it will be close to $0 . 1 y _ { 1 } ^ { 2 }$ . So the idea lies at hand to reintroduce this solution into (8.1) and now solve the differential equation

$$
y _ { 2 } ^ { \prime } = x ^ { 2 } + y _ { 2 } + 0 . 1 \bigl ( y _ { 1 } ( x ) \bigr ) ^ { 2 } , y _ { 2 } ( 0 ) = 0 \ ,
$$

We can use Formula (3.3) again and obtain after some calculations

$$
\begin{array} { l } { { y _ { 2 } ( x ) = y _ { 1 } ( x ) + \displaystyle \frac { 2 } { 5 } e ^ { 2 x } - \displaystyle \frac { 2 } { 1 5 } e ^ { x } ( x ^ { 3 } + 3 x ^ { 2 } + 6 x - 5 4 ) } } \\ { { - \displaystyle \frac { 1 } { 1 0 } ( x ^ { 4 } + 8 x ^ { 3 } + 3 2 x ^ { 2 } + 7 2 x + 7 6 ) . } } \end{array}
$$

This is already much closer to the correct solution, as can be seen from the following comparison of the errors $e _ { 1 } { = } y ( x ) { - } y _ { 1 } ( x )$ and $e _ { 2 } { = } y ( x ) { - } y _ { 2 } ( x )$ ：

$$
\begin{array} { l l l } { { x = 0 . 2 } } & { { \ e _ { 1 } = 0 . 2 2 8 \times 1 0 ^ { - 0 7 } } } & { { e _ { 2 } = 0 . 2 3 3 \times 1 0 ^ { - 1 2 } } } \\ { { x = 0 . 4 } } & { { e _ { 1 } = 0 . 3 2 7 \times 1 0 ^ { - 0 5 } } } & { { e _ { 2 } = 0 . 5 6 6 \times 1 0 ^ { - 0 9 } } } \\ { { x = 0 . 8 } } & { { e _ { 1 } = 0 . 5 3 4 \times 1 0 ^ { - 0 3 } } } & { { e _ { 2 } = 0 . 1 6 5 \times 1 0 ^ { - 0 5 } \ , } } \end{array}
$$

It looks promising to continue this process, but the computations soon become very tedious.

# Picard iteration

The general formulation of the method is the following: we try, if possible, to split up the function $f \left( x , y \right)$ of the differential equation

$$
y ^ { \prime } = f ( x , y ) = f _ { 1 } ( x , y ) + f _ { 2 } ( x , y ) , \qquad y ( x _ { 0 } ) = y _ { 0 }
$$

so that any differential equation of the form $y ^ { \prime } { = } f _ { 1 } ( x , y ) { + } g \left( x \right)$ can be solved analytically and so that $f _ { 2 } ( x , y )$ is small. Then we start with a first approxim ation $y _ { 0 } ( x )$ and compute successively $y _ { 1 } ( x )$ ， $y _ { 2 } ( x ) , . . . .$ by solving

$$
y _ { i + 1 } ^ { \prime } = f _ { 1 } ( x , y _ { i + 1 } ) + f _ { 2 } ( x , y _ { i } ( x ) ) \ , y _ { i + 1 } ( x _ { 0 } ) = y _ { 0 } \ .
$$

The most primitive form of this process is obtained by choosing $f _ { 1 } { = } 0 , f _ { 2 } { = } f$ ，in which case (8.6) is immediately integrated and becomes

$$
y _ { i + 1 } ( x ) = y _ { 0 } + \intop _ { x _ { 0 } } ^ { x } f \left( s , y _ { i } ( s ) \right) d s .
$$

This is called the Picard iteration method. It appeared several times in the literature, e.g. in Liouville (1838)， Cauchy， Peano (1888), Lindelof (1894)， Bendixson (1893). Picard (1890) considered it merely as a by-product of a similar idea for partial differential equations and analyzed it thoroughly in his famous treatise Picard (1891- 96), Vol.II, Chap.XI, Sect.III.

The main practical drawback of the method is the need for the repeated computation of integrals, which is usually not very convenient, if at all possible， and soon becomes very tedious. On the other hand, the method is a good tool for theoretical investigations.

Its fast convergence, for $| x - x _ { 0 } |$ small, is readily seen: if we subtract formula (8.7) from the same with i replaced by $i - 1$ , we have

$$
y _ { i + 1 } ( x ) - y _ { i } ( x ) = \int _ { x _ { 0 } } ^ { x } \biggl ( f \left( s , y _ { i } ( s ) \right) - f \left( s , y _ { i - 1 } ( s ) \right) \biggr ) d s .
$$

We now apply the Lipschitz condition (7.7) and the triangle inequality to obtain

$$
| y _ { i + 1 } ( x ) - y _ { i } ( x ) | \leq L \intop _ { x _ { 0 } } ^ { x } | y _ { i } ( s ) - y _ { i - 1 } ( s ) | d s .
$$

When we assume $y _ { 0 } ( x ) \equiv y _ { 0 } ,$ ， we have from the triangle inequality

applied to (8.7) with $i = 0$ the estim ate

$$
| y _ { 1 } ( x ) - y _ { \ 0 } ( x ) | \le A \ | x - x _ { 0 } |
$$

where A is, as in Section I.7, a bound for $\left| f \right|$ . We next insert this into the right hand side of (8.9) repeatedly to obtain finally the estimate

$$
| y _ { i } ( x ) - y _ { i - 1 } ( x ) | \leq A L ^ { i - 1 } { \frac { | x - x _ { 0 } | ^ { i } } { i ! } } ~ .
$$

Theright-handsideiaterof theTaylorseriesforexl which converges for all $\mathcal { A }$ ; we therefore conclude that $| y _ { i + k } - y _ { i } |$ becomes arbitrarily small when i is large. The error is bounded by the remainder of the above exponential series. So the sequence $y _ { i } ( x )$ converges uniformly to the solution $y \left( x \right)$ . For example, if $L \ | x - x _ { 0 } | \leq 1 / 1 0$ and the constant A is moderate, 10 iterations would provide a numerical solution with about 17 correct digits.

# Taylor Series

"Apres avoir montre l'insufsance des methodes d'integration fondees sur le developpement en series, il me reste a dire en peu de mots ce qu’on peut leur substituer."   
(Cauchy)

A third possible existence proof can be based on a study of the convergence of the Taylor series of the solutions. This was mentioned in a footnote of Liouville (1836, p.255)， and brought to perfection by Cauchy (1839-42).

We have already seen the recursive computation of the Taylor coefficients in the work of Newton (see Section I.2). Euler (1768) then formulated the general procedure for the higher derivatives of the solution of

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 }
$$

which, by successive differentiation, are obtained as

$$
\begin{array} { c } { y ^ { \prime \prime } = f _ { x } + f _ { y } y ^ { \prime } = f _ { x } + f _ { y } f } \\ { y ^ { \prime \prime \prime } = f _ { x x } + 2 f _ { x y } f + f _ { y y } f ^ { 2 } + f _ { y } ( f _ { x } + f _ { y } f ) } \end{array}
$$

etc. Then the solution is

$$
y \left( x _ { 0 } \mathbf { + } h \right) = y \left( x _ { 0 } \right) + y ^ { \prime } ( x _ { 0 } ) h + y ^ { \prime \prime } ( x _ { 0 } ) { \frac { h ^ { 2 } } { 2 ! } } + \cdot \cdot \cdot .
$$

The formulas (8.12) for higher derivatives soon become very complicated. Euler therefore proposed to use only a few terms of this series with $h$ sufficiently small and to repeat the computations from the point ${ { x } _ { 1 } } ^ { = } { { x } _ { 0 } } ^ { + h }$ ("analytic continuation").

# Convergence proof

We shall now outline the main ideas of Cauchy's convergence proof for the series (8.13). We suppose that $f \left( x , y \right)$ is analytic in the neighbourhood of the initial value $x _ { 0 } , y _ { 0 }$ , which for simplicity of notation we assume located at the origin ${ x _ { 0 } } \mathrm { { = } } { y _ { 0 } } \mathrm { { = } } 0$ ：

$$
f ( x , y ) = \sum _ { i , j \geq 0 } a _ { i j } x ^ { i } y ^ { j } ,
$$

where the $a _ { i j }$ are multiples of the partial derivatives occurring in (8.12). If the series (8.14) is assumed to converge for $\{ x \mid \leq r , \mid y \mid \leq r$ then the Cauchy inequalities from classical complex analysis give

$$
| a _ { i j } | ~ \leq ~ { \frac { M } { r ^ { i + j } } } ~ , \quad \mathrm { w h e r e } ~ M ~ = ~ \operatorname* { m a x } _ { \left| x ~ \left| \leq r ~ , ~ \right| y ~ \right| \leq r } \left| f \left( x ~ , y \right) \right| ~ .
$$

The idea is now the following: since all signs in (8.12) are positive, we obtain the worst possible result if we replace in (8.14)al $a _ { i j }$ by the largest possible values (8.15) ("method of majorants"):

$$
f \left( x , y \right) \to \sum _ { i , j \geq 0 } M \frac { x ^ { i } y ^ { j } } { r ^ { i + j } } = \frac { M } { \left( 1 - x / r \right) \left( 1 - y / r \right) } .
$$

However, the majorizing differential equation

$$
y ~ ^ { \prime } = ~ { \frac { M } { ( 1 - x ~ / r ) ( 1 - y ~ / r ) } } ~ , \qquad y ( 0 ) { = } 0
$$

is readily integrated by separation of variables (see Section I.3) and has the solution

$$
y ~ = r \left( 1 - \left( 1 + 2 M \log ( 1 - \frac { x } { r } ) \right) ^ { 1 / 2 } \right) ~ ,
$$

This solution has a power series which converges for all $x$ such that $| 2 M \log ( 1 { - } x / r ) | { < } 1$ .Therefore, the series (8.13) also converges at least for all $\mid h \mid < r ( 1 { - } \exp ( - 1 / 2 M ) )$ . QED.

# Recursive Computation of Taylor Coefficients

"...dieses Verfahren praktisch nicht in Frage kommen kann".   
(Runge-Konig, 1924)   
"The exact opposite is true, if we use the right approach .."   
(R.E. Moore, 1979)

The "right approach" is, in fact, an extension of Newton's approach and has been rediscovered several times (e.g. Steffensen (1956)) and implemented in generality into computer programs by Gibbons (1960) and Moore (1966). For a more extensive bibliography see the references in Wanner (1969), p.10-20.

The idea is the following: let

$$
Y _ { i } = \frac { 1 } { i ! } y ^ { ( i ) } ( x _ { 0 } ) , F _ { i } = \frac { 1 } { i ! } \bigg ( f \left( x , y \left( x \right) \right) \bigg ) ^ { ( i ) } \vert _ { x = x _ { 0 } }
$$

be the Taylor coefficients of $y \left( x \right)$ and of $f \left( x , y \left( x \right) \right)$ , so that (8.13) becomes

$$
y \left( x _ { 0 } { + } h \right) = \sum _ { i = 0 } ^ { \infty } h ^ { i } Y _ { i } .
$$

Then, from (8.11),

$$
Y _ { i + 1 } = { \frac { 1 } { i + 1 } } F _ { i } .
$$

Now suppose that $f \left( x , y \right)$ is the composition of a sequence of algebraic operations and elementary functions. This leads to a sequence of items,

$$
x , y , p , q , r \ , \ldots , \mathrm { ~ a n d ~ f i n a l l y } \ f .
$$

For each of these items we find formulas for generating the $i - t h$ Taylor coefficient from the preceding ones as follows:

a) $r = p \pm q$

$$
R _ { i } = P _ { i } \pm Q _ { i } \qquad i = 0 , 1 , \cdots
$$

b) $r = p q$

$$
R _ { i } = \sum _ { j = 0 } ^ { i } P _ { j } Q _ { i - j } i = 0 , 1 , \cdots
$$

(the Cauchy product).

c） $r \ = p / q$ : write $p = r q$ , use formula b) and solve for $R _ { i }$ ：

$$
R _ { i } = { \frac { 1 } { Q _ { 0 } } } \biggl ( P _ { i } - \sum _ { j = 0 } ^ { i - 1 } R _ { j } Q _ { i - j } \biggr ) \qquad i = 0 , 1 , \cdots ,
$$

There also exist formulas for many elementary functions (in fact, because these functions are themselves solutions of rational differential equations). Examples:

d） $r = \exp ( p )$ : use $r ^ { \prime } { = } p ^ { \prime } { \cdot } r$ and apply (8.20.b). This gives (for $i = 1 , 2 , \ldots ,$

$$
R _ { 0 } = \exp ( P _ { 0 } ) , ~ R _ { i } = \frac { 1 } { i } \sum _ { j = 0 } ^ { i - 1 } ( i { - } j ) R _ { j } P _ { i { - } j } ~ .
$$

e） $r = \log ( p )$ : use $p { = } \mathbf { e x p } ( r )$ and rearrange formula d). This gives

$$
R _ { 0 } = \log ( P _ { 0 } ) , \quad R _ { i } = \frac { 1 } { P _ { 0 } } \biggl ( P _ { i } - \frac { 1 } { i } \sum _ { j = 1 } ^ { i - 1 } ( i - j ) P _ { j } R _ { i - j } \biggr ) \ .
$$

f） $r = p ^ { c } , c \neq 1$ constant. Use $\boldsymbol { r ^ { \prime } } { = } \boldsymbol { c p } ^ { c - 1 } \boldsymbol { p }$ ',i.e. ${ p r } ^ { \prime } { = } c r p ^ { \prime }$ and apply (8.20.b)

$$
R _ { 0 } ^ { c } ~ , ~ R _ { i } ^ { } ~ = ~ { \frac { 1 } { i P _ { 0 } } } \bigg ( \sum _ { j = 0 } ^ { i - 1 } ( c i - ( c + 1 ) j ) R _ { j } ^ { } P _ { i - j } ^ { } \bigg ) ~ .
$$

g） $r = \cos ( p ) , s = \sin ( p ) ;$ as in d) we have

$$
\begin{array} { l } { { \displaystyle { R _ { 0 } = \mathrm { c o s } P _ { 0 } , \quad R _ { i } = - \frac { 1 } { i } \sum _ { j = 0 } ^ { i - 1 } ( i - j ) S _ { j } P _ { i - j } } . } } \\ { { \displaystyle { S _ { 0 } = \mathrm { s i n } P _ { 0 } , \quad S _ { i } = \frac { 1 } { i } \sum _ { j = 0 } ^ { i - 1 } ( i - j ) R _ { j } P _ { i - j } } . } } \end{array}
$$

The alternating use of (8.20) and (8.18) then allows us to compute the Taylor coefcients for (8.17) to any wanted order in a very economical way. It is not difficult to write subroutines for the above formulas, which have to be called in the same order as the differential equation (8.11) is composed of elementary operations. There also exist computer programs which "compile" Fortran statements for $f \left( x , y \right)$ into this list of subroutine calls. One has been written by T.Szym anski and J.H.Gray (see Knapp-Wanner (1969)).

Example. The diferential equation $y ^ { \prime } { = } x ^ { 2 } { + } y ^ { 2 }$ leads to the recursion $\scriptstyle { Y _ { 0 } = y ( 0 ) }$ ，

$$
Y _ { i + 1 } = { \frac { 1 } { i + 1 } } \left( P _ { i } + \sum _ { j = 0 } ^ { i } Y _ { j } Y _ { i - j } \right) \qquad i = 0 , 1 , \ \cdot \ \cdot \ .
$$

where ${ \bar { P } } _ { i } = 1$ for $i = 2$ and ${ \boldsymbol { P } } _ { i } = 0$ for $i \neq 2$ are the coefficients for $x ^ { 2 }$ .One can imagine how much easier this is than Formulas (8.12).

An important property of this approach is that it can be executed in interval analysis and thus allows us to obtain reliable error bounds by

the use of Lagrange's error formula for Taylor series. We refer to the books by R.E. Moore (1966) and (1979) for more details.

# Exercises

1. Obtain from (8.10) the estimate

$$
| y _ { i } ( x ) - y _ { 0 } | ~ \le ~ \frac { 1 } { L } \left( e ^ { L \left( x - x _ { 0 } \right) } - 1 \right) A
$$

and explain the similarity of this result with (7.16).

2. Apply the method of Picard to the problem $y ^ { \prime } { = } K y$ ， $y \left( 0 \right) { = } 1$

3. Compute three Picard iterations for the problem $y ^ { \prime } { = } x ^ { 2 } { + } y ^ { 2 }$ ， $y \left( 0 \right) { = } 0$ ， $y \left( 1 / 2 \right) = ?$ and make a rigorous error estimate. Compare the result with the correct solution y(1/2)=0.041791146154681863220768806849179 .

4. Compute with an iteration method the solution of

$$
y ^ { \prime } = \sqrt { x } + \sqrt { y } , \qquad y \left( 0 \right) = 0
$$

and observe that the method can work well for equations which pose serious problems with other methods. An even greater difference occurs for the equations

$$
y ^ { \prime } = \sqrt { x } + { y ^ { 2 } } , y ( 0 ) = 0 \mathrm { ~ a n d ~ } y ^ { \prime } = \frac { 1 } { \sqrt { x } } + { y ^ { 2 } } , y ( 0 ) = 0 .
$$

5. Define $f \left( x , y \right)$ by

$$
f \left( x , y \right) = \left\{ \begin{array} { l l } { 0 } & { \mathrm { f o r ~ } x \leq 0 } \\ { \displaystyle 2 x } & { \mathrm { f o r ~ } x > 0 ~ , \quad y < 0 } \\ { \displaystyle 2 x - \frac { 4 y } { x } } & { \mathrm { f o r ~ } x > 0 ~ , \quad 0 \leq y \leq x ^ { 2 } } \\ { \displaystyle - 2 x } & { \mathrm { f o r ~ } x > 0 ~ , \quad x ^ { 2 } < y ~ . } \end{array} \right.
$$

a) Show that $f \left( x , y \right)$ is continuous, but not Lipschitz.

b) Show that for the problem $y ^ { \prime } { = } f \left( x , y \right)$ ， $y \left( 0 \right) { = } 0$ the iteration method does not converge.

c) Show that there is a unique solution and that the Euler polygons converge.

6. Use the method of Picard iteration to prove: If $f \left( x , y \right)$ is continuous and satisfies a Lipschitz condition (7.7)

on the infinite strip $D = \{ ( x \ , \ y ) ; x _ { 0 } { \leq } x { \leq } X \}$ , then the initial value problem $y ^ { \prime } { = } f \left( x \ , \ y \right)$ ， $y \left( x _ { 0 } \right) { = } y _ { 0 }$ possesses a unique solution on $x _ { 0 } \leq x \leq X$

Compare this global result with Theorem 7.3.

7. Define a function $y \left( x \right)$ (the "inverse error function") by the relation

$$
x : = \frac { 2 } { \sqrt { \pi } } \int _ { 0 } ^ { y } e ^ { - t ^ { 2 } } d t
$$

and show that it satisfies the differential equation

$$
y ^ { \prime } = \frac { \sqrt { \pi } } { 2 } e ^ { y ^ { 2 } } , \qquad y \left( 0 \right) { = } 0 .
$$

Obtain recursion formulas for its Taylor coefficients.

I.9. Existence theory for systems of equations

The first treatment of an existence theory for simultaneous systems of differential equations was undertaken in the last existing pages (p.123-136) of Cauchy (1824). Using the index notation, which at that time was not yet en vogue, we write the equations as

$$
\begin{array} { c c c } { { y _ { 1 } ^ { \prime } = f _ { 1 } ( x , y _ { 1 } , \ldots , y _ { n } ) ~ , } } & { { } } & { { y _ { 1 } ( x _ { 0 } ) = y _ { 1 0 } ~ , } } \\ { { \ldots } } & { { } } & { { \ldots } } \\ { { y _ { n } ^ { \prime } = f _ { n } ( x , y _ { 1 } , \ldots , y _ { n } ) ~ , } } & { { } } & { { y _ { n } ( x _ { 0 } ) = y _ { n 0 } ~ , } } & { { y _ { n } ( X ) = 7 } } \end{array}
$$

and ask for the existence of the n solutions $y _ { 1 } ( x ) , \ldots , y _ { n } ( x ) .$ As the equations (9.1) prescribe, for any given $y _ { 1 } , \ldots , y _ { n }$ , the derivatives of these functions, it is again natural to consider, in analogy to (7.3), the method of Euler

$$
y _ { k , i + 1 } = y _ { k i } + ( x _ { i + 1 } - x _ { i } ) \cdot f _ { k } ( x _ { i } , y _ { 1 i } , . . . , y _ { n i } )
$$

$$
k = 1 , . . . , n , \quad i = 0 , 1 , 2 , \cdot \cdot \cdot ,
$$

Here $y _ { k i }$ is intended to approximate $y _ { k } \left( x _ { i } \right)$ ,where $x _ { 0 } { < } x _ { 1 } { < } x _ { 2 } { ~ } { \cdot } { } ~ { \cdot } ~ .$ is a subdivision of the interval of integration as in (7.2).

We now try to carry over everything we have done in Section I.7 to the new situation. Although we have no problem in extending (7.4) to the estim ate

$$
| y _ { k i } - y _ { k 0 } | \ \leq \ A _ { k } \ | x _ { i } - x _ { 0 } | \qquad \mathrm { i f } \quad | f _ { k } \left( x \ , y _ { 1 } \ldots , y _ { n } \right) | \ \leq \ A _ { k } \ ,
$$

things become a little more complicated for (7.7): we have to estimate

$$
\begin{array} { r l r } {  { f _ { k } ( x , z _ { 1 } , \dots , z _ { n } ) - f _ { k } ( x , y _ { 1 } , \dots , y _ { n } ) } } \\ & { } & { \quad = \frac { \partial f _ { k } } { \partial y _ { 1 } } { \cdot } ( z _ { 1 } { - } y _ { 1 } ) + \cdot \cdot \cdot + \frac { \partial f _ { k } } { \partial y _ { n } } ( z _ { n } { - } y _ { n } ) \ , } \end{array}
$$

where the derivatives $\partial f _ { k } / \partial y _ { i }$ are taken at suitable intermediate points. Here Cauchy uses the inequality which he invented just before and which now is called the "Cauchy-Schwarz inequality" ("Enfin, il resulte de la formule (13) de la 11e lecon du calcul differentiel ..") to obtain

$$
| f _ { k } ( x , z _ { 1 } , . . . , z _ { n } ) - f _ { k } ( x , y _ { 1 } , . . . , y _ { n } ) |
$$

$$
\leq \left( { \bigl ( } { \frac { \partial f _ { k } } { \partial y _ { 1 } } } { \bigr ) } ^ { 2 } + \cdot \cdot \cdot + { \bigl ( } { \frac { \partial f _ { k } } { \partial y _ { n } } } { \bigr ) } ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \left( { \bigl ( } z _ { 1 } { - } y _ { 1 } { \bigr ) } ^ { 2 } + \cdot \cdot \cdot + { \bigl ( } z _ { n } { - } y _ { n } { \bigr ) } ^ { 2 } \right) ^ { \frac { 1 } { 2 } } .
$$

At this stage, we begin to feel that further development is advisable only after the introduction of vector notation.

# Vector notation

This was promoted in our subject by the papers of Peano, (1888) and (1890)，who was influenced, as he says, by the famous "Ausdehnungslehre" of Grassmann and the work of Hamilton, Cayley, and Sylvester. We introduce the vectors (Peano called them "complexes")

$$
y = ( y _ { 1 } , \ldots , y _ { n } ) ^ { T } , y _ { i } = ( y _ { 1 i } , \ldots , y _ { n i } ) ^ { T } , z = ( z _ { 1 } , \ldots , z _ { n } ) ^ { T }
$$

and hope that the reader will not confuse the components $y _ { i }$ of a vector y with vectors with indices. We consider the "vector function" $f \left( x , y \right) = \left( f _ { 1 } ( x , y ) , \ldots , f _ { n } \left( x , y \right) \right) ^ { T }$ , so that Equations (9.1) become

$$
y ^ { \prime } = f \left( x , y \right) , \qquad y \left( x _ { 0 } \right) = y _ { 0 } , \qquad y \left( X \right) = ?
$$

and Euler's method (9.2) is

$$
y _ { i + 1 } = y _ { i } + ( x _ { i + 1 } - x _ { i } ) f ( x _ { i } , y _ { i } ) \ \quad \quad i = 0 , 1 , 2 , { \mathrm { ~ e t c } } \ .
$$

There is no longer any difference in notation with the onedimensional cases (7.1) and (7.3).

$y = ( y _ { 1 } , \ldots , y _ { n } ) ^ { T }$ trce

$$
\parallel y \parallel = { \bigl ( y _ { 1 } ^ { ~ 2 } + \dots + y _ { n } ^ { ~ 2 } \bigr ) ^ { 1 / 2 } }
$$

which satisfies all the usual properties of a norm, for exam ple the tri-angle inequality

$$
\| { \textbf { \it y } } + z \| \ \leq \ \| { \textbf { \it y } } \| + \| { \textbf { \it z } } \| , \| \sum _ { i = 1 } ^ { m } \| \leq \sum _ { i = 1 } ^ { m } \| { \textbf { \it y } } _ { i } \| .
$$

We now are able to formulate Estimates (9.3) and (9.5) as follows, in perfect analogy with (7.4) and (7.7):

Theorem 9.1. Suppose that $\left| \left| ~ f \left( x , y \right) \right| \right| \leq A$ ; then we have for the $y _ { i }$ defined by (9.2') the estimate

$$
\begin{array} { r } { \left| \left| ~ y _ { i } - y _ { 0 } \right| \right| ~ \leq ~ A ~ | x _ { i } - x _ { 0 } | ~ . } \\ { I f ~ | ~ \frac { \partial f _ { k } } { \partial y _ { i } } | ~ \leq ~ q _ { k i } , { t h e n } ~ } \end{array}
$$

$$
\begin{array} { r l } { { \left\| \begin{array} { l } { f \left( x , z \right) - f \left( x , y \right) | } \end{array} } } & {\right\ { } \leq L \ \left\| \begin{array} { l } { z - y } \end{array} \right\| } \\ { } & { { } } \\ { w h e r e \quad L } & { { } = \bigg ( \sum _ { i , k } q _ { k i } ^ { 2 } \bigg ) ^ { 1 / 2 } . } \end{array}
$$

Proof: (9.9) is obtained by squaring (9.5) and adding up for $k = 1 , \ldots , n$ . QED.

The estimate (9.9) is called the "mean value theorem" and can be found in many books on analysis.

The Euclidean norm (9.6) is not the only one possible, we also use ("on pourrait aussi definir par $m x$ la plus grande des valeurs absolues des elements de x ; alors les proprietes des modules sont presqu'evidentes." (Peano))

$$
\parallel y \parallel = \operatorname* { m a x } ( \mid y _ { 1 } \mid , . . . , \mid y _ { n } \mid ) .
$$

In this case, in order to establish (9.9), we estimate (9.4) in the following way:

$$
| f _ { k } ( x , z ) - f _ { k } ( x , y ) | \leq \bigg ( | \frac { \partial f _ { k } } { \partial y _ { 1 } } | + \cdot \cdot \cdot + | \frac { \partial f _ { k } } { \partial y _ { n } } | \bigg ) \cdot \operatorname* { m a x } _ { i } ( | z _ { i } - y _ { i } | ) ~ .
$$

Therefore, Theorem 9.1 remains true if we replace (9.10) by

$$
L \ = \ \operatorname* { m a x } _ { k } \left( \sum _ { i } | q _ { k i } | \right) .
$$

Finally, if we want to use the norm

$$
\parallel y \parallel = | y _ { 1 } | + \cdot \cdot \cdot + | y _ { n } | ,
$$

(9.10) of Theorem 9.1 has to be replaced by

$$
L \ = \operatorname* { m a x } _ { i } \left( \sum _ { k } | q _ { k i } | \right) .
$$

In all three cases, we have established a perfect analogy with (7.5) and (7.7) of Section I.7. Al that remains to do is, Da capo al fine, read Sections I.7 and I.8 again: Theorems 7.2, 7.3, 7.4, 7.5, and 7.6 together with their proofs and the estimates (7.10), (7.13),(7.15), (7.16), (7.17), and (7.18) carry over to the more general case with the only changes that some absolute values are to be replaced by norms.

# Subordinate matrix norms

Denote by $Q$ the matrix with elements $q _ { k i } .$ The constant defined in (9.10'), which we now denote by

$$
\parallel \boldsymbol { \mathcal { Q } } \parallel = \operatorname* { m a x } _ { k } \left( \sum _ { i } | q _ { k i } | \right)
$$

is callcd the matrix norm subordinate to the vector norm (9.6'). It is the smallest number which allows the estim ate

$$
\| ~ Q y ~ \| ~ \leq ~ \| ~ Q ~ \| ~ \| ~ y ~ \|
$$

for all vectors y, or, in other words,

$$
\parallel { \cal Q } \parallel = \operatorname* { s u p } _ { y \neq 0 } \frac { \parallel \boldsymbol { Q } y \parallel } { \parallel y \parallel } \mathrm { ~ , ~ }
$$

Similarly, the matrix norm subordinate to the norm (9.6") appears in (9.10"), i.e.

$$
\parallel Q \parallel = \operatorname* { m a x } _ { i } \left( \sum _ { k } | q _ { k i } | \right) .
$$

However, (9.10) (which is called the "Schur norm") is nol subordinate to the norm (9.6), since,although it satisfies (9.12), it is not the smallest possible bound. Here, the subordinate norm is given by

$$
\parallel \boldsymbol { \mathcal { Q } } \parallel = \sqrt { \mathsf { A } _ { \operatorname* { m a x } } } \mathrm { ~ , ~ }
$$

where $\lambda _ { \operatorname* { m a x } }$ is the largest eigenvalue of $Q ^ { T } Q$ . This can be seen from

$$
\parallel Q y \parallel ^ { 2 } = y ^ { T } Q ^ { T } Q y
$$

with the help of an orthogonal transformation of $Q ^ { T } Q$ to diagonal form.

Au these formulas remain valid for complex matrices. Only $Q ^ { T }$ has to be replaced by $Q ^ { * }$ (transposed and complex conjugate). See e.g. Wilkinson (1965), p.55-61, Bakhvalov (1976), Chap. VI, Par. 3.

# Picard iteration for systems

The iteration method of Picard also carres over to systems of equations when in (8.7) we interpret $y _ { i + 1 } ( x ) , y _ { 0 }$ and $f \left( s , y _ { i } ( s ) \right)$ as vectors， integrated componentwise. The convergence result with the estimate (8.10) also remains the same; for its proof we have to use, between (8.8) and (8.9), the inequality

$$
\| \int _ { a } ^ { b } g ( x ) d x \parallel \leq \int _ { a } ^ { b } \| g ( x ) \| d x
$$

for a vector valued function $g \left( x \right) = ( g _ { 1 } ( x ) , \ldots , g _ { n } ( x ) ) ^ { T }$ Equation (9.14) is proved by applying the triangle inequality (9.7) to the finite Riemann sums which define the two integrals.

The Taylor series method, its convergence proof, and the recursive generation of the Taylor coefficients also generalize in a straightforward manner to systems of equations.