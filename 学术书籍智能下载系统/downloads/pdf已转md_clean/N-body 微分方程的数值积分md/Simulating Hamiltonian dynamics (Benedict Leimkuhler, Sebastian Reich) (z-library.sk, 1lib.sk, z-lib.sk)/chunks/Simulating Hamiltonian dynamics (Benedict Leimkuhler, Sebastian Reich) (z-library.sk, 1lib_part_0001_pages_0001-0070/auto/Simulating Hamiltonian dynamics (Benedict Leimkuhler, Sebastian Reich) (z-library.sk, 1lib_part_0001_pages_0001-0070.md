# Simulating Hamiltonian Dynamics

Benedict Leimkuhlerand Sebastian Reich

![](images/cb43057a3dd216a85d752666236137b2cf768290d222495ee70b943cef553de9.jpg)

# Simulating Hamiltonian Dynamics

The Cambridge Monographs on Applied and Computational Mathematics reflects the crucial role of mathematical and computational techniques in contemporary science. The series publishes expositions on all aspects of applicable and numerical mathematics, with an emphasis on new developments in this fast-moving area of research.

State-of-the-art methods and algorithms as well as modern mathematical descriptions of physical and mechanical ideas are presented in a manner suited to graduate research students and professionals alike. Sound pedagogical presentation is a prerequisite. It is intended that books in the series will serve to inform a new generation of researchers.

# Also in this series:

1. A Practical Guide to Pseudospectral Methods, Bengt Fornberg   
2. Dynamical Systems and Numerical Analysis, A. M. Stuart and A. R. Humphries   
3. Level Set Methods and Fast Marching Methods, J. A. Sethian   
4. The Numerical Solution of Integral Equations of the Second Kind, Kendall E. Atkinson   
5. Orthogonal Rational Functions, Adhemar Bultheel, Pablo Gonzalez-Vera, Erik Hendiksen, and´   
Olav Njastad ˚   
6. The Theory of Composites, Graeme W. Milton   
7. Geometry and Topology for Mesh Generation Herbert Edelsfrunner   
8. Schwarz–Christoffel Mapping Tofin A. Driscoll and Lloyd N. Trefethen   
9. High-Order Methods for Incompressible Fluid Flow, M. O. Deville, P. F. Fischer and   
E. H. Mund   
10. Practical Extrapolation Methods, Avram Sidi   
11. Generalized Riemann Problems in Computational Fluid Dynamics, Matania Ben-Artzi and   
Joseph Falcovitz   
12. Radial Basis Functions, Martin D. Buhmann   
13. Iterative Krylov Methods for Large Linear Systems, Henk A. van der Vorst.   
15. Collocation Methods for Volterra Integral and Related Functional Equations, Hermann Brunner.

# Simulating Hamiltonian Dynamics

BENEDICT LEIMKUHLER University of Leicester

SEBASTIAN REICH Imperial College, London

   Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore, São Paulo

Cambridge University Press   
The Edinburgh Building, Cambridge  , UK   
Published in the United States of America by Cambridge University Press, New York   
www.cambridge.org   
Information on this title: www.cambridge.org/9780521772907

$^ ©$ Cambridge University Press 2004

This book is in copyright. Subject to statutory exception and to the provision of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published in print format  2005 - ---- eBook (NetLibrary) - --- eBook (NetLibrary)

- ---- hardback - --- hardback

Cambridge University Press has no responsibility for the persistence or accuracy of s for external or third-party internet websites referred to in this book, and does not guarantee that any content on such websites is, or will remain, accurate or appropriate.

# Contents

# Preface ix

# Acknowledgements xvi

# 1 Introduction

# 1

1.1 N-body problems 2   
1.2 Problems and applications 3   
1.3 Constrained dynamics 6   
1.4 Exercises . 8

# 2 Numerical methods 11

2.1 One-step methods 13   
2.2 Numerical example: the Lennard–Jones oscillator   
2.3 Higher-order methods   
2.4 Runge–Kutta methods   
2.5 Partitioned Runge–Kutta methods   
2.6 Stability and eigenvalues   
2.7 Exercises .

# 3 Hamiltonian mechanics 36

3.1 Canonical and noncanonical Hamiltonian systems 36   
3.2 Examples of Hamiltonian systems 39   
3.3 First integrals 44   
3.4 The flow map and variational equations 48   
3.5 Symplectic maps and Hamiltonian flow maps 52   
3.6 Differential forms and the wedge product 61   
3.7 Exercises . 66

# 4 Geometric integrators 70

4.1 Symplectic maps and methods . 74

4.2 Construction of symplectic methods by Hamiltonian splitting . . 76   
4.3 Time-reversal symmetry and reversible discretizations . 81   
4.4 First integrals 87   
4.5 Case studies 91   
4.6 Exercises . 99

# 5 The modified equations 105

5.1 Forward v. backward error analysis 107   
5.2 The modified equations 117   
5.3 Geometric integration and modified equations 129   
5.4 Modified equations for composition methods 133   
5.5 Exercises . 139

# 6 Higher-order methods 142

6.1 Construction of higher-order methods 143   
6.2 Composition methods 144   
6.3 Runge–Kutta methods 149   
6.4 Generating functions 159   
6.5 Numerical experiments 161   
6.6 Exercises . 165

# 7 Constrained mechanical systems 169

7.1 N-body systems with holonomic constraints 170   
7.2 Numerical methods for constraints 173   
7.3 Transition to Hamiltonian mechanics 184   
7.4 The symplectic structure with constraints 186   
7.5 Direct symplectic discretization 188   
7.6 Alternative approaches to constrained integration 191   
7.7 Exercises . 195

# 8 Rigid body dynamics 199

8.1 Rigid bodies as constrained systems . . . 201   
8.2 Angular momentum and the inertia tensor 210   
8.3 The Euler equations of rigid body motion 212   
8.4 Order 4 and order 6 variants of RATTLE for the free rigid body 223   
8.5 Freely moving rigid bodies 224   
8.6 Other formulations for rigid body motion 228   
8.7 Exercises . 230

# 9 Adaptive geometric integrators 234

9.1 Sundman and Poincar´e transformations 235

9.2 Reversible variable stepsize integration . 238   
9.3 Sundman transformations . 246   
9.4 Backward error analysis . 249   
9.5 Generalized reversible adaptive methods 251   
9.6 Poincar´e transformations 253   
9.7 Exercises . 255

# 10 Highly oscillatory problems 257

10.1 Large timestep methods 258   
10.2 Averaging and reduced equations 269   
10.3 The reversible averaging (RA) method 271   
10.4 The mollified impulse (MOLLY) method 276   
10.5 Multiple frequency systems 279   
10.6 Exercises . 280

# 11 Molecular dynamics 287

11.1 From liquids to biopolymers . 290   
11.2 Statistical mechanics from MD trajectories 296   
11.3 Dynamical formulations for the NVT, NPT and   
other ensembles . 299   
11.4 A symplectic approach: the Nos´e–Poincar´e method 305   
11.5 Exercises . 313

# 12 Hamiltonian PDEs 316

12.1 Examples of Hamiltonian PDEs . . . 316   
12.2 Symplectic discretizations 325   
12.3 Multi-symplectic PDEs 335   
12.4 Exercises . 352   
References . 357   
Index . 374

# Preface

# About geometric integration

This book is about simulating dynamical systems, especially conservative systems such as arise in celestial mechanics and molecular models. We think of the integrator as the beating heart of any dynamical simulation, the scheme which replaces a differential equation in continuous time by a difference equation defining approximate snapshots of the solution at discrete timesteps. As computers grow in power, approximate solutions are computed over ever-longer time intervals, and the integrator may be iterated many millions or even billions of times; in such cases, the qualitative properties of the integrator itself can become critical to the success of a simulation. Geometric integrators are methods that exactly (i.e. up to rounding errors) conserve qualitative properties associated to the solutions of the dynamical system under study.

The increase in the use of simulation in applications has mirrored rising interest in the theory of dynamical systems. Many of the recent developments in mathematics have followed from the appreciation of the fundamentally chaotic nature of physical systems, a consequence of nonlinearities present in even the simplest useful models. In a chaotic system the individual trajectories are by definition inherently unpredictable in the exact sense: solutions depend sensitively on the initial data. In some ways, this observation has limited the scope and usefulness of results obtainable from mathematical theory. Most of the common techniques rely on local approximation and perturbation expansions, methods best suited for understanding problems which are “almost linear,” while the new mathematics that would be needed to answer even the most basic questions regarding chaotic systems is still in its infancy. In the absence of a useful general theoretical method for analyzing complex nonlinear phenomena, simulation is increasingly pushed to the fore. It provides one of the few broadly applicable and practical means of shedding light on the behavior of complex nonlinear systems, and is now a standard tool in everything from materials modeling to bioengineering, from atomic theory to cosmology.

As models grow in complexity and dimension, and the demands placed on simulation have risen, the need for more sophisticated numerical methods and analytic techniques also grows. Longer time interval simulations require more stable methods. Larger problems call for more efficient schemes, tailored to a particular application or family of applications. And more intricate modeling of delicate behaviors or properties requires corresponding improvements in the resolution of those properties during simulation.

In writing this book for a broad audience of scientists, we have attempted to limit the introduction of technical detail, but in some places this cannot be avoided. The calculations are generally included for the benefit of students. We hope that appreciation of the general principles will not be lost in following the details of arguments. In the words of John Von Neumann, “One expects a mathematical theorem or a mathematical theory not only to describe and classify in a simple and elegant way numerous and a priori disparate special cases. One also expects elegance in its architectural, structural make-up. . . . If the deductions are lengthy or complicated there should be some simple general principle involved, which explains the complications and details, reduces the apparent arbitrariness to a few simple guiding motivations.” If there is one such guiding principle underlying our work it is this: classical mechanics – on which all physical models are based – also provides the proper foundation for numerical simulation of those systems. We will attempt to show in this book that practical, efficient methods for simulating conservative systems can be realized by making judicious use of the methods of classical mechanics.

# An emphasis on methods

In this book we address ourselves primarily to the following pair of questions:

Which properties should be fundamental to an integration method for a (conservative) model?

How can we design and implement schemes that respect physical principles regardless of timestep or traditional accuracy considerations?

Although our interest is always ultimately in the methods themselves and in quantifying the relative differences among them, we will find that in attempting to answer the above questions, we are drawn far afield from the usual domain of the numerical analyst. The first question will lead us into the field of mechanics so that we may appreciate something of the nature of those structures and symmetries that underlie physical models and contribute to their long-term evolution. The second question will take us outside even the areas that have traditionally been investigated by mathematicians, since the special forms of force functions, presence of constraints, relationships among the variables, or efficiency considerations dictate to a large extent the features of appropriate (i.e. practical) methods used in applications.

It is important to emphasize that our treatment is not comprehensive; we have made a selection from the literature which comprises – in our view – the most important material from the standpoint of practical application.

Beginning with the idea of splitting we will show how many simple but effective integrators can be generated by using a few building blocks. The same techniques can be used to derive more sophisticated schemes. For example, explicit higherorder methods have a very natural derivation in the case of canonical mechanical systems developed in terms of the “kinetic $^ +$ potential” form of the energy.

We survey recent work on methods for constrained systems and consider various approaches to the simulation of rigid body systems, methods which offer an efficient and – in many cases – demonstrably superior geometric alternative to more widespread schemes. Variable stepsize geometric integrators will be introduced based on a rescaling of the time variable. Methods for mixed systems possessing both rapidly and slowly varying degrees of freedom – or weak and strong forces – also call for the construction of specialized schemes. In all cases, our aim will be to present the ideas in as general a form as is prudent, highlighting instances where a given technique might be of use in other applications. Molecular dynamics applications are an important source of challenging problems for geometric integration, so we devote some time to their particular characteristics. Conservative partial differential equations introduce many new issues for the development of geometric integrators, a topic we touch on in the final chapter of the book.

# How to use this book

This book is intended, first, as a text for a course in computational mechanics or as a tool for self-instruction, and, second, as a basic reference for researchers and educators – regardless of discipline – interested in using and developing geometric integrators. The book should serve as a bridge from traditional training in the sciences to the recent research literature in the field of geometric integration. By emphasizing mathematical and computational issues and illustrating the various concepts and techniques with carefully developed model problems, it is hoped that the book can appeal to a wide audience, including mathematicians unfamiliar with modeling issues, and physicists, chemists, and engineers wishing to gain a better understanding of the mathematical underpinnings of existing methods or in developing effective methods for new applications.

The book assumes only that the reader has had undergraduate coursework in linear algebra and differential equations. At several points we introduce, but do not thoroughly develop, topics from dynamical systems. A good introductory text in dynamical systems is the book of VERHULST [197]. We develop – in Chapters 2 and 3 – most of the necessary preliminaries of numerical analysis and classical mechanics from the ground up, however the reader should be aware that the treatment provided here of the required background material is necessarily brief; only those elements that are essential to our later study of geometric integrators are given. For an introduction to numerical analysis, the reader is referred to the classic books of ATKINSON [11], BURDEN AND FAIRES [37], and DAHLQUIST AND BJORK¨ [48]. The book of GEAR [70] can provide a useful introduction to the numerical solution of differential equations. The books of HAIRER, NøRSETT AND WANNER [82] and HAIRER AND WANNER [84] can serve as references for obtaining a more complete picture of the mathematical issues associated with construction of methods and error analysis for ordinary differential equations. ISERLES [91] has written an integrated text that introduces numerical methods for both ordinary and partial differential equations.

First published at the end of the 19th century, ROUTH’s Dynamics of a System of Rigid Bodies (Elementary Part)1 remains a marvelous introduction to classical mechanics and provides a wealth of examples and exercises for the student (many of which could now be revisited with the aid of the modern computational techniques developed in this book). For a more systematic treatment to Hamiltonian classical mechanics the reader is referred to the following texts: LANDAU AND LIFSHITZ [105], MARION [121], GOLDSTEIN [73], and ARNOLD [7], all of which are well-worn occupants of our bookshelves. These books are quite varied in their use of notation and even in the way in which they motivate and explain identical material, but we have found all of them to be helpful on various occasions. If only one book is to be consulted, the elegant book of LANCZOS [104] is remarkable both in terms of its readability and its breadth, owing partly to the absence of detailed proofs. A modern rigorous treatment of classical mechanics may be found in MARSDEN AND RATIU [124], a book which also contains a number of useful examples and notes on history and applications.

The book by SANZ-SERNA AND CALVO [172] was the first to cover symplectic integration methods and applications to classical mechanics and is still an excellent introduction to the subject. The more recent book by HAIRER, LUBICH, AND WANNER [80] covers a wide range of topics from geometric integration and should be very useful as an additional reference.

In a graduate course in applied mathematics or computational physics, it is probable that much of the material of Chapters 1–3 could be skipped or skimmed, depending on the backgrounds of the students and the interests of the teacher. Some caution should be exercised here. In particular, it is essential that the student understand the concepts of convergence and order of convergence for a numerical method, the definition of the flow map, first integrals, and at least the condition for a symplectic map in terms of the Jacobian of the flow map.

Molecular dynamics provides a rich source of problems for geometric integration, and we often draw on examples from this field for motivation and for evaluation of concepts and methods. Here again, it is likely that the reader may, on occasion, wish for a more detailed description of the problems or of typical approaches used by chemists and physicists. One reference stands out in this area for clarity of presentation and breadth: ALLEN AND TILDESLEY [4]. More recent books of FRANKEL AND SMIT [66] and SCHLICK [174] help to fill in the picture.

Exercises included at the end of each chapter are intended to be demanding but not overwhelming; some of the multi-part problems could be assigned as projects, especially those involving the use of computers.

# Computer software

This book primarily emphasizes the mathematical properties of algorithms for solving differential equations. In later chapters, we will often see the methods introduced and analyzed as abstract maps of phase space. This approach, while essential to understanding and generalizing the methods, has the tendency to obscure both the intuitive basis for the theory and the ultimate importance of the subject. We would like emphasize that the student must implement and test numerical methods in order to gain a full understanding of the subject.

While any programming language and graphics package could, in principle, be employed, the need for flexibility in the coding and testing of methods and the need to be able to work easily with scientific functions of vectors and matrices makes a specialized, interpreted language system for mathematics the best environment for problem solving.

At the time of this writing, there are several widely distributed commercial software packages that support the simplified design and testing of algorithms, including the commercial packages MATLAB, MAPLE, and MATHEMATICA. Of these, the authors prefer the user interface and programming structure of MATLAB, but this is largely a matter of taste and any of the three mentioned systems would be suitable. These packages are all available to students at heavily discounted prices and run on a variety of computer platforms.

For a student on a severe budget, there are several widely available free alternatives to the commercial packages. These options include, notably, OCTAVE, which is distributed under the Free Software Foundation’s GNU Public License. Our experience with this software is that it is adequate for most study purposes, although the commercial alternatives are generally superior with regard to easeof-use, documentation, and reliability.

We will occasionally describe algorithms in this text, but we will attempt to avoid system-specific details, so the student is expected to supplement the mathematical study with study of the the user’s guide for the software system they are using, in particular the appropriate sections on programming.

# Notation

Let us summarize some basic notation used throughout the book. Dependent variables, such as positions $\pmb q$ and velocities $\pmb { v }$ are elements of a Euclidean space $\mathbb { R } ^ { d }$ , where $d \geq 1$ is the appropriate dimension. More specifically, we will always identify dependent variables with column vectors. When two column vectors $\pmb { u } \in$ $\mathbb { R } ^ { k }$ , $\pmb { v } \in \mathbb { R } ^ { I }$ are given we may write $( \pmb { u } , \pmb { v } ) ^ { T }$ for the column vector in $\mathbb { R } ^ { k + I }$ obtained by concatenating the two vectors. The transpose is there to remind us that the result is again a column vector. We will often need to refer to a set indexed by a parameter for which we write $\{ a _ { t } \} _ { t \in P }$ , where $P$ is the index set. As a short-hand, we will write $\left\{ \boldsymbol { a } _ { t } \right\}$ if the index set is clear from the context.

The set of $k \times k$ matrices with real coefficients is $\mathbb { R } ^ { k \times k }$ and capital bold-face letter are used to denote matrices, e.g., A, $B \in \mathbb { R } ^ { k \times k }$ . The $k$ -dimensional identity is $\boldsymbol { I } _ { k }$ or $\prime$ as a short-hand if the dimension is clear from the context.

A vector-valued function $\pmb { { \cal F } } : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ will be assumed to map column vectors of dimension $n$ to column vectors of dimension $m$ . The vector of partial derivatives of a scalar-valued function $f ( \pmb q )$ is identified with a row vector in $\mathbb { R } ^ { d }$ and is denoted by $f _ { q } ( q )$ or, equivalently, by $\partial f / \partial \pmb q \left( \pmb q \right)$ . Hence the Jacobian matrix of a vector-valued function $\pmb { F } ( \pmb { q } )$ is identified with the $m \times n$ matrix $F _ { q } ( q )$ .

The scalar product, inner product, or dot product of two column vectors a and $^ { b }$ in $\mathbb { R } ^ { d }$ is denoted by $\left. a , b \right.$ or ${ \pmb { a } } { \cdot } { \pmb { b } }$ , or, simply, $\partial ^ { T } \boldsymbol { b }$ , where $\partial ^ { T }$ is the transpose of a. The cross product of a and $b$ is denoted $\pmb { \partial } \times \pmb { b }$ . We will frequently use

$$
{ \widehat { \pmb { a } } } { \pmb { b } } = { \pmb { a } } \times { \pmb { b } } ,
$$

where $\widehat { \pmb { a } } \in \mathbb { R } ^ { 3 \times 3 }$ is a skew-symmetric matrix related to the vector $\pmb { a } = \left( a _ { 1 } , a _ { 2 } \right.$ , $a _ { 3 } ) ^ { T }$ by

$$
\widehat { \pmb { a } } = \left[ \begin{array} { c c c } { 0 } & { - a _ { 3 } } & { a _ { 2 } } \\ { a _ { 3 } } & { 0 } & { - a _ { 1 } } \\ { - a _ { 2 } } & { a _ { 1 } } & { 0 } \end{array} \right] .
$$

The norm of a vector a is defined by

$$
\lVert \pmb { a } \rVert = \langle \pmb { a } , \pmb { a } \rangle ^ { 1 / 2 } .
$$

A real-valued function $f$ defined on an interval $I$ of the real line is said to be square-integrable if $\textstyle \int _ { I } f ( x ) ^ { 2 } d x$ is bounded. In that case we say that $f$ lies in the function space $L _ { 2 }$ on the interval $I$ . We say that the $L _ { 2 }$ -norm of $f$ is

$$
\| f \| _ { 2 } = \left( \int _ { I } f ( x ) ^ { 2 } d x \right) ^ { \frac { 1 } { 2 } } ,
$$

and we define the $L _ { 2 }$ -inner product of two square integrable functions $f$ and $g$ by

$$
( f , g ) = \int _ { I } f ( x ) g ( x ) d x
$$

The gradient $\nabla _ { q } V ( q )$ of a scalar-valued differentiable function $V ( q )$ is defined by

$$
\langle \nabla _ { \boldsymbol { q } } V ( \boldsymbol { q } ) , \boldsymbol { u } \rangle = \operatorname* { l i m } _ { \varepsilon \to 0 } \frac { V ( \boldsymbol { q } + \varepsilon \boldsymbol { u } ) - V ( \boldsymbol { q } ) } { \varepsilon } ,
$$

where the equality is to hold for all vectors $\pmb { u }$ of the same dimension as $\pmb q$ . This definition leads to the relation

$$
\nabla _ { \pmb { q } } V ( \pmb q ) = V _ { \pmb { q } } ( \pmb q ) ^ { T } ,
$$

and, hence, the gradient $\nabla _ { q } V ( q )$ is a column vector.

The time derivative of a function $\pmb q ( t )$ will normally be denoted by $d \pmb q / d t ( t )$ , but whenever it is more convenient we may instead use the short-hand $\dot { \pmb q } ( t )$ . If clear from the context, we will also frequently drop the argument in functions and write, for example, $\dot { \pmb q }$ instead of $\dot { \pmb q } ( t )$ , or $\boldsymbol { F }$ instead of $F ( q )$ . The same conventions apply to higher-order derivatives.

If a variable $u$ depends on several independent variables such as time $t$ and space $x$ , then the partial derivatives are often denoted by $u _ { t }$ and $u _ { x }$ , respectively.

Given two maps $\pmb { \psi } _ { 1 } : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ and $\pmb { \psi } _ { 2 } : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ with compatible range and domain, we define their composition $\psi _ { 2 } \circ \psi _ { 1 }$ by

$$
\left[ \pmb { \psi } _ { 2 } \circ \pmb { \psi } _ { 1 } \right] ( z ) = \pmb { \psi } _ { 2 } ( \pmb { \psi } _ { 1 } ( z ) ) ,
$$

for all $z \in \mathbb { R } ^ { n }$ . The inverse of a one-to-one map $\pmb { \psi }$ is denoted by $\psi ^ { - 1 }$ . Hence

$$
\pmb { \psi } ^ { - 1 } \circ \pmb { \psi } = \mathbf { i d } ,
$$

where $\mathbf { i d } ( z ) = z$ the identity map.

Finally the Landau-order notation $\mathcal { O } ( \Delta t )$ is used to denote a quantity that goes to zero as rapidly as $\Delta t$ goes to zero. More generally, we will write $g ( \Delta t ) =$ $\mathcal { O } ( \Delta t ^ { p } )$ if $g ( \Delta t ) / \Delta t ^ { p }$ is bounded as $\Delta t \to 0$ but $g ( \Delta t ) / \Delta t ^ { q }$ is unbounded if $q > p$ .

# Acknowledgements

We have to admit that when we began this project, we had no appreciation for its ultimate complexity. The only thing that has kept the project going at some critical points was the broad support and encouragement we received from our families, our colleagues, and our students.

A key aspect of the book is the emphasis on applications. Brian Laird proposed the Lennard–Jones model discussed in Chapter 4 and made several other helpful comments. Chris Sweet contributed most of the numerical experiments in Chapter 6, including the long-term simulations of the solar system, and Eric Barth provided the alanine dipeptide simulation in Chapter 11. Jason Frank helped with many of the experiments in Chapter 12. Jason’s tireless proofreading of the entire manuscript must also be remarked!

We hope that the book will be useful for teaching upper-division undergraduate and graduate courses. In 2002, Ph.D. students from various fields and various parts of Europe – Martin Dahlberg (chemistry), Thomas Sauvaget (mathematics/physics), Marko Vranicar (physics), and Fredrick Hedman (mathematics) – attended an informal summer school in Leicester taught from an early draft of the book. Part of the book formed the basis for a series of survey lectures given by one of us in Bari, Italy in 2002. Mitch Luskin, Claudia Wulff, and Steve Bond have subjected their classes to a preliminary draft of the book for testing in this setting, and provided useful comments.

We would like also to thank Teijo Arponen, Jeff Cash, Colin Cotter, Ernst Hairer, Zhidong Jia, Per-Christian Moan, Brian Moore, and Antonella Zanna for reading various parts of the manuscript and providing feedback. We have also relied on the extraordinary patience of Cambridge University Press, particularly our editors David Tranah and Joseph Bottrill.

# 1

# Introduction

This book is about numerical methods for use in simulating dynamical phenomena governed by conservative processes. In this chapter, we review a few basic principles regarding conservative models. In general, we are concerned here with initial value problems for systems of ordinary differential equations (ODEs) of the form

$$
\frac { d } { d t } z = { \bf { \nabla } } f ( z ) , \qquad z ( t _ { 0 } ) = z ^ { 0 } ,
$$

where $z : \mathbb { R } \to \mathbb { R } ^ { k }$ . The basic questions encountered early on in a first course on ODEs concern existence and uniqueness of solutions, a topic addressed, for example, by Picard’s theorem. Discussion then turns to various techniques for analytically solving the differential equations when $\boldsymbol { f }$ has a prescribed form. In particular, the scalar case $k = 1$ is an instance of a separable differential equation and such models are in principle solvable in quadratures (i.e. by evaluating certain integrals and solving certain algebraic equations). Linear systems are exactly solvable after determination of the eigenvalues and eigenvectors (or generalized eigenvectors, in the degenerate case). Beyond these and a few other special cases, most models are not exactly integrable. In this book we are mostly interested in complex models that do not admit exact solutions.

The emphasis of this book is on the particular models which are formulated naturally as conservative systems of ODEs, most importantly Hamiltonian systems. As a general rule, mechanical systems resulting from physical principles are Hamiltonian until (usually for prudent modeling purposes) subjected to simplifying reductions or truncations. For example, in typical fluid dynamics applications, the incorporation of diffusive effects due to friction with a boundary plays an essential role in the modeling. However, in many situations, the conservative paradigm can be retained and remains the most appropriate foundation for the construction of models, since it is in no small measure due to properties such as conservation of energy and angular momentum that matter behaves as it does.

The existence of Kepler’s laws which approximately describe the motion of the planets in the solar system are reflections of the conservative nature of gravitational dynamics. The celebrated Kolmogorov–Arnold–Moser theory which discusses the local stability of nonlinear dynamical systems in the vicinity of certain critical points applies only to conservative systems. Even dissipative systems typically retain certain conservation laws (for example conservation of mass in fluid dynamics), and many of the ideas developed in this book are still applicable to such problems.

# 1.1 $N \cdot$ -body problems

Conservative dynamical systems most often originate through application of Newton’s second law which describes the motion of a body in an applied force field. In a classical N-body system (Fig. 1.1), several point masses are involved and the forces acting on any one body arise from the presence of neighboring bodies or some external field.

![](images/42d0c7fb477eec76e41e02819edf59d287aeaadba795d437b4ef6904e0120982.jpg)  
Figure 1.1 An N-body system.

Let the ith body be assigned a mass $m _ { j }$ , an instantaneous position $\pmb q _ { j }$ (with respect to some appropriate reference frame), and a velocity $\pmb { V } _ { I }$ , $i = 1 , \dots , N$ . Let $F _ { j }$ represent the force acting on body $j$ (due, for example, to interactions with the other particles). We assume that the force can be obtained as the negative gradient of a potential energy function $V$ with respect to the i th particle position $\pmb q _ { I }$ , i.e.

$$
\pmb { F } _ { i } = - \nabla _ { \pmb { q } _ { i } } V \big ( \pmb { q } _ { 1 } , \pmb { q } _ { 2 } , \dots , \pmb { q } _ { N } \big ) .
$$

The $N .$ -point particles then move according to Newton’s equations of motion

$$
\begin{array} { c } { { \displaystyle \frac { d } { d t } { \pmb q } _ { i } = { \pmb v } _ { i } , } } \\ { { m _ { i } \displaystyle \frac { d } { d t } { \pmb v } _ { i } = { \pmb F } _ { i } , \qquad i = 1 , 2 , \ldots , N . } } \end{array}
$$

N-body problems can be naturally formulated to describe motion in any Euclidean space $\mathbb { R } ^ { \nu }$ , $\nu > 0$ , i.e. with $\pmb q _ { j }$ , $v _ { j }$ , and $F _ { j }$ all in $\mathbb { R } ^ { \nu }$ . Such a system is said to have νN degrees of freedom. We will say that the phase space of an $N .$ -body problem is the $2 \nu N \cdot$ -dimensional set consisting of all possible positions $\pmb q = ( \pmb q _ { 1 } , \pmb q _ { 2 } , \dotsb q _ { N } ) ^ { T }$ and velocities $\pmb { v } = ( \pmb { v } _ { 1 } , \pmb { v } _ { 2 } , \dots , \pmb { v } _ { N } ) ^ { T }$ of the particles. Under mild smoothness assumptions on the potential energy function $V$ , there exists, at least locally through any point $( \pmb q ^ { 0 } , \pmb v ^ { 0 } )$ of phase space, a unique trajectory of the mechanical system: a solution of the equations (1.1)–(1.2) subject to the initial conditions $\pmb q ( 0 ) = \pmb q ^ { 0 }$ , $\pmb { v } ( 0 ) = \pmb { v } ^ { 0 }$ . At a critical point $q = \bar { q }$ , all of the forces acting on the particles in the system vanish; hence the trajectory through $( \bar { \pmb q } , \pmb 0 )$ reduces to a single point.

The total energy associated to the mechanical system (1.1)–(1.2) is the sum of kinetic and potential terms

$$
E ( \pmb { q } , \pmb { v } ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } m _ { i } \| \pmb { v } _ { i } \| ^ { 2 } + V ( \pmb { q } ) .
$$

It is easy to see that the energy is constant along a trajectory, since

$$
\begin{array} { r l } { \displaystyle \frac { d } { d t } E = \sum _ { i = 1 } ^ { N } m _ { i } \pmb { v } _ { i } \cdot \dot { \pmb { v } } _ { i } + \sum _ { i = 1 } ^ { N } \nabla _ { q _ { i } } V ( \pmb { q } ) \cdot \dot { \pmb { q } } _ { i } } & { } \\ { \displaystyle = \sum _ { i = 1 } ^ { N } m _ { i } \pmb { v } _ { i } \cdot \left( \frac { 1 } { m _ { i } } \pmb { F } _ { i } \right) - \sum _ { i = 1 } ^ { N } \pmb { F } _ { i } \cdot \pmb { v } _ { i } = 0 . } \end{array}
$$

(Refer to the preface for details on the notation used in this derivation and later in the book.) A system with an energy function constant along solutions is referred to as a conservative system.

# 1.2 Problems and applications

Let us briefly survey a few of the most important recurring N-body applications. Examples of these problems, along with a number of other types of models, are developed in more detail in various places in the book.

The historical origin of the N-body problem lies in gravitational modeling, and these problems remain of substantial current interest. Simulations are being conducted on a wide variety of astronomical systems, including planetary systems (for understanding both their formation and their long-term stability), systems of interacting stars or binaries, galaxies, and globular clusters. Closely related problems arise in semi-classical studies of atomic systems. As an example, the three-body gravitational problem involving bodies of unequal mass has the potential energy

$$
V ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) = - \frac { G m _ { 1 } m _ { 2 } } { \| q _ { 1 } - q _ { 2 } \| } - \frac { G m _ { 2 } m _ { 3 } } { \| q _ { 2 } - q _ { 3 } \| } - \frac { G m _ { 1 } m _ { 3 } } { \| q _ { 1 } - q _ { 3 } \| } ,
$$

where $G$ is the universal gravitational constant. Such a three-body problem has no general, analytical solution, so simulation is needed to enhance understanding, sometimes in conjunction with partial theoretical analysis, for example to determine the stability of certain configurations of the bodies. Chaotic solutions of the three-body problem may include arbitrarily close approaches of the bodies, in which case the singularity in the potential may cause significant difficulty for numerical simulation and some sort of regularizing transformations of time and/or coordinates are needed. We will return to consider some of these issues in one of the book’s later chapters.

Classical mechanics is also the basis of many molecular models in chemistry, physics, and biology, including those commonly used for studying liquids and gases, materials, proteins, nucleic acids, and other polymers. In these applications, $V$ is composed of a sum of several heterogeneous nonlinear contributions based on the distances between pairs of particles, varying both in functional form and in relative intensity. These terms may be “local” (“short-range”) meaning that they effectively involve only contributions from nearby particles, or they may be “longrange.” A commonly treated system with only local interactions is the simplified model of a gas or liquid, consisting of $N$ identical atoms of a certain prescribed mass, interacting in a Lennard–Jones pair potential

$$
\varphi _ { \mathsf { L . J . } } ( r ) = \epsilon \left[ \left( { \frac { \bar { r } } { r } } \right) ^ { 1 2 } - 2 \left( { \frac { \bar { r } } { r } } \right) ^ { 6 } \right] .
$$

The total potential energy is

$$
V = \sum _ { 1 \leq i < j \leq N } \varphi _ { \mathsf { L } . \mathsf { J } . } ( \| \pmb { q } _ { i } - \pmb { q } _ { j } \| ) .
$$

Note that such models are always simplifications of vastly more complex quantummechanical models. The parameters $\epsilon$ and $\bar { r }$ of the Lennard–Jones potential provide a fit to experiment, but would depend on the temperature and pressure at which the simulation is performed. Strictly speaking, the pair interactions between atoms would include all pairs, no matter how distant, but since the energy decays like $r ^ { - 6 }$ , the forces are generally found to be so small outside of some critical radius that the potential can simply be cut off beyond this distance. In practice, this is usually done by introducing a smooth transition of the potential energy function to a constant value.

Regardless of what other potentials may be present, the presence of the Lennard–Jones potential ensures that the particle forces are ultimately strongly repulsive at short range. These repulsive forces are a very important aspect of molecular systems. The potential will be singular where particle positions overlap, but otherwise, the potential is smooth and the solution is globally defined: solutions started away from singularities can be extended without bound in $t$ . Thus molecular systems do not undergo the extreme collisions encountered in strictly Coulombic problems such as gravitation.

Still other classes of conservative systems arise through discretization of partial differential equations. A semi-linear wave equation of the form

$$
u _ { t t } = u _ { x x } - f ( u ) , \qquad u = u ( x , t ) ,
$$

is conservative under certain prescriptions of boundary and initial data. If we assume, for example, that solutions are defined on the interval $[ 0 , L ]$ and are periodic with period $L$ , then the energy functional is

$$
E [ u ] = \int _ { 0 } ^ { L } \left[ \frac { 1 } { 2 } u _ { t } ^ { 2 } + \frac { 1 } { 2 } u _ { x } ^ { 2 } + F ( u ) \right] d x ,
$$

where $\begin{array} { r } { F ( u ) \ = \ \int _ { 0 } ^ { u } f ( s ) d s } \end{array}$ . The equations of motion could be written in the “Newton-like” form

$$
v _ { t } = - \delta _ { u } V [ u ] , \qquad u _ { t } = v ,
$$

where $\begin{array} { r } { V [ u ] = \int _ { 0 } ^ { L } \left[ \frac { 1 } { 2 } u _ { x } ^ { 2 } + F ( u ) \right] d x } \end{array}$ represents the potential energy, and $\delta _ { u }$ , termed the variational derivative, is the analogue of the gradient appearing in the Newtonian equations of motion,

$$
( \delta _ { u } G [ u ] , \delta u ) = \operatorname* { l i m } _ { \varepsilon \to 0 } \frac { G [ u + \varepsilon \delta u ] - G [ u ] } { \varepsilon } ,
$$

where $G$ is a functional, like the potential energy $V$ , that assigns a real number to functions $u ( x )$ and the equality holds for all sufficiently regular periodic functions $\delta \boldsymbol { u } ( \boldsymbol { x } )$ , i.e. $\delta u ( x ) = \delta u ( x + L )$ . This definition is formally equivalent to the defining relation for the gradient mentioned in the preface with $\langle . , . \rangle$ replaced by the $L _ { 2 }$ inner product,

$$
( u , v ) = \int _ { 0 } ^ { L } u ( x ) v ( x ) d x .
$$

Note that $\delta _ { u } G [ u ]$ is itself a function of $x$ .

The simplest centered finite difference spatial discretization takes the form, for $i = 1 , 2 , \dots , N$ ,

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } u _ { i } = v _ { i } , } \\ { \displaystyle \frac { d } { d t } v _ { i } = \frac { u _ { i - 1 } - 2 u _ { i } + u _ { i + 1 } } { \Delta x ^ { 2 } } - f ( u _ { i } ) , } \end{array}
$$

