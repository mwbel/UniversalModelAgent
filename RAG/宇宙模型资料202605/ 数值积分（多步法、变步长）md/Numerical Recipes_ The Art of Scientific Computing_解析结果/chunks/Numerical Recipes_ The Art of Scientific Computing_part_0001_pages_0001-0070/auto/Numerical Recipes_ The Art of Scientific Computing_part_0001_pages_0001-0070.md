# NUMERICAL RECIPES

The Art of Sclentific Computing

THIRD EDITION

William H. Press Saul A. Teukolsky willtam T.Vetterling Brlan P. Flannery

The Art of Scientific Computing

Third Edition

# NUMERICAL RECIPES

# The Art of Scientific Computing

# Third Edition

William H. Press

Raymer Chair in Computer Sciences and Integrative Biology The University of Texas at Austin

Saul A. Teukolsky

Hans A. Bethe Professor of Physics and Astrophysics Cornell University

William T. Vetterling

Research Fellow and Director of Image Science ZINK Imaging, LLC

Brian P.Flannery

Science, Strategy and Programs Manager Exxon Mobil Corporation

CAMBRIDGE UNIVERSITY PRESS Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore, São Paulo

Cambridge University Press   
The Edinburgh Building, Cambridge CB2 8RU, UK   
Published in the United States of America by Cambridge University Press, New York   
www.cambridge.org   
Information on this title: www.cambridge.org/9780521880688

$^ ©$ Cambridge University Press 1988, 1992, 2002, 2007 except for 13.10, which is placed into the public domain, and except for all other computer programs and procedures, which are This publication is in copyright. Subject to statutory exception and to the provision of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published in print format 2007

ISBN-13 978-0-511-33555-6 eBook (NetLibrary) ISBN-10 0-511-33555-5 eBook (NetLibrary)

ISBN-13 978-0-521-88068-8 hardback ISBN-10 0-521-88068-8 hardback

Cambridge University Press has no responsibility for the persistence or accuracy of urls for external or third-party internet websites referred to in this publication, and does not guarantee that any content on such websites is, or will remain, accurate or appropriate.

