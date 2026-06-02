Approximation Theory and Approximation Practice, Extended Edition is a textbook on classical polynomial and rational approximation theory for the twenty-first century. It is aimed at advanced undergraduates and graduate students across all of applied mathematics.

Nick Trefethen is Professor of Numerical Analysis at the University of Oxford and a Fellow of the Royal Society. During 2011–2012 he served as President of SIAM.

# siam.

Society for Industrial and Applied Mathematics 3600 Market Street, 6th Floor Philadelphia, PA 19104-2688 USA +1-215-382-9800 • Fax +1-215-386-7999 siam@siam.org • www.siam.org

# Approximation Theory and Approximation Practice

Extended Edition

# Approximation Theory and Approximation Practice

Extended Edition

![](images/65cf6e039127b1292ea5f9f3316614b432012f1f74abc2a4709d1428c4bc4e13.jpg)

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

![](images/a4907fa20ca2c90fb551bb4661e603bf39b0e9c031af17981b2d92ce0445c966.jpg)

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

![](images/089a3422b2298919e2a08410d5fb117384299dae94c663faf66b12d4af6c0320.jpg)

They cluster near $^ { 1 }$ and $^ { - 1 }$ , with the average spacing as $n \to \infty$ being given by a density function with square root singularities at both ends (Exercise 2.2).

Let $\{ f _ { j } \}$ , $0 \leq j \leq n$ , be a set of numbers, which may or may not come from sampling a function $f ( x )$ at the Chebyshev points. Then there exists a unique polynomial $p$ of degree $n$ that interpolates these data, i.e., $p ( x _ { j } ) = f _ { j }$ for each $j$ . When we say “of degree $n$ ,” we mean of degree less than or equal to $n$ , and we let $\mathcal { P } _ { n }$ denote the set of all such polynomials:

$$
{ \mathcal { P } } _ { n } = \{ { \mathrm { p o l y n o m i a l s ~ o f ~ d e g r e e ~ a t ~ m o s t ~ } } n \} .
$$

As we trust the reader already knows, the existence and uniqueness of polynomial interpolants apply for any distinct set of interpolation points. In the case of Chebyshev points, we call the polynomial the Chebyshev interpolant.

Polynomial interpolants through equally spaced points have terrible properties, as we shall see in Chapters 11–15. Polynomial interpolants through Chebyshev points, however, are excellent. It is the clustering near the ends of the interval that makes the difference, and other sets of points with similar clustering, like Legendre points (Chapter 17), have similarly good behavior. The explanation of this fact has a lot to do with potential theory, a subject we shall introduce in Chapter 12. Specifically, what makes Chebyshev or Legendre points effective is that each one has approximately the same average distance from the others, as measured in the sense of the geometric mean. On the interval $[ - 1 , 1 ]$ , this average distance is about $1 / 2$ (Exercise 2.6).

Chebfun is built on Chebyshev interpolants [Battles $\&$ Trefethen 2004]. For example, here is a certain step function:

![](images/da9403ad7939323187e0f7e46c26b3b43ca380954178231da4330fd326ed12e2.jpg)

By calling chebfun with a second explicit argument of 6, we can construct the Chebyshev interpolant to $f$ through 6 points, that is, of degree 5:

$_ { \mathrm { ~ p ~ } } =$ chebfun(f,6); hold on, plot(p,'.-')

![](images/306ce5cebfd233191ff303f096d666529c76fef06adfceafdcfdd1e946014890.jpg)

Similarly, here is the Chebyshev interpolant of degree 25:

plot(f,'k'), p = chebfun(f,26); hold on, plot(p,'.-')

![](images/1f6a7ddf24f12aa216eb5805c2fdf961a36cccf4160adfafb15b347982c2748a.jpg)

Here are a more complicated function and its interpolant of degree 100:

f = sin( $6 * \mathbf { x } .$ ) $^ +$ sign(sin(x+exp(2\*x))); plot(f,'k'), $_ { \mathrm { ~ p ~ } } =$ chebfun(f,101); hold on, plot(p)

![](images/988a66496449bbfc0ad7d7054054c3e5f991576cf4ff4fe747cd807963b78830.jpg)