where $u _ { i } \approx u ( i \Delta x , t ) , \Delta x = L / N$ , and the periodic boundary condition leads to the definitions $u _ { 0 } \equiv u _ { N }$ , $u _ { N + 1 } \equiv u _ { 1 }$ . This is in the form of a standard $N -$ body system in one dimension with positions $\pmb { \imath } = ( u _ { 1 } , u _ { 2 } , \ldots , u _ { N } ) ^ { T }$ , velocities $\pmb { v } = ( v _ { 1 } , v _ { 2 } , \ldots , v _ { N } ) ^ { T }$ , and potential

$$
V ( \pmb { u } ) = \sum _ { i = 1 } ^ { N } \left( \frac { u _ { i + 1 } - u _ { i } } { \Delta x } \right) ^ { 2 } + \sum _ { i = 1 } ^ { N } F ( u _ { i } ) .
$$

# 1.3 Constrained dynamics

In the setting of modern applications, we will need to consider generalizations of the traditional N-body problem in which the basic modeling unit is not the point particle moving in Euclidean space but an object moving in some constrained space.

For instance, in molecular dynamics, the bond stretch between two atoms is typically modeled by a spring with rest length $L > 0$ , say

$$
V _ { 1 2 } ( \pmb { q } _ { 1 } , \pmb { q } _ { 2 } ) = \frac { \alpha } { 2 } ( \lVert \pmb { q } _ { 1 } - \pmb { q } _ { 2 } \rVert - L ) ^ { 2 } ,
$$

