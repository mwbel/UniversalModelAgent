# Numerical Methods for Least Squares Problems

Second Edition

![](images/59d86f7ba9f529f80d8d583e5076c6e8c322f4f778bfff4fda18e69e7506fa14.jpg)  
Ake Bjorck

Siam

# Numerical Methods for Least Squares Problems

# Numerical Methods for Least Squares Problems

Second Edition

Ake Bjorck Linkoping University Linkoping, Sweden

Society for Industrial and Applied Mathematics Philadelphia

# 10987654321

Allrights reserved.Printed in the United States of America.No part of this book may bereproduced,stored,or transmitted in any manner without the writen permisson of the publisher.For information, write to the Society for Industrial and Applied Mathematics,3600 Market Street,6th Floor,Philadelphia,PA 19104-2688 USA.

No warranties,express or implied,are made by the publisher,authors,and their employers that the programs contained in this volume are free of error.They should not be reliedon as the sole basis to solve a problem whose incorrect solution could result in injury to person or property.If the programs areemployed insuch amanner,it is at the user's own risk and the publisher,authors,and their employers disclaim alliability for such misuse.

Trademarked names may be used in this book without the inclusion of atrademark symbol.These names are used in an editorial context only;no infringement of trademark is intended.

MATLAB is a registered trademark of The MathWorks,Inc.For MATLAB product information,please contact The MathWorks,Inc.,3 Apple Hill Drive,Natick,MA 01760-2098 USA,508-647-700,Fax: 508-647-7001, info@mathworks.com,www.mathworks.com.

Publications Director   
Executive Editor   
Acquisitions Editor   
Developmental Editor   
Managing Editor   
Production Editor   
Copy Editor   
Production Manager   
Production Coordinator   
Compositor   
Graphic Designer

Kivmars H. Bowling Elizabeth Greenspan Elizabeth Greenspan Rose Kolassiba Kelly Thomas Lisa Briggeman Lisa Briggeman Rachel Ginder Cally A. Shrader Cheryl Hufnagle Doug Smock

SiamL s registretadear

# Contents

List of Figures vii

List of Tables ix

Preface xi

Preface to the First Edition xiii

# [ Mathematical and Statistical Foundations 1

1.1 Introduction 1   
1.2 Some Fundamental Matrix Decompositions 8   
1.3 Perturbation Analysis 19   
1.4 Floating-Point Computation 32

# 2 Basic Numerical Methods 39

2.1 The Method of Normal Equations 39   
2.2 Orthogonalization Methods 46   
2.3 Rank-Deficient Least Squares Problems 71   
2.4 Methods Based on LU Factorization 84   
2.5 Estimating Condition Numbers and Errors 94   
2.6 Blocked Algorithms and Subroutine Libraries 106

# 3 Generalized and Constrained Least Squares 115

3.1 Generalized Least Squares Problems 115   
3.2 Weighted Least Squares 128   
3.3 Modified Least Squares Problems 137   
3.4 Equality Constrained Problems 155   
3.5 Inequality Constrained Problems 160   
3.6 Regularized Least Squares. 171

# 4 Special Least Squares Problems 183

4.1 Band Least Squares Problems 183   
4.2 Bidiagonalization 191   
4.3 Some Structured Problems 204   
4.4 Total Least Squares .218   
4.5 Least Squares Problems with Special Bases . . 227

# 5 Direct Methods for Sparse Problems 243

5.1 Tools for Sparse Matrix Computations . 243   
5.2 Sparse QR Factorization . 253   
5.3 Special Topics .262

# 6 Iterative Methods 267

6.1 Basic Iterative Methods .267   
6.2 Krylov Subspace Methods 278   
6.3 Preconditioners for Least Squares Problems .306   
6.4 Regularization by Iterative Methods . . 325

# 7 SVD Algorithms and Matrix Functions 339

7.1 The QRSVD Algorithm .339   
7.2 Alternative SVD Algorithms 349   
7.3 Computing Selected Singular Triplets .363   
7.4 Matrix Functions and SVD .376

# 8 Nonlinear Least Squares Problems 389

8.1 Newton-Type Methods . .389   
8.2 Separable Least Squares Problems .402   
8.3 Nonnegativity Constrained Problems 416   
8.4 Robust Regression and Related Topics .420

# Bibliography 431

# Index 487

# List of Figures

1.1.1 Geometric interpretation of least squares property... 6   
2.2.1 Reflection of a vector $a$ in a hyperplane with normal $u$ 46   
3.6.1 Singular values $\sigma _ { i }$ of a discretized integral operator. 173   
4.1.1 Matrix $A$ after reduction of first $k = 3$ blocks using Householder reflections ．.190   
4.1.2 Reduction of a band matrix. .191   
4.2.1 Relative error and residual for PLS and TSVD solutions. 203   
4.3.1 One and two levels of dissection of a region. 206   
5.1.1 Nonzero pattern of matrix from structural problem and its Cholesky factor... 244   
5.1.2 The labeled graph $G ( C )$ of the matrix in (5.1.2). .248   
5.1.3 Sequence of elimination graphs of the matrix in (5.1.2). 249   
5.1.4 The transitive reduction and elimination tre $T ( A ^ { T } A )$ 250   
5.1.5 The graph of a matrix for which minimum degree is not optimal. 252   
5.2.1 Sparse matrix $A$ and factor $R$ using the MATLAB colperm reordering. 260   
5.2.2 Sparse matrix $A$ and factor $R$ using the MATLAB colamd ordering.. 260   
5.2.3 Structure of upper triangular matrix $R$ for a rank-deficient matrix. 261   
6.1.1 Structure of $A$ and $A ^ { T } A$ for a simple image reconstruction problem. 268   
6.2.1 $\lVert \boldsymbol { x } ^ { \dagger } - \boldsymbol { x } _ { k } \rVert$ and $\| A ^ { T } r _ { k } \|$ for problem ILLC1850: LSQR and CGLS . 295   
6.2.2 $\lVert \boldsymbol { x } ^ { \dagger } - \boldsymbol { x } _ { k } \rVert$ and $\| A ^ { T } r _ { k } \|$ for problem ILLC1850: LSQR and LSMR . 296   
6.2.3 Underdetermined consistent problem with transpose of ILLC1850: $\lVert x ^ { \dagger } - x _ { k } \rVert$   
and $\| r _ { k } \|$ ; CGME and LSME. . 297   
6.2.4 Problem ILLC1850 overdetermined consistent: $\lVert x ^ { \dagger } - x _ { k } \rVert$ and $\| r _ { k } \|$ ; CGME   
and CGLS .298   
7.3.1 Spectral transformation with shift $\mu = 1$ ： 366   
8.2.1 Orthogonal distance regression for $q = n = 1$ 407   
8.4.1 The penalizing effect using the $\ell _ { p }$ -norm for $p = 0 . 1 , 1 , 2 , 1 0$ 421

# List of Tables

1.4.1IEEE 754-2008 binary floating-point formats. 32

2.2.1Condition number and loss of orthogonality in CGS and MGS. 63   
2.5.1Average number of correct significant decimal digits.. 106

3.2.1 Average number of correct significant decimal digits in the solution before and after iterative refinement with various QR factorizations.. 132

7.1.1Comparison of multiplications for SVD algorithms.... . 347

# Preface

More than 25 years have passed since the first edition of this book was published in 1996.Least squares and least-norm problems have become more significant with every passng decade,and applications have grown in size,complexity,and variety. More advanced techniques for data acquisition give larger amounts of data to be treated. What counts as a large matrix has gone from dimension 1000 to $1 0 ^ { 6 }$ . Hence, iterative methods play an increasingly crucial role for the solution of least squares problems. On top of these changes, methods must be adapted to new generations of multiprocessing hardware.

This second edition is primarily aimed at applied mathematicians and graduate students. Like the first edition, it aims to give a comprehensive review of the state of the art and to survey the most important publications. Special effort has gone into making the revised bibliography as comprehensive and up to date as possble. More than half the references are new,and a substantial share are from the last decade.

To address the mentioned trends,many parts of this edition are enlarged and completely rewrittn. Several new sections have been added,and the content has been reordered.Because underdetermined linear systems increasingly occur in applications,the duality between least squares and least-norm problems is now more emphasized throughout.

The Cosine-Sine (CS) decomposition is a new addition to Chapter 1. Among the novelties in Chapter 2 are new results on Gram-Schmidt and block QR algorithms.Blocked and recursive algorithms for Cholesky and QR factorization are also covered. The section on computing the SVD has been much enlarged and moved to the new Chapter 7.

Chapter 3 presents more complete treatments of generalized and weighted least squares problems.Oblique projectors and elliptic Modified Gram-Schmidt (MGS) and Householder algorithms are other important additions,and new results are given on the stability of algorithms for weighted least squares. Linear equality and inequality constrained least squares problems are treated, along with a more complete treatment of quadratic constraints. A much enlarged treatment of regularization methods is also found in Chapter 3, including truncated singular value decomposition (SVD),Tikhonov regularization,and transformation to standard form.

