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

![](images/b9c5d8bd2ab33dd6e3b23f56612cc8565cd1964121c50103e342d6e7e7707fe9.jpg)  
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

![](images/8c0b71d08f42b9d5adb8d4a459081f677272e3bcc3763004ec4a6b73bd72459c.jpg)  
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

![](images/5cde3ea303362e43cb8a10c66579d44965b3354b6f5388b6704e6d6752e95194.jpg)  
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

![](images/56ad26e6fef6f3f2b7ca31060f2268bcd6ec2f5e182d284ca047197c2960d7a5.jpg)  
Figure 1.4 A linear inverse problem: determine the density deviation of a buried line mass, $\Delta \rho ( x ) ,$ relative to a background model,from gravity anomaly observations $d ( x )$

roughened transformation of $d ( x )$ . For this reason we again need to be wary of possibly severe deleterious effects of noise in the data.

# Example 1.5

Consider a variation on Example 1.4,where the depth of the line density perturbation varies,rather than the density contrast. The gravity anomaly is now atributable to a variation in the burial depth, $m ( x ) = h ( x )$ , of an assumed known density perturbation, $\Delta \rho$ (Figure 1.5). The physics is the same as in Example 1.4,so the data are still given by the superposition of density perturbation contributions to the gravitational anomaly field, but the mathematical model now takes the form

$$
d ( x ) = \Gamma \intop _ { - \infty } ^ { \infty } \frac { m ( \xi ) } { \left( ( \xi - x ) ^ { 2 } + m ^ { 2 } ( \xi ) \right) ^ { 3 / 2 } } \Delta \rho d \xi .
$$

This problem is nonlinear in $m ( x )$ because (1.25) does not follow the superposition and scaling rules (1.5) and (1.6).

Nonlinear inverse problems are generally significantly more difficult to solve than linear ones.In special cases,they may be solvable by coordinate transformations that globally linearize the problem or by other clever special-case methods. In other cases, the problem cannot be globally linearized, so nonlinear optimization techniques must be applied. The essential differences in the treatment of linear and nonlinear problems arise because,as we shall see,all linear problems can be generalized to be the“same” in an important sense, so that a single set of solution methods can be applied to all. In contrast, nonlinear problems tend to be nonlinear in mathematically different ways and either require specific strategies or, more commonly, can by solved by iterative methods that may rely on local linearization.

![](images/74043c77762cc5c7a34164d1a852077dd608e391cffedd39554ea3d31935359e.jpg)  
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

![](images/d6eac43d71290eee4cd6d2089d9351c8aaef0d5bb222546e3eb78ce1368dbc72.jpg)  
Figure 1.6 The Shaw diffraction intensity problem (1.26).

![](images/3ca414f24e6e59d83af887102576894939d231c4b1d24d01d80575ca2d38c851.jpg)  
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

![](images/185b6cf4b106a67e4733118cb37b61903956c8f6bd51d81b0868df1a15c1bf90.jpg)  
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

![](images/1103cfd502a35cb5c922bc2f08120aad2c342ab7ff81346bcfc9831fb22a8f99.jpg)  
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

![](images/ce98fbfd6d89cd0969f8b93cc685566e09bdfc605470814739ea4107aeb16647.jpg)  
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

![](images/6c1c6150b6229057a92d9b4ac2a93129fada3e1f0c274d3d4f20cdd2303ce494.jpg)  
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

![](images/277384f4af13ab831d2b64ca1b113923b7a9b881847330587a50cc1883c5fa00.jpg)  
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

![](images/c17b7badf4a9b157e9f5102dbf574ad77bc82d47bb677bc5588e6bdbe435aed3.jpg)  
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

![](images/4da9410c14f96e20557532581022c2a7345a402e3ef613aa6d55f4ca81d5db32.jpg)  
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

![](images/18e2aca63dd19c83cd3b2a90a00b1c9612b0e5368491bd43b304b9b0ed775b44.jpg)  
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