where $\pmb q _ { 1 }$ and $\pmb q _ { 2 }$ are the positions of the atoms and $\alpha$ is a positive parameter. When $\alpha$ is large, the vibrational frequency is also large, while the variation in the length of the stretch from $L$ will typically be small. It is then common practice to replace one or more of these bonds by rigid length constraints, i.e. to introduce a constraint of the form

$$
\| \pmb { q } _ { 1 } - \pmb { q } _ { 2 } \| ^ { 2 } = L ^ { 2 } .
$$

If enough constraints among a set of particles are imposed simultaneously, the group becomes completely rigid. Such rigid bodies have very interesting dynamical properties in and of themselves. For example, in molecular dynamics, it is standard practice to replace small polyatomic molecules (for example, ${ \sf H } _ { 2 } \mathrm { O }$ ) by rigid bodies. As another illustration, while it may be appropriate to treat the bodies in the solar system as point masses for many purposes, in more delicate situations, the nonspherical rigid body structure of the planets may need to be taken into consideration.

Let us begin by extending Newton’s equations for particle motion to the constrained case. Imagine a particle of mass $m$ moving on a constraint surface defined as the zero set of some smooth function $g$ . At any time, the particle is acted on by two types of forces: applied forces defined in the usual way by a potential energy function $V$ , and constraint forces which act in such a way as to make the particle lie on the constraint surface. Although we do not in general know anything about the directionality of the applied force, we may take as our starting point the principle of D’Alembert: the constraint force acts along the normal direction to the constraint surface, i.e. along the direction of the gradient to the function $g$ at the point of contact (Fig. 1.2).

![](images/1368284cf47cbfa1e3ba071f328e2c66e8b0fb9229b0ad83b4d170152d337d39.jpg)  
Figure 1.2 D’Alembert’s Principle: the constraint force acts in the normal direction to the constraint surface at the point of contact.

Thus, if we denote the constraint forces by $F _ { g }$ , we have

$$
\begin{array} { r l } { F _ { g } } & { { } | \mathbf { \omega } | \quad \nabla _ { q } g ( q ) , } \end{array}
$$

or

$$
\pmb { F } _ { g } = \lambda \nabla _ { \pmb { q } } g ( \pmb { q } ) ,
$$

where $\lambda$ is a scalar.

Using Newton’s second law, the equations of motion then take the form

$$
\begin{array} { c } { { m \dot { \pmb v } = - \nabla _ { \pmb q } V ( \pmb q ) + \lambda \nabla _ { \pmb q } g ( \pmb q ) , } } \\ { { \dot { \pmb q } = \pmb v , } } \\ { { g ( \pmb q ) = 0 . } } \end{array}
$$

The parameter $\lambda$ is an unknown which is uniquely determined by the condition that $\pmb q ( t )$ satisfy (1.8) at all points on the trajectory and that the trajectory be smooth. Specifically, if we differentiate the equation $g ( \pmb q ( t ) ) = 0$ twice with respect to time, we find first

$$
\frac { d } { d t } g ( \pmb { q } ) = \nabla _ { \pmb { q } } g ( \pmb { q } ) \cdot \dot { \pmb { q } } = \nabla _ { \pmb { q } } g ( \pmb { q } ) \cdot \pmb { v } = 0 ,
$$

and, then

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } g ( \pmb { q } ) = \langle \pmb { v } , g _ { \pmb { q } \pmb { q } } ( \pmb { q } ) \pmb { v } \rangle + m ^ { - 1 } \nabla _ { \pmb { q } } g ( \pmb { q } ) \cdot [ - \nabla _ { \pmb { q } } V ( \pmb { q } ) + \lambda \nabla _ { \pmb { q } } g ( \pmb { q } ) ] = 0 ,
$$

where $g _ { q q } ( \pmb q )$ represents the Hessian matrix of $g$ . Provided that $\nabla _ { q } g ( \pmb q ) \neq 0$ , the equation (1.10) has a unique solution $\lambda = \Lambda ( \boldsymbol { q } , \boldsymbol { v } )$

$$
\Lambda ( \boldsymbol { q } , \boldsymbol { v } ) = \frac { m } { \| \nabla _ { \boldsymbol { q } } g ( \boldsymbol { q } ) \| ^ { 2 } } \left( \frac { 1 } { m } \langle \nabla _ { \boldsymbol { q } } g ( \boldsymbol { q } ) , \nabla _ { \boldsymbol { q } } V ( \boldsymbol { q } ) \rangle - \langle \boldsymbol { v } , g _ { \boldsymbol { q } \boldsymbol { q } } ( \boldsymbol { q } ) \boldsymbol { v } \rangle \right) .
$$

Equations (1.6)–(1.8) are a special case of the constrained Euler–Lagrange equations. As a simple illustration, we mention the example of a bead (of mass $m$ ) moving in gravity in two dimensions (coordinates $( x , z ) )$ ) along a wire described by the curve $\boldsymbol { \mathsf { I } } : \boldsymbol { \mathsf { Z } } = \boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ . The constraint is $g ( x , z ) : = z - f ( x )$ , and the equations of motion take the form

$$
\begin{array} { c } { { m \ddot { x } = - \lambda f ^ { \prime } ( x ) , } } \\ { { m \ddot { z } = - m g + \lambda , } } \\ { { z = f ( x ) . } } \end{array}
$$

Here $g$ represents the earth’s gravitational constant.

As a second illustration, consider the spherical pendulum consisting of a bob of mass $m$ suspended from a fixed point on a rigid massless rod of length $L > 0$ . We formulate the problem in cartesian coordinates $( x , y , z )$ with energy

$$
E = \frac { 1 } { 2 m } ( \dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 } ) + m g z ,
$$

and equations of motion

$$
\begin{array} { r } { m \ddot { x } = 2 \lambda x , \qquad } \\ { m \ddot { y } = 2 \lambda y , \qquad } \\ { m \ddot { z } = - m g + 2 \lambda z , \qquad } \\ { 0 = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } - L ^ { 2 } . } \end{array}
$$

# 1.4 Exercises

1. Scalar nonlinear models. Consider a single-degree-of-freedom problem of the form

$$
\begin{array} { c } { { \dot { q } = v , } } \\ { { m \dot { v } = - \varphi ^ { \prime } ( q ) . } } \end{array}
$$

a. Write the energy function $E ( q , v )$ for the above system and verify that it is conserved along trajectories of the system.

b. Set the energy function to a constant value, say $E _ { 0 }$ , and show that the resulting equation can be solved for $V$ as a function of $q$ , subject to a choice of the sign of $V$ . Using this, together with the differential equations, show that the equations of motion reduce to a first-order differential equation for $q$ of the form

$$
\dot { q } = \pm \sqrt { \left( \frac { 2 } { m } \right) \left( E _ { 0 } - \varphi ( q ) \right) } .
$$

(Observe that this equation is separable, and hence the solution can in principle be recovered by integration.)

Discuss first the case $v \neq 0$ and continue with an investigation of the solution behavior in the vicinity of $v = 0$ .

2. Morse oscillator. (See problem 1 above.) The Morse oscillator is a onedegree-of-freedom conservative system consisting of a single particle of unit mass moving in the potential $\varphi ( q ) = D ( 1 - e ^ { - \beta q } ) ^ { 2 }$ . In the following set $D = 1$ and $\beta = 1$ .

a. Sketch the graph of $\varphi$ as a function of $q$ .   
b. Sketch several of the level curves $( E ( q , v ) = E _ { 0 }$ , $E _ { 0 }$ fixed) of the energy function. In particular, observe that the system has bounded trajectories for $E < E _ { * }$ . What is $\boldsymbol { E } _ { * }$ ? What can be said about an orbit with energy $E = E _ { * }$ ?   
c. Sketch the graphs of several solution curves as functions of $t$ . [Hint: the velocity field can be sketched by using the result of problem 1b.]

3. Pendulum. The planar version of the pendulum is described by the equations

$$
\begin{array} { c } { { m \ddot { x } = 2 \lambda x , } } \\ { { m \ddot { y } = - m g + 2 \lambda y , } } \\ { { 0 = x ^ { 2 } + y ^ { 2 } - L ^ { 2 } . } } \end{array}
$$

Introduce coordinates $x = L \sin \theta$ , $y = - L \cos \theta$ and show that the equations of motion can be reduced to a single second-order differential equation for $\theta$ which is in the form of a nonlinear oscillator.

4. Bead-on-wire. Consider the “bead-on-wire” problem (1.11)–(1.13). Show that the equations of motion can be reduced to a second-order unconstrained differential equation for $x$ of the form

$$
\ddot { x } = - f ^ { \prime } ( x ) \frac { g + f ^ { \prime \prime } ( x ) \dot { x } ^ { 2 } } { 1 + f ^ { \prime } ( x ) ^ { 2 } } .
$$

5. Variational derivative. Using the definition (1.5) of the variational derivative and integration by parts, verify that

$$
\delta _ { u } V [ u ] = - u _ { x x } + F ^ { \prime } ( u ) ,
$$

for

$$
V [ u ] = \int _ { 0 } ^ { L } \left[ \frac { 1 } { 2 } u _ { x } ^ { 2 } + F ( u ) \right] d x .
$$

# 2

# Numerical methods

In this chapter, we introduce the concepts of accuracy and stability for a numerical method approximating the solution of an ordinary differential equation initial value problem

$$
{ \frac { d } { d t } } z = { \pmb { f } } ( z ) , \qquad z ( t _ { 0 } ) = z ^ { 0 } \in \mathbb { R } ^ { k } .
$$

Here $z ( t )$ represents the solution at a particular time $t$ ; $z = z ( t )$ thus defines a parameterized trajectory. We assume that trajectories are defined for all initial values $z ^ { 0 } \in \mathbb { R } ^ { n }$ and for all times $t \geq t _ { 0 }$ . For simplicity, we typically take $t _ { 0 } = 0$ . One also often uses the notation $\boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ to distinguish the trajectory to a given initial value $z ^ { 0 }$ .

It is an important feature of the initial value problems we consider, that the solution value at any given point on the trajectory determines the solution at all later points on the trajectory, through integration of an appropriate initial value problem. In effect, the solutions $\boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ of the differential equation define a mapping, or rather a one-parametric family of mappings, $\{ \pmb { \phi } _ { t } \} _ { t \geq 0 }$ , which take initial data to later points along trajectories, i.e.

$$
\pmb { \phi } _ { t } \mathopen { } \mathclose \bgroup \left( z ^ { 0 } \aftergroup \egroup \right) = z \mathopen { } \mathclose \bgroup \left( t ; z ^ { 0 } \aftergroup \egroup \right) , \qquad z ^ { 0 } \in \mathbb { R } ^ { k } .
$$

We term the map $\pmb { \phi } _ { t } : \mathbb { R } ^ { k } \  \ \mathbb { R } ^ { k }$ the flow map of the given system (see Fig. 2.1).

![](images/d229038d44b23811af2403cb573806b8cad77138e77455873c7bb42da277421e.jpg)  
Figure 2.1 The flow map. The existence of a trajectory through each point of phase space (left) implies the existence of a flow map $\pmb { \phi } _ { t }$ taking points of phase space to their evolution through $t$ units of time (right).

In general, the flow map has the following property: if we solve the differential equations from a given initial point $z ^ { 0 }$ up to a time $t _ { 1 }$ , then solve from the resulting point forward $t _ { 2 }$ units of time, the effect is the same as solving the equations with initial value $z ^ { 0 }$ up to time $t _ { 1 } + t _ { 2 }$ . In terms of the mapping, $\pmb { \phi } _ { t _ { 1 } } \circ \pmb { \phi } _ { t _ { 2 } } = \pmb { \phi } _ { t _ { 1 } + t _ { 2 } }$ . Such a family of mappings is sometimes referred to as a one-parametric semigroup. 1

Given a differential equation and an initial value, a discrete version of a trajectory of the system could be obtained by taking snapshots of the solution at equally spaced points in time $t _ { 0 }$ , $t _ { 1 } = t _ { 0 } + \Delta t$ , $t _ { 2 } = t _ { 1 } + \Delta t , . . . .$ . The idea of most numerical methods for solving the initial value problem is to provide a simple rule for computing approximations to a discrete trajectory. Assume that this is done by a sequential iterative procedure: starting at $t _ { 0 }$ , and given the initial value $z ( t _ { 0 } ) = z ^ { 0 }$ , we compute, via some equation or system of equations, an approximation $z ^ { 1 }$ to $\boldsymbol { z } ( t _ { 1 } )$ , then, by the same means, $z ^ { 2 } \approx z ( t _ { 2 } )$ , etc. In this way, as much of the solution as desired can be obtained. This computational paradigm was understood by Euler, and was used – long before the advent of computers – as a means of studying the theoretical properties of differential equations. The framework was refined and applied to track the motion of charged particles and planets in the first decades of this century, and molded into a practical, effective tool in various fields of science and engineering during the computer revolution of the 1950s and 1960s.

Even the simplest general timestepping methods can, in principle, be used for a wide variety of dynamics simulations, but shortcomings soon become evident in simulations of large, nonlinear dynamical systems. Standard error analysis can be used to demonstrate that a certain numerical method converges in the limit of a small timestep, but in any simulation the ability to take small timesteps is in direct conflict with the cost of a timestep and the need to perform integrations on time intervals long enough to elicit relevant macroscopic behavior. Moreover, even the seemingly elementary supposition that accuracy should be the foundation for analyzing methods is in question in many modern simulations, since, as we have noted in the introduction, accuracy of a particular trajectory may not be directly relevant to simulations of chaotic systems on long time intervals.

In this chapter, we will discuss some elementary properties of timestepping schemes for ordinary differential equations, including the notions of accuracy and stability, and we discuss the application of various schemes to some simple classes of differential equations, notably linear conservative models.

# 2.1 One-step methods

Given a discrete trajectory up to time $t _ { n }$ , there are, in general, few restrictions on the way in which the next approximation $z ^ { n + 1 }$ is computed. For example, it might be based on a formula involving the previous computed points along the discrete trajectory, on the derivative of the solution at previous points, or on the values of higher derivatives of the solution at the previous timestep. A common choice is to base the next approximation only on the $I$ previously computed points $z ^ { n - I + 1 }$ , $z ^ { n - I + 2 } , \dots , z ^ { n }$ and the corresponding values of the derivative at those points, $\dot { z } ^ { n - I + 1 } , \dot { z } ^ { n - I + 2 } , \dots , \dot { z } ^ { n }$ (where $\dot { z } ^ { i } \equiv f ( z ^ { i } ) )$ . A linear multistep method is defined by a linear recurrence relation involving these data together with the associated values at the subsequent time point, $z ^ { n + 1 }$ and $\dot { z } ^ { n + 1 }$ .

We will be primarily concerned with the case $I = 1$ , generalized one-step methods. By iterating the flow map, we know that we obtain a series of snapshots of the true trajectory

$$
z ^ { 0 } , \pmb { \phi } _ { \Delta t } ( z ^ { 0 } ) , \pmb { \phi } _ { \Delta t } \circ \pmb { \phi } _ { \Delta t } ( z ^ { 0 } ) , . . .
$$

or, compactly, $\{ \pmb { \phi } _ { \Delta t } ^ { n } ( z ^ { 0 } ) \} _ { n = 0 } ^ { \infty }$ , where the composition power $\pmb { \phi } _ { \Delta t } ^ { n }$ is the identity if $n = 0$ and is otherwise the $n$ -fold composition of $\pmb { \phi } _ { \Delta t }$ with itself. For a one-step method, the approximating trajectory can be viewed as the iteration of another mapping $\pmb { \psi } _ { \Delta t } : \mathbb { R } ^ { k }  \mathbb { R } ^ { k }$ of the underlying space, so that

$$
z ^ { n } = \pmb { \psi } _ { \Delta t } ^ { n } ( z ^ { 0 } ) .
$$

The mapping $\psi _ { \Delta t }$ is generally nonlinear, will depend on the function $\boldsymbol { f }$ and/or its derivatives, and may be quite complicated – perhaps even defined implicitly as the solution of some nonlinear algebraic system. Because one-step methods generate a mapping of the phase space, they can be studied with the same techniques and concepts that one employs for understanding the flow map itself. To benefit from this natural correspondence, we will primarily focus on one-step methods throughout this book.

# 2.1.1 Derivation of one-step methods

One-step methods can be derived in various ways. One way is to first integrate both sides of (2.1) on a small interval $\left[ { t , t + \Delta t } \right]$ , obtaining

$$
z ( t + \Delta t ) - z ( t ) = \int _ { 0 } ^ { \Delta t } f ( z ( t + \tau ) ) d \tau .
$$

The right-hand side can then be replaced by a suitable quadrature formula resulting in an approximation of the form

$$
z ( t + \Delta t ) \approx z ( t ) + \sum _ { i = 1 } ^ { s } b _ { i } { \pmb f } ( z ( t + \tau _ { i } ) ) ,
$$

for an appropriate set of weights $\{ b _ { i } \}$ and quadrature points $\{ \tau _ { i } \}$ . In Euler’s method, the quadrature rule used is just

$$
\int _ { 0 } ^ { \Delta t } { \pmb { f } } ( { \pmb { z } } ( t + \tau ) ) d \tau = \Delta t { \pmb { f } } ( { \pmb { z } } ( t ) ) + { \mathcal { O } } ( \Delta t ^ { 2 } ) .
$$

The implicit Euler method, on the other hand, is obtained by replacing the value of $\pmb { f }$ at the left endpoint of the interval with its value at the right endpoint. The term implicit here refers to the fact that a nonlinear system of equations must be solved to advance the step. The trapezoidal rule is based on

$$
\int _ { 0 } ^ { \Delta t } { \pmb { f } } ( { \pmb { z } } ( t + \tau ) ) d \tau = \frac { 1 } { 2 } \Delta t \left[ { \pmb { f } } ( { \pmb { z } } ( t ) ) + { \pmb f } ( { \pmb { z } } ( t + \Delta t ) ) \right] + { \cal O } ( \Delta t ^ { 3 } ) ,
$$

and the implicit midpoint method is defined by

$$
\int _ { 0 } ^ { \Delta t } { \pmb { f } } ( { \pmb { z } } ( t + \tau ) ) d \tau = \Delta t { \pmb { f } } \left( \frac { { \pmb { z } } ( t ) + { \pmb { z } } ( t + \Delta t ) } { 2 } \right) + { \cal O } ( \Delta t ^ { 3 } ) .
$$

In each case, the associated one-step methods are obtained by using the truncated approximation formula to relate subsequent points $z ^ { n }$ and $z ^ { n + 1 }$ along a discrete trajectory.

$$
z ^ { n + 1 } = z ^ { n } + \Delta t \pmb { f } ( z ^ { n } ) \qquad z ^ { n + 1 } = z ^ { n } + \Delta t \pmb { f } ( z ^ { n + 1 } )
$$