Without an additional license to use the contained software, this book is intended as a text and reference book, for reading and study purposes only. However, a restricted, limited free license for use of the software by the individual owner of a copy of this book who personally keyboards one or more routines into a single computer is granted under terms described on p. xix. See the section “License and Legal Information” (pp. xix–xxi) for information on obtaining more general licenses. Machine-readable media containing the software in this book, with included license for use by a single individual, are available from Cambridge University Press. The software may also be downloaded, with immediate purchase of a license also possible, from the Numerical Recipes Software Web site (http: //www.nr.com). Unlicensed transfer of Numerical Recipes programs to any other format, or to any computer except one that is specifically licensed, is strictly prohibited. Technical questions, corrections, and requests for information should be addressed to Numerical Recipes Software, P.O. Box 380243, Cambridge, MA 02238-0243 (USA), email info $@ \mathrm { n r }$ . com, or fax 781-863-1739.

Preface to the Third Edition (2007) xi

Preface to the Second Edition (1992) xiv

Preface to the First Edition (1985) xvii

License and Legal Information xix

# 1 Preliminaries 1

1.0 Introduction 1   
1.1 Error, Accuracy, and Stability 8   
1.2 C Family Syntax . 12   
1.3 Objects, Classes, and Inheritance 17   
1.4 Vector and Matrix Objects . 24   
1.5 Some Further Conventions and Capabilities . 30

# 2 Solution of Linear Algebraic Equations 37

2.0 2.1 Introduction Gauss-Jordan Elimination 3741   
2.2 Gaussian Elimination with Backsubstitution 46   
2.3 $L U$ Decomposition and Its Applications 48   
2.4 Tridiagonal and Band-Diagonal Systems of Equations 56   
2.5 Iterative Improvement of a Solution to Linear Equations 61   
2.6 Singular Value Decomposition . 65   
2.7 Sparse Linear Systems . 75   
2.8 Vandermonde Matrices and Toeplitz Matrices . 93   
2.9 Cholesky Decomposition 100   
2.10 QR Decomposition 102   
2.11 Is Matrix Inversion an $N ^ { 3 }$ Process? 106

# 3 Interpolation and Extrapolation 110

3.0 Introduction 110   
3.1 Preliminaries: Searching an Ordered Table 114   
3.2 Polynomial Interpolation and Extrapolation 118   
3.3 Cubic Spline Interpolation . 120   
3.4 Rational Function Interpolation and Extrapolation 124   
3.5 Coefficients of the Interpolating Polynomial 129   
3.6 Interpolation on a Grid in Multidimensions 132   
3.7 Interpolation on Scattered Data in Multidimensions 139   
3.8 Laplace Interpolation 150

# 4 Integration of Functions 155

4.0 Introduction 155   
4.1 Classical Formulas for Equally Spaced Abscissas . 156   
4.2 Elementary Algorithms 162   
4.3 Romberg Integration . 166   
4.4 Improper Integrals 167   
4.5 Quadrature by Variable Transformation 172   
4.6 Gaussian Quadratures and Orthogonal Polynomials 179   
4.7 Adaptive Quadrature . 194   
4.8 Multidimensional Integrals 196

# 5 Evaluation of Functions 201

5.0 Introduction 201   
5.1 Polynomials and Rational Functions . 201   
5.2 Evaluation of Continued Fractions . 206   
5.3 Series and Their Convergence 209   
5.4 Recurrence Relations and Clenshaw’s Recurrence Formula . 219   
5.5 Complex Arithmetic 225   
5.6 Quadratic and Cubic Equations 227   
5.7 Numerical Derivatives 229   
5.8 Chebyshev Approximation . 233   
5.9 Derivatives or Integrals of a Chebyshev-Approximated Function . . 240   
5.10 Polynomial Approximation from Chebyshev Coefficients 241   
5.11 Economization of Power Series 243   
5.12 Pade Approximants´ 245   
5.13 Rational Chebyshev Approximation 247   
5.14 Evaluation of Functions by Path Integration . 251

# 6 Special Functions 255

6.0 Introduction 255   
6.1 Gamma Function, Beta Function, Factorials, Binomial Coefficients 256   
6.2 Incomplete Gamma Function and Error Function . 259   
6.3 Exponential Integrals 266   
6.4 Incomplete Beta Function 270   
6.5 Bessel Functions of Integer Order 274   
6.6 Bessel Functions of Fractional Order, Airy Functions, Spherical   
Bessel Functions 283   
6.7 Spherical Harmonics . 292   
6.8 Fresnel Integrals, Cosine and Sine Integrals 297   
6.9 Dawson’s Integral 302   
6.10 Generalized Fermi-Dirac Integrals . 304   
6.11 Inverse of the Function $x \log ( x )$ . 307   
6.12 Elliptic Integrals and Jacobian Elliptic Functions 309   
6.13 Hypergeometric Functions . . 318   
6.14 Statistical Functions 320

# 7 Random Numbers 340

7.0 Introduction 340   
7.1 Uniform Deviates 341   
7.2 Completely Hashing a Large Array 358   
7.3 Deviates from Other Distributions 361   
7.4 Multivariate Normal Deviates 378   
7.5 Linear Feedback Shift Registers 380   
7.6 Hash Tables and Hash Memories 386   
7.7 Simple Monte Carlo Integration 397   
7.8 Quasi- (that is, Sub-) Random Sequences 403   
7.9 Adaptive and Recursive Monte Carlo Methods 410

# 8 Sorting and Selection

# 419

8.0 Introduction 419   
8.1 Straight Insertion and Shell’s Method 420   
8.2 Quicksort . 423   
8.3 Heapsort 426   
8.4 Indexing and Ranking 428   
8.5 Selecting the $M$ th Largest 431   
8.6 Determination of Equivalence Classes . 439

# 9 Root Finding and Nonlinear Sets of Equations 442

9.0 Introduction 442   
9.1 Bracketing and Bisection 445   
9.2 Secant Method, False Position Method, and Ridders’ Method 449   
9.3 Van Wijngaarden-Dekker-Brent Method 454   
9.4 Newton-Raphson Method Using Derivative 456   
9.5 Roots of Polynomials 463   
9.6 Newton-Raphson Method for Nonlinear Systems of Equations . . 473   
9.7 Globally Convergent Methods for Nonlinear Systems of Equations 477

# 10 Minimization or Maximization of Functions 487

10.0 Introduction 487   
10.1 Initially Bracketing a Minim 490   
10.2 Golden Section Search in One Dimension 492   
10.3 Parabolic Interpolation and Brent’s Method in One Dimension . 496   
10.4 One-Dimensional Search with First Derivatives . 499   
10.5 Downhill Simplex Method in Multidimensions 502   
10.6 Line Methods in Multidimensions 507   
10.7 Direction Set (Powell’s) Methods in Multidimensions 509   
10.8 Conjugate Gradient Methods in Multidimensions 515   
10.9 Quasi-Newton or Variable Metric Methods in Multidimensions 521   
10.10 Linear Programming: The Simplex Method . 526   
10.11 Linear Programming: Interior-Point Methods 537   
10.12 Simulated Annealing Methods . 549   
10.13 Dynamic Programming 555

# 11 Eigensystems 563

11.0 Introduction 563   
11.1 Jacobi Transformations of a Symmetric Matrix 570   
11.2 Real Symmetric Matrices 576   
11.3 Reduction of a Symmetric Matrix to Tridiagonal Form: Givens   
and Householder Reductions 578   
11.4 Eigenvalues and Eigenvectors of a Tridiagonal Matrix 583   
11.5 Hermitian Matrices 590   
11.6 Real Nonsymmetric Matrices 590   
11.7 The $\boldsymbol { \mathcal { Q } R }$ Algorithm for Real Hessenberg Matrices 596   
11.8 Improving Eigenvalues and/or Finding Eigenvectors by Inverse   
Iteration 597

# 12 Fast Fourier Transform 600

12.0 Introduction 600   
12.1 Fourier Transform of Discretely Sampled Data 605   
12.2 Fast Fourier Transform (FFT) 608   
12.3 FFT of Real Functions . 617   
12.4 Fast Sine and Cosine Transforms 620   
12.5 FFT in Two or More Dimensions 627   
12.6 Fourier Transforms of Real Data in Two and Three Dimensions . 631   
12.7 External Storage or Memory-Local FFTs 637

# 13 Fourier and Spectral Applications 640

13.0 Introduction 640   
13.1 Convolution and Deconvolution Using the FFT 641   
13.2 Correlation and Autocorrelation Using the FFT 648   
13.3 Optimal (Wiener) Filtering with the FFT 649   
13.4 Power Spectrum Estimation Using the FFT 652   
13.5 Digital Filtering in the Time Domain 667   
13.6 Linear Prediction and Linear Predictive Coding . . 673   
13.7 Power Spectrum Estimation by the Maximum Entropy (All-Poles)   
Method 681   
13.8 Spectral Analysis of Unevenly Sampled Data 685   
13.9 Computing Fourier Integrals Using the FFT . 692   
13.10 Wavelet Transforms 699   
13.11 Numerical Use of the Sampling Theorem 717

# 14 Statistical Description of Data 720

14.0 Introduction 720   
14.1 Moments of a Distribution: Mean, Variance, Skewness, and So Forth 721   
14.2 Do Two Distributions Have the Same Means or Variances? . 726   
14.3 Are Two Distributions Different? 730   
14.4 Contingency Table Analysis of Two Distributions 741   
14.5 Linear Correlation 745   
14.6 Nonparametric or Rank Correlation 748   
14.7 Information-Theoretic Properties of Distributions . 754   
14.8 Do Two-Dimensional Distributions Differ? 762

14.9 Savitzky-Golay Smoothing Filters . . . . 766

# 15 Modeling of Data 773

15.0 Introduction 773   
15.1 Least Squares as a Maximum Likelihood Estimator . 776   
15.2 Fitting Data to a Straight Line 780   
15.3 Straight-Line Data with Errors in Both Coordinates 785   
15.4 General Linear Least Squares 788   
15.5 Nonlinear Models 799   
15.6 Confidence Limits on Estimated Model Parameters 807   
15.7 Robust Estimation 818   
15.8 Markov Chain Monte Carlo 824   
15.9 Gaussian Process Regression 836

# 16 Classification and Inference 840

16.0 Introduction 840   
16.1 Gaussian Mixture Models and k-Means Clustering 842   
16.2 Viterbi Decoding . 850   
16.3 Markov Models and Hidden Markov Modeling 856   
16.4 Hierarchical Clustering by Phylogenetic Trees 868   
16.5 Support Vector Machines 883

# 17 Integration of Ordinary Differential Equations 899

17.0 Introduction 899   
17.1 Runge-Kutta Method . 907   
17.2 Adaptive Stepsize Control for Runge-Kutta 910   
17.3 Richardson Extrapolation and the Bulirsch-Stoer Method 921   
17.4 Second-Order Conservative Equations 928   
17.5 Stiff Sets of Equations . 931   
17.6 Multistep, Multivalue, and Predictor-Corrector Methods . 942   
17.7 Stochastic Simulation of Chemical Reaction Networks . 946

# 18 Two-Point Boundary Value Problems 955

18.0 Introduction 955   
18.1 The Shooting Method 959   
18.2 Shooting to a Fitting Point 962   
18.3 Relaxation Methods 964   
18.4 A Worked Example: Spheroidal Harmonics . 971   
18.5 Automated Allocation of Mesh Points . 981   
18.6 Handling Internal Boundary Conditions or Singular Points . . . 983

# 19 Integral Equations and Inverse Theory 986

19.0 Introduction 986   
19.1 Fredholm Equations of the Second Kind 989   
19.2 Volterra Equations 992   
19.3 Integral Equations with Singular Kernels 995   
19.4 Inverse Problems and the Use of A Priori Information 1001   
19.5 Linear Regularization Methods 1006   
19.6 Backus-Gilbert Method 1014

19.7 Maximum Entropy Image Restoration . . . . . 1016

# 20 Partial Differential Equations 1024

20.0 Introduction 1024   
20.1 Flux-Conservative Initial Value Problems 1031   
20.2 Diffusive Initial Value Problems 1043   
20.3 Initial Value Problems in Multidimensions 1049   
20.4 Fourier and Cyclic Reduction Methods for Boundary Value   
Problems 1053   
20.5 Relaxation Methods for Boundary Value Problems 1059   
20.6 Multigrid Methods for Boundary Value Problems . 1066   
20.7 Spectral Methods . 1083

# 21 Computational Geometry 1097

21.0 Introduction 1097   
21.1 Points and Boxes 1099   
21.2 KD Trees and Nearest-Neighbor Finding 1101   
21.3 Triangles in Two and Three Dimensions 1111   
21.4 Lines, Line Segments, and Polygons 1117   
21.5 Spheres and Rotations 1128   
21.6 Triangulation and Delaunay Triangulation 1131   
21.7 Applications of Delaunay Triangulation . . 1141   
21.8 Quadtrees and Octrees: Storing Geometrical Objects 1149

# 22 Less-Numerical Algorithms 1160

22.0 Introduction 1160   
22.1 Plotting Simple Graphs 1160   
22.2 Diagnosing Machine Parameters . . 1163   
22.3 Gray Codes . 1166   
22.4 Cyclic Redundancy and Other Checksums 1168   
22.5 Huffman Coding and Compression of Data 1175   
22.6 Arithmetic Coding 1181   
22.7 Arithmetic at Arbitrary Precision 1185

# Index 1195

# Preface to the Third Edition (2007)

“I was just going to say, when I was interrupted: : :” begins Oliver Wendell Holmes in the second series of his famous essays, The Autocrat of the Breakfast Table. The interruption referred to was a gap of 25 years. In our case, as the autocrats of Numerical Recipes, the gap between our second and third editions has been “only” 15 years. Scientific computing has changed enormously in that time.

The first edition of Numerical Recipes was roughly coincident with the first commercial success of the personal computer. The second edition came at about the time that the Internet, as we know it today, was created. Now, as we launch the third edition, the practice of science and engineering, and thus scientific computing, has been profoundly altered by the mature Internet and Web. It is no longer difficult to find somebody’s algorithm, and usually free code, for almost any conceivable scientific application. The critical questions have instead become, “How does it work?” and “Is it any good?” Correspondingly, the second edition of Numerical Recipes has come to be valued more and more for its text explanations, concise mathematical derivations, critical judgments, and advice, and less for its code implementations per se.

Recognizing the change, we have expanded and improved the text in many places in this edition and added many completely new sections. We seriously considered leaving the code out entirely, or making it available only on the Web. However, in the end, we decided that without code, it wouldn’t be Numerical Recipes. That is, without code you, the reader, could never know whether our advice was in fact honest, implementable, and practical. Many discussions of algorithms in the literature and on the Web omit crucial details that can only be uncovered by actually coding (our job) or reading compilable code (your job). Also, we needed actual code to teach and illustrate the large number of lessons about object-oriented programming that are implicit and explicit in this edition.

Our wholehearted embrace of a style of object-oriented computing for scientific applications should be evident throughout this book. We say $^ { * } a$ style,” because, contrary to the claims of various self-appointed experts, there can be no one rigid style of programming that serves all purposes, not even all scientific purposes. Our style is ecumenical. If a simple, global, C-style function will fill the need, then we use it. On the other hand, you will find us building some fairly complicated structures for something as complicated as, e.g., integrating ordinary differential equations. For more on the approach taken in this book, see $\ S 1 . 3 - \ S 1 . 5$ .

In bringing the text up to date, we have luckily not had to bridge a full 15-year gap. Significant modernizations were incorporated into the second edition versions in Fortran 90 $( 1 9 9 6 ) ^ { * }$ and $\mathrm { C } { + } { + }$ (2002), in which, notably, the last vestiges of unitbased arrays were expunged in favor of C-style zero-based indexing. Only with this third edition, however, have we incorporated a substantial amount (several hundred pages!) of completely new material. Highlights include:

- a new chapter on classification and inference, including such topics as Gaussian mixture models, hidden Markov modeling, hierarchical clustering (phylogenetic trees), and support vector machines

- a new chapter on computational geometry, including topics like KD tree quad- and octrees, Delaunay triangulation and applications, and many usef algorithms for lines, polygons, triangles, spheres, etc.   
- many new statistical distributions, with pdfs, cdfs, and inverse cdfs   
- an expanded treatment of ODEs, emphasizing recent advances, and with com pletely new routines   
- much expanded sections on uniform random deviates and on deviates fro many other statistical distributions   
- an introduction to spectral and pseudospectral methods for PDEs   
- interior point methods for linear programming   
- more on sparse matrices   
- interpolation on scattered data in multidimensions   
- curve interpolation in multidimensions   
- quadrature by variable transformation and adaptive quadrature   
- more on Gaussian quadratures and orthogonal polynomials   
- more on accelerating the convergence of series   
- improved incomplete gamma and beta functions and new inverse functions - improved spherical harmonics and fast spherical harmonic transforms - generalized Fermi-Dirac integrals   
- multivariate Gaussian deviates   
- algorithms and implementations for hash memory functions   
- incremental quantile estimation   
- chi-square with small numbers of counts   
- dynamic programming   
- hard and soft error correction and Viterbi decoding   
- eigensystem routines for real, nonsymmetric matrices   
- multitaper methods for power spectral estimation   
- wavelets on the interval   
- information-theoretic properties of distributions   
- Markov chain Monte Carlo   
- Gaussian process regression and kriging   
- stochastic simulation of chemical reaction networks   
- code for plotting simple graphs from within programs

The Numerical Recipes Web site, www.nr.com, is one of the oldest active sites on the Internet, as evidenced by its two-letter domain name. We will continue to make the Web site useful to readers of this edition. Go there to find the latest bug reports, to purchase the machine-readable source code, or to participate in our readers’ forum. With this third edition, we also plan to offer, by subscription, a completely electronic version of Numerical Recipes — accessible via the Web, downloadable, printable, and, unlike any paper version, always up to date with the latest corrections. Since the electronic version does not share the page limits of the print version, it will grow over time by the addition of completely new sections, available only electronically. This, we think, is the future of Numerical Recipes and perhaps of technical reference books generally. If it sounds interesting to you, look at http://www.nr.com/electronic.

This edition also incorporates some “user-friendly” typographical and stylistic improvements: Color is used for headings and to highlight executable code. For code, a label in the margin gives the name of the source file in the machine-readable distribution. Instead of printing repetitive #include statements, we provide a convenient Web tool at http://www.nr.com/dependencies that will generate exactly the statements you need for any combination of routines. Subsections are now numbered and referred to by number. References to journal articles now include, in most cases, the article title, as an aid to easy Web searching. Many references have been updated; but we have kept references to the grand old literature of classical numerical analysis when we think that books and articles deserve to be remembered.

# Acknowledgments

Regrettably, over 15 years, we were not able to maintain a systematic record of the many dozens of colleagues and readers who have made important suggestions, pointed us to new material, corrected errors, and otherwise improved the Numerical Recipes enterprise. It is a tired cliche to say that “you know who you are.” Actually, ´ in most cases, we know who you are, and we are grateful. But a list of names would be incomplete, and therefore offensive to those whose contributions are no less important than those listed. We apologize to both groups, those we might have listed and those we might have missed.

We prepared this book for publication on Windows and Linux machines, generally with Intel Pentium processors, using LaTeX in the TeTeX and MiKTeX implementations. Packages used include amsmath, amsfonts, txfonts, and graphicx, among others. Our principal development environments were Microsoft Visual Studio / Microsoft Visual $\mathrm { C } { + + }$ and GNU $\mathrm { C } { + + }$ . We used the SourceJammer crossplatform source control system. Many tasks were automated with Perl scripts. We could not live without GNU Emacs. To all the developers: “You know who you are,” and we thank you.

Research by the authors on computational methods was supported in part by the U.S. National Science Foundation and the U.S. Department of Energy.

# Preface to the Second Edition (1992)

Our aim in writing the original edition of Numerical Recipes was to provide a book that combined general discussion, analytical mathematics, algorithmics, and actual working programs. The success of the first edition puts us now in a difficult, though hardly unenviable, position. We wanted, then and now, to write a book that is informal, fearlessly editorial, unesoteric, and above all useful. There is a danger that, if we are not careful, we might produce a second edition that is weighty, balanced, scholarly, and boring.

It is a mixed blessing that we know more now than we did six years ago. Then, we were making educated guesses, based on existing literature and our own research, about which numerical techniques were the most important and robust. Now, we have the benefit of direct feedback from a large reader community. Letters to our alter-ego enterprise, Numerical Recipes Software, are in the thousands per year. (Please, don’t telephone us.) Our post office box has become a magnet for letters pointing out that we have omitted some particular technique, well known to be important in a particular field of science or engineering. We value such letters and digest them carefully, especially when they point us to specific references in the literature.

The inevitable result of this input is that this second edition of Numerical Recipes is substantially larger than its predecessor, in fact about $50 \%$ larger in both words and number of included programs (the latter now numbering well over 300). “Don’t let the book grow in size,” is the advice that we received from several wise colleagues. We have tried to follow the intended spirit of that advice, even as we violate the letter of it. We have not lengthened, or increased in difficulty, the book’s principal discussions of mainstream topics. Many new topics are presented at this same accessible level. Some topics, both from the earlier edition and new to this one, are now set in smaller type that labels them as being “advanced.” The reader who ignores such advanced sections completely will not, we think, find any lack of continuity in the shorter volume that results.

Here are some highlights of the new material in this second edition:

- a new chapter on integral equations and inverse methods   
- a detailed treatment of multigrid methods for solving elliptic partial differential equations routines for band-diagonal linear systems improved routines for linear algebra on sparse matrices Cholesky and $\boldsymbol { \mathcal { Q } R }$ decomposition orthogonal polynomials and Gaussian quadratures for arbitrary weight functions methods for calculating numerical derivatives   
- Pade approximants and rational Chebyshev approximation´ Bessel functions, and modified Bessel functions, of fractional order and several other new special functions improved random number routines quasi-random sequences routines for adaptive and recursive Monte Carlo integration in high-dimensional spaces   
- globally convergent methods for sets of nonlinear equations   
- simulated annealing minimization for continuous control spaces   
- fast Fourier transform (FFT) for real data in two and three dimensions   
- fast Fourier transform using external storage improved fast cosine transform routines wavelet transforms   
Fourier integrals with upper and lower limits spectral analysis on unevenly sampled data Savitzky-Golay smoothing filters fitting straight line data with errors in both coordinates a two-dimensional Kolmogorov-Smirnoff test the statistical bootstrap method embedded Runge-Kutta-Fehlberg methods for differential equations high-order methods for stiff differential equations   
a new chapter on “less-numerical” algorithms, including Huffman and arithmetic coding, arbitrary precision arithmetic, and several other topics

Consult the Preface to the first edition, following, or the Contents, for a list of the more “basic” subjects treated.

# Acknowledgments

It is not possible for us to list by name here all the readers who have made useful suggestions; we are grateful for these. In the text, we attempt to give specific attribution for ideas that appear to be original and are not known in the literature. We apologize in advance for any omissions.

Some readers and colleagues have been particularly generous in providing us with ideas, comments, suggestions, and programs for this second edition. We especially want to thank George Rybicki, Philip Pinto, Peter Lepage, Robert Lupton, Douglas Eardley, Ramesh Narayan, David Spergel, Alan Oppenheim, Sallie Baliunas, Scott Tremaine, Glennys Farrar, Steven Block, John Peacock, Thomas Loredo, Matthew Choptuik, Gregory Cook, L. Samuel Finn, P. Deuflhard, Harold Lewis, Peter Weinberger, David Syer, Richard Ferch, Steven Ebstein, Bradley Keister, and William Gould. We have been helped by Nancy Lee Snyder’s mastery of a complicated TEX manuscript. We express appreciation to our editors Lauren Cowles and Alan Harvey at Cambridge University Press, and to our production editor Russell Hahn. We remain, of course, grateful to the individuals acknowledged in the Preface to the first edition.

Special acknowledgment is due to programming consultant Seth Finkelstein, who wrote, rewrote, or influenced many of the routines in this book, as well as in its Fortran-language twin and the companion Example books. Our project has benefited enormously from Seth’s talent for detecting, and following the trail of, even very slight anomalies (often compiler bugs, but occasionally our errors), and from his good programming sense. To the extent that this edition of Numerical Recipes in $C$ has a more graceful and “C-like” programming style than its predecessor, most of the credit goes to Seth. (Of course, we accept the blame for the Fortranish lapses that still remain.)

We prepared this book for publication on DEC and Sun workstations running the UNIX operating system and on a $4 8 6 / 3 3 ~ \mathrm { P C }$ compatible running MS-DOS $5 . 0 /$ Windows 3.0. We enthusiastically recommend the principal software used: GNU Emacs, TEX, Perl, Adobe Illustrator, and PostScript. Also used were a variety of C compilers — too numerous (and sometimes too buggy) for individual acknowledgment. It is a sobering fact that our standard test suite (exercising all the routines in this book) has uncovered compiler bugs in many of the compilers tried. When possible, we work with developers to see that such bugs get fixed; we encourage interested compiler developers to contact us about such arrangements.

WHP and SAT acknowledge the continued support of the U.S. National Science Foundation for their research on computational methods. DARPA support is acknowledged for $\ S 1 3 . 1 0$ on wavelets.

# Preface to the First Edition (1985)

We call this book Numerical Recipes for several reasons. In one sense, this book is indeed a “cookbook” on numerical computation. However, there is an important distinction between a cookbook and a restaurant menu. The latter presents choices among complete dishes in each of which the individual flavors are blended and disguised. The former — and this book — reveals the individual ingredients and explains how they are prepared and combined.

Another purpose of the title is to connote an eclectic mixture of presentational techniques. This book is unique, we think, in offering, for each topic considered, a certain amount of general discussion, a certain amount of analytical mathematics, a certain amount of discussion of algorithmics, and (most important) actual implementations of these ideas in the form of working computer routines. Our task has been to find the right balance among these ingredients for each topic. You will find that for some topics we have tilted quite far to the analytic side; this where we have felt there to be gaps in the “standard” mathematical training. For other topics, where the mathematical prerequisites are universally held, we have tilted toward more indepth discussion of the nature of the computational algorithms, or toward practical questions of implementation.

We admit, therefore, to some unevenness in the “level” of this book. About half of it is suitable for an advanced undergraduate course on numerical computation for science or engineering majors. The other half ranges from the level of a graduate course to that of a professional reference. Most cookbooks have, after all, recipes at varying levels of complexity. An attractive feature of this approach, we think, is that the reader can use the book at increasing levels of sophistication as his/her experience grows. Even inexperienced readers should be able to use our most advanced routines as black boxes. Having done so, we hope that these readers will subsequently go back and learn what secrets are inside.

If there is a single dominant theme in this book, it is that practical methods of numerical computation can be simultaneously efficient, clever, and — important — clear. The alternative viewpoint, that efficient computational methods must necessarily be so arcane and complex as to be useful only in “black box” form, we firmly reject.

Our purpose in this book is thus to open up a large number of computational black boxes to your scrutiny. We want to teach you to take apart these black boxes and to put them back together again, modifying them to suit your specific needs. We assume that you are mathematically literate, i.e., that you have the normal mathematical preparation associated with an undergraduate degree in a physical science, or engineering, or economics, or a quantitative social science. We assume that you know how to program a computer. We do not assume that you have any prior formal knowledge of numerical analysis or numerical methods.

The scope of Numerical Recipes is supposed to be “everything up to, but not including, partial differential equations.” We honor this in the breach: First, we do have one introductory chapter on methods for partial differential equations. Second, we obviously cannot include everything else. All the so-called “standard” topics of a numerical analysis course have been included in this book: linear equations, interpolation and extrapolation, integration, nonlinear root finding, eigensystems, and ordinary differential equations. Most of these topics have been taken beyond their standard treatments into some advanced material that we have felt to be particularly important or useful.

Some other subjects that we cover in detail are not usually found in the standard numerical analysis texts. These include the evaluation of functions and of particular special functions of higher mathematics; random numbers and Monte Carlo methods; sorting; optimization, including multidimensional methods; Fourier transform methods, including FFT methods and other spectral methods; two chapters on the statistical description and modeling of data; and two-point boundary value problems, both shooting and relaxation methods.

# Acknowledgments

Many colleagues have been generous in giving us the benefit of their numerical and computational experience, in providing us with programs, in commenting on the manuscript, or with general encouragement. We particularly wish to thank George Rybicki, Douglas Eardley, Philip Marcus, Stuart Shapiro, Paul Horowitz, Bruce Musicus, Irwin Shapiro, Stephen Wolfram, Henry Abarbanel, Larry Smarr, Richard Muller, John Bahcall, and A.G.W. Cameron.

We also wish to acknowledge two individuals whom we have never met: Forman Acton, whose 1970 textbook Numerical Methods That Work (New York: Harper and Row) has surely left its stylistic mark on us; and Donald Knuth, both for his series of books on The Art of Computer Programming (Reading, MA: Addison-Wesley), and for TEX, the computer typesetting language that immensely aided production of this book.

Research by the authors on computational methods was supported in part by the U.S. National Science Foundation.

# License and Legal Information

You must read this section if you intend to use the code in this book on a computer. You’ll need to read the following Disclaimer of Warranty, acquire a Numerical Recipes software license, and get the code onto your computer. Without the license, which can be the limited, free “immediate license” under terms described below, this book is intended as a text and reference book, for reading and study purposes only.

For purposes of licensing, the electronic version of the Numerical Recipes book is equivalent to the paper version. It is not equivalent to a Numerical Recipes software license, which must still be acquired separately or as part of a combined electronic product. For information on Numerical Recipes electronic products, go to http://www.nr.com/electronic.

# Disclaimer of Warranty

We make no warranties, express or implied, that the programs contained in this volume are free of error, or are consistent with any particular standard of merchantability, or that they will meet your requirements for any particular application. They should not be relied on for solving a problem whose incorrect solution could result in injury to a person or loss of property. If you do use the programs in such a manner, it is at your own risk. The authors and publisher disclaim all liability for direct or consequential damages resulting from your use of the programs.

# The Restricted, Limited Free License

We recognize that readers may have an immediate, urgent wish to copy a small amount of code from this book for use in their own applications. If you personally keyboard no more than 10 routines from this book into your computer, then we authorize you (and only you) to use those routines (and only those routines) on that single computer. You are not authorized to transfer or distribute the routines to any other person or computer, nor to have any other person keyboard the programs into a computer on your behalf. We do not want to hear bug reports from you, because experience has shown that virtually all reported bugs in such cases are typing errors! This free license is not a GNU General Public License.

# Regular Licenses

When you purchase a code subscription or one-time code download from the Numerical Recipes Web site (http://www.nr.com), or when you buy physical Numerical Recipes media published by Cambridge University Press, you automatically get a Numerical Recipes Personal Single-User License. This license lets you personally use Numerical Recipes code on any one computer at a time, but not to allow anyone else access to the code. You may also, under this license, transfer precompiled, executable programs incorporating the code to other, unlicensed, users or computers, providing that (i) your application is noncommercial (i.e., does not involve the selling of your program for a fee); (ii) the programs were first developed, compiled, and successfully run by you; and (iii) our routines are bound into the programs in such a manner that they cannot be accessed as individual routines and cannot practicably be unbound and used in other programs. That is, under this license, your program user must not be able to use our programs as part of a program library or “mix-and-match” workbench. See the Numerical Recipes Web site for further details.

Businesses and organizations that purchase code subscriptions, downloads, or media, and that thus acquire one or more Numerical Recipes Personal Single-User Licenses, may permanently assign those licenses, in the number acquired, to individual employees. In most cases, however, businesses and organizations will instead want to purchase Numerical Recipes licenses “by the seat,” allowing them to be used by a pool of individuals rather than being individually permanently assigned. See http://www.nr.com/licenses for information on such licenses.

Instructors at accredited educational institutions who have adopted this book for a course may purchase on behalf of their students one-semester subscriptions to both the electronic version of the Numerical Recipes book and to the Numerical Recipes code. During the subscription term, students may download, view, save, and print all of the book and code. See http://www.nr.com/licenses for further information.

Other types of corporate licenses are also available. Please see the Numerical Recipes Web site.

# About Copyrights on Computer Programs

Like artistic or literary compositions, computer programs are protected by copyright. Generally it is an infringement for you to copy into your computer a program from a copyrighted source. (It is also not a friendly thing to do, since it deprives the program’s author of compensation for his or her creative effort.) Under copyright law, all “derivative works” (modified versions, or translations into another computer language) also come under the same copyright as the original work.

Copyright does not protect ideas, but only the expression of those ideas in a particular form. In the case of a computer program, the ideas consist of the program’s methodology and algorithm, including the necessary sequence of steps adopted by the programmer. The expression of those ideas is the program source code (particularly any arbitrary or stylistic choices embodied in it), its derived object code, and any other derivative works.

If you analyze the ideas contained in a program, and then express those ideas in your own completely different implementation, then that new program implementation belongs to you. That is what we have done for those programs in this book that are not entirely of our own devising. When programs in this book are said to be “based” on programs published in copyright sources, we mean that the ideas are the same. The expression of these ideas as source code is our own. We believe that no material in this book infringes on an existing copyright.

# Trademarks

Several registered trademarks appear within the text of this book. Words that are known to be trademarks are shown with an initial capital letter. However, the capitalization of any word is not an expression of the authors’ or publisher’s opinion as to whether or not it is subject to proprietary rights, nor is it to be regarded as affecting the validity of any trademark.

Numerical Recipes, NR, and nr.com (when identifying our products) are trademarks of Numerical Recipes Software.

# Attributions

The fact that ideas are legally “free as air” in no way supersedes the ethical requirement that ideas be credited to their known originators. When programs in this book are based on known sources, whether copyrighted or in the public domain, published or “handed-down,” we have attempted to give proper attribution. Unfortunately, the lineage of many programs in common circulation is often unclear. We would be grateful to readers for new or corrected information regarding attributions, which we will attempt to incorporate in subsequent printings.

# Routines by Chapter and Section

Previous editions included a table of all the routines in the book, along with a short description, arranged by chapter and section. This information is now available as an interactive Web page at http://www.nr.com/routines. The following illustration gives the idea.

![](images/e16191e2c8a5b45b1d6703ac229894737e9e0483a4b67b99b22effc61144124f.jpg)

# 1.0 Introduction

This book is supposed to teach you methods of numerical computing that are practical, efficient, and (insofar as possible) elegant. We presume throughout this book that you, the reader, have particular tasks that you want to get done. We view our job as educating you on how to proceed. Occasionally we may try to reroute you briefly onto a particularly beautiful side road; but by and large, we will guide you along main highways that lead to practical destinations.

Throughout this book, you will find us fearlessly editorializing, telling you what you should and shouldn’t do. This prescriptive tone results from a conscious decision on our part, and we hope that you will not find it irritating. We do not claim that our advice is infallible! Rather, we are reacting against a tendency, in the textbook literature of computation, to discuss every possible method that has ever been invented, without ever offering a practical judgment on relative merit. We do, therefore, offer you our practical judgments whenever we can. As you gain experience, you will form your own opinion of how reliable our advice is. Be assured that it is not perfect!

We presume that you are able to read computer programs in $\mathrm { C } { + } { + }$ . The question, “Why $\mathrm { C } { + } { + } ? ^ { \circ }$ , is a complicated one. For now, suffice it to say that we wanted a language with a C-like syntax in the small (because that is most universally readable by our audience), which had a rich set of facilities for object-oriented programming (because that is an emphasis of this third edition), and which was highly backwardcompatible with some old, but established and well-tested, tricks in numerical programming. That pretty much led us to $\mathrm { C } { + } { + }$ , although Java (and the closely related $\mathbf { C } \# \mathbf { \Gamma } _ { \ }$ ) were close contenders.

Honesty compels us to point out that in the 20-year history of Numerical Recipes, we have never been correct in our predictions about the future of programming languages for scientific programming, not once! At various times we convinced ourselves that the wave of the scientific future would be . . . Fortran . . . Pascal . . . C . . . Fortran 90 (or 95 or 2000) . . . Mathematica . . . Matlab . . . $\mathrm { C } { + } { + }$ or Java . . . . Indeed, several of these enjoy continuing success and have significant followings (not including Pascal!). None, however, currently command a majority, or even a large plurality, of scientific users.

With this edition, we are no longer trying to predict the future of programming languages. Rather, we want a serviceable way of communicating ideas about scientific programming. We hope that these ideas transcend the language, $\mathrm { C } { + + }$ , in which we are expressing them.

When we include programs in the text, they look like this:

# void flmoon(const Int n, const Int nph, Int &jd, Doub &frac) {

Our routines begin with an introductory comment summarizing their purpose and explaining their calling sequence. This routine calculates the phases of the moon. Given an integer n and a code nph for the phase desired $\mathbf { \hat { n } p h } = \mathbf { 0 }$ for new moon, 1 for first quarter, 2 for full, 3 for last quarter), the routine returns the Julian Day Number jd, and the fractional part of a day frac to be added to it, of the $\mathrm { n } t h$ such phase since January, 1900. Greenwich Mean Time is assumed.

const Doub RAD $\scriptstyle 1 = 3$ .141592653589793238/180.0;   
Int i;   
Doub am,as,c,t,t2,xtra;   
$\mathtt { C } = \mathtt { n } +$ nph/4.0; This is how we comment an individual line. t=c/1236.85;   
t2=t\*t;   
as ${ } = { }$ 359.2242+29.105356\*c; You aren’t really intended to understand am $\mid =$ 306.0253+385.816918\*c+0.010730\*t2; this algorithm, but it does work! jd=2415020+28\*n+7\*nph;   
xtra=0.75933+1.53058868\*c+((1.178e-4)-(1.55e-7)\*t)\*t2;   
if (nph $\scriptstyle = = 0$ || nph $\scriptstyle = = \ 2$ )   
xtra $+ =$ (0.1734-3.93e-4\*t)\*sin(RAD\*as)-0.4068\*sin(RAD\*am);   
else if (nph $\mathbf { \Phi } = \mathbf { \Phi } 1$ || nph $\scriptstyle = = \ 3$ )   
xtra $+ =$ (0.1721-4.0e-4\*t)\*sin(RAD\*as)-0.6280\*sin(RAD\*am);   
else throw("nph is unknown in flmoon"); This indicates an error condition. $\mathrm { i } =$ Int(xtra $> = \ 0 . 0$ ? floor(xtra) : ceil(xtra-1.0));   
jd $+ = \pm$ ;   
frac $=$ xtra-i;

Note our convention of handling all errors and exceptional cases with a statement like throw("some error message");. Since $\mathrm { C } { + } { + }$ has no built-in exception class for type char\*, executing this statement results in a fairly rude program abort. However we will explain in $\ S 1 . 5 . 1$ how to get a more elegant result without having to modify the source code.

# 1.0.1 What Numerical Recipes Is Not

We want to use the platform of this introductory section to emphasize what Numerical Recipes is not:

1. Numerical Recipes is not a textbook on programming, or on best programming practices, or on $\mathrm { C } { + } { + }$ , or on software engineering. We are not opposed to good programming. We try to communicate good programming practices whenever we can — but only incidentally to our main purpose, which is to teach how practical numerical methods actually work. The unity of style and subordination of function to standardization that is necessary in a good programming (or software engineering) textbook is just not what we have in mind for this book. Each section in this book has as its focus a particular computational method. Our goal is to explain and illustrate that method as clearly as possible. No single programming style is best for all such methods, and, accordingly, our style varies from section to section.

2. Numerical Recipes is not a program library. That may surprise you if you are one of the many scientists and engineers who use our source code regularly. What makes our code not a program library is that it demands a greater intellectual commitment from the user than a program library ought to do. If you haven’t read a routine’s accompanying section and gone through the routine line by line to understand how it works, then you use it at great peril! We consider this a feature, not a bug, because our primary purpose is to teach methods, not provide packaged solutions. This book does not include formal exercises, in part because we consider each section’s code to be the exercise: If you can understand each line of the code, then you have probably mastered the section.

There are some fine commercial program libraries [1,2] and integrated numerical environments [3-5] available. Comparable free resources are available, both program libraries [6,7] and integrated environments [8-10]. When you want a packaged solution, we recommend that you use one of these. Numerical Recipes is intended as a cookbook for cooks, not a restaurant menu for diners.

# 1.0.2 Frequently Asked Questions

This section is for people who want to jump right in.

1. How do I use NR routines with my own program?

The easiest way is to put a bunch of #include’s at the top of your program. Always start with $\mathtt { n r 3 . h }$ , since that defines some necessary utility classes and functions (see $\ S 1 . 4$ for a lot more about this). For example, here’s how you compute the mean and variance of the Julian Day numbers of the first 20 full moons after January 1900. (Now there’s a useful pair of quantities!)

#include "nr3.h" #include "calendar.h" #include "moment.h"

Int main(void) { const Int NTOT=20; Int i,jd,nph $^ { = 2 }$ ; Doub frac,ave,vrnce; VecDoub data(NTOT); for ( $\scriptstyle \dot { 1 } = 0$ ;i<NTOT; $\dot { \bf 1 } + +$ ) { flmoon(i,nph,jd,frac); data[i] $=$ jd; avevar(data,ave,vrnce); cout << "Average $= 1 1 1 < <$ setw(12) << ave; cout << " Variance $=$ " << setw(13) << vrnce << endl; return 0;   
}

#

Be sure that the NR source code files are in a place that your compiler can find them to #include. Compile and run the above file. (We can’t tell you how to do this part.) Output should be something like this:

Average $=$ 2.41532e+06 Variance $=$

30480.7

2. Yes, but where do I actually get the NR source code as computer files?

You can buy a code subscription, or a one-time code download, at the Web site http://www.nr.com, or you can get the code on media published by Cambridge

![](images/6ff18adecccf563fa0c8cc13e651764aae8454117ed701b33e9705569c4ca150.jpg)  
Figure 1.0.1. The interactive page located at http://www.nr.com/dependencies sorts out the dependencies for any combination of Numerical Recipes routines, giving an ordered list of the necessary #include files.

University Press (e.g., from Amazon.com or your favorite online or physical bookstore). The code comes with a personal, single-user license (see License and Legal Information on p. xix). The reason that the book (or its electronic version) and the code license are sold separately is to help keep down the price of each. Also, making these products separate meets the needs of more users: Your company or educational institution may have a site license — ask them.

3. How do I know which files to #include? It’s hard to sort out the dependencies among all the routines.

In the margin next to each code listing is the name of the source code file that it is in. Make a list of the source code files that you are using. Then go to http://www.nr.com/dependencies and click on the name of each source code file. The interactive Web page will return a list of the necessary #includes, in the correct order, to satisfy all dependencies. Figure 1.0.1 will give you an idea of how this works.

4. What is all this Doub, Int, VecDoub, etc., stuff?

We always use defined types, not built-in types, so that they can be redefined if necessary. The definitions are in $\mathtt { n r 3 . h }$ . Generally, as you can guess, Doub means double, Int means int, and so forth. Our convention is to begin all defined types with an uppercase letter. VecDoub is a vector class type. Details on our types are in $\ S 1 . 4$ .

# 5. What are Numerical Recipes Webnotes?

Numerical Recipes Webnotes are documents, accessible on the Web, that include some code implementation listings, or other highly specialized topics, that are not included in the paper version of the book. A list of all Webnotes is at http://www.nr.com/webnotes. By moving some specialized material into Webnotes, we are able to keep down the size and price of the paper book. Webnotes are automatically included in the electronic version of the book; see next question.

<table><tr><td colspan="2">Tested Operating Systems and Compilers</td></tr><tr><td>O/S</td><td>Compiler</td></tr><tr><td>MicrosoftWindows XP SP2 Microsoft Windows XP SP2 MicrosoftWindows XP SP2</td><td>Visual C++ ver.14.00(Visual Studio 2005) Visual C++ ver.13.10(Visual Studio 2003) Intel C++ Compiler ver. 9.1</td></tr></table>

6. I am a post-paper person. I want Numerical Recipes on my laptop. Where do I get the complete, fully electronic version?

A fully electronic version of Numerical Recipes is available by annual subscription. You can subscribe instead of, or in addition to, owning a paper copy of the book. A subscription is accessible via the Web, downloadable, printable, and, unlike any paper version, always up to date with the latest corrections. Since the electronic version does not share the page limits of the printed version, it will grow over time by the addition of completely new sections, available only electronically. This, we think, is the future of Numerical Recipes and perhaps of technical reference books generally. We anticipate various electronic formats, changing with time as technologies for display and rights management continuously improve: We place a big emphasis on user convenience and usability. See http://www.nr.com/electronic for further information.

# 7. Are there bugs in NR?

Of course! By now, most NR code has the benefit of long-time use by a large user community, but new bugs are sure to creep in. Look at http://www.nr.com for information about known bugs, or to report apparent new ones.

# 1.0.3 Computational Environment and Program Validation

The code in this book should run without modification on any compiler that implements the ANSI/ISO $\mathrm { C } { + } { + }$ standard, as described, for example, in Stroustrup’s book [11].

As surrogates for the large number of hardware and software configurations, we have tested all the code in this book on the combinations of operating systems and compilers shown in the table above.

In validating the code, we have taken it directly from the machine-readable form of the book’s manuscript, so that we have tested exactly what is printed. (This does not, of course, mean that the code is bug-free!)

# 1.0.4 About References

You will find references, and suggestions for further reading, listed at the end of most sections of this book. References are cited in the text by bracketed numbers like this [12].

We do not pretend to any degree of bibliographical completeness in this book. For topics where a substantial secondary literature exists (discussion in textbooks, reviews, etc.) we often limit our references to a few of the more useful secondary sources, especially those with good references to the primary literature. Where the existing secondary literature is insufficient, we give references to a few primary sources that are intended to serve as starting points for further reading, not as complete bibliographies for the field.

Since progress is ongoing, it is inevitable that our references for many topics are already, or will soon become, out of date. We have tried to include older references that are good for “forward” Web searching: A search for more recent papers that cite the references given should lead you to the most current work.

Web references and URLs present a problem, because there is no way for us to guarantee that they will still be there when you look for them. A date like $2 0 0 7 +$ means “it was there in 2007.” We try to give citations that are complete enough for you to find the document by Web search, even if it has moved from the location listed.

The order in which references are listed is not necessarily significant. It reflects a compromise between listing cited references in the order cited, and listing suggestions for further reading in a roughly prioritized order, with the most useful ones first.

# 1.0.5 About “Advanced Topics"

Material set in smaller type, like this, signals an “advanced topic,” either one outside of the main argument of the chapter, or else one requiring of you more than the usual assumed mathematical background, or else (in a few cases) a discussion that is more speculative or an algorithm that is less well tested. Nothing important will be lost if you skip the advanced topics on a first reading of the book.

Here is a function for getting the Julian Day Number from a calendar date.

Int julday(const Int mm, const Int id, const Int iyyy) {

In this routine julday returns the Julian Day Number that begins at noon of the calendar date specified by month mm, day id, and year iyyy, all integer variables. Positive year signifies A.D.; negative, B.C. Remember that the year after 1 B.C. was 1 A.D.

const Int IGREG=15+31\*(10+12\*1582); Gregorian Calendar adopted Oct. 15, 1582.   
Int ja,jul,jy=iyyy,jm;   
if (jy $\scriptstyle = = 0 .$ ) throw("julday: there is no year zero.");   
if (jy $< ~ 0$ ) $^ { + + }$ jy;   
if $\left( \mathbf { m } \right) > 2 \mathbf { \Gamma }$ ) { $\scriptstyle { \mathrm { j m } } = { \mathrm { m m } } + 1$ ;   
} else { --jy; jm=mm+13;   
}   
jul $=$ Int(floor(365.25\*jy)+floor(30.6001\*jm)+id+1720995);   
if (id+31\*(mm+12\*iyyy) $> =$ IGREG) Test whether to change to Gregorian Calja=Int(0.01\*jy); endar. jul $+ =$ 2-ja+Int(0.25\*ja);   
}   
return jul;

And here is its inverse.

void caldat(const Int julian, Int &mm, Int &id, Int &iyyy) { Inverse of the function julday given above. Here julian is input as a Julian Day Number, and the routine outputs mm,id, and iyyy as the month, day, and year on which the specified Julian Day started at noon.

const Int IGREG $=$ 2299161;   
Int ja,jalpha,jb,jc,jd,je;   
if (julian $> =$ IGREG) { Cross-over to Gregorian Calendar produces this correcjalpha=Int((Doub(julian-1867216)-0.25)/36524.25); tion. ja=julian+1+jalpha-Int(0.25\*jalpha);   
} else if (julian $< ~ 0$ ) { Make day number positive by adding integer number of ja=julian+36525 $^ *$ (1-julian/36525); Julian centuries, then subtract them off   
} else at the end. ja=julian;   
jb=ja+1524;   
jc $: =$ Int(6680. $^ { 0 + }$ (Doub(jb-2439870)-122.1)/365.25);   
jd=Int(365\*jc+(0.25\*jc));   
je $=$ Int((jb-jd)/30.6001);   
id=jb-jd-Int(30.6001\*je);   
mm=je-1;   
if (mm > 12) $\mathrm { m m } \mathrm { ~ \ -- ~ } 1 2$ ;   
iyyy=jc-4715;   
if (mm $>$ 2) --iyyy;   
if (iyyy $\scriptstyle < = 0$ ) --iyyy;   
if (julian $<$ 0) iyyy $- =$ 100\*(1-julian/36525);

As an exercise, you might try using these functions, along with flmoon in $\ S 1 . 0$ , to search for future occurrences of a full moon on Friday the 13th. (Answers, in time zone GMT minus 5: 9/13/2019 and 8/13/2049.) For additional calendrical algorithms, applicable to various historical calendars, see [13].

# CITED REFERENCES AND FURTHER READING:

Visual Numerics, $^ { 2 0 0 7 + }$ , IMSL Numerical Libraries, at http://www.vni.com.[1]   
Numerical Algorithms Group, $^ { 2 0 0 7 + }$ , NAG Numerical Library, at http://www.nag.co.uk.[2]   
Wolfram Research, Inc., $^ { 2 0 0 7 + }$ , Mathematica, at http://www.wolfram.com.[3]   
The MathWorks, Inc., $^ { 2 0 0 7 + }$ , MATLAB, at http://www.mathworks.com.[4]   
Maplesoft, Inc., $^ { 2 0 0 7 + }$ , Maple, at http://www.maplesoft.com.[5]   
GNU Scientific Library, $^ { 2 0 0 7 + }$ , at http://www.gnu.org/software/gsl.[6]   
Netlib Repository, $^ { 2 0 0 7 + }$ , at http://www.netlib.org.[7]   
Scilab Scientific Software Package, $^ { 2 0 0 7 + }$ , at http://www.scilab.org.[8]   
GNU Octave, $^ { 2 0 0 7 + }$ , at http://www.gnu.org/software/octave.[9]   
R Software Environment for Statistical Computing and Graphics, $^ { 2 0 0 7 + }$ , at http://www.r-project.org.[10]   
Stroustrup, B. 1997, The $C { + + }$ Programming Language, 3rd ed. (Reading, MA: Addison-Wesley).[11]   
Meeus, J. 1982, Astronomical Formulae for Calculators, 2nd ed., revised and enlarged (Richmond, VA: Willmann-Bell).[12]   
Hatcher, D.A. 1984, “Simple Formulae for Julian Day Numbers and Calendar Dates,” Quarterly Journal of the Royal Astronomical Society,vol.25,pp.53-55; see also op.cit.1985,vol.26, pp. 151–155, and 1986, vol. 27, pp. 506–507.[13]

# 1.1 Error, Accuracy, and Stability

Computers store numbers not with infinite precision but rather in some approximation that can be packed into a fixed number of bits (binary digits) or bytes (groups of 8 bits). Almost all computers allow the programmer a choice among several different such representations or data types. Data types can differ in the number of bits utilized (the wordlength), but also in the more fundamental respect of whether the stored number is represented in fixed-point (like int) or floating-point (like float or double) format.

A number in integer representation is exact. Arithmetic between numbers in integer representation is also exact, with the provisos that (i) the answer is not outside the range of (usually, signed) integers that can be represented, and (ii) that division is interpreted as producing an integer result, throwing away any integer remainder.

# 1.1.1 Floating-Point Representation

In a floating-point representation, a number is represented internally by a sign bit $S$ (interpreted as plus or minus), an exact integer exponent $E$ , and an exactly represented binary mantissa $M$ . Taken together these represent the number

$$
S \times M \times b ^ { E - e }
$$

where $b$ is the base of the representation $b = 2$ almost always), and $e$ is the bias of the exponent, a fixed integer constant for any given machine and representation.

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=7 colspan=1>float</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>1-254</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>(-1)$ × 2E-127 ×1.F</td></tr><tr><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>nonzero</td><td rowspan=1 colspan=1>(-1)$ × 2-126 ×0.F*</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>+0.0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-0.0</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>255</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>+8</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>255</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>255</td><td rowspan=1 colspan=1>nonzero</td><td rowspan=1 colspan=1>NaN</td></tr><tr><td rowspan=7 colspan=1>double</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>1-2046</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>(-1)$ × 2E-1023 × 1.F</td></tr><tr><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>nonzero</td><td rowspan=1 colspan=1>(-1)$ × 2-1022 ×0.F*</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>+0.0</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-0.0</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2047</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>+8</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2047</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>2047</td><td rowspan=1 colspan=1>nonzero</td><td rowspan=1 colspan=1>NaN</td></tr><tr><td rowspan=1 colspan=5>*unnormalized values</td></tr></table>

Several floating-point bit patterns can in principle represent the same number. If $b = 2$ , for example, a mantissa with leading (high-order) zero bits can be left-shifted, i.e., multiplied by a power of 2, if the exponent is decreased by a compensating amount. Bit patterns that are “as left-shifted as they can be” are termed normalized.

Virtually all modern processors share the same floating-point data representations, namely those specified in IEEE Standard 754-1985 [1]. (For some discussion of nonstandard processors, see $\ S 2 2 . 2 .$ ) For 32-bit float values, the exponent is represented in 8 bits (with $e = 1 2 7 _ { \cdot }$ ), the mantissa in 23; for 64-bit double values, the exponent is 11 bits (with $e = 1 0 2 3$ ), the mantissa, 52. An additional trick is used for the mantissa for most nonzero floating values: Since the high-order bit of a properly normalized mantissa is always one, the stored mantissa bits are viewed as being preceded by a “phantom” bit with the value 1. In other words, the mantissa $M$ has the numerical value $1 . F$ , where $F$ (called the fraction) consists of the bits (23 or 52 in number) that are actually stored. This trick gains a little “bit” of precision.

Here are some examples of IEEE 754 representations of double values:

$$
 \begin{array} { l } { { 0 \ { 1 1 1 1 1 1 1 1 1 1 \ 0 0 0 0 \ ( + 4 8 \bmod { \mathrm { z e r e s } } ) = + 1 \times 2 ^ { 1 0 2 3 - 1 0 2 3 } \times 1 . 0 _ { 2 } = 1 . } } \\ { { \mathrm { 1 } } \ { 0 \ 1 1 1 1 1 1 1 1 \ 0 0 0 0 ( + 4 8 \bmod { \mathrm { z e r e s } } ) = - 1 \times 2 ^ { 1 0 2 3 - 1 0 2 3 } \times 1 . 0 _ { 2 } = - 1 . } } \\ { { 0 \ 1 1 1 1 1 1 1 1 1 1 \ 1 0 0 0 ( + 4 8 \bmod { \mathrm { z e r e s } } ) = + 1 \times 2 ^ { 1 0 2 3 - 1 0 2 3 } \times 1 . 1 _ { 2 } = 1 . } } \\ { { 0 \ 0 \ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ( + 4 8 \bmod { z e r e s } ) = + 1 \times 2 ^ { 1 0 2 4 - 1 0 2 3 } \times 1 . 0 _ { 2 } = 2 . } } \\ { { 0 \ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ( + 4 8 \bmod { z e r e s } ) = + 1 \times 2 ^ { 1 0 2 4 - 1 0 2 3 } \times 1 . 0 _ { 2 } = 2 . } } \\ { { 0 \ 1 8 2 0 0 0 0 0 0 0 0 0 0 0 1 \ 1 0 1 0 ( + 4 8 \bmod { z e r e s } ) = { + } + 1 \times 2 ^ { 1 0 2 5 - 1 0 2 3 } \times 1 . 1 0 1 0 _ { 2 } = 6 } } \end{array} }
$$

You can examine the representation of any value by code like this:

union Udoub { double d; unsigned char c[8];   
};   
void main() { Udoub u; $\iota . \mathsf { d } \ = \ 6 . 5$ ; for (int $\mathbf { i = } 7 ; \mathbf { i > = } 0 ; \mathbf { i - } - )$ ) printf("%02x",u.c[i]); printf( $" \mathrm { \textmu } \mathrm { \textmu } \mathrm { \textmu } \mathrm { \textmu } \mathrm { \textmu } \mathrm { \textmu } \mathrm { \Sigma }$ ;   
}

This is C, and deprecated style, but it will work. On most processors, including Intel Pentium and successors, you’ll get the printed result 401a000000000000, which (writing out each hex digit as four binary digits) is the last line in equation (1.1.2). If you get the bytes (groups of two hex digits) in reverse order, then your processor is big-endian instead of little-endian: The IEEE 754 standard does not specify (or care) in which order the bytes in a floating-point value are stored.

The IEEE 754 standard includes representations of positive and negative infinity, positive and negative zero (treated as computationally equivalent, of course), and also NaN (“not a number”). The table on the previous page gives details of how these are represented.

The reason for representing some unnormalized values, as shown in the table, is to make “underflow to zero” more graceful. For a sequence of smaller and smaller values, after you pass the smallest normalizable value (with magnitude $2 ^ { - 1 2 7 }$ or $2 ^ { - 1 0 2 3 }$ ; see table), you start right-shifting the leading bit of the mantissa. Although you gradually lose precision, you don’t actually underflow to zero until 23 or 52 bits later.

When a routine needs to know properties of the floating-point representation, it can reference the numeric_limits class, which is part of the $\mathrm { C } { + } { + }$ Standard Library. For example, numeric_limits<double>::min() returns the smallest normalized double value, usually $2 ^ { - 1 0 2 2 } \approx 2 . 2 3 \times 1 0 ^ { - 3 0 8 }$ . For more on this, see $\ S 2 2 . 2$ .

# 1.1.2 Roundoff Error

Arithmetic among numbers in floating-point representation is not exact, even if the operands happen to be exactly represented (i.e., have exact values in the form of equation 1.1.1). For example, two floating numbers are added by first right-shifting (dividing by two) the mantissa of the smaller (in magnitude) one and simultaneously increasing its exponent until the two operands have the same exponent. Low-order (least significant) bits of the smaller operand are lost by this shifting. If the two operands differ too greatly in magnitude, then the smaller operand is effectively replaced by zero, since it is right-shifted to oblivion.

The smallest (in magnitude) floating-point number that, when added to the floating-point number 1.0, produces a floating-point result different from 1.0 is termed the machine accuracy $\epsilon _ { m }$ . IEEE 754 standard float has $\epsilon _ { m }$ about $1 . 1 9 \times 1 0 ^ { - 7 }$ , while double has about $2 . 2 2 \times 1 0 ^ { - 1 6 }$ . Values like this are accessible as, e.g., numeric _limits <double>::epsilon(). (A more detailed discussion of machine characteristics is in $\ S 2 2 . 2 .$ ) Roughly speaking, the machine accuracy $\epsilon _ { m }$ is the fractional accuracy to which floating-point numbers are represented, corresponding to a change of one in the least significant bit of the mantissa. Pretty much any arithmetic operation among floating numbers should be thought of as introducing an additional fractional error of at least $\epsilon _ { m }$ . This type of error is called roundoff error.

It is important to understand that $\epsilon _ { m }$ is not the smallest floating-point number that can be represented on a machine. That number depends on how many bits there are in the exponent, while $\epsilon _ { m }$ depends on how many bits there are in the mantissa.

Roundoff errors accumulate with increasing amounts of calculation. If, in the course of obtaining a calculated value, you perform $N$ such arithmetic operations, you might be so lucky as to have a total roundoff error on the order of $\sqrt { N } \epsilon _ { m }$ , if the roundoff errors come in randomly up or down. (The square root comes from a random-walk.) However, this estimate can be very badly off the mark for two reasons:

(1) It very frequently happens that the regularities of your calculation, or the peculiarities of your computer, cause the roundoff errors to accumulate preferentially in one direction. In this case the total will be of order $N \epsilon _ { m }$ .

(2) Some especially unfavorable occurrences can vastly increase the roundoff error of single operations. Generally these can be traced to the subtraction of two very nearly equal numbers, giving a result whose only significant bits are those (few) low-order ones in which the operands differed. You might think that such a “coincidental” subtraction is unlikely to occur. Not always so. Some mathematical expressions magnify its probability of occurrence tremendously. For example, in the familiar formula for the solution of a quadratic equation,

$$
x = { \frac { - b + { \sqrt { b ^ { 2 } - 4 a c } } } { 2 a } }
$$

the addition becomes delicate and roundoff-prone whenever $b > 0$ and $| a c | \ll b ^ { 2 }$ . $\mathrm { T n } \ S 5 . 6$ we will learn how to avoid the problem in this particular case.)

# 1.1.3 Truncation Error

Roundoff error is a characteristic of computer hardware. There is another, different, kind of error that is a characteristic of the program or algorithm used, independent of the hardware on which the program is executed. Many numerical algorithms compute “discrete” approximations to some desired “continuous” quantity. For example, an integral is evaluated numerically by computing a function at a discrete set of points, rather than at “every” point. Or, a function may be evaluated by summing a finite number of leading terms in its infinite series, rather than all infinity terms. In cases like this, there is an adjustable parameter, e.g., the number of points or of terms, such that the “true” answer is obtained only when that parameter goes to infinity. Any practical calculation is done with a finite, but sufficiently large, choice of that parameter.

The discrepancy between the true answer and the answer obtained in a practical calculation is called the truncation error. Truncation error would persist even on a hypothetical, “perfect” computer that had an infinitely accurate representation and no roundoff error. As a general rule there is not much that a programmer can do about roundoff error, other than to choose algorithms that do not magnify it unnecessarily (see discussion of “stability” below). Truncation error, on the other hand, is entirely under the programmer’s control. In fact, it is only a slight exaggeration to say that clever minimization of truncation error is practically the entire content of the field of numerical analysis!

Most of the time, truncation error and roundoff error do not strongly interact with one another. A calculation can be imagined as having, first, the truncation error that it would have if run on an infinite-precision computer, “plus” the roundoff error associated with the number of operations performed.

# 1.1.4 Stability

Sometimes an otherwise attractive method can be unstable. This means that any roundoff error that becomes “mixed into” the calculation at an early stage is successively magnified until it comes to swamp the true answer. An unstable method would be useful on a hypothetical, perfect computer; but in this imperfect world it is necessary for us to require that algorithms be stable — or if unstable that we use them with great caution.

Here is a simple, if somewhat artificial, example of an unstable algorithm: Suppose that it is desired to calculate all integer powers of the so-called “Golden Mean,” the number given by

$$
\phi \equiv \frac { \sqrt { 5 } - 1 } { 2 } \approx 0 . 6 1 8 0 3 3 9 8
$$

It turns out (you can easily verify) that the powers $\phi ^ { n }$ satisfy a simple recursion relation,

$$
\phi ^ { n + 1 } = \phi ^ { n - 1 } - \phi ^ { n }
$$

Thus, knowing the first two values $\phi ^ { 0 } = 1$ and $\phi ^ { 1 } = 0 . 6 1 8 0 3 3 9 8$ , we can successively apply (1.1.5) performing only a single subtraction, rather than a slower

multiplication by $\phi$ , at each stage.

Unfortunately, the recurrence (1.1.5) also has another solution, namely the value $- { \frac { 1 } { 2 } } ( { \sqrt { 5 } } + { \dot { 1 } } )$ . Since the recurrence is linear, and since this undesired solution has magnitude greater than unity, any small admixture of it introduced by roundoff errors will grow exponentially. On a typical machine, using a 32-bit float, (1.1.5) starts to give completely wrong answers by about $n = 1 6$ , at which point $\phi ^ { n }$ is down to only $1 0 ^ { - 4 }$ . The recurrence (1.1.5) is unstable and cannot be used for the purpose stated.

We will encounter the question of stability in many more sophisticated guises later in this book.

# CITED REFERENCES AND FURTHER READING:

IEEE, 1985, ANSI/IEEE Std 754–1985: IEEE Standard for Binary Floating-Point Numbers (New York: IEEE).[1]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 1.   
Kahaner, D., Moler, C., and Nash, S. 1989, Numerical Methods and Software (Englewood Cliffs, NJ: Prentice-Hall), Chapter 2.   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 1 . 3$ .   
Wilkinson, J.H. 1964, Rounding Errors in Algebraic Processes (Englewood Cliffs, NJ: Prentice-Hall).

# 1.2 C Family Syntax

Not only $\mathrm { C } { + } { + }$ , but also Java, C#, and (to varying degrees) other computer languages, share a lot of small-scale syntax with the older C language [1]. By small scale, we mean operations on built-in types, simple expressions, control structures, and the like. In this section, we review some of the basics, give some hints on good programming, and mention some of our conventions and habits.

# 1.2.1 Operators

A first piece of advice might seem superfluous if it were not so often ignored: You should learn all the C operators and their precedence and associativity rules. You might not yourself want to write

$$
\textbf { \em n } < < \textbf { \em 1 } \ | \ \textbf { \em 1 }
$$

as a synonym for $2 \ast \mathtt { n } + 1$ (for positive integer n), but you definitely do need to be able to see at a glance that

$$
\texttt { n } < < \texttt { 1 } + \texttt { 1 }
$$

is not at all the same thing! Please study the table on the next page while you brush your teeth every night. While the occasional set of unnecessary parentheses, for clarity, is hardly a sin, code that is habitually overparenthesized is annoying and hard to read.

<table><tr><td colspan="3"> Operator Precedence and Associativity Rules in C and C++</td></tr><tr><td>：：</td><td> scope resolution</td><td>left-to-right</td></tr><tr><td>0</td><td>function call</td><td>left-to-right</td></tr><tr><td>[</td><td>array element (subscripting)</td><td></td></tr><tr><td>：</td><td>member selection</td><td></td></tr><tr><td>1&gt;</td><td>member selection (by pointer)</td><td></td></tr><tr><td>++</td><td> post increment</td><td>right-to-left</td></tr><tr><td></td><td> post decrement</td><td></td></tr><tr><td>！</td><td>logical not</td><td>right-to-left</td></tr><tr><td>~</td><td>bitwise complement</td><td></td></tr><tr><td></td><td>unary minus</td><td></td></tr><tr><td>++</td><td> pre increment</td><td></td></tr><tr><td></td><td> pre decrement</td><td></td></tr><tr><td>&amp;</td><td>address of</td><td></td></tr><tr><td>*</td><td>contents of (dereference)</td><td></td></tr><tr><td>new</td><td>create</td><td></td></tr><tr><td>delete</td><td>destroy</td><td></td></tr><tr><td>(type)</td><td> cast to type</td><td></td></tr><tr><td>sizeof</td><td> size in bytes</td><td></td></tr><tr><td>*</td><td>multiply</td><td>left-to-right</td></tr><tr><td>/</td><td>divide</td><td></td></tr><tr><td>%</td><td>remainder</td><td></td></tr><tr><td>+</td><td>add</td><td>left-to-right</td></tr><tr><td>1</td><td>subtract</td><td></td></tr><tr><td>会</td><td>bitwise left shift</td><td>left-to-right</td></tr><tr><td>&gt;&gt;</td><td>bitwise right shift</td><td></td></tr><tr><td></td><td>arithmetic less than</td><td>left-to-right</td></tr><tr><td>&lt; 》</td><td> arithmetic greater than</td><td></td></tr><tr><td>&lt;=</td><td> arithmetic less than or equal to</td><td></td></tr><tr><td>&gt;=</td><td> arithmetic greater than or equal to</td><td></td></tr><tr><td>==</td><td> arithmetic equal</td><td>left-to-right</td></tr><tr><td>!=</td><td> arithmetic not equal</td><td></td></tr><tr><td>&amp;</td><td>bitwise and</td><td>left-to-right</td></tr><tr><td>，</td><td>bitwise exclusive or</td><td>left-to-right</td></tr><tr><td>一</td><td>bitwise or</td><td>left-to-right</td></tr><tr><td>&amp;&amp;</td><td>logical and</td><td>left-to-right</td></tr><tr><td>=</td><td>logical or</td><td>left-to-right</td></tr><tr><td>？ ：</td><td>conditional expression</td><td> right-to-left</td></tr><tr><td></td><td>assignment operator</td><td>right-to-left</td></tr><tr><td></td><td> also += -= *= /= %=</td><td></td></tr><tr><td></td><td>&lt;&lt;= &gt;&gt;= &amp;= ^= |=</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>=</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td></table>

# 1.2.2 Control Structures

These should all be familiar to you.

Iteration. In C family languages simple iteration is performed with a for loop, for example

for ( $\scriptstyle { \dot { \mathsf { J } } } = 2$ ;j<=1000;j++) { b[j]=a[j-1]; a[j-1]=j;   
}

It is conventional to indent the block of code that is acted upon by the control structure, leaving the structure itself unindented. We like to put the initial curly brace on the same line as the for statement, instead of on the next line. This saves a full line of white space, and our publisher loves us for it.

Conditional. The conditional or if structure looks, in full generality, like this:

if (...) {   
else if (...) {   
}   
else 3

However, since compound-statement curly braces are required only when there is more than one statement in a block, the if construction can be somewhat less explicit than that shown above. Some care must be exercised in constructing nested if clauses. For example, consider the following:

if (b > 3) if $\textsf { \textsf { a } } > \textsf { 3 }$ ) b $+ = ~ 1$ ;   
else b $\scriptstyle - = \ 1$ ;

/\* questionable! \*/

As judged by the indentation used on successive lines, the intent of the writer of this code is the following: ‘If b is greater than 3 and a is greater than 3, then increment b. If b is not greater than 3, then decrement b.’ According to the rules, however, the actual meaning is ‘If b is greater than 3, then evaluate a. If a is greater than 3, then increment b, and if a is less than or equal to 3, decrement b.’ The point is that an else clause is associated with the most recent open if statement, no matter how you lay it out on the page. Such confusions in meaning are easily resolved by the inclusion of braces that clarify your intent and improve the program. The above fragment should be written as

if (b > 3) { if (a > 3) b += 1;   
} else { b $\scriptstyle - = \ 1$ ;   
}

While iteration. Alternative to the for iteration is the while structure, for example,

while $( \mathrm { ~ n ~ } < \mathrm { ~ 1 0 0 0 ~ }$ ) { n $\ast = ~ 2$ ; $\mathrm { ~ j ~ } + = \mathrm { ~ 1 ~ }$ ;   
}

The control clause (in this case $\mathrm { ~ n ~ } < \mathrm { ~ 1 0 0 0 ~ }$ ) is evaluated before each iteration. If the clause is not true, the enclosed statements will not be executed. In particular, if this code is encountered at a time when n is greater than or equal to 1000, the statements will not even be executed once.

Do-While iteration. Companion to the while iteration is a related control structure that tests its control clause at the end of each iteration:

do { $\texttt { n } * = \texttt { 2 } ;$ ${ \mathrm { ~ \ j ~ \ } ^ { + = } \ 1 ; }$   
} while (n < 1000);

In this case, the enclosed statements will be executed at least once, independent of the initial value of n.

Break and Continue. You use the break statement when you have a loop that is to be repeated indefinitely until some condition tested somewhere in the middle of the loop (and possibly tested in more than one place) becomes true. At that point you wish to exit the loop and proceed with what comes after it. In C family languages the simple break statement terminates execution of the innermost for, while, do, or switch construction and proceeds to the next sequential instruction. A typical usage might be

for(;;) { if (...) break;   
}

Companion to break is continue, which transfers program control to the end of the body of the smallest enclosing for, while, or do statement, but just inside that body’s terminating curly brace. In general, this results in the execution of the next loop test associated with that body.

# 1.2.3 How Tricky Is Too Tricky?

Every programmer is occasionally tempted to write a line or two of code that is so elegantly tricky that all who read it will stand in awe of its author’s intelligence. Poetic justice is that it is usually that same programmer who gets stumped, later on, trying to understand his or her own creation. You might momentarily be proud of yourself at writing the single line

$$
k = ( 2 \mathrm { - j } ) * ( 1 \mathrm { + } 3 \mathrm { * j } ) / 2 ;
$$

if you want to permute cyclically one of the values ${ \mathrm { ~ \ j ~ } = \left( 0 , 1 , 2 \right) }$ into respectively $\mathbf { k } = ( 1 , 2 , 0 )$ . You will regret it later, however. Better, and likely also faster, is

k=j+1;   
if (k == 3) k=0;

On the other hand, it can also be a mistake, or at least suboptimal, to be too ploddingly literal, as in

switch (j) { case 0: $\mathrm { k } = 1$ ; break; case 1: $\mathrm { k } = 2$ ; break; case 2: $\mathtt { k } = 0$ ; break; default: { cerr << "unexpected value for j"; exit(1); }   
}

This (or similar) might be the house style if you are one of $1 0 ^ { 5 }$ programmers working for a megacorporation, but if you are programming for your own research, or within a small group of collaborators, this kind of style will soon cause you to lose the forest for the trees. You need to find the right personal balance between obscure trickery and boring prolixity. A good rule is that you should always write code that is slightly less tricky than you are willing to read, but only slightly.

There is a fine line between being tricky (bad) and being idiomatic (good). Idioms are short expressions that are sufficiently common, or sufficiently self-explanatory, that you can use them freely. For example, testing an integer n’s even- or odd-ness by

if (n & 1) ...

is, we think, much preferable to

$$
{ \mathrm { i f } } \quad ( \textrm { n \% 2 } = \textrm { \scriptsize 1 } ) \quad . \ . \ .
$$

We similarly like to double a positive integer by writing

$$
\mathbf { n _ { \lambda } } < < = \mathbf { \lambda } 1 ;
$$

or construct a mask of $\mathbf { n }$ bits by writing

$$
( 1 ~ < < ~ \mathtt { n } ) ~ - ~ 1
$$

and so forth.

Some idioms are worthy of consideration even when they are not so immediately obvious. S.E. Anderson [2] has collected a number of “bit-twiddling hacks,” of which we show three here:

The test

if ( $\left( \mathtt { v } \& \left( \mathtt { v } - 1 \right) \right) = = 0 $ ) {} Is a power of 2 or zero.

tests whether $\mathtt { v }$ is a power of 2. If you care about the case $\tau = 0$ , you have to write

if $\scriptstyle \big ( \mathtt { V } \& \& \big ( \big ( \mathtt { V } \& \big ( \mathtt { V } - 1 \big ) \big ) = = 0 \big )$ ) {} Is a power of 2.

The idiom

for $( \mathsf { c } = 0 ; \mathsf { v } ; \mathsf { c } + + ) \texttt { v } \& = \texttt { v } - \texttt { 1 ; }$

gives as $^ { \texttt { c } }$ the number of set $( = 1$ ) bits in a positive or unsigned integer v (destroying $\mathtt { v }$ in the process). The number of iterations is only as many as the number of bits set.

The idiom

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } & { } &  \end{array}
$$

rounds a positive (or unsigned) 32-bit integer v up to the next power of 2 that is $\geq \tau$ . When we use the bit-twiddling hacks, we’ll include an explanatory comment in the code.

# 1.2.4 Utility Macros or Templated Functions

The file nr3.h includes, among other things, definitions for the functions

MAX(a,b) MIN(a,b) SWAP(a,b) SIGN(a,b)

These are all self-explanatory, except possibly the last. SIGN(a,b) returns a value with the same magnitude as a and the same sign as b. These functions are all implemented as templated inline functions, so that they can be used for all argument types that make sense semantically. Implementation as macros is also possible.

# CITED REFERENCES AND FURTHER READING:

Harbison, S.P., and Steele, G.L., Jr. 2002, C: A Reference Manual, 5th ed. (Englewood Cliffs, NJ: Prentice-Hall).[1]   
Anderson, S.E. 2006, “Bit Twiddling Hacks,” at http://graphics.stanford.edu/\~seander/ bithacks.html.[2]

# 1.3 Objects, Classes, and Inheritance

An object or class (the terms are interchangeable) is a program structure that groups together some variables, or functions, or both, in such a way that all the included variables or functions “see” each other and can interact intimately, while most of this internal structure is hidden from other program structures and units. Objects make possible object-oriented programming (OOP), which has become recognized as the almost unique successful paradigm for creating complex software. The key insight in OOP is that objects have state and behavior. The state of the object is described by the values stored in its member variables, while the possible behavior is determined by the member functions. We will use objects in other ways as well.

The terminology surrounding OOP can be confusing. Objects, classes, and structures pretty much refer to the same thing. Member functions in a class are often referred to as methods belonging to that class. In $\mathrm { C } { + } { + }$ , objects are defined with either the keyword class or the keyword struct. These differ, however, in the details of how rigorously they hide the object’s internals from public view. Specifically,

struct SomeName { is defined as being the same as class SomeName { public:

In this book we always use struct. This is not because we deprecate the use of public and private access specifiers in OOP, but only because such access control would add little to understanding the underlying numerical methods that are the focus of this book. In fact, access specifiers could impede your understanding, because you would be constantly moving things from private to public (and back again) as you program different test cases and want to examine different internal, normally private, variables.

Because our classes are declared by struct, not class, use of the word “class” is potentially confusing, and we will usually try to avoid it. So “object” means struct, which is really a class!

If you are an OOP beginner, it is important to understand the distinction between defining an object and instantiating it. You define an object by writing code like this:

# struct Twovar {

Doub a,b; Twovar(const Doub aa, const Doub bb) : a(aa), b(bb) {} Doub sum() {return a+b;} Doub diff() {return a-b;} };

This code does not create a Twovar object. It only tells the compiler how to create one when, later in your program, you tell it to do so, for example by a declaration like,

# Twovar mytwovar(3.,5.);

which invokes the Twovar constructor and creates an instance of (or instantiates) a Twovar. In this example, the constructor also sets the internal variables a and b to 3 and 5, respectively. You can have any number of simultaneously existing, noninteracting, instances:

Twovar anothertwovar(4.,6.);   
Twovar athirdtwovar(7.,8.);

We have already promised you that this book is not a textbook in OOP, or the $\mathrm { C } { + + }$ language; so we will go no farther here. If you need more, good references are [1-4].

# 1.3.1 Simple Uses of Objects

We use objects in various ways, ranging from trivial to quite complex, depending on the needs of the specific numerical method that is being discussed. As mentioned in $\ S 1 . 0$ , this lack of consistency means that Numerical Recipes is not a useful examplar of a program library (or, in an OOP context, a class library). It also means that, somewhere in this book, you can probably find an example of every possible way to think about objects in numerical computing! (We hope that you will find this a plus.)

Object for Grouping Functions. Sometimes an object just collects together a group of closely related functions, not too differently from the way that you might use a namespace. For example, a simplification of Chapter 6’s object Erf looks like:

struct Erf { No constructor needed. Doub erf(Doub x); Doub erfc(Doub x); Doub inverf(Doub p); Doub inverfc(Doub p); Doub erfccheb(Doub z);   
};

As will be explained in $\ S 6 . 2$ , the first four methods are the ones intended to be called by the user, giving the error function, complementary error function, and the two corresponding inverse functions. But these methods share some code and also use common code in the last method, erfccheb, which the user will normally ignore completely. It therefore makes sense to group the whole collection as an $\mathtt { E r f }$ object. About the only disadvantage of this is that you must instantiate an Erf object before you can use (say) the erf function:

Erf myerf;   
Doub $\mathtt { y } =$ myerf.erf(3.);

The name myerf is arbitrary.

Instantiating the object doesn’t actually do anything here, because Erf contains no variables (i.e., has no stored state). It just tells the compiler what local name you are going to use in referring to its member functions. (We would normally use the name erf for the instance of Erf, but we thought that erf.erf(3.) would be confusing in the above example.)

Object for Standardizing an Interface. In $\ S 6 . 1 4$ we’ll discuss a number of useful standard probability distributions, for example, normal, Cauchy, binomial, Poisson, etc. Each gets its own object definition, for example,

struct Cauchydist { Doub mu, sig; Cauchydist(Doub mmu $\qquad = \ 0 .$ , Doub ssig $\ c = ~ 1 . )$ : mu(mmu), sig(ssig) {} Doub p(Doub x); Doub cdf(Doub x); Doub invcdf(Doub p);   
};

where the function $\mathtt { p }$ returns the probability density, the function cdf returns the cumulative distribution function (cdf), and the function invcdf returns the inverse of the cdf. Because the interface is consistent across all the different probability distributions, you can change which distribution a program is using by changing a single program line, for example from

Cauchydist mydist();

to

# Normaldist mydist();

All subsequent references to functions like mydist.p, mydist.cdf, and so on, are thus changed automatically. This is hardly OOP at all, but it can be very convenient.

Object for Returning Multiple Values. It often happens that a function computes more than one useful quantity, but you don’t know which one or ones the user is actually interested in on that particular function call. A convenient use of objects is to save all the potentially useful results and then let the user grab those that are of interest. For example, a simplified version of the Fitab structure in Chapter 15, which fits a straight line $y = a + b x$ to a set of data points xx and yy, looks like this:

struct Fitab { Doub a, b; Fitab(const VecDoub &xx, const VecDoub &yy); Constructor.   
};

(We’ll discuss VecDoub and related matters below, in $\ S 1 . 4 . $ The user calculates the fit by calling the constructor with the data points as arguments,

Fitab myfit(xx,yy);

Then the two “answers” $a$ and $b$ are separately available as myfit.a and myfit.b.   
We will see more elaborate examples throughout the book.

Objects That Save Internal State for Multiple Uses. This is classic OOP, worthy of the name. A good example is Chapter 2’s LUdcmp object, which (in abbreviated form) looks like this:

struct LUdcmp { Int n; MatDoub lu; LUdcmp(const MatDoub &a); Constructor. void solve(const VecDoub &b, VecDoub &x); void inverse(MatDoub &ainv); Doub det();   
};

This object is used to solve linear equations and/or invert a matrix. You use it by creating an instance with your matrix a as the argument in the constructor. The constructor then computes and stores, in the internal matrix lu, a so-called $L U$ decomposition of your matrix (see $\ S 2 . 3 \AA$ . Normally you won’t use the matrix lu directly (though you could if you wanted to). Rather, you now have available the methods solve(), which returns a solution vector $_ \texttt { x }$ for any right-hand side b, inverse(), which returns the inverse matrix, and det(), which returns the determinant of your matrix.

You can call any or all of LUdcmp’s methods in any order; you might well want to call solve multiple times, with different right-hand sides. If you have more than one matrix in your problem, you create a separate instance of LUdcmp for each one, for example,

# LUdcmp alu(a), aalu(aa);

after which alu.solve() and aalu.solve() are the methods for solving linear equations for each respective matrix, a and aa; alu.det() and aalu.det() return the two determinants; and so forth.

We are not finished listing ways to use objects: Several more are discussed in the next few sections.

# 1.3.2 Scope Rules and Object Destruction

This last example, LUdcmp, raises the important issue of how to manage an object’s time and memory usage within your program.

For a large matrix, the LUdcmp constructor does a lot of computation. You choose exactly where in your program you want this to occur in the obvious way, by putting the declaration

# LUdcmp alu(a);

in just that place. The important distinction between a non-OOP language (like C) and an OOP language (like $\mathrm { C } { + + }$ ) is that, in the latter, declarations are not passive instructions to the compiler, but executable statments at run-time.

The LUdcmp constructor also, for a large matrix, grabs a lot of memory, to store the matrix lu. How do you take charge of this? That is, how do you communicate that it should save this state for as long as you might need it for calls to methods like alu.solve(), but not indefinitely?

The answer lies in $\mathrm { C } { + } { + }$ ’s strict and predictable rules about scope. You can start a temporary scope at any point by writing an open bracket, “{”. You end that scope by a matching close bracket, $\mathbf { \Phi } ^ { \ast } \mathbf { \Phi } ^ { \ast }$ . You can nest scopes in the obvious way. Any objects that are declared within a scope are destroyed (and their memory resources returned) when the end of the scope is reached. An example might look like this:

MatDoub a(1000,1000); Create a big matrix,   
VecDoub b(1000),x(1000); and a couple of vectors. Begin temporary scope. LUdcmp alu(a); Create object alu. . alu.solve(b,x); Use alu.   
} End temporary scope. Resources in alu are freed.   
Doub d $=$ alu.det(); ERROR! alu is out of scope.

This example presumes that you have some other use for the matrix a later on. If not, then the the declaration of a should itself probably be inside the temporary scope.

Be aware that all program blocks delineated by braces are scope units. This includes the main block associated with a function definition and also blocks associated with control structures. In code like this,

for (;;) {LUdcmp alu(a);  
}

a new instance of alu is created at each iteration and then destroyed at the end of that iteration. This might sometimes be what you intend (if the matrix a changes on each iteration, for example); but you should be careful not to let it happen unintentionally.

# 1.3.3 Functions and Functors

Many routines in this book take functions as input. For example, the quadrature (integration) routines in Chapter 4 take as input the function $f ( x )$ to be integrated. For a simple case like $f ( x ) = x ^ { 2 }$ , you code such a function simply as

Doub f(const Doub x) { return x\*x; }

and pass f as an argument to the routine. However, it is often useful to use a more general object to communicate the function to the routine. For example, $f ( x )$ may depend on other variables or parameters that need to be communicated from the calling program. Or the computation of $f ( x )$ may be associated with other subcalculations or information from other parts of the program. In non-OOP programing, this communication is usually accomplished with global variables that pass the information “over the head” of the routine that receives the function argument f.

$\mathrm { C } { + + }$ provides a better and more elegant solution: function objects or functors. A functor is simply an object in which the operator () has been overloaded to play the role of returning a function value. (There is no relation between this use of the word functor and its different meaning in pure mathematics.) The case $f ( x ) = x ^ { 2 }$ would now be coded as

struct Square { Doub operator()(const Doub x) { return x\*x; }   
};

To use this with a quadrature or other routine, you declare an instance of Square

# Square g;

and pass $\mathsf { g }$ to the routine. Inside the quadrature routine, an invocation of $\mathtt { g } ( \mathtt { x } )$ returns the function value in the usual way.

In the above example, there’s no point in using a functor instead of a plain function. But suppose you have a parameter in the problem, for example, $f ( x ) =$ $c x ^ { p }$ , where $c$ and $p$ are to be communicated from somewhere else in your program. You can set the parameters via a constructor:

struct Contimespow { Doub c,p; Contimespow(const Doub cc, const Doub pp) : c(cc), p(pp) {} Doub operator()(const Doub x) { return c\*pow(x,p); }   
};

In the calling program, you might declare the instance of Contimespow by

Contimespow $\mathtt { h } ( 4 , , 0 . 5 )$ ; Communicate c and p to the functor.

and later pass h to the routine. Clearly you can make the functor much more complicated. For example, it can contain other helper functions to aid in the calculation of the function value.

So should we implement all our routines to accept only functors and not functions? Luckily, we don’t have to decide. We can write the routines so they can accept either a function or a functor. A routine accepting only a function to be integrated from $a$ to $b$ might be declared as

Doub someQuadrature(Doub func(const Doub), const Doub a, const Doub b);

To allow it to accept either functions or functors, we instead make it a templated function:

template <class T> Doub someQuadrature(T &func, const Doub a, const Doub b);

Now the compiler figures out whether you are calling someQuadrature with a function or a functor and generates the appropriate code. If you call the routine in one place in your program with a function and in another with a functor, the compiler will handle that too.

We will use this capability to pass functors as arguments in many different places in the book where function arguments are required. There is a tremendous gain in flexibility and ease of use.

As a convention, when we write Ftor, we mean a functor like Square or Contimespow above; when we write fbare, we mean a “bare” function like f above; and when we write ftor (all in lower case), we mean an instantiation of a functor, that is, something declared like

Ftor ftor(...);

Of course your names for functors and their instantiations will be different.

Slightly more complicated syntax is involved in passing a function to an object that is templated to accept either a function or functor. So if the object is

template <class T>   
struct SomeStruct { SomeStruct(T &func, constructor

we would instantiate it with a functor like this:

Ftor ftor; SomeStruct<Ftor> s(ftor, but with a function like this:

SomeStruct<Doub (const Doub)> s(fbare,

In this example, fbare takes a single const Doub argument and returns a Doub.   
You must use the arguments and return type for your specific case, of course.

# 1.3.4 Inheritance

Objects can be defined as deriving from other, already defined, objects. In such inheritance, the “parent” class is called a base class, while the “child” class is called a derived class. A derived class has all the methods and stored state of its base class, plus it can add any new ones.

“Is-a” Relationships. The most straightforward use of inheritance is to describe so-called is-a relationships. OOP texts are full of examples where the base class is ZooAnimal and a derived class is Lion. In other words, Lion “is-a” ZooAnimal. The base class has methods common to all ZooAnimals, for example eat() and sleep(), while the derived class extends the base class with additional methods specific to Lion, for example roar() and eat_visitor().

In this book we use is-a inheritance less often than you might expect. Except in some highly stylized situations, like optimized matrix classes (“triangular matrix is-a matrix”), we find that the diversity of tasks in scientific computing does not lend itself to strict is-a hierarchies. There are exceptions, however. For example, in Chapter 7, we define an object Ran with methods for returning uniform random deviates of various types (e.g., Int or Doub). Later in the chapter, we define objects for returning other kinds of random deviates, for example normal or binomial. These are defined as derived classes of Ran, for example,

struct Binomialdev : Ran {};

so that they can share the machinery already in Ran. This is a true is-a relationship, because “binomial deviate is-a random deviate.”

Another example occurs in Chapter 13, where objects Daub4, Daub4i, and Daubs are all derived from the Wavelet base class. Here Wavelet is an abstract base class or ABC [1,4] that has no content of its own. Rather, it merely specifies interfaces for all the methods that any Wavelet is required to have. The relationship is nevertheless is-a: “Daub4 is-a Wavelet”.

“Prerequisite” Relationships. Not for any dogmatic reason, but simply because it is convenient, we frequently use inheritance to pass on to an object a set of methods that it needs as prerequisites. This is especially true when the same set of prerequisites is used by more than one object. In this use of inheritance, the base class has no particular ZooAnimal unity; it may be a grab-bag. There is not a logical is-a relationship between the base and derived classes.

An example in Chapter 10 is Bracketmethod, which is a base class for several minimization routines, but which simply provides a common method for the initial bracketing of a minimum. In Chapter 7, the Hashtable object provides prerequisite methods to its derived classes Hash and Mhash, but one cannot say, “Mhash is-a Hashtable” in any meaningful way. An extreme example, in Chapter 6, is the base class Gauleg18, which does nothing except provide a bunch of constants for Gauss-Legendre integration to derived classes Beta and Gamma, both of which need them. Similarly, long lists of constants are provided to the routines StepperDopr853 and StepperRoss in Chapter 17 by base classes to avoid cluttering the coding of the algorithms.

Partial Abstraction. Inheritance can be used in more complicated or situationspecific ways. For example, consider Chapter 4, where elementary quadrature rules such as Trapzd and Midpnt are used as building blocks to construct more elaborate quadrature algorithms. The key feature these simple rules share is a mechanism for adding more points to an existing approximation to an integral to get the “next” stage of refinement. This suggests deriving these objects from an abstract base clase called Quadrature, which specifies that all objects derived from it must have a next() method. This is not a complete specification of a common is-a interface; it abstracts only one feature that turns out to be useful.

For example, in $\ S 4 . 6$ , the Stiel object invokes, in different situations, two different quadrature objects, Trapzd and DErule. These are not interchangeable. They have different constructor arguments and could not easily both be made ZooAnimals (as it were). Stiel of course knows about their differences. However, one of Stiel’s methods, quad(), doesn’t (and shouldn’t) know about these differences. It uses only the method next(), which exists, with different definitions, in both Trapzd and DErule.

While there are several different ways to deal with situations like this, an easy one is available once Trapzd and DErule have been given a common abstract base class Quadrature that contains nothing except a virtual interface to next. In a case like this, the base class is a minor design feature as far as the implementation of Stiel is concerned, almost an afterthought, rather than being the apex of a top-down design. As long as the usage is clear, there is nothing wrong with this.

Chapter 17, which discusses ordinary differential equations, has some even more complicated examples that combine inheritance and templating. We defer further discussion to there.

# CITED REFERENCES AND FURTHER READING:

Stroustrup, B. 1997, The $C { + } { + }$ Programming Language, 3rd ed. (Reading, MA: Addison-Wesley).[1] Lippman, S.B., Lajoie, J., and Moo, B.E. 2005, $C { + } { + }$ Primer, 4th ed. (Boston: Addison-Wesley).[2] Keogh, J., and Giannini, M. 2004, OOP Demystified (Emeryville, CA: McGraw-Hill/Osborne).[3] Cline, M., Lomow, G., and Girou, M. 1999, $C { + } { + }$ FAQs, 2nd ed. (Boston: Addison-Wesley).[4]

# 1.4 Vector and Matrix Objects

The $\mathrm { C } { + + }$ Standard Library [1] includes a perfectly good vector<> template class. About the only criticism that one can make of it is that it is so feature-rich that some compiler vendors neglect to squeeze the last little bit of performance out of its most elementary operations, for example returning an element by its subscript. That performance is extremely important in scientific applications; its occasional absence in $\mathrm { C } { + } { + }$ compilers is a main reason that many scientists still (as we write) program in C, or even in Fortran!

Also included in the $\mathrm { C } { + + }$ Standard Library is the class valarray<>. At one time, this was supposed to be a vector-like class that was optimized for numerical computation, including some features associated with matrices and multidimensional arrays. However, as reported by one participant,

The valarray classes were not designed very well. In fact, nobody tried to determine whether the final specification worked. This happened because nobody felt “responsible” for these classes. The people who introduced valarrays to the $\mathrm { C } { + + }$ standard library left the committee a long time before the standard was finished. [1]

The result of this history is that $\mathrm { C } { + } { + }$ , at least now, has a good (but not always reliably optimized) class for vectors and no dependable class at all for matrices or higher-dimensional arrays. What to do? We will adopt a strategy that emphasizes flexibility and assumes only a minimal set of properties for vectors and matrices. We will then provide our own, basic, classes for vectors and matrices. For most compilers, these are at least as efficient as vector $\vartriangle { \mathsf { { C } } } \ v { \mathbf { \{ \Lambda } } $ and other vector and matrix classes in common use. But if, for you, they’re not, then it is easy to change to a different set of classes, as we will explain.

# 1.4.1 Typedefs

Flexibility is achieved by having several layers of typedef type-indirection, resolved at compile time so that there is no run-time performance penalty. The first level of type-indirection, not just for vectors and matrices but for virtually all variables, is that we use user-defined type names instead of $\mathrm { C } { + } { + }$ fundamental types. These are defined in $\mathtt { n r 3 . h }$ . If you ever encounter a compiler with peculiar builtin types, these definitions are the “hook” for making any necessary changes. The complete list of such definitions is

<table><tr><td>NR Type</td><td>Usual Definition</td><td>Intent</td></tr><tr><td>Char</td><td>char</td><td rowspan="6">8-bit signed integer 8-bit unsigned integer 32-bit signed integer</td></tr><tr><td>Uchar</td><td>unsigned char</td></tr><tr><td>Int int</td><td></td></tr><tr><td>Uint unsigned int</td><td>32-bit unsigned integer</td></tr><tr><td>Llong</td><td>long long int 64-bit signed integer</td></tr><tr><td>Ullong</td><td>unsigned long long int 64-bit unsigned integer</td></tr><tr><td>Doub</td><td>double</td><td>64-bit floating point</td></tr><tr><td>Ldoub</td><td>long double</td><td>[reserved for future use]</td></tr><tr><td>Complex</td><td>complex&lt;double&gt;</td><td>2 × 64-bit floating complex</td></tr><tr><td>Bool</td><td>bool</td><td>true or false</td></tr></table>

An example of when you might need to change the typedefs in nr3.h is if your compiler’s int is not 32 bits, or if it doesn’t recognize the type long long int.

You might need to substitute vendor-specific types like (in the case of Microsoft) __int32 and $\_ { - } \mathtt { i n t } 6 4$ .

The second level of type-indirection returns us to the discussion of vectors and matrices. The vector and matrix types that appear in Numerical Recipes source code are as follows. Vectors: VecInt, VecUint, VecChar, VecUchar, VecCharp, VecLlong, VecUllong, VecDoub, VecDoubp, VecComplex, and VecBool. Matrices: MatInt, MatUint, MatChar, MatUchar, MatLlong, MatUllong, MatDoub, MatComplex, and MatBool. These should all be understandable, semantically, as vectors and matrices whose elements are the corresponding user-defined types, above. Those ending in a “p” have elements that are pointers, e.g., VecCharp is a vector of pointers to char, that is, char\*. If you are wondering why the above list is not combinatorially complete, it is because we don’t happen to use all possible combinations of Vec, Mat, fundamental type, and pointer in this book. You can add further analogous types as you need them.

Wait, there’s more! For every vector and matrix type above, we also define types with the same names plus one of the suffixes “_I”, “_O”, and “_IO”, for example VecDoub_IO. We use these suffixed types for specifying argument types in function definitions. The meaning, respectively, is that the argument is “input”, “output”, or “both input and output”. The $_ - \ I$ types are automatically defined to be const. We discuss this further in $\ S 1 . 5 . 2$ under the topic of const correctness.

It may seem capricious for us to define such a long list of types when a much smaller number of templated types would do. The rationale is flexibility: You have a hook into redefining each and every one of the types individually, according to your needs for program efficiency, local coding standards, const-correctness, or whatever. In fact, in $\mathtt { n r 3 . h }$ , all these types are typedef’d to one vector and one matrix class, along the following lines:

typedef NRvector<Int> VecInt, VecInt_O, VecInt_IO;   
typedef const NRvector<Int> VecInt_I;   
typedef NRvector<Doub> VecDoub, VecDoub_O, VecDoub_IO;   
typedef const NRvector<Doub> VecDoub_I;   
typedef NRmatrix<Int> MatInt, MatInt_O, MatInt_IO;   
typedef const NRmatrix<Int> MatInt_I;   
typedef NRmatrix<Doub> MatDoub, MatDoub_O, MatDoub_IO;   
typedef const NRmatrix<Doub> MatDoub_I;

So (flexibility, again) you can change the definition of one particular type, like VecDoub, or else you can change the implementation of all vectors by changing the definition of NRvector<>. Or, you can just leave things the way we have them in nr3.h. That ought to work fine in $9 9 . 9 \%$ of all applications.

# 1.4.2 Required Methods for Vector and Matrix Classes

The important thing about the vector and matrix classes is not what names they are typedef’d to, but what methods are assumed for them (and are provided in the NRvector and NRmatrix template classes). For vectors, the assumed methods are a subset of those in the $\mathrm { C } { + } { + }$ Standard Library vector $\cdot >$ class. If $\mathtt { v }$ is a vector of type NRvector ${ \mathrm { - } } \mathrm { T } >$ , then we assume the methods:

$\mathtt { v } ( )$ Constructor, zero-length vector.   
v(Int n) Constructor, vector of length n.   
v(Int n, const T &a) Constructor, initialize all elements to the value a.   
v(Int n, const T \*a) Constructor, initialize elements to values in a C-style array, a[0], a[1], : : :   
v(const NRvector &rhs) Copy constructor.   
v.size() Returns number of elements in v.   
v.resize(Int newn) Resizes v to size newn. We do not assume that contents are preserved.   
v.assign(Int newn, const T &a) Resize v to size newn, and set all elements to the value a.   
v[Int i] Element of v by subscript, either an l-value and an r-value.   
$\qquad \mathtt { v } =$ rhs Assignment operator. Resizes v if necessary and makes it a copy of the vector rhs.   
typedef T value_type; Makes T available externally (useful in templated functions or classes).

As we will discuss later in more detail, you can use any vector class you like with Numerical Recipes, as long as it provides the above basic functionality. For example, a brute force way to use the $\mathrm { C } { + } { + }$ Standard Library vector<> class instead of NRvector is by the preprocessor directive

# #define NRvector vector

(In fact, there is a compiler switch, _USESTDVECTOR_, in the file nr3.h that will do just this.)

The methods for matrices are closely analogous. If vv is a matrix of type NRmatrix<T>, then we assume the methods:

vv() Constructor, zero-length vector.   
vv(Int n, Int m) Constructor, ${ \mathfrak { n } } \times { \mathfrak { m } }$ matrix.   
vv(Int n, Int m, const T &a) Constructor, initialize all elements to the value a.   
vv(Int n, Int m, const T \*a) Constructor, initialize elements by rows to the values in a C-style array.   
vv(const NRmatrix &rhs) Copy constructor.   
vv.nrows() Returns number of rows n.   
vv.ncols() Returns number of columns m.   
vv.resize(Int newn, Int newm) Resizes vv to newn $\times$ newm. We do not assume that contents are preserved.   
vv.assign(Int newn, Int newm, Resizes vv to $\mathtt { n e w n } \times \mathtt { n e w m }$ , const t &a) and sets all elements to the value a.   
vv[Int i] Return a pointer to the first element in row i (not often used by itself).   
v[Int i][Int j] Element of vv by subscript, either an l-value and an r-value.   
vv = rhs Assignment operator. Resizes vv if necessary and makes it a copy of the matrix rhs.   
typedef T value_type; Makes T available externally.

For more precise specifications, see $\ S 1 . 4 . 3$

There is one additional property that we assume of the vector and matrix classes, namely that all of an object’s elements are stored in sequential order. For a vector, this means that its elements can be addressed by pointer arithmetic relative to the first element. For example, if we have

VecDoub a(100);   
Doub $\ast \boldsymbol { \mathrm b } ~ = ~ \& \boldsymbol { \mathrm [ 0 ] }$ ;

then a[i] and b[i] reference the same element, both as an l-value and as an rvalue. This capability is sometimes important for inner-loop efficiency, and it is also useful for interfacing with legacy code that can handle Doub\* arrays, but not VecDoub vectors. Although the original $\mathrm { C } { + + }$ Standard Library did not guarantee this behavior, all known implementations of it do so, and the behavior is now required by an amendment to the standard [2].

For matrices, we analogously assume that storage is by rows within a single sequential block so that, for example,

Int $\scriptstyle \mathtt { n } = 9 7$ , $\mathtt { m } = 1 0 3$ ;  
MatDoub $\mathtt { a } ( \mathtt { n } , \mathtt { m } )$ ;  
Doub \*b $=$ &a[0][0];

implies that a[i][j] and b $[ \mathrm { m } { * \mathrm { i } + \mathrm { j } } ]$ are equivalent.

A few of our routines need the capability of taking as an argument either a vector or else one row of a matrix. For simplicity, we usually code this using overloading, as, e.g.,

void someroutine(Doub \*v, Int m) { Version for a matrix row.   
}   
inline void someroutine(VecDoub &v) { Version for a vector. someroutine(&v[0],v.size());   
}

For a vector v, a call looks like someroutine(v), while for row i of a matrix vv it is someroutine(&vv[i][0],vv.ncols()). While the simpler argument vv[i] would in fact work in our implementation of NRmatrix, it might not work in some other matrix class that guarantees sequential storage but has the return type for a single subscript different from $^ { \mathrm { T } * }$ .

# 1.4.3 Implementations in nr3.h

For reference, here is a complete declaration of NRvector.

template <class T>   
class NRvector {   
private: int nn; Size of array, indices $0 \cdot \cdot \mathtt { n n } ^ { - 1 }$ . T \*v; Pointer to data array.   
public: NRvector(); Default constructor. explicit NRvector(int n); Construct vector of size n. NRvector(int n, const T &a); Initialize to constant value a. NRvector(int n, const T \*a); Initialize to values in C-style array a. NRvector(const NRvector &rhs); Copy constructor. NRvector & operator $\mathop { : = }$ (const NRvector &rhs); Assignment operator. typedef T value_type; Make T available. inline T & operator[](const int i); Return element number i. inline const T & operator[](const int i) const; const version. inline int size() const; Return size of vector. void resize(int newn); Resize, losing contents. void assign(int newn, const T &a); Resize and assign a to every element. \~NRvector(); Destructor.

The implementations are straightforward and can be found in the file $\mathtt { n r 3 . h }$ . The only issues requiring finesse are the consistent treatment of zero-length vectors and the avoidance of unnecessary resize operations.

A complete declaration of NRmatrix is

template <class T>   
class NRmatrix {   
private: int nn; Number of rows and columns. Index int mm; range is 0..nn-1, 0..mm-1. T \*\*v; Storage for data.   
public: NRmatrix(); Default constructor. NRmatrix(int n, int m); Construct ${ \mathfrak { n } } \times { \mathfrak { m } }$ matrix. NRmatrix(int n, int m, const T &a); Initialize to constant value a. NRmatrix(int n, int m, const T \*a); Initialize to values in C-style array a. NRmatrix(const NRmatrix &rhs); Copy constructor. NRmatrix & operator $^ { * = }$ (const NRmatrix &rhs); Assignment operator. typedef T value_type; Make T available. inline T\* operator[](const int i); Subscripting: pointer to row i. inline const $^ { \mathrm { T } * }$ operator[](const int i) const; const version. inline int nrows() const; Return number of rows. inline int ncols() const; Return number of columns. void resize(int newn, int newm); Resize, losing contents. void assign(int newn, int newm, const T &a); Resize and assign a to every element. \~NRmatrix(); Destructor.   
};

A couple of implementation details in NRmatrix are worth commenting on. The private variable $\ast \ast \tau$ points not to the data but rather to an array of pointers to the data rows. Memory allocation of this array is separate from the allocation of space for the actual data. The data space is allocated as a single block, not separately for each row. For matrices of zero size, we have to account for the separate possibilities that there are zero rows, or that there are a finite number of rows, but each with zero columns. So, for example, one of the constructors looks like this:

template <class T>   
NRmatrix<T>::NRmatrix(int n, int m) : nn(n), mm(m), v(n>0 ? new T\*[n] : NULL)   
{ int i,nel=m\*n; if (v) v[0] $=$ nel>0 ? new T[nel] : NULL; for ( $\dot { \bf 1 } = 1$ ;i<n; $\dot { 1 } + + \dot { 1 }$ ) v[i] $=$ v[i-1] + m;   
}

Finally, it matters a lot whether your compiler honors the inline directives in NRvector and NRmatrix above. If it doesn’t, then you may be doing full function calls, saving and restoring context within the processor, every time you address a vector or matrix element. This is tantamount to making $\mathrm { C } { + } { + }$ useless for most numerical computing! Luckily, as we write, the most commonly used compilers are all “honorable” in this respect.

# CITED REFERENCES AND FURTHER READING:

Josuttis, N.M. 1999, The $C { + } { + }$ Standard Library: A Tutorial and Reference (Boston: Addison-Wesley).[1] International Standardization Organization 2003, Technical Corrigendum ISO 14882:2003.[2]

# 1.5 Some Further Conventions and Capabilities

We collect in this section some further explanation of $\mathrm { C } { + } { + }$ language capabilities and how we use them in this book.

# 1.5.1 Error and Exception Handling

We already mentioned that we code error conditions with simple throw statements, like this

# throw("error foo in routine bah");

If you are programming in an environment that has a defined set of error classes, and you want to use them, then you’ll need to change these lines in the routines that you use. Alternatively, without any additional machinery, you can choose between a couple of different, useful behaviors just by making small changes in nr3.h.

By default, nr3.h redefines throw() by a preprocessor macro, #define throw(message) \ {printf("ERROR: %s\n in file %s at line %d\n", \ message,__FILE__,__LINE__); \ exit(1);}

This uses standard ANSI C features, also present in $\mathrm { C } { + } { + }$ , to print the source code file name and line number at which the error occurs. It is inelegant, but perfectly functional.

Somewhat more functional, and definitely more elegant, is to set nr3.h’s compiler switch _USENRERRORCLASS_, which instead substitutes the following code:

struct NRerror { char \*message; char \*file; int line; NRerror(char \*m, char \*f, int l) : message(m), file(f), line(l) {}   
};   
void NRcatch(NRerror err) { printf("ERROR: %s\n in file %s at line %d\n", err.message, err.file, err.line); exit(1);   
}

#define throw(message) throw(NRerror(message,__FILE__,__LINE__));

Now you have a (rudimentary) error class, NRerror, available. You use it by putting a try : : : catch control structure at any desired point (or points) in your code, for example (-2.9),

try Cholesky achol(a);   
}   
catch (NRerror err) { NRcatch(err);   
}

As shown, the use of the NRcatch function above simply mimics the behavior of the previous macro in the global context. But you don’t have to use NRcatch at all: You can substitute any code that you want for the body of the catch statement. If you want to distinguish between different kinds of exceptions that may be thrown, you can use the information returned in err. We’ll let you figure this out yourself. And of course you are welcome to add more complicated error classes to your own copy of $\mathtt { n r 3 . h }$ .

# 1.5.2 Const Correctness

Few topics in discussions about $\mathrm { C } { + } { + }$ evoke more heat than questions about the keyword const. We are firm believers in using const wherever possible, to achieve what is called “const correctness.” Many coding errors are automatically trapped by the compiler if you have qualified identifiers that should not change with const when they are declared. Also, using const makes your code much more readable: When you see const in front of an argument to a function, you know immediately that the function will not modify the object. Conversely, if const is absent, you should be able to count on the object being changed somewhere.

We are such strong const believers that we insert const even where it is theoretically redundant: If an argument is passed by value to a function, then the function makes a copy of it. Even if this copy is modified by the function, the original value is unchanged after the function exits. While this allows you to change, with impunity, the values of arguments that have been passed by value, this usage is error-prone and hard to read. If your intention in passing something by value is that it is an input variable only, then make it clear. So we declare a function $f ( x )$ as, for example,

# Doub f(const Doub x);

If in the function you want to use a local variable that is initialized to ${ \tt x }$ but then gets changed, define a new quantity — don’t use x. If you put const in the declaration, the compiler will not let you get this wrong.

Using const in your function arguments makes your function more general: Calling a function that expects a const argument with a non-const variable involves a “trivial” conversion. But trying to pass a const quantity to a non-const argument is an error.

A final reason for using const is that it allows certain user-defined conversions to be made. As discussed in [1], this can be useful if you want to use Numerical Recipes routines with another matrix/vector class library.

We now need to elaborate on what exactly const does for a nonsimple type such as a class that is an argument of a function. Basically, it guarantees that the object is not modified by the function. In other words, the object’s data members are unchanged. But if a data member is a pointer to some data, and the data itself is not a member variable, then the data can be changed even though the pointer cannot be.

Let’s look at the implications of this for a function f that takes an NRvector<Doub> argument a. To avoid unnecessary copying, we always pass vectors and matrices by reference. Consider the difference between declaring the argument of a function with and without const:

void f(NRvector<Doub> &a) versus void f(const NRvector<Doub> &a)

The const version promises that f does not modify the data members of a. But a statement like

inside the function definition is in principle perfectly OK — you are modifying the data pointed to, not the pointer itself.

“Isn’t there some way to protect the data?” you may ask. Yes, there is: You can declare the return type of the subscript operator, operator[], to be const. This is why there are two versions of operator[] in the NRvector class,

# T & operator[](const int i);const T & operator[](const int i) const;

The first form returns a reference to a modifiable vector element, while the second returns a nonmodifiable vector element (because the return type has a const in front).

But how does the compiler know which version to invoke when you just write a[i]? That is specified by the trailing word const in the second version. It refers not to the returned element, nor to the argument i, but to the object whose operator[] is being invoked, in our example the vector a. Taken together, the two versions say this to the compiler: “If the vector a is const, then transfer that const’ness to the returned element a[i]. If it isn’t, then don’t.”

The remaining question is thus how the compiler determines whether a is const. In our example, where a is a function argument, it is trivial: The argument is either declared as const or else it isn’t. In other contexts, a might be const because you originally declared it as such (and initialized it via constructor arguments), or because it is a const reference data member in some other object, or for some other, more arcane, reason.

As you can see, getting const to protect the data is a little complicated. Judging from the large number of matrix/vector libraries that follow this scheme, many people feel that the payoff is worthwhile. We urge you always to declare as const those objects and variables that are not intended to be modified. You do this both at the time an object is actually created and in the arguments of function declarations and definitions. You won’t regret making a habit of const correctness.

In $\ S 1 . 4$ we defined vector and matrix type names with trailing $_ - \ I$ labels, for example, VecDoub_I and MatInt_I. The _I, which stands for “input to a function,” means that the type is declared as const. (This is already done in the typedef statement; you don’t have to repeat it.) The corresponding labels $_ - 0$ and $_ - \pm 0$ are to remind you when arguments are not just non-const, but will actually be modified by the function in whose argument list they appear.

Having rightly put all this emphasis on const correctness, duty compels us also to recognize the existence of an alternative philosophy, which is to stick with the more rudimentary view “const protects the container, not the contents.” In this case you would want only one form of operator[], namely

# T & operator[](const int i) const;

It would be invoked whether your vector was passed by const reference or not. In both cases element i is returned as potentially modifiable. While we are opposed to this philosophically, it turns out that it does make possible a tricky kind of automatic type conversion that allows you to use your favorite vector and matrix classes instead of NRvector and NRmatrix, even if your classes use a syntax completely different from what we have assumed. For information on this very specialized application, see [1].

# 1.5.3 Abstract Base Class (ABC), or Template?

There is sometimes more than one good way to achieve some end in $\mathrm { C } { + + }$ . Heck, let’s be honest: There is always more than one way. Sometimes the differences amount to small tweaks, but at other times they embody very different views about the language. When we make one such choice, and you prefer another, you are going to be quite annoyed with us. Our defense against this is to avoid foolish consistencies, and to illustrate as many viewpoints as possible.

A good example is the question of when to use an abstract base class (ABC) versus a template, when their capabilities overlap. Suppose we have a function func that can do its (useful) thing on, or using, several different types of objects, call them ObjA, ObjB, and ObjC. Moreover, func doesn’t need to know much about the object it interacts with, only that it has some method tellme.

We could implement this setup as an abstract base class:

Abstract Base Class for objects with tellme.

Derived class.

Derived class.

struct ObjABC { virtual void tellme ${ \mathrm { ~  ~ \omega ~ } } ( \ k ) \ = \ 0$   
};   
struct ObjA : ObjABC { void tellme() {...}   
};   
struct ObjB : ObjABC { void tellme() {...}   
};   
struct ObjC : ObjABC { void tellme() {...}   
};   
void func(ObjABC &x) { ... x.tellme();   
}

Derived class.

References the appropriate tellme.

On the other hand, using a template, we can write code for func without ever seeing (or even knowing the names of) the objects for which it is intended:

template<class T>   
void func(T &x) { ... x.tellme();   
}

That certainly seems easier! Is it better?

Maybe. A disadvantage of templates is that the template must be available to the compiler every time it encounters a call to func. This is because it actually compiles a different version of func for every different type of argument T that it encounters. Unless your code is so large that it cannot easily be compiled as a single unit, however, this is not much of a disadvantage. On the other side, favoring templates, is the fact that virtual functions incur a small run-time penalty when they are called. But this is rarely significant.

The deciding factors in this example relate to software engineering, not performance, and are hidden in the lines with ellipses (...). We haven’t really told you how closely related ObjA, ObjB, and ObjC are. If they are close, then the ABC approach offers possibilities for putting more than just tellme into the base class. Putting things into the base class, whether data or pure virtual methods, lets the compiler enforce consistency across the derived classes. If you later write another derived object ObjD, its consistency will also be enforced. For example, the compiler will require you to implement a method in every derived class corresponding to every pure virtual method in the base class.

By contrast, in the template approach, the only enforced consistency will be that the method tellme exists, and this will only be enforced at the point in the code where func is actually called with an ObjD argument (if such a point exists), not at the point where ObjD is defined. Consistency checking in the template approach is thus somewhat more haphazard.

Laid-back programmers will opt for templates. Up-tight programmers will opt for ABCs. We opt for. . . both, on different occasions. There can also be other reasons, having to do with subtle features of class derivation or of templates, for choosing one approach over the other. We will point these out as we encounter them in later chapters. For example, in Chapter 17 we define an abstract base class called StepperBase for the various “stepper” routines for solving ODEs. The derived classes implement particular stepping algorithms, and they are templated so they can accept function or functor arguments (see $\ S 1 . 3 . 3 )$ .

# 1.5.4 NaN and Floating Point Exceptions

We mentioned in $\ S 1 . 1 . 1$ that the IEEE floating-point standard includes a representation for NaN, meaning “not a number.” NaN is distinct from positive and negative infinity, as well as from every representable number. It can be both a blessing and a curse.

The blessing is that it can be useful to have a value that can be used with meanings like “don’t process me” or “missing data” or “not yet initialized.” To use NaN in this fashion, you need to be able to set variables to it, and you need to be able to test for its having been set.

Setting is easy. The “approved” method is to use numeric_limits. In nr3.h the line

static const Doub NaN $=$ numeric_limits<Doub>::quiet_NaN();

defines a global value NaN, so that you can write things like

$$
\begin{array} { r } { \tt { x } = N a N ; } \end{array}
$$

at will. If you ever encounter a compiler that doesn’t do this right (it’s a pretty obscure corner of the standard library!), then try either

Uint proto_nan[2] $=$ 0xffffffff, 0x7fffffff;   
double NaN $\qquad = ~ *$ ( double\* )proto_nan;

(which assumes little-endian behavior; cf. $\ S 1 . 1 . 1 )$ or the self-explanatory

Doub $\begin{array} { r } { \mathbb { N } { \bf a } \mathbb { N } = { \bf s } { \bf q } { \bf r } { \bf t } \left( - 1 . \right) ; } \end{array}$

which may, however, throw an immediate exception (see below) and thus not work for this purpose. But, one way or another, you can generally figure out how to get a NaN constant into your environment.

Testing also requires a bit of (one-time) experimentation: According to the IEEE standard, $\mathrm { N a N }$ is guaranteed to be the only value that is not equal to itself!

So, the “approved” method of testing whether Doub value x has been set to NaN is

$$
\mathrm { i } \textbf { f } \left( \textbf { x } : = \textbf { x } \right) ~ \{ \dots , \}
$$

(or test for equality to determine that it’s not a NaN). Unfortunately, at time of writing, some otherwise perfectly good compilers don’t do this right. Instead, they provide a macro isnan() that returns true if the argument is NaN, otherwise false. (Check carefully whether the required #include is math.h or float.h — it varies.)

What, then, is the curse of NaN? It is that some compilers, notably Microsoft, have poorly thought-out default behaviors in distinguishing quiet NaNs from signalling NaNs. Both kinds of NaNs are defined in the IEEE floating-point standard. Quiet NaNs are supposed to be for uses like those above: You can set them, test them, and propagate them by assignment, or even through other floating operations. In such uses they are not supposed to signal an exception that causes your program to abort. Signalling NaNs, on the other hand, are, as the name implies, supposed to signal exceptions. Signalling NaNs should be generated by invalid operations, such as the square root or logarithm of a negative number, or pow(0.,0.).

If all NaNs are treated as signalling exceptions, then you can’t make use of them as we have suggested above. That’s annoying, but OK. On the other hand, if all NaNs are treated as quiet (the Microsoft default at time of writing), then you will run long calculations only to find that all the results are NaN — and you have no way of locating the invalid operation that triggered the propagating cascade of (quiet) NaNs. That’s not OK. It makes debugging a nightmare. (You can get the same disease if other floating-point exceptions propagate, for example overflow or division-by-zero.)

Tricks for specific compilers are not within our normal scope. But this one is so essential that we make it an “exception”: If you are living on planet Microsoft, then the lines of code,

int cw $=$ _controlfp(0,0);   
cw $\& = \widetilde $ (EM_INVALID | EM_OVERFLOW | EM_ZERODIVIDE );   
_controlfp(cw,MCW_EM);

at the beginning of your program will turn NaNs from invalid operations, overflows, and divides-by-zero into signalling NaNs, and leave all the other NaNs quiet. There is a compiler switch, _TURNONFPES_ in nr3.h that will do this for you automatically. (Further options are EM_UNDERFLOW, EM_INEXACT, and EM_DENORMAL, but we think these are best left quiet.)

# 1.5.5 Miscellany

- Bounds checking in vectors and matrices, that is, verifying that subscripts are in range, is expensive. It can easily double or triple the access time to subscripted elements. In their default configuration, the NRvector and NRmatrix classes never do bounds checking. However, $\mathtt { n r 3 . h }$ has a compiler switch, _CHECKBOUNDS_, that turns bounds checking on. This is implemented by preprocessor directives for conditional compilation so there is no performance penalty when you leave it turned off. This is ugly, but effective.

The vector $< >$ class in the $\mathrm { C } { + } { + }$ Standard Library takes a different tack. If you access a vector element by the syntax $\tau \left[ \dot { \bf 1 } \right]$ , there is no bounds checking. If you instead use the at() method, as v.at(i), then bounds checking is performed. The obvious weakness of this approach is that you can’t easily change a lengthy program from one method to the other, as you might want to

do when debugging.

- The importance to performance of avoiding unnecessary copying of large objects, such as vectors and matrices, cannot be overemphasized. As already mentioned, they should always be passed by reference in function arguments. But you also need to be careful about, or avoid completely, the use of functions whose return type is a large object. This is true even if the return type is a reference (which is a tricky business anyway). Our experience is that compilers often create temporary objects, using the copy constructor, when the need to do so is obscure or nonexistent. That is why we so frequently write void functions that have an argument of type (e.g.) MatDoub_O for returning the “answer.” (When we do use vector or matrix return types, our excuse is either that the code is pedagogical, or that the overhead is negligible compared to some big calculation that has just been done.)

You can check up on your compiler by instrumenting the vector and matrix classes: Add a static integer variable to the class definition, increment it within the copy constructor and assignment operator, and look at its value before and after operations that (you think) should not require any copies. You might be surprised.

- There are only two routines in Numerical Recipes that use three-dimensional arrays, rlft3 in $\ S 1 2 . 6$ , and solvde in $\ S 1 8 . 3$ . The file nr3.h includes a rudimentary class for three-dimensional arrays, mainly to service these two routines. In many applications, a better way to proceed is to declare a vector of matrices, for example,

vector<MatDoub> threedee(17);   
for (Int i=0;i<17;i++) threedee[i].resize(19,21);

which creates, in effect, a three-dimensional array of size $1 7 \times 1 9 \times 2 1$ . You can address individual components as threedee[i][j][k].

- “Why no namespace?” Industrial-strength programmers will notice that, unlike the second edition, this third edition of Numerical Recipes does not shield its function and class names by a NR:: namespace. Therefore, if you are so bold as to #include every single file in the book, you are dumping on the order of 500 names into the global namespace, definitely a bad idea!

The explanation, quite simply, is that the vast majority of our users are not industrial-strength programmers, and most found the NR:: namespace annoying and confusing. As we emphasized, strongly, in $\ S 1 . 0 . 1$ , NR is not a program library. If you want to create your own personal namespace for NR, please go ahead.

- In the distant past, Numerical Recipes included provisions for unit- or onebased, instead of zero-based, array indices. The last such version was published in 1992. Zero-based arrays have become so universally accepted that we no longer support any other option.

# CITED REFERENCES AND FURTHER READING:

Numerical Recipes Software 2007, “Using Other Vector and Matrix Libraries,” Numerical Recipes Webnote No. 1,at http://www.nr.com/webnotes?1 [1]

# Solution of Linear Algebraic Equations

# 2.0 Introduction

The most basic task in linear algebra, and perhaps in all of scientific computing, is to solve for the unknowns in a set of linear algebraic equations. In general, a set of linear algebraic equations looks like this:

$$
\begin{array} { c } { { a _ { 0 0 } x _ { 0 } + a _ { 0 1 } x _ { 1 } + a _ { 0 2 } x _ { 2 } + \dots + a _ { 0 , N - 1 } x _ { N - 1 } = b _ { 0 } } } \\ { { \ } } \\ { { a _ { 1 0 } x _ { 0 } + a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \dots + a _ { 1 , N - 1 } x _ { N - 1 } = b _ { 1 } } } \\ { { \ } } \\ { { a _ { 2 0 } x _ { 0 } + a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \dots + a _ { 2 , N - 1 } x _ { N - 1 } = b _ { 2 } } } \\ { { \ } } \\ { { \dots } } \\ { { \ } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \end{array}
$$

Here the $N$ unknowns $x _ { j }$ , $j = 0 , 1 , \dotsc , N - 1$ are related by $M$ equations. The coefficients $a _ { i j }$ with $i \ = \ 0 , 1 , \ldots , M - 1$ and $j ~ = ~ 0 , 1 , \ldots , N - 1$ are known numbers, as are the right-hand side quantities $b _ { i }$ , $i = 0 , 1 , \ldots , M - 1$ .

If $N = M$ , then there are as many equations as unknowns, and there is a good chance of solving for a unique solution set of $x _ { j }$ ’s. Otherwise, if $N \neq M$ , things are even more interesting; we’ll have more to say about this below.

If we write the coefficients $a _ { i j }$ as a matrix, and the right-hand sides $b _ { i }$ as a column vector,

$$
\mathbf { A } = \left[ \begin{array} { c c c c } { a _ { 0 0 } } & { a _ { 0 1 } } & { \ldots } & { a _ { 0 , N - 1 } } \\ { a _ { 1 0 } } & { a _ { 1 1 } } & { \ldots } & { a _ { 1 , N - 1 } } \\ { \ldots } & { \ldots } & { } & { } \\ { a _ { M - 1 , 0 } } & { a _ { M - 1 , 1 } } & { \ldots } & { a _ { M - 1 , N - 1 } } \end{array} \right] \qquad \mathbf { b } = \left[ \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \ldots } \\ { b _ { M - 1 } } \end{array} \right]
$$

then equation (2.0.1) can be written in matrix form as

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

Here, and throughout the book, we use a raised dot to denote matrix multiplication, or the multiplication of a matrix and a vector, or the dot product of two vectors.

This usage is nonstandard, but we think it adds clarity: the dot is, in all of these cases, a contraction operator that represents the sum over a pair of indices, for example

$$
\begin{array} { l c l } { { { \bf C } = { \bf A \cdot B } } } & { { \displaystyle \Longleftrightarrow } } & { { \displaystyle c _ { i k } = \sum _ { j } a _ { i j } b _ { j k } } } \\ { { } } & { { } } & { { } } \\ { { { \bf b } = { \bf A \cdot x } } } & { { \displaystyle \Longleftrightarrow } } & { { \begin{array} { r } { { b _ { i } = \displaystyle \sum _ { j } a _ { i j } x _ { j } } } \\ { { } } \end{array} } } \\ { { \bf d = x \cdot A } } & { { \displaystyle \Longleftrightarrow } } & { { \begin{array} { r } { { d _ { j } = \displaystyle \sum _ { i } x _ { i } a _ { i j } } } \\ { { } } \end{array} } } \\ { { \boldsymbol { q } = { \bf x \cdot y } } } & { { \displaystyle \Longleftrightarrow } } & { { \boldsymbol { q } = \displaystyle \sum _ { i } x _ { i } y _ { i } } } \end{array}
$$

In matrices, by convention, the first index on an element $a _ { i j }$ denotes its row and the second index its column. For most purposes you don’t need to know how a matrix is stored in a computer’s physical memory; you just reference matrix elements by their two-dimensional addresses, e.g., $a _ { 3 4 } = \mathtt { a } [ 3 ]$ [4]. This $\mathrm { C } { + + }$ notation can in fact hide a variety of subtle and versatile physical storage schemes, see $\ S 1 . 4$ and $\ S 1 . 5$ .

# 2.0.1 Nonsingular versus Singular Sets of Equations

You might be wondering why, above, and for the case $M = N$ , we credited only a “good” chance of solving for the unknowns. Analytically, there can fail to be a solution (or a unique solution) if one or more of the $M$ equations is a linear combination of the others, a condition called row degeneracy, or if all equations contain certain variables only in exactly the same linear combination, called column degeneracy. It turns out that, for square matrices, row degeneracy implies column degeneracy, and vice versa. A set of equations that is degenerate is called singular. We will consider singular matrices in some detail in $\ S 2 . 6$ .

Numerically, at least two additional things prevent us from getting a good solution:

- While not exact linear combinations of each other, some of the equations may be so close to linearly dependent that roundoff errors in the machine render them linearly dependent at some stage in the solution process. In this case your numerical procedure will fail, and it can tell you that it has failed. Accumulated roundoff errors in the solution process can swamp the true solution. This problem particularly emerges if $N$ is too large. The numerical procedure does not fail algorithmically. However, it returns a set of $x$ ’s that are wrong, as can be discovered by direct substitution back into the original equations. The closer a set of equations is to being singular, the more likely this is to happen, since increasingly close cancellations will occur during the solution. In fact, the preceding item can be viewed as the special case in which the loss of significance is unfortunately total.

Much of the sophistication of well-written “linear equation-solving packages” is devoted to the detection and/or correction of these two pathologies. It is difficult to give any firm guidelines for when such sophistication is needed, since there is no such thing as a “typical” linear problem. But here is a rough idea: Linear sets with $N$ no larger than 20 or 50 are routine if they are not close to singular; they rarely require more than the most straightforward methods, even in only single (that is, float) precision. With double precision, this number can readily be extended to $N$ as large as perhaps 1000, after which point the limiting factor anyway soon becomes machine time, not accuracy.

Even larger linear sets, $N$ in the thousands or millions, can be solved when the coefficients are sparse (that is, mostly zero), by methods that take advantage of the sparseness. We discuss this further in $\ S 2 . 7$ .

Unfortunately, one seems just as often to encounter linear problems that, by their underlying nature, are close to singular. In this case, you might need to resort to sophisticated methods even for the case of $N = 1 0$ (though rarely for $N = 5$ ). Singular value decomposition (-2.6) is a technique that can sometimes turn singular problems into nonsingular ones, in which case additional sophistication becomes unnecessary.

# 2.0.2 Tasks of Computational Linear Algebra

There is much more to linear algebra than just solving a single set of equations with a single right-hand side. Here, we list the major topics treated in this chapter. (Chapter 11 continues the subject with discussion of eigenvalue/eigenvector problems.)

When $M = N$ :

- Solution of the matrix equation $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ for an unknown vector $\mathbf { X }$ $( \ S 2 . 1 -$ $\ S 2 . 1 0 )$ .   
- Solution of more than one matrix equation $\mathbf { A } \cdot \mathbf { x } _ { j } = \mathbf { b } _ { j }$ , for a set of vectors $\mathbf { X } _ { j }$ , $j = 0 , 1 , \ldots$ , each corresponding to a different, known right-hand side vector $\mathbf { b } _ { j }$ . In this task the key simplification is that the matrix A is held constant, while the right-hand sides, the b’s, are changed $( \ S 2 . 1 - \ S 2 . 1 0 )$ .   
- Calculation of the matrix $\mathbf { A } ^ { - 1 }$ that is the matrix inverse of a square matrix A, i.e., $\mathbf { A } \cdot \mathbf { A } ^ { - 1 } = \mathbf { A } ^ { - 1 } \cdot \mathbf { A } = \mathbf { 1 }$ , where 1 is the identity matrix (all zeros except for ones on the diagonal). This task is equivalent, for an $N \times N$ matrix A, to the previous task with $N$ different $\mathbf { b } _ { j }$ ’s $( j = 0 , 1 , \ldots , N - 1 )$ , namely the unit vectors $( \mathbf { b } _ { j } =$ all zero elements except for 1 in the $j$ th component). The corresponding $\mathbf { X }$ ’s are then the columns of the matrix inverse of A $\ S 2 . 1$ and $\ S 2 . 3 )$ .   
- Calculation of the determinant of a square matrix A (-2.3).

If $M < N$ , or if $M = N$ but the equations are degenerate, then there are effectively fewer equations than unknowns. In this case there can be either no solution, or else more than one solution vector $\mathbf { X }$ . In the latter event, the solution space consists of a particular solution $\mathbf { x } _ { p }$ added to any linear combination of (typically) $N - M$ vectors (which are said to be in the nullspace of the matrix A). The task of finding the solution space of A involves

- Singular value decomposition of a matrix A (-2.6).

If there are more equations than unknowns, $M \ > \ N$ , there is in general no solution vector $\mathbf { X }$ to equation (2.0.1), and the set of equations is said to be overdetermined. It happens frequently, however, that the best “compromise” solution is sought, the one that comes closest to satisfying all equations simultaneously. If closeness is defined in the least-squares sense, i.e., that the sum of the squares of the differences between the left- and right-hand sides of equation (2.0.1) be minimized, then the overdetermined linear problem reduces to a (usually) solvable linear problem, called the

- Linear least-squares problem.

The reduced set of equations to be solved can be written as the $N \times N$ set of equations

$$
( \mathbf { A } ^ { T } \cdot \mathbf { A } ) \cdot \mathbf { x } = ( \mathbf { A } ^ { T } \cdot \mathbf { b } )
$$

where $\mathbf { A } ^ { T }$ denotes the transpose of the matrix A. Equations (2.0.5) are called the normal equations of the linear least-squares problem. There is a close connection between singular value decomposition and the linear least-squares problem, and the latter is also discussed in $\ S 2 . 6$ . You should be warned that direct solution of the normal equations (2.0.5) is not generally the best way to find least-squares solutions.

Some other topics in this chapter include

- Iterative improvement of a solution (-2.5)   
- Various special forms: symmetric positive-definite (-2.9), tridiagonal (-2.4), band-diagonal (-2.4), Toeplitz (-2.8), Vandermonde (-2.8), sparse (-2.7)   
- Strassen’s “fast matrix inversion” (-2.11).

# 2.0.3 Software for Linear Algebra

Going beyond what we can include in this book, several good software packages for linear algebra are available, though not always in $\mathrm { C } { + } { + }$ . LAPACK, a successor to the venerable LINPACK, was developed at Argonne National Laboratories and deserves particular mention because it is published, documented, and available for free use. ScaLAPACK is a version available for parallel architectures. Packages available commercially include those in the IMSL and NAG libraries.

Sophisticated packages are designed with very large linear systems in mind. They therefore go to great effort to minimize not only the number of operations, but also the required storage. Routines for the various tasks are usually provided in several versions, corresponding to several possible simplifications in the form of the input coefficient matrix: symmetric, triangular, banded, positive-definite, etc. If you have a large matrix in one of these forms, you should certainly take advantage of the increased efficiency provided by these different routines, and not just use the form provided for general matrices.

There is also a great watershed dividing routines that are direct (i.e., execute in a predictable number of operations) from routines that are iterative (i.e., attempt to converge to the desired answer in however many steps are necessary). Iterative methods become preferable when the battle against loss of significance is in danger of being lost, either due to large $N$ or because the problem is close to singular. We will treat iterative methods only incompletely in this book, in $\ S 2 . 7$ and in Chapters 19 and 20. These methods are important but mostly beyond our scope. We will, however, discuss in detail a technique that is on the borderline between direct and iterative methods, namely the iterative improvement of a solution that has been obtained by direct methods (-2.5).

# CITED REFERENCES AND FURTHER READING:

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press).

Gill, P.E., Murray, W., and Wright, M.H. 1991, Numerical Linear Algebra and Optimization, vol. 1 (Redwood City, CA: Addison-Wesley).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 4.   
Ueberhuber, C.W. 1997, Numerical Computation: Methods, Software, and Analysis, 2 vols. (Berlin: Springer), Chapter 13.   
Coleman, T.F., and Van Loan, C. 1988, Handbook for Matrix Computations (Philadelphia: S.I.A.M.).   
Forsythe, G.E., and Moler, C.B. 1967, Computer Solution of Linear Algebraic Systems (Englewood Cliffs, NJ: Prentice-Hall).   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), Chapter 2.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), Chapter 9.

# 2.1 Gauss-Jordan Elimination

Gauss-Jordan elimination is probably the way you learned to solve linear equations in high school. (You may have learned it as “Gaussian elimination,” but, strictly speaking, that term refers to the somewhat different technique discussed in $\ S 2 . 2 .$ ) The basic idea is to add or subtract linear combinations of the given equations until each equation contains only one of the unknowns, thus giving an immediate solution. You might also have learned to use the same technique for calculating the inverse of a matrix.

For solving sets of linear equations, Gauss-Jordan elimination produces both the solution of the equations for one or more right-hand side vectors b, and also the matrix inverse $\mathbf { A } ^ { - 1 }$ . However, its principal deficiencies are (i) that it requires all the right-hand sides to be stored and manipulated at the same time, and (ii) that when the inverse matrix is not desired, Gauss-Jordan is three times slower than the best alternative technique for solving a single linear set (-2.3). The method’s principal strength is that it is as stable as any other direct method, perhaps even a bit more stable when full pivoting is used (see $\ S 2 . 1 . 2 )$ .

For inverting a matrix, Gauss-Jordan elimination is about as efficient as any other direct method. We know of no reason not to use it in this application if you are sure that the matrix inverse is what you really want.

You might wonder about deficiency (i) above: If we are getting the matrix inverse anyway, can’t we later let it multiply a new right-hand side to get an additional solution? This does work, but it gives an answer that is very susceptible to roundoff error and not nearly as good as if the new vector had been included with the set of right-hand side vectors in the first instance.

Thus, Gauss-Jordan elimination should not be your method of first choice for solving linear equations. The decomposition methods in $\ S 2 . 3$ are better. Why do we discuss Gauss-Jordan at all? Because it is straightforward, solid as a rock, and a good place for us to introduce the important concept of pivoting which will also be important for the methods described later. The actual sequence of operations performed in Gauss-Jordan elimination is very closely related to that performed by the routines in the next two sections.

# 2.1.1 Elimination on Column-Augmented Matrices

For clarity, and to avoid writing endless ellipses $( \cdots )$ we will write out equations only for the case of four equations and four unknowns, and with three different righthand side vectors that are known in advance. You can write bigger matrices and extend the equations to the case of $N \times N$ matrices, with $M$ sets of right-hand side vectors, in completely analogous fashion. The routine implemented below in $\ S 2 . 1 . 2$ is, of course, general.

Consider the linear matrix equation

$$
\begin{array} { r } { [ \begin{array} { c c c c } { a _ { 0 0 } } & { a _ { 0 1 } } & { a _ { 0 2 } } & { a _ { 0 3 } } \\ { a _ { 1 0 } } & { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 0 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 0 } } & { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} ] \cdot [ \begin{array} { c } { ( \begin{array} { c } { x _ { 0 0 } } \\ { x _ { 1 0 } } \\ { x _ { 2 1 } } \\ { x _ { 3 0 } } \end{array} ) _ { \perp } } \\ { ( \begin{array} { c } { x _ { 2 1 } } \\ { x _ { 3 1 } } \\ { x _ { 3 2 } } \end{array} ) _ { \perp } } \end{array} ( \begin{array} { c } { x _ { 0 1 } } \\ { x _ { 1 1 } } \\ { x _ { 2 2 } } \\ { x _ { 3 1 } } \\ { x _ { 3 2 } } \end{array} ) _ { \perp } ( \begin{array} { c } { y _ { 0 0 } } \\ { y _ { 1 0 } } \\ { y _ { 2 2 } } \\ { y _ { 3 0 } } \end{array} ) _ { \perp } ( \begin{array} { c c c c } { y _ { 0 1 } } & { y _ { 0 1 } } & { y _ { 0 2 } } & { y _ { 0 3 } } \\ { y _ { 1 1 } } & { y _ { 1 1 } } & { y _ { 1 2 } } & { y _ { 1 3 } } \\ { y _ { 2 0 } } & { y _ { 2 1 } } & { y _ { 2 2 } } & { y _ { 2 3 } } \\ { y _ { 3 0 } } & { y _ { 3 1 } } & { y _ { 3 2 } } & { y _ { 3 3 } } \end{array} ) ] } \\  = [ ( \begin{array} { c }  ( \begin{array} { c } { b _ { 0 0 } } \\ { b _ { 1 0 } } \\ { b _ { 1 0 } } \\ { b _ { 2 0 } } \\ { b _ { 3 0 } } \end{array} ) _ { \perp } ( \begin{array} { c } { b _ { 0 1 } } \\ { b _ { 1 1 } } \\ { b _ { 2 1 } } \\ { b _ { 3 1 } } \end{array} ) _ { \perp } ( \begin{array} { c } { b _ { 0 2 } } \\ { b _ { 1 2 } } \\  \end{array} \end{array} \end{array}
$$

Here the raised dot (	) signifies matrix multiplication, while the operator $\sqcup$ just signifies column augmentation, that is, removing the abutting parentheses and making a wider matrix out of the operands of the $\sqcup$ operator.

It should not take you long to write out equation (2.1.1) and to see that it simply states that $x _ { i j }$ is the $i$ th component $( i = 0 , 1 , 2 , 3 )$ ) of the vector solution of the $j$ th right-hand side $( j = 0 , 1 , 2 )$ , the one whose coefficients are $b _ { i j } , i = 0 , 1 , 2 , 3$ ; and that the matrix of unknown coefficients $y _ { i j }$ is the inverse matrix of $a _ { i j }$ . In other words, the matrix solution of

$$
[ \mathbf { A } ] \cdot [ \mathbf { x _ { 0 } } \sqcup \mathbf { x _ { 1 } } \sqcup \mathbf { x } _ { 2 } \sqcup \mathbf { Y } ] = [ \mathbf { b } _ { 0 } \sqcup \mathbf { b } _ { 1 } \sqcup \mathbf { b } _ { 2 } \sqcup \mathbf { 1 } ]
$$

where $\mathbf { A }$ and $\mathbf { Y }$ are square matrices, the $\mathbf { b } _ { i }$ ’s and $\mathbf { X } _ { i }$ ’s are column vectors, and 1 is the identity matrix, simultaneously solves the linear sets

$$
\mathbf { A } \cdot \mathbf { x } _ { 0 } = \mathbf { b } _ { 0 } \qquad \mathbf { A } \cdot \mathbf { x } _ { 1 } = \mathbf { b } _ { 1 } \qquad \mathbf { A } \cdot \mathbf { x } _ { 2 } = \mathbf { b } _ { 2 }
$$

and

$$
\mathbf { A \cdot Y } = \mathbf { 1 }
$$

Now it is also elementary to verify the following facts about (2.1.1):

- Interchanging any two rows of A and the corresponding rows of the $\mathbf { b }$ ’s and of 1 does not change (or scramble in any way) the solution $\mathbf { X }$ ’s and Y . Rather, it just corresponds to writing the same set of linear equations in a different order. Likewise, the solution set is unchanged and in no way scrambled if we replace any row in A by a linear combination of itself and any other row, as long as we do the same linear combination of the rows of the $\mathbf { b }$ ’s and 1 (which then is no longer the identity matrix, of course).

- Interchanging any two columns of A gives the same solution set only if we simultaneously interchange corresponding rows of the $\mathbf { X }$ ’s and of Y . In other words, this interchange scrambles the order of the rows in the solution. If we do this, we will need to unscramble the solution by restoring the rows to their original order.

Gauss-Jordan elimination uses one or more of the above operations to reduce the matrix A to the identity matrix. When this is accomplished, the right-hand side becomes the solution set, as one sees instantly from (2.1.2).

# 2.1.2 Pivoting

In “Gauss-Jordan elimination with no pivoting,” only the second operation in the above list is used. The zeroth row is divided by the element $a _ { 0 0 }$ (this being a trivial linear combination of the zeroth row with any other row — zero coefficient for the other row). Then the right amount of the zeroth row is subtracted from each other row to make all the remaining $a _ { i 0 }$ ’s zero. The zeroth column of A now agrees with the identity matrix. We move to column 1 and divide row 1 by $a _ { 1 1 }$ , then subtract the right amount of row 1 from rows 0, 2, and 3, so as to make their entries in column 1 zero. Column 1 is now reduced to the identity form. And so on for columns 2 and 3. As we do these operations to A, we of course also do the corresponding operations to the b’s and to 1 (which by now no longer resembles the identity matrix in any way!).

Obviously we will run into trouble if we ever encounter a zero element on the (then current) diagonal when we are going to divide by the diagonal element. (The element that we divide by, incidentally, is called the pivot element or pivot.) Not so obvious, but true, is the fact that Gauss-Jordan elimination with no pivoting (no use of the first or third procedures in the above list) is numerically unstable in the presence of any roundoff error, even when a zero pivot is not encountered. You must never do Gauss-Jordan elimination (or Gaussian elimination; see below) without pivoting!

So what is this magic pivoting? Nothing more than interchanging rows (partial pivoting) or rows and columns (full pivoting), so as to put a particularly desirable element in the diagonal position from which the pivot is about to be selected. Since we don’t want to mess up the part of the identity matrix that we have already built up, we can choose among elements that are both (i) on rows below (or on) the one that is about to be normalized, and also (ii) on columns to the right (or on) the column we are about to eliminate. Partial pivoting is easier than full pivoting, because we don’t have to keep track of the permutation of the solution vector. Partial pivoting makes available as pivots only the elements already in the correct column. It turns out that partial pivoting is “almost” as good as full pivoting, in a sense that can be made mathematically precise, but which need not concern us here (for discussion and references, see [1]). To show you both variants, we do full pivoting in the routine in this section and partial pivoting in $\ S 2 . 3$ .

We have to state how to recognize a particularly desirable pivot when we see one. The answer to this is not completely known theoretically. It is known, both theoretically and in practice, that simply picking the largest (in magnitude) available element as the pivot is a very good choice. A curiosity of this procedure, however, is that the choice of pivot will depend on the original scaling of the equations. If we take the third linear equation in our original set and multiply it by a factor of a million, it is almost guaranteed that it will contribute the first pivot; yet the underlying solution of the equations is not changed by this multiplication! One therefore sometimes sees routines which choose as pivot that element which would have been largest if the original equations had all been scaled to have their largest coefficient normalized to unity. This is called implicit pivoting. There is some extra bookkeeping to keep track of the scale factors by which the rows would have been multiplied. (The routines in $\ S 2 . 3$ include implicit pivoting, but the routine in this section does not.)

Finally, let us consider the storage requirements of the method. With a little reflection you will see that at every stage of the algorithm, either an element of A is predictably a one or zero (if it is already in a part of the matrix that has been reduced to identity form) or else the exactly corresponding element of the matrix that started as 1 is predictably a one or zero (if its mate in A has not been reduced to the identity form). Therefore the matrix 1 does not have to exist as separate storage: The matrix inverse of A is gradually built up in A as the original A is destroyed. Likewise, the solution vectors x can gradually replace the right-hand side vectors $\mathbf { b }$ and share the same storage, since after each column in A is reduced, the corresponding row entry in the b’s is never again used.

Here is a routine that does Gauss-Jordan elimination with full pivoting, replacing its input matrices by the desired answers. Immediately following is an overloaded version for use when there are no right-hand sides, i.e., when you want only the matrix inverse.

# void gaussj(MatDoub_IO &a, MatDoub_IO &b)

Linear equation solution by Gauss-Jordan elimination, equation (2.1.1) above. The input matrix is a[0..n-1][0..n-1]. b[0..n-1][0..m-1] is input containing the m right-hand side vectors. On output, a is replaced by its matrix inverse, and b is replaced by the corresponding set of solution vectors.

Int i,icol,irow,j,k,l,ll, $\mathrm { n } = \mathrm { a }$ .nrows(),m=b.ncols();   
Doub big,dum,pivinv;   
VecInt indxc(n),indxr(n),ipiv(n); These integer arrays are used for bookkeeping on   
for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) ipiv[j] ${ = } 0$ ; the pivoting.   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) { This is the main loop over the columns to be big=0.0; reduced. for (j=0;j<n;j++) This is the outer loop of the search for a pivot if (ipiv[j] $\ ! = ~ 1 \cdot$ ) element. for (k=0;k<n;k++) { if (ipiv[k] $\scriptstyle = = 0 .$ ) { if (abs(a[j][k]) $> =$ big) { big=abs(a[j][k]); irow=j; icol=k; } } }

# $^ { + + }$ (ipiv[icol]);

We now have the pivot element, so we interchange rows, if needed, to put the pivot element on the diagonal. The columns are not physically interchanged, only relabeled: indxc[i], the column of the $( \mathrm { i } + 1 ) \mathrm { t h }$ pivot element, is the $( \mathrm { i } + 1 ) \mathrm { t h }$ column that is reduced, while indxr[i] is the row in which that pivot element was originally located. If indxr[i] $\neq$ indxc[i], there is an implied column interchange. With this form of bookkeeping, the solution b’s will end up in the correct order, and the inverse matrix will be scrambled by columns.

if (irow $! =$ icol) { for $\scriptstyle 1 = 0$ ;l<n; $\beth + +$ ) SWAP(a[irow][l],a[icol][l]); for $\scriptstyle \mathbf { 1 } = 0$ ;l<m;l++) SWAP(b[irow][l],b[icol][l]);   
}   
indxr[i] $=$ irow; We are now ready to divide the pivot row by the pivot element, located at irow and icol.   
indxc[i] $=$ icol;   
if (a[icol][icol] $\mathrm { = = } \ 0 . 0$ ) throw("gaussj: Singular Matrix");   
pivinv $= 1$ .0/a[icol][icol];   
a[icol][icol] $^ { = 1 }$ .0;   
for ( $\scriptstyle 1 = 0$ ;l<n; $\beth + +$ ) a[icol][l] $\ast =$ pivinv;   
for ( $\scriptstyle 1 = 0$ ;l<m;l++) b[icol][l] $\ast =$ pivinv;   
for ( $\mathtt { 1 1 } mathtt { = 0 }$ ;ll<n;ll++) Next, we reduce the rows... if (ll ! $! =$ icol) { ...except for the pivot one, of course. dum $_ { 1 } = \mathtt { a }$ [ll][icol]; a[ll][icol] ${ = } 0$ .0; for ( $\scriptstyle 1 = 0$ ;l<n; $^ { 1 + + }$ ) a[ll][l] $- =$ a[icol][l]\*dum; for ( $\scriptstyle 1 = 0$ ;l<m; $^ { 1 + + }$ ) b[ll][l] $- =$ b[icol][l]\*dum; }

This is the end of the main loop over columns of the reduction. It only remains to unscramble the solution in view of the column interchanges. We do this by interchanging pairs of columns in the reverse order that the permutation was built up.

for (l=n-1;l>=0;l--) { if (indxr[l] $! =$ indxc[l]) for ( $\scriptstyle 1 = 0$ ;k<n;k++) SWAP(a[k][indxr[l]],a[k][indxc[l]]);   
} And we are done.

# }

void gaussj(MatDoub_IO &a)   
Overloaded version with no right-hand sides. Replaces a by its inverse.   
{ MatDoub b(a.nrows(),0); Dummy vector with zero columns. gaussj(a,b);   
}

# 2.1.3 Row versus Column Elimination Strategies

The above discussion can be amplified by a modest amount of formalism. Row operations on a matrix A correspond to pre- (that is, left-) multiplication by some simple matrix $\mathbf { R }$ . For example, the matrix $\mathbf { R }$ with components

$$
R _ { i j } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } i = j { \mathrm { ~ a n d ~ } } i \neq 2 , 4 } \\ { 1 } & { { \mathrm { i f ~ } } i = 2 , j = 4 } \\ { 1 } & { { \mathrm { i f ~ } } i = 4 , j = 2 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

effects the interchange of rows 2 and 4. Gauss-Jordan elimination by row operations alone (including the possibility of partial pivoting) consists of a series of such left-multiplications, yielding successively

$$
\begin{array} { c } { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ { \left( \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { A } \right) \cdot \mathbf { x } = \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { b } } \\ { \left( \mathbf { 1 } \right) \cdot \mathbf { x } = \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { b } } \\ { \mathbf { x } = \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { b } } \end{array}
$$

The key point is that since the $\mathbf { R }$ ’s build from right to left, the right-hand side is simply transformed at each stage from one vector to another.

Column operations, on the other hand, correspond to post-, or right-, multiplications by simple matrices, call them C. The matrix in equation (2.1.5), if right-multiplied onto a matrix A, will interchange columns 2 and 4 of A. Elimination by column operations involves (conceptually) inserting a column operator, and also its inverse, between the matrix A and the

unknown vector $\mathbf { X }$ :

$$
\begin{array} { r l r } & { } & { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { ( \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } \cdot \mathbf { C } _ { 2 } \cdot \dots ) \cdots \mathbf { C } _ { 2 } ^ { - 1 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { ( \mathbf { 1 } \cdot \mathbf { \dots } \mathbf { C } _ { 2 } ^ { - 1 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \end{array}
$$

which (peeling off the $\mathbf { C } ^ { - 1 }$ ’s one at a time) implies a solution

$$
\mathbf { x } = \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } \cdot \mathbf { C } _ { 2 } \cdot \cdot \cdot \mathbf { b }
$$

Notice the essential difference between equation (2.1.8) and equation (2.1.6). In the latter case, the $\mathbf { C }$ ’s must be applied to $\mathbf { b }$ in the reverse order from that in which they become known. That is, they must all be stored along the way. This requirement greatly reduces the usefulness of column operations, generally restricting them to simple permutations, for example in support of full pivoting.

# CITED REFERENCES AND FURTHER READING:

Wilkinson, J.H. 1965, The Algebraic Eigenvalue Problem (New York: Oxford University Press).[1]   
Carnahan, B., Luther, H.A., and Wilkes, J.O. 1969, Applied Numerical Methods (New York: Wiley), Example 5.2, p. 282.   
Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hill),p. 247.   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 9 . 3 – 1$ .

# 2.2 Gaussian Elimination with Backsubstitution

Any discussion of Gaussian elimination with backsubstitution is primarily pedagogical. The method stands between full elimination schemes such as Gauss-Jordan, and triangular decomposition schemes such as will be discussed in the next section. Gaussian elimination reduces a matrix not all the way to the identity matrix, but only halfway, to a matrix whose components on the diagonal and above (say) remain nontrivial. Let us now see what advantages accrue.

Suppose that in doing Gauss-Jordan elimination, as described in $\ S 2 . 1$ , we at each stage subtract away rows only below the then-current pivot element. When $a _ { 1 1 }$ is the pivot element, for example, we divide the row 1 by its value (as before), but now use the pivot row to zero only $a _ { 2 1 }$ and $a _ { 3 1 }$ , not $a _ { 0 1 }$ (see equation 2.1.1). Suppose, also, that we do only partial pivoting, never interchanging columns, so that the order of the unknowns never needs to be modified.