Another way to use the chebfun command is by giving it an explicit vector of data rather than a function to sample, in which case it interprets the vector as data for a Chebyshev interpolant of the appropriate order. Here, for example, is the interpolant of degree 99 through random data values at 100 Chebyshev points in $[ - 1 , 1 ]$ :

![](images/ed9a30cce97abab6bb5c7f3e8ca10ac81f79e8aa8d7756b71c6d25fedbc5a71d.jpg)

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

![](images/68bf43077d13d7c1f725d86d95ad84072ad9bc82a5fda182fa15547bcf1122fa.jpg)

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

![](images/a38111d609b1c613fa82cd5c080ecc8b9adcd79544f13eeb366e15d78996273e.jpg)

If we plot the absolute values of the Chebyshev coefficients, here is what we find:

a $=$ chebcoeffs(f); semilogy(abs(a),'m')

![](images/5be2ec1f43e4b7d1b635b6016ce0da4727c62c690c2d8e81d0d988c9d9675ecf.jpg)

One can explain this plot as follows. Up to a degree of approximately $k = 8 0$ , a Chebyshev series cannot resolve $f$ much at all, for the oscillations occur on too short wavelengths. After that, the series begins to converge rapidly. By the time we reach $k = 1 5 0$ , the accuracy is about 15 digits, and the computed Chebyshev series is truncated there. We can find out exactly where the truncation took place with the command length(f):

length(f)

This tells us that the chebfun is a polynomial interpolant through 151 points, that is, of degree 150.

Without giving all the engineering details (see Aurentz & Trefethen 2017b), here is a fuller description of how Chebfun constructs its approximation. First it calculates the polynomial interpolant through the function sampled at 17 Chebyshev points, i.e., a polynomial of degree 16, and checks whether the Chebyshev coefficients appear to be small enough. For the example just given, the answer is no. Then it tries 33 points, then 65, and so on. In this case Chebfun judges at 257 points that the Chebyshev coefficients have fallen to the level of rounding error. At this point it truncates the tail of terms deemed to be negligible, leaving a series of 151 terms (Exercise 3.13). The corresponding degree 150 polynomial is then evaluated at 151 Chebyshev points via the FFT, and these 151 numbers become the data defining this particular chebfun. Engineers would say that the signal has been downsampled from 257 points to 151.

For another example we consider a function with two spikes:

![](images/38f4bc5beb53618c5e4c94687cfc271e28765dbac3d0e73350ca3cf36d2a5d54.jpg)

Here are the Chebyshev coefficients of the chebfun. This time, instead of chebcoeffs and semilogy, we execute the special command plotcoeffs, which has the same effect.

plotcoeffs(f,'m')

![](images/7d5983c43a58691660a94bfe374771938eea932b1df109b376064066a476e7c4.jpg)

Note that although it is far less wiggly, this function needs six times as many points to resolve as the previous one (Exercise 3.13). We shall explain these polynomial degrees in Chapter 8.

Chebyshev interpolants are effective for complex functions (still defined on a real interval) as well as real ones. Here, for example, is a complex function that happens to be periodic, though the Chebyshev representation does not take advantage of this fact.

$\begin{array} { r l r } { \mathbf { f } } & { = } & { \left( 3 + \sin \left( 1 0 ^ { \ast } \mathbf { p } \mathbf { i } ^ { \ast } \mathbf { x } \right) + \sin \left( 6 1 ^ { \ast } \mathbf { e x p } \left( . 8 \ast \sin \left( \mathbf { p } \mathbf { i } ^ { \ast } \mathbf { x } \right) + . 7 \right) \right) \right) \ast \mathbf { e x p } \left( 1 \mathbf { i } ^ { \ast } \mathbf { p } \mathbf { i } ^ { \ast } \mathbf { x } \right) ; } \end{array}$ A plot shows the image of $[ - 1 , 1 ]$ under $f$ , which appears complicated: plot(f,'color',[0 .8 0])

![](images/55ab47f52feebe6e58596e0e70bbdb4d5d3c05874ee41bb7850c7d816d5e13c7.jpg)

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

![](images/84418133a7618ae8edae1555741d0d56e9de746ebecdc608b0af410e69a41275.jpg)

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

![](images/c3400146e9e81a4fe3f33873b958a85347149eefbc2cba3306720e9892245901.jpg)