$$
\begin{array} { r l } { z ^ { n + 1 } = z ^ { n } + \frac { \Delta t } { 2 } \left[ \pmb { f } ( z ^ { n } ) + \pmb { f } ( z ^ { n + 1 } ) \right] } & { { } z ^ { n + 1 } = z ^ { n } + \Delta t \pmb { f } \left( \frac { z ^ { n } + z ^ { n + 1 } } { 2 } \right) } \end{array}
$$

This can of course be generalized to design more accurate approximations, as we shall shortly see.

Let us show in detail how we would apply such methods to treat a secondorder system of differential equations

$$
\ddot { \pmb q } = \pmb q ( \pmb q ) ,
$$

such as arises from Newton’s second law. We begin by writing the differential equations in a first-order form

$$
\begin{array} { l } { \dot { \pmb q } = \pmb v , } \\ { \dot { \pmb v } = \pmb g ( \pmb q ) . } \end{array}
$$

Next, we identify the pair of dependent variables (or vectors of dependent variables) with a new vector $z$ , and define a vector field $\pmb { f } ( z )$ by pairing the right-hand sides of each equation

$$
z = { \Bigg [ } { \pmb q } { \Bigg ] } , \qquad { \pmb f } ( z ) = { \pmb f } ( { \pmb q } ^ { } ) ) = { \Bigg [ } { \pmb v } ^ { }  \\ { { \pmb v } ^ { } { \Bigg ] } , \qquad { \pmb f } ( { \pmb z } ) = { \pmb f } ( { \pmb z } ^ { } ) \Bigg ] . }
$$

We can then apply any of the numerical methods given to the equation ${ \dot { z } } = f ( z )$ . Thus Euler’s method for the second-order system becomes

$$
\begin{array} { l } { { { \pmb q } ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb v } ^ { n } , } } \\ { { { \pmb v } ^ { n + 1 } = { \pmb v } ^ { n } + \Delta t { \pmb g } ( { \pmb q } ^ { n } ) . } } \end{array}
$$

# 2.1.2 Error analysis

Error analysis for a one-step method such as those discussed above centers on two issues: (i) the accuracy of the one-step approximation, as determined by comparison of the Taylor series expansions of true solutions and the numerical approximation in a timestep, and (ii) the accumulation of the error during computation of a discrete trajectory. The errors due to round-off in the computations (to which all floating point calculations are subject) are typically assumed to be much smaller than the errors due to the introduction of the approximation scheme, and are simply ignored.

We will use the term local error for the difference between the exact and approximate solutions on a single timestep of size $\Delta t$ , say starting from a point $\bar { z }$ along some particular trajectory. Let us denote the local error at this point by ${ \bf \delta l e } ( \Delta t ; \bar { z } )$ (see Fig. 2.2). Using Taylor series, we can obtain an expansion in powers of $\Delta t$ of the form

$$
\begin{array} { r } { \mathbf { { l e } } ( \Delta t ; \bar { z } ) = \mathbf { C } _ { p + 1 } ( \bar { z } ) \Delta t ^ { p + 1 } + \mathbf { C } _ { p + 2 } ( \bar { z } ) \Delta t ^ { p + 2 } + \dots . } \end{array}
$$

The integer $p$ is termed the order of the method. Below we give the leading terms of the local error for the elementary one-step methods introduced earlier. We use the notation $z ^ { ( k ) }$ to denote the $k$ th derivative of $z ( t )$ at $z ( t ) = \bar { z }$ .

![](images/2a75bac91de018c15742b7fb86e78ea45a59b75746d8e050f2896fc1aa86992e.jpg)  
Figure 2.2 Local errors in numerical integration.

![](images/6616e37d84d51602c22571b421d49ec93d84ab092efc9bb73eeb48a47a9b47d7.jpg)

To make sense of these formulas, observe that any derivative of a trajectory $z ( t )$ at the point where $z ( t ) = \bar { z }$ could be rewritten as a function just of $\bar { z }$ itself by using the differential equations. For example

$$
\dot { z } ( t ) = \pmb { f } ( \bar { z } ) ,
$$

and

$$
\ddot { z } ( t ) = \frac { d } { d t } f ( z ( t ) ) | _ { z } ( t ) = \bar { z } = f ^ { \prime } ( \bar { z } ) f ( \bar { z } ) ,
$$

where $\pmb { f } ^ { \prime }$ denotes the Jacobian matrix of $\boldsymbol { f }$ . In this way, the leading terms in the local error given above can be viewed as products of a coefficient function of a point $\bar { z }$ with a power of $\Delta t$ .

At the first integration step, the local error introduced is $\mathbf { l e } ( \Delta t ; z ^ { 0 } )$ . At the next step, the relevant term is $\mathbf { l e } ( \Delta t ; z ^ { 1 } )$ . A similar error is introduced at each step of the method. The issue then becomes how these errors accumulate over a certain time interval $[ 0 , T ]$ . The form that the global error development takes depends on the type of method involved. A global error bound for Euler’s method, for example, is easy to obtain under the assumption that $\boldsymbol { f }$ obeys a Lipschitz condition in an appropriate open set $D \subset \mathbb { R } ^ { k }$ containing the exact solution

$$
\| \ b { t } ( \pmb { u } ) - \pmb { t } ( \pmb { v } ) \| \leq L \| \pmb { u } - \pmb { v } \| , \qquad \mathrm { u n i f o r m l y ~ f o r ~ a l l ~ } \pmb { u } , \pmb { v } \in D ,
$$

where $L$ is a positive constant. The following theorem then tells us that the largest error in the numerical solution is proportional to the stepsize.

Theorem 1 Under the assumption (2.3), and provided the exact solution is twice continuously differentiable, then the error for Euler’s method admits a bound of the form

$$
\| z ( t _ { n } ) - z ^ { n } \| \leq K \left( e ^ { t _ { n } L } - 1 \right) \Delta t \leq K \left( e ^ { T L } - 1 \right) \Delta t , \quad n = 1 , 2 , \ldots , N ,
$$

where $\boldsymbol { K }$ is independent of the integration interval $T$ and the stepsize $\Delta t =$ $T / N$ . ✷

Proof. We first construct a recurrence relation for the numerical error defined by

$$
\begin{array} { r } { \pmb { e } ^ { n } = z ( t _ { n } ) - z ^ { n } . } \end{array}
$$

We make use of the Taylor expansion of the solution on the one hand and of the numerical method on the other, then regroup terms

$$
\begin{array} { l } { { \displaystyle e ^ { n + 1 } = \left( z ( t _ { n } ) + \Delta t \dot { z } ( t _ { n } ) + \frac { 1 } { 2 } \Delta t ^ { 2 } \ddot { z } ( \tau ) \right) - \left( z ^ { n } + \Delta t f ( z ^ { n } ) \right) } } \\ { ~ } \\ { { \displaystyle ~ = \left( z ( t _ { n } ) + \Delta t f ( z ( t _ { n } ) ) + \frac { 1 } { 2 } \Delta t ^ { 2 } \dot { z } ( \tau ) \right) - \left( z ^ { n } + \Delta t f ( z ^ { n } ) \right) } } \\ { ~ } \\ { { \displaystyle ~ = \left( z ( t _ { n } ) - z ^ { n } \right) + \Delta t \big ( f ( z ( t _ { n } ) ) - f ( z ^ { n } ) \big ) + \frac { 1 } { 2 } \Delta t ^ { 2 } \ddot { z } ( \tau ) , } } \end{array}
$$

$\tau \in \left[ t _ { n } , t _ { n + 1 } \right]$ . Next we take norms, apply the triangle inequality, and use the Lipschitz condition (2.3) to obtain

$$
\begin{array} { l } { \displaystyle \| e ^ { n + 1 } \| \le \| z ( t _ { n } ) - z ^ { n } \| + \Delta t \| f ( z ( t _ { n } ) ) - f ( z ^ { n } ) \| + \frac { 1 } { 2 } \Delta t ^ { 2 } \| \dot { z } ( \tau ) \| } \\ { \displaystyle \le ( 1 + \Delta t L ) \| e ^ { n } \| + \frac { 1 } { 2 } \Delta t ^ { 2 } \| \dot { z } ( \tau ) \| . } \end{array}
$$

Since the solution is twice continuously differentiable, we may bound $\ddot { z } ( \tau )$ on $[ 0 , T ]$ by a constant $M$ . Observe that a linear recurrence relation of the form

$$
a _ { n + 1 } \leq C a _ { n } + D
$$

satisfies the bound $\begin{array} { r } { a _ { n } \leq C ^ { n } a _ { 0 } + \frac { C ^ { n } - 1 } { C - 1 } D } \end{array}$ . The bound (2.4) with $\begin{array} { r } { K = \frac { M } { 2 L } } \end{array}$ follows by applying this result to the case at hand. In particular, we set $a _ { n } = \| e ^ { n } \|$ , $C = 1 + \Delta t L$ , $D = \Delta t ^ { 2 } M / 2$ and observe that $\partial ^ { 0 } = 0$ as well as

$$
( 1 + \Delta t L ) ^ { n } \leq \mathsf { e } ^ { n \Delta t L } .
$$

It is important to note several features of this bound, which is representative of the types of error bounds obtainable for numerical difference equations. First, the positive constant $L$ may be quite large (it can be obtained as the norm of the Jacobian matrix $\pmb { f } ^ { \prime }$ of $\pmb { f }$ ). The error bound thus grows exponentially in time and will quickly have little to tell us quantitatively about the numerical solution.

Fixing the length of the time interval, $\tau$ , the error inequality does provide us with a precise upper bound on the error and suggests that the error is reduced in proportion to the reduction of the stepsize. In practical applications, such a linear scaling relationship between the timestep and error is usually observed, even if the scaling factor is generally found to be rather smaller (but still exponential in $\tau$ ) in comparison with that given by the bound $( K e ^ { T L } )$ .

# 2.2 Numerical example: the Lennard–Jones oscillator

In many situations, the error will exhibit a nonuniform growth, due to abrupt changes in the dynamics. Let us illustrate this phenomenon by examining the growth of error when Euler’s method is applied to a Lennard–Jones oscillator

$$
\begin{array} { l } { { \dot { q } = v , } } \\ { { \dot { v } = - \varphi ^ { \prime } ( q ) , } } \end{array}
$$

where $\varphi ( q ) = q ^ { - 1 2 } - 2 q ^ { - 6 }$ . It is clear that the potential will rise rapidly without bound for $q  0$ , thus solutions of the system must be bounded away from $q = 0$ if the energy $E = v ^ { 2 } / 2 + \varphi ( q )$ is to remain constant along trajectories. Moreover, it can be shown that the solutions are bounded for $E \leq 0$ and unbounded for $E > 0$ . A trajectory is shown on the left in Fig. 2.3. On the right in the same figure, the energy error is plotted as a function of time, for a sample trajectory with stepsize $\Delta t = 0 . 0 0 1$ .

For studying examples such as this one, it is often useful to keep in mind a local propagation relation of the form

$$
\| \pmb { e } ^ { n + 1 } \| \le \left( 1 + \Delta t a ( t _ { n } ) \right) \| \pmb { e } ^ { n } \| + \Delta t ^ { 2 } b ( t _ { n } ) + O ( \Delta t ^ { 3 } ) .
$$

![](images/8ee4e507e77fe926e731c8a484e10928bd16b58887d9cb7e191de0df4841b753.jpg)  
Figure 2.3 Solution curves in the $q V \cdot$ -plane (left) and energy error (right) for Euler’s method applied to the Lennard–Jones oscillator.

The functions $a = a ( t )$ and $b = b ( t )$ depend on a particular trajectory of the system. Such an estimate would hold for any first-order method. For Euler’s method, we have

$$
\begin{array} { r l } & { a ( t _ { n } ) = \| f ^ { \prime } ( z ( t _ { n } ) ) \| , } \\ & { b ( t _ { n } ) = \underset { \tau \in [ t _ { n } , t _ { n + 1 } ] } { \operatorname* { m a x } } \frac { 1 } { 2 } \| \dot { z } ( \tau ) \| , } \end{array}
$$

where $z = z ( t )$ represents the particular trajectory of interest, and $\pmb { f } ^ { \prime }$ denotes the Jacobian matrix of $\pmb { f }$ . A proof is developed in the exercises of this chapter. While still only a bound, (2.5) indicates that increase in the error in Euler’s method at a timestep arises from two sources: the sensitivity of the solution to perturbations in the initial data (measured by $a ( t ) )$ ) and the local smoothness of the solution (measured by $b ( t )$ ).

Let us examine the bound (2.5) in the case of a nonlinear oscillator. In terms of the variables $q$ and $v = \dot { q }$ , the vector field has the expression

$$
f ( z ) = \left[ \begin{array} { c } { { v } } \\ { { - \varphi ^ { \prime } ( q ) } } \end{array} \right] .
$$

We can write the $2 \times 2$ Jacobian matrix of $\pmb { f }$ as

$$
{ \pmb f } ^ { \prime } ( z ) = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - \varphi ^ { \prime \prime } ( q ) } } & { { 0 } } \end{array} \right] .
$$

The 2-norm of a matrix $\pmb { A }$ is the square root of the magnitude of the largest eigenvalue of $A ^ { T } A$ , which for our Jacobian matrix is just $\mathsf { m a x } \{ 1 , | \varphi ^ { \prime \prime } ( q ) | \}$ . On

the other hand, the second derivative of a solution $z = z ( t )$ can be evaluated in terms of the vector field, i.e.

$$
\ddot { z } = { \left[ \begin{array} { l } { \ddot { q } } \\ { \ddot { v } } \end{array} \right] } = { \left[ - \varphi ^ { \prime } \right]} ^ { \phantom { \dagger } }  ,
$$

hence

$$
\| \dot { z } ( t ) \| = \sqrt { ( \varphi ^ { \prime } ( q ( t ) ) ) ^ { 2 } + ( \varphi ^ { \prime \prime } ( q ( t ) ) ) ^ { 2 } v ( t ) ^ { 2 } } .
$$

We can use the energy relation $\textstyle { \frac { 1 } { 2 } } v ^ { 2 } + \varphi ( q ) = E$ to replace the latter expression by one involving $q$ only. Summarizing, the two numbers $a ( t )$ and $b ( t )$ which govern the potential growth of errors in the bound (2.5) are

