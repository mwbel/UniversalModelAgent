<!-- source: Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-library.sk, 1lib.sk, z-lib.sk).pdf -->

<!-- pdf_type: normal; pages: 359; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
Approximation Theory and Approximation Practice, Extended Edition is a textbook on classical polynomial and rational approximation theory for the twenty-first century. It is aimed at advanced undergraduates and graduate students across all of applied mathematics.

Nick Trefethen is Professor of Numerical Analysis at the University of Oxford and a Fellow of the Royal Society. During 2011–2012 he served as President of SIAM.

# siam.

Society for Industrial and Applied Mathematics 3600 Market Street, 6th Floor Philadelphia, PA 19104-2688 USA +1-215-382-9800 • Fax +1-215-386-7999 siam@siam.org • www.siam.org

# Approximation Theory and Approximation Practice

Extended Edition

# Approximation Theory and Approximation Practice

Extended Edition

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/65cf6e039127b1292ea5f9f3316614b432012f1f74abc2a4709d1428c4bc4e13.jpg)

The cover photo shows the Thames River and Port Meadow in Oxford, United Kingdom. This scene has been largely unchanged for the past thousand years.

# Approximation Theory and Approximation Practice

Extended Edition

Lloyd N. Trefethen

University of Oxford Oxford, United Kingdom

Society for Industrial and Applied Mathematics Philadelphia

10 9 8 7 6 5 4 3 2 1

All rights reserved. Printed in the United States of America. No part of this book may be reproduced, stored, or transmitted in any manner without the written permission of the publisher. For information, write to the Society for Industrial and Applied Mathematics, 3600 Market Street, 6th Floor, Philadelphia, PA 19104-2688 USA.

MATLAB is a registered trademark of The MathWorks, Inc. For MATLAB product information, please contact The MathWorks, Inc., 3 Apple Hill Drive, Natick, MA 01760-2098 USA, 508-647-7000, Fax: 508-647-7001, info@mathworks.com, www.mathworks.com.

Publications Director Executive Editor Developmental Editor Managing Editor Production Editor Copy Editor Production Manager Production Coordinator Graphic Designer

Kivmars H. Bowling Elizabeth Greenspan Mellisa Pascale Kelly Thomas Louis R. Primus Susan Fleshman Donna Witzleben Cally A. Shrader Doug Smock

# Library of Congress Cataloging-in-Publication Data

Names: Trefethen, Lloyd N. (Lloyd Nicholas), author.

Title: Approximation theory and approximation practice / Lloyd N.   
Trefethen.

Description: Extended edition. | Philadelphia $:$ Society for Industrial and Applied Mathematics, [2019] | Includes bibliographical references and index. | Summary: “Including two new appendices, this extended edition of Trefethen’s textbook covers classical polynomial and rational approximation theory for the twenty-rst century”-- Provided by publisher.

Identiers: LCCN 2019027107 (print) | LCCN 2019027108 (ebook) | ISBN 9781611975932 (hardback) | ISBN 9781611975949 (ebook)

Subjects: LCSH: Approximation theory.   
Classication: LCC QA221 .T73 2019 (print) | LCC QA221 (ebook) | DDC 511/.4--dc23   
LC record available at https://lccn.loc.gov/2019027107   
LC ebook record available at https://lccn.loc.gov/2019027108

# Contents

Preface to the Extended Edition ix   
1. Introduction 1   
2. Chebyshev Points and Interpolants 7   
3. Chebyshev Polynomials and Series 13   
4. Interpolants, Projections, and Aliasing 25   
5. Barycentric Interpolation Formula 33   
6. Weierstrass Approximation Theorem 43   
7. Convergence for Differentiable Functions 49   
8. Convergence for Analytic Functions 55   
9. Gibbs Phenomenon 63   
10. Best Approximation 73   
11. Hermite Integral Formula 81   
12. Potential Theory and Approximation 89   
13. Equispaced Points, Runge Phenomenon 95   
14. Discussion of High-Order Interpolation 103   
15. Lebesgue Constants 107   
16. Best and Near-Best 117   
17. Orthogonal Polynomials 123   
18. Polynomial Roots and Colleague Matrices 133   
19. Clenshaw–Curtis and Gauss Quadrature 143   
20. Carath´eodory–Fej´er Approximation 155   
21. Spectral Methods 165   
22. Linear Approximation: Beyond Polynomials 177   
23. Nonlinear Approximation: Why Rational Functions? 189   
24. Rational Best Approximation 199   
25. Two Famous Problems 209   
26. Rational Interpolation and Linearized Least-Squares 221   
27. Pad´e Approximation 235   
28. Analytic Continuation and Convergence Acceleration 251   
Appendix A: Six Myths of Polynomial Interpolation and Quadrature 263   
Appendix B: “ $A T A P$ for Periodic Functions” (SISC 2015) 273   
Appendix C: “ $A T A P$ for the Unit Disk” (SINUM 2014) 297   
References 329   
Index 357

# Preface to the Extended Edition

Approximation Theory and Approximation Practice ( ${ } ^ { 6 } A T A P$ ”), originally published in 2013, concerns approximation of nonperiodic functions on the interval $[ - 1 , 1 ]$ , the Chebyshev setting of constructive analysis. But this is just one of three essentially equivalent situations:

Chebyshev, for nonperiodic functions of $x \in [ - 1 , 1 ]$ , Fourier, for periodic functions of $\theta \in [ - \pi , \pi ]$ , Laurent/Taylor, for functions of $z$ on the unit circle $| z | = 1$ .

As discussed on p. 14, my original plan had been to give equal treatment to all three settings, but it became clear that a book written to that plan would be ponderous. So Chebyshev became the subject, since it was the most important of the three for numerical computation and also the least understood.

In this extended edition, we have found a way to give a kind of summary of the parallel mathematics of the Fourier and Laurent/Taylor cases without changing the main text. We have added appendices reprinting two papers published recently in SIAM journals:

Appendix B. Fourier.   
G. B. Wright, M. Javed, H. Montanelli and L. N. Trefethen (2015), Extension of Chebfun to periodic functions, SIAM J. Sci. Comput. 37, C554–C573.   
Appendix C. Laurent/Taylor.   
A. P. Austin, P. Kravanja and L. N. Trefethen (2014), Numerical algorithms based on analytic function values at roots of unity, SIAM J. Numer. Anal. 52, 1795–1821.

In the first of these papers, readers will see a list of 10 parallels between Fourier and Chebyshev spelled out in Table B.1, followed by a discussion of 10 respects in which the two cases differ. These differences are not deep mathematically (there are no deep mathematical differences between Fourier and Chebyshev!), but they involve conceptual twists. Readers may also enjoy Figure B.9, highlighting the continuity from Runge in 1904 to his descendants in 2015. One may think of Wright et al. as a kind of “ $A T A P$ for periodic functions.” Specifically, it is noted on p. 275 that Section B.2 of the paper corresponds to Chapter 3 of this book, Section B.3 to Chapters 2, 4, and 5, and Section B.4 to Chapters 6, 7, 8, 10, and 19.

In the second paper, a notable feature of the presentation is a sequence of 13 short MATLAB code segments (summarized on pp. 320–321), many just one line long, for interpolation, differentiation, integration, and zero- and polefinding from data values at roots of unity. The links to Chapters 2–5, 18, and 19 of this book are very close. The history of this mathematics is collected in Figure C.1 of the paper, and Figure C.4 shows a striking image related to the Jentzsch, Walsh, and Blatt– Saff theorems discussed here on pp. 140–141. Austin et al. is a kind of “ $A T A P$ for the unit disk.”

Since the first edition of $A T A P$ was published, the use of Chebfun has grown around the world. The code was completely rewritten during 2013–14 by a team led by Nick Hale, and version 5 was released in June 2014. By the combined efforts of Alex Townsend, Behnam Hashemi, Grady Wright, Heather Wilber, and Nicolas Boull´e, Chebfun has been expanded to compute with functions not only on intervals but also on rectangles, boxes, spheres, disks, and balls. Multidimensional approximation is not treated in this book, but it is a hot topic in the era of big data, and these new capabilities of Chebfun make use of low-rank compression ideas that are familiar to today’s engineers and data scientists.

I have taken the opportunity of the new edition to correct a number of errors pointed out by readers and colleagues, of whom I would like in particular to acknowledge Folkmar Bornemann, Behnam Hashemi, Mohsin Javed, Yuji Nakatsukasa, Grady Wright, and Kuan Xu. The corrections have included updates to Chebfun syntax such as the replacement of interp1, chebpolyplot, and chebellipseplot by chebfun.interp1, plotcoeffs, and plotregion, respectively.

Although this is not a thoroughgoing revision of $A T A P$ , about a dozen new references have been added. Let me mention two areas of particularly interesting developments since 2013. One is Chebyshev spectral discretization of ordinary differential equations, a subject reflected in the new SIAM book Exploring ODEs [Trefethen, Birkisson & Driscoll 2018]. $A T A P$ and Exploring ODEs are siblings, two mathematical textbooks based on Chebfun, and a PDF file of the latter is freely available at http://people.maths.ox.ac.uk/trefethen/ExplODE. Chebfun now makes systematic use of the rectangular spectral discretizations introduced by Driscoll and Hale [2015]; a leader of this effort was Asgeir Birkisson. Details can ´ be found in [Aurentz & Trefethen 2017a] and in Appendix A of Exploring ODEs.

The other area to highlight is rational approximation. As described in the last six chapters of this book, rational approximations are particularly effective for functions that have singularities since they can cluster poles and zeros near them. On the other hand, they are traditionally hard to compute. A few years after this book was published, a flexible new method for computing rational approximations on arbitrary real or complex domains, the AAA algorithm, was introduced by Nakatsukasa, S\`ete, and myself [2018]. The AAA algorithm gets its power from combining a barycentric rational representation with an adaptive choice of support points. Most recently, attempts to extend AAA have led to the introduction of lightning Laplace solvers, which exploit rational functions to solve certain partial differential equations with remarkable speed and accuracy on regions with corners, where solutions almost invariably have singularities [Gopal & Trefethen 2019a,b]. The approximation theory underlying these new methods is built on generalizations for rational functions of the Hermite integral formula and the potential theory presented in Chapters 11–12 for polynomials. Together, these encouraging developments in the numerical use of rational functions suggest, as we like to say (see the references labeled 1885a and 1964), that “Runge” is joining forces with “Newman.”

# Chapter 1. Introduction

Welcome to a beautiful subject!—the constructive approximation of functions. And welcome to a rather unusual book.

Approximation theory is an established field, and my aim is to teach you some of its most important ideas and results, centered on classical topics related to polynomials and rational functions. The style of this book, however, is quite different from what you will find elsewhere. Everything is illustrated computationally with the help of the Chebfun software package in MATLAB, from Chebyshev interpolants to Lebesgue constants, from the Weierstrass approximation theorem to the Remez algorithm. Everything is practical and fast, so we will routinely compute polynomial interpolants or Gauss quadrature weights for tens of thousands of points. In fact, each chapter of this book is a single MATLAB M-file, and the book has been produced by executing these files with the MATLAB “publish” facility. The chapters come from M-files called chap1.m, . . . , chap28.m and you can download them and use them as templates to be modified for explorations of your own.

Beginners are welcome, and so are experts, who will find familiar topics approached from new angles and familiar conclusions turned on their heads. Indeed, the field of approximation theory came of age in an era of polynomials of degree perhaps O(10). Now that O(1000) is easy and O(1,000,000) is not hard, different questions come to the fore. For example, we shall see that “best” approximants are hardly better than “near-best,” though they are much harder to compute, and that, contrary to widespread misconceptions, numerical methods based on highorder polynomials can be extremely efficient and robust.

This is a book about approximation, not Chebfun, and for the most part we shall use Chebfun tools with little explanation. For information about Chebfun, see www.chebfun.org. In the course of the book we shall use Chebfun overloads of the following MATLAB functions, among others:

CONV, CUMSUM, DIFF, INTERP1, NORM, POLY, POLYFIT, ROOTS, SPLINE.

We also use additional Chebfun commands such as

CF, CHEBPADE, CHEBPOLY, CHEBPTS, LEBESGUE, LEGPOLY, LEGPTS, MINIMAX, PADEAPPROX, PLOTREGION, RATINTERP.

There are quite a number of excellent books on approximation theory. Three classics are [Cheney 1966], [Davis 1975], and [Meinardus 1967], and a slightly more recent computationally oriented classic is [Powell 1981]. Perhaps the first approximation theory text was [Borel 1905].

A good deal of my emphasis will be on ideas related to Chebyshev points and polynomials, whose origins go back more than a century to mathematicians including Chebyshev (1821–1894), de la Vall´ee Poussin (1866–1962), Bernstein (1880– 1968), and Jackson (1888–1946). In the computer era, some of the early figures who developed “Chebyshev technology,” in approximately chronological order, were Lanczos, Clenshaw, Babenko, Good, Fox, Elliott, Mason, Orszag, and V. I. Lebedev. Books on Chebyshev polynomials have been published by Snyder [1966], Fox and Parker [1968], Paszkowski [1975], Rivlin [1990], and Mason and Handscomb [2003]. One reason we emphasize Chebyshev technology so much is that in practice, for working with functions on intervals, these methods are unbeatable. For example, we shall see in Chapter 16 that the difference in approximation power between Chebyshev and “optimal” interpolation points is utterly negligible. Another reason is that if you know the Chebyshev material well, this is the best possible foundation for work on other approximation topics and for understanding the links with Fourier analysis.

My style is conversational, but that doesn’t mean the material is all elementary. The book aims to be more readable than most, and the numerical experiments help achieve this. At the same time, theorems are stated and proofs are given, often rather tersely, without all the details spelled out. It is assumed that the reader is comfortable with rigorous mathematical arguments and familiar with ideas like continuous functions on compact sets, Lipschitz continuity, contour integrals in the complex plane, and norms of operators. If you are a student, I hope you are an advanced undergraduate or graduate who has taken courses in numerical analysis and complex analysis. If you are a seasoned mathematician, I hope you are also a MATLAB user.

Each chapter has a collection of exercises, which span a wide range from mathematical theory to Chebfun-based numerical experimentation. Please do not skip the numerical exercises! If you are going to do that, you might as well put this book aside and read one of the classics from the 1960s.

To give readers easy access to all the examples in executable form, the book was produced using publish in LATEX mode: thus this chapter, for example, can be generated with the MATLAB command publish('chap1','latex'). To achieve the desired layout, we begin each chapter by setting a few default parameters concerning line widths for plots, etc., which are collected in an M-file called ATAPformats that is included with the standard distribution of Chebfun. Most readers can ignore these details and simply apply publish to each chapter. For the actual production of the printed book, publish was executed not chapter by chapter but on a concatenation of all the chapters, and quite a few tweaks were made to the resulting

LATEX file, including removal of MATLAB commands whose effects are evident from looking at the figures, like title, axis, hold off, and grid on.

The Lagrange interpolation formula was discovered by Waring, the Gibbs phenomenon was discovered by Wilbraham, and the Hermite integral formula is due to Cauchy. These are just some of the instances of Stigler’s Law in approximation theory, and in writing this book I have taken pleasure in trying to cite the originator of each of the main ideas. Thus the entries in the References stretch back several centuries, and each has an editorial comment attached. Often the original papers are surprisingly readable and insightful, at least if you are comfortable with French or German, and in any case, it seems particularly important to pay heed to original sources in a book like this that aims to reexamine material that has grown too standardized in the textbooks. Another reason for looking at original sources is that in recent years it has become far easier to track them down, thanks to the digitization of journals, though there are always difficult special cases like [Wilbraham 1848], which I finally found in an elegant leather-bound volume in the Balliol College library. No doubt I have missed originators of certain ideas, and I would be glad to be corrected on such points by readers. For a great deal of information about approximation theory, including links to dozens of classic papers, see the History of Approximation Theory website at http://www.math.technion.ac.il/hat/.

Perhaps I may add a further personal comment. As an undergraduate and graduate student in the late 1970s and early 1980s, one of my main interests was approximation theory. I regarded this subject as the foundation of my wider field of numerical analysis, but as the years passed, research in approximation theory came to seem to me dry and academic, and I moved into other areas. Now times have changed, computers have changed, and my perceptions have changed. I now again regard approximation theory as exceedingly close to computing, and in this book we shall discuss many practical numerical problems, including interpolation, quadrature, rootfinding, analytic continuation, extrapolation of sequences and series, and solution of differential equations.

Why is approximation theory useful? The answer goes much further than the rather tired old fact that your computer relies on approximations to evaluate functions like $\sin ( x )$ and $\exp ( x )$ . For my personal answer to the question, concerning polynomials and rational functions in particular, take a look at the last three pages of Chapter 23, beginning with the quotes of Runge and Kirchberger from the beginning of the 20th century. There are also many other fascinating and important topics of approximation theory not touched upon in this volume, including splines, wavelets, radial basis functions, compressed sensing, and multivariate approximations of all kinds.

In summary, here are some distinctive features of this book:

• The emphasis is on topics close to numerical algorithms.

• Everything is illustrated with Chebfun.

• Each chapter is a publishable MATLAB M-file, available online.

• There is a bias toward theorems and methods for analytic functions, which appear so often in applications, rather than on functions at the edge of discontinuity with their seductive theoretical challenges.

• Original sources are cited rather than textbooks, and each item in the bibliography is listed with an editorial comment.

At a more detailed level, virtually every chapter contains mathematical and scholarly novelties. Examples are the use of barycentric formulas beginning in Chapter 5, the tracing of barycentric formulas and the Hermite integral formula back to Jacobi in 1825 and Cauchy in 1826, Theorem 7.1 on the size of Chebyshev coefficients, the introduction to potential theory in Chapter 12, the discussion in Chapter 14 of prevailing misconceptions about interpolation, the presentation of colleague matrices for rootfinding in Chapter 18 with Jacobi matrices for quadrature as a special case in Chapter 19, Theorem 19.5 showing that Clenshaw–Curtis quadrature converges about as fast as Gauss quadrature, the first textbook presentation of Carath´eodory–Fej´er approximation in Chapter 20, the explanation in Chapter 22 of why polynomials are not optimal functions for linear approximation, the extensive discussion in Chapter 23 of the uses of rational approximations, and the SVD-based algorithms for robust rational interpolation and linearized least-squares fitting and Pad´e approximation in Chapters 26 and 27.

All in all, we shall see that there is scarcely an idea in classical approximation theory that cannot be illustrated in a few lines of Chebfun code, and as I first imagined around 1975, anyone who wants to be expert at numerical computation really does need to know this material.

Dozens of people have helped me in preparing this book. I cannot name them all, but I would like to thank in particular Serkan Gugercin, Nick Higham, J¨org Liesen, Ricardo Pach´on, and Ivo Panayotov for reading the whole text and making many useful suggestions, Jean-Paul Berrut for teaching me about rational functions and barycentric formulas, Folkmar Bornemann for bringing to light historical surprises involving Jacobi, Cauchy, and Marcel Riesz, and Volker Mehrmann for hosting a sabbatical visit to the Technical University of Berlin in 2010 during which much of the work was done. I am grateful to Max Jensen of the University of Durham, whose invitation to give a 50-minute talk in March 2009 sparked the whole project, and to Marlis Hochbruck and Caroline Lasser for testing a draft of the book with their students in Karlsruhe and Munich. I have enjoyed decades of collaboration on approximation-related topics with Martin Gutknecht and Andr´e Weideman. Here in the Numerical Analysis Group at Oxford, Endre S¨uli and Andy Wathen have been the finest colleagues one could ask for these past 15 years, and the remarkable Lotti Ekert makes everything run smoothly. At SIAM I have benefited from the enthusiastic and professional design, production, and copy editing assistance of Elizabeth Greenspan, Lou Primus, David Riegelhaupt, and Gina Rinelli. The project of using publish to produce a book was encouraged and supported by Ned Gulley, Cleve Moler, and Matthew Simoneau at MathWorks. Finally, none of this would have been possible without the team who have made Chebfun so powerful and beautiful, my good friends Zachary Battles, Asgeir Birkisson, Toby Driscoll, ´ Pedro Gonnet, Stefan G¨uttel, Nick Hale, Ricardo Pach´on, Rodrigo Platte, Mark Richardson, and Alex Townsend.

Exercise 1.1. Chebfun download. Download Chebfun from www.chebfun.org or https://github.com/chebfun/chebfun and install it in your MATLAB path. Execute chebtest('chebfun') to make sure things are working, and note the time taken. Execute chebtest('chebfun') again, and note how much speedup there is now that various files have been brought into memory. Now read Chapter 1 of the online Chebfun Guide, and look at the collection of examples at www.chebfun.org.

Exercise 1.2. The publish command. Execute help publish and doc publish in MATLAB to learn the basics of how the publish command works. Then download the files chap1.m and chap2.m from http://www.chebfun.org/ATAP and publish them with publish('chap1','latex') followed by appropriate LATEX commands. If you are a student taking a course for which you are expected to turn in writeups of the exercises, I recommend that you make it your habit to produce them with publish.

Exercise 1.3. Textbook $\boldsymbol { x }$ . Buy or borrow a copy of an approximation theory textbook, which we shall call $X$ ; good examples are the books of Achieser, Braess, Cheney, Davis, Lorentz, Meinardus, Natanson, Powell, Rice, Rivlin, Sch¨onhage, Timan, and Watson listed in the References. As you work through Approximation Theory and Approximation Practice, keep $X$ at your side and get in the habit of comparing treatments of each topic between $A T A P$ and $X$ . (a) What are the author, title, and publication date of $X$ ? (b) Where did/does the author work and what were/are his/her dates? (c) Look at the first three theorems in $X$ and write down one of them that interests you. You do not have to write down the proof.

# Chapter 2. Chebyshev Points and Interpolants

Any interval $[ a , b ]$ can be scaled to $[ - 1 , 1 ]$ , so most of the time, we shall just talk about $[ - 1 , 1 ]$ .

Let $n$ be a positive integer:

Consider $n + 1$ equally spaced angles $\{ \theta _ { j } \}$ from $0$ to $\pi$ :

tt = linspace(0,pi,n+1);

We can think of these as the arguments of $n + 1$ points $\{ z _ { j } \}$ on the upper half of the unit circle in the complex plane. These are the $( 2 n ) \mathrm { t h }$ roots of unity lying in the closed upper half-plane:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/a4907fa20ca2c90fb551bb4661e603bf39b0e9c031af17981b2d92ce0445c966.jpg)

The Chebyshev points associated with the parameter $n$ are the real parts of these points,

$$
x _ { j } = \operatorname { R e } z _ { j } = { \frac { 1 } { 2 } } ( z _ { j } + z _ { j } ^ { - 1 } ) , \quad 0 \leq j \leq n ,
$$

xx = real(zz);

Some authors use the terms Chebyshev–Lobatto points, Chebyshev extreme points, or Chebyshev points of the second kind, but as these are the points most often used in practical computation, we shall just say Chebyshev points.

Another way to define the Chebyshev points is in terms of the original angles,

$$
x _ { j } = \cos ( j \pi / n ) , \quad 0 \leq j \leq n ,
$$

xx = cos(tt);

and the problem of polynomial interpolation in these points was considered at least as early as [Jackson 1913]. There is also an equivalent Chebfun command chebpts:

xx = chebpts(n+1);

Actually, this result isn’t exactly equivalent, as the ordering is left-to-right rather than right-to-left. Concerning rounding errors when these numbers are calculated numerically, see Exercise 2.3.

Let us add the Chebyshev points to the plot:

hold on, for ${ \mathfrak { j } } ~ = ~ 2 { : } \mathtt { n }$ , plot( $\left[ \mathbf { x x } \left( \mathbf { n } + 2 - j \right. \right]$ ) zz(j)],'k'), endplot(xx,0\*xx,'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/089a3422b2298919e2a08410d5fb117384299dae94c663faf66b12d4af6c0320.jpg)

They cluster near $^ { 1 }$ and $^ { - 1 }$ , with the average spacing as $n \to \infty$ being given by a density function with square root singularities at both ends (Exercise 2.2).

Let $\{ f _ { j } \}$ , $0 \leq j \leq n$ , be a set of numbers, which may or may not come from sampling a function $f ( x )$ at the Chebyshev points. Then there exists a unique polynomial $p$ of degree $n$ that interpolates these data, i.e., $p ( x _ { j } ) = f _ { j }$ for each $j$ . When we say “of degree $n$ ,” we mean of degree less than or equal to $n$ , and we let $\mathcal { P } _ { n }$ denote the set of all such polynomials:

$$
{ \mathcal { P } } _ { n } = \{ { \mathrm { p o l y n o m i a l s ~ o f ~ d e g r e e ~ a t ~ m o s t ~ } } n \} .
$$

As we trust the reader already knows, the existence and uniqueness of polynomial interpolants apply for any distinct set of interpolation points. In the case of Chebyshev points, we call the polynomial the Chebyshev interpolant.

Polynomial interpolants through equally spaced points have terrible properties, as we shall see in Chapters 11–15. Polynomial interpolants through Chebyshev points, however, are excellent. It is the clustering near the ends of the interval that makes the difference, and other sets of points with similar clustering, like Legendre points (Chapter 17), have similarly good behavior. The explanation of this fact has a lot to do with potential theory, a subject we shall introduce in Chapter 12. Specifically, what makes Chebyshev or Legendre points effective is that each one has approximately the same average distance from the others, as measured in the sense of the geometric mean. On the interval $[ - 1 , 1 ]$ , this average distance is about $1 / 2$ (Exercise 2.6).

Chebfun is built on Chebyshev interpolants [Battles $\&$ Trefethen 2004]. For example, here is a certain step function:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/da9403ad7939323187e0f7e46c26b3b43ca380954178231da4330fd326ed12e2.jpg)

By calling chebfun with a second explicit argument of 6, we can construct the Chebyshev interpolant to $f$ through 6 points, that is, of degree 5:

$_ { \mathrm { ~ p ~ } } =$ chebfun(f,6); hold on, plot(p,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/306ce5cebfd233191ff303f096d666529c76fef06adfceafdcfdd1e946014890.jpg)

Similarly, here is the Chebyshev interpolant of degree 25:

plot(f,'k'), p = chebfun(f,26); hold on, plot(p,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/1f6a7ddf24f12aa216eb5805c2fdf961a36cccf4160adfafb15b347982c2748a.jpg)

Here are a more complicated function and its interpolant of degree 100:

f = sin( $6 * \mathbf { x } .$ ) $^ +$ sign(sin(x+exp(2\*x))); plot(f,'k'), $_ { \mathrm { ~ p ~ } } =$ chebfun(f,101); hold on, plot(p)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/988a66496449bbfc0ad7d7054054c3e5f991576cf4ff4fe747cd807963b78830.jpg)

Another way to use the chebfun command is by giving it an explicit vector of data rather than a function to sample, in which case it interprets the vector as data for a Chebyshev interpolant of the appropriate order. Here, for example, is the interpolant of degree 99 through random data values at 100 Chebyshev points in $[ - 1 , 1 ]$ :

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/ed9a30cce97abab6bb5c7f3e8ca10ac81f79e8aa8d7756b71c6d25fedbc5a71d.jpg)

This experiment illustrates how robust Chebyshev interpolation is. If we had taken a million points instead of 100, the result would not have been much different mathematically, though it would have been harder to plot. We shall return to this figure in Chapter 15.

For illustrations like these it is interesting to pick data with jumps or wiggles, and Chapter 9 discusses such interpolants systematically. In applications where polynomial interpolants are most useful, however, the data will typically be smooth.

Summary of Chapter 2. Polynomial interpolants in equispaced points in $[ - 1 , 1 ]$ have very poor approximation properties, but interpolants in Chebyshev points, which cluster near $\pm 1$ , are excellent.

Exercise 2.1. Chebyshev interpolants through random data. (a) Repeat the experiment of interpolation through random data for 10, 100, 1000, and 10000 points. In each case use minandmax(p) to determine the minimum and maximum values of the interpolant and measure the computer time required for this computation (e.g., using tic and toc). (b) In addition to the four plots over $[ - 1 , 1 ]$ , use xlim([0.9999 1]) to zoom in the 10000-point plot to the interval [0.9999, 1]. How many of the 10000 grid points fall in this interval?

Exercise 2.2. Limiting density as $n \to \infty$ . (a) Suppose $x _ { 0 } , \ldots , x _ { n }$ are $n + 1$ points equally spaced from $^ { - 1 }$ to 1. If $- 1 \leq a < b \leq 1$ , what fraction of the points fall in the interval $[ a , b ]$ in the limit $n \to \infty$ ? Give an exact formula. (b) Give the analogous formula for the case where $x _ { 0 } , \ldots , x _ { n }$ are the Chebyshev points. (c) How does the result of (b) match the number found in [0.9999, 1] in the last exercise for the case $n = 9 9 9 9 9$ ? (d) Show that in the limit $n \to \infty$ , the density of the Chebyshev points near $x \in ( - 1 , 1 )$ approaches $n / ( \pi \sqrt { 1 - x ^ { 2 } } )$ (see (12.10)).

Exercise 2.3. Rounding errors in computing Chebyshev points. On a computer in floating point arithmetic, the formula (2.2) for the Chebyshev points is not so good, because it lacks the expected symmetry. (a) Write a MATLAB program that finds the smallest even value $n \geq 2$ for which, on your computer as computed by this formula, $x _ { n / 2 } \neq 0$ . (You will probably find that $n = 2$ is the first such value.) (b) Find the line in the code chebpts.m where Chebfun computes Chebyshev points. What alternative formula does it use? Explain why this formula achieves perfect symmetry for all $n$ in floating point arithmetic. (c) Show that this formula is mathematically equivalent to (2.2).

Exercise 2.4. Chebyshev points of the first kind. The Chebyshev points of the first kind, also known as Gauss–Chebyshev points, are obtained by taking the real parts of points on the unit circle midway between those we have considered, i.e., $x _ { j } = \cos ( ( j + \textstyle \frac { 1 } { 2 } ) \pi / ( n + 1 ) )$ for integers $0 \leq j \leq n$ . Call help chebpts and help legpts to find out how to generate these points in Chebfun and how to generate Legendre points for comparison (these are roots of Legendre polynomials—see Chapter 17). For $n + 1 = 1 0 0$ , what is the maximum difference between a Chebyshev point of the first kind and the corresponding Legendre point? Draw a plot to illustrate as informatively as you can how close these two sets of points are.

Exercise 2.5. Convergence of Chebyshev interpolants. (a) Use Chebfun to produce a plot on a log scale of $\| f - p _ { n } \|$ as a function of $n$ for $f ( x ) = e ^ { x }$ on $[ - 1 , 1 ]$ , where $p _ { n }$ is the Chebyshev interpolant in $\mathcal { P } _ { n }$ . Take $\| \cdot \|$ to be the supremum norm, which can be computed by $\mathtt { n o r m } ( \mathtt { f } \mathtt { - p } , \mathtt { i n f } )$ . How large must $n$ be for accuracy at the level of machine precision? What happens if $n$ is increased beyond this point? (b) The same questions for $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ . Convergence rates like these will be analyzed in Chapters 7 and 8.

Exercise 2.6. Geometric mean distance between points. Write a code meandistance that takes as input a vector of points $x _ { 0 } , \ldots , x _ { n }$ in $[ - 1 , 1 ]$ and produces a plot with $x _ { j }$ on the horizontal axis and the geometric mean of the distances of $x _ { j }$ to the other points on the vertical axis. (The MATLAB command prod may be useful.) (a)

What are the results for Chebyshev points with $n = 5 , 1 0 , 2 0 !$ (b) The same for Legendre points (see Exercise 2.4). (c) The same for equally spaced points from $x _ { 0 } = - 1$ to $x _ { n } = 1$ . Exercise 2.7. Chebyshev points scaled to the interval $[ a , b ]$ . (a) Use chebpts(10) to print the values of the Chebyshev points in $[ - 1 , 1 ]$ for $n = 9$ . (b) Use chebfun(@sin,10) to compute the degree 9 interpolant $p ( x )$ to $\sin ( x )$ in these points. Make a plot showing $p ( x )$ and $\sin ( x )$ over the larger interval $[ - 6 , 6 ]$ , and also a semilog plot of $| f ( x ) - p ( x ) |$ over that interval. Comment on the results. (c) Now use chebpts(10,[0 6]) to print the values of the Chebyshev points for $n = 9$ scaled to the interval [0, 6]. (d) Use chebfun(@sin, [0 6],10) to compute the degree 9 interpolant to $\sin ( x )$ in these points, and make the same two plots as before over $[ - 6 , 6 ]$ . Comment.

# Chapter 3. Chebyshev Polynomials and Series

Throughout applied mathematics, one encounters three closely analogous canonical settings associated with the names of Fourier, Laurent, and Chebyshev. In fact, if we impose certain symmetries in the Fourier and Laurent cases, the analogies become equivalences. The Chebyshev setting is the one of central interest in this book, concerning a variable $x$ and a function $f$ defined on $[ - 1 , 1 ]$ :

$$
C h e b y s h e v \colon \ x \in [ - 1 , 1 ] , \quad f ( x ) \approx \sum _ { k = 0 } ^ { n } { a _ { k } T _ { k } ( x ) } .
$$

Here $T _ { k }$ is the $k$ th Chebyshev polynomial, which we shall discuss in a moment. For the equivalent Laurent problem, let $z$ be a variable that ranges over the unit circle in the complex plane. Given $f ( x )$ , define a transplanted function $F ( z )$ on the unit circle by the condition $F ( z ) = f ( x )$ , where $x = ( z + z ^ { - 1 } ) / 2$ as in (2.1). Note that this means that there are two values of $z$ for each value of $x$ , and $F$ satisfies the symmetry property $F ( z ) = F ( z ^ { - 1 } )$ . The series now involves a polynomial in both $z$ and $z ^ { - 1 }$ , known as a Laurent polynomial:

$$
L a u r e n t : \quad | z | = 1 , \quad F ( z ) = F ( z ^ { - 1 } ) \approx \frac { 1 } { 2 } \sum _ { k = 0 } ^ { n } a _ { k } ( z ^ { k } + z ^ { - k } ) .
$$

For the equivalent Fourier problem, let $\theta$ be a variable that ranges over $[ - \pi , \pi ]$ , which we regard as a $2 \pi$ -periodic domain. Transplant $f$ and $F$ to a function $\mathcal { F }$ defined on $[ - \pi , \pi ]$ by setting ${ \mathcal { F } } ( \theta ) = F ( e ^ { i \theta } ) = f ( \cos ( \theta ) )$ as in (2.2). Now we have a 1-to-1 correspondence $z = e ^ { i \theta }$ between $\theta$ and $z$ and a 2-to-1 correspondence between $\theta$ and $x$ , with the symmetry $\mathcal { F } ( \boldsymbol { \theta } ) = \mathcal { F } ( - \boldsymbol { \theta } )$ , and the series is a trigonometric

polynomial:

$$
F o u r i e r ; \quad \theta \in [ - \pi , \pi ] , \quad \mathcal { F } ( \theta ) = \mathcal { F } ( - \theta ) \approx \frac { 1 } { 2 } \sum _ { k = 0 } ^ { n } a _ { k } ( e ^ { i k \theta } + e ^ { - i k \theta } ) .
$$

One can carry (3.1)–(3.3) further by introducing canonical systems of grid points in the three settings. We have already seen the $( n + 1 )$ -point Chebyshev grid,

$$
C h e b y s h e v ~ p o i n t s : ~ x _ { j } = \cos ( j \pi / n ) , ~ 0 \leq j \leq n ,
$$

and we have interpreted these in terms of the $( 2 n ) \mathrm { t h }$ roots of unity:

$$
R o o t s ~ o f ~ u n i t y . ~ z _ { j } = e ^ { i j \pi / n } , ~ - n + 1 \leq j \leq n .
$$

These grids are transplants of the set of $2 n$ equispaced points in $[ - \pi , \pi ]$ :

$$
E q u i s p a c e d ~ p o i n t s : \quad \theta _ { j } = j \pi / n , \quad - n + 1 \leq j \leq n .
$$

All three of these settings are unassailably important. Real analysts cannot do without Fourier, complex analysts cannot do without Laurent, and numerical analysts cannot do without Chebyshev. Moreover, the mathematics of the connections between the three frameworks is beautiful. But all this symmetry presents an expository problem. Without a doubt, a fully logical treatment should consider $x$ , $z$ , and $\theta$ in parallel. Each theorem should appear in three forms. Each application should be one of a trio.

It was on this basis that I started to write a book in 2008. The symmetries were elegant, but as the chapters accumulated, I came to realize that this would be a very long book and not a lovable one. The excellent logic was just a dead weight. The next year, I started again with the decision that the book would focus on $x \in [ - 1 , 1 ]$ . This is the setting closest to much of approximation theory and numerical analysis, and it has a further special feature: it is the one least familiar to people. Nobody is surprised if you compute a Fourier transform of a million data values, but the fact that you can compute a polynomial interpolant through a million Chebyshev points surprises people indeed.

Here then is the mathematical plan for this book. Our central interest will be the approximation of functions $f ( x )$ on $[ - 1 , 1 ]$ . When it comes to deriving formulas and proving theorems, however, we shall generally transplant to $F ( z )$ on the unit circle so as to take advantage of the tools of complex analysis.

Now let us turn to the definitions, already implicit in (3.1)–(3.3). The $k$ th Chebyshev polynomial can be defined as the real part of the function $z ^ { k }$ on the unit circle:

$$
\begin{array} { r } { x = \frac { 1 } { 2 } ( z + z ^ { - 1 } ) = \cos \theta , \quad \theta = \cos ^ { - 1 } x , } \end{array}
$$

$$
\begin{array} { r } { T _ { k } ( x ) = \frac { 1 } { 2 } ( z ^ { k } + z ^ { - k } ) = \cos ( k \theta ) . } \end{array}
$$

(Chebyshev polynomials were introduced by Chebyshev in the 1850s, though without the connection to the variables $z$ and $\theta$ [Chebyshev 1854 & 1859]. The label $T$ was apparently chosen by Bernstein, following French transliterations such as

“Tchebischeff.”) The Chebyshev polynomials are a family of orthogonal polynomials with respect to a certain weight function (Exercise 3.7), but we shall not use orthogonality until Chapters 17–19.

It follows from (3.8) that $T _ { k }$ satisfies $- 1 \leq T _ { k } ( x ) \leq 1$ for $x \in \left[ - 1 , 1 \right]$ and takes alternating values $\pm 1$ at the $k + 1$ Chebyshev points. What is not obvious is that $T _ { k }$ is a polynomial. We can verify this property by the computation

$$
{ \textstyle { \frac { 1 } { 2 } } } ( z + z ^ { - 1 } ) ( z ^ { k } + z ^ { - k } ) = { \textstyle { \frac { 1 } { 2 } } } ( z ^ { k + 1 } + z ^ { - k - 1 } ) + { \textstyle { \frac { 1 } { 2 } } } ( z ^ { k - 1 } + z ^ { - k + 1 } )
$$

for any $k \geq 1$ , that is,

$$
2 x T _ { k } ( x ) = T _ { k + 1 } ( x ) + T _ { k - 1 } ( x ) ,
$$

or in other words

$$
T _ { k + 1 } ( x ) = 2 x T _ { k } ( x ) - T _ { k - 1 } ( x ) .
$$

By induction, this 3-term recurrence relation implies that for each $k \geq 1$ , $T _ { k }$ is a polynomial of degree exactly $k$ with leading coefficient $2 ^ { k - 1 }$ . In Chapters 18 and 19 the coefficients of this recurrence will be taken as the entries of a “colleague matrix,” whose eigenvalues can be computed to find roots of polynomials or quadrature nodes.

The Chebfun command chebpoly(n) returns the chebfun corresponding to $T _ { n }$ . 1 Here, for example, are $T _ { 1 } , \ldots , T _ { 6 }$ :

for $\mathrm { ~ n ~ } = \mathrm { ~ 1 { : } ~ 6 ~ }$ , T{n} = chebpoly(n); subplot(3,2,n), plot(T{n}), end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/68bf43077d13d7c1f725d86d95ad84072ad9bc82a5fda182fa15547bcf1122fa.jpg)

These plots do not show the Chebyshev points, which are the extremes of each curve; thus the numbers of Chebyshev points in the six plots are 2, 3, 4, 5, 6, and 7.

Here are the coefficients of these polynomials with respect to the monomial basis $1 , x , x ^ { 2 } , \ldots$ . As usual, MATLAB orders coefficients from highest degree down to degree zero.

for n = 1:6, disp(poly(T{n})), end

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c } { { 1 } } & { { } } & { { } } & { { 0 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } &  \end{array}
$$

So, for example,

$$
T _ { 5 } ( x ) = 1 6 x ^ { 5 } - 2 0 x ^ { 3 } + 5 x .
$$

The monomial basis is familiar and comfortable, but you should never use it for numerical work with functions on an interval. Use the Chebyshev basis instead (Exercise 3.8). (If the domain is $[ a , b ]$ rather than $[ - 1 , 1 ]$ , the Chebyshev polynomials must be scaled accordingly, and Chebfun does this automatically when it works on other intervals.) For example, $x ^ { 5 }$ has the Chebyshev expansion

$$
x ^ { 5 } = \frac { 5 } { 8 0 } T _ { 5 } ( x ) + \frac { 5 } { 1 6 } T _ { 3 } ( x ) + \frac { 5 } { 8 } T _ { 1 } ( x ) .
$$

We can calculate such expansion coefficients by using the command chebpoly(p), where $p$ is the chebfun whose coefficients we want to know:

x = chebfun('x'); chebpoly(x^5)

ans $=$

0.0625 0 0.3125 0 0.6250

Any polynomial $p$ can be written uniquely like this as a finite Chebyshev series: the functions $T _ { 0 } ( x ) , T _ { 1 } ( x ) , \dots , T _ { n } ( x )$ form a basis for $\mathcal { P } _ { n }$ . Since $p$ is determined by its values at Chebyshev points, it follows that there is a 1-to-1 linear mapping between values at Chebyshev points and Chebyshev expansion coefficients. This mapping can be applied in $O ( n \log n )$ operations with the aid of the Fast Fourier Transform (FFT) or the Fast Cosine Transform, a crucial observation for practical work that was perhaps first made by Ahmed and Fisher and Orszag around 1970 [Ahmed $\&$ Fisher 1970, Orszag 1971a and 1971b, Gentleman 1972b, Geddes 1978]. This is what Chebfun does every time it constructs a chebfun. We shall not give details of the FFT.

Just as a polynomial $p$ has a finite Chebyshev series, a more general function $f$ has an infinite Chebyshev series. Exactly what kind of “more general function” can we allow? For an example like $f ( x ) = e ^ { x }$ with a rapidly converging Taylor series, everything will surely be straightforward, but what if $f$ is merely differentiable rather than analytic? Or what if it is continuous but not differentiable? Analysts have studied such cases carefully, identifying exactly what degrees of smoothness correspond to what kinds of convergence of Chebyshev series. We shall not concern ourselves with trying to state the sharpest possible result but will just make a particular assumption that covers most applications. We shall assume that $f$ is Lipschitz continuous on $[ - 1 , 1 ]$ . Recall that this means that there is a constant $C$ such that $| f ( x ) - f ( y ) | \leq C | x - y |$ for all $x , y \in [ - 1 , 1 ]$ . Recall also that a series is absolutely convergent if it remains convergent when each term is replaced by its absolute value, and that this implies that one can reorder the terms arbitrarily without changing the result. Such matters are discussed in analysis textbooks such as [Rudin 1976].

Here is our basic theorem about Chebyshev series and their coefficients.

Theorem 3.1. Chebyshev series. If $f$ is Lipschitz continuous on $[ - 1 , 1 ]$ , it has a unique representation as a Chebyshev series,

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) ,
$$

which is absolutely and uniformly convergent. The coefficients are given for $k \geq 1$ by the formula

$$
a _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \frac { f ( x ) T _ { k } ( x ) } { \sqrt { 1 - x ^ { 2 } } } d x
$$

and for $k = 0$ by the same formula with the factor $2 / \pi$ changed to $1 / \pi$

Proof. Equation (3.12) will come from the Cauchy integral formula, and to make this happen, we begin by transplanting $f$ to $F$ on the unit circle as described above: $F ( z ) = F ( z ^ { - 1 } ) = f ( x )$ with $x = ( z + z ^ { - 1 } ) / 2$ . To convert between integrals in $x$ and $z$ , we have to convert between $d x$ and $d z$ :

$$
\begin{array} { r } { d x = \frac 1 2 ( 1 - z ^ { - 2 } ) d z = \frac 1 2 z ^ { - 1 } ( z - z ^ { - 1 } ) d z . } \end{array}
$$

Since

$$
\textstyle { \frac { 1 } { 2 } } ( z - z ^ { - 1 } ) = i \operatorname { I m } z = \pm i { \sqrt { 1 - x ^ { 2 } } } ,
$$

this implies

$$
d x = \pm i z ^ { - 1 } { \sqrt { 1 - x ^ { 2 } } } d z .
$$

In these equations the plus sign applies for $\ln z \ge 0$ and the minus sign for√ $\ln z \le 0$ .

These formulas have implications for smoothness. Since ${ \sqrt { 1 - x ^ { 2 } } } \leq 1$ for all $x \in [ - 1 , 1 ]$ , they imply that if $f ( x )$ is Lipschitz continuous, then so is $F ( z )$ . By a standard result in Fourier analysis, this implies that $F$ has a unique representation as an absolutely and uniformly convergent Laurent series on the unit circle,

$$
F ( z ) = { \frac { 1 } { 2 } } \sum _ { k = 0 } ^ { \infty } a _ { k } ( z ^ { k } + z ^ { - k } ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) .
$$

Recall that a Laurent series is an infinite series in both positive and negative powers of $z$ , and that if $F ^ { \prime }$ is analytic, such a series converges in the interior of an annulus. A good treatment of Laurent series for analytic functions can be found in [Markushevich 1985]; see also other complex variables texts such as [Hille 1973, Priestley 2003, Saff & Snider 2003].

The $k$ th Laurent coefficient of a Lipschitz continuous function $\begin{array} { r l } { G ( z ) } & { { } = } \end{array}$ $\scriptstyle \sum _ { k = - \infty } ^ { \infty } b _ { k } z ^ { k }$ on the unit circle can be computed by the Cauchy integral formula,

$$
b _ { k } = { \frac { 1 } { 2 \pi i } } \int _ { | z | = 1 } z ^ { - 1 - k } G ( z ) d z .
$$

(We shall make more substantial use of the Cauchy integral formula in Chapters 8 and 11–12.) The notation $| z | = 1$ indicates that the contour consists of the unit circle traversed once in the positive (counterclockwise) direction. Here we have a function $F$ with the special symmetry property $F ( z ) = F ( z ^ { - 1 } )$ , and we have also introduced a factor $1 / 2$ in front of the series. Accordingly, we can compute the coefficients $a _ { k }$ from either of two contour integrals,

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { | z | = 1 } z ^ { - 1 + k } F ( z ) d z = { \frac { 1 } { \pi i } } \int _ { | z | = 1 } z ^ { - 1 - k } F ( z ) d z ,
$$

with $\pi i$ replaced by $2 \pi i$ for $k = 0$ .

In particular, we can get a formula for $a _ { k }$ that is symmetric in $k$ and $- k$ by combining the two integrals like this:

$$
a _ { k } = { \frac { 1 } { 2 \pi i } } \int _ { | z | = 1 } ( z ^ { - 1 + k } + z ^ { - 1 - k } ) F ( z ) d z = { \frac { 1 } { \pi i } } \int _ { | z | = 1 } z ^ { - 1 } T _ { k } ( x ) F ( z ) d z ,
$$

with $\pi i$ replaced by√ $2 \pi i$ for $k ~ = ~ 0$ . Replacing $F ( z )$ by $f ( x )$ and $z ^ { - 1 } d z$ by $- i d x / ( \pm \sqrt { 1 - x ^ { 2 } } )$ gives

$$
a _ { k } = - \frac { 1 } { \pi } \int _ { | z | = 1 } \frac { f ( x ) T _ { k } ( x ) } { \pm \sqrt { 1 - x ^ { 2 } } } d x ,
$$

with $\pi$ replaced by $2 \pi$ for $k = 0$ . We have now almost entirely converted to the $x$ variable, except that the contour of integration is still the circle $| z | = 1$ . When $z$ traverses the circle all the way around in the positive direction, $x$ decreases from 1 to $^ { - 1 }$ and then increases back to 1 again. At the turning point $z = x = - 1$ , the $\pm$ sign attached to the square root switches from $^ +$ to $-$ . Thus instead of canceling, the two traverses of $x \in [ - 1 , 1 ]$ contribute equal halves to $a _ { k }$ . Converting to a single integration from $^ { - 1 }$ to $^ { 1 }$ in the $x$ variable multiplies the integral by $- 1 / 2$ and hence multiplies the formula for $a _ { k }$ by $- 2$ , giving (3.12).

We now know that any function $f$ , so long as it is Lipschitz continuous, has a Chebyshev series. Chebfun represents a function as a finite series of some degree $n$ , storing both its values at Chebyshev points and also, equivalently, their Chebyshev coefficients. How does it figure out the right value of $n$ ? Given a set of $n + 1$ samples, it converts the data to a Chebyshev expansion of degree $n$ and examines the resulting Chebyshev coefficients. If several of these in a row fall below a relative level of approximately $1 0 ^ { - 1 5 }$ , then the grid is judged to be fine enough. For example, here are the Chebyshev coefficients of the chebfun corresponding to $e ^ { x }$ :

f = exp(x); chebcoeffs(f)

ans $=$

1.266065877752008   
1.130318207984970   
0.271495339534077   
0.044336849848664   
0.005474240442094   
0.000542926311914   
0.000044977322954   
0.000003198436462   
0.000000199212481   
0.000000011036772   
0.000000000550590   
0.000000000024980   
0.000000000001039   
0.000000000000040   
0.000000000000001

Notice that the last coefficient is about at the level of machine precision.

For complicated functions it is often more interesting to plot the coefficients than to list them. For example, here is a function with a number of wiggles:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/a38111d609b1c613fa82cd5c080ecc8b9adcd79544f13eeb366e15d78996273e.jpg)

If we plot the absolute values of the Chebyshev coefficients, here is what we find:

a $=$ chebcoeffs(f); semilogy(abs(a),'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/5be2ec1f43e4b7d1b635b6016ce0da4727c62c690c2d8e81d0d988c9d9675ecf.jpg)

One can explain this plot as follows. Up to a degree of approximately $k = 8 0$ , a Chebyshev series cannot resolve $f$ much at all, for the oscillations occur on too short wavelengths. After that, the series begins to converge rapidly. By the time we reach $k = 1 5 0$ , the accuracy is about 15 digits, and the computed Chebyshev series is truncated there. We can find out exactly where the truncation took place with the command length(f):

length(f)

This tells us that the chebfun is a polynomial interpolant through 151 points, that is, of degree 150.

Without giving all the engineering details (see Aurentz & Trefethen 2017b), here is a fuller description of how Chebfun constructs its approximation. First it calculates the polynomial interpolant through the function sampled at 17 Chebyshev points, i.e., a polynomial of degree 16, and checks whether the Chebyshev coefficients appear to be small enough. For the example just given, the answer is no. Then it tries 33 points, then 65, and so on. In this case Chebfun judges at 257 points that the Chebyshev coefficients have fallen to the level of rounding error. At this point it truncates the tail of terms deemed to be negligible, leaving a series of 151 terms (Exercise 3.13). The corresponding degree 150 polynomial is then evaluated at 151 Chebyshev points via the FFT, and these 151 numbers become the data defining this particular chebfun. Engineers would say that the signal has been downsampled from 257 points to 151.

For another example we consider a function with two spikes:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/38f4bc5beb53618c5e4c94687cfc271e28765dbac3d0e73350ca3cf36d2a5d54.jpg)

Here are the Chebyshev coefficients of the chebfun. This time, instead of chebcoeffs and semilogy, we execute the special command plotcoeffs, which has the same effect.

plotcoeffs(f,'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/7d5983c43a58691660a94bfe374771938eea932b1df109b376064066a476e7c4.jpg)

Note that although it is far less wiggly, this function needs six times as many points to resolve as the previous one (Exercise 3.13). We shall explain these polynomial degrees in Chapter 8.

Chebyshev interpolants are effective for complex functions (still defined on a real interval) as well as real ones. Here, for example, is a complex function that happens to be periodic, though the Chebyshev representation does not take advantage of this fact.

$\begin{array} { r l r } { \mathbf { f } } & { = } & { \left( 3 + \sin \left( 1 0 ^ { \ast } \mathbf { p } \mathbf { i } ^ { \ast } \mathbf { x } \right) + \sin \left( 6 1 ^ { \ast } \mathbf { e x p } \left( . 8 \ast \sin \left( \mathbf { p } \mathbf { i } ^ { \ast } \mathbf { x } \right) + . 7 \right) \right) \right) \ast \mathbf { e x p } \left( 1 \mathbf { i } ^ { \ast } \mathbf { p } \mathbf { i } ^ { \ast } \mathbf { x } \right) ; } \end{array}$ A plot shows the image of $[ - 1 , 1 ]$ under $f$ , which appears complicated: plot(f,'color',[0 .8 0])

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/55ab47f52feebe6e58596e0e70bbdb4d5d3c05874ee41bb7850c7d816d5e13c7.jpg)

Yet the degree of the polynomial is not so high:

length(f)

ans = 617

People often ask, Is there anything special about Chebyshev points and Chebyshev polynomials? Could we equally well interpolate in other points and expand in other sets of polynomials? From an approximation point of view, the answer is yes, and in particular, Legendre points and polynomials have approximately the same power for representing a general function $f$ , as we shall see in Chapters $1 7 -$ 19. Legendre points and polynomials are neither much better than Chebyshev for approximating functions nor much worse; they are essentially the same. One can improve upon both Legendre and Chebyshev, shrinking the number of sample points needed to represent a given function by a factor of up to $\pi / 2$ , but to do so one must leave the class of polynomials. See Chapter 22.

Nevertheless, there is a big advantage of Chebyshev over Legendre points, and this is that one can use the FFT to go from point values to coefficients and back again. There are algorithms that make such computations practicable for Legendre interpolants too [Piessens 1974, Alpert & Rokhlin 1991, Dutt, Gu & Rokhlin 1996, Potts, Steidl & Tasche 1998, Iserles 2011]—see also Theorem 19.6 of this book—but Chebyshev remains the easiest case.

Summary of Chapter 3. The Chebyshev polynomial $T _ { k } ( x )$ is an analogue for $[ - 1 , 1 ]$ of the monomial $z ^ { k }$ on the unit circle. Each Lipschitz continuous function $f$ on $\lfloor - 1 , 1 \rfloor$ has an absolutely and uniformly convergent Chebyshev series, that is, an expansion $f ( x ) = a _ { 0 } T _ { 0 } ( x ) + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot$ .

Exercise 3.1. Monomial and Chebyshev coefficients. Let $p \in \mathcal { P } _ { n }$ have coefficient vectors $a = ( a _ { 0 } , a _ { 1 } , \ldots , a _ { n } ) ^ { T }$ for a Chebyshev series and $b = ( b _ { 0 } , b _ { 1 } , \ldots , b _ { n } ) ^ { \scriptscriptstyle T }$ for a series in the monomials $1 , x , \ldots , x ^ { \pi }$ . Show that $a$ and $b$ are related by $A a = b$ , where $A$ is an uppertriangular matrix, whose entries you should describe precisely, though you don’t have to give explicit formulas for them. Prove that any $p \in \mathcal { P } _ { n }$ has uniquely defined coefficient vectors $a$ and $b$ for both representations.

Exercise 3.2. A Chebyshev coefficient. Use Chebfun to determine numerically the coefficient of $T _ { 5 }$ in the Chebyshev expansion of $\tan ^ { - 1 } ( x )$ on $[ - 1 , 1 ]$ .

Exercise 3.3. Chebyshev coefficients and “rat.” (a) Use Chebfun to determine numerically the coefficients of the Chebyshev series for $1 + x ^ { 3 } + x ^ { 4 }$ . By inspection, identify these rational numbers. Use the MATLAB command $[ { \bf n } , { \bf d } ] = { \bf r a t } ( { \bf c } )$ to confirm this. (b) Use Chebfun and rat to make good guesses as to the Chebyshev coefficients of $x ^ { 7 } / 7 + x ^ { 9 } / 9$ . (Of course it is not hard to figure them out analytically.)

Exercise 3.4. Dependence on wave number. (a) Calculate the length $L ( k )$ of the chebfun corresponding to $f ( x ) = \sin ( k x )$ on $[ - 1 , 1 ]$ for $k = 1 , 2 , 4 , 8 , \ldots , 2 ^ { 1 0 }$ . (You can do this elegantly by defining a MATLAB anonymous function $\textbf { f } = \Theta ( \mathbf { k } ) \ldots$ ) Make a loglog plot of $L ( k )$ as a function of $k$ and comment on the result. (b) Do the same for $g ( x ) =$ $1 / ( 1 + ( k x ) ^ { 2 } )$ .

Exercise 3.5. Chebyshev series of a complicated function. (a) Make chebfuns of the three functions $f ( x ) = \operatorname { t a n h } ( x )$ , $g ( x ) = 1 0 ^ { - 5 } \operatorname { t a n h } ( 1 0 x )$ , $h ( x ) = 1 0 ^ { - 1 0 } \operatorname { t a n h } ( 1 0 0 x )$ on $[ - 1 , 1 ]$ , and call plotcoeffs to show their Chebyshev coefficients. Comment on the results. (b) Now define $s = f + g + h$ and comment on the result of plotcoeffs applied to $s$ . Chebfun does not automatically chop the tail of a Chebyshev series obtained by summation, but applying the simplify command will do this. What happens with plotcoeffs(simplify(s))?

Exercise 3.6. Chebyshev series of $\mathbf { s i g n } ( x )$ and $| x |$ [Bernstein 1914b]. Derive the following Chebyshev series coefficients by using the first equality in (3.14). (a) For $f ( x ) = \operatorname { s i g n } ( x )$ , $a _ { k } ~ = ~ 0$ for $k$ even and $a _ { k } = ( 4 / \pi ) ( - 1 ) ^ { ( k - 1 ) / 2 } / k$ for $k$ odd. (b) For $f ( x ) = \left| x \right|$ , $a _ { k } = 0$ for $k$ odd, $a _ { 0 } = 2 / \pi$ , and $a _ { k } = ( 4 / \pi ) ( - 1 ) ^ { ( k / 2 ) } / ( 1 - k ^ { 2 } )$ for $k \geq 2$ even.

Exercise 3.7. Orthogonality of Chebyshev polynomials. Equation (3.12) gives the Chebyshev coefficient $a _ { k }$ of $f$ by integration of $f$ against just the single Chebyshev polynomial $T _ { k }$ . This formula implies an orthogonality property for $\{ T _ { j } \}$ involving a weighted integral. State exactly what this orthogonality property is and show carefully how it follows from the equations of this chapter.

Exercise 3.8. Conditioning of the Chebyshev basis. Although the Chebyshev polynomials are not orthogonal with respect to the standard unweighted inner product, they are close enough to orthogonal to provide a well-behaved basis. Set $\boldsymbol { \mathrm { ~ T ~ } } =$ chebpoly(0:10) and explore the Chebfun “quasimatrix” that results with commands like size(T), spy(T), plot(T), svd(T). Explain the meaning of T (you may find Chapter 6 of the Chebfun Guide helpful) and determine the condition number of this basis with cond(T). (b) Now construct the corresponding quasimatrix of monomials by executing $\textbf { x } = \mathtt { c h e b f u n } ( ^ { \prime } \textbf x ^ { \prime } ) ; \mathbb { M } \ =$ T; for $\mathrm { ~ j ~ } = ~ 0 { : } 1 0 , ~ \mathsf { M } ( : , \mathsf { j } { + } 1 ) ~ = ~ \mathsf { x } ^ { \cdot } \mathrm { j }$ ; end. What is the condition number of M? (c) Produce a plot of these two condition numbers for quasimatrices whose columns span $\mathcal { P } _ { n }$ over $[ - 1 , 1 ]$ for $n = 0 , 1 , \ldots , 1 0$ . (d) What happens to the condition numbers if $M$ is constructed from monomials on [0, 1] rather than $[ - 1 , 1 ]$ via $\mathrm { ~ \tt ~ x ~ } =$ chebfun( $" \mathbf { x } \cdot \mathbf { \xi }$ ,[0,1])?

Exercise 3.9. Derivatives at endpoints. Prove from (3.10) that the derivatives of the Chebyshev polynomials satisfy $T _ { n } ^ { \prime } ( 1 ) = n ^ { 2 }$ for each $n \geq 0$ . (Markov’s inequality asserts that for any $p \in { \mathcal { P } } _ { n }$ , $\| p ^ { \prime } \| \leq n ^ { 2 } \| p \|$ , where $\| \cdot \|$ is the supremum norm.)

Exercise 3.10. Odd and even functions. Prove that if $f$ is an odd function on $[ - 1 , 1 ]$ , its Chebyshev coefficients of even order are zero; prove similarly that if $f$ is even, its odd-order coefficients are zero.

Exercise 3.11. A function neither even nor odd. Apply plotcoeffs to the chebfun for $f ( x ) = \exp ( x ) / ( 1 + 1 0 0 0 0 x ^ { 2 } )$ . Why does the plot have the appearance of a stripe?

Exercise 3.12. Extrema and roots of Chebyshev polynomials. Give formulas for the extrema and roots of $T _ { n }$ in $[ - 1 , 1 ]$ .

Exercise 3.13. Chebyshev coefficients and machine precision. By a command like $\mathbf { f } ~ = ~ \mathbf { \mathrm { c h e b f u n } } ( \mathbf { \ " e x p } ( \mathbf { x } ) \mathbf { \ " } , \mathbf { n p } )$ , one can force Chebfun to produce a chebfun of length np (i.e., degree $\tt n p - 1$ ) rather than determine the length automatically. (a) Do this for the “function with wiggles” of this section with $\mathtt { n p } = 2 5 7$ , and comment on how the plotcoeffs result differs from that shown in the text. (b) Likewise for the “function with two spikes” with np = 2049.

Exercise 3.14. Chebyshev series for a simple pole. (a) Let $t$ be a complex number with $| t | < 1$ and define $F ( z ) = ( z - t ) ^ { - 1 } + ( z ^ { - 1 } - t ) ^ { - 1 }$ . What is the Laurent series for $F ^ { \prime }$ ? (b) For the same $t$ , show further that

$$
1 + 2 \sum _ { k = 1 } ^ { \infty } t ^ { k } T _ { k } ( x ) = \frac { 1 - t ^ { 2 } } { 1 - 2 t x + t ^ { 2 } } .
$$

(This formula can be interpreted as a generating function for the Chebyshev polynomials.) (c) Let $a \not \in [ - 1 , 1 ]$ be a real or complex number and let $t$ be a real or complex number with $| t | < 1$ such that $( t + t ^ { - 1 } ) / 2 = a$ . Show that

$$
\frac { 1 } { x - a } = \frac { 2 } { t - t ^ { - 1 } } \left[ 1 + 2 \sum _ { k = 1 } ^ { \infty } t ^ { k } T _ { k } ( x ) \right] .
$$

Exercise 3.15. Chebyshev series of $e ^ { a x }$ . It can be shown that the Chebyshev series of $e ^ { a x }$ is

$$
e ^ { a x } = 2 \sum _ { k = 0 } ^ { \infty } { } ^ { \prime } I _ { k } ( a ) T _ { k } ( x ) ,
$$

where $I _ { k }$ is the modified Bessel function of the first kind and the prime indicates that the term $k = 0$ is to be multiplied by $1 / 2$ . Derive the Chebyshev series for $\sinh ( a x )$ and $\cosh ( a x )$ .

Exercise 3.16. Clenshaw’s algorithm. Let a polynomial $p \in \mathcal { P } _ { n }$ be given by a finite Chebyshev series (3.11) and let $x \in [ - 1 , 1 ]$ be given. Show that $p ( x )$ can be evaluated by the following process. Set $u _ { n + 1 } = 0$ and $u _ { n } = a _ { n }$ and

$$
u _ { k } = 2 x u _ { k + 1 } - u _ { k + 2 } + a _ { k } , \quad k = n - 1 , n - 2 , \ldots , 0 .
$$

Then $\begin{array} { r } { p ( x ) = \frac { 1 } { 2 } ( a _ { 0 } + u _ { 0 } - u _ { 2 } ) } \end{array}$ .

# Chapter 4. Interpolants, Projections, and Aliasing

Suppose $f ( x )$ is a Lipschitz continuous function on $[ - 1 , 1 ]$ with Chebyshev series coefficients $\{ a _ { k } \}$ as in Theorem 3.1,

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) .
$$

One approximation to $f$ in $\mathcal { P } _ { n }$ is the polynomial obtained by interpolation in Chebyshev points:

$$
p _ { n } ( x ) = \sum _ { k = 0 } ^ { n } c _ { k } T _ { k } ( x ) .
$$

Another is the polynomial obtained by truncation or projection of the series to degree $n$ , whose coefficients through degree $n$ are the same as those of $f$ itself:

$$
f _ { n } ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } T _ { k } ( x ) .
$$

The relationship of the Chebyshev coefficients of $f _ { n }$ to those of $f$ is obvious, and in a moment we shall see that the Chebyshev coefficients of $p _ { n }$ have simple expressions too. In computational work generally, and in particular in Chebfun, the polynomials $\left\{ p _ { n } \right\}$ are usually almost as good approximations to $f$ as the polynomials $\left\{ f _ { n } \right\}$ and are easier to work with, since one does not need to evaluate the integral (3.12). The polynomials $\left\{ f _ { n } \right\}$ , on the other hand, are also interesting. In this book, most of our computations will make use of $\left\{ p _ { n } \right\}$ , but many of our theorems will treat both cases. A typical example is Theorem 8.2, which asserts that if $f$ is analytic on $[ - 1 , 1 ]$ , then both $\| f - f _ { n } \|$ and $\| f - p _ { n } \|$ decrease geometrically to $0$ as $n \to \infty$ .

The key to understanding $\left\{ c _ { k } \right\}$ is the phenomenon of aliasing, a term that originated with radio engineers early in the 20th century. On the $( n { + } 1 )$ -point Chebyshev grid, it is obvious that any function $f$ is indistinguishable from a polynomial of degree $n$ . But something more is true: any Chebyshev polynomial $T _ { N }$ , no matter how big $N$ is, is indistinguishable on the grid from a single Chebyshev polynomial $T _ { m }$ for some $m$ with $0 \leq m \leq n$ . We state this as a theorem.

Theorem 4.1. Aliasing of Chebyshev polynomials. For any $n \geq 1$ and $0 ~ \leq ~ m ~ \leq ~ n$ , the following Chebyshev polynomials take the same values on the $( n + 1 )$ -point Chebyshev grid:

$$
T _ { m } , T _ { 2 n - m } , T _ { 2 n + m } , T _ { 4 n - m } , T _ { 4 n + m } , T _ { 6 n - m } , . . . .
$$

Equivalently, for any $k \geq 0$ , $T _ { k }$ takes the same value on the grid as $T _ { m }$ with

$$
m = | ( k + n - 1 ) ( { \bmod { 2 n } } ) - ( n - 1 ) | ,
$$

a number in the range $0 \leq m \leq n$ .

Proof. Recall from (2.1) and (3.8) that Chebyshev polynomials on $[ - 1 , 1 ]$ are related to monomials on the unit circle by $T _ { m } ( x ) = ( z ^ { m } + z ^ { - m } ) / 2$ , and Chebyshev points are related to $( 2 n ) \mathrm { t h }$ roots of unity by $x _ { n } = ( z _ { n } + z _ { n } ^ { - 1 } ) / 2$ . It follows that the first assertion of the theorem is equivalent to the statement that the following functions take the same values at the $( 2 n ) \mathrm { t h }$ roots of unity:

$$
z ^ { m } + z ^ { - m } , \ z ^ { 2 n - m } + z ^ { m - 2 n } , \ z ^ { 2 n + m } + z ^ { - 2 n - m } , \cdot \cdot \cdot \cdot
$$

Inspection of the exponents shows that in every case, modulo $2 n$ , we have one exponent equal to $+ m$ and the other to $- m$ . The conclusion now follows from the elementary phenomenon of aliasing of monomials on the unit circle: at the $( 2 n ) \mathrm { t h }$ roots of unity, $z ^ { 2 \nu n } = 1$ for any integer $\nu$ .

For the second assertion (4.4), suppose first that $0 \leq k \left( { \bmod { 2 } } n \right) \leq n$ . Then $n - 1 \leq ( k + n - 1 ) ( { \bmod { 2 n } } ) \leq 2 n - 1$ , so (4.4) reduces to $m = k ( { \bmod { 2 } } n )$ , with $0 \leq m \leq n$ , and we have just shown that this implies that $T _ { k }$ and $T _ { m }$ take the same values on the grid. On the other hand, suppose that $n + 1 \leq k { \bigl ( } { \mathrm { m o d } } 2 n { \bigr ) } \leq 2 n - 1$ . Then $0 \leq ( k + n - 1 ) ( { \bmod { 2 n } } ) \leq n - 2$ , so the absolute value becomes a negation and (4.4) reduces to $m = ( - k ) ( { \bmod { 2 } } n )$ , with $1 \leq m \leq n - 1$ . Again we have just shown that this implies that $T _ { k }$ and $T _ { m }$ take the same values on the grid.

Here is a numerical illustration of Theorem 4.1. Taking $n = 4$ , let $\mathtt { X }$ be the Chebyshev grid with $n { \mathrel { + { 1 } } }$ points, and let $T \{ 1 \} , \ldots , T \{ 1 0 \}$ be the first 10 Chebyshev polynomials:

Then $T _ { 3 }$ and $T _ { 5 }$ are the same on the grid:

disp([T{3}(X) T{5}(X)])

T3 T5   
-1.000000000000000 -1.000000000000000   
0.707106781186548 0.707106781186547   
0 0   
-0.707106781186548 -0.707106781186547   
1.000000000000000 1.000000000000000

So are $T _ { 1 }$ , $T _ { 7 }$ , and $T _ { 9 }$ :

disp([T{1}(X) T{7}(X) T{9}(X)])

T1 T7 T9   
-1.000000000000000 -1.000000000000000 -1.000000000000000   
-0.707106781186547 -0.707106781186548 -0.707106781186547   
0 0 0   
0.707106781186547 0.707106781186548 0.707106781186547   
1.000000000000000 1.000000000000000 1.000000000000000

As a corollary of Theorem 4.1, we can now derive the connection between $\{ a _ { k } \}$ and $\left\{ c _ { k } \right\}$ . The following result can be found in [Clenshaw & Curtis 1960].

Theorem 4.2. Aliasing formula for Chebyshev coefficients. Let $f$ be Lipschitz continuous on $[ - 1 , 1 ]$ , and let $p _ { n }$ be its Chebyshev interpolant in $\mathcal { P } _ { n }$ , $n \geq 1$ . Let $\{ a _ { k } \}$ and $\left\{ c _ { k } \right\}$ be the Chebyshev coefficients of $f$ and $p _ { n }$ , respectively. Then

$$
\begin{array} { l } { { c _ { 0 } = a _ { 0 } + a _ { 2 n } + a _ { 4 n } + \cdots , } } \\ { { } } \\ { { c _ { n } = a _ { n } + a _ { 3 n } + a _ { 5 n } + \cdots , } } \end{array}
$$

and for $1 \leq k \leq n - 1$ ,

$$
c _ { k } = a _ { k } + ( a _ { k + 2 n } + a _ { k + 4 n } + \cdot \cdot \cdot ) + ( a _ { - k + 2 n } + a _ { - k + 4 n } + \cdot \cdot \cdot ) .
$$

Proof. By Theorem 3.1, $f$ has a unique Chebyshev series (3.11), and it converges absolutely. Thus we can rearrange the terms of the series without affecting convergence, and in particular, each of the three series expansions written above converges since they correspond to the Chebyshev series (3.11) evaluated at $x = 1$ . So the formulas (4.5)–(4.7) do indeed define certain numbers $c _ { 0 } , \ldots , c _ { n }$ . Taking these numbers as coefficients multiplied by the corresponding Chebyshev polynomials $T _ { 0 } , \ldots , T _ { n }$ gives us a polynomial of degree $n$ . By Theorem 4.1, this polynomial takes the same values as $f$ at each point of the Chebyshev grid. Thus it is the unique interpolant $p _ { n } \in \mathcal { P } _ { n }$ .

We can summarize Theorem 4.2 as follows. On the $( n + 1 )$ -point grid, any function $f$ is indistinguishable from a polynomial of degree $n$ . In particular, the Chebyshev series of the polynomial interpolant to $f$ is obtained by reassigning all the Chebyshev coefficients in the infinite series for $f$ to their aliases of degrees 0 through $n$ .

As a corollary, Theorems 4.1 and 4.2 give us absolutely convergent series for $f - f _ { n }$ and $f - p _ { n }$ , which we shall exploit in Chapters 7 and 8:

$$
f ( x ) - f _ { n } ( x ) = \sum _ { k = n + 1 } ^ { \infty } a _ { k } T _ { k } ( x ) ,
$$

$$
f ( x ) - p _ { n } ( x ) = \sum _ { k = n + 1 } ^ { \infty } a _ { k } ( T _ { k } ( x ) - T _ { m } ( x ) ) ,
$$

where $m = m ( k , n )$ is given by (4.4).

To illustrate Theorem 4.2, here is the function $f ( x ) = \operatorname { t a n h } ( 4 x - 1 )$ (solid) and its degree 4 Chebyshev interpolant $p _ { 4 } ( x )$ (dashed):

x = chebfun('x'); f = tanh( $4 * \mathbf { x } - 1 )$ ; $\mathrm { ~ n ~ } = \mathrm { ~ 4 ~ }$ ; pn $=$ chebfun(f, $\ n { + } 1 $ ); plot(f), hold on, plot(pn,'.--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/84418133a7618ae8edae1555741d0d56e9de746ebecdc608b0af410e69a41275.jpg)

The first 5 Chebyshev coefficients of $f$ , a $=$ chebpoly(f); a = a(end:-1:1)'; a(1:n+1)

ans $=$   
-0.166584582703135   
1.193005991160944   
0.278438064117869   
-0.239362401056012   
-0.176961398392888

are different from the Chebyshev coefficients of $p _ { n }$ ,

c $=$ chebpoly(pn); c $=$ c(end:-1:1)'   
c = -0.203351068209675 1.187719968517890 0.379583465333916 -0.190237989543227 -0.178659622412173

As asserted in (4.5) and (4.6), the coefficients $c _ { 0 }$ and $c _ { n }$ are given by sums of coefficients $a _ { k }$ with a stride of $2 n$ :

c0 = sum(a(1:2\*n:end)), cn = sum(a(n+1:2\*n:end))

$\mathsf { c 0 } \ = \ - 0 \ . 2 0 3 3 5 1 0 6 8 2 0 9 6 7 5$ $\mathtt { c n } \ = \ - 0 . 1 7 8 6 5 9 6 2 2 4 1 2 1 7 4$

And as asserted in (4.7), the coefficients $c _ { 1 }$ through $c _ { n - 1 }$ involve two sums of this kind:

for $\mathtt { k } \ = \ 1 { : } \mathtt { n - 1 }$ ck $=$ sum(a(1+k:2\*n:end)) + sum(a(1-k+2\*n:2\*n:end))   
end

ck = 1.187719968517889   
ck = 0.379583465333916   
ck = -0.190237989543227

Following up on the last figure, how does the truncated series $f _ { n }$ compare with the interpolant $p _ { n }$ as an approximation to $f$ ? Chebfun includes a 'trunc' option for computing $f _ { n }$ , which we now add to the plot as a dot-dash line:

fn $=$ chebfun(f,'trunc', $\tt { n } { + } 1$ ); plot(fn,'-.g')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/c3400146e9e81a4fe3f33873b958a85347149eefbc2cba3306720e9892245901.jpg)

Here are the errors $f - f _ { n }$ and $f - p _ { n }$ :

subplot(1,2,1), plot(f-fn, $" \mathtt { g } ^ { \prime }$ ), subplot(1,2,2), plot(f-pn,'r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/2b24a7bbb741c1e16f18e5ca8d1105d962920a71e53b9ba4b0aaed099e3195ee.jpg)

Here is the analogous plot with $n = 4$ increased to 24:

$\tt { n } = 2 4$ ; pn $=$ chebfun(f, $\mathtt { n } + 1 )$ ; fn $=$ chebfun(f,'trunc', $\ n { + } 1 \cdot$ ); subplot(1,2,1), plot(f-fn, $" \mathtt { g } " .$ ), subplot(1,2,2), plot(f-pn, $" \mathbf { r } \cdot \mathbf { \xi }$ )

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/bced4887f07c445164e08746af701fc74e33ce0d61fe7e2a9ead14ee92130e4b.jpg)

On the basis of plots like these, one might speculate that $f _ { n }$ may often be a better approximation than $p _ { n }$ but that the difference is small. This is indeed the case, as we shall confirm in Theorems 7.2 and 8.2, both of which suggest a difference of a factor of 2, and Theorem 16.1, which suggests a factor of $\pi / 2$ .

Let us review where we stand. We have considered Chebyshev interpolants (Chapter 2) and Chebyshev expansions (Chapter 3) for a Lipschitz continuous function $f ( x )$ defined on $[ - 1 , 1 ]$ . Mathematically speaking, each coefficient of a Chebyshev expansion is equal to the value of the integral (3.12). This formula, however, is not needed for effective polynomial approximation, since Chebyshev interpolants are nearly as accurate as projections. Chebfun readily computes Chebyshev coefficients of polynomial interpolants, and this is done not by evaluating the integral but by taking the FFT of the sample values in Chebyshev points. If the degree of the interpolant is high enough that the polynomial matches $f$ to machine precision, then the Chebyshev coefficients will usually match too.

Summary of Chapter 4. Two excellent methods of approximating a function $f$ on $[ - 1 , 1 ]$ by a polynomial are truncation of its Chebyshev series, also known as projection, and interpolation in Chebyshev points. The Chebyshev interpolant is the polynomial obtained by reassigning contributions of degree $> n$ in the Chebyshev series to their aliases of degree $\leq n$ . The two approximations are typically within a factor of 2 of each other in accuracy.

Exercise 4.1. Node polynomial for Chebyshev points. Show using Theorem 4.1 that $p ( x ) = 2 ^ { - n } ( T _ { n + 1 } ( x ) - T _ { n - 1 } ( x ) )$ is the unique monic polynomial in $\mathcal { P } _ { n + 1 }$ with zeros at the $n + 1$ Chebyshev points (2.2).

Exercise 4.2. Examples of aliasing. (a) On the $( n + 1 )$ -point Chebyshev grid with $n = 2 0$ , which Chebyshev polynomials $T _ { k }$ take the same values as $T 5$ ? (b) Use Chebfun to draw plots illustrating some of these intersections.

Exercise 4.3. Aliasing in roots of unity. For each $n \geq 0$ , let $p _ { n } \in \mathcal { P } _ { n }$ be the degree $n$ polynomial interpolant to the function $f ( z ) = z ^ { - 1 }$ at the $( n + 1 ) \mathrm { s t }$ roots of unity on the unit circle in the $z$ -plane. Use the aliasing observation of the proof of Theorem 4.1 to prove that in the closed unit disk of complex numbers $z$ with $| z | \le 1$ , there is one and only one value $z$ for which $p _ { n }$ converges to $f$ as $n  \infty$ . (This example comes from [M´eray 1884].)

Exercise 4.4. Fooling the Chebfun constructor. (a) Construct the MATLAB anonymous function $\textbf { f } = \textsf { Q } ( \mathbb { M } )$ chebfu $\mathtt { n } ( \ @ ( \mathbf { x } ) 1 { + } \mathtt { e x p } ( - ( \mathtt { M } * ( \mathbf { x } { - } 0 . 4 ) ) \hat { - } 4 ) \mathtt { ) }$ ) and plot f(10) and $\mathtt { f } \left( 1 0 0 \right)$ . This function has a narrow spike of width proportional to $1 / M$ . Confirm this by comparing $\mathtt { s u m } ( \mathtt { f } \left( 1 0 \right) )$ and sum(f(100)). (b) Plot length(f(M)) as a function of $M$ for $M = 1 , 2 , 3 , \ldots$ , going into the region where the length becomes 1. What do you think is happening? (c) Let Mmax be the largest integer for which the constructor behaves normally and execute semilogy( $\texttt { f } ( \mathtt { M m a x } ) - 1 )$ . Superimpose on this plot information to show the locations of the points returned by chebpts(17), which is the default initial grid on which Chebfun samples a function. Explain how this result fits with (b). (d) Now for np taking values 33, 65, 129, execute chebfunpref.setDefaults('minSamples',np) and length( $\mathbf { f } \left( \mathtt { M m a x } { + } 1 \right) )$ , and plot the Chebyshev points on your semilog plot of (c). The minSamples flag forces Chebfun to sample the function at the indicated number of points. How do these results match your observations of (b) and (c)? When you’re done, be sure to return Chebfun to its default state with chebfunpref.setDefaults('factory').

Exercise 4.5. Relative precision. Try Exercise 4.4 again but without the “1+” in the definition of $\pm$ . The value of Mmax will be different, and the reason has to do with the Chebfun aim of constructing each function to about 15 digits of relative precision, not absolute. Can you figure out what is happening and explain it quantitatively?

Exercise 4.6. Chebfun computation of truncations. In the text we computed Chebyshev truncations of $f ( x ) = \mathrm { t a n h } ( 4 x - 1 )$ using the 'trunc' flag in the Chebfun constructor. Another method is to compute all the Chebyshev coefficients of $f$ down to machine precision by making a chebfun of $f$ , then truncate the series. Compute $f _ { 4 }$ by this method and verify that the results agree to machine precision.

Exercise 4.7. When projection equals interpolation. Sometimes the projection $f _ { n }$ and the interpolant $p _ { n }$ are identical, even though both differ from $f$ . Characterize exactly when this occurs, and give an example with $n = 3$ .

# Chapter 5. Barycentric Interpolation Formula

How does one evaluate a Chebyshev interpolant? One good approach, involving $O ( n \log n )$ work for a single point evaluation, is to compute Chebyshev coefficients and use the Chebyshev series. However, there is a direct method requiring just $O ( n )$ work, not based on the series expansion, that is both elegant and numerically stable. It also has the advantage of generalizing to sets of points other than Chebyshev. It is called the barycentric interpolation formula, introduced by Salzer [1972], with an earlier closely related formula due to Marcel Riesz [1916]. The more general barycentric formula for arbitrary interpolation points, of which Salzer’s formula is an exceptionally simple special case, was developed earlier by Dupuy [1948], with origins at least as early as Jacobi [1825]. Taylor [1945] introduced the barycentric formula for equispaced grid points. For a survey of barycentric formulas, see [Berrut $\&$ Trefethen 2004].

The study of polynomial interpolation goes back a long time; the word “interpolation” may be due to Wallis in 1656 (see [Pearson 1920] for an early account of some of the history). In particular, Newton addressed the topic and devised a method based on divided differences. Many textbooks claim that it is important to use Newton’s formulation for reasons of numerical stability, but this is not true, and we shall not discuss Newton’s approach.

Instead, the barycentric formula is of the alternative Lagrange form, where the interpolant is written as a linear combination of Lagrange or cardinal or fundamental polynomials:

$$
p ( x ) = \sum _ { j = 0 } ^ { n } f _ { j } \ell _ { j } ( x ) .
$$

Here we have a set of distinct interpolation points $x _ { 0 } , \ldots , x _ { n }$ , which could be real or complex, and $\ell _ { j } ( x )$ , the $j$ th Lagrange polynomial, is the unique polynomial in

$\mathcal { P } _ { n }$ that takes the value $1$ at and $0$ at the other points : $x _ { j }$ $x _ { k }$

$$
\ell _ { j } ( x _ { k } ) = \left\{ \begin{array} { l l } { 1 , } & { k = j , } \\ { 0 , } & { k \neq j . } \end{array} \right.
$$

For example, here is a plot of $\ell _ { 5 }$ on the equispaced 7-point grid (i.e., $n = 6$ ):

${ \mathrm { ~ d ~ } } =$ domain(-1,1); s = linspace(-1,1,7); y = [0 0 0 0 0 1 0]; $\mathtt { p } \ =$ interp1(s,y,d); plot(p), hold on, plot(s,p(s),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/7ada0eebcb2ee5cdf0418824c694efc707322b0982fec40be5c7c0e25b9f3437.jpg)

It is easy to write down an explicit expression for $\ell _ { j }$ :

$$
\ell _ { j } ( x ) = { \frac { \prod _ { k \neq j } ( x - x _ { k } ) } { \prod _ { k \neq j } ( x _ { j } - x _ { k } ) } } .
$$

Since the denominator is a constant, this function is a polynomial of degree $n$ with zeros at the right places, and clearly it takes the value 1 when $x = x _ { j }$ . Equation (5.3) is very well known and can be found in many textbooks as a standard representation for Lagrange interpolants. Lagrange worked with (5.1) and (5.3) in 1795 [Lagrange 1795], and his name is firmly attached to these ideas,2 but the same formulas were published earlier by Waring [1779] and by Euler [1783], who had been Lagrange’s predecessor at the Berlin Academy.

Computationally speaking, (5.1) is excellent but (5.3) is not so good. It requires $O ( n )$ operations to evaluate $\ell _ { j } ( x )$ for each value of $x$ , and then $O ( n )$ such evaluations must be added up in (5.1), giving a total operation count of $O ( n ^ { 2 } )$ for evaluating $p ( x )$ at a single value of $x$ .

By a little rearrangement we can improve the operation count. The key observation is that for the various values of $j$ , the numerators in (5.3) are the same except that they are missing different factors $\boldsymbol { x } - \boldsymbol { x _ { j } }$ . To take advantage of this commonality, we define the node polynomial $\ell \in \mathcal { P } _ { n + 1 }$ for the given grid by

$$
\ell ( x ) = \prod _ { k = 0 } ^ { n } ( x - x _ { k } ) .
$$

Then (5.3) becomes the elementary but extremely important identity

$$
\ell _ { j } ( x ) = \frac { \ell ( x ) } { \ell ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) } .
$$

(We shall use this equation to derive the Hermite integral formula in Chapter 11.) Equivalently, let us define

$$
\lambda _ { j } = { \frac { 1 } { \prod _ { k \neq j } ( x _ { j } - x _ { k } ) } } ,
$$

that is,

$$
\lambda _ { j } = { \frac { 1 } { \ell ^ { \prime } ( x _ { j } ) } } .
$$

Then (5.3) becomes

$$
\ell _ { j } ( x ) = \ell ( x ) \frac { \lambda _ { j } } { x - x _ { j } } ,
$$

and the Lagrange formula (5.1) becomes

$$
p ( x ) = \ell ( x ) \sum _ { j = 0 } ^ { n } { \frac { \lambda _ { j } } { x - x _ { j } } } f _ { j } .
$$

These formulas were derived by Jacobi in his PhD thesis in Berlin [Jacobi 1825], and they appeared in 19th century textbooks.3

Equation (5.9) has been called the “modified Lagrange formula” (by Higham) and the “first form of the barycentric interpolation formula” or the “type 1 barycentric formula” (starting with Rutishauser). What is valuable here is that the dependence on $x$ inside the sum is so simple. If the weights $\{ \lambda _ { j } \}$ are known, (5.9) produces each value $p ( x )$ with just $O ( n )$ operations. Computing the weights from (5.6) requires $O ( n ^ { 2 } )$ operations, but this computation only needs to be done once and for all, independently of $_ { x }$ ; and for special grids $\{ x _ { j } \}$ such as Chebyshev, as we shall see in a moment, the weights are known analytically and don’t need to be computed at all. (For Legendre and other grids associated with orthogonal polynomials, the necessary computations can be carried out very fast; see Exercise 5.11 and Theorem 19.6.)

However, there is another barycentric formula that is more elegant. If we add up all the Lagrange polynomials $\ell _ { j }$ , we get a polynomial in $\mathcal { P } _ { n }$ that takes the value 1 at every point of the grid. Since polynomial interpolants are unique, this must be the constant polynomial 1:

$$
\sum _ { j = 0 } ^ { n } \ell _ { j } ( x ) = 1 .
$$

Dividing (5.8) by this expression enables us to cancel the factor $\ell ( x )$ , giving

$$
\ell _ { j } ( x ) = { \frac { \lambda _ { j } } { x - x _ { j } } } \left/ \sum _ { k = 0 } ^ { n } { \frac { \lambda _ { k } } { x - x _ { k } } } \right. .
$$

By inserting these representations in (5.1), we get the “second form of the barycentric interpolation formula” or “true barycentric formula” for polynomial interpolation in an arbitrary set of $n + 1$ points $\{ x _ { j } \}$ .

Theorem 5.1. Barycentric interpolation formula. The polynomial interpolant through data $\{ f _ { j } \}$ at $n + 1$ points $\{ x _ { j } \}$ is given by

$$
p ( x ) = \sum _ { j = 0 } ^ { n } \frac { \lambda _ { j } f _ { j } } { x - x _ { j } } \Bigg / \sum _ { j = 0 } ^ { n } \frac { \lambda _ { j } } { x - x _ { j } } ,
$$

with the special case $p ( x ) = f _ { j }$ if $x = x _ { j }$ for some $j$ , where the weights $\{ \lambda _ { j } \}$ are defined by

$$
\lambda _ { j } = { \frac { 1 } { \prod _ { k \neq j } ( x _ { j } - x _ { k } ) } } .
$$

Proof. The proof is given in the discussion above.

It is obvious that the function defined by (5.11) interpolates the data. As $x$ approaches one of the values $x _ { j }$ , one term in the numerator blows up and so does one term in the denominator. Their ratio is $f _ { j }$ , so this is clearly the value approached as $x$ approaches $x _ { j }$ . On the other hand, if $x$ is equal to $x _ { j }$ , we can’t use the formula: that would be a division of $\infty$ by $\infty$ . This is why the theorem is stated with the qualification for the special case $x = x _ { j }$ .

What is not obvious is that the function defined by (5.11) is a polynomial, let alone a polynomial of degree $n$ : it looks like a rational function. The fact that it is a polynomial depends on the special values (5.12) of the weights. For choices of nonzero weights that differ from (5.12), (5.11) will still interpolate the data, but in general it will be a rational function that is not a polynomial. (These rational barycentric interpolants can be very useful [Berrut, Baltensperger & Mittelmann 2005, Tee & Trefethen 2006, Floater & Hormann 2007, Berrut, Floater & Klein 2011] and form the basis of a general method for rational approximation known as the AAA algorithm [Nakatsukasa, S\`ete & Trefethen 2018].)

The Chebfun overload of the MATLAB interp1 command, which was illustrated at the beginning of this chapter, incorporates an implementation of (5.11)–(5.12). We shall make use of interp1 again in Exercise 5.7 and in Chapters 13 and 15. Now, however, let us turn to the special case that is so important in practice.

For Chebyshev points, the weights $\{ \lambda _ { j } \}$ are wonderfully simple: they are equal to $( - 1 ) ^ { j }$ times the constant $2 ^ { n - 1 } / n$ , or half this value for $j = 0$ and $n$ . These numbers were worked out by Marcel Riesz in 1916 [Riesz 1916]. The constant cancels in the numerator and denominator when we divide by the formula for $^ { 1 }$ in (5.11), giving Salzer’s amazingly simple result from 1972 [Salzer 1972].

Theorem 5.2. Barycentric interpolation in Chebyshev points. The polynomial interpolant through data $\{ f _ { j } \}$ at the Chebyshev points (2.2) is

$$
p ( x ) = { \sum _ { j = 0 } ^ { n } } ^ { \prime } { \frac { ( - 1 ) ^ { j } f _ { j } } { x - x _ { j } } } \Bigg / { \sum _ { j = 0 } ^ { n } } ^ { \prime } { \frac { ( - 1 ) ^ { j } } { x - x _ { j } } } ,
$$

with the special case $p ( x ) = f _ { j }$ if $\boldsymbol { x } ~ = ~ x _ { j }$ . The primes on the summation signs signify that the terms $j = 0$ and $j = n$ are multiplied by $1 / 2$ .

Equation (5.13) is scale-invariant: for interpolation in Chebyshev points scaled to any interval $[ a , b ]$ , the formula is exactly the same. This is a big advantage on the computer when $n$ is in the thousands or higher, because it means that we need not worry about underflow or overflow.

Proof. Equation (5.13) is a special case of (5.11). To prove it, we will show that for Chebyshev points, the weights (5.12) reduce to $( - 1 ) ^ { j }$ times the constant $2 ^ { n - 1 } / n$ , and half this value for $j = 0$ or $n$ . To do this, we begin by noting that for Chebyshev points, the node polynomial (5.4) can be written as $\ell ( x ) = 2 ^ { - n } ( T _ { n + 1 } ( x ) - T _ { n - 1 } ( x ) )$ (Exercise 4.1). Together with (5.8), this implies

$$
\ell _ { j } ( x ) = 2 ^ { - n } \lambda _ { j } { \frac { T _ { n + 1 } ( x ) - T _ { n - 1 } ( x ) } { x - x _ { j } } } ,
$$

and from (5.7) we have

$$
\lambda _ { j } = { \frac { 1 } { \ell ^ { \prime } ( x _ { j } ) } } = { \frac { 2 ^ { n } } { T _ { n + 1 } ^ { \prime } ( x _ { j } ) - T _ { n - 1 } ^ { \prime } ( x _ { j } ) } } .
$$

Now it can be shown that

$$
T _ { n + 1 } ^ { \prime } ( x _ { j } ) - T _ { n - 1 } ^ { \prime } ( x _ { j } ) = 2 n ( - 1 ) ^ { j } , \quad 1 \leq j \leq n - 1 ,
$$

with twice this value for $j = 0$ and $n$ (Exercise 5.3). So we have

$$
\lambda _ { j } = \frac { 2 ^ { n - 1 } } { n } ( - 1 ) ^ { j } , \quad 1 \leq j \leq n - 1 ,
$$

with half this value for $j = 0$ and $n$ , as claimed.

The formula (5.13) is extraordinarily effective, even if $n$ is in the thousands or millions, and even if $p$ must be evaluated at thousands or millions of points. As a first example, let us construct a rather wiggly chebfun:

x = chebfun('x'); f = tanh(20\*sin(12\*x)) + .02\*exp(3\*x)\*sin(300\*x); length(f)

We now plot f using 10000 sample points and note the time required:

xx $=$ linspace(-1,1,1e4); tic, plot(xx,f(xx)), toc

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/3aa6a6a4ea6eade5aa8567f1ac4f1a523d15359d4782f62c7b80e1e66c729cb2.jpg)

In this short time, Chebfun has evaluated a polynomial interpolant of degree about 5000 at 10000 sample points.

Raising the degree further, let $p$ be the Chebyshev interpolant of degree $1 0 ^ { 6 }$ to the function $\sin ( 1 0 ^ { 5 } x )$ on $[ - 1 , 1 ]$ :

$$
\begin{array} { r } { \textbf { f f } = \textbf { \textsf { Q } } ( \textbf { x } ) \ \sin \left( 1 \mathrm { e } 5 * \mathrm { x } \right) ; \mathrm { ~ p ~ = ~ c h e b f u n } \left( \mathrm { f f } , 1 0 0 0 0 0 1 \right) ; } \end{array}
$$

How long does it take to evaluate this interpolant at 100 points?

xx = linspace(0,0.0001); tic, pp = p(xx); toc

Elapsed time is 0.237103 seconds.

Not bad for a million-degree polynomial! The result looks fine, plot(xx,pp,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/11381c55506928be74d84be9a15384993956419a8d7cb81123ab61e96e95021f.jpg)

and it matches the target function closely:

for ${ \mathrm { ~ j ~ } } = ~ 1 : 5$ , r = rand; disp([ff(r) p(r) ff(r)-p(r)]), end

0.705930356624765 0.705930356617951 0.000000000006814   
-0.931512002954607 -0.931512002958003 0.000000000003395   
0.583585101736752 0.583585101743138 -0.000000000006386   
-0.851482366899905 -0.851482366903565 0.000000000003660   
0.988082673530624 0.988082673532397 -0.000000000001773

The apparent loss of 4 or 5 digits of accuracy is to be expected since the derivative of this function is of order $1 0 ^ { 5 }$ : each evaluation is the correct result for a value of $x$ within about $1 0 ^ { - 1 6 }$ of the correct one (Exercise 5.5).

Experiments like these show that barycentric interpolation in Chebyshev points is a robust process: it is numerically stable, untroubled by rounding errors on a computer. This may seem surprising if you look at (5.9) or (5.13)—shouldn’t cancellation errors on a computer cause trouble if $x$ is close to one of the Chebyshev points $x _ { j }$ ? In fact they do not, and these formulas have been proved stable in floating point arithmetic for all $x \in [ - 1 , 1 ]$ [Rack $\&$ Reimer 1982, Higham 2004]. This is in marked contrast to the more familiar algorithm of polynomial interpolation via solution of a Vandermonde linear system of equations, which is exponentially unstable (Exercise 5.2).

We must emphasize that whereas (5.13) is stable for interpolation, it is unstable for extrapolation, that is, the evaluation of $p ( x )$ for $x \not \in [ - 1 , 1 ]$ . The more general formula (5.11) is unstable for extrapolation too and is unstable even for interpolation when used with arbitrary points rather than points suitably clustered like Chebyshev points. In these cases it is important to use the “type $1 ^ { \mathfrak { s } }$ barycentric formula (5.9) instead, which Higham proved stable in all cases. The disadvantage of (5.9) is that when $n$ is larger than about a thousand, it is susceptible to troubles of underflow or overflow, which must be countered by rescaling $[ - 1 , 1 ]$ to $[ - 2 , 2 ]$ or by computing products by addition of logarithms.

More precisely, Higham [2004] showed that when they are used to evaluate $p ( x )$ for $x \in \left[ { - 1 , 1 } \right]$ with data at Chebyshev points, both (5.9) and (5.11)–(5.13) have a certain property that numerical analysts call forward stability. If you want to evaluate $p ( x )$ for values of $x$ outside $[ - 1 , 1 ]$ , however, (5.11)–(5.13) lose their stability and it is important to use (5.9), which has the stronger property known as backward stability [Webb, Trefethen $\&$ Gonnet 2012]. It is also important to use (5.9) rather than (5.11) for computing interpolants through equispaced points or other point sets that are far from the Chebyshev distribution. (As we shall discuss in Chapters 13–14, in these cases the problem is probably so ill-conditioned that one should not be doing polynomial interpolation in the first place.)

These observations show that (5.9) has advantages over (5.11) and (5.13), but it also has an important disadvantage: it is not scale-invariant, and the weights grow exponentially as functions of the inverse of the length of the interval of interpolation. We see this in (5.14), where the weights have size $2 ^ { n }$ and would in fact overflow on a computer in standard IEEE double precision arithmetic for $n$ bigger than about 1000. (Higham’s analysis ignores overflow and underflow.) We shall have more to say about this exponential dependence in Chapters 11–15. So (5.11) and (5.13) remain a good choice for most applications, so long as the interpolation points are Chebyshev or similar and the evaluation points lie in $[ - 1 , 1 ]$ .

Summary of Chapter 5. Polynomial interpolants can be evaluated quickly and stably by the barycentric formula, even for thousands or millions of interpolation points. The barycentric formula has the form of a rational function but reduces to a polynomial because of the use of specially determined weights.

Exercise 5.1. Barycentric coefficients by hand. (a) Work out on paper the barycentric interpolation coefficients $\{ \lambda _ { j } \}$ for the case $n = 3$ and $x _ { 0 } = - 1$ , $x _ { 1 } = 0$ , $x _ { 2 } = 1 / 2$ , $x _ { 3 } = 1$ . (b) Confirm that (5.9) gives the right value $p ( - 1 / 2 )$ for the polynomial interpolant to data $1 , 2 , 3 , 4$ in these points.

Exercise 5.2. Instability of Vandermonde interpolation. The best-known numerical algorithm for polynomial interpolation, unlike the barycentric formula, is unstable. This is the method implemented in the MATLAB polyfit command, which forms a Vandermonde matrix of sampled powers of $x$ and solves a corresponding linear system of equations. (In [Trefethen 2000], to my embarrassment, this unstable method is used throughout, forcing the values of $n$ used for plots in that book to be kept small.) (a) Explore this instability by comparing a Chebfun evaluation of $p ( 0 )$ with the result of polyval(polyfit $( \mathbf { x } \mathbf { x } , \mathbf { f } ( \mathbf { x } \mathbf { x } ) , \mathbf { n } ) , 0 )$ , where f $\mathbf { \beta } = \mathbf { \beta } \Theta ( \mathbf { x } ) \cos \left( \mathbf { k } { * } \mathbf { x } \right)$ for $k = 1 0 , 2 0 , \ldots , 9 0 , 1 0 0$ , $_ n$ is the degree of the corresponding chebfun, and $\tt x x$ is a fine grid. (b) Examining the MATLAB polyfit code as appropriate, construct the Vandermonde matrices $V$ for each of these 10 problems and compute their condition numbers. (You can also use the MATLAB vander command.) By contrast, the underlying Chebyshev interpolation problem is wellconditioned.

Exercise 5.3. Calculating derivatives for the proof of Theorem 5.2. Derive the following identities used in the proof of Theorem 5.2. (a) For $1 \leq j \leq n - 1$ , $T _ { n + 1 } ^ { \prime } ( x _ { j } ) \textrm { - }$ $T _ { n - 1 } ^ { \prime } ( x _ { j } ) = 2 n ( - 1 ) ^ { j }$ . (b) For $j = 0$ and $j = n$ , $T _ { n + 1 } ^ { \prime } ( x _ { j } ) - T _ { n - 1 } ^ { \prime } ( x _ { j } ) = 4 n ( - 1 ) ^ { j }$ . One can derive this formula directly, or indirectly by a symmetry argument.

Exercise 5.4. Interpolating the sign function. Use $\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun $( \because { \tt x } ^ { \prime } )$ , $\textbf { f } = \mathtt { s i g n } ( \mathtt { x } )$ to construct the sign function on $[ - 1 , 1 ]$ and ${ \tt p } = { \tt { \tau } }$ chebfun('sign(x)',10000) to construct its interpolant in 10000 Chebyshev points. Explore the difference in the interesting region by defining $\mathsf { d } = \mathsf { f } - \mathsf { p }$ , $\texttt { d } = \texttt { d } \{ - 0 . 0 0 2 , 0 . 0 0 2 \}$ . What is the maximum value of p? In what subset of $[ - 1 , 1 ]$ is p smaller than 0.5 in absolute value?

Exercise 5.5. Accuracy of point evaluations. (a) Construct the chebfun $g$ corresponding to $f ( x ) = \sin ( \exp ( 1 0 x ) )$ on $[ - 1 , 1 ]$ . What is the degree of this polynomial? (b) Let $\tt x x$ be the vector of 1000 linearly spaced points from $^ { - 1 }$ to 1. How long does it take on your computer to evaluate $f ( \mathbf { x x } )$ ? $g ( \mathbf { x x } ) \acute { : }$ ? (c) Draw a loglog plot of the vector of errors $| f ( \mathbf { x x } ) - g ( \mathbf { x x } ) |$ against the vector of derivatives $\left| f ^ { \prime } ( \tt x x ) \right|$ . Comment on why the dots line up as they do.

Exercise 5.6. Equispaced points. Show that for equispaced points in $[ - 1 , 1 ]$ with spacing $h$ , the barycentric weights are $\lambda _ { j } = ( - 1 ) ^ { n - j } / ( j ! ( n - j ) ! h ^ { n } )$ , or equivalently, after canceling common factors in the numerator and denominator of (5.11), $\lambda _ { j } = ( - 1 ) ^ { j } { \binom { n } { j } }$ [Taylor 1945].

Exercise 5.7. A greedy algorithm for choosing interpolation grids. Write a program using the Chebfun interp1 command to compute a sequence of polynomial interpolants to a function $f$ on $[ - 1 , 1 ]$ in points selected by a greedy algorithm: take $x _ { 0 }$ t o be a point where $| f ( x ) |$ achieves its maximum, then $x _ { 1 }$ to be a point where $| ( f - p _ { 0 } ) ( x ) |$ achieves its maximum, then $x _ { 2 }$ to be a point where $| ( f - p _ { 1 } ) ( x ) |$ achieves its maximum, and so on. Plot the error curves $( f - p _ { n } ) ( x )$ , $x \in [ - 1 , 1 ]$ , computed by this algorithm for $f ( x ) = \left| x \right|$ and $0 \leq n \leq 2 5$ . Comment on the spacing of the grid $\{ x _ { 0 } , \ldots , x _ { 2 5 } \}$ .

Exercise 5.8. Barycentric formula for Chebyshev polynomials. Derive an elegant formula for $T _ { n } ( x )$ from (5.13) [Salzer 1972].

Exercise 5.9. Barycentric interpolation in roots of unity. Derive the barycentric weights $\{ \lambda _ { j } \}$ for polynomial interpolation in (a) $\{ \pm 1 \}$ , (b) $\{ 1 , i , - 1 , - i \}$ , and (c) the $( n + 1 ) \mathrm { s t }$ roots of unity for arbitrary $n \geq 0$ .

Exercise 5.10. Barycentric weights for a general interval. (a) How does the formula (5.14) for Chebyshev barycentric weights on $[ - 1 , 1 ]$ change for weights on an interval $[ a , b ]$ ? (b) The capacity of $[ a , b ]$ (see Chapter 12) is equal to $c = ( b - a ) / 4$ . How do the barycentric weights behave as $n \to \infty$ for an interval of capacity $c$ ? As a function of $c$ , what is the maximal value of $n$ for which they can be represented in IEEE double precision arithmetic without overflow or underflow? (You may assume the overflow and underflow limits are $1 0 ^ { 3 0 8 }$ and $1 0 ^ { - 3 0 8 }$ . The overflow/underflow problem goes away with the use of the divided form (5.13).)

Exercise 5.11. Barycentric interpolation in Legendre points. Chebfun includes fast algorithms for computing barycentric weights for various distributions of points other than Chebyshev, such as Legendre points, the zeros of Legendre polynomials (see Chapter 17 and Theorem 19.6). Perform a numerical experiment to compare the accuracy of interpolants in Chebyshev and Legendre points to $f ( x ) = e ^ { x } \sin ( 3 0 0 x )$ at $x = 0 . 9 9$ . Specifically, compute $[ { \bf s } , { \bf w } , \mathrm { { 1 a m b d a } } ] = \mathrm { { 1 e g p t s } } \left( { \bf n + 1 } \right)$ and bary(0.99,f(s),s,lambda) for $1 \leq n \leq 5 0 0$ and make a semilog plot of the absolute value of the error as a function of $n$ ; compare this with the analogous plot for Chebyshev points.

Exercise 5.12. Barycentric rational interpolation. (a) If the formula (5.13) is used with points $\{ x _ { j } \}$ other than Chebyshev with maximum spacing $h$ , it produces a rational interpolant of accuracy $O ( h ^ { 2 } )$ as $h  0$ [Berrut 1988]. Confirm this numerically for $f ( x ) =$ $e ^ { x }$ and equispaced points in $[ - 1 , 1 ]$ . (b) Show numerically that the accuracy improves to $O ( h ^ { 3 } )$ if the pattern of coefficients near the left end is changed from ${ \scriptstyle { \frac { 1 } { 2 } } , - 1 , 1 , - 1 , \dots }$ to ${ \begin{array} { l } { { \frac { 1 } { 4 } } , - { \frac { 3 } { 4 } } , 1 , - 1 , \dots } \end{array} }$ and analogously at the right end [Floater & Hormann 2007].

Exercise 5.13. Barycentric weights and geometric mean distances. (a) Give an interpretation of (5.6) in terms of geometric mean distances between grid points. (b) Show how one of the theorems of this chapter explains the result of Exercise 2.6.

# Chapter 6. Weierstrass Approximation Theorem

Every continuous function on a bounded interval can be approximated to arbitrary accuracy by polynomials. This is the famous Weierstrass approximation theorem, proved by Karl Weierstrass when he was 70 years old [Weierstrass 1885]. The theorem was independently discovered at about the same time, in essence, by Carl Runge: as pointed out in 1886 by Phragm´en in remarks published as a footnote stretching over four pages in a paper by Mittag-Leffler [1900], it can be derived as a corollary of results Runge published in a pair of papers in 1885 [Runge 1885a & 1885b].

Here and throughout this book, unless indicated otherwise, $\| \cdot \|$ denotes the supremum norm on $[ - 1 , 1 ]$ .

Theorem 6.1. Weierstrass approximation theorem. Let $f$ be a continuous function on $[ - 1 , 1 ]$ , and let $\varepsilon > 0$ be arbitrary. Then there exists a polynomial $p$ such that

$$
\| f - p \| < \varepsilon .
$$

Outline of proof. We shall not spell out an argument in detail. However, here is an outline of the beautiful proof from Weierstrass’s original paper. First, extend $f ( x )$ to a continuous function $\tilde { f }$ with compact support on the whole real line. Now, take $\ddot { f }$ as initial data at $t ~ = ~ 0$ for the diffusion equation $\partial u / \partial t = \partial ^ { 2 } u / \partial x ^ { 2 }$ o n the real line. It is known that by convolving $\ddot { f }$ with the Gaussian kernel $\phi ( x ) = $ $e ^ { - x ^ { 2 } / 4 t } / \sqrt { 4 \pi t }$ , we get a solution to this PDE that converges uniformly to $f$ as $t  0$ and thus can be made arbitrarily close to $f$ on $[ - 1 , 1 ]$ by taking $t$ small enough. On the other hand, since $\tilde { f }$ has compact support, for each $t > 0$ this solution is an integral over a bounded interval of entire functions and is thus itself an entire function, that is, analytic throughout the complex plane. Therefore it has a uniformly convergent Taylor series on $[ - 1 , 1 ]$ , which can be truncated to give polynomial approximations of arbitrary accuracy.

For a fuller presentation of the argument just given as “one of the most amusing applications of the Gaussian kernel,” where the result is stated for the more general case of a function of several variables approximated by multivariate polynomials, see [Folland 1995].

Many other proofs of the Weierstrass theorem are also known, including these early ones:

Runge (1885)   
Picard (1891)   
Lerch (1892 and 1903)   
Volterra (1897)   
Lebesgue (1898)   
Mittag-Leffler (1900)   
Fej´er (1900 and 1916)   
Landau (1908)   
de la Vall´ee Poussin (1908)   
Jackson (1911)   
Sierpinski (1911)   
Bernstein (1912)   
Montel (1918)

For example, Bernstein’s proof is a discrete analogue of the argument just given: continuous diffusion is replaced by a random walk made precise by the notion of Bernstein polynomials (Exercise 6.4) [Bernstein 1912d]. Lebesgue’s proof, which appeared in his first paper published as a student at age 23, is based on reducing the approximation of general continuous functions to the approximation of $| x |$ (Exercise 6.5) [Lebesgue 1898]. Fej´er was an even younger student, age 20, when he published his proof based on Ces\`aro means (Exercise 6.6(a)) [Fej´er 1900], and he published a different proof years later based on Hermite–Fej´er interpolation (Exercise 6.6(b)) [Fej´er 1916]. This long list gives an idea of the great amount of mathematics stimulated by Weierstrass’s theorem and the significant role it played in the development of analysis in the early 20th century. For a fascinating presentation of this corner of mathematical history, see [Pinkus 2000].

Weierstrass’s theorem establishes that even extremely nonsmooth functions can be approximated by polynomials, functions like $x \sin ( x ^ { - 1 } )$ or even $\sin ( x ^ { - 1 } ) \sin ( 1 / \sin ( x ^ { - 1 } ) )$ . The latter function has an infinite number of points near which it oscillates infinitely often, as we begin to see from the plot below over the range [0.07, 0.4]. In this calculation Chebfun is called with a user-prescribed number of interpolation points, 30000, since the usual adaptive procedure has no chance of resolving the function to machine precision.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/756be56501e27c15923928c47a67e99435011337960d728fa84e898d2e29cf3a.jpg)

We can illustrate the idea of Weierstrass’s proof by showing the convolution of this complicated function with a Gaussian. First, here is the same function $f$ recomputed over a subinterval extending from one of its zeros to another:

a = 0.2885554757; b = 0.3549060246;   
$\boldsymbol { \tt { f } } 2 { \it { \Delta \phi } } =$ chebfun(@(x) sin(1/x)\*sin(1/sin(1/x)),[a,b],2000); plot(f2)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/3fbf3af31fbdfe1b929c7cdb3f715dd8626a285940e86e5fd70ea1db685ccd3f.jpg)

Here is a narrow Gaussian with integral 1:

$\scriptstyle { \mathrm { ~ t ~ } } = { \mathrm { ~ 1 } } \mathtt { e } - 7$ ;   
phi $=$ chebfun(@(x) exp(-x^2/(4\*t))/sqrt(4\*pi\*t),.003\*[-1 1]); plot(phi)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/3d9de49f557f2dd48979c8d49aa6ab15cfe8fd777d11b57b28e53c0340cadbc4.jpg)

Convolving the two gives a smoothed version of the close-up of $f$ . Notice how the short wavelengths vanish while the long ones are nearly undisturbed.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/7112b59880b548805bd95a1e245b4d6c774f2ccf38e34461aafa0e705afe4b29.jpg)

This is an entire function, which means it can be approximated by polynomials by truncating the Taylor series.

Weierstrass’s theorem has an important generalization to complex analytic functions. Suppose a function $f$ is defined on a compact set $K$ in the complex plane whose complement is connected (so $K$ cannot have any holes). Mergelyan’s theorem asserts that if $f$ is continuous on $K$ and analytic in the interior, then $f$ can be approximated on $K$ by polynomials [Mergelyan 1951, Gaier 1987]. The earlier Runge’s theorem is the weaker result in which $f$ is assumed to be analytic throughout $K$ , not just in the interior [Runge 1885a].

For all its beauty, power, and importance, the Weierstrass approximation theorem has in some respects served as an unfortunate distraction. Knowing that even troublesome functions can be approximated by polynomials, we naturally ask, How can we do it? A famous result of Faber and Bernstein asserts that there is no fixed array of grids of $1 , 2 , 3 , \ldots$ interpolation points, Chebyshev or otherwise, that achieves convergence as $n  \infty$ for all continuous $f$ [Faber 1914, Bernstein 1919]. So it becomes tempting to look at approximation methods that go beyond interpolation, and to warn people that interpolation is dangerous, and to try to characterize exactly what minimal properties of $f$ suffice to ensure that interpolation will work after all. A great deal is known about these subjects. The trouble with this line of research is that for almost all the functions encountered in practice, Chebyshev interpolation works beautifully! Weierstrass’s theorem has encouraged mathematicians over the years to give too much of their attention to pathological functions at the edge of discontinuity, leading to the bizarre and unfortunate situation where many books on numerical analysis caution their readers that interpolation may fail without mentioning that for functions with a little bit of smoothness, it succeeds outstandingly. For discussions of the history of such misrepresentations and misconceptions, see Chapter 14, Appendix A, and [Trefethen 2016].

Summary of Chapter 6. A continuous function on a bounded interval can be approximated arbitrarily closely by polynomials.

Exercise 6.1. A pathological function of Weierstrass. Weierstrass was one of the first to give an example of a function continuous but nowhere differentiable on $[ - 1 , 1 ]$ , and it is one of the early examples of a fractal [Weierstrass 1872]:

$$
w ( x ) = \sum _ { k = 0 } ^ { \infty } 2 ^ { - k } \cos ( 3 ^ { k } x ) .
$$

(a) Construct a chebfun w7 corresponding to this series truncated at $k = 7$ . Plot w7, its derivative (use diff), and its indefinite integral (cumsum). What is the degree of the polynomial defining this chebfun? (b) Prove that $w$ is continuous. (You can use the Weierstrass M-test.)

Exercise 6.2. Taylor series of an entire function. To illustrate the proof of the Weierstrass approximation theorem, we plotted a Gaussian kernel. The key point of the proof is that this kernel is entire, so its Taylor series converges for all $x$ . (a) For $x = 1$ at the given time $t = 1 0 ^ { - 7 }$ , how many terms of the Taylor series about $x = 0$ would you have to take before the terms fall below 1? Estimate the answer at least to within a factor of 2. You may find Stirling’s formula helpful. (b) Also for $x = 1$ and $t = 1 0 ^ { - 7 }$ , approximately how big is the biggest term in the Taylor series?

Exercise 6.3. Resolving a difficult function. Although the example function $f ( x ) = \sin ( 1 / x ) \sin ( 1 / \sin ( 1 / x ) )$ of this chapter is not Lipschitz continuous, its Chebyshev interpolants do in fact converge. Explore this phenomenon numerically by computing the degree $n$ Chebyshev interpolant to $f$ over the interval [0.07, 0.4] for $n + 1 = 4 , 8 , 1 6 , \dots , 2 ^ { 1 4 }$ and measuring the error in each case over a Chebyshev grid of $2 n$ points. Plot the results on a loglog scale. How do you think the error depends on $_ n$ as $n \to \infty$ ? Approximately how large would $_ n$ have to be to get 16-digit accuracy for this function over this interval?

Exercise 6.4. Bernstein’s proof. For $f \in C ( [ 0 , 1 ] )$ , the associated degree $_ n$ Bernstein polynomial is defined by

$$
B _ { n } ( x ) = \sum _ { k = 0 } ^ { n } f ( k / n ) { \binom { n } { k } } x ^ { k } ( 1 - x ) ^ { n - k } .
$$

Bernstein proved the Weierstrass approximation theorem by showing that $B _ { n } ( x )  f ( x )$ uniformly as $n \to \infty$ . (a) Give an interpretation of $B _ { n } ( x )$ involving a random walk driven by a coin which comes up heads with probability $_ x$ and tails with probability ${ \mathrm { ~ 1 ~ - ~ } } x$ . (b) Show that max $B _ { n } ( x ) \leq \operatorname* { m a x } f ( x )$ and $\operatorname* { m i n } B _ { n } ( x ) \geq \operatorname* { m i n } f ( x )$ for $x \in [ 0 , 1 ]$ .

Exercise 6.5. Lebesgue’s proof. (a) Show using uniform continuity that any $f \in$ $C ( [ - 1 , 1 ] )$ can be approximated uniformly by a polygonal curve, i.e., a function $g ( x )$ that is piecewise linear and continuous. (b) Show that such a function can be written in the form $\begin{array} { r } { g ( x ) = A + B x + \sum _ { k = 1 } ^ { m } C _ { k } | x - x _ { k } | } \end{array}$ . (c) Show that $| x |$ can be uniformly approximated by polynomials on $\lfloor - 1 , 1 \rfloor$ by truncating the binomial expansion

$$
| x | = [ 1 + ( x ^ { 2 } - 1 ) ] ^ { 1 / 2 } = \sum _ { n = 0 } ^ { \infty } { \binom { \frac { 1 } { 2 } } { n } } ( x ^ { 2 } - 1 ) ^ { n } .
$$

You may use without proof the fact that these binomial coefficients are of size $O ( n ^ { - 3 / 2 } )$ as $n \to \infty$ . (d) Explain how (a)–(c) combine to give a proof of the Weierstrass approximation theorem.

Exercise 6.6. Fej´er’s proofs. (a) In 1900 Fej´er proved the Weierstrass approximation theorem via Ces\`aro means. In the Chebyshev case, define $S _ { n }$ to be the mean of the partial sums of the Chebyshev series (3.11)–(3.12) of orders 0 through $n$ . Then it can be shown that $S _ { n } \ \to \ f$ uniformly as $n  \infty$ for any $f \in C ( [ - 1 , 1 ] )$ . Explore such approximations for $f ( x ) = e ^ { x }$ with various degrees $n$ . For this very smooth function $f$ , how does the accuracy compare with that of ordinary Chebyshev interpolants? (b) In 1916 Fej´er proved the theorem again by considering what are now known as Hermite–Fej´er interpolants: he showed that if $p _ { 2 n - 1 } \in \mathcal { P } _ { 2 n - 1 }$ is obtained by interpolating $f \in C ( [ - 1 , 1 ] )$ in the zeros of $T _ { n } ( x )$ and also setting $p ^ { \prime } ( x ) = 0$ at these points, then $p _ { 2 n - 1 } \to f$ uniformly as $n  \infty$ . Explore such interpolants numerically for various $n$ by using interp1 to construct polynomials $p 2 n - 1$ with $p _ { 2 n - 1 } ( x _ { j } ) = p _ { 2 n - 1 } ( x _ { j } + 1 0 ^ { - 6 } ) = \exp ( x _ { j } )$ . Again how does the accuracy compare with that of ordinary Chebyshev interpolants?

Exercise 6.7. Convergent series of polynomials. (a) Show that any $f \in C ( [ - 1 , 1 ] )$ ) can be written as a uniformly convergent series

$$
f ( \boldsymbol { x } ) = \sum _ { k = 0 } ^ { \infty } q _ { k } ( \boldsymbol { x } ) ,
$$

where each $q _ { k }$ is a polynomial of some degree. (b) Show that a series of this kind also exists for a function continuous on the whole real line, with pointwise convergence for all $_ x$ and uniform convergence on any bounded subset.

# Chapter 7. Convergence for Differentiable Functions

The principle mentioned at the end of the last chapter might be regarded as the central dogma of approximation theory: the smoother a function, the faster its approximants converge as $n  \infty$ . Connections of this kind were explored in the early years of the 20th century by three of the founders of approximation theory: Charles de la Vall´ee Poussin (1866–1962), a mathematician at Leuven in Belgium, Sergei Bernstein (1880–1968), a Ukrainian mathematician who had studied with Hilbert in G¨ottingen, and Dunham Jackson (1888–1946), an American student of Landau’s also at G¨ottingen. (Henri Lebesgue in France (1875–1941) also proved some of the early results. For remarks on the history see [Goncharov 2000] and [Steffens 2006].) Bernstein made the following comment concerning best approximation errors $E _ { n } ( f ) = \| f - p _ { n } ^ { * } \| _ { \infty }$ (see Chapter 10) in his summary article for the International Congress of Mathematicians in 1912 [Bernstein 1912a]:

The general fact that emerges from this study is the existence of a most intimate connection between the differential properties of the function $f ( x )$ and the asymptotic rate of decrease of the positive numbers $E _ { n } [ f ( x ) ]$ .4

In this and the next chapter our aim is to make the smoothness–approximability link precise in the context of Chebyshev projections and interpolants. Everything here is analogous to results for Fourier analysis of periodic functions, and indeed, the whole theory of Chebyshev interpolation can be regarded as a transplant to nonperiodic functions on $[ - 1 , 1 ]$ of the theory of trigonometric interpolation of periodic functions on $[ - \pi , \pi ]$ .

Suppose a function $f$ is $\nu$ times differentiable on $[ - 1 , 1 ]$ , possibly with jumps in the $\nu$ th derivative, and suppose you look at the convergence of its Chebyshev interpolants as $n \to \infty$ , measuring the error in the $\infty$ -norm. You will typically see convergence at the rate $O ( n ^ { - \nu } )$ . We can explore this effect readily with Chebfun. For example, the function $f ( x ) = \left| x \right|$ is once differentiable with a jump in the first derivative at $x = 0$ , and the convergence curve nicely matches $n ^ { - 1 }$ (shown as a straight line). Actually the match is more than just nice in this case—it is exact, with $p _ { n }$ taking its maximal error at the value $p ( 0 ) = 1 / n$ for odd $n$ . (For even $n$ the error is somewhat smaller.)

$\mathbf { x } ~ = ~ \mathrm { c h e b f u n } ( \mathbf { \Sigma } ^ { \prime } \mathbf { x } ^ { \prime } ) ; ~ \mathbf { f } ~ = ~ \mathsf { a b s } ( \mathbf { x } ) ; ~ \mathbf { n } \mathbf { n } ~ = ~ 2 * \mathbf { r o u n d } ( 2 . \hat { ~ } ( 0 : . 3 : 7 ) ) - 1 ;$ $\mathtt { e e } \ = \ 0 * \mathtt { n n }$ ;   
for $\begin{array} { r l } & { \mathrm { \bf ~ j ~ = ~ 1 : \mathrm { l e n g t h } ( n n ) } } \\ & { \mathrm { \bf ~ n ~ = ~ n n ( j ) ; ~ \mathrm { \bf ~ f } n ~ = ~ \mathrm { c h e b f u n } ( f , n + 1 ) ; ~ \mathrm { \bf ~ e e ( j ) ~ = ~ \mathrm { n o r m } ( f - f n , i n f ) ; } } } \end{array}$ end   
$\mathtt { l o g l o g ( n n , 1 . / n n , ' r " ) }$ , hold on, loglog(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/0732e20948736cab1a0a6e41228ed0e34dd06745bbfda041344b6d8922ad2135.jpg)

Similarly, we get cubic convergence for

$$
f ( x ) = | \sin ( 5 x ) | ^ { 3 } ,
$$

which is three times differentiable with jumps in the third derivative at $x = 0$ and $\pm \pi / 5$ .

fo $\begin{array} { r l } { \mathbf { \Psi } } & { \mathbf { \beth } = \mathbf { \beth } \mathbf { b } \mathbf { s } \left( \mathbf { \beth } \mathbf { \beth } ( \mathbf { \beth } \mathbf { \beth } \mathbf { \beth } ) \right) \mathbf { \beth } \mathbf { \beth } \mathbf { \ b } ; } \\ { \mathbf { \beth } } & { \mathbf { \ b j } ~ = ~ \mathbf { \ b { 1 } } : \mathbf { \ b { 1 } } \mathbf { } \mathbf { e n g t h } \left( \mathbf { n n } \right) } \\ & { \mathbf { \ b n } ~ = ~ \mathbf { \ b { n } } \mathbf { n } ( \mathbf { j } ) \colon \mathbf { \ b j } ~ \mathbf { \ b n } ~ = ~ \mathbf { \ b { c h e b f u n } } ( \mathbf { f } , \mathbf { n } + \mathbf { 1 } ) ; ~ \mathbf { \ b e } \mathbf { e } \left( \mathbf { j } \right) ~ = ~ \mathbf { \ b n o r m } \left( \mathbf { f } - \mathbf { f } \mathbf { n } , \mathbf { i } \mathbf { n } \mathbf { f } \right) ; } \end{array}$ end $\mathtt { l o g l o g ( n n , n n . \hat { \mu } ^ { - } 3 , \mu ^ { \prime } r ^ { \prime } ) }$ , hold on, loglog(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/9fc66b531bba634f0249beabcffc6d0907ed446aac9bcf64db6037c22f21f12e.jpg)

Encouraged by such experiments, you might look in a book to try to find theorems about $O ( n ^ { - \nu } )$ . If you do, you’ll run into two difficulties. First, it’s hard to find theorems about Chebyshev interpolants, for most of the literature is about other approximations such as best approximations (see Chapters 10 and 16) or interpolants in Chebyshev polynomial roots rather than extrema. Second, you will probably fall one power of $n$ short! In particular, the most commonly quoted of the Jackson theorems asserts that if $f$ is $\nu$ times continuously differentiable on $[ - 1 , 1 ]$ , then its best polynomial approximations converge at the rate $O ( n ^ { - \nu } )$ [Jackson 1911; Cheney 1966, Sect. 4.6]. But the first and third derivatives of the functions we just looked at, respectively, are not continuous. Thus we must settle for the zeroth and second derivatives, respectively, if we insist on continuity, so this theorem would ensure only $O ( n ^ { 0 } )$ and $O ( n ^ { - 2 } )$ convergence, not the $O ( n ^ { - 1 } )$ and $O ( n ^ { - 3 } )$ that are actually observed. And it would apply to best approximations, not Chebyshev interpolants.

We can get the result we want by recognizing that most functions encountered in applications have a property that is not assumed in the theorems just mentioned: bounded variation. A function, whether continuous or not, has bounded variation if its total variation is finite. The total variation is the 1-norm of the derivative (as defined if necessary in the distributional sense; see [Ziemer 1989, Chap. 5] or [Evans & Gariepy 1991, Sect. 5.10]). We can compute this number conveniently with Chebfun by writing a function called tv that evaluates $\| f ^ { \prime } \| _ { 1 }$ for a given function $f$ :

tv = @(f) norm(diff(f),1);

Here are the total variations of $x$ and $\sin ( 1 0 \pi x )$ over $[ - 1 , 1 ]$ :

disp([tv(x) tv(sin(10\*pi\*x))])

2.000000000000000 40.000000000000007

Here is the total variation of the derivative of $| x |$ :

tv(diff(abs(x)))

Here is the total variation of the third derivative of the function $f$ of (7.1):

ans = 2.102783663403057e+04

It is the finiteness of this number that allowed the Chebyshev interpolants to this function $f$ to converge at the rate $O ( n ^ { - 3 } )$ .

To get to a precise theorem, we begin with a bound on Chebyshev coefficients, an improvement (in the definition of the quantity $V$ ) of a similar result in [Trefethen 2008] whose proof was provided by Endre S¨uli. The condition of absolute continuity is a standard one which we shall not make detailed use of, so we will not discuss it. An absolutely continuous function is equal to the integral of its derivative, which exists almost everywhere and is Lebesgue integrable.

Theorem 7.1. Chebyshev coefficients of differentiable functions. For an integer $\nu \geq 0$ , let $f$ and its derivatives through $f ^ { ( \nu - 1 ) }$ be absolutely continuous on $[ - 1 , 1 ]$ and suppose the νth derivative $f ^ { ( \nu ) }$ is of bounded variation $V$ . Then for $k \geq \nu + 1$ , the Chebyshev coefficients of $f$ satisfy

$$
| a _ { k } | \leq { \frac { 2 V } { \pi k ( k - 1 ) \cdots ( k - \nu ) } } \leq { \frac { 2 V } { \pi ( k - \nu ) ^ { \nu + 1 } } } .
$$

Proof. As in the proof of Theorem 3.1, setting $x = { \textstyle { \frac { 1 } { 2 } } } ( z + z ^ { - 1 } )$ with $z$ on the unit circle gives

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { | z | = 1 } f ( { \frac { 1 } { 2 } } ( z + z ^ { - 1 } ) ) z ^ { k - 1 } d z ,
$$

and integrating by parts with respect to $z$ converts this to

$$
a _ { k } = { \frac { - 1 } { \pi i } } \int _ { | z | = 1 } f ^ { \prime } ( { \textstyle { \frac { 1 } { 2 } } } ( z + z ^ { - 1 } ) ) { \frac { z ^ { k } } { k } } { \frac { d x } { d z } } d z ;
$$

the factor $d x / d z$ appears since $f ^ { \prime }$ denotes the derivative with respect to $x$ rather than $z$ . Suppose now $\nu = 0$ , so that all we are assuming about $f$ is that it is of bounded variation $V = \| f ^ { \prime } \| _ { 1 }$ . Then we note that this integral over the upper half of the unit circle is equivalent to an integral in $x$ ; the integral over the lower half gives another such integral. Combining the two gives

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { - 1 } ^ { 1 } f ^ { \prime } ( x ) { \frac { z ^ { k } - z ^ { - k } } { k } } d x = { \frac { 2 } { \pi } } \int _ { - 1 } ^ { 1 } f ^ { \prime } ( x ) \operatorname { I m } { \frac { z ^ { k } } { k } } d x ,
$$

and since $| z ^ { k } / k | \leq 1 / k$ for $x \in [ - 1 , 1 ]$ and $V = \| f ^ { \prime } \| _ { 1 }$ , this implies $| a _ { k } | \leq 2 V / \pi k$ , as claimed.

If $\nu > 0$ , we replace $d x / d z$ by $\scriptstyle { \frac { 1 } { 2 } } \left( 1 - z ^ { - 2 } \right)$ in (7.3), obtaining

$$
a _ { k } = - { \frac { 1 } { \pi i } } \int _ { | z | = 1 } f ^ { \prime } ( { \frac { 1 } { 2 } } ( z + z ^ { - 1 } ) ) \left[ { \frac { z ^ { k } } { 2 k } } - { \frac { z ^ { k - 2 } } { 2 k } } \right] d z .
$$

Integrating by parts again with respect to $z$ converts this to

$$
a _ { k } = \frac { 1 } { \pi i } \int _ { | z | = 1 } f ^ { \prime \prime } ( \frac { 1 } { 2 } ( z + z ^ { - 1 } ) ) \left[ \frac { z ^ { k + 1 } } { 2 k ( k + 1 ) } - \frac { z ^ { k - 1 } } { 2 k ( k - 1 ) } \right] \frac { d x } { d z } d z .
$$

Suppose now $\nu = 1$ so that we are assuming $f ^ { \prime }$ has bounded variation $V = \| f ^ { \prime \prime } \| _ { 1 }$ Then again this integral is equivalent to an integral in $x$ ,

$$
a _ { k } = { \frac { - 2 } { \pi } } \int _ { - 1 } ^ { 1 } f ^ { \prime \prime } ( x ) \operatorname { I m } \left[ { \frac { z ^ { k + 1 } } { 2 k ( k + 1 ) } } - { \frac { z ^ { k - 1 } } { 2 k ( k - 1 ) } } \right] d x .
$$

Since the term in square brackets is bounded by $1 / k ( k - 1 )$ for $x \in \left[ - 1 , 1 \right]$ and $V = \| f ^ { \prime \prime } \| _ { 1 }$ , this implies $| a _ { k } | \leq 2 V / \pi k ( k - 1 )$ , as claimed.

If $\nu > 1$ , we continue in this fashion with a total of $\nu + 1$ integrations by parts with respect to $z$ , in each case first replacing $d x / d z$ by $\scriptstyle { \frac { 1 } { 2 } } \left( 1 - z ^ { - 2 } \right)$ . At the next step the term that appears in square brackets is

$$
\left[ \frac { z ^ { k + 2 } } { 4 k ( k + 1 ) ( k + 2 ) } - \frac { z ^ { k } } { 4 k ^ { 2 } ( k + 1 ) } - \frac { z ^ { k } } { 4 k ^ { 2 } ( k - 1 ) } + \frac { z ^ { k - 2 } } { 4 k ( k - 1 ) ( k - 2 ) } \right] ,
$$

which is bounded by $1 / k ( k - 1 ) ( k - 2 )$ for $x \in [ - 1 , 1 ]$ . And so on.

From Theorems 3.1 and 7.1 we can derive consequences about the accuracy of Chebyshev projections and interpolants. Variations on the estimate (7.5) can be found as Corollary 2 of [Mastroianni & Szabados 1995] and Theorem 2 of [Mastroianni & Russo 2010]. The analogous result for best approximations as opposed to Chebyshev interpolants or projections was announced in [Bernstein 1911] and proved in [Bernstein 1912b].

Theorem 7.2. Convergence for differentiable functions. If $f$ satisfies the conditions of Theorem 7.1, with $V$ again denoting the total variation of $f ^ { ( \nu ) }$ for some $\nu \geq 1$ , then for any $n > \nu$ , its Chebyshev projections satisfy

$$
\| f - f _ { n } \| \leq \frac { 2 V } { \pi \nu ( n - \nu ) ^ { \nu } }
$$

and its Chebyshev interpolants satisfy

$$
\| f - p _ { n } \| \leq \frac { 4 V } { \pi \nu ( n - \nu ) ^ { \nu } } .
$$

Proof. For (7.4), Theorem 7.1 applied to (4.8) gives us

$$
\Vert f - f _ { n } \Vert \leq \sum _ { k = n + 1 } ^ { \infty } | a _ { k } | \leq \frac { 2 V } { \pi } \sum _ { k = n + 1 } ^ { \infty } ( k - \nu ) ^ { - \nu - 1 }
$$

and this sum can in turn be bounded by

$$
\int _ { n } ^ { \infty } ( s - \nu ) ^ { - \nu - 1 } d s = { \frac { 1 } { \nu ( n - \nu ) ^ { \nu } } } .
$$

For (7.5), we use (4.9) instead of (4.8) and get the same bound except with coefficients $2 | a _ { k } |$ rather than $\left| a _ { k } \right|$ .

In a nutshell, a $\nu$ th derivative of bounded variation implies convergence at the algebraic rate $O ( n ^ { - \nu } )$ . Here is a way to remember this message. Suppose we try to approximate the step function $\mathrm { s i g n } ( x )$ by polynomials. There is no hope of convergence, since polynomials are continuous and $\mathrm { s i g n } ( x )$ is not, so all we can achieve is accuracy $O ( 1 )$ as $n  \infty$ . That’s the case $\nu = 0$ . But now, each time we make the function “one derivative smoother,” $\nu$ increases by 1 and so does the order of convergence.

How sharp is Theorem 7.2 for our example functions? In the case of $f ( x ) =$ $| x |$ , with $\nu = 1$ and $V \ : = \ : 2$ , it predicts $\| f - f _ { n } \| \leq 4 / \pi ( n - 1 )$ and $\| f - p _ { n } \| \leq$ $8 / \pi ( n - 1 ) \approx 2 . 5 5 / ( n - 1 )$ . As mentioned above, the actual value for Chebyshev interpolation is $\| f - p _ { n } \| = 1 / n$ for odd $n$ . The minimal possible error in polynomial approximation, with $p _ { n }$ replaced by the best approximation $\boldsymbol { p } _ { n } ^ { * }$ (Chapter 10), is $\lVert f - p _ { n } ^ { * } \rVert \sim 0 . 2 8 0 1 6 9 \ldots n ^ { - 1 }$ as $\textit { n } \to \infty$ [Varga $\&$ Carpenter 1985]. So we see that the range from best approximant, to Chebyshev interpolant, to bound on Chebyshev interpolant is less than a factor of 10. The approximation of $| x |$ was a central problem studied by Lebesgue, de la Vall´ee Poussin, Bernstein, and Jackson a century ago (Exercise 6.5), and we shall consider it further in Chapter 25.

The results are similar for the other example, $f ( x ) = | \sin ( 5 x ) | ^ { 3 }$ , whose third derivative, we saw, has variation $V ~ \approx ~ 2 1 0 2 8$ . Equation (7.5) implies that the Chebyshev interpolants satisfy $\| f - p _ { n } \| < 7 0 2 0 / ( n - 1 ) ^ { 3 }$ , whereas in fact we have $\| f - p _ { n } \| \approx 3 0 9 / n ^ { 3 }$ for large odd $n$ and $\| f - p _ { n } ^ { * } \| \approx 8 0 / n ^ { 3 }$ .

We close with a comment about Theorem 7.2. We have assumed in this theorem that $f ^ { ( \nu ) }$ is of bounded variation. A similar but weaker condition would be that $f ^ { ( \nu - 1 ) }$ is Lipschitz continuous (Exercise 7.2). This weaker assumption is enough to ensure $\| f - p _ { n } ^ { * } \| = O ( n ^ { - \nu } )$ for the best approximations $\{ p _ { n } ^ { * } \}$ ; this is one of the Jackson theorems. On the other hand, it is not enough to ensure $O ( n ^ { - \nu } )$ convergence of Chebyshev projections and interpolants. The reason we emphasize the stronger assumption with the stronger conclusion is that in practice, one rarely deals with a function that is Lipschitz continuous while lacking a derivative of bounded variation, whereas one constantly deals with projections and interpolants rather than best approximations.

Incidentally, it was de la Vall´ee Poussin [1908] who first showed that the strong hypothesis is enough to reach the weak conclusion: if $f ^ { ( \nu ) }$ is of bounded variation, then $\| f - p _ { n } ^ { * } \| = O ( n ^ { - \nu } )$ for the best approximation $\boldsymbol { p } _ { n } ^ { * }$ . Three years later Jackson [1911] sharpened the result by weakening the hypothesis as just indicated.

Summary of Chapter 7. The smoother a function $f$ defined on $\lfloor - 1 , 1 \rfloor$ is, the faster its approximants converge. In particular, if the νth derivative of $f$ is of bounded variation $V$ , then the Chebyshev coefficients $\{ a _ { k } \}$ of $f$ satisfy $| a _ { k } | \leq 2 \pi ^ { - 1 } V ( k - \nu ) ^ { - \nu - 1 }$ . For $\nu \geq 1$ , it follows that the degree $n$ Chebyshev projection and interpolant of $f$ both have accuracy $O ( V n ^ { - \nu } )$ .

Exercise 7.1. Total variation. (a) Determine numerically the total variation of $f ( x ) =$ $\sin ( 1 0 0 x ) / ( 1 + x ^ { 2 } )$ on $[ - 1 , 1 ]$ . (b) It is no coincidence that the answer is $\approx 1 0 0$ ; the total variation of $\sin ( M x ) / ( 1 + x ^ { 2 } )$ on $[ - 1 , 1 ]$ is asymptotic to $M$ as $M \to \infty$ . Explain why.

Exercise 7.2. Lipschitz continuous vs. derivative of bounded variation. (a) Prove that if the derivative $f ^ { \prime }$ of a function $f$ has bounded variation, then $f$ is Lipschitz continuous. (b) Give an example to show that the converse does not hold.

Exercise 7.3. Convergence for Weierstrass’s function. Exercise 6.1 considered a “pathological function” $w ( x )$ that is continuous but nowhere differentiable on $[ - 1 , 1 ]$ . (a) Make an anonymous function in MATLAB that evaluates $w ( \mathbf { x x } )$ for a vector $\tt x x$ to machine precision by taking the sum (6.1) to 53 terms. (b) Use Chebfun to produce a plot of $\| w - p _ { n } \|$ accurate enough and for high enough values of $n$ to confirm that convergence appears to take place as $n \to \infty$ . Thus $w$ is not one of the functions for which interpolants fail to converge, a fact we can prove with the techniques of Chapter 15 (Exercise 15.9).

Exercise 7.4. Sharpness of Theorem 7.2. Consider the functions (a) $f ( x ) = | x |$ , (b) $f ( x ) = | x | ^ { 5 }$ , and (c) $f ( x ) = \sin ( 1 0 0 x )$ . In each case plot, as functions of $_ n$ , the error $\| f - p _ { n } \|$ in Chebyshev interpolation on $[ - 1 , 1 ]$ and the bound on this quantity from (7.5). How close is the bound to the actuality? In cases (a) and (b), take $\nu$ as large as possible, and in case (c), take $\nu = 2$ , 4, and 8.

Exercise 7.5. Total variation. Let $f$ be a smooth function defined on [0, 1] and let $t ( x )$ be its total variation over the interval $[ 0 , x ]$ . What is the total variation of $t$ over [0, 1]?

Exercise 7.6. Chebyshev coefficients of a spline. A cubic spline is a piecewise cubic polynomial with two continuous derivatives. (a) How fast must the Chebyshev coefficients of a cubic spline decay? (b) Test this prediction with s=linspace(-1,1,10), $\mathtt { p } =$ chebfun( $( \Subset ( \mathbf { x } $ spline(s,exp(s),x))), plotcoeffs(p,'loglog').

# Chapter 8. Convergence for Analytic Functions

Suppose $f$ is not just $k$ times differentiable but infinitely differentiable and in fact analytic on $[ - 1 , 1 ]$ . (Recall that this means that for any $s \in [ - 1 , 1 ]$ , $f$ has a Taylor series about $s$ that converges to $f$ in a neighborhood of $s$ .) Then without any further assumptions we may conclude that the Chebyshev projections and interpolants converge geometrically, that is, at the rate $O ( C ^ { - n } )$ for some constant $C > 1$ . This means the errors will look like straight lines (or better) on a semilog scale rather than a loglog scale. This kind of connection was first announced in 1911 by Bernstein, who showed that the best approximations to a function $f$ on $[ - 1 , 1 ]$ converge geometrically as $n \to \infty$ if and only if $f$ is analytic [Bernstein 1911 & 1912b].

For example, for Chebyshev interpolants of the function $( 1 + 2 5 x ^ { 2 } ) ^ { - 1 }$ , known as the Runge function (Chapter 13), we get steady geometric convergence down to the level of rounding errors:

$\begin{array} { r l } & { \mathtt { x \_ } { c h e b f u n } ( \mathrm { \iota _ { X } ^ { \prime } ~ } \mathtt { x ^ { \prime } } ) \mathrm { ; ~ } \mathtt { f \_ } = \mathrm { \mathtt { 1 / ( 1 + 2 5 * x ^ { \circ } 2 ) } } \mathrm { ; ~ } \mathtt { n n \_ } = \mathrm { \mathtt { 0 : 1 0 : 2 0 0 } } \mathrm { ; ~ } \mathtt { e e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \_ \mathtt { e \mathtt { e } \_ \mathtt { \mathtt { i } } } } } } } } } } \mathtt { o } } = \mathrm { \mathtt { 0 : } } \mathtt { n } \mathrm { n } \mathrm { ; ~ } } \\ & { \mathtt { f o r \_ j } = \mathrm { \mathtt { 1 : 1 \mathtt { e n g t h } ( n n \mathtt { n } ) } } } \\ & { \mathtt { n \_ } = \mathtt { n \_ { e \_ \mathtt { e \_ { e \_ \mathtt { e \_ { e \_ \mathtt { e \_ { e } } } } } } } } \mathtt { n \_ } \mathtt { f n \_ } = \mathtt { c h e b f u n } ( \mathtt { f \_ { \mathtt { e } , n + 1 } } ) \mathrm { ; ~ } \mathtt { e e ( j ) \ } = \mathtt { n o r m } ( \mathtt { f \mathrm { - } f n , i n f } ) \mathrm { ; ~ } } \end{array}$   
end   
semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/72ea8df1c59a1d8b6e0c461a1caeb2c66610e22ed3ff60ccca6f136bb88ef4e0.jpg)

If $f$ is analytic not just on $[ - 1 , 1 ]$ but in the whole complex plane—such a function is said to be entire—then the convergence is even faster than geometric. Here, for the function $\cos ( 2 0 x )$ , the dots are approaching not a fixed straight line but a curve that gets steeper as $n$ increases, until rounding errors cut off the progress.

f $\begin{array} { r l } { = } & { \cos \left( 2 0 { * \mathbf { x } } \right) ; ~ \mathrm { n n ~ = ~ } 0 : 2 : 6 0 ; ~ \mathrm { e e ~ = ~ } 0 { * \mathbf { n } } \mathrm { n } ; } \\ { \mathrm { 3 r ~ j ~ = ~ } 1 : \mathrm { 1 e n g t h } \left( \mathrm { n n } \right) } \\ { \mathrm { ~ n ~ = ~ } \mathrm { n n ( j ) } ; ~ \mathrm { f n ~ = ~ c h e b f u n } \left( \mathrm { f , n + 1 } \right) ; ~ \mathrm { e e ( j ) ~ = ~ } \mathrm { n o r m } \left( \mathrm { f - f n , i n f } \right) ; } \end{array}$   
end   
semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/63bd3fd8967484fb149e6ea5504922c367fdc556e220582d4c3baf49c78fa183.jpg)

There are elegant theorems that explain these effects. If $f$ is analytic on $[ - 1 , 1 ]$ , then it can be analytically continued to a neighborhood of $[ - 1 , 1 ]$ in the complex plane. (The idea of analytic continuation is explained in complex variables textbooks; see also Chapter 28.) The bigger the neighborhood, the faster the convergence. In particular, for polynomial approximations, the neighborhoods that matter are the regions in the complex plane bounded by ellipses with foci at $^ { - 1 }$ and 1, known as Bernstein ellipses [Bernstein 1912b, 1912c & 1914a]. It is easy to plot these curves: pick a number $\rho > 1$ and plot the image in the complex $x$ -plane of the circle of radius $\rho$ in the $z$ -plane under the Joukowsky map $x = ( z + z ^ { - 1 } ) / 2$ . We let $E _ { \rho }$ denote the open region bounded by this ellipse. Here, for example, are the Bernstein ellipses corresponding to the parameters $\rho = 1 . 1 , 1 . 2 , . . . , 2$ :

z = exp(2i\*pi\*x);   
f $\mathrm { \Lambda } _ { 0 \Sigma } \ \mathrm { \bf ~ r h o } = 1 . 1 : 0 . 1 : 2$ e = (rho\*z+(rho\*z)^(-1))/2; plot(e), hold on   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/69575e4e795ac7ee11b111ff42e27f587cba42c34c5d6960fc5662c715aa98a0.jpg)

It is not hard to verify that the length of the semimajor axis of $E _ { \rho }$ plus the length of the semiminor axis is equal to $\rho$ (Exercise 8.1).

Here is the basic bound on Chebyshev coefficients of analytic functions from which many other things follow. It first appeared in Section 61 of [Bernstein 1912b].

Theorem 8.1. Chebyshev coefficients of analytic functions. Let a function $f$ analytic in $[ - 1 , 1 ]$ be analytically continuable to the open Bernstein ellipse $E _ { \rho }$ , where it satisfies $| f ( x ) | \leq M$ for some $M$ . Then its Chebyshev coefficients satisfy $| a _ { 0 } | \le M$ and

$$
\begin{array} { r } { | a _ { k } | \leq 2 M \rho ^ { - k } , \quad k \geq 1 . } \end{array}
$$

Proof. As in the proofs of Theorems 3.1, 4.1, and 7.1, we make use of the transplantation from $f ( x )$ and $T _ { k } ( x )$ on $[ - 1 , 1 ]$ in the $x$ -plane to $F ( z )$ and $( z ^ { k } +$ $z ^ { - k } ) / 2$ on the unit circle in the $z$ -plane, with $x = ( z + z ^ { - 1 } ) / 2$ and $F ( z ) = F ( z ^ { - 1 } ) =$ $f ( x )$ . The ellipse $E _ { \rho }$ in the $x$ -plane corresponds under this formula in a 1-to-2 fashion to the annulus $\rho ^ { - 1 } < | z | < \rho$ in the $z$ -plane. By this we mean that for each $x$ in $E _ { \rho } \backslash [ - 1 , 1 ]$ there are two corresponding values of $z$ that are inverses of one another, and both the circles $| z | = \rho$ and $| z | = \rho ^ { - 1 }$ map onto the ellipse itself. The first thing to note is that if $f$ is analytic in the ellipse, then $F ^ { \prime }$ is analytic in the annulus since it is the composition of the two analytic functions $z \mapsto ( z + z ^ { - 1 } ) / 2$ and $x \mapsto f ( x )$ . Now we make use of the contour integral formula (3.13),

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { | z | = 1 } z ^ { - 1 - k } F ( z ) d z ,
$$

with $\pi i$ replaced by $2 \pi i$ for $k = 0$ . Suppose for a moment that $F$ is analytic not just in the annulus but in its closure $\rho ^ { - 1 } \leq | z | \leq \rho$ . Then we can expand the contour to $| z | = \rho$ without changing the value of the integral, giving

$$
a _ { k } = { \frac { 1 } { \pi i } } \int _ { | z | = \rho } z ^ { - 1 - k } F ( z ) d z ,
$$

again with $\pi i$ replaced by $2 \pi i$ for $k ~ = ~ 0$ . Since the circumference is $2 \pi \rho$ and $| F ( z ) | \le M$ , the required bound now follows from an elementary estimate. If $F$ is analytic only in the open annulus, we can move the contour to $| z | = s$ for any $s < \rho$ , leading to the same bound for any $s < \rho$ and hence also for $s = \rho$ .

Here are two of the consequences of Theorem 8.1. Equation (8.2) first appeared in [Bernstein 1912b, Sect. 61]. I do not know where (8.3) may have appeared, though similar slightly weaker bounds can be found in (4.13) and (4.16) of [Tadmor 1986]. For a generalization of (8.3) to interpolation in other point sets with the same asymptotic distribution as Chebyshev points, see Theorem 12.1.

Theorem 8.2. Convergence for analytic functions. If $f$ has the properties of Theorem 8.1, then for each $n \geq 0$ its Chebyshev projections satisfy

$$
\| f - f _ { n } \| \leq { \frac { 2 M \rho ^ { - n } } { \rho - 1 } }
$$

and its Chebyshev interpolants satisfy

$$
\| f - p _ { n } \| \leq { \frac { 4 M \rho ^ { - n } } { \rho - 1 } } .
$$

Proof. Equation (8.2) follows from Theorem 8.1 and (4.8), and (8.3) follows from Theorem 8.1 and (4.9).

We can apply Theorem 8.2 directly if $f$ is analytic and bounded in $E _ { \rho }$ . If it is analytic but unbounded in $E _ { \rho }$ , then it will be analytic and bounded in $E _ { s }$ for any $s < \rho$ , so we still get convergence at the rate $O ( s ^ { - n } )$ for any $s < \rho$ . If it is unbounded in $E _ { \rho }$ but the only singularities on the ellipse are simple poles, then we get convergence at the rate $O ( \rho ^ { - n } )$ after all (Exercise 8.15).

Before applying Theorem 8.2 to a couple of examples, it will be convenient to note formulas for $\rho$ in two common special cases. Suppose $f$ has its dominant singularity at a real value $x _ { 0 } = \pm \alpha$ for some $\alpha > 1$ . Then the corresponding ellipse parameter is

$$
\rho = \alpha + \sqrt { \alpha ^ { 2 } - 1 } \quad ( \mathrm { r e a l \ s i n g u l a r i t y \ a t \ } x = \pm \alpha ) .
$$

Or suppose that the dominant singularity is at the pure imaginary value $x _ { 0 } = \pm i \beta$ for some $\beta > 0$ . Then we have

$$
\rho = \beta + { \sqrt { \beta ^ { 2 } + 1 } } \quad ( { \mathrm { i m a g i n a r y ~ s i n g u l a r i t y ~ a t ~ } } x = \pm i \beta ) .
$$

For example, the Runge function $( 1 + 2 5 x ^ { 2 } ) ^ { - 1 }$ considered above has poles at√ $\pm i / 5$ . By (8.5), the corresponding value of $\rho$ is $( 1 + \sqrt { 2 6 } ) / 5 \approx 1 . 2 2 0$ , and the errors in Chebyshev interpolation match this rate beautifully:

$\begin{array} { r l } { \mathbf { f } } & { = \mathbf { \Phi } _ { 1 } / ( 1 + 2 5 * \mathbf { x } \cdot 2 ) ; \mathbf { \Phi } \mathrm { n n } \ = \ 0 : 1 0 : 2 0 0 ; \mathbf { \Phi } \mathrm { e e ~ = \ 0 * \mathrm { n n } } ; } \\ { \mathbf { f o r } \ \mathbf { j } } & { = \mathbf { \Phi } _ { 1 } : \mathbf { { l } \mathrm { e n g t h } } ( \mathrm { n n } ) } \\ { \mathbf { n } } & { = \mathbf { \Phi } \mathrm { n n } ( \mathbf { j } ) ; \mathbf { \Phi } \mathrm { f n } \ = \ { \mathrm { c h e b f u n } } ( \mathbf { f } , \mathbf { n } + 1 ) ; \mathbf { \Phi } \mathrm { e e ( \mathbf { j } ) } \ = \ \mathbf { \mathrm { n o r m } } ( \mathbf { f } \mathrm { - } \mathbf { f n } , \mathbf { i } \mathrm { n f } ) ; } \end{array}$ end   
rho $=$ ( $1 +$ sqrt(26))/5;   
semilogy(nn,rho.^-nn, $\ " - \mathbf { r } \cdot \mathbf { \sigma }$ ), hold on, semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/d326a4b3ef702de624286acfd195a476bf5444dd6766a320c981a3ea782d1461.jpg)

Here is a more extreme but entirely analogous example: $\operatorname { t a n h } ( 5 0 \pi x )$ , with poles at $\pm 0 . 0 1 i$ . These poles are so close to $[ - 1 , 1 ]$ that the convergence is much slower, but it is still robust. The only difference in this code segment is that $\mathtt { n o r m } ( \mathtt { f } \mathtt { - f } \mathtt { n } , \mathtt { i n f } )$ , a relatively slow Chebfun operation that depends on finding zeros of the derivative of $\tt f - f n$ , has been replaced by the default 2-norm norm(f-fn), which is quick. This makes little difference to the figure, as the exponential decay rates are the same. (In the $\infty$ -norm, the dots in the figure would appear just above the red line instead of just below it.)

$\begin{array} { r l } & { \mathrm { ~ f ~ \omega = \ t a n h ( 5 0 * p i * x ) ~ ; ~ n n ~ \omega = ~ 0 : 2 0 0 : 4 0 0 0 ; ~ \eta \in \varphi = \varphi 0 * n n ; } } \\ & { \mathrm { ~ f o r ~ j ~ \omega = ~ 1 : 1 \mathrm { e n g t h } ( n n ) } } \\ & { \mathrm { ~ n ~ = ~ n n ( j ) ~ ; ~ f { n ~ = ~ c h e b f u n ( f , n + 1 ) } ~ ; ~ \eta \in e ( j ) ~ \omega = \varphi _ { n o r m } ( f - f { n } ) ~ ; } } \end{array}$ end   
rho $=$ ( $1 +$ sqrt(10001))/100;   
semilogy(nn,rho.^-nn,'-r'), hold on, semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/ae6d627aab68f93b8b6605848098e28f3faec1735413b2d13dce5c7b784f660a.jpg)

For an example with a real singularity, the function √ $\sqrt { 2 - x }$ has a branch point at $x = 2$ , corresponding by (8.4) to $\rho = 2 + \sqrt { 3 }$ . Again we see a good match, with the curve gradually bending over to the expected slope as $n \to \infty$ .

f $\begin{array} { r l } { = } & { \mathbf { s q r t } ( 2 \mathbf { - x } ) ; ~ \mathrm { n n ~ = ~ } 0 : 3 0 ; ~ \mathbf { e e ~ = ~ } 0 * \mathrm { n n } ; } \\ { \mathrm { ~ \mathrm { ~  ~ \lambda ~ } ~ } ] ~ \mathrm { ~  ~ \lambda ~ } = ~ 1 : \mathrm { { l e n g t h } } ( \mathrm { n n } ) } \\ { ~ \mathrm { ~  ~ \lambda ~ } = } & { \mathrm { { n n } ( j ) ~ ; ~ \mathrm { ~ \mathrm { ~ f n ~ = ~ c h e b f u n } ( f , n + 1 ) ~ } ; ~ \mathbf { e e } ( j ) ~ = ~ \mathrm { n o r m } ( f \mathrm { - } f n , \mathrm { i n f } ) ~ } ; } \end{array}$   
f   
end   
rho $=$ 2+sqrt(3); semilogy(nn,rho.^-nn,'-r')   
hold on, semilogy(nn,ee,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/124f5ab1686affef3bb200a80fa21247e2ca85304b6e3063b758f75f778428c9.jpg)

We now derive an elegant converse of Theorem 8.2, also due to Bernstein [1912b, Sect. 9]. The converse is not quite exact: Theorem 8.2 assumes analyticity and boundedness in $E _ { \rho }$ , whereas the conclusion of Theorem 8.3 is analyticity but not necessarily boundedness (Exercise 8.15).

Theorem 8.3. Converse of Theorem 8.2. Suppose $f$ is a function on $[ - 1 , 1 ]$ for which there exist polynomial approximations $q _ { n } \in P _ { n }$ satisfying

$$
\left\| f - q _ { n } \right\| \leq C \rho ^ { - n } , \quad n \geq 0 ,
$$

for some constants $\rho > 1$ and $C > 0$ . Then $f$ can be analytically continued to an analytic function in the open Bernstein ellipse $E _ { \rho }$ .

Proof. The assumption implies that the polynomials $\left\{ q _ { n } \right\}$ satisfy $\| q _ { n } - q _ { n - 1 } \| \leq$ $2 C \rho ^ { 1 - n }$ on $[ - 1 , 1 ]$ . Since $q _ { n } \mathrm { ~ - ~ } q _ { n - 1 } \in \mathcal { P } _ { n }$ , it can be shown that this implies $\| q _ { n } - q _ { n - 1 } \| _ { E _ { s } } \leq 2 C s ^ { n } \rho ^ { 1 - n }$ for any $s > 1$ , where $\| \cdot \| _ { E _ { s } }$ is the supremum norm on the $s$ -ellipse $E _ { s }$ . (This estimate is one of Bernstein’s inequalities, from Section 9 of [Bernstein 1912b]; see Exercise 8.6.) For $s < \rho$ , this gives us a representation for $f$ in $E _ { s }$ as a series of analytic functions,

$$
f = q _ { 0 } + ( q _ { 1 } - q _ { 0 } ) + ( q _ { 2 } - q _ { 1 } ) + \cdots ,
$$

which is uniformly convergent according to the Weierstrass M-test. According to another well-known theorem of Weierstrass, this implies that the limit is a bounded analytic function [Ahlfors 1953, Markushevich 1985]. Since this is true for any $s < \rho$ , the analyticity applies throughout $E _ { \rho }$ .

Note that Theorems 8.2 and 8.3 together establish a simple fact, sometimes known as Bernstein’s theorem: a function defined on $[ - 1 , 1 ]$ can be approximated by polynomials with geometric accuracy if and only if it is analytic. (See also Exercise 8.11 and [Bagby & Levenberg 1993].)

The term “Bernstein ellipse” refers to any ellipse in the complex plane with foci $\{ - 1 , 1 \}$ , and if $f$ is a function analytic on $[ - 1 , 1 ]$ , the bounds of Theorems 8.1 and 8.2 apply for any Bernstein ellipse inside which $f$ is analytic and bounded. If there is a largest ellipse inside which $f$ is analytic, then one might choose to say that this was “the” Bernstein ellipse for $f$ , but this might not always be the ellipse that gives the most useful bound, and if $f$ is entire, then there is no largest ellipse at all (Exercise 8.3).

Chebfun computations, however, suggest a practical way to single out a special Bernstein ellipse associated with a given function $f$ . The Chebfun ellipse for $f$ is the Bernstein ellipse whose parameter $\rho$ satisfies the condition

$$
\rho ^ { - n } = \varepsilon ,
$$

where $\varepsilon$ is the tolerance used by the Chebfun constructor (normally $2 ^ { - 5 2 }$ ) and $n$ is the degree of the polynomial chosen by Chebfun to resolve $f$ . The command plotregion plots these Chebfun ellipses. Thus for $f ( x ) = 1 / ( 1 { + } 2 5 x ^ { 2 } )$ , for example, the Chebfun ellipse comes very close to passing through the poles at $\pm 0 . 2 i$ :

$\begin{array} { r l } { \hat { \mathbf { f } } } & { { } = } \end{array}$ chebfun('1/(1+25\*x^2)'); plotregion(f), hold on, plot([.2i -.2i],'xr')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/be6fa3870d4c5327066d466f249064457bbd940e1ceea9eaf2e1a41cedcad210.jpg)

For the entire function $f ( x ) = \exp ( - 2 0 0 x ^ { 2 } )$ , the Chebfun ellipse has much the same shape, although now $f$ has no singularities:

f = chebfun('exp(-200\*x^2)'); plotregion(f)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0001_pages_0001-0070/auto/images/e24a609c87bb2d15d9eceae1984aaa1a388f8766374a10cd91b9d1cb0a5966b7.jpg)

Summary of Chapter 8. If $f$ is analytic, its Chebyshev coefficients $\{ a _ { k } \}$ decrease geometrically. In particular, if $f$ is analytic with $| f ( x ) | \leq M$ in the Bernstein $\rho$ -ellipse about $[ - 1 , 1 ]$ , then $| a _ { k } | \le 2 M \rho ^ { - k }$ . It follows that the degree $n$ Chebyshev projection and interpolant of $f$ have accuracy $O ( M \rho ^ { - n } )$ .

Exercise 8.1. Bernstein ellipses. Verify that for any $\rho > 1$ , the length of the semiminor axis plus the length of the semimajor axis of the Bernstein ellipse $E _ { \rho }$ is equal to $\rho$ .

Exercise 8.2. A Chebyshev series. With $\textbf { x } = \mathtt { c h e b f u n } ( \mathbf { \Omega } ^ { \prime } \mathbf { x } ^ { \prime } )$ , execute the command plotcoeffs $( \sin { ( 1 0 0 * ( \mathbf { x } - 1 ) ) } + . 0 1 * \operatorname { t a n h } { ( 2 0 * \mathbf { x } ) } )$ . Explain the various features of the resulting plot as quantitatively as you can.

Exercise 8.3. Interpolation of an entire function. The function $f ( x ) = \exp ( - x ^ { 2 } )$ is analytic throughout the complex $_ x$ -plane, so Theorem 8.2 can be applied for any value of the parameter $\rho > 1$ . Produce a semilog plot of $\| f - p _ { n } \|$ as a function of $n$ together with lines corresponding to the upper bound of the theorem for $\rho = 1 . 1 , 1 . 2 , 1 . 4 , 2 , 3 , 5 , 8$ . Be sure to use the right value of $M$ in each case. How well do your bounds fit the data?

Exercise 8.4. Convergence rates for different functions. Based on the theorems of this chapter, what can you say about the convergence as $n  \infty$ of the Chebyshev interpolants to (a) $\tan ( x )$ , (b) $\operatorname { t a n h } ( x )$ , (c) $\log ( ( x + 3 ) / 4 ) / ( x - 1 )$ , (d) $\int _ { - 1 } ^ { \cdot x } \cos ( t ^ { 2 } ) d t$ , (e) $\tan ( { \tan ( x ) } )$ , and (f) $( 1 + x ) \log ( 1 + x ) { \stackrel { . } { . } }$ ? In each case compare theoretical bounds with numerically computed results. Which is the case that converges much faster than the theorems predict? Can you speculate as to why?

Exercise 8.5. Accuracy of approximations in the complex plane. Let $_ p$ be the chebfun for $f ( x ) = \exp ( - 2 0 0 x ^ { 2 } )$ and plot contour lines in the complex $_ x$ -plane corresponding to $| f ( x ) - p ( x ) | = 1 0 ^ { - 2 } , 1 0 ^ { - 4 } , \cdot \cdot \cdot , 1 0 ^ { - 1 4 }$ . How do these curves compare to the Bernstein ellipses corresponding to parameters $\rho$ satisfying $\rho ^ { - n } = \varepsilon \times \{ 1 0 ^ { 2 } , 1 0 ^ { 4 } , \cdot \cdot \cdot , 1 0 ^ { 1 4 } \}$ , where $\varepsilon$ is the Chebfun constructor tolerance $2 ^ { - 5 2 }$ ?

Exercise 8.6. Proof of Bernstein inequality. Prove Bernstein’s inequality used in the proof of Theorem 8.3: if $p$ is a polynomial of degree $d$ , then $\| p \| _ { E _ { \rho } } \leq \rho ^ { d } \| p \|$ , where $\| \cdot \| _ { E _ { \rho } }$ is the $\infty$ -norm over the $\rho$ -ellipse and $\| \cdot \|$ is the $\infty$ -norm over $[ - 1 , 1 ]$ . (Hint: Show that if the branch cut is taken to be the unit interval $[ - 1 , 1 ]$ , the function $q ( z ) = p ( z ) / ( z + ( z ^ { 2 } - 1 ) ^ { 1 / 2 } ) ^ { d }$ is analytic throughout the region consisting of the complex plane plus the point $z = \infty$ minus $[ - 1 , 1 ]$ . Apply the maximum modulus principle.)

Exercise 8.7. Absolute value function. The function $| x - i |$ is analytic for $x \in [ - 1 , 1 ]$ . This means it can be analytically continued to an analytic function $f ( x )$ in a neighborhood of $[ - 1 , 1 ]$ in the complex $_ x$ -plane. The formula $| x - i |$ itself does not define an analytic function in any complex neighborhood. Find another formula for $f$ that does, and use it to explain what singularities $f$ has in the complex plane.

Exercise 8.8. Chebyshev polynomials on the Bernstein ellipse. Show that for any $\rho > 1$ and any $z$ on the boundary of the ellipse $E _ { \rho }$ in the complex $_ x$ -plane, $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } | T _ { n } ( x ) | ^ { 1 / n } = \rho } \end{array}$ .

Exercise 8.9. You can’t judge smoothness by eye. Define $f ( x ) = 2 + \sin ( 5 0 x )$ and $g ( x ) = f ( x ) ^ { 1 . 0 0 0 1 }$ and construct chebfuns for these functions on $[ - 1 , 1 ]$ . What are their lengths? Explain this effect quantitatively using the theorems of this chapter.

Exercise 8.10. Convergence of conjugate gradient iteration. Suppose we wish to approximate $f ( x ) = x ^ { - 1 }$ on the interval $[ m , M ]$ with $0 < m < M$ . Show that for any $\kappa > M / m$ , there exist polynomials $p _ { n } \in \mathcal { P } _ { n }$ such that $\| f - p _ { n } \| = O ( ( 1 + 2 / { \sqrt { \kappa } } ) ^ { - n } )$ as $n \to \infty$ , where $\| \cdot \|$ is the $\infty$ -norm on $[ m , M ]$ . This result is famous in numerical linear algebra as providing an upper bound for the convergence of the conjugate gradient iteration applied to a symmetric positive definite system of equations $A x = b$ with condition number $\kappa$ . See Theorem 38.5 of [Trefethen & Bau 1997].

Exercise 8.11. Bernstein’s theorem. Show that the conclusion of Theorem 8.3 also holds if the hypothesis is weakened to $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \| f - q _ { n } \| ^ { 1 / n } \leq \rho ^ { - 1 } } \end{array}$ .

Exercise 8.12. Resolution power of Chebyshev interpolants. The function $f _ { M } ( x ) = \exp ( - M ^ { 2 } x ^ { 2 } / 2 )$ has a spike of width $O ( 1 / M )$ at $x \ = \ 0$ . Let $n ( M )$ be the degree of a chebfun for $f _ { M }$ . (a) Determine the asymptotic behavior of $n ( M )$ as $M \to \infty$ by numerical experiments. (b) Explain this result based on the theorems of this chapter.

Exercise 8.13. Resolution power of Bernstein polynomials. Continuing the last exercise, now let $n ( M )$ be the degree of a Bernstein polynomial (6.2) needed to approximate $f _ { M }$ to machine precision. (For this discussion rescale (6.2) from $[ 0 , 1 ]$ to $[ - 1 , 1 ]$ .) (a) Determine the asymptotic behavior of $n ( M )$ as $M  \infty$ by numerical experiments. (b) Explain this result, not necessarily rigorously.

Exercise 8.14. Formulas for ellipse parameter. Derive (8.4) and (8.5).

Exercise 8.15. Simple poles on the Bernstein ellipse. (a) Explain how (3.16) illustrates that Theorem 8.3 is not an exact converse of Theorem 8.2. (b) Let $f$ be analytic in the open Bernstein ellipse region $E _ { \rho }$ for some $\rho > 1$ with the only singularities on the ellipse itself being simple poles. Show that $\| f - f _ { n } \|$ and $\| f - p _ { n } \|$ are of size $O ( \rho ^ { - n } )$ as $n \to \infty$ .


<!-- chunk 0002: pages 71-140 -->
# Chapter 9. Gibbs Phenomenon

Polynomial interpolants and projections oscillate and overshoot near discontinuities. We have observed this Gibbs phenomenon already in Chapter 2, and now we shall look at it more carefully. We shall see that the Gibbs effect for interpolants can be regarded as a consequence of the oscillating inverse-linear tails of Lagrange polynomials, i.e., interpolants of Kronecker delta functions. Chapter 15 will show that these same tails, combined together in a different manner, are also the origin of Lebesgue constants of size $O ( \log n )$ , with implications throughout approximation theory.

To start, consider $\mathtt { s i g n } ( \mathtt { x } )$ , interpolated in $n + 1 = 1 0$ and 20 Chebyshev points. We take $n$ odd to avoid a grid point at the middle of the step.

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun $( \mathbf { \partial } ^ { \prime } \mathbf { x } ^ { \prime } )$ ; f = sign(x); subplot(1,2,1) plot(f,'k') hold on $\mathtt { f 9 } =$ chebfun(f,10); plot(f9,'.-') subplot(1,2,2) plot(f,'k'), hold on, $\yen 19 ~ =$ chebfun(f,20); plot(f19,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/a41920a9115a68882886a5a5d6c6cfb20cacf995fedafa34b1e1d789705c5eb3.jpg)

Both of these figures show a substantial overshoot near the jump. As $n$ increases from 9 to 19, the overshoot gets narrower, but not shorter, and it will not go away as $n \to \infty$ . Let us zoom in and look at the plot on subintervals:

subplot(1,2,1), plot(f,'k'), hold on plot(f9,'.-','interval',[0 0.8]) subplot(1,2,2), plot(f,'k'), hold on plot(f19,'.-','interval',[0 0.4])

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/3e74bbafa1851a7007123be0b0d13fe831ca66da32948f2d4bf759b0904bc286.jpg)

We now zoom in further with analogous plots for $n = 9 9$ and 999.

subplot(1,2,1), plot(f, $^ { 1 } \mathtt { k } ^ { \prime } )$ , hold on   
$\mathtt { f 9 9 } =$ chebfun(f,100); plot(f99,'.-','interval',[0 0.08])   
subplot(1,2,2), plot(f,'k'), hold on   
$\mathbf { f } 9 9 9 ~ =$ chebfun(f,1000); plot(f999,'.-','interval',[0 0.008])

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/c1e5465a9e980e49e1325bfe0cab6fbb30233e4b9d5ceaa568f8e81052b9882c.jpg)

Notice that in these figures, the vertical scale is always fixed while the horizontal scale is adjusted proportionally, confirming that the Gibbs overshoot gets narrower but approaches a constant height in the limit $n \to \infty$ .

What is this height? We can measure it numerically with the max command:

for $\mathtt { n } ~ = ~ 2 . \hat { \ } ( 1 : 8 ) - 1$ gibbs $=$ max(chebfun(f,n+1)); fprintf('%7d %17.8f\n', n, gibbs)   
end

<table><tr><td>n</td><td>Gibbs amplitude</td></tr><tr><td>1</td><td>1.00000000</td></tr><tr><td>3</td><td>1.18807518</td></tr><tr><td>7</td><td>1.26355125</td></tr><tr><td>15</td><td>1.27816423</td></tr><tr><td>31</td><td>1.28131717</td></tr><tr><td>63</td><td>1.28204939</td></tr><tr><td>127</td><td>1.28222585</td></tr><tr><td>255</td><td>1.28226917</td></tr></table>

Clearly as $n \to \infty$ , the maximum of the Chebyshev interpolant to the sign function converges to a number bigger than 1. The total variation of the interpolant, meanwhile, diverges slowly to $\infty$ , at a rate proportional to $\log n$ , and this is the effect we shall examine further in Chapter 15.

for n = 2.^(1:8)-1 tv $=$ norm(diff(chebfun(f,n+1)),1); fprintf('%7d %14.2f\n', n, tv)   
end

<table><tr><td>n</td><td>variation</td></tr><tr><td>1</td><td>2.00</td></tr><tr><td>3</td><td>2.75</td></tr><tr><td>7</td><td>3.64</td></tr><tr><td>15</td><td>4.56</td></tr><tr><td>31</td><td>5.47</td></tr><tr><td>63</td><td>6.37</td></tr><tr><td>127</td><td>7.26</td></tr><tr><td>255</td><td>8.15</td></tr></table>

The following theorem summarizes the Gibbs phenomenon for Chebyshev interpolants. Well, perhaps it is a little bold to call it a “theorem,” since it is not clear that a proof has ever been written down. The formulas necessary to represent the interpolant (in the equivalent trigonometric case—see Exercise 9.4) can be found in various forms in [Runck 1962] and in [Helmberg & Wagner 1997], which relates the interpolating polynomial to the beta function and reports the numbers 1.282 and 1.066 to 3 digits of accuracy. The more precise results presented here have been privately communicated to me by Wagner based on calculations to more than 500 digits.

Theorem 9.1. Gibbs phenomenon for Chebyshev interpolants. Let $p _ { n }$ be the degree $n$ Chebyshev interpolant of the function $f ( x ) = \mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ . Then as $n \to \infty$ ,

$$
\operatorname* { l i m } _ { n \to \infty , n o d d } \| p _ { n } \| = c _ { 1 } = 1 . 2 8 2 2 8 3 4 5 5 7 7 5 4 2 8 5 4 8 1 3 \dots ,
$$

$$
\operatorname* { l i m } _ { n \to \infty , n e v e n } \| p _ { n } \| = c _ { 2 } = 1 . 0 6 5 7 8 3 8 8 8 2 6 6 4 4 8 0 9 9 0 5 \dots .
$$

(The case of n even differs in having a grid point at the middle of the jump.)

Although we are not going to prove Theorem 9.1, we do want to indicate where the fixed-overshoot effect comes from. Everything falls into place when we consider the Lagrange polynomials introduced in Chapter 5. Recall from (5.2) that the $j$ th Lagrange polynomial $\ell _ { j } ( x )$ for the $( n + 1 )$ -point Chebyshev grid is the unique polynomial in $\mathcal { P } _ { n }$ that takes the values $1$ at $x _ { j }$ and $0$ at the other grid points $x _ { k }$ . On the 20-point grid, i.e., $n = 1 9$ , here are the Lagrange polynomials $\ell _ { 1 0 }$ and $\ell _ { 1 1 }$ with a dashed line marked at $x = - 0 . 1 5$ , which we will take as our point of special interest:

yl = [-0.3 1.3]; xc = -0.15\*[1 1];   
$\mathtt { p 1 0 ~ = ~ }$ chebfun([zeros(1,10) 1 zeros(1,9)]);   
${ \tt p } 1 1 \ =$ chebfun([zeros(1,11) 1 zeros(1,8)]);   
subplot(1,2,1), plot(p10,'.-'), hold on, plot(xc,yl,'--r') subplot(1,2,2), plot(p11,'.-'), hold on, plot(xc,yl,'--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/7c8788999043c554c7c2767b5dbad514d61ff969c97559c83ba6dcf5ea12398b.jpg)

Here are $\ell _ { 1 2 }$ and $\ell _ { 1 3 }$ :

$\mathtt { p } 1 2 \ =$ chebfun([zeros(1,12) 1 zeros(1,7)]);   
$\mathtt { p 1 3 } =$ chebfun([zeros(1,13) 1 zeros(1,6)]);   
subplot(1,2,1), plot(p12,'.-'), hold on, plot(xc,yl,'--r') subplot(1,2,2), plot(p13,'.-'), hold on, plot(xc,yl,'--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/22a86db9515be1639567a9ad59e767e6c78a64bbab701f6b15ab4579d3ad838c.jpg)

Following (5.1), we note that by taking the sum of a sequence of such Lagrange functions, we get the interpolant to the function that jumps from 0 for $x < 0$ to $^ { 1 }$ for $x > 0$ . Here is the sum of the four just plotted, which is beginning to look like a square wave:

plot(p10+p11+p12+p13,'.-'), hold on, plot(xc,yl,'--r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d20ed3ca107e1bcd81584662cbad935f8a0fe28d570f54fafd59402a32e277c1.jpg)

If we went all the way to the last grid point we would get the interpolant

$$
p ( x ) = \sum _ { j = ( n + 1 ) / 2 } ^ { n } \ell _ { j } ( x ) .
$$

Note that for any fixed $x < x _ { ( n - 1 ) / 2 }$ , this is an alternating series of small terms whose amplitudes decrease inverse-linearly to zero. The finite but nonzero sum of such a series in the limit $n  \infty$ is what gives rise to the fixed-overshoot Gibbs effect in polynomial interpolation.

In particular, suppose we focus on the dashed line at $x = - 0 . 1 5$ in the figures. Notice the alternating signs of the values of $\ell _ { 1 0 } , \ell _ { 1 1 } , \ell _ { 1 2 } , \ell _ { 1 3 }$ at this value of $x$ . In the figure for $\ell _ { 1 0 } + \ell _ { 1 1 } + \ell _ { 1 2 } + \ell _ { 1 3 }$ we accordingly see the Gibbs overshoot beginning to converge to its asymptotic amplitude $\approx 0 . 1 4 1$ . This number is half of the value 0.282 . . . of Theorem 9.1, since the jump for this function is of amplitude 1 instead of 2.

In Chapter 15 we shall consider the same alternating series but with signs multiplied by $( - 1 ) ^ { j }$ . This eliminates the alternation, so that we have approximately a harmonic series of inverse-linear terms. The partial sums of such a series grow at a logarithmic rate, as we saw above in the calculation of the variation.

Our discussion so far has concerned interpolants, but there is a parallel theory of the Gibbs phenomenon for projections—in the notation of this book, polynomials $f _ { n }$ rather than $p _ { n }$ . (The required Chebyshev coefficients are defined by the same integral (3.12) of Theorem 3.1, even though we are now dealing with functions $f$ that are not Lipschitz continuous as in the assumption stated for that theorem.) As always, though the interpolants are closer to practical computation, the projections may appear to be more fundamental mathematically. Historically speaking, it was the case of Fourier (trigonometric) projection that was analyzed first. The original discoverer was not Gibbs but Henry Wilbraham, a 22-year-old fellow of Trinity College, Cambridge, in 1848, who unfortunately made the mistake of publishing his fine paper in the short-lived Cambridge and Dublin Journal of Mathematics [Wilbraham 1848]. Fourier series for certain functions with jumps were already long known in Wilbraham’s day—in fact they go back to Euler, half a century before Fourier. The particular series studied by Wilbraham, originally due to Euler in 1772, is

$$
\cos ( t ) - { \frac { 1 } { 3 } } \cos ( 3 t ) + { \frac { 1 } { 5 } } \cos ( 5 t ) - \cdot \cdot \cdot ,
$$

which approximates a square wave of height $\pm \pi / 4$ (compare Exercise 3.6(a)):

t = chebfun('t',[-6,6]); f = (pi/4)\*sign(cos(t)); plot(f,'k') f9 $=$ cos(t) - cos(3\*t)/3 + cos(5\*t)/5 - cos(7\*t)/7 $^ +$ cos(9\*t)/9; hold on, plot(f9)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d47b726b556cb9c50e111d3ad41a9e075aa075ca74734581f44e4d52c496431a.jpg)

Wilbraham worked out the magnitude of the overshoot, and thus the following analogue of Theorem 9.1 is due to him.

Theorem 9.2. Gibbs phenomenon for Chebyshev projections. Let $f _ { n }$ be the degree $n$ Chebyshev projection of the sign function $f ( x ) = \mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ . Then as $n \to \infty$ ,

$$
\operatorname* { l i m } _ { n \to \infty } \| f _ { n } \| = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } { \frac { \sin { x } } { x } } d x = 1 . 1 7 8 9 7 9 7 4 4 4 7 2 1 6 7 \ldots .
$$

(The function $\begin{array} { r } { \mathrm { S i } ( x ) = \int _ { 0 } ^ { x } t ^ { - 1 } \sin { t } d t } \end{array}$ is known as the sine integral; see Exercise 9.6.) To see this number experimentally we can use the 'trunc' option in the Chebfun constructor. The overshoots look similar to what we saw before, but with smaller amplitude.

f = sign(x); subplot(1,2,1), plot(f,'k'), hold on $\begin{array} { r l } { \mathbf { f } 9 } & { { } = } \end{array}$ chebfun(f,'trunc',10); plot(f9,'-') subplot(1,2,2), plot(f,'k'), hold on $\yen 19 ~ =$ chebfun(f,'trunc',20); plot(f19,'-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/05db5756b4d57edfa7e5fe80873c79ffbffb6c7ba97a600becc9070fe0747966.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/34f5a32f7a0ced3afff4edf602eebbd45a8d3b210eeb4a1286dc8a8a64eaab85.jpg)

The numbers behave as predicted:

for np = 2.^(4:7) g = chebfun(f,'trunc',np);

fprintf('%7d %17.8f\n', np, max(g{0,5/np})) end limit $=$ (2/pi)\*sum(chebfun('sin(x)/x',[0 pi]))

n Gibbs amplitude 16 1.18028413 32 1.17930541 64 1.17906113 128 1.17900009 limit = 1.178979744472167

In all the experiments of this chapter we have worked with polynomials rather than trigonometric series, but the effects are the same (Exercise 9.4).

It is worth commenting on a particular property of series such as (9.3) that we have taken for granted throughout this discussion: even though each partial sum is continuous, a series may converge pointwise to a discontinuous limit, everywhere except at the points of discontinuity themselves. This kind of behavior seems familiar enough nowadays, but in the century beginning with Fourier’s work in 1807, it often seemed paradoxical and confusing to mathematicians. The same pointwise convergence to discontinuous functions can also occur with interpolants, as in Theorem 9.1.

In this chapter we have focused on the height of the overshoot of a Gibbs oscillation, because this is the effect so readily seen in plots. Perhaps the most important property of Gibbs oscillations for practical applications, however, is not their height but their slow decay as one moves away from the point of discontinuity. If $f$ has a jump, the oscillations at a distance $k$ grid points away must be expected to be of size $O ( k ^ { - 1 } )$ ; if $f ^ { \prime }$ has a jump, we expect oscillations of size $O ( k ^ { - 2 } )$ , and so on. (See Exercise 9.8. Exercise 26.5 will look at the analogous exponents for interpolation by rational functions rather than polynomials.) This algebraic rate of decay of information in polynomial interpolants can be contrasted with the exponential decay that one gets with spline approximations, which is the key advantage of splines for certain applications. Chebfun responds to this problem by representing functions with discontinuities by piecewise polynomials rather than global ones, with breakpoints at the discontinuities. For example, the location of the discontinuity in the function $\exp ( | x - 0 . 1 | )$ will be determined automatically in response to the command

The result is a chebfun consisting of two pieces each of degree 3, and the break in the middle appears at the right place:

f.ends(2)

# ans $=$ 0.100000000000000

Let us return to 22-year-old Mr. Wilbraham. Unfortunately, his published paper had little impact, and the effect was rediscovered and discussed in the pages of Nature during 1898–1899 by James Michelson, A. E. H. Love, and J. Willard

Gibbs. These authors got more attention for a number of reasons. First, they were leading scientists. Second, their problem arose at a time when applied mathematics had advanced much further and in a practical application, a mechanical graphing machine called a “harmonic analyzer” used by Michelson and Stratton. Third, they published their observations in a major journal. Fourth, they failed to get it right at first, so several publications appeared in succession! Other mathematicians got involved too, notably Poincar´e. Finally, they were lucky enough to have “Gibbs’s phenomenon” named and highlighted a few years later in a major research article on Fourier analysis by the mathematician Maxime Bˆocher [1906]. For a fascinating discussion of the history of the Gibbs phenomenon (for projection, not interpolation), which they more properly call the Gibbs–Wilbraham phenomenon, see [Hewitt & Hewitt 1979].

Summary of Chapter 9. Chebyshev projections and interpolants, as well as other polynomial and trigonometric approximations, tend to oscillate near discontinuities. The oscillations decay algebraically, not exponentially, with distance from the discontinuity.

Exercise 9.1. Calculations for larger $\textbf { \em n }$ . We measured the height of the Gibbs overshoot for a step function for $n = 1 , 3 , 7 , \dotsc , 2 5 5$ . Larger values of $n$ get a bit slow, but knowing that the maximum occurs around $x = 3 / n$ , compute these numbers up to $n = 4 0 9 5$ using a command of the form $\mathtt { m a x } ( \mathtt { g } \{ 0 , 5 / \mathtt { n } \} )$ . How great a speedup does this trick produce?

Exercise 9.2. A function with many jumps. Use Chebfun to produce a plot of the degree 200 Chebyshev interpolant to the function round $\mathbf { \tilde { e } } \mathbf { x p } ( \mathbf { s i n } ( 2 \ast \mathbf { p i } \ast \mathbf { x } ) ) )$ on $[ - 1 , 1 ]$ .

Exercise 9.3. Lagrange polynomials. Take $n \geq 2$ to be even and let $p$ be the degree $_ n$ Chebyshev interpolant to the Kronecker delta function at $x = x _ { n / 2 } = 0$ . (a) Use the barycentric formula of Theorem 5.2 to obtain a simple formula for $p$ . (b) Derive a formula for the values of $p$ at the “Chebyshev midpoints” defined by the usual formula $x _ { j } = \cos ( j \pi / n )$ of Chapter 2 except with half-integer values of $j$ . (c) For $n = 1 0 0$ , use Chebfun to produce an elegant plot showing the inverse-linear amplitudes of these values. (You can get the Chebyshev midpoints from chebpts $( \mathtt { n } , 1 )$ or from $\mathbf { x } =$ chebpts $^ { 2 * \mathtt { n } + 1 }$ ), $\mathtt { x } { = } \mathtt { x } ( 2 { : } 2 { : } \mathtt { e n d } )$ .)

Exercise 9.4. Fourier and Chebyshev Gibbs phenomena. We have repeatedly made the connection between Chebyshev polynomials $T _ { n } ( x )$ on the unit interval, Laurent polynomials $( z ^ { n } + z ^ { - n } ) / 2$ on the unit circle, and trigonometric polynomials $\cos ( n \theta )$ on $[ - \pi , \pi ]$ . Use these connections to show that the Gibbs overshoot in Chebyshev interpolation of $\mathrm { s i g n } ( x )$ on $[ - 1 , 1 ]$ , with $n$ even, is identical to the overshoot for a certain problem of trigonometric interpolation in $\theta$ .

Exercise 9.5. Local minima of a truncated sine series. (a) Plot $\phi _ { n }$ with $n = 1 0 , 1 0 0$ , and 1000 for a sum going back to Euler in 1755,

$$
\phi _ { n } ( x ) = \sum _ { k = 1 } ^ { n } { \frac { \sin ( k x ) } { k } } .
$$

What function does the sum evidently converge to? Is the Gibbs overshoot of the same relative magnitude as for (9.3)? (b) For each case, determine the first four local minimum values of $\phi _ { n } ( x )$ in $( 0 , \pi )$ . (c) Write an elegant Chebfun program that determines the smallest value of $_ n$ for which these minima are not monotonically decreasing. (This effect was investigated by Gronwall [1912].)

Exercise 9.6. Sine integral. (a) Construct and plot a chebfun for the sine integral $\begin{array} { r } { \mathrm { S i } ( x ) = \int _ { 0 } ^ { x } t ^ { - 1 } \sin { t } d t } \end{array}$ for $x \in [ 0 , 1 0 ]$ . What is its length? (b) Same for $x \in [ 0 , 1 0 0 ]$ . (c) Same for $\dot { \boldsymbol { x } } \in [ 0 , 1 0 0 0 ]$ .

Exercise 9.7. An unresolvable function. The polynomial interpolant to $\sin ( 1 / x )$ through 100,000 Chebyshev points can be produced by the command $\textbf { f } = \mathtt { c h e b f u n } ( \mathbb { Q } ( \textbf x )$ $\mathtt { s i n } ( 1 / \mathtt { x } )$ ,100000). The plot produced by plot(f) looks as if there is a bug in the computation somewhere. Produce similar plots for 10000, 1000, and smaller even numbers of points and explain why, in fact, there is no bug.

Exercise 9.8. Decay away from discontinuity. (a) Plot the function $f ( x ) \ =$ $\cos ( 7 x ) \sin ( 3 x ) + \sin ( \sin ( x / 2 ) ) e ^ { x }$ on $[ - 1 , 1 ]$ as well as its interpolating polynomial $p _ { n } ( x )$ in $n + 1 = 1 0 0$ Chebyshev points. (b) Confirm the algebraic rate of decay away from the discontinuity by plotting $| f ( x ) - p _ { n } ( x ) |$ together with the function $c / | x |$ for a suitable value of $c$ . (c) Using the spline command as in Exercise 7.6 with a sufficiently fine equispaced grid, confirm that the rate of decay is exponential for spline interpolants.

# Chapter 10. Best Approximation

An old idea, going back to Chebyshev himself and earlier to Poncelet, is to look for a polynomial $p ^ { * }$ of specified degree $n$ that is the best approximation to a given continuous function $f$ in the sense of minimizing the $\infty$ -norm of the difference on an interval [Poncelet 1835, Chebyshev 1854 & 1859]. (A best approximation is also called a Chebyshev approximation, but we shall avoid this usage to minimize confusion. Other terms are minimax and equiripple.) It is known that $p ^ { * }$ exists and is unique, as we shall prove below. There is a Chebfun command minimax for computing these approximants, due to Silviu Filip and others: if $f$ is a chebfun, then minimax(f,n) is the chebfun corresponding to its best approximation of degree $n$ . For details see [Filip et al. 2018].

We shall argue in Chapter 16 that best approximations in the $\infty$ -norm are not always as useful as one might imagine; Chebyshev interpolants are often as good or even better. Nevertheless, they represent an elegant and fundamental idea and a line of investigation going back more than 150 years. So for the moment, let us enjoy them.

For example, here are the best approximants of degrees 2 and 4 to $| x |$ , together with their error curves $( f - p ^ { * } ) ( [ - 1 , 1 ] )$ :

x = chebfun $( \because \tt X ^ { \prime } )$ ; f = abs(x);   
for $\texttt { n } = \texttt { 2 : 2 : 4 }$ subplot(1,2,1), plot(f,'k') [p,err] $=$ minimax(f,n); hold on, plot(p,'b') subplot(1,2,2), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/305d97302ff976bf6e62aa896a493ed9f96bcf70060e2746ea4e69758baac280.jpg)

Notice the equioscillation property: the error curve attains its extreme magnitude with alternating signs at a succession of values of $x$ . Chebyshev appears to have known this in the 1850s, and indeed suggested he was not the first to know it (“comme on le sait,” p. 114 of [Chebyshev 1854]), but he did not explicitly address questions of existence, uniqueness, or even alternation of signs. More systematic treatments came at the beginning of the 20th century with work by Blichfeldt [1901], Kirchberger [1902], and Borel [1905]. It seems to have been Kirchberger, in his PhD thesis written under Hilbert, who first stated and proved the characterization theorem that is now so well known [Kirchberger 1902], proving in particular that a best approximation $p ^ { * }$ exists. Note that in the characterization part of this theorem, $f$ is assumed to be real, whereas most of the discussion in this book allows $f$ to be real or complex. Existence and uniqueness in the complex case were established by Tonelli [1908]. Complex generalizations of the characterization originate with [Kolmogorov 1948] and [Remez 1951]. Many further generalizations can also be found in the approximation theory literature, for example, with the set of polynomials on an interval replaced by a more general set of functions satisfying a property known as the Haar condition.

Theorem 10.1. Equioscillation characterization of best approximants. A continuous function $f$ on $[ - 1 , 1 ]$ has a unique best approximation $p ^ { * } \in \mathcal { P } _ { n }$ . If $f$ is real, then $p ^ { * }$ is real too, and in this case a polynomial $p \in \mathcal { P } _ { n }$ is equal to $p ^ { * }$ if and only if $f - p$ equioscillates in at least $n + 2$ extreme points.

Proof. A set of $n + 2$ points of equioscillation of this kind is called an alternant, though we shall not make much use of this term.

To prove existence of a best approximation, we note that $\| f - p \|$ is a continuous function of $p \in \mathcal { P } _ { n }$ . Since one candidate approximation is the zero function, we know that if $p ^ { * }$ exists, it lies in $\{ p \in { \mathcal { P } } _ { n } : \| f - p \| \leq \| f \| \}$ . This is a closed and bounded subset of a finite-dimensional space, hence compact (the Heine–Borel property), and thus the minimum is attained. (This argument originates with $\mathrm { F }$ . Riesz [1918].)

Next we show that equioscillation implies optimality. Suppose $f$ and $p$ are real and $( f - p ) ( x )$ takes equal extreme values with alternating signs at $n + 2$ points $x _ { 0 } < x _ { 1 } < \cdots < x _ { n + 1 }$ , and suppose $\| f - q \| < \| f - p \|$ for some real polynomial $q \in \mathcal { P } _ { n }$ . Then $p - q$ must take nonzero values with alternating signs at the equioscillation points, implying that it takes the value zero in at least $n { \mathrel { + { 1 } } }$ points in between. This implies that $p - q$ is identically zero, which is a contradiction.

The third step is to show that optimality implies equioscillation (this part of the argument was given in [Blichfeldt 1901]). Suppose $f - p$ equioscillates at fewer than $n + 2$ points, and set $E = \| f - p \|$ . Without loss of generality suppose the leftmost extremum is one where $f - p$ takes the value $- E$ . Then there are numbers $- 1 < x _ { 1 } < \cdot \cdot \cdot < x _ { k } < 1$ with $k \leq n$ such that $( f - p ) ( x ) < E$ for $x \in [ - 1 , x _ { 1 } ] \cup$ $[ x _ { 2 } , x _ { 3 } ] \cup [ x _ { 4 } , x _ { 5 } ] \cup \ldots$ and $( f - p ) ( x ) > - E$ for $x \in [ x _ { 1 } , x _ { 2 } ] \cup [ x _ { 3 } , x _ { 4 } ] \cup \cdot \cdot \cdot .$ If we define $\delta p ( x ) = ( x _ { 1 } - x ) ( x _ { 2 } - x ) \cdot \cdot \cdot ( x _ { k } - x )$ , then $( p - \varepsilon \delta p ) ( x )$ will be a better approximation than $p$ to $f$ for all sufficiently small $\varepsilon > 0$ .

Finally, to prove uniqueness of best approximations—we treat the real case only—we refine the argument that equioscillation implies optimality. Suppose $p$ is a best approximation with equioscillation extreme points $x _ { 0 } < x _ { 1 } < \cdots < x _ { n + 1 }$ , and suppose $\| f - q \| ~ \leq ~ \| f - p \|$ for some real polynomial $q \in \mathcal { P } _ { n }$ . Then (without loss of generality) $( p - q ) ( x )$ must be $\leq 0$ at $x _ { 0 } , x _ { 2 } , x _ { 4 } , \ldots$ and $\geq 0$ at $x _ { 1 } , x _ { 3 } , x _ { 5 } , \dotsc .$ This implies that $p - q$ has roots in each of the $n + 1$ closed intervals $[ x _ { 0 } , x _ { 1 } ] , [ x _ { 1 } , x _ { 2 } ] , \dotsc , [ x _ { n } , x _ { n + 1 } ]$ . We wish to conclude that $p - q$ has at least $n + 1$ roots in total, counted with multiplicity, implying that $p = q$ . To make the argument we prove by induction that $p - q$ has at least $k$ roots in $[ x _ { 0 } , x _ { k } ]$ for each $k$ . The case $k = 1$ is immediate. For the general case, suppose $p - q$ has at least $j$ roots in $[ x _ { 0 } , x _ { j } ]$ for each $j \le k - 1$ but only $k - 1$ roots in $[ x _ { 0 } , x _ { k } ]$ . Then there must be a simple root at $x _ { k - 1 }$ . By the induction hypothesis, $p - q$ must have exactly $k - 2$ roots in $[ x _ { 0 } , x _ { k - 2 } ]$ with a simple root at $x _ { k - 2 }$ , $k - 3$ roots in $[ x _ { 0 } , x _ { k - 3 } ]$ with a simple root at $x _ { k - 3 }$ , and so on down to 1 root in $[ x _ { 0 } , x _ { 1 } ]$ , with a simple root at $x _ { 1 }$ . It follows that $p - q$ must be nonzero at $x _ { 0 }$ and at $x _ { k }$ , and since the sign of $p - q$ changes at each of the simple roots $x _ { 1 } , \ldots , x _ { k - 1 }$ , the signs at $x _ { 0 }$ and $x _ { k }$ must be the same if $k$ is odd and opposite if $k$ is even. On the other hand, from the original alternation condition we know that $p - q$ must take the same signs at $x _ { 0 }$ and $x _ { k }$ if $k$ is even and opposite signs if $k$ is odd.

There is a simpler proof of uniqueness than the one just given, in which one supposes $p$ and $q$ are distinct best approximations and considers $( p + q ) / 2$ (Exercise 10.10). However, that proof does not generalize to the problem of rational approximation (Theorem 24.1).

Note that the error curve for a best approximation may have more than $n + 2$ points of equioscillation, and indeed this will always happen if $f$ and $n$ are both even or both odd (Exercise 10.4). For example, for the function $f ( x ) = \left| x \right|$ considered above, the degree 2 approximation equioscillates at 5 points, not 4, and the degree 4 approximation equioscillates at 7 points, not 6. This phenomenon of “extra” points of equioscillation will become important in the generalization to rational approximation in Chapter 24.

Here is another example, the degree 10 best approximation to $\exp ( x )$ . There are 12 points of equioscillation.

f = exp(x); [p,err] $=$ minimax(f,10); plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/8e2e0618097c13d769454a2b0be72f9d2f0c0714f3644ade1d8d25529b4834c8.jpg)

And here is another example. The Chebfun cumsum command returns the indefinite integral, producing in this case a zigzag function.

f = cumsum(sign(sin(20\*exp(x)))); plot(f,'k'), hold on [p,err] $=$ minimax(f,20); plot(p)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/7e60c660203476097b15f215657c12a267cb7ca11a74416508c3af3200082041.jpg)

The corresponding error curve reveals $2 0 + 2 = 2 2$ points of equioscillation:

plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/ce8e5be65aa0e3ce8ba127374c5394c0f01ca8b05df5dda292cb52f4814ca2cf.jpg)

Here’s the analogous curve for degree 30, plotted on the same scale.

[p,err] $=$ minimax(f,30); plot $( \tt f - p )$ , hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/8ae0b68648d55d83481ff1b590333b589f91c45076e247be52091368be8dd475.jpg)

The algorithm underlying minimax, known as the Remez algorithm or the exchange algorithm, goes back to the Soviet mathematician Evgeny Remez in 1934 and is based on iteratively adjusting a trial alternant until it converges to a correct one [Remes 1934a, 1934b, Remez 1957; Powell 1981]. We shall not give details here, but in fact, Chebfun is an excellent platform for such computations since the algorithm depends on repeatedly finding the local extrema of trial error curves, an operation carried out easily via the roots command (see Chapter 18). Also crucial to the success of minimax is the use of the barycentric representation (5.11) for all polynomials, based not at Chebyshev points but at the points of each trial alternant [Filip et al. 2018]. (The observations of [Webb, Trefethen & Gonnet 2012] suggest that it might be better to use the “first barycentric formula” (5.9).)

The history of the Remez algorithm is interesting, or perhaps we should say the sociology. It stands out as one of the preeminent examples of a nontrivial algorithm for a nonlinear computational problem that was developed before the invention of computers. Perhaps in part because of this early appearance, it became remarkably well known, a fixture in numerical analysis courses worldwide. One might imagine, based on its fame, that the Remez algorithm must be very important in practice, but in fact it seems there is not much software and just a moderate amount of use of these ideas. One application has been in the design of routines for computing special functions [Cody, Fraser & Hart 1968, Cody 1993, Muller 2006]. Another is in the field of digital signal processing, where variants of the Remez ideas were developed by Parks and McClellan beginning in 1971 with tremendous success for designing low-pass, high-pass, and other digital filters [Parks & McClellan 1972]. Parks and McClellan too found that the use of a barycentric representation was crucial, as they describe memorably in [McClellan & Parks 2005].

Chapter 16 will show that Chebyshev interpolants are often as good as best approximations in practice, and this fact may have something to do with why the Remez algorithm is used rather rarely. Chapter 20 will show that if you really want a best approximation, it may be more practical to compute it by CF approximation than by the Remez algorithm, at least if $f$ is smooth. There are also other algorithms for computing best approximations, based, for example, on linear programming, which we shall not discuss.

Summary of Chapter 10. Any $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $p ^ { * } \in \mathcal { P } _ { n }$ with respect to the $\infty$ -norm. If $f$ is real, $p ^ { * }$ is characterized by having an error curve that equioscillates between at least $n + 2$ extreme points.

Exercise 10.1. A function with spikes. Compute numerically the degree 10 polynomial best approximation to $\mathrm { s e c h } ^ { 2 } ( 5 ( x + 0 . 6 ) ) + \mathrm { s e c h } ^ { 4 } ( 5 0 ( x + 0 . 2 ) ) + \mathrm { s e c h } ^ { 6 } ( 5 0 0 ( x - 0 . 2 ) )$ on $[ - 1 , 1 ]$ and plot $f$ together with $p ^ { * }$ as well as the error curve. What is the error? How does this compare with the error in 11-point Chebyshev interpolation?

Exercise 10.2. Best approximation of $| x |$ . (a) Use Chebfun to determine the errors $E _ { n } \ = \ \| f - p _ { n } \|$ in the degree $n$ best approximation of $f ( x ) \ = \ | x |$ on $[ - 1 , 1 ]$ for $n =$ $2 , 4 , 8 , \ldots , 2 5 6$ , and make a table of the values $\beta _ { n } ~ = ~ n E _ { n }$ as a function of $n$ . (b) Use Richardson extrapolation to improve your data. How many digits can you estimate for the limiting number $\beta = \mathrm { l i m } _ { n  \infty } \beta _ { n } \mathrm { : }$ (We shall discuss this problem in detail in Chapter 25.)

Exercise 10.3. de la Vall´ee Poussin lower bound. Suppose an approximation $p \in \mathcal { P } _ { n }$ to $f \in C ( [ - 1 , 1 ] )$ approximately equioscillates in the sense that there are points $- 1 \leq s _ { 0 } <$ $s _ { 1 } < \cdot \cdot \cdot < s _ { n + 1 } \leq 1$ at which $f - p$ alternates in sign with $| f ( s _ { j } ) - p ( s _ { j } ) | \geq \varepsilon$ for some $\varepsilon > 0$ . Show that $\| f - p ^ { * } \| \geq \varepsilon$ . (This estimate originates in [de la Vall´ee Poussin 1910].)

Exercise 10.4. Best approximation of even functions. Let $f \in C ( [ - 1 , 1 ] )$ be an even function, i.e., $f ( - x ) = f ( x )$ for all $_ x$ . (a) Prove as a corollary of Theorem 10.1 that for any $n \geq 0$ , the best approximation $\boldsymbol { p } _ { n } ^ { * }$ is even. (b) Prove that for any $n \geq 0$ , $p _ { 2 n } ^ { * } = p _ { 2 n + 1 } ^ { * }$ . (c) Conversely, suppose $f \in C ( [ - 1 , 1 ] )$ is not even. Prove that for all sufficiently large $n$ , its best approximations $\boldsymbol { p } _ { n } ^ { * }$ are not even.

Exercise 10.5. An invalid theorem. The first two figures of this chapter suggest the following “theorem”: if $f$ is an even function on $[ - 1 , 1 ]$ and $p ^ { * }$ is its best approximation of some degree $_ n$ , then one of the extreme points of $| ( f - p ^ { * } ) ( x ) |$ occurs at $x = 0$ . Pinpoint the flaw in the following “proof.” By the argument of Exercise 10.4(b), $p ^ { * }$ is the best approximation to $f$ for all $n$ in some range of the form even $\leq n \leq$ odd, such as $4 \leq n \leq 5$ or $1 0 \leq n \leq 1 3$ . By Theorem 10.1, the maximal number of equioscillation points of $f - p ^ { * }$ must accordingly be of the form $\mathrm { o d d } + 2$ , that is, odd. By symmetry, 0 must be one of these points. Exactly which of these three logical steps is invalid, and why?

Exercise 10.6. Nonlinearity of best approximation operator. We have mentioned that for given $_ n$ , the operator that maps a function $f \in C ( [ - 1 , 1 ] )$ to its best degree $n$ approximation $p _ { n } ^ { * }$ is nonlinear. Prove this (on paper, not numerically) by finding two functions $f _ { 1 }$ and $f _ { 2 }$ and an integer $n \geq 0$ such that the best approximation of the sum in $\mathcal { P } _ { n }$ is not the sum of the best approximations.

Exercise 10.7. Bernstein’s lethargy theorem. Exercise 6.1 considered a function of Weierstrass, continuous but nowhere differentiable. A variant of the same function based on Chebyshev polynomials would be

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } 2 ^ { - k } T _ { 3 ^ { k } } ( x ) .
$$

(a) Show that the polynomial $f _ { 3 ^ { k } }$ obtained by truncating (10.1) to degree $3 ^ { k }$ is the best approximation to $f$ in the spaces $\mathcal { P } _ { n }$ for certain $n$ . What is the complete set of $_ n$ for which this is true? What is the error? (b) Let $\left\{ \varepsilon _ { n } \right\}$ be a sequence decreasing monotonically to 0. Prove that there is a function $f \in C ( [ - 1 , 1 ] )$ such that $\| f - p _ { n } ^ { * } \| \geq \varepsilon _ { n }$ for all $_ n$ . (Hint: Change the coefficients $2 ^ { - k }$ of (10.1) to values related to $\left\{ \varepsilon _ { n } \right\}$ .)

Exercise 10.8. Continuity of best approximation operator. For any $n \geq 0$ , the mapping from functions $f \in C ( [ - 1 , 1 ] )$ to their best approximants $p ^ { * } \in \mathcal { P } _ { n }$ is continuous with respect to the $\infty$ -norm in $C ( [ - 1 , 1 ] )$ . Prove this by an argument combining the uniqueness of best approximations with compactness. (This continuity result appears in Section I.5 of [Kirchberger 1902]. In fact, the mapping is not just continuous but Lipschitz continuous, a property known as strong uniqueness, but this is harder to prove.)

Exercise 10.9. Approximation of $e ^ { x }$ . Truncating the Taylor series for $e ^ { x }$ gives polynomial approximations with maximum error $E _ { n } \sim 1 / ( n + 1 ) !$ ! on $[ - 1 , 1 ]$ , but the best

approximations do better by a factor of $2 ^ { n }$ :

$$
E _ { n } \sim \frac { 1 } { 2 ^ { n } ( n + 1 ) ! } , \quad n \to \infty .
$$

(a) Derive (10.2) by combining Exercises 3.15 and 10.3 with the asymptotic formula $I _ { k } ( 1 ) \sim$ $1 / ( 2 ^ { n } n ! )$ . (b) Make a table comparing this estimate with the actual values $E _ { n }$ computed numerically for $0 \leq n \leq 1 0$ .

Exercise 10.10. Alternative proof of uniqueness. Prove uniqueness of the degree $_ n$ best approximant to a real continuous function $f$ by a simpler argument than the one given in the proof of Theorem 10.1: suppose $p$ and $q$ are best approximants, and apply the equioscillation characterization to $r = ( p + q ) / 2$ .

Exercise 10.11. Chebyshev polynomials and best approximations. (a) What is the best degree $n$ polynomial approximation to $x ^ { n + 1 }$ on $[ - 1 , 1 ]$ ? What is the error? Derive the answers from Theorem 10.1, using the fact that $T _ { n + 1 }$ oscillates between values $\pm 1$ at $n + 2$ points in $[ - 1 , 1 ]$ . (b) What is the best approximation to 0 among monic polynomials of degree $n + 1$ ? What is the error?

Exercise 10.12. Every best approximant is an interpolant. Let $p$ be the best approximation in $\mathcal { P } _ { n }$ to a real function $f \in C ( [ - 1 , 1 ] )$ . Show that there exist $n + 1$ distinct points $- 1 < x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < 1$ such that $p$ is the interpolant in $\mathcal { P } _ { n }$ to $f$ in the points $\{ x _ { j } \}$ .

Exercise 10.13. A contrast to Faber’s theorem. Although Faber showed that there does not exist an array of nodes in $[ - 1 , 1 ]$ whose polynomial interpolants converge for every $f \in C [ - 1 , 1 ]$ , for any fixed $f$ there exists an array whose interpolants converge to $f$ [Marcinkiewicz 1936–37]. Prove this by combining the Weierstrass approximation theorem with the result of the previous exercise.

Exercise 10.14. Asymptotics of the leading coefficient. Let $\{ p _ { n } ^ { * } \}$ be the sequence of best approximations of a function $f \in C ( [ - 1 , 1 ] )$ , and let $p _ { n } ^ { * }$ have leading Chebyshev coefficient $a _ { n } ^ { * }$ . It is known that $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n  \infty } | a _ { n } ^ { * } | ^ { 1 / n } \leq 1 } \end{array}$ , with strict inequality if and only if $f$ is analytic on $[ - 1 , 1 ]$ [Blatt $\&$ Saff 1986, Thm. 2.1]. Verify this result numerically by estimating $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } | a _ { n } ^ { * } | ^ { 1 / n } } \end{array}$ for $f ( x ) = \left| x \right|$ and $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ .

# Chapter 11. Hermite Integral Formula

If there is a single most valuable mathematical tool in the analysis of accuracy of polynomial approximations, it is contour integrals in the complex plane.5 From a contour integral one can see why some approximations are extraordinarily good, like interpolation in Chebyshev points, and others are impossibly bad, like interpolation in equispaced points. This chapter presents the basics of the contour integrals, and the next applies them to take some first steps toward the subject of potential theory, which relates the accuracy of approximations to equipotential or minimal-energy problems for electrostatic charge distributions in the plane.

The starting ingredients have already appeared in Chapter 5. Following the formulation there, let $x _ { 0 } , \ldots , x _ { n }$ be a set of $n + 1$ distinct interpolation or “grid” points, which may be real or complex, and define the node polynomial $\ell \in \mathcal { P } _ { n + 1 }$ a s in (5.4) by

$$
\ell ( x ) = \prod _ { k = 0 } ^ { n } ( x - x _ { k } ) .
$$

Repeating (5.5), the function

$$
\ell _ { j } ( x ) = { \frac { \ell ( x ) } { \ell ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) } }
$$

is the Lagrange polynomial associated with $x _ { j }$ , that is, the unique polynomial in $\mathcal { P } _ { n }$ that takes the value 1 at $x _ { j }$ and $0$ at the other points $x _ { k }$ . Following (5.1), a linear combination of these functions gives the interpolant in $\mathcal { P } _ { n }$ to an arbitrary function

$f$ defined on the grid:

$$
p ( x ) = \sum _ { j = 0 } ^ { n } f ( x _ { j } ) \ell _ { j } ( x ) .
$$

We now make a crucial observation. Let $\Gamma _ { j }$ be a contour in the complex $x$ -plane that encloses $x _ { j }$ but none of the other grid points, nor the point $x$ . (By “encloses” we always mean that it winds around the specified set once in the counterclockwise direction, in the usual sense of complex variables.) Then the expression on the right in (11.2) can be written as

$$
{ \frac { \ell ( x ) } { \ell ^ { \prime } ( x _ { j } ) \left( x - x _ { j } \right) } } = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { j } } { \frac { \ell ( x ) } { \ell ( t ) ( x - t ) } } d t .
$$

To verify this formula we ignore the $\ell ( x )$ term on both sides, which has nothing to do with the integral, and use the fact that $1 / ( \ell ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) )$ is the residue of the function $1 / ( \ell ( t ) ( x - t ) )$ at the pole $t = x _ { j }$ .

From (11.2) and (11.4) we thus have an expression for $\ell _ { j } ( x )$ as a contour integral:

$$
\ell _ { j } ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma _ { j } } { \frac { \ell ( x ) } { \ell ( t ) ( x - t ) } } d t ,
$$

where $\Gamma _ { j }$ encloses $x _ { j }$ . Now let $\Gamma ^ { \prime }$ be a contour that encloses all of the grid points $\{ x _ { j } \}$ , but still not the point $x$ , and let $f$ be a function analytic on and interior to $\Gamma ^ { \prime }$ . Then we can combine these integrals to get an expression for the interpolant $p$ to $f$ in $\{ x _ { j } \}$ :

$$
p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma ^ { \prime } } { \frac { \ell ( x ) f ( t ) } { \ell ( t ) ( x - t ) } } d t .
$$

Note how neatly this formula replaces the sum of (11.3) by a contour integral with contributions from the same points $x _ { j }$ .

Now suppose we enlarge the contour of integration to a new contour $\Gamma$ that encloses $x$ as well as $\{ x _ { j } \}$ , and we assume $f$ is analytic on and inside $\Gamma$ . The residue of the integrand of (11.6) at $t = x$ is $- f ( x )$ , so this brings in a new contribution $- f ( x )$ to the integral, yielding an equation for the error in polynomial interpolation:

$$
p ( x ) - f ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( x ) f ( t ) } { \ell ( t ) ( x - t ) } } d t .
$$

And thus we have derived one of the most powerful formulas in all of approximation theory, the Hermite integral formula. This name comes from Hermite [1878], but nearly the same result was stated 52 years earlier by Cauchy [1826]. (Hermite, however, generalized the discussion significantly to nondistinct or “confluent” interpolation points and corresponding interpolation of derivatives as well as function values; see Exercise 11.2.)

Theorem 11.1. Hermite integral formula. Let $f$ be analytic in a region $\Omega$ containing distinct points $x _ { 0 } , \ldots , x _ { n }$ , and let $\Gamma$ be a contour in $\Omega$ enclosing these points in the positive direction. The polynomial interpolant $p \in \mathcal { P } _ { n }$ to $f$ at $\{ x _ { j } \}$ is

$$
p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { f ( t ) \left( \ell ( t ) - \ell ( x ) \right) } { \ell ( t ) \left( t - x \right) } } d t ,
$$

and if $_ { x }$ is enclosed by $\Gamma$ , the error in the interpolant is

$$
f ( x ) - p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( x ) } { \ell ( t ) } } { \frac { f ( t ) } { ( t - x ) } } d t .
$$

Proof. Equation (11.9) is the same as (11.7). For (11.8), we note that if $\Gamma$ encloses $x$ , then $f ( x )$ can be written

$$
f ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( t ) f ( t ) } { \ell ( t ) ( t - x ) } } d t ,
$$

and combining this with (11.7) gives the result. But the integrand of (11.8) has no pole at $t = x$ , so the same result also applies if $\Gamma$ does not enclose $x$ .

It is perhaps interesting to sketch Cauchy’s slightly different derivation from 1826, outlined in [Smithies 1997, p. 117], which may have been influenced by Jacobi’s thesis a year earlier [Jacobi 1825]. Cauchy started from the observation that $p ( x ) / \ell ( x )$ is a rational function with denominator degree greater than the numerator degree. This implies that it must be equal to the sum of the $n + 1$ inverse-linear functions $r _ { j } / ( x - x _ { j } )$ , where $r _ { j }$ is the residue of $p ( t ) / \ell ( t )$ at $t = x _ { j }$ (a partial fraction decomposition, to be discussed further in Chapter 23). Since $p$ interpolates $f$ at $\{ x _ { j } \}$ , $r _ { j }$ is also the residue of $f ( t ) / \ell ( t )$ at $t = x _ { j }$ . By residue calculus we therefore have

$$
{ \frac { p ( x ) } { \ell ( x ) } } = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma ^ { \prime } } { \frac { f ( t ) } { \ell ( t ) \left( x - t \right) } } d t
$$

if $\Gamma ^ { \prime }$ is again a contour that encloses the points $\{ x _ { k } \}$ but not $x$ itself, or equivalently, (11.6).

Now let us see how Theorem 11.1 can be used to estimate the accuracy of polynomial interpolants.

Suppose $f$ and $x$ are fixed and we want to estimate $f ( x ) - p ( x )$ for various degrees $n$ and corresponding sets of $n + 1$ points $\{ x _ { j } \}$ . On a fixed contour $\Gamma$ , the quantities $f ( t )$ and $t - x$ in (11.9) are independent of $n$ . The ratio

$$
{ \frac { \ell ( x ) } { \ell ( t ) } } = { \frac { \prod _ { j = 0 } ^ { n } ( x - x _ { j } ) } { \prod _ { j = 0 } ^ { n } ( t - x _ { j } ) } } ,
$$

however, is another matter. If $\Gamma$ is far enough from $\{ x _ { j } \}$ , then for each $t \in \Gamma$ , this ratio will shrink exponentially as $n \to \infty$ , and if this happens, we may conclude from (11.9) that $p ( x )$ converges exponentially to $f ( x )$ as $n \to \infty$ . The crucial condition for this argument is that it must be possible for $f$ to be analytically continued as far out as $\Gamma$ .

Here is a warm-up example mentioned on p. 63 of [Gaier 1987]. Suppose the interpolation points $\{ x _ { j } \}$ lie in $[ - 1 , 1 ]$ for each $n$ and $x \in \left[ { - 1 , 1 } \right]$ also. Let $S$ be the “stadium” in the complex plane consisting of all numbers lying at a distance $\leq 2$ from $[ - 1 , 1 ]$ , and suppose $f$ is analytic in a larger region $\Omega$ that includes a contour $\Gamma$ enclosing $S$ . We can sketch the situation like this:

$$
\begin{array} { l } { { { \bf x } = { \bf c h e b f u n } ( { \bf \Phi } ^ { \prime } { \bf x } ^ { \prime } ) ; ~ { \bf p l o t } ( { \bf r e a l } ( { \bf x } ) , \mathrm { i m a g ( { \bf x } ) } , { \bf \Phi } ^ { \prime } { \bf r } ^ { \prime } ) } } \\ { { \bf s e m i } = 2 * \exp ( 0 . 5 \mathrm { i } * { \bf p i } * { \bf x } ) ; ~ { \bf S } = { \bf \Phi } [ { \bf x } - 2 \mathrm { i } ; ~ 1 + \mathrm { s e m i } ; ~ 2 \mathrm { i } - { \bf x } ; ~ - 1 - \mathrm { s e m i } ] ; }  \\ { { \bf h o l d ~ o n } , ~ { \bf p l o t } ( { \bf S } , { \bf \Phi } ^ { \prime } { \bf k } ^ { \prime } ) , ~ { \bf z } = { \bf e x p } ( 1 \mathrm { i } * { \bf p i } * { \bf x } ) ; } \\ { { \bf G a m m a } = ( 2 . 8 + . 2 \mathrm { i } ) * ( { \bf s i n h } ( { \bf z } ) + . 5 * { \bf r e a l } ( { \bf z } ) ) ; ~ { \bf p l o t } ( \mathrm { G a m m a } , { \bf \Phi } ^ { \prime } { \bf b } ^ { \prime } ) }  \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/090cff5c4738302a6fcbdad53de7cd8f1a2262647cb46fe39db17c40c333d410.jpg)

Under these assumptions, there is a constant $\gamma > 1$ such that for every $t \in \Gamma$ and every $x _ { j }$ , $| t - x _ { j } | \geq \gamma | x - x _ { j } |$ . This implies

$$
| \ell ( x ) / \ell ( t ) | \leq \gamma ^ { - n - 1 } ,
$$

and thus by (11.9),

$$
\| f - p \| = O ( \gamma ^ { - n } ) .
$$

Note that this conclusion applies regardless of the distribution of the interpolation points in $[ - 1 , 1 ]$ . They could be equally spaced or random, for example. (At least that is true in theory. In practice, such choices would be undone by rounding errors on a computer, as we shall see in Chapter 13.)

So convergence of polynomial interpolants to analytic functions on $[ - 1 , 1 ]$ is all about how small $\ell ( x )$ is on $[ - 1 , 1 ]$ , compared with how big it is on a contour $\Gamma$ inside which $f$ is analytic. From this point of view we can begin to see why Chebyshev points are so good: because a polynomial with roots at the Chebyshev points has approximately uniform magnitude on $[ - 1 , 1 ]$ . Suppose, for example, we consider the polynomial $\ell \in \mathcal { P } _ { 8 }$ with roots at 8 Chebyshev points. On $[ - 1 , 1 ]$ it has size $O ( 2 ^ { - 8 } )$ , roughly speaking, but it grows rapidly for $x$ outside this interval. Here is a plot for $x \in [ - 1 . 5 , 1 . 5 ]$ :

$\tt { n p } = 8$ ; xj = chebpts(np); d = domain([-1.5,1.5]); ell = poly(xj,d); plot(ell) hold on, plot(xj,ell(xj),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/afe169c097c908d62ba4b88cfbff7e960b0d4a932919f120384b9d8e1fa1f44c.jpg)

With the MATLAB contour command we can examine the size of $\ell ( x )$ for complex values of $x$ . The following code plots contours at $| \ell ( x ) | = 2 ^ { - 6 } , 2 ^ { - 5 } , \ldots , 1$ .

$\mathtt { p l o t } ( \mathtt { x j } , \mathtt { e l l } ( \mathtt { x j } ) , \mathtt { \xi ^ { \prime } . k ^ { \prime } } )$ , hold on xgrid $= - 1 . 5 \colon . 0 2 \colon 1 . 5$ ; ygrid $=$ -0.9:.02:0.9; [xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ; ellzz $=$ ell(zz); levels $= \ 2 . \widehat { \ } ( - 6 : 0 )$ ; contour(xx,yy,abs(ellzz),levels,'k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/c40f562791a686ecdce074397048601bf36943b6a91d23b2f186af2ac7560a97.jpg)

We can see a great deal in this figure. On $[ - 1 , 1 ]$ , it confirms that $\ell ( x )$ is small, with maximum value $| \ell ( x ) | = 2 ^ { - 6 }$ at $x = 0$ . Away from $[ - 1 , 1 ]$ , $| \ell ( x ) |$ grows rapidly and takes constant values on curves that look close to ellipses. For $t$ on the outermost of the curves plotted, the ratio $| \ell ( x ) / \ell ( t ) |$ will be bounded by $2 ^ { - 6 }$ for any $x \in [ - 1 , 1 ]$ .

Let us compare this to the very different behavior if we take points that are not close to the Chebyshev distribution. To make a specific and quite arbitrary choice, let us again take 8 points, four of them at $^ { - 1 }$ and four at 1. Here is the plot on the real axis.

xj = [-1 -1 -1 -1 1 1 1 1]; ell $=$ poly(xj,d); plot(ell), hold on, plot(xj,ell(xj),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/735248b016b94bc01c6ecb06875918eb06e82c81ea69dfd0573119617f4f1c3d.jpg)

And here are the contours in the complex plane.

plot(xj,ell(xj),'.k'), hold on, ellzz $=$ ell(zz); contour(xgrid,ygrid,abs(ellzz),levels, $" \Bbbk ^ { \prime }$ )

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/9fc45111788ab22960429d13c7ae118b2fd5143e928513ab505ef2fc73aaee02.jpg)

These figures show that the size of $\ell ( x )$ on $[ - 1 , 1 ]$ is not at all uniform: it is far smaller than $2 ^ { - 6 }$ for $x \approx \pm 1$ , but as big as $1$ at $x = 0$ . Now, for $x \in [ - 1 , 1 ]$ and $t$ on the outermost curve shown, the maximum of the ratio $| \ell ( x ) / \ell ( t ) |$ is no better than 1 since that curve touches $[ - 1 , 1 ]$ . If we wanted to achieve $| \ell ( x ) / \ell ( t ) | \leq 2 ^ { - 6 }$ as in the last example, $\Gamma$ would have to be a much bigger curve—closer to the “stadium”:

xgrid = -2:.04:2; ygrid = -1.5:.04:1.5; [xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathsf { z } \mathsf { z } = \mathsf { x } \mathbf { x } \mathsf { + } 1 \mathrm { i } \ast \mathbf { y } \mathbf { y }$ ; ellzz $=$ ell(zz); levels $=$ $[ 2 \hat { \bf \Phi } 6 , 2 \hat { \bf \Phi } 6 ]$ ; hold on, contour(xgrid,ygrid,abs(ellzz),levels,'r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4e87f3763916a780709955cb00df5e640ab61cfe74abb1ec7b01d0710b1cc9a5.jpg)

The function $f$ would have to be analytic within this much larger region for the bound (11.9) to apply with a ratio $| \ell ( x ) / \ell ( t ) |$ as favorable as $2 ^ { - 6 }$ .

Summary of Chapter 11. The error of a polynomial interpolant can be represented by a contour integral in the complex plane, the Hermite integral formula. This provides the standard method for showing geometric convergence for certain approximations of analytic functions.

Exercise 11.1. Chebfun computation of Cauchy integrals. (a) Figure out (on paper) the polynomial $p \in \mathcal { P } _ { 2 }$ that takes the values $p ( - 1 ) = 1$ , $p ( 1 / 2 ) = 2$ , and $p ( 1 ) = 2$ . What is $p ( 2 )$ ? (b) Read about the numerical computation of Cauchy integrals in Chapter 5 of the online Chebfun Guide. Write a program to confirm Theorem 11.1 by computing $p ( 2 )$ numerically by a Cauchy integral for the function $f ( x ) = ( x + 1 ) ( x - 0 . 5 ) ( x - 1 ) e ^ { x } + 1 1 / 6 +$ $x / 2 - x ^ { 2 } / 3$ . Take both $| x | = 3 / 2$ and $| x | = 3$ as contours to confirm that it does not matter whether or not $\Gamma$ encloses $_ x$ . (c) Write an anonymous function $\mathfrak { p } \ : = \ : \mathfrak { Q } ( \mathbf { x } ) . . .$ to apply the above calculation not just for $x = 2$ but for arbitrary $_ x$ , and construct a chebfun on $[ - 1 , 1 ]$ from this anonymous function. Do its coefficients as reported by poly match your expectations?

Exercise 11.2. Confluent interpolation points. Modify the above problem to require $p ( - 1 ) = 1$ , $p ( 1 ) = 2$ , and $p ^ { \prime } ( 1 ) = 0$ . This is a Hermite interpolation problem, in which some interpolation points are specified multiply with corresponding values specified for derivatives. What is the analytic solution to this interpolation problem? Do the computations involving contour integrals and anonymous functions deliver the right result?

Exercise 11.3. Interpolation in a disk. Suppose a function $f$ is interpolated by polynomials in arbitrary points of the disk $| x | \leq r ^ { \prime }$ and we measure the accuracy $f ( x ) { - } p ( x )$ for $_ x$ in the disk $| x | \leq r$ . Show that geometric convergence is ensured (in exact arithmetic, ignoring rounding errors) if $f$ is analytic in the disk $| x | \le r + 2 r ^ { \prime }$ . Give the constant $\rho$ for convergence at the rate $O ( \rho ^ { - n } )$ . (This result originates with [M´eray 1884].)

Exercise 11.4. Working around a simple pole. Let $f$ be analytic on the closed Bernstein ellipse region $\overline { { E } } _ { \rho }$ for some $\rho > 1$ . It can be shown that $| \ell ( x ) / \ell ( t ) | = O ( \rho ^ { - n } )$ uniformly as $n \to \infty$ for $x \in [ - 1 , 1 ]$ and $t$ on the ellipse, and thus Theorem 11.1 can be used to show that $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ , as asserted by Theorem 8.2. Now suppose that $f$ has a finite number of singularities on the ellipse but these are just simple poles. Explain how the contour integral argument can be modified to show that the rate of convergence will still be $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ , as was established by another method in Exercise 8.15.

# Chapter 12. Potential Theory and Approximation

The explorations of the last chapter are glimmerings of potential theory in the complex plane, a subject that has been connected with approximation of functions at least since the work of Walsh early in the 20th century [Walsh 1969]. In this chapter we shall outline this connection. Potential theory in the complex plane is presented in [Ransford 1995] and [Finkelshtein 2006], and a survey of applications in approximation theory can be found in [Levin & Saff 2006].

We begin by looking again at (11.10), the formula giving the ratio of the size of the node polynomial $\ell$ at an approximation point $x$ to its size at a point $t$ o n a contour $\Gamma$ . Notice that the numerator and the denominator of this formula each contain a product of $n + 1$ terms. With this in mind, let us define $\gamma _ { n } ( x , t )$ as the following $( n + 1 ) \mathrm { s t }$ root:

$$
\gamma _ { n } ( x , t ) = { \frac { \left( \prod _ { j = 0 } ^ { n } | t - x _ { j } | \right) ^ { 1 / ( n + 1 ) } } { \left( \prod _ { j = 0 } ^ { n } | x - x _ { j } | \right) ^ { 1 / ( n + 1 ) } } } .
$$

Then the magnitude of the quotient in (11.10) becomes

$$
\left| \frac { \ell ( x ) } { \ell ( t ) } \right| = \gamma _ { n } ( x , t ) ^ { - n - 1 } .
$$

This way of writing things brings out a key point: if $\gamma _ { n } ( x , t )$ is bounded above $1$ , we will get exponential convergence as $n \to \infty$ . With this in mind, let us define $\alpha _ { n }$ to be the scalar

$$
\alpha _ { n } = \operatorname* { m i n } _ { x \in X , t \in \Gamma } \gamma _ { n } ( x , t ) ,
$$

where $x$ ranges over a domain $X$ where we wish to approximate $f$ (say, $X = [ - 1 , 1 ]$ ) and $t$ ranges over a contour $\Gamma$ enclosing that domain. If $\alpha _ { n } \geq \alpha$ for some $\alpha > 1$ for all sufficiently large $n$ , and if $f$ is analytic in the region bounded by $\Gamma$ , then (11.9) tells us that $p ( x )$ must converge to $f ( x )$ at the rate $O ( \alpha ^ { - n } )$ .

The condition $\alpha _ { n } > 1$ has a geometric interpretation. The numerator of (12.1) is the geometric mean distance of $t$ to the grid points $\{ x _ { j } \}$ , and the denominator is the geometric mean distance of $x$ to the same points. If $\alpha _ { n } > 1$ , then every point $t \in \Gamma$ is at least $\alpha _ { n }$ times farther from the grid points, in the geometric mean sense, than every point $x$ in the approximation domain. It is this property that allows the Hermite integral formula to show exponential convergence.

To bring these observations into potential theory, we linearize the products by taking logarithms. From (12.1) we find

$$
\log \gamma _ { n } ( x , t ) = \frac { 1 } { n + 1 } \sum _ { j = 0 } ^ { n } \log | t - x _ { j } | - \frac { 1 } { n + 1 } \sum _ { j = 0 } ^ { n } \log | x - x _ { j } | .
$$

Let us define the discrete potential function associated with the points $x _ { 0 } , \ldots , x _ { n }$ by

$$
u _ { n } ( s ) = { \frac { 1 } { n + 1 } } \sum _ { j = 0 } ^ { n } \log | s - x _ { j } | .
$$

Note that $u _ { n }$ is a harmonic function throughout the complex $s$ -plane away from the grid points, that is, a solution of the Laplace equation $\Delta u _ { n } = 0$ . We may think of each $x _ { j }$ as a point charge of strength $1 / ( n + 1 )$ , like an electron, and of $u _ { n }$ as the potential generated by all these charges, whose gradient defines an “electric” field. A difference from the electrical case is that whereas electrons repel one another with an inverse-square force, whose potential function is inverse-linear, here in the twodimensional plane the repulsion is inverse-linear and the potential is logarithmic. (Some authors put a minus sign in front of (12.5), so that the potential approaches $\infty$ rather than $- \infty$ as $s  x _ { j }$ , making $u _ { n }$ an energy rather than the negative of an energy.)

From (12.4) and (12.5) we find

$$
\log { \gamma _ { n } ( x , t ) } = u _ { n } ( t ) - u _ { n } ( x ) ,
$$

and hence by (12.2),

$$
\left| \frac { \ell ( x ) } { \ell ( t ) } \right| = e ^ { ( n + 1 ) [ u _ { n } ( x ) - u _ { n } ( t ) ] } .
$$

If $\alpha _ { n } \geq \alpha > 1$ for all sufficiently large $n$ , as considered above, then $\log { \gamma _ { n } ( x , t ) } \geq$ $\log \alpha _ { n } \geq \log \alpha > 0$ , so we have

$$
\operatorname* { m i n } _ { t \in \Gamma } u _ { n } ( t ) - \operatorname* { m a x } _ { x \in X } u _ { n } ( x ) \geq \log \alpha .
$$

Together with (11.9) this implies

$$
\| f - p \| = O ( e ^ { - n \log \alpha } ) .
$$

Notice the flavor of this result: the interpolants converge exponentially, with a convergence constant that depends on the difference of the values taken by the potential function on the set of points where the interpolant is to be evaluated and on a contour inside which $f$ is analytic.

We now take the step from discrete to continuous potentials. Another way to write (12.5) is as a Lebesgue–Stieltjes integral [Stein $\&$ Shakarchi 2005],

$$
u ( s ) = \int _ { - 1 } ^ { 1 } \log | s - \tau | d \mu ( \tau ) ,
$$

where $\mu$ is a measure consisting of a sum of Dirac delta functions, each of strength $1 / ( n + 1 )$ ,

$$
\mu ( \tau ) = \frac { 1 } { n + 1 } \sum _ { j = 0 } ^ { n } \delta ( \tau - x _ { j } ) .
$$

This is the potential or logarithmic potential associated with the measure $\mu$ . The same formula (12.7) also applies if $\mu$ is a continuous measure, which will typically be obtained as the limit of a family of discrete measures as $n  \infty$ . (The precise notion of convergence appropriate for this limit is known as weak $^ *$ convergence, pronounced “weak-star.”) Equally spaced grids in $[ - 1 , 1 ]$ converge to the limiting measure

$$
\mu ( \tau ) = \frac { 1 } { 2 } .
$$

Chebyshev grids in $[ - 1 , 1 ]$ converge to the Chebyshev measure identified in Exercise 2.2,

$$
\mu ( \tau ) = \frac { 1 } { \pi \sqrt { 1 - \tau ^ { 2 } } } ,
$$

and so do other grids associated with zeros or extrema of orthogonal polynomials on $[ - 1 , 1 ]$ , such as Legendre, Jacobi, or Gegenbauer polynomials (see Chapter 17).

And now we can identify the crucial property of the Chebyshev measure (12.10): The potential (12.7) it generates is constant on $[ - 1 , 1 ]$ . The measure is known as the equilibrium measure for $\lfloor - 1 , 1 \rfloor$ , and physically, it corresponds to one unit of charge adjusting itself into an equilibrium, minimal-energy distribution. Given a unit charge distribution $\mu$ with support on $[ - 1 , 1 ]$ , the associated energy is the integral

$$
I ( \mu ) = - \int _ { - 1 } ^ { 1 } u ( s ) d \mu ( s ) = - \int _ { - 1 } ^ { 1 } \int _ { - 1 } ^ { 1 } \log | s - \tau | d \mu ( \tau ) d \mu ( s ) .
$$

It is clear physically, and can be proved mathematically, that for $I ( \mu )$ to be minimized, $u ( s )$ must be constant, so the gradient of the potential is zero and there are no net forces on the points in $( - 1 , 1 )$ [Ransford 1995].

This discussion has gone by speedily, and the reader may have to study these matters several times to appreciate how naturally ideas associated with electric charges connect with the accuracy of polynomial approximations. Potential theory is also of central importance in the study of approximation by rational functions; see [Levin $\&$ Saff 2006] and [Stahl $\&$ Schmelzer 2009].

We have just characterized the equilibrium measure $\mu$ for interpolation on $[ - 1 , 1 ]$ as the unit measure on $[ - 1 , 1 ]$ that generates a potential $u$ that takes a constant value. To be precise, $u$ is the solution to the following problem involving a Green’s function: find a function $u ( s )$ in the complex $s$ -plane that is harmonic outside $[ - 1 , 1 ]$ , approaches a constant value as $s  [ - 1 , 1 ]$ , and is equal to $\log | s | + O ( s ^ { - 1 } )$ as $s \to \infty$ . (This last condition comes from the property that the total amount of charge is 1.) Quite apart from the motivation from approximation theory, suppose we are given this Green’s function problem to solve. Since Laplace’s equation is invariant under conformal maps, the solution can be derived by introducing a conformal map that transplants the exterior of the interval to the exterior of a disk, taking advantage of the fact that the Green’s function problem is trivial on a disk. Such a mapping is the function

$$
z = \phi ( s ) = { \frac { 1 } { 2 } } ( s + i \sqrt { 1 - s ^ { 2 } } ) ,
$$

which maps the exterior of $[ - 1 , 1 ]$ in the $s$ -plane onto the exterior of the disk $| z | \leq$ $1 / 2$ in the $z$ -plane. There, the solution of the potential problem is $\log | z |$ . Mapping back to $s$ , we find that the Chebyshev potential is given by $u ( s ) = \log | \phi ( s ) |$ , that is,

$$
u ( s ) = \log | s + i \sqrt { 1 - s ^ { 2 } } | - \log 2 ,
$$

with constant value $u ( s ) = - \log 2$ on $[ - 1 , 1 ]$ .

By definition, the Green’s function has a constant value on $[ - 1 , 1 ]$ , namely $u ( s ) =$ $- \log 2$ . For values $u _ { 0 } > - \log 2$ , the equation $u ( s ) = u _ { 0 }$ defines an equipotential curve enclosing $[ - 1 , 1 ]$ that is exactly the Bernstein ellipse $E _ { \rho }$ with $\rho = 2 \exp ( u _ { 0 } )$ , as defined in Chapter 8. Here is a contour plot of (12.13), confirming that the contours look the same as the ellipses plotted there. The factor $\mathtt { s i g n } ( \mathrm { i m a g } ( \mathbf { s } ) )$ is included to make $\mathbf { u }$ return the correct branch of the square root for $\mathrm Ḋ s Ḍ < 0$ .

u = @(s) log(abs(s+1i\*sign(imag(s)).\*sqrt(1-s.^2))) - log(2);   
xgrid = -1.5:.02:1.5; ygrid $=$ -0.91:.02:0.91;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); ss $=$ xx+1i\*yy; uss $=$ u(ss);   
levels $=$ -log(2) + log(1.1:0.1:2);   
contour(xgrid,ygrid,uss,levels,'k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f02a656d73d03252be05c615386be61c1403cddad82c6f977c049a4c1974549c.jpg)

The constant $- \log 2$ in (12.13) is a reflection of the length of the interval $[ - 1 , 1 ]$ . Specifically, this constant is the logarithm of the capacity (or logarithmic capacity or transfinite diameter ) of $[ - 1 , 1 ]$ ,

$$
c = { \frac { 1 } { 2 } } .
$$

The capacity is a standard notion of potential theory, and in a simply connected two-dimensional case like this one, it can be defined as the radius of the equivalent disk. The associated minimal energy is the Robin constant of $[ - 1 , 1 ]$ :

$$
\operatorname* { m i n } _ { \mu } I ( \mu ) = - \log ( c ) = \log 2 .
$$

The fact that the capacity of $[ - 1 , 1 ]$ is $1 / 2$ has the following interpretation, explored earlier in Exercise 2.6. For Chebyshev or other asymptotically optimal grids on $[ - 1 , 1 ]$ , in the limit $n  \infty$ , each grid point lies at a distance $1 / 2$ from the others in the geometric mean sense.

This is a book about approximation on intervals, but it is worth noting that all these ideas of equilibrium measure, minimal energy, Robin constant, and capacity generalize to other compact sets $E$ in the complex plane. If $E$ is connected, then $\mu$ and $u$ can be obtained from a conformal map of its exterior onto the exterior of a disk, whereas if it is disconnected, a more general Green’s function problem may be solved. In any case, the equilibrium measure, which is supported on the outer boundary of $E$ , describes a good asymptotic distribution of interpolation points as $n \to \infty$ , and the limiting geometric mean distance from one point to the others is equal to the capacity, which is related to the Robin constant by $c ( E ) =$ $\mathrm { e x p } ( - \mathrm { m i n } _ { \mu } I ( \mu ) )$ .

Having discussed the continuous limit, let us return to the finite problem of finding good sets of $n + 1$ points $\{ x _ { j } \}$ for interpolation by a polynomial $p \in \mathcal { P } _ { n }$ on a compact set $E$ in the complex plane. Three particular families of points have received special attention. We say that $\{ x _ { j } \}$ is a set of Fekete points for the given $n$ and $E$ if the quantity

$$
{ \bigg ( } \prod _ { j < k } | x _ { j } - x _ { k } | { \bigg ) } ^ { 2 / n ( n + 1 ) } ,
$$

which is the geometric mean of the distances between the points, is as large as possible, that is, the points are exactly in a minimal-energy configuration. As $n  \infty$ , these maximal quantities decrease monotonically to $c ( E )$ , the fact which gives rise to the expression “transfinite diameter.” As a rule Fekete points have some of the cleanest mathematical properties for a given set $E$ but are the hardest to compute numerically. Next, if $E$ is connected and $\phi ( x )$ is a map of its exterior to the exterior of a disk in the $z$ -plane centered at the origin, a set of Fej´er points is a set $\phi ^ { - 1 } ( \{ z _ { j } \} )$ , where $\{ z _ { j } \}$ consists of any $n + 1$ points spaced equally around the boundary circle. Fej´er points are more readily computable since it is often possible to get one’s hands on a suitable mapping $\phi$ . Finally, Leja points are approximations to Fekete points obtained by a “greedy algorithm.” Here, one starts with an arbitrary first point $x _ { 0 } \in E$ and then computes successive points $x _ { 1 } , x _ { 2 } , \dotsc$ by an incremental version of the Fekete condition: with $x _ { 0 } , \ldots , x _ { n - 1 }$ known, $x _ { n }$ is chosen to maximize the same quantity (12.14) or, equivalently, to maximize

$$
\prod _ { j = 0 } ^ { n - 1 } | x _ { j } - x _ { n } | .
$$

All three of these families of points can be shown, under reasonable assumptions, to converge to the equilibrium measure as $n \to \infty$ , and all work well in practice for interpolation. A result showing near-optimality of Leja points for interpolation on general sets in the complex plane can be found in [Taylor $\&$ Totik 2010].

In Chapter 8 we proved a precise theorem (Theorem 8.2): if $f$ is analytic and bounded by $M$ in the Bernstein ellipse $E _ { \rho }$ , then $\| f - p _ { n } \| \leq 4 M \rho ^ { - n } / ( \rho - 1 )$ , where $p _ { n } \in \mathcal { P } _ { n }$ is the interpolant in $n + 1$ Chebyshev points. The proof made use of the Chebyshev expansion of $f$ and the aliasing properties of Chebyshev polynomials at

Chebyshev points. By the methods of potential theory and the Hermite integral formula discussed in this chapter one can derive a much more general theorem to similar effect. For any set of $n + 1$ nodes in $\lfloor - 1 , 1 \rfloor$ , let $\ell \in \mathcal P _ { n + 1 }$ be the node polynomial (5.4), and let $\begin{array} { r } { M _ { n } = \operatorname* { s u p } _ { x \in [ - 1 , 1 ] } | \ell ( x ) | } \end{array}$ . A sequence of grids of $1 , 2 , 3 , \ldots$ interpolation nodes is said to be uniformly distributed on $[ - 1 , 1 ]$ if it satisfies

$$
\operatorname* { l i m } _ { n  \infty } M _ { n } ^ { 1 / n } = \frac { 1 } { 2 } .
$$

(On a general set $E$ , the number $1 / 2$ becomes the capacity.)

Theorem 12.1. Interpolation in uniformly distributed points. Given $f \in C ( [ - 1 , 1 ] )$ , let $\rho$ ( $1 \le \rho \le \infty$ ) be the parameter of the largest Bernstein ellipse $E _ { \rho }$ to which $f$ can be analytically continued, and let $\{ p _ { n } \}$ be the interpolants to $f$ in any sequence of grids in $[ - 1 , 1 ]$ uniformly distributed as defined above. Then the errors satisfy

$$
\operatorname* { l i m } _ { n \to \infty } \| f - p _ { n } \| ^ { 1 / n } = \rho ^ { - 1 } .
$$

Proof. See Chapter 2 of [Gaier 1987].

A set of polynomials satisfying (12.16) is said to be maximally convergent. Examples of such polynomials are interpolants through most systems of roots or extrema of Legendre, Chebyshev, or Gauss–Jacobi points; the convergence rates of such systems differ only at the margins, in possible algebraic factors like $n$ or $\log n$ .

Summary of Chapter 12. Potential theory provides a powerful tool for studying the behavior of polynomial approximations in the limit $n  \infty$ . Polynomial interpolants to analytic functions on $[ - 1 , 1 ]$ converge geometrically if the grids are uniformly distributed according to the Chebyshev distribution.

Exercise 12.1. Fekete points in an interval. It can be shown that the equilibrium configuration for $n + 1$ points in $[ - 1 , 1 ]$ consists of the roots of $( x ^ { 2 } - 1 ) P _ { n - 1 } ^ { ( 1 , 1 ) } ( x )$ , where $P _ { n - 1 } ^ { ( 1 , 1 ) }$ is the degree $n - 1$ Jacobi polynomial with parameters $( 1 , 1 )$ [Stieltjes 1885] (see Chapter 17). (An equivalent statement is that the points lie at the local extrema in $[ - 1 , 1 ]$ of the Legendre polynomial of degree $n + 1$ .) Thus $( x ^ { 2 } - 1 ) P _ { n - 1 } ^ { ( 1 , 1 ) } ( x )$ is the degree $n - 1$ Fekete polynomial in $[ - 1 , 1 ]$ . Verify numerically using the Chebfun jacpts command that in the case $n = 1 0$ , the net forces on the 9 interior points are zero.

Exercise 12.2. Capacity of an ellipse. Let $E$ be an ellipse in the complex plane of semiaxis lengths $a$ and $^ { b }$ . Show that $c ( E ) = ( a + b ) / 2$ .

Exercise 12.3. Leja points and capacity. Let $E$ be the “half-moon” set consisting of the boundary of the right half of the unit disk. Write a code to compute a sequence of 100 Leja points for this set. To keep things simple, begin by approximating the boundary by a discrete set of 1000 points. What approximation of the capacity of $E$ do your points provide? (The exact answer is $4 / 3 ^ { 3 / 2 }$ , as discussed with other examples and algorithms in [Ransford 2010].)

# Chapter 13. Equispaced Points, Runge Phenomenon

So far in this book, we have considered three good methods for approximating functions by polynomials: Chebyshev interpolation, Chebyshev projection, and best approximation. Now we shall look at a catastrophically bad method!—interpolation in equally spaced points. This procedure is so unreliable that, for generations, it has tainted people’s views of the whole subject of polynomial interpolation. The mathematical tools we will need to understand what is going on are the Hermite integral formula and potential theory, as discussed in the last two chapters.

As mentioned in Chapter 5, polynomial interpolation was an established tool by the 19th century. The question of whether polynomial interpolants would converge to an underlying function as $n  \infty$ was not given much attention. Presumably many mathematicians would have supposed that if the function was analytic, the answer would be yes. In 1884 and 1896, M´eray published a pair of papers in which he identified the fact that certain interpolation schemes do not converge [M´eray 1884 & 1896]. In the first paper he writes

It is rather astonishing that practical applications have not yet turned up any cases in which the interpolation is illusory.6

M´eray’s derivations had the key idea of using the Hermite integral formula. However, the examples he devised were rather contrived, and his idiosyncratically written papers had little impact. It was Runge in 1901 who made the possibility of divergence famous by showing that divergence of interpolants occurs in general even for equispaced points in a real interval and evaluation points in the interior of that interval [Runge 1901].

Runge illustrated his discovery with an example that has become known as the Runge function: $1 / ( 1 + x ^ { 2 } )$ on $[ - 5 , 5 ]$ or, equivalently, $1 / ( 1 + 2 5 x ^ { 2 } )$ on $[ - 1 , 1 ]$ :

We already know from Chapter 8 that there is nothing wrong with this function for polynomial interpolation in Chebyshev points: $f$ is analytic, and the polynomial interpolants converge geometrically. Now, however, let us follow Runge and look at interpolants in equally spaced points, which we can compute using the Chebfun overload of the MATLAB interp1 command.

Here is what we get with 8 points:

s = linspace(-1,1,8); $\mathrm { ~ p ~ } =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/220391880c7937795d2a9af13b48ce80b6fa12e0d2e8136eeb3914781a7ef305.jpg)

Here is the result for 16 points:

s = linspace(-1,1,16); $\mathtt { p } \ =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/272777894d27087f9e71a2990d29c2cf75494c5ceeda3cb53c0548f33b6447c4.jpg)

Is this going to converge as $n \to \infty$ ? Things look pretty good in the middle but not so good at the edges. Here is the result for 20 points:

s = linspace(-1,1,20); $\mathtt { p } \ =$ chebfun.interp1(s,f); plot(f), hold on, plot(p,'r'), plot(s,p(s),'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/9c9ccb320d97d2b57b1ec070a2ef7573c0bc77d622225af921e473a48166ef48.jpg)

What is happening is exponential convergence in the middle of the interval but exponential divergence near the ends. The next figure shows the maximum error over $[ - 1 , 1 ]$ as a function of the number of points. We get a hint of convergence at first, but after $n = 1 0$ , things just get worse. Note the log scale.

f $\begin{array} { r l } & { \mathsf { e } ~ = ~ \left[ \mathsf { J } \right] ; ~ \mathrm { n n } ~ = ~ 2 { : 2 : 5 0 } ; } \\ & { \mathsf { o r } ~ \mathrm { n p } ~ = ~ \mathrm { n n } } \\ & { ~ \mathsf { s } ~ = ~ \mathrm { 1 i n s p a c e } ( - 1 , 1 , \mathrm { n p } ) ; ~ \mathsf { p } ~ = ~ \mathrm { c h e b f u n . i n t e r p 1 } ( \mathsf { s } , \mathsf { f } ) ; } \\ & { \mathsf { e e } ~ = ~ \left[ \mathsf { e e } ~ \mathrm { n o r m } ( \mathsf { f } \mathrm { - p } , \mathrm { i n f } ) \right] ; } \end{array}$   
end   
semilogy(nn,ee,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/7b0de94fd102b98c6ad7e5f80670335e81c7c370a08e420e707bdfb4f86efd8e.jpg)

By now the reader may have suspected that what is going wrong here can be understood by looking at potentials, as in the last two chapters. Here is an adaptation of a code segment from Chapter 11 to plot equipotential curves for $n + 1 = 8$ and 20.

d = domain([-1.5,1.5]);   
xgrid $=$ -1.5:.02:1.5; ygrid $=$ -1:.02:1;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ;   
for np $=$ [8 20] xj $=$ linspace(-1,1,np); ell $=$ poly(xj,d); plot(xj,ell(xj),'.k') hold on, ellzz $=$ ell(zz); levels $=$ ((1.25:.25:3)/exp(1)).^np; contour(xx,yy,abs(ellzz),levels,'k')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/3742bbf26473d69b848b293749f91a2c79ff984b9790bb0715ec8cfeb35e8ac7.jpg)  
Level curves of $\| ( { \boldsymbol { \mathsf { x } } } ) \|$ for 8 equispaced points

What we see here is that $[ - 1 , 1 ]$ is very far from being a level curve for equispaced interpolation points. From the last two chapters, we expect serious consequences of this irregularity. In the second plot just shown, for example, it is the fourth curve (from inside out) that approximately touches the endpoints $\pm 1$ . For Theorem 11.1 to be of any use in such a landscape, $f$ will have to be analytic in a region larger than the “football” enclosed by that curve. Analyticity on $[ - 1 , 1 ]$ is not enough for convergence; we will need analyticity in a much bigger region of the complex plane. This is what Runge discovered in 1901.

Following the method of the last chapter, we now consider the limit $n  \infty$ , where the distribution of interpolation points approaches the constant measure (12.9),

$$
\mu ( \tau ) = \frac { 1 } { 2 } .
$$

The potential (12.7) associated with this measure is

$$
u ( s ) = - 1 + { \frac { 1 } { 2 } } \mathrm { R e } \left[ ( s + 1 ) \log ( s + 1 ) - ( s - 1 ) \log ( s - 1 ) \right] .
$$

Here is a code that plots just one level curve of this potential, the one passing through $\pm 1$ , where the value of the potential is $- 1 + \log 2$ .

$\begin{array} { r l } & { \mathrm { x 1 ~ = ~ - 1 . 6 5 : ~ } . 0 2 : 1 . 6 5 ; \mathrm { y 1 ~ = ~ - 0 . 7 : ~ } . 0 2 : 0 . 7 ; } \\ & { \mathrm { [ x x , y y ] ~ = ~ m e s h g r i d } ( \mathrm { x 1 } , \mathrm { y 1 } ) ; \mathrm { s s ~ = ~ x x + 1 i * y y ; } } \\ & { \mathrm { u ~ = ~ } \varnothing ( \mathtt { s } ) - 1 + 0 . 5 * \mathrm { r e a l } ( ( \mathtt { s } + 1 ) . * \mathrm { l o g } ( \mathtt { s } + 1 ) - ( \mathtt { s } - 1 ) . * \mathrm { l o g } ( \mathtt { s } - 1 ) ) ; } \\ & { \mathrm { c o n t o u r } ( \mathrm { x 1 } , \mathrm { y 1 } , \mathrm { u } ( \mathtt { s } \mathtt { s } ) , ( - 1 + \mathrm { l o g } ( 2 ) ) * [ 1 \ 1 ] , \mathrm { \xi } ^ { \mathrm { , ~ } } \mathrm { k } ^ { \prime } ) } \end{array}$ hold on, plot(.5255i,'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d5b237d98f9f8c9cc5858e8678ca2e39b45fc99a482b8bada4b7addf7223900b.jpg)

For the interpolants to a function $f$ in equispaced nodes to converge as $n \to \infty$ for all $x \in [ - 1 , 1 ]$ , $f$ must be analytic, not just on $[ - 1 , 1 ]$ but throughout this Runge region, which crosses the real axis at $\pm 1$ and the imaginary axis at $\pm 0 . 5 2 5 5 2 4 9 1 4 5 7 \ldots i$ . Runge reports this number correctly to 4 digits and writes

The curve has somewhat the shape of an ellipse. At the ends of the long axis, however, our curve is more pointed than an ellipse.7

Here are the values of (13.2) at the endpoints and the middle:

$$
u ( \pm 1 ) = - 1 + \log 2 , \quad u ( 0 ) = - 1 ;
$$

thus

$$
\exp ( u ( \pm 1 ) ) = \frac { 2 } { e } , \quad \exp ( u ( 0 ) ) = \frac { 1 } { e } .
$$

These numbers indicate that in the limit $n  \infty$ , the endpoints of an equispaced grid in $[ - 1 , 1 ]$ lie at an average distance $2 / e$ from the other grid points, in the geometric mean sense, whereas the midpoint lies at an average distance of just $1 / e$ . As emphasized in the last chapter, notably in (12.6), the effect of such a discrepancy grows exponentially with $n$ .

Here are some examples. Equispaced interpolation will converge (in the absence of rounding errors) throughout $[ - 1 , 1 ]$ for $f ( x ) = \exp ( - x ^ { 2 } )$ , which is analytic everywhere, and for $f ( x ) = ( 1 + x ^ { 2 } ) ^ { - 1 }$ , which has poles at $\pm i$ . On the other hand, it will not converge for $f ( x ) = ( 1 + 1 6 x ^ { 2 } ) ^ { - 1 }$ , which has poles at $\pm i / 4$ . It will converge slowly for $f ( x ) = ( 1 + ( x / 0 . 5 3 ) ^ { 2 } ) ^ { - 1 }$ and diverge slowly for $f ( x ) = ( 1 + ( x / 0 . 5 2 ) ^ { 2 } ) ^ { - 1 }$ (Exercise 13.3).

The worst-case rate of divergence is $2 ^ { n }$ , and this rate will generally appear if $f$ is not analytic on $[ - 1 , 1 ]$ . To be precise, for such a function the errors will be of size $O ( 2 ^ { n } )$ as $n \to \infty$ but not of size $O ( C ^ { n } )$ for any $C < 2$ . Here, for example, we take $f$ to be a hat function, with just one derivative of bounded variation. The dots show errors in Chebyshev interpolation, converging at the rate $O ( n ^ { - 1 } )$ in keeping with Theorem 7.2, and the crosses show errors in equispaced interpolation, with a dashed line parallel to $2 ^ { n }$ for comparison.

pequi $=$ chebfun.interp1(s,f); eequi $=$ [eequi norm(f-pequi,inf)]; pcheb $=$ chebfun(f, $\tt { n } { + } 1$ ); echeb $=$ [echeb norm(f-pcheb,inf)]; end semilogy(nn,2.^(nn-12),'--r'), hold on semilogy(nn,eequi,'x-r'), semilogy(nn,echeb,'.-b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/1cd234b3c0d20801cabea992bcbeb832a43c65b31b0f5d428fad9289ebf4d9fb.jpg)

All of the above remarks about equispaced interpolation concern the ideal mathematics of the problem. On a computer in floating point arithmetic, however, a further complication arises: even if convergence ought to take place in theory, rounding errors will be amplified by $O ( 2 ^ { n } )$ , causing divergence in practice. Here, for example, are the errors in equispaced and Chebyshev interpolation of the entire function $\exp ( x )$ :

${ \textbf { f } } = \exp \left( \mathbf { x } \right)$ ; eequi $=$ []; echeb $=$ []; nn = 2:2:80;   
for $\texttt { n } = \texttt { n n }$ s $=$ linspace(-1,1,n+1); pequi $=$ chebfun.interp1(s,f); eequi $=$ [eequi norm(f-pequi,inf)]; pcheb $=$ chebfun(f, $\ n { + } 1 $ ); echeb $=$ [echeb norm(f-pcheb,inf)];   
end   
semilogy $\left( \operatorname { n n } , 2 . { \hat { \mathbf { \phi } } } ( \operatorname { n n - 5 0 } ) , \mathbf { \mu } ^ { * } - \mathbf { - r } \mathbf { \mu } ^ { * } \right)$ , hold on   
semilogy(nn,eequi, $\mathbf { \partial } ^ { \prime } \mathbf { x } \mathbf { - } \mathbf { r } ^ { \prime } \mathbf { \partial } .$ ), semilogy(nn,echeb,'.-b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4d86eea9a01b201af78e3728e92ab79faf74d1ad29b4d948372bcae93131ed96.jpg)

In exact arithmetic we would see convergence for both sets of points, but on the computer the divergence for equispaced points sets in early. The rate is cleanly $O ( 2 ^ { n } )$ until we reach $O ( 1 )$ . Notice that the line of crosses, if extended backward to $n = 0$ , meets the $y$ -axis at approximately $1 0 ^ { - 1 8 }$ , i.e., a digit or two below machine precision.

The $2 ^ { n }$ divergence of equispaced polynomial interpolants is a fascinating subject, and we must remind ourselves that one should only go into so much detail in analyzing a method that should never be used! But perhaps we should qualify that “never” in one respect. As Runge himself emphasized, though interpolants in equispaced points do not converge on the whole interval of interpolation, they may still do very well near the middle. In the numerical solution of differential equations, for example, higher-order centered difference formulas are successfully used based on 5 or 7 equally spaced grid points. A less happy example would be Newton–Cotes quadrature formulas, based on polynomial interpolation in equally spaced points, where the $O ( 2 ^ { n } )$ effect is unavoidable and causes serious problems for larger $n$ and divergence as $n \to \infty$ , as first proved by P´olya [1933]. We shall discuss quadrature in Chapter 19.

We close this chapter with an observation that highlights the fundamental nature of the Runge phenomenon and its associated mathematics. Suppose you want to persuade somebody that it is important to know something about complex variables, even for dealing with real functions. I still remember the argument my calculus teacher explained to me: to understand why the Taylor series for $1 / ( 1 + x ^ { 2 } )$ converges only for $- 1 < x < 1$ , you need to know that Taylor series converge within disks in the complex plane, and that this function has poles at $\pm i$ .

Runge’s observation is precisely a generalization of this fact to interpolation points equispaced in an interval rather than all at $x \ = \ 0$ . The convergence or divergence of polynomial interpolants to a function $f$ again depends on whether $f$ is analytic in a certain region; the change is that the region is now not a disk but elongated. Even the phenomenon of divergence in floating point arithmetic for functions whose interpolants “ought” to converge is a generalization of familiar facts from real arithmetic. Just try to evaluate $\exp ( x )$ on a computer for $x = - 2 0$ using the Taylor series!

Summary of Chapter 13. Polynomial interpolation in equispaced points is exponentially ill-conditioned: the interpolant $p _ { n }$ may have oscillations near the edge of the interval nearly $2 ^ { n }$ times larger than the function $f$ being interpolated, even if $f$ is analytic. In particular, even if $f$ is analytic and the interpolant is computed exactly without rounding errors, $p _ { n }$ need not converge to $f$ as $n \to \infty$ .

Exercise 13.1. Three examples. Draw plots comparing accuracy of equispaced and Chebyshev interpolants as functions of $n$ for $\exp ( x ^ { 2 } )$ , $\exp ( - x ^ { 2 } )$ , $\exp ( - 1 / x ^ { 2 } )$ .

Exercise 13.2. Computing geometric means in Chebfun. (a) What output is produced by the program below? (b) Why?

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x',[0 1]);   
f $=$ chebfun(@(y) prod(abs(x-1i\*y)),[0.1 1]); roots(f-2/exp(1))

Exercise 13.3. Borderline convergence. The claim was made in the text that equispaced polynomial interpolants on $[ - 1 , 1 ]$ converge for $f ( x ) = ( 1 + ( x / 0 . 5 3 ) ^ { 2 } ) ^ { - 1 }$ and diverge for $f ( x ) = ( 1 + ( x / 0 . 5 2 ) ^ { 2 } ) ^ { - 1 }$ . Can you observe this difference numerically? Run appropriate experiments and discuss the results.

Exercise 13.4. Approaching the sinc function. The sinc function is defined for all $_ x$ by $S ( x ) = \sin ( \pi x ) / ( \pi x )$ (and $S ( 0 ) = 1$ ). For any $n \geq 1$ , an approximation to $S$ is given

by

$$
S _ { n } = \prod _ { k = 1 } ^ { n } ( 1 - x ^ { 2 } / k ^ { 2 } ) .
$$

Construct $S _ { 2 0 }$ in Chebfun on the interval $[ - 2 0 , 2 0 ]$ and compare it with $S$ . On what interval around $x = 0$ do you find $| S _ { 2 0 } ( x ) - S ( x ) | < 0 . 1 ?$ (It can be shown that for every $_ x$ , $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } S _ { n } ( x ) = S ( x ) } \end{array}$ .)

Exercise 13.5. Barycentric weights and ill-conditioning. (a) Suppose a function is interpolated by a polynomial in $n + 1$ equispaced points in $[ - 1 , 1 ]$ , with $n$ even. From the result of Exercise 5.6, derive a formula for the ratio of the barycentric weights at the midpoint $x = 0$ and the endpoint $x = 1$ . (b) With reference to the barycentric formula (5.11), explain what this implies about sensitivity of these polynomial interpolants to perturbations in the data at $x = 0$ .

# Chapter 14. Discussion of High-Order Interpolation

As mentioned at various points in this book, high-order polynomial interpolation has a bad reputation. For equispaced points this is entirely appropriate, as shown in the last chapter, but for Chebyshev points it is entirely inappropriate. Here are some illustrative quotes from 50 years of numerical analysis textbooks, which we present anonymously.

We cannot rely on a polynomial to be a good approximation if exact matching at the sample points is the criterion used to select the polynomial. The explanation of this phenomenon is, of course, that the derivatives grow too rapidly. (1962)

However, for certain functions the approximate representation of $f ( x )$ by a single polynomial throughout the interval is not satisfactory. (1972)

But there are many functions which are not at all suited for approximation by a single polynomial in the entire interval which is of interest. (1974)

Polynomial interpolation has drawbacks in addition to those of global convergence. The determination and evaluation of interpolating polynomials of high degree can be too time-consuming for certain applications. Polynomials of high degree can also lead to difficult problems associated with roundoff error. (1977)

We end this section with two brief warnings, one against trusting the interpolating polynomial outside [the interval] and one against expecting too much of polynomial interpolation inside [the interval]. (1980)

Although Lagrangian interpolation is sometimes useful in theoretical investigations, it is rarely used in practical computations. (1985)

Polynomial interpolants rarely converge to a general continuous function. Polynomial interpolation is a bad idea. (1989)

While theoretically important, Lagrange’s formula is, in general, not as suitable for actual calculations as some other methods to be described below, particularly for large numbers $n$ of support points. (1993)

Unfortunately, there are functions for which interpolation at the Chebyshev points fails to converge. Moreover, better approximations of functions like $1 / ( 1 + x ^ { 2 } )$ can be obtained by other interpolants—e.g., cubic splines. (1996)

In this section we consider examples which warn us of the limitations of using interpolation polynomials as approximations to functions. (1996)

Increasing the number of interpolation points, i.e., increasing the degree of the polynomials, does not always lead to an improvement in the approximation. The spline interpolation that we will study in this section remedies this deficiency. (1998)

The surprising state of affairs is that for most continuous functions, the quantity $\| f - p _ { n } \| _ { \infty }$ will not converge to 0. (2002)

Because its derivative has $n - 1$ zeros, a polynomial of degree n has $n - 1$ extreme or inflection points. Thus, simply put, a high-degree polynomial necessarily has many “wiggles,” which may bear no relation to the data to be fit. (2002)

By their very nature, polynomials of a very high degree do not constitute reasonable models for real-life phenomena, from the approximation and from the handling pointof-view. (2004)

The oscillatory nature of high degree polynomials, and the property that a fluctuation over a small portion of the interval can induce large fluctuations over the entire range, restricts their use. (2005)

In addition to the inherent instability of Lagrange interpolation for large $_ { n }$ , there are also classes of functions that are not suitable for approximation by certain types of interpolation. There is a celebrated example of Runge. . . . (2011)

A great deal of confusion underlies remarks like these. Some of them are literally true, but they are all misleading. In fact, polynomial interpolants in Chebyshev points are problem-free when evaluated by the barycentric interpolation formula. They have the same behavior as discrete Fourier series for periodic functions, whose reliability nobody worries about. The introduction of splines is a red herring: the true advantage of splines is not that they converge where polynomials fail to do so, but that they are more easily adapted to irregular point distributions and more localized, giving errors that decay exponentially rather than just algebraically away from singularities (Exercise 9.8).

It is interesting to speculate as to how the distrust of high-degree polynomials became so firmly established. I think the crucial circumstance is that not one but several combined problems affect certain computations with polynomials, a situation complex enough to have obscured the truth from easy elucidation. If working with polynomials had been the central task of scientific computing, the truth would have been worked out nonetheless, but over the years there were always bigger problems pressing upon the attention of numerical analysts, like matrix computations and differential equations. Polynomial computations were always a sideline.

At the most fundamental level there are the two issues of conditioning and stability—both crucial, and not the same. See [Trefethen & Bau 1997] for a general

discussion of conditioning and stability.

(1) Conditioning of the problem. The interpolation points must be properly spaced (e.g., Chebyshev or Legendre) for the interpolation problem to be wellconditioned. This means that the interpolant should not depend too sensitively on the data. The Runge phenomenon for equally spaced points is the well-known consequence of extreme ill-conditioning, with sensitivities of order $2 ^ { n }$ . The next chapter makes such statements precise through the use of Lebesgue constants.

(2) Stability of the algorithm. The interpolation algorithm must be stable (e.g., the barycentric interpolation formula) for a computation to be accurate, even when the problem is well-conditioned. This means that in the presence of rounding errors, the computed solution should be close to an exact solution for some interpolation data close to the exact data. In particular, the best-known algorithm of all, namely the “polyval/polyfit” algorithm of solving a Vandermonde linear system of equations to find the coefficients of the interpolant expressed as a linear combination of monomials, is explosively unstable, relying on a matrix whose condition number grows exponentially with the dimension (Exercise 5.2).

These facts would be enough to explain a good deal of confusion, but another consideration has muddied the water further, namely crosstalk with the notoriously troublesome problem of finding roots of a polynomial from its coefficients (to be discussed in Chapter 18). The difficulties of polynomial rootfinding were widely publicized by Wilkinson beginning in the 1950s, who later wrote an article called “The perfidious polynomial” that won the Chauvenet Prize of the Mathematical Association of America [Wilkinson 1984]. Undoubtedly this negative publicity further discouraged people from the use of polynomials, even though interpolation and rootfinding are different problems. They are related, with related widespread misconceptions about accuracy: just as interpolation on an interval is trouble-free for a stable algorithm based on Chebyshev points, rootfinding on an interval is troublefree for a stable algorithm based on expansions in Chebyshev polynomials (Chapter 18). But very few textbooks tell readers these facts.

Summary of Chapter 14. Generations of numerical analysis textbooks have warned readers that polynomial interpolation is dangerous. In fact, if the interpolation points are clustered and a stable algorithm is used, it is bulletproof.

Exercise 14.1. Convergence as $n  \infty$ . The 1998 quote asserts that increasing $n$ “does not always lead to an improvement.” Based on the theorems of this book, for interpolation in Chebyshev points, for which functions $f$ do we know that increasing $n$ must lead to an improvement?

Exercise 14.2. Too many wiggles. Using the Chebfun roots(f,'all') option, plot all the roots in the complex plane of the derivative of the chebfun corresponding to $f ( x ) =$ $\exp ( x ) \operatorname { t a n h } ( 2 x - 1 )$ on $[ - 1 , 1 ]$ . What is the error in the argument in the second 2002 quote used to show that “a high-degree polynomial necessarily has many wiggles”? (We shall return to this phenomenon in the discussion of the theorems of Walsh and of Blatt and Saff at the end of Chapter 18.)

Exercise 14.3. Your own textbook. Find a textbook of numerical analysis and examine its treatment of polynomial interpolation. (a) What does it say about behavior for large $_ n$ ? If it asserts that this behavior is problematic, is this conclusion based on the assumption of equally spaced points, and does the text make this clear? (b) Does it mention interpolation in Chebyshev points? Does it state that such interpolants converge exponentially for analytic functions? (c) Does it mention the barycentric formula? (d) Does it claim that one should use a Newton rather than a Lagrange interpolation formula for numerical work? (This is a myth.)

Exercise 14.4. Spline interpolants. (a) Use the Chebfun spline command to interpolate $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ by a cubic spline in $n + 1$ equally spaced points on $[ - 1 , 1 ]$ . Compare the $\infty$ -norm error as $n \to \infty$ with that of polynomial interpolation in Chebyshev points. (b) Same problem for $f ( x ) = | x + 1 / \pi |$ . (c) Same problem for $f ( x ) = | x + 1 / \pi |$ , but measuring the error by the $\infty$ -norm over the interval [0, 1]. (Compare Exercise 9.8.)

# Chapter 15. Lebesgue Constants

There is a well-developed theory that quantifies the convergence or divergence of polynomial interpolants. A key notion is that of the Lebesgue constant, $\Lambda$ , for interpolation in a given set of points. The Lebesgue constant is the $\infty$ -norm of the linear mapping from data to interpolant:

$$
\Lambda = \operatorname* { s u p } _ { f } { \frac { \| p \| } { \| f \| } } ,
$$

where $\| \cdot \|$ denotes the $\infty$ -norm in $C ( [ - 1 , 1 ] )$ . In words, if you have data values on an $( n + 1 )$ -point grid, and the data come from sampling a function that is no greater than $^ { 1 }$ in absolute value, what is the largest possible value of the interpolant $p$ somewhere in $[ - 1 , 1 ]$ ?

In the plots of Chapter 13 for interpolation of Runge’s function, for example, we saw that the interpolants grew much bigger than the data. Thus the Lebesgue constants must be large for equispaced interpolation. For example, for $n = 5 0$ , the data are bounded by 1 for all $n$ , yet the interpolant is bigger than $1 0 ^ { 5 }$ . Thus the Lebesgue constant for interpolation in 50 equispaced points must be greater than $1 0 ^ { 5 }$ . (In fact, it is about $4 . 2 \times 1 0 ^ { 1 2 }$ .)

From the basic Lagrange formula (5.1) for polynomial interpolation,

$$
p ( x ) = \sum _ { j = 0 } ^ { n } f _ { j } \ell _ { j } ( x ) ,
$$

we can get a formula for $\Lambda$ in terms of the Lagrange polynomials $\{ \ell _ { j } \}$ . At any point $x \in [ - 1 , 1 ]$ , the maximum possible value of $| p ( x ) |$ for grid data bounded by $1$ in absolute value will be the number $\lambda ( x )$ obtained if each data value is $\pm 1$ , with signs

chosen to make all the signs at $x$ coincide:

$$
\lambda ( x ) = \sum _ { j = 0 } ^ { n } | \ell _ { j } ( x ) | .
$$

This sum of absolute values is known as the Lebesgue function for the given grid, and the Lebesgue constant is equal to its maximum value,

$$
\Lambda = \operatorname* { s u p } _ { x \in [ - 1 , 1 ] } \lambda ( x ) .
$$

The reason Lebesgue constants are interesting is that interpolants are guaranteed to be good if and only if the Lebesgue constants are small. We can make this statement precise as follows. Let $\Lambda$ be the Lebesgue constant for interpolation in a certain set of points. Without loss of generality (since the interpolation process is linear), suppose the largest absolute value of the samples is 1. If $p$ is the interpolant in these points to a function $f$ , we know that $\| p \|$ might be as great as $\Lambda$ ; yet $\| f \|$ might be as small as 1. Thus $\| f - p \|$ might be as great as $\Lambda - 1$ , showing that a large Lebesgue constant rigorously implies the possibility of a large interpolation error.

Conversely, let $p ^ { * }$ be the best degree $n$ polynomial approximation to $f$ in the $\infty$ -norm. If $p$ is the polynomial interpolant to $f$ in the given points, then $p - p ^ { * }$ is the polynomial interpolant to $f - p ^ { * }$ . By the definition of the Lebesgue constant, $\| p - p ^ { * } \|$ is no greater than $\Lambda \| f - p ^ { * } \|$ . Since $f - p = ( f - p ^ { * } ) - ( p - p ^ { * } )$ , this implies that $\| f - p \|$ is no greater than $( \Lambda + 1 ) \| f - p ^ { * } \|$ . Thus a small Lebesgue constant implies that interpolation will be close to best.

Actually, the discussion of the last two paragraphs is not limited to interpolation. What is really in play here is any approximation process that is a linear projection from $C ( [ - 1 , 1 ] )$ to $\mathcal { P } _ { n }$ , of which Chebyshev projection (truncation of the Chebyshev series) would be an example as well as interpolation. Suppose we let $L$ denote an operator that maps functions $f \in C ( [ - 1 , 1 ] )$ to approximations by polynomials $p \in \mathcal { P } _ { n }$ . For $L$ to be linear means that $L ( f _ { 1 } + f _ { 2 } ) = L f _ { 1 } + L f _ { 2 }$ for any $f _ { 1 } , f _ { 2 } \in$ $C ( [ - 1 , 1 ] )$ and $L ( \alpha f ) = \alpha L f$ for any scalar $\alpha$ , and for $L$ to be a projection means that if $p \in \mathcal { P } _ { n }$ , then $L p \ = \ p$ . By the argument above we have established the following result applicable to any linear projection.

Theorem 15.1. Near-best approximation and Lebesgue constants. Let $\Lambda$ (or $\Lambda _ { n }$ ) be the Lebesgue constant for a linear projection $L$ of $C ( [ - 1 , 1 ] )$ onto $\mathcal { P } _ { n }$ . Let $f$ be a function in $C ( [ - 1 , 1 ] )$ , $p = L f$ the corresponding polynomial approximant to $f$ , and $p ^ { * }$ the best approximation. Then

$$
\| f - p \| \leq ( \Lambda + 1 ) \| f - p ^ { * } \| .
$$

Proof. The proof is given in the paragraphs above.

So it all comes down to the question, How big is $\Lambda$ ? According to the theorem of Faber mentioned in Chapter 6 [Faber 1914], no sets of interpolation points can lead to convergence for all $f \in C ( [ - 1 , 1 ] )$ , so it follows from Theorems 6.1 and 15.1 that

$$
\operatorname* { l i m } _ { n \to \infty } \Lambda _ { n } = \infty
$$

for interpolation in any sets of points (Exercise 15.12). However, for well-chosen sets of points, the growth of $\Lambda _ { n }$ as $n  \infty$ may be exceedingly slow. Chebyshev points are nearly optimal, whereas equispaced points are very bad.

The following theorem summarizes a great deal of knowledge accumulated over the past century about interpolation processes. At the end of the chapter an analogous theorem is stated for Chebyshev projection. As always in this book, by “Chebyshev points” we mean Chebyshev points of the second kind, defined by (2.2).

Theorem 15.2. Lebesgue constants for polynomial interpolation. The Lebesgue constants $\Lambda _ { n }$ for degree $n \geq 0$ polynomial interpolation in any set of $n + 1$ distinct points in $[ - 1 , 1 ]$ satisfy

$$
\Lambda _ { n } \geq \frac { 2 } { \pi } \log ( n + 1 ) + 0 . 5 2 1 2 5 \ldots ;
$$

the number 0.52125 . . . is $( 2 / \pi ) ( \gamma + \log ( 4 / \pi ) )$ , where $\gamma \approx 0 . 5 7 7$ is Euler’s constant. For Chebyshev points, they satisfy

$$
\Lambda _ { n } \leq \frac { 2 } { \pi } \log ( n + 1 ) + 1 a n d \Lambda _ { n } \sim \frac { 2 } { \pi } \log n , n  \infty .
$$

For equispaced points they satisfy

$$
\Lambda _ { n } > \frac { 2 ^ { n - 2 } } { n ^ { 2 } } a n d \Lambda _ { n } \sim \frac { 2 ^ { n + 1 } } { e n \log n } , n  \infty ,
$$

with the inequality (15.9a) applying for $n \geq 1$ .

Proof. The fact that Lebesgue constants for polynomial interpolation always grow at least logarithmically goes back to Bernstein [1912b], Jackson [1913], and Faber [1914]. Bernstein knew that $( 2 / \pi ) \log n$ was the controlling asymptotic factor for interpolation in an interval, and the proof of (15.7) in this sharp form is due to Erd˝os [1961], who got a constant $C$ , and Brutman [1978], who improved the constant to 0.52125 . . . . Equation (15.8a) is a consequence of Theorem 4 of [Ehlich & Zeller 1966]; see also [Brutman 1997] and [McCabe & Phillips 1973]. Equation (15.8b) follows from this together with Erd˝os’s result. (Bernstein [1919] did the essential work, deriving this asymptotic result for Chebyshev points of the first kind, i.e., zeros of Chebyshev polynomials—see Exercise 15.2.) Equation (15.9b) is due to Turetskii [1940] and independently Sch¨onhage [1961], and for (15.9a) and a discussion of related work, see [Trefethen & Weideman 1991].

Equations (15.8) show that Lebesgue constants for Chebyshev points grow more slowly than any polynomial: for many practical purposes they might as well be 1. It is interesting to relate this bound to the interpolant through 100 random data points plotted on p. 10. The Lebesgue constant is the maximum amplitude this curve could possibly have attained, if the data had been as bad as possible. For 100 points this number is about 3.94. In the plot we see that random data have in fact come nowhere near even this modest limit.

On the other hand, equations (15.9) show that Lebesgue constants for equispaced points grow faster than any polynomial: for many practical purposes, unless $n$ is very small, they might as well be $\infty$ .

Taking advantage again of the interp1 command, as in Chapter 13, we can use Chebfun as a laboratory in which to see how such widely different Lebesgue constants emerge. Consider, for example, the case of four equally spaced points. Here are plots of the four Lagrange polynomials $\{ \ell _ { j } \}$ . In Chapter 9 we have already seen plots of Lagrange polynomials, but on a grid of 20 Chebyshev points instead of 4 equispaced points.

npts $\mathit { \Theta } = \mathit { \Theta } 4$ ; clear p, d = domain(-1,1); s = linspace(-1,1,4);   
for $\texttt { k } = \texttt { 1 }$ :npts subplot(2,2,k) $\textrm { y } =$ [zeros(1,k-1) 1 zeros(1,npts-k)]; p{k} $=$ interp1(s,y,d); plot(p{k}), hold on, plot(s,p{k}(s),'.') plot(s(k),p{k}(s(k)),'hr')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/c2485d98d1a80c2864b8a6cd8d05ec41a23975b5db921503a3b8ebf78d9f0312.jpg)

By taking the absolute values of these curves, we see the largest possible effect at each point in $[ - 1 , 1 ]$ of data that is nonzero at just one point of the grid:

for $\texttt { k } = \texttt { 1 }$ :npts subplot(2,2,k), absp $=$ abs(p{k}); plot(absp), hold on, plot(s,absp(s),'.') plot(s(k),absp(s(k)),'hr')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f5113bb6133227a0e9fc82a6bf578a58b9ba4fd545535a2d67c1066c21f8186d.jpg)

Now let us add up these absolute values as in (15.3):

$\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ chebfun('x'); ${ \mathrm { ~ \cal ~ L ~ } } = { \mathrm { ~ 0 * x } }$ ; for k = 1:npts, $\mathrm { ~ L ~ } = \mathrm { ~ L ~ } +$ abs(p{k}); end plot(L), hold on, plot(s,L(s),'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d2748eece46b5b136215ab68be2ce0412085b849789dcfc188cf15a40251dcc0.jpg)

This is the Lebesgue function $\lambda ( x )$ , a piecewise polynomial, telling us the largest possible effect at each point $x \in [ - 1 , 1 ]$ of interpolating data of norm 1. The Lebesgue constant (15.4) is the height of the curve:

Lconst $=$ norm(L,inf)

Lconst $=$ 1.631130309440900

A code lebesgue for automating the above computation (actually based on a more efficient method) is included in Chebfun, and it optionally returns the Lebesgue constant as well as the Lebesgue function. Here are the results for 8 equispaced points:

s = linspace(-1,1,8); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst

Lconst $=$ 6.929739656126466

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/a708f71491e25c2aa7d3a3bffd7c7ba9f5579d6665b47c8495182bd2e9a4ba17.jpg)

And here they are for 12 points. Note that the Lebesgue constant has jumped from 7 to 51.

s = linspace(-1,1,12); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst

Lconst $=$ 51.214223185730020

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/1e48e6558849edde9bb798b139902543923504e308c74e4d2af78825dcfcc7a4.jpg)

The function takes large values near $\pm 1$ , as we expect from Chapter 13 since the Runge phenomenon is associated with interpolants becoming very large near the endpoints. In fact the Lebesgue function for interpolation in equispaced points is more naturally displayed on a log scale. Here it is for $n = 3 0$ :

s $=$ linspace(-1,1,30); [L,Lconst] $=$ lebesgue(s); semilogy(L), hold on, semilogy(s,L(s),'.'), Lconst

Lconst $=$ 3.447738672687561e+06

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/8a180e83159c55efa5e7b8158b8cc89d5676cd62f056c235516a2498b1683ef7.jpg)

For comparison, here are the corresponding results for 4, 8, and 12 Chebyshev points, now back again on a linear scale.

for npts $=$ 4:4:12 s $=$ chebpts(npts); [L,Lconst] $=$ lebesgue(s); plot(L), hold on, plot(s,L(s),'.'), Lconst   
end

Lconst $=$ 1.666666666666667   
Lconst $=$ 2.202214555205528   
Lconst $=$ 2.489430376881968

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/07d20a576c0d8356d0f243252221d479ad7b31319cffbf96a6449b16680fb8e7.jpg)

Here are 100 Chebyshev points, with a comparison of the actual Lebesgue constant with the bound from Theorem 15.2:

$\mathtt { n p t s } ~ = ~ 1 0 0$ ; s $=$ chebpts(npts); [L,Lconst] $=$ lebesgue(s); plot(L), Lconst, Lbound $=$ 1 + (2/pi)\*log(npts)

Lconst $=$ 3.887871431579913   
Lbound $=$ 3.931742395517711

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f4514cec933477f55fc1cf21c2cfc468af5d80ee5e0ff9c669eba4e15f452bfe.jpg)

The low height of this curve shows how stable Chebyshev interpolation is.

In Chapter 9 it was mentioned that combinations of Lagrange polynomials are the source of both the Gibbs phenomenon and the size of Lebesgue functions. Let us now explain this remark. To analyze the Gibbs oscillations near a step, we added up a succession of Lagrange polynomials with constant amplitude 1. Since a single Lagrange polynomial has an oscillatory inverse-linear tail, the sum corresponds to an alternating series that converges to a constant as $n \to \infty$ . Lebesgue functions, on the other hand, are defined by taking a maximum at each point on the grid. The maximum is achieved by adding up Lagrange polynomials with equal but alternating coefficients, so as to make the combined signs all equal. For example, on the 20- point Chebyshev grid, the maximum possible value of an interpolant is achieved at $x = 0$ by taking data with this pattern:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/d3d42282ce745d2591889d8f130d63b6532a5d2a4437adc5c8f2bc84af934779.jpg)

Here is the Chebyshev interpolant:

p = chebfun(d); hold on, plot(p)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/b6c51ce0a0064ec698268ec5fe3d212feaac408e92b60400fc14de94f8175ad9.jpg)

We readily confirm that the maximum of this interpolant is indeed the Lebesgue constant for this grid:

max(p), [L,Lconst] $=$ lebesgue(s); Lconst

ans $=$ 2.837131699740443   
Lconst $=$ 2.837131699740441

We can now summarize why Lebesgue constants for Chebyshev points, and indeed for any sets of interpolation points, must grow at least logarithmically with $n$ . The fastest a Lagrange polynomial can decay is inverse-linearly, and the Lebesgue function adds up those alternating tails with alternating coefficients, giving a harmonic series.

Our discussion in this chapter has focused on Chebyshev interpolation rather than projection. However, as usual, there are parallel results for projection, which historically were worked out earlier (for the Fourier case, not Chebyshev). We record here a theorem analogous to Theorem 15.2.

Theorem 15.3. Lebesgue constants for Chebyshev projection. The Lebesgue constants $\Lambda _ { n }$ for degree $n \geq 1$ Chebyshev projection in $[ - 1 , 1 ]$ are given by

$$
\Lambda _ { n } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \left| \frac { \sin ( ( n + 1 / 2 ) t ) } { \sin ( t / 2 ) } \right| d t .
$$

They satisfy

$$
\Lambda _ { n } \leq { \frac { 4 } { \pi ^ { 2 } } } \log ( n + 1 ) + 3 a n d \Lambda _ { n } \sim { \frac { 4 } { \pi ^ { 2 } } } \log n , n  \infty .
$$

Proof. See [Rivlin 1981]. Equation (15.11b) is due to Fej´er [1910].

Related to Theorem 15.3 is another result concerning the norm of projection operators, proved by Landau [1913]. If $f$ is analytic in the unit disk and continuous on the boundary, and $p \in \mathcal { P } _ { n }$ is the Taylor projection of $f$ obtained by truncating its Taylor series, how much bigger can $p$ be than $f$ on the unit disk? Landau showed that these norms (now known as Landau constants) grow at a rate asymptotic to $( 1 / \pi ) \log n$ as $n \to \infty$ , a discovery that is perhaps the starting point of all results about logarithmic growth of norms of approximation operators.

For details about Lebesgue constants, an outstanding source is the survey article by Brutman [1997].

Though Lebesgue constants are a notion for linear approximation, the phenomenon of ill-conditioning that they quantify applies in nonlinear approximation too—see [Platte, Trefethen & Kuijlaars 2011].

Summary of Chapter 15. The Lebesgue constant for interpolation or any other linear projection is the $\infty$ -norm of the operator mapping the data to the approximant. For interpolation in $n + 1$ Chebyshev points, the Lebesgue constant is bounded by $1 + 2 \pi ^ { - 1 } \log ( n + 1 )$ , whereas for $n + 1$ equispaced points it is asymptotic to $2 ^ { n + 1 } / e n \log ( n )$ .

Exercise 15.1. Plots of Lebesgue functions. Plot the Lebesgue functions for the following distributions of interpolation points: (a) $- 0 . 9$ , $- 0 . 8$ , 0, 0.1, 0.2, 0.8; (b) same as in (a) but with additional points at a distance 0.01 to the right of the others.

Exercise 15.2. Chebyshev points of the first kind. The Lebesgue constant for interpolation in $n$ Chebyshev points is bounded by the Lebesgue constant for interpolation in $n { - } 1$ Chebyshev points of the first kind, introduced in Exercise 2.4 (see also help chebpts), with equality when $n$ is odd (Ehlich and Zeller [1966], McCabe and Phillips [1973]). Verify this numerically for $2 \leq n \leq 2 0$ .

Exercise 15.3. Reproducing a table by Brutman. Page 698 of [Brutman 1978] gives a table of various quantities associated with the Lebesgue function for interpolation in Chebyshev points of the first kind, mentioned in the last exercise. Track down this paper and write the shortest, most elegant Chebfun program you can to duplicate this table. Are all of Brutman’s digits correct?

Exercise 15.4. Omitting the endpoints. Suppose one performs polynomial interpolation in the usual Chebyshev points (2.2), but omitting the endpoints $x = \pm 1$ . Perform numerical experiments to determine what happens to the Lebesgue constants in this case. Does the growth appear to be of order $\log n$ , or $n ^ { \alpha }$ for some $\alpha$ , or what?

Exercise 15.5. Optimal interpolation points. Starting from the $n + 1$ Chebyshev points, one could attempt to use one of the MATLAB optimization codes to adjust the points to minimize the Lebesgue constant. Do this and give the Lebesgue constant and plot the Lebesgue function for (a) $n = 4$ , (b) $n = 5$ , (c) $n = 6$ , (d) $n = 7$ , and (e) $n = 8$ . How much improvement do you find in the Lebesgue constants as compared with Chebyshev points?

Exercise 15.6. Improving Turetskii’s estimate. For interpolation in equispaced points, Sch¨onhage [1961] derived a more accurate estimate than (15.9b): $\Lambda _ { n } ~ \sim$ $2 ^ { n + 1 } / e n ( \log n + \gamma )$ , where $\gamma = 0 . 5 7 7 \dots$ is again Euler’s constant. Perform a numerical study of $\Lambda _ { n }$ as a function of $n$ and see what difference this correction makes. For example, it might be helpful to make a table showing the percentage errors in both estimates as functions of $n$ .

Exercise 15.7. Interpolating data with a gap. (a) Consider polynomial interpolation in $n + 1$ points of a function $f$ defined on $[ - 1 , 1 ]$ , with half the points equally spaced from $^ { - 1 }$ to $- 1 / 4$ and the other half equally spaced from $1 / 4$ to 1. Determine the Lebesgue constants for this interpolation process numerically for the cases $n + 1 = 2 0$ and 40. (b) Suppose $f$ is analytic and bounded by 1 in the $\rho$ -ellipse $E _ { \rho }$ with $\rho = 2$ . Carefully quoting theorems from this book as appropriate, give upper bounds for the error $| f ( 0 ) - p ( 0 ) |$ for these two cases.

Exercise 15.8. Smallest local minimum of the Lebesgue function. Interpolation in equispaced points is much better near the middle of an interval than at the ends. In particular, the smallest local maximum of the Lebesgue function $\lambda$ is $\sim \log n / \pi$ as $n \to \infty$ [Tietze 1917]. Make a plot of these minima as a function of $n$ to verify this behavior numerically.

Exercise 15.9. Convergence for Weierstrass’s function. Exercise 7.3 promised that in Chapter 15 we would show that Chebyshev interpolants to Weierstrass’s nowheredifferentiable function of (6.1) converge as $n  \infty$ . Write down such a proof based on combining various theorems of this book.

Exercise 15.10. Random interpolation points. (a) Compute Lebesgue functions and constants numerically for degree $n$ interpolation in uniformly distributed random points in $[ - 1 , 1 ]$ . How does $\Lambda$ appear to grow with $n$ ? (b) The same question for points randomly distributed according to the Chebyshev density (11.18).

Exercise 15.11. A wiggly function. (a) Let $f$ be the function $T _ { m } ( x ) + T _ { m + 1 } ( x ) +$ $\cdots + T _ { n } ( x )$ with $m = 2 0$ and $n = 4 0$ , and let $p ^ { * }$ be the best approximation of $f$ of degree $m - 1$ . Plot $f$ and $f - p ^ { * }$ . What are their $\infty$ -norms and 2-norms? (b) The same questions with $m = 2 0 0$ and $n = 3 0 0$ .

Exercise 15.12. Divergence of Lebesgue constants. Spell out precisely the reasoning used to justify (15.6) in the text. In particular, make it clear why a “lim sup” rather than a “sup” appears in the formula.

Exercise 15.13. Confluent interpolation nodes. Let $\{ x _ { j } \}$ be a set of $n + 1$ distinct interpolation nodes in $[ - 1 , 1 ]$ . Now change $x _ { 0 }$ to $x _ { 1 } + \varepsilon$ , where $\varepsilon > 0$ is a parameter, and let $\Lambda ( \varepsilon )$ be the corresponding Lebesgue constant. Show that $\Lambda ( \varepsilon )$ diverges to $\infty$ as $\varepsilon  0$ . Can you quantify the rate of divergence?

# Chapter 16. Best and Near-Best

Traditionally, approximation theory has given a great deal of attention to best approximations in the $\infty$ -norm and rather less to alternatives such as Chebyshev interpolants. One might think that this is because best approximations are much better than the alternatives. However, this is not true.

In a moment we shall continue with Lebesgue constants to shed some light on this matter, but first, let us do some experiments. We start with the extreme case of a very smooth function, $\exp ( x )$ , and compare convergence of its Chebyshev interpolants $p$ and best approximants $p ^ { * }$ . (The difference between $n$ and $n { \mathrel { + { 1 } } }$ in this code is intentional, since chebfun takes as argument the number of interpolation points, whereas minimax takes the degree of the polynomial.)

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x'); f = exp(x); nn = 0:15;   
errbest $=$ []; errcheb $=$ []; i = 0;   
for $\texttt { n } = \texttt { n n }$ $\\\\\\\\\textbf { i } = \ \dot { \bf 1 } + 1$ ; [p,err] $=$ minimax(f,n); errbest(i) $=$ err; errcheb(i) $=$ norm(f-chebfun(f, $\tt { n } { + } 1$ ),inf);   
end   
semilogy(nn,errcheb,'. $- \mathbf { r } ^ { \mathsf { \Pi } }$ ), hold on, semilogy(nn,errbest,'h-b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/dcbac3d9b6c7e7a7569f3845cfd830ce109c14ed6bb6c0ecfe1fd7215b78e87e.jpg)

Clearly the stars for $p ^ { * }$ aren’t much better than the dots for $p$ . The ratio of the two converges toward 2 until the rounding errors set in for larger degrees:

ratio $=$ errcheb./errbest; fprintf('%8d %12.5f\n',[nn; ratio])

<table><tr><td>n</td><td>ratio</td></tr><tr><td>0</td><td>1.46212</td></tr><tr><td>1</td><td>2.00000</td></tr><tr><td>2</td><td>1.74436</td></tr><tr><td>3</td><td>1.96807</td></tr><tr><td>4</td><td>1.94991</td></tr><tr><td>5</td><td>1.98188</td></tr><tr><td>6</td><td>1.98182</td></tr><tr><td>7</td><td>1.98861</td></tr><tr><td>8</td><td>1.99105</td></tr><tr><td>9</td><td>1.99222</td></tr><tr><td>10</td><td>1.99468</td></tr><tr><td>11</td><td>1.99259</td></tr><tr><td>12</td><td>1.97361</td></tr><tr><td>13</td><td>1.27028</td></tr><tr><td></td><td>0.25152</td></tr><tr><td>14</td><td></td></tr><tr><td>15</td><td>0.80000</td></tr></table>

At the other extreme of smoothness, consider $| x |$ :

f = abs(x); nn = [0 2 4 10 20 40 100 200];   
errbest $= ~ [ ]$ ; errcheb $=$ []; i = 0;   
for $\texttt { n } = \texttt { n n }$ $\\\\\\\\\textbf { i } = \ \dot { \bf 1 } + 1$ ; [p,err] $=$ minimax(f,n); errbest(i) $=$ err; errcheb(i) $=$ norm(f-chebfun(f, $\ n { + } 1 \cdot$ ),inf);   
end   
loglog( $\mathtt { n n } { + } 1$ ,errbest, $" \mathrm { h } - \mathrm { b } \cdot$ ) hold on, loglog( $\mathtt { n n } { + 1 }$ ,errcheb,'.-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4a49b5ad3fff42464dff32d93fc5afe678c9e3a9140d55230772055eaa3dd915.jpg)

Again the stars are only a little better than the dots, by a constant factor of about 2.1306:

ratio $=$ errcheb./errbest; fprintf('%8d %12.5f\n',[nn; ratio])

<table><tr><td>n</td><td>ratio</td></tr><tr><td>0</td><td>2.00000</td></tr><tr><td>2</td><td>2.00000</td></tr><tr><td>4</td><td>2.10234</td></tr><tr><td>10</td><td>2.12677</td></tr><tr><td>20</td><td>2.12968</td></tr><tr><td>40</td><td>2.13037</td></tr><tr><td>100</td><td>2.13056</td></tr><tr><td>200</td><td>2.13059</td></tr></table>

(For odd values of $n$ the ratio is somewhat larger, approaching a constant of about 3.57.)

So for these examples at least, you don’t buy much with best approximations. And the cost in computing time is considerable. Here is the time for computing a Chebyshev interpolant $p$ of degree 200 and evaluating it at 100 points:

xx = rand(100,1); tic, p = chebfun(f,201); p(xx); toc

Elapsed time is 0.019866 seconds.

Here is the time for finding the best approximation $p ^ { * }$ and evaluating it at the same points:

tic, p = minimax(f,200); p(xx); toc

Elapsed time is 0.284064 seconds.

The reason computing $p ^ { * }$ is more difficult is that the mapping from $f$ to $p ^ { * }$ is nonlinear, hence requiring iteration in a numerical implementation, whereas the mapping from $f$ to $p$ is linear (Exercise 10.6). It is perfectly feasible to compute $p$ for degrees in the millions, whereas for $p ^ { * }$ we would rarely attempt degrees higher than hundreds.

Why has $p ^ { * }$ received so much more attention than $p$ over the years? One reason is that in the days before fast computers, the degrees were low, so small differences in accuracy were more important. Another is that the theory of best approximations is so beautiful! Indeed, their very nonlinearity makes best approximations seemingly a richer field for research than the simpler Chebyshev interpolants. Everybody remembers Theorem 10.1, the equioscillation theorem, from the moment they first see it.

Yet in actual computation, true best approximations are not so often used, as we have mentioned earlier (Chapter 10). This is a clue that the world of practice may have its own wisdom, independent of the theorists.

Now let us see what theoretical results might tell us about the difference between $p$ and $p ^ { * }$ . The first such results pertain to Theorems 7.2 and 8.2 given earlier. Those theorems concerned convergence rates of $p _ { n }$ to $f$ , depending on the smoothness of $f$ . What about analogous theorems for $\boldsymbol { p } _ { n } ^ { * }$ ? Apart from constant factors, they turn out to be the same! For example, exactly the same bound (8.3) was published by de la Vall´ee Poussin [1919, pp. 123–124], except with the Chebyshev interpolant $p _ { n }$ replaced by the best approximation $\boldsymbol { p } _ { n } ^ { * }$ . So within the two classes of functions considered in Chapters 7 and 8— $f$ having a $k$ th derivative of bounded variation, or $f$ being analytic—there is no clear reason to expect $\boldsymbol { p } _ { n } ^ { * }$ to be much better than $p _ { n }$ .

An observation for arbitrary functions $f$ is the following consequence of Theorems 15.1–15.3.

Theorem 16.1. Chebyshev projections and interpolants are near-best. Let $f \in C ( [ - 1 , 1 ] )$ have degree $n$ Chebyshev projection $f _ { n }$ , Chebyshev interpolant $p _ { n }$ , and best approximant $\boldsymbol { p } _ { n } ^ { * }$ , $n \geq 1$ . Then

$$
\| f - f _ { n } \| \leq \left( 4 + { \frac { 4 } { \pi ^ { 2 } } } \log ( n + 1 ) \right) \| f - p _ { n } ^ { * } \|
$$

and

$$
\| f - p _ { n } \| \leq \left( 2 + { \frac { 2 } { \pi } } \log ( n + 1 ) \right) \| f - p _ { n } ^ { * } \| .
$$

Proof. The proof follows from Theorems 15.1, 15.2, and 15.3.

So the loss of accuracy in going from $\boldsymbol { p } _ { n } ^ { * }$ to $p _ { n }$ , say, can never be larger than a factor of $2 + ( 2 / \pi ) \log ( n + 1 )$ . It is interesting to examine the size of this quantity for various values of $n$ . For $n = 1 0 ^ { 5 }$ , for example,

ans = 9.3294

Since this number is less than 10, we see that in dealing with polynomials of degree up to $n = 1 0 0 0 0 0$ , the nonoptimality of Chebyshev interpolation can never cost us more than 1 digit of accuracy. Here is the computation for $n = 1 0 ^ { 6 6 }$ :

ans $=$ 98.7475

So we never lose more than 2 digits for degrees all the way up to $1 0 ^ { 6 6 }$ —which might as well be $\infty$ for practical purposes. (For British audiences, one can give a talk on these matters with the title “ $1 0 ^ { 6 6 }$ and All That.”)

In fact, one might question whether best approximations are really better than near-best ones at all. Of course they are better in a literal sense, as measured in the $\infty$ -norm. However, consider the following error curves, which are quite typical for high-degree approximation of a function that is smoother in some regions than others.

$\begin{array} { r l } { \mathbf { f } } & { { } = } \end{array}$ abs(x-0.8); tic, pbest $=$ minimax(f,100); toc, hold off, plot(f-pbest,'r') tic, pcheb $=$ chebfun(f,101); toc, hold on, plot(f-pcheb)

Elapsed time is 0.195897 seconds.   
Elapsed time is 0.005879 seconds.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/6e6dc52df76454a7f7e350d0f95d05a8f379a23b984d35c5834e9ca9dfe04255.jpg)

We see that pbest is worse than pcheb for almost all values of $x$ , because the damage done by the singularity at $x = 0 . 8$ is global. By contrast, the effect of the singularity on pcheb decays with distance. Of course, pbest is better in the $\infty$ -norm:

errcheb $=$ norm(f-pcheb,inf), errbest $=$ norm(f-pbest,inf)

errcheb $=$ 0.0060 errbest $= \ 0 . 0 0 1 7 $

In the 2-norm, however, it is a good deal worse:

errcheb2 $=$ norm(f-pcheb,2), errbest2 $=$ norm(f-pbest,2)

errcheb2 $=$ 4.3337e-04   
errbest2 $=$ 0.0017

One might question how many applications there might be in which pbest was truly better than pcheb as an approximation to this function $f$ . To echo a title of Corless and Watt [2004], minimax approximations are optimal, but Chebyshev interpolants may sometimes be better!

Li [2004] takes another angle on the near-optimality of Chebyshev interpolants, pointing out that for applications to elementary functions, bounds on certain derivatives usually hold that imply that the error in interpolation in Chebyshev points of the first kind exceeds that of the best approximation by less than a factor of 2 or, as he calls it, “a fractional bit.”

From a more theoretical point of view, we return to a notion mentioned in Theorem 12.1. Given $f \in C ( [ - 1 , 1 ] )$ , let $\rho$ ( $1 \le \rho \le \infty$ ) be the parameter of the largest Bernstein ellipse $E _ { \rho }$ to which $f$ can be analytically continued, and let $\left\{ p _ { n } \right\}$ be any sequence of approximations to $f$ with $p _ { n } \in \mathcal { P } _ { n }$ . Then

$$
\operatorname* { l i m } _ { n \to \infty } \| f - p _ { n } \| ^ { 1 / n } \geq \rho ^ { - 1 } ,
$$

and if equality holds, $\left\{ p _ { n } \right\}$ is said to be maximally convergent. It follows from Theorems 8.2 and 15.1 that if $\{ p _ { n } \}$ comes from a linear projection with Lebesgue constants $\Lambda _ { n }$ that grow more slowly than exponentially as $\begin{array} { r l } { n \ \to \ \infty } \end{array}$ , i.e., with $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \Lambda _ { n } ^ { 1 / n } = 1 } \end{array}$ , then $\left\{ p _ { n } \right\}$ is maximally convergent for every $f \in C ( [ - 1 , 1 ] )$ . In particular, Chebyshev projections and interpolants are maximally convergent. This is a precise sense in which such approximations are “near-best.”

Finally, we mention another kind of optimality that has received attention in the approximation theory literature [Bernstein 1931, Erd˝os 1961, Kilgore 1978, de Boor & Pinkus 1978]: optimal interpolation points (Exercise 15.5). Chebyshev points are very good, but they do not quite minimize the Lebesgue constant. Optimal points minimize the Lebesgue constant (by definition), and they level out the peaks of the Lebesgue function exactly (it has been proved)—but the improvement is negligible. The first statement of Theorem 15.2 establishes that, like Chebyshev points, they lead to Lebesgue constants that are asymptotic to $( 2 / \pi ) \log n$ as $n  \infty$ , which means they do not improve upon Chebyshev points even by a constant factor.

Summary of Chapter 16. The $\infty$ -norm error in degree $n$ Chebyshev interpolation is never greater than $2 + ( 2 / \pi ) \log ( n + 1 )$ times the error in best approximation, and in practice, the ratio rarely exceeds even a factor of 2. In the 2-norm, the interpolant is often much better than the best approximation.

Exercise 16.1. Computing times for interpolation and best approximation. (a) Repeat the experiment of this chapter involving $\left| x - 0 . 8 \right|$ but for all the values $n = 1 0 0 , 2 0 0 , 3 0 0 , \ldots , 1 0 0 0$ . In each case measure the computing times for Chebyshev interpolation and best approximation as calculated by the Chebfun minimax command, the $L ^ { 2 }$ errors of both approximants, and the $L ^ { \infty }$ errors. Plot these results and comment on what you find. (b) In particular, produce a plot of error curves like that in the text.

Exercise 16.2. Approximation of a wiggly function. Define $f ( x ) = T _ { 2 0 0 } ( x ) +$ $T _ { 2 0 1 } ( x ) + \cdot \cdot \cdot + T _ { 2 2 0 } ( x )$ . Construct the Chebyshev interpolant $p$ and best approximation $p ^ { * }$ of degree 199. Plot the errors and measure the $\infty$ - and 2-norms.

Exercise 16.3. Rounding errors on a grid of $\mathbf { 1 0 ^ { 6 6 } }$ points. Suppose we had a computer with 16-digit precision capable of applying the barycentric formula (5.13) to evaluate a polynomial interpolant $p ( x )$ for data on a Chebyshev grid of $1 0 ^ { 6 6 }$ points. (For the sake of this thought experiment, imagine that the differences $\boldsymbol { x } - \boldsymbol { x _ { j } }$ can be evaluated correctly to 16-digit precision rather than coming out as 0 and thereby invoking the $x = x _ { j }$ clause of Theorem 5.2.) The evaluation would require adding up about $1 0 ^ { 6 6 }$ numbers, entailing about $1 0 ^ { 6 6 }$ rounding errors. Even if these errors accumulated only in the square root fashion of a random walk, it would still seem we must end up with errors on the order of $1 0 ^ { 3 3 }$ times $1 0 ^ { - 1 6 }$ , destroying all accuracy. Yet in fact, the computation would be highly accurate. What is the flaw in this $1 0 ^ { 3 3 }$ reasoning?

Exercise 16.4. Another wiggly function. Consider the function $f ( x ) = \sin ( x ^ { 2 } ) +$ $\ \sin ( x ) ^ { 2 }$ on the interval [0, 14]. Compute its degree 100 best polynomial approximation $p$ and make plots of $f$ and $p$ together and of $f - p$ . Discuss these curves in light of the developments of this chapter.

# Chapter 17. Orthogonal Polynomials

This book gives special attention to Chebyshev polynomials, since they are so useful in applications and the analogue on $[ - 1 , 1 ]$ of trigonometric polynomials on $[ - \pi , \pi ]$ . However, Chebyshev polynomials are just one example of a family of orthogonal polynomials defined on the interval $[ - 1 , 1 ]$ , and in this chapter we note some of the other possibilities, especially Legendre polynomials, which are the starting point for Gauss quadrature (Chapter 19). The study of orthogonal polynomials was initiated by Jacobi [1826] and already well developed by the end of the 19th century thanks to work by mathematicians including Chebyshev, Christoffel, Darboux, and Stieltjes. Landmark books on the subject include Szeg˝o [1985] and Gautschi [2004].

Let $w \in C ( - 1 , 1 )$ be a weight function with $w ( x ) > 0$ for all $x \in ( - 1 , 1 )$ and $\textstyle \int _ { - 1 } ^ { 1 } w ( x ) d x < \infty$ ; we allow $w ( x )$ to approach 0 or $\infty$ as $x  \pm 1$ . The function $w$ defines an inner product for functions defined on $[ - 1 , 1 ]$ :

$$
( f , g ) = \int _ { - 1 } ^ { 1 } w ( x ) { \overline { { f ( x ) } } } g ( x ) d x .
$$

(The bar over $f ( x )$ indicates the complex conjugate and can be ignored when working with real functions.) A family of orthogonal polynomials associated with $w$ is a family

$$
p _ { 0 } , p _ { 1 } , p _ { 2 } , \ldots ,
$$

where $p _ { n }$ has degree exactly $n$ for each $n$ and the polynomials satisfy the orthogonality condition

$$
( p _ { j } , p _ { k } ) = 0 , \quad k \neq j .
$$

Notice that this condition implies that each $p _ { n }$ is orthogonal to all polynomials of degree $k < n$ . The condition (17.2) determines the family uniquely except that each $p _ { n }$ can be multiplied by a constant factor. One common normalization is to

require that each $p _ { n }$ be monic, in which case we have a family of monic orthogonal polynomials. Another common normalization is $p _ { 0 } > 0$ together with the condition

$$
( p _ { j } , p _ { k } ) = \delta _ { j k } = { \left\{ \begin{array} { l l } { 1 , } & { k = j , } \\ { 0 , } & { k \neq j , } \end{array} \right. }
$$

in which case we have orthonormal polynomials. A third choice, the standard one for Chebyshev and Legendre polynomials, is to require $p _ { n } ( 1 ) = 1$ for each $n$ .

As we have seen in Chapter 3, the Chebyshev polynomials $\{ T _ { k } \}$ are orthogonal with respect to the weight function

$$
w ( x ) = { \frac { 2 } { \pi { \sqrt { 1 - x ^ { 2 } } } } }
$$

(Exercise 3.7). In fact, if $T _ { 0 }$ is replaced by $T _ { 0 } / \sqrt { 2 }$ , they are orthonormal. The first three Chebyshev polynomials are

$$
T _ { 0 } ( x ) = 1 , \quad T _ { 1 } ( x ) = x , \quad T _ { 2 } ( x ) = 2 x ^ { 2 } - 1 ,
$$

as we can confirm with the chebpoly command:

for ${ \mathrm { ~ j ~ } } = ~ 0 : 5$ , disp(fliplr(poly(chebpoly(j)))), end

$$
\begin{array} { c c c c c c c c c c c c c c c c } { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \end{array}
$$

The Chebyshev weight function has an inverse–square root singularity at each end of $[ - 1 , 1 ]$ . Allowing arbitrary power singularities at each end gives the Jacobi weight function $w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta }$ , where $\alpha , \beta > - 1$ are parameters. The associated orthogonal polynomials are known as Jacobi polynomials and written as $\{ P _ { n } ^ { ( \alpha , \beta ) } \}$ . In the special case $\alpha = \beta$ we get the Gegenbauer or ultraspherical polynomials.

The most special case of all is $\alpha = \beta = 0$ , leading to Legendre polynomials, with the simplest of all weight functions, a constant:

$$
w ( x ) = 1 .
$$

If we normalize according to (17.3), the first three Legendre polynomials are

$$
p _ { 0 } ( x ) = \sqrt { 1 / 2 } , \quad p _ { 1 } ( x ) = \sqrt { 3 / 2 } x , \quad p _ { 2 } ( x ) = \sqrt { 4 5 / 8 } x ^ { 2 } - \sqrt { 5 / 8 } ,
$$

as we can confirm by using the flag 'norm' with the legpoly command:

for ${ \mathrm { ~ j ~ } } = ~ 0 : 5$ , c = fliplr(poly(legpoly(j,'norm'))); disp(c), end

<table><tr><td>-0.7906</td><td>-0.0000</td><td>2.3717</td><td></td><td></td></tr><tr><td>0.0000</td><td>-2.8062</td><td>-0.0000</td><td>4.6771</td><td></td></tr><tr><td>0.7955</td><td>0.0000</td><td>-7.9550</td><td>-0.0000</td><td>9.2808</td></tr><tr><td>0.0000</td><td>4.3973</td><td>-0.0000</td><td>-20.5206</td><td>0.0000 18.4685</td></tr></table>

However, as mentioned above, it is more common to normalize Legendre polynomials by the condition $p _ { j } ( 1 ) = 1$ . Switching to an uppercase $P$ to follow the usual notation, the first three Legendre polynomials are

$$
\begin{array} { r } { P _ { 0 } ( x ) = 1 , \quad P _ { 1 } ( x ) = x , \quad P _ { 2 } ( x ) = \frac { 3 } { 2 } x ^ { 2 } - \frac { 1 } { 2 } . } \end{array}
$$

These are the polynomials returned by legpoly by default:

for ${ \mathrm { ~ j ~ } } = ~ 0 : 5$ , c = fliplr(poly(legpoly(j))); disp(c), end

The rest of this chapter is devoted to comparing Legendre and Chebyshev polynomials. The comparison, and the consideration of orthogonal polynomials in general, will continue into the next two chapters on rootfinding (Chapter 18) and quadrature (Chapter 19). For example, Theorem 19.6 presents a fast method for calculating the barycentric interpolation weights for Legendre points, the zeros of Legendre polynomials. On the whole, different families of orthogonal polynomials have similar approximation properties, but Chebyshev points have the particular advantage that one can convert back and forth between interpolant and expansion by the FFT.

We begin with a visual comparison of the Chebyshev and Legendre polynomials of degrees 1–6 for $x \in [ - 1 , 1 ]$ . The shapes are similar, with the degree $n$ polynomial always having $n$ roots in the interval (Exercise 17.4).

for $\mathrm { ~ n ~ } = \mathrm { ~ 1 { : } ~ 6 ~ }$ $\mathrm { { T } \{ n \} \mathrm { { \Omega } = } }$ chebpoly(n); subplot(3,2,1), plot(T{n}) $\mathsf { P \{ n \} } = \mathsf { I e g p o l y ( n ) }$ ; subplot(3,2,2), plot(P{n},'m')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/1a20f25dd9da4716489b90fc593c2788273dd0907ffe4dcac8bc6f3f5409b30f.jpg)

For Legendre polynomials normalized by $P _ { j } ( 1 ) = 1$ , the orthogonality condition turns out to be

$$
\int _ { - 1 } ^ { 1 } P _ { j } ( x ) P _ { k } ( x ) d x = { \left\{ \begin{array} { l l } { 0 , } & { j \neq k , } \\ { { \cfrac { 2 } { 2 k + 1 } } , } & { j = k . } \end{array} \right. }
$$

We can verify this formula numerically by constructing what Chebfun calls a quasimatrix $X$ , that is, a “matrix” whose columns are chebfuns, and then taking inner products of each column with each other column via the quasimatrix product $X ^ { T } X$ . One way to construct $X$ is like this:

Another equivalent method is built into legpoly:

Here is the quasimatrix product:

X'\*X ans $=$

0.6667 0.0000 0.0000 -0.0000 -0.0000 -0.0000

<table><tr><td>0.0000</td><td>0.4000</td><td>-0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.0000</td></tr><tr><td>0.0000</td><td>-0.0000</td><td>0.2857</td><td>-0.0000</td><td>0.0000</td><td>-0.0000</td></tr><tr><td>-0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.2222</td><td>-0.0000</td><td>-0.0000</td></tr><tr><td>-0.0000</td><td>-0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.1818</td><td>0.0000</td></tr><tr><td>-0.0000</td><td>0.0000</td><td>0.0000</td><td>-0.0000</td><td>0.0000</td><td>0.1538</td></tr></table>

This matrix of inner products looks diagonal, as it should, and we can confirm the diagonal structure by checking the norm of the off-diagonal terms:

norm(ans-diag(diag(ans)))

ans = 2.3066e-16

The entries on the diagonal are the numbers $2 / 3 , 2 / 5 , 2 / 7 , \ldots$ prescribed by (17.5). Legendre polynomials satisfy the 3-term recurrence relation

$$
( k + 1 ) P _ { k + 1 } ( x ) = ( 2 k + 1 ) x P _ { k } ( x ) - k P _ { k - 1 } ( x ) ,
$$

which may be compared with the recurrence relation (3.10) for Chebyshev polynomials. In general, orthogonal polynomials defined by (17.1)–(17.2) always satisfy a 3-term recurrence relation, and the reason is as follows. Supposing $\left\{ p _ { n } \right\}$ are monic for simplicity, one can determine $p _ { n + 1 }$ by the Gram–Schmidt orthogonalization procedure, subtracting off the projections of the monic degree $n + 1$ polynomial $x p _ { n }$ onto each of the polynomials $p _ { 0 } , \ldots , p _ { n }$ , with the coefficient of the projection onto $p _ { k }$ being given by the normalized inner product $( x p _ { n } , p _ { k } ) / ( p _ { k } , p _ { k } )$ :

$$
p _ { n + 1 } = x p _ { n } - { \frac { ( x p _ { n } , p _ { n } ) } { ( p _ { n } , p _ { n } ) } } p _ { n } - { \frac { ( x p _ { n } , p _ { n - 1 } ) } { ( p _ { n - 1 } , p _ { n - 1 } ) } } p _ { n - 1 } - \cdots - { \frac { ( x p _ { n } , p _ { 0 } ) } { ( p _ { 0 } , p _ { 0 } ) } } p _ { 0 } .
$$

For every $k < n { - } 1$ , however, the inner product is equal to $0$ because $p _ { n }$ is orthogonal to the lower-degree polynomial $x p _ { k }$ : 8

$$
\left( x p _ { n } , p _ { k } \right) = \left( p _ { n } , x p _ { k } \right) = 0 , \quad k < n - 1 .
$$

Thus the series above reduces to the 3-term recurrence [Darboux 1878]

$$
p _ { n + 1 } = x p _ { n } - { \frac { ( x p _ { n } , p _ { n } ) } { ( p _ { n } , p _ { n } ) } } p _ { n } - { \frac { ( x p _ { n } , p _ { n - 1 } ) } { ( p _ { n - 1 } , p _ { n - 1 } ) } } p _ { n - 1 } .
$$

When the weight function $w$ is even, the middle term drops out (Exercise 17.5), and the formula further simplifies to

$$
p _ { n + 1 } = x p _ { n } - { \frac { \left( x p _ { n } , p _ { n - 1 } \right) } { \left( p _ { n - 1 } , p _ { n - 1 } \right) } } p _ { n - 1 } \quad { \mathrm { f o r ~ } } w { \mathrm { ~ e v e n } } .
$$

Chebyshev polynomials are not orthogonal in the standard inner product:

ans =

Nevertheless, Legendre and Chebyshev polynomials have much in common, as is further suggested by plots of $T _ { 5 0 }$ and $P _ { 5 0 }$ :

$\mathrm { T 5 0 ~ = }$ chebpoly(50); P50 $=$ legpoly(50); subplot(2,1,1), plot(T50), subplot(2,1,2), plot(P50,'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/e5d90fc270f7450248ea2b1c856e47fbef6043888b3234374787fb6bc4a6a7e9.jpg)

The zeros of the two families of polynomials are similar, as can be confirmed by comparing Chebyshev (dots) and Legendre (crosses) zeros for degrees 10, 20, and 50. (Instead of using the roots command here, one could achieve the same effect with chebpts(n,1) and legpts(n)—see Chapter 19.)

$\mathrm { T 1 0 ~ = }$ chebpoly(10); $\mathrm { { \Delta P 1 0 ~ } = }$ legpoly(10); Tr $=$ roots(T10); Pr = roots(P10); plot(Tr,.8,'.b'), hold on $\mathtt { p l o t } ( \mathtt { P r } , 0 . 9 , \mathbf { \Phi } ^ { \prime } \mathbf { x } \mathrm { m } ^ { \prime } )$ , ${ \mathrm { T } } 2 0 ~ =$ chebpoly(20); P20 = legpoly(20); Tr $=$ roots(T20); Pr $=$ roots(P20); plot(Tr,0.4,'.b') plot(Pr,0.5,'xm'), Tr $=$ roots(T50); Pr $=$ roots(P50); plot(Tr,0,'.b'), plot(Pr,0.1,'xm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/3740ddcf5c692d75db05d0c234a46138c6e6323c2609fbc88ed75e7ca3d25a0e.jpg)

Asymptotically as $n \to \infty$ , both sets of zeros cluster near $\pm 1$ with the same density distribution $n \mu ( x )$ , with $\mu$ given by (12.10). This behavior is made precise in

Theorem 12.1.4 of [Szeg˝o 1939] (Exercise 17.7), and exploitation of more detailed asymptotic properties of Jacobi polynomials is the crucial idea of [Hale & Townsend 2013].

Another comparison between Chebyshev and Legendre points concerns their Lebesgue functions and Lebesgue constants. Here we repeat a computation of Lebesgue functions from Chapter 15 for 8 Chebyshev points and compare it with the analogous computation for 8 Legendre points. Chebyshev and Legendre points as we have defined them so far differ not just in which polynomials they are connected with, but in that Chebyshev points come from extrema whereas Legendre points come from zeros.

$\qquad \mathtt { s } \ =$ chebpts(8); [L,Lconst] $=$ lebesgue(s);   
subplot(1,2,1), plot(L), hold on, plot(s,L(s),'.'), Lconst s $=$ legpts(8); [L,Lconst] $=$ lebesgue(s);   
subplot(1,2,2), plot(L), hold on, plot(s,L(s),'.'), Lconst

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/cdef487416dfbf74a75466ec8a6492f07456e9383e3368b077b9f7b47033309d.jpg)

The Lebesgue functions and constants for Legendre points are a little bigger than for Chebyshev points, having size $O ( n ^ { 1 / 2 } )$ rather than $O ( \log n )$ because of behavior near the endpoints [Szeg˝o 1939, p. 338]. This small difference is of little significance for most applications: the Lebesgue constants are still quite small, and either set of points will usually deliver excellent interpolants.

An alternative is to consider Legendre extreme points—the $n { \mathrel { + { 1 } } }$ points in $[ - 1 , 1 ]$ at which $| P _ { n } ( x ) |$ attains a local maximum. (The Legendre extreme points in $( - 1 , 1 )$ are also the roots of the Jacobi polynomial $P ^ { ( 1 , 1 ) } ( x )$ .) The Lebesgue function in this case looks even more satisfactory:

$\begin{array} { r } { \{ \begin{array} { r l } \end{array} \} = } & { { } \left[ - 1 \right. } \end{array}$ ; roots(diff(legpoly(7))); 1]; [L,Lconst] $=$ lebesgue(s); subplot(1,2,1), plot(L), hold on, plot(s,L(s),'.'), Lconst $\mathbf { s } 1 5 ~ = ~ [ - 1$ ; roots(diff(legpoly(15))); 1]; [L,Lconst] $=$ lebesgue(s15); subplot(1,2,2), plot(L), hold on, plot(s15,L(s15),'.'), Lconst

Lconst $=$ 1.9724 Lconst $= \ 2 . 4 3 0 3$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/f7c717a5dd83eb265b9678958aa24fb2c4a0c928fa0045020762ee3ff17e2ec0.jpg)

The Legendre extreme points have a memorable property: as shown by Stieltjes [1885], they are the Fekete or minimal-energy points in $[ - 1 , 1 ]$ , solving the equipotential problem on that interval for a finite number of equal charges (Exercise 12.1). Here, for example, is a repetition of a figure from Chapter 11 but now for 8 Legendre extreme points instead of 8 Chebyshev points. Again the behavior is excellent.

ell = poly(s,domain(-1,1)); plot(s,ell(s),'.k'), hold on xgrid $=$ -1.5:.02:1.5; ygrid $=$ -0.9:.02:0.9;   
[xx,yy] $=$ meshgrid(xgrid,ygrid); $\mathbf { z } \mathbf { z } = \mathbf { x } \mathbf { x } \mathbf { + } 1 \mathbf { i } \mathbf { * } \mathbf { y } \mathbf { y }$ ;   
ellzz $=$ ell(zz); levels $=$ 2.^(-6:0);   
contour(xx,yy,abs(ellzz),levels, $" \mathrm { \text k } "$ )

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/6b047fa41059702f7cc737862d2b7cf9a89af12b45f4fe02088e26526005d763.jpg)

Summary of Chapter 17. Chebyshev polynomials are just one example of a family of polynomials orthogonal with respect to a weight function $w ( x )$ on $[ - 1 , 1 ]$ . For $w ( x ) = c o n s t a n t$ , one gets the Legendre polynomials.

Exercise 17.1. Chebyshev and Legendre Lebesgue constants. Extend the experiments of the text to a table and a plot of Lebesgue constants of Chebyshev, Legendre, and Legendre extreme points for interpolation in $n + 1$ points with $n = 1 , 2 , 4 , \dotsc , 2 5 6$ . (To compute Legendre extreme points efficiently, you can use the observation about Jacobi polynomials mentioned in the text and the Chebfun command jacpoly.) What asymptotic behavior do you observe as $n \to \infty$ ?

Exercise 17.2. Chebyshev and Legendre interpolation points. Define $f ( x ) =$ $x \operatorname { t a n h } ( 2 \sin ( 2 0 x ) )$ , and let $p$ and $p _ { L }$ be the interpolants to $f$ in $n + 1$ Chebyshev or Legendre points on $[ - 1 , 1 ]$ , respectively. The latter can be computed with interp1 as in

Chapter 13. (a) For $n + 1 = 3 0$ , plot $f$ , $p$ , and $p _ { L }$ . What are the $\infty$ -norm errors $\| f - p \|$ and $\| f - p _ { L } \| ^ { . }$ ? (b) For $n + 1 = 3 0 0$ , plot $f - p$ and $f - p _ { L }$ . What are the errors now?

Exercise 17.3. Orthogonal polynomials via QR decomposition. (a) Construct a Chebfun quasimatrix A with columns corresponding to $1 , x , \ldots , x ^ { 5 }$ on $[ - 1 , 1 ]$ . Execute $\begin{array} { r } { [ { \mathsf Q } , { \mathsf R } ] { \mathsf \Pi } = { \mathsf Q } { \mathsf r } \left( { \mathsf A } \right) } \end{array}$ to find an equivalent set of orthonormal functions, the columns of $\mathsf { Q }$ , and plot these with plot(Q). How do the columns of $\mathsf { Q }$ compare with the Legendre polynomials normalized by (17.3)? (b) Write a for loop to normalize the columns of $\mathsf { Q }$ in a fashion corresponding to $P _ { j } ( 1 ) = 1$ and to adjust $R$ correspondingly so that the product $\scriptstyle { \mathsf { Q } } \ast { \mathsf { R } }$ continues to be equal to A, up to rounding errors, and plot the new quasimatrix with plot(Q). How do the columns of the new $\mathsf { Q }$ compare with the Legendre polynomials normalized by $P _ { j } ( 1 ) = 1 \Rsh$

Exercise 17.4. Zeros of orthogonal polynomials. Let $\left\{ p _ { n } \right\}$ be a family of orthogonal polynomials on $[ - 1 , 1 ]$ defined by (17.1)–(17.2). Show by using (17.2) that the zeros of $p _ { n }$ are distinct and lie in $( - 1 , 1 )$ .

Exercise 17.5. Even and odd orthogonal polynomials. Suppose the weight function $w$ of (17.1) is even. Prove by induction that $p _ { n }$ is even when $n$ is even and odd when $_ n$ is odd.

Exercise 17.6. Legendre and Chebyshev differential equations. (a) Show from the recurrence relation (17.6) that the Legendre polynomial $P _ { n }$ satisfies the differential equation $( 1 - x ^ { 2 } ) P ^ { \prime \prime } - 2 x P ^ { \prime } + n ( n + 1 ) P = 0$ . (b) Show from (3.10) that the Chebyshev polynomial $T _ { n }$ satisfies the differential equation $( 1 - x ^ { 2 } ) T ^ { \prime \prime } - x T ^ { \prime } + n ^ { 2 } T = 0$ .

Exercise 17.7. The envelope of an orthogonal polynomial. Theorem 12.1.4 of [Szeg˝o 1939] asserts that as $n \to \infty$ , the envelope of an orthonormal polynomial $p _ { n }$ defined by (17.1)–(17.3) approaches the curve $( w _ { \mathrm { C H E B } } ( x ) / w ( x ) ) ^ { 1 / 2 }$ , where $w _ { \mathrm { C H E B } }$ is the Chebyshev weight (17.4). Explore this prediction numerically with plots of Legendre polynomials for various $_ n$ .

Exercise 17.8. Minimality of orthogonal polynomials. Let $\left\{ p _ { n } \right\}$ be the family of monic orthogonal polynomials associated with the inner product (17.1). Show that if $q$ is any monic polynomial of degree $_ n$ , then $\left( q , q \right) \geq \left( p _ { n } , p _ { n } \right)$ .

# Chapter 18. Polynomial Roots and Colleague Matrices

It is well known that if $p$ is a polynomial expressed as a linear combination of monomials $x ^ { k }$ , then the roots of $p$ are equal to the eigenvalues of a certain companion matrix formed from its coefficients (Exercise 18.1). Indeed, from its beginning in the late 1970s, MATLAB has included a command roots that calculates roots of polynomials by using this identity. This method of zerofinding is effective and numerically stable, but only in a very narrow sense. It is a numerically stable algorithm for precisely the problem just posed: given the monomial coefficients, find the roots. The trouble is, this problem is an awful one! As Wilkinson made famous beginning in the 1960s, it is a highly ill-conditioned problem in general [Wilkinson 1984]. The roots tend to be so sensitive to perturbations in the coefficients that even though the algorithm is stable in the sense that it usually produces roots that are exactly correct for a polynomial whose coefficients match the specified ones to a coefficientwise relative error on the order of machine precision [Goedecker 1994, Toh & Trefethen 1994], this slight perturbation is enough to cause terrible inaccuracy.

There is an exception to this dire state of affairs. Finding roots from polynomial coefficients is a well-conditioned problem in the special case of polynomials with roots on or near the unit circle (see Exercise 18.7(a) and [Sitton et al. 2003]). The trouble is, most applications are not of this kind. More often, the roots of interest lie in or near a real interval, and in such cases one should avoid monomials, companion matrices, and the MATLAB roots command completely.

Fortunately, there is a well-conditioned alternative for such problems, and that is the subject of this chapter. By now we are experts in working with functions on $[ - 1 , 1 ]$ by means of Chebyshev interpolants and Chebyshev series. Within this class of tools, there is a natural way of computing the roots of a polynomial by solving an eigenvalue problem. Here is the crucial result, due independently to Specht [1960, p. 222] and Good [1961].9 The matrix $C$ of the theorem is called a colleague matrix.

Theorem 18.1. Polynomial roots and colleague matrix eigenvalues. The roots of the polynomial

$$
p ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } T _ { k } ( x ) , \quad a _ { n } \ne 0 ,
$$

are the eigenvalues of the matrix

$$
C = \left( \begin{array} { c c c c c c c c } { { 0 } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \frac { 1 } { 2 } } } & { { 0 } } & { { \frac { 1 } { 2 } } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \frac { 1 } { 2 } } } & { { 0 } } & { { \frac { 1 } { 2 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { \frac { 1 } { 2 } } } \\ { { } } & { { } } & { { } } & { { } } & { { \frac { 1 } { 2 } } } & { { 0 } } & { { } } & { { a _ { 1 } } } & { { a _ { 2 } } } & { { \ldots } } & { { a _ { n - 1 } } } \end{array} \right) .
$$

(Entries not displayed are zero.) If there are multiple roots, these correspond to eigenvalues with the same multiplicities.

Proof. Let $x$ be any number, and consider the nonzero $n$ -vector

$$
v = ( T _ { 0 } ( x ) , T _ { 1 } ( x ) , \ldots , T _ { n - 1 } ( x ) ) ^ { T } .
$$

If we multiply $C$ by $v$ , then in every row but the first and last the result is

$$
\begin{array} { r } { T _ { k } ( x ) \mapsto \frac 1 2 T _ { k - 1 } ( x ) + \frac 1 2 T _ { k + 1 } ( x ) = x T _ { k } ( x ) , } \end{array}
$$

thanks to the 3-term recurrence relation (3.9) for Chebyshev polynomials. In the first row we likewise have

$$
T _ { 0 } ( x ) \mapsto T _ { 1 } ( x ) = x T _ { 0 } ( x )
$$

since $T _ { 0 } ( x ) = 1$ and $T _ { 1 } ( x ) = x$ . It remains to examine the bottom row. Here it is convenient to imagine that in the difference of matrices defining $C$ above, the “missing” entry $1 / 2$ is added in the $( n , n + 1 )$ position of the first matrix and subtracted again from the $( n , n + 1 )$ position of the second matrix. Then by considering the recurrence relation again we find

$$
T _ { n - 1 } ( x ) \mapsto x T _ { n - 1 } ( x ) - { \frac { 1 } { 2 a _ { n } } } ( a _ { 0 } T _ { 0 } ( x ) + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot + a _ { n } T _ { n } ( x ) ) .
$$

This equation holds for any $x$ , and if $x$ is a root of $p$ , then the term in parentheses on the right vanishes. In other words, if $x$ is a root of $p$ , then $C v$ is equal to $x v$ in every entry, making $v$ an eigenvector of $C$ with eigenvalue $x$ . If $p$ has $n$ distinct roots, this implies that they are precisely the eigenvalues of $C$ , and this completes the proof in the case where $p$ has distinct roots.

If $p$ has multiple roots, we must show that each one corresponds to an eigenvalue of $C$ with the same multiplicity. For this we can consider perturbations of the coefficients $a _ { 0 } , \ldots , a _ { n - 1 }$ of $p$ with the property that the roots become distinct. Each root must then correspond to an eigenvalue of the correspondingly perturbed matrix $C$ , and since both roots of polynomials and eigenvalues of matrices are continuous functions of the parameters, the multiplicities must be preserved in the limit as the amplitude of the perturbations goes to zero.

As mentioned above, the matrix $C$ of (18.1) is called a colleague matrix. Theorem 18.1 has been rediscovered several times, for example by Day & Romero [2005]. Since Specht [1957] there have also been generalizations to other families of orthogonal polynomials besides Chebyshev polynomials, and the associated generalized colleague matrices are called comrade matrices [Barnett 1975a & 1975b]. The generalization is immediate: one need only change the entries of rows 1 to $n - 1$ to correspond to the appropriate recurrence relation.

For an example to illustrate Theorem 18.1, consider the polynomial $p ( x ) =$ $x ( x - 1 / 4 ) ( x - 1 / 2 )$ .

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/4538c54c3096c0ab991b7ee3c1f9d20e8d5c95ed7b5c2307d5607307f3648368.jpg)

Obviously $p$ has roots $0$ , $1 / 4$ , and $1 / 2$ . The Chebyshev coefficients are $- 3 / 8 , 7 / 8$ , $- 3 / 8 , 1 / 4$ :

a = fliplr(chebpoly(p))   
a = -0.3750 0.8750 -0.3750 0.2500

As expected, the colleague matrix (18.1) for this polynomial,

C = [0 1 0; 1/2 0 1/2; 0 1/2 0] - (1/(2\*a(4)))\*[0 0 0; 0 0 0; a(1:3)] ${ \mathrm { ~ \small ~ C ~ } } =$

<table><tr><td>0</td><td>1.0000 0</td></tr><tr><td>0.5000</td><td>0 0.5000</td></tr><tr><td>0.7500</td><td>-1.2500 0.7500</td></tr></table>

has eigenvalues that match the roots of $p$ :

eig(C)

0.500000000000002   
0.249999999999999

In Chebfun, every function is represented by a polynomial or a piecewise polynomial. Theorem 18.1 provides Chebfun with its method of numerical rootfinding, implemented in the Chebfun roots command. For this polynomial $\mathrm { \Delta p }$ , we can call roots to add the roots to the plot, like this:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0002_pages_0071-0140/auto/images/0f3a505ef380cf16e56ba97b6127b80e6ed487af6dbf61e4b795f24fa5999962.jpg)

In this example, $\mathrm { \Delta } _ { \mathrm { { P } } }$ was a polynomial from the start. The real power of Theorem 18.1, however, comes when it is applied to the problem of finding the roots on $[ - 1 , 1 ]$ of a general function $f$ . To do this, we first approximate $f$ by a polynomial and then find the roots of the polynomial. This idea was proposed in Good’s original 1961 paper [Good 1961]. In a more numerical era, it has been advocated in a number of papers by John Boyd, including [Boyd 2002], and it is exploited virtually every time Chebfun is used.

For example, here is the chebfun corresponding to $\cos ( 5 0 \pi x )$ on $[ - 1 , 1 ]$

It doesn’t take long to compute its roots, tic, r $=$ roots(f); toc

Elapsed time is 0.015067 seconds.

The exact roots of this function on $[ - 1 , 1 ]$ are $- 0 . 9 9 , - 0 . 9 7 , \hdots , 0 . 9 7 , 0 . 9 9$ . Inspecting a few of the computed results shows they are accurate to close to machine precision:


<!-- chunk 0003: pages 141-210 -->
ans $=$   
-0.990000000000000   
-0.970000000000000   
-0.950000000000000   
-0.930000000000000   
-0.910000000000000

Changing the function to $\cos ( 5 0 0 \pi x )$ makes the chebfun 10 times longer,

f = cos(500\*pi\*x); length(f)

ans $=$ 1685

One might think this would increase the rootfinding time greatly, since the number of operations for an eigenvalue computation grows with the cube of the matrix dimension. (The colleague matrix has a special structure that can be used to bring the operation count down to $O ( n ^ { 2 } )$ , but this is not done in a straightforward MATLAB call to eig.) However, an experiment shows that the timing is still quite good,

tic, r = roots(f); toc

Elapsed time is 0.151371 seconds.

and the accuracy is still outstanding:

r(1:5)

ans $=$   
-0.999000000000000   
-0.997000000000000   
-0.995000000000000   
-0.993000000000000   
-0.991000000000000

We can make sure all 1000 roots are equally accurate by computing a norm:

exact = [-0.999:0.002:0.999]'; norm(r-exact,inf)

ans $=$ 4.440892098500626e-16

The explanation of this great speed in finding the roots of a polynomial of degree in the thousands is that the complexity of the algorithm has been improved from $O ( n ^ { 3 } )$ to $O ( n ^ { 2 } )$ by recursion. If a chebfun has length greater than 50, the interval is divided recursively into subintervals, with a chebfun constructed on each subinterval of appropriately lower degree. Thus no eigenvalue problem is ever solved of dimension greater than 50. This idea of rootfinding based on recursive subdivision of intervals and Chebyshev eigenvalue problems was developed by John Boyd in the 1980s and 1990s and published by him in 2002 [Boyd 2002]. Details of the original

Chebfun implementation of roots were presented in [Battles 2005], and in 2012 the Chebfun algorithm was speeded up substantially by Pedro Gonnet (unpublished).

These techniques are remarkably powerful for practical computations. For example, how many zeros does the Bessel function $J _ { 0 }$ have in the interval $\lfloor 0 , 5 0 0 0 \rfloor$ ? Chebfun finds the answer in a fraction of a second:

tic, f $=$ chebfun(@(x) besselj(0,x),[0,5000]); r $=$ roots(f); toc, length(r)

Elapsed time is 0.320189 seconds. ans $=$ 1591

What is the 1000th zero?

r(1000)

ans $=$ 3.140807295225079e+03

We readily verify that this zero is an accurate one:

besselj(0,ans)

ans $=$ 6.531871585675192e-15

This example, like a few others scattered around the book, makes use of a chebfun defined on an interval other than the default $[ - 1 , 1 ]$ . The mathematics is straightforward; $[ 0 , 5 0 0 0 ]$ is reduced to $[ - 1 , 1 ]$ by a linear transformation.

Here is another illustration of recursive colleague matrix rootfinding for a highorder polynomial. The function

$$
f ( x ) = e ^ { x } [ { \mathrm { s e c h } } ( 4 \sin ( 4 0 x ) ) ] ^ { \exp ( x ) }
$$

features a row of narrower and narrower spikes. Where in $[ - 1 , 1 ]$ does it take the value 1? We can find the answer by using roots to find the zeros of the equation $f ( x ) - 1 = 0$ :

$\mathbf { f } \mathbf { f } \ = \ \mathcal { Q } \left( \mathbf { x } \right)$ exp(x).\*sech(4\*sin(40\*x)).^exp(x); tic, f $=$ ff(x); r = roots(f-1); toc plot(f), hold on, plot(r,f(r),'or')

Elapsed time is 0.195736 seconds.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/0b48e90ad038745cf2dc85330b880ea1dcc37fcf6e690f490ae7c13f326b03e9.jpg)

Notice that we have found the roots here of a polynomial of quite high degree:

length(f)

ans $=$ 3541

A numerical check confirms that the roots are accurate, max(abs(ff(r)-1))

ans $=$ 2.042810365310288e-13 and zooming in gives perhaps a more convincing plot:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/d7aeb998b15c2f7cfe5cf15561b54b1dcb51e22b29d7fd495ec943544f9d6f13.jpg)

Computations like this are examples of global rootfinding, a special case of global optimization. They are made possible by the combination of fast methods of polynomial approximation with the extraordinarily fast and accurate methods for matrix eigenvalue problems that have been developed in the time since Francis invented the QR algorithm in the very same year as Good proposed his colleague matrices [Francis 1961]. (A crucial algorithmic feature that makes these eigenvalue calculations so accurate is known as “balancing,” introduced in [Parlett & Reinsch 1969]—see [Toh & Trefethen 1994] and Exercise 18.3.)

Global rootfinding is a step in many other practical computations. It is used by Chebfun, for example, in computing minima, maxima, $\infty$ -norms, 1-norms, and absolute values.

It is worth mentioning that as an alternative to eigenvalue problems based on Chebyshev expansion coefficients, it is possible to relate roots of polynomials to eigenvalue problems (or generalized eigenvalue problems) constructed from function values themselves at Chebyshev or other points. Mathematical processes along these lines are described in [Fortune 2001], [Amiraslani et al. 2004], and [Amiraslani 2006]. So far there has not been much numerical exploitation of these ideas, but preliminary experiments suggest that in the long run they may be competitive.

We close this chapter by clarifying a point that may have puzzled the reader, and which has fascinating theoretical connections. In plots like the last two, we see only real roots of a function. Yet if the function is a chebfun based on a polynomial representation, won’t there be complex roots too? This is indeed the case, but the Chebfun roots command by default returns only those roots in the interval where the function is defined. As mentioned in Exercise 14.2, this default behavior can be overridden by the use of the flags 'all' or 'complex'. For example, suppose we make a chebfun corresponding to the function $f ( x ) = ( x - 0 . 5 ) / ( 1 + 1 0 x ^ { 2 } )$ , which has just one root in the complex plane, at $x = 0 . 5$ :

$\textbf { f } = \textbf { ( x - 0 . 5 ) } / ( 1 + 1 0 * \mathbf x \hat { \textbf { \ i } } 2 ) ; \ \mathrm { 1 e n g t h } ( \mathbf f )$

Typing roots alone gives just the root at $x = 0 . 5$ :

roots(f)

ans $=$ 0.500000000000006

With roots(f,’all’), however, we get 106 roots:

r = roots(f,'all'); length(r)

ans $=$ 106

The complex roots are meaningless from the point of view of the underlying function $f$ ; they are an epiphenomenon that arises in the process of approximating $f$ on $[ - 1 , 1 ]$ . A plot reveals that they have a familiar distribution, lying almost exactly on the Chebfun ellipse for this function:

chebellipseplot(f,'r'), hold on, plot(r,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/57ac6591ccdeeaeab82ef8458c6ddb46314a600434aa53bfd66d02cc6c4594cf.jpg)

The fact that roots of best and near-best approximations cluster along the maximum Bernstein ellipse of analyticity is a special case of a theorem due to Walsh [1959]. Blatt and Saff [1986] extended Walsh’s result to the situation in which the function being approximated has no ellipse of analyticity but is merely continuous on $[ - 1 , 1 ]$ . They showed that in this case, the zeros of the best approximants cluster at every point of the interval as $n  \infty$ . This phenomenon applies not only to the best approximations but to all near-best approximations that are maximally convergent as defined in Chapter 12, and hence in particular to Chebyshev interpolants. Here, for example, are the roots of the degree 100 Chebyshev interpolant to $| x |$ :

f = chebfun('abs(x)',101); length(f), r = roots(f,'all'); plot([-1,1],[0,0],'r'), hold on, plot(r,'.')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/622668859309b51b0eb9398fbe20d615d1c1f022a582f796b0282e89cfaa2e20.jpg)

The Walsh and Blatt–Saff theorems are extensions of Jentzsch’s theorem, which asserts that the partial sums of a Taylor series have roots clustering along every point of the circle of convergence [Jentzsch 1914].

Summary of Chapter 18. The roots of a polynomial are equal to the eigenvalues of a colleague matrix formed from its coefficients in a Chebyshev series, tridiagonal except in the final row. This identity, combined with recursive subdivision, leads to a stable and efficient numerical method for computing roots of a polynomial in an interval. For orthogonal polynomials other than Chebyshev, the colleague matrix generalizes to a comrade matrix with the same almost-tridiagonal structure.

Exercise 18.1. Companion matrix. Prove that the roots of the polynomial $p ( x ) = a _ { 0 } +$ $a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ , $a _ { n } \neq 0$ , are the eigenvalues of the $n \times n$ matrix with zero entries everywhere except for the value 1 in the first superdiagonal and the values $- a _ { 0 } / a _ { n } , \ldots , - a _ { n - 1 } / a _ { n }$ in the last row.

Exercise 18.2. Four forms of colleague matrix. A matrix $C$ has the same eigenvalues and eigenvalue multiplicities as $C ^ { T }$ and also as $S C S ^ { - 1 }$ , where $S$ is any nonsingular matrix. Use these properties to derive three alternative forms of the colleague matrix in which the Chebyshev coefficients appear in (a) the first row, (b) the first column, and (c) the last column.

Exercise 18.3. Some forms more stable than others. Mathematically, all the matrices described in the last exercise have the same eigenvalues. Numerically, however, some may suffer more than others from rounding errors, and in fact Chebfun works with the first-column option for just this reason. (a) Determine the $1 1 \times 1 1$ colleague matrix corresponding to roots $- 1 , - 0 . 8 , - 0 . 6 , \dots , 1$ . Get the entries of the matrix exactly, either analytically or by intelligent guesswork based on the MATLAB rat command. (b) How does the accuracy of the eigenvalues of the four matrix variants compare? Which one is best? Is the difference significant? (c) What happens if you solve the four eigenvalue problems again using the MATLAB 'nobalance' option in the eig command?

Exercise 18.4. Legendre polynomials. The Legendre polynomials satisfy $P _ { 0 } ( x ) = 1$ , $P _ { 1 } ( x ) = x$ , and, for $k \geq 1$ , the recurrence relation (17.6). (a) Derive a “comrade matrix” analogue of Theorem 18.1 for the roots of a polynomial expanded as a linear combination of Legendre polynomials. (b) Verify numerically that the roots of the particular polynomial $P _ { 0 } + P _ { 1 } + \cdots + P _ { 5 }$ match the prediction of your theorem. (Try sum(legpoly(0:5),2) to construct this polynomial elegantly in Chebfun and don’t forget to use roots(...,'all').) Exercise 18.5. Complex roots. For each of the following functions defined on $[ - 1 , 1 ]$ , construct corresponding chebfuns and plot all their roots in the complex plane with plot(roots(f,'all')). Comment on the patterns you observe. (Your comments are not expected to go very deep.) (a) $x ^ { 2 0 } - 1$ , (b) $\exp ( x ) ( x ^ { 2 0 } - 1 )$ , (c) $1 / ( 1 + 2 5 x ^ { 2 } )$ , (d $x \exp ( 3 0 i x )$ , (e) $\sin ( 1 0 \pi x )$ , (f) $\sqrt { 1 . 1 - x }$ , (g) an example of your own choosing.

Exercise 18.6. The Szeg˝o curve. If $f$ is entire, then it has no maximal Bernstein ellipse of analyticity. Plot the roots in the complex $_ x$ -plane of the Chebfun polynomial approximation to $e ^ { x }$ on $[ - 1 , 1 ]$ and, for comparison, the “Szeg˝o curve” defined by $| x e ^ { 1 - x } | =$ 1 and $| x | \le 1$ [Szeg˝o 1924, Saff & Varga 1978b, Pritsker & Varga 1997]. More precisely, for the comparison, rescale the Szeg˝o curve by multiplying it by the polynomial degree.

Exercise 18.7. Roots of random polynomials. (a) Use the MATLAB roots command to plot the roots of a polynomial $p ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { 2 0 0 } z ^ { 2 0 0 }$ with coefficients selected from the standard normal distribution. (b) Use chebfun('randn(201,1)','coeffs') and plot(roots(p,'all')) to plot the roots of a polynomial $p ( x ) = a _ { 0 } T _ { 0 } + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot +$ $a _ { 2 0 0 } T _ { 2 0 0 } ( x )$ with the same kind of random coefficients. (Effects like these are analyzed rigorously in [Shiffman & Zelditch 2003].)

# Chapter 19. Clenshaw–Curtis and Gauss Quadrature

One thing that is famous about Legendre points and polynomials is their connection with Gauss quadrature, invented by Gauss [1814]. Chebyshev points, similarly, are the basis of Clenshaw–Curtis quadrature [Clenshaw & Curtis 1960], and equispaced points are the basis of Newton–Cotes quadrature. Quadrature is the standard term for the numerical calculation of integrals. It is one of the areas where approximation theory has an immediate link to applications, as we shall see in Theorems 19.3–19.5.

In the basic quadrature problem, we are given a function $f \in C ( [ - 1 , 1 ] )$ and wish to calculate

$$
I = \int _ { - 1 } ^ { 1 } f ( x ) d x .
$$

(More generally the integral may include a weight function $w ( x )$ as in (17.1).) There is a standard idea for doing this that is the basis of the Gauss, Clenshaw–Curtis, and Newton–Cotes formulas and many others besides. Given $n \geq 0$ , we sample $f$ at a certain set of $n + 1$ distinct nodes $x _ { 0 } , \ldots , x _ { n }$ in $[ - 1 , 1 ]$ . We then approximate $I$ by $I _ { n }$ , the exact integral of the degree $n$ polynomial interpolant $p _ { n }$ of $f$ in these nodes:

$$
I _ { n } = \int _ { - 1 } ^ { 1 } p _ { n } ( x ) d x .
$$

One might wonder, Why use a polynomial rather than some other interpolant? This is a very good question, and in Chapter 22 we shall see that other interpolants may in fact be up to $\pi / 2$ times more efficient. Nevertheless, polynomial interpolants have been the standard idea in numerical quadrature since the 18th century.

To integrate $p _ { n }$ , we do not construct it explicitly. Instead, $I _ { n }$ is computed from

the formula

$$
I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) ,
$$

where the numbers $w _ { 0 } , \ldots , w _ { n }$ are a set of $n + 1$ weights that have been predetermined so that the value of $I _ { n }$ will come out right. From (5.1) it is clear that the weights must be the integrals of the Lagrange polynomials,

$$
w _ { k } = \int _ { - 1 } ^ { 1 } \ell _ { k } ( x ) d x .
$$

Another way to write (19.3) is to say that $I _ { n }$ is given by an inner product,

$$
I _ { n } = w ^ { T } v ,
$$

where $w$ and $\boldsymbol { v }$ are column vectors of the weights $w _ { k }$ and function values $f ( x _ { k } )$ . Any linear process of computing an approximate integral from $n + 1$ sample points must be representable in this inner product form, and the integration of polynomial interpolants is a linear process. The mapping from $\{ f ( x _ { k } ) \}$ to $I _ { n }$ is a linear functional (Exercise 19.1).

When the weights $\{ w _ { k } \}$ of a quadrature formula (19.3) are determined by the principle of integrating the polynomial interpolant, i.e., by (19.4), the formula is said to be interpolatory. (Logically, the term should really be polynomial interpolatory.) For the following theorem, we say that a formula is exact when applied to $f$ if the result it gives is the exactly correct integral of $f$ .

Theorem 19.1. Polynomial degree of quadrature formulas. For any $n \geq 0$ , an $( n + 1 )$ -point interpolatory quadrature formula such as Clenshaw–Curtis, Gauss, or Newton–Cotes is exact for $f \in \mathcal { P } _ { n }$ . The $( n + 1 )$ -point Gauss formula is exact for $f \in \mathscr { P } _ { 2 n + 1 }$ .

Proof. Since an interpolatory formula is constructed by integration of a polynomial interpolant of degree $n$ , it is immediate that it is exact for $f \in \mathcal { P } _ { n }$ . The nontrivial property to be established is that Gauss quadrature achieves more than this, being exact for polynomials all the way up to degree $2 n + 1$ . The following standard argument, based on orthogonal polynomials, comes from [Jacobi 1826]. Gauss’s original work 12 years earlier made use of continued fractions rather than orthogonal polynomials.

Suppose that $f \in \mathcal { P } _ { 2 n + 1 }$ . Such a function can be written in the form $f ( x ) =$ $P _ { n + 1 } ( x ) q _ { n } ( x ) + r _ { n } ( x )$ , where $P _ { n + 1 }$ is the $( n + 1 ) \mathrm { s t }$ Legendre polynomial and $q _ { n } , r _ { n } \in$ $\mathcal { P } _ { n }$ . This implies

$$
I = \int _ { - 1 } ^ { 1 } f ( x ) d x = \int _ { - 1 } ^ { 1 } P _ { n + 1 } ( x ) q _ { n } ( x ) d x + \int _ { - 1 } ^ { 1 } r _ { n } ( x ) d x .
$$

The first of the integrals on the right is zero because of the orthogonality property of Legendre polynomials, leaving us with

$$
I = \int _ { - 1 } ^ { 1 } r _ { n } ( x ) d x .
$$

Now consider $I _ { n }$ , the $( n + 1 )$ -point Gauss quadrature approximation to $I$ . The nodes of this formula are the zeros of $P _ { n + 1 } ( x )$ . Accordingly, at each node $x _ { k }$ we have $f ( x _ { k } ) = r _ { n } ( x _ { k } )$ . Thus the value $I _ { n }$ the Gauss formula gives for $f$ will be the same as the value it gives for $r _ { n }$ . But $\boldsymbol { r } _ { n } \in \mathcal { P } _ { n }$ , so this value is exactly the integral of $r _ { n }$ , that is, ${ \boldsymbol { I } } _ { n } = { \boldsymbol { I } }$ .

Theorem 19.1 is famous, but we shall see that it is misleading. It suggests that there is a significant gap between Clenshaw–Curtis and Newton–Cotes quadrature, with one rate of convergence, and Gauss quadrature, with a rate twice as high. In fact, the great gap is between Newton–Cotes, which does not converge at all in general, and both Clenshaw–Curtis and Gauss, which converge for every continuous $f$ and do so typically at similar rates. The crucial distinction is that the weights $w _ { k }$ for both the Clenshaw–Curtis and the Gauss formulas are positive [Imhof 1963], whereas for Newton–Cotes they oscillate in sign and diverge to $\infty$ (Exercise 19.9).

First, let us give some more details of the Clenshaw–Curtis and Gauss formulas. For Clenshaw–Curtis quadrature, one way to compute $I _ { n }$ is by constructing the weight vector $w$ explicitly. It can be shown that the weights are all positive and sum to 2 (the same properties also hold for Gauss quadrature weights, whose computation we discuss later in the chapter). From a practical point of view, this approach may be advantageous for integrating a collection of functions on a single Chebyshev grid. There is a classical formula for calculation of the weights with $O ( n ^ { 2 } )$ operations [Davis $\&$ Rabinowitz 1984, Trefethen 2000], and it is also possible to compute the weights faster, in $O ( n \log n )$ operations, using the FFT [Waldvogel 2006]. This fast algorithm is invoked by Chebfun when the command chebpts is called with two arguments, as we illustrate with $n + 1 = 3$ :

[nodes,weights] $=$ chebpts(3)

0.333333333333333 1.333333333333333 0.333333333333333

By increasing 3 to one million we see the speed of Waldvogel’s algorithm:

tic, [nodes,weights] $=$ chebpts(1000000); toc

Elapsed time is 0.108811 seconds.

The other way to carry out Clenshaw–Curtis quadrature, simplest when just one or a small number of integrands are involved, is to use the FFT to transform the problem to coefficient space (see Chapter 3) at a cost of $O ( n \log n )$ operations per integrand. (This idea was not proposed by Clenshaw and Curtis, who wrote before the rediscovery of the FFT in 1965, but by Morven Gentleman a few years later [Gentleman 1972a, 1972b].) To see how this works, we observe that the integral of the Chebyshev polynomial $T _ { k }$ from $^ { - 1 }$ to $1$ is zero if $k$ is odd and

$$
\int _ { - 1 } ^ { 1 } T _ { k } ( x ) d x = { \frac { 2 } { 1 - k ^ { 2 } } }
$$

if $k$ is even (Exercise 19.6). This gives us the following theorem, the basis of the FFT realization of Clenshaw–Curtis quadrature.

Theorem 19.2. Integral of a Chebyshev series. The integral of a degree $n$ polynomial expressed as a Chebyshev series is

$$
\int _ { - 1 } ^ { 1 } \sum _ { k = 0 } ^ { n } c _ { k } T _ { k } ( x ) d x \ = \quad \sum _ { k = 0 , k { \mathrm { e v e n } } } ^ { n } { \frac { 2 c _ { k } } { 1 - k ^ { 2 } } } .
$$

Proof. The proof follows from (19.6).

Chebfun applies Theorem 19.2 every time one types sum(f), and this theorem is also the basis of Waldvogel’s algorithm mentioned above.

By combining (19.6) with Theorems 8.1 and 19.1, we can now write down a theorem about the geometric convergence of Clenshaw–Curtis and Gauss quadrature for analytic integrands. For Gauss quadrature, this estimate is due to Rabinowitz [1969], and the extension to Clenshaw–Curtis can be found in [Trefethen 2008]. This result is fundamental and very important. For analytic integrands, the Gauss and Clenshaw–Curtis formulas converge geometrically. Every numerical analysis textbook should state this fact.

Theorem 19.3. Quadrature formulas for analytic integrands. Let a function $f$ be analytic in $[ - 1 , 1 ]$ and analytically continuable to the open Bernstein ellipse $E _ { \rho }$ , where it satisfies $| f ( z ) | \leq M$ for some $M$ . Then $( n + 1 )$ -point Clenshaw– Curtis quadrature with $n \geq 2$ applied to $f$ satisfies

$$
| I - I _ { n } | \leq { \frac { 6 4 } { 1 5 } } { \frac { M \rho ^ { 1 - n } } { \rho ^ { 2 } - 1 } }
$$

and $( n + 1 )$ -point Gauss quadrature with $n \geq 1$ satisfies

$$
\left. I - I _ { n } \right. \leq \frac { 6 4 } { 1 5 } \frac { M \rho ^ { - 2 n } } { \rho ^ { 2 } - 1 } .
$$

The factor $\rho ^ { 1 - n }$ in (19.7) can be improved to $\rho ^ { - n }$ if $n$ is even, and the factor 64/15 can be improved to 144/35 if $n \geq 4$ in (19.7) or $n \geq 2$ in (19.8).

Proof. If the constants 64/15 are increased to 8 and $\rho ^ { 2 } - 1$ is reduced to $\rho - 1$ , these conclusions can be obtained as corollaries of Theorem 8.2. The key is to note that the error in integrating $f$ will be the same as the error in integrating $f - f _ { n }$ . Applying the triangle inequality, this gives us

$$
| I - I _ { n } | \leq | I ( f - f _ { n } ) | + | I _ { n } ( f - f _ { n } ) | .
$$

By Theorem 8.2, $| ( f - f _ { n } ) ( x ) | \leq 2 M \rho ^ { - n } / ( \rho - 1 )$ for each $| x |$ . Since the interval $[ - 1 , 1 ]$ has length 2, this implies

$$
\vert I ( f - f _ { n } ) \vert \leq \frac { 4 M \rho ^ { - n } } { \rho - 1 } .
$$

In addition to this, there also holds the analogous property

$$
\left| I _ { n } ( f - f _ { n } ) \right| \leq { \frac { 4 M \rho ^ { - n } } { \rho - 1 } } .
$$

This follows from the fact that the weights are positive.

To get the sharper results stated, we use an additional fact: both Gauss and Clenshaw–Curtis formulas get the right answer, namely zero, when integrating an odd function. In particular the error is zero in integration of $T _ { k } ( x )$ for any odd $k$ . Now by Theorem 19.1, Gauss quadrature is exact through the term of degree $2 n + 1$ in the Chebyshev expansion of $f$ . Since odd terms do not contribute, we see that the error in integrating $f$ by $( n + 1 )$ -point Gauss quadrature will thus be the error in integrating

$$
a _ { 2 n + 2 } T _ { 2 n + 2 } ( x ) + a _ { 2 n + 4 } T _ { 2 n + 4 } ( x ) + \cdot \cdot \cdot ,
$$

a series in which the smallest index that appears is at least 4. Now by (19.6), the true integral of $T _ { k }$ for $k \geq 4$ is of magnitude at most 2/15. When $T _ { k }$ is integrated over $[ - 1 , 1 ]$ by the Gauss quadrature formula, the result will be of magnitude at most 2 since the weights are positive and add up to 2. Thus the error in integrating each $T _ { k }$ is at most $2 + 2 / 1 5 = 3 2 / 1 5$ . Combining this estimate with the bound $| a _ { k } | \leq 2 M \rho ^ { - k }$ of Theorem 8.1 gives (19.8). The argument for (19.7) is analogous. For the improvement from 64/15 to 144/35, see Exercise 19.5.

Just as Theorem 19.3 follows from the results of Chapter 8 for analytic integrands, there is an analogous result for differentiable integrands based on the results of Chapter 7.

Theorem 19.4. Quadrature formulas for differentiable integrands. For any $f \in C ( [ - 1 , 1 ] )$ , both the Clenshaw–Curtis and Gauss approximations $I _ { n }$ converge to the integral $I$ as $n  \infty$ . For an integer $\nu \geq 1$ , let $f$ and its derivatives through $f ^ { ( \nu - 1 ) }$ be absolutely continuous on $[ - 1 , 1 ]$ and suppose the νth derivative $f ^ { ( \nu ) }$ is of bounded variation $V$ . Then $( n + 1 )$ -point Clenshaw–Curtis quadrature applied to $f$ satisfies

$$
| I - I _ { n } | \leq \frac { 3 2 } { 1 5 } \frac { V } { \pi \nu ( n - \nu ) ^ { \nu } }
$$

for $n > \nu$ and $( n + 1 )$ -point Gauss quadrature satisfies

$$
| I - I _ { n } | \leq \frac { 3 2 } { 1 5 } \frac { V } { \pi \nu ( 2 n + 1 - \nu ) ^ { \nu } }
$$

for $n \geq \nu / 2$ .

Proof. The first assertion, for arbitrary continuous $f$ , is due to Stieltjes [1884]. As for (19.9) and (19.10), these can be derived as in the previous proof, but now using Theorem 7.2.

Here is a numerical example, the integration of the function (18.1) with a sequence of spikes:

$$
I = \int _ { - 1 } ^ { 1 } e ^ { x } [ { \mathrm { s e c h } } ( 4 \sin ( 4 0 x ) ) ] ^ { \mathrm { e x p } ( x ) } d x
$$

$\mathbf { f } \mathbf { f } \ = \ \mathcal { Q } \left( \mathbf { x } \right)$ exp(x).\*sech(4\*sin(40\*x)).^exp(x);$\mathrm { ~ x ~ } =$ chebfun $( \mathbf { \partial } ^ { \prime } \mathbf { x } ^ { \prime } )$ ; f $=$ ff(x); plot(f)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/23226133b7fe630874e30104b8115d38e008ccede804b35a99658e2c5102e39a.jpg)

The corresponding chebfun is not exactly short:

length(f)

ans $=$ 3541

Nevertheless, Chebfun computes the integral in a fraction of a second:

sum(f)

ans = 0.543384000907901

Now let us look at Gauss quadrature. The nodes for the $( n + 1 )$ -point Gauss formula are the roots of the Legendre polynomial $P _ { n + 1 } ( x )$ . A good method for computing these numbers is implicit in Theorem 18.1 and the comment after it. According to that theorem, the roots of a polynomial expressed as a Chebyshev series are equal to the eigenvalues of a colleague matrix whose structure is tridiagonal apart from a nonzero final row. If the Chebyshev series reduces to the single polynomial $T _ { n + 1 }$ , the matrix reduces to tridiagonal without the extra row. Similarly the roots of a polynomial expressed as a series in Legendre polynomials are the eigenvalues of a comrade matrix, which is again tridiagonal except for a final row, and for the roots of $P _ { n + 1 }$ itself, the matrix reduces to tridiagonal. When symmetrized, this matrix is called a Jacobi matrix (Exercise 19.7). The classic numerical algorithm for implementing Gauss quadrature formulas comes from Golub and Welsch in 1969, who showed that the weights as well as the nodes can be obtained by solving the eigenvalue problem for this Jacobi matrix [Golub $\&$ Welsch 1969]. The Golub– Welsch algorithm can be coded in six lines of MATLAB (see gauss.m in [Trefethen 2000]), and the operation count is in principle $O ( n ^ { 2 } )$ , although it is $O ( n ^ { 3 } )$ in the simple implementation since MATLAB does not offer a command to exploit the tridiagonal structure of the eigenvalue problem.

For larger values of $n$ , a much faster alternative algorithm was introduced by Glaser, Liu, and Rokhlin [2007], based on numerical solution of certain linear ordinary differential equations by high-order Taylor series approximations combined with Newton iteration. This GLR algorithm shrank the operation count dramatically to $O ( n )$ and became the default algorithm invoked by Chebfun during 2009– 2012 when the legpts command was called with two output arguments. Most recently even faster algorithms have been introduced by Hale and Townsend [2013] and Bogaert [2014]. The key idea of the Hale–Townsend algorithm is to start from high-accuracy asymptotic approximations for nodes and then take one or two Newton steps, with $P _ { n }$ and $P _ { n } ^ { \prime }$ evaluated to machine precision by known asymptotic formulas. When $n$ is large enough, one may not even need any Newton steps at all. A crucial feature is that the method treats the nodes independently, so that it vectorizes readily, and this is a primary reason why it is approximately 20 times faster than the GLR algorithm in a MATLAB implementation.

Following the illustration of Clenshaw–Curtis quadrature earlier, here are nodes and weights for Gauss quadrature with $n + 1 = 3$ :

[nodes,weights] = legpts(3)   
nodes $=$ -0.774596669241483 0 0.774596669241483   
weights $=$ 0.555555555555556 0.888888888888889 0.555555555555556

And here is the time it takes to compute Gauss quadrature nodes and weights for one million points, about the same as for Clenshaw–Curtis:

tic, [nodes,weights] $=$ legpts(1000000); toc

Elapsed time is 0.089773 seconds.

For example, here is the integral (19.11) computed by $n$ -point Gauss quadrature for various values of $n$ . We write $\mathtt { w } { * } \mathtt { f f } \left( \mathtt { s } \right)$ rather than $\kappa ^ { \prime } { \ast } \mathbf { f } \mathbf { f } \left( \mathbf { s } \right)$ since $w$ as returned by legpts is a row vector, not a column vector.

for $\texttt { n } = \phantom { - } 5 0 0 : 5 0 0 : 1 5 0 0$ tic, $[ \mathbf { s } , \mathbf { w } ] ~ = ~ \mathrm { { 1 e g p t s } } \left( \mathrm { { n + 1 } } \right) ; ~ \mathrm { { 1 } } ~ = ~ \mathsf { w } { * } \mathbf { f } \mathsf { f } \left( \mathbf { s } \right) ; ~ \mathsf { t } ~ = ~ \mathsf { t o c } ;$ fprintf $\because n = \% 4 d$ , $\mathrm { ~ I ~ } = \ \% 1 6 . 1 4 \pounds$ , time $=$ %6.4f\n',n,I,t)   
end

$$
\begin{array} { r l r l } & { \mathtt { n } = } & { 5 0 0 , \quad \mathtt { I } \ = \ 0 . 5 4 3 3 9 2 7 5 8 1 0 6 2 2 , \quad \mathtt { t i m e } \ = \ 0 . 0 0 1 8 } \\ & { \mathtt { n } = } & { 1 0 0 0 , \quad \mathtt { I } \ = \ 0 . 5 4 3 3 8 4 0 0 1 8 2 5 5 8 , \quad \mathtt { t i m e } \ = \ 0 . 0 0 2 7 } \\ & { \mathtt { n } = } & { 1 5 0 0 , \quad \mathtt { I } \ = \ 0 . 5 4 3 3 8 4 0 0 0 9 0 7 8 4 , \quad \mathtt { t i m e } \ = \ 0 . 0 0 3 7 } \end{array}
$$

Gauss quadrature has not often been employed for numbers of nodes in the thousands, because with traditional algorithms the computations are too expensive. It is clear from this experiment that the GLR and Hale–Townsend algorithms make such computations feasible after all.

So is Gauss quadrature the formula of choice? In particular, how does it compare with Clenshaw–Curtis quadrature as $n \to \infty$ ? As mentioned above, the traditional expectation, based on Theorem 19.1 and seemingly supported by Theorems 19.3 and 19.4, is that Gauss should converge twice as fast as Clenshaw–Curtis. However, numerical experiments show that the truth is not so simple. We begin with the easy integrand $f ( x ) = \exp ( - 1 0 0 x ^ { 2 } )$ .

er $\begin{array} { r l } { = } & { \Theta ( \mathbf { x } ) \ \exp \left( { - 1 0 0 * \mathbf { x } . \hat { \phantom { . } } \mathrm { \hat { \Phi } } ^ { 2 } } \right) ; \mathrm { ~ I ~ \ = ~ \mathbf { s u m } ( \mathrm { c h e b f u n } ( \mathrm { g g } ) ) } ; } \\ { \mathrm { r c c } = } & { [ ] ; \mathrm { ~ e r r g a u s s \ = ~ [ ] ~ ; ~ \boldsymbol { n } = ~ \boldsymbol { \Omega } [ \hat { \omega } , ~ \boldsymbol { n } = ~ \boldsymbol { \Omega } _ 2 : 2 : 8 0 } ; } \\ { \mathrm { ~ r ~ \hat { \omega } ~ \in ~ \boldsymbol { n } { \operatorname { m } } ~ \hat { \omega } ~ } } \\ { \mathrm { ~ I c c ~ = ~ \boldsymbol { s u m } ( \mathrm { c h e b f u n } ( \mathrm { g g } , \boldsymbol { n } + 1 ) ) ; ~ e r r c c } = } & { \left[ { \mathrm { e r r c c } \ \mathrm { \hat { \omega } a b s } \left( \mathrm { I - I c c } \right) } \right] ; } \\ { \mathrm { ~ \hat { \omega } , \tilde { \boldsymbol { u } } ] ~ = ~ \mathbf { 1 } e g p t s ( \boldsymbol { n } + 1 ) ; ~ \hat { \omega } ~ } } \\ { \mathrm { ~ I g a u s s \ = ~ \mathbf { w } * g g ( \hat { \omega } s ) } ; \mathrm { ~ e r r g a u s s \ = ~ \begin{array} { l } { \left[ \mathrm { e r r g a u s s } \ { a b s } \ { ( \mathrm { I - I g a u s s } ) } \right] ; } \\ { \mathrm { ~ e r r g a u s s } \ \mathrm { a b s } \ ( \mathrm { I - I g a u s s } ) } \end{array} } } \end{array}$ fo   
end   
semilogy(nn,errcc,'.-'), hold on, semilogy(nn,errgauss,'h-m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/639b448a0f07d31574bc929f9f98732f9f97b44ce42c761b34b656ee01eca676.jpg)

This behavior is typical: for smaller values of $n$ , Clenshaw–Curtis (dots) and Gauss quadrature (stars) have similar accuracy, not a difference of a factor of 2. This effect was pointed out by Clenshaw and Curtis in their original paper [1960]. Only at a sufficiently large value of $n$ , if the integrand is analytic, does a kink appear in the Clenshaw–Curtis convergence curve, whose further convergence is then about half as fast as before. An explanation of this effect based on ideas of rational approximation is given in Figures 4–6 of [Trefethen 2008], and another explanation based on aliasing can be derived from Theorems 4.2 and 19.2 and goes back to O’Hara and Smith [1968] (Exercise 19.4). For a full analysis, see [Weideman $\&$ Trefethen 2007a].

Here is a similar comparison for the harder integral (19.11):

I = sum(f); $\mathtt { n n } \ = \ 5 0 : 5 0 : 2 0 0 0$ ;   
errcc $= ~ [ ]$ ; errgauss $=$ [];   
for $\texttt { n } = \texttt { n n }$ Icc $=$ sum(chebfun(ff, $\tt { n } { + } 1 \tt {  }$ )); errcc $=$ [errcc abs(I-Icc)]; [s,w] = legpts $\left( \mathtt { n } + 1 \right)$ ; Igauss $=$ w\*ff(s); errgauss $=$ [errgauss abs(I-Igauss)];   
end   
semilogy(nn,errcc,'.-'), hold on, semilogy(nn,errgauss,'h-m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/ae74f1a813ebbd75928cab325bc2c247f387fd0a9f4ee4b4e3cfea080ba54d6c.jpg)

This time, for the values of $n$ under study, the kink does not appear at all. Clenshaw–Curtis has approximately the same accuracy as Gauss throughout, and in particular, it obtains the correct integral to machine precision by around $n = 1 8 0 0$ , which is about half the length of the chebfun, length(f), reported earlier! This is typical of Clenshaw–Curtis quadrature: just as with Gauss quadrature, the quadrature value converges about twice as fast as the underlying polynomial approximation, even though Theorems 19.1, 19.3, and 19.4 give no hint of such behavior.

There is a theorem that substantiates this effect. The following result, whose proof we shall not give, comes from [Trefethen 2008].

Theorem 19.5. Clenshaw–Curtis quadrature for differentiable integrands. Under the hypotheses of Theorem 19.4, the same conclusion (19.10) also holds for $( n + 1 )$ -point Clenshaw–Curtis quadrature:

$$
| I - I _ { n } | \leq \frac { 3 2 } { 1 5 } \frac { V } { \pi \nu ( 2 n + 1 - \nu ) ^ { \nu } } .
$$

The only difference is that this bound applies for all sufficiently large $n$ (depending on $\nu$ but not $f$ ) rather than for $n \geq \nu / 2$ .

Proof. See [Trefethen 2008]. Here, the definition of $V$ is somewhat different, but this does not affect the argument leading to (19.12).

Theorems 19.4–19.5 are not sharp: Xiang and Bornemann [2012] have shown that the actual convergence rates are one factor of $n$ better than these theorems indicate. I regret that there has not been time to include their results here.

In summary, though Gauss quadrature is more celebrated than Clenshaw–Curtis, its behavior in practice is not much different. For a survey of many aspects of Gauss quadrature, see [Gautschi 1981], and for general information about quadrature, see [Davis & Rabinowitz 1984]. In practice it is common to use adaptive formulas of low or moderate order rather than letting $n$ increase toward $\infty$ with a global grid, though Chebfun is an exception to this pattern.

As mentioned earlier, both Gauss and Clenshaw–Curtis quadrature grids can be improved by a factor approaching $\pi / 2$ by the introduction of a change of variables, taking us beyond the realm of polynomial approximations. These ideas are discussed in Chapter 22.

We have not said much about Newton–Cotes quadrature formulas, based on equispaced points. For smaller orders these are of practical interest: $n = 4$ gives Simpson’s rule, and Espelid has used Newton–Cotes rules of order up to 33 as the basis of excellent codes coted2a and da2glob for adaptive quadrature [Espelid 2004]. The weights $\{ w _ { j } \}$ of Newton–Cotes formulas, however, oscillate in sign between magnitudes on the order of $2 ^ { n }$ , a reflection of the Runge phenomenon, causing terrible numerical instability for large $n$ . Even in the absence of rounding errors, the results of Newton–Cotes formulas do not converge in general as $n \to \infty$ , even for analytic functions. It was clear upon publication of Runge’s paper in 1901 that such divergence was likely, and a theorem to this effect was proved by P´olya [1933].

We close this chapter with an elegant application of Gauss quadrature nodes and weights pointed out by Wang and Xiang [2012].

Theorem 19.6. Barycentric weights for Legendre points. The barycentric weights of Theorem 5.1 for polynomial interpolation in Legendre points can be written as

$$
\lambda _ { k } = C ( - 1 ) ^ { k } { \sqrt { ( 1 - x _ { k } ^ { 2 } ) w _ { k } } } ,
$$

where $x _ { k }$ and $w _ { k }$ are the nodes and weights for $( n + 1 )$ -point Gauss quadrature.

Proof. Both the barycentric weights $\left\{ \lambda _ { k } \right\}$ and the quadrature weights $\{ w _ { k } \}$ are related to the node polynomial $\ell$ . In particular, it is shown in [Winston 1934] that the weights can be written as $w _ { k } = C ( 1 - x _ { k } ^ { 2 } ) ^ { - 1 } [ \ell ^ { \prime } ( x _ { k } ) ] ^ { - 2 }$ .

This theorem implies that polynomial interpolants in Legendre points, just as with Chebyshev points, can be evaluated in $O ( n )$ operations. The formulas are implemented in Chebfun and accessed when one calls legpts, jacpts, hermpts, or lagpts with three output arguments [Hale & Trefethen 2012].

Summary of Chapter 19. Clenshaw–Curtis quadrature is derived by integrating a polynomial interpolant in Chebyshev points, and Gauss quadrature from Legendre points. The nodes and weights for both families can be computed quickly and accurately, even for millions of points. Though Gauss has twice the polynomial order of accuracy of Clenshaw–Curtis, their rates of convergence are approximately the same for nonanalytic integrands.

Exercise 19.1. Riesz Representation Theorem. (a) Look up the Riesz Representation Theorem and write down a careful mathematical statement of it. (b) Show that the computation of an approximate integral $I _ { n }$ from $n + 1$ samples of a function $f \in C ( [ - 1 , 1 ] )$ by integrating the degree $n$ polynomial interpolant through a fixed set of $n + 1$ nodes in $[ - 1 , 1 ]$ is an example of the kind of linear functional to which this theorem applies, provided we work in a finite-dimensional space rather than all of $C ( [ - 1 , 1 ] )$ . (c) In what sense is the Riesz Representation Theorem significantly more general than is needed for this particular application to quadrature?

Exercise 19.2.  -. Evaluate (19.11) with the MATLAB integral command. As a function of the specified precision, what is the actual accuracy obtained and how long does the computation take? How do these results compare with Chebfun sum?

Exercise 19.3. Quadrature weights. (a) Use Chebfun to illustrate the identity (19.4) for Clenshaw–Curtis quadrature in the case $n = 2 0$ , $k = 7$ . (b) Do the same for Gauss quadrature.

Exercise 19.4. Accuracy of Clenshaw–Curtis quadrature. Using theorems of Chapters 4 and 19, derive an exact expression for the error $I \mathrm { ~ - ~ } I _ { n }$ in Clenshaw–Curtis quadrature applied to the function $f ( x ) = T _ { k } ( x )$ for $k > n$ [Gentleman 1972a].

Exercise 19.5. Sharpening Theorem 19.3. Suppose we assume $n \geq 2$ instead of $n \geq 1$ in the Gauss quadrature bound of Theorem 19.3. Show why the constant 64/15 improves to 144/35. What is this actual “constant” as a function of $n$ ?

Exercise 19.6. Integral of a Chebyshev polynomial. Derive the formula (19.6) for the integral of $T _ { k } ( x )$ with $k$ even. (Hint: Following the proof of Theorem 3.1, replace $T _ { k } ( x ) d x$ by $( z ^ { k } + z ^ { - k } ) ( d x / d z ) d z$ .)

Exercise 19.7. Symmetrization in the Golub–Welsch algorithm. The nodes $\{ x _ { j } \}$ of the $( n + 1 )$ -point Gauss quadrature rule are the zeros of the Legendre polynomial $P _ { n + 1 }$ . From the recurrence relation (17.6), it follows as in Theorem 18.1 that they are the eigenvalues of a certain $( n + 1 ) \times ( n + 1 )$ tridiagonal matrix $A$ . (a) Give formulas for the entries of $A$ . (b) Find the unique diagonal matrix $D = \mathrm { d i a g } ( d _ { 0 } , \ldots , d _ { n } )$ with $d _ { 0 } = 1$ and $d _ { j } ~ > ~ 0$ for $j \geq 1$ such that $B = D A D ^ { - 1 }$ , which has the same eigenvalues as $A$ , is real symmetric. What are the entries of $B$ ? (This symmetrized matrix is the Jacobi matrix that is the basis of the Golub–Welsch algorithm.)

Exercise 19.8. Integrating the Bernstein polynomial. Given $f \in C ( [ - 1 , 1 ] )$ , let $B _ { n } ( x )$ be the Bernstein polynomial defined by (6.2) and let $I _ { n }$ be the approximation to $\textstyle \int _ { - 1 } ^ { 1 } f ( x ) d x$ defined by $\begin{array} { r } { I _ { n } = \int _ { - 1 } ^ { 1 } B _ { n } ( x ) d x } \end{array}$ . (a) Show that $I _ { n } = ( n + 1 ) ^ { - 1 } \textstyle \sum _ { k = 0 } ^ { n } f ( k / n )$ (b) Is this an interpolatory quadrature formula? (c) What is its order of accuracy $\alpha$ for smooth integrands as defined by the condition $I - I _ { n } = O ( n ^ { - \alpha } ) ^ { \cdot }$ ?

Exercise 19.9. Nonnegative weights and convergence. Suppose the weights $w _ { k }$ of an interpolatory quadrature formula (19.3) are all nonnegative. Show using the Weierstrass approximation theorem that $I _ { n } \to I$ for any continuous integrand $f$ . (P´olya [1933] showed that uniform boundedness of the sums of the absolute values of the weights is necessary and sufficient for convergence for all $f$ .)

# Chapter 20. Carath´eodory–Fej´er Approximation

We have seen that Chebyshev interpolants are near-best approximations in the sense that they come within a factor of at most $O ( \log n )$ of best approximations, usually even closer. For many applications, this is all one could ask for. But there is another kind of near-best approximations that are so close to best that for smooth functions, they are often indistinguishable from best approximations to machine precision on a computer. These are $\mathit { C F }$ (Carath´eodory–Fej´er) approximations, introduced by Gutknecht and Trefethen [1982]. Earlier related ideas were proposed in [Darlington 1970, Elliott 1973, Lam 1972, Talbot 1976], and the theoretical basis goes back to the early 20th century [Carath´eodory & Fej´er 1911, Schur 1918].10

Before explaining the mathematics of CF approximants, let us illustrate the remarkable degree of near-optimality they sometimes achieve. Here is the optimal $\infty$ -norm error in approximation of $f ( x ) = e ^ { x }$ on $[ - 1 , 1 ]$ by a polynomial of degree 2:

$\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun('x'); f = exp(x); n = 2; pbest $=$ minimax(f,n); errbest $=$ norm(f-pbest,inf)

errbest $=$ 0.045017388402819

Here is the corresponding error for CF approximation computed by the Chebfun cf command:

pcf $=$ cf(f,n); errcf $=$ norm(f-pcf,inf)

errcf = 0.045017388414604

These two numbers agree to an extraordinary 9 significant digits. Comparing the best and CF polynomials directly to one another, we confirm that they are almost the same:

norm(pbest-pcf,inf)

# ans $=$ 1.178473985063988e-11

That was for degree $n = 2$ , and the near-optimality of the CF approximants grows stronger as $n$ increases. Let us explore the dependence on $n$ . On a semilog plot, the upper curve in the next figure shows the accuracy of the best polynomial as an approximation to $f ( x )$ , while the lower curve shows the accuracy of the CF polynomial as an approximation to the best polynomial. The two errors are of entirely different orders, and for $n > 3$ , the CF and best polynomials are indistinguishable in floating point arithmetic.

$\mathtt { n n } ~ = ~ 0 : 1 0$ ; err1 = []; err2 = [];   
for $\texttt { n } = \texttt { n n }$ pbest $=$ minimax(f,n); err1 $=$ [err1 norm(f-pbest,inf)]; pcf $=$ cf(f,n); err2 $=$ [err2 norm(pbest-pcf,inf)];   
end   
semilogy(nn,err1,'.-'), hold on, semilogy(nn,err2,'.-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/d76648981e8628108d5b09395f6a61f6be075bf549e534a3bc2852a9bae1cf7f.jpg)

Here is the same experiment repeated for $f ( x ) = \operatorname { t a n h } ( 4 ( x - 0 . 3 ) )$ .

f = tanh(4\*(x-.3)); ${ \tt n n } = 0 : 3 0$ ; err1 $=$ []; $\mathbf { e r r } 2 \ = \ \left[ \mathbf { } \mathbf { } \right]$ ;   
for $\texttt { n } = \texttt { n n }$ pbest $=$ minimax(f,n); err1 $=$ [err1 norm(f-pbest,inf)]; pcf $=$ cf(f,n); err2 $=$ [err2 norm(pbest-pcf,inf)];   
end   
semilogy(nn,err1,'.-'), hold on, semilogy(nn,err2,'.-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/4be6d2ec218d128b5ec2b6bae14ac23f7f20343d37b5af4b7c654d663efb5ad7.jpg)

Again we see that pbest−pcf is much smaller than f−pbest, implying that the CF approximant is for practical purposes essentially optimal. (Concerning the erratic oscillations, see Exercise 20.4.) Yet it is far easier to compute:

tic, minimax(f,20); tbest $=$ toc, tic, cf(f,20); tcf = toc

tbest $=$ 0.0389   
tcf $=$ 0.0098

Turning to a nonsmooth function, here again is the jagged example from Chapter 10 with its best approximation of degree 20:

f $=$ cumsum(sign(sin(20\*exp(x)))); plot(f,'k') tic, [pbest,err] $=$ minimax(f,20); tbest $=$ toc; hold on, plot(pbest)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/2355b5b8e5b6a93935c03f732071bf7d06024a4c20eb4cb53828d1a0facc24cd.jpg)

We saw the error curve before:

plot(f-pbest), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/609153f9f623bceea1209fd607f4b77668097bcd0d528f87550e6340eb16ec47.jpg)

In CF approximation, we must start from a polynomial, not a jagged function. As a rule of thumb, truncating the Chebyshev series at 5 times the degree of the desired approximation is usually pretty safe. Here is what we get:

$\yen 100 ~ =$ chebfun(f,100); tic, pcf $=$ cf(f100,20); tcf $=$ toc; plot(f-pcf), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/02fdd95c1b8a1523f0cf69d0f0ff4404ea19b9f4f87fce661df238205559118a.jpg)

Evidently the error falls short of optimality by just a few percent. Yet again the computation is much faster:

tbest, tcf

tbest $=$ 0.9996   
tcf $=$ 0.0105

Here for comparison is the error in Chebyshev interpolation.

pinterp $=$ chebfun(f,21); hold off, plot(f-pinterp), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1,1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/624b6a13cda812ad123b782025aa4cffc3ea886e50bd210045df8fe28faf4ce9.jpg)

The time has come to describe what CF approximation is all about. We shall see that the hallmark of this method is the use of eigenvalues and eigenvectors (or singular values and singular vectors) of a Hankel matrix of Chebyshev coefficients.

We start with a real function $f$ on $[ - 1 , 1 ]$ , which we want to approximate by a polynomial of degree $n \geq 0$ . Following Theorem 3.1, we assume that $f$ is Lipschitz continuous, so it has an absolutely convergent Chebyshev series

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } ( x ) .
$$

Since our aim is polynomial approximation, there is no loss of generality if we suppose that $a _ { 0 } = a _ { 1 } = \cdot \cdot \cdot = a _ { n } = 0$ , so that the Chebyshev series of $f$ begins at the term $T _ { n + 1 }$ . For technical simplicity, let us further suppose that the series is a finite one, ending at the term $T _ { N }$ for some $N \geq n + 1$ . Then $f$ has the Chebyshev series

$$
f ( x ) = \sum _ { k = n + 1 } ^ { N } a _ { k } T _ { k } ( x ) .
$$

We now transplant $f$ to a function $F$ on the unit circle in the complex $z$ -plane by defining $F ( z ) = F ( z ^ { - 1 } ) = f ( x )$ for $| z | = 1$ , where $x = ( z + z ^ { - 1 } ) / 2$ . As in the proof of Theorem 3.1, this gives us a formula for $F$ as a Laurent polynomial,

$$
F ( z ) = \frac { 1 } { 2 } \sum _ { k = n + 1 } ^ { N } a _ { k } ( z ^ { k } + z ^ { - k } ) .
$$

We can divide $F ^ { \prime }$ into two parts, $F ( z ) = G ( z ) + G ( z ^ { - 1 } )$ , with

$$
G ( z ) = \frac { 1 } { 2 } \sum _ { k = n + 1 } ^ { N } a _ { k } z ^ { k } .
$$

The function $G$ is called the analytic part of $F$ , since it can be analytically continued to an analytic function in $| z | \le 1$ . Similarly $G ( z ^ { - 1 } )$ is the coanalytic part of $F ^ { \prime }$ , analytic for $1 \leq | z | \leq \infty$ .

Now we ask the following question: what is the best approximation $\ddot { P }$ to $G$ on the unit circle of the form

$$
\tilde { P } ( z ) = \frac { 1 } { 2 } \sum _ { k = - \infty } ^ { n } b _ { k } z ^ { k } ,
$$

where the series converges for all $z$ with $1 \leq | z | < \infty$ ? In other words, $\ddot { P }$ must be analytic in the exterior of the unit disk apart from a pole of order at most $n$ a t $z = \infty$ . This is the problem that Carath´eodory and Fej´er solved, and the solution is elegant. First of all, $\ddot { P }$ exists, and it is unique. Second, $G - \tilde { P }$ maps the unit circle onto a perfect circle that winds counterclockwise around the origin a number of times: the winding number is at least $n + 1$ . Third, as shown by Schur a few years after Carath´eodory and Fej´er [Schur 1918], $\ddot { P }$ can be constructed explicitly by solving a certain matrix singular value problem. Let $H$ denote the $( N - n ) \times ( N - n )$ real symmetric matrix of Chebyshev coefficients arranged like this,

$$
H = \left( \begin{array} { c c c c c } { a _ { n + 1 } } & { a _ { n + 2 } } & { a _ { n + 3 } } & { \ldots } & { a _ { N } } \\ { a _ { n + 2 } } & { a _ { n + 3 } } & { } & { } & { } \\ { a _ { n + 3 } } & { } & { } & { \ldots } & { } \\ { \vdots } & { } & { } & { } & { } \\ { a _ { N } } & { } & { } & { } & { } \end{array} \right) ,
$$

where the entries in the lower-right triangle are zero. A matrix with this structure, constant along diagonals so that $a _ { i j }$ depends only on $i + j$ , is called a Hankel matrix. Let $\lambda$ be the largest eigenvalue of $H$ in absolute value, let $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { N - n - 1 } ) ^ { T }$ be a corresponding real eigenvector, and define

$$
u ( z ) = u _ { 0 } + u _ { 1 } z + \cdot \cdot \cdot + u _ { N - n - 1 } z ^ { N - n - 1 } .
$$

Here is the theorem due to Carath´eodory and Fej´er and Schur.

Theorem 20.1. Carath´eodory–Fej´er–Schur theorem. The approximation problem described above has a unique solution $\ddot { P }$ , and it is given by the error formula

$$
( G - \tilde { P } ) ( z ) = \lambda z ^ { n + 1 } \frac { u ( z ) } { u ( z ) } .
$$

The function $G - \tilde { P }$ maps the unit circle to a circle of radius $| \lambda |$ and winding number $\geq n + 1$ , and if $| \lambda | > | \mu |$ for all other eigenvalues $\mu$ , the winding number is exactly $n + 1$ .

Proof. The result is due to Carath´eodory and Fej´er [1911] and Schur [1918]. See Theorem 1.1 of [Gutknecht & Trefethen 1982] and Theorem 4 of [Hayashi, Trefethen $\&$ Gutknecht 1990].

Theorem 20.1 is a mathematical assertion about the approximation of a function $G$ on the unit circle by an infinite series. We use this result to construct the polynomial CF approximant as follows. Since $G - \tilde { P }$ maps the unit circle to a circle of winding number $\geq n + 1$ , its real part (times 2)

$$
( G - { \tilde { P } } ) ( z ) + ( G - { \tilde { P } } ) ( z ^ { - 1 } )
$$

maps the unit circle to an equioscillating curve with at least $n + 2$ extreme points. Thus the function

$$
\tilde { p } ( x ) = \tilde { P } ( z ) + \tilde { P } ( z ^ { - 1 } )
$$

yields the equioscillatory behavior that characterizes a best approximation polynomial of degree $n$ to $f ( x )$ on $[ - 1 , 1 ]$ (Theorem 10.1). Unfortunately, $\tilde { p } ( x )$ is not a polynomial of degree $n$ . However, it will generally be very close to one. The function $\ddot { P }$ will normally have Laurent series coefficients $b _ { k }$ that decay as $k \to - \infty$ . We truncate these at degree $- n$ to define

$$
\mathcal { P } _ { _ \mathrm { C F } } ( z ) = \frac { 1 } { 2 } \sum _ { k = - n } ^ { n } b _ { k } z ^ { k } ,
$$

with real part (times 2)

$$
p _ { _ { \mathrm { C F } } } ( x ) = \mathcal { P } _ { _ { \mathrm { C F } } } ( z ) + \mathcal { P } _ { _ { \mathrm { C F } } } ( z ^ { - 1 } ) = \frac { 1 } { 2 } \sum _ { k = - n } ^ { n } ( b _ { k } + b _ { - k } ) z ^ { k } .
$$

If the truncated terms are small, $f - p _ { \mathrm { { C F } } }$ maps $[ - 1 , 1 ]$ to a curve that comes very close to equioscillation with $\geq n + 2$ extrema, and thus $p _ { \mathrm { C F } }$ is close to optimal.

For more details on real polynomial CF approximation, with numerical examples, see [Gutknecht $\&$ Trefethen 1982], [Trefethen 1983], and [Hayashi, Trefethen $\&$ Gutknecht 1990].

Our experiments in the opening pages of this chapter showed that CF approximants can be exceedingly close to best. The truncation described above gives an idea of how this happens. In the simplest case, suppose $f$ is an analytic function on $\lfloor - 1 , 1 \rfloor$ . Then by Theorem 8.1, its Chebyshev coefficients decrease geometrically, and let us suppose that this happens smoothly at a rate $a _ { k } = O ( \rho ^ { k } )$ . Then, roughly speaking, the dominant degree $n + 1$ term of $f$ is of order $\rho ^ { - n - 1 }$ , and the terms $b _ { n } , b _ { n - 1 } , \ldots , b _ { - n }$ are of orders $\rho ^ { - n - 2 } , \rho ^ { - n - 3 } , \cdot \cdot \cdot , \rho ^ { - 3 n - 2 }$ . This suggests that the truncation in going from $\tilde { p }$ to $p _ { \mathrm { C F } }$ will introduce an error of order $\rho ^ { - 3 n - 3 }$ . This is usually a very small number and, in particular, much smaller than the error $\| f - p ^ { * } \|$ of order $\rho ^ { - n - 1 }$ .

In fact, the actual order of accuracy for polynomial CF approximation is one order higher, $\rho ^ { - 3 n - 4 }$ rather than $\rho ^ { - 3 n - 3 }$ . (The reason is that the first truncated term is a multiple of $T _ { 3 n + 3 }$ , the same Chebyshev polynomial that dominates the error $f - p ^ { * }$ itself, and so it is not until the second truncated term, $T _ { 3 n + 4 }$ , that the equioscillation is broken.) On the other hand, to go from this rough argument to a precise theorem is not so easy, because in fact, Chebyshev series need not decay smoothly (Exericse 20.3). Here we quote without proof a theorem from [Gutknecht $\&$ Trefethen 1982].

Theorem 20.2. Accuracy of polynomial CF approximation. For any fixed $m \geq 0$ , let $f$ have a Lipschitz continuous $( 3 m + 3 ) r d$ derivative on $[ - 1 , 1 ]$ with a nonzero $( m + 1 ) s t$ derivative at $x = 0$ , and for each $s \in ( 0 , 1 ]$ , let $p ^ { * }$ and $p _ { { _ { C F } } }$ $b e$ the best and the $\mathit { C F }$ approximations of degree $_ { \mathbf { \nabla } ^ { \prime } \mathbf { \nabla } ^ { \prime } } \psi _ { \mathbf { \nabla } ^ { \prime } }$ to $f ( s x )$ on $[ - 1 , 1 ]$ , respectively. Then as $s \to 0$ ,

$$
\| f - p ^ { * } \| = O ( s ^ { m + 1 } )
$$

and

$$
\| f - p ^ { * } \| \neq O ( s ^ { m + 2 } )
$$

and

$$
\| p _ { { \scriptscriptstyle C F } } - p ^ { * } \| = O ( s ^ { 3 m + 4 } ) .
$$

Proof. See Theorem 3.4 of [Gutknecht $\&$ Trefethen 1982].

We can verify this result numerically. The two plots below display norms for $m = 1$ and $m = 2$ for the function $f ( x ) = e ^ { 5 x }$ .

${ \bf f } { \bf f } = \mathbb { Q } ( { \bf x } ) \exp ( { \sf5 * x } )$ ;   
for $\texttt { m } = \texttt { 1 : 2 }$ $\begin{array} { r } { \sin \mathtt { s s } = \mathtt { \Omega } . 8 . \hat { \mathbf { \Omega } } ^ { } ( 0 : 2 0 ) \mathrm { { ; ~ \ e r r f { p } ~ = ~ [ ] ~ ; ~ \ e r r p p ~ = ~ [ ] ~ ; ~ } } } \end{array}$ for $\mathrm { ~ \mathsf ~ { ~ s ~ } ~ } = \mathrm { ~ \mathsf ~ { ~ s ~ s ~ } ~ }$ $\begin{array} { r l } { \underline { { \mathsf { f } } } } & { { } = } \end{array}$ chebfun(@(x) ff(s\*x)); pbest $=$ minimax(f,m); pcf $=$ cf(f,m); errfp $=$ [errfp norm(f-pbest,inf)]; errpp $=$ [errpp norm(pcf-pbest,inf)]; end loglog(ss,errfp,'.-') hold on, loglog(ss,errpp,'.-r'), loglog(ss,ss.^(m+1),'--'); $\textbf { s } = \ 0 . 0 2 5$ ; loglog(ss,ss.^( $3 * \mathtt { m } + 4 ,$ ,'--r')   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/68087d695ebf3f3fdcfb8ad852a5d9a9b57f103c80be00428449070e4b348699.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/87d97e3db79daad033ecea33113cd8dd5bcd46a194ee686febc205072474fffe.jpg)

In this chapter we have considered CF approximation in its simplest context of approximation of one polynomial $f$ of degree $N$ by another polynomial $p _ { \mathrm { C F } }$ of degree $n$ . In fact, the method is much more general. So long as $f$ has an absolutely convergent Chebyshev series, which is implied, for example, if it is Lipschitz continuous, then Theorem 20.1 still applies [Hayashi, Trefethen $\&$ Gutknecht 1990]. Now $H$ is an infinite matrix which can be shown to represent a compact operator on $\ell ^ { 2 }$ or $\ell ^ { 1 }$ , its dominant eigenvector is an infinite vector, and $u ( z )$ is defined by an infinite series. The error curve is still a continuous function of winding number at least $n + 1$ .

Another generalization is to approximation by rational functions rather than polynomials. Everything goes through in close analogy to what has been written here, and now the other eigenvalues of the Hankel matrix come into play. The theoretical underpinnings of rational CF approximation can be found in papers of Takagi [1924], Adamjan, Arov, and Krein [1971], and Trefethen and Gutknecht [1983b], as well as the article by Hayashi, Trefethen, and Gutknecht cited above. Quite apart from theory, one can compute these approximations readily by the Chebfun cf command using capabilities introduced by Joris Van Deun. For details and examples see [Van Deun & Trefethen 2011].

Further generalizations of CF approximation concern approximation of vector or matrix functions rather than just scalars, and here, such techniques are associated with the name $H _ { \infty }$ approximation. An important early paper was Glover [1984], and there have been many extensions and generalizations since then [Antoulas 2005, Zhou, Doyle $\&$ Glover 1996].

We have emphasized the practical power of CF approximants as providing nearbest approximations at low computational cost. The conceptual and theoretical significance of the technique, however, goes beyond this. Indeed, the eigenvalue/singular value analysis of Carath´eodory–Fej´er approximation seems to be the principal known algebraic window into the detailed analysis of best approximations, and in most cases where best approximations of a function happen to be known exactly, these best approximations are CF approximations in which an approximant like $\tilde { P }$ or $\ddot { p }$ already has the required finite form, so that nothing needs to be truncated to get to $P$ or $p$ [Gutknecht 1983].

Summary of Chapter 20. Carath´eodory–Fej´er approximation constructs near-best approximations of a function $f \in C ( [ - 1 , 1 ] )$ from the singular values and vectors of a Hankel matrix of Chebyshev coefficients. If $f$ is smooth, CF approximants are often indistinguishable in machine precision from true best approximants.

Exercise 20.1. Approximating $\cos ( n x )$ . (a) For $n = \mathrm { 2 } , \mathrm { 4 } , \mathrm { 8 } , \mathrm { 1 6 } , \dots$ , compute the degree $_ { n }$ CF approximant to $f ( x ) = \cos ( n x )$ and plot the error curve. How high can you go in this sequence? (b) What happens if $\cos ( n x )$ is changed to $\cos ( 0 . 9 n x )$ ?

Exercise 20.2. Approximating the jagged function. Four of the figures of this chapter concerned approximations of degree 20 to a jagged function. (a) How do the $L ^ { 2 }$ norms of the best and CF approximations compare? (b) The CF approximation was based on truncation of the Chebyshev series at term $N = 1 0 0$ . How does the $\infty$ -norm of the error vary with $N$ ? (c) Draw a conclusion from this exploration: is the imperfect equioscillation of the error curve in the figure given in the text for this function mostly due to the fact that CF approximation is not best approximation, or to the fact that $N < \infty$ ?

Exercise 20.3. Complex approximation on the unit disk. (a) Suppose $f$ is an analytic function on the closed unit disk and $p$ is a polynomial of degree $_ n$ . Prove that $p$ is a best approximation to $f$ in the $\infty$ -norm on the disk $| z | \le 1$ if and only if it is a best approximation on the circle $| z | = 1$ . (b) Look up Rouch´e’s theorem and write down a careful statement, citing your source. (c) Suppose $f$ is an analytic function in the closed unit disk and $p$ is a polynomial of degree $_ n$ such that $f - p$ maps the unit circle to a circle of winding number at least $n + 1$ . Prove that $p$ is a best approximation to $f$ on the unit disk. (In fact it is unique, though this is not obvious.)

Exercise 20.4. Irregularity of CF approximation. The second figure of this chapter showed quite irregular dependence of $\| p _ { \mathrm { C F } } - p ^ { * } \|$ on the degree $n$ for the function $f ( x ) =$ $\operatorname { t a n h } ( 4 ( x - 0 . 3 ) )$ . In particular, $n = 1 5$ and $n = 1 6$ give very different results. Following the derivation of $p _ { \mathrm { { C F } } }$ in the text, investigate this difference numerically. (a) For $n = 1 5$ , how do the coefficients $\left| b _ { k } \right|$ depend on $k$ , and how big are the truncated terms in going from $\ddot { p }$ to $p _ { \mathrm { C F } }$ ? (b) Answer the same questions for $n = 1 6$ .

# Chapter 21. Spectral Methods

Theorem 8.2 described the geometric convergence of Chebyshev projections and interpolants for an analytic function $f$ defined on $[ - 1 , 1 ]$ . For such a function, it is not just the polynomials that converge geometrically, but also their derivatives. The following theorem makes this precise. An early publication with a result along these lines is [Tadmor 1986].

Theorem 21.1. Geometric convergence of derivatives. Let a function $f$ be analytic in $[ - 1 , 1 ]$ and analytically continuable to the closed Bernstein ellipse $\overline { { E } } _ { \rho }$ for some $\rho > 1$ . Then for each integer $\nu \geq 0$ , the νth derivatives of the Chebyshev projections $f _ { n }$ and interpolants $p _ { n }$ satisfy as $n \to \infty$

$$
\| f ^ { ( \nu ) } - f _ { n } ^ { ( \nu ) } \| = O ( \rho ^ { - n } ) , \quad \| f ^ { ( \nu ) } - p _ { n } ^ { ( \nu ) } \| = O ( \rho ^ { - n } ) .
$$

Proof. Here is an outline, to be filled in in Exercise 21.1. If $f$ is analytic in the closed region $\overline { { E } } _ { \rho }$ , it is also analytic and bounded in the open region $E _ { \tilde { \rho } }$ for some $\bar { \rho } > \rho$ . By Theorem 8.1 it follows that the Chebyshev coefficients satisfy $a _ { k } = O ( \tilde { \rho } ^ { - k } )$ . The bounds (21.1) follow by differentiating the Chebyshev series for $f ^ { ( \nu ) } - f _ { n } ^ { ( \nu ) }$ and $f ^ { ( \nu ) } - p _ { n } ^ { ( \nu ) }$ term by term. The differentiations introduce powers of $n$ , since $T _ { n } ^ { \prime }$ is of size $O ( n ^ { 2 } )$ on $[ - 1 , 1 ]$ , for example, but since $n ^ { \alpha } \tilde { \rho } ^ { - n } = O ( \rho ^ { - n } )$ as $n \to \infty$ for any fixed $\alpha$ , we still get $O ( \rho ^ { - n } )$ convergence for any fixed $\nu$ .

The phenomenon captured in Theorems 8.2 and 21.1 is a general one in complex analysis. When a property holds for an analytic function, there is a good chance that a similar property holds for its derivatives too. The ultimate reason is that both function and derivative can be related to Cauchy integrals, and indeed, an alternative proof of Theorem 21.1 can be based on the Hermite integral formula.

The present chapter is a practical one, devoted to outlining some of the wideranging consequences of Theorem 21.1 for scientific computing: the whole field of spectral methods for the numerical solution of differential equations. Spectral methods are noted for achieving spectral accuracy, which means accuracy that is limited not by the order of the numerical discretization, but only by the smoothness of the function being approximated. This is in contrast to a traditional finite difference or finite element method, which might achieve just $O ( ( \Delta x ) ^ { 2 } )$ or $O ( ( \Delta x ) ^ { 4 } )$ accuracy as $\Delta x  0$ , say, where $\Delta x$ is a grid spacing, even when the function being approximated is $C ^ { \infty }$ or analytic. For a leisurely introduction to spectral methods on Chebyshev grids, see [Trefethen 2000].

We now put aside $\left\{ f _ { n } \right\}$ and focus on spectral collocation methods, based on point values and polynomial interpolants, as opposed to spectral Galerkin methods, based on integrals.

The starting point of spectral collocation methods is the notion of a differentiation matrix. If $p$ is a polynomial of degree $n$ , it is determined by its values on an $( n + 1 )$ -point grid in $[ - 1 , 1 ]$ . The derivative $p ^ { \prime }$ , a polynomial of degree $n - 1$ , is determined by its values on the same grid. The classical spectral differentiation matrix is the $( n + 1 ) \times ( n + 1 )$ matrix that represents the linear map from the vector of values of $p$ on the grid to the vector of values of $p ^ { \prime }$ . (Later we shall mention rectangular alternatives to this classical square matrix formulation.) An explicit formula for this matrix in the case where $\pm 1$ are not among the grid points follows from (5.8) and was first published by Bellman, Kashef, and Casti [1972] (Exercise 21.9):

$$
D _ { i j } = \ell _ { j } ^ { \prime } ( x _ { i } ) = \left\{ \begin{array} { l l } { \displaystyle \frac { \lambda _ { j } } { \lambda _ { i } ( x _ { i } - x _ { j } ) } , } & { i \neq j , } \\ { \displaystyle \frac { x _ { j } } { 1 - x _ { j } ^ { 2 } } , } & { i = j . } \end{array} \right.
$$

The particularly important special case is that of a Chebyshev grid. For exam ple, the function $\sin ( x )$ can be represented to machine precision by a Chebyshev interpolant $p$ on a grid of 14 points:

ans = 14

Suppose we wish to calculate the values of $p ^ { \prime }$ on the same grid. In Chebfun we can write

pp $=$ diff(p); $\tt { x 1 4 } =$ chebpts(14); $\mathtt { p p 1 4 } \ = \ \mathtt { p p } ( \mathtt { x } 1 4 )$   
$\tt p p 1 4 =$ 0.540302305868155 0.564522388819886 0.632936510563863 0.732703188872980 0.842943722651218 0.937783753082982 0.992744245701781 0.992744245701782 0.937783753082982

0.842943722651218   
0.732703188872980   
0.632936510563863   
0.564522388819886   
0.540302305868155

But we can also get our hands on the differentiation matrix explicitly with these commands involving a chebfun object known as a “chebop”:

D = chebop(@(u) diff(u)); D14 = D(14);

If the matrix D14 is multiplied by the vector $\mathtt { p } ( \mathtt { x } 1 4 )$ , the result is the same vector pp14 of sampled derivatives, up to rounding errors:

ans = 3.253654380697663e-14

Above, we put a semicolon after D(14) to avoid printing a $1 4 \times 1 4$ matrix. To give the idea while using up a little less space, here are the $3 \times 3$ and $5 \times 5$ Chebyshev differentiation matrices on $[ - 1 , 1 ]$ :

ans = -1.5000 2.0000 -0.5000 -0.5000 0 0.5000 0.5000 -2.0000 1.5000

# D(5)

ans =

-5.5000 6.8284 -2.0000 1.1716 -0.5000   
-1.7071 0.7071 1.4142 -0.7071 0.2929   
0.5000 -1.4142 0 1.4142 -0.5000   
-0.2929 0.7071 -1.4142 -0.7071 1.7071   
0.5000 -1.1716 2.0000 -6.8284 5.5000

Formulas for the entries of Chebyshev differentiation matrices were first published by Gottlieb, Hussaini, and Orszag [1984], and recurrence relations for computing them fast and stably were given by Welfert [1997], based on earlier work by Fornberg [1988]. Welfert’s paper in turn led to the influential MATLAB Differentiation Matrix Suite by Weideman and Reddy [2000], and another MATLAB code cheb for generating these matrices can be found in [Trefethen 2000].

There is no need to stop at the first derivative. Here is the $5 \times 5$ Chebyshev matrix corresponding to the second derivative on $[ - 1 , 1 ]$ :

D2 $=$ chebop(@(u) diff(u,2)); D2(5)

ans $=$

17.0000 -28.4853 18.0000 -11.5147 5.0000   
9.2426 -14.0000 6.0000 -2.0000 0.7574   
-1.0000 4.0000 -6.0000 4.0000 -1.0000   
0.7574 -2.0000 6.0000 -14.0000 9.2426   
5.0000 -11.5147 18.0000 -28.4853 17.0000

Yes, D2(5) is the square of D(5):

norm(D2(5)-(D(5))^2)

ans = 5.5939e-15

The entries of this matrix can be interpreted as follows. The $j$ th column ( $0 \leq j \leq n$ ) contains the second derivatives of the Lagrange polynomial $\ell _ { j } ( x )$ evaluated at grid points $x _ { 0 } , \ldots , x _ { n }$ . That is, its $( i , j )$ entry (with indexing from 0 to $n$ ) is $\ell _ { j } ^ { \prime \prime } ( x _ { i } )$ . (We have seen Lagrange polynomials in Chapters 5, 9, 11, and 15.) For example, here is the Lagrange polynomial supported at $x _ { 3 }$ :

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/ecddf1bbac8ce66d50410f7c305e97fa5c3a94f8f5f48e184b6c58dd5b7ce342.jpg)

Its second derivatives at the grid points are the values in the fourth column of the matrix $D ( 5 )$ just shown:

ans $=$   
-11.5147   
-2.0000   
4.0000   
-14.0000   
-28.4853

In Chebfun, an object like D or D2 is called a linear chebop (and internally within the Chebfun system, a linop). A linear chebop is not a matrix, but rather a prescription for how to construct matrices of arbitrary order. (A computer science term for the process of filling such prescriptions is lazy evaluation.) If $D$ is applied to an integer argument, the matrix of that dimension is produced:

size(D(33)) ans $=$ 33 33

If $D$ is applied to a chebfun, it has the effect appropriate to the length of that chebfun:

$$
\textbf { f } = \mathbf { \Omega } _ { \mathbf { S } } \mathrm { i n } \left( 7 * \mathbf { x } \right) * \mathbf { e x p } \left( \mathbf { x } \right) * \mathrm { t a n } \left( \mathbf { x } \right) ; \mathbf { \Omega } \mathrm { n o r m } \left( \mathrm { d i f f \left( \mathbf { f } \right) - D * \mathbf { f } \Lambda } \right)
$$

ans = 0

More generally, a chebop can be defined for any differential (or integral) operator. For example, here is the chebop corresponding to the map $L : u \mapsto u ^ { \prime \prime } + u ^ { \prime } + 1 0 0 u$ on $[ - 1 , 1 ]$ :

$$
\mathrm { \small ~ L ~ = ~ c h e b o p ~ ( \mathfrak { Q } ~ ( u ) ~ \ d i f f ~ ( u , 2 ) ~ + ~ d i f f ~ ( u ) ~ + ~ 1 0 0 * u } ) ~ ;
$$

Here is the $5 \times 5$ realization of this operator:

ans $=$

111.5000 -21.6569 16.0000 -10.3431 4.5000   
7.5355 86.7071 7.4142 -2.7071 1.0503   
-0.5000 2.5858 94.0000 5.4142 -1.5000   
0.4645 -1.2929 4.5858 85.2929 10.9497   
5.5000 -12.6863 20.0000 -35.3137 122.5000

We can illustrate its use by applying it to the chebfun for $e ^ { x }$ :

ans $=$ 2.0967e-13

Now we come at last to spectral methods proper. If we just wanted to apply differential operators to functions, we would not need matrices. To solve a differential equation, however, we need to invert the process of applying a differential operator. We want to find a function $u$ satisfying certain boundary conditions such that $\boldsymbol { L u }$ is equal to a prescribed function $f$ . This is where the matrices come in, for matrices can be inverted.

Suppose, for example, we seek a function $u$ that satisfies the equation

$$
u ^ { \prime \prime } + u ^ { \prime } + 1 0 0 u = x , \quad u ( - 1 ) = u ( 1 ) = 0
$$

with $x \in [ - 1 , 1 ]$ . The matrix realization above had no boundary conditions. Now we need to impose them, and a standard way of doing this is to modify one or more initial or final rows of the matrix, one row for each boundary condition (see Chapters 7 and 13 of [Trefethen 2000]). For Dirichlet boundary conditions as in (21.3), we change the first and last rows to correspond to rows of the identity:

L.bc $=$ 'dirichlet'; feval(L,5,'oldschool')

ans =

(We shall explain the clumsy command feval(L,5,'oldschool') in a moment.) Thus, instead of imposing the differential equation at the boundary points $x _ { 0 }$ and $x _ { n }$ , we are imposing boundary conditions at those points. We can now use exactly this matrix to solve the ODE approximately with a $5 \times 5$ spectral discretization. The right-hand side of the matrix problem will be the vector of $x$ sampled at the Chebyshev points—except that the first and last components of the vector will be changed to the appropriate Dirichlet values at $x _ { 0 }$ and $x _ { n }$ , namely zero.

$\mathtt { x 5 } \ =$ chebpts(5); x5([1 end]) = 0; $\mathtt { u 5 } \ =$ feval(L,5,'oldschool') $\mathtt { \backslash x 5 }$ ; plot(chebfun(u5),'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/7760fc9b2bae4c1b1835bd989be3849791033173bf1111d11050c85d26428bc8.jpg)

We have just computed our first solution of a boundary value problem with a spectral method. From the picture it is not evident whether the result is close to correct or not. In fact it is not, as increasing the resolution reveals:

$\tt { x 1 2 } =$ chebpts(12); x12([1 end]) = 0; $\tt { u } 1 2 \ =$ feval(L,12,'oldschool')\x12; plot(chebfun(u12),'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/e0c5dd7f4a2b19f6bb209c73bac98c52b82ad8eecc6970bfeac64bf9fa54361c.jpg)

This curve is beginning to get close to the true solution. How fine a grid do we need to reach approximately machine precision? In Chebfun, the appropriate grid is determined automatically when one solves the problem without specifying dimensions, still with the backslash command:

u = L\x; plot(u,'.-')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/3909a25866b98cfff9c8c5cceabf1359eb5722dfd798d95c6367a2bea7bec921.jpg)

To get this result, Chebfun has solved matrix problems of sizes 17, 33, and 65, at which point its convergence criteria were satisfied. The final length is

length(u)

and we can verify that the accuracy is good:

norm(L\*u-x)

ans = 1.1362e-12

This brings us to the clumsy expression feval(L,5,'oldschool') in the demonstration above. This notation instructs Chebfun to display a spectral differentiation matrix corresponding to boundary conditions imposed in the classical way that we have just described, in which certain rows of a square differentiation matrix are replaced by rows corresponding to boundary conditions [Trefethen 2000]. This method of applying boundary conditions relies on the assumption that for each boundary condition, there is a clear choice of which row of the ODE discretization matrix it should replace. In fact, this ceases to be clear in various situations involving systems of equations or more complicated boundary conditions, as well as more general side conditions such as $\textstyle \int u ( x ) d x = 0$ . Around 2010, Driscoll and Hale realized that more robust and flexible discretizations could be obtained by switching to a different approach based on rectangular differentiation matrices. For an order $d$ differential operator to be applied on an $( n + 1 )$ -point grid, the Driscoll–Hale discretization begins with a matrix of dimension $( n + 1 - d ) \times ( n + 1 )$ corresponding to a map from data on an $( n + 1 )$ -grid to data on an $( n + 1 - d )$ -grid, and then appends an additional $d$ rows for boundary conditions. No collocation equation gets replaced in this process. This is now the discretization strategy used routinely by Chebfun, and it is what Chebfun actually did in solving the problem $\texttt { u } = \texttt { L } \backslash \texttt { x }$ above. To see the matrices, one can type the more natural expression L(5) instead of feval(L,5,'oldschool'). We shall not go into details here; see [Driscoll & Hale 2015] and [Aurentz & Trefethen 2017a].

Homogeneous Dirichlet conditions at both ends are only the simplest of many possible boundary conditions for a boundary value problem. To solve (21.3) again except with Neumann conditions $u ^ { \prime } ( - 1 ) = u ^ { \prime } ( 1 ) = 0$ , the first and last rows of the discretization matrix would classically get replaced by the corresponding rows of the first derivative matrix:

L.bc $=$ 'neumann'; feval(L,5,'oldschool')

ans =   
-5.5000 6.8284 -2.0000 1.1716 -0.5000   
7.5355 86.7071 7.4142 -2.7071 1.0503   
-0.5000 2.5858 94.0000 5.4142 -1.5000   
0.4645 -1.2929 4.5858 85.2929 10.9497   
0.5000 -1.1716 2.0000 -6.8284 5.5000

Here is the Chebfun solution, again based on the Driscoll–Hale discretization, now plotted without dots:

$\texttt { u } = \texttt { L } \backslash \texttt { x }$ ; plot(u)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/7128fd6ac5add7d725356a87dd567f4c6bdbe9f3ed4c681ddf772a409d20be94.jpg)

Spectral methods can also solve problems with variable coefficients. For example, suppose we wish to solve the Airy equation boundary value problem

$$
u ^ { \prime \prime } - x u = 0 , \quad u ( - 3 0 ) = 1 , \ u ( 3 0 ) = 0
$$

for $x \in [ - 3 0 , 3 0 ]$ . Here is the solution:

L = chebop(@(x,u) diff $( \mathtt { u } , 2 ) \mathtt { - x } . \mathtt { * u }$ ,[-30,30]); L.lbc $\ c = ~ 1$ ; $\mathtt { L . r b c } = \mathtt { 0 }$ ; $\tt { u } = \tt { L } \backslash 0$ ; plot(u)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/fda62db12db0af10cd530c95478748b328a95c24c12c1d2756c92bc73a30cbbc.jpg)

For nonlinear problems, one would normally use a Newton iteration or some variant. Chebfun handles these cases too. For example, the equation

$$
\theta ^ { \prime \prime } + \mathrm { s i n } ( \theta ) = 0 , \quad \theta \in [ 0 , 6 ] ,
$$

describes the motion in time of a nonlinear pendulum situated at height $h ( t ) =$ $- \cos ( \theta ( t ) ) \in [ - 1 , 1 ]$ . If we prescribe boundary conditions

$$
u ( 0 ) = - \pi / 2 , \quad u ( 6 ) = \pi / 2 ,
$$

we can solve the system numerically with Chebfun as follows. Notice that the solution is still invoked by the backslash command, though we are very far now from the original MATLAB notion of backslash for solving a square system of linear equations.

N = chebop(0,6); N.op $=$ @(theta) diff(theta,2) $^ +$ sin(theta); N.lbc $=$ -pi/2; N.rbc $=$ pi/2; theta $=$ N\0; plot(-cos(theta))

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/51dd67a0f7e1b309c5c389dbbccca972d46ebad59c4ab4577d10135d5319940c.jpg)

This solution corresponds to the pendulum first going up above height 0 for a time, and then swinging over to the other side, where it again goes above height 0 before falling back down again. On the other hand, suppose we change the right-hand boundary condition to $5 \pi / 2$ . Then another solution appears, corresponding to the pendulum swinging once around the top:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/77be7365c74c98dbe70a824f4e9a6ab97f0e8efa369498d55ee92dd2e920f079.jpg)

These two solutions do not exhaust the full set of possibilities for this nonlinear problem; see Exercise 21.7.

To compute solutions of nonlinear differential equations, Chebfun uses variants of Newton’s method implemented for continuous functions rather than discrete vectors. Where one might expect to encounter Jacobian matrices in the solution process, Chebfun actually utilizes their continuous analogues known as Fr´echet derivative operators, which are constructed by a process of automatic differentiation, again exploiting lazy evaluation. These capabilities are due to Birkisson and

Driscoll [2012]. Chebfun can also solve systems of equations, eigenvalue problems, and problems specified by coefficients that are just piecewise smooth.

This is a book about approximation theory, not differential equations, and we began this chapter with an approximation result, a theorem about the $O ( \rho ^ { - n } )$ accuracy of derivatives of approximations of analytic functions. It would be excellent if this theorem implied that spectral methods converge to analytic solutions at the rate $O ( \rho ^ { - n } )$ , but it does not. Theorem 21.1 ensures that if $u$ is an analytic solution to a boundary value problem $L u = f$ , then the Chebyshev interpolants to $\boldsymbol { L u }$ would converge geometrically to $f$ as $n  \infty$ . In spectral computations, however, we do not have the exact solution available to discretize but must approximate it by solving matrix problems. One can hope that the approximations will converge at the expected rate, and indeed they do so under many circumstances, but proving this requires further arguments, which we shall not attempt to discuss here. As a rule, in this business, the practice is ahead of the theory.

Some of the ideas behind spectral methods are as old as Fourier and Chebyshev expansions, and many people contributed in the early years of computers, including Lanczos, Elliott, Fox, and Clenshaw. But it was their application to the PDEs of fluid mechanics by Orszag and Gottlieb and others beginning around 1970 that made these methods famous, and it was Orszag who coined the term “spectral methods” [Orszag 1971a & 1971b]. Spectral methods divide into Fourier methods, for periodic problems, and Chebyshev and related methods, for nonperiodic problems. As always in this book, we have emphasized the nonperiodic case, which is less obvious, even though at bottom it is essentially the same. In applications, Fourier and Chebyshev discretizations are often found mixed together. For example, a three-dimensional cylindrical geometry may be discretized by a Chebyshev grid for the radial variable, a periodic Fourier grid for the circumferential variable, and another periodic grid serving as an approximation to an ideal infinite Fourier grid for the longitudinal variable. When the grids are fine, implementations are often based on the FFT rather than matrices.

For details of the spectral methods incorporated in Chebfun, see [Driscoll, Bornemann & Trefethen 2008] and [Driscoll & Hale 2015] for the linear case and [Birkisson & Driscoll 2012] for nonlinear aspects; more recent material can be found in [Aurentz & Trefethen 2017a] and Appendix A of [Trefethen, Birkisson & Driscoll 2018]. For information about spectral methods in general, see texts such as [Fornberg 1996], [Trefethen 2000], [Boyd 2001], [Canuto et al. 2006], [Hesthaven, Gottlieb & Gottlieb 2007], and [Shen, Tang & Wang 2011].

This chapter began by noting that if a function is smooth, the derivatives of its interpolants converge rapidly. A contrapositive of this observation is the phenomenon that if the discrete approximations to derivatives of a function blow up as the mesh is refined, it is not smooth. Chebfun exploits this principle as the basis of its edge detection algorithm for breaking piecewise smooth functions into subintervals, which was illustrated at the end of Chapter 9. This algorithm was developed by Rodrigo Platte and is described in [Pach´on, Platte & Trefethen 2010].

Summary of Chapter 21. Spectral collocation methods are numerical algorithms for solving differential equations based on polynomial or trigonometric interpolants. For problems whose solutions are analytic, they typically converge geometrically as the grid is refined.

Exercise 21.1. Proof of Theorem 21.1. Write down a careful proof of Theorem 21.1 as a corollary of Theorems 3.1 and 8.1. Be sure to state precisely what properties of the Chebyshev polynomials $\{ T _ { k } \}$ your proof depends on.

Exercise 21.2. Extension of Theorem 21.1. Theorem 21.1 quantifies the accuracy of the derivatives of Chebyshev interpolants based on an assumption of analyticity in a Bernstein ellipse. State and prove a different theorem about the convergence of the derivatives for any sequence of polynomials $p _ { n } \in \mathcal { P } _ { n }$ for which the errors satisfy $\| f - p _ { n } \| =$ $O ( \rho ^ { - n } )$ for some $\rho > 1$ .

Exercise 21.3. Differentiation matrices. (a) The text displayed the $3 \times 3$ matrix $D ( 3 )$ . Derive the entries of this matrix analytically. (b) Also displayed was the $5 \times 5$ matrix $D 2 ( 5 )$ . Derive the entries of the middle column of this matrix analytically.

Exercise 21.4. Linear boundary value problems. Solve the following linear ODE boundary value problems numerically with Chebfun. In each case plot the solution and report the value of $u$ at the midpoint of the interval and the length of the chebfun repre senting $_ u$ .

(a) $0 . 0 0 1 u ^ { \prime \prime } + x u ^ { \prime } - u = \exp ( - 1 0 x ^ { 2 } )$ , $x \in [ - 1 , 1 ]$ , $u ( - 1 ) = 2$ , $u ( 1 ) = 1$ .   
(b) $0 . 0 0 1 u ^ { \prime \prime } + ( 1 - x ^ { 2 } ) u = 1$ , $x \in [ - 5 , 5 ]$ , $u ( - 5 ) = 0$ , $u ( 5 ) = 0$ .   
(c) $0 . 0 0 1 u ^ { \prime \prime } + \sin ( x ) u = 1 ,$ $x \in [ - 1 0 , 1 0 ]$ , $u ( - 1 0 ) = 0$ , $u ^ { \prime } ( 1 0 ) = 0$ .

Exercise 21.5. Nonlinear boundary value problems. Find a solution numericall to each of the following nonlinear ODE boundary value problems. In each case plot th solution and report the value of $u$ at the midpoint of the interval.

(a) $0 . 0 5 u ^ { \prime \prime } + ( u ^ { \prime } ) ^ { 2 } - u = 1$ , $x \in [ 0 , 1 ]$ , $u ( 0 ) = 2$ , $u ( 1 ) = 1$ . (b) $0 . 0 1 u ^ { \prime \prime } - u u ^ { \prime } - u = 0$ , $x \in [ - 1 , 1 ]$ , $u ( - 1 ) = 1$ , $u ( 1 ) = 2$

Exercise 21.6. Convergence with $\mathbf { \nabla } ^ { \prime } \mathbf { \pmb { \nu } } ^ { \prime }$ . The text solved the boundary value problem $u ^ { \prime \prime } + u ^ { \prime } + 1 0 0 u = x$ on $[ - 1 , 1 ]$ with boundary conditions $u ( - 1 ) = u ( 1 ) = 0$ for grid parameters $n + 1 = 5$ , 12, and 35. Perform a numerical study of the $\infty$ -norm error of the solution as a function of $_ n$ , and comment on the results.

Exercise 21.7. Nonunique solutions. (a) For each of the two nonlinear pendulum problems solved at the end of the chapter, determine exactly how many solutions there must be. (You can use physical reasoning, or phase plane analysis.) (b) Find them all numerically with Chebfun by using sufficiently close initial guesses specified by a command of the form $\mathbb { N } . \mathrm { i n i t } \ = \ \mathbf { \ " } \mathbf { f } \left( \mathrm { t h e t a } \right)$ to start the iteration. Report the maximum heights $- \cos ( \theta )$ of the pendulum in all cases and the time(s) at which these heights are reached.

Exercise 21.8. Painlev´e equation. Solutions to the second Painlev´e equation, $u ^ { \prime \prime } = 2 u ^ { 3 } + x u$ , typically blow up at various locations on the $_ x$ -axis. There exist special solutions, however, that are smooth for all real $_ x$ . Characterized by the asymptotic boundary conditions $u \sim \pm \sqrt { - x / 2 }$ as $x  - \infty$ and $u  0$ as $x \to + \infty$ , these are the so-called Hastings–McLeod solutions. Truncate the problem to the interval $[ - L , L ]$ with boundary conditions $u ( - L ) = \sqrt { L / 2 }$ , $u ( L ) = 0$ and compute and plot solutions for $L = 1 , 2 , 4 , 8 , 1 6$ . Produce a table of $u ( 0 )$ and $u ^ { \prime } ( 0 )$ for each value of $L$ . To 10 digits, what do you think are the values of $u ( 0 )$ and $u ^ { \prime } ( 0 )$ in the limit $L \to \infty$ ?

Exercise 21.9. Formula for square differentiation matrix. Derive (21.2) from (5.8).

Exercise 21.10. Eigenvalues of differentiation matrices. Let $D _ { 1 }$ and $D _ { 2 }$ be the $2 0 \times 2 0$ matrices corresponding to spectral discretization of the second derivative operator on $[ - 1 , 1 ]$ with Dirichlet boundary conditions of the Driscoll–Hale and “old school” types, respectively. Are the eigenvalues real or complex? What are the condition numbers? How do the condition numbers grow with the dimension? (This is an important matter for accuracy of spectral methods.)

# Chapter 22. Linear Approximation: Beyond Polynomials

Several times in the previous chapters, we have hinted that polynomials are not optimal functions for linear approximation on $[ - 1 , 1 ]$ . (Nonlinear approximations are another matter and will make their appearance in the next chapter.) It is now time to explain these hints and introduce alternative approximations that may be up to $\pi / 2$ times more efficient. One reason the alternatives are valuable is that they have practical advantages in some applications, especially for spectral methods in more than one space dimension. An equally important reason is that they push us to think more deeply about what it means to approximate a function and what may or may not be special about polynomials. The ideas of this chapter originate in [Bakhvalov 1967] and [Hale & Trefethen 2008]. Related ideas are the basis of work on sinc function numerical methods [Stenger 1993 & 2010, Richardson & Trefethen 2011], tanh and double exponential or tanh-sinh quadrature [Sag $\&$ Szekeres 1964, Takahasi & Mori 1974, Mori & Sugihara 2001], and the transformed-grid spectral methods introduced by Kosloff and Tal-Ezer [1993].

Recall from Chapter 8 that if $f$ is analytic on $[ - 1 , 1 ]$ , then to investigate its polynomial approximations, we ask how large a Bernstein ellipse $E _ { \rho }$ it can be analytically continued to. Here, for example, is the ellipse $E _ { \rho }$ with $\rho = 1 . 1 5$ . The words “Bernstein ellipse” written inside will help in a moment to visualize a conformal map. (Mathematically, these words are a piecewise linear complex function of a real variable constructed by the Chebfun scribble command.)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/bc5a67f9aa3e39cc7f814658724b47882a7a98247079adb5358b03bca5467d2b.jpg)

Bernstein ellipses are unavoidable if one works with polynomial interpolants, but from the user’s point of view, they have an unfortunate property: they are thicker in the middle than near the ends! For a function $f$ to be analytic in the region just shown, its Taylor series about a point $x \approx 0$ must have a radius of convergence 0.14 or more. For $x \approx \pm 1$ , on the other hand, a radius of convergence of 0.01 is sufficient. Thus the smoothness requirement on $f$ is highly nonuniform, and this is not an artifact of the analysis. Polynomials of a given degree really can resolve rougher behavior of a function $f$ near the endpoints than in the middle. This phenomenon turns up in one form of another whenever approximation theorists seek sharp results about polynomial approximations, whether $f$ is analytic or not. See, for example, [Timan 1951], [Lorentz 1986], [Ditzian $\&$ Totik 1987], and Chapter 8 of [DeVore and Lorentz 1993].

Of course, there are some functions that have most of their complexity near $\pm 1$ , and for these, the nonuniform approximation power of polynomials may be an advantage. For example, functions of this kind arise in fluid mechanics problems with boundary layers. More often, however, the nonuniform approximation power of polynomials is a disadvantage from a practical point of view, as well as being a conceptual complication. If only those ellipses had constant width for all $x \in [ - 1 , 1 ] !$

As soon as one frames the difficulty in this way, a possibility for a solution suggests itself. The idea is to change variables by means of a function that conformally maps ellipses, approximately at least, to straight-sided $\varepsilon$ -neighborhoods of $\lfloor - 1 , 1 \rfloor$ , while mapping $[ - 1 , 1 ]$ to itself. To explore this idea we shall use the variable $x$ for the domain where $f$ is defined and introduce a new variable $s$ for the parameter domain, where the Chebyshev points and ellipses live. Our conformal map will be $x = g ( s )$ , and we shall approximate a function $f ( x )$ on $[ - 1 , 1 ]$ by $p ( g ^ { - 1 } ( x ) ) = p ( s )$ , where $p$ is a polynomial. Equivalently, we shall approximate $f ( g ( s ) )$ on $[ - 1 , 1 ]$ by a polynomial. In the remainder of this chapter we explore the consequences of this idea, considering just one fixed example of a map $g$ ,

$$
g ( s ) = { \frac { 1 } { 5 3 0 8 9 } } ( 4 0 3 2 0 s + 6 7 2 0 s ^ { 3 } + 3 0 2 4 s ^ { 5 } + 1 8 0 0 s ^ { 7 } + 1 2 2 5 s ^ { 9 } ) ,
$$

or as a Chebfun command,

$$
\begin{array} { r }  \begin{array} { l } { \mathrm { g ~ = ~ c h e b f u n } { \left( \mathfrak { Q } \left( \mathbf { s } \right) \begin{array} { l l } { ( 4 0 3 2 0 \ast \mathbf { s } + 6 7 2 0 \ast \mathbf { s } \widehat { \textbf { \small s } } + 3 0 2 4 \ast \mathbf { s } \widehat { \textbf { \small s } } + \mathbf { \small ~ \cdot } \widehat { \textbf { \small { \xi } } } \cdot \mathbf { \xi } \cdot \mathbf { \xi } \cdot \mathbf { \xi } ) } \end{array} \right. } \\ { \quad \left. \begin{array} { l } { 1 8 0 0 \ast \mathbf { s } \widehat { \textbf { \small s } } ^ { - } 7 \ + \ 1 2 2 5 \ast \mathbf { s } \widehat { \textbf { \small s } } ^ { } 9 ) / 5 3 0 8 9 } \end{array} \right) ; } \end{array} } \end{array}
$$

This function $g$ is derived by truncating the Taylor series of $( 2 / \pi ) \sin ^ { - 1 } ( x )$ and then rescaling the result so that $g ( \pm 1 ) = \pm 1$ . See [Hale & Trefethen 2008] for a discussion of this and other possible choices of $g$ , some of which (notably a conformal map onto an infinite strip) come closer to realizing the maximum possible improvement by a factor of $\pi / 2$ . See also Exercises 22.2 and 22.3.

To begin the discussion, let us look at how $g$ transforms ellipses about $[ - 1 , 1 ]$ . Here is a plot of $g ( E _ { 1 . 1 5 } )$ , the transformed version of the ellipse shown earlier. Notice the much straighter sides.

plot(g(z(1.15)),'m'), hold on, plot(g(f),'k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/3f5788a0d11dfe8aa24b7abdd438d78d7743c54f2e36502da7e05663aa506fc8.jpg)

Following [Hale & Trefethen 2008], we call $g$ a sausage map and $g ( E _ { 1 . 1 5 } )$ a sausage region. The crucial property is that for most of its length, the sausage is narrower than the ellipse, as the distorted “Bernstein ellipse” label makes clear. The ellipse has half-width approximately $\rho - 1$ , which is about $3 2 \%$ more than the half-width $0 . 7 6 ( \rho - 1 )$ of the sausage:

ellipse_width $=$ max(imag(z(1.15))) sausage_width $=$ max(imag(g(z(1.15)))) ratio $=$ ellipse_width/sausage_width ellipse_width = 0.1402 sausage_width $= ~ 0 . 1 0 6 1$ ratio $=$ 1.3210

We can learn more by looking at a family of ellipses. Following Chapter 8, here is a plot of $E _ { \rho }$ for $\rho = 1 , 1 . 2 , . . . , 2 . 2$ :

$\mathtt { w } = \mathtt { e x p } ( 2 \mathtt { i } \ast \mathtt { p i } \ast \mathtt { x } )$ ; for rho $=$ 1.1:0.2:2.2, plot( $( \mathtt { r h o } * _ { \mathsf { W } } + ( \mathtt { r h o } * _ { \mathsf { W } } ) \hat { \mathbf { \xi } } ( - 1 ) ) / 2 )$ , hold on, end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/e1cc3591d2061a32ed6003802c81f39d5c3810e6b7d48c452cb83c744bc29253.jpg)

Here is the corresponding figure for the images $g ( E _ { \rho } )$ :

for rho $= \ 1 . 1 : 0 . 2 : 2 . 2$ plot $( { \ g ( { ( { { \bf { \bar { \Phi } } } { { ( { { \bf { \bar { \Phi } } } { { \bf { \bar { \Phi } } } { { ( { { \bf { \bar { \Phi } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } } ) } } } + { ( { { { \bf { \bar { \Phi } } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } ) } \hat { \bf { \Lambda } } } } ) } \cdot \mathrm { { \Lambda } } } ) } + ( { { \bf { \bar { \Phi } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } { { \bf { \Lambda } } } } ) \cdot \mathrm { { \Lambda } }  )$ , hold on   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/70cb75854628d4586637894b834e8e541309db27a659f401d7dad8644d9e2bab.jpg)

It is clear that near $[ - 1 , 1 ]$ , the transformed ellipses are narrower and more uniform in shape than the ellipses, but further away, their behavior is more irregular. We shall see some of the implications of these shapes as we explore the uses of this map.

Chapter 2 considered polynomial interpolants in Chebyshev points $\left\{ s _ { k } \right\}$ . With the transformation $g$ , $f$ is interpolated by transformed polynomials $p ( g ^ { - 1 } ( x ) )$ in the points $\{ g ( s _ { k } ) \}$ . We illustrate the difference between Chebyshev and transformed Chebyshev points by adapting a code segment from Chapter 17. The squares show the transformed points.

ss $=$ chebpts(10); plot(ss,.9,'.b'), hold on, plot(g(ss),.8,'sm') ss $=$ chebpts(20); plot(ss,.5,'.b'), plot(g(ss),.4,'sm') ss $=$ chebpts(50); plot(ss,.12,'.b'), plot(g(ss),0,'sm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/6189e1c158c916011fb303df42912e4cb1a9182a823869043c26f7e997bc8a1c.jpg)

Note that the squares are more evenly distributed than the dots, and in particular, they are denser in the middle, providing finer resolution.

Chapter 3 considered Chebyshev polynomials and series. We adapt another code segment from Chapter 17 to illustrate how a Chebyshev polynomial $T _ { n } ( x )$ compares to the corresponding transformed polynomial $T _ { n } ( g ^ { - 1 } ( x ) )$ . For this we need the inverse map $g ^ { - 1 }$ .

$\tt { g i } = \tt { i n v } ( \tt { g } )$ ; $\mathrm { T 5 0 ~ = }$ chebpoly(50); subplot(2,1,1), plot(T50), plot(T50(gi),'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/092327442afbae877400180cee5b60fe4a6be53b3d8330b4fa60397ff6f8ac7d.jpg)

Notice that the lower curves are more like uniform sine waves than the upper ones.

Theorem 3.1 summarized some basic facts about Chebyshev series, and these carry over immediately to a theorem for transformed Chebyshev series. The theorem as stated assumes $g$ is analytic, though in fact, continuous differentiability would be enough.

Theorem 22.1. Transformed Chebyshev series. Let $g$ be an analytic function on $[ - 1 , 1 ]$ mapping $[ - 1 , 1 ]$ to itself with $g ^ { \prime } ( s ) > 0$ . Then if $f$ is Lipschitz continuous on $[ - 1 , 1 ]$ , it has a unique representation as an absolutely convergent series

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } T _ { k } { \bigl ( } g ^ { - 1 } ( x ) { \bigr ) } ,
$$

and the coefficients are given for $k \geq 1$ by the formula

$$
a _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \frac { f ( g ( s ) ) T _ { k } ( s ) } { \sqrt { 1 - s ^ { 2 } } } d s
$$

and for $k = 0$ by the same formula with the factor $2 / \pi$ changed to $1 / \pi$

Proof. This is a consequence of Theorem 3.1.

For many functions $f$ , the transformed series are $2 0 - 3 0 \%$ more efficient than the originals. For example, Chebyshev interpolation of $( 2 + \cos ( 2 0 x + 1 ) ) ^ { - 1 }$ requires about 520 terms for 15-digit accuracy:

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/3ee084befebde40f7769f1c49fbec04e681c07b84f3dd47adcbe9f25b88c3522.jpg)

For the transformed interpolants the number is closer to 400:

plotcoeffs(f(g),'m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/5990e9478385f1faccb15819b7e9b302f53d5ac8e689fd5c34b060a28adc0027.jpg)

Chapter 7 considered convergence for differentiable functions. Theorem 7.2 can readily be restated for the transformed context—see Exercise 22.1. For a numerical illustration, here is a repetition of the experiment from Chapter 7 involving $f ( x ) =$ $| x |$ . On the loglog scale, the transformed approximants run parallel to the same line as the Chebyshev interpolants, but lower.

$\begin{array} { r l } & { \mathrm { \bf ~ f ~ = ~ \ a b s ( x ) : ~ \ f g ~ = ~ \bf ~ f \left( g \right) : ~ \omega ~ } } \\ & { \mathrm { \bf ~ n n ~ = ~ \omega ~ 2 * r o u n d \left( 2 . \hat { \omega } ( 0 : \cdot 3 : 7 ) \right) - 1 ; ~ { \vec { \varphi } } ~ e ~ = ~ \omega ~ 0 * n n ; ~ { \vec { \varphi } } ~ e \in ~ \omega _ 0 \ * n n ; } } \\ & { \mathrm { \bf ~ f o r ~ \bf ~ j ~ = ~ \bf ~ 1 : 1 \cdot } \mathrm { \bf ~ e n g t h } \mathrm { \bf ~ ( n n ) } } \\ & { \mathrm { \bf ~ n ~ = ~ \omega ~ n n ( j ) : ~ \omega _ \mathrm { { f } ~ n ~ = ~ \ c h e b f u n ( f , n + 1 ) ; ~ \vec { \varphi } e e ( j ) ~ = ~ \ n o r m ( f - f n , i n f ) ~ ; } } } \\ & { \mathrm { \bf ~ f n 2 ~ = ~ \ c h e b f u n ( f g , n + 1 ) ; ~ \vec { \varphi } e e 2 ( j ) ~ = ~ \ n o r m ( f g - f n 2 , i n f ) ~ ; } } \end{array}$   
end   
$\log 1 0 \mathbf { g } \left( \mathtt { n n } , 1 . / \mathtt { n n } , ^ { \prime } \mathtt { r } ^ { \prime } \right)$   
hold on, loglog(nn,ee,'.'), loglog(nn,ee2,'sm')   
ratio $=$ ee(end-4:end)./ee2(end-4:end)

ratio $=$

1.3167 1.3167 1.3167 1.3167 1.3167

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/f7077a8ad74b49d1e12289efd32e01b45e17d95f749d1ed792a1e2fc23225126.jpg)

Chapter 8 considered convergence for analytic functions. Here is the transformed equivalent of Theorems 8.1 and 8.2.

Theorem 22.2. Transformed coefficients of analytic functions. For given $\rho > 1$ , let $_ { g }$ and $f$ be analytic functions on $[ - 1 , 1 ]$ that can be analytically continued to $E _ { \rho }$ and $g ( E _ { \rho } )$ , respectively, with $| f ( z ) | \leq M$ for $z \in g ( E _ { \rho } )$ . Then the transformed Chebyshev coefficients of Theorem 22.1 satisfy

$$
| a _ { k } | \leq 2 M \rho ^ { - n } ,
$$

the truncated transformed series satisfy

$$
\| f - f _ { n } ( g ^ { - 1 } ( x ) ) \| \leq \frac { 2 M \rho ^ { - n } } { \rho - 1 } ,
$$

and the transformed Chebyshev interpolants satisfy

$$
\| f - p _ { n } ( g ^ { - 1 } ( x ) ) \| \leq { \frac { 4 M \rho ^ { - n } } { \rho - 1 } } .
$$

Proof. These results follow from Theorems 8.2 and 22.1.

Here is a repetition of the Chapter 8 experiment for the Runge function, now with squares to show the transformed approximants.

$\begin{array} { r l } & { \mathrm { \bf ~ f ~ = ~ \bf ~ 1 / \left( 1 + 2 5 * x \mathrm { \bf ~ \dot { \bf ~ \underline { ~ } { ~ 2 ~ } } } \right) ; ~ \bf ~ f ~ g ~ = ~ \bf ~ f ~ ( g ) ~ } ; } \\ & { \mathrm { \bf ~ n n ~ = ~ \bf ~ 0 : 1 0 : 2 0 0 ; ~ { \bf ~ e ~ e ~ = ~ \bf ~ 0 * n n } ; ~ { \bf ~ e } e 2 ~ = ~ \bf ~ 0 * n n } ; } \\ & { \mathrm { \bf ~ f o r ~ \bf ~ j ~ = ~ \bf ~ 1 : 1 \mathrm { e n g t h } ( n n ) } } \\ & { \mathrm { \bf ~ n ~ = ~ \bf ~ n n ( j ) ; ~ \bf ~ f ~ n ~ = ~ \mathrm { c h e b f u n } ( f , n + 1 ) ; ~ { \bf ~ e } e ( j ) ~ = ~ \mathrm { n o r m } ( f - f n , i n f ) ~ } ; } \\ & { \mathrm { \bf ~ f n 2 ~ = ~ \mathrm { c h e b f u n } ( f g , n + 1 ) ; ~ { \bf ~ e } e 2 ( j ) ~ = ~ \mathrm { n o r m } ( f g - f n 2 , i n f ) ~ } ; } \end{array}$ end semilogy(nn,ee,'.'), hold on, semilogy(nn,ee2,'sm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/b74d126d2d240c6898ae1da52ce8737fe13528ace924ee8cb2a3c92a885336b7.jpg)

The speedup is clear. On the other hand, here is a repetition of the experiment with $\cos ( 2 0 x )$ .

f f $\begin{array} { l } { { \mathrm { \tiny ~ ( ~ \cos ~ ( 2 0 * x ) ~ ; ~ f g ~ = ~ f ~ ( g ) ~ ; ~ ~ n n ~ = ~ 0 : 2 : 6 0 ; ~ \ e e ~ = ~ 0 * n n ; ~ \ e e 2 ~ = ~ 0 : n n ; } } } \\ { { \mathrm { \tiny ~ ( ~ \partial ~ 1 : 1 \mathrm { { z } \it ~ { h } } ( n n ) ~ \partial ~ 1 ~ \partial ~ 2 ~ ) ~ } } } \\ { { \mathrm { \tiny ~ { n } ~ = ~ n n ( j ) ~ ; ~ f n ~ = ~ c h e b f u n ( f , n + 1 ) ~ ; ~ \ e e ( j ) ~ = ~ n o r m ( f - f n , i n f ) ~ ; } } } \\ { { \mathrm { \tiny ~ { f n 2 ~ = ~ c h e b f u n ( f g , n + 1 ) ~ ; ~ \ e e 2 ( j ) ~ = ~ n o r m ( f g - f n 2 , i n f ) ~ ; } } } } \end{array}$ end semilogy(nn,ee,'.'), hold on, semilogy(nn,ee2,'sm')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/c5dde1ffdbd77482370e51a11163b26ba7a691d7e79e628ad60cc3913aa8b2c7.jpg)

Now the result is ambiguous: the transformed method starts out ahead, but the standard Chebyshev method wins eventually. The explanation can be found in the nested ellipses $E _ { \rho }$ and their images plotted earlier. The function cos(20 $x$ ) is entire, and for larger $n$ , the Chebyshev points take good advantage of its analyticity well away from $[ - 1 , 1 ]$ . The transformed points do not do as well. (The advantage of the transformation becomes decisive again if we change $\cos ( 2 0 x )$ to $\cos ( 1 0 0 x )$ .)

We can see similar effects if we look at best approximations. For a nonsmooth function like $| x |$ , transformed polynomials typically approximate better than true ones. The following figures should be compared with those of Chapter 10, and the variable ratio quantifies the degree of improvement.

$\begin{array} { r l } { \mathbf { f } } & { { } = } \end{array}$ abs(x); subplot(1,2,1), plot(f,'k')   
$\mathbf { f } \mathbf { g } \ = \ \mathbf { f } \left( \mathbf { g } \right)$ ; [p,err] $=$ minimax(fg,4);   
hold on, plot(p(gi),'m') subplot(1,2,2), hold off   
1 $\mathrm { \Omega ) 1 0 t ( g , f { \mathrm { - p } } ( g i ) , \mathrm { ' m } ^ { \prime } ) }$ , hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p2,err2] $=$ minimax(f,4); ratio $=$ err2/err

ratio $=$ 1.2847

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/1845e770388d2f91a6a63afd7d8a12eed41d56d5314988e5b12e59132018b3df.jpg)

On the other hand, for a gentle entire function like $\exp ( x )$ , pure polynomials converge very fast and transformed polynomials cannot compete. The following error curve is seven orders of magnitude larger than that of Chapter 10.

f = exp(x); $\mathbf { f } \mathbf { g } \ = \ \mathbf { f } \left( \mathbf { g } \right)$ ;   
[p,err] $=$ minimax(fg,10); plot(g,fg-p,'m'), hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p2,err2] $=$ minimax(f,10); ratio $=$ err2/err

ratio $=$ 2.9938e-07

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/9f0452bccff8c3ccc9940ad1366c0f614976292b5867844611b0c023be87b487.jpg)

Our final application of transformed polynomial approximants is the one that was the subject of [Hale & Trefethen 2008]: quadrature. As described in Chapter 19, standard quadrature formulas are based on the idea of integrating a function numerically by interpolating it by a polynomial and then integrating the interpolant. This is the basis of all the well-known quadrature formulas, including Gauss, Newton– Cotes, Simpson, and Clenshaw–Curtis. But why should quadrature formulas be based on polynomials? This is a question not often raised in the quadrature literature. Some of the explanation surely has to do with custom going back centuries, before the appearance of computers, when the algebraic simplicity of polynomials would have been a telling advantage. If one had to give a mathematical answer still with some validity today, it would probably be that a polynomial formula is optimal if the order is fixed while the grid size is decreased to zero. If the order increases to $\infty$ on a fixed interval of integration, however, polynomial formulas are in no sense optimal.

In particular, a “transformed Gauss” quadrature formula can be obtained by applying Gauss quadrature to the integral on the right in the formula

$$
\int _ { - 1 } ^ { 1 } f ( x ) = \int _ { - 1 } ^ { 1 } f ( g ( s ) ) g ^ { \prime } ( s ) d s .
$$

To illustrate this transplanted quadrature idea we pick a wiggly function,

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/c2dcd2e35bcba46969634a33e170e23dc0c24f900efb28070c675e1eabe709fb.jpg)

Here is a code in which I represents Gauss quadrature and I2 is transformed Gauss quadrature—and we see that the dots decrease about $3 0 \%$ more slowly than the squares.

gp $=$ diff(g); Iexact $=$ sum(f); err $=$ []; err2 $=$ []; nn = 50:50:2000;   
for $\texttt { n } = \texttt { n n }$ $[ \bf s _ { \tau } , \bf w ] _ { \tau } = \mathrm { \sf ~ 1 e g p t s } \left( \ln \mathrm { \right) ; \mathrm { ~ \cal ~ I ~ } = \mathrm { \bf ~ w * f } \left( \bf s \right) }$ ; err $=$ [err abs(I-Iexact)]; $\begin{array} { r } { \texttt { I 2 } = \texttt { w * } ( \texttt { f } ( \texttt { g } ( \texttt { s } ) ) * \wp ( \texttt { s } ) ) } \end{array}$ ; err2 $=$ [err2 abs(I2-Iexact)];   
end   
semilogy(nn,err,'.-'), hold on, semilogy(nn,err2,'s-m')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/44f69757e2b5552406911841849cb223729abd383099b2bb62db946daa1ca729.jpg)

We emphasize that in the end a quadrature formula is just a quadrature formula, as specified in (19.3):

$$
I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) .
$$

Gauss leads to one choice of nodes and weights, Clenshaw–Curtis leads to another, transplanted Gauss leads to a third, and transplanted Clenshaw–Curtis leads to a fourth. Regardless of what concepts may have been employed in the derivation, in the end the quadrature formula just takes a linear combination of function values, and the transformed formulas usually outperform the classical ones. For example, in [Hale & Trefethen 2008] it is proved that the transformed Gauss formulas based on mapping $E _ { 1 . 1 }$ to an infinite strip converge $5 0 \%$ faster than Gauss quadrature for the class of functions analytic in the $\varepsilon$ -neighborhood of $[ - 1 , 1 ]$ , for any $\varepsilon < 0 . 0 5$ .

This chapter has shown that polynomials are not the only effective general linear class of approximants for general functions $f$ on an interval and indeed are often suboptimal. There is much more that can be said on this subject. For example, there is the matter of how the mapping $g$ was derived and what other maps might be useful; an influential family of maps was introduced by Kosloff and Tal-Ezer [1993]. Another topic we have not discussed is the application to spectral methods, Kosloff and Tal-Ezer’s motivation, and it is here that transformations of variables are perhaps most important in practice. Finally, there is the idea of using the map $g$ for rational functions rather than polynomials. The last two ideas have been combined powerfully in Tee’s adaptive rational spectral collocation method based on adaptively determined conformal maps [Tee & Trefethen 2006, Hale & Tee 2009].

Summary of Chapter 22. Although many numerical methods are based on polynomial approximations of a function $f \in C ( [ - 1 , 1 ] )$ , such approximations are not optimal, for polynomials have higher resolution near the endpoints of the interval than near the middle. By a conformal transplantation one can derive approximations that are up to $\pi / 2$ times more efficient.

Exercise 22.1. A challenging integrand. Repeat the Gauss vs. transformed Gauss quadrature experiment for the “spiky integrand” (18.2). By approximately what percentage is Gauss slower than transformed Gauss for this function? How do you account for this behavior?

Exercise 22.2. Chebfun '	
'. [Unfortunately to carry out this exercise it is necessary to acquire the pre-2014 Chebfun version 4.] Chebfun contains a 'map' parameter that enables one to explore some of the ideas of this chapter in an automatic fashion (try help maps for information). To illustrate this, construct $\textbf { f } = \mathbf { \nabla } _ { 1 } / ( 1 { + } 2 5 { * } \mathbf { x } \hat { \mathbf { \nabla } } 2 )$ with both $\mathrm { ~ \tt ~ x ~ } =$ chebfun $( ^ { \prime } { \tt x } ^ { \prime } )$ as usual and also $\qquad \tt { x } =$ chebfun( $" \mathbf { x } \cdot \mathbf { \lambda }$ ,'map',{'sausage',9}). How do the plotcoeffs results compare? (b) What if the parameter 9 is varied to $1 , 3 , 5 , \ldots , 1 5 ?$ (This is the degree of the expansion in (22.1).)

Exercise 22.3. Transformed Clenshaw–Curtis quadrature. Generate the final plot of this chapter again, but now with two further curves added corresponding to Clenshaw– Curtis and transformed Clenshaw–Curtis quadrature. How do the results compare with those for Gauss and transformed Gauss?

Exercise 22.4. Gauss quadrature transformed by an infinite strip. Better than a sausage map for some applications is a map onto an infinite strip. Following the last two exercises, use $\begin{array} { r l } { \mathbf { x } } & { { } = } \end{array}$ chebfun( $" \mathbf { x } \cdot \mathbf { \xi }$ ,'map',{'strip',1.4}) to reproduce the final plot of this chapter again, now with one other curve added corresponding to Gauss quadrature transformed by the strip map of the Bernstein ellipse of parameter $\rho = 1 . 4$ . How do the results compare with those from the sausage transformation?

Exercise 22.5. Interpolation of equispaced data. Here is a scheme for interpolation of data at equispaced points on $[ - 1 , 1 ]$ : use a conformal map $g ^ { - 1 }$ to transform the equispaced grid to an approximate Chebyshev grid, and then compute a polynomial interpolant by means of the barycentric formulas (5.11)–(5.12). Explore this method in Chebfun for interpolation of the Runge function $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ where $g$ is the map (22.1), using interp1 to compute the interpolant. Do these approximants weaken the Runge phenomenon? (A theorem of [Platte, Trefethen $\&$ Kuijlaars 2011] asserts that no approximation scheme can eliminate the Runge phenomenon entirely.)

# Chapter 23. Nonlinear Approximation: Why Rational Functions?

Up to now, this book has been about polynomials or, in the last chapter, their transplants. The final six chapters of the book are about rational functions, which have been a mainstay of approximation theory from the beginning. Why do rational approximations occupy such a large place in the literature? Polynomials are familiar and comfortable, but rational functions seem complex and specialized. Is their position in approximation theory justified, or is it an artifact of history, perhaps a holdover from the precomputer era? In this chapter we attempt to answer these questions, and in doing so we shall find ourselves considering the broader question of what the uses are of the whole subject of approximation theory.

I think the answer is this. Although rational functions indeed became an established part of approximation theory long before computers and many of today’s practical applications, their place in the subject is deserved. Their importance stems from a conjunction of two facts. On the one hand, rational functions are more powerful than polynomials at approximating functions near singularities and on unbounded domains. On the other hand, for various reasons related, for example, to partial fraction decompositions, they are easier to work with than their nonlinearity might suggest—indeed, sometimes no more complicated than polynomials.

A rational function is the ratio of two polynomials, and in particular, given $m \geq 0$ and $n \geq 0$ , we say that $r$ is a rational function of type $( m , n )$ if it can be written as a quotient $p _ { m } / q _ { n }$ with $p _ { m } \in \mathcal { P } _ { m }$ and $q _ { n } \in \mathcal { P } _ { n }$ . The set of all rational functions of type $( m , n )$ is denoted by $\mathcal { R } _ { m n }$ , and any $r \in \mathcal { R } _ { m n }$ can be written in the form

$$
r ( x ) = \sum _ { k = 0 } ^ { m } a _ { k } x ^ { k } { \Bigg / } \sum _ { k = 0 } ^ { n } b _ { k } x ^ { k }
$$

for some real or complex coefficients $\{ a _ { k } \}$ and $\left\{ b _ { k } \right\}$ . The degrees need not be exact, i.e., there is no requirement that $a _ { m }$ or $b _ { n }$ must be nonzero. Nor do we require that the numerator and denominator be relatively prime, that is, that they have no common zeros.

Suppose, however, that for some nonzero $r \in \mathcal { R } _ { m n }$ , we choose a representation with relatively prime numerator and denominator. Define $\mu \leq m$ to be the index of the highest degree nonzero numerator coefficient and similarly $\nu \leq n$ for the denominator, and further normalize the coefficients by requiring $b _ { \nu } = 1$ . Then we can write

$$
r ( x ) = \sum _ { k = 0 } ^ { \mu } a _ { k } x ^ { k } \Biggl / \sum _ { k = 0 } ^ { \nu } b _ { k } x ^ { k } ~ , ~ a _ { \mu } \neq 0 , ~ b _ { \nu } = 1 .
$$

In this case $r$ has exactly $\mu$ finite zeros and $\nu$ finite poles, counted with multiplicity: we say that $r$ is of exact type $( \mu , \nu )$ . (The case in which $r$ is identically zero is a special one, with no nonzero coefficients in the numerator, and we say it has exact type $( - \infty , 0 )$ .) If $\mu > \nu$ , then $r$ has a pole at $x = \infty$ of order $\mu - \nu$ , and if $\nu > \mu$ , it has a zero at $x = \infty$ of order $\nu - \mu$ . Basic properties of rational functions are described in books of complex analysis such as [Ahlfors 1953, Henrici 1974, Markushevich 1985].

These representations highlight the nonlinearity of rational functions, but a different perspective is suggested when we represent them by partial fractions. (Partial fractions were the subject of Jacobi’s PhD thesis [1825], and an excellent general reference is Chapter 7 of [Henrici 1974].) In the simplest situation, consider

$$
r ( x ) = \sum _ { k = 1 } ^ { n } { \frac { c _ { k } } { x - \xi _ { k } } } ,
$$

where $\{ \xi _ { k } \}$ are distinct real or complex numbers. For any coefficients $\left\{ c _ { k } \right\}$ , this is a rational function of type $( n - 1 , n )$ . The number $c _ { k }$ is the residue of $r$ at $\xi _ { k }$ . This representation highlights the linear aspects of rational functions. For example, whereas computing the integral of $r$ written in the form $p / q$ looks daunting, in the representation (23.3) we have simply

$$
\int ^ { x } r ( s ) d s = C + \sum _ { k = 1 } ^ { n } c _ { k } \log ( x - \xi _ { k } ) .
$$

In applications, it is interesting how often a formula like this turns out to be instrumental in making a rational function useful.

The partial fraction form (23.3) does not apply to all rational functions. One limitation is that it always represents a rational function of exact type $( \mu , \nu )$ with $\mu \ < \nu$ . Another is that it does not represent all functions of this kind, since it cannot account for poles of multiplicity greater than 1. The following theorem gives a partial fraction representation for the general case.

Theorem 23.1. Partial fraction representation. Given $m , n \ \geq \ 0$ , let $r \in \mathcal { R } _ { m n }$ be arbitrary. Then $r$ has a unique representation in the form

$$
r ( x ) = p _ { 0 } ( x ) + \sum _ { k = 1 } ^ { \mu } p _ { k } ( ( x - \xi _ { k } ) ^ { - 1 } ) ,
$$

where $p _ { 0 }$ is a polynomial of exact degree $\nu _ { 0 }$ for some $\nu _ { 0 } \leq m$ (unless $p = 0$ ) and $\left\{ p _ { k } \right\}$ , $1 \leq k \leq \mu$ , are polynomials of exact degrees $\nu _ { k } ~ \geq ~ 1$ with $p _ { k } ( 0 ) = 0$ and $\scriptstyle \sum _ { k = 1 } ^ { \mu } \nu _ { k } \leq n$ .

Proof. See Theorem 4.4h of [Henrici 1974].

The function $p _ { 0 }$ is the polynomial part of $r$ , and $p _ { k } \big ( ( x - \xi _ { k } ) ^ { - 1 } \big )$ is its principal part at $\xi _ { k }$ .

This is all we shall say for the moment about the mathematics of rational functions. Let us now turn to the main subject of this chapter, the discussion of why these functions are useful in approximation theory and approximation practice.

The right place to start is with a cautionary observation. Rational functions are not always better than polynomials. Indeed, consider the most basic of all situations, in which a function $f$ is analytic in a $\rho$ -ellipse $E _ { \rho }$ for some $\rho > 1$ . For such a function, by Theorem 8.2, polynomial approximations will converge at the rate $O ( \rho ^ { - n } )$ . It turns out that a typical convergence rate for type $( n , n )$ rational functions is $O ( \rho ^ { - 2 n } )$ . So, doubling the number of parameters to be determined sometimes just approximately doubles the convergence rate. (In fact, sometimes it does not increase the convergence rate at all [Szabados 1970].) For applications of this kind, rational functions may outperform polynomials, but often it is by a rather modest factor.

For example, here are a pair of curves showing $\| f - p _ { 2 n } ^ { * } \|$ (dots) and $\| f - r _ { n n } ^ { * } \|$ (stars) as functions of $n$ for $f ( x ) = \exp ( - x ^ { 4 } )$ , where $p _ { 2 n } ^ { * }$ and $r _ { n n } ^ { * }$ are the best approximations to $f$ in $\mathcal { P } _ { 2 n }$ and $\mathcal { R } _ { n n }$ , respectively. (We shall discuss rational best approximation in the next chapter.) Both curves decrease slightly faster than geometrically, and there is not much difference between them. (The rational approximations here should in principle be computed with minimax, but Chebfun’s rational Remez algorithm is currently not robust enough, so cf is used instead.)

$\begin{array} { r } { \mathrm { ~ x ~ = ~ c h e b f u n ( ~ ` ~ x ' ~ ) ~ ; ~ f ~ = ~ e x p ( - x ' 4 ) ~ ; ~ n n ~ = ~ 0 : 2 0 ; ~ e x r p ~ = ~ [ ] ~ ; ~ e x r r ~ = ~ [ ] ~ ; } } \end{array}$   
for $\texttt { n } = \texttt { n n }$ p2n $=$ minimax(f,2\*n); errp $=$ [errp norm(f-p2n,inf)]; [p,q,foo] $=$ cf(f,n,n); $\mathtt { r n n } = \mathtt { p } / { \mathtt { q } }$ ; errr $=$ [errr norm(f-rnn,inf)];   
end   
semilogy(nn,errp,'.-'), hold on, semilogy(nn,errr,'h-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/5348b9738a28172861973c7f703c95f71573f070eebf075b4b16c11224e9f365.jpg)

What makes rational functions important is that, in contrast to this example, there are many problems where one wants to operate near singularities, or on unbounded domains. For these problems, rational approximations may converge much faster than polynomials. For example, here is an experiment like the last one, but with $f ( x ) = \left| x \right|$ . For this function, a type $( n , n )$ rational approximant with $n = 1 5 0$ gives 16-digit accuracy, whereas polynomial approximants would need $n = 1 0 ^ { 1 5 }$ to do so well. (Again this code should in principle use minimax but cannot, so known best approximation errors are hardwired in.)

f = abs(x); xx = linspace(-1,1,1000); $\mathtt { n n } ~ = ~ 0 : 5 0$ ; errp = [];   
errr $=$ [.5 4.37e-2 8.50e-3 2.28e-3 7.37e-4 2.69e-4 1.07e-4 ... 4.60e-5 2.09e-5 9.89e-6 4.88e-6 2.49e-6 1.30e-6 ... 6.3\*exp(-pi\*sqrt(26:2:max(nn)))];   
errr $=$ kron(errr,[1 1]); errr(end) $=$ [];   
for $\texttt { n } = \texttt { n n }$ p2n $=$ minimax(f, $^ { 2 * \mathrm { n } }$ ); errp $=$ [errp norm(f(xx)-p2n(xx),inf)];   
end   
semilogy(nn,errp,'.-'), hold on, semilogy(nn,errr,'h-r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/8ef41d96a0d562740d0ad1f854d6a45a57a6609f840faa242b7ab614da97b403.jpg)

The approximation of $| x |$ by rational functions is one of the “two famous problems” to be considered in Chapter 25. Half a century ago Donald Newman proved that whereas polynomial approximants to $| x |$ converge just at the rate $O ( n ^ { - 1 } )$ , for rational approximants the rate is $\exp ( - C { \sqrt { n } } )$ with $C > 1$ [Newman 1964]. This result rigorously established the possibility of an exponential difference in effectiveness of the two types of approximations.

The rest of this chapter is devoted to an outline of 12 applications in which rational approximations are useful. In most of these examples, there is a singularity or unbounded domain in the picture. The exceptions are applications #1 and #8, where rational functions outperform polynomials less decisively.

1. Elementary and special functions. Classically, approximation theory brings to mind the problem of designing subroutines for computers to evaluate elementary functions, like $\sin ( x )$ , and special functions, like Airy or Bessel functions. For some of these applications, especially when the number of digits of accuracy required is known in advance, rational approximations prove to be the best choice. A classic project in this line is the SPECFUN software package [Cody 1993], descendant of the earlier FUNPACK [Cody 1975], which uses rational best approximations to evaluate Bessel functions, error functions, gamma functions, and exponential integrals to 18 digits of accuracy. For many years a driving force behind these software products and an expert on the matter of practical rational approximations was W. J. Cody at the Argonne National Laboratory; Cody’s version of the rational Remez algorithm is described in [Cody, Fraser & Hart 1968]. For a presentation of some of the state of the art early in the 21st century, see [Muller 2006].

2. Digital filters. In electrical engineering, the construction of low-pass, highpass, and other digital filters often involves approximation of functions with jumps. (For these problems the approximation domain is usually the unit circle in the complex plane.) Jumps amount to singularities on or near the domain of approximation, and Theorem 8.3 implies that polynomials have no chance of rapid convergence for such functions. As Newman’s theorem would lead us to expect, rational approximations sometimes do much better. Engineers use the term FIR (Finite Impulse Response) for polynomial filters and IIR (Infinite Impulse Response) in the rational case [Oppenheim, Schafer & Buck 1999].

3. Convergence acceleration for sequences and series. The mathematical sciences are full of problems of extrapolation. For example, one might be interested in $\scriptstyle \operatorname* { l i m } _ { h \to 0 } f ( h )$ , where $f ( h )$ is a quantity computed numerically on a grid of spacing $h$ . For such a problem, $f$ is often analytic at $h = 0$ , in which case Richardson extrapolation, based on interpolating the data by a polynomial, may be beautifully effective. On the other hand, suppose we want to evaluate $\scriptstyle \operatorname* { l i m } _ { n \to \infty } a _ { n }$ for a sequence $\{ a _ { n } \}$ . We can regard this problem too as $\scriptstyle \operatorname* { l i m } _ { h \to 0 } f ( h )$ with the definition $f ( 1 / n ) =$ $a _ { n }$ , but now, in many applications, $f ( h )$ will not be analytic at $h = 0$ and Richardson extrapolation will be ineffective. The more powerful extrapolation methods that have been developed for such problems, such as Aitken extrapolation and the epsilon algorithm, are mostly based on rational approximations. See Chapter 28.

4. Determination of poles. Suppose a function $f$ is analytic on $[ a , b ]$ and has some real or complex poles nearby whose positions and residues are of interest. Classic examples of such problems arise in the study of phase transitions in condensed matter physics. If we approximate $f$ by polynomials on $[ a , b ]$ , then by Theorem 8.3, the convergence fails outside a $\rho$ -ellipse of analyticity, so not much information about poles can be obtained. If we approximate by rational functions, exponential convergence to some of the poles can often be achieved. Specifically, a good strategy is to consider the poles of $r _ { m n }$ for moderate values of $n$ , where $r _ { m n }$ is a rational approximant to $f$ obtained by Pad´e or Chebyshev–Pad´e approximation or rational interpolation or least-squares. See Chapters 26–28.

5. Analytic continuation. If $f$ is analytic on $[ a , b ]$ , then in many applications it can be analytically continued, in theory, to the rest of the complex plane, apart from exceptional points and curves in the form of poles, other singularities, and branch cuts. Computing such continuations numerically, however, is a difficult problem. One could try approximating $f$ by a polynomial, but this approach will be useless outside the largest Bernstein ellipse in which $f$ is analytic. Rational functions, by contrast, may be effective for continuation much further out. Again see Chapter 28.

6. Eigenvalues and eigenvectors of matrices. Suppose we want to compute an eigenvector of a matrix $A$ . One approach, the power method, is to pick a starting vector $x$ and compute $\scriptstyle \operatorname* { l i m } _ { n \to \infty } A ^ { n } x$ , but the convergence of this polynomial-based idea is very slow in general. A much faster method, inverse iteration, is based on rational approximations: find an approximation $\mu$ to some eigenvalue $\lambda$ and compute $\scriptstyle \operatorname* { l i m } _ { n \to \infty }$ $( A - \mu I ) ^ { - n } x$ . The convergence gets faster the closer $\mu$ is to the singularity $\lambda$ , and exploitation of this effect leads to the spectacularly effective QR algorithm for matrix eigenvalues and eigenvectors [Francis 1961]. Experts in numerical linear algebra do not usually think about rational approximations when discussing inverse iteration or the QR algorithm, but such approximations come explicitly to the fore in the analysis of extensions such as shift-and-invert Arnoldi or rational Krylov iteration [G¨uttel 2010].

7. Model reduction and optimal control. A major topic in numerical linear algebra and control theory is the approximation of complex input-output systems by simpler ones for more efficient computation. Via the Laplace transform, problems of this kind (in the case of continuous as opposed to discrete time) can in many cases be reduced to problems of approximation on the imaginary axis in the complex plane. The unbounded domain makes rational approximations a natural choice, and in fortunate cases, a system with hundreds of thousands of degrees of freedom may be reduced to a model with just dozens or hundreds. One set of methods for such problems goes by the name of $H _ { \infty }$ approximation, based on results by Adamjan, Arov, and Krein [1971] and Glover [1984] that are related to CF approximation (Chapter 20). For more information see [Antoulas 2005, Zhou, Doyle & Glover 1996, Embree & Sorensen 2013].

8. Exponential of a matrix. A famous paper in numerical analysis is “Nineteen Dubious Ways to Compute the Exponential of a Matrix,” by Moler and Van Loan in 1978, reprinted in expanded form 25 years later [Moler & Van Loan 2003]. These authors compared many algorithms for computing $e ^ { A }$ and reached the conclusion that the most effective was a scaling-and-squaring method based on Pad´e approximation [Ward 1977]. Here, first $A$ is scaled so that its norm is on the order of 1. Then $e ^ { A }$ is approximated by $r ( A )$ , where $r$ is a type $( n , n )$ Pad´e approximant to $e ^ { x }$ (Chapter 27). This is an example where rational approximations outperform polynomials not decisively but by a more or less constant factor. This approach is used by the matrix exponential program expm in MATLAB, which for many years was based on type $( 6 , 6 )$ Pad´e approximation. A more careful analysis of the scalingand-squaring algorithm was later provided by Higham [2009], who concluded that a better choice was type (13, 13), and the expm code was adjusted accordingly in MATLAB Version 8. In [Higham & Al-Mohy 2010, Appendix] the authors conclude that Pad´e approximants are up to $2 3 \%$ more efficient than Taylor polynomials in this application.

9. Numerical solution of stiff PDEs. A particularly important set of problems related to matrix exponentials are derived from PDEs. The starting point of such applications is the Laplace operator $\Delta$ on a spatial domain $\Omega$ with Dirichlet boundary conditions, which has an infinite set of negative real eigenvalues diverging to $- \infty$ . To solve the heat equation $\partial u / \partial t = \Delta u$ numerically on $\Omega$ with initial data $u ( x , 0 ) = u _ { 0 }$ , one would like to be able to compute the matrix exponential product $e ^ { t A } v _ { 0 }$ , where $A$ is a matrix discretization of $\Delta$ and $v _ { 0 }$ is a discretization of $u _ { 0 }$ . The wide range of eigenvalues makes such a problem “stiff,” posing challenges for numerical methods. One method for coping with stiffness is to find a rational function $r ( x )$ that approximates $e ^ { x }$ accurately on $( - \infty , 0 ]$ , hence in particular at all of the eigenvalues of $A$ , and then to compute $r ( t A ) v _ { 0 }$ . Polynomials cannot approximate a bounded function uniformly on an infinite interval, but rational functions can. This problem of rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ goes back to Cody,

Meinardus, and Varga [1969], whose “1/9 conjecture,” eventually settled by Gonchar and Rakhmanov [1989], is the other famous problem considered in Chapter 25. Generalizations have become important in scientific computing in recent years in the design of exponential integrators for the fast numerical solution of stiff nonlinear ODEs and PDEs [Hochbruck & Ostermann 2010, Kassam & Trefethen 2005, Schmelzer & Trefethen 2007].

10. Quadrature formulas. As we have seen in Chapter 19, a quadrature formula approximates an integral $\begin{array} { r } { I ~ = ~ \int _ { a } ^ { b } f ( x ) d x } \end{array}$ by a finite linear combination $\begin{array} { r } { I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) } \end{array}$ . If the weights $w _ { k }$ are interpreted as residues of a rational function $r ( x )$ with poles at the nodes $x _ { k }$ , then by estimation of a Cauchy integral over a contour $\Gamma$ enclosing $[ a , b ]$ in the complex plane, one can show that the error $I - I _ { n }$ is bounded in terms of the size of $f$ in the region enclosed by $\Gamma$ times the error in approximation of the analytic function $\log ( ( x + 1 ) / ( x - 1 ) )$ by $r$ over the same region [Takahasi $\&$ Mori 1971]. So every quadrature formula is connected with a rational approximation problem. In fact, Gauss’s original derivation of the $( n + 1 )$ -point Gauss quadrature formula on $[ - 1 , 1 ]$ was based on exactly this connection: via continued fractions, he considered type $( n , n + 1 )$ Pad´e approximation of $\log ( ( x + 1 ) / ( x - 1 ) )$ at $x = \infty$ [Gauss 1814].

11. Adaptive spectral methods for $P D E s$ . The barycentric interpolation formula has the form of a rational function that reduces to a polynomial for a special choice of weights (Chapter 5). Regardless of the choice of weights, however, one still gets an interpolant, so long as the weights are nonzero, and in some applications there is no compelling reason to force the interpolant to be a polynomial. This opens up the possibility of much more flexible rational interpolants, which have the particular advantage of not being so sensitive to the distribution of the interpolation points. These ideas originated with Salzer [1981] and Schneider and Werner [1986], building on earlier work going as far back as Jacobi [1846], and were later developed by Berrut [1988] and Floater and Hormann [2007]. For ODEs and PDEs, they form the basis of adaptive spectral methods for solving problems whose solutions have singularities close to the region of approximation [Berrut, Baltensperger & Mittelmann 2005, Tee & Trefethen 2006, Hale & Tee 2009].

12. One-way wave equations. Our final application became well known in the 1970s and 1980s [Halpern & Trefethen 1988]. The usual wave equation permits energy propagation in all directions, but there are applications where one would like to restrict to half the permitted angles, a $1 8 0 ^ { \circ }$ range. For example, this idea is useful in underwater acoustics [Tappert 1977], geophysical migration [Claerbout 1985], and the design of absorbing boundary conditions for numerical simulations [Lindman 1975, Engquist $\&$ Majda 1977]. How can we define a system that behaves like $u _ { t t } = u _ { x x } + u _ { y y }$ for leftgoing waves, say, with negative $x$ -component of velocity, while not propagating rightgoing waves? (The subscripts represent partial derivatives.) A Fourier transform shows that the dispersion relation of such a system should be $\xi = \omega \sqrt { 1 - s ^ { 2 } }$ , where $s = \eta / \omega$ and $\omega , \xi , \eta$ are the dual variables to $t , x , y$ . Only the positive branch of the square root should be present, making this system a pseudodifferential operator. However, a rational approximation ${ \sqrt { 1 - s ^ { 2 } } } \approx r ( s )$ simplifies this to a differential equation. For example, the type $( 2 , 2 )$ Pad´e approximation $r ( s ) = ( 1 - \textstyle { \frac { 3 } { 4 } } s ^ { 2 } ) / ( 1 - \textstyle { \frac { 1 } { 4 } } s ^ { 2 } )$ leads to the PDE $\begin{array} { r } { u _ { x t t } - \frac { 1 } { 4 } u _ { x y y } = u _ { t t t } - \frac { 3 } { 4 } u _ { t y y } } \end{array}$ , sometimes known as the “ $4 5 ^ { \circ }$ equation” because it has high accuracy approximately for angles up to $4 5 ^ { \circ }$ . In this application, rational functions are superior to polynomials both because of higher accuracy in view of the singularities at $s = \pm 1$ , and because polynomial approximations lead to PDEs that are ill-posed [Trefethen $\&$ Halpern 1986].

We have just seen a list of 12 applications. In concluding this chapter I would like to consider what light these may shed on the biggest question of all, namely, What is the use of approximation theory?

To see some possible views, let us go back to 1901. That was the year of Runge’s landmark paper (Chapter 13), whose title was $^ { 1 1 }$

“On Empirical Functions and Interpolation between Equidistant Ordinates.”

In reading this today, one is struck by the word “empirical.” The empirical theme is echoed in the opening sentence:

The relationship between two measurable quantities can, strictly speaking, not be found by observation.

Runge goes on to mention “observations” six times more in the opening paragraph. It would seem that his motivation is the processing of scientific data: interpolation in the traditional sense of evaluating a function at points lying between those at which it is listed in a table.

The next year, 1902, brought another landmark of approximation theory: Kirchberger’s PhD thesis under Hilbert in G¨ottingen, which included the first systematic statement and proof of the equioscillation theorem for polynomial approximation (Theorem 10.1). Here is the first paragraph of Kirchberger’s thesis, as reprinted in the first paragraph of his published paper a year later [1903], setting forth a clear motivation for approximation theory. We may imagine that this was probably also Hilbert’s view of the subject.12

The notion of a function entails the assumption that a numerical value of the function can be calculated for any value of the independent variable. But since the only operations that can really be carried out numerically are the four elementary operations of addition, subtraction, multiplication and division, or strictly speaking only the first three of these, it follows that we are really only masters of more general functions insofar as we can replace them by rational functions, that is, represent them approximately. This highlights the great significance of approximation problems for the whole of mathematics and the special role of approximation by polynomials and rational functions. Indeed, for numerical calculation at least, any use of other approximations such as trigonometric functions presupposes that these can in turn be approximated by rational functions.

Updated to the 21st century, we may say that Kirchberger’s justification of approximation theory is all about machine arithmetic. Approximation by polynomials and rational functions is important, he is saying, because ultimately computers can only carry out polynomial and rational operations.

Both Runge’s emphasis on data and Kirchberger’s emphasis on arithmetic capture aspects of approximation theory that remain valid today. In particular, Kirchberger’s paragraph seems a remarkably clear statement of a justification of approximation theory that in a certain philosophical sense seems almost unarguable (although the line between “primitive” operations like $^ +$ and “derived” ones like $\sin ( \cdot )$ is not always so clear on actual computers, with their multiple levels of hardware, software, and microcode). The same argument is often seen nowadays.

Nevertheless, I do not think data analysis and machine arithmetic get at the heart of why approximation theory is important and interesting. In fact I don’t think Runge’s words even capture the truth of why he was interested in the subject! (He becomes more of a mathematician in the second half of his paper.) What these observations miss is the importance of algorithms.

Let us look again at the list of applications. Kirchberger’s motivation could be said to be on target for #1 and #2 (evaluation of functions, digital filters), and Runge’s for #3, $\# 4$ , and #5 (extrapolation, determination of poles, analytic continuation). But the remaining seven items need to be accounted for in other ways. It is noteworthy that applications #6 to #9 all involve matrices, sometimes of very large dimension (eigenvalues and eigenvectors, model reduction, exponentials of matrices, stiff PDEs). Applications #9 to #12 all involve integrals and differential equations (stiff PDEs, quadrature, adaptive spectral methods, one-way wave equations). In most of these problems we seem a long way from scalars $x$ and $r ( x )$ : the polynomial and rational operations are applied to matrices and operators, not just numbers.

Chebfun provides another interesting data point (for polynomials rather than rational functions). Chebfun is built on a century of developments in polynomial interpolation and approximation, and it makes it possible to work with univariate functions numerically in almost unlimited ways. A particularly important Chebfun capability is finding roots of a function $f ( x )$ , which enables many further operations like computing extrema, absolute values, and 1-norms. Chebfun finds the roots by the algorithm proposed by Good [1961] and Boyd [2002] and described in Chapter 18: approximate $f$ by polynomial interpolants, and then find roots of the polynomials by computing eigenvalues of colleague matrices. This is as powerful an application of approximation theory as one could ask for, but it has little to do with data analysis or machine arithmetic.

Why are polynomial and rational approximations useful? Not because $r ( x )$ is easier to evaluate than $\exp ( x )$ , but because $r ( A )$ is easier to evaluate than $\exp ( A )$ , and $r ( \partial / \partial x )$ is easier to evaluate than $\exp ( \partial / \partial x )$ ! Not because we can evaluate $p ( x )$ , but because we can find its roots !

Summary of Chapter 23. Rational functions are more powerful than polynomials for approximating functions near singularities or on unbounded domains. This is the reason for their importance in approximation theory and approximation practice.

Exercise 23.1. Examples of partial fractions. Express the following functions in partial fraction form: (a) $x ^ { 3 } / ( 1 - x )$ , (b) $x / ( x ^ { 2 } - 4 )$ , (c) $x ^ { 2 } / ( x ^ { 2 } - 4 ) ^ { 2 }$ , (d) $( 1 - x ^ { 3 } ) / ( 1 + x ^ { 2 } )$ . Exercise 23.2. Uses of partial fractions. (a) Express the function $r ( x ) = ( x ( x +$ $1 ) ( x + 2 ) ) ^ { - 1 }$ in partial fraction form. (b) What is its integral from 1 to $t$ ? (c) What is the sum of the infinite series $r ( 1 ) + r ( 2 ) + r ( 3 ) + \cdot \cdot \cdot ?$

Exercise 23.3. Another infinite series. (a) Based on numerical experiments, conjecture a value of the infinite sum $1 / ( 1 \cdot 3 \cdot 5 ) + 2 / ( 3 \cdot 5 \cdot 7 ) + 3 / ( 5 \cdot 7 \cdot 9 ) + \cdot \cdot \cdot .$ (b) Verify your conjecture with partial fractions.

Exercise 23.4. A trigonometric identity. Verify the identity $1 / ( 1 \cdot 3 \cdot 5 ) - 1 / ( 7 \cdot 9 \cdot$ $1 1 ) + 1 / ( 1 3 \cdot 1 5 \cdot 1 7 ) - \cdot \cdot \cdot = \pi / 4 8$ .

Exercise 23.5. Polynomial vs. rational experiments. Produce plots comparing $E _ { 2 n , 0 } ( f )$ and $E _ { n , n } ( f )$ for the following functions $f$ defined on $[ - 1 , 1 ]$ : (a) $\log ( 1 + x ^ { 2 } )$ , (b) $\operatorname { t a n h } ( 5 x )$ , (c) $\exp ( x ) / ( 2 - x )$ .

Exercise 23.6. Approximation of a gamma function. Consider the function $f ( x ) =$ $\Gamma ( x + 2 )$ on $[ - 1 , 1 ]$ , which has simple poles at $x = - 2 , - 3 , \ldots .$ . Determine analytically the geometric convergence rates to be expected as $m \to \infty$ for rational approximants to $f$ of types (a) $( m , 0 )$ , (b) $( m , 1 )$ , (c) $( m , 2 )$ .

# Chapter 24. Rational Best Approximation

Chapter 10 considered best or “minimax” approximation by polynomials, that is, approximation in the $\infty$ -norm, where optimality is characterized by an equioscillating error curve. This chapter presents analogous results for approximation by rational functions. Much remains the same, but a crucial new feature is the appearance in the equioscillation condition of a number known as the defect, which leads to the phenomenon of square blocks of degenerate entries in the “Walsh table” of best approximations. This complication adds a fascinating new dimension to the theory, but it is a complication with destructive consequences in terms of the fragility of rational approximations and the difficulty of computing them numerically. An antidote to some such difficulties may be the use of algorithms based on linearized least-squares and the singular value decomposition, a theme we shall take up in Chapters 26 and 27.

Another new feature in rational approximation is that we must now be careful to distinguish real and complex situations, because of a curious phenomenon: best rational approximations to real functions are in general complex. This effect is intriguing, but it has little relevance to practical problems, so for the most part we shall restrict our attention to approximations in the space $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ consisting of functions in $\mathcal { R } _ { m n }$ with real coefficients.

We will first state the main theorem, then give some examples, and then present a proof. To begin the discussion, we must define the defect. Suppose $r \in \mathcal { R } _ { m n }$ , that is, $r$ is a rational function of type $( m , n )$ . As discussed in the last chapter, this means that $r$ can be written as a fraction $p / q$ in lowest terms with $p$ and $q$ having exact degrees $\mu \leq m$ and $\nu \leq n$ . The defect $d$ of $r$ in $\mathcal { R } _ { m n }$ is the number between $0$ and $n$ defined by

$$
d = \operatorname* { m i n } \{ m - \mu , n - \nu \} \geq 0 .
$$

Note that $d$ is a measure of how far both the numerator and the denominator degrees fall short of their maximum allowed values. Thus $( 1 - x ^ { 2 } ) / ( 1 + x ^ { 2 } )$ , for example, has defect $0$ in $\mathcal { R } _ { 2 2 }$ or $\mathcal { R } _ { 2 3 }$ and defect 1 in $\mathcal { R } _ { 3 3 }$ .

A special case to be noted is the situation in which $r = 0$ , that is, $r$ is identically zero. Recall that in this case we defined $\mu = - \infty$ and $\nu = 0$ , so that $r$ is said to have exact type $( - \infty , 0 )$ . The definition (24.1) remains in force in this case, so if $r = 0$ , we say that $T$ has defect $d = n$ in $\mathcal { R } _ { m n }$ , regardless of $m$ .

The reason why defects matter has to do with the counting of zeros. Suppose $r = p / q \in \mathcal { R } _ { m n }$ has exact type $( \mu , \nu )$ and $\tilde { r } = \tilde { p } / \tilde { q }$ is another function in $\mathcal { R } _ { m n }$ . Then we have

$$
r - \tilde { r } = \frac { p } { q } - \frac { \tilde { p } } { \tilde { q } } = \frac { p \tilde { q } - \tilde { p } q } { q \tilde { q } } ,
$$

a rational function of type $( \operatorname* { m a x } \{ \mu + n , m + \nu \} , n + \nu )$ . By (24.1), this implies that $r - \bar { r }$ is of type $( m + n - d , 2 n - d )$ . Thus $r - \bar { r }$ can have at most $m + n - d$ zeros, and this zero count is a key to equioscillation and uniqueness results.

Here is our main theorem. The study of rational best approximations goes back to Chebyshev [1859], including the idea of equioscillation, though without a precise statement of what form an alternant must take. Existence was first proved by de la Vall´ee Poussin [1911] and Walsh [1931], and equioscillation is due to Achieser [1930].

Theorem 24.1. Equioscillation characterization of best approximants. $A$ real function $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $r ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ , and a function $r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ is equal to $r ^ { * }$ if and only if $f - r$ equioscillates between at least $m + n + 2 - d$ extreme points, where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ .

“Equioscillation” here is defined just as in Chapter 10. For $f - r$ to equioscillate between $k$ extreme points means that there exists a set of numbers $- 1 \leq x _ { 1 } < \cdot \cdot \cdot <$ $x _ { k } \le 1$ such that

$$
f ( x _ { j } ) - r ( x _ { j } ) = ( - 1 ) ^ { j + i } \| f - r \| , \qquad 1 \leq j \leq k ,
$$

with $i = 0$ or 1. Here and throughout this chapter, $\| \cdot \|$ is the supremum norm.

We now give some examples. To begin with, here is a function with a spike at $x = 0$ :

Polynomial approximations of this function converge rather slowly. For example, it takes $n = 2 0$ to achieve 1 digit of accuracy:

[p,err] $=$ minimax(f,10); subplot(1,2,1), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p,err] $=$ minimax(f,20); subplot(1,2,2), plot(f-p), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/71364f9cd98091156bcd840d63950feea6cbb1351b11bd535434152b78f2c657.jpg)

Notice that the extreme points of these error curves are distributed all across $[ - 1 , 1 ]$ , even though the challenging part of the function would appear to be in the middle. As discussed in Chapter 16, this is typical of polynomial best approximations.

If we switch to rational approximations, which can also be computed by the Chebfun minimax command [Filip et al. 2018, Pach´on 2010], the accuracy improves. Here we see error curves for approximations of types $( 2 , 2 )$ and $( 4 , 4 )$ , with much smaller errors despite the degrees being low. Note that most of the extreme points are now localized in the middle.

[p,q,rh,err] $=$ minimax(f,2,2); subplot(1,2,1), plot(f-p/q), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') [p,q,rh,err] $=$ minimax(f,4,4); subplot(1,2,2), plot(f-p/q), hold on plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/5a158a7a1c8b82ee4e508ef486ec2dd932c1de7544806d4b9e8c107d16725881.jpg)

The error curves just plotted provide good examples of the role of the defect in the characterization of best approximants. The function $f$ is even, and so are its best approximations (Exercise 24.1). Thus we expect that the type $( 2 , 2 )$ , $( 3 , 2 )$ , $( 2 , 3 )$ , and $( 3 , 3 )$ best approximations will all be the same function, a rational function of exact type $( 2 , 2 )$ whose error curve has 7 points of equioscillation. For $( m , n ) =$ $( 2 , 2 )$ , the defect is $0$ and there is one more equioscillation point than the minimum $m + n + 2 - d = 6$ . For $( m , n ) = ( 3 , 2 )$ or $( 2 , 3 )$ , the defect is $0$ and the number of equioscillation points is exactly the minimum $m + n + 2 - d$ . For $( m , n ) = ( 3 , 3 )$ , the defect is $1$ and the number of equioscillation points is again exactly the minimum $m + n + 2 - d$ .

Similarly, the error curve in the plot on the right, with 11 extrema, indicates that this rational function is a best approximation not only of type $( 4 , 4 )$ but also of types $( 5 , 4 )$ , $( 4 , 5 )$ , and $( 5 , 5 )$ .

Here is another example, an odd function:

f = x.\*exp(-5\*abs(abs(x)-.3)); plot(f)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/dae37f7f8c0bd16c20f22e13a193c5feb32662b17dbeaebd0596fb863e222e99.jpg)

If we look for a best approximation of type $( 4 , 5 )$ , we find that the numerator has exact degree 3,

[p,q,rh,err] $=$ minimax(f,4,5); chebcoeffs(p)'

ans $=$

0.0000 0.0154 0.0000 0.0045 and the denominator has exact degree 4,

chebcoeffs(q)'

ans =

0.1468 0.0000 0.1987 0.0000 0.0574

The defect is 1, so there must be at least $4 + 5 + 2 - 1 = 1 0$ extreme points in the error curve. In fact, there are exactly 10:

plot(f-p/q), hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/a4eb78e96c299be0b8944715e676a297b9a8a6e5ca0d38788e5458b962e9bf4c.jpg)

We conclude that $r$ is the best approximation of types $( 4 , 4 ) , ( 4 , 5 ) , ( 3 , 4 )$ , and $( 3 , 5 )$ . Let us now turn to the proof of Theorem 24.1. For polynomial approximations, our analogous theorem was Theorem 10.1, whose proof proceeded in four steps:

1. Existence proof via compactness,   
2. Equioscillation $\Rightarrow$ optimality,

3. Optimality equioscillation,

4. Uniqueness proof via equioscillation.

For rational functions, we shall follow the same sequence. The main novelty is in step 1, where compactness must be applied in a subtler way. We shall see an echo of this argument one more time in Chapter 27, in the proof of Theorem 27.1 for Pad´e approximants.

Part 1 of proof: Existence via compactness. For polynomial approximation, in Chapter 10, we noted that $\| f - p \|$ is a continuous function on $\mathcal { P } _ { n }$ , and since one candidate approximation was the zero polynomial, it was enough to look in the bounded subset $\{ p \in { \mathcal { P } } _ { n } : \| f - p \| \leq \| f \| \}$ . Since this set was compact, the minimum was attained.

For rational functions, $\| f - r \|$ is again a continuous function on $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ , and again it is enough to look in the bounded subset $\{ r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } : \| f - r \| \leq \| f \| \}$ or, more simply, the larger bounded set $\{ r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } : \| r \| \leq 2 \| f \| \}$ . The difficulty is that bounded sets of rational functions are not, in general, compact. To illustrate this fact, consider the family of functions

$$
r _ { \varepsilon } ( x ) = { \frac { x ^ { 3 } + \varepsilon } { x ^ { 2 } + \varepsilon } } ,
$$

where $\varepsilon > 0$ is a parameter. For each $\varepsilon$ , $r _ { \varepsilon } ( x )$ is a continuous function on $[ - 1 , 1 ]$ with $\| r _ { \varepsilon } \| = 1$ . As $\varepsilon  0$ , however, $r _ { \varepsilon }$ behaves discontinuously:

$$
\operatorname* { l i m } _ { \varepsilon \to 0 } r _ { \varepsilon } ( x ) = { \left\{ \begin{array} { l l } { 1 , } & { x = 0 , } \\ { x , } & { x \neq 0 . } \end{array} \right. }
$$

So we cannot find a limit function $r _ { 0 }$ by taking a limit as $\varepsilon \  \ 0$ . What saves us, however, is that the spaces of numerators and denominators are both compact, so we can argue that the numerators and denominators separately approach limits and , which in this example would be $x ^ { 3 }$ and $x ^ { 2 }$ . We then define a limiting $p _ { 0 }$ $q _ { 0 }$   
rational function by $r _ { 0 } = p _ { 0 } / q _ { 0 }$ and argue by continuity that it has the necessary properties. This kind of reasoning is spelled out in greater generality in [Walsh 1931].

Suppose then that $\{ r _ { k } \}$ is a sequence of functions in $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ with $\| r _ { k } \| \le 2 \| f \|$ and

$$
\operatorname* { l i m } _ { k \to \infty } \left\| f - r _ { k } \right\| = E = \operatorname* { i n f } _ { r \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } } } \left\| f - r \right\| .
$$

Write each $r _ { k }$ in the form $p _ { k } / q _ { k }$ with $p _ { k } \in \mathcal { P } _ { m }$ , $q _ { k } \in \mathcal { P } _ { n }$ , $q _ { k } ( x ) \neq 0$ for all $x \in [ - 1 , 1 ]$ , and $\| q _ { k } \| = 1$ ; hence $\| p _ { k } \| \leq \| q _ { k } \| \| r _ { k } \| \leq 2 \| f \|$ . Since $\left\{ p _ { k } \right\}$ and $\left\{ q _ { k } \right\}$ lie in compact sets, we may assume by passing to a subsequence if necessary that $p _ { k } \to p ^ { * }$ and $q _ { k } \to q ^ { * }$ for some $p ^ { * } \in \mathcal { P } _ { m }$ and $q ^ { * } \in \mathcal { P } _ { n }$ . Since $\| q _ { k } \| = 1$ for each $k$ , $\| q ^ { * } \| = 1$ too, and thus $q ^ { * }$ is not identically zero but has at most a finite set of zeros on $[ - 1 , 1 ]$ . Now define $r ^ { * } = p ^ { * } / q ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . For all $x \in [ - 1 , 1 ]$ except perhaps the zeros of $q ^ { * }$ , $| f ( x ) - r ^ { * } ( x ) | = \operatorname* { l i m } _ { k \to \infty } | f ( x ) - r _ { k } ( x ) | \leq E$ . By continuity, the same must hold for all $x \in [ - 1 , 1 ]$ , with $p ^ { * }$ having zeros in $[ - 1 , 1 ]$ wherever $q ^ { * }$ does. Thus $r ^ { * }$ is a best approximation to $f$ .

Part 2 of proof: Equioscillation $\Rightarrow$ optimality. Suppose $f { - } r$ takes equal extreme values with alternating signs at $m + n + 2 - d$ points $x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { m + n + 1 - d }$ , and suppose $\| f - \tilde { r } \| < \| f - r \|$ for some $\tilde { r } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . Then $r - \bar { r }$ must take nonzero values with alternating signs at the equioscillation points, implying that it must take the value zero in at least $m + n + 1 - d$ points in between. However, as observed above, $r - \bar { r }$ is of type $( m + n - d , 2 n - d )$ . Thus it cannot have $m + n + 1 - d$ zeros unless it is identically zero, a contradiction.

Part 3 of proof: Optimality equioscillation. Suppose $f - r$ equioscillates at fewer than $m + n + 2 - d$ points, and set $E = \| f - r \|$ . Without loss of generality suppose the leftmost extremum is one where $f - r$ takes the value $- E$ . Then by a compactness argument, for all sufficiently small $\varepsilon > 0$ , there are numbers $- 1 < x _ { 1 } < \dots < x _ { k } < 1$ with $k \leq m + n - d$ such that $( f - r ) ( x ) < E - \varepsilon$ for x $ [ - 1 , x _ { 1 } + \varepsilon ] \cup [ x _ { 2 } - \varepsilon , x _ { 3 } + \varepsilon ] \cup [ x _ { 4 } - \varepsilon , x _ { 5 } + \varepsilon ] \cup$ · · · and $( f - r ) ( x ) > - E + \varepsilon$ for $x \in | x _ { 1 } - \varepsilon , x _ { 2 } + \varepsilon | \cup | x _ { 3 } - \varepsilon , x _ { 4 } + \varepsilon | \cup \cdot \cdot \cdot$ . Let $r$ be written in the form $p / q$ , where $p$ has degree $\mu \leq m - d$ and $q$ has degree $\nu \leq n - d$ , with $p$ and $q$ having no roots in common. The proof now consists of showing that $r$ can be perturbed to a function $\tilde { r } = ( p + \delta p ) / ( q + \delta q ) \in \mathcal { R } _ { m n }$ with the properties that $\| \tilde { r } - r \| < \varepsilon$ and $\bar { r } - r$ is strictly negative for $x \in [ - 1 , x _ { 1 } - \varepsilon ] \cup [ x _ { 2 } + \varepsilon , x _ { 3 } - \varepsilon ] \cup [ x _ { 4 } + \varepsilon , x _ { 5 } - \varepsilon ] \cup \cdot \cdot \cdot$ and strictly positive for $x \in | x _ { 1 } + \varepsilon , x _ { 2 } - \varepsilon | \cup | x _ { 3 } + \varepsilon , x _ { 4 } - \varepsilon | \cup \cdot \cdot \cdot$ . Such a function $\tilde { r }$ will have error less than $E$ throughout the whole interval $\lfloor - 1 , 1 \rfloor$ . We calculate

$$
\tilde { r } = \frac { p + \delta p } { q + \delta q } = \frac { ( p + \delta p ) ( q - \delta q ) } { q ^ { 2 } } + O ( \lVert \delta q \rVert ^ { 2 } )
$$

and therefore

$$
\tilde { r } - r = \frac { q \delta p - p \delta q } { q ^ { 2 } } + O ( \| \delta p \| \| \delta q \| + \| \delta q \| ^ { 2 } ) .
$$

We are done if we can show that $\delta p$ and $\delta \boldsymbol { q }$ can be chosen so that $q \delta p - p \delta q$ is a nonzero polynomial of degree exactly $k$ with roots $x _ { 1 } , \ldots , x _ { k }$ ; by scaling this $\delta p$ and $\delta \boldsymbol { q }$ sufficiently small, the quadratic terms above can be made arbitrarily small relative to the others, so that the required $\varepsilon$ conditions are satisfied. This can be shown by the Fredholm alternative of linear algebra. The map from the $( m + n + 2 )$ - dimensional set of choices of $\delta p$ and $\delta \boldsymbol { q }$ to the $( m + n + 1 - d )$ -dimensional space of polynomials $q \delta p - p \delta q$ is linear. To show the map is surjective, it is enough to show that its kernel has dimension $d + 1$ but no more. Suppose then that $q \delta p - p \delta q$ is zero, that is, $q \delta p = p \delta q$ . Then since $p$ and $q$ have no roots in common, all the roots of $p$ must be roots of $\delta p$ and all the roots of $q$ must be roots of $\delta \boldsymbol { q }$ . In other words we must have $\delta p = g p$ and $\delta q = g q$ for some polynomial $g$ . Since $\delta p$ has degree no greater than $m$ and $\delta \boldsymbol { q }$ has degree no greater than $n$ , $g$ can have degree no greater than $d$ . The set of polynomials of degree $d$ has dimension $d + 1$ , so we are done.

Part 4 of proof: Uniqueness via equioscillation. Finally, to prove uniqueness, suppose $r$ is a best approximation whose error curve equioscillates between extreme points at $\tilde { r } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ . Then (without loss of generality) $x _ { 0 } < x _ { 1 } < \dots < x _ { m + n + 1 - d }$ , and suppose $( r - \tilde { r } ) ( x )$ must be $\| f - \tilde { r } \| \leq \| f - r \|$ $\leq 0$ at $x _ { 0 } , x _ { 2 } , x _ { 4 } , \ldots$ for some and $\geq 0$ at $x _ { 1 } , x _ { 3 } , x _ { 5 } , \ldots$ . This implies that $r - \tilde { r }$ has roots in each of the $m + n +$ $1 - d$ closed intervals $[ x _ { 0 } , x _ { 1 } ] , \dotsc , [ x _ { m + n - d } , x _ { m + n + 1 - d } ]$ , and since $r - \tilde { r }$ is a rational function of type $( m + n - d , 2 n - d )$ , the same must hold for its numerator polynomial. We wish to conclude that its numerator polynomial has at least $m + n + 1 - d$ roots in total, counted with multiplicity, implying that $r = \tilde { r }$ . The argument for this is the same as given in the proof of Theorem 10.1.

We have now finished the substantial mathematics. It is time to look at some of the consequences.

One of the recurring themes in the subject of rational approximation is the phenomenon of square blocks in the Walsh table. Suppose that a real function $f \in$ $C ( [ - 1 , 1 ] )$ is given, and consider the set of all of its real rational best approximations of type $( m , n )$ for various $m , n \geq 0$ . We can imagine these laid out in an array, with $m$ along the horizontal and $n$ along the vertical. This array is called the Walsh table for $f$ [Walsh 1934].

Generically, all the entries in the Walsh table for a given $f$ will be distinct, and in this case we say that $f$ is normal. Sometimes, however, certain entries in the table may be repeated, and in fact this is a frequent occurrence because it happens whenever $f$ is even or odd. If $f$ is even, then for any nonnegative integers $j$ and $k$ , all of its rational approximations of types $( 2 j , 2 k )$ , $( 2 j + 1 , 2 k )$ , $( 2 j , 2 k + 1 )$ , and $( 2 j + 1 , 2 k + 1 )$ must be the same. Similarly, if $f$ is odd, then all of its approximations of types $( 2 j + 1 , 2 k )$ , $( 2 j + 2 , 2 k )$ , $( 2 j + 1 , 2 k + 1 )$ , and $( 2 j + 2 , 2 k + 1 )$ must be the same. We have already seen a number of examples.

More generally, repeated entries or “degeneracies” in the Walsh table may take complicated forms. Nevertheless the equioscillation condition imposes quite a bit of structure on the chaos. Degeneracies always appear precisely in a pattern of square blocks. The following statement of this result is taken from [Trefethen 1984], where a discussion of various aspects of this and related problems can be found. We shall return to the subject of square blocks in Chapter 27, on Pad´e approximation.

Theorem 24.2. Square blocks in the Walsh table. The Walsh table of best real rational approximants to a real function $f \in C ( [ - 1 , 1 ] )$ breaks into precisely square blocks containing identical entries. (If $f$ is rational, one of these will be infinite in extent.) The only exception is that if an entry $r = 0$ appears in the table, then it fills all of the columns to the left of some fixed index $m = m _ { 0 }$ .

Proof. Given a nonrational function $f$ , let $r \neq 0$ be a best approximation in $\mathcal { R } _ { \mu \nu } ^ { \mathrm { r e a . } }$ l of exact type $( \mu , \nu )$ . (The cases of rational $f$ or $r = 0$ can be handled separately.) By Theorem 24.1, the number of equioscillation points of $f - r$ is $\mu + \nu + 2 + k$ for some integer $k \geq 0$ . We note that $r$ is an approximation to $f$ in $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ for any $m \geq \mu$ and $n \geq \nu$ , and the defect is $\operatorname* { m i n } \{ m - \mu , n - \nu \}$ . Thus by Theorem 24.1, $r$ is the best approximation to $f$ precisely for those values of $( m , n )$ satisfying $m \geq \mu$ , $n \geq \nu$ , and $\mu + \nu + 2 + k \geq m + n + 2 - \operatorname* { m i n } \{ m - \mu , n - \nu \}$ . The latter condition simplifies to $n \leq \nu + k$ and $m \leq \mu + k$ , showing that $r$ is the best approximation to $f$ precisely in the square block $\mu \leq m \leq \mu + k$ , $\nu \leq n \leq \nu + k$ .

Within a square block in the Walsh table, the defect $d$ is equal to zero precisely in the first column and the first row. An approximation with $d = 0$ is sometimes said to be nondegenerate. It can have more points of equioscillation than the generic number $m + n + 2$ , but never fewer.

As mentioned above, the theory of equioscillation and degeneracies is very appealing mathematically. As an example we note a result due to Werner [1964], in completion of earlier work of Maehly and Witzgall [1960]: the type $( m , n )$ best approximation operator, which maps functions $f$ to their best approximations $r _ { m n } ^ { * }$ , is continuous at $f$ with respect to the supremum norm if and only if $f \in \mathcal { R } _ { m n }$ or the corresponding function $r _ { m n } ^ { * }$ is nondegenerate. The essential reason for this effect is that if a function $r ^ { * }$ is the best approximation to $f$ in a nontrivial square block, then a small perturbation $f  { \ddot { f } }$ might fracture that block into smaller pieces [Trefethen 1984]. If $( m , n )$ corresponds to a degenerate position in the block, with $d > 0$ , then the best approximation $\tilde { r } ^ { * }$ for such an $\ddot { f }$ might need to have a higher equioscillation number than that of $r ^ { * }$ for $f$ , requiring $\tilde { r } ^ { * }$ to be far from $r ^ { * }$ if $\| f - r ^ { * } \|$ is positive.

These complications hint at some of the practical difficulties of rational approximation. For example, the Remez algorithm is based on explicit manipulation of alternant sets. If the number of extremal points is not known a priori, it is plausible that one may expect numerical difficulties in certain circumstances. Indeed, this is the case, and so far as I am aware, no implementation of the Remez algorithm for rational approximation, including that of Chebfun, can be called fully robust. Other kinds of algorithms may have better prospects.

We finish by returning to the matter of best complex approximations to real functions. Nonuniqueness of certain complex rational approximations was pointed out by Walsh in the 1930s. Later Lungu [1971] noticed, following a suggestion of Gonchar, that the nonuniqueness arises even for approximation of a real function $f$ on $[ - 1 , 1 ]$ , with examples as simple as type $( 1 , 1 )$ approximation of $| x |$ . (Exercise 24.3 gives another proof that there must exist such examples.) These observations were rediscovered independently by Saff and Varga [1978a]. Ruttan [1981] showed that complex best approximations are always better than real ones in the strict lower-right triangle of a square block, that is, when a type $( m , n )$ best approximation equioscillates in no more than $m + n + 1$ points. Trefethen and Gutknecht [1983a] showed that for every $( m , n )$ with $n \geq m + 3$ , examples exist where the ratio of the optimal complex and real errors is arbitrarily small. Levin, Ruttan, and Varga showed that the minimal ratio is exactly $1 / 3$ for $n = m + 2$ and exactly $1 / 2$ for $1 \leq n \leq m + 1$ [Ruttan & Varga 1989]. None of this has much to do with practical approximation, but it is fascinating.

Summary of Chapter 24. Any real function $f \in C ( [ - 1 , 1 ] )$ has a unique best approximation $r ^ { \ast } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ with respect to the $\infty$ -norm, and $r ^ { * }$ is characterized by having an error curve that equioscillates between at least $m + n + 2 - d$ extreme points, where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ . In the Walsh table of all best approximations to $f$ indexed by $m$ and $n$ , repeated entries, if any, lie in exactly square blocks.

Exercise 24.1. Approximating even functions. Prove that if a real function $f \in$ $C ( [ - 1 , 1 ] )$ is even, then its real best approximations of all types $( m , n )$ are even.

Exercise 24.2. Approximating the Gaussian. The first figures of this chapter considered lower degree polynomial and rational approximations of $\exp ( - 1 0 0 x ^ { 2 } )$ on $[ - 1 , 1 ]$ . Make a plot of the errors in approximations of types $( n , 0 )$ and $( n , n )$ , now taking $n$ as high as you can. (You may find that the cf command takes you farther than minimax.) How do the polynomial and rational approximations compare?

Exercise 24.3. Complex approximations and nonuniqueness. (a) Suppose a real function $f \in C ( [ - 1 , 1 ] )$ takes both the values 1 and $^ { - 1 }$ . Prove that no real rational function $r \in \mathcal { R } _ { 0 n } ^ { \mathrm { r e a l } }$ , for any $n$ , can have $\| f - r \| < 1$ . (b) On the other hand, show that for any $\varepsilon > 0$ , there is a complex rational function $r \in \mathcal { R } _ { 0 n }$ for some $n$ with $\| f - r \| < \varepsilon$ . (Hint: Perturb $f$ by an imaginary constant and consider its reciprocal.) (c) Conclude that type $( 0 , n )$ complex rational best approximations in $C ( [ - 1 , 1 ] )$ are nonunique in general for large enough $_ n$ .

Exercise 24.4. A function with a spike. Plot chebfuns of the function (24.2) for $\varepsilon = 1 , 0 . 1 , \dots , 1 0 ^ { - 6 }$ and determine the polynomial degree $n ( \varepsilon )$ of the chebfun in each case. What is the observed asymptotic behavior of $n ( \varepsilon )$ as $\varepsilon  0$ ? How accurately can you explain this observation based on the theory of Chapter 8?

Exercise 24.5. de la Vall´ee Poussin lower bound. Suppose an approximation $r \in$ $\mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ to $f \in C ( [ - 1 , 1 ] )$ approximately equioscillates in the sense that there are points $- 1 \leq s _ { 0 } < s _ { 1 } < \cdot \cdot \cdot < s _ { m + n + 1 - d } \leq 1$ at which $f - r$ alternates in sign with $| f ( s _ { j } ) - r ( s _ { j } ) | \geq$ $\varepsilon$ for some $\varepsilon > 0$ , where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ . Show that the best approximation $r ^ { * } \in \mathcal { R } _ { m n } ^ { \mathrm { r e a l } }$ satisfies $\| \boldsymbol { f } - \boldsymbol { r } ^ { * } \| \ge \varepsilon$ . (Compare Exercise 10.3.)

Exercise 24.6. A rational lethargy theorem. Let $\left\{ \varepsilon _ { n } \right\}$ be a sequence decreasing monotonically to 0. Adapt the proof of Exercise 10.7 to show that there is a function $f \in C ( [ - 1 , 1 ] )$ such that $\| f - r _ { n n } ^ { * } \| \geq \varepsilon { n }$ for all $_ n$ .

Exercise 24.7. Approximation of $e ^ { z }$ . Equation (10.2) gave an asymptotic formula for the accuracy of polynomial best approximations to $e ^ { z }$ on $[ - 1 , 1 ]$ . The generalization to rational best approximations is

$$
E _ { m n } \sim \frac { m ! n ! } { 2 ^ { m + n } ( m + n ) ! ( m + n + 1 ) ! } , \quad m + n \to \infty
$$

(conjectured by Meinardus [1967], proved by Braess [1984]). Produce a table of numerically computed best approximation errors for $0 \leq m + n \leq 1 2$ . How well do these numbers match the asymptotic formula?

# Chapter 25. Two Famous Problems

In this chapter we discuss two problems of rational approximation that have been the focus of special attention over the years: approximation of $| x |$ on $[ - 1 , 1 ]$ , a prototype of approximation of nonsmooth functions, and approximation of $e ^ { x }$ on $( - \infty , 0 ]$ , a prototype of approximation on unbounded domains. Both stories go back many decades and feature initial theorems, later conjectures based on numerical experiments, and eventual proofs of the conjectures based on mathematical methods related to potential theory. We shall not present the proofs of the sharpest results, but we shall show that the essential rates of approximation can be achieved by using the trick that appears several times in this book: if a function $f ( x )$ can be written as an integral with respect to a variable $s$ , then an approximation $r ( x )$ in partial fractions form is obtained by applying a quadrature formula (19.3) to the integral.

The problem of approximation of $| x |$ on $[ - 1 , 1 ]$ originates at the beginning of the 20th century, when polynomial approximations of this function were of interest to Lebesgue, de la Vall´ee Poussin, Jackson, and Bernstein (Exercise 6.5). This was an era when the fundamental results of approximability were being developed, and $| x |$ served as a function from which many other results could be derived. Bernstein’s prize-winning article on the subject ran for 104 pages [1912b] and was followed by another of 57 pages [1914b]. Among other things, Bernstein proved that in best polynomial approximation of $| x |$ as $n  \infty$ , the errors decrease linearly but no faster, that is, at the rate $O ( n ^ { - 1 } )$ but not $o ( n ^ { - 1 } )$ .

Why linearly? This is an example of the fundamental principle mentioned first in Chapter 7: the close connection between the smoothness of a function and its rate of approximation. The function $f ( x ) = | x |$ has a derivative of bounded variation $V = 2$ on $[ - 1 , 1 ]$ , so by Theorem 7.2, its Chebyshev projections $\{ f _ { n } \}$ satisfy

$$
\| f - f _ { n } \| \leq { \frac { 4 } { \pi ( n - 1 ) } }
$$

for $n \geq 2$ , and its Chebyshev interpolants $\left\{ p _ { n } \right\}$ satisfy the same bound with 4 replaced by 8. Thus approximations to $| x |$ converge at least at the rate $O ( n ^ { - 1 } )$ . What Bernstein showed is that the rate is in fact no better than this: no approximations to $| x |$ can beat Chebyshev projection or interpolation by more than a constant factor. Or to put it another way, convergence of polynomial approximants to a function $f$ at a rate faster than $O ( n ^ { - 1 } )$ implies that $f$ is in some sense smoother than $| x |$ . Such results in the direction approximability $\Longrightarrow$ smoothness go by the general name of Bernstein theorems. In this book we have presented one result of this kind, Theorem 8.3, asserting that geometric convergence implies analyticity.

It is hard not to be curious about the constants. Bernstein in fact proved in [Bernstein 1914b] that there exists a number $\beta$ such that the best approximation errors satisfy

$$
E _ { n } ( | x | ) \sim { \frac { \beta } { n } }
$$

as $n \to \infty$ , and he obtained the bound

$$
0 . 2 7 8 < \beta < 0 . 2 8 6 .
$$

(Theorem 7.2 gives $\beta \leq 4 / \pi \approx 1 . 2 7 .$ .) He noted as a “curious coincidence” that $1 / 2 \sqrt { \pi } \approx 0 . 2 8 2 0 9 \ldots$ falls in this range, and the idea that $\beta$ might take exactly this value became known as Bernstein’s conjecture. Seventy years later, Varga and Carpenter [1985] investigated the problem numerically to great accuracy and found that in fact

$$
\beta \approx 0 . 2 8 0 1 6 9 4 9 9 0 2 3 8 6 9 1 3 3 0 3 6 4 3 6 4 9 \ldots
$$

(Of course the difference between 0.282 and 0.280 would not have the slightest practical importance.) Along with this numerical result, which was based on Richardson extrapolation, Varga and Carpenter established the rigorous bounds

$$
0 . 2 8 0 1 6 8 5 < \beta < 0 . 2 8 0 1 7 3 4 .
$$

For example, here are the values of $n E _ { n } ( | x | )$ for $n = 1 , 2 , 4 , \dots , 6 4$ , showing quadratic convergence to the limit value. A comparison with the much more accurate Table 2.1 of [Varga & Carpenter 1985] indicates that the Chebfun results are accurate in all but the last digit or two.

$\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ chebfun('x'); f = abs(x); limit $=$ 0.280169499023869133;   
for n = 2.^(0:6) [p,err] $=$ minimax(f,n); fprintf('%14d %16.8f %16.2e\n',n,n\*err,n\*err-limit)   
end

<table><tr><td>n</td><td>n*err</td><td>n*err - limit</td></tr><tr><td>1</td><td>0.50000000</td><td>2.20e-01</td></tr><tr><td>2</td><td>0.25000000</td><td>-3.02e-02</td></tr><tr><td>4</td><td>0.27048360</td><td>-9.69e-03</td></tr><tr><td>8</td><td>0.27751782</td><td>-2.65e-03</td></tr><tr><td>16</td><td>0.27948884</td><td>-6.81e-04</td></tr><tr><td>32</td><td>0.27999815</td><td>-1.71e-04</td></tr><tr><td>64</td><td>0.28012659</td><td>-4.29e-05</td></tr></table>

Now all this is for polynomial approximation. What about rational functions? As mentioned in Chapter 23, the dramatic discovery here came from Donald Newman, 50 years after Bernstein: best rational approximants to $| x |$ converge “rootexponentially.” Newman’s bounds were these:

$$
\frac { 1 } { 2 } e ^ { - 9 \sqrt { n } } \leq E _ { n n } ( | x | ) \leq 3 e ^ { - \sqrt { n } } .
$$

We have already seen in the second plot of Chapter 23 what an improvement in convergence rate this is as compared with (25.1). For approximating nonsmooth functions, rational functions can be far more powerful than polynomials.

Again mathematicians could not resist trying to sharpen the constants. First, Vyacheslavov [1975] found that the exact exponent is midway between Newman’s bounds of 1 and 9: it is $\pi$ . Then Varga, Ruttan, and Carpenter [1993] performed computations with a version of the Remez algorithm to 200 decimal places, leading to numerical evidence for the conjecture

$$
E _ { n n } \sim 8 e ^ { - \pi { \sqrt { n } } }
$$

as $n  \infty$ . Soon afterward this result was proved by Stahl [1993]. Later Stahl generalized the result to approximation of $x ^ { \alpha }$ on $[ 0 , 1 ]$ for any $\alpha > 0$ [Stahl 2003].

The following theorem summarizes the results we have mentioned.

Theorem 25.1. Approximation of $| x |$ on $[ - 1 , \bf 1 ]$ . The errors in best polynomial and rational approximation of $| x |$ on $[ - 1 , 1 ]$ satisfy as $n \to \infty$

$$
E _ { n 0 } ( | x | ) \sim \frac { \beta } { n } , \quad \beta = 0 . 2 8 0 1 \ldots ,
$$

and

$$
E _ { n n } ( \vert x \vert ) \sim 8 e ^ { - \pi { \sqrt { n } } } .
$$

Proof. Equation (25.4) is due to Varga and Carpenter [1985], and (25.5) is due to Stahl [1993].

Why can rational approximations of $| x |$ achieve $O ( C ^ { - \sqrt { n } } )$ accuracy? The crucial fact is that the poles of $r$ can be chosen to cluster near the singular point $x = 0$ . In particular, a good choice is to make the poles approach 0 geometrically, for each fixed $n$ , with a geometric factor depending on $\sqrt { n }$ .

Here is a derivation of a rational approximation that achieves the right rootexponential convergence. (Arguments like this have been made by Stenger in various publications; see, for example, [Stenger 1986].) We start from the identity

$$
\frac { 1 } { | x | } = \frac { 2 } { \pi } \int _ { 0 } ^ { \infty } \frac { d t } { t ^ { 2 } + x ^ { 2 } } ,
$$

which is derived in calculus courses. Multiplying by $x ^ { 2 }$ gives

$$
| x | = { \frac { 2 x ^ { 2 } } { \pi } } \int _ { 0 } ^ { \infty } { \frac { d t } { t ^ { 2 } + x ^ { 2 } } } .
$$


<!-- chunk 0004: pages 211-280 -->
(This formula is perhaps due to Roberts [1980], though the essence of the matter dates to Zolotarev in the 1870s.) The change of variables $t = e ^ { s }$ , $d t = e ^ { s } d s$ converts this to

$$
| x | = \frac { 2 x ^ { 2 } } { \pi } \int _ { - \infty } ^ { \infty } \frac { e ^ { s } d s } { e ^ { 2 s } + x ^ { 2 } } ,
$$

which is an attractive integral to work with because the integrand decays exponentially as $| s | \to \infty$ . We now get a rational approximation of $| x |$ by approximating this integral by the trapezoidal rule with node spacing $h > 0$ :

$$
r ( x ) = \frac { 2 h x ^ { 2 } } { \pi } \sum _ { k = - ( n - 2 ) / 4 } ^ { ( n - 2 ) / 4 } \frac { e ^ { k h } } { e ^ { 2 k h } + x ^ { 2 } } .
$$

Here $n$ is a positive even number, and there are $n / 2$ terms in the sum, so $r ( x )$ is a rational function of $x$ of type $( n , n )$ . There are two sources of error that make $r ( x )$ differ from $| x |$ . The fact that the sum has been terminated at a limit $n < \infty$ introduces an error on the order of $e ^ { - n h / 4 }$ , and the finite step size $h > 0$ introduces an error on the order of $e ^ { - \pi ^ { 2 } / h }$ . (The integrand is analytic in the strip around the real $s$ -axis of half-width $a = \pi / 2$ , corresponding to a convergence rate $e ^ { - 2 \pi a / h }$ .) Balancing these sources of error suggests the condition $e ^ { - n h / 4 } \approx e ^ { - \pi ^ { 2 } / h }$ , that is,

$$
h \approx 2 \pi / { \sqrt { n } } ,
$$

with error of order

$$
e ^ { - ( \pi / 2 ) { \sqrt { n } } } .
$$

We can see these approximations with an experiment.

$$
\mathrm { ~ \bf ~ r ~ } = \mathrm { ~ \bf ~ r ~ } + \mathrm { ~ \bf ~ e x p } ( \mathrm { k } * \mathrm { h } ) / ( \mathrm { e x p } ( 2 * \mathrm { k } * \mathrm { h } ) + \mathrm { \bf x } ^ { \sim } 2 ) ;
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/cb2cc26b80ce5a52caaed3b5c6470377411b761de70ff44511665e1fddcc7b45.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/becf66a58b9e5c05e1a7583a0cfa870af25b853b965c729413383fe622ae605f.jpg)

The poles of (25.7)–(25.8) in the $x$ -plane lie at

$$
\pm i e ^ { 2 \pi k / { \sqrt { n } } } .
$$

Here are these numbers (those in the upper half-plane) for the six approximations plotted above, showing the wide range of amplitudes associated with the exponential spacing.

for $\texttt { n } = \texttt { 2 } : 2 : 1 2$ $\mathrm { ~ h ~ = ~ 2 ^ { * } p i / s q r t { ( n ) } ; ~ k ~ = ~ - { ( n - 2 ) / 4 } : { ( n - 2 ) / 4 } ; ~ y ~ = ~ \exp { ( k * h ) } ~ ; }$ fprintf('%8.2ei ',y)   
end   
Poles of rational approximants to |x|:   
$1 . 0 0 \mathsf { e } ^ { + 0 0 \dot { 1 } }$   
2.08e-01i 4.81e+00i   
7.69e-02i 1.00e+00i 1.30e+01i   
3.57e-02i 3.29e-01i 3.04e+00i 2.80e+01i   
1.88e-02i 1.37e-01i 1.00e+00i 7.29e+00i 5.32e+01i   
1.07e-02i 6.58e-02i 4.04e-01i 2.48e+00i 1.52e+01i 9.32e+01i

The approximations aren’t optimal, but they are close. The convergence rate (25.10) as $n \to \infty$ is one-quarter of the optimal rate (25.5) in the sense that we need 4 times as large a value of $n$ to achieve a certain accuracy in (25.10) as in (25.5).

Above, we computed errors for best polynomial approximations to $| x |$ with the Chebfun command minimax. In the rational case, minimax does not succeed in computing best approximations beyond a certain low order. This difficulty is related to the exponential spacing of the oscillations of $f - r ^ { * }$ near $x = 0$ .

It is worth noting that the problem of approximating $| x |$ on $[ - 1 , 1 ]$ is equivalent to certain other approximation problems. If $r ( x )$ is a type $( m , n )$ approximation to $| x |$ on $[ - 1 , 1 ]$ , then normally $r$ will be an even function of $x$ and $m$ and $n$ can be taken to be even too. Thus $r ( x ) = \tilde { r } ( x ^ { 2 } )$ , where $\tilde { r }$ is a rational function of type $( m / 2 , n / 2 )$ . Since $\tilde { r } ( x ^ { 2 } )$ approximates $| x |$ for $x \in [ - 1 , 1 ]$ , $\tilde { r } ( x )$ approximates $\sqrt { x }$ for $x \in [ 0 , 1 ]$ . This reasoning holds for any approximations, and in particular, by counting equioscillations one finds that best type $( m , n )$ approximation of $| x |$ o n $[ - 1 , 1 ]$ is equivalent to best type $( m / 2 , n / 2 )$ approximation of $\sqrt { x }$ on $[ 0 , 1 ]$ . The following pair of plots illustrates this equivalence. Notice that the error curves are the same apart from the scaling of the $x$ -axis.

f = abs(x); [p,q,rh,err] = minimax(f,2,2);   
subplot(1,2,1), plot(f-p/q), hold on   
plot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k') f $=$ chebfun('sqrt(x)',[0,1],'splitting','on');   
[p,q,rh,err] $=$ minimax(f,1,1);   
subplot(1,2,2), plot(f-p/q), hold on   
plot([-.03 1],err\*[1 1],'--k'), plot([0 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a53178e113481cdc5cff0f9fd61f90f98fd58b1541b27f4ec150fa914301216f.jpg)

For applications in scientific computing, the approximation of $\sqrt { x }$ on an interval $[ a , b ]$ is particularly interesting because of the case in which $x$ is a matrix $A$ with eigenvalues in $[ a , b ]$ , which might come from discretizing a differential operator. Rational approximations of the square root lead to powerful algorithms for evaluating $A ^ { 1 / 2 } v$ for vectors $v$ , as described in [Hale, Higham & Trefethen 2008] and [Higham 2008]. At the other end of the historical spectrum, approximation of square roots was the problem addressed by Poncelet in the very first paper on minimax approximation [Poncelet 1835].

We now turn to the second of the famous problems of this chapter: approximation of $e ^ { x }$ on $( - \infty , 0 ]$ . This problem was introduced in a paper of Cody, Meinardus, and Varga [1969], which drew attention to the connection of such approximations with the numerical solution of PDEs, since a rational approximation can be used to compute the exponential of a matrix arising from a numerical discretization [Moler $\&$ Van Loan 2003].13 Curiously, despite that good motivation from applied mathematics, the influence of this paper was mainly in theoretical approximation theory for quite a few decades, until computers and numerical linear algebra had advanced to the point where it became more practical to take advantage of algorithms based on rational functions.

The first thing we may note about approximation of $e ^ { x }$ on $( - \infty , 0 ]$ is that polynomials cannot do the job at all. Since any nonconstant polynomial $p ( x )$ diverges to $\pm \infty$ as $x \to - \infty$ , the only polynomials that can approximate $e ^ { x }$ with finite error on $( - \infty , 0 ]$ are constants, so the minimax error can never be less than $1 / 2$ .

Inverse-polynomials of the form $1 / p _ { n } ( x )$ , however, can be chosen to converge geometrically. This makes sense when you consider that $e ^ { x }$ on $( - \infty , 0 ]$ is the same as $1 / e ^ { x }$ for $x \in [ 0 , \infty )$ . Cody, Meinardus, and Varga noted that to achieve geometric convergence, it is enough to consider $1 / p _ { n } ( x )$ , where $p _ { n }$ is the degree $n$ truncation of the Taylor series for $e ^ { x }$ . They showed that these approximations converge at a rate $O ( 2 ^ { - n } )$ , and then they improved this rate to $O ( 2 . 2 9 8 ^ { - n } )$ by a shift of origin. It was later proved by Sch¨onhage [1973] that the optimal rate for inverse-polynomials is $O ( 3 ^ { - n } )$ .

Since $1 / p _ { n } ( x )$ is a rational function of type $( n , n )$ , these observations tell us that best rational type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ converge at least geometrically. Newman [1974] proved that the convergence is no faster than geometric. What is the optimal rate? With twice as many parameters to work with as with inverse-polynomials, one might guess that it should be $O ( 9 ^ { - n } )$ , and this idea became known in the 1970s as the $1 / 9$ conjecture. In fact, the optimal convergence rate turned out to be $O ( H ^ { n } )$ with $H \approx 1 / 9 . 2 8 9 0 3$ , a number now known as Halphen’s constant, equal to the unique positive root of the equation

$$
h ( s ) = \sum _ { k = 1 } ^ { \infty } { \frac { k s ^ { n } } { 1 - ( - s ) ^ { n } } } = { \frac { 1 } { 8 } } .
$$

This number was conjectured numerically based on Carath´eodory–Fej´er singular values by Trefethen and Gutknecht [1983b], verified to many digits by high-precision Remez algorithms by Carpenter, Ruttan, and Varga [1984], conjectured to have the exact value associated with a certain problem of elliptic functions treated by Halphen [1886] by Magnus via the Carath´eodory–Fej´er method [Magnus 1985, Magnus & Meinguet 2000], and then proved using quite different methods of potential theory by Gonchar and Rakhmanov [1989]. This work represents a fascinating and important line of investigation in approximation theory, and for a summary of many of the ideas with wide generalizations to related problems, a good place to start is [Stahl & Schmelzer 2009]. A presentation of the potential theory underlying results in this area can be found in [Saff & Totik 1997].

Following the idea presented earlier for $| x |$ on $[ - 1 , 1 ]$ , it is interesting to see what can be achieved for this problem by the trapezoidal rule approximation of a contour integral. Here is a derivation of a rational approximation that achieves the rate $O ( ( 2 . 8 4 9 \dots . . . ) ^ { - n } )$ , adapted from [Weideman $\&$ Trefethen 2007b]; such approximations are discussed more generally in [Trefethen, Weideman $\&$ Schmelzer 2006]. We begin with a Laplace transform identity that is easily proved by residue calculus,

$$
e ^ { x } = \frac { 1 } { 2 \pi i } \int \frac { e ^ { t } d t } { t - x }
$$

for $x \in ( - \infty , 0 ]$ , where the integral is over any contour in the complex plane that starts at $- \infty$ below the $t$ -axis, circles around $t = 0$ , and finishes at $- \infty$ above the $t$ -axis. Choosing the contour to be a parabola, we convert this to an integral over the real $s$ -axis by the change of variables

$$
t = ( i s + a ) ^ { 2 } , \quad d t = 2 i ( i s + a ) d s
$$

for some constant $a > 0$ , which gives

$$
e ^ { x } = \frac { 1 } { \pi } \int _ { - \infty } ^ { \infty } \frac { e ^ { ( i s + a ) ^ { 2 } } ( i s + a ) d s } { ( i s + a ) ^ { 2 } - x } .
$$

As in (25.8), we now approximate this integral by the trapezoidal rule with node spacing $h > 0$ :

$$
r ( x ) = \frac { h } { \pi } \sum _ { k = - ( n - 1 ) / 2 } ^ { ( n - 1 ) / 2 } \frac { e ^ { ( i k h + a ) ^ { 2 } } ( i k h + a ) } { ( i k h + a ) ^ { 2 } - x } .
$$

Here $n$ is a positive even number, and since $x$ rather than $x ^ { 2 }$ appears in each term we now take $n$ terms in the sum rather than $n / 2$ as in (25.8) to make $r ( x )$ a rational function of $x$ of type $( n - 1 , n )$ .

This time, the integral has square-exponential rather than just exponential decay as $s  \infty$ , so choosing $h = O ( 1 / { \sqrt { n } } )$ is enough to make the errors from endpoint truncation exponentially small. We also have the parameter $a$ to play with. By taking $a = O ( { \sqrt { n } } )$ , we can make the errors due to grid spacing exponentially small too, and in this fashion we can achieve geometric convergence. More precisely, the choices

$$
a = { \sqrt { \frac { \pi n } { 2 4 } } } , \quad h = { \sqrt { \frac { 3 \pi } { 2 n } } }
$$

lead to the convergence rate

$$
\lVert f - r _ { n n } \rVert = O ( e ^ { - \pi n / 3 } ) \approx O ( ( 2 . 8 4 9 \cdot . . ) ^ { - n } ) .
$$

As before, we can see these approximations with an experiment, this time plotting $f - r$ rather than $r$ itself.

$\mathrm { ~ x ~ } =$ $\begin{array} { r l } & { = \mathrm { \ c h e b f u n } ( ^ { \prime } \mathrm { \ x } ^ { \prime } , [ - 2 , - . 0 1 ] ) ; \mathrm { ~ f ~ = ~ } \exp ( \mathrm { \ x } ) ; } \\ & { \mathrm { \texttt { r n } ~ = ~ } 2 ; 2 \colon 8 } \\ & { \mathrm { \texttt { r } ~ = ~ } 0 * \mathrm { \texttt { x } } ; \mathrm { \texttt { h } ~ = ~ s q r t } ( 3 * \mathrm { p i } / ( 2 * \mathrm { n } ) ) ; \mathrm { \texttt { a } ~ = ~ s q r t } ( \mathrm { p i } * \mathrm { n } / 2 4 ) ; } \\ & { \mathrm { \texttt { f o r ~ k } ~ = ~ } - ( \mathrm { n } - 1 ) / 2 ; ( \mathrm { n } - 1 ) / 2 } \\ & { \mathrm { \texttt { r } ~ = ~ } \mathrm { \texttt { r } ~ + ~ } \exp ( ( 1 \mathrm { i } * \mathrm { k } * \mathrm { h } + \mathrm { a } ) \cdot 2 ) * ( 1 \mathrm { i } * \mathrm { k } * \mathrm { h } + \mathrm { a } ) . / ( ( 1 \mathrm { i } * \mathrm { k } * \mathrm { h } + \mathrm { a } ) \cdot 2 - \mathrm { x } ) ; } \end{array}$ fo   
end   
$\begin{array} { r } { \mathbf { r } ~ = ~ \left( \mathrm { h / p i } \right) { * } \mathrm { r e a l } \left( \mathrm { r } \right) } \end{array}$ ; subplot(2,2,n/2), plot(f-r)   
err $=$ norm(f-r,inf);   
ss $=$ sprintf('(%1d,%1d) error = %7.5f',n,n,err);   
end

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/3e8d41548190afd51e3d6f0652968652ec9e34cbbd699d04204fe73f05ad89df.jpg)

Let us summarize these results with a theorem, which goes further to include the precise leading-order asymptotic behavior of the best approximation errors as conjectured by Magnus [1994] and proved by Aptekarev [2002].

Theorem 25.2. Approximation of $e ^ { \mathbf { x } }$ on $( - \infty , \mathbf { 0 } ]$ . The errors in best type $( 0 , n )$ and $( n , n )$ rational approximation of $\exp ( x )$ on $( - \infty , 0 ]$ satisfy as $n \to \infty$

$$
\operatorname* { l i m } _ { n \to \infty } { E _ { 0 n } ^ { 1 / n } } = \frac { 1 } { 3 }
$$

and

$$
E _ { n n } \sim 2 H ^ { n + 1 / 2 } , ~ H = 1 / 9 . 2 8 9 0 2 5 4 9 1 9 2 0 8 \ldots _ { \cdot \cdot \cdot }
$$

Proof. Equation (25.17) is due to Sch¨onhage [1973] and (25.18) to Aptekarev [2002], extending the earlier result on $_ { n }$ th root asymptotics and the constant $H$ by Gonchar and Rakhmanov [1989].

We finish this chapter by showing that the numerical computation of these best approximants is surprisingly easy. The crucial matter is to note that the change of variables

$$
x = a \frac { s - 1 } { s + 1 } , \qquad s = \frac { a + x } { a - x } ,
$$

where $a$ is a positive parameter, maps the negative real axis $( - \infty , 0 ]$ in $x$ to the interval $( - 1 , 1 ]$ in $s$ . Since the mapping is a rational function of type $( 1 , 1 )$ , it transplants a rational function of type $( n , n )$ in $s$ or $x$ to a rational function of type $( n , n )$ in the other variable. In particular, for the approximation of $f ( x ) = e ^ { x }$ o n $( - \infty , 0 ]$ , let us define

$$
F ( s ) = e ^ { a ( s - 1 ) / ( s + 1 ) } , \quad s \in ( - 1 , 1 ] .
$$

A good choice of the parameter is $a ~ = ~ 9$ , which has a big effect for numerical computation in improving the conditioning of the approximation problem. We now find we have a function that can be approximated to machine precision by a Chebyshev interpolating polynomial $p ( s )$ of degree less than 50:

ans $=$ 47

The Chebyshev series of $F$ decreases at a good exponential rate:

plotcoeffs(F)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/51a7bceac042511ae0e9b7e05af9f6ac74389ce54a1ecede84ecbd6ca3ad4a6f.jpg)

This gives us yet another way to compute rational approximations to $e ^ { x }$ on $( - \infty , 0 ]$ : truncate this Chebyshev series in $s$ , and then transplant by (25.19) to get rational functions in $x$ .

Alternatively, we can get true best approximations from (25.19) by applying the Chebfun minimax command. Here, for example, is the error for the best approximation of type $( 8 , 8 )$ plotted in the $s$ variable, showing 18 points of equioscillation.

[P,Q,RH,err] $=$ minimax(F,8,8); $\mathtt { R } \ = \ \mathtt { P } / \mathtt { Q }$ ; plot(F-R), hold onplot([-1 1],err\*[1 1],'--k'), plot([-1 1],-err\*[1 1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/19010920f0ecc626278b032a01e08552bb2f555b4da4b13e4b32bce56754a27f.jpg)

If we plot the same curve in the $x$ variable, it’s hard to see much because of the varying scale:

${ \bf s } 1 ~ = ~ - . 9 9 9$ ; s2 = .999; s = chebfun('s',[s1 s2]); $\textbf { x } = ~ 9 * \left( \mathbf { s } \mathbf { - } 1 \right) / \left( \mathbf { s } + 1 \right)$ ; plot(x,F{s1,s2}-R{s1,s2}), hold on $\bf { x } \bf { x } ~ = ~ [ - 1 e 4 ~ - 1 e - 2 ]$ ; plot(xx,err\*[1,1],'--k') plot(xx,-err\*[1,1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/f15b47e1106e1e775122ce5d66eb94578ba89660daed32b24abb34e65c922e0c.jpg)

Putting the $x$ -axis on a log scale, however, makes the plot informative again:

semilogx(x,F{s1,s2}-R{s1,s2}), hold on semilogx(xx,err\*[1,1],'--k'), plot(xx,-err\*[1,1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/bb34a2dee411d4a350616e3d4bc53e5a10171dd4c0b7141577f260b91cea6342.jpg)

Here is the analogous plot for type (12, 12) approximation:

[P,Q,RH,err] $=$ minimax(F,12,12); $\mathtt { R } \ = \ \mathtt { P } . / \mathtt { Q }$ ;$\mathbf { s e m i l o g x } ( \mathbf { x } , \mathbf { F } \{ \mathbf { s } 1 , \mathbf { s } 2 \} - \mathbb { R } \{ \mathbf { s } 1 , \mathbf { s } 2 \} )$ , hold onplot(xx,err\*[1,1],'--k'), plot(xx,-err\*[1,1],'--k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/f38b49fe9b0b8ca55739285215fc25a6be46e8ebb86ca2d216306184305efbf7.jpg)

These plots are modeled after [Trefethen, Weideman & Schmelzer 2006], where it is shown that Carath´eodory–Fej´er approximation is equally effective and even faster than the Remez algorithm at computing these approximations.

Summary of Chapter 25. Two problems involving rational functions have attracted special attention, highlighting the power of rational approximations near singularities and on unbounded domains. For approximating $| x |$ on $[ - 1 , 1 ]$ , best rational functions converge root-exponentially, whereas polynomials converge linearly. For approximating $e ^ { x }$ on $( - \infty , 0 ]$ , best rational functions converge geometrically, whereas polynomials do not converge at all. Both rates of approximation can be achieved by constructing partial fractions from trapezoidal rule approximations to certain integrals.

Exercise 25.1. Newton iteration for $| { \pmb x } |$ . (This problem has roots in [Roberts 1980].) (a) Let $_ x$ be a number, and suppose we want to solve the equation $r ^ { 2 } = x ^ { 2 }$ for the unknown $r$ using Newton iteration. Show that the iteration formula is $r ^ { ( k + 1 ) } = ( ( r ^ { ( k ) } ) ^ { 2 } +$ $x ^ { 2 } ) / 2 r ^ { ( k ) }$ . (b) If the initial guess is $r ^ { ( 0 ) } = 1$ , then for $k \geq 1$ , what is the smallest $_ n$ for which the rational function $r ^ { ( k ) } ( x )$ is of type $( n , n )$ ? (c) Use Chebfun to compute and plot the approximations $r ^ { ( 0 ) } ( x ) , \ldots , r ^ { ( 5 ) } ( x )$ on the interval $[ - 1 , 1 ]$ . What is the sup-norm error $\| | x | - r ^ { ( k ) } ( x ) \|$ , and where is it attained? (d) What rate of convergence does this correspond to for $\| | x | - r ^ { ( k ) } ( x ) \|$ as a function of $n$ ? How does this compare with the optimal rate given by Theorem 25.1? (e) Make a semilog plot of $| | x | - r ^ { ( 5 ) } ( x ) |$ as a function of $x \in [ - 1 , 1 ]$ and comment further on the nature of these rational approximations.

Exercise 25.2. An elementary approximant for $e ^ { \alpha }$ on $( - \infty , \mathbf { 0 } ]$ . (a) A degree $n$ polynomial $p ( s )$ on $[ - 1 , 1 ]$ can be transplanted to a type $( n , n )$ rational function $r ( x )$ on $( - \infty , 0 ]$ by the map (25.19). Combine this observation with Theorem 8.2 to show that type $( n , n )$ approximants to $e ^ { x }$ on $( - \infty , 0 ]$ exist with accuracy $O ( \exp ( - C n ^ { - 2 / 3 } ) )$ . (b) How does the $n ^ { - 2 / 3 }$ prediction match the data in the curve after (25.20)?

Exercise 25.3. Computing Halphen’s constant. Write a short Chebfun program that computes Halphen’s constant to 10 or more digits based on the condition (25.12).

Exercise 25.4. Best approximation errors for $e ^ { \alpha }$ . (a) Using minimax and the change of variables (25.20), compute best approximation errors in type $( n , n )$ approximation of $e ^ { x }$ on $( - \infty , 0 ]$ for $n = 0 , 1 , \ldots , 1 3$ . Plot the results on a log scale and compare them with estimates from the asymptotic formula (25.18). Also on a log scale, plot the difference between the estimates and the true errors, and comment on the results. (b) Repeat the computation with CF instead of minimax. This time, plot the difference between the CF and true errors on a log scale, and comment on the results.

Exercise 25.5. Behavior of approximants of $| { \pmb x } |$ in the complex plane. It is shown in [Blatt, Iserles & Saff 1987] that the type $( n , n )$ best approximants to $| x |$ on $[ - 1 , 1 ]$ have all their zeros and poles on the imaginary axis and converge to $_ x$ for $\operatorname { R e } ( x ) > 0$ and to $- x$ for $\mathrm { R e } ( x ) < 0$ as $n \to \infty$ . Verify this result numerically by plotting $| x - r _ { n n } ^ { * } ( x ) |$ against $\mathrm { R e } ( x )$ for $x \in [ - 1 + 0 . 5 i , 1 + 0 . 5 i ]$ for $n = 1 , 2 , 3 , 4$ .

Exercise 25.6. Behavior of approximants of $e ^ { \alpha }$ in the complex plane. It is stated in [Stahl & Schmelzer 2009] that the poles of best type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ move off to $\infty$ as $n \to \infty$ , and the convergence at $n$ th-root rate governed by $H \approx 1 / 9 . 2 8 9 0 3$ applies on any compact set in the complex plane. With this result in mind, produce contour plots in the complex $z$ -plane for the errors $\displaystyle | e ^ { z } - r _ { n n } ( z ) |$ for the approximations (25.14)–(25.15) with $n = 2 , 4 , 6 , 8 , 1 0$ . Does it appear likely that these approximations too converge on all compact sets in the plane?

# Chapter 26. Rational Interpolation and Linearized Least-Squares

For polynomials, we have emphasized that although best approximations with their equioscillating error curves are fascinating, Chebyshev interpolants or projections are just as good for most applications and simpler to compute since the problem is linear. To some degree at least, the same is true of rational functions. Best rational approximations are fascinating, but for practical purposes, it is often a better idea to use rational interpolants, and again an important part of the problem is linear since one can multiply through by the denominator.

But there is a big difference. Rational interpolation problems are not entirely linear, and unlike polynomial interpolation problems, they suffer from both nonexistence and discontinuous dependence on data in some settings. To use rational interpolants effectively, one must formulate the problem in a way that minimizes such effects. The method we shall recommend for this, here and in the next two chapters, makes use of the singular value decomposition (SVD) and the generalization of the linearized interpolation problem to one of least-squares fitting. This approach originates in [Pach´on, Gonnet & Van Deun 2012] and [Gonnet, Pach´on $\&$ Trefethen 2011]. The literature of rational interpolation goes back to Cauchy [1821] and Jacobi [1846], but much of it is rather far from computational practice.

Here is an example to illustrate the difficulties. Suppose we seek a rational function $r \in \mathcal { R } _ { 1 1 }$ satisfying the conditions

$$
r ( - 1 ) = 2 , \quad r ( 0 ) = 1 , \quad r ( 1 ) = 2 .
$$

Since a function in $\mathcal { R } _ { 1 1 }$ is determined by three parameters, the count appears right for this problem to be solvable. In fact, however, there is no solution, and one can prove this by showing that if a function in $\mathcal { R } _ { 1 1 }$ takes equal values at two points,

it must be a constant (Exercise 26.1). We conclude that solutions to seemingly sensible rational interpolation problems do not always exist.

Let us modify the problem and seek a function $r \in \mathcal { R } _ { 1 1 }$ satisfying the conditions

$$
r ( - 1 ) = 1 + \varepsilon , \quad r ( 0 ) = 1 , \quad r ( 1 ) = 1 + 2 \varepsilon ,
$$

where $\varepsilon$ is a parameter. Now there is a solution for any $\varepsilon$ , namely

$$
r ( x ) = 1 + \frac { \frac { 4 } { 3 } \varepsilon x } { x - \frac { 1 } { 3 } } .
$$

However, this is not quite the smooth interpolant one might have hoped for. Here is the picture for $\varepsilon = 0 . 1$ :

$$
\begin{array} { l } { \mathrm {  ~ x ~ = ~ c h e b f u n ( \bar { ~ } x ^ { \prime } ) ~ } ; \mathrm {  ~ r ~ = ~ } \emptyset \left( \mathrm { e p } \right) \mathrm {  ~ 1 ~ } + \mathrm {  ~ \left( 4 / 3 \right) } { * \mathrm { e p } ^ { * } \mathrm { x } } / \left( \mathrm { x } - \left( \mathrm { 1 / 3 } \right) \right) ; } \\ { \mathrm { e p } = \mathrm {  ~ 0 ~ } . 1 ; \mathrm {  ~ p l o t } \left( \mathrm { r \left( e p \right) } \right) , \mathrm { \ h o l d ~ o n ~ } } \\ { \mathrm { p l o t } \mathrm {  ~ ( } \mathrm { [ - 1 ~ } \mathrm {  ~ 0 ~ } \mathrm {  ~ 1 ] ~ } , \mathrm { \mathrm { [ 1 + e p ~ 1 ~ } ~ 1 + 2 * \mathrm { e p ] ~ } , \mathrm {  ~ \cdot ~ } } . \mathrm { k } ^ { \prime } \mathrm {  ~ ) } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a922a6a33d1513ea97ca77179498ae0ea8d3af9c3f468ab44336e55886904154.jpg)

And here it is for $\varepsilon = 0 . 0 0 1$ :

$\mathtt { e p } \ = \ 0 . 0 0 1$ ; plot(r(ep)), hold on plot([-1 0 1],[1+ep 1 1+2\*ep],'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/14fcd2d1f524126e58fc09f801506da302bdcb986693054316d462fa9f43d8ca.jpg)

Looking back at the formula (26.3), we see that for any nonzero value of $\varepsilon$ , this function has a pole at $x = 1 / 3$ . When $\varepsilon$ is small, the effect of the pole is quite localized, and we may confirm this by calculating that the residue is $( 4 / 9 ) \varepsilon$ . Another way to interpret the local effect of the pole is to note that $r$ has a zero at a distance just $O ( \varepsilon )$ from the pole:

$$
\begin{array} { r } { \mathrm { p o l e : ~ } x = \frac { 1 } { 3 } , \qquad \mathrm { z e r o : ~ } x = \frac { 1 } { 3 } / ( 1 + \frac { 4 } { 3 } \varepsilon ) . } \end{array}
$$

For $| x - { \textstyle \frac { 1 } { 3 } } | \gg \varepsilon$ , the pole and the zero will effectively cancel. This example shows that even when a rational interpolation problem has a unique solution, the problem may be ill-posed in the sense that the solution depends discontinuously on the data. For $\varepsilon = 0$ , (26.3) reduces to the constant $r = 1$ , whereas for any nonzero $\varepsilon$ there is a pole, though it seems to have little to do with approximating the data. Such poles are often called spurious poles. Since a spurious pole is typically associated with a nearby zero that approximately cancels its effect further away, another term is Froissart doublet, named after the physicist Marcel Froissart [Froissart 1969]. We may also say that the function has a spurious pole-zero pair.

Here is an example somewhat closer to practical approximation. Consider the function $f ( x ) = \cos ( e ^ { x } )$ ,

and suppose we want to construct rational interpolants of type $( n , n )$ to $f$ based on samples at $2 n + 1$ Chebyshev points in $[ - 1 , 1 ]$ . Chebfun has a command ratinterp that will do this, and here is a table of the maximum errors obtained by ratinterp for $n = 1 , 2 , \ldots , 6$ :

for $\mathrm { ~ n ~ } = \mathrm { ~ 1 { : } ~ 6 ~ }$

$\begin{array} { l } { { \mathrm { [ p , q ] ~ = ~ r a t i n t e r p ( f , n , n ) ; ~ e r r ~ = ~ n o r m ( f \mathrm { - } p / q , i n f ) ; } } } \\ { { \mathrm { f p r i n t f ( \mathrm { ' } \phantom { n } ( \% 1 { \mathrm { d } } , \% 1 d ) ~ \% 7 . 2 e \setminus n \mathrm { " } , n , n , e r r ) } } } \end{array}$ end

We seem to have very fast convergence, but what has gone wrong with the type $( 3 , 3 )$ approximant? A plot reveals that the problem is a spurious pole:

[p,q] = ratinterp(f,3,3); plot(p/q), hold on xx = chebpts(7); plot(xx,f(xx),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/6106bef17cdb2ef9e4ddc7b1c1fa17ba59233a3d0c78594b0b722f14a9aa8059.jpg)

One might suspect that this artifact has something to do with rounding errors on the computer, but it is not so. The spurious pole is in the mathematics, with residue equal to about $- 0 . 0 0 1 3$ .

In other examples, on the other hand, spurious poles do indeed arise from rounding errors. In fact, they appear very commonly when one aims for approximations with accuracy close to machine precision. Here, for example, is a numerically computed interpolant of type $( 8 , 8 )$ to $e ^ { x }$ in 21 Chebyshev points:

[p,q] = ratinterp(exp(x),8,8,[],[],0); plot(p/q), hold on xx $=$ chebpts(21); plot(xx,exp(xx),'.k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/1b9092b88f30bc9b2a7360d60f3bd92612fab5957831c18369de3f6d6c17311d.jpg)

The picture looks fine, but that is only because Chebfun has failed to detect that $p / q$ has a spurious pole-zero pair:

spurious_zero $=$ roots(p), spurious_pole $=$ roots(q)

spurious_zero $=$ 0.819870673405979   
spurious_pole $=$ 0.819870673405979

One could attempt to get around this particular pathology by computing in higher-precision arithmetic. However, quite apart from the practical difficulties of high-precision arithmetic, that approach would not really address the challenges of rational interpolation at a deeper level. The better response is to adjust the formulation of the rational interpolation problem so as to make it more robust. In this last example, it seems clear that a good algorithm should be sensible enough to reduce the number of computed poles. We now show how this can be done systematically with the SVD.

At this point, we shall change settings. Logically, we would now proceed to develop a robust rational interpolation strategy on $[ - 1 , 1 ]$ . However, that route would require us to combine new ideas related to robustness with the complexities of Chebyshev points, Chebyshev polynomials, and rational barycentric interpolation formulas. Instead, now and for most of the rest of the book, we shall move from the real interval $[ - 1 , 1 ]$ to the unit disk and switch variable names from $x$ to $z$ . This will make the presentation simpler, and it fits with the fact that many applications of rational interpolants and approximants involve complex variables.

Specifically, here is the problem addressed in the remainder of this chapter, following [Pach´on, Gonnet & Van Deun 2012] and [Gonnet, Pach´on & Trefethen 2011] but with origins as far back as Jacobi [1846]. Suppose $f$ is a function defined on the unit circle in the complex plane and we consider its values $f ( z _ { j } )$ at the $( N + 1 ) \mathrm { s t }$ roots of unity for some $N \geq 0$ ,

$$
z _ { j } = e ^ { 2 \pi i j / ( N + 1 ) } , \quad 0 \le j \le N .
$$

Using this information, how can we construct a good approximation $r \in \mathcal { R } _ { m n }$ ? We assume for the moment that $m$ , $n$ , and $N$ are related by $N = m + n$ . The parameter count is then right for an interpolant $r = p / q$ satisfying

$$
\frac { p ( z _ { j } ) } { q ( z _ { j } ) } = f ( z _ { j } ) , \quad 0 \leq j \leq N .
$$

The problem of finding such a function $r$ is known as the Cauchy interpolation problem. As we have seen, however, a solution does not always exist.

Our first step toward greater robustness will be to linearize the problem and seek polynomials $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ such that

$$
p ( z _ { j } ) = f ( z _ { j } ) q ( z _ { j } ) , \quad 0 \leq j \leq N .
$$

By itself, this set of equations isn’t very useful, because it has the trivial solution $p = q = 0$ . Some kind of normalization is needed, and for this we introduce the representations

$$
p ( z ) = \sum _ { k = 0 } ^ { m } a _ { k } z ^ { k } , \qquad q ( z ) = \sum _ { k = 0 } ^ { n } b _ { k } z ^ { k }
$$

with

$$
\mathbf { a } = ( a _ { 0 } , \ldots , a _ { m } ) ^ { T } , \qquad \mathbf { b } = ( b _ { 0 } , \ldots , b _ { n } ) ^ { T } .
$$

Our normalization will be the condition

$$
\| \mathbf { b } \| = 1 ,
$$

where $\| \cdot \|$ is the standard 2-norm on vectors,

$$
\| \mathbf { b } \| = \left( \sum _ { k = 0 } ^ { n } | b _ { k } | ^ { 2 } \right) ^ { 1 / 2 } ,
$$

and similarly for vectors of dimensions other than $n + 1$ . Our linearized rational interpolation problem consists of solving the two equations (26.5)–(26.6). A solution with $q ( z _ { j } ) \neq 0$ for all $j$ will also satisfy (26.4), but if $q ( z _ { j } ) = 0$ for some $j$ , then (26.4) may or may not be satisfied. A point where it is not attained is called an unattainable point.

We turn (26.5)–(26.6) into a matrix problem as follows. Given an arbitrary $( n { + } 1 )$ -vector $\mathbf { b }$ , there is a corresponding polynomial $q \in \mathcal { P } _ { n }$ , which we may evaluate at the $( N + 1 ) \mathrm { { ; } }$ st roots of unity $\{ z _ { j } \}$ . Multiplying by the values $f ( z _ { j } )$ gives a set of $N + 1$ numbers $f ( z _ { j } ) q ( z _ { j } )$ . There is a unique polynomial $\hat { p } \in \mathcal { P } _ { N }$ that interpolates these data,

$$
\begin{array} { r } { \hat { p } ( z _ { j } ) = f ( z _ { j } ) q ( z _ { j } ) , \quad 0 \leq j \leq N . } \end{array}
$$

Let $\hat { p }$ be written as

$$
\hat { p } ( z ) = \sum _ { k = 0 } ^ { N } \hat { a } _ { k } z ^ { k } , \quad \hat { \mathbf { a } } = ( \hat { a } _ { 0 } , \ldots , \hat { a } _ { N } ) ^ { T } .
$$

Then $\hat { \bf a }$ is a linear function of $\mathbf { b }$ , and we may accordingly express it as the product

$$
\hat { \mathbf { a } } = \hat { C } \mathbf { b } ,
$$

where $\hat { C }$ is a rectangular matrix of dimensions $( N + 1 ) \times ( n + 1 )$ depending on $f$ . It can be shown that $\hat { C }$ is a Toeplitz matrix with entries given by the discrete Laurent or Fourier coefficients

$$
c _ { j k } = \frac { 1 } { N + 1 } \sum _ { \ell = 0 } ^ { N } z _ { \ell } ^ { k - j } f ( z _ { \ell } ) .
$$

And now we can solve (26.5)–(26.6). Let $\bar { C }$ be the $n \times ( n + 1 )$ matrix consisting of the last $n$ rows of $\hat { C }$ . Since $\tilde { C }$ has more columns than rows, it has a nontrivial null vector, and for $\mathbf { b }$ we take any such null vector normalized to length 1:

$$
\tilde { C } { \bf b } = 0 , \quad \| { \bf b } \| = 1 .
$$

The corresponding vector $\hat { \mathbf { a } } = \hat { C } \mathbf { b }$ is equal to zero in positions $m + 1$ through $N$ , and we take $\mathbf { a }$ to be the remaining, initial portion of $\hat { \bf a }$ : $a _ { j } = { \hat { a } } _ { j }$ , $0 \leq j \leq m$ . In matrix form we can write this as

$$
\mathbf { a } = C \mathbf { b } ,
$$

where $C$ is the $( m + 1 ) \times ( n + 1 )$ matrix consisting of the first $m + 1$ rows of $\hat { C }$ .   
Equations (26.8)–(26.9) constitute a solution to (26.5)–(26.6).

In a numerical implementation of the algorithm just described, the operations should properly be combined into a MATLAB function, and a function like this called ratdisk is presented in [Gonnet, Pach´on & Trefethen 2011]. Here, however, for the sake of in-line presentation, we shall achieve the necessary effect with a string of anonymous functions.

The first step is to construct the Toeplitz matrix $\hat { C }$ using the MATLAB fft command. The real command below eliminates imaginary parts at the level of rounding errors and would need to be removed for a function $f$ that was not real on the real axis.

$$
\begin{array} { r l } & { \mathrm { \bf ~ f ~ j ~ = ~ \boldsymbol { \mathfrak { Q } } \left( \mathbf { \mathfrak { f } } , \boldsymbol { \mathbb { N } } \right) ~ \ f ~ ( e x p \left( 2 i \ast p \mathbf { i } \ast \left( 0 : \mathbb { N } \right) \cdot \big / \left( \mathbb { N } + 1 \right) \right) ) ~ ; } } \\ & { \mathrm { \bf ~ e x t r a c t ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { A } } , I , \mathbf { J } \right) ~ \ A \left( \mathbf { \bar { I } } , \mathbf { J } \right) ~ ; } } \\ & { \mathrm { \bf ~ c o l u m n ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { f } } , \boldsymbol { \mathbb { N } } \right) ~ \ r e a l \left( \mathbf { \bar { f } } \mathbf { f } \left( \mathbf { f } \left( \mathbf { f } , \mathbb { N } \right) \right) \right) / \left( \mathbb { N } + 1 \right) ~ ; } } \\ & { \mathrm { \bf ~ r o w ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { f } } , \mathbf { n } , \mathbb { N } \right) ~ \ e x t r a c t \left( c o l u m n \left( \mathbf { \bar { f } } , \mathbb { N } \right) ~ , \left[ \mathbf { \bar { \lambda } } \mathbb { N } + 1 : - 1 : \mathbb { N } + 2 - \mathbf { n } \right] ~ , 1 \right) ; } } \\ &  \mathrm { \bf ~ { \boldsymbol ~ C h a t ~ = ~ \boldsymbol { \mathcal { Q } } \left( \mathbf { \mathfrak { f } } , \mathbf { n } , \mathbb { N } \right) ~ \ t o e p \mathbf { \bar { \lambda } } i \ t z \left( c o l u m n \left( \mathbf { \bar { f } } , \mathbb { N } \right) , \mathbf { r o w } \left( \mathbf { \bar { f } } , \mathbf { n } , \mathbb { N } \right) \right) ~ ; } } \end{array}
$$

Next we extract the submatrices $\tilde { C }$ and $C$ :

Ctilde $\mathbf { \delta } = \mathbf { \delta } \otimes ( \mathbf { f _ { \delta } } , \mathbf { m } , \mathbf { n } , \mathbf { N } )$ extract(Chat(f,n,N),m+2:N+1,:);   
$\bar { \mathrm { ~ C ~ } } = \mathrm { ~ \textcircled ~ { ~ 2 ~ } ~ } ( \mathrm { ~ f ~ } , \mathrm { ~ m ~ } , \mathrm { ~ n ~ } , \mathrm { ~ N ~ } )$ extract(Chat(f,n,N),1:m+1,:);

Finally we compute the vector $\mathbf { b }$ using the MATLAB null command, which makes use of the SVD, and multiply by $C$ to get a:

$$
\begin{array} { r l r } & { \mathbf { q } } & { = \ \odot \left( \mathbf { f } \ , \mathtt { m } , \mathbf { n } , \mathtt { N } \right) \ \mathrm { n u l 1 } \left( \mathbf { C t i } 1 \mathrm { d e } \left( \mathbf { f } \ , \mathtt { m } , \mathbf { n } , \mathtt { N } \right) \right) ; } \\ & { \mathbf { p } } & { = \ \odot \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } \right) \ \mathbf { C } \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } \right) * \mathbf { q } \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } \right) ; } \end{array}
$$

For example, here are the coefficients of the type $( 2 , 2 )$ interpolant to $e ^ { z }$ in the 5th roots of unity:

$\textbf { f } = \mathbb { Q } \left( \boldsymbol { z } \right)$ exp(z); ${ \mathfrak { m } } = { \mathfrak { 2 } }$ ; $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ 2 ~ }$ ; N = m+n;   
pp = p(f,m,n,N), qq = q(f,m,n,N)   
pp = -0.893131422200046 -0.446418130422149 -0.074390723603151   
qq $=$ -0.891891822763679 0.446093473426966 -0.074361209330862

The zeros lie in the left half-plane and the poles in the right half-plane (cf. Exercise 18.5):

rzeros $=$ roots(flipud(pp)), rpoles $=$ roots(flipud(qq))   
rzeros $=$ -3.000495954331878 + 1.732909565613550i -3.000495954331878 - 1.732909565613550i   
rpoles $=$ $\mathrm { 2 . 9 9 9 5 0 3 8 9 0 8 1 3 0 2 2 \ + \ 1 . 7 3 1 1 9 1 2 6 0 7 6 7 6 8 4 i }$ 2.999503890813022 - 1.731191260767684i

Here are the values of the interpolant at $z = 0$ and $z = 2$ , which one can see are not too far from $e ^ { 0 }$ and $e ^ { 2 }$ :

$\textbf { r } = \~ \Theta ( z )$ polyval(flipud(pp),z)./polyval(flipud(qq),z);   
approximation $=$ r([0 2]), exact $=$ exp([0 2])   
approximation $=$ 1.001389854021227 7.011719966971134   
exact $=$ 1.000000000000000 7.389056098930650

Now let us take stock. We have derived an algorithm for computing rational interpolants based on the linearized formula (26.5), but we have not yet dealt with spurious poles. Indeed, the solution developed so far has neither uniqueness nor continuous dependence on data. It is time to take our second step toward greater robustness, again relying on the SVD.

An example will illustrate what needs to be done. Suppose that instead of a type $( 2 , 2 )$ interpolant to $e ^ { z }$ in 5 points, we want a type $( 8 , 8 )$ interpolant in 17 points. (This is like the type $( 8 , 8 )$ interpolant computed earlier, but now in roots of unity rather than Chebyshev points.) Here is what we find:

$\mathtt { m \_ s } \mathtt { n \_ n } = 8 ; \mathtt { n \_ w } = 8 ; \mathtt { N \_ m } = \mathtt { m \_ m } + \mathtt { n \_ p p } = \mathtt { p } ( \mathtt { f \_ m } , \mathtt { n } , \mathtt { n } ) , \mathtt { q } \mathtt { q } = \mathtt { q } ( \mathtt { f \_ m } , \mathtt { n } , \mathtt { n } , \mathtt { N } )$   
pp = -0.1447 -0.9818

-1.0170 -0.7967  
-0.4901 -0.2675  
-0.1118 -0.0517  
-0.0155 -0.0065  
-0.0014 -0.0006  
-0.0001 -0.0000  
-0.0000 -0.0000  
-0.0000 -0.0000  
qq =  
-0.1447 -0.9818  
-0.8723 0.1851  
0.4546 0.0383  
-0.1062 -0.0189  
0.0148 0.0033  
-0.0013 -0.0003  
0.0001 0.0000  
-0.0000 -0.0000  
0.0000 0.0000

Instead of the expected vectors a and $\mathbf { b }$ , we have matrices of dimension $9 \times 2$ , and the reason is that $\tilde { C }$ has a nullspace of dimension 2. This would not be true in exact arithmetic, but it is true in 16-digit floating point arithmetic. If we construct an interpolant from one of these vectors, it will have a spurious pole-zero pair. Here is an illustration, showing that the spurious pole (cross) and zero (circle) are near the unit circle, which is typical. The other seven nonspurious poles and zeros have moduli about 10 times larger.

rpoles $=$ roots(flipud(pp(:,1))); rzeros $=$ roots(flipud(qq(:,1))); plot(exp(2i\*pi\*x)), hold on, plot(rpoles,'xk'), plot(rzeros,'or')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/25663588c0e4aa5ac6fa3523a12e349e59e7f04b3d3313e5134364a4ae233645.jpg)

Having identified the problem, we can fix it as follows. If $\bar { C }$ has rank $n - d$ for some $d \geq 1$ , then it has a nullspace of dimension $d + 1$ . (We intentionally use the same letter $d$ as was used to denote the defect in Chapter 24.) There must exist a vector $\mathbf { b }$ in this nullspace whose final $d$ entries are zero. We could do some linear algebra to construct this vector, but a simpler approach is to reduce $m$ and $n$ by $d$ and $N$ by $2 d$ and compute the interpolant again. Here is a function for computing $d$ with the help of the MATLAB rank command, which is based on the SVD. The tolerance $1 0 ^ { - 1 2 }$ ensures that contributions close to machine precision are discarded.

$\mathsf { d } \ = \ \odot ( \mathtt { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } )$ n-rank(Ctilde(f,m,n,N),1e-12);

We redefine q and $\mathtt { p }$ to use this information:

$$
\begin{array} { r l } { \mathbf { q } } & { = \mathbf { \Phi } \odot ( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } ) \mathrm { n u l l } \left( \mathbf { C } \mathbf { t } \mathrm { i } 1 \mathtt { d } \mathbf { e } \left( \mathbf { f } \ , \mathtt { m } \mathrm { - } \mathtt { d } , \mathtt { n } \mathrm { - } \mathtt { d } , \mathtt { N } \mathrm { - } 2 \ast \mathtt { d } \right) \right) ; } \\ { \mathbf { p } } & { = \mathbf { \Phi } \odot ( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } ) \mathbf { C } ( \mathbf { f } \ , \mathtt { m } \mathrm { - } \mathtt { d } , \mathtt { n } \mathrm { - } \mathtt { d } , \mathtt { N } \mathrm { - } 2 \ast \mathtt { d } ) \ast \mathbf { q } \left( \mathbf { f } \ , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } \right) ; } \end{array}
$$

Our example now gives vectors instead of matrices, with no spurious poles.

$$
\begin{array} { r l } & { \mathrm { p p ~ = ~ \ p ( f , m , n , n , d ( f , m , n , n ) ) ~ , ~ } \ q \mathrm { q } = \ q ( \mathbf { f } , \mathtt { m } , \mathtt { n } , \mathtt { N } , \mathtt { d } ( \mathbf { f } , \mathtt { m } , \mathtt { n } , \mathtt { N } ) ) } \end{array}
$$

pp qq  
-0.889761508242969 -0.889761508242815  
-0.444881276259238 0.444880231983654  
-0.101109523962203 -0.101109001824429  
-0.013481293296385 0.013481177243356  
-0.001123443568826 -0.001123429053792  
-0.000056172338563 0.000056171300326  
-0.000001337441819 -0.000001337407096

This type $( 7 , 7 )$ rational function approximates $e ^ { z }$ to approximately machine precision in the unit disk. To verify this loosely, we write a function error that measures the maximum of $| f ( z ) - r ( z ) |$ over 1000 random points in the disk:

$\textbf { r } = \~ \Theta \left( z \right)$ polyval(flipud(pp),z)./polyval(flipud(qq),z); $_ z =$ sqrt(rand(1000,1)).\*exp(2i\*pi\*rand(1000,1)); error $=$ $\mathbf { \Sigma } ( \boldsymbol { \mathfrak { Q } } ( \mathbf { f } , \mathbf { r } )$ norm(f(z)-r(z),inf); error(f,r)

# ans $=$ 7.520010650629788e-13

Mathematically, in exact arithmetic, the trick of reducing $m$ and $n$ by $d$ restores uniqueness and continuous dependence on data, making the rational interpolation problem well-posed. On a computer, we do the same but rely on finite tolerances to remove contributions from singular values close to machine epsilon. A much more careful version of this algorithm can be found in the MATLAB code ratdisk from [Gonnet, Pach´on & Trefethen 2011], mentioned earlier.

We conclude this chapter by taking a third step toward robustness. So far, we have spoken only of interpolation, where the number of data values exactly matches the number of parameters in the fit. In some approximation problems, however, it may be better to have more data than parameters and perform a least-squares fit. This is one of those situations, and in particular, a least-squares formulation will reduce the likelihood of obtaining poles in the region near the unit circle where one is hoping for good approximation. This is why we have included the parameter $N$ throughout the derivation of the last six pages. We will now consider the situation $N > m + n$ . Typical choices for practical applications might be $N = 2 ( m + n )$ or $N = 4 ( m + n )$ .

Given an $( n + 1 )$ -vector $\mathbf { b }$ and corresponding function $q$ , we have already defined $\| \mathbf b \|$ as the usual 2-norm. For the function $q$ , let us now define

$$
\| q \| _ { N } = ( N + 1 ) ^ { - 1 / 2 } \Big ( \sum _ { j = 0 } ^ { N } | q ( z _ { j } ) | ^ { 2 } \Big ) ^ { 1 / 2 } ,
$$

a weighted 2-norm of the values of $q ( z )$ over the unit circle. So long as $N \geq n$ , the two norms are equal:

$$
\| q \| _ { N } = \| \mathbf { b } \| .
$$

The norm $\| \cdot \| _ { N }$ , however, applies to any function, not just a polynomial. In particular, our linearized least-squares rational approximation problem is this generalization of (26.5)–(26.6):

$$
\| p - f q \| _ { N } = \mathrm { { m i n i m u m } , \quad } \| q \| _ { N } = 1 .
$$

The algorithm we have derived for interpolation solves this problem too. What changes is that the matrix $\tilde { C }$ , of dimension $( N - m ) \times ( n + 1 )$ , may no longer have a null vector. If its singular values are $\sigma _ { 1 } \geq \cdot \cdot \cdot \geq \sigma _ { n + 1 } \geq 0$ , then the minimum error will be

$$
\| p - f q \| _ { N } = \sigma _ { n + 1 } ,
$$

which may be positive or zero. If $\sigma _ { n } > \sigma _ { n + 1 }$ , $\mathbf { b }$ is obtained from the corresponding singular vector and that is all there is to it. If

$$
\sigma _ { n - d } > \sigma _ { n - d + 1 } = \cdot \cdot \cdot = \sigma _ { n + 1 }
$$

for some $d \geq 1$ , then the minimum singular space is of dimension $d + 1$ , and as before, we reduce $m$ and $n$ by $d$ . The parameter $N$ can be left unchanged, so $f$ does not need to be evaluated at any new points.

For example, let $f$ be the function $f ( z ) = \log ( 1 . 4 4 - z ^ { 2 } )$ ,

$$
\textbf { f } = \textsf { Q } ( \mathbf { z } ) \ \log \left( 1 . 4 4 \mathbf { - } \mathbf { z } \cdot \mathbf { \hat { \mu } } ^ { - } 2 \right) ;
$$

with branch points at $\pm 1 . 2$ , and suppose we want a type $( 4 0 , 4 0 )$ least-squares approximant with $N = 4 0 0$ . The approximation delivered by the SVD algorithm comes out with exact type (18, 18):

$$
\begin{array} { r l } & { \mathfrak { m } = 4 0 ; \ \mathfrak { n } = 4 0 ; \ \mathbb { N } = 4 0 0 ; } \\ & { \mathrm { p p } = \mathfrak { p } ( \mathbf { f } , \mathfrak { m } , \mathfrak { n } , \mathfrak { N } , \mathsf { d } ( \mathbf { f } , \mathfrak { m } , \mathfrak { n } , \mathbb { N } ) ) ; \ \mathbf { q } \mathbf { q } = \mathbf { q } ( \mathbf { f } , \mathfrak { m } , \mathfrak { n } , \mathbb { N } , \mathsf { d } ( \mathbf { f } , \mathfrak { m } , \mathbf { n } , \mathbb { N } ) ) ; } \\ & { \mathfrak { m } \equiv 1 \mathrm { e n g t h } ( \mathtt { p p } ) - 1 ; \ \mathtt { n u } = \mathbf { \lambda } \mathrm { e n g t h } ( \mathbf { q } \mathbf { q } ) - 1 ; } \\ & { \mathbf { f p r i n t f } ( \mathbf { \lambda } ^ { \prime } \qquad \mathfrak { m u } = \sqrt [ \gamma _ { 0 } ] { \mathsf { d } } \mathbf { \lambda } \qquad \mathtt { n u } = \sqrt [ \gamma _ { 0 } ] { \mathsf { d } } \mathsf { N } ^ { \prime } , \mathtt { m u } , \mathtt { n u } ) } \end{array}
$$

$$
\mathrm { \ m u } \ = \ 1 8 \qquad \mathrm { \ n u } \ = \ 1 8
$$

The accuracy in the unit disk is good (Exercise 26.4):

$\textbf { r } = \textsf { Q } ( \boldsymbol { z } )$ polyval(flipud(pp),z)./polyval(flipud(qq),z); error(f,r)

ans $=$ 6.884478705857767e-12

Here are the poles:

rpoles $=$ roots(flipud(qq)); plot(exp(2i\*pi\*x)), hold on, plot(rpoles+1e-10i,'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/142436d8ae81686bec488fb2dbd84abd731ed2b398484f2e3c8c1f924e3a220a.jpg)

For comparison, suppose we revert to the original definitions of the anonymous functions $\mathrm { \Delta p }$ and q, with no removal of negligible singular values:

$\mathbf { q _ { \lambda } } = \mathbf { \lambda } \otimes ( \mathbf { f _ { \lambda } } , \mathbf { m _ { \lambda } } , \mathbf { n _ { \lambda } } , \mathbf { N } )$ null(Ctilde(f,m,n,N));   
p = @(f,m,n,N) C(f,m,n,N)\*q(f,m,n,N);

Now the computation comes out with exact type $( 4 0 , 4 0 )$ , and half the poles are spurious:

$\mathtt { m } ~ = ~ 4 0$ ; $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ 4 0 ~ }$ ; $\tt { N } = \tt { 4 0 0 }$ ;   
pp = p(f,m,n,N); pp = pp(:,end); qq = q(f,m,n,N); qq = qq(:,end); rpoles $=$ roots(flipud(qq)); hold off, plot(exp(2i\*pi\*x)), hold on plot(rpoles+1e-10i,'.r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/76e29bad9d92b0d67373adc66181e0f71c55da1721c330fdb4b1cabebd163a94.jpg)

The error looks excellent,

$\mathbf { r } ~ = ~ \mathbb { Q } \left( \mathbf { z } \right)$ polyval(flipud(pp),z)./polyval(flipud(qq),z); error(f,r)

ans = 1.632044892792071e-14

but in fact it is not so good. Because of the spurious poles, the maximum error in the unit disk is actually infinite, but this has gone undetected at the 1000 random sample points used by the error command.

In closing this chapter we return for a moment to the variable $x$ on the interval $[ - 1 , 1 ]$ . Earlier we used the Chebfun command ratinterp to compute a type $( 8 , 8 )$ interpolant to $e ^ { x }$ in Chebyshev points and found that it had a spurious pole-zero pair introduced by rounding errors. This computation was one of pure interpolation, with no SVD-related safeguards of the kind described in the last few pages. However, ratinterp is actually designed to incorporate SVD robustness by default.

The earlier computation called ratinterp(exp(x),8,8,[],[],0) in order to force a certain SVD tolerance to be 0 instead of the default $1 0 ^ { - 1 4 }$ . If we repeat the computation with the default robustness turned on, we find that an approximation of exact type $( 8 , 4 )$ is returned and it has no spurious pole and zero:

[p,q,rh,mu,nu] $=$ ratinterp(exp(x),8,8); mu, nu spurious_zero $=$ roots(p), spurious_pole $=$ roots(q)

$\mathtt { m u } \ = \ 8$   
nu = 4   
spurious_zero $=$ Empty matrix: 0-by-1   
spurious_pole $=$ Empty matrix: 0-by-1

Summary of Chapter 26. Generically, there exists a unique type $( m , n )$ rational interpolant through $m + n + 1$ data points, but such interpolants do not always exist, depend discontinuously on the data, and exhibit spurious pole-zero pairs both in exact arithmetic and even more commonly in floating point arithmetic. They can be computed by solving a matrix problem involving a Toeplitz matrix of discrete Fourier coefficients. Uniqueness, continuous dependence, and avoidance of spurious poles can be achieved by reducing $m$ and $n$ when the minimal singular value of this matrix is multiple. It may also be helpful to oversample and solve a least-squares problem.

Exercise 26.1. Nonexistence of certain interpolants. Show that if a function in $\mathcal { R } _ { 1 1 }$ takes equal values at two points, it must be a constant.

Exercise 26.2. An invalid argument. We saw that the type $( 3 , 3 )$ interpolant to $\cos ( e ^ { x } )$ in 7 Chebyshev points has a pole near $x = 0 . 6$ . What is the flaw in the following argument? (Spell it out carefully; don’t just give a word or two.) The interpolant through these 7 data values can be regarded as a combination of cardinal functions, i.e., type $( 3 , 3 )$ rational interpolants through Kronecker delta functions supported at each of the data points. If the sum has a pole at $x _ { 0 }$ , then one of the cardinal interpolants must have a pole at $x _ { 0 }$ . So type $( 3 , 3 )$ rational interpolants to almost every set of data at these 7 points will have a pole at exactly the same place.

Exercise 26.3. Explicit example of degeneracy. Following the example (26.2)–(26.3), but now on the unit circle, let $r$ be the type $( 1 , 1 )$ rational function satisfying $r ( 1 ) = 1$ , $r ( \omega ) = 1 + i \varepsilon$ , $r ( \overline { { \omega } } ) = 1 - i \varepsilon$ , where $\omega$ is the cube root of 1 in the upper half-plane and $\varepsilon > 0$ is a parameter. (a) What is $r$ ? (b) What is the $2 \times 3$ matrix $\hat { C }$ of (26.7)? (c) How do the singular values of $\hat { C }$ behave as $\varepsilon  0$ ?

Exercise 26.4. Rational vs. polynomial approximation. The final computational example of this chapter considered type $( n , n )$ rational approximation of $f ( z ) = \log ( 1 . 4 4 -$ $z ^ { 2 }$ ) with $n = 4 0$ , which was reduced to $n = 1 8$ by the robust algorithm. For degree $2 n$ polynomial approximation, one would expect accuracy of order $O ( \rho ^ { - 2 n } )$ , where $\rho$ is the radius of convergence of the Taylor series of $f$ at $z = 0$ . How large would $n$ need to be for this figure to be comparable to the observed accuracy of $1 0 ^ { - 1 1 }$ ?

Exercise 26.5. Rational Gibbs phenomenon (from [Pach´on 2010, Sect. 5.1]). We saw in Chapter 9 that if $f ( x ) = \mathrm { s i g n } ( x )$ is interpolated by polynomials in Chebyshev points in $[ - 1 , 1 ]$ , the errors decay inverse-linearly with distance from the discontinuity. Use ratinterp to explore the analogous rates of decay for type $( m , 2 )$ and $( m , 4 )$ linearized rational interpolants to the same function, keeping $m$ odd for simplicity. What do the decay rates appear to be?

Exercise 26.6. A function with two rows of poles. After Theorem 22.1 we considered as an example the function $f ( x ) = ( 2 + \cos ( 2 0 x + 1 ) ) ^ { - 1 }$ . (a) Call ratinterp with $( m , n ) =$ (100, 20) to determine a rational approximation $r$ to $f$ on $[ - 1 , 1 ]$ with up to 20 poles. How many poles does $r$ in fact have, and what are they? (b) Determine analytically the full set of poles of $f$ and produce a plot of the approximations from (a) together with the nearby poles of $f$ . How accurate are these approximations?

# Chapter 27. Pad´e Approximation

Suppose $f$ is a function with a Taylor series

$$
f ( z ) = c _ { 0 } + c _ { 1 } z + c _ { 2 } z ^ { 2 } + \cdot \cdot \cdot
$$

at $z = 0$ .14 Whether or not the series converges doesn’t matter in this chapter (it is enough for $f$ to be a formal power series). For any integer $m \geq 0$ , the degree $m$ Taylor approximant to $f$ is the unique polynomial $p _ { m } \in \mathcal { P } _ { m }$ that matches the series as far as possible, which will be at least through degree $m$ ,

$$
( f - p _ { m } ) ( z ) = O ( z ^ { m + 1 } ) .
$$

Pad´e approximation is the generalization of this idea to rational approximation. For any integers $m , n \geq 0$ , $r \in \mathcal { R } _ { m n }$ is the type $( m , n )$ Pad´e approximant to $f$ if their Taylor series at $z = 0$ agree as far as possible:

$$
( f - r _ { m n } ) ( z ) = O ( z ^ { \mathrm { m a x i m u m } } ) .
$$

In these conditions the “big O” notation has its usual precise meaning. Equation (27.2) asserts, for example, that the first nonzero term in the Taylor series for $f - p _ { m }$ is of order $z ^ { k }$ for some $k \geq m + 1$ , but not necessarily $k = m + 1$ .

Pad´e approximation can be viewed as the special case of rational interpolation in which the interpolation points coalesce at a single point. Thus there is a close analogy between the mathematics of the last chapter and this one, thoughsome significant differences too that spring from the fact that the powers $z ^ { 0 } , z ^ { 1 } , \dots$ are ordered whereas the roots of unity are all equal in status. We shall see that a key property is that $r _ { m n }$ exists and is unique. Generically, it matches $f$ through term $m + n$ ,

$$
( f - r _ { m n } ) ( z ) = O ( z ^ { m + n + 1 } ) ,
$$

but in some cases, the matching will be to lower or higher order.

For example, the type $( 1 , 1 )$ Pad´e approximant to $e ^ { z }$ is $( 1 + \textstyle { \frac { 1 } { 2 } } z ) / ( 1 - \textstyle { \frac { 1 } { 2 } } z )$ , as we can verify numerically with the Chebfun command padeapprox:

[r,a,b] $=$ padeapprox(@exp,1,1); fprintf(' Numerator coeffs: %19.15f %19.15f\n',a) fprintf(' Denominator coeffs: %19.15f %19.15f\n',b)

Numerator coeffs: 1.000000000000000 0.500000000000000   
Denominator coeffs: 1.000000000000000 -0.500000000000000

The algorithm used by padeapprox will be discussed in the second half of this chapter.

The early history of Pad´e approximation is hard to disentangle because every continued fraction can be regarded as a Pad´e approximant (Exercise 27.7), and continued fractions got a lot of attention in past centuries. For example, Gauss derived the idea of Gauss quadrature from a continued fraction that amounts to a Pad´e approximant to the function $\log ( ( z + 1 ) / ( z - 1 ) )$ at the point $z = \infty$ [Gauss 1814, Takahasi & Mori 1971, Trefethen 2008]. Ideas related to Pad´e approximation have been credited to Anderson (1740), Lambert (1758), and Lagrange (1776), and contributions were certainly made by Cauchy [1826] and Jacobi [1846]. The study of Pad´e approximants began to come closer to the current form with the papers of Frobenius [1881] and Pad´e himself [1892], who was a student of Hermite and published many articles after his initial thesis on the subject. Throughout the early literature, and also in the more recent era, much of the discussion of Pad´e approximation is connected with continued fractions, determinants, and recurrence relations, but here we shall follow a more robust matrix formulation.

We begin with a theorem about existence, uniqueness, and characterization, analogous to Theorem 24.1 for rational best approximation on an interval. There, the key idea was to count points of equioscillation of the error function $f - r$ . Here, we count how many initial terms of the Taylor series of $f - r$ are zero. The arguments are similar, and again, everything depends on the integer known as the defect. Recall that if $r \in \mathcal { R } _ { m n }$ is of exact type $( \mu , \nu )$ for some $\mu \leq m$ , $\nu \leq n$ , then the defect of $r$ with respect to $\mathcal { R } _ { m n }$ is $d = \operatorname* { m i n } \{ m - \mu , n - \nu \} \geq 0$ , with $\mu = - \infty$ and $d = n$ in the special case $r = 0$ .

Theorem 27.1. Characterization of Pad´e approximants. For each $m , n \geq$ 0, a function $f$ has a unique Pad´e approximant $r _ { m n } \in \mathcal { R } _ { m n }$ as defined by the condition (27.3), and a function $r \in \mathcal { R } _ { m n }$ is equal to $r _ { m n }$ if and only if $( f - r ) ( z ) =$ $O ( z ^ { m + n + 1 - d } )$ , where $d$ is the defect of $r$ in $\mathcal { R } _ { m n }$ .

Proof. The first part of the argument is analogous to parts 2 and 4 of the proof of Theorem 24.1: we show that if $r$ satisfies $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ , then $r$ is the unique type $( m , n )$ Pad´e approximant to $f$ as defined by the condition (27.3). Suppose then that $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ and that $( f - \tilde { r } ) ( z ) = O ( z ^ { m + n + 1 - d } )$ also for some possibly different function $\tilde { r } \in \mathcal { R } _ { m n }$ . Then $( r - { \tilde { r } } ) ( z ) = O ( z ^ { m + n + 1 - d } )$ . However, $r - \tilde { r }$ is of type $( m + n - d , 2 n - d )$ , so it can only have $m + n - d$ zeros at $z = 0$ unless it is identically zero. This implies $\tilde { r } = r$ .

The other half of the proof is to show that there exists a function $r$ with $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ . This part of the argument makes use of linear algebra and is given in the two paragraphs following (27.8).

Let us consider some examples to illustrate the characterization of Theorem 27.1. First, a generic case: We noted above that the type (1,1) Pad´e approximant to $e ^ { z }$ is $r _ { 1 1 } ( z ) = ( 1 + \textstyle \frac { 1 } { 2 } z ) / ( 1 - \textstyle \frac { 1 } { 2 } z )$ . The defect of $r _ { 1 1 }$ in $\mathcal { R } _ { 1 1 }$ is $d = 0$ , and we have

$$
r _ { 1 1 } ( z ) - e ^ { z } = \textstyle { \frac { 1 } { 1 2 } } z ^ { 3 } + \textstyle { \frac { 1 } { 1 2 } } z ^ { 4 } + \cdot \cdot \cdot = O ( z ^ { 3 } ) .
$$

Since $m + n + 1 - d = 3$ , this confirms that $r _ { 1 1 }$ is the Pad´e approximant.

On the other hand, if $f$ is even or odd, we soon find ourselves in the nongeneric case. Suppose we consider

$$
\begin{array} { r } { f ( z ) = \cos ( z ) = 1 - \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 2 4 } z ^ { 4 } - \cdot \cdot \cdot } \end{array}
$$

and the rational approximation

$$
\begin{array} { r } { r ( z ) = 1 - \frac { 1 } { 2 } z ^ { 2 } } \end{array}
$$

of exact type $( 2 , 0 )$ . This gives

$$
( f - r ) ( z ) = O ( z ^ { 4 } ) , \ \ne O ( z ^ { 5 } ) .
$$

By Theorem 27.1, this implies that $r$ is the Pad´e approximation to $f$ for four different choices of $( m , n )$ : $( 2 , 0 )$ , $( 3 , 0 )$ , $( 2 , 1 )$ , and $( 3 , 1 )$ . With $( m , n ) = ( 2 , 0 )$ , for example, the defect is $d = 0$ and we need $( f - r ) ( z ) = O ( z ^ { 2 + 0 + 1 - 0 } ) = O ( z ^ { 3 } )$ , and with $( m , n ) = ( 3 , 1 )$ , the defect is $d = 1$ and we need $( f - r ) ( z ) = O ( z ^ { 3 + 1 + 1 - 1 } ) = O ( z ^ { 4 } )$ . Both matching conditions are satisfied, so $r$ is the Pad´e approximant of both types $( 2 , 0 )$ and $( 3 , 1 )$ . Similarly it is also the Pad´e approximant of types $( 3 , 0 )$ and $( 2 , 1 )$ , but for no other values of $( m , n )$ .

This example involving an even function suggests the general situation. In analogy to the Walsh table of Chapter 24, the Pad´e table of a function $f$ consists of the set of its Pad´e approximants for various $m , n \geq 0$ laid out in an array, with $m$ along the horizontal and $n$ along the vertical:

$$
\left( { \begin{array} { c c c c } { r _ { 0 0 } } & { r _ { 1 0 } } & { r _ { 2 0 } } & { . . . } \\ { r _ { 0 1 } } & { r _ { 1 1 } } & { r _ { 2 1 } } & { . . . } \\ { r _ { 0 2 } } & { r _ { 1 2 } } & { r _ { 2 2 } } & { . . . } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } \end{array} } \right) .
$$

The idea of the Pad´e table was proposed by Pad´e [1892], who called it “a table of approximate rational fractions. . . analogous to the multiplication table, unbounded to the right and below.” Like the Walsh table for real rational approximation on an interval, the Pad´e table breaks into square blocks of degenerate entries, again as a consequence of the equioscillation-type characterization [Trefethen 1984].

Theorem 27.2. Square blocks in the Pad´e table. The Pad´e table for any function $f$ breaks into precisely square blocks containing identical entries. (If $f$ is rational, one of these will be infinite in extent.) The only exception is that if an entry $r = 0$ appears in the table, then it fills all of the columns to the left of some fixed index $m = m _ { 0 }$ .

Proof. The proof is essentially the same as the proof of Theorem 24.2.

As in the case of best real approximation on an interval discussed in Chapter 24, square blocks and defects have a variety of consequences for Pad´e approximants. In particular, the Pad´e approximation operator, which maps Taylor series $f$ to their Pad´e approximants $r _ { m n }$ , is continuous at $f$ with respect to a norm based on Taylor coefficients if and only if $r _ { m n }$ has defect $d = 0$ . Another related result is that best supremum-norm approximations on intervals $[ - \varepsilon , \varepsilon ]$ converge to the Pad´e approximant as $\varepsilon  0$ if $d = 0$ , but not, in general, if $d > 0$ . These results come from [Trefethen $\&$ Gutknecht 1985], with earlier partial results due to Walsh; Werner and Wuytak; and Chui, Shisha, and Smith.

At this point we have come a good way into the theory of Pad´e approximation without doing any algebra. To finish the job, and to lead into algorithms, it is time to introduce vectors and matrices, closely analogous to those of the last chapter.

Given a function $f$ with Taylor coefficients $\{ c _ { j } \}$ , suppose we look for a representation of the Pad´e approximant $r _ { m n }$ as a quotient $r = p / q$ with $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ . Equation (27.4) is nonlinear, but multiplying through by the denominator suggests the linear condition

$$
p ( z ) = f ( z ) q ( z ) + O ( z ^ { m + n + 1 } ) ,
$$

just as (26.4) led to (26.5). To express this equation in matrix form, suppose that $p$ and $q$ are represented by coefficient vectors $\mathbf { a }$ and $\mathbf { b }$ :

$$
\mathbf { a } = \left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { m } } \end{array} \right) , \qquad \mathbf { b } = \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) ,
$$

$$
p ( z ) = \sum _ { k = 0 } ^ { m } a _ { k } z ^ { k } , \qquad q ( z ) = \sum _ { k = 0 } ^ { n } b _ { k } z ^ { k } .
$$

Then (27.5) can be written as an equation involving a Toeplitz matrix of Taylor coefficients of $f$ , that is, a matrix with constant entries along each diagonal. For $m \geq n$ , the equation looks like this:

$$
\left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { n } } \\ { \vdots } \\ { \vdots } \\ { a _ { m + 1 } } \\ { a _ { m + 1 } } \\ { \vdots } \\ { a _ { m + n } } \end{array} \right) = \left( \begin{array} { c c c c c } { c _ { 0 } } & & & & \\ { c _ { 1 } } & & { c _ { 0 } } & & \\ { \vdots } & { \vdots } & { \ddots } & & \\ { c _ { n } } & { c _ { m - 1 } } & { \ddots } & & { c _ { 0 } } \\ { \vdots } & { \vdots } & & & { \vdots } \\ { c _ { m } } & { c _ { m - 1 } } & { \hdots } & { c _ { m - n } } \\ { c _ { m + 1 } } & { c _ { m } } & { \hdots } & { c _ { m + 1 - n } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { c _ { m + n } } & { c _ { m + n - 1 } } & { \hdots } & { c _ { m } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right)
$$

coupled with the condition

$$
a _ { m + 1 } = \cdots = a _ { m + n } = 0 .
$$

In other words, $\mathbf { b }$ must be a null vector of the $n \times ( n + 1 )$ matrix displayed below the horizontal line. If $m < n$ , the equation looks like this:

$$
\left( \begin{array} { c } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { m + 1 } } \\ { a _ { m + 1 } } \\ { \vdots } \\ { a _ { n } } \\ { a _ { m } } \end{array} \right) = \left( \begin{array} { c c c c c c c } { c _ { 0 } } \\ { c _ { 1 } } \\ { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \ddots } \\ { c _ { m } } & { c _ { m - 1 } } & { \ldots } & { c _ { 0 } } \\ { c _ { m + 1 } } & { c _ { m } } & { \ldots } & { c _ { 1 } } & { c _ { 0 } } \\ { c _ { m + 1 } } & { c _ { m } } & { \ldots } & { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } \\ { c _ { n } } & { c _ { n - 1 } } & { \ddots } & { c _ { 1 } } & { c _ { 0 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { c _ { m + n } } & { c _ { m + n - 1 } } & { \ldots } & { c _ { m } } \end{array} \right) \left( \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right) .
$$

For simplicity we shall use the label (27.6) to refer to both cases, writing the $n ~ \times$ $( n + 1 )$ matrix always as

$$
C = \left( \begin{array} { c c c c } { { c _ { m + 1 } } } & { { c _ { m } } } & { { \ldots } } & { { c _ { m + 1 - n } } } \\ { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { c _ { m + n } } } & { { c _ { m + n - 1 } } } & { { \ldots } } & { { c _ { m } } } \end{array} \right)
$$

with the convention that $c _ { k } = 0$ for $k < 0$ .

One solution to (27.6)–(27.7) would be $\mathbf { a } = \mathbf { 0 }$ and $\mathbf { b } = \mathbf { 0 }$ , corresponding to the useless candidate $r = 0 / 0$ . However, an $n \times ( n + 1 )$ matrix always has a nonzero null vector,

$$
C \mathbf { b } = \mathbf { 0 } , \quad \mathbf { b } \neq \mathbf { 0 } ,
$$

and once $\mathbf { b }$ is chosen, the coefficients $a _ { 0 } , \ldots , a _ { m }$ of $p$ can be obtained by multiplying out the matrix-vector product above the line. Thus there is always a solution to (27.5) with $q \neq 0$ .

If $b _ { 0 } \neq 0$ , then dividing (27.5) by $q$ shows that $p / q$ is a solution to (27.4). Some nonzero null vectors $\mathbf { b }$ , however, may begin with one or more zero components. Suppose that $\mathbf { b }$ is a nonzero null vector with $b _ { 0 } = b _ { 1 } = \cdot \cdot \cdot = b _ { \sigma - 1 } = 0$ and $b _ { \sigma } \neq 0$ for some $\sigma \geq 1$ . Then the corresponding vector $\mathbf { a }$ will also have $u _ { 0 } = u _ { 1 } = \cdot \cdot \cdot =$ $a _ { \sigma - 1 } = 0$ (and $a _ { \sigma }$ might be zero or nonzero). It follows from the Toeplitz structure of (27.6) that we can shift both $\mathbf { a }$ and $\mathbf { b }$ upward by $\sigma$ positions to obtain new vectors $\tilde { \mathbf { a } } = ( a _ { \sigma } , \ldots , a _ { m } , 0 , \ldots , 0 ) ^ { T }$ and $\bar { \mathbf { b } } = ( b _ { \sigma } , \ldots , b _ { n } , 0 , \ldots , 0 ) ^ { T }$ while preserving the quotient $r = \tilde { p } / \tilde { q } = p / q$ . Thus $r$ has defect $d \geq \sigma$ , and (27.6)–(27.7) are still satisfied except that $\tilde { a } _ { m + n - \sigma + 1 } , \dots , \tilde { a } _ { m + n }$ may no longer be zero, implying $( f - r ) ( z ) = O ( z ^ { m + n + 1 - \sigma } )$ . Thus $( f - r ) ( z ) = O ( z ^ { m + n + 1 - d } )$ , and this completes the proof of Theorem 27.1.

We have just shown that any nonzero null vector of the matrix $C$ of (27.8) gives a function $r$ that satisfies the condition for a Pad´e approximation and hence must be the unique approximant provided by Theorem 27.1. So we have proved the following theorem.

Theorem 27.3. Linear algebra solution of Pad´e problem. Given a function $f$ with Taylor coefficients $\{ c _ { j } \}$ , let b be any nonzero null vector of the matrix

$C$ of (27.8), let a be the corresponding vector obtained from (27.6), and let $p \in \mathcal { P } _ { m }$ and $q \in \mathcal { P } _ { n }$ be the corresponding polynomials. Then $r _ { m n } = p / q$ is the unique type $( m , n )$ Pad´e approximant to $f$ .

We emphasize that the vectors $\mathbf { a }$ and $\mathbf { b }$ are not unique in general: a function in $\mathcal { R } _ { m n }$ may have many representations $p / q$ . Nevertheless, all choices of $\mathbf { a }$ and $\mathbf { b }$ lead to the same rmn.

From Theorems 27.1–27.3 one can derive a precise characterization of the algebraic structure of the Pad´e approximants to a function $f$ , as follows. Let $\hat { r }$ b e a rational function of exact type $( \mu , \nu )$ that is the Pad´e approximant to $f$ in a $( k + 1 ) \times ( k + 1 )$ square block for some $k \geq 0$ :

$$
\left( \begin{array} { c c c } { { r _ { \mu \nu } } } & { { . . . } } & { { r _ { \mu + k , \nu } } } \\ { { } } & { { } } & { { } } \\ { { \vdots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } \\ { { r _ { \mu , \nu + k } } } & { { . . . } } & { { r _ { \mu + k , \nu + k } } } \end{array} \right) .
$$

Write $\hat { r } = \hat { p } / \hat { q }$ with $\hat { p }$ and $\hat { q }$ of exact degrees $\mu$ and $\nu$ . From Theorem 27.1 we know that the defect $d$ must be distributed within the square block according to this pattern illustrated for $k = 5$ :

$$
\begin{array} { r l } { { \operatorname* { d e f e c t } \ d : } } & { { } \left( \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { 2 } & { 2 } & { 2 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 3 } & { 3 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 4 } \\ { 0 } & { 1 } & { 2 } & { 3 } & { 4 } & { 5 } \end{array} \right) \ . } \end{array}
$$

According to Theorem 27.3, the polynomials $p$ and $q$ that result from solving the matrix problem (27.6)–(27.7) must be related to $\hat { p }$ and $\hat { q }$ by

$$
p ( z ) = \pi ( z ) \hat { p } ( z ) , \quad q ( z ) = \pi ( z ) \hat { q } ( z )
$$

for some polynomial $\pi$ of degree at most $d$ . Now let us define the deficiency $\lambda$ of $r$ as the distance below the cross-diagonal in the square block, with the following pattern:

$$
\mathrm { d e f f c i e n c y ~ } \lambda : \quad \left( \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 3 } } & { { 4 } } & { { 5 } } \end{array} \right) ~ . \nonumber
$$

From Theorem 27.1, we know that in the positions of the block with $\lambda ~ > ~ 0$ , $( f - r ) ( z ) = O ( z ^ { m + n + 1 - \lambda } ) , \neq O ( z ^ { m + n + 2 - \lambda } )$ , for otherwise, the block would be bigger. For this to happen, $\pi ( z )$ must be divisible by $z ^ { \lambda }$ , so that at least $\lambda$ powers of $z$ are lost when solutions $p$ and $q$ from (27.6) are normalized to $\hat { p }$ and $\hat { q }$ . Since may have degree up to $d$ , the number of degrees of freedom remaining in and $\pi$ $p$ $q$ is $d - \lambda$ , an integer we denote by $\chi$ , distributed within the block according to this

pattern:

$$
\mathrm { r a n k ~ d e f i c i e n c y ~ } \chi ; \quad \left( \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 2 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) \ .
$$

Thus the dimensionality of the space of vectors $q$ is $\chi + 1$ , and the same for $p$ . We call $\chi$ the rank deficiency of $r$ because of a fact of linear algebra: the rank of the $n \times ( n + 1 )$ matrix $C$ of (27.8) must be equal to $n - \chi$ , so that its space of null vectors will have the required dimension $\chi + 1$ . Some ideas related to these developments can be found in [Heinig & Rost 1984].

We have just outlined a proof of the following theorem, which can be found in Section 3 of [Gragg 1972].

Theorem 27.4. Structure of a Pad´e approximant. Let $f$ and $m , n \geq 0$ be given, let the type $( m , n )$ Pad´e approximant $r _ { m n }$ of $f$ have exact type $( \mu , \nu )$ , and let $\hat { p }$ and $\hat { q } \neq 0$ be polynomials of exact degrees $\mu$ and $\nu$ with $r _ { m n } = \hat { p } / \hat { q }$ . Let the defect $d$ , deficiency $\lambda$ , and rank deficiency $\chi = d - \lambda$ be defined as above. Then the matrix $C$ of (27.8) has rank $n - \chi$ , and two polynomials $p \in P _ { m }$ and $q \in P _ { n }$ satisfy (27.5) if and only if

$$
p ( z ) = \pi ( z ) \hat { p } ( z ) , \quad q ( z ) = \pi ( z ) \hat { q } ( z )
$$

for some $\pi \in \mathcal { P } _ { d }$ divisible by $z ^ { \lambda }$ .

Although we did not state it in the last chapter, there is an analogue of this theorem for rational interpolation in distinct points, proved by Maehly and Witzgall [1960] and discussed also in [Gutknecht 1990] and [Pach´on, Gonnet & Van Deun 2012].

With the results of the past few pages to guide us, we are now prepared to talk about algorithms.

At one level, the computation of Pad´e approximants is trivial, just a matter of implementing the linear algebra of (27.6)–(27.7). In particular, in the generic case, the matrix $C$ of (27.8) will have full rank, and so will its $n \times n$ submatrix obtained by deleting the first column. One computational approach to Pad´e approximation is accordingly to normalize $\mathbf { b }$ by setting $b _ { 0 } = 1$ and then determine the rest of the entries of $\mathbf { b }$ by solving a system of equations involving this square matrix.

This approach will fail, however, when the square matrix is singular, and it is nonrobust with respect to rounding errors even when the matrix is nonsingular. To work with (27.8) robustly, it is a better idea to normalize by the condition

$$
\| \mathbf { b } \| = 1 ,
$$

where $\| \cdot \|$ is the vector 2-norm, as in (26.6) of the last chapter. We then again consider the SVD (singular value decomposition) of $C$ , a factorization

$$
\boldsymbol { C } = \boldsymbol { U \Sigma V } ^ { * } ,
$$

where $U$ is $n \times n$ and unitary, $V$ is $( n + 1 ) \times ( n + 1 )$ and unitary, and $\Sigma$ is an $n \times ( n + 1 )$ real diagonal matrix with diagonal entries $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { n } \geq 0$ .

Suppose $\sigma _ { n } ~ > ~ 0$ . Then $C$ has rank $n$ , and the final column of $V$ provides a unique nonzero null vector $\mathbf { b }$ of $C$ up to a scale factor. This null vector defines a polynomial $q \in \mathcal { P } _ { n }$ . Moreover, from (27.11), we know that $( m , n )$ must lie on the outer boundary of its square block in the Pad´e table. If $q$ is divisible by $z ^ { \lambda }$ for some $\lambda \geq 1$ , then $( m , n )$ must lie in the bottom row or right column, and dividing $p$ and $q$ by $z ^ { \lambda }$ brings it to the left column or top row, respectively. A final trimming of any trailing zeros in $p$ or $q$ brings them to the minimal forms $\hat { p }$ and $\hat { q }$ with exact degrees $\mu$ and $\nu$ .

On the other hand, suppose $\sigma _ { n } = 0$ , so that the number of zero singular values of $C$ is $\chi \geq 1$ . In this case (27.11) tells us that $( m , n )$ must lie in the interior of its square block at a distance $\chi$ from the boundary. Both $m$ and $n$ can accordingly be reduced by $\chi$ and the process repeated with a new matrix and a new SVD, $\chi$ steps closer to the upper-left $( \mu , \nu )$ corner. After a small number of such steps (never more than $2 + \log _ { 2 } ( d + 1 )$ , where $d$ is the defect), convergence is guaranteed.

These observations suggest the following SVD-based algorithm, introduced in [Gonnet, G¨uttel $\&$ Trefethen 2013].

Algorithm 27.1. Pure Pad´e approximation in exact arithmetic

Input: $m \geq 0$ , $n \geq 0$ , and a vector c of Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ of $a$ function $f$ .

Output: Polynomials $p ( z ) = a _ { 0 } + \cdot \cdot \cdot + a _ { \mu } z ^ { \mu }$ and $q ( z ) = b _ { 0 } + \cdot \cdot \cdot + b _ { \nu } z ^ { \nu }$ , $b _ { 0 } = 1$ , of the minimal degree type $( m , n )$ Pad´e approximation of $f$ .

1. If $c _ { 0 } = \cdots = c _ { m } = 0$ , set $p = 0$ and $q = 1$ and stop.

2. If $n = 0$ , set $p ( z ) = c _ { 0 } + \cdot \cdot \cdot + c _ { m } z ^ { m }$ and $q = 1$ and go to Step 8.

3. Compute the $S V D$ (27.13) of the $n \times ( n + 1 )$ matrix $C$ . Let $\rho \leq n$ be the number of nonzero singular values.

4. If $\rho < n$ , reduce $n$ to $\rho$ and $m$ to $m - ( n - \rho )$ and return to Step 2.

5. Get $q$ from the null right singular vector b of $C$ and then $p$ from the upper part of (27.6).

6. If $b _ { 0 } = \cdot \cdot \cdot = b _ { \lambda - 1 } = 0$ for some $\lambda \geq 1$ , which also implies $a _ { 0 } = \cdot \cdot \cdot = a _ { \lambda - 1 } = 0$ , cancel the common factor of $z ^ { \lambda }$ in $p$ and $q$ .

7. Divide $p$ and $q$ by $b _ { 0 }$ to obtain a representation with $b _ { 0 } = 1$ .

8. Remove trailing zero coefficients, if any, from $p ( z )$ or $q ( z )$ .

In exact arithmetic, this algorithm produces the unique Pad´e approximant $r _ { m n }$ in a minimal-degree representation of type $( \mu , \nu )$ with $b _ { 0 } = 1$ . The greatest importance of Algorithm 27.1, however, is that it generalizes readily to numerical computation with rounding errors, or with noisy Taylor coefficients $\{ c _ { j } \}$ . All one needs to do is modify the tests for zero singular values or zero coefficients so as to incorporate a suitable tolerance, such as $1 0 ^ { - 1 4 }$ for computations in standard 16-digit arithmetic. The following modified algorithm also comes from [Gonnet, G¨uttel $\&$ Trefethen 2013].

Algorithm 27.2. Robust Pad´e approximation for noisy data or floating point arithmetic

Input: $m \geq 0$ , $n \geq 0$ , a vector c of Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ of a function $f$ , and a relative tolerance $\mathbf { t o l } \geq 0$ .

Output: Polynomials $p ( z ) = a _ { 0 } + \cdot \cdot \cdot + a _ { \mu } z ^ { \mu }$ and $q ( z ) = b _ { 0 } + \cdot \cdot \cdot + b _ { \nu } z ^ { \nu }$ , $b _ { 0 } = 1$ , of the minimal degree type $( m , n )$ Pad´e approximation of a function close to $f$ .

1. Rescale $f ( z )$ to $f ( z / \gamma )$ for some $\gamma > 0$ if desired to get a function whose Taylor coefficients $c _ { 0 } , \ldots , c _ { m + n }$ do not vary too widely.

2. Define $\tau = \pm \circ 1 \cdot \| \mathbf { c } \| _ { 2 }$ . If $| c _ { 0 } | = \cdot \cdot \cdot = | c _ { m } | \leq \tau$ , set $p = 0$ and $q = 1$ and stop.

3. If $n = 0$ , set $p ( z ) = c _ { 0 } + \cdot \cdot \cdot + c _ { m } z ^ { m }$ and $q = 1$ and go to Step 7.

4. Compute the $S V D$ (27.13) of the $n \times ( n + 1 )$ matrix $C$ . Let $\rho \leq n$ be the number of singular values of $C$ that are greater than $\gamma$ .

5. If $\rho < n$ , reduce n to $\rho$ and m to $m - ( n - \rho )$ and return to Step 3.

6. Get $q$ from the null right singular vector b of $C$ and then p from the upper part of (27.6).

7. If $| b _ { 0 } | , \ldots , | b _ { \lambda - 1 } | \leq \mathrm { t o l }$ for some $\lambda \geq 1$ , zero the first $\lambda$ coefficients of $p$ and $q$ and cancel the common factor $z ^ { \lambda }$ .

8. If $| b _ { n + 1 - \lambda } | , \ldots , | b _ { n } | \leq \mathtt { t o l }$ for some $\lambda \geq 1$ , remove the last $\lambda$ coefficients of $q$ . If $| a _ { m + 1 - \lambda } | , \ldots , | a _ { m } | \leq \tau$ for some $\lambda \geq 1$ , remove the last $\lambda$ coefficients of $p$ .

9. Divide $p$ and $q$ by $b _ { 0 }$ to obtain a representation with $b _ { 0 } = 1$ .

10. Undo the scaling of Step 1 by redefining $\gamma ^ { j } a _ { j }$ as $a _ { j }$ and $\gamma ^ { j } b _ { j }$ as $b _ { j }$ for each $j$

Algorithm 27.2 has been implemented in a MATLAB code called padeapprox that is included in the Chebfun distribution, though it does not involve chebfuns. In its basic usage, padeapprox takes as input a vector $\mathbf { c }$ of Taylor coefficients together with a specification of $m$ and $n$ , with $\mathtt { t o l } = 1 0 ^ { - 1 4 }$ by default. For example, following [Gragg 1972], suppose

$$
f ( z ) = { \frac { 1 - z + z ^ { 3 } } { 1 - 2 z + z ^ { 2 } } } = 1 + z + z ^ { 2 } + 2 z ^ { 3 } + 3 z ^ { 4 } + 4 z ^ { 5 } + \cdots .
$$

Then the type $( 2 , 5 )$ Pad´e approximation of $f$ comes out with the theoretically correct exact type $( 0 , 3 )$ :

c = [1 1 (1:50)]; [r,a,b] $=$ padeapprox(c,2,5); disp(a.'), disp(b.')

Coefficients of numerator: 1.0000 Coefficients of denominator:

1.0000 -1.0000 0.0000 -1.0000

To illustrate the vital role of the SVD in such a calculation, here is what happens if robustness is turned off by setting $\tt t o l = 0$ :

[r,a,b] $=$ padeapprox(c,2,5,0); disp(a.'), disp(b.')

Coefficients of numerator:

1.0e+15 \*  
0.0000 -0.0000 3.4166

Coefficients of denominator:

0.0000 -0.0000 3.4166 -3.4166 0.0000 -3.4166

We now see longer vectors with enormous entries, on the order of the inverse of machine precision. The type appears to be $( 2 , 5 )$ , but the zeros and poles reveal that this is spurious:

disp(roots(a(end:-1:1))), disp(roots(b(end:-1:1)))

Zeros:

1.44015621657119e-16 + 1.71080672699754e-08i1.44015621657119e-16 - 1.71080672699754e-08iPoles:-0.341163901914009 + 1.16154139999725i-0.341163901914009 - 1.16154139999725i0.6823278038280191.44015621642544e-16 + 1.71080672699754e-08i1.44015621642544e-16 - 1.71080672699754e-08i

We see that the two zeros are virtually canceled by two poles that differ from them by only about $1 0 ^ { - 2 4 }$ . Thus this approximant has two spurious pole-zero pairs, or Froissart doublets, introduced by rounding errors. Many Pad´e computations over the years have been contaminated by such effects, and in an attempt to combat them, many authors have asserted that it is necessary to compute Pad´e approximations in high-precision arithmetic.

If padeapprox is called with a MATLAB function handle $f$ rather than a vector as its first argument, then it assumes $f$ is a function analytic in a neighborhood of the closed unit disk and computes Taylor coefficients by the FFT. For example, here is the type $( 2 , 2 )$ Pad´e approximant of $f ( z ) = \cos ( z )$ :

[r,a,b] = padeapprox(@cos,2,2); disp(a.'), disp(b.')

Coefficients of numerator: 1.000000000000000 0 -0.416666666666667   
Coefficients of denominator: 1.000000000000000 0 0.083333333333333

One appealing application of padeapprox is the numerical computation of block structure in the Pad´e table for a given function $f$ . For example, here is a table of the computed pair $( \mu , \nu )$ for each $( m , n )$ in the upper-left portion of the Pad´e table of $\cos ( z )$ with $0 \leq m , n \leq 8$ . One sees the $2 \times 2$ block structure resulting from the evenness of $\cos ( z )$ .

nmax $= ~ 8$ ; for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$

for $\mathtt { m } \ = \ 0$ :nmax [r,a,b,mu,nu] $=$ padeapprox(@cos,m,n); fprintf(' (%1d,%1d)',mu,nu) end fprintf $( " \setminus " )$ end

(0,0) (0,0) (2,0) (2,0) (4,0) (4,0) (6,0) (6,0) (8,0) (0,0) (0,0) (2,0) (2,0) (4,0) (4,0) (6,0) (6,0) (8,0) (0,2) (0,2) (2,2) (2,2) (4,2) (4,2) (6,2) (6,2) (8,2) (0,2) (0,2) (2,2) (2,2) (4,2) (4,2) (6,2) (6,2) (8,2) (0,4) (0,4) (2,4) (2,4) (4,4) (4,4) (6,4) (6,4) (8,4) (0,4) (0,4) (2,4) (2,4) (4,4) (4,4) (6,4) (6,4) (8,4) (0,6) (0,6) (2,6) (2,6) (4,6) (4,6) (6,6) (6,6) (8,6) (0,6) (0,6) (2,6) (2,6) (4,6) (4,6) (6,6) (6,6) (8,6) (0,8) (0,8) (2,8) (2,8) (4,8) (4,8) (6,8) (6,8) (8,8)

We can also show the block structure with a color plot, like this:

d = zeros(nmax $^ { + 2 }$ );   
rand('state',7); h = tan(2\*rand(50)-1); h(8,1) = 1;   
for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$ , for m = 0:nmax $[ \mathbf { r } , \mathbf { a } , \mathbf { b } , \mathtt { m u } , \mathtt { n u } ] \ = \ \mathtt { p a d e a p p r o x } ( \mathtt { q c o s } , \mathtt { m } , \mathtt { n } ) ; \ \mathtt { d } ( \mathtt { n } + 1 , \mathtt { m } + 1 ) \ = \ \mathtt { h } ( \mathtt { m u } + 1 , \mathtt { n u } + 1 )$ ;   
end, end, pcolor(d), axis ij square off

Pad´e table of cos(z)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/d1bcc5e47359d73544afa6fe38d9c72ede3bff9a0a46350c613c3fd463d7de52.jpg)

The pattern of $2 \times 2$ blocks is broken if we compute a larger segment of the table, such as $0 \leq m , n \leq 1 6$ :

nmax $\textstyle { \begin{array} { r l } \end{array} } = { \begin{array} { r l } { 1 6 } \end{array} }$ ; d = zeros(nmax+2);   
for $\mathtt { n } \ = \ 0 : \mathtt { n m a x }$ , for $\mathtt { m } \ = \ 0$ :nmax [r,a,b,mu,nu] $=$ padeapprox(@cos,m,n); d( $\mathtt { n } { + } 1$ ,m+1) = h(mu+1,nu+1);   
end, end, pcolor(d), axis ij square off

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/1f5924d667f3826fa7628b5e5879ac29b445e6eb79057f4275c3ed0ef985e38b.jpg)

What is going on here is that for $m + n$ greater than about 16, $\cos ( z )$ is resolved to machine precision, and the diagonal stripes of the plot show that padeapprox has automatically cut $m$ and $n$ down to this level.

For an “arbitrary” function $f$ with gaps in its Taylor series, the block structure can be quite intriguing, as illustrated by this example with $f ( z ) = 1 + z + z ^ { 4 } + z ^ { 7 } +$ $z ^ { 1 0 } + z ^ { 1 3 } + z ^ { 1 6 } + z ^ { 1 7 }$ :

$$
\begin{array} { r l } & { \mathrm { ~ \beta = ~ \Theta ( z ) ~ \gamma _ 1 + z + z _ { \perp } \cdot \gamma _ 4 + z _ { \perp } \cdot \hat { \mathrm {  ~ \gamma ~ } } \mathrm { \hat { \mathrm {  ~ \gamma ~ } } \mathrm { \hat { \mathrm {  ~ \psi ~ } } \mathrm {  ~ \psi ~ } } } } } \\ & { \mathrm { ~ \beta r ~ \mathrm { ~ n ~ \beta ~ = ~ 0 : n m a x , ~ \hat { \mathrm { ~ f ~ o r ~ ~ m ~ \psi ~ } } = ~ 0 : n m a x } ~ } } \\ & { \mathrm { ~ [ \hat { \mathrm { ~  ~ r ~ } } , \mathrm { ~ a ~ } , \mathrm { b ~ } , m u , n u ] ~ \mathrm { ~ \beta ~ = ~ \ p a d e a p p r o x ( \mathrm { ~ f ~ , ~ m ~ } , n ) ~ ; ~ \mathrm { ~ d ~ } ( n + 1 , m + 1 ) ~ \mathrm { ~ \beta ~ = ~ h ~ ( m u + 1 , n u + 1 ) ~ ; ~ \hat { \mathrm { ~ o r ~ } ~ } \mathrm { ~ \hat { \delta ~ } ~ } } ~ } } } \end{array}
$$

end, end, pcolor(d), axis ij square off

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/08a9b6677bb826de065fa36fe7c1499a670bc0e4d892b4dd93100a577ea21ee7.jpg)

Apart from $z ^ { 1 7 }$ , these are the initial terms of the Taylor series of

$$
f ( z ) = { \frac { 1 + z - z ^ { 3 } } { 1 - z ^ { 3 } } } ,
$$

an example for which Pad´e worked out the block structure for $0 \leq m \leq 7$ , $0 \leq n \leq 5$ [Pad´e 1892], showing vividly a $2 \times 2$ block, two $3 \times 3$ blocks, and the beginning of the infinite block at position $( 3 , 3 )$ .

In this chapter we have discussed how to compute Pad´e approximants, but not what they are useful for. As outlined in Chapter 23, applications of these approximations typically involve situations where we know a function in one region of the $z$ -plane and wish to evaluate it in another region that lies near or beyond certain singularities. The next chapter is devoted to practical exploration of such problems.

From a theoretical perspective, a central question for more than a century has been, what sort of convergence of Pad´e approximants of a function $f$ can we expect as $m$ and/or $n$ increase to $\infty$ ? In the simplest case, suppose that $f$ is an entire function, that is, analytic for all $z$ . Then for any compact set $K$ in the complex plane, we know that the type $( m , 0 )$ Pad´e approximants converge uniformly on $K$ as $m \to \infty$ , since these are just the Taylor approximants. One might hope that the same would be true of type $( m , n _ { 0 } )$ approximants for fixed $n _ { 0 } \geq 1$ as $m \to \infty$ , or of type $( n , n )$ approximants as $n \to \infty$ , but in fact, pointwise convergence need not occur in either of these situations. The problem is that spurious pole-zero pairs, Froissart doublets, may appear at seemingly arbitrary locations in the plane. As $m$ and/or $n$ increases, the doublets get weaker and their effects more localized, but they can never be guaranteed to go away. (In fact, there exist functions $f$ whose Pad´e approximants have so many spurious poles that the sequence of $( n , n )$ approximants is unbounded for every $z \neq 0$ [Perron 1929, Wallin 1972].) The same applies if $f$ is meromorphic, i.e., analytic apart from poles, or if it has more complicated singularities such as branch points. All this is true in exact mathematics, and when there are rounding errors on a computer, the doublets become ubiquitous.

Despite these complexities, important theorems have been proved. The theorem of de Montessus de Ballore [1902] concerns the case of $m \to \infty$ with fixed $n$ , guaranteeing convergence in a disk about $z = 0$ if $f$ has exactly $n$ poles there. The Nuttall– Pommerenke theorem [Nuttall 1970, Pommerenke 1973] concerns $m = \pi \to \infty$ and ensures convergence for meromorphic $f$ not pointwise but in measure or in capacity, these being precise notions that require accuracy over most of a region as $m , n \to \infty$ while allowing for localized anomalies. This result was powerfully generalized for functions with branch points by Stahl [1997], who showed that as $n  \infty$ , almost all the poles of type $( n , n )$ Pad´e approximants line up along branch cuts that have a property of minimal capacity in the $z ^ { - 1 }$ -plane. For discussion of these results see [Baker & Graves-Morris 1996]. There are also analogous results for multipoint Pad´e approximation and other forms of rational interpolation. For example, an analogue of the de Montessus de Ballore theorem for interpolation as in the last chapter was proved by Saff [1972].

As a practical matter, these complexities of convergence are well combated by the SVD approach we have described, which can be regarded as a method of regularization of the Pad´e problem.

For reasons explained in the last chapter, the whole discussion of this chapter has been based on the behavior of a function $f ( z )$ at $z = 0$ rather than this book’s usual context of a function $f ( x )$ on an interval such as $[ - 1 , 1 ]$ . There is an analogue of Pad´e approximation for $[ - 1 , 1 ]$ called Chebyshev–Pad´e approximation, developed by Hornecker [1956], Maehly [1963], Frankel and Gragg [1973], Clenshaw and Lord [1974], and Geddes [1981]. The idea is to consider the analogue of (27.3) for Chebyshev series rather than Taylor series:

$$
( f - r _ { m n } ) ( x ) = O ( T _ { \mathrm { m a x i m u m } } ( x ) ) .
$$

(The Maehly version starts from the analogue of the linearized form (27.5).) In analogy to Theorem 27.1, it turns out that any $r \in \mathcal { R } _ { m n }$ satisfying $( f - r ) ( x ) =$ $O ( T _ { m + n + 1 - d } ( x ) )$ is the unique Chebyshev–Pad´e approximant according to this definition, but now, there is no guarantee that such a function $T$ exists. For theoretical details, see [Trefethen & Gutknecht 1987], and for computations in Chebfun, there is a code chebpade. As of today, there has not yet been a study of Chebyshev–Pad´e approximation employing the SVD-based robustness ideas described in this chapter for Pad´e approximation.

For extensive information about Pad´e approximation, see the book by Baker and Graves-Morris [1996]. However, that monograph uses an alternative definition according to which a Pad´e approximant exists only if (27.4) can be satisfied, and in fact the present treatment is mathematically closer to the landmark review of Gragg [1972], which uses the definition (27.3).

Summary of Chapter 27. Pad´e approximation is the generalization of Taylor polynomials to rational approximation, that is, rational interpolation at a single point. Pad´e approximants are characterized by a kind of equioscillation condition and can be computed robustly by an algorithm based on the SVD. The analogue on the interval $[ - 1 , 1 ]$ is known as Chebyshev–Pad´e approximation.

Exercise 27.1. Pad´e approximation of a logarithm. Show from Theorem 27.1 that the function $f ( z ) = \log ( 1 + z )$ has Pad´e approximants $r _ { 0 0 } = 0$ , $r _ { 1 , 0 } ( z ) = z$ , $r _ { 0 1 } ( z ) = 0$ , and $r _ { 1 1 } = z / ( 1 + \textstyle { \frac { 1 } { 2 } } z )$ .

Exercise 27.2. Reciprocals and exponentials. (a) Suppose $r _ { m n }$ is the type $( m , n )$ Pad´e approximant to a function $f$ with $f ( 0 ) \neq 0$ . Show that $1 / r _ { m n }$ is the type $( n , m )$ Pad´e approximant to $1 / f$ . (b) As a corollary, state a theorem relating the $( m , n )$ and $( n , m )$ Pad´e approximants of $e ^ { z }$ .

Exercise 27.3. Prescribed block structures. Devise functions $f$ with the following structures in their Pad´e tables, and verify your claims numerically by color plots for $0 \leq$ $m , n \leq 2 0$ . (a) $3 \times 3$ blocks everywhere. (b) $1 \times 1$ blocks everywhere, except that $r _ { 1 1 } =$ $r _ { 2 1 } = r _ { 1 2 } = r _ { 2 2 }$ . (c) $1 \times 1$ blocks everywhere, except that all $r _ { m n }$ with $n \leq 2$ are the same.

Exercise 27.4. Order stars. The order star of a function $f$ and its approximation $r$ is the set of points $z$ in the complex plane for which $| f ( z ) | = | r ( z ) |$ . Use the MATLAB contour command to plot the order stars of the Pad´e approximations $r _ { 1 1 }$ , $r _ { 2 2 }$ , $r _ { 3 2 }$ , and $r _ { 2 3 }$ to $e ^ { z }$ . Comment on the behavior near the origin.

Exercise 27.5. Nonsingularity and normality. Show that for a given $f$ and $( m , n )$ , the Pad´e approximation $r _ { m n }$ has defect $d = 0$ if and only if the square matrix obtained by deleting the first column of (27.8) is nonsingular. (If all such matrices are nonsingular, the Pad´e table of $f$ is accordingly normal, with all its entries distinct.)

Exercise 27.6. Arbitrary patterns of square blocks? Knowing that degeneracies in the Pad´e table always occupy square blocks, one might conjecture that, given any tiling of the quarter-plane $m \geq 0$ , $n \geq 0$ by square blocks, there exists a function $f$ with this pattern in its Pad´e table. Prove that this conjecture is false. (Hint: Consider the case where the first two rows of the table are filled with $2 \times 2$ blocks [Trefethen 1984].)

Exercise 27.7. Continued fractions and the Pad´e table. If $d _ { 0 } , d _ { 1 } , \ldots$ is a sequence of numbers, the continued fraction

$$
d _ { 0 } + \frac { d _ { 1 } z } { 1 + \displaystyle \frac { d _ { 2 } z } { 1 + \cdot \cdot \cdot } }
$$

is shorthand for the sequence of rational functions

$$
d _ { 0 } , \ d _ { 0 } + d _ { 1 } z , \ d _ { 0 } + { \frac { d _ { 1 } z } { 1 + d _ { 2 } z } } , \ldots ,
$$

known as convergents of the continued fraction. (a) Show that if $d \sb { 0 } , \ldots , d \sb { k - 1 } \neq 0$ and $d _ { k } = 0$ , then (27.15) defines a rational function $r ( z )$ , and determine its exact type. (b) Assuming $d _ { k } \neq 0$ for all $k$ , show that the convergents are the Pad´e approximants of types $( 0 , 0 ) , ( 1 , 0 ) , ( 1 , 1 ) , ( 2 , 1 ) , ( 2 , 2 ) , \ldots$ of a certain formal power series.

# Chapter 28. Analytic Continuation and Convergence Acceleration

We have considered techniques for rational approximation by best approximation on an interval (Chapter 24, minimax), interpolation or linearized least-squares fitting on an interval or disk (Chapter 26, ratinterp and ratdisk), and Pad´e approximation at a point or Chebyshev–Pad´e approximation on an interval (Chapter 27, padeapprox and chebpade). In this final chapter, we turn to the application of such approximations for extrapolating a function to real or complex values $z$ outside the region where it is initially known. Three of the applications listed in Chapter 23 fall into this category: those numbered 3 (convergence acceleration for sequences and series), 4 (determination of poles), and 5 (analytic continuation).

It will be a chapter more of examples than theory. For an example to begin the discussion, suppose we pretend that we can evaluate

$$
f ( z ) = \operatorname { t a n h } ( z )
$$

for real values of $z$ but know nothing about complex values, and we wish to estimate where $f$ has poles. How might we proceed? (Of course we really know the answer: there are poles at all the odd multiples of $\pm \pi i / 2$ .)

The first thing to try might be polynomials. For example, we could use Chebfun to construct a polynomial that approximates $f$ to 16 digits on $[ - 1 , 1 ]$ ,

f = @(z) tanh(z); p = chebfun(f); length(p)

ans $=$ 30

From here, however, it is hard to make much progress. As we know from Chapter 8, $p$ will be a good approximation to $f$ within a certain Bernstein ellipse, the Chebfun ellipse, which can be plotted by the command plotregion. We can expect this ellipse to reach approximately out to the first singularities at $\pm \pi i / 2$ . Once we hit the ellipse, however, everything will change. According to the theory of Walsh [1959] and Blatt and Saff [1986] mentioned in Chapter 18, zeros of $p$ will cluster all along the boundary, and a further result of Blatt and Saff states that outside the ellipse, there will be no convergence at all. The polynomial $p$ will simply grow rapidly, its behavior having nothing to do with that of $f$ . We can confirm this prediction with contour plots. Here are plots of $| f ( z ) |$ and $| p ( z ) |$ in the upper half-plane, with black contours at levels $0 . 2 5 , 0 . 5 , \ldots , 3$ and red contours at $1 0 ^ { 1 } , 1 0 ^ { 3 } , 1 0 ^ { 5 } , \dots , 1 0 ^ { 1 9 }$ . We see immediately that $p$ matches $f$ very well inside the Chebfun ellipse, which is marked in blue, but not at all outside.

$\textbf { x } = \mathbf { \delta } - 4 : . 0 5 : 4$ ; $\texttt { y } = \texttt { 0 } : . 0 5 : 8$ ; [xx yy] $=$ meshgrid(x,y); $\mathrm { z z \ = \ \mathrm { x } \mathrm { x } \ + \ 1 i \mathrm { * } \mathrm { y } \mathrm { y } }$ ; ff = f(zz); $\mathtt { p p } = \mathtt { p } ( \mathtt { z } \mathtt { z } )$ ;   
lev1 $=$ .25:.25:2; lev2 = 10.^(1:2:19);   
subplot(1,2,1), contour(x,y,abs(ff),lev1,'k'), hold on contour(x,y,abs(ff),lev2,'r')   
subplot(1,2,2), contour(x,y,abs(pp),lev1,'k'), hold on contour(x,y,abs(pp),lev2, $" \mathbf { r } \cdot \mathbf { \xi }$ ), plotregion(p,'b')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/8629c7df03e133bbf2924e062e7042469204fdfb0197a09f837a86ed316cdefd.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a2ca5ea5f99c523e430da9d6a5a1f689c7f5c975ce95610d127b90a29b00806b.jpg)

To get better information, we turn to rational approximation. A practical approach is to use ratinterp to compute rational linearized least-squares approximations of $f$ in $[ - 1 , 1 ]$ . Specifically, suppose we take $r$ to be the type $( 7 , 8 )$ approximation to $f$ in 1000 Chebyshev points and draw the same contour plots as before. The picture changes completely, showing very impressive agreement over most of the range plotted. This is the power and the promise of rational approximation.

d = domain(-1,1);   
[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,7,8,1000); $\mathbf { r } \mathbf { r } ~ = ~ \mathbf { r } \left( { \bf z } { \bf z } \right)$ ; subplot(1,2,1), contour(x,y,abs(ff),lev1,'k'), hold on contour(x,y,abs(ff),lev2,'r')   
subplot(1,2,2), contour(x,y,abs(rr),lev1,'k'), hold on contour(x,y,abs(rr),lev2,'r')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/a2e22e6021bf581acff7c45ce58c23f10b19fa5be049f34363b77383d9206149.jpg)

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/f56962bce9da3e4c02fb137c3d8d7ab3aeb79d774a0995a3a226fe0db100b517.jpg)

For a direct measure of the accuracy of $r$ as an approximation to $f$ , we can look at $| f ( z ) - r ( z ) |$ . In the following plot the contours, from bottom to top, lie at $1 0 ^ { - 1 4 } , 1 0 ^ { - 1 2 } , \textrm { -- } , 1 0 ^ { - 2 }$ . Evidently the approximation is excellent over a wide region.

$\mathtt { l e v e l s \ = \ 1 0 \_ \hat { \ } ( - 1 4 : 2 : - 2 ) }$ ; contour(x,y,abs(ff-rr),levels,'k')

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/4a72e9fc14d019edb8529a1a25f24d4fd6c07b57513344bee9a57ef31d516c6a.jpg)

Results like these become all the more remarkable when one recalls that the problem of analytic continuation is ill-posed: analytic continuations are unique, but they do not depend continuously on the data. For example, the following observation shows the ill-posedness of the problem of continuing a function analytically from the interval $( - 1 , 1 )$ to the unit disk. If $f$ is analytic in the disk, then for any $\varepsilon > 0$ , there is another function $g$ analytic in the disk such that $\| f - g \| \ge 1$ on the disk and yet $\| f - g \| \leq \varepsilon$ on the interval. (Proof: Perturb $f$ by $\varepsilon \sin ( M z )$ for a suitable value of $M$ .) Because of this ill-posedness, every successful example of numerical analytic continuation must entail some smoothness assumptions about $f$ , whether implicit or explicit. That is to say, numerical analytic continuation always involves some kind of regularization. (A standard reference on this subject is [Hansen 1998].) In the computations just shown, the regularization is introduced by the use of the SVD in ratinterp.

The question with which we opened the discussion was, Where are the poles of $\operatorname { t a n h } ( z )$ ? To experiment with this, let us now apply ratinterp to compute approximants of types $( 2 , 2 ) , ( 3 , 3 ) , \dots , ( 8 , 8 )$ , and examine the poles of these approximations. In the next output, following the convention of the past few chapters, $( m , n )$

represents the permitted type of each approximant and $( \mu , \nu )$ the exact type, with $\mu \leq m$ and $\nu \leq n$ . Note that $( \mu , \nu )$ always comes out in the form (odd, even), because $f$ is an odd function. Thus there are always an even number of poles, which come in complex conjugate pairs and are pure imaginary, and we print just their positive imaginary parts.

for $\texttt { n } = \texttt { 2 } : 8$ [p,q,r,mu,nu,poles] $=$ ratinterp(d,f,n,n,1000);fprintf $( \cdot \setminus \mathrm { n } \left( \mathrm { m } , \mathrm { n } \right) = \left( \% \mathrm { d } , \% \mathrm { d } \right)$ , (mu,nu) $=$ (%d,%d):\n',n,n,mu,nu)yi $=$ sort(imag(poles)); fprintf('%15.10fi',yi(yi>0))  
end  
$( { \mathfrak { m } } , { \mathfrak { n } } ) = ( 2 , 2 )$ , $( \mathtt { m u } , \mathtt { n u } ) = ( 1 , 2 ) :$ 1.8048291471i  
$( \mathrm { m } , \mathrm { n } ) = ( 3 , 3 ) , ( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } ) = ( 3 , 2 ) :$ 1.5884736641i  
$( \mathrm { m } , \mathrm { n } ) = ( 4 , 4 ) , ( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } ) = ( 3 , 4 ) :$ 1.5716968677i 6.6346803797i  
$( \mathrm { m } , \mathrm { n } ) = ( 5 , 5 ) , ( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } ) = ( 5 , 4 ) :$ 1.5708250772i 5.0809800411i  
$( \mathtt { m } , \mathtt { n } ) = ( 6 , 6 )$ , $( \mathtt { m u } , \mathtt { n u } ) = ( 5 , 6 )$ :1.5707969475i 4.7823014265i 13.7250545528i  
$( \mathtt { m } , \mathtt { n } ) = ( 7 , 7 )$ , $( \mathtt { m u } , \mathtt { n u } ) = ( 7 , 6 )$ :1.5707963365i 4.7228280448i 9.4123430302i  
$( \mathtt { m } , \mathtt { n } ) = ( 8 , 8 )$ , (mu,nu)=(7,8):1.5707963258i 4.7123498987i 8.2068730934i 22.4267991875i

The table shows that for larger values of $( m , n )$ , two of the poles lie near $1 . 5 7 0 7 9 6 3 i$ and $4 . 7 1 i$ . We compare these with the actual first three poles of $\operatorname { t a n h } ( z )$ in the upper half-plane:

fprintf('%15.10fi',(pi/2) $^ *$ [1 3 5])

Exact poles:

1.5707963268i 4.7123889804i 7.8539816340i

Evidently the type $( 7 , 8 )$ approximation has captured the first two poles to 9 and 3 digits of accuracy, respectively, numbers that are consistent with the contour levels near $z = 1 . 5 7 i$ and $4 . 7 1 i$ in the last contour plot.

To understand computations like this, it is important to recognize that the “goal” of $r$ is not to find the poles of $f$ , but simply to approximate $f$ over $[ - 1 , 1 ]$ . If $r$ turns out to have poles near those of $f$ , this is a by-product, a side effect that happened because placing poles there is an effective strategy for approximation.15

To illustrate this, suppose we compare the type $( 7 , 8 )$ approximation above to one of type (15, 8). One might expect that with more degrees of freedom, the new approximation would capture the first pole more accurately. In fact, the approximation returned has exact type $( 1 5 , 2 )$ , and the accuracy of the pole has deteriorated, because the denominator is less important to the quality of the least-squares approximation:

[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,15,8,1000); fprintf $\therefore \ln ( \ln , \mathbf { n } ) = ( 1 5 , 8 )$ , (mu,nu) $=$ (%d,%d):\n',mu,nu) yi $=$ sort(imag(poles)); fprintf('%15.10fi',yi(yi>0))

$( \mathtt { m } , \mathtt { n } ) = ( 1 5 , 8 )$ , (mu,nu) $=$ (15,2): 1.5707964024i

If we go further and ask for a type (35, 8) approximant, ratinterp returns an approximation with no poles at all. The numerator now provides so much flexibility for the least-squares problem that the degrees of freedom in the denominator are not needed in 16-digit arithmetic, putting us back in the situation of the Chebfun ellipse of the first plot of this chapter.

[p,q,r,mu,nu,poles] $=$ ratinterp(d,f,35,8,1000); fprintf $\therefore \ln ( \ln , \mathbf { n } ) = ( 3 5 , 8 )$ , (mu,nu) $=$ (%d,%d):\n',mu,nu)

$$
\left( \mathrm { m } , \mathrm { n } \right) = \left( 3 5 , 8 \right) , \left( \mathrm { m } \mathrm { u } , \mathrm { n } \mathrm { u } \right) = \left( 2 5 , 0 \right) :
$$

One must always bear this in mind when using rational approximations for extrapolation: increasing $m$ and/or $n$ does not always improve the accuracy of the quantities one cares about.

One way to get an idea of the dependence of an approximation on $m$ and $n$ is to print a table of digits of accuracy. The following table, for example, indicates the number of digits of accuracy in the computed first pole of $\operatorname { t a n h } ( z )$ for $m =$ $1 , 3 , 5 , \ldots , 1 9$ and $n = 2 , 4 , 6 , \dots , 2 0$ , all based on robust least-squares fits in 200 Chebyshev points in 16-digit arithmetic. The table shows again the effect that increasing $m$ beyond a certain small value—moving right in the table—diminishes the accuracy of the pole.

err $=$ zeros(1,10);   
for $\texttt { n } = \texttt { 2 : 2 : 2 0 }$ for $\texttt { m } = \texttt { 1 : 2 : 1 9 }$ [p,q,r,mu,nu,poles] $=$ ratinterp(d,f,m,n,200); $\mathtt { p 1 } \ =$ imag(poles(abs(poles-1.6i) $= =$ min(abs(poles-1.6i)))); err((m+1)/2) $=$ -round(log10(abs(p1-pi/2))); end fprintf('%3d',err)   
end

<table><tr><td>DIGITS</td><td>OF 3</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>ACCURACY:LEAST-SQUARES 7</td></tr><tr><td>1 1</td><td>2 3</td><td>5</td><td>6</td><td>7 8</td><td>8</td><td>7</td><td></td></tr><tr><td>2</td><td>4</td><td>6 8</td><td>9</td><td>8</td><td>8 7</td><td></td><td></td></tr><tr><td>2</td><td>5</td><td>8</td><td>9 9</td><td>8</td><td>8</td><td>7</td><td></td></tr><tr><td>3</td><td></td><td>9</td><td>9 9</td><td>8</td><td></td><td>7</td><td></td></tr><tr><td>4</td><td></td><td>9</td><td>9</td><td>9 8</td><td>8</td><td>7</td><td></td></tr><tr><td>4</td><td>87</td><td>9</td><td>9 9</td><td>8</td><td>8</td><td>7</td><td></td></tr><tr><td>5</td><td>7</td><td>9</td><td>9 9</td><td>8</td><td>8</td><td>7</td><td></td></tr><tr><td>5</td><td>7</td><td></td><td>9 9</td><td>8</td><td></td><td>7</td><td>7</td></tr><tr><td>5</td><td>7</td><td>9 9</td><td>9 9</td><td>8</td><td>8 8</td><td>8 7</td><td>7</td></tr></table>

The use of rational approximations for locating poles or other singularities has an honorable history. Many applications are mentioned in the monograph by Baker and Graves-Morris [1996], which is a standard reference on Pad´e approximation. One interesting kind of application is to locating singularities of solutions of ODEs or PDEs computed numerically, an idea explored by Weideman, among others [2003]. For Chebfun-based explorations, including the application of ratinterp to find complex singularities of solutions to the Lorenz and Lotka–Volterra equations, see [Pach´on 2010] and [Webb 2013].

Having just mentioned Pad´e approximation, which was the subject of the last chapter, let us now turn to this alternative method of constructing rational approximations. Here is a repetition of the last experiment, the table of digits of accuracy in the first pole of $\operatorname { t a n h } ( z )$ , but now based on Pad´e approximation instead of rational least-squares. The results are similar, but better. This is not a general conclusion: it depends on the problem.

for $\texttt { n } = \texttt { 2 : 2 : 2 0 }$ for $\texttt { m } = \texttt { 1 : 2 : 1 9 }$ [r,a,b,mu,nu,poles] $=$ padeapprox(f,m,n); $\mathtt { p 1 } \ =$ imag(poles(abs(poles-1.57i) $\mathbf { \partial } = = \mathbf { \partial }$ min(abs(poles-1.57i)))); err((m+1)/2) $=$ -round(log10(abs(p1-pi/2))); end fprintf('%3d',err)   
end

<table><tr><td colspan="2"></td><td>DIGITS</td><td>4</td><td colspan="2">OF ACCURACY:PADE</td></tr><tr><td>1</td><td>2</td><td>3</td><td>5 6</td><td>7 8</td><td>9 10 13 13</td></tr><tr><td>2</td><td>3</td><td>5</td><td>6 8</td><td>9 11</td><td>12</td></tr><tr><td>2</td><td>5</td><td>7</td><td>9 10</td><td>12 15</td><td>11 12 13</td></tr><tr><td>3</td><td>6</td><td>8</td><td>11 13</td><td>14 12</td><td>15 11 12</td></tr><tr><td>3</td><td>7</td><td>10</td><td>12</td><td>14 13 14</td><td>12 15 11</td></tr><tr><td>4</td><td>8</td><td>12</td><td>14 12</td><td>14 13</td><td>14 12 15</td></tr><tr><td>5</td><td>9</td><td>13</td><td>12 14</td><td>12 14</td><td>13 14 12</td></tr><tr><td>5</td><td>11</td><td>11</td><td>13 12</td><td>14 12</td><td>14 13 14</td></tr><tr><td>6</td><td>12</td><td>11</td><td>11 13</td><td>12 14</td><td>12 14 13</td></tr><tr><td>612</td><td></td><td>12</td><td>11 11</td><td>13 12</td><td>14 12 14</td></tr></table>

In principle, least-squares fitting and Pad´e approximation are very different techniques, since the first uses function values only at many different points, whereas the second uses values of the function and its derivatives at a single point. (These are the extreme cases of the general notion of multipoint Pad´e approximation.) In our actual computation, however, the difference is diminished, because padeapprox begins by computing Taylor coefficients numerically by the FFT based on samples of the function at roots of unity, a standard technique. So in fact, in this comparison, ratinterp and padeapprox both work from function values: the first from samples on $[ - 1 , 1 ]$ , the second from samples on the unit circle. This raises the question, What is achieved by passing through the intermediate stage of Taylor coefficients? It is a fair point, and indeed, another effective approach would be to solve a rational least-squares problem on the circle directly as in Chapter 26. Explorations of this kind are presented in [Pach´on 2010].

We now turn to the topic of acceleration of convergence of sequences and series. The challenge here is as follows. Suppose we know some of the initial terms of a convergent sequence,

$$
s _ { 0 } , s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . \to S ,
$$

and we want to estimate the limit $S$ . Equivalently, suppose we wish to estimate the limit of an infinite sum,

$$
S = a _ { 0 } + a _ { 1 } + a _ { 2 } + \cdots .
$$

The two problems are equivalent since we may regard (28.1) as a sequence of partial sums,

$$
s _ { n } = \sum _ { k = 0 } ^ { n } a _ { k } , \quad a _ { k } = s _ { k + 1 } - s _ { k } .
$$

If the sequence or series converges slowly, how might we speed it up? For example, perhaps we can afford to compute 20 terms, but this gives just 2-digit accuracy. Can we process the data further somehow to improve the accuracy to 6 digits?

There is a long history to such questions, reaching from Stirling and Euler to the recent tour de force solution of nine of the ten “SIAM 100-Digit Challenge” problems to 10000 digits of accuracy [Bornemann et al. 2004]. It is probably fair to say that almost every method for accelerating convergence is based on the idea of embedding the sequence in an analytic function, though this may not be how the original authors conceived or described their method.

One way in which a sequence might be embedded in an analytic function is if the terms of the sequence can be regarded as values of a fixed function at different arguments. For example, suppose we define a function $f ( z )$ at the points $z =$ $1 , 2 ^ { - 1 } , 2 ^ { - 2 } , \ldots$ by the formula $f ( 2 ^ { - k } ) = s _ { k }$ . Then (28.1) becomes

$$
f ( 1 ) , f ( 2 ^ { - 1 } ) , f ( 2 ^ { - 2 } ) , . . . \to S .
$$

Does this point of view help us estimate $S$ ? The answer will probably be yes if there exists a function $f$ that is analytic in a neighborhood of $z = 0$ and takes the given values at $z = 2 ^ { - k }$ . In such a case, to estimate $S$ , it is enough to interpolate some of the data by a polynomial $p ( z )$ and then compute $p ( 0 )$ . This is the method known as Richardson extrapolation, which is of great practical importance in applications.16 In a typical application, $h$ might be the mesh size of a numerical discretization and $f ( h ) , f ( h / 2 ) , f ( h / 4 ) , \ldots$ the estimates obtained of a quantity of interest as the mesh is successively refined. Often only even powers of $h$ appear, indicating that $f$ is an even function, so one could take the view that the data are given at $\pm h , \pm h / 2 , \ldots$ and Richardson extrapolation is really Richardson interpolation. In the specific case in which $f ( h )$ is an estimate of an integral by the trapezoidal or rectangle rule with step length $h$ , this becomes the quadrature method known as Romberg quadrature. Nor is the idea of polynomial extrapolation from data such as (28.4) limited to cases in which the sample points are related by factors of 2. If they are $1 , 1 / 2 , 1 / 3 , \ldots$ , this is called Salzer extrapolation [Salzer 1955].

Often, however, the limit of a sequence or series is not in the interior of a region of analyticity of an analytic function. In such a case there may be less mileage in Richardson extrapolation, and one looks for formulations adapted to the edge of a region of analyticity. For such problems, there is a basic starting point: to insert a parameter $z$ in (28.2) so that it becomes the series

$$
S ( z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdots .
$$

Now we have the problem of evaluating $S ( 1 )$ for a function $S ( z )$ with known Taylor coefficients. If (28.2) converges, then $z = 1$ is a point of convergence of (28.5), and if (28.2) converges more slowly than geometrically, then $z = 1$ must be on the boundary of the disk of convergence of (28.5). So by introducing a parameter $z$ , we have converted the problem of the summation of a slowly convergent series to a problem of evaluating an analytic function at a point on the boundary of the disk of convergence of its Taylor series.

The simplest idea would be to evaluate $S ( z )$ for a succession of values of $z$ and use the identity

$$
S ( 1 ) = \operatorname* { l i m } _ { z \to 1 } S ( z ) ,
$$

where the limit is over real values of $z$ increasing to 1. This idea is known as Abel summation [Hardy 1991].

A more powerful and general approach is to use rational functions, specifically Pad´e approximants since the data are given as Taylor coefficients. Two variants of this idea have received special attention. We could construct a sequence of type $( m , 1 )$ Pad´e approximants, with one pole, and evaluate them at $z = 1$ :

$$
r _ { 0 1 } ( 1 ) , r _ { 1 1 } ( 1 ) , r _ { 2 1 } ( 1 ) , \ldots .
$$

This is called Aitken extrapolation or Aitken’s $\Delta ^ { 2 }$ method, used by Aitken [1926], though with origins further back. Or we could work with type $( n , n )$ Pad´e approximants,

$$
r _ { 0 0 } ( 1 ) , r _ { 1 1 } ( 1 ) , r _ { 2 2 } ( 1 ) , \ldots .
$$

This is called epsilon extrapolation (originally for sequences) [Shanks 1955, Wynn 1956] or eta extrapolation (originally for series) [Bauer 1959]. An earlier appearance of essentially the same idea is due to Schmidt [1941].

Here is an example showing how powerful eta extrapolation can be for some problems. What is the value of

$$
S = \sum _ { n = 2 } ^ { \infty } { \frac { \sin ( n ) } { \log ( n ) } } ?
$$

The series is extremely slow to converge, as we see by taking partial sums of as many as a million terms:

${ \sf S } = \mathbb { Q } \left( { \sf { n } } \right)$ sum(sin(2:n)./log(2:n));for $\texttt { n } = \texttt { 1 0 . \hat { } } [ 1 : 6 ]$ , fprintf('%6.1e %12.6f\n',n,S(n)), end

<table><tr><td>n</td><td>S(n)</td></tr><tr><td>1.0e+01</td><td>0.907319</td></tr><tr><td>1.0e+02</td><td>0.457822</td></tr><tr><td>1.0e+03</td><td>0.669234</td></tr><tr><td>1.0e+04</td><td>0.761940</td></tr><tr><td>1.0e+05</td><td>0.764913</td></tr><tr><td>1.0e+06</td><td>0.609190</td></tr></table>

To get 10-digit accuracy by summing the series in this fashion, we would need $1 0 ^ { 1 0 0 0 0 0 0 0 0 0 0 }$ terms! The actual answer (not known analytically) is

$$
S \approx 0 . 6 8 3 9 1 3 7 8 6 4 1 8 2 8 \ldots
$$

Here are the diagonal extrapolants, that is, the results of eta extrapolation. Now we just go from $2 ^ { 1 }$ to $2 ^ { 6 }$ instead of from $1 0 ^ { 1 }$ to $1 0 ^ { 6 }$ , yet we get 14 digits of accuracy instead of 1:

$\mathtt { \Delta 1 } ~ = ~ 2 { : } 1 5 0$ ; c = [0 0 sin(n)./log(n)];   
for $\textbf { n } = \ 2 . \hat { \ } ( 1 { : } 6 )$ [r,a,b,mu,nu] $=$ padeapprox(c,n,n,0); fprintf(' (%2.0d,%2.0d) (%2.0d,%2.0d) %19.15f\n',n,n,mu,nu,r(1))   
end

<table><tr><td>n,n) (mu,nu) （ 2，2) (2，2) (4，4) (4，4) （8,8) (8,8) (16,16) (16,16) (32,32) (32,32)</td><td>r_nn(1) 0.987966950435009 0.716844624573063 0.684142517808568 0.683915162212272 0.683913786418312</td></tr></table>

The convergence is excellent. Note that we have computed Pad´e approximants nonrobustly by specifying a tolerance of 0 to padeapprox. In typical applications, this use of nonrobust formulas seems advantageous in extrapolation applications, though it brings a risk of sensitivity to noise. For this example, calling padeapprox with its default tolerance $1 0 ^ { - 1 4 }$ leads to stagnation at type (15, 15) with just 7 digits of accuracy.

This simple method of eta extrapolation, at least as implemented by the Chebfun Pad´e approximation code, can be encapsulated in a single MATLAB command we may call extrap. Given a sequence $a _ { 0 } , a _ { 1 } , \dotsc , a _ { N }$ , we can round $N / 2$ to integers (say, round up for $m$ and down for $_ { n }$ ) and then use padeapprox to compute the type $( m , n )$ Pad´e approximation $r$ . The accelerated value is then $r ( 1 )$ . Here is the code.

$\begin{array} { l } { { \tt e v a l \_ a t \_ 1 } = \ { \tt o } \left( { \tt r } \right) { \tt r } \left( 1 \right) ; { \tt N } 2 = \ { \tt O } \left( { \tt c } \right) { \tt 1 } { \tt e n g t h } \left( { \tt c } \right) / 2 ; } \end{array}$ extrap $=$ @(c) eval_at_1(padeapprox(c,ceil(N2(c)),floor(N2(c)),0));

The $\sin ( n ) / \log ( n )$ example just treated is this:

extrap([0 0 sin(2:150)./log(2:150)])

ans $=$ 0.683913786418279

For another example, suppose we extrapolate the alternating series

$$
1 - { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } - \cdot \cdot \cdot = \log ( 2 ) .
$$

The result is accurate to machine precision:

$$
\mathtt { \cdot t r a p } ( ( - 1 ) \cdot \hat { \mathbf { \alpha } } ^ { \hat { } } ( 0 : 3 0 ) \cdot / ( 1 : 3 1 ) ) , \mathtt { \ e x a c t } \ = \ \log ( 2 )
$$

ans = 0.693147180559945   
exact = 0.693147180559945

Note that here, the function $f$ of (28.5) is $\log ( 1 + z )$ , so this example shows that eta extrapolation can be effective for functions with branch cuts as well as poles.

Another famous alternating series, which we can obtain by setting $t = 0$ in (9.3), is

$$
1 - { \frac { 1 } { 3 } } + { \frac { 1 } { 5 } } - \cdot \cdot \cdot = { \frac { \pi } { 4 } } .
$$

Again, extrapolation gives machine precision:

extrap((-1).^(0:30)./(1:2:61)), exact = pi/4

ans $=$ 0.785398163397447   
exact $=$ 0.785398163397448

These examples are very impressive, but it is not always so. For example, here is what happens if we attempt to extrapolate the series

$$
\zeta ( 2 ) = 1 + { \frac { 1 } { 2 ^ { 2 } } } + { \frac { 1 } { 3 ^ { 2 } } } + \cdots = { \frac { \pi ^ { 2 } } { 6 } } ,
$$

extrap(1./(1:30).^2), exact = pi^2/6

ans $=$ 1.640824460821040   
exact $=$ 1.644934066848226

The convergence is very poor because in this case the function $f ( z )$ of (28.5), known as the dilogarithm, has a branch point at $z = 1$ itself. As it happens, this is a case where Salzer extrapolation is effective (Exercise 28.3).

The discussion of convergence acceleration of the last five pages has little in common with the large literature of this subject, because our focus has been solely on the underlying approximations, particularly Pad´e approximants, and not at all on the mechanics. Our numerical illustrations have utilized the linear algebra of Chapter 27, based on the SVD and requiring $O ( n ^ { 3 } )$ floating point operations to compute a single estimate based on a type $( n , n )$ approximant. The literature of convergence acceleration is quite different, for it emphasizes recurrence relations and triangular or rhomboidal arrays related to continued fractions that can be used to generate a sequence of approximations at great speed without solving matrix problems. These approaches are certainly faster, though they come with a risk of sensitivity to noise and the possibility of breakdown if there is a division by 0.

A major reason why we have ignored the mechanical or implementational aspects of convergence acceleration is that these matters are complicated—and, one might say, distracting. The differences between various extrapolation algorithms in practice can be quite intricate, and in a discussion of such matters, one quickly loses sight of the underlying mathematics of approximation. For details of these aspects of convergence acceleration see surveys such as Chapter 3 of [Baker & Graves-Morris 1996], [Brezinski & Redivo Zaglia 1991], [Gragg 1972], [Joyce 1971], [Sidi 2003], [Weniger 1989], [Wimp 1981], or the appendix by Laurie in [Bornemann et al. 2004]. Such literature also points to many further acceleration methods beyond those we have mentioned, such as Levin’s sequence transformation and Brezinski’s theta method.

We finish with an observation that points to exciting further territories of interest to mathematicians at least since Euler. The series (28.5) consists just of Taylor coefficients, so it is meaningful even if the radius of convergence is less than 1. Therefore our methods based on analytic continuation can sum divergent series as well as convergent ones. For example, the Taylor series

$$
{ \frac { 1 } { 1 + z } } = 1 - z + z ^ { 2 } - z ^ { 3 } + \cdot \cdot \cdot
$$

suggests the result

$$
1 - 1 + 1 - 1 + \cdot \cdot = { \frac { 1 } { 2 } }
$$

if we set $z = 1$ . Similarly, setting $z = 2$ suggests

$$
1 - 2 + 4 - 8 + \cdot \cdot \cdot = { \frac { 1 } { 3 } } .
$$

Are these identities “correct”? As usual in mathematics, the answer depends on what definitions we choose. The formulas (28.9) and (28.10) are not too problematic since they correspond to Taylor series with positive radii of convergence. In more challenging cases, the series is only asymptotic. For example, what about this series with factorial coefficients considered by Euler [1760],

$$
0 ! - 1 ! + 2 ! - 3 ! + \cdot \cdot = ?
$$

The factorials grow too fast to be Taylor coefficients for any function analytic in a neighborhood of $z = 0$ . However, they are the asymptotic series coefficients at $z = 0$ for a function analytic in the right half-plane, namely

$$
f ( z ) = \int _ { 0 } ^ { \infty } { \frac { e ^ { - t } } { 1 + z t } } d t .
$$

So a plausible candidate for the sum of (28.11), as suggested by Euler, is

$$
0 ! - 1 ! + 2 ! - 3 ! + \dots = f ( 1 ) = 0 . 5 9 6 3 4 7 3 6 2 \dots . . .
$$

Our code extrap makes a creditable attempt at computing this number:

extrap((-1).^(0:10).\*factorial(0:10))

ans $=$ 0.593294558846647

Summary of Chapter 28. Rational approximations provide one of the basic technologies for analytic continuation and extrapolation. In particular, Pad´e approximants are the basis of standard methods of convergence acceleration for sequences and series including the Aitken $\Delta ^ { 2 }$ , Shanks, epsilon, and eta methods.

Exercise 28.1. Contour plot for Taylor polynomials. Draw a contour plot like the pair in this chapter for the Taylor polynomial approximants to $f ( z ) = \operatorname { t a n h } ( z )$ . Comment on the result.

Exercise 28.2. The divergent factorial series. Compute numerically the Pad´e approximants $r _ { 3 3 } , r _ { 4 4 } , \ldots , r _ { 7 7 }$ for the Taylor coefficients (28.11), and show that they match $f ( 1 )$ to better than $1 \%$ , where $f$ is defined by (28.12). What accuracy do these approximants give for $f ( 1 / 2 )$ ?

Exercise 28.3. Zeta function. It was noted in the text that eta extrapolation is ineffective for the series (28.8). Study the behavior of Richardson and Salzer extrapolation instead.

Exercise 28.4. Alternating square roots. (a) To 8 digits of accuracy, what do you think is the limit of $1 - 1 / \sqrt { 2 } + 1 / \sqrt { 3 } - \cdot \cdot \cdot ?$ (b) To the same accuracy, what number would you propose as a good choice for the sum of the divergent series $1 - { \sqrt { 2 } } + { \sqrt { 3 } } - \dots ?$

Exercise 28.5. Approximations to $e ^ { z }$ . Compute type $( 1 , 1 )$ approximations to $e ^ { z }$ on $[ - 1 , 1 ]$ by (a) Pad´e approximation, (b) best approximation, (c) Chebyshev–Pad´e approximation, (d) Carath´eodory–Fej´er approximation, (e) interpolation in 3 Chebyshev points, and (f) linearized least-squares approximation in a number of Chebyshev points large enough to be effectively infinite. In each case list the coefficients, measure the $L ^ { 2 }$ and $L ^ { \infty }$ errors, and plot the error curve.

Exercise 28.6. Nonlinear least-squares approximation. Find a way to compute the true type $( 1 , 1 )$ nonlinear least-squares approximation to $e ^ { z }$ on $[ - 1 , 1 ]$ , and report the same data for this function as for the approximations of Exercise 28.7.

Exercise 28.7. An alternating series. The following identity is known:

$$
1 + { \frac { 1 } { 2 } } - { \frac { 1 } { 3 } } - { \frac { 1 } { 4 } } + { \frac { 1 } { 5 } } + { \frac { 1 } { 6 } } - { \frac { 1 } { 7 } } - \cdots = { \frac { \pi } { 4 } } + { \frac { 1 } { 2 } } \log 2 .
$$

How many digits do you get by taking $1 0 ^ { 1 } , 1 0 ^ { 2 } , \dots , 1 0 ^ { 6 }$ terms of the series? Can you get more by extrapolation?

# Appendix A. Six Myths of Polynomial Interpolation and Quadrature

[This article was first published by the Institute of Mathematics and Its Applications (www.ima.org.uk): L. N. Trefethen (2012), Six myths of polynomial interpolation and quadrature, Mathematics Today 47, no. 4, 184–188.]

It is a pleasure to offer this essay for Mathematics Today as a record of my Summer Lecture on 29 June 2011 at the Royal Society.

Polynomials are as basic a topic as any in mathematics, and for numerical mathematicians like me, they are the starting point of numerical methods that in some cases go back centuries, like quadrature formulas for numerical integration and Newton iterations for finding roots. You would think that by now, the basic facts about computing with polynomials would be widely understood. In fact, the situation is almost the reverse. There are indeed widespread views about polynomials, but some of the important ones are wrong, founded on misconceptions entrenched by generations of textbooks.

Since 2006, my colleagues and I have been solving mathematical problems with polynomials using the Chebfun software system (www.chebfun.org). We have learned from daily experience how fast and reliable polynomials are. This entirely positive record has made me curious to try to pin down where these misconceptions come from, and this essay is an attempt to summarize some of my findings.

The essay is organised around “six myths.” Each myth has some truth in it— mathematicians rarely say things that are simply false! Yet each one misses something important.

Throughout the discussion, $f$ is a continuous function defined on the interval $[ - 1 , 1 ]$ , $n + 1$ distinct points $x _ { 0 } , \ldots , x _ { n }$ in $[ - 1 , 1 ]$ are given, and $p _ { n }$ is the unique polynomial of degree at most $n$ with $p _ { n } ( x _ { j } ) ~ = ~ f ( x _ { j } )$ for each $j$ . Two families of points will be of particular interest: equispaced points, $x _ { j } = - 1 + 2 j / n$ , and Chebyshev points, $x _ { j } = \cos ( j \pi / n )$ . I will also mention Legendre points, defined as the zeros of the degree $n + 1$ Legendre polynomial $P _ { n + 1 }$ .

The discussion of each myth begins with two or three representative quotations from leading textbooks, listed anonymously with the year of publication. Then I say a word about the mathematical truth underlying the myth, and after that, what that truth overlooks.

# Myth 1. Polynomial interpolants diverge as $n \to \infty$

Textbooks regularly warn students not to expect $p _ { n } \to f$ as $n \to \infty$ “Polynomial interpolants rarely converge to a general continuous function.” (1989)

“Unfortunately, there are functions for which interpolation at the Chebyshev points fails to converge.” (1996)

On the face of it, this caution is justified by two theorems. Weierstrass proved in 1885 that any continuous function can be approximated arbitrarily closely by polynomials. On the other hand, Faber proved in 1914 that no polynomial interpolation scheme, no matter how the points are distributed, will converge for all such functions.

So it sounds as if there is something wrong with polynomial interpolation. Yet the truth is, polynomial interpolants in Chebyshev points always converge if $f$ is $a$ little bit smooth. (We shall call them Chebyshev interpolants.) Lipschitz continuity is more than enough, that is, $| f ( x ) - f ( y ) | \leq L | x - y |$ for some constant $L$ and all $x , y \in [ - 1 , 1 ]$ . So long as $f$ is Lipschitz continuous, as it will be in almost any practical application, $p _ { n } \to f$ is guaranteed.

There is indeed a big problem with convergence of polynomial interpolants, but it pertains to interpolation in equispaced points. As Runge showed in 1901, equispaced interpolants may diverge exponentially, even if $f$ is so smooth as to be analytic (holomorphic). This genuinely important fact, known as the Runge phenomenon, has confused people. With Faber’s theorem seeming to provide justification, a real problem with equispaced polynomial interpolants has been overgeneralized so that people have suspected it of applying to polynomial interpolants in general.

The smoother $f$ is, the faster its Chebyshev interpolants converge. If $f$ has $\nu$ derivatives, with the $\nu$ th derivative being of bounded variation $V$ , then $\| f - p _ { n } \| =$ $O ( V n ^ { - \nu } )$ as $n  \infty$ . (By $\| f - p _ { n } \|$ I mean the maximum of $| f ( x ) - p _ { n } ( x ) |$ for $x \in [ - 1 , 1 ]$ .) If $f$ is analytic, the convergence is geometric, with $\| f - p _ { n } \| = O ( \rho ^ { - n } )$ for some $\rho > 1$ . I will give details about the parameter $\rho$ under Myth 5.

For example, here is the degree 10000 Chebyshev interpolant $p _ { n }$ to the sawtooth function $f ( x )$ defined as the integral from $^ { - 1 }$ to $x$ of $\mathrm { s i g n } ( \sin ( 1 0 0 t / ( 2 - t ) )$ ). This curve may not look like a polynomial, but it is! With $\| f - p _ { n } \| \approx 0 . 0 0 0 1$ , the plot is indistinguishable from a plot of $f$ itself.

$$
\int M M M \min
$$

There is not much use in polynomial interpolants to functions with so little smoothness as this, but mathematically they are trouble free. For smoother functions like $e ^ { x }$ , $\cos ( 1 0 x )$ or $1 / ( 1 + 2 5 x ^ { 2 } )$ , we get convergence to 15 digits of accuracy for small values of $n$ (14, 34, and 182, respectively).

# Myth 2. Evaluating polynomial interpolants numerically is problematic

Interpolants in Chebyshev points may converge in theory, but aren’t there problems on a computer? Textbooks warn students about this.

“Polynomial interpolation has drawbacks in addition to those of global convergence. The determination and evaluation of interpolating polynomials of high degree can be too time-consuming and can also lead to difficulty problems associated with roundoff error.” (1977)

“Although Lagrangian interpolation is sometimes useful in theoretical investigations, it is rarely used in practical computations.” (1985)

“Interpolation is a notoriously tricky problem from the point of view of numerical stability.” (1990)

The origin of this view is the fact that some of the methods one might naturally try for evaluating polynomial interpolants are slow or numerically unstable or both. For example, if you write down the Lagrange interpolation formula in its most obvious form and implement it on a computer as written, you get an algorithm that requires $O ( n ^ { 2 } )$ work per evaluation point. (Partly because of this, books warn readers that they should use Newton interpolation formulas rather than Lagrange— another myth.) And if you compute interpolants “linear algebra style” by setting up a Vandermonde matrix whose columns contain samples of $1 , x , x ^ { 2 } , \ldots , x ^ { n }$ at the grid points, your numerical method is exponentially unstable. This is the “polyval/polyfit” algorithm of MATLAB, and I am guilty of propagating Myth 2 myself by using this algorithm in my textbook Spectral Methods in MATLAB. Rounding errors on a computer destroy all accuracy of this method even for $n = 6 0$ , let alone $n = 1 0 0 0 0$ as in the plot above.

Or how about $n = 1$ ,000,000? Here is a plot of the polynomial interpolant to $f ( x ) = \sin ( 1 0 / x )$ in a million Chebyshev points. The plot was obtained in about 30 seconds on my laptop by evaluating the interpolant at 2000 points clustered near zero.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/162d2e5dae70ccdf319789bcd980fe9124166566fef0af4445294e145a7058ec.jpg)

The fast and stable algorithm that makes these calculations possible comes from a representation of the Lagrange interpolant known as the barycentric formula, published by Salzer in 1972:

$$
p _ { n } ( x ) = { \sum _ { j = 0 } ^ { n } } ^ { \prime } { \frac { ( - 1 ) ^ { j } f _ { j } } { x - x _ { j } } } \Bigg / { \sum _ { j = 0 } ^ { n } } ^ { \prime } { \frac { ( - 1 ) ^ { j } } { x - x _ { j } } } ,
$$

with the special case $p _ { n } ( x ) = f _ { j }$ if $\boldsymbol { x } = \boldsymbol { x } _ { j }$ . The primes on the summation signs signify that the terms $j = 0$ and $j = n$ are multiplied by $1 / 2$ . The work required is $O ( n )$ per evaluation point, and though the divisions by $\boldsymbol { x } - \boldsymbol { x _ { j } }$ may look dangerous for $x \approx x _ { j }$ , the formula is numerically stable, as was proved by Nick Higham in 2004.

# Myth 3. Best approximations are optimal

This one sounds true by definition!

“Since the Remes algorithm, or indeed any other algorithm for producing genuine best approximations, requires rather extensive computations, some interest attaches to other more convenient procedures to give good, if not optimal, polynomial approximations.” (1968)

“Minimal polynomial approximations are clearly suitable for use in functions evaluation routines, where it is advantageous to use as few terms as possible in an approximation.” (1968)

“Ideally, we would want a best uniform approximation.” (1980)

Though the statement of this myth looks like a tautology, there is content in it. The “best approximation” is a common name for the unique polynomial $\boldsymbol { p } _ { n } ^ { * }$ that minimizes $\| f - p _ { n } ^ { * } \|$ . So a best approximant is optimal in the maximum norm, but is it really the best in practice?

As the first quotation suggests, computing $\boldsymbol { p } _ { n } ^ { * }$ is not a trivial matter, since the dependence on $f$ is nonlinear. By contrast, computing a Chebyshev interpolant with the barycentric formula is easy. Here our prejudices about value for money begin to intrude. If best approximations are hard to compute, they must be valuable!

Two considerations make the truth not so simple. First of all, the maximumnorm accuracy difference between Chebyshev interpolants and best approximations can never be large, for Ehlich and Zeller proved in 1966 that $\| f - p _ { n } \|$ cannot exceed $\| f - p _ { n } ^ { * } \|$ by more than the factor $2 + ( 2 / \pi ) \log ( n + 1 )$ . Usually the difference is less than that, and in fact the best known error bounds for functions that have $\nu$ derivatives or are analytic—the two smoothness classes mentioned under Myth 1— are just a factor of 2 larger for Chebyshev interpolants as for best approximations.

Secondly, according to the equioscillation theorem going back to Chebyshev in the 1850s, the maximum error of a best approximation is always attained at at least $n + 2$ points in $[ - 1 , 1 ]$ . For example, the black curve below is the error curve $f ( x ) - p _ { n } ^ { * } ( x )$ , $x \in [ - 1 , 1 ]$ , for the best approximant to $| x - 1 / 4 |$ of degree 100, equioscillating between 102 extreme values $\approx \pm 0 . 0 0 2 7$ . The red curve corresponds to the polynomial interpolant $p _ { n }$ in Chebyshev points. It is clear that for most values of $x$ , $| f ( x ) - p _ { n } ( x ) |$ is much smaller than $\left| f ( x ) - p _ { n } ^ { * } ( x ) \right|$ . Which approximation would be more useful in an application? I think the only reasonable answer is, it depends. Sometimes one really does need a guarantee about worst-case behavior. In other situations, it would be wasteful to sacrifice so much accuracy over 95% of the range just to gain one bit of accuracy in a small subinterval.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/8bc50a0f5e4b96ca11c50508e652aebb691db3daa1b3ff1dc5d0b9a0f06d297a.jpg)

# Myth 4. Gauss quadrature has twice the order of accuracy of Clenshaw–Curtis

Quadrature formulas are usually derived from polynomials. We approximate an integral by a finite sum,

$$
I = \int _ { - 1 } ^ { 1 } f ( x ) d x \quad \approx \quad I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) ,
$$

and the weights $\{ w _ { k } \}$ are determined by the principle of interpolating $f$ by a polynomial at the points $\{ x _ { k } \}$ and integrating the interpolant. Newton–Cotes quadrature corresponds to equispaced points, Clenshaw–Curtis quadrature to Chebyshev points, and Gauss quadrature to Legendre points. Almost every textbook first describes Newton–Cotes, which achieves ${ \boldsymbol { I } } _ { n } = { \boldsymbol { I } }$ exactly if $f$ is a polynomial of degree $n$ , and then shows that Gauss has twice this order of exactness: ${ { I } _ { n } } \mathrm { ~ = ~ } I$ if $f$ is a polynomial of degree $2 n + 1$ . Clenshaw–Curtis is occasionally mentioned, but it only has order of exactness $n$ , no better than Newton–Cotes.

“However, the degree of accuracy for Clenshaw–Curtis quadrature is only $n - 1$ .” (1997)

“Clenshaw–Curtis rules are not optimal in that the degree of an n-point rule is only $n - 1$ , which is well below the maximum possible.” (2002)

This ubiquitous emphasis on order of exactness is misleading. Textbooks suggest that the reason Gauss quadrature gives better results than Newton–Cotes is its higher order of exactness, but this is not correct. The problem with Newton–Cotes is that the sample points are equally spaced: the Runge phenomenon. In fact, as P´olya proved in 1933, Newton–Cotes quadrature does not converge as $n  \infty$ , in general, even if $f$ is analytic.

Clenshaw–Curtis and Gauss quadratures behave entirely differently. Both schemes converge for all continuous integrands, and if the integrand is analytic, the convergence is geometric. Clenshaw–Curtis is easy to implement, using either the Fast Fourier Transform or by an algorithm of Waldvogel in 2006, and one reason it gets little attention may be that Gauss quadrature had a big head start, invented in 1814 instead of 1960. Both Clenshaw–Curtis and Gauss quadrature are practical even if $n$ is in the millions, in the latter case because nodes and weights can be calculated by an algorithm implemented in Chebfun due to Glaser, Liu and Rokhlin in 2007. (Indeed, since Glaser–Liu–Rokhlin, it is another myth to imagine that Gauss quadrature is only practicable for small values of $n$ .)

With twice the order of exactness, we would expect Gauss quadrature to converge twice as fast as Clenshaw–Curtis. Yet it does not. Unless $f$ is analytic in a large region surrounding $[ - 1 , 1 ]$ in the complex plane, one typically finds that Clenshaw–Curtis quadrature converges at about the same rate as Gauss, as illustrated by these curves for $f ( x ) = \exp ( - 1 / x ^ { 2 } )$ :

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/6d9bb5af3a37051ca1ddc3ad6f6613f5ce3a4982085af7398e06ef38c270de3f.jpg)

A theorem of mine from 2008 makes this observation precise. If $f$ has a $\nu$ th derivative of bounded variation $V$ , Gauss quadrature can be shown to converge at the rate $O ( V ( 2 n ) ^ { - \nu } )$ , the factor of 2 reflecting its doubled order of exactness. The theorem asserts that the same rate $O ( V ( 2 n ) ^ { - \nu } )$ , with the same factor of 2, is also achieved by Clenshaw–Curtis. (Folkmar Bornemann (private communication) has pointed out that both of these rates can probably be improved by one further power of $n$ .)

The explanation for this surprising result goes back to O’Hara and Smith in 1968. It is true that $( n + 1 )$ -point Gauss quadrature integrates the Chebyshev polynomials $T _ { n + 1 } , T _ { n + 2 } , . . .$ exactly whereas Clenshaw–Curtis does not. However, the error that Clenshaw–Curtis makes consists of aliasing them to the Chebyshev polynomials $T _ { n - 1 } , T _ { n - 2 } , . . .$ and integrating these correctly. As it happens, the integrals of $T _ { n + k }$ and $T _ { n - k }$ differ by only $O ( n ^ { - 3 } )$ , and that is why Clenshaw–Curtis is more accurate than its order of exactness seems to suggest.

# Myth 5. Gauss quadrature is optimal

Gauss quadrature may not be much better than Clenshaw–Curtis, but at least it would appear to be as accurate as possible, the gold standard of quadrature formulas.

“The precision is maximised when the quadrature is Gaussian.” (1982)

“In fact, it can be shown that among all rules using n function evaluations, the $n$ -point Gaussian rule is likely to produce the most accurate estimate.” (1989)

There is another misconception here, quite different from the one just discussed as Myth 4. Gauss quadrature is optimal as measured by polynomial order of exactness, but that is a skewed measure.

The power of polynomials is nonuniform: they have greater resolution near the ends of an interval than in the middle. Suppose, for example, that $f ( x )$ is an analytic function on $[ - 1 , 1 ]$ , which means it can be analytically continued into a neighborhood of $[ - 1 , 1 ]$ in the complex $x$ -plane. Then polynomial approximants to $f$ , whether Chebyshev or Legendre interpolants or best approximants, will converge at a geometric rate $O ( \rho ^ { - n } )$ determined by how close any singularities of $f$ in the plane are to $[ - 1 , 1 ]$ . To be precise, $\rho$ is the sum of the semiminor and semimajor axis lengths of the largest ellipse with foci $\pm 1$ inside which $f$ is analytic and bounded. But ellipses are narrower near the ends than in the middle. If $f$ has a singularity at $x _ { 0 } = i \varepsilon$ for some small $\varepsilon$ , then we get $O ( \rho ^ { - n } )$ convergence with $\rho \approx 1 + \varepsilon$ . If √ $f$ has a singularity at $1 + \varepsilon$ , on the other hand, the parameter becomes $\rho \approx 1 + \sqrt { 2 \varepsilon }$ , corresponding to much faster convergence. A function with a singularity at 1.01 converges 14 times faster than one with a singularity at $0 . 0 1 i$ .

Quadrature rules generated by polynomials, including both Gauss and Clenshaw–Curtis, show the same nonuniformity. This might seem unavoidable, but in fact, there is no reason why a quadrature formula (A.1) needs to be derived from polynomials. By introducing a change of variables, one can generate alternative formulas based on interpolation by transplanted polynomials, which may converge up to $\pi / 2$ times faster than Gauss or Clenshaw–Curtis quadrature for many functions. This idea was developed in a paper of mine with Nick Hale in 2008 and is related to earlier work by Kosloff and Tal-Ezer in 1993.

The following theorem applies to one of the transformed methods Hale and I proposed. Let $f$ be a function that is analytic in an $\varepsilon$ -neighborhood of $\lfloor - 1 , 1 \rfloor$ for $\varepsilon \leq$ 0.05. Then whereas Gauss quadrature converges at the rate $I _ { n } - I = O ( ( 1 + \varepsilon ) ^ { - 2 n } )$ , transformed Gauss quadrature converges $5 0 \%$ faster, $I _ { n } - I = O ( ( 1 + \varepsilon ) ^ { - 3 n } )$ . Here is an illustration for $f ( x ) = 1 / ( 1 + 2 5 x ^ { 2 } )$ .

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/38f190837c274692b5cea20fae46462403b16b1e8502ef891a491d91f1f2f6b7.jpg)

The fact that some quadrature formulas converge up to $\pi / 2$ times faster than Gauss as $n \to \infty$ is probably not of much practical importance. The importance is conceptual.

# Myth 6. Polynomial root-finding is dangerous

Our final myth originates with Jim Wilkinson (1919–1986), a hero of mine who taught me two courses in graduate school at Stanford. Working with Alan Turing on the Pilot Ace computer in 1950, Wilkinson found that attempts to compute roots of even some low-degree polynomials failed dramatically. He publicized this discovery widely.

“Our main object in this chapter has been to focus attention on the severe inherent limitations of all numerical methods for finding the zeros of polynomials.” (1963)

“Beware: Some polynomials are ill-conditioned!” (1992)

The first of these quotations comes from Wilkinson’s book on rounding errors, and he also coined the memorable phrase “the perfidious polynomial” as the title of a 1984 article that won the Chauvenet Prize for outstanding mathematical exposition.

What Wilkinson discovered was the extreme ill-conditioning of roots of certain polynomials as functions of their coefficients. Specifically, suppose a polynomial $p _ { n }$ is specified by its coefficients in the form $a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }$ . If $p _ { n }$ has roots near the unit circle in the complex plane, these pose no difficulties: they are wellconditioned functions of the coefficients $a _ { k }$ and can be computed accurately by the MATLAB roots command, based on the calculation of eigenvalues of a companion matrix containing the coefficients. Roots far from the circle, however, such as roots on the interval $[ - 1 , 1 ]$ , can be so ill-conditioned as to be effectively uncomputable. The monomials $x ^ { k }$ form exponentially bad bases for polynomials on $[ - 1 , 1 ]$ .

The flaw in the argument is that it says nothing about the condition of roots of polynomials as functions of their values. For effective root-finding on $[ - 1 , 1 ]$ based on pointwise samples, all one must do is fix the basis: replace the monomials $x ^ { k }$ , which are orthogonal polynomials on the unit circle, by the Chebyshev polynomials $T _ { k } ( x )$ , which are orthogonal on the interval. Suppose a polynomial $p _ { n }$ is specified by its coefficients in the form $a _ { 0 } T _ { 0 } ( x ) + a _ { 1 } T _ { 1 } ( x ) + \cdot \cdot \cdot + a _ { n } T _ { n } ( x )$ . If $p _ { n }$ has roots near $[ - 1 , 1 ]$ , these are well-conditioned functions of the coefficients $a _ { k }$ , and they can be computed accurately by solving an eigenvalue problem involving a “colleague matrix.” The details were worked out by Specht in 1957 and Good in 1961.

Chebfun finds roots of a function $f$ on $[ - 1 , 1 ]$ by approximating it by a polynomial expressed in Chebyshev form and then solving a colleague-matrix eigenvalue problem, and if the degree is greater than 100, first subdividing the interval recursively to reduce it. These ideas originated with John Boyd in 2002 and are extraordinarily effective. Far from being exceptionally troublesome, polynomial root-finding when posed in this fashion begins to emerge as the most tractable of all root-finding problems, for we can solve the problem globally with just $O ( n ^ { 2 } )$ work to get all the roots in an interval to high accuracy.

For example, the function $f ( x ) = \sin ( 1 0 0 0 \pi x )$ on $[ - 1 , 1 ]$ is represented in Chebfun by a polynomial of degree 4091. It takes 2 seconds on my laptop to find all

2001 of its roots in $[ - 1 , 1 ]$ , and the maximum deviation from the exact values is $4 . 4 \times 1 0 ^ { - 1 6 }$ .

Here is another illustration of the robustness of polynomial root-finding on an interval. In Chebfun, we have plotted the function $f ( x ) = \exp ( x / 2 ) ( \sin ( 5 x )$ $+ \sin ( 1 0 1 x ) ,$ ) and then executed the commands $\mathbf { r } ~ = ~ \mathbf { r o o t s } \left( \mathbf { f - r o u n d } \left( \mathbf { f } \right) \right)$ , $\mathtt { p l o t } ( \mathtt { r } , \mathtt { f } \left( \mathtt { r } \right) , \mathtt { \xi } ^ { \prime } \cdot \mathtt { \xi } ^ { \prime } )$ . This sequence solves a collection of hundreds of polynomial root-finding problems to locate all the points where $f$ takes a value equal to an integer or a half-integer, and plots them as dots. The computation took $2 / 3$ of a second.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/aa94022df73a9a664b4cb4073759540e659b4caa33f59bc66b7ecbb3db693682.jpg)

# Conclusion

Perhaps I might close by mentioning another perspective on the misconceptions that have affected the study of computation with polynomials. By the change of variables $x = \cos \theta$ , one can show that interpolation by polynomials in Chebyshev points is equivalent to interpolation of periodic functions by series of sines and cosines in equispaced points. The latter is the subject of discrete Fourier analysis, and one cannot help noting that whereas there is widespread suspicion that it is not safe to compute with polynomials, nobody worries about the Fast Fourier Transform! In the end this may be the biggest difference between Fourier and polynomial interpolants, the difference in their reputations.

And here’s a bonus, free of charge.

# Myth 7. Lagrange discovered Lagrange interpolation

It was Waring in 1779. Euler used the formula in 1783, and Lagrange in 1795.

# Appendix B. “ATAP for Periodic Functions”

[This article was first published by the Society for Industrial and Applied Mathematics (www.siam.org): G. B. Wright, M. Javed, H. Montanelli, and L. N. Trefethen (2015), Extension of Chebfun to periodic functions, SIAM J. Sci. Statist. 37, no. 5, C554–C573.]

# B.1 Introduction

It is well known that trigonometric representations of periodic functions and Chebyshev polynomial representations of nonperiodic functions are closely related. Table B.1 lists some of the parallels between these two situations. Chebfun, a software system for computing with functions and solving ordinary differential equations (ODEs) [4, 12, 27], relied entirely on Chebyshev representations in its first decade. This paper describes its extension to periodic problems initiated by the first author and released with Chebfun Version 5.1 in December 2014.

Though Chebfun is a software product, the main focus of this paper is mathematics and algorithms rather than software per se. What makes this subject interesting is that the trigonometric/Chebyshev parallel, though close, is not an identity. The experience of building a software system based first on one kind of representation and then extending it to the other has given the Chebfun team a uniquely intimate view of the details of these relationships. We begin this paper by listing 10 differences between Chebyshev and trigonometric formulations that we have found important. This will set the stage for presentations of the problems of trigonometric series, polynomials, and projections (Section B.2), trigonometric interpolants, aliasing, and barycentric formulas (Section B.3), approximation theory and quadrature (Section B.4), and various aspects of our algorithms (Sections B.5–B.7).

Table B.1: Some parallels between trigonometric and Chebyshev settings. The row of contributors’ names is just a sample of some key figures.   

<table><tr><td>Trigonometric</td><td>Chebyshev</td></tr><tr><td>t ∈[0,2π]</td><td>x ∈[-1,1]</td></tr><tr><td>periodic</td><td>nonperiodic</td></tr><tr><td>exp(ikt)</td><td>T(x）</td></tr><tr><td>trigonometric polynomials</td><td>algebraic polynomials</td></tr><tr><td>equispaced points</td><td>Chebyshev points</td></tr><tr><td>trapezoidal rule</td><td>Clenshaw-Curtis quadrature</td></tr><tr><td>companion matrix</td><td>colleague matrix</td></tr><tr><td>Horner&#x27;srule</td><td>Clenshaw recurrence</td></tr><tr><td>fast Fourier transform</td><td>fast cosine transform</td></tr><tr><td>Gauss,Fourier, Zygmund,...</td><td>Bernstein,Lanczos,Clenshaw,..</td></tr></table>

1. One basis or two. For working with polynomials on $[ - 1 , 1 ]$ , the only basis functions one needs are the Chebyshev polynomials $T _ { k } ( x )$ . For trigonometric polynomials on $[ 0 , 2 \pi ]$ , on the other hand, there are two equally good equivalent choices: complex exponentials $\exp ( i k t )$ , or sines and cosines $\sin ( k t )$ and $\cos ( k t )$ . The former is mathematically simpler; the latter is mathematically more elementary and provides a framework for dealing with even and odd symmetries. A fully useful software system for periodic functions needs to offer both kinds of representation.

2. Complex coefficients. In the $\exp ( i k t )$ representation, the expansion coefficients of a real periodic function are complex. Mathematically, they satisfy certain symmetries, and a software system needs to enforce these symmetries to avoid imaginary rounding errors. Polynomial approximations of real nonperiodic functions, by contrast, do not lead to complex coefficients.

3. Even and odd numbers of parameters. A polynomial of degree $n$ is determined by $n + 1$ parameters, a number that may be odd or even. A trigonometric polynomial of degree $n$ , by contrast, is determined by $2 n + 1$ parameters, always an odd number, as a consequence of the $\exp ( \pm i n x )$ symmetry. For most purposes it is unnatural to speak of trigonometric polynomials with an even number of degrees of freedom. Even numbers make sense, on the other hand, in the special case of trigonometric polynomials defined by interpolation at equispaced points, if one imposes the symmetry condition that the interpolant of the $( - 1 ) ^ { j }$ sawtooth should be real, i.e., a cosine rather than a complex exponential. Here distinct formulas are needed for the even and odd cases.

4. The effect of differentiation. Differentiation lowers the degree of an algebraic polynomial, but it does not lower the degree of a trigonometric polynomial; indeed it enhances the weight of its highest-degree components.

5. Uniform resolution across the interval. Trigonometric representations have uniform properties across the interval of approximation, but polynomials are nonuniform, with much greater resolution power near the ends of $[ - 1 , 1 ]$ than near the

middle [28, Chap. 22].

6. Periodicity and translation invariance. The periodicity of trigonometric representations means that a periodic chebfun constructed on $[ 0 , 2 \pi ]$ , say, can be perfectly well evaluated at $1 0 \pi$ or $1 0 0 \pi$ ; nonperiodic chebfuns have no such global validity. Thus, whereas interpolation and extrapolation are utterly different for polynomials, they are not so different in the trigonometric case. A subtler consequence of translation invariance is explained in the footnote at the beginning of Section B.5.

7. Operations that break periodicity. A function that is smooth and periodic may lose these properties when restricted to a subinterval or subjected to operations like rounding or absolute value. This elementary fact has the consequence that a number of operations on periodic chebfuns require their conversion to nonperiodic form.

8. Good and bad bases. The functions $\exp ( i k t )$ or $\sin ( k t )$ and $\cos ( k t )$ are wellbehaved by any measure, and nobody would normally think of using any other basis functions for representing trigonometric functions. For polynomials, however, many people would reach for the basis of monomials $x ^ { k }$ before the Chebyshev polynomials $T _ { k } ( x )$ . Unfortunately, the monomials are exponentially ill-conditioned on $[ - 1 , 1 ]$ : a degree- $n$ polynomial of size $^ { 1 }$ on $[ - 1 , 1 ]$ will typically have coefficients of order $2 ^ { n }$ when expanded in the basis $1 , x , \ldots , x ^ { n }$ . Use of this basis will cause trouble in almost any numerical calculation unless $n$ is very small.

9. Good and bad interpolation points. For interpolation of periodic functions, nobody would normally think of using any interpolation points other than equispaced. For interpolation of nonperiodic functions by polynomials, however, equispaced points lead to exponentially ill-conditioned interpolation problems [23, 72]. The mathematically appropriate choice is not obvious until one learns it: Chebyshev points, quadratically clustered near $\pm 1$ .

10. Familiarity. All the world knows and trusts Fourier analysis. By contrast, experience with Chebyshev polynomials is often the domain of experts, and it is not as widely appreciated that numerical computations based on polynomials can be trusted. Historically, points 8 and 9 of this list have led to this mistrust.

The book Approximation Theory and Approximation Practice [28] summarizes the mathematics and algorithms of Chebyshev technology for nonperiodic functions. The present paper was written with the goal in mind of compiling analogous information in the trigonometric case. In particular, Section B.2 corresponds to Chapter 3 of [28], Section B.3 to Chapters 2, 4, and 5, and Section B.4 to Chapters 6, 7, 8, 10, and 19.

# B.2 Trigonometric series, polynomials, and projections

Throughout this paper, we assume $f$ is a Lipschitz continuous periodic function on $[ 0 , 2 \pi ]$ . Here and in all our statements about periodic functions, the interval $[ 0 , 2 \pi ]$ should be understood periodically: $t = 0$ and $t = 2 \pi$ are identified, and any smoothness assumptions apply across this point in the same way as for $t \in$ $( 0 , 2 \pi )$ [18, Chap. 1].

It is known that $f$ has a unique trigonometric series, absolutely and uniformly

convergent, of the form

$$
f ( t ) = \sum _ { k = - \infty } ^ { \infty } c _ { k } e ^ { i k t } ,
$$

with Fourier coefficients

$$
c _ { k } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) e ^ { - i k t } d t .
$$

(All coefficients in our discussions are in general complex, though in cases of certain symmetries they will be purely real or imaginary.) Equivalently, we have

$$
f ( t ) = \sum _ { k = 0 } ^ { \infty } a _ { k } \cos ( k t ) + \sum _ { k = 1 } ^ { \infty } b _ { k } \sin ( k t ) ,
$$

with $a _ { 0 } = c _ { 0 }$ and

$$
a _ { k } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) \cos ( k t ) d t , \quad b _ { k } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) \sin ( k t ) d t \qquad ( k \geq 1 ) .
$$

The formulas (B.4) can be derived by matching the $e ^ { i k t }$ and $e ^ { - i k t }$ terms of (B.3) with those of (B.1), which yields the identities

$$
c _ { k } = \frac { a _ { k } } { 2 } + \frac { b _ { k } } { 2 i } , \quad c _ { - k } = \frac { a _ { k } } { 2 } - \frac { b _ { k } } { 2 i } \qquad ( k \ge 1 )
$$

or, equivalently,

$$
a _ { k } = c _ { k } + c _ { - k } , \quad b _ { k } = i ( c _ { k } - c _ { - k } ) \quad \quad ( k \geq 1 ) .
$$

Note that if $f$ is real, then (B.4) implies that $a _ { k }$ and $b _ { k }$ are real. The coefficients $c _ { k }$ are generally complex, and (B.5) implies that they satisfy $c _ { - k } = \overline { { c } } _ { k }$ .

The degree n trigonometric projection of $f$ is the function

$$
f _ { n } ( t ) = \sum _ { k = - n } ^ { n } c _ { k } e ^ { i k t }
$$

or, equivalently,

$$
f _ { n } ( t ) = \sum _ { k = 0 } ^ { n } a _ { k } \cos ( k t ) + \sum _ { k = 1 } ^ { n } b _ { k } \sin ( k t ) .
$$

More generally, we say that a function of the form (B.7)–(B.8) is a trigonometric polynomial of degree $n$ , and we let $P _ { n }$ denote the $( 2 n + 1 )$ -dimensional vector space of all such polynomials. The trigonometric projection $f _ { n }$ is the least-squares approximant to $f$ in $P _ { n }$ , i.e., the unique best approximation to $f$ in the $L ^ { 2 }$ norm over $[ 0 , 2 \pi ]$ .

# B.3 Trigonometric interpolants, aliasing, and barycentric formulas

Mathematically, the simplest degree $n$ trigonometric approximation of a periodic function $f$ is its trigonometric projection (B.7)–(B.8). This approximation depends on the values of $f ( t )$ for all $t \in [ 0 , 2 \pi ]$ via (B.2) or (B.4). Computationally, a simpler approximation of $f$ is its degree $n$ trigonometric interpolant, which only depends on the values at certain interpolation points. In our basic configuration, we wish to interpolate $f$ in equispaced points by a function $p _ { n } \in P _ { n }$ . Since the dimension of $P _ { n }$ is $2 n + 1$ , there should be $2 n + 1$ interpolation points. We take these trigonometric points to be

$$
t _ { k } = { \frac { 2 \pi k } { N } } , \qquad 0 \leq k \leq N - 1 ,
$$

with $N = 2 n + 1$ . The trigonometric interpolation problem goes back at least to the young Gauss’s calculations of the orbit of the asteroid Ceres in 1801 [15].

It is known that there exists a unique interpolant $p _ { n } \in P _ { n }$ to any set of data values $f _ { k } = f ( t _ { k } )$ . Let us write $p _ { n }$ in the form

$$
p _ { n } ( t ) = \sum _ { k = - n } ^ { n } \tilde { c } _ { k } e ^ { i k t }
$$

or, equivalently,

$$
p _ { n } ( t ) = \sum _ { k = 0 } ^ { n } \widetilde { a } _ { k } \cos ( k t ) + \sum _ { k = 1 } ^ { n } \widetilde { b } _ { k } \sin ( k t )
$$

for some coefficients ${ \bar { c } } _ { - n } , \ldots , { \bar { c } } _ { n }$ or, equivalently, $\ddot { a } _ { 0 } , \dots , \ddot { a } _ { n }$ and $\ddot { b } _ { 1 } , \dotsc , \ddot { b } _ { n }$ . The coefficients $\bar { c } _ { k }$ and $c _ { k }$ are related by

$$
\tilde { c } _ { k } = \sum _ { j = - \infty } ^ { \infty } c _ { k + j N } \qquad ( | k | \le n )
$$

(the Poisson summation formula) and, similarly, $\begin{array} { r } { \tilde { a } _ { 0 } = \sum _ { j = 0 } ^ { \infty } a _ { j N } } \end{array}$ and $\tilde { a } _ { k } / \tilde { b } _ { k }$ and $a _ { k } / b _ { k }$ are related by

$$
\tilde { a } _ { k } = a _ { k } + \sum _ { j = 1 } ^ { \infty } ( a _ { k + j N } + a _ { - k + j N } ) , \quad \tilde { b } _ { k } = b _ { k } + \sum _ { j = 1 } ^ { \infty } ( b _ { k + j N } - b _ { - k + j N } )
$$

for $1 \leq k \leq n$ . We can derive these formulas by considering the phenomenon of aliasing. For all $j$ , the functions $\exp ( i [ k + j N ] t )$ take the same values at the trigonometric points (B.9). This implies that $f$ and the trigonometric polynomial (B.10) with coefficients defined by (B.12) take the same values at these points. In other words, (B.10) is the degree $n$ trigonometric interpolant to $f$ . A similar argument justifies (B.11)–(B.13).

Another interpretation of the coefficients $\tilde { c } _ { k } , \tilde { a } _ { k } , \tilde { b } _ { k }$ is that they are equal to the approximations to $c _ { k } , a _ { k } , b _ { k }$ one gets if the integrals (B.2) and (B.4) are approximated by the periodic trapezoidal quadrature rule with $N$ points [29]:

$$
\tilde { c } _ { k } = \frac { 1 } { N } \sum _ { j = 0 } ^ { N - 1 } f _ { j } e ^ { - i k t _ { j } } ,
$$

$$
\tilde { a } _ { k } = \frac { 2 } { N } \sum _ { j = 0 } ^ { N - 1 } f _ { j } \cos ( k t _ { j } ) , \quad \tilde { b } _ { k } = \frac { 2 } { N } \sum _ { j = 0 } ^ { N - 1 } f _ { j } \sin ( k t _ { j } ) \qquad ( k \ge 1 ) .
$$

To prove this, we note that the trapezoidal rule computes the same Fourier coefficients for $f$ as for $p _ { n }$ , since they take the same values at the grid points; but these must be equal to the true Fourier coefficients of $p _ { n }$ , since the $N = ( 2 n + 1 )$ -point trapezoidal rule is exactly correct for $e ^ { - 2 i n t } , \ldots , e ^ { 2 i n t }$ , hence for any trigonometric polynomial of degree $2 n$ , hence, in particular, for any trigonometric polynomial of degree $n$ times an exponential $\exp ( - i k t )$ with $| k | \le n$ . From (B.14)–(B.15) it is evident that the discrete Fourier coefficients $\bar { c } _ { k }$ , $\ddot { a } _ { k }$ , $\ddot { b } _ { k }$ can be computed by the Fast Fourier Transform (FFT), which, in fact, Gauss invented for this purpose.

Suppose one wishes to evaluate the interpolant $p _ { n } ( t )$ at certain points $t$ . One good algorithm is to compute the discrete Fourier coefficients and then apply them. Alternatively, another good approach is to perform interpolation directly by means of the barycentric formula for trigonometric interpolation, introduced by Salzer [26] and later simplified by Henrici [38]:

$$
p _ { n } ( t ) = \sum _ { k = 0 } ^ { N - 1 } ( - 1 ) ^ { k } f _ { k } \csc \left( \frac { t - t _ { k } } { 2 } \right) \bigg / \sum _ { k = 0 } ^ { N - 1 } ( - 1 ) ^ { k } \csc \left( \frac { t - t _ { k } } { 2 } \right) \quad ( N \ \mathrm { o d d } ) .
$$

(If $t$ happens to be exactly equal to a grid point $t _ { k }$ , one takes $p _ { n } ( t ) = f _ { k }$ .) The work involved in this formula is just $O ( N )$ operations per evaluation, and stability has been established (after a small modification) in [3]. In practice, we find the Fourier coefficients and barycentric formula methods equally effective.

In the above discussion, we have assumed that the number of interpolation points, $N$ , is odd. However, trigonometric interpolation, unlike trigonometric projection, makes sense for an even number of degrees of freedom too (see, e.g., [14, 19, 30]); it would be surprising if FFT codes refused to accept input vectors of even lengths! Suppose $n \geq 1$ is given and we wish to interpolate $f$ in $N = 2 n$ trigonometric points (B.9) rather than $N = 2 n + 1$ . This is one data value less than usual for a trigonometric polynomial of this degree, and we can lower the number of degrees of freedom in (B.10) by imposing the condition

$$
\widetilde c _ { - n } = \widetilde c _ { n }
$$

or, equivalently, in (B.11) by imposing the condition

$$
\tilde { b } _ { n } = 0 .
$$

This amounts to prescribing that the trigonometric interpolant through sawtoothed data of the form $f _ { k } = ( - 1 ) ^ { k }$ should be $\cos ( n t )$ rather than some other function such as $\exp ( i n t )$ —the only choice that ensures that real data will lead to a real interpolant. An equivalent prescription is that an arbitrary number $N$ of data values, even or odd, will be interpolated by a linear combination of the first $N$ terms of the sequence

$$
1 , \cos ( t ) , \sin ( t ) , \cos ( 2 t ) , \sin ( 2 t ) , \cos ( 3 t ) , \ldots .
$$

In this case of trigonometric interpolation with $N$ even, the formulas (B.9)– (B.15) still hold, except that (B.12) and (B.14) must be multiplied by $1 / 2$ for $k = \pm n$ . FFT codes, however, do not store the information that way. Instead, following (B.17), they compute ${ \ddot { c } } _ { - n }$ by (B.14) with $2 / N$ instead of $1 / N$ out front— thus effectively storing $\tilde { c } _ { - n } + \tilde { c } _ { n }$ in the place of ${ \ddot { c } } _ { - n }$ —and then apply (B.10) with the $k = n$ term omitted. This gives the right result for values of $t$ on the grid, but not at points in between.

Note that the conditions (B.17)–(B.19) are very much tied to the use of the sample points (B.9). If the grid were translated uniformly, then different relationships between $c _ { n }$ and $c _ { - n }$ or $a _ { n } / b _ { n }$ and $a _ { - n } / b _ { - n }$ would be appropriate in (B.17)–(B.18) and different basis functions in (B.19), and if the grid were not uniform, then it would be hard to justify any particular choices at all for even $N$ . For these reasons, even numbers of degrees of freedom make sense in equispaced interpolation but not in other trigonometric approximation contexts, in general. Henrici [38] provides a modification of the barycentric formula (B.16) for the equispaced case $N = 2 n$ .

# B.4 Approximation theory and quadrature

The basic question of approximation theory is, Will approximants to a function $f$ converge as the degree is increased, and how fast? The formulas of the last two sections enable us to derive theorems addressing this question for trigonometric projection and interpolation. (For finer points of trigonometric approximation theory, see [21].) The smoother $f$ is, the faster its Fourier coefficients decrease, and the faster the convergence of the approximants. (If $f$ were merely continuous rather than Lipschitz continuous, then the trigonometric version of the Weierstrass approximation theorem [18, Section I.2] would ensure that it could be approximated arbitrarily closely by trigonometric polynomials, but not necessarily by projection or interpolation.)

Our first theorem asserts that Fourier coefficients decay algebraically if $f$ has a finite number of derivatives, and geometrically if $f$ is analytic. Here and in Theorem B.2 below, we make use of the notion of the total variation, $V$ , of a periodic function $\varphi$ defined on $[ 0 , 2 \pi ]$ , which is defined in the usual way as the supremum of all sums $\textstyle \sum _ { i = 1 } ^ { n } | \varphi ( x _ { i } ) - \varphi ( x _ { i - 1 } ) |$ , where $\{ x _ { i } \}$ are ordered points in $[ 0 , 2 \pi ]$ with $x _ { 0 } = x _ { n }$ ; $V$ is equal to the the 1-norm of $f ^ { \prime }$ , interpreted if necessary as a Riemann–Stieltjes integral [18, Section I.4]. Thus $| \sin ( t ) |$ on $[ 0 , 2 \pi ]$ , for example, corresponds to $\nu = 1$ , and $| \sin ( t ) | ^ { 3 }$ to $\nu = 3$ . All our theorems continue to assume that $f$ is $2 \pi$ -periodic.

Theorem B.1. If $f$ is $\nu \geq 0$ times differentiable and $f ^ { ( \nu ) }$ is of bounded variation $V$ on $[ 0 , 2 \pi ]$ , then

$$
| c _ { k } | \leq { \frac { V } { 2 \pi | k | ^ { \nu + 1 } } } .
$$

If $f$ is analytic with $| f ( t ) | \leq M$ in the open strip of half-width $\alpha$ around the real axis in the complex $t$ -plane, then

$$
| c _ { k } | \leq M e ^ { - \alpha | k | } .
$$

Proof. The bound (B.20) can be derived by integrating (B.2) by parts $\nu + 1$ times. Equation (B.21) can be derived by shifting the interval of integration $[ 0 , 2 \pi ]$ of (B.2) downward in the complex plane for $k > 0$ , or upward for $k < 0$ , by a distance arbitrarily close to $\alpha$ ; see [29, Section 3].

To apply Theorem B.1 to trigonometric approximations, we note that the error in the degree $n$ trigonometric projection (B.7) is

$$
f ( t ) - f _ { n } ( t ) = \sum _ { | k | > n } c _ { k } e ^ { i k t } ,
$$

a series that converges absolutely and uniformly by the Lipschitz continuity assumption on $f$ . Similarly, (B.12) implies that the error in trigonometric interpolation is

$$
f ( t ) - p _ { n } ( t ) = \sum _ { | k | > n } c _ { k } ( e ^ { i k t } - e ^ { i k ^ { \prime } t } ) ,
$$

where $k ^ { \prime } = \mathrm { m o d } ( k + n , 2 n + 1 ) - n$ is the index that $k$ gets aliased to on the $( 2 n + 1 )$ -point grid, i.e., the integer of absolute value $\leq n$ congruent to $k$ modulo $2 n + 1$ . These formulas give us bounds on the error in trigonometric projection and interpolation.

Theorem B.2. If $f$ is $\nu \geq 1$ times differentiable and $f ^ { ( \nu ) }$ is of bounded variation $V$ on $[ 0 , 2 \pi ]$ , then its degree $n$ trigonometric projection and interpolant satisfy

$$
\| f - f _ { n } \| _ { \infty } \leq { \frac { V } { \pi \nu n ^ { \nu } } } , \qquad \| f - p _ { n } \| _ { \infty } \leq { \frac { 2 V } { \pi \nu n ^ { \nu } } } .
$$

If $f$ is analytic with $| f ( t ) | \leq M$ in the open strip of half-width $\alpha$ around the real axis in the complex $t$ -plane, they satisfy

$$
\| f - f _ { n } \| _ { \infty } \leq \frac { 2 M e ^ { - \alpha n } } { e ^ { \alpha } - 1 } , \qquad \| f - p _ { n } \| _ { \infty } \leq \frac { 4 M e ^ { - \alpha n } } { e ^ { \alpha } - 1 } .
$$

Proof. The estimates (B.24) follow by bounding the tails (B.22) and (B.23) with (B.20), and (B.25) likewise by bounding them with (B.21).

A slight variant of this argument gives an estimate for quadrature. If $I$ denotes the integral of a function $f$ over $[ 0 , 2 \pi ]$ and $I _ { N }$ its approximation by the $N$ -point periodic trapezoidal rule, then from (B.2) and (B.14), we have $I = 2 \pi c _ { 0 }$ and $I _ { N } =$ $2 \pi \tilde { c } _ { 0 }$ . By (B.12) this implies

$$
I _ { N } - I = 2 \pi \sum _ { j \neq 0 } c _ { j N } ,
$$

which gives the following result.

Theorem B.3. If $f$ is $\nu \geq 1$ times differentiable and $f ^ { ( \nu ) }$ is of bounded variation $V$ on $[ 0 , 2 \pi ]$ , then the $N$ -point periodic trapezoidal rule approximation to its integral over $[ 0 , 2 \pi ]$ satisfies

$$
| I _ { N } - I | \leq \frac { 4 V } { N ^ { \nu + 1 } } .
$$

If $f$ is analytic with $| f ( t ) | \leq M$ in the open strip of half-width $\alpha$ around the real axis in the complex $t$ -plane, it satisfies

$$
| I _ { N } - I | \leq \frac { 4 \pi M } { e ^ { \alpha N } - 1 } .
$$

Proof. These results follow by bounding (B.26) with (B.20) and (B.21) as in the proof of Theorem B.2. From (B.20), the bound one gets is $2 V \zeta ( \nu + 1 ) / N ^ { \nu + 1 }$ , where $\zeta$ is the Riemann zeta function, which we have simplified by the inequality $\zeta ( \nu + 1 ) \leq \zeta ( 2 ) < 2$ for $\nu \geq 1$ . The estimate (B.28) originates with Davis [17]; see also [19, 29].

Finally, in a section labeled “approximation theory” we must mention another famous candidate for periodic function approximation: best approximation in the $\infty$ -norm. Here the trigonometric version of the Chebyshev alternation theorem holds, assuming $f$ is real. This result is illustrated later in Figure B.11.

Theorem B.4. Let $f$ be real and continuous on the periodic interval $[ 0 , 2 \pi ]$ . For each $n \geq 0$ , $f$ has a unique best approximant $p _ { n } ^ { * } \in \boldsymbol { P } _ { n }$ with respect to the norm $\| \cdot \| _ { \infty }$ , and $\boldsymbol { p } _ { n } ^ { * }$ is characterized by the property that the error curve $( f - p _ { n } ^ { * } ) ( t )$ equioscillates on $[ 0 , 2 \pi )$ between at least $2 n + 2$ equal extrema $\pm \| f - p _ { n } ^ { * } \| _ { \infty }$ of alternating signs.

Proof. See [21, Section 5.2] for a proof.

# B.5 Trigfun computations

Building on the mathematics of the past three sections, Chebfun was extended in 2014 to incorporate trigonometric representations of periodic functions alongside its traditional Chebyshev representations. (Here and in the remainder of the paper, we assume the reader is familiar with Chebfun.) Our convention is that a trigfun is a representation via coefficients $c _ { k }$ as in (B.7) of a sufficiently smooth periodic function $f$ on an interval by a trigonometric polynomial of adaptively determined degree, the aim always being accuracy of 15 or 16 digits relative to the $\infty$ -norm of the function on the interval. This follows the same pattern as traditional Chebyshevbased chebfuns, which are representations of nonperiodic functions by polynomials, and a trigfun is not a distinct object from a chebfun but a particular type of chebfun. The default interval, as with ordinary chebfuns, is $[ - 1 , 1 ]$ , and other intervals are handled by the obvious linear transplantation.17

For example, here we construct and plot a trigfun for $\cos ( t ) + \sin ( 3 t ) / 2$ on $[ 0 , 2 \pi ]$ :

The plot appears in Figure B.1, and the following text output is produced, with the flag trig signaling the periodic representation.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/2edb0421aeed0cb35fec4b75249de3dd62ed45cd325e542f313647aa5c6af9fd.jpg)  
Figure B.1: The trigfun representing $f ( t ) = \cos ( t ) + \sin ( 3 t ) / 2$ on $[ 0 , 2 \pi ]$ . One can evaluate $f$ with $\pm \left( \ t \right)$ , compute its definite integral with sum(f) or its maximum with max(f), find its roots with roots(f), and so on.

f = chebfun column (1 smooth piece) interval length endpoint values trig   
[ 0, 6.3] 7 1 1

We see that Chebfun has determined that this function $f$ is of length $N = 7$ . This means that there are 7 degrees of freedom, i.e., $f$ is a trigonometric polynomial of degree $n = 3$ , whose coefficients we can extract with $\begin{array} { r l } { \mathtt { C } } & { { } = } \end{array}$ trigcoeffs(f), or in cosine/sine form with $[ { \mathsf { a } } , { \mathsf { b } } ] =$ trigcoeffs(f).

Note that the Chebfun constructor does not analyze its input symbolically but just evaluates the function at trigonometric points (B.9), and from this information the degree and the values of the coefficients are determined. The constructor also detects when a function is real. A trigfun constructed in the ordinary manner is always of odd length $N$ , corresponding to a trigonometric polynomial of degree $n = ( N - 1 ) / 2$ , though it is possible to make even-length trigfuns by explicitly specifying $N$ .

To construct a trigfun, Chebfun samples the function on grids of size $1 6 , 3 2 , 6 4 , \ldots$ and tests the resulting discrete Fourier coefficients for convergence down to relative machine precision. (Powers of 2 are used since these are particularly efficient for the FFT, even though the result will ultimately be trimmed to an odd number of points. As with nontrigonometric Chebfun, the engineering details are complicated and under ongoing development.) When convergence is achieved, the series is chopped at an appropriate point and the degree reduced accordingly.

Once a trigfun has been created, computations can be carried out in the usual Chebfun fashion via overloads of familiar MATLAB commands. For example,

>> sum(f^2) ans = 3.926990816987241

This number is computed by integrating the trigonometric representation of $f ^ { 2 }$ , i.e., by returning the number $2 \pi c _ { 0 }$ corresponding to the trapezoidal rule applied to $f ^ { 2 }$ as described around Theorem B.3. The default 2-norm is the square root of this result,

>> norm(f) ans = 1.981663648803005

Derivatives of functions are computed by the overloaded command diff. (In the unusual case where a trigfun has been constructed of even length, differentiation will increase its length by 1.) The zeros of $f$ are found with roots,

>> roots(f)   
ans = 1.263651122898791 4.405243776488583

and Chebfun determines maxima and minima by first computing the derivative, then checking all of its roots:

>> max(f) ans = 1.389383416980387

Concerning the algorithm used for periodic rootfinding, one approach would be to solve a companion matrix eigenvalue problem, and $O ( n ^ { 2 } )$ algorithms for this task have recently been developed [1]. When development of these methods settles down, they may be incorporated in Chebfun. For the moment, trigfun rootfinding is done by first converting the problem to nonperiodic Chebfun form using the standard Chebfun constructor, whereupon we take advantage of Chebfun’s $O ( n ^ { 2 } )$ recursive interval subdivision strategy [6]. This shifting to subintervals for rootfinding is an example of an operation that breaks periodicity as mentioned in item 7 of the introduction.

The main purpose of the periodic part of Chebfun is to enable machine precision computation with periodic functions that are not exactly trigonometric polynomials. For example, $\exp ( \sin t )$ on $[ 0 , 2 \pi ]$ is represented by a trigfun of length 27, i.e., a trigonometric polynomial of degree 13:

$$
\begin{array} { r l } & { \mathrm { ~ g ~ = ~ c h e b f u n } { ( \mathrm {  ~ \cdot ~ } \exp ( \mathrm { s i n } ( \mathrm { t } ) ) \mathrm {  ~ \cdot ~ } , ~ \mathrm { ~ } [ 0 ~ 2 * \mathrm { p i } ] ~ , ~ \mathrm {  ~ \cdot ~ } \mathrm { t r i g } ^ { \mathrm {  ~ \cdot ~ } } ) } } \\ & { \mathrm { ~ g ~ = ~ } } \\ & { \quad \mathrm { ~ c h e b f u n ~ c o l u m n ~ \Lambda ~ ( 1 ~ \ s m o o t h ~ \ p i e c e ) ~ } } \\ & { \quad \quad \quad \quad \mathrm { i n t e r v a l ~ } \quad \quad \quad \mathrm { l e n g t h } \quad \quad \quad \mathrm { e n d p o i n t ~ \ v a l u e s ~ \ t r i g } } \\ & { \mathrm { ~ [ ~ } \quad \quad 0 , \quad \quad \quad 6 . 3 \mathrm { ] } \quad \quad 2 7 \quad \quad \quad 1 } \end{array}
$$

The coefficients can be plotted on a log scale with the command plotcoeffs(f), and Figure B.2 reveals the faster-than-geometric decay of an entire function.

Figure B.3 shows trigfuns and coefficient plots for $f ( t ) = \operatorname { t a n h } ( 5 \cos ( 5 t ) )$ and $g ( t ) = \exp ( - 1 / \operatorname* { m a x } \{ 0 , 1 - t ^ { 2 } / 4 \} )$ on $[ - \pi , \pi ]$ . The latter is $C ^ { \infty }$ but not analytic. Figure B.4 shows a further pair of examples that we call an “AM signal” and an “FM signal.” These are among the preloaded functions available with cheb.gallerytrig, Chebfun’s trigonometric analogue of the MATLAB gallery command.

Computation with trigfuns, as with nonperiodic chebfuns, is carried out by a continuous analogue of floating point arithmetic [27]. To illustrate the “rounding” process involved, the degrees of the trigfuns above are 555 and 509, respectively. Mathematically, their product is of degree 1064. Numerically, however, Chebfun achieves 16-digit accuracy with degree 556.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/78599dc4b0da7ac0e6e0cf1af144dc909d16f33b3aa04fcd15add5ffb367a116.jpg)  
Figure B.2: Absolute values of the Fourier coefficients of the trigfun for $\exp ( \sin t )$ on $[ 0 , 2 \pi ]$ . This is an entire function (analytic throughout the complex $t$ -plane), and in accordance with Theorem B.1, the coefficients decrease faster than geometrically.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0004_pages_0211-0280/auto/images/6a92bdc582656533fb1f8420b436a60477d4bb01b47a97f6c6cd1ca66dbff1f9.jpg)  
Figure B.3: Trigfuns of $\operatorname { t a n h } ( 5 \sin t )$ and $\exp ( - 1 0 0 ( t + . 3 ) ^ { 2 } )$ (upper row) and corresponding absolute values of Fourier coefficients (lower row).


<!-- chunk 0005: pages 281-350 -->
![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/9e97c24efa4c9cea2b8cb0df0ca54398aec8937acafb0793be69229914ab9cd9.jpg)  
Figure B.4: Trigfuns of the “AM signal” $\cos ( 5 0 t ) ( 1 + \cos ( 5 t ) / 5 )$ and of the “FM signal” $\cos ( 5 0 t + 4 \sin ( 5 t ) )$ (upper row) and corresponding absolute values of Fourier coefficients (lower row).

Here is a more complicated example of Chebfun rounding adapted from [27], where it is computed with nonperiodic representations:

$$
\begin{array} { r l } & { \mathbf { f _ { \lambda } } = \mathbf { \lambda } \mathrm { c h e b f u n } \left( \mathbb { Q } \left( \mathrm { t } \right) \ \mathrm { s i n } \left( \mathrm { p i } \ast \mathrm { t } \right) , \ \mathrm { \Lambda } ^ { \prime } \mathrm { t r i g } ^ { \prime } \right) } \\ & { \mathbf { s _ { \lambda } } = \mathbf { f _ { \lambda } } } \\ & { \mathbf { f o r } \ \mathbf { j _ { \lambda } } = \ 1 : 1 5 } \\ & { \mathbf { f _ { \lambda } } = \mathbf { \lambda } \left( 3 / 4 \right) \ast \left( 1 \ - \ 2 \ast \mathbf { f } ^ { \sim } 4 \right) , \ \mathbf { s _ { \lambda } } = \mathbf { \lambda } \mathbf { s _ { \lambda } } + \mathbf { \lambda } \mathbf { f _ { \lambda } } } \end{array}
$$

This program takes 15 steps of an iteration that in principle quadruples the degree at each step, giving a function $s$ at the end of degree $4 ^ { 1 5 } \ = \ 1$ ,073,741,824. In actuality, however, because of the rounding to 16 digits, the degree comes out one million times smaller as 1148. This function is plotted in Figure B.5. Following [27], we can compute the roots of $s - 8$ in half a second on a desktop machine:

>> roots(s-8)   
ans = -0.992932107411876 -0.816249934290177 -0.798886729723433 -0.201113270276572 -0.183750065709828 -0.007067892588112 0.346696120418255

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/468074f4004a911d43929a64de9a7c80bba191ec499f2330fc09ace0c0d5ae2a.jpg)  
Figure B.5: After 15 steps of an iteration, this periodic function has degree 1148 in its Chebfun representation rather than the mathematically exact figure 1,073,741,824.

0.401617073482111   
0.442269489632475   
0.557730510367530   
0.598382926517899   
0.653303879581760

The integral with sum(s) is 15.265483825826763, correct except in the last two digits.

If one tries to construct a trigfun by sampling a function that is not smoothly periodic, Chebfun will by default go up to length $2 ^ { 1 6 }$ and then issue a warning:

>> h = chebfun('exp(t)', [0 2\*pi], 'trig') Warning: Function not resolved using 65536 pts. Have you tried a non-trig representation?

On the other hand, computations that are known to break periodicity or smoothness will result in the representation being automatically cast from a trigfun to a chebfun. For example, here we define $g$ to be the absolute value of the function $f ( t ) =$ $\cos ( t ) + \sin ( 3 t ) / 2$ of Figure B.1. The system detects that $f$ has zeros, implying that $g$ will probably not be smooth, and accordingly constructs it not as a trigfun but as an ordinary chebfun with several pieces (Figure B.6):

>> f = chebfun('cos(t) + sin(3\*t)/2', [0 2\*pi], 'trig'), g = abs(f)   
g = chebfun column (3 smooth pieces) interval length endpoint values   
[ 0, 1.3] 17 1 3.8e-16   
[ 1.3, 4.4] 25 1.8e-15 7.3e-16   
[ 4.4, 6.3] 20 -6.6e-18 1   
Total length $\ c = ~ 6 2$ .

Similarly, if you add or multiply a trigfun and a chebfun, the result is a chebfun.

# B.6 Applications

Analysis of periodic functions and signals is one of the oldest topics of mathematics and engineering. Here we give six examples of how a system for automating such computations may be useful.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/1bd4928b83686d7df43439a7011057889ef08d727a819478e81b816b270a6333.jpg)  
Figure B.6: When the absolute value of the trigfun $f$ of Figure B.1 is computed, the result is a nonperiodic chebfun with three smooth pieces.

Complex contour integrals. Smooth periodic integrals arise ubiquitously in complex analysis. For example, suppose we wish to determine the number of zeros of $f ( z ) = \cos ( z ) - z$ in the complex unit disk. The answer is given by

$$
m = { \frac { 1 } { 2 \pi i } } \int { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z = { \frac { 1 } { 2 \pi i } } \int { \frac { 1 } { f ( z ) } } { \frac { d f } { d t } } d t
$$

if $z = \exp ( i t )$ with $t \in [ 0 , 2 \pi ]$ . With periodic Chebfun, we can compute $m$ by

$$
\begin{array} { r l } & { \mathrm { \gamma > ~ z ~ = ~ c h e b f u n ( ~ ' \exp ( 1 i * t ) ~ ' , ~ [ 0 ~ 2 * p i ] ~ , ~ ' t r i g ' ) } ; } \\ & { \mathrm { \gamma > ~ f ~ = ~ c o s ( z ) ~ - ~ z ; } } \\ & { \mathrm { \gamma > ~ m ~ = ~ \mathrm { r e a l } ( s u m ( d i f f ( f ) / f ) / ( 2 i * p i ) ) } } \\ & { \mathrm { \gamma ~ m ~ = ~ 1 . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } } \end{array}
$$

Changing the integrand from $f ^ { \prime } ( z ) / f ( z )$ to $z f ^ { \prime } ( z ) / f ( z )$ gives the location of the zero, correct to all digits displayed:

>> z0 = real(sum(z\*diff(f)/f)/(2i\*pi)) z0 = 0.739085133215161

(The real commands are included to remove imaginary rounding errors.) For wide-ranging extensions of calculations like these, including applications to matrix eigenvalue problems, see [2].

Linear algebra. Chebfun does not work from explicit formulas: to construct a function, it is only necessary to be able to evaluate it. This is an extremely useful feature for linear algebra calculations. For example, the matrix

$$
A = \frac { 1 } { 3 }
$$

has all its eigenvalues in the unit disk. A question with the flavor of control and stability theory is, What is the maximum resolvent norm $\lVert ( z I - A ) ^ { - 1 } \rVert$ for $z$ on the unit circle? We can calculate the answer with the code below, which constructs a periodic chebfun of degree $n = 5 6 9$ . The maximum is 27.68851, attained with $z = \exp ( 0 . 4 5 4 5 9 6 i )$ (Figure B.7).

$$
\begin{array} { r l } & { \mathrm { ~ \tt ~ A ~ = ~ [ 2 ~ - 2 i ~ 1 ~ 1 ~ 1 ; ~ 2 i ~ - 2 ~ 0 ~ 2 ; ~ - 2 ~ 0 ~ 1 ~ 2 ; ~ 0 ~ 1 { \tt } ~ 1 ~ 0 ~ 2 ] / 3 , ~ { \tt ~ I } ~ = ~ { \tt } e y e ( 4 ) } } \\ & { \mathrm { ~ \tt ~ f ~ f ~ = ~ { \tt ~ Q } ( t ) ~ \tt ~ 1 / m i n ( \ s v d ( e x p ( 1 1 * t ) * I - A ) ) } } \\ & { \mathrm { ~ \tt ~ f ~ = ~ \ c h e b f u n ( f f , ~ [ 0 ~ 2 * p i ] , ~ \theta ' { \tt ~ t r i g } ' , ~ \theta ' v e c t o r i z e ' ) } } \\ & { \mathrm { ~ [ m a x v a l , m a x p o s ] ~ \theta = \ m a x ( f ) ~ \theta ~ } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/263f3666c3798528417cf37c2000cb4bbe4c7506c31266b45dbb6336556487e4.jpg)  
Figure B.7: Resolvent norm $\| ( z I - A ) ^ { - 1 } \|$ for a $4 \times 4$ matrix $A$ with $z = e ^ { i t }$ on the unit circle.

Circular convolution and smoothing. The circular or periodic convolution of two functions $f$ and $g$ with period $T$ is defined by

$$
( f * g ) ( t ) : = \int _ { t _ { 0 } } ^ { t _ { 0 } + T } g ( s ) f ( t - s ) d s ,
$$

where $t _ { 0 }$ is aribtrary. Circular convolutions can be computed for trigfuns with the circconv function, whose algorithm consists of coefficientwise multiplication in Fourier space. For example, here is a trigonometric interpolant through 201 samples of a smooth function plus noise, shown in the upper-left panel of Figure B.8.

N = 201, tt = trigpts(N, [-pi pi]) ff = exp(sin(tt)) + 0.05\*randn(N,1) f = chebfun(ff, [-pi pi], 'trig')

The high wave numbers can be smoothed by convolving $f$ with a mollifier. Here we use a Gaussian of standard deviation $\sigma = 0 . 1$ (numerically periodic for $\sigma \leq 0 . 3 5$ ). The result is shown in the upper-right panel of the figure.

$$
\begin{array} { r l } & { \mathrm { g a u s s i a n ~ \ b = ~ \ b \emptyset ( \mathbf { t } , \mathbf { s i g m a } ) ~ \ b 1 / ( \mathbf { s i g m a * s q r t } ( \ b 2 * \mathbf { p i } ) ) * \mathbf { e x p } ( \ b - \ b 0 . 5 * ( \mathbf { t } / \mathbf { s i g m a } ) \cdot \ b \cdot \ b \cdot 2 ) } } \\ & { \mathrm { g ~ \ b = ~ \ b \emptyset ( \mathbf { s i g m a } ) ~ \ c h e b f u n ( \ b \emptyset ( \mathbf { t } ) ~ \mathbf { g a u s s i a n } ( \mathbf { t } , \mathbf { s i g m a } ) , ~ \{ \ b \cdot \_ p i ~ \mathbf \} ] ~ \ b , ~ \cdot \_ \mathbf { t r i g } \cdot ) ~ } } \\ & { \mathrm { h ~ \ b = ~ \ b c i r c c o n v ( \mathbf { f } , ~ \mathbf { g } ( \ b 0 . 1 ) ) ~ } } \end{array}
$$

Fourier coefficients of nonsmooth functions. A function $f$ that is not smoothly periodic will at best have a very slowly converging trigonometric series, but still, one may be interested in its Fourier coefficients. These can be computed by applying trigcoeffs to a chebfun representation of $f$ and specifying how many coefficients are required; the integrals (B.2) are then evaluated numerically by Chebfun’s standard method of Clenshaw–Curtis quadrature. For example, Figure B.9 shows a portrayal of the Gibbs phenomenon from Runge’s 1904 book together with its Chebfun equivalent computed in a few seconds with the commands

$$
\begin{array} { l } { { \mathrm {  ~ \ l ~ \ l ~ \bar { \ t } ~ \ l u ~ \bar { \ t } ~ u n ( \bar { \ t } ~ t ) ~ , ~ \bar { \ t } - p i ~ p i ] ~ , ~ \bar { \ t } ~ = ~ ( \bar { \ a b s } ( \bar { t } ) ~ \bar { \ } ~ \bar { \ t } ~ \mathrm {  ~ \ p i / } 2 ) } } } \\ { { \mathrm { \ o r ~ \mit \ N ~ = ~ 2 * \big [ ~ 1 ~ 3 ~ 5 ~ 7 ~ 2 1 ~ 7 9 \big ] ~ \bar { \ t } ~ 1 } } } \\ { { \mathrm {  ~ \ l ~ \bar { \ t } ~ \ l s o ~ \bar { \ t } { \mit \ c o e f f s } ( \bar { \sf \Phi } ( f , \bar { \ t } ) ~ \ l ) ~ } } } \\ { { \mathrm {  ~ \ f ~ \ l ~ \bar { \ t } ~ \ l e ~ \ b e b f u n ( c , \bar { \ t } ~ \bar { \ t } - p i ~ \bar { \ t } ] ~ , ~ \bar { \ t } ~ \mathrm { c o e f f s ^ { \prime } ~ , ~ \bar { \ t } r i g ^ { \prime } ) } } } } \\ { { \mathrm {  ~ \ p l o t ~ \ \bar { \ t } ~ \ i n t e r v a l ~ \bar { \ } ~ , ~ \bar { \ t } ~ \ l o ~ 4 * \ p i \big ] ~ } } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/65ac9ac4788532cc9248c8f85e8187915a990c3313f0c7a513532956c7cee921.jpg)  
Figure B.8: Circular convolution of a noisy function with a smooth mollifier.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/ba29bcb64c1a21ac510e18069bfb8f10b5587ea7ec04aef9c25dd39d34c2b9b9.jpg)  
Figure B.9: On the left, a figure from Runge’s 1904 book Theorie und Praxis der Reihen [25]. On the right, the equivalent computed with periodic Chebfun. Among other things, this figure illustrates that a trigfun can be accurately evaluated outside its interval of definition.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/e232bbdf411f89c5d4b335957ee6abbe78ff8c6bb0f67f76d494a5c0a9c716d8.jpg)  
Figure B.10: Trigonometric interpolation of $| t |$ in unequally spaced points with the generalized barycentric formula implemented in chebfun/interp1.

Interpolation in unequally spaced points. Very little attention has been given to trigonometric interpolation in unequally spaced points, but the barycentric formula (B.16) for odd $N$ and Henrici’s generalization for even $N$ have been generalized to this case by Berrut [5]. Chebfun makes these formulas available through the command chebfun.interp1, just as has long been true for interpolation by algebraic polynomials. For example, the code

interpolates the function $| t |$ on $[ - \pi , \pi ]$ in the 9 points indicated by a trigonometric polynomial of degree $n = 4$ . The interpolant is shown in Figure B.10 together with the analogous curve for equispaced points.

Best approximation, Carath´eodory–Fej´er approximation, and rational functions. Chebfun has long had a dual role: it is a tool for computing with functions and also a tool for exploring principles of approximation theory, including advanced ones. The trigonometric side of Chebfun extends this second aspect to periodic problems. For example, Chebfun’s new trigremez command can compute best approximants with equioscillating error curves as described in Theorem B.3 [17]. Here is an example that generates the error curve displayed in Figure B.11, with error 12.1095909:

$$
\begin{array} { l } { \mathbf { f } ~ = ~ \mathrm { c h e b f u n } ( ^ { \prime } 1 / ( 1 . 0 1 \mathrm { - } \mathrm { s i n } ( \mathrm { t - } 2 ) ) ^ { \prime } , ~ [ 0 ~ 2 \mathrm { * p i } ] , ~ ^ { \prime } \mathrm { t r i g } ^ { \prime } ) } \\ { \mathbf { p } ~ = ~ \mathrm { t r i g r e m e z } ( \mathbf { f } , 1 0 ) , ~ \mathbf { p } \mathbf { l o t } ( \mathbf { f } - \mathbf { p } ) } \end{array}
$$

Chebfun is also acquiring other capabilities for trigonometric polynomial and rational approximation, including Carath´eodory–Fej´er near-best approximation via singular values of Hankel matrices, and these will be described elsewhere.

# B.7 Periodic ODEs, operator exponentials, and eigenvalue problems

A major capability of Chebfun is the solution of linear and nonlinear ODEs, as well as integral equations, by applying the backslash command to a “chebop” object. We have extended these capabilities to periodic problems, both scalars and systems. See [13] for the theory of existence and uniqueness of solutions to periodic ODEs, which goes back to Floquet in the 1880s, a key point being the avoidance of nongeneric configurations corresponding to eigenmodes.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/342345daaa48bc6dc3cdac2419f11f37bfddbd1ec780ceaa30645f34f4fae0cd.jpg)  
Figure B.11: Error curve in degree $n = 1 0$ best trigonometric approximation to $f ( t ) =$ $1 / ( 1 . 0 1 - \sin ( t - 2 ) )$ over $[ 0 , 2 \pi ]$ . The curve equioscillates between $2 n + 2 = 2 2$ alternating extrema.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/2e553a1bc621c1f29fdfddae4afeaad59a1d660045144020b4ff3fb88a49d8d0.jpg)  
Figure B.12: Solution of the linear periodic ODE (B.32) as a trigfun of degree 168, computed by an automatic Fourier spectral method.

Chebfun’s algorithm for linear ODEs amounts to an automatic spectral collocation method wrapped up so that the user need not be aware of the discretization. With standard Chebfun, these are Chebyshev spectral methods, and now with the periodic extension, they are Fourier spectral methods [9]. The problem is solved on grids of size 32, 64, and so on until the system judges that the Fourier coefficients have converged down to the level of noise, and the series is then truncated at an appropriate point.

For example, consider the problem

$$
0 . 0 0 1 ( u ^ { \prime \prime } + u ^ { \prime } ) - \cos ( t ) u = 1 , \qquad 0 \leq t \leq 6 \pi ,
$$

with periodic boundary conditions. The following Chebfun code produces the solution plotted in Figure B.12 in half a second on a laptop. Note that the trigonometric discretizations are invoked by the flag L.bc $=$ 'periodic':

$$
\begin{array} { l } { \mathrm { L ~ = ~ c h e b o p } ( 0 , 6 * \mathrm { p i } ) } \\ { \mathrm { L . o p ~ = ~ \Theta ^ { } ( x , u ) ~ 0 . 0 0 1 * d i f f ( u , 2 ) ~ + ~ 0 . 0 0 1 * d i f f ( u ) ~ - ~ \cos { ( x ) * u } ~ } } \\ { \mathrm { L . b c ~ = ~ \Omega ^ { * } ~ p e r i o d i c ^ { * } } } \\ { \mathrm { u ~ = ~ L \backslash { 1 } } } \end{array}
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/ad106ca66e2e4a4b0f5f9566a84a8d31b711a4d121ff59230565704c454fd76b.jpg)  
Figure B.13: Solution of the nonlinear periodic ODE (B.33) computed by iterating the Fourier spectral method within a continuous form of Newton iteration. Executing max(diff(u)) shows that the maximum of $u ^ { \prime }$ is 32.094.

This trigfun is of degree 168, and the residual reported by norm(L\*u-1) is $1 \times 1 0 ^ { - 1 2 }$ As always, $u$ is a chebfun; its maximum, for example, is $\mathtt { m a x } ( \mathtt { u } ) = 6 6 . 9 2 8$ .

For periodic nonlinear ODEs, Chebfun applies trigonometric analogues of the algorithms developed by Driscoll and Birkisson in the Chebyshev case [7, 8]. The whole solution is carried out by a Newton or damped Newton iteration formulated in a continuous mode (“solve then discretize” rather than “discretize then solve”), with Jacobian matrices replaced by Fr´echet derivative operators implemented by means of automatic differentiation and automatic spectral discretization. For example, suppose we seek a solution of the nonlinear problem

$$
0 . 0 0 4 u ^ { \prime \prime } + u u ^ { \prime } - u = \cos ( 2 \pi t ) , \qquad t \in [ - 1 , 1 ] ,
$$

with periodic boundary conditions. After seven Newton steps, the Chebfun commands below produce the result shown in Figure B.13, of degree $n = 3 6 2$ , and the residual norm norm(N(u)-rhs,'inf') is reported as $8 \times 1 0 ^ { - 9 }$ :

$$
\begin{array} { l } { { \mathrm { ~ N ~ = ~ c h e b o p ( - 1 , 1 ) ~ } } } \\ { { \mathrm { ~ N . o p ~ = ~ \mathbb { Q } ( x , u ) ~ \Lambda . ~ 0 0 4 * d i f f \left( u , 2 \right) ~ + ~ u * d i f f \left( u \right) ~ - ~ u } } } \\ { { \mathrm { ~ N . b c ~ = ~ \Lambda ^ \ast { p e r i o d i c } ^ { \ast } ~ } } } \\ { { \mathrm { ~ r h s ~ = ~ c h e b f u n ( \Lambda ^ \ast \cos { ( 2 * p i * t ) } ~ \Lambda ^ \ast { t r i g } ^ { \ast } ) ~ } } } \\ { { \mathrm { ~ u ~ = ~ \mathbb { N } \backslash r h s ~ } } } \end{array}
$$

Chebfun’s overload of the MATLAB eigs command solves linear ODE eigenvalue problems by, once again, automated spectral collocation discretizations [11]. This too has been extended to periodic problems, with Fourier discretizations replacing Chebyshev. For example, a famous periodic eigenvalue problem is the Mathieu equation

$$
- u ^ { \prime \prime } + 2 q \cos ( 2 t ) u = \lambda u , \qquad t \in [ 0 , 2 \pi ] ,
$$

where $q$ is a parameter. The commands below give the plot shown in Figure B.14:

$$
\begin{array} { l } { { \mathrm {  ~ q ~ = ~ 2 ~ \mit } } } \\ { { \mathrm {  ~ L ~ \mit = ~ \ c h e b o p { ( \mathfrak { O } ( x , u ) ~ \mathrm {  ~ \bar { \ c } d i f f ( u , 2 ) } + 2 \ast q \ast c o s ( 2 \ast x ) \ast u , ~ [ 0 ~ 2 \ast p i ] ~ , ~ \mathrm {  ~ \bar { \ p e r i o d i c } } } } } } \end{array}
$$

So far as we know, Chebfun is the only system offering such convenient solution of ODEs and related problems, now in the periodic as well as the nonperiodic case.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/ee806050cd09a3647916dd824f938ce6cfc21503be16a5704e5985031e3b4ff8.jpg)  
Figure B.14: First five eigenfunctions of the Mathieu equation (B.34) with $q = 2$ , computed with eigs.

We have also implemented a periodic analogue of Chebfun’s expm command for computing exponentials of linear operators, which we omit from discussion here for reasons of space. All the capabilities mentioned in this section can be explored with Chebgui, the graphical user interface written by Birkisson, which now invokes trigonometric spectral discretizations when periodic boundary conditions are specified.

# B.8 Discussion

Chebfun is an open-source project written in MATLAB and hosted on GitHub; details and the user’s guide can be found at www.chebfun.org [12]. About 30 people have contributed to its development over the years and, at present, there are about 10 developers based mainly at the University of Oxford. During 2013–2014 the code was redesigned and rewritten as version 5 (first released June 2014) in the form of about 100,000 lines of code realizing about 40 classes. The aim of this redesign was to enhance Chebfun’s modularity, clarity, and extensibility, and the introduction of periodic capabilities, which had not been planned in advance, was the first big test of this extensibility. We were pleased to find that the modifications proceeded smoothly. The central new feature is a new class @trigtech in parallel to the existing @chebtech1 and @chebtech2, which work with polynomial interpolants in first- and second-kind Chebyshev points, respectively.

About half the classes of Chebfun are concerned with representing functions, and the remainder are mostly concerned with ODE discretization and automatic differentiation for solution of nonlinear problems, whether scalar or systems, possibly with nontrivial block structure. The incorporation of periodic problems into this second, more advanced part of Chebfun was achieved by introducing a new class @trigcolloc matching @chebcolloc1 and @chebcolloc2.

About a dozen software projects in various computer languages have been modeled on Chebfun, and a partial list can be found at www.chebfun.org. One of these, Fourfun, is a MATLAB system for periodic functions developed independently of the present work by K. McLeod [20], a student of former Chebfun developer R. Platte. Another that also has periodic and differential equations capabilities is ApproxFun, written in Julia by S. Olver and former Chebfun developer A. Townsend [22].18 We think the enterprise of numerical computing with functions is here to stay, but we cannot predict what systems or languages may be dominant, say, 20 years from now. For the moment, only Chebfun offers the breadth of capabilities entailed in the vision of MATLAB-like functionality for continuous functions and operators in analogy to the long-familiar methods for discrete vectors and matrices.

In this article we have not discussed Chebfun computations with twodimensional periodic functions, which are under development. For example, we are investigating capabilities for solution of time-dependent PDEs on a periodic spatial domain and for PDEs in two space dimensions, one or both of which are periodic. A particularly interesting prospect is to apply such representations to computation with functions on disks and spheres.

For computing with vectors and matrices, although MATLAB codes are rarely the fastest in execution, their convenience makes them nevertheless the best tool for many applications. We believe that Chebfun, including now its extension to periodic problems, plays the same role for numerical computing with functions.

# Acknowledgments

This work was carried out in collaboration with the rest of the Chebfun team, whose names are listed at www.chebfun.org. Particularly active in this phase of the project have been Anthony Austin, Asgeir Birkisson, Toby Driscoll, Nick Hale, ´ Hrothgar (an Oxford graduate student who has just a single name), Alex Townsend, and Kuan Xu. We are grateful to all of these people for their suggestions in preparing this paper. The first author would like to thank the Oxford University Mathematical Institute and, in particular, the Numerical Analysis Group, for hosting and supporting his sabbatical visit in 2014, during which this research was initiated.

# Bibliography

[1] J. L. Aurentz, T. Mach, R. Vandebril, and D. S. Watkins, Fast and backward stable computation of roots of polynomials, SIAM J. Matrix Anal. Appl., 36 (2005), pp. 942–973.   
[2] A. P. Austin, P. Kravanja and L. N. Trefethen, Numerical algorithms based on analytic function values at roots of unity, SIAM J. Numer. Anal., 52 (2014), pp. 1795–1821.   
[3] A. P. Austin and K. Xu, On the numerical stability of the second barycentric formula for trigonometric interpolation in shifted equispaced points, IMA J. Numer. Anal., 37 (2017), pp. 1355–1374.   
[4] Z. Battles and L. N. Trefethen, An extension of MATLAB to continuous functions and operators, SIAM J. Sci. Comput., 25 (2004), pp. 1743–1770.   
[5] J.-P. Berrut, Baryzentrische Formeln zur trigonometrischen Interpolation (I), J. Appl. Math. Phys., 35 (1984), pp. 91–105.   
[6] J.-P. Berrut and L. N. Trefethen, Barycentric Lagrange interpolation, SIAM Rev., 46 (2004), pp. 501–517.   
[7] A. Birkisson and T. A. Driscoll, Automatic Fr´echet differentiation for the numerical solution of boundary-value problems, ACM Trans. Math. Software, 38 (2012), 26.   
[8] A. Birkisson and T. A. Driscoll, Automatic Linearity Detection, preprint, http://eprints.maths.ox.ac.uk, 2013.   
[9] J. P. Boyd, Chebyshev and Fourier Spectral Methods, 2nd ed., Dover, Mineola, NY, 2001.   
[10] P. J. Davis, On the numerical integration of periodic analytic functions, in On Numerical Integration, R. E. Langer, ed., University of Wisconsin Press, Madison, WI, 1959, pp. 45–59.   
[11] T. A. Driscoll, Automatic spectral collocation for integral, integrodifferential, and integrally reformulated differential equations, J. Comput. Phys., 229 (2010), pp. 5980–5998.   
[12] T. A. Driscoll, N. Hale, and L. N. Trefethen, Chebfun Guide, Pafnuty Publications, Oxford, 2014; also available online at www.chebfun.org.   
[13] M. S. P. Eastham, The Spectral Theory of Periodic Differential Equations, Scottish Academic Press, Edinburgh, 1973.   
[14] G. Faber, Uber stetige Funktionen ¨ , Math. Ann., 69 (1910), pp. 372–443.   
[15] C. F. Gauss, Theoria interpolationis methodo nova tractata, in C. F. Gauss, Werke, Bd. 3, K¨oniglichen Gesellschaft der Wissenschaften, G¨ottingen, Germany, 1866, pp. 265–327.   
[16] P. Henrici, Barycentric formulas for interpolating trigonometric polynomials and their conjugates, Numer. Math., 33 (1979), pp. 225–234.   
[17] M. Javed and L. N. Trefethen, The Remez Algorithm for Trigonometric Approximation of Periodic Functions, unpublished preprint.   
[18] Y. Katznelson, An Introduction to Harmonic Analysis, Dover, New York, 1968.   
[19] R. Kress, Ein ableitungsfreies Restglied f¨ur die trigonometrische Interpolation periodischer analytischer Funktionen, Numer. Math., 16 (1971), pp. 389–396.   
[20] K. N. McLeod, Fourfun: A new system for automatic computations using Fourier expansions, SIAM Undergrad. Res. Online, 7 (2014), pp. 330–351.   
[21] G. Meinardus, Approximation of Functions: Theory and Numerical Methods, Springer, Berlin, 1967.   
[22] S. Olver and A. Townsend, A practical framework for infinite-dimensional linear algebra, in Proceedings of the First Workshop for High Performance Technical Computing in Dynamic Languages, IEEE Press, Piscataway, NJ, 2014, pp. 57–62.   
[23] R. B. Platte, L. N. Trefethen, and A. B. J. Kuijlaars, Impossibility of fast stable approximation of analytic functions from equispaced samples, SIAM Rev., 53 (2011), pp. 308–318.   
[24] C. Runge, Uber empirische Funktionen und die Interpolation zwischen ¨ ¨aquisitanten Ordinaten, Z. Math. Phys., 46 (1901), pp. 224–243.   
[25] C. D. T. Runge, Theorie und Praxis der Reihen, reprint, VKM Verlag, Saarbr¨ucken, 2007.   
[26] H. E. Salzer, Coefficients for facilitating trigonometric interpolation, J. Math. Phys., 27 (1948), pp. 274–278.   
[27] L. N. Trefethen, Computing numerically with functions instead of numbers, Commun. ACM, 28 (2015), pp. 91–97.   
[28] L. N. Trefethen, Approximation Theory and Approximation Practice, SIAM, Philadelphia, 2013.   
[29] L. N. Trefethen and J. A. C. Weideman, The exponentially convergent trapezoidal rule, SIAM Rev., 56 (2014), pp. 385–458.   
[30] A. Zygmund, Trigonometric Series, Cambridge University Press, Cambridge, UK, 1959.

# Appendix C. “ATAP for the Unit Disk”

[This article was first published by the Society for Industrial and Applied Mathematics (www.siam.org): A. P. Austin, P. Kravanja, and L. N. Trefethen (2014), Numerical algorithms based on analytic function values at roots of unity, SIAM J. Numer. Anal. 52, no. 4, 1795–1821.]

# C.1 Introduction and the unit disk filter function

The title of this paper suggests a narrow topic, but in fact our aim is a broad one: to present a set of ideas underlying certain numerical algorithms used across computational science. In each application, each geometry, it is easy to get lost in details particular to the problem at hand. But the common threads are remarkable, and concentrating our attention on analytic functions at roots of unity on the unit disk will help us to see them. Figure C.1 summarizes the problems and algorithms we shall discuss. From analytic functions on the unit disk one can reach out to generalizations including harmonic functions [16], matrix-valued functions [70], noncircular geometries [24], irregular sample points [41], nonsmooth functions [20], periodic functions with discontinuities [25], dimensions greater than 2 [78], Helmholtz problems [52], integral equations [37], radial basis functions (RBFs) [26], nonlinear partial differential equations [51], and linear operators [36]. (The references just given are a mix of mathematical classics and numerical state of the art.) We offer this list with the thought in mind that researchers may find it fruitful, in investigating some of these variants, to use the present paper as a template.

Throughout this paper, $n$ is a positive integer and $\left\{ \boldsymbol { z } _ { k } \right\}$ , $0 \leq k \leq n - 1$ , are the $n$ th roots of unity, $z _ { k } = \exp ( 2 \pi i k / n )$ . We let $S$ denote the unit circle, $D$ the open unit disk, and $D _ { R }$ the open disk $\{ z \in C : | z | < R \}$ . The function $f$ is assumed to be analytic in $D _ { R }$ but not $\overline { { D } } _ { R }$ for some $R > 1$ , and $\left\{ f _ { k } \right\}$ are its sampled values $f _ { k } = f ( z _ { k } )$ . The symbol $P _ { n - 1 }$ denotes the set of polynomials of degree at most $n - 1$ .

<table><tr><td></td><td>Polynomial interpolation Méray 1884</td><td>Discrete Cauchy integral Lyness-Delves 1967</td><td>Linearized rational interpolation</td></tr><tr><td rowspan="2">Derivatives or</td><td>Walsh 1935 Henrici 1982 Gutknecht 1986 Boyd 2013 [P],[P*]</td><td>[c]</td><td>Gonnet-Pachon-Tref. 2011 Pachón-Gonnet-V.Deun 2012 [ratdisk]</td></tr><tr><td>Ioakimidis-Pap.-Perd.1991</td><td>Lyness-Sande 1971 Henrici 1979 Fornberg 1981 Bornemann 2011 Ioakimidis-Pap.-Perd.1991</td><td></td></tr><tr><td>Zeros and poles</td><td>Corless 2004 Amiraslani 2006 Townsend 2012</td><td>McCune 1966 Delves-Lyness 1967 Burniston-Siewert 1973 Henrici 1979 Ioakimidis 1985 Anastasselou 1986 Kravanja-Sak.-V.Barel1999 Kravanja-Van Barel 1999 Kravanja-Van Barel 2000</td><td></td></tr><tr><td rowspan="2">Matrix eigenvalues</td><td>[Pz],[Pz*]</td><td>Luck-Stevens 2002 [Cz1],[Cz2],[Cp] Goedecker 1999 Sakurai-Sugiura 2003</td><td>[ratdisk_K],[ratdisk]</td></tr><tr><td></td><td>Sakurai-Tadano 2007 Polizzi 2009 Ikegami-Sakurai 2010 Asakura et al. 2009</td><td></td></tr><tr><td></td><td>[det]</td><td>Beyn 2012</td><td>[res],[ratdisk]</td></tr></table>

A certain simple function will have special importance in our discussion, which one might call the unit disk filter function:19

$$
b ( z ) = { \frac { 1 } { 1 - z ^ { n } } } = \prod _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } } { z _ { k } - z } } .
$$

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/72153cde0d7fc6f256e90bc9820dd997ec8fd5c3e209f47f45cd52e5dc9e2bd5.jpg)  
Figure C.2: Absolute value of the unit disk filter function $b ( z )$ of $( C . 1 )$ for $n = 3 2$ . As $n  \infty$ , the function converges to $^ { 1 }$ for $| z | < 1$ and $_ 0$ for $| z | > 1$ , but there is always a ring of poles along the unit circle.

This is a rational function with $n$ poles and no zeros, apart from a zero of multiplicity $n$ at $z = \infty$ . Figure C.2 illustrates the shape of $b ( z )$ in the complex plane, with values $b ( z ) \approx 1$ inside $D$ and $b ( z ) \approx 0$ outside. The separation between the two regions is effected by a cage of poles along the unit circle. The pole at $z _ { k }$ has residue

$$
\mathrm { R e s } _ { k } = - \frac { z _ { k } } { n } ,
$$

and thus each individual pole gets weaker as $n  \infty$ . In the limit, pointwise for each $z$ with $| z | \neq 1$ , we have

$$
\operatorname* { l i m } _ { n \to \infty } b ( z ) = { \left\{ \begin{array} { l l } { 1 , } & { | z | < 1 , } \\ { 0 , } & { | z | > 1 . } \end{array} \right. }
$$

# C.2 Evaluating a function and its derivatives in the unit disk

# C.2.1 Two algorithms for evaluating a function

We begin with the most basic of all computational problems. Suppose $z \in D$ is given and we wish to evaluate $f ( z )$ approximately based on the values $\left\{ f _ { k } \right\}$ . Here are two good algorithms, whose interplay will resonate throughout this paper. A third approach, based on rational rather than polynomial interpolation, will be introduced in Sections C.4 and C.5 and considered more squarely in Section C.6.

Algorithm P. Polynomial interpolation. Approximate $f ( z )$ by $p ( z )$ , where $p \in P _ { n - 1 }$ is the unique polynomial interpolant to $f$ in the points $\left\{ z _ { k } \right\}$ .

Algorithm C. Discrete Cauchy integral. Approximate $f ( z )$ by the trapezoidal rule discretization in the points $\left\{ \boldsymbol { z } _ { k } \right\}$ of the integral $( 2 \pi i ) ^ { - 1 } \int _ { S } ( \zeta - z ) ^ { - 1 } f ( \zeta ) d \zeta$ .

Both algorithms make use of exactly the same data $\left\{ f _ { k } \right\}$ , and both, as we shall see in Section C.2.4, deliver results that converge geometrically to $f ( z )$ as $n \to \infty$ . Indeed, one’s first thought might be, Are these two different descriptions of the same method? But they are not the same. We shall see that Algorithm C approximates $f ( z )$ not by a polynomial but by the rational function

$$
r ( z ) = { \frac { p ( z ) } { 1 - z ^ { n } } } = b ( z ) p ( z ) .
$$

Thus the result of Algorithm C is the same as that of Algorithm P, but multiplied by the filter function (C.1), which introduces poles at all the roots of unity (except if a sample value $f _ { k }$ happens to be zero). In this paper we shall consider the significance of this relationship from several angles.

In the special case $z = 0$ , $b ( z )$ takes the value 1, and the results of Algorithms $\mathrm { P }$ and C are identical. This is the case that has gotten the most attention in the literature, beginning with work in the 1960s by Lyness and his coauthors, which may partly explain why, amid many publications that discuss algorithms of type C, it is hard to find many that discuss algorithms of type P (see, however, [12, Chapter 5]). Yet for $z \neq 0$ , not only are P and C different, but $\mathrm { P }$ is much more accurate for $| z | \approx 1$ (Theorem C.1). At the data points $\left\{ { z } _ { k } \right\}$ themselves, $\mathrm { P }$ returns exactly correct results, whereas C makes errors of infinite magnitude.

A practical situation where evaluation of a function $f$ from samples on a circle is useful is in problems where accurate direct computation of $f ( z )$ in floating-point arithmetic is impossible because of rounding errors. For an elementary example, consider the evaluation of a “phi function” like $( e ^ { z } - 1 - z ) / z ^ { 2 }$ , a problem of practical importance not only for scalars $z$ but also for matrices [51, 76].

# C.2.2 Barycentric formulas for the two algorithms

To derive formulas for the polynomial interpolant $p$ of algorithm P, one may first define the node polynomial

$$
\ell ( z ) = \prod _ { k = 0 } ^ { n - 1 } ( z - z _ { k } ) = z ^ { n } - 1
$$

and the barycentric weights

$$
\lambda _ { k } = { \frac { 1 } { \ell ^ { \prime } ( z _ { k } ) } } = { \frac { z _ { k } } { n } } .
$$

These give the degree $n - 1$ cardinal polynomial

$$
\ell _ { k } ( z ) = \ell ( z ) \frac { \lambda _ { k } } { z - z _ { k } } = \frac { 1 } { n } \ell ( z ) \frac { z _ { k } } { z - z _ { k } }
$$

for any $k$ , taking the values $^ { 1 }$ at $z = z _ { k }$ and $0$ at the other roots of unity. From (C.7) it follows that the interpolant $p$ can be written in Lagrange form as

$$
p ( z ) = { \frac { 1 } { n } } \ell ( z ) \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } f _ { k } } { z - z _ { k } } } ,
$$

and this is the barycentric formula of the first kind. Here it is to be understood that if $z = z _ { k }$ for some $k$ , then the use of the formula is replaced by the exact value $f _ { k }$ . A similar qualification applies to (C.7) and other formulas in this paper involving

divisions by $z - z _ { k }$ . The resulting polynomial evaluation algorithms are known to be numerically stable [40].

In particular, if $f \equiv 1$ , then its polynomial interpolant is the constant function $p \equiv 1$ , which we can write in the form (C.8) as

$$
1 = { \frac { 1 } { n } } \ell ( z ) \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } } { z - z _ { k } } } .
$$

If (C.8) is divided by (C.9), the factors $n ^ { - 1 } \ell ( z )$ in the numerator and denominator cancel, giving the elegant identity

$$
p ( z ) = \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } f _ { k } } { z - z _ { k } } \Bigg / \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } } { z - z _ { k } } ,
$$

the barycentric formula of the second kind, or in MATLAB,

$$
\mathtt { p z } = \mathtt { m e a n } ( \mathtt { z k . * f k . } / ( \mathtt { z - z k } ) ) / \mathtt { m e a n } ( \mathtt { z k . } / ( \mathtt { z - z k } ) ) .
$$

The work involved is $O ( n )$ operations. Here and in all the MATLAB formulas of this article, $_ { z \mathrm { k } }$ is a column vector containing the $n$ th roots of unity, $z _ { k } = \exp ( 2 \pi i k / n )$ , $0 \leq k \leq n - 1$ , and $\mathtt { f k }$ is the corresponding column vector of values $f _ { k }$ .

The use of the barycentric formula falls in the category of a calculation “by values.” It is equally possible to evaluate $p ( z )$ “by coefficients.” The Taylor coefficients can be computed by the Fast Fourier Transform (FFT), and the algorithm for evaluating $p ( z )$ becomes

$$
\mathsf { c } ~ = ~ \mathsf { f f t } \left( \mathsf { f k } \right) / \mathrm { n } , ~ \mathsf { p z } ~ = ~ \mathsf { p o l y v a l } \left( \mathsf { f l i p u d } \left( \mathsf { c } \right) , \mathsf { z } \right) ,
$$

requiring $O ( n \log n )$ operations, with $O ( n )$ additional operations for each point $z$ after the first one. The formulas behind [P\*] appear in the next section.

We now turn to Algorithm C. The trapezoidal rule formula is [63]

$$
r ( z ) = - { \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } f _ { k } } { z - z _ { k } } } ,
$$

or in MATLAB,

$$
\tt r z = - m e a n ( z k . * f k . / ( z - z k ) ) ,
$$

again with $O ( n )$ operations. Comparing (C) with (C.8), we see that the discrete Cauchy integral approximation to $f ( z )$ is

$$
r ( z ) = - { \frac { p ( z ) } { \ell ( z ) } } ,
$$

and since $- 1 / \ell ( z ) = b ( z )$ , this confirms (C.4). Note that $r$ is a rational function of type $( n - 1 , n )$ , meaning that it has at most $n - 1$ finite zeros (unless it is identically zero) and at most $n$ finite poles, counted with multiplicity, with a zero of order at least $^ { 1 }$ at $z = \infty$ .

# C.2.3 Taylor projections and polynomial interpolants

Suppose $f$ is analytic in $D _ { R }$ for some $R > 1$ . Then it has a Taylor series

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }
$$

with coefficients given by the Cauchy integrals

$$
a _ { k } = { \frac { 1 } { 2 \pi i } } \int _ { S } \zeta ^ { - k - 1 } f ( \zeta ) d \zeta .
$$

Since $f$ is bounded in $D _ { \rho }$ for any $\rho < R$ , Cauchy’s estimate gives

$$
\left| a _ { k } \right| = O ( \rho ^ { - k } ) , \quad k \to \infty .
$$

If we truncate the series to the degree $n - 1$ Taylor section

$$
f _ { n - 1 } ( z ) = \sum _ { k = 0 } ^ { n - 1 } a _ { k } z ^ { k } ,
$$

it follows that for any $z \in D _ { R }$ and $\rho$ with $| z | < \rho < R$ we have

$$
| f _ { n - 1 } ( z ) - f ( z ) | = O ( ( | z | / \rho ) ^ { n } ) , \quad n \to \infty ,
$$

uniformly for all $z$ in each closed disk of radius $< \rho$ about the origin.

In this paper our interest is not Taylor sections $f _ { n - 1 }$ but polynomial interpolants $p _ { n - 1 }$ . (We use the labels $p$ and $p _ { n - 1 }$ interchangeably.) If we write $p _ { n - 1 }$ in the form

$$
p _ { n - 1 } ( z ) = \sum _ { k = 0 } ^ { n - 1 } c _ { k } z ^ { k } ,
$$

then the coefficients $\{ a _ { k } \}$ and $\left\{ c _ { k } \right\}$ are related by the aliasing identity

$$
c _ { k } = a _ { k } + a _ { k + n } + a _ { k + 2 n } + \cdots , \quad 0 \leq k \leq n - 1 .
$$

by its alias In words, $p _ { n - 1 }$ $a _ { k } z ^ { k ( \mathrm { m o d } \ n ) }$ is obtained from . By (C.13) this implies $f$ by replacing each term $a _ { k } z ^ { k }$ in the series (C.11)

$$
| p _ { n - 1 } ( z ) - f ( z ) | = O ( \rho ^ { - n } ) , \quad | z | \leq 1 ,
$$

as $n  \infty$ for any $\rho < R$ , since the leading term of the error is the first of the aliases, $a _ { n } z ^ { 0 }$ , and $a _ { n } = O ( \rho ^ { - n } )$ . For $1 < | z | < R$ , the leading term of the error becomes $- a _ { n } z ^ { n }$ , of order $O ( | z | ^ { n } \rho ^ { - n } )$ , so we get

$$
| p _ { n - 1 } ( z ) - f ( z ) | = O ( | z | ^ { n } \rho ^ { - n } ) , \quad 1 \leq | z | < \rho ,
$$

for any $\rho < R$ . Again these bounds hold uniformly for all $z$ in each closed disk of radius $< \rho$ about the origin.

If the Taylor coefficients $\{ a _ { k } \}$ , $0 \leq k \leq n - 1$ , are approximated by applying the trapezoidal rule to (C.12), the same aliasing occurs, and so the resulting coefficients are $\left\{ c _ { k } \right\}$ . It is this property that led to the FFT-based algorithm [P\*], which utilizes the fact that the FFT computes all $n$ trapezoidal rule approximations at once.

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/3dd94186b259e67a3008c6f265378d27073d72407fcc44ec7e42b9c8c9963e4a.jpg)  
Figure C.3: Error plot for approximations with $n = 3 2$ to $f ( z ) = \log ( 1 . 2 - z )$ by Algorithms P (left) and C (right), with the unit circle marked by a black curve and the branch point at $z = 1 . 2$ marked by a dot. The color bars represent base 10 logarithms. As established in Theorem $C . 1$ , Algorithm P converges throughout $D _ { 1 . 2 }$ as $n \to \infty$ , whereas Algorithm C converges only in $D$ . Faint white dots reflect exact interpolation at the $n = 3 2$ roots of unity on the left, and on the right, at $n + 1 = 3 3$ points close to a smaller circle (see Section C.2.9). At the roots of unity on the right, the errors are infinite because of the poles introduced by the trapezoidal rule.

# C.2.4 Accuracy of the two algorithms

The observations of the foregoing pages are summarized in the following theorem. For a general discussion of the geometric convergence of the trapezoidal rule for periodic analytic integrands, see [85].

Theorem C.1. Let $f$ be analytic in $D _ { R }$ for some $R > 1$ . Then as $n \to \infty$ , for any with $1 < \rho < R$ , the approximation of algorithm $\mathrm { P }$ has accuracy $\rho$

$$
| p ( z ) - f ( z ) | = { \left\{ \begin{array} { l l } { O ( \rho ^ { - n } ) , } & { | z | \leq 1 , } \\ { O ( | z | ^ { n } \rho ^ { - n } ) , } & { 1 \leq | z | < \rho , } \end{array} \right. }
$$

whereas algorithm $C$ gives

$$
| r ( z ) - f ( z ) | = \left\{ { O } ( \rho ^ { - n } ) , \quad | z | \leq R ^ { - 1 } , \right.
$$

These bounds hold uniformly for all $z$ in each closed disk of radius $< \rho$ about the origin.

Proof. Equation (C.20) was already given as (C.18) and (C.19). Equation (C.21) follows from this together with (C.4), since $1 - ( 1 - z ^ { n } ) ^ { - 1 } = O ( | z | ^ { n } )$ as $n \to \infty$ for each $z$ with $| z | < 1$ .

Let us look at these conclusions in a numerical example. In Figure C.3, the function $f ( z ) = \log ( 1 . 2 - z )$ has been approximated by Algorithms $\mathrm { P }$ and C with $n = 3 2$ . The figure plots the error $| f ( z ) - p ( z ) |$ or $\left| f ( z ) - r ( z ) \right|$ in each approximation, revealing that $\mathrm { P }$ is accurate in a region considerably larger than the unit disk. This phenomenon, which is predicted by (C.20), is known as overconvergence. Method C, on the other hand, only converges in the unit disk, and near the unit circle it loses accuracy, as predicted in (C.21). To be precise, the estimates indicate that $\mathrm { P }$ is more accurate than C for $| z | > R ^ { - 1 }$ .

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/b259fe1dbaaf88ceaaa19fb7ac69741568933331cd7769c0e500ab5f8e87e230.jpg)  
Figure C.4: Phase portraits (see [88]) for the same two approximations as in Figure $C . 3$ . The image on the left shows $n { - } 2$ zeros of $p$ converging as $n \to \infty$ to $| z | = R = 1 . 2$ , the circle of analyticity for this function, in keeping with Jentzsch’s theorem and its generalization by Walsh (Section C.2.5). (The $( n - 1 ) \mathrm { s t }$ zero converges to the zero of $f$ at $z = 0 . 2$ .) The image on the right shows exactly the same zeros and in addition the $n$ poles at the $n$ th roots of unity of the approximation $r ( z ) = b ( z ) p ( z )$ .

Figure C.4 displays the approximations $p ( z )$ and $r ( z )$ themselves, rather than the associated errors. These images are phase portraits, depicting the phase but not the amplitude of each function: red for positive real, green for positive imaginary, cyan for negative real, and violet for negative imaginary [88]. Within the unit disk, it is apparent that both algorithms approximate the same function $f$ , whose zero at $z = 0 . 2$ shows up as a point where all the colors meet. The differences between the two figures near and outside the unit circle, on the other hand, are pronounced.

The theorems and figures of this section highlight an effect that was foreshadowed in Figure C.2: a Cauchy integral over a contour $\Gamma$ does not just approximate a function in the region enclosed by $\Gamma$ ; it acts to separate that region from the exterior. If such a separation is not part of one’s computational purpose, then the discrete Cauchy integral may not be the best algorithm.

# C.2.5 Zeros, poles, and the Jentzsch and Walsh theorems

A striking feature of Figure C.4 is the ring of colorful stripes in each image outside the unit disk. In both cases, these stripes end at $n - 2 = 3 0$ zeros lying approximately on the circle $| z | = 1 . 3$ , which will shrink to $| z | = 1 . 2$ as $n \to \infty$ . For the polynomial approximant $p ( z )$ on the left, the stripes extend outward to $z = \infty$ , where they meet at the pole of multiplicity $n - 1 = 3 1$ . For the rational approximant $r ( z )$ on the right, they point inward and terminate at the $n = 3 2$ poles on the unit circle.

The appearance of a ring of zeros near the circle of convergence of a Taylor series is a well-known phenomenon. According to Jentzsch’s theorem [49], if $f$ is analytic in $D _ { R }$ but not $\overline { { D } } _ { R }$ , the zeros of Taylor sections $f _ { n - 1 }$ cluster at every point on the circle $| z | = R$ as $n \to \infty$ . (This is a generalization of the phenomenon that the zeros of the partial sum $1 + z + \cdots + z ^ { n - 1 }$ of the Taylor series of $( 1 - z ) ^ { - 1 }$ are the $n$ th roots of unity except $z = 1$ .) In the present case Jentzsch’s theorem is inapplicable, because the polynomials $p _ { n - 1 }$ are interpolants in roots of unity rather than Taylor sections. However, a generalization due to Walsh asserts the same conclusion for any sequence of polynomials that is maximally convergent on $D$ , meaning $\begin{array} { r } { \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \| p _ { n - 1 } - f \| _ { D } ^ { 1 / n } = R ^ { - 1 } } \end{array}$ , where $\| \cdot \| _ { D }$ is the supremum norm on $D$ [86]. By Theorem C.1, polynomial interpolants in roots of unity are maximally convergent, and thus Walsh’s theorem applies to Figure C.4. As $n \to \infty$ , zeros will cluster near every $z$ with $| z | = 1 . 2$ .

# C.2.6 Cauchy integrals of the second kind

The developments of Section C.2.2 suggest a curious observation. In analogy to our progression from (C.8) to (P), we could consider the “Cauchy integral of the second kind”

$$
f ( z ) = \int _ { S } \frac { f ( \zeta ) } { z - \zeta } d \zeta \int _ { S } \frac { 1 } { z - \zeta } d \zeta ,
$$

obtained by dividing the usual Cauchy integral formula for $f$ by the same formula for the case $f \equiv 1$ . Discretizing both the numerator and the denominator of this quotient by the trapezoidal rule then suggests a “discrete Cauchy integral of the second kind,”

$$
\tilde { r } ( z ) = \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } f _ { k } } { z - z _ { k } } \Bigg / \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } } { z - z _ { k } } .
$$

But this is exactly (P)! Thus the discrete Cauchy integral and the polynomial interpolation ideas give the same result after all, if one realizes the former by a nonstandard “second kind” discretization. As Helsing and Ojala put it in the context of an analogous formula for integral equations [37], “One could say that the denominator in this formula compensates for the error in the numerator.” This kind of compensation is familiar to devotees of barycentric formulas, which look numerically unstable at first sight because of their poles but are in fact stable [40].

This multiplicative derivation of (P) may appear rather magical, but a third and more straightforward additive realization of the Cauchy integral idea leads to the same formula. Note that unlike $f ( s ) / ( z - s )$ , the quotient $( f ( z ) - f ( s ) ) / ( z - s )$ has no pole at $s = z$ , so it is an analytic function of $s \in D _ { R }$ , whose Cauchy integral must be equal to zero. A trapezoidal rule discretization of that Cauchy integral accordingly gives

$$
- { \frac { 1 } { n } } \sum _ { k = 0 } ^ { n - 1 } { \frac { z _ { k } { \big ( } f ( z ) - f ( z _ { k } ) { \big ) } } { z - z _ { k } } } \approx 0 ,
$$

and now the summands do not diverge as $z  z _ { k }$ , so one can expect the trapezoidal rule to be more accurate than in (C). Solving for $f ( z )$ in (C.24) gives (C.23) again. This argument has been employed by various authors to derive improved discretizations of integrals near contours [37, 45]. Ioakimidis calls it “the use of the Cauchy theorem instead of the Cauchy formula” [44, 45].

# C.2.7 Derivatives of $f$ or Taylor coefficients

The ideas we have considered for the evaluation of $f ( z )$ extend readily to the evaluation of derivatives $f ^ { ( m ) } ( z )$ for any $m \geq 0$ or, equivalently, the computation of Taylor coefficients. Algorithms $\mathrm { P }$ and $\mathrm { C }$ have the following analogues.

Algorithm $\mathrm { P } ^ { ( m ) }$ . Approximate $f ^ { ( m ) } ( z )$ by $p ^ { ( m ) } ( z )$ , where $p \in \mathcal P _ { n - 1 }$ is the polynomial interpolant to $f$ in $\left\{ { z } _ { k } \right\}$ .

Algorithm $\mathrm { C } ^ { ( m ) }$ . Approximate $f ^ { ( m ) } ( z )$ by the trapezoidal rule discretization in $\left\{ { z } _ { k } \right\}$ of the integral $m ! ( 2 \pi i ) ^ { - 1 } \int _ { S } ( \zeta - z ) ^ { - m - 1 } f ( \zeta ) d \zeta$ .

The same convergence bounds hold as in Theorem C.1, with $\mathrm { P } ^ { ( m ) }$ more accurate than $\mathrm { C } ^ { ( m ) }$ and converging in a larger disk.

MATLAB generalizations of [P], $[ \mathsf { P } { * } ]$ , and [C] can be written as follows for the case $m = 1$ , the first derivative. Formula [P'] evaluates the derivative by a barycentric formula, a technique that originates with [77].

[P'\*]

$$
\begin{array} { r l } & { \mathrm { p z ~ = ~ \ p o n ( z k . * f k . / ( z { - } z k ) ) / m e a n ( z k . / ( z { - } z k ) ) } } \\ & { \mathrm { p p z ~ = ~ \ m e a n ( z k . * ( p z { - } f k ) . / ( z { - } z k ) . ^ { - } 2 ) / m e a n ( z k . / ( z { - } z k ) ) , } } \\ & { \mathrm { c ~ = ~ \ f f t ( t k ) / n , ~ \ c p ~ = ~ \ t ( \ t { - } 1 ) ' . * c ( 2 : e n d ) ~ } } \\ & { \mathrm { p p z ~ = ~ \ p o l y v a l ( f l i i p u d ( c p ) , \boldsymbol z ) , } } \\ & { \mathrm { r p z ~ = ~ \ m e a n ( z k . * f k . / ( z { - } z k ) . ^ { - } 2 ) . } } \end{array}
$$

We shall not discuss these methods at any length, since the mathematics is so close to the case $m = 0$ . However, it is worth noting that it is in the context of derivatives, not function values, that numerical methods based on complex samples are best known, since they eliminate the instabilities that afflict real finite differences. In the words of Lyness and Moler [64], “Once complex arguments are allowed, the principal difficulties encountered in numerical differentiation simply disappear.”

# C.2.8 Scaling of the radius

In this paper we work always with the unit disk and unit circle, but in practice, it is often desirable to vary the radius. According to (C.20), Algorithm P converges approximately at the rate $O ( R ^ { - n } )$ . It follows that if $z$ is rescaled by a factor $\tau < 1$ , so that $f$ is sampled on the circle $| z | = \tau$ , the convergence rate will improve to $O ( ( \tau / R ) ^ { n } )$ . On the other hand, as $\tau$ gets smaller, problems appear of ill-conditioning and rounding errors in floating-point arithmetic. The computation is particularly problematic when one wants to obtain higher Taylor coefficients of $f$ and do so with high relative as opposed to just absolute accuracy. These effects have been noted in this subject from the start, and in the 1980s Fornberg developed an algorithm for determining a good radius adaptively [27]. More recently Bornemann has published a theory showing that an optimal choice of $\tau$ can often eliminate ill-conditioning completely even for very high order derivatives [11].

An interesting extreme case in the matter of choice of radius arises in the method of “complex step differentiation” for computing the first derivative of a real function [80]. Here the grid size is $n = 2$ , using the midpoint rather than the trapezoidal rule, i.e., an imaginary rather than a real finite difference, and the radius $\tau$ is taken smaller than machine epsilon, which is possible since the real and imaginary parts of $z$ and $f ( z )$ are independent floating-point numbers that need not have the same scales.

# C.2.9 The method of fundamental solutions

Let us look again at the faint white spots in Figure C.3, showing points of interpolation. On the left, $f$ is approximated by a polynomial $p \in P _ { n - 1 }$ , which we can think of as a rational function with $n - 1$ poles at $z = \infty$ . The particular approximation in this class is determined by the condition of interpolation of $f$ at the $n$ th roots of unity. On the right, $f$ is approximated by a rational function with $n$ poles at the roots of unity, and the white spots show that it interpolates $f$ in a ring of $n + 1$ points lying approximately on a circle of radius 0.8.

These considerations suggest a unifying view of Algorithms $\mathrm { P }$ and C: choose a set of basis functions $\{ ( z - \zeta _ { k } ) ^ { - 1 } \}$ defined by a fixed set of poles $\left\{ \zeta _ { k } \right\}$ , and approximate $f$ by a linear combination of these basis functions determined by interpolation. To fit the framework of this paper, the interpolation points must be the roots of unity. The two algorithms now begin to look like extremes of a continuum, with poles at $\infty$ or on the unit circle. In-between choices could also be considered, such as poles distributed along a circle such as $| z | = 1 . 1$ . This is the method of fundamental solutions, also known as the charge simulation method [6] (and related to the Trefftz method). If one generalizes the idea to the Helmholtz equation, for example, then the appropriate fundamental solutions become Hankel functions rather than rational functions defined by simple poles.

The reason it may be advantageous to place poles near $S$ rather than at $z = \infty$ has to do with ill-conditioning. If one places poles on the circle $| z | = \tau$ for some $\tau$ , the interpolation problem becomes exponentially ill-conditioned as $\tau$ increases, making large finite values of $\tau$ unworkable. It happens that $\tau = \infty$ is well-behaved, because we can represent polynomials by means other than as linear combinations of simple poles, but such well-behaved representations are not always available in more general situations, such as problems on noncircular domains. And so the idea of placing singularities near the boundary of the problem domain is a powerful one. There is always a trade-off between wanting singularities well separated from the boundary, for accuracy, and close to the boundary, for conditioning.

Related issues of ill-conditioning arise in the use of RBFs for approximating functions $f$ or solving differential equations [26]. RBFs differ from fundamental solutions in that they do not exactly satisfy the differential equation under consideration; on the other hand they need not have singular points, and interpolation points can be distributed inside the problem domain as well as outside it. In analogy to the radius $\tau$ for the method of fundamental solutions, there is now a smoothness parameter $\varepsilon$ , and the limit $\varepsilon  0$ is associated with better approximations but worse conditioning.

# C.3 Zerofinding in the unit disk

# C.3.1 Two algorithms for zerofinding

We now turn to the second fundamental problem of this paper, the calculation of the zeros of $f$ within $D$ . This is an inverse of the former problem: instead of determining the value of $f$ at a given point, now we want to find points where $f$ takes a given value. For clarity we will use the letter $w$ to denote a zero. Once again, we begin with two basic ideas, polynomial interpolation and discretized Cauchy integrals.

We shall see that this time, the Cauchy integral has an advantage when $n$ is large. The first idea can be stated immediately. Curiously, there seems to be very little literature on the following simple algorithm; we know only of [12, Chapter 5].

Algorithm $\mathrm { P } ^ { Z }$ . Polynomial interpolation. Approximate $f$ by the polynomial interpolant $p ( z )$ in $\left\{ \boldsymbol { z } _ { k } \right\}$ and compute the zeros of p that lie in $D$ .

The zeros of $p$ can be calculated by computing its coefficients with the discrete Fourier transform, then finding its zeros by solving a companion matrix eigenvalue problem. In MATLAB, the eigenvalue computation is invoked by the roots command:

$$
\left[ \mathbb { P } \mathrm { z } ^ { * } \right] \qquad \textrm { \textsf { c } } = \textrm { f f t } \left( \mathrm { f k } \right) / \mathrm { n } , \textrm { \textsf { w } } = \textrm { r o o t s } \left( \mathrm { f l } \mathrm { i p u d } \left( \mathrm { c } \right) \right) , \textrm { \textsf { w } } = \textrm { w } \left( \mathrm { a b s } \left( \mathrm { w } \right) < 1 \right) .
$$

Alternatively, working from values rather than coefficients [29], one can compute zeros by solving an $( n + 1 ) \times ( n + 1 )$ generalized eigenvalue problem with arrowhead structure [2, 15]. (This approach produces two spurious eigenvalues at $\infty$ as well as the $n - 1$ eigenvalues corresponding to zeros of $p$ .) The following particularly elegant symmetric form has been suggested by Townsend [82]:

[Pz]

$$
\begin{array} { r l } { \mathrm { ~  ~ A ~ } = } & { \left[ 0 \mathrm { f i k . ~ } ^ { \prime } ; \mathrm { f i k ~ } \mathrm { d i a g } ( \mathrm { f k } ) \right] , \mathrm { ~  ~ B ~ } = \mathrm { d i a g } ( \left[ 0 ; \mathrm { f k . ~ } / z \mathrm { k } \right] ) } \\ { \mathrm { ~  ~ w ~ } = } & { \mathrm { e i g } ( \mathrm { A } , \mathrm { B } ) , \mathrm { ~  ~ w ~ } = \mathrm { w } ( \mathrm { a b s } \left( \mathrm { w } \right) < 1 ) . } \end{array}
$$

Both [Pz] and [Pz\*] require $O ( n ^ { 3 } )$ operations.

Like Algorithms $\mathrm { P }$ and $\mathrm { P } ^ { ( m ) }$ , Algorithm $\mathrm { P } ^ { Z }$ converges geometrically, at least when the zeros are simple.

Theorem C.2. Let $f$ be analytic in $D _ { R }$ for some $R > 1$ with exactly $K$ zeros in $D$ , all of them simple, and no zeros with $| z | = 1$ . Then for all sufficiently large $n$ , Algorithm $\mathrm { P } ^ { Z }$ produces exactly $K$ zeros in $D$ , which converge to the zeros of $f$ at the rate $O ( \rho ^ { - n } )$ as $n \to \infty$ for any $\rho < R$ .

Proof. This follows from (C.20) and the fact that simple zeros of analytic functions vary smoothly with analytic perturbations. ■

Another approach to zerofinding is to use a discretized contour integral. Many different integrals are suitable, and we begin with the one that has had the most attention in the literature, involving the logarithmic derivative $f ^ { \prime } / f$ . This approach has roots in the work of Delves and Lyness and was developed more fully by Kravanja and Van Barel, in collaboration with Sakurai [54], [56, Section 1.2]. The next subsection considers the alternative choice $1 / f$ , a derivative-free variant developed by Kravanja and Van Barel [55], [56, Section 1.6].

To simplify the discussion, we begin by assuming that $f$ has exactly one zero $w$ in $D$ and no zeros with $| w | = 1$ . In this case, $w$ is given by the integral

$$
w = { \frac { 1 } { 2 \pi i } } \int _ { S } { \frac { \zeta f ^ { \prime } ( \zeta ) } { f ( \zeta ) } } d \zeta ,
$$

as follows easily from the residue theorem. This formula goes back to the 19th century and was proposed in the computer era by Delves and Lyness [18] and McCune [66]. In analogy to (C) we get

$$
w \approx \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } \frac { z _ { k } ^ { 2 } f _ { k } ^ { \prime } } { f _ { k } } .
$$

For some problems, samples of $f _ { k } ^ { \prime }$ are available and this formula can be used as written. Our convention in this paper, however, is that just $\left\{ f _ { k } \right\}$ are known, in which case $\left\{ f _ { k } ^ { \prime } \right\}$ can be approximated by differentiating the polynomial interpolant as in [P'] or $[ \mathsf { P } ^ { \prime } * ]$ . This gives the following algorithm:

[McCune]

$$
\begin{array} { r l } & { \mathbf { c } ~ = ~ \mathbf { f f t } ( \mathbf { f k } ) / \mathbf { n } , ~ \mathbf { c p } ~ = ~ \left( 1 { : } \mathbf { n - 1 } \right) { : } ~ \mathbf { . } { * } { \mathbf { c } } \left( 2 : \mathbf { e n d } \right) } \\ & { \mathbf { p p } { \mathbf { z } } \mathbf { k } ~ = ~ \mathbf { n } { * } \mathbf { i f f t } ( \left[ \mathbf { c p } { ; } 0 \right] ) , ~ \mathbf { w } ~ = ~ \mathbf { m e a n } ( { \mathbf { z } } \mathbf { k . } { \mathbf { \sigma } } ^ { \sim } 2 . { \boldsymbol { * } } \mathbf { p p } { \mathbf { z } } \mathbf { k } . / \mathbf { f k } ) } \end{array}
$$

Algorithms $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ and [McCune] both work excellently in certain circumstances and converge geometrically, with $[ \mathsf { P } z ]$ , as in Sections C.2.4 and C.2.7, having the better convergence constant. A new feature arises now, however, that gives [McCune] an advantage. As mentioned above, $[ \mathsf { P } z ]$ and $[ \mathsf { P } z ^ { * } ]$ require $O ( n ^ { 3 } )$ operations when implemented by general-purpose solvers, whereas the operation count for [McCune] is just $O ( n \log n )$ . For modest values of $n$ like 32 or 64, this difference may not be very important, but when $n$ is in the hundreds, it becomes significant. For example, the function $f ( z ) = \log ( 1 . 1 - z )$ has a zero $w = 0 . 1$ . For 10-digit accuracy, algorithms $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ require $n = 1 9 0$ sample points and 0.5 sec on a 2012 desktop computer, whereas [McCune] requires $n = 2 4 0$ points but less than 0.001 sec.

This difference between algorithms $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ and [McCune] is rooted in the distinction mentioned in the introduction, Cauchy integrals’ property of separating the region inside the contour from the region outside. Algorithm [Pz] computes all the zeros of a polynomial interpolant, whereas algorithm [McCune] first projects the problem onto the unit disk and then computes only the zeros there. For a problem that is complicated in the large but relatively simple in the disk, this may be much more efficient.

It remains to generalize [McCune] to functions with more than one zero in $D$ . Following [56, Section 1.2], we begin with a generalization of (C.25). Suppose $f$ has $K$ zeros $w _ { 1 } , \ldots , w _ { K }$ in $D$ , which we assume to be simple, and no zeros on $S$ .20 Then for any integer $m \geq 0$ ,

$$
s _ { m } : = \frac { 1 } { 2 \pi i } \int _ { S } \frac { \zeta ^ { m } f ^ { \prime } ( \zeta ) } { f ( \zeta ) } d \zeta = \sum _ { j = 1 } ^ { K } w _ { j } ^ { m } .
$$

Taking $m = 2$ gives the sum of the squares of the zeros, $m = 3$ gives the sum of the cubes, and so on; also $m = 0$ recovers a familiar formula for counting the number of zeros. (These “moment integrals” are the starting point of a theory of formal orthogonal polynomials [19] with respect to the weight function $f ^ { \prime } ( \zeta ) / f ( \zeta )$ [54].) Now consider the $K \times K$ Hankel matrices

$$
H = \left( \begin{array} { c c c } { s _ { 0 } } & { \ldots } & { s _ { K - 1 } } \\ { \vdots } & { } & { \vdots } \\ { s _ { K - 1 } } & { \ldots } & { s _ { 2 K - 2 } } \end{array} \right) , \quad H ^ { < } = \left( \begin{array} { c c c } { s _ { 1 } } & { \ldots } & { s _ { K } } \\ { \vdots } & { } & { \vdots } \\ { s _ { K } } & { \ldots } & { s _ { 2 K - 1 } } \end{array} \right) .
$$

The roots $w _ { 1 } , \ldots , w _ { K }$ are precisely the eigenvalues $\lambda$ of the generalized eigenvalue problem

$$
H ^ { < } x = \lambda H x .
$$

To show this, note that the Hankel matrices can be factored as

$$
\boldsymbol { H } = V V ^ { T } , \quad \boldsymbol { H } ^ { < } = V \mathrm { d i a g } ( w _ { 1 } , \dots , w _ { K } ) V ^ { T } ,
$$

where $V$ is the Vandermonde matrix

$$
V = \left( \begin{array} { c c c } { { 1 } } & { { \dots } } & { { 1 } } \\ { { w _ { 1 } } } & { { \dots } } & { { w _ { K } } } \\ { { } } & { { } } & { { \vdots } } \\ { { w _ { 1 } ^ { K - 1 } } } & { { \dots } } & { { w _ { K } ^ { K - 1 } } } \end{array} \right) .
$$

It is readily verified that the $j$ th column of $V ^ { - T ^ { \prime } }$ is an eigenvector $x$ in (C.29) with eigenvalue $\lambda = w _ { j }$ . If the integrals are approximated by the trapezoidal rule in roots of unity, with $f _ { k } ^ { \prime }$ approximated by polynomial interpolation as in [McCune], this gives us an algorithm for approximating $K$ distinct roots of $f$ in $D$ . The following is a MATLAB realization. Because of the use of the FFT, this algorithm assumes $n \geq 2 K$ , which is not much of a restriction since we would normally expect to have $n \gg K$ when applying any of the algorithms of this article. The same condition arises in the error analysis of this algorithm published in [73].

[Cz1]

$$
\begin{array} { r l } & { \mathrm {  ~ c ~ } = \mathrm {  ~ f f t } ( \mathrm { f } \mathrm { k } ) / \mathrm { n } , \mathrm {  ~ c p ~ } = \mathrm {  ~ ( 1 } { \mathrm {  ~ \cdot n - 1 } } ) \mathrm {  ~ \cdot ~ } \mathrm {  ~ \ast c } ( \mathrm { 2 } : \mathrm { e n d } ) } \\ & { \mathrm { p p z } \mathrm { k } = \mathrm {  ~ n } { \mathrm { \ast } } \mathrm { i } \mathrm { f } \mathrm { f t } ( \mathrm { [ ~ c p ~ } ; 0 \mathrm { ] } ) , \mathrm {  ~ s ~ } = \mathrm { \ i f f t } ( \mathrm { p p z } \mathrm { k } \mathrm {  ~ \cdot ~ } \mathrm { \not { f } \mathrm { k } } ) } \\ & { \mathrm {  ~ H ~ } = \mathrm { \ h a n k e } 1 ( \mathrm { s } ( \mathrm { 2 } : \mathrm { K } { + } \mathrm { 1 } ) , \mathrm {  ~ s } ( \mathrm { K } { + } \mathrm { 1 } : \mathrm { 2 } { \ast } \mathrm { K } ) ) } \\ & { \mathrm {  ~ H 2 ~ } = \mathrm { \ h a n k e } 1 ( \mathrm { s } ( \mathrm { 3 } : \mathrm { K } { + } \mathrm { 2 } ) , \mathrm {  ~ s } ( \mathrm { K } { + } \mathrm { 2 } : \mathrm { 2 } { \ast } \mathrm { K } { + } \mathrm { 1 } ) ) } \\ & { \mathrm {  ~ w ~ } = \mathrm { \ e i g } ( \mathrm { H 2 } , \mathrm { H } ) } \end{array}
$$

Apart from its use of approximations to $f _ { k } ^ { \prime }$ rather than exact values, this algorithm is due to Kravanja and Van Barel in collaboration with Sakurai [54], based on earlier work by Delves and Lyness [18].

Although we have presented $[ \mathsf { C z 1 } ]$ as a generalization of [McCune] to multiple roots, in fact it is different in the case $K = 1$ , and more accurate. This is because its generalized eigenvalue problem gives it the “second kind” nature of a quotient of two trapezoidal approximations, as in (C.23), rather than a single trapezoidal approximant, as in (C.8). For $K = 1$ , the estimate of $w$ delivered by [Cz1] is equal to the estimate delivered by [McCune] divided by a constant close to 1, namely, the trapezoidal approximation to $s _ { 0 } = 1$ , the number of zeros inside the unit disk.

As we shall see in the numerical experiments of Section C.4.2, the assumption of distinct zeros used in deriving [Cz1] is an essential one. As explained in [56], nearly equal zeros cause instability for this algorithm, and additional formulas must be used to treat cases with confluent zeros.

# C.3.2 Cauchy integrals involving $1 / f$ instead of $f ^ { \prime } / f$

In the Cauchy integral method just described, values of the derivative $f ^ { \prime }$ were in principle required and approximated in practice by polynomial interpolation. Other contour integrals can be used for zerofinding, however, that do not involve $f ^ { \prime }$ . For the case where $f$ has just one zero in $D$ , an integral formulation analogous to (C.25) is

$$
w = \int _ { S } \frac { \zeta } { f ( \zeta ) } d \zeta \int _ { S } \frac { 1 } { f ( \zeta ) } d \zeta ,
$$

proposed by Luck and Stevens [61]. The trapezoidal discretization takes this form:

[LuckStevens]

$$
\ l _ { \sf U } = \ m e { \bf a } \ n \left( { \bf z } { \bf k . \hat { \mu } } \hat { \bf \phi } ^ { - } 2 . / { \bf f } { \bf k } \right) / \ m { \bf e } { \bf a } \mathrm { n } \left( { \bf z } { \bf k . \ / } \hat { \bf f } { \bf k } \right) .
$$

Note that unlike [McCune], [LuckStevens] contains a denominator sum, giving it the flavor of a “second kind” discretization. As a consequence, the generalization to the case of $K$ zeros will reduce exactly to [LuckStevens] in the case $K = 1$ .

That generalization is surprisingly easy: we just delete the $f ^ { \prime }$ terms from the algorithm of Section C.3.1! Following [56, Section 1.6], let us redefine the numbers $s _ { m }$ by replacing the integral (C.27) by

$$
s _ { m } : = \frac { 1 } { 2 \pi i } \int _ { S } \frac { \zeta ^ { m } } { f ( \zeta ) } d \zeta = \sum _ { j = 1 } ^ { K } \frac { w _ { j } ^ { m } } { f ^ { \prime } ( w _ { j } ) } ,
$$

assuming the roots are simple. From here the developments proceed as before. Again the zeros of $f$ are the eigenvalues of the generalized eigenvalue problem (C.29); the derivation is the same as before, except with the $j$ th column of $V$ divided by $( f ^ { \prime } ( w _ { j } ) ) ^ { 1 / 2 }$ . (Any choice of square roots will do. There is a much more general structure to these problems; see [7] and [56].) The trapezoidal rule in roots of unity gives accurate approximations and can be realized as follows in MATLAB:

[Cz2]

$$
\begin{array} { r l } & { \textbf { s } = \mathrm { ~ i f f t } ( 1 . / \mathrm { f k } ) } \\ & { \mathrm { ~ H ~ } = \mathrm { ~ h a n k e l } ( \mathbf { s } ( 2 : \mathrm { K } { + } 1 ) , \ \mathbf { s } ( \mathrm { K } { + } 1 : 2 { * } \mathrm { K } ) ) } \\ & { \mathrm { ~ H } 2 \ = \ \mathrm { h a n k e l } ( \mathbf { s } ( 3 : \mathrm { K } { + } 2 ) , \ \mathbf { s } ( \mathrm { K } { + } 2 : 2 { * } \mathrm { K } { + } 1 ) ) } \\ & { \mathbf { w } \ = \ \mathbf { e i g } ( \mathrm { H } 2 , \mathrm { H } ) } \end{array}
$$

Unlike [Cz1], algorithm [Cz2] is able to calculate nearly equal or multiple zeros, as we shall see in the numerical experiments of Section C.4.2. Both algorithms involve Hankel matrices that may be ill-conditioned, however, so they are not stable in all cases.

# C.4 Polefinding in the unit disk

To find zeros of an analytic function $f$ , algorithms [Cz1] and [Cz2] applied Cauchy integrals to the functions $f ^ { \prime } / f$ and $1 / f$ , respectively. However, one might say that at bottom, any algorithm utilizing Cauchy integrals is really a “polefinding” algorithm. Following this line of thinking, suppose we are given a function $g$ that is meromorphic in $D _ { R }$ for some $R > 1$ , having exactly $K$ poles there, which we assume are all in $D$ . We could then consider the problem of calculating these $K$ poles from samples of $g$ at roots of unity. Note that this problem is not quite equivalent to the problem of the last section with $g = 1 / f$ , since $g$ may have both poles and zeros, whereas $f$ was assumed to have no poles.

# C.4.1 Two algorithms for polefinding

Again we shall distinguish two approaches: interpolation and Cauchy integrals. The new feature that appears is that for polefinding, it is necessary to interpolate by rational functions rather than polynomials.

Algorithm $\mathrm { R } ^ { P }$ . Linearized rational interpolation. Assuming $_ { g }$ has $K$ poles in $D _ { R }$ , approximate it by $r ( z ) = p ( z ) / q ( z )$ , where $p \in { \cal P } _ { n - 1 - K }$ , $q \in P _ { K }$ is monic, and the equation $g ( z _ { k } ) q ( z _ { k } ) = p ( z _ { k } )$ holds at each of the nth roots of unity; then compute the zeros of $q$ in $D$ .

Generically, the linearized rational interpolant is a true rational interpolant, but interpolation may fail in cases where $q ( z _ { k } ) = 0$ . Algorithms for computing $r$ and a corresponding MATLAB code ratdisk are given in [33], based on a singular value decomposition (SVD) of a $K \times ( K { + } 1 )$ rectangular Toeplitz matrix of discrete Fourier coefficients of $g$ ; we shall say more in Section C.6. Using these tools, polefinding by linearized rational interpolation reduces to a single call to ratdisk:

$$
[ \bf { r } , \bf { a } , \bf { b } , \mathrm { m u } , \mathrm { n u } , \bf { w } ] ^ { \mathrm { ~ ~ } } = \ c a t d i s k ( \mathrm { g } { \bf } { \bf } { \bf } { \bf } , \ n - 1 - \mathrm { K } , \ \mathrm { K } )
$$

(The same effect is also available via ratinterp(gk,n-1-K,K,[],'unitroots') in Chebfun.) Here gk represents a column vector of samples of $g$ at the roots of unity. If our aim is to find zeros of an analytic function $f$ , we precede [ratdisk_K] by $\mathrm { g } \mathrm { k } \ = \ 1 . / \mathrm { f } \mathrm { k }$ .

Alternatively, we can compute poles by Cauchy integrals. The natural approach here is to use algorithm $[ \mathsf { C } z 2 ]$ with $1 / f$ relabeled as $g$ . For completeness we give this formulation of the algorithm the new name $[ \mathsf { C p } ]$ :

[Cp]

$$
\begin{array} { r l } & { \mathrm { { \bf ~ s } ~ = ~ \mathrm { i f f t } ( \mathrm { { \bf ~ g } k } ) } } \\ & { \mathrm { { \bf ~ H } ~ = ~ \mathrm { h a n k e l } ( \mathrm { { \bf ~ s } } ( 2 : \mathrm { K } { + } 1 ) , ~ \mathrm { { \bf ~ s } } ( \mathrm { { \bf ~ K } } { + } 1 : 2 * \mathrm { K } ) ) } } \\ & { \mathrm { { \bf ~ H } 2 ~ = ~ \mathrm { h a n k e l } ( \mathrm { { \bf ~ s } } ( 3 : \mathrm { K } { + } 2 ) , ~ \mathrm { { \bf ~ s } } ( \mathrm { { \bf ~ K } } { + } 2 : 2 * \mathrm { K } { + } 1 ) ) } } \\ & { \mathrm { { \bf ~ w } ~ = ~ \mathrm { e i g } ( \mathrm { { \bf ~ H } } 2 , \mathrm { { \bf { H } } } ) } } \end{array}
$$

# C.4.2 Numerical illustration of five algorithms for zerofinding

We have presented five algorithms that can be used for zerofinding, with MATLAB names $[ \mathsf { P } z ]$ and [Pz\*] (these two are equivalent), [Cz1], [Cz2] (or [Cp]), and [ratdisk_K]. To illustrate the behavior of these algorithms, we apply them with $n = 5 0$ to the function $f ( z ) = \sin ( z - 0 . 3 ) \log ( 1 . 2 - z )$ , which has two nearby zeros in $D$ at 0.2 and 0.3. The first four algorithms find zeros of $f$ directly, and [ratdisk_K] finds poles of $g = 1 / f$ . Here are the results:

Arrowhead matrix, Algorithm [Pz]: 0.20002100, 0.29997794   
Companion matrix, Algorithm [Pz\*]: 0.20002100, 0.29997794   
Cauchy integrals in f'/f, Algorithm [Cz1]: 0.20468368, 0.30432215   
Cauchy integrals in 1/f, Algorithm [Cz2]: 0.20000116, 0.29999865   
Rational interp. of 1/f, Algorithm [ratdisk_K]: 0.20000116, 0.29999865

These numbers reveal several interesting properties. First, [Pz] and $[ \mathsf { P } z * ]$ give the same results, since they are mathematically equivalent. Second, [Cz1] gives far worse results. This is a consequence of the nearly equal zeros; this algorithm must be modified in such cases, as explained in [56]. Third, [Cz2] and [ratdisk_K] also give the same results. This is a new observation (although it can be found between the lines in Section 2.3 of [56]), which we explain in the next subsection.

Fourth, this last pair of algorithms do not suffer from the nearly equal zeros, and indeed their results are slightly more accurate than those of $[ \mathsf { P z } ] / \left[ \mathsf { P z } \ast \right]$ . As a rule, we believe that linearized rational interpolation is quite a good method for approximating zeros of analytic functions; we shall say more in Section C.6.

# C.4.3 Equivalence of linearized rational interpolation and a discretized contour integral algorithm

The two polefinding algorithms we have described, [ratdisk_K] and [Cz2] (or [Cp]), are mathematically equivalent. We now outline this connection.

let $n \geq 1$ $K < n$ , let  poly $g$ be a funomial in on defined, and let $_ { n }$ f unity,be the $\textstyle q ( z ) = \sum _ { k = 0 } ^ { K } b _ { k } z ^ { k }$ $P _ { K }$ $\textstyle p ( z ) = \sum _ { k = 0 } ^ { n - 1 } a _ { k } z ^ { k }$ polynomial in $P _ { n - 1 }$ that interpolates $g ( z ) q ( z )$ at the roots of unity. We know that $p / q$ corresponds to a linearized rational interpolant to $g$ if $p$ belongs to $P _ { n - 1 - K }$ .

Since $p \in P _ { n - 1 }$ , its coefficients $a _ { 0 } , \ldots , a _ { n - 1 }$ can be calculated by interpolation in the roots of unity: a discrete Fourier transform of the data $g ( z _ { k } ) q ( z _ { k } )$ . The condition for $p / q$ to be a linearized rational interpolant to $g$ is $\scriptstyle a _ { n - K } = a _ { n - K + 1 } =$ $\dots = a _ { n - 1 } = 0$ , that is, $K$ equations in the $K + 1$ unknowns $b _ { 0 } , \dots , b _ { K }$ . This rectangular linear system of equations always has a nontrivial solution, and ratdisk finds such a solution by computing an SVD.

Algorithm [Cp] is based on an alternative interpretation of the same conditions $a _ { n - K } = a _ { n - K + 1 } = \cdot \cdot \cdot = a _ { n - 1 } = 0$ . If $p$ has degree $< n - 1$ , its discrete contour integral in the $n$ th roots of unity must be zero:

$$
\sum _ { k = 0 } ^ { n - 1 } z _ { k } p ( z _ { k } ) = \sum _ { k = 0 } ^ { n - 1 } z _ { k } g ( z _ { k } ) q ( z _ { k } ) = 0 .
$$

But for any $j < K$ , $z ^ { j } p ( z )$ still has degree $< n - 1$ , so we actually have

$$
\sum _ { k = 0 } ^ { n - 1 } z _ { k } ^ { j + 1 } g ( z _ { k } ) q ( z _ { k } ) = 0 , \quad 0 \leq j \leq K - 1 .
$$

That is, $q$ is orthogonal to $1 , z , \dots , z ^ { K - 1 }$ , with respect to a discrete symmetric bilinear form supported at the roots of unity (not quite an inner product, since it lacks positive-definiteness and conjugate-symmetry). We say that $q$ is the degree $K$ discrete formal orthogonal polynomial defined by the weights $z _ { k } g ( z _ { k } )$ at the $n$ th roots of unity. From here, standard manipulations bring us to a generalized eigenvalue problem involving Hankel matrices of discrete moments, as described in (C.28)–(C.31) above, with the eigenvalues being the roots of $q$ .

In a word, [ratdisk_K] determines $q$ by its coefficients and [Cp] by its zeros.

# C.5 Computing the eigenvalues of a matrix in the unit disk

Let $A$ be a square matrix of dimension $N$ . How can we find its eigenvalues in the unit disk? This question is a natural extension of the topics addressed up to now in this paper, and it points toward major challenges of computational science, where $A$ will typically be an approximation with $N \gg 1$ to a partial differential or other linear operator. For simplicity we speak of the standard eigenvalue problem $A x = \lambda x$ , though most of the ideas carry over to the generalized eigenvalue problem $A x = \lambda B x$ .

One idea with a zerofinding flavor would be to compute zeros of the determinant, i.e., zeros of the function

$$
f ( z ) = \operatorname* { d e t } ( z I - A ) .
$$

To do this, we could evaluate $f ( z )$ at the $n$ th roots of unity and then apply any of the algorithms of Section C.3 or Section C.4 (with $g = 1 / f$ ). In MATLAB, one could write

[det]

$$
\mathbf { f o r } \ \mathrm {  ~ k ~ } = \ 1 : \mathrm { n } , \mathbf { f k } \left( \mathrm { k } \right) \ = \ \mathbf { d e t } \left( { z \mathrm { k } \left( \mathrm { k } \right) } * \mathrm { I } - \mathrm { A } \right) , \ \mathrm { e n d }
$$

followed by, say, $[ \mathsf { P } z ]$ . (The operation count could be improved from $O ( n N ^ { 3 } )$ to $O ( N ^ { 3 } + n N ^ { 2 } )$ by a preliminary factorization.) To illustrate, consider the $4 \times 4$ matrix

$$
A = \left( \begin{array} { r r r r } { { 3 . 2 } } & { { 1 . 5 } } & { { 0 . 5 } } & { { - 0 . 5 } } \\ { { - 1 . 6 } } & { { 0 . 0 } } & { { - 0 . 4 } } & { { 0 . 6 } } \\ { { - 2 . 1 } } & { { - 2 . 2 } } & { { 0 . 2 } } & { { - 0 . 1 } } \\ { { 2 0 . 7 } } & { { 9 . 3 } } & { { 3 . 9 } } & { { - 3 . 4 } } \end{array} \right)
$$

with eigenvalues $0 . 2 , 0 . 3 , 1 . 5 , - 1 . 9$ ; thus the eigenvalues in $D$ are 0.2 and 0.3. Here are the computed eigenvalue estimates with $n = 3 0$ :

Polynomial interpolation, Algorithm [Pz]/[Pz\*]: 0.20000000, 0.30000000   
Cauchy integrals in f'/f, Algorithm [Cz1]: 0.19901287, 0.29895203   
Cauchy integrals in 1/f, Alg. [Cz2]/[ratdisk_K]: 0.19994887, 0.30005345

In this case polynomial interpolation gives the exact result, since the determinant is a polynomial of degree $N \leq n$ . For dimensions $N \gg 1$ , of course, one would not be prepared to compute enough determinants for this property to hold. The other two algorithms give geometrically accurate results, with linearized rational interpolation performing particularly well.

Although this small-scale experiment was successful, we are not sure whether finding zeros of the determinant is likely to be an attractive option in many largescale computations. An algorithm of this nature has been proposed in [50].

The other approach for computing eigenvalues we will now consider is certainly an important one: computing poles of the resolvent. Strengthening the foundations of algorithms of this kind was a significant motivation for us to write this paper.

The eigenvalues of $A$ are the poles of the resolvent function, $( z I - A ) ^ { - 1 }$ . This function is matrix-valued, but suppose $u$ and $\boldsymbol { v }$ are fixed $N$ -vectors. Then the rational function

$$
g ( z ) = u ^ { * } ( z I - A ) ^ { - 1 } v
$$

is scalar-valued. If $u$ and $v$ are random vectors, then with probability $1$ , $g$ will have poles at all the eigenvalues of $A$ (though some of the residues may be very small). The same applies in the special case where $u$ and $v$ are taken to be equal.

This immediately gives us a first idea for approximating eigenvalues by polefinding: evaluate the scalarized resolvent function $g$ at roots of unity, then use [Cp] or

equivalently [ratdisk_K] to estimate its poles. Each point evaluation of $g$ requires the solution of a linear system of equations involving a shift of $A$ , which may be carried out in parallel:

[res]

$$
\mathrm { f o r ~ \ k ~ = ~ 1 : n , ~ \ g k ( k ) ~ \ b ~ = ~ u ^ { \prime } * ( \tau ( z k ( k ) * I - A ) \setminus \ v u ) , ~ \ e n d }
$$

As an example, consider the same $4 \times 4$ matrix as before. Here are the computed eigenvalue estimates with $n = 3 0$ and $u = v = ( 1 , 1 , 1 , 1 ) ^ { T }$ :

Rational interpolation, Alg. [Cz2]/[ratdisk_K]: 0.20021799, 0.29990926

In the past decade, algorithms of this kind have begun to be widely used. There are two main schools of research in this area: Sakurai and his collaborators in Japan [5, 42, 43, 74, 75], and Polizzi and his collaborators [30, 53, 57, 58, 71, 81], who have given their software package the name FEAST. The Sakurai school began with a trapezoidal discretization of Cauchy integrals, effectively [Cp] applied to the scalarized resolvent function $g$ [74]. Polizzi chose instead a Gauss quadrature discretization over semicircles. Both groups have applied their algorithms to largescale problems in physics, particularly the calculation of electronic structure, where earlier related algorithms were presented by Goedecker [32].

For these eigenvalue computations to be fully effective, one must move beyond scalar functions $g ( z )$ . To explain this we note that although algorithm [ratdisk_K] will find multiple poles, not every multiple eigenvalue of a matrix $A$ produces a multiple pole of the function $g$ ; this will happen only if the eigenvalues correspond to just a single Jordan block (i.e., the algebraic multiplicity is >1 but the geometric multiplicity is 1). The Hermitian matrices that often arise in physics are very far from this situation. To get around this problem, rather than using a single pair of vectors $u$ and $v$ , one can use a set of such vectors, so that $g$ effectively becomes a matrix function of dimension greater than 1 but much less than $N$ . Polizzi utilized this device from the start [71], and Sakurai (the “block Sakurai–Sugiura method”) from 2010 [42, 43]. A further important practical modification is that the sampling at roots of unity may be embedded in an outer loop, so that in the language of our introduction, the unit disk filter function is applied not just once but several times to improve the projection onto the unit disk, damping eigenvector components outside the disk relative to those inside. Many other practical variations have been considered, including use of regions other than a disk, and this is a rapidly moving area of research. Generalizations to nonlinear eigenvalue problems have been published by Asakura et al. [5] and Beyn [10].

# C.6 Rational approximations

Up to now, rational approximations have featured in this paper in two ways. First, there were rational approximations constructed implicitly by discretization of contour integrals, with poles fixed at the roots of unity. Second, there were rational interpolants with $K$ free poles, of type $( n - 1 - K , K )$ , constructed in Sections C.4 and C.5 for the purpose of locating $K$ poles in the unit disk. A rational function is of type $( J , K )$ if it can be written as a quotient $p ( z ) / q ( z )$ for some polynomials $p$ and $q$ of degrees no greater than $J$ and $K$ , respectively.

Here, we want to highlight the power of rational approximations with more free poles, for example, of type $( n - 1 - K , K )$ with $K \approx n / 2$ . (We are grateful to an anonymous referee for urging us to include these comments.) For another publication that showcases the power of rational approximations as compared with polynomials, see [20].

Suppose that samples $f _ { k } = f ( x _ { k } )$ of a function $f$ are available at the $_ { n }$ th roots of unity and we wish to construct a rational approximation $r$ to $f$ of type $( J , K )$ for some prescribed $J$ and $K$ . The most basic method for constructing such approximants is linearized interpolation, as utilized in the last two sections. Here we fix $K \leq n - 1$ and $J = n - 1 - K$ . The linearized equations $f ( z _ { k } ) q ( z _ { k } ) = p ( z _ { k } )$ , $0 \leq k \leq n - 1$ , can always be satisfied, and generically, such solutions will correspond to solutions of the nonlinear equations $f ( z _ { k } ) = p ( z _ { k } ) / q ( z _ { k } )$ too, so long as $q ( z _ { k } ) \neq 0$ . We use the ratdisk algorithm and code of [33] to compute these interpolants, and we shall say more about the significance of this choice in a moment.

Let us look again at some examples already considered in this paper, but now addressing them by linearized rational interpolation with $K = n / 2$ . First, following section C.2.4, suppose $f ( z ) = \log ( 1 . 2 - z ) / \log ( 1 . 2 - 0 . 8 )$ and we wish to evaluate $f ( 0 . 8 )$ based on samples at $n = 3 2$ roots of unity; the exact value is 1. Here are the results for polynomial interpolation as in Section C.2.2, discretized Cauchy integrals also as in Section C.2.2, and linearized rational interpolation with $K = n / 2$ :

[P] or [P\*] 1.00028 [C] 1.0011 [ratdisk] 1.000000000030

We see a dramatic improvement from 3 or 4 correct digits for the earlier methods to 10 correct digits for rational interpolation with $K = n / 2$ . Figure C.5 further reinforces this remarkable result, repeating the images of Figures C.3 and C.4 but now for the new rational approximation $r$ . We see immediately that this is strikingly more accurate than the previous approximations and not confined in the same way to the unit disk.

These happy results are not as straightforward as they may seem. If rational interpolants are computed by the obvious methods of numerical linear algebra, then unless $K$ is sufficiently small, there is a tendency for spurious pole-zero pairs to arise, known as Froissart doublets, in which a pole and a zero are present that are separated by only the order of machine epsilon. Equivalently, these are spurious poles with residues of order machine epsilon. Such difficulties have an august history in the field of rational approximation, both theoretical and numerical, and if the example just displayed is run as suggested with $n = 3 2$ , one such Froissart doublet appears. However, regularization based on an SVD of a Hankel matrix of Laurent coefficients can be used to largely eliminate such effects. Such a regularization algorithm is presented in [33], and the code ratdisk includes this procedure in its default mode of operation. In practice, we believe that this regularization is crucial for the reliability of numerical methods based on rational approximation. For more discussion, see the final chapters of [84].

For the next example, following Section C.4.2, suppose $f ( z ) ~ = ~ \sin ( z ~ -$ $0 . 3 ) \log ( 1 . 2 - z )$ and we seek the zeros of $f$ in the unit disk based on samples at $n = 5 0$ roots of unity; the exact zeros are 0.2 and 0.3. Here are the results for polynomial zerofinding as in Section C.3.1, a discretized contour integral as in

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0005_pages_0281-0350/auto/images/fcb6e1601a5e82a537f210ac7270cafcd5c90f6424ce9be7454def0b18c0f5ca.jpg)  
Figure C.5: Repetition of Figures $C . 3$ and $C . 4$ but for the type $( J , K )$ linearized rational interpolant $r$ with $K = n / 2$ as computed robustly with ratdisk. The approximation is now far more accurate. In fact, it remains more accurate even if $N$ is reduced from 32 to 10.

Section C.3.2 (which is the same as ratdisk with $K = 2$ as in Section C.4.1), and ratdisk with $K = n / 2$ . In the last case we simply interpolate the data by rational function, then compute the zeros of this interpolant.

[Pz] or [Pz\*] 0.200021 0.299978 [Cz2] or [ratdisk_K] 0.2000012 0.2999986 [ratdisk] 0.200000000000061 0.299999999999884

The accuracy has improved from 4 or 5 digits to 13. (Without regularization, this example would have five Froissart doublets and hence five spurious zeros.)

Now, consider the $4 \times 4$ matrix eigenvalue example of Section C.5, with eigenvalues 0.2 and 0.3 and $n = 3 0$ roots of unity. We obtain the following results:

[Cp] or [ratdisk_K] 0.20022 0.299909 [ratdisk] 0.200000000000032, 0.299999999999986

Once more there is a great increase in accuracy. (And once more, without regularization, there would be five Froissart doublets—spurious eigenvalues.)

These examples illustrate that over a range of problems, rational approximations with a significant number of free poles have the potential to achieve high accuracy. The results are not always as good as those shown, especially for functions $f$ with complicated behavior outside the unit disk, and they are more fragile than with purely polynomial methods. But it is safe to say that rational approximations are worthy of serious attention in many applications. In the business of FEAST-related algorithms for computing eigenvalues, such approximations are well-established, though not ordinarily presented in these terms. Sakurai and Polizzi speak of choosing larger than necessary parameters to enlarge the search subspace to accelerate convergence. In our language, this amounts to increasing the denominator degree $K$ in a rational approximation.

What we have called linearized rational interpolation is actually, in cases where Froissart doublets are removed, linearized rational least-squares fitting, in which the

sum of squares

$$
\sum _ { k = 0 } ^ { n - 1 } \left| f ( z _ { k } ) q ( z _ { k } ) - p ( z _ { k } ) \right| ^ { 2 }
$$

is minimized. The reason is that ratdisk reduces the denominator degree from $K$ to $K ^ { \prime }$ when certain singular values fall below a tolerance set by default to $1 0 ^ { - 1 4 }$ , so that now there are more constraints than free parameters. For details, see [33] and [84, Chapter 26].

Beyond linearized least-squares, another rational approximation idea is true nonlinear least-squares approximation, where one minimizes

$$
\sum _ { k = 0 } ^ { n - 1 } \left| f ( z _ { k } ) - { \frac { p ( z _ { k } ) } { q ( z _ { k } ) } } \right| ^ { 2 } .
$$

Here, best approximations need not even be unique, but in practice there may be advantages. A paper of Meier and Luenberger shows that a necessary condition for $r$ to be a rational least-squares approximation to an analytic function $f$ on the unit disk is that $r$ interpolates $f$ and also $r ^ { \prime }$ interpolates $f ^ { \prime }$ at the points in the disk that are the symmetric images with respect to the unit circle of the poles of $r$ [67]. This observation has been used as the basis of iterative algorithms in model reduction on the unit circle (“MIRIAm”) [13] and the imaginary axis (“IRKA”) [34]. When the unit circle is discretized by roots of unity, one can formulate an analogous necessary condition involving a polynomial interpolant of $f$ , as we shall report elsewhere.

Beyond these ideas, there are some powerful further methods for constructing rational approximations based on singular value analysis of Hankel matrices. These techniques stem from work of Adamjan, Arov, and Krein around 1970 [1], and different variants go by the names of Hankel norm approximation and CF approximation [4, 31, 83]. In many cases such methods provide approximations that are extremely close to optimal in the $L ^ { \infty }$ norm (where, as with the $L ^ { 2 }$ norm, optima need not always be unique), and an additional feature is that they may satisfy specified stability constraints on the number of poles within the unit disk. An article drawing these threads together, whether in the continuous setting or in the context of discrete data at the roots of unity, remains to be written.

# C.7 Further notes on the literature

In 2008, the third author started to write a book called Neoclassical Numerics, which was to begin with a chapter on the unit disk. Later he decided that the work should concentrate instead on $[ - 1 , 1 ]$ , and it evolved into Approximation Theory and Approximation Practice $/ A T A P$ ) [84]. The present paper now returns to that project of 2008, informed by the subsequent years’ experience with $A T A P$ and also the Chebfun software project: one may think of this paper as a kind of “ $A T A P$ for the unit disk,” or as the mathematical basis for a “Diskfun” project (not planned). There are close links between monomials, roots of unity, and the disk $D _ { R }$ as considered here and Chebyshev polynomials, Chebyshev points, and Bernstein ellipses as discussed in [84].

A feature of both that project and this one is that the mathematics involved is in good part classical, depending on results well distributed across the past century.

In particular, when it comes to approximation of functions in roots of unity, a great expert was Joseph Walsh (1895–1973), who served on the mathematics faculty at Harvard from 1921 to 1966. Walsh had little interest in numerical algorithms, but much of what we have done here would be familiar to him, and we wish he were here to comment on every line of this paper. His book [87] is an important resource, though difficult to read.

In the following we record some notes on individual sections and subsections.

Section C.2.1. Two algorithms for evaluating a function. Algorithm P is not discussed much in the numerical analysis literature, except in [12], but Algorithm C has received plenty of attention, beginning with the work of Lyness and his coauthors in the 1960s [18], [62, 63, 64, 65]. We do not know how often it has been noticed that Algorithms P and C are related by (C.4); this observation appears as equation (5.12) of [35].

Section C.2.2. Barycentric formulas for the two algorithms. For general point sets $\left\{ { z } _ { k } \right\}$ , the first barycentric formula (C.8) is due to Jacobi in 1825 [47] and the second to Dupuy in 1948 [21]. For the particular case of roots of unity, formula (P) was perhaps first written down by Henrici and can be found in print in [9, 35].

Section C.2.3. Taylor projections and polynomial interpolants. A parallel treatment of Chebyshev projections and interpolants can be found in Chapter 4 of [84].

Section C.2.4. Accuracy of the two algorithms. It was Runge in 1904 who first showed convergence in $D$ of polynomial interpolants in roots of unity [72, Section II.15, pp. 136–137], though M´eray had the necessary tools in hand two decades earlier [68]. Geometric convergence in the context of the trapezoidal rule for quadrature was analyzed by Davis in 1959 [17]. The better accuracy of polynomial interpolation as compared with discretized contour integrals for points near the boundary is emphasized in [12, Chapter 5].

Section C.2.5. Zeros, poles, and the Jentzsch and Walsh theorems. Beautiful phase portraits illustrating Jentzsch’s theorem and discretized contour integrals can be found in Figures 3.9–3.14 and 4.18 of [88].

Section C.2.6. Cauchy integrals of the second kind. In the integral equations literature, series-related reformulations of the standard Nystr¨om-type algorithms to achieve better accuracy near contours have been developed lately. An example in the context of the fast multipole method is the QBX method of Kl¨ockner et al. [52].

Section C.2.7. Derivatives of $f$ or Taylor series. The first proposal of numerical calculation of derivatives via the trapezoidal rule applied to Cauchy integrals may have been in [62, 63]. The FFT was introduced into the algorithm in [65], and barycentric formulas for derivatives were introduced in [77].

Section C.2.8. Scaling of the radius. The question of adjusting the radius $\tau$ goes back to [62], where the problem of numerical instability for small $\tau$ was noted.

Section C.2.9. The method of fundamental solutions. The trade-off between accuracy and conditioning in the smooth, high-accuracy regime is a central issue in the field of RBFs [23, 28].

Section C.3.1. Two algorithms for zerofinding. Equation (C.27) goes back to [46]. The classic paper on numerical zerofinding algorithms based on trapezoidal discretization of Cauchy integrals is [18], whose Section 6 proposes the use of the polynomial interpolant to approximate $\left\{ f _ { k } ^ { \prime } \right\}$ as in [Cz1] (i.e., Taylor polynomials with coefficients calculated by the trapezoidal rule). Delves and Lyness use Newton identities to find the roots; Kravanja, Sakurai, and Van Barel [54] use a generalized eigenvalue problem based on modified moments. The “discrete Cauchy integral of the second kind” idea is applied to zerofinding in [44]. The special case of (C.27) with $m = 0$ is the subject of [79].

Section C.4.1. Two algorithms for polefinding. There does not appear to be much literature explicitly on polefinding based on data at roots of unity, though such problems get some attention in [56, Chapter 3] and [33]. Perhaps the most interesting work we know in this connection is [28], where rational interpolants in roots of unity are utilized to evaluate a meromorphic function accurately in the unit disk despite the presence of poles there.

Section C.5. Computing the eigenvalues of a matrix in the unit disk. For more on the interplay of contour integrals, spectral projectors, and electronic structure, see [8, 60].

Section C.6. Rational approximations. A general discussion of the comparative features of rational and polynomial approximation can be found in [84, Chapters 23–28].

# C.8 Conclusions

The central theme of this article is that there are two kinds of algorithms for the problems at hand: those based on function approximations (polynomial or rational) and those based on discretized Cauchy integrals (which implicitly also construct rational approximations). The former have the advantage that they introduce no singularities on the boundary contour and may therefore be more accurate, while the latter have the advantage that they restrict the problem to the interior region and may therefore be faster. Sometimes the two concepts lead to the same result, as in [P] and (C.23), which are identical, or [Cp] and [ratdisk], which are mathematically equivalent but have different stability properties. It is rare in the literature for the two types of algorithms to be distinguished or compared. We believe such comparisons may reveal new computational possibilities, not just for analytic functions on the unit disk but in many other areas that may be regarded as variations on this theme. A list of such variations with references was given in the introduction.

The main algorithms we have discussed can be summarized as follows, listed with the names of their MATLAB realizations:

<table><tr><td>[P]</td><td>Evaluation of f(z） by polynomial interpolation (p. 301)</td></tr><tr><td>[P*]</td><td>Same,coefficient-based algorithm (p. 301)</td></tr><tr><td>[C]</td><td>Evaluation of f(z) by discretized Cauchy integral (p. 301)</td></tr><tr><td>[P&#x27;]</td><td>Evaluation of f&#x27;(z） by polynomial interpolation (p. 306)</td></tr><tr><td>[P&#x27;*]</td><td>Same,coefficient-based algorithm (p. 306)</td></tr><tr><td>[C&#x27;]</td><td>Evaluation of f&#x27;(z) by discretized Cauchy integral (p. 306)</td></tr><tr><td>[Pz]</td><td>Zerofinding for f via polynomial interpolation (p. 308)</td></tr></table>

<table><tr><td>[Pz*] Same,coefficient-based algorithm (p. 308)</td></tr><tr><td>[Cz1] Zerofinding for f via discretized Cauchy integral for f&#x27;/f (p. 310)</td></tr><tr><td>[Cz2] Zerofinding for f via discretized Cauchy integral for 1/f (p. 311)</td></tr><tr><td>[ratdisk_K] Polefinding for g via rational interpolation with K poles (p. 312)</td></tr><tr><td>[Cp] Polefinding for g via discretized Cauchy integral (p. 312)</td></tr><tr><td>[ratdisk] Evaluation/zerofinding/polefinding via rational interpolation</td></tr><tr><td>(p. 315)</td></tr></table>

We close by summarizing some of the main points of this paper:

• For evaluating $f ( z )$ , polynomial interpolants and discretized Cauchy integrals are equivalent for $z = 0$ and otherwise are distinct. The latter method approximates $f$ by a rational function equal to the polynomial interpolant divided by $1 - z ^ { n }$ , making it less accurate for $| z | \approx 1$ .   
• On the other hand, the barycentric formula for polynomial interpolation is identical to a “discretized Cauchy integral of the second kind,” or as Ioakimidis puts it [44, 45], a discretization of “the Cauchy theorem instead of the Cauchy formula.”   
• For zerofinding, the Cauchy integral approach has an $O ( n \log n )$ versus $O ( n ^ { 3 } )$ complexity advantage over polynomial interpolation, because the integral serves to project the problem onto the unit disk. It is not clear that zerofinding via polynomial interpolation has ever been proposed in the literature.   
• The polefinding method we have called [Cp], based on discretized Cauchy integrals, is mathematically equivalent to computing the poles of a linearized rational interpolant, the algorithm we have called [ratdisk_K]. However, the latter is numerically more stable.   
• The originators of algorithm [Cp], Kravanja and Van Barel, recognized its instability and proposed a more stable algorithm based on modified moments and formal orthogonal polynomials [55, 56]. A challenge for future research is to compare the stability of that algorithm and [ratdisk_K].   
• FEAST and related algorithms for finding eigenvalues of a matrix in a disk are derived from the idea of polefinding for the resolvent function. In the simplest case the resolvent is reduced to a scalar; more robust block algorithms reduce it to an intermediate dimension. In addition, an outer iteration may be applied to improve the projection onto the unit disk.   
• All the algorithms mentioned above are outperformed for some problems by rational approximations with more free poles, for example, rational interpolants of type approximately $( n / 2 , n / 2 )$ . Use of the SVD-regularized algorithm and code known as ratdisk from [33] for such calculations (or

equivalently the Chebfun code ratinterp with the 'unitroots' flag) prevents the appearance of spurious pole-zero Froissart doublets.

# Acknowledgments

We are grateful for corrections and suggestions from Alex Barnett, Jean-Paul Berrut, John Boyd, Bengt Fornberg, Martin Gutknecht, Georges Klein, Edward Saff, Alex Townsend, Elias Wegert, and Andr´e Weideman.

# Bibliography

[1] V. Adamjan, D. Arov, and M. Krein, Analytic properties of Schmidt pairs for a Hankel operator and the generalized Schur–Takagi problem, Math. USSR Sb., 15 (1971), pp. 31–73.

[2] A. Amiraslani, New Algorithms for Matrices, Polynomials, and Matrix Polynomials, Ph.D. dissertation, University of Western Ontario, 2006.

[3] E. G. Anastasselou, A formal comparison of the Delves–Lyness and Burniston–Siewert methods for locating the zeros of analytic functions, IMA J. Numer. Anal., 6 (1986), pp. 337–341.

[4] A. C. Antoulas, Approximation of Large-Scale Dynamical Systems, SIAM, Philadelphia, 2005.

[5] J. Asakura, T. Sakurai, H. Tadano, T. Ikegami, and K. Kimura, A numerical method for nonlinear eigenvalue problems using contour integrals, JSIAM Lett., 1 (2009), pp. 52–55.

[6] A. H. Barnett and T. Betcke, Stability and convergence of the method of fundamental solutions for Helmholtz problems on analytic domains, J. Comput. Phys., 227 (2008), pp. 7003–7026.

[7] B. Beckermann, G. H. Golub, and G. Labahn, On the numerical condition of a generalized Hankel eigenvalue problem, Numer. Math., 106 (2007), pp. 41–68.

[8] M. Benzi, P. Boito, and N. Razouk, Decay properties of spectral projectors with applications to electronic structure, SIAM Rev., 55 (2013), pp. 3–64.

[9] J.-P. Berrut and L. N. Trefethen, Barycentric Lagrange interpolation, SIAM Rev., 46 (2004), pp. 501–517.

[10] W.-J. Beyn, An integral method for solving nonlinear eigenvalue problems, Linear Algebra Appl., 436 (2012), 3839–3863.

[11] F. Bornemann, Accuracy and stability of computing high-order derivatives of analytic functions by Cauchy integrals, Found. Comput. Math., 11 (2011), pp. 1–63.

[12] J. P. Boyd, Solving Transcendental Equations: The Chebyshev Polynomial Proxy and Other Numerical Rootfinders, Perturbation Series, and Oracles, SIAM, Philadelphia, 2014.   
[13] A. Bunse-Gerstner, D. Kubalinska, G. Vossen, and D. Wilczek ´ , $h _ { 2 }$ - norm optimal model reduction for large scale discrete dynamical MIMO systems, J. Comput. Appl. Math., 233 (2010), pp. 1202–1216.   
[14] E. E. Burniston and C. E. Siewert, The use of Riemann problems in solving a class of transcendental equations, Proc. Cambridge Phil. Soc., 73 (1973), pp. 111–118.   
[15] R. Corless, Generalized companion matrices for the Lagrange basis, in Proceedings of EACA, 2004, pp. 317–322.   
[16] J. H. Curtiss, Interpolation by harmonic polynomials, J. SIAM, 10 (1962), pp. 709–736.   
[17] P. J. Davis, On the numerical integration of periodic analytic functions, in R. E. Langer, ed., On Numerical Integration: Proceedings of a Symposium, Madison, April 21–23, 1958, University of Wisconsin, 1959, pp. 45–59.   
[18] L. M. Delves and J. N. Lyness, A numerical method for locating the zeros of an analytic function, Math. Comput., 21 (1967), pp. 543–560.   
[19] A. Draux, Formal orthogonal polynomials revisited. Applications, Numer. Algorithms, 11 (1996), pp. 143–158.   
[20] T. A. Driscoll and B. Fornberg, A Pad´e-based algorithm for overcoming the Gibbs phenomenon, Numer. Algorithms, 26 (2001), pp. 77–92.   
[21] M. Dupuy, Le calcul num´erique des fonctions par l’interpolation barycentrique, C. R. Acad. Sci., 226 (1948), 158–159.   
[22] O. E ¨ gecio ˜ glu and C¸ . Koc¸ ˜ , A fast algorithm for rational interpolation via orthogonal polynomials, Math. Comp., 53 (1989), pp. 249–264.   
[23] G. E. Fasshauer, Meshfree Approximation Methods with Matlab, World Scientific, Singapore, 2007.   
[24] L. Fej´er, Interpolation und konforme Abbildung, G¨ottinger Nachrichten (1918), pp. 319–331.   
[25] M. S. Floater and K. Hormann, Barycentric rational interpolation with no poles and high rates of approximation, Numer. Math., 107 (2007), pp. 315–331.   
[26] B. Fornberg and N. Flyer, A Primer on Radial Basis Functions with Applications to the Geosciences, CBMS-NSF Regional Conf. Ser. in Appl. Math. 87, SIAM, Philadelphia, 2015.   
[27] B. Fornberg, Numerical differentiation of analytic functions, ACM Trans. Math. Software, 7 (1981), pp. 512–526.   
[28] B. Fornberg and G. Wright, Stable computation of multiquadric interpolants for all values of the shape parameter, Comput. Math. Appl., 48 (2004), pp. 853–867.   
[29] S. Fortune, Polynomial root finding using iterated eigenvalue computation, in Proceedings of the International Symposium on Symbolic and Algebrica Computation, ACM, 2001, pp. 121–128.   
[30] B. Gavin and E. Polizzi, Non-linear-eigensolver-based alternative to traditional SCF methods, J. Chem. Phys., 138 (2013), pp. 1–8.   
[31] K. Glover, All optimal Hankel-norm approximations of linear multivariable systems and their $L ^ { \infty }$ -error bounds, Internat. J. Control, 39 (1984), pp. 1115– 1193.   
[32] S. Goedecker, Linear scaling electronic structure methods, Rev. Modern Phys., 71 (1999), pp. 1085–1123.   
[33] P. Gonnet, R. Pachon, and L. N. Trefethen ´ , Robust rational interpolation and least-squares, Electron. Trans. Numer. Anal., 38 (2011), pp. 146–167.   
[34] S. Gugercin, A. C. Antoulas, and C. Beattie, $\mathcal { H } _ { 2 }$ model reduction for large-scale linear dynamical systems, SIAM J. Matrix Anal. Appl., 30 (2008), pp. 609–638.   
[35] M. H. Gutknecht, Numerical conformal mapping methods based on function conjugation, J. Comput. Appl. Math, 14 (1986), pp. 31–77.   
[36] N. Hale, N. J. Higham, and L. N. Trefethen, Computing $A ^ { \alpha }$ , $\log ( A )$ , and related matrix functions by contour integrals, SIAM J. Numer. Anal., 46 (2008), pp. 2505–2523.   
[37] J. Helsing and R. Ojala, On the evaluation of layer potentials close to their sources, J. Comput. Phys., 227 (2008), pp. 2899–2921.   
[38] P. Henrici, Fast Fourier methods in complex analysis, SIAM Rev., 21 (1979), pp. 481–527.   
[39] P. Henrici, Essentials of Numerical Analysis with Pocket Calculator Demonstrations, Wiley, New York, 1982.   
[40] N. J. Higham, The numerical stability of barycentric Lagrange interpolation, IMA J. Numer. Anal., 24 (2004), pp. 547–556.   
[41] E. Hlawka, Interpolation analytischer Funktionen auf dem Einheitskreis, in Number Theory and Analysis, P. Tur´an, ed., Plenum, New York, 1969, pp. 99– 118.   
[42] T. Ikegami and T. Sakurai, Contour integral eigensolver for non-Hermitian systems: A Rayleigh–Ritz-type approach, Taiwan J. Math., 14 (2010), pp. 825– 837.

[43] T. Ikegami, T. Sakurai, and U. Nagashima, A filter diagonalization for generalized eigenvalue problems based on the Sakurai–Sugiura projection method, J. Comput. Appl. Math., 223 (2010), pp. 1927–1936.

[44] N. I. Ioakimidis, A modification of the classical quadrature method for locating zeros of analytic functions, BIT, 25 (1985), pp. 681–686.   
[45] N. I. Ioakimidis, K. E. Papadakis, and E. A. Perdios, Numerical evaluation of analytic functions by Cauchy’s theorem, BIT, 31 (1991), pp. 276–285.   
[46] D. Jackson, Roots and singular points of semi-analytic functions, Ann. of Math., 19 (1917), pp. 142–151.   
[47] C. G. J. Jacobi, Disquisitiones Analyticae de Fractionibus Simplicibus, Dissertation, Berlin, 1825.   
[48] C. G. J. Jacobi, Uber die Darstellung einer Reihe gegebner Werthe durch eine ¨ gebrochne rationale Function, J. Reine Angew. Math., 30 (1846), pp. 127–156.   
[49] R. Jentzsch, Untersuchungen zur Theorie Analytischer Funktionen, Dissertation, Berlin, 1914.   
[50] E. Kamgnia and B. Philippe, Counting eignevalues in domains of the complex field, Electron. Trans. Numer. Anal., 40 (2013), pp. 1–16.   
[51] A.-K. Kassam and L. N. Trefethen, Fourth-order time-stepping for stiff PDEs, SIAM J. Sci. Comput., 26 (2005), pp. 1214–1233.   
[52] A. Klockner, A. Barnett, L. Greengard, and M. O’Neil ¨ , Quadrature by expansion: A new method for the evaluation of layer potentials, J. Comput. Phys., 252 (2013), pp. 332–349.   
[53] L. Kramer, E. Di Napoli, M. Galgon, B. Lang, and P. Bientinesi ¨ , Dissecting the FEAST algorithm for generalized eigenproblems, J. Comput. Appl. Math., 244 (2013), pp. 1–9.   
[54] P. Kravanja, T. Sakurai, and M. Van Barel, On locating clusters of zeros of analytic functions, BIT, 39 (1999), pp. 646–682.   
[55] P. Kravanja and M. Van Barel, A derivative-free algorithm for computing zeros of analytic functions, Computing, 63 (1999), pp. 69–91.   
[56] P. Kravanja and M. Van Barel, Computing the Zeros of Analytic Functions, Lecture Notes in Math. 1727, Springer, New York, 2000.   
[57] S. E. Laux, Solving complex band structure problems with the FEAST eigenvalue algorithm, Phys. Rev. B, 86 (2012), 075103.   
[58] A. R. Levin, D. Zhang, and E. Polizzi, FEAST fundamental framework for electronic structure calculations: Reformulation and solution of the muffintin problem, Comput. Phys. Comm., 183 (2012), pp. 2370–2375.

[59] T.-Y. Li, On locating all zeros of an analytic function within a bounded domain by a revised Delves/Lyness method, SIAM J. Numer. Anal., 20 (1983), pp. 865– 871.

[60] L. Lin, J. Lu, L. Ying, and W. E, Pole-based approximation of the Fermi– Dirac function, Chin. Ann. Math. Ser. B, 30 (2009), pp. 729–742.

[61] R. Luck and J. W. Stevens, Explicit solutions for transcendental equations, SIAM Rev., 44 (2002), pp. 227–233.

[62] J. N. Lyness, Numerical algorithms based on the theory of complex variable, in Proceedings of the 22nd National Conference, ACM, 1967, pp. 125–133.

[63] J. N. Lyness and L. M. Delves, On numerical contour integration round a closed contour, Math. Comp., 21 (1967), pp. 561–577.

[64] J. N. Lyness and C. B. Moler, Numerical differentiation of analytic functions, SIAM J. Numer. Anal., 4 (1967), pp. 202–210.

[65] J. N. Lyness and G. Sande, Algorithm 413: ENTCAF and ENTCRE: Evaluation of normalized Taylor coefficients of an analytic function, Commun. ACM, 14 (1971), pp. 669–675.

[66] J. E. McCune, Exact inversion of dispersion relations, Phys. Fluids, 9 (1966), pp. 2082–2084.

[67] L. Meier III and G. G. Luenberger, Approximation of linear constant systems, IEEE Trans. Automat. Control, 12 (1967), pp. 585–588.

[68] C. M´eray, Observations sur la l´egitimit´e de l’interpolation, Ann. Sci. Ec. ´ Norm. Sup´er., 3 (1884), pp. 165–176.

[69] R. Pachon, P. Gonnet, and J. Van Deun ´ , Fast and stable rational interpolation in roots of unity and Chebyshev points, SIAM J. Numer. Anal., 50 (2012), pp. 1713–1734.

[70] C. Pearcy, An elementary proof of the power inequality for the numerical radius, Michigan Math. J., 13 (1966), pp. 289–291.

[71] E. Polizzi, Density-matrix-based algorithm for solving eigenvalue problems, Phys. Rev. B, 79 (2009), pp. 1–6.

[72] C. Runge, Theorie und Praxis der Reihen, G. J. G¨oschen, Leipzig, 1904.

[73] T. Sakurai, P. Kravanja, H. Sugiura, and M. Van Barel, An error analysis of two related quadrature methods for computing zeros of analytic functions, J. Comput. Appl. Math., 152 (2003), pp. 467–480.

[74] T. Sakurai and H. Sugiura, A projection method for generalized eigenvalue problems using numerical integration, J. Comput. Appl. Math, 159 (2003), pp. 119–128.

[75] T. Sakurai and H. Tadano, CIRR: A Rayleigh–Ritz type method with contour integral for generalized eigenvalue problems, Hokkaido Math. J., 36 (2007), pp. 745–757.   
[76] T. Schmelzer and L. N. Trefethen, Evaluating matrix functions for exponential integrators via Carath´eodory–Fej´er approximation and contour integrals, Electron. Trans. Numer. Anal., 29 (2007), pp. 1–18.   
[77] C. Schneider and W. Werner, Some new aspects of rational interpolation, Math. Comp., 47 (1986), pp. 285–299.   
[78] I. H. Sloan and R. S. Womersley, Extremal systems of points and numerical integration on the sphere, Adv. Comput. Math., 21 (2004), pp. 107–125.   
[79] R. Spira, Zeros of approximate functional approximations, Math. Comp., 21 (1967), pp. 41–48.   
[80] W. Squire and G. Trapp, Using complex variables to estimate derivatives of real functions, SIAM Rev., 40 (1998), pp. 110–112.   
[81] P. T. P. Tang and E. Polizzi, Subspace iteration with approximate spectral projection, SIAM J. Matrix Anal. Appl., 35 (2014), pp. 354–390.   
[82] A. Townsend, private communication, 2012.   
[83] L. N. Trefethen, Rational approximation on the unit disk, Numer. Math., 37 (1981), pp. 297–320.   
[84] L. N. Trefethen, Approximation Theory and Approximation Practice, SIAM, Philadelphia, 2013.   
[85] L. N. Trefethen and J. A. C. Weideman, The exponentially convergent trapezoidal rule, SIAM Rev., 56 (2014), pp. 385–458.   
[86] J. L. Walsh, The analogue for maximally convergent polynomials of Jentzsch’s theorem, Duke Math. J., 26 (1959), pp. 605–616.   
[87] J. L. Walsh, Interpolation and Approximation by Rational Functions in the Complex Domain, 5th ed., AMS, Providence, RI, 1969.   
[88] E. Wegert, Visual Complex Functions, Springer, New York, 2012.

# References

Each reference is followed by a note highlighting a contribution of that publication that is relevant to this book. These notes are by no means comprehensive: in most cases the reference includes other significant contributions too. Papers listed by authors such as Cauchy, Chebyshev, Gauss, Jacobi, and Weierstrass can also be found in their collected works.

Among mathematicians of the 19th century, it is hard not to be struck by the remarkable creativity of Jacobi (1804–1851), who in his short life made key early contributions to barycentric interpolation [1825], orthogonal polynomials and Gauss quadrature [1826], and Pad´e approximation and rational interpolation [1846], as well as innumerable topics outside the scope of this book.

As of September 2019, the Mathematics Genealogy Project lists 13445 academic descendants of Pafnuty Lvovich Chebyshev. For example, one chain runs Chebyshev–Lyapunov– Steklov–Smirnov–Sobolev–Ladyzhenskaya–Faddeev–Its and another runs Chebyshev– Markov–Voronoy–Sierpinsky–Mazurkiewicz–Zygmund–Stein–Fefferman.

N. I. Achieser (1930), On extremal properties of certain rational functions (Russian), DAN 18, 495–499. [Equioscillation characterization for best rational approximations.]

N. I. Achieser (1992), Theory of Approximation, Dover. [Treatise by one of Chebyshev’s academic great-grandsons, first published in 1956.]

V. Adamjan, D. Arov and M. Krein (1971), Analytic properties of Schmidt pairs for a Hankel operator and the generalized Schur–Takagi problem, Math. USSR Sb. 15, 31–73. [Major work with a general extension of results of Carath´eodory, Fej´er, Schur, and Takagi to rational approximation on the unit circle.]

L. Ahlfors (1978), Complex Analysis, 3rd ed., McGraw-Hill. [A terse and beautiful complex analysis text by one of the masters, first published in 1953.]

N. Ahmed and P. S. Fisher (1970), Study of algorithmic properties of Chebyshev coefficients, Int. J. Comp. Math. 2, 307–317. [Possibly the first paper to point out that Chebyshev coefficients can be computed by the FFT.]

A. C. Aitken (1926), On Bernoulli’s numerical solution of algebraic equations, Proc. Roy. Soc. Edinb. 46, 289–305. [Discussion of Aitken extrapolation.]   
B. K. Alpert and V. Rokhlin (1991), A fast algorithm for the evaluation of Legendre expansions, SIAM J. Sci. Statist. Comput. 12, 158–179. [Algorithm for converting between Legendre and Chebyshev expansion coefficients.]   
A. Amiraslani (2006), New Algorithms for Matrices, Polynomials, and Matrix Polynomials, PhD diss., U. Western Ontario. [Algorithms related to rootfinding by values rather than Chebyshev coefficients.]   
A. Amiraslani, R. M. Corless, L. Gonzalez-Vega and A. Shakoori (2004), Polynomial algebra by values, TR-04-01, Ontario Research Center for Computer Algebra. [Outlines eigenvalue-based algorithms for finding roots of polynomials from their values at sample points rather than from coefficients in an expansion.]   
A. C. Antoulas (2005), Approximation of Large-Scale Dynamical Systems, SIAM. [Textbook about model reduction, a subject making much use of rational approximation.] A. I. Aptekarev (2002), Sharp constants for rational approximations of analytic functions, $S b$ . Math. 193, 1–72. [Extends the result of Gonchar & Rakhmanov 1989 on rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ to give the precise asymptotic form $E _ { n n } \sim 2 H ^ { n + 1 / 2 }$ first conjectured by Magnus, where $H$ is Halphen’s constant.]   
J. L. Aurentz and L. N. Trefethen (2017a), Block operators and spectral discretizations, SIAM Rev. 59, 423–446. [General presentation of rectangular discretization ideas springing from Driscoll and Hale 2015, the basis of Chebfun’s treatment of ODE BVPs.] J. L. Aurentz and L. N. Trefethen (2017b), Chopping a Chebyshev series, ACM Trans. Math. Softw. 43, 33. [Details of Chebfun’s algorithm for chopping a Chebyshev series at machine precision.]   
T. Bagby and N. Levenberg (1993), Bernstein theorems, New Zeal. J. Math. 22, 1–20. [Presentation of four proofs of Bernstein’s result that best polynomial approximants to a function $f \in C ( [ - 1 , 1 ] )$ converge geometrically if and only if $f$ is analytic, with discussion of extension to higher dimension.]   
G. A. Baker, Jr. and P. Graves-Morris (1996), Pad´e Approximants, 2nd ed., Cambridge U. Press. [The standard reference on many aspects of Pad´e approximations and their applications.]   
N. S. Bakhvalov (1967), On the optimal speed of integrating analytic functions, Comput. Math. Math. Phys. 7, 63–75. [A theoretical paper that introduces the idea of going beyond polynomials to speed up Gauss quadrature by means of a change of variables/conformal map, as in Hale & Trefethen 2008.]   
S. Barnett (1975a), A companion matrix analogue for orthogonal polynomials, Lin. Alg. Applics. 12, 197–208. [Generalization of Good’s colleague matrices to orthogonal polynomials other than Chebyshev. Barnett apparently did not know that Specht 1957 had covered the same ground.]   
S. Barnett (1975b), Some applications of the comrade matrix, Internat. J. Control 21, 849–855. [Further discussion of comrade matrices.]   
Z. Battles (2005), Numerical Linear Algebra for Continuous Functions, DPhil thesis, Oxford U. Computing Laboratory. [Presentation of Chebfun, including description of the Chebfun rootfinding algorithm based on recursion and eigenvalues of colleague matrices.] Z. Battles and L. N. Trefethen (2004), An extension of MATLAB to continuous functions and operators, SIAM J. Sci. Comput. 25, 1743–1770. [Chebfun was conceived on December 8, 2001, and this was the first publication about it.]

F. L. Bauer (1959), The quotient-difference and epsilon algorithms, in R. E. Langer, ed., On Numerical Approximation, U. Wisconsin Press, pp. 361–370. [Introduction of the eta extrapolation algorithm for series.]

R. Bellman, B. G. Kashef and J. Casti (1972), Differential quadrature: A technique for the rapid solution of nonlinear partial differential equations, J. Comput. Phys. 10, 40–52. [Perhaps the first publication to give a formula for the entries of a spectral differentiation matrix.]

S. N. Bernstein (1911), Sur l’approximation des fonctions continues par des polynˆomes, Compt. Rend. Acad. Sci. 152, 502–504. [Announcement of some results proved in Bernstein 1912b.]

S. N. Bernstein (1912a), Sur les recherches r´ecentes relatives \`a la meilleure approximation des fonctions continues par des polynˆomes, in Proc. 5th Intern. Math. Congress, v. 1, pp. 256–266. [Announcement of the results of Bernstein and Jackson on polynomial approximation, including a table summarizing theorems by Bernstein, Jackson, and Lebesgue linking smoothness to rate of convergence.]

S. N. Bernstein (1912b), Sur l’ordre de la meilleure approximation des fonctions continues par des polynˆomes de degr´e donn´e, M´em. Acad. Roy. Belg., 1–104. [Major work, which won a prize from the Belgian Academy of Sciences, establishing a number of the Jackson and Bernstein theorems on rate of convergence of best approximations for differentiable or analytic $f$ . Bernstein’s fundamental estimates for functions analytic in an ellipse appear in Sections 9 and 61.]

S. N. Bernstein (1912c), Sur la valeur asymptotique de la meilleure approximation des fonctions analytiques, Compt. Rend. Acad. Sci. 155, 1062–1065. [One of the first appearances of Bernstein ellipses, used here to analyze convergence of best approximations for a function with a single real singularity on the ellipse.]

S. N. Bernstein (1912d), D´emonstration du th´eor\`eme de Weierstrass fond´ee sur le calcul des probabilit´es, Proc. Math. Soc. Kharkov 13, 1–2. [Bernstein’s proof of the Weierstrass approximation theorem based on Bernstein polynomials.]

S. N. Bernstein (1914a), Sur la meilleure approximation des fonctions analytiques poss´edant des singularit´es complexes, Compt. Rend. Acad. Sci. 158, 467–469. [Generalization of Bernstein 1912c to functions with a conjugate pair of singularities.]

S. N. Bernstein (1914b), Sur la meilleure approximation de $| x |$ par des polynˆomes de degr´es donn´es, Acta Math. 37, 1–57. [Investigates polynomial best approximation of $| x |$ on $[ - 1 , 1 ]$ and mentions as a “curious coincidence” that $n E _ { n } \approx 1 / 2 \sqrt { \pi }$ , a value that became known as the “Bernstein conjecture,” later shown false by Varga and Carpenter.]

S. N. Bernstein (1919), Quelques remarques sur l’interpolation, Math. Annal. 79, 1–12. [Written in 1914 but delayed in publication by the war, this paper, like Faber 1914, pointed out that no array of nodes for interpolation could yield convergence for all continuous functions.]

S. N. Bernstein (1931), Sur la limitation des valeurs d’un polynˆomes $P ( x )$ de degr´e $_ n$ sur tout un segment par ses valeurs en $( n + 1 )$ points du segment, Izv. Akad. Nauk SSSR 7, 1025–1050. [Discussion of the problem of optimal interpolation nodes, defined by minimization of the Lebesgue constant.]

S. N. Bernstein (1938), On the inverse problem of the theory of the best approximation of continuous functions, Sochineya 2, 292–294. [Bernstein’s lethargy theorem.]

J.-P. Berrut (1988), Rational functions for guaranteed and experimentally wellconditioned global interpolation, Comput. Math. Appl. 15, 1–16. [Observes that if the barycentric formula is applied on an arbitrary grid with weights $1 , - 1 , 1 , - 1 , \ldots$ or ${ \scriptstyle { \frac { 1 } { 2 } } , - 1 , 1 , - 1 \ldots }$ , the resulting rational interpolants are pole-free and accurate.]

J.-P. Berrut, R. Baltensperger and H. D. Mittelmann (2005), Recent developments in barycentric rational interpolation, Intern. Ser. Numer. Math. 151, 27–51. [Combines conformal maps with the rational barycentric formula to get high-accuracy approximations of difficult functions.]

J.-P. Berrut, M. S. Floater and G. Klein (2011), Convergence rates of derivatives of a family of barycentric rational interpolants, Appl. Numer. Math. 61, 989–1000. [Establishes convergence rates for derivatives of Floater–Hormann barycentric rational interpolants.]

J.-P. Berrut and L. N. Trefethen (2004), Barycentric Lagrange interpolation, SIAM Rev. 46, 501–517. [Review of barycentric formulas for polynomial and trigonometric interpolation.]

A. Birkisson and T. A. Driscoll (2012), Automatic Fr´echet differentiation for the numerical solution of boundary-value problems. ACM Trans. Math. Softw. 38, 26. [Description of Chebfun’s method for solving nonlinear differential equations based on Newton or damped-Newton iteration and automatic differentiation.]

H.-P. Blatt, A. Iserles and E. B. Saff (1987), Remarks on the behaviour of zeros of best approximating polynomials and rational functions, in J. C. Mason and M. G. Cox, eds., Algorithms for Approximation, Clarendon Press, pp. 437–445. [Shows that the type $( n , n )$ best rational approximations to $| x |$ on $[ - 1 , 1 ]$ have all their zeros and poles on the imaginary axis and converge to $_ x$ in the right half-plane and to $- x$ in the left half-plane.]

H.-P. Blatt and E. B. Saff (1986), Behavior of zeros of polynomials of near best approximation, J. Approx. Th. 46, 323–344. [Shows that if $f \in C ( [ - 1 , 1 ] )$ is not analytic on $[ - 1 , 1 ]$ , then the roots of its best approximants $\{ p _ { n } ^ { * } \}$ cluster at every point of $[ - 1 , 1 ]$ as $n \to \infty$ .]

H. F. Blichfeldt (1901), Note on the functions of the form $f ( x ) \equiv \phi ( x ) + a _ { 1 } x ^ { n - 1 } +$ $a _ { 2 } x ^ { n - 2 } + \cdots + a _ { n }$ which in a given interval differ the least possible from zero, Trans. Amer. Math. Soc. 2, 100–102. [Blichfeldt proves a part of the equioscillation theorem: optimality implies equioscillation.]

M. Bocher ˆ (1906), Introduction to the theory of Fourier’s series, Ann. Math. 7, 81–152. [The paper that named the Gibbs phenomenon.]

I. Bogaert (2014), Iteration-free computation of Gauss–Legendre quadrature nodes and weights, SIAM J. Sci. Comput. 36, A1008–A1026. [Fastest known algorithm for computing nodes and weights even in millions of points, used by Chebfun.]

$\acute { \mathrm { E } }$ . Borel (1905), Le¸cons sur les fonctions de variables r´eelles et les d´eveloppements en s´eries de polynˆomes, Gauthier-Villars, Paris. [The first textbook essentially about approximation theory, including a proof of the equioscillation theorem, which Borel attributes to Kirchberger.]

F. Bornemann, D. Laurie, S. Wagon and J. Waldvogel (2004), The SIAM 100-Digit Challenge: A Study in High-Accuracy Numerical Computing, SIAM. [Detailed study of ten problems whose answers are each a single number, nine of which the authors manage to compute to 10000 digits of accuracy through the use of ingenious algorithms and acceleration methods.]

J. P. Boyd (2001), Chebyshev and Fourier Spectral Methods, 2nd ed., Dover. [A 668-page treatment of the subject with a great deal of practical information.]

J. P. Boyd (2002), Computing zeros on a real interval through Chebyshev expansion and polynomial rootfinding, SIAM J. Numer. Anal. 40, 1666–1682. [Proposes recursive Chebyshev expansions for finding roots of real functions, the idea that is the basis of the roots command in Chebfun.]

J. P. Boyd (2014), Solving Transcendental Equations: The Chebyshev Polynomial Proxy and Other Numerical Rootfinders, Perturbation Series, and Oracles, SIAM. [Presentation of a wide range of ideas related to the proxy rootfinding idea stemming from Good 1961 and used by Chebfun.]

D. Braess (1984), On the conjecture of Meinardus on rational approximation to $e ^ { x }$ . II, $J$ . Approx. Th. 40, 375–379. [Establishes an asymptotic formula conjectured by Meinardus for the best approximation error of $e ^ { x }$ on $[ - 1 , 1 ]$ .]

D. Braess (1986), Nonlinear Approximation Theory, Springer. [Advanced text on rational approximation and other topics, with emphasis on methods of functional analysis.]

C. Brezinski (1996), Extrapolation algorithms and Pad´e approximations: A historical survey, Appl. Numer. Math. 20, 299–318. [Historical survey.]

C. Brezinski and M. Redivo Zaglia (1991), Extrapolation Methods: Theory and Practice, North-Holland. [Extensive survey.]

L. Brutman (1978), On the Lebesgue function for polynomial interpolation, SIAM J. Numer. Anal. 15, 694–704. [Sharpening of a result of Erd˝os 1961 concerning Lebesgue constants.]

L. Brutman (1997), Lebesgue functions for polynomial interpolation—a survey, Ann. Numer. Math. 4, 111–127. [Exceptionally useful survey, including detailed results on interpolation in Chebyshev points.]

P. Butzer and F. Jongmans (1999), P. L. Chebyshev (1821–1894): A guide to his life and work, J. Approx. Th. 96, 111–138. [Discussion of the leading Russian mathematician of the 19th century.]

C. Canuto, M. Y. Hussaini, A. Quarteroni and T. A. Zang (2006), Spectral Methods: Fundamentals in Single Domains, Springer. [A major monograph on both collocation and Galerkin spectral methods.]

C. Carath´eodory and L. Fej´er (1911), Uber den Zusammenhang der Extremen von ¨ harmonischen Funktionen mit ihrer Koeffizienten und ¨uber den Picard-Landauschen Satz, Rend. Circ. Mat. Palermo 32, 218–239. [The paper that led, together with Schur 1918, to the connection of approximation problems with eigenvalues and singular values of Hankel matrices, later the basis of the Carath´eodory–Fej´er method for near-best approximation.]

A. J. Carpenter, A. Ruttan and R. S. Varga (1984), Extended numerical computations on the “1/9” conjecture in rational approximation theory, in P. Graves-Morris, E. B. Saff and R. S. Varga, eds., Rational Approximation and Interpolation, Lect. Notes Math. 1105, Springer. [Calculation to 40 significant digits of the best rational approximations to $e ^ { x }$ on $( - \infty , 0 ]$ of types $( 0 , 0 ) , ( 1 , 1 ) , \dots , ( 3 0 , 3 0 )$ .]

A. L. Cauchy (1821), Sur la formule de Lagrange relative \`a l’interpolation, Cours d’Analyse de l’Ecole Royale Polytechnique: Analyse alg´ebrique, ´ Imprimerie Royale, Paris. [First treatment of the “Cauchy interpolation problem” of interpolation by rational functions.]

A. L. Cauchy (1826), Sur un nouveau genre de calcul analogue au calcul infinit´esimal, Exerc. Math´ematiques 1, 11–24. [One of Cauchy’s foundational texts on residue calculus, including a derivation of what became known as the Hermite integral formula.]

P. L. Chebyshev (1854), Th´eorie des m´ecanismes connus sous le nom de parall´elogrammes, M´em. Acad. Sci. P´etersb., Series 7, 539–568. [Introduction of the idea of best approximation by polynomials in the supremum norm.]

P. L. Chebyshev (1859), Sur les questions de minima qui se rattachent \`a la repr´esentation approximative des fonctions, M´em. Acad. Sci. P´etersb. Series 7, 199–291. [Chebyshev’s principal work on best approximation.]

E. W. Cheney (1999), Introduction to Approximation Theory, Chelsea. [Classic approximation theory text first published in 1966.]

J. F. Claerbout (1985), Imaging the Earth’s Interior, Blackwell. [Text about the mathematics of migration for earth imaging by the man who developed many of these techniques, based on rational approximations of pseudodifferential operators.]

C. W. Clenshaw and A. R. Curtis (1960), A method for numerical integration on an automatic computer, Numer. Math. 2, 197–205. [Introduction of Clenshaw–Curtis quadrature.]

C. W. Clenshaw and K. Lord (1974), Rational approximations from Chebyshev series, in B. K. P. Scaife, ed., Studies in Numerical Analysis, Academic Press, pp. 95–113. [Analysis of Chebyshev–Pad´e approximations.]

W. J. Cody (1975), The FUNPACK package of special function subroutines, ACM Trans. Math. Softw. 1, 13–25. [Codes for evaluating special functions based on rational approximations.]

W. J. Cody (1993), Algorithm 715: SPECFUN—A portable FORTRAN package of special function routines and test drivers, ACM Trans. Math. Softw. 19, 22–32. [Descendant of FUNPACK with greater portability.]

W. J. Cody, W. Fraser and J. F. Hart (1968), Rational Chebyshev approximation using linear equations, Numer. Math. 12, 242–251. [Algol 60 code for best rational approximation by a variant of the Remez algorithm.]

W. J. Cody, G. Meinardus and R. S. Varga (1969), Chebyshev rational approximations to $e ^ { - x }$ in $[ 0 , + \infty )$ and applications to heat-conduction problems, J. Approx. Th. 2, 50–65. [Introduces the problem of approximation of $e ^ { - x }$ on $[ 0 , \infty )$ , or equivalently $e ^ { x }$ on $( - \infty , 0 ]$ , and shows that rational best approximants converge geometrically.]

R. M. Corless and S. M. Watt (2004), Bernstein bases are optimal, but, sometimes, Lagrange bases are better, in Proc. SYNASC (Symbolic and Numeric Algorithms for Scientific Computing), Timisoara, pp. 141–152. [A contribution to polynomial rootfinding with a marvelous title.]

G. Darboux (1878), M´emoire sur l’approximation des fonctions de tr\`es-grands nombres, et sur une classe ´etendue de d´eveloppements en s´erie, J. Math. Pures Appl. 4, 5–56. [3-term recurrence for orthogonal polynomials.]

S. Darlington (1970), Analytical approximations to approximations in the Chebyshev sense, Bell System Tech. J. 49, 1–32. [A precursor to the Carath´eodory–Fej´er method.]

P. J. Davis (1975), Interpolation and Approximation, Dover. [A leading text on the subject, first published in 1963.]

P. J. Davis and P. Rabinowitz (1984), Methods of Numerical Integration, 2nd ed., Academic Press. [The leading reference on numerical integration, with detailed information on many topics, first published in 1975.]

D. Day and L. Romero (2005), Roots of polynomials expressed in terms of orthogonal polynomials, SIAM J. Numer. Anal. 43, 1969–1987. [A rediscovery of the results of Specht, Good, Barnett, and others on colleague and comrade matrices.]

C. de Boor and A. Pinkus (1978), Proof of the conjectures of Bernstein and Erd˝os concerning the optimal nodes for polynomial interpolation, J. Approx. Th. 24, 289–303. [Together with Kilgore 1978, one of the papers solving the theoretical problem of optimal interpolation.]

R. A. DeVore and G. G. Lorentz (1993), Constructive Approximation, Springer. [A monograph emphasizing advanced topics.]

Z. Ditzian and V. Totik (1987), Moduli of Smoothness, Springer. [Careful analysis of smoothness and its effect on polynomial approximation on an interval, including the dependence on location in the interval.]

T. A. Driscoll, F. Bornemann and L. N. Trefethen (2008), The chebop system for automatic solution of differential equations, BIT Numer. Math. 48, 701–723. [Extension of Chebfun to solve differential and integral equations.]   
T. A. Driscoll and N. Hale (2015), Rectangular spectral collocation, IMA J. Numer. Anal. 36, 108–132. [Introduction of spectral collocation methods based on rectangular matrices. See also Aurentz & Trefethen 2017a.]   
M. Dupuy (1948), Le calcul num´erique des fonctions par l’interpolation barycentrique, Compt. Rend. Acad. Sci. 226, 158–159. [This paper is apparently the first to use the expression “barycentric interpolation” and also the first to generalize barycentric interpolation beyond the case of equidistant points considered by Taylor 1945.]   
A. Dutt, M. Gu and V. Rokhlin (1996), Fast algorithms for polynomial interpolation, integration, and differentiation, SIAM J. Numer. Anal. 33, 1689–1711. [Uses the Fast Multipole Method to derive fast algorithms for non-Chebyshev points.]   
H. Ehlich and K. Zeller (1966), Auswertung der Normen von Interpolationsoperatoren, Math. Ann. 164, 105–112. [Bound on Lebesgue constant for interpolation in Chebyshev points.]   
D. Elliott (1973), A direct method for “almost” best uniform approximation, in F. de Hoog and C. Jarvis, eds., Error, Approximation, and Accuracy, U. Queensland Press, pp. 129–143. [A precursor to the Carath´eodory–Fej´er method.]   
M. Embree and D. Sorensen (2013), An Introduction to Model Reduction for Linear and Nonlinear Differential Equations, to appear. [Long-awaited textbook.]   
B. Engquist and A. Majda (1977), Absorbing boundary conditions for the numerical simulation of waves, Math. Comp. 31, 629–651. [Highly influential paper on the use of Pad´e approximations to a pseudodifferential operator to develop numerical boundary conditions.]   
P. Erdos˝ (1961), Problems and results on the theory of interpolation. II, Acta Math. Acad. Sci. Hungar. 12, 235–244. [Shows that Lebesgue constants for optimal interpolation points are no better than for Chebyshev points asymptotically as $n \to \infty$ .]   
T. O. Espelid (2004), Extended doubly adaptive quadrature routines, Tech. Rep. 266, Dept. Informatics, U. Bergen. [Presentation of the exceptionally fast and accurate coteda and da2glob quadrature codes.]   
L. Euler (1760), De seriebus divergentibus, Novi Commentarii academiae scientiarum Petropolitanae 5, 205–237. [Early work on divergent series.]   
L. Euler (1783), De eximio usu methodi interpolationum in serierum doctrina, Opuscula Analytica 1, 157–210. [A work on various applications of interpolation, including equations related to the Newton and Lagrange formulas for polynomial interpolation.]   
L. C. Evans and R. F. Gariepy (1991), Measure Theory and Fine Properties of Functions, CRC Press. [Includes a definition of the total variation in the measure theoretic context.]   
G. Faber (1914), Uber die interpolatorische Darstellung stetiger Funktion ¨ en, Jahresber. Deutsch. Math. Verein. 23, 190–210. [Shows that no fixed system of nodes for polynomial interpolation will lead to convergence for all continuous $f$ .]   
L. Fej´er (1900), Sur les fonctions born´ees et int´egrables, Compt. Rend. Acad. Sci. 131, 984–987. [Fej´er, age 20, provides a new method of summing divergent Fourier series, with

a new proof of the Weierstrass approximation theorem as a corollary.]

L. Fej´er (1910), Lebesguesche Konstanten und divergente Fourierreihen, J. f. Math. 138, 22–53. [Shows that Lebesgue constants for Fourier projection are asymptotic to $( 4 / \pi ^ { 2 } ) \log n$ as $n \to \infty$ .]

L. Fej´er (1916), Ueber Interpolation, Nachr. Gesell. Wiss. G¨ottingen Math. Phys. Kl., 66–91. [Proves the Weierstrass approximation theorem by showing that Hermite–Fej´er interpolants in Chebyshev points of the first kind converge for any $f \in C ( [ - 1 , 1 ] )$ .]

S.-I. Filip, Y. Nakatsukasa, L. N. Trefethen and B. Beckermann (2018), Rational minimax approximation via adaptive barycentric representations, SIAM J. Sci. Comput. 40, A2427–A2455. [Chebfun implementation of Remez algorithm for computing polynomial and rational best approximations.]

A. M. Finkelshtein (2006), Equilibrium problems of potential theory in the complex plane, in Orthogonal Polynomials and Special Functions, Lect. Notes Math. 1883, Springer, pp. 79–117. [Survey article.]

M. S. Floater and K. Hormann (2007), Barycentric rational interpolation with no poles and high rates of approximation, Numer. Math. 107, 315–331. [Extension of results of Berrut 1988 to a family of barycentric rational interpolants of arbitrary order.]

G. B. Folland (1995), Introduction to Partial Differential Equations, 2nd ed., Princeton U. Press. [An elegant introduction to PDEs published first in 1976, including the Weierstrass approximation theorem proved via the heat equation in one or multiple dimensions.]

B. Fornberg (1988), Generation of finite difference formulas on arbitrarily spaced grids, Math. Comp. 51, 699–706. [Stable algorithm for generating finite difference formulas on arbitrary grids.]

B. Fornberg (1996), A Practical Guide to Pseudospectral Methods, Cambridge U. Press. [Practically oriented textbook of spectral collocation methods for solving ODEs and PDEs, based on Chebyshev interpolants.]

S. Fortune (2001), Polynomial root finding using iterated eigenvalue computation, in Proc. 2001 Intl. Symp. Symb. Alg. Comput., ACM, pp. 121–128. [An eigenvalue-based rootfinding algorithm that works directly from data samples rather than expansion coefficients.]

L. Fox and I. B. Parker (1968), Chebyshev Polynomials in Numerical Analysis, Oxford U. Press. [A precursor to the work of the 1970s and later on Chebyshev spectral methods.]

J. G. F. Francis (1961), The QR transformation: A unitary analogue to the LR transformation, parts I and II, Computer J. 4, 256–272 and 332–345. [Introduction of the QR algorithm for numerical computation of matrix eigenvalues.]

A. P. Frankel and W. B. Gragg (1973), Algorithmic almost best uniform rational approximation with error bounds (abstract), SIAM Rev. 15, 418–419. [Short note proposing a method of Chebyshev–Pad´e approximation for $m \geq n$ , based on transplantation to the unit circle.]

G. Freud (1955), Uber einseitige Approximation durch Polynome I, ¨ Acta Sci. Math. (Szeged) 6, 12–28. [Precursor to Xiang & Bornemann 2012.]

G. Frobenius (1881), Ueber Relationen zwischen den N¨aherungsbr¨uchen von Potenzreihen, J. Reine Angew. Math. 90, 1–17. [The first systematic treatment of Pad´e approximation.]

M. Froissart (1969), Approximation de Pad´e: application \`a la physique des particules ´el´ementaires, RCP, Programme No. 25, v. 9, CNRS, Strasbourg, pp. 1–13. [A rare publication by the mathematician and physicist after whom Froissart doublets were named (by Bessis).]

D. Gaier (1987), Lectures on Complex Approximation, Birkh¨auser. [A shorter book presenting some of the material considered at greater length in Smirnov & Lebedev 1968 and Walsh 1969.]

C. F. Gauss (1814), Methodus nova integralium valores per approximationem inveniendi, Comment. Soc. Reg. Scient. Gotting. Recent., pp. 39–76. [Introduction of Gauss quadrature—via continued fractions, not orthogonal polynomials.]

W. Gautschi (1981), A survey of Gauss–Christoffel quadrature formulae, in P. L. Butzer and F. Feh´er, eds., E. B. Christoffel: The Influence of His Work in Mathematics and the Physical Sciences, Birkh¨auser, pp. 72–147. [Outstanding survey of many aspects of Gauss quadrature.]

W. Gautschi (2004), Orthogonal Polynomials: Computation and Approximation, Oxford U. Press. [A monograph on orthogonal polynomials with emphasis on numerical aspects.]

K. O. Geddes (1978), Near-minimax polynomial approximation in an elliptical region, SIAM J. Numer. Anal. 15, 1225–1233. [Chebyshev expansions via the FFT for analytic functions on an interval.]

K. O. Geddes (1981), Block structure in the Chebyshev–Pad´e table, SIAM J. Numer. Anal. 18, 844–861. [Analysis of Chebyshev–Pad´e approximants, showing that previous formulations may break down in cases corresponding to a transplanted problem having poles inside the unit disk.]

W. M. Gentleman (1972a), Implementing Clenshaw–Curtis quadrature, I: Methodology and experience, Comm. ACM 15, 337–342. [A surprisingly modern paper that includes the aliasing formula for Chebyshev polynomials.]

W. M. Gentleman (1972b), Implementing Clenshaw–Curtis quadrature, II: Computing the cosine transformation, Comm. ACM 15, 343–346. [First connection of Clenshaw–Curtis quadrature with the FFT.]

A. Glaser, X. Liu and V. Rokhlin (2007), A fast algorithm for the calculation of the roots of special functions, SIAM J. Sci. Comput. 29, 1420–1438. [Introduction of an algorithm for computation of Gauss quadrature nodes and weights in $O ( n )$ operations rather than $O ( n ^ { 2 } )$ as in Golub & Welsch 1969.]

K. Glover (1984), All optimal Hankel-norm approximations of linear multivariable systems and their $L ^ { \infty }$ -error bounds, Internat. J. Control 39, 1115–1193. [Highly influential article on rational approximations in control theory.]

S. Goedecker (1994), Remark on algorithms to find roots of polynomials, SIAM J. Sci. Comput. 15, 1059–1063. [Emphasizes the stability of companion matrix eigenvalues as an algorithm for polynomial rootfinding, given a polynomial expressed by its coefficients in the monomial basis.]

G. H. Golub and J. H. Welsch (1969), Calculation of Gauss quadrature rules, Math. Comp. 23, 221–230. [Presentation of the famous $O ( n ^ { 2 } )$ algorithm for Gauss quadrature nodes and weights via a tridiagonal Jacobi matrix eigenvalue problem.]

A. A. Gonchar and E. A. Rakhmanov (1989), Equilibrium distributions and degree of rational approximation of analytic functions, Math. USSR-Sb. 62, 305–348. [A landmark paper, first published in Russian in 1987, that applies methods of potential theory to prove that the optimal rate of convergence for type $( n , n )$ rational minimax approximations of $e ^ { x }$ on $( - \infty , 0 ]$ is $O ( ( 9 . 2 8 9 0 3 \dots . . . ) ^ { - n } )$ as $n \to \infty$ .]

V. L. Goncharov (2000), The theory of best approximation of functions, J. Approx. Th. 106, 2–57. [English translation of a 1945 historical survey in Russian emphasizing contributions of Chebyshev and his successors.]

P. Gonnet, S. Guttel and L. N. Trefethen ¨ (2013), Robust Pad´e approximation via SVD, SIAM Rev. 55, 101–117. [Introduction of the robust SVD-based algorithm for computing Pad´e approximants presented in Chapter 27.]

P. Gonnet, R. Pachon and L. N. Trefethen ´ (2011), Robust rational interpolation and least-squares, Elect. Trans. Numer. Anal. 38, 146–167. [A robust algorithm based on the SVD for computing rational approximants without spurious poles.]

I. J. Good (1961), The colleague matrix, a Chebyshev analogue of the companion matrix, Quart. J. Math. 12, 61–68. [Together with Specht 1960, one of the two original independent discoveries that roots of polynomials in Chebyshev form can be computed as eigenvalues of colleague matrices, a term introduced here. Good recommends this approach to numerical rootfinding for functions other than polynomials too; see Boyd 2014.]

A. Gopal and L. N. Trefethen (2019a), New Laplace and Helmholtz solvers, Proc. Natl. Acad. Sci. USA 116, 10223–10225. [Announcement of new algorithms for solving PDEs on regions with corner singularities based on rational approximations with root-exponential convergence as in Newman 1964.]

A. Gopal and L. N. Trefethen (2019b), Solving Laplace problems with corner singularities via rational functions, SIAM J. Numer. Anal. 57, 2074–2094. [Details of the “lightning Laplace solver” announced in the paper above, including a proof of root-exponential convergence based on Hermite and Cauchy integrals.]

D. Gottlieb, M. Y. Hussaini and S. A. Orszag (1984), Theory and applications of spectral methods, in R. G. Voigt, D. Gottlieb, and M. Y. Hussaini, eds., Spectral Methods for Partial Differential Equations, SIAM, pp. 1–54. [Early survey article on spectral collocation methods, including the first publication of the formula for the entries of Chebyshev differentiation matrices.]

W. B. Gragg (1972), The Pad´e table and its relation to certain algorithms of numerical analysis, SIAM Rev. 14, 1–62. [A careful and extensive mathematical reference on the structure and algebra of the Pad´e table as presented in Chapter 27, though with an emphasis on determinants.]

A. Greenbaum and L. N. Trefethen (1994), GMRES/CR and Arnoldi/Lanczos as matrix approximation problems, SIAM J. Sci. Comput. 15, 359–368. [Shows that the GMRES/CR and Arnoldi/Lanczos matrix iterations are equivalent to certain polynomial approximation problems and generalizes this observation to matrix approximation problems such as “ideal GMRES.”]

T. H. Gronwall (1912), Uber die Gibbssche Erscheinung und die trigonometrischen ¨ Summen $\sin x + { \frac { 1 } { 2 } } \sin 2 x + \cdots + { \frac { 1 } { n } } \sin n x$ , Math. Ann. 72, 228–243. [Investigates detailed behavior of Fourier approximations near Gibbs discontinuities.]

M. H. Gutknecht (1983), Algebraically solvable Chebyshev approximation problems, in C. K. Chui, L. L. Schumaker, and J. D. Ward., eds., Approximation Theory IV, Academic Press. [Shows that many examples of $\infty$ -norm best approximations that can be written down explicitly correspond to Carath´eodory–Fej´er approximations.]

M. H. Gutknecht (1990), In what sense is the rational interpolation problem well posed?, Constr. Approx. 6, 437–450. [Generalization of Trefethen & Gutknecht 1985 from Pad´e to multipoint Pad´e approximation.]

M. H. Gutknecht and L. N. Trefethen (1982), Real polynomial Chebyshev approximation by the Carath´eodory–Fej´er method, SIAM J. Numer. Anal. 19, 358–371. [Introduction of CF approximation on an interval.]

S. Guttel ¨ (2010), Rational Krylov Methods for Operator Functions, PhD diss., TU Bergakademie Freiberg. [Survey and analysis of advanced methods of numerical linear algebra based on rational approximations.]

N. Hale, N. J. Higham and L. N. Trefethen (2008), Computing $A ^ { \alpha }$ , $\log ( A )$ , and related matrix functions by contour integrals, SIAM J. Numer. Math. 46, 2505–2523. [Derives efficient algorithms for computing matrix functions from trapezoidal rule approximations to contour integrals accelerated by contour maps. These are equivalent to rational approximations.]

N. Hale and T. W. Tee (2009), Conformal maps to multiply slit domains and applications, SIAM J. Sci. Comput. 31, 3195–3215. [Extension of Tee & Trefethen 2006 to new geometries and applications.]

N. Hale and A. Townsend (2013), Fast and accurate computation of Gauss–Legendre and Gauss–Jacobi quadrature nodes and weights, SIAM J. Sci. Comput. 35, A652–A674. [Proposes an $O ( n )$ algorithm based on asymptotic formulas for computing Gauss quadrature nodes and weights for large $_ n$ , faster than the Glaser–Liu–Rokhlin algorithm and also more accurate. See also Bogaert 2014.]

N. Hale and L. N. Trefethen (2008), New quadrature formulas from conformal maps, SIAM J. Numer. Anal. 46, 930–948. [Shows that conformal mapping can be used to derive quadrature formulas that converge faster than Gauss, as in Bakhvalov 1967.]

N. Hale and L. N. Trefethen (2012), Chebfun and numerical quadrature, Science China Math. 55, 1749–1760. [Review of quadrature algorithms in Chebfun, including fast Gauss and Gauss–Legendre quadrature by the Glaser–Liu–Rokhlin algorithm (but not yet the Hale–Townsend algorithm) with applications to computing with functions with singularities.]

L. Halpern and L. N. Trefethen (1988), Wide-angle one-way wave equations, $J$ . Acoust. Soc. Amer. 84, 1397–1404. [Review of rational approximations to $\sqrt { 1 - s ^ { 2 } }$ on $[ - 1 , 1 ]$ for application to one-way wave equations.]

G. H. Halphen (1886), Trait´e des fonctions elliptiques et de leurs applications, Gauthier-Villars, Paris. [A treatise on elliptic functions that contains a calculation to six digits of the number ${ \approx } 1 / 9 . 2 8 9 0 3$ that later became known as “Halphen’s constant” in connection with the rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ .]

P. C. Hansen (1998), Rank-Deficient and Discrete Ill-Posed Problems: Numerical Aspects of Linear Inversion, SIAM. [A leading monograph on the treatment of rank-deficient or ill-posed matrix problems.]

G. H. Hardy (1991), Divergent Series, revised ed., Editions Jacques Gabay. [Hardy’s ´ marvelous posthumous volume on the mathematics of divergent series, first published in 1949.]

J. F. Hart et al. (1968), Computer Approximations, Wiley. [A classic compendium on computer evaluation of special functions, containing 150 pages of explicit coefficients of rational approximations.]

E. Hayashi, L. N. Trefethen and M. H. Gutknecht (1990), The CF table, Constr. Approx. 6, 195–223. [The most systematic and detailed treatment of the problem of rational CF approximation of a function $f$ on the unit disk, including cases where $f$ is just in the Wiener class or continuous on the unit circle.]

G. Heinig and K. Rost (1984), Algebraic Methods for Toeplitz-like Matrices and Operators, Birkh¨auser. [Analyzes rank properties of Toeplitz and Hankel matrices related to the robust Pad´e algorithms of Chapter 27.]

G. Helmberg and P. Wagner (1997), Manipulating Gibbs’ phenomenon for Fourier interpolation, J. Approx. Th. 89, 308–320. [Analyzes the overshoot in various versions of the Gibbs phenomenon for trigonometric interpolation.]

P. Henrici (1974), Applied and Computational Complex Analysis, Vol. 1, Wiley. [First of three extensive and highly readable volumes of applied complex analysis, full of details that are hard to find elsewhere.]

C. Hermite (1878), Sur la formule d’interpolation de Lagrange, J. Reine Angew. Math. 84, 70–79. [Application of what became known as the Hermite integral formula for polynomial interpolation, which had earlier been given by Cauchy, to problems of interpolation with confluent data points.]

J. S. Hestaven, S. Gottlieb and D. Gottlieb (2007), Spectral Methods for Time-Dependent Problems, Cambridge U. Press. [Well-known textbook on spectral methods.]

E. Hewitt and R. E. Hewitt (1979), The Gibbs–Wilbraham phenomenon: An episode in Fourier analysis, Arch. Hist. Exact Sci. 21, 129–160. [Discussion of the complex and not always pretty history of attempts to analyze the Gibbs phenomenon.]

N. J. Higham (2004), The numerical stability of barycentric Lagrange interpolation, IMA J. Numer. Anal. 24, 547–556. [Proves that barycentric interpolation in Chebyshev points is numerically stable, following earlier work of Rack & Reimer 1982.]

N. J. Higham (2008), Functions of Matrices: Theory and Computation, SIAM. [The definitive treatment of the problem of computing functions of matrices as of 2008. Many of the algorithms have connections with polynomial or rational approximation.]

N. J. Higham (2009), The scaling and squaring method for the matrix exponential revisited, SIAM Rev. 51, 747–764. [Careful analysis of the MATLAB method of evaluating $e ^ { A }$ leads to several improvements in the algorithm and the recommendation to use the Pad´e approximant of type (13, 13).]

N. J. Higham and A. H. Al-Mohy (2010), Computing matrix functions, Acta Numer. 19, 159–208. [Survey includes an appendix comparing Pad´e and Taylor approximants for computing the exponential of a matrix.]

E. Hille (1973), Analytic Function Theory, 2 vols., 2nd ed., Chelsea. [Major work first published in 1959 and 1962.]

M. Hochbruck and A. Ostermann (2010), Exponential integrators, Acta Numer. 19, 209–286. [Survey of exponential integrators for the fast numerical solution of stiff ODEs and PDEs.]

G. Hornecker (1956), D´etermination des meilleures approximations rationnelles (au sens de Tchebichef) de fonctions r´eelles d’une variable sur un segment fini et des bornes d’erreur correspondantes, Compt. Rend. Acad. Sci. 249, 2265–2267. [Possibly the first proposal of a kind of Chebyshev–Pad´e approximation for intervals.]

J. P. Imhof (1963), On the method for numerical integration of Clenshaw and Curtis, Numer. Math. 5, 138–141. [Shows that the Clenshaw–Curtis quadrature weights are positive.]

A. Iserles (2011), A fast and simple algorithm for the computation of Legendre coefficients, Numer. Math. 117, 529–553. [A fast algorithm based on a numerical contour integral over an ellipse in the complex plane.]

D. Jackson (1911), Uber die Genauigkeit der Ann¨aherung stetiger Funktionen d ¨ urch ganze rationale Funktionen gegebenen Grades und trigonometrische Summen gegebener Ordnung, dissertation, G¨ottingen. [Jackson’s PhD thesis under Landau in G¨ottingen, which together with Bernstein’s work at the same time (1912b) established many of the fundamental results of approximation theory. Despite the German, Jackson was an American from Massachusetts, like me—Harvard Class of 1908.]

D. Jackson (1913), On the accuracy of trigonometric interpolation, Trans. Amer. Math.

Soc. 14, 453–461. [In the final paragraph of this paper, polynomial interpolation in Chebyshev points (2.2) is considered, possibly for the first time in the literature.]

C. G. J. Jacobi (1825), Disquisitiones Analyticae de Fractionibus Simplicibus, dissertation, Berlin. [In his discussion of partial fractions Jacobi effectively states the “first form” of the barycentric interpolation formula.]

C. G. J. Jacobi (1826), Uber Gauss’ neue Methode, die Werthe der Integrale ¨ n¨aherungsweise zu finden, J. Reine Angew. Math. 1, 301–308. [This paper first invents the subject of orthogonal polynomials and then shows that Gauss quadrature can be derived in this framework.]

C. G. J. Jacobi (1846), Uber die Darstellung einer Reihe gegebener Werthe durch ein ¨ e gebrochene rationale Function, J. Reine Angew. Math. 30, 127–156. [Jacobi’s major work on rational interpolation.]

R. Jentzsch (1914), Untersuchungen zur Theorie der Folgen analytischer Funktionen, dissertation, Berlin. [Proves that every point on the circle of convergence of a power series is the limit of zeros of its partial sums. Jentzsch was also a noted poet and was killed at age 27 in World War I.]

D. C. Joyce (1971), Survey of extrapolation processes in numerical analysis, SIAM Rev. 13, 435–490. [Scholarly review of a wide range of material.]

A.-K. Kassam and L. N. Trefethen (2005), Fourth-order time-stepping for stiff PDEs, SIAM J. Sci. Comput. 26, 1214–1233. [Application of exponential integrator formulas to efficient numerical solution of stiff PDEs.]

T. A. Kilgore (1978), A characterization of the Lagrange interpolating projection with minimal Tchebycheff norm, J. Approx. Th. 24, 273–288. [Together with de Boor & Pinkus 1978, one of the papers solving the theoretical problem of optimal interpolation.]

P. Kirchberger (1902), Ueber Tchebychefsche Ann¨aherungsmethoden, PhD thesis, G¨ottingen. [Kirchberger’s PhD thesis under Hilbert contains apparently the first full statement and proof of the equioscillation theorem.]

P. Kirchberger (1903), Uber Tchebychefsche Ann¨aherungsmethoden, ¨ Math. Ann. 57, 509–540. [Extract from his PhD thesis the year before, focusing on multivariable extensions but without the equioscillation theorem.]

A. N. Kolmogorov (1948), A remark on the polynomials of P. L. Chebyshev deviating the least from a given function (Russian), Uspehi Mat. Nauk 3, 216–221. [Criterion for best complex approximations.]

D. Kosloff and H. Tal-Ezer (1993), A modified Chebyshev pseudospectral method with an $O ( N ^ { - 1 } )$ time step restriction, J. Comput. Phys. 104, 457–469. [Introduces a change of variables as a basis for nonpolynomial spectral methods.]

A. B. J. Kuijlaars (2006), Convergence analysis of Krylov subspace iterations with methods from potential theory, SIAM Rev. 48, 3–40. [Analyzes the connection between potential theory and the roots of polynomial approximants implicitly constructed by Krylov iterations such as the conjugate gradient and Lanczos iterations.]

J. L. Lagrange (1795), Le¸cons ´el´ementaires sur les Math´ematiques, Le¸con V., J. de l’Ecole polytechnique, ´ Tome II, Cahier 8, Paris, pp. 274–278. [Contains what became known as the Lagrange interpolation formula, published earlier by Waring 1779 and Euler 1783.]

B. Lam (1972), Some Exact and Asymptotic Results for Best Uniform Approximation, PhD thesis, U. of Tasmania. [A precursor to the Carath´eodory–Fej´er method.]

E. Landau (1913), Absch¨atzung der Koeffizientensumme einer Potenzreihe, Archiv Math.

Phys. 21, 42–50 and 250–255. [Investigates the norm of the degree $n$ Taylor projection for functions analytic in the unit disk, now known as the Landau constant, showing it is asymptotic to $\pi ^ { - 1 } \log n$ as $n \to \infty$ .]

H. Lebesgue (1898), Sur l’approximation des fonctions, Bull. Sci. Math. 22, 278–287. [In Lebesgue’s first published paper, he proves the Weierstrass approximation theorem by approximating $| x |$ by polynomials and noting that any continuous function can be approximated by piecewise linear functions.]

A. L. Levin and E. B. Saff (2006), Potential theoretic tools in polynomial and rational approximation, in J.-D. Fournier et al., eds., Harmonic Analysis and Rational Approximation, Lect. Notes Control Inf. Sci. 326, Springer, pp. 71–94. [Survey article by two of the experts.]

R.-C. Li (2004), Near optimality of Chebyshev interpolation for elementary function computations, IEEE Trans. Computers 53, 678–687. [Shows that although Lebesgue constants for Chebyshev points grow logarithmically as $n \to \infty$ , for many classes of functions of interest the interpolants come within a factor of 2 of optimality.]

E. L. Lindman (1975), “Free-space” boundary conditions for the time-dependent wave equation, J. Comput. Phys. 18, 66–78. [Absorbing boundary conditions based on Pad´e approximation of a square root function, later developed further by Engquist & Majda 1977].

G. G. Lorentz (1986), Approximation of Functions, 2nd ed., Chelsea. [A readable treatment including good summaries of the Jackson theorems for polynomial and trigonometric approximation, first published in 1966.]

K. N. Lungu (1971), Best approximations by rational functions, Math. Notes 10, 431– 433. [Shows that the best rational approximations to a real function on an interval may be complex and hence also nonunique, with examples as simple as type $( 1 , 1 )$ approximation of $| x |$ on $[ - 1 , 1 ]$ .]

H. J. Maehly (1963), Methods for fitting rational approximations, Parts II and III, $J$ . ACM 10, 257–277. [Posthumous completion by Ch. Witzgall of a 1957 publication by Maehly on practical numerical methods of rational approximation, including a linearized form of Chebyshev–Pad´e approximation.]

H. J. Maehly and Ch. Witzgall (1960), Tschebyscheff-Approximationen in kleinen Intervallen. II. Stetikeitss¨atze f¨ur gebrochen rationale Approximationen, Numer. Math. 2, 293–307. [Investigates well-posedness of the Cauchy interpolation problem and asymptotics of best approximations on small intervals.]

A. P. Magnus (1985), CFGT determination of Varga’s constant “1/9”, unpublished manuscript. [First identification of the exact value of Halphen’s constant $C = 9 . 2 8 9 0 3 \dots$ for the optimal rate of convergence $O ( C ^ { - n } )$ of best type $( n , n )$ approximations to $e ^ { x }$ on $( - \infty , 0 ]$ , later proved correct by Gonchar $\&$ Rakhmanov 1989.]

A. P. Magnus (1994), Asymptotics and super asymptotics for best rational approximation error norms to the exponential function (the “1/9” problem) by the Carath´eodory–Fej´er method, in A. Cuyt et al., eds., Nonlinear Methods and Rational Approximation II, Kluwer, 1994, pp. 173–185. [Sharper conjectures on the “1/9 problem,” later proved valid by Aptekarev.]

A. P. Magnus and J. Meinguet (2000), The elliptic functions and integrals of the “1/9” problem, Numer. Alg. 24, 117–139. [Summary of work initiated by Magnus relating potential theory, elliptic functions, and the “1/9” problem.]

J. Marcinkiewicz (1936–37), Quelques remarques sur l’interpolation, Acta Sci. Math. (Szeged) 8, 127–30. [In contrast to the result of Faber 1914, shows that for any fixed continuous function $f$ there is an array of interpolation nodes that leads to convergence as $n \to \infty$ .]

A. I. Markushevich (1985), Theory of Functions of a Complex Variable, 2nd ed., 3 vols., Chelsea. [A highly readable treatise on complex variables first published in 1965, including chapters on Laurent series, polynomial interpolation, harmonic functions, and rational approximation.]   
J. C. Mason and D. C. Handscomb (2003), Chebyshev Polynomials, Chapman and Hall/CRC. [An extensive treatment of four varieties of Chebyshev polynomials and their applications.]   
G. Mastroianni and M. G. Russo (2010), Some new results on Lagrange interpolation for bounded variation functions, J. Approx. Th. 162, 1417–1428. [A collection of bounds in $L ^ { p }$ norms for both $p < \infty$ and $p = \infty$ .]   
G. Mastroianni and J. Szabados (1995), Jackson order of approximation by Lagrange interpolation. II, Acta Math. Acad. Sci. Hungar. 69, 73–82. [Corollary 2 bounds the rate of convergence of Chebyshev interpolants for functions whose $k { \mathrm { t h } }$ derivative has bounded variation.]   
J. H. McCabe and G. M. Phillips (1973), On a certain class of Lebesgue constants, BIT 13, 434–442. [Shows that the Lebesgue constant for polynomial interpolation in $n + 1$ Chebyshev points of the second kind is bounded by that of $_ n$ Chebyshev points of the first kind. The same result had been found earlier by Ehlich & Zeller 1966.]   
J. H. McClellan and T. W. Parks (2005), A personal history of the Parks–McClellan algorithm, IEEE Sign. Proc. Mag. 82, 82–86. [The story of the development of the celebrated filter design algorithm published in Parks & McClellan 1972.]   
G. Meinardus (1967), Approximation of Functions: Theory and Numerical Methods, Springer. [Classic approximation theory monograph.]   
C. M´eray (1884), Observations sur la l´egitimit´e de l’interpolation, Annal. Scient. de l’Ecole Normale Sup´erieure ´ 3, 165–176. [Discussion of the possibility of nonconvergence of polynomial interpolants 17 years before Runge, though without so striking an example or conclusion. M´eray uses just the right technique, the Hermite integral formula, which he correctly attributes to Cauchy.]   
C. M´eray (1896), Nouveaux exemples d’interpolations illusoires, Bull. Sci. Math. 20, 266–270. [Continuation of M´eray 1884 with more examples.]   
S. N. Mergelyan (1951), On the representation of functions by series of polynomials on closed sets (Russian), Dokl. Akad. Nauk SSSR (N. S.) 78, 405–408. Translation: Translations Amer. Math. Soc. 3 (1962), 287–293. [Famous theorem asserting that a function continuous on a compact set in the complex plane whose complement is connected, and analytic in the interior, can be uniformly approximated by polynomials.]   
H. N. Mhaskar and D. V. Pai (2000), Fundamentals of Approximation Theory, CRC/Narosa. [Extensive treatment of many topics, especially in linear approximation.] G. Mittag-Leffler (1900), Sur la repr´esentation analytique des fonctions d’une variable r´eelle, Rend. Circ. Mat. Palermo 14, 217–224. [Contains a long footnote by Phragm´en explaining how the Weierstrass approximation theorem follows from the work of Runge.] C. Moler and C. Van Loan (2003), Nineteen dubious ways to compute the exponential of a matrix, twenty-five years later, SIAM Rev. 45, 3–49. [Expanded reprinting of 1978 paper summarizing methods for computing $\exp ( A )$ , the best method being related to Pad´e approximation.]   
R. de Montessus de Ballore (1902), Sur les fractions continues alg´ebriques, Bull. Soc.

Math. France 30, 28–36. [Shows that type $( m , n )$ Pad´e approximants to meromorphic functions converge pointwise as $m \to \infty$ in a disk about $z = 0$ with exactly $_ n$ poles.]

M. Mori and M. Sugihara (2001), The double-exponential transformation in numerical analysis, J. Comput. Appl. Math. 127, 287–296. [Survey of the quadrature algorithm introduced by Takahasi & Mori 1974.]

J.-M. Muller (2006), Elementary Functions: Algorithms and Implementation, 2nd ed., Birkh¨auser. [A text on implementation of elementary functions on computers, including a chapter on the Remez algorithm.]

Y. Nakatsukasa, Z. Bai and F. Gygi (2010), Optimizing Halley’s iteration for computing the matrix polar decomposition, SIAM J. Matrix Anal. Appl. 31, 2700–2720. [Proposal of an algorithm based on a rational function of high degree generated by iteration of a simple equiripple approximation.]

Y. Nakatsukasa, O. S\`ete and L. N. Trefethen (2018), The AAA algorithm for rational approximation, SIAM J. Sci. Comput. 40, A1494–A1522. [Introduction of an adaptive method for rational approximation exploiting barycentric representations.]

I. P. Natanson (1965), Constructive Theory of Functions, 3 vols., Frederick Ungar. [This major work by a scholar in Leningrad gives equal emphasis to algebraic and trigonometric approximation.]

D. J. Newman (1964), Rational approximation to $| x |$ , Mich. Math. J. 11, 11–14. [Shows that whereas polynomial approximants to $| x |$ on $[ - 1 , 1 ]$ converge at the rate $O ( n ^ { - 1 } )$ , for rational approximants the rate is $O ( \exp ( - C { \sqrt { n } } ) )$ ).]

D. J. Newman (1974), Rational approximation to $e ^ { - x }$ , $J$ . Approx. Th. 10, 301–303. [Shows by a lower bound $1 2 8 0 ^ { - n }$ that type $( n , n )$ rational approximants to $e ^ { x }$ on $( - \infty , 0 ]$ can converge no faster than geometrically as $n \to \infty$ in the supremum norm.]

J. Nuttall (1970), The convergence of Pad´e approximants of meromorphic functions, $J$ . Math. Anal. Appl. 31, 147–153. [Shows that type $( n , n )$ Pad´e approximants to meromorphic functions converge in measure as $n \to \infty$ , though not pointwise.]

H. O’Hara and F. J. Smith (1968), Error estimation in the Clenshaw–Curtis quadrature formula, Comput. J. 11, 213–219. [Early paper arguing that Clenshaw–Curtis and Gauss quadrature have comparable accuracy in practice.]

A. V. Oppenheim, R. W. Schafer and J. R. Buck (1999), Discrete-time Signal Processing, Prentice-Hall. [A standard textbook on the subject, which is tightly connected with polynomial and rational approximation.]

S. A. Orszag (1971a), Galerkin approximations to flows within slabs, spheres, and cylinders, Phys. Rev. Lett. 26, 1100–1103. [Orszag’s first publication on Chebyshev spectral methods.]

S. A. Orszag (1971b), Accurate solution of the Orr–Sommerfeld stability equation, J. Fluid Mech. 50, 689–703. [The most influential of Orszag’s early papers on Chebyshev spectral methods.]

R. Pachon´ (2010), Algorithms for Polynomial and Rational Approximation in the Complex Domain, DPhil thesis, U. of Oxford. [Includes chapters on rational best approximants, interpolants, and Chebyshev–Pad´e approximants and their application to exploration of functions in the complex plane.]

R. Pachon, P. Gonnet and J. Van Deun ´ (2012), Fast and stable rational interpolation in roots of unity and Chebyshev points, SIAM J. Numer. Anal. 50, 1713–1734. [Linear algebra formulation of the rational interpolation problem in a manner closely suited to computation.]

R. Pachon, R. B. Platte and L. N. Trefethen ´ (2010), Piecewise-smooth chebfuns, IMA J. Numer. Anal. 30, 898–916. [Generalization of Chebfun from single to multiple polynomial pieces, including edge detection algorithm to determine breakpoints.]

H. Pad´e (1892), Sur la repr´esentation approch´ee d’une fonction par des fractions rationelles, Annales Sci. de l’Ecole Norm. Sup. ´ 9 (suppl´ement), 3–93. [The first of many publications by Pad´e on the subject that became known as Pad´e approximation, with discussion of defect and block structure including a number of explicit examples.]

T. W. Parks and J. H. McClellan (1972), Chebyshev approximation for nonrecursive digital filters with linear phase, IEEE Trans. Circuit Theory CT-19, 189–194. [Proposes what became known as the Parks–McClellan algorithm for digital filter design, based on a barycentric formulation of the Remez algorithm for best approximation by trigonometric polynomials.]

B. N. Parlett and C. Reinsch (1969), Handbook series linear algebra: Balancing a matrix for calculation of eigenvalues and eigenvectors, Numer. Math. 13, 293–304. [Introduction of the technique of balancing a matrix by a diagonal similarity transformation that is crucial to the success of the QR algorithm.]

S. Paszkowski (1975), Numerical Applications of Chebyshev Polynomials and Series (Polish), PWN, Warsaw. [This monograph was later translated into Russian, but not English.]

K. Pearson (1920), On the Construction of Tables and on Interpolation I. Uni-variate Tables, Cambridge U. Press. [Contains as an appendix a fascinating annotated bibliography of 50 early contributions to interpolation. Pearson’s annotations are not always as polite as my own, with comments like “Not very adequate” and “A useful, but somewhat disappointing book.”]

O. Perron (1929), Die Lehre von den Kettenbr¨uchen, 2nd ed., Teubner. [This classic monograph on continued fractions, first published in 1913, was perhaps the first to identify the problem of spurious poles or Froissart doublets in Pad´e approximation. At the end of §78 a function is constructed whose type $( m , 1 )$ Pad´e approximants have poles appearing infinitely often on a dense set of points in the complex plane.]

R. Piessens (1974), Algorithm 473: Computation of Legendre series coefficients [C6], Comm. ACM 17, 25. $[ O ( n ^ { 2 } )$ algorithm for converting from Chebyshev to Legendre expansions.]

A. Pinkus (2000), Weierstrass and approximation theory, J. Approx. Th. 107, 1–66. [Detailed discussion of Weierstrass’s nowhere-differentiable function and of the Weierstrass approximation theorem and its many proofs and generalizations.]

R. B. Platte, L. N. Trefethen and A. B. J. Kuijlaars (2011), Impossibility of fast stable approximation of analytic functions from equispaced samples, SIAM Rev. 53, 308–318. [Shows that any exponentially convergent scheme for approximating analytic functions from equispaced samples in an interval must be exponentially ill-conditioned as $n \to \infty$ ; thus no approximation scheme can eliminate the Gibbs and Runge phenomena completely.]

G. Polya ´ (1933), Uber die Konvergenz von Quadraturverfahren, ¨ Math. Z. 37, 264–286. [Proves that a family of interpolating quadrature rules converges for all continuous integrands if and only if the sums of the absolute values of the weights are uniformly bounded; proves further that Newton–Cotes quadrature approximations do not always converge as $n \to \infty$ , even if the integrand is analytic.]

Ch. Pommerenke (1973), Pad´e approximants and convergence in capacity, J. Math. Anal. Appl., 41, 775–780. [Sharpens Nuttall’s result on convergence of Pad´e approximants in measure to convergence in capacity.]

J. V. Poncelet (1835), Sur la valeur approch´ee lin´eaire et rationelle des radicaux de la forme ${ \sqrt { a ^ { 2 } + b ^ { 2 } } } , { \sqrt { a ^ { 2 } - b ^ { 2 } } }$ etc., J. Reine Angew. Math. 13, 277–291. [Perhaps the very first discussion of minimax approximation.]

D. Potts, G. Steidl and M. Tasche (1998), Fast algorithms for discrete polynomial transforms, Math. Comp. 67, 1577–1590. [Algorithms for converting between Chebyshev and Legendre expansions.]

M. J. D. Powell (1981), Approximation Theory and Methods, Cambridge U. Press. [Approximation theory text with a computational emphasis, particularly strong on the Remez algorithm and on splines.]

H. A. Priestley (2003), Introduction to Complex Analysis, 2nd ed., Oxford U. Press. [Well-known introductory complex analysis textbook first published in 1985.]

I. E. Pritsker and R. S. Varga (1997), The Szeg˝o curve, zero distribution and weighted approximation, Trans. Amer. Math. Soc. 349, 4085–4105. [Analysis of the Szeg˝o curve using methods of potential theory.]

P. Rabinowitz (1969), Rough and ready error estimates in Gaussian integration of analytic functions, Comm. ACM 12, 268–270. [Derives tight bounds on accuracy of Gaussian quadrature by simple arguments.]

H.-J. Rack and M. Reimer (1982), The numerical stability of evaluation schemes for polynomials based on the Lagrange interpolation form, BIT 22, 101–107. [Proof of stability for barycentric polynomial interpolation in well-distributed point sets, later developed further by Higham 2004.]

T. Ransford (1995), Potential Theory in the Complex Plane, Cambridge U. Press. [Perhaps the only book fully devoted to this subject.]

T. Ransford (2010), Computation of logarithmic capacity, Comput. Meth. Funct. Th. 10, 555–578. [An algorithm for computing capacity of a set in the complex plane, with examples.]

E. Remes (1934a), Sur un proc´ed´e convergent d’approximations successives pour d´eterminer les polynˆomes d’approximation, Compt. Rend. Acad. Sci. 198, 2063–2065. [One of the original papers presenting the Remez algorithm.]

E. Remes (1934b), Sur le calcul effectif des polynˆomes d’approximation de Tchebichef, Compt. Rend. Acad. Sci. 199, 337–340. [The other original paper presenting the Remez algorithm.]

E. Ya. Remez (1951), On approximations in the complex domain (Russian), Dokl. Akad. Nauk SSSR 77, 965–968. [Characterizes best approximations on complex domains.]

E. Ya. Remez (1957), General computational methods of Tchebycheff approximation, Atomic Energy Commission Translation 4491, Kiev, pp. 1–85. [Remez’s summary of computational methods for best approximation.]

J. R. Rice (1969), The Approximation of Functions, Addison-Wesley. [Two volumes, the first linear and the second nonlinear.]

L. F. Richardson (1927), The deferred approach to the limit. I—single lattice. Phil. Trans. Roy. Soc. A 226, 299–349. [Systematic discussion of Richardson extrapolation, emphasizing discretizations with $O ( h ^ { 2 } )$ error behavior.]

M. Richardson and L. N. Trefethen (2011), A sinc function analogue of Chebfun, SIAM J. Sci. Comput. 33, 2519–2535. [Presents a “Sincfun” software analogue of Chebfun for dealing with functions with endpoint singularities via variable transformation and sinc function interpolants.]

F. Riesz (1918), Uber lineare Funktionalgleichungen, ¨ Acta Math. 41, 71–98. [First statement of the general existence result for best approximation from finite-dimensional linear spaces.]

M. Riesz (1916), Uber einen Satz des Herrn Serge Bernstein, ¨ Acta Math. 40, 43–47. [Gives a new proof of a Bernstein inequality based on the barycentric formula for Chebyshev points, in the process deriving the barycentric coefficients ${ \scriptstyle { \frac { 1 } { 2 } } } , - 1 , 1 , - 1 , \ldots$ half a century before Salzer 1972.]

T. J. Rivlin (1981), An Introduction to the Approximation of Functions, Dover. [Appealing short textbook originally published in 1969.]

T. J. Rivlin (1990), Chebyshev Polynomials: From Approximation Theory to Algebra and Number Theory, 2nd ed., Wiley. [Classic book on Chebyshev polynomials and applications, with first edition in 1974.]

J. D. Roberts (1980), Linear model reduction and solution of the algebraic Riccati equation by use of the sign function, Internat. J. Control 32, 677–687. [This article connecting rational functions with the sign function was written in 1971 as Technical Report CUED/B-Control/TR13 of the Cambridge University Engineering Dept.]

W. Rudin (1976), Principles of Mathematical Analysis, 3rd ed., McGraw-Hill. [Influential textbook first published in 1953.]

P. O. Runck (1962), Uber Konvergenzfragen bei Polynominterpolation mit ¨aqui ¨ distanten Knoten. II, J. Reine Angew. Math. 210, 175–204. [Analyzes the Gibbs overshoot for two varieties of polynomial interpolation of a step function.]

C. Runge (1885a), Zur Theorie der eindeutigen analytischen Functionen, Acta Math. 6, 229–244. [Publication of Runge’s theorem: a function analytic on a compact set in the complex plane whose complement is connected can be uniformly approximated by polynomials. This was later generalized by Mergelyan.]

C. Runge (1885b), Uber die Darstellung willk¨urlicher Functionen, ¨ Acta Math. 7, 387–392. [Shows that a continuous function on a finite interval can be uniformly approximated by rational functions. It was later noted by Phragm´en and Mittag-Leffler that this and the previous paper by Runge together imply the Weierstrass approximation theorem.]

C. Runge (1901), Uber empirische Funktionen und die Interpolation zwischen ¨ ¨aquidistanten Ordinaten, Z. Math. Phys. 46, 224–243. [M´eray had pointed out that polynomial interpolants might fail to converge, but it was this paper that focused on equispaced sample points, showed that divergence can take place even in the interval of interpolation, and identified the “Runge region” where analyticity is required for convergence.]

A. Ruttan (1981), The length of the alternation set as a factor in determining when a best real rational approximation is also a best complex rational approximation, J. Approx. Th. 31, 230–243. [Shows that complex best approximations are always better than real ones in the strict lower-right triangle of a square block of the Walsh table.]

A. Ruttan and R. S. Varga (1989), A unified theory for real vs. complex rational Chebyshev approximation on an interval, Trans. Amer. Math. Soc. 312, 681–697. [Shows that type $( m , m + 2 )$ complex rational approximants to real functions can be up to 3 times as accurate as real ones.]

E. B. Saff (1972), An extension of Montessus de Ballore’s theorem on the convergence of interpolating rational functions, J. Approx. Th. 6, 63–67. [Generalizes the de Montessus de Ballore theorem from Pad´e to multipoint Pad´e approximation.]

E. B. Saff and A. D. Snider (2003), Fundamentals of Complex Analysis with Applications to Engineering, Science, and Mathematics, 3rd ed., Prentice-Hall. [Widely used introductory complex analysis textbook.]

E. B. Saff and V. Totik (1997), Logarithmic Potentials with External Fields, Springer. [Presentation of connections between potential theory and rational approximation.] E. B. Saff and R. S. Varga (1978a), Nonuniqueness of best complex rational approximations to real functions on real intervals, J. Approx. Th. 23, 78–85. [Rediscovery of results of Lungu 1971.]   
E. B. Saff and R. S. Varga (1978b), On the zeros and poles of Pad´e approximants to $e ^ { z }$ . III, Numer. Math. 30, 241–266. [Analysis of the curves in the complex plane along which poles and zeros of these approximants cluster.]   
T. W. Sag and G. Szekeres (1964), Numerical evaluation of high-dimensional integrals, Math. Comp. 18, 245–253. [Introduction of changes of variables that can speed up Gauss and other quadrature formulas, even in one dimension.]   
H. E. Salzer (1955), A simple method for summing certain slowly convergent series, $J$ . Math. Phys. 33, 356–359. [“Salzer’s method” for acceleration of convergence, based on interpreting a sequence of values as samples of a function $f ( x )$ at $x _ { n } = n ^ { - 1 }$ .]   
H. E. Salzer (1972), Lagrangian interpolation at the Chebyshev points $x _ { n , \nu } = \cos ( \nu \pi / n )$ , $\nu = 0 ( 1 ) n$ ; some unnoted advantages, Computer J. 15, 156–159. [Barycentric formula for polynomial interpolation in Chebyshev points.]   
H. E. Salzer (1981), Rational interpolation using incomplete barycentric forms, $Z$ . Angew. Math. Mech. 61, 161–164. [One of the first publications to propose the use of rational interpolants defined by barycentric formulas.]   
T. Schmelzer and L. N. Trefethen (2007), Evaluating matrix functions for exponential integrators via Carath´eodory–Fej´er approximation and contour integrals, Elect. Trans. Numer. Anal. 29, 1–18. [Fast methods based on rational approximations for evaluating the $\varphi$ functions used by exponential integrators for solving stiff ODEs and PDEs.] J. R. Schmidt (1941), On the numerical solution of linear simultaneous equations by an iterative method, Philos. Mag. 32, 369–383. [Proposal of what became known as the epsilon or eta algorithm some years before Shanks 1955, Wynn 1956, and Bauer 1959.] C. Schneider and W. Werner (1986), Some new aspects of rational interpolation, Math. Comp. 47, 285–299. [Extension of barycentric formulas to rational interpolation.] A. Schonhage ¨ (1961), Fehlerfortpflanzung bei Interpolation, Numer. Math. 3, 62–71. [Independent rediscovery of results close to those of Turetskii 1940 concerning Lebesgue constants for equispaced points.]   
A. Schonhage ¨ (1971), Approximationstheorie, de Gruyter. [This monograph was unfortunately not translated into English.]   
A. Schonhage ¨ (1973), Zur rationalen Approximierbarkeit von $e ^ { - x }$ ¨uber $[ 0 , \infty )$ , J. Approx. Th. 7, 395–398. [Proves that in maximum-norm approximation of $e ^ { x }$ on $( - \infty , 0 ]$ by inversepolynomials $1 / p _ { n } ( x )$ , the optimal rate is $O ( 3 ^ { - n } )$ .]   
I. Schur (1918), Uber Potenzreihen, die im Innern des Einheitskreises besch ¨ r¨ankt sind, J. Reine Angew. Math. 148, 122–145. [Solution of the problem of Carath´eodory and Fej´er via the eigenvalue analysis of a Hankel matrix of Taylor coefficients.]   
D. Shanks (1955), Non-linear transformations of divergent and slowly convergent sequences, J. Math. Phys. 34, 1–42. [Introduction of Shanks’ method for convergence acceleration by Pad´e approximation, closely related to the epsilon algorithm of Wynn 1956.] J. Shen, T. Tang and L.-L. Wang (2011), Spectral Methods: Algorithms, Analysis and Applications, Springer. [Systematic presentation of spectral methods including convergence theory.]

B. Shiffman and S. Zelditch (2003), Equilibrium distribution of zeros of random polynomials, Int. Math. Res. Not., no. 1. [Shows that polynomials given by expansions in orthogonal polynomials with random coefficients have roots clustering near the support of the orthogonality measure.]

A. Sidi, Practical Extrapolation Methods (2003), Cambridge U. Press. [Extensive treatment of methods for acceleration of convergence.]

G. A. Sitton, C. S. Burrus, J. W. Fox and S. Treitel (2003), Factoring very-highdegree polynomials, IEEE Signal Proc. Mag. 20, 27–42. [Discussion of rootfinding for polynomials of degree up to one million by the Lindsey–Fox algorithm.]

V. I. Smirnov and N. A. Lebedev (1968), Functions of a Complex Variable: Constructive Theory, MIT Press. [Major survey of problems of polynomial and rational approximation in the complex plane.]

F. Smithies (1997), Cauchy and the Creation of Complex Function Theory, Cambridge U. Press. [Detailed account of Cauchy’s almost single-handed creation of this field from 1814 to 1831.]

M. A. Snyder (1966), Chebyshev Methods in Numerical Approximation, Prentice-Hall. [An appealing short book emphasizing rational as well as polynomial approximations.]

W. Specht (1957), Die Lage der Nullstellen eines Polynoms. III, Math. Nachr. 16, 369– 389. [Development of comrade matrices, whose eigenvalues are roots of polynomials expressed in bases of orthogonal polynomials.]

W. Specht (1960), Die Lage der Nullstellen eines Polynoms. IV, Math. Nachr. 21, 201– 222. [The final page considers colleague matrices, the special case of comrade matrices for Chebyshev polynomials. These ideas were developed independently by Good 1961.]

H. Stahl (1993), Best uniform rational approximation of $| x |$ on $[ - 1 , 1 ]$ , Russian Acad. Sci. Sb. Math. 76, 461–487. [Proof of the conjecture of Varga, Ruttan, and Carpenter that best rational approximations to $| x |$ on $[ - 1 , 1 ]$ converge at the rate $\sim 8 \exp ( - \pi { \sqrt { n } } )$ .]

H. Stahl (1997), The convergence of Pad´e approximants to functions with branch points, J. Approx. Th. 91, 139–204. [Generalizes the Nuttall–Pommerenke theorem on convergence of type $( n , n )$ Pad´e approximants to the case of functions $f$ with branch points.]

H. Stahl (1998), Spurious poles in Pad´e approximation, J. Comput. Appl. Math. 99, 511–527. [Defines and analyzes what it means for a pole of a Pad´e approximant to be spurious.]

H. R. Stahl (2003), Best uniform rational approximation of $x ^ { \alpha }$ on [0, 1], Acta Math. 190, 241–306. [Generalization of the results of the paper above to approximation of $x ^ { \alpha }$ on $[ 0 , 1 ]$ , completing earlier investigations of Ganelius and Vyacheslavov.]

H. Stahl and T. Schmelzer (2009), An extension of the “1/9”-problem, J. Comput. Appl. Math. 233, 821–834. [Announcement of numerous extensions of the “9.28903” result of Gonchar & Rakhmanov 1989 for type $( n , n )$ best approximation of $e ^ { x }$ on $( - \infty , 0 ]$ , showing that the same rate of approximation applies on compact sets in the complex plane and on Hankel contours, and that “9.28903” is also achieved on $( - \infty , 0 ]$ in type $( n , n + k )$ approximation of $e ^ { x }$ or of related functions such as $\varphi$ functions for exponential integrators.]

K.-G. Steffens (2006), The History of Approximation Theory: From Euler to Bernstein, Birkh¨auser. [Discussion of many people and results, especially of the St. Petersburg school, by a student of Natanson.]

E. M. Stein and R. Shakarchi (2005), Real Analysis: Measure Theory, Integration, and Hilbert Spaces, Princeton U. Press. [A leading textbook.]

F. Stenger (1986), Explicit nearly optimal linear rational approximation with preassigned poles, Math. Comp. 47, 225–252. [Construction of rational approximants by a method related to sinc expansions.]

F. Stenger (1993), Numerical Methods Based on Sinc and Analytic Functions, Springer. [Comprehensive treatise by the leader in sinc function algorithms.]

F. Stenger (2010), Sinc Numerical Methods, CRC Press. [A handbook of sinc methods and their implementation in the author’s software package Sinc-Pack.]

T. J. Stieltjes (1884), Quelques recherches sur la th´eorie des quadratures dites m´ecaniques, Ann. Sci. Ecole Norm. Sup. ´ 1, 409–426. [Proves that Gauss quadrature converges for any Riemann integrable integrand.]

T. J. Stieltjes (1885), Sur les polynˆomes de Jacobi, Compt. Rend. Acad. Sci. 199, 620– 622. [Shows that the roots of $( x ^ { 2 } - 1 ) P _ { n - 1 } ^ { ( 1 , 1 ) } ( x )$ are Fekete points (minimal-energy points) in $[ - 1 , 1 ]$ .]

J. Szabados (1970), Rational approximation to analytic functions on an inner part of the domain of analyticity, in A. Talbot, ed., Approximation Theory, Academic Press, pp. 165– 177. [Shows that for some functions analytic in a Bernstein $\rho$ -ellipse, type $( n , n )$ rational best approximations are essentially no better than degree $n$ polynomial best approximations.]

G. Szego˝ (1924), Uber eine Eigenschaft der Exponentialreihe, ¨ Sitzungsber. Berl. Math. Ges. 23, 50–64. [Shows that as $n \to \infty$ , the zeros of the normalized partial sums $s _ { n } ( n z )$ of the Taylor series of $e ^ { z }$ approach the Szeg˝o curve in the complex $z$ -plane defined by $| z e ^ { 1 - z } | = 1$ and $| z | \le 1$ .]

G. Szego˝ (1985), Orthogonal Polynomials, American Mathematical Society. [A classic monograph by the master, including chapters on polynomial interpolation and quadrature, first published in 1939.]

E. Tadmor (1986), The exponential accuracy of Fourier and Chebyshev differencing methods, SIAM J. Numer. Anal. 23, 1–10. [Presents theorems on exponential accuracy of Chebyshev interpolants of analytic functions and their derivatives.]

T. Takagi (1924), On an algebraic problem related to an analytic theorem of Carath´eodory and Fej´er and on an allied theorem of Landau, Japan J. Math. 1, 83–91 and ibid., 2 (1925), 13–17. [Beginnings of the generalization of Carath´eodory & Fej´er 1911 and Schur 1918 to rational approximation.]

H. Takahasi and M. Mori (1971), Estimation of errors in the numerical quadrature of analytic functions, Applicable Anal. 1, 201–229. [Relates the accuracy of a quadrature formula to the accuracy of an associated rational function as an approximation to $\log ( ( z + 1 ) / ( z - 1 ) )$ on a contour enclosing $[ - 1 , 1 ]$ .]

H. Takahasi and M. Mori (1974), Double exponential formulas for numerical integration, Publ. RIMS, Kyoto U. 9, 721–741. [Introduction of the double exponential or tanh-sinh quadrature rule, in which Gauss quadrature is transformed by a change of variables to another formula that can handle endpoint singularities.]

A. Talbot (1976), The uniform approximation of polynomials by polynomials of lower degree, J. Approx. Th. 17, 254–279. [A precursor to the Carath´eodory–Fej´er method.]

F. D. Tappert (1977), The parabolic approximation method, in J. B. Keller and J. S. Papadakis, eds., Wave Propagation and Underwater Acoustics, Springer, pp. 224–287. [Describes techniques for one-way acoustic wave simulation in the ocean, based on polynomial and rational approximations of a pseudodifferential operator.]

R. Taylor and V. Totik (2010), Lebesgue constants for Leja points, IMA J. Numer.

Anal. 30, 462–486. [Proves that for general sets in the complex plane, the Lebesgue constants associated with Leja points grow subexponentially.]

W. J. Taylor (1945), Method of Lagrangian curvilinear interpolation, J. Res. Nat. Bur. Stand. 35, 151–155. [The first use of the barycentric interpolation formula, for equidistant points only and without the term “barycentric,” which was introduced by Dupuy 1948.]

T. W. Tee and L. N. Trefethen (2006), A rational spectral collocation method with adaptively transformed Chebyshev grid points, SIAM J. Sci. Comput. 28, 1798– 1811. [Numerical solution of differential equations with highly nonuniform solutions using Chebyshev–Pad´e approximation, conformal maps, and spectral methods based on rational barycentric interpolants, as advocated by Berrut and coauthors.]

H. Tietze (1917), Eine Bemerkung zur Interpolation, Z. Angew. Math. Phys. 64, 74– 90. [Investigates the Lebesgue function for equidistant points, showing the local maxima decrease monotonically from the outside of the interval toward the middle.]

A. F. Timan (1951), A strengthening of Jackson’s theorem on the best approximation of continuous functions by polynomials on a finite interval of the real axis, Doklady Akad. Nauk SSSR 78, 17–20. [A theorem on polynomial approximation that recognizes the greater approximation power near the ends of the interval.]

A. F. Timan (1994), Theory of Approximation of Functions of a Real Variable, Dover. [First published in Russian in 1960.]

K.-C. Toh and L. N. Trefethen (1994), Pseudozeros of polynomials and pseudospectra of companion matrices, Numer. Math. 68, 403–425. [Analysis of stability of companion matrix eigenvalues as an algorithm for polynomial rootfinding, given a polynomial expressed by its coefficients in the monomial basis.]

L. Tonelli (1908), I polinomi d’approssimazione di Tschebychev, Annali di Mat. 15, 47–119. [Extension of results on real best approximation to the complex case.]

L. N. Trefethen (1983), Chebyshev approximation on the unit disk, in H. Werner et al., eds., Computational Aspects of Complex Analysis, D. Riedel, pp. 309–323. [An introduction to several varieties of CF approximation.]

L. N. Trefethen (1984), Square blocks and equioscillation in the Pad´e, Walsh, and CF tables, in P. R. Graves-Morris et al., eds., Rational Approximation and Interpolation, Lect. Notes in Math. 1105, Springer. [Shows that square block structure in all three tables of rational approximations arises from equioscillation-type characterizations involving the defect.]

L. N. Trefethen (2000), Spectral Methods in MATLAB, SIAM. [MATLAB-based textbook on spectral methods for ODEs and PDEs.]

L. N. Trefethen (2008), Is Gauss quadrature better than Clenshaw–Curtis?, SIAM Rev. 50, 67–87. [Shows by considering approximation properties in the complex plane that for most functions, the Clenshaw–Curtis and Gauss formulas have comparable accuracy.]

L. N. Trefethen (2010), Householder triangularization of a quasimatrix, IMA J. Numer. Anal. 30, 887–897. [Extends the Householder triangularization algorithm to quasimatrices, i.e., “matrices” whose columns are functions rather than vectors.]

L. N. Trefethen (2016), Inverse Yogiisms, Notices Amer. Math. Soc. 63, 1281–1285. [Discusses the phenomenon that mathematicians tend to say things that are literally true yet misleading, with Faber’s theorem of polynomial interpolation as an example.]

L. N. Trefethen and D. Bau, III (1997), Numerical Linear Algebra, SIAM. [A standard text, with a section “When vectors become continuous functions” at p. 52 that foreshadows Chebfun computation with quasimatrices.]

L. N. Trefethen, A. Birkisson and T. A. Driscoll ´ (2018), Exploring ODEs, SIAM. [Chebfun-based textbook.]

L. N. Trefethen and M. H. Gutknecht (1983a), Real vs. complex rational Chebyshev approximation on an interval, Trans. Amer. Math. Soc. 280, 555–561. [Shows that type $( m , n )$ complex rational approximations to a real function on an interval may be arbitrarily much better than real ones for $n \geq m + 3$ .]

L. N. Trefethen and M. H. Gutknecht (1983b), The Carath´eodory–Fej´er method for real rational approximation, SIAM J. Numer. Anal. 20, 420–436. [Introduction of real rational CF approximation, and first numerical computation of the constant 9.28903 . . . for minimax rational approximation of $e ^ { x }$ on $( - \infty , 0 ]$ .]

L. N. Trefethen and M. H. Gutknecht (1985), On convergence and degeneracy in rational Pad´e and Chebyshev approximation, SIAM J. Math. Anal. 16, 198–210. [Proves theorems to the effect that the Pad´e approximation operator is continuous, and Pad´e approximants are limits of best approximants on regions shrinking to a point, provided that the defect is 0.]

L. N. Trefethen and M. H. Gutknecht (1987), Pad´e, stable Pad´e, and Chebyshev– Pad´e approximation, in J. C. Mason and M. G. Cox, eds., Algorithms for Approximation, Clarendon Press, pp. 227–264. [Reduces the problem of Chebyshev–Pad´e approximation to the problem of stable Pad´e approximation, that is, Pad´e approximation with a constraint on location of poles.]

L. N. Trefethen and L. Halpern (1986), Well-posedness of one-way wave equations and absorbing boundary conditions, Math. Comp. 47, 421–435. [Shows that approximations from two diagonals of the Pad´e table must be used in these applications; polynomial and other approximations are ill-posed.]

L. N. Trefethen and J. A. C. Weideman (1991), Two results concerning polynomial interpolation in equally spaced points, J. Approx. Th. 65, 247–260. [Discussion of the size of Lebesgue constants and “6 points per wavelength” for polynomial interpolation in equispaced points.]

L. N. Trefethen and J. A. C. Weideman (2014), The exponentially convergent trapezoidal rule, SIAM Rev. 56, 385–458. [Survey of uses of the periodic trapezoidal rule and its variants in numerical analysis.]

L. N. Trefethen, J. A. C. Weideman and T. Schmelzer (2006), Talbot quadratures and rational approximations, BIT Numer. Math. 46, 653–670. [Shows how integrals approximated by the trapezoidal rule correspond to rational approximations in the complex plane, with particular attention to the approximation of $e ^ { x }$ on $( - \infty , 0 ]$ .]

A. H. Turetskii (1940), The bounding of polynomials prescribed at equally distributed points (Russian), Proc. Pedag. Inst. Vitebsk 3, 117–127. [Derivation of the $\sim 2 ^ { n } / e n \log n$ asymptotic size of Lebesgue constants for equispaced polynomial interpolation. This paper went largely unnoticed for fifty years and the main result was rediscovered by Sch¨onhage 1961.]

Ch.-J. de la Vall´ee Poussin (1908), Note sur l’approximation par un polynˆome d’une fonction dont la deriv´ee est \`a variation born´ee, Bull. Acad. Belg., 403–410. [Proof of the Weierstrass approximation theorem.]

Ch. de la Vall´ee Poussin (1910), Sur les polynˆomes d’approximation et la repr´esentation approch´ee d’un angle, Acad. Roy. de Belg., Bulletins de la Classe des Sci. 12. [Includes the de la Vall´ee Poussin lower bound on best approximation error.]

Ch. de la Vall´ee Poussin (1911), Sur la methode de l’approximation minimum, Annales Soc. Scient. Brux. 35, 1–16. [Rational best approximation.]

Ch. J. de la Vall´ee Poussin (1919), Le¸cons sur l’approximation des fonctions d’une variable r´eelle, Gauthier-Villars, Paris. [Monograph collecting de la Vall´ee Poussin’s results of the previous decade.]

J. Van Deun and L. N. Trefethen (2011), A robust implementation of the Carath´eodory–Fej´er method, BIT Numer. Math. 51, 1039–1050. [Twenty-five years after the original theoretical papers, a presentation of the practical details behind the Chebfun cf command.]

R. S. Varga and A. J. Carpenter (1985), On the Bernstein conjecture in approximation theory, Constr. Approx. 1, 333–348. [Shows that degree $n$ best polynomial approximants to $| x |$ have asymptotic accuracy $0 . 2 8 0 \dots n ^ { - 1 }$ rather than $0 . 2 8 2 \dots n ^ { - 1 }$ .]

R. S. Varga, A. Ruttan and A. J. Carpenter (1993), Numerical results on best uniform rational approximation of $| x |$ on $[ - 1 , 1 ]$ , Math. USSR-Sb. 74, 271–290. [Highprecision numerical calculations lead to the conjecture that best rational approximations to $| x |$ on $[ - 1 , 1 ]$ converge asymptotically at the rate $\sim 8 \exp ( - \pi { \sqrt { n } } )$ , proved by Stahl 1993.]

N. S. Vyacheslavov (1975), On the uniform approximation of $| x |$ by rational functions, Sov. Math. Dokl. 16, 100–104. [Sharpens the result of Newman 1964 by showing that rational approximations to $| x |$ on $[ - 1 , 1 ]$ converge at the rate $O ( \exp ( - \pi { \sqrt { n } } ) )$ .]

J. Waldvogel (2006), Fast construction of the Fej´er and Clenshaw–Curtis quadrature rules, BIT Numer. Math. 46, 195–202. [Presentation of $O ( n \log n )$ algorithms for finding nodes and weights.]

H. Wallin (1972), On the convergence theory of Pad´e approximants, in Linear Operators and Approximation, Internat. Ser. Numer. Math. 20, Birkh¨auser, pp. 461–469. [Shows that there exists an entire function $f$ whose $( n , n )$ Pad´e approximants are unbounded for all $z \neq 0$ .]

J. L. Walsh (1931), The existence of rational functions of best approximation, Trans. Amer. Math. Soc. 33, 668–689. [Shows that there exists a best rational approximation of type $( m , n )$ to a given continuous function $f$ , not just on an interval such as $[ - 1 , 1 ]$ but also on more general sets in the complex plane.]

J. L. Walsh (1934), On approximation to an analytic function by rational functions of best approximation, Math. Z. 38, 163–176. [Perhaps the first discussion of what is now called the Walsh table, the table of best rational approximations to a given function $f$ for various types $( m , n )$ .]

J. L. Walsh (1959), The analogue for maximally convergent polynomials of Jentzsch’s theorem, Duke Math. J. 26, 605–616. [Shows that every point on the boundary of a region of convergence of a sequence of polynomial approximations is the limit of zeros of its partial sums.]

J. L. Walsh (1969), Interpolation and Approximation by Rational Functions in the Complex Domain, 5th ed., American Mathematical Society. [An encyclopedic but hard-to-read treatise on all kinds of material related to polynomial and rational approximation in the complex plane, originally published in 1935.]

H. Wang and S. Xiang (2012), On the convergence rates of Legendre approximation, Math. Comp. 81, 861–877. [Theorem 3.1 connects barycentric interpolation weights $\left\{ \lambda _ { k } \right\}$ and Gauss–Legendre quadrature weights $\{ w _ { k } \}$ .]

R. C. Ward (1977), Numerical computation of the matrix exponential with accuracy estimate, SIAM J. Numer. Anal. 14, 600–610. [Presentation of a scaling-and-squaring algorithm for computing the exponential of a matrix by Pad´e approximation, a form of which is used by the MATLAB expm command.]

E. Waring (1779), Problems concerning interpolations, Phil. Trans. R. Soc. 69, 59–67. [Presents the Lagrange interpolation formula 16 years before Lagrange.]

G. A. Watson (1980), Approximation Theory and Numerical Methods, Wiley. [Textbook with special attention to $L _ { 1 }$ and $L _ { p }$ norms.]

M. Webb (2013), Computing complex singularities of differential equations with Chebfun, SIAM Undergrad. Research Online 6, https://doi.org/10.1137/12S011520. [Exploration of rational approximation for locating complex singularities of numerical solutions to ODE problems including Lorenz and Lotka–Volterra equations.]

M. Webb, L. N. Trefethen and P. Gonnet (2012), Stability of barycentric interpolation formulas for extrapolation, SIAM J. Sci. Comput. 35, A3009–A3015. [Confirming the theory of Higham 2004, shows that the “type 2” barycentric interpolation formula can be dangerously unstable if used for extrapolation outside the data interval.]

J. A. C. Weideman (2003), Computing the dynamics of complex singularities of nonlinear PDEs, SIAM J. Appl. Dyn. Syst. 2, 171–186. [Applies Pad´e approximation to computed solutions of nonlinear time-dependent PDEs to estimate locations of moving poles and other singularities.]

J. A. C. Weideman and S. C. Reddy (2000), A MATLAB differentiation matrix suite, ACM Trans. Math. Softw. 26, 465–519. [A widely used collection of MATLAB programs for generating Chebyshev, Legendre, Laguerre, Hermite, Fourier, and sinc spectral differentiation matrices of arbitrary order.]

J. A. C. Weideman and L. N. Trefethen (2007a), The kink phenomenon in Fej´er and Clenshaw–Curtis quadrature, Numer. Math. 107, 707–727. [Analysis of the effect that as $n$ increases, Clenshaw–Curtis quadrature initially converges at the same rate as Gauss rather than half as fast, as commonly supposed.]

J. A. C. Weideman and L. N. Trefethen (2007b), Parabolic and hyperbolic contours for computing the Bromwich integral, Math. Comp. 76 (2007), 1341–1356. [Derivation of geometrically convergent “Talbot contour”–type rational approximations for problems related to $e ^ { x }$ on $( - \infty , 0 ]$ .]

K. Weierstrass (1872), Uber continuierliche Functionen eines reellen Arguments, ¨ die f¨ur keinen Werth des letzteren einen bestimmten Differentialquotienten besitzen, K¨onigliche Akademie der Wissenschaften, 18 July 1872. [Weierstrass’s publication of an example (which he had lectured on a decade earlier) of a continuous, nowhere-differentiable function.]

K. Weierstrass (1885), Uber die analytische Darstellbarkeit sogenannter willk¨u ¨ rlicher Functionen einer reellen Ver¨anderlichen, Sitzungsberichte der Akademie zu Berlin, 633–639 and 789–805. [Presentation of the Weierstrass approximation theorem.]

B. D. Welfert (1997), Generation of pseudospectral differentiation matrices I, SIAM J. Numer. Anal. 34, 1640–1657. [Derivation of stable recursive formulas for computation of derivatives of interpolants.]

E. J. Weniger (1989), Nonlinear sequence transformations for the acceleration of convergence and the summation of divergent series, Computer Phys. Rep. 10, 189–371 (also available as arXiv:math/0306302v1, 2003). [Extensive survey.]

H. Werner (1964), On the rational Tschebyscheff operator, Math. Z. 86, 317–326. [Shows that the operator mapping a real function $f \in C [ - 1 , 1 ]$ to its best real rational approximation of type $( m , n )$ is continuous if and only if $f$ is itself rational of type $( m , n )$ or its best approximation has defect 0 (“nondegenerate”).]

H. Wilbraham (1848), On a certain periodic function, Cambridge and Dublin Math. J. 3, 198–201. [Analyzes the Gibbs phenomenon fifty years before Gibbs.]

J. H. Wilkinson (1984), The perfidious polynomial, in G. H. Golub, ed., Studies in Numerical Analysis, Mathematical Association of America. [Wilkinson’s major work on polynomials was in the 1960s, but this entertaining review, which won the Chauvenet Prize of the Mathematical Association of America in 1987, remains noteworthy not least because of its memorable title.]   
J. Wimp (1981), Sequence Transformations and their Applications, Academic Press. [Monograph on many methods for acceleration of convergence.]   
C. Winston (1934), On mechanical quadratures formulae involving the classical orthogonal polynomials, Ann. Math. 35, 658–677. [States a general connection between Gauss– Jacobi quadrature weights and Lagrange polynomials.]   
P. Wynn (1956), On a device for computing the $e _ { m } ( S _ { n } )$ transformation, Math. Comp. 10, 91–96. [Wynn’s first of many papers about the epsilon algorithm for acceleration of convergence of sequences.]   
S. Xiang and F. Bornemann (2012), On the convergence rates of Gauss and Clenshaw– Curtis quadrature for functions of limited regularity, SIAM J. Numer. Anal. 50, 2581–2587. [Shows that Gauss and Clenshaw–Curtis quadrature formulas converge by one factor of $n$ faster than one might expect. See also Freud 1955.]   
K. Xu and N. Hale (2016) Explicit construction of rectangular differentiation matrices, IMA J. Numer. Anal. 36, 618–632. [Explicit formulas for the rectangular differentiation matrices of Driscoll & Hale 2015 and Aurentz & Trefethen 2017a.]   
K. Zhou, J. C. Doyle and K. Glover (1996), Robust and Optimal Control, Prentice-Hall. [A leading textbook on optimal control, with special attention to approximation issues.]   
W. P. Ziemer (1989), Weakly Differentiable Functions, Springer. [Includes a definition of total variation in the measure theoretic context.]


<!-- chunk 0006: pages 351-359 -->
# Index

0.28016949902. . . , 53, 210   
0.52552491457. . . , 99   
0.68391378641. . . , 259–260   
1.06578388826. . . , 65   
1.17897974447. . . , 68–69   
1.28228345577. . . , 65   
9.28902549192. . . , 214–216, 220

AAA algorithm, x–xi, 36   
absolute continuity, 51–52, 147   
absolute convergence, 17, 27, 158, 162, 181   
abs( $_ { x }$ ), 22, 47, 50–51, 53, 62, 73, 75, 78, 118, 122, 140, 182–184, 192, 209– 214   
Adamjan–Arov–Krein approximation, 162, 194   
Airy equation, 172, 192   
Aitken extrapolation, 193, 258, 262   
algorithm, 3, 197, 254   
aliasing, 25–31, 93, 150, 268   
aliasing formula, 27   
alternant, 74, 77, 200, 206   
analytic continuation, 3, 56, 59, 62, 83, 94, 121, 159, 177, 182, 193, 197, 251–262, 269   
analytic function, 3, 16–17, 25, 43, 46, 55–62, 82–87, 90–101, 106, 115– 116, 120, 146, 182–186, 191–195, 210, 212, 244, 247, 253, 257–258, 261, 264–269   
analytic part, 159   
approximation, multivariate, 3, 44   
approximation theory, 1–5, 14, 49, 63, 117, 143, 189–198, 215   
Arnoldi iteration, 127, 194   
asymptotic series, 261   
ATAPformats, 2   
backward stability, 39, see also stability   
balancing, 139, 141   
barycentric interpolation formula, 4, 33– 41, 70, 104, 187, 266 and ill-conditioning, 102 and Remez algorithm, 77 first, 77 for Chebyshev polynomials, 40 for Legendre points, 40, 125, 152 for rational functions, 40, 195, 224 for roots of unity, x, 40 in the literature, 106 stability, 38–39, 105, 122 weights, 102   
Battles, Zachary, 4, 9, 137   
Bernstein, Sergei, 2, 14, 44, 49, 53, 55–62, 109, 209 ellipse, 56, 62, 93, 94, 121, 140, 142, 177–179, 191, 193, 251, 269 inequality, 60–61 lethargy theorem, 78 polynomial, 44, 47, 62, 79, 153 theorem(s), 60, 62, 210   
Berrut, Jean-Paul, 4, 33, 36, 41, 195   
Bessel function, 23, 138, 192   
best approximation, 1, 49, 73–79, 117, 266 operator, continuity of, 78, 205 operator, nonlinearity of, 78, 119 strong uniqueness of, 78   
Birkisson, Asgeir, x, 4, 173, 174 ´   
Blatt–Saff theorem, x, 79, 105, 140–141, 219, 252   
Borel, Emile, 2, 74 ´   
Bornemann, Folkmar, x, 4, 35, 151, 174, 257, 261, 268   
bounded variation, see variation   
Boyd, John, 136, 137, 174, 197, 270   
branches and branch points, 59, 61, 92, 193, 195, 230, 247, 260   
capacity, 40, 92–94 convergence in, 247   
cardinal function, 232   
cardinal polynomial, 33, 63, 66, 70, 107, 114   
Cauchy, Augustin-Louis, 3–4, 34, 82–83, 221, 236 integral, 86, 165, 195 integral formula, 17–18 interpolation problem, 225   
central dogma of approximation theory, 49   
Ces\`aro means, 44, 47   
cf, 2, 155–163, 191   
CF (Carath´eodory–Fej´er) approximation, 4, 155–163, 215, 219, 262   
chebellipseplot, 2, 60–61, 140, 252   
Chebfun, x, 1–5, 9, 263 and chebfun, 15 constructor, 20 ellipse, 60 Guide, 5, 22, 86   
chebfunpref, 30   
chebop, 167–175   
chebpade, 2, 251   
chebpoly, 2, 14, 19, 135   
chebpts, 2, 8, 11, 115   
chebtest, 4   
Chebyshev, Pafnuty, 2, 14, 73, 74, 123, 329

approximation, 73 coefficients, 57, 158 expansion, see Chebyshev series extreme points, 8 grid, see Chebyshev points interpolant, 7–12, 25–31, 264 interpolation, 1, 133, 158 points, 7–12, 14, 109, 264 points of the first kind, 11, 115 points of the second kind, 8 polynomials, 13–23, 62, 105, 175, 268 projection, 25–31 series, ix, 13–23, 33, 93, 133, 139, 158, 217 technology, ix, 2 Chebyshev–Pad´e approximation, 193, 247 Clenshaw, Charles, 2, 145 Clenshaw’s algorithm, 23 Clenshaw–Curtis quadrature, 4, 143–153, 267–269 coanalytic part, 159 Cody, W. J., 77, 192–194, 214 colleague matrix, 4, 15, 133–142, 148, 197, 270 compact operator, 162 set, complex, 93, 220, 247 set, real, 2, 43, 46, 204 set of functions, 74, 78, 202–203 companion matrix, 133 complex approximation, 20, 46, 61, 93, 193–195, 199, 247, 251 existence and uniqueness, 74 of $| x |$ , 219 of $\exp ( x )$ , 142, 220 of real functions, 206 on the imaginary axis, 194 on the unit disk, 163, 193 complex variables, 2, 14, 81, 101 compressed sensing, 3 comrade matrix, 135, 141, 148 conditioning, 22, 39–40, 62, 101–102, 104–105, 115, 133, 175, 217, 270 confluent nodes, 82, 86, 116 conjugate gradient iteration, 62 continued fractions, 144, 195, 236, 248– 249, 261 contour integral, 2, 81, 215 conv, 2, 45 convergence acceleration, 3, 193, 257–262 convolution, 43–46

cos(x), 46, 56, 136–137, 163, 183–184,   
237, 244–246   
cosh(x), 23   
cumsum, 2, 47, 76, 157   
defect, 199–207, 228, 236–242, 248   
deficiency, 240–241   
degenerate rational approximation, 199,   
205, 232, 237   
diff, 2, 51, 65, 129, 166–173, 185   
differential equations, 3, 101, 104, 131,   
165–175   
differentiation matrix, x, 166–175   
diffusion equation, 43, 194   
digital filters, 77, 193, 197   
Dirac delta function, 91   
discontinuity, 3, 46, 69–71, 193, 233   
divergent series, 261–262   
downsampling, 20   
Driscoll, Toby, x, 4, 171   
Driscoll–Hale discretization, 171–175

edge detection, 174   
eigenvalue problem, 15, 133–141, 148, 153, 158–162, 174, 193, 197, 254, 270   
Elliott, David, 2, 155, 174   
entire function, 43, 46–47, 56, 60–61, 100   
epsilon algorithm, 193, 258, 262   
equilibrium measure, 91–94   
equioscillation, 74–79, 119, 160–163, 196, 199–207, 213, 217, 221, 236–237, 248, 267   
equiripple approximation, 73   
equispaced points, 40, 95–102, 106, 109, 187, 264   
error curve, 40, 73   
eta extrapolation, see epsilon algorithm   
Euler, Leonhard, 34, 67, 70, 257, 261–262, 271   
Euler’s constant, 109, 116   
even function, 22, 23, 75, 78, 127, 131, 201, 205, 206, 213, 237, 244, 258   
exp(x), 75, 78, 142, 169, 194, 197, 207, 214–220, 224, 248, 262   
exponential function, see exp(x) integral, 192 integrators, 195 of a matrix, 194   
extrap, 259–262   
extrapolation of sequences and series, see convergence acceleration   
Faber’s theorem, 46, 79, 108, 264   
Fej´er, Lip´ot, 44, 47 points, 93   
Fekete points, 93–94, 130   
FFT (Fast Fourier Transform), 14, 16, 20–21, 30, 125, 145–146, 174, 226, 244, 257, 271   
Floater–Hormann interpolation, 36, 41, 195   
floating point arithmetic, see rounding errors   
fluid mechanics, 174, 178   
formal power series, 235, 249   
forward stability, 39, see also stability   
Fourier, Joseph, 13, 69 analysis, 2, 11, 17, 49, 70, 271 coefficients, 226, 232 polynomials, see trigonometric polynomials projection, 67, 115 series, ix–x, 67–69, 104, 174 spectral methods, 174 transform, 195, see also FFT   
Fox, Leslie, 2, 174   
fractal, 46   
Fr´echet derivative, 173   
Fredholm alternative, 204   
Froissart doublets, 223, 244, 247   
FUNPACK, 192   
gamma function, 192, 198   
Gauss, Carl Friedrich, 143–144, 195, 236   
Gauss–Chebyshev points, 11   
Gauss quadrature, 1, 4, 123, 143–153, 185–187, 195, 236, 267–270 Glaser–Liu–Rokhlin algorithm, 148, 268 Golub–Welsch algorithm, 129, 148, 152–153 Hale–Townsend algorithm, 129, 148– 149   
Gaussian kernel, 43–47   
Gegenbauer polynomials, 91, 124   
geometric mean distance, 9, 11–12, 41, 90, 93, 99, 101   
Gibbs, Josiah Willard, 67, 69   
Gibbs phenomenon, 63–71, 114 for Fourier series, 70 for projection, 67 rational, 232   
global optimization, 139   
Golub, Gene, 214   
Gonchar and Rakhmanov, 195, 206, 215, 217   
Gonnet, Pedro, 4, 39, 77, 137, 221–233, 235, 241   
Good, Jack, 2, 136, 197   
Gragg, William, 248   
greedy algorithm, 40, 93   
Green’s function, 91–93   
Gutknecht, Martin, 4, 155–163, 206, 214– 215, 238, 241, 248   
G¨uttel, Stefan, 4, 194, 235, 242   
$H _ { \infty }$ approximation, 162, 194   
Haar condition, 74   
Hale, Nick, x, 4, 152, 171, 177–187, 195, 214, 269, see also Driscoll–Hale discretization and Gauss quadrature, Hale–Townsend algorithm   
Halphen’s constant, 215, 219   
Hankel matrix, 155–162   
hat function, 99   
heat equation, see diffusion equation   
Hermite, Charles, 236 integral formula, xi, 3–4, 35, 81–87, 90, 94–95, 165 interpolation problem, 86   
Hermite–Fej´er interpolation, 44, 47   
hermpts, 152   
Higham, Nicholas, 4, 35, 38–39, 194, 214, 266   
Hilbert, David, 49, 74, 196   
IEEE arithmetic, 39–40   
ill-posed problem, 196, 223, 253   
inner product, 22, 123, 144   
integral, 152   
interpolation, 3, 25, 103–106 rational, see rational interpolation   
interpolatory quadrature, 144, 153   
interp1, x, 2, 34, 36, 40, 47, 96, 110, 130, 187   
'interval', 64   
inverse iteration, 193–194   
Jackson, Dunham, 2, 8, 44, 49, 53–54, 109, 209   
Jackson theorems, 51   
Jacobi, Carl Gustav Jacob, 4, 33, 35, 83, 123, 144, 190, 195, 221, 224, 236, 329 matrix, 4, 148, 153 polynomials, 91, 94, 124, 129–130 weight function, 124   
Jacobian matrix, 173   
jacpts, 94, 152   
Jentzsch’s theorem, x, 141   
Joukowsky map, 56   
Kirchberger, Paul, 3, 74, 78, 196–197   
Kosloff and Tal-Ezer, 177, 186, 269   
Kronecker delta function, 63, 70, 232   
Krylov iteration, 194   
Lagrange, Joseph-Louis, 34, 236, 271 interpolation formula, 3, 33–35, 103, 107, 265, 271   
Lagrange polynomial, see cardinal polynomial   
Lanczos, Cornelius, 2, 174 iteration, 127, 254   
Landau, Edmund, 44, 49, 115 constants, 115   
Laplace equation, xi, 90, 92, 194   
Laplace transform, 194, 215   
LATEX, 2, 5   
Laurent coefficient, 17, 160, 226 polynomial, 13, 70, 159 series, ix, 17, 23   
lazy evaluation, 168, 173   
least-squares rational approximation linearized, 4, 193, 199, 221–233, 251– 262 nonlinear, 262   
lebesgue, 2, 111   
Lebesgue, Henri, 44, 47, 49, 53, 209 constant, 1, 63, 105, 107–122, 129– 130 function, 107–116, 129 integrable, 51   
Lebesgue–Stieltjes integral, 91   
Legendre extreme points, 129, 130 points, 9, 11, 21, 40, 125, 264 polynomials, 21, 91, 124, 141, 148   
legpoly, 2, 124–129, 141   
legpts, 2, 11, 40, 129, 148–152, 185   
Leja points, 93–94   
length, 19   
lethargy theorem, 78, 207   
linear programming, 77   
linop, 168   
Lipschitz continuous, 2, 16–18, 21, 25, 27, 47, 54, 67, 78, 158, 161, 181, 264   
$\log ( x )$ , 248   
logarithmic

capacity, see capacity

potential, see potential machine precision, 11, 19, 23, 30–31, 44, 54, 62, 100, 133, 155, 162, 170, 228, 224 see also IEEE arithmetic and rounding errors 'map', 186 Markov inequality, 22 MATLAB, x, 1–5, 133, 148, 265 matrix computations, 104, 127, 193 max, 64 maximally convergent, 94, 121, 140 maximum modulus principle, 61 M´eray, Charles, 95 Mergelyan’s theorem, 46 meromorphic function, 247 minandmax, 11 minimax, 2, 73, 76, 117–120, 122, 155– 161, 184, 191–192, 200–202, 210, 213, 217–218, 251 minimax approximation, 73, 121, 199, 214 see also best approximation 'minsamples', 30 model reduction, 194, 197 monomial basis, 15–16, 21–22, 26, 105, 133, 270 de Montessus de Ballore theorem, 247 near-best, 1, 108, 117–122, 155 Newman, Donald, xi, 192–193, 211, 215 Newton, Isaac, 33 interpolation formula, 33, 106, 265 iteration, 148–149, 172–173, 219, 263 Newton–Cotes quadrature, 101, 143, 267–268 node polynomial, 30, 34, 37, 81, 89, 94, 152 nonexistence, 221, 232 nonlinearity, 77–78, 115, 119, 172–175, 177, 189–198, 238, 262, 266 nonuniqueness, 175, 206 norm, 2, 139 norm, 2, 11 normal, 205, 248 odd function, 22–23, 75, 131, 147, 201, 205, 237, 254 one-way wave equation, 195, 197 optimal control, 194 optimal interpolation points, 2, 93, 109, 116, 122 order star, 248

orthogonal polynomials, 15, 22, 35, 91, 123–131, 135, 141, 144, 270   
orthonormal polynomials, 124, 131   
overflow, 36–40   
Pach´on, Ricardo, 4, 73, 77, 174, 201, 221– 233, 241, 256–257   
padeapprox, 2, 236, 243, 257, 259   
Pad´e approximation, 4, 193–195, 203, 235–249, 251–262 algorithm, 242–243 multipoint, 247, 257 operator, 238 table, 237, see also square blocks   
Painlev´e equation, 175   
Parks–McClellan algorithm, 77   
partial fractions, 83, 189–190, 198, 219   
PDEs (partial differential equations), 194, 197   
Phragm´en, Lars Edvard, 43   
Platte, Rodrigo, 4, 174   
Platte–Trefethen–Kuijlaars theorem, 115, 187   
plotcoeffs, x, 20   
Poincar´e, Henri, 70   
poles, x, 23, 87, 193, 197, 198, 251   
pole-zero pair, see Froissart doublet   
poly, 2   
P´olya, Georg, 101, 151, 153, 268   
polyfit and polyval, 2, 39, 105, 265   
polynomial part, 191   
Poncelet, Jean-Victor, 73, 214   
potential, 91 theory, xi, 4, 9, 81, 89–95, 201, 215   
power method, 193   
principal part, 191   
projection, 25, 31, 108, 115   
pseudodifferential operator, 195   
publish, 1, 2, 5   
QR algorithm, 139, 194   
QR decomposition, 131   
quadrature, 3, 101, 123, 143–153, 195, 197, 263–271 Clenshaw–Curtis, see Clenshaw– Curtis quadrature and rational approximation, 195, 209 Gauss, see Gauss quadrature interpolatory, 144 Newton–Cotes, see Newton–Cotes quadrature Romberg, 258

tanh-sinh, 177 transformed, 185–187 quasimatrix, 22, 126, 131

radial basis functions, 3   
random data, 10–11, 109 interpolation points, 84, 116 polynomials, 142 sample points, 229, 231 walk, 44, 47, 122   
rank, 229   
ratdisk, 226, 229, 251   
ratinterp, 2, 223–224, 231–233, 251–257   
rational approximation, x–xi, 150, 162, 189– 262 function, 36, 40, 91, 189–198 interpolation, 235   
recurrence relation, 15, 127, 131–135, 141, 153, 167, 236, 261   
recursion, 137   
regularization, 247, 253   
Remez algorithm, 1, 77, 192, 206, 211, 215, 266   
Richardson, Mark, 4, 177   
Richardson extrapolation, 78, 193, 210, 257–258, 262   
Riesz, Frigyes, 75   
Riesz, Marcel, 4, 33, 36   
Riesz Representation Theorem, 152   
Robin constant, 92–93   
Romberg quadrature, 258   
rootfinding, 3, 133–142, 139, 197   
roots, 2, 77, 101, 105, 128–129, 133, 136– 142, 224, 271   
roots of unity, 7, 14, 26, 30, 40, 224–227, 235, 257   
Rouch´e’s theorem, 163   
rounding errors, 8, 11, 20, 38, 55–56, 84, 86, 100–101, 103, 105, 118, 122, 131, 141, 151, 156, 167, 224–226, 228, 232, 241–243, 247, 265, 270   
Runge, Carl, x, xi, 3, 43, 95, 98, 101, 196– 197, 264 function, 11, 55, 58, 60, 79, 96, 104, 106–107, 142, 187, 265, 269 phenomenon, 95–102, 105, 112, 151, 187, 264, 268 region, 99 theorem, 46   
Ruttan, Arden, 206, 211, 215   
Saff, Edward, 17, 79, 89, 91, 142, 206, 215, 247   
Salzer, Herbert, 33, 36, 195, 266 extrapolation, 258, 260   
sausage region, 179   
scale-invariance, 36   
scribble, 177   
sech(x), 78, 138, 147   
self-adjoint, 127   
sequences and series, 193   
Shanks extrapolation, 258, 262, see also epsilon algorithm   
SIAM 100-Digit Challenge, 257   
$\mathrm { s i g n } ( x )$ , 22, 40, 53, 63   
Simpson’s rule, 151, 185   
$\sin ( x )$ , 166, 197   
$\sin ( 1 / x )$ , 45, 47   
$\sin ^ { - 1 } ( x )$ , 178   
sinc function, 101, 177   
sine integral, 68, 71   
singularities, x–xi, 189, 191   
$\sinh ( x )$ , 23   
SPECFUN, 192   
Specht, Wilhelm, 133, 135, 270   
special functions, 77, 192   
spectral methods, 165–175 adaptive, 195 collocation and Galerkin, 166 Fourier and Chebyshev, 174 naming of, 174   
spline, 2   
splines, 3, 54, 69, 71, 104, 106   
spurious pole, see Froissart doublet   
sqrt(x), 213   
square blocks in Pad´e table, 205, 237, 240, 242, 244– 248 in Walsh table, 205   
stability, 39, 105, 141   
Stahl, Herbert, 91, 211, 215, 220, 247   
Stenger, Frank, 177, 211   
stiff PDEs, 194–195, 197   
Stigler’s law, 3   
Stirling’s formula, 47   
strong uniqueness, 78   
sum, 30, 69, 141, 146, 148   
SVD (singular value decomposition), 4, 22, 158, 159, 221, 224–232, 241   
Szeg˝o curve, 142   
$\tan ( x )$ , 61   
tanh(x), 22, 27–31, 37, 58–61, 105, 198, 251–257, 262   
Taylor series, ix, 16, 46–47, 101, 141, 235, 238, 261   
Tee, Teik Wynn, 36, 186, 195   
Toeplitz matrix, 226, 232, 238–239   
total variation, see variation   
Townsend, Alex, 4, see also Gauss quadrature, Hale–Townsend algorithm   
transfinite diameter, 92–93   
trapezoidal rule, 212, 215, 219, 258   
trigonometric approximation, 70 functions, 197 identity, 198 interpolation, 50, 65, 70, 174 polynomials, 13–14, 70, 123 projection, 67 series, 69   
'trunc', 29, 31, 68   
truncation, see projection   
Turetskii, A. H., 109, 116   
Turing, Alan, 134, 270   
tv, 51   
type of a rational function, 189, 199, 235 exact, 190, 200

ultraspherical, see Gegenbauer   
unattainable point, 225   
unbounded domain, 189–198   
underflow, 36–40   
uniform convergence, 17, 21, 43–48, 247   
uniformly distributed, 94

unit circle, 7, 11, 13–21, 26, 52, 57, 70, 133, 159–163, 193, 224, 228–232, 257, 270   
de la Vall´ee Poussin, Charles, 2, 44, 49, 53, 54, 119, 200, 209 lower bound, 78, 207   
Vandermonde matrix, 39, 105, 265   
Varga, Richard, 53, 195, 206, 211, 215   
variation, 51, 52, 54   
Waldvogel algorithm, 145–146, 268   
Wallis, John, 33   
Walsh, Joseph, 89, 200, 203, 206, 238 table, 199, 205–206, 237 theorem, x, 105, 140–141, 252   
Waring, Edward, 3, 34, 271   
wavelets, 3   
Weideman, J. A. C., 4, 109, 150, 167, 215, 219, 256   
Weierstrass, Karl, 43, 46, 60 approximation theorem, 1, 43–48, 69, 79, 153, 264 M-test, 47, 60 nondifferentiable function, 46, 54, 78, 116   
weight function, 15, 22, 123–131, 143   
Wilbraham, Henry, 3, 67–70   
Wilkinson, James, 105, 133, 270   
zerofinding, see rootfinding   
zeta function, 260, 262   
Zolotarev, Yegor Ivanovich, 212

# Key Formulas for Polynomials

Waring (1779), Lagrange (1795) (1) ${ \mathrm { N o d e ~ p o l y n o m i a l : ~ } } \ell ( x ) = \prod _ { k = 0 } ^ { n } ( x - x _ { k } )$ (5.4) Jacobi (1825) From (1) (2) Barycentric weights: λj = 1ℓ′(x ) (5.7)   
M. Riesz (1916), Salzer (1972)From (1) and (2) (3) ${ \mathrm { C h e b y s h e v ~ c a s e } } \colon \lambda _ { j } = { \frac { 2 ^ { n - 1 } } { n } } ( - 1 ) ^ { j } .$ , halved for $j = 0 , n$ (5.14) Jacobi (1825)From (1) and (2) (5.8) (4) ${ \mathrm { L a g r a n g e ~ p o l y n o m i a l ~ a t ~ } } x _ { j } \colon \ell _ { j } ( x ) = \ell ( x ) { \frac { \lambda _ { j } } { x - x _ { j } } }$ From (4) (5) $\mathrm { 1 s t ~ b a r y c e n t r i c ~ f o r m u l a : } ~ p ( x ) = \ell ( x ) \sum _ { j = 0 } ^ { n } \frac { \lambda _ { j } } { x - x _ { j } } f _ { j }$ (5.9) Dupuy (1948)From (5) (6) ${ \mathrm { 2 n d ~ b a r y c e n t r i c ~ f o r m u l a : ~ } } p ( x ) = \sum _ { j = 0 } ^ { n } { \frac { \lambda _ { j } f _ { j } } { x - x _ { j } } } \left. \sum _ { j = 0 } ^ { n } { \frac { \lambda _ { j } } { x - x _ { j } } } \right.$ (5.11)   
Cauchy (1826), Hermite (1878) From (5) (7) ${ \mathrm { H e r m i t e ~ i n t e g r a l : ~ } } f ( x ) - p ( x ) = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } { \frac { \ell ( x ) } { \ell ( t ) } } { \frac { f ( t ) } { ( t - x ) } } d t$   
Newton (1687), Cotes (1722)From (4) (8) ${ \mathrm { Q u a d r a t u r e : ~ } } I _ { n } = \sum _ { k = 0 } ^ { n } w _ { k } f ( x _ { k } ) , \quad w _ { k } = \int _ { - 1 } ^ { 1 } \ell _ { k } ( x ) d x$ (19.3), (19.4) Winston (1934)p. 152 (9) Gauss–Jacobi quadrature weights: $w _ { k } = \frac { C } { ( 1 - x _ { k } ^ { 2 } ) [ \ell ^ { \prime } ( x _ { k } ) ] ^ { 2 } }$ Wang and Xiang (2012) From (2) and (9) (10) $\mathrm { L i n k ~ t o ~ b a r y c e n t r i c ~ w e i g h t s : ~ } \lambda _ { k } = C ( - 1 ) ^ { k } \sqrt { ( 1 - x _ { k } ^ { 2 } ) w _ { k } }$ (19.13)   
ellman, Kashef and Casti (1972) From (4) (11) ${ \mathrm { S p e c t r a l ~ d i f f } } ^ { \prime } { \mathrm { n } } \colon D _ { i j } = \ell _ { j } ^ { \prime } ( x _ { i } ) = { \frac { \lambda _ { j } } { \lambda _ { i } ( x _ { i } - x _ { j } ) } } ; \ { \frac { x _ { j } } { 1 - x _ { j } ^ { 2 } } } { \mathrm { i f } } \ i = j$

The Runge phenomenon follows from (7), as does exponential convergence of Chebyshev interpolants and Gauss or Clenshaw–Curtis quadrature for analytic functions.