Here are the errors $f - f _ { n }$ and $f - p _ { n }$ :

subplot(1,2,1), plot(f-fn, $" \mathtt { g } ^ { \prime }$ ), subplot(1,2,2), plot(f-pn,'r')

![](images/2b24a7bbb741c1e16f18e5ca8d1105d962920a71e53b9ba4b0aaed099e3195ee.jpg)

Here is the analogous plot with $n = 4$ increased to 24:

$\tt { n } = 2 4$ ; pn $=$ chebfun(f, $\mathtt { n } + 1 )$ ; fn $=$ chebfun(f,'trunc', $\ n { + } 1 \cdot$ ); subplot(1,2,1), plot(f-fn, $" \mathtt { g } " .$ ), subplot(1,2,2), plot(f-pn, $" \mathbf { r } \cdot \mathbf { \xi }$ )

![](images/bced4887f07c445164e08746af701fc74e33ce0d61fe7e2a9ead14ee92130e4b.jpg)

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

![](images/7ada0eebcb2ee5cdf0418824c694efc707322b0982fec40be5c7c0e25b9f3437.jpg)

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

![](images/3aa6a6a4ea6eade5aa8567f1ac4f1a523d15359d4782f62c7b80e1e66c729cb2.jpg)

In this short time, Chebfun has evaluated a polynomial interpolant of degree about 5000 at 10000 sample points.

Raising the degree further, let $p$ be the Chebyshev interpolant of degree $1 0 ^ { 6 }$ to the function $\sin ( 1 0 ^ { 5 } x )$ on $[ - 1 , 1 ]$ :

$$
\begin{array} { r } { \textbf { f f } = \textbf { \textsf { Q } } ( \textbf { x } ) \ \sin \left( 1 \mathrm { e } 5 * \mathrm { x } \right) ; \mathrm { ~ p ~ = ~ c h e b f u n } \left( \mathrm { f f } , 1 0 0 0 0 0 1 \right) ; } \end{array}
$$

How long does it take to evaluate this interpolant at 100 points?

xx = linspace(0,0.0001); tic, pp = p(xx); toc

Elapsed time is 0.237103 seconds.

Not bad for a million-degree polynomial! The result looks fine, plot(xx,pp,'.')

![](images/11381c55506928be74d84be9a15384993956419a8d7cb81123ab61e96e95021f.jpg)

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

![](images/756be56501e27c15923928c47a67e99435011337960d728fa84e898d2e29cf3a.jpg)

We can illustrate the idea of Weierstrass’s proof by showing the convolution of this complicated function with a Gaussian. First, here is the same function $f$ recomputed over a subinterval extending from one of its zeros to another:

a = 0.2885554757; b = 0.3549060246;   
$\boldsymbol { \tt { f } } 2 { \it { \Delta \phi } } =$ chebfun(@(x) sin(1/x)\*sin(1/sin(1/x)),[a,b],2000); plot(f2)

![](images/3fbf3af31fbdfe1b929c7cdb3f715dd8626a285940e86e5fd70ea1db685ccd3f.jpg)

Here is a narrow Gaussian with integral 1:

$\scriptstyle { \mathrm { ~ t ~ } } = { \mathrm { ~ 1 } } \mathtt { e } - 7$ ;   
phi $=$ chebfun(@(x) exp(-x^2/(4\*t))/sqrt(4\*pi\*t),.003\*[-1 1]); plot(phi)

![](images/3d9de49f557f2dd48979c8d49aa6ab15cfe8fd777d11b57b28e53c0340cadbc4.jpg)

Convolving the two gives a smoothed version of the close-up of $f$ . Notice how the short wavelengths vanish while the long ones are nearly undisturbed.

![](images/7112b59880b548805bd95a1e245b4d6c774f2ccf38e34461aafa0e705afe4b29.jpg)

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

![](images/0732e20948736cab1a0a6e41228ed0e34dd06745bbfda041344b6d8922ad2135.jpg)

Similarly, we get cubic convergence for

$$
f ( x ) = | \sin ( 5 x ) | ^ { 3 } ,
$$

which is three times differentiable with jumps in the third derivative at $x = 0$ and $\pm \pi / 5$ .

fo $\begin{array} { r l } { \mathbf { \Psi } } & { \mathbf { \beth } = \mathbf { \beth } \mathbf { b } \mathbf { s } \left( \mathbf { \beth } \mathbf { \beth } ( \mathbf { \beth } \mathbf { \beth } \mathbf { \beth } ) \right) \mathbf { \beth } \mathbf { \beth } \mathbf { \ b } ; } \\ { \mathbf { \beth } } & { \mathbf { \ b j } ~ = ~ \mathbf { \ b { 1 } } : \mathbf { \ b { 1 } } \mathbf { } \mathbf { e n g t h } \left( \mathbf { n n } \right) } \\ & { \mathbf { \ b n } ~ = ~ \mathbf { \ b { n } } \mathbf { n } ( \mathbf { j } ) \colon \mathbf { \ b j } ~ \mathbf { \ b n } ~ = ~ \mathbf { \ b { c h e b f u n } } ( \mathbf { f } , \mathbf { n } + \mathbf { 1 } ) ; ~ \mathbf { \ b e } \mathbf { e } \left( \mathbf { j } \right) ~ = ~ \mathbf { \ b n o r m } \left( \mathbf { f } - \mathbf { f } \mathbf { n } , \mathbf { i } \mathbf { n } \mathbf { f } \right) ; } \end{array}$ end $\mathtt { l o g l o g ( n n , n n . \hat { \mu } ^ { - } 3 , \mu ^ { \prime } r ^ { \prime } ) }$ , hold on, loglog(nn,ee,'.')

![](images/9fc66b531bba634f0249beabcffc6d0907ed446aac9bcf64db6037c22f21f12e.jpg)

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

![](images/72ea8df1c59a1d8b6e0c461a1caeb2c66610e22ed3ff60ccca6f136bb88ef4e0.jpg)

If $f$ is analytic not just on $[ - 1 , 1 ]$ but in the whole complex plane—such a function is said to be entire—then the convergence is even faster than geometric. Here, for the function $\cos ( 2 0 x )$ , the dots are approaching not a fixed straight line but a curve that gets steeper as $n$ increases, until rounding errors cut off the progress.

f $\begin{array} { r l } { = } & { \cos \left( 2 0 { * \mathbf { x } } \right) ; ~ \mathrm { n n ~ = ~ } 0 : 2 : 6 0 ; ~ \mathrm { e e ~ = ~ } 0 { * \mathbf { n } } \mathrm { n } ; } \\ { \mathrm { 3 r ~ j ~ = ~ } 1 : \mathrm { 1 e n g t h } \left( \mathrm { n n } \right) } \\ { \mathrm { ~ n ~ = ~ } \mathrm { n n ( j ) } ; ~ \mathrm { f n ~ = ~ c h e b f u n } \left( \mathrm { f , n + 1 } \right) ; ~ \mathrm { e e ( j ) ~ = ~ } \mathrm { n o r m } \left( \mathrm { f - f n , i n f } \right) ; } \end{array}$   
end   
semilogy(nn,ee,'.')

![](images/63bd3fd8967484fb149e6ea5504922c367fdc556e220582d4c3baf49c78fa183.jpg)

There are elegant theorems that explain these effects. If $f$ is analytic on $[ - 1 , 1 ]$ , then it can be analytically continued to a neighborhood of $[ - 1 , 1 ]$ in the complex plane. (The idea of analytic continuation is explained in complex variables textbooks; see also Chapter 28.) The bigger the neighborhood, the faster the convergence. In particular, for polynomial approximations, the neighborhoods that matter are the regions in the complex plane bounded by ellipses with foci at $^ { - 1 }$ and 1, known as Bernstein ellipses [Bernstein 1912b, 1912c & 1914a]. It is easy to plot these curves: pick a number $\rho > 1$ and plot the image in the complex $x$ -plane of the circle of radius $\rho$ in the $z$ -plane under the Joukowsky map $x = ( z + z ^ { - 1 } ) / 2$ . We let $E _ { \rho }$ denote the open region bounded by this ellipse. Here, for example, are the Bernstein ellipses corresponding to the parameters $\rho = 1 . 1 , 1 . 2 , . . . , 2$ :

z = exp(2i\*pi\*x);   
f $\mathrm { \Lambda } _ { 0 \Sigma } \ \mathrm { \bf ~ r h o } = 1 . 1 : 0 . 1 : 2$ e = (rho\*z+(rho\*z)^(-1))/2; plot(e), hold on   
end

![](images/69575e4e795ac7ee11b111ff42e27f587cba42c34c5d6960fc5662c715aa98a0.jpg)

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

![](images/d326a4b3ef702de624286acfd195a476bf5444dd6766a320c981a3ea782d1461.jpg)

Here is a more extreme but entirely analogous example: $\operatorname { t a n h } ( 5 0 \pi x )$ , with poles at $\pm 0 . 0 1 i$ . These poles are so close to $[ - 1 , 1 ]$ that the convergence is much slower, but it is still robust. The only difference in this code segment is that $\mathtt { n o r m } ( \mathtt { f } \mathtt { - f } \mathtt { n } , \mathtt { i n f } )$ , a relatively slow Chebfun operation that depends on finding zeros of the derivative of $\tt f - f n$ , has been replaced by the default 2-norm norm(f-fn), which is quick. This makes little difference to the figure, as the exponential decay rates are the same. (In the $\infty$ -norm, the dots in the figure would appear just above the red line instead of just below it.)

$\begin{array} { r l } & { \mathrm { ~ f ~ \omega = \ t a n h ( 5 0 * p i * x ) ~ ; ~ n n ~ \omega = ~ 0 : 2 0 0 : 4 0 0 0 ; ~ \eta \in \varphi = \varphi 0 * n n ; } } \\ & { \mathrm { ~ f o r ~ j ~ \omega = ~ 1 : 1 \mathrm { e n g t h } ( n n ) } } \\ & { \mathrm { ~ n ~ = ~ n n ( j ) ~ ; ~ f { n ~ = ~ c h e b f u n ( f , n + 1 ) } ~ ; ~ \eta \in e ( j ) ~ \omega = \varphi _ { n o r m } ( f - f { n } ) ~ ; } } \end{array}$ end   
rho $=$ ( $1 +$ sqrt(10001))/100;   
semilogy(nn,rho.^-nn,'-r'), hold on, semilogy(nn,ee,'.')

![](images/ae6d627aab68f93b8b6605848098e28f3faec1735413b2d13dce5c7b784f660a.jpg)

For an example with a real singularity, the function √ $\sqrt { 2 - x }$ has a branch point at $x = 2$ , corresponding by (8.4) to $\rho = 2 + \sqrt { 3 }$ . Again we see a good match, with the curve gradually bending over to the expected slope as $n \to \infty$ .

f $\begin{array} { r l } { = } & { \mathbf { s q r t } ( 2 \mathbf { - x } ) ; ~ \mathrm { n n ~ = ~ } 0 : 3 0 ; ~ \mathbf { e e ~ = ~ } 0 * \mathrm { n n } ; } \\ { \mathrm { ~ \mathrm { ~  ~ \lambda ~ } ~ } ] ~ \mathrm { ~  ~ \lambda ~ } = ~ 1 : \mathrm { { l e n g t h } } ( \mathrm { n n } ) } \\ { ~ \mathrm { ~  ~ \lambda ~ } = } & { \mathrm { { n n } ( j ) ~ ; ~ \mathrm { ~ \mathrm { ~ f n ~ = ~ c h e b f u n } ( f , n + 1 ) ~ } ; ~ \mathbf { e e } ( j ) ~ = ~ \mathrm { n o r m } ( f \mathrm { - } f n , \mathrm { i n f } ) ~ } ; } \end{array}$   
f   
end   
rho $=$ 2+sqrt(3); semilogy(nn,rho.^-nn,'-r')   
hold on, semilogy(nn,ee,'.')

![](images/124f5ab1686affef3bb200a80fa21247e2ca85304b6e3063b758f75f778428c9.jpg)

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

![](images/be6fa3870d4c5327066d466f249064457bbd940e1ceea9eaf2e1a41cedcad210.jpg)

For the entire function $f ( x ) = \exp ( - 2 0 0 x ^ { 2 } )$ , the Chebfun ellipse has much the same shape, although now $f$ has no singularities:

f = chebfun('exp(-200\*x^2)'); plotregion(f)

![](images/e24a609c87bb2d15d9eceae1984aaa1a388f8766374a10cd91b9d1cb0a5966b7.jpg)

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