$$
\begin{array} { l } { { a ( t ) = \operatorname * { m a x } \{ 1 , | \varphi ^ { \prime \prime } ( q ( t ) ) | \} , } } \\ { { b ( t ) = \displaystyle \frac 1 2 \sqrt { ( \varphi ^ { \prime } ( q ( t ) ) ) ^ { 2 } + 2 ( \varphi ^ { \prime \prime } ( q ( t ) ) ) ^ { 2 } ( E - \varphi ( q ( t ) ) } . } } \end{array}
$$

If we graph these two numbers against time along a trajectory, we observe fluctuations in $^ { a }$ , $b$ and the error as shown in Fig. 2.4. Both $^ { a }$ and $b$ increase rapidly as $q$ approaches the singularity at $q = 0$ . The graphs indicate that the largest growth in the error is well correlated with the increase in a and $b$ .

This example highlights an important issue for numerical simulation: the need to incorporate adaptivity in the timestep when solving problems for which the solution exhibits a varying degree of smoothness on the relevant time interval. We will return to this issue in Chapter 9.

# 2.3 Higher-order methods

The Euler method is a first-order integrator, meaning that it has global error proportional to the stepsize. Higher-order methods have global error which satisfies a higher power law in the stepsize.

Suppose that a given one-step method $\psi _ { \Delta t }$ is such that, at some given point $\bar { z }$ of phase space, $\pmb { \psi } _ { \Delta t } ( \bar { z } )$ approximates the solution $z ( \Delta t , \bar { z } )$ through $\bar { z }$ for small $\Delta t$ . The quality of this local approximation can be measured by comparing the Taylor series expansions of $\pmb { \psi } _ { \Delta t } ( \bar { z } )$ and $z ( \Delta t , \bar { z } )$ in terms of $\Delta t$ . The order of the numerical one-step method is then defined as the largest integer $p \geq 1$ such that coefficients of the stepsize powers $\Delta t ^ { j }$ , $i = 1 , \dots , p$ , are identical in the Taylor series expansions or, in other words,

$$
| | \psi _ { \Delta t } ( \bar { z } ) - z ( \Delta t , \bar { z } ) | | \leq C \Delta t ^ { p + 1 } ,
$$

for all $\bar { z }$ in the domain of interest, where $C > 0$ is an appropriate constant.

![](images/6f32f7cb64e243107c186b910bb7ee71139d473215d0a7e1dcdc6d63d2097e7f.jpg)  
Figure 2.4 Comparison of the variation in coefficients a and $b$ with the evolution of the error.

Let us assume that our vector field satisfies the Lipschitz condition (2.3). For many classes of one-step methods, including the Runge–Kutta methods considered in the next subsection, it is then possible to show that the map $\psi _ { \Delta t }$ itself obeys a Lipschitz condition of the form:

$$
| | \psi _ { \Delta t } ( z _ { 1 } ) - \psi _ { \Delta t } ( z _ { 2 } ) | | \leq ( 1 + \bar { L } \Delta t ) | | z _ { 1 } - z _ { 2 } | | , \qquad \bar { L } \geq L .
$$

Using an argument very similar to that used to prove the convergence of Euler’s method (see, for example, [82] for details) one then finds that over a fixed time interval, the approximation of the flow by timesteps of size $\Delta t$ will be accurate to within $\mathcal { O } ( \Delta t ^ { p } )$ , i.e.,

$$
\begin{array} { r } { | | \psi _ { \Delta t } ^ { n } ( z ^ { 0 } ) - z ( n \Delta t , z ^ { 0 } ) | | \leq K \left( e ^ { \bar { L } T } - 1 \right) \Delta t ^ { p } , \qquad 1 \leq n \leq N , } \end{array}
$$

where $K > 0$ is an appropriate constant.

As mentioned above, the practical value of this type of estimate is severely limited by the presence of the exponential term involving the time interval, by the involvement of the Lipschitz constant which can be exceedingly large at certain points during the course of integration, and by the fact that the estimate does not take into account any structure of the map $\psi _ { \Delta t }$ , such as whether it is expanding or contracting. Nonetheless, the global error bound is useful on shorter time intervals.

Using relation (2.6) and the leading terms in the local error expansions for various methods worked out earlier, we can conclude that the Euler and implicit Euler methods are first-order accurate, while the trapezoidal rule and implicit midpoint methods are of second order.

# 2.4 Runge–Kutta methods

All of the methods discussed so far are special cases of Runge–Kutta methods.   
The class of general $S ^ { \th }$ -stage Runge–Kutta methods is given below.

![](images/817ca1f5e85f4dfa6481f3ec87be9db7bd12e29b1438da0675400708dd29b561.jpg)

The number of stages $s$ and the constant coefficients $\{ b _ { i } \}$ , $\{ a _ { i j } \}$ completely characterize a Runge–Kutta method. In general, such a method is implicit and leads to a nonlinear system in the $s$ internal stage variables $Z _ { j }$ . In some cases the formulas are layered in such a way that the first stage variable $Z _ { 1 }$ is given explicitly in terms of $z ^ { n }$ , then $Z _ { 2 }$ is determined from $z ^ { n }$ and $Z _ { 1 }$ , etc.

An example of a fourth-order explicit Runge–Kutta method is given next.

# A FOURTH-ORDER RUNGE–KUTTA METHOD (RK-4)

$$
\begin{array} { l } { { Z _ { 1 } = z ^ { n } , } } \\ { { \displaystyle Z _ { 2 } = z ^ { n } + \frac { 1 } { 2 } \Delta t f ( Z _ { 1 } ) , } } \\ { { \displaystyle Z _ { 3 } = z ^ { n } + \frac { 1 } { 2 } \Delta t f ( Z _ { 2 } ) , } } \\ { { \displaystyle Z _ { 4 } = z ^ { n } + \Delta t f ( Z _ { 3 } ) , } } \\ { { \displaystyle Z _ { n + 1 } = z _ { n } + \frac { \Delta t } { 6 } \left[ f ( Z _ { 1 } ) + 2 f ( Z _ { 2 } ) + 2 f ( Z _ { 3 } ) + f ( Z _ { 4 } ) \right] . } } \end{array}
$$

To see that this method has fourth order, one views (2.7)–(2.11) as defining a function $z ^ { n + 1 } = \pmb { \psi } _ { \Delta t } ( z ^ { n } )$ . We take the difference of this function with the solution $z ( \Delta t ; z ^ { n } )$ through $z ^ { n }$ , then expand this difference in a Taylor series about $\Delta t = 0$ . After some simplification, it will be found that the constant through fourthorder terms of this expansion in powers of $\Delta t$ vanish identically, and we are left with

$$
z ^ { n + 1 } - z ( \Delta t ; z ^ { n } ) = C _ { 5 } ( z ^ { n } ) \Delta t ^ { 5 } + \mathcal { O } ( \Delta t ^ { 6 } ) ,
$$

where the coefficient function $C _ { 5 } ( z )$ depends on the vector field $\pmb { f }$ and its derivatives. Since the method introduces a local error of size proportional to $\Delta t ^ { 5 }$ at each step, it will exhibit fourth-order global accuracy.

In some cases the increased order of accuracy associated with a particular higher-order explicit Runge–Kutta method may provide a better approximation of the solution, but this increased accuracy must be balanced against the increased work involved in computing the timestep. Moreover, in very long-term simulations or at large stepsizes, nonphysical effects generally become apparent, such as energy drift or artificial dissipation.

This is well illustrated by reconsidering the Lennard–Jones oscillator solved earlier with Euler’s method. The graph of solutions obtained using the fourthorder Runge–Kutta method given above is shown in Fig. 2.5 along with the energy error. It is immediately clear that the error is much smaller in magnitude, by a factor of more than ten, despite a much increased timestep of $\Delta t = 0 . 1$ . But note, too, that the energy error grows in a similar way, in jumps associated to the approach of $q$ to the singularity at the origin. If the simulation is carried out on a much longer time interval (but still very short in relation to an actual molecular dynamics simulation), the error steadily accumulates (Fig. 2.6, left) until the numerical solution bears little relation to the true orbit. Another important observation to be made from (2.6) is that the drift in the energy error (right panel) can be very small compared with the error being introduced in the solution itself. Qualitatively, the picture for Euler’s method and the picture for the fourth-order Runge–Kutta method are quite similar: steady drift is observed in the energy and in the solution trajectories, eventually rendering the results of numerical computation useless.

![](images/c1945b5712ff34d534fee1bfb0d8f35c853bedecff7f00cd90728de3ebeedf67.jpg)  
Figure 2.5 Solution curves in the $q V \cdot$ -plane (left) and energy error (right) for the fourth-order Runge–Kutta method applied to the Lennard–Jones oscillator.

![](images/ccbe3f2db1ebfb3e96cf6d89c36c1abb0530ec26fa72637470f8026786ae5edc.jpg)  
Figure 2.6 Solution curves in the $q V \cdot$ -plane (left) and energy error (right) for the fourth-order Runge–Kutta method applied to the Lennard–Jones oscillator on a time interval [0, 5000].

# 2.5 Partitioned Runge–Kutta methods

Yet another approach to approximating the solution trajectory is based on using different approximation formulas for different components of the solution. For example, we will often treat canonical Hamiltonian systems in this book which admit a natural dichotomy between positions and momenta. Partitioned Runge– Kutta (PRK) methods exploit this dichotomy by using different sets of quadrature rules for each subset of the variables. If the system can be written in the form $\begin{array} { r } { \frac { d } { d t } \pmb { u } = \pmb { g } ( \pmb { u } , \pmb { v } ) } \end{array}$ , $\begin{array} { r } { \frac { d } { d t } \pmb { v } = \pmb { h } ( \pmb { u } , \pmb { v } ) } \end{array}$ , then the associated Partitioned Runge–Kutta method of $S$ stages uses two sets of coefficients $\left( \{ \bar { b } _ { i } \} , \{ \bar { a } _ { i j } \} \right)$ and $( \{ \widetilde { b } _ { i } \} , \{ \widetilde { a } _ { i j } \} )$ , and computes the timestep as follows:

<table><tr><td>PARTITIONED RUNGE-KUTTA METHODS FOR du = g(u,v);v = h(u,v)</td></tr><tr><td></td></tr><tr><td>S un+1 =u&quot;+△t∑big(Ui, Vi), i=1</td></tr><tr><td>S vn+1 =v&quot;+△t∑bih(Ui,Vi), i=1</td></tr><tr><td>where，fori=1,2,...,s,</td></tr><tr><td>S</td></tr><tr><td></td></tr><tr><td>Ui = u&quot; +△t∑aijg(Ui, Vi),</td></tr><tr><td>i=1</td></tr><tr><td>s</td></tr><tr><td>Vi = v&quot; + △t∑aijh(Ui, Vi). i=1</td></tr></table>

These methods are often used for treating mechanically derived problems of the form:

$$
\pmb { M } \frac { d ^ { 2 } } { d t ^ { 2 } } \pmb { q } = - \nabla _ { \pmb { q } } V ( \pmb { q } ) ,
$$

with $\textbf { \em u } = \textbf { \em q }$ and $\begin{array} { r } { { \pmb v } = \frac { d } { d t } { \pmb q } } \end{array}$ , in which setting they are typically referred to as Runge–Kutta–Nystr¨om (RKN) methods.

One example of this type of Partitioned Runge–Kutta method is the method below

$$
\begin{array} { c } { { \pmb q ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb v } ^ { n } , } } \\ { { \pmb M \pmb v ^ { n + 1 } = { \pmb M \pmb v } ^ { n } - \Delta t \nabla _ { \pmb q } V ( { \pmb q } ^ { n + 1 } ) . } } \end{array}
$$

This method is very similar to Euler’s method, except that the vector field is evaluated in one component at time level $n + 1$ and in the other at time level $n$ . It is immediately obvious that we could as well have proposed the alternative method

$$
\begin{array} { c } { { \pmb q ^ { n + 1 } = \pmb q ^ { n } + \Delta t { \pmb v } ^ { n + 1 } , } } \\ { { \pmb M { \pmb v } ^ { n + 1 } = \pmb M { \pmb v } ^ { n } - \Delta t \nabla _ { \pmb q } \pmb V ( \pmb q ^ { n } ) . } } \end{array}
$$

Both of these methods are explicit and first-order accurate. We call these methods collectively the Asymmetrical Euler methods. To distinguish these two schemes, we refer to the first (2.12)–(2.13) as Asymmetrical Euler-A and the second as Asymmetrical Euler- $B$ (or, briefly, Euler- $A$ and Euler- $B$ ).

Another Partitioned Runge–Kutta method is the St¨ormer–Verlet method for Newton’s equations $\dot { \pmb q } = \pmb { v }$ , $M \dot { \pmb { v } } = - \nabla _ { \pmb { q } } V ( \pmb { q } ) )$ , defined as follows:

$$
\begin{array} { c } { { q ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb v } ^ { n + \frac { 1 } { 2 } } , } } \\ { { { \displaystyle M } { \pmb v } ^ { n + \frac { 1 } { 2 } } = { \pmb M } { \pmb v } ^ { n } - \frac { \Delta t } { 2 } \nabla _ { \pmb q } V ( { \pmb q } ^ { n } ) , } } \\ { { { \displaystyle M } { \pmb v } ^ { n + 1 } = { \pmb M } { \pmb v } ^ { n + \frac { 1 } { 2 } } - \frac { \Delta t } { 2 } \nabla _ { \pmb q } V ( { \pmb q } ^ { n + 1 } ) . } } \end{array}
$$

Evidently, the scheme is fully explicit, since we can evaluate successively the formula (2.17), then (2.16) and finally (2.18) without solving any nonlinear system. Note further that the discretization can be solved in terms of the half-step velocites $\pmb { v } ^ { n - \frac { 1 } { 2 } } , \pmb { v } ^ { n + \frac { 1 } { 2 } }$ , etc., resulting in

$$
\begin{array} { c } { { q ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb v } ^ { n + \frac { 1 } { 2 } } , } } \\ { { M \pmb v } ^ { n + \frac { 1 } { 2 } } = { \pmb M } { \pmb v } ^ { n - \frac { 1 } { 2 } } - \Delta t \nabla _ { \pmb q } V ( { \pmb q } ^ { n } ) . } \end{array}
$$

One can altogether eliminate the velocities from the St¨ormer–Verlet method to obtain the following two-step method in the coordinates only

$$
{ \cal M } \frac { { \pmb q } ^ { n + 1 } - 2 { \pmb q } ^ { n } + { \pmb q } ^ { n + 1 } } { \Delta t ^ { 2 } } = - \nabla _ { \pmb { q } } V ( { \pmb q } ^ { n } ) .
$$

This formulation is often called the leapfrog method. Both the leapfrog and the St¨ormer–Verlet formulation can be shown to be second-order accurate.

# 2.6 Stability and eigenvalues

![](images/159eb6aef7a9258c934a6633ecca30a2f520f2b9247d84c4f3b198863949a6b6.jpg)  
Figure 2.7 Numerical solution of the harmonic oscillator obtained using Euler’s method (left) and the Euler-B method (right).

If we graph a solution of the harmonic oscillator $\dot { \boldsymbol { q } } = \boldsymbol { v }$ ; $\dot { v } = - q$ we should see a circle in the phase plane (the $q v \cdot$ -plane). On the other hand, if we apply a numerical method and compute discrete points with the method, there is no reason to expect that these would lie on a circle. Numerical solutions obtained using two different methods are shown in Fig. 2.7, graphed along with the circle that would represent the exact solution for the chosen initial condition. Observe that the solutions spiral out in the case of the first method (left) and that they appear to lie on an ellipse in the case of the second method (right). The method used to produce the illustration on the left is Euler’s method, while the scheme used on the right is the Euler-B method (2.14)–(2.15) we encountered in the previous section.

While neither method exactly replicates the circular orbits, it seems clear that there is an important qualitative difference between the two schemes. The terminology we use to discuss this distinction is asymptotic stability. In this section, we show that the long-term asymptotic dynamics of numerical methods can be thoroughly understood in the case of the harmonic oscillator, or, more generally, any linear mechanical system.

Write the equation for the harmonic oscillator in the form

$$
\frac { d } { d t } z = { \bf A } z ,
$$

where

$$
\pmb { A } = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] .
$$

The solution at any time can be defined by a matrix (the fundamental solution matrix), $R ( t )$

$$
\begin{array} { r } { z ( t ; z ^ { 0 } ) = R ( t ) z ^ { 0 } , \qquad R ( t ) = \left[ \begin{array} { c c } { \cos \omega t } & { \frac { 1 } { \omega } \sin \omega t } \\ { - \omega \sin \omega t } & { \cos \omega t } \end{array} \right] , } \end{array}
$$

which has the eigenvalues $\mu _ { 1 , 2 } = e ^ { \pm i \omega t }$ , both of which lie on the unit circle. It is also easy to verify that the determinant of $R ( t )$ is equal to one.

The Euler’s method approximation leads to the mapping

$$
\begin{array} { r } { z ^ { n + 1 } = \hat { R } ( \Delta t ) z ^ { n } , \hat { R } ( \Delta t ) = \left[ \begin{array} { c c } { 1 } & { \Delta t } \\ { - \Delta t \omega ^ { 2 } } & { 1 } \end{array} \right] , } \end{array}
$$

where the propagation matrix $\hat { R } ( \Delta t )$ has the eigenvalues

$$
\hat { \lambda } _ { 1 , 2 } = 1 \pm i \Delta t \omega .
$$

The growth of error through the powers $[ \hat { R } ] ^ { n }$ is determined by the powers of the eigenvalues of that matrix. A numerical method is asymptotically stable if the growth of the solution for a linear model problem is asymptotically bounded. A sufficient condition for asymptotic stability is that the eigenvalues of the method are (i) in the unit disk in the complex plane, and (ii) simple (not repeated) if on the unit circle. Since the eigenvalues of Euler’s method are both of modulus greater than one, their powers grow exponentially fast and the method is unstable.

Note that the asymptotic instability of Euler’s method does not contradict the convergence of the method, since fixing any time interval $[ 0 , T ]$ and simultaneously driving the number of steps $N$ to infinity as $\Delta t \to 0$ so that $N \Delta t = T$ , we have

$$
\operatorname* { l i m } _ { N  \infty } ( \hat { \lambda } _ { 1 , 2 } ) ^ { N } = \operatorname* { l i m } _ { N  \infty } ( 1 \pm i \Delta t \omega ) ^ { N } = e ^ { \pm i \omega T } + O ( \Delta t ) .
$$

In some cases, it is possible to show that the eigenvalues of a numerical method applied to the harmonic oscillator also lie on the unit circle in the complex plane. Applying the St¨ormer–Verlet method to the harmonic oscillator results in the propagator

$$
\begin{array} { r } { \hat { R } ( \Delta t ) = \left[ \begin{array} { c c } { 1 - \frac { \Delta t ^ { 2 } \omega ^ { 2 } } { 2 } } & { \Delta t } \\ { - \Delta t \omega ^ { 2 } \left( 1 - \frac { \Delta t ^ { 2 } \omega ^ { 2 } } { 4 } \right) } & { 1 - \frac { \Delta t ^ { 2 } \omega ^ { 2 } } { 2 } } \end{array} \right] , } \end{array}
$$

which has eigenvalues

$$
\hat { \lambda } _ { 1 , 2 } = 1 - \mu ^ { 2 } \pm \sqrt { 2 \mu ^ { 2 } ( \frac { 1 } { 2 } \mu ^ { 2 } - 1 ) } , ~ \mu ^ { 2 } = \frac { 1 } { 2 } \Delta t ^ { 2 } \omega ^ { 2 } .
$$

Note that $\hat { \lambda } _ { 1 } \hat { \lambda } _ { 2 } = 1$ for all values of $\mu \geq 0$ implying that the determinant of $\hat { R } ( \Delta t )$ is equal to one. Furthermore, for $\mu ^ { 2 } < 2$ , the eigenvalues are complex, and

$$
| \hat { \lambda } _ { 1 , 2 } | ^ { 2 } = ( 1 - \mu ^ { 2 } ) ^ { 2 } + 2 \mu ^ { 2 } ( 1 - \frac { 1 } { 2 } \mu ^ { 2 } ) = 1 .
$$

For $\mu ^ { 2 } > 2$ , the eigenvalues are real and one has modulus greater than unity. Thus the St¨ormer–Verlet rule has a stability condition of the form

$$
\Delta t ^ { 2 } \omega ^ { 2 } < 4 ,
$$

when applied to the harmonic oscillator.

As we vary the stepsize $\Delta t$ from zero, the eigenvalues of the St¨ormer–Verlet method move around the unit circle until $\Delta t = 2 / \omega$ , at which timestep both eigenvalues are at $^ { - 1 }$ . For larger stepsizes, one eigenvalue heads toward the origin along the negative real axis, while the other goes off to infinity.

![](images/51406f897c6b25e88b29c86c719b7d195b38d8ed2df16fabe316db9304a43b28.jpg)  
Figure 2.8 Comparison of eigenvalue curves (bold, marked by arrows) for (a) the true propagator, (b) Euler’s method, and (c) the St¨ormer–Verlet method.

The eigenvalues for the propagators obtained by using Euler’s method and the St¨ormer–Verlet method are diagrammed in Fig. 2.8(b) and (c). Compare these curves (marked by arrows) with the eigenvalues of the exact propagator (Fig. 2.8(a). It is more useful to visualize the stability properties of the different methods as curves in three-dimensional space, parameterized by adding a dimension of time (or timestep). For the true propagator, these eigenvalue curves are helices on the cylinder of radius one (see Fig. 2.9). Numerical methods like Euler’s method (or the fourth-order Runge–Kutta method) have eigenvalue curves that leave the cylinder, even for small $\Delta t$ , whereas for certain other methods such as Euler-B (see Exercises) and St¨ormer–Verlet, the eigenvalues remain on the surface of the cylinder. until $\Delta t = 2 / \omega$ . The curves for Euler and St¨ormer–Verlet are also shown in Fig. 2.9. In Chapter 5, we will see that this desirable linear stability property can be viewed as the elementary consequence of certain general geometric principles respected by the St¨ormer–Verlet and Euler-B methods. In the case considered here, these geometric principles reduce to the fact that the determinant of the matrices $R ( t )$ and $\hat { R } ( \Delta t )$ , respectively, are equal to one.

![](images/45c7e3df14a8cc6e463ca5b8e6a91d9d6439bbbca32cf690c252b63a885742e5.jpg)  
Figure 2.9 Eigenvalue curves as functions of time or timestep. The eigenvalues of the exact propagator for the harmonic oscillator are helices on the unit cylinder, whereas the eigenvalues of Euler’s method immediately leave the cylinder. Those of St¨ormer–Verlet remain on the cylinder until $\Delta t = 2 / \omega$ .

We can easily extend this discussion to a $2 N \cdot$ -dimensional linear system of differential equations of the form

$$
\begin{array} { l } { \displaystyle { \frac { d } { d t } \boldsymbol { q } = \boldsymbol { v } , } } \\ { \displaystyle { \frac { d } { d t } \boldsymbol { v } = - \boldsymbol { K } \boldsymbol { q } . } } \end{array}
$$

We assume that $\kappa$ is an $N \times N$ constant symmetric matrix. (In general, if this system arose from Newton’s laws of motion in linear forces, or through a process of linearization of a nonlinear mechanical system, we might expect to find mass coefficients multiplying the accelerations in the second equation, but we ignore these for simplicity.)

The behavior of solutions to a linear system such as this one over time is determined by the eigenvalue–eigenvector structure of the matrix K. Recall that an eigenvalue–eigenvector pair for a symmetric $N \times N$ matrix $\kappa$ consists of a (real) scalar $\lambda$ and a nonzero N-vector $\pmb { v }$ , related by the equation

$$
K { \pmb v } = \lambda { \pmb v } .
$$

Furthermore the eigenvectors form a complete basis in $\mathbb { R } ^ { N }$ . Denote the eigenvalue– eigenvector pairs by $\left( \lambda _ { i } , v _ { i } \right)$ , $i = 1 , \dots , N$ . The eigenvectors can be viewed as the columns of a matrix $v$ with the property

$$
\begin{array} { r } { K V = [ K v _ { 1 } , K v _ { 2 } , \ldots , K v _ { N } ] = [ \lambda _ { 1 } v _ { 1 } , \lambda _ { 2 } v _ { 2 } , \ldots , \lambda _ { N } v _ { N } ] = V \Lambda , } \end{array}
$$

where $\wedge$ is a diagonal matrix with the eigenvalues on the diagonal. Since the columns of $v$ are linearly independent, the matrix $v$ is nonsingular, so we may premultiply both sides of the above equation by ${ \cal { V } } ^ { - 1 }$ to obtain

$$
\pmb { V } ^ { - 1 } \pmb { K } \pmb { V } = \pmb { I } ,
$$

and we say that the matrix $\kappa$ is diagonalizable.

Returning to the linear mechanical system, the behavior of solutions is now easily analyzed. Starting from the linear differential equations (2.22–2.23), we make the nonsingular changes of variables

$$
\pmb { q } ( t ) = \pmb { V } \pmb { u } ( t ) ,
$$

and

$$
\pmb { v } ( t ) = \pmb { V } \pmb { w } ( t ) ,
$$

resulting in the equations

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } V \pmb { u } = V \pmb { w } , } \\ { \displaystyle \frac { d } { d t } V \pmb { w } = - K V \pmb { u } . } \end{array}
$$

