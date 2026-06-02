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

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0001_pages_0001-0070/auto/images/e16191e2c8a5b45b1d6703ac229894737e9e0483a4b67b99b22effc61144124f.jpg)

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

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0001_pages_0001-0070/auto/images/6ff18adecccf563fa0c8cc13e651764aae8454117ed701b33e9705569c4ca150.jpg)  
Figure 1.0.1. The interactive page located at http://www.nr.com/dependencies sorts out the dependencies for any combination of Numerical Recipes routines, giving an ordered list of the necessary #include files.

University Press (e.g., from Amazon.com or your favorite online or physical bookstore). The code comes with a personal, single-user license (see License and Legal Information on p. xix). The reason that the book (or its electronic version) and the code license are sold separately is to help keep down the price of each. Also, making these products separate meets the needs of more users: Your company or educational institution may have a site license — ask them.

3. How do I know which files to #include? It’s hard to sort out the dependencies among all the routines.

In the margin next to each code listing is the name of the source code file that it is in. Make a list of the source code files that you are using. Then go to http://www.nr.com/dependencies and click on the name of each source code file. The interactive Web page will return a list of the necessary #includes, in the correct order, to satisfy all dependencies. Figure 1.0.1 will give you an idea of how this works.

4. What is all this Doub, Int, VecDoub, etc., stuff?

We always use defined types, not built-in types, so that they can be redefined if necessary. The definitions are in $\mathtt { n r 3 . h }$ . Generally, as you can guess, Doub means double, Int means int, and so forth. Our convention is to begin all defined types with an uppercase letter. VecDoub is a vector class type. Details on our types are in $\ S 1 . 4$ .
