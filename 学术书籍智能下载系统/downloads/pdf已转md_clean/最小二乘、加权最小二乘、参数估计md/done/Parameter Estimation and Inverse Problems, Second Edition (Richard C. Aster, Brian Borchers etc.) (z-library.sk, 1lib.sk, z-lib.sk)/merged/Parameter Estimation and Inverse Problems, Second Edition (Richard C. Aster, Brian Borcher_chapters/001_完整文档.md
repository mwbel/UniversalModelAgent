<!-- source: Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borchers etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf -->

<!-- pdf_type: normal; pages: 377; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
# Parameter Estimation and Inverse Problems

Second Editon

# Richard C. Aster Brian Borchers Clifford H. Thurber

ResidualNorm||G(m)-d|l

# PARAMETER ESTIMATION AND INVERSE PROBLEMS

Second Edition

# PARAMETER ESTIMATION AND INVERSE PROBLEMS

Second Edition

RICHARD C. ASTER

BRIAN BORCHERS

CLIFFORD H. THURBER

Academic Press is an imprint of Elsevier 225Wyman Street,Waltham,MA O2451,USA The Boulevard,Langford Lane,Kidlington,Oxford, OX5 1GB,UK $\circled{ c}$ 2013 Elsevier Inc.All rights reserved.

No partof this publication may be reproduced or transmited inany form or byany means,electronic or mechanical, including photocopying,recording,oranyinformation storage and retrieval system,without permision in writing from thePublisher.Details onhow to seek permission,further information about the Publisher's permissions policies and our arrangements with organizationssuch as the Copyright Clearance Center and the Copyright Licensing Agency,can be found at our website: www.elsevier.com/permissions.

This book and the individualcontributions contained in it are protected under copyrightbythe Publisher (other than as may be noted herein).

# Notices

Knowledge and best practice in this field are constantly changing. As new research and experience broaden our understanding,changes in research methods,professional practices,or medical treatment may become necessary.

Practitioners and researchers must always rely on their own experience and knowledge in evaluating and using any information,methods,compounds,or experiments described herein.In using such information or methods they should be mindful of their own safety and the safety of others,including parties for whom they have a professional responsibility.

Tothe fullest extentofthe law,neitherthe Publisher nor the authors,contributors,oreditors,assumeany liability for anyinjuryand/or damage topersons or propertyasamatterof products liability,negligence orotherwise,orfromany use or operation of any methods,products,instructions,or ideas contained in the material herein.

# Library of Congress Cataloging-in-Publication Data

Aster, Richard C.

Parameter estimation and inverse problems.-2nd ed./Richard C.Aster, Clifford H. Thurber.

Includes bibliographical references and index.

ISBN 978-0-12-385048-5 (hardback)

1.Parameter estimation.2.Inverse problems (Differential equations）3.Inversion (Geophysics) 4.Mathematical models.I. Thurber, Clifford H.II. Title.   
QA276.8.A88 2012   
515'.357-dc23

2011032004

# British Library Cataloguing-in-Publication Data

A catalogue record for this book is available from the British Library.

For information on all Academic Press publications visit our website at www.elsevierdirect.com

Typeset by: diacriTech,India

Printed in the United States of America 1213141510987654321

# CONTENTS

Preface ix

# 1. Introduction

# 1

.1. Classification of Parameter Estimation and Inverse Problems 1

1.2.Examples of Parameter Estimation Problems 4

1.3.Examples of Inverse Problems 8

1.4.Discretizing Integral Equations 14

1.5.Why Inverse Problems Are Dificult 19

1.6.Exercises 22

1.7.Notes and Further Reading 23

2. Linear Regression 25

2.1. Introduction to Linear Regression 25

2.2.Statistical Aspects of Least Squares 27

2.3．An Alternative View of the $9 5 \%$ Confidence Ellipsoid 37

2.4. Unknown Measurement Standard Deviations 38

2.5. $L _ { 1 }$ Regression 42

2.6.Monte Carlo Error Propagation 47

2.7.Exercises 49

2.8.Notes and Further Reading 52

# . Rank Deficiency and ll-Conditioning 55

3.1.The SVD and the Generalized Inverse 55

3.2. Covariance and Resolution of the Generalized Inverse Solution 62

3.3. Instability of the Generalized Inverse Solution 64

3.4.A Rank Deficient Tomography Problem 68

3.5.Discrete Il-Posed Problems 74

3.7.Notes and Further Reading 91

# 4. Tikhonov Regularization 93

4.1．Selecting Good Solutions to Il-Posed Problems 93

4.2.SVD Implementation of Tikhonov Regularization 95

4.3.Resolution,Bias,and Uncertainty in the Tikhonov Solution 99

4.4.Higher-Order Tikhonov Regularization 103

4.5.Resolution in Higher-Order Tikhonov Regularization 111

4.6.The TGSVD Method 113

#

4.7.Generalized Cross-Validation 115   
4.8.Error Bounds 119   
4.9. Exercises 124   
4.10. Notes and Further Reading 127

# 5．Discretizing Problems Using Basis Functions 129

5.1．Discretization by Expansion of the Model 129   
5.2. Using Representers as Basis Functions 133   
5.3. The Method of Backus and Gilbert 134   
5.4. Exercises 139   
5.5. Notes and Further Reading 140

# 6. Iterative Methods 141

6.1．Introduction 141   
6.2. Iterative Methods for Tomography Problems 142   
6.3. The Conjugate Gradient Method 150   
6.4. The CGLS Method 155   
6.5. Resolution Analysis for Iterative Methods 160   
6.6. Exercises 166   
6.7. Notes and Further Reading 168

# 7． Additional Regularization Techniques 169

7.1．Using Bounds as Constraints 169   
7.2.Sparsity Regularization 174

7.3.Using IRLS to Solve $L _ { 1 }$ Regularized Problems 176

7.4.Total Variation 186

7.5.Exercises 191

7.6.Notes and Further Reading 192

# 8.Fourier Techniques 193

8.1. Linear Systems in the Time and Frequency Domains 193   
8.2. Linear Systems in Discrete Time 199   
8.3. Water Level Regularization 204   
8.4. Tikhonov Regularization in the Frequency Domain 208   
8.5. Exercises 214   
8.6. Notes and Further Reading 215

# 9. Nonlinear Regression 217

9.1. Introduction to Nonlinear Regression 217 9.2.Newton's Method for Solving Nonlinear Equations 217 9.3.The Gauss-Newton and Levenberg-Marquardt Methods for Solving Nonlinear Least Squares Problems 220

9.4.Statistical Aspects of Nonlinear Least Squares 224   
9.5. Implementation Issues 228   
9.6. Exercises 234   
9.7.Notes and Further Reading 237

# 10. Nonlinear Inverse Problems

# 239

10.1.Regularizing Nonlinear Least Squares Problems 239   
10.2.Occam's Inversion 244   
10.3.Model Resolution in Nonlinear Inverse Problems 248   
10.4. Exercises 251   
10.5. Notes and Further Reading 252

# 11. Bayesian Methods 253

11.1.Review of the Classical Approach 253   
11.2.The Bayesian Approach 255   
11.3.The Multivariate Normal Case 260   
11.4.The Markov Chain Monte Carlo Method 269   
11.5.Analyzing MCMC Output 273   
11.6. Exercises 278   
11.7. Notes and Further Reading 280

# 12. Epilogue

281

# Appendix A. Review of Linear Algebra 283

#

A.1. Systems of Linear Equations 283

A.2.Matrix and Vector Alqebra 286

A.3.Linear Independence 292

A.4.Subspaces of $R ^ { n }$ 293

A.5.Orthogonality and the Dot Product 298

A.6.Eigenvalues and Eigenvectors 302

A.7.Vector and Matrix Norms 304

A.8.The Condition Number of a Linear System 306

A.9.The QR Factorization 308

A.10. Complex Matrices and Vectors 310

A.11. Linear Algebra in Spaces of Functions 311

A.12. Exercises 312

A.13. Notes and Further Reading 314

# Appendix B. Review of Probability and Statistics 315

B.1．Probability and Random Variables 315   
B.2.Expected Value and Variance 321

B 3．Joint Distributions 323   
B.4. Conditional Probability 326   
B5. The Multivariate Normal Distribution 329   
B.6. The Central Limit Theorem 330   
B.7. Testing for Normality 330   
B.8. Estimating Means and Confidence Intervals 332   
B.9. Hypothesis Tests 334   
B.10. Exercises 336   
B.11. Notes and Further Reading 337

# ppendix C. Review of Vector Calculus 339

C.1.The Gradient, Hessian,and Jacobian 339   
C.2. Taylor's Theorem 341   
C.3. Lagrange Multipliers 341   
C.4. Exercises 344   
C.5.Notes and Further Reading 345

# Appendix D. Glossary of Notation

347

Bibliography Index

349

355

This textbook evolved from a course in geophysical inverse methods taught during the past two decades at New Mexico Tech, first by Rick Aster and, subsequently, jointly between Rick Aster and Brian Borchers.The audience for the course has included a broad range of first- or second-year graduate students (and occasionally advanced undergraduates) from geophysics,hydrology, mathematics,astrophysics,and other disciplines. Cliff Thurber joined this collaboration during the production of the first edition and has taught a similar course at the University of Wisconsin-Madison.

Our principal goal for this text is to promote fundamental understanding of param-eter estimation and inverse problem philosophy and methodology, specifically regarding such key issues as uncertainty, ill-posedness,regularization, bias,and resolution. We emphasize theoretical points with illustrative examples,and MATLAB codes that implement these examples are provided on a companion website. Throughout the examples and exercises,a web icon indicates that there is additional material on the website. Exercises include a mix of applied and theoretical problems.

This book has necessarily had to distill a tremendous body of mathematics and science going back to (at least) Newton and Gauss. We hope that it will continue to find a broad audience of students and professionals interested in the general problem of estimating physical models from data. Because this is an introductory text surveying a very broad field,we have not been able to go into great depth. However, each chapter has a“notes and further reading” section to help guide the reader to further explo-ration of specific topics. Where appropriate, we have also directly referenced research contributions to the field.

Some advanced topics have been deliberately left out of this book because of space limitations and/or because we expect that many readers would not be sufciently familiar with the required mathematics. For example, readers with a strong mathematical background may be surprised that we primarily consider inverse problems with discrete data and discretized models.By doing this we avoid much of the technical complexity of functional analysis. Some advanced applications and topics that we have omitted include inverse scattering problems,seismic difraction tomography, wavelets, data assimilation, simulated annealing,and expectation maximization methods.

We expect that readers of this book will have prior familiarity with calculus, differential equations, linear algebra, probability, and statistics at the undergraduate level. In our experience, many students can benefit from at least a review of these topics,and we commonly spend the first two to three weeks of the course reviewing material from Appendices A, B, and C.

Chapters 1 through 4 form the heart of the book,and should be covered in sequence. Chapters 5 through 8 are mostly independent of each other, but draw heavily on the material in Chapters 1 through 4. As such, they may be covered in any order. Chapters 9 and 1O are independent of Chapters 5 through 8, but are most appropriately covered in sequence. Chapter 11 is independent of the material in Chapters 5 through 10,and provides an introduction to the Bayesian perspective on inverse problems and Bayesian solution methods.

If significant time is allotted for review of linear algebra, vector calculus, probability, and statistics in the appendices,there will probably not be time to cover the entire book in one semester. However, it should be possible for teachers to cover substantial material following Chapter 4.

We especially wish to acknowledge our own professors and mentors in this field, including Kei Aki, Robert Parker, and Peter Shearer. We thank our many collagues, including many students in our courses,who provided sustained encouragement and feedback during the initial drafting and subsequent revision of the book,particularly Kent Anderson, James Beck,Aaron Masters,Elena Resmerita, Charlotte Rowe,Tyson Strand,and Suzan van der Lee. Stuart Anderson, Greg Beroza, Ken Creager, Don Clewett, Ken Dueker, Eliza Michalopoulou, Paul Segall,Anne Sheehan,and Kristy Tiampo deserve special mention for their classroom testing of early and subsequent ver-sions of this text and their helpful suggestions,and Jason Mattax deserves special mention for his thorough proofreading of the second edition text. Robert Nowack, Gary Pavlis, Randall Richardson, and Steve Roecker provided thorough and very helpful reviews during the initial scoping. We offer special thanks to Per Christian Hansen of the Technical University of Denmark for his Regularization Tools, which we highly recommend as an adjunct to this text,and which were an inspiration in writing the first edition. Valu-able feedback that improved the second edition included that provided by Ken Dueker, Anne Sheehan, Pamela Moyer, John Townend, Frederik Tilmann,and Kurt Feigl. Oleg Makhnin cotaught this course with Rick Aster at New Mexico Tech in 2O1O and provided significant contributions, particularly regarding material in Chapter 11, that have been incorporated into this second edition. We also thank the editorial staff at Elsevier over the years,especially Frank Cynar,Kyle Sarofeen, Jennifer Helé,and John Fedor for essential advice and direction. Suzanne Borchers and Susan Delap provided valuable proofreading and graphics expertise. Brian Borchers was a visiting fellow at the Institute for Pure and Applied Mathematics (IPAM) at University of California-Los Angeles,and Rick Aster was partially supported by the New Mexico Tech Geophysical Research Center during preparation of this book. Finally, we express thanks for the boundless support of our families during the many years that it has taken to complete this effort.

# Introduction

# Synopsis

General issues associated with parameter estimation and inverse problems are introduced through the concepts of the forward problem and its inverse solution. Scaling and super-position properties that characterize linear systems are given,and common situations leading to linear and nonlinear mathematical models are discussed. Examples of discrete and continuous linear and nonlinear parameter estimation problems to be revisited in later chapters are shown. Mathematical demonstrations highlighting the key issues of solution existence, uniqueness,and instability are presented and discussed.

# 1.1.CLASSIFICATION OF PARAMETER ESTIMATION AND INVERSE PROBLEMS

Scientists and engineers frequently wish to relate physical parameters characterizing a model, $m$ , to collected observations making up some set of data, d. We will commonly assume that the fundamental physics are adequately understood, so a function, $G$ may be specified relating $m$ and $d$ such that

$$
G ( m ) = d .
$$

In practice, $d$ may be a function of time and/or space, or may be a collection of discrete observations.An important issue is that actual observations always contain some amount of noise. Two common ways that noise may arise are unmodeled influences on instrument readings and numerical round-off. We can thus envision data as generally consisting of noiseless observations from a “perfect’ experiment, $d _ { \mathrm { t r u e } }$ ， plus a noise component $\eta$ ，

$$
\begin{array} { c } { d = G ( m _ { \mathrm { t r u e } } ) + \eta } \\ { = d _ { \mathrm { t r u e } } + \eta , } \end{array}
$$

where $d _ { \mathrm { t r u e } }$ exactly satisfies (1.1） for $m$ equal to the true model, $m _ { \mathrm { t r u e } }$ ， and we assume that the forward modeling is exact. We will see that it is commonly mathematically possible, although practically undesirable, to also fit all or part of $\eta$ by (1.1). It may seem remarkable,but it is often the case that a solution for $m$ that is influenced by even a small noise amplitude $\eta$ can have little or no correspondence to $m _ { \mathrm { t r u e } }$ . Another key issue that may seem astounding at first is that commonly there are an infinite number of models aside from $m _ { \mathrm { t r u e } }$ which fit the perfect data, $d _ { \mathrm { t r u e } }$

When $m$ and $d$ are functions, we typically refer to $G$ as an operator. $G$ will be called a function when $m$ and $d$ are vectors. The operator $G$ can take on many forms. In some cases $G$ is an ordinary differential equation (ODE) or partial differential equation (PDE). In other cases, $G$ is a linear or nonlinear system of algebraic equation.

Note that there is some inconsistency between mathematicians and other scientists in modeling terminology. Applied mathematicians usually refer to $G ( m ) = d$ as the“mathematical model” and to $m$ as the“parameters.’ On the other hand,scientists often refer to $G$ as the“forward operator” and to $m$ as the“model.’ We will adopt the scientific parlance and refer to $m$ as the“the model’ while referring to the equation $G ( m ) = d$ as the“mathematical model."

The forward problem is to find $d$ given m. Computing $G ( m )$ might involve solving an ODE or PDE,evaluating an integral, or applying an algorithm for which there is no explicit analytical formula for $G ( m )$ . Our focus in this text is on the inverse problem of finding m given $d$ .A third problem, not addressed here, is the model identification problem of determining $G$ given examples of $m$ and $d$

In many cases, we will want to determine a finite number of parameters, $n$ ,to define a model. The parameters may define a physical entity directly (e.g.， density, voltage, seismic velocity),or may be coefcients or other constants in a functional relationship that describes a physical process. In this case, we can express the model parameters as an $n$ element vector m. Similarly, if there are a finite number of data points then we can express the data as an m element vector d. (Note that the use of the integer $m$ here for the number of data points is easily distinguishable from the model $m$ by its context.) Such problems are called discrete inverse problems or parameter estimation problems. A general parameter estimation problem can be written as a system of equations

$$
{ \cal G } ( { \bf m } ) = { \bf d } .
$$

In other cases,where the model and data are functions of continuous variables, such as time or space, the associated task of estimating $m$ from $d$ is called a continuous inverse problem. A central theme of this book is that continuous inverse problems can often be well-approximated by discrete inverse problems.

We will generally refer to problems with small numbers of parameters as “parameter estimation problems.’ Problems with a larger number of parameters,and which will often require the application of stabilizing constraints,will be referred to as “inverse problems.”A key aspect of many inverse problems is that they are ill-conditioned in a sense that will be discussed later in this chapter.In both parameter estimation and inverse problems we solve for a set of parameters that characterize a model, and a key point of this text is that the treatment of all such problems can be sufficiently generalized so that the distinction is largely irrelevant. In practice,what is important is the distinction between ill-conditioned and well-conditioned parameter estimation problems.

A type of mathematical model for which many useful results exist is the class of linear systems. Linear systems obey superposition

$$
G ( m _ { 1 } + m _ { 2 } ) = G ( m _ { 1 } ) + G ( m _ { 2 } )
$$

and scaling

$$
G ( \alpha m ) = \alpha G ( m ) .
$$

In the case of a discrete linear inverse problem, (1.4) can always be written in the form of a linear system of algebraic equations (see Exercise 1.1).

$$
G ( \mathbf { m } ) = \mathbf { G } \mathbf { m } = \mathbf { d } .
$$

In a continuous linear inverse problem, $G$ can often be expressed as a linear integral operator, where (1.1) has the form

$$
\int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) d \xi = d ( x )
$$

and the function $g ( x , \xi )$ is called the kernel. The linearity of (1.8) is easily seen because

$$
\int _ { a } ^ { b } g ( x , \xi ) ( m _ { 1 } ( \xi ) + m _ { 2 } ( \xi ) ) d \xi = \int _ { a } ^ { b } g ( x , \xi ) m _ { 1 } ( \xi ) d \xi + \int _ { a } ^ { b } g ( x , \xi ) m _ { 2 } ( x ) d \xi
$$

and

$$
\int _ { a } ^ { b } g ( x , \xi ) \alpha m ( \xi ) d \xi = \alpha \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) d \xi .
$$

Equations in the form of (1.8),where $m ( x )$ is the unknown,are called Fredholm inte-gral equations of the first kind (IFK). IFKs arise in a surprisingly large number of inverse problems.A key characteristic of these equations is that they have mathematical properties which make it difficult to obtain useful solutions by straightforward methods.

In many cases the kernel in (1.8) can be written to depend explicitly on $x - \xi$ ， producing a convolution equation,

$$
\int _ { - \infty } ^ { \infty } g ( x - \xi ) m ( \xi ) d \xi = d ( x ) .
$$

Here we have written the interval of integration as extending from minus infinity to plus infinity, but other intervals can easily be accommodated by having $g ( x - \xi ) = 0$ outside of the interval of interest. When a forward problem has the form of (1.11),determining $d ( x )$ from $m ( x )$ is called convolution,and the inverse problem of determining $m ( x )$ from $d ( x )$ is called deconvolution.

Another IFK arises in the problem of inverting a Fourier transform

$$
\Phi ( f ) = \int _ { - \infty } ^ { \infty } e ^ { - \imath 2 \pi f x } \phi ( x ) d x
$$

(where $\imath$ is $\sqrt { - 1 } )$ to obtain $\phi ( x )$ . Although there are many tables and analytic methods of obtaining Fourier transforms and their inverses, numerical estimates of $\phi ( x )$ may be of interest, such as where there is no analytic inverse,or where we wish to estimate $\phi ( x )$ from spectral data collected at discrete frequencies.

It is an intriguing question as to why linearity appears in many interesting physical problems.A principal reason is that many such systems are associated with only small departures from equilibrium. One important geophysical example is seismic wave propagation,where the stresses associated with elastic fields are often very small relative to the elastic moduli of the medium. This situation leads to small strains and to a very nearly linear stress-strain relationship. Because of this, seismic wave field problems in many useful circumstances obey superposition and scaling. Other fields such as gravity and magnetism, at field strengths typically encountered in geophysics,also show effectively linear physics.

Because many important inverse problems are linear, and because linear theory is a key component in solving nonlinear problems, Chapters 2 through 8 of this book cover theory and methods for the solution of linear inverse problems.Nonlinear mathematical models arise when the parameters of interest have an inherently nonlinear relationship to the observables. This situation commonly occurs, for example, in electromagnetic feld problems where we wish to relate geometric model parameters such as layer thicknesses to observed field properties. We discuss methods for nonlinear parameter estimation and inverse problems in Chapters 9 and 1O, respectively.

# 1.2.EXAMPLES OF PARAMETER ESTIMATION PROBLEMS

# Example 1.1

A canonical parameter estimation problem is the fiting ofa function, defined by a collection of parameters, to a data set. In cases where this function fitting procedure can be cast as a linear inverse problem, the procedure is referred to as linear regression. An ancient example of linear regression is the characterization of a balistic trajectory. In a basic take on this problem,the data, y,are altitude observations ofa balistic body at a set of times t (Figure 1.1). We wish to solve for a model, $\mathbf { m }$ ,that contains the initial altitude $( m _ { 1 } )$ ,initial vertical velocity $\left( m _ { 2 } \right)$ ,and effective gravitational acceleration $( m _ { 3 } )$ experienced by the body during its trajectory. This and related problems are naturally of practical interest in aeronautics and weaponry, but are also of fundamental geophysical interest, for example, in absolute gravity meters capable of estimating $g$ from the acceleration of a falling object in a vacuum to accuracies on the order of one part in $1 0 ^ { 9 }$ [91].

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/b9c5d8bd2ab33dd6e3b23f56612cc8565cd1964121c50103e342d6e7e7707fe9.jpg)  
Figure 1.1 The parabolic trajectory problem.

The mathematical model is a quadratic function in the $( t , \gamma )$ plane

$$
\gamma ( t ) = m _ { 1 } + m _ { 2 } t - ( 1 / 2 ) m _ { 3 } t ^ { 2 }
$$

that we expect to apply at all times along the trajectory, not just at the times $t _ { i }$ when we happen to have observations. The data will consist of $m$ observations of the height of the body $\gamma _ { i }$ at corresponding times $t _ { i }$ .Assuming that the $t _ { i }$ are measured precisely, and applying (1.13) to each observation, we obtain a system of equations with $m$ rows and $n = 3$ columns that relates the data $\gamma _ { i }$ to the model parameters, $m _ { j }$

$$
\left[ { \begin{array} { c c c } { 1 } & { t _ { 1 } } & { - { \frac { 1 } { 2 } } t _ { 1 } ^ { 2 } } \\ { 1 } & { t _ { 2 } } & { - { \frac { 1 } { 2 } } t _ { 2 } ^ { 2 } } \\ { 1 } & { t _ { 3 } } & { - { \frac { 1 } { 2 } } t _ { 3 } ^ { 2 } } \\ { \vdots } & { \vdots } & { \vdots } \\ { 1 } & { t _ { m } } & { - { \frac { 1 } { 2 } } t _ { m } ^ { 2 } } \end{array} } \right] \left[ { \begin{array} { c } { m _ { 1 } } \\ { m _ { 2 } } \\ { m _ { 3 } } \end{array} } \right] = \left[ { \begin{array} { c } { \gamma _ { 1 } } \\ { \gamma _ { 2 } } \\ { \gamma _ { 3 } } \\ { \vdots } \\ { \gamma _ { m } } \end{array} } \right] .
$$

Although the mathematical model of (1.13) is quadratic,the equations for the three parameters $m _ { i }$ in (1.14) are linear, so solving for $\mathbf { m } = [ m _ { 1 } , m _ { 2 } , m _ { 3 } ] ^ { T }$ is a linear parameter estimation problem.

If there are more data points than model parameters in (1.14) $( m > n )$ ，then the $m$ constraint equations in (1.14) will likely be inconsistent, and it willbe impossible to find a model m that satisfies every equation exactly. The nonexistence of a model exactly satisfying the observations in such a case can be seen geometrically because no parabola will exist that goes through all of the $( t _ { i } , \ \gamma _ { i } )$ points (Exercise 1.2). Such a situation could arise in practice because of noise in the determinations of the $\gamma _ { i }$ ，and/or because the forward model of (1.13) is approximate. For example, we have neglected the physics of atmospheric drag, so a true trajectory will not be exactly parabolic and thus exactly modeled by (1.13).

In elementary linear algebra,where an exact solution is typically expected for a system of linear equations, we might throw up our hands at this point and simply state that no solution exists.However, useful solutions to such systems may be found in practice by solving for model parameters that satisfy the data in an approximate, or "best-fit,’ sense.

A reasonable approach to finding the “best”approximate solution to an inconsistent system of linear equations is to find an m that minimizes some misfit measure,calculated from the differences between the observations and the theoretical predictions of the forward problem, commonly called residuals. A traditional and very widely applied strategy is to find the model that minimizes the 2-norm (Euclidean length) of the residual vector

$$
\| \mathbf { y } - \mathbf { G m } \| _ { 2 } = \sqrt { \sum _ { i = 1 } ^ { m } ( \gamma _ { i } - ( \mathbf { G m } ) _ { i } ) ^ { 2 } } .
$$

However,(1.15) is not the only, or necessarily the best, misfit measure that can be applied to approximate solve systems of equations. An alternative misfit measure that is superior in many situations is the 1-norm

$$
\| \mathbf { y } - \mathbf { G m } \| _ { 1 } = \sum _ { i = 1 } ^ { m } | \gamma _ { i } - ( \mathbf { G m } ) _ { i } | .
$$

We shall see in Chapter 2 that a solution that minimizes (1.16) is less sensitive to data points that are wildly discordant with the mathematical model than one that minimizes (1.15). Solution techniques that are resistant to such data outliers are called robust estimation procedures.

# Example 1.2

A classic nonlinear parameter estimation problem in geophysics is determining the space and time coordinates of an earthquake nucleation, the hypocenter, which is specified by

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/8c0b71d08f42b9d5adb8d4a459081f677272e3bcc3763004ec4a6b73bd72459c.jpg)  
Figure 1.2 The earthquake location problem.

the four-vector

$$
\mathbf { m } = \left[ \begin{array} { l } { \pmb { \xi } } \\ { \tau } \end{array} \right]
$$

where $\pmb { \xi }$ is the three-dimensional earthquake location and the fourth element, $\tau$ ，is the earthquake origin time (Figure 1.2). The hypocenter model we seek best fits a vector of seismic phase arrival times, t, observed at an $m$ -station seismic network.The mathematical model is

$$
G ( \mathbf { m } ) = \mathbf { t }
$$

where $G$ models the physics of seismic wave propagation to map a hypocenter into a vector of predicted seismic arrival times at $m$ stations. $G$ depends on the seismic velocity structure, $\nu ( \mathbf { x } )$ ,which we assume here to be known.

The earthquake location problem is nonlinear even if $\nu ( \mathbf { x } )$ is a constant,c. In this case,all of the ray paths in Figure 1.2 would be straight,and the arrival time of the seismic signal at station $i$ would be

$$
t _ { i } = \frac { \| \mathbf { S } . , i - \pmb { \xi } \| _ { 2 } } { c } + \tau
$$

where the ith column of the matrix S, $\mathbf { S } _ { \cdot , i }$ ，specifies the coordinates for station i. Equation (1.19) is nonlinear with respect to the spatial parameters $\xi _ { i }$ in $\mathbf { m }$ ，and thus the problem cannot be expressed as a linear system of equations.

# 1.3.EXAMPLES OF INVERSE PROBLEMS

# Example 1.3

In vertical seismic profiling,we wish to know the vertical seismic velocity of the material surrounding a borehole. A downward-propagating seismic wavefront is gener-ated at the surface by a source,and seismic waves are sensed by a string of seismometers in the borehole (Figure 1.3).

The arrival times of the seismic wavefront at each instrument,which reflects the seismic velocity for vertically traveling waves as a function of depth,are measured from the recorded seismograms. The problem is nonlinear if it is expressed in terms of seismic velocities.However, we can linearize this problem via a simple change of variables where we parameterize the seismic structure in terms of slowness, $s ( z )$ , the reciprocal of the velocity $\nu ( z )$ . The observed travel time at depth $z$ can then be expressed as the definite integral of the vertical slowness, $s$ ,from the surface to $z$

$$
\begin{array} { c } { { t ( z ) = \displaystyle \int _ { 0 } ^ { z } s ( \xi ) d \xi } } \\ { { \displaystyle = \displaystyle \int _ { 0 } ^ { \infty } s ( \xi ) H ( z - \xi ) d \xi } } \end{array}
$$

where the kernel function $H$ is the Heaviside step function, which is equal to one when its argument is nonnegative and zero when its argument is negative. The explicit dependence of the kernel on $z - \xi$ shows that (1.21) is a convolution.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/5cde3ea303362e43cb8a10c66579d44965b3354b6f5388b6704e6d6752e95194.jpg)  
Figure 1.3 The vertical seismic profiling problem.

In theory, we can solve (1.21) quite easily because, by the fundamental theorem of calculus,

$$
s ( z ) = \frac { d t ( z ) } { d z } .
$$

In practice,simply differentiating the observations to obtain a solution may not be useful. This is because there will generally be noise present in the observed times $t ( z )$ ，and applying (1.22) may result in a solution that includes unphysical values of $s ( z )$ or other unrealistic model features.

# Example 1.4

A further instructive linear inverse problem is the inversion of a vertical gravity anomaly, $d ( x )$ ， observed at some height, $h$ ，to estimate an unknown buried line mass density distribution deviation from a background model, $m ( x ) = \Delta \rho ( x )$ (Figure 1.4). The mathematical model for this problem can be written as an IFK,because the data are a superposition of the vertical gravity contributions from the differential elements comprising the line mass

$$
\begin{array} { l } { d ( x ) = \Gamma { \displaystyle \int _ { - \infty } ^ { \infty } } \frac { h } { \left( ( \xi - x ) ^ { 2 } + h ^ { 2 } \right) ^ { 3 / 2 } } m ( \xi ) d \xi } \\ { = \displaystyle \int _ { - \infty } ^ { \infty } g ( \xi - x ) m ( \xi ) d \xi } \\ { \displaystyle - \infty } \end{array}
$$

where $\Gamma$ is Newton's gravitational constant. Note that the kernel has the form $g ( \xi - x )$ ， and (1.24) is thus a convolution.Because the kernel is a smooth function, $d ( x )$ will be a smoothed and scaled transformation of $m ( x )$ . Conversely, solutions for $m ( x )$ will be a

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/56ad26e6fef6f3f2b7ca31060f2268bcd6ec2f5e182d284ca047197c2960d7a5.jpg)  
Figure 1.4 A linear inverse problem: determine the density deviation of a buried line mass, $\Delta \rho ( x ) ,$ relative to a background model,from gravity anomaly observations $d ( x )$

roughened transformation of $d ( x )$ . For this reason we again need to be wary of possibly severe deleterious effects of noise in the data.

# Example 1.5

Consider a variation on Example 1.4,where the depth of the line density perturbation varies,rather than the density contrast. The gravity anomaly is now atributable to a variation in the burial depth, $m ( x ) = h ( x )$ , of an assumed known density perturbation, $\Delta \rho$ (Figure 1.5). The physics is the same as in Example 1.4,so the data are still given by the superposition of density perturbation contributions to the gravitational anomaly field, but the mathematical model now takes the form

$$
d ( x ) = \Gamma \intop _ { - \infty } ^ { \infty } \frac { m ( \xi ) } { \left( ( \xi - x ) ^ { 2 } + m ^ { 2 } ( \xi ) \right) ^ { 3 / 2 } } \Delta \rho d \xi .
$$

This problem is nonlinear in $m ( x )$ because (1.25) does not follow the superposition and scaling rules (1.5) and (1.6).

Nonlinear inverse problems are generally significantly more difficult to solve than linear ones.In special cases,they may be solvable by coordinate transformations that globally linearize the problem or by other clever special-case methods. In other cases, the problem cannot be globally linearized, so nonlinear optimization techniques must be applied. The essential differences in the treatment of linear and nonlinear problems arise because,as we shall see,all linear problems can be generalized to be the“same” in an important sense, so that a single set of solution methods can be applied to all. In contrast, nonlinear problems tend to be nonlinear in mathematically different ways and either require specific strategies or, more commonly, can by solved by iterative methods that may rely on local linearization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/74043c77762cc5c7a34164d1a852077dd608e391cffedd39554ea3d31935359e.jpg)  
Figure 1.5 A nonlinear inverse problem: determine the depth to a buried line mass density anomaly $h ( x )$ from observed gravity anomaly observations $d ( x )$

# Example 1.6

A classic pedagogical inverse problem is an experiment in which an angular distribution of illumination passes through a thin slit and produces a diffraction pattern, for which the intensity is observed (Figure 1.6; [141]).

The data, $d ( s )$ , are measurements of diffracted light intensity as a function of the outgoing angle $- \pi / 2 \leq s \leq \pi / 2$ . Our goal is to find the intensity of the incident light on the slit, $m ( { \boldsymbol { \theta } } )$ , as a function of the incoming angle $- \pi / 2 \leq \theta \leq \pi / 2$

The forward problem relating $d$ and $m$ can be expressed as the linear mathematical model,

$$
d ( s ) = \int _ { - \pi / 2 } ^ { \pi / 2 } ( \cos ( s ) + \cos ( \theta ) ) ^ { 2 } \left( \frac { \sin ( \pi ( \sin ( s ) + \sin ( \theta ) ) ) } { \pi ( \sin ( s ) + \sin ( \theta ) ) } \right) ^ { 2 } m ( \theta ) d \theta .
$$

# Example 1.7

Consider the problem of recovering the history of groundwater polltion at a source site from later measurements of the contamination at downstream wells to which the contaminant plume has been transported by advection and diffusion (Figure 1.7). This

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/d6eac43d71290eee4cd6d2089d9351c8aaef0d5bb222546e3eb78ce1368dbc72.jpg)  
Figure 1.6 The Shaw diffraction intensity problem (1.26).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/3ca414f24e6e59d83af887102576894939d231c4b1d24d01d80575ca2d38c851.jpg)  
Figure 1.7 The contaminant plume source history reconstruction problem.

“source history reconstruction problem” has been considered by a number of authors [117, 144, 145].

The mathematical model for contaminant transport is an advection-diffusion equation

$$
\begin{array} { c } { { \displaystyle \frac { \partial C } { \partial t } = D \frac { \partial ^ { 2 } C } { \partial x ^ { 2 } } - \nu \frac { \partial C } { \partial x } } } \\ { { \displaystyle C ( 0 , t ) = C _ { i n } ( t ) } } \\ { { \displaystyle C ( x , t )  0 \mathrm { a s } x  \infty } } \end{array}
$$

where $D$ is the diffusion coefficient and $\nu$ is the velocity of groundwater flow. The solution to (1.27) at time $T$ is the convolution

$$
C ( x , \ T ) = \int _ { 0 } ^ { T } C _ { i n } ( t ) f ( x , \ T - t ) d t ,
$$

where $C _ { i n } ( t )$ is the time history of contaminant injection at $x = 0$ ,and the kernel is

$$
f ( x , \ T - t ) = { \frac { x } { 2 { \sqrt { \pi D ( T - t ) ^ { 3 } } } } } \mathrm { e } ^ { - { \frac { [ x - \nu ( T - t ) ] ^ { 2 } } { 4 D ( T - t ) } } } .
$$

# Example 1.8

An important and instructive inverse problem is tomography, from the Greek roots tomos,“to section”or“to cut” (the ancient concept of an atom was that of an irreducible, uncuttable object） and graphein,“to write.’ Tomography is the general technique of determining models that are consistent with path-integrated properties such as attenuation (e.g., X-ray, radar, muon, seismic), travel time (e.g.， electromagnetic, seismic, or acoustic), or source intensity (e.g., positron emisson). Here, we willuse examples from seismic tomography. Although tomography problems originally involved determining models that were two-dimensional slices of three-dimensional objects,the term is now commonly used in situations where the model is two- or three-dimensional. Tomography has many applications in medicine,engineering,acoustics,and Earth science. One important geophysical example is cross-well tomography, where seismic sources are installed in a borehole,and the signals are received by sensors in another borehole. Another example is joint earthquake location/velocity structure inversion carried out on scales ranging from a fraction of a cubic kilometer to global [158, 159, 160].

The physical model for tomography in its most basic form (Figure 1.8) assumes that geometric ray theory (essentially the high-frequency limiting case of the wave equation) is valid, so that wave energy traveling between a source and receiver can be considered to be propagating along infinitesimally narrow ray paths. The density of ray path coverage in a tomographic problem may vary significantly throughout a section or volume, and provide much better constraints on physical properties in densely sampled regions than in sparsely sampled ones.

In seismic tomography, if the slowness at a point $\mathbf { x }$ is $s ( \mathbf { x } )$ ,and the ray path $\ell$ is known, then the travel time for seismic energy transiting along that ray path is given by the line integral along $\ell$

$$
t = \int _ { \ell } s ( \mathbf x ( l ) ) d l .
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/185b6cf4b106a67e4733118cb37b61903956c8f6bd51d81b0868df1a15c1bf90.jpg)  
Figure 1.8 Conceptual depiction of ray path tomography.Sources and receivers may,in general, be either at the edges or within the volume,and ray paths maybe either straight,as depicted,or curved.

Note that (1.3O) is just a higher-dimensional generalization of (1.21), the forward problem for the vertical seismic profiling example. In general, seismic ray paths will be bent due to refraction and/or reflection. In cases where such effects are negligible, ray paths can be usefully approximated as straight lines (e.g.，as depicted in Figure 1.8), and the forward and inverse problems can be cast in a linear form. However, if the ray paths are significantly bent by slowness variations, the resulting inverse problem will be nonlinear.

# 1.4.DISCRETIZING INTEGRAL EQUATIONS

Consider problems of the form

$$
d ( x ) = \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) d \xi .
$$

Here $d ( x )$ is a known function, typically representing observed data. The kernel $g ( x , \xi )$ is considered to be given,and encodes the physics relating an unknown model $m ( x )$ to observed data $d ( s )$ . The interval $[ a , b ]$ may be finite or infinite. The function $d ( x )$ might in theory be known over an entire interval, but in practice we will only have measurements of $d ( x )$ at a finite set of points.

We wish to solve for $m ( x )$ . This type of linear equation is called a Fredholm integral equation of the first kind, or IFK.A surprisingly large number of inverse problems,including all of the examples from the previous section, can be written as IFKs. Unfortunately, IFKs have properties that can make them very challenging to solve.

To obtain useful numerical solutions to IFKs, we will frequently discretize them into forms that are tractably solvable using the methods of linear algebra. We first assume that $d ( x )$ is known at a finite number of points $x _ { 1 }$ ， $x _ { 2 }$ $x _ { m }$ . We can then write the forward problem as

$$
d _ { i } = d ( x _ { i } ) = \int _ { a } ^ { b } g ( x _ { i } , \xi ) m ( \xi ) d \xi \quad i = 1 , 2 , . . . , m
$$

oras

$$
d _ { i } = \int _ { a } ^ { b } g _ { i } ( x ) m ( x ) d x \quad i = 1 , 2 , . . . , m ,
$$

where $g _ { i } ( x ) = g ( x _ { i } , \xi )$ . The functions $g _ { i } ( t )$ are referred to as representers or data kernels.

Here,we will apply a quadrature rule to approximate (1.33） numerically. Note that,although quadrature methods are applied in this section to linear integral equations, they also have utility in the discretization of nonlinear problems. The simplest quadrature approach is the midpoint rule,where we divide the interval $[ a , b ]$ into $n$ subintervals, and pick points $x _ { 1 }$ ， $x _ { 2 }$ ，， $x _ { n }$ in the middle of each interval. The points are given by

$$
x _ { j } = a + \frac { \Delta x } { 2 } + ( j - 1 ) \Delta x
$$

where

$$
\Delta x = { \frac { b - a } { n } } .
$$

The integral (1.33) is then approximated by (Figure 1.9):

$$
d _ { i } = \int _ { a } ^ { b } g _ { i } ( x ) m ( x ) d x \approx \sum _ { j = 1 } ^ { n } g _ { i } ( x _ { j } ) m ( x _ { j } ) \Delta x , \quad i = 1 , 2 , . . . , m .
$$

If we let

$$
\begin{array} { r l } { G _ { i , j } = g _ { i } ( x _ { j } ) \Delta x } & { { } \left( \begin{array} { l } { i = 1 , 2 , \mathrm { ~ . ~ . ~ . ~ , ~ } m } \\ { j = 1 , 2 , \mathrm { ~ . ~ . ~ . ~ , ~ } n } \end{array} \right) } \end{array}
$$

and

$$
m _ { j } = m ( x _ { j } ) \quad j = 1 , 2 , \ldots , n ,
$$

then we obtain a linear system of equations $\mathbf { G m } = \mathbf { d }$

The approach of using the midpoint rule to approximate the integral is known as simple collocation. Of course, there are also more sophisticated quadrature rules for numerically approximating integrals (e.g.， the trapezoidal rule, or Simpson's rule). In each case, we end up with an $m$ by $n$ linear system of equations,but the formulas for evaluating the elements of $\mathbf { G }$ will be different.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/1103cfd502a35cb5c922bc2f08120aad2c342ab7ff81346bcfc9831fb22a8f99.jpg)  
Figure 1.9 Grid for the midpoint rule.

# Example 1.9

Consider vertical seismic profiling (Example 1.3),where we wish to estimate vertical seismic slowness using travel time measurements of downward propagating seismic waves (Figure 1.1O). We discretize the forward problem (1.21) for $m$ travel time data points, $t _ { i }$ ， and $n$ model depths, $z _ { j }$ ， spaced at constant intervals of $\Delta z .$ .This discretization is depicted in Figure 1.10.

The discretized problem has

$$
t _ { i } = \sum _ { j = 1 } ^ { n } H ( \gamma _ { i } - z _ { j } ) s _ { j } \Delta z ,
$$

where $n / m = \Delta \gamma / \Delta z$ is an integer. The rows, $\mathbf { G } _ { i , \cdot }$ , of the matrix each consist of $i \cdot n / m$ elements equal to $\Delta z$ on the left and $n - ( i \cdot n / m )$ zeros on the right. For $n = m$ ， $\mathbf { G }$ is a lower triangular matrix with each nonzero entry equal to $\Delta z$

# Example 1.10

To discretize the Shaw problem (1.26),we apply the method of simple collocation with $m$ and $n$ intervals for the data and model functions,respectively. We additionally define

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/ce98fbfd6d89cd0969f8b93cc685566e09bdfc605470814739ea4107aeb16647.jpg)  
Figure 1.10 Discretization of the vertical seismic profiling problem $( n = 2 m )$ into uniform intervals.

the data and model points at $m$ and $n$ equally spaced respective angles given by

$$
s _ { i } = \frac { ( i - 0 . 5 ) \pi } { m } - \frac { \pi } { 2 } \quad i = 1 , 2 , . . . , m
$$

and

$$
\theta _ { j } = \frac { ( j - 0 . 5 ) \pi } { n } - \frac { \pi } { 2 } \quad j = 1 , 2 , . . . , n .
$$

Correspondingly, discretizing the data and model into $m -$ and $n$ -length vectors

$$
d _ { i } = d ( s _ { i } ) \quad i = 1 , 2 , \ldots , m
$$

and

$$
m _ { j } = m ( \theta _ { j } ) \quad j = 1 , 2 , \ldots , n
$$

leads to a discrete linear system $\mathbf { G m } = \mathbf { d }$ where

$$
G _ { i , j } = ( \cos ( s _ { i } ) + \cos ( \theta _ { j } ) ) ^ { 2 } \left( \frac { \sin ( \pi ( \sin ( s _ { i } ) + \sin ( \theta _ { j } ) ) ) } { \pi ( \sin ( s _ { i } ) + \sin ( \theta _ { j } ) ) } \right) ^ { 2 } \Delta \theta
$$

and

$$
\Delta \theta = { \frac { \pi } { n } } .
$$

# Example 1.11

We discretize the advection-diffusion problem (1.27),assuming that the parameters $D$ and $\nu$ in (1.29) are known. We wish to estimate $C _ { i n } ( t )$ from simultaneous concentration observations at the locations $x _ { i }$ at some later time $T$ .The convolution (1.28) for $C ( x , \ T )$ is discretized as

$$
\mathbf { d } = \mathbf { G } \mathbf { m }
$$

where $\mathbf { d }$ is a vector of sampled concentrations at different well locations, $\mathbf { x }$ ,at time $T$ ， $\mathbf { m }$ is a vector of $C _ { i n }$ values to be estimated,and

$$
\begin{array} { r l } & { G _ { i , j } = f ( x _ { i } , \ T - t _ { j } ) \Delta t } \\ & { \quad \quad = \frac { x _ { i } } { 2 \sqrt { \pi D ( T - t _ { j } ) ^ { 3 } } } \mathrm e ^ { - \frac { [ x _ { i } - \nu ( T - t _ { j } ) ] ^ { 2 } } { 4 D ( T - t _ { j } ) } \Delta t } . } \end{array}
$$

# Example 1.12

A common way of discretizing the model in a tomographic problem is as uniform blocks (Figure 1.11). This approach is essentially applying the midpoint rule to the travel-time forward problem (1.30).

In this parameterization, the elements ofG are just the lengths of the ray paths within corresponding blocks. Consider the example of Figure 1.11,where nine homogeneous blocks with sides of unit length and unknown slowness are crossed by eight ray paths. For straight ray paths,we map the two-dimensional slowness grid to a model vector using a row-by-row indexing convention. The constraint equations in the mathematical model are then

Because there are nine unknown parameters $s _ { i , j }$ in the model, but only eight constraints, the $\mathbf { G }$ matrix is clearly rank deficient. In fact,rank $\mathbf { \tau } ( \mathbf { G } )$ is only seven. In addition, there is clearly redundant information in (1.49), in that the slownes $s _ { 3 , 3 }$ is completely determined by $t _ { 8 }$ ,yet $s _ { 3 , 3 }$ also influences the observations $t 3 , t 6$ ,and $t _ { 7 }$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/6c1c6150b6229057a92d9b4ac2a93129fada3e1f0c274d3d4f20cdd2303ce494.jpg)  
Figure 1.11 Discretization of a tomography problem into uniform blocks. Ray paths correspond to the constraint equations in (1.49).

# 1.5.WHY INVERSE PROBLEMS ARE DIFFICULT

Scientists and engineers need to be concerned with far more than simply finding mathematically acceptable answers to parameter estimation and inverse problems. One reason is that there may be many models that adequately fit the data. It is essential to characterize just what solution has been obtained,how“good’ it is in terms of physical plausibility, its ability to predict the data,and perhaps how consistent it is with other constraints. Essential issues that must be considered include solution existence, solution uniqueness, and instability of the solution process.

1. Existence. There may be no model that exactly fits the data. This can occur in practice because the mathematical model of the system's physics is approximate (or perhaps simply incorrect) or because the data contain noise.

2.Uniqueness If exact solutions do exist, they may not be unique,even for an infi-nite number of exact data points. That is,there may be other solutions besides $m _ { \mathrm { t r u e } }$ that exactly satisfy $G ( m ) = d _ { \mathrm { t r u e } }$ . This situation commonly occurs in potential field problems.A classic example is the external gravitational field from a spherically symmetric mass distribution,which depends only on the total mass,and not on the radial density distribution.

Nonuniqueness is a characteristic of rank deficient discrete linear inverse problems because the matrix $\mathbf { G }$ in this case has a nontrivial null space. In linear inverse problems, models $\mathbf { \Pi } ( \mathbf { m } _ { 0 } )$ that lie in the null space of $\mathbf { G }$ are solutions to $\mathbf { G m } _ { 0 } = \mathbf { 0 }$ .By superposition, any linear combination of these null space models can be added to a particular model that satisfies (1.7) and not change the fit to the data. There are thus an infinite number of mathematically acceptable models in such situations. In practical terms,suppose that there exists a nonzero model $\mathbf { m } _ { 0 }$ that results in an instrument reading of zero. We cannot discriminate this situation from the situation where $\mathbf { m } _ { 0 }$ is truly zero.

An important and thorny issue with problems that have nonunique solutions is that an estimated model may be significantly smoothed or otherwise biased relative to the true situation. Characterizing such bias is essential to interpreting models in terms of their possible correspondence to reality. This issue falls under the general topic of model resolution analysis.

3. Instability. The process of computing an inverse solution can be,and often is, extremely unstable in that a small change in measurement (e.g.,a smal $\eta$ in (1.3)) can lead to an enormous change in the estimated model. Inverse problems where this situation arises are referred to as ill-posed in the case of continuous systems,or illconditioned in the case of discrete linear systems.A key point is that it is commonly possible to stabilize the inversion process by imposing additional constraints that bias the solution, a process that is generally referred to as regularization. Regularization is frequently essential to producing a usable solution to an otherwise intractable ill-posed or ill-conditioned inverse problem.

To examine existence, uniqueness, and instability issues,let us consider some simple mathematical examples using an IFK,

$$
\intop _ { 0 } ^ { 1 } g ( x , \xi ) m ( \xi ) d \xi = \gamma ( x ) .
$$

First,consider the trivial case where the kernel is a constant, such as

$$
g ( x , \xi ) = 1 ,
$$

which produces the integral equation

$$
\int _ { 0 } ^ { 1 } m ( \xi ) d \xi = \gamma ( x ) .
$$

Because the left-hand side of (1.52) is independent of $_ x$ ，this system has no solution unless $\gamma ( \boldsymbol { x } )$ is a constant.Thus, there are an infinite number of mathematically conceivable data sets $\gamma ( \boldsymbol { x } )$ that are not constant and for which no exact solution exists. This is a simple illustration of a solution existence issue.

Where a solution to (1.52) does exist, the solution is nonunique because there are an infinite number of functions that, when integrated over the unit interval, produce the same constant and thus satisfy the IFK exactly. This demonstrates a uniqueness issue.

A more subtle example of nonuniqueness can be seen for

$$
g ( x , \xi ) = x \cdot \sin ( \pi \xi )
$$

in (1.50), so that the IFK becomes

$$
\intop _ { 0 } ^ { 1 } x \cdot \sin ( \pi \xi ) m ( \xi ) d \xi = \gamma ( x ) .
$$

The functions $\sin ( k \pi x )$ for integer values of $k$ are orthogonal in the sense that

$$
\int _ { 0 } ^ { 1 } \sin ( k \pi x ) \sin ( l \pi x ) d x = - \frac { 1 } { 2 } \intop _ { 0 } ^ { 1 } \cos ( \pi ( k + l ) x ) - \cos ( \pi ( k - l ) x ) d x =
$$

$$
- { \frac { 1 } { 2 \pi } } \left( \frac { \sin ( \pi ( k + l ) ) } { k + l } - \frac { \sin ( \pi ( k - l ) ) } { k - l } \right) = 0 \quad ( k \neq \pm l ; k , l \neq 0 ) .
$$

Thus, in (1.54), for models of the form $m ( x ) = \sin ( k \pi x )$ ,for $k = \pm 2$ ， $\pm 3$ ，...，we have

$$
\intop _ { 0 } ^ { 1 } g ( x , \xi ) m ( \xi ) d \xi = \intop _ { 0 } ^ { 1 } g ( x , \xi ) \sin ( k \pi \xi ) d \xi = 0 .
$$

Furthermore, because (1.54) is a linear system, we can add any function of the form

$$
m _ { 0 } ( x ) = \sum _ { k = 2 } ^ { \infty } \alpha _ { k } \ \sin ( k \pi x )
$$

to a solution, $m ( x )$ ,and obtain a new model that fits the data equally well.

$$
\begin{array} { c } { { { \displaystyle \int } _ { x } ^ { 1 } x \cdot \sin ( \pi \xi ) ( m ( \xi ) + m _ { 0 } ( \xi ) ) d \xi = \displaystyle \int _ { 0 } ^ { 1 } x \cdot \sin ( \pi \xi ) m ( \xi ) d \xi + \displaystyle \int _ { 0 } ^ { 1 } s \cdot \sin ( \pi \xi ) m _ { 0 } ( \xi ) d \xi , } } \\ { { { } } } \\ { { { } = \displaystyle \int _ { 0 } ^ { 1 } x \cdot \sin ( \pi \xi ) m ( \xi ) d \xi + 0 . } } \end{array}
$$

There are thus an infinite number of very different solutions that fit the data equally well.

Finally, even if we do not encounter existence or uniqueness issues, instability is a fundamental feature of IFKs. It can be shown that, in the limit as $k$ goes to infinity,

$$
\operatorname* { l i m } _ { k \to \infty } \intop _ { - \infty } ^ { \infty } g ( x , \xi ) \sin { k \pi \xi } d \xi = 0
$$

for all square-integrable functions $g ( x , \xi )$ . This result is known as the Riemann-Lebesgue lemma [134]. Examining (1.59) in more detail, we can better understand why this occurs. The oscillatory sine function is smoothed by integration with the kernel $g ( \xi , x )$ . For sufficiently large values of the sine frequency, $k .$ ， the positive and negative excursions of the sine function will average out to zero. The inverse problem has this situation reversed, so that an inferred model can be extremely sensitive to smal changes in the data. If such small data changes are created by random noise that has nothing to do with the physical system that we are studying, then an inferred model from solving an inverse problem to fit this noise can easily have essentially no correspondence to the true model.

The unstable character of IFK solutions is similar to the situation encountered in solving linear systems of equations where the condition number of the matrix is very large,or equivalently, where the matrix is nearly singular. In both cases,the difficulty lies in the mathematical model itself, and not in the particular algorithm used to solve the problem. Fundamentally, most inverse problems are ill-posed.

# 1.6. EXERCISES

1. Consider a mathematical model of the form $G ( \mathbf { m } ) = \mathbf { d }$ ，where $\mathbf { m }$ is a vector of length $n$ ,and $\mathbf { d }$ is a vector of length m. Suppose that the model obeys the superposition and scaling laws and is thus linear. Show that ${ \cal G } ( { \bf m } )$ can be written in the form

$$
G ( \mathbf { m } ) = \Gamma \mathbf { m }
$$

where $\mathbf { \Gamma } ^ { \Gamma }$ is an $m$ by $n$ matrix. What are the elements of $\Gamma ?$ Hint: Consider the standard basis,and write $\mathbf { m }$ as a linear combination of the vectors in the standard basis.Apply the superposition and scaling laws.Finally, recall the definition of matrix-vector multiplication.

2. Can (1.14) be inconsistent, even with only $m = 3$ data points? How about just $m = 2$ data points? If the system can be inconsistent, give an example. If not, explain why.

3. Consider the borehole vertical seismic profile problem of Examples 1.3 and 1.9 for $n = 1 0 0$ equally spaced seismic sensors located at depths of $z = 0 . 2$ ,0.4，..., $2 0 \mathrm { m }$ ， and for a model m describing $n$ corresponding equal-length seismic slowness values for $0 . 2 \mathrm { m }$ intervals having midpoints at $z - 0 . 1 \mathrm { m }$

a. Calculate the appropriate system matrix, $\mathbf { G }$ ,for discretizing the integral equation (1.21) using the midpoint rule.

b. For a seismic velocity model having a linear depth gradient specified by

$$
\nu = \nu _ { 0 } + k z ,
$$

where the velocity at $z = 0$ is $\nu _ { 0 } = 1 ~ \mathrm { k m / s }$ and the gradient is $k = 4 0 \ \mathrm { m / s }$ per m, calculate the true slowness values, $\mathbf { m _ { \mathrm { t r u e } } }$ ,at the midpoints of the $n$ intervals. Integrate the corresponding slowness function for (1.61) using (1.21) to calculate a noiseless synthetic data vector, $\mathbf { d }$ ,of predicted seismic travel times at the sensor depths.

c. Solve for the slowness, m,as a function of depth using your $\mathbf { G }$ matrix and analytically calculated noiseless travel times using the MATLAB backslash operator. Compare your result graphically with $\mathbf { m } _ { \mathrm { t r u e } }$

d. Generate a noisy travel time vector where independent normally distributed noise with a standard deviation of $0 . 0 5 ~ \mathrm { m s }$ is added to the elements of d. Resolve the system for m and again compare your result graphically with $\mathbf { m } _ { \mathrm { t r u e } }$ . How has the model changed?   
e. Repeat the problem, but for just $n = 4$ sensor depths and corresponding equal length slowness intervals. Is the recovery of the true model improved? Explain in terms of the condition numbers of your $\mathbf { G }$ matrices.

4. Find a journal article that discusses the solution of an inverse problem in a discipline of special interest to you. What are the data? Are the data discrete or continuous? Have the authors discussed possible sources of noise in the data? What is the model? Is the model continuous or discrete? What physical laws determine the forward operator $G \overrightarrow { \mathbfit { \Omega } }$ Is $G$ linear or nonlinear? Do the authors discuss any issues associated with existence,uniqueness,or instability of solutions?

# 1.7. NOTES AND FURTHER READING

Some important references on inverse problems in geophysics and remote sensing include [28, 60, 99,126,166]. Instructive examples of ill-posed problems and their solu-tions can be found in the book edited by Tikhonov and Goncharsky [162]. More mathematically oriented references on inverse problems include [8, 45,59, 65, 67, 90, 94, 108, 112,155,161]. Tomography, particularly in medical imaging and seismology, is a very large field. Some general references on tomography are [70,79,84, 98, 100, 114, 121].

# Linear Regression

# Synopsis

Linear regression is introduced as a parameter estimation problem,and least squares solutions are derived. Maximum likelihood is defined, and its association with least squares solutions under normally distributed data errors is demonstrated. Statistical tests based on $\chi ^ { 2 }$ that provide insight into least squares solutions are discussed. The mapping of data errors into model errors in the context of least squares is described. The determination of confidence intervals using the model covariance matrix and the meaning of model parameter correlations is discussed. The problems of estimating unknown data standard deviations and recognizing proportional data errors are addressed. The issue of data outliers and the concept of robust estimation are introduced,and 1-norm minimization is introduced as a robust estimation technique. General propagation of errors between data and model using Monte Carlo methods is discussed in the context of the iteratively reweighted least squares 1-norm minimization algorithm.

# 2.1. INTRODUCTION TO LINEAR REGRESSION

The problem of finding a parameterized curve that approximately fits a set of data is referred to as regression. When the regression model is linear in the fitted parameters, then we have a linear regression problem. In this chapter, linear regression problems are analyzed as discrete linear inverse problems.

Consider a discrete linear inverse problem. We begin with a data vector, $\mathbf { d }$ ,of m observations,and a vector, $\mathbf { m }$ ,of $n$ model parameters that we wish to determine. The forward problem can be expressed as a lnear system of equations using an $m$ by $n$ matrix $\mathbf { G }$

$$
\mathbf { G m } = \mathbf { d } .
$$

Recall that if $\operatorname { r a n k } ( \mathbf G ) = n .$ ,then the matrix has full column rank. In this chapter we will assume that the matrix $\mathbf { G }$ has full column rank. In Chapter 3 we will consider rank deficient problems.

For a ful column rank matrix, it is frequently the case that there is no solution $\mathbf { m }$ that satisfies (2.1) exactly. This happens because the dimension of the range of $\mathbf { G }$ is smaller than $m$ and a noisy data vector, $\mathbf { d }$ ， will generally lie outside of the range of $\mathbf { G }$ (d will lie in $R ^ { n }$ for typical noise scenarios).

A useful approximate solution may stil be found by finding a particular model m that minimizes some measure of the misfit between the actual data and $\mathbf { G m }$ .The residual vector is the vector of differences between observed data and corresponding model predictions

$$
\mathbf { r } = \mathbf { d } - \mathbf { G m } .
$$

and the elements of r are frequently referred to simply as residuals. One commonly used measure of the misfit is the 2-norm of the residual vector,and a model that minimizes this 2-norm is called a least squares solution. The least squares or 2-norm solution is of special interest both because it is readily amenable to analysis and geometric intuition, and because it turns out to be statistically the most likely solution if data errors are normally distributed.

The least squares solution is, from the normal equations (A.73),

$$
\mathbf { m } _ { L _ { 2 } } = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { d } .
$$

It can be shown that if $\mathbf { G }$ is of full column rank, then $( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 }$ exists (Exercise A.13f).

A classic linear regression problem is finding parameters $m _ { 1 }$ and $m _ { 2 }$ for a line, $\gamma _ { i } =$ $m _ { 1 } + m _ { 2 } x _ { i }$ , that best fits a set of $m > 2$ data points. The system of equations in this case is

$$
\mathbf { G m } = \left[ \begin{array} { c c } { 1 } & { x _ { 1 } } \\ { 1 } & { x _ { 2 } } \\ { . } & { . } \\ { . } & { . } \\ { . } & { . } \\ { 1 } & { x _ { m } } \end{array} \right] \left[ \begin{array} { c } { m _ { 1 } } \\ { m _ { 2 } } \end{array} \right] = \left[ \begin{array} { c } { d _ { 1 } } \\ { d _ { 2 } } \\ { . } \\ { . } \\ { . } \\ { d _ { m } } \end{array} \right] = \mathbf { d } ,
$$

where the $d _ { i }$ are observations of $\gamma$ at each corresponding position $x _ { i }$ . Applying (2.3) to the $\mathbf { G }$ and $\mathbf { m }$ specified in (2.4) gives the least squares solution

$$
\begin{array} { r l } & { \mathbf { \Psi } _ { 2 } = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { d } } \\ & { \mathbf { \Psi } = \left( \left[ \begin{array} { l l l } { 1 } & { \cdots } & { 1 } \\ { x _ { 1 } } & { \cdots } & { x _ { m } } \end{array} \right] \left[ \begin{array} { l l } { 1 } & { x _ { 1 } } \\ { \vdots } & { \vdots } \\ { 1 } & { x _ { m } } \end{array} \right] \right) ^ { - 1 } \left[ \begin{array} { l l l } { 1 } & { \cdots } & { 1 } \\ { x _ { 1 } } & { \cdots } & { x _ { m } } \end{array} \right] \left[ \begin{array} { l } { d _ { 1 } } \\ { d _ { 2 } } \\ { \vdots } \\ { d _ { m } } \end{array} \right] } \\ & { \mathbf { \Psi } = \left[ \begin{array} { l l } { m } & { \sum _ { i = 1 } ^ { m } x _ { i } } \\ { \sum _ { i = 1 } ^ { m } x _ { i } } & { \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l } { \sum _ { i = 1 } ^ { m } d _ { i } } \\ { \sum _ { i = 1 } ^ { m } x _ { i } d _ { i } } \end{array} \right] } \\ & { \mathbf { \Psi } = \frac { 1 } { m \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } - ( \sum _ { i = 1 } ^ { m } x _ { i } ) ^ { 2 } } \left[ \begin{array} { l l l } { \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } } & { - \sum _ { i = 1 } ^ { m } x _ { i } } \\ { - \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } } & { m } \end{array} \right] \left[ \begin{array} { l } { \sum _ { i = 1 } ^ { m } d _ { i } } \\ { \sum _ { i = 1 } ^ { m } x _ { i } d _ { i } } \end{array} \right] . } \end{array}
$$

# 2.2. STATISTICAL ASPECTS OF LEAST SQUARES

If we consider data points to be imperfect measurements that include random errors, then we are faced with the problem of finding the solution that is best from a statistical point of view. One approach, maximum likelihood estimation, considers the ques-tion from the following perspective. Given that we observed a particular data set, that we know the statistical characteristics of these observations,and that we have a mathematical model for the forward problem,what is the model from which these observations would most likely arise?

Maximum likelihood estimation is a general method that can be applied to any estimation problem where a joint probability density function (B.26) can be assigned to the observations. The essential problem is to find the most likely model, as characterized by the elements of the parameter vector m, for the set of observations contained in the vector d. We will assume that the observations are independent so that we can use the product form of the joint probability density function (B.28).

Given a model m, we have a probability density function $f _ { i } ( d _ { i } | \mathbf { m } )$ for each of the observations. In general, these probability density functions will vary depending on $\mathbf { m }$ ， so probability densities are conditional on m. The joint probability density for a vector of independent observations $\mathbf { d }$ will be

$$
f ( \mathbf { d } | \mathbf { m } ) = f _ { 1 } ( d _ { 1 } | \mathbf { m } ) \cdot f _ { 2 } ( d _ { 2 } | \mathbf { m } ) \cdot \cdot \cdot f _ { m } ( d _ { m } | \mathbf { m } ) .
$$

Note that the $f ( d _ { i } | \mathbf { m } )$ are probability densities, not probabilities. We can only com-pute the probability of observing data in some range for a given model $\mathbf { m }$ by integrating $f ( \mathbf { d } | \mathbf { m } )$ over that range. In fact,the probability of geting any particular set of data exactly is precisely zero! This conceptual conundrum can be resolved by considering the probability of getting a data set that lies within a small $m \cdot$ -dimensional box around a particular data set d. This probability will be nearly proportional to the probability density $f ( \mathbf { d } | \mathbf { m } )$

In practice,we measure a particular data vector and wish to find the“best”model to match it in the maximum likelihood sense.That is, $\mathbf { d }$ will be a fixed set of observations, and $\mathbf { m }$ will be a vector of parameters to be estimated. The likelihood function, $L$ ,is the probability of m given an observed $\mathbf { d }$ ,which is identical to (2.6),the joint probability density function of $\mathbf { d }$ given m

$$
L ( \mathbf { m } | \mathbf { d } ) = f ( \mathbf { d } | \mathbf { m } ) .
$$

For many possible models, $\mathbf { m }$ ， (2.7) will be extremely close to zero because such models would be extremely unlikely to produce the observed data set d. The likelihood would be much larger for any models that, conversely, would be relatively likely to produce the observed data. According to the maximum likelihood principle we should select the model m that maximizes the likelihood function (2.7). Model estimates obtained in this manner have many desirable statistical properties [29, 40].

It is particularly insightful that when we have a discrete linear inverse problem and the data errors are independent and normally distributed, then the maximum likelihood principle solution is the least squares solution. To show this,assume that the data have independent random errors that are normally distributed with expected value zero,and where the standard deviation of the ith observation, $d _ { i }$ ,is $\sigma _ { i }$ .The probability density for $d _ { i }$ then takes the form of (B.6),

$$
f _ { i } ( d _ { i } | { \bf m } ) = \frac { 1 } { \sigma _ { i } \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } ( d _ { i } - ( { \bf G m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } .
$$

The likelihood function for the complete data set is the product of the individual likelihoods,

$$
L ( \mathbf { m } | \mathbf { d } ) = \frac { 1 } { ( 2 \pi ) ^ { m / 2 } \prod _ { i = 1 } ^ { m } \sigma _ { i } } \prod _ { i = 1 } ^ { m } e ^ { - \frac { 1 } { 2 } ( d _ { i } - ( \mathbf { G } \mathbf { m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } .
$$

The constant factor does not affect the maximization of $L$ ， so we can solve

$$
\operatorname* { m a x } \prod _ { i = 1 } ^ { m } e ^ { - \frac { 1 } { 2 } ( d _ { i } - ( \mathbf { G m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } .
$$

The natural logarithm is a monotonically increasing function, so we can equivalently solve

$$
\operatorname* { m a x } \log \prod _ { i = 1 } ^ { m } e ^ { - \frac { 1 } { 2 } ( d _ { i } - ( \mathbf { G m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } = \operatorname* { m a x } \left[ - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } \frac { ( d _ { i } - ( \mathbf { G m } ) _ { i } ) ^ { 2 } } { \sigma _ { i } ^ { 2 } } \right] .
$$

Finally, if we turn the maximization into a minimization by changing sign and ignore the constant factor of $1 / 2$ ，the problem becomes

$$
\operatorname* { m i n } \sum _ { i = 1 } ^ { m } \frac { ( d _ { i } - ( \mathbf { G } \mathbf { m } ) _ { i } ) ^ { 2 } } { \sigma _ { i } ^ { 2 } } .
$$

Aside from the distinct $1 / \sigma _ { i } ^ { 2 }$ factors in each term of the sum,this is identical to the least squares problem for $\mathbf { G m } = \mathbf { d }$

To incorporate the data standard deviations into this solution, we scale the system of equations to obtain a weighted system of equations. Let a diagonal weighting matrix be

$$
\mathbf { W } = \mathrm { d i a g } ( 1 / \sigma _ { 1 } , 1 / \sigma _ { 2 } , \ldots , 1 / \sigma _ { m } ) .
$$

Then let

$$
\mathbf { G } _ { u } = \mathbf { w } \mathbf { G }
$$

and

$$
\mathbf { d } _ { u } = \mathbf { w } \mathbf { d } .
$$

The weighted system of equations is then

$$
\mathbf { G } _ { u } , \mathbf { m } = \mathbf { d } _ { u } .
$$

The normal equations (A.73) solution to (2.16) is

$$
\mathbf { m } _ { L _ { 2 } } = ( \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } ) ^ { - 1 } \mathbf { G } _ { u } ^ { T } \mathbf { d } _ { u } .
$$

Now,

$$
\| \mathbf { d } _ { w } - \mathbf { G } _ { w } \mathbf { m } _ { L _ { 2 } } \| _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { m } ( d _ { i } - ( \mathbf { G } \mathbf { m } _ { L _ { 2 } } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } .
$$

Thus, the least squares solution to $\mathbf { G } _ { \boldsymbol { w } } \mathbf { m } = \mathbf { d } _ { \boldsymbol { w } }$ is the maximum likelihood solution.

The sum of the squares of the residuals also provides useful statistical information about the quality of model estimates obtained with least squares. The chi-square statistic is

$$
\chi _ { \mathrm { o b s } } ^ { 2 } = \sum _ { i = 1 } ^ { m } ( d _ { i } - ( { \bf G m } _ { L _ { 2 } } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } .
$$

Since $\chi _ { \mathrm { o b s } } ^ { 2 }$ der rsi $\mathbf { d }$   
It can be shown that under our assmptions, X²bs $\chi ^ { 2 }$ $\nu = m - n$ degrees of freedom [29, 40].

The probability density function for the $\chi ^ { 2 }$ distribution is

$$
f _ { \chi ^ { 2 } } ( x ) = \frac { 1 } { 2 ^ { \nu / 2 } \Gamma ( \nu / 2 ) } x ^ { \frac { 1 } { 2 } \nu - 1 } e ^ { - x / 2 }
$$

(Figure B.4). The $\chi ^ { 2 }$ test provides a statistical assessment of the assumptions that we used in finding theleast squaressolution. Inthis test, wecompute $\chi _ { \mathrm { o b s } } ^ { 2 }$ and compare it to the theoretical $\chi ^ { 2 }$ distribution with $\nu = m - n$ degrees of freedom.

The probability of obtaining a $\chi ^ { 2 }$ value as large or larger than the observed value (and hence a worse misfit between data and model data predictions than that obtained) is called the $\pmb { p }$ value of the test, and is given by

$$
p = \intop _ { \chi _ { \mathrm { o b s } } ^ { 2 } } ^ { \infty } f _ { \chi ^ { 2 } } ( x ) d x .
$$

When data errors are independent and normally distributed,and the mathematical model is correct, it can be shown that the $p$ -value will be uniformly distributed between zero and one (Exercise 2.4). In practice, particular $p .$ -values that are very close to either extreme indicate that one or more of these assumptions are incorrect.

There are three general cases.

1. The $p$ -value is not too small and not too large. Our least squares solution produces an acceptable data fit and our statistical assumptions of data errors are consistent. Practically, $p$ does not actually have to be very large to be deemed marginally “acceptable” in many cases (e.g, $p \approx 1 0 ^ { - 2 } ,$ ), as truly“wrong” models will typically produce extraordinarily small $p$ -values (e.g., $1 0 ^ { - 1 2 } .$ ）because of the short-tailed nature of the normal distribution.

Because the $p$ -value will be uniformly distributed when we have a correct mathematical model and our statistical data assumptions are valid, it is inappropriate to conclude anything based on the differences between $p$ -values in this range. For example,one should not conclude that a $p .$ -value of O.7 is“better” than a $p$ -value of 0.2.

2. The $p$ -value is very small. We are faced with three nonexclusive possibilities, but something is clearly wrong.

a. The data truly represent an extremely unlikely realization. This is easy to rule out for $p$ -values very close to zero. For example, suppose an experiment produced a data realization where the probability of a worse fit was $1 0 ^ { - 9 }$ . If the model was correct, then we would have to perform on the order of a billion experiments to get a comparably poor fit to the data. It is far more likely that something else is wrong.   
b. The mathematical model $\mathbf { G m } = \mathbf { d }$ is incorrect. Most often this happens because we have left some important aspect of the physics out of the mathematical model.   
c. The data errors are underestimated or not normally distributed. In particular, we may have underestimated the $\sigma _ { i }$

3. The $p$ -value is very close to one. The fit of the model predictions to the data is almost exact. We should investigate the possbility that we have overestimated the data errors.A more sinister possibility is that a very high $p$ -value is indicative of data fraud, such as might happen if data were cooked up ahead of time to fit a particular model!

A rule of thumb for problems with a large number of degrees of freedom, $\nu$ ,is that the expected value of $\chi ^ { 2 }$ approaches $\nu$ . This arises because,by the central limit theorem (Section B.6), the $\chi ^ { 2 }$ random variable,which is itself a sum of random variables, will become normally distributed as the number of terms in the sum becomes large. The mean of the resulting distribution will approach $\nu$ and the standard deviation will approach (2v)1/2.

In addition to examining $\chi _ { \mathrm { o b s } } ^ { 2 }$ , it is importanttoexaminetheindividual weghtd residuals corresponding to a model, $\boldsymbol { \mathrm { r } } _ { \boldsymbol { w } , i } = ( \mathbf { d } - \mathbf { G m } ) _ { i } / \sigma _ { i } = ( \mathbf { d } _ { \boldsymbol { w } } - \mathbf { G } _ { \boldsymbol { w } } \mathbf { m } ) _ { i } .$ The elements of $\mathbf { r } _ { w }$ should be roughly normally distributed with standard deviation one and should show no obvious patterns. In some cases where an incorrect model has been fitted to the data, the residuals will reveal the nature of the modeling error. For example,in linear regression to a line, it might be that all of the residuals are negative for small and large values of the independent variable $_ x$ but positive for intermediate values of $_ x$ This would suggest that an additional quadratic term is required in the regresson model.

Parameter estimates obtained via linear regression are linear combinations of the data (2.17). If the data errors are normally distributed, then the parameter estimates will also be normally distributed because a linear combination of normally distributed random variables is normally distributed [4, 29]. To derive the mapping between data and model covariances,consider the covariance of a data vector, d, of normally distributed, independent random variables, operated on by a general linear transformation specified by a matrix, A. The appropriate covariance mapping is (B.65)

$$
\operatorname { C o v } ( \mathbf { A } \mathbf { d } ) = \mathbf { A } \operatorname { C o v } ( \mathbf { d } ) \mathbf { A } ^ { T } .
$$

The least squares solution has $\mathbf { A } = ( \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } ) ^ { - 1 } \mathbf { G } _ { u } ^ { T }$ . The general covariance matrix of the model parameters for a least squares solution is thus

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) = ( \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } ) ^ { - 1 } \mathbf { G } _ { \nu } ^ { T } \mathrm { C o v } ( \mathbf { d } _ { \nu } ) \mathbf { G } _ { \nu } ( \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } ) ^ { - 1 } . } \end{array}
$$

If the weighted data are independent,and thus have an identity covariance matrix, this simplifies to

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) = ( \mathbf { G } _ { \psi } ^ { T } \mathbf { G } _ { \psi } ) ^ { - 1 } \mathbf { G } _ { \psi } ^ { T } \mathbf { I } _ { m } \mathbf { G } _ { \psi } ( \mathbf { G } _ { \psi } ^ { T } \mathbf { G } _ { \psi } ) ^ { - 1 } = ( \mathbf { G } _ { \psi } ^ { T } \mathbf { G } _ { \psi } ) ^ { - 1 } . } \end{array}
$$

In the case of independent and identically distributed normal data errors,so that the data covariance matrix $\mathrm { C o v } ( \mathbf { d } )$ is simply the variance $\sigma ^ { 2 }$ times the $m$ by $m$ identity matrix, ${ \mathbf I } _ { m }$ ， (2.24) can be written in terms of the unweighted system matrix as

$$
\begin{array} { r } { \mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = \sigma ^ { 2 } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } . } \end{array}
$$

Note that even for a diagonal data covariance matrix, the model covariance matrix is typically not diagonal,and the model parameters are thus correlated. Because elements of least squares models are each constructed from linear combinations of the data vector elements, this statistical dependence between the elements of $\mathbf { m }$ should not be surprising.

The expected value of the least squares solution is

$$
E [ \mathbf { m } _ { L _ { 2 } } ] = ( \mathbf { G } _ { w } ^ { T } \mathbf { G } _ { w } ) ^ { - 1 } \mathbf { G } _ { w } ^ { T } E [ \mathbf { d } _ { w } ] .
$$

Because $E [ \mathbf { d } _ { \boldsymbol { w } } ] = \mathbf { d } _ { \mathrm { t r u e } , \boldsymbol { w } }$ ,and $\mathbf { G } _ { u } \mathbf { m } _ { \mathrm { t r u e } } = \mathbf { d } _ { \mathrm { t r u e } , w }$ ， we have

$$
\mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } , \mathbf { m } _ { \mathrm { t r u e } } = \mathbf { G } _ { u } ^ { T } \mathbf { d } _ { \mathrm { t r u e } , u } .
$$

Thus

$$
\begin{array} { r l } & { E [ \mathbf { m } _ { L _ { 2 } } ] = ( \mathbf { G } _ { \boldsymbol { w } } ^ { T } \mathbf { G } _ { \boldsymbol { w } } ) ^ { - 1 } \mathbf { G } _ { \boldsymbol { w } } ^ { T } \mathbf { G } _ { \boldsymbol { w } } \mathbf { m } _ { \mathrm { t r u e } } } \\ & { \qquad = \mathbf { m } _ { \mathrm { t r u e } } . } \end{array}
$$

In statistical terms,the least squares solution is said to be unbiased.

We can compute $9 5 \%$ confidence intervals for individual model parameters using the fact that each model parameter $m _ { i }$ has a normal distribution with mean given by the corresponding element of $\mathbf { m } _ { \mathrm { t r u e } }$ and variance $\mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) _ { i , i }$ .The $9 5 \%$ confidence intervals are given by

$$
\mathbf { m } _ { L _ { 2 } } \pm 1 . 9 6 ~ \mathrm { d i a g } ( \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) ) ^ { 1 / 2 } ,
$$

where the 1.96 factor arises from

$$
{ \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } \int _ { - 1 . 9 6 \sigma } ^ { 1 . 9 6 \sigma } e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x \approx 0 . 9 5 .
$$

# Example 2.1

Let us recall Example 1.1 of linear regression of ballstic observations to a quadratic model, where the regression model is

$$
\gamma ( t ) = m _ { 1 } + m _ { 2 } t - ( 1 / 2 ) m _ { 3 } t ^ { 2 } .
$$

Here $\gamma$ is measured in the upward direction,and the minus sign is applied to the third term because gravitational acceleration is downward. Consider a synthetic data set with $m = 1 0$ observations and independent normal data errors $\langle \sigma = 8 \mathrm { ~ m ~ } ,$ ， generated using

$$
\mathbf { m } _ { \mathrm { t r u e } } = [ 1 0 \mathrm { m } , 1 0 0 \mathrm { m } / \mathrm { s } , 9 . 8 \mathrm { m } / \mathrm { s } ^ { 2 } ] ^ { T }
$$

# (Table 2.1).

To obtain the least squares solution, we construct the $\mathbf { G }$ matrix. The ith row of $\mathbf { G }$ is given by

$$
\mathbf { G } _ { i , \cdot } = [ 1 , t _ { i } , - ( 1 / 2 ) t _ { i } ^ { 2 } ] ,
$$

Table 2.1 Data for the ballstics example.   

<table><tr><td>t (s)</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>y (m)</td><td></td><td></td><td></td><td></td><td>109.4187.5267.5331.9386.1428.4452.2498.1</td><td></td><td></td><td></td><td>512.3</td><td>3513.0</td></tr></table>

so that

$$
\mathbf { G } = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { - 0 . 5 } \\ { 1 } & { 2 } & { - 2 . 0 } \\ { 1 } & { 3 } & { - 4 . 5 } \\ { 1 } & { 4 } & { - 8 . 0 } \\ { 1 } & { 5 } & { - 1 2 . 5 } \\ { 1 } & { 6 } & { - 1 8 . 0 } \\ { 1 } & { 7 } & { - 2 4 . 5 } \\ { 1 } & { 8 } & { - 3 2 . 0 } \\ { 1 } & { 9 } & { - 4 0 . 5 } \\ { 1 } & { 1 0 } & { - 5 0 . 0 } \end{array} \right] } .
$$

We solve for the parameters using the weighted normal equations, (2.17),to obtain a model estimate,

$$
\mathbf { m } _ { L _ { 2 } } = [ 1 6 . 4 \mathrm { m } , 9 7 . 0 \mathrm { m } / \mathrm { s } , 9 . 4 \mathrm { m } / \mathrm { s } ^ { 2 } ] ^ { T } .
$$

Figure 2.1 shows the observed data and the fitted curve. The model covariance matrix associated with ${ \bf { m } } _ { L _ { 2 } }$ is

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) = \left[ \begin{array} { r r r } { 8 8 . 5 3 } & { - 3 3 . 6 0 } & { - 5 . 3 3 } \\ { - 3 3 . 6 0 } & { 1 5 . 4 4 } & { 2 . 6 7 } \\ { - 5 . 3 3 } & { 2 . 6 7 } & { 0 . 4 8 } \end{array} \right] . } \end{array}
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/277384f4af13ab831d2b64ca1b113923b7a9b881847330587a50cc1883c5fa00.jpg)  
Figure 2.1 Data and model predictions for the ballistics example, with one standard deviation data error bounds indicated.

In our example, $m = 1 0$ and $n = 3$ ,so (2.3O) gives the following parameter estimates with $9 5 \%$ confidence intervals:

$$
\mathbf { m } _ { L _ { 2 } } = [ 1 6 . 4 2 \pm 1 8 . 4 4 \mathrm { m } , 9 6 . 9 7 \pm 7 . 7 0 \mathrm { m } / \mathrm { s } , 9 . 4 1 \pm 1 . 3 6 \mathrm { m } / \mathrm { s } ^ { 2 } ] ^ { T } .
$$

The $\chi ^ { 2 }$ value for this regression is approximately 4.2, and the number of degrees of freedom is $\nu = m - n = 1 0 - 3 = 7$ so the $p .$ -value, (2.21), is

$$
p = \int _ { 4 . 2 0 } ^ { \infty } { \frac { 1 } { 2 ^ { 7 / 2 } \Gamma ( 7 / 2 ) } } x ^ { { \frac { 5 } { 2 } } } e ^ { - { \frac { x } { 2 } } } d x \approx 0 . 7 6 ,
$$

which is in the realm of plausibility. This means that the fitted model is consistent with the modeling and data uncertainty assumptions.

If we consider combinations of model parameters,the interpretation of the uncertainty in the model parameters becomes more complicated. To characterize model uncertainty more effectively， we can examine $9 5 \%$ confidence regions for pairs or larger sets of parameters. When joint parameter confidence regions are projected onto the coordinate axes, $m _ { i }$ ，we obtain intervals for parameters that may be significantly larger than we would estimate when considering parameters individually, as in (2.38).

For a vector of estimated model parameters ${ \bf { m } } _ { L _ { 2 } }$ characterized by an $n \cdot$ -dimensional multivariate normal distribution with mean $\mathbf { m } _ { \mathrm { t r u e } }$ and covariance matrix $\mathbf { C } =$ $\mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } )$ ，

$$
( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) ,
$$

can be shown to have a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom [89]. Thus if $\Delta ^ { 2 }$ is the 95th percentile of the $\chi ^ { 2 }$ distribution with $n$ degrees of freedom, the $9 5 \%$ confidence region is defined by the inequality

$$
( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) \leq \Delta ^ { 2 } .
$$

The confidence region defined by this inequality is an $n$ -dimensional ellipsoid.

If we wish to find an error ellipsoid for a lower dimensional subset of the model parameters,we can project the $n \cdot$ -dimensional error elipsoid onto the lower dimensional subspace by taking only those rows and columns of C and elements of m that correspond to the dimensions that we want to keep [1]. In this case, the number of degrees of freedom in the associated $\Delta ^ { 2 }$ calculation should be correspondingly reduced from $n$ to match the number of model parameters in the projected error ellipsoid.

Since the covariance matrix and its inverse are symmetric and positive definite, we can diagonalize ${ \bf C } ^ { - 1 }$ using (A.77) as

$$
\mathbf { C } ^ { - 1 } = \mathbf { P } ^ { T } \pmb { \Lambda } \mathbf { P } ,
$$

where $\pmb { \Lambda }$ is a diagonal matrix of positive eigenvalues and the columns of $\mathbf { P }$ are orthonormal eigenvectors. The semiaxes defined by the columns of $\mathbf { P }$ and associated eigenvalues are referred to as the principal axes of the error ellipsoid. The ith semimajor error ellpsoid axis direction is defined by $\mathbf { P } _ { \cdot , i }$ and its corresponding length is $\Delta / \sqrt { \Lambda _ { i , i } }$

Because the model covariance matrix is typically not diagonal, the principal axes are typically not aligned in the $m _ { i }$ axis directions. However, we can project the appropriate confidence ellipsoid onto the $m _ { i }$ axes to obtain a“box”that includes the entire $9 5 \%$ error elipsoid,along with some additional external volume. Such a box provides a conservative confidence interval for a joint collction of model parametrs.

Correlations for parameter pairs $( m _ { i } , ~ m _ { j } )$ are measures of the inclination of the error ellipsoid with respect to the parameter axes.A correlation approaching $+ 1$ means the projection is needle-like with its long principal axis having a positive slope,a zero correlation means that the projection has principal axes that are aligned with the axes of the $( m _ { i } , ~ m _ { j } )$ plane,and a correlation approaching $- 1$ means that the projection is needle-like with its long principal axis having a negative slope.

# Example 2.2

The parameter correlations for Example 2.1 are

$$
\rho _ { m _ { i } , m _ { j } } = \frac { \mathrm { C o v } ( m _ { i } , m _ { j } ) } { \sqrt { \mathrm { V a r } ( m _ { i } ) \cdot \mathrm { V a r } ( m _ { j } ) } } ,
$$

which give

$$
\begin{array} { r } { \rho _ { m _ { 1 } , m _ { 2 } } = - 0 . 9 1 } \\ { \rho _ { m _ { 1 } , m _ { 3 } } = - 0 . 8 1 } \\ { \rho _ { m _ { 2 } , m _ { 3 } } = 0 . 9 7 . } \end{array}
$$

The three model parameters are highly statistically dependent,and the error elipsoid is thus inclined in model space. Figure 2.2 shows the $9 5 \%$ confidence ellipsoid.

Diagonalization of ${ \bf C } ^ { - 1 }$ (2.42) shows that the directions of the semiaxes for the error ellipsoid are

$$
\mathbf { P } = [ \mathbf { P } _ { \cdot , 1 } , \mathbf { P } _ { \cdot , 2 } , \mathbf { P } _ { \cdot , 3 } ] \approx \left[ \begin{array} { r r r } { 0 . 9 3 } & { 0 . 3 6 } & { - 0 . 0 3 } \\ { - 0 . 3 6 } & { 0 . 9 0 } & { - 0 . 2 3 } \\ { - 0 . 0 6 } & { 0 . 2 3 } & { 0 . 9 7 } \end{array} \right] ,
$$

with corresponding eigenvalues

$$
[ \lambda _ { 1 } , \lambda _ { 2 } , \lambda _ { 3 } ] \approx [ 0 . 0 0 9 8 , 0 . 4 0 4 6 , 1 0 4 . 7 ] .
$$

The corresponding $9 5 \%$ confidence ellisoid semiaxis lengths are

$$
\sqrt { F _ { \chi ^ { 2 } , 3 } ^ { - 1 } ( 0 . 9 5 ) } [ 1 / \sqrt { \lambda _ { 1 } } , 1 / \sqrt { \lambda _ { 2 } } , 1 / \sqrt { \lambda _ { 3 } } ] \approx [ 2 8 . 2 , 4 . 4 , 0 . 2 7 ]
$$

where F-1 $F _ { \chi ^ { 2 } , 3 } ^ { - 1 } ( 0 . 9 5 ) \approx 7 . 8 0$ is the 95th percentile of the $\chi ^ { 2 }$ distribution with three degrees of freedom.

Projecting the $9 5 \%$ confidence elipsoid defined by (2.47) and (2.49) into the $( m _ { 1 } , m _ { 2 } , m _ { 3 } )$ coordinate system, and selecting maximum absolute values in the $m _ { i }$ direc-tions to define an ellpsoid-bounding box, we obtain $9 5 \%$ confidence intervals for the parameters considered jointly,

$$
[ m _ { 1 } , m _ { 2 } , m _ { 3 } ] = [ 1 6 . 4 2 \pm 2 6 . 2 5 \mathrm { m } , 9 6 . 9 7 \pm 1 0 . 2 4 \mathrm { m } / \mathrm { s } , 9 . 4 1 \pm 1 . 6 5 \mathrm { m } / \mathrm { s } ^ { 2 } ] ,
$$

which are appreciably broader than the single parameter confidence estimates obtained using only the diagonal covariance matrix terms in (2.38). Note that there is actually a greater than $9 5 \%$ probability that the box defined by (2.5O) will include the true values of the parameters. The reason is that these intervals,considered together as a rectangular prism-shaped region, include a significant parameter space volume that lies outside of the $9 5 \%$ confidence ellipsoid.

It is insightful to note that the model covariance matrix (2.23) does not depend on the estimated model, but depends solely on the system matrix and data covariance. Model covariance is thus exclusively a characteristic of experimental design that reflects how much influence the noise in a general data set will have on a model estimate, not on particular data values from an individual experiment. It is essential to evaluate the $p .$ -value, or another “goodness-of-fit” measure, in assessing a model because an examination of the solution parameters and the covariance matrix alone does not reveal whether we are actually fitting the data adequately.

# 2.3.AN ALTERNATIVE VIEW OF THE $95 \%$ CONFIDENCE ELLIPSOID

Recall (2.29) that in linear regression, the least squares solution $\mathbf { m } _ { L _ { 2 } }$ for zero-mean multivariate distributed normal data errors itself has a multivariate normal distribution with

$$
E [ \mathbf { m } _ { L _ { 2 } } ] = \mathbf { m } _ { \mathrm { t r u e } } .
$$

By (2.24), the model covariance matrix is

$$
\mathbf { C } = \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) = ( \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } ) ^ { - 1 } ,
$$

where the rows of $\mathbf { G } _ { w }$ are those of $\mathbf { G }$ that have been weighted by respective reciprocal data standard deviations (2.14),and we assume that the data errors are independent and that $( \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } )$ is nonsingular. By Theorem B.6,

$$
( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } )
$$

has a $\chi ^ { 2 }$ distribution with degrees of freedom equal to the number of model parameters, $n$ Let $\Delta ^ { 2 }$ be the 95th percentile of the $\chi ^ { 2 }$ distribution with $n$ degrees of freedom. Then the probability

$$
P \left( ( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { L _ { 2 } } ) \leq \Delta ^ { 2 } \right)
$$

will be 0.95.

Although (2.54) describes an elipsoid centered at $\mathbf { m } _ { \mathrm { t r u e } }$ , the inequality is symmetric in $\mathbf { m } _ { \mathrm { t r u e } }$ and ${ \bf { m } } _ { L _ { 2 } }$ , and can also therefore be thought of as defining an ellipsoid centered around ${ \bf { m } } _ { L _ { 2 } }$ . Thus, there is a $9 5 \%$ probability that when we gather our data and compute $\mathbf { m } _ { L _ { 2 } }$ , the true model $\mathbf { m _ { \mathrm { t r u e } } }$ willie within the model space ellipsoid defined by

$$
( \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ) \leq \Delta ^ { 2 } .
$$

Since $\mathbf { C } = ( \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } ) ^ { - 1 }$ ， $\mathbf { C } ^ { - 1 } = \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u }$ , and the 95th percentile confidence ellipsoid can also be written as

$$
( \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } ( \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ) \leq \Delta ^ { 2 } .
$$

If we let

$$
\boldsymbol { \chi } ^ { 2 } ( \mathbf { m } ) = \| \mathbf { G } _ { w } \mathbf { m } - \mathbf { d } _ { w } \| _ { 2 } ^ { 2 } = ( \mathbf { G } _ { w } \mathbf { m } - \mathbf { d } _ { w } ) ^ { T } ( \mathbf { G } _ { w } \mathbf { m } - \mathbf { d } _ { w } ) ,
$$

then

$$
\begin{array} { r l } & { { \bf \Pi } ^ { 2 } ( { \bf m } ) - \chi ^ { 2 } ( { \bf m } _ { L _ { 2 } } ) = ( { \bf G } _ { w } { \bf m } - { \bf d } _ { w } ) ^ { T } ( { \bf G } _ { w } { \bf m } - { \bf d } _ { w } ) - ( { \bf G } _ { w } { \bf m } _ { L _ { 2 } } - { \bf d } _ { w } ) ^ { T } ( { \bf G } _ { w } { \bf m } _ { L _ { 2 } } - { \bf d } _ { w } ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad = { \bf m } ^ { T } { \bf G } _ { w } ^ { T } { \bf G } _ { w } { \bf m } - { \bf d } _ { w } ^ { T } { \bf G } _ { w } { \bf m } - { \bf m } ^ { T } { \bf G } _ { w } ^ { T } { \bf d } _ { w } + { \bf d } _ { w } ^ { T } { \bf d } _ { w } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad - { \bf m } _ { L _ { 2 } } ^ { T } { \bf G } _ { w } ^ { T } { \bf G } _ { w } { \bf m } _ { L _ { 2 } } + { \bf d } _ { w } ^ { T } { \bf G } _ { w } { \bf m } _ { L _ { 2 } } + { \bf m } _ { L _ { 2 } } { \bf G } _ { w } ^ { T } { \bf d } _ { w } - { \bf d } _ { w } ^ { T } { \bf d } _ { w } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad = { \bf m } ^ { T } { \bf G } _ { w } ^ { T } { \bf G } _ { w } { \bf m } - { \bf d } _ { w } ^ { T } { \bf G } _ { w } { \bf m } - { \bf m } ^ { T } { \bf G } _ { w } ^ { T } { \bf d } _ { w } } \\ & { \quad \quad \quad \quad \quad \quad \quad - { \bf m } _ { L _ { 2 } } ^ { T } { \bf G } _ { w } ^ { T } { \bf G } _ { w } { \bf m } _ { L _ { 2 } } + { \bf d } _ { w } ^ { T } { \bf G } _ { w } { \bf m } _ { L _ { 2 } } + { \bf m } _ { L _ { 2 } } ^ { T } { \bf G } _ { w } ^ { T } { \bf d } _ { w } . } \end{array}
$$

Since ${ \bf { m } } _ { L _ { 2 } }$ is a least squares solution to the weighted system of equations, it satisfies the corresponding normal equations. We can thus replace all occurrences of $\mathbf { G } _ { 2 } ^ { T } \mathbf { d } _ { u }$ with $\mathbf { G } _ { u } ^ { T } \mathbf { G } _ { u } \mathbf { m } _ { L _ { 2 } }$ using (2.3) to obtain

$$
\begin{array} { r l } & { \chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } _ { L _ { 2 } } ) = \mathbf { m } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } \mathbf { m } - \mathbf { m } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { w } \mathbf { m } _ { L _ { 2 } } } \\ & { \qquad - \mathbf { m } _ { L _ { 2 } } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } \mathbf { m } _ { L _ { 2 } } + \mathbf { m } _ { L _ { 2 } } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { w } \mathbf { m } _ { L _ { 2 } } + \mathbf { m } _ { L _ { 2 } } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { w } \mathbf { m } _ { L _ { 2 } } } \\ & { \qquad = \mathbf { m } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { w } \mathbf { m } } \\ & { \qquad - \mathbf { m } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } \mathbf { m } _ { L _ { 2 } } + \mathbf { m } _ { L _ { 2 } } ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { w } \mathbf { m } _ { L _ { 2 } } , } \end{array}
$$

and, finally,

$$
\chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } _ { L _ { 2 } } ) = ( \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ) ^ { T } \mathbf { G } _ { \nu } ^ { T } \mathbf { G } _ { \nu } ( \mathbf { m } - \mathbf { m } _ { L _ { 2 } } ) .
$$

Thus our $9 5 \%$ confidence elipsoid can also be writen as

$$
\chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } _ { L _ { 2 } } ) \leq \Delta ^ { 2 }
$$

and the contour of the $\chi ^ { 2 } ( \mathbf { m } )$ function at $\chi ^ { 2 } ( \mathbf { m } _ { L _ { 2 } } ) + \Delta ^ { 2 }$ gives the boundary of the 95th percentile confidence ellipsoid.

# 2.4. UNKNOWN MEASUREMENT STANDARD DEVIATIONS

Suppose that we do not know the standard deviations of the measurement errors a priori. In this case,if we assume that the measurement errors are independent and normally distributed with expected value of zero and standard deviation $\sigma$ , then we can perform the linear regression and estimate $\sigma$ from the residuals.

First, we find the least squares solution to the unweighted problem $\mathbf { G m } = \mathbf { d }$ ,and let

$$
\mathbf { r } = \mathbf { d } - \mathbf { G m } _ { L _ { 2 } } .
$$

To estimate the standard deviation from the residuals,let

$$
s = { \frac { | | \mathbf { r } | | _ { 2 } } { \sqrt { \nu } } } ,
$$

where $\nu = m - n$ is the number of degrees of freedom [40].

As you might expect, there is a statistical cost associated with not knowing the true standard deviation. If the data standard deviations are known ahead of time, then each

$$
m _ { i } ^ { \prime } = \frac { m _ { i } - m _ { \mathrm { t r u e } _ { i } } } { \sqrt { { \bf C } _ { i , i } } } ,
$$

where $\mathbf { C }$ is the covariance matrix (2.25), has a standard normal distribution. However, if instead of a known standard deviation we have an estimate, $s$ ，obtained using (2.63), then, if $\mathbf { C ^ { \prime } }$ is given by the covariance matrix formula (2.25), but with $\sigma = s$ ,each

$$
m _ { i } ^ { \prime } = \frac { m _ { i } - m _ { \mathrm { t r u e } _ { i } } } { \sqrt { \mathbf { C } _ { i , i } ^ { \prime } } }
$$

has a Student's $t$ distribution (B.7) with $\nu = m - n$ degrees of freedom. For smaller numbers of degrees of freedom this produces appreciably broader confidence intervals than the standard normal distribution.As $\nu$ becomes large,(2.63) becomes an increasingly better estimate of $\sigma$ as the two distributions converge. Confidence ellipsoids corresponding to this case can also be computed, but the formula is somewhat more complicated than in the case of known standard deviations [40].

In assessing goodness-of-fit in this case,a problem arises in that we can no longer apply the $\chi ^ { 2 }$ test. Recall that the $\chi ^ { 2 }$ test was based on the assumption that the data errors were normally distributed with known standard deviations $\sigma _ { i }$ .If the actual residuals were too large relative to the $\sigma _ { i }$ ，then $\chi ^ { 2 }$ would be large,and we would reject the linear regression fit based on a very small $p$ -value. However, if we substitute (2.63) into (2.19), we find that $\chi _ { \mathrm { o b s } } ^ { 2 } = \nu$ ， so such a model will always pass the $\chi ^ { 2 }$ test.

# Example 2.3

Consider the analysis of a linear regression problem in which the measurement errors are assumed to be independent and normally distributed, with equal but unknown standard deviations, $\sigma$ . We are given data $\gamma _ { i }$ collected at points $x _ { i }$ (Figure 2.3) that appear to follow a linear relationship.

In this case, the system matrix for the forward problem is

$$
\mathbf { G } = \left[ \begin{array} { l l } { 1 } & { x _ { 1 } } \\ { 1 } & { x _ { 2 } } \\ { . } & { . } \\ { . } & { . } \\ { . } & { . } \\ { 1 } & { x _ { m } } \end{array} \right] .
$$

The least squares solution to

$$
\mathbf { G m } = \mathbf { y }
$$

has

$$
\gamma _ { i } = - 1 . 0 3 + 1 0 . 0 9 x _ { i } .
$$

Figure 2.3 shows the data and the linear regresson line. Our estimate of the standard deviation of the measurement errors from (2.63) is $s = 3 0 . 7 4$ . The estimated covariance matrix for the fitted parameters is

$$
\mathbf { C } ^ { \prime } = s ^ { 2 } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } = \left[ { \begin{array} { c c } { 3 3 8 . 2 4 } & { - 4 . 9 3 } \\ { - 4 . 9 3 } & { 0 . 0 8 } \end{array} } \right] .
$$

The parameter confidence intervals, evaluated for each parameter separately, are

$$
m _ { 1 } = - 1 . 0 3 \pm \sqrt { 3 3 8 . 2 4 } t _ { m - 2 , 0 . 9 7 5 } = - 1 . 0 3 \pm 3 8 . 0 5
$$

and

$$
m _ { 2 } = 1 0 . 0 9 \pm \sqrt { 0 . 0 8 } t _ { m - 2 , 0 . 9 7 5 } = 1 0 . 0 9 \pm 0 . 5 9 .
$$

Since the actual standard deviation of the measurement errors is unknown,we cannot perform a $\chi ^ { 2 }$ test of goodness-of-fit. However, we can still examine the residuals. Figure 2.4 shows the residuals. It is clear that although they appear to be random, the standard deviation seems to increase as $_ x$ and $\gamma$ increase. This is a common phenomenon in linear regression， called a proportional effect. One possible way that such an effect might occur is if the sizes of the measurement errors were proportional to the measurement magnitude due to characteristics of the instrument used.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/c17b7badf4a9b157e9f5102dbf574ad77bc82d47bb677bc5588e6bdbe435aed3.jpg)  
Figure 2.4 Unweighted residuals for Example 2.3.

For independent errors where the standard deviations of the data points are proportional to the observation, we can rescale the system of equations (2.67) by dividing each equation by $\gamma _ { i }$ ,to obtain

$$
\mathbf { G } _ { u } \mathbf { m } = \mathbf { y } _ { u } .
$$

If statistical assumptions are correct, (.72) has a least squares solution that approximates (2.17). We obtain a revised least squares estimate of

$$
\gamma _ { i } = - 1 2 . 2 4 + 1 0 . 2 5 x _ { i }
$$

with $9 5 \%$ parameter confidence intervals, evaluated as in (2.7O) and (2.71), of

$$
m _ { 1 } = - 1 2 . 2 4 \pm 2 2 . 3 9
$$

and

$$
m _ { 2 } = 1 0 . 2 5 \pm 0 . 4 7 .
$$

Figure 2.5 shows the data and least squares fit. Figure 2.6 shows the scaled residuals. Note that there is now no obvious trend in the magnitude of the residuals as $_ x$ and $\gamma$ increase,as there was in Figure 2.4. The estimated standard deviation is O.O45,or $4 . 5 \%$ of the $\gamma$ value. In fact, these data were generated according to the true model $\gamma _ { i } = 1 0 x _ { i } + 0$ ， using standard deviations for the measurement errors that were $5 \%$ of the $\gamma$ value.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/4da9410c14f96e20557532581022c2a7345a402e3ef613aa6d55f4ca81d5db32.jpg)  
Figure 2.5 Data for Example 2.3,and corresponding linear regression line, weighted system.   
Figure 2.6 Weighted residuals for Example 2.3.

# 2.5. $L _ { 1 }$ REGRESSION

Least squares solutions are highly susceptible to even small numbers of discordant observations,or outliers. Outliers are data points that are highly inconsistent with the other data. Outliers may arise from procedural measurement error, for example from incorrectly recording the position of a decimal point in an observation or from instrumental glitches. Outliers should be investigated carefully, since the data may actually be showing us that the form of the mathematical model that we are trying to fit is incorect. However, if we conclude that there are only a small number of outliers in the data due to incorrect measurements,we need to analyze the data in a way that minimizes their effect on the estimated model.

We can readily appreciate the strong effect of outliers on least squares solutions from a maximum likelihood perspective by noting the very rapid fall-off of the tails of the normal distribution. For example, the probability of a single data point drawn from a normal distribution being more than five standard deviations away from its expected value is less than 1 in 1 million:

$$
P ( | X - E [ X ] | \geq 5 \sigma ) = \frac { 2 } { \sqrt { 2 \pi } } \intop _ { 5 } ^ { \infty } e ^ { - \frac { 1 } { 2 } x ^ { 2 } } d x \approx 6 \times 1 0 ^ { - 7 } .
$$

If an outlier occurs in the data set due to a non-normal error process,the least squares solution will go to great lengths to accommodate it,and thus prevent its corresponding factor in the total likelihood product (2.9) from being vanishingly small.

As an alternative to least squares,consider the solution that minimizes the 1-norm of the residual vector,

$$
\mu ^ { ( 1 ) } = \sum _ { i = 1 } ^ { m } \frac { | d _ { i } - ( \mathbf { G m } ) _ { i } | } { \sigma _ { i } } = \| \mathbf { d } _ { w } - \mathbf { G } _ { w } \mathbf { m } \| _ { 1 } .
$$

The 1-norm solution, $\mathbf { m } _ { L _ { 1 } }$ ,will be more outlier resistant, or robust, than the least squares solution, ${ \bf m } _ { L _ { 2 } }$ ,because (2.77) does not square each of the terms in the misfit measure,as (2.12) does. The 1-norm solution $\mathbf { m } _ { L _ { 1 } }$ also has a maximum likelihood interpretation; it is the maximum likelihood estimator for data with errors distributed according to a double-sided exponential distribution (Appendix B),

$$
f ( x ) = { \frac { 1 } { \sigma { \sqrt { 2 } } } } e ^ { - { \sqrt { 2 } } | x - \mu | / \sigma } .
$$

Data sets distributed as (2.78) are unusual. Nevertheless, it is often worthwhile to consider a solution where (2.77) is minimized rather than (2.12)，even if most of the measurement errors are normally distributed, should there be reason to suspect the presence of outliers. This solution strategy may be useful if the data outliers occur for reasons that do not undercut our belief that the mathematical model is otherwise correct.

# Example 2.4

We can demonstrate the advantages of 1-norm minimization using the quadratic regres-sion example discussed earlier. Figure 2.7 shows the original sequence of independent data points with unit standard deviations, except one of the points $( d _ { 4 } )$ is now an outlier with respect to a mathematical model of the form (2.32). It is the original data point with $2 0 0 ~ \mathrm { m }$ subtracted from it. The least squares model for this data set is

$$
\mathbf { m } _ { L _ { 2 } } = [ 2 6 . 4 \mathrm { ~ m } , 7 5 . 6 \mathrm { ~ m } / \mathrm { s } , 4 . 8 6 \mathrm { ~ m } / \mathrm { s } ^ { 2 } ] ^ { T } .
$$

The least squares solution is skewed away from the majority of data points in trying to accommodate the outlier and is a poor estimate of the true model. We can also see that (2.79) fails to fit these data acceptably because of its huge $\chi ^ { 2 }$ value $( \approx 4 8 9 )$ . This is clearly astronomically out of bounds for a problem with 7 degrees of freedom, where the $\chi ^ { 2 }$ value should not be far from 7. The corresponding $p .$ -value for $\chi ^ { 2 } = 4 8 9$ is effectively zero.

The upper curve in Figure 2.7

$$
\mathbf { m } _ { L _ { 1 } } = [ 1 7 . 6 ~ \mathrm { m } , 9 6 . 4 ~ \mathrm { m } / \mathrm { s } , 9 . 3 1 ~ \mathrm { m } / \mathrm { s } ^ { 2 } ] ^ { T }
$$

is obtained using the 1-norm solution that minimizes (2.77). The data prediction from (2.80) faithfully fits the quadratic trend for the majority of the data points and is only slightly influenced by the outlier at $t = 4$ .It is also much closer than (2.79) to the true model (2.33),and to the least squares model for the data set without the outlier (2.36).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0001_pages_0001-0070/auto/images/18e2aca63dd19c83cd3b2a90a00b1c9612b0e5368491bd43b304b9b0ed775b44.jpg)  
Figure 2.7 $L _ { 1 }$ (solid) and $L _ { 2 }$ (dashed) solutions for a parabolic data set with an outlier at $t = 4 \ s$

In examining the differences between $2 \mathrm { - }$ and 1-norm models, it is instructive to con-sider the almost trivial regression problem of estimating the value of a single parameter from repeated measurements. The system of equations $\mathbf { G m } = \mathbf { d }$ is

$$
\begin{array} { r } { \left[ 1 \atop 1 \right] \qquad \left[ d _ { 1 } \atop d _ { 2 } \right] } \\ { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } \\ { \mathrm { ~ . ~ } } \end{array}
$$

where $\mathbf { m }$ is the 1 by 1 vector containing the parameter that we wish to estimate.

The least squares solution to (2.81) can be seen from the normal equations (A.73) to be simply the observational average

$$
\mathbf { m } _ { L _ { 2 } } = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { d } = m ^ { - 1 } \sum _ { i = 1 } ^ { m } d _ { i } .
$$

Finding the 1-norm solution is more complicated. The problem is that the 1-norm of the residual vector,

$$
f ( \mathbf { m } ) = \| \mathbf { d - G m } \| _ { 1 } = \sum _ { i = 1 } ^ { m } | d _ { i } - ( \mathbf { G m } ) _ { i } | ,
$$

is a nondifferentiable function of $\mathbf { m }$ at each point where $( \mathbf { G m } ) _ { i } = d _ { i }$ . The good news is that $f ( \mathbf { m } )$ is a convex function of $\mathbf { m }$ . Thus any local minimum point is also a global minimum point. We can proceed by finding $f ^ { \prime } ( \mathbf { m } )$ at those points where it is defined, and then separately consider the points at which the derivative is not defined. Every minimum point must either have $f ^ { \prime } ( \mathbf { m } )$ undefined or $f ^ { \prime } ( { \mathbf { m } } ) = 0$

At those points where $f ^ { \prime } ( \mathbf { m } )$ is defined, it is given by

$$
f ^ { \prime } ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } \operatorname { s g n } ( d _ { i } - \mathbf { m } ) .
$$

where the signum function, $\operatorname { s g n } ( x )$ ,is $- 1$ if its argument is negative, 1 if its argument is positive,and O if its argument is zero.The derivative (2.84) is zero when exactly half of the data are less than $\mathbf { m }$ and half of the data are greater than m. Of course, this can only happen when the number of observations, $m$ ，is even.In this case,any value of m lying between the two middle observations is a 1-norm solution. When there are an odd number of data,the median data point is the unique 1-norm solution. Even an extreme outlier will not have a large effect on the median of an otherwise clustered set of observations.This illuminates the robustness of the 1-norm solution.

The general problem of finding solutions that minimize $\lVert \mathbf { d } - \mathbf { G m } \rVert _ { 1 }$ is a bit complicated. One practical method is iteratively reweighted least squares, or IRLS [138]. The IRLS algorithm solves a sequence of weighted least squares problems whose solutions converge to a 1-norm minimizing solution. Beginning with the residual vector

$$
\mathbf { r } = \mathbf { d } - \mathbf { G m } ,
$$

we want to minimize

$$
f ( \mathbf { m } ) = \| \mathbf { r } \| _ { 1 } = \sum _ { i = 1 } ^ { m } | r _ { i } | .
$$

The function in (.86), like the function in (2.83),is nondifferentiable at any point where one of the elements of $\mathbf { r }$ is zero. Ignoring this issue for a moment, we can go ahead and compute the derivatives of $f$ at other points:

$$
{ \frac { \partial f ( { \mathbf { m } } ) } { \partial m _ { k } } } = \sum _ { i = 1 } ^ { m } { \frac { \partial | r _ { i } | } { \partial m _ { k } } } = - \sum _ { i = 1 } ^ { m } G _ { i , k } \operatorname { s g n } ( r _ { i } ) .
$$

Writing $\operatorname { s g n } ( r _ { i } )$ as $r _ { i } / | r _ { i } |$ gives

$$
\frac { \partial f ( \mathbf { m } ) } { \partial m _ { k } } = - \sum _ { i = 1 } ^ { m } G _ { i , k } \frac { 1 } { | r _ { i } | } r _ { i } .
$$

The gradient of $f$ is

$$
\nabla f ( \mathbf { m } ) = - \mathbf { G } ^ { T } \mathbf { R } \mathbf { r } = - \mathbf { G } ^ { T } \mathbf { R } ( \mathbf { d } - \mathbf { G } \mathbf { m } ) ,
$$

where $\mathbf { R }$ is a diagonal weighting matrix with diagonal elements that are the absolute values of the reciprocals of the residuals, so that

$$
R _ { i , i } = 1 / | r _ { i } | .
$$

To find the 1-norm minimizing solution, we solve $\nabla f ( \mathbf { m } ) = \mathbf { 0 }$ ,which gives

$$
\mathbf { G } ^ { T } \mathbf { R } ( \mathbf { d } - \mathbf { G m } ) = \mathbf { 0 }
$$

or

$$
\mathbf { G } ^ { T } \mathbf { R } \mathbf { G } \mathbf { m } = \mathbf { G } ^ { T } \mathbf { R } \mathbf { d } .
$$

Because $\mathbf { R }$ is a nonlinear function of $\mathbf { m }$ ， (2.92) is a nonlinear system of equations that we cannot solve directly. IRLS is an iterative algorithm to find the appropriate weights and solve the system. The algorithm begins with the least squares solution $\mathbf { m } ^ { 0 } =$ ${ \bf m } _ { L _ { 2 } }$ . We calculate the corresponding residual vector $\mathbf { r } ^ { 0 } = \mathbf { d } - \mathbf { G m } ^ { 0 }$ to construct the weighting matrix $\mathbf { R }$ using (2.9O). We then solve (2.92) to obtain a new model $\mathbf { m } ^ { 1 }$ and associated residual vector $\mathbf { r } ^ { 1 }$ . The process is repeated until the model and residual vectors converge. A typical rule is to stop the iteration when

$$
\frac { \| \mathbf { m } ^ { k + 1 } - \mathbf { m } ^ { k } \| _ { 2 } } { 1 + \| \mathbf { m } ^ { k + 1 } \| _ { 2 } } < \tau
$$

for some tolerance $\tau$

If any element of the residual vector becomes zero, then (2.9O) becomes undefined. However, this problem can be easily addressed by selectinga tolerance $\epsilon$ below which we consider the residuals to be effectively zero. If $| r _ { i } | < \epsilon$ , then we set $R _ { i , i } = 1 / \epsilon$ . With this modification it can be shown that this procedure willalways converge to an approximate 1-norm minimizing solution.

As with the $\chi ^ { 2 }$ misfit measure for least squares solutions, there is a corresponding $p -$ value that can be evaluated under the assumption of normal data errors for the assessment of 1-norm solutions [127]. Let

$$
\mu _ { \mathrm { o b s } } ^ { ( 1 ) } = \| \mathbf { G } \mathbf { m } _ { L _ { 1 } } - \mathbf { d } \| _ { 1 } .
$$

For an observed 1-norm misfit measure (2.94),the probability that a worse misfit could have occurred, given independent and normally distributed data and $\nu$ degrees of freedom, is approximately given by

$$
p ^ { ( 1 ) } ( x , \nu ) = P \left( \mu ^ { ( 1 ) } > \mu _ { \mathrm { o b s } } ^ { ( 1 ) } \right) = 1 - S ( x ) + \frac { \gamma Z ^ { ( 2 ) } ( x ) } { 6 } ,
$$

where

$$
S ( x ) = \frac { 1 } { \sigma _ { 1 } \sqrt { 2 \pi } } \int _ { - \infty } ^ { x } e ^ { - \frac { \xi ^ { 2 } } { 2 \sigma _ { 1 } ^ { 2 } } } d \xi
$$

$$
\sigma _ { 1 } = \sqrt { ( 1 - 2 / \pi ) \nu }
$$

$$
\gamma = \frac { 2 - \pi / 2 } { ( \pi / 2 - 1 ) ^ { 3 / 2 } \nu ^ { \frac { 1 } { 2 } } }
$$

$$
Z ^ { ( 2 ) } ( x ) = \frac { x ^ { 2 } - 1 } { \sqrt { 2 \pi } } e ^ { - \frac { x ^ { 2 } } { 2 } }
$$

$$
x = \frac { \mu ^ { ( 1 ) } - \sqrt { 2 / \pi } \nu } { \sigma _ { 1 } } .
$$

# 2.6. MONTE CARLO ERROR PROPAGATION

For solution techniques that are nonlinear and/or algorithmic, such as IRLS, there is typically no simple way to propagate uncertainties in the data to uncertainties in the

estimated model parameters. In such cases, one can apply Monte Carlo error propagation techniques, in which we simulate a collection of noisy data vectors and then examine the statistics of the resulting ensemble of models.

For $L _ { 1 }$ minimizing solutions,we can obtain an approximate covariance matrix by first forward-propagating the solution into an assumed noise-free baseline data vector

$$
\mathbf { G m } _ { L _ { 1 } } = \mathbf { d } _ { b } .
$$

We next re-solve the IRLS problem many times for independent data realizations, obtaining a suite of $q \ 1$ -norm solutions to

$$
\mathbf { G m } _ { L _ { 1 } , i } = \mathbf { d } _ { b } + \pmb { \eta } _ { i }
$$

where $\pmb { \eta } _ { i }$ is the ith noise vector realization. If $\mathbf { A }$ is the $q$ by $n$ matrix where the ith row contains the difference between the ith model estimate and the average model,

$$
\mathbf { A } _ { i , \cdot } = \mathbf { m } _ { L _ { 1 } , i } ^ { T } - \bar { \mathbf { m } } _ { L _ { 1 } } ^ { T } ,
$$

then an empirical estimate of the covariance matrix is

$$
\mathrm { C o v } ( \mathbf { m } _ { L _ { 1 } } ) = \frac { \mathbf { A } ^ { T } \mathbf { A } } { q } .
$$

# Example 2.5

Recall Example 2.4. An estimate of $\mathrm { C o v } ( \mathbf { m } _ { L _ { 1 } } )$ ）using 10,000 iterations of the Monte Carlo procedure is

$$
\mathrm { C o v } ( \mathbf { m } _ { L _ { 1 } } ) = \left[ \begin{array} { r r r } { 1 2 4 . 1 } & { - 4 5 . 4 7 } & { - 7 . 0 5 9 } \\ { - 4 5 . 4 7 } & { 2 0 . 5 4 } & { 3 . 5 0 1 } \\ { - 7 . 0 5 9 } & { 3 . 5 0 1 } & { 0 . 6 3 1 6 } \end{array} \right] ,
$$

which contains elements that are about 1.4 times as large as those of the least squares solution (2.37).Unlike least squares solutions, model parameters obtained with the IRLS algorithm will not generally be normally distributed. However, we can com-pute approximate confidence intervals for the parameters from the covariance matrix diagonal, provided that analysis of the obtained Monte Carlo solution parameter distributions reveals that they are approximately normally distributed. Such an analysis can be performed by examining the parameter distributions with a $\mathbf { Q - } \mathbf { Q }$ plot (Appendix B) and/or generating an elipsoidal confidence boundary under normal assumptions and counting the proportion of points within the ellpsoid to check for consistency. In this example, $Q - Q$ plots reveal the estimates to be approximately normally distributed, and calculating corresponding $9 5 \%$ confidence intervals from (2.105) using (2.30) gives

$$
\mathbf { m } _ { L _ { 1 } } = [ 1 7 . 6 \pm 2 1 . 8 \mathrm { m } , 9 6 . 4 \pm 8 . 8 8 \mathrm { m } / \mathrm { s } , 9 . 3 1 \pm 1 . 5 6 \mathrm { m } / \mathrm { s } ^ { 2 } ] ^ { T } .
$$

# 2.7. EXERCISES

1. A seismic profiling experiment is performed where the first arrival times of seismic energy from a mid-crustal refractor are observed at distances (in kilometers) of

$$
\mathbf { x } = { \left[ \begin{array} { l } { 6 . 0 0 0 0 } \\ { 1 0 . 1 3 3 3 } \\ { 1 4 . 2 6 6 7 } \\ { 1 8 . 4 0 0 0 } \\ { 2 2 . 5 3 3 3 } \\ { 2 6 . 6 6 6 7 } \end{array} \right] }
$$

from the source,and are found to be (in seconds after the source origin time)

$$
\mathbf { t } = { \left[ \begin{array} { l } { 3 . 4 9 3 5 } \\ { 4 . 2 8 5 3 } \\ { 5 . 1 3 7 4 } \\ { 5 . 8 1 8 1 } \\ { 6 . 8 6 3 2 } \\ { 8 . 1 8 4 1 } \end{array} \right] } .
$$

These vectors can also be found in the MATLAB data file profile.mat. A two-layer, flat Earth structure gives the mathematical model

$$
t _ { i } = t _ { 0 } + s _ { 2 } x _ { i } ,
$$

where the intercept time, $t _ { \mathrm { 0 } }$ , depends on the thickness and slowness of the upper layer, and $s _ { 2 }$ is the slowness of the lower layer. The estimated noise in the first arrival time measurements is believed to be independent and normally distributed with expected value O and standard deviation $\sigma = 0 . 1 \mathrm { ~ s ~ }$

a.Find the least squares solution for the model parameters $t _ { \mathrm { 0 } }$ and $s _ { 2 }$ . Plot the data, the fitted model,and the residuals.   
b. Calculate and comment on the model parameter correlation matrix (e.g., 2.43). How are the correlations manifested in the general appearance of the error ellipsoid in $( t _ { 0 } , s _ { 2 } )$ space?   
c.Plot the error ellipsoid in the $( t _ { 0 } , s _ { 2 } )$ plane and calculate conservative $9 5 \%$ confidence intervals for $t _ { \mathrm { 0 } }$ and $s _ { 2 }$ for the appropriate value of $\Delta ^ { 2 }$ . Hint: The following MATLAB function will plot a two-dimensional covariance ellpse about the model parameters,where $\textrm { C }$ is the covariance matrix, DELTA2 is $\Delta ^ { 2 }$ ，and m is the 2-vector of model parameters. %set the number of points on the ellipse to generate and plot function plot_ellipse(DELTA2,C,m)   
$\mathsf { n } { = } 1 0 0$ ；   
%construct a vector of n equally-spaced angles from $( 0 , 2 \star \mathsf { p i }$ ） theta $= ^ { \cdot }$ linspace(0,2\*pi,n)';   
%corresponding unit vector   
xhat $=$ [cos(theta）,sin(theta)];   
Cinv $=$ inv(C);   
%preallocate output array   
$\gamma =$ zeros(n,2);   
for $\dot { 7 } = 1$ :n   
%store each （x,y） pair on the confidence ellipse   
%in the corresponding row of r   
$\Upsilon \left( \mathrm { ~ i ~ } , : \right) = \varsigma$ qrt(DELTA2/(xhat(i,:)\*Cinv\*xhat(i,:)'))\*xhat(i,:); end   
plot $( \mathsf { m } ( \mathrm { ~ 1 ~ } ) + \mathsf { r } ( \mathrm { ~ : ~ } , \mathrm { ~ 1 ~ } )$ ， $\mathfrak { m } ( 2 ) + \mathfrak { r } ( : , 2 ) \ )$ ；   
axis equal

d. Evaluate the $p .$ -value for this model. You may find the library function chi2cdf to be useful here.

e. Evaluate the value of $\chi ^ { 2 }$ for 1000 Monte Carlo simulations using the data prediction from your model perturbed by noise that is consistent with the data assumptions. Compare a histogram of these $\chi ^ { 2 }$ values with the theoretical $\chi ^ { 2 }$ distribution for the correct number of degrees of freedom. You may find the library function chi2pdf to be useful here.

2. In this chapter we have largely assumed that the data errors are independent. Suppose instead that the data errors have an MVN distribution with expected value O and a covariance matrix $\mathbf { C } _ { D }$ . It can be shown that the likelihood function is then

$$
L ( \mathbf { m } | \mathbf { d } ) = \frac { 1 } { ( 2 \pi ) ^ { m / 2 } } \frac { 1 } { \sqrt { \operatorname* { d e t } ( \mathbf { C } _ { D } ) } } e ^ { - ( \mathbf { G } \mathbf { m } - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) / 2 } .
$$

a. Show that the maximum likelihood estimate can be obtained by solving the minimization problem,

$$
\operatorname* { m i n } ( \mathbf { G m } - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G m } - \mathbf { d } ) .
$$

b. Show that (2.111) can be solved using the system of equations

$$
\mathbf { G } ^ { T } \mathbf { C } _ { D } ^ { - 1 } \mathbf { G m } = \mathbf { G } ^ { T } \mathbf { C } _ { D } ^ { - 1 } \mathbf { d } .
$$

c. Show that (2.111) is equivalent to the linear least squares problem

$$
\operatorname* { m i n } { \bf \| C } _ { D } ^ { - 1 / 2 } { \bf G m - C } _ { D } ^ { - 1 / 2 } { \bf d } \| _ { 2 } ,
$$

where $\mathbf { C } _ { D } ^ { - 1 / 2 }$ is the matrix square roo of $\mathbf { C } _ { D } ^ { - 1 }$

d. The Cholesky factorization of $\mathbf { C } _ { D } ^ { - 1 }$ can also be used instead of the matrix square root. Show that (2.111) is equivalent to the linear least squares problem

$$
\operatorname* { m i n } \ \| \mathbf { R G m - R d } \| _ { 2 } ,
$$

where $\mathbf { R }$ is the Cholesky factor of $\mathbf { C } _ { D } ^ { - 1 }$

3.Use MATLAB to generate 1O,OOO realizations of a data set of $m = 5$ points $\mathbf { d } = a +$ $b \mathbf { x } + \pmb { \eta }$ ，where $\mathbf { x } = [ 1 , 2 , 3 , 4 , 5 ] ^ { T }$ ,the $n = 2$ true model parameters are $a = b = 1$ ， and $\pmb { \eta }$ is an $m$ -element vector of independent $N ( 0 , 1 )$ noise.

a. Assuming that the noise standard deviation is known a priori to be 1,solve for the parameters $a$ and $b$ using least squares for each realization and histogram them in 100 bins.

b. Calculate the parameter covariance matrix, $\mathbf { C } = \sigma ^ { 2 } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 }$ ， assuming independent $N ( 0 , 1 )$ data errors,and give standard deviations, $\sigma _ { a }$ and $\sigma _ { b }$ ,for your estimates of $a$ and $b$ estimated from $\mathbf { C }$

c. Calculate standardized parameter estimates

$$
a ^ { \prime } = \frac { a - 1 } { \sqrt { C _ { 1 , 1 } } }
$$

and

$$
b ^ { \prime } = \frac { b - 1 } { \sqrt { C _ { 2 , 2 } } }
$$

for your solutions for $a$ and $b$ . Demonstrate using a $Q - Q$ plot (Appendix B) that your estimates for $a ^ { \prime }$ and $b ^ { \prime }$ are distributed as $N ( 0 , 1 )$

d. Show, using a $Q - Q$ plot, that the squared residual lengths

$$
\left\| \mathbf { r } \right\| _ { 2 } ^ { 2 } = \left\| \mathbf { d } - \mathbf { G m } \right\| _ { 2 } ^ { 2 }
$$

for your solutions in (a) are distributed as $\chi ^ { 2 }$ with $m - n = \nu = 3$ degrees of freedom.

e. Assume that the noise standard deviation for the synthetic data set is not known, and instead estimate it for each realization, $k$ as

$$
s _ { k } = \sqrt { \frac { 1 } { n - m } \sum _ { i = 1 } ^ { m } r _ { i } ^ { 2 } } .
$$

Histogram your standardized solutions

$$
a ^ { \prime } = \frac { a - \overline { { a } } } { \sqrt { C _ { 1 , 1 } ^ { \prime } } }
$$

and

$$
b ^ { \prime } = \frac { b - \bar { b } } { \sqrt { C _ { 2 , 2 } ^ { \prime } } } ,
$$

where $\mathbf { C } ^ { \prime } = s _ { k } ^ { 2 } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 }$ is the covariance matrix estimation for the kth realization.

f. Demonstrate using a $Q { \mathrm { - } } Q$ plot that your estimates for $a ^ { \prime }$ and $b ^ { \prime }$ are distributed as the Student's $t$ distribution with $\nu = 3$ degrees of freedom.

4. Suppose that we analyze a large number of data sets $\mathbf { d }$ in a linear regression problem and compute $p .$ values for each data set. The $\chi _ { \mathrm { o b s } } ^ { 2 }$ values should be distributed according to a $\chi ^ { 2 }$ distribution with $m - n$ degrees of freedom. Show that the corresponding $p$ -values will be uniformly distributed between O and 1.

5. Use linear regression to fit a polynomial of the form

$$
\gamma _ { i } = a _ { 0 } + a _ { 1 } x _ { i } + a _ { 2 } x _ { i } ^ { 2 } + . ~ . ~ . + a _ { 1 9 } x _ { i } ^ { 1 9 }
$$

to the noise-free data points

$$
( x _ { i } , \gamma _ { i } ) = ( - 0 . 9 5 , - 0 . 9 5 ) , ( - 0 . 8 5 , - 0 . 8 5 ) , . . . , ( 0 . 9 5 , 0 . 9 5 ) .
$$

Use the normal equations to solve the least squares problem.

Plot the data and your fitted model, and list the parameters, $a _ { i }$ ，obtained in your regression. Clearly, the correct solution has $a _ { 1 } = 1$ , and all other $a _ { i } = 0$ . Explain why your answer differs.

# 2.8.NOTES AND FURTHER READING

Linear regression is a major subfield within statistics,and there are literally hundreds of associated textbooks. Many of these references focus on applications of linear regression in the social sciences. In such applications, the primary focus is often on determining which variables have an effect on response variables of interest (rather than on estimating parameter values for a predetermined model). In this context it is important to compare alternative regresson models and to test the hypothesis that a predictor variable has a nonzero coefficient in the regression model. Since we normally know which predictor variables are important in the physical sciences, the approach commonly differs.Useful linear regression references from the standpoint of estimating parameters in the context considered here include [40, 113].

Robust statistical methods are an important topic.Huber discusses a variety of robust statistical procedures [77]. The computational problem of computing a 1-norm solution has been extensively researched. Techniques for 1-norm minimization include methods based on the simplex method for linear programming, interior point methods,and iteratively reweighted least squares [6,32,130,138]. The IRLS method is the simplest to implement, but interior point methods can be the most efficient approaches for very large problems. Watson reviews the history of methods for finding $p .$ -norm solutions including the 1-norm case [171].

We have assumed that $\mathbf { G }$ is known exactly. In some cases elements of this matrix might be subject to measurement error. This problem has been studied as the total least squares problem [78]. An alternative approach to least squares problems with uncertainties in $\mathbf { G }$ that has recently received considerable attention is called robust least squares [11, 43].

# Rank Deficiency and Ill-Conditioning

# Synopsis

The characteristics of rank-deficient and il-conditioned linear systems of equations are explored using the singular value decomposition. The connection between model and data null spaces and solution uniqueness and ability to fit data is examined. Model and data resolution matrices are defined. The relationship between singular value size and singular vector roughness and its connection to the effect of noise on solutions are discussed in the context of the fundamental trade-off between model resolution and instability. Specific manifestations of these issues in rank-deficient and il-conditioned discrete problems are shown in several examples.

# 3.1.THE SVD AND THE GENERALIZED INVERSE

A method of analyzing and solving least squares problems that is of particular interest in ill-conditioned and/or rank-deficient systems is the singular value decomposition, or SVD. In the SVD [53, 93, 152], an $m$ by $n$ matrix $\mathbf { G }$ is factored into

$$
\mathbf { G } = \mathbf { U } \mathbf { S } \mathbf { V } ^ { T } ,
$$

where

： $\mathbf { U }$ is an $m$ by $m$ orthogonal matrix with columns that are unit basis vectors spanning the data space, $R ^ { m }$   
. $\mathbf { v }$ is an $n$ by $n$ orthogonal matrix with columns that are basis vectors spanning the model space, $R ^ { n }$   
$\mathbf { s }$ is an $m$ by $n$ diagonal matrix with diagonal elements called singular values.

The SVD matrices can be computed in MATLAB with the svd command. It can be shown that every matrix has a singular value decomposition [53].

The singular values along the diagonal of S are customarily arrnged in decreasing size, $s _ { 1 } \geq s _ { 2 } \geq . ~ . ~ . \geq s _ { \operatorname* { m i n } ( m , n ) } \geq 0 .$ Note that some of the singular values may be zero. If only the first $p$ singular values are nonzero, we can partition $\mathbf { s }$ as

$$
\begin{array} { r } { \mathbf { S } = \left[ \begin{array} { l l } { \mathbf { S } _ { p } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { 0 } } \end{array} \right] } \end{array}
$$

where $\mathbf { S } _ { p }$ is a $p$ by $p$ diagonal matrix composed of the positive singular values. Expanding the SVD representation of $\mathbf { G }$ in terms of the columns of $\mathbf { U }$ and $\mathbf { v }$ gives

$$
\begin{array} { r l } & { \mathbf { G } = \left[ \mathbf { U } _ { \cdot , 1 } , \mathbf { U } _ { \cdot , 2 } , \mathbf { \Omega } , \mathbf { \Omega } , \mathbf { \Lambda } , \mathbf { \Lambda } , \mathbf { U } _ { \cdot , m } \right] \left[ \mathbf { S } _ { p } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { 0 } \right] \left[ \mathbf { V } _ { \cdot , 1 } , \mathbf { V } _ { \cdot , 2 } , \mathbf { \Omega } , \mathbf { \Lambda } , \mathbf { \Lambda } , \mathbf { V } _ { \cdot , n } \right] ^ { T } } \\ & { \mathbf { \Lambda } = \left[ \mathbf { U } _ { p } , \mathbf { U } _ { 0 } \right] \left[ \begin{array} { l l } { \mathbf { S } _ { p } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { 0 } } \end{array} \right] \left[ \mathbf { V } _ { p } , \mathbf { V } _ { 0 } \right] ^ { T } \phantom { \left[ \mathbf { V } _ { \cdot , 1 } , \mathbf { V } _ { \cdot , 2 } , \mathbf { \Omega } , \mathbf { \Lambda } , \mathbf { \Lambda } , \mathbf { V } _ { \cdot , n } \right] ^ { T } } } \end{array}
$$

where $\mathbf { U } _ { p }$ denotes the first $p$ columns of U, $\mathbf { U } _ { 0 }$ denotes the last $m - p$ columns of $\mathbf { U }$ ， $\mathbf { V } _ { p }$ denotes the first $p$ columns of $\mathbf { v }$ ,and $\mathbf { V } _ { 0 }$ denotes the last $n - p$ columns of $\mathbf { v }$ Because the last $m - p$ columns of $\mathbf { U }$ and the last $n - p$ columns of $\mathbf { v }$ in (3.4) are multiplied by zeros in $\mathbf { s }$ , we can simplify the SVD of $\mathbf { G }$ into its compact form

$$
\mathbf { G } = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } .
$$

For any vector $\mathbf { y }$ in the range of $\mathbf { G }$ ， applying (3.5) gives

$$
\begin{array} { r } { \mathbf { y } = \mathbf { G } \mathbf { x } \quad } \\ { = \mathbf { U } _ { p } \Big ( \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { x } \Big ) . } \end{array}
$$

Thus every vector in $R ( \mathbf G )$ can be written as $\mathbf { y } = \mathbf { U } _ { p } \mathbf { z }$ where $\begin{array} { r } { \mathbf { z } = \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { x } } \end{array}$ . Writing out this matrix-vector multiplication,we see that any vector $\mathbf { y }$ in $R ( \mathbf G )$ can be written as a linear combination of the columns of $\mathbf { U } _ { p }$

$$
\mathbf { y } = \sum _ { i = 1 } ^ { p } z _ { i } \mathbf { U } . _ { , i } .
$$

The columns of $\mathbf { U } _ { p }$ span $R ( \mathbf G )$ ,are linearly independent,and form an orthonormal basis for $R ( \mathbf G )$ . Because this orthonormal basis has $p$ vectors, $\operatorname { r a n k } ( \mathbf G ) = p$

Since $\mathbf { U }$ is an orthogonal matrix, the columns of $\mathbf { U }$ form an orthonormal basis for $R ^ { m }$ . By Theorem A.5, $N ( { \bf G } ^ { T } ) + R ( { \bf G } ) = R ^ { m }$ ， so the remaining $m - p$ columns of $\mathbf { U } _ { 0 }$ form an orthonormal basis for the null space of $\mathbf { G } ^ { T }$ . Note that because the null space basis is nonunique,and because basis vectors contain an inherent sign ambiguity, basis vectors calculated and illustrated in this chapter and elsewhere may not match ones calculated locally using the provided MATLAB code. We will sometimes refer to $N ( \mathbf G ^ { T } )$ as the data null space. Similarly because $\mathbf G ^ { T } = \mathbf V _ { p } \mathbf S _ { p } \mathbf U _ { p } ^ { T }$ , the columns of $\mathbf { V } _ { p }$ form an orthonormal basis for $R ( \mathbf { G } ^ { T } )$ and the columns of $\mathbf { V } _ { 0 }$ form an orthonormal basis for $N ( \mathbf G )$ . We will sometimes refer to $N ( \mathbf G )$ as the model null space.

Two other important SVD properties are similar to properties of eigenvalues and eigenvectors. See Section A.6. Because the columns of $\mathbf { v }$ are orthonormal,

$$
\mathbf { V } ^ { T } \mathbf { V } _ { \cdot , i } = \mathbf { e } _ { i } .
$$

Thus

$$
\begin{array} { r l } & { \mathbf { G } \mathbf { V } _ { \cdot , i } = \mathbf { U S V } ^ { T } \mathbf { V } _ { \cdot , i } } \\ & { \qquad = \mathbf { U S e } _ { i } } \\ & { \qquad = s _ { i } \mathbf { U } _ { \cdot , i } , } \end{array}
$$

and, similarly,

$$
\begin{array} { r l } & { \mathbf { G } ^ { T } \mathbf { U } . , i = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { U } . , i } \\ & { \qquad = \mathbf { V } \mathbf { S } ^ { T } \mathbf { e } _ { i } } \\ & { \qquad = s _ { i } \mathbf { V } . , i . } \end{array}
$$

There is a connection between the singular values of $\mathbf { G }$ and the eigenvalues of $\mathbf { G } \mathbf { G } ^ { T }$ and $\mathbf { G } ^ { T } \mathbf { G }$

$$
\begin{array} { r } { \mathbf { G } \mathbf { G } ^ { T } \mathbf { U } _ { \cdot , i } = \mathbf { G } s _ { i } \mathbf { V } _ { \cdot , i } } \\ { = s _ { i } \mathbf { G } \mathbf { V } _ { \cdot , i } } \\ { = s _ { i } ^ { 2 } \mathbf { U } _ { \cdot , i } . } \end{array}
$$

Similarly,

$$
\mathbf { G } ^ { T } \mathbf { G } \mathbf { V } _ { \cdot , i } = s _ { i } ^ { 2 } \mathbf { V } _ { \cdot , i } .
$$

These relations show that we could, in theory, compute the SVD by finding the eigenvalues and eigenvectors of $\mathbf { G } ^ { T } \mathbf { G }$ and $\mathbf { G } \mathbf { G } ^ { T }$ . In practice，more efficient specialized algorithms are used [38, 53, 164].

The SVD can be used to compute a generalized inverse of $\mathbf { G }$ ，called the Moore-Penrose pseudoinverse, because it has desirable inverse properties originally identified by Moore and Penrose [11O, 129]. The generalized inverse is

$$
\mathbf G ^ { \dagger } = \mathbf V _ { p } \mathbf S _ { p } ^ { - 1 } \mathbf U _ { p } ^ { T } .
$$

MATLAB has a pinv command that generates $\mathbf { G } ^ { \dagger }$ . This command allows the user to select a tolerance such that singular values smaller than the tolerance are not included in the computation.

Using (3.2O), we define the pseudoinverse solution to be

$$
\begin{array} { c } { \mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d } } \\ { \mathbf { \Lambda } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } . } \end{array}
$$

Among the desirable properties of (3.22) is that $\mathbf { G } ^ { \dagger }$ ，and hence $\mathbf { m } _ { \dagger }$ ， always exist. In contrast, the inverse of $\mathbf { G } ^ { T } \mathbf { G }$ that appears in the normal equations (2.3) does not exist

when $\mathbf { G }$ is not of full column rank.We will shortly show that $\mathbf { m } _ { \dagger }$ is a least squares solution.

To encapsulate what the SVD tells us about our linear system, $\mathbf { G }$ ，and the corres-ponding generalized inverse system $\mathbf { G } ^ { \dagger }$ , consider four cases:

1. $m = n = p$ .Both the model and data null spaces, $N ( \mathbf G )$ and $N ( \mathbf G ^ { T } )$ , respectively, are trivial. $\mathbf { U } _ { p } = \mathbf { U }$ and $\mathbf { V } _ { p } = \mathbf { V }$ are square orthogonal matrices, so that $\mathbf { U } _ { p } ^ { T } = \mathbf { U } _ { p } ^ { - 1 }$ ,and $\mathbf { V } _ { p } ^ { T } = \mathbf { V } _ { p } ^ { - 1 }$ . Equation (3.22 iues

$$
\begin{array} { r l } & { \mathbf { G } ^ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } } \\ & { \qquad = ( \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } ) ^ { - 1 } } \\ & { \qquad = \mathbf { G } ^ { - 1 } } \end{array}
$$

which is the matrix inverse for a square full rank matrix. The solution is unique, and the data are fit exactly.

2. $m = p$ and $p < n$ $N ( \mathbf G )$ is nontrivial because $p < n$ but $N ( \mathbf G ^ { T } )$ is trvial. $\mathbf { U } _ { p } ^ { T } = \mathbf { U } _ { p } ^ { - 1 }$ and $\mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } = \mathbf { I } _ { p }$ $\mathbf { G }$ applied to the generalized inverse solution gives

$$
\begin{array} { r l } & { \mathbf { G m } _ { \dagger } = \mathbf { G } \mathbf { G } ^ { \dagger } \mathbf { d } } \\ & { \qquad = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { I } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { d } . } \end{array}
$$

The data are fit exactly but the solution is nonunique because of the existence of the nontrivial model null space $N ( \mathbf G )$

If m is any least squares solution, then it satisfies the normal equations. This is shown in Exercise C.5.

$$
( \mathbf { G } ^ { T } \mathbf { G } ) \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } .
$$

Since $\mathbf { m } _ { \dagger }$ is a least squares solution,it also satisfies the normal equations.

$$
( \mathbf { G } ^ { T } \mathbf { G } ) \mathbf { m } _ { \dagger } = \mathbf { G } ^ { T } \mathbf { d } .
$$

Subtracting (3.30) from (3.31), we find that

$$
( \mathbf { G } ^ { T } \mathbf { G } ) ( \mathbf { m } _ { \dagger } - \mathbf { m } ) = \mathbf { 0 } .
$$

Thus $\mathbf { m } _ { \dagger } - \mathbf { m }$ lies in $N ( \mathbf G ^ { T } \mathbf G )$ . It can be shown (see Exercise 13f in Appendix A) that $N ( \mathbf { G } ^ { T } \mathbf { G } ) = N ( \mathbf { G } )$ . This implies that $\mathbf { m } _ { \uparrow } - \mathbf { m }$ lies in $N ( \mathbf G )$

The general solution is thus the sum of $\mathbf { m } _ { \dagger }$ and an arbitrary model null space vector, $\mathbf { m } _ { 0 }$ , that can be written as a linear combination of a set of basis vectors for

$N ( \mathbf G )$ . In terms of the columns of $\mathbf { v }$ ,we can thus write

$$
\begin{array} { c } { { \displaystyle { \bf m } = { \bf m } _ { \dagger } + { \bf m } _ { 0 } } } \\ { { \displaystyle \mathrm {  ~ \Omega ~ } } } \\ { { \displaystyle \mathrm {  ~ \Omega ~ } = { \bf m } _ { \dagger } + \sum _ { i = p + 1 } ^ { n } \alpha _ { i } { \bf V } _ { \cdot , i } } } \end{array}
$$

for any coefficients, $\alpha _ { i }$ .Because the columns of $\mathbf { v }$ are orthonormal, the square of the 2-norm of a general solution always equals or exceeds that of $\mathbf { m } _ { \dagger }$

$$
\| \mathbf { m } \| _ { 2 } ^ { 2 } = \| \mathbf { m } _ { \dag } \| _ { 2 } ^ { 2 } + \sum _ { i = p + 1 } ^ { n } \alpha _ { i } ^ { 2 } \geq \| \mathbf { m } _ { \dag } \| _ { 2 } ^ { 2 }
$$

where we have equality only if all of the $\alpha _ { i }$ are zero. The generalized inverse solution is thus a minimum length least squares solution.

We can also write this solution in terms of $\mathbf { G }$ and $\mathbf { G } ^ { T }$

$$
\begin{array} { r l } & { \mathbf { m } \dagger = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { U } _ { p } \mathbf { S } _ { p } ^ { - 2 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { G } ^ { T } ( \mathbf { U } _ { p } \mathbf { S } _ { p } ^ { - 2 } \mathbf { U } _ { p } ^ { T } ) \mathbf { d } } \\ & { \qquad = \mathbf { G } ^ { T } ( \mathbf { G } \mathbf { G } ^ { T } ) ^ { - 1 } \mathbf { d } . } \end{array}
$$

In practice it is better to compute a solution using the SVD than to use (3.38) because of numerical accuracy issues.

3. $n = p$ and $p < m$ $N ( \mathbf G )$ is trivial but $N ( \mathbf G ^ { T } )$ is nontrivial. Because $p < m , R ( \mathbf { G } )$ is a subspace of $R ^ { m }$ .Here

$$
\begin{array} { c } { \mathbf { G m } _ { \dagger } = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ { \mathbf { \Lambda } = \mathbf { U } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { d } . } \end{array}
$$

The product $\mathbf { U } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { d }$ gives the projection of $\mathbf { d }$ onto $R ( \mathbf G )$ . Thus $\mathbf { G m } _ { \dagger }$ is the point in $R ( \mathbf G )$ that is closest to $\mathbf { d }$ ,and $\mathbf { m } _ { \dagger }$ is a least squares solution to $\mathbf { G m } = \mathbf { d }$ Only if d is actually in $R ( \mathbf G )$ will $\mathbf { m } _ { \dagger }$ be an exact solution to $\mathbf { G m } = \mathbf { d }$

We can see that this solution is exactly that obtained from the normal equations because

$$
\begin{array} { r l } & { ( \mathbf G ^ { T } \mathbf G ) ^ { - 1 } = ( \mathbf V _ { p } \mathbf S _ { p } \mathbf U _ { p } ^ { T } \mathbf U _ { p } \mathbf S _ { p } \mathbf V _ { p } ^ { T } ) ^ { - 1 } } \\ & { \quad \quad \quad \quad \quad = ( \mathbf V _ { p } \mathbf S _ { p } ^ { 2 } \mathbf V _ { p } ^ { T } ) ^ { - 1 } } \\ & { \quad \quad \quad = \mathbf V _ { p } \mathbf S _ { p } ^ { - 2 } \mathbf V _ { p } ^ { T } } \end{array}
$$


<!-- chunk 0002: pages 71-140 -->
and

$$
\begin{array} { r l } & { \mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 2 } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { d } . } \end{array}
$$

This solution is unique, but cannot fit general data exactly. As with (3.38), it is better in practice to use the generalized inverse solution than to use (3.47) because of numerical accuracy issues.

4. $p < m$ and $p < n$ Both $N ( \mathbf G ^ { T } )$ and $N ( \mathbf G )$ are nontrivial. In this case, the generali-zed inverse solution encapsulates the behavior of both of the two previous cases, minimizing both $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ and $\| \mathbf { m } \| _ { 2 }$

As in case 3,

$$
\begin{array} { r l } & { \mathbf { G m } _ { \dagger } = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathbf { U } _ { p } \mathbf { U } _ { p } ^ { T } \mathbf { d } } \\ & { \qquad = \mathrm { p r o j } _ { R ( \mathbf { G } ) } \mathbf { d } . } \end{array}
$$

Thus $\mathbf { m } _ { \dagger }$ is a least squares solution to $\mathbf { G m } = \mathbf { d }$

As in case 2 we can write the model and its norm using (3.33) and (3.34). Thus $\mathbf { m } _ { \dagger }$ is the least squares solution of minimum length.

We have shown that the generalized inverse provides an inverse solution (3.22) that always exists,is both least squares and minimum length,and properly accommodates the rank and dimensions of $\mathbf { G }$ .Relationships between the subspaces $R ( \mathbf G )$ ， $N ( \mathbf G ^ { T } )$ ， $R ( \mathbf G ^ { T } )$ ， $N ( \mathbf G )$ , and the operators $\mathbf { G }$ and $\mathbf { G } ^ { \dagger }$ , are schematically depicted in Figure 3.1. Table 3.1 summarizes the SVD and its properties.

The existence of a nontrivial model null space (one that includes more than just the zero vector) is at the heart of solution nonuniquenes. There are an infinite number of solutions that will fit the data equally well, because model components in $N ( \mathbf G )$ have no effect on data fit. To select a particular preferred solution from this infinite set thus requires more constraints (such as minimum length or smoothing constraints) than are encoded in the matrix $\mathbf { G }$

Table 3.1 Summary of the SVD and its associated scalars and matrices.   

<table><tr><td>Object</td><td>Size</td><td>Properties</td></tr><tr><td>p</td><td>scalar</td><td>rank(G)= p; Number of nonzero singular values</td></tr><tr><td>m</td><td>scalar</td><td>Dimension of the data space</td></tr><tr><td>n</td><td>scalar</td><td>Dimension of the model space</td></tr><tr><td>G</td><td>m by n</td><td></td></tr><tr><td>U</td><td>m by m</td><td>Orthogonal matrix; U= [Up, Uo]</td></tr><tr><td>Si</td><td>scalar</td><td>ith singular value</td></tr><tr><td>S</td><td>m by n</td><td>Diagonal matrix of singular values; Si,i = si</td></tr><tr><td>V</td><td>n by n</td><td>Orthogonal matrix; V= [Vp, Vo]</td></tr><tr><td>Up</td><td>m by p</td><td>Columns form a basis for R(G)</td></tr><tr><td>Sp</td><td>p by p</td><td>Diagonal matrix of nonzero singular values</td></tr><tr><td>Vp</td><td>n by p</td><td>Columns form an orthonormal basis for R(GT)</td></tr><tr><td>Uo</td><td>m by m-p</td><td>Columns form an orthonormal basis for N(GT)</td></tr><tr><td>Vo</td><td>n by n-p</td><td>Columns form an orthonormal basis for N(G)</td></tr><tr><td>U.,i</td><td>m by 1</td><td>Eigenvector of GGT with eigenvalue s2</td></tr><tr><td>V.i Gf</td><td>n by 1</td><td></td></tr><tr><td></td><td>n by m</td><td>Pseudoinverse of G; G† = VpS-1UT p</td></tr><tr><td>mt</td><td>m by 1</td><td>Generalized inverse solution; m† = G†d</td></tr></table>

To see the significance of the $N ( \mathbf G ^ { T } )$ subspace, consider an arbitrary data vector, $\mathbf { d } _ { \mathrm { 0 } }$ ， which lies in $N ( \mathbf G ^ { T } )$ ：

$$
{ \bf d } _ { 0 } = \sum _ { i = p + 1 } ^ { m } \beta _ { i } { \bf U } . _ { , i } .
$$

The generalized inverse operating on such a data vector gives

$$
\begin{array} { r l } & { \mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } _ { 0 } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \displaystyle \sum _ { i = p + 1 } ^ { n } \beta _ { i } \mathbf { U } _ { p } ^ { T } \mathbf { U } _ { \cdot , i } = \mathbf { 0 } } \end{array}
$$

because the $\mathbf { U } _ { \cdot , i }$ are orthogonal. $N ( \mathbf G ^ { T } )$ is a subspace of $R ^ { m }$ consisting of all vectors $\mathbf { d } _ { 0 }$ that have no influence on the generalized inverse model, $\mathbf { m } _ { \dagger }$ .If $p < n$ ，there are an infinite number of potential data sets that will produce the same model when (3.22) is applied.

# 3.2.COVARIANCE AND RESOLUTION OF THE GENERALIZED INVERSE SOLUTION

The generalized inverse always gives us a solution, $\mathbf { m } _ { \dagger }$ , with well-determined properties, but it is essential to investigate how faithful a representation any model is likely to be of the true situation.

In Chapter 2, we found that under the assumption of independent and normally distributed measurement errors with constant standard deviation, the least squares solution was an unbiased estimator of the true model, and that the estimated model parameters had a multivariate normal distribution with covariance

$$
\begin{array} { r } { \mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = \sigma ^ { 2 } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } . } \end{array}
$$

We can attempt the same analysis for the generalized inverse solution $\mathbf { m } \dagger$ . The covariance matrix would be given by

$$
\begin{array} { l } { \displaystyle \mathrm { C o v } ( { \bf m } _ { \dagger } ) = { \bf G } ^ { \dagger } \mathrm { C o v } ( { \bf d } ) ( { \bf G } ^ { \dagger } ) ^ { T } } \\ { \displaystyle = \sigma ^ { 2 } { \bf G } ^ { \dagger } ( { \bf G } ^ { \dagger } ) ^ { T } } \\ { \displaystyle = \sigma ^ { 2 } { \bf V } _ { p } \mathbb { S } _ { p } ^ { - 2 } { \bf V } _ { p } ^ { T } } \\ { \displaystyle = \sigma ^ { 2 } \sum _ { i = 1 } ^ { p } \frac { V _ { \cdot , i } V _ { \cdot , i } ^ { T } } { s _ { i } ^ { 2 } } . } \end{array}
$$

Since the $s _ { i }$ are decreasing, successive terms in this sum make larger and larger contributions to the covariance. If we were to truncate (3.58), we could actually decrease the variance in our model estimate! This is discussed further in Section 3.3.

Unfortunately, unless ${ \boldsymbol { p } } = n$ ,the generalized inverse solution is not an unbiased estimator of the true solution. This occurs because the true solution may have nonzero projections onto those basis vectors in $\mathbf { v }$ that are unused in the generalized inverse solu-tion. In practice, the bias introduced by restricting the solution to the subspace spanned by the columns of $\mathbf { V } _ { p }$ may be far larger than the uncertainty due to measurement error.

The concept of model resolution is an important way to characterize the bias of the generalized inverse solution. In this approach we see how closely the generalized inverse solution matches a given model, assuming that there are no errors in the data. We begin with a model $\mathbf { m } _ { \mathrm { t r u e } }$ . By multiplying $\mathbf { G }$ times $\mathbf { m _ { \mathrm { t r u e } } }$ , we can find a corresponding data vector $\mathbf { d } _ { \mathrm { t r u e } }$ . If we then multiply $\mathbf { G } ^ { \dagger }$ times ${ \bf d } _ { \mathrm { t r u e } }$ ,we obtain a generalized inverse solution

$$
\mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { G m } _ { \mathrm { t r u e } } .
$$

We would obviously like to recover the original model, so that $\mathbf { m } ^ { \dagger } = \mathbf { m } _ { \mathrm { { t r u e } } }$ . However, because $\mathbf { m } _ { \mathrm { t r u e } }$ may have had a nonzero projection onto the model null space

$N ( \mathbf G )$ ， $\mathbf { m } _ { \dagger }$ will not in general be equal to $\mathbf { m _ { \mathrm { t r u e } } }$ . The model resolution matrix that characterizes this effect is

$$
\begin{array} { r l } & { \mathbf { R } _ { \mathrm { m } } = \mathbf { G } ^ { \dagger } \mathbf { G } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } } \\ & { \qquad = \mathbf { V } _ { p } \mathbf { V } _ { p } ^ { T } . } \end{array}
$$

If $N ( \mathbf G )$ is trivial, then $\operatorname { r a n k } ( \mathbf G ) = p = n$ and $\mathbf { R } _ { \mathrm { m } }$ is the $n$ by $n$ identity matrix. In this case the original model is recovered exactly and we say that the resolution is perfect. If $N ( \mathbf G )$ is a nontrivial subspace of $R ^ { n }$ ，then $p = { \mathrm { r a n k } } ( \mathbf G ) < n$ ，so that $\mathbf { R } _ { \mathrm { m } }$ is not the identity matrix. The model resolution matrix is instead a nonidentity symmetric matrix that characterizes how the generalized inverse solution smears out the original model, $\mathbf { m _ { \mathrm { t r u e } } }$ , into a recovered model, $\mathbf { m } _ { \dagger }$ . The trace of $\mathbf { R } _ { \mathrm { m } }$ is often used as a simple quantitative measure of the resolution. If $\operatorname { T r } ( \mathbf { R } _ { \mathrm { m } } )$ is close to $n$ ，then $\mathbf { R } _ { \mathrm { m } }$ is relatively close to the identity matrix.

The model resolution matrix can be used to quantify the bias introduced by the pseudoinverse when $\mathbf { G }$ does not have full column rank. We begin by showing that the expected value of $\mathbf { m } _ { \dagger }$ is $\mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } }$

$$
\begin{array} { r l } & { E [ \mathbf { m } _ { \dagger } ] = E [ \mathbf { G } ^ { \dagger } \mathbf { d } ] } \\ & { \qquad = \mathbf { G } ^ { \dagger } E [ \mathbf { d } ] } \\ & { \qquad = \mathbf { G } ^ { \dagger } \mathbf { G } \mathbf { m } _ { \mathrm { t r u e } } } \\ & { \qquad = \mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } } . } \end{array}
$$

Thus the bias in the generalized inverse solution is

$$
\begin{array} { r } { E [ \mathbf { m } _ { \dagger } ] - \mathbf { m } _ { \mathrm { t r u e } } = \mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { \mathrm { t r u e } } } \\ { = ( \mathbf { R } _ { \mathrm { m } } - \mathbf { I } ) \mathbf { m } _ { \mathrm { t r u e } } \quad } \end{array}
$$

where

$$
\begin{array} { c } { { { \bf R } _ { \mathrm { m } } - { \bf I } = { \bf V } _ { p } { \bf V } _ { p } ^ { T } - { \bf V } { \bf V } ^ { T } } } \\ { { = - { \bf V } _ { 0 } { \bf V } _ { 0 } ^ { T } . } } \end{array}
$$

We can formulate a bound on the norm of the bias using (3.68) as

$$
\begin{array} { r } { \| E [ \mathbf { m } _ { \dagger } ] - \mathbf { m } _ { \mathrm { t r u e } } \| \leq \| \mathbf { R } _ { \mathrm { m } } - \mathbf { I } \| \| \mathbf { m } _ { \mathrm { t r u e } } \| . } \end{array}
$$

$\| \mathbf { R } _ { \mathrm { m } } - \mathbf { I } \|$ thus characterizes the bias introduced by the generalized inverse solution. However, the detailed effects of limited resolution on the recovered model will depend on $\| \mathbf { m } _ { \mathrm { t r u e } } \|$ , about which we may have quite limited a priori knowledge.

In practice, the model resolution matrix is commonly used in two different ways. First,we can examine diagonal elements of $\mathbf { R } _ { \mathrm { m } }$ . Diagonal elements that are close to one correspond to parameters for which we can claim good resolution. Conversely, if any of the diagonal elements are small, then the corresponding model parameters will be poorly resolved. Second,we can multiply $\mathbf { R } _ { \mathrm { m } }$ times a particular test model m to see how that model would be resolved by the inverse solution. This strategy is called a resolution test. One commonly used test model is a spike model, which is a vector with all zero elements,except for a single entry which is one.Multiplying $\mathbf { R } _ { \mathrm { m } }$ times a spike model effectively picks out the corresponding column of the resolution matrix. These columns of the resolution matrix are called resolution kernels. Such functions are also similar to the averaging kernels in the method of Backus and Gilbert discussed in Chapter 5.

We can multiply $\mathbf { G } ^ { \dagger }$ and $\mathbf { G }$ in the opposite order from (3.62) to obtain the data space resolution matrix, $\mathbf { R } _ { \mathrm { d } }$

$$
\begin{array} { c } { \mathbf { d } _ { \dagger } = \mathbf { G m } _ { \dagger } } \\ { \mathbf { \Lambda } = \mathbf { G G } ^ { \dagger } \mathbf { d } } \\ { \mathbf { \Lambda } = \mathbf { R } _ { \mathrm { d } } \mathbf { d } } \end{array}
$$

where

$$
\begin{array} { r } { \mathbf { R } _ { \mathrm { d } } = \mathbf { U } _ { p } \mathbf { S } _ { p } \mathbf { V } _ { p } ^ { T } \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } } \\ { = \mathbf { U } _ { p } \mathbf { U } _ { p } ^ { T } . \qquad } \end{array}
$$

If $N ( \mathbf G ^ { T } )$ contains only the zero vector, then $p = m$ ,and $\mathbf { R } _ { \mathrm { d } } = \mathbf { I }$ In this case, $\mathbf { d } _ { \dagger } = \mathbf { d }$ and the generalized inverse solution $\mathbf { m } \dagger$ fits the data exactly. However, if $N ( \mathbf G ^ { T } )$ is nontrivial, then $p < m$ and $\mathbf { R } _ { \mathrm { d } }$ is not the identity matrix. In this case $\mathbf { m } _ { \dagger }$ does not exactly fit the data.

Note that model and data space resolution matrices (3.62) and (3.76) do not depend on specific data or models, but are exclusively properties of $\mathbf { G }$ .They reflect the physics and geometry of a problem,and can thus be assessed during the design phase of an experiment.

# 3.3.INSTABILITY OF THE GENERALIZED INVERSE SOLUTION

The generalized inverse solution $\mathbf { m } _ { \dagger }$ has zero projection onto $N ( \mathbf G )$ . However, it may include terms involving column vectors in $\mathbf { V } _ { p }$ with very small nonzero singular values. In analyzing the generalized inverse solution it is useful to examine the singular value spectrum, which is simply the range of singular values. Small singular values cause the generalized inverse solution to be extremely sensitive to small amounts of noise in the data.As a practical matter, it can also be difficult to distinguish between zero singular values and extremely small singular values. We can quantify the instabilities created by small singular values by recasting the generalized inverse solution to make the effect of small singular values explicit. We start with the formula for the generalized inverse solution,

$$
\begin{array} { r } { \mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } . } \end{array}
$$

The elements of the vector $\mathbf { U } _ { p } ^ { T } \mathbf { d }$ are the dot products of the first $p$ columns of $\mathbf { U }$ with d

$$
\mathbf { U } _ { p } ^ { T } \mathbf { d } = \left[ \begin{array} { c } { ( \mathbf { U } _ { \cdot , 1 } ) ^ { T } \mathbf { d } } \\ { ( \mathbf { U } _ { \cdot , 2 } ) ^ { T } \mathbf { d } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { ( \mathbf { U } _ { \cdot , p } ) ^ { T } \mathbf { d } } \end{array} \right] .
$$

When we left-multiply $\mathbf { S } _ { p } ^ { - 1 }$ times (3.78), we obtain

$$
\mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } = \left[ \begin{array} { c } { \frac { ( \mathbf { U } _ { \cdot , 1 } ) ^ { T } \mathbf { d } } { s _ { 1 } } } \\ { \frac { ( \mathbf { U } _ { \cdot , 2 } ) ^ { T } \mathbf { d } } { s _ { 2 } } } \\ { \cdot } \\ { \cdot } \\ { \cdot } \\ { \frac { ( \mathbf { U } _ { \cdot , p } ) ^ { T } \mathbf { d } } { s _ { p } } } \end{array} \right] .
$$

Finally, when we left-multiply $\mathbf { V } _ { p }$ times (3.79),we obtain a linear combination of the columns of $\mathbf { V } _ { p }$ that can be written as

$$
\mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } = \sum _ { i = 1 } ^ { p } { \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } } \mathbf { V } _ { \cdot , i } .
$$

In the presence of random noise, $\mathbf { d }$ will generally have a nonzero projection onto each of the directions specified by the columns of $\mathbf { U }$ .The presence of a very small $s _ { i }$ in the denominator of (3.8O) can thus give us a very large coefficient for the corresponding model space basis vector $\mathbf { V } _ { \cdot , i }$ ,and these basis vectors can dominate the solution.In the worst case,the generalized inverse solution is just a noise amplifier,and the answer is practically useless.

A measure of the instability of the solution is the condition number. Note that the condition number considered here for an $m$ by $n$ matrix is a generalization of the condition number for an $n$ by $n$ matrix (A.1O7),and the two formulations are equivalent when $m = n$

Suppose that we have a data vector $\mathbf { d }$ and an associated generalized inverse solution $\mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d }$ . If we consider a slightly perturbed data vector $\mathbf { d } ^ { \prime }$ and its associated generalized inverse solution $\mathbf { m } _ { \dagger } ^ { \prime } = \mathbf { G } ^ { \dagger } \mathbf { d } ^ { \prime }$ ，then

$$
\mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } = \mathbf { G } ^ { \dagger } ( \mathbf { d } - \mathbf { d } ^ { \prime } )
$$

and

$$
\lVert \mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } \rVert _ { 2 } \leq \lVert \mathbf { G } ^ { \dagger } \rVert _ { 2 } \lVert \mathbf { d } - \mathbf { d } ^ { \prime } \rVert _ { 2 } .
$$

From (3.8O), it is clear that the largest difference in the inverse models will occur when $\mathbf { d } - \mathbf { d } ^ { \prime }$ is in the direction $\mathbf { U } _ { \cdot , p }$ If

$$
\mathbf { d } - \mathbf { d } ^ { \prime } = \alpha \mathbf { U } _ { \cdot , p } ,
$$

then

$$
\|  { \mathbf { d } } -  { \mathbf { d } } ^ { \prime } \| _ { 2 } = \alpha .
$$

We can then compute the effect on the generalized inverse solution as

$$
\mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } = \frac { \alpha } { s _ { p } } \mathbf { V } _ { \cdot , p }
$$

with

$$
\| \mathbf { m } _ { \dag } - \mathbf { m } _ { \dag } ^ { \prime } \| _ { 2 } = \frac { \alpha } { s _ { p } } .
$$

Thus,we have a bound on the instability of the generalized inverse solution

$$
\| \mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } \| _ { 2 } \leq \frac { 1 } { s _ { p } } \| \mathbf { d } - \mathbf { d } ^ { \prime } \| _ { 2 } .
$$

Similarly, we can see that the generalized inverse model is smallest in norm when d points in a direction parallel to $\mathbf { V } _ { \cdot , 1 }$ . Thus

$$
\| \mathbf { m } _ { \dagger } \| _ { 2 } \geq \frac { 1 } { s _ { 1 } } \| \mathbf { d } \| _ { 2 } .
$$

Combining these inequalities, we obtain

$$
\frac { \| \mathbf { m } _ { \dagger } - \mathbf { m } _ { \dagger } ^ { \prime } \| _ { 2 } } { \| \mathbf { m } _ { \dagger } \| _ { 2 } } \leq \frac { s _ { 1 } } { s _ { p } } \frac { \| \mathbf { d } - \mathbf { d } ^ { \prime } \| _ { 2 } } { \| \mathbf { d } \| _ { 2 } } .
$$

The bound (3.89) is applicable to pseudoinverse solutions, regardless of what value of $p$ we use. If we decrease $p$ and thus eliminate model space vectors associated with small singular values,then the solution becomes more stable. However, this stability comes at the expense of reducing the dimension of the subspace of $R ^ { n }$ where the solution lies.

As a esult, the model resolution matrix for the stabilized solution obtained by decreasing $p$ becomes less like the identity matrix,and the fit to the data worsens.

The condition number of $\mathbf { G }$ is the coefficient in (3.89)

$$
\mathrm { c o n d } ( \mathbf { G } ) = \frac { s _ { 1 } } { s _ { k } }
$$

where $k = \operatorname* { m i n } ( m , n )$ . The MATLAB command cond can be used to compute (3.90). If $\mathbf { G }$ is of full rank,and we use all of the singular values in the pseudoinverse solution $( p = k )$ , then the condition number is exactly (3.90). If $\mathbf { G }$ is of less than full rank, then the condition number is effectively infinite. As with the model and data resolution matrices (3.62) and (3.76)), the condition number is a property of $\mathbf { G }$ that can be computed in the design phase of an experiment before any data are collected.

A condition that insures solution stability and arises naturally from consideration of (3.80) is the discrete Picard condition [67]. The discrete Picard condition is satisfied when the dot products of the columns of $\mathbf { U }$ and the data vector decay to zero more quickly than the singular values, $s _ { i }$ . Under this condition,we should not see instability due to small singular values. The discrete Picard condition can be assessed by plotting the ratios of $\mathbf { U } _ { . , i } ^ { T } \mathbf { d }$ to $s _ { i }$ across the singular value spectrum.

If the discrete Picard condition is not satisfied, we may stillbe able to recover a useful model by truncating the series for $\mathbf { m } \dagger$ (3.80) at term $\boldsymbol { p } ^ { \prime } < \boldsymbol { p }$ ， to produce a truncated SVD,or TsVD solution. One way to decide where to truncate the series is to apply the discrepancy principle. Under the discrepancy principle, we choose $p ^ { \prime }$ so that the model fits the data to a specified tolerance, $\delta$ ,that is,

$$
\lVert \mathbf { G } _ { w } \mathbf { m } - \mathbf { d } _ { w } \rVert _ { 2 } \leq \delta ,
$$

where $\mathbf { G } _ { \boldsymbol { w } }$ and $\mathbf { d } _ { \boldsymbol { w } }$ are the weighted system matrix and data vector, respectively.

How should we select $\delta \ ?$ We discussed in Chapter 2 that when we estimate the solu-tion to a full column rank least squares problem, $\| \mathbf { G } _ { u } \mathbf { m } _ { L _ { 2 } } - \mathbf { d } _ { u } \| _ { 2 } ^ { 2 }$ has a $\chi ^ { 2 }$ distribution with $m - n$ degrees of freedom, so we could set $\delta$ equal to $m - n$ if $m > n$ .However, when the number of model parameters $n$ is greater than or equal to the number of data $m$ ,this formulation fails because there is no $\chi ^ { 2 }$ distribution with fewer than one degree of freedom. In practice, a common heuristic is to require $\lVert \mathbf { G } _ { u } \mathbf { m } - \mathbf { d } _ { u } \rVert _ { 2 } ^ { 2 }$ to be smaller than $m$ , because the approximate median of a $\chi ^ { 2 }$ distribution with $m$ degrees of freedom is m (Figure B.4).

A TSVD solution willnot fit the data as well as solutions that include the model space basis vectors with small singular values.However, fitting the data vector too precisely in ill-posed problems (sometimes referred to as over-fiting) will allow data noise to control major features, or even completely dominate, the model.

The TSVD solution is but one example of regularization,where solutions are selected to sacrifice fit to the data in exchange for solution stability. Understanding the trade-off between fiting the data and solution stability involved in regularization is of fundamental importance.

# 3.4.A RANK DEFICIENT TOMOGRAPHY PROBLEM

A linear least squares problem is said to be rank deficient if there is a clear distinction between the nonzero and zero singular values and $\operatorname { r a n k } ( \mathbf G )$ is less than $n$ Numerically computed singular values will often include some that are extremely small but not quite zero,because of round-off errors. If there is a substantial gap between the largest of these tiny singular values and the first truly nonzero singular value, then it can be easy to distinguish between the two populations.Rank deficient problems can often be solved in a straightforward manner by applying the generalized inverse solution. After truncating the effectively zero singular values,a least squares model of limited resolution will be produced,and stability will seldom be an issue.

# Example 3.1

Using the SVD,let us revisit the straight ray path tomography example that we con-sidered earlier in Examples 1.6 and 1.12 (Figure 3.2). We introduced a rank deficient system in which we were constraining an $n = 9$ -parameter slowness model with $m = 8$ travel time observations. We map the two-dimensional grid of slownesses into a model vector by using a row-by-row indexing convention to obtain

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/ffe016010ef7080307e3aafd9798121add77c22786d59bf23f1b0d8baa0ce683.jpg)  
Figure 3.2 A simple tomography example (revisited).

$$
\mathbf { G m } = { \left[ \begin{array} { l l l l l l l l l } { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 1 } \\ { { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { { \sqrt { 2 } } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { { \sqrt { 2 } } } \end{array} \right] } { \left[ \begin{array} { l } { s _ { 1 1 } } \\ { s _ { 1 2 } } \\ { s _ { 3 1 } } \\ { s _ { 2 1 } } \\ { s _ { 2 2 } } \\ { s _ { 2 3 } } \\ { s _ { 3 1 } } \\ { s _ { 3 2 } } \\ { s _ { 3 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { t _ { 1 } } \\ { t _ { 2 } } \\ { t _ { 3 } } \\ { t _ { 4 } } \\ { t _ { 5 } } \\ { t _ { 6 } } \\ { t _ { 7 } } \\ { t _ { 8 } } \end{array} \right] } .
$$

The eight singular values of $\mathbf { G }$ are, numerically evaluated,

$$
\operatorname { d i a g } ( \mathbf { S } ) = { \left[ \begin{array} { l } { 3 . 1 8 0 } \\ { 2 . 0 0 0 } \\ { 1 . 7 3 2 } \\ { 1 . 7 3 2 } \\ { 1 . 7 3 2 } \\ { 1 . 6 0 7 } \\ { 0 . 5 5 3 } \\ { 1 . 4 2 9 \times 1 0 ^ { - 1 6 } } \end{array} \right] } .
$$

The smallest singular value, $s _ { 8 }$ , is nonzero in numerical evaluation only because of round-off errors in the SVD algorithm. It is zero in an analytical solution and is effectively zero in numerical computation relative to the other singular values. The ratio of the largest to smallest of the other singular values is about 6,and the generalized inverse solution (3.8O) will thus be stable in the presence of noise. Because $\operatorname { r a n k } ( \mathbf G ) = p = 7$ is less than both $m$ and $n$ ，the problem is both rank deficient and will in general have no exact solution. The model null space, $N ( \mathbf G )$ , is spanned by the two orthonormal vectors that form the 8th and 9th columns of $\mathbf { v }$ . An orthonormal basis for the nullspace is

$$
\mathbf { V } _ { 0 } = \left[ \mathbf { V } _ { , 8 } , \mathbf { V } _ { , 9 } \right] = \left[ \begin{array} { c c } { - 0 . 0 6 2 0 } & { - 0 . 4 0 3 5 } \\ { - 0 . 4 0 3 5 } & { 0 . 0 6 2 0 } \\ { 0 . 4 6 5 5 } & { 0 . 3 4 1 5 } \\ { 0 . 4 0 3 5 } & { - 0 . 0 6 2 0 } \\ { 0 . 0 6 2 0 } & { 0 . 4 0 3 5 } \\ { - 0 . 4 6 5 5 } & { - 0 . 3 4 1 5 } \\ { - 0 . 3 4 1 5 } & { 0 . 4 6 5 5 } \\ { 0 . 3 4 1 5 } & { - 0 . 4 6 5 5 } \\ { 0 . 0 0 0 0 } & { 0 . 0 0 0 0 } \end{array} \right] .
$$

To obtain a geometric appreciation for the two model null space vectors in this exam-ple,we can reshape them into 3 by 3 matrices corresponding to the geometry of the blocks (e.g., by using the MATLAB reshape command) to plot their elements in proper physical positions. Here,we have

$$
\begin{array} { r l } { \mathrm { r e s h a p e } ( \mathbf { V } _ { \mathrm { . 8 } } , \ 3 , \ 3 ) ^ { \prime } = \left[ \begin{array} { c c c } { - 0 . 0 6 2 0 } & { - 0 . 4 0 3 5 } & { 0 . 4 6 5 5 } \\ { 0 . 4 0 3 5 } & { 0 . 0 6 2 0 } & { - 0 . 4 6 5 5 } \\ { - 0 . 3 4 1 5 } & { 0 . 3 4 1 5 } & { 0 . 0 0 0 0 } \end{array} \right] } & { } \\ { \mathrm { r e s h a p e } ( \mathbf { V } _ { \mathrm { . 9 } } , \ 3 , \ 3 ) ^ { \prime } = \left[ \begin{array} { c c c } { - 0 . 4 0 3 5 } & { 0 . 0 6 2 0 } & { 0 . 3 4 1 5 } \\ { - 0 . 0 6 2 0 } & { 0 . 4 0 3 5 } & { - 0 . 3 4 1 5 } \\ { 0 . 4 6 5 5 } & { - 0 . 4 6 5 5 } & { 0 . 0 0 0 0 } \end{array} \right] } & { } \end{array}
$$

(Figures 3.3 and 3.4).

Recall that if $\mathbf { m } _ { 0 }$ is in the model null space, then (because $\mathbf { G m } _ { 0 } = \mathbf { 0 }$ ）we can add such a model to any solution and not change the fit to the data (3.33). When mapped to their physical locations, three common features of the model null space basis vector elements in this example stand out:

1. The sums along all rows and columns are zero.   
2. The upper left to lower right diagonal sum is zero.   
3. There is no projection in the $m _ { 9 } = s _ { 3 3 }$ model space direction.

The zero sum conditions (1） and (2) arise because paths pasing through any thre horizontal or vertical sets of blocks can only constrain the sum of those block values. The condition (3) that $m \mathrm { { g } } = 0$ occurs because that model element is uniquely constrained by the 8th ray, which passes exclusively through the $s _ { 3 , 3 }$ block. Thus,any variation in m9 will clearly affect the predicted data, and any vector in the model nul space must have a value of zero in m9.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/bd9f712fa8d119d99be74f0ef68875edb24dc6aad53a18e1dfe9715e2164c989.jpg)  
Figure 3.3 Image of the nullspace model $\mathbf { V } _ { \cdot , 8 }$

The single basis vector spanning the data null space in this example is

$$
\mathbf { U } _ { 0 } = \mathbf { U } _ { , 8 } = { \left[ \begin{array} { l } { - 0 . 4 0 8 } \\ { - 0 . 4 0 8 } \\ { - 0 . 4 0 8 } \\ { 0 . 4 0 8 } \\ { 0 . 4 0 8 } \\ { 0 . 4 0 8 } \\ { 0 . 0 0 0 } \\ { 0 . 0 0 0 } \end{array} \right] } .
$$

This indicates that increasing the times $t _ { 1 } , t _ { 2 }$ ,and $t _ { 3 }$ and decreasing the times $t _ { 4 } , \ t _ { 5 }$ ,and $t _ { 6 }$ by equal amounts wil result in no change in the pseudoinverse solution.

Recall that, even for noise-free data, we will not recover a general $\mathbf { m _ { \mathrm { t r u e } } }$ in a rank deficient problem using (3.22)， but will instead recover a “smeared’ model $\mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } }$ Because $\mathbf { R } _ { \mathrm { m } }$ for a rank deficient problem is itself rank deficient, this smearing is irreversible. The full $\mathbf { R } _ { \mathrm { m } }$ matrix dictates precisely how this smearing occurs. The elements of $\mathbf { R } _ { \mathrm { m } }$ for this example are shown in Figure 3.5.

Examining the entire $n$ by $n$ model resolution matrix becomes cumbersome in large problems.The $n$ diagonal elements of $\mathbf { R } _ { \mathrm { m } }$ can be examined more easily to provide basic information on how well recovered each model parameter will be. The reshaped

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/4c28c082ecbc2c0ca4f2e2c7f6839985388066c0538737ecae71cf85205489e5.jpg)  
Figure 3.5 Elements of the model resolution matrix, $\mathbf { R } _ { \mathrm { m } }$ (3.62), for the generalized inverse solution.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/7d69b4c6054a45bacbfc729fba73560c0bdc9587d7b5b7895c44676f06df2af0.jpg)  
Figure 3.6 Diagonal elements of the resolution matrix plotted in their respective geometric model locations.

diagonal of $\mathbf { R } _ { \mathrm { m } }$ from Figure 3.5 is

$$
\mathrm { r e s h a p e } ( \mathrm { d i a g } ( \mathbf { R } _ { \mathrm { m } } ) , 3 , 3 ) ^ { \prime } = \left[ { \begin{array} { l l l } { 0 . 8 3 3 } & { 0 . 8 3 3 } & { 0 . 6 6 7 } \\ { 0 . 8 3 3 } & { 0 . 8 3 3 } & { 0 . 6 6 7 } \\ { 0 . 6 6 7 } & { 0 . 6 6 7 } & { 1 . 0 0 0 } \end{array} } \right] .
$$

These values are plotted in Figure 3.6.

Figure 3.6 and (3.98) tellus that m9 is perfectly resolved, but that we can expect loss of resolution (and hence smearing of the true model into other blocks) for all of the other solution parameters.

We next assess the smoothing effects of limited model resolution by performing a resolution test using synthetic data for a test model of interest, and assessing the recovery of the test model by examining the corresponding inverse solution. Consider a spike model consisting of the vector with its 5th element equal to one and zeros elsewhere (Figure 3.7). Forward modeling gives the predicted data set for $\mathbf { m } _ { \mathrm { t e s t } }$

$$
\mathbf { d } _ { \mathrm { t e s t } } = \mathbf { G } \mathbf { m } _ { \mathrm { t e s t } } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \\ { 0 } \\ { 1 } \\ { 0 } \\ { \sqrt { 2 } } \\ { 0 } \end{array} \right] }
$$

and the corresponding (reshaped) generalized inverse model is the fifth column of $\mathbf { R } _ { \mathrm { m } }$ ， which is

$$
\mathrm { r e s h a p e } ( \mathbf { m } _ { \mathord { \left/ { \vphantom { \mathrm { 0 . 1 6 7 } } } \right. \kern - delimiterspace } 3 } , 3 , 3 ) ^ { \prime } = \left[ \begin{array} { r r r } { 0 . 1 6 7 } & { 0 } & { - 0 . 1 6 7 } \\ { 0 } & { 0 . 8 3 3 } & { 0 . 1 6 7 } \\ { - 0 . 1 6 7 } & { 0 . 1 6 7 } & { 0 . 1 } \end{array} \right]
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/fced92ee9a6018d658e945d7a56e510f975fec2b68561f56efb097c9b086bcb3.jpg)  
Figure 3.7 A spike test model.

(Figure 3.8). The recovered model in this spike test shows that limited resolution causes information about the central block slowness to smear into some,but not all, of the adjacent blocks even for noise-free data, with the exact form of the smearing dictated by the model resolution matrix.

It is important to reemphasize that the ability to recover the true model in practice is affected both by the bias caused by limited resolution,which is a characteristic of the matrix $\mathbf { G }$ and hence applies even to noise-free data,and by the mapping of any data noise into the model parameters.In specific cases one effect or the other may dominate.

# 3.5.DISCRETE ILL-POSED PROBLEMS

In many problems the singular values decay gradually toward zero and do not show an obvious jump between nonzero and zero singular values. This happens frequently when we discretize Fredholm integral equations of the first kind as in Chapter 1. In particular, as we increase the number of points in the discretization,we typically find that $\mathbf { G }$ becomes more and more poorly conditioned. We will refer to these as discrete ill-posed problems.

The rate of singular value spectrum decay can be used to characterize a discrete ill-posed problem as mildly, moderately, or severely ill-posed. If $s _ { j } = O ( j ^ { - \alpha } )$ for $\alpha \leq 1$ (where $O$ means “on the order of") then we call the problem mildly il-posed. If $s _ { j } =$ $O ( j ^ { - \alpha } )$ for $\alpha > 1$ ,then the problem is moderately ill-posed. If $s _ { j } = O ( e ^ { - \alpha j } )$ for some $\alpha > 0$ , then the problem is severely ill-posed.

In discrete ill-posed problems, singular vectors $\mathbf { V } _ { \cdot , j }$ associated with large singular values are typically smooth，while those corresponding to smaller singular values are highly oscillatory [67]. The influence of rough basis functions becomes increasingly apparent in the character of the generalized inverse solution as more singular values and vectors are included. When we attempt to solve such a problem with the TSVD in the presence of data noise,it is critical to decide where to truncate (3.8O). If we truncate the sum too early, then our solution will lack details that require model vectors associated with the smallr singular values for their representation. However, if we include too many terms,then the solution becomes dominated by the influence of the data noise.

# Example 3.2

Consider an inverse problem where we have a physical process (e.g., seismic ground motion） recorded by a linear instrument of limited bandwidth (e.g.，a vertical seismometer; Figure 3.9). The response of such a device is commonly characterized by an instrument impulse response, which is the response of the system to a delta function input. Consider the instrument impulse response

$$
g ( t ) = \left\{ { \begin{array} { l l } { g _ { 0 } t e ^ { - t / T _ { 0 } } } & { ( t \geq 0 ) } \\ { 0 } & { ( t < 0 ) . } \end{array} } \right.
$$

Figure 3.9 shows the displacement response of a critically damped seismometer with a characteristic time constant $T _ { 0 }$ and gain, $g _ { 0 }$ , to a unit area $( 1 ~ \mathrm { m } / \mathrm { s } ^ { 2 } \cdot \mathrm { s } )$ impulsive ground acceleration input.

Assuming that the displacement of the seismometer is electronically converted to output volts, we conveniently choose $g _ { 0 }$ to be $T _ { 0 } e ^ { - 1 } \ : \mathrm { V / m \cdot s }$ to produce a 1-V maximum output value for the impulse response,and $T _ { \mathrm { 0 } } = 1 0 ~ \mathrm { s }$

The seismometer output (or seismogram), $\nu ( t )$ , is a voltage record given by the convolution of the true ground acceleration, $m _ { \mathrm { t r u e } } ( t )$ , with (3.101)

$$
\nu ( t ) = \intop _ { - \infty } ^ { \infty } g ( \tau - t ) m _ { \mathrm { t r u e } } ( \tau ) d \tau .
$$

We are interested in the inverse deconvolution operation that wil remove the smoothing effect of $g ( t )$ in (3.1O2) and allow us to recover the true ground acceleration $m _ { \mathrm { t r u e } }$

Discretizing (3.102) using the midpoint rule with a time interval $\Delta t$ ，we obtain

$$
\mathbf { d } = \mathbf { G } \mathbf { m }
$$

where

$$
G _ { i , j } = \left\{ \begin{array} { l l } { ( t _ { i } - t _ { j } ) e ^ { - ( t _ { i } - t _ { j } ) / T _ { 0 } } \Delta t } & { ( t _ { i } \geq t _ { j } ) } \\ { 0 } & { ( t _ { i } < t _ { j } ) . } \end{array} \right.
$$

The rows of $\mathbf { G }$ in (3.104) are time-reversed,and the columns of $\mathbf { G }$ are non-timereversed, sampled representations of the impulse response $g ( t )$ ，lagged by $i$ and $j$ respectively. Using a time interval of $[ - 5 , 1 0 0 ]$ s,outside of which (3.101) and any model, $\mathbf { m }$ ,of interest are assumed to be very small or zero,and a discretization interval of $\Delta t = 0 . 5 \mathrm { ~ s ~ }$ ，we obtain a discretized $m$ by $n$ system matrix $\mathbf { G }$ with $m = n = 2 1 0$

The singular values of $\mathbf { G }$ are all nonzero and range from about 25.3 to 0.017, giving a condition number of ${ \approx } 1 4 8 0$ ， and showing that this discretization has produced a discrete system that is mildly ill-posed (Figure 3.1O). However, adding noise at the level of 1 part in 1OOO will be sufficient to make the generalized inverse solution unstable. The reason for this can be seen by examining successive rows of $\mathbf { G }$ ,which are nearly but not quite identical, with

$$
\frac { \mathbf { G } _ { i , \cdot } \mathbf { G } _ { i + 1 , \cdot } ^ { T } } { \| \mathbf { G } _ { i , \cdot } \| _ { 2 } \| \mathbf { G } _ { i + 1 , \cdot } \| _ { 2 } } \approx 0 . 9 9 9 .
$$

This near-identicalnessof the rows of $\mathbf { G }$ makes the system of equations nearly singular, hence resulting in a large condition number.

Now, consider a true ground acceleration signal that consists of two acceleration pulses with widths of $\sigma = 2 ~ \mathrm { s }$ ，centered at $t = 8 :$ Sand $t = 2 5$ S

$$
m _ { \mathrm { t r u e } } ( t ) = e ^ { - ( t - 8 ) ^ { 2 } / ( 2 \sigma ^ { 2 } ) } + 0 . 5 e ^ { - ( t - 2 5 ) ^ { 2 } / ( 2 \sigma ^ { 2 } ) } .
$$

We sample $\mathbf { m } _ { \mathrm { t r u e } } ( t )$ on the time interval $[ - 5 , 1 0 0 ]$ s to obtain a 210-element vector $\mathbf { m _ { \mathrm { t r u e } } }$ , and generate the noise-free data set

$$
\mathbf { d } _ { \mathrm { t r u e } } = \mathbf { G } \mathbf { m } _ { \mathrm { t r u e } }
$$

and a second data set with independent $N ( 0 , ( 0 . 0 5 \mathrm { ~ V } ) ^ { 2 } )$ noise added. The data set with noise is shown in Figure 3.12.

The recovered least squares model from the full $( p = 2 1 0 )$ generalized inverse solution,

$$
\mathbf { m } = \mathbf { V } \mathbf { S } ^ { - 1 } \mathbf { U } ^ { T } \mathbf { d } _ { \mathrm { t r u e } }
$$

is shown in Figure 3.13. The model fits its noiseless data vector, ${ \bf d } _ { \mathrm { t r u e } }$ ， perfectly, and is essentially identical to the true model (Figure 3.11).

The least squares solution for the noisy data vector, $\mathbf { d } _ { \mathrm { t r u e } } + \pmb { \eta }$ ，

$$
\mathbf { m } = \mathbf { V } \mathbf { S } ^ { - 1 } \mathbf { U } ^ { T } ( \mathbf { d } _ { \mathrm { t r u e } } + \pmb { \eta } )
$$

is shown in Figure 3.14.

Although this solution fits its particular data vector, $\mathbf { d } _ { \mathrm { t r u e } } + \pmb { \eta }$ ,exactly, it is worthless in divining information about the true ground motion. Information about $\mathbf { m } _ { \mathrm { t r u e } }$ is overwhelmed by the small amount of added noise,amplified enormously by the inversion process.

Can a useful model be recovered by the TSVD? Using the discrepancy principle as our guide and selecting a range of solutions by varying $p ^ { \prime }$ ，we can in fact obtain an appropriate solution when we use just $p ^ { \prime } = 2 6$ columns of $\mathbf { v }$ to obtain a solution (Figure 3.15).

Essential features of the true model are resolved in the solution of Figure 3.15,but the solution technique introduces oscillations and loss of resolution. Specifically, we see that the widths of the inferred pulses are somewhat wider,and the inferred amplitudes somewhat less,than those of the true ground acceleration. These effects are both hallmarks of limited resolution,as characterized by a nonidentity model resolution matrix.

An image of the model resolution matrix in Figure 3.16 shows a finite-width central band and oscillatory side lobes.

A typical (8Oth) column of the model resolution matrix displays the smearing of the true model into the recovered model for the choice of the $p = 2 6$ inverse operator (Figure 3.17). The smoothing is over a characteristic width of about $5 \ { \mathrm { s } } ,$ ，which is why our recovered model, although it does a decent job of rejecting noise, underestimates the amplitude and narrowness of the pulses in the true model (Figure 3.11). The oscillatory behavior of the resolution matrix is attributable to our abrupt truncation of the model space.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/d9585f8bc274ecbfeb6f6b6cab7efac1059302fedfebb9772d9eda004da64649.jpg)  
Figure 3.15 TSVD solution using $p ^ { \prime } = 2 6$ singular values for the noisy data shown in Figure 3.12.   
Figure 3.16 The model resolution matrix elements, $\mathbf { R } _ { \mathrm { m } i , j } ,$ for the TSVD solution including $p ^ { \prime } = 2 6$ singular values.

Each of the $n$ columns of $\mathbf { v }$ is an oscillatory model basis function,with $j - 1$ zero crossings，where $j$ is the column number. In truncating (3.8O) at 26 terms to stabilize the inverse solution,we place a limit on the most oscillatory model space basis vectors that we wil allow. This truncation gives us a model, and model resolution, that contain

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/8356189117ac108c0ea8f880f51160ff8641fa7c3f04f126473a4cdfbe183ad9.jpg)  
Figure 3.17 The (80th) column of the model resolution matrix, $\mathbf { R } _ { \mathrm { m } } ,$ for the TSVD solution including $p ^ { \prime } = 2 6$ singular values.

Oscillatory structure with up to around $p - 1 = 2 5$ zero crossings. We will examine this perspective further in Chapter 8,where issues associated with oscillatory model basis functions will be revisited in the context of Fourier theory.

# Example 3.3

Recall the Shaw problem from Examples 1.6 and 1.10. Figure 3.18 shows the singular value spectrum for the corresponding G matrix with $n = m = 2 0$ ,which is characterized by very rapid singular value decay to zero.

This is a severely ill-posed problem,and there is no obvious break point above which the singular values can reasonably be considered to be nonzero and below which the singular values can be considered to be O. The MATLAB rank command gives $p ^ { \prime } = 1 8$ ， suggesting that the last two singular values are effectively O. The condition number of this problem is enormous (larger than $1 0 ^ { 1 4 }$ ）.

The 18th column of V, which corresponds to the smallest nonzero singular value, is shown in Figure 3.19.In contrast, the first column of $\mathbf { v }$ ，which corresponds to the largest singular value, represents a much smoother model (Figure 3.2O). This behavior is typical of discrete ill-posed problems.

Next, we wil perform a simple resolution test. Suppose that the input to the system is given by

$$
m _ { i } = { \left\{ \begin{array} { l l } { 1 } & { i = 1 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/4465c7c3d979d354f7148534e3759dbcfdd0b3d2c0d75874107b8dbc7f637256.jpg)  
Figure 3.18 Singular values of Gfor the Shaw example $\mathrm { \Delta } n = m = 2 0 \mathrm { \Delta }$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/7fcdf655fae26aa2902861e2eb68897f44cd30eff1b973a92aa8dc648ddbfc7d.jpg)  
Figure 3.19 $\mathbf { V } _ { \cdot , 1 8 }$ for the Shaw example problem.

(Figure 3.21). We use the model to obtain noise-free data and then apply the generalized inverse (3.22) with various values of $p$ to obtain TSVD inverse solutions. The corresponding data are shown in Figure 3.22. If we compute the generalized inverse from these data using MATLAB's double-precision algorithms, we get fairly good recovery of (3.11O),although there are still some lower amplitude negative intensity values (Figure 3.23).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/ad012a711b8f95db99ea6dd534b648f4f85f8cf9c758aa3ae99cb809143c74f5.jpg)  
Figure 3.20 $\mathbf { V } _ { \cdot , 1 }$ for the Shaw example problem.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/81c621b228dc15332de44039fef8f462b54c71de0b917f49f2b3f1a2774a279e.jpg)  
Figure 3.21 The spike model.

However, if we add a very small amount of noise to the data in Figure 3.22, things change dramatically. Ading $N ( 0 , ( 1 0 ^ { - 6 } ) ^ { 2 } )$ noise to the data of Figure 3.22 and com-puting a generalized inverse solution using $p ^ { \prime } = 1 8$ produces the wild solution of Figure 3.24,which bears no resemblance to the true model. Note that the vertical scale in Figure 3.24 is multiplied by $1 0 ^ { 6 } !$ Furthermore, the solution includes negative intensities, which are not physically possible. This inverse solution is even more sensitive to noise than that of the previous deconvolution example, to the extent that even noise on the order of 1 part in $1 0 ^ { 6 }$ will destabilize the solution.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/60e2d15173461dd7c661c7c43cff68fa386b6cda80a3305f5f0d740d8281ab72.jpg)  
Figure 3.22 Noise-free data predicted for the spike model.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/2fc8e52c0def4a7471af9fe71b67db883b0a10f75cec4eaadc15f6cbd228f215.jpg)  
Figure 3.23 The generalized inverse solution for the spike model, no noise.

Next, we consider what happens when we use only the 1O largest singular values and their corresponding model space vectors to construct a TSVD solution. Figure 3.25 shows the solution using 1O singular values with the same noise as Figure 3.24. Because we have cut off a number of singular values,we have reduced the model resolution. The inverse solution is smeared out, but it is still possble to conclude that there is some significant spike-like feature near $\theta = 0$ . In contrast to the situation that we observed in Figure 3.24, the model recovery is not visibly affected by the noise. The trade-off is that we must now accept the imperfect resolution of this solution and its attendant bias towards smoother models.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/b5e2637412061598956e769d516f808cd818621ee0fddd39dd2d2d874314449e.jpg)  
Figure 3.24 Recovery of the spike model with $N ( 0 , ( 1 0 ^ { - 6 } ) ^ { 2 } )$ noise using the TSVD method $( p ^ { \prime } = 1 8 )$ Note that the intensity scale ranges from $- 4 \times 1 0 ^ { 6 }$ to $4 \times 1 0 ^ { 6 }$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/df4b3c4281874c1701171de35515e2d56e6ca3b4cde6dbdd9121b24f2f147283.jpg)  
Figure 3.25 Recovery of the spike model with noise using the TSVD method $( p ^ { \prime } = 1 0 )$

What happens if we discretize the problem with a larger number of intervals? Figure 3.26 shows the singular values for the $\mathbf { G }$ matrix with $n = m = 1 0 0$ intervals. The first 20 or so singular values are apparently nonzero, while the last 8O or so singular values are effectively zero.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/f1cc8e1196f9662c60f7bd93d16cb16d375b8efffbbaaf7196cda308ee89c14d.jpg)  
Figure 3.26 Singular values of Gfor the Shaw example $\mathrm { { \Delta } } n = m = 1 0 0 \mathrm { { \Delta } }$   
Figure 3.27 Recovery of the spike model with noise using the TSVD method $( n = m = 1 0 0 , p ^ { \prime } = 1 0 )$

Figure 3.27 shows the inverse solution for the spike model with $n = m = 1 0 0$ and $p = 1 0$ . This solution is very similar to the solution shown in Figure 3.24. In general, discretizing over more intervals does not hurt as long as the solution is appropriately regularized and the additional computation time is acceptable.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/54824c0f4d49a31c3fdca986a37c6c1243cdfbd9b194fb4f537059f7ad663708.jpg)  
Figure 3.28 Singular values of Gfor the Shaw example $( n = m = 6 )$

What about a smaller number of intervals? Figure 3.28 shows the singular values of the $\mathbf { G }$ matrix with $n = m = 6$ . In this case there are no terribly small singular values. However, with only 6 elements in the model vector, we cannot hope to resolve the details of a source intensity distribution with a complex structure. This is an example of regularization by discretization (see also Exercise 1.3).

This example again demonstrates a fundamental dilemma. If we include small singular values in the series solution (3.8O),then our solution becomes unstable in the presence of data noise. If we do not include these terms, our solution is less sensitive to data noise, but we sacrifice resolution and introduce bias.

# 3.6. EXERCISES

1. The pseudoinverse of a matrix $\mathbf { G }$ was originally defined by Moore and Penrose as the unique matrix $\mathbf { G } ^ { \dagger }$ with the properties

a. $\mathbf { G } \mathbf { G } ^ { \dagger } \mathbf { G } = \mathbf { G }$   
b. $\mathbf { G } ^ { \dagger } \mathbf { G } \mathbf { G } ^ { \dagger } = \mathbf { G } ^ { \dagger }$   
c. $( \mathbf { G } \mathbf { G } ^ { \dagger } ) ^ { T } = \mathbf { G } \mathbf { G } ^ { \dagger }$   
d. $( \mathbf { G } ^ { \dagger } \mathbf { G } ) ^ { T } = \mathbf { G } ^ { \dagger } \mathbf { G }$

Show that $\mathbf { G } ^ { \dagger }$ as given by (3.20)satisfies these four properties.

2. Another resolution test commonly performed in tomography studies is a checkerboard test, which consists of using a test model composed of alternating positive and negative perturbations. Perform a checkerboard test on the tomography problem

in Example 3.1 using the test model,

$$
\mathbf { m } _ { \mathrm { t r u e } } = \left[ { \begin{array} { r r r } { - 1 } & { 1 } & { - 1 } \\ { 1 } & { - 1 } & { 1 } \\ { - 1 } & { 1 } & { - 1 } \end{array} } \right] .
$$

Evaluate the difference between the true (checkerboard) model and the recovered model in your test,and interpret the pattern of differences. Are any block values recovered exactly? If so, does this imply perfect resolution for these model parameters?

3. Using the parameter estimation problem described in Example 1.1 for determining the three parameters defining a ballistic trajectory, construct synthetic examples that demonstrate the following four cases using the SVD. In each case, display and interpret the SVD components U,V,and S in terms of the rank, $p$ ，of your forward problem $\mathbf { G }$ matrix. Display and interpret any model and data null space vector(s) and calculate model and data space resolution matrices.

a. Three data points that are exactly fit by a unique model. Plot your data points and the predicted data for your model.   
b. Two data points that are exactly fit by an infinite suite of parabolas. Plot your data points and the predicted data for a suite of these models.   
c.Four data points that are only approximately fit by a parabola. Plot your data points and the predicted data for the least squares model.   
d. Two data points that are only approximately fit by any parabola, and for which there are an infinite number of least squares solutions. Plot your data points and the predicted data for a suite of least squares models.

4. A large north-south by east-west-oriented, nearly square plan view, sandstone quarry block ( $1 6 ~ \mathrm { m }$ by $1 6 ~ \mathrm { m } ,$ ） with a bulk compressional wave seismic velocity of approximately $3 0 0 0 ~ \mathrm { m / s }$ is suspected of harboring higher-velocity dinosaur remains. An ultrasonic tomography scan is performed in a horizontal plane bisecting the boulder, producing a data set consisting of $1 6 { \mathrm { ~ E } } {  } \mathbb { W } ,$ $1 6 ~ \mathrm { N { \to } S }$ $3 1 \mathrm { \ N E {  } S W } ,$ and 31 $\mathrm { N W } {  } \mathrm { S E }$ travel times (see Figure 3.29). The travel time data (units of s) have statistically independent errors,and the travel time contribution for a uniform background model (with a velocity of $3 0 0 0 \ \mathrm { m / s } ,$ ）has been subtracted from each travel time measurement.

The MATLAB data files that you will need to load containing the travel time data follow: rowscan.mat, colscan.mat, diag1scan.mat, and diag2scan.mat. The standard deviations of all data measurements are $1 . 5 \times 1 0 ^ { - 5 } \mathrm { s }$ Because the travel time contributions for a uniform background model (with a velocity of $3 0 0 0 ~ \mathrm { m / s }$ ）have been subtracted from each travel time measurement, you will be solving for slowness and velocity perturbations relative to a uniform slowness model of $1 / 3 0 0 0 ~ \mathrm { { s / m } }$ Use a row-by-row mapping between the slowness grid and the model vector (e.g.,Exam-ple 1.12). The row format of each data file is $( x _ { 1 } , \ \gamma _ { 1 } , \ x _ { 2 } , \ \gamma _ { 2 } , \ t )$ where the starting point coordinate of each source is $( x _ { 1 } , \gamma _ { 1 } )$ , the end point coordinate is $( x _ { 2 } , \gamma _ { 2 } )$ ,and the travel time along a ray path between the source and receiver points is a path integral (in seconds).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/458e93df153564af5502db5b0b4ce76f887fb6a62794b4811ece8846e7ef4445.jpg)  
Figure 3.29 Tomography exercise, showing block discretization, block numbering convention,and representative ray paths going east-west (a), north-south (b),southwest-northeast (c),and northwestsoutheast (d).

Parameterize the slowness structure in the plane of the survey by dividing the boulder into a $1 6 \times 1 6$ grid of 256 1-m-square,north-by-east blocks and construct a linear system for the forward problem (Figure 3.29). Assume that the ray paths through each homogeneous block can be represented by straight lines, so that the travel time expression is

$$
\begin{array} { l } { { \displaystyle t = \int _ { \ell } s ( { \bf x } ) d \ell } } \\ { { \displaystyle \ = \sum _ { \mathrm { b l o c k s } } s _ { \mathrm { b l o c k } } \cdot \Delta l _ { \mathrm { b l o c k } } } , } \end{array}
$$

where $\Delta l _ { \mathrm { b l o c k } }$ is $1 ~ \mathrm { m }$ for the row and column scans and $\sqrt { 2 } \mathrm { m }$ for the diagonal scans.

Use the SVD to find a minimum-length/least squares solution, $\mathbf { m } _ { \dagger }$ ,for the 256 block slowness perturbations that fit the data as exactly as possible. Perform two inversions in this manner:

1. Use the row and column scans only.

2.Use the complete data set.

For each inversion:

a. Note the rank of your $\mathbf { G }$ matrix relating the data and model.   
b. State and discuss the general solution and/or data fit significance of the elements and dimensions of the data and model null spaces. Plot and interpret an element of each space and contour or otherwise display a nonzero model that fits the trivial data set $\mathbf { G m } = \mathbf { d } = \mathbf { 0 }$ exactly.   
c. Note whether there are any model parameters that have perfect resolution.   
d.Produce a 16 by 16 element contour or other plot of your slowness perturbation model, displaying the maximum and minimum slowness perturbations in the title of each plot. Interpret any internal structures geometrically and in terms of seismic velocity $( \mathrm { i n ~ m } / \mathrm { s } )$ ).   
e. Show the model resolution by contouring or otherwise displaying the 256 diagonal elements of the model resolution matrix, reshaped into an appropriate 16 by 16 grid.   
f. Describe how one could use solutions to $\mathbf { G m } = \mathbf { d } = \mathbf { 0 }$ to demonstrate that very rough models exist that will fit any data set just as well as a generalized inverse model. Show one such wild model.

5. Consider the data in Table 3.2 (also found in the file ifk.mat).

The function $d ( \gamma )$ ， $0 \leq \gamma \leq 1$ , is related to an unknown function $m ( x ) , 0 \leq x \leq 1$ ， by the mathematical model

$$
d ( \gamma ) = \int _ { 0 } ^ { 1 } x e ^ { - x \gamma } m ( x ) d x .
$$

a. Using the data provided, discretize the integral equation using simple collocation to create a square $\mathbf { G }$ matrix and solve the resulting system of equations.

Table 3.2 Data for Exercise 3.5.   

<table><tr><td>y d(y)</td><td>0.0250 0.07500.12500.1750 0.2250 0.2750 0.32500.37500.4250 0.4750 0.2388 0.2319 0.2252 0.21880.2126 0.2066 0.20080.1952 0.1898</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>80.1846</td></tr><tr><td>y</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.5250 0.5750 0.62500.6750 0.7250 0.77500.8250 0.8750 0.9250 0.9750</td><td></td><td></td></tr><tr><td>d(y)</td><td>0.1795</td><td></td><td></td><td></td><td></td><td>0.1746 0.1699 0.1654 0.16100.1567（</td><td>0.1526</td><td>0.1486</td><td>0.1447</td><td>0.1410</td></tr></table>

b.What is the condition number for this system of equations? Given that the data $d ( \gamma )$ are only accurate to about four digits,what does this tell you about the accuracy of your solution?   
c. Use the TSVD to compute a solution to this problem. You may find a plot of the Picard ratios $\mathbf { U } _ { . , i } ^ { T } \mathbf { d } / s _ { i }$ to be especially useful in deciding how many singular values to include.

# 3.7. NOTES AND FURTHER READING

The Moore-Penrose generalized inverse was independently discovered by Moore in 1920 and Penrose in 1955 [11O,129]. Penrose is generally credited with first showing that the SVD can be used to compute the generalized inverse [129]. Books that discuss the linear algebra of the generalized inverse in more detail include [10, 23].

There was significant early work on the SVD in the 19th century by Beltrami, Jordan, Sylvester, Schmidt,and Weyl [151]. However, the singular value decomposition in matrix form is typically credited to Eckart and Young [41]. Some books that discuss the properties of the SVD and prove its existence include [53,109,152]. Lanczos presents an alternative derivation of the SVD [93]. Algorithms for the computation of the SVD are discussed in [38, 53,164].Books that discuss the use of the SVD and truncated SVD in solving discrete linear inverse problems include [65, 67, 1O8,153].

Resolution tests with spike and checkerboard models as in Example 3.1 are commonly used in practice.However, Leveque, Rivera,and Wittlinger discuss some serious problems with such resolution tests [97]. Complementary information can be acquired by examining the diagonal elements of the resolution matrix,which can be efficiently calculated in isolation from off-diagonal elements even for very large inverse problems [9,103] (Chapter 6).

Matrices like those in Example 3.2 in which the elements along diagonals are con-stant are called Toeplitz matrices [74]. Specialized methods for regularization of problems involving Toeplitz matrices are available [66].

It is possble to effectively regularize the solution to a discretized version of a continuous inverse problem by selecting a coarse discretization (e.g.，Exercise 1.3 and Example 3.3). This approach is analyzed in [45]. However, in doing so we lose the ability to analyze the bias introduced by the regularization. In general, we prefer to use a fine discretization that is consistent with the physics of the forward problem and explicitly regularize the resulting discretized problem.

# Tikhonov Regularization

# Synopsis

The method of Tikhonov regularization for stabilizing inverse problem solutions is introduced and illustrated with examples. Zeroth-order Tikhonov regularization is explored, including its resolution, bias,and uncertainty properties. The concepts of filter factors (which control the contribution of singular values and their corresponding singular vec-tors to the solution) and the discrepancy and L-curve criteria (strategies for selecting the regularization parameter) are presented. Higher-order Tikhonov regularization techniques and their computation by the generalized singular value decomposition (GSVD) and truncated GSVD are discussed.

# 4.1. SELECTING GOOD SOLUTIONS TO ILL-POSED PROBLEMS

We saw in Chapter 3 that, given the SVD of $\mathbf { G }$ (3.1),we can express a generalized inverse solution by a series (3.81)

$$
\mathbf { m } _ { \dagger } = \mathbf { V } _ { p } \mathbf { S } _ { p } ^ { - 1 } \mathbf { U } _ { p } ^ { T } \mathbf { d } = \sum _ { i = 1 } ^ { p } { \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } } \mathbf { V } _ { \cdot , i } .
$$

We also saw that the generalized inverse solution can become extremely unstable when one or more of the singular values, $s _ { i }$ ，is small. One approach for dealing with this difficulty, the truncated singular value decomposition (TSVD), was to truncate the series to remove singular vectors, $\mathbf { V } _ { \cdot , i }$ ,associated with smaller singular values, $s _ { i }$ This stabilized, or regularized,the solution in the sense that it made the result less sensitive to data noise.The cost of this stabilization approach is that the regularized solution had reduced resolution and was no longer unbiased.

In this chapter we will introduce and discuss Tikhonov regularization, a very widely applied and easily implemented technique for regularizing discrete ill-posed problems. We will show a series formula for the Tikhonov solution that is a modified version of the generalized inverse series (3.81). The Tikhonov series solution has coefficients that are functions of the regularization parameter controlling the degree of regularization and which give greater weight to model elements associated with larger singular values.

For a general linear least squares problem there may be infinitely many least squares solutions. If we consider that the data contain noise,and that there is no point in fitting such noise exactly, it becomes evident that there can be many solutions that can adequately fit the data in the sense that $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ is small enough.

In zeroth-order Tikhonov regularization，we consider all solutions with $\| \mathbf { G m } -$ $\mathbf { d } \| _ { 2 } \leq \delta$ ,and select the one that minimizes the norm of m

$$
\begin{array} { c } { { \operatorname* { m i n } \lVert \mathbf { m } \rVert _ { 2 } } } \\ { { \lVert \mathbf { G m } - \mathbf { d } \rVert _ { 2 } \leq \delta . } } \end{array}
$$

The fundamental motivation for minimizing the norm of $\mathbf { m }$ is to arrive at a solution that contains just sufficient feature complexity, as quantified by a norm measure, to adequately fit the data. Note that as $\delta$ increases,the set of feasible models expands,and the minimum value of $\| \mathbf { m } \| _ { 2 }$ decreases. In other words,as we allow a poorer fit to the data,a smaller norm model will suffice to fit the data. We can thus trace out a curve of minimum values of $\| \mathbf { m } \| _ { 2 }$ versus $\delta$ (Figure 4.1). It is also possible to trace out this curve by considering problems of the form

$$
\begin{array} { r l } & { \operatorname* { m i n } \| \mathbf G \mathbf { m } - \mathbf { d } \| _ { 2 } } \\ & { \| \mathbf { m } \| _ { 2 } \leq \epsilon . } \end{array}
$$

As $\epsilon$ decreases, the set of feasible solutions becomes smaller,and the minimum value of $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ increases. Again,as we adjust $\epsilon$ we trace out the curve of optimal values of $\| \mathbf { m } \| _ { 2 }$ and $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ (Figure 4.2).

A third option is to consider the damped least squares problem

$$
\operatorname* { m i n } \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { m } \| _ { 2 } ^ { 2 } ,
$$

which arises when we apply the method of Lagrange multipliers to (4.2),where $\alpha$ is a regularization parameter. It can be shown that for appropriate choices of $\delta , \epsilon .$ and $\alpha$ , the three problems (4.2), (4.3),and (4.4) yield the same solution [65]. We will concentrate on solving the damped least squares form of the problem (4.4). Solutions to (4.2) and (4.3) can be obtained using (4.4) by adjusting the regularization parameter $\alpha$ until the constraints are just satisfied.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/7ba02eb4974021e24c59cedd42adabd16a92d51800d190fe983ddcd0ff19fa71.jpg)  
Figure 4.1 A particular misfit norm, $\delta ,$ and its position on the trade-off curve between residual misfit, $\| \mathbf { G m - d } \| _ { 2 } ,$ and model norm, $\| \mathbf { m } \| _ { 2 }$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/ca350e9af79ca396a79b6a2a6ad452db8c7ac5b315cd319c566ab2fb02bf8c06.jpg)  
Figure 4.2 A particular model norm, $\epsilon _ { i }$ ,and its position on the trade-off curve between residual misfit, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } ,$ and model norm, $\| \mathbf { m } \| _ { 2 }$

When plotted on a log-log scale, the curve of optimal values of $\| \mathbf { m } \| _ { 2 }$ versus $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ often takes on a characteristic“L” shape in linear problems. This happens because $\| \mathbf { m } \| _ { 2 }$ is a strictly decreasing function of $\alpha$ and $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ is a strictly increasing function of $\alpha$ . The sharpness of the“corner” varies from problem to problem, but it is frequently well-defined. For this reason, the curve is called an L-curve [63]. In addition to the discrepancy principle, another popular criterion for picking the value of $\alpha$ is the L-curve criterion, in which the value of $\alpha$ that gives the solution closest to the corner of the L-curve is selected.

# 4.2.SVD IMPLEMENTATION OF TIKHONOV REGULARIZATION

The damped least squares problem (4.4) is equivalent to the ordinary least squares prob-lem obtained by augmenting the least squares problem for $\mathbf { G m } = \mathbf { d }$ in the following manner:

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } } .
$$

As long as $\alpha$ is nonzero, the last $n$ rows of the augmented matrix in (4.5) are obviously linearly independent. Equation (4.5) is thus a full rank least squares problem that can be solved by the method of normal equations, that is,

$$
\begin{array} { r } { \left[ { \mathbf G } ^ { T } \quad \alpha { \mathbf I } \right] \bigg [ \mathbf { G } ^ { } \bigg ] \mathbf { m } = \left[ { \mathbf G } ^ { T } \quad \alpha { \mathbf I } \right] \bigg [ \mathbf { 0 } ^ { } \bigg ] . } \end{array}
$$

Equation (4.6) simplifies to

$$
( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } ,
$$

which is the set of constraint equations for a zeroth-order Tikhonov regularization solution of $\mathbf { G m } = \mathbf { d }$

Employing the SVD of $\mathbf { G }$ ， (4.7) can be written as

$$
\begin{array} { c } { ( \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { S } \mathbf { V } ^ { T } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } } \\ { ( \mathbf { V } \mathbf { S } ^ { T } \mathbf { S } \mathbf { V } ^ { T } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { m } = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \end{array}
$$

A simple substitution diagonalizes this system of equations and makes it straightforward to write out the solution. Let $\mathbf { x } = \mathbf { V } ^ { T } \mathbf { m }$ and $\mathbf { m } = \mathbf { V } \mathbf { x }$ Since $\mathbf { V } \mathbf { V } ^ { T } = \mathbf { I }$ ，we can write (4.9) as

$$
\begin{array} { r } { ( \mathbf { V } \mathbf { S } ^ { T } \mathbf { S } \mathbf { V } ^ { T } + \alpha ^ { 2 } \mathbf { V } \mathbf { V } ^ { T } ) \mathbf { m } = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \\ { \mathbf { V } ( \mathbf { S } ^ { T } \mathbf { S } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { V } ^ { T } \mathbf { m } = \mathbf { V } \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \\ { ( \mathbf { S } ^ { T } \mathbf { S } + \alpha ^ { 2 } \mathbf { I } ) \mathbf { x } = \mathbf { S } ^ { T } \mathbf { U } ^ { T } \mathbf { d } . } \end{array}
$$

The matrix on the left-hand side of this equation is diagonal,so it is trivial to solve the system of equations,

$$
x _ { i } = \frac { s _ { i } \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } } .
$$

Since $\mathbf { m } = \mathbf { V } \mathbf { x }$ ,we obtain the solution

$$
\mathbf { m } _ { \alpha } = \sum _ { i = 1 } ^ { k } \ { \frac { s _ { i } \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } } } \mathbf { V } _ { \cdot , i }
$$

vhere $k = \operatorname* { m i n } ( m , n )$ so that all of the nonzero singular values and vectors are included. To relate this formula to (4.1),we can rewrite it slightly as

$$
\mathbf { m } _ { \alpha } = \sum _ { i = 1 } ^ { k } \ { \frac { s _ { i } ^ { 2 } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } } } { \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } } \mathbf { V } _ { \cdot , i }
$$

or

$$
\mathbf { m } _ { \alpha } = \sum _ { i = 1 } ^ { k } f _ { i } \frac { \mathbf { U } _ { \cdot , i } ^ { T } \mathbf { d } } { s _ { i } } \mathbf { V } _ { \cdot , i } \ .
$$

Here, the filter factors

$$
f _ { i } = \frac { s _ { i } ^ { 2 } } { s _ { i } ^ { 2 } + \alpha ^ { 2 } }
$$

control the contribution to the sum from different terms.For $s _ { i } \gg \alpha , f _ { i } \approx 1$ ，and for $s _ { i } \ll \alpha$ ， $f _ { i } \approx 0$ . For singular values between these two extremes,as the $s _ { i }$ decrease,

the $f _ { i }$ produce a monotonically decreasing contribution of corresponding model space vectors, $\mathbf { V } _ { \cdot , i }$

A related method called the damped SVD method [65] uses the filter factors

$$
\hat { f } _ { i } = \frac { s _ { i } } { s _ { i } + \alpha } .
$$

This has a similar effect to using (4.17),but transitions more slowly with the index i.

# Example 4.1

We revisit the severely ill-posed Shaw problem,which was previously introduced in Examples 1.6 and 1.1O,and was analyzed using the SVD in Example 3.3. The true model in this synthetic example is a spike of unit amplitude in the 1Oth model element, and independent $N ( 0 , ( 1 0 ^ { - 6 } ) ^ { 2 } )$ noise has been added to the data vector. We begin by computing the L-curve at 1OOO points and finding its corner by estimating the point of maximum curvature. Figure 4.3 shows the L-curve. The corner of the curve corresponds to α ≈ 6.40 × 10-6.

Next, we compute the Tikhonov regularization solution corresponding to this value of $\alpha$ . This solution is shown in Figure 4.4. Note that this solution is much better than the wild solution obtained by the TSVD with $p ^ { \prime } = 1 8$ (Figure 3.24).

Alternatively, we can use the discrepancy principle to find an appropriate $\alpha$ to obtain a Tikhonov regularized solution. Because independent $N ( 0 , ( 1 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ noise was added to these $m = 2 0$ data points,we search for a solution for which the square of the norm of the residuals is $2 0 \times 1 0 ^ { - 1 2 }$ ， which corresponds to a residual norm $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ of $\sqrt { 2 0 } \times 1 0 ^ { - 6 } \approx 4 . 4 7 \times 1 0 ^ { - 6 }$ .

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/a9ebe060d1668a5eb321a42b9d4a29b55ac160a263470df58029ea0b1dd667ed.jpg)  
Figure 4.3 Zeroth-order Tikhonov regularization L-curve for the Shaw problem, with corner estimated using maximum functional curvature.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/20c8b526e76fc434fde128cfc29a20b5ea504def66e62d24f89ab0a0ae0db411.jpg)  
Figure 4.4 Recovery of the spike model with noise, zeroth-order Tikhonov solution $( \alpha = 6 . 4 0 \times 1 0 ^ { - 6 }$ determined from the L-curve corner).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/57f0b6a7fa4c9116880ac5f653a324084a06e3df0f7388221e09740533490729.jpg)  
Figure 4.5 Recovery of the spike model with noise,zeroth-order Tikhonov solution $( \alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ determined from the discrepancy principle).

The discrepancy principle results in a somewhat larger value of the regularization parameter, $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ ， than that obtained using the L-curve technique above. The corresponding solution, shown in Figure 4.5, thus has a smaller model norm, but the two models are quite close.

It is interesting to note that the norm of the residual of the true (spike) model in this particular case, $3 . 8 6 \times 1 0 ^ { - 6 }$ , is actually slightly smaller than the tolerance that we specified via the discrepancy principle $( 4 . 4 7 \times 1 0 ^ { - 6 } )$ . The discrepancy principle method did not recover the original spike model because the spike model has a norm of 1, while the solution obtained by the discrepancy principle has a norm of only 0.67.

Plotting the singular values $s _ { i }$ ，the values of $| ( \mathbf { U } _ { \cdot , i } ) ^ { T } \mathbf { d } |$ ,and the ratios $| ( \mathbf { U } _ { \cdot , i } ) ^ { T } \mathbf { d } | / s _ { i }$ allows us to examine the discrete Picard condition for this problem (Figure 4.6). $| ( \mathbf { U } _ { \cdot , i } ) ^ { T } \mathbf { d } |$ reaches a noise floor of about $1 \times 1 0 ^ { - 6 }$ after $i = 1 1$ . The singular values continue to decay. As a consequence, the ratios increase rapidly. It is clear from this plot that we cannot expect to obtain useful information from the singular values beyond $i = 1 1$ .The 11th singular value is ${ \approx } 5 . 1 \times 1 0 ^ { - 6 }$ , which is comparable to the values of $\alpha$ in Figures 4.4 and 4.5.

# 4.3.RESOLUTION, BIAS, AND UNCERTAINTY IN THE TIKHONOV SOLUTION

As in our earlier TSVD approach,we can compute a model resolution matrix for the Tikhonov regularization method. Using equation (4.7) and the SVD, the solution can be written as

$$
\begin{array} { r } { { \bf { m } } _ { \alpha } = ( { \bf { G } } ^ { T } { \bf { G } } + \alpha ^ { 2 } { \bf { I } } ) ^ { - 1 } { \bf { G } } ^ { T } { \bf { d } } } \\ { = { \bf { G } } ^ { \sharp } { \bf { d } } } \\ { = { \bf { V } } { \bf { F } } { \bf { S } } ^ { \dagger } { \bf { U } } ^ { T } { \bf { d } } , } \end{array}
$$

where $\mathbf { F }$ is an $n$ by $n$ diagonal matrix with diagonal elements given by the filter factors $f _ { i }$ of (4.17), and $\mathbf { S } ^ { \dagger }$ is the pseudoinverse of S. $\mathbf { G } ^ { \sharp }$ is a generalized inverse matrix that can be used to construct model and data resolution matrices as was done for the SVD solution in (3.63) and (3.77). The resolution matrices are

$$
{ \bf { R } } _ { \mathrm { { m } } } = { \bf { G } } ^ { \sharp } { \bf { G } } = { \bf { V } } { \bf { F } } { \bf { V } } ^ { T }
$$

and

$$
\mathbf { R } _ { \mathrm { d } } = \mathbf { G } \mathbf { G } ^ { \sharp } = \mathbf { U } \mathbf { F } \mathbf { U } ^ { T } .
$$

Note that the resolution matrices are dependent on the particular value of $\alpha$ (4.19).

# Example 4.2

In Example 4.1, with $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ as selected using the discrepancy principle, the model resolution matrix for zeroth-order Tikhonov regularization has the following diagonal elements:

$$
\begin{array} { l } { { \mathrm { l i a g } ( { \bf R } _ { \mathrm { m } } ) \approx [ 0 . 9 1 , 0 . 4 9 , 0 . 4 5 , 0 . 3 9 , 0 . 4 2 , 0 . 4 1 , 0 . 4 3 , 0 . 4 4 , 0 . 4 4 , . . . . } } \\ { { \mathrm { 0 . 4 5 , ~ 0 . 4 5 , ~ 0 . 4 4 , 0 . 4 4 , 0 . 4 3 , 0 . 4 1 , 0 . 4 2 , 0 . 3 9 , 0 . 4 5 , 0 . 4 9 , 0 . 9 1 ] } ^ { T } } } \end{array} .
$$

indicating that most model parameters are not well resolved. Figure 4.7 displays the effect of this limited resolution by applying $\mathbf { R } _ { \mathrm { m } }$ to the (true) spike model (3.63) or, equiva-lently, inverting noise-free spike model data using (4.6) for the regularization parameter value estimated using the discrepancy principle. Note that the result of limited resolution is that the true model “leaks”or“smears” into adjacent model parameters and is reduced in its maximum amplitude in the recovered model. In this example,the noise-free spike model recovery obtained in this resolution test is nearly identical to the recovery from the noisy spike model data using zeroth-order Tikhonov regulariza-tion (Figure 4.5), indicating that noise has only a very slight effect on model recovery accuracy. Thus, the diferences between the true and recovered models here are essentially entirely due to the regularization that was necessry to stabilize the solution, rather than from noise propagation from data to model (see Example 4.3). Figure 4.7 displays just a single row or column from the (symmetric) $\mathbf { R } _ { \mathrm { m } }$ ,but effects of limited resolu-tion can be examined more comprehensively by imaging the entire resolution matrix (Figure 4.8).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/63f45a4ce048b065e1066a1c2dfc9f6f750c22924ae7d2ee08bd59c736e3a244.jpg)  
Figure4.7 Resolution test using the spike model $( \alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ determined from the discrepancy principle). Note that this model is nearly equivalent to that shown in Figure 4.5.

As in Chapter 2,we can compute a covariance matrix for the estimated model parameters using (B.65). Since

$$
\mathbf { m } _ { \alpha } = \mathbf { G } ^ { \sharp } \mathbf { d } ,
$$

the model covariance is

$$
\mathrm { C o v } ( { \bf m } _ { \alpha } ) = { \bf G } ^ { \sharp } \mathrm { C o v } ( { \bf d } ) ( { \bf G } ^ { \sharp } ) ^ { T } .
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/aadb5e094a9db60d1c424d64e8d7d577a0cd1b451796453707fe9a87167ef1f8.jpg)  
Figure 4.9 Tikhonov solution and confidence intervals for the Shaw problem,estimated using (4.24), wherethe true model isaspikeandthedata noiseis independentand $N ( 0 , ( 1 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ The regularization parameter $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ was chosen using the discrepancy principle. The confidence interval is barely visible at this scale because inaccuracy in the model recovery is dominated by limited resolution.

Note that, as with the TSVD solution of Chapter 3, the Tikhonov regularized solution will generally be biased,and differences between the regularized solution values and the true model may actually be much larger than the confidence intervals obtained from the covariance matrix of the model parameters.Rather, the confidence intervals reflect the difference between $\mathbf { m } _ { \alpha }$ and $\mathbf { R } _ { \mathrm { m } } \mathbf { m } _ { \mathrm { t r u e } }$ . See Figure 4.9.

# Example 4.3

Recall our earlier example of the Shaw problem with the true spike model. Figure 4.9 shows the true model, the solution obtained using $\alpha = 4 . 2 9 \times 1 0 ^ { - 5 }$ chosen using the discrepancy principle,and $9 5 \%$ confidence intervals for the estimated parameters.Note that the confidence intervals are extremely tight,and that very few of the true model parameters are included within the confidence intervals. In this case,the regularization bias,which is not estimated by the covariance matrix,is far larger than the propagated data uncertainty. In other words, the inaccuracy in model recovery in this case is dominated by limited resolution rather than by noise propagation from data to model. The solution shown in Figure 4.9 is essentially identical to the product of $\mathbf { R } _ { \mathrm { m } }$ and $\mathbf { m } _ { \mathrm { t r u e } }$ shown in Figure 4.7 or the 1Oth column of the resolution matrix of Figure 4.8.

# 4.4.HIGHER-ORDER TIKHONOV REGULARIZATION

So far in our discussions of Tikhonov regularization we have minimized an objective function involving $\| \mathbf { m } \| _ { 2 }$ . In many situations,we would prefer to obtain a solution that minimizes some other measure of $\mathbf { m }$ ，expressed as $\mathbf { L m }$ ，such as the norm of the first or second derivative of $\mathbf { m }$ ,reflectinga preference for a“flat”or “smooth” model. We then solve the regularized least squares problem

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } \mathbf { m } \| _ { 2 } ^ { 2 } .
$$

As with (4.5),this can be rewritten as a standard linear least squares problem:

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } } .
$$

For example, if we have discretized our problem using simple collocation and our model is one-dimensional, then we can approximate, to a multiplicative constant, the first derivative of the model by a finite-difference operation $\mathbf { L } _ { 1 } \mathbf { m }$ ，where

$$
\mathbf { L } _ { 1 } = \left[ { \begin{array} { r r r r r r r } { - 1 } & { 1 } & & & & \\ & { - 1 } & { 1 } & & & \\ & & { \ddots } & { \ddots } & & \\ & & & { - 1 } & { 1 } & \\ & & & & & { - 1 } & { 1 } \end{array} } \right] .
$$

The matrices that are used to differentiate $\mathbf { m }$ for the purposes of regularization are commonly referred to as roughening matrices. In (4.27), $\mathbf { L } _ { 1 } \mathbf { m }$ is a finite-difference approximation that is proportional to the first derivative of m.By penalizing $\| \mathbf { L } _ { 1 } \mathbf { m } \| _ { 2 }$ ， we will favor solutions that are relatively flat (i.e.,in the limit, constant). Note that $\| \mathbf { L } _ { 1 } \mathbf { m } \| _ { 2 }$ is a seminorm because it is zero for any constant model, not just for $\mathbf { m } = \mathbf { 0 }$

In applying second-order Tikhonov regularization to a one-dimensional problem, we use a roughening matrix of the form

$$
\mathbf { L } _ { 2 } = \left[ { \begin{array} { r r r r r r r } { 1 } & { - 2 } & { 1 } & & & & \\ & { 1 } & { - 2 } & { 1 } & & & \\ & & { \ddots } & { \ddots } & { \ddots } & & \\ & & & { 1 } & { - 2 } & { 1 } & \\ & & & & { 1 } & { - 2 } & { 1 } \end{array} } \right] .
$$

Here, $\mathbf { L } _ { 2 } \mathbf { m }$ is a finite-difference approximation that is proportional to the second derivative of $\mathbf { m }$ ,and the seminorm term $\| \mathbf { L } _ { 2 } \mathbf { m } \| _ { 2 }$ in (4.25) penalizes solutions that are rough in a squared second derivative sense. We will refer to regularization strategies of the form of (4.25) that use $\mathbf { L } _ { 1 }$ and $\mathbf { L } _ { 2 }$ roughening matrices as first- and second-order Tikhonov regularization, respectively.

If our model is higher dimensional (e.g.,two or three dimensions), then the roughening matrices described here would not be appropriate. In such cases,second-order Tikhonov regularization is often implemented using a finite-difference approximation to the Laplacian operator of appropriate dimensionality (see Exercise 4.3).

To ensure that the least squares problem (4.26) has a unique solution, we wil require that the matrix

$$
A = \left[ \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } &  & & & & & & & & & & & & & & & & & & & & & & & & & \\ & & & & & & & & & & & & & & & & & & \\ & & & & & & & & & & & & & & & & & & \end{array} \right]
$$

has full column rank or equivalently that $N ( { \bf G } ) \cap N ( { \bf L } ) = \{ { \bf 0 } \}$

We have already seen how to apply zeroth-order Tikhonov regularization to solve (4.25), with $\mathbf { L } = \mathbf { I }$ , using the singular value decomposition (4.16). To solve and analyze higher-order Tikhonov regularization problems, we employ the generalized singular value decomposition, or GSVD [54, 62, 65]. The GSVD enables the solution (4.25) to be expressed as a sum of filter factors times generalized singular vectors in a manner that is analogous to the series representation of the generalized inverse solution (4.16).

Unfortunately, the definition of the GSVD and associated notation are not presently standardized. In the following,we will adhere to the conventions used by the MATLAB gsvd command where $\mathbf { G }$ is an $m$ by $n$ matrix and $\mathbf { L }$ isa $p$ by $n$ matrix. Although MATLAB's implementation of the GSVD can handle matrices $\mathbf { G }$ and $\mathbf { L }$ that have overlapping null spaces, we assume in the following derivation that the matrix in (4.29) has full column rank so that the solution to (4.26) will be unique.To further simplify the derivation we will also assume that rai $ \mathbf { \nabla } \mathrm { 1 k } ( \mathbf { L } ) = p$ .This is certainly true for the $\mathbf { L }$ matrices in (4.27) and (4.28). In general we can eliminate redundant rows from $\mathbf { L }$ to make $\mathbf { L }$ have full row rank.

Under the above assumptions there exist matrices U, V, X, $\pmb { \Lambda }$ , and M with the following properties and relationships:

： $\mathbf { U }$ is $m$ by $m$ and orthogonal. $\mathbf { v }$ is $p$ by $p$ and orthogonal. $\mathbf { x }$ is $n$ by $n$ and nonsingular. $\pmb { \Lambda }$ is an $m$ by $n$ matrix with diagonal entries that may be shifted from the main diagonal of the matrix. The diagonal entries are

$$
0 \leq \Lambda _ { 1 , k + 1 } \leq \Lambda _ { 2 , k + 2 } \leq \cdot \cdot \cdot \leq \Lambda _ { m , k + m } \leq 1
$$

where $k = 0$ when $m > n$ ,and $k = n - m$ when $m \leq n$

· $\mathbf { M }$ is a $p$ by $n$ diagonal matrix with

$$
M _ { 1 , 1 } \geq M _ { 2 , 2 } \geq \cdot \cdot \cdot \geq M _ { p , p } \geq 0 ,
$$

and

$$
\mathbf { M } ^ { T } \mathbf { M } + \mathbf { A } ^ { T } \mathbf { A } = \mathbf { I } .
$$

· The matrices $\mathbf { G }$ and $\mathbf { L }$ can be written as

$$
\mathbf { G } = \mathbf { U } \mathbf { A } \mathbf { X } ^ { T }
$$

and

$$
\mathbf { L } = \mathbf { V } \mathbf { M } \mathbf { X } ^ { T } .
$$

The generalized singular values of $\mathbf { G }$ and $\mathbf { L }$ are

$$
\gamma _ { i } = \frac { \lambda _ { i } } { \mu _ { i } }
$$

where

$$
\boldsymbol { \lambda } = \sqrt { \operatorname { d i a g } ( \mathbf { A } ^ { T } \mathbf { A } ) }
$$

and

$$
\begin{array} { r } { { \boldsymbol \mu } = \sqrt { \mathop { \mathrm { d i a g } } ( \mathbf { M } ^ { T } \mathbf { M } ) } . } \end{array}
$$

These definitions may seem somewhat odd, since the diagonal elements of $\pmb { \Lambda } ^ { T } \pmb { \Lambda }$ and $\mathbf { M } ^ { T } \mathbf { M }$ are simply squares of the diagonal elements of $\pmb { \Lambda }$ and $\mathbf { M }$ .The issue here is that the diagonals of $\pmb { \Lambda }$ and $\mathbf { M }$ are not of the same length. The effect of these definitions is to create vectors $\lambda$ and $\mu$ that are of length $n$ ， padding with zeros as needed.

Because of the ordering of $\lambda$ and $\mu$ ， the generalized singular values appear in ascending order with

$$
\gamma _ { 1 } \leq \gamma _ { 2 } \leq \cdot \cdot \cdot \leq \gamma _ { n } .
$$

Also note that if $\mu _ { i } = 0$ , then the corresponding generalized singular value $\gamma _ { i }$ is infinite or undefined.

Letting ${ \bf Y } = { \bf X } ^ { - T }$ (the inverse transpose), we can apply (4.33)and the orthogonality of $\mathbf { U }$ to show that

$$
\mathbf { Y } ^ { T } \mathbf { G } ^ { T } \mathbf { G } \mathbf { Y } = \mathbf { A } ^ { T } \mathbf { A } .
$$

Note that

$$
\lambda _ { i } = \sqrt { \mathbf { Y } _ { \cdot , i } ^ { T } \mathbf { G } ^ { T } \mathbf { G } \mathbf { Y } _ { \cdot , i } } = \Vert \mathbf { G } \mathbf { Y } _ { \cdot , i } \Vert _ { 2 } .
$$

Whenever $\lambda _ { i }$ is O,this means that the corresponding column of $\mathbf { Y }$ is in $N ( \mathbf G )$ . However, when $\lambda _ { i }$ is nonzero, the corresponding column of $\mathbf { Y }$ is not in $N ( \mathbf G )$ . Since $\mathbf { Y }$ is nonsingular, the columns of $\mathbf { Y }$ are linearly independent. If we pick $r$ so that $\lambda _ { r } = 0$ ,but $\lambda _ { r + 1 } \neq 0$ ，then $r$ is the dimension of $N ( \mathbf G )$ , and the vectors $\mathbf { Y } _ { \cdot , 1 } , \ \mathbf { Y } _ { \cdot , 2 } , \ \ldots \ , \ \mathbf { Y } _ { \cdot , r }$ form a basis for $N ( \mathbf G )$ . Note that because rank $( { \bf G } ) + \mathrm { d i m } ( N ( { \bf G } ) ) = n$ ，we have determined that rank $( \mathbf { G } ) = n - r$

Similarly, it is easy to use (4.34) and the orthogonality of $\mathbf { v }$ to show that

$$
\mathbf { Y } ^ { T } \mathbf { L } ^ { T } \mathbf { L } \mathbf { Y } = \mathbf { M } ^ { T } \mathbf { M } .
$$

Since rank $( \mathbf { L } ) = p$ , the dimension of the null space of $\mathbf { L }$ is $n - p$ .Thus $\mu _ { p + 1 }$ ， $\begin{array} { r } { \mu _ { p + 2 } , \ldots . } \end{array}$ $\mu _ { n }$ are O,and the vectors $\mathbf { Y } _ { \cdot , p + 1 }$ ， $\mathbf { Y } _ { \cdot , p + 2 }$ $\mathbf { Y } _ { \cdot , n }$ form a basis for $N ( \mathbf { L } )$ . Note that the columns of $\mathbf { Y }$ are not generally orthogonal, so we have not found orthonormal bases for the null spaces of $\mathbf { G }$ and $\mathbf { L }$

The GSVD may be computationally expensive (or intractable for very large problems) to evaluate. However, as with the SVD, once the decomposition matrices are computed, solutions to least squares problems may be calculated very easily. We begin by introducing the change of variables

$$
\mathbf { Y } \mathbf { x } = \mathbf { m } .
$$

With this substitution, the normal equations for (4.26) become

$$
\left( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) \mathbf { Y } \mathbf { x } = \mathbf { G } ^ { T } \mathbf { d } .
$$

Using (4.33) and (4.34), and ${ \bf Y } = { \bf X } ^ { - T }$ ,we have

$$
\begin{array} { r } { \left( \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { A } \mathbf { Y } ^ { - 1 } + \alpha ^ { 2 } \mathbf { Y } ^ { - T } \mathbf { M } ^ { T } \mathbf { V } ^ { T } \mathbf { V } \mathbf { M } \mathbf { Y } ^ { - 1 } \right) \mathbf { \Psi } \mathbf { Y } \mathbf { x } = \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { d } , } \\ { \left( \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { A } \mathbf { Y } ^ { - 1 } + \alpha ^ { 2 } \mathbf { Y } ^ { - T } \mathbf { M } ^ { T } \mathbf { M } \mathbf { Y } ^ { - 1 } \right) \mathbf { \Psi } \mathbf { Y } \mathbf { x } = \mathbf { Y } ^ { - T } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { d } , } \end{array}
$$

and, finally,

$$
\left( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } \right) \mathbf { x } = \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { d } .
$$

The matrix on the left-hand side of this system of equations is diagonal. Multiplying both sides by the inverse of this diagonal matrix gives the solution

$$
x _ { i } = \frac { \lambda _ { i } \mathbf { U } _ { \cdot , i + k } ^ { T } \mathbf { d } } { \lambda _ { i } ^ { 2 } + \alpha ^ { 2 } \mu _ { i } ^ { 2 } } ,
$$

where,as in (4.30), $k = 0$ when $m > n$ ，and $k = n - m$ when $m \leq n$ . In terms of the generalized singular values,this can be written as

$$
x _ { i } = \frac { \gamma _ { i } ^ { 2 } } { \gamma _ { i } ^ { 2 } + \alpha ^ { 2 } } \frac { \mathbf { U } _ { \cdot , i + k } ^ { T } \mathbf { d } } { \lambda _ { i } } .
$$

Substituting this expression for $x _ { i }$ into $\mathbf { m } = \mathbf { Y } \mathbf { x }$ ,we obtain the summation formula

$$
{ \bf { m } } _ { \alpha , L } = \sum _ { i = 1 } ^ { n } { \frac { { \gamma } _ { i } ^ { 2 } } { { \gamma } _ { i } ^ { 2 } + { \alpha } ^ { 2 } } } \frac { { \bf { U } } _ { \cdot , i + k } ^ { T } \bf { d } } { { \lambda } _ { i } } { Y } _ { \cdot , i }
$$

where

$$
f _ { i } = \frac { \gamma _ { i } ^ { 2 } } { \gamma _ { i } ^ { 2 } + \alpha ^ { 2 } }
$$

are GSVD flter factors that are analogous to the filter factors obtained in the series expression for the zeroth-order Tikhonov regularized solution (4.17). In evaluating this sum,we sometimes encounter situations in which $\gamma _ { i }$ is infinite.In those cases, the filter factor $f _ { i }$ should be set to 1. Similarly, there are situations in which $\lambda _ { i } = 0$ and $\gamma _ { i } = 0$ ， producing an expression of the form $0 ^ { 2 } / 0$ in the sum. These terms should be treated as O.

When $\mathbf { G }$ comes from a Fredholm integral equation of the first kind, the GSVD typically has two properties that were also characteristic of the SVD. First, the $m$ nonzero generalized singular values $\prime _ { n } , \gamma _ { n - 1 } , \gamma _ { n - m + 1 }$ from (4.35) trend toward zero without any obvious break. Second, the vectors $\mathbf { U } _ { \cdot , i } , \mathbf { V } _ { \cdot , i } , \mathbf { X } _ { \cdot , i } ,$ and $\mathbf { Y } _ { \cdot , i }$ tend to become rougher as $\gamma _ { i }$ decreases.

# Example 4.4

We return to the vertical seismic profiling example previously discussed in Examples 1.3 and 1.9. Here, consider a $1 { - } \mathrm { k m }$ deep borehole experiment discretized using $m = n = 5 0$ observation and model points, corresponding to sensors every $2 0 ~ \mathrm { m }$ and $2 0 ~ \mathrm { m }$ thick, constant-slowness model layers. Figure 4.1O shows the test model that we will try to recover. A synthetic data set was generated with $N ( 0 , ( 2 \times 1 0 ^ { - 4 } \mathrm { s } ) ^ { 2 } )$ noise added.

The discretized system of equations $\mathbf { G m } = \mathbf { d }$ has a small condition number (64). This happens in part because we have chosen a very coarse discretization, which effectively regularizes the problem by discretization. Another reason is that the vertical seismic profiling problem is only mildly ill-posed [45]. Figure 4.11 shows the least squares solution, together with $9 5 \%$ confidence intervals.

From the statistical point of view, this solution is completely acceptable. However, suppose that from other information,we believe the slowness should vary smoothly with depth. We will next apply higher-order Tikhonov regularization to obtain smooth solutions to this problem.

Figure 4.12 shows the first-order Tikhonov regularization L-curve for this problem. The L-curve has a distinct corner near $\alpha \approx 1 2 2$ . Figure 4.13 shows the corresponding solution. The first-order regularized solution is much smoother than the least squares solution,and is much closer to the true solution.

Figure 4.14 shows the L-curve for second-order Tikhonov regularization, which has a corner near $\alpha \approx 1 9 6 5$ . Figure 4.15 shows the corresponding solution. This solution is smoother still compared to the first-order regularized solution.Both the first- and second-order solutions depart most from the true solution at shallow depths where the true slowness has the greatest slope and curvature. This happens because the first- and second-order Tikhonov regularized solutions are biased towards flatness and secondderivative smoothness, respectively.

Figure 4.16 shows filter factors corresponding to these first- and second-order solu-tions. Higher-order terms in (4.49)are severely downweighted in both cases, particularly in the second-order case. Because of the smoothness of the true model, the model seminorms can be reduced considerably through the selection of relatively large regularization parameters, $\alpha$ , without large data misfit increases. In this example the 2-norms of the difference between the first- and second-order solutions and the true model (discretized into 5O values) are approximately $1 . 2 \times 1 0 ^ { - 5 } ~ \mathrm { s / k m }$ and $1 . 0 \times 1 0 ^ { - 5 } \ \mathrm { s / k m }$ ， respectively.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/f8ac13daf3af33e06fd6c1c81c52a29a19d9560452ca39467edc800c4d7db11c.jpg)  
Figure 4.12 L-curve and corner for the VSP problem,first-order regularization.   
Figure 4.13 Tikhonov solution for the VSP problem,first-order regularization, $\alpha = 1 2 2$ ，shown in comparison with the true model (Figure 4.10).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/c5cc24f7455bbaa000256f0282a82f439e35c6a814170531921ae613d64436fa.jpg)  
Figure 4.14 L-curve and corner for the VSP problem,second-order regularization.   
Figure 4.15 Tikhonov solution for the VSP problem,second-order regularization, $\alpha = 2 3 4 1$ , shown in comparison with the true model (Figure 4.10).

# 4.5. RESOLUTION IN HIGHER-ORDER TIKHONOV REGULARIZATION

As with zeroth-order Tikhonov regularization, we can compute a resolution matrix for higher-order Tikhonov regularization. For a particular roughening matrix $\mathbf { L }$ and value of $\alpha$ , the Tikhonov regularization solution can be written as

$$
\mathbf { m } _ { \alpha , L } = \mathbf { G } ^ { \sharp } \mathbf { d }
$$

where

$$
\mathbf { G } ^ { \sharp } = ( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } ) ^ { - 1 } \mathbf { G } ^ { T } .
$$

Using the GSVD, we can write this expression as

$$
\begin{array} { r l } & { \mathbf { G } ^ { \sharp } = ( \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { A } \mathbf { X } ^ { T } + \alpha ^ { 2 } ( \mathbf { X } \mathbf { M } ^ { T } \mathbf { V } ^ { T } \mathbf { V } \mathbf { M } \mathbf { X } ^ { T } ) ) ^ { - 1 } \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } } \\ & { \quad = ( \mathbf { X } \mathbf { A } ^ { T } \mathbf { A } \mathbf { X } ^ { T } + \alpha ^ { 2 } ( \mathbf { X } \mathbf { M } ^ { T } \mathbf { M } \mathbf { X } ^ { T } ) ) ^ { - 1 } \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } } \\ & { \quad = ( \mathbf { X } ( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } ) \mathbf { X } ^ { T } ) ^ { - 1 } \mathbf { X } \mathbf { A } ^ { T } \mathbf { U } ^ { T } } \\ & { \quad = \mathbf { X } ^ { - T } ( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } ) ^ { - 1 } \mathbf { A } ^ { T } \mathbf { U } ^ { T } . } \end{array}
$$

The model resolution matrix is then

$$
\begin{array} { r l } & { \mathbf { R } _ { \mathrm { m } } = \mathbf { G } ^ { \sharp } \mathbf { G } } \\ & { \quad \quad = \mathbf { X } ^ { - T } ( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } ) ^ { - 1 } \mathbf { A } ^ { T } \mathbf { U } ^ { T } \mathbf { U } \mathbf { A } \mathbf { X } ^ { T } } \\ & { \quad \quad = \mathbf { X } ^ { - T } \mathbf { F } \mathbf { X } ^ { T } , } \end{array}
$$

where

$$
\mathbf { F } = \left( \mathbf { A } ^ { T } \mathbf { A } + \alpha ^ { 2 } \mathbf { M } ^ { T } \mathbf { M } \right) ^ { - 1 } \mathbf { \Lambda } \mathbf { A } ^ { T } \mathbf { A }
$$

is a diagonal matrix of GSVD filter factors (4.50).

# Example 4.5

To examine the resolution of the Tikhonov regularized inversions of Example 4.4, we perform a spike test using (4.59). Figure 4.17 shows the effect of multiplying $\mathbf { R } _ { \mathrm { m } }$ times a unit amplitude spike model (at depth $5 0 0 ~ \mathrm { m } ,$ ）under first-and second-order Tikhonov regularization using $\alpha$ values of 122 and 2341,respectively. These curves can equivalently be conceptualized as rows/columns of the full resolution matrix at the index corresponding to $5 0 0 ~ \mathrm { m }$ .The spike test results indicate that these Tikhonov regularized solutions are smoothed versions of the spike model. Under first- or second-order regularization, the resolution of various model features will depend critically on how smooth or rough these features are in the true model. In Figures 4.13 and 4.15, the higher-order solutions recover the true model better because the true model is smooth. Conversely, the spike model is not well recovered because of its rapid variation.

# 4.6.THE TGSVD METHOD

In the discussion of the SVD in Chapter 3, we examined the TSVD method of regularization,which rejects model space basis vectors associated with smaller singular values. Equivalently, this can be thought of as a damped SVD solution in which filter factors of one are used for basis vectors associated with larger singular values,and filter factors of zero are used for basis vectors associated with smaller singular values.This approach can be extended to the GSVD solution (4.49) to produce a truncated generalized singular value decomposition or TGSVD solution. In the TGSVD solution we simply assign filter factors (4.5O) of one to the $q$ largest generalized singular values terms in the sum to obtain

$$
\mathbf { m } _ { q , L } = \sum _ { i = n - q + 1 } ^ { n } \frac { \mathbf { U } _ { \cdot , i + k } ^ { T } \mathbf { d } } { \lambda _ { i } } Y _ { \cdot , i }
$$

# Example 4.6

Applying the TGSVD method to the VSP problem, we find L-curve corners near $q = 8$ in the first-order case shown in Figure 4.18,and $q = 7$ in the second-order case shown in Figure 4.19. Examining the filter factors obtained for the corresponding Tikhonov solu-tions shown in Figure 4.16, we find that they decay precipitously with decreasing index near these locations.Figures 4.2O and 4.21 show the corresponding TGSVD solutions.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/2e904022208bc3e41f3cb3b6c9716a902920b0c7e0c5f1bdc728d01afe3a9054.jpg)  
Figure 4.18 TGSVD L-curve for the VSP problem as a function of $q$ for first-order regularization with the $q = 8$ solution indicated.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/5a7d99b6d7868ca8cd365bc44b210ca1ed29a67e389513f892042449e5844e43.jpg)  
Figure 4.19 TGSVD L-curve for the VSP problemas a function of $q$ for second-order regularization with the $q = 7$ solution indicated.   
Figure 4.20 TGSVD solution of the VSP problem, $q = 8$ ,first-order regularization,shown in comparison with the true model.

The model recovery is comparable to that obtained with the Tikhonov method. The 2-norms of the difference between the first- and second-order solutions and the true model are approximately $1 . 0 \times 1 0 ^ { - 2 } \mathrm { s / k m }$ and $7 . 1 \times 1 0 ^ { - 3 } \mathrm { s / k m }$ , respectively, which are similar to the Tikhonov solutions in Example 4.4.

# 4.7. GENERALIZED CROSS-VALIDATION

Generalized cross-validation (GCV) is an alternative method for selecting a regularization parameter, $\alpha$ , that has a number of desirable statistical properties.

In ordinary or“leave-one-out” cross-validation,we consider the models that are obtained by leaving one of the $m$ data points out of the fitting process.Consider the modified Tikhonov regularization problem in which we ignore a data point $d _ { k }$ ，

$$
\operatorname* { m i n } \sum _ { i \neq k } ( ( \mathbf G \mathbf { m } ) _ { i } - d _ { i } ) ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } \mathbf { m } \| _ { 2 } ^ { 2 }
$$

Call the solution tothis roblem $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ ， where the superscript indicates that $d _ { k }$ was left out ofthecomputation.Ideallythemodel $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ would accurately predict themsing data value $d _ { k }$ . In the leave-one-out approach, we select the regularization parameter $\alpha$ so as to minimize the predictive errors for all $k$ ：

$$
\operatorname* { m i n } g ( \alpha ) = \frac { 1 } { m } \sum _ { k = 1 } ^ { m } ( ( \mathbf { G } \mathbf { m } _ { \alpha , L } ^ { [ k ] } ) _ { k } - d _ { k } ) ^ { 2 } .
$$

Unfortunately, computing $g ( \alpha )$ involves solving $m$ problems of the form (4.62). Generalized cros-validation is a way to speed up this computation.

First, let

$$
\widetilde { d } _ { i } = \left\{ \begin{array} { l l } { ( { \bf G m } _ { \alpha , L } ^ { [ k ] } ) _ { k } } & { i = k } \\ { d _ { i } } & { i \neq k . } \end{array} \right.
$$

Note that because $( \mathbf { G m } _ { \alpha , L } ^ { [ k ] } ) _ { k } = \tilde { d } _ { k }$ ， $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ also solves

$$
\mathrm { m i n } ( ( { \bf G m } ) _ { k } - \tilde { d } _ { k } ) ^ { 2 } + \sum _ { i \neq k } ( ( { \bf G m } ) _ { i } - \tilde { d } _ { i } ) ^ { 2 } + \alpha ^ { 2 } \| { \bf L m } \| _ { 2 } ^ { 2 } ,
$$

which is equivalent to

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \tilde { \mathbf { d } } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } \mathbf { m } \| _ { 2 } ^ { 2 } .
$$

This result is known as the leave-one-out lemma. By this lemma,

$$
\mathbf { m } _ { \alpha , L } ^ { [ k ] } = \mathbf { G } ^ { \sharp } \tilde { \mathbf { d } } .
$$

We will use (4.67) to eliminate $\mathbf { m } _ { \alpha , L } ^ { [ k ] }$ from (4.63), because

$$
\frac { ( \mathbf { G } \mathbf { G } ^ { \sharp } \tilde { \mathbf { d } } ) _ { k } - ( \mathbf { G } \mathbf { G } ^ { \sharp } \mathbf { d } ) _ { k } } { \tilde { d } _ { k } - d _ { k } } = ( \mathbf { G } \mathbf { G } ^ { \sharp } ) _ { k , k } ,
$$

where $( \mathbf { G G } ^ { \sharp } ) _ { k , k }$ are the diagonal elements of the data resolution matrix (4.21). Subtracting both sides of the equation from 1 gives

$$
\frac { \tilde { d } _ { k } - d _ { k } - ( { \bf G } { \bf G } ^ { \sharp } \tilde { \bf d } ) _ { k } + ( { \bf G } { \bf G } ^ { \sharp } { \bf d } ) _ { k } } { \tilde { d } _ { k } - d _ { k } } = 1 - ( { \bf G } { \bf G } ^ { \sharp } ) _ { k , k } .
$$

Since $( \mathbf { G } \mathbf { G } ^ { \sharp } \mathbf { d } ) _ { k } = ( \mathbf { G } \mathbf { m } _ { \alpha , L } ) _ { k }$ $( \mathbf { G G } ^ { \sharp } \mathbf { \tilde { d } } ) _ { k } = \mathbf { \tilde { d } } _ { k } .$ and $( \mathbf { G m } _ { \alpha , L } ^ { [ k ] } ) _ { k } = \tilde { d } _ { k } ,$ ，quation (4.69) simplifies to

$$
\frac { ( \mathbf { G } \mathbf { m } _ { \alpha , L } ) _ { k } - d _ { k } } { ( \mathbf { G } \mathbf { m } _ { \alpha , L } ^ { [ k ] } ) _ { k } - d _ { k } } = 1 - ( \mathbf { G } \mathbf { G } ^ { \sharp } ) _ { k , k } .
$$

Rearranging this formula and substituting into (4.63), we obtain

$$
g ( \alpha ) = \frac { 1 } { m } \sum _ { k = 1 } ^ { m } \left( \frac { ( { \bf G m } _ { \alpha , L } ) _ { k } - d _ { k } } { 1 - ( { \bf G } { \bf G } ^ { \sharp } ) _ { k , k } } \right) ^ { 2 } .
$$

We can simplify the formula further by replacing the $( \mathbf { G G } ^ { \sharp } ) _ { k , k }$ with the average value

$$
( \mathbf { G } \mathbf { G } ^ { \sharp } ) _ { k , k } \approx \frac { 1 } { m } \mathrm { T r } ( \mathbf { G } \mathbf { G } ^ { \sharp } ) ,
$$

which gives an expression for the (4.63) that can be evaluated as a function of $\alpha$ ：

$$
\begin{array} { c l } { { \displaystyle g ( { \boldsymbol \alpha } ) \approx \frac { 1 } { m } \sum _ { k = 1 } ^ { m } \frac { ( ( { \bf G m } _ { { \boldsymbol \alpha } , L } ) _ { k } - d _ { k } ) ^ { 2 } } { ( \frac { 1 } { m } ( m - \mathrm { T r } ( { \bf G G } ^ { \sharp } ) ) ) ^ { 2 } } } } \\ { { \displaystyle = \frac { m \| { \bf G m } _ { { \boldsymbol \alpha } , L } - { \bf d } \| _ { 2 } ^ { 2 } } { \mathrm { T r } ( { \bf I } - { \bf G G } ^ { \sharp } ) ^ { 2 } } . } } \end{array}
$$

It can be shown that under reasonable assumptions regarding the noise and smoothness of $\mathbf { m _ { \mathrm { t r u e } } }$ , the value of $\alpha$ that minimizes (4.74) approaches the value that minimizes $E [ \mathbf { G m } _ { \alpha , L } - \mathbf { d } _ { \mathrm { t r u e } } ]$ as the number of data points $m$ goes to infinity, and that under the same assumptions, $E [ \| \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { m } _ { \alpha , L } \| _ { 2 } ]$ goes to O as $m$ goes to infinity [36,170]. In practice,the size of the data set is fixed in advance,so the limit is not directly applicable. However, these results provide a theoretical justification for using the GCV method to select the Tikhonov regularization parameter.

# Example 4.7

Figures 4.22 and 4.23 show $g ( \alpha )$ for the VSP test problem, using first- and second-order Tikhonov regularization, respectively. Respective GCV function (4.74) minima occur

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/d7eb388b07f0c55e61b9f80de22d73af50a55424c8d2e847750115e3586a481f.jpg)  
Figure 4.22 GCV curve for the VSP problem and its minimum,first-order regularization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/b2efae813f9c2f7a285d82ceb0d12f028b38ad3d01ac0e295b5c2744b864297a.jpg)  
Figure 4.23 GCV curve for the VSP problem and its minimum,second-order regularization.   
Figure 4.24 GCV solution for the VSP problem,first-order, $\alpha = 7 6 . 3$ ,shown in comparison with the true model.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/2ebdf2b563581777c3ca81a7d151ee59d6d31106b352be34f6f625b2272d70c2.jpg)  
Figure 4.25 GCV solution for the VSP problem,second-order, $\alpha = 9 8 1$ , shown in comparison with the true model.

near $\alpha = 7 6 . 3$ and $\alpha = 9 8 1$ ，which are somewhat smaller than the $\alpha$ values estimated previously using the L-curve (Example 4.4). The corresponding models (Figures 4.24 and 4.25) thus have somewhat larger seminorms.

# 4.8.ERROR BOUNDS

We next present two theoretical results that help to address the accuracy of Tikhonov regularization solutions. We will present these results in a simplified form, covering only zeroth-order Tikhonov regularization.

The first question is whether for a particular value of the regularization parameter, $\alpha$ ,we can establish a bound on the sensitivity of the regularized solution to the noise in the observed data d and/or errors in the system matrix $\mathbf { G }$ ，This would provide a sort of condition number for the inverse problem. Note that this does not tell us how far the regularized solution is from the true model, since Tikhonov regularization has introduced a bias in the solution. Under Tikhonov regularization with a nonzero $\alpha$ ，we would not obtain the true model even if the noise was O.

The following theorem gives a bound for zeroth-order Tikhonov regularization [65].A slightly more complicated formula is available for higher-order Tikhonov regularization [65].

Theorem 4.1 Suppose that the problems

$$
m i n \ \| \mathbf G \mathbf m - \mathbf d \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf m \| _ { 2 } ^ { 2 }
$$

and

$$
m i n \ \| \bar { \bf G } { \bf m } - \bar { \bf d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| { \bf m } \| _ { 2 } ^ { 2 }
$$

are solved to obtain $\mathbf { m } _ { \alpha }$ and $\bar { \mathbf { m } } _ { \alpha }$ . Then

$$
\frac { \| \mathbf { m } _ { \alpha } - \bar { \mathbf { m } } _ { \alpha } \| _ { 2 } } { \| \mathbf { m } _ { \alpha } \| _ { 2 } } \leq \frac { \bar { \kappa } _ { \alpha } } { 1 - \epsilon \bar { \kappa } _ { \alpha } } \left( 2 \epsilon + \frac { \| \mathbf { e } \| _ { 2 } } { \| \mathbf { d } _ { \alpha } \| _ { 2 } } + \epsilon \bar { \kappa } _ { \alpha } \frac { \| \mathbf { r } _ { \alpha } \| _ { 2 } } { \| \mathbf { d } _ { \alpha } \| _ { 2 } } \right)
$$

where

$$
\begin{array} { r l } & { \bar { \kappa } _ { \alpha } = \frac { \| \mathbf { G } \| _ { 2 } } { \alpha } } \\ & { \mathbf { E } = \mathbf { G } - \bar { \mathbf { G } } } \\ & { \mathbf { e } = \mathbf { d } - \bar { \mathbf { d } } } \\ & { \epsilon = \frac { \| \mathbf { E } \| _ { 2 } } { \| \mathbf { G } \| _ { 2 } } } \end{array}
$$

$$
\mathbf { d } _ { \alpha } = \mathbf { G } \mathbf { m } _ { \alpha }
$$

and

$$
\mathbf { r } _ { \alpha } = \mathbf { d } - \mathbf { d } _ { \alpha } .
$$

In the particular_case when $\mathbf { G } = \bar { \mathbf { G } }$ ， and the only difference between the two problems is $\mathbf { e } = \mathbf { d } - \bar { \mathbf { d } }$ ,the inequality becomes even simpler

$$
\frac { \| \mathbf { m } _ { \alpha } - \bar { \mathbf { m } } _ { \alpha } \| _ { 2 } } { \| \mathbf { m } _ { \alpha } \| _ { 2 } } \leq \bar { \kappa } _ { \alpha } \frac { \| \mathbf { e } \| _ { 2 } } { \| \mathbf { d } _ { \alpha } \| _ { 2 } } .
$$

The condition number $\bar { \kappa } _ { \alpha }$ is inversely proportional to $\alpha$ . Thus increasing $\alpha$ will decrease the sensitivity of the solution to perturbations in the data.Of course, increasing $\alpha$ also increases the error in the solution due to regularization bias and decreases resolution.

The second question is whether we can establish any sort of bound on the norm of the difference between the regularized solution and the true model. This bound would incorporate both sensitivity to noise and the bias introduced by Tikhonov regularization. Such a bound must of course depend on the magnitude of the noise in the data. It must also depend on the particular regularization parameter chosen. Tikhonov developed a beautiful theorem that addresses this question in the context of inverse problems involving IFKs [161]. More recently, Neumaier has developed a version of Tikhonov's theorem that can be applied directly to discretized problems [116].

Recall that in a discrete ill-posed linear inverse problem,the matrix $\mathbf { G }$ commonly has a smoothing effect, in that when we multiply $\mathbf { G m }$ ，the result is smoother than m. Similarly, if we multiply $\mathbf { G m }$ by $\mathbf { G } ^ { T }$ , the result will be even smoother than $\mathbf { G m }$ This smoothing in such problems is a consequence of the fact that the singular vectors corresponding to the larger singular values of $\mathbf { G }$ are smooth.Note, however, that this is not a universal property of all matrices; for example, if $\mathbf { G }$ is a matrix that approximates the differentiation operator, then $\mathbf { G m }$ will be rougher than $\mathbf { m }$

For discrete ill-posed problems,models in the range of $\mathbf { G } ^ { T }$ will form a relatively smooth subspace of all possible models in $R ^ { n }$ . Models in this subspace can be written using the range of $\mathbf { G } ^ { T }$ as a basis as $\mathbf { m } = \mathbf { G } ^ { T } \mathbf { w }$ ,using the coefficients w. Furthermore, models in the range of $\mathbf { G } ^ { T } \mathbf { G }$ form a subspace of $R ( \mathbf { G } ^ { T } )$ , since any model in $R ( \mathbf G ^ { T } \mathbf G )$ can be written as $\mathbf { m } = \mathbf { G } ^ { T } ( \mathbf { G } \mathbf { w } )$ ， which is a linear combination of columns of $\mathbf { G } ^ { T }$ Because of the smoothing effect of $\mathbf { G }$ and $\mathbf { G } ^ { T }$ ， we would expect these models to be even smoother than the models in $R ( \mathbf G ^ { T } )$ . We could construct smaller subspaces of $R ^ { n }$ that contain even smoother models, but it turns out that with zeroth-order Tikhonov regularization these are the only subspaces of interest.

There is another way to see that models in $R ( \mathbf G ^ { T } )$ will be relatively smooth. Recall that the vectors $\mathbf { V } _ { \cdot , 1 } , \mathbf { V } _ { \cdot , 2 } , \ldots . \cdot , \mathbf { V } _ { \cdot , p }$ from the SVD of $\mathbf { G }$ form an orthonormal basis for $R ( \mathbf { G } ^ { T } )$ . For discrete ill-posed problems, we know from Chapter 3 that these basis vectors will be relatively smooth,so linear combinations of these vectors in $R ( \mathbf G ^ { T } )$ should be smooth.

The following theorem gives a bound on the total error including bias due to regularization and error due to noise in the data for zeroth-order Tikhonov regularization [116].

Theorem 4.2 Suppose that we use zeroth-order Tikhonov regularization with regularization parameter α to solve $\mathbf { G m } = \mathbf { d }$ ，and that $\mathbf { m _ { \mathrm { t r u e } } }$ can be expressed as one of the following distinct cases, for some W, and as parameterized by $p$ ，

$$
\mathbf { m } _ { \mathrm { t r u e } } = \left\{ \begin{array} { l l } { \mathbf { G } ^ { T } \mathbf { w } } & { p = 1 } \\ { \mathbf { G } ^ { T } \mathbf { G } \mathbf { w } } & { p = 2 } \end{array} \right.
$$

and that

$$
\| \mathbf { G m } _ { \mathrm { t r u e } } - \mathbf { d } \| _ { 2 } \leq \Delta \| \mathbf { w } \| _ { 2 }
$$

for some $\Delta > 0$ . Then

$$
\| \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { G } ^ { \sharp } \mathbf { d } \| _ { 2 } \leq \left( \frac { \Delta } { 2 \alpha } + \gamma \alpha ^ { p } \right) \| \mathbf { w } \| _ { 2 } ,
$$

where

$$
\gamma = \left\{ { \begin{array} { l l } { 1 / 2 } & { p = 1 } \\ { 1 } & { p = 2 } \end{array} } . \right.
$$

Furthermore, if we begin with the bound

$$
\| \mathbf { G m } _ { \mathrm { t r u e } } - \mathbf { d } \| _ { 2 } \leq \delta ,
$$

we can let

$$
\Delta = { \frac { \delta } { \| \mathbf { w } \| _ { 2 } } } .
$$

Under this condition the optimal value ofα is

$$
\hat { \alpha } = \left( \frac { \Delta } { 2 \gamma p } \right) ^ { \frac { 1 } { p + 1 } } = { \cal O } ( \Delta ^ { \frac { 1 } { p + 1 } } ) .
$$

With this choice of $\alpha$

$$
\Delta = 2 \gamma p \hat { \alpha } ^ { p + 1 }
$$

and the eror bound simplifes to

$$
\begin{array} { r } { \| \mathbf { m } _ { \mathrm { t r u e } } - \mathbf { G } _ { \hat { \alpha } } ^ { \sharp } \mathbf { d } \| _ { 2 } \leq \gamma ( p + 1 ) \hat { \alpha } ^ { p } | | \mathbf { w } | | _ { 2 } = O ( \Delta ^ { \frac { p } { p + 1 } } ) . } \end{array}
$$

Theorem 4.2 tels us that the error in the Tikhonov regularization solution depends on both the noise level $\delta$ and on the regularization parameter $\alpha$ . For larger values of $\alpha$ , the error due to regularization in recovering the true model will be dominant. For smaller values of $\alpha$ ,the error due to noise in the data will be dominant.We seek the optimal value of $\alpha$ that best balances these effects.Using the optimal $\alpha$ , (4.93) indicates that we can obtain an error bound of $O ( \Delta ^ { 2 / 3 } )$ if $p = 2$ ,and an error bound of $O ( \Delta ^ { 1 / 2 } )$ if $p = 1$

Of course, the above result can only be applied when our true model lives in the restricted subspace of $R ( \mathbf { G } ^ { T } )$ . In practice,even if the model does lie in $R ( \mathbf { G } ^ { T } )$ ，the vector w could have a very large norm, making the bound uninformative.

Thus, applying this theorem in a quantitative fashion is typically impractical. However, the theorem does provide some useful insight into the ability of Tikhonov regularization to recover a true model. The first point is that the accuracy of the regu-larized solution depends very much on the smoothness of the true model. If $\mathbf { m _ { \mathrm { t r u e } } }$ is not smooth, then Tikhonov regularization simply will not give an accurate solution. Furthermore, if the model $\mathbf { m _ { \mathrm { t r u e } } }$ is smooth, then we can hope for an error in the Tikhonov regularized solution which is ${ \cal O } ( \delta ^ { 1 / 2 } )$ or $O ( \delta ^ { 2 / 3 } )$ . Another way of saying this is that we can hope at best for an answer with about two thirds as many correct significant digits as the data.

# Example 4.8

Recall the Shaw problem previously considered in Examples 4.1 and 4.3. Because $\mathbf { G } ^ { T }$ is a nonsingular matrix, the spike model should lie in $R ( \mathbf { G } ^ { T } )$ . However, $\mathbf { G } ^ { T }$ is numerically singular due to the ill-posedness of the problem,and the spike model thus lies outside of the effective range of $\mathbf { G } ^ { T }$ . Any unregularized attempt to find w produces a meaningless answer due to numerical instability. Because the spike model does not lie in $R ( \mathbf { G } ^ { T } )$ ， Theorem 4.2 does not apply.

Figure 4.26 shows a smooth model that does lie in the range of $\mathbf { G } ^ { T }$ . For this model we constructed a synthetic data set with noise as before at $\delta = 4 . 4 7 \times 1 0 ^ { - 6 }$ . Equa-tion (4.93) suggests using $\alpha = 8 . 0 \times 1 0 ^ { - 4 }$ . The resulting error bound is $8 . 0 \times 1 0 ^ { - 4 }$ ， while the actual norm of the model error is $6 . 6 \times 1 0 ^ { - 4 }$ . Here the data were accurate to roughly six digits, while the solution was accurate to roughly four digits. Figure 4.27 shows the reconstruction of the model with $N ( 0 , ( 1 . 0 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ noise added to the data vector, showing that the solution is well recovered. This example once again demon-strates the importance of smoothness in the true model in determining how accurately it can be reconstructed with Tikhonov regularization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/cc5b2bc8fd6eb25c5fa55d6ba69da8f997e56f36af13a84d013edde4181da312.jpg)  
Figure 4.26 A smooth model in $R ( \mathbf G ^ { T } )$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0002_pages_0071-0140/auto/images/b062e076f44b41c3975a13218efdf102a7802527e9396824482b6b551cdd66a5.jpg)  
Figure 4.27 Reconstruction of the smooth model with $N ( 0 , ( 1 . 0 \times 1 0 ^ { - 6 } ) ^ { 2 } )$ noise.

# 4.9. EXERCISES

1. Use the method of Lagrange multipliers (Appendix C) to derive the damped least squares problem (4.4) from the discrepancy principle problem (4.2),and demonstrate that (4.4) can be written as (4.5).

2. Consider the integral equation and data set from Problem 3.5. You can find a copy of this data set in the file ifk.mat.

a. Discretize the problem using simple collocation.

b.Using the data supplied,and assuming that the numbers are accurate to four significant figures, determine a reasonable bound δ for the misfit.

c.Use zeroth-order Tikhonov regularization to solve the problem. Use GCV, the discrepancy principle,and the L-curve criterion to pick the regularization parameter.

d.Use first-order Tikhonov regularization to solve the problem. Use GCV, the discrepancy principle,and the L-curve criterion to pick the regularization parameter.

e.Use second-order Tikhonov regularization to solve the problem. Use GCV, the discrepancy principle,and the L-curve criterion to pick the regularization parameter.

f.Analyze the resolution of your solutions. Are the features you see in your inverse solutions unambiguously real? Interpret your results. Describe the size and location of any significant features in the solution.

3. Consider the following problem in cross-well tomography. Two vertical wells are located $1 6 0 0 \mathrm { ~ m ~ }$ apart.A seismic source is inserted in one well at depths of 50,150,. ．．, $1 5 5 0 ~ \mathrm { m }$ . A string of receivers is inserted in the other well at depths of $5 0 ~ \mathrm { m }$ ， $1 5 0 \ \mathrm { m }$ 。.， $1 5 5 0 \mathrm { ~ m ~ }$ . See Figure 4.28. For each source-receiver pair,a travel time is recorded, with a measurement standard deviation of $0 . 5 ~ \mathrm { m s }$ . There are 256 ray paths and 256 corresponding data points. We wish to determine the velocity structure in the two-dimensional plane between the two wells.

Discretizing the problem into a 16 by 16 grid of 10O meter by 10O meter blocks gives 256 model parameters. The $\mathbf { G }$ matrix and noisy data,d, for this problem (assuming straight ray paths) are in the file crosswell.mat. The order of parameter indexing from the slowness grid to the model vector is row by row (e.g., Example 1.12).

a.Use the TSVD to solve this inverse problem using an L-curve. Plot the result.   
b. Use zeroth-order Tikhonov regularization to solve this problem and plot your solution.Explain why it is difficult to use the discrepancy principle to select the regularization parameter. Use the L-curve criterion to select your regularization parameter. Plot the L-curve as well as your solution.   
c.Use second-order Tikhonov regularization to solve this problem and plot your solution.Because this is a two-dimensional problem, you wil need to implement a finite-difference approximation to the Laplacian (second derivative in the

horizontal direction plus the second derivative in the vertical direction） in the roughening matrix. The $\mathbf { L }$ matrix can be generated using the following MATLAB code:

L=zeros( $1 4 \star 1 4 , 2 5 6 )$ ；   
$k { = } 1$ ；   
for $\mathsf { i } = 2 : 1 5$ ， for $\mathrm { j } = 2 : 1 5$ ， $\mathsf { M } =$ zeros(16,16); $\mathsf { M } ( \mathrm { ~ i ~ } , \mathrm { ~ j ~ } ) = - 4$ ； M(i, $\mathrm { j } + 1 ) = 1$ ； M $1 ( \mathrm { ~ i ~ } , \mathrm { ~ j ~ } \cdot 1 ) { = } 1$ ； $\mathsf { M } ( \mathrm { ~ i + 1 ~ } , \mathrm { ~ j ~ } ) { = } \mathrm { 1 }$ ； $\mathsf { M } ( \mathrm { ~ i ~ } - 1 , \mathrm { ~ j ~ } ) { = } \mathrm { 1 }$ ； L(k，:) $=$ reshape(M,256,1)'; $k { = } k { + } 1$ ； end   
end

What, if any, problems did you have in using the L-curve criterion on this problem? Plot the L-curve as well as your solution.

d. Discuss your results. If vertical bands appeared in some of your solutions, can you explain why?

4.Apply second-order Tikhonov regularization to solve the problem of finding a smooth curve that approximately fits a set of noisy data points. Write a MAT-LAB program to find a function specified at the 191 points $x = 1$ ,1.1,1.2,  . . ,20 that approximately fits the 2O data points specified at $x = 1$ ,2,3,..．,20 given in the file interpdata.mat. Construct an appropriate 2O by $1 9 1 \textbf { G }$ matrix,and use the library function get_lrough to obtain the necessary second-order roughening matrix, L. Produce solutions for regularization parameter values of $\alpha =$ 0.2, 0.4, O.6,...，1O and show the tradeoff curve between 2-norm data misfit and model seminorm on a linear-linear plot. If the data noise is independent and normally distributed with a standard deviation of O.3,use the discrepancy principle to find and plot an optimal interpolated curve along with the data points. What is the $\chi ^ { 2 }$ value of this solution? Is it reasonable?

5. In some situations it is appropriate to bias the regularized solution toward a particular model $\mathbf { m } _ { 0 }$ . In this case, we would solve

$$
\operatorname* { m i n } \ \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L ( m - m } _ { 0 } ) \| _ { 2 } ^ { 2 } .
$$

Write this as an ordinary linear least squares problem. What are the normal equations? Can you find a solution for this problem using the GSVD?

# 4.10.NOTES AND FURTHER READING

Hansen’s book [65] is a very complete reference on the linear algebra of Tikhonov regularization. Arnold Neumaier's tutorial [116] is also a very useful reference. Two other surveys of Tikhonov regularization are [44, 45]. Vogel [169] includes an extensive discussion of methods for selecting the regularization parameter. Hansen's MATLAB Regularization Tools [64] is a collection of software for performing regularization within MATLAB.

The GSVD was first defined by Van Loan [1O1]. References on the GSVD and algorithms for computing the GSVD include [3, 53, 62, 65].

Selecting the regularization parameter is an important problem in both theory and practice.Much of the literature on functional analytic approaches assumes that the noise level is known. When the noise level is known, the discrepancy principle provides a scheme for selecting the regularization parameter for il-posed problems that is conver-gent in the sense that, in the limit as the noise level goes to zero, the regularized solution goes to $\mathbf { m _ { \mathrm { t r u e } } }$ [45].

In practice, the noise level is often unknown, so there has been a great deal of interest in schemes for selecting the regularization parameter without its prior knowledge. The two most popular approaches are the L-curve method and GCV. The L-curve method was introduced by Hansen [63, 65]. GCV was introduced by Craven and Wahba [36, 170]. The formula for GCV given here is very expensive to compute for large problems. A GCV algorithm for large-scale problems is given by Golub and von Matt [54]. Vogel has shown that the L-curve method can fail to converge [168]. It can be shown that no scheme that depends only on noisy data without knowledge of the noise level can be convergent in the limit as the noise level goes to zero [45].

Within statistics, poorly conditioned linear regression problems are said to sufer from “multicollinearity”A method called“ridge regression,” which is identical to Tikhonov regularization,is often used to deal with such problems [4O]. Statisticians also use a method called “principal components regression” (PCR)，which is identical to the TSVD method [113].

# Discretizing Problems Using Basis Functions

# Synopsis

Techniques for discretizing continuous inverse problems characterized by Fredholm integral equations of the first kind using continuous basis functions are discussed,both for general basis functions and for representers. The Gram matrix is defined and used in analyzing these problems. The method of Backus and Gilbert is also introduced.

# 5.1.DISCRETIZATION BY EXPANSION OF THE MODEL

To this point,we have discretized continuous inverse problems using the collocation scheme discussed in Chapter 1. In this chapter, we discuss an alternative approach in which we expand the unknown model $m ( x )$ in terms of a set of basis functions.

We begin with a Fredholm integral equation of the first kind,

$$
d ( x ) = \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) d \xi .
$$

Note from Section A.11 that we can generalize linear algebra, including the concepts of linear independence, dot products,orthogonality, and the 2-norm, to spaces defined by functions. We will assume that our model $m ( x )$ lies in the space $L _ { 2 } ( a , \ b )$ of functions that are square integrable on $[ a , b ]$

In $L _ { 2 } ( a , \ b )$ , the dot product of two functions $f ( x )$ and $g ( x )$ is defined as

$$
\langle f ( x ) , g ( x ) \rangle = \intop _ { a } ^ { b } f ( x ) g ( x ) \ d x ,
$$

the 2-norm of $f ( x )$ is

$$
\| f ( x ) \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } f ( x ) ^ { 2 } ~ d x } } ,
$$


<!-- chunk 0003: pages 141-210 -->
and the distance between two functions under this norm is

$$
\| f ( x ) - g ( x ) \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } ( f ( x ) - g ( x ) ) ^ { 2 } ~ d x } } .
$$

Ideally, we could try to solve the Tikhonov regularization problem

$$
\begin{array} { c } { \displaystyle \operatorname* { m i n } _ { { \mathbf \xi } } \| m ( x ) \| _ { 2 } } \\ { \displaystyle \left\| \displaystyle \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) \ d \xi - d ( x ) \right\| _ { 2 } \le \Delta . } \end{array}
$$

However, in practical cases,we do not fully know $d ( x )$ in the sense that we normally have a finite number of data points $d _ { 1 } = d ( x _ { 1 } )$ ， $d _ { 2 } = d ( x _ { 2 } )$ ，.， $d _ { m } = d ( x _ { m } )$ arranged in a vector d. An appropriate approach is thus to minimize the model norm $\| m ( x ) \| _ { 2 }$ subject to a constraint on the misfit at the data points:

$$
\begin{array} { c } { { \operatorname* { m i n } \| m ( x ) \| _ { 2 } } } \\ { { \| \mathbf { g } ( m ( x ) ) - \mathbf { d } \| _ { 2 } \leq \delta , } } \end{array}
$$

where

$$
\mathbf { g } ( m ) = \left[ \begin{array} { l } { b } \\ { \int _ { a } ^ { b } g ( x _ { 1 } , \xi ) m ( \xi ) \ d \xi } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { 2 } , \xi ) m ( \xi ) \ d \xi } } \\ { \int _ { a } ^ { b } g ( x _ { 2 } , \xi ) m ( \xi ) \ d \xi } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { m } , \xi ) m ( \xi ) \ d \xi } } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { m } , \xi ) m ( \xi ) \ d \xi } } \\ { \phantom { \int _ { a } ^ { b } g ( x _ { m } , \xi ) m ( \xi ) \ d \xi } } \end{array} \right] .
$$

Consider a finite dimensional subspace $H$ of $L _ { 2 } ( a , \ b )$ ,with the basis

$$
h _ { 1 } ( x ) , h _ { 2 } ( x ) , . . . . , h _ { n } ( x )
$$

so that any model $m ( x )$ in the subspace $H$ can be written uniquely as

$$
m ( x ) = \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ( x ) .
$$

We will seek the model $m ( x )$ in $H$ that has minimum norm and adequately fits the data.

Substituting (5.9) into (5.1),and considering only those points $x _ { i }$ where we have data, we obtain

$$
d ( x _ { i } ) = \int _ { a } ^ { b } g ( x _ { i } , \xi ) \left( \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ( \xi ) \right) d \xi \quad i = 1 , 2 , . . . , m .
$$

To simplify the notation, let

$$
g _ { i } ( \xi ) = g ( x _ { i } , \xi ) \quad i = 1 , 2 , . ~ . ~ . ~ , m
$$

and

$$
d _ { i } = d ( x _ { i } ) \quad i = 1 , 2 , \ldots , m .
$$

We interchange the integral and sum to get

$$
d _ { i } = \sum _ { j = 1 } ^ { n } \beta _ { j } \int _ { a } ^ { b } g _ { i } ( x ) h _ { j } ( x ) \ d x \quad i = 1 , 2 , . . . \ , m .
$$

If we let $\mathbf { G }$ be the $m \times n$ matrix with entries

$$
G _ { i , j } = \int _ { a } ^ { b } g _ { i } ( x ) h _ { j } ( x ) \ d x ,
$$

then the discretized inverse problem can be written as

$$
\mathbf { G } { \boldsymbol { \beta } } = \mathbf { d } ,
$$

which can be solved to find the functional expansion coefficients $\beta$ in (5.9) to construct the desired model.

Because of noise in the data, we do not normally desire, nor wil we be generally able, to solve (5.15) exactly. Furthermore,we typically need to regularize our solution to the inverse problem. We could try to solve

$$
\begin{array} { c } { { \operatorname* { m i n } \| \pmb { \beta } \| _ { 2 } } } \\ { { \| \mathbf { G } \pmb { \beta } - \mathbf { d } \| _ { 2 } \leq \delta . } } \end{array}
$$

However, $\| { \boldsymbol { \beta } } \| _ { 2 }$ is generally not proportional to $\| m ( x ) \| _ { 2 }$ . Instead, note that

$$
\begin{array} { l } { { \displaystyle \| m ( x ) \| _ { 2 } ^ { 2 } = \int _ { \quad \^ { d } } ^ { b } m ( x ) ^ { 2 } ~ d x } } \\ { { \displaystyle \qquad = \int _ { a } ^ { b } ~ \left( \sum _ { i = 1 } ^ { n } \beta _ { i } h _ { i } ( x ) \right) ~ \left( \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ( x ) \right) ~ d x } } \\ { { \displaystyle \qquad = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \beta _ { i } \beta _ { j } \int _ { a } ^ { b } h _ { i } ( x ) h _ { j } ( x ) ~ d x . } } \end{array}
$$

If we let $\mathbf { H }$ be the $n$ by $n$ matrix with

$$
H _ { i , j } = \int _ { a } ^ { b } h _ { i } ( x ) h _ { j } ( x ) \ d x ,
$$

then

$$
\| m ( x ) \| _ { 2 } ^ { 2 } = \pmb { \beta } ^ { T } \mathbf { H } \pmb { \beta } .
$$

The matrix $\mathbf { H }$ is called the Gram matrix of the functions $h _ { i } ( x )$ . It is relatively easy to show that $\mathbf { H }$ is a symmetric and positive definite matrix,and thus has a Cholesky factorization

$$
{ \displaystyle { \bf H } = { \bf R } ^ { T } { \bf R } } ,
$$

so that

$$
\begin{array} { c } { \| m ( \boldsymbol { x } ) \| _ { 2 } ^ { 2 } = \beta ^ { T } \mathbf { R } ^ { T } \mathbf { R } \beta } \\ { = \| \mathbf { R } \beta \| _ { 2 } ^ { 2 } . } \end{array}
$$

We can write the Tikhonov regularization problem as

$$
\operatorname* { m i n } _ { \| \mathbf { G } \pmb { \beta } - \mathbf { d } \| _ { 2 } } \interleave _ { 2 }
$$

We can use the Lagrange multiplier technique (Appendix $\textrm { C }$ ） to turn this into an unconstrained minimization problem

$$
\operatorname* { m i n } \ \| \mathbf { G } { \boldsymbol { \beta } } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { R } { \boldsymbol { \beta } } \| _ { 2 } ^ { 2 } ,
$$

where the regularization parameter $\alpha$ is selected so that we obtain a solution that adequately fits the data. This problem can easily be solved using the Cholesky factorization of the normal equations, the generalized singular value decomposition, or iterative methods discussed in Chapter 6.

Note that if we choose an orthonormal basis of functions, then

$$
H _ { i , j } = \int _ { a } ^ { b } h _ { i } ( x ) h _ { j } ( x ) \ d x = { \left\{ \begin{array} { l l } { 1 } & { i = j } \\ { 0 } & { i \not = j } \end{array} \right. }
$$

or ${ \bf H } = { \bf R } = { \bf I }$ ,and the minimization problem simplifies to (5.16).

To minimize a model derivative norm (e.g., $\| m ^ { \prime \prime } ( x ) \| _ { 2 }$ instead of $\| m ( x ) \| _ { 2 } )$ , note that because

$$
m ^ { \prime \prime } ( x ) = \sum _ { j = 1 } ^ { n } \beta _ { j } h _ { j } ^ { \prime \prime } ( x ) ,
$$

we can simply use the second derivative Gram matrix

$$
H _ { i , j } = \int _ { a } ^ { b } h _ { i } ^ { \prime \prime } ( x ) h _ { j } ^ { \prime \prime } ( x ) \ d x
$$

instead of (5.18).

The simple collocation scheme described in Chapter 1 can also be thought of as a special case of this approach,in which the $h _ { i } ( x )$ basis functions are“boxcar” functions centered at the measurement points $x _ { i }$ .A variety of other bases have been used in practice.For example, sine and cosine functions can be used to produce solutions that are Fourier series,and,for problems involving spherical symmetries,the spherical harmonic functions are often used. In recent years, many researchers have investigated the use of wavelet bases in the solution of inverse problems.

The choice of the finite dimensional subspace $H$ and its basis is critical to the success of this method in solving practical problems.As we have seen, the method finds the model $m ( x )$ in the subspace $H$ that minimizes $\| m ( x ) \| _ { 2 }$ subject to fitting the data. There is no guarantee that the model we obtain will actually have the minimum norm over the entire space $L _ { 2 } ( a , \ b )$ . However, if the subspace includes a sufficiently large class of functions, the resulting solution may be an adequate approximation to the solution of (5.6).

# 5.2. USING REPRESENTERS AS BASIS FUNCTIONS

A particularly interesting choice of basis is to use the representers (1.33) themselves as the basis functions. This approach results in a solution that does effectively minimize $\| m ( x ) \| _ { 2 }$ over the entire space $L _ { 2 } ( a , \ b )$

Consider the space $G$ spanned by the representers

$$
g _ { j } ( \xi ) = g ( x _ { j } , \xi ) \quad j = 1 , 2 , . ~ . ~ . ~ , m .
$$

Let $G ^ { \perp }$ be the perpendicular complement of $G . \ G ^ { \perp }$ consists of the functions $f ( x )$ in $L _ { 2 } ( a , b )$ such that

$$
\int _ { a } ^ { b } f ( x ) g _ { j } ( x ) \ d x = 0 \quad j = 1 , 2 , . . . , m .
$$

Thus every function $f ( x )$ in $G ^ { \perp }$ is in the null space of the forward operator. Every function $m ( x )$ in $L _ { 2 } ( a , \ b )$ can be written uniquely as

$$
m ( x ) = m _ { 1 } ( x ) + m _ { 2 } ( x )
$$

where $m _ { 1 } ( x )$ is in $G$ and $m _ { 2 } ( x )$ is in $G ^ { \perp }$ . By the Pythagorean theorem,

$$
\| m ( x ) \| _ { 2 } ^ { 2 } = \| m _ { 1 } ( x ) \| _ { 2 } ^ { 2 } + \| m _ { 2 } ( x ) \| _ { 2 } ^ { 2 } .
$$

Since any nonzero function $m _ { 2 } ( x )$ would have no effect on the fit to the data but would increase $\| m ( x ) \| _ { 2 }$ ， the optimal norm-minimizing solution to (5.6） will always have $m _ { 2 } ( x ) = 0$ . This means that minimizing $\| m ( x ) \| _ { 2 }$ over our subspace $G$ will be equivalent to minimizing $\| m ( x ) \| _ { 2 }$ over all of $L _ { 2 } ( a , \ b )$

The Gram matrix of the representers, $\mathbf { \Gamma } ^ { \Gamma }$ ,has entries

$$
\Gamma _ { i , j } = \int _ { a } ^ { b } g _ { i } ( x ) g _ { j } ( x ) \ d x .
$$

In terms of this matrix,

$$
\| m ( x ) \| _ { 2 } ^ { 2 } = \pmb { \beta } ^ { T } \pmb { \Gamma } \pmb { \beta } ,
$$

so that the discretized Tikhonov regularization problem (5.22) becomes

$$
\begin{array} { l } { \operatorname* { m i n } \| \mathbf { R } \pmb { \beta } \| _ { 2 } } \\ { \| \mathbf { r } \pmb { \beta } - \mathbf { d } \| _ { 2 } \le \delta , } \end{array}
$$

where $\mathbf { R }$ is the Cholesky factorization of $\mathbf { \Gamma } ^ { \Gamma }$

Can we extend this approach to minimizing a derivative-based model roughness measure (e.g., $\| m ^ { \prime \prime } ( x ) ) \|$ as we did in (5.26)? It is still true that adding a nonzero function $m _ { 2 } ( x )$ from $G ^ { \perp }$ to $m ( x )$ will have no effect on the fit to the data. Unfortunately, derivatives of models in $G$ and $G ^ { \perp }$ will no longer generally satisfy the orthogonality relationship (5.30), that is,

$$
\| m ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } \neq \| m _ { 1 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } + \| m _ { 2 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } ,
$$

because orthogonality of two functions $f ( x )$ and $g ( x )$ does not imply orthogonality of $f ^ { \prime \prime } ( x )$ and $g ^ { \prime \prime } ( x )$ . Because adding a nonzero function $m _ { 2 } ( x )$ from $G ^ { \perp }$ might actually decrease $\| m ^ { \prime \prime } ( x ) \| _ { 2 }$ ，minimizing $\| m ^ { \prime \prime } ( x ) \| _ { 2 }$ over our subspace $G$ in this case will not be equivalent to minimizing over $L _ { 2 } ( a , b )$

# 5.3.THE METHOD OF BACKUS AND GILBERT

The method of Backus and Gilbert [2, 126] is applicable to continuous linear inverse problems of the form

$$
d ( x ) = \int _ { a } ^ { b } g ( x , \xi ) m ( \xi ) \ d \xi ,
$$

where we have observations at points $x _ { 1 } , x _ { 2 } , . . . . , x _ { n }$ .Let

$$
d _ { j } = d ( x _ { j } ) \quad j = 1 , 2 , \ldots , m
$$

and

$$
g _ { j } ( \xi ) = g ( x _ { j } , \xi ) \quad j = 1 , 2 , . ~ . ~ . ~ , m .
$$

Using (5.35), we can write the $d _ { j }$ in terms of the true model, $m _ { \mathrm { t r u e } }$ ,as

$$
\begin{array} { l } { { d _ { j } = \displaystyle \int _ { a } ^ { b } g ( x _ { j } , \xi ) m _ { \mathrm { t r u e } } ( \xi ) \ d \xi } } \\ { { \displaystyle \quad = \displaystyle \int _ { a } ^ { b } g _ { j } ( \xi ) m _ { \mathrm { t r u e } } ( \xi ) \ d \xi . } } \end{array}
$$

The Backus and Gilbert method estimates $m _ { \mathrm { t r u e } } ( x )$ at some point $\hat { x }$ ， given the $m$ data values $d _ { j }$ . The method produces model estimates that are linear combinations of the data elements

$$
\hat { m } = \sum _ { j = 1 } ^ { m } c _ { j } d _ { j } \approx m _ { \mathrm { t r u e } } ( \hat { x } )
$$

where the coefficients $c _ { j }$ are to be determined.

Combining (5.37) and (5.38) gives

$$
\begin{array} { l } { { \displaystyle { \hat { m } } = \sum _ { j = 1 } ^ { m } c _ { j } \int _ { a } ^ { b } g _ { j } ( x ) m _ { \mathrm { t r u e } } ( x ) ~ d x } } \\ { { \displaystyle ~ = \int _ { a } ^ { b } \left( \sum _ { j = 1 } ^ { m } c _ { j } g _ { j } ( x ) \right) m _ { \mathrm { t r u e } } ( x ) ~ d x } } \\ { { \displaystyle ~ = \int _ { a } ^ { b } A ( x ) m _ { \mathrm { t r u e } } ( x ) ~ d x } , } \end{array}
$$

where

$$
A ( x ) = \sum _ { j = 1 } ^ { m } c _ { j } g _ { j } ( x ) .
$$

The function $A ( x )$ is caled an averaging kernel. Ideally we would like the averaging kernel to closely approximate a delta function

$$
A ( x ) = \delta ( x - \hat { x } )
$$

because, assuming exact data, (5.4O) would then produce exact agreement between the true and estimated model $( \hat { m } = m _ { \mathrm { t r u e } } ( \hat { x } ) )$ . Since this is not possible,we will instead select the coefficients so that the area under the averaging kernel is one,and so that the width of the averaging kernel around $\hat { x }$ is as small as possible.

In terms of the coefficients $\mathbf { c }$ , the unit area constraint can be writen as

$$
\int _ { a } ^ { b } A ( x ) \ d x = \int _ { a } ^ { b } \sum _ { j = 1 } ^ { m } c _ { j } g _ { j } ( x ) \ d x = \sum _ { j = 1 } ^ { m } c _ { j } \ \left( \int _ { a } ^ { b } g _ { j } ( x ) \ d x \right) = 1 .
$$

Letting

$$
q _ { j } = \int _ { a } ^ { b } g _ { j } ( x ) \ d x ,
$$

the unit area constraint (5.43) can be writen as

$$
{ \mathbf { q } } ^ { T } { \mathbf { c } } = 1 .
$$

Averaging kernel widths can be usefully characterized in a variety of ways [126]. The most commonly used measure is the second moment of $A ( x )$ about $\hat { x }$ ：

$$
\nu = \int _ { a } ^ { b } A ( x ) ^ { 2 } ( x - { \hat { x } } ) ^ { 2 } \ d x .
$$

In terms of the coeffcients $\mathbf { c }$ ,this can be writen using (5.43) as

$$
\boldsymbol { w } = \mathbf { c } ^ { T } \mathbf { H } \mathbf { c }
$$

where

$$
H _ { j , k } = \int _ { a } ^ { b } g _ { j } ( x ) g _ { k } ( x ) ( x - \hat { x } ) ^ { 2 } ~ d x .
$$

Now, the problem of finding the optimal coefficients can be writen as

$$
\begin{array} { c } { \operatorname* { m i n } \mathbf { c } ^ { T } \mathbf { H } \mathbf { c } } \\ { \mathbf { c } ^ { T } \mathbf { q } = 1 , } \end{array}
$$

which can be solved using the Lagrange multiplier technique.

In practice, the data may be noisy, and the solution may thus be unstable. For mea-surements with independent errors,the standard deviation of the estimate is given by

$$
\mathrm { V a r } ( \hat { m } ) = \sum _ { j = 1 } ^ { m } c _ { j } ^ { 2 } \sigma _ { j } ^ { 2 } ,
$$

where $\sigma _ { j }$ is the standard deviation of the $j$ th observation.

The solution can be stabilized by adding a constraint on the variance to (5.49)

$$
\begin{array} { r } { \operatorname* { m i n } \mathbf { \epsilon } ^ { T } \mathbf { H } \mathbf { c } } \\ { \mathbf { q } ^ { T } \mathbf { c } = 1 } \\ { \displaystyle \sum _ { j = 1 } ^ { n } c _ { j } ^ { 2 } \sigma _ { j } ^ { 2 } \leq \delta . } \end{array}
$$

Again,this problem can be solved by the method of Lagrange multipliers.Smaller values of 8 decrease the variance of the estimate, but restrict the choice of coefficients so that the width of the averaging kernel increases. There is thus a trade-off between stability of the solution and the width of the averaging kernel.

The method of Backus and Gilbert produces a model estimate at a particular point $\hat { x }$ It is possible to use the method to compute estimates on a grid of points $x _ { 1 }$ ， $x _ { 2 }$ ，.， $x _ { n }$ However, since the averaging kernels may not be well localized around their associated grid points,and may vary and overlap in complicated ways, this is not equivalent to the simple collocation method of model representation introduced in Chapter 1. Furthermore, such an approach requires the computationally intensive solution of (5.51) for each point. For these reasons, the method does not receive wide use.

# Example 5.1

For a spherically symmetric Earth model, the mass $M _ { e }$ and moment of inertia $I _ { e }$ are determined by the radial density $\rho ( r )$ ,where

$$
M _ { e } = \int _ { 0 } ^ { R _ { e } } \left( 4 \pi r ^ { 2 } \right) \rho \left( r \right) d r
$$

and

$$
I _ { e } = \int _ { 0 } ^ { R _ { e } } { \left( { \frac { 8 } { 3 } } \pi r ^ { 4 } \right) \rho ( r ) d r } .
$$

Using $R _ { e } = 6 . 3 7 0 8 \times 1 0 ^ { 6 } \mathrm { ~ m ~ }$ as the radius of a spherical Earth, and supposing that from astronomical measurements we can infer that $M _ { e } = 5 . 9 7 3 \pm 0 . 0 0 0 5 \times 1 0 ^ { 2 4 } { \mathrm { ~ k g } }$ and $I _ { e } =$ $8 . 0 2 \pm 0 . 0 0 5 \times 1 0 ^ { 3 7 } \ \mathrm { k g \cdot m ^ { 2 } }$ ，we will estimate the density of the Earth in the lower mantle (e.g., at $r = 5 0 0 0 ~ \mathrm { k m } ,$ , and core (e.g., at $r = 1 0 0 0 \mathrm { k m } ,$ ).

Equations (5.52) and (5.53) include terms that span an enormous numerical range. Scaling so that

$$
\hat { r } = r / R _ { e } \quad \hat { \rho } = \rho / 1 0 0 0 \quad \hat { I } _ { e } = I _ { e } / 1 0 ^ { 3 7 } \quad \hat { M } _ { e } = M _ { e } / 1 0 ^ { 2 4 }
$$

gives

$$
\hat { M } _ { e } = 0 . 2 5 8 6 \intop _ { 0 } ^ { 1 } \left( 4 \pi \hat { r } ^ { 2 } \right) \hat { \rho } ( \hat { r } ) d \hat { r }
$$

and

$$
\hat { I } _ { e } = 1 . 0 4 9 2 \int _ { 0 } ^ { 1 } \left( \frac { 8 } { 3 } \pi \hat { r } ^ { 4 } \right) \hat { \rho } ( \hat { r } ) d \hat { r } .
$$

Applying (5.49) for $r = 5 0 0 0 { \mathrm { k m } }$ gives the coefficient values $\mathbf { c } ^ { T } = [ 1 . 1 8 0 9 , - 0 . 1 5 8 8 ]$ and a corresponding model density of $5 . 8 ~ \mathrm { g } / \mathrm { c m } ^ { 3 }$ . This is a fairly accurate estimate of density for this radius,where standard earth models estimated using seismological methods [96] infer densities of approximately $5 { \mathrm { g } } / { \mathrm { c m } } ^ { 3 }$ . The associated standard deviation (5.50) is $0 . 0 0 1 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ , so there is very litle sensitivity to data uncertainty.

At $r = 1 0 0 0 ~ \mathrm { k m }$ ，we obtain the coefficients $\mathbf { c } ^ { T } = [ 2 . 5 5 3 7 , - 1 . 0 0 4 7 ]$ ,and a corre-sponding density estimate of $7 . 2 ~ \mathrm { g } / \mathrm { c m } ^ { 3 }$ . This is not an accurate estimate for the density of the inner core,where standard earth models have densities of around $1 3 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ . The corresponding standard deviation is just $0 . 0 0 5 \mathrm { g } / \mathrm { c m } ^ { 3 }$ , so this inaccuracy is not related to instability in the inverse problem.

Figure 5.1 shows the averaging kernels corresponding to these model element estimates,and explains both the successul mantle and failed core density estimates. In the mantle case, the averaging kernel has much of its area near the targeted radius of

$5 0 0 0 ~ \mathrm { k m }$ .In the core case, however, the averaging kernel has most of its area at much greater $r$ ,and little area near the target radius of $1 0 0 0 ~ \mathrm { k m }$ .The fundamental reason for this situation is that both the mass and moment of inertia are relatively insensitive to the density of the innermost earth.

# 5.4. EXERCISES

1. Consider the earth density estimation problem of Example 5.1. Apply the generalized inverse to estimate the density as a function of radius,using the given values of mass and moment of inertia. Obtain a density model composed of 2O spherical shells of equal thickness, and compare your results to a standard model.

2. Use the Gram matrix technique to discretize the integral equation from Example 5.1.

a. Solve the resulting linear system of equations,and plot the resulting model.

b. What was the condition number of $\Gamma ?$ What does this tell you about the accuracy of your solution?

3. Show that if the representers $g _ { i } ( t )$ are linearly independent, then the Gram matrix $\mathbf { \Gamma } ^ { \Gamma }$ is nonsingular.

4. Show that if the basis functions in (5.9) are orthonormal, then $\| m ( x ) \| _ { 2 } = \| \pmb { \beta } \| _ { 2 }$ Hint: Expand $\| m ( x ) \| _ { 2 } ^ { 2 }$ using (5.3),and then simplify using the orthogonality of the basis functions.

5.Recall the polynomial regression problem from Exercise 2.5. Instead of using the polynomials $1 , x , \ldots , x ^ { 1 9 }$ ,we will usethebasis ofLegendre polynomials,which are orthogonal on the interval $[ - 1 , 1 ]$ . These polynomials are generated by the recurrence relation

$$
p _ { n + 1 } ( x ) = \frac { ( 2 n + 1 ) x p _ { n } ( x ) - n p _ { n - 1 } ( x ) } { n + 1 } ,
$$

starting with

$$
p _ { 0 } ( x ) = 1
$$

and

$$
p _ { 1 } ( x ) = x .
$$

The next two Legendre polynomials are $p _ { 2 } ( x ) = ( 3 x ^ { 2 } - 1 ) / 2$ and $p _ { 3 } ( x ) = ( 5 x ^ { 3 } -$ $3 x ) / 2$ . This recurrence relation can be used both to compute coefficients of the Legendre polynomials and to compute values of the polynomials for particular values of $_ x$

Use the first 2O Legendre polynomials to ft a polynomial of degree 19 to the data from Exercise 2.5. Express your solution as a linear combination of the Legendre polynomials and also as a regular polynomial. How well-conditioned was this system of equations? Plot your solution and compare it with your solution to Exercise 2.5.

6. Construct specific examples of functions $m _ { 1 } ( x )$ and $m _ { 2 } ( x )$ in $L _ { 2 } ( - 1 , 1 )$ ，such that $m ( x ) = m _ { 1 } ( x ) + m _ { 2 } ( x )$ ， $m _ { 1 } ( x ) \perp m _ { 2 } ( x )$ ,but $\| m ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } \neq \| m _ { 1 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 } + \| m _ { 2 } ^ { \prime \prime } ( x ) \| _ { 2 } ^ { 2 }$

# 5.5.NOTES AND FURTHER READING

Techniques for discretizing integral equations are discussed in [45,126,166,172]. A variety of basis functions have been used to discretize integral equations including sines and cosines,spherical harmonics,B-splines,and wavelets.In selecting the basis functions,it is important to select a basis that can reasonably represent likely models. The basis functions must be linearly independent, so that a function can be written in terms of the basis functions in exactly one way, and (5.9) is thus unique. As we have seen, the use of an orthonormal basis has the further advantage that $\| { \pmb { \beta } } \| _ { 2 } = \| { \pmb { m } } ( { \boldsymbol { x } } ) \| _ { 2 }$

The selection of an appropriate basis for a particular problem is a fine art that requires detailed knowledge of the problem as well as of the behavior of the basis functions. Beware that a poorly selected basis may not adequately approximate the solution, resulting in an estimated model $m ( x )$ that is very wrong. The choice of basis can also have a very large effect on the condition number of the discretized problem, potentially making it very ill-conditioned.

An important theoretical question is whether the solutions to discretized versions of a continuous inverse problem with noise-free data will converge to a solution of the continuous inverse problem. Engl, Hanke,and Neubauer provide an explicit example showing that nonconvergence of a discretization scheme is possible [45]. They also provide conditions under which convergence is guaranteed. For Fredholm integral equa-tions of the first kind, the Gram matrix approach using representers can be shown to be convergent [45].

# Iterative Methods

# Synopsis

We present several methods for solving linear inverse problems that may be far too large for the methods previously discussed to be practical. These methods are iterative,in that a sequence of trial solutions is generated that converges to a final solution. Kacz-marz's algorithm and the related ART and SIRT methods form one class,while methods based on conjugate gradients form a second class. When the method of conjugate gradients is applied to the normal equations, the resulting conjugate gradient least squares (CGLS) method regularizes the solution to the inverse problem.Methods for estimat-ing model resolution for very large model spaces are described. Ilustrative examples involving tomography and image deblurring are given.

# 6.1.INTRODUCTION

Singular value decomposition (SVD)-based pseudoinverse and Tikhonov regularization solutions become impractical when we consider larger problems in which $\mathbf { G }$ has,for example,tens of thousands of rows and columns. Storing all of the elements in such a large $\mathbf { G }$ matrix can require a great deal of computer memory. If many of the elements in the $\mathbf { G }$ matrix are zero,as for example in ray-theory tomography, then $\mathbf { G }$ isa sparse matrix, and we can obviate this problem by storing only the nonzero elements of G and their locations. The density of G is the percentage of nonzero elements in the matrix.MATLAB can store sparse matrices and most built-in MATLAB functions operate eficiently on sparse matrices. Dense matrices contain enough nonzero elements that sparse storage schemes are not efficient.

Methods for the solution of linear systems of equations based on matrix factorizations such as the Cholesky factorization,QR factorization, or SVD do not tend to work well with sparse matrices. The problem is that the matrices that occur in the factorization of $\mathbf { G }$ are often more dense than $\mathbf { G }$ itself.In particular, the U and $\mathbf { v }$ matrices in the SVD and the $\mathbf { Q }$ matrix in the QR factorization are orthogonal matrices,which typically make these matrices dense.

The iterative methods discussed in this chapter do not require the storage of large dense matrices. Instead, they work by generating a sequence of models $\mathbf { m }$ that converge to an optimal solution. Steps in these algorithms typically involve multiplying $\mathbf { G }$ and $\mathbf { G } ^ { T }$ times vectors,which can be done without additional storage. Because iterative methods can also take advantage of the sparsity commonly found in the $\mathbf { G }$ matrix, they are often used for very large problems.

For example, consider a two-dimensional tomography problem where the model is of size 256 by 256 (65,536 model elements) and there are 100,000 ray paths.Each ray path will pass through less than $1 \%$ of the model cells, so the vast majority of the elements (e.g., more than $9 9 \%$ in $\mathbf { G }$ will be zero. If we stored $\mathbf { G }$ as a full matrix, it would require about 5O gigabytes (GB) of storage. Furthermore, if we wished to apply the SVD, the U matrix would require ${ 8 0 } \mathrm { G B }$ of storage, and the V matrix would require about 35 GB. Because of the extreme sparsity of $\mathbf { G }$ ,such a matrix can be stored in less than 1 GB using sparse storage.

At the time this book was written, computers with several gigabytes of main memory were common, while only computers classified as supercomputers would have hundreds or thousands of gigabytes of main memory. The point at which it becomes necessary to use sparse matrix storage depends on the computer that we are using. Although the memory capacity of computers has been increasing steadily for many years, it is safe to say that there will always be problems for which sparse matrix storage will be required. Furthermore, programs that use sparse matrix storage often run much faster than programs that do not take advantage of sparsity. Thus it is a good idea to consider using sparse storage even in cases where sufficient memory is available to store the full matrix.

# 6.2. ITERATIVE METHODS FOR TOMOGRAPHY PROBLEMS

We will concentrate in this section on Kaczmarz's algorithm and its ART and SIRT variants. These algorithms were originally developed for tomographic applications and are particularly effective for such problems.

Kaczmarz's algorithm is an easy-to-implement algorithm for solving a linear system of equations $\mathbf { G m } = \mathbf { d }$ . To understand the algorithm, note that each of the m equations $\mathbf { G } _ { i , \cdot } \mathbf { m } = d _ { i }$ defines an $n$ -dimensional hyperplane in $R ^ { m }$ . Kaczmarz's algorithm starts with an initial solution $\mathbf { m } ^ { ( 0 ) }$ ， and then moves to a solution $\mathbf { m } ^ { ( 1 ) }$ by projecting the initial solution onto the hyperplane defined by the first row in $\mathbf { G }$ Next $\mathbf { m } ^ { ( 1 ) }$ is similarly projected onto the hyperplane defined by the second row in $\mathbf { G }$ ，and so forth. The process is repeated until the solution has been projected onto all $m$ hyperplanes defined by the system of equations. At that point, a new cycle of projections begins. These cycles are repeated until the solution has converged sufficiently. Figure 6.1 shows an example in which Kaczmarz's algorithm is used to solve the system of equations

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/394c2b3299070a9e369969c3ebe77d4f56212b5450c52219416378694c3ff471.jpg)  
Figure 6.1 Kaczmarz's algorithm on a system of two equations.

$$
\begin{array} { c } { { \gamma = 1 } } \\ { { - x + \gamma = - 1 . } } \end{array}
$$

To implement the algorithm, we need a formula to compute the projection of a $i$ $\mathbf { G } _ { i + 1 , \cdot } \mathbf { m } = d _ { i + 1 }$ ${ \bf G } _ { i + 1 , } ^ { T }$ update to $\mathbf { m } ^ { ( i ) }$ from the constraint due to row $i + 1$ of $\mathbf { G }$ will be proportional to $\mathbf { G } _ { i + 1 , \cdot } ^ { T }$

$$
\mathbf { m } ^ { ( i + 1 ) } = \mathbf { m } ^ { ( i ) } + \beta \mathbf { G } _ { i + 1 , \cdot } ^ { T } .
$$

Using the fact that $\mathbf { G } _ { i + 1 , \cdot } \mathbf { m } ^ { ( i + 1 ) } = d _ { i + 1 }$ to solve for $\beta$ , we obtain

$$
\begin{array} { c } { \displaystyle { \mathbf { G } _ { i + 1 , \cdot } \Big ( \mathbf { m } ^ { ( i ) } + \beta \mathbf { G } _ { i + 1 , \cdot } ^ { T } \Big ) = d _ { i + 1 } } } \\ { \displaystyle { \mathbf { G } _ { i + 1 , \cdot } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } = - \beta \mathbf { G } _ { i + 1 , \cdot } \mathbf { G } _ { i + 1 , \cdot } ^ { T } } } \\ { \displaystyle { \beta = - \frac { \mathbf { G } _ { i + 1 , \cdot } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } } { \mathbf { G } _ { i + 1 , \cdot } \mathbf { G } _ { i + 1 , \cdot } ^ { T } } . } } \end{array}
$$

Thus the update formula is

$$
\mathbf { m } ^ { ( i + 1 ) } = \mathbf { m } ^ { ( i ) } - \frac { \mathbf { G } _ { i + 1 , } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } } { \mathbf { G } _ { i + 1 , } \mathbf { G } _ { i + 1 , } ^ { T } } \mathbf { G } _ { i + 1 , \cdot } ^ { T } .
$$

It can be shown that if the system of equations $\mathbf { G m } = \mathbf { d }$ has a unique solution, then Kaczmarz's algorithm will converge to this solution. If the system of equations has many solutions, then the algorithm will converge to the solution that is closest to the point $\mathbf { m } ^ { ( 0 ) }$ . In particular, if we start with $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$ , we will obtain a minimum length solution. If there is no exact solution to the system of equations, then the algorithm will fail to converge, but will typically bounce around near an approximate solution.

A second important question is how quickly Kaczmarz's algorithm will converge to a solution. If the hyperplanes described by the system of equations are nearly orthogonal, then the algorithm will converge very quickly. However, if two or more hyperplanes are nearly parallel to each other, convergence can be extremely slow. Figure 6.2 shows a typical situation in which the algorithm zigzags back and forth without making much progress towards a solution. As the two lines become more nearly parallel, the problem becomes worse. This problem can be alleviated by picking an ordering of the equations such that adjacent equations describe hyperplanes that are nearly orthogonal to each other. In the context of tomography, this can be done by ordering the equations so that successive equations do not share common model cells.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/d29f05fc218d4b3566648bd159e2fbed46bab3fe37354698091d2ebe86275797.jpg)  
Figure 6.2 Slow convergence occurs when hyperplanes are nearly parallel.

# Example 6.1

Consider a tomographic reconstruction problem with the same geometry used in Exercise 4.4,in which the slowness structure is parameterized in homogeneous blocks of size $l$ by l. The true model is shown in Figure 6.3. Synthetic data were generated, with normally distributed random noise added.The random noise had a standard deviation of 0.01. Figure 6.4 shows the TSVD solution. The two anomalies are apparent, but it is not possible to distinguish the small hole within the larger of the two.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/bdfa8e508cabfe305b892d4d4d4ba45310fffcd82c752b63918350e6caf5475d.jpg)  
Figure 6.3 True model.   
Figure 6.4 Truncated SVD solution.

Figure 6.5 shows the solution obtained after 2OO iterations of Kaczmarz's algorithm. This solution is extremely similar to the TSVD solution,and both solutions are about the same distance from the true model.

The algebraic reconstruction technique (ART) is a version of Kaczmarz's algorithm that has been modified especially for the tomographic reconstruction problem. In (6.6), the updates to the solution always consist of adding a multiple of a row of $\mathbf { G }$ to the current solution. The numerator in the fraction is the difference between the right-hand side of equation $i + 1$ and the value of the $i + 1$ component of $\mathbf { G m }$ .The denominator in (6.6) is simply the square of the norm of $\mathbf { G } _ { i + 1 , \cdot }$ . Effectively, Kaczmarz's algorithm is determining the error in equation $i + 1$ , and then adjusting the solution by spreading the required correction over the elements of $\mathbf { m }$ that appear in equation $i + 1$

# Algorithm 6.1Kaczmarz's Algorithm

Given a system of equations $\mathbf { G m } = \mathbf { d }$

1. Let $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$   
2.For $i = 0$ ,1,..., $m - 1$ ,let

$$
\mathbf { m } ^ { ( i + 1 ) } = \mathbf { m } ^ { ( i ) } - \frac { \mathbf { G } _ { i + 1 , } \mathbf { m } ^ { ( i ) } - d _ { i + 1 } } { \mathbf { G } _ { i + 1 , } \mathbf { G } _ { i + 1 , } ^ { T } } \mathbf { G } _ { i + 1 , \cdot } ^ { T } .
$$

3. If the solution has not yet converged, return to step 2.

A crude approximation to the Kaczmarz update, used in ART, is to replace all of the nonzero elements in row $i + 1$ of $\mathbf { G }$ with ones. We define

$$
q _ { i + 1 } = \sum _ { \mathrm { \scriptsize ~ c e l l } ~ j ~ \mathrm { i n ~ r a y ~ p a t h } ~ i + 1 } \mathbf { m } _ { j } l
$$

as an approximation to the travel time along ray path $i + 1$ ,where $l$ is the cell dimension. The difference between $q _ { i + 1 }$ and $d _ { i + 1 }$ is roughly the residual for the predicted travel time of ray $i + 1$

Examining (6.6) for the ART-modified $\mathbf { G }$ ，we see that ART simply takes the total travel time misfit for ray $i + 1$ and divides it by $l$ times the number of cells in the ray path, $N _ { i + 1 }$ . This correction factor is then multiplied by a vector that has ones in cells along ray path $i + 1$ . This procedure has the effect of smearing the needed correction in travel time equally over all of the cels in the ray path.

The ART approximate update formula can thus be written as

$$
\begin{array} { r } { m _ { j } ^ { ( i + 1 ) } = \left\{ { \begin{array} { l l } { m _ { j } ^ { ( i ) } - \frac { q _ { i + 1 } - d _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l } j \mathrm { i n } \mathrm { r a y p a t h } i + 1 } \\ { m _ { j } ^ { ( i ) } } & { \mathrm { c e l l } j \mathrm { n o t i n r a y p a t h } i + 1 . } \end{array} } \right. } \end{array}
$$

The approximation can be improved by taking into account that the ray path lengths actually will vary from cell to cell. If $L _ { i + 1 }$ is the length of ray path $i + 1$ ，the corresponding improved update formula from (6.6) for the tomography problem is

$$
m _ { j } ^ { ( i + 1 ) } = \left\{ \begin{array} { l l } { m _ { j } ^ { ( i ) } + \frac { d _ { i + 1 } } { L _ { i + 1 } } - \frac { q _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l } j \mathrm { i n \ r a y \ p a t h } i + 1 } \\ { m _ { j } ^ { ( i ) } } & { \mathrm { c e l l } j \mathrm { n o t i n \ r a y \ p a t h } i + 1 . } \end{array} \right.
$$

The main advantage of ART is that it saves storage. We need only store information about which rays pass through which cells,and we do not need to record the length of each ray in each cell. A second advantage of the method is that it reduces the number of floating-point multiplications compared to that required by Kaczmarz's algorithm. Although in current computers floating-point multiplications and additions require roughly the same amount of time,during the 197Os,when ART was first developed, multiplication was slower than addition.

# Algorithm 6.2 ART

Given a system of equations $\mathbf { G m } = \mathbf { d }$ arising from a tomography problem:

1.Let ${ \pmb m } ^ { ( 0 ) } = { \bf 0 }$   
2.For $i = 0$ ,1，...， $m$ ,let $N _ { i }$ be the number of cells traversed by ray path i.   
3.For $i = 0$ ,1，..., $m$ ,let $L _ { i }$ be the length of ray path i.

# Algorithm 6.2 (Continued)

4. For i=0,1,...,m-1,j=1,2,...,n,let

$$
\begin{array} { r } { m _ { j } ^ { ( i + 1 ) } = \left\{ \begin{array} { l l } { m _ { j } ^ { ( i ) } + \frac { d _ { i + 1 } } { L _ { i + 1 } } - \frac { q _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l } j \mathrm { i n \ r a y \ p a t h } i + 1 } \\ { m _ { j } ^ { ( i ) } } & { \mathrm { c e l l } j \mathrm { n o t i n \ r a y \ p a t h } i + 1 . } \end{array} \right. } \end{array}
$$

5. If the solution has not yet converged,let ${ \pmb m } ^ { ( 0 ) } = { \pmb m } ^ { ( m ) }$ and return to step 4. Otherwise, return the solution $\pmb { m } = \pmb { m } ^ { ( m ) }$

One problem with ART is that the resulting tomographic images tend to be noisier than images produced by Kaczmarz's algorithm (6.7). The simultaneous iterative recon-struction technique (SIRT) is a variation on ART that gives slightly better images in practice,at the expense of a slightly slower algorithm. In the SIRT algorithm, all(up to m nonzero) updates using (6.1O) are computed for each cell $j$ of the model, for each ray that passes through cell $j$ . The set of updates for cell $j$ are then averaged before updating the coresponding model element $m _ { j }$

# Algorithm 6.3 SIRT

Given a system of equations $\mathbf { G m } = \mathbf { d }$ arising from a tomography problem:

1. Let $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$

2.For $j = 0$ ,1,..., $n$ let $K _ { j }$ be the number of ray paths that passthrough cell $j$

3. For $i = 0$ ,1,..., $m$ let $L _ { i }$ be the length of ray path i.

4.For $i = 0$ ,1,..., $m$ ,let $N _ { i }$ be the number of cells traversed by ray path i.

5.Let $\Delta { \pmb m } ^ { ( i + 1 ) } = { \pmb 0 }$

6.For $i = 0$ ,1,..., $m - 1 , j = 1$ ,2，...,n,let

$$
\begin{array} { r } { \Delta m _ { j } ^ { ( i + 1 ) } = \Delta m _ { j } ^ { ( i + 1 ) } + \left\{ \begin{array} { l l } { \frac { d _ { i + 1 } } { L _ { i + 1 } } - \frac { q _ { i + 1 } } { l N _ { i + 1 } } } & { \mathrm { c e l l ~ } j \mathrm { ~ i n ~ r a y ~ p a t h ~ } i + 1 } \\ { 0 } & { \mathrm { c e l l ~ } j \mathrm { ~ n o t ~ i n ~ r a y ~ p a t h ~ } i + 1 . } \end{array} \right. } \end{array}
$$

7. For $j = 1 , 2 , \dots , n ,$ let

$$
m _ { j } ^ { ( i + 1 ) } = m _ { j } ^ { ( i + 1 ) } + \frac { \Delta m _ { j } ^ { ( i + 1 ) } } { K _ { j } } .
$$

8. Ifthe solution has not yet converged,return to step 5. Otherwise, return the current solution.

# Example 6.2

Returning to our earlier tomography example, Figure 6.6 shows the ART solution obtained after 2OO iterations. Again, the solution is very similar to the TSVD solution.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/b204a190823df5cf77077efc9485c9ddc3f0665a71d1a22b0f91cfbaf3e69b0e.jpg)  
Figure 6.6 ART solution.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/5ffa21a61400d498b01bc17d579d811e1dd5a4d6bb93fbe2ac7d69b964352d26.jpg)  
Figure 6.7 shows the SIRT solution for our example tomography problem after 200 iterations. This solution is similar to the TSVD,Kaczmarz's,and ART solutions.   
Figure 6.7 SIRT solution.

# 6.3.THE CONJUGATE GRADIENT METHOD

We next consider the conjugate gradient (CG) method for solving a symmetric and positive definite system of equations $\mathbf { A x } = \mathbf { b }$ . We will later apply the CG method to solving the normal equations for $\mathbf { G m } = \mathbf { d }$ .Consider the quadratic optimization problem,

$$
\operatorname* { m i n } \ { \phi } ( { \mathbf { x } } ) = \frac { 1 } { 2 } { \mathbf { x } } ^ { T } { \mathbf { A } } { \mathbf { x } } - { \mathbf { b } } ^ { T } { \mathbf { x } } ,
$$

where $\mathbf { A }$ is an $n \times n$ symmetric and positive definite matrix. We require A be positive definite so that the function $\phi ( \mathbf { x } )$ will be convex and have a unique minimum. We can calculate $\nabla \phi ( \mathbf { x } ) = \mathbf { A } \mathbf { x } - \mathbf { b }$ and set it equal to zero to find the minimum. The minimum occurs at a point $\mathbf { x }$ that satisfies the equation

$$
\mathbf { A x } - \mathbf { b } = \mathbf { 0 }
$$

or

$$
\mathbf { A x } = \mathbf { b } .
$$

Thus solving the system of equations $\mathbf { A x } = \mathbf { b }$ is equivalent to minimizing $\phi ( \mathbf { x } )$

The conjugate gradient method approaches the problem of minimizing $\phi ( \mathbf { x } )$ by constructing a basis for $R ^ { n }$ in which the minimization problem is extremely simple. The basis vectors $\mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \dots . . . , \mathbf { p } _ { n - 1 }$ are selected so that

$$
\mathbf { p } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { j } = 0 \quad \mathrm { w h e n } i \neq j .
$$

A collection of vectors with this property is said to be mutually conjugate with respect to A. We express $\mathbf { x }$ in terms of these basis vectors as

$$
\mathbf { x } = \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \mathbf { p } _ { i }
$$

so that

$$
\phi \left( \alpha \right) = \frac { 1 } { 2 } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \mathbf { p } _ { i } \right) ^ { T } \mathbf { A } \left( \sum _ { j = 0 } ^ { n - 1 } \alpha _ { j } \mathbf { p } _ { j } \right) - \mathbf { b } ^ { T } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \mathbf { p } _ { i } \right) .
$$

The product $\mathbf { x } ^ { T } \mathbf { A x }$ can be written as a double sum, so the equation becomes

$$
\phi ( \pmb { \alpha } ) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { n - 1 } \sum _ { j = 0 } ^ { n - 1 } \alpha _ { i } \alpha _ { j } \pmb { \mathrm { p } } _ { i } ^ { T } \pmb { \mathrm { A } } \pmb { \mathrm { p } } _ { j } - \mathbf { b } ^ { T } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \pmb { \mathrm { p } } _ { i } \right) .
$$

Since the vectors are mutually conjugate with respect to A, this simplifies to

$$
\phi \left( \pmb { \alpha } \right) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } ^ { 2 } \pmb { \mathrm { p } } _ { i } ^ { T } \pmb { \mathrm { A } } \pmb { \mathrm { p } } _ { i } - \mathbf { b } ^ { T } \left( \sum _ { i = 0 } ^ { n - 1 } \alpha _ { i } \pmb { \mathrm { p } } _ { i } \right)
$$

or

$$
\phi \left( { \pmb { \alpha } } \right) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { n - 1 } \bigl ( \alpha _ { i } ^ { 2 } { \pmb { \mathrm { p } } } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { i } - 2 \alpha _ { i } \mathbf { b } ^ { T } \mathbf { p } _ { i } \bigr ) .
$$

Equation (6.22) shows that $\phi ( { \pmb { \alpha } } )$ consists of $n$ terms,each of which is independent of the other terms. Thus we can minimize $\phi ( { \pmb \alpha } )$ by selecting each $\alpha _ { i }$ to minimize the ith term,

$$
\alpha _ { i } ^ { 2 } \mathbf { p } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { i } - 2 \alpha _ { i } \mathbf { b } ^ { T } \mathbf { p } _ { i } .
$$

Differentiating with respect to $\alpha _ { i }$ and setting the derivative equal to zero, we find that the optimal value for $\alpha _ { i }$ is

$$
\alpha _ { i } = { \frac { \mathbf { b } ^ { T } \mathbf { p } _ { i } } { \mathbf { p } _ { i } ^ { T } \mathbf { A p } _ { i } } } .
$$

This shows that if we have a basis of vectors that are mutually conjugate with respect to A, then minimizing $\phi ( \mathbf { x } )$ is very easy. We have not yet shown how to construct the mutually conjugate basis vectors.

Our algorithm will actually construct a sequence of solution vectors $\mathbf { x } _ { i }$ ，residual vectors $\mathbf { r } _ { i } = \mathbf { b } - \mathbf { A x } _ { i }$ ，and basis vectors $\mathbf { p } _ { i }$ .The algorithm begins with $\mathbf { x } _ { \mathrm { 0 } } = \mathbf { 0 }$ ， $\mathbf { r } _ { 0 } = \mathbf { b }$ ， $\mathbf { p } _ { 0 } = \mathbf { r } _ { 0 }$ ,and $\alpha _ { 0 } = ( { \bf r } _ { 0 } ^ { T } { \bf r } _ { 0 } ) / ( { \bf p } _ { 0 } ^ { T } { \bf A } { \bf p } _ { 0 } )$

Suppose that at the start of iteration $k$ of the algorithm, we have constructed $\mathbf { x } _ { \mathrm { 0 } }$ ， $\mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { k } , \mathbf { r } _ { 0 } , \mathbf { r } _ { 1 } , \ldots , \mathbf { r } _ { k } , \mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \ldots , \mathbf { p } _ { k }$ and $\alpha _ { 0 } , \alpha _ { 1 } , \ldots , \alpha _ { k }$ ，We assume that the first $k + 1$ basis vectors $\mathbf { p } _ { i }$ are mutually conjugate with respect to $\mathbf { A }$ ,the first $k + 1$ residual vectors $\mathbf { r } _ { i }$ are mutually orthogonal, and that $\mathbf { r } _ { i } ^ { T } \mathbf { p } _ { j } = 0$ when $i \neq j$

We let

$$
\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k } .
$$

This effectively adds one more term of (6.18) into the solution. Next, we let

$$
\mathbf { r } _ { k + 1 } = \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } .
$$

This correctly updates the residual, because

$$
\begin{array} { r l } & { \mathbf { r } _ { k + 1 } = \mathbf { b } - \mathbf { A x } _ { k + 1 } } \\ & { \qquad = \mathbf { b } - \mathbf { A } \big ( \mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k } \big ) } \\ & { \qquad = ( \mathbf { b } - \mathbf { A x } _ { k } ) - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } . } \end{array}
$$

We let

$$
\beta _ { k + 1 } = { \frac { \| \mathbf { r } _ { k + 1 } \| _ { 2 } ^ { 2 } } { \| \mathbf { r } _ { k } \| _ { 2 } ^ { 2 } } } = { \frac { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } } { \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } } }
$$

and

$$
\mathbf { p } _ { k + 1 } = \mathbf { r } _ { k + 1 } + \beta _ { k + 1 } \mathbf { p } _ { k } .
$$

In the following calculations,it will be useful to know that $\mathbf { b } ^ { T } \mathbf { p } _ { k } = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k }$ . This is shown by

$$
\begin{array} { r l } & { \mathbf { b } ^ { T } \mathbf { p } _ { k } = ( \mathbf { r } _ { k } + \mathbf { A x } _ { k } ) ^ { T } \mathbf { p } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { k } + \mathbf { x } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { k } + \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { x } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } ( \mathbf { r } _ { k } + \beta _ { k } \mathbf { p } _ { k - 1 } ) + \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { x } _ { k } } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + \beta _ { k } \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { k - 1 } + \mathbf { p } _ { k } ^ { T } \mathbf { A } \big ( \alpha _ { 0 } \mathbf { p } _ { 0 } + \cdot \cdot \cdot + \alpha _ { k - 1 } \mathbf { p } _ { k - 1 } \big ) } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + 0 + 0 } \\ & { \qquad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } . } \end{array}
$$

We will now show that $\mathbf { r } _ { k + 1 }$ is orthogonal to $\mathbf { r } _ { i }$ for $i \leq k$ For every $i < k$ ，

$$
\begin{array} { r } { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = ( \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } ) ^ { T } \mathbf { r } _ { i } } \\ { = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { i } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { r } _ { i } } \\ { = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { i } - \alpha _ { k } \mathbf { r } _ { i } ^ { T } \mathbf { A } \mathbf { p } _ { k } . } \end{array}
$$

Since $\mathbf { r } _ { k }$ is orthogonal to all of the earlier $\mathbf { r } _ { i }$ vectors,

$$
\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = 0 - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { r } _ { k } .
$$

Also, since $\mathbf { p } _ { i } = \mathbf { r } _ { i } + \beta _ { i } \mathbf { p } _ { i - 1 }$

$$
\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = 0 - \alpha _ { k } \big ( \mathbf { p } _ { i } - \beta _ { i } \mathbf { p } _ { i - 1 } \big ) ^ { T } \mathbf { A } \mathbf { p } _ { k } .
$$

Both $\mathbf { p } _ { i }$ and $\mathbf { p } _ { i - 1 }$ are conjugate with $\mathbf { p } _ { k }$ . Thus

$$
\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } = 0 .
$$

We also have o show that $\mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k } = 0$

$$
\begin{array} { r l } & { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k } = ( \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } ) ^ { T } \mathbf { r } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { r } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } ( \mathbf { p } _ { k } - \beta _ { k } \mathbf { p } _ { k - 1 } ) } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } ( \mathbf { p } _ { k } - \beta _ { k } \mathbf { p } _ { k - 1 } ) ^ { T } \mathbf { A } \mathbf { p } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \alpha _ { k } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { k } + \alpha _ { k } \beta _ { k } \mathbf { p } _ { k - 1 } ^ { T } \mathbf { A } \mathbf { p } _ { k } } \\ & { \quad \quad \quad = \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } - \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + \alpha _ { k } \beta _ { k } 0 } \\ & { \quad \quad \quad = 0 . } \end{array}
$$

Next, we will show that $\mathbf { r } _ { k + 1 }$ is orthogonal to $\mathbf { p } _ { i }$ for $i \leq k$

$$
\begin{array} { r l } & { \mathbf { r } _ { k + 1 } ^ { T } \mathbf { p } _ { i } = \mathbf { r } _ { k + 1 } ^ { T } \big ( \mathbf { r } _ { i } + \beta _ { i } \mathbf { p } _ { i - 1 } \big ) } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } + \beta _ { i } \mathbf { r } _ { k + 1 } ^ { T } \mathbf { p } _ { i - 1 } } \\ & { \qquad = 0 + \beta _ { i } \mathbf { r } _ { k + 1 } ^ { T } \mathbf { p } _ { i - 1 } } \\ & { \qquad = \beta _ { i } \big ( \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \mathbf { p } _ { k } \big ) ^ { T } \mathbf { p } _ { i - 1 } } \\ & { \qquad = \beta _ { i } ( \mathbf { r } _ { k } ^ { T } \mathbf { p } _ { i - 1 } - \alpha _ { k } \mathbf { p } _ { i - 1 } ^ { T } \mathbf { A } \mathbf { p } _ { k } ) } \\ & { \qquad = \beta _ { i } ( 0 - 0 ) = 0 . } \end{array}
$$

Finally, we need to show that $\mathbf { p } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } = 0$ for $i \leq k$ For $i < k$ ，

$$
\begin{array} { r l } & { \mathbf { p } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } = ( \mathbf { r } _ { k + 1 } + \boldsymbol { \beta } _ { k + 1 } \mathbf { p } _ { k } ) ^ { T } \mathbf { A } \mathbf { p } _ { i } } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } + \boldsymbol { \beta } _ { k + 1 } \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { i } } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { i } + 0 } \\ & { \qquad = \mathbf { r } _ { k + 1 } ^ { T } \left( \frac { 1 } { \alpha _ { i } } ( \mathbf { r } _ { i } - \mathbf { r } _ { i + 1 } ) \right) } \\ & { \qquad = \cfrac { 1 } { \alpha _ { i } } \left( \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i } - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { i + 1 } \right) } \\ & { \qquad = 0 . } \end{array}
$$

For $i = k$

$$
\begin{array} { r l } & { \mathbf { p } _ { k + 1 } ^ { T } \mathbf { A } \mathbf { p } _ { k } = \left( \mathbf { r } _ { k + 1 } + \beta _ { k + 1 } \mathbf { p } _ { k } \right) ^ { T } \Bigg ( \frac { 1 } { \alpha _ { k } } ( \mathbf { r } _ { k } - \mathbf { r } _ { k + 1 } ) \Bigg ) } \\ & { \qquad = \frac { 1 } { \alpha _ { k } } \Big ( \beta _ { k + 1 } \big ( \mathbf { r } _ { k } + \beta _ { k } \mathbf { p } _ { k - 1 } \big ) ^ { T } \mathbf { r } _ { k } - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } \Big ) } \\ & { \qquad = \frac { 1 } { \alpha _ { k } } \big ( \beta _ { k + 1 } \mathbf { r } _ { k } ^ { T } \mathbf { r } _ { k } + \beta _ { k + 1 } \beta _ { k } \mathbf { p } _ { k - 1 } ^ { T } \mathbf { r } _ { k } - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } \big ) } \\ & { \qquad = \frac { 1 } { \alpha _ { k } } \big ( \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } + \beta _ { k + 1 } \beta _ { k } 0 - \mathbf { r } _ { k + 1 } ^ { T } \mathbf { r } _ { k + 1 } \big ) } \\ & { \qquad = 0 . } \end{array}
$$

We have now shown that the algorithm generates a sequence of mutually conju-gate basis vectors. In theory, the algorithm will find an exact solution to the system of equations in $n$ iterations.In practice,due to round-off errors in the computation, the exact solution may not be obtained in $n$ iterations.In practical implementations of the algorithm, we iterate until the residual is smaler than some tolerance that we specify. The algorithm can be summarized as follows.

# Algorithm 6.4 Conjugate Gradient Method

Given a positive definite and symmetric system of equations $\mathbf { A x } = \mathbf { b }$ ，and an initial solution $\mathbf { x } _ { \mathrm { 0 } }$ ,let $\beta _ { - 1 } = 0$ ， $\mathbf { p } _ { - 1 } = \mathbf { 0 }$ ， $\mathbf { r } _ { 0 } = \mathbf { b } - \mathbf { A x } _ { 0 }$ ,and $k = 0$

1. Let $\mathbf { p } _ { k } = - \mathbf { r } _ { k } + \beta _ { k - 1 } \mathbf { p } _ { k - 1 }$   
2. Let $\begin{array} { r } { \alpha _ { k } = \frac { \| \mathbf { r } _ { k } \| _ { 2 } ^ { 2 } } { \mathbf { p } _ { k } ^ { T } \mathbf { A } \mathbf { p } _ { k } } } \end{array}$   
3. Let Xk+1 = Xk +αkPk.   
4. Let $\mathbf { r } _ { k + 1 } = \mathbf { r } _ { k } + \alpha _ { k } \mathbf { A } \mathbf { p } _ { k }$   
5.Let βk=1   
6.Let $k = k + 1$   
7. Repeat the previous steps until convergence.

A major advantage of the CG method is that it requires storage only for the vectors $\mathbf { x } _ { k }$ ， $\mathbf { p } _ { k }$ ， $\mathbf { r } _ { k }$ ， and the symmetric matrix A. If A is large and sparse, then sparse matrix techniques can be used to store A more efficiently. Unlike factorization methods such as QR, SVD, or Cholesky factorization, there will be no fill-in of the zero elements in A at any stage in the solution process. Thus it is possible to solve extremely large systems using CG in cases where direct factorization would require far too much storage. In fact, the only way in which the algorithm uses A is in one multiplication of $\mathbf { A } \mathbf { p } _ { k }$ for each iteration. In some applications of the CG method, it is possible to perform these matrix vector multiplications without explicitly constructing A.

# 6.4.THE CGLS METHOD

The CG method by itself can only be applied to positive definite systems of equations, and is thus not directly applicable to general least squares problems. In the conjugate gradient least squares (CGLS) method, we solve a least squares problem,

$$
\operatorname* { m i n } \ \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ,
$$

by applying CG to the normal equations,

$$
\mathbf { G } ^ { T } \mathbf { G } \mathbf { m } = \mathbf { G } ^ { T } \mathbf { d } .
$$

In implementing this algorithm it is important to avoid round-off errors. One important source of error is the evaluation of the residual, $\mathbf { G } ^ { T } \mathbf { G } \mathbf { m } - \mathbf { G } ^ { T } \mathbf { d } .$ It turns out that this calculation is more accurate when we factor out $\mathbf { G } ^ { T }$ and compute $\mathbf { G } ^ { T } ( \mathbf { G m - d } )$ We will use the notation $\mathbf { s } _ { k } = \mathbf { G } \mathbf { m } _ { k } - \mathbf { d }$ and $\mathbf { r } _ { k } = \mathbf { G } ^ { T } \mathbf { s } _ { k }$ . Note that we can compute $\mathbf { s } _ { k + 1 }$ recursively from $\mathbf { s } _ { k }$ as follows

$$
{ \begin{array} { r l } & { \mathbf { s } _ { k + 1 } = \mathbf { G m } _ { k + 1 } - \mathbf { d } } \\ & { \qquad = \mathbf { G } ( \mathbf { m } _ { k } + \alpha _ { k } \mathbf { p } _ { k } ) - \mathbf { d } } \\ & { \qquad = ( \mathbf { G m } _ { k } - \mathbf { d } ) + \alpha _ { k } \mathbf { G p } _ { k } } \\ & { \qquad = \mathbf { s } _ { k } + \alpha _ { k } \mathbf { G } \mathbf { p } _ { k } . } \end{array} }
$$

With this trick, we can now state the CGLS algorithm.

# Algorithm 6.5 CGLS

Given a least squares problem min $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ ,let $k = 0$ ， $\mathbf { m } _ { 0 } = \mathbf { 0 }$ ， $\mathbf { p } _ { - 1 } = \mathbf { 0 }$ ， $\beta _ { - 1 } = 0$ ， $\mathbf { s } _ { 0 } = - \mathbf { d } .$ and $\mathbf { r } _ { 0 } = \mathbf { G } ^ { T } \mathbf { s } _ { 0 }$

1. Let $\mathbf { p } _ { k } = - \mathbf { r } _ { k } + \beta _ { k - 1 } \mathbf { p } _ { k - 1 }$

3. Let $\mathbf { m } _ { k + 1 } = \mathbf { m } _ { k } + \alpha _ { k } \mathbf { p } _ { k }$

4. Let $\mathbf { s } _ { k + 1 } = \mathbf { s } _ { k } + \alpha _ { k } \mathbf { G } \mathbf { p } _ { k }$

5.Let $\mathbf { r } _ { k + 1 } = \mathbf { G } ^ { T } \mathbf { s } _ { k + 1 }$

6. Let $\beta _ { k } = { \frac { \| \mathbf { r } _ { k + 1 } \| _ { 2 } ^ { 2 } } { \| \mathbf { r } _ { k } \| _ { 2 } ^ { 2 } } }$

7. Let $k = k + 1$

8. Repeat the previous steps until convergence.

Note that this algorithm only requires one multiplication of $\mathbf { G } \mathbf { p } _ { k }$ and one multiplication of $\mathbf { G } ^ { T } \mathbf { s } _ { k + 1 }$ per iteration. We never explicitly compute $\mathbf { G } ^ { T } \mathbf { G }$ ，which might require considerable time,and which might have far more nonzero elements than $\mathbf { G }$ itself.

The CGLS algorithm has an important property that makes it particularly useful for ill-posed problems. It can be shown that, for exact arithmetic, $\| \mathbf { m } _ { k } \| _ { 2 }$ increases monotonically and $\| \mathbf { G m } _ { k } - \mathbf { d } \| _ { 2 }$ decreases monotonically with increasing iterations [61, 65]. We can use the discrepancy principle together with this property to obtain a regularized solution. Simply stop the CGLS algorithm as soon as $\| \mathbf { G m } _ { k } - \mathbf { d } \| _ { 2 } < \delta$ . In practice, this algorithm typically gives good solutions after a very small number of iterations.

An alternative way to use CGLS is to solve the Tikhonov regularization problem (4.4) by applying CGLS to

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } } .
$$

For nonzero values of the regularization parameter $\alpha$ ,this least squares problem should be reasonably well-conditioned. By solving this problem for several values of $\alpha$ ,we can compute an L-curve. The disadvantage of this approach is that the number of CGLS iterations for each value of $\alpha$ may be large,and we need to solve the problem for several values of $\alpha$ . Thus the computational effort is far greater.

# Example 6.3

A commonly used mathematical model of image blurring involves the two-dimensional convolution of the true image $I _ { \mathrm { t r u e } } ( x , \gamma )$ with a point spread function, $\Psi ( u , \nu )$ [14]:

$$
I _ { \mathrm { b l u r r e d } } ( x , \gamma ) = \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } I _ { \mathrm { t r u e } } ( x - u , \gamma - \nu ) \Psi ( u , \nu ) \ d u \ d \nu .
$$

Here the point spread function shows how a point in the true image is altered in the blurred image. A point spread function that is commonly used to represent the blurring that occurs because an image is out of focus is the Gaussian point spread function

$$
\Psi ( u , \nu ) = e ^ { \frac { u ^ { 2 } + \nu ^ { 2 } } { 2 \sigma ^ { 2 } } } .
$$

Here the parameter $\sigma$ controls the relative width of the point spread function. In prac-tice, the blurred image and point spread function are discretized into pixels. In theory, $\Psi$ is nonzero for all values of $u$ and $\nu$ ，However, it becomes small quickly as $u$ and $\nu$ increase. If we set small values of $\Psi$ to O, then the $\mathbf { G }$ matrix in the discretized problem will be sparse.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/b4153518e6eb49c6578a6bdfd9df42ff97bdb00e2e58e2a5ce2f9bd32d2fa8a9.jpg)  
Figure 6.8 Blurred image.

Figure 6.8 shows an image that has been blurred and also has a small amount of added noise. This image is of size 2OO pixels by 20O pixels,so the $\mathbf { G }$ matrix for the blurring operator is of size 4O,OOO by 40,OOO. Fortunately, the blurring matrix $\mathbf { G }$ is quite sparse, with less than $0 . 1 \%$ nonzero elements. The sparse matrix requires about $1 2 ~ \mathrm { M B }$ of storage. A dense matrix of this size would require about $1 3 \ \mathrm { G B }$ of storage. Using the SVD approach to Tikhonov regularization would require far more storage than many current computers have. However, CGLS works quite well on this problem.

Figure 6.9 shows the L-curve for the solution of this problem by CGLS without explicit regularization and by CGLS with explicit regularization. The line with circles shows the solutions obtained by CGLS without explicit regularization. For the first 30 or so iterations of CGLS without explicit regularization, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ decreases quickly. After that point, the improvement in misfit slows down, while $\| \mathbf { m } \| _ { 2 }$ increases rapidly.

Figure 6.1O shows the CGLS solution without explicit regularization after 3O iterations.The blurring has been greatly improved. Note that 3O iterations is far less than the size of the matrix $( n = 4 0 , 0 0 0 )$ . Unfortunately, further CGLS iterations do not significantly improve the image. In fact, noise builds up rapidly, both because of the accumulation of round-off errors and because the algorithm is converging slowly towards an unregularized least squares solution. Figure 6.11 shows the CGLS solution after 1OO iterations.In this image the noise has been greatly amplified, with little or no improvement in the clarity of the image.

We also computed CGLS solutions with explicit Tikhonov regularization for 22 values of $\alpha$ . For each value of $\alpha$ , 200 iterations of CGLS were performed. The resulting

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/48c406a95a64f6887326ec63e012ac1e3032e1d9791f9105616c6f2c0f38c97a.jpg)  
Figure 6.9 L-curves for CGLS deblurring.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/4f4dfd492b3ff51d3f878bd9f2b11e6ece485db56ecbcce0a0755025446154c5.jpg)  
Figure 6.10 CGLS solution after 30iterations, no explicit regularization.

L-curve is shown in Figure 6.9 with “x”markers for each regularized solution that was obtained. This L-curve is slightly better than the L-curve from the CGLS solution without explicit regularization in that the values of $\| \mathbf { m } \| _ { 2 }$ and $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ are smaller. However, it required 4O times as much computational effort. The corner solution for $\alpha = 7 . 0 \times 1 0 ^ { - 4 }$ is shown in Figure 6.12. This solution is similar to the one shown in Figure 6.10.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/8334639ea5214e08d8e5d89d1d2cd90be6ffe5121d615fc5b6f8925ca4f622ed.jpg)  
Figure 6.11 CGLS solution after 100 iterations, no explicit regularization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/bd8bf87e8444b27a813f9e0e157e4a384b1e7097eb54836807232113cfbfa3b8.jpg)  
Figure 6.12 CGLS solution,explicit regularization, $\alpha = 7 . 0 \times 1 0 ^ { - 4 }$

We have focused on the CGLS method in this section because it is particularly easy to derive and because of the implicit regularization effect of the CGLS method. However, many other iterative methods have been developed for large-scale least squares problems [5,135]. An analysis of the implicit regularizing effects of these methods can be found in Hanke [61]. The LSQR method of Paige and Saunders has been very widely used in many geophysical applications [123,124]. MATLAB has an efcient and robust implementation of LSQR in its lsqr routine.

# 6.5.RESOLUTION ANALYSIS FOR ITERATIVE METHODS

Analyzing the resolution of a regularized solution computed by the iterative methods described in this chapter is a challenging problem. The formulas developed in Chapter 4 for the model resolution matrix under zeroth-order Tikhonov regularization were based on the SVD of the $\mathbf { G }$ matrix, but as we have seen it is often unfeasible to compute the SVD of a large matrix,and even when it is extremely sparse, the SVD is typically dense. For higher-order regularization,we have formulas for the resolution matrix based on the GSVD of the $\mathbf { G }$ matrix, such as (4.2O),but it is also impractical to compute the GSVD of very large matrices.

A brute force approach that offers some advantages over the computation of the SVD or GSVD is to use (4.52) with Cholesky factorization of $( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } )$ [19]. Cholesky factorization is considerably faster in practice than computing the SVD. However, since the Cholesky factor of this matrix is typically dense,this is still a very large-scale computation that would generally need to be performed in parallel on a computer with suficient memory to store a dense $n$ by $n$ matrix.

If we want to compute an individual column of the model resolution matrix, this can be accomplished by solving an additional least squares problem. Applying the expression for the least squares Tikhonov inverse operator $\mathbf { G } ^ { \sharp }$ (4.52), the ith column of $\mathbf { R } _ { m }$ can be expressed as

$$
\begin{array} { r l } & { \mathbf { R } _ { , i } = \mathbf { R } _ { m } \mathbf { e } _ { i } } \\ & { \quad \quad = \mathbf { G } ^ { \sharp } \mathbf { G } \mathbf { e } _ { i } } \\ & { \quad \quad = \mathbf { G } ^ { \sharp } \mathbf { G } _ { . , i } } \\ & { \quad \quad = \left( \mathbf { G } ^ { T } \mathbf { G } + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) ^ { - 1 } \mathbf { G } ^ { T } \mathbf { G } _ { . , i } . } \end{array}
$$

This is (4.26), a regularized least squares problem

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathbf { R } _ { . , i } - \left[ \mathbf { \bar { G } } _ { . , i } \right] \right\| _ { 2 } ^ { 2 } }
$$

that can be solved for $\mathbf { R } _ { . , i }$ using CGLS, LSQR,or some other iterative method. We could conceivably solve (6.8O) to retrieve every column of the model resolution matrix in this manner, but this would require the solution of $n$ least squares problems.

A number of authors have considered iterative techniques for computing low-rank approximations to the resolution matrix in combination with iterative least squares solu-tion methods [12,13,174]. In such approaches, iterative methods are applied to compute the largest $k$ singular values of a matrix and the associated singular vectors. For a sparse matrix,these methods are vastly more effcient than standard algorithms for computing the SVD.

Suppose that we obtain a low-rank ( $k$ singular values and vectors) approximation to the SVD

$$
\mathbf { G } \approx \mathbf { U } _ { k } \mathbf { L } _ { k } \mathbf { V } _ { k } ^ { T }
$$

where $\mathbf { L } _ { k }$ is a $k$ by $k$ nonsingular matrix, and $\mathbf { U } _ { k }$ and $\mathbf { V } _ { k }$ are matrices with $k$ orthogonal columns. The pseudoinverse of $\mathbf { G }$ is then approximately

$$
\mathbf G ^ { \dagger } \approx \mathbf V _ { k } \mathbf L _ { k } ^ { - 1 } \mathbf U _ { k } ^ { T } .
$$

Combining these approximations,we have

$$
\mathbf { R } _ { m } \approx \mathbf { V } _ { k } \mathbf { V } _ { k } ^ { T } .
$$

Note that we would not want to explicitly multiply out $\mathbf { V } _ { k } \mathbf { V } _ { k } ^ { T }$ ， creating a huge and dense $n$ by $n$ resolution matrix. Rather, we could store the relatively smal vector $\mathbf { V } _ { k }$ and use it to compute desired entries of the $\mathbf { R } _ { m }$ matrix as needed.

A more sophisticated version of this approach is to compute a low-rank approximation to the singular value decomposition of the augmented $\mathbf { G }$ matrix [173]. Consider an augmented system of equations

$$
\mathbf { A } = { \left[ \begin{array} { l } { \mathbf { G } } \\ { \alpha \mathbf { L } } \end{array} \right] }
$$

using truncated SVD approximations for $\mathbf { A }$ and its pseudoinverse, $\mathbf { A } ^ { \dagger }$ ，

$$
\mathbf { A } \approx \mathbf { U } _ { k } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T }
$$

and

$$
\mathbf { A } ^ { \dagger } \approx \mathbf { V } _ { k } \mathbf { S } _ { k } ^ { - 1 } \mathbf { U } _ { k } ^ { T } ,
$$

where $\mathbf { U } _ { k }$ and $\mathbf { V } _ { k }$ are composed of the frst $k$ columns of $\mathbf { U }$ and $\mathbf { v }$ ,and $\mathbf { S } _ { k }$ is a square $k$ by $k$ matrix diagonal matrix of the largest $k$ singular values.

It is convenient to write $\mathbf { U } _ { k }$ as

$$
\mathbf { U } _ { k } = \left[ \mathbf { U } _ { G } \right] ,
$$

where $\mathbf { U } _ { G }$ and $\mathbf { U } _ { L }$ contain the rows of $\mathbf { U } _ { k }$ corresponding to those of $\mathbf { G }$ and $\alpha \mathbf { L }$ ， respectively, in A. We can thus partition (.85)using

$$
\mathbf { G } \approx \mathbf { U } _ { G } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T } .
$$

Given (6.88) and (6.86),we can calculate an approximation of the model resolution matrix

$$
\mathbf { R } _ { m } = \mathbf { A } ^ { \dagger } \begin{array} { c } { \left[ \mathbf { G } \right] } \\ { \mathbf { 0 } } \end{array} \approx \mathbf { V } _ { k } \mathbf { S } _ { k } ^ { - 1 } \begin{array} { c } { \left[ \mathbf { U } _ { G } ^ { T } \mathbf { U } _ { L } ^ { T } \right] } \\ { \mathbf { 0 } } \end{array} \left[ \begin{array} { c } { \mathbf { U } _ { G } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T } } \\ { \mathbf { 0 } } \end{array} \right] ,
$$

which simplifies to

$$
\mathbf { R } _ { m } \approx \mathbf { V } _ { k } \mathbf { S } _ { k } ^ { - 1 } \mathbf { U } _ { \mathrm { G } } ^ { T } \mathbf { U } _ { \mathrm { G } } \mathbf { S } _ { k } \mathbf { V } _ { k } ^ { T } .
$$

Using the identity

$$
\mathbf { U } _ { G } ^ { T } \mathbf { U } _ { G } = \mathbf { I } - \mathbf { U } _ { L } ^ { T } \mathbf { U } _ { L }
$$

we can alternatively write (6.90) as

$$
\mathbf { R } _ { m } \approx \mathbf { V } _ { k } \Big ( \mathbf { I } - \mathbf { S } _ { k } ^ { - 1 } \mathbf { U } _ { L } ^ { T } \mathbf { U } _ { L } \mathbf { S } _ { k } \Big ) \mathbf { V } _ { k } ^ { T } .
$$

Depending on the relative sizes of $\mathbf { U } _ { G }$ and $\mathbf { U } _ { L }$ ,one or the other of (6.90) or (6.92) might be more easily evaluated. Again, we would probably not want to, or be able to, explicitly multiply out the matrices to obtain the entire dense $n$ by $n$ model resolution matrix for a large problem, but could instead use (6.9O) or (6.92) to compute specific desired elements of the resolution matrix.

In practice, it may not be feasible for very large problems to compute, or even store, a sufficient number of singular values and vectors to adequately approximate the model resolution matrix using low-rank, SVD-based approximations [37]. We will thus consider an alternative stochastic approach based on [9] that estimates solely the resolution matrix diagonal, but which is not limited by low-rank matrix approximations.

Consider a sequence of $s$ random vectors from $\mathbf { R } ^ { n }$ ， $\mathbf { v } _ { 1 }$ ，..， ${ \bf v } _ { s }$ ，with independent elements drawn from a standard normal distribution. The sth corresponding estimate for the diagonal of an $n$ by $n$ square matrix $\mathbf { A }$ is given by

$$
\mathbf { q } _ { s } = \left[ \sum _ { k = 1 } ^ { s } \mathbf { v } _ { k } \odot \mathbf { A } \mathbf { v } _ { k } \right] { \boldsymbol { \oslash } } \left[ \sum _ { k = 1 } ^ { s } \mathbf { v } _ { k } \odot \mathbf { v } _ { k } \right]
$$

where $\odot$ denotes element-wise multiplication and $\oslash$ denotes element-wise division of vectors. Note that the only way in which $\mathbf { A }$ is used within this algorithm is in matrix-vector multiplications, so as long as we have a function that can implement the matrix vector multiplication, then we can implement the algorithm. As we have already seen, the multiplication of a large matrix with a vector can be effected by solving a least squares problem (6.8O). Specifically, to solve for the kth product $\mathbf { y } = \mathbf { R } _ { m }$ , we solve [103]

$$
\operatorname* { m i n } { \left\| \left[ \begin{array} { c } { \mathbf { G } } \\ { \alpha \mathbf { L } } \end{array} \right] \mathbf { y } - \left[ \begin{array} { c } { \mathbf { G } \mathbf { v } _ { k } } \\ { \mathbf { 0 } } \end{array} \right] \right\| _ { 2 } ^ { 2 } } .
$$

It is necessary to solve $s$ least squares systems of equations (6.94) to calculate (6.93). In practice, relatively small values of $s$ in (6.93) (e.g.,100 to 1000) are adequate even when there are tens or hundreds of thousands of model parameters [103].

The stochastic algorithm (6.93) can also be used to implement generalized cros-validation. In (4.74), the most difficult computation is evaluation of the trace of $\mathbf { I } - \mathbf { G } \mathbf { G } ^ { \sharp }$ . Computing this matrix explicitly and then evaluating the trace would require excessive time and storage. Using (6.93) and evaluating the necessary $\mathbf { G } ^ { \sharp }$ matrix-vector multiplications by solving an associated least squares problem using an iterative method such as LSQR or CGLS makes it tractable to compute an approximation to the GCV function (4.74), where we solve $s$ least squares problems for each value of $\alpha$ [103].

# Example 6.4

We will examine the solution to a large-scale tomography problem involving 30,000 rays passing through a cubic volume discretized into a 30 by 30 by 3O model of 27,000 cells (Figure 6.13).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/e3b1cf943a822f6c7f324ccaf72ec9983add02967f2752880d2dd55d16901731.jpg)  
Figure 6.13 A 30 by 30 by 30 block tomography model interrogated by 30,000 ray paths.

Ray path start and end points are uniformly randomly distributed across the sides of the volume with 10,OoO rays passing between each pair of parallel sides. The corresponding $\mathbf { G }$ matrix is 30,000 by 27,000,but only $0 . 2 \%$ of its entries are nonzero. Synthetic travel time data (with travel time perturbation values between approximately $- 2 0$ and 30 time units) were generated from a zero-mean smooth model with $N ( 0 , ( 0 . 5 ) ^ { 2 } )$ noise added. We implemented second-order Tikhonov regularization with a small amount of additional zeroth-order regularization to regularize the solution.

Figure 6.14 shows the L-curve for this problem. Figure 6.15 shows a plot of the GCV function (4.74) computed using stochastic estimates of the diagonal of $\mathbf { I } - \mathbf { G } \mathbf { G } ^ { \sharp }$ . The L-curve corner and GCV minimum both occur at about $\alpha = 0 . 5$ . For the solution obtained using $\alpha = 0 . 5$ , we computed a stochastic estimate of the diagonal of the reso-lution matrix using (6.93). For comparison, we also computed exact resolution matrix diagonal element values for 1OO randomly selected indices using (6.79). Figure 6.16 shows a scatter plot of the stochastic estimates compared with corresponding exact determinations, and indicates that the stochastic estimates are accurate to a few percentage points. It is common to use counts of the number of rays transecting each cell as a proxy for assessing the diagonal of the resolution matrix in tomographic problems. In general, the association between ray density and resolution in a tomography problem will depend on the specific ray path geometry. Figure 6.17 shows a scatter plot of the ray densities versus the accurately computed values of the diagonal elements of $\mathbf { R } _ { m }$ for the $1 0 0 \ \mathrm { r a n - }$ dom indices plotted in Figure 6.16. The relationship shows a nonlinear trend between ray density and the resolution diagonal element values, and there are also anomalously wel-resolved outliers in the plot with resolution diagonal element values greater than 0.9.Further examination shows that the anomalously well-resolved outliers correspond to cells that reside on the model exterior and are thus constrained by two-dimensional ray path geometries.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/48f4101596b3e1d7173be50d493a723a14666c36d6d582ad9fa83e7684b8ec7f.jpg)  
Figure 6.14 L-curve for the tomography example of Figure 6.13 and its corner near $\alpha = 0 . 5$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/983c4e6c66596e0f67ad288882ae450f299d970231d960ca37aa8578d317329a.jpg)  
Figure 6.15 GCV plot for the tomography example of Figure 6.13 and its minimum near $\alpha = 0 . 5$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/2dc515ad9c4503c62e577513ee28805d1390e3c5617dab7be445821f95305057.jpg)  
Figure 6.16 Stochastic estimates versus computed values of the diagonal of $\mathbf { R } _ { m }$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/032b28332994767fe93cc81222ad2c83f5da204f234893f408493c2db18c3762.jpg)  
Figure 6.17 Comparison of ray densities and resolution.

# 6.6. EXERCISES

1. Consider the cross-well tomography problem of Exercise 4.3.

a. Apply Kaczmarz's algorithm to this problem.   
b. Apply ART to this problem.   
c.Apply SIRT to this problem.   
d. Comment on the solutions that you obtained.

2. A very simple iterative regularization method is the Landweber iteration [67]. The algorithm begins with $\mathbf { m } ^ { ( 0 ) } = \mathbf { 0 }$ ,and then follows the iteration,

$$
\mathbf { m } ^ { ( k + 1 ) } = \mathbf { m } ^ { ( k ) } - \omega ( \mathbf { G } \mathbf { m } ^ { ( k ) } - \mathbf { d } ) .
$$

To ensure convergence, the parameter $\omega$ must be selected so that $0 < \omega < 2 / s _ { 1 } ^ { 2 }$ ， where $s _ { 1 }$ is the largest singular value of $\mathbf { G }$

In practice, the CGLS method generally works better than the Landweber iteration. However, it is easier to analyze the performance of the Landweber iteration. It can be shown that the kth iterate of the Landweber iteration is exactly the same as the SVD solution with filter factors of

$$
f _ { i } ^ { ( k ) } = 1 - ( 1 - \omega s _ { i } ^ { 2 } ) ^ { k } .
$$

a. Implement the Landweber iteration and apply it to the Shaw problem from Example 4.3.

b. Verify that $\mathbf { m } ^ { ( 1 0 ) }$ from the Landweber iteration matches the SVD solution with filter factors given by (6.96).   
c. Derive (6.96).

3.The Landweber iteration described in the previous exercise converges under the condition that $0 < \omega < 2 / s _ { 1 } ^ { 2 }$ ，where $s _ { 1 }$ is the largest singular value of $\mathbf { G }$ (or equivalently, $s _ { 1 } = \| \mathbf G \| _ { 2 } )$ . As a practical matter we typically cannot compute the full SVD of $\mathbf { G }$ . However, it is possible to rapidly estimate this quantity using an iterative method that we will derive in this exercise. Recall from Appendix A that $\| \mathbf G \| _ { 2 } = s _ { 1 }$ is the square root of the largest eigenvalue of the matrix $\mathbf { G } ^ { T } \mathbf { G }$

a. Using (A.77), diagonalize the matrix $\mathbf { A } = \mathbf { G } ^ { T } \mathbf { G }$ and use the diagonalization to show that

$$
\mathbf { A } ^ { n } = \mathbf { P } \mathbf { A } ^ { n } \mathbf { P } ^ { - 1 } .
$$

Assume that the eigenvalues of A are sorted so that $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \cdot \ \cdot \ \cdot \geq \lambda _ { n } \geq 0$

b. Take an arbitrary vector $\mathbf { x }$ in $\mathbf { R } ^ { n }$ , and write it in terms of the eigenvectors of $\mathbf { A }$ as

$$
\mathbf { x } = \alpha _ { 1 } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + \alpha _ { n } \mathbf { v } _ { n } .
$$

Then show that

$$
\mathbf { A } ^ { k } x = \alpha _ { 1 } \lambda _ { 1 } ^ { k } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + \alpha _ { n } \lambda _ { n } ^ { k } \mathbf { v } _ { n } .
$$

c. Starting with a random vector $\pmb { x } _ { 0 }$ ，and assuming that $\alpha _ { 1 } \neq 0$ (a reasonable assumption for a random vector $\pmb { x } _ { 0 }$ ),show that

$$
\operatorname* { l i m } _ { k  \infty } { \frac { \| \mathbf { A } ^ { k } \mathbf { x } _ { 0 } \| _ { 2 } } { \| \mathbf { A } ^ { k - 1 } \mathbf { x } _ { 0 } \| _ { 2 } } } = \lambda _ { 1 } .
$$

This leads to a simple iterative algorithm for estimating $s _ { 1 } = \sqrt { \lambda _ { 1 } }$ . Start with a random vector $\mathbf { x } _ { \mathrm { 0 } }$ . In each iteration, let

$$
\mathbf { x } _ { k + 1 } = \frac { \mathbf { G } ^ { T } ( \mathbf { G } \mathbf { x } _ { k } ) } { \| \mathbf { x } _ { k } \| _ { 2 } }
$$

and let

$$
\begin{array} { r } { \rho _ { k } = \sqrt { \| \mathbf G ^ { T } ( \mathbf G \mathbf x _ { k } ) \| _ { 2 } } . } \end{array}
$$

The sequence $\rho _ { k }$ converges to $s _ { 1 }$ . This function is implemented in MATLAB as the normest function. Write your own implementation of this function and compare the results you obtain with normest.

4.Use the Landweber iteration discussed in Exercise 6.2 to deblur the image from Example 6.3. In order to use the Landweber iteration, you will need to estimate $s _ { 1 } = \| \mathbf G \| _ { 2 }$ ， which can be done using the normest command discussed in Exercise 6.3.

5. In Example 6.3 we have included a function blur that computes the system matrix for the problem of deblurring an image that has been blurred by a Gaussian point spread function. The fle blur.mat contains a blur-inducing sparse $\mathbf { G }$ matrix and a data vector $\mathbf { d }$ ， where the 100 by 10O pixel gray-scale image is mapped into d using a column-by-column indexing convention.

a. How large is the $\mathbf { G }$ matrix? How many nonzero elements does it have? How much storage would be required for the $\mathbf { G }$ matrix if all of its elements were nonzero? How much storage would the SVD of $\mathbf { G }$ require?   
b. Plot the raw image.   
c. Using the MATLAB cgls algorithm with 10O iterations, deblur the image by solving $\mathbf { G m } = \mathbf { d }$ and interpret the evolution of your solutions with increasing iterations.

6. Show that if $\mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \dots . . . , \mathbf { p } _ { n - 1 }$ are nonzero and mutually conjugate with respect to an $n \times n$ symmetric and positive definite matrix A,then the vectors are also linearly independent. Hint: Use the definition of linear independence.

7. Recal the iteratively reweighted least squares method introduced in Chapter 2. The system of equations (2.92) solved in each iteration of the IRLS algorithm might well be dense, even if the matrix $\mathbf { G }$ is sparse. However, this system of equations can also be thought of as the normal equations for a particular least squares problem that will be sparse when $\mathbf { G }$ is sparse. Write down this least squares problem. Write a MATLAB function that uses the lsqr routine to solve these least squares problems in an IRLS scheme to minimize $\| \mathbf { G m } - \mathbf { d } \| _ { 1 }$ Hint: Use the fact that R is a diagonal matrix with positive elements; you can take its square root.

# 6.7. NOTES AND FURTHER READING

Iterative methods for the solution of linear systems of equations are an important topic in numerical analysis. Some basic references include [5,87,135,142].

Iterative methods for tomography problems including Kaczmarz's algorithm, ART, and SIRTare discussed in [84,115,163],and parallel algorithms based on these methodologies are discussed in [3O]. These methods are often referred to as row action methods because they access only one row of the matrix at a time, which makes them relatively easy to implement in parallel processing. In practice, the conjugate gradient and LSQR methods generally provide better performance than the row action methods. There are some interesting connections between SIRT and the conjugate gradient method discussed in [120,146,147].

Hestenes and Stiefel are generally credited with the invention of the conjugate gradient method [72]. However, credit is also due to Lanczos [92]. The history of the conjugate gradient method is discussed in [55,71]. Shewchuk's technical report [142] provides an introduction to the conjugate gradient method with illustrations that help to make the geometry of the method very clear. Filter factors for the CGLS method similar to those in Exercise 2 can be determined. These are derived in [65]. The LSQR method of Paige and Saunders [65,123,124] is an alternative way to apply the CG method to the normal equations. The resolution of LSQR solutions is discussed in [12,13]. Schemes have been developed for using CGLS with explicit regularization and dynamic adjustment of the regularization parameter $\alpha$ [85,86, 106]. This can poten-tially remove the computational burden of solving the problem for many values of $\alpha$ An alternative approach can be used to compute regularized solutions for several values of $\alpha$ at once [5O]. The performance of the CG algorithm degrades dramatically on poorly conditioned systems of equations. In such situations a technique called preconditioning can be used to improve the performance of CG. Essentially, preconditioning involves a change of variables $\bar { \boldsymbol { x } } = \mathbf { C } \boldsymbol { x }$ The matrix $\mathbf { C }$ is selected so that the resulting system of equations will be better conditioned than the original system of equations [38,53，164]. The conjugate gradient method can also be generalized to nonlinear minimization problems [58,142].

Inverse problems in image processing are a very active area of research. Some books on inverse problems in imaging include [14,115].

# Additional Regularization Techniques

# Synopsis

Alternatives or adjuncts to Tikhonov regularization are introduced. Bounds constraints allow the use of prior knowledge on the permissible range of parameter values. Sparsity regularization selects solutions with the minimum number of nonzero model parameters.A modification of the iteratively reweighted least squares algorithm presented in Chapter 2 for 1-norm parameter estimation is introduced to solve these problems.In compressive sensing, sparsity regularization is applied in association with a change of basis, where the basis is chosen so that the desired model will be sparse (i.e., have only a few nonzero coefficients in the model expansion). Total variation regularization uses a regularization term based on the 1-norm of the model gradient that allows for discontinuous jumps in the model to bias the solution towards piecewise-constant functions.

# 7.1. USING BOUNDS AS CONSTRAINTS

In many physical situations,bounds exist,or can be usefully estimated,on the maximum and/or minimum values of model parameters. For example, the model parameters may represent a physical quantity such as density that is inherently non-negative, establishing a strict lower bound for model parameters of 0. The problem of solving for a least squares solution that includes this constraint, referred to as non-negative least squares (NNLS), can be expressed as

$$
\begin{array} { r } { \operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } \qquad } \\ { \mathbf { m } \geq \mathbf { 0 } , } \end{array}
$$

where $\mathbf { m } \geq \mathbf { 0 }$ means that every element of the vector m must be non-negative. This problem can be solved by an algorithm called non-negative least squares (NNLS) that was originally developed by Lawson and Hanson [94]. MATLAB includes a command, lsqnonneg, that solves the NNLS problem.

We might also declare a strict upper bound, so that model parameters may not exceed some value, for example,a density $3 5 0 0 \mathrm { k g } / \mathrm { m } ^ { 3 }$ for crustal rocks in a particular region.

Given the lower and upper bound vectors l and $\mathbf { u }$ , we can pose the bounded variables least squares (BVLS) problem:

$$
\begin{array} { r } { \operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } } \\ { \mathbf { m } \geq \mathbf { l } } \\ { \mathbf { m } \leq \mathbf { u } . } \end{array}
$$

Given a BVLS algorithm for solving (7.2),we can also perform Tikhonov regulariza-tion with bounds by augmenting the system of equations (e.g.，(4.5) and then solving the augmented system under bounding constraints. Stark and Parker [15O] developed an algorithm for solving the BVLS problem, which we employ here as a MATLAB function bvls.m. A similar algorithm is given in the 1995 edition of Lawson and Hanson's book [94].

A related optimization problem involves minimizing or maximizing a linear function of the model for a set of $n$ coefficients $c _ { i }$ , subject to bounds constraints and a constraint on the misfit. This problem can be formulated as

$$
\begin{array} { r } { \operatorname* { m i n } \mathbf { c } ^ { T } \mathbf { m } } \\ { \| \mathbf { G m } - \mathbf { d } \| _ { 2 } \leq \delta } \\ { \mathbf { m } \geq 1 } \\ { \mathbf { m } \leq \mathbf { u } . } \end{array}
$$

# Example 7.1

Recall the source history reconstruction problem of Example 1.7, where data are taken in concentration units at spatial positions, $_ x$ ,at a particular time (assumed dimensionless here), $T$ .Figure 7.1 shows the true (smooth) source model used to generate the data, and Figure 7.2 shows these data as a function of distance, $_ x$ ，at time $T = 3 0 0$ ，with $N ( 0 , 0 . 0 0 1 ^ { 2 } )$ noise added.

Figure 7.3 shows the least squares solution, which has the extremely large amplitudes and oscillatory behavior characteristic of an unregularized solution to an ill-posed problem. This solution is, furthermore, physically unrealistic in having negative concentrations. Figure 7.4 shows the non-negative least squares solution, which, although certainly more realistic in having all of the concentration values nonnegative, consists of high-amplitude spikes that do not accurately reconstruct the (smooth) true source history. Suppose that the solubility limit of the contaminant in water is known to be 1.1 units, thus providing a natural upper bound on model parameters. Figure 7.5 shows the corresponding BVLS solution,which exhibits spiky features similar to those of Figure 7.4. Further regularization is indicated if we believe that the true model is smooth.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/4b1e6172ff84518030fb6c52d0a7d41f083edb02d9bdd87c19f1da3d7c113bd2.jpg)  
Figure 7.1 True source history.   
Figure 7.2 Concentration data as a function of position, $x ,$ taken at $T = 3 0 0$

Figure 7.6 shows the L-curve for a second-order Tikhonov regularization solution applied with bounds of $0 \leq \mathbf { m } \leq 1 . 1$ on the model vector elements. Figure 7.7 shows the regularized solution for $\alpha = 0 . 0 1$ . This solution correctly reveals the two major input concentration peaks. As is typical for cases of non-ideal model resolution,the solution peaks are somewhat lower and broader than those of the true model. This solution does not,however, resolve the smaller subsidiary peak near $t = 1 5 0$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/74388ad4f919d3df0f47f1d98e0b32f5c2b7f083034920afa933bb59d05bed47.jpg)  
Figure 7.3 Least squares source history solution with true history (Figure 7.1) shown as a dashed curve. Because the least squares solution has extremely large amplitudes,the true model appears as aflat line at this scale.   
Figure 7.4 NNLS source history solution with true history (Figure 7.1) shown as a dashed curve.

We can additionally use (7.3) to establish bounds on linear combinations of the model parameters. For example, we might want to establish bounds on the average concentration from $t = 1 2 5$ to $t = 1 5 0$ . These concentrations appear in positions 51 through 60 of the model vector m. We let $c _ { i }$ be zero in positions 1 through 5O and 61 through 100,and let $c _ { i }$ be 0.1 in positions 51 through 6O to form a 1O-time-sample averaging function.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/932d5d42c5f78d05208e947ccee6fedf5d731501e0d1c2004b4539e3fb2447fe.jpg)  
Figure7.5 BVLS source history solution $\mathbf { \left( 1 = 0 , u = 1 . 1 \right. }$ with true history(Figure7.1) shown as a dashed curve.   
Figure 7.6 L-curve for the second-order Tikhonov solution with BVLS $\mathbf { \Omega } ( \mathbf { l } = \mathbf { 0 }$ ， $\mathbf { u } = \mathbf { 1 . 1 }$ ) implementation, cornerat $\alpha = 0 . 0 1$ .

The value of $\mathbf { c } ^ { T } \mathbf { m }$ is the average of model parameters 51 through 60. The value of the solution to (7.3) will then be a lower bound on the average concentration from $t = 1 2 5$ to $t = 1 5 0$ . Similarly, by maximizing $\mathbf { c } ^ { T } \mathbf { m }$ or equivalently by minimizing $- \mathbf { c } ^ { T } \mathbf { m }$ we can obtain an upper bound on the average concentration from $t = 1 2 5$ to $t = 1 5 0$ . Solving the minimization problems for $\mathbf { c } ^ { T } \mathbf { m }$ and $- \mathbf { c } ^ { T } \mathbf { m }$ ，we obtain, respectively,a lower bound of O.36 and an upper bound of O.73 for the average concentration during this time period. The true concentration average over this interval (Figure 7.1) is 0.57.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/d34b9b91375431103177537eb9f05c28f0392baab33c8dd79e9a9e248c8bd0b5.jpg)  
Figure7.7 Second-order Tikhonov regularization source history solution determined from the L-curve of Figure 7.6,with true history (Figure 7.1) shown as a dashed curve.

# 7.2. SPARSITY REGULARIZATION

In some situations there are reasons to expect that many of the unknown model parameters will be zero.Rather than using Tikhonov regularization to minimize $\| \mathbf { m } \| _ { 2 }$ ，we may choose to minimize the number of nonzero entries in m to obtain a sparse model.

The notation $\| \mathbf { m } \| _ { 0 }$ is commonly used to denote the number of nonzero entries in $\mathbf { m }$ (Note that this O-norm definition is nonstandard because it is inconsistent with the definition of the $p$ -norm in (A.85) and does not satisfy the requirements for a vector norm in Section A.7.） We can formulate a corresponding regularized inverse problem as

$$
\begin{array} { c } { { \operatorname* { m i n } \ \| \mathbf { m } \| _ { 0 } } } \\ { { \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } \leq \delta . } } \end{array}
$$

Unfortunately, these kinds of optimization problems can be extremely diffcult to solve.

A surprisingly effective alternative to (7.4) is to instead find the least squares solution that minimizes $\| \mathbf { m } \| _ { 1 }$ . To see that this is a reasonable approach,consider the set of models with $\| \mathbf { m } \| _ { 2 } = 1$ . Among the models with $\| \mathbf { m } \| _ { 2 } = 1$ , it turns out that the models with precisely one nonzero entry of $+ 1$ or $- 1$ have the smallest 1-norms (Figure 7.8). Thus,regularizing a least squares problem to minimize its model 1-norm will tend to produce sparse solutions. This tendency for 1-norm regularized models to be sparse becomes even more prominent in higher dimensions. The heuristic approach of minimizing $\| \mathbf { m } \| _ { 1 }$ instead of $\| \mathbf { m } \| _ { 0 }$ works very well in practice,and recent work [21] has demonstrated reasonable conditions under which the solution to the 1-norm regularized problem is identical to or at least close to the solution of the O-norm regularized problem (7.4).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/af87b7d6cec6c3c76ce9cff3dc1c35a9618d4fb9e1c1e6d24f4d828a11f13476.jpg)  
Figure 7.8 Two-dimensional demonstration of the use of model 1-norm minimization (7.5) to obtain sparsity regularization.The square shaded area shows the region $\| \mathbf { m } \| _ { 1 } \leq c _ { 1 }$ ,while the circle shows the region with $\| \mathbf { m } \| _ { 2 } \leq c _ { 2 }$ .An arbitrary constraint equation in this 2-dimensional model space, $( \mathbf { G m } ) _ { i } -$ $d _ { i } = 0$ ,defines a line.The minimum 2-norm residual model satisfying the constraint $\mathbf { m } _ { 2 }$ ,will not generally be sparse. However,the minimum 1-norm model satisfying the constraint, $\mathbf { m } _ { 1 } = [ 0 c _ { 1 } ] ^ { T }$ , will tend to be sparse due to the presence of corners in the 1-norm contour.

The $L _ { 1 }$ regularized least squares problem can be written as

$$
\begin{array} { c } { { \operatorname* { m i n } \ \| \mathbf { m } \| _ { 1 } } } \\ { { \| \mathbf { G m } - \mathbf { d } \| _ { 2 } \leq \delta . } } \end{array}
$$

Using the standard approach of moving the constraint into the objective function, we can select a positive regularization parameter, $\alpha$ , so that this is equivalent to

$$
\operatorname* { m i n } \ \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { m } \| _ { 1 } .
$$

This is a convex optimization problem that can be solved efficiently by many different algorithms. We next present an iterative least squares solution method.

# 7.3. USING IRLS TO SOLVE $L _ { 1 }$ REGULARIZED PROBLEMS

To solve problems of the form of (7.6) we extend the IRLS algorithm introduced in Chapter 2 for $L _ { 1 }$ regression. Let

$$
f ( \mathbf { m } ) = \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { L m } \| _ { 1 }
$$

and let

$$
\mathbf { y } = \mathbf { L m } .
$$

At points where any element of $\mathbf { L m }$ is zero, $f ( \mathbf { m } )$ is not differentiable because of the nondifferentiability of the absolute values in the $L _ { 1 }$ norm. However, at other points we can easily compute the gradient of $\boldsymbol { \mathsf { \Sigma } }$

$$
\nabla f ( \mathbf { m } ) = 2 \mathbf { G } ^ { T } \mathbf { G } \mathbf { m } - 2 \mathbf { G } ^ { T } \mathbf { d } + \alpha \sum _ { i = 1 } ^ { m } \nabla | \gamma _ { i } | .
$$

For $\gamma _ { i }$ nonzero,

$$
\frac { \partial | \gamma _ { i } | } { \partial m _ { k } } = L _ { i , k } \mathrm { s g n } ( \gamma _ { i } ) .
$$

Writing $\operatorname { s g n } ( \gamma _ { i } )$ as $\gamma _ { i } / | \gamma _ { i } |$ , and using $\begin{array} { r } { \| \mathbf { L m } \| _ { 1 } = \sum _ { i = 1 } ^ { m } \| \gamma _ { i } \| } \end{array}$ , we obtain

$$
\frac { \partial \| \mathbf { L m } \| _ { 1 } } { \partial m _ { k } } = \sum _ { i = 1 } ^ { m } L _ { i , k } \frac { \gamma _ { i } } { | \gamma _ { i } | } .
$$

Let $\mathbf { w }$ be the diagonal matrix with elements

$$
W _ { i , i } = \frac { 1 } { | \gamma _ { i } | } .
$$

Then

$$
\nabla \mathbf { \Psi } ( \| \mathbf { L m } \| _ { 1 } ) = \mathbf { L } ^ { T } \mathbf { W } \mathbf { L m }
$$

and

$$
\boldsymbol { \nabla } f ( \mathbf { m } ) = 2 \mathbf { G } ^ { T } \mathbf { G } \mathbf { m } - 2 \mathbf { G } ^ { T } \mathbf { d } + \alpha \mathbf { L } ^ { T } \mathbf { W } \mathbf { L } \mathbf { m } .
$$

Setting $\nabla f ( \mathbf { m } ) = \mathbf { 0 }$ ,we obtain

$$
\left( 2 \mathbf { G } ^ { T } \mathbf { G } + \alpha \mathbf { L } ^ { T } \mathbf { W } \mathbf { L } \right) \mathbf { m } = 2 \mathbf { G } ^ { T } \mathbf { d } .
$$

Because W depends on $\mathbf { L m }$ ,this is a nonlinear system of equations. Furthermore, $\mathbf { w }$ is not defined at any point where $\mathbf { L m }$ has a zero element.

To accommodate the nondifferentiability of the 1-norm at the origin，as in Chapter 2,we set a tolerance $\epsilon$ ,and let

$$
W _ { i , i } = \left\{ \begin{array} { l l } { 1 / | \gamma _ { i } | } & { | \gamma _ { i } | \geq \epsilon } \\ { 1 / \epsilon } & { | \gamma _ { i } | < \epsilon . } \end{array} \right.
$$

In the IRLS procedure, we solve (7.15), update $\mathbf { w }$ according to (7.16),and iterate until the solution has converged.

The system of equations (7.15) can be seen as the normal equations for the least squares problem,

$$
\begin{array} { r } { \operatorname* { m i n } \left\| \left[ \begin{array} { c } { \mathbf { G } } \\ { \sqrt { \frac { \alpha } { 2 } } \sqrt { \mathbf { W } } \mathbf { L } } \end{array} \right] \mathbf { m } - \left[ \begin{array} { c } { \mathbf { d } } \\ { \mathbf { 0 } } \end{array} \right] \right\| _ { 2 } . } \end{array}
$$

When $\mathbf { G }$ is large and sparse it can be extremely advantageous to apply LSQR to solve the least squares problem (7.17) rather than solving the system of equations (7.15).

# Example 7.2

Consider a deconvolution example in which a controlled surface source sends seismic waves down into the earth. Seismic reflections will occur from abrupt material discontinuities at various depths,and a seismogram of the reflected signals (which will generally include multiple reflections) is recorded at the surface. Here, $g ( t )$ is the known source signal, $d ( t )$ is the recorded seismogram, and $m ( t )$ is the unknown reflection response of the earth. We'd like to recover the times of these reflections to study the respon-sible earth structure. This is a linear forward problem characterized by a convolution (e.g., (1.11))

$$
d ( t ) = \int _ { - \infty } ^ { \infty } g ( t - \xi ) \ m ( \xi ) \ d \xi .
$$

In this highly simplified reflection seismology example,we will assume a onedimensional structure with depth and consider upward- and downward-traveling plane compressional seismic waves detected by a vertically oriented seismometer. In this case, the presence of horizontally oriented seismic structural discontinuities in an otherwise smooth medium will ideally be manifested in $m ( t )$ as a sequence of delta functions.As in Chapter 1, we will discretize $m ( t )$ as a model vector $\mathbf { m }$ . We seek models where m consists of an optimal sequence of spikes.

The source signal is a short pulse with a characteristic time of around $0 . 4 \ : s$

$$
g ( t ) = e ^ { - 5 t } \sin ( 1 0 t ) .
$$

We'll add independent normally distributed random noise to the corresponding recorded data (7.18) and attempt to recover $m ( t )$ in regularized inversions.All time series were sampled uniformly at 1OO samples/s to create model and data vectors of 1000 points spanning 1O-s time intervals. The true reflectivity model (Figure 7.9) is the response of a single subsurface reflector with a coefficient of $r = 0 . 4$ ,located at a depth corresponding to a two-way seismic travel time from the surface of $\tau = 1 . 5 s$ This source signal $g ( t )$ begins at $0 . 5 s$ ， and the primary reflection and surface-reflector multiples appear in Figure 7.9 as alternating-sign spikes at intervals of $\tau$ with amplitudes that decrease by a factor of $r$ upon each reflection. Figure 7.10 shows the corresponding data from (7.18) with $N ( 0 , ( 0 . 0 0 2 ^ { 2 } ) )$ noise added. The noise and smoothing from the convolution largely obscure the signal corresponding to the later impulses of Figure 7.9.

Figure 7.11 shows the L-curve for this problem with zeroth-order regularization, using the frequency-domain techniques described in Chapter 8,and Figure 7.12 shows a corresponding solution. The impulses are broadened relative to the true model due to the associated regularization bias,and there are noise-generated secondary peak. Figures 7.13, 7.14,and 7.15, however, show that using (7.5) produces excellent recovery of $m ( t )$ . Note that the spikes are correctly placed in time and that allare resolved save the tiny pulse at $7 . 5 \ : \mathrm { s }$ ,which has an amplitude of only $r ^ { 5 } \approx 0 . 0 1$ ,or just $1 \%$ of the amplitude of the source spike. The amplitude of the spikes is reduced and they are slightly broader than they should be,but the model is vastly better than that obtained with Tikhonov regularization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/1310c4404bddb190f759549757395b71c3c9a600a03dc2ceddd2cfc6b8c51db7.jpg)  
Figure 7.13 L-curve for the 1-norm regularized solution with corner at $\alpha = 2 . 4 \times 1 0 ^ { - 4 }$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/149efb00f7b3be74675e4ba29229fc1610a8ff36b85855e6277c5180485f2e1c.jpg)  
Figure 7.14 1-norm regularized solutions corresponding to the range of regularization parameters used to construct Figure 7.13.Model corresponding to the L-curve corner is shown in bold.

In many situations, there is no reason to bias models to be sparse. If the true model is not sparse, then sparsity regularization will of course produce poor model recovery. However, it is possible in some cases to implement a change of variables so that the coefficients of the model with respect to the new basis wil be sparse, or can at least be well approximated by a sparse model.

Recall from Appendix A that if a set of vectors $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , \ldots . . . , \mathbf { w } _ { n }$ form a basis for $R ^ { n }$ ， then any vector $\mathbf { m }$ in $R ^ { n }$ can be written as a linear combination of the basis vectors with $n$ coefficients, $x _ { i }$ ：

$$
\begin{array} { r } { { \bf m } = x _ { 1 } { \bf w } _ { 1 } + x _ { 2 } { \bf w } _ { 2 } + \cdot \cdot \cdot + x _ { n } { \bf w } _ { n } . } \end{array}
$$

In vector-matrix form, this can be writen as

$$
\mathbf { m } = \mathbf { W } \mathbf { x }
$$

where the basis vectors $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , \ldots . . . , \mathbf { w } _ { n }$ are the columns of $\mathbf { w }$ . We can also perform the change of variables in the reverse direction as

$$
\mathbf { x } = \mathbf { W } ^ { - 1 } \mathbf { m } .
$$

In practice, linear transformation algorithms,such as the fast Fourier transform (FFT; Chapter 8) or discrete cosine transform (DCT),are often used in place of the matrixvector multiplications of (7.21） and (7.22) to effect the corresponding forward and inverse operations.

# Example 7.3

Figure 7.16 shows the 40,000-pixel image from Example 6.3. If we were to zero out any significant fraction of these pixels,the efect on the image would be quite obvious. However, if instead we encode the image in terms of the discrete cosine transform (DCT) of the pixel values,a sparser representation of the image is possible that closely approximates the original. Calculating the discrete cosine transform of the two-dimensional image using MATLAB's dct2 command produces a set of 40,000 coefficients. Of these 40,O0O coefficients, the 16,O0O coefficients ( $40 \%$ of the original coefficients) that were smallest in absolute value were set to zero.

After inverting the DCT, we produced the image shown in Figure 7.17. This second image appears to be very similar to the original image, yet $40 \%$ fewer coefficients were used to represent the image in terms of the DCT basis. This is because the coefficients associated with the 16,OOO unused basis vectors in the original image were small.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/33e4d3d9dd9ce5e12fca16718c8193c8495902db4182ad9f623fb7a967571461.jpg)  
Figure 7.16 Image before discrete cosine transform threshholding.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/6ee48c64c8caa51da21cf26064ff498763a4f7d5a48cb7c35379108689d80b97.jpg)  
Figure 7.17 Image after removing smallest $4 0 \%$ of DCT coefficients.

The discrete cosine transform is the basis for the widely used JPEG standard for image compression. Wavelet bases are also widely used in image processing,and threshholding the wavelet transform produces similar results in compressng images. The newer JPEG 2OOO standard for image compression uses wavelets rather than the discrete cosine transform.

In compressive sensing, we apply sparsity regularization using a basis chosen so that the model can be represented by a linear combination of the basis vectors with a sparse set of coefficients. The regularized problem can be written using (7.21) and (7.6) as

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { W } \mathbf { x } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { x } \| _ { 1 } ,
$$

where $\mathbf { G }$ is called the measurement matrix.

The recovery of a sparse solution using (7.23) depends on the details and appropriateness of the particular $\mathbf { G }$ and $\mathbf { w }$ used in (7.23). The analysis and implementation of compressive schemes become relatively simple if the measurement matrix is random [27].

# Example 7.4

Consider the recovery of a signal, $\mathbf { m }$ ，shown in Figure 7.18. This 10-s long time series of $n = 1 0 0 1$ time points, $t _ { i }$ ,is sampled at 1OO samples/s and consists of two sine waves at $f _ { 1 } = 2 5$ and $f _ { 2 } = 3 5 \mathrm { H z }$ ：

$$
m _ { i } = h _ { i } \cdot \left( 5 \cos ( 2 \pi f _ { 1 } t _ { i } ) + 2 \cos ( 2 \pi f _ { 2 } t _ { i } ) \right) 1 \leq i \leq n ,
$$

where the signal envelope has also been smoothed with term-by-term multiplication by a Hann taper function,

$$
h _ { i } = \frac { 1 } { 2 } \ \left( 1 - \cos ( 2 \pi ( i - 1 ) / n ) \right) \ 1 \leq i \leq n .
$$

In the standard basis, the signal (7.24),shown in Figure 7.18, is obviously not sparse. However, because it is constructed from two cosine components, this model has a very sparse representation in the DCT basis.

We use a random measurement matrix $\mathbf { G }$ that is $m = 1 0 0$ by $n = 1 0 0 1$ ，with entries chosen independently from $N ( 0 , 1 )$ to generate a synthetic set of 1OO data measurements, $\mathbf { d } = \mathbf { G } \mathbf { m }$ ，and then add independent $N ( 0 , 2 5 )$ noise. The matrix of basis vectors, $\mathbf { w }$ ，is constructed by applying the discrete cosine transform to standard basis vectors for the model space $R ^ { n }$ .

Figures 7.19 and 7.2O show solutions obtained by solving $\mathbf { G m } = \mathbf { d }$ using secondorder Tikhonov regularization.The highlighted solution $( \alpha = 1 0 0 )$ fits the data with a residual norm that approximately satisfies the discrepancy principle, so that $\| \mathbf G \mathbf m - \mathbf d \|$ $\approx 5 \cdot { \sqrt { m } } = 5 0 .$ However, this solution,and others across a wide range of $\alpha$ values, bear essentially no resemblance to the true signal shown in Figure 7.18.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/2b1b88c17e560b9151b71d74fdd300b38c7d50f3a67c5ce2fbb73355d21d3295.jpg)  
Figure 7.18 A 1001-point signal consisting of 25-and $3 5 - 1 1 z$ cosines (7.24), multiplied bya Hann taper.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/7220a3055d3e57a89de787f33b37f79d07b34664487489f83f94a106471da223.jpg)  
Figure 7.19 Signal recovery using second-order Tikhonov regularization. Solution amplitudes are normalized to improve legibility.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/2cfc7ce42ed5d020f7abe6d58970e8520fd29f4378a3dc1e00bb60db0063e8be.jpg)  
Figure7.20 Arepresentative solution using second-order Tikhonov regularization that approximately satisfies the discrepancy principle from Figure 7.19 $( \alpha = 1 0 )$ .

An L-curve obtained by solving (7.23） for $n$ DCT coefficients $\mathbf { x }$ ，and subsequently constructing models $\mathbf { w _ { x } }$ for various $\alpha$ values， shows a very abrupt corner near $\alpha = 1 0 ^ { - 1 1 }$ . For very low levels of regularization beyond this corner, solutions rapidly transition from excellent model recovery to essentially random noise. For $\alpha$ values greater than a few hundred,on the other hand, solutions rapidly approach the zero model. For a wide range of $\alpha$ values between these extreme values, the recovered signal $\mathbf { w _ { x } }$ is stable and is quite close to the true signal (Figures 7.21 and 7.22).

It may seem paradoxical that we can recover a 1OO1-point signal so well from only 10O random linear combination measurements, when the Nyquist sampling theo-rem (8.4O) suggests that at least $1 0 \mathrm { s } \times 3 5 \mathrm { H z } \times 2 = 7 0 0$ equally spaced samples should be required to accurately represent it. This is possible in the current example because the measured signal is sparse with respect to the DCT basis,and just a few cosine basis functions are therefore necessary to represent it well. The corresponding sparse set of coefficients is easily recovered when sparsity regularization is employed.

# 7.4.TOTAL VARIATION

Total variation (TV) regularization is appropriate for problems where we expect there to be discontinuous jumps in the model. In the one-dimensional case, the TV regularization function is

$$
\begin{array} { c } { { \displaystyle \mathrm { T V } ( } { \bf m } ) = \sum _ { i = 1 } ^ { n - 1 } | m _ { i + 1 } - m _ { i } | } \\ { { \displaystyle = \| { \bf L m } \| _ { 1 } } , } \end{array}
$$

where, for one-dimensional models, $\mathbf { L } = \mathbf { L } _ { 1 }$ (4.27). In higher-dimensional problems, $\mathbf { L }$ is a discretization of the gradient operator.

In first- and second-order Tikhonov regularization, discontinuities in the model are smoothed out and do not show up well in the inverse solution.This is because smooth changes are penalized less by the regularization term than sharp ones. The particular feature of (7.27) is that the regularization term imposes a constraint to keep the number of discontinuous transitions to a minimum (i.e., keeping $\mathbf { L m }$ sparse). We can insert the TV regularization term (7.27) in place of $\| \mathbf { L m } \| _ { 2 } ^ { 2 }$ in the Tikhonov regularization optimization problem to obtain

$$
\operatorname* { m i n } \ \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha \| \mathbf { L } \mathbf { m } \| _ { 1 } ,
$$

which is a convex optimization problem in the form of(7.6) that imposes a higher-order sparsity constraint.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/6a01be28d916c84da9a05c7a193e281278f0ee42c4824d06e160babe0a29cb89.jpg)  
Figure 7.21 Signal recovery using compressive sensing with 100 signal measurements.Solution amplitudes are normalized to improve legibility.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/f842765fb5f303b27d6e3adda3fb25812c0620f9add26f8742bfa151af09b1f8.jpg)  
Figure 7.22 A representative solution obtained from Figure 7.21 using compressive sensing with $\alpha = 1 0 0$ thatapproximately satisfies the discrepancy principle.

This approach has seen wide use in the problem of “denoising” a model [122]. Denoising is a linear inverse problem in which $\mathbf { G } = \mathbf { I }$ . In denoising,the general goal is to remove features considered to be spurious from a signal, while still retaining other key features, such as long-term trends and perhaps sharp discontinuities.

# Example 7.5

Figure 7.23 shows a signal that is smooth with the exception of two discontinuous jumps at 2 and $7 s .$ Figure 7.24 shows the signal after $N ( 0 , 4 )$ independent noise has been added. Our goal is to remove this noise from the signal while optimally recovering the discontinuities.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/b296fa6116efce638719ef34e578a98030fbddf27efe2b03daa1e5c783a21f51.jpg)  
Figure 7.23 An otherwise smooth signal with two sharp discontinuities.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/59c90c6adb615f5f9288e7b9b3adcebb658f0e29cadf160f252602312a39d7dd.jpg)  
Figure 7.24 The signal with $N ( 0 , 4 )$ noise added.

We first attempt to denoise the signal using second-order Tikhonov regularization with L given by (4.28). The L-curve is shown in Figure 7.25,and the resulting solution is shown in Figure 7.26. If the location of the large discontinuities is a feature that we wish to recover, this solution obviously does not do a good job because the regularization scheme biases the model based on smoothness.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/3944424a11a61d7841da02b65520b251a3faabc49f1d4b9ac419a32c329824be.jpg)  
Figure 7.25 L-curve with second-order Tikhonov regularization with corner at $\alpha = 1 0 0 0$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/4cfaa4afdec204beea8d0831571c0f30fa1844a031a0a7451647241b155ed298.jpg)  
Figure 7.26 Second-order Tikhonov solution $( \alpha = 1 0 0 0 )$ ）with the true model plotted as a dashed curve.

We next apply TV regularization to solve the problem. Figure 7.27 shows the L-curve trade-off between $\| \mathbf { m } - \mathbf { d } \| _ { 2 }$ and $\| \mathbf { L m } \| _ { 1 }$ , and the presence of a corner near $\alpha \approx 1 8$ . Figure 7.28 shows the corresponding models for various levels of regular-ization, with the optimal one selected from the L-curve shown in Figure 7.29. This piecewise-constant recovery of the original signal reveals the large discontinuities at $2 \thinspace s$ and $7 s$ quite well.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/fbf26c7c06e076974fe2c54e189cbed858db71ccea266d5a2210a2c29ad4b5a7.jpg)  
Figure 7.27 L-curve for TV regularization with corner at $\alpha = 1 8$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/210d70ce0c95e9b76e5056b4b8cb634d71fde98586cd1918313f3c8571fd8084.jpg)  
Figure 7.28 Signal recovered with TV regularization with model corresponding to the L-curve corner shown in bold.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0003_pages_0141-0210/auto/images/51464e4e49057b18cfddda687fb0715465de6f484f1cdad1a7ebd90938087af9.jpg)  
Figure 7.29 Signal recovered with TV regularization for $\alpha = 1 8$ from Figure 7.28 with the true model plotted as a dashed curve.

# 7.5. EXERCISES

1. Using the method of Lagrange multipliers, develop a formula that can be used to solve

$$
\begin{array} { l } { \operatorname* { m i n } \mathbf { c } ^ { T } \mathbf { m } } \\ { \| \mathbf { G } \mathbf { m } - \mathbf { d } \| _ { 2 } \leq \delta . } \end{array}
$$

2.Noisy seismic travel time data (units of s) from equally spaced (every $2 0 \mathrm { m } )$ seismometers deployed in a $1 0 0 0 \mathrm { - m }$ deep vertical seismic profile experiment (the same geometry as in Example 4.4) are to be inverted to reveal the slowness of the earth as a function of depth. Invert the data in vsp.mat using TV regularization with an L-curve analysis and assess the presence of any likely discontinuities. Compare this with the least squares solution and with a direct finite-difference solution suggested by (1.22).

3.In many cases, it is valuable to implement multiple regularization constraints,such as smoothness combined with bounds. Consider the gravity anomaly data in the vector $\mathbf { d n }$ (units of $\mathrm { m } / \mathrm { s } ^ { 2 }$ ） found in the file gdata.mat. The data are taken at the surface above a $1 0 0 0 \mathrm { m }$ section of a partially debris-blocked buried pipe located with its center at a depth of $2 5 \mathrm { m }$ .Use the methodology of Example 1.4 to invert these data for subsurface density perturbations,assuming that the pipe has a cross-sectional area of $1 ~ \mathrm { m } ^ { 2 }$ . Anomalous density along the pipe relative to background density is parameterized as point masses located at 1OO equally spaced points along the section, as specified by the vector rhox. The noisy surface gravity anomaly observations contained in the vector $\mathbf { d n }$ are made at 5OO points along the same $1 0 0 0 \mathrm { m }$ span as the buried pipe section of interest at points specified in the vector $\mathbf { x }$ Invert the data for density perturbations along the buried pipe by assuming that all mass in each segment can be concentrated at the points specified by rhox.

a. Invert for density perturbations along the pipe transect in $\mathrm { k g } / \mathrm { m } ^ { 3 }$ using least squares.   
b. Invert for density perturbations along the pipe transect in $\mathrm { k g } / \mathrm { m } ^ { 3 }$ using secondorder Tikhonov regularization and an L-curve analysis.   
c. Solve the problem using second-order Tikhonov regularization combined with BVLS and an L-curve analysis. Employ the knowledge that density variations for $x < 9 1$ and $x > 8 9 9 \mathrm { ~ m ~ }$ are negligible, and that the density variations overall are bounded by $- 1 5 0 \mathrm { k g / m ^ { 3 } } \le \delta \rho \mathrm { ( x ) } \le 1 5 0 \mathrm { k g / m ^ { 3 } }$   
d. Compare and discuss your three solutions. Where are the prominent maxima and minima located?

4.Returning to the problem in Exercise 3.1,solve for the density profile using total variation regularization.How does your solution compare to the solutions obtained in Exercise 3.1 and Exercise 4.4?

# 7.6.NOTES AND FURTHER READING

Methods for bounded variables least squares problems and minimizing a linear function subject to a bound on the misfit are given in [15O]. Some applications of these techniques can be found in [73,125,128,148,149]. There is a long history of sparsity regularization in geophysical inverse problems. Claerbout and Muir were early advocates of this approach [31]; however, there was litle theoretical justification for this prior to the work of Candes, Romberg,and Tao,which brought about a resurgence of interest in this methodology [24,25,26]. In recent years there has been an explosion of interest in compressve (or compressed) sensing, with applications in many areas of signal and image processing and inverse problems. There are numerous surveys and tutorials on compressive sensing, including [21,27,1O4]. Methods for total variation regularization are discussed in [122,169].

# Fourier Techniques

# Synopsis

The formulation of a general linear forward problem as a convolution is derived. The Fourier transform, Fourier basis functions,and the convolution theorem are introduced for continuous- and discrete-time systems. The inverse problem of deconvolution is explored in the context of the convolution theorem. Water level and Tikhonov regularization in the frequency domain are employed to solve discrete deconvolution problems.

# 8.1.LINEAR SYSTEMS IN THE TIME AND FREQUENCY DOMAINS

A remarkable feature of linear time-invariant systems is that the forward problem can generally be described by a convolution (1.11),

$$
d ( t ) = \int _ { - \infty } ^ { \infty } m ( \tau ) g ( t - \tau ) \ d \tau .
$$

Inverse problems involving such systems can be solved by deconvolution. Here, the independent variable $t$ is time,and the data $d$ ，model $m$ ，and system kernel $g$ are all time functions. However, the results here are equally applicable to spatial problems (e.g., Example 8.1) and to higher dimensions. We will first overview the essentials of Fourier theory in the context of performing convolutions and deconvolutions.

Consider a linear time-invariant forward operator, $G$ ,that maps an unknown model function, $m ( t )$ ,into an observable data function, $d ( t )$ ，

$$
d ( t ) = G [ m ( t ) ] .
$$

Because it is linear and time-invariant, (8.2) obeys the principles of superposition (1.5) and scaling (1.6). It is possible to show that any such system can be cast in the form of (8.1), by utilizing the sifting property of the impulse or delta function, $\delta ( t )$ . The delta function can be conceptualized as the limiting case of a pulse as its width goes to zero, its height goes to infinity,and its area stays constant and equal to one, for example, as the limiting case ofa unit area Gaussian pulse centered on the origin,

$$
\delta ( t ) = \operatorname* { l i m } _ { \sigma \to 0 } \frac { 1 } { \sigma \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } t ^ { 2 } / \sigma _ { . } ^ { 2 } } \nonumber
$$

The sifting property of the delta function extracts the value of a function at a particular point from within a definite integral

$$
\int _ { a } ^ { b } f ( t ) \delta ( t - t _ { 0 } ) \ d t = { \left\{ \begin{array} { l l } { f ( t _ { 0 } ) } & { a \leq t _ { 0 } \leq b } \\ { 0 } & { { \mathrm { e l s e w h e r e } } , } \end{array} \right. }
$$

for any $f ( t )$ that is continuous at finite $t = t _ { 0 }$ . The impulse response, or Green's function, $g ( t )$ , for a system where the model and data are related by an operator $G$ as in (8.2), is defined as the system output (data) for a delta function input (model),

$$
g ( t ) = G [ \delta ( t ) ] .
$$

The concept of the impulse response can be used to demonstrate our initial assertion in this chapter that linear time-invariant forward problems can generally be expressed as convolutions.

Theorem 8.1 We begin with a restatement of (8.2);

$$
d ( t ) = G [ m ( t ) ] .
$$

$m ( t )$ can be writen as a summation of impulse functions by invoking (8.4),

$$
m ( t ) = \int _ { - \infty } ^ { \infty } m ( \tau ) \delta ( t - \tau ) \ d \tau ,
$$

and we can thus write

$$
d ( t ) = G \left[ \int _ { - \infty } ^ { \infty } m ( \tau ) \delta ( t - \tau ) \ d \tau \right] .
$$

Applying the definition ofthe integral as a limit of a sum of $\Delta t$ width rectangular areas as $\Delta t$ goes to zero, we have

$$
d ( t ) = G \Biggl [ \underbrace { l i m } _ { \Delta \tau  0 } \sum _ { n = - \infty } ^ { \infty } m ( \tau _ { n } ) \delta ( t - \tau _ { n } ) \Delta \tau \Biggr ] .
$$

Because $G$ is a linear and time-invariant operator, superposition allws us to move the operator inside of the summation in (8.9). Furthermore, using the scaling relation, we can factor out the

coeffcients $m ( \tau _ { n } )$ from inside of the operator to obtain

$$
d ( t ) = l i m \sum _ { \Delta \tau  0 } ^ { \infty } \sum _ { n = - \infty } ^ { \infty } m ( \tau _ { n } ) G [ \delta ( t - \tau _ { n } ) ] \Delta \tau .
$$

In the limit as $\Delta t \to 0$ and substituting (8.5)， (8.10) thus defines the integral

$$
d ( t ) = \int _ { - \infty } ^ { \infty } m ( \tau ) g ( t - \tau ) \ d \tau ,
$$

which is identical to $( 8 . 1 )$ , the convolution of $m ( t )$ and $g ( t )$

Note that it is common to denote the convolution of two functions $h _ { 1 } ( t )$ and $h _ { 2 } ( t )$ simply as $h _ { 1 } ( t ) * h _ { 2 } ( t ) = h _ { 2 } ( t ) * h _ { 1 } ( t )$ . The indicated reciprocity is easily demonstrated from (8.11) with a change of variables.

Convolution can thus be used to describe the mapping of models to data for any linear time-invariant system. Important examples include the mapping between a physical process and a set of observables that occurs in a forward problem,or the output of a linear instrumentation system. For example,a perfect instrument that recorded some model $m ( t )$ with perfect fidelity, but imposed a time delay $t _ { \mathrm { 0 } }$ , would have a time-delayed delta function impulse response:

$$
\begin{array} { l } { d ( t ) = m ( t ) * \delta ( t - t _ { 0 } ) } \\ { \displaystyle \qquad \propto \qquad } \\ { \displaystyle \quad = \int _ { - \infty } m ( \tau ) \delta ( t - t _ { 0 } - \tau ) \ d \tau } \\ { \displaystyle \qquad \quad - \infty \qquad } \\ { \displaystyle \qquad = m ( t - t _ { 0 } ) . } \end{array}
$$

We define the Fourier transform of a function, $h ( t )$ ,as

$$
\begin{array} { l } { \displaystyle \mathcal { H } ( f ) = \mathcal { F } [ h ( t ) ] } \\ { \displaystyle \qquad \infty } \\ { \displaystyle \qquad = \int _ { - \infty } ^ { \infty } h ( t ) e ^ { - \imath 2 \pi f t } \ d t , } \\ { \displaystyle \qquad - \infty } \end{array}
$$

and the corresponding inverse Fourier transform as

$$
\begin{array} { c } { h ( t ) = \mathcal { F } ^ { - 1 } [ \mathcal { H } ( f ) ] } \\ { \displaystyle } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } \mathcal { H } ( f ) e ^ { \imath 2 \pi f t } d f , } \end{array}
$$

where $f$ has units of reciprocal time (frequency) and $\imath$ is the square root of $- 1$

The impulse response of a linear system, $g ( t ) = G [ \delta ( t ) ]$ ， is commonly called the time domain response of the system when the independent variable is time. Note, however, that the impulse response concept and Fourier theory are trivially generalizable to functions of space or other variables. The Fourier transform or spectrum of the impulse response, $\mathcal { F } ( g ( t ) )$ , is variously referred to as the frequency response, or transfer function of the system.

The Fourier transform (8.16) provides a formula for evaluating the spectrum. The inverse Fourier transform (8.18) states that the time domain function $g ( t )$ can be exactly reconstructed via a weighted integration of functions of the form $e ^ { \imath 2 \pi f t }$ ，where the weighting is provided by the spectrum $\mathcal G ( f )$ . The essence of Fourier analysis expressed in the transforms (8.16) and (8.18) is that general functions can be expressed and ana-lyzed as a continuous weighted superposition of Fourier basis functions of the form $e ^ { \imath 2 \pi f t }$ . Note that this representation difers from the finite basis function sets considered in Chapter 5 in that the sets of Fourier basis functions in (8.16) and (8.18) are infinite.

Because the Fourier basis functions, $e ^ { \imath 2 \pi f t } = \cos ( 2 \pi f t ) + \imath \sin ( 2 \pi f t )$ , are complex, a general real-valued function $h ( t )$ will have a corresponding spectrum, $\mathcal { H } ( f )$ ， that can be complex valued. $| \mathcal { H } ( f ) |$ is called the spectral amplitude. It is commonly very convenient to express spectra in polar form,

$$
\mathcal { H } ( \boldsymbol { f } ) = | \mathcal { H } ( \boldsymbol { f } ) | e ^ { \imath \theta ( \boldsymbol { f } ) } ,
$$

where the angle that $\mathcal { H } ( f )$ makes in the complex plane,

$$
\theta ( f ) = \tan ^ { - 1 } \left( \frac { \operatorname* { i m a g } ( \mathcal { G } ( f ) ) } { \operatorname { r e a l } ( \mathcal { G } ( f ) ) } \right) ,
$$

is called the spectral phase.

A useful feature of the Fourier transform is that it is length preserving for the 2-norm measure, in the sense that the 2-norm of a function and its Fourier transform are identical. Consider a time domain norm of the form of (5.3) for a general complex function $h ( t )$

$$
\| h ( t ) \| _ { 2 } ^ { 2 } = \intop _ { - \infty } ^ { \infty } h ( t ) h ^ { \ast } ( t ) \ d t .
$$

Expressing $h ( t )$ using the inverse Fourier transform (8.18) and applying complex con-jugation (denoted by an asterisk) gives

$$
\| h ( t ) \| _ { 2 } ^ { 2 } = \int _ { - \infty } ^ { \infty } h ( t ) \left( \int _ { - \infty } ^ { \infty } { \mathcal { H } } ^ { * } ( f ) e ^ { - \imath 2 \pi f t } d f \right) d t .
$$

Interchanging the order of integration and utilizing (8.16), we have

$$
\begin{array} { l } { \displaystyle \| h ( t ) \| _ { 2 } ^ { 2 } = \int _ { - \infty } ^ { \infty } \mathcal { H } ^ { * } ( f ) \left( \int _ { - \infty } ^ { \infty } h ( t ) e ^ { - \imath 2 \pi f _ { l } } \ d t \right) d f } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } \mathcal { H } ^ { * } ( f ) \mathcal { H } ( f ) \ d f } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } \mathcal { H } ^ { * } ( f ) \mathcal { H } ( f ) \ d f } \\ { \displaystyle = \| \mathcal { H } ( f ) \| _ { 2 } ^ { 2 } , } \end{array}
$$

whichis the 2-norm ofthe Fourier transform of $h ( t )$ . Equation (8.23) is most commonly referred to as Parseval's theorem.

We have shown in (8.11) that the data produced by a linear time-invariant system for a model, $m ( t )$ , is the convolution of $m ( t )$ with the system impulse response. Evaluating the Fourier transform of this convolution produces an especially important result.

# Theorem 8.2

$$
\mathcal { F } [ m ( t ) * g ( t ) ] = \int _ { - \infty } ^ { \infty } \left( \intop _ { - \infty } ^ { \infty } m ( \tau ) g ( t - \tau ) \ d \tau \right) e ^ { - \imath 2 \pi f t } \ d t .
$$

Reversing the order of integration gives

$$
\mathcal { F } [ m ( t ) * g ( t ) ] = \int _ { - \infty } ^ { \infty } m ( \tau ) \left( \intop _ { - \infty } ^ { \infty } g ( t - \tau ) e ^ { - \imath 2 \pi f t } \ d t \right) d \tau .
$$

Introducing a change of variables, $\xi = t - \tau$ , we obtain

$$
\begin{array} { l } { { \displaystyle { \mathcal F } [ m ( t ) * g ( t ) ] = \int _ { - \infty } ^ { \infty } m ( \tau ) \left( \begin{array} { l } { { \displaystyle \sum _ { - \infty } ^ { \infty } g ( \xi ) e ^ { - \imath 2 \pi f ( \xi + \tau ) } \ d \xi } } \\ { { \displaystyle - \infty } } \end{array} \right) d \tau } } \\ { { \displaystyle \qquad = \left( \begin{array} { l } { { \displaystyle \sum _ { - \infty } ^ { \infty } m ( \tau ) e ^ { - \imath 2 \pi f \tau } \ d \tau } } \\ { { \displaystyle - \infty } } \end{array} \right) \left( \begin{array} { l } { { \displaystyle \sum _ { - \infty } ^ { \infty } g ( \xi ) e ^ { - \imath 2 \pi f \xi } \ d \xi } } \\ { { \displaystyle - \infty } } \end{array} \right) } } \\ { { \displaystyle \qquad = { \mathcal M } ( f ) { \mathcal G } ( f ) } . } \end{array}
$$

Equation (8.26),which applies to any pair of functions, is called the convolution theorem. The theorem states that convolution of two functions in the time domain corresponds to the multiplication of their Fourier transforms in the frequency domain. When the two functions are a model, $m ( t )$ , and an impulse response, $g ( t )$ , in a forward problem, (8.26) indicates that the corresponding data spectrum is simply the product of the model and impulse response spectra.

To examine the implications of the convolution theorem more explicitly, consider the data produced by a linear time-invariant system,characterized by the spectrum of the impulse response, $\mathcal G ( f )$ , for a model, $m _ { 0 } ( t )$ ,that is a Fourier basis function of frequency $f _ { 0 }$ ，

$$
m _ { 0 } ( t ) = e ^ { \imath 2 \pi f _ { 0 } t } .
$$

The spectrum of (8.27) is a delta function located at $f = f _ { 0 } , \delta ( f - f _ { 0 } )$ .This can be seen by constructing an inverse Fourier transform (8.18) that invokes the sifting property of the delta function

$$
e ^ { \imath 2 \pi f _ { 0 } } = \int _ { - \infty } ^ { \infty } \delta ( f - f _ { 0 } ) e ^ { \imath 2 \pi f _ { t } } d f .
$$

The spectrum of the corresponding data is thus, by (8.26),a delta function at $f = f _ { \mathrm { 0 } }$ ， scaled by the spectrum of $G ( t )$ ：

$$
\mathcal { F } \left[ G \left[ e ^ { \iota 2 \pi f _ { 0 } t } \right] \right] = \mathcal { F } \left[ \mathcal { G } ( f ) e ^ { \iota 2 \pi f _ { 0 } t } \right] = \delta ( f - f _ { 0 } ) \mathcal { G } ( f _ { 0 } ) .
$$

The corresponding time domain response is, by (8.18),

$$
\begin{array} { r l r } {  { \int _ { - \infty } ^ { \infty } \mathcal { G } ( f _ { 0 } ) \delta ( f - f _ { 0 } ) e ^ { \imath 2 \pi f t } \ d f = \mathcal { G } ( f _ { 0 } ) e ^ { \imath 2 \pi f _ { 0 } t } } } \\ & { } & { = \vert \mathcal { G } ( f _ { 0 } ) \vert e ^ { \imath \theta ( f _ { 0 } ) } e ^ { \imath 2 \pi f _ { 0 } t } } \\ & { } & { = \vert \mathcal { G } ( f _ { 0 } ) \vert e ^ { \imath \theta ( f _ { 0 } ) } m _ { 0 } ( t ) . } \end{array}
$$

Linear time-invariant systems thus transform the Fourier basis functions (8.27) to iden-tical functions,altering only their amplitude and phase by frequency-dependent factors $| \mathcal { G } ( f _ { 0 } ) | e ^ { \imath \theta ( f _ { 0 } ) }$ . Because the system is linear,the transformation for a general input function is just the superposition of all such components at all frequencies,where the appropriate functional weighting is $\mathcal G ( f )$ . Of particular relevance here when considering inverse methods is the result that model basis function amplitudes at frequencies that are weakly mapped to the data (frequencies where $| \mathcal { G } ( f ) |$ is small) in a forward problem, and/or are obscured by noise, may be difficult or impossible to recover in an inverse problem.

The spectrum of the impulse response (transfer function) can be evaluated in a particularly useful analytical manner when we can express the forward problem $d ( t ) = G [ m ( t ) ]$ as a linear differential equation,

$$
\begin{array} { c } { \iota _ { r } m ^ { ( r ) } + a _ { r - 1 } m ^ { ( r - 1 ) } + \cdot \cdot \cdot + a _ { 1 } m ^ { ( 1 ) } + a _ { 0 } m } \\ { = b _ { q } d ^ { ( q ) } + b _ { q - 1 } d ^ { ( q - 1 ) } + \cdot \cdot \cdot + b _ { 1 } d ^ { ( 1 ) } + b _ { 0 } d , } \end{array}
$$

where the superscripts denote the order of time differentiation of $m$ and $d$ ,and the $a _ { i }$ and $b _ { i }$ are constant coefcients.Because each term in (8.31) is linear (there are no powers or other nonlinear functions of $m , d ,$ or their derivatives),and because differentiation is itself a linear operation, (8.31) expresses a linear time-invariant system obeying superposition and scaling.

If (8.31) operates on a model of the form $m ( t ) = e ^ { \imath 2 \pi f t }$ ，(8.30） indicates that the corresponding output will be $d ( t ) = \mathcal { G } ( \ f ) e ^ { \ i 2 \pi f t }$ Substituting this form of $m ( t )$ and differentiating each term,eachtimederivative, $m ^ { ( k ) }$ and $d ^ { ( k ) }$ , will generatecorresponding multipliers $( 2 \pi t f ) ^ { k }$ . Finally, dividing the resulting equation on both sides by $e ^ { \imath 2 \pi f t }$ ,and solving for $\mathcal G ( f )$ gives

$$
\begin{array} { c } { { \displaystyle \mathcal { G } ( f ) = \frac { \mathcal { D } ( f ) } { \mathcal { M } ( f ) } } } \\ { { = \frac { \sum _ { j = 0 } ^ { q } b _ { j } ( 2 \pi \imath f ) ^ { j } } { \sum _ { k = 0 } ^ { r } a _ { k } ( 2 \pi \imath f ) ^ { k } } . } } \end{array}
$$

The transfer function can thus be expressed as a ratio of two complex polynomials in $f$ for any system expressible in the form of (8.31). The $q + 1$ ， generally complex, frequencies $f _ { z }$ , for which the numerator of (8.33) is zero,are referred to as zeros of the transfer function (8.33). The predicted data for the forward problem will thus be zero for inputs of the form $e ^ { \imath 2 \pi f _ { z } t }$ ,regardlessof their amplitude. Any real-valued frequency, $f _ { z } = f _ { 0 }$ , corresponding to the Fourier model basis function $e ^ { \imath 2 \pi f _ { 0 } t }$ will thus lie in the model null space and be unrecoverable by any inverse methodology. The $r + 1$ ， generally complex, frequencies $f _ { p }$ for which the denominator of (8.33) is zero,are called poles of (8.33). The system will be unstable when excited by model basis functions $e ^ { \imath 2 \pi f _ { p } t }$ Along with a scalar gain factor, the transfer function (and hence the response) ofa general linear system that is expressible in the form of (8.31) can be completely characterized by tabulating the poles and zeros,along with a scalar gain factor. This characterization is commonly employed in specifying instrument responses.

# 8.2.LINEAR SYSTEMS IN DISCRETE TIME

To implement Fourier methods numerically,a discrete theory is required with properties that are analogous to the continuous transforms (8.16) and (8.18). This is achieved by the discrete Fourier transform, or DFT. In its most basic formulation, the DFT operates on a uniformly sampled (e.g., space or time) sequence with a specified number of terms $n$ The frequency, $f _ { s }$ , at which sampling occurs is called the sampling rate. The forward discrete Fourier transform of an $n \cdot$ -point sequence, $m _ { j } , j = 0$ ， $1 , \ldots , n - 1$ ,is

$$
\begin{array} { l } { \displaystyle \mathcal { M } _ { k } = ( { \mathrm { D F T } } [ { \mathbf { m } } ] ) _ { k } } \\ { \displaystyle = \sum _ { j = 0 } ^ { n - 1 } m _ { j } e ^ { - \imath 2 \pi j k / n } , } \end{array}
$$


<!-- chunk 0004: pages 211-280 -->
and its inverse is

$$
\begin{array} { l } { { \displaystyle m _ { j } = \big ( \mathrm { D F T } ^ { - 1 } [ \mathcal { M } ] \big ) _ { j } } } \\ { { \displaystyle ~ = \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } \mathcal { M } _ { k } e ^ { \imath 2 \pi j k / n } . } } \end{array}
$$

Equation (8.37) states that the sequence $m _ { j }$ can be expressed as a linear combination of the $n$ basis functions $e ^ { { \imath 2 \pi j k } / { n } }$ ， where the complex weights in the linear combination are the discrete spectral elements $\mathcal { M } _ { k }$ (with an additional scaling factor of $1 / n$ in (8.37)). The DFT basis functions are orthonormal on an $n$ -point interval in that, for any integers $l$ and $k$

$$
\frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } e ^ { \imath 2 \pi j l } e ^ { - \imath 2 \pi j k / n } = \left\{ { 1 } \atop { 0 } \right. \ l \ne k . \nonumber
$$

The DFT operations (8.35) and (8.37) are also widely referred to as the FFT and IFFT because a particularly efcient algorithm, the fast Fourier transform, is nearly ubiquitously used for their evaluation. The transforms can be calculated in MATLAB using the fft and ifft commands (note that FFT vectors and arrays in MATLAB,as is standard, are indexed beginning with one instead of zero). The DFT expression of Parseval’s theorem (8.23) is

$$
\sum _ { j = 0 } ^ { n - 1 } | m _ { j } | ^ { 2 } = \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } | \mathcal { M } _ { k } | ^ { 2 } .
$$

DFT spectra, $\mathcal { M } _ { k }$ ， are generally complex, discrete,and periodic,where the period is $n$ . There is an implicit assumption in DFT theory that the associated time domain sequence, $m _ { j }$ ,is also periodic with period $n$ Because of these periodicities,DFT results can be stored in complex vectors of length $n$ without loss of information,although (8.35)and (8.37) are valid for any integer index $k$ ，The DFT of a real-valued sequence has Hermitian symmetry about $k = 0$ and $k = n / 2$ , as defined by $\mathcal { M } _ { k } = \mathcal { M } _ { n - k } ^ { * }$ (see Exercise 8.2).

The mapping of the discrete spectrum index to specific frequencies is proportional to the sampling rate $f _ { s }$ .For $n$ even,the positive frequencies, $l f _ { s } / n$ ，where $l =$ 1,..., $n / 2 - 1$ , correspond to indices $k = 1$ ，， $n / 2 - 1$ , and the negative frequencies, $- l f _ { s } / n$ ,correspond to indices $k = n / 2 + 1$ ，.， $n - 1$ . The frequencies $\pm f _ { s } / 2$ have identical DFT values and correspond to index $k = n / 2$ .For $n$ odd, there is no integer $k$ corresponding to exactly half of the sampling rate. In this case, positive frequencies correspond to indices 1 through $( n - 1 ) / 2$ and negative frequencies correspond to indices $( n + 1 ) / 2$ through $n - 1$ .Figure 8.1 displays the discrete spectrum index-frequency mapping with respect to $k$ for an $n = 1 6$ -length DFT.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/8a021bb4104efb3cdda27cfd14f5812178a79ada345033114211067b41f28a27.jpg)  
Figure 8.1 Frequency and index mapping for the DFT of a real-valued sequence ( ${ \mathit { n } } = 1 6 )$ sampled at $f _ { s }$ .For DFT theory to accurately represent Fourier operations on a continuous time signal, $f _ { s }$ must be greater than or equal to the Nyquist frequency (8.40).

The Hermitian symmetry of the DFT implies that, for a real-valued sequence, the spectral amplitude, $| { \mathcal { M } } |$ ， is symmetric and the spectral phase is antisymmetric with respect to $k = 0$ and $k = n / 2$ . See Figure 8.1. For this reason it is customary to just plot the spectral amplitude and phase for positive frequencies in depicting the spectrum of a real signal.

For a uniformly sampled sequence to accurately represent a continuous function that contains nonnegligible spectral energy up to some maximum frequency $f _ { \mathrm { m a x } }$ ，the sampling rate, $f _ { s }$ , must be at least as large as the Nyquist frequency, $f _ { N }$ ，so that

$$
f _ { s } \ge f _ { N } = 2 f _ { \mathrm { m a x } } .
$$

Should (8.4O) not be met, a nonlinear and generally irreversible distortion called aliasing occurs. Generally speaking,aliasing causes spectral energy at frequencies $f > f _ { s } / 2$ to be“folded” and superimposed onto the DFT spectrum within the frequency range $- f _ { s } / 2 \le f \le f _ { s } / 2$

Consider a model sequence $m _ { j }$ of length $n$ and an impulse response sequence $g _ { j }$ of length $p$ , where both sequences are synchronously and uniformly sampled at $f _ { s } = 1 / \Delta t$ The discrete convolution of the two sequences can be performed in two ways.

The first method is a serial convolution, which produces a sequence of length $^ { n + }$ $p - 1$ ：

$$
d _ { j } = \sum _ { k = 0 } ^ { n - 1 } m _ { k } g _ { j - k } \ \Delta t \quad j = 0 , \ 1 , \ . \ . \ . \ , \ n + p - 2 .
$$

Serial convolution implements the discrete approximation to the convolution integral, and is implemented in MATLAB by the conv command.

The second type of discrete convolution is a circular convolution. Circular convo-lution is applicable to two sequences of equal length. If the lengths initially differ, they may be equalized by padding the shorter of the two sequences with zeros.The result of a circular convolution is as if each sequence is first expanded to be periodic (with period $n$ ),and then serially convolved solely on the index interval $j = 0$ ,1，..., $n - 1$ A circular convolution can be implemented using the discrete counterpart of the convolution theorem,

$$
\begin{array} { r c l } { \mathbf { d } = \mathrm { D F T } ^ { - 1 } [ \mathrm { D F T } [ \mathbf { m } ] \odot \mathrm { D F T } [ \mathbf { g } ] ] \Delta t } \\ { = \mathrm { D F T } ^ { - 1 } [ \mathcal { M } \odot \mathcal { G } ] \Delta t , } \end{array}
$$

where $\mathcal { M } \odot \mathcal { G }$ indicates element-by-element multiplication of the vectors $\mathcal { M }$ and $\mathcal { G }$

A very important practical consideration is that circular convolution implemented using the discrete convolution theorem (8.42) is much more efficient than serial convolution invoked with simple summation as in (8.41). To avoid wrap-around effects arising due to the implied $n \cdot$ -length periodicity of $\mathbf { m }$ and $\mathbf { g }$ in the circular convolution, and thus obtain a result that is indistinguishable from the serial convolution (8.41),it may be necessry to pad one or both series with up to $n$ zeros and apply (8.42) on the extended sequences.Because of the factoring strategy used in the FFT algorithm, it is also desirable for computational efficiency to pad $\mathbf { m }$ and $\mathbf { g }$ to lengths that are powers of 2,or are at least have many small prime factors.

Consider the case where we have a theoretically known, or accurately estimated, system impulse response, $g ( t )$ , convolved with an unknown model, $m ( t )$ . The continuous forward problem is

$$
d ( t ) = \int _ { a } ^ { b } g ( t - \tau ) m ( \tau ) \ d \tau .
$$

Uniformly discretizing this expression using simple collocation with a sampling rate, $f _ { s } = 1 / \Delta t$ , that is rapid enough to satisfy (8.4O) and thus avoid aliasing, gives

$$
\mathbf { d } = \mathbf { G } \mathbf { m } ,
$$

where $\mathbf { d }$ and $\mathbf { m }$ are $m$ and $n$ length sequences, respectively, and $\mathbf { G }$ is a matrix with $m$ rows of length $n$ .Each row of $\mathbf { G }$ is a time-reversed and time-shifted representation of the impulse response, scaled by $\Delta t$ to approximate the convolution integral,

$$
G _ { j , k } = g _ { j - k } \Delta t .
$$

This time domain representation of a forward problem convolution was previously examined in Example 3.2.

An inverse solution using Fourier methods can be obtained by first padding $\mathbf { d }$ and $\mathbf { g }$ appropriately with zeros so that they are of some equal and suficient length, $n$ ,to render moot any wrap-around artifacts associated with circular convolution. $\mathbf { G }$ then becomes an $n$ by $n$ matrix. Applying the DFT and (8.26) allows us to cast the forward problem as a complex-valued linear system,

$$
{ \mathcal { D } } = \mathbf { G } { \mathcal { M } } .
$$

$\mathbf { G }$ in (8.46) is a complex-valued diagonal matrix with

$$
G _ { k , k } = \mathcal { G } _ { k } ,
$$

where $\mathcal { G }$ is the discrete Fourier transform of the sampled impulse response g, $\mathcal { D }$ is the discrete Fourier transform of the data vector $\mathbf { d }$ and $\mathcal { M }$ is the discrete Fourier transform of the model vector m. We can write (8.46) more simply using the element-by-element multiplication operator as

$$
\mathcal { D } = \mathcal { G } \odot \mathcal { M } .
$$

Equation (8.46) suggests a solution by spectral division, where we first solve for the Fourier transform of the model using the element-by-element division operation (or equivalently, inverting the diagonal matrix $\mathbf { G }$ in (8.46)),

$$
\mathcal { M } = \mathcal { D } \oslash \mathcal { G } ,
$$

and then obtaining the model $\mathbf { m } = \mathrm { D F T } ^ { - 1 } [ \mathcal { M } ]$

Equation (8.49) is appealing in its simplicity and efficiency. The application of (8.26), combined with the effcient FFT implementation of the DFT, reduces the necessary computational effort from solving a potentially very large linear system of time domain equations (8.44) to just three $n \cdot$ -length DFT operations (taking the DFT of the data and impulse response vectors,and then the inverse DFT of the element-by-element quotient). If $\mathbf { d }$ and $\mathbf { g }$ are real, packing/unpacking algorithms also exist that allow DFT operations to be further reduced to complex vectors of length $n / 2$

However, (8.49) does not avoid the instability that is potentially associated with deconvolution if the reciprocal of any element in $\mathcal { G }$ is large. Equation (8.49) typically requires regularization to be useful.

# 8.3.WATER LEVEL REGULARIZATION

A straightforward and widely applied method of regularizing spectral division is water level regularization. The water level strategy employs a modified impulse response spectrum, $\mathcal { G } _ { \boldsymbol { w } }$ , in (8.49),where

$$
( \mathcal { G } _ { w } ) _ { i } = \left\{ \begin{array} { l l } { \mathcal { G } _ { i } } & { ( | \mathcal { G } _ { i } | > w ) } \\ { w ( \mathcal { G } _ { i } / | \mathcal { G } _ { i } | ) } & { ( 0 < | \mathcal { G } _ { i } | \leq w ) } \\ { w } & { ( \mathcal { G } _ { i } = 0 ) . } \end{array} \right.
$$

The water level regularized model estimate is then

$$
\begin{array} { r } { \mathbf { m } _ { w } = \mathrm { D F T } ^ { - 1 } \left[ \mathscr { D } \oslash \mathcal { G } _ { w } \right] \Delta t . } \end{array}
$$

The colorful name for this technique arises from the construction of $\mathcal { G } _ { w }$ ，applying the analogy of pouring water into the low-amplitude “holes” of $\mathcal { G }$ until the spectral amplitude levels there reach $w$ . The effect in (8.51） is to prevent undesirable noise amplification from occurring at frequencies where $\| \mathcal G \|$ is small.

An optimal water level value, $\boldsymbol { \nu }$ ，will reduce the sensitivity to noise in the inverse solution while stil recovering important model features. As is typical of the regularization process, it is possible to choose a “best” solution by assessing the trade-off between the norm of the residuals (fiting the data) and the model norm (smoothness of the model） as the regularization parameter $\boldsymbol { \nu }$ is varied. In calculating a trade-off curve, Parseval’s theorem (8.39) usefully facilitates calculations of the model and residual norms from spectra without calculating inverse Fourier transforms.Note that the 2-norm of the water level-regularized solution, $\mathbf { m } _ { u }$ ， will be nonincreasing with increasing $\boldsymbol { \nu }$ because $| ( \mathcal { G } _ { u } ) _ { i } | \geq | \mathcal { G } _ { i } |$

# Example 8.1

In Example 3.2, we investigated time domain deconvolution for uniformly sampled data with a sampling rate of $\dot { \gamma } _ { s } = 2 \ \mathrm { H z }$ using the truncated single value decomposition. Here, we solve this problem using frequency-domain deconvolution regularized via the water level technique. The impulse response, true model,and noisy data for this example are plotted in Figures 3.9, 3.11,and 3.12,respectively. We first pad the 210-point data and impulse response vectors with 21O additional zeros to eliminate wrap-around artifacts, and apply the fast Fourier transform to both vectors to obtain corresponding discrete spectra. The spectral amplitudes of the impulse response, data,and noise are critical in assessing the stability of the spectral division solution. See Figure 8.2. The frequencies range from O to $f _ { s } / 2 = 1$ Hz. Because spectral amplitudes for real-valued sequences are symmetric about $k = 0$ and $k = n / 2$ (Figure 8.1), only positive frequencies are shown.

Examining the impulse response spectral amplitude, $| \mathcal { G } _ { k } |$ , in Figure 8.2, we note that it decreases by approximately three orders of magnitude between very low frequencies and half of the sampling frequency $( f _ { s } / 2 = 1 \ \mathrm { H z } )$ . The convolution theorem (8.26) shows that the forward problem convolution multiplies the spectrum of the model by $\mathcal G ( f )$ in mapping it to the data. Thus,the convolution of a general signal with broad frequency content with this impulse response will strongly attenuate higher frequencies. Figure 8.2 also shows that the spectral amplitudes of the noise-free data fall off more quickly than the impulse response. This indicates that spectral division will be a stable process for noise-free data in this problem. Figure 8.2 also shows that the spectral amplitudes of the noisy data dominate the signal at frequencies higher than $f \approx 0 . 1 ~ \mathrm { H z }$ ，Because of the small values of $\mathcal { G } _ { k }$ at these frequencies,the spectral divi-sion solution using the noisy data will be dominated by noise (as was the case in the time domain solution of Example 3.2; see Figure 3.14). Figure 8.3 shows the amplitude spectrum of the noisy data (Figure 3.14) divided by the spectrum of the impulse response. The resulting model spectrum is dominated by noise at frequencies above about $0 . 1 \mathrm { H z }$

To regularize the spectral division solution,an optimal water level, $w$ ，is sought, where $\boldsymbol { \nu }$ should be large enough to avoid the undesirable amplification of noise. Figures 8.2 and 8.3 suggest that the optimal value of $w$ is near the crossover spectral amplitude where the data spectrum is surpassed by noise,or near $w$ somewhat greater than 1. However, such a determination might be more difficult for data with a more complex spectrum,and/or where the distinction between signal and noise spectra is generally less clear. Figure 8.4 shows an L-curve for this example, which suggests an optimal $\boldsymbol { \nu }$ close to 3. Figure 8.5 shows a corresponding range of solutions, and Figure 8.6 shows the solution for $w = 3 . 1 6$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/564b613fdcfb3c6e92fd9ddd3919a6f7397258c6ea093d4f45b132e43b8e2004.jpg)  
Figure 8.3 Spectral amplitudes resulting from the Fouriertransform of the noisy data divided by the Fourier transform of the impulse response (the transfer function).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/7b51d30b1132dc83556cbc2db8ef7a32c05f13e9474431d564b9febe5f732349.jpg)  
Figure8.4 L-curve fora logarithmically distributed range of water level values as indicated.

The solution shown in Figure 8.6, chosen from the corner of the trade-off curve of Figure 8.4, shows features of limited resolution that are typical of regularized solutions. In this case, imperfect resolution induced by regularization is manifested by reduced amplitude,oscillatory side lobes,and model broadening relative to the true model.

# 8.4.TIKHONOV REGULARIZATION IN THE FREQUENCY DOMAIN

An alternative regularized approach to solving the frequency-domain forward problem (8.46) is to consider the system as a least squares minimization problem,as we did in Chapter 4 (e.g., (4.4)):

$$
\operatorname* { m i n } \| \mathbf G \mathcal M - \mathcal D \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathcal M \| _ { 2 } ^ { 2 } .
$$

Expressing 8.52 as an augmented forward problem gives

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathcal { M } - \left[ \mathcal { D } \right] \right\| _ { 2 } ^ { 2 } } .
$$

We solve (8.53) by applying the normal equations using the conjugate transpose of the diagonal matrix $\mathbf { G }$ ， $\mathbf { G } ^ { H } ,$ which gives

$$
\big [ \mathbf { G } ^ { H } \quad \alpha \mathbf { I } \big ] \ \left[ \begin{array} { l } { \mathbf { G } } \\ { \alpha \mathbf { I } } \end{array} \right] \ \mathcal { M } = \big [ \mathbf { G } ^ { H } \quad \alpha \mathbf { I } \big ] \ \left[ \begin{array} { l } { \mathcal { D } } \\ { \mathbf { 0 } } \end{array} \right] .
$$

Equation (8.47) corresponds to the zeroth-order Tikhonov-regularized formulation

$$
( \mathbf { G } ^ { H } \mathbf { G } + \alpha ^ { 2 } \mathbf { I } ) \mathcal { M } = \mathbf { G } ^ { H } \mathcal { D } .
$$

with the frequency-domain solution,

$$
\mathcal { M } _ { \alpha } = ( \mathbf { G } ^ { H } \mathbf { G } + \alpha ^ { 2 } \mathbf { I } ) ^ { - 1 } \mathbf { G } ^ { H } \mathcal { D } .
$$

Because $\mathbf { G } ^ { H } \mathbf { G }$ is diagonal, (8.56)can be expressed solely using $n$ -length vector elementby-element operations as

$$
\mathcal { M } _ { \alpha } = ( \mathcal { G } ^ { H } \odot \mathcal { D } ) \oslash ( | \mathcal { G } | _ { 2 } ^ { 2 } + \alpha ^ { 2 } \mathbf { e } ) ,
$$

where $\mathbf { e }$ is an $n$ -length vector of ones. Applying the IDFT to $\mathcal { M } _ { \alpha }$ then produces the corresponding regularized time domain solution, m.

Although we have implemented $\| \mathcal { M } \| _ { 2 } = \| \mathrm { D F T } [ \mathbf { m } ] \| _ { 2 }$ rather than $\| \mathbf { m } \| _ { 2 }$ in (8.53) to regularize the problem, by Parseval's theorem (8.39),the norm of the model spectrum is proportional to the norm of the time domain model. Thus,(8.57) is equivalent to that obtained if we were to regularize using the norm of the model in the time domain model (although the specific values of $\alpha$ will be different).

An important consideration is that the inverse operation (8.57) is applied by elementby-element spectral division of $n$ -length vectors，so the solution can be calculated extremely eficiently relative to inverting a nondiagonal $n$ by $n$ matrix. Even with the additional calculations associated with the FFT, this methodology is typically much more efficient than a time domain approach, such as is described in Example 3.2.

To implement higher-order Tikhonov regularization, we note that

$$
\begin{array} { r l r } {  { \frac { d } { d t } m ( t ) = \frac { d } { d t } \int _ { - \infty } ^ { \infty } M ( f ) e ^ { 2 \pi f t } d f } } \\ & { } & { \displaystyle = \int _ { - \infty } ^ { \infty } \frac { \partial } { \partial t } [ M ( f ) e ^ { 2 \pi f t } ] d f } \\ & { } & { \displaystyle = \int _ { - \infty } ^ { \infty } 2 \pi \imath f M ( f ) e ^ { 2 \pi f t } d f } \\ & { } & { \displaystyle - \infty } \\ & { } & { \displaystyle = \mathcal { F } ^ { - 1 } [ 2 \pi \imath f \mathcal { M } ( f ) ] . } \end{array}
$$

Taking the Fourier transform of both sides gives

$$
\mathcal { F } \left[ \frac { d } { d t } m ( t ) \right] = 2 \pi \imath f \mathcal { M } ( f ) .
$$

Equation (8.59) enables us to effect a first derivative seminorm by multiplying each element of $\mathcal { M }$ by $2 \pi f _ { j }$ ，choosing the $f _ { j }$ to be proportional to the spectral frequency of the $j$ th-element (Figure 8.1). Proportionality is sufficient, because the exact con-stant frequency-scaling factor for converting the DFT index to frequency can be absorbed into the range of the regularization parameter $\alpha$ . Thus, we can effect pth-order Tikhonov regularization by solving

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathcal { M } - \left[ \mathcal { D } \right] \right\| _ { 2 } ^ { 2 } } ,
$$

where $\mathbf { K }$ is an $n$ by $n$ diagonal matrix with diagonal elements (e.g., for $n$ even)

$$
K _ { j , j } = \left\{ { ( j - 1 ) / n } \atop { ( j - 1 ) / n - 1 } \right. \quad j = 1 , 2 , \mathrm { ~ . ~ . ~ . ~ , ~ } n / 2 \eqno { }
$$

that are proportional to the frequency represented by the jth element of $\mathcal { M }$ . The least squares solution, obtained utilizing the normal equations, is thus

$$
\mathcal { M } _ { \alpha } = ( \mathbf { G } ^ { H } \mathbf { G } + \alpha ^ { 2 } \mathbf { K } ^ { 2 p } ) ^ { - 1 } \mathbf { G } ^ { H } \mathcal { D }
$$

or

$$
\mathcal { M } _ { \alpha } = ( \mathcal { G } ^ { H } \odot \mathcal { D } ) \oslash ( | \mathcal { G } | _ { 2 } ^ { 2 } + \alpha ^ { 2 } \mathbf { k } ^ { 2 p } ) ,
$$

where $\mathbf { k } ^ { 2 p }$ is the vector composed of the diagonal elements of $\mathbf { K } ^ { 2 p }$

As with the zeroth-order solution (8.57)，(8.63) can be evaluated very efficiently with element-by-element $n$ -length vector operations. Note that the implementation of the (nonidentity） matrix $\mathbf { K }$ in (8.62) weights the higher frequency components of the model more in the regularization,and thus tends to make them small. It is thus straightforward to consider and implement more general regularization matrices that will penalize particular Fourier components (e.g.， within a particular frequency range).

# Example 8.2

Let us reconsider Example 8.1 in a Tikhonov regularization framework.

We first implement zeroth-order regularization using (8.56) and examine the tradeoff curve (Figure 8.7). The suite of solutions is shown in Figure 8.8,and a solution selected from the trade-off curve is shown in Figure 8.9 compared with the true model. Note that, compared to the water level solution shown in Figure 8.6, the Tikhonov regularized solution has better amplitude recovery and is somewhat smoother. On the other hand, the recovered zeroth-order Tikhonov regularized model shows higher amplitude structure later in the time series. Applying second-order Tikhonov regularization, we obtain a corresponding trade-off curve (Figure 8.1O) and recover a still smoother model that is generally closer to the true model than either water level or zeroth-order Tikhonov regularization (Figures 8.11 and 8.12). The final accuracy of any regularized solution will,of course, depend on properties of the true solution.In this particular case the true model is smooth,and the second-order regularization solution is closest.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/6e71dc01e4522614ca9401af350daae9ced187bfc582aa679d0bc3b5f6de290b.jpg)  
Figure 8.7 L-curve for a logarithmically distributed range of regularization-parameter values, zerothorder Tikhonov regularization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/b6677abf70e4edebae615970b511002391f37632ed43a2acc8456258a5132d86.jpg)  
Figure 8.8 Zeroth-order Tikhonov regularized models corresponding to the range of regularization parameters used to construct Figure 8.7.Dashed curves show the true model,and bold trace shows the L-curve determined model with $\alpha = 0 . 4 8$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/8cce630e48c7856d0b0d87db0fab9f0ce96e09b76355e4f2e8eabcf2598f8c94.jpg)  
Figure 8.9 Zeroth-order Tikhonov regularized model corresponding to $\alpha = 0 . 4 8 .$ Dashed curve shows the true model.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/1e5d5cee01d72a05aeaa0e477384a6433724c6dea0e2e75651e6bf0c5a63a828.jpg)  
Figure 8.10 L-curve for a logarithmically distributed range of regularization-parameter values, second-order Tikhonov regularization.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/74c9ef63709c5c70d3125be15edf92dbbe1da0fef969b0f18cf189c7e889ca0e.jpg)  
Figure 8.11 Second-order Tikhonov regularized models corresponding to the range of regularization parameters used to construct Figure 8.7. Dashed curves show the true model,and bold trace shows the L-curve determined model with $\alpha = 3 0 . 2$ (Figure 8.10).

A significant new idea introduced by the Fourier methodology is that it provides a set of orthonormal model and data basis functions of the form of (8.27),the complex exponentials, that have the property of passing through a linear system altered in phase and amplitude,but not in frequency or functional character (8.3O). This remarkable fact is the essence of the convolution theorem (8.26),which leads to frequency-domain inverse methodologies that are very efficient when coupled with the FFT algorithm. This efficiency can become critically important when larger and/or higher-dimensional models are of interest, a large number of deconvolutions must be performed, or computational speed is critical, such as in real-time applications. The spectrum of the impulse response (such as in Figures 8.2 and 8.3) can be used to understand what frequency components may exhibit instability in an inverse solution. The information contained in the spectrum of Figure 8.2 is thus analogous to that obtained with a Picard plot in the context of the SVD (Chapters 3 and 4). The Fourier perspective also provides a link between linear inverse theory and the (vast) field of linear filtering. The deconvolution problem in this context is identical to finding an optimal inverse filter to recover the model while suppressing the influence of noise, and Tikhonov regularization in the frequency domain applies a preferential filtering to the solution that reduces amplitudes of high-frequency Fourier components.

# 8.5. EXERCISES

1. Given thatthe Fourier transform ofareal-valued linear system $g ( t )$ ，

$$
\mathcal { F } [ g ( t ) ] = \mathcal { G } ( f ) = \mathrm { r e a l } ( \mathcal { G } ( f ) ) + \operatorname* { i m a g } ( \mathcal { G } ( f ) ) = \alpha ( f ) + \imath \beta ( f ) ,
$$

is Hermitian,

$$
\mathcal { G } ( f ) = \mathcal { G } ^ { * } ( - f ) ,
$$

show that convolving $g ( t )$ with $\sin ( 2 \pi f _ { 0 } t )$ and $\cos ( 2 \pi f _ { 0 } t )$ produces the scaled and phase-shifted sinusoids,

$$
\begin{array} { r l } & { \boldsymbol { g } ( t ) \ast \sin ( 2 \pi f _ { 0 } t ) = \vert \boldsymbol { \mathcal { G } } ( f _ { 0 } ) \vert \sin ( 2 \pi f _ { 0 } t + \theta ( f _ { 0 } ) ) } \\ & { \boldsymbol { g } ( t ) \ast \cos ( 2 \pi f _ { 0 } t ) = \vert \boldsymbol { \mathcal { G } } ( f _ { 0 } ) \vert \cos ( 2 \pi f _ { 0 } t + \theta ( f _ { 0 } ) ) , } \end{array}
$$

where the scale factor is the spectral amplitude,

$$
| \mathcal { G } ( f _ { 0 } ) | = ( \alpha ^ { 2 } ( f _ { 0 } ) + \beta ^ { 2 } ( f _ { 0 } ) ) ^ { \frac { 1 } { 2 } } ,
$$

and the phase-shift factor is the spectral phase

$$
\theta ( f _ { 0 } ) = \tan ^ { - 1 } \left( \frac { \beta ( f _ { 0 } ) } { \alpha ( f _ { 0 } ) } \right) .
$$

2. (a) Demonstrate using (8.35) that the DFT of an $n \cdot$ -point, real-valued sequence, $\mathbf { x }$ ， is Hermitian, i.e.,

$$
\mathcal { X } _ { n - k } = \mathcal { X } _ { k } ^ { * }
$$

(b) Demonstrate that the Hermitian symmetry shown in part (a) implies that the $N$ independent elements in a time series $\mathbf { x }$ produce $N / 2 + 1$ independent elements $N$ even) or $( N - 1 ) / 2 + 1$ independent elements ( $_ N$ odd) in the DFT $\mathcal { X }$ .As the DFT has an inverse (8.37) that reproduces $\mathbf { x }$ from $\mathcal { X }$ ,clearly information has not been lost in taking the DFT, yet the number of independent elements in $\mathbf { x }$ and $\mathcal { X }$ differ. Explain.

3.A linear damped vertical harmonic oscillator consisting of a mass suspended on a lossy spring is affixed to the surface of a terrestrial planet to function as a seismometer, where the recorded displacement, $z ( t )$ ,of the mass relative to its equilibrium position will depend on ground motion (note that when the surface of the planet moves upward, the inertia of the mass will tend to make it remain at rest,and the corresponding motion of the mass relative to its suspension system will be downward). For an upward ground displacement, $u ( t )$ , the system can be mathematically modeled as the linear differential equation (8.31) as

$$
\frac { d ^ { 2 } z } { d t ^ { 2 } } + \frac { D } { M } \frac { d z } { d t } + \frac { K } { M } z = \frac { d ^ { 2 } u } { d t ^ { 2 } } ,
$$

where the physical properties of the oscillator are defined by the mass $M$ ，the displacement-proportional spring force constant $K$ ，and the velocity-proportional damping force constant $D$

(a) By taking the Fourier transform of (8.71),obtain the transfer function $\mathcal { G } ( f ) =$ $\mathcal { Z } ( f ) / \mathcal { U } ( f )$ ,where $\mathcal { Z } ( f )$ and $\mathcal { U } ( f )$ are the Fourier transforms of $z ( t )$ and $u ( t )$ ， respectively.

In terms of $M , K$ and $D$ ,and $f _ { s } = \sqrt { K / M }$ ：

(b) For what general frequency range of ground motion will the response of this instrument be difficult to remove via a deconvolution?   
(c) For what general frequency range of ground motion will the output of this instrument be nearly identical to the true ground motion?

4.A displacement seismogram is observed from a large earthquake at a far-field seismic station, from which the source region can be approximated as a point. A much smaller aftershock from the main shock region is used as an empirical Green's function for this event. It is supposed that the observed signal from the large event should be approximately equal to the convolution of the main shock's rupture history with this empirical Green’s function. The 256-point seismogram is in the file seis.mat. The impulse response of the seismometer is in the file impresp.mat.

(a) Deconvolve the impulse response from the observed main shock seismogram using frequency-domain Tikhonov zeroth-order deconvolution to solve for the source time function of the large earthquake.Note that the source time function is expected to consist of a nonnegative pulse or set of pulses. Estimate the source duration in samples and assess any evidence for subevents and their relative dura-tions and amplitudes. Approximately what water level do you believe is best for this data set? Why?

(b) Perform second-order ( $\vert p = 2 )$ , frequency-domain Tikhonov deconvolution to solve this problem. See Exercise 8.4(b).

(c)Recast the problem as a discrete linear inverse problem,as described in the example for Chapter 3,and solve the system using second-order Tikhonov regularization.

(d) Are the results in (c) better or worse than in (a) or (b)? How and why? Compare the amount of time necessary to find the solution in each case on your computing platform.

# 8.6. NOTES AND FURTHER READING

Although we examine one-dimensional convolution and deconvolution problems here for conceptual simplicity, note that these results are readily generalizable to higher dimensions,and higher-dimensional formulations of the DFT are widely utilized.

MATLAB has a general $n \cdot$ -dimensional set of FFT algorithms,fftn and ifftn. Many regularization matrices (e.g., the $\mathbf { L }$ roughening matrices introduced for one-dimensional Tikhonov regularization in this text (4.27) and (4.28) are easily recognized as convolutions,where the rows are time-reversed sampled representations of the impulse response of the convolution effected by $\mathbf { L m }$ Fourier analysis of the frequency response of regularization matrices thus facilitates more sophisticated regularization matrix design.

In some physics and geophysics treatments, the sign convention chosen for the complex exponentials in the Fourier transform and its inverse may be reversed, so that the forward transform (8.16) has a plus sign in the exponent and the inverse transform (8.18) has a minus sign in the exponent. This alternative sign convention merely induces a complex conjugation in the spectrum that is reversed when the corresponding inverse transform is applied. An additional convention issue arises as to whether to express frequency in ${ \mathrm { H z ~ } } ( f )$ or radians per second $( \omega = 2 \pi f .$ ). Alternative Fourier transform formulations using $\omega$ differ from (8.16) and (8.18) by a simple change of variables, and introduce scaling factors of $2 \pi$ in the forward, reverse, or both transforms.

Gubbins [6O] also explores connections between Fourier and inverse theory in a geophysical context. Kak and Slaney [84] give an extensive treatment of Fourier-based methods for tomographic imaging. Vogel [169] discusses Fourier methods for image deblurring. Because of the tremendous utility of Fourier techniques, there are numerous resources on their use in the physical sciences,engineering,and pure mathematics. A basic treatment covering theory and some applications at the approximate level of this text is [2O],and a recommended advanced text on the topic is [131].

# Nonlinear Regression

# Synopsis

Common approaches to solving nonlinear regression problems are introduced, extending the development of linear regression in Chapter 2. We begin with a discussion of Newton's method,which provides a general framework for solving nonlinear systems of equations and nonlinear optimization problems.Then we discuss the Gauss-Newton (GN) and Levenberg-Marquardt (LM) methods, which are versions of Newton's method specialized for nonlinear regression problems.The distinction between LMand Tikhonov regularization is also made. Statistical aspects and implementation issues are addressed,and examples of nonlinear regression are presented.

# 9.1. INTRODUCTION TO NONLINEAR REGRESSION

In previous chapters we have concentrated on linear forward and inverse problems,and have seen that such problems are uniformly approachable using a variety of solution methods. We wil next consider problems that are nonlinear, i.e., forward and inverse problems that do not obey the rules of superposition (1.5) and scaling (1.6). There is no general theory for the solution of nonlinear parameter estimation and inverse problems. However, we wil see that iterative strategies incorporating linear concepts can be applied to solve them in many circumstances.

# 9.2. NEWTON'S METHOD FOR SOLVING NONLINEAR EQUATIONS

Consider a nonlinear system of $m$ equations in $m$ unknowns

$$
\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 } { \mathrm { . } }
$$

We will construct a sequence of vectors, $\mathbf { x } ^ { 0 } , \mathbf { x } ^ { 1 }$ ，.．.，that will converge to a solution $\mathbf { x } ^ { * }$ . If the nonlinear vector function $\mathbf { F }$ is continuously differentiable，we can construct a Taylor series approximation about some starting solution estimate, $\mathbf { x } ^ { 0 }$ ，

$$
\begin{array} { r } { \mathbf { F } \big ( \mathbf { x } ^ { 0 } + \Delta \mathbf { x } \big ) \approx \mathbf { F } \big ( \mathbf { x } ^ { 0 } \big ) + \mathbf { J } \big ( \mathbf { x } ^ { 0 } \big ) \Delta \mathbf { x } , } \end{array}
$$

where $\mathbf { J } ( \mathbf { x } ^ { 0 } )$ is the Jacobian,

$$
\mathbf { J } \big ( \mathbf { x } ^ { 0 } \big ) = \left[ \begin{array} { c c c } { \frac { \partial F _ { 1 } ( \mathbf { x } ) } { \partial x _ { 1 } } } & { \mathbf { \textnormal { . . . } } } & { \frac { \partial F _ { 1 } ( \mathbf { x } ) } { \partial x _ { m } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial F _ { m } ( \mathbf { x } ) } { \partial x _ { 1 } } } & { \mathbf { \textnormal { . . . } } } & { \frac { \partial F _ { m } ( \mathbf { x } ) } { \partial x _ { m } } } \end{array} \right] \Bigg \vert _ { \mathbf { x } = \mathbf { x } ^ { 0 } } .
$$

Using (9.2),and expressing the difference between the desired solution, $\mathbf { x } ^ { * }$ ,and $\mathbf { x } ^ { 0 }$ as

$$
\Delta \mathbf { x } = \mathbf { x } ^ { * } - \mathbf { x } ^ { 0 }
$$

gives

$$
\mathbf { F } ( \mathbf { x } ^ { * } ) = \mathbf { 0 } \approx \mathbf { F } ( \mathbf { x } ^ { 0 } ) + \mathbf { J } ( \mathbf { x } ^ { 0 } ) \Delta \mathbf { x } ,
$$

which produces a linear system of equations,

$$
\mathbf { J } ( \mathbf { x } ^ { 0 } ) \Delta \mathbf { x } \approx - \mathbf { F } ( \mathbf { x } ^ { 0 } ) ,
$$

that can be solved for $\Delta \mathbf { x }$ to improve the solution estimate.

# Algorithm 9.1 Newton's Method

Given a system of equations $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ and an initial solution $\mathbf { x } ^ { 0 }$ ， repeat the following steps to compute a sequence of solutions $\mathbf { x } ^ { k }$ . Stop if and when the sequence adequately converges to a solution with $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$

1. Calculate the Jacobian $\mathbf { J } ( \mathbf { x } ^ { k } )$ and $\mathbf { F } ( \mathbf { x } ^ { k } )$ .   
2. Solve $\mathbf { J } ( \mathbf { x } ^ { k } ) \Delta \mathbf { x } = - \mathbf { F } ( \mathbf { x } ^ { k } )$   
3.Let $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \Delta \mathbf { x }$   
4.Let $k = k + 1$

The theoretical properties of Newton’s method are summarized in the follwing theorem. For a proof, see [39].

Theorem 9.1 If $\mathbf { \dot { x } } ^ { 0 }$ is close enough to $\mathbf { x } ^ { * }$ $\mathbf { F } ( \mathbf { x } )$ is continuously differentiable in a neighborhood of $\mathbf { \dot { x } } ^ { * }$ ，and $\mathbf { J } ( \mathbf { x } ^ { * } )$ is nonsingular, then Newton's method will converge to $\mathbf { x } ^ { * }$ . The convergence rate is quadratic in the sense that there is a constant $c$ ， such that for large $k$ ，

$$
\left\| \mathbf { x } ^ { k + 1 } - \mathbf { x } ^ { * } \right\| _ { 2 } \leq c \left\| \mathbf { x } ^ { k } - \mathbf { x } ^ { * } \right\| _ { 2 } ^ { 2 } .
$$

In practical terms,quadratic convergence means that as we approach $\mathbf { x } ^ { * }$ , the number of accurate digits in the solution doubles at each iteration. Unfortunately, if the hypotheses in the above theorem are not satisfied, then Newton's method can converge very slowly or even fail altogether.

A simple modification to Newton’s method often helps with convergence problems. In the damped Newton's method, we use the Newton’s method equations at each iteration to compute an iterative correction to the working solution. However, instead of taking the full step $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \Delta \mathbf { x }$ , we perform a line search across solutions lying along the line $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \alpha \Delta \mathbf { x }$ for a range of positive $\alpha$ values and take the one with minimum $\| \mathbf F ( \mathbf x ^ { k + 1 } ) \| _ { 2 }$

Now suppose that we wish to minimize a scalar-valued function $f ( \mathbf { x } )$ . If we assume that $f ( \mathbf { x } )$ is twice continuously differentiable,we can construct a Taylor series approximation,

$$
f ( \mathbf { x } ^ { 0 } + \Delta \mathbf { x } ) \approx f ( \mathbf { x } ^ { 0 } ) + \nabla f ( \mathbf { x } ^ { 0 } ) ^ { T } \Delta \mathbf { x } + \frac { 1 } { 2 } \Delta \mathbf { x } ^ { T } \mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) \Delta \mathbf { x } ,
$$

where $\nabla f ( \mathbf { x } ^ { 0 } )$ is the gradient

$$
\begin{array} { r } { \nabla f ( \mathbf { x } ^ { 0 } ) = [ { \begin{array} { c } { \frac { \partial f ( \mathbf { x } ) } { \partial x _ { 1 } } } \\ { \vdots } \\ { \frac { \partial f ( \mathbf { x } ) } { \partial x _ { m } } } \end{array} } ]  _ { \mathbf { x } = \mathbf { x } ^ { 0 } } } \end{array}
$$

and $\mathbf { H } ( f (  { \mathbf { x } } ^ { 0 } ) )$ is the Hessian

$$
\mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) = \left[ \begin{array} { c c c } { \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { 1 } ^ { 2 } } } & { \cdot \mathbf { \nabla } \cdot \mathbf { \nabla } \cdot \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { 1 } \partial x _ { m } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { m } \partial x _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot \mathbf { \nabla } \cdot \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { m } ^ { 2 } } } \end{array} \right] \left[ \begin{array} { c } { \mathbf { \nabla } \cdot \mathbf { x } } \\ { \mathbf { \nabla } \cdot \mathbf { \nabla } \cdot \mathbf { \nabla } } \\ { \mathbf { \nabla } \cdot \mathbf { x } } \end{array} \right] .
$$

A necessary condition for $\mathbf { x } ^ { * }$ to be a minimum of $f ( \mathbf { x } )$ is that $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ . We can approximate the gradient in the vicinity of $x ^ { 0 }$ by

$$
\nabla f ( \mathbf { x } ^ { 0 } + \Delta \mathbf { x } ) \approx \nabla f ( \mathbf { x } ^ { 0 } ) + \mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) \Delta \mathbf { x } .
$$

Setting the approximate gradient (9.11) equal to zero gives

$$
\mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) \Delta \mathbf { x } = - \nabla f ( \mathbf { x } ^ { 0 } ) .
$$

Solving the linear system of equations (9.12) for successve solution steps leads to Newton's method for minimizing $f ( \mathbf { x } )$

Since Newton's method for minimizing $f ( \mathbf { x } )$ is exactly Newton's method for solving a nonlinear system of equations applied to $\mathbf { F } = \nabla f ( \mathbf { x } ) = \mathbf { 0 }$ , the convergence proof follows immediately from the proof of Theorem 9.1.

Theorem 9.2 If $f ( \mathbf { x } )$ is twice continuously differentiable in a neighborhood of a local minimizer $\mathbf { x } ^ { * }$ ， there is a constant $\lambda$ such that $\| \mathbf { H } ( f ( \mathbf { x } ) ) - \mathbf { H } ( f ( \mathbf { y } ) ) \| _ { 2 } \leq \lambda \| \mathbf { x } - \mathbf { y } \| _ { 2 }$ for every

vector y in the neighborhood, $\mathbf { H } ( f ( \mathbf { x } ^ { * } ) )$ is positive definite, and $\mathbf { x } ^ { 0 }$ is close enough to $\mathbf { x } ^ { * }$ ，then Newton's method will converge quadratically to $\mathbf { x } ^ { * }$

# Algorithm 9.2 Newton's Method for Minimizing $f ( \mathbf { x } )$

Given a twice continuously diffrentiable function $f ( \mathbf { x } )$ , and an initial solution $\mathbf { x } ^ { 0 }$ , repeat the following steps to compute a sequence of solutions $\mathbf { x } ^ { 1 }$ ， $\mathbf { x } ^ { 2 }$ ，.... Stop if and when the sequence adequately converges to a solution with $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$

1. Calculate the gradient $\nabla f ( \mathbf { x } ^ { k } )$ and Hessian $\mathbf { H } ( f ( \mathbf { x } ^ { k } ) )$   
2. Solve $\mathbf { H } ( f ( \mathbf { x } ^ { k } ) ) \Delta \mathbf { x } = - \nabla f ( \mathbf { x } ^ { k } )$   
3.Let $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \Delta \mathbf { x }$   
4.Let $k = k + 1$

Newton's method for minimizing $f ( \mathbf { x } )$ can be very effcient, but the method can also fail to converge. As with Newton's method for solving a system of equations, the convergence properties of the algorithm can be improved in practice by modifying the model update step with a line search.

# 9.3.THE GAUSS-NEWTON AND LEVENBERG-MARQUARDTMETHODS FOR SOLVING NONLINEAR LEAST SQUARES PROBLEMS

Newton's method is not directly applicable to most nonlinear regression and inverse problems. We may not have equal numbers of data points and model parameters, there may not be an exact solution to $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ or $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ may have multiple solutions. Here,we will use a specialized version of Newton's method to minimize a nonlinear least squares problem.

Given a nonlinear system of equations $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ ,consider the problem of finding an $n$ -length parameter vector, m, constrained by an $n \cdot$ -length data vector, d, with associated specified data standard deviations. Our goal is to find a set of parameters that best fits the data in the sense of minimizing the 2-norm of the residuals.

As with linear regression, if we assume that the measurement errors are normally distributed, then the maximum likelihood principle leads us to minimizing the sum of squared residuals normalized by their respective standard deviations (2.12). We seek to minimize the weighted residual norm

$$
f ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } { \bigg ( } { \frac { G ( \mathbf { m } ) _ { i } - d _ { i } } { \sigma _ { i } } } { \bigg ) } ^ { 2 } .
$$

We define the scalar-valued functions

$$
f _ { i } ( \mathbf { m } ) = \frac { G ( \mathbf { m } ) _ { i } - d _ { i } } { \sigma _ { i } } i = 1 , 2 , . . . , m
$$

and the vector-valued function

$$
\mathbf { F ( m ) } = \left[ \begin{array} { c } { f _ { 1 } ( \mathbf { m } ) } \\ { \vdots } \\ { f _ { m } ( \mathbf { m } ) } \end{array} \right] .
$$

Thus

$$
f ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } f _ { i } ( \mathbf { m } ) ^ { 2 } = \| \mathbf { F } ( \mathbf { m } ) \| _ { 2 } ^ { 2 } .
$$

The gradient of $f ( \mathbf { m } )$ can be writen as the sum of the gradients of the individual terms,

$$
\nabla f ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } \nabla \big ( f _ { i } ( \mathbf { m } ) ^ { 2 } \big ) .
$$

The elements of the gradient of $f ( \mathbf { m } )$ are

$$
( { \nabla } f ( { \mathbf { m } } ) ) _ { j } = \sum _ { i = 1 } ^ { m } 2 f _ { i } ( { \mathbf { m } } ) ( { \nabla } f _ { i } ( { \mathbf { m } } ) ) _ { j } ,
$$

and the gradient can thus be written in matrix notation as

$$
\nabla f ( \mathbf { m } ) = 2 \mathbf { J } ( \mathbf { m } ) ^ { T } \mathbf { F } ( \mathbf { m } ) ,
$$

where $\mathbf { J } ( \mathbf { m } )$ is the Jacobian

$$
\mathbf { J } ( \mathbf { m } ) = \left[ \begin{array} { c c c } { \frac { \partial f _ { 1 } ( \mathbf { m } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial f _ { 1 } ( \mathbf { m } ) } { \partial m _ { n } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial f _ { m } ( \mathbf { m } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial f _ { m } ( \mathbf { m } ) } { \partial m _ { n } } } \end{array} \right] .
$$

Similarly, we can express the Hessian of $f ( \mathbf { m } )$ using the $f _ { i } ( \mathbf { m } )$ terms to obtain

$$
\begin{array} { l } { { \displaystyle { \bf H } ( f ( { \bf m } ) ) = \sum _ { i = 1 } ^ { m } { \bf H } ( f _ { i } ( { \bf m } ) ^ { 2 } ) } \ ~ } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } { \bf H } ^ { i } ( { \bf m } ) } , } \end{array}
$$

where $\mathbf { H } ^ { i } ( \mathbf { m } )$ is the Hessian of $f _ { i } ( \mathbf { m } ) ^ { 2 }$

The $j , k$ element of $\mathbf { H } ^ { i } ( \mathbf { m } )$ is

$$
\begin{array} { l } { { \displaystyle { \cal H } _ { j , k } ^ { i } ( { \bf m } ) = \frac { \partial ^ { 2 } ( f _ { i } ( { \bf m } ) ^ { 2 } ) } { \partial m _ { j } \partial m _ { k } } } \ ~ } \\ { { \displaystyle ~ = \frac { \partial } { \partial m _ { j } } \bigg ( 2 f _ { i } ( { \bf m } ) \frac { \partial f _ { i } ( { \bf m } ) } { \partial m _ { k } } \bigg ) } \ ~ } \\ { { \displaystyle ~ = 2 \bigg ( \frac { \partial f _ { i } ( { \bf m } ) } { \partial m _ { j } } \frac { \partial f _ { i } ( { \bf m } ) } { \partial m _ { k } } + f _ { i } ( { \bf m } ) \frac { \partial ^ { 2 } f _ { i } ( { \bf m } ) } { \partial m _ { j } \partial m _ { k } } \bigg ) } . } \end{array}
$$

Thus

$$
\mathbf { H } ( f ( \mathbf { m } ) ) = 2 \mathbf { J } ( \mathbf { m } ) ^ { T } \mathbf { J } ( \mathbf { m } ) + \mathbf { Q } ( \mathbf { m } ) ,
$$

where

$$
\mathbf { Q } ( \mathbf { m } ) = 2 \sum _ { i = 1 } ^ { m } f _ { i } ( \mathbf { m } ) \mathbf { H } ( f _ { i } ( \mathbf { m } ) ) .
$$

In the Gauss-Newton (GN) method, we ignore the $\mathbf { Q } ( \mathbf { m } )$ term in (9.26) and approximate the Hessian as

$$
\mathbf { H } ( f ( \mathbf { m } ) ) \approx 2 \mathbf { J } ( \mathbf { m } ) ^ { T } \mathbf { J } ( \mathbf { m } ) .
$$

In the context of nonlinear regression, we expect that the $f _ { i } ( \mathbf { m } )$ terms will be small as we approach the optimal parameters $\mathbf { m } ^ { * }$ , so that this should be a reasonable approximation in the vicinity of the solution. Conversely, this is not a reasonable approximation for nonlinear least squares problems in which the values of $f _ { i } ( \mathbf { m } )$ can be large.

Implementing Newton's method for minimizing $f ( \mathbf { m } )$ (9.12) using the gradient (9.19)and the approximate Hessian (9.28),and dividing both sides by 2, we obtain

$$
\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) \Delta \mathbf { m } = - \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { F } ( \mathbf { m } ^ { k } ) ,
$$

which provides a formula for solving for successive update steps $\Delta \mathbf { m }$ The $n$ by $n$ matrix $\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ is symmetric and positive semidefinite. If the matrix is actually positive definite then we can use the Cholesky factorization or another full-rank method to solve the system of equations for $\Delta \mathbf { m }$ However, if the matrix is singular then such straightforward approaches will fail. Although the GN method often works wellin practice, it is based on Newton's method, and can thus fail by converging to a local maximum or saddle point where $\nabla f ( \mathbf { m } ) \approx 0$ , or by not converging at all. An additional point to con-sider in using GN and other such iterative methods is that the algorithm may converge to a local minimum rather than to a global minimum (see Section 9.5).

In the Levenberg-Marquardt (LM) method, the GN method model update equations (9.29) are modified to

$$
( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \lambda \mathbf { I } ) \Delta \mathbf { m } = - \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { F } ( \mathbf { m } ^ { k } ) ,
$$

and the positive parameter $\lambda$ is adjusted during the course of iterations to ensure convergence. One important reason for this modification is to ensure that the matrix on the left-hand side of (9.3O) is nonsingular. Since the matrix in this system of equations is symmetric and positive definite,we can use the Cholesky factorization to efficiently solve the system for the model update steps $\delta \mathbf { m }$

For very large values of $\lambda$ ，

$$
\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \lambda \mathbf { I } \approx \lambda \mathbf { I } ,
$$

and the solution to (9.30) is

$$
\Delta \mathbf { m } \approx - \frac { 1 } { \lambda } \nabla f ( \mathbf { m } ) .
$$

This is called a steepest-descent step, meaning that the algorithm simply moves down-gradient to most rapidly reduce $f ( \mathbf { m } )$ . The steepest-descent approach provides very slow but certain convergence to a local minimum. Conversely, for very small values of $\lambda$ ,the LM method reverts to the GN method (9.29),which gives potentially fast but uncertain convergence.

A challenge associated with implementing the LM method is determining the optimal value of $\lambda$ . The general strategy is to use small values of $\lambda$ in situations where the GN method is working well, but to increase $\lambda$ when the GN method fails to make progress in reducing the residual norm. A simple approach is to start with a small value of $\lambda$ ,and then adjust it in every iteration. If the LM method leads to a residual norm reduction, then update $\mathbf { m }$ and decrease $\lambda$ by a constant multiplicative factor (e.g.,a factor of 2) before the next iteration. Conversely, if the LM method does not improve the solution,we then increase $\lambda$ by a constant factor and try again,repeating this process until a model update is found that decreases the residual norm. Robust implementations of the LM method use more sophisticated strategies for adjusting $\lambda$ ,but even this simple strategy works surprisingly well.

In practice,a careful LM implementation offers the good performance of the GN method as well as robust convergence properties,and LM is usually the method of choice for smal- to medium-sized nonlinear least squares problems.

Note that although the LM stabilization term λI in (9.3O) resembles expressions used elsewhere (e.g., Chapter 4) for Tikhonov regularization purposes,it does not alter the ultimate model achieved at convergence. The λI term is used to stabilize the solution of the linear system of equations that determines the search direction to be used.Because the λI term is only used as a way to improve the convergence of the algorithm,and does not enter into the residual norm objective function that is being minimized, it does not regularize the nonlinear least squares problem. We discuss the regularization of nonlinear problems in Chapter 10.

# 9.4. STATISTICAL ASPECTS OF NONLINEAR LEAST SQUARES

Recall from Appendix B that if a vector $\mathbf { d }$ has a multivariate normal distribution,and A is an appropriately sized matrix, then Ad also has a multivariate normal distribution with an associated covariance matrix

$$
\operatorname { C o v } ( \mathbf { A } \mathbf { d } ) = \mathbf { A } \operatorname { C o v } ( \mathbf { d } ) \mathbf { A } ^ { T } .
$$

In Chapter 2, we applied this formula to the linear least squares problem for $\mathbf { G m } = \mathbf { d }$ ， which we solved by the normal equations. The resulting formula for $\operatorname { C o v } ( \mathbf { m } )$ was

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathrm { C o v } ( \mathbf { d } ) \mathbf { G } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } . } \end{array}
$$

In the simplest case, where $\mathbf { C o v } ( \mathbf { d } ) = \sigma ^ { 2 } \mathbf { I } .$ (9.34) simplified to

$$
\begin{array} { r } { \mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = \sigma ^ { 2 } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } . } \end{array}
$$

For the nonlinear regression problem，we no longer have a linear relationship between the data and the estimated model parameters,so we cannot assume that the estimated model parameters have a multivariate normal distribution,and cannot use the above formulas. However, we can obtain useful corresponding formulas by linearization if the data errors are not too large.

If small data perturbations result in small model perturbations in a nonlinear system, we can consider a linearization of the misfit function (9.15) about a solution, $\mathbf { m } ^ { * }$ ：

$$
\begin{array} { r } { \mathbf { F ( m ^ { * } + \Delta m ) } \approx \mathbf { F ( m ^ { * } ) } + \mathbf { J ( m ^ { * } ) } \Delta \mathbf { m } . } \end{array}
$$

Under this approximation, there is a linear relationship between changes in $\mathbf { F }$ and changes in the parameters m:

$$
\mathbf { F ( m ^ { * } + \Delta \Delta m ) } - \mathbf { F ( m ^ { * } ) } = \Delta \mathbf { F } \approx \mathbf { J ( m ^ { * } ) } \Delta \mathbf { m } .
$$

To the extent that the residual misfit terms (the elements of $\mathbf { F } ( \mathbf { m } ^ { * } ) )$ are small, the Hessian can be approximated by (9.28). In this case $\mathbf { J } ( \mathbf { m } ^ { * } )$ in nonlinear regression can take the place of $\mathbf { G }$ in linear problems (e.g.， (9.35)） to estimate the covariance of the model parameters. Equation (9.13) incorporates the respective data element standard deviations $\sigma _ { i }$ into the formula for the residual norm $f ( \mathbf { m } )$ ,and explicitly weights the nonlinear constraint equations. $\operatorname { C o v } ( \mathbf { d } )$ , in the case of independent data errors,is thus the identity matrix in such a weighted system. In this case we have

$$
\mathrm { C o v } ( \mathbf { m } ^ { * } ) \approx ( \mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ) ^ { - 1 } .
$$

As in Chapter 2,we can construct a $9 5 \%$ confidence elipsoid for the fitted parameters in terms of this covariance matrix,

$$
( \mathbf { m } - \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ( \mathbf { m } - \mathbf { m } ^ { * } ) \leq \Delta ^ { 2 } ,
$$

where $\Delta ^ { 2 }$ is the ninety-fifth percentile of a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom. It is important to reiterate that this confidence elipsoid only defines an approximate confidence region because we linearized $\mathbf { F } ( \mathbf { m } )$ in (9.37).

As in Chapter 2,there is an alternative derivation of the $9 5 \%$ confidence region for the fitted parameters in terms of $\chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } ^ { * } )$ . If we let

$$
\chi ^ { 2 } ( \mathbf { m } ) = \| \mathbf { F } ( \mathbf { m } ) \| _ { 2 } ^ { 2 } = \mathbf { F } ( \mathbf { m } ) ^ { T } \mathbf { F } ( \mathbf { m } ) ,
$$

then the inequality

$$
\chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } ^ { * } ) \leq \Delta ^ { 2 }
$$

defines an approximate $9 5 \%$ confidence region for $\mathbf { m } ^ { * }$ . Because of the nonlinearity in the $\chi ^ { 2 } ( \mathbf { m } )$ function, this $9 5 \%$ confidence region is typically not an elipsoid. Unfortunately, this confidence region is not exact,because this development is still based on the assumption of multivariate normality, and $\mathbf { m } ^ { * }$ , because it is not a linear combination of the data vector elements, wil not in general have a multivariate normal distribution in nonlinear problems.

Should (9.39) or (9.41) be used in practice? If $G ( \mathbf { m } )$ is not too strongly nonlinear, then there should be very little difference between the two confidence region. However, if $G ( \mathbf { m } )$ is more strongly nonlinear, then the difference between the two confidence regions may be large and neither confidence region can really be trusted. In such situations,Monte Carlo methods are a more useful and appropriate way to estimate parameter uncertainty. This is discussed further in Chapter 11.

As with linear regression, it is possible to apply nonlinear regression when the measurement errors are independent and normally distributed and the standard deviations are unknown but assumed to be equal (Section 3.3). We set the $\sigma _ { i }$ to 1 and minimize the sum of squared errors, and define a residual vector,

$$
r _ { i } = G ( \mathbf { m } ^ { * } ) _ { i } - d _ { i } \quad i = 1 , 2 , \ldots , m .
$$

Our estimate of the measurement standard deviation is then

$$
s = \sqrt { \frac { \| \mathbf { r } \| _ { 2 } ^ { 2 } } { m - n } } ,
$$

and the corresponding approximate covariance matrix for the estimated model parameters is

$$
\mathrm { C o v } ( \mathbf { m } ^ { * } ) = s ^ { 2 } ( \mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ) ^ { - 1 } .
$$

Given $\mathbf { m } ^ { * }$ and $\mathrm { C o v } ( \mathbf { m } ^ { * } )$ , we can establish confidence intervals for the model parameters using the methods described in Chapter 2.As with any parameter estimation problem, it is also important to examine the residuals for systematic patterns or deviations from normality. If we have not estimated the measurement standard deviation s from the fitted residuals,then it is also important to test the $\chi ^ { 2 }$ value for goodness of fit and perform an associated $\pmb { p }$ -value test (2.21) if we have normally distributed data errors.The appropriateness of this test will depend on how well the nonlinear model is approximated by the Jacobian linearization for points near the optimal parameter values.

# Example 9.1

A classic method in hydrology for determining the transmissivity and storage coeficient of an aquifer is called the“slug test” [49].

A known volume $Q$ of water (the slug) is injected into a well,and the resulting effects on the head, $h$ ，at an observation well a distance $d$ away from the injection well are observed at various times $t$ ，The change in the head measured at the observation well typically increases rapidly and then decreases more slowly. We wish to determine the dimensionless storage coefficient, $S$ ，and the transmissivity $T$

The mathematical model for the slug test is

$$
h = { \frac { Q } { 4 \pi T t } } e ^ { - d ^ { 2 } S / ( 4 T t ) } .
$$

We know the parameters $Q = 5 0 ~ \mathrm { m } ^ { 3 }$ and $d = 6 0 \mathrm { ~ m ~ }$ ，and the times $t$ at which the head $h$ is measured. Our data are given in Table 9.1,where head measurements are roughly accurate to $0 . 0 1 \mathrm { ~ m ~ }$ $( \sigma _ { i } = 0 . 0 1 \mathrm { ~ m ~ }$ ).

The optimal parameter values are $S = 0 . 0 0 2 0 7$ and $T = 0 . 5 8 5 ~ \mathrm { m } ^ { 2 } / \mathrm { h r }$ .The observed $\chi ^ { 2 }$ value is 2.04, with a corresponding $p$ -value of O.73.Thus this fit passes the $\chi ^ { 2 }$ test. The data points and fitted curve are shown in Figure 9.1.

Using the Jacobian evaluated at the optimal parameter values,we computed an approximate covariance matrix for the fitted parameters. The resulting $9 5 \%$ confidence intervals for $S$ and $T$ are

$$
\begin{array} { l } { S = 0 . 0 0 2 0 7 \pm 0 . 0 0 0 1 2 } \\ { \ } \\ { T = 0 . 5 8 5 \pm 0 . 0 2 9 \ \mathrm { m } ^ { 2 } / \mathrm { h r } . } \end{array}
$$

Table 9.1 Slug Test Data   

<table><tr><td rowspan=1 colspan=1>t (hr)</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>h (m)</td><td rowspan=1 colspan=1>0.72</td><td rowspan=1 colspan=1>0.49</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>0.12</td></tr></table>

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/db0e7e744ba1fb00ed984b2e88fd3dfb26dbb4355520306cb4636083c7789b7e.jpg)  
Figure 9.1 Data, with one standard deviation error bars,and fitted model for the slug test.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/499f95b17d8fa82c24c1af49970520fff0e2bc2c02bba9aab5e7726579b1e308.jpg)  
Figure 9.2 $\chi ^ { 2 }$ contour plot for the slug test for a wide range of parameters.The small box shows the close-up axis range displayed in Figure 9.3.

A contour plot of the $\chi ^ { 2 }$ surface obtained by varying $S$ and $T$ is shown in Figure 9.2. Note that,unlike our earlier linear regression problems,the contours are not even approximately eliptical because of the nonlinearity of the problem. However, if we zoom into the immediate vicinity of the optimal parameters (Figure 9.3),we find that the $\chi ^ { 2 }$ contours are approximately ellptical at this scale. The approximate ellipticity of the contours indicates that the linear approximation of ${ \bf G } ( { \bf m } )$ around the optimal parameter values is a reasonable approximation for model perturbations in this range.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/124133e810303e726e0c059436e82e18529681e92cd2aac527b5c904276d49e2.jpg)  
Figure 9.3 Close-up $\chi ^ { 2 }$ contour plot for the immediate vicinity of the optimal parameters $\mathbf { m } ^ { * }$ for the slug test example, showing nonlinear $90 \%$ ， $9 5 \%$ (bold), and $9 9 \%$ confidence contours.The nearly elliptical contours are indicative of a approximatelylinear behavior at this scale.Dashed ellipse shows the linearized approximation to the $9 5 \%$ confidence contour calculated using (9 38). Ninety-five percent confidence intervals for the parameters calculated from (9.38)are shown as dashed lines.

# 9.5.IMPLEMENTATION ISSUES

Iterative methods for solving nonlinear problems require the computation of the functions $f _ { i } ( \mathbf { m } )$ and their partial derivatives with respect to the model parameters $m _ { j }$ These partial derivatives in turn depend on the derivatives of the nonlinear $\mathbf { G }$ ：

$$
\frac { \partial f _ { i } ( \mathbf { m } ) } { \partial m _ { j } } = \frac { 1 } { \sigma _ { i } } \frac { \partial \mathbf { G } ( \mathbf { m } ) _ { i } } { \partial m _ { j } } .
$$

In some cases, we have explicit formulas for $\mathbf { G } ( \mathbf { m } )$ and its derivatives. In other cases, $\mathbf { G } ( \mathbf { m } )$ exists only as a black box subroutine that can be called as required to evaluate the function.

When an explicit formula for $\mathbf { G } ( \mathbf { m } )$ is available,and the number of parameters is relatively small, we can differentiate analytically. There also exist automatic differen-tiation software packages that can translate the source code of a program that computes $\mathbf { G } ( \mathbf { m } )$ into a program that computes the derivatives of ${ \bf G } ( { \bf m } )$

Another approach is to use finite differences to approximate the derivatives of ${ \bf G } ( { \bf m } ) _ { i }$ .A simple first-order scheme is to employ the linearization

$$
\frac { \partial G ( \mathbf { m } ) _ { i } } { \partial m _ { j } } \approx \frac { G ( \mathbf { m } + h \mathbf { e } _ { j } ) _ { i } - G ( \mathbf { m } ) _ { i } } { h } ,
$$

where $\mathbf { e } _ { j }$ is the jth standard basis vector,and the scalar $h$ is chosen to be suitably small. However, if $h$ becomes very small, significant round-off error in the numerator of (9.49) may occur. A good rule of thumb is to set $h = \sqrt { \epsilon }$ , where $\epsilon$ is the relative accuracy of the evaluations of ${ \bf G } ( { \bf m } ) _ { i }$ . For example,if the function evaluations are accurate to O.0001, then an appropriate choice of $h$ would be about O.01. Determining the actual accuracy of function evaluations can be diffcult, especially when $\mathbf { G }$ is a black box routine. One useful assessment technique is to plot function values as a parameter of interest is varied over a small range. These plots should be smooth at the scale of $h$ When $\mathbf { G }$ is available only as a black box subroutine that can be called with particular values of $\mathbf { m }$ ，and the source code for the subroutine is not available,then the only available approach is to use finite differences.

In practice, many diffculties in solving nonlinear regression problems can be traced back to incorrect derivative computations. It is thus a good idea to cross-check any available analytical formulas for the derivative with finite-difference approximations. Many software packages for nonlinear regression include options for checking the accuracy of derivative formulas.

A second important issue in the implementation of the GN and LM methods is deciding when to terminate the iterations. We would like to stop when the gradient $\nabla f ( \mathbf { m } )$ is approximately O and $\mathbf { m }$ has stopped changing substantially from one iteration to the next. Because of scaling issues, it is not possible to set an absolute tolerance on $\| \nabla f ( \mathbf { m } ) \| _ { 2 }$ that would be appropriate for all problems. Similarly, it is difficult to pick a single absolute tolerance on $\| \mathbf { m } ^ { \bar { k } + 1 } - \mathbf { m } ^ { k } \| _ { 2 }$ or $| f ( \mathbf { m } ^ { k + 1 } ) - f ( \mathbf { m } ^ { k } ) |$

The following convergence tests have been normalized so that they will work well on a wide variety of problems.We assume that values of $\mathbf { G } ( \mathbf { m } )$ can be calculated with a relative accuracy of $\epsilon$ . To ensure that the gradient of $f ( \mathbf { m } )$ is approximately 0, we require that

$$
\| \nabla f ( \mathbf { m } ^ { k } ) \| _ { 2 } < \sqrt { \epsilon } ( 1 + | f ( \mathbf { m } ^ { k } ) | ) .
$$

To ensure that successive values of $\mathbf { m }$ are close, we require

$$
\begin{array} { r } { \| \mathbf { m } ^ { k } - \mathbf { m } ^ { k - 1 } \| _ { 2 } < \sqrt { \epsilon } ( 1 + \| \mathbf { m } ^ { k } \| _ { 2 } ) . } \end{array}
$$

Finally to make sure that the values of $f ( \mathbf { m } )$ have stopped changing, we require that

$$
| f ( \mathbf { m } ^ { k } ) - f ( \mathbf { m } ^ { k - 1 } ) | < \epsilon ( 1 + | f ( \mathbf { m } ^ { k } ) | ) .
$$

There are a number of additional problems that can arise during the solution of a nonlinear regression problem by the GN or LM methods related to the functional behavior of $f ( \mathbf { m } )$

The first issue is that our methods, because they involve calculation of the Jacobian and the Hessian, assume that $f ( \mathbf { m } )$ is a smooth function. This means not only that $f ( \mathbf { m } )$ must be continuous,but also that its first and second partial derivatives with respect to the parameters must be continuous. Figure 9.4 shows a function that is itself continuous, but has discontinuities in the first derivative at $m = 0 . 2$ and the second derivative at $m = 0 . 5$ . When $\mathbf { G } ( \mathbf { m } )$ is given by an explicit formula, it is usually easy to verify that $f ( \mathbf { m } )$ is smooth, but when $\mathbf { G } ( \mathbf { m } )$ is implemented as a black box routine it may be difficult.

A second issue is that the function $f ( \mathbf { m } )$ may have a “flat bottom.” See Figure 9.5. In such cases, there are many values of $\mathbf { m }$ that come close to fitting the data,and it is difficult to determine the optimal $\mathbf { m } ^ { * }$ . In practice, this condition is seen to occur when $\mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } )$ is nearly singular. Because of this ill-conditioning, computing accurate confidence intervals for the model parameters can be effectively impossible. We will address this difficulty in Chapter 1O by applying regularization.

The final problem that we will consider is that $f ( \mathbf { m } )$ may be nonconvex and therefore have multiple local minimum points. See Figure 9.6. The GN and LM methods are designed to converge to a local minimum, but depending on where we begin the search, there is no way to be certain that such a solution will be a global minimum. Depending on the particular problem, the optimization algorithm might well converge to a locally optimal solution.

Global optimization methods have been developed to deal with this issue [17, 75, 76,140]. Deterministic global optimization procedures can be used on problems with a very small number of variables,while stochastic search procedures can be applied to large-scale problems. Stochastic search procedures can be quite effective in practice, even though they do not find a global optimum with certainty.

However, even a deterministic global optimization procedure is not a panacea. In the context of nonlinear regression, if the nonlinear least squares problem has multiple locally optimal solutions with similar objective function values, then each of these solutions will correspond to a statistically likely solution. We cannot simply report one globally optimal solution as our best estimate and construct confidence intervals using (9.38),because this would mean ignoring other likely solutions. However, if we could show that there is one globally optimal solution and other locally optimal solutions have very small $p .$ -values, then it would be appropriate to report the globally optimal solution and corresponding confidence intervals.

Although a thorough discusson of global optimization is beyond the scope of this book,we will discuss one simple global optimization procedure called the multistart method in the next example. In the multistart method, we randomly generate a large number of initial solutions,and then apply the LM method starting with each of these initial solutions. We then examine the local minimum solutions found by the procedure, and examine ones with acceptable values of $f ( \mathbf { m } )$ . The multistart approach has two important practical advantages. First, by potentially identifying multiple locally optimal solutions,we can determine whether there is more than one statistically likely solution. Second, we can make effective use of the fast convergence of the LM method to find the locally optimal solutions.

# Example 9.2

Consider the problem of fiting a model of two superimposed exponential decay functions characterized by four parameters,

$$
\gamma _ { i } = m _ { 1 } e ^ { m _ { 2 } x _ { i } } + m _ { 3 } x _ { i } e ^ { m _ { 4 } x _ { i } } ,
$$

to a set of observations. The true model parameters are $m _ { 1 } = 1 . 0 , m _ { 2 } = - 0 . 5 , m _ { 3 } = 1 . 0$ ， and $m _ { 4 } = - 0 . 7 5$ ,and the $x _ { i }$ values are 25 evenly spaced points between 1 and 7. We compute corresponding $\gamma _ { i }$ values and add independent normally distributed noise with a standard deviation of O.O1 to obtain a synthetic data set.

We next apply the LM method to solve the problem 2O times,using random initial solutions,with each initial parameter uniformly distributed between $- 1$ and 1. This produces a total of three different locally optimal solutions (Table 9.2).

Solution number 1, with a $\chi ^ { 2 }$ value of approximately 17, has an acceptable $p$ -value of about O.69 for a regression with 21 degrees of freedom. The other two solutions have unreasonably large $\chi ^ { 2 }$ values,and hence much lower $p$ -values.We will thus analyze only the first solution. Figure 9.7 shows the data points with $1 \sigma$ error bars and the fitted curve for solution number 1,and Figure 9.8 shows the corresponding residuals normalized by the data standard deviations.Note that the majority of the residuals are within O.5 standard deviations,with a few residuals as large as 1.9 standard deviations. There is no obvious residual trend as $_ x$ ranges from 1 to 7.

Table 9.2 Locally Optimal Solutions for the Sample Problem   

<table><tr><td>Solution Number</td><td>m1</td><td>m2</td><td>m3</td><td>m4</td><td>x²</td><td>p-value</td></tr><tr><td>1</td><td>0.9874</td><td>-0.5689</td><td>1.0477</td><td>-0.7181</td><td>17.3871</td><td>0.687</td></tr><tr><td>2</td><td>1.4368</td><td>0.1249</td><td>-0.5398</td><td>-0.0167</td><td>40.0649</td><td>0.007</td></tr><tr><td>3</td><td>1.5529</td><td>-0.1924</td><td>-0.1974</td><td>-0.1924</td><td>94.7845</td><td>2 ×10-11</td></tr></table>

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/3230c0d69d943d6296c4f12f663fa0b7532622c5334e55940f42d319866a79f0.jpg)  
Figure 9.7 Data points and fitted curve.   
Figure 9.8 Normalized residuals corresponding to Figure 9.7.

Next, we compute the approximate covariance matrix for the model parameters using (9.38). The square roots of the diagonal elements of the covariance matrix are standard deviations for the individual model parameters. These are then used to compute $9 5 \%$ confidence intervals for model parameters. The solution parameters with $9 5 \%$ confidence intervals are

$$
\begin{array} { l } { m _ { 1 } = 0 . 9 8 \pm 0 . 2 2 } \\ { m _ { 2 } = - 0 . 5 7 \pm 0 . 7 7 } \\ { m _ { 3 } = 1 . 0 5 \pm 0 . 5 0 } \\ { m _ { 4 } = - 0 . 7 2 \pm 0 . 2 0 . } \end{array}
$$

The true parameters $( 1 , - 0 . 5 , \ 1$ ，and $- 0 . 7 5 )$ are all covered by these confidence intervals. However, there is a large degree of uncertainty. This is an example of a poorly conditioned nonlinear regresson problem in which the data do not strongly constrain the parameter values.

The correlation matrix provides some insight into the nature of the ill-conditioning in this example by quantifying strong parameter trade-offs. For our preferred solution, the correlation matrix calculated using (9.38) is

$$
\rho = \left[ { \begin{array} { r r r r } { 1 . 0 0 } & { - 0 . 8 4 } & { 0 . 6 8 } & { 0 . 8 9 } \\ { - 0 . 8 4 } & { 1 . 0 0 } & { - 0 . 9 6 } & { - 0 . 9 9 } \\ { 0 . 6 8 } & { - 0 . 9 6 } & { 1 . 0 0 } & { 0 . 9 3 } \\ { 0 . 8 9 } & { - 0 . 9 9 } & { 0 . 9 3 } & { 1 . 0 0 } \end{array} } \right] .
$$

Note the strong positive and negative correlation between pairs of parameters. The high negative correlation between $m _ { 1 }$ and $m _ { 2 }$ tells us that by increasing $m _ { 1 }$ and simultaneously decreasing $m _ { 2 }$ we can obtain a solution that is very nearly as good as our optimal solution. There are also strong negative correlations between $m _ { 2 }$ and $m _ { 3 }$ and between $m _ { 2 }$ and $m _ { 4 }$

# 9.6. EXERCISES

1. Show that (9.29) is equivalent to the normal equations (2.3) when $G ( \mathbf { m } ) = \mathbf { G } \mathbf { m }$ where $\mathbf { G }$ is a matrix of constant coefficients.

2. A recording instrument sampling at $5 0 ~ \mathrm { H z }$ records a noisy sinusoidal voltage signal in a 40-s-long record. The data are to be modeled using

$$
\gamma ( t ) = A \sin ( 2 \pi f _ { 0 } t + \phi ) + c + \sigma \eta ( t )
$$

where $\eta ( t )$ is believed to be unit standard deviation,independent,and normally distributed noise,and $\sigma$ is an unknown standard deviation.Using the data in the MATLAB data file instdata.mat, solve for the parameter $( A , f _ { 0 } , \phi , c )$ ，using the

LM method. Show that it is critical to choose a good initial solution (suitable initial parameters can be found by examining a plot of the time series by eye). Once you are satisfied that you have found a good solution, use it to estimate the noise amplitue $\sigma$ Use your solution and estimate of $\sigma$ to find corresponding covariance and correlation matrices and $9 5 \%$ parameter confidence intervals. Which pair of parameters is most strongly correlated? Are there multiple equally good solutions for this problem?

3. In hydrology, the van Genuchten model is often used to relate the volumetric water content in an unsaturated soil to the head [52]. The model is

$$
\theta ( h ) = \theta _ { r } + \frac { \theta _ { s } - \theta _ { r } } { ( 1 + ( - \alpha h ) ^ { n } ) ^ { ( 1 - 1 / n ) } }
$$

where $\theta _ { s }$ is the volumetric water content at saturation, $\theta _ { r }$ is the residual volumetric water content at a very large negative head, and $\alpha$ and $n$ are two parameters which can be fit to laboratory measurements.

The file vgdata.mat contains measurements for a loam soil at the Bosque del Apache National Wildlife Refuge in New Mexico [68]. Fit the van Genuchten model to the data. The volumetric water content at saturation is $\theta _ { s } = 0 . 4 4$ ,and the residual water content is $\theta _ { r } = 0 . 0 9$ . You may assume that the measurements of $\theta ( h )$ are accurate to about $2 \%$ of the measured values.

You will need to determine appropriate values for $\sigma _ { i }$ , write functions to compute $\theta ( h )$ and its derivatives,and then use the LM method to estimate the parameters. In doing so, you should consider whether or not this problem might have local minima. It will be helpful to know that typical values of $\alpha$ range from about O.001 to 0.02, and typical values of $n$ run from 1 to 10.

4.An alternative version of the LM method stabilizes the GN method by multiplicative damping. Instead of adding λI to the diagonal of $\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ , this method multi-plies the diagonal ofJ $[ ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ by a factor of $( 1 + \lambda )$ . Show that this method can fail by producing an example in which the modified. $\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ matrix is singular, no matter how large $\lambda$ becomes.

5.A cluster of 1O small earthquakes occurs in a shallow geothermal reservoir. The field is instrumented with nine seismometers,eight of which are at the surface and one of which is $3 0 0 ~ \mathrm { m }$ down a borehole. The P-wave velocity of the fractured granite medium is thought to be an approximately uniform $2 ~ \mathrm { k m } / \mathrm { s }$ .The station locations (in meters relative to a central origin) are given in Table 9.3 and in the MATLAB data file stmat.mat.

The arrival times of P-waves from the earthquakes are carefully measured at the stations,with an estimated error of approximately $1 ~ \mathrm { m s }$ .The arrival time estimates for each earthquake, $\mathrm { e } _ { i }$ , at each station (in seconds relative to an arbitrary reference), are given in Table 9.4. These data can also be found in the MATLAB data file eqdata.mat.

Table 9.3 Station Locations for the Earthquake Location Problem   

<table><tr><td>Station</td><td>x(m)</td><td>y(m)</td><td>z(m)</td></tr><tr><td>1</td><td>500</td><td>-500</td><td>0</td></tr><tr><td>2</td><td>-500</td><td>-500</td><td>0</td></tr><tr><td>3</td><td>100</td><td>100</td><td>0</td></tr><tr><td>4</td><td>-100</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>100</td><td>0</td></tr><tr><td>6</td><td>0</td><td>-100</td><td>0</td></tr><tr><td>7</td><td>0</td><td>-50</td><td>0</td></tr><tr><td>8</td><td>0</td><td>200</td><td>0</td></tr><tr><td>9</td><td>10</td><td>50</td><td>-300</td></tr></table>

Table9.4 Data for the Earthquake Location Problem. Times are in Seconds   

<table><tr><td>Station</td><td>e1</td><td>e2</td><td>e3</td><td>e4</td><td>e5</td></tr><tr><td>1</td><td>0.8423</td><td>1.2729</td><td>0.8164</td><td>1.1745</td><td>1.1954</td></tr><tr><td>2</td><td>0.8680</td><td>1.2970</td><td>0.8429</td><td>1.2009</td><td>1.2238</td></tr><tr><td>3</td><td>0.5826</td><td>1.0095</td><td>0.5524</td><td>0.9177</td><td>0.9326</td></tr><tr><td>4</td><td>0.5975</td><td>1.0274</td><td>0.5677</td><td>0.9312</td><td>0.9496</td></tr><tr><td>5</td><td>0.5802</td><td>1.0093</td><td>0.5484</td><td>0.9145</td><td>0.9313</td></tr><tr><td>6</td><td>0.5988</td><td>1.0263</td><td>0.5693</td><td>0.9316</td><td>0.9480</td></tr><tr><td>7</td><td>0.5857</td><td>1.0141</td><td>0.5563</td><td>0.9195</td><td>0.9351</td></tr><tr><td>8</td><td>0.6017</td><td>1.0319</td><td>0.5748</td><td>0.9362</td><td>0.9555</td></tr><tr><td>9</td><td>0.5266</td><td>0.9553</td><td>0.5118</td><td>0.8533</td><td>0.8870</td></tr><tr><td>Station</td><td>e6</td><td>e7</td><td>e8</td><td>e9</td><td>e10</td></tr><tr><td>1</td><td>0.5361</td><td>0.7633</td><td>0.8865</td><td>1.0838</td><td>0.9413</td></tr><tr><td>2</td><td>0.5640</td><td>0.7878</td><td>0.9120</td><td>1.1114</td><td>0.9654</td></tr><tr><td>3</td><td>0.2812</td><td>0.5078</td><td>0.6154</td><td>0.8164</td><td>0.6835</td></tr><tr><td>4</td><td>0.2953</td><td>0.5213</td><td>0.6360</td><td>0.8339</td><td>0.6982</td></tr><tr><td>5</td><td>0.2795</td><td>0.5045</td><td>0.6138</td><td>0.8144</td><td>0.6833</td></tr><tr><td>6</td><td>0.2967</td><td>0.5205</td><td>0.6347</td><td>0.8336</td><td>0.6958</td></tr><tr><td>7</td><td>0.2841</td><td>0.5095</td><td>0.6215</td><td>0.8211</td><td>0.6857</td></tr><tr><td>8</td><td>0.3025</td><td>0.5275</td><td>0.6394</td><td>0.8400</td><td>0.7020</td></tr><tr><td>9</td><td>0.2115</td><td>0.4448</td><td>0.5837</td><td>0.7792</td><td>0.6157</td></tr></table>

a.Apply the LM method to this data set to estimate least squares locations of the earthquakes.

b.Estimate the uncertainties in $x , \ y , \ z$ (in meters) and origin time (in seconds) for each earthquake using the diagonal elements of the appropriate covariance matrix. Do the earthquake locations follow any discernible trend?

Table 9.5 Data for the Lightning Mapping Array Problem   

<table><tr><td>Station</td><td>t(s)</td><td>x(km)</td><td>y(km)</td><td>z(km)</td></tr><tr><td>1</td><td>0.0922360280</td><td>-24.3471411</td><td>2.14673146</td><td>1.18923667</td></tr><tr><td>2</td><td>0.0921837940</td><td>-12.8746056</td><td>14.5005985</td><td>1.10808551</td></tr><tr><td>3</td><td>0.0922165500</td><td>16.0647214</td><td>-4.41975194</td><td>1.12675062</td></tr><tr><td>4</td><td>0.0921199690</td><td>0.450543748</td><td>30.0267473</td><td>1.06693166</td></tr><tr><td>6</td><td>0.0923199800</td><td>-17.3754105</td><td>-27.1991732</td><td>1.18526730</td></tr><tr><td>7</td><td>0.0922839580</td><td>-44.0424408</td><td>-4.95601205</td><td>1.13775547</td></tr><tr><td>8</td><td>0.0922030460</td><td>-34.6170855</td><td>17.4012873</td><td>1.14296361</td></tr><tr><td>9</td><td>0.0922797660</td><td>17.6625731</td><td>-24.1712580</td><td>1.09097830</td></tr><tr><td>10</td><td>0.0922497250</td><td>0.837203704</td><td>-10.7394229</td><td>1.18219520</td></tr><tr><td>11</td><td>0.0921672710</td><td>4.88218031</td><td>10.5960946</td><td>1.12031719</td></tr><tr><td>12</td><td>0.0921702350</td><td>16.9664920</td><td>9.64835135</td><td>1.09399160</td></tr><tr><td>13</td><td>0.0922357370</td><td>32.6468622</td><td>-13.2199767</td><td>1.01175261</td></tr></table>

6. The Lightning Mapping Array is a portable system that locates the sources of lightning radio-frequency radiation in three spatial dimensions and time [132]. The system measures the arrival times of impulsive radiation events with an uncertainty specified by a standard deviation of $7 \times 1 0 ^ { - 2 } ~ \mu \mathrm { s }$ . Measurements are made at multiple locations, typically in a region 40 to $6 0 \mathrm { k m }$ in diameter.Each station records the peak radiation event in successive $1 0 0 \mathrm { - } \mu \mathrm { s }$ time intervals; from such data,several hundred to over a thousand distinct radiation sources may typically be located per lightning discharge. Example data from the LMA are shown in Table 9.5 and are found in the MATLAB data file lightningdata.mat.

a.Use the arrival times at stations 1,2,4,6,7,8,10,and 13 to find the time and location of the associated source. Assume that radio wave signals travel along straight paths at the speed of light in a vacuum $( 2 . 9 9 7 \times 1 0 ^ { 8 } ~ \mathrm { m } / \mathrm { s } )$ .   
b.A challenge in dealing with the large number of detections from the LMA is to disentangle overlapping signals from multiple events. Locate using subsets of the data set to find the largest subset of the data for nine or more stations that gives a good solution,and compare it to the station subset from part (a).

# 9.7. NOTES AND FURTHER READING

Newton's method is central to the field of optimization [39, 58, 87,88,119],and is, because of its speed, the basis for most methods of nonlinear optimization.A number of modifications to the method are used to ensure convergence to a local minimum of $f ( \mathbf { x } )$ [58,119]. One important difficulty in Newton’s method is that, for very large problems, it may be impractical to store the Hessan matrix. Specialized methods have ben developed for the solution of such large-scale optimization problems [58, 119].

The GN and LM methods are discussed in more detail in [16,58, 119]. Statistical aspects of nonlinear regression are discussed in [7,4O,113]. A more detailed discus-sion of the termination criteria for the LM method described in Section 9.5 can be found in [58]. There are a number of freely available and commercial software packages for nonlinear regression, including GaussFit [82], MINPACK [111], and ODRPACK [18]. Automatic differentiation has applications in many areas of numerical computing, including optimization and numerical solution of ordinary and partial diferential equations. Two books that survey this topic are [34,57]. Global optimization is a large field of research. Some basic references include [17,75,76]. For a survey of global optimization methods in geophysical inversion, see [140].

# Nonlinear Inverse Problems

# Synopsis

The nonlinear regression approaches of Chapter 9 are generalized to problems requiring regularization. The Tikhonov regularization and Occam's inversion approaches are introduced. Seismic tomography and electrical conductivity inversion examples are used to illustrate the application of these methods.Resolution analysis for nonlinear problems is addressed.

# 10.1.REGULARIZING NONLINEAR LEAST SQUARES PROBLEMS

As with linear problems,the nonlinear least squares approaches can run into difficulty with ill-conditioned problems. This typically happens as the number of model parameters grows. Here,we will discuss regularization of nonlinear inverse problems and algorithms for computing a regularized solution to a nonlinear inverse problem.

The basic ideas of Tikhonov regularization can be extended to nonlinear problem. Suppose that we are given a nonlinear discrete inverse problem where an $n \cdot$ -element model m and an $m \cdot$ -element data vector $\mathbf { d }$ are related by a nonlinear system of equations $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ .For convenience, we will assume that the m nonlinear constraint equations have been scaled to incorporate the measurement standard deviations $\sigma _ { i }$ . We seek the solution with the smallest seminorm $\| \mathbf { L m } \| _ { 2 }$ that comes sufficiently close to fitting the data vector, where $\mathbf { L }$ is an appropriate roughening matrix (e.g., (4.28)).

We can formulate this problem as

$$
\begin{array} { r l } & { \operatorname* { m i n } \| \mathbf { L m } \| _ { 2 } } \\ & { \| \mathbf { G } ( \mathbf { m } ) - \mathbf { d } \| _ { 2 } \leq \delta . } \end{array}
$$

Note that the form of the problem is virtually identical to that which was considered in the linear case (e.g., (4.25)),with the only difference being that we now have a general function ${ \bf G } ( { \bf m } )$ instead of a matrix-vector multiplication $\mathbf { G m }$ 、As in the linear case, we can reformulate this problem in terms of minimizing the misfit subject to a constraint on $\| \mathbf { L m } \| _ { 2 }$ ，

$$
\begin{array} { r l } & { \operatorname* { m i n } \lVert \mathbf G ( \mathbf { m } ) - \mathbf d \rVert _ { 2 } } \\ & { \qquad \lVert \mathbf { L m } \rVert _ { 2 } \leq \epsilon , } \end{array}
$$

or as a regularized (often referred to as “damped") least squares problem,

$$
\operatorname* { m i n } \| \mathbf G ( \mathbf { m } ) - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf L \mathbf m \| _ { 2 } ^ { 2 } .
$$

All three versions of the regularized least squares problem can be solved by applying standard nonlinear optimization software. In particular, (1O.3) is a nonlinear least squares problem, so we can apply the LM or GN methods to it. Of course,any such approach will still have to deal with the possbility of local minima that are not global minimum points. In some cases, it is possible to show that nonlinear least squares problems are convex,and thus possess only global minima. In other cases we will have to employ multistart or some other global optimization strategy to determine whether there are multiple minima.

To apply the GN method to (10.3), we rewrite it as

$$
\operatorname* { m i n } \left\| { \bf G } ( { \bf m } ) - { \bf d } \right\| _ { 2 } ^ { 2 } .
$$

The Jacobian of (1O.4) for the kth iteration is

$$
\mathbf { K } ( \mathbf { m } ^ { k } ) = \left[ \begin{array} { c } { \mathbf { J } ( \mathbf { m } ^ { k } ) } \\ { \alpha \mathbf { L } } \end{array} \right] ,
$$

where $\mathbf { J } ( \mathbf { m } ^ { k } )$ is the Jacobian of $\mathbf { G } ( \mathbf { m } ^ { k } )$ . A GN model step is obtained by applying (9.29) and solving

$$
{ \bf K } ( { \bf m } ^ { k } ) ^ { T } { \bf K } ( { \bf m } ^ { k } ) \Delta { \bf m } = - { \bf K } ( { \bf m } ^ { k } ) ^ { T } \left[ \begin{array} { c } { { \bf G } ( { \bf m } ^ { k } ) - { \bf d } } \\ { { \alpha { \bf L } { \bf m } ^ { k } } } \end{array} \right] ,
$$

or, combining (10.5)and (10.6),by solving

$$
\left( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) \ \Delta \mathbf { m } = - \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } ( \mathbf { G } ( \mathbf { m } ^ { k } ) - \mathbf { d } ) - \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \mathbf { m } ^ { k } .
$$

Equation (1O.7) resembles the LM method (9.3O). Note, however, that $\alpha$ in (10.7) now appears in the objective function being minimized (1O.4) and thus introduces regularization. To further stabilize the iterations,as in the LM method,a variable $\lambda \mathbf { I }$ term could be added to the matrix term of the left-hand side of (1O.7) to steer iterative updates toward the direction of steepest descent. This will not be necessary if the explicit regularization of (10.7) sufficiently stabilizes the system of equations.

# Example 10.1

Consider a modified version of the cross-well tomography example from Exercise 4.3. We introduce nonlinearity by employing a more realistic forward model that incorporates ray-path bending due to seismic velocity changes. The two-dimensional velocity structure is parameterized using a 64-element matrix of uniformly spaced slownes nodes on an 8 by 8 grid spanning a $1 6 0 0 \mathrm { m }$ by $1 6 0 0 ~ \mathrm { m }$ region.

We apply an approximate ray-bending technique to estimate refracted ray paths within the slowness model and to estimate travel times and their partial derivatives with respect to the model parameters [167]. Figure 10.1 shows the true velocity model and a corresponding set of 64 ray paths. The true model consists of a background velocity of $2 . 9 \ \mathrm { k m / s }$ with large embedded fast $( + 1 0 \% )$ and slow $( - 1 5 \% )$ Gaussian-shaped anoma-lies. The data set consists of the 64 travel times between each pair of opposing sources and receivers with $N ( 0 , ( 0 . 0 0 1 \mathrm { s } ) ^ { 2 } )$ noise added.

Note that refracted ray paths tend to be“repelled” from low-velocity regions (dark shading) and are,conversely，“attracted’ to high-velocity regions (light shading) in accordance with Fermat’s least-time principle. In practice this effect makes low-velocity regions more difficult to resolve in such studies because they will be less well sampled by ray paths.

A discrete approximation of the two-dimensional Laplacian operator is used to regularize this problem. Iterative GN (1O.7） solutions were obtained for a range of 16 values of $\alpha$ ranging logarithmically from approximately 4.9 to 367. Figure 10.2 shows the suite of solutions after five iterations. An L-curve plot of seminorm versus data misfit is plotted in Figure 1O.3,along with the discrepancy principle value $\delta = 0 . 0 0 1 \cdot \sqrt { 6 4 } = 0 . 0 0 8$ Note that the two most lightly regularized solutions are out of their expected monotonically decreasing residual norm positions on the L-curve. This is because the linearization-based GN method is unable to accurately solve the corre-sponding poorly conditioned least squares systems (1O.7) in these cases. Such solutions could be improved by modifying the system of equations with an LM stabilizing term as described above. The solution best satisfying the discrepancy principle corresponds to $\alpha \approx 3 7$ (Figure 10.4).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/460b7aba91b04de8603d7db1d4e4a4246f6df1351002dd9905c390493685c492.jpg)  
Figure 10.2 Suite of GN (10.7),second-order regularized solutions, ranging from least (upper left) to most (lower right) regularized,and associated $\alpha$ values.The physical dimensions and gray scale are identical to those of Figures 10.1 and 10.4.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/781789a16de3c962ba03e2907bcc5bad8daf3b5afc64bcd7357f3c8750fbfb0e.jpg)  
Figure 10.3 L-curve and corresponding $\alpha$ values for the solutions of Figure 10.2.

Because we know the true model in this example, it is instructive to examine how well the regularized solutions of Figure 10.2 compare to it. Figure 10.5 shows the 2-norm model misfit as a function of $\alpha$ , and demonstrates that the discrepancy principle solution for this problem,and for this particular noise realization,is indeed close to the minimum in $\| \mathbf { m } - \mathbf { m } _ { \mathrm { { t r u e } } } \| _ { 2 }$ . Note that the solution shown in Figure 1O.4 exhibits resolution artifacts that are common in regularized solutions, such as streaking, side lobes,and amplitude under-recovery (see Example 10.3).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/11441e9155b73bf5596297aee18f580070af66784460d5179ea2d807643488fe.jpg)  
Figure 10.4 Best-solution velocity structure $( \mathsf { m } / \mathsf { s } )$ , $\alpha$ selected using the discrepancy principle, $\alpha \approx 3 7$   
Figure 10.5 Model misfit 2-norm as a function of regularization parameter $\alpha _ { \iota }$ ,with preferred model highlighted.

# 10.2.OCCAM'S INVERSION

Occam's inversion is a popular algorithm for nonlinear inversion introduced by Constable,Parker, and Constable [33]. The name refers to the 14th-century philosopher Willam of Ockham, who argued that simpler explanations should always be preferred to more complicated explanations.A similar statement occurs as rule 1 in Newton's “Rules for the Study of Natural Philosophy”[118]. This principle has become known as“Occam's razor."

Occam's inversion uses the discrepancy principle,and searches for the solution that minimizes $\| \mathbf { L m } \| _ { 2 }$ subject to the constraint $\| \mathbf { G } ( \mathbf { m } ) - \mathbf { d } \| _ { 2 } \leq \delta$ . The algorithm is straightforward to implement, requires only the nonlinear forward model $\mathbf { G } ( \mathbf { m } )$ and its Jacobian, and works well in practice.

We assume that our nonlinear inverse problem has been cast in the form of (10.1). The roughening matrix $\mathbf { L }$ can be I to implement zeroth-order Tikhonov regularization,or it can be a finite difference approximation of a first (4.27) or second (4.28) derivative for higher-order regularization. In practice, Occam's inversion is often used on two- or three-dimensional problems where $\mathbf { L }$ is a discrete approximation of the Laplacian operator.

As usual, we will assume that the measurement errors in $\mathbf { d }$ are independent and normally distributed. For convenience, we will also assume that the system of equations $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ has been scaled so that the standard deviations $\sigma _ { i }$ are equal.

The basic idea behind Occam's inversion is an iteratively applied local linearization Given a trial model $\mathbf { m } ^ { k }$ ,Taylor's theorem is applied to obtain the local approximation,

$$
\begin{array} { r } { \mathbf G ( \mathbf m ^ { k } + \Delta \mathbf m ) \approx \mathbf G ( \mathbf m ^ { k } ) + \mathbf J ( \mathbf m ^ { k } ) \Delta \mathbf m , } \end{array}
$$

where $\mathbf { J } ( \mathbf { m } ^ { k } )$ is the Jacobian,

$$
\mathbf { J } ( \mathbf { m } ^ { k } ) = \left[ \begin{array} { c c c } { \frac { \partial G _ { 1 } ( \mathbf { m } ^ { k } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial G _ { 1 } ( \mathbf { m } ^ { k } ) } { m _ { n } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial G _ { m } ( \mathbf { m } ^ { k } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial G _ { m } ( \mathbf { m } ^ { k } ) } { \partial m _ { n } } } \end{array} \right] .
$$

Using (10.8), the regularized least squares problem (10.3) becomes

$$
\begin{array} { r } { \operatorname* { m i n } \| \mathbf { G } ( \mathbf { m } ^ { k } ) + \mathbf { J } ( \mathbf { m } ^ { k } ) \Delta \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } ( \mathbf { m } ^ { k } + \Delta \mathbf { m } ) \| _ { 2 } ^ { 2 } , } \end{array}
$$

where the variable is $\Delta \mathbf { m }$ and $\mathbf { m } ^ { k }$ is constant. Reformulating this as a problem in which the variable is $\mathbf { m } ^ { k + 1 } = \mathbf { m } ^ { k } + \Delta \mathbf { m }$ , and letting

$$
\hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) = \mathbf { d } - \mathbf { G } ( \mathbf { m } ^ { k } ) + \mathbf { J } ( \mathbf { m } ^ { k } ) \mathbf { m } ^ { k } ,
$$

gives

$$
\operatorname* { m i n } \| \mathbf { J } ( \mathbf { m } ^ { k } ) ( \mathbf { m } ^ { k } + \Delta \mathbf { m } ) - ( \mathbf { d } - \mathbf { G } ( \mathbf { m } ^ { k } ) + \mathbf { J } ( \mathbf { m } ^ { k } ) \mathbf { m } ^ { k } ) \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } ( \mathbf { m } ^ { k } + \Delta \mathbf { m } ) \| _ { 2 } ^ { 2 }
$$

or

$$
\mathrm { m i n } \| \mathbf { J } ( \mathbf { m } ^ { k } ) \mathbf { m } ^ { k + 1 } - \hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } ( \mathbf { m } ^ { k + 1 } ) \| _ { 2 } ^ { 2 } .
$$

Because $\mathbf { J } ( \mathbf { m } ^ { k } )$ and $\hat { \mathbf { d } } ( \mathbf { m } ^ { k } )$ are constant within a given iteration, (1O.13) is in the form of a regularized linear least squares problem. If the system is of ful rank, the solution is given by

$$
\mathbf { m } ^ { k + 1 } = \mathbf { m } ^ { k } + \Delta \mathbf { m } = \left( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) ^ { - 1 } \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) .
$$

Note that this method is similar to the GN method applied to the regularized least squares problem (1O.3) (see Exercise 10.1). The difference is that in Occam's inversion the parameter $\alpha$ is dynamically adjusted so that the solution will not exceed the allowable misfit.At each iteration we pick the largest value of $\alpha$ that keeps the $\chi ^ { 2 }$ value of the solution from exceeding the bound on $\delta$ specified in (1O.1). If this is impossible, we instead pick the value of $\alpha$ that minimizes the $\chi ^ { 2 }$ value. At the end of the procedure, we should have a solution with $\chi ^ { 2 } = \delta ^ { 2 }$ . We can now state the algorithm.

# Algorithm 10.1 Occam's Inversion

Beginning with an initial solution $\mathbf { m } ^ { 0 }$ , repeat the following steps to compute a sequence of solutions $\mathbf { m } ^ { k }$ . Stop if and when the sequence converges to a solution with $\chi ^ { 2 } = \delta ^ { 2 }$

1. Calculate the Jacobian $\mathbf { J } ( \mathbf { m } ^ { k } )$ and the vector $\hat { \mathbf { d } } ( \mathbf { m } ^ { k } )$

2. Calculate updated models corresponding to a range of regularization parameter values, $\alpha$ ，

$$
\mathbf { m } ^ { k + 1 } = \left( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) ^ { - 1 } \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) .
$$

3. Choose the particular $\mathbf { m } ^ { k + 1 }$ with the largest value of $\alpha$ such that $\chi ^ { 2 } ( \mathbf { m } ^ { k + 1 } ) \leq \delta ^ { 2 }$ If no such value exists, then use the value of $\alpha$ that minimizes $\chi ^ { 2 } ( \mathbf { m } ^ { k + 1 } )$

4.Let $k = k + 1$

# Example 10.2

We will consider the problem of estimating subsurface electrical conductivities from above-ground electromagnetic induction measurements. The instrument used in this example is the Geonics EM-38 ground conductivity meter. A description of the instrument and the mathematical model of its response can be found in [69]. The mathematical model is complicated, but we will treat it as a black box,and concentrate on the inverse problem.

Measurements are taken at heights of O,10,20,30,40, 50,75,100,and $1 5 0 \mathrm { c m }$ above the surface,with the coils oriented in both the vertical and horizontal orientations. There are a total of 18 observations (Table 10.1). We will assume measurement standard deviations of $0 . 1 ~ \mathrm { m S / m }$

We discretize the subsurface electrical conductivity profile into 1O- and $2 0 \mathrm { - c m }$ thick layers and a semi-infinite layer below $2 ~ \mathrm { m }$ ， giving us 11 parameters to estimate. The forward problem function $\mathbf { G } ( \mathbf { m } )$ is available to us as a subroutine. Since we do not have simple formulas for $\mathbf { G } ( \mathbf { m } )$ , we cannot write down analytic expressions for the elements of the Jacobian. However, we can use finite difference approximations to estimate the necessary partial derivatives.

We first apply the LM method to estimate unregularized model parameters. After 50 iterations, the LM method produced the model shown in Figure 1O.6. The $\chi ^ { 2 }$ value for this model is 9.62 and there are $1 8 - 1 1 = 7$ degrees of freedom,so the model actually fits the data reasonably well. However, the least squares problem is very badly conditioned, with a condition number for $\mathbf { J } ^ { T } \mathbf { J }$ of approximately $2 \times 1 0 ^ { 1 7 }$ . Furthermore, the resulting model is unrealistic because it includes negative electrical conductivities and exhibits the high amplitudes and high-frequency oscillations that are characteristic of under-regularized solutions to inverse problems.

Table 10.1 Data for the EM-38 Example   

<table><tr><td>Height (cm) EMV (mS/m)</td></tr><tr><td>0 134.5 117.4</td></tr><tr><td>10 129.0 97.7</td></tr><tr><td>20 120.5 81.7</td></tr><tr><td>30 110.5 69.2</td></tr><tr><td>40 100.5 59.6</td></tr><tr><td>50 90.8 51.8</td></tr><tr><td>75 70.9 38.2</td></tr><tr><td>100 56.8 29.8</td></tr><tr><td>150 38.5 19.9</td></tr></table>

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/d14e166747026804831cf6592c173d886305751d84f50f449bd996d8fab05298.jpg)  
Figure 10.6 LM solution.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/427bb5de9e5bd10eff83d3b63a8b6fef1edf635817520480d557c5f03aa22182.jpg)  
Figure 10.7 Occam's inversion solution.

We next apply Occam's inversion with second-order regularization and a discrepancy principle value of $\delta = 0 . 1 \cdot { \sqrt { 1 8 } } \approx 0 . 4 2 4$ The resulting model is shown in Figure 10.7, and Figure 1O.8 shows the true model. The Occam's inversion method provides a fairly good reproduction of the true model.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/04a1e45649bf7916b075e1ef35e86c8f75761e531973b403747613e4268c2f85.jpg)  
Figure 10.8 True model.

# 10.3.MODEL RESOLUTION IN NONLINEAR INVERSE PROBLEMS

We introduced the concept of model resolution in Chapter 3 (see(3.63)) by expressing the generalized inverse solution for a linear problem as

$$
\mathbf { m } = \mathbf { R } _ { m } \mathbf { m } _ { \mathrm { t r u e } } = \mathbf { G } ^ { \dagger } \mathbf { G } \mathbf { m } _ { \mathrm { t r u e } }
$$

where $\mathbf { G }$ is a (forward problem) matrix that produces data from a model, $\mathbf { G } ^ { \dagger }$ is the generalized inverse matrix used to recover a model from data,and $\mathbf { m }$ and $\mathbf { m _ { \mathrm { t r u e } } }$ are the recovered and true models, respectively. In a linear problem, the action of mapping a model to data and then back to a recovered model can be completely characterized by the model resolution matrix $\mathbf { R } _ { m } = \mathbf { G } ^ { \dagger } \mathbf { G }$ in (10.16). In Chapter 4 we saw that this concept could easily be extended to Tikhonov regularization (4.2O), by substituting the corresponding Tikhonov inverse matrix, $\mathbf { G } ^ { \sharp }$ ,for $\mathbf { G } ^ { \dagger }$ in (10.16).

We can recast (10.16) for nonlinear problems as

$$
\mathbf { m } = G ^ { - 1 } ( G ( \mathbf { m } _ { \mathrm { t r u e } } ) )
$$

where $G ^ { - 1 }$ and $G$ are inverse and forward operators, respectively. However, the combined action of the forward and inverse operations is not representable as a matrix, such as $\mathbf { R } _ { m }$ in (1O.17),because the forward operator is a nonlinear function or algorithm, and the inverse operator is typically realized with an iterative method based on stepwise linearization, such as GN or Occam's inversion.Furthermore,model resolution for a nonlinear inversion will not only depend on the physics, model parameterization, and data collection specifics,as was the case for linear problems, but may furthermore depend on the choice of starting model used in the solution algorithm, chosen convergence criteria,and possibly on the existence of multiple equally good solutions. Finally, as with linear methods, nonlinear model resolution wil depend on the level and nature of the imposed regularization.

Because of these complexities, nonlinear resolution is typically analyzed using resolution tests. In seismic tomography, for example, it is common to evaluate the effects of nonideal resolution by generating noise-free synthetic data from a spike, checkerboard,or other test model using an identical source and receiver geometry as for the actual data in the problem of interest.A model is then recovered using the identical inverse methodology as was used for the actual data,and is compared to the test model to evaluate inversion artifacts. If there are specific features of the true model that will affect the resolution,such as a known strong velocity gradient with depth in seismic problems that significantly affects the curvature of the ray paths, those features should also be incorporated into the resolution test model. Because the problem is nonlinear, resolution analysis results will also potentially be dependent on test model amplitudes. A second resolution analysis strategy, sometimes referred to as a “squeeze” test, restricts the freedom of the model in regions that are suspected to be unnecessary or marginal for achieving an acceptable fit to the data. One example would be to modify the regularization constraints to strongly penalize model variations in the deeper part of a tomographic model to assess whether an acceptable data fit can still be achieved when structure is predominantly restricted to shallower depths.

# Example 10.3

Revisiting Example 1O.1,we calculate noise-free synthetic data for a checkerboard velocity structure,using an identical starting model and ray-path end points. The checkerboard model (Figure 10.9) consists of an 8 by 8 node $2 . 9 ~ \mathrm { k m / s }$ background model with alternating $10 \%$ variations for the 36 interior blocks. Inverting these data using the identical methodology as in Example 1O.1 for the same regularization con-straints and range of regularization parameters, we obtain the suite of models shown in Figure 1O.1O.For lower levels of regularization, the checkerboard is more apparent,while for higher levels, the horizontally varying velocity structure is substantially smoothed out. For the level of regularization chosen from the discrepancy principle for Example 10.1, $\alpha \approx 3 7$ ，we note substantial smearing that makes it diffcult to discern the full checkerboard pattern, indicating that structural variations of this character and spatial scale will be dificult to recover in some parts of the model without additional data. If we did not know the true model in Example 10.1, this test would helpfully show that we would expect significant horizontal smearing for the inversion result shown in Figure 1O.4,and that the true model anomalies are thus not necessarily horizontally elongated.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/7a339c5f271d694fd5809d6ec91d89a2b7989c2d839aaeb915b5fbc56ae590f2.jpg)  
Figure 10.9 Checkerboard test model and ray paths for the cross-well tomography problem of Example 10.1.   
Figure 10.10 Suite of recovered models for a range of regularization parameter values (same as in Figure 10.2) for the checkerboard test model of Figure 10.9.

# 10.4.EXERCISES

1. Show that, for a given value of $\alpha$ , the GN (10.7) and Occam's inversion model (10.14) update steps are mathematically equivalent.

2.Recal Example 1.5,in which we had gravity anomaly observations above a density perturbation of variable depth $m ( x )$ , and fixed density $\Delta \rho$ . Use Occam's inversion to solve an instance of this inverse problem. Consider a gravity anomaly along a $1 \mathrm { - k m }$ section,with observations taken every $5 0 \textrm { m }$ ，and density perturbation of $\Delta \rho =$ $2 0 0 ~ \mathrm { k g } / \mathrm { m } ^ { 3 }$ $( 0 . 2 ~ \mathrm { g } / \mathrm { c m } ^ { 3 } )$ . The perturbation is expected to be at a depth of roughly $2 0 0 ~ \mathrm { m }$

The MATLAB data file gravprob.mat contains a vector $\mathbf { x }$ of observation locations. Use the same coordinates for your discretization of the model. The vector obs contains the actual observations.Assume that the observations are accurate to about $1 . 0 \times 1 0 ^ { - 1 2 }$

a.Derive a formula for the elements of the Jacobian.   
b. Write MATLAB routines to compute the model predictions and the Jacobian for this problem.   
c.Use the supplied implementation of Occam's inversion from Example 10.2 to solve the inverse problem with second-order regularization.   
d.Discuss your results. What features in the inverse solution appear to be real? What is the resolution of your solution? Were there any difficulties with local minimum points?   
e. What would happen if the true density perturbation was instead at a depth of about $1 0 0 0 ~ \mathrm { { m } ? }$

3.Apply the GN method with explicit regularization to the EM inversion problem by modifying the MATLAB code from Example 10.2. Compare your solution with the solution obtained by Occam's inversion. Which method required more computational effort?

4. Apply Occam's inversion to a cross-well, bent-ray tomography problem with identical geometry to Example 1O.1. Use the example subroutine getj.m to forward model the travel times,calculate the Jacobian,and implement second-order regularization. Travel-time data and subroutine control parameters are contained in the MATLAB data file benddata.mat. Start with the uniform $2 9 0 0 \mathrm { m / s }$ velocity 8 by 8 node initial velocity model in benddata.mat,and assume independent and normally distributed data errors with $\sigma = 0 . 0 0 1 ~ \mathrm { m s }$

Hint: A search range of $\alpha ^ { 2 }$ between 10 and $1 0 ^ { 5 }$ is appropriate for this problem. MATLAB code for generating a second-order roughening matrix that approximates a two-dimensional Laplacian operator can be found in makerough.m.

# 10.5.NOTES AND FURTHER READING

In inverse problems with a large number of parameters, the most difficult computational problem is often computing derivatives of $\mathbf { G } ( \mathbf { m } )$ with respect to the model parameters, often referred to as Frechet derivatives [1O7]. Computation of analytic formulas is commonly impractical. Finite difference estimates require computational effort, which increases with the number of parameters and may become impractical for large problems. A promising technique for calculating Frechet derivatives is the adjoint approach [46, 154,165],which is likely to see increasing use in large problems as forward modeling capabilities advance. An alternative approach involves using the discretized differential equation as a set of constraints to be added to the nonlinear least squares problem [15].

For large-scale problems, it may be impractical to use direct factorization to solve the systems of equations (10.7) or (10.14) involved in computing the GN or Occam step. One approach in this case is to use an iterative method such as conjugate gradients to solve the linear systems of equations [58]. The conjugate gradient method can also be extended to minimize the nonlinear objective function directly [58, 142].

# Bayesian Methods

# Synopsis

Following a review of the classical least squares approach to solving inverse problems, we introduce the Bayesian approach,which treats the model as a random variable with a probability distribution that we seek to estimate.A prior distribution for the model parameters is combined with the data to produce a posterior distribution for the model parameters. In special cases, the Bayesian approach produces solutions that are equivalent to the least squares, maximum likelihood,and Tikhonov regularization solutions. Several examples of the Bayesian approach are presented. Markov Chain Monte Carlo methods for sampling from the posterior distribution are presented and demonstrated.

# 11.1.REVIEW OF THE CLASSICAL APPROACH

In the classical approach to parameter estimation and inverse problems with discrete data and models, we begin with a mathematical model of the form $\mathbf { G m } = \mathbf { d }$ in the linear case or $G ( \mathbf { m } ) = \mathbf { d }$ in the nonlinear case. We assume that there exists a true model, $\mathbf { m } _ { \mathrm { t r u e } }$ ， and a true data set, ${ \bf d } _ { \mathrm { t r u e } }$ ，such that $\mathbf { G m } _ { \mathrm { t r u e } } = \mathbf { d } _ { \mathrm { t r u e } }$ . We acquire an actual data set, $\mathbf { d } .$ which is generally the sum of ${ \bf d } _ { \mathrm { t r u e } }$ and measurement noise. Our goal is to recover $\mathbf { m _ { \mathrm { t r u e } } }$ from the noisy data.

For well-conditioned linear problems,under the assumption of independent and normally distributed data errors, the theory is well developed. In Chapter 2 it was shown that the maximum likelihood principle leads to the least squares solution, which is found by minimizing the 2-norm of the residual, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ . Since there is noise in the data,we should expect some misfit between the data predictions of the forward model and the data,so that observed values of the square of the 2-norm of the inverse standard deviation-weighted residual, $\chi _ { \mathrm { o b s } } ^ { 2 }$ ，will not typically be zero. We saw that the $\chi ^ { 2 }$ distribution can be used to test the goodness-of-fit of a least squares solution. We showed that the least squares solution, ${ \bf { m } } _ { L _ { 2 } }$ , is an unbiased estimate of $\mathbf { m _ { \mathrm { t r u e } } }$ . We were also able to compute a covariance matrix for the estimated parameters

$$
\mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } { \bf G } ^ { T } \mathrm { C o v } ( { \bf d } ) { \bf G } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 }
$$

to compute confidence intervals for and correlations between the estimated parameters.

This approach works very wellfor linear regression problems where the least squares problem is well-conditioned. We found, however, that in many cases the least squares problem is not well-conditioned. In such situations, the set of solutions that adequately fits the data is large and diverse,and commonly contains physically unreasonable models.

In Chapters 4 through 8,we discussed a number of approaches to regularizing the least squares problem. These approaches pick a single “best” solution out of those that adequately fit the data, based on a preference for what sort of model features constitute a good solution. Zeroth-order Tikhonov regularization selects the model that minimizes the model 2-norm $\| \mathbf { m } \| _ { 2 }$ subject to the residual norm constraint, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } < \delta$ ， while higher-order Tikhonov regularization selects the model that minimizes a model seminorm $\| \mathbf { L m } \| _ { 2 }$ subject to $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } < \delta$ . We introduced $L _ { 1 }$ regularization and the related technique of total variation regularization which are now widely used in compressive sensing.

For relatively small linear problems， straightforward, insightful,and robust computation of regularized solutions can be performed with the help of singular value decomposition (SVD). For large sparse linear problems, iterative methods such as conjugate gradient least squares (CGLS) or LSQR are widely used.

For nonlinear problems,as discussed in Chapters 9 and 1O, the Gauss-Newton, Levenberg-Marquardt,or Occam's inversion methods can be used to find local minima of the nonlinear least squares problem. We showed how approximate confidence intervals for the fitted parameters can be obtained by linearizing the nonlinear model around the best fit parameters. As in linear inverse problems, the nonlinear least squares problem can be badly conditioned in which case regularization may be needed to obtain a stable solution.

Unfortunately nonlinear problems may have a large number of local minimum solutions,and finding the global minimum can be diffcult. Furthermore, if there are several local minimum solutions with acceptable data fits, then it may be difficult to select a single“best” solution.

How can we more generally justify selecting one solution from the set of models that adequately fit the data? One justification is Occam's razor, which is the philosophy that when we have several different hypotheses to consider,we should select the simplest. Solutions selected by regularization are in some sense the simplest models that fit the data. However, this approach is not by itself entirely satisfactory because different choices of the regularization term used in obtaining regularized solutions can result in very different models,and the specific choice of regularization may be subjective.

Recall from Chapter 4 (e.g., Example 4.3) that once we have regularized a least squares problem,we lose the ability to obtain statistically useful confidence intervals for the parameters because regularization introduces bias. In particular, the expected value of the regularized solution is not generally equal to the true model. In practice this regularization bias is often much more significant than the effect of noise in the data.Bounds on the error in Tikhonov regularized solution error were discussed in Section 4.8, but these estimates require knowledge of the true model that is typically not available in practice.

# 11.2.THE BAYESIAN APPROACH

The Bayesian approach is named after Thomas Bayes,an 18th-century pioneer in probability theory. The methodology is based on philosophically different ideas than we have considered so far.However, as we wil see, it frequently results in similar solutions.

The most fundamental difference between the classical and Bayesian approaches is in the conceptualization of the solution. In the classical approach, there is a specifc but unknown model $\mathbf { m _ { \mathrm { t r u e } } }$ that we would like to uncover. In the Bayesian approach the model is not deterministic, but is rather a random variable,and the solution takes the form of a probability distribution for the model parameters called the posterior distribution. Once we have this probability distribution, we can use it to answer probabilistic questions about the model, such as “What is the probability that $m 5$ is less than $1 ? ^ { \dag }$ In the classical approach such questions do not make sense, since the true model that we seek is not a random variable.

A second very important difference between the classical and Bayesian approaches is that the Bayesian approach naturally incorporates prior information about the solution, ranging from hard additional constraints to experience-based intuition. This information is expressed mathematically as a prior distribution for the model. Once data have been collected, they are combined with the prior distribution using Bayes' theorem (B.54) to produce the desired posterior distribution for the model parameters.

If no other information is available, then under the principle of indifference, we may alternatively pick a prior distribution where all model parameter values have equal likelihood. Such a prior distribution is said to be uninformative.

It should be pointed out that, in the common case where the model parameters are contained in the range $( - \infty , \infty )$ , the uninformative prior is not a proper probability distribution. This is because a probability density function $f ( x )$ does not exist which satisfies (B.4) so that

$$
\intop _ { - \infty } ^ { \infty } f ( x ) \ d x = 1
$$

and $f ( x )$ is constant.In practice, the use of this improper prior distribution in Bayesian methods can nevertheless be justified because the resulting posterior distribution for the model is a proper distribution.

One of the main objections to the Bayesian approach is that the method is “unscientific” because it allows the analyst to incorporate subjective judgments into the model that are not solely based on the data.Proponents of the approach rejoin that there are also subjective aspects to the classical approach embodied in the choice of regularization biases,and furthermore, that one is free to choose an uninformative prior distribution.

Here, we denote the prior distribution by $p ( \mathbf { m } )$ , and assume that we can compute the conditional probability distribution, $f ( \mathbf { d } | \mathbf { m } )$ , that, given a particular model, correspond-ing data,d, will be observed. Given a prior distribution,we then seek the conditional (posterior) distribution of the model parameter(s) given the data. We will denote this posterior probability distribution for the model parameters by $q ( \mathbf { m } | \mathbf { d } )$ .Bayes’theorem relates the prior and posterior distributions in a way that makes the computation of $q ( \mathbf { m } | \mathbf { d } )$ possible,and can be stated as follows.

# Theorem 11.1

$$
q ( \mathbf { m } | \mathbf { d } ) = \frac { f ( \mathbf { d } | \mathbf { m } ) _ { P } ( \mathbf { m } ) } { c }
$$

where

$$
c = \int _ { \mathrm { { a l l } } \mathrm { { m o d e l s } } } \ f ( \mathbf { d } | \mathbf { m } ) p ( \mathbf { m } ) d \mathbf { m } .
$$

Note that the constant $c$ in (11.3） simply normalizes the conditional distribution $q ( \mathbf { m } | \mathbf { d } )$ so that its integral in model space is one.

For some purposes, knowing the normalization constant, $c$ ，is not necessry. For example, we can compare two models $\hat { \mathbf { m } }$ and $\bar { \bf m }$ by computing the likelihood ratio:

$$
\frac { q ( \hat { \mathbf { m } } | \mathbf { d } ) } { q ( \bar { \mathbf { m } } | \mathbf { d } ) } = \frac { f ( \mathbf { d } | \hat { \mathbf { m } } ) p ( \hat { \mathbf { m } } ) } { f ( \mathbf { d } | \bar { \mathbf { m } } ) p ( \bar { \mathbf { m } } ) } .
$$

A very small likelihood ratio would indicate that the model $\bar { \bf m }$ is far more likely than the model $\hat { \mathbf { m } }$ Because $c$ is not always needed, (11.3) is often written as a statement of proportionality,

$$
q ( \mathbf { m } | \mathbf { d } ) \propto f ( \mathbf { d } | \mathbf { m } ) p ( \mathbf { m } ) .
$$

However, there are many other situations in which knowing $c$ in (11.3) is required. In particular, $c$ is required to compute any posterior probabilities and to compute the expected value and variance of the posterior distribution.

It is important to re-emphasize that the probability distribution $q ( \mathbf { m } | \mathbf { d } )$ does not provide a single model that we can consider to be the“answer.” However, in cases where we want to single out a representative model, it may be appropriate to identify the one corresponding to the largest value of $q ( \mathbf { m } | \mathbf { d } )$ . This model is referred to as the maximum a posteriori (MAP) model. Another possibility is to select the mean of the posterior distribution. In situations where the posterior distribution is normal, the MAP and posterior mean models will be identical.

In general, the computation of a posterior distribution using (11.3) can be difficult. The chief difficulty lies in evaluating the integral in (11.4). This integral often has very high dimensionality, and numerical integration techniques may thus be computationally daunting.

Fortunately, there are a number of useful special cases in which the computation of the posterior distribution is greatly simplified. One simplification occurs when the prior distribution $p ( \mathbf { m } )$ is uninformative, in which case (11.6) simplifies to

$$
q ( \mathbf { m } | \mathbf { d } ) \propto f ( \mathbf { d } | \mathbf { m } ) ,
$$

and the posterior distribution is precisely the likelihood function, $L ( \mathbf { m } | \mathbf { d } )$ . Under the maximum likelihood principle,we would select the model $\mathbf { m } _ { \mathrm { M L } }$ that maximizes $L ( \mathbf { m } | \mathbf { d } )$ ,which is the MAP model.

A further simplification occurs when data noise elements are independent and normally distributed with standard deviation $\sigma$ . Because the data errors are independent, we can write the likelihood function as

$$
L ( \mathbf { m } | \mathbf { d } ) = f ( \mathbf { d } | \mathbf { m } ) = f ( d _ { 1 } | \mathbf { m } ) \cdot f ( d _ { 2 } | \mathbf { m } ) \cdot \cdot \cdot f ( d _ { n } | \mathbf { m } ) .
$$

If the data points $d _ { i }$ are normally distributed with expected values given by the (linear or nonlinear) operation $( G ( \mathbf { m } ) ) _ { i }$ ,and each has standard deviation $\sigma$ , we can write

$$
f ( d _ { i } | { \bf m } ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } e ^ { - \frac { ( ( G ( { \bf m } ) ) _ { i } - d _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } }
$$

and

$$
L ( \mathbf { m } | \mathbf { d } ) = \left( \frac { 1 } { \sigma \sqrt { 2 \pi } } \right) ^ { m } e ^ { - \sum _ { i = 1 } ^ { m } \frac { ( ( G ( \mathbf { m } ) ) _ { i } - d _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } .
$$

We can maximize (11.1O) by maximizing the exponent or equivalently minimizing the negative of the exponent.

$$
\operatorname* { m i n } \ \sum _ { i = 1 } ^ { m } \frac { ( ( G ( \mathbf { m } ) ) _ { i } - d _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } .
$$

This is a weighted least squares problem. Thus we have shown that when we have independent and normally distributed measurement errors and we use an uninformative prior, the MAP solution is the least squares solution.

# Example 11.1

Consider a very simple parameter estimation problem where we perform repeated weighings of a microscopic object to determine its mass in micrograms. The measurement erors are normally distributed with zero mean and standard deviation $\sigma = 1 ~ { \mu \mathrm { g } }$ Our goal is to estimate the mass of the object.

For the specified normally distributed and zero mean measurement error, the probability density function for a measurement $d$ given $m$ is

$$
f ( d | m ) = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - d ) ^ { 2 } / 2 } .
$$

Suppose that we weigh the mass once and obtain a measurement of $d _ { 1 } = 1 0 . 3 ~ \mu \mathrm { g }$ What do we now know about m? For an uninformative prior, (11.7) gives

$$
q ( m | d _ { 1 } = 1 0 . 3 ) \propto f ( 1 0 . 3 | m ) = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 3 ) ^ { 2 } / 2 } .
$$

Because (11.13) is itself a normal probability distribution, the constant of proportionality in (11.3) is 1,and the posterior distribution for the mass in micrograms (Figure 11.1) is therefore

$$
q ( m | d _ { 1 } = 1 0 . 3 ) = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 3 ) ^ { 2 } / 2 } .
$$

Next, suppose that we obtain a second statistically independent measurement of $d _ { 2 } =$ $1 0 . 1 ~ \mu \mathrm { g }$ . We can then use the distribution (11.14) estimated from the first measurement

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/678047192b58381d1c3d2a8c78b36386dc0ccda4caa119a499685c0d57704ed9.jpg)  
Figure 11.1 Posterior distribution $q ( m | d _ { 1 } = 1 0 . 3 \mu \mathrm { g } )$ , uninformative prior.

as an informative prior distribution to compute a revised posterior distribution:

$$
\begin{array} { c } { { q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) \propto f ( d _ { 2 } = 1 0 . 1 | m ) q ( m | d _ { 1 } = 1 0 . 3 ) } } \\ { { { } } } \\ { { { } = { \displaystyle { \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 1 ) ^ { 2 } / 2 } \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 3 ) ^ { 2 } / 2 } } } . } } \end{array}
$$

Combining the exponents and absorbing the $1 / \sqrt { 2 \pi }$ factors into the constant of proportionality gives

$$
q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) \propto e ^ { - ( ( m - 1 0 . 3 ) ^ { 2 } + ( m - 1 0 . 1 ) ^ { 2 } ) / 2 } .
$$

Finally, we can simplify the exponent by combining terms and completing the square to obtain

$$
( m - 1 0 . 3 ) ^ { 2 } + ( m - 1 0 . 1 ) ^ { 2 } = 2 ( m - 1 0 . 2 ) ^ { 2 } + 0 . 0 2 .
$$

Thus,

$$
q ( m | d _ { 1 } = 1 0 . 3 ~ \mu \mathrm { g } , ~ d _ { 2 } = 1 0 . 1 ) \propto e ^ { - ( 2 ( m - 1 0 . 2 ) ^ { 2 } + 0 . 0 2 ) / 2 } .
$$

The constant $e ^ { - 0 . 0 2 / 2 }$ caneabsorbeditothestantofproportioalitygiving

$$
q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) \propto e ^ { - ( 1 0 . 2 - m ) ^ { 2 } } .
$$

Normalizing (11.19) gives a normal posterior distribution

$$
q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) = \frac { 1 } { ( 1 / \sqrt { 2 } ) \sqrt { 2 \pi } } e ^ { - \frac { ( 1 0 . 2 - m ) ^ { 2 } } { 2 ( 1 / \sqrt { 2 } ) ^ { 2 } } } ,
$$

with mean $1 0 . 2 ~ { \mu \mathrm { g } }$ and $\sigma = 1 / \sqrt { 2 } ~ \mu \mathrm { g }$ (Figure 11.2). Since we used an uninformative prior and the measurement errors were independent and normally distributed, the MAP solution is precisely the least squares solution for this problem.

It is notable in the second part of this example that we started with a normal prior distribution,accommodated normally distributed data,and obtained a normal posterior distribution (see (11.2O)). In general we should not expect that the prior and posterior distributions will both be well-known distributions whose properties are well known. A prior distribution associated with a simple posterior distribution in this way is called a conjugate prior. There are other families of conjugate distributions for various parameter estimation problems, but in general this is unusual [51].

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/9ff696572019161e2a7e22d2c7f961a029e72db348ed462019efca38647ac9c9.jpg)  
Figure 11.2 Posterior distribution $q ( m | d _ { 1 } = 1 0 . 3 \mu \mathrm { g }$ $d _ { 2 } = 1 0 . 1 \mu \mathrm { g } ,$ .

# 11.3.THE MULTIVARIATE NORMAL CASE

The result shown in Example 11.1 in which a normal prior distribution and normally distributed data lead to a normal posterior distribution can be readily extended to problems with many model parameters. We next examine the problem of determining the posterior distribution for a linear model, multivariate normal (MVN) distributed data errors,and an MVN prior distribution.

Let $\mathbf { d } _ { \mathrm { { o b s } } }$ be the observed data, $\mathbf { C } _ { D }$ be the corresponding data covariance matrix, $\mathbf { m } _ { \mathrm { p r i o r } }$ be the mean of the prior distribution, and $\mathbf { C } _ { M }$ be the covariance matrix for the prior distribution. The prior distribution is thus, by (B.62),

$$
p ( \mathbf { m } ) \propto e ^ { - \frac { 1 } { 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) } ,
$$

and the conditional distribution of the data, given $\mathbf { m }$ ,is

$$
f ( \mathbf { d } | \mathbf { m } ) \propto e ^ { - \frac { 1 } { 2 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) } .
$$

Thus, (11.6) gives

$$
q ( \mathbf { m } | \mathbf { d } ) \propto e ^ { - \frac { 1 } { 2 } ( ( \mathbf { G } \mathbf { m } - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) + ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ) } .
$$

Tarantola [155] showed that this can be simplified to

$$
q ( \mathbf { m } | \mathbf { d } ) \propto e ^ { - \frac { 1 } { 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { M A P } } ) ^ { T } \mathbf { C } _ { M ^ { \prime } } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { M A P } } ) } ,
$$

where ${ \bf m } _ { \mathrm { M A P } }$ is the MAP solution, and

$$
\mathbf { C } _ { M ^ { \prime } } = ( \mathbf { G } ^ { T } \mathbf { C } _ { D } ^ { - 1 } \mathbf { G } + \mathbf { C } _ { M } ^ { - 1 } ) ^ { - 1 } .
$$

The MAP solution can be found by maximizing the exponent in (1.23),or equivalently by minimizing its negative:

$$
\mathrm { m i n } ( \mathbf { G m - d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G m - d } ) + ( \mathbf { m - m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m - m } _ { \mathrm { p r i o r } } ) .
$$

The key to minimizing (11.26) is to rewrite it in terms of the matrix square roots of $\mathbf { C } _ { M } ^ { - 1 }$ and $\mathbf { C } _ { D } ^ { - 1 }$ . Notethateveryovaranematrixispositiedefiiteandhsqe positive definite matrix square root,which may be calculated in MATLAB using the sqrtm routine. This minimization problem can then be reformulated as

$$
\begin{array} { r l } & { \operatorname* { m i n } \ ( \mathbf { C } _ { D } ^ { - 1 / 2 } ( \mathbf { G m } - \mathbf { d } ) ) ^ { T } ( \mathbf { C } _ { D } ^ { - 1 / 2 } ( \mathbf { G m } - \mathbf { d } ) ) \ + } \\ & { \qquad ( \mathbf { C } _ { M } ^ { - 1 / 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ) ^ { T } ( \mathbf { C } _ { M } ^ { - 1 / 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ) , } \end{array}
$$

or as the standard least squares problem,

$$
\mathrm { m i n } \left\| \left[ \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } .
$$

Examining the right-hand terms in (11.28), note that

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { d } ) = \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { C } _ { D } ( \mathbf { C } _ { D } ^ { - 1 / 2 } ) ^ { T } = \mathbf { I } . } \end{array}
$$

The multiplication of $\mathbf { C } _ { D } ^ { - 1 / 2 }$ times $\mathbf { d }$ in (11.28)cnusbceptalizdsdata transformation that both makes the resulting elements independent and normalizes the staddeve $\bar { \mathbf { C } } _ { M } ^ { - 1 / 2 }$ has te sae efet.

An interesting limiting case is where the prior distribution provides essentially no information. Consider an MVN prior distribution with a covariance matrix $\mathbf { C } _ { M } = \alpha ^ { 2 } \mathbf { I } .$ in the limit where $\alpha$ is extremely large.In this case,the diagonal elements of $\mathbf { C } _ { M } ^ { - 1 }$ will be extremely small, and the posterior covariance matrix (11.25) will be well-approximated by

$$
\mathbf { C } _ { M ^ { \prime } } \approx ( \mathbf { G } ^ { T } \operatorname { C o v } ( \mathbf { d } ) ^ { - 1 } \mathbf { \Sigma } \mathbf { G } ) ^ { - 1 } .
$$

If the data covariance matrix is $\mathbf { C } _ { D } = \sigma ^ { 2 } \mathbf { I }$ ,then

$$
\mathbf { C } _ { M ^ { \prime } } \approx \sigma ^ { 2 } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } ,
$$

which is precisely the covariance matrix for the least squares model parameters in (11.1). Furthermore, when we solve (11.28) to obtain the MAP solution, we find that it simplifies to the least squares problem of minimizing $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 }$ . Thus,under the common assumption of normally distributed and independent data errors with constant variance, a very broad prior distribution leads to a MAP solution that is the unregularized least squares solution.

It is also worthwhile to consider what happens in the special case where $\mathbf { C } _ { D } = \sigma ^ { 2 } \mathbf { I }$ and $\mathbf { C } _ { M } = \alpha ^ { 2 } \mathbf { I }$ . In this case the corresponding matrix square roots are also proportional to identity matrices,and (11.28) simplifies to

$$
\operatorname* { m i n } \ ( 1 / \sigma ) ^ { 2 } \| ( \mathbf { G m } - \mathbf { d } ) \| _ { 2 } ^ { 2 } + ( 1 / \alpha ) ^ { 2 } \| \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } \| _ { 2 } ^ { 2 } ,
$$

which is a modified optimization problem for zeroth-order Tikhonov regularization (4.4),where the 2-norm regularization term is evaluated relative to $\mathbf { m } _ { \mathrm { p r i o r } }$ ，and the equivalent Tikhonov regularization parameter is $\sigma / \alpha$ . Thus,the MAP solution obtained by using a prior with independent and normally distributed model parameters is precisely the zeroth-order Tikhonov regularized solution obtained by solving (11.32). However, this does not mean that the Bayesian approach is entirely equivalent to Tikhonov regularization,because the Bayesian solution is a probability distribution, whereas the Tikhonov solution is a single model from that distribution.

Once we have obtained the posterior distribution, it is straightforward to generate corresponding model realizations. We may wish to do this to assess likely or unlikely model features. Following the procedure outlined in Example B.1O,we compute the Cholesky factorization of the posterior distribution covariance matrix,

$$
{ \bf C } _ { M ^ { \prime } } = { \bf R } ^ { T } { \bf R } ,
$$

and generate a random solution

$$
\mathbf { m } = \mathbf { R } ^ { T } \mathbf { s } + \mathbf { m } _ { \mathrm { M A P } } ,
$$

where the vector s consists of independent and normally distributed random numbers with a zero mean and a unit standard deviation.

# Example 11.2

We consider Bayesian solutions to the Shaw problem that was previously considered in Examples 3.3, 4.1, 4.2, 4.3, and 4.8.

We first use a relatively uninformative MVN prior distribution with mean 0.5, standard deviation O.5,and zero covariances，so that $\mathbf { C } _ { M } = 0 . 2 5 \textbf { I }$ 、As in the previous examples, the measurement noise has standard deviation $1 . 0 \times 1 0 ^ { - 6 }$ ,so that $\mathbf { C } _ { D } =$ $1 . 0 \times 1 0 ^ { - 1 2 }$ 1. Solving (11.28) produces the mMAP solution shown in Figure 11.3. Figure 11.4 shows this same solution with error bars. These error bars are not classical $9 5 \%$ confidence intervals (e.g., Figure 4.9). Rather, they are $9 5 \%$ probability intervals calculated from the MVN posterior distribution,so that there is $9 5 \%$ probability that each model parameter lies within the corresponding symmetric interval around mMAP.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/8949d80b3a50096246990a1034ac0ee92bda979ccc71211e36ca7bc158d706c8.jpg)  
Figure 11.3 The MAP solution and the true model for the Shaw example using an MVN priol distribution with mean O 5,standard deviation O 5,and zero covariance.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/26a1bd544c45de3badd5ead14cd0fe267396171828f7b43ca79723560e3efd5b.jpg)  
Figure11.4 The MAP solution of Figure 11.3, with $9 5 \%$ probability intervals.

Figure 11.5 shows a random solution generated from the posterior distribution. This solution varies considerably from the true model,and demonstrates great uncertainty in the inverse solution, consistent with the large $9 5 \%$ probability intervals in Figure 11.3. The roughness of this solution realization is a consequence of the fact that the prior distribution $\mathbf { C } _ { M }$ had zero covariances,so model realizations from the posterior distribution have no preference for smoothness.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/ed18c6b2df84c0c4eac18372ba47df21c9cd09d98b29a6c5a1deb9497031ceac.jpg)  
Figure 11.5 A model realization for the Shaw example using an MVN prior distribution with mean 0.5, standard deviation O 5,and zero covariance.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/cf6eeb76d23c848063dd66e52da660a236251ca865442e8931f7ee379375060a.jpg)  
Figure 11.6 A more restrictive zero covariance prior distribution for the Shaw problem with $9 5 \%$ probability intervals.

Next,consider a more restrictive prior distribution. Suppose we have reason to believe that the largest amplitudes in the solution should be near the center of the model. We thus choose the bell-shaped zero-covariance prior distribution depicted in Figure 11.6. Figures 11.7 and 11.8 show the resulting MAP model and its probability intervals for this case. The solution recovery is, not surprisingly, improved by our more restrictive prior model given that the true model is highly restricted and is thus consistent with the prior distribution (Figure 11.3).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/bde714b7b44a4a57989ff6df90d070760a8ca1f067ad29e47696df963146e008.jpg)  
Figure 11.7 The MAP solution for the Shaw example using the prior distribution shown in Figure 11.6.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/5716c58eae6861a370170d0a29e0d3cf0ddb946703bac53eaf4eac81548307f3.jpg)  
Figure 11.8 The MAP solution of Figure 11.7 with probability intervals.

These results illustrate a principal issue with applying the Bayesian approach to poorly conditioned problems.To obtain a tight posterior distribution in such cases,we will have to make strong prior assumptions. Conversely, if such assumptions are not made, then we cannot recover the true model features well. This situation is analogous to that of Tikhonov regularization,which must also impose strong and consistent model bias to produce “good” solutions and must also make strong model assumptions to estimate solution error bounds (Section 4.8).

In the previous example,we applied a prior that preferentially concentrated the model structure in a particular region (the center) by imposing a zero prior with small standard deviations near the model edges. Because this prior distribution had zero covariances,resulting model realizations were rough. Prior distributions can be readily designed to enforce smoothness constraints on realizations from the posterior distribution by specifying a nondiagonal prior covariance matrix. A straightforward way to accomplish this for a 1-dimensional model is to construct a correlation matrix with columns

$$
\begin{array} { r } { { \bf R } _ { i , . } = \mathrm { s h i f t } ( a _ { j } , i ) , } \end{array}
$$

where $a _ { j }$ is the desired sequence of parameter correlations,with a zero lag correlation of 1. The shift operator shifts the sequence (truncating as necessary) so that the zero-lag (unit) maximum of the correlation sequence is centered on element $i .$ ,and hence on the diagonal of R. Suitable sequences $a _ { i }$ that ensure the positive definiteness of $\mathbf { R }$ can be constructed using autocorrelation (e.g., using the MATLAB xcorr function). Here, we use the autocorrelation of a triangle function, which produces a cubic approximation to a Gaussian function. Given the correlation matrix, $\mathbf { R }$ ,a corresponding prior distribution covariance matrix with uniform parameter variances, $\sigma _ { M }$ ,can then be constructed as

$$
\mathbf { C } _ { M } = \sigma _ { M } ^ { 2 } \mathbf { R } .
$$

# Example 11.3

Consider the vertical seismic profile (VSP) problem first introduced in Example 1.3, which was solved and analyzed using Tikhonov regularization in Examples 4.4, 4.5, 4.6,and 4.7. We revisit this problem as a Bayesian problem, implementing an MVN prior with a covariance matrix of the form of (11.36). The model consists of 5O equally spaced slowness intervals along a $1 0 0 0 \mathrm { - m }$ vertical borehole with an interval length of $2 0 \mathrm { m }$ . Seismic travel time data are collected at 5O equally spaced depths with independent zero-mean normal erors with standard deviation of $\sigma _ { D } = 2 \times 1 0 ^ { - 4 } ~ \mathrm { s }$ ， producing a data covariance matrix $\mathbf { C } _ { D } = \sigma _ { D } ^ { 2 }$ I. We apply a prior distribution that is consistent with a seismic slownes decrease (velocity increase) with depth and has a constant gradient between known seismic slownesses from the top and the bottom of the borehole. We first impose a prior distribution standard deviation of $\sigma _ { M } = 2 \times 1 0 ^ { - 5 } \mathrm { s / m }$ on all parameters to repre-sent an estimated variability in model slownesses,and utilize a prior correlation function that falls off with a scale length of five model intervals (i.e.,a correlation of $1 / e$ at a model parameter lag of approximately five model parameters or $1 0 0 ~ \mathrm { m }$ ). The prior distribution and its parameter standard deviations are shown in Figure 11.9,and the corresponding parameter correlation function is shown in Figure 11.1O. The resulting posterior distribution and its standard deviations are shown in Figure 11.11. We next apply a prior with twice the correlation length (Figure 11.12). The resulting posterior distribution is shown in Figure 11.13.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/46fc94eac9a475a0bf79c3165afb425cd765e30d656d8925756d24106d74b3ba.jpg)  
Figure 11.9 A constant-slowness gradient prior distribution and its $9 5 \%$ distribution intervals for the VSP problem.The true model is shown as the gray smooth curve.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/3cdfddfb5b09a5fa4c32ea65cff0b2c4f83f8542005c6ab915a6bcc122d321c7.jpg)  
Figure 11.10 A correlation function for the prior distribution of Figure 11.9 with a $1 / e$ correlation length of approximately five parameters $( 1 0 0 \mathsf { m } )$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/683c97c05cc605d4930026c1391fc554748ca352ab91c763c1ae2c9940af248b.jpg)  
Figure 11.11 MAP model obtained from the posterior distribution,and its $9 5 \%$ distribution intervals, using the prior distribution described in Figures 11.9 and 11.10.The true model is shown as the gray smooth curve.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/529da890a8765d34881afb9ed238dd0a876883555e8e10870f3b5ac2950339dc.jpg)  
Figure 11.12 A correlation function for the prior distribution of Figure 11.9 with a $1 / e$ correlation length of approximately10 parameters $( 2 0 0 \mathsf { m } )$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0004_pages_0211-0280/auto/images/650346aba64012bad47090159673e9ff1616865ddd505e190ff8a06b145bfc93.jpg)  
Figure 11.13 MAP model obtained from the posterior distribution,and its $9 5 \%$ distribution intervals, using the prior distribution depicted in Figures 11.9 and 11.12.The true model is shown as the gray smooth curve.

The approach described in this section can be extended to nonlinear problems. To find the MAP solution, solve the nonlinear least squares problem,

$$
\operatorname* { m i n } \quad \mathbf { G } ( \mathbf { m } ) - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } ( \mathbf { m } ) - \mathbf { d } ) + ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) .
$$

One can then linearize around the MAP solution to obtain the approximate posterior covariance,

$$
\mathbf { C } _ { M ^ { \prime } } = ( \mathbf { \Delta J ( m _ { M A P } ) } ^ { T } \mathbf { C } _ { D } ^ { - 1 } \mathbf { J ( m _ { M A P } ) } + \mathbf { C } _ { M } ^ { - 1 } ) ^ { - 1 } ,
$$

where $\mathbf { J } ( \mathbf { m } )$ is the Jacobian. As with other nonlinear optimization problems,we must consider the possbility of multiple local optima. If (11.37) has multiple solutions with comparable likelihoods,then a single MAP solution and associated $\mathbf { C } _ { M ^ { \prime } }$ from (11.38) will not accurately characterize the posterior distribution.

# 11.4.THE MARKOV CHAIN MONTE CARLO METHOD

We next introduce the use of Markov Chain Monte Carlo (MCMC) methods to sample from a posterior distribution. Given a sufficient population of such samples,we can use them to characterize the solution of a Bayesian inverse problem.Because MCMC methods depend only on the forward model and associated likelihood calculations, they are easily applied to both linear and nonlinear problems.


<!-- chunk 0005: pages 281-350 -->
A Markov chain is a sequence of random variables,

$$
X ^ { 0 } , X ^ { 1 } , X ^ { 2 } , \ldots ,
$$

where the probability distribution of $X ^ { n + 1 }$ depends solely on the previous value, $X ^ { n }$ , and not on earlier values of random variables in the sequence. That is,

$$
P ( X ^ { n + 1 } | X ^ { 0 } , X ^ { 1 } , \ . \ . \ . \ , X ^ { n } ) = P ( X ^ { n + 1 } | X ^ { n } ) .
$$

The particular Markov chains considered here will be time-invariant, so that the Markov chain transition kernel

$$
P ( X ^ { n } , X ^ { n + 1 } ) = P ( X ^ { n + 1 } | X ^ { n } )
$$

is independent of $n$ .

For example, consider a one-dimensional random process in which we start at $X ^ { 0 } = 0$ , and then iteratively compute $X ^ { n + 1 }$ from $X ^ { n }$ by adding an $N ( 0 , \sigma ^ { 2 } )$ realization to $X ^ { n }$ . Clearly $X ^ { n + 1 }$ depends directly on $X ^ { n }$ , and this dependence is time-invariant. The transition kernel for this Markov chain is

$$
k ( x _ { 1 } , x _ { 2 } ) = \frac { 1 } { \sqrt { 2 \pi } \sigma } e ^ { - \frac { 1 } { 2 } ( x _ { 1 } - x _ { 2 } ) ^ { 2 } / \sigma ^ { 2 } } .
$$

In the MCMC method, we are interested in Markov chains that have limiting distributions, $q ( \mathbf { x } )$ , such that

$$
\operatorname* { l i m } _ { n  \infty } { \cal P } ( X ^ { n } | X ^ { 0 } ) = q ( { \bf x } ) .
$$

Not all Markov chains have limiting distributions. For example, if $X ^ { n }$ is the sum of $n$ independent $N ( 0 , \sigma ^ { 2 } )$ random variables, $X ^ { n }$ has an $N ( 0 , n \sigma ^ { 2 } )$ distribution. This does not approach a limiting probability distribution as $n \to \infty$ .

For a general multivariate model, it can be shown that if $q ( \mathbf { x } )$ and $k ( \mathbf { x } , \mathbf { y } )$ satisfy the local balance equation

$$
q ( \mathbf { x } ) k ( \mathbf { x } , \mathbf { y } ) = q ( \mathbf { y } ) k ( \mathbf { y } , \mathbf { x } )
$$

for all models $\mathbf { x }$ and $\mathbf { y }$ , then $q ( \mathbf { x } )$ is the limiting distribution of the Markov chain. Equation (11.44) states that the rate of model transitions from $\mathbf { x }$ to $\mathbf { y }$ equals the rate from $\mathbf { y }$ to $\mathbf { x }$ .

The Metropolis-Hastings sampler is an algorithm that simulates a Markov chain with a specified limiting distribution. We will apply it to produce samples from a posterior distribution $q ( \mathbf { m } | \mathbf { d } )$ that will tend to densely sample its higher likelihood regions. With enough such samples, we can usefully characterize the posterior distribution of a Bayesian parameter estimation or inverse problem. Since the data vector $\mathbf { d }$ is given, we will simply write $q ( \mathbf { m } | \mathbf { d } )$ as $q ( \mathbf { m } )$ throughout the following development.

We begin a Metropolis-Hastings sampler implementation by picking a proposal distribution $r ( \mathbf { x } , \mathbf { y } )$ that facilitates random steps in the posterior model space. These randomly perturbed samples will subsequently be subjected to a likelihood-based test in the Metropolis-Hastings sampler. A common choice for the proposal distribution is an MVN distribution with zero covariances and variances $\sigma _ { i } ^ { 2 }$ , so that

$$
r ( x _ { i } , \ \gamma _ { i } ) \propto e ^ { - \frac { 1 } { 2 } ( x _ { i } - \gamma _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } .
$$

Although $r ( \mathbf { x } , \mathbf { y } )$ cannot be implemented as a transition kernel directly, because it does not satisfy (11.44), this can be remedied by introducing a factor called the acceptance ratio,

$$
\alpha ( \mathbf { x } , \mathbf { y } ) = \operatorname* { m i n } ( 1 , s ) ,
$$

where

$$
s = \frac { q ( \mathbf { y } ) r ( \mathbf { y } , \mathbf { x } ) } { q ( \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) } .
$$

Note that $0 \leq \alpha ( \mathbf { x } , \mathbf { y } ) \leq 1$ . Also note that

$$
\alpha ( \mathbf { y } , \mathbf { x } ) = \operatorname* { m i n } { \big ( } 1 , s ^ { - 1 } { \big ) } .
$$

At least one of $\alpha ( \mathbf { x } , \mathbf { y } )$ and $\alpha ( \mathbf { y } , \mathbf { x } )$ will thus be equal to 1, depending on whether $s$ is greater than or less than 1.

Now, let

$$
\tilde { k } ( \mathbf { x } , \mathbf { y } ) = \alpha ( \mathbf { x } , \mathbf { y } ) r ( \mathbf { x } , \mathbf { y } ) .
$$

$\alpha ( \mathbf { x } , \mathbf { y } ) \leq 1$ , so

$$
\beta ( x ) = \int _ { \mathrm {  ~ \scriptstyle { \tau } ~ } , \mathrm {  ~ { \tau } ~ } } \tilde { k } ( { \bf x } , { \bf y } ) \ d { \bf y } = \int _ { \mathrm {  ~ \scriptstyle { \tau } ~ } , \mathrm {  ~ { \tau } ~ } } \alpha ( { \bf x } , { \bf y } ) r ( { \bf x } , { \bf y } ) \ d { \bf y } \leq 1 .
$$

Thus $\tilde { k } ( \mathbf { x } , \mathbf { y } )$ is not a properly normalized transition kernel. We can, however, obtain a normalized kernel by defining

$$
k ( \mathbf { x } , \mathbf { y } ) = \tilde { k } ( \mathbf { x } , \mathbf { y } ) + ( 1 - \beta ) \delta ( \mathbf { x } - \mathbf { y } )
$$

so that

all

$$
\begin{array} { r l r }    \int _ { \mathrm {  ~ \scriptstyle { \Psi ~ } } } k ( \mathbf { x } , \mathbf { y } ) \ d y = \begin{array} { l } { \displaystyle \int _ { \mathrm {  ~ \scriptstyle { \Psi ~ } } } \alpha ( \mathbf { x } , \mathbf { y } ) r ( \mathbf { x } , \mathbf { y } ) \ d \mathbf { y } + \small { \int _ { \mathrm {  ~ \scriptstyle { \Psi ~ } } } } ( 1 - \beta ) \delta ( \mathbf { x } - \mathbf { y } ) \ d \mathbf { y } } \\ { \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm { \scriptscriptstyle { \mathrm {  ~ \scriptstyle { ~ \psi ~ } } ~ } } } \end{array} \end{array}
$$

A simple algorithm can now be used to generate a random value $\mathbf { y }$ from $\mathbf { x }$ that satisfies (11.44).

# Algorithm 11.1 Transition Kernel Evaluation

1. Generate a candidate $\mathbf { y }$ from $\mathbf { x }$ according to the proposal distribution $r ( \mathbf { x } , \mathbf { y } )$ .   
2. Compute $\alpha ( \mathbf { x } , \mathbf { y } )$ .   
3. With probability $\alpha$ , return the candidate $\mathbf { y }$ .   
4. With probability $1 - \alpha$ , return the previous value $\mathbf { x }$ .

Now, we need to show that $q ( \mathbf { x } )$ and $k ( \mathbf { x } , \mathbf { y } )$ as defined above satisfy the local balance equation (11.44). If $\mathbf { y } = \mathbf { x }$ , this is obviously true. For $\mathbf { y } \neq \mathbf { x }$ , we need to consider the two cases of $\alpha ( \mathbf { x } , \mathbf { y } ) = 1$ or $\alpha ( \mathbf { y } , \mathbf { x } ) = 1$ . If $\alpha ( \mathbf { x } , \mathbf { y } ) = 1$ , then

$$
\alpha ( \mathbf { y } , \mathbf { x } ) = s ^ { - 1 } = \frac { q ( \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) } { q ( \mathbf { y } ) r ( \mathbf { y } , \mathbf { x } ) }
$$

and

$$
q ( { \bf x } ) k ( { \bf x } , { \bf y } ) = q ( { \bf x } ) \alpha ( { \bf x } , { \bf y } ) r ( { \bf x } , { \bf y } ) = q ( { \bf x } ) r ( { \bf x } , { \bf y } ) .
$$

Also,

$$
q ( { \bf y } ) k ( { \bf y } , { \bf x } ) = q ( { \bf y } ) \alpha ( { \bf y } , { \bf x } ) r ( { \bf y } , { \bf x } ) = q ( { \bf y } ) \frac { q ( { \bf x } ) r ( { \bf x } , { \bf y } ) } { q ( { \bf y } ) r ( { \bf y } , { \bf x } ) } r ( { \bf y } , { \bf x } ) = q ( { \bf x } ) r ( { \bf x } , { \bf y } ) .
$$

However, $q ( \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) = q ( \mathbf { x } ) k ( \mathbf { x } , \mathbf { y } )$ , so

$$
q ( \mathbf { y } ) k ( \mathbf { y } , \mathbf { x } ) = q ( \mathbf { x } ) k ( \mathbf { x } , \mathbf { y } ) ,
$$

thus satisfying (11.44). A similar argument shows that (11.44) is satisfied for the case where $\alpha ( \mathbf { y } , \mathbf { x } ) = 1$ .

There are several important tactics that help to simplify the method further. Because the product of $q$ and $r$ appears in both the numerator and denominator of $s$ , we need only know these factors to constants of proportionality, and thus do not need to normalize $q$ and $r$ in individual calculations. Also note that the posterior distribution, $q ( \mathbf { m } )$ , is proportional to the product of the prior, $p ( \mathbf { m } )$ , and the likelihood, $f ( \mathbf { d } | \mathbf { m } )$ (11.3). We can thus write (11.46) as

$$
\begin{array} { r } { \alpha ( \mathbf { x } , \mathbf { y } ) = \operatorname* { m i n } { \left( 1 , \frac { p ( \mathbf { y } ) f ( \mathbf { d } | \mathbf { y } ) r ( \mathbf { y } , \mathbf { x } ) } { p ( \mathbf { x } ) f ( \mathbf { d } | \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) } \right) } . } \end{array}
$$

If $r ( \mathbf { x } , \mathbf { y } )$ is a symmetric distribution, such as (11.45), then $r ( \mathbf { x } , \ \mathbf { y } ) = r ( \mathbf { y } , \ \mathbf { x } )$ , and we can simplify (11.57) to

$$
\alpha ( \mathbf { x } , \mathbf { y } ) = \operatorname* { m i n } { \left( 1 , \frac { q ( \mathbf { y } ) } { q ( \mathbf { x } ) } \right) } .
$$

In computational practice, numbers in the numerator of (11.58) may be extremely small, and can thus generate floating point underflow problems. This is easily avoided by evaluating $\log \alpha ( \mathbf { x } , \mathbf { y } )$ instead of $\alpha ( \mathbf { x } , \mathbf { y } )$ . We now have all the components to describe the Metropolis-Hastings sampler.

# Algorithm 11.2 The Metropolis-Hastings Sampler

Given a starting model, $\mathbf { m } ^ { 0 }$ , repeat the following steps for $j = 1 , 2 , \dots { }$ . until the posterior distribution is sufficiently sampled by the set of models $\mathbf { m } ^ { j }$ .

1. Generate a candidate model $\mathbf { c }$ from the previous model, $\mathbf { m } ^ { j }$ , using the proposal distribution $r ( \mathbf { m } ^ { j } , \mathbf { c } )$ .   
2. Compute log $\alpha ( \mathbf { m } ^ { j } , \mathbf { c } )$ .   
3. Let $t$ be a realization of a uniformly distributed random variable on [0, 1].   
4. If $\log \ t < \log \alpha ( \mathbf { m } ^ { j } , \mathbf { c } )$ , then accept the candidate model and let $\mathbf { m } ^ { j + 1 } = \mathbf { c }$ ; otherwise reject the candidate model and let $\mathbf { m } ^ { j + 1 } = \mathbf { m } ^ { j }$ .

Note that if $\log t$ is quite small, we will occasionally accept a new model that has a small acceptance ratio and thus move towards a model with reduced likelihood. This property of the algorithm helps overcome the problem of having the sampling become trapped near a localized likelihood maximum. The behavior of the algorithm and its ability to sample the posterior distribution fruitfully and efficiently will depend on the size of the steps taken in generating candidate models. In the case of the normal formulation for the proposal distribution (11.45), this will be controlled by the size of the $\sigma _ { i }$ . Smaller steps will result in higher acceptance rates, but the algorithm may be unacceptably slow at exploring the posterior distribution. Conversely, larger steps will result in lower acceptance ratios and will thus be less frequently accepted. Either situation may cause the algorithm to become stuck in a particular region of the posterior distribution. Often, the step size parameters are explored adaptively in multiple runs of the algorithm (which may be run as independent parallel processes on a multi-CPU computer system). Some studies, e.g., [51], suggest that the algorithm is optimally tuned when the new model acceptance rate is between approximately $20 \%$ and $50 \%$ .

# 11.5. ANALYZING MCMC OUTPUT

Although the limiting distribution of the Markov chain sampled by the Metropolis-Hastings algorithm is the desired posterior distribution, there are significant practical challenges in analyzing the output of an MCMC simulation.

First, successive models $m ^ { k }$ , $m ^ { k + 1 }$ , $m ^ { k + 2 }$ , . . . , produced by the simulation are typically strongly correlated with each other, but most statistical techniques require independent samples. In practice, this complication can be avoided by analyzing a subset of samples that are far apart in the sample sequence. For example, if we examine $\mathbf { m } ^ { k }$ , $\mathbf { m } ^ { k + 1 0 0 0 }$ , $\mathbf { m } ^ { k + 2 0 0 0 }$ , . . . , it is likely that samples taken 1000 steps apart will not be highly correlated. We can verify this by plotting the successive model autocorrelations for the history of sampling over some moving window length.

Second, early Metropolis-Hastings algorithm samples will be biased by the initial model $\mathbf { m } ^ { 0 }$ , which may not lie in a high likelihood region of the posterior distribution. This issue is commonly addressed by skipping over early samples in the chain to give time for the algorithm to “burn in,” and/or by running the process with a variety of starting models, either sequentially or in parallel on multiple CPUs. For example, if it is determined that samples spaced 1000 steps apart are effectively uncorrelated, then it might be reasonable to let the Metropolis-Hastings sampler establish itself for 10,000 steps before beginning to collect samples.

Once we are confident that the procedure has produced a large enough collection of effectively independent samples, we can use the results to characterize the posterior distribution. For a suitably large sample, the MAP solution can be estimated as the retrieved posterior distribution sample that has the greatest likelihood. The posterior distribution may be approximately multivariate normal, which can be established by examining model histograms and quantile-quantile (Q-Q) plots. In this case we can readily construct probability intervals for describing the posterior distribution from the sample mean and covariance using normal assumptions. However, if the distribution is distinctly non-normal, it will be more difficult to produce a simple summary of its character, particularly for very high dimensional models. A common approach is to produce and evaluate scatter plots and/or histograms that display key features of the posterior distribution and to use counting statistics to establish probability intervals.

# Example 11.4

Reconsidering the ill-posed nonlinear parameter estimation problem of Example 9.2, we apply the Metropolis-Hastings algorithm to the problem of fitting four parameters, $m _ { i }$ , to the nonlinear function

$$
d _ { i } = ( G ( \mathbf { m } ) ) _ { i } = m _ { 1 } e ^ { m _ { 2 } x _ { i } } + m _ { 3 } x _ { i } e ^ { m _ { 4 } x _ { i } }
$$

given a set of observations, $d _ { i }$ , with specified independent normally distributed data noise, specified by corresponding standard deviations $\sigma _ { i }$ . As in Example 9.2, the true model parameters are $m _ { 1 } = 1 . 0 , \ m _ { 2 } = - 0 . 5 , \ m _ { 3 } = 1 . 0 ,$ , and $m _ { 4 } = - 0 . 7 5$ ; data are produced at 25 equally spaced points, $x _ { i }$ , on the interval [1, 7]; and $N ( 0 , 0 . 0 1 ^ { 2 } )$ independent noise is added to each data element. The likelihood function is specified by

$$
f ( \mathbf { d } | \mathbf { m } ) \propto \prod _ { i = 1 } ^ { m } e ^ { - \frac { 1 } { 2 } ( d _ { i } - G ( \mathbf { m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } ,
$$

which, after taking the natural logarithm, is

$$
\log ( f ( \mathbf { d } | \mathbf { m } ) ) = - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } ( d _ { i } - G ( \mathbf { m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } + C ,
$$

where $C$ is the logarithm of the constant of proportionality in (11.60). We sample the posterior distribution using 410,000 steps, and produce a low-correlation set of 400 samples by allowing a 10,000 sample burn in and selecting subsequent samples spaced 1000 steps apart by down-sampling the full 410,000 length sequence. The procedure was initiated using a random model selected from a 4-dimensional uniform distribution bounded by $[ - 1 , 1 ]$ in each parameter direction and applying a uniform prior for the region $m _ { 1 } = [ 0 , 2 ]$ , $m _ { 2 } = [ - 1 , 0 ]$ , $m _ { 3 } = [ 0 , 2 ]$ , and $m _ { 4 } = [ - 1 , 0 ]$ . In each of the MCMC steps, we apply independent normally distributed random perturbations with standard deviations of 0.005 in each of the four model parameter directions, accepting or rejecting the corresponding candidate models according to the Metropolis-Hastings algorithm. The procedure produced an acceptance rate of approximately $3 9 . 5 \%$ , which is in the nominally acceptable range of not being too large or too small [51].

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/fff9738852e6a1b06f006ca74348f591dcb55c1258f9318494547abfd9f177aa.jpg)  
Figure 11.14 Sampled posterior distribution for Example 11.3. The true model is shown as the large black dot, and the MAP model estimated from the maximum likelihood posterior distribution sample is indicated by the open circle. 400 retrieved samples of the posterior distribution (every 1000th calculated sample from the MCMC output) are shown as gray dots. Ninety-five percent probability intervals estimated from the MCMC posterior distribution samples are shown by boxes.

Figure 11.14 shows scatter plots and histograms of the resulting sampled posterior distribution, along with the corresponding MAP solution and $9 5 \%$ probability intervals for each parameter direction, which well enclose the true solution. Figure 11.15 shows the time history of the corresponding 400 samples. The prominent quasilinear scattering trends in the output between $m _ { 2 }$ and $m _ { 3 }$ are indicative of a high degree of anticorrelation between some parameter pairs. This anticorrelation is also apparent in the sequence of parameter samples in Figure 11.15, for example in the anticorrelated trends of $m _ { 2 }$ and m3. An examination of the parameter autocorrelations for the samples shown in Figure 11.14 (Figure 11.16) shows that individual parameter estimates are effectively decorrelated after 20 or fewer steps. Figure 11.17 shows a histogram of the natural log of likelihood values for the posterior samples. The multimodal nature of this histogram is reflective of the “bumpy” likelihood function surface for this ill-posed problem with random data noise, a situation that also resulted in multiple solutions when we applied classical nonlinear solution methods in Example 9.2. However, the MCMC method here provided a sufficiently thorough search of the model space to allow us to discriminate the MAP solution from solutions corresponding to subsidiary likelihood maxima.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/698eb19fb1d3779bfd3cb4fc96b2410f9c07f822f955ed4b303e639d1c746e88.jpg)  
Figure 11.15 Time history of the posterior samples plotted in Figure 11.14. True parameters are shown as gray lines.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/6d7295f0add0d254e3552708048a8687db1695bd25701f520eb393ccdb08d59e.jpg)  
Figure 11.16 Twenty-point autocorrelations for posterior distribution parameters shown in Figure 11.15.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/fee2f04818f682d736a9619f14784b2196421a05ade3ae29601ed1194df60d7c.jpg)  
Figure 11.17 Natural logarithm of the likelihood function for the 400 posterior distribution samples shown in Figures 11.14 and 11.15. The value for the true model is approximately −10 2, and the value for the MAP model is approximately $- 8 . 7$ .

# 11.6. EXERCISES

1. Reanalyze the data in Example 11.1 using a prior distribution that is uniform on the interval [9, 11]. Compute the posterior distribution after the first measurement of $1 0 . 3 ~ \mu \mathrm { g }$ and after the second measurement of $1 0 . 1 ~ { \mu \mathrm { g } }$ . What is the posterior mean?

2. Consider the estimation problem $\mathbf { d } = \mathbf { m }$ (i.e., where $\mathbf { G } = \mathbf { I } )$ ) in two dimensions. The data, $\mathbf { d } = [ 5 \ 1 5 ] ^ { T } ,$ have identical and independent normal errors with standard deviations of $\sqrt { 2 }$ . Apply a zero-mean MVN prior characterized by a covariance matrix where $m _ { 1 }$ and $m _ { 2 }$ have a correlation coefficient of 0.9, and equal standard deviations of $\sqrt { 5 }$ . Calculate the MAP model, and compute and plot the $50 \%$ , $90 \%$ , and $9 5 \%$ contours of the MVN distributions d, $\mathbf { m } _ { \mathrm { p r i o r } }$ , and the posterior model.

3. In writing (11.28) we made use of the matrix square root.

a. Suppose that A is a symmetric and positive definite matrix. Using the SVD, find an explicit formula for the matrix square root. Your square root should itself be a symmetric and positive definite matrix.   
b. Show that instead of using the matrix square roots of $\mathbf { C } _ { D } ^ { - 1 }$ and $\mathbf { C } _ { M } ^ { - 1 }$ , we could have used the Cholesky factorizations of $\mathbf { C } _ { D } ^ { - 1 }$ and $\mathbf { C } _ { M } ^ { - 1 }$ in formulating the least squares problem.

4. Consider the following coin tossing experiment. We repeatedly toss a coin, and each time record whether it comes up heads (0) or tails (1). The bias $b$ of the coin is the probability that it comes up heads. We have reason to believe that this is not a fair coin, so we will not assume that $b = 1 / 2$ . Instead, we will begin with a uniform prior distribution $p ( b ) = 1$ , for $0 \leq b \leq 1$ .

a. What is $f ( d | b ) \Rsh$ Note that the only possible data are 0 and 1, so this distribution will involve delta functions at $d = 0$ , and $d = 1$ .   
b. Suppose that on our first flip, the coin comes up heads. Compute the posterior distribution $q ( b | d _ { 1 } = 0 )$ .   
c. The second, third, fourth, and fifth flips are 1, 1, 1, and 1. Find the posterior distribution $q ( b | d _ { 1 } = 0 , d _ { 2 } = 1 , d _ { 3 } = 1 , d _ { 4 } = 1 , d _ { 5 } = 1 )$ . Plot the posterior distribution.   
d. What is your MAP estimate of the bias?   
e. Now, suppose that you initially felt that the coin was at least close to fair, with

$$
\begin{array} { r } { p ( b ) \propto e ^ { - 1 0 ( b - 0 . 5 ) ^ { 2 } } \quad 0 \leq b \leq 1 . } \end{array}
$$

Repeat the analysis of the five coin flips described above.

5. Apply the Bayesian method to Exercise 2 in Chapter 4. Select what you consider to be a reasonable prior. How sensitive is your solution to the prior mean and covariance?

6. Apply the Bayesian method to Exercise 9.3. Assume an MVN prior distribution for $\alpha$ and $n$ , with $\alpha$ and $n$ independent. The prior for $\alpha$ should have a mean of 0.01 and a standard deviation of 0.005, and the prior for $n$ should have a mean of 5 and a standard deviation of 3. Compare your solution with the solution that you obtained to Exercise 9.3. How sensitive is your solution to the choice of the prior?

7. Repeat Exercise 11.6, using MCMC to estimate the posterior distribution. Compare your solution to the solution that you obtained for Exercise 11.6.

8. Apply the Metropolis-Hastings sampler to produce a sampled posterior distribution for the nonlinear parameter estimation problem of Example 9.1. Use a prior distribution that is uniform on $S = [ 0 , 0 . 0 1 ]$ and $T = [ 0 , 2 ]$ , a zero covariance MVN proposal distribution, and a starting model of $( S , \ T ) = ( 5 \times 1 0 ^ { - 3 }$ , 1.0). Generate 200,000 samples using a 10,000-sample burn-in and explore independent step sizes for the two parameters in your proposal distribution to obtain a Metropolis-Hastings sampler acceptance rate between $10 \%$ and $50 \%$ . Extract every 1000th sample for analysis and establish that these 191 samples are not highly dependent by examining sample autocorrelation functions. Examine the sampled distribution to obtain the MAP model and empirical $9 5 \%$ probability intervals on $S$ and $T$ . Apply a $\mathrm { Q - }$ $\mathrm { Q }$ plot and assess the multivariate normality of the sampled posterior distribution and compare normal assumption and empirical estimates of the $9 5 \%$ probability intervals.

9. Apply the Metropolis-Hastings sampler to produce a sampled posterior distribution for the nonlinear inverse problem for gravity observations above a buried density perturbation with an unknown variable depth $m ( x )$ and a fixed density perturbation $\Delta \rho$ , as described in Exercise 10.2. Your prior should be selected to favor smooth (specified by nonzero parameter correlations) models.

# 11.7. NOTES AND FURTHER READING

The arguments for and against the use of Bayesian methods in statistics and inverse problems have raged for decades. Some classical references that provide context for these arguments include [35, 42, 80, 81, 136]. Sivia and Skilling’s book [143] is a good general introduction to Bayesian ideas for scientists and engineers. The book by Calvetti and Somersalo introduces Bayesian methods for inverse problems including Markov Chain Monte Carlo sampling and includes MATLAB examples [22]. The book by Kaipio and Somersalo provides a more detailed theoretical treatment of Bayesian methods for inverse problems and includes some interesting case studies [83]. An early paper by Tarantola and Valette on the application of the Bayesian approach was quite influential [156], and Tarantola’s book is the standard reference work on Bayesian methods for inverse problems [155]. The book by Rodgers [133] focuses on application of the Bayesian approach to problems in atmospheric sounding. The paper by Gouveia and Scales [56] discusses the relative advantages and disadvantages of Bayesian and classical methods for inverse problems. The draft textbook by Scales and Smith [137] takes a Bayesian approach to inverse problems.

In many cases the solution to an inverse problem will be used in making a decision, with measurable consequences for making the “wrong” decision. Statistical decision theory can be helpful in determining the optimal decision. The paper by Evans and Stark provides a good introduction to the application of statistical decision theory to inverse problems [48].

# Epilogue

The theme of this book has been obtaining and analyzing solutions to discretized parameter estimation problems using classical and Bayesian approaches. We have discussed computational procedures for both linear and nonlinear problems. Classical procedures produce estimates of the parameters and their associated uncertainties. In Bayesian methods, the model is a random variable, and the solution is its probability distribution.

However, there are critical issues that arise in solving these problems. When we discretize a continuous problem, the choice of the discretization scheme, basis functions, and grid spacing can have large effects on the behavior of the discretized problem and its solutions, and these effects will not be reflected in the statistical analysis of the solution of the discretized problem. The discretization errors in the solution could potentially be far larger than any explicitly computed statistical uncertainty. Thus it is important to ensure that the discretization provides an adequate approximation to the continuous problem. If no formal analysis is performed, it is at least desirable to see whether varying the discretization has a significant effect on the solutions obtained.

For well-conditioned problems with normally distributed measurement errors, we can use the classical least squares approach. This results in unbiased parameter estimates and associated confidence intervals. For ill-conditioned problems, and for problems where we have good reason to prefer a specific bias in the character of the solution, Tikhonov regularization can be applied to obtain a solution. However, regularization introduces bias into the solution, and it is impossible to even bound this bias without making additional assumptions about the model.

Although Bayesian approaches are also applicable to well-conditioned situations, they are particularly interesting in the context of ill-conditioned problems. By selecting a prior distribution, we make explicit assumptions about the model. The resulting posterior distribution is not affected by regularization bias. In the multivariate normal case for linear problems the Bayesian approach is no more difficult computationally than the least squares approach.

Various efforts have been made to avoid the use of subjective priors in the Bayesian approach. Principles such as maximum entropy can be used to derive prior distributions that have been claimed to be, in some sense, “objective.” However, we do not find these arguments completely convincing, and in many cases the choice of prior has a similar effect on the choice of the regularization operations in Tikhonov and other classical approaches. Markov Chain Monte Carlo methods present a computationally intensive methodology to sample and characterize the Bayesian posterior distribution using forward model-based likelihood calculations.

Both the classical and Bayesian approaches can be extended to nonlinear inverse problems. The computation of the estimated model parameters becomes substantially more complex in that we must solve nonlinear optimization problems which may have multiple locally optimal solutions. In both standard approaches, the statistical analysis is typically performed approximately by analyzing a linearization of the nonlinear model around the estimated parameters. However, the validity of this approach will depend on the data uncertainties and the nonlinearity of the problem. The Bayesian approach can in theory be applied when measurement errors are not normally distributed. In practice, however, the associated analytical computations can be difficult. Markov Chain Monte Carlo methods provide a very general approach for characterizing the posterior distribution that avoids the difficulties of computing it in analytical form.

# APPENDIX A

# Review of Linear Algebra

# Synopsis

A summary of essential concepts, definitions, and theorems in linear algebra used throughout this book.

# A.1. SYSTEMS OF LINEAR EQUATIONS

Recall that a system of linear equations can be solved by the process of Gaussian elimination.

# Example A.1

Consider the following system of equations:

$$
\begin{array} { l } { { x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = 1 4 } } \\ { { \qquad } } \\ { { x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 1 1 } } \\ { { \qquad } } \\ { { x _ { 1 } + 3 x _ { 2 } + 4 x _ { 3 } = 1 9 . } } \end{array}
$$

We eliminate $x _ { 1 }$ from the second and third equations by subtracting the first equation from the second and third equations to obtain

$$
\begin{array} { r l r } & { } & { x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = 1 4 } \\ & { } & { - x _ { 3 } = - 3 } \\ & { } & { x _ { 2 } + x _ { 3 } = 5 . } \end{array}
$$

We would like $x _ { 2 }$ to appear in the second equation, so we interchange the second and third equations:

$$
\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = ~ 1 4 } \\ { x _ { 2 } + x _ { 3 } = ~ 5 } \\ { - x _ { 3 } = - 3 . } \end{array}
$$

Next, we eliminate $x _ { 2 }$ from the first equation by subtracting two times the second equation from the first equation:

$$
\begin{array} { c } { { x _ { 1 } + x _ { 3 } = ~ 4 } } \\ { { x _ { 2 } + x _ { 3 } = ~ 5 } } \\ { { - x _ { 3 } = - 3 . } } \end{array}
$$

We then multiply the third equation by $- 1$ to get an equation for $x _ { 3 }$

$$
\begin{array} { r } { x _ { 1 } + x _ { 3 } = 4 } \\ { x _ { 2 } + x _ { 3 } = 5 } \\ { x _ { 3 } = 3 . } \end{array}
$$

Finally, we eliminate $x _ { 3 }$ from the first two equations to obtain a solution to the original system of equations:

$$
\begin{array} { l } { x _ { 1 } = 1 } \\ { x _ { 2 } = 2 } \\ { x _ { 3 } = 3 . } \end{array}
$$

Geometrically the constraints specified by the three equations of (A.1) describe three planes that, in this case, intersect in a single point, $x _ { 1 } = 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = 3$ .

In solving (A.1), we used three elementary row operations: adding a multiple of one equation to another equation, multiplying an equation by a nonzero constant, and swapping two equations. This process can be extended to solve systems of equations with an arbitrary number of variables.

In performing the elimination process, the actual names of the variables are insignificant. We could have renamed the variables in the above example to $a , b$ , and $c$ without changing the solution in any significant way. Because the actual names of the variables are insignificant, we can save space by writing down the significant coefficients from the system of equations in matrix form as an augmented matrix. The augmented matrix form is also useful in solving a system of equations in computer algorithms, where the elements of the augmented matrix are stored in an array.

In augmented matrix form (A.1) becomes

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 1 } & { 2 } & { 2 } \\ { 1 } & { 3 } & { 4 } \end{array} \right] } \ 1 4 { \bigg ] } .
$$

In augmented notation, the elementary row operations become adding a multiple of one row to another row, multiplying a row by a nonzero constant, and interchanging

two rows. The Gaussian elimination process is essentially identical to the process used in Example A.1, with the final version of the augmented matrix given by

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 3 } \end{array} \right] } .
$$

Definition A.1 A matrix is said to be in reduced row echelon form (RREF) if it has the following properties:

1. The first nonzero element in each row is a 1. The first nonzero row elements of the matrix are called pivot elements. A column in which a pivot element appears is called a pivot column.   
2. Except for the pivot element, all elements in pivot columns are 0s.   
3. Each pivot element is to the right of the pivot elements in previous rows.   
4. Any rows consisting entirely of 0s are at the bottom of the matrix.

In solving a system of equations in augmented matrix form, we apply elementary row operations to reduce the augmented matrix to RREF and then convert back to conventional notation to read off the solutions. The process of transforming a matrix into RREF can easily be automated. In MATLAB, this is done by the rref command.

It can be shown that any linear system of equations has either no solutions, exactly one solution, or infinitely many solutions [95]. In a system of two dimensions, for example, lines represented by the equations can fail to intersect (no solution), intersect at a point (one solution), or intersect in a line (many solutions). The following example shows how to determine the number of solutions from the RREF of the augmented matrix.

# Example A.2

Consider a system of two equations in three variables that has many solutions:

$$
\begin{array} { r } { x _ { 1 } + x _ { 2 } + x _ { 3 } = 0 } \\ { x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 0 . } \end{array}
$$

We put this system of equations into augmented matrix form and then find the RREF, which is

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] } .
$$

We can translate this back into equation form as

$$
\begin{array} { r } { x _ { 1 } = 0 } \\ { \qquad } \\ { x _ { 1 } + x _ { 3 } = 0 . } \end{array}
$$

Clearly, $x _ { 1 }$ must be 0 in any solution to the system of equations. However, $x _ { 2 }$ and $x _ { 3 }$ are not fixed. We could treat $x _ { 3 }$ as a free variable and allow it to take on any value. Whatever value $x _ { 3 }$ takes on, $x _ { 2 }$ must be equal to $- { x } _ { 3 }$ . Geometrically, this system of equations describes the intersection of two planes, where the intersection consists of points on the line $x _ { 2 } = - x _ { 3 }$ in the $x _ { 1 } = 0$ plane.

A linear system of equations may have more equation constraints than variables, in which case the system of equations is over-determined. Although over-determined systems often have no solutions, it is possible for an over-determined system of equations to have either many solutions or exactly one solution.

Conversely, a system of equations with fewer equations than variables is underdetermined. Although in many cases under-determined systems of equations have infinitely many solutions, it is also possible for such systems to have no solutions.

A system of equations with all 0s on the right-hand side is homogeneous. Every homogeneous system of equations has at least one solution, the trivial solution in which all of the variables are 0s. A system of equations with a nonzero right-hand side is nonhomogeneous.

# A.2. MATRIX AND VECTOR ALGEBRA

As we have seen in the previous section, a matrix is a table of numbers laid out in rows and columns. A vector is a matrix consisting of a single column or row of numbers (vectors in this text are typically expressed as column vectors). In general, matrices and vectors may contain complex numbers as well as real numbers. With the exception of Chapter 8, all of the vectors and matrices in this book are real.

There are several important notational conventions used here for matrices and vectors. Boldface capital letters such as A, $\mathbf { B }$ , . . . are used to denote matrices. Boldface lower-case letters such as $\mathbf { x }$ , y, . . . are used to denote vectors. Lower-case letters or Greek letters such as ${ \it m } , n , \alpha , \beta , \ldots .$ . will be used to denote scalars.

At times we will need to refer to specific parts of a matrix. The notation $A _ { i , j }$ denotes the element of the matrix $\mathbf { A }$ in row $i$ and column $j .$ . We denote the jth element of the vector $\mathbf { x }$ by $x _ { j }$ . The notation $\mathbf { A } _ { \cdot , j }$ is used to refer to column $j$ of the matrix A, while $\mathbf { A } _ { i } ,$ · refers to row $i$ of A.

We can also construct larger matrices from smaller matrices. The notation $\mathbf { A } =$ $[ \mathbf { B } \ \mathbf { C } ]$ means that the matrix $\mathbf { A }$ is composed of the matrices $\mathbf { B }$ and $\mathbf { C }$ , with matrix $\mathbf { C }$ to the right of $\mathbf { B }$ .

If $\mathbf { A }$ and $\mathbf { B }$ are two matrices of the same size, we can add them by simply adding corresponding elements. Similarly, we can subtract B from A by subtracting the corresponding elements of $\mathbf { B }$ from those of A. We can multiply a scalar times a matrix by multiplying the scalar times each matrix element. Because vectors are just $n$ by 1 matrices, we can perform the same arithmetic operations on vectors. A zero matrix, 0, is a matrix composed of all zero elements. A zero matrix plays the same role in matrix algebra as the scalar 0, with

$$
\begin{array} { c } { \mathbf { A + 0 } = \mathbf { A } } \\ { \mathbf { \qquad } } \\ { \mathbf { \qquad = 0 + A } . } \end{array}
$$

Using vector notation, we can write a linear system of equations in vector form.

# Example A.3

Recall the system of equations (A.9),

$$
\begin{array} { r } { x _ { 1 } + x _ { 2 } + x _ { 3 } = 0 \quad } \\ { x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 0 , } \end{array}
$$

from Example A.2. We can write this in vector form as

$$
x _ { 1 } \left[ 1 \atop 1 \right] + x _ { 2 } \left[ 1 \atop 2 \right] + x _ { 3 } \left[ 1 \atop 2 \right] = \left[ 0 \atop 0 \right] .
$$

The expression on the left-hand side of (A.15) where vectors are multiplied by scalars and the results are summed together is called a linear combination.

If A is an $m$ by $n$ matrix, and $\mathbf { x }$ is an $n$ element vector, we can multiply A times $\mathbf { x }$ where the product is defined by

$$
\mathbf { A } \mathbf { x } = x _ { 1 } \mathbf { A } . _ { , 1 } + x _ { 2 } \mathbf { A } . _ { , 2 } + \cdot \cdot \cdot + x _ { n } \mathbf { A } . _ { , n } .
$$

# Example A.4

Given

$$
\mathbf { A } = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \end{array} \right] }
$$

and

$$
\mathbf { x } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 2 } \end{array} \right] } ,
$$

then

$$
\mathbf { A } \mathbf { x } = 1 \left[ { 1 } atop { 4 } \right] + 0 \left[ { 2 } \atop { 5 } \right] + 2 \left[ { 3 } \atop { 6 } \right] = { \binom { 7 } { 1 6 } } .
$$

The formula (A.16) for $\mathbf { A x }$ is a linear combination much like the one that occurred in the vector form of a system of equations. It is possible to write any linear system of equations in the form $\mathbf { A x } = \mathbf { b }$ , where $\mathbf { A }$ is a matrix containing the coefficients of the variables in the equations, $\mathbf { b }$ is a vector containing the coefficients on the right-hand sides of the equations, and $\mathbf { x }$ is a vector containing the variables.

Definition A.2 If A is a matrix of size $m$ by $n$ , and $\mathbf { B }$ is a matrix of size $n$ by $r$ , then the product $\mathbf { C } = \mathbf { A } \mathbf { B }$ is obtained by multiplying $\mathbf { A }$ times each of the columns of $\mathbf { B }$ and assembling the matrix vector products in $\mathbf { C }$ :

$$
\mathbf { C } = \bigl [ \mathbf { A } \mathbf { B } . , \mathbf { \partial } _ { 1 } \ \mathbf { A } \mathbf { B } . , 2 \ \cdot \ \cdot \ \mathbf { A } \mathbf { B } . , \bigr ] .
$$

This approach given in (A.20) for calculating a matrix-matrix product will be referred to as the matrix-vector method.

Note that the product (A.20) is only possible if the two matrices are of compatible sizes. If A has m rows and $n$ columns, and $\mathbf { B }$ has $n$ rows and $r$ columns, then the product AB exists and is of size $m$ by $r$ . In some cases, it is thus possible to multiply AB but not BA. It is important to note that when both AB and BA exist, AB is not generally equal to BA!

An alternate way to compute the product of two matrices is the row-column expansion method, where the product element $C _ { i , j }$ is calculated as the matrix product of row $i$ of A and column $j$ of $\mathbf { B }$ .

# Example A.5

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 3 } & { 4 } \\ { 5 } & { 6 } \end{array} \right] }
$$

and

$$
\mathbf { B } = { \left[ \begin{array} { l l } { 5 } & { 2 } \\ { 3 } & { 7 } \end{array} \right] } .
$$

The product matrix $\mathbf { C } = \mathbf { A } \mathbf { B }$ will be of size 3 by 2. We compute the product using both methods. First, using the matrix-vector approach (A.20), we have

$$
\begin{array} { r l } { \mathbf { C } = \left[ \mathbf { A } \mathbf { B } , _ { \cdot 1 } \ \mathbf { A } \mathbf { B } , _ { \cdot 2 } \right] } \\ { = { \left[ 5 \left[ \begin{array} { l } { 1 } \\ { 3 } \\ { 5 } \end{array} \right] } + 3 \left[ \begin{array} { l } { 2 } \\ { 4 } \\ { 6 } \end{array} \right] } & { 2 { \left[ \begin{array} { l } { 1 } \\ { 3 } \\ { 5 } \end{array} \right] } + 7 { \left[ \begin{array} { l } { 2 } \\ { 4 } \\ { 6 } \end{array} \right] } { \right] } } \\ { = { \left[ \begin{array} { l l } { 1 1 } & { 1 6 } \\ { 2 7 } & { 3 4 } \\ { 4 3 } & { 5 2 } \end{array} \right] } . } \end{array}
$$

Next, we use the row-column approach:

$$
{ \begin{array} { r l } & { \mathbf { C } = { \left[ \begin{array} { l l } { 1 \cdot 5 + 2 \cdot 3 } & { 1 \cdot 2 + 2 \cdot 7 } \\ { 3 \cdot 5 + 4 \cdot 3 } & { 3 \cdot 2 + 4 \cdot 7 } \\ { 5 \cdot 5 + 6 \cdot 3 } & { 5 \cdot 2 + 6 \cdot 7 } \end{array} \right] } } \\ & { \mathbf { \Lambda } = { \left[ \begin{array} { l l } { 1 1 } & { 1 6 } \\ { 2 7 } & { 3 4 } \\ { 4 3 } & { 5 2 } \end{array} \right] } . } \end{array} }
$$

Definition A.3 The $n$ by $n$ identity matrix ${ \mathbf I } _ { n }$ is composed of 1s in the diagonal and 0s in the off-diagonal elements.

For example, the 3 by 3 identity matrix is

$$
\mathbf { I } _ { 3 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } .
$$

We often write I without specifying the size of the matrix in situations where the size of matrix is obvious from the context. It is easily shown that if $\mathbf { A }$ is an $m$ by $n$ matrix, then

$$
\begin{array} { c } { \mathbf { A } \mathbf { I } _ { n } = \mathbf { A } } \\ { \mathbf { \Lambda } } \\ { \mathbf { \Lambda } = \mathbf { I } _ { m } \mathbf { A } . } \end{array}
$$

Thus, multiplying by I in matrix algebra is similar to multiplying by 1 in conventional scalar algebra.

We have not defined matrix division, but it is possible at this point to define the matrix algebra equivalent of the reciprocal.

Definition A.4 If A is an $n$ by $n$ matrix, and there is a matrix $\mathbf { B }$ such that

$$
\mathbf { A B } = \mathbf { B A } = \mathbf { I } ,
$$

then $\mathbf { B }$ is the inverse of A. We write $\mathbf { B } = \mathbf { A } ^ { - 1 }$ .

How do we compute the inverse of a matrix? If $\mathbf { A B } = \mathbf { I }$ , then

$$
\left[ \mathbf { A } \mathbf { B } . , _ { 1 } ~ \mathbf { A } \mathbf { B } . , _ { 2 } ~ . ~ . ~ . ~ \mathbf { A } \mathbf { B } . , _ { n } \right] = \mathbf { I } .
$$

Since the columns of the identity matrix and $\mathbf { A }$ are known, we can solve

$$
\mathbf { A B } _ { \cdot , 1 } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] }
$$

to obtain $\mathbf { B } _ { 1 }$ . We can find the remaining columns of the inverse in the same way. If any of these systems of equations are inconsistent, then $\mathbf { A } ^ { - 1 }$ does not exist.

The inverse matrix can be used to solve a system of linear equations with $n$ equations and $n$ variables. Given the system of equations $\mathbf { A x } = \mathbf { b }$ , and $\mathbf { A } ^ { - 1 }$ , we can multiply $\mathbf { A x } = \mathbf { b }$ on both sides by the inverse to obtain

$$
\mathbf { A } ^ { - 1 } \mathbf { A x } = \mathbf { A } ^ { - 1 } \mathbf { b } .
$$

Because

$$
\begin{array} { r } { \mathbf { A } ^ { - 1 } \mathbf { A } \mathbf { x } = \mathbf { I } \mathbf { x } } \\ { = \mathbf { x } , } \end{array}
$$

this gives the solution

$$
\mathbf { x } = \mathbf { A } ^ { - 1 } \mathbf { b } .
$$

This argument shows that if $\mathbf { A } ^ { - 1 }$ exists, then for any right-hand side $\mathbf { b }$ , a system of equations has a unique solution. If $\mathbf { A } ^ { - 1 }$ does not exist, then the system of equations may have either many solutions or no solution.

Definition A.5 When A is an $n$ by $n$ matrix, $\mathbf { A } ^ { k }$ is the product of $k$ copies of A. By convention, we define $\mathbf { A } ^ { 0 } = \mathbf { I }$ .

Definition A.6 The transpose of a matrix A, denoted $\mathbf { A } ^ { T } ,$ , is obtained by taking the columns of A and writing them as the rows of the transpose. We will also use the notation $\mathbf { A } ^ { - T }$ for $( \mathbf { A } ^ { - 1 } ) ^ { T } .$ .

# Example A.6

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 5 } & { 2 } \end{array} \right] } .
$$

Then

$$
\mathbf { A } ^ { T } = { \left[ \begin{array} { l l } { 2 } & { 5 } \\ { 1 } & { 2 } \end{array} \right] } .
$$

Definition A.7 A matrix is symmetric if $\mathbf { A } = \mathbf { A } ^ { T } .$ .

Although many elementary textbooks on linear algebra consider only square diagonal matrices, we will have occasion to refer to $m$ by $n$ matrices that have nonzero elements only on the diagonal.

Definition A.8 An $m$ by $n$ matrix $\mathbf { A }$ is diagonal if $A _ { i , j } = 0$ whenever $i \neq j$ .

Definition A.9 An $m$ by $n$ matrix $\mathbf { R }$ is upper-triangular if $R _ { i , j } = 0$ whenever $i > j$ .   
A matrix $\mathbf { L }$ is lower-triangular if ${ \bf L } ^ { T }$ is upper-triangular.

# Example A.7

The matrix

$$
\mathbf { S } = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 3 } & { 0 } & { 0 } \end{array} \right] }
$$

is diagonal, and the matrix

$$
\mathbf { R } = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 0 } & { 2 } & { 4 } \\ { 0 } & { 0 } & { 5 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] }
$$

is upper-triangular.

Theorem A.1 The following statements are true for any scalars s and t and matrices A, B, and C. It is assumed that the matrices are of the appropriate size for the operations involved and that whenever an inverse occurs, the matrix is invertible.

1. $\mathbf { A } + \mathbf { 0 } = \mathbf { 0 } + \mathbf { A } = \mathbf { A }$ .   
2. $\mathbf { A } + \mathbf { B } = \mathbf { B } + \mathbf { A }$ .   
3. $( \mathbf { A } + \mathbf { B } ) + \mathbf { C } = \mathbf { A } + ( \mathbf { B } + \mathbf { C } )$ .   
4. $\mathbf { A } ( \mathbf { B C } ) = ( \mathbf { A B } ) \mathbf { C }$ .   
5. $\mathbf { A } ( \mathbf { B } + \mathbf { C } ) = \mathbf { A B } + \mathbf { A C }$ .   
6. $( \mathbf { A } + \mathbf { B } ) \mathbf { C } = \mathbf { A } \mathbf { C } + \mathbf { B } \mathbf { C }$ .   
7. $( s t ) \mathbf { A } = s ( t \mathbf { A } )$ .   
8. $s ( \mathbf { A B } ) = ( s \mathbf { A } ) \mathbf { B } = \mathbf { A } ( s \mathbf { B } )$ .   
9. $( s + t ) \mathbf { A } = s \mathbf { A } + t \mathbf { A }$ .   
10. $s ( \mathbf { A } + \mathbf { B } ) = s \mathbf { A } + s \mathbf { B }$ .   
11. $( \mathbf { A } ^ { T } ) ^ { T } = \mathbf { A }$ .   
12. $( s \mathbf { A } ) ^ { T } = s ( \mathbf { A } ^ { T } )$ .   
13. $( \mathbf { A } + \mathbf { B } ) ^ { T } = \mathbf { A } ^ { T } + \mathbf { B } ^ { T } .$   
14. $( \mathbf { A } \mathbf { B } ) ^ { T } = \mathbf { B } ^ { T } \mathbf { A } ^ { T } .$ .   
15. $( \mathbf { A } \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } \mathbf { A } ^ { - 1 } .$ .   
16. $( \mathbf { A } ^ { - 1 } ) ^ { - 1 } = \mathbf { A }$ .   
17. $( \mathbf { A } ^ { T } ) ^ { - 1 } = ( \mathbf { A } ^ { - 1 } ) ^ { T } .$ .   
18. If $\mathbf { A }$ and $\mathbf { B }$ are $n$ by $n$ matrices,

The first 10 rules in this list are identical to rules of conventional algebra, and you should have little trouble in applying them. The rules involving transposes and inverses are new, but they can be mastered without too much trouble.

Some students have difficulty with the following statements, which would appear to be true on the surface, but that are in fact false for at least some matrices.

1. $\mathbf { A } \mathbf { B } = \mathbf { B } \mathbf { A }$ .   
2. If $\mathbf { A } \mathbf { B } = \mathbf { 0 }$ , then $\mathbf { A } = \mathbf { 0 }$ or $\mathbf { B } = \mathbf { 0 }$ .   
3. If $\mathbf { A } \mathbf { B } = \mathbf { A } \mathbf { C }$ and $\mathbf { A } \neq 0$ , then $\mathbf { B } = \mathbf { C }$ .

It is a worthwhile exercise to construct examples of 2 by 2 matrices for which each of these statements is false.

# A.3. LINEAR INDEPENDENCE

Definition A.10 The vectors $\mathbf { v } _ { 1 }$ , $\mathbf { v } _ { 2 }$ , . . . , ${ \bf v } _ { n }$ are linearly independent if the system of equations

$$
c _ { 1 } \mathbf { v } _ { 1 } + c _ { 2 } \mathbf { v } _ { 2 } + \cdot \cdot \cdot + c _ { n } \mathbf { v } _ { n } = \mathbf { 0 }
$$

has only the trivial solution $\mathbf { c } = \mathbf { 0 }$ . If there are multiple solutions, then the vectors are linearly dependent.

Determining whether a set of vectors is linearly independent is simple. Just solve the above system of equations (A.42).

# Example A.8

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \\ { 7 } & { 8 } & { 9 } \end{array} \right] } .
$$

Are the columns of A linearly independent vectors? To determine this we set up the system of equations $\mathbf { A x } = \mathbf { 0 }$ in an augmented matrix, and then find the RREF,

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 2 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } ^ { } { \boldsymbol { 0 } } { \Bigg ] } .
$$

The solutions are

$$
{ \bf x } = x _ { 3 } \left[ \begin{array} { r } { 1 } \\ { - 2 } \\ { 1 } \end{array} \right] .
$$

We can set $x _ { 3 } = 1$ and obtain the nonzero solution,

$$
\mathbf { x } = { \left[ - 2 \right] } { \begin{array} { r } { 1 } \\ { - 2 } \\ { 1 } \end{array} } .
$$

Thus, the columns of A are linearly dependent.

There are a number of important theoretical consequences of linear independence. For example, it can be shown that if the columns of an $n$ by $n$ matrix A are linearly independent, then $\mathbf { A } ^ { - 1 }$ exists, and the system of equations $\mathbf { A x } = \mathbf { b }$ has a unique solution for every right-hand side $\mathbf { b }$ [95].

# A.4. SUBSPACES OF $\pmb { R } ^ { n }$

So far, we have worked with vectors of real numbers in the $n$ -dimensional space $R ^ { n } .$ . There are a number of properties of $R ^ { n }$ that make it convenient to work with vectors. First, the operation of vector addition always works. We can take any two vectors in $R ^ { n }$ and add them together and get another vector in $R ^ { n } .$ Second, we can multiply any vector in $R ^ { n }$ by a scalar and obtain another vector in $R ^ { n } .$ . Finally, we have the 0 vector, with the property that for any vector $\mathbf { x }$ , $\mathbf { x } + \mathbf { 0 } = \mathbf { 0 } + \mathbf { x } = \mathbf { x }$ .

Definition A.11 A subspace $W$ of $R ^ { n }$ is a subset of $R ^ { n }$ that satisfies the three properties:

1. If $\mathbf { x }$ and $\mathbf { y }$ are vectors in $W$ , then $\mathbf x + \mathbf y$ is also a vector in $W$ . 2. If $\mathbf { x }$ is a vector in $W$ and $s$ is any real scalar, then $s \mathbf { x }$ is also a vector in $W$ . 3. The 0 vector is in $W$ . A subspace of $R ^ { n }$ is nontrivial if it contains vectors other than the 0 vector.

# Example A.9

In $R ^ { 3 }$ , the plane $P$ defined by the equation

$$
x _ { 1 } + x _ { 2 } + x _ { 3 } = 0
$$

is a subspace of $R ^ { n } .$ . To see this, note that if we take any two vectors in the plane and add them together, we get another vector in the plane. If we take a vector in this plane and multiply it by any scalar, we get another vector in the plane. Finally, 0 is a vector in the plane.

Subspaces are important because they provide an environment within which all of the rules of matrix-vector algebra apply. An especially important subspace of $R ^ { n }$ that we will work with is the null space of an $m$ by $n$ matrix.

Definition A.12 Let A be an $m$ by $n$ matrix. The null space of $\mathbf { A }$ , written $N ( \mathbf { A } )$ , is the set of all vectors $\mathbf { x }$ such that $\mathbf { A x } = \mathbf { 0 }$ .

To show that $N ( \mathbf { A } )$ is actually a subspace of $R ^ { n }$ , we need to show that:

1. If $\mathbf { x }$ and $\mathbf { y }$ are in $N ( \mathbf { A } )$ , then $\mathbf { A x } = \mathbf { 0 }$ and $\mathbf { A } \mathbf { y } = \mathbf { 0 }$ . By adding these equations, we find that $\mathbf { A } ( \mathbf { x } + \mathbf { y } ) = \mathbf { 0 }$ . Thus $\mathbf x + \mathbf y$ is in $N ( \mathbf { A } )$ .

2. If $\mathbf { x }$ is in $N ( \mathbf { A } )$ and $s$ is any scalar, then $\mathbf { A x } = \mathbf { 0 }$ . We can multiply this equation by s to get $s \mathbf { A } \mathbf { x } = \mathbf { 0 }$ . Thus $\mathbf { A } ( s \mathbf { x } ) = \mathbf { 0 }$ , and $s \mathbf { x }$ is in $N ( \mathbf { A } )$ .

3. $\mathbf { A } \mathbf { 0 } = \mathbf { 0 }$ , so 0 is in $N ( \mathbf { A } )$

Computationally, the null space of a matrix can be determined by solving the system of equations $\mathbf { A x } = \mathbf { 0 }$ .

# Example A.10

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l l l } { 3 } & { 1 } & { 9 } & { 4 } \\ { 2 } & { 1 } & { 7 } & { 3 } \\ { 5 } & { 2 } & { 1 6 } & { 7 } \end{array} \right] } .
$$

To find the null space of A, we solve the system of equations $\mathbf { A x } = \mathbf { 0 }$ . To solve the equations, we put the system of equations into an augmented matrix,

$$
{ \left[ \begin{array} { l l l l l } { 3 } & { 1 } & { 9 } & { 4 } \\ { 2 } & { 1 } & { 7 } & { 3 } \\ { 5 } & { 2 } & { 1 6 } & { 7 } \end{array} \right] } ^ { 0 } { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } ,
$$

and find the RREF,

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 3 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } .
$$

From the augmented matrix, we find that

$$
\mathbf { x } = x _ { 3 } \left[ { - 3 \atop 1 } \right] + x _ { 4 } \left[ { - 1 \atop 0 } \right] .
$$

Any vector in the null space can be written as a linear combination of the above vectors, so the null space is a two-dimensional plane within $R ^ { 4 }$ .

Now, consider the problem of solving $\mathbf { A x } = \mathbf { b }$ , where

$$
\mathbf { b } = { \left[ \begin{array} { l } { 2 2 } \\ { 1 7 } \\ { 3 9 } \end{array} \right] }
$$

and one particular solution is

$$
\mathbf { p } = { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 1 } \\ { 2 } \end{array} \right] } .
$$

We can take any vector in the null space of $\mathbf { A }$ and add it to this solution to obtain another solution. Suppose that $\mathbf { x }$ is in $N ( \mathbf { A } )$ . Then

$$
\begin{array} { r l } & { \mathbf { A } ( \mathbf { x } + \mathbf { p } ) = \mathbf { A } \mathbf { x } + \mathbf { A } \mathbf { p } } \\ & { ~ \mathbf { A } ( \mathbf { x } + \mathbf { p } ) = \mathbf { 0 } + \mathbf { b } } \\ & { ~ \mathbf { A } ( \mathbf { x } + \mathbf { p } ) = \mathbf { b } . } \end{array}
$$

For example,

$$
\mathbf { x } = \left[ { 2 \atop 1 } \right] + 2 \left[ { - 3 \atop 1 } \right] + 3 \left[ { - 1 \atop 0 } \right]
$$

is also a solution to $\mathbf { A x } = \mathbf { b }$ .

In the context of inverse problems, the null space is critical because the presence of a nontrivial null space leads to nonuniqueness in the solution to a linear system of equations.

Definition A.13 A basis for a subspace $W$ is a set of vectors $\mathbf { v } _ { 1 } , \ldots . . . , \mathbf { v } _ { p }$ such that:

1. Any vector in $W$ can be written as a linear combination of the basis vectors.

2. The basis vectors are linearly independent.

A particularly simple and useful basis is the standard basis.

Definition A.14 The standard basis for $R ^ { n }$ is the set of vectors $\mathbf { e } _ { 1 } , \ldots . . . , \mathbf { e } _ { n }$ such that the elements of $\mathbf { e } _ { i }$ are all zero except for the ith element, which is 1.

Any nontrivial subspace $W$ of $R ^ { n }$ will have many different bases. For example, we can take any basis and multiply one of the basis vectors by 2 to obtain a new basis. It is possible to show that all bases for a subspace $W$ have the same number of basis vectors [95].

Theorem A.2 Let $W$ be a subspace of $R ^ { n }$ with basis $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots . \mathbf { \ v } _ { p }$ . Then all bases for $W$ have $p$ basis vectors, and $p$ is the dimension of $W$ .

It can be shown that the procedure used in the above example always produces a basis for $N ( \mathbf { A } )$ [95]. A basis for the null space of a matrix can be found in MATLAB using the null command.

Definition A.15 Let A be an $m$ by $n$ matrix. The column space or range of A (written $R ( \mathbf { A } ) )$ ) is the set of all vectors $\mathbf { b }$ such that $\mathbf { A x } = \mathbf { b }$ has at least one solution. In other words, the column space is the set of all vectors $\mathbf { b }$ that can be written as a linear combination of the columns of A.

The range is important in the context of discrete linear inverse problems, because $R ( \mathbf G )$ consists of all vectors $\mathbf { d }$ for which there is a model $\mathbf { m }$ such that $\mathbf { G m } = \mathbf { d }$ .

To find the column space of a matrix, we consider what happens when we compute the RREF of $\left[ \mathbf { A } \mid \mathbf { b } \right]$ . In the part of the augmented matrix corresponding to the lefthand side of the equations we always get the same result, namely the RREF of A. The solution to the system of equations may involve some free variables, but we can always set these free variables to 0. Thus when we are able to solve $\mathbf { A x } = \mathbf { b }$ , we can solve the system of equations by using only variables corresponding to the pivot columns in the RREF of A. In other words, if we can solve $\mathbf { A x } = \mathbf { b }$ , then we can write $\mathbf { b }$ as a linear combination of the pivot columns of A. Note that these are columns from the original matrix A, not columns from the RREF of A. An orthonormal (see below) basis for the range of a matrix can be found in MATLAB using the orth command.

# Example A.11

As in the previous example, let

$$
\mathbf { A } = { \left[ \begin{array} { l l l l } { 3 } & { 1 } & { 9 } & { 4 } \\ { 2 } & { 1 } & { 7 } & { 3 } \\ { 5 } & { 2 } & { 1 6 } & { 7 } \end{array} \right] } .
$$

To find the column space of $\mathbf { A }$ , note that the RREF of $\mathbf { A }$ is

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 3 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } .
$$

Thus, whenever we can solve $\mathbf { A x } = \mathbf { b }$ , we can find a solution in which $x _ { 3 }$ and $x _ { 4 }$ are 0. In other words, whenever there is a solution to $\mathbf { A x } = \mathbf { b }$ , we can write $\mathbf { b }$ as a linear combination of the first two columns of A:

$$
\mathbf { b } = x _ { 1 } { \left[ \begin{array} { l } { 3 } \\ { 2 } \\ { 5 } \end{array} \right] } + x _ { 2 } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 2 } \end{array} \right] } .
$$

Since these two vectors are linearly independent and span $R ( \mathbf { A } )$ , they form a basis for $R ( \mathbf { A } )$ . The dimension of $R ( \mathbf { A } )$ is 2.

In finding the null space and range of a matrix A, we found that the basis vectors for $N ( \mathbf { A } )$ corresponded to nonpivot columns of A, while the basis vectors for $R ( \mathbf { A } )$ corresponded to pivot columns of A. Since the matrix $\mathbf { A }$ had $n$ columns, we obtain the following theorem.

# Theorem A.3

$$
d i m ~ N ( { \bf A } ) + d i m ~ R ( { \bf A } ) = n .
$$

In addition to the null space and range of a matrix $\mathbf { A }$ , we will often work with the null space and range of the transpose of A. Since the columns of $\mathbf { A } ^ { T }$ are rows of $\mathbf { A }$ , the column space of $\mathbf { A } ^ { T }$ is also called the row space of A. Since each row of A can be written as a linear combination of the nonzero rows of the RREF of A, the nonzero rows of the RREF form a basis for the row space of A. There are exactly as many nonzero rows in the RREF of A as there are pivot columns. Thus we have the following theorem.

# Theorem A.4

$$
d i m ( R ( { \bf A } ^ { T } ) ) = d i m ~ R ( { \bf A } ) .
$$

Definition A.16 The rank of an $m$ by $n$ matrix $\mathbf { A }$ is the dimension of $R ( \mathbf { A } )$ . If $\mathrm { r a n k } ( \mathbf { A } ) = \operatorname* { m i n } ( m , n )$ , then A has full rank. If ${ \mathrm { r a n k } } ( \mathbf { A } ) = m$ , then A has full row rank. If $\operatorname { r a n k } ( \mathbf { A } ) = n$ , then $\mathbf { A }$ has full column rank. If $\operatorname { r a n k } ( \mathbf { A } ) < \operatorname* { m i n } ( m , n )$ , then A is rank deficient.

The rank of a matrix is readily found in MATLAB by using the rank command.

# A.5. ORTHOGONALITY AND THE DOT PRODUCT

Definition A.17 Let $\mathbf { x }$ and $\mathbf { y }$ be two vectors in $R ^ { n } .$ . The dot product of $\mathbf { x }$ and $\mathbf { y }$ is

$$
\mathbf { x } \cdot \mathbf { y } = \mathbf { x } ^ { T } \mathbf { y } = x _ { 1 } \gamma _ { 1 } + x _ { 2 } \gamma _ { 2 } + \cdot \cdot \cdot + x _ { n } \gamma _ { n } .
$$

Definition A.18 Let $\mathbf { x }$ be a vector in $R ^ { n } .$ . The 2-norm or Euclidean length of $\mathbf { x }$ is

$$
\| \mathbf { x } \| _ { 2 } = \sqrt { \mathbf { x } ^ { T } \mathbf { x } } = \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { 2 } } .
$$

Later we will introduce two other ways of measuring the “length” of a vector. The subscript 2 is used to distinguish this 2-norm from the other norms.

You may be familiar with an alternative definition of the dot product in which $\mathbf { x } \cdot \mathbf { y } =$ $\| \mathbf { x } \| \| \mathbf { y } \| \cos ( \theta )$ , where $\theta$ is the angle between the two vectors. The two definitions are equivalent. To see this, consider a triangle with sides $\mathbf { x }$ , y, and $\mathbf x - \mathbf y$ . See Figure A.1.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/4ef469f2c7af9330024908cd6b8ea828be0d048cc2d6bf538b7886845063b918.jpg)  
Figure A.1 Relationship between the dot product and the angle between two vectors.

The angle between sides $\mathbf { x }$ and $\mathbf { y }$ is $\theta$ . By the law of cosines,

$$
\begin{array} { c } { \| \mathbf { x } - \mathbf { y } \| _ { 2 } ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } + \| \mathbf { y } \| _ { 2 } ^ { 2 } - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \ \qquad ( \mathbf { x } - \mathbf { y } ) ^ { T } ( \mathbf { x } - \mathbf { y } ) = \mathbf { x } ^ { T } \mathbf { x } + \mathbf { y } ^ { T } \mathbf { y } - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \mathbf { x } ^ { T } \mathbf { x } - 2 \mathbf { x } ^ { T } \mathbf { y } + \mathbf { y } ^ { T } \mathbf { y } = \mathbf { x } ^ { T } \mathbf { x } + \mathbf { y } ^ { T } \mathbf { y } - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \ \qquad - 2 \mathbf { x } ^ { T } \mathbf { y } = - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \mathbf { x } ^ { T } \mathbf { y } = \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) . } \end{array}
$$

We can also use this formula to compute the angle between two vectors:

$$
\theta = \cos ^ { - 1 } \left( \frac { \mathbf { x } ^ { T } \mathbf { y } } { \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } } \right) .
$$

Definition A.19 Two vectors $\mathbf { x }$ and $\mathbf { y }$ in $R ^ { n }$ are orthogonal, or equivalently, perpendicular (written $\mathbf { x } \perp \mathbf { y } )$ ), if $\mathbf { x } ^ { T } \mathbf { y } = 0$ .

Definition A.20 A set of vectors $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots . \mathbf { v } _ { p }$ is orthogonal if each pair of vectors in the set is orthogonal.

Definition A.21 Two subspaces $V$ and $W$ of $R ^ { n }$ are orthogonal if every vector in $V$ is perpendicular to every vector in $W$ .

If $\mathbf { x }$ is in $N ( \mathbf { A } )$ , then $\mathbf { A x } = \mathbf { 0 }$ . Since each element of the product Ax can be obtained by taking the dot product of a row of $\mathbf { A }$ and $\mathbf { x } , \mathbf { x }$ is perpendicular to each row of A. Since $\mathbf { x }$ is perpendicular to all of the columns of $\mathbf { A } ^ { T }$ , it is perpendicular to $R ( \mathbf { A } ^ { T } )$ . We have the following theorem.

Theorem A.5 Let A be an m by n matrix. Then

$$
N ( \mathbf { A } ) \perp R ( \mathbf { A } ^ { T } ) .
$$

Furthermore,

$$
\begin{array} { r } { N ( { \bf A } ) + R ( { \bf A } ^ { T } ) = R ^ { n } . } \end{array}
$$

That is, any vector $\mathbf { x }$ in $R ^ { n }$ can be written uniquely as $\mathbf { x } = \mathbf { p } + \mathbf { q }$ , where $\mathbf { p }$ is in $N ( \mathbf { A } )$ and $\mathbf { q }$ is in $R ( \mathbf { A } ^ { T } )$ .

Definition A.22 A basis in which the basis vectors are orthogonal is an orthogonal basis. A basis in which the basis vectors are orthogonal and have length 1 is an orthonormal basis.

Definition A.23 An $n$ by $n$ matrix $\mathbf { Q }$ is orthogonal if the columns of $\mathbf { Q }$ are orthogonal and each column of $\mathbf { Q }$ has length 1.

With the requirement that the columns of an orthogonal matrix have length 1, using the term “orthonormal” would make logical sense. However, the definition of “orthogonal” given here is standard and we will not try to change standard usage.

Orthogonal matrices have a number of useful properties.

Theorem A.6 If $\mathbf { Q }$ is an orthogonal matrix, then:

1. $\mathbf { Q } ^ { T } \mathbf { Q } = \mathbf { Q } \mathbf { Q } ^ { T } = \mathbf { I }$ . In other words, $\mathbf { Q } ^ { - 1 } = \mathbf { Q } ^ { T }$ .   
2. For any vector $\mathbf { x }$ in $R ^ { n }$ , $\| \mathbf { Q x } \| _ { 2 } = \| \mathbf { x } \| _ { 2 } .$ .   
3. For any two vectors $\mathbf { x }$ and $\mathbf { y }$ in $R ^ { n }$ , $\mathbf { x } ^ { T } \mathbf { y } = ( \mathbf { Q } \mathbf { x } ) ^ { T } ( \mathbf { Q } \mathbf { y } ) .$

A problem that we will often encounter in practice is projecting a vector $\mathbf { x }$ onto another vector $\mathbf { y }$ or onto a subspace $W$ to obtain a projected vector $\mathbf { p }$ . See Figure A.2. We know that

$$
\mathbf { x } ^ { T } \mathbf { y } = \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) ,
$$

where $\theta$ is the angle between $\mathbf { x }$ and $\mathbf { y }$ . Also,

$$
\cos ( \theta ) = { \frac { \| \mathbf { p } \| _ { 2 } } { \| \mathbf { x } \| _ { 2 } } } .
$$

Thus

$$
\| \mathbf { p } \| _ { 2 } = { \frac { \mathbf { x } ^ { T } \mathbf { y } } { \| \mathbf { y } \| _ { 2 } } } .
$$

Since $\mathbf { p }$ points in the same direction as $\mathbf { y }$ ,

$$
\mathbf { p } = \operatorname { p r o j } _ { \mathbf { y } } \mathbf { x } = { \frac { \mathbf { x } ^ { T } \mathbf { y } } { \mathbf { y } ^ { T } \mathbf { y } } } \mathbf { y } .
$$

The vector $\mathbf { p }$ is called the orthogonal projection or simply the projection of $\mathbf { x }$ onto $\mathbf { y }$ .

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/315cf57af580e29fc10670f9126c7f2d87b2f7dcb6ad9ab9475fa08c0e74884b.jpg)  
Figure A.2 The orthogonal projection of $\mathbf { x }$ onto y.

Similarly, if $W$ is a subspace of $R ^ { n }$ with an orthogonal basis $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , \ldots . \mathbf { \mu } . \mathbf { w } _ { p } ,$ , then the orthogonal projection of $\mathbf { x }$ onto $W$ is

$$
\mathbf { p } = \mathrm { p r o j } _ { W } \mathbf { x } = \frac { \mathbf { x } ^ { T } \mathbf { w } _ { 1 } } { \mathbf { w } _ { 1 } ^ { T } \mathbf { w } _ { 1 } } \mathbf { w } _ { 1 } + \frac { \mathbf { x } ^ { T } \mathbf { w } _ { 2 } } { \mathbf { w } _ { 2 } ^ { T } \mathbf { w } _ { 2 } } \mathbf { w } _ { 2 } + \cdot \cdot \cdot + \frac { \mathbf { x } ^ { T } \mathbf { w } _ { p } } { \mathbf { w } _ { p } ^ { T } \mathbf { w } _ { p } } \mathbf { w } _ { p } .
$$

Note that this equation can be simplified considerably if the orthogonal basis vectors are also orthonormal. In that case, $\mathbf { w } _ { 1 } ^ { \bar { T } } \mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } ^ { T } \mathbf { w } _ { 2 } , \ldots . . . , \mathbf { w } _ { p } ^ { T } \mathbf { w } _ { p }$ are all 1.

It is inconvenient that the projection formula requires an orthogonal basis. The Gram-Schmidt orthogonalization process can be used to turn any basis for a subspace of $R ^ { n }$ into an orthogonal basis. We begin with a basis $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots . \mathbf { \mu } , \mathbf { v } _ { p } $ . The process recursively constructs an orthogonal basis by taking each vector in the original basis and then subtracting off its projection on the space spanned by the previous vectors. The formulas are

$$
\mathbf { w } _ { 1 } = \mathbf { v } _ { 1 }
$$

$$
\begin{array} { r } { \mathbf { w } _ { 2 } = \mathbf { v } _ { 2 } - \frac { \mathbf { v } _ { 1 } ^ { T } \mathbf { v } _ { 2 } } { \mathbf { v } _ { 1 } ^ { T } \mathbf { v } _ { 1 } } \mathbf { v } _ { 1 } = \mathbf { v } _ { 2 } - \frac { \mathbf { w } _ { 1 } ^ { T } \mathbf { v } _ { 2 } } { \mathbf { w } _ { 1 } ^ { T } \mathbf { w } _ { 1 } } \mathbf { w } _ { 1 } } \end{array}
$$

$$
\mathbf { w } _ { p } = \mathbf { v } _ { p } - { \frac { \mathbf { w } _ { 1 } ^ { T } \mathbf { v } _ { p } } { \mathbf { w } _ { 1 } ^ { T } \mathbf { w } _ { 1 } } } \mathbf { w } _ { 1 } - \cdot \cdot \cdot - { \frac { \mathbf { w } _ { p } ^ { T } \mathbf { v } _ { p } } { \mathbf { w } _ { p } ^ { T } \mathbf { w } _ { p } } } \mathbf { w } _ { p } .
$$

Unfortunately, the Gram-Schmidt process is numerically unstable when applied to large bases. In MATLAB the command orth provides a numerically stable way to produce an orthogonal basis from a nonorthogonal basis. An important property of orthogonal projection is that the projection of $\mathbf { x }$ onto $W$ is the point in $W$ which is closest to $\mathbf { x }$ . In the special case that $\mathbf { x }$ is in $W$ , the projection of $\mathbf { x }$ onto $W$ is $\mathbf { x }$ .

Given an inconsistent system of equations $\mathbf { A x } = \mathbf { b }$ , it is often desirable to find an approximate solution. A natural measure of the quality of an approximate solution is the norm of the difference between Ax and $\mathbf { b }$ , $\| \mathbf { A x } - \mathbf { b } \|$ . A solution that minimizes the 2-norm, $\| \mathbf { A x } - \mathbf { b } \| _ { 2 }$ , is called a least squares solution, because it minimizes the sum of the squares of the residuals.

The least squares solution can be obtained by projecting $\mathbf { b }$ onto $R ( \mathbf { A } )$ . This calculation requires us to first find an orthogonal basis for $R ( \mathbf { A } )$ . There is an alternative approach that does not require finding an orthogonal basis. Let

$$
\mathbf { A } \mathbf { x } _ { l s } = \mathrm { p r o j } _ { R ( \mathbf { A } ) } \mathbf { b } .
$$

Then, the difference between the projection (A.71) and $\mathbf { b }$ , $\mathbf { A x } _ { l s } - \mathbf { b }$ , will be perpendicular to $R ( \mathbf { A } )$ (Figure A.3). This orthogonality means that each of the columns of A will be orthogonal to $\mathbf { A x } _ { l s } - \mathbf { b }$ . Thus

$$
\mathbf { A } ^ { T } ( \mathbf { A x } _ { l s } - \mathbf { b } ) = \mathbf { 0 }
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/466c3f0ffd37487759cd3359e2ca975d7cf47f0abdb257606c1227c0ecb023f9.jpg)  
Figure A.3 Geometric conceptualization of the least squares solution to $\mathbf { A } \mathbf { x } = \mathbf { b }$ . b generally lies in $R ^ { m }$ , but $R ( \mathbf { A } )$ is generally a subspace of $R ^ { m }$ . The least squares solution $\mathbf { x } _ { l s }$ minimizes $\| \mathbf { A x } - \mathbf { b } \| _ { 2 }$ .

or

$$
\mathbf { A } ^ { T } \mathbf { A x } _ { l s } = \mathbf { A } ^ { T } \mathbf { b } .
$$

This last system of equations is referred to as the normal equations for the least squares problem. It can be shown that if the columns of $\mathbf { A }$ are linearly independent, then the normal equations have exactly one solution for $\mathbf { x } _ { l s }$ and this solution minimizes the sum of squared residuals [95].

# A.6. EIGENVALUES AND EIGENVECTORS

Definition A.24 An $n$ by $n$ matrix A has an eigenvalue $\lambda$ with an associated eigenvector $\mathbf { x }$ if $\mathbf { x }$ is not 0, and

$$
\mathbf { A } \mathbf { x } = \lambda \mathbf { x } .
$$

To find eigenvalues and eigenvectors, we rewrite the eigenvector equation (A.74) as

$$
( \mathbf { A } - \lambda \mathbf { I } ) \mathbf { x } = \mathbf { 0 } .
$$

To find nonzero eigenvectors, the matrix $\mathbf { A } - \lambda \mathbf { I }$ must be singular. This leads to the characteristic equation,

$$
\operatorname* { d e t } ( \mathbf { A } - \lambda \mathbf { I } ) = 0 .
$$

where det denotes the determinant. For small matrices (e.g., 2 by 2 or 3 by 3), it is relatively easy to solve (A.76) to find the eigenvalues. The eigenvalues can then be substituted into (A.75), and the resulting system can then be solved to find corresponding eigenvectors. Note that the eigenvalues can, in general, be complex. For larger matrices, solving the characteristic equation becomes impractical and more sophisticated numerical methods are used. The MATLAB command eig can be used to find eigenvalues and eigenvectors of a matrix.

Suppose that we can find a set of $n$ linearly independent eigenvectors, $\mathbf { v } _ { i }$ , of an $n$ by $n$ matrix A with associated eigenvalues $\lambda _ { i }$ . These eigenvectors form a basis for $R ^ { n } .$ . We can use the eigenvectors to diagonalize the matrix as

$$
\mathbf { A } = \mathbf { P } \mathbf { A } \mathbf { P } ^ { - 1 } ,
$$

where

$$
\mathbf { P } = \left[ \mathbf { v } _ { 1 } \quad \mathbf { v } _ { 2 } \quad \ldots \quad \mathbf { v } _ { n } \right] ,
$$

and $\pmb { \Lambda }$ is a diagonal matrix of eigenvalues

$$
\Lambda _ { i i } = \lambda _ { i } .
$$

To see that this works, simply compute AP:

$$
\begin{array} { r l } { \mathbf { A P } = \mathbf { A } \left[ \mathbf { v } _ { 1 } \quad \mathbf { v } _ { 2 } \quad . ~ . ~ . ~ \mathbf { v } _ { n } \right] } & { } \\ { = \left[ \lambda _ { 1 } \mathbf { v } _ { 1 } \quad \lambda _ { 2 } \mathbf { v } _ { 2 } \quad . ~ . ~ . ~ \lambda _ { n } \mathbf { v } _ { n } \right] } & { } \\ { = \mathbf { P A } . } \end{array}
$$

Thus, $\mathbf { A } = \mathbf { P } \pmb { \Lambda } \mathbf { P } ^ { - 1 } ,$ . Not all matrices are diagonalizable, because not all matrices have $n$ linearly independent eigenvectors. However, there is an important special case in which matrices can always be diagonalized.

Theorem A.7 If A is a real symmetric matrix, then A can be written as

$$
\mathbf { A } = \mathbf { Q } \mathbf { A } \mathbf { Q } ^ { - 1 } = \mathbf { Q } \mathbf { A } \mathbf { Q } ^ { T } ,
$$

where $\mathbf { Q }$ is a real orthogonal matrix of eigenvectors of $\mathbf { A }$ , and $\pmb { \Lambda }$ is a real diagonal matrix of the eigenvalues of A.

This orthogonal diagonalization of a real symmetric matrix A will be useful later on when we consider orthogonal factorizations of general matrices.

The eigenvalues of symmetric matrices are particularly important in the analysis of quadratic forms.

Definition A.25 A quadratic form is a function of the form

$$
f ( \mathbf { x } ) = \mathbf { x } ^ { T } \mathbf { A } \mathbf { x } ,
$$

where $\mathbf { A }$ is a symmetric $n \times n$ matrix. The quadratic form $f ( \mathbf { x } )$ is positive definite if $f ( x ) \geq 0$ for all $\mathbf { x }$ and $f ( \mathbf { x } ) = 0$ only when $\mathbf { x } = \mathbf { 0 }$ . The quadratic form is positive semidefinite if $f ( \mathbf { x } ) \geq 0$ for all $\mathbf { x }$ . Similarly, a symmetric matrix A is positive definite if the associated quadratic form $f ( \mathbf { x } ) = \mathbf { x } ^ { T } \mathbf { A } \mathbf { x }$ is positive definite. The quadratic form is negative semidefinite if $- f ( \mathbf { x } )$ is positive semidefinite. If $f ( \mathbf { x } )$ is neither positive semidefinite nor negative semidefinite, then $f ( \mathbf { x } )$ is indefinite.

Positive definite quadratic forms have an important application in analytic geometry. Let A be a symmetric and positive definite matrix. Then the region defined by the inequality

$$
( \mathbf { x } - \mathbf { c } ) ^ { T } \mathbf { A } ( \mathbf { x } - \mathbf { c } ) \leq \delta
$$

is an ellipsoidal volume, with its center at c. We can diagonalize $\mathbf { A }$ as

$$
\mathbf { A } = \mathbf { P } \mathbf { A } \mathbf { P } ^ { - 1 } ,
$$

where the columns of $\mathbf { P }$ are normalized eigenvectors of $\mathbf { A }$ , and $\pmb { \Lambda }$ is a diagonal matrix whose elements are the eigenvalues of A. It can be shown that the ith eigenvector of A points in the direction of the ith semimajor axis of the ellipsoid, and the length of the√ ith semimajor axis is given by $\sqrt { \delta / \lambda _ { i } }$ [95].

An important connection between positive semidefinite matrices and eigenvalues is the following theorem.

Theorem A.8 $A$ symmetric matrix A is positive semidefinite if and only if its eigenvalues are greater than or equal to 0. A is positive definite if and only if its eigenvalues are greater than 0.

This provides a convenient way to check whether a symmetric matrix is positive semidefinite or positive definite.

The Cholesky factorization provides another way to determine whether a symmetric matrix is positive definite.

Theorem A.9 Let A be an an n by $n$ positive definite and symmetric matrix. Then A can be written uniquely as

$$
\mathbf { A } = \mathbf { R } ^ { T } \mathbf { R } = \mathbf { L } \mathbf { L } ^ { T } ,
$$

where R is a nonsingular upper-triangular matrix and ${ \bf L } = { \bf R } ^ { T }$ is a nonsingular lower-triangular matrix. Note that A can be factored in this way if and only if it is positive definite.

The MATLAB command chol can be used to compute the Cholesky factorization.

# A.7. VECTOR AND MATRIX NORMS

Although the conventional Euclidean length (A.61) is most commonly used, there are alternative ways to measure the length of a vector.

Definition A.26 Any measure of vector length satisfying the following four conditions is called a norm.

1. For any vector $\mathbf { x }$ , $\| \mathbf { x } \| \geq 0$ .   
2. For any vector $\mathbf { x }$ and any scalar $s$ , $\| s \mathbf { x } \| = | s | \| \mathbf { x } \|$ .   
3. For any vectors $\mathbf { x }$ and $\mathbf { y }$ , $\| \mathbf { x } + \mathbf { y } \| \leq \| \mathbf { x } \| + \| \mathbf { y } \|$ .   
4. $\| \mathbf { x } \| = 0$ if and only if $\mathbf { x } = \mathbf { 0 }$ .

If $\Vert { \big \vert } { \big \vert } $ satisfies conditions 1, 2, and 3, but does not satisfy condition 4, then $\Vert { \big \vert } { \big \Vert }$ is called a seminorm.

Definition A.27 The $p$ -norm of a vector in $R ^ { n }$ is defined for $p \geq 1$ by

$$
\| x \| _ { p } = ( | x _ { 1 } | ^ { p } + | x _ { 2 } | ^ { p } + \cdot \cdot \cdot + | x _ { n } | ^ { p } ) ^ { 1 / p } .
$$

It can be shown that for any $p \geq 1$ , (A.85) satisfies the conditions of Definition A.26 [53]. The conventional Euclidean length is just the 2-norm, but two other $p$ -norms are also commonly used. The 1-norm is the sum of the absolute values of the elements in $\mathbf { x }$ . The $\infty$ -norm is obtained by taking the limit as $p$ goes to infinity. The $\infty$ -norm is the maximum of the absolute values of the elements in $\mathbf { x }$ . The MATLAB command norm can be used to compute the norm of a vector, and has options for the 1, 2, and infinity norms.

The 2-norm is particularly important because of its natural connection with dot products and projections. The projection of a vector onto a subspace is the point in the subspace that is closest to the vector as measured by the 2-norm. We have also seen in (A.73) that the problem of minimizing $\| \mathbf { A x } - \mathbf { b } \| _ { 2 }$ can be solved by computing projections or by using the normal equations. In fact, the 2-norm can be tied directly to the dot product by the formula

$$
\| \mathbf { x } \| _ { 2 } = { \sqrt { \mathbf { x } ^ { T } \mathbf { x } } } .
$$

The $1 -$ and $\infty$ -norms can also be useful in finding approximate solutions to overdetermined linear systems of equations. To minimize the maximum of the residuals, we minimize $\| \mathbf { A x - b } \| _ { \infty }$ . To minimize the sum of the absolute values of the residuals, we minimize $\| \mathbf { A x } - \mathbf { b } \| _ { 1 }$ . Unfortunately, these minimization problems are generally more difficult to solve than least squares problems.

Definition A.28 Any measure of the size or length of an $m$ by $n$ matrix that satisfies the following five properties can be used as a matrix norm.

1. For any matrix A, $\| \mathbf { A } \| \geq 0$ .   
2. For any matrix $\mathbf { A }$ and any scalar $s$ , $\| s \mathbf { A } \| = | s | \| \mathbf { A } \|$ .   
3. For any matrices A and $\mathbf { B }$ , $\| \mathbf { A + B } \| \leq \| \mathbf { A } \| + \| \mathbf { B } \|$ .   
4. $\| \mathbf { A } \| = 0$ if and only if $\mathbf { A } = \mathbf { 0 }$ .   
5. For any two matrices A and $\mathbf { B }$ of compatible sizes, $\| \mathbf { A B } \| \leq \| \mathbf { A } \| \| \mathbf { B } \|$ .

Definition A.29 The $p$ -norm of a matrix A is

$$
\| \mathbf { A } \| _ { p } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { p } = 1 } \| \mathbf { A } \mathbf { x } \| _ { p } ,
$$

where $\left\| \mathbf { x } \right\| _ { p }$ and $\| \mathbf { A x } \| _ { p }$ are vector $p .$ -norms, while $\| \mathbf { A } \| _ { p }$ is the matrix $p$ -norm of A.

Solving the maximization problem of (A.87) to determine a matrix $p .$ -norm could be extremely difficult. Fortunately, there are simpler formulas for the most commonly used matrix $p$ -norms. See Exercises A.11, A.12, and C.4:

$$
\begin{array} { r } { \| \mathbf { A } \| _ { 1 } = \displaystyle \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | } \\ { \| \mathbf { A } \| _ { 2 } = \sqrt { \lambda _ { \operatorname* { m a x } } ( \mathbf { A } ^ { T } \mathbf { A } ) } } \\ { \| \mathbf { A } \| _ { \infty } = \displaystyle \operatorname* { m a x } _ { i } \sum _ { j = 1 } ^ { n } | A _ { i , j } | , } \end{array}
$$

where $\lambda _ { \operatorname* { m a x } } ( \mathbf { A } ^ { T } \mathbf { A } )$ denotes the largest eigenvalue of $\mathbf { A } ^ { T } \mathbf { A }$ .

Definition A.30 The Frobenius norm of an $m$ by $n$ matrix is given by

$$
\| \mathbf { A } \| _ { F } = \sqrt { \sum _ { i = 1 } ^ { m } \sum _ { j = 1 } ^ { n } A _ { i , j } ^ { 2 } } .
$$

Definition A.31 A matrix norm $\parallel \parallel _ { M }$ and a vector norm $\Vert \big | \big | \big | \big | \big | \big | \big | \big | \big |$ are compatible if

$$
\left\| \mathbf { A x } \right\| _ { V } \leq \left\| \mathbf { A } \right\| _ { M } \left\| \mathbf { x } \right\| _ { V } .
$$

The matrix $p$ -norm is by its definition compatible with the vector $p$ -norm from which it was derived. It can also be shown that the Frobenius norm of a matrix is compatible with the vector 2-norm [109]. Thus the Frobenius norm is often used with the vector 2-norm.

In practice, the Frobenius norm, 1-norm, and $\infty \cdot$ -norm of a matrix are easy to compute, while the 2-norm of a matrix can be difficult to compute for large matrices. The MATLAB norm command has options for computing these matrix norms.

# A.8. THE CONDITION NUMBER OF A LINEAR SYSTEM

Suppose that we want to solve a system of $n$ equations in $n$ variables

$$
\mathbf { A x } = \mathbf { b } .
$$

Suppose further that because of measurement errors in $\mathbf { b }$ , we actually solve

$$
\begin{array} { r } { \mathbf { A } \hat { \mathbf { x } } = \hat { \mathbf { b } } . } \end{array}
$$

Can we get a bound on $\lVert \bf { x } - \hat { \bf { x } } \rVert$ in terms of $\| \mathbf { b } - { \hat { \mathbf { b } } } \| $ ? Starting with (A.93) and (A.94), we have

$$
\begin{array} { r l } & { \mathbf { A } ( \mathbf { x } - \hat { \mathbf { x } } ) = \mathbf { b } - \hat { \mathbf { b } } } \\ & { \quad ( \mathbf { x } - \hat { \mathbf { x } } ) = \mathbf { A } ^ { - 1 } ( \mathbf { b } - \hat { \mathbf { b } } ) } \\ & { \| \mathbf { x } - \hat { \mathbf { x } } \| = \| \mathbf { A } ^ { - 1 } ( \mathbf { b } - \hat { \mathbf { b } } ) \| } \\ & { \quad \| \mathbf { x } - \hat { \mathbf { x } } \| \leq \| \mathbf { A } ^ { - 1 } \| \| \mathbf { b } - \hat { \mathbf { b } } \| . } \end{array}
$$

This formula provides an absolute bound on the error in the solution. It is also worthwhile to compute a relative error bound:

$$
\begin{array} { r l } & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf b } \| } \leq \frac { \| { \bf A } ^ { - 1 } \| \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf A } ^ { - 1 } \| } \leq \frac { \| { \bf A } ^ { - 1 } \| \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \| { \bf x } - { \hat { \bf x } } \| \leq \| { \bf A } { \bf x } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \| { \bf x } - { \hat { \bf x } } \| \leq \| { \bf A } \| \| { \bf x } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf x } \| } \leq \| { \bf A } \| \| { \bf x } ^ { 1 } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf x } \| } \leq \| { \bf A } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } . } \end{array}
$$

The relative error in $\mathbf { b }$ is measured by

$$
{ \frac { \| \mathbf { b } - { \hat { \mathbf { b } } } \| } { \| \mathbf { b } \| } } .
$$

The relative error in $\mathbf { x }$ is measured by

$$
\frac { \lVert \mathbf { x } - \hat { \mathbf { x } } \rVert } { \lVert \mathbf { x } \rVert } .
$$

The constant

$$
\mathrm { c o n d } ( \mathbf { A } ) = \| \mathbf { A } \| \| \mathbf { A } ^ { - 1 } \|
$$

is called the condition number of A.

Note that nothing that we did in the calculation of the condition number depends on which norm we used. The condition number can be computed using the 1-norm,

2-norm, $\infty$ -norm, or Frobenius norm. The MATLAB cond command can be used to find the condition number of a matrix using each of these norms.

The condition number provides an upper bound on how inaccurate the solution to a system of equations might be because of errors in the right-hand side. In some cases, the condition number greatly overestimates the error in the solution. As a practical matter, it is wise to assume that the error is of roughly the size predicted by the condition number. In practice, double-precision floating point arithmetic only allows us to store numbers to about 16 digits of precision. If the condition number is greater than $1 0 ^ { 1 6 }$ , then by the above inequality, there may be no accurate digits in the computer solution to the system of equations. Systems of equations with very large condition numbers are called ill-conditioned.

It is important to understand that ill-conditioning is a property of the system of equations and not of the algorithm used to solve the system of equations. Ill-conditioning cannot be fixed simply by using a better algorithm. Instead, we must either increase the precision of our floating point representation or find a different, better conditioned system of equations to solve.

# A.9. THE QR FACTORIZATION

Although the theory of linear algebra can be developed using the reduced row echelon form, there is an alternative computational approach that works better in practice. The basic idea is to compute factorizations of matrices that involve orthogonal, diagonal, and upper-triangular matrices. This alternative approach leads to algorithms that can quickly compute accurate solutions to linear systems of equations and least squares problems. In this section we introduce the QR factorization, which is one of the most widely used orthogonal matrix factorizations. Another factorization, the singular value decomposition (SVD), is introduced in Chapter 3.

Theorem A.10 Let A be an m by n matrix. A can be written as

$$
\mathbf { A } = \mathbf { Q } \mathbf { R } ,
$$

where $\mathbf { Q }$ is an m by m orthogonal matrix, and $\mathbf { R }$ is an m by n upper-triangular matrix. This is called the QR factorization of A.

The MATLAB command qr can be used to compute the QR factorization of a matrix. In a common situation, A will be an $m$ by $n$ matrix with $m > n$ , and the rank of A will be $n$ . In this case, we can write

$$
\begin{array} { r } { \mathbf { R } = \biggl [ \mathbf { R } _ { 1 } \biggr ] , } \end{array}
$$

where $\mathbf { R } _ { 1 }$ is $n$ by $n$ , and

$$
\begin{array} { r } { { \bf Q } = [ { \bf Q } _ { 1 } \quad { \bf Q } _ { 2 } ] , } \end{array}
$$

where $\mathbf { Q } _ { 1 }$ is $m$ by $n$ and $\mathbf { Q } _ { 2 }$ is $m$ by $m - n$ . In this case, the QR factorization has some important properties.

Theorem A.11 Let $\mathbf { Q }$ and $\mathbf { R }$ be the QR factorization of an m by n matrix A with $m > n$ and ran $k ( \mathbf { A } ) = n$ . Then,

1. The columns of ${ \bf Q } _ { 1 }$ are an orthonormal basis for $R ( \mathbf { A } )$ .   
2. The columns of $\mathbf { Q } _ { 2 }$ are an orthonormal basis for $N ( \mathbf { A } ^ { T } )$ .   
3. The matrix $\mathbf { R } _ { 1 }$ is nonsingular.

Now, suppose that we want to solve the least squares problem,

$$
\operatorname* { m i n } \| \mathbf { A x } - \mathbf { b } \| _ { 2 } .
$$

Since multiplying a vector by an orthogonal matrix does not change its length, this is equivalent to

$$
\operatorname* { m i n } \| \mathbf { Q } ^ { T } ( \mathbf { A x } - \mathbf { b } ) \| _ { 2 } .
$$

But

$$
{ \bf Q } ^ { T } { \bf A } = { \bf Q } ^ { T } { \bf Q } { \bf R } = { \bf R } .
$$

So, we have

$$
\operatorname* { m i n } \lVert \mathbf { R } \mathbf { x } - \mathbf { Q } ^ { T } \mathbf { b } \rVert _ { 2 }
$$

or

$$
\begin{array} { r } { \operatorname* { m i n } \| \mathbf { R } _ { 1 } \mathbf { x } - \mathbf { Q } _ { 1 } ^ { T } \mathbf { b } \| _ { 2 } . } \\ { \mathbf { 0 } \mathbf { x } - \mathbf { Q } _ { 2 } ^ { T } \mathbf { b } \| _ { 2 } } \end{array}
$$

Whatever value of $\mathbf { x }$ we pick, we will probably end up with nonzero residuals because of the $\mathbf { 0 x } - \mathbf { Q } _ { 2 } ^ { T } \mathbf { b }$ part of the least squares problem. We cannot minimize the norm of this part of the vector. However, we can find an $\mathbf { x }$ that exactly solves $\mathbf { R } _ { 1 } \mathbf { x } = \mathbf { Q } _ { 1 } ^ { T } \mathbf { b }$ . Thus, we can minimize the least squares problem by solving the square system of equations,

$$
\mathbf { R } _ { 1 } \mathbf { x } = \mathbf { Q } _ { 1 } ^ { T } \mathbf { b } .
$$

The advantage of solving this system of equations instead of the normal equations (A.73) is that the normal equations are typically much more badly conditioned than (A.115).

# A.10. COMPLEX MATRICES AND VECTORS

Although nearly all of the mathematics in this textbook involves real numbers, complex numbers do appear in Chapter 8 when we consider the Fourier transform. We assume that the reader is already familiar with arithmetic involving complex numbers including addition, subtraction, multiplication, division, and complex exponentials. Most theorems of linear algebra extend trivially from real to complex vectors and matrices. In this section we briefly discuss our notation and some important differences between the real and complex cases.

Given a complex number $z = a + b \imath$ , where $\imath$ is the $\sqrt { - 1 }$ , the complex conjugate of $z$ is $z ^ { * } = a - b \quad$ . Note that the absolute value of $z$ is

$$
| z | = { \sqrt { a ^ { 2 } + b ^ { 2 } } } = { \sqrt { z ^ { * } z } } .
$$

The main difference between linear algebra on real vectors and complex vectors is in the definition of the dot product of two vectors. We define the dot product of two complex vectors $\mathbf { x }$ and $\mathbf { y }$ to be

$$
\mathbf { x } \cdot \mathbf { y } = \mathbf { x } ^ { * ^ { T } } \mathbf { y } .
$$

The advantage of this definition is that

$$
\mathbf { x ^ { * } } ^ { T } \mathbf { x } = \sum _ { k = 1 } ^ { n } x _ { k } ^ { * } x _ { k } = \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { 2 } .
$$

Thus we can then define the 2-norm of a complex vector by

$$
\| \boldsymbol { x } \| _ { 2 } = \sqrt { \mathbf { x } ^ { * } \overset { T } { \mathbf { x } } } .
$$

The combination of taking the complex conjugate and transpose, called the Hermitian transpose, occurs so frequently that we denote this by

$$
\mathbf { x } ^ { H } = \mathbf { x } ^ { * ^ { T } } .
$$

Note that for a real vector, $\mathbf { x }$ , the conjugate is simply ${ \bf x } ^ { * } = { \bf x }$ , so $\mathbf { x } ^ { H } = \mathbf { x } ^ { T } .$ In MATLAB, the apostrophe denotes the Hermitian transpose.

In general, you will almost never go wrong by using the Hermitian transpose in any linear algebra computation involving complex numbers that would normally involve a transpose when working with real vectors and matrices. For example, if we want to minimize $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ , where ${ \bf G } , { \bf m }$ , and $\mathbf { d }$ are complex, we can solve the normal equations,

$$
\mathbf { G } ^ { H } \mathbf { G } \mathbf { m } = \mathbf { G } ^ { H } \mathbf { d } .
$$

# A.11. LINEAR ALGEBRA IN SPACES OF FUNCTIONS

So far, we have considered only vectors in $R ^ { n } .$ The concepts of linear algebra can be extended to other contexts. In general, as long as the objects that we want to consider can be multiplied by scalars and added together, and as long as they obey the laws of vector algebra, then we have a vector space in which we can practice linear algebra. If we can also define a vector product similar to the dot product, then we have what is called an inner product space, and we can define orthogonality, projections, and the 2-norm.

There are many different vector spaces used in various areas of science and mathematics. For our work in inverse problems, a very commonly used vector space is the space of functions defined on an interval [a, b].

Multiplying a scalar times a function or adding two functions together clearly produces another function. In this space, the function $z ( x ) = 0$ takes the place of the 0 vector, since $f ( x ) + z ( x ) = f ( x )$ . Two functions $f ( x )$ and $g ( x )$ are linearly independent if the only solution to

$$
c _ { 1 } f ( x ) + c _ { 2 } g ( x ) = z ( x )
$$

is $c _ { 1 } = c _ { 2 } = 0$ .

We can define the dot product of two functions $f$ and $g$ to be

$$
f \cdot g = \int _ { a } ^ { b } f ( x ) g ( x ) \ d x .
$$

Another commonly used notation for this dot product or inner product of $f$ and $g$ is

$$
f \cdot g = \langle f , g \rangle .
$$

It is easy to show that this inner product has all of the algebraic properties of the dot product of two vectors in $R ^ { n } .$ A more important motivation for defining the dot product in this way is that it leads to a useful definition of the 2-norm of a function. Following√ our earlier formula that $\| x \| _ { 2 } = \sqrt { x ^ { T } x }$ , we have

$$
\| f \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } f ( x ) ^ { 2 } \ d x } } .
$$

Using this definition, the distance between two functions $f$ and $g$ is

$$
\| f - g \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } ( f ( x ) - g ( x ) ) ^ { 2 } \ d x } } .
$$

This measure is obviously 0 when $f ( x ) = g ( x )$ everywhere, but can also be 0 when $f ( x )$ and $g ( x )$ differ at a finite or countably infinite set of points. The measure is only nonzero if $\dot { \boldsymbol { f } } ( \boldsymbol { x } )$ and $g ( x )$ differ on an interval.

Using this inner product and norm, we can reconstruct the theory of linear algebra from $R ^ { n }$ in our space of functions. This includes the concepts of orthogonality, projections, norms, and least squares solutions.

Definition A.32 Given a collection of functions $f _ { 1 } ( x ) , f _ { 2 } ( x ) , . . . . , f _ { m } ( x )$ in an inner product space, the Gram matrix of the functions is the $m \times m$ matrix $\mathbf { \Gamma }$ , whose elements are given by

$$
\Gamma _ { i , j } = f _ { i } \cdot f _ { j } .
$$

The Gram matrix has several important properties. It is symmetric and positive semidefinite. If the functions are linearly independent, then the Gram matrix is also positive definite. Furthermore, the rank of $\mathbf { \Gamma }$ is equal to the size of the largest linearly independent subset of the functions $f _ { 1 } ( x ) , \ldots . \ldots , f _ { m } ( x )$ .

# A.12. EXERCISES

1. Let A be an $m$ by $n$ matrix with $n$ pivot columns in its RREF. Can the system of equations $\mathbf { A x } = \mathbf { b }$ have infinitely many solutions?

2. If $\mathbf { C } = \mathbf { A } \mathbf { B }$ is a 5 by 4 matrix, then how many rows does A have? How many columns does $\mathbf { B }$ have? Can you say anything about the number of columns in A?

3. Suppose that $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 }$ , and $\mathbf { v } _ { 3 }$ are three vectors in $R ^ { 3 }$ and that $\mathbf { v } _ { 3 } = - 2 \mathbf { v } _ { 1 } + 3 \mathbf { v } _ { 2 }$ . Are the vectors linearly dependent or linearly independent?

4. Let

$$
\mathbf { A } = { \left[ \begin{array} { l l l l } { 1 } & { 2 } & { 3 } & { 4 } \\ { 2 } & { 2 } & { 1 } & { 3 } \\ { 4 } & { 6 } & { 7 } & { 1 1 } \end{array} \right] } .
$$

Find bases for ${ \cal N } ( { \bf A } ) , { \cal R } ( { \bf A } ) , { \cal N } ( { \bf A } ^ { T } )$ , and $R ( \mathbf { A } ^ { T } )$ . What are the dimensions of the four subspaces?

5. Let A be an $n$ by $n$ matrix such that $\mathbf { A } ^ { - 1 }$ exists. What are ${ \cal N } ( { \bf A } ) , { \cal R } ( { \bf A } ) , { \cal N } ( { \bf A } ^ { T } )$ and $R ( \mathbf { A } ^ { T } ) \vec { \ ? }$

6. Let A be any 9 by 6 matrix. If the dimension of the null space of $\mathbf { A }$ is 5, then what is the dimension of $R ( \mathbf { A } )$ ? What is the dimension of $R ( \mathbf { A } ^ { T } ) \vec { \ ? }$ What is the rank of A?

7. Suppose that a nonhomogeneous system of equations with four equations and six unknowns has a solution with two free variables. Is it possible to change the righthand side of the system of equations so that the modified system of equations has no solutions?

8. Let $W$ be the set of vectors $\mathbf { x }$ in $R ^ { 4 }$ such that $x _ { 1 } x _ { 2 } = 0$ . Is $W$ a subspace of $R ^ { 4 }$ ?

9. Let $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \mathbf { v } _ { 3 }$ be a set of three nonzero orthogonal vectors. Show that the vectors are also linearly independent.

10. Show that if $\mathbf { x } \perp \mathbf { y }$ , then

$$
\left\| \mathbf { x } + \mathbf { y } \right\| _ { 2 } ^ { 2 } = \left\| \mathbf { x } \right\| _ { 2 } ^ { 2 } + \left\| \mathbf { y } \right\| _ { 2 } ^ { 2 } .
$$

11. In this exercise, we will derive the formula (A.88) for the 1-norm of a matrix. Begin with the optimization problem

$$
\| \mathbf { A } \| _ { 1 } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { 1 } = 1 } \| \mathbf { A } \mathbf { x } \| _ { 1 } .
$$

(a) Show that if $\| \mathbf { x } \| _ { 1 } = 1$ , then

$$
\| \mathbf { A x } \| _ { 1 } \leq \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | .
$$

(b) Find a vector $\mathbf { x }$ such that $\| \mathbf { x } \| _ { 1 } = 1$ , and

$$
\| \mathbf { A x } \| _ { 1 } = \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | .
$$

(c) Conclude that

$$
\| \mathbf { A } \| _ { 1 } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { 1 } = 1 } \| \mathbf { A } \mathbf { x } \| _ { 1 } = \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | .
$$

12. Derive the formula (A.90) for the infinity norm of a matrix.

13. Let $\mathbf { A }$ be an $m$ by $n$ matrix.

(a) Show that $\mathbf { A } ^ { T } \mathbf { A }$ is symmetric.   
(b) Show that $\mathbf { A } ^ { T } \mathbf { A }$ is positive semidefinite. Hint: Use the definition of positive semidefinite rather than trying to compute eigenvalues.   
(c) Show that if $\operatorname { r a n k } ( \mathbf { A } ) = n$ , then the only solution to $\mathbf { A x } = \mathbf { 0 }$ is $\mathbf { x } = \mathbf { 0 }$ .   
(d) Use part c to show that if ra $\operatorname { n k } ( \mathbf { A } ) = n$ , then $\mathbf { A } ^ { T } \mathbf { A }$ is positive definite.   
(e) Use part $\mathrm { d }$ to show that if ra $\mathrm { n k } ( \mathbf { A } ) = n$ , then $\mathbf { A } ^ { T } \mathbf { A }$ is nonsingular.   
(f) Show that $N ( \mathbf { A } ^ { T } \mathbf { A } ) = N ( \mathbf { A } )$ .

14. Show that

$$
\operatorname { c o n d } ( \mathbf { A } \mathbf { B } ) \leq \operatorname { c o n d } ( \mathbf { A } ) \operatorname { c o n d } ( \mathbf { B } ) .
$$

15. Let A be a symmetric and positive definite matrix with Cholesky factorization,

$$
\mathbf { A } = \mathbf { R } ^ { T } \mathbf { R } .
$$

Show how the Cholesky factorization can be used to solve $\mathbf { A x } = \mathbf { b }$ by solving two systems of equations, each of which has $\mathbf { R }$ or $\mathbf { R } ^ { T }$ as its matrix.

16. Let $P _ { 3 } [ 0 , 1 ]$ be the space of polynomials of degree less than or equal to 3 on the interval [0, 1]. The polynomials $p _ { 1 } ( x ) = 1 , p _ { 2 } ( x ) = x , p _ { 3 } ( x ) = x ^ { 2 }$ , and $p _ { 4 } ( x ) = x ^ { 3 }$ form a basis for $P _ { 3 } [ 0 , 1 ]$ , but they are not orthogonal with respect to the inner product,

$$
f \cdot g = \int _ { 0 } ^ { 1 } f ( x ) g ( x ) \ d x .
$$

Use the Gram-Schmidt orthogonalization process to construct an orthogonal basis for $P _ { 3 } [ 0 , 1 ]$ . Once you have your basis, use it to find the third-degree polynomial that best approximates $f ( x ) = e ^ { - x }$ on the interval [0, 1] in the least squares sense.

# A.13. NOTES AND FURTHER READING

Much of this material is typically covered in sophomore-level linear algebra courses, and there are an enormous number of textbooks at this level. One good introductory linear algebra textbook is [95]. At a slightly more advanced level, [109] and [152] are both excellent. The book by Strang and Borre [153] reviews linear algebra in the context of geodetic problems.

Fast and accurate algorithms for linear algebra computations are a somewhat more advanced and specialized topic. A classic reference is [53]. Other good books on this topic include [38] and [164].

The extension of linear algebra to spaces of functions is a topic in the subject of functional analysis. Unfortunately, most textbooks on functional analysis assume that the reader has a considerable mathematical background. One book that is reasonably accessible to readers with limited mathematical backgrounds is [102].

# Review of Probability and Statistics

# Synopsis

A brief review is given of the topics in classical probability and statistics that are used throughout the book. Connections between probability theory and its application to the analysis of data with random measurement errors are highlighted. Note that some very different philosophical interpretations of probability theory are discussed in Chapter 11.

# B.1. PROBABILITY AND RANDOM VARIABLES

The mathematical theory of probability begins with an experiment, which has a set $S$ of possible outcomes. We will be interested in events that are subsets $A$ of $S$ .

Definition B.1 The probability function $P$ is a function defined on subsets of $S$ with the following properties:

1. $P ( S ) = 1$ .   
2. For every event $A \subseteq S$ , $P ( A ) \geq 0$ .   
3. If events $A _ { 1 } , A _ { 2 }$ , . . . , $A _ { n }$ are pairwise mutually exclusive (i.e., impossible to both occur), so that $A _ { i } \cap A _ { j }$ is empty for all pairs $i , j$ , then

$$
P ( \cup _ { i = 1 } ^ { n } A _ { i } ) = \sum _ { i = 1 } ^ { n } P ( A _ { i } ) .
$$

The probability properties given above are fundamental to developing the mathematics of probability theory. However, applying this definition of probability to real-world situations frequently requires ingenuity.

# Example B.1

Consider the experiment of throwing a dart at a dart board. We will assume that our dart thrower is an expert who always hits the dart board. The sample space $S$ consists of the points on the dart board. We can define an event $A$ that consists of the points in the bullseye, so that $P ( A )$ is the probability that the thrower hits the bullseye.

In practice, the outcome of an experiment is often a number rather than an event. Random variables are a useful generalization of the basic concept of probability.

Definition B.2 A random variable $X$ is a function $X ( s )$ that assigns a value to each outcome $s$ in the sample space $S$ .

Each time that we perform an experiment, we obtain a particular value of the random variable. These values are called realizations of the random variable.

# Example B.2

To continue our previous example, let $X$ be the function that takes a point on the dart board and returns the associated score. Suppose that throwing the dart in the bullseye scores 50 points. Then for each point $s$ in the bullseye, $X ( s ) = 5 0$ .

In this book we deal frequently with experimental measurements that can include some random measurement error.

# Example B.3

Suppose that we measure the mass of an object five times to obtain the realizations $m _ { 1 } = 1 0 . 1 ~ \mathrm { k g }$ , $m _ { 2 } = 1 0 . 0 ~ \mathrm { k g }$ , $m _ { 3 } = 1 0 . 0 ~ \mathrm { k g }$ , $m _ { 4 } = 9 . 9 ~ \mathrm { k g } .$ , and $m _ { 5 } = 1 0 . 1 ~ \mathrm { k g }$ . We will assume that there is one true mass $m$ , and that the measurements we obtained varied because of random measurement errors $e _ { i }$ , so that

$$
\begin{array} { r } { m _ { 1 } = m + e _ { 1 } , m _ { 2 } = m + e _ { 2 } , m _ { 3 } = m + e _ { 3 } , m _ { 4 } = m + e _ { 4 } , m _ { 5 } = m + e _ { 5 } . } \end{array}
$$

We can treat the measurement errors as realizations of a random variable $E$ . Equivalently, since the true mass m is just a constant, we could treat the measurements $m _ { 1 }$ , $m _ { 2 }$ , . . . , $m _ { 5 }$ as realizations of a random variable $M$ . In practice it makes little difference whether we treat the measurements or the measurement errors as random variables.

Note that in a Bayesian approach the mass $m$ of the object would itself be a random variable. This is a viewpoint that we consider in Chapter 11.

The relative probability of realization values for a random variable can be characterized by a non-negative probability density function (PDF), $f _ { X } ( x )$ , with

$$
P ( X \leq a ) = \int _ { - \infty } ^ { a } f _ { X } ( x ) \ d x .
$$

Because a random variable always has some value,

$$
\intop _ { - \infty } ^ { \infty } f _ { X } ( x ) \ d x = 1 .
$$

The following definitions give some useful random variables that frequently arise in inverse problems.

Definition B.3 The uniform random variable on the the interval [a, b] (Figure B.1) has the following PDF:

$$
f _ { U } ( x ) = \left\{ { \begin{array} { l r } { \frac { 1 } { b - a } } & { a \leq x \leq b } \\ { 0 } & { x < a } \\ { 0 } & { x > b . } \end{array} } \right.
$$

Definition B.4 The normal or Gaussian random variable (Figure B.2) has the following PDF:

$$
f _ { N } ( x ) = { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - { \frac { 1 } { 2 } } ( x - \mu ) ^ { 2 } / \sigma ^ { 2 } } .
$$

The notation $N ( \mu , \sigma ^ { 2 } )$ is used to denote a normal distribution with parameters $\mu$ and $\sigma$ . The standard normal random variable, $N ( 0 , 1 )$ , has $\mu = 0$ and $\sigma ^ { 2 } = 1$ .

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/06caaa85f9f6d0ca1245ba0e49c0c3aebd53dfc8834e50cca460b072ca752234.jpg)  
Figure B.1 The PDF for the uniform random variable on [0, 1].

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/4eda9f198433205b805743c01deb9433c9cfd58cf597814937d4712794fd0a5f.jpg)  
Figure B.2 The PDF of the standard normal random variable.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/97fb734eed2d79d0004396fc3efbc026c08416640111c4e88d12724202bb2400.jpg)  
Figure B.3 The Student’s $t$ probability density function for $\nu = 3$ and $\nu = 2 0$ . Dashed curve shows the normal distribution $N ( 0 , 1 )$ (Figure B 2).

Definition B.5 The Student’s $\pmb { t }$ distribution with $\nu$ degrees of freedom (Figure B.3) has the PDF

$$
f _ { t } ( x ) = \frac { \Gamma ( ( \nu + 1 ) / 2 ) } { \Gamma ( \nu / 2 ) } \frac { 1 } { \sqrt { \nu \pi } } \left( 1 + \frac { x ^ { 2 } } { \nu } \right) ^ { - ( \nu + 1 ) / 2 } ,
$$

where the gamma function is

$$
\Gamma ( x ) = \int _ { 0 } ^ { \infty } \xi ^ { x - 1 } e ^ { - \xi } d \xi .
$$

The Student’s $t$ distribution is so named because W. S. Gosset used the pseudonym “Student” in publishing the first paper in which the distribution appeared. In the limit as $\nu$ goes to infinity, Student’s $t$ distribution approaches a standard normal distribution. However, for small values of $\nu$ , (B.7) has a greater percentage of extreme values than (B.6).

Definition B.6 The $\chi ^ { 2 }$ random variable has the PDF (Figure B.4)

$$
f _ { \chi ^ { 2 } } ( x ) = \frac { 1 } { 2 ^ { \nu / 2 } \Gamma ( \nu / 2 ) } x ^ { \frac { 1 } { 2 } \nu - 1 } e ^ { - x / 2 } ,
$$

where the parameter $\nu$ is the number of degrees of freedom.

Definition B.7 The exponential random variable (Figure B.5) has the PDF

$$
f _ { e x p } ( x ) = \left\{ \begin{array} { l l } { \lambda e ^ { - \lambda x } } & { x \ge 0 } \\ { 0 } & { x < 0 . } \end{array} \right.
$$

Definition B.8 The double-sided exponential random variable (Figure B.6) has the PDF

$$
f _ { d e x p } ( x ) = \frac { 1 } { \sigma \sqrt { 2 } } e ^ { - \sqrt { 2 } | x - \mu | / \sigma } .
$$

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/0bab3696a67196878387d27408052b06b3b35978f00ecf8f6265b87122d7560b.jpg)  
Figure B.4 The $\chi ^ { 2 }$ PDF for several values of $\nu$ .

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/7bd4e208287089d8244ca9f3a96ba37e7ca62c93ecbf906b83bdae70b011f7a8.jpg)  
Figure B.5 The exponential PDF $\left( \lambda = 1 \right)$ ).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/d40fd1acf921ec16268068be5c6f1049af5f63d3421ed3bcb3880a089ba48e15.jpg)  
Figure B.6 The double-sided exponential PDF $( \mu = 0$ , $\sigma = 1$ ).

It can be shown that for $n$ independent random variables, $X _ { i }$ , with standard normal distributions, the random variable

$$
Z = \sum _ { i = 1 } ^ { n } X _ { i } ^ { 2 }
$$

is a $\chi ^ { 2 }$ random variable with $\nu = n$ degrees of freedom [47].

The cumulative distribution function (CDF) $F _ { X } ( a )$ of a one-dimensional random variable $X$ is given by the definite integral of the associated PDF

$$
F _ { X } ( a ) = P ( X \leq a ) = \intop _ { - \infty } ^ { a } f _ { X } ( x ) \ d x .
$$

Note that $F _ { X } ( a )$ must lie in the interval [0, 1] for all $a$ , and is a nondecreasing function of $^ a$ because of the unit area and non-negativity of the PDF.

For the uniform PDF on the unit interval, for example, the CDF is a ramp function,

$$
\begin{array} { l } { { \displaystyle F _ { U } ( a ) = \int _ { - \infty } ^ { a } f _ { u } ( z ) ~ d z } } \\ { { \displaystyle F _ { U } ( a ) = \left\{ \begin{array} { l l } { { 0 } } & { { \quad a \leq 0 } } \\ { { a } } & { { 0 \leq a \leq 1 } } \\ { { 1 } } & { { \quad a > 1 . } } \end{array} \right. } } \end{array}
$$

The PDF, $f _ { X } ( x )$ , or CDF, $F _ { X } ( a )$ , completely determine the properties of a random variable. The probability that a particular realization of $X$ will lie within a general interval [a, $b ]$ i s

$$
\begin{array} { l } { { P ( a \leq X \leq b ) = P ( X \leq b ) - P ( X \leq a ) = F _ { X } ( b ) - F _ { X } ( a ) } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle = \int _ { - \infty } ^ { b } f _ { X } ( x ) ~ d x - \int _ { - \infty } ^ { a } f _ { X } ( x ) ~ d x = \int _ { a } ^ { b } f _ { X } ( x ) ~ d x . } } \end{array}
$$

# B.2. EXPECTED VALUE AND VARIANCE

Definition B.9 The expected value of a random variable $X$ , denoted by $E [ X ]$ or $\mu ( X )$ , is

$$
E [ X ] = \int _ { - \infty } ^ { \infty } x f _ { X } ( x ) \ d x .
$$

In general, if $g ( X )$ is some function of a random variable $X$ , then

$$
E [ g ( X ) ] = \int _ { - \infty } ^ { \infty } g ( x ) f _ { X } ( x ) ~ d x .
$$

Some authors use the term “mean” for the expected value of a random variable. We will reserve this term for the average of a set of data. Note that the expected value of

a random variable is not necessarily identical to the mode (the value with the largest value of $f ( x ) )$ nor is it necessarily identical to the median, the value of $_ x$ for which the value of the CDF is $F _ { X } ( x ) = 1 / 2$ .

# Example B.4

The expected value of an $N ( \mu , \sigma )$ random variable $X$ is

$$
{ \begin{array} { r l } & { E [ X ] = \displaystyle \int _ { - \infty } ^ { \infty } x { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - { \frac { ( x - \mu ) ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x } \\ & { \qquad = \displaystyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } ( x + \mu ) e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x } \\ & { \qquad = \mu \displaystyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x + \displaystyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } x e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x . } \end{array} }
$$

The first integral term is $\mu$ because the integral of the entire PDF is 1, and the second term is 0 because it is an odd function integrated over a symmetric interval. Thus,

$$
E [ X ] = \mu .
$$

Definition B.10 The variance of a random variable $X$ , denoted by $\operatorname { V a r } ( X )$ or $\sigma _ { X } ^ { 2 }$ , is given by

$$
\begin{array} { l } { \displaystyle \mathrm { V a r } ( X ) = E [ ( X - E [ X ] ) ^ { 2 } ] } \\ { \displaystyle = E [ X ^ { 2 } ] - E [ X ] ^ { 2 } } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } ( x - E [ X ] ) ^ { 2 } f _ { X } ( x ) ~ d x . } \end{array}
$$

The standard deviation of $X$ , often denoted $\sigma _ { X }$ , is

$$
\sigma _ { X } = { \sqrt { \operatorname { V a r } ( X ) } } .
$$

The variance and standard deviation serve as measures of the spread of the random variable about its expected value. Since the units of $\sigma$ are the same as the units of $\mu$ , the standard deviation is generally more practical for reporting a spread measure. However, the variance has properties that make it more useful for certain calculations.

# B.3. JOINT DISTRIBUTIONS

Definition B.11 If we have two random variables $X$ and $Y$ , they may have a joint probability density function ( JDF), $f ( x , \gamma )$ , with

$$
P ( X \leq a { \mathrm { ~ a n d ~ } } Y \leq b ) = \int _ { - \infty } ^ { a } \intop _ { - \infty } ^ { b } f ( x , \gamma ) \ d \gamma \ d x .
$$

If $X$ and $Y$ have a JDF, then we can use it to evaluate the expected value of a function of $X$ and $Y$ . The expected value of $g ( X , Y )$ is

$$
E [ g ( X , \ Y ) ] = \int _ { - \infty } ^ { \infty } \int \displaylimits _ { - \infty } ^ { \infty } g ( x , \gamma ) f ( x , \gamma ) \ d \gamma \ d x .
$$

Definition B.12 Two random variables $X$ and $Y$ are independent if a JDF exists and is defined by

$$
f ( x , \gamma ) = f _ { X } ( x ) f _ { Y } ( \gamma ) .
$$

Definition B.13 If $X$ and $Y$ have a JDF, then the covariance of $X$ and $Y$ is

$$
\operatorname { C o v } ( X , Y ) = E [ ( X - E [ X ] ) ( Y - E [ Y ] ) ] = E [ X Y ] - E [ X ] E [ Y ] .
$$

If $X$ and $Y$ are independent, then $E [ X Y ] = E [ X ] E [ Y ]$ , and $\operatorname { C o v } ( X , \ Y ) = 0$ . However, if $X$ and $Y$ are dependent, it is still possible, given some particular distributions, for $X$ and $Y$ to have $\operatorname { C o v } ( X , \ Y ) = 0$ . If $\operatorname { C o v } ( X , \ Y ) = 0$ , $X$ and $Y$ are called uncorrelated.

Definition B.14 The correlation of $X$ and $Y$ is

$$
\rho ( X , ~ Y ) = \frac { \operatorname { C o v } ( X , ~ Y ) } { \sqrt { \operatorname { V a r } ( X ) \operatorname { V a r } ( Y ) } } .
$$

Correlation is thus a scaled covariance.

Theorem B.1 The following properties of Var, Cov, and correlation hold for any random variables $X$ and $Y$ and scalars s and a.

1. $V a r ( X ) \geq 0$ .   
2. ${ \cal V } a r ( X + a ) = { \cal V } a r ( X )$ .   
3. ${ \cal { V } } a r ( s X ) = s ^ { 2 } { \cal { V } } a r ( X ) .$   
4. $V a r ( X + Y ) = V a r ( X ) + V a r ( Y ) + 2 C o \nu ( X , Y ) .$   
5. $C o \nu ( X , Y ) = C o \nu ( Y , X )$ .   
6. $\rho ( X , \ Y ) = \rho ( Y , X )$ .   
7. $- 1 \le \rho ( X , ~ Y ) \le 1$ .

The following example demonstrates the use of some of these properties.

# Example B.5

Suppose that $Z$ is a standard normal random variable. Let

$$
X = \mu + \sigma Z .
$$

Then

$$
E [ X ] = E [ \mu ] + \sigma E [ Z ]
$$

so

$$
E [ X ] = \mu .
$$

Also,

$$
\operatorname { V a r } ( X ) = \operatorname { V a r } ( \mu ) + \sigma ^ { 2 } \operatorname { V a r } ( Z ) = \sigma ^ { 2 } .
$$

Thus, if we have a program to generate random numbers with the standard normal distribution, we can use it to generate normal random numbers with any desired expected value and standard deviation. The MATLAB command randn generates independent realizations of an $N ( 0 , 1 )$ random variable.

# Example B.6

What is the CDF (or PDF) of the sum of two independent random variables $X + Y ?$ To see this, we write the desired CDF in terms of an appropriate integral over the JDF, $f ( x , \gamma )$ , which gives (Figure B.7):

$$
\begin{array} { r l } { F _ { X + Y } ( z ) } & { = P ( X + Y \leq z ) } \\ & { = \displaystyle \iint _ { z \in \mathcal { X } _ { r } } f ( x , y ) d x \ d y } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \iint \int \int \ f _ { X } ( x ) \hat { f } _ { Y } ( y ) d x \ d y , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \int \displaystyle \int \int _ { z \in \mathcal { X } _ { r } } \int \int \hat { f } ( x ) \hat { f } _ { Y } ( y ) d x \ d y } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \iint \displaystyle \int _ { z \in \mathcal { X } _ { r } } \int \hat { f } _ { X } ( x ) \ d x \hat { f } _ { Y } ( y ) \ d y , } \\ & { = \displaystyle \int \displaystyle \int _ { z \in \mathcal { X } _ { r } } \int \hat { f } _ { X } ( x ) \ d x \hat { f } _ { Y } ( y ) \ d y . } \end{array}
$$

$$
= \int _ { - \infty } ^ { \infty } F _ { X } ( z - \gamma ) f _ { Y } ( \gamma ) \ d \gamma .
$$

The associated PDF is

$$
{ \begin{array} { l } { f _ { X + Y } ( z ) = { \cfrac { d } { d z } } \ { \displaystyle \int _ { - \infty } ^ { \infty } } \ F _ { X } ( z - y ) f _ { Y } ( y ) \ d y } \\ { = \int _ { - \infty } ^ { \infty } { \cfrac { d } { d z } } F _ { X } ( z - y ) f _ { Y } ( y ) \ d y } \\ { = \displaystyle \int _ { - \infty } ^ { \infty } f _ { X } ( z - y ) f _ { Y } ( y ) \ d y } \\ { \quad - \infty } \\ { \quad - \infty } \\ { \quad = f _ { X } ( z ) * f _ { Y } ( z ) . } \end{array} }
$$

Adding two independent random variables thus produces a new random variable that has a PDF given by the convolution of the PDFs of the two individual variables.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/7e90df4d3a22255c00ec6c5fe2e391a91e6e240f50fa302f1f6d543e3f61e646.jpg)  
Figure B.7 Integration of a JDF for two independent random variables, $X$ and $Y ,$ to evaluate the CDF of $Z = X + Y$ .

The JDF can be used to evaluate the CDF or PDF arising from a general function of jointly distributed random variables. The process is identical to the previous example except that the specific form of the integral limits is determined by the specific function.

# Example B.7

Consider the product of two independent, identically distributed, standard normal random variables,

$$
Z = X Y ,
$$

with a JDF given by

$$
f ( x , \ \gamma ) = f ( x ) f ( \gamma ) = { \frac { 1 } { 2 \pi \sigma ^ { 2 } } } e ^ { - ( x ^ { 2 } + \gamma ^ { 2 } ) / 2 \sigma ^ { 2 } } .
$$

The CDF of $Z$ is

$$
F ( z ) = P ( Z \leq z ) = P ( X Y \leq z ) .
$$

For $z \le 0$ , this is the integral of the JDF over the exterior of the hyperbolas defined by $x \gamma \leq z \leq 0$ , while for $z \ge 0$ , we integrate over the interior of the complementary hyperbolas $x \gamma \leq z \geq 0$ . At $z = 0$ , the integral covers exactly half of the $( x , \gamma )$ plane (the second and fourth quadrants) and, because of the symmetry of the JDF, has accumulated half of the probability, or $1 / 2$ .

The integral is thus

$$
F ( z ) = 2 \int _ { - \infty } ^ { 0 } \int _ { z / x } ^ { \infty } \frac { 1 } { 2 \pi { \sigma } ^ { 2 } } e ^ { - ( x ^ { 2 } + \gamma ^ { 2 } ) / 2 { \sigma } ^ { 2 } } d \gamma \ d x \ ( z \leq 0 )
$$

and

$$
F ( z ) = 1 / 2 + 2 \intop _ { - \infty } ^ { 0 } \intop _ { 0 } ^ { z / x } \frac { 1 } { 2 \pi \sigma ^ { 2 } } e ^ { - ( x ^ { 2 } + \gamma ^ { 2 } ) / 2 \sigma ^ { 2 } } d \gamma \ d x \ ( z \geq 0 ) .
$$

As in the previous example for the sum of two random variables, the PDF may be obtained from the CDF by differentiating with respect to $z$ .

# B.4. CONDITIONAL PROBABILITY

In some situations we will be interested in the probability of an event happening given that some other event has also happened.

Definition B.15 The conditional probability of $A$ given that $B$ has occurred is given by

$$
P ( A | B ) = { \frac { P ( A \cap B ) } { P ( B ) } } .
$$

Arguments based on conditional probabilities are often very helpful in computing probabilities. The key to such arguments is the law of total probability.

Theorem B.2 Suppose that $B _ { 1 }$ , $B _ { 2 }$ , . . . , $B _ { n }$ are mutually disjoint and exhaustive events. That is, $B _ { i } \cap B _ { j } = \varnothing$ (the empty set) for $i \neq j$ , and

$$
\cup _ { i = 1 } ^ { n } B _ { i } = S .
$$

Then

$$
P ( A ) = \sum _ { i = 1 } ^ { n } P ( A | B _ { i } ) P ( B _ { i } ) .
$$

It is often necessary to reverse the order of conditioning in a conditional probability. Bayes’ theorem provides a way to do this.

# Theorem B.3 Bayes Theorem

$$
P ( B | A ) = \frac { P ( A | B ) P ( B ) } { P ( A ) } .
$$

# Example B.8

A screening test has been developed for a very serious but rare disease. If a person has the disease, then the test will detect the disease with probability $9 9 \%$ . If a person does not have the disease, then the test will give a false-positive detection with probability $1 \%$ . The probability that any individual in the population has the disease is $0 . 0 1 \%$ . Suppose that a randomly selected individual tests positive for the disease. What is the probability that this individual actually has the disease?

Let $A$ be the event “the person tests positive.” Let $B$ be the event “the person has the disease.” We then want to compute $P ( B | A )$ . By Bayes theorem,

$$
P ( B | A ) = \frac { P ( A | B ) P ( B ) } { P ( A ) } .
$$

We have that $P ( A | B )$ is 0.99, and that $P ( B )$ is 0.0001. To compute $P ( A )$ , we apply the law of total probability, considering separately the probability of a diseased individual testing positive and the probability of someone without the disease testing positive:

$$
P ( A ) = 0 . 9 9 \cdot 0 . 0 0 0 1 + 0 . 0 1 \cdot 0 . 9 9 9 9 = 0 . 0 1 0 0 9 8 .
$$

Thus

$$
P ( B | A ) = { \frac { 0 . 9 9 \cdot 0 . 0 0 0 1 } { 0 . 0 1 0 0 9 8 } } = 0 . 0 0 9 8 .
$$

In other words, even after a positive screening test, it is still unlikely that the individual will have the disease. The vast majority of those individuals who test positive will in fact not have the disease.

The concept of conditioning can be extended from simple events to distributions and expected values of random variables. If the distribution of $X$ depends on the value of $Y$ , then we can work with the conditional PDF $f _ { X \mid Y } ( x )$ , the conditional CDF $F _ { X \mid Y } ( a )$ , and the conditional expected value $E [ X | Y ]$ .

In this notation, we can also specify a particular value of $Y$ by using the notation $f _ { X \mid Y = \gamma }$ , $F _ { X \mid Y = \gamma }$ , or $E [ X | Y = \gamma ]$ . In working with conditional distributions and expected values, the following versions of the law of total probability can be very useful.

Theorem B.4 Given two random variables $X$ and $Y$ , with the distribution of $X$ depending on $Y$ , we can compute

$$
P ( X \leq a ) = \int _ { - \infty } ^ { \infty } P ( X \leq a | Y = \gamma ) f _ { Y } ( \gamma ) \ d \gamma
$$

and

$$
E [ X ] = \intop _ { - \infty } ^ { \infty } E [ X | Y = \gamma ] f _ { Y } ( \gamma ) d \gamma .
$$

# Example B.9

Let $U$ be a random variable uniformly distributed on (1, 2). Let $X$ be an exponential random variable with parameter $\lambda = U$ . We will find the expected value of $X$ :

$$
E [ X ] = \intop _ { 1 } ^ { 2 } E [ X | U = u ] f _ { U } ( u ) \ d u .
$$

Since the expected value of an exponential random variable with parameter $\lambda$ is $1 / \lambda$ , and the PDF of a uniform random variable on (1, 2) is $f _ { U } ( u ) = 1$ ,

$$
E [ X ] = \int _ { 1 } ^ { 2 } \frac { 1 } { u } d u = \log 2 .
$$

# B.5. THE MULTIVARIATE NORMAL DISTRIBUTION

Definition B.16 If the random variables $X _ { 1 }$ , . . . , $X _ { n }$ have a multivariate normal distribution (MVN), then the JDF is

$$
f ( { \bf x } ) = \frac { 1 } { ( 2 \pi ) ^ { n / 2 } } \frac { 1 } { \sqrt { \operatorname* { d e t } ( { \bf C } ) } } e ^ { - ( { \bf x } - { \boldsymbol \mu } ) ^ { T } { \bf C } ^ { - 1 } ( { \bf x } - { \boldsymbol \mu } ) / 2 }
$$

where $\mathbf { x } = [ X _ { 1 } , X _ { 2 } , . ~ . ~ . ~ , X _ { n } ] ^ { T }$ and $\mathbfcal \mu = [ \mu _ { 1 } , \mu _ { 2 } , \dots \dots , \mu _ { n } ] ^ { T }$ is a vector containing the expected values along each of the coordinate directions of $X _ { 1 }$ , . . . , $X _ { n }$ , and $\mathbf { C }$ contains the covariances between the random variables,

$$
C _ { i , j } = \operatorname { C o v } ( X _ { i } , X _ { j } ) .
$$

Note that if $\mathbf { C }$ is singular, then the JDF involves a division by zero, and is simply not defined.

The vector $\mu$ and the covariance matrix $\mathbf { C }$ completely characterize the MVN distribution. There are other multivariate distributions that are not completely characterized by the expected values and covariance matrix.

Theorem B.5 Let $\mathbf { x }$ be a multivariate normal random vector with expected values defined by the vector $\mu$ and covariance matrix $\mathbf { C }$ , and let $\mathbf { Y } = \mathbf { A } \mathbf { X }$ . Then $\mathbf { Y }$ is also multivariate normal, with

$$
E [ \mathbf { Y } ] = \mathbf { A } \mu
$$

and

$$
\mathbf { C o v } ( \mathbf { Y } ) = \mathbf { A C A } ^ { T } .
$$

Theorem B.6 If we have an $n$ -dimensional MVN distribution $\mathbf { x }$ with covariance matrix C and expected value $\mu$ , and the covariance matrix is of full rank, then the quantity

$$
Z = ( \mathbf { X } - { \boldsymbol { \mu } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { X } - { \boldsymbol { \mu } } )
$$

has a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom.

# Example B.10

We can generate vectors that are realizations of an MVN distribution with a known mean, $\mu$ , and covariance matrix, $\mathbf { C }$ , as follows.

1. Find the lower-triangular Cholesky factorization ${ \mathbf { C } } = { \mathbf { L } } { \mathbf { L } } ^ { T }$ .   
2. Let $\mathbf { z }$ be a vector of $n$ independent $N ( 0 , 1 )$ random numbers.   
3. Let $\mathbf { X } = \mu + \mathbf { L } \mathbf { Z }$ .

We can easily show that this procedure produces the desired distribution. Because $E [ \mathbf { Z } ] = \mathbf { 0 }$ , $E [ \mathbf { X } ] = \mu + \mathbf { L 0 } = \mu$ . Also, since $\mathrm { C o v } ( \mathbf { Z } ) = \mathbf { I }$ and $\mathrm { C o v } ( \mu ) = { \bf 0 }$ , $\operatorname { C o v } ( \mathbf { X } ) =$ $\operatorname { C o v } ( \mu + \mathbf { L } \mathbf { Z } ) = \operatorname { C o v } ( \mathbf { L } \mathbf { Z } ) = \mathbf { L } \mathbf { I } \mathbf { L } ^ { T } = \mathbf { C }$ using (B.64).

# B.6. THE CENTRAL LIMIT THEOREM

Theorem B.7 Let $X _ { 1 }$ , $X _ { 2 }$ , . . . , $X _ { n }$ be independent and identically distributed (IID) random variables with a finite expected value $\mu$ and variance $\sigma ^ { 2 }$ . Let

$$
Z _ { n } = { \frac { X _ { 1 } + X _ { 2 } + \cdot \cdot \cdot + X _ { n } - n \mu } { \sqrt { n } \sigma } } .
$$

In the limit as n approaches infinity, the distribution of $Z _ { n }$ approaches the standard normal distribution.

The central limit theorem shows why quasi-normally distributed random variables appear so frequently in nature; the sum of numerous independent random variables produces an approximately normal random variable, regardless of the distribution of the underlying IID variables. In particular, this is one reason that measurement errors are often normally distributed. As we will see in Chapter 2, having normally distributed measurement errors leads us to consider least squares solutions to parameter estimation and inverse problems.

# B.7. TESTING FOR NORMALITY

Many of the statistical procedures that we will use assume that data are normally distributed. Fortunately, the statistical techniques that we describe are generally robust in the face of small deviations from normality. Large deviations from the normal distribution can cause problems. Thus, it is important to be able to examine a data set to see whether the distribution is approximately normal.

Plotting a histogram of the data provides a quick view of the distribution. The histogram should show a roughly “bell-shaped” distribution, symmetrical around a single peak. If the histogram shows that the distribution is obviously skewed, then it would be unwise to assume that the data are normally distributed.

The Q-Q plot provides a more precise graphical test of whether a set of data could have come from a particular distribution. The data points,

$$
\mathbf { d } = [ d _ { 1 } , \ d _ { 2 } , \ . \ . \ . \ , \ d _ { n } ] ^ { T } ,
$$

are first sorted in numerical order from smallest to largest into a vector $\mathbf { y }$ , which is plotted versus

$$
x _ { i } = F ^ { - 1 } ( ( i - 0 . 5 ) / n ) \quad ( i = 1 , 2 , \dots , n ) ,
$$

where $F ( x )$ is the CDF of the distribution against which we wish to compare our observations.

If we are testing to see if the elements of $\mathbf { d }$ could have come from the normal distribution, then $F ( x )$ is the CDF for the standard normal distribution:

$$
F _ { N } ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { x } e ^ { - { \frac { 1 } { 2 } } z ^ { 2 } } d z .
$$

If the elements of $\mathbf { d }$ are normally distributed, the $Q \mathrm { - } Q$ plot points $( \gamma _ { i } , x _ { i } )$ will follow a straight line with a slope and intercept determined by the standard deviation and expected value, respectively, of the normal distribution that produced the data.

# Example B.11

Figure B.8 shows the histogram from a set of 1000 data points. The characteristic bell-shaped curve in the histogram might make it appear at first that these data are normally distributed. The sample mean is $- 0 . 0 1$ and the sample standard deviation is 1.41.

Figure B.9 shows the Q-Q plot for these data, which makes it apparent that the data set contains substantially more extreme values than the normal distribution would predict. In fact, these data were generated according to a $t$ distribution with 5 degrees of freedom, that has broader tails than the normal distribution (Figure B.3).

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/fd86d31db7361d09cd9d7d50006184aaa101c4a142cbb9730f94b6312afddb37.jpg)  
Figure B.8 Histogram of a sample data set.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0005_pages_0281-0350/auto/images/42e2383be4f18cc778e4ce1a49ce49a41ed7f7b30541839ad73e96abe62be110.jpg)  
Figure B.9 Q-Q plot for the sample data set.

There are a number of statistical tests for normality. These include the Kolmogorov-Smirnov test, Anderson-Darling test, and Lilliefors test. Each produces probabilistic measures called $\pmb { p }$ -values. A small $p$ -value indicates that the observed data would be unlikely if the distribution were in fact normal, while a larger $p .$ -value is consistent with normality.

# B.8. ESTIMATING MEANS AND CONFIDENCE INTERVALS

Given a collection of $n$ noisy measurements $m _ { 1 }$ , $m _ { 2 }$ , . . . , $m _ { n }$ of some quantity of interest, how can we estimate the true value $m$ , and how uncertain is this estimate? This is a classic problem in statistics.

We will assume first that the measurement errors are independent and normally distributed with expected value 0 and some unknown standard deviation $\sigma$ . Equivalently, the measurements themselves are normally distributed with expected value $m$ and standard deviation $\sigma$ .

We begin by computing the measurement average,

$$
{ \bar { m } } = { \frac { m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { n } } { n } } .
$$

This sample mean $\bar { m }$ will serve as our estimate of $m$ . We will also compute an estimate $s$ of the standard deviation

$$
s = \sqrt { \frac { \sum _ { i = 1 } ^ { n } ( m _ { i } - \bar { m } ) ^ { 2 } } { n - 1 } } .
$$

The key to our approach to estimating $m$ is the following theorem.

Theorem B.8 (The Sampling Theorem) Under the assumption that measurements are independent and normally distributed with expected value m and standard deviation $\sigma$ , the random quantity

$$
t = \frac { m - \bar { m } } { s / \sqrt { n } }
$$

has a Student’s t distribution with $n - 1$ degrees of freedom.

If we had the true standard deviation $\sigma$ instead of the estimate $s$ , then $t$ would in fact be normally distributed with expected value 0 and standard deviation 1. This does not quite work out because we have used an estimate $s$ of the standard deviation. For smaller values of $n$ , the estimate $s$ is less accurate, and the $t$ distribution therefore has fatter tails than the standard normal distribution. As $n$ becomes large, $s$ becomes a better estimate of $\sigma$ and it can be shown that the $t$ distribution converges to a standard normal distribution [47].

Let $t _ { n - 1 , 0 . 9 7 5 }$ be the $9 7 . 5 \%$ -tile of the $t$ distribution and let $t _ { n - 1 , 0 . 0 2 5 }$ be the $2 . 5 \% \AA$ -tile of the $t$ distribution. Then

$$
P \bigg ( t _ { n - 1 , 0 . 0 2 5 } \leq \frac { m - \bar { m } } { s / \sqrt { n } } \leq t _ { n - 1 , 0 . 9 7 5 } \bigg ) = 0 . 9 5 .
$$

This can be rewritten as

$$
P \big ( \big ( t _ { n - 1 , 0 . 0 2 5 } s / \sqrt { n } \big ) \leq ( m - \bar { m } ) \leq \big ( t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n } \big ) \big ) = 0 . 9 5 .
$$

We can construct the√ $9 5 \%$ confidence interval for √ $m$ as the interval from $\bar { m } +$ $t _ { n - 1 , 0 . 0 2 5 } s / \sqrt { n }$ to $\bar { m } + t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n }$ . Because the $t$ distribution is symmetric, this can√ also be written as $\bar { m } - t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n }$ to $\bar { m } + t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n }$ .

As we have seen, there is a $9 5 \%$ probability that when we construct the confidence interval, that interval will contain the true mean, m. Note that we have not said that, given a particular set of data and the resulting confidence interval, there is a $9 5 \%$ probability that $m$ is in the confidence interval. The semantic difficulty here is that $m$ is not a random variable, but is rather some true fixed quantity that we are estimating; the measurements $m _ { 1 } , m _ { 2 } , \ldots . m _ { n }$ , and the calculated m¯ , s, and confidence interval are the random quantities.

# Example B.12

Suppose that we want to estimate the mass of an object and obtain the following ten measurements of the mass (in grams):

$$
\begin{array} { r r r r r } { 9 . 9 8 } & { { } 1 0 . 0 7 } & { 9 . 9 4 } & { { } 1 0 . 2 2 } & { 9 . 9 8 } \\ { 1 0 . 0 1 } & { { } 1 0 . 1 1 } & { { } 1 0 . 0 1 } & { 9 . 9 9 } & { { } 9 . 9 2 } \end{array}
$$

The sample mean is $\bar { m } = 1 0 . 0 2 ~ \mathrm { g }$ . The sample standard deviation is $s = 0 . 0 8 8 3$ grams. The $9 7 . 5 \%$ -tile of the $t$ distribution with $n - 1 = 9$ degrees of freedom is (from a $t \cdot$ -table or function) 2.262. Thus our $9 5 \%$ confidence interval for the mean is

$$
\left[ \bar { m } - 2 . 2 6 2 s / \sqrt { n } , \bar { m } + 2 . 2 6 2 s / \sqrt { n } \right] \mathrm { g } .
$$

Substituting the values for ${ \bar { m } } , s ,$ , and $n$ , we get an interval of

$$
\left[ 1 0 . 0 2 - 2 . 2 6 2 \cdot 0 . 0 8 8 3 / \sqrt { 1 0 } , 1 0 . 0 2 + 2 . 2 6 2 \cdot 0 . 0 8 8 3 / \sqrt { 1 0 } \right] \mathrm { g }
$$

or

The above procedure for constructing a confidence interval for the mean using the $t$ distribution was based on the assumption that the measurements were normally distributed. In situations where the data are not normally distributed, this procedure can fail in a very dramatic fashion (Exercise B.9). However, it may be safe to generate an approximate confidence interval using this procedure if (1) the number $n$ of data is large (50 or more) or (2) the distribution of the data is not strongly skewed and $n$ is at least 15.

# B.9. HYPOTHESIS TESTS

In some situations we want to test whether a set of normally distributed data could reasonably have come from a normal distribution with expected value $\mu _ { 0 }$ . Applying the sampling theorem, we see that if our data did come from a normal distribution with expected value $\mu _ { 0 }$ , then there would be a $9 5 \%$ probability that

$$
t _ { \mathrm { o b s } } = \frac { \mu _ { \mathrm { 0 } } - \bar { m } } { s / \sqrt { n } }
$$

would lie in the interval

$$
[ F _ { t } ^ { - 1 } ( 0 . 0 2 5 ) , F _ { t } ^ { - 1 } ( 0 . 9 7 5 ) ] = [ t _ { n - 1 , 0 . 0 2 5 } , t _ { n - 1 , 0 . 9 7 5 } ] ,
$$

and only a $5 \%$ probability that $t$ would lie outside this interval. Equivalently, there is only a $5 \%$ probability that $| t _ { \mathrm { o b s } } | \geq t _ { n - 1 , 0 . 9 7 5 }$ .

This leads to the $\scriptstyle { \mathbf { \alpha } } _ { t } .$ -test: If $| t _ { \mathrm { o b s } } | \geq t _ { n - 1 , 0 . 9 7 5 }$ , then we reject the hypothesis that $\mu = \mu _ { 0 }$ . On the other hand, if $| t _ { \mathrm { o b s } } | < t _ { n - 1 , 0 . 9 7 5 }$ , then we cannot reject the hypothesis that $\mu = \mu _ { 0 }$ . Although the $9 5 \%$ confidence level is traditional, we can also perform the $t \cdot$ -test at a $9 9 \%$ or some other confidence level. In general, if we want a confidence level of 1 − α, then we compare |tobs| to tn−1,1−α/2.

In addition to reporting whether or not a set of data passes a $t \cdot$ -test, it is good practice to report the associated $t \cdot$ -test $p$ -value. The $p$ -value associated with a $t \cdot$ -test is the largest value of $\alpha$ for which the data passes the $t \cdot$ -test. Equivalently, it is the probability that we could have gotten a greater $t$ value than we have observed, given that all of our assumptions are correct.

# Example B.13

Consider the following data:

These appear to be roughly normally distributed, with a mean that seems to be larger than 0. We will test the hypothesis $\mu = 0$ . The $t$ statistic is

$$
t _ { \mathrm { o b s } } = \frac { \mu _ { \mathrm { 0 } } - \bar { m } } { s / \sqrt { n } } ,
$$

which, for this data set, is

$$
t _ { \mathrm { o b s } } = { \frac { 0 - 1 . 0 2 5 3 } { 1 . 1 8 9 5 / { \sqrt { 1 0 } } } } \approx - 2 . 7 2 5 .
$$

Because $| t _ { \mathrm { o b s } } |$ is larger than $t 9 , 0 . 9 7 5 = 2 . 2 6 2$ , we reject the hypothesis that these data came from a normal distribution with expected value 0 at the $9 5 \%$ confidence level.

The $t \cdot$ -test (or any other statistical test) can fail in two ways. First, it could be that the hypothesis that $\mu = \mu _ { 0 }$ is true, but our particular data set contained some unlikely values and failed the $t \cdot$ -test. Rejecting the hypothesis when it is in fact true is called a type I error. We can control the probability of a type I error by decreasing $\alpha$ .

The second way in which the $t \cdot$ -test can fail is more difficult to control. It could be that the hypothesis $\mu = \mu _ { 0 }$ was false, but the sample mean was close enough to $\mu _ { 0 }$ to pass the $t \cdot$ -test. In this case, we have a type $\mathbf { I I }$ error. The probability of a type II error depends very much on how close the true mean is to $\mu _ { \mathrm { 0 } }$ . If the true mean $\mu = \mu _ { 1 }$ is very close to $\mu _ { 0 }$ , then a type II error is quite likely. If the true mean $\mu = \mu _ { 1 }$ is very far from $\mu _ { 0 }$ , then a type II error will be less likely. Given a particular alternative hypothesis, $\mu = \mu _ { 1 }$ , we call the probability of a type $\mathrm { I I }$ error $\beta ( \mu _ { 1 } )$ , and call the probability of not making a type II error $( 1 - \beta ( \mu _ { 1 } ) )$ the power of the test. We can estimate $\beta ( \mu _ { 1 } )$ by repeatedly generating sets of $n$ random numbers with $\mu = \mu _ { 1 }$ and performing the hypothesis test on the sets of random numbers (Exercise B.10).

The results of a hypothesis test should always be reported with care. It is important to discuss and justify any assumptions (such as the normality assumption made in the $t \cdot$ -test) underlying the test. The $p$ -value should always be reported along with whether the hypothesis was rejected. If the hypothesis was not rejected and some particular alternative hypothesis is available, it is good practice to estimate the power of the hypothesis test against this alternative hypothesis. Confidence intervals for the mean should be reported along with the results of a hypothesis test.

It is important to distinguish between the statistical significance of a hypothesis test and the actual magnitude of any difference between the observed mean and the hypothesized mean. For example, with very large $n$ it is nearly always possible to achieve statistical significance at the $9 5 \%$ confidence level, even though the observed mean may differ from the hypothesis by only $1 \%$ or less.

# B.10. EXERCISES

1. Compute the expected value and variance of a uniform random variable in terms of the parameters $a$ and $b$ .

2. Compute the CDF of an exponential random variable with parameter $\lambda$ . You may find the MATLAB library function exprand.m to be useful here.

3. Show that

$$
\operatorname { C o v } ( a X , Y ) = a \operatorname { C o v } ( X , Y )
$$

and that

$$
\operatorname { C o v } ( X + Y , Z ) = \operatorname { C o v } ( X , Z ) + \operatorname { C o v } ( Y , Z ) .
$$

4. Show that the PDF for the sum of two independent uniform random variables on [a $\iota , b ] = [ 0 , 1 ]$ is

$$
f ( x ) = \left\{ \begin{array} { l l } { 0 \quad ( x \leq 0 ) } \\ { x \quad ( 0 \leq x \leq 1 ) } \\ { 2 - x \quad ( 1 \leq x \leq 2 ) } \\ { 0 \quad ( x \geq 2 ) . } \end{array} \right.
$$

5. Suppose that $X$ and $Y$ are independent random variables. Use conditioning to find a formula for the CDF of $X + Y$ in terms of the PDFs and CDFs of $X$ and $Y$ .

6. Suppose that ${ \bf x } = ( X _ { 1 } , X _ { 2 } ) ^ { T }$ is a vector composed of two random variables with a multivariate normal distribution with expected value $\mu$ and covariance matrix $\mathbf { C }$ , and that A is a 2 by 2 matrix. Use properties of expected value and covariance to show that $\mathbf { y } = \mathbf { A } \mathbf { x }$ has expected value $\mathbf { A } \mu$ and covariance $\mathbf { A } \mathbf { C } \mathbf { A } ^ { T }$ .

7. Suppose that $\mathbf { x }$ is a multivariate normal random variable with mean vector $\mu$ and covariance matrix $\mathbf { C }$ . Use Theorem B.5 to show that the ith component of $\mathbf { x }$ , $\mathbf { x } _ { i }$ , is normally distributed with mean $\mu _ { i }$ and variance $\mathbf { C } _ { i , i }$ . Hint: Let $\mathbf { A } = \mathbf { e } _ { i } ^ { T }$ , where $\mathbf { e } _ { i }$ is the ith column of the identity matrix.

8. Consider the following data, which we will assume are drawn from a normal distribution.

$$
\begin{array} { r r r r } { - 0 . 4 3 2 6 } & { { } - 1 . 6 6 5 6 } & { 0 . 1 2 5 3 } & { 0 . 2 8 7 7 } & { { } - 1 . 1 4 6 5 } \\ { 1 . 1 9 0 9 } & { { } 1 . 1 8 9 2 } & { - 0 . 0 3 7 6 } & { { } 0 . 3 2 7 3 } & { 0 . 1 7 4 6 } \end{array}
$$

Find the sample mean and standard deviation. Use these to construct a $9 5 \%$ confidence interval for the mean. Test the hypothesis $H _ { 0 } : \mu = 0$ at the $9 5 \%$ confidence level. What do you conclude? What was the corresponding $p$ -value?

9. Using MATLAB, repeat the following experiment 1000 times. Generate five exponentially distributed random numbers from the exponential probability density function (B.10) with means $\mu = 1 / \lambda = 1 0$ . You may find the library function exprand to be useful here. Use (B.74) to calculate a $9 5 \%$ confidence interval for the 1000 mean determinations. How many times out of the 1000 experiments did the $9 5 \%$ confidence interval cover the expected value of 10? What happens if you instead generate 50 exponentially distributed random numbers at a time? Discuss your results.

10. Using MATLAB, repeat the following experiment 1000 times. Use the randn function to generate a set of 10 normally distributed random numbers with expected value 10.5 and standard deviation 1. Perform a $t \cdot$ -test of the hypothesis $\mu = 1 0$ at the $9 5 \%$ confidence level. How many type II errors were committed? What is the approximate power of the $t \cdot$ -test with $n = 1 0$ against the alternative hypothesis $\mu = 1 0 . 5 ?$ Discuss your results.

11. Using MATLAB, repeat the following experiment 1000 times. Generate five exponentially distributed random numbers with expected value 10. You may find the library function exprand to be useful here. Take the average of the five random numbers. Plot a histogram and a $Q \mathrm { - } Q$ plot of the 1000 averages that you computed. Are the averages approximately normally distributed? Explain why or why not. What would you expect to happen if you took averages of 50 exponentially distributed random numbers at a time? Try it and discuss the results.

# B.11. NOTES AND FURTHER READING

Most of the material in this Appendix can be found in virtually any introductory textbook in probability and statistics. Some recent textbooks include [4, 29]. The multivariate normal distribution is a somewhat more advanced topic that is often ignored in introductory courses. Searle [139] has a good discussion of the multivariate normal distribution and its properties. Numerical methods for probability and statistics are a specialized topic. Two standard references include [89, 157].

# Review of Vector Calculus

# Synopsis

A review of key vector calculus topics, including the gradient, Hessian, Jacobian, Taylor’s theorem, and Lagrange multipliers.

# C.1. THE GRADIENT, HESSIAN, AND JACOBIAN

In vector calculus, the familiar first and second derivatives of a single-variable function are generalized to operate on vectors.

Definition C.1 Given a scalar-valued function with a vector argument, $f ( \mathbf { x } )$ , the gradient of $f$ is

$$
\begin{array} { r } { \nabla f ( \mathbf { x } ) = \left[ \begin{array} { c } { \frac { \partial f } { \partial x _ { 1 } } } \\ { \frac { \partial f } { \partial x _ { 2 } } } \\ { \vdots } \\ { \frac { \partial f } { \partial x _ { n } } } \end{array} \right] . } \end{array}
$$

The vector $\nabla f ( \mathbf { x } )$ has an important geometric interpretation in that it points in the direction in which $f ( \mathbf { x } )$ increases most rapidly at the point $\mathbf { x }$ .

Recall from single-variable calculus that if a function $f$ is continuously differentiable, then a point $x ^ { * }$ can only be a minimum or maximum point of $f$ if $\stackrel { \cdot } { f } ^ { \prime } ( x ) | _ { x = x ^ { * } } = 0$ . Similarly in vector calculus, if $f ( \mathbf { x } )$ is continuously differentiable, then a point $\mathbf { x } ^ { * }$ can only be a minimum or maximum point if $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ . In more than one dimension, a point $\mathbf { x } ^ { * }$ where $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ can also be a saddle point. Any point where $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ is called a critical point.


<!-- chunk 0006: pages 351-377 -->
Definition C.2 Given a scalar-valued function of a vector, $f ( \mathbf { x } )$ , the Hessian of $f$ is a square matrix of partial derivatives given by

$$
\mathbf { H } ( f ( \mathbf { x } ) ) = \left[ \begin{array} { c c c c } { \frac { \partial ^ { 2 } f } { \partial x _ { 1 } ^ { 2 } } } & { \frac { \partial ^ { 2 } f } { \partial x _ { 1 } \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial ^ { 2 } f } { \partial x _ { 1 } \partial x _ { n } } } \\ { \frac { \partial ^ { 2 } f } { \partial x _ { 2 } \partial x _ { 1 } } } & { \frac { \partial ^ { 2 } f } { \partial x _ { 2 } ^ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial ^ { 2 } f } { \partial x _ { 2 } \partial x _ { n } } } \\ { \vdots } & { \vdots } & { \cdot } & { \vdots } \\ { \frac { \partial ^ { 2 } f } { \partial x _ { n } \partial x _ { 1 } } } & { \frac { \partial ^ { 2 } f } { \partial x _ { n } \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial ^ { 2 } f } { \partial x _ { n } ^ { 2 } } } \end{array} \right] .
$$

If $\dot { \boldsymbol { f } }$ is twice continuously differentiable, the Hessian is symmetric. It is common in mathematics to write the Hessian using the operator $\nabla ^ { 2 }$ , but this sometimes leads to confusion with another vector calculus operator, the Laplacian.

Theorem C.1 If $f ( \mathbf { x } )$ is a twice continuously differentiable function, and $\mathbf { H } ( f ( \mathbf { x } _ { \mathrm { 0 } } ) )$ is a positive semidefinite matrix, then $f ( \mathbf { x } )$ is a convex function at $\mathbf { x } _ { \mathrm { 0 } }$ . If $\mathbf { H } ( f ( \mathbf { x } _ { \mathrm { 0 } } ) )$ is positive definite, then $f ( \mathbf { x } )$ is strictly convex at $\mathbf { x } _ { \mathrm { 0 } }$ .

This theorem can be used to check whether a critical point is a minimum of $f$ . If $\mathbf { x } ^ { * }$ is a critical point of $f$ and $\mathbf { H } ( f ( \mathbf { x } ^ { * } ) )$ is positive definite, then $f$ is convex at $\mathbf { x } ^ { * } ,$ , and $\mathbf { x } ^ { * }$ is thus a local minimum of $f$ .

It will be necessary to compute derivatives of quadratic forms.

Theorem C.2 Let $f ( \mathbf { x } ) = \mathbf { x } ^ { T } \mathbf { A } \mathbf { x }$ , where A is an n by $n$ symmetric matrix. Then

$$
\nabla f ( \mathbf { x } ) = 2 \mathbf { A } \mathbf { x }
$$

and

$$
\mathbf { H } ( f ( \mathbf { x } ) ) = 2 \mathbf { A } .
$$

Definition C.3 Given a vector-valued function of a vector, $\mathbf { F } ( \mathbf { x } )$ , where

$$
\begin{array} { r } { \mathbf { F } ( \mathbf { x } ) = \left[ \begin{array} { c } { f _ { 1 } ( \mathbf { x } ) } \\ { f _ { 2 } ( \mathbf { x } ) } \\ { \vdots } \\ { f _ { m } ( \mathbf { x } ) } \end{array} \right] , } \end{array}
$$

the Jacobian of $\mathbf { F }$ is

$$
\begin{array} { r } { \mathbf { J } ( \mathbf { x } ) = \left[ \begin{array} { c c c c c } { \frac { \partial f _ { 1 } } { \partial x _ { 1 } } } & { \frac { \partial f _ { 1 } } { \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial f _ { 1 } } { \partial x _ { n } } } \\ { \frac { \partial f _ { 2 } } { \partial x _ { 1 } } } & { \frac { \partial f _ { 2 } } { \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial f _ { 2 } } { \partial x _ { n } } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial f _ { m } } { \partial x _ { 1 } } } & { \frac { \partial f _ { m } } { \partial x _ { 2 } } } & { \cdot \cdot \cdot } & { \frac { \partial f _ { m } } { \partial x _ { n } } } \end{array} \right] . } \end{array}
$$

Some authors use the notation $\nabla \mathbf { F } ( \mathbf { x } )$ for the Jacobian. Note that the rows of J $\lceil ( \mathbf { x } )$ are the gradients (C.1) of the functions $f _ { 1 } ( { \bf x } ) , f _ { 2 } ( { \bf x } ) , \ldots . . . , f _ { m } ( { \bf x } )$ .

# C.2. TAYLOR’S THEOREM

In the calculus of single-variable functions, Taylor’s theorem produces an infinite series for $f ( x + \Delta x )$ in terms of $f ( x )$ and its derivatives. Taylor’s theorem can be extended to a function of a vector $f ( \mathbf { x } )$ , but in practice, derivatives of order higher than 2 are extremely inconvenient. The following form of Taylor’s theorem is often used in optimization theory.

Theorem C.3 Suppose that $f ( \mathbf { x } )$ and its first and second partial derivatives are continuous. For any vectors $\mathbf { x }$ and $\Delta \mathbf { x }$ , there is a vector $\mathbf { c }$ , with $\mathbf { c }$ on the line between $\mathbf { x }$ and $\mathbf { x } + \Delta \mathbf { x }$ , such that

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) = f ( \mathbf { x } ) + \nabla f ( \mathbf { x } ) ^ { T } \Delta \mathbf { x } + \frac { 1 } { 2 } \Delta \mathbf { x } ^ { T } \mathbf { H } ( \mathbf { \nabla } f ( \mathbf { c } ) ) \Delta \mathbf { x } .
$$

This form of Taylor’s theorem with remainder term is useful in many proofs. However, in computational work there is no way to determine c. For that reason, when $\Delta \mathbf { x }$ is a small perturbation, we often make use of the approximation

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) \approx f ( \mathbf { x } ) + \nabla f ( \mathbf { x } ) ^ { T } \Delta \mathbf { x } + \frac { 1 } { 2 } \Delta \mathbf { x } ^ { T } \mathbf { H } ( \mathbf { \nabla } f ( \mathbf { x } ) ) \Delta \mathbf { x } .
$$

An even simpler version of Taylor’s theorem, called the mean value theorem, uses only the first derivative.

Theorem C.4 Suppose that $f ( \mathbf { x } )$ and its first partial derivatives are continuous. For any vectors x and $\Delta \mathbf { x }$ there is a vector $\mathbf { c }$ , with $\mathbf { c }$ on the line between $\mathbf { x }$ and $\mathbf { x } + \Delta \mathbf { x }$ such that

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) = f ( \mathbf { x } ) + \nabla f ( \mathbf { c } ) ^ { T } \Delta \mathbf { x } .
$$

We will make use of a truncated version of (C.8):

$$
f ( \mathbf { x } + \Delta \mathbf { x } ) \approx f ( \mathbf { x } ) + \nabla f ( \mathbf { x } ) ^ { T } \Delta \mathbf { x } .
$$

By applying (C.10) to each of the functions $f _ { 1 } ( { \bf x } ) , f _ { 2 } ( { \bf x } ) , \ldots . . . , f _ { m } ( { \bf x } )$ , we obtain the approximation

$$
\mathbf { F } ( \mathbf { x } + \Delta \mathbf { x } ) \approx \mathbf { F } ( \mathbf { x } ) + \mathbf { J } ( \mathbf { x } ) \Delta \mathbf { x } .
$$

# C.3. LAGRANGE MULTIPLIERS

The method of Lagrange multipliers is an important technique for solving optimization problems of the form:

$$
\begin{array} { l } { \operatorname* { m i n } { f ( \mathbf { x } ) } } \\ { g ( \mathbf { x } ) = 0 , } \end{array}
$$

where the scalar-valued function of a vector argument, $f ( \mathbf { x } )$ , is called the objective function.

Figure C.1 shows a general situation. The solid contour represents the set of points where the (nonconstant) function $g ( \mathbf { x } ) = 0$ , and the dashed contours are those of another function $f ( \mathbf { x } )$ that has a minimum as indicated. Moving along the $g ( \mathbf { x } ) = 0$ contour, we can trace out the curve ${ \mathbf x } ( t )$ , parameterized by the variable $t \geq 0$ , where $g ( \mathbf { x } ( t ) ) = 0$ and $t$ increases as we progress counter-clockwise. At any point ${ \bf x } ( t )$ on the contour, the gradient of $g ( \mathbf { x } ( t ) )$ must be perpendicular to the contour because the function is constant along this curve. Note that in Figure $\mathbf { C } . 1 , g ( \mathbf { x } )$ increases in the outward direction relative to the contour, so the gradient of $g ( \mathbf { x } )$ will be outward.

By the chain rule,

$$
f ^ { \prime } ( \mathbf { x } ( t ) ) = \mathbf { x } ^ { \prime } ( t ) ^ { T } \nabla f ( \mathbf { x } ( t ) ) ,
$$

where ${ \mathbf { x } } ^ { \prime } ( t )$ is the counter-clockwise tangent to the contour $g ( x ) = 0$ . For the point $\mathbf { x } _ { 1 } = \mathbf { x } ( t _ { 1 } )$ in Figure C.1, $\nabla f ( \mathbf { x } _ { 1 } )$ and $\mathbf { x } ^ { \prime } ( t _ { 1 } )$ are at an obtuse angle, and their dot product $f ^ { \prime } ( \mathbf { x } _ { 1 } )$ (C.13) will therefore be negative. Thus, $f ( \mathbf { x } )$ is decreasing as we move counterclockwise around the contour $g ( \mathbf { x } ) = 0$ from $\mathbf { x } _ { 1 }$ , and $\mathbf { x } _ { 1 }$ cannot satisfy (C.12).

In Figure C.2, for the point ${ \mathbf x } _ { 0 } = { \mathbf x } ( t _ { 0 } )$ , $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ is perpendicular to the curve $g ( \mathbf { x } ) = 0$ . In this case, by (C.13), $f ^ { \prime } ( \mathbf { x } _ { \mathrm { 0 } } ) = 0$ , and the point $\mathbf { x } _ { \mathrm { 0 } }$ may or may not be a minimum for $f ( \mathbf { x } )$ along the contour. Figure C.2 shows that a point $\mathbf { x } _ { \mathrm { 0 } }$ on the curve $g ( \mathbf { x } ) = 0$ can only be a possible minimum point for $f ( \mathbf { x } )$ if $\nabla g ( \mathbf { x } _ { \mathrm { 0 } } )$ and $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ are parallel or antiparallel. A point where this occurs is called a stationary point.

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0006_pages_0351-0377/auto/images/5c07e974532333a5095aa2e88fdb180338c20ccca4c6e36cfd31036559f60805.jpg)  
Figure C.1 The situation at a point $\mathbf { x } _ { 1 } = \mathbf { x } ( t _ { 1 } )$ along the contour $g ( \mathbf { x } ) = 0$ that is not a minimum of $f ( \mathbf { x } )$ and thus does not satisfy (C.12).

Finding a stationary point is necessary, but not sufficient, for finding a minimum of $f ( \mathbf { x } )$ along the contour $g ( \mathbf { x } ) = 0$ , because such a point may be a minimum, maximum, or saddle point. Furthermore, a problem may have several local minima. Thus it is necessary to examine the behavior of $f ( \mathbf { x } )$ at all stationary points to find a global minimum.

Theorem C.5 (C.12) can only be satisfied at a point $\mathbf { x } _ { \mathrm { 0 } }$ where

$$
\nabla f ( \mathbf { x } _ { 0 } ) + \lambda \nabla g ( \mathbf { x } _ { 0 } ) = \mathbf { 0 }
$$

for some λ. λ is called a Lagrange multiplier.

The Lagrange multiplier condition can be extended to problems of the form

$$
\begin{array} { l } { \operatorname* { m i n } { f ( \mathbf { x } ) } } \\ { g ( \mathbf { x } ) \leq 0 . } \end{array}
$$

Since points along the curve $g ( \mathbf { x } ) = 0$ are still feasible in (C.15), (C.14) must still hold true. However, there is an additional restriction. Suppose that $\nabla g ( \mathbf { x } _ { \mathrm { 0 } } )$ and $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ both point in the outward direction, as in Figure C.2. In this case, we can move in the opposite direction, into the feasible region to decrease $f ( \mathbf { x } )$ (e.g., in the situation depicted in Figure C.2, the solution to (C.15) is simply the indicated minimum of $f ( \mathbf { x } ) )$ . Thus, a point $\mathbf { x } _ { \mathrm { 0 } }$ satisfying (C.14) cannot satisfy (C.15) unless the gradients of $g ( \mathbf { x } _ { \mathrm { 0 } } )$ and $f ( \mathbf { x } _ { \mathrm { 0 } } )$ point in opposite directions.

Theorem C.6 (C.15) can only be satisfied at a point $\mathbf { x } _ { \mathrm { 0 } }$ where

$$
\nabla f ( \mathbf { x } _ { 0 } ) + \lambda \nabla g ( \mathbf { x } _ { 0 } ) = \mathbf { 0 }
$$

for some Lagrange multiplier $\lambda > 0$ .

![](../chunks/Parameter Estimation and Inverse Problems, Second Edition (Richard C. Aster, Brian Borcher_part_0006_pages_0351-0377/auto/images/2521b9c3a199f095c94eda5071a3db82804844f576553748f86ae7ac65ce5b89.jpg)  
Figure C.2 The situation at a point ${ \mathbf x } _ { 0 } = { \mathbf x } ( t _ { 0 } )$ along the contour $g ( \mathbf { x } ) = 0$ that is a minimum of $f ( \mathbf { x } )$ and thus satisfies (C.12). Note that $\nabla g ( \mathbf { x } _ { 0 } )$ and $\nabla f ( \mathbf { x } _ { \mathrm { 0 } } )$ are parallel.

# Example C.1

Consider a simple example in two variables where $f ( \mathbf { x } )$ defines linear contours and $g ( \mathbf { x } ) = 0$ defines a unit circle

$$
\begin{array} { r l } { \operatorname* { m i n } \ x _ { 1 } + x _ { 2 } } & { } \\ { \quad \quad \ d { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } - 1 } \leq 0 . } \end{array}
$$

The Lagrange multiplier condition is

$$
{ \binom { 1 } { 1 } } + \lambda \left[ { 2 x _ { 1 } } \right] = \mathbf { 0 } .
$$

One stationary point solution to this nonlinear system of equations is $x _ { 1 } = 0 . 7 0 7 1$ , $x _ { 2 } = 0 . 7 0 7 1$ , with $\lambda = - 0 . 7 0 7 1 .$ . This is the maximum $\operatorname { o f } f ( \mathbf { x } )$ subject to $g ( \mathbf { x } ) \leq 0$ . The second solution to (C.18) is $x _ { 1 } = - 0 . 7 0 7 1$ , $x _ { 2 } = - 0 . 7 0 7 1$ , with $\lambda = 0 . 7 0 7 1$ . Because this is the only solution with $\lambda > 0$ , so that $\nabla f ( \mathbf { x } )$ and $\nabla g ( \mathbf { x } )$ are antiparallel, this solves the minimization problem.

Note that (C.16) is (except for the non-negativity constraint on $\lambda$ ) the necessary condition for a minimum point of the unconstrained minimization problem,

$$
\operatorname* { m i n } { f ( \mathbf { x } ) } + \lambda g ( \mathbf { x } ) .
$$

Here the parameter $\lambda$ can be adjusted so that, for the optimal solution, $\mathbf { x } ^ { * } , g ( \mathbf { x } ^ { * } ) \leq 0$ . We will make frequent use of this technique to convert constrained optimization problems into unconstrained optimization problems.

# C.4. EXERCISES

1. Let

$$
f ( { \bf x } ) = x _ { 1 } ^ { 2 } x _ { 2 } ^ { 2 } - 2 x _ { 1 } x _ { 2 } ^ { 2 } + x _ { 2 } ^ { 2 } - 3 x _ { 1 } ^ { 2 } x _ { 2 } + 1 2 x _ { 1 } x _ { 2 } - 1 2 x _ { 2 } + 6 .
$$

Find the gradient, $\nabla f ( \mathbf { x } )$ , and Hessian, $\mathbf { H } ( f ( \mathbf { x } ) )$ . What are the critical points of $\dot { \boldsymbol { f } }$ ?

Which of these are minima and maxima of $f$

2. Find a Taylor’s series approximation for $f ( \mathbf { x } + \Delta \mathbf { x } )$ , where

$$
f ( \mathbf { x } ) = e ^ { - ( x _ { 1 } + x _ { 2 } ) ^ { 2 } }
$$

is near the point

$$
\mathbf { x } = { \binom { 2 } { 3 } } .
$$

3. Use the method of Lagrange multipliers to solve the problem,

$$
\begin{array} { l } { \operatorname* { m i n } \ : 2 x _ { 1 } + x _ { 2 } \qquad } \\ { 4 x _ { 1 } ^ { 2 } + 3 x _ { 2 } ^ { 2 } - 5 \leq 0 . } \end{array}
$$

4. Derive the formula (A.89) for the 2-norm of a matrix. Begin with the maximization problem,

$$
\operatorname* { m a x } _ { \| \mathbf { x } \| _ { 2 } = 1 } ~ \| \mathbf { A x } \| _ { 2 } ^ { 2 } .
$$

Note that we have squared $\| \mathbf { A x } \| _ { 2 }$ . We will take the square root at the end of the problem.

i. Using the formula $\| \mathbf { x } \| _ { 2 } = \sqrt { \mathbf { x } ^ { T } \mathbf { x } }$ , rewrite the above maximization problem without norms.   
ii. Use the Lagrange multiplier method to find a system of equations that must be satisfied by any stationary point of the maximization problem.   
iii. Explain how the eigenvalues and eigenvectors of $\mathbf { A } ^ { T } \mathbf { A }$ are related to this system of equations. Express the solution to the maximization problem in terms of the eigenvalues and eigenvectors of $\mathbf { A } ^ { T } \mathbf { A }$ .   
iv. Use this solution to get $\| \mathbf { A } \| _ { 2 }$ .

5. Derive the normal equations (2.3) using vector calculus, by letting

$$
f ( \mathbf { m } ) = \| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 }
$$

and minimizing $f ( \mathbf { m } )$ . Note that in problems with many least squares solutions, all of the least squares solutions will satisfy the normal equations.

i. Rewrite $f ( \mathbf { m } )$ as a dot product and then expand the expression.   
ii. Find $\nabla f ( \mathbf { m } )$ .   
iii. Set $\nabla f ( \mathbf { m } ) = \mathbf { 0 }$ , and obtain the normal equations.

# C.5. NOTES AND FURTHER READING

Basic material on vector calculus can be found in many calculus textbooks. However, more advanced topics, such as Taylor’s theorem for functions of a vector, are often skipped in basic texts. The material in this chapter is particularly important in optimization, and can often be found in associated references [58, 105, 119].

# Glossary of Notation

• α, $\beta$ , γ , ...: Scalars.   
• a, b, c, ...: Scalar-valued functions or scalars.   
a, b, c, ...: Column vectors. $a _ { i }$ : ith element of vector a.   
A, B, C, ...: Scalar-valued functions or random variables.   
A, B, C, ...: Fourier transforms.   
A, B, C, ...: Vector-valued functions or matrices. $\mathbf { A } _ { i } ,$ ·: ith row of matrix A. $\mathbf { A } _ { \cdot , i }$ : ith column of matrix A. $A _ { i , j }$ : (i, $j )$ th element of matrix A. $\mathbf { A } ^ { - 1 }$ : Inverse of matrix A. $\mathbf { A } ^ { T }$ : Transpose of matrix A. $\mathbf { x } ^ { * }$ : Complex conjugate of matrix x. $\mathbf { A } ^ { H }$ : Complex conjugate transpose of matrix A. a $_ { \odot \mathbf { b } }$ : Vector constructed by element-by-element multiplication of vectors $\mathbf { a }$ and b. a $\oslash \mathbf { b }$ : Vector constructed by element-by-element division of vector a by $\mathbf { b }$ . $\mathbf { A } ^ { - T }$ : Transpose of matrix $\mathbf { A } ^ { - 1 }$ . $R ^ { n }$ : Space of $n$ -dimensional real vectors. $N ( \mathbf { A } )$ : Null space of matrix A. $R ( \mathbf { A } )$ : Range of matrix A. rank(A): Rank of matrix A. $\mathrm { T r } ( \mathbf A )$ : Trace of matrix A. $\| \mathbf { x } \|$ : Norm of vector x. A subscript is used to specify the 1-norm, 2-norm, or infinity norm. $\| \mathbf { A } \|$ : Norm of matrix A. A subscript is used to specify the 1-norm, 2-norm, or infinity norm.   
• $\mathbf { G } ^ { \dagger }$ : Generalized inverse of matrix $\mathbf { G }$ . $\mathbf { m } _ { \dagger }$ : Generalized inverse solution $\mathbf { m } _ { \dagger } = \mathbf { G } ^ { \dagger } \mathbf { d }$ . $\mathbf { G } ^ { \sharp }$ : A regularized generalized inverse of matrix $\mathbf { G }$ . $E [ X ]$ : Expected value of random variable $X$ . a¯: Mean value of elements in vector a. $N ( \mu , \sigma ^ { 2 } )$ : Normal probability distribution with expected value $\mu$ and variance $\sigma ^ { 2 }$ . $\operatorname { C o v } ( X , Y )$ : Covariance of random variables $X$ and $Y$ .   
• $\operatorname { C o v } ( \mathbf { x } )$ : Matrix of covariances of elements of vector $\mathbf { x }$ .   
• $\rho ( X , Y )$ : Correlation between random variables $X$ and $Y$ . $\mathrm { V a r } ( X )$ : Variance of random variable $X$ . $f ( \mathbf { d } | \mathbf { m } )$ : Conditional probability density for $\mathbf { d }$ , conditioned on a particular model m. $L ( \mathbf { m } | \mathbf { d } )$ : Likelihood function for a model $\mathbf { m }$ , given a particular data vector d. $\sigma$ : Standard deviation. $\sigma ^ { 2 }$ : Variance.   
. $\nabla f ( \mathbf { x } )$ : Gradient of function $f ( \mathbf { x } )$ . $\mathbf { J } ( \mathbf { x } )$ : Jacobian of vector-valued function, $\mathbf { F } ( \mathbf { x } )$ . $\mathbf { H } ( f ( \mathbf { x } ) )$ : Hessian of scalar-valued function $f ( \mathbf { x } )$ .   
[1] R. C. Aster. On projecting error ellipsoids. Bulletin of the Seismological Society of America, 78(3): 1373–1374, 1988.   
[2] G. Backus and F. Gilbert. Uniqueness in the inversion of inaccurate gross earth data. Philosophical Transactions of the Royal Society A, 266:123–192, 1970.   
[3] Z. Bai and J. W. Demmel. Computing the generalized singular value decomposition. SIAM Journal on Scientific Computing, 14:1464–1486, 1993.   
[4] L. J. Bain and M. Englehardt. Introduction to Probability and Mathematical Statistics, 2nd ed. Brooks/Cole, Pacific Grove, CA, 2000.   
[5] R. Barrett, M. Berry, T. F. Chan, J. Demmel, J. Donato, V. Eijkhout, R. Pozo, C. Romine, and H. van der Vorst. Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods, 2nd Ed. SIAM, Philadelphia, 1994.   
[6] I. Barrowdale and F. D. K. Roberts. Solution of an overdetermined system of equations in the $l _ { 1 }$ norm. Communications of the ACM, 17(6):319–326, 1974.   
[7] D. M. Bates and D. G. Watts. Nonlinear Regression Analysis and Its Applications. Wiley, New York, 1988.   
[8] J. Baumeister. Stable Solution of Inverse Problems. Vieweg, Braunschweig, 1987.   
[9] C. Bekas, E. Kokiopoulou, and Y. Saad. An estimator for the diagonal of a matrix. Applied Numerical Mathematics, 57(11–12):1214–1229, 2005.   
[10] A. Ben-Israel and T. N. E. Greville. Generalized Inverses, 2nd ed. Springer-Verlag, New York, 2003.   
[11] A. Ben-Tal and A. Nemirovski. Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications. SIAM, Philadelphia, 2001.   
[12] J. G. Berryman. Analysis of approximate inverses in tomography. I. Resolution analysis. Optimization and Engineering, 1(1):87–115, 2000.   
[13] J. G. Berryman. Analysis of approximate inverses in tomography. II. Iterative inverses. Optimization and Engineering, 1(4):437–473, 2000.   
[14] M. Bertero and P. Boccacci. Introduction to Inverse Problems in Imaging. Institute of Physics, London, 1998.   
[15] J. T. Betts. Practical Methods for Optimal Control Using Nonlinear Programming. SIAM, Philadelphia, 2001.   
[16] A. Bj ˚ orck. ¨ Numerical Methods for Least Squares Problems. SIAM, Philadelphia, 1996.   
[17] C. G. E. Boender and H. E. Romeijn. Stochastic methods. In R. Horst and P. M. Pardalos, eds., Handbook of Global Optimization, pages 829–869. Kluwer Academic Publishers, Dordrecht, 1995.   
[18] P. T. Boggs, J. R. Donaldson, R. H. Byrd, and R. B. Schnabel. ODRPACK software for weighted orthogonal distance regression. ACM Transactions on Mathematical Software, 15(4):348–364, 1989. Available at http://www.netlib.org/odrpack/.   
[19] L. Boschi. Measures of resolution in global body wave tomography. Geophysical Research Letters, 30:SDE 2-1-SDE 2-4, 2003.   
[20] R. Bracewell. The Fourier Transform and Its Applications, 3rd ed. McGraw-Hill, Boston, 2000.   
[21] A. M. Bruckstein, D. L. Donoho, and M. Elad. From sparse solutions of systems of equations to sparse modeling of signals and images. SIAM Review, 51(1):34–81, 2009.   
[22] D. Calvetti and E. Somersalo. Introduction to Bayesian Scientific Computing: Ten Lectures on Subjective Computing. Springer, New York, 2007.   
[23] S. L. Campbell and C. D. Meyer, Jr. Generalized Inverses of Linear Transformations. Dover, Mineola, NY, 1991.   
[24] E. J. Candes, J. K. Romberg, and T. Tao. Robust uncertainty principles: Exact signal reconstruc- \` tion from highly incomplete frequency information. IEEE Transactions on Information Theory, 52(2): 489–509, 2006.   
[25] E. J. Candes, J. K. Romberg, and T. Tao. Stable signal recovery from incomplete and inaccurate \` measurements. Communications on Pure and Applied Mathematics, 59(8):1207–1223, 2006.   
[26] E. J. Candes and T. Tao. Near-optimal signal recovery from random projections: Universal encoding \` strategies? IEEE Transactions on Information Theory, 52(12):5406–5425, 2006.   
[27] E. J. Candes and M. B. Wakin. An introduction to compressive sampling. \` IEEE Signal Processing Magazine, 25(2):21–30, 2008.   
[28] P. Carrion. Inverse Problems and Tomography in Acoustics and Seismology. Penn, Atlanta, GA, 1987.   
[29] G. Casella and R. L. Berger. Statistical Inference, 2nd ed. Duxbury, Pacific Grove, CA, 2002.   
[30] Y. Censor and S. A. Zenios. Parallel Optimization: Theory, Algorithms, and Applications. Oxford University Press, New York, 1997.   
[31] J. F. Claerbout and F. Muir. Robust modeling with erratic data. Geophysics, 38(5):826–844, 1973.   
[32] T. F. Coleman and Y. Li. A globally and quadratically convergent method for linear $l _ { 1 }$ problems. Mathematical Programming, 56:189–222, 1992.   
[33] S. C. Constable, R. L. Parker, and C. G. Constable. Occam’s inversion: A practical algorithm for generating smooth models from electromagnetic sounding data. Geophysics, 52(3):289–300, 1987.   
[34] G. Corliss, C. Faure, A. Griewank, L. Hascoet, and U. Naumann. Automatic Differentiation of Algorithms. Springer-Verlag, Berlin, 2002.   
[35] R. T. Cox. Algebra of Probable Inference. Johns Hopkins University Press, Baltimore, 2002.   
[36] P. Craven and G. Wahba. Smoothing noisy data with spline functions: Estimating the correct degree of smoothing by the method of generalized cross-validation. Numerische Mathematik, 31:377–403, 1979.   
[37] M. M. Deal and G. Nolet. Comment on estimation of resolution and covariance for large matrix inversions by J. Zhang and G. A. McMechan. Geophysical Journal International, 127(1):245–250, 1996.   
[38] J. W. Demmel. Applied Numerical Linear Algebra. SIAM, Philadelphia, 1997.   
[39] J. E. Dennis, Jr. and R. B. Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations. SIAM, Philadelphia, 1996.   
[40] N. R. Draper and H. Smith. Applied Regression Analysis, 3rd ed. Wiley, New York, 1998.   
[41] C. Eckart and G. Young. A principal axis transformation for non-Hermitian matrices. Bulletin of the American Mathematical Society, 45:118–121, 1939.   
[42] A. W. F. Edwards. Likelihood. Johns Hopkins University Press, Baltimore, 1992.   
[43] L. El Ghaoui and H. Lebret. Robust solutions to least-squares problems with uncertain data. SIAM Journal on Matrix Analysis and Applications, 18(4):1035–1064, 1997.   
[44] H. W. Engl. Regularization methods for the stable solution of inverse problems. Surveys on Mathematics for Industry, 3:71–143, 1993.   
[45] H. W. Engl, M. Hanke, and A. Neubauer. Regularization of Inverse Problems. Kluwer Academic Publishers, Boston, 1996.   
[46] R. M. Errico. What is an adjoint model? Bulletin of the American Meteorological Society, 78(11): 2577–2591, 1997.   
[47] M. Evans, N. Hasting, and B. Peacock. Statistical Distributions, 2nd ed. John Wiley & Sons, New York, 1993.   
[48] S. N. Evans and P. B. Stark. Inverse problems as statistics. Inverse Problems, 18:R1–R43, 2002.   
[49] J. G. Ferris and D. B. Knowles. The Slug-Injection Test for Estimating the Coefficient of Transmissibility of an Aquifer. In U.S. Geological Survey Water Supply Paper 1536-I, pages 299–304. U.S. Geological Survey, Washington, DC, 1963.   
[50] A. Frommer and P. Maass. Fast CG-based methods for Tikhonov-Phillips regularization. SIAM Journal on Scientific Computing, 20(5):1831–1850, 1999.   
[51] A. Gelman, J. B. Carlin, H. S. Stern, and D. B. Rubin. Bayesian Data Analysis, 2nd ed. Chapman & Hall/CRC Press, Boca Raton, FL, 2003.   
[52] M. Th. van Genuchten. A closed-form equation for predicting the hydraulic conductivity of unsaturated soils. Soil Science Society of America Journal, 44:892–898, 1980.   
[53] G. H. Golub and C. F. van Loan. Matrix Computations, 3rd ed. Johns Hopkins University Press, Baltimore, 1996.   
[54] G. H. Golub and U. von Matt. Generalized cross-validation for large-scale problems. Journal of Computational and Graphical Statistics, 6(1):1–34, 1997.   
[55] G. H. Golub and D. P. O’Leary. Some history of the conjugate gradient and Lanczos methods. SIAM Review, 31(1):50–102, 1989.   
[56] W. P. Gouveia and J. A. Scales. Resolution of seismic waveform inversion: Bayes versus Occam. Inverse Problems, 13(2):323–349, 1997.   
[57] A. Griewank. Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation. SIAM, Philadelphia, 2000.   
[58] I. Griva, S. G. Nash, and A. Sofer. Linear and Nonlinear Programming, 2nd ed. SIAM, Philadelphia, 2008.   
[59] C. W. Groetsch. Inverse Problems in the Mathematical Sciences. Vieweg, Braunschweig, 1993.   
[60] D. Gubbins. Time Series Analysis and Inverse Theory for Geophysicists. Cambridge University Press, Cambridge, 2004.   
[61] M. Hanke. Conjugate Gradient Type Methods for Ill-Posed Problems. CRC Press, New York, 1995.   
[62] P. C. Hansen. Relations between SVD and GSVD of discrete regularization problems in standard and general form. Linear Algebra and Its Applications, 141:165–176, 1990.   
[63] P. C. Hansen. Analysis of discrete ill-posed problems by means of the L-curve. SIAM Review, 34(4):561–580, 1992.   
[64] P. C. Hansen. Regularization tools: A MATLAB package for analysis and solution of discrete ill-posed problems. Numerical Algorithms, 6(I–II):1–35, 1994. http://www.imm.dtu.dk/documents/ users/pch/Regutools/regutools.html.   
[65] P. C. Hansen. Rank-Deficient and Discrete Ill-Posed Problems: Numerical Aspects of Linear Inversion. SIAM, Philadelphia, 1998.   
[66] P. C. Hansen. Deconvolution and regularization with Toeplitz matrices. Numerical Algorithms, 29:323–378, 2002.   
[67] P. C. Hansen. Discrete Inverse Problems: Insight and Algorithms. Society for Industrial and Applied Mathematics, Philadelphia, 2010.   
[68] J. M. H. Hendrickx. Bosque del Apache soil data. Personal communication, 2003.   
[69] J. M. H. Hendrickx, B. Borchers, J. D. Rhoades, D. L. Corwin, S. M. Lesch, A. C. Hilgendorf, and J. Schlue. Inversion of soil conductivity profiles from electromagnetic induction measurements: Theory and experimental verification. Soil Science Society of America Journal, 66(3):673–685, 2002.   
[70] G. T. Herman. Image Reconstruction from Projections. Academic Press, San Francisco, 1980.   
[71] M. R. Hestenes. Conjugacy and gradients. In Stephen G. Nash, ed., A History of Scientific Computing, pages 167–179. ACM Press, New York, 1990.   
[72] M. R. Hestenes and E. Stiefel. Methods of conjugate gradients for solving linear systems. Journal of Research, National Bureau of Standards, 49:409–436, 1952.   
[73] J. A. Hildebrand, J. M. Stevenson, P. T. C. Hammer, M. A. Zumberge, R. L. Parker, C. J. Fox, and P. J. Meis. A sea–floor and sea–surface gravity survey of axial volcano. Journal of Geophysical Research, 95(B8):12751–12763, 1990.   
[74] R. A. Horn and C. R. Johnson. Matrix Analysis. Cambridge University Press, Cambridge, 1985.   
[75] R. Horst and P. M. Pardalos. Handbook of Global Optimization. Kluwer Academic Publishers, Dordrecht, 1995.   
[76] R. Horst, P. M. Pardalos, and N. V. Thoai. Introduction to Global Optimization. Kluwer Academic Publishers, Dordrecht, 1995.   
[77] P. J. Huber. Robust Statistical Procedures, 2nd ed. SIAM, Philadelphia, 1996.   
[78] S. von Huffel and J. Vandewalle. The Total Least Squares Problem: Computational Aspects and Analysis. SIAM, Philadelphia, 1991.   
[79] H. Iyer and K. Hirahara (eds.). Seismic Tomography. Chapman & Hall, New York and London, 1993.   
[80] E. T. Jaynes. Probability Theory: The Logic of Science. Cambridge University Press, Cambridge, 2003.   
[81] H. Jeffreys. Theory of Probability. Oxford University Press, New York, 1998.   
[82] W. H. Jeffreys, M. J. Fitzpatrick, and B. E. McArthur. Gaussfit—a system for least squares and robust estimation. Celestial Mechanics, 41(1–4):39–49, 1987. Available at http://clyde.as.utexas.edu/ Gaussfit.html.   
[83] J. Kaipio and E. Somersalo. Statistical and Computational Inverse Problems. Springer, New York, 2004.   
[84] A. C. Kak and M. Slaney. Principles of Computerized Tomographic Imaging. SIAM, Philadelphia, 2001. Transactions on Medical Imaging, 15(3):385–389, 1996. [86] L. Kaufman and A. Neumaier. Regularization of ill-posed problems by envelope guided conjugate gradients. Journal of Computational and Graphical Statistics, 6(4):451–463, 1997. [87] C. T. Kelley. Iterative Methods for Solving Linear and Nonlinear Equations. SIAM, Philadelphia, 1995.   
[88] C. T. Kelley. Solving Nonlinear Equations with Newton’s Method. SIAM, Philadelphia, 2003.   
[89] W. J. Kennedy, Jr. and J. E. Gentle. Statistical Computing. Marcel Dekker, New York, 1980. [90] A. Kirsch. An Introduction to the Mathematical Theory of Inverse Problems. Springer-Verlag, New York, 1996.   
[91] F. J. Klopping, G. Peter, D. S. Robertson, K. A. Berstis, R. E. Moose, and W. E. Carter. Improvements in absolute gravity observations. Journal of Geophysical Research, 96(B5):8295–8303, 1991.   
[92] C. Lanczos. Solutions of systems of linear equations by minimized iterations. Journal of Research, National Bureau of Standards, 49:33–53, 1952. [93] C. Lanczos. Linear Differential Operators. Dover, Mineola, NY, 1997.   
[94] C. L. Lawson and R. J. Hanson. Solving Least Squares Problems. SIAM, Philadelphia, 1995.   
[95] D. C. Lay. Linear Algebra and Its Applications, 3rd ed. Addison-Wesley, Boston, 2003.   
[96] T. Lay and T. Wallace. Modern Global Seismology. Academic Press, San Diego, 1995. [97] J.-J. Leveque, L. Rivera, and G. Wittlinger. On the use of the checker-board test to assess the resolution of tomographic inversions. Geophysical Journal International, 115(1):313–318, 1993.   
[98] Z.-P. Liang and P. C. Lauterbur. Principles of Magnetic Resonance Imaging: A Signal Processing Perspective. IEEE Press, New York, 2000.   
[99] L. R. Lines, ed. Inversion of Geophysical Data. Society of Exploration Geophysicists, Tulsa, OK, 1988.   
[100] T.-W. Lo and P. Inderwiesen. Fundamentals of Seismic Tomography. Society of Exploration Geophysicists, Tulsa, OK, 1994.   
[101] C. F. van Loan. Generalizing the singular value decomposition. SIAM Journal on Numerical Analysis, 13:76–83, 1976.   
[102] D. G. Luenberger. Optimization by Vector Space Methods. John Wiley and Sons, New York, 1969.   
[103] J. MacCarthy, B. Borchers, and R. Aster. Estimating the model resolution matrix diagonal and generalized cross-validation for large geophysical inverse problems. Journal of Geophysical Research, 2011. In press.   
[104] D. Mackenzie. Compressed sensing makes every pixel count. In What’s Happening in the Mathematical Sciences. American Mathematical Society, Providence, RI, 2009.   
[105] W. H. Marlow. Mathematics for Operations Research. Dover, Mineola, NY, 1993.   
[106] P. J. McCarthy. Direct analytic model of the L-curve for Tikhonov regularization parameter selection. Inverse Problems, 19:643–663, 2003.   
[107] P. R. McGillivray and D. Oldenburg. Methods for calculating Frechet derivatives and sensitivities for the non-linear inverse problem: A comparative study. Geophysical Prospecting, 38:499–524, 1990.   
[108] W. Menke. Geophysical Data Analysis: Discrete Inverse Theory, volume 45 of International Geophysics Series, rev. ed. Academic Press, San Diego, 1989.   
[109] C. D. Meyer. Matrix Analysis and Applied Linear Algebra. SIAM, Philadelphia, 2000.   
[110] E. H. Moore. On the reciprocal of the general algebraic matrix. Bulletin of the American Mathematical Society, 26:394–395, 1920.   
[111] J. J. More, B. S. Garbow, and K. E. Hillstrom. User guide for MINPACK-1. Technical Report ANL-80-74, Argonne National Laboratory, 1980.   
[112] V. A. Morozov. Methods for Solving Incorrectly Posed Problems. Springer-Verlag, New York, 1984.   
[113] R. H. Myers. Classical and Modern Regression with Applications, 2nd ed. PWS Kent, Boston, 1990.   
[114] F. Natterer. The Mathematics of Computerized Tomography. SIAM, Philadelphia, 2001.   
[115] F. Natterer and F. Wubbeling. ¨ Mathematical Methods in Image Reconstruction. SIAM, Philadelphia, 2001.   
[116] A. Neumaier. Solving ill-conditioned and singular linear systems: A tutorial on regularization. SIAM Review, 40(3):636–666, 1998.   
[117] R. Neupauer, B. Borchers, and J. L. Wilson. Comparison of inverse methods for reconstructing the release history of a groundwater contamination source. Water Resources Research, 36(9):2469–2475, 2000.   
[118] I. Newton. The Principia, Mathematical Principles of Natural Philosophy, trans. by I. B. Cohen and A. Whitman. University of California Press, Berkeley, 1999.   
[120] G. Nolet. Solving or resolving inadequate and noisy tomographic systems. Journal of Computational Physics, 61(3):463–482, 1985.   
[121] G. Nolet, ed. Seismic Tomography with Applications in Global Seismology and Exploration Geophysics. D. Reidel, Boston, 1987.   
[122] S. J. Osher and R. P. Fedkiw. Level Set Methods and Dynamic Implicit Surfaces. Springer-Verlag, New York, 2002.   
[123] C. C. Paige and M. A. Saunders. Algorithm 583 LSQR: Sparse linear equations and least-squares problems. ACM Transactions on Mathematical Software, 8(2):195–209, 1982.   
[124] C. C. Paige and M. A. Saunders. LSQR: An algorithm for sparse linear equations and sparse least squares. ACM Transactions on Mathematical Software, 8(1):43–71, 1982.   
[125] R. L. Parker. A theory of ideal bodies for seamount magnetism. Journal of Geophysical Research, 96(B10):16101–16112, 1991.   
[126] R. L. Parker. Geophysical Inverse Theory. Princeton University Press, Princeton, NJ, 1994.   
[127] R. L. Parker and M. K. McNutt. Statistics for the one-norm misfit measure. Journal of Geophysical Research, 85:4429–4430, 1980.   
[128] R. L. Parker and M. A. Zumberge. An analysis of geophysical experiments to test Newton’s law of gravity. Nature, 342:29–32, 1989.   
[129] R. Penrose. A generalized inverse for matrices. Mathematical Proceedings of the Cambridge Philosophical Society, 51:406–413, 1955.   
[130] S. Portnoy and R. Koenker. The Gaussian hare and the Laplacian tortoise: Computability of squarederror versus absolute-error estimators. Statistical Science, 12:279–296, 1997.   
[131] M. B. Priestley. Spectral Analysis and Time Series. Academic Press, London, 1983.   
[132] W. Rison, R. J. Thomas, P. R. Krehbiel, T. Hamlin, and J. Harlin. A GPS-based three-dimensional lightning mapping system: Initial observations in central New Mexico. Geophysical Research Letters, 26(23):3573–3576, 1999.   
[133] C. D. Rodgers. Inverse Methods for Atmospheric Sounding: Theory and Practice. Word Scientific Publishing, Singapore, 2000.   
[134] W. Rudin. Real and Complex Analysis, 3rd ed. McGraw-Hill, New York, 1987.   
[135] Y. Saad. Iterative Methods for Sparse Linear Systems, 2nd ed. SIAM, Philadelphia, 2003.   
[136] L. J. Savage. The Foundation of Statistics, 2nd ed. Dover, Mineola, NY, 1972.   
[137] J. Scales and M. Smith. DRAFT: Geophysical inverse theory. http://landau.Mines.EDU/samizdat/ inverse theory/, 1997.   
[138] J. A. Scales, A. Gersztenkorn, and S. Treitel. Fast lp solution of large, sparse, linear systems: Application to seismic travel time tomography. Journal of Computational Physics, 75(2):314–333, 1988.   
[139] S. R. Searle. Matrix Algebra Useful for Statistics. Wiley-Interscience, New York, 2006.   
[140] M. K. Sen and P. L. Stoffa. Global Optimization Methods in Geophysical Inversion. Number 4 in Advances in Exploration Geophysics. Elsevier, New York, 1995.   
[141] C. B. Shaw, Jr. Improvement of the resolution of an instrument by numerical solution of an integral equation. Journal of Mathematical Analysis and Applications, 37:83–112, 1972.   
[142] J. R. Shewchuk. An introduction to the Conjugate Gradient Method without the agonizing pain. Technical report, School of Computer Science, Carnegie Mellon University, 1994. http://www.cs. cmu.edu/jrs/jrspapers.html.   
[143] D. S. Sivia and J. Skilling. Data Analysis: A Bayesian Tutorial, 2nd ed. Oxford University Press, New York, 2006.   
[144] T. H. Skaggs and Z. J. Kabala. Recovering the release history of a groundwater contaminant. Water Resources Research, 30(1):71–79, 1994.   
[145] T. H. Skaggs and Z. J. Kabala. Recovering the history of a groundwater contaminant plume: Method of quasi-reversibility. Water Resources Research, 31:2669–2673, 1995.   
[146] A. Van der Sluis and H. A. Van der Vorst. Numerical solution of large, sparse linear algebraic systems arising from tomographic problems. In G. Nolet, ed., Seismic Tomography, pages 49–83. D. Reidel, Hingham, MA, 1987.   
[147] W. Spakman and G. Nolet. Imaging algorithms, accuracy and resolution in delay time tomography. In M. J. R. Wortel, N. J. Vlaar, G. Nolet, and S. A. P. L. Cloetingh, eds., Mathematical Geophysics: A Survey of Recent Developments in Seismology and Geodynamics, pages 155–187. D. Reidel, Dordrecht, 1988.   
[148] P. B. Stark and R. L. Parker. Velocity bounds from statistical estimates of $\tau ( p )$ and $x ( p )$ . Journal of Geophysical Research, 92(B3):2713–2719, 1987.   
[149] P. B. Stark and R. L. Parker. Correction to “velocity bounds from statistical estimates of $\tau ( p )$ and $x ( p )$ .” Journal of Geophysical Research, 93:13821–13822, 1988.   
[150] P. B. Stark and R. L. Parker. Bounded-variable least-squares: An algorithm and applications. Computational Statistics, 10(2):129–141, 1995.   
[151] G. W. Stewart. On the early history of the singular value decomposition. SIAM Review, 35:551–566, 1993.   
[152] G. Strang. Linear Algebra and Its Applications, 3rd ed. Harcourt Brace Jovanovich, San Diego, 1988.   
[153] G. Strang and K. Borre. Linear Algebra, Geodesy, and GPS. Wellesley–Cambridge Press, Wellesley, MA, 1997.   
[154] N. Z. Sun. Inverse Problems in Groundwater Modeling. Kluwer Academic Publishers, Boston, 1984.   
[155] A. Tarantola. Inverse Problem Theory and Methods for Model Parameter Estimation. SIAM, Philadelphia, 2004.   
[156] A. Tarantola and B. Valette. Inverse problems $=$ quest for information. Journal of Geophysics, 50(3):159–170, 1982.   
[157] R. A. Thisted. Elements of Statistical Computing. Chapman and Hall, New York, 1988.   
[158] C. Thurber. Hypocenter velocity structure coupling in local earthquake tomography. Physics of the Earth and Planetary Interiors, 75(1–3):55–62, 1992.   
[159] C. Thurber and K. Aki. Three-dimensional seismic imaging. Annual Review of Earth and Planetary Sciences, 15:115–139, 1987.   
[160] C. Thurber and J. Ritsema. Theory and observations—seismic tomography and inverse methods. In Treatise on Geophysics, pages 323–360. Elsevier, Amsterdam, 2007.   
[161] A. N. Tikhonov and V. Y. Arsenin. Solutions of Ill-Posed Problems. Halsted Press, New York, 1977.   
[162] A. N. Tikhonov and A. V. Goncharsky, eds. Ill-Posed Problems in the Natural Sciences. MIR Publishers, Moscow, 1987.   
[163] J. Trampert and J.-J. Lev´ eque. Simultaneous iterative reconstruction technique: Physical interpreta- ´ tion based on the generalized least squares solution. Journal of Geophysical Research, 95(B8):12553– 12559, 1990.   
[164] L. N. Trefethen and D. Bau. Numerical Linear Algebra. SIAM, Philadelphia, 1997.   
[165] J. Tromp, C. Tape, and Q. Liu. Seismic tomography, adjoint methods, time reversal, and bananadoughnut kernels. Geophysical Journal International, 160:195–216, 2005.   
[166] S. Twomey. Introduction to the Mathematics of Inversion in Remote Sensing and Indirect Measurements. Dover, Mineola, NY, 1996.   
[167] J. Um and C. Thurber. A fast algorithm for 2-point seismic ray tracing. Bulletin of the Seismological Society of America, 77(3):972–986, 1987.   
[168] C. R. Vogel. Non-convergence of the L-curve regularization parameter selection method. Inverse Problems, 12:535–547, 1996.   
[169] C. R. Vogel. Computational Methods for Inverse Problems. SIAM, Philadelphia, 2002.   
[170] G. Wahba. Spline Models for Observational Data. SIAM, Philadelphia, 1990.   
[171] G. A. Watson. Approximation in normed linear spaces. Journal of Computational and Applied Mathematics, 121(1–2):1–36, 2000.   
[172] G. M. Wing. A Primer on Integral Equations of the First Kind: The Problem of Deconvolution and Unfolding. SIAM, Philadelphia, 1991.   
[173] H. Zhang and C. H. Thurber. Estimating the model resolution matrix for large seismic tomography problems based on Lanczos bidiagonalization with partial reorthogonalization. Geophysical Journal International, 170(1):337–345, 2007.   
[174] J. Zhang and G. A. McMechan. Estimation of resolution and covariance for large matrix inversions. Geophysical Journal International, 121(2):409–426, 1995.

Note: Bold entries signify the introduction and/or definition of a topic.

$\infty$ -norm, 305, 305–307, 313   
0-norm, 174   
1-norm, 6, 43–48, 50, 53, 305, 306, 307, 313   
2-norm, 6, 26, 59, 109, 114, 243, 298, 301, 305,   
306, 311, 345

# A

acceptance ratio, 271   
adjoint equation, 252   
advection–diffusion equation, 12–17, 170   
algebraic reconstruction technique, 146, 146–149,   
166   
aliasing, 201, 202   
ART, see algebraic reconstruction technique   
augmented matrix, 284, 285, 293   
automatic differentiation, 228   
averaging kernel, 64, 135, 135–139

# B

B-splines, 140   
Backus–Gilbert method, 64, 134–139   
basis, 58, 62, 65, 67, 70, 71, 80, 81, 113, 121, 140, 150–151, 154, 198, 199, 281, 296, 303, 314 Fourier, 196, 200, 213 orthogonal, 139, 299, 300, 301 orthonormal, 55–56, 60, 139, 297, 299, 309 standard, 22, 296   
Bayes’ theorem, 256, 327   
Bayesian statistics, 255–280, 316   
biased estimator, 19, 32, 62, 63, 99, 102, 281   
bounded variables least squares problem, 170, 170–174   
BVLS, see bounded variables least squares problem

# C

CDF, see cumulative distribution function   
central limit theorem, 30, 330   
CG, see conjugate gradient method   
CGLS, see conjugate gradient least squares method   
characteristic equation, 302   
checkerboard resolution test, 87, 91, 249   
chi–square test, 29, 34, 226, 246   
Cholesky factorization, 141, 154, 262, 278, 304, 314, 330   
circular convolution, 202   
collocation, 15, 16, 90, 103, 124, 137, 202   
column space, see range   
compact form of the singular value decomposition, 56   
complex conjugate, 310   
complex number, 310 absolute value, 310   
compressive sensing, 183   
condition number, 65, 67, 76, 81, 91, 119, 120, 139, 140, 246, 306, 307   
conditional distribution, 27, 256, 328   
conditional expected value, 328   
conditional probability, 327   
confidence ellipsoids, see confidence regions   
confidence intervals, 32, 39–41, 48–50, 102, 226, 230, 232, 234, 253, 254, 262, 281, 333, 333–334, 336, 337   
confidence regions, 34, 34–37, 39, 49, 228   
conjugate distribution, 259   
conjugate gradient least squares method, 155, 155–159, 167, 168, 254   
conjugate gradient method, 150, 150–155, 252   
continuous inverse problem, 2, 3, 91, 134, 140, 281   
contour plot, 227–228   
convex function, 45, 150, 230, 340   
convolution, 4, 8, 9, 12, 17, 76, 156, 193–203, 215   
convolution theorem, 197, 203, 213   
correlation, 35, 49, 234, 323   
covariance, 36, 262, 279, 323, 336   
covariance matrix, 31–36, 40, 48–51, 62, 101, 102, 224–226, 233, 236, 260–269, 329, 336   
critical point, 339, 340   
cross-well tomography, 13, 125, 126, 240–244, 251   
cumulative distribution function, 321, 322, 324, 326, 328, 331, 336

# D

damped least squares problem, 94, 95, 103, 124, 240, 244, 245   
damped SVD method, 97   
data kernels, see representers   
data null space, 56, 58, 61, 71, 90   
deconvolution, 4, 76–81, 84, 177, 193, 202–207, 213, 215   
delta function, 75, 135, 193, 198, 279   
denoising, 187   
dense matrix, 141, 141–142, 157   
determinant, 302   
DFT, see discrete Fourier transform   
diagonalization of a matrix, 35, 303   
discrepancy principle, 67, 77, 95, 98, 99, 102, 124, 125, 127, 156, 241, 243, 244   
discrete Fourier transform, 199, 199–216   
discrete ill-posed problem, 20, 74, 74–87, 93, 121, 156 mildly ill-posed, 74 moderately ill-posed, 74, 108 severely ill-posed, 74, 81   
discrete inverse problem, 2, 3, 19, 25, 28, 74, 91, 215, 239, 296   
distribution chi-square, 29, 34, 67, 253, 319, 329 double-sided exponential, 43, 319 exponential, 319, 328, 336, 337 Gaussian, see distribution, normal multivariate normal, 26, 28, 30–32, 34, 38, 39, 43, 47–49, 62, 145, 220, 224, 225, 232, 244, 252, 253, 257, 260–269, 281, 329, 329–330, 332–334, 336, 337 normal, 30, 32, 39, 43, 259, 317, 330–337 Student’s t, 39, 52, 319, 333 uniform, 30, 52, 232, 278, 317   
dot product, 65, 67, 298, 299, 305, 311, 342, 345   
double-sided exponential distribution, see distribution, double-sided exponential

# E

earthquake location problem, 7, 13, 235–236   
eigenvalue, 35, 56, 57, 60, 302, 302–304, 306, 313, 345   
eigenvector, 35, 56, 57, 60, 302, 302–304, 345   
elementary row operations, 284   
expected value, 31, 63, 117, 321, 322–324, 328–330, 336

exponential distribution, see distribution, exponential

# F

fast Fourier transform, 200, 202–204, 213   
Fermat’s least-time principle, 241   
FFT, see fast Fourier transform   
filter factors, 96, 100, 104, 107, 108, 113, 166, 168   
finite-difference derivatives, 104, 228, 229, 246, 252   
forward problem, 2, 4, 6, 16, 22, 27, 202, 203   
Fourier basis functions, see basis, Fourier   
Fourier transform, 4, 195, 195–216   
Frechet derivatives,´ 252   
Fredholm integral equation of the first kind, 3, 14, 74, 140   
frequency response, 196   
Frobenius norm, 306, 308   
full rank least squares problem, see matrix, full rank

# G

gamma function, 29, 34, 319   
Gauss-Newton method, 222, 222–223, 228–232, 235, 238, 240, 241, 245, 251, 252, 254   
Gaussian distribution, see distribution, normal   
Gaussian elimination, 283, 283–285   
Gaussian point spread function, 156, 167   
GCV, see generalized cross-validation   
generalized cross-validation, 115, 119, 124, 127, 162   
generalized singular value decomposition, 104, 114, 127   
Geonics EM-38 ground conductivity meter, 246–248   
global optimization, 231, 231–234, 238, 254   
GN method, see Gauss–Newton method   
Gosset, W. S., 319   
gradient, 46, 219, 221, 229, 339, 340, 342–344   
Gram matrix, 132, 139, 140, 312   
Gram-Schmidt orthogonalization process, 301, 314   
Green’s function, 194, 215   
GSVD, see generalized singular value decomposition

#

Heaviside step function, 8   
Hermitian symmetry, 200, 214   
Hermitian transpose, 310

Hessian, 219, 221, 222, 224, 237, 340, 344 higher-order Tikhonov regularization, 103, 104, 113–115, 117, 124, 125, 215, 254 histogram, 50–52, 330–332, 337

# I

identity matrix, see matrix, identity   
IDFT, see inverse Fourier transform, discrete   
IFFT, see inverse Fourier transform, fast   
IFK, 14, see Fredholm integral equation of the first kind   
ill-posed problem, see discrete ill-posed problem   
image deblurring, 156–159, 167, 168   
impulse resolution test, see spike resolution test   
impulse response, 75, 76, 194, 195, 197, 198, 202–205, 215   
indefinite matrix, see matrix, indefinite   
independent random variables, 27, 28, 30–32, 38, 39, 44, 47, 62, 88, 136, 225, 244, 252, 253, 257, 262, 320, 323, 323–326, 329, 330, 332, 333, 336   
inner product, 311   
inverse Fourier transform, 4, 195, 198, 204, 216 discrete, 200, 201, 214 fast, 200   
inverse of a matrix, 34, 58, 290, 291, 292   
IRLS, see iteratively reweighted least squares   
iterative methods, 46–47, 53, 141–168, 241, 244, 252, 254   
iteratively reweighted least squares, 46–48, 50, 53, 167

# J

Jacobian, 218, 221, 226, 240, 244, 246, 251, 269, 340   
JDF, see joint probability density function   
joint probability density function, 27, 323, 324, 326, 329

K Kaczmarz’s algorithm, 142, 142–149, 166

L   
L-curve, 95, 97, 98, 108, 119, 124–127, 156–158, 170, 241   
Lagrange multipliers, 94, 124, 132, 136, 137, 191, 341, 341–345   
Landweber iteration, 166   
Laplacian operator, 104, 126, 241, 244, 252   
law of total probability, 327, 328   
least squares problem, 26–32, 38, 40–46, 48, 49, 51, 52, 55, 58–60, 62, 68, 77, 93, 155, 157, 170, 253, 261, 278, 281, 301, 302, 305, 308, 309, 312, 345   
least squares solution, see least squares problem   
leave-one-out cross-validation, 115   
Legendre polynomials, 139   
Levenberg-Marquardt method, 222, 222–223, 228–236, 238, 240, 246, 254   
likelihood function, see maximum likelihood estimation   
line search, 219, 220   
linear combination, 19, 22, 31, 56, 59, 65, 121, 140, 200, 287, 295–298   
linear independence, 56, 95, 139, 140, 167, 292, 293, 296, 297, 302, 303, 311–313   
linear regression, 4, 25–48, 52, 127, 139, 220, 225–227   
linear systems, 3   
LM method, see Levenberg–Marquardt method   
local minimum points, 219, 230, 232, 235, 237, 240, 251, 254, 269, 282, 343

#

MAP model, see maximum a posteriori model   
Markov Chain Monte Carlo method, 270   
mathematical model, 2, 11, 12, 30, 43, 44, 49, 90, 156, 198, 214, 226, 246, 252, 253   
MATLAB commands bvls, 170 chi2pdf, 50 chol, 304 cond, 67, 308 conv, 202 dct2, 182 eig, 303 fft, 200 fftn, 216 ifft, 200 ifftn, 216 lsqnonneg, 169 lsqr, 159, 168 norm, 305 normest, 167 null, 296 orth, 297, 301 pinv, 57   
MATLAB commands (continued) qr, 308 randn, 324 rank, 81, 298 reshape, 70 rref, 285 sqrtm, 261 svd, 55 xcorr, 266   
matrix diagonal, 28, 31, 35, 46, 55, 56, 60, 100, 203, 291 full column rank, 25, 26, 58, 63, 298, 308, 309, 313 full rank, 58, 67, 95, 298, 329 full row rank, 298 identity, 31, 58, 63, 64, 67, 79, 95, 99, 104, 105, 111, 117, 187, 223, 224, 235, 240, 244, 261, 262, 289, 290, 292, 300, 302 indefinite, 304 lower-triangular, 16, 291 orthogonal, 55, 56, 58, 60, 104, 141, 300, 303, 308–309 positive definite, 34, 150, 154, 155, 167, 220, 261, 278, 304, 312, 313, 340 positive semidefinite, 304, 312, 313 rank-deficient, 18, 19, 55, 68, 71, 298 square root, 261, 278 symmetric, 34, 63, 150, 152, 154, 167, 278, 291, 303, 304, 312, 313, 340 upper-triangular, 291, 304, 308   
matrix-matrix product, 288   
matrix norm, 63, 305, 305–308, 313, 345   
matrix-vector product, 287   
maximum a posteriori model, 257, 260–269, 279   
maximum likelihood estimation, 27, 27–29, 43, 50, 51, 220, 253, 254, 257, 269, 280   
maximum likelihood principle, see maximum likelihood estimation   
MCMC, see Markov chain Monte Carlo method   
mean value theorem, 341   
measurement matrix, 183   
median, 45, 67, 322   
Metropolis-Hastings Sampler, 270   
midpoint rule, 15, 18, 76   
minimum length least squares solution, 59, 59–61   
minimum length solution, 94, 144   
mode, 322   
model identification problem, 2   
model null space, 56, 58–60, 63, 70, 90, 199   
model resolution, 19, 62, 62–64, 73–74, 207, 244, 251   
Monte Carlo error propagation, 48   
Moore-Penrose pseudoinverse, 57, 63, 66, 67, 87, 141   
MRE method, see minimum relative entropy method   
MTSVD, see modified truncated SVD   
multicollinearity, 127   
multistart method, 232, 232–234, 240   
MVN, see distribution, multivariate normal

#

Newton’s method, 218, 218–220, 237 damped, 219   
NNLS, see nonnegative least squares method   
non-negative least squares method, 169   
nonlinear least squares problem, 220, 223, 232, 236, 239–241, 246, 254, 257, 269, 281   
nonlinear regression, 220, 220–238   
nonnegative least squares method, 170, 172   
norm, see vector norm, matrix norm   
normal distribution, see distribution, normal   
normal equations, 26, 29, 33, 45, 52, 58, 59, 95, 150, 155, 168, 224, 302, 309, 345   
null space of a matrix, 19, 56, 58–61, 63, 64, 69, 104, 106, 199, 294, 294–297, 299, 309, 312, 313   
Nyquist frequency, 201

# O

objective function, 103, 223, 232, 240, 252, 341   
Occam’s inversion, 244, 244–252   
Occam’s razor, 244, 254   
ordinary cross-validation, see leave one out cross-validation   
orthogonal basis, see basis, orthogonal   
orthogonal functions, 21, 311–312   
orthogonal matrix, see matrix, orthogonal   
orthogonal polynomials, 139   
orthogonal projection, see projection   
orthogonal subspaces, 299   
orthogonal vectors, 61, 104, 151, 152, 299   
orthonormal basis, see basis, orthonormal, 132   
outliers, 6, 42, 42–45, 50   
over-fitting of data, 67

# P

$p$ -value chi–square test, 29, 29–30, 226–228, 233 t-test, 335, 336, 337   
Parseval’s theorem, 197   
PCR, see principle components regression   
PDF, see probability density function   
perpendicular, see orthogonal   
Picard condition, 67, 99   
pivot column, 285, 297, 298, 312   
point spread function, 156, 167   
poles of a transfer function, 199   
posterior distribution, 255, 255–280   
power of a hypothesis test, 335   
power of a matrix, 290   
preconditioning, 168   
principal axes, error ellipsoid, 35   
principle of indifference, 255   
prior distribution, 255, 255–280   
probability density function, 27, 29, 316, 316–320, 336   
projection, 35, 59, 62, 64, 65, 70, 142, 143, 300, 300–301, 305, 311, 312   
proportional effect, 41   
proposal distribution, 271   
pseudoinverse, see Moore–Penrose pseudoinverse

# Q

regularization parameter, 94, 98, 102, 109, 115, 117, 119, 120, 122, 124, 125, 127, 156, 243   
representers, 14, 133–134   
residual vector, 26   
residuals, 6, 26, 29, 31, 38–43, 45–47, 49, 51, 67, 98, 147, 151, 152, 154, 155, 204, 220, 225, 226, 233   
resolution, 248   
resolution kernel, see resolution matrix, model, 64   
resolution matrix data, 64, 67 model, 63, 63–64, 67, 71, 79–81, 90, 99, 101, 111, 112   
resolution test, 64, 73, 81, 91, 249   
ridge regression, 127   
Riemann-Lebesgue lemma, 21   
robust estimation, 6   
robust estimation procedures, 43, 45, 52   
robust least squares, 53   
roughening matrix, 103, 126, 216, 239, 241, 252   
row action methods, 168   
row space of a matrix, 298   
row-column expansion method, 288   
RREF, see reduced row echelon form

Q-Q plot, 51, 52, 330   
QR factorization, 141, 154, 308, 308–309   
quadratic form, 303, 303–304, 340

# S

# R

random variables, 29–31, 39, 255, 316   
range of a matrix, 25, 56, 59, 60, 121–123, 296, 298, 299, 301, 309, 312   
rank, 90   
rank deficient least squares problem, see matrix, rank deficient   
rank of a matrix, 18, 56, 60, 63, 69, 104, 298, 308, 312   
ray-paths, 7, 13, 18, 68–74, 88–91, 142, 146–149, 240–244   
reduced row echelon form, 285, 293, 295–298, 312   
regularization by discretization, 87   
regularization by truncated singular value decomposition, 68   
saddle point, 339   
sample mean, 331, 333, 334, 335, 337   
sampling rate, 199, 200–202, 204, 205, 234   
seismogram, see seismometer   
seismometer, 8, 75–81, 204–207, 214, 215   
seminorm, 103, 109, 241, 242, 305   
serial convolution, 201, 202   
Shaw problem, 11, 11–17, 81–87, 97, 99–102, 123, 166, 262–266   
sifting property of the delta function, 193, 198   
signum function, 45   
simultaneous iterative reconstruction technique, 148, 148–149, 166   
singular value decomposition, 55, 55–61, 68, 69, 89, 91, 93, 95, 99, 100, 102, 121, 141, 154, 157, 166, 167, 213, 254, 278   
singular value spectrum, 64, 67, 74   
SIRT, see simultaneous iterative reconstruction technique   
slowness, 8, 13, 16, 18, 19, 49, 69, 74, 89, 90, 108, 112, 145, 241   
slug test, 226, 226–228   
solution existence, 19, 23   
solution stability, 20, 21, 23, 64–68, 93, 136, 138, 203, 213   
solution uniqueness, 19, 20, 23, 58, 60, 296   
sparse, 157   
sparse matrix, 141, 142, 156, 254   
sparsity regularization, 174   
spectral amplitude, 196, 197, 198, 200, 201, 204, 205, 214   
spectral division, 203, 204, 205   
spectral phase, 196, 198, 200, 201, 214   
spectrum, 195, 196, 213   
spherical harmonic functions, 140   
spike resolution test, 73, 74, 91, 249   
standard basis, 229   
standard deviation, 28, 30, 31, 38, 41, 43, 44, 49, 51, 52, 88, 125, 136, 138, 145, 220, 225, 226, 232–234, 239, 244, 246, 257–259, 261, 262, 322, 324, 331–334, 337   
standard normal distribution, 317, 319, 324, 326, 330   
stationary point, 342, 345   
steepest-descent method, 223   
Student, see Gosset, W. S.   
Student’s $t$ distribution, see distribution, Student’s t   
subspace of $R ^ { m }$ , 297   
subspace of $R ^ { n }$ , 293, 293–294, 298   
SVD, see singular value decomposition   
system of equations, 283 ill-conditioned, 20, 55, 140, 308 over-determined, 286, 305 under-determined, 286 vector form, 287   
Toeplitz matrix, 91   
tomography, 12, 23, 68–74, 125, 142–149, 166, 168, 216, 240–244, 251   
total least squares problem, 53   
total variation regularization, 186, 186–191   
transfer function, see impulse response, 199   
Transition kernel, 270   
transpose of a matrix, 290, 292, 297   
truncated generalized singular value decomposition, 113, 114   
truncated singular value decomposition, 62, 67, 75, 77, 82, 84, 91, 99, 125, 145, 149, 204   
TSVD, see truncated singular value decomposition   
type I error, 335   
type II error, 335, 337

#

unbiased estimator, 32, 62, 93, 281 uncorrelated random variables, 323 uniform distribution, see distribution, uniform uninformative prior distribution, 255

#

van Genuchten, M. Th., 235   
variance, 31, 32, 62, 136, 256, 261, 322, 330, 336   
vector norm, 26, 43, 45, 59, 94, 98, 99, 103, 110, 114, 120, 122–124, 146, 204, 243, 305, 305–306, 309   
vertical seismic profiling, 8, 8–9, 107, 110, 113, 114, 117, 119   
VSP, see vertical seismic profiling

# T

t-test, 334, 335–337   
Taylor’s theorem, 217, 219, 229, 244, 341   
TGSVD, see truncated generalized singular value decomposition   
Tikhonov regularization, 94, 124–127, 141, 156, 157, 170, 223, 239, 244, 254, 255, 262, 266, 281 frequency-domain, 208

# W

water level regularization, 204, 204–213   
wavelets, 140   
wrap-around, 202, 203

Z zeros of a transfer function, 199