After premultiplying each equation by $V ^ { - 1 }$ , we arrive at

$$
\begin{array} { l } { \displaystyle { \frac { d } { d t } \boldsymbol { u } = \boldsymbol { w } , } } \\ { \displaystyle { \frac { d } { d t } \boldsymbol { w } = - V ^ { - 1 } K \boldsymbol { V } \boldsymbol { u } = - \boldsymbol { \Lambda } \boldsymbol { u } . } } \end{array}
$$

Because $\pmb { \Lambda }$ is diagonal, we see that the system of $2 N$ equations reduces to N decoupled $2 \times 2$ systems of the form

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } u _ { i } = w _ { i } , } \\ { \displaystyle \frac { d } { d t } w _ { i } = - \lambda _ { i } u _ { i } . } \end{array}
$$

The eigenvalues $\lambda _ { j }$ are real, since $\kappa$ is symmetric. If the matrix $\kappa$ is, moreover, positive definite, then the $\lambda _ { j }$ are all positive, and the decoupled systems are harmonic oscillators.

The numerical analysis of this system proceeds along similar lines. We apply a discretization method to (2.22)–(2.23), then use the same set of linear transformations to decouple the variables. In the end, we find that the stability of the numerical method on the linear system is determined by the stability of the same method when applied to each of the oscillators (2.24)–(2.25).

Thus, for a linear mechanical system with potential $\begin{array} { r } { V = \frac { 1 } { 2 } \pmb { q } ^ { T } K \pmb { q } } \end{array}$ , with $\kappa$ a symmetric positive definite matrix, the harmonic stability condition such as that for the St¨ormer–Verlet method (2.21) must be applied with $\omega ^ { 2 }$ replaced by each of the eigenvalues of the matrix K. For large systems, the number of eigenvalues and different components or modes of the solution will be similarly large, but for the asymptotic stability of the numerical solution, the restriction on the timestep for all of the components is determined by the timestep restriction for the fastest mode of the system.

Much recent research in numerical methods for differential equations is aimed at developing new classes of methods which allow the slow modes to be propagated more efficiently in the presence of such high-frequency components, and we introduce some such schemes in Chapter 10.

# 2.7 Exercises

1. Euler’s method. Assume that the vector field $\boldsymbol { f }$ is continuously differentiable and a given solution $z = z ( t )$ is twice continuously differentiable. Assume the convergence of Euler’s method, then use this to prove the following error growth relation for Euler’s method

$$
\| \pmb { e } ^ { n + 1 } \| \le \left( 1 + \Delta t a ( t _ { n } ) \right) \| \pmb { e } ^ { n } \| + \Delta t ^ { 2 } b ( t _ { n } ) + \mathcal { O } ( \Delta t ^ { 3 } ) ,
$$

where

$$
\begin{array} { r l } & { a ( t _ { n } ) = \| \pmb { f ^ { \prime } } ( \pmb { z } ( t _ { n } ) ) \| , } \\ & { b ( t _ { n } ) = \underset { \tau \in [ t _ { n } , t _ { n + 1 } ] } { \operatorname* { m a x } } \frac { 1 } { 2 } \| \ddot { \ b { z } } ( \tau ) \| . } \end{array}
$$

2. Asymmetrical Euler: order of accuracy. Show that the Euler-B method (2.14)–(2.15) is a Partitioned Runge–Kutta method by defining all of the relevant coefficients. Show that this method introduces an error proportional to $\Delta t ^ { 2 }$ in one step when applied to a general one-degree-of-freedom problem and find the leading term in the local error expansion for this method.

3. Asymmetrical Euler: stability. Determine the stability condition for the Euler-A method using the technique of Section 2.6, and graph the eigenvalues when applied to the harmonic oscillator. Compare with the corresponding stability conditions of the St¨ormer–Verlet and Euler methods.

4. Stability: the pendulum. Consider the planar pendulum described by

$$
\ddot { \theta } = - \frac { g } { L } \sin \theta ,
$$

where $g$ is the earth’s gravitational constant and $L$ the length of the pendulum. Using a linearization of this equation, determine the stepsize stability restriction for the Euler-B method applied to integrate the system near the hanging-down configuration $( \theta = 0$ ).

Note: In general, the stability of the discrete linearized problem at a critical point does not automatically imply the stability of the corresponding nonlinear equations. In order to say something about the latter, more powerful methods such as the KAM theory must typically be invoked (see, for example, [197]).

5. Boundary of the stability region. We have seen that for $\Delta t \omega < 2$ , the eigenvalues of the St¨ormer–Verlet method applied to the Harmonic oscillator are both on the unit circle and are distinct. The special case $\Delta t \omega = 2$ is interesting, since it represents the boundary of the stability region. Is the St¨ormer–Verlet method stable when applied to the Harmonic oscillator (in the sense that the numerical solution is bounded asymptotically for all $n$ ) when $\Delta t \omega = 2 ?$ Explain.

6. Linear spring-mass system. Consider a linear system in 1D consisting of $N -$ point particles with nonuniform masses $m _ { j }$ , with the $i , j$ particle pair joined by a zero rest-length spring (spring constant $k _ { j j }$ ).

a. Show that the total potential energy can be written $\begin{array} { r } { V = \frac { 1 } { 2 } \pmb { q } ^ { T } K \pmb { q } } \end{array}$ , where $\kappa$ is a symmetric, positive semi-definite matrix, then show that the equations of motion are in the form of an $N .$ -body system

$$
M \frac { d ^ { 2 } } { d t ^ { 2 } } \pmb q = - K \pmb q ,
$$

where $M$ is a diagonal matrix.

b. Introduce a scaling $\tilde { \pmb q } _ { i } = \sqrt { m _ { i } } \pmb q _ { i }$ and show that in the new variables, the equations can be written

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } \tilde { \pmb q } = - \tilde { \cal K } \tilde { \pmb q } ,
$$

where $\tilde { \kappa }$ is symmetric and positive semi-definite.

c. Consider the special case of a homogeneous nearest neighbor spring system with both boundaries fixed at the origin, $N$ unit masses, and uniform spring constant $\kappa$ . Write out the solution in this case. Hint: The $N \times N$ matrix $\pmb { A } = \left( a _ { i j } \right)$ with

$$
a _ { i j } = \left\{ { \begin{array} { l l } { - 2 , } & { i = j } \\ { 1 , } & { | { \it { i } } - { \it { j } } | = 1 } \\ { 0 , } & { { \mathrm { e } } { \mathrm { l s e } } } \end{array} } \right.
$$

has eigenvalues

$$
\lambda _ { k } = - 2 ( 1 + \cos ( \theta _ { k } ) ) ,
$$

and corresponding eigenvectors $\pmb { u } _ { k }$ with components

$$
u _ { k j } = \mathsf { s i n } ( j \theta _ { k } ) , \qquad j = 1 , \ldots , N ,
$$

where $\begin{array} { r } { \theta _ { k } = \frac { \pi k } { N + 1 } } \end{array}$ , $k = 1 , 2 , \ldots , N .$

d. Determine the numerical stability restriction for using Euler’s method and the St¨ormer–Verlet method to solve this linear spring-mass system, as a relation involving $N$ and $\Delta t$ .

7. Flow maps and numerical methods. A set $\mathcal { G }$ together with an associative product relation $^ *$ is called a group if (i) $\mathcal { G }$ is closed under $^ *$ , i.e. $g _ { 1 } , g _ { 2 } \in \mathcal { G }$ implies $g _ { 1 } * g _ { 2 } \in \mathcal { G } ,$ , (ii) $\mathcal { G }$ contains an identity element $e$ such that $e * g =$ $g * e = g$ , and (iii) for any element $g \in { \mathcal { G } }$ there is an inverse element $g ^ { - 1 } \in \mathcal { G }$ such that $g * g ^ { - 1 } = g ^ { - 1 } * g = e$ .

a. Suppose that a given differential equation

$$
{ \frac { d } { d t } } z = { \pmb f } ( z )
$$

admits solutions defined for infinite time in both the positive and negative directions. Show that the flow maps $\{ \pmb { \phi } _ { t } \} _ { t \in \mathbb { R } }$ defined as the mappings which take points $\bar { z }$ to points $t$ units in time later along the solution passing through $\bar { z }$ constitute a one-parametric group, where the group operation $^ *$ is a composition of maps and

$$
\pmb { \psi } _ { t _ { 1 } + t _ { 2 } } = \pmb { \phi } _ { t _ { 2 } } \circ \pmb { \phi } _ { t _ { 1 } } .
$$

b. Consider now the set $\hat { \mathcal { G } }$ which consists of all the mappings defined by applying Euler’s method with timesteps $\Delta t > 0$ . Does $\hat { \mathcal { G } }$ constitute a one-parametric group in the above sense with $\Delta t$ taking the role of time $t ?$

8. Computer project with one-step methods. In this exercise you will write a small computer program to test a numerical method for solving $\dot { \boldsymbol { q } } ~ = ~ \boldsymbol { v }$ , $\dot { v } = - \varphi ^ { \prime } ( q )$ , $q ( 0 ) = q ^ { 0 }$ , $v ( 0 ) = v ^ { 0 }$ . Refer to the preface for a discussion of computer software.

a. Write a module eulerstep that takes as input:

• an arbitrary function $\varphi : \mathbb { R }  \mathbb { R }$ , real scalars $q ^ { n } , v ^ { n } , \Delta t$ ,

and computes the result of taking a single step with Euler’s method applied to the differential equation.

b. Write a computer program stepper which takes as inputs:

an arbitrary function $\varphi : \mathbb { R }  \mathbb { R }$ ,   
. real scalars $q ^ { 0 } , v ^ { 0 } , \Delta t$ ,   
integer $N$ , the name of a module (such as eulerstep) which implements a one-step method for the differential equation. Then solve the system ${ \dot { q } } = v$ , $\dot { v } = - \varphi ^ { \prime } ( q )$ by taking $N$ steps with Euler’s method starting from $q ^ { 0 } , \ v ^ { 0 }$ . The program should produce as output a pair of $( N + 1 )$ one-dimensional arrays $Q$ , $v$ consisting of the beginning and ending of positions and velocities and all intermediate steps.   
c. Write modules eulerAstep, eulerBstep, stormerstep and rk4step with similar inputs and outputs to the module eulerstep but implementing a single timestep of the Euler-A, Euler-B, St¨ormer–Verlet, and fourth-order Runge–Kutta methods of the text.   
d. Experiment with the various methods using the stepper routine. Examine the energy conservation of the various methods, when applied to a Morse oscillator with unit coefficients, $\varphi ( q ) = ( 1 - \exp ( - q ) ) ^ { 2 }$ .

# 3

# Hamiltonian mechanics

In this chapter we introduce the Hamiltonian formulation of classical mechanics. The elementary properties of Newton’s equations such as the conservation of energy or momentum can be explained without much difficulty by the use of nothing more than the chain rule of calculus, but it turns out that there is another, deeper level of structure that relates to the properties of bundles of trajectories emanating from a set of initial conditions. The most useful tool for describing the solutions is the flow map already introduced in the previous chapter.

For any differential equation $\dot { z } = f ( z )$ , recall that we denote the solution through a given initial condition $z ^ { 0 }$ by $\boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ . Assuming that this solution is globally defined, we may fix a value of $t$ , and consider the trajectories starting from any arbitrary point $z ^ { 0 }$ in phase space. The flow map $\pmb { \phi } _ { t }$ is the mapping from initial points $z ^ { 0 }$ to final points $\boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ along trajectories, thus

$$
z ( t ; z ^ { 0 } ) = \pmb { \phi } _ { t } ( z ^ { 0 } ) .
$$

For conservative mechanical systems, it turns out that the flow map inherits certain global qualitative or geometric properties which are, in a very real sense, as fundamental as any of the physical laws which characterize our understanding of the properties of matter. An example of such a qualitative property is the conservation of the volume of a set of points of phase space under their simultaneous time evolution. Another example is found in the stringent restrictions placed on the asymptotic behavior of solutions of Hamiltonian systems near equilibrium points. In this chapter, we explore the geometric properties which are the consequences of Hamiltonian mechanics. This treatment is necessarily restricted; the reader is referred to the preface for suggestions for further reading.

# 3.1 Canonical and noncanonical Hamiltonian systems

Let us begin our discussion by recalling Newton’s equations (1.1)–(1.2) for $N$ particles moving in $\mathbb { R } ^ { 3 }$ . To compactify the notation, we introduce the diagonal

mass matrix $\pmb { M } \in \mathbb { R } ^ { 3 N \times 3 N }$ such that

$$
M \pmb { v } = ( m _ { 1 } \pmb { v } _ { 1 } , \dots , m _ { N } \pmb { v } _ { N } ) ^ { T } .
$$

We also eliminate the particle velocities and write (1.1)–(1.2) as a second-order differential equation

$$
M \ddot { \pmb q } = \pmb { F } ( \pmb q )
$$

in the vector of particle coordinates

$$
\pmb { q } : = ( \pmb { q } _ { 1 } , \dots , \pmb { q } _ { N } ) ^ { T } .
$$

The force $\boldsymbol { F }$ is given by the negative gradient of a potential energy function with respect to position

$$
\pmb { \cal F } ( \pmb { q } ) : = - \nabla _ { \pmb { q } } V ( \pmb { q } ) .
$$

The Hamiltonian formulation of Newtonian mechanics reduces (3.1) back to a system of first-order equations, but instead of including the particle velocities it relies on the vector of linear momenta $\pmb { p } \in \mathbb { R } ^ { 3 N }$ defined by

$$
p : = M { \dot { q } } .
$$

There are obviously many ways to rewrite second-order equations as systems of first-order equations. A priori, there is no reason why one approach should have a significant advantage over another. The observation of Hamilton was that the differential equations defining both position and momentum are obtained by dual operations on the same total energy function.

For Newtonian mechanics, the differential equations take the following form:

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \pmb q } = { \pmb M } ^ { - 1 } { \pmb p } } , \ } \\ { { \displaystyle { \frac { d } { d t } } { \pmb p } = - \nabla _ { \pmb q } V ( { \pmb q } ) . } \ } \end{array}
$$

The equations (3.2)–(3.3) are termed a Hamiltonian system with Hamiltonian (or energy)

$$
H ( \pmb { q } , \pmb { p } ) : = \frac { \pmb { p } ^ { T } M ^ { - 1 } \pmb { p } } { 2 } + V ( \pmb { q } ) ,
$$

which is a first integral (constant of motion), i.e.

$$
\frac { d } { d t } H ( \pmb { q } ( t ) , \pmb { p } ( t ) ) = \pmb { p } ( t ) ^ { T } \pmb { M } ^ { - 1 } \pmb { \dot { p } } ( t ) + \pmb { \dot { q } } ( t ) ^ { T } \nabla _ { \pmb { q } } V ( \pmb { q } ( t ) ) = 0 ,
$$

along solutions $( \pmb q ( t ) , \pmb p ( t ) )$ of (3.2)–(3.3).

It is easy and useful to generalize equations (3.2)–(3.3). Given a phase space $\mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$ of arbitrary (even) dimension $2 d \geq 2$ and an arbitrary (smooth) Hamiltonian function $H : \mathbb R ^ { d } \times \mathbb R ^ { d } \to \mathbb R$ , the corresponding canonical Hamiltonian equations of motion are

$$
\begin{array} { c } { { \displaystyle { \frac { d } { d t } } \pmb { q } = + \nabla _ { p } H ( \pmb { q } , \pmb { p } ) , } } \\ { { \displaystyle { \frac { d } { d t } } \pmb { p } = - \nabla _ { \pmb { q } } H ( \pmb { q } , \pmb { p } ) . } } \end{array}
$$

It now becomes evident that the change of variables to positions and momenta has uncovered a symmetry in their function (or, rather, an antisymmetry, since we also have a change of sign). We will see shortly that this antisymmetry, together with the smoothness of the solutions with respect to perturbation of the initial data, has important ramifications for the flow map of the system.

When discussing Hamiltonian systems, it is often convenient to use the notation

$$
z : = ( q , p ) ^ { T } ,
$$

with $\pmb q , \pmb p \in \mathbb { R } ^ { d }$ , $z \in \mathbb { R } ^ { 2 d }$ , and to introduce the $2 d \times 2 d$ canonical structure matrix $\jmath$ ,

$$
J : = \left[ \begin{array} { c c } { { { \bf 0 } } } & { { + I _ { d } } } \\ { { - I _ { d } } } & { { { \bf 0 } } } \end{array} \right] .
$$

Then the Hamiltonian system (3.4)–(3.5) can be rewritten in compact form:

$$
\frac { d } { d t } z = J \nabla _ { z } H ( z ) .
$$

The term “canonical” is reserved for Hamiltonian systems on an even dimensional Euclidean space with $\jmath$ as in (3.6), but Hamiltonian systems can be generalized in various ways without altering the discussion of their geometric properties in any essential way. For example, we may allow $\jmath$ to be an arbitrary invertible constant skew-symmetric matrix (with $J ^ { T } = - J$ ). Still more generally, we may allow, under suitable restrictions, the structure matrix itself to depend on the phase space variable $z$ , i.e. $\begin{array} { r } { J = J ( z ) } \end{array}$ , or the phase space may be replaced by an appropriate smooth, even-dimensional manifold.1

The system (3.7) is an example of an autonomous differential equation, meaning that the vector field is formally independent of time. Time-dependent or non-autonomous Hamiltonian systems with $H = H ( z , t )$ also arise frequently in applications. The equations of motion are then given by

$$
\frac { d } { d t } z = J \nabla _ { z } H ( z , t ) .
$$

In most cases, the special structures associated to autonomous Hamiltonian systems are easily extended to non-autonomous systems.

# 3.2 Examples of Hamiltonian systems

In this section, we survey some of the many types of Hamiltonian systems that arise in the physical sciences. It is our experience that having a feel for the types of applications which may arise is important to understanding both the theoretical and numerical issues associated with their study.

# 3.2.1 Linear systems

A canonical linear Hamiltonian system is defined by a quadratic Hamiltonian $\begin{array} { r } { H = \frac { 1 } { 2 } z ^ { T } L z } \end{array}$ , where $\pmb { L }$ is a symmetric $2 d \times 2 d$ matrix and $J$ a structure matrix of type (3.6). The equations of motion are thus

$$
\frac { d } { d t } z = J L z .
$$

A matrix of the form $A = J L$ with $\pmb { L }$ symmetric is typically referred to as a Hamiltonian matrix. For example, the harmonic oscillator is a one-degree-offreedom linear Hamiltonian system with

$$
\begin{array} { r } { L = \left[ \begin{array} { c c } { \omega ^ { 2 } } & { 0 } \\ { 0 } & { 1 } \end{array} \right] , } \end{array}
$$

and $z = ( q , p ) ^ { T }$

The solution of a linear Hamiltonian system is formally computable in terms of the eigenvalues and eigenvectors of the matrix $A = J L$ . (In practice, the computation of the eigenstructure may be quite involved, so the solution is often propagated instead by an appropriate numerical method.) It is interesting to consider some of the properties of this eigenstructure. Since $A = J L$ is real, it follows that the eigenvalues occur in complex conjugate pairs. Moreover, if $\lambda$ is an eigenvalue of $\pmb { A }$ , it follows that $\lambda$ is also an eigenvalue of $\pmb { A } ^ { T } = \pmb { L } ^ { T } \pmb { J } ^ { T } = - \pmb { L } \pmb { J }$ , i.e.

![](images/b1ed1ab72597e19bcb9372772437749aa1fb78d3382e0b1d2c69c839554ecf68.jpg)  
Figure 3.1 If $\lambda$ is an eigenvalue of a Hamiltonian matrix, then so are $\bar { \lambda }$ , $- \lambda$ , and $- \bar { \lambda }$ .

$$
- L J u = \lambda u
$$

for some $\pmb { u }$ . Let ${ \pmb v } = J { \pmb u }$ , then we have

$$
- \pmb { L } \pmb { v } = \lambda \pmb { J } ^ { - 1 } \pmb { v } ,
$$

and, after premultiplying by $\jmath$

$$
- J L v = \lambda v .
$$

This means that $- \lambda$ is also an eigenvalue of $\pmb { A }$ (with eigenvector $\mathbf { \nabla } J \mathbf { \nabla } \mu$ ). Summarizing, if $\lambda$ is an eigenvalue of a Hamiltonian matrix, then so are $\bar { \lambda }$ , $- \lambda$ , and, by extension, $- \bar { \lambda }$ . A Hamiltonian matrix therefore has a symmetric spectrum with respect to both coordinate axes of the complex plane (Fig. 3.1).

# 3.2.2 Single-degree-of-freedom problems

Anharmonic one-degree-of-freedom oscillators with Hamiltonians of the form $H ( q , p ) = p ^ { 2 } + \varphi ( q )$ are also of interest. In the previous chapters we encountered the Lennard–Jones oscillator, with potential

$$
\varphi _ { \mathsf { L . J . } } ( q ) = \epsilon \left[ \left( \frac { \bar { r } } { q } \right) ^ { 1 2 } - 2 \left( \frac { \bar { r } } { q } \right) ^ { 6 } \right] .
$$

As another example, the plane pendulum can be described in terms of the angle $q$ made with the vertical axis by the Hamiltonian

$$
H = { \frac { 1 } { 2 } } p ^ { 2 } - { \frac { g } { L } } \cos q ,
$$

where $L$ is the length of the pendulum and $g$ the gravitational constant.

The phase portrait of a planar system qualitatively summarizes the global dynamics by depicting a few representative orbits in the $q , p$ domain. These orbits can obviously be identified with pieces of the curves defined by the equation $H ( q , p ) =$ constant, thus we may view the orbits as level curves of the Hamiltonian function. The graph of the surface $E = H ( q , p )$ in $( q , p , E )$ -space characterizes the dynamics of a single-degree-of-freedom system. In particular, the equilibria are associated with critical points on this surface: local minima correspond to stable equilibria, while saddle points correspond to unstable equilibria. In Fig. 3.2, we show the graph of $E = H ( q , p )$ together with the phase portrait (level curves of $H$ ) for the Lennard–Jones oscillator $\epsilon = 0 . 2 5$ , $\bar { r } = 1$ ) and the pendulum $g / L = 1$ ).

![](images/207cf65f7b9510ac8395ac64a600ee0485d830aa18a71d17377521d47f8ee6e3.jpg)  
Figure 3.2 Energy surfaces for one-degree-of-freedom problems, and phase portraits. Left, Lennard–Jones oscillator. Right, plane pendulum.

# 3.2.3 Central forces

Next, consider the three-degree-of-freedom nonlinear system describing the motion of a body of unit mass in $\mathbb { R } ^ { 3 }$ , i.e. $\pmb q = ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) ^ { T }$ , with a potential energy of interaction given by $\varphi = \varphi ( r )$ where $r$ represents the distance from the body to

the origin. This is an instance of a central-force problem. If $\varphi ( r ) = - 1 / r$ , then we have the Kepler problem with Hamiltonian

$$
H = \frac { 1 } { 2 } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } + p _ { 3 } ^ { 2 } ) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } } } .
$$

The level sets of constant energy are five dimensional surfaces (!), hence nontrivial to visualize, but, as we shall see in Section 3.3, a complete description of the dynamics of the system is still easily obtained by using some additional properties of the equations.

# 3.2.4 Charged particle in a magnetic field

Up to normalization of certain constants, the Kepler problem can be viewed as a model of gravitational dynamics. It also represents, qualitatively, the classical model of an electron in the field of a positively charged fixed nucleus. It is interesting to consider in this context a generalization in which the electron moves not only under the Coulombic potential, but also in an applied (constant) magnetic field. If $\pmb { b } = ( b _ { 1 } , b _ { 2 } , b _ { 3 } ) ^ { T }$ is a vector representing such a field, the equations of motion for the particle are found to take the form

$$
m \ddot { \pmb q } = - \gamma \frac { \pmb q } { \lVert \pmb q \rVert ^ { 3 } } + \pmb { b } \times \dot { \pmb q } ,
$$

where $m$ is the mass of the particle, $\gamma$ is a positive constant, and $\times$ is the usual cross product of vectors.

Defining the momenta in the usual way, we have the first-order system

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \pmb { q } = \frac { 1 } { m } \pmb { p } , } \\ { \displaystyle \frac { d } { d t } \pmb { p } = - \gamma \frac { \pmb { q } } { \| \pmb { q } \| ^ { 3 } } - \frac { 1 } { m } \pmb { p } \times \pmb { b } . } \end{array}
$$

Here $\pmb q$ , and $\pmb { p }$ are assumed to be vectors in $\mathbb { R } ^ { 3 }$ . It is easy to show that this is not a canonical Hamiltonian system, since, if it were, we would have to have

$$
\nabla _ { \boldsymbol { p } } \boldsymbol { H } = \frac { 1 } { m } \boldsymbol { p } , \qquad \nabla _ { \boldsymbol { q } } \boldsymbol { H } = \gamma \frac { \boldsymbol { q } } { \| \boldsymbol { q } \| ^ { 3 } } + \frac { 1 } { m } \boldsymbol { p } \times \boldsymbol { b } ,
$$

and equality of mixed partials would be violated. However, a Hamiltonian description (3.7) does follow if we define instead

$$
\boldsymbol { J } = \left[ \begin{array} { l l } { 0 } & { \boldsymbol { I } } \\ { - \boldsymbol { I } } & { \boldsymbol { \widehat { b } } } \end{array} \right] ,
$$

where $\widehat { b }$ is the skew symmetric matrix defined by

$$
\begin{array} { r } { \widehat { \pmb { b } } = \left[ \begin{array} { c c c } { 0 } & { - b _ { 3 } } & { b _ { 2 } } \\ { b _ { 3 } } & { 0 } & { - b _ { 1 } } \\ { - b _ { 2 } } & { b _ { 1 } } & { 0 } \end{array} \right] , } \end{array}
$$

taking as Hamiltonian2

$$
H ( \pmb q , \pmb p ) = \frac { 1 } { 2 m } \| \pmb { p } \| ^ { 2 } - \frac { \gamma } { \| \pmb q \| } .
$$

# 3.2.5 Lagrange’s equation

Given a Lagrangian function $L ( \pmb q , \dot { \pmb q } )$ , Lagrange’s equation of motion is

$$
\frac { d } { d t } \nabla _ { \dot { q } } L ( \pmb { q } , \dot { \pmb { q } } ) - \nabla _ { \pmb { q } } L ( \pmb { q } , \dot { \pmb { q } } ) = \mathbf { 0 } .
$$

This equation is the Euler–Lagrange equation minimizing the action integral

$$
\mathcal { L } [ \pmb { q } ] = \int _ { t _ { 0 } } ^ { t _ { 1 } } L ( \pmb { q } ( t ) , \dot { \pmb { q } } ( t ) ) d t .
$$

For more details see [7, 8, 73]. Lagrange’s equation (3.13) is second order in time. It is reduced to a system of first-order equations by introducing the conjugate momenta

$$
\pmb { p } = \nabla _ { \dot { \pmb { q } } } L ( \pmb { q } , \dot { \pmb { q } } ) .
$$

We require that this relation defines a one-to-one map between $p$ and $\dot { \pmb q }$ for fixed $\pmb q$ . It can be shown (see problem 1 in the Exercises) that the equation (3.14) together with the reformulation

$$
\pmb { \dot { p } } = \nabla _ { \pmb { q } } L ( \pmb { q } , \dot { \pmb { q } } )
$$

of Lagrange’s equation (3.13) are canonical with Hamiltonian

$$
H ( { \pmb q } , { \pmb p } ) = { \pmb p } \cdot \dot { \pmb q } - L ( { \pmb q } , \dot { \pmb q } ) .
$$

For example, take a particle of unit mass moving in a central field. The Lagrangian is

$$
L = \frac { 1 } { 2 } ( \dot { q } _ { 1 } ^ { 2 } + \dot { q } _ { 2 } ^ { 2 } + \dot { q } _ { 3 } ^ { 2 } ) + \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } } } .
$$

Note the change in sign compared with the Hamiltonian (3.9). The conjugate momenta is

$$
\begin{array} { r } { p = \dot { \pmb q } , } \end{array}
$$

as expected.

The charged particle in a magnetic field has Lagrangian

$$
L = \frac { m } { 2 } \| \dot { \pmb q } \| ^ { 2 } + \frac { \gamma } { \| \pmb q \| } + \frac { 1 } { 2 } \pmb q ^ { T } \widehat b \dot { \pmb q } .
$$

According to (3.14), the conjugate momenta is

$$
\pmb { p } = m \dot { \pmb q } - \frac 1 2 \widehat { \pmb { b } } \pmb { q } .
$$

This definition of $p$ is different from the one used in Section 3.2.4! In Problem 1 in the Exercises you will be asked to derive the associated Hamiltonian and to verify the canonical equations of motion (3.32)–(3.33). This example emphasizes the point that the Hamiltonian formulation of a problem need not be unique and that there is a certain freedom in the choice of the Hamiltonian $H$ and the structure matrix $\jmath$ .

# 3.2.6 $N$ -body problem

Finally, let us return to the homogeneous system of $N$ bodies moving in $\mathbb { R } ^ { 3 }$ with masses $m _ { j }$ , $i = 1 , \dots , N$ , interacting through a particle–particle interaction potential (pair-potential) $\varphi ( r )$ , with $r$ the distance between two particles. The corresponding canonical equations of motion are

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } { \pmb q } _ { i } = \frac { 1 } { m _ { i } } { \pmb p } _ { i } , } \\ { \displaystyle \frac { d } { d t } { \pmb p } _ { i } = - \sum _ { i \neq j } \frac { \varphi ^ { \prime } ( r _ { i j } ) } { r _ { i j } } ( { \pmb q } _ { i } - { \pmb q } _ { j } ) , \qquad i = 1 , 2 , \dots , N , } \end{array}
$$

where $r _ { i j } = | | \pmb { q } _ { i } - \pmb { q } _ { j } | |$ ; the Hamiltonian function is

$$
H = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } \frac { | | \pmb { p } _ { i } | | ^ { 2 } } { m _ { i } } + \sum _ { i = 1 } ^ { N - 1 } \sum _ { j = i + 1 } ^ { N } \varphi ( r _ { i j } ) .
$$

# 3.3 First integrals

A first integral, constant of motion, or conserved quantity of a general differential equation is a function $G : \mathbb { R } ^ { 2 d }  \mathbb { R }$ which is constant along all solution curves $\boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ of the system, i.e.

$$
G ( z ( t ; z ^ { 0 } ) ) = G ( z ^ { 0 } ) ,
$$

for all $z ^ { 0 } \in \mathbb { R } ^ { 2 d }$ and all $t \in \mathbb R$ . We say that having a first integral is a “geometric property” of a system of differential equations because its existence implies that the solutions are at least partly described by the geometry of the lowerdimensional manifolds $\{ z \in \mathbb { R } ^ { 2 d } \mid G ( z ) = { \mathsf { c o n s t a n t } } \}$ .

What are the conditions that ensure that a particular function $G$ is a first integral for a canonical Hamiltonian system (3.7)? Assume that $z ( t )$ is a solution curve of (3.7), then

$$
\begin{array} { r l } & { \frac { d } { d t } G ( z ( t ) ) = \nabla _ { z } G ( z ( t ) ) \cdot \dot { z } ( t ) } \\ & { \qquad = \left[ \nabla _ { z } G ( z ( t ) ) \right] ^ { T } \dot { z } ( t ) } \\ & { \qquad = \left[ \nabla _ { z } G ( z ( t ) ) \right] ^ { T } J \nabla _ { z } H ( z ( t ) ) . } \end{array}
$$

If this quantity is to vanish for every trajectory $\boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ with initial conditions chosen from some open set in phase space, we must have that the Poisson bracket of $G$ and $H$ , defined by

$$
\{ G , H \} ( z ) : = \left[ \nabla _ { z } G ( z ) \right] ^ { T } J \nabla _ { z } H ( z ) ,
$$

vanishes identically, i.e.

$$
\{ G , H \} ( z ) \equiv 0 .
$$

This is a necessary and sufficient condition for $G$ to be a first integral of a Hamiltonian system with Hamiltonian $H$ .

More generally, the time evolution of an arbitrary, smooth function $G : \mathbb { R } ^ { 2 d } $ $\mathbb { R }$ along a solution of a canonical system with Hamiltonian $H$ is given by

$$
\frac { d } { d t } G ( z ) = \{ G , H \} ( z ) .
$$

For example, take $G ( { \pmb q } , { \pmb p } ) : = { \ b q } _ { i }$ , then

$$
\frac { d } { d t } q _ { i } = \{ q _ { i } , H \} ( \pmb { q } , \pmb { p } ) = \frac { \partial } { \partial p _ { i } } H ( \pmb { q } , \pmb { p } ) ,
$$

as we would expect.

The Poisson bracket is a bilinear, antisymmetric operation.3 This means that, for functions $F , G , H : \mathbb { R } ^ { 2 d }  \mathbb { R }$ , and scalars $\alpha , \beta$

$$
\{ F , \alpha G + \beta H \} = \alpha \{ F , G \} + \beta \{ F , H \} ,
$$

and

$$
\{ F , G \} = - \{ G , F \} .
$$

Note that the latter identity implies linearity in the first argument as well. Moreover, $\{ F , F \} = - \{ F , F \}$ , hence $\{ F , F \} = 0$ , i.e. the Poisson bracket of a function with itself vanishes identically.

We have already seen that the Hamiltonian (or energy) $H$ of a Hamiltonian system is a first integral. Using the Poisson bracket notation, this statement reduces to the observation $\{ H , H \} = 0$ .

Example 1 The Kepler problem in $\mathbb { R } ^ { 3 }$ possesses an interesting and nontrivial integral invariant structure. First, the energy,

$$
H = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { p } - \frac { 1 } { | | \pmb { q } | | } = \frac { 1 } { 2 } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } + p _ { 3 } ^ { 2 } ) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } } } ,
$$

is a constant of motion. Moreover, one easily verifies that the components of the angular momentum vector,

$$
\pmb { m } = \pmb { q } \times \pmb { p } = \left[ \begin{array} { c } { m _ { 1 } } \\ { m _ { 2 } } \\ { m _ { 3 } } \end{array} \right]
$$

are conserved quantities. For example

$$
\begin{array} { l } { { \displaystyle \{ m _ { 1 } , H \} = \{ q _ { 2 } p _ { 3 } - q _ { 3 } p _ { 2 } , H \} } } \\ { { \displaystyle \quad = p _ { 3 } \frac { \partial H } { \partial p _ { 2 } } - p _ { 2 } \frac { \partial H } { \partial p _ { 3 } } + q _ { 3 } \frac { \partial H } { \partial q _ { 2 } } - q _ { 2 } \frac { \partial H } { \partial q _ { 3 } } } } \\ { { \displaystyle \quad = p _ { 3 } p _ { 2 } - p _ { 2 } p _ { 3 } - q _ { 3 } q _ { 2 } / \| { \bf q } \| ^ { 3 } + q _ { 2 } q _ { 3 } / \| { \bf q } \| ^ { 3 } } } \\ { { \displaystyle \quad = 0 . } } \end{array}
$$

Since, for any vectors a and $^ { b }$ , we have

$$
a \cdot ( a \times b ) = 0 , \qquad b \cdot ( a \times b ) = 0 ,
$$

it follows that $\pmb q$ and $p$ lie permanently in the plane perpendicular to $\pmb { m }$ (see Fig. 3.3). For simplicity, it is typically assumed that this plane of motion is oriented such that $\pmb { m }$ points in the $q _ { 3 }$ direction, in which case we have $p _ { 3 } \equiv 0$ , implying $q _ { 3 }$ is constant along trajectories, and the more traditional planar Kepler problem results with Hamiltonian reduced to

$$
H = \frac { 1 } { 2 } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } .
$$

This is a system with two degrees of freedom and two first integrals; energy $H$ and the third component of the angular momentum vector $\pmb { m }$ . Hence any bounded motion is restricted to a two-dimensional surface which is diffeomorph to a torus.

Furthermore, the special form of the Kepler force field creates an additional vector, namely the Runge–Lenz vector

$$
\pmb { e } = \pmb { p } \times \pmb { m } - \frac { \pmb { q } } { | | \pmb { q } | | } ,
$$

which is constant along solution curves (see problem 2 in the Exercises). This invariance implies that the bounded trajectories of the Kepler problem are closed in the $\left( q _ { 1 } , q _ { 2 } \right)$ -plane [7]. ✷

![](images/33f52facacef0259643dd9d50ca5662d39a0faddcf16c1f23b96c9380329d3b2.jpg)  
Figure 3.3 Significance of the angular momentum in the Kepler problem: orbits lie in the plane perpendicular to $m = \pmb { q } \times \pmb { p }$ .

Angular momentum $m = \pmb { q } \times \pmb { p }$ is a first integral for any particle moving under a central force field (see problem 2 in the Exercises), i.e. with Hamiltonian of the form

$$
H = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { p } + \varphi ( | | \pmb { q } | | ) ,
$$

thus all such systems have planar motion.

In general, each first integral reduces the number of degrees of freedom by one as an intersection of invariant manifolds. The Kepler problem is an example of an integrable Hamiltonian system, meaning, intuitively, that the system possesses an independent first integral $G _ { i }$ for each of its degrees of freedom. The solutions of an integrable system of $d$ degrees of freedom are then restricted to $d \cdot$ -dimensional level sets