Chapter 4 starts with a section on band matrices and methods for band least squares problems; this section originally appeared in Section 6.1 of the first edition. Next,a new section follows on Householder and Golub-Kahan bidiagonalizations and their connection to the concept of core problems for linear systems and Krylov subspace approximations. Another new section covers algorithms for the partial least squares (PLS) method for prediction and cause-effect inference. (PLS is much used in chemometrics, bioinformatics,food research, medicine, pharmacology, social sciences,physiology.）Next, this chapter gives methods for least squares problems with special structure,such as block-angular form, Kronecker, or Toeplitz. An introduction to tensor computations and tensor decompositions is also a new addition to this chapter. The section on total least squares problems now includes a treatment of large-scale problems.

Chapter 5 treats direct methods for sparse problems and corresponds to Chapter 6 in the first edition. New software,such as SuiteSparse QR,is surveyed.A notable addition is a section on methods for solving mixed sparse-dense least squares problems.

Iterative methods for least squares and least-norm problems are treated in Chapter 6. The Krylov subspace methods CGLS and LSQR as well as the recently introduced LSMR are de-scribed. The section on preconditioners is completely revised and covers new results on, e.g., approximate Cholesky and QR preconditioners.A survey of preconditioners based on random sampling is also new. Section 6.4 now covers regularization by iterative methods, including methods for saddle point and symmetric quasi-definite (SQD) systems.

Chapter 7 on algorithms for computing the SVD is a much enlarged version of Section 2.6 of the first edition. Here,new topics are Jacobi-type methods and differential qd and MRRR algorithms. Brief surveys of the matrix square root and sign functions as well as the polar decomposition are also included.

Chapter 8 covers methods for nonlinear least squares problems. Several new topics are included, such as inexact Gauss-Newton methods, bilinear least squares,and nonnegative least squares. Also discussed here are algorithms for robust regression, least-angle regression, and LASSO; compressed sensing; and iteratively reweighted least squares (IRLS).

# Acknowledgments

The works of Nick Higham, Lars Eldén, G. W. Stewart, Luc Giraud, and many others have been prominent inspirations for many of the topics new to this edition. Special thanks goes to Michael Saunders, who patiently read several versions of the book and gave valuable advice.Without his encouragement and support, this revision would never have been finished.

Ake Bjorck Linkoping,March 2023

# Preface to the First Edition

A basic problem in science is to fit a model to observations subject to errors. It is clear that the more observations that are available the more accurately will it be possible to calculate the parameters in the model. This gives rise to the problem of “solving”an overdetermined linear or nonlinear system of equations.It can be shown that the solution which minimizes a weighted sum of the squares of the residual is optimal in a certain sense. Gauss claims to have discovered the method of least squares in 1795 when he was 18 years old. Hence this book also marks the bicentennial of the use of the least squares principle.

The development of the basic modern numerical methods for solving linear least squares problems took place in the late sixties. The QR decomposition by Householder transformations was developed by Golub and published in 1965.The implicit QR algorithm for computing the singular value decomposition (SVD) was developed about the same time by Kahan, Golub,and Wilkinson,and the final algorithm was published in 1970. These matrix decompositions have since been developed and generalized to a high level of sophistication. Great progress has been made in the last decade in methods for generalized and modified least squares problems and in direct and iterative methods for large sparse problems.Methods for total least squares problems, which allow errors also in the system matrix,have been systematically developed.

Applications of least squares of crucial importance occur in many areas of applied and en-gineering research such as statistics, geodetics, photogrammetry, signal processing,and control. Because of the great increase in the capacity for automatic data capturing, least squares problems of large size are now routinely solved. Therefore, sparse direct methods as well as iterative methods play an increasingly important role. Applications in signal processing have created a great demand for stable and efficient methods for modifying least squares solutions when data are added or deleted. This has led to renewed interest in rank-revealing QR decompositions, which lend themselves beter to updating than the singular value decomposition. Generalized and weighted least squares problems and problems of Toeplitz and Kronecker structure are becoming increasingly important.

Chapter 1 gives the basic facts and the mathematical and statistical background of least squares methods. In Chapter 2 relevant matrix decompositions and basic numerical methods are covered in detail. Although most proofs are omitted, these two chapters are more elementary than the rest of the book and essentially self-contained. Chapter 3 treats modified least squares problems and includes many recent results.In Chapter 4 generalized QR and SVD decompositions are presented, and methods for generalized and weighted problems surveyed. Here also, robust methods and methods for total least squares are treated. Chapter 5 surveys methods for problems with linear and quadratic constraints. Direct and iterative methods for large sparse least squares problems are covered in Chapters 6 and 7. These methods are still subject to intensive research, and the presentation is more advanced. Chapter 8 is devoted to problems with special bases,including least squares fiting of polynomials and problems of Toeplitz and Kronecker structures. Finally, Chapter 9 contains a short survey of methods for nonlinear problems.

This book will be of interest to mathematicians working in numerical linear algebra, computational scientists and engineers,and statisticians,as well as electrical engineers. Although a solid understanding of numerical linear algebra is needed for the more advanced sections,I hope the book will be found useful in upper-level undergraduate and beginning graduate courses in scientific computing and applied sciences.

I have aimed to make the book and the bibliography as comprehensive and up to date as possible.Many recent research results are included, which were only available in the research literature before. Inevitably, however, the content reflects my own interests,and Iapologize in advance to those whose work has not been mentioned. In particular, work on the least squares problem in the former Soviet Union is, to a large extent, not covered.

The history of this book dates back to at least 1981, when I wrote a survey entitled “Least Squares Methods in Physics and Engineering” for the Academic Training Programme at CERN in Geneva. In 1985 I was invited to contribute a chapter on “Least Squares Methods” in the Handbook of Numerical Analysis,edited by P.G. Ciarlet and J. L. Lions. This chapter was finished in 1988 and appeared in Volume 1 of the Handbook,published by North-Holland in 1990.The present book is based on this contribution,although it has been extensively updated and made more complete.

The book has greatly benefited from the insight and knowledge kindly provided by many friends and colleagues. In particular, I have been greatly influenced by the work of Gene H. Golub, Nick Higham,and G. W. Stewart. Per-Ake Wedin gave valuable advice on the chapter on nonlinear problems. Part of the Handbook chapter was written while I had the benefit of visiting the Division of Mathematics and Statistics at CSIRO in Canberra and the Chr.Michelsen Institute in Bergen.

Thanks are due to Elsevier Science B.V.for the permission to use part of the material from the Handbook chapter. Finally,I thank Beth Gallagher and Vickie Kearn at SIAM for the cheerful and professional support they have given throughout the copy editing and production of the book.

Ake Bjorck Linkoping,February 1996

# Chapter 1

# Mathematical and Statistical Foundations

De tous les principes qu'on peut proposer pour cet objet, je pense qu'il n'en est pas de plus général, de plus exact, ni d'une application plus facile que celui qui ... consiste ä rendre minimum la somme de quarrés des erreurs.

—Adrien Marie Legendre, Nouvelles méthodes pour la détermination des orbites des cometes. Appendice.1805.

# 1.1 - Introduction

# 1.1.1 - Historical Remarks

The least squares problem is a computational problem of primary importance in science and engineering. Originally, it arose from the need to reduce the influence of errors when fitting a mathematical model to given observations. A way to do this is to use a greater number of measurements than the number of unknown parameters in the model. As an example, consider a function known to be a linear combination of $n$ known basis function $\phi _ { j } ( t )$ ：

$$
f ( t ) = \sum _ { j = 1 } ^ { n } c _ { j } \phi _ { j } ( t ) .
$$

The problem is to determine the $n$ unknown parameters $c _ { 1 } , \ldots , c _ { n }$ from $m > n$ measurements $f ( t _ { i } ) = y _ { i } + \epsilon _ { i }$ ， $i = 1 , \ldots , m$ ,subject to random errors $\epsilon _ { i }$

In 1748, before the development of the principle of least squares,Tobias Mayer had developed a method for “solving”overdetermined systems of equations,which later became known as the method of averages. The $m$ equations in $n$ unknowns are separated into $n$ groups and groupwise summed. In this way the overdetermined system is replaced by a square linear system that can be solved by elimination. Cauchy developed a related interpolation algorithm that leads to systems of the form

$$
\begin{array} { r } { Z ^ { T } A \vec { x } = Z ^ { T } \vec { b } , \quad Z = ( \vec { z } _ { 1 } , \dots , \vec { z } _ { n } ) , } \end{array}
$$

where $z _ { i j } = \pm 1$ . An advantage of this choice is that forming the new system requires no multiplications.

Laplace proposed in 1793 that observations be combined by minimizing the sum of the absolute values of the residuals $r _ { i } = y _ { i } - f ( t _ { i } )$ with the added condition that the sum of the residuals be equal to zero.He showed that this implies that the solution $x$ must satisfy exactly $n$ out of the $m$ equations. Gauss argued against this, saying that by the principles of probability, greater or smaller errors are equally possible in all equations. Therefore,a solution that precisely satisfies a subset of the equations must be regarded as less consistent with the laws of probability. This led him to the alternative principle of minimizing the sum of squared residuals $\textstyle S = \sum _ { i = 1 } ^ { m } r _ { i } ^ { 2 }$ ， which also gives a simpler computational procedure.

The first to publish the algebraic procedure and use the name “least squares method” was Legendre [729,18o5]. A few years later, in a paper titled (in translation) Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections2 Gauss [444,18ogl justified the method of least squares as a statistical procedure. Much to the annoyance of Legendre, he wrote

Our principle, which we have made use of since 1795,has lately been published by Legendre.

Most historians agree that Gauss was right in his claim of precedence.He had used the least squares principle earlier for the analyses of survey data and in astronomical calculations and had communicated the principle to several astronomers. A famous example is Gauss's prediction of the orbit of the asteroid Ceres in 1801. After this success, the method of least squares quickly became the standard procedure for analysis of astronomical and geodetic data and remains so to this day.

Another early application of the least squares method is from 1793.At that time,the French government decided to base the new metric system upon a unit,the meter, equal to one 10,000,Oooth part of the distance from the North Pole to the Equator along a meridian arc through Paris.In a 1795 survey, four subsections of an arc from Dunkirk to Barcelona were measured. For each subsection,the length $S$ of the arc (in modules), the degrees $d$ of latitude,and the latitude $L$ of the midpoint were determined by the following astronomical observations:

<table><tr><td>Segment</td><td>Arc length S</td><td>Latitude d</td><td>Midpoint L</td></tr><tr><td>Dunkirk to Pantheon</td><td>62472.59</td><td>2.18910°</td><td>49° 56&#x27; 30&quot;</td></tr><tr><td>Pantheon to Evaux</td><td>76145.74</td><td>2.66868°</td><td>47° 30&#x27; 46&quot;</td></tr><tr><td>Evaux to Carcassonne</td><td>84424.55</td><td>2.96336°</td><td>44° 41&#x27; 48&quot;</td></tr><tr><td>Carcassonne to Barcelona</td><td>52749.48</td><td>1.85266°</td><td>42° 17&#x27; 20&quot;</td></tr></table>

If the earth is assumed to be ellipsoidal, then to a good approximation it holds that

$$
z + y \sin ^ { 2 } ( L ) = S / d ,
$$

where $z$ and $y$ are unknown parameters. The meridian quadrant is then $M = 9 0 ( z + y / 2 )$ ， and the eccentricity $e$ is found from $1 / e \ : = \ : 3 ( z / y + 1 / 2 )$ ．The least squares estimates are $1 / e = 1 5 7 . 9 5 1 3 7 4$ and $M = 2 , 5 6 4 , 8 0 1 . 4 6$ ；see Stigler [1038,1981].

The early development of statistical methods for estimating parameters in linear models is surveyed by Farebrother [397,1999]. Detailed accounts of the invention and history of least squares are given by Plackett [895，1972]，Stigler [1037，1977]， [1038，1981],and Goldstine [484,1977].

Analyzing data sets of very large size is now a regular task in a broad variety of applications.The method of least squares, now over 2OO years old, is still one of the most frequently used methods for data fitting. Applications of least squares fitting cover a wide range of scientific disciplines, such as geodesy, photogrammetry, tomography, molecular modeling, structural analysis, signal processing, cluster analysis and pattern matching. Many of these lead to problems of large size and complexity.

An application of spectacular size for its time is the least squares adjustment of coordinates of the geodetic stations comprising the North American Datum; see Kolata [704,1978]. This problem consists of about 6.5 million equations in 540,Oo0 unknowns ( $\mathop { \bf { \bar { \ } { \ } } } =$ twice the number of stations). Since the equations are mildly nonlinear,only two or three linearized problems of this size have to be solved.

A more recent application is the determination of the gravity field of Earth from highly accurate satelite measurements; see Baboulin et al. [49, 2oo9]. To model the gravitational potential, a function of the form

$$
V ( r , \theta , \lambda ) = \frac { G M } { R } \sum _ { l = 0 } ^ { L } \left( \frac { r } { R } \right) ^ { l + 1 } \sum _ { m = 0 } ^ { l } P _ { l m } ( \cos \theta ) \left[ c _ { l m } \cos m \lambda + s _ { l m } \sin m \lambda \right]
$$

is used,where $G$ is the gravitational constant, $M$ is Earth's mass, $R$ is Earth's reference radius, and $P _ { l m }$ are the normalized Legendre polynomials of order $m$ ． The normalized harmonic coefficients $c _ { l m }$ and $s _ { l m }$ are to be determined. For $L = 3 0 0$ ，the resulting least squares problem involves 90,OoO unknowns and millions of observations and needs to be solved on a daily basis.

The demand for fast and accurate least squares solvers continues to grow as problem scales become larger and larger. Analyzing data sets of billions of records is now a regular task at many companies and institutions. Such large-scale problems arise in a variety of fields,such as genetics, image processing, geophysics, language processing, and high-frequency trading.

# 1.1.2 - Statistical Preliminaries

Gauss gave the method a sound theoretical basis in his two-part memoir,“Theoria Combinationis”[445,1821],[446,1823]. These contain his definitive treatment of the area. (An English translation is given by Stewart [447,1995l.） Gauss proves the optimality of the least squares estimate without assuming that the random errors follow a particular distribution. This contribution of Gauss was somehow neglected until being rediscovered by Markov [775,1912]; see Theorem 1.1.4.

Let $x$ be a random variable with distribution function $F ( x )$ ，where $F ( x )$ is nondecreasing and right continuous and satisfies

$$
0 \leq F ( x ) \leq 1 , \quad F ( - \infty ) = 0 , \quad F ( \infty ) = 1 .
$$

The expected value $\mu$ and variance $\sigma ^ { 2 }$ of $x$ are defined as

$$
\mu = \mathcal { E } ( x ) = \int _ { - \infty } ^ { \infty } y d F ( x ) , \quad \sigma ^ { 2 } = \mathcal { E } \big ( ( x - \mu ) ^ { 2 } \big ) = \int _ { - \infty } ^ { \infty } ( x - \mu ) ^ { 2 } d F ( x ) .
$$

Let $\boldsymbol { x } = ( x _ { 1 } , \ldots , x _ { n } ) ^ { T }$ be a vector of random variables where the joint distribution of $x _ { i }$ and $x _ { j }$ is $F ( x _ { i } , x _ { j } )$ . Then the covariance $\sigma _ { i j }$ between $x _ { i }$ and $x _ { j }$ is defined by

$$
\tau _ { i j } = \mathrm { c o v } ( x _ { i } , x _ { j } ) = \mathcal { E } [ ( x _ { i } - \mu _ { i } ) ( x _ { j } - \mu _ { j } ) ] = \int _ { x _ { i } , x _ { j } = - \infty } ^ { \infty } ( x _ { i } - \mu _ { i } ) ( x _ { j } - \mu _ { j } ) d F ( x _ { i } , x _ { j } ) .
$$

Then $\sigma _ { i j } = \mathcal { E } ( x _ { i } x _ { j } ) - \mu _ { i } \mu _ { j }$ , where $\mu _ { i } = \mathcal { E } ( x _ { i } )$ . The covariance matrix $V \in \mathbb { R } ^ { n \times n }$ of the vecto1 $x$ is defined by

$$
\mathcal V ( x ) = V = \mathcal E [ ( x - \mu ) ( x - \mu ) ^ { T } ] = \mathcal E ( x x ^ { T } ) - \mu \mu ^ { T } ,
$$

where $\mu = { \mathcal { E } } ( x ) = ( \mu _ { 1 } , \ldots , \mu _ { n } )$ . We now prove some useful properties.

Lemma 1.1.1. Let $z = F x$ where $\boldsymbol { F } \in \mathbb { R } ^ { m \times n }$ is a given matrix, and let $x \in \mathbb { R } ^ { n }$ be a random vector with $\mathcal { E } ( x ) = \mu$ and covariance matrix $V$ .Then

$$
\mathcal { E } ( z ) = F \mu , \qquad \mathcal { V } ( z ) = F V F ^ { T } .
$$

Proof. The first property follows directly from the definition of expected value. The second is proved as

$$
\mathcal V ( F x ) = \mathcal E [ F ( x - \mu ) ( x - \mu ) ^ { T } F ^ { T } ] = F \mathcal E [ ( x - \mu ) ( x - \mu ) ^ { T } ] F ^ { T } = F V F ^ { T } .
$$

In the special case when $F = f ^ { T }$ is a row vector, $z = f ^ { T } x$ is a linear functional of $x$ . Then, if $V = \sigma ^ { 2 } I$ ， $\mathcal { V } ( z ) = \sigma ^ { 2 } f ^ { T } f$ . The following lemma is given without proof.

Lemma 1.1.2. Let $A \in \mathbb { R } ^ { n \times n }$ be a symmetric matrix, and let y be a random vector with expected value $\mu$ and covariance matrix $V$ .Then

$$
{ \mathcal { E } } ( y ^ { T } A y ) = \mu ^ { T } A \mu + \operatorname { t r a c e } \left( A V \right) ,
$$

where trace $( A V )$ denotes the sum of diagonal elements of $A V$

In the Gauss-Markov linear model it is assumed that the random vector of observations $b \in \mathbb { R } ^ { m }$ is related to a parameter vector $x \in \mathbb { R } ^ { n }$ by a linear equation

$$
A x = b , \quad \mathcal { E } ( b ) = \bar { b } , \quad \mathcal { V } ( b ) = \sigma ^ { 2 } V ,
$$

where $V$ is the known covariance of a random error vector $\epsilon$ of mean zero. The standard model has $V = I$ ,i.e., the errors $b _ { i } - { \bar { b } } _ { i }$ are assumed to be uncorrelated and to have the same variance.

Definition 1.1.3. A function $f ( x )$ of a random vector $x$ is an unbiased estimate of a parameter $\theta i f { \mathcal { E } } ( f ( x ) ) = \theta$ If c is a vector of constants, then $c ^ { T } x$ is called a best linear unbiased estimate of $\theta$ if $\mathcal { E } ( c ^ { T } x ) = \theta$ and $\mathcal { V } ( c ^ { T } x )$ is minimized over allinear estimates.

Theorem 1.1.4(Gauss-Markov Theorem). Consider the standard Gauss-Markov linear model (1.1.2), where $A \in \mathbb { R } ^ { m \times n }$ is a known matrix of rank $n$ . Then the best linear unbiased estimate of any linear functional $c ^ { T } x$ is $c ^ { T } { \widehat { x } } ,$ where $\widehat { x }$ is the least squares estimator that minimizes the sum of squares $r ^ { T } r$ ，where $r = b - A x$ Furthermore, $\widehat { x }$ is obtained by solving the symmetric positive definite system of normal equations

$$
A ^ { T } A x = A ^ { T } b .
$$

Proof. See Theorem 1.1.5 and Zelen [1143,1962, pp. 560-561].

In the literature,this result is often stated in less general form, where the errors are assumed to be normally distributed or independent and identically distributed. However, Gauss only assumed the weaker condition that the errors are uncorrelated with zero mean and equal variance.

From Lemma 1.1.1 it follows that the covariance matrix of the least squares estimate ${ \widehat { x } } =$ $( A ^ { T } A ) ^ { - 1 } A ^ { T } b$ is

$$
\mathcal V ( \widehat x ) = ( A ^ { T } A ) ^ { - 1 } A ^ { T } \mathcal V ( \widehat b ) A ( A ^ { T } A ) ^ { - 1 } = \sigma ^ { 2 } ( A ^ { T } A ) ^ { - 1 } .
$$

Let $\sigma ^ { 2 } = \mathcal { E } ( s ^ { 2 } )$ , where $s ^ { 2 }$ is the quadratic form

$$
s ^ { 2 } = \frac { 1 } { m - n } \hat { r } ^ { T } \hat { r } , \quad \hat { r } = b - A \hat { x } .
$$

It can be shown that the $s ^ { 2 }$ ,and therefore also the $\widehat { r }$ is uncorrelated with $\widehat { x }$ ,i.e.,

$$
\operatorname { c o v } ( { \widehat { r } } , { \widehat { x } } ) = 0 , \qquad \operatorname { c o v } ( s ^ { 2 } , { \widehat { x } } ) = 0 .
$$

From the normal equations it follows that $A ^ { T } { \widehat { r } } = A ^ { T } ( b - A { \widehat { x } } ) = 0 .$ .This shows that there are $n$ linear relations among the $m$ components of $\widehat { r }$

Some applications lead to complex least squares problems to minimize

$$
\| r \| _ { 2 } ^ { 2 } = r ^ { H } r = \sum _ { i = 1 } ^ { n } | r _ { i } | ^ { 2 } , \quad r = b - A x ,
$$

where $A \in \mathbb { C } ^ { m \times n }$ ， $b \in \mathbb { C } ^ { m }$ ，and $r ^ { H }$ denotes the conjugate transpose of $r$ .An example in complex stochastic processes is given by Miller [795,1973]. In the complex case, the normal equations are

$$
{ \cal A } ^ { H } { \cal A } x = { \cal A } ^ { H } b ,
$$

where $A ^ { H }$ is the conjugate transpose of $A$ .Most of the results and algorithms for the real case given in this book admit straightforward extensions to the complex case.

The least squares method can be generalized to a Gauss-Markov linear model with $\operatorname { r a n k } ( A ) =$ $n$ and a positive definite covariance matrix $\mathcal { V } ( \epsilon ) = \sigma ^ { 2 } V$

Gauss and Laplace also treated weighted least squares problems, where the covariance matrix is diagonal: $V = \operatorname { d i a g } \left( v _ { 1 } , \ldots , v _ { m } \right)$ . The case with a general positive definite covariance matrix $V$ was first considered by Aitken [12,1934]. The best unbiased linear estimate of $x$ is then obtained from the generalized least squares problem

$$
\operatorname* { m i n } _ { x } ( A x - b ) ^ { T } V ^ { - 1 } ( A x - b )
$$

and satisfies the generalized normal equations (see Section 3.1)

$$
A ^ { T } V ^ { - 1 } A x = A ^ { T } V ^ { - 1 } b .
$$

# 1.1.3 - Characterization of Least Squares Solutions

Theorem 1.1.5. Given $A \in \mathbb { R } ^ { m \times n }$ ， $m > n$ ， $b \in \mathbb { R } ^ { m }$ let

$$
\mathcal { S } = \{ x \in \mathbb { R } ^ { n } \ \vert \ \Vert A x - b \Vert _ { 2 } = \operatorname* { m i n } \}
$$

be the set of all least squares solutions, where $\| \cdot \| _ { 2 }$ denotes the Euclidean vector norm $\| x \| _ { 2 } =$ $( x ^ { T } x ) ^ { 1 / 2 }$ .Then $x \in { \mathcal { S } }$ if and onlyif the orthogonality condition $A ^ { T } ( b - A x ) = 0$ holds or, equivalently, $x$ satisfies the normal equations

$$
A ^ { T } A x = A ^ { T } b .
$$

Proof. Assume that $\hat { x }$ satisfies $A ^ { T } \hat { r } = 0$ ，where ${ \hat { r } } = b - A { \hat { x } }$ . Then for any $x \in \mathbb { R } ^ { n }$ we have $r = b - A x = \hat { r } + A ( \hat { x } - x ) \equiv \hat { r } + A e$ From this we obtain

$$
\boldsymbol { r } ^ { T } \boldsymbol { r } = ( \hat { \boldsymbol { r } } + \boldsymbol { A } \boldsymbol { e } ) ^ { T } ( \hat { \boldsymbol { r } } + \boldsymbol { A } \boldsymbol { e } ) = \hat { \boldsymbol { r } } ^ { T } \hat { \boldsymbol { r } } + \| \boldsymbol { A } \boldsymbol { e } \| _ { 2 } ^ { 2 } ,
$$

which is minimized when $x = { \hat { x } }$ . On the other hand,suppose $A ^ { T } \hat { r } = z \neq 0$ If $x = \hat { x } + \epsilon z$ ,then $r = \hat { r } - \epsilon A z$ and

$$
\boldsymbol { r } ^ { T } \boldsymbol { r } = \hat { r } ^ { T } \hat { \boldsymbol { r } } - 2 \epsilon z ^ { T } \boldsymbol { z } + \epsilon ^ { 2 } ( A z ) ^ { T } A \boldsymbol { z } < \hat { r } ^ { T } \hat { \boldsymbol { r } }
$$

for sufficiently small $\epsilon > 0$ . Hence $\hat { x }$ is not a least squares solution.

Theorem 1.1.6. The matrix $A ^ { T } A$ of normal equations is positive definite if and only if the columns of $A \in \mathbb { R } ^ { m \times n }$ are linearly independent, i.e., $\operatorname { r a n k } ( A ) = n$ .Then the matrix $( A ^ { T } A ) ^ { - 1 }$ exists,and the unique least squares solution and residual are

$$
\begin{array} { r } { x = ( A ^ { T } A ) ^ { - 1 } A ^ { T } b , \qquad r = b - A ( A ^ { T } A ) ^ { - 1 } A ^ { T } b . } \end{array}
$$

Proof. If the columns of $A$ are linearly independent, then $x \neq 0 \Rightarrow A x \neq 0$ ，and therefore $x \neq 0 \Rightarrow x ^ { T } A ^ { T } A x = \| A x \| _ { 2 } ^ { 2 } > 0$ Hence $A ^ { T } A$ is positive definite. On the other hand, if the columns are linearly dependent, then for some $x _ { 0 } \neq 0$ we have $A x _ { 0 } = 0$ .Then $x _ { 0 } ^ { T } A ^ { T } A x _ { 0 } = 0$ and $A ^ { T } A$ is only positive semidefinite. □

For a matrix $A \in \mathbb { R } ^ { m \times n }$ of rank $r$ , the range (or column space)is the subspace

$$
{ \mathcal { R } } ( A ) = \{ y = A x \mid x \in \mathbb { R } ^ { n } \} \in \mathbb { R } ^ { m }
$$

of dimension $r$ .Because $A ^ { T } b \in \mathcal { R } ( A ^ { T } ) = \mathcal { R } ( A ^ { T } A )$ ，the normal equations are consistent. Hence, for $A$ of any dimensions and rank there always exists at least one least squares solution. From the normal equations $A ^ { T } ( b - A x ) = A ^ { T } r = 0$ , it follows that

$$
A x \in { \mathcal { R } } ( A ) , \qquad r = b - A x \perp { \mathcal { R } } ( A ) .
$$

Thus, $x$ is a least squares solution if and only if the residual $r = b - A x$ is perpendicular to $\mathcal { R } ( A )$ This geometric characterization is shown in Figure 1.1.1. The nullspace of a matrix $A \in \mathbb { R } ^ { m \times n }$ is defined as the subspace

$$
\mathcal { N } ( A ) = \{ z \in \mathbb { R } ^ { m } \mid A z = 0 \} \in \mathbb { R } ^ { n }
$$

of dimension $n - r$ . A fundamental theorem in linear algebra says that

$$
{ \mathcal { R } } ( A ) \cup { \mathcal { N } } ( A ^ { T } ) = \mathbb { R } ^ { m } , \qquad { \mathcal { N } } ( A ) \cup { \mathcal { R } } ( A ^ { T } ) = \mathbb { R } ^ { n } ,
$$

where $\mathbb { R } ^ { m }$ and $\mathbb { R } ^ { n }$ denote the space of $m$ -vectors and $n$ -vectors. Further, from the singular value decomposition (SVD) of $A$ in Section 1.2.2 it follows that ${ \mathcal { R } } ( A ) \perp { \mathcal { N } } ( A ^ { T } )$ and ${ \mathcal { N } } ( A ) \perp$ $\mathcal { R } ( A ^ { T } )$

Definition 1.1.7. A square matrix $P \in \mathbb { C } ^ { m \times m }$ is a projector onto $\mathcal { R } ( P )$ if it satisfies $P ^ { 2 } = P$ or, equivalently, $P ( I - P ) = 0 $ Such a matrix is also called idempotent. If also $P ^ { T } = P$ ，then $P$ is an orthogonal projector.

![](images/775294b85f01d6336771112f9ca1c9b21af61ff5b1fff6e5c1bd8812083ea217.jpg)  
Figure1.1.1. Geometric interpretation of least squares property.

If $P$ is an orthogonal projector, then $P ( I - P ) b = ( P - P ^ { 2 } ) b = 0$ and

$$
( I - P ) ^ { 2 } = I - 2 P + P ^ { 2 } = ( I - P ) .
$$

It follows that $I - P$ is an orthogonal projector onto $\mathcal { N } ( P )$ . The rank-one modification of the unit matrix

$$
\begin{array} { r } { P = I - q q ^ { T } , \quad q ^ { T } q = 1 , } \end{array}
$$

is called an elementary orthogonal projector. An arbitrary vector $b \in \mathbb { R } ^ { m }$ is uniquely decom-posed by an orthogonal projector $P$ into two components $b = P b + ( I - P ) b = b _ { 1 } + b _ { 2 }$ ，such that $b _ { 1 } \perp b _ { 2 }$ .If $\lambda$ is an eigenvalue of $P$ ,then $P x = \lambda x$ for some nonzero $x$ .From $P ^ { 2 } = P$ it follows that $\lambda ^ { 2 } = \lambda$ . Hence the eigenvalues of $P$ are either 1 or O,and $\operatorname { r a n k } ( P ) = \operatorname { t r a c e } \left( P \right)$

The orthogonal projector onto a given subspace can be shown to be unique. If $\operatorname { r a n k } ( A ) = n$ ， we find from the normal equation that $A x = A ( A ^ { T } A ) ^ { - 1 } A ^ { T } b .$ Hence,

$$
P = A ( A ^ { T } A ) ^ { - 1 } A ^ { T }
$$

is the orthogonal projector onto $\mathcal { R } ( A )$ . The above results can be summarized as follows.

Theorem 1.1.8. The following statements are equivalent:

1. x solves the least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$

2. x satisfies the normal equation $A ^ { T } A x = A ^ { T } b$

3. The residual $r = b - A x$ is orthogonal to $\mathcal { R } ( A )$

4. x solves the consistent linear system $A x = P _ { \mathcal { R } ( A ) } b _ { \mathrm { ~ ~ } }$ where $P _ { \mathcal { R } ( A ) }$ is the orthogonal pro-jector onto $\mathcal { R } ( A )$

If $r = { \mathrm { r a n k } } ( A ) < n$ ,then $A$ has a nullspace of dimension $n - r > 0$ . Then the problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ is underdetermined,and its solution is not unique. If $\hat { x }$ is a particular least squares solution, then the set of all least squares solutions is ${ \mathcal { S } } = \{ x = { \hat { x } } + z \mid z \in { \mathcal { N } } ( A ) \}$ In this case we can seek the least squares solution of least-norm $\lVert x \rVert _ { 2 }$ ,i.e., solve

$$
\operatorname* { m i n } _ { x \in S } \| x \| _ { 2 } , \quad S = \{ x \in \mathbb { R } ^ { n } \mid \| b - A x \| _ { 2 } = \operatorname* { m i n } \} .
$$

This solution is always unique.

Theorem 1.1.9. Let x be a solution of the problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ Then $x$ is a least squares solution of least-norm if and only if $x \perp { \mathcal { N } } ( A )$ or, equivalently, $x = A ^ { T } z$ $z \in \mathbb { R } ^ { m }$

Proof. Let $\hat { x }$ be any least squares solution, and set $x = { \hat { x } } + z$ ,where $z \in \mathcal { N } ( A )$ . Then $A z = 0$ ， s0 $r = b - A \hat { x } = b - A x$ and $\hat { x }$ is also a least squares solution. By the Pythagorean theorem, $\| x \| _ { 2 } ^ { 2 } = \| \hat { x } \| _ { 2 } ^ { 2 } + \| z \| _ { 2 } ^ { 2 }$ , which is minimized when $z = 0$ □

If the system $A x = b$ is consistent, then the least-norm solution satisfies the normal equations of second kind,

$$
x = A ^ { T } z , \quad A A ^ { T } z = b .
$$

f $\operatorname { r a n k } ( A ) = m$ ,then $A A ^ { T }$ is nonsingular,and the solution to (1.1.17) is unique.

From this result and Theorem 1.1.8 we have the following characterization of a solution to the least squares problem (1.1.16). It includes both the over- and underdetermined cases.

Theorem 1.1.10. For $A$ of any dimension and rank, the least squares solution of minimum norm $\| x \| _ { 2 }$ is unique and characterized by the conditions

$$
r = b - A x \perp \mathcal { R } ( A ) \ a n d \ x \perp \mathcal { N } ( A ) .
$$

The normal equations $A ^ { T } A x = A ^ { T } b$ are equivalent to the linear equations $A ^ { T } r = 0$ and $r = b - A x$ .Together, these form a symmetric augmented system of $m + n$ equations

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { y } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { b } } \\ { { c } } \end{array} \right) ,
$$

where $y = r$ and $c = 0$ . The augmented system is nonsingular if and only if $\operatorname { r a n k } ( A ) = n$ .Then its inverse is

$$
\left( \begin{array} { c c } { \boldsymbol { I } } & { \boldsymbol { A } } \\ { \boldsymbol { A } ^ { T } } & { \boldsymbol { 0 } } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { \boldsymbol { I } - \boldsymbol { P } _ { \mathcal { R } ( A ) } } & { \boldsymbol { A } ( \boldsymbol { A } ^ { T } \boldsymbol { A } ) ^ { - 1 } } \\ { ( \boldsymbol { A } ^ { T } \boldsymbol { A } ) ^ { - 1 } \boldsymbol { A } ^ { T } } & { - ( \boldsymbol { A } ^ { T } \boldsymbol { A } ) ^ { - 1 } } \end{array} \right) ,
$$

where $P _ { \mathcal { R } ( A ) } = A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ is the orthogonal projector onto $\mathcal { R } ( A )$

Theorem 1.1.11. $I f \operatorname { r a n k } ( A ) = n$ ， then the augmented system (1.1.19) has a unique solution that solves the primal and dual least squares problems,

$$
\begin{array} { r l } & { \underset { x \in \mathbb { R } ^ { n } } { \operatorname* { m i n } } \frac { 1 } { 2 } \| b - A x \| _ { 2 } ^ { 2 } + c ^ { T } x , } \\ & { \underset { y \in \mathbb { R } ^ { m } } { \operatorname* { m i n } } \frac { 1 } { 2 } \| y - b \| _ { 2 } ^ { 2 } \ s u b j e c t \ t o \ A ^ { T } y = c . } \end{array}
$$

Proof. Differentiating (1.1.21) gives $A ^ { T } ( b - A x ) = c$ ,which with $y = b - A x$ is the augmented system (1.1.19). This system is also obtained by differentiating the Lagrangian

$$
L ( x , y ) = \frac { 1 } { 2 } ( y - b ) ^ { T } ( y - b ) + x ^ { T } ( A ^ { T } y - c )
$$

for (1.1.22) and equating to zero. Here $x$ is the vector of Lagrange multipliers.

# 1.2 - Some Fundamental Matrix Decompositions

# 1.2.1 - The Cholesky Factorization

The classical method for solving a linear least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ ， $A \in \mathbb { R } ^ { m \times n }$ ,is to form and solve the symmetric normal equations $A ^ { T } A x = A ^ { T } b$ If $\operatorname { r a n k } ( A ) = n$ ,then $x \neq 0$ implies that $A x \neq 0$ .Hence

$$
x ^ { T } A ^ { T } A x > 0 \quad \forall x \in \mathbb { R } ^ { n } , \quad x \neq 0 ,
$$

and $A ^ { T } A$ is positive definite. Conversely, a symmetric positive definite matrix is nonsingular. If it were singular, there would be a vector $x$ such that $A x = 0$ .But then $x ^ { T } A x = 0$ ,which is a contradiction. To solve the normal equations, Gauss developed an elimination process that uses pivots from the diagonal; see Stewart [1O29,1995]. Then al reduced matrices are symmetric, and only elements on and below (say) the main diagonal have to be computed. This reduces the number of operations and amount of storage needed by half.

Theorem 1.2.1 (Cholesky Factorization). Let the matrix $C \in \mathbb { C } ^ { n \times n }$ be Hermitian positive definite. Then there exists a unique upper triangular matrix $R = \left( r _ { i j } \right)$ with real positive diagonal elements called the Cholesky factor of $C$ such that

$$
C = R ^ { H } R .
$$

Proof. The proof is by induction. The result is clearly true for $n = 1$ . If it is true for some $n - 1$ , the leading principal submatrix $C _ { n - 1 }$ of $C$ has a unique Cholesky factorization $C _ { n - 1 } =$ $R _ { n - 1 } ^ { H } R _ { n - 1 }$ , where $R _ { n - 1 }$ is nonsingular. Then

$$
\begin{array} { r } { \boldsymbol { C _ { n } } = \left( \begin{array} { c c } { \boldsymbol { C _ { n - 1 } } } & { \boldsymbol { d } } \\ { \boldsymbol { d ^ { H } } } & { \boldsymbol { \gamma } } \end{array} \right) = \left( \begin{array} { c c } { \boldsymbol { R _ { n - 1 } ^ { H } } } & { \boldsymbol { 0 } } \\ { \boldsymbol { r ^ { H } } } & { \boldsymbol { \rho } } \end{array} \right) \left( \begin{array} { c c } { \boldsymbol { R _ { n - 1 } } } & { \boldsymbol { r } } \\ { \boldsymbol { 0 } } & { \boldsymbol { \rho } } \end{array} \right) } \end{array}
$$

holds if $r$ and $\rho$ satisfy

$$
R _ { n - 1 } ^ { H } r = d , \qquad r ^ { H } r + \rho ^ { 2 } = \gamma .
$$

The first equation has a unique solution $r$ . It remains to show that $\gamma - r ^ { H } r > 0$ .From the positive definiteness of $C$ it follows that

$$
\begin{array} { r l } { 0 < \bigl ( r ^ { H } R _ { n - 1 } ^ { - H } } & { - 1 \bigr ) A \left( \begin{array} { c } { R _ { n - 1 } ^ { - 1 } r } \\ { - 1 } \end{array} \right) = r ^ { H } R _ { n - 1 } ^ { - H } C _ { n - 1 } R _ { n - 1 } ^ { - 1 } r - 2 r ^ { H } R _ { n - 1 } ^ { - 1 } c + \gamma } \\ & { \qquad = r ^ { H } r - 2 r ^ { H } r + \gamma = \gamma - r ^ { H } r . } \end{array}
$$

Hence $\rho = ( \gamma - r ^ { H } r ) ^ { 1 / 2 }$ is uniquely determined.

Substituting the Cholesky factorization $C = A ^ { H } A = R ^ { H } R$ into the normal equations gives $R ^ { H } R x = d$ , where $d = A ^ { H } b$ . Hence,the solution is obtained by solving two triangular systems,

$$
R ^ { H } z = d , \qquad R x = z .
$$

This method is easy to implement and often faster than other direct solution methods. It works well unless $A$ is ill-conditioned.

For a consistent underdetermined linear system $A x = b$ ,the solution to the least-norm problem min $\| x \| _ { 2 }$ subject to $A x = b$ satisfies the normal equations of the second kind,

$$
x = A ^ { H } z , \qquad A A ^ { H } z = b .
$$

If $A$ has full row rank, then $A A ^ { H }$ is symmetric positive definite,and the Cholesky factorization $A A ^ { H } = R ^ { H } R$ exists. Then $z$ is obtained by solving

$$
R ^ { H } w = b , \qquad R z = w .
$$

It is often preferable to work with the Cholesky factorization of the cross-product of the extended matrix $( A b )$ ，

$$
\begin{array} { r } { \left( \begin{array} { l } { A ^ { H } } \\ { b ^ { H } } \end{array} \right) ( A \quad b ) = \left( \begin{array} { l l } { A ^ { H } A } & { A ^ { H } b } \\ { b ^ { H } A } & { b ^ { H } b } \end{array} \right) , } \end{array}
$$

when solving a least squares problem. If $\operatorname { r a n k } ( A ) = n$ ,then the Cholesky factor of the crossproduct (1.2.7),

$$
S = \left( \begin{array} { c c } { { R } } & { { z } } \\ { { 0 } } & { { \rho } } \end{array} \right) ,
$$

exists, where we may have $\rho = 0$ .Forming $S ^ { H } S$ shows that

$$
A ^ { H } A = R ^ { H } R , \qquad R ^ { H } z = A ^ { H } b , \qquad b ^ { H } b = z ^ { H } z + \rho ^ { 2 } .
$$

Hence, $R$ is the Cholesky factor of $A ^ { H } A$ , and the least squares solution is obtained from $R x = z$ Since $r = b - A x$ is orthogonal to $A x$ ,we have

$$
\| A x \| _ { 2 } ^ { 2 } = ( r + A x ) ^ { H } A x = b ^ { H } A x = b ^ { H } A R ^ { - 1 } R ^ { - T } A ^ { H } b = z ^ { H } z ,
$$

and hence $\| r \| _ { 2 } ^ { 2 } = \rho ^ { 2 } = b ^ { H } b - z ^ { H } z$ and $| b - A x | | _ { 2 } = \rho$

Let $A \in \mathbb { C } ^ { m \times n }$ have full column rank, let $A ^ { H } A = R ^ { H } R$ be its Cholesky factorization, and set $Q _ { 1 } = A R ^ { - 1 }$ . Then

$$
A = Q _ { 1 } R , \quad Q _ { 1 } ^ { H } Q _ { 1 } = I _ { n } ,
$$

is the Cholesky QR factorization of $A$ The orthonormal factor $Q _ { 1 }$ can be computed as the unique solution of the lower triangular matrix equation $R ^ { H } Q _ { 1 } ^ { H } = A ^ { H }$ by forward substitution. The normal equation simplifies to $R ^ { H } Q _ { 1 } ^ { H } Q _ { 1 } R x = R ^ { H } R x = R ^ { H } Q _ { 1 } ^ { H } b$ or

$$
R x = Q _ { 1 } ^ { H } b .
$$

In the real case, the arithmetic cost of this Cholesky QR algorithm is $2 m n ^ { 2 } + n ^ { 3 } / 3$ flops. More accurate methods that compute the QR factorization (1.2.9) directly from $A$ are described in Sections 2.2.2-2.2.4.

We now state some useful properties of Hermitian positive definite matrices. From the proof of Theorem 1.2.1 follows a well-known characterization.

Lemma 1.2.2 (Sylvester's Criterion). Let $C _ { k } \in \mathbb { C } ^ { k \times k }$ ， $k = 1 , \dots , n$ be the leading principal submatrices of the Hermitian matrix $C \in \mathbb { C } ^ { n \times n }$ Then $C$ is positive definite if and only if $\operatorname* { d e t } ( C _ { k } ) > 0$ $k = 1 , \dots , n$

Theorem 1.2.3. Let $C \in \mathbb { C } ^ { n \times n }$ be Hermitian, and let $\ b X \in \mathbb { C } ^ { n \times p }$ have full column rank. Then $X ^ { H } C X$ is positive definite. In particular, any principal $p \times p$ submatrix

$$
\left( \begin{array} { c c c } { c _ { i _ { 1 } i _ { 1 } } } & { \ldots } & { c _ { i _ { 1 } i _ { p } } } \\ { \vdots } & & { \vdots } \\ { \bar { c } _ { i _ { p } i _ { 1 } } } & { \ldots } & { c _ { i _ { p } i _ { p } } } \end{array} \right) \in \mathbb { C } ^ { p \times p } , \quad 1 \leq p < n ,
$$

is positive definite. From $p = 1$ it follows that all diagonal elements in $C$ are real positive.

Proof. Suppose $C$ is positive definite, $z \neq 0$ ,and $y = X z$ .Then since $X$ has full column rank, it follows that $y \ne 0$ and

$$
z ^ { H } ( X ^ { H } C X ) z = y ^ { H } C y > 0 .
$$

The result now follows because any principal submatrix of $C$ can be written as $X ^ { H } C X$ ,where the columns of $X$ are taken to be the columns $\begin{array} { r l r } { k } & { { } = } & { i _ { j } } \end{array}$ ， $\begin{array} { r c l } { j } & { = } & { 1 , \dotsc , p } \end{array}$ ，of the identity matrix. $\bigtriangledown$

Theorem 1.2.4. The element of maximum magnitude of a real symmetric positive definite matrix $C = ( c _ { i j } ) \in \mathbb { C } ^ { n \times n }$ lies on the diagonal.

Proof.From Theorem 1.2.3 and Sylvester's criterion it follows that

$$
\operatorname* { d e t } \left( \begin{array} { l l } { c _ { i i } } & { c _ { i j } } \\ { \bar { c } _ { i j } } & { c _ { j j } } \end{array} \right) = c _ { i i } c _ { j j } - | c _ { i j } | ^ { 2 } > 0 , \quad 1 \leq i , j \leq n .
$$

Hence $\begin{array} { r } { | c _ { i j } | ^ { 2 } < c _ { i i } c _ { j j } \leq \operatorname* { m a x } _ { 1 \leq i \leq n } c _ { i i } ^ { 2 } } \end{array}$

# 1.2.2 - SVD and Related Eigenvalue Decompositions

The singular value decomposition (SVD) provides a diagonal form of a complex bilinear form $x ^ { T } A y$ $A \in \mathbb { C } ^ { m \times n }$ , under a unitary equivalence transformation. It has numerous applications in areas such as signal and image processing, control theory, pattern recognition,and time-series analysis. The use of the SVD in numerical computations first became practical with the development of the effcient and stable QRSVD algorithm by Golub and Reinsch [5O7,1971]).

Theorem 1.2.5 (The Singular Value Decomposition). For any matrix $A \in \mathbb { C } ^ { m \times n }$ of rank $r$ there exist unitary matrices $U = ( u _ { 1 } , \dots , u _ { m } ) \in \mathbb { C } ^ { m \times m }$ and $V = ( v _ { 1 } , \ldots , v _ { n } ) \in \mathbb { C } ^ { n \times n }$ such that

$$
\boldsymbol { A } = \boldsymbol { U } \boldsymbol { \Sigma } \boldsymbol { V } ^ { H } = \boldsymbol { U } \left( \begin{array} { c c } { \boldsymbol { \Sigma } _ { 1 } } & { \boldsymbol { 0 } } \\ { \boldsymbol { 0 } } & { \boldsymbol { 0 } } \end{array} \right) \boldsymbol { V } ^ { H } ,
$$

where $\Sigma _ { 1 } = \operatorname { d i a g } \left( \sigma _ { 1 } , \sigma _ { 2 } , \ldots , \sigma _ { r } \right) \in \mathbb { R } ^ { r \times r }$ The $\sigma _ { i }$ are the singular values of $A$ ,and $u _ { i } \in \mathbb { C } ^ { m }$ and $v _ { i } \in \mathbb { C } ^ { n }$ are the left and right singular vectors. In the following we assume that the singular values are ordered so that

$$
\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { r } > 0 .
$$

Proof. We give an inductive proof that constructs the SVD from its largest singular value $\sigma _ { 1 }$ and the associated left and right singular vectors. Let $v _ { 1 } \in \mathbb { C } ^ { n }$ with $\| v _ { 1 } \| _ { 2 } = 1$ be a unit vector such that

$$
\| A v _ { 1 } \| _ { 2 } = \| A \| _ { 2 } = \sigma _ { 1 } ,
$$

where $\sigma _ { 1 }$ is real and positive. The existence of such a vector follows from the definition of a subordinate matrix norm $\| A \|$ If $\sigma _ { 1 } = 0$ ，then $A = 0$ ，and(1.2.11） holds with $\Sigma = 0$ and arbitrary unitary matrices $U$ and $V$ .If $\sigma _ { 1 } > 0$ ,set $u _ { 1 } = ( 1 / \sigma _ { 1 } ) A v _ { 1 } \in \mathbb { C } ^ { m }$ ,and let

$$
\begin{array} { r } { V = ( v _ { 1 } \quad V _ { 1 } ) \in \mathbb { C } ^ { n \times n } , \quad U = ( u _ { 1 } \quad U _ { 1 } ) \in \mathbb { C } ^ { m \times m } } \end{array}
$$

be unitary matrices. (Recall that it is always possible to extend a unitary set of vectors to a unitary basis for the whole space.) Since $U _ { 1 } ^ { H } A v _ { 1 } = \sigma U _ { 1 } ^ { H } u _ { 1 } = 0$ , it follows that $U ^ { H } A V$ has the structure

$$
\begin{array} { r } { A _ { 1 } \equiv U ^ { H } A V = \left( \begin{array} { c c } { \sigma _ { 1 } } & { w ^ { H } } \\ { 0 } & { B } \end{array} \right) , } \end{array}
$$

where $w ^ { H } = u _ { 1 } ^ { H } A V _ { 1 }$ and $B = U _ { 1 } ^ { H } A V _ { 1 } \in \mathbb { C } ^ { ( m - 1 ) \times ( n - 1 ) }$

From the two inequalities

$$
\| A _ { 1 } \| _ { 2 } ( \sigma _ { 1 } ^ { 2 } + w ^ { H } w ) ^ { 1 / 2 } \geq \left\| A _ { 1 } \left( { \sigma _ { 1 } ^ { \sigma _ { 1 } } } \right) \right\| _ { 2 } = \left\| \left( { \sigma ^ { 2 } } + w ^ { H } w \right) \right\| _ { 2 } \geq \sigma _ { 1 } ^ { 2 } + w ^ { H } w
$$

it follows that $\| A _ { 1 } \| _ { 2 } \ge ( \sigma _ { 1 } ^ { 2 } + w ^ { H } w ) ^ { 1 / 2 }$ .But $U$ and $V$ are unitary and $\| A _ { 1 } \| _ { 2 } = \| A \| _ { 2 } = \sigma _ { 1 }$ Hence $w = 0$ , and the proof can now be completed by an induction argument on the smallest dimension $\operatorname* { m i n } ( m , n )$ □

Instead of the full SVD (1.2.11), it often suffices to consider the compact or economy size SVD,

$$
\boldsymbol { A } = U _ { 1 } \boldsymbol { \Sigma _ { 1 } } V _ { 1 } ^ { H } = \sum _ { i = 1 } ^ { r } \sigma _ { i } u _ { i } \boldsymbol { v } _ { i } ^ { H } ,
$$

where $U _ { 1 } = \mathbb { C } ^ { m \times r }$ and $V _ { 1 } = \mathbb { C } ^ { n \times r }$ are the singular vectors corresponding to nonzero singular values. If $A$ has full column rank, then $V _ { 1 } = V$ .Similarly, if $A$ has full row rank, then $U _ { 1 } = U$ . By (1.2.12), $A$ is decomposed into a sum of $r$ rank-one matrices.

Like the eigenvalues of a real Hermitian matrix, the singular values have a min-max characterization.

Theorem 1.2.6. Let $A \in \mathbb { C } ^ { m \times n }$ have singular values $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { p } \geq 0 ,$ $p = \operatorname* { m i n } ( m , n )$ and let $s$ be a linear subspace of $\mathbb { C } ^ { n }$ . Then

$$
\sigma _ { i } = \operatorname* { m i n } _ { \dim \left( S \right) = n - i + 1 } \operatorname* { m a x } _ { x \in S \atop x \neq 0 } \frac { \| A x \| _ { 2 } } { \| x \| _ { 2 } } .
$$

Proof. The result is established similarly to the characterization of the eigenvalues of a symmetric matrix in the Courant-Fischer theorem; see Horn and Johnson [641, 2012]. □

If $A \in \mathbb { C } ^ { m \times n }$ represents a linear mapping from $\mathbb { C } ^ { n }$ t0 $\mathbb { C } ^ { m }$ , the significance of Theorem 1.2.5 is that there exists a unitary basis in each of these spaces, with respect to which this mapping is represented by a generalized diagonal matrix $\Sigma$ with real nonnegative elements.

The singular values of $A$ are uniquely determined. The singular vectors $u _ { i }$ and $v _ { i }$ corresponding to a singular value $\sigma _ { i }$ are unique if and only if $\sigma _ { i }$ is simple. To a singular value $\sigma _ { i }$ of multiplicity $p > 1$ there correspond $p$ singular vectors that can be chosen as any unitary basis for the unique subspace that they span. The SVD gives unitary bases for the four fundamental subspaces associated with $A$ . It is easy to verify that

$$
\begin{array} { r l } { \mathcal { R } ( \boldsymbol { A } ) = \mathrm { s p a n } \{ u _ { 1 } , \ldots , u _ { r } \} , \quad } & { \mathcal { N } ( \boldsymbol { A } ) = \mathrm { s p a n } \{ v _ { r + 1 } , \ldots , v _ { n } \} , } \\ { \mathcal { R } ( \boldsymbol { A } ^ { H } ) = \mathrm { s p a n } \{ v _ { 1 } , \ldots , v _ { r } \} , \quad } & { \mathcal { N } ( \boldsymbol { A } ^ { H } ) = \mathrm { s p a n } \{ u _ { r + 1 } , \ldots , u _ { m } \} . } \end{array}
$$

Note that $\mathcal { N } ( A ^ { H } )$ is the unitary complement in $\mathbb { C } ^ { m }$ of $\mathcal { R } ( A )$ ,and ${ \mathcal { N } } ( A )$ is the unitary complement of $\mathcal { R } ( A ^ { H } )$ in $\mathbb { C } ^ { n }$ ：

$$
{ \mathcal { N } } ( A ) ^ { \perp } = { \mathcal { R } } ( A ^ { H } ) , \qquad { \mathcal { R } } ( A ) ^ { \perp } = { \mathcal { N } } ( A ^ { H } ) .
$$

Once a singular vector $v _ { i }$ or $u _ { i }$ corresponding to a simple singular value $\sigma _ { i } > 0$ has been determined, $u _ { i }$ or $v _ { i }$ is uniquely determined from

$$
\sigma _ { j } u _ { j } = A v _ { j } , \qquad \sigma _ { j } v _ { j } = A ^ { H } u _ { j } .
$$

There is a close relationship between the SVD and the Hermitian (or real symmetric) eigenvalue problems for $A ^ { H } A$ and $A A ^ { H }$ .If $A = U \Sigma V ^ { H } \in \mathbb { C } ^ { m \times n }$ is the SVD, then these eigenvalue decompositions are

$$
A ^ { H } A = V \Sigma ^ { T } \Sigma V ^ { H } , \qquad A A ^ { H } = U \Sigma ^ { T } \Sigma U ^ { H } .
$$

It follows that the singular values $\sigma _ { i }$ are the nonnegative square roots of the eigenvalues of $A ^ { H } A$ and $A A ^ { H }$

The Hermitian matrix

$$
\begin{array} { r } { C = \left( \begin{array} { c c } { 0 } & { A } \\ { A ^ { H } } & { 0 } \end{array} \right) , \quad A \in \mathbb { C } ^ { m \times n } , } \end{array}
$$

is often referred to as the Jordan-Wielandt matrix.The following theorem is implicit in Jordan's derivation of the SVD [676, $\mathbf { 1 8 7 4 } ]$ ·

Theorem 1.2.7 (Jordan-Wielandt). Let $A \in \mathbb { C } ^ { m \times n }$ ， $m \geq n$ , be a matrix of rank $r$ ,and let its SVD be $A = U \Sigma V ^ { H }$ ,where Σ= diag (£1 0), $U = \left( U _ { 1 } \quad U _ { 2 } \right)$ ,and $V = \left( \begin{array} { l l } { V _ { 1 } } & { V _ { 2 } } \end{array} \right)$ . Then

$$
C = \left( \begin{array} { c c } { { 0 } } & { { A } } \\ { { A ^ { H } } } & { { 0 } } \end{array} \right) = P \left( \begin{array} { c c c } { { \Sigma _ { 1 } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - \Sigma _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) P ^ { H } ,
$$

where $P$ is the unitary matrix

$$
P = \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c c c } { { U _ { 1 } } } & { { U _ { 1 } } } & { { \sqrt { 2 } U _ { 2 } } } & { { 0 } } \\ { { V _ { 1 } } } & { { - V _ { 1 } } } & { { 0 } } & { { \sqrt { 2 } V _ { 2 } } } \end{array} \right) ^ { H } .
$$

The eigenvalues of $C$ are $\pm \sigma _ { i }$ ， $i = 1 , \dots , r$ , and zero is repeated $( m + n - 2 r )$ times.

The use of $C$ for computing the SVD of $A$ was pioneered by Lanczos [717,1958], [714, $1 9 6 1$ , Chap. 3]. Note that the matrix

$$
C ^ { 2 } = \left( \begin{array} { c c } { { A A ^ { H } } } & { { 0 } } \\ { { 0 } } & { { A ^ { H } A } } \end{array} \right)
$$

has block diagonal form. Such a matrix is said to be two-cyclic.

The following example illustrates that explicitly forming $A ^ { H } A$ (or $A A ^ { H }$ ) can lead to a severe loss of accuracy in the smaller singular values.

Example 1.2.8. Let $A = \left( u _ { 1 } , u _ { 2 } \right)$ ，where $u _ { 1 }$ and $u _ { 2 }$ are unit vectors such that $0 < u _ { 1 } ^ { T } u _ { 2 } =$ $\cos \gamma$ ,where $\gamma$ is the angle between the vectors $u _ { 1 }$ and $u _ { 2 }$ . The eigenvalues of the matrix

$$
A ^ { T } A = \binom { 1 } { \cos \gamma } \quad \cos \gamma \nonumber
$$

are the roots of the equation $( \lambda - 1 ) ^ { 2 } = \cos ^ { 2 } \gamma$ and equal $\lambda _ { 1 } = 2 \cos ^ { 2 } ( \gamma / 2 )$ ， $\lambda _ { 2 } = 2 \sin ^ { 2 } ( \gamma / 2 )$ Hence the singular values of $A$ are

$$
\sigma _ { 1 } = { \sqrt 2 } \cos ( \gamma / 2 ) , \qquad \sigma _ { 2 } = { \sqrt 2 } \sin ( \gamma / 2 ) .
$$

The right singular vectors of $A$ are the eigenvectors of $A ^ { T } A$ ，

$$
v _ { 1 } = { \frac { 1 } { \sqrt { 2 } } } \left( { 1 \atop 1 } \right) , \qquad v _ { 2 } = { \frac { 1 } { \sqrt { 2 } } } \left( { - 1 \atop 1 } \right) .
$$

The left singular vectors can be determined from (1.2.16). However, if $\gamma$ is less than the square root of the unit roundoff, then numerically $\cos \gamma \approx 1 \pm \gamma ^ { 2 } / 2 = 1$ . Then the computed eigenvalues of $A ^ { T } A$ are O and 2,i.e., the smallest singular value of $A$ has been lost! □

# Notes and references

Beltrami [98, $\mathrm { 1 8 7 3 ] }$ derived the SVD for a real, square, nonsingular matrix having distinct singular values.A year later, Jordan [676, $\mathbf { 1 8 7 4 } ]$ independently published a derivation of the SVD that handled multiple singular values and gave a variational characterization of the largest singular value as the maximum of a function. Picard [893,19o9] seems to have been the first to call the numbers $\sigma _ { i }$ singular values. Autonne [42,19i3] extended the SVD to complex matrices. The generalization to singular and rectangular matrices appeared in Autonne [43,1915]. More detailed accounts of the history of the SVD are given by Horn and Johnson [640,1991,Sect. 3.0] and Stewart [1026,1993].

# 1.2.3 - The Pseudoinverse and Generalized Inverses

By Theorem 1.1.10, for $A \in \mathbb { C } ^ { m \times n }$ of any dimension and rank, the unique least squares solution of minimum norm is characterized by $r = b - A x \perp \mathcal { R } ( A )$ ,and $x \perp { \mathcal { N } } ( A )$ . The full SVD

$A = U \Sigma V ^ { H }$ gives unitary bases for these two subspaces. Thus the SVD is a perfect tool for solving least squares problems.

Theorem 1.2.9. The least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| x \| _ { 2 } , \quad S = \{ x \in \mathbb { R } ^ { n } \mid \| b - A x \| _ { 2 } = \operatorname* { m i n } \} ,
$$

has a unique solution that can be written as $x = A ^ { \dagger } b _ { \dagger }$ where

$$
\boldsymbol { A } ^ { \dagger } = \boldsymbol { V } \left( \begin{array} { c c } { \Sigma _ { 1 } ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) \boldsymbol { U } ^ { H }
$$

is the pseudoinverse of $A$

Proof. Let $\begin{array} { r } { z = V ^ { H } x = \binom { z _ { 1 } } { z _ { 2 } } , c = U ^ { H } b = \binom { c _ { 1 } } { c _ { 2 } } } \end{array}$ where $z _ { 1 } , c _ { 1 } \in \mathbb { C } ^ { r }$ Then

$$
\begin{array}{c} \begin{array} { l } { \| b - A x \| _ { 2 } = \| U ^ { H } ( b - A V V ^ { H } x ) \| _ { 2 } } \\ { \qquad = \left\| \left( { \begin{array} { c c } { c _ { 1 } } \\ { c _ { 2 } } \end{array} } \right) - \left( { \begin{array} { c c } { \Sigma _ { 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} } \right) \left( { \begin{array} { c } { z _ { 1 } } \\ { z _ { 2 } } \end{array} } \right) \right\| _ { 2 } = \left\| \left( { \begin{array} { c } { c _ { 1 } - \Sigma _ { 1 } z _ { 1 } } \\ { c _ { 2 } } \end{array} } \right) \right\| _ { 2 } . } \end{array}  \end{array}
$$

Thus,the residual norm will be minimized for $z _ { 1 } = \Sigma _ { 1 } ^ { - 1 } c _ { 1 }$ and any $z _ { 2 }$ .The choice $z _ { 2 } = 0$ minimizes $\left. z \right. _ { 2 }$ ,and gives $\| x \| _ { 2 } = \| V z \| _ { 2 }$ □

The pseudoinverse was introduced by Moore and rediscovered by Penrose [889,1955l. The pseudoinverse is therefore also called the Moore-Penrose inverse. Penrose gave it an elegant algebraic characterization.

Theorem 1.2.10 (The Penrose Conditions). The pseudoinverse $X$ is uniquely determined by the following four conditions:

$$
\begin{array} { l l } { { A X A = A , \qquad } } & { { ( 2 ) \quad X A X = X , } } \\ { { ( A X ) ^ { H } = A X , \qquad } } & { { ( 4 ) \quad ( X A ) ^ { H } = X A . } } \end{array}
$$

It is easily verified that $A ^ { \dagger }$ in (1.2.22) satisfies the Penrose conditions.By the uniqueness ol $A ^ { \dagger }$ ,this does not depend on the particular choice of $U$ and $V$ in the SVD. It follows easily from Theorem 1.2.9 that $A ^ { \dagger }$ minimizes $\| A X - I \| _ { F }$

If $A$ is nonsingular, then $A ^ { \dagger } = A ^ { - 1 }$ ,so (1.2.22) is a generalization of the usual inverse. From the SVD it easily follows that

$$
A ^ { \dagger } = ( A ^ { H } A ) ^ { \dagger } A ^ { H } = A ^ { H } ( A A ^ { H } ) ^ { \dagger } .
$$

In the special case that $\operatorname { r a n k } ( A ) = n$ ,we have

$$
A ^ { \dagger } = ( A ^ { H } A ) ^ { - 1 } A ^ { H } , \qquad ( A ^ { H } ) ^ { \dagger } = A ( A ^ { H } A ) ^ { - 1 } .
$$

The pseudoinverse of a scalar is

$$
\sigma ^ { \dagger } = { \left\{ \begin{array} { l l } { 1 / \sigma } & { { \mathrm { i f ~ } } \sigma \neq 0 , } \\ { 0 } & { { \mathrm { i f ~ } } \sigma = 0 . } \end{array} \right. }
$$

This shows the important fact that the pseudoinverse $A ^ { \dagger }$ is not a continuous function of $A$ ,unless we allow only perturbations that do not change the rank of $A$ . The pseudoinverse has the property

$$
A ^ { \dagger } = \operatorname* { l i m } _ { \delta  0 } ( A ^ { H } A + \delta I ) ^ { - 1 } A ^ { H } .
$$

The following properties of the pseudoinverse follow from (1.2.22).

1. $( A ^ { \dagger } ) ^ { \dagger } = A$ ；   
2. $( A ^ { \dagger } ) ^ { H } = ( A ^ { H } ) ^ { \dagger }$ ；   
3. $( \alpha A ) ^ { \dagger } = \alpha ^ { \dagger } A ^ { \dagger }$ ；   
4. $( A ^ { H } A ) ^ { \dagger } = A ^ { \dagger } ( A ^ { \dagger } ) ^ { H }$   
5.if $U$ and $V$ are unitary, $( U A V ^ { H } ) ^ { \dagger } = V A ^ { \dagger } U ^ { H }$ ；   
6.if $A = \textstyle \sum _ { i } A _ { i } ,$ where $A _ { i } A _ { j } ^ { H } = 0 , A _ { i } ^ { H } A _ { j } = 0 , i \neq j ,$ then $\begin{array} { r } { A ^ { \dagger } = \sum _ { i } A _ { i } ^ { \dagger } } \end{array}$ ；   
7. if A is normal ( $\mathbf { \bar { \Psi } } A A ^ { H } = A ^ { H } A ^ { \prime }$ ),then $A ^ { \dagger } A = A A ^ { \dagger }$ and $( A ^ { n } ) ^ { \dagger } = ( A ^ { \dagger } ) ^ { n }$ ：   
8.A, $A ^ { H } , A ^ { \dagger }$ ,and $A ^ { \dagger } A$ all have rank equal to trace $( A ^ { \dagger } A )$

For the pseudoinverse, the relations and $A A ^ { \dagger } = A ^ { \dagger } A$ and $( A B ) ^ { \dag } = B ^ { \dag } A ^ { \dag }$ are not in general true. For example, let $A = \left( \begin{array} { l l } { 1 } & { 0 } \end{array} \right)$ and $B = \left( \begin{array} { l l } { 1 } & { 1 } \end{array} \right) ^ { T }$ . Then $A B = 1$ ,but

$$
B ^ { \dagger } A ^ { \dagger } = \frac { 1 } { 2 } \left( \begin{array} { l l } { 1 } & { 1 } \end{array} \right) \left( \begin{array} { l } { 1 } \\ { 0 } \end{array} \right) = \frac { 1 } { 2 } .
$$

Necessary and sufficient conditions for the identity $( A B ) ^ { \dag } = B ^ { \dag } A ^ { \dag }$ to hold have been given by Greville [536,1966]. The following theorem gives an important sufficient condition.

Theorem 1.2.11. If $A \in \mathbb { C } ^ { m \times p }$ ， $B \in \mathbb { C } ^ { p \times n }$ ,and $\operatorname { r a n k } ( A ) = \operatorname { r a n k } ( B ) = p ,$ then

$$
( A B ) ^ { \dagger } = B ^ { \dagger } A ^ { \dagger } = B ^ { H } ( B B ^ { H } ) ^ { - 1 } ( A ^ { H } A ) ^ { - 1 } A ^ { H } .
$$

Proof. The last equality follows from (1.2.25). The first equality is verified by showing that the four Penrose conditions are satisfied. □

The pseudoinverse and the singular vectors of $A$ give simple expressions for orthogonal pro-jections onto the four fundamental subspaces of $A$ . The following expressions are easily verified using the Penrose conditions and the SVD:

$$
\begin{array} { r l } { { P _ { \mathcal { R } ( A ) } } = A A ^ { \dagger } = U _ { 1 } U _ { 1 } ^ { H } , \quad } & { { } P _ { \mathcal { N } ( A ^ { H } ) } = I - A A ^ { \dagger } = U _ { 2 } U _ { 2 } ^ { H } , } \\ { { P _ { \mathcal { R } ( A ^ { H } ) } } = A ^ { \dagger } A = V _ { 1 } V _ { 1 } ^ { H } , \quad } & { { } P _ { \mathcal { N } ( A ) } = I - A ^ { \dagger } A = V _ { 2 } V _ { 2 } ^ { H } , } \end{array}
$$

where $U _ { 1 } = ( u _ { 1 } , \ldots , u _ { r } )$ and $V _ { 1 } = ( v _ { 1 } , \ldots , v _ { r } )$ . From this we get the following expression for the inverse of the augmented system matrix when $A$ has full column rank:

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { H } } } & { { 0 } } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { { I - A A ^ { \dagger } } } & { { ( A ^ { \dagger } ) ^ { T } } } \\ { { A ^ { \dagger } } } & { { - ( A ^ { H } A ) ^ { - 1 } } } \end{array} \right) .
$$

If only some of the four Penrose conditions hold, the corresponding matrix is called a generalized inverse. Such inverses have been extensively analyzed; see Nashed [823,1976]. Any matrix $A ^ { - }$ satisfying the first Penrose condition $A A ^ { - } A = A$ is called an inner inverse or $\{ 1 \}$ inverse.If it satisfies the second condition $A ^ { - } A A ^ { - } = A ^ { - }$ , it is called an outer inverse or a $\{ 2 \}$ -inverse.

Let $A ^ { - }$ be a $\{ 1 \}$ -inverse of $A$ . Then for all $b$ such that the system $A x = b$ is consistent, $x = A ^ { - } b$ is a solution. The general solution can be written

$$
\begin{array} { r } { x = A ^ { - } b + ( I - A ^ { - } A ) y , \quad y \in \mathbb { C } ^ { n } . } \end{array}
$$

For any $\{ 1 \}$ -inverse of $A$ , it holds that

$$
( A A ^ { - } ) ^ { 2 } = A A ^ { - } A A ^ { - } = A A ^ { - } , \qquad ( A ^ { - } A ) ^ { 2 } = A ^ { - } A A ^ { - } A = A ^ { - } A .
$$

This shows that $A A ^ { - }$ and $A ^ { - } A$ are idempotent and therefore (in general, oblique) projectors; see Section 3.1.4. The residual norm $\| A x - b \| _ { 2 }$ is minimized when $x$ satisfies the normal equations $A ^ { H } A x = A ^ { H } b$ .Suppose that a $\{ 1 \}$ -inverse $A ^ { - }$ also satisfies the third Penrose condition

$$
( A A ^ { - } ) ^ { H } = A A ^ { - } .
$$

Then $A A ^ { - }$ is the orthogonal projector onto $\mathcal { R } ( A )$ and $A ^ { - }$ is called a least squares inverse. We have

$$
A ^ { H } = ( A A ^ { - } A ) ^ { H } = A ^ { H } A A ^ { - } ,
$$

which shows that $x = A ^ { - } b$ satisfies the normal equations and therefore is a least squares solution.

The following dual result also holds.If $A ^ { - }$ is a generalized inverse and $( A ^ { - } A ) ^ { H } = A ^ { - } A$ ， then $A ^ { - } A$ is the orthogonal projector onto ${ \mathcal { N } } ( A )$ ，and $A ^ { - }$ is called a least-norm inverse. If $A x = b$ is consistent, the unique solution for which $\| x \| _ { 2 }$ is smallest satisfies the normal equations of the second kind,

$$
x = A ^ { H } z , \quad A A ^ { H } z = b .
$$

For a least-norm inverse $A ^ { - }$ it holds that

$$
A ^ { H } = ( A A ^ { - } A ) ^ { H } = A ^ { - } A A ^ { H } .
$$

Hence, $x = A ^ { H } z = A ^ { - } ( A A ^ { H } ) z = A ^ { - } b$ ,which shows that $x = A ^ { - } b$ is the solution of smallest norm. Conversely, let $A ^ { - }$ be such that, whenever $A x = b$ has a solution, $x = A ^ { - } b$ is a least-norm solution. Then $A ^ { - }$ is a least-norm inverse.

Finally,a warning: Manipulations with generalized inverses can hide intrinsic computational difficulties associated with nearly rank-deficient matrices and should be used with caution.

# Notes and references

The notion of inverse of a matrix was generalized to include all matrices $A$ ， singular as well as rectangular, by E.H. Moore [804,192o]. Moore called this the“general reciprocal.” His contribution used unnecessarily complicated notation and was soon sinking into oblivion; see Ben-Israel [100,2oo2]. A collection of papers on generalized inverses can be found in Nashed [823, 1976]. Ben-Israel and Greville [1O1, 2oo3l give a comprehensive survey of generalized inverses.

# 1.2.4 - Principal Angles and the CS Decomposition

The acute angle between two unit vectors $x$ ， $y \in \mathbb { C } ^ { n }$ is

$$
\theta = \angle ( x , y ) = \operatorname { a r c c o s } | x ^ { H } y | , \quad 0 \leq \theta \leq \pi / 2 .
$$

The general concept of principal angles between any two subspaces of $\mathbb { C } ^ { n }$ goes back to a remarkable paper by Jordan [677,1875].

Definition 1.2.12. Let $\mathcal { X } = \mathcal { R } ( X )$ and $\mathcal { V } = \mathcal { R } ( Y )$ be two subspaces of $\mathbb { C } ^ { n }$ .Without restriction we can assume that

$$
p = \dim \left( { \mathcal { X } } \right) \geq \dim \left( { \mathcal { Y } } \right) = q \geq 1 .
$$

The principal angles $\theta _ { k }$ between $\mathcal { X }$ and $\mathcal { V }$ and the corresponding principal vectors $u _ { k }$ ， $v _ { k }$ ， $k =$ $1 , \ldots , q$ ，are recursively defined by

$$
\cos \theta _ { k } = \operatorname* { m a x } _ { u \in \mathcal { X } } \operatorname* { m a x } _ { v \in \mathcal { Y } } u ^ { H } v , \quad \| u \| _ { 2 } = \| v \| _ { 2 } = 1 ,
$$

subject to the constraints $u \perp u _ { j } , v \perp v _ { j } , j = 1 , \perp . . . , k - 1 .$

Note that for $k = 1$ , the constraints are empty, and $\theta _ { 1 }$ is the smallest principal angle between $\mathcal { X }$ and $\mathcal { V }$ . The principal vectors need not be uniquely defined, but the principal angles always should be.

From the min-max characterization of the singular values and vectors given in Theorem 1.2.6 follows a relationship between principal angles and the SVD.

Theorem 1.2.13. Assume that $\ b X \in \mathbb { C } ^ { m \times p }$ and $Y \in \mathbb { C } ^ { m \times q }$ form unitary bases for two subspaces $\mathcal { X }$ and $\mathcal { V }$ .Consider the SVD

$$
\begin{array} { r } { M = { X } ^ { H } { Y } = { W C Z } ^ { H } , \quad { C } = \mathrm { d i a g } \left( \boldsymbol { \sigma } _ { 1 } , \ldots , \boldsymbol { \sigma } _ { q } \right) , } \end{array}
$$

where $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { q }$ ， $W ^ { H } W = Z ^ { H } Z = I _ { q }$ . Then the principal angles $\theta _ { k }$ and principal vectors are given by

$$
\cos \theta _ { k } = \sigma _ { k } , \quad U = X W , \quad V = Y Z .
$$

Using this result, Bjorck and Golub [144,1973l give stable algorithms for computing the principal angles and vectors between subspaces. Golub and Zha [515,1994], [516,1995] give a detailed perturbation analysis,discuss equivalent characterizations of principal angles,and present algorithms for large and structured matrices. The stability of the Bjorck-Golub algorithm is proved by Drma [334, 2000].

The principal angles can be used to determine when two subspaces $\mathcal { X }$ and $\mathcal { V }$ are close to each other. $\mathcal { X }$ and $\mathcal { V }$ are identical if and only if all principal angles are zero.

Definition 1.2.14. The largest principal angle $\theta _ { \mathrm { m a x } }$ between two subspaces $\mathcal { X }$ and $\mathcal { V }$ of the same dimension is a measure of the distance between them:

$$
\mathrm { d i s t } ( \mathcal { X } , \mathcal { Y } ) = | \sin \theta _ { \mathrm { { m a x } } } ( \mathcal { X } , \mathcal { Y } ) | .
$$

An alternative definition is $\mathrm { d i s t } ( \mathcal { X } , \mathcal { Y } ) = \| P _ { \mathcal { X } } - P _ { \mathcal { Y } } \| _ { 2 }$ ,where $P _ { \mathcal { X } }$ and $P _ { \mathcal { y } }$ are the orthogonal projectors onto the subspaces $\mathcal { X }$ and $\mathcal { V }$ of $\mathbb { C } ^ { n }$ . This follows from the result that the nonzero singular values of $\left( P _ { \mathcal { X } } - P _ { \mathcal { Y } } \right)$ are

$$
\sin \theta _ { k } ( \mathcal { X } , \mathcal { Y } ) , \quad k = 1 , \dots , q ;
$$

see Golub and Van Loan [512,1996,Theorem 2.6.1].

Let $Q \in \mathbb { C } ^ { m \times n }$ ， $m > n$ , be unitary and partitioned as

$$
\begin{array} { r } { Q = \left( \begin{array} { l } { Q _ { 1 1 } } \\ { Q _ { 2 1 } } \end{array} \right) , \quad Q _ { 1 1 } \in \mathbb { R } ^ { m _ { 1 } \times n } , \quad Q _ { 2 1 } \in \mathbb { R } ^ { m _ { 2 } \times n } , } \end{array}
$$

where $m _ { 1 } + m _ { 2 } = m$ .Then the SVD of the blocks $Q _ { 1 1 }$ and $Q _ { 2 1 }$ are closely related. To simplify the discussion, we assume that both $Q _ { 1 1 }$ and $Q _ { 2 1 }$ are square, i.e., $m _ { 1 } = m _ { 2 } = n$ and $Q _ { 1 1 }$ is nonsingular. Let

$$
Q _ { 1 1 } = U _ { 1 } C V _ { 1 } ^ { H } , \quad C = \operatorname { d i a g } \left( c _ { 1 } , \dots , c _ { n } \right)
$$

be the SVD of $Q _ { 1 1 }$ , and set $X = Q _ { 2 1 } V _ { 1 }$ . Then $V _ { 1 } ^ { H } Q _ { 1 1 } ^ { H } Q _ { 1 1 } V _ { 1 } = C ^ { 2 }$ , and because $Q _ { 1 1 } ^ { H } Q _ { 1 1 } +$ $Q _ { 2 1 } ^ { H } Q _ { 2 1 } = I _ { n }$ , the columns of $X$ are orthogonal as follows:

$$
X ^ { H } X = V _ { 1 } ^ { H } Q _ { 2 1 } ^ { H } Q _ { 2 1 } V _ { 1 } = V _ { 1 } ^ { H } ( I - C ^ { 2 } ) V _ { 1 } = I - C ^ { 2 } .
$$

Then $U _ { 2 } = X S ^ { - 1 }$ ,where ${ \cal S } = \mathrm { d i a g } \left( s _ { 1 } , \ldots , s _ { n } \right)$ , is orthonormal, and $Q _ { 2 1 } = U _ { 2 } S V _ { 1 } ^ { H }$ .Thus, we have the CS decomposition

$$
\binom { Q _ { 1 1 } } { Q _ { 2 1 } } = \binom { U _ { 1 } } { 0 } \binom { 0 } { U _ { 2 } } \binom { C } { S } \binom { V _ { 1 } ^ { H } } { 0 } \binom { 0 } { V _ { 2 } ^ { H } } .
$$

A more general CS decomposition for a unitary matrix, where $Q _ { 1 1 }$ and $Q _ { 2 1 }$ are not required to be square matrices, is given by Paige and Saunders [856, 1981].

Theorem 1.2.15 (CS Decomposition). For an arbitrary partitioning of a square unitary matrix Q ∈Cmxm,

$$
Q = { \frac { m _ { 1 } } { m _ { 2 } } } { \binom { n _ { 1 } } { Q _ { 2 1 } } } \quad Q _ { 2 2 } \qquad 
$$

$n _ { 1 } + n _ { 2 } = m _ { 1 } + m _ { 2 } = m$ ，there are unitary matrices $U _ { 1 } , U _ { 2 } , V _ { 1 } , V _ { 2 }$ such that

$$
\left( { \begin{array} { c c } { U _ { 1 } ^ { H } } & { 0 } \\ { 0 } & { U _ { 2 } ^ { H } } \end{array} } \right) \left( { \begin{array} { c c } { Q _ { 1 1 } } & { Q _ { 1 2 } } \\ { Q _ { 2 1 } } & { Q _ { 2 2 } } \end{array} } \right) \left( { \begin{array} { c c } { V _ { 1 } } & { 0 } \\ { 0 } & { V _ { 2 } } \end{array} } \right) = \left( { \begin{array} { c c } { D _ { 1 1 } } & { D _ { 1 2 } } \\ { D _ { 2 1 } } & { D _ { 2 2 } } \end{array} } \right) ,
$$

where $D _ { i j } = U _ { i } ^ { H } Q _ { i j } V _ { j } \in \mathbb { R } ^ { n _ { i } \times m _ { j } } , i , j = 1 , 2 ,$ are real and diagonal matrices,

$$
\begin{array}{c} \left( { \cal D } _ { 1 1 } { \cal D } _ { 1 2 } \right) = \left( \frac { I { \cal \mathrm { \Lambda } } } { { \cal O } _ { s } } { \cal O } _ { c } \frac { \Bigg | { \cal O } _ { s } ^ { H } } { { \cal D } _ { \cal S } } { \cal S } \right. ~ { \cal I } ~  \\ { \left. { \cal D } _ { 2 1 } { \cal D } _ { 2 2 } \right) = \left( \frac { I { \cal \mathrm { \Lambda } } } { { \cal O } _ { s } } { \cal S } _ { { \cal D } _ { { \cal I } } } \Bigg | ^ { \cal I } { \cal U } \right)} \\ { { \cal S } { \cal S } _ { { \cal I } } { \cal I } { \cal \mathrm { \Lambda } } } & { { - C } } \\ { { \cal D } _ { { \cal \mathrm { \Lambda } } } { \cal O } _ { { \cal L } } ^ { H } } \end{array}  ,
$$

$C = \operatorname { d i a g } \left( c _ { 1 } , \ldots , c _ { p } \right) , S = \operatorname { d i a g } \left( s _ { 1 } , \ldots , s _ { p } \right)$ ,and

$$
1 > c _ { 1 } \geq \cdots \geq c _ { r } > 0 , \qquad 0 < s _ { 1 } \leq \cdots \leq s _ { r } < 1 ,
$$

and $c _ { i } ^ { 2 } + s _ { i } ^ { 2 } = 1$ Here $O _ { c }$ and $O _ { s }$ are zero blocks or may be empty matrices having no rows or no columns. The unit matrices need not be equal and may not be present.

Proof. Paige and Wei [870,1994] note that $Q _ { i j } = U _ { i } C V _ { j } ^ { H }$ ， $i , j = 1 , 2$ , are essentially the SVDs of the four blocks in the partitioned unitary matrix $Q$ .Take $U _ { 1 }$ and $V _ { 1 }$ so that $Q _ { 1 1 } = U _ { 1 } D _ { 1 1 } V _ { 1 } ^ { H }$ is the SVD of $Q _ { 1 1 }$ . Hence, $D _ { 1 1 }$ is a nonnegative diagonal matrix with elements less than or equal to unity. Choose unitary $U _ { 2 }$ and $V _ { 2 }$ to make $U _ { 2 } ^ { H } Q _ { 2 1 } V _ { 1 }$ lower triangular and $U _ { 1 } ^ { H } Q _ { 1 2 } V _ { 2 }$ upper triangular with real nonnegative elements on their diagonals. Since the columns are orthonormal, $D _ { 2 1 }$ must have the stated form. The orthonormality of rows gives $D _ { 1 2 }$ ,except for the dimension of the zero block denoted $O _ { s } ^ { H }$ . Since each row and column has unit length, the last block column must have the form

$$
U _ { 2 } \left( Q _ { 2 2 } \right) V _ { 2 } ^ { H } = \left( \begin{array} { c c c } { { { \cal O } _ { 1 2 } } } & { { } } & { { } } \\ { { } } & { { S } } & { { } } \\ { { } } & { { } } & { { I } } \\ { { K } } & { { L } } & { { } } \\ { { M } } & { { N } } & { { } } \\ { { } } & { { } } & { { { \cal O } _ { 2 2 } } } \end{array} \right) .
$$

The orthogonality of the second and fourth blocks of columns shows that $S M = 0$ .Hence $M = 0$ because $S$ is nonsingular. Similarly, from the second and fourth blocks of rows, $L = 0$ Next, from the fifth and second blocks of rows, $S C + N S = 0$ and hence $N = - C$ .Then we see that $K K ^ { H } = I$ and $K ^ { H } K = I$ ，and they can be transformed into $I$ without altering the rest of $D$ .Finally, the unit matrices in the $( 1 , 1 )$ and $( 4 , 4 )$ blocks show that $O _ { 1 2 } = O _ { s } ^ { H }$ and $O _ { 2 2 } = O _ { c } ^ { H }$ □

As remarked by Stewart [1017,1977], the CS decomposition of a unitary matrix $Q$ "often enables one to obtain routine computational proofs of geometric theorems that would otherwise require considerable ingenuity to establish.” Some contexts need only the compact CS decompo-sition that corresponds to the first $k _ { 1 }$ columns $Q _ { 1 1 }$ and $Q _ { 2 1 }$ of $Q$ .The above proof is constructive, and $U _ { 1 } , V _ { 1 }$ ,and $C$ can be computed by a standard SVD algorithm. However, if some singular values $c _ { i }$ are close to 1, this is not a stable algorithm for computing $S$ and $U _ { 2 }$

# Notes and references

The canonical correlations $\cos \theta _ { k }$ , where $\theta _ { k }$ are the principal angles, were introduced by Hotelling [642,1936]. These are used in statistical modeling in a wide variety of applications,such as econometrics, psychology,and geodesy. The concept of principal angles is generalized to elliptic scalar products by Knyazev and Argentati [7O1, 2002].

The CS decomposition is implicit in the works by Davis and Kahan [288,197o] and Bjorck and Golub [144,1973]. An explicit form is put forward by Stewart [1017,1977]. Stable algorithms for computing the CS decomposition are given by Paige and Saunders 856,1981], Stewart [1020,1982],and Van Loan [1080,1985]. Higham [624,2003] gives an analogue of the CS decomposition for pseudounitary matrices. Sutton [1052, 2oo9] gives a two-phase algorithm for computing the full CS decomposition. Applications are surveyed by Paige and Wei [870, 1994].

# 1.3 - Perturbation Analysis

# 1.3.1 - Vector and Matrix Norms

A norm is a function of a vector or matrix that gives a measure of its magnitude. Such norms can be regarded as generalizations of the absolute value for scalars and are useful for error analysis and other purposes.The Euclidean length of a vector is an example,but it is not the most convenient in all situations.

A vector norm is a function $\| \cdot \| : \mathbb { C } ^ { n } \to \mathbb { R }$ that satisfies the following conditions:

1. $\| x \| > 0 \quad \forall x \in \mathbb { C } ^ { n } , \quad x \neq 0$ (definiteness);   
2. $\| \alpha x \| = | \alpha | \| x \| \quad \forall \alpha \in \mathbb { C } , \quad x \in \mathbb { C } ^ { n }$ (homogeneity);   
3. $\begin{array} { r l } { \| x + y \| \leq \| x \| + \| y \| } & { { } \forall x , y \in \mathbb { C } ^ { n } } \end{array}$ (triangle inequality).

The most common vector norms are the Holder $\ell _ { p }$ -norms

$$
\| x \| _ { p } = \left( | x _ { 1 } | ^ { p } + | x _ { 2 } | ^ { p } + \cdot \cdot \cdot + | x _ { n } | ^ { p } \right) ^ { 1 / p } , \quad 1 \leq p < \infty .
$$

These have the property $\| x \| _ { p } = \| | x | \| _ { p }$ , where $| x | = ( | x _ { 1 } | , \ldots , | x _ { n } | )$ . Such norms are said to be absolute. The most important particular cases are $p = 1 , 2$ and the limit when $p  \infty$ ，

$$
\begin{array} { r l } & { \| x \| _ { 1 } = | x _ { 1 } | + \cdot \cdot \cdot + | x _ { n } | , } \\ & { \| x \| _ { 2 } = \left( | x _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { n } | ^ { 2 } \right) ^ { 1 / 2 } = \left( x ^ { H } x \right) ^ { 1 / 2 } , } \\ & { \| x \| _ { \infty } = \displaystyle \operatorname* { m a x } _ { 1 \leq i \leq n } | x _ { i } | . } \end{array}
$$

The vector $\ell _ { 2 }$ -norm is the Euclidean length of the vector.If $Q$ is unitary, then $\| Q x \| _ { 2 } ^ { 2 } =$ $x ^ { H } Q ^ { H } Q x \ : = \ : x ^ { H } x \ : = \ : \| x \| _ { 2 } ^ { 2 }$ ,i.e.,this norm is invariant under unitary transformations:On a finite-dimensional space,two norms differ by at most a positive constant that only depends on the dimension. For the vector $\ell _ { p }$ -norms,

$$
\begin{array} { r } { \| \ b { x } \| _ { p _ { 2 } } \leq \| \ b { x } \| _ { p _ { 1 } } \leq n ^ { \left( \frac { 1 } { p _ { 1 } } - \frac { 1 } { p _ { 2 } } \right) } \| \ b { x } \| _ { p _ { 2 } } , \quad p _ { 1 } \leq p _ { 2 } . } \end{array}
$$

An important property of $\ell _ { p }$ norms is the Holder inequality,

$$
| x ^ { H } y | \leq \| x \| _ { p } \| y \| _ { q } , \quad 1 / p + 1 / q = 1 .
$$

In the special case $p = q = 2$ this is the Cauchy-Schwarz inequality.

Definition 1.3.1. For any given vector norm $\| \cdot \| o n \mathbb { C } ^ { n }$ ， the dual norm $\| \cdot \| _ { D }$ is defined by

$$
\| x \| _ { D } = \operatorname* { m a x } _ { y \neq 0 } | x ^ { H } y | / \| y \| .
$$

The vectors in the set $\{ y \in \mathbb { C } ^ { n } \mid \| y \| _ { D } \| x \| = y ^ { H } x = 1 \}$ are said to be dual vectors to $x$ with respect to $\| \cdot \|$

From Holder's inequality it follows that the dual of the $\ell _ { p }$ -norm is the $\ell _ { q }$ -norm, where $1 / p +$ $1 / q = 1$ .Hence the dual of the $\ell _ { 2 }$ -norm is itself. It is the only norm with this property; see Horn and Johnson [641, 2012, Theorem 5.4.16].

A matrix norm is a function $\| \cdot \| : \mathbb { C } ^ { m \times n }  \mathbb { R }$ that satisfies analogues of the three properties of a vector norm. The matrix norm subordinate to a given vector norm is defined by

$$
\| A \| = \operatorname* { m a x } _ { x \neq 0 } { \frac { \| A x \| } { \| x \| } } = \operatorname* { m a x } _ { \| x \| = 1 } \| A x \| .
$$

From this it follows directly that

$$
\left\| A x \right\| \leq \left\| A \right\| \left\| x \right\| \quad \forall x \in \mathbb { C } ^ { n } .
$$

A subordinate matrix norm is submultiplicative,i.e.,whenever the product $A B$ is defined, the inequality $\| A B \| \leq \| A \| \| B \|$ holds.The matrix norms subordinate to the vector $\ell _ { p }$ -norms are especially important. For $p = 2$ it is given by the spectral norm

$$
\| A \| _ { 2 } = \operatorname* { m a x } _ { \| x \| _ { 2 } = 1 } \| A x \| _ { 2 } = \sigma _ { 1 } ( A ) ,
$$

where $\sigma _ { 1 } ( A )$ is the largest singular value of $A \in \mathbb { C } ^ { m \times n }$ . Because the nonzero singular values of $A$ and $A ^ { H }$ are the same, it follows that $\| A \| _ { 2 } = \| A ^ { H } \| _ { 2 }$

For $p = 1$ and $p = \infty$ it can be shown that the matrix subordinate norms are

$$
\| A \| _ { 1 } = \operatorname* { m a x } _ { 1 \leq j \leq n } \sum _ { i = 1 } ^ { m } | a _ { i j } | , \qquad \| A \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq m } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

If $e = ( 1 , \ldots , 1 ) ^ { T }$ is a vector of ones of appropriate dimension, we can write

$$
\| A \| _ { \infty } = \| | A | e \| _ { \infty } = \| A ^ { H } \| _ { 1 } .
$$

These norms are easily computable. A useful upper bound for the spectral norm, which is expensive to compute,is given by

$$
\| A \| _ { 2 } \leq ( \| A \| _ { 1 } \| A \| _ { \infty } ) ^ { 1 / 2 } .
$$

Another way to define matrix norms is to regard $\mathbb { C } ^ { m \times n }$ as an mn-dimensional vector space and apply a vector norm over that space.An example is the Frobenius norm derived from the vector $\ell _ { 2 }$ -norm,

$$
\| A \| _ { F } = \| A ^ { H } \| _ { F } = \left( \sum _ { i = 1 } ^ { m } \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) ^ { 1 / 2 } = \operatorname { t r a c e } \left( A ^ { H } A \right) ^ { 1 / 2 } .
$$

The Frobenius norm is submultiplicative but is often larger than necessary, e.g., $\| I \| _ { F } = n ^ { 1 / 2 }$ Lower and upper bounds for the matrix $\ell _ { 2 }$ -norm in terms of the Frobenius norm are

$$
{ \frac { 1 } { \sqrt { n } } } \| A \| _ { F } \leq \| A \| _ { 2 } \leq \| A \| _ { F } .
$$

The Frobenius norm and the matrix subordinate norms for $p = 1$ and $p = \infty$ satisfy $\| \left| A \right| \| =$ $\| A \|$ .However, for the $\ell _ { 2 }$ -norm, the best result is $\| | A | \| _ { 2 } ~ \le ~ n ^ { 1 / 2 } \| A \| _ { 2 }$ .The spectral and Frobenius norms of $A$ both can be expressed in terms of singular values $\sigma _ { i } ( A )$ as

$$
\| A \| _ { 2 } = \sigma _ { \operatorname* { m a x } } ( A ) , \qquad \| A \| _ { F } = \bigg ( \sum _ { i = 1 } ^ { r } \sigma _ { i } ^ { 2 } ( A ) \bigg ) ^ { 1 / 2 } , \quad r = \operatorname* { m i n } \{ m , n \} .
$$

Such norms are unitarily invariant, i.e., $\| A \| = \| U ^ { H } A V \|$ for any unitary $U$ and $V$ .The following characterization of such norms was given by von Neumann [1O94,1937l; see Stewart and Sun [1033, 1990].

Theorem 1.3.2. Any unitarily invariant matrix norm $\| A \|$ is a symmetric function of the singular values of $A$ ,i.e.,

$$
\| A \| = \Phi ( \sigma _ { 1 } , \ldots , \sigma _ { n } ) ,
$$

where $\Phi$ is invariant under permutation of its arguments.

Proof. Let the singular value decomposition of $A$ be $A = U \Sigma V ^ { H }$ .The invariance implies that $\| A \| = \| \Sigma \|$ , which shows that $\Phi ( A )$ only depends on $\Sigma$ . As the ordering of the singular values in $\Sigma$ is arbitrary, $\Phi$ must be symmetric in $\sigma _ { i }$ □

The converse of Theorem 1.3.2 was also proved by von Neumann,i.e.，any function $\Phi ( \sigma _ { 1 } , \ldots , \sigma _ { n } )$ that is symmetric in its arguments and satisfies the properties of a vector norm defines a unitarily invariant matrix norm. Such functions are called symmetric gauge functions.

An important class of unitarily invariant matrix norms is the so-called Schatten norms (Schatten [969,196o]) obtained by taking the $\ell _ { p }$ vector norm (1.3.1) of the vector of singular values $\sigma = ( \sigma _ { 1 } , \ldots , \sigma _ { n } )$ of $A$ ：

$$
\| A \| = \| \sigma \| _ { p } , \quad 1 \leq p < \infty .
$$

For $p = 2$ we get the Frobenius norm, and $p  \infty$ gives the spectral norm $\| A \| _ { 2 } = \sigma _ { 1 }$ . Taking $p = 1$ , we obtain the nuclear norm or Ky Fan norm (see Ky Fan [394,1949l)

$$
\| A \| _ { * } = \operatorname { t r a c e } { ( { \sqrt { A ^ { H } A } } ) } = \sum _ { i = 1 } ^ { n } \sigma _ { i } ( A ) .
$$

# 1.3.2 - Sensitivity of Singular Values and Vectors

By applying classical perturbation bounds for Hermitian matrices to the Jordan-Wielandt matrix (1.2.18), the following results for the sensitivity of the singular values and vectors of $A$ to perturbations can be derived; see Wedin [11O7,1972].

Theorem 1.3.3. Let $A \in \mathbb { R } ^ { m \times n }$ have the singular values $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { n }$ Then the singular values $\tilde { \sigma } _ { 1 } \geq \tilde { \sigma } _ { 2 } \geq \cdot \cdot \cdot \geq \tilde { \sigma } _ { n }$ of the perturbed matrix ${ \tilde { A } } = A + E$ ， $m \geq n$ ，satisfy

$$
| \sigma _ { i } - \tilde { \sigma } _ { i } | \leq \| E \| _ { 2 } , \qquad \mathrm { ( i i ) } \ : \ : \sum _ { i = 1 } ^ { n } | \sigma _ { i } - \tilde { \sigma } _ { i } | ^ { 2 } \leq \| E \| _ { F } ^ { 2 } .
$$

Proof. See Stewart [1015, 1973, Theorem 6.6].

The second inequality in (1.3.13) is known as the Wielandt-Hoffman theorem for singular values. The fact that a perturbation of $A$ will produce perturbations of the same or smaller magnitude in its singular values is important for the use of the SVD to determine the“numerical rank" of a matrix; see Section 1.3.3.

Theorem 1.3.4. Let $A \in \mathbb { R } ^ { m \times n }$ have a simple singular value $\sigma _ { i }$ with corresponding left and right singular vectors $u _ { i }$ and $v _ { i }$ .Let $\gamma _ { i } = \mathrm { m i n } _ { j \neq i } | \sigma _ { i } - \sigma _ { j } |$ be the absolute gap between $\sigma _ { i }$ and the other singular values of $A$ .Then, the perturbed matrix ${ \tilde { A } } = A + E$ ，where $\| E \| _ { 2 } < \gamma _ { i } ,$ has a singular value $\tilde { \sigma } _ { i }$ with singular vectors $\tilde { u } _ { i }$ and $\tilde { v } _ { i }$ that satisfy

$$
\operatorname* { m a x } \left( \sin \theta ( u _ { i } , \tilde { u } _ { i } ) , \sin \theta ( v _ { i } , \tilde { v } _ { i } ) \right) \leq \frac { \| E \| _ { 2 } } { \gamma _ { i } - \| E \| _ { 2 } } .
$$

It is well known that the eigenvalues of the leading principal minor of order $( n - 1 )$ of a Hermitian matrix $A \in \mathbb { R } ^ { n \times n }$ interlace the eigenvalues of $A$ .From the min-max characterization in Theorem 1.2.6,a similar result for the singular values follows.

Theorem 1.3.5. Let $A$ be bordered by a column $u \in \mathbb { R } ^ { m }$ ，

$$
{ \widehat { A } } = ( A \quad u ) \in \mathbb { R } ^ { m \times n } , \quad m \geq n .
$$

Then the ordered singular values $\sigma _ { i }$ of $A$ separate the ordered singular values $\hat { \sigma } _ { i }$ of $\hat { A }$

$$
\hat { \sigma } _ { 1 } \geq \sigma _ { 1 } \geq \hat { \sigma } _ { 2 } \geq \sigma _ { 2 } \geq \cdots \geq \hat { \sigma } _ { n - 1 } \geq \sigma _ { n - 1 } \geq \hat { \sigma } _ { n } .
$$

Simlary $A$ is borerd by w $\boldsymbol { v } ^ { T } \in \mathbb { R } ^ { n }$ $\widehat { A } = \left( \begin{array} { c } { A } \\ { v ^ { T } } \end{array} \right) \in \mathbb R ^ { m \times n }$ $m \geq n$

$$
\widehat { \sigma } _ { 1 } \geq \sigma _ { 1 } \geq \widehat { \sigma } _ { 2 } \geq \sigma _ { 2 } \geq \cdots \geq \widehat { \sigma } _ { n - 1 } \geq \sigma _ { n - 1 } \geq \widehat { \sigma } _ { n } \geq \sigma _ { n } .
$$

Lemma 1.3.6. Let $A \in \mathbb { C } ^ { m \times n }$ and $B _ { k } = X _ { k } Y _ { k } ^ { H }$ where $X _ { k } , Y _ { k } \in \mathbb { C } ^ { m \times k }$ Then $\mathrm { r a n k } ( B _ { k } ) \leq$ $k < \mathrm { m i n } \{ m , n \}$ and $\sigma _ { 1 } ( A - B _ { k } ) \geq \sigma _ { k + 1 } ( A )$ ,where $\sigma _ { i } ( \cdot )$ denotes the ith singular value of its argument.

Proof. Let $v _ { i }$ ， $i = 1 , \ldots , n$ ,be the right singular vectors of $A$ . Since $\operatorname { r a n k } ( Y ) = k < n$ ,there is a vector $v = c _ { 1 } v _ { 1 } + \cdot \cdot \cdot + c _ { k + 1 } v _ { k + 1 }$ such that $\| v \| _ { 2 } ^ { 2 } = c _ { 1 } ^ { 2 } + \cdot \cdot \cdot + c _ { k + 1 } ^ { 2 }$ and ${ \cal Y } ^ { H } { \boldsymbol { v } } = 0$ . It follows that

$$
\begin{array} { r l } & { \sigma _ { 1 } ^ { 2 } ( A - B _ { k } ) \geq v ^ { H } ( A - B _ { k } ) ^ { H } ( A - B _ { k } ) v = v ^ { H } A ^ { H } A v } \\ & { \qquad = | c _ { 1 } | ^ { 2 } \sigma _ { 1 } ^ { 2 } + \cdot \cdot \cdot + | c _ { k + 1 } | ^ { 2 } \sigma _ { k + 1 } ^ { 2 } \geq \sigma _ { k + 1 } ^ { 2 } . } \end{array}
$$

Lemma 1.3.7. Let $A = B + C$ ，where $B , C \in \mathbb { C } ^ { m \times n }$ ， $m \geq n$ ，have ordered singular values $\sigma _ { 1 } ( B ) \ge \cdots \ge \sigma _ { n } ( B )$ and $\sigma _ { 1 } ( C ) \geq \cdot \cdot \cdot \geq \sigma _ { n } ( C )$ ，respectively. Then the ordered singular values of $A$ satisfy

$$
\sigma _ { i + j - 1 } ( A ) \leq \sigma _ { i } ( B ) + \sigma _ { j } ( C ) .
$$

Proof. For $i = j = 1$ we have $\sigma _ { 1 } ( A ) = u _ { 1 } ^ { H } A v _ { 1 } = u _ { 1 } ^ { H } B v _ { 1 } + u _ { 1 } ^ { H } C v _ { 1 } \leq \sigma _ { 1 } ( B ) + \sigma _ { 1 } ( C ) .$ Now let $B _ { i - 1 }$ and $C _ { i - 1 }$ denote the SVD expansions truncated to $_ { i - 1 }$ terms. Then $\sigma _ { 1 } ( B - B _ { i - 1 } ) = \sigma _ { i } ( B )$ and $\sigma _ { 1 } ( C - C _ { i - j } ) = \sigma _ { j } ( C )$ .Moreover, $\operatorname { r a n k } ( B _ { i - 1 } + C _ { i - 1 } ) \leq i + j - 2$ .From these facts and Lemma 1.3.6 it follows that

$$
\begin{array} { r l } & { \sigma _ { i } ( B ) + \sigma _ { j } ( C ) = \sigma _ { 1 } ( B - B _ { i - 1 } ) + \sigma _ { 1 } ( C - C _ { j - 1 } ) } \\ & { \qquad \geq \sigma _ { 1 } ( A - B _ { i - 1 } + C _ { j - 1 } ) \geq \sigma _ { i + j - 1 } ( A ) . } \end{array}
$$

We are now able to prove an important best approximation property of truncated SVD expansions.

Theorem 1.3.8 (Eckart-Young-Mirsky Theorem).Let $A \in \mathbb { C } ^ { m \times n }$ be a matrix of rank $r$ ， and let $\mathcal { M } _ { k } ^ { m \times n }$ denote the set of matrices in $\mathbb { C } ^ { m \times n }$ of rank $k$ Then,forall unitarilyinvariant norms,the solution of the problem

$$
\operatorname* { m i n } _ { B } \| A - B \| , \quad B \in \mathcal { M } _ { k } ^ { m \times n } , \quad 1 \leq k < r ,
$$

$k < r$ terms: $\begin{array} { r } { A _ { k } = \sum _ { i = 1 } ^ { k } \sigma _ { i } u _ { i } v _ { i } ^ { H } } \end{array}$ The minimum

$$
\| A - A _ { k } \| _ { 2 } = \sigma _ { k + 1 } , \qquad \| A - A _ { k } \| _ { F } = ( \sigma _ { k + 1 } ^ { 2 } + \cdot \cdot \cdot + \sigma _ { r } ^ { 2 } ) ^ { 1 / 2 } .
$$

Proof. For the spectral norm the result follows directly from Lemma 1.3.6.For the Frobenius norm, set $B = A - B _ { k }$ ，where $B _ { k }$ has rank $k$ . Then $\sigma _ { k + 1 } ( B _ { k } ) = 0$ and, setting $j = k + 1$ in (1.3.15), we obtain $\sigma _ { i } ( A - B _ { k } ) \geq \sigma _ { k + 1 } ( A )$ ， $i = 1 , 2 , \dots .$ From this it follows that $\| A - B _ { k } \| _ { F } ^ { 2 } \geq$ $\sigma _ { k + 1 } ^ { 2 } ( A ) + \cdot \cdot \cdot + \sigma _ { n } ^ { 2 } ( A )$ □

The Eckart-Young-Mirsky theorem was originally proved for the Frobenius norm,for which the solution is unique;see Eckhart and Young [357,1936]. The result for an arbitrary unitarily invariant norm is due to Mirsky [797,196o]. An elementary proof of the general case is given by Li and Strang [740, 2020].

The best approximation property of the partial sums of the SVD expansion has a wide range of applications in applied mathematics and is a key tool for constructing reduced-order models. In signal processing, $A$ may be derived from data constituting a noisy signal, and a rank reduction is used to filter out the noise and reconstruct the true signal. Other applications are noise filtering in statistics and model reduction in control and systems theory. Recently it has been recognized that most high-dimensional data sets can be well approximated by low-rank matrices; see Udell and Townsend [1071, 2019].

# Notes and references

Golub, Hoffman,and Stewart [494,1987] prove a generalization that shows how to obtain a best approximation when a specified set of columns in the matrix is to remain fixed.

# 1.3.3 - Perturbation Theory of Pseudoinverses

The condition number of a problem is a measure of the sensitivity of the solution to small perturbations in the input data. For a nonsingular matrix $A \in \mathbb { R } ^ { n \times n }$ the inverse $( A + E ) ^ { - 1 }$ exists for sufficiently small $\| E \|$ ， where the norm is assumed to be submultiplicative. Taking norms of the identity $( A + E ) ^ { - 1 } - A ^ { - 1 } = ( A + E ) ^ { - 1 } E A ^ { - 1 }$ , we obtain

$$
\operatorname* { m a x } _ { \| E \| \leq \epsilon } \left\| ( A + E ) ^ { - 1 } - A ^ { - 1 } \right\| \leq \epsilon \left\| ( A + E ) ^ { - 1 } \right\| \left\| A ^ { - 1 } \right\| .
$$

The absolute condition number for computing the inverse $A ^ { - 1 }$ is defined as the limit

$$
\operatorname* { i n f } _ { \| E \| \leq \epsilon } \operatorname* { m a x } _ { \| E \| \leq \epsilon } \frac { 1 } { \epsilon } \big \| ( A + E ) ^ { - 1 } - A ^ { - 1 } \big \| = \| A ^ { - 1 } \| ^ { 2 } , \quad \epsilon \to + 0 .
$$

The relative condition number for computing the inverse is obtained by multiplying this quantity by $\| A \| / \| A ^ { - 1 } \|$ ：

$$
\kappa ( A ) = \| A \| \| A ^ { - 1 } \| .
$$

This is invariant under multiplication of $A$ by a scalar, $\kappa ( \alpha A ) = \kappa ( A )$ . From (1.3.18) it follows that

$$
\kappa ( A B ) \leq \kappa ( A ) \kappa ( B ) .
$$

From the identity $A A ^ { - 1 } = I$ it follows that $\kappa _ { \mathcal { P } } ( A ) \geq \| I \| _ { \mathcal { P } } = 1$ for all matrix $\ell _ { p }$ -norms. A matrix with large condition number is called ill-conditioned; otherwise, it is called well-conditioned.

To indicate that a particular norm is used, we write $\kappa _ { \infty } ( A )$ . For the Euclidean norm the condition number can be expressed in terms of the singular values $\sigma _ { 1 } \geq \cdots \geq \sigma _ { n }$ of $A$ as

$$
\kappa _ { 2 } ( A ) = \sigma _ { 1 } ( A ) / \sigma _ { n } ( A ) .
$$

This expression applies also to rectangular matrices $A \in \mathbb { C } ^ { m \times n }$ with $\operatorname { r a n k } ( A ) = n$ .For a real orthogonal or unitary matrix $U$ ，

$$
\kappa _ { 2 } ( U ) = \| U \| _ { 2 } \| U ^ { - 1 } \| _ { 2 } = 1 .
$$

Such matrices are perfectly conditioned in the $\ell _ { 2 }$ -norm.Furthermore,if $P$ and $Q$ are real orthogonal or unitary, then $\kappa ( P A Q ) = \kappa ( A )$ for both the $\ell _ { 2 }$ -norm and the Frobenius norm.This is one reason why real orthogonal and unitary transformations play such a central role in matrix computations.

The normwise relative distance of a matrix $A$ to the set of singular matrices is defined as

$$
\operatorname { d i s t } ( A ) : = \operatorname* { m i n } _ { E } { \big \{ } \| E \| / \| A \| ~ | ~ A + E { \mathrm { ~ i s ~ s i n g u l a r } } { \big \} } .
$$

For the spectral norm it follows from the Eckart-Young-Mirsky theorem (Theorem 1.3.8) that

$$
\mathrm { d i s t } _ { 2 } ( A ) = 1 / ( \| A \| _ { 2 } \| A ^ { - 1 } \| _ { 2 } ) = 1 / \kappa _ { 2 } ( A ) .
$$

This equality holds for any subordinate matrix norm and can be used to get a lower bound for the condition number; see Kahan [681,1966] and Stewart and Sun [1033,199o,Theorem I.2.8].

Let $B \ = \ A + E$ be a perturbation of a matrix $A \ \in \ \mathbb { R } ^ { m \times n }$ .Estimating the difference $\| ( A + E ) ^ { \dagger } - A ^ { \dagger } \|$ is complicated by the fact that $A ^ { \dagger }$ varies discontinuously when the rank of $A$ changes.A trivial example is

$$
A = \left( { \begin{array} { c c } { \sigma } & { 0 } \\ { 0 } & { 0 } \end{array} } \right) , \quad E = \left( { \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { \epsilon } \end{array} } \right) ,
$$

where $\sigma > 0 , \epsilon \neq 0$ . Then the perturbation in $A ^ { \dagger }$ becomes unbounded when $\epsilon  0$ ：

$$
\| ( A + E ) ^ { \dagger } - A ^ { \dagger } \| _ { 2 } = | \epsilon | ^ { - 1 } .
$$

Definition 1.3.9. Two subspaces $\mathcal { R } ( A )$ and $\mathcal { R } ( B )$ are said to be acute if the corresponding orthogonal projections satisfy

$$
\left\| P _ { \mathcal { R } ( A ) } - P _ { \mathcal { R } ( B ) } \right\| _ { 2 } < 1 .
$$

A perturbation $B = A + E$ of $A$ is said to be acute if $\mathcal { R } ( A )$ and $\mathcal { R } ( B )$ , as well as $\mathcal { R } ( A ^ { H } )$ and $\mathcal { R } ( B ^ { H } )$ ,are acute.

Theorem 1.3.10. The matrix $B$ is an acute perturbation of $A$ if and only if

$$
\operatorname { r a n k } ( A ) = \operatorname { r a n k } ( B ) = \operatorname { r a n k } ( P _ { \mathcal { R } ( A ) } B P _ { \mathcal { R } ( A ^ { T } ) } ) .
$$

Proof. See Stewart [1018,1977].

If the perturbation $E$ does not change the rank of $A$ , then unbounded growth of $( A + E ) ^ { \dagger }$ cannot occur.

Lemma 1.3.11. $I f \operatorname { r a n k } ( A + E ) = \operatorname { r a n k } ( A )$ and $\eta = \| A ^ { \dagger } \| _ { 2 } \| E \| _ { 2 } < 1$ ，then

$$
\lVert ( A + E ) ^ { \dagger } \rVert _ { 2 } \leq \frac { 1 } { 1 - \eta } \lVert A ^ { \dagger } \rVert _ { 2 } .
$$

Proof. From the assumption and Theorem 1.3.3 it follows that

$$
1 / \| ( A + E ) ^ { \dagger } \| _ { 2 } = \sigma _ { r } ( A + E ) \geq \sigma _ { r } ( A ) - \| E \| _ { 2 } = 1 / \| A ^ { \dagger } \| _ { 2 } - \| E \| _ { 2 } > 0 ,
$$

which implies (1.3.23).

By expressing the projections in terms of pseudoinverses and using the relations in (1.2.29), we obtain Wedin's identity (Wedin [1106,1969]). If $B = A + E$ ,then

$$
B ^ { \dagger } - A ^ { \dagger } = - B ^ { \dagger } E A ^ { \dagger } + ( B ^ { H } B ) ^ { \dagger } E ^ { H } P _ { \mathcal { N } ( A ^ { T } ) } - P _ { \mathcal { N } ( B ) } E ^ { H } ( A A ^ { H } ) ^ { \dagger } .
$$

Theorem 1.3.12. If $B = A + E$ and $\operatorname { r a n k } ( B ) = \operatorname { r a n k } ( A )$ ，then

$$
\| B ^ { \dagger } - A ^ { \dagger } \| \leq \mu \| B ^ { \dagger } \| \| A ^ { \dagger } \| \| E \| ,
$$

where $\mu = 1$ for the Frobenius norm $\lVert \cdot \rVert _ { F }$ provided that $\operatorname { r a n k } ( A ) = \operatorname* { m i n } ( m , n )$ For the spectral norm $\| \cdot \| _ { 2 }$ ，

$$
\mu = { \left\{ \begin{array} { l l } { { \frac { 1 + { \sqrt { 5 } } } { 2 } } } & { i f \operatorname { r a n k } \left( A \right) < \operatorname* { m i n } ( m , n ) , } \\ { { \sqrt { 2 } } } & { i f \operatorname { r a n k } \left( A \right) = \operatorname* { m i n } ( m , n ) . } \end{array} \right. }
$$

The result for the 2-norm is due to Wedin [1108,1973]. For the Frobenius norm, $\mu = 1$ as shown by van der Sluis and Veltkamp [1O74,1979]. From the results above we deduce that

$$
\operatorname* { l i m } _ { E \to 0 } ( A + E ) ^ { \dagger } = A ^ { \dagger } \iff \operatorname* { l i m } _ { E \to 0 } \operatorname { r a n k } ( A + E ) = \operatorname { r a n k } ( A ) .
$$

Let $B = A ( \tau ) = A + \tau E$ ，where $\tau$ is a scalar parameter. Letting $\tau  0$ and assuming $A ( \tau )$ has constant local rank, we see that Wedin's identity gives the following formula for the derivative of the pseudoinverse:

$$
\frac { d A ^ { \dagger } } { d \tau } = - A ^ { \dagger } \frac { d A } { d \tau } A ^ { \dagger } + ( A ^ { H } A ) ^ { \dagger } \frac { d A ^ { H } } { d \tau } P _ { \mathcal { N } ( A ^ { T } ) } - P _ { \mathcal { N } ( A ) } \frac { d A ^ { H } } { d \tau } ( A A ^ { H } ) ^ { \dagger } .
$$

Similar formulas for derivatives of orthogonal projectors and pseudoinverses are derived by Golub and Pereyra [5O3,1973]. For the least squares solution $x = A ^ { \dagger } b$ ,we obtain

$$
\frac { d x } { d \tau } = - A ^ { \dagger } \frac { d A } { d \tau } x + ( A ^ { H } A ) ^ { \dagger } \frac { d A ^ { H } } { d \tau } P _ { \mathcal { N } ( A ^ { T } ) } b - P _ { \mathcal { N } ( A ) } \frac { d A ^ { H } } { d \tau } ( A ^ { H } ) ^ { \dagger } x .
$$

The discontinuity of the pseudoinverse means that the mathematical notion of rank is not appropriate in numerical computations. If a matrix $A$ has (mathematical) rank $k < n$ ,and $E$ is a random perturbation, then $A + E$ will most likely have full rank $n$ ,and $A ^ { \dagger }$ will differ significantly from $( A + E ) ^ { \dagger }$ . Thus,if $A$ is close to a rank-deficient matrix, for practical purposes it should be considered as rank-deficient. It is important that this be recognized, because overestimating the rank of $A$ can lead to a computed solution $x$ of very large norm.

The considerations above show that the numerical rank assigned to $A$ should depend on a tolerance reflecting the level of errors in $A$ .We say that $A$ has numerical $\delta$ -rank equal to $k$ if

$$
k = \operatorname* { m i n } \{ \operatorname { r a n k } ( B ) \mid \| A - B \| _ { 2 } \leq \delta \} .
$$

That is, the numerical rank of $A$ is the smallest rank of all matrices at a distance from $A$ less than orequal to $\delta$ Let $\begin{array} { r } { A = U \Sigma V ^ { H } = \sum _ { i = 1 } ^ { n } { u _ { i } \sigma _ { i } v _ { i } ^ { H } } } \end{array}$ be the SVD expansion of $A$ By the Wielandt-Hoffman Theorem 1.3.3, for $k < n$ ，

$$
\operatorname* { i n f } _ { \operatorname { r a n k } ( B ) \leq k } \| A - B \| _ { 2 } = \sigma _ { k + 1 } .
$$

$\begin{array} { r } { B = \sum _ { i = 1 } ^ { k } \sigma _ { i } u _ { i } v _ { i } ^ { H } } \end{array}$ It folostatt $A$ has rureical $\delta$ rank $k$ if and

$$
\sigma _ { 1 } \geq \cdots \geq \sigma _ { k } > \delta \geq \sigma _ { k + 1 } , \geq \cdots \geq \sigma _ { n } .
$$

From (1.3.28) it follows that

$$
\| A - A _ { k } \| _ { 2 } = \| A V _ { 2 } \| _ { 2 } \leq \delta , \quad V _ { 2 } = ( v _ { k + 1 } , \ldots , v _ { n } ) ,
$$

where $\mathcal { R } ( V _ { 2 } )$ is the numerical nullspace of $A$ . In many applications the cost of using SVD to determine the numerical rank and nullspace of a matrix can be prohibitively high.

Choosing the parameter $\delta$ in (1.3.3O) depends on the context and is not always an easy matter. Let $E = ( e _ { i j } )$ be an upper bound on the absolute eror in $A$ ，If the elements $e _ { i j }$ are about the same magnitude,and $| e _ { i j } | \le \epsilon$ for all $i , j$ , then

$$
\| E \| _ { 2 } \leq \| E \| _ { F } \leq ( m n ) ^ { 1 / 2 } \epsilon .
$$

In this case a reasonable choice in (1.3.30) is $\delta = ( m n ) ^ { 1 / 2 } \epsilon$

Definition (1.3.30) is satisfactory only when there is a well-defined gap between $\sigma _ { k + 1 }$ and $\sigma _ { k }$ . This should be the case if the exact matrix $\tilde { A }$ is rank-deficient but well-conditioned. However, some matrices lack a well-determined numerical rank. Then additional information is needed to determine a meaningful solution; see Section 3.5.3.

# 1.3.4 - Perturbation of Least Squares Solutions

Let $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ be a least squares problem with $\operatorname { r a n k } ( A ) = n$ .Denote by $x + \delta x$ the solution to the perturbed problem

$$
\operatorname* { m i n } _ { x } \| ( A + E ) x - ( b + f ) \| _ { 2 } , \quad \| E \| _ { 2 } < \sigma _ { n } ( A ) .
$$

Then $\operatorname { r a n k } ( A + E ) = n$ ,and the perturbed solution satisfies the normal equations

$$
( A + E ) ^ { T } ( ( A + E ) ( x + \delta x ) - ( b + f ) ) = 0 .
$$

We shallderive a first-order estimate of $\| \delta x \| _ { 2 }$ Subtracting $A ^ { T } ( A x - b ) = 0$ and neglecting second-order terms, we get $( A ^ { T } A ) \delta x = A ^ { T } ( f - E x ) + E ^ { T } ( b - A x )$ or

$$
\delta \boldsymbol { x } = A ^ { \dagger } ( \boldsymbol { f } - E \boldsymbol { x } ) + ( A ^ { T } A ) ^ { - 1 } E ^ { T } \boldsymbol { r } ,
$$

where $A ^ { \dagger } = ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ and $r = b - A x$ . (Note that $\delta x = A ^ { \dagger } f = A ^ { \dagger } A A ^ { \dagger } f = A ^ { \dagger } P _ { \mathcal { R } ( A ) } f$ depends only on the component $f _ { 1 } = P _ { \mathcal { R } ( A ) } f$ in $\mathcal { R } ( A )$ .) From the SVD $A = U \Sigma V ^ { T }$ we have

$$
\| ( A ^ { T } A ) ^ { - 1 } A ^ { T } \| _ { 2 } = 1 / \sigma _ { n } , \qquad \| ( A ^ { T } A ) ^ { - 1 } \| _ { 2 } = 1 / \sigma _ { n } ^ { 2 } ,
$$

and taking norms in (1.3.31) gives the first-order result

$$
\| \delta x \| _ { 2 } \leq \frac { 1 } { \sigma _ { n } } \big ( \| f \| _ { 2 } + \| E \| _ { 2 } \| x \| _ { 2 } \big ) + \frac { 1 } { \sigma _ { n } ^ { 2 } } \| E \| _ { 2 } \| r \| _ { 2 } .
$$

Since $1 / \sigma _ { n } = \kappa ( A ) / \| A \| _ { 2 }$ ,the last term in (1.3.32) is proportional to $\kappa ^ { 2 } ( A )$ . Golub and Wilkinson [514,1g66] were the first to note that a term proportional to $\kappa ^ { 2 }$ occurs when $r \neq 0$ . Van der Sluis [1073,1975l gives a geometrical explanation for the occurrence of this term.

Wedin [11O8,1973l gives a more refined analysis that applies also to rank-defcient prob-lems. To be able to prove any meaningful result, he assumes that the perturbation $E$ satisfies the conditions

$$
\operatorname { r a n k } ( A + E ) = \operatorname { r a n k } ( A ) , \qquad \eta = \| A ^ { \dagger } \| _ { 2 } \| E \| _ { 2 } < 1 .
$$

Note that if $\operatorname { r a n k } ( A ) = \operatorname* { m i n } ( m , n )$ then the condition $\eta < 1$ suffices to guarantee that $\operatorname { r a n k } ( A +$ $E ) = \operatorname { r a n k } ( A )$ . The analysis needs the following estimate for the largest principal angle between the fundamental subspaces of $\tilde { A }$ and $A$ (see Definition 1.2.12).

Lemma 1.3.13. Suppose ${ \tilde { A } } = A + E$ and conditions (1.3.33) are satisfied. Then if $\chi ( \cdot )$ denotes any of the four fundamental subspaces,

$$
\sin \theta _ { \operatorname* { m a x } } ( \chi ( \tilde { A } ) , \chi ( A ) ) \leq \eta < 1 .
$$

Proof. See Wedin [1108, 1973,Lemma 4.1].

Nearly optimal bounds for the perturbation of the solution of least squares problems are derived in Bjorck [125,1967].

Theorem 1.3.14. Suppose 1 $\operatorname { a n k } ( A + E ) = \operatorname { r a n k } ( A )$ and that perturbations $E$ and $f$ satisfy the normwise relative bounds

$$
\| E \| _ { 2 } / \| A \| _ { 2 } \le \epsilon _ { A } , \quad \| f \| _ { 2 } / \| b \| _ { 2 } \le \epsilon _ { b } .
$$

Then if $\eta = \kappa \epsilon _ { A } < 1$ ， the perturbations $\delta x$ and δr in the least squares solution $x$ and residual $r = b - A x$ satisfy

$$
\begin{array} { l } { \displaystyle \| \delta x \| _ { 2 } \leq \frac { \kappa } { 1 - \eta } \left( \epsilon _ { A } \| x \| _ { 2 } + \epsilon _ { b } \frac { \| b \| _ { 2 } } { \| A \| _ { 2 } } + \epsilon _ { A } \kappa \frac { \| r \| _ { 2 } } { \| A \| _ { 2 } } \right) + \epsilon _ { A } \kappa \| x \| _ { 2 } , } \\ { \displaystyle \| \delta r \| _ { 2 } \leq \epsilon _ { A } \| x \| _ { 2 } \| A \| _ { 2 } + \epsilon _ { b } \| b \| _ { 2 } + \epsilon _ { A } \kappa \| r \| _ { 2 } . } \end{array}
$$

Proof. Decomposing $\delta x = \tilde { A } ^ { \dagger } \tilde { b } - x = A ^ { \dagger } ( A x + r + f ) - x$ and using $P _ { \mathcal { N } ( \tilde { A } ) } = I - \tilde { A } ^ { \dagger } \tilde { A }$ we get

$$
\delta x = \tilde { A } ^ { \dagger } P _ { \mathcal { R } ( \tilde { A } ) } ( f - E x ) + \tilde { A } ^ { \dagger } r - P _ { \mathcal { N } ( \tilde { A } ) } x .
$$

We separately estimate each of the three terms in this decomposition of $\delta x$ . From Lemma 1.3.11 it follows that

$$
\| \tilde { A } ^ { \dagger } ( f - E x ) \| _ { 2 } \leq \frac { 1 } { 1 - \eta } \| A ^ { \dagger } \| _ { 2 } ( \| E \| _ { 2 } \| x \| _ { 2 } + \| f \| _ { 2 } ) .
$$

From $r \perp \mathcal { R } ( A )$ we have $r = P _ { \mathcal { N } ( A ^ { T } ) } r$ ,and from (1.2.29) the second term becomes

$$
\tilde { A } ^ { \dagger } r = \tilde { A } ^ { \dagger } \tilde { A } \tilde { A } ^ { \dagger } r = \tilde { A } ^ { \dagger } P _ { \mathcal { R } ( \tilde { A } ) } P _ { \mathcal { N } ( A ^ { T } ) } r .
$$

By definition, $\| P _ { \mathcal { R } ( \tilde { A } ) } P _ { \mathcal { N } ( A ^ { T } ) } \| _ { 2 } = \sin \theta _ { \mathrm { m a x } } ( \mathcal { R } ( \tilde { A } ) , \mathcal { R } ( A ) )$ ，where $\theta _ { \mathrm { m a x } }$ is the largest principal angle between the subspaces $\mathcal { R } ( \tilde { \boldsymbol { A } } )$ and $\mathcal { R } ( A )$ .Similarly, $x = P _ { \mathcal { R } ( A ^ { T } ) } x$ ，and the third term can be written as $P _ { \mathcal { N } ( \tilde { A } ) } x = P _ { \mathcal { N } ( \tilde { A } ) } P _ { \mathcal { R } ( A ^ { T } ) } x$ ， where by Lemma 1.3.13 $\| P _ { \mathcal { N } ( \tilde { A } ) } P _ { \mathcal { R } ( A ^ { T } ) } \| _ { 2 } =$ $\sin \theta _ { \operatorname* { m a x } } ( \mathcal { N } ( \tilde { A } ) , \mathcal { N } ( A ) ) \leq \eta$ .The estimate (1.3.36) now follows, and (1.3.37) is proved using the decomposition

$$
\begin{array} { r l } & { \tilde { r } - r = P _ { \mathrm { \mathcal { N } ( \tilde { A } ^ { T } ) } } ( b + f ) - P _ { \mathrm { \mathcal { N } ( A ^ { T } ) } } b } \\ & { \qquad = P _ { \mathrm { \mathcal { N } ( \tilde { A } ^ { T } ) } } f + P _ { \mathrm { \mathcal { N } ( \tilde { A } ^ { T } ) } } P _ { \mathrm { \mathcal { R } ( A ) } } b - P _ { \mathcal { R } ( \tilde { A } ^ { T } ) } P _ { \mathrm { \mathcal { N } ( A ^ { T } ) } } r , } \end{array}
$$

and $P _ { \mathcal { N } ( \tilde { A } ^ { T } ) } P _ { \mathcal { R } ( A ) } b = P _ { \mathcal { N } ( \tilde { A } ^ { T } ) } A x = - P _ { \mathcal { N } ( \tilde { A } ^ { T } ) } E x .$

If $\operatorname { r a n k } ( A ) = n$ ，then $\mathcal { N } ( { \tilde { A } } ) = \{ 0 \}$ ，and the last term in (1.3.36) (and therefore also in (1.3.37)) vanishes. If the system is consistent, then $r = 0$ ,and the term involving $\kappa ^ { 2 }$ in (1.3.36) vanishes.If $\operatorname { r a n k } ( A ) = n$ and $\epsilon _ { b } = 0$ ,the condition number of the least squares problem can be written as

$$
\kappa _ { L S } ( A , b ) = \kappa ( A ) \left( 1 + \kappa ( A ) \frac { \| r \| _ { 2 } } { \| A \| _ { 2 } \| x \| _ { 2 } } \right) .
$$

Note that the condition depends on $r$ and therefore on the right-hand side $b$ 、This dependence is negligible if $\kappa ( A ) \| r \| _ { 2 } \ll \| A \| _ { 2 } \| x \| _ { 2 }$ . By considering first-order approximations of the terms, it can be shown that for any matrix $A$ of rank $n$ and vector $b$ there are perturbations $E$ and $f$ such that the estimates in Theorem 1.3.14 can almost be attained.

In many applications,one is not directly interested in the least squares solution $x$ but in some functional $c = L ^ { T } x$ ,where $\boldsymbol { L } \in \mathbb { R } ^ { n \times k }$ . For example,in the determination of positions using GPS systems,the main quantities of interest are the three-dimensional coordinates,but the statistical model involves several other auxiliary parameters; see Arioli, Baboulin, and Gratton [32, 2007]. The sensitivity of functionals of the solution of ill-conditioned least squares problems is studied by Eldén [372,1990]. From(1.3.31) we have

$$
\delta L ^ { T } x = L ^ { T } A ^ { \dagger } ( f - E x ) + L ^ { T } ( A ^ { T } A ) ^ { - 1 } E ^ { T } r .
$$

Assume for convenience that $\operatorname { r a n k } ( A ) = n$ ，and let $A = Q R$ be the QR factorization of $A$ Then $A ^ { \dagger } = R ^ { - 1 } Q ^ { T }$ ， $( A ^ { T } A ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }$ ,and $\| R ^ { - T } \| _ { 2 } = \sigma _ { n } ( A )$ . We obtain the perturbation bound

$$
\| \delta c \| _ { 2 } \leq \| C \| _ { 2 } { \bigg ( } \| f \| _ { 2 } + \| E \| _ { 2 } \| x \| _ { 2 } + { \frac { 1 } { \sigma _ { n } } } \| r \| _ { 2 } { \bigg ) } ,
$$

where $C = R ^ { - T } L$ . A bound for the perturbation of a particular component $x _ { i }$ of the least squares solution is obtained by taking $\boldsymbol { L } = \boldsymbol { e } _ { i }$ ,the ith column of the unit matrix $I _ { n }$ . In particular, for $i = n$ , the solution of $R ^ { T } C = e _ { n }$ is simply $C = r _ { n n } ^ { - 1 } e _ { n }$ and $\| C \| _ { 2 } = r _ { n n } ^ { - 1 }$ .If $A$ is rank-deficient, the SVD $A = U \Sigma V ^ { T }$ can be used instead of the QR factors. Substituting

$$
A ^ { \dagger } = V \Sigma ^ { \dagger } U , \qquad ( A ^ { T } A ) ^ { - 1 } = V \Sigma ^ { \dagger } ( \Sigma ^ { \dagger } ) ^ { T } V ^ { T }
$$

into (1.3.42) gives (1.3.43) with $C ^ { T } = ( L ^ { T } V ) \Sigma ^ { \dagger }$ and $\sigma _ { n }$ exchanged for $\sigma _ { r }$ , where $r = { \mathrm { r a n k } } ( A )$

Normwise perturbation bounds yield results that are easy to present but ignore how the perturbations are distributed among the elements of the matrix and vector. When the matrix is poorly scaled or sparse,such bounds can greatly overestimate the error. For this reason, componentwise perturbation analysis is gaining increasing attention. As stressed in the excelent survey by Higham [620,1994l, the conditioning of a problem should always be defined with respect to a particular class of perturbations. In normwise analysis, perturbations are considered that satisfy the inequality $\| E \| \leq \epsilon$ for some matrix norm.If the columns of $A$ have vastly different norms, then a more relevant class of perturbations might be

$$
\tilde { a } _ { j } = a _ { j } + \delta a _ { j } , \quad \| \delta a _ { j } \| \le \epsilon \| a _ { j } \| , \quad j = 1 , \ldots , n .
$$

In componentwise analysis, scaling factors $e _ { i j } \geq 0$ and $f _ { i } \geq 0$ are specified, and perturbations such that

$$
| \delta a _ { i j } | \le \omega e _ { i j } , \qquad | \delta b _ { i } | \le \omega f _ { i } , \quad i , j = 1 , \ldots , n ,
$$

for some $\omega > 0$ are considered. By setting $e _ { i j }$ to zero,we can ensure that the corresponding element $a _ { i j }$ is not perturbed. With $\begin{array} { r } { e _ { i j } \ = \ | a _ { i j } | } \end{array}$ and $f _ { i } = | b _ { i } |$ ， $\omega$ bounds the componentwise relative perturbation in each component of $A$ and $b$

We now introduce some notation to be used in the following. A matrix $A$ is nonnegative, $A \geq 0$ ,if $a _ { i j } \geq 0$ for all $i , j$ . Similarly, $A$ is positive, $A > 0$ ,if $a _ { i j } > 0$ for all $i , j$ .If $A$ and $B$ are nonnegative, then so are their sum $A + B$ and product $A B$ .Hence, nonnegative matrices form a convex set. The partial orderings ‘ $\because$ and " $\cdot _ { < } \ "$ for nonnegative matrices $A$ ， $B$ and vectors $x , y$ are to be interpreted componentwise, e.g.,

$$
A \leq B \iff a _ { i j } \leq b _ { i j } , \quad x \leq y \iff x _ { i } \leq y _ { i } .
$$

$A \geq B$ means the same as $B \leq A$ ，and $A > B$ is the same as $B < A$ . These orderings are transitive: if $A \leq B$ and $B \leq C$ ，then $A \leq C$ . Note that there are matrices that cannot be compared by any of these relations. It is rather obvious which rules for handling inequalities can be generalized to this partial ordering in matrix spaces. If $C = A B$ , it is easy to show that $| c _ { i j } | \le$ $\scriptstyle \sum _ { k = 1 } ^ { n } \left| a _ { i k } \right| \left| b _ { k j } \right|$ ,i.e., $\left| C \right| \leq \left| A \right| \left| B \right|$ . A similar rule holds for matrix-vector multiplication.

With the above notation the componentwise bounds (1.3.45) can be writen more compactly as

$$
\begin{array} { r } { | \delta A | \le \omega E , \qquad | \delta b | \le \omega f , } \end{array}
$$

where $E > 0 , f > 0$ . Componentwise relative perturbations are obtained by taking $E = | A |$ and $f = | b |$ . We first consider a nonsingular square linear system $A x = b$ .The basic identity used for a componentwise perturbation analysis is

$$
\delta x = ( I + A ^ { - 1 } \delta A ) ^ { - 1 } A ^ { - 1 } ( \delta A x + \delta b ) .
$$

If $| A ^ { - 1 } | | \delta A | < 1$ , then taking absolute values gives

$$
| \delta \boldsymbol { x } | \leq ( I - | A ^ { - 1 } | | \delta A | ) ^ { - 1 } | A ^ { - 1 } | ( | \delta A | | \boldsymbol { x } | + | \delta \boldsymbol { b } | ) ,
$$

where the inequality is to be interpreted componentwise. The matrix $\left( I - | A ^ { - 1 } | | \delta A | \right)$ is guaranteed to be nonsingular if $\parallel \vert A ^ { - 1 } \vert \vert \delta A \vert \parallel < 1$ .For perturbations satisfying (1.3.47), we obtain

$$
| \delta \boldsymbol { x } | \leq \omega ( I - \omega | A ^ { - 1 } | E ) ^ { - 1 } | A ^ { - 1 } | ( E | \boldsymbol { x } | + f ) .
$$

Assuming that $\omega \kappa _ { E } ( A ) < 1$ , it follows from (1.3.48) that for any absolute norm,

$$
\| \delta x \| \leq { \frac { \omega } { 1 - \omega \kappa _ { E } ( A ) } } \| | A ^ { - 1 } | ( | E | | x | + f ) \| .
$$

Hence $\kappa _ { E } ( A ) = \| | A ^ { - 1 } | E \|$ can be taken to be the componentwise condition number with respect to $E$ . For componentwise relative error bounds $( E = | A | ,$ ,we obtain the Bauer-Skeel condition number of $A$ ，

$$
\kappa _ { | A | } ( A ) = \operatorname { c o n d } \left( A \right) = \| \mathbf { \Lambda } | A ^ { - 1 } | | A | \| .
$$

It can be shown that cond $( A )$ and the bound (1.3.49) with $E = | A |$ are invariant under row scaling.

The Bauer-Skeel perturbation analysis of linear systems can be extended to linear least squares problems by considering the augmented system

$$
\begin{array} { r } { M z = d \ \equiv \ \left( \begin{array} { c c } { I } & { A } \\ { A ^ { T } } & { 0 } \end{array} \right) \left( \begin{array} { c } { y } \\ { x } \end{array} \right) = \left( \begin{array} { c } { b } \\ { c } \end{array} \right) . } \end{array}
$$

If $A$ has full column rank, then

$$
\begin{array} { r } { M ^ { - 1 } = \left( \begin{array} { c c } { P _ { N ( A ^ { T } ) } } & { ( A ^ { \dagger } ) ^ { T } } \\ { A ^ { \dagger } } & { - ( A ^ { T } A ) ^ { - 1 } } \end{array} \right) , } \end{array}
$$

where $P _ { \mathcal { N } ( A ^ { T } ) } = I - A A ^ { \dagger }$ is the orthogonal projection onto ${ \mathcal { N } } ( A ^ { T } )$ . Componentwise perturbations $| \delta A | \le \omega E$ ， $| \delta b | \le \omega f$ ,and $| \delta c | \leq \omega g$ give rise to perturbations

$$
\delta M = \left( \begin{array} { c c } { { 0 } } & { { \delta A } } \\ { { \delta A ^ { T } } } & { { 0 } } \end{array} \right) , \qquad \delta d = \left( \begin{array} { c } { { \delta b } } \\ { { \delta c } } \end{array} \right)
$$

of system (1.3.51). From (1.3.49) applied to $M z = d$ , neglecting terms of order $\omega ^ { 2 }$ ,we obtain

$$
\begin{array} { r l } & { | \delta y | \le \omega | P _ { N ( A ^ { T } ) } | ( E | x | + f ) + \omega | ( A ^ { \dagger } ) ^ { T } | ( E ^ { T } | y | + g ) , } \\ & { | \delta x | \le \omega | A ^ { \dagger } | ( f + E | x | ) + \omega | ( A ^ { T } A ) ^ { - 1 } | ( E ^ { T } | y | + g ) . } \end{array}
$$

The least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ corresponds to taking $c = g = 0$ and $r \ : = \ : y$ With $E = | A |$ and $f = | b |$ we obtain, after taking norms,

$$
\begin{array} { r l } & { \| \delta \boldsymbol { r } \| \leq \omega \| P _ { N ( A ^ { T } ) } ( | A | | \boldsymbol { x } | + | b | ) \| + \omega \| | ( A ^ { \dagger } ) ^ { T } | | A | ^ { T } | \boldsymbol { r } | \| , } \\ & { \| \delta \boldsymbol { x } \| \leq \omega \| | A ^ { \dagger } | ( | A | | \boldsymbol { x } | + | b | ) \| + \omega \| | ( A ^ { T } A ) ^ { - 1 } | | A | ^ { T } | \boldsymbol { r } | \| ; } \end{array}
$$

see Bjorck [132,1991]. For small-residual problems the componentwise condition number for the least squares solution $x$ can be defined as

$$
\operatorname { c o n d } ( A ) = \parallel | A ^ { \dagger } | | A |  .
$$

The least-norm problem min $\lVert y \rVert _ { 2 }$ subject to $A ^ { T } y = c$ corresponds to taking $b = f = 0$

$$
| \delta \boldsymbol { y } | \le \omega | P _ { N ( A ^ { T } ) } E | \boldsymbol { x } | + \omega | ( A ^ { \dagger } ) ^ { T } | ( E ^ { T } | \boldsymbol { y } | + g ) ,
$$

# Notes and references

Componentwise perturbation analysis originated with Bauer [95,1966] and was later refined by Skeel [1000,1979l; see also Higham [620,1994]. A good survey on matrix perturbation theory is given by Stewart and Sun [1033,199o]. Demmel [304,1992] conjectured that the distance of a matrix from a singular matrix in a componentwise sense is close to the reciprocal of its Bauer-Skeel condition number. This conjecture was later proved for the general weighted condition number $\kappa _ { E } ( A )$ by Rump [945,1999].

Abdelmalek [3,1974l gives a perturbation analysis for pseudoinverses and linear least squares problems. Stewart [1O17,1977] gives a unified treatment of the perturbation theory for pseudoinverses and least squares solutions with historical comments.In particular,asymptotic forms and derivatives for orthogonal projectors, pseudoinverses,and least squares solutions are derived. Grcar [531, 2o1o] derives spectral condition numbers of orthogonal projections and full-rank linear least squares problems. Gratton [527,1996] obtains condition numbers of the least squares problem in a weighted Frobenius norm. A similar componentwise analysis is given in Arioli, Duff,and de Rijk [36,198g]. Baboulin and Gratton [50, 2oo9] give sharp bounds for the condition numbers of linear functionals of least squares solutions.

# 1.4 - Floating-Point Computation

# 1.4.1 - Floating-Point Arithmetic

In floating-point computation a real number $a$ is represented in the form

$$
a = \pm m \cdot \beta ^ { e } , \quad \beta ^ { - 1 } \leq m < 1 ,
$$

where exponent $e$ is an integer and $\beta$ is the base of the system. If $t$ digits are used to represent the fraction part $m$ ,we write

$$
m = ( 0 . d _ { 1 } d _ { 2 } \cdot \cdot \cdot d _ { t } ) _ { \beta } , \quad 0 \leq d _ { i } < \beta .
$$

The exponent is limited to a finite range $e _ { \mathrm { m i n } } \le e \le e _ { \mathrm { m a x } }$ . In a floating-point number system, every real number in the floating-point range can be represented with a relative error that does not exceed the unit roundoff

$$
\begin{array} { r } { { \bf u } = \frac { 1 } { 2 } \beta ^ { - t + 1 } . } \end{array}
$$

The IEEE 754-2008 standard for binary floating-point arithmetic [655, 2o19] is used on virtually all general-purpose computers. It specifies formats for floating-point numbers,elementary operations, and rounding rules. Three basic formats are specified for representing a number: single, double,and quadruple precision using 32, 64,and 128 bits,respectively. Also, a half precision format fpl6 using 16 bits was introduced. This offers massive speed-up, but because the maximum number that can be represented is only about 65,Ooo,overflow is more likely. This motivated Google to propose another half precision format with wider range called bfloat16. Half precision formats have applications in computer graphics as well as deep learning; see Pranesh [9O4, 2o19]. Because it is cheaper to move data in lower precision, the cost of communication is reduced. The characteristics of floating-point formats are summarized in Table 1.4.1.

Table 1.4.1. IEEE 754-2008 binary floating-point formats.   

<table><tr><td></td><td>Format</td><td>t</td><td>e</td><td>emin</td><td>emax</td><td>u</td></tr><tr><td>Half bfloat16</td><td>16</td><td>8</td><td>8</td><td>-126</td><td>+127</td><td>3.91 · 10-3</td></tr><tr><td>Half fp16</td><td>16</td><td>11</td><td>5</td><td>-14</td><td>+15</td><td>4.88 · 10-4</td></tr><tr><td>Single</td><td>32</td><td>24</td><td>8</td><td>-126</td><td>+127</td><td>5.96 · 10-8</td></tr><tr><td>Double</td><td>64</td><td>53</td><td>11</td><td>-1022</td><td>+1023</td><td>1.11 · 10-16</td></tr><tr><td>Quadruple</td><td>128</td><td>113</td><td>15</td><td>-16,382</td><td>+16,383</td><td>0.963 · 10-34</td></tr></table>

Four rounding modes are supported by the standard. The default rounding mode is round to the nearest representable number, with rounding to even in the case of a tie. Chopping (i.e., rounding toward zero) is also supported,as well as directed rounding to $\infty$ and $- \infty$ .The latter modes simplify the implementation of interval arithmetic.

The IEEE standard specifies that al arithmetic operations, including the square root, should be performed as if they were first calculated to infinite precision and then rounded to a foatingpoint number according to one of the four modes mentioned above. One reason for specifying precisely the results of arithmetic operations is to improve the portability of software. If a pro-gram is moved between two computers,both supporting the IEEE standard, intermediate and final results should be the same.

If $x$ and $y$ are floating-point numbers, then

$$
f l ( x + y ) , \quad f l ( x - y ) , \quad f l ( x \cdot y ) , \quad f l ( x / y )
$$

denote the results of floating-point operations that the machine stores in memory (after rounding or chopping). Unless underflow or overflow occurs,in IEEE floating-point arithmetic,

$$
f l \left( x \operatorname { o p } y \right) = ( x \operatorname { o p } y ) ( 1 + \delta ) , \quad | \delta | \leq \mathbf { u } ,
$$

where $\mathbf { u }$ is the unit roundoff and“op” stands for one of the four elementary operations $+ , - , \cdot ,$ and $/$ . Similarly,for the square root it holds that

$$
f l \left( { \sqrt { x } } \right) = { \sqrt { x } } ( 1 + \delta ) , \quad | \delta | \leq \mathbf { u } .
$$

Complex arithmetic can be reduced to real arithmetic as follows. If we let $x = a + i b$ and $y = c + i d$ be two complex numbers, where $y \ne 0$ ,then

$$
\begin{array} { c } { { x \pm y = a \pm c + i ( b \pm d ) , } } \\ { { x \times y = ( a c - b d ) + i ( a d + b c ) , } } \\ { { x / y = \displaystyle \frac { a c + b d } { c ^ { 2 } + d ^ { 2 } } + i \displaystyle \frac { b c - a d } { c ^ { 2 } + d ^ { 2 } } ~ . } } \end{array}
$$

The square root of a complex number $u + i v = \sqrt { x + i y }$ is given by

$$
u = ( r + x / 2 ) ^ { 1 / 2 } , \qquad v = \left( r - x / 2 \right) ^ { 1 / 2 } , \quad r = \sqrt { x ^ { 2 } + y ^ { 2 } } .
$$

When $x > 0$ there will be cancellation when computing $v$ This can be severe if also $| x | \gg | y |$ (cf. Section 2.3.4 of [284, 2oo8]). To avoid this,we note that

$$
u v = { \frac { 1 } { 2 } } { \sqrt { r ^ { 2 } - x ^ { 2 } } } = { \frac { y } { 2 } } ,
$$

S0 $v$ can be computed from $v = y / ( 2 u )$ . When $x < 0$ we instead compute $v$ from (1.4.6) and set $u = y / ( 2 v )$

Very few quantities in the physical world is known to an accuracy beyond IEEE double precision. A value of $\pi$ correct to 2O decimal digits would suffice to calculate the circumference of a circle around the Sun at the orbit of Earth to within the width of an atom! Occasionally one may want to perform some calculation,e.g., evaluate some mathematical constant such as $\pi$ to very high precision. Extremely high precision is also sometimes needed in experimental mathematics when searching for new identities. For such purposes, multiple precision packages have been developed that simulate arithmetic of arbitrarily high precision using standard floatingpoint arithmetic; see Brent [177,178,1978].

When validated answers to mathematical problems have to be computed, another possibility is to use interval arithmetic. Input data are given as intervals,and inclusion intervals for each intermediate result are systematically calculated. An interval vector is denoted by $[ x ]$ and has interval components $[ x _ { i } ] = [ \underline { { x } } _ { i } , \overline { { x _ { i } } } ]$ ， $i = 1 : n$ .Likewise,an interval matrix $[ A ] = ( [ a _ { i j } ] )$ has interval entries

$$
\begin{array} { r } { [ a _ { i j } ] = [ \underline { { a } } _ { i j } , \overline { { a } } _ { i j } ] , \quad i = 1 : m , \quad j = 1 : n . } \end{array}
$$

Operations between interval matrices and interval vectors are defined in an obvious manner. The interval matrix-vector product $[ A ] [ x ]$ is the smallest interval vector that contains the set $\{ A x \mid A \in [ A ]$ ， $x \in [ x ] \}$ , but it normally does not coincide with this set. By the inclusion property,

$$
\{ A x \mid A \in [ A ] , x \in [ x ] \} \subseteq [ A ] [ x ] = { \biggl ( } \sum _ { j = 1 } ^ { n } [ a _ { i j } ] [ x _ { j } ] { \biggr ) } .
$$

In general the image of an interval vector under a transformation is not an interval vector. As a consequence, the inclusion operation will usually yield an overestimation. This phenomenon, intrinsic to interval computations,is called the wrapping effect. Rump [943,1999] gives an algorithm for computing the product of two interval matrices using eight matrix products.

A square interval matrix $[ A ]$ is called nonsingular if it does not contain a singular matrix. An interval linear system is a system of the form $[ A ] x = [ b ]$ ,where $A$ is a nonsingular interval matrix and $b$ an interval vector. The solution set of such an interval linear system is the set

$$
{ \mathcal { X } } = \{ x \mid A x = b , A \in [ A ] , b \in [ b ] \} .
$$

Computing this solution set can be shown to be an intractable (NP-complete) problem. Even for a $2 \times 2$ linear system, this set may not be easy to represent.

An efficient and easy-to-use MATLAB toolbox called INTLAB (INTerval LABoratory) has been developed by Rump [944,1999]. It contains many useful subroutines and allows verified solutions of linear least squares problems to be computed.

# 1.4.2- Rounding Errors in Matrix Operations

By repeatedly using the formula for floating-point multiplication,one can show that the com-puted product $f l ( x _ { 1 } x _ { 2 } \cdot \cdot \cdot x _ { n } )$ is exactly equal to

$$
x _ { 1 } x _ { 2 } ( 1 + \epsilon _ { 2 } ) x _ { 3 } ( 1 + \epsilon _ { 3 } ) \cdot \cdot \cdot x _ { n } ( 1 + \epsilon _ { n } ) ,
$$

where $| \epsilon _ { i } | \le \mathbf { u } , i = 2 , 3 , \dots , n$ .This can be interpreted as a backward error analysis; we have shown that the computed product is the exact product of factors $x _ { 1 }$ ， $\tilde { x } _ { i } = x _ { i } ( 1 { + } \epsilon _ { i } )$ ， $i = 2 , \ldots , n$ It also follows from this analysis that

$$
| f l ( x _ { 1 } x _ { 2 } \cdots x _ { n } ) - x _ { 1 } x _ { 2 } \cdots x _ { n } | \leq \delta | x _ { 1 } x _ { 2 } \cdots x _ { n } | ,
$$

where $\delta = ( 1 + \mathbf { u } ) ^ { n - 1 } - 1 < 1 . 0 6 ( n - 1 ) \mathbf { u }$ ，and the last inequality holds if the condition $( n \mathrm { ~ - ~ } 1 )  { \mathbf { u } } \mathrm { ~ < ~ } 0 . 1$ is satisfied. This bounds the forward error in the computed result. Similar results can easily be derived for basic vector and matrix operations; see Wilkinson [1120, $1 9 6 5$ ，pp.114-118].

In the following we mainly use notation due to Higham [623, 2oo2, Sect. 3.4]. Let $| \delta _ { i } | \leq \mathbf { u }$ and $\rho _ { i } = \pm 1$ ， $i = 1 { : } n$ If $n \mathbf u < 1$ ,then

$$
\prod _ { i = 1 } ^ { n } ( 1 + \delta _ { i } ) ^ { \rho _ { i } } = 1 + \theta _ { n } , \quad | \theta _ { n } | < \gamma _ { n } , \quad \gamma _ { n } = \frac { n \mathbf { u } } { 1 - n \mathbf { u } } .
$$

With the realistic assumption that $n \mathbf { u } < 0 . 1$ ,it holds that $\gamma _ { n } < 1 . 0 6 n \mathbf { u }$ .Often it can be assumed that $n \mathbf u \ll 1$ , and we can set $\gamma _ { n } = n \mathbf { u }$ . When it is not worth the trouble to keep precise track of constants in the $\gamma _ { k }$ terms,we use Higham's notation

$$
\tilde { \gamma } _ { n } \equiv \frac { c n \mathbf { u } } { 1 - c n \mathbf { u } } ,
$$

where $c$ denotes a small integer constant whose exact value is unimportant.

If the inner product $x ^ { T } y = x _ { 1 } y _ { 1 } + x _ { 2 } y _ { 1 } + \cdot \cdot \cdot + x _ { n } y _ { n }$ is accumulated from left to right, repeated use of (1.4.4) gives

$$
f l \left( x ^ { T } y \right) = x _ { 1 } y _ { 1 } ( 1 + \delta _ { 1 } ) + x _ { 2 } y _ { 2 } ( 1 + \delta _ { 2 } ) + \cdot \cdot \cdot + x _ { n } y _ { n } ( 1 + \delta _ { n } ) ,
$$

where $| \delta _ { 1 } | < \gamma _ { n }$ ， $| \delta _ { i } | < \gamma _ { n + 2 - i }$ ， $i = 2 , \ldots , n$ . This gives the forward error bound

$$
| f l \left( x ^ { T } y \right) - x ^ { T } y | < \gamma _ { n } | x _ { 1 } | | y _ { 1 } | + \sum _ { i = 2 } ^ { n } \gamma _ { n + 2 - i } | x _ { i } | | y _ { i } | < \gamma _ { n } | x | ^ { T } | y | ,
$$

where $| x | , | y |$ denote vectors with elements $| x _ { i } | , | y _ { i } |$ . Note that the error magnitudes depend on the order of evaluation. The last upper bound in (1.4.11) holds independently of the summation order and is also valid for floating-point computation with no guard digit rounding. The corresponding backward error bounds

$$
f l \ ( x ^ { T } y ) = ( x + \Delta x ) ^ { T } y = x ^ { T } ( y + \Delta y ) , \quad | \Delta x | \leq \gamma _ { n } | x | , \quad | \Delta y | \leq \gamma _ { n } | y |
$$

also hold for any order of evaluation. This result is easily generalized to yield a forward error analysis of matrix-matrix multiplication. However,for this case there is no backward error analy-sis, because the rows and columns of the two matrices participate in several inner products! For the outer product $x y ^ { T }$ of two vectors $x , y \in \mathbb { R } ^ { n }$ we have $f l \left( x _ { i } y _ { j } \right) = x _ { i } y _ { j } ( 1 + \delta _ { i j } ) , | \delta$ $| \delta _ { i j } | \leq \mathbf { u }$ and so

$$
| f l \left( x y ^ { T } \right) - x y ^ { T } | \leq \mathbf { u } | x y ^ { T } | .
$$

This is a satisfactory result for many purposes. However, the computed result is usually not a rank-one matrix. In general, it is not possible to find perturbations $\Delta x$ and $\Delta y$ such that $f l ( x y ^ { T } ) = ( x + \Delta x ) ( y + \Delta y ) ^ { T }$

In many matrix algorithms, expressions of the form

$$
y = \left( c - \sum _ { i = 1 } ^ { k - 1 } a _ { i } b _ { i } \right) \Big / { d }
$$

occur repeatedly. A simple extension of the roundoff analysis of an inner product shows that if the term $c$ is added last, then the computed $\bar { y }$ satisfies

$$
\bar { y } d ( 1 + \delta _ { k } ) = c - \sum _ { i = 1 } ^ { k - 1 } a _ { i } b _ { i } ( 1 + \delta _ { i } ) ,
$$

where $| \delta _ { 1 } | \leq \gamma _ { k - 1 }$ ， $| \delta _ { i } | \le \gamma _ { k + 1 - i }$ ， $i = 2 , \ldots , k - 1$ ,and $| \delta _ { k } | \le \gamma _ { 2 }$ . The result is formulated so that $c$ is not perturbed. The forward error satisfes

$$
\left| { \bar { y } } d - \left( c - \sum _ { i = 1 } ^ { k - 1 } a _ { i } b _ { i } \right) \right| \leq \gamma _ { k } \left( | { \bar { y } } d | + \sum _ { i = 1 } ^ { k - 1 } | a _ { i } | | b _ { i } | \right) ,
$$

and this inequality holds for any summation order.

From the error analysis of inner products,error bounds for matrix-vector and matrix-matrix products can easily be obtained. Suppose $A \in \mathbb { R } ^ { m \times n }$ ， $x \in \mathbb { R } ^ { n }$ ,and $y = A x$ Then $y _ { i } = a _ { i } ^ { T } x$ ， where $a _ { i } ^ { T }$ is the $i$ th row of $A$ .From (1.4.12) we have $f l \left( { { a } _ { i } ^ { T } } x \right) = { { \left( { { a } _ { i } } + \Delta { { a } _ { i } } \right) } ^ { T } } y .$ ，where $| \Delta a _ { i } | \leq$ $\gamma _ { n } | a _ { i } |$ , giving the backward error result

$$
f l \left( A x \right) = { { \left( A + \Delta A \right) } x } , \quad \left| \Delta A \right| \leq \gamma _ { n } | A | ,
$$

where the inequality is to be interpreted elementwise.

Consider the matrix product $C = A B$ ,where $A \in \mathbb { R } ^ { m \times n }$ and $B = ( b _ { 1 } , \ldots , b _ { p } ) \in \mathbb { R } ^ { n \times p }$ .By (1.4.16), we have

$$
f l \left( A b _ { j } \right) = ( A + \Delta _ { j } ) b _ { j } , \quad \vert \Delta _ { j } A \vert \leq \gamma _ { n } \vert A \vert .
$$

Hence each computed column $c _ { j }$ in $C$ has a small backward error. The same cannot be said for $C = A B$ as a whole, because the perturbation of $A$ depends on $j$ .For the forward error we get the bound

$$
| f l \left( A B \right) - A B | \leq \gamma _ { n } | A | | B | ,
$$

and it follows that $\left\| f l \left( A B \right) - A B \right\| \leq \gamma _ { n } \left\| \left| A \right| \right\| \left\| \left| B \right| \right\|$ . Hence for any absolute norm, such as $\ell _ { 1 } , \ell _ { \infty }$ ,and Frobenius norms,it holds that

$$
\left\| f l \left( A B \right) - A B \right\| \leq \gamma _ { n } \left\| A \right\| \left\| B \right\| .
$$

For the $\ell _ { 2 }$ -norm the best upper bound is $\| f l \left( A B \right) - A B \| _ { 2 } < n \gamma _ { n } \| A \| _ { 2 } \| B \| _ { 2 }$ ,unless $A$ and $B$ have only nonnegative elements.The rounding error results here are formulated for real arithmetic. Similar bounds hold for complex arithmetic provided the constants in the bounds are increased appropriately.

# 1.4.3 - Stability of Matrix Algorithms

Consider a finite algebraic algorithm that from data $a = ( a _ { 1 } , \ldots , a _ { r } ) $ computes the solution $f = ( f _ { 1 } , \dots , f _ { s } )$ . In a forward error analysis one attempts to bound some norm of the error $| { \hat { f } } - f |$ in the computed solution $\hat { f } _ { i }$ . An algorithm is said to be forward stable (or acceptableerror stable) if for some norm $\| \cdot \|$ the computed solution $\bar { f }$ satisfies

$$
\| { \bar { f } } - f \| \leq c \kappa \mathbf { u } ,
$$

where $c$ is a not-too-large constant and $\kappa$ is the condition number of the problem from a perturbation analysis. Clearly this is a weaker form of stability.

Backward error analysis for matrix algorithms was pioneered by J. H. Wilkinson in the late 1950s. When it applies, it tends to be markedly superior to forward analysis.In a backward error analysis one attempts to show that for some class of input data,the algorithm computes a solution $\hat { f }$ that is the exact solution corresponding to a modified set of data $\tilde { a } _ { i }$ close to the original data $a _ { i }$ . There may be an infinite number of such sets,but it can also happen that no such set exists. An algorithm is said to be backward stable if for some norm $\| \cdot \|$ ，

$$
\| \tilde { \boldsymbol { a } } - \boldsymbol { a } \| < c \mathbf { u } \| \boldsymbol { a } \| ,
$$

where $c$ is a not-too-large constant. Backward error analysis usually gives better insight into the stability (or lack thereof)of the algorithm, which often is the primary purpose of an error analysis. Notice that no reference is made to the exact solution for the original data. A backward stable algorithm is guaranteed to give an accurate solution only if the problem is wel-conditioned. To yield error bounds for the solution, the backward error analysis has to be complemented with a perturbation analysis. It can only be expected that the error satisfies an inequality of the form (1.4.19).Nevertheless,if the backward error is within the uncertainties of the given data, it can be argued that the computed solution is as good as the data warrants. From the error bound (1.4.15) it is straightforward to derive a bound for the backward error in solving a triangular system of equations.

Theorem 1.4.1. If the lower triangular system $L x = b $ $L \in \mathbb { R } ^ { n \times n }$ is solved by forward substitution, the computed solution $\bar { y }$ is the exact solution of $( L + \Delta L ) \bar { x } = b$ , where for $i = 1 , \ldots , n ,$

$$
| \Delta l _ { i j } | \le \left\{ \begin{array} { l l } { \gamma _ { 2 } | l _ { i j } | } & { i f j = i , } \\ { \gamma _ { i - j } | l _ { i j } | } & { i f j < i , } \end{array} \right.
$$

where $\gamma _ { n } = n \mathbf { u } / ( 1 - n \mathbf { u } )$ Hence $| \Delta L | \leq \gamma _ { n } | L |$ for any summation order:

Proof. See Higham [623, 2002, Theorem 8.3].

A similar result holds for the computed solution of an upper triangular system.We conclude that the algorithm for solving triangular systems by forward orbackward substitution is backward stable.More precisely,we callthe algorithm componentwise backward stable, because (1.4.20) bounds the perturbations in $L$ componentwise.Note that it is not necessary to perturb the righthand side $b$

Often the data matrix $M$ belongs to a class $\mathcal { M }$ of structured matrices, such as Toeplitz matrices (see Section 4.5.5) or the augmented system matrix

$$
M = \left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) .
$$

An algorithm for solving $M x = b$ ， $M \in \mathcal { M }$ ，is strongly backward stable if it computes an exact solution of a system $\bar { M } x = \bar { b }$ ，where $\bar { M } \in \mathcal { M }$ ，and $\bar { M }$ and $\bar { b }$ are close to $M$ and $b$ see Bunch [185,1987]. For many classes of structured problems, strongly backward stable methods do not exist, but there are algorithms that can be proved to give a solution close to the exact answer of some relevant nearby system.

Chapter 2

# Basic Numerical Methods

# 2.1 - The Method of Normal Equations

# 2.1.1 - Introduction

The classical method used by Gaus for solving linear least squares problems

$$
\operatorname* { m i n } _ { \boldsymbol { x } } \| \boldsymbol { A } \boldsymbol { x } - \boldsymbol { b } \| _ { 2 } , \quad \boldsymbol { A } \in \mathbb { R } ^ { m \times n } ,
$$

is to form and solve the normal equations $A ^ { T } A x = A ^ { T } b$ If $A$ has full column rank, then $A ^ { T } A$ is positive definite and hence nonsingular. Gauss developed an elimination method for solving the normal equations that uses pivots chosen from the diagonal; see Stewart [1028,1995]. Then all reduced matrices are symmetric,and the storage and number of needed operations are reduced by half. Later, the preferred way to organize this elimination algorithm was to use Cholesky factorization, named after André-Louis Cholesky (1875-1918). The accuracy of the computed least squares solution using the normal equations depends on the square of the condition number of $A$ . Indeed, accuracy may be lost already when forming $A ^ { T } A$ and $A ^ { T } b$ ，Hence,the method of normal equations works well only for well-conditioned problems or when modest accuracy is required. Otherwise,algorithms based on orthogonalization should be preferred.

Much of the background theory on the matrix algorithms in this chapter is given in the excellent textbook of Stewart [1030,1998]. Accuracy and stability properties of matrix algorithms are admirably covered by Higham [623,2002].

# 2.1.2 - Forming the Normal Equations

The first step in the method of normal equations is to form

$$
C = A ^ { T } A \in \mathbb { R } ^ { n \times n } , \qquad d = A ^ { T } b \in \mathbb { R } ^ { n } .
$$

Given the symmetry of $C$ , it suffices to compute the $\textstyle { \frac { 1 } { 2 } } n ( n + 1 )$ elements of its upper triangular part (say). If $m \geq n$ , this number is always less than the mn elements in $A \in \mathbb { R } ^ { m \times n }$ . Hence, forming the normal equations can be viewed as data compression,in particular when $m \gg n$ If $A = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ , the elements of $C$ and $d$ can be expressed in inner product form as

$$
c _ { j k } = a _ { j } ^ { T } a _ { k } , \qquad d _ { j } = a _ { j } ^ { T } b , \quad 1 \leq j \leq k \leq n .
$$

If $A$ is instead partitioned by rows $\widetilde { a } _ { i }$ ， $i = 1 , \ldots , m$ ,a row-oriented algorithm is obtained:

$$
C = \sum _ { i = 1 } ^ { m } \widetilde { a } _ { i } \widetilde { a } _ { i } ^ { T } , \qquad d = \sum _ { i = 1 } ^ { m } b _ { i } \widetilde { a } _ { i } .
$$

This expresses $C$ as a sum of $m$ matrices of rank one and $d$ as a linear combination of the rows of $A$ . It has the advantage that only one pass through the data $A$ and $b$ is required,and it can be used to update the normal equations when equations are added or deleted. For a dense matrix, both schemes require $m n ( n + 1 )$ floating-point operations or flops,but the outer product form requires more memory access. When $A$ is sparse, zero elements in $A$ can more easily be taken into account by the outer product scheme. If the maximum number of nonzero elements in a row of $A$ is $p$ , then the outer product scheme only requires $m ( p + 1 ) ^ { 2 }$ flops. Note that the flop count only measures the amount of arithmetic work of a matrix computation but is often not an adequate measure of the overall complexity of the computation.

Rounding errors made in forming the normal equations can be obtained from the results in Section 1.4.2 for floating-point arithmetic. The computed elements in $C = A ^ { T } A$ are

$$
\bar { c } _ { i j } = \sum _ { k = 1 } ^ { m } a _ { i k } a _ { j k } ( 1 + \delta _ { k } ) , \quad | \delta _ { k } | < 1 . 0 6 ( m + 2 - k ) \mathbf { u } ,
$$

where $\mathbf { u }$ is the unit roundoff. It follows that the computed matrix satisfes $\bar { C } = C + E$ where

$$
\begin{array} { r } { | e _ { i j } | < 1 . 0 6 m \mathbf { u } | a _ { i } | ^ { T } | a _ { j } | \leq 1 . 0 6 m \mathbf { u } \| a _ { i } \| _ { 2 } \| a _ { j } \| _ { 2 } . } \end{array}
$$

A similar estimate holds for the rounding errors in the computed vector $A ^ { T } b$ . It is important to note that the rounding errors in forming $A ^ { T } A$ are in general not equivalent to small perturbations of the initial data matrix $A$ , i.e., it is not true that $\bar { C } = ( A + E ) ^ { T } ( A + E )$ for some small error matrix $E$ .Furthermore,forming the normal equations squares the condition number:

$$
\kappa ( C ) = \kappa ^ { 2 } ( A ) .
$$

Therefore methods that form the normal equations explicitly are not backward stable.

Example 2.1.1. A simple example where information is lost when $A ^ { T } A$ is formed is the matrix studied by Läuchli [724,1961]:

$$
A = \left( \begin{array} { c c c } { { 1 } } & { { 1 } } & { { 1 } } \\ { { \epsilon } } & { { } } & { { } } \\ { { } } & { { \epsilon } } & { { } } \\ { { } } & { { } } & { { \epsilon } } \end{array} \right) , \qquad A ^ { T } A = \left( \begin{array} { c c c } { { 1 + \epsilon ^ { 2 } } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { 1 + \epsilon ^ { 2 } } } & { { 1 } } \\ { { 1 } } & { { 1 } } & { { 1 + \epsilon ^ { 2 } } } \end{array} \right) .
$$

Assume that $\epsilon = 1 0 ^ { - 8 }$ and that six decimal digits are used for the elements of $A ^ { T } A$ Then, because $1 + \epsilon ^ { 2 } = 1 + 1 0 ^ { - 1 6 }$ is rounded to 1 even in IEEE double precision,all information contained in the last three rows of $A$ is irretrievably lost. □

Sometimes an unsuitable formulation of the problem will cause the least squares problem to be il-conditioned. Then a different choice of parametrization may significantly reduce the ill-conditioning. For example,in regression problems one should try to use orthogonal or nearly orthogonal base functions. Consider, for example,a linear regression problem for fiting a linear model $y = \alpha + \beta t$ to the given data $( y _ { i } , t _ { i } )$ ， $i = 1 , \ldots , m$ ．This isa least squares problem

$\mathrm { m i n } _ { x } \| A x - y \| _ { 2 }$ ,where $x = ( \alpha , \beta ) ^ { T }$ ,and

$$
A = \left( e \quad t \right) = \left( \begin{array} { c c } { { 1 } } & { { t _ { 1 } } } \\ { { 1 } } & { { t _ { 2 } } } \\ { { \vdots } } & { { \vdots } } \\ { { 1 } } & { { t _ { m } } } \end{array} \right) , \qquad y = \left( \begin{array} { c c } { { y _ { 1 } } } \\ { { y _ { 2 } } } \\ { { \vdots } } \\ { { y _ { m } } } \end{array} \right) .
$$

The corresponding normal equations can be written as

$$
\left( \begin{array} { l l } { { m } } & { { e ^ { T } t } } \\ { { e ^ { T } t } } & { { t ^ { T } t } } \end{array} \right) \left( \begin{array} { l } { { \alpha } } \\ { { \beta } } \end{array} \right) = \left( \begin{array} { l } { { e ^ { T } y } } \\ { { y ^ { T } t } } \end{array} \right) .
$$

The solution is

$$
\boldsymbol { \beta } = \frac { m ( \boldsymbol { y } ^ { T } t ) - ( e ^ { T } t ) ( e ^ { T } \boldsymbol { y } ) } { m ( t ^ { T } t ) - ( e ^ { T } t ) ^ { 2 } } , \qquad \boldsymbol { \alpha } = ( e ^ { T } \boldsymbol { y } - \boldsymbol { \beta } e ^ { T } t ) / m .
$$

Note that the mean values of the data $\bar { y } = e ^ { T } y / m$ ， $\bar { t } = e ^ { T } t / m$ lie on the fitted line, that is, $\alpha + \beta \bar { t } = \bar { y }$

A more accurate formula for $\beta$ is obtained by centering the data, i.e., by making the change of variables $\widetilde { y } _ { i } = y _ { i } - \bar { y } , \widetilde { t } _ { i } = t _ { i } - \bar { t } , i = 1 , \dots , \stackrel { \_ } { m }$ ,and writing the model as $\widetilde y = \beta \hat { t }$ . In the new variables, $e ^ { T } \widetilde t = 0$ and $e ^ { T } \widetilde { y } = 0$ Hence thematrix ofnormalequations isdagonal,andwe get

$$
\beta = \widetilde { y } ^ { T } \widetilde { t } / \widetilde { t } ^ { T } \widetilde { t } .
$$

When the elements in $A$ and $b$ are the original data,ill-conditioning cannot be avoided,as in the above example,by choosing another parametrization. The method of normal equations works well for well-conditioned problems or when only modest accuracy is required. However, the accuracy of the computed solution will depend on the square of the condition number of $A$ In view of the perturbation result in Theorem 1.3.14,this is not consistent with the sensitivity of smal-residual problems,and the method of normal equations can introduce errors much greater than those of a backward stable algorithm. For less severely il-conditioned problems,this can be offset by iterative refinement; see Section 2.5.3. Otherwise,algorithms that use orthogonal transformations and avoid forming $A ^ { T } A$ should be used; see Section 2.2.

# 2.1.3 - Algorithms for Cholesky Factorization

The Cholesky factorization is the preferred way to organize the elimination algorithm for the normal equations.3 By Theorem 1.2.1, for any symmetric positive definite matrix $C \in \mathbb { R } ^ { n \times n }$ there exists a unique Cholesky factorization

$$
{ \cal C } = { \cal R } ^ { T } { \cal R } ,
$$

where $R = \left( r _ { i j } \right)$ is upper triangular with positive diagonal elements.Writen componentwise, this is $n ( n + 1 ) / 2$ equations

$$
c _ { i j } = r _ { i i } r _ { i j } + \sum _ { k = 1 } ^ { i - 1 } r _ { k i } r _ { k j } , \quad 1 \leq i \leq j \leq n ,
$$

for the $n ( n { + } 1 ) / 2$ unknown elements in $R$ . If properly sequenced,(2.1.6) can be used to compute $R$ . An element $r _ { i j }$ can be computed from equation (2.1.6) provided $r _ { i i }$ and the elements $r _ { k i }$ ， $r _ { k j }$ ， $k < i$ ,are known. It follows that one way is to compute $R$ column by column from left to right as in the proof of Theorem 1.2.1. Such an algorithm is_called left-looking.Let $C _ { k } \in \mathbb { R } ^ { k \times k }$ be the $k$ th leading principal submatrix of $C$ .If $C _ { k - 1 } = R _ { k - 1 } ^ { H } R _ { k - 1 }$ ,then

$$
\begin{array} { r } { C _ { k } = \left( \begin{array} { c c } { C _ { k - 1 } } & { d _ { k } } \\ { d _ { k } ^ { T } } & { \gamma _ { k } } \end{array} \right) = \left( \begin{array} { c c } { R _ { k - 1 } ^ { H } } & { 0 } \\ { r _ { k } ^ { H } } & { \rho _ { k } } \end{array} \right) \left( \begin{array} { c c } { R _ { k - 1 } } & { r _ { k } } \\ { 0 } & { \rho _ { k } } \end{array} \right) } \end{array}
$$

implies that

$$
R _ { k - 1 } ^ { H } r _ { k } = d _ { k } , \qquad \rho _ { k } ^ { 2 } = \gamma _ { k } - r _ { k } ^ { H } r _ { k } .
$$

Hence, the $k$ th step of columnwise Cholesky factorization requires the solution of a lower tri-angular system. The algorithm requires approximately ${ \scriptstyle { \frac { 1 } { 3 } } } n ^ { 3 }$ flops and $n$ square roots. Only the elements in the upper triangular part of $C$ are referenced, and $R$ can overwrite $C$

# Algorithm 2.1.1 (Columnwise Cholesky).

function $\mathtt { R } \ =$ cholc(C);   
$\%$ CHOLC computes the Cholesky factor $\mathtt { R } \ = \ ( \mathtt { r } ( \mathtt { i } , \mathtt { j } ) )$ $\%$ of the positive definite Hermitian matrix C in $\%$ columnwise order.   
$\%$   
$\mathrm { ~ n ~ } =$ size(C,1)； R = zeros(n,n);   
${ \tt R } \left( 1 , 1 \right) \ = \ { \tt s q r t } \left( { \tt C } \left( 1 , 1 \right) \right)$ ；   
for ${ \mathfrak { j } } ~ = ~ 2 { : } { \mathtt { n } }$ $\%$ Compute the j:th column of R. $\texttt { I } = \texttt { 1 : j - 1 }$ ； %I is index set   
$\begin{array} { r l } { \mathrm { R } ( \mathrm { I } , \mathrm { j } ) } & { = \mathrm { \sf ~ R } ( \mathrm { I } , \mathrm { I } ) \ddot { \bf \Xi } \backslash \mathtt { C } ( \mathrm { I } , \mathrm { j } ) ; } \\ { \mathrm { R } ( \mathrm { j } , \mathrm { j } ) } & { = \mathrm { \sf ~ s q r t } ( \mathrm { C } ( \mathrm { j } : \mathrm { j } ) - \mathrm { \sf ~ R } ( \mathrm { I } , \mathrm { j } ) \ ' _ { \ast \mathrm { R } ( \mathrm { I } , \mathrm { j } ) ) } ; } \end{array}$   
end

A second variant computes in step $k = 1 , \dots , n$ the elements in the $k$ th row of $R$ .This is a rowwise or right-looking algorithm. The arithmetic work is dominated by matrix-vector products.

# Algorithm 2.1.2 (Rowwise Cholesky).

function R = cholr(C);   
$\%$ CHOLR computes the Cholesky factor $\mathtt { R } \ = \ ( \mathtt { r } ( \mathtt { i } , \mathtt { j } ) )$ of the   
$\%$ positive definite Hermitian matrix C in rowwise order.   
$\%$   
$\mathrm { ~ n ~ } =$ size(C,1)； R = zeros(n,n);   
for $\dot { \mathrm { ~ \scriptsize ~ 1 ~ } } = \dot { \mathrm { ~ \scriptsize ~ 1 ~ } } : \mathtt { n }$ % Compute the i:th row of R. if $\dot { \mathrm { ~ \scriptsize ~ 1 ~ } } > \mathrm { ~ \scriptsize ~ 1 ~ }$ ， $\mathrm { ~ s ~ } ( \mathrm { i } : \mathrm { n } ) ~ = ~ \mathrm { C } \left( \mathrm { i } , \mathrm { i } : \mathrm { n } \right) ~ - ~ \mathrm { R } \left( 1 : \mathrm { i } - 1 , \mathrm { i } \right) { } ^ { \prime } \ast \mathrm { R } \left( 1 : \mathrm { i } - 1 , \mathrm { i } : \mathrm { n } \right) ;$ end $\begin{array} { l } { { \mathrm { R } \left( \mathrm { i } , \mathrm { i } \right) \ = \ \mathsf { s q r t } \left( \mathrm { s } \left( \mathrm { i } \right) \right) \mathrm { ; } } } \\ { { \mathrm { R } \left( \mathrm { i } \ , \mathrm { i } + \mathrm { 1 } : \mathrm { n } \right) \ = \ \mathrm { s } \left( \mathrm { i } + \mathrm { 1 } : \mathrm { n } \right) / \mathrm { R } \left( \mathrm { i } \ , \mathrm { i } \right) \mathrm { ; } } } \end{array}$   
end

It is simple to modify the Cholesky algorithms so that they instead compute a factorization of the form $C = R ^ { T } D R$ ，where $D$ is diagonal and $R$ unit upper triangular. This factorization requires no square roots and may therefore be slightly faster. The two algorithms above are numerically equivalent, i.e., they compute the same factor $R$ ,even taking rounding errors into account. A normwise error analysis is given by Wilkinson [1121,1968].

Taking $i = j$ in (2.1.6) gives $\begin{array} { r } { c _ { i i } = \sum _ { k = 1 } ^ { i } \dot { r } _ { k i } ^ { 2 } } \end{array}$ ， $i = 1 , \ldots , n$ It follws that

$$
c _ { i i } \geq \operatorname* { m a x } _ { 1 \leq k \leq j } | r _ { k j } | ^ { 2 } , \quad i = 1 , \ldots , n .
$$

Hence,the elements in $R$ are bounded in size by the square root of the maximum diagonal elements in $C$ . This shows the numerical stability of Cholesky factorization.

Theorem 2.1.2. Let $C \in R ^ { n \times n }$ be a symmetric positive definite matrix such that

$$
2 n ^ { 3 / 2 } { \bf u } \kappa ( C ) < 0 . 1 .
$$

Then the Cholesky factor of $C$ can be computed without breakdown, and the computed $\bar { R }$ satisfies

$$
\bar { R } ^ { T } \bar { R } = C + E , \quad \| E \| _ { 2 } < 2 . 5 n ^ { 3 / 2 } { \bf u } \| C \| _ { 2 } .
$$

A componentwise result is given by Demmel [303,1989].

Theorem 2.1.3. If Cholesky factorization applied to the symmetric positive definite matrix $C \in$ $R ^ { n \times n }$ runs to completion, then the computed factor $\overline { { R } }$ satisfies

$$
\begin{array} { r } { \overline { { R } } ^ { T } \overline { { R } } = C + E , \quad | E | \leq \gamma _ { n + 1 } ( 1 - \gamma _ { n + 1 } ) d d ^ { T } , } \end{array}
$$

where $d _ { i } = c _ { i i } ^ { - 1 / 2 }$ and $\gamma _ { k } = k \mathbf { u } / ( 1 - k \mathbf { u } )$

These results show that the given algorithms for computing the Cholesky factor $R$ from $C$ are backward stable. The error in the computed Cholesky factor will affect the error in the least squares solution $\bar { x }$ computed by the method of normal equations. When $C = A ^ { T } A$ ， $\kappa ( C ) = \kappa ^ { 2 } ( A )$ ,and this squaring of the condition number implies that the Cholesky algorithm may break down,and roots of negative numbers may arise when $\kappa ( A )$ is of the order of $1 / \sqrt { \mathbf { u } }$ Rounding errors in the solution of the triangular systems $R ^ { T } R x = A ^ { T } b$ are usually negligible; see Higham [615,198g]. From Theorem 2.1.2 it follows that the backward error in the computed solution $\bar { x }$ caused by the Cholesky factorization satisfies

$$
( A ^ { T } A + E ) \bar { x } = A ^ { T } b , \quad \| E \| _ { 2 } < 2 . 5 n ^ { 3 / 2 } { \bf u } \| A \| _ { 2 } ^ { 2 } .
$$

A perturbation analysis shows that

$$
\| \bar { \boldsymbol { x } } - \boldsymbol { x } \| _ { 2 } \leq 2 . 5 n ^ { 3 / 2 } \mathbf { u } \kappa ^ { 2 } ( \boldsymbol { A } ) \| \boldsymbol { x } \| _ { 2 } .
$$

The squared condition number shows that the method of normal equations is not a backward stable method for solving a least squares problem.

# 2.1.4 - Conditioning and Scaling Invariance

In a linear system $A x = b$ the unknowns $x _ { j }$ ， $i = 1 , \ldots , n$ ,are often physical quantities. Changing the units in which these are measured is equivalent to scaling the columns of $A$ .If we also multiply each equation by a scalar, this corresponds to scaling the rows of $A$ and $b$ . The original system is then transformed into an equivalent system $A ^ { \prime } x ^ { \prime } = b ^ { \prime }$ ,where

$$
A ^ { \prime } = D _ { 2 } A D _ { 1 } , \quad b ^ { \prime } = D _ { 2 } b , \quad x = D _ { 1 } x ^ { \prime } .
$$

It seems natural to expect that such a scaling should have no effect on the relative accuracy of the computed solution. If the system is solved by Gaussian elimination or, equivalently, by LU factorization, this is in fact true,as shown by the following theorem due to Bauer [95,1966].

Theorem 2.1.4. Denote by $\bar { x }$ and ${ \bar { x } } ^ { \prime }$ the computed solution using $L U$ factorization in floating-point arithmetic to the two linear systems $A x = b$ and $( D _ { 2 } A D _ { 1 } ) x ^ { \prime } = D _ { 2 } b ,$ where $D _ { 1 }$ and $D _ { 2 }$ are diagonal scaling matrices. Ifno rounding errors are introduced by the scaling, and the same pivots are used, then $\bar { x } = D _ { 1 } \bar { x } ^ { \prime }$ holds exactly.

For a least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ , the column scaling $A D$ corresponds to a two-sided symmetric scaling $( A D ) ^ { T } A D = D C D$ of the normal equations matrix. Note that scaling the rows in $A$ is not allowed because this would change the LS objective function; see Section 3.2.1.

Cholesky factorization of $C = A ^ { T } A$ is a special case of LU factorization, and therefore by Theorem 2.1.4 it is numerically invariant under a diagonal scaling that preserves symmetry. Condition (2.1.10) in Theorem 2.1.2 can therefore be replaced by $\bar { 2 n ^ { 3 / 2 } \mathbf { u } ( \kappa ^ { \prime } ) ^ { 2 } } < \bar { 0 . 1 }$ ，where $\begin{array} { r } { \kappa ^ { \prime } ( A ) = \operatorname* { m i n } _ { D } \kappa ( A D ) , D > 0 , } \end{array}$ Furthermore,the error bound (2.1.13) for the computed solution by Cholesky factorization can be improved to

$$
\begin{array} { r } { \| \bar { x } - x \| _ { 2 } \leq 2 . 5 n ^ { 3 / 2 } \mathbf { u } \kappa ^ { \prime } ( A ) \kappa ( A ) \| x \| _ { 2 } . } \end{array}
$$

Note that these improvements hold without explicitly carrying out any scaling in the algorithm.

Theorem 2.1.5. Let $C \in \mathbb { R } ^ { n \times n }$ be symmetric and positive definite with at most $q \leq n$ nonzero elements in any row. If all diagonal elements in $C$ are equal, then

$$
\kappa ( C ) \leq q \operatorname* { m i n } _ { D > 0 } \kappa ( D C D ) ,
$$

where $D > 0$ denotes the set of all $n \times n$ diagonal matrices with positive entries.

Proof. See Higham [623, 2002, Theorem 7.5].

$C = A ^ { T } A$ and the columns of $A$ are scaled to have equal 2-norms, then $C$ ，then from Theorem 2.1.5 with $q = n$ ,it follows that

$$
\kappa ( A ) = { \sqrt { n } } \operatorname* { m i n } _ { D > 0 } \kappa ( A D ) .
$$

Hence, choosing $D$ so that the columns of $A D$ have equal length is a nearly optimal scaling.

Example 2.1.6. Sometimes the error in the solution computed by the method of normal equa-tions is much smaller than the error bound in (2.1.13). This is often due to poor column scaling, and the observed error bound is wel predicted by (2.1.15). Consider the least squares fiting of a polynomial

$$
p ( t ) = c _ { 0 } + c _ { 1 } t + \cdot \cdot \cdot + t ^ { n - 1 }
$$

to observations $y _ { i } = p ( t _ { i } )$ at points $t _ { i } = 0 , 1 , \ldots , m - 1$ . The resulting least squares problem is $\operatorname* { m i n } _ { c } \| A c - y \| _ { 2 }$ ,where $A \in \mathbb { R } ^ { m \times n }$ has elements

$$
a _ { i j } = ( i - 1 ) ^ { j - 1 } , \quad 1 \leq i \leq m , \quad 1 \leq j \leq n .
$$

For $m = 2 1$ and $n = 6$ ,the matrix is quite ill-conditioned: $\kappa ( A ) = 6 . 4 0 \cdot 1 0 ^ { 6 }$ However, the condition number of the scaled matrix $A D$ ，where all columns have unit length, is more than three orders of magnitude smaller: $\kappa ( A D _ { 1 } ) = 2 . 2 2 \cdot 1 0 ^ { 3 }$

# 2.1.5 - Computing the Covariance Matrix

In least squares problems it is often necessary to compute the associated covariance matrix in order to estimate the accuracy of the computed results. In particular, the variance of $x _ { i }$ is proportional to the $i$ th diagonal element of $( A ^ { T } A ) ^ { - 1 }$ . Let $A x = b + \epsilon$ $A \in \mathbb { R } ^ { m \times n }$ , be a full-rank linear model, where $\epsilon$ is a random vector with zero mean and covariance matrix $\sigma ^ { 2 } I$ Bythe Gauss-Markov theorem, the covariance matrix of the least squares estimate $\hat { x }$ is $\sigma ^ { 2 } C _ { x }$ ,where

$$
C _ { x } = ( A ^ { T } A ) ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T } .
$$

The inverse $S = R ^ { - 1 } = \left( s _ { i j } \right)$ is upper triangular and can be computed in $n ^ { 3 } / 3$ flops from the matrix equation $R S = I$ as follows:

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathrm { f o r ~ } j = n , n - 1 , \ldots , 1 } } \\ { { } } & { { } } & { { s _ { j j } = 1 / r _ { j j } ; } } \\ { { } } & { { } } & { { \mathrm { f o r ~ } i = j - 1 , \ldots , 2 , 1 } } \\ { { } } & { { } } & { { s _ { i j } = - \displaystyle \biggl ( \sum _ { k = i + 1 } ^ { j } r _ { i k } s _ { k j } \biggr ) \biggl / r _ { i i } ; } } \\ { { } } & { { } } & { { , } } \end{array}
$$

end

The computed elements of $S$ can overwrite the corresponding elements of $R$ in storage. Forming the upper triangular part of $C _ { x } = S S ^ { T }$ requires an additional $n ^ { 3 } / 3$ flops. This computation can be sequenced so that the elements of $C _ { x }$ overwrite those of $S$ . The variance of the components of $x$ is given by the diagonal elements of $C _ { x }$ ：

$$
c _ { n n } = s _ { n n } ^ { 2 } = 1 / r _ { n n } ^ { 2 } , \qquad c _ { i i } = \sum _ { j = i } ^ { n } s _ { i j } ^ { 2 } , \quad i = n - 1 , \ldots , 1 .
$$

Note that the variance for $x _ { n }$ is available directly from the last diagonal element $r _ { n n }$ The covariance matrix of the residual vector $\hat { r } = b - A \hat { x }$ is

$$
C _ { r } = ( I - A ( A ^ { T } A ) ^ { - 1 } A ^ { T } ) = ( I - Q _ { 1 } Q _ { 1 } ^ { T } ) , \quad Q _ { 1 } = A R ^ { - 1 } .
$$

Here $I - Q _ { 1 } Q _ { 1 } ^ { T }$ is the orthogonal projector onto the nullspace of $A ^ { T }$

An unbiased estimate of $\sigma ^ { 2 }$ in the Gauss-Markov model is given by

$$
s ^ { 2 } = \| \hat { r } \| _ { 2 } ^ { 2 } / ( m - n ) , \quad \hat { r } = b - A \hat { x } .
$$

The normalized residuals

$$
\boldsymbol { \tilde { r } } = ( s \mathrm { d i a g } C _ { r } ) ^ { - 1 / 2 } \boldsymbol { \hat { r } }
$$

are often used to detect and identify single or multiple bad data, which are assumed to correspond to large components in $\tilde { r }$

Often $C _ { x }$ occurs only as an intermediate quantity in a formula. For example, the variance of a linear functional $f ^ { T } \hat { x }$ is

$$
\begin{array} { r } { f ^ { T } C _ { x } f = f ^ { T } R ^ { - 1 } R ^ { - T } f = z ^ { T } z , } \end{array}
$$

where $z = R ^ { - T } f$ . Thus,the variance can be computed by solving the lower triangular system $R ^ { T } z = f$ and forming $z ^ { T } z$ . This is a more stable and efficient approach than using the expression $f ^ { T } C _ { x } f$

An algorithm for computing selected elements of $C _ { x }$ when $A$ is a band matrix is given in Section 4.1.3. This uses the identity $R C _ { x } = R ^ { - T }$ that follows from the definition (2.1.18).

# 2.2 - Orthogonalization Methods

# 2.2.1 - Householder and Givens Transformations

A rank-one modification of the unit matrix $E = I - \beta u v ^ { T }$ is called an elementary matrix. In particular,a matrix of the form

$$
P = I - \beta u u ^ { T } , \quad \beta = 2 / ( u ^ { T } u )
$$

is symmetric and orthogonal: $P ^ { T } = P$ and ${ \cal P } ^ { T } { \cal P } = I$ It follows that $P ^ { 2 } = I$ and hence $P ^ { - 1 } = P$ Note the similarity to an elementary orthogonal projection matrix; see (1.1.15). The product of $P$ with a given vector $a$ is

$$
P a = a - \beta ( u ^ { T } a ) u
$$

and can be found without explicitly forming $P$ itself. The effect of this transformation is that it reflects the vector $a$ in the hyperplane with normal vector $u$ ； see Figure 2.2.1. Note that $P a \in \operatorname { s p a n } \left\{ a , u \right\}$ and $P u = - u$ so that $P$ reverses $u$

![](images/3382f5f11d79e467c1f135d9cf34349585ee4d6c4a212643daf093fc155b064c.jpg)  
Figure 2.2.1. Reflection of a vector a in a hyperplane with normal u.

The use of orthogonal reflections in numerical linear algebra was initiated by Householder [644,1958]. Therefore,a matrix $P$ of the form (2.2.1) is also called a Householder reflector. The most common use of Householder reflectors is reducing a given vector $a$ to a multiple of the unit vector $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T }$ ：

$$
P a = a - \beta ( u ^ { T } a ) u = \pm \sigma e _ { 1 } .
$$

Since $P$ is orthogonal, we have $\sigma = \| a \| _ { 2 } \neq 0$ .From (2.2.2) it follows that $P a = \pm \sigma e _ { 1 }$ for

$$
u = a \mp \sigma e _ { 1 } .
$$

Furthermore, setting $\alpha _ { 1 } = a ^ { T } e _ { 1 }$ , we have

$$
\begin{array} { r } { \boldsymbol { u } ^ { T } \boldsymbol { u } = ( a \mp \sigma e _ { 1 } ) ^ { T } ( a \mp \sigma e _ { 1 } ) = \sigma ^ { 2 } \mp 2 \sigma \alpha _ { 1 } + \sigma ^ { 2 } = 2 \sigma ( \sigma \mp \alpha _ { 1 } ) , } \end{array}
$$

so that $1 / \beta = \sigma ( \sigma \mp \alpha _ { 1 } )$ .To avoid cancellation when $a$ is close to a multiple of $e _ { 1 }$ , the standard choice is to take

$$
u = a + \mathrm { s i g n } ( \alpha _ { 1 } ) \sigma e _ { 1 } , 1 / \beta = \sigma ( \sigma + | \alpha _ { 1 } | ) .
$$

This corresponds to choosing the outer bisector in the Householder reflector.

Given real vector $a \neq 0$ ,Algorithm 2.2.1 computes a Householder reflector $P = I - \beta u u ^ { T }$ ， where $u$ is normalized so that $u _ { 1 } = 1$ .If $n = 1$ or $a ( 2 : n ) = 0$ ,then $\beta = 0$ is returned.

# Algorithm 2.2.1 (Construct Householder Reflector).

function [u,beta,sigma] $=$ houseg(a) $\%$ Constructs a Householder reflector such $\%$ that (I - beta\*u\*u')a $=$ sigma\*e_1 % $\mathrm { ~ u ~ } = \mathrm { ~ a ~ } ;$ sigma $=$ norm(a); ${ \mathrm {  ~ u ~ } } ( 1 ) \ = \ { \mathrm { s i g m a } } \ + \ { \mathrm { a b s } } \left( { \mathrm { a } } \left( 1 \right) \right) ;$ beta $= \mathrm { ~ u ~ } ( 1 ) / \mathrm { s i g m a }$ if $\mathtt { a } \left( \mathtt { 1 } \right) \ < \ 0$ ${ \mathfrak { u } } ( 1 ) \ = \ - { \mathfrak { u } } ( 1 )$ ： else $\mathsf { \Gamma } _ { \mathsf { s i g m a } } = \mathsf { \Gamma } _ { - \mathsf { s i g m a } } ;$ end $\mathrm { ~ u ~ } = \mathrm { ~ u ~ } / \mathrm { u } \left( 1 \right)$ ；   
end

Householder reflections for use with complex vectors and matrices can be constructed as follows; see Wilkinson [1119,1965,pp. 49-50]. A complex Householder reflector has the form

$$
P = I - \beta u u ^ { H } , \quad \beta = \frac { 2 } { u ^ { H } u } , \quad u \in \mathbb { C } ^ { n } ,
$$

and is Hermitian and unitary $P ^ { H } = P$ ， $P ^ { H } P = I { \ u { r } }$ . Given $x \in \mathbb { C } ^ { n }$ such that $e _ { 1 } ^ { T } x = \xi _ { 1 } =$ $e ^ { i \alpha } | \xi _ { 1 } |$ , we want to determine $P$ so that

$$
P x = \gamma e _ { 1 } , \quad | \gamma | = \sigma = \| x \| _ { 2 } .
$$

Since $P$ is Hermitian, $x ^ { H } P x = \gamma x ^ { H } e _ { 1 } = \gamma \xi _ { 1 }$ must be real. It follows that $\gamma = \pm e ^ { i \alpha } \sigma$ To avoid cancellation in the first component of $u$ ,the sign is chosen so that

$$
u = x - \gamma e _ { 1 } , \quad \gamma = - e ^ { i \alpha } \sigma , \quad \beta = 1 / \sigma ( \sigma + | \xi _ { 1 } | ) ,
$$

and $\ P x = - e ^ { i \alpha } \sigma e _ { 1 }$ . Complex Householder transformations are discussed in more detail by Lehoucq [732,1996] and Demmel et al. [309,2008].

Householder matrices can be used to introduce zeros in a column or a row of a matrix $A \in$ $\mathbb { R } ^ { m \times n }$ . The product $P A$ can be computed as follows using only $\beta$ and the Householder vector $u$ ：

$$
P A = ( I - \beta u u ^ { T } ) A = A - \beta u ( u ^ { T } A ) .
$$

This requires $4 m n$ flops and alters $A$ by a matrix of rank one. Similarly, multiplication from the right is computed as

$$
A P = A ( I - \beta u u ^ { T } ) = A - \beta ( A u ) u ^ { T } .
$$

Another useful class of elementary orthogonal transformations are plane rotations,often called Givens rotations; see Givens [480,1958]. These have the form

$$
G = \left( \begin{array} { c c } { { c } } & { { s } } \\ { { - s } } & { { c } } \end{array} \right) , \quad c = \cos { \theta } , \quad s = \sin { \theta } ,
$$

and satisfy $G ^ { T } G = I$ and $\operatorname* { d e t } ( G ) = c ^ { 2 } + s ^ { 2 } = 1$ For a two-dimensional vector $v$ ， $G v$ represents a clockwise rotation through an angle $\theta$ . The matrix representing a two-dimensional rotation in

the plane spanned by the unit vectors $e _ { i }$ and $e _ { k } , i < k$ ,is a rank-two modification of the unit matrix $I _ { n }$ ：

$$
G _ { i k } = \left( \begin{array} { l l l l l l } & & { i } & & { k } & \\ { 1 } & & { \vdots } & & { \vdots } & \\ & { \ddots } & { \vdots } & & { \vdots } & \\ { \cdots } & { \cdots } & { c } & { \cdots } & { s } & { \cdots } & { \cdots } \\ & & { \vdots } & { \ddots } & { \vdots } & \\ { \cdots } & { \cdots } & { - s } & { \cdots } & { c } & { \cdots } & { \cdots } \\ & & { \vdots } & & { \vdots } & { \ddots } \\ & & { \vdots } & & { \vdots } & & { 1 } \end{array} \right) .
$$

Premultiplying a column vector $\boldsymbol { a } = ( \alpha _ { 1 } , \ldots , \alpha _ { n } ) ^ { T }$ by $G _ { i k }$ will affect only elements in rows $i$ and $j$ ：

$$
\left( { \begin{array} { l } { \alpha _ { i } ^ { \prime } } \\ { \alpha _ { k } ^ { \prime } } \end{array} } \right) = \left( { \begin{array} { l l } { c } & { s } \\ { - s } & { c } \end{array} } \right) \left( { \begin{array} { l } { \alpha _ { i } } \\ { \alpha _ { k } } \end{array} } \right) = \left( { \begin{array} { l } { c \alpha _ { i } + s \alpha _ { k } } \\ { - s \alpha _ { i } + c \alpha _ { k } } \end{array} } \right) .
$$

Any element in a vector or matrix can be annihilated by a plane rotation. For example, if in (2.2.12) we take

$$
c = { \alpha _ { i } } / { \sigma } , \quad s = { \alpha _ { k } } / { \sigma } , \quad \sigma = \sqrt { { \alpha _ { i } ^ { 2 } + { \alpha _ { k } ^ { 2 } } } } \ne 0 ,
$$

then $\alpha _ { i } ^ { \prime } = \sigma$ and $\alpha _ { k } ^ { \prime } = 0$ ，Premultiplication of $A \in \mathbb { R } ^ { m \times n }$ with a plane rotation $G _ { i k } \in \mathbb { R } ^ { m \times m }$ requires $6 n$ flops and only affects rows $i$ and $j$ in $A$ . Similarly, postmultiplying $A$ with $G _ { i j } \in$ $\mathbb { R } ^ { n \times n }$ will only change columns $i$ and $j$

A robust algorithm for computing $c , s$ and $\sigma$ in a plane rotation $G$ such that $G ( \alpha , \beta ) ^ { T } = \sigma e _ { 1 }$ to nearly full machine precision is given below. Note that the naive expression $\sigma = ( \alpha ^ { 2 } + \beta ^ { 2 } ) ^ { 1 / 2 }$ may produce damaging underflows and overflows even though the data and result are well within the range of the floating-point number system.

This algorithm requires two divisions,three multiplications,and one square root. No inverse trigonometric functions are involved. Overflow can only occur if the true value of $\sigma$ itself were to overflow.

# Algorithm 2.2.2 (Construct a Real Plane Rotation).

function [c,s,sigma] $=$ givrot(alpha,beta) % GIVR0T constructs a 2 by 2 real plane rotation $\%$ - if beta $\ c = ~ 0$ $\mathrm { ~  ~ c ~ } = \mathrm { ~  ~ 1 ~ } . 0 ; \mathrm { ~ \bf ~ s ~ } = \mathrm { ~  ~ 0 ~ } . 0 ;$ sigma $=$ alpha; elseif abs(beta) $>$ abs(alpha) t $=$ alpha/beta；tt $=$ sqrt(1+t\*t); s = 1/tt； $\mathrm { ~ \mathsf ~ { ~ c ~ } ~ } = \mathrm { ~ t * s ~ }$ ；sigma $=$ tt\*beta; else $\begin{array} { l } { \mathrm { ~ t ~ = ~ b e t a / a 1 p h a ; ~ \Delta ~ t t ~ = ~ s q r t ( 1 + t * t ) ~ } ; } \\ { \mathrm { ~ c ~ = ~ 1 / t t ; ~ \Delta ~ s ~ = ~ t * c } { \mathrm { ; ~ \Delta ~ s i g m a ~ = ~ t t * a 1 p h a } } } \end{array}$ end   
end

The standard task of mapping a given vector $x \in \mathbb { R } ^ { m }$ onto a multiple of $e _ { 1 }$ can be performed in different ways by a sequence of plane rotations. Let $G _ { i k }$ denote a plane rotation in the plane $( i , k )$ that zeros out the $k$ th component in a vector. Then one solution is to take

$$
G _ { 1 m } \cdot \cdot \cdot G _ { 1 3 } G _ { 1 2 } x = \sigma e _ { 1 } .
$$

Note that because $G _ { 1 k }$ only affects components 1 and $k$ , previously introduced zeros will not be destroyed later. Another possibility is to take

$$
G _ { 1 2 } G _ { 2 3 } \cdot \cdot \cdot G _ { n - 1 , n } a = \sigma e _ { 1 } ,
$$

where $G _ { k - 1 , k }$ is chosen to zero the $k$ th component. This flexibility of plane rotations compared to Householder reflections is particularly useful when operating on sparse matrices.

A plane rotation $G$ (or reflector) can be represented by $c$ and $s$ and need never be explicitly formed. Even more economical is to store either $c$ or $s$ ,whichever is smaller. Stewart [1016, 1976] devised a scheme in which the two cases are distinguished by storing the reciprocal of $c$ Then $c = 0$ has to be treated as a special case. If for the matrix (2.2.1O) we define

$$
\rho = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } c = 0 , } \\ { \operatorname { s i g n } { ( c ) } s } & { { \mathrm { i f ~ } } | s | < | c | , } \\ { \operatorname { s i g n } { ( s ) } / c } & { { \mathrm { i f ~ } } | c | \leq | s | , } \end{array} \right. }
$$

then the numbers $c$ and $s$ can be retrieved up to a common factor $\pm 1$ by

$$
\begin{array} { l } { { \mathrm { i f ~ } \rho = 1 , \mathrm { ~ t h e n ~ } c = 0 ; s = 1 ; } } \\ { { \mathrm { i f ~ } | \rho | < 1 , \mathrm { ~ t h e n ~ } s = \rho ; c = ( 1 - s ^ { 2 } ) ^ { 1 / 2 } ; } } \\ { { \mathrm { i f ~ } | \rho | > 1 , \mathrm { ~ t h e n ~ } c = 1 / \rho ; s = ( 1 - c ^ { 2 } ) ^ { 1 / 2 } . } } \end{array}
$$

This scheme is used because the formula $\sqrt { 1 - x ^ { 2 } }$ gives poor accuracy when $| x |$ is close to unity. An alternative to plane rotations favored by some are plane reflectors of the form

$$
\widetilde { G } = \left( \begin{array} { c c } { { c } } & { { s } } \\ { { s } } & { { - c } } \end{array} \right) , \quad c = \cos { \theta } , \quad s = \sin { \theta } ,
$$

for which $\operatorname* { d e t } ( \widetilde G ( \theta ) ) = - 1$ . These reflectors are symmetric and orthogonal, $\tilde { G } ^ { - 1 } = \tilde { G } =$ $\tilde { G } ^ { T }$ ,and represent a plane rotation followed by a reflection about an axis.From trigonometric identities,it follows that $\widetilde { G }$ equals the $2 \times 2$ Householder reflector

$$
\widetilde { G } = I - ( I - \widetilde { G } ) = I - 2 u u ^ { T } , \quad u = \left( { - \sin ( \theta / 2 ) } \right) .
$$

In the complex case a plane rotation has the form

$$
G = \left( \begin{array} { c c } { { \bar { c } } } & { { \bar { s } } } \\ { { - s } } & { { c } } \end{array} \right) , \quad | c | ^ { 2 } + | s | ^ { 2 } = 1 ,
$$

where $\bar { c }$ and $\bar { s }$ denote complex conjugates. Then

$$
G ^ { H } G = \left( { \begin{array} { c c } { c } & { - { \bar { s } } } \\ { s } & { { \bar { c } } } \end{array} } \right) \left( { \begin{array} { c c } { { \bar { c } } } & { { \bar { s } } } \\ { - s } & { c } \end{array} } \right) = \left( { \begin{array} { c c } { | c | ^ { 2 } + | s | ^ { 2 } } & { 0 } \\ { 0 } & { | c | ^ { 2 } + | s | ^ { 2 } } \end{array} } \right) = I ,
$$

which shows that $G$ is unitary. We want to construct $G$ so that

$$
G \left( { \begin{array} { l } { \alpha } \\ { \beta } \end{array} } \right) = \left( { \begin{array} { l } { \sigma } \\ { 0 } \end{array} } \right) .
$$

For efficiency, we want $c$ to be real also in the complex case. If $\alpha \neq 0$ and $\beta \neq 0$ ,this can be achieved by taking

$$
c = | \alpha | / ( \sqrt { | \alpha | ^ { 2 } + \beta | ^ { 2 } } ) , \qquad s = \mathrm { s i g n } ( \alpha ) \bar { \beta } / ( \sqrt { | \alpha | ^ { 2 } + \beta | ^ { 2 } } ) ,
$$

where $\sigma = \mathrm { s i g n } ( \alpha ) \sqrt { | \alpha | ^ { 2 } + \beta | ^ { 2 } }$ .Here $\mathrm { s i g n } \left( z \right) = z / | z |$ is defined for any complex $z \neq 0$ If$\alpha = 0$ and $\beta \neq 0$ ,we take

$$
c = 0 , \quad s = \operatorname { s i g n } { \bar { \beta } } ) , \quad \sigma = | \beta | .
$$

Finally, if $\alpha = \beta = 0$ , we take $c = 1$ ， $s = \sigma = 0$ . The efficient and reliable computation of $\sigma$ ， $c$ ,and $s$ in real and complex plane rotations is surprisingly complicated; see Bindel et al. [120, 2002].

So-called fast plane rotations were introduced by Gentleman [45O,1973l and Hammarling [563,1974]. Suppose that we want to perform the Givens transformation

$$
G A = \left( \begin{array} { l l } { \gamma } & { \sigma } \\ { - \sigma } & { \gamma } \end{array} \right) A , \qquad A = \left( \begin{array} { l l l l } { \alpha } & { a _ { 2 } } & { \ldots } & { a _ { n } } \\ { \beta } & { b _ { 2 } } & { \ldots } & { b _ { n } } \end{array} \right) ,
$$

where $G$ is constructed to zero the element $\beta$ in $A$ .By keeping $A$ in scaled form

$$
A = D A ^ { \prime } , \quad D = \left( \begin{array} { c c } { { d _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { d _ { 2 } } } \end{array} \right) ,
$$

and updating the two factors separately, the number of multiplications can be reduced. The transformation (2.2.19) is represented in the factored form

$$
G A = G D A ^ { \prime } = \tilde { D } P A ^ { \prime } , \qquad G D = \tilde { D } P ,
$$

where $\tilde { D }$ is a diagonal matrix chosen so that two elements in $P$ are equal to unity. This eliminates $2 n$ multiplications in forming the product $P A ^ { \prime }$ . In actual computation, $D ^ { 2 }$ rather than $D$ is stored in order to avoid square roots.

Consider first the case $| \gamma | \geq | \sigma |$ ,i.e., $| \theta | \leq \pi / 4$ . Then

$$
G D = \left( \begin{array} { c c } { { d _ { 1 } \gamma } } & { { d _ { 2 } \sigma } } \\ { { - d _ { 1 } \sigma } } & { { d _ { 2 } \gamma } } \end{array} \right) = \gamma D \left( \begin{array} { c c } { { 1 } } & { { \left( \frac { d _ { 2 } } { d _ { 1 } } \right) \frac { \sigma } { \gamma } } } \\ { { - \left( \frac { d _ { 1 } } { d _ { 2 } } \right) \frac { \sigma } { \gamma } } } & { { 1 } } \end{array} \right) = \tilde { D } P ,
$$

and ${ \tilde { D } } ^ { 2 } = \gamma ^ { 2 } D ^ { 2 }$ . Since $\sigma / \gamma = \beta / \alpha = ( d _ { 2 } / d _ { 1 } ) ( \beta ^ { \prime } / \alpha ^ { \prime } )$ we have

$$
P = \left( { \begin{array} { c c } { 1 } & { p _ { 1 2 } } \\ { - p _ { 2 1 } } & { 1 } \end{array} } \right) , \quad p _ { 2 1 } = { \frac { \beta ^ { \prime } } { \alpha ^ { \prime } } } , \quad p _ { 1 2 } = \left( { \frac { d _ { 2 } } { d _ { 1 } } } \right) ^ { 2 } p _ { 2 1 } .
$$

Hence we only need the squares of the scale factors $d _ { 1 }$ and $d _ { 2 }$ . The identity $\gamma ^ { 2 } = ( 1 + \sigma ^ { 2 } / \gamma ^ { 2 } ) ^ { - 1 }$ implies that

$$
\tilde { d } _ { 1 } ^ { 2 } = d _ { 1 } ^ { 2 } / t , \quad \tilde { d } _ { 2 } ^ { 2 } = d _ { 2 } ^ { 2 } / t , \quad t = 1 + \sigma ^ { 2 } / \gamma ^ { 2 } = 1 + p _ { 1 2 } p _ { 2 1 } .
$$

This eliminates the square root in the plane transformation. Similar formulas are easily derived for the other case $| \gamma | < | \sigma |$ ,i.e., $| \theta | > \pi / 4$ ,giving

$$
P = \left( { \begin{array} { c c } { p _ { 1 1 } } & { 1 } \\ { - 1 } & { p _ { 2 2 } } \end{array} } \right) , \quad p _ { 2 2 } = { \frac { \alpha ^ { \prime } } { \beta ^ { \prime } } } , \quad p _ { 1 1 } = \left( { \frac { d _ { 1 } } { d _ { 2 } } } \right) ^ { 2 } p _ { 2 2 } ,
$$

and

$$
\tilde { d } _ { 1 } ^ { 2 } = d _ { 2 } ^ { 2 } / t , \qquad \tilde { d } _ { 2 } ^ { 2 } = d _ { 1 } ^ { 2 } / t , \qquad t = 1 + \gamma ^ { 2 } / \sigma ^ { 2 } = p _ { 1 1 } p _ { 2 2 } + 1 .
$$

Fast plane rotations have the advantage that they reduce the number of multiplications and square roots.However, when they are applied, the square of the scale factors is always updated by a factor in the interval $[ 1 / 2 , 1 ]$ . Thus after many transformations the elements in $D$ may underflow. Therefore the size of the scale factors must be careful monitored to prevent underflow or overflow. This substantially decreases the efficiency of fast plane rotations.

Anda and Park [21, 1994l developed self-scaling fast rotations,which obviate rescalings. Four variations of these modified fast rotations are used. The choice among the four Variants is made to diminish the larger diagonal element while increasing the smaller one.

On modern processors the gain in speed of fast plane rotations is modest, due to the nontrivial amount of monitoring needed. Hence,their usefulness appears to be limited,and LAPACK does not make use of them.

Example 2.2.1. Let $Q \in \mathbb { R } ^ { 3 \times 3 }$ ， $\operatorname* { d e t } ( Q ) = 1$ , be an orthogonal matrix representing an arbitrary pure rotation in three dimensions. A classical problem is to express this as a product of three normal equations $A ^ { T } A x = A ^ { T } b$ ，

$$
G _ { 2 3 } ( \phi ) G _ { 1 2 } ( \theta ) G _ { 2 3 } ( \psi ) Q = I ,
$$

where $\phi , \theta$ ,and $\psi$ are the Euler angles,

$$
\left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { c _ { 3 } } } & { { s _ { 3 } } } \\ { { 0 } } & { { - s _ { 3 } } } & { { c _ { 3 } } } \end{array} \right) \left( \begin{array} { c c c } { { c _ { 2 } } } & { { s _ { 2 } } } & { { 0 } } \\ { { - s _ { 2 } } } & { { c _ { 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { c _ { 1 } } } & { { s _ { 1 } } } \\ { { 0 } } & { { - s _ { 1 } } } & { { c _ { 1 } } } \end{array} \right) \left( \begin{array} { c c c } { { q _ { 1 1 } } } & { { q _ { 1 2 } } } & { { q _ { 1 3 } } } \\ { { q _ { 2 1 } } } & { { q _ { 2 2 } } } & { { q _ { 2 3 } } } \\ { { q _ { 3 1 } } } & { { q _ { 3 2 } } } & { { q _ { 3 3 } } } \end{array} \right) = I .
$$

The first rotation $G _ { 2 3 } ( \psi )$ is used to zero the element $q _ { 3 1 }$ Next, $G _ { 1 2 } ( \theta )$ zeros the modified element $q _ { 2 1 }$ . Finally, $G _ { 2 3 } ( \phi )$ is used to zero $q _ { 3 2 }$ . The angles can always be chosen to make the diagonal elements positive. Since the final product is orthogonal and upper triangular, it must be the unit matrix $I _ { 3 }$ . By orthogonality, we have

$$
Q = G _ { 2 3 } ( - \psi ) G _ { 1 2 } ( - \theta ) G _ { 2 3 } ( - \phi ) .
$$

A problem with this representation is that the Euler angles may not depend continuously on the data.If $Q$ equals the unit matrix plus small terms, then a small perturbation may change an angle by as much as $2 \pi$ ．A different set of angles,based on zeroing the elements in the order $q _ { 2 1 } , q _ { 3 1 } , q _ { 3 2 }$ ,yields a continuous representation and is preferred. This corresponds to the product

$$
G _ { 2 3 } ( \phi ) G _ { 1 3 } ( \theta ) G _ { 1 2 } ( \psi ) Q = I _ { 3 } .
$$

For more details,see Hanson and Norris [590,1981]. An application of Euler angles for solving the eigenproblem of a symmetric $3 \times 3$ matrix is given by Bojanczyk and Lutoborksi [167,1991].

# Notes and references

Wilkinson [1120,1965l proved the backward stability of algorithms based on sequences of Householder reflectors. Parlet [884,1998] gives stable formulas for the choice of Householder reflector corresponding to the inner bisector. Dubrulle [338,2ooo] shows that the inner reflectors perform better in some eigenvalue algorithms but can lead to a loss of accuracy in other algorithms.

Plane rotations seem to have been first used by Jacobi [658,1845] to achieve diagonal dominance in systems of normal equations. The systematic use of orthogonal transformations to reduce matrices to simpler form was initiated by Givens $[ 4 8 0 , \ 1 9 5 8 ]$ and Householder [644, 1958].

# 2.2.2 - Householder QR Factorization

Any matrix $A \in \mathbb { C } ^ { m \times n }$ ， $m \geq n$ ,can be reduced to upper triangular form by a sequence of orthogonal transformations. This QR factorization is one of the most important matrix factorizations and is extensively used in least squares and eigenvalue problems.

Theorem 2.2.2 (The QR Factorization). For any matrix $A \in \mathbb { C } ^ { m \times n }$ ， $m \geq n$ ， of full column rank there exists a factorization

$$
A = Q \left( { \begin{array} { l } { R } \\ { 0 } \end{array} } \right) = \left( Q _ { 1 } \quad Q _ { 2 } \right) \left( { \begin{array} { l } { R } \\ { 0 } \end{array} } \right) = Q _ { 1 } R ,
$$

where $Q \in \mathbb { C } ^ { m \times m }$ is unitary, $Q _ { 1 } \in \mathbb { C } ^ { m \times n }$ ,and $R \in \mathbb { C } ^ { n \times n }$ is upper triangular with real positive diagonal elements. The matrices $R$ and $Q _ { 1 } = A R ^ { - 1 }$ are uniquely determined. $Q _ { 2 }$ is not unique, and (2.2.25) holds if we substitute $Q _ { 2 } P$ ,where $P \in \mathbb { C } ^ { ( m - n ) \times ( m - n ) }$ is any unitary matrix. The corresponding orthogonal projectors

$$
P _ { { \mathcal R } ( A ) } = Q _ { 1 } Q _ { 1 } ^ { H } , \quad P _ { A ^ { \perp } } = Q _ { 2 } Q _ { 2 } ^ { H } = I - Q _ { 1 } Q _ { 1 } ^ { H }
$$

are uniquely determined.

Proof. The proof is constructive. Set $A ^ { ( 1 ) } = A$ and compute $A ^ { ( k + 1 ) } = H _ { k } A ^ { ( k ) }$ ， $k = 1 , \dots , n$ Here $H _ { k }$ is a Householder reflection chosen to zero the elements below the main diagonal in column $k$ of $A ^ { ( k ) }$ . After step $k$ ， $A ^ { ( k + 1 ) }$ is triangular in its first $k$ columns, i.e.,

$$
A ^ { ( k + 1 ) } = \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { \tilde { A } ^ { ( k + 1 ) } } } \end{array} \right) , \quad k = 1 , \ldots , n ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ is upper triangular and $( R _ { 1 1 } , R _ { 1 2 } )$ are the first $k$ rows of the final factor $R$ If $\tilde { A } ^ { ( k ) } = ( \tilde { a } _ { k } ^ { ( k ) } , \dots , \tilde { a } _ { n } ^ { ( k ) } )$ ， $H _ { k }$ is take as

$$
H _ { k } = \operatorname { d i a g } \big ( I _ { k - 1 } , \tilde { H } _ { k } \big ) , \quad \tilde { H } _ { k } = I - \boldsymbol { u } _ { k } \boldsymbol { u } _ { k } ^ { T } / \gamma _ { k } , \quad k = 1 , \ldots , n ,
$$

where

$$
\begin{array} { r } { \tilde { H } _ { k } \tilde { { a } } _ { k } ^ { ( k ) } = \sigma _ { k } e _ { 1 } , \quad \sigma _ { k } = r _ { k k } = \| \tilde { { a } } _ { k } ^ { ( k ) } \| _ { 2 } . } \end{array}
$$

Note that $H _ { k }$ only transforms $\tilde { A } ^ { ( k ) }$ and does not destroy zeros introduced in earlier steps. After $n$ steps,we have

$$
A ^ { ( n + 1 ) } = Q ^ { T } A = { \binom { R } { 0 } } , \qquad Q = H _ { 1 } \cdot \cdot \cdot H _ { n } ,
$$

which is the QR factorization of $A$ ，where $Q$ is given as a product of Householder transformations. If $m = n$ ,the last transformation $H _ { n }$ can be skipped. □

From (2.2.25) the columns of $Q _ { 1 }$ and $Q _ { 2 }$ form orthonormal bases for $\mathcal { R } ( A )$ and its orthogonal complement:

$$
{ \mathcal { R } } ( A ) = { \mathcal { R } } ( Q _ { 1 } ) , \qquad { \mathcal { N } } ( A ^ { H } ) = { \mathcal { R } } ( Q _ { 2 } ) .
$$

The vectors $\tilde { u } ^ { ( k ) }$ ， $k = 1 , \dots , n$ ,can overwrite the elements on and below the main diagonal of $A$ .Thus all information associated with the factors $Q$ and $R$ fits into the array holding $A$ .The vector $( \beta _ { 1 } , \ldots , \beta _ { n } )$ of length $n$ is usually stored separately but can also be recomputed from $\beta _ { k } = \textstyle { \frac { 1 } { 2 } } ( 1 + \| \widehat { u } _ { k } \| _ { 2 } ^ { 2 } ) ^ { 1 / 2 }$

For a complex matrix $A \in \mathbb { C } ^ { m \times n }$ the QR factorization can be computed similarly by using a sequence of unitary Householder reflectors. Note that a factor $R$ with real positive diagonal elements can always be obtained by a unitary scaling:

$$
A = U \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) = ( U D ^ { - 1 } ) \left( \begin{array} { c c } { { D R } } \\ { { 0 } } \end{array} \right) , \quad D = \mathrm { d i a g } ( e ^ { i \alpha _ { 1 } } , \ldots , e ^ { i \alpha _ { n } } ) .
$$

The factor $Q$ is usually kept in factored form and accessed through $\beta _ { k }$ and the Householder vectors $\tilde { u } ^ { ( k ) }$ ， $k = 1 , \ldots , n$ In step $k$ the application of the Householder reflector to the active part of the matrix requires $4 ( m - k + 1 ) ( n - k )$ flops.Hence,the total flop count becomes $2 ( m n ^ { 2 } - n ^ { 3 } / 3 )$ or $4 n ^ { 3 } / 3$ flops if $m = n$

Algorithm 2.2.3 computes the QR factorization of $A \in \mathbb { C } ^ { m \times n }$ $\mathbf { \chi } _ { m } \ge n \mathbf { \chi } )$ using Householder trasoat $r _ { k k }$ will e posiy i $a _ { k } ^ { ( k k ) }$ is negative and ng ative otherwise. Negative diagonal elements may be removed by multiplying the corresponding rows of $R$ and columns of $Q$ by $- 1$

# Algorithm 2.2.3 (Householder QR Factorization).

function [U,R,bet $\mathsf { a } \mathsf { l } \mathsf { \Pi } = \mathsf { h }$ ouseqr (A) $\%$ HOUSEQR computes the Householder $\mathbb { Q R }$ factorization $\%$ of the m by n matrix A $\mathrm { ~ ( ~ m ~ } > = \mathrm { ~ n ~ ) ~ }$ .At return, $\%$ U and beta contain the Householder reflections. $\%$ $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ size(A); if $\left( \mathfrak { m } \ < \ \mathfrak { n } \right)$ ，error('Illegal dimensions of $\tt { A } ^ { \prime }$ )；end $u \ =$ zeros(m,1)；beta $=$ zeros $( \mathtt { n } , 1 )$ ； for $\mathtt { k } \ = \ 1 { : } \mathtt { n }$ if $\texttt { k } < \texttt { m }$ ， $\%$ Construct and save k:th Householder reflector $\begin{array} { r l } & { \left[ \mathop { \bf u } \left( \mathrm { k } : \mathrm { m } \right) , \mathrm { b e t a } \left( \mathrm { k } \right) , \mathrm { A } \left( \mathrm { k } , \mathrm { k } \right) \right] \ = \ \mathrm { h o u s e g } \left( \mathrm { A } \left( \mathrm { k } : \mathrm { m } , \mathrm { k } \right) \right) } \\ & { \quad \times \ r _ { \mathrm { ~ r ~ - ~ } } , \mathrm { ~ \ r ~ > ~ \ r ~ \ e t a ~ \left( ~ \mathrm { k } ~ , ~ \mathrm { ~ A ~ } ~ . ~ c ~ . ~ \right) ~ . } } \end{array}$ $\mathtt { A } \left( \mathtt { k } + 1 : \mathtt { m } , \mathtt { k } \right) \ = \ \mathtt { u } \left( \mathtt { k } + 1 : \mathtt { m } \right) ;$ %Apply k:th Householder reflector $\begin{array} { r l } & { \mathtt { A } \left( \mathtt { k } : \mathtt { m } , \mathtt { k } + 1 : \mathtt { n } \right) \ = \ \mathtt { A } \left( \mathtt { k } : \mathtt { m } , \mathtt { k } + 1 : \mathtt { n } \right) \ \mathrm { \ - ~ \Gamma ~ \mathtt { \mathtt { k } } ~ \cdot ~ \mathtt { \mathtt { t } } ~ \cdot ~ \mathtt { n } ~ } } \\ & { \mathtt { b e t a } \left( \mathtt { k } \right) \ast \mathtt { u } \left( \mathtt { k } : \mathtt { m } \right) \ast \left( \mathtt { u } \left( \mathtt { k } : \mathtt { m } \right) \ \mathrm { \ast A } \left( \mathtt { k } : \mathtt { m } , \mathtt { k } + 1 : \mathtt { n } \right) \right) ; } \end{array}$ end end $\begin{array} { r l } & { \mathrm { ~ U ~ = ~ \Theta ~ e _ { J } e _ { \Phi } ( m , n ) \phi ~ + ~ \Theta _ { \mathrm { t r i } 1 } ( A , - 1 ) : } } \\ & { \mathrm { ~ R _ { \theta } = ~ t r i u _ { \theta } ( A ( 1 { : } n , : ) ) ~ ; } } \end{array}$   
end

Should $Q$ be explicitly required, it can be computed by accumulating the products in

$$
Q = \left( Q _ { 1 } \quad Q _ { 2 } \right) = H _ { 1 } \cdot \cdot \cdot H _ { n } I _ { m } \in \mathbb { R } ^ { m \times m }
$$

from left to right. Since the transformation $H _ { k + 1 }$ leaves the frst $k$ rows unchanged, it follows that

$$
q _ { k } = H _ { 1 } \cdot \cdot \cdot H _ { p } e _ { k } , \quad k = 1 : m , \quad p = \mathrm { m i n } \{ k , n \} .
$$

Generating the full matrix $Q$ takes $4 ( m n ( m - n ) + n ^ { 3 } / 3 )$ flops. Algorithm 2.2.4 generates the matrix $Q _ { 1 } \in \mathbb { R } ^ { m \times n }$ $m \geq n ,$ and requires $2 ( m n ^ { 2 } - n ^ { 3 } / 3 )$ flops.

# Algorithm 2.2.4 (Accumulating $Q _ { 1 }$ in Householder QR).

function ${ \sf Q } =$ houseq1(U,beta) $\%$ HOUSEQ1 generates the m by n orthonormal matrix $\% ~ \mathsf { Q }$ from a given Householder $\mathbb { Q R }$ factorization %- $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ size(U); ${ \sf Q } = { \sf e y e } \left( { \sf m } , { \sf n } \right)$ fo $\begin{array} { r l } & { \textbf { r } \textbf { k } = \textbf { n } : - 1 : 1 } \\ & { \quad \mathrm { u } \textbf { k } = \textbf { U } ( \mathbf { k } : \mathrm { m } , \mathbf { k } ) ; \quad \mathrm { ~ v ~ = ~ u } \mathbf { k } ^ { \prime } * \boldsymbol { \Theta } \left( \mathbf { k } : \mathrm { m } , \mathbf { k } : \mathrm { n } \right) ; } \\ & { \quad \boldsymbol { \mathbb { Q } } \left( \mathbf { k } : \mathrm { m } , \mathbf { k } : \mathrm { n } \right) = \textbf { Q } \left( \mathbf { k } : \mathrm { m } , \mathbf { k } : \mathrm { n } \right) - \textbf { \Phi } \left( \mathbf { b } \in \mathbf { t } \mathrm { a } \left( \mathbf { k } \right) * \mathrm { u } \mathbf { k } \right) * _ { \mathrm { V } } ; } \end{array}$ end   
end

The matrix $Q _ { 2 } ~ \in ~ \mathbb { R } ^ { m \times ( m - n ) }$ givesanorthogonalbasis for theorthogonal complement ${ \mathcal { N } } ( A ^ { T } )$ and can be generated in $2 n ( m - n ) ( 2 m - n )$ flops.Householder QR factorization is backward stable. The following result is due to Higham [623,2oo2,Theorem 19.4].

Theorem 2.2.3. Let $\bar { R } \in \mathbb { R } ^ { m \times n }$ denote the upper trapezoidal matrix computed by the Householder $Q R$ factorization for $A \in \mathbb { R } ^ { m \times n }$ . Then there exists an exactly orthogonal matrix $Q \in$ $\mathbb { R } ^ { m \times m }$ such that $A + \Delta A = Q { \bar { R } }$ where

$$
\| \Delta a _ { j } \| _ { 2 } \leq \widetilde { \gamma } _ { m n } \| a _ { j } \| _ { 2 } , \quad j = 1 , \ldots , n .
$$

Here the matrix $Q$ is given by $Q = H _ { n } \cdot \cdot \cdot H _ { 2 } H _ { 1 }$ ，where $H _ { k }$ is the Householder matrix that corresponds to the exact application of the kth step to the computed matrix produced after $k - 1$ steps.

Note that the matrix $\bar { Q }$ computed by the Householder QR factorization is not the exact orthogonal matrix $Q$ in Theorem 2.2.3.However, it is very close to this:

$$
\| \bar { Q } - Q \| _ { F } \leq \sqrt { n } \gamma _ { m n } .
$$

Householder QR factorization is invariant under column scaling in the following sense. If applied to the scaled matrix $\widetilde { A } = A D$ ，where $D > 0$ is diagonal, it yields the factors $\widetilde Q = Q$ and ${ \widetilde { R } = R D }$ . This invariance holds also in finite-precision arithmetic, provided the scaling is done without introducing rounding errors. The columnwise bound in Theorem 2.2.3 reflects this invariance and gives the weaker bound $\| \Delta A \| _ { F } \leq \tilde { \gamma } _ { m } \| A \| _ { F }$

Let $A \in \mathbb { C } ^ { m \times n }$ have the QR factorization $A = Q _ { 1 } R$ ，where $R \in \mathbb { C } ^ { n \times n }$ and $Q _ { 1 } \in \mathbb { C } ^ { m \times n }$ The following perturbation bounds for the factors when $A$ is perturbed to $A + E$ are given by Sun [1048,1991].

Theorem 2.2.4. Let $A = Q R$ be the QR factorization of $A \in \mathbb { C } ^ { m \times n }$ with $\operatorname { r a n k } ( A ) = n$ Let $A$ be perturbed to $A + E$ ,where $E \in \mathbb { C } ^ { m \times n }$ satisfies

$$
\begin{array} { r } { \mu = \kappa ( A ) \| E \| _ { 2 } / \| A \| _ { 2 } < 1 . } \end{array}
$$

Then there is a unique QR factorization $A + E = ( Q + W ) ( R + F ) ,$ where

$$
\frac { \Vert F \Vert _ { F } } { \Vert R \Vert _ { p } } \leq \frac { \sqrt { 2 } \kappa _ { 2 } ( A ) } { 1 - \mu } \frac { \Vert E \Vert _ { F } } { \Vert A \Vert _ { p } } , \qquad \Vert \delta Q \Vert _ { F } \leq \frac { ( 1 + \sqrt { 2 } ) \kappa _ { 2 } ( A ) } { 1 - \mu } \frac { \Vert E \Vert _ { F } } { \Vert A \Vert _ { 2 } } , \quad p = 2 , F .
$$

An important special case is the computation of the QR factorization of a matrix of the form

$$
A = { \binom { R _ { 1 } } { R _ { 2 } } } ,
$$

where $R _ { 1 }$ ， $R _ { 2 } \in \mathbb { R } ^ { n \times n }$ are upper triangular. This “merging” of triangular matrices occurs as a subproblem in parallel QR factorization and in QR factorization of band and other sparse matrices. If the rows of $A$ are permuted in order $1 , n + 1 , 2 , n + 1 , \ldots , n , 2 n$ ， then standard Householder QR can be used without introducing extra fill. This is illustrated in the following diagram for $n = 4$ ：

$$
\begin{array}{c} \begin{array} { r l r l r l r } { \times } & { \times } & { \times } & { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } & { \times } \\ & & & { \times } & { \times } & { \times } \end{array} ] , \quad \verb  & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } & { \times } \end{array} [ \begin{array} { l l l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } \\ { 0 } & { \times } & { \times } & { \times } & { \times } \\ { 0 } & { \otimes } & { \times } & { \times } & { \times } \\ { \otimes } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } \\ & & & & { \times } & { \times } \end{array} ] , \quad \begin{array} { l l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } & { } \\ { 0 } & { \times } & { \times } & { \times } & { \times } \\ & { \otimes } & { \times } & { \times } & { \times } \\ & { 0 } & { \otimes } & { \times } & { \times } \\ & { \otimes } & { \otimes } & { \times } \\ & { \otimes } & { \times } & { \otimes } \\ & & { \times } & { \times } \end{array} ] .
$$

In the diagram, $\times$ stands for a (potential) nonzero element, $\otimes$ for a nonzero element that has been zeroed out,and $^ +$ for a nonzero element that has been introduced in the computations (if any). In practice the reordering of the rows need only be carried out implicitly. The QR factorization requires a total of approximately $2 n ^ { 3 } / 3$ flops if the Householder transformations are not accumulated.

In Givens QR factorization,a sequence of rotations is used to eliminate the elements below the diagonal of $A$ ． An advantage over Householder QR is that the rotations can be adapted to the nonzero structure of the matrix.For example,in the QR factorization of band matrices, zeros can be introduced one row at a time. This case is considered further in Section 4.1. Another important example arises in algorithms for the unsymmetric eigenvalue problem. Here the QR factorization of a Hessenberg matrix

$$
H _ { n } = \left( \begin{array} { c c c c c c } { h _ { 1 1 } } & { h _ { 1 2 } } & { \cdots } & { h _ { 1 , n - 1 } } & { h _ { 1 , n } } \\ { h _ { 2 1 } } & { h _ { 2 2 } } & { \cdots } & { h _ { 2 , n - 1 } } & { h _ { 2 , n } } \\ & { h _ { 3 2 } } & { \cdots } & { \vdots } & { \vdots } \\ & & { \ddots } & { h _ { n - 1 , n - 1 } } & { h _ { n - 1 , n } } \\ & & & { h _ { n , n - 1 } } & { h _ { n , n } } \\ & & & & { h _ { n + 1 , n } } \end{array} \right) \in \mathbb { R } ^ { n \times n }
$$

is needed. This is obtained using a sequence of $n$ plane rotations,

$$
G _ { n , n + 1 } \cdot \cdot \cdot G _ { 2 3 } G _ { 1 2 } H = Q \left( { \begin{array} { l } { R } \\ { 0 } \end{array} } \right) ,
$$

where $G _ { k , k + 1 }$ is used to zero the element $h _ { k + 1 , k }$ ， $k = 1 , \dots , n$ .The total work in Hessenberg QR factorization is about $\textstyle \sum _ { k = 1 } ^ { n } 6 ( n - k ) \approx 3 n ^ { 2 }$ flops.In the specal case when $H _ { n }$ is bidiagonal, the flop count for QR factorization is linear in $n$

As for Householder QR factorization,the factor $Q$ is usually not explicitly formed. To be able to perform operations with $Q$ it suffices to store the rotations. The rotations $G _ { i j } ( \theta )$ can be stored in the zeroed part of $A$ using Stewart's storage scheme described in Section 4.5.3. The error properties are similar to those for the Householder algorithm. The backward error bound