$$
\mathcal { M } _ { \mathrm { c } } = \{ ( \boldsymbol { q } , \boldsymbol { p } ) \in \mathbb { R } ^ { 2 d } : G _ { i } ( \boldsymbol { q } , \boldsymbol { p } ) = c _ { i } , i = 1 , \ldots , d \} .
$$

If these level sets are compact sets (i.e. closed and bounded), then they can be viewed as $d \cdot$ -dimensional tori, i.e. the level sets can be transformed by a smooth (and smoothly invertible) mapping to a set of the form $T = S ^ { 1 } \times S ^ { 1 } \times S ^ { 1 } . . . \times S ^ { 1 }$ ( $d$ times), where $S ^ { 1 }$ is the circle.4 Upon introducing angle variables $\phi$ to describe the tori and identifying each torus by its action ${ \textbf { \textsf { l } } } \in \mathbb { R } ^ { d }$ [7, 8], the integrable system can be transformed to the canonical system

$$
\dot { \mathbf { l } } = \mathbf { 0 } , \qquad \dot { \pmb { \phi } } = \nabla _ { \mathrm { l } } S ( \mathbf { l } ) ,
$$

with Hamiltonian $S ( \boldsymbol { \mathsf { I } } )$ . Thus integrable systems have regular quasi-periodic solutions with frequency $\pmb { \omega } = \nabla _ { 1 } S ( \pmb { \mathsf { I } } )$ .

Most systems do not possess a full complement of first integrals. The few first integrals that are typically present can be of substantial physical and practical importance. In complex nonlinear systems, they sometimes provide a simple way of distinguishing plausible trajectories from nonphysical ones or of assessing the quality of an approximation.

Example 2 The equations of motion (3.19)-(3.20)of $N$ particles interacting through a distance-dependent pair-potential $\varphi ( r )$ admit total linear momentum $\pmb { p } _ { \mathrm { t o t } } = \sum _ { i } \pmb { p } _ { i }$ and total angular momentum $\begin{array} { r } { m _ { \mathrm { t o t } } = \sum _ { i } { q _ { i } } \times p _ { i } } \end{array}$ as first integrals. For example:

$$
{ \frac { d } { d t } } { \pmb { p } } _ { t o t } = \sum _ { i } { \frac { d } { d t } } { \pmb { p } } _ { i } = \sum _ { i } \sum _ { i \neq j } - { \frac { \varphi ^ { \prime } ( r _ { i j } ) } { r _ { i j } } } ( { \pmb { q } } _ { i } - { \pmb { q } } _ { j } ) = { \bf 0 } ,
$$

since $r _ { i j } = r _ { j i }$

In molecular applications, periodic boundary conditions are often introduced as a modeling device. In this case, the total linear momentum remains a conserved quantity, but the total angular momentum is sacrificed.

# 3.4 The flow map and variational equations

Each Hamiltonian system gives rise to a family of flow maps parameterized by time $t$ . Contrary to the previously used notation $\pmb { \phi } _ { t }$ , we denote the flow map from now on by $\phi _ { t , H }$ to indicate its dependence on the Hamiltonian $H$ . As we have mentioned in the previous chapter, the family of flow maps is closed under the composition operation, i.e. for any $t = \tau _ { 1 } , \ t = \tau _ { 2 }$

$$
\begin{array} { r } { \pmb { \phi } _ { \tau _ { 1 } , H } \circ \pmb { \phi } _ { \tau _ { 2 } , H } = \pmb { \phi } _ { \tau _ { 2 } , H } \circ \pmb { \phi } _ { \tau _ { 1 } , H } = \pmb { \phi } _ { \tau _ { 1 } + \tau _ { 2 } , H } . } \end{array}
$$

The flow map $\pmb { \phi } _ { 0 , H }$ at $t = 0$ is the identity map (abbreviated id). Every flow map evidently has an inverse in the family, since

$$
\pmb { \phi } _ { - t , H } \circ \pmb { \phi } _ { t , H } = \pmb { \phi } _ { 0 , H } = \mathbf { i d } .
$$

4Some additional technical assumptions have to be made [7, 8].

The one-parameter family of time $t$ flow maps of a Hamiltonian system thus defines a commutative group.

Example 3 Consider a particle of mass $m$ that is moving in $\mathbb { R } ^ { 3 }$ without any force acting on it. The corresponding Hamiltonian is the kinetic energy of the particle and the flow map is given by

$$
\pmb { \phi } _ { t , H } ( \pmb q , \pmb { p } ) = \left[ \begin{array} { c } { \pmb { q } + \frac { t } { m } \pmb { p } } \\ { \pmb { p } } \end{array} \right] .
$$

Example 4 For the linear Hamiltonian system (3.8),the flow map $\pmb { \phi } _ { t , H }$ is given by a matrix exponential

$$
\pmb { \phi } _ { t , H } ( z ) = \mathrm { e x p } ( t J L ) z .
$$

Let us consider in detail the example of the harmonic oscillator

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } q = p } , } \\ { { \displaystyle { \frac { d } { d t } } p = - \omega ^ { 2 } q . } } \end{array}
$$

The first step is to introduce new coordinates $\hat { z } : = { S } ^ { - 1 } z$ , $z = ( q , p ) ^ { T }$ , with

$$
\pmb { S } = \left[ \begin{array} { c c } { 1 / \sqrt { \omega } } & { 0 } \\ { 0 } & { \sqrt { \omega } } \end{array} \right] .
$$

In these new coordinates the matrix

$$
\begin{array} { r } { J L = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] } \end{array}
$$

gets transformed to

$$
\pmb { S } ^ { - 1 } \pmb { J } \pmb { L } \pmb { S } = \left[ \begin{array} { c c } { 0 } & { \omega } \\ { - \omega } & { 0 } \end{array} \right] .
$$

The corresponding transformed linear system

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \hat { q } = \omega \hat { p } , } \\ { \displaystyle \frac { d } { d t } \hat { p } = - \omega \hat { q } , } \end{array}
$$

$\hat { z } = ( \hat { q } , \hat { p } ) ^ { T }$ , generates the flow map

$$
\begin{array} { r l } & { \pmb { \hat { \phi } } _ { t , H } = \exp ( t \pmb { \cal S } ^ { - 1 } J L \pmb { \cal S } ) , } \\ & { \quad \quad = \left[ \begin{array} { l l } { \cos \omega t } & { \sin \omega t } \\ { - \sin \omega t } & { \cos \omega t } \end{array} \right] . } \end{array}
$$

We obtain the flow map $\pmb { \phi } _ { t , H }$ by transforming $\hat { \pmb { \phi } } _ { t , H }$ back to the variable $z = S \hat { z }$ . Thus

$$
\begin{array} { r l } & { \boldsymbol { \phi } _ { t , H } ( z ) = \exp ( t J L ) z } \\ & { \qquad = \boldsymbol { S } \boldsymbol { \hat { \phi } } _ { t , H } \boldsymbol { S } ^ { - 1 } \boldsymbol { z } } \\ & { \qquad = \left[ \begin{array} { c c } { 1 / \sqrt { \omega } } & { 0 } \\ { 0 } & { \sqrt { \omega } } \end{array} \right] \left[ \begin{array} { c c } { \cos \omega t } & { \sin \omega t } \\ { - \sin \omega t } & { \cos \omega t } \end{array} \right] \left[ \begin{array} { c c } { \sqrt { \omega } } & { 0 } \\ { 0 } & { 1 / \sqrt { \omega } } \end{array} \right] z } \\ & { \qquad = \left[ \begin{array} { c c } { \cos \omega t } & { \omega ^ { - 1 } \sin \omega t } \\ { \omega \sin \omega t } & { \sin \omega t } \end{array} \right] z . } \end{array}
$$

Hence the flow of the harmonic oscillator is described by a product of three matrices: a scaling, a rotation, and the inverse scaling.

Hamiltonian systems with bounded smooth Hamiltonian function $H$ admit smooth flow maps. The inverse map $\pmb { \phi } _ { t , H } ^ { - 1 } \equiv \pmb { \phi } _ { - t , H }$ is also smooth. A map which is smooth, invertible, and whose inverse map is also smooth is called a diffeomorphism.

Even when the potential energy is not smooth (for example, when it has singular points) we can still often define a flow map subject to a suitable domain restriction. For example, for an $N .$ -body system subject to a pair potential $\varphi$ with a singularity at $r = 0$ , ultimately repulsive at short range $\begin{array} { r l } { ( \operatorname* { l i m } _ { r \to 0 + } \varphi ( r ) = } & { { } } \end{array}$ $+ \infty )$ , we can define a global flow map on the complement of the singular set $\{ ( { \pmb q } _ { 1 } , { \pmb q } _ { 2 } , \dots , { \pmb q } _ { N } ) | { \pmb q } _ { i } = { \pmb q } _ { j }$ , some $i , j , i \neq j \}$ .

In general, the flow map cannot be written down explicitly but can only be approximated numerically. We will take up this task in the following chapters.

The flow map notation allows us to emphasize solution properties that are shared by bundles of trajectories. For example, instead of considering a single initial point $z ^ { 0 }$ , we can look at a neighborhood $\mathcal { U } \subset \mathbb { R } ^ { 2 d }$ of initial points near the given $z ^ { 0 }$ and can ask how this whole set of initial conditions is transported by the flow map, i.e. we can discuss the transformed sets

$$
\begin{array} { r l } & { \mathcal { U } _ { t } : = \pmb { \phi } _ { t , H } ( \mathcal { U } ) , } \\ & { \quad \quad : = \{ z \in \mathbb { R } ^ { 2 d } : z = \pmb { \phi } _ { t , H } ( \hat { z } ) \ \mathrm { w i t h } \ \hat { z } \in \mathcal { U } \} , } \end{array}
$$

$t > 0$ . This point of view will allow us to better understand some of the qualitative properties of Hamiltonian equations of motion.

A first step in this direction is to investigate the solution behavior of a system near a given trajectory $z ( t ; z ^ { 0 } )$ via linearization of the system along $z ( t ; z ^ { 0 } )$ . Let $\boldsymbol { z } ( t ; \bar { \boldsymbol { z } } ^ { 0 } )$ denote another solution with an almost identical initial condition, i.e. $\bar { z } ^ { 0 } \approx z ^ { 0 }$ . Then it is often of interest to know how this small difference

$$
\delta z ^ { 0 } : = \bar { z } ^ { 0 } - z ^ { 0 }
$$

in the initial conditions is propagated in time. Of course, the answer is obtained by simply comparing the two solution curves, i.e.

$$
\delta z ( t ) : = z ( t ; \bar { z } ^ { 0 } ) - z ( t ; z ^ { 0 } ) .
$$

However, if only $z ( t ; z ^ { 0 } )$ is explicitly known, then an approximation for $\delta z ( t )$ can be obtained via Taylor series expansion of the flow map in $\delta z ^ { 0 }$

$$
\begin{array} { l } { \displaystyle \delta z ( t ) = \pmb { \phi } _ { t , H } ( \bar { z } ^ { 0 } ) - \pmb { \phi } _ { t , H } ( z ^ { 0 } ) } \\ { \displaystyle = \pmb { \phi } _ { t , H } ( z ^ { 0 } + \delta z ^ { 0 } ) - \pmb { \phi } _ { t , H } ( z ^ { 0 } ) } \\ { \displaystyle \approx \frac { \partial } { \partial z } \pmb { \phi } _ { t , H } ( z ^ { 0 } ) \delta z ^ { 0 } . } \end{array}
$$

This motivates the definition of the time-dependent vector

$$
\pmb { \xi } ( t ) = \frac { \partial } { \partial z } \pmb { \phi } _ { t , H } ( z ^ { 0 } ) \delta z ^ { 0 } .
$$

We can differentiate with respect to time making use of

$$
\frac { d } { d t } z ( t ) = \frac { \partial } { \partial t } \pmb { \phi } _ { t , H } ( z ( 0 ) ) = J \nabla _ { z } H ( \pmb { \phi } _ { t , H } ( z ( 0 ) ) ) = J \nabla _ { z } H ( z ( t ) )
$$

to obtain

$$
\begin{array} { r l } & { \frac { d } { d t } \pmb { \xi } ( t ) = \frac { \partial } { \partial t } \frac { \partial } { \partial z } \phi _ { t , H } ( z ^ { 0 } ) \delta z ^ { 0 } } \\ & { \qquad = \frac { \partial } { \partial z } \left[ \frac { \partial } { \partial t } \phi _ { t , H } ( z ^ { 0 } ) \right] \delta z ^ { 0 } } \\ & { \qquad = \frac { \partial } { \partial z } \left[ J \nabla _ { z } H ( \phi _ { t , H } ( z ^ { 0 } ) ) \right] \delta z ^ { 0 } } \\ & { \qquad = J H _ { z z } ( z ( t ) ) \left[ \frac { \partial } { \partial z } \phi _ { t , H } ( z ^ { 0 } ) \delta z ^ { 0 } \right] } \\ & { \qquad = J H _ { z z } ( z ( t ) ) \xi ( t ) . } \end{array}
$$

Hence we have derived a linear time-dependent differential equation in $\pmb { \xi } \in \mathbb { R } ^ { 2 d }$ , called the variational equations along a solution $\boldsymbol { z } ( t ) = \boldsymbol { z } ( t ; \boldsymbol { z } ^ { 0 } )$ :

VARIATIONAL EQUATIONS

$$
\frac { d } { d t } \pmb { \xi } = J H _ { z z } ( z ( t ) ) \pmb { \xi } .
$$

Note that the quality of the approximation $\delta z ( t ) \approx \pmb { \xi } ( t )$ depends on the smallness of $\delta z ^ { 0 }$ and will only be valid, in general, over relatively short time intervals. However, the variational equations are important in their own right as we will see in the following section.

In the particular situation that $z ( t ; z ^ { 0 } )$ is an equilibrium solution $z ( t ; z ^ { 0 } ) \equiv$ $\bar { z } = z ^ { 0 }$ , the variational equations (3.23) reduce to the time-independent linear system

$$
\frac { d } { d t } \pmb { \xi } = J H _ { z z } ( \bar { z } ) \pmb { \xi } .
$$

For the Newtonian mechanical system (3.2)–(3.3) with equilibrium $\bar { z } = ( \bar { \pmb q } , { \bf 0 } )$ , the variational equations about $z = \bar { z }$ are

$$
\frac { d } { d t } \pmb { \xi } = \left[ \begin{array} { c c } { \ \mathbf { 0 } } & { \ M ^ { - 1 } } \\ { - V _ { q q } ( \bar { q } ) } & { \ \mathbf { 0 } } \end{array} \right] \pmb { \xi } .
$$

The study of this linear system often allows one to understand the behavior of solutions of the nonlinear system in the vicinity of the equilibrium point. For example, if the matrix $V _ { q q } ( \bar { q } )$ is positive definite, the equilibrium point $\bar { \pmb q }$ will be stable for both the linear system and the nonlinear system.5

Let us abbreviate the Jacobian of the flow map $\Phi _ { t , H }$ by $\pmb { F } ( t ) \in \mathbb { R } ^ { 2 d \times 2 d }$ , i.e.

$$
\pmb { F } ( t ) = \frac { \partial } { \partial z } \pmb { \phi } _ { t , H } ( z ^ { 0 } ) .
$$

Then formula (3.22) can be written as ${ \pmb \xi } ( t ) = { \pmb F } ( t ) \delta z ^ { 0 }$ , which holds for any vector $\delta z ^ { 0 }$ . It is then easy to verify that the matrix $\pmb { F } ( t )$ itself is the solution of the matrix-valued variational equation

$$
\frac { d } { d t } \pmb { F } = J H _ { z z } ( z ( t ) ) \pmb { F } ,
$$

with initial condition $F ( 0 ) = I _ { 2 d }$

# 3.5 Symplectic maps and Hamiltonian flow maps

This and following sections are devoted to the definition of symplecticness of a smooth mapping $\pmb { \psi } : \mathbb { R } ^ { 2 d }  \mathbb { R } ^ { 2 d }$ and its implications for the solution behavior of canonical Hamiltonian systems. The presentation in this section is divided into three parts. We start with an algebraic definition of symplecticness and show that the flow map $\pmb { \phi } _ { \tau , H }$ of a canonical Hamiltonian system is symplectic. In the second part, we discuss the implications on the solution behavior for singledegree-of-freedom systems. Finally, in the third part, we give another derivation of symplecticness, making clear its geometric interpretation in arbitrary finite dimensions.

A smooth map $\pmb { \psi }$ on the phase space $\mathbb { R } ^ { 2 d }$ is called a symplectic map with respect to the (constant and invertible) structure matrix $J$ if its Jacobian $\pmb { \psi } _ { z } ( z )$ satisfies:

$$
\begin{array} { r } { [ \pmb { \psi } _ { z } ( z ) ] ^ { T } J ^ { - 1 } \pmb { \psi } _ { z } ( z ) = J ^ { - 1 } , } \end{array}
$$

for all $z$ in the domain of definition of $\pmb { \psi }$ . In case $\jmath$ in (3.25), given by (3.6), one sees the term “canonical map” used as a synonym for the term “symplectic map.”

For a linear transformation $\pmb { \psi } ( z ) ~ = ~ \pmb { B z }$ , the condition of symplecticness reduces to $B ^ { T } J ^ { - 1 } B = J ^ { - 1 }$ and $B$ is referred to as a symplectic matrix.

Example 5 Consider the Hénon map $\pmb { \psi } _ { a , b } : \mathbb { R } ^ { 2 }  \mathbb { R } ^ { 2 }$ defined by

$$
\pmb { \psi } _ { a , b } ( q , p ) : = \left[ \underset { 1 + b q + a p ^ { 2 } } { p } \right] ,
$$

a, $b \neq 0$ parameters. To check that this map is canonical, we compute the Jacobian matrix

$$
\frac { \partial } { \partial z } \pmb { \psi } _ { a , b } ( z ) = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { b } & { 2 a p } \end{array} \right] ,
$$

of $\psi _ { a , b }$ . Then a straightforward calculation yields

$$
\left[ \frac { \partial } { \partial z } \psi _ { a , b } \right] ^ { T } J ^ { - 1 } \frac { \partial } { \partial z } \psi _ { a , b } = \left[ \begin{array} { c c } { 0 } & { b } \\ { 1 } & { 2 a p } \end{array} \right] \left[ \begin{array} { c c } { 0 } & { - 1 } \\ { 1 } & { 0 } \end{array} \right] \left[ \begin{array} { c c } { 0 } & { 1 } \\ { b } & { 2 a p } \end{array} \right] = - b J ^ { - 1 } .
$$

(Here $\jmath$ is the $2 \times 2$ canonical symplectic structure matrix.) Hence the H´enon map is symplectic for $b = - 1$ . ✷

Example6 Often，a non-linear change of position in coordinates from $\pmb q$ to $\hat { \pmb q }$ is prescribed by

$$
{ \hat { \pmb q } } = { \pmb h } ( { \pmb q } ) ,
$$

where $\pmb { \mathscr { h } } : \mathcal { U } \subset \mathbb { R } ^ { d }  \mathbb { R } ^ { d }$ is a diffeomorphism (i.e. a smooth map with a smooth inverse).

For example, consider the transformation

$$
\begin{array} { r } { q _ { 1 } = r \sin \theta , } \\ { q _ { 2 } = r \cos \theta } \end{array}
$$

from polar $( r , \theta )$ coordinates to Cartesian $\left( q _ { 1 } , q _ { 2 } \right)$ coordinates.