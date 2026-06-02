# PURE AND APPLIED MATHEMATICS

A Wiley-Interscience Series of Texts,Monographs,and Tracts

Founded by RICHARD COURANT   
EditOrS:LIPMAN BERS.PETER HILTON,HARRY HOCHSTADT,PETER LAX, JOHN TOLAND   
ADAMEK,HERRLICH,and STRECKER-Abstract and Concrete Categories   
\*ARTIN-Geometric Algebra   
BERMAN, NEUMANN,and STERN-Nonnegative.Matrices in Dynamic Systems   
\*CARTER-Finite Groups of Lie Type   
CLARK-Mathematical Bioeconomics: The Optimal Management of Renewable Resources, 2nd Edition   
\*CURTIS and REINER-Representation Theory of Finite Groups and Associative Algebras   
\*CURTIS and REINER-Methods of Representation Theory: With Applications to Finite Groups and Orders,Vol. I   
CURTIS and REINER-Methods of Representation Theory: With Applications to Finite Groups and Orders,Vol. II   
\*DUNFORD and SCHWARTZ-Linear Operators Part 1-General Theory Part 2—Spectral Theory, Self Adjoint Operators in Hilbert Space Part 3—Spectral Operators   
FOLLAND-Real Analysis:Modern Techniques and Their Applications   
FRIEDMAN-Variational Principles and Free-Boundary Problems   
FROLICHER and KRIEGL-Linear Spaces and Differentiation Theory   
GARDINER-Teichmuller Theory and Quadratic Differentials   
GRIFFITHS and HARRIS-Principles of Algebraic Geometry   
HANNA and ROWLAND-Fourier Series and Integrals of Boundary Value Problems, 2nd Edition   
HARRIS-A Grammar of English on Mathematical Principles   
\*HENRICI-Applied and Computational Complex Analysis \*Vol.1, Power Series-Integration-Conformal Mapping-Location of Zeros Vol. 2.Special Functions-Integral Transforms-Asymptotics-Continued Fractions Vol. 3,Discrete Fourier Analysis, Cauchy Integrals,Construction of Conformal Maps,Univalent Functions   
\*HILTON and WU-A Course in Modern Algebra   
\*HOCHSTADT-Integral Equations   
KOBAYASHI and NOMIZU-Foundations of Differential Geometry, Vol. I   
KOBAYASHI and NOMIZU-Foundations of Differential Geometry,Vol: II   
KRANTZ-Function Theory of Sevqral Complex Variables   
LAMB-Elements of Soliton Theory   
LAY-Convex Sets and Their Applicatidns   
McCONNELL and ROBSON-Noncommutative Noetherian Rings   
NAYFEH-Perturbation Methods   
NAYFEH   
\*PRENTE   
RAO-M   
RENELT /）   
RIVLIN-Chebyshev Polynomials:From Approximation Theory to Algebra and Number Theory,2nd Edition   
ROCKAFELLAR-Network Flows and Monotropic Optimization   
ROITMAN-Introduction to Modern Set Theory   
\*RUDIN-Fourier Analysis on Groups   
SCHUMAKER-Spline Functions:Basic Theory   
SENDOV and POPOV-The Averaged Moduli of Smoothness   
\*SIEGEL-Topics in Complex Function Theory

Volume 1-Elliptic Functions and Uniformization Theory blume 2-Automorphic Functions and Abelian Integrals

Volume 3-Abelian Functions and Modular Functions of Several Variables   
STAKGOLD-Green's Functions and Boundary Value Problems   
\*STOKER-Differential Geometry   
STOKER-Nonlinear Vibrations in Mechanical and Electrical Systems   
TURAN-On a New Method of Analysis and Its Applications   
WHITHAM-Linear and Nonlinear Waves   
ZAUDERER-Partial Differential Equations of Applied Mathematics,2nd edition

\*Now available in a lower priced paperback edition in the Wiley Classics Library.

# CHEBYSHEV POLYNOMIALS

# CHEBYSHEV POLYNOMIALS

# From Approximation Theory to Algebra and Number Theory

Second Edition

THEODORE J. RIVLIN IBM Research Division Thomas J. Watson Research Center Yorktown Heights, New York

# A Wiley-Interscience Publication

JOHN WILEY & SONS, INC.

New York · Chichester · Brisbane · Toronto · Singapre

Copyright $\circledcirc$ 1990 by John Wiley & Sons, Inc.

All rights reserved. Published simultaneously in Canada.

Reproduction or translation of any part of this work beyond that permitted by Section 107 or 108 of the 1976 United States Copyright Act without the permission of the copyright owner is unlawful. Requests for permission or further information should be addressed to the Permissions Department, John Wiley & Sons, Inc.

Library of Congress Cataloging in Publication Data

Rivlin, Theodore J., 1926- Chebyshev polynomials: from approximation theory to algebra and number theory/Theodore J.Rivlin.-2nd ed.

p cm. (Pure and applied mathematics) “A Wiley-Interscience publication." 515'.55--dc20 ISBN 0-471-62896-4 109876543 Printed in the Eablioihek

# PREFACE

In this new edition, errors (mostly minor) that have come to my attention have been corrected and new material, amounting to about one-third of the contents of the first edition, has been added. The new material has been inserted in its appropriate seting in the form of text or exercises (about 80 in number). In addition, a new chapter introducing some elementary algebraic and number theoretic properties of the Chebyshev polynomials has been appended.

Let me next outline the more substantial additions in this new edition. In Chapter 1, results about the minimal Lebesgue constants for polynomial interpolation and an estimate of the size of the Lebesgue constants for interpolation in equally spaced points are given. The connections between the Fibonacci and Lucas numbers and the Chebyshev polynomials are exhibited, thus providing easy access to many properties of these numbers. The first chapter ends with an exposition of Erdos' result (and related material), extending to the complex plane the property of the Chebyshev polynomial as the polynomial of most “rapid growth” on the real line.

In Chapter 2 the notion of strong uniqueness of polynomials of best approximation is introduced and the best strong uniqueness constant for the best approximation of the Chebyshev polynomial is obtained explicitly. An extensive discusson of generalizations of the Bernstein and Markov inequalities for polynomials is given, and some recent results about extremal properties of polynomials with “curved majorants” are presented.The Remez inequality for polynomials is mentioned,as is the recent proof of Erdos' conjecture that the Chebyshev polynomial is the “longest polynomial” on [-1,1]. The chapter ends with an extensive description of the role of the Chebyshev polynomials in an iterative method of solving a system of linear equations.

Chapter 3 contains the analog (due to Szego) of the Enestrom-Kakeya theorem for polynomials represented in the Chebyshev basis. In Chapter 4 the phenomenon of the “white curves,”visible when graphs of the first thirty Chebyshev polynomials are superimposed in the square $- 1 \leqslant x \leqslant 1 ,$ ， $- 1 \leqslant y \leqslant 1$ , is discussed. The major result of the new Chapter 5 is a detailed and complete description of the factorization of the Chebyshev polynomials into irreducible polynomials over the rational numbers.

I have endeavored to maintain the “reader-friendly” tone of the exposition in the new material in the continuing hope of introducing the student, and other readers, to various interesting areas of mathematics by means of the example of the Chebyshev polynomials,as well as adding to the repository of information about these useful and ubiquitous mathematical objects.

Chappaqua, N.Y. January 1990

THEODORE J. RIVLIN

# PREFACE TO THE FIRST EDITION

This book has two main aims: (1) to give a survey of the most important properties of the Chebyshev polynomials and (2) to introduce some interesting areas of mathematical analysis: interpolation theory， orthogonal polynomials,approximation theory,numerical integration, numerical analysis,ergodic theory, by the example of the Chebyshev polynomials. The Chebyshev polynomial is like a fine jewel that reveals different characteristics under illumination from varying positions,and I feel that apart from its great intrinsic interest it is an ideal vehicle for giving the student a taste of these various areas.

A brief outline of the book follows. In the first chapter,after definitions and notation are presented, polynomial interpolation at the zeros and extrema of the Chebyshev polynomial is thoroughly examined. The rest of the chapter is devoted to the Chebyshev polynomials as orthogonal polynomials. The point of departure of the second chapter is the minimax property of the Chebyshev polynomial on an interval. This is seen as approximating a monomial best by lower powers or alternatively maximizing the leading coefficient of a polynomial of fixed degree and size. The former point of view leads to a brief course in the theory of best uniform approximation and the latter to an essay on maximizing linear functionals on a space of polynomials. This chapter is a much amplified version of Rivlin and Shapiro [1] $( [ n ]$ refers to item n after the associated name in the references). Related material may be found in Shapiro [2]. The second part of this chapter is a prelude to the systematic and much more detailed study of similar problems in Voronovskaja [1]. One highlight of the chapter is Duffin and Schaeffer's generalization of V. A. Markov's bound on the derivative of a polynomial, which appears in a book in English for the first time here.

The Chebyshev polynomials have found extensive application in numerical analysis. One important technique in applications is the expansion of a function in a series of Chebyshev polynomials. The main theme of the third chapter is the effectiveness of the partial sums of a Chebyshev expansion of a function as approximations to the function. One of the most striking porperties of the set of Chebyshev polynomials is that it is closed under functional composition. The fourth, and last, chapter focuses on this facet of the polynomials and concludes with a study of their ergodic properties.

An attempt has been made to maintain a moderate pace in the exposition and to spell out many details with the hope that the book might serve as well as "leisure reading” for a broader mathematical community. More than two hundred exercises of varying degrees of diffculty have been provided. Some substantial results are broken up into chains of exercises and hints have been given for the more difficult ones.

I make no encyclopedic claims for the book's coverage of facts about Chebyshev polynomials. Among the omissions of which I am aware I particularly regret that ignorance prevented me from discussing two topics, the number theoretic aspects of the Chebyshev polynomials and applications of Chebyshev polynomials in kinematics.

It is my pleasant duty to thank many friends for helpful discussions of material in the book. In particular, I want to thank my collagues Charles Micchelli and Roy Adler. Dr. Micchelli read a preliminary version of the manuscript and made many helpful recommendations, Dr. Adler suggested several improvements in the last chapter.

THEODORE J. RIVLIN

Chappaqua,New York March 1974

# CONTENTS

# 1 Definitions and Some Elementary Properties

1.1 Definition of the Chebyshev Polynomials,1 Exercises 1.1.1-1.1.6,5

1.2Some Simple Properties, 5   
Exercises 1.2.1-1.2.23, 7

1.3Polynomial Interpolation at the Zeros and Extrema, 10 Exercises 1.3.1-1.3.24, 23

1.4 Hermite Interpolation, 28 Exercises 1.4.1-1.4.10, 29 Exercises 1.4.11-1.4.12,34 .5Orthogonality, 34 1. Second Order Linear Homogeneous Differential Equation, 36 Exercises 1.5.1-1.5.13, 37 2. Three-Term Recurrence Formula, 39 Exercises 1.5.14-1.5.19, 40 3. Generating Function, 41 4. Least Squares, 42 5. Numerical Integration, 43 Exercises 1.5.20-1.5.25, 46 Exercises 1.5.26-1.5.67, 53

# 2 Extremal Properties

AUniform Approximation of Continuous Functions, 68 2.1 Convex Sets in n-Space, 68 Exercises 2.1.1-2.1.5, 71 2.2 Characterization of Best Approximations, 71 Exercises 2.2.1-2.2.15,76

2.3Chebyshev Systems and Uniqueness, 78 Exercises 2.3.1-2.3.4, 83

2.4 Approximation on an Interval, 84 Exercises 2.4.1-2.4.50, 88

B Maximizing Linear Functionals on $\mathbf { \mathcal { P } _ { n } } , \mathbf { \mathcal { P } } \mathbf { \mathcal { I } }$

2.5An Interpolation Formula for Linear Functionals,97 Exercises 2.5.1-2.5.12, 99

2.6 Linear Functionals on ${ \mathcal { P } } _ { n }$ ，102   
Exercises 2.6.1-2.6.13,106

2.7Some Examples in which the Chebyshev Polynomials Are Extremal, 107 1. Growth Outside the Interval, 108 2. Size of Coefficients,110 3. The Tau Method, 113 4. Size of the Derivative, 118 5. V. A. Markov's Theorem, 123 Exercises 2.7.1-2.7.14,138

2.8Additional Extremal Problems,141

1． More About the Bernstein and Markov Inequalities, 141 1.1POLYNOMIAL INEQUALITIES IN THE COMPLEX PLANE,141 1.2 POLYNOMIALS WITH CURVED MAJORANTS, 145 Exercises 2.8.1-2.8.8, 147

2.Miscellaneous Extremal Properties， 149

2.1THE REMEZ INEQUALITY FOR POLYNOMIALS,149   
2.2 THE LONGEST POLYNOMIAL,149   
2.3 AN ITERATIVE SOLUTION OF A SYSTEM OF LINEAR EQUATIONS, 151

3Expansion of Functions in Series of Chebyshev Polynomials

3.1Polynomials in Chebyshev Form,155   
3.2Evaluating Polynomials in Chebyshev Form, 156 Exercises 3.2.1-3.2.5,159   
3.3 Chebyshev Series,161   
3.4 The Relationship of ${ \pmb S } _ { \pmb { n } }$ to $E _ { n }$ ，166 Exercises 3.4.1-3.4.7, 168 Exercises 3.4.8-3.4.12, 179

3.5The Evaluation of Chebyshev Coefficients, 180 Exercises 3.5.1-3.5.4, 187

3.6An Optimal Property of Chebyshev Expansions, 188

4Iterative Properties and Some Remarks About the Graphs of the $\pmb { T _ { \pmb { n } } }$

4.1 Permutable Polynomials,192 Exercises 4.1.1-4.1.9,196   
4.2Ergodic and Mixing Properties,200   
4.3 The“White" Curves and Intersection Points of Pairs of Chebyshev Polynomials, 208

5Some Algebraic and Number Theoretic Properties of the Chebyshev Polynomials

5.1The Discriminant of the Chebyshev Polynomials,217 Exercises 5.1.1.-5.1.4, 219

5.2The Factorization of the Chebyshev Polynomials into Polynomials with Rational Coefficients, 220

1． Preliminary Definitions and Results,220 Exercises 5.2.1.-5.2.23,221

2.The Irreducibility of the Cyclotomic Polynomials, 224 Exercises 5.2.24-5.2.25， 226

3．The Factorization of the Chebyshev Polynomials Over $\mathbb { Q }$ ，227 Exercises 5.2.26-5.2.29,230

5.3Some Number Theoretic Properties of the Chebyshev Polynomials, 231

1． Pell's Equation, 231   
2. Fermat's Theorem for the Chebyshev Polynomials, 232   
3 $( \mathcal { U } _ { n } ( x ) , \mathcal { U } _ { m } ( x ) ) = \mathcal { U } _ { ( m , n ) } ( x ) ,$ 232

References

Glossary of Symbols

Index

# CHEBYSHEV POLYNOMIALS

#

# DEFINITIONS AND SOME ELEMENTARY PROPERTIES

# 1.1.Definition of the Chebyshev Polynomials

This book is about polynomials. Let us recal that a polynomial is a function $p ( x )$ which can be written in the form

$$
p ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n } .
$$

We shall suppose that, unless otherwise indicated, $a _ { 0 } , \ldots , a _ { n }$ are real numbers and $\pmb { x }$ is a real variable. If $\pmb { a _ { n } \neq 0 }$ , then we say that $\pmb { p }$ is a polynomial of degree $\pmb { n . \dag }$ We shall often be interested in the set of polynomials whose degree does not exceed $\pmb { n } .$ 、This set is denoted by $\mathcal { P } _ { n } \mathrm { : }$ i.e., if $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { k } x ^ { k }$ and $k \leqslant n ,$ then

$$
\pmb { p } \in \mathscr { P } _ { n } .
$$

Polynomials have many agreeable properties. They can be diferentiated as often as desired for any value of $\mathbf { x } ,$ , and can be integrated over any interval. Moreover, they are “simple” in the sense that $p ( x )$ is completely specified by the $n + 1$ numbers $a _ { 0 } , \ldots , a _ { n }$ .It is this finiteness that makes polynomials particularly suitable as approximations to more complicated functions.

Consider the function

$$
T _ { n } ( x ) = \cos n \theta ,
$$

fThus nonzero constants are polynomials of degree zero. Zero is in the anomalous position of being a polynomial without a degree. We remedy this situation by assigning the degree $^ { - 1 }$ to the polynomial $\pmb { p } = \pmb { 0 }$

where $\pmb { n }$ is a nonnegative integer, $\boldsymbol { x } = \cos { \theta }$ and $0 \leqslant \theta \leqslant \pi$ As $\pmb \theta$ increases from 0 to $\pmb { \pi } , \pmb { x }$ decreases from 1 to $^ { - 1 }$ .The function $T _ { n } ( x )$ is defined by (1.2) on the interval $- 1 \leqslant x \leqslant 1 .$ ，which we also denote by $\pmb { I }$ ; i.e., given $\pmb { x } \in \mathbf { I }$ we find the unique value of $\theta = \operatorname { a r c } \cos x$ which satisfies $0 \leqslant \theta \leqslant \pi$ and $T _ { n } ( x )$ has the value cos n0. Thus $T _ { n } ( x )$ is a single-valued function defined on $\pmb { I }$ , which may be written

$$
T _ { n } ( x ) = \cos n ( \operatorname { a r c } \cos x ) ,
$$

where $0 \leqslant \operatorname { a r c c o s } x \leqslant \pi .$

We recall that

$$
e ^ { i \theta } = \cos \theta + i \sin \theta
$$

and

$$
e ^ { i n \theta } = ( \cos \theta + i \sin \theta ) ^ { n } = \cos n \theta + i \sin n \theta .
$$

By the binomial expansion

$$
\begin{array} { c } { { ( \cos \theta + i \sin \theta ) ^ { n } = \cos ^ { n } \theta + { \binom { n } { 1 } } \cos ^ { n - 1 } \theta ( i \sin \theta ) } } \\ { { + { \binom { n } { 2 } } \cos ^ { n - 2 } \theta ( i ^ { 2 } \sin ^ { 2 } \theta ) + \cdots + { \binom { n } { n } } ( i \sin \theta ) ^ { n } . } } \end{array}
$$

Equating the real parts of the last equation of (1.4), we obtain

$$
\begin{array} { c } { { \cos n \theta = \cos ^ { n } \theta - { \binom { n } { 2 } } \cos ^ { n - 2 } \theta \sin ^ { 2 } \theta + { \binom { n } { 4 } } \cos ^ { n - 4 } \theta \sin ^ { 4 } \theta + \cdots } } \\ { { + ( - 1 ) ^ { [ n / 2 ] } { \binom { n } { 2 [ n / 2 ] } } \cos ^ { n - 2 [ n / 2 ] } \theta \sin ^ { 2 [ n / 2 ] } \theta . { \dagger } } } \end{array}
$$

Note that only even powers of $\sin \theta$ occur in (1.5). We therefore make the substitution $\sin ^ { 2 } \theta = 1 - \cos ^ { 2 } \theta$ in (1.5) and obtain

$$
\cos n \theta = \sum _ { q = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { q } { \binom { n } { 2 q } } \cos ^ { n - 2 q } \theta { \binom { q } { k = 0 } } ^ { k } { \binom { q } { k } } \cos ^ { 2 k } \theta \bigg ) .
$$

The right-hand side of (1.6) is a polynomial in $\scriptstyle x = \cos \theta ,$ ,and so our function $T _ { n } ( x ) _ { \mathrm { { \bar { \it ~ ( ~ 1 ~ ) ~ } } } }$ ，defined in (1.3), is a polynomial. We proceed to determine its

t[y] means the greatest integer not exceeding y; e.g., if $\pmb { n }$ is even $[ n / 2 ] = n / 2 ,$ whereas if $\pmb { n }$ is odd $[ n / 2 ] = ( n - 1 ) / 2$

coefficients. The right-hand side of (1.6) is a“triangular” sum; namely, if we write

$$
A _ { q } = ( - 1 ) ^ { q } { \binom { n } { 2 q } } \cos ^ { n - 2 q } \theta , q = 0 , . . . , \left[ { \frac { n } { 2 } } \right]
$$

and

$$
B _ { k , q } = ( - 1 ) ^ { k } { \binom { q } { k } } \cos ^ { 2 k } \theta , \qquad k = 0 , 1 , \ldots , q ,
$$

then

$$
\begin{array} { r l } & { \cos n \theta = A _ { 0 } B _ { 0 , 0 } } \\ & { \phantom { = } + A _ { 1 } B _ { 0 , 1 } + A _ { 1 } B _ { 1 , 1 } } \\ & { \phantom { = } + A _ { 2 } B _ { 0 , 2 } + A _ { 2 } B _ { 1 , 2 } + A _ { 2 } B _ { 2 , 2 } } \\ & { \phantom { = } + } \\ & { \phantom { = } \vdots } \\ & { \phantom { = } + A _ { [ n / 2 ] } B _ { 0 , [ n / 2 ] } + \cdots + A _ { [ n / 2 ] } B _ { [ n / 2 ] , [ n / 2 ] } . } \end{array}
$$

Let us add up the right-hand side of(1.7) by stripping off successive diagonals. We then obtain

$$
{ \begin{array} { l } { \cos n \theta = ( A _ { 0 } B _ { 0 , 0 } + A _ { 1 } B _ { 1 , 1 } + \cdots + A _ { [ n / 2 ] } B _ { [ n / 2 ] , [ n / 2 ] } ) } \\ { \qquad + ( A _ { 1 } B _ { 0 , 1 } + A _ { 2 } B _ { 1 , 2 } + \cdots + A _ { [ n / 2 ] } B _ { [ n / 2 ] - 1 , [ n / 2 ] } ) } \\ { \qquad + } \\ { \qquad \vdots } \\ { \qquad \vdots } \\ { \qquad + ( A _ { [ n / 2 ] - 1 } B _ { 0 , [ n / 2 ] - 1 } + A _ { [ n / 2 ] } B _ { 1 , [ n / 2 ] } ) } \\ { \qquad + A _ { [ n / 2 ] } B _ { 0 , [ n / 2 ] } ; } \end{array} }
$$

or, by replacing the $A _ { q }$ and $B _ { k , q }$ with what they stand for

$$
\cos n \theta = \sum _ { k = 0 } ^ { [ n / 2 ] } { \biggl ( } ( - 1 ) ^ { k } \sum _ { j = k } ^ { [ n / 2 ] } { \binom { n } { 2 j } } { \binom { j } { k } } { \biggr ) } \cos ^ { n - 2 k } \theta .
$$

Equation (1.8) reveals that $T _ { n } ( x )$ is a polynomial of degree m. m If we write

$$
T _ { n } ( x ) = t _ { 0 } ^ { ( n ) } + t _ { 1 } ^ { ( n ) } x + \cdots + t _ { n } ^ { ( n ) } x ^ { ( n ) } ,
$$

we deduce from (1.8) that

$$
\begin{array} { c } { { t _ { n - ( 2 k + 1 ) } ^ { ( n ) } = 0 , \qquad k = 0 , . . . , \biggl [ \displaystyle \frac { n - 1 } { 2 } \biggr ] , } } \\ { { \nonumber } } \\ { { t _ { n - 2 k } ^ { ( n ) } = ( - 1 ) ^ { k } \sum _ { j = k } ^ { [ n / 2 ] } { \binom { n } { 2 j } \binom { j } { k } } , \qquad k = 0 , . . . , \biggl [ \displaystyle \frac { n } { 2 } \biggr ] . } } \end{array}
$$

Thus $T _ { n } ( x ) ,$ .which was defined in (1.2) by its values in $I _ { : }$ ,turns out to be a polynomial of degree ${ \pmb n } _ { \pmb { \imath } }$ ，hence is defined for all $\pmb { x }$ (indeed for all complex numbers $\pmb { x }$ . $\pmb { T _ { n } } ( \pmb { x } )$ is called the Chebyshev polynomial of degree n. For each nonnegative integer $\pmb { n }$ the Chebyshev polynomial of degree $\pmb { n }$ is given explicitly by formulas (1.9) and (1.10). Let us list the first few Chebyshev polynomials obtained from (1.9) and (1.10):

$$
\begin{array} { l c r } { { T _ { 0 } ( x ) = 1 ; \qquad T _ { 1 } ( x ) = x ; \qquad T _ { 2 } ( x ) = 2 x ^ { 2 } - 1 ; } } \\ { { T _ { 3 } ( x ) = 4 x ^ { 3 } - 3 x ; \qquad T _ { 4 } ( x ) = 8 x ^ { 4 } - 8 x ^ { 2 } + 1 ; } } \\ { { T _ { 5 } ( x ) = 1 6 x ^ { 5 } - 2 0 x ^ { 3 } + 5 x . } } \end{array}
$$

$T _ { 0 } , T _ { 1 } , . . . , T _ { 5 }$ are graphed in Figure 1.1.

![](images/0734715985482fc92155e4dcc735c1db95008197a9844eac62794ab72e948af3.jpg)  
Figure 1.1.

The sequence of polynomials $\{ T _ { n } ( x ) \} _ { n = 0 } ^ { \infty }$ is named after the Russian mathematician P.L. Chebyshev (1821-1894) who first studied them. The collected works of this eminent savant are available in Russian and French (Tchebychef [1].) This book is devoted to the study of various properties of these polynomials.In using the notation $T _ { n } ( x )$ for the Chebyshev polynomial of degree n we are following traditional usage derived from another transliteration of the name Chebyshev in the form Tchebycheff or related forms.

# EXERCISES 1.1.1-1.1.6

# 1.1.1. Show that

$$
\begin{array} { r } { T _ { n } ( x ) = \frac { 1 } { 2 } [ ( x + \sqrt { x ^ { 2 } - 1 } ) ^ { n } + ( x - \sqrt { x ^ { 2 } - 1 } ) ^ { n } ] . } \end{array}
$$

Hint. Suppose that $\boldsymbol { x } \in \boldsymbol { I }$ and recall that cc $s n \theta = ( e ^ { i n \theta } + e ^ { - i n \theta } ) / 2$

1.1.2. If $\boldsymbol { x } \geqslant \boldsymbol { 1 }$ ，prove that

$$
T _ { n } ( x ) = \cosh n t ,
$$

where $\pmb { x } = \mathbf { c o s h } t$ ， $\pmb { t \geqslant 0 }$

As a consequence of (1.2) any trigonometric identities involving cos nθ can be carried over immediately to identities involving the Chebyshev polynomials.The following exercises illustrate this theme.In the absence of other instructions the reader should attempt to verify an exercise.

1.1.3. If ${ \pmb m } , { \pmb n }$ are nonnegative integers, then

$$
\begin{array} { r } { T _ { m } ( x ) T _ { n } ( x ) = \frac { 1 } { 2 } ( T _ { m + n } ( x ) + T _ { | m - n | } ( x ) ) . } \end{array}
$$

$$
\begin{array} { r } { \int T _ { n } ( x ) d x = \frac 1 2 \bigg ( \cfrac { T _ { n + 1 } ( x ) } { n + 1 } - \cfrac { T _ { n - 1 } ( x ) } { n - 1 } \bigg ) + C , \qquad n \geqslant 2 . } \end{array}
$$

1.1.5. $( T _ { m + n } ( x ) - 1 ) ( T _ { | m - n | } ( x ) - 1 ) = ( T _ { m } ( x ) - T _ { n } ( x ) ) ^ { 2 } .$

1.1.6. $T _ { m } ( T _ { n } ( x ) ) = T _ { m n } ( x )$ for all nonnegative integers $\pmb { m }$ and $\pmb { n }$

# 1.2. Some Simple Properties

Now that we have defined the Chebyshev polynomials and written down an explicit formula for them we proceed to investigate some of their simpler properties.

Formula (1.10) reveals that for even n only even powers of $\pmb { x }$ occur in $T _ { n } ( x ) ,$ whereas for odd $\pmb { n }$ only odd powers of $\pmb { x }$ occur. Thus for al nonnegative integers $\pmb { n }$

$$
T _ { n } ( - x ) = ( - 1 ) ^ { n } T _ { n } ( x ) ;
$$

i.e., $\pmb { T _ { n } } ( \pmb { x } )$ is an even function for even $\pmb { n }$ and an odd function for odd $\pmb { n }$

We also observe from (1.1O) that the nonzero coefficients of $T _ { n } ( x )$ are integers that alternate in sign, the leading coeffcient, $t _ { n } ^ { ( n ) } = t _ { n } , \dag$ being positive. Indeed, if $n > 0 , t _ { n } ^ { ( n ) }$ has a particularly simple form for

$$
t _ { n } = \sum _ { j = 0 } ^ { [ n / 2 ] } { \binom { n } { 2 j } } = { \frac { 1 } { 2 } } \{ ( 1 + 1 ) ^ { n } + ( 1 - 1 ) ^ { n } \} = 2 ^ { n - 1 } .
$$

For some purposes the polynomial with leading coefficient 1,

$$
\begin{array} { c } { { \displaystyle \widetilde { T } _ { n } ( x ) = 2 ^ { 1 - n } T _ { n } ( x ) = x ^ { n } + 2 ^ { 1 - n } \sum _ { j = 0 } ^ { n - 1 } t _ { j } x ^ { j } , \qquad n > 0 , } } \\ { { ( \widetilde { T } _ { 0 } ( x ) = 1 ) , } } \end{array}
$$

is useful.

We turn next to the significant points of $T _ { n } ( x ) .$ .These are the zeros and extreme of $\pmb { T _ { n } }$ . The zeros are, of course, simply the values of $\pmb { x }$ for which $\begin{array} { r } { T _ { n } ( x ) = 0 . } \end{array}$ Since $T _ { n } ( x ) = \cos n \theta$ and cos ${ \pmb n } \pmb \theta _ { j } = 0$ for

$$
\theta _ { j } = \theta _ { j } ^ { ( n ) } = \frac { ( 2 j - 1 ) } { n } \frac \pi 2 , \qquad j = 1 , \ldots , n ,
$$

we see that the points

$$
\xi _ { j } = \xi _ { j } ^ { ( n ) } = \cos \theta _ { j } ^ { ( n ) } = \cos \frac { ( 2 j - 1 ) } { n } \frac { \pi } { 2 } , ~ j = 1 , \ldots , n
$$

are all distinct, lie in $I ,$ and satisfy

$$
T _ { n } ( \xi _ { j } ) = 0 , \qquad j = 1 , \ldots , n .
$$

(Once again we omit superscripts when n is fixed.) Since $T _ { n } ( x )$ is of degree $\pmb { n } ,$ it has exactly n zeros and so the numbers $\xi _ { j } ^ { ( n ) } , j = 1 , \ldots , n ,$ defined in (1.17), are all the zeros of $T _ { n } ( x )$

It is clear from (1.2) that if $\boldsymbol { x } \in \boldsymbol { I }$

$$
- 1 \leqslant T _ { n } ( x ) \leqslant 1 .
$$

The points of I at which $\vert T _ { n } ( x ) \vert = 1$ we call the extrema of $T _ { n } ( x )$ . We know that cos $k \pi = ( - 1 ) ^ { k }$ for any integer $k ;$ hence if

$$
\varphi _ { k } = \varphi _ { k } ^ { ( n ) } = \frac { k \pi } { n } , \qquad k = 0 , 1 , \ldots , n ,
$$

$\dagger \mathbf { W } \mathbf { e }$ have written the coefficient of $x ^ { k }$ in $T _ { n } ( x ) , t _ { k } ^ { ( n ) }$ ，with the superscript $\mathbf { \rho } ( n )$ ,to exhibit the fact that the Chebyshev polynomials of different degree have independent sets of coefficients,but when the degree of the polynomial is fixed in a discussion and no confusion results we simply drop the superscript.

the points

$$
\eta _ { k } = \eta _ { k } ^ { ( n ) } = \cos \varphi _ { k } ^ { ( n ) } = \cos \frac { k \pi } { n } , \qquad k = 0 , 1 , \dots , n ,
$$

are all distinct, lie in $I _ { \ast }$ , and satisfy

$$
T _ { n } ( \eta _ { k } ) = ( - 1 ) ^ { k } , \qquad k = 0 , \ldots , n .
$$

The points $\pmb { \eta _ { 0 } , \dots , \pmb { \eta _ { n } } }$ are the extrema of $\pmb { T _ { n } } ( \pmb { x } ) .$ It is clear that, since $| T _ { n } ( x ) | \leqslant 1$ for $\boldsymbol { x } \in \boldsymbol { I }$ ，the points $\eta _ { 1 } , \dotsc , \eta _ { n - 1 }$ which lie in the interior of $\pmb { I }$ are relative extrema of $T _ { n } ( x )$ so that

$$
T _ { n } ^ { \prime } ( \eta _ { k } ) = 0 , \qquad k = 1 , \ldots , n - 1 .
$$

Since $T _ { \pmb { n } } ^ { \prime }$ is a polynomial of degree $n - 1$ , all its zeros are $\pmb { \eta _ { 1 } } , \dotsc , \pmb { \eta _ { n - 1 } }$ and so the points $\eta _ { 0 } = 1$ and $\eta _ { n } = - 1$ are not relative extrema of $T _ { n } ( x ) .$

On differentiating $T _ { n } ( x ) = \cos n \theta$ with respect to $\pmb { x }$ we obtain

$$
T _ { n } ^ { \prime } ( x ) = \left( { \frac { d } { d \theta } } \cos n \theta \right) { \frac { d \theta } { d x } } = { \frac { - n \sin n \theta } { - \sin \theta } } = n { \frac { \sin n \theta } { \sin \theta } } , \qquad x = \cos \theta .
$$

The polynomial of degree ${ \pmb n } - 1$

$$
U _ { n - 1 } ( x ) = \frac { 1 } { \mathfrak { n } } ~ T _ { n } ^ { \prime } ( x ) = \frac { \sin n \theta } { \sin \theta } , \qquad x = \cos \theta ,
$$

is calledthe Chebyshevpolynomialofthesecond kind.Its zerosare $\eta _ { 1 } , \dotsc , \eta _ { n - 1 }$ and its explicit form is easily obtained by differentiating (1.9) and dividing by $\pmb { n } .$

Because we refer frequently to zeros and extrema of $T _ { n } ( x ) ,$ the reader should note that both $\xi _ { 1 } , \ldots , \xi _ { n }$ and $\pmb { \eta _ { 0 } } , \dotsc , \pmb { \eta _ { n } }$ move from right to left in $\pmb { I }$ with increasing index.

# EXERCISES 1.2.1-1.2.23

1.2.1. Show that if ${ \pmb n } = 2 m$

$$
T _ { n } ( x ) = \tau _ { m } ( x ^ { 2 } ) ,
$$

and if $n = 2 m + 1$

$$
T _ { n } ( x ) = x \tau _ { m } ( x ^ { 2 } ) ,
$$

where

$$
\tau _ { m } ( t ) = \sum _ { j = 0 } ^ { m } { \left( - 1 \right) ^ { j } { \binom { n } { 2 j } } t ^ { m - j } ( 1 - t ) ^ { j } } .
$$

1.2.2. Find all the solutions of $x = T _ { n } ( x ) , n = 2 , 3 , \ldots$

1.2.3. Verify that

$$
\begin{array} { l } { { T _ { n } ^ { \prime } ( \xi _ { j } ) = ( - 1 ) ^ { j - 1 } \displaystyle \frac { n } { \sin { ( 2 j - 1 ) } ( \pi / 2 n ) } , \qquad j = 1 , \ldots , n , } } \\ { { { } } } \\ { { = ( - 1 ) ^ { j - 1 } \displaystyle \frac { n } { \sqrt { 1 - \xi _ { j } ^ { 2 } } } . \qquad } } \end{array}
$$

# 1.2.4. Show that

$$
| T _ { n } ^ { \prime } ( x ) | \leqslant n ^ { 2 } , \qquad x \in I ,
$$

with equality holding only if $\pmb { \mathrm { 1 } } = \pmb { \mathrm { 1 } } ( \pmb { n } \geqslant 2 )$

Hint. Use the representation (1.22) and mathematical inducation on $\pmb { n }$

1.2.5. Show that if $\begin{array} { r } { n = 2 r k + m ; k , r \geqslant 0 , } \end{array}$

$$
T _ { n } ( \xi _ { j } ^ { ( k ) } ) = ( - 1 ) ^ { r } T _ { | m | } ( \xi _ { j } ^ { ( k ) } ) .
$$

1.2.6. Show that any polynomial $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ can be written $p ( x ) = b _ { 0 } + b _ { 1 } T _ { 1 } ( x ) + \cdots + b _ { n } T _ { n } ( x )$ and $b _ { n } = 2 ^ { - ( n - 1 ) } a _ { n } , n \geqslant 1$

# 1.2.7. Show that

$$
\begin{array} { r } { T _ { n } ( \xi _ { j } ^ { ( n + 1 ) } ) = ( - 1 ) ^ { j - 1 } \sqrt { 1 - ( \xi _ { j } ^ { ( n + 1 ) } ) ^ { 2 } } , } \\ { n = 0 , 1 , 2 , . . . ; j = 1 , 2 , . . . , n + 1 , } \end{array}
$$

and

$$
T _ { n + 1 } ( \xi _ { j } ^ { ( n ) } ) = ( - 1 ) ^ { j } \sqrt { 1 - ( \xi _ { j } ^ { ( n ) } ) ^ { 2 } } , \qquad n = 1 , 2 , \ldots , j = 1 , 2 , \ldots , n .
$$

# 1.2.8. Show that

$$
T _ { n } ^ { \prime \prime } ( \xi _ { j } ) = ( - 1 ) ^ { j - 1 } n \frac { \xi _ { j } } { ( 1 - \xi _ { j } ^ { 2 } ) ^ { 3 / 2 } } .
$$

1.2.9. Show that

$$
\sum _ { j = 1 } ^ { n } \xi _ { j } ^ { ( n ) } = 0 .
$$

1.2.10. Show that

$$
T _ { n } ^ { \prime } ( x ) = \sum _ { i = 1 } ^ { n } { \frac { T _ { n } ( x ) } { x - \xi _ { i } } } .
$$

1.2.11. Show that for $\pmb { n } \geqslant 2$ the only solution of $T _ { n } ( x ) = T _ { n } ^ { \prime } ( x )$ that satisfies $\mathbf x > 1$ lies in $( n , n + 1 / 2 n )$

1.2.12. Suppose $p ( x ) = ( T _ { n } ( x ) ) ^ { 2 k + 1 }$ in Exercise 1.2.6 and that

$$
( T _ { n } ( x ) ) ^ { 2 k + 1 } = B _ { 0 } + B _ { 1 } T _ { 1 } ( x ) + \cdots + B _ { n ( 2 k + 1 ) } T _ { n ( 2 k + 1 ) } ( x ) .
$$

Show that $B _ { 0 } = B _ { 1 } = \cdots = B _ { n - 1 } = 0$

Hint. Use the fact that Exercise 1.1.3 implies that $T _ { n } ^ { 2 k } = ( ( 1 + T _ { 2 n } ) / 2 ) ^ { k } ,$ and then use Exercise 1.1.3 repeatedly.

# 1.2.13. Show that

$$
U _ { k } ( x ) = 2 \sum _ { j = 0 } ^ { [ k / 2 ] } T _ { k - 2 j } ( x ) - { \frac { ( - 1 ) ^ { k } + 1 } { 2 } } , \qquad k = 0 , 1 , \ldots .
$$

$$
\frac { U _ { k } ( x ) + U _ { k - 1 } ( x ) } { 2 } = \frac { \ d H _ { 1 } } { \ d z ^ { 2 } } + T _ { 1 } ( x ) + \dots + T _ { k } ( x ) .
$$

Hint. sin Acos $B = { \textstyle \frac { 1 } { 2 } } [ \sin \left( A - B \right) + \sin \left( A + B \right) ] .$

1.2.14. If $U _ { n } ( x ) = u _ { 0 } + u _ { 1 } x + \cdots + u _ { n } x ^ { n }$ then $u _ { n } = 2 ^ { n }$

1.2.15. (a) （c） $\begin{array} { l } { { \displaystyle { | \begin{array} { l } { U _ { n } ( x ) - U _ { n - 2 } ( x ) = 2 T _ { n } ( x ) , } } \\ { { | T _ { n } ( x ) = U _ { n } ( x ) - x U _ { n - 1 } ( x ) , } } \\ { { T _ { k - 1 } ( x ) - T _ { k + 1 } ( x ) = 2 ( 1 - x ^ { 2 } ) U _ { k - 1 } ( x ) , } } \end{array} } k = 1 , 2 , \ldots }  \\ { { \displaystyle { | \begin{array} { l } { { ( 1 + x ) U _ { k } ( x ) = 1 + 2 T _ { 1 } ( x ) + \cdots + 2 T _ { k } ( x ) + T _ { k + 1 } ( x ) , } } \\ { { U _ { n m - 1 } ( x ) = U _ { m - 1 } ( T _ { n } ( x ) ) U _ { n - 1 } ( x ) , } } \end{array} } k = 0 , 1 , \ldots } } \\ { { \displaystyle { U _ { n } ( x ) = \sum _ { j = 0 } ^ { n } x ^ { \prime } T _ { n - j } ( x ) , } } } \\ { { \displaystyle { ( n + 1 ) T _ { n } ( x ) = \sum _ { j = 0 } ^ { n } \left( 2 T _ { j } ( x ) - x ^ { j } \right) T _ { n - j } ( x ) . } } } \\ { { \displaystyle { ~ 2 \sum _ { j = 0 } ^ { n } T _ { j } ( x ) T _ { n - j } ( x ) = U _ { n } ( x ) + ( n + 1 ) T _ { n } ( x ) . } } } \end{array}$   
d   
（e)   
(f）   
（g)   
(b)   
i $T _ { n } ^ { 2 } ( x ) - ( x ^ { 2 } - 1 ) U _ { n - 1 } ^ { 2 } ( x ) = 1 .$

1.2.16. Let $s _ { k } ^ { ( n ) } = t _ { 0 } ^ { ( n ) } + t _ { 1 } ^ { ( n ) } + \cdots + t _ { k } ^ { ( n ) }$ $\pmb { k = 0 , 1 , \dots , n } .$ If $q ( x ) = s _ { 0 } + s _ { 1 } x + \cdots + s _ { n } x ^ { n } ,$ show that $p ( x ) = ( 1 - x ) q ( x ) = T _ { n } ( x ) - x ^ { n + 1 }$

1.2.17. Show that $p ( x ) = T _ { n } ( x ) - x ^ { n + 1 }$ has at least $[ n / 2 ]$ distinct zeros in (0,1].

1.2.18. Show that $p ( x ) = T _ { n } ( x ) - x ^ { n + 1 }$ has $[ n / 2 ]$ positive zeros other than ${ \boldsymbol { x } } = { \boldsymbol { 1 } }$

Hint. According to Descartes’rule of signs,if $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n + 1 } x ^ { n + 1 }$ has $\pmb { N }$ positive zeros and there are $\pmb { W }$ changes of sign in the sequence $a _ { 0 } , a _ { 1 } , \ldots , a _ { n + 1 } ,$ then $W - N$ is either zero or a positive even number; but, in view of (1.10), $W = [ n / 2 ] + 1$

1.2.19. Show that the numbers $s _ { n - 2 j } ^ { ( n ) } , j = 0 , . . . , [ n / 2 ] ,$ defined in Exercise 1.2.16, alternate in sign.

Hint. Use Descartes' rule of signs again, this time starting with information about the number of zeros of ${ \pmb q } ( { \pmb x } ) .$

# 1.2.20. Show that

$$
U _ { n } ( x ) = { \frac { ( x + { \sqrt { x ^ { 2 } - 1 } } ) ^ { n + 1 } - ( x - { \sqrt { x ^ { 2 } - 1 } } ) ^ { n + 1 } } { 2 { \sqrt { x ^ { 2 } - 1 } } } } .
$$

Let $R _ { n } ( x ) = x ^ { n } T _ { n } ( 1 / x ) ,$ $\pmb { n = 0 }$ ,1,.... We call $\pmb { R _ { n } }$ the reversal of $T _ { \pmb { n } }$ since its coefficients are the coefficients of $T _ { \pmb { n } }$ in reverse order; e.g., $R _ { 0 } ( x ) = 1 , R _ { 1 } ( x ) = 1 , R _ { 2 } ( x ) = 2 - x ^ { 2 }$ ， $R _ { 3 } ( x ) = 4 - 3 x ^ { 2 }$ ... . Notice that $R _ { n } \in \mathcal { P } _ { n }$ but while $\pmb { R } _ { 2 k }$ is of degree 2k, $\pmb { R _ { 2 k + 1 } }$ is also of degree $^ { 2 k }$

# 1.2.21. Show that

$$
R _ { n } ( x ) = \sum _ { j = 0 } ^ { [ n / 2 ] } { \binom { n } { 2 j } } ( 1 - x ^ { 2 } ) ^ { j } .
$$

Hint.Use Exercise 1.2.1.

1.2.22. For $\pmb { n = 0 , 1 , \dots }$

(a) $\pmb { R _ { n } } ( \pmb { x } )$ is an even function of $\pmb { x }$   
(b) $1 \leqslant R _ { n } ( x ) \leqslant 2 ^ { n - 1 }$ ,xeI.   
（c） $\pmb { R _ { n } } ( \pmb { x } )$ is monotone increasing from 1 to $2 ^ { n - 1 }$ in $- 1 \leqslant x \leqslant 0$ . (Hence monotone decreasing from $2 ^ { n - 1 }$ to 1 in $0 \leqslant x \leqslant 1 .$   
(d) $R _ { n } ( x ) \leqslant R _ { n + 1 } , x \in I .$

1.2.23. The polynomial $T _ { n } ( z ) - R _ { n } ( z )$ has all its zeros on the unit circle, $| z | = 1$

Hint. If $z$ is a zero of $T _ { n } - { \pmb R _ { n } }$ then

$$
\frac { T _ { n } ( z ) } { z ^ { n } T _ { n } \left( \frac { 1 } { z } \right) } = 1 .
$$

Now use the factorization $T _ { n } ( z ) = 2 ^ { n - 1 } ( z - \xi _ { 1 } ) \cdots ( z - \xi _ { n } ) .$

# 1.3. Polynomial Interpolation at the Zeros and Extrema

The zeros and extrema of the Chebyshev polynomials play an important role in the theory of polynomial interpolation. The setting is the following.

Suppose $f ( x )$ is a continuous function defined on $\pmb { I }$ ，which we wish to approximate by a polynomial of degree at most $\pmb { k }$ . As a measure of how good an approximation of $f ( x )$ is provided by a given $\pmb { p } \in \mathcal { P } _ { \pmb { k } }$ we adopt the uniform norm

$$
\| f - p \| = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | f ( x ) - p ( x ) | ;
$$

i.e., the measure of approximation is the greatest distance between $f ( x )$ and $p ( { \boldsymbol { x } } )$ as $\pmb { x }$ runs through I. A rather natural way to seek polynomial approximations to $f ( x )$ is to sample $f ( x )$ at distinct points of I, $\boldsymbol { x } _ { 1 } , \ldots , \boldsymbol { x } _ { n }$ ,and try to find a polynomial that takes on the same values as $f ( x )$ at $x _ { 1 } , \ldots , x _ { n }$ Such a polynomial is said to interpolate $f ( x )$ at the nodes $x _ { 1 } , \ldots , x _ { n }$ As a mater of fact, we shall now show that, given distinct points of I, $x _ { 1 } , \ldots , x _ { n }$ it is easy to construct a unique $\pmb { p } \in \mathcal { P } _ { { \pmb { n } } - 1 }$ that interpolates $f ( x )$ at $x _ { 1 } , \ldots , x _ { n }$

We wish to construct a polynomial that passes through the points $( x _ { 1 } , f ( x _ { 1 } ) ) , ( x _ { 2 } , f ( x _ { 2 } ) ) , \ldots , ( x _ { n } , f ( x _ { n } ) ) .$

Let us put

$$
l _ { j , n } ( x ) = l _ { j } ( x ) = { \frac { ( x - x _ { 1 } ) ( x - x _ { 2 } ) \cdots ( x - x _ { j - 1 } ) ( x - x _ { j + 1 } ) \cdots ( x - x _ { n } ) } { ( x _ { j } - x _ { 1 } ) ( x _ { j } - x _ { 2 } ) \cdots ( x _ { j } - x _ { j - 1 } ) ( x _ { j } - x _ { j + 1 } ) \cdots ( x _ { j } - x _ { n } ) } } , \quad \quad 
$$

$l _ { j } ( \boldsymbol { x } )$ is a polynomial of degree ${ \pmb n } - 1$ that satisfies

$$
l _ { j } ( x _ { i } ) = \left\{ { \begin{array} { l l } { 0 , } & { \quad j \neq i , } \\ { 1 , } & { \quad j = i , } \end{array} } \right. \quad i , j = 1 , \ldots , n ,
$$

as is readily evident from (1.25); $l _ { 1 , 1 }$ is identically 1 and $l _ { 1 } ( x ) , \ldots , l _ { n } ( x )$ are called the fundamental polynomials for interpolation at $x _ { 1 } , \ldots , x _ { n }$

$$
L _ { n - 1 } ( x ) = f ( x _ { 1 } ) l _ { 1 } ( x ) + f ( x _ { 2 } ) l _ { 2 } ( x ) + \dotsb + f ( x _ { n } ) l _ { n } ( x )
$$

is a polynomial of degree at most ${ \pmb n } - 1$ that passes through the points in question. Moreover, if $\pmb { p } \in \mathcal { P } _ { { \pmb n } - 1 }$ and $\pmb { p }$ interpolates $f$ at $x _ { 1 } , \ldots , x _ { n }$ ，then $\begin{array} { r } { p = L _ { n - 1 } , } \end{array}$ ,for if $p ( x _ { j } ) = f ( x _ { j } ) , j = 1 , . . . , n$ then

$$
L _ { n - 1 } ( x _ { j } ) - p ( x _ { j } ) = 0 , \qquad j = 1 , \ldots , n ,
$$

and the polynomial $L _ { n - 1 } - p \in \mathcal { P } _ { n - 1 }$ has n zeros which means that $L _ { n - 1 } = p$ Thus $L _ { n - 1 } ( x ) ,$ ，as defined in (1.27), is the unique member of $\mathcal { P } _ { n - 1 }$ that interpolates $f ( x )$ at $x _ { 1 } , \ldots , x _ { n }$ .This unique interpolating polynomial, when writen in the form (1.27), is called the Lagrange interpolating polynomial (to $f ( x )$ at $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { n } )$

If we start with an infinite triangular array of nodes,

$$
\begin{array} { r l } & { x _ { 1 } ^ { ( 1 ) } } \\ & { x _ { 1 } ^ { ( 2 ) } , x _ { 2 } ^ { ( 2 ) } } \\ { X \colon } & { \colon } \\ & { x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { n } ^ { ( n ) } } \\ & { \vdots } \end{array}
$$

where for $\pmb { n = 1 , 2 , \dots }$ each $x _ { j } ^ { ( n ) } \in I , j = 1 , . . . , n ,$ the rows of $\pmb { X }$ determine a sequence of interpolating polynomials

$$
\{ L _ { k } \} _ { k = 0 } ^ { \infty } ,
$$

the polynomial $L _ { n - 1 } \in \mathcal { P } _ { n - 1 }$ being the unique interpolating polynomial determined by the nth row. The notation $L _ { k }$ for a member of the sequence (1.29) is shorthand for $L _ { k } ( f , X ; x ) ,$ in which the subscript indicates an element of $\mathcal { P } _ { k }$ obtained by interpolating the first argument $f ( x )$ at the entries in the $( k + 1 ) { \mathsf { s t } }$ row of the second argument $\pmb { X }$

Given $\pmb { X }$ ,the sequence (1.29) provides us with approximating polynomials to $f ( x )$ on $I .$ How good an approximation these polynomials are is, as we assumed, measured by the numbers

$$
M _ { k } = \| f - L _ { k } \| = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | f ( x ) - L _ { k } ( x ) | , \qquad k = 0 , 1 , 2 , \ldots .
$$

We wish to compare $M _ { k }$ with the best approximation possible by means of $\pmb { p } \in \mathcal { P } _ { \pmb { k } }$ . It is known (cf. Rivlin [1]) that there is a $\pmb { p } ^ { * } \in \mathcal { P } _ { \pmb { k } }$ that gives this best approximation; i.e., given $f ( x ) ,$

$$
\| f - p ^ { * } \| \leqslant \| f - p \| \quad { \mathrm { ~ f o r ~ a l l ~ } } p \in { \mathcal { P } } _ { k } .
$$

We put

$$
E _ { k } ( f ) = \| f - p ^ { * } \| .
$$

We can now prove a result comparing $M _ { k }$ with $\scriptstyle { E _ { k } }$ ·

Theorem 1.1.

$$
M _ { k } \leqslant E _ { k } \Bigg ( 1 + \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \sum _ { j = 1 } ^ { k + 1 } | l _ { j } ( x ) | \Bigg ) , \qquad k = 0 , 1 , \ldots .
$$

Proof. After subtracting and adding $\pmb { p } ^ { * }$ to $f - L _ { k }$ , we obtain

$$
| f ( x ) - L _ { k } ( f , X ; x ) | \leqslant | f ( x ) - p ^ { * } ( x ) | + | p ^ { * } ( x ) - L _ { k } ( f , X ; x ) | .
$$

Now, if $\pmb { p } \in \mathcal { P } _ { \pmb { k } }$

$$
L _ { k } ( p , X ; x ) = p ( x ) ,
$$

since $L _ { k } ( p , X ; x )$ is the unique interpolating polynomial to $p ( { \boldsymbol { x } } )$ in the $( k + 1 ) { \mathsf { s t } }$ row of $\pmb { X }$ and $\pmb { p }$ surely interpolates itself. Hence, in particular,

$$
p ^ { * } ( x ) = L _ { k } ( p ^ { * } , X ; x ) ,
$$

and in view of (1.27)

$$
\begin{array} { c } { { p ^ { * } ( x ) - { \cal L } _ { k } ( f , X ; x ) = { \cal L } _ { k } ( p ^ { * } , X ; x ) - { \cal L } _ { k } ( f , X ; x ) } } \\ { { { } } } \\ { { = { \cal L } _ { k } ( p ^ { * } - f , X ; x ) . } } \end{array}
$$

From (1.31) we obtain

$$
| f ( x ) - L _ { k } ( f , X ; x ) | \leqslant E _ { k } + | L _ { k } ( p ^ { * } - f , X ; x ) | ,
$$

but, in general, if $g ( x )$ is continuous on $I _ { : }$

$$
\vert L _ { k } ( g , X ; x ) \vert \leqslant \vert g ( x _ { 1 } ^ { ( k + 1 ) } ) l _ { 1 , k + 1 } ( X ; x ) \vert + \cdots + \vert g ( x _ { k + 1 } ^ { ( k + 1 ) } ) l _ { k + 1 , k + 1 } ( X ; x ) \vert
$$

(where $l _ { j , k + 1 } ( X ; x )$ is a full notation for (1.25) with the $( k + 1 )$ st row of $\pmb { X }$ as the nodes), and so

$$
| L _ { k } ( g , X ; x ) | \leqslant \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | g ( x ) | \quad \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \sum _ { j = 1 } ^ { k + 1 } | l _ { j } ( x ) | .
$$

If we apply (1.33) with $\pmb { \mathscr { g } } = \pmb { p } ^ { * } - \pmb { f }$ and note that

$$
E _ { k } = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | p ^ { \ast } ( x ) - f ( x ) | ,
$$

we obtain from (1.32)

$$
| f ( x ) - L _ { k } ( f , X ; x ) \leqslant E _ { k } { \Biggl ( } 1 + \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \sum _ { j = 1 } ^ { k + 1 } | l _ { j } ( x ) | { \Biggr ) } .
$$

The theorem now follows by choosing $\pmb { x }$ on the left-hand side of (1.34) so that $\lvert f ( x ) - L _ { k } ( f , X ; x ) \rvert = \lvert \lvert f - L _ { k } \rvert \rvert$

The function

$$
\lambda _ { k + 1 } ( X ; x ) = \sum _ { j = 1 } ^ { k + 1 } | l _ { j , k + 1 } ( X ; x ) | ,
$$

which appears in (1.30), is caled the Lebesgue function of order $k + 1$ of $\pmb { X }$ Note that it does not depend on $f ( x ) .$ . The quantity

$$
\Lambda _ { k + 1 } ( X ) = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \lambda _ { k + 1 } ( X ; x )
$$

is called the Lebesgue constant of order $k + 1$ of $\pmb { X }$ ; (1.30) may now be written

concisely as

$$
M _ { k } \leqslant E _ { k } ( 1 + \Lambda _ { k + 1 } ) , \qquad k = 0 , 1 , \ldots ,
$$

the various dependencies on $f$ and $\pmb { X }$ being tacitly understood as usual.

Since $E _ { k }$ depends on f and $k _ { \mathrm { { s } } }$ , but not on $\pmb { X }$ ,the effect on $M _ { k }$ of $\pmb { X }$ , insofar as (1.36) is informative, comes from the Lebesgue constant $\Lambda _ { k + 1 }$ .Formula tells us that the smaller $\Lambda _ { k } ( X ) ,$ the better the sequence of Lagrange imterpolating polynomials at the nodes of $\pmb { X }$ as uniform approximations off. It is a fact that there is an array of nodes $X ^ { * }$ such that

$$
\Lambda _ { k } ( X ^ { * } ) \leqslant \Lambda _ { k } ( X ) , \qquad k = 1 , 2 , 3 , \ldots ,
$$

for any array of nodes $\pmb { X }$ (see Rivlin [1; p.100]). The point of this digression on the topic of polynomial interpolation is that the zeros of the Chebyshev polynomials provide an array of nodes with“small" Lebesgue constants. We proceed now toward making this assertion more precise.

We shall observe at the end of this section that there exists a positive constant, $\pmb { c } _ { \mathrm { : } }$ ，such that

$$
\Lambda _ { k } ( X ) > { \frac { 2 } { \pi } } \log k + c , ~ k = 1 , 2 , . . . ,
$$

for any $\pmb { X }$ .A consequence of (1.37) is that $\Lambda _ { k } ( X ) \to \infty$ as $k \to \infty$ , a fact with the startling consequence (Faber [1]) that, given $\pmb { X }$ ,there exists a function, $f ( x ) ,$ continuous on $I ,$ , such that $\{ L _ { k } ( f , X ; x ) \}$ does not converge uniformly to $f ( x )$ (A proof of this result may be found in Rivlin [1].) Thus our original hope of approximating all continuous functions, using a fixed $\pmb { X }$ , turns out to be illusory. We shall show next, however, that

$$
\Lambda _ { k } ( T ) \leqslant { \frac { 2 } { \pi } } \log k + 1 , \qquad k = 1 , 2 , . . . ,
$$

where $_ { T }$ is the array whose $\pmb { k }$ th row is $\xi _ { 1 } ^ { ( k ) } , \ldots , \xi _ { k } ^ { ( k ) }$ , i.e., the zeros of $T _ { k } ( x ) .$ In view of (1.37) and (1.36), although $_ { T }$ may not be the best array of nodes for interpolation, it is a good choice.

Let us see what $L _ { n - 1 } ( f , T ; x )$ looks like. We remark first that if we put

$$
\omega ( x ) = ( x - x _ { 1 } ) ( x - x _ { 2 } ) \cdot \cdot \cdot ( x - x _ { n } ) ,
$$

then $l _ { j } ( x ) ,$ as defined in (1.25), can be writen as

$$
l _ { j } ( x ) = { \frac { \omega ( x ) } { ( x - x _ { j } ) \omega ^ { \prime } ( x _ { j } ) } } , \qquad j = 1 , . . . , n ,
$$

so that (1.27) becomes

$$
L _ { n - 1 } ( x ) = \omega ( x ) \sum _ { j = 1 } ^ { n } \frac { f ( x _ { j } ) } { ( x - x _ { j } ) \omega ^ { \prime } ( x _ { j } ) } .
$$

When $_ T$ is the array of nodes, $\omega ( x ) = \widetilde { T } _ { n } ( x )$ and so

$$
\begin{array} { l } { { \displaystyle { \cal L } _ { n - 1 } ( f , T ; x ) = T _ { n } ( x ) \sum _ { j = 1 } ^ { n } \frac { f ( \xi _ { j } ^ { ( n ) } ) } { ( x - \xi _ { j } ^ { ( n ) } ) T _ { n } ^ { \prime } ( \xi _ { j } ^ { ( n ) } ) } } \ ~ } \\ { { \displaystyle ~ = \frac { T _ { n } ( x ) } { n } \sum _ { j = 1 } ^ { n } ( - 1 ) ^ { j - 1 } \frac { f ( \xi _ { j } ) \sin { [ ( 2 j - 1 ) \pi ] } / 2 n } { ( x - \xi _ { j } ) } \ ~ } } \\ { { \displaystyle ~ = \frac { T _ { n } ( x ) } { n } \sum _ { j = 1 } ^ { n } ( - 1 ) ^ { j - 1 } \frac { f ( \xi _ { j } ) ( 1 - \xi _ { j } ^ { 2 } ) ^ { 1 / 2 } } { ( x - \xi _ { j } ) } , } } \end{array}
$$

where we have used Exercise 1.2.3.

If we use the trigonometric form, (1.41) becomes

$$
L _ { n - 1 } ( f , T ; \cos \theta ) = { \frac { \cos n \theta } { n } } \sum _ { j = 1 } ^ { n } { \bigl ( } - 1 { \bigr ) } ^ { j - 1 } { \frac { f ( \cos \theta _ { j } ) } { \cos \theta - \cos \theta _ { j } } } \sin \theta _ { j } ,
$$

and the Lebesgue function may be written

$$
\lambda _ { n } ( T ; x ) = \lambda _ { n } ( \cos \theta ) = { \frac { | \cos n \theta | } { n } } \sum _ { j = 1 } ^ { n } { \frac { \sin \theta _ { j } } { | \cos \theta - \cos \theta _ { j } | } } .
$$

To establish (1.38) we show first, following Ehlich and Zeller [2], that $\Lambda _ { n } ( T ) = \lambda _ { n } ( T ; 1 )$ for $\pmb { n } \geqslant 2$ (that $\lambda _ { 1 } ( T , 1 ) = \Lambda _ { 1 } ( T ) = 1$ is a trivial observation). To this end we need some information about trigonometric polynomials. A trigonometric polynomial of degree $k$ is a function

$$
t ( \theta ) = \sum _ { j = 0 } ^ { k } { \bigl ( } a _ { j } \cos j \theta + b _ { j } \sin j \theta { \bigr ) } ,
$$

with $a _ { k } ^ { 2 } + b _ { k } ^ { 2 } > 0 .$ .We suppose that, unless otherwise stated, the coefficients $a _ { 0 } , \dots , a _ { k } ; b _ { 0 } , \dots , b _ { k }$ are real numbers. The set of trigonometric polynomials of degree at most $\pmb { n }$ is denoted by $\mathcal { T } _ { n }$ .(The zero polynomial is arbitrarily assigned the degree -1.) A nonzero trigonometric polynomial of degree $\pmb { k }$ has at most $^ { 2 k }$ zeros in the interval $[ 0 , 2 \pi )$ ,where multiple zeros are counted as distinct; i.e., a zero of multiplicity $\pmb { m }$ is counted as m zeros.We leave this fact as an exercise (Exercise 1.3.13).

Let us put [cf. (1.16)]

$$
\theta _ { j } = ( 2 j - 1 ) \frac { \pi } { 2 n } , j = 0 , \pm 1 , \pm 2 , . . . ,
$$

and

$$
d _ { k } ( \theta ) = \frac { 1 } { 2 n } \frac { \sin n ( \theta - \theta _ { k } ) } { \tan \frac { 1 } { 2 } ( \theta - \theta _ { k } ) } , \qquad k = 0 , \pm 1 , \pm 2 , . . . ;
$$

then $d _ { k } ( \theta ) \in \mathcal { T } _ { n }$ . To verify this we observe that

$$
d _ { k } ( \theta ) = \frac { 1 } { 2 n } \frac { \sin 2 n ( \theta - \theta _ { k } ) / 2 } { \sin { ( \theta - \theta _ { k } ) / 2 } } \cos \frac { \theta - \theta _ { k } } { 2 } ,
$$

which implies, in view of the trigonometric form of Exercises 1.2.15d and 1.2.13, that

$$
d _ { k } ( \theta ) = \frac { 1 } { 2 n } \biggl [ 1 + 2 \sum _ { j = 1 } ^ { n - 1 } \cos j ( \theta - \theta _ { k } ) + \cos n ( \theta - \theta _ { k } ) \biggr ] .
$$

Furthermore, for $j = 1 , \ldots , 2 n ; k = 1 , \ldots , 2 n$

$$
d _ { k } ( \theta _ { j } ) = { \left\{ \begin{array} { l l } { 0 , \quad } & { j \neq k , } \\ { 1 , \quad } & { j = k . } \end{array} \right. }
$$

Thus the functions $d _ { k } ( \theta ) , k = 1 , . . . , 2 n$ are fundamental polynomials for interpolation by trigonometric polynomials of degree at most $\pmb { n }$ at $\theta _ { 1 } , \ldots , \theta _ { 2 n }$ ： i.e.,

$$
t ( \theta ) = \sum _ { k = 1 } ^ { 2 n } \ y _ { k } d _ { k } ( \theta )
$$

satisfies

$$
t ( \theta _ { j } ) = y _ { j } , \qquad j = 1 , \ldots , 2 n .
$$

The trigonometric Lebesgue function

$$
\delta _ { n } ( \theta ) = \sum _ { k = 1 } ^ { 2 n } \ | d _ { k } ( \theta ) |
$$

has the property that

$$
\delta _ { n } \left( \theta + \frac { \pi } { n } \right) = \delta _ { n } ( \theta ) .
$$

This follows from the observations that $d _ { k } ( \theta + ( \pi / n ) ) = d _ { k - 1 } ( \theta ) ,$ and $d _ { 0 } ( \theta ) = d _ { 2 n } ( \theta ) .$ As a consequence of (1.50)

$$
\Delta _ { n } = \operatorname * { m a x } _ { 0 \leqslant \theta \leqslant 2 \pi } | \delta _ { n } ( \theta ) | = \operatorname * { m a x } _ { - \pi / 2 n \leqslant \theta \leqslant \pi / 2 n } | \delta _ { n } ( \theta ) | .
$$

Now for each $k = 1 , \ldots , 2 n , d _ { k } ( \theta _ { j } ) = 0 , j \neq k , j = 1 , \ldots , 2 n ,$ and, in addition, $d _ { k } ^ { \prime } ( \theta _ { k + n } ) = d _ { k } ^ { \prime } ( \theta _ { k - n } ) = 0 ,$ Note that either $1 \leqslant k + n \leqslant 2 n$ or $1 \leqslant k - n \leqslant 2 n ,$ so that for each $d _ { k } ( \theta )$ we have accounted for $2 n - 2$ simple zeros and one double zero, i.e., for all $_ { 2 n }$ of its zeros in $[ 0 , 2 \pi )$ Hence, for $k = 1 , . . . , 2 n ,$ $d _ { k } ( \theta ) \neq 0$ in $( - \pi / 2 n , \pi / 2 n )$ and $\delta _ { n } ( \theta )$ coincides with a trigonometric polynomial

$$
t ( \theta ) = \sum _ { k = 1 } ^ { 2 n } \ \varepsilon _ { k } d _ { k } ( \theta )
$$

in the interval $[ - \pi / 2 n , \pi / 2 n ] .$ where $\pm _ { k } = \pm 1$ ,the sign being chosen so that $\varepsilon _ { k } d _ { k } ( \theta ) > 0$ for $- \pi / 2 n < \theta < \pi / 2 n$ .Therefore $\pmb { \mathscr { E } _ { k } }$ has the same sign as

$$
d _ { k } ( 0 ) = \frac { 1 } { 2 n } \frac { \sin n \theta _ { k } } { \tan { ( \theta _ { k } / 2 ) } } = \frac { ( - 1 ) ^ { k - 1 } } { 2 n } \frac { 1 } { \tan ^ { ( 2 k - 1 ) } ( \pi / 4 n ) } ,
$$

i.e.,

$$
\begin{array} { l l } { \varepsilon _ { k } = ( - 1 ) ^ { k - 1 } , } & { \quad k = 1 , \dots , n , } \\ { { \qquad } } & { { \qquad } \varepsilon _ { k } = ( - 1 ) ^ { k } , } & { \quad k = n + 1 , \dots , 2 n , } \end{array}
$$

and so,

$$
t ( \theta ) = \sum _ { k = 1 } ^ { n } { \bigl ( } - 1 { \bigr ) } ^ { k - 1 } d _ { k } ( \theta ) - \sum _ { k = n + 1 } ^ { 2 n } { \bigl ( } - 1 { \bigr ) } ^ { k - 1 } d _ { k } ( \theta ) .
$$

A simple computation next reveals that $d _ { k } ( - \theta ) = d _ { 2 n - k + 1 } ( \theta )$ and consequently $t ( \theta ) = t ( - \theta ) ;$ so that $\pmb { t }$ is an even function.

Let

$$
\Delta _ { n } = \operatorname* { m a x } _ { \mathbf { \Gamma } - \pi / 2 n \leqslant \theta \leqslant \pi / 2 n } t ( \theta ) = t ( \bar { \theta } ) .
$$

We claim that $\overline { { \theta } } = 0 .$

First note that $\bar { \theta } \neq \pm \pi / ( 2 n ) ,$ for if $\bar { \theta } = \pm \pi / ( 2 n )$ then $t ( \overline { { \theta } } ) = 1$ in view of (1.51) and (1.47) and $\Delta _ { n } = 1$ ,but

$$
s ( \theta ) = \sum _ { k = 1 } ^ { 2 n } d _ { k } ( \theta )
$$

satisfies $s ( \theta _ { j } ) = 1 , j = 1 , \ldots , 2 n _ { \colon }$ hence $1 - s ( \theta ) = u ( \theta ) .$ , where $\pmb { u } \in \mathcal { T } _ { \pmb { n } }$ either has simple zeros at $\theta _ { 1 } , . . . , \theta _ { 2 n }$ or is identically zero. In the former case ${ \pmb u } ( \theta )$

changes sign at the $\theta _ { j }$ .In particular, then, there exists $\pmb { \theta } ^ { * }$ close to $\pmb { \theta _ { 1 } }$ so that $u ( \theta ^ { * } ) < 0$ and $s ( \theta ^ { * } ) = 1 - u ( \theta ^ { * } ) > 1$ and

$$
1 = \Delta _ { n } \geqslant \delta _ { n } ( \theta ^ { * } ) \geqslant | s ( \theta ^ { * } ) | > 1
$$

gives a contradiction. If ${ \pmb u } = { \bf 0 }$ ,then $s = 1$ and $\delta _ { n } ( \theta ) \equiv 1$ ，which implies that $t ( \theta ) \equiv 1$ ，However, since $n \geqslant 2 ,$ we have $t ( \theta _ { 2 } ) = - 1$ in view of (1.51) and (1.47), again giving a contradiction.

Suppose_ that $0 < | \bar { \theta | } < \pi / 2 n ;$ then, because of the evenness of $t ,$ $t ( { \bar { \theta } } ) = t ( - { \bar { \theta } } ) ,$ and by Rolle's theorem $\pmb { t } ^ { \prime }$ has a zero between $- \bar { \pmb { \theta } }$ and $\bar { \theta , }$ in addition to $t ^ { \prime } ( { \bar { \theta } } ) = { t ^ { \prime } } ( - { \bar { \theta } } ) = 0 ,$ ，for a total of at least three distinct zeros in $( - \pi / ( 2 n ) , \pi / ( 2 n ) )$ 、Also, from our previous observation that $d _ { k } ( \theta +$ $( { \pi } / { n } ) ) = d _ { k - 1 } ( \theta )$ it follows that $d _ { k } ( \theta + \pi ) = d _ { k - n } ( \theta ) = d _ { k + n } ( \theta ) ;$ hence $t ( \theta + \pi ) = ( - 1 ) ^ { n + 1 } t ( \theta )$ .Therefore $t ^ { \prime } ( \theta )$ also has at least three distinct zeros in $( \theta _ { n } , \theta _ { n + 1 } ) .$ Since $t ( \theta _ { k } ) = ( - 1 ) ^ { k - 1 }$ ， $k = 1 , . . . , n , t$ has at least ${ \pmb n } - 1$ distinct zeros in $( \theta _ { 1 } , \theta _ { n } )$ and by Rolle's theorem $\pmb { t ^ { \prime } }$ has at least $\pmb { n } - 2$ zeros in $( \theta _ { 1 } , \theta _ { n } ) .$ Similarly, $t ( \theta _ { k } ) = ( - 1 ) ^ { k }$ ， $k = n + 1 , . . . , 2 n$ and $t ^ { \prime }$ has at least $n - 2$ zeros in $( \theta _ { n + 1 } , \theta _ { 2 n } )$ Thus $t ^ { \prime } \in \mathcal { T } _ { n }$ has at least $2 n - 4 + 6 = 2 n + 2$ zeros,hence is identically zero, and $t$ is a constant, but $t ( \theta _ { 1 } ) = 1$ and $t ( \theta _ { 2 } ) = - 1 ( n \geqslant 2 ) .$ a contradiction. We have proved that $\Delta _ { n } = \delta _ { n } ( 0 )$ Since

$$
( - 1 ) ^ { k - 1 } d _ { k } ( 0 ) = { \frac { 1 } { 2 n } } \cot { \frac { ( 2 k - 1 ) \pi } { 4 n } } ,
$$

we obtain

$$
\Delta _ { n } = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \cot \frac { ( 2 k - 1 ) \pi } { 4 n } .
$$

Observe that

$$
\begin{array} { c } { { { \frac { \pi } { 2 } } \Delta _ { n } = { \displaystyle { \frac { \pi } { 2 n } } \sum _ { k = 1 } ^ { n } \left( \cot { \frac { ( 2 k - 1 ) \pi } { 4 n } } - { \frac { 4 n } { ( 2 k - 1 ) \pi } } \right) } + 2 \sum _ { k = 1 } ^ { n } { \displaystyle { \frac { 1 } { 2 k - 1 } } \sum _ { i = 1 } ^ { n } } } } \\ { { = a _ { n } + 2 \sum _ { k = 1 } ^ { n } { \displaystyle { \frac { 1 } { 2 k - 1 } } } ; } } \end{array}
$$

hence

$$
{ \frac { \pi } { 2 } } \Delta _ { n } - \log n = a _ { n } + 2 \sum _ { k = 1 } ^ { n } { \frac { 1 } { 2 k - 1 } } - \log n .
$$

The ${ a } _ { n }$ form a sequence of Riemann sums of the integral

$$
\int _ { 0 } ^ { \pi / 2 } \left( \cot x - { \frac { 1 } { x } } \right) d x = \log { \frac { 2 } { \pi } } ;
$$

hence

$$
\operatorname* { l i m } _ { n \to \infty } a _ { n } = \log { \frac { 2 } { \pi } } ,
$$

whereas

$$
2 \sum _ { k = 1 } ^ { n } { \frac { 1 } { 2 k - 1 } } - \log n = 2 \left( \sum _ { k = 1 } ^ { 2 n } { \frac { 1 } { k } } - \log 2 n \right) - \left( \sum _ { k = 1 } ^ { n } { \frac { 1 } { k } } - \log n \right) + \log 4 .
$$

Since we know that

$$
\gamma = \operatorname* { l i m } _ { m  \infty } ( \sum _ { j = 1 } ^ { m } { \frac { 1 } { j } } - \log m ) = 0 . 5 7 7 2 \ldots .
$$

(y is called Euler's constant), we have

$$
\operatorname* { l i m } _ { n \to \infty } \left( \Delta _ { n } - { \frac { 2 } { \pi } } \log n \right) = { \frac { 2 } { \pi } } \left( \log { \frac { 8 } { \pi } } + \gamma \right) = 0 . 9 6 2 5 \ldots .
$$

Theorem 1.2. For $n = 1 , 2 , . . . , \Lambda _ { n } ( T ) = \lambda _ { n } ( T ; 1 )$ and

$$
\frac { 2 } { \pi } \log n + \frac { 2 } { \pi } \left( \log \frac { 8 } { \pi } + \gamma \right) < \Lambda _ { n } ( T ) \leqslant \frac { 2 } { \pi } \log n + 1 .
$$

Moreover, $\tau _ { n } = \Lambda _ { n } ( T ) - \frac { 2 } { \pi } \log n , n = 1 , 2 , . . . ,$ is a strictly monotone decreasing sequence with $\tau _ { 1 } = 1$ and

$$
\operatorname* { l i m } _ { n \to \infty } \tau _ { n } = \frac { 2 } { \pi } \biggl ( \log \frac { 8 } { \pi } + \gamma \biggr ) .
$$

Proof. We show first that $\Lambda _ { n } ( T ) = \lambda _ { n } ( T ; 1 ) = \Delta _ { n }$ .If $\pmb { n = 1 }$ ,this is trivial. Suppose $\pmb { n } \geqslant 2 .$ As we have seen (p.17), $d _ { k } ( \theta ) + d _ { 2 n - k + 1 } ( \theta )$ is an even function, hence a cosine polynomial. Thus, if $\begin{array} { r } { { \boldsymbol { x } } = \cos \theta , } \end{array}$ we have for $k = 1 , \ldots , n .$

$$
p _ { k } ( x ) = d _ { k } ( \theta ) + d _ { 2 n - k + 1 } ( \theta ) \in \mathcal { P } _ { n } .
$$

Now for $i = 1 , \ldots , n ,$

$$
p _ { k } ( \xi _ { i } ^ { ( n ) } ) = d _ { k } ( \theta _ { i } ) + d _ { 2 n - k + 1 } ( \theta _ { i } ) = d _ { k } ( \theta _ { i } ) = { \left\{ \begin{array} { l l } { 0 , \quad } & { i \neq k } \\ { 1 , \quad } & { i = k } \end{array} \right. }
$$

and (1.46) reveals that the leading coefficient of $p _ { \pmb { k } } ( \pmb { x } )$ is zero. Hence

$$
p _ { k } ( x ) = l _ { k , n } ( T ; x ) , \qquad k = 1 , . . . , n ,
$$

and

$$
\lambda _ { n } ( T ; x ) = \sum _ { k = 1 } ^ { n } | p _ { k } ( x ) | .
$$

Thus

$$
\lambda _ { n } ( T ; x ) \leqslant \delta _ { n } ( \theta ) \leqslant \Delta _ { n } ,
$$

and it is easy to see from (1.43) that $\lambda _ { n } ( T ; 1 ) = \Delta _ { n }$ . Hence $\Lambda _ { n } ( T ) = \Delta _ { n }$

The rest of the theorem is proved by showing that the sequence $\tau _ { n } = \Delta _ { n } - ( 2 / \pi ) \log n$ is monotone decreasing as $\pmb { n }$ increases. To this end we need some information about the monotone convergence of Riemann sums to the integral, and so we digress from the proof to obtain the following lemma due to D.J.Newman and the author, which is not without interest in itself.

Lemma 1.2.1. If $f ^ { \prime \prime } ( x )$ and $f ^ { \prime \prime } ( x )$ are both nonnegative in [O,1], the Riemann sums

$$
b _ { n } = { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } ~ f \left( { \frac { 2 k - 1 } { 2 n } } \right)
$$

are monotone increasing as $\pmb { n }$ increases.

Proof. Integrating three times by parts yields

$$
\begin{array} { r l r } {  { \frac { 1 } { n } \sum _ { k = 1 } ^ { n } f ( \frac { 2 k - 1 } { 2 n } ) = \int _ { 0 } ^ { 1 } f ( t ) d t - \frac { f ^ { \prime \prime } ( 0 ) } { 2 4 n ^ { 2 } } } } \\ & { } & { - \int _ { 0 } ^ { 1 } \frac { 4 ( n t - [ n t + \frac { 1 } { 2 } ] ) ^ { 3 } + [ n t + \frac { 1 } { 2 } ] } { 2 4 n ^ { 3 } } f ^ { \prime \prime } ( 1 - t ) d t , } \end{array}
$$

(the[] here is the integer part notation; cf. foonote p. 2). Since $f ^ { \prime \prime } ( 0 ) \geqslant 0 ,$ ,the sequence $- f ^ { \prime \prime } ( 0 ) / ( 2 4 n ^ { 2 } )$ is monotone increasing; hence, since $t ^ { 3 } f ^ { \prime \prime } ( 1 - t ) \geqslant 0 ,$ it suffices to show that the function

$$
\frac { 4 ( n t - [ n t + \frac { 1 } { 2 } ] ) ^ { 3 } + [ n t + \frac { 1 } { 2 } ] } { 2 4 n ^ { 3 } t ^ { 3 } }
$$

decreases as $\pmb { n }$ increases. Thus it is enough to show that

$$
\frac { 4 ( x - [ x + \frac { 1 } { 2 } ] ) ^ { 3 } + [ x + \frac { 1 } { 2 } ] } { x ^ { 3 } }
$$

is a decreasing function for $\mathbf { \nabla } _ { \mathbf { x } } > \mathbf { 0 } .$ . This function is continuously differentiable even at the points $k - ( { \textstyle { \frac { 1 } { 2 } } } ) , k$ an integer; hence it suffces to verify that its derivative is negative for $\begin{array} { r } { k - ( \frac { 1 } { 2 } ) < x < k + ( \frac { 1 } { 2 } ) } \end{array}$ .In this interval, however,the function is

$$
\frac { 4 ( x - k ) ^ { 3 } + k } { x ^ { 3 } }
$$

whose derivative is

$$
{ \frac { 1 2 k } { x ^ { 4 } } } ( ( x - k ) ^ { 2 } - { \frac { 1 } { 4 } } ) ,
$$

which is indeed negative throughout the interval.

Returning now to the theorem, we apply the lemma with

$$
. \qquad f ( x ) = \frac { 1 } { ( \pi / 2 ) x } - \cot \frac { \pi } { 2 } x .
$$

Since

$$
{ \frac { 1 } { z } } - \cot z = c _ { 1 } z + c _ { 3 } z ^ { 3 } + \cdots + c _ { 2 k - 1 } z ^ { 2 k - 1 } + \cdots ,
$$

with $c _ { 2 k - 1 } > 0 , k = 1 , 2 , . . .$ (the expansion is valid in $| z | < \pi$ See Knopp [1]). It is evident that $f ^ { \prime \prime }$ and $f ^ { \prime \prime }$ are nonnegative in [O,1]. The $b _ { n }$ defined in (1.56) satisfy $a _ { n } = - ( \pi / 2 ) b _ { n }$ , where $a _ { n }$ is defined in (1.53). Since the $b _ { n }$ are monotone increasing, the ${ a } _ { n }$ are monotone decreasing. Also, if we put

$$
u _ { n } = 2 \sum _ { k = 1 } ^ { n } { \frac { 1 } { 2 k - 1 } } - \log n ,
$$

then

$$
u _ { n } - u _ { n + 1 } = \log { \left( 1 + { \frac { 1 } { n } } \right) } - { \frac { 2 } { 2 n + 1 } }
$$

is positive for $\pmb { n = 1 }$ and tends to zero as $\pmb { n }$ tends to infinity.

Since the derivative of

$$
\log { \left( 1 + { \frac { 1 } { x } } \right) } - { \frac { 2 } { 2 x + 1 } }
$$

is

$$
- \frac { 1 } { x ( x + 1 ) ( 2 x + 1 ) ^ { 2 } } < 0 , \qquad x > 0 ,
$$

$u _ { n } > u _ { n + 1 } , n = 1 , 2 , \ldots .$ Thus the ${ \pmb u } _ { \pmb n }$ are strictly monotone decreasing, and so is the sequence $( \pi / 2 ) \tau _ { n } = a _ { n } + u _ { n }$

Finally, we wish to provide some further information about the minimal Lebesgue constants, $\Lambda _ { k } ( X ^ { * } ) ,$ whose existence was previously affirmed. We observe first that if $\pmb { X }$ is any array of nodes (as defined in (1.28)) and $x _ { 1 } < x _ { 2 } < \cdots < x _ { k }$ is the arrangement of its $k$ th row, $k \geqslant 2 ,$ , then numbers $a ( k )$ and $b ( k )$ are defined by

$$
a x _ { 1 } + b = - 1 , \qquad a x _ { k } + b = 1 .
$$

If we put

$$
x _ { j } ^ { \prime } = a x _ { j } + b , \qquad j = 1 , 2 , \ldots , k ,
$$

then the points $\boldsymbol { x } _ { 1 } ^ { \prime } , \boldsymbol { x } _ { 2 } ^ { \prime } , \ldots , \boldsymbol { x } _ { k } ^ { \prime }$ satisfying $- 1 = x _ { 1 } ^ { \prime } < x _ { 2 } ^ { \prime } < \dots < x _ { k } ^ { \prime } = 1$ form the $\pmb { k }$ th row of array, $\pmb { X ^ { \prime } }$ ，which is the expansion of $\pmb { X }$

It is easy to see that for $k \geqslant 2$

$$
\Lambda _ { k } ( X ^ { \prime } ) = \operatorname* { m a x } _ { x _ { 1 } \leqslant x \leqslant x _ { k } } \lambda _ { k } ( X ; x ) \leqslant \Lambda _ { k } ( X ) .
$$

Thus if

$$
\operatorname* { m i n } _ { X } \Lambda _ { k } ( X ) = \Lambda _ { k } ( X ^ { * } ) ,
$$

we conclude that there exists a best array of nodes, callit $X ^ { \ast }$ ， whose every row—after the first—includes $\pm 1$ as nodes. Let us, therefore, restrict our attention to fully expanded arrays, i.e., all $\pmb { X }$ such that $X = X ^ { \prime }$

Fix $k \geqslant 3 .$ Let

$$
M _ { j } = M _ { j } ( \boldsymbol { X } ) = \operatorname* { m a x } _ { \boldsymbol { x } _ { j } \leqslant \boldsymbol { x } \leqslant \boldsymbol { x } _ { j + 1 } } \lambda _ { k } ( \boldsymbol { X } ; \boldsymbol { x } ) , \qquad j = 1 , \ldots , k - 1 .
$$

Bernstein [4] conjectured (quite plausibly) that if $M _ { 1 } ( X ) = M _ { 2 } ( X ) = \cdots$ $= M _ { k - 1 } ( X )$ then $\pmb { X }$ is a best array of nodes. Erdos [1] amplified Bernstein's conjecture as follows: there is a unique (expanded) array, $X ^ { * }$ ，for which

$M _ { 1 } = \cdots = M _ { k - 1 }$ holds, and for any array, $\pmb { X }$ ，

$$
\operatorname* { m i n } _ { 1 \leqslant j \leqslant k - 1 } M _ { j } ( X ) \leqslant \Lambda _ { k } ( X ^ { * } ) .
$$

The conjectures of Bernstein and Erdos were proved by Kilgore [1] and de Boor and Pinkus [1]. However, the nodes of the best array are not known explicitly.

For the array ${ \pmb T } ^ { \prime }$ (the expanded Chebyshev array obtained by multiplying each entry in the $\pmb { k }$ th row of $T$ by sec $( { \pmb \pi } / { 2 k } ) )$ ,Brutman [1] showed that

$$
\operatorname* { m i n } _ { 1 \leqslant j \leqslant k - 1 } M _ { j } ( T ^ { \prime } ) > \frac { 2 } { \pi } \log k + \frac { 1 } { 2 } ,
$$

and

$$
\Lambda _ { k } ( T ) < \frac { 2 } { \pi } \log k + \frac { 3 } { 4 } .
$$

Thus, in view of the validity of the Erdos conjecture we obtain, for $k \geqslant 3$

$$
\Lambda _ { k } ( T ^ { \prime } ) > \Lambda _ { k } ( X ^ { * } ) > \frac { 2 } { \pi } \log k + \frac { 1 } { 2 } ,
$$

and conclude that: (i) $1 / 2 < c < 3 / 4$ in (1.37), and (ii) the readily available expanded Chebyshev array, $\pmb { T } ^ { \prime }$ is, for all practical purposes, as useful as the optimal nodes.

# EXERCISES 1.3.1-1.3.24

1.3.1. For any $\pmb { X }$ and $n = 1 , 2 , \ldots ,$

$$
\sum _ { j = 1 } ^ { n } l _ { j , n } ( X ; x ) = 1 ,
$$

and so

$$
\lambda _ { n } ( X ; x ) \geqslant 1 , \qquad n = 1 , 2 , \ldots , x \in I .
$$

Hint. $1 \in P _ { n } , n = 1 , 2 , \ldots .$

1.3.2. (a)

$$
\frac { T _ { n } ( x ) } { T _ { n + 1 } ( x ) } = \frac { 1 } { n + 1 } \sum _ { j = 1 } ^ { n + 1 } \frac { 1 - ( \xi _ { j } ^ { ( n + 1 ) } ) ^ { 2 } } { x - \xi _ { j } ^ { ( n + 1 ) } } .
$$

$$
\frac { U _ { n - 1 } ( x ) } { U _ { n } ( x ) } = \frac { 1 } { n + 1 } \sum _ { j = 1 } ^ { n } \frac { 1 - ( \eta _ { j } ^ { ( n + 1 ) } ) ^ { 2 } } { x - \eta _ { j } ^ { ( n + 1 ) } } .
$$

$$
\frac { 1 } { T _ { n } ( x ) } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \frac { ( - 1 ) ^ { j - 1 } \sqrt { 1 - ( \xi _ { j } ^ { ( n ) } ) ^ { 2 } } } { x - \xi _ { j } ^ { ( n ) } } .
$$

$$
\frac { 1 } { U _ { n } ( x ) } = \frac { 1 } { n + 1 } \sum _ { j = 1 } ^ { n } \frac { ( - 1 ) ^ { j - 1 } ( 1 - ( \eta _ { j } ^ { ( n + 1 ) } ) ^ { 2 } ) } { x - \eta _ { j } ^ { ( n + 1 ) } } .
$$

# 1.3.3. Show that

$$
L _ { k - 1 } ( T _ { n } , T ; x ) = ( - 1 ) ^ { r } T _ { | m | } ( x ) ,
$$

where

$$
n = 2 k r + m ; \quad | m | < k , \qquad k , r \geqslant 0 .
$$

# Hint. See Exercise 1.2.5.

1.3.4. If $\pmb { U }$ denotes the array of nodes whose $^ { n + }$ 1st row is $\pmb { \eta _ { 0 } } , \dotsc , \pmb { \eta _ { n } }$ , the extrema of $T _ { n } ( x ) ,$ show that

$$
\begin{array} { r l r } & { } & { L _ { n } ( f , U ; x ) = ( 1 - x ^ { 2 } ) T _ { n } ^ { \prime } ( x ) \biggl \{ \displaystyle \frac { f ( 1 ) } { ( 1 - x ) 2 n ^ { 2 } } + \displaystyle \frac { f ( - 1 ) } { ( 1 + x ) ( - 1 ) ^ { n + 1 } 2 n ^ { 2 } } } \\ & { } & { + \displaystyle \sum _ { j = 1 } ^ { n - 1 } \displaystyle \frac { f ( \eta _ { j } ) } { ( x - \eta _ { j } ) ( 1 - \eta _ { j } ^ { 2 } ) T _ { n } ^ { \prime \prime } ( \eta _ { j } ) } \biggr \} . } \end{array}
$$

1.3.5. For any $\pmb { X }$ and $\pmb { n } \geqslant 2$ show that

$$
l _ { j } ^ { \prime } ( x _ { j } ) = \frac { \omega ^ { \prime \prime } ( x _ { j } ) } { 2 \omega ^ { \prime } ( x _ { j } ) } .
$$

1.3.6. If $x _ { 1 } > x _ { 2 } > \cdots > x _ { n }$ ， show that $\omega ( x ) = ( x - x _ { 1 } ) \cdots ( x - x _ { n } )$ satisfies

$$
\operatorname { s g n } \omega ^ { \prime } ( x _ { j } ) = ( - 1 ) ^ { j - 1 } , \qquad j = 1 , \ldots , n ,
$$

where

$$
\mathsf { s g n } \ t = \left\{ - 1 , \quad \begin{array} { r l } { 1 , } & { { } \quad t > 0 , } \\ { - 1 , } & { { } \quad t < 0 , } \\ { 0 , } & { { } \quad t = 0 . } \end{array} \right.
$$

If $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ are distinct real points and $f ( x )$ is a function defined for $\boldsymbol { x } = \boldsymbol { x } _ { i }$ ， $i = 1 , \ldots , n ,$ ,the coefficient of $x ^ { n - 1 }$ in the polynomial of degree at most $n - 1$ ,which interpolates $f$ at the $\boldsymbol { x } _ { i }$ , is denoted by $f ( x _ { 1 } , \ldots , x _ { n } )$ and called the divided difference off with respect to $x _ { 1 } , \ldots , x _ { n }$ .Note that there is no notational ambiguity when $n = 1$

# 1.3.7. Show that

$$
f ( x _ { 1 } , \ldots , x _ { n } ) = \sum _ { i = 1 } ^ { n } { \frac { f ( x _ { i } ) } { \omega ^ { \prime } ( x _ { i } ) } } .
$$

1.3.8. Show that if ${ \pmb x } _ { 1 } \neq { \pmb x } _ { { \pmb k } }$

$$
{ \frac { f ( x _ { 1 } , \ldots , x _ { k - 1 } ) - f ( x _ { 2 } , \ldots , x _ { k } ) } { x _ { 1 } - x _ { k } } } = f ( x _ { 1 } , \ldots , x _ { k } )
$$

(hence the name divided difference).

# 1.3.9. Show that

$$
\begin{array} { l } { p ( x ) = f ( x _ { 1 } ) + ( x - x _ { 1 } ) f ( x _ { 1 } , x _ { 2 } ) + ( x - x _ { 1 } ) ( x - x _ { 2 } ) f ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) } \\ { \qquad + \dotsb + ( x - x _ { 1 } ) \dotsb ( x - x _ { n - 1 } ) f ( x _ { 1 } , \dots , x _ { n } ) } \end{array}
$$

satisfies $p ( { x _ { i } } ) = f ( x _ { i } ) , i = 1 , . . . , n .$ Equation (1.61) is called Newton's form of the interpolating polynomial.

Hint. Write the unique interpolating polynomial in the form $a _ { 1 } + a _ { 2 } ( { \pmb x } - { \pmb x } _ { 1 } ) +$ $\cdots + a _ { n } ( x - x _ { 1 } ) \cdots ( x - x _ { n - 1 } )$ and recall the definition of divided differences.

# 1.3.10. Show that

$$
f ( t ) - L _ { n - 1 } ( f ; t ) = ( t - x _ { 1 } ) \cdots ( t - x _ { n } ) f ( x _ { 1 } , \ldots , x _ { n } , t )
$$

holds for allt. (The right-hand side is defined as zero when $t = x _ { i } , i = 1 , . . . , n . )$

Hint. Use Exercise 1.3.7.

1.3.11. If $\boldsymbol { x } _ { 1 } , \ldots , \boldsymbol { x } _ { n }$ and $t$ are points of $[ a , b ]$ and $f \in C ^ { n } [ a , b ] .$ show that

$$
f ( t ) - L _ { n - 1 } ( f ; t ) = ( t - x _ { 1 } ) \cdots ( t - x _ { n } ) { \frac { f ^ { ( n ) } ( \xi ) } { n ! } }
$$

for some $\xi ( t )$ in $[ a , b ]$

Hint. Let $\begin{array} { r } { \begin{array} { r } { h ( t ) / g ( t ) = ( f ( t ) - L _ { n - 1 } ( f ; t ) ) / ( t - x _ { 1 } ) \cdots ( t - x _ { n } ) . } \end{array} } \end{array}$ Then $h ( t ) g ( x ) - g ( t ) h ( x ) ,$ as a function of $\pmb { x }$ has $\pm 1$ zeros $\pmb { x } _ { 1 } \ldots , \pmb { x } _ { n }$ ,t.Now apply Rolles theorem.

1.3.12. If $x _ { 1 } , \ldots , x _ { k }$ are distinct points of $[ a , b ]$ and $f \in C ^ { k - 1 } [ a , b ]$ then

$$
f ( x _ { 1 } , . . . , x _ { k } ) = { \frac { f ^ { ( k - 1 ) } ( \xi ) } { ( k - 1 ) ! } }
$$

for some point $\xi$ of $[ a , b ]$

1.3.13. If $t \in \mathcal { T } _ { n }$ (the trigonometric polynomials of degree at most $\pmb { n }$ and $\mathbf { \boldsymbol { t } } \neq \mathbf { 0 } .$ show that $\pmb { t }$ has at most 2n zeros in the interval $[ 0 , 2 \pi )$

Hint. $t ( \theta ) = e ^ { - i n \theta } q ( e ^ { i \theta } ) ;$ where $\pmb q$ is a polynomial of degree at most $_ { 2 n }$ with complex coefficients.

1.3.14. Is the $t$ satisfying (1.49) unique?

1.3.15.Show that Lemma 1.2.1 is also valid if $f ^ { \prime \prime } ( x ) \geqslant 0$ and $f ^ { \prime \prime } ( x ) \leqslant 0$

1.3.16. Show that $\Lambda _ { n } ( T )$ is strictly monotone increasing with $\pmb { n }$

1.3.17. If $\mathbf { } _ { t \in \mathcal { T } _ { n } }$ ， $0 \leqslant \alpha < \beta < \pi$ and $t ( \alpha ) t ( \beta ) > 0$ show that $t$ has an even number (counting multiplicities) of zeros in $( \alpha , \beta )$ If $t ( \alpha ) t ( \beta ) < 0$ show that t has an odd number of zeros in $( \alpha , \beta )$

1.3.18. If $t \in \mathcal { T } _ { n }$ ， $0 \leqslant \varphi _ { 0 } < \varphi _ { 1 } < \cdots < \varphi _ { k } < 2 \pi _ { : }$ and $t ( \varphi _ { i } ) t ( \varphi _ { i + 1 } ) < 0 , i = 0 , \ldots , k - 1 ,$ show that $t$ has at least $\pmb { k }$ zeros in $[ \varphi _ { 0 } , \varphi _ { k } ]$

Hint. Use Exercise 1.3.17.

1.3.19. Suppose that $\mathbf { } _ { t \in \mathcal { T } _ { n } }$ satisfies

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } | t ( \theta ) | = 1
$$

and $t ( 0 ) = 1$ Show that $t ( \theta ) \neq 0$ for $| \theta | < \pi / 2 n .$ and $t ( \pm \pi / ( 2 n ) ) = 0$ ,if and only if $t ( \theta ) = \cos { n \theta }$

Hint. Consider $r ( \theta ) = \cos n \theta - t ( \theta )$ and suppose that the result we seek is false. Note that $r ( j \pi / n ) r ( ( j + 1 ) \pi / n ) \leqslant 0 , j = 1 , \ldots , 2 n - 2$ and $r ( \pi / n ) \leqslant 0$ whereas $r ( \theta _ { 0 } ) > 0 ;$ where $\pmb { \theta _ { 0 } }$ is a zero of $t$ in $( 0 , \pi / ( 2 n ) )$ ,say. Apply Exercise 1.3.18 and also observe that $r ( 0 ) = r ^ { \prime } ( 0 ) = 0$

1.3.20. (M. Riesz [1]) Suppose that $\mathbf { \Delta } _ { t \in \mathcal { T } _ { n } }$ and

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } \left. t ( \theta ) \right. = M > 0 .
$$

If $| t ( \varphi ) | = M$ ,then $t ( \theta )$ has no zero in $| \theta - \varphi | < \pi / ( 2 n )$ and $t ( \varphi \pm \pi / ( 2 n ) ) = 0$ if and only if $t ( \theta ) = \pm M \cos n ( \theta - \varphi ) .$

1.3.21.Ehlich and Zeller [2] showed that for even $\pmb { n }$

$$
\Lambda _ { n } ( U ) = \Lambda _ { n - 1 } ( T ) .
$$

Show that $\Lambda _ { 2 k } ( U ) - ( 2 / \pi ) \log { ( 2 k ) }$ is a strictly monotone-increasing function of $\pmb { k }$ with limit $( 2 / \pi ) ( \log { ( 8 / \pi ) } + \gamma )$

Hint. Use (1.57) with $f ( x ) = [ ( \pi / 2 ) x ] ^ { - 1 } - \cos { ( \pi / 2 ) } x$ to obtain an upper bound on $b _ { n + 2 } - b _ { n }$ ,in the notation of (1.56).

We have emphasized the effectiveness of the Chebyshev nodes for polynomial interpolation. Interpolation in equally spaced points is an attractive alternative because of the simple structure of the nodes.Let us investigate the size of the Lebesgue constants for them.If $E$ denotes the array of equally spaced points (including $\pm 1 ]$ ofI and $\pmb { n } = 2 \pmb { k } + 1$ ， $k = 1$ ,2,... then the elements of the nth row of $\pmb { { \cal E } }$ are

$$
x _ { i } = \frac { i } { k } , \qquad i = - k , - k + 1 , \dots , k - 1 , k ,
$$

and

$$
\lambda _ { n } ( E ; x ) = \sum _ { j = - k } ^ { k } \prod _ { i \neq j } { \frac { \left| x - x _ { i } \right| } { \left| x _ { j } - x _ { i } \right| } } .
$$

# 1.3.22. Show that

$$
\prod _ { i \neq j } | x _ { j } - x _ { i } | = { \frac { ( k - j ) ! ( k + j ) ! } { k ^ { 2 k } } } ,
$$

$$
\prod _ { i \not = j } | x - x _ { i } | \leqslant { \frac { ( 2 k ) ! } { k ^ { 2 k } } } , \qquad x \in I
$$

and hence

$$
\begin{array} { r } { \lambda _ { n } ( E ; x ) \leqslant \frac { 1 } { 2 } 2 ^ { n } , \qquad x \in I . } \end{array}
$$

1.3.23. Put $t = 1 - ( 1 / 2 k ) .$ Show that

$$
\begin{array} { c } { { \displaystyle { \prod _ { i \ne j } | t - x _ { i } | \geqslant \displaystyle \frac { 1 } { 2 k } \cdot \frac { 1 } { 2 k } \cdot \frac { 3 } { 2 k } \cdot \cdots \frac { 2 ( j + 1 ) - 1 } { 2 k } \cdot \frac { 2 j - 3 } { 2 k } \cdot \frac { 2 ( j - 1 ) - 3 } { 2 k } \cdot \cdot \cdot \frac { 4 k - 3 } { 2 k } } } } \\ { { \geqslant \displaystyle \frac { 1 } { 2 k } \cdot \frac { 1 } { 2 k } \cdot \frac { 2 } { 2 k } \cdot \cdots \frac { 4 k - 4 } { 2 k } = \displaystyle \frac { 1 } { 4 } \frac { ( 2 k - 2 ) ! } { k ^ { 2 k } } . } } \end{array}
$$

Now show that, in view of Exercise 1.3.22a,

$$
\lambda _ { n } ( E ; t ) \geqslant { \frac { 1 } { 8 ( n - 1 ) ( n - 2 ) } } 2 ^ { n } .
$$

1.3.24. From ${ \pmb n } ( \geqslant 3 )$ odd

$$
\frac { 1 } { 8 ( n - 1 ) ( n - 2 ) } \leqslant \frac { \Lambda _ { n } ( E ) } { 2 ^ { n } } \leqslant \frac 1 2 ,
$$

hence

$$
\operatorname* { l i m } _ { k \to \infty } \left[ \Lambda _ { 2 k + 1 } ( E ) \right] ^ { 1 / ( 2 k + 1 ) } = 2 .
$$

These results should be compared to (1.55). The case of even n leads to the same result. The methods suggested in Exercises 1.3.22 and 1.3.23 are due to Jia Rong-Qing, privately communicated by C. de Boor.

# 1.4. Hermite Interpolation

We have just seen the sense in which the zeros of the Chebyshev polynomials are “good” nodes for polynomial interpolation. Our discussion was intended mainly as an introduction to the notion of polynomial interpolation, and the conclusion that there was no universal array of nodes at which the interpolating polynomials converged to every continuous function was disappointingly negative.To obtain positive results we must amplify the idea of interpolation. We do this by requiring the polynomial not only to take on given values at the nodes but by also fixing the value of its frst derivative at the given nodes.

Given nodes $x _ { 1 } , \ldots , x _ { n }$ , all contained in $\pmb { I }$ , real numbers $y _ { 1 } ^ { \prime } , \ldots , y _ { n } ^ { \prime }$ , and a function $f ( x )$ defined on $I ,$ ，we wish to construct a $\pmb { p } \in \mathcal { P } _ { 2 n - 1 }$ having the properties that

$$
p ( x _ { j } ) = f ( x _ { j } ) = y _ { j } , \qquad j = 1 , \ldots , n
$$

and

$$
p ^ { \prime } ( x _ { j } ) = y _ { j } ^ { \prime } , \qquad j = 1 , \ldots , n .
$$

Note that $y _ { j } ^ { \prime }$ is not necessarily related to $f ^ { \prime } ( x _ { j } ) ,$ even if the latter exists. We put

$$
\omega ( x ) = ( x - x _ { 1 } ) ( x - x _ { 2 } ) \cdot \cdot \cdot ( x - x _ { n } )
$$

and construct two sets of fundamental polynomials,

$$
\begin{array} { l } { { h _ { j } ( x ) = \left( 1 - \displaystyle \frac { \omega ^ { \prime \prime } ( x _ { j } ) } { \omega ^ { \prime } ( x _ { j } ) } ( x - x _ { j } ) \right) l _ { j } ^ { 2 } ( x ) , \qquad j = 1 , . . . , n , } } \\ { { \mathfrak { h } _ { j } ( x ) = ( x - x _ { j } ) l _ { j } ^ { 2 } ( x ) , \qquad j = 1 , . . . , n , } } \end{array}
$$

where $l _ { j } ( \boldsymbol { x } )$ is defined in (1.25). $\boldsymbol { h } _ { 1 } , . . . , \boldsymbol { h } _ { n } \in \mathcal { P } _ { 2 n - 1 }$ are called fundamental polynomials of the first kind for Hermite interpolation (which is the name given to polynomial interpolation that satisfies (1.62) and (1.63), and ${ \mathfrak { h } } _ { 1 } , \ldots ,$ $\mathfrak { h } _ { n } \in \mathcal { P } _ { 2 n - 1 }$ are fundamental polynomials of the second kind for Hermite interpolation.It is not hard to verify that

$$
\begin{array} { r l } & { h _ { j } ( x _ { i } ) = \left\{ \begin{array} { l l } { 0 , } & { \quad i \neq j } \\ { 1 , } & { \quad i = j } \end{array} \right. \quad i , j = 1 , \dots , n , } \\ & { ~ h _ { j } ^ { \prime } ( x _ { i } ) = 0 , \quad \quad i , j = 1 , \dots , n , } \\ & { ~ \mathfrak { h } _ { j } ( x _ { i } ) = 0 , \quad \quad i , j = 1 , \dots , n , } \\ & { ~ \mathfrak { h } _ { j } ^ { \prime } ( x _ { i } ) = \left\{ \begin{array} { l l } { 0 , } & { \quad i \neq j } \\ { 1 , } & { \quad i = j } \end{array} \right. \quad i , j = 1 , \dots , n , } \end{array}
$$

and the reader is urged to do so. Exercise 1.3.5 is useful in calculating $h _ { j } ^ { \prime } ( x _ { j } ) .$

The polynomial

$$
W _ { 2 n - 1 } ( x ) = \sum _ { j = 1 } ^ { n } { y } _ { j } h _ { j } ( x ) + \sum _ { j = 1 } ^ { n } { y } _ { j } ^ { \prime } { \mathfrak { h } } _ { j } ( x )
$$

is a member of $\mathcal { P } _ { 2 n - 1 }$ and satisfies

$$
W _ { 2 n - 1 } ( x _ { j } ) = y _ { j } , \qquad W _ { 2 n - 1 } ^ { \prime } ( x _ { j } ) = y _ { j } ^ { \prime } ,
$$

in view of (1.65)-(1.68). The process of obtaining $W _ { 2 n - 1 }$ is called Hermite interpolation. Moreover, $W _ { 2 n - 1 }$ is the only member of $\mathscr { P } _ { 2 n - 1 }$ with these properties， for if $\pmb { p } \in \mathcal { P } _ { 2 n - 1 }$ satisfies (1.62) and (1.63) then ${ \pmb q } = { \pmb p } -$ $W _ { 2 n - 1 } \in \mathcal P _ { 2 n - 1 } , q ( x _ { j } ) = 0 , j = 1 , . . . , n$ and $q ^ { \prime } ( x _ { j } ) = 0 , j = 1 , \ldots , n .$ Thus $\pmb q$ has zeros of multiplicity at least 2 at $x _ { 1 } , \ldots , x _ { n }$ ,hence has, at least, $_ { 2 n }$ zeros and therefore $\begin{array} { r } { \pmb q = 0 . } \end{array}$ A consequence of the uniqueness of $W _ { 2 n - 1 }$ is that if $\pmb { p } \in \mathscr { P } _ { 2 n - 1 }$ then

$$
p ( x ) = \sum _ { j = 1 } ^ { n } \ p ( x _ { j } ) h _ { j } ( x ) + \sum _ { j = 1 } ^ { n } \ p ^ { \prime } ( x _ { j } ) \mathfrak { h } _ { j } ( x ) .
$$

Let us suppose now that $x _ { 1 } , \ldots , x _ { n }$ are chosen to be $\xi _ { 1 } , \ldots , \xi _ { n }$ , the zeros of $T _ { n } ( x )$ Then,in view of Exercise 1.2.3 and 1.2.8,we obtain

$$
h _ { j } ( x ) = h _ { j , n } ( T ; x ) = { \frac { 1 - \xi _ { j } x } { 1 - \xi _ { j } ^ { 2 } } } ( l _ { j , n } ( T ; x ) ) ^ { 2 } = { \frac { 1 - \xi _ { j } x } { n ^ { 2 } } } \left( { \frac { T _ { n } ( x ) } { x - \xi _ { j } } } \right) ^ { 2 }
$$

and

$$
\mathfrak { h } _ { j } ( x ) = \mathfrak { h } _ { j , n } ( T ; x ) = ( x - \xi _ { j } ) ( l _ { j , n } ( T ; x ) ) ^ { 2 } = \frac { 1 } { n ^ { 2 } } \frac { 1 - \xi _ { j } ^ { 2 } } { x - \xi _ { j } } T _ { n } ^ { 2 } ( x ) .
$$

# EXERCISES 1.4.1-1.4.10

1.4.1. Show that for any choice of nodes

$$
\sum _ { j = 1 } ^ { n } h _ { j } ( x ) = 1 ,
$$

and

$$
\sum _ { j = 1 } ^ { n } \ ( x - x _ { j } ) h _ { j } ( x ) = \sum _ { j = 1 } ^ { n } \mathrm { ~ b } _ { j } ( x ) .
$$

1.4.2. If we put

$$
v _ { j } ( x ) = 1 - { \frac { \omega ^ { \prime \prime } ( x _ { j } ) } { \omega ^ { \prime } ( x _ { j } ) } } ( x - x _ { j } )
$$

so that $h _ { j } ( x ) = v _ { j } ( x ) l _ { j } ^ { 2 } ( x ) , j = 1 , \ldots , n ,$ show that

$$
\sum _ { j = 1 } ^ { n } v _ { j } ( x ) = n ^ { 2 } .
$$

Hint. Recall Exercise 1.3.7.

1.4.3. Show that

$$
h _ { j , n } ( T ; x ) \geqslant 0 , \qquad x \in I , j = 1 , \ldots , n .
$$

# 1.4.4. Show that

$$
| \mathfrak { h } _ { j , n } ( T ; x ) | \leqslant h _ { j } ( x ) , \qquad x \in I , \qquad j = 1 , \ldots , n ,
$$

hence that

$$
\sum _ { j = 1 } ^ { n } | \mathfrak { h } _ { j , n } ( T ; x ) | \leqslant 1 .
$$

# 1.4.5. Show that

$$
\sum _ { j = 1 } ^ { n } \mathfrak { h } _ { j , n } ( T ; x ) = \frac { 1 } { n } T _ { n - 1 } ( x ) T _ { n } ( x ) .
$$

1.4.6. If $\pmb { p } \in \mathcal { P } _ { 2 n - 1 }$ and

$$
| p ( \xi _ { j } ) | \leqslant A , \quad | p ^ { \prime } ( \xi _ { j } ) | \leqslant B , \quad \quad j = 1 , \ldots , n ,
$$

then

$$
\vert p ( x ) \vert \leqslant A + B , \qquad x \in I .
$$

If $\pmb { n = 1 }$ , the bound $\pmb { A } + \pmb { B }$ in (1.77) cannot be improved.

Hint.Apply (1.70), (1.73), (1.74),and (1.76).

1.4.7. Equation (1.38) shows that (1.76) can be improved to

$$
\sum _ { j = 1 } ^ { n } \frac { | \mathfrak { h } _ { j , n } ( T ; x ) | } { ( 1 - \xi _ { j } ^ { 2 } ) ^ { 1 / 2 } } \leqslant \frac { 1 } { n } \biggl ( \frac { 2 } { \pi } \log n + 1 \biggr ) .
$$

1.4.8.Prove that under the hypotheses of Exercise 1.4.6 the conclusion (1.77) can be strengthened to read

$$
\vert p ( x ) \vert \leqslant A + \mu _ { n } B , \qquad x \in I ,
$$

where

$$
\mu _ { n } = { \frac { 1 } { n } } \left( { \frac { 2 } { \pi } } \log n + 1 \right) .
$$

Indeed, show that (1.79) remains true if the hypothesis on $\pmb { p } ^ { \prime }$ in Exercise 1.4.6 is weakened to read

$$
| p ^ { \prime } ( \xi _ { j } ) | \leqslant B ( 1 - \xi _ { j } ^ { 2 } ) ^ { - 1 / 2 } , \qquad j = 1 , \ldots , n .
$$

# 1.4.9. Show that

$$
\sum _ { j = 1 } ^ { n } [ l _ { j , n } ( T ; x ) ] ^ { 2 } \leqslant 2 \cos ^ { 2 } { \frac { \pi } { 4 n } } \leqslant 2 , \qquad { \mathrm { a l l ~ } } x \in I .
$$

Hint. Use (1.73) and (1.71). (Compare this result with (1.37), taking $X = T .$ ）

1.4.10. Show that for $j = 1 , \ldots , n$

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | l _ { j , n } ( T ; x ) | \leqslant \sqrt { 2 } .
$$

We show next that Hermite interpolation in the Chebyshev nodes succeeds where Lagrange interpolation failed; i.e., given a continuous function it provides us with a sequence of polynomials that converges to the function. This result is due to L. Fejer [1].

Theorem 1.3. Let $f ( x )$ be continuous on $I .$ Let $W _ { 2 n - 1 } ( x )$ be the Hermite interpolating polynomial defined by the conditions

$$
\begin{array} { l } { { W _ { 2 n - 1 } ( \xi _ { j } ) = y _ { j } = f ( \xi _ { j } ) , \qquad j = 1 , \ldots , n , } } \\ { { \nonumber } } \\ { { W _ { 2 n - 1 } ^ { \prime } ( \xi _ { j } ) = 0 , \qquad j = 1 , \ldots , n ; } } \end{array}
$$

then

$$
\operatorname* { l i m } _ { n \to \infty } W _ { 2 n - 1 } ( x ) = f ( x )
$$

uniformly in $I .$

Proof. In view of (1.69) $( y _ { j } ^ { \prime } = 0 )$ ， we have

$$
W _ { 2 n - 1 } ( { \boldsymbol { x } } ) = \sum _ { j = 1 } ^ { n } ~ f ( \xi _ { j } ) h _ { j , n } ( T ; { \boldsymbol { x } } )
$$

and, recalling (1.73),

$$
f ( x ) = \sum _ { j = 1 } ^ { n } f ( x ) h _ { j , n } ( T ; x ) .
$$

Hence for $\boldsymbol { x } \in \boldsymbol { I }$

$$
| f ( x ) - W _ { 2 n - 1 } ( x ) | \leqslant \sum _ { j = 1 } ^ { n } | f ( x ) - f ( \xi _ { j } ) | h _ { j , n } ( T ; x ) ,
$$

since $h _ { j , n } ( T ; x ) \geqslant 0 , j = 1 , \ldots , n$ (cf. Exercise 1.4.3).

Given $\pmb \varepsilon > \mathbf 0$ ,let us choose $\delta > 0$ and so small that

$$
| f ( x ^ { \prime } ) - f ( x ^ { \prime \prime } ) | < \frac { \varepsilon } { 2 }
$$

whenever $| x ^ { \prime } - x ^ { \prime \prime } | < \delta , \ x ^ { \prime } , \ x ^ { \prime \prime } \in I .$ This can be done, for $f$ is uniformly continuous on $I .$ Fix $\boldsymbol { x } \in I$ and let $\pmb { \alpha }$ be the set of $j$ for which $| \xi _ { j } - x | < \delta ; \beta$ denotes the set of the remaining $j$ among $1 , \ldots , n .$ Then, in view of(1.74) and (1.73),

$$
\sum _ { j \in \alpha } | f ( x ) - f ( \xi _ { j } ) | h _ { j , n } ( T ; x ) < \frac { \varepsilon } { 2 } \sum _ { j \in \alpha } h _ { j , n } ( T ; x ) \leqslant \frac { \varepsilon } { 2 } \sum _ { j = 1 } ^ { n } h _ { j , n } ( T ; x ) = \frac { \varepsilon } { 2 } .
$$

Moreover, if $j \in \beta _ { : }$ ,then $| \xi _ { j } - x | \geqslant \delta$ and so

$$
h _ { j , n } ( T ; x ) = \frac { 1 - \xi _ { j } x } { n ^ { 2 } } \left( \frac { T _ { n } ( x ) } { x - \xi _ { j } } \right) ^ { 2 } < \frac { 2 } { n ^ { 2 } \delta ^ { 2 } } ,
$$

since $1 - \xi _ { j } x < 2$ and $T _ { n } ^ { 2 } ( x ) \leqslant 1$ If

$$
M = \underset { - 1 \leqslant x \leqslant 1 } { \mathbf { m a x } } ~ | f ( x ) | ,
$$

then $| f ( x ) - f ( \xi _ { j } ) | \leqslant 2 M , j = 1 , \ldots , n ,$ and

$$
\sum _ { j \in \beta } | f ( x ) - f ( \xi _ { j } ) | h _ { j , n } ( T ; x ) < \frac { 4 M } { n \delta ^ { 2 } } ,
$$

since the number of indices in $\beta$ does not exceed $\pmb { n }$

From (1.83), (1.84) and (1.85) we conclude that for each $\boldsymbol { x } \in \boldsymbol { I }$

$$
| f ( x ) - W _ { 2 n - 1 } ( x ) | < \frac { \varepsilon } { 2 } + \frac { 4 M } { n \delta ^ { 2 } } ,
$$

and so there exists $N$ such that for $n > N$

$$
| f ( x ) - W _ { 2 n - 1 } ( x ) | < \varepsilon ;
$$

i.e.,

$$
\operatorname* { l i m } _ { n \to \infty } W _ { 2 n - 1 } ( x ) = f ( x )
$$

uniformly in I.

An immediate consequence of Theorem 1.3 is the Weierstrass approxi-.mation theorem.

Theorem 1.4. Given $f ( x )$ continuous on $\pmb { I }$ and $\varepsilon > 0 ;$ ，there exists a polynomial, $p ( { \boldsymbol { x } } ) _ { : }$ ，such that

$$
| f ( x ) - p ( x ) | < \varepsilon
$$

for all $\boldsymbol { x } \in \boldsymbol { I }$

The Weierstrass theorem is the theoretical basis for the great utility of polynomials, since, roughly speaking, it enables us to replace any continuous function with a polynomial in the course of a mathematical argument.

Theorem 1.3 was proved by Fejer in 1916.In 1930 (Fejér [2]) he returned to the same topic and was able to improve the result by weakening the requirement in (1.81) that the derivative of the interpolating polynomial vanish at the Chebyshev nodes. More precisely he provided the following theorem.

Theorem 1.5. Let $f ( x )$ be continuous on $I .$ Let $W _ { 2 n - 1 } ( x )$ be a Hermite interpolating polynomial defined by the conditions

$$
\begin{array} { l c r } { { W _ { 2 n - 1 } ( \xi _ { j } ) = f ( \xi _ { j } ) , \qquad j = 1 , \ldots , n , } } \\ { { \nonumber } } \\ { { W _ { 2 n - 1 } ^ { \prime } ( \xi _ { j } ) = y _ { j } ^ { \prime } , \qquad j = 1 , \ldots , n , } } \end{array}
$$

where

$$
| y _ { j } ^ { \prime } | \leqslant \varepsilon _ { n } { \frac { n } { \log n } } \left( 1 - \xi _ { j } ^ { 2 } \right) ^ { - 1 / 2 } , \qquad j = 1 , \ldots , n ,
$$

with

$$
\operatorname* { l i m } _ { n  \infty } \varepsilon _ { n } = 0 .
$$

Then lim $W _ { 2 n - 1 } ( x ) = f ( x )$ uniformly in I. $\pmb { n }  \infty$

Proof.

$$
W _ { 2 n - 1 } ( x ) = \sum _ { j = 1 } ^ { n } \ f ( \xi _ { j } ) h _ { j } ( x ) + \sum _ { j = 1 } ^ { n } \ y _ { j } ^ { \prime } \mathfrak { h } _ { j } ( x ) ,
$$

but by Theorem 1.3 we know that

$$
\operatorname* { l i m } _ { n  \infty } ( \sum _ { j = 1 } ^ { n } f ( \xi _ { j } ) h _ { j } ( x ) ) = f ( x )
$$

uniformly in $I _ { \cdot }$ ,whereas in view of (1.78) and (1.86)

$$
\left| \sum _ { j = 1 } ^ { n } y _ { j } ^ { \prime } { \mathfrak h } _ { j } ( x ) \right| \leqslant \varepsilon _ { n } \left( { \frac { 2 } { \pi } } + { \frac { 1 } { \log n } } \right)
$$

and

$$
\varepsilon _ { n } \left( { \frac { 2 } { \pi } } + { \frac { 1 } { \log n } } \right) \to 0
$$

as $n  \infty$ , by (1.87), thus proving the theorem.

# EXERCISES 1.4.11-1.4.12

1.4.11. Prove that if $f ^ { \prime } ( x )$ is bounded on $\pmb { I }$ and $W _ { 2 n - 1 }$ satisfies

$$
\begin{array} { r l } { W _ { 2 n - 1 } ( \xi _ { j } ) = f ( \xi _ { j } ) , \quad } & { j = 1 , \ldots , n , } \\ { W _ { 2 n - 1 } ^ { \prime } ( \xi _ { j } ) = f ^ { \prime } ( \xi _ { j } ) , \quad } & { j = 1 , \ldots , n , } \end{array}
$$

Then lim $W _ { 2 n - 1 } ( x ) = f ( x )$ uniformly in I. n→8

1.4.12. Prove that if $f ^ { \prime } ( x )$ is continuous on $\pmb { I }$ ,the Weierstrass approximation theorem (Theorem 1.4) can be strengthened by adding the conclusion that $| f ^ { \prime } ( x ) - p ^ { \prime } ( x ) | < \varepsilon$ for all $\boldsymbol { x } \in \boldsymbol { I } .$

Hint.Apply Theorem 1.4 to $f ^ { \prime } ( x )$ and consider the indefinite integral of the polynomial thus obtained.

# 1.5. Orthogonality

Further interesting properties of the Chebyshev polynomials follow directly from the definition (1.2). It is easy to verify that for all nonnegative integers $m , k$

$$
\int _ { 0 } ^ { \pi } \cos { k \theta } \cos { m \theta } d \theta = 0 , \qquad m \neq k ,
$$

$$
\int _ { 0 } ^ { \pi } \cos ^ { 2 } k \theta ~ d \theta = { \Bigg \{ } { \frac { \pi } { 2 } } , \qquad k \neq 0 ,
$$

If we make the change of variables $\scriptstyle x = \cos \theta$ in (18.8a,b), we obtain the orthogonality relationship

$$
\int _ { - 1 } ^ { 1 } T _ { k } ( x ) T _ { m } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0 , \qquad m \ne k ,
$$

$$
\int _ { - 1 } ^ { 1 } T _ { k } ^ { 2 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \begin{array} { l l l } { \displaystyle \frac { \pi } { 2 } , } & { } & { k \neq 0 , } \\ { \displaystyle \pi , } & { } & { k = 0 ; } \end{array}
$$

that is to say, the Chebyshev polynomials $\lbrace T _ { n } ( x ) \rbrace _ { n = 0 } ^ { \infty }$ form a sequence of orthogonal polynomials on $\pmb { I }$ with respect to the weight function $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ As such they are members of several large, important, and much studied families of sequences of orthogonal polynomials:

1. Sequences of polynomials $\{ p _ { n } ( x ) \} _ { n = 0 } ^ { \infty }$ that satisfy

$$
\int _ { - 1 } ^ { 1 } p _ { k } ( x ) p _ { m } ( x ) w ( x ) d x = 0 , \qquad m \neq k ,
$$

with a weight function $w ( x ) \geqslant 0$ on $\pmb { I }$

2. The subset of (1) consisting of sequences of polynomials $\{ p _ { n } ^ { ( \alpha , \beta ) } ( x ) \} _ { n = 0 } ^ { \infty }$ that satisfy (1.90) with

$$
w ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } , ~ \alpha > - 1 , \beta > - 1 .
$$

These are called the Jacobi polynomials.

3. The subset of (2) consisting of sequences of polynomials $\{ p _ { n } ^ { ( \lambda ) } ( x ) \} _ { n = 0 } ^ { \infty }$ that satisfy (1.90) and (1.91) with $\alpha = \beta$ and $\begin{array} { r } { \lambda = \alpha + \frac { 1 } { 2 } . } \end{array}$ These are called the ultraspherical (or Gegenbauer) polynomials.

It is clear that the Chebyshev polynomials are ultraspherical polynomials with $\lambda = 0$ .We shall examine some properties of the Chebyshev polynomials that are characteristic of the larger classes of orthogonal polynomials mentioned above. The reader who is interested in seeing the generalizations of these results to the larger classes (and learning to which class a specific result generalizes) of orthogonal polynomials should consult Szego [i].

# 1. Second-Order Linear Homogeneous Differential Equation We saw in (1.23) that

$$
{ \frac { 1 } { n } } \ T _ { n } ^ { \prime } ( x ) = { \frac { \sin n \theta } { \sin \theta } } , \qquad x = \cos \theta .
$$

Therefore

$$
T _ { n } ^ { \prime \prime } ( x ) = n \frac { d } { d \theta } \left( \frac { \sin n \theta } { \sin \theta } \right) \biggl ( - \frac { 1 } { \sin \theta } \biggr ) ,
$$

from which it is easy to verify that $y = T _ { n } ( x )$ satisfies the second-order linear homogeneous differential equation

$$
( 1 - x ^ { 2 } ) y ^ { \prime \prime } - x y ^ { \prime } + n ^ { 2 } y = 0
$$

for $x \in I ,$ ,hence for all $\pmb { x }$

If we write (cf. (1.9))

$$
T _ { n } ( x ) = t _ { 0 } + t _ { 1 } x + \cdots + t _ { n } x ^ { n }
$$

and substitute in (1.92), we obtain

$$
( 1 - x ^ { 2 } ) \sum _ { k = 0 } ^ { n } k ( k - 1 ) t _ { k } x ^ { k - 2 } - x \sum _ { k = 0 } ^ { n } k t _ { k } x ^ { k - 1 } + n ^ { 2 } \sum _ { k = 0 } ^ { n } t _ { k } x ^ { k } = 0 ,
$$

or

$$
\sum _ { k = 0 } ^ { n } k ( k - 1 ) t _ { k } x ^ { k - 2 } + \sum _ { k = 0 } ^ { n } ( n ^ { 2 } - k ^ { 2 } ) t _ { k } x ^ { k } = 0 .
$$

Combining coefficients of like powers gives

$$
0 = \sum _ { k = 0 } ^ { n - 2 } { \bigl ( } t _ { k } ( n ^ { 2 } - k ^ { 2 } ) + t _ { k + 2 } ( k + 2 ) ( k + 1 ) { \bigr ) } x ^ { k } + ( n ^ { 2 } - ( n - 1 ) ^ { 2 } ) t _ { n - 1 } x ^ { n - 1 } ,
$$

from which we conclude that

$$
t _ { n - 1 } = 0
$$

and

$$
t _ { k } ( n ^ { 2 } - k ^ { 2 } ) + t _ { k + 2 } ( k + 2 ) ( k + 1 ) = 0 , \qquad k = 0 , \ldots , ( n - 2 ) .
$$

Equations (1.93) and (1.94) immediately imply (what we already knew; cf. (1.10)) that $t _ { n - ( 2 k - 1 ) } = 0$ Since,according to (1.14),

$$
t _ { n } = 2 ^ { n - 1 }
$$

we see that

$$
t _ { n - 2 } = - 2 ^ { n - 3 } \cdot { \frac { n ( n - 1 ) } { ( n - 1 ) } } = - { \frac { n } { 4 } } t _ { n }
$$

and

$$
t _ { n - 4 } = { \frac { n ( n - 1 ) ( n - 2 ) ( n - 3 ) } { 2 ! ( n - 1 ) ( n - 2 ) } } 2 ^ { n - 5 } .
$$

In general we have

$$
t _ { n - 2 m } = ( - 1 ) ^ { m } { \frac { n ( n - 1 ) \cdot \cdot \cdot ( n - 2 m + 1 ) } { m ! ( n - 1 ) ( n - 2 ) \cdot \cdot \cdot ( n - m ) } } 2 ^ { n - 2 m - 1 } ,
$$

as we may readily establish by mathematical induction. From (1.95) we easily obtain, for ${ \pmb n } > { \bf 0 }$ ，

$$
t _ { n - 2 m } ^ { ( n ) } = ( - 1 ) ^ { m } { \frac { n } { n - m } } { \binom { n - m } { m } } 2 ^ { n - 2 m - 1 } , \qquad m = 0 , 1 , \ldots , { \bigg [ } { \frac { n } { 2 } } { \bigg ] } ,
$$

a more concise form for the nonzero coefficients than we had before.

# EXERCISES 1.5.1-1.5.13

1.5.1. Show that if $- 1 \leqslant x \leqslant 1$ and $\pmb { n } \neq \mathbf { 0 }$

$$
\int _ { - 1 } ^ { x } T _ { n } ( t ) \frac { d t } { \sqrt { 1 - t ^ { 2 } } } = - \frac { \sqrt { 1 - x ^ { 2 } } U _ { n - 1 } ( x ) } { n } ,
$$

hence

$$
\left| \int _ { - 1 } ^ { x } T _ { n } ( t ) \frac { d t } { \sqrt { 1 - t ^ { 2 } } } \right| \leqslant \frac { 1 } { n } .
$$

1.5.2. Show that for $n \geqslant 1$

$$
\int _ { - 1 } ^ { 1 } | T _ { n } ( t ) | \frac { d t } { \sqrt { 1 - t ^ { 2 } } } = 2 .
$$

# 1.5.3. Show that for $\pmb { n } \geqslant 2$

$$
I _ { n } = \int _ { - 1 } ^ { 1 } \left| T _ { n } ( x ) \right| d x = \frac { 2 } { n ^ { 2 } - 1 } \left[ \frac { n } { \sin \pi / 2 n } - 1 \right] .
$$

(b) $I _ { 1 } , I _ { 2 } , I _ { 3 } , \ldots$ , is a monotone-increasing sequence with limit $4 / \pi$

1.5.4. If the polynomial $p \left( \neq 0 \right)$ satisfies the differential equation (1.92), then $p = c T _ { n }$ for some constant $^ { c }$

Hint. Putting ${ \boldsymbol { y } } = { \boldsymbol { p } }$ in (1.92) yields a polynomial identity. Examine the leading coefficient on the left and thereby determine the degree of $\pmb { p }$

1.5.5. Show that for $k \geqslant 1$

$$
( 1 - x ^ { 2 } ) T _ { n } ^ { ( k + 1 ) } ( x ) - ( 2 k - 1 ) x T _ { n } ^ { ( k ) } ( x ) + ( n ^ { 2 } - ( k - 1 ) ^ { 2 } ) T _ { n } ^ { ( k - 1 ) } ( x ) = 0 .
$$

# 1.5.6. Verify that

$$
T _ { n } ^ { ( k ) } ( 1 ) = \frac { n ^ { 2 } ( n ^ { 2 } - 1 ) ( n ^ { 2 } - 2 ^ { 2 } ) \cdot \cdot \cdot ( n ^ { 2 } - ( k - 1 ) ^ { 2 } ) } { 1 . 3 . 5 \cdot \cdot \cdot ( 2 k - 1 ) } .
$$

1.5.7. Show that (1.60) may be simplifed and writen

$$
L _ { n } ( f , U ; x ) = \frac { ( 1 - x ^ { 2 } ) T _ { n } ^ { \prime } ( x ) } { n ^ { 2 } } \sum _ { j = 0 } ^ { n } { } ^ { \stackrel { \prime } { } } ( - 1 ) ^ { j + 1 } \frac { f ( \eta _ { j } ) } { ( x - \eta _ { j } ) } ,
$$

where $\Sigma ^ { \prime \prime }$ is a“trapezoidal"” sum:; i.e.,

$$
\sum _ { j = 0 } ^ { n } \sp { \prime \prime } u _ { j } = { \textstyle { \frac { 1 } { 2 } } } u _ { 0 } + u _ { 1 } + u _ { 2 } + \cdots + u _ { n - 1 } + { \textstyle { \frac { 1 } { 2 } } } u _ { n } .
$$

1.5.8. (Duffin and Schaeffer [1]) Prove that if $\pmb { p } \in \mathcal { P } _ { \pmb { \pi } }$ and

$$
| p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

then

$$
| p ^ { \prime } ( \xi _ { j } ^ { ( n ) } ) | \leqslant n ( 1 - ( \xi _ { j } ^ { ( n ) } ) ^ { 2 } ) ^ { - 1 / 2 } = | T _ { n } ^ { \prime } ( \xi _ { j } ^ { ( n ) } ) | , \qquad j = 1 , \ldots , n .
$$

Equality in (1.100) occurs for any one $^ j$ only if $p ( x ) = \pm T _ { n } ( x ) .$

Hint. Note that $p ^ { \prime } ( \xi _ { j } ) = L _ { n } ^ { \prime } ( p , \ U ; \ \xi _ { j } ) ;$ hence $T _ { n } ^ { \prime } ( \xi _ { j } ) = L _ { n } ^ { \prime } ( T _ { n } , ~ U ; ~ \xi _ { j } )$ and recall Exercise 1.2.3.

1.5.9. (Duffin and Schaeffer [1]) Prove that if $\pmb { p } \in \mathcal { P } _ { n }$ and

$$
| p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

then

$$
| p ^ { ( k ) } ( \tau ) | \leqslant | T _ { n } ^ { ( k ) } ( \tau ) | , \qquad k = 1 , \dots , n ,
$$

where $\pmb { \tau }$ is any zero of $T _ { n } ^ { ( k - 1 ) } ( x ) .$ .Equality occurs for any single $\pmb { \tau }$ only if $p = \pm T _ { n } ( x )$

Hint. Note that $k = 1$ is Exercise 1.5.8. Use mathematical induction on $\pmb { k }$ and express $\pmb { p } ^ { ( k ) }$ as its own interpolating polynomial in the zeros of $T _ { n } ^ { ( k - 1 ) }$

.1.5.10. If $\pmb { p } \in \mathcal { P } _ { n }$ and

$$
| p ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

show that

$$
\vert p ^ { ( k ) } ( x ) \vert \leqslant T _ { n } ^ { ( k ) } ( x ) , \qquad x \geqslant u ,
$$

where $\pmb { u }$ is the largest zero of $T _ { n } ^ { ( k - 1 ) } ( x ) ,$

1.5.11. (Rogosinski [1]) If $\pmb { p } \in \mathcal { P } _ { n }$ and

$$
| \mathbb { p } ( \eta _ { j } ^ { ( n ) } ) | \leqslant 1 , \qquad j = 0 , \ldots , n ,
$$

then

$$
| p ^ { ( k ) } ( t ) | \leqslant | T _ { n } ^ { ( k ) } ( t ) | , | t | \geqslant 1 , \qquad k = 0 , \ldots , n ,
$$

with equality only if $p = \pm T _ { n }$ for $k \geqslant 1$ and $k = 0 , \left| t \right| > 1$

1.5.12. Show that for all nonnegative integers $m , k$

$$
\int _ { - 1 } ^ { 1 } U _ { k } ( x ) U _ { m } ( x ) { \sqrt { 1 - x ^ { 2 } } } d x = { \left\{ \begin{array} { l l } { 0 , } & { \quad k \neq m , } \\ { \pi } \\ { { \overline { { 2 } } } ^ { , } } & { \quad k = m . } \end{array} \right. }
$$

Thus the Chebyshev polynomials of the second kind are ultraspherical polynomials, $p _ { n } ^ { ( \lambda ) } ( x ) ,$ with $\lambda = 1$

# 1.5.13. Show that

$$
U _ { n } \left( { \frac { x } { 2 } } \right) = \sum _ { k = 0 } ^ { [ n / 2 ] } ( - 1 ) ^ { k } \left( { n - k } \right) x ^ { n - 2 k } .
$$

# 2. Three-Term Recurrence Formula

The three-term recurrence formula satisfied by the Chebyshev polynomials is the translation of the elementary trigonometric identity

$$
\cos n \theta + \cos ( n - 2 ) \theta = 2 \cos \theta \cos ( n - 1 ) \theta ,
$$

which becomes

$$
T _ { n } ( x ) = 2 x T _ { n - 1 } ( x ) - T _ { n - 2 } ( x ) , n = 2 , 3 , \ldots ,
$$

with $T _ { 0 } ( x ) = 1$ and $T _ { 1 } ( x ) = x $

# EXERCISES 1.5.14-1.5.19

1.5.14. Show that (1.101) is valid for $\displaystyle n = 0 , \pm 1 , \pm 2 , \ldots$ , if we put

$$
T _ { - n } = T _ { n }
$$

for positive integers $\pmb { n }$

1.5.15. Show that no two consecutive Chebyshev polynomials, $T _ { k } ( x ) , T _ { k + 1 } ( x ) ,$ have a zero in common.

1.5.16.

$$
( 1 - x ^ { 2 } ) T _ { n } ^ { \prime } ( x ) = n [ T _ { n - 1 } ( x ) - x \dot { T } _ { n } ( x ) ] .
$$

# 1.5.17. Show that

$$
\sum _ { j = 0 } ^ { n } { ^ { \prime } T _ { j } ( x ) T _ { j } ( y ) } = { \frac { 1 } { 2 } \left[ \frac { T _ { n + 1 } ( x ) T _ { n } ( y ) - T _ { n } ( x ) T _ { n + 1 } ( y ) } { x - y } \right] }
$$

where $\Sigma _ { j = 0 } ^ { \prime n } u _ { j }$ means

$$
{ \textstyle \frac { 1 } { 2 } } u _ { 0 } + u _ { 1 } + u _ { 2 } + \cdots + u _ { n } .
$$

(1.102) is called the Christoffel-Darboux formula.

# 1.5.18. Show that

$$
2 \sum _ { j = 0 } ^ { n } { } ^ { \stackrel { \prime } { T } } { } _ { j } ^ { 2 } = T _ { n + 1 } ^ { \prime } T _ { n } - T _ { n + 1 } T _ { n } ^ { \prime } ,
$$

hence that

$$
T _ { n + 1 } ^ { \prime } T _ { n } - T _ { n + 1 } T _ { n } ^ { \prime } \geqslant 1 .
$$

Also show that $T _ { n + 1 } ^ { 2 } ( x ) - T _ { n } ( x ) T _ { n + 2 } ( x ) = 1 - x ^ { 2 } , n = 0 , 1 , 2 , \ldots .$

Hint. Apply the recurrence formula to obtain $T _ { n + 1 } ^ { 2 } ( x ) - T _ { n } ( x ) T _ { n + 2 } ( x ) =$ $T _ { n } ^ { 2 } ( x ) - T _ { n - 1 } ( x ) T _ { n + 1 } ( x ) .$

1.5.19.Show that the Chebyshev polynomials of the second kind satisfy the threeterm recurrence formula $U _ { n } ( x ) = 2 x U _ { n - 1 } ( x ) - U _ { n - 2 } ( x ) ,$ $\pmb { n } = 2 ,$ ，3,..., (identical to (1.101)) with $U _ { \circ } ( { \pmb x } ) = { \pmb 1 }$ and $U _ { 1 } ( x ) = 2 x$

(a) Also show that $U _ { n + 1 } ^ { 2 } - U _ { n } U _ { n + 2 } = 1$ ， $\pmb { n = 0 }$ ， 1, 2,... Note that the three-term recurrence formula is valid for $n = 0 , \pm 1 , \pm 2 , \ldots ,$ if we put $U _ { - n } ( x ) = - U _ { n - 2 } ( x ) .$

(b) Show that the fundamental polynomials for Lagrange interpolation at the extrema of $\smash { T _ { n } ( x ) }$ are

$$
l _ { k , n + 1 } ( U ; x ) = \left\{ \begin{array} { l l } { \displaystyle \frac { 2 } { n } \sum _ { j = 0 } ^ { n } T _ { j } ( \eta _ { k } ^ { ( n ) } ) T _ { j } ( x ) , } & { \quad 0 < k < n , } \\ { \displaystyle \frac { 1 } { n } \sum _ { j = 0 } ^ { n } T _ { j } ( \eta _ { k } ^ { ( n ) } ) T _ { j } ( x ) , } & { \quad k = 0 , n . } \end{array} \right.
$$

Hint.Put $y = \eta _ { k } ^ { ( n ) }$ in (1.102) and note Exercise 1.2.15c and (1.98).

# 3.Generating Function

Suppose that $| u | < 1$ ,then

$$
\sum _ { n = 0 } ^ { \infty } u ^ { n } e ^ { i n \theta } = \sum _ { n = 0 } ^ { \infty } ( u e ^ { i \theta } ) ^ { n } = { \frac { 1 } { 1 - u e ^ { i \theta } } } .
$$

On equating the real parts of this equality, we obtain

$$
\sum _ { n = 0 } ^ { \infty } \ u ^ { n } \cos \ n \theta = { \frac { \cdot \ 1 - u \cos \ \theta } { 1 + u ^ { 2 } - 2 u \cos \ \theta } }
$$

or

$$
F ( u , x ) = { \frac { 1 - u x } { 1 + u ^ { 2 } - 2 u x } } = \sum _ { n = 0 } ^ { \infty } T _ { n } ( x ) u ^ { n } , \qquad x \in I .
$$

The function $\pmb { F } ( \pmb { u } , \pmb { x } )$ is called a generating function for the Chebyshev polynomials, since they appear as the coeffcients in its expansion in powers of $\pmb { u }$

It is interesting to remark that we can recover (1.96) from (1.105). To do so we note that

$$
F \left( u , { \frac { x } { 2 } } \right) = \left( 1 - { \frac { u x } { 2 } } \right) { \frac { 1 } { 1 - u ( x - u ) } } .
$$

If we suppose that $\begin{array} { r } { | u | \leqslant \frac { 1 } { 2 } } \end{array}$ and that $\boldsymbol { x } \in \boldsymbol { I } ,$ then

$$
\begin{array} { r } { - \frac { 3 } { 4 } \leqslant u ( x - u ) \leqslant \frac { 1 } { 4 } } \end{array}
$$

and so

$$
{ \frac { 1 } { 1 - u ( x - u ) } } = \sum _ { k = 0 } ^ { \infty } \left( u ( x - u ) \right) ^ { k } = \sum _ { k = 0 } ^ { \infty } u ^ { k } ( x - u ) ^ { k } .
$$

The coefficient of $\pmb { u } ^ { m }$ in the right-most expression in (1.107) is

$$
\begin{array} { l }  { { \displaystyle x ^ { m } - \left( \begin{array} { c } { { m - 1 } } \\ { { 1 } } \end{array} \right) x ^ { m - 2 } + \left( \begin{array} { c } { { m - 2 } } \\ { { 2 } } \end{array} \right) x ^ { m - 4 } + \dots + ( - 1 ) ^ { j } \left( \begin{array} { c } { { m - j } } \\ { { j } } \end{array} \right) x ^ { m - 2 j } } } \\ { { { + \dots + ( - 1 ) ^ { [ m / 2 ] } \left( \begin{array} { c } { { n - [ m / 2 ] } } \\ { { [ m / 2 ] } } \end{array} \right) x ^ { m - 2 [ m / 2 ] } } , } } \end{array}
$$

as we can see by starting with the term $k = m$ in the infinite series, extracting from it the term in ${ \pmb u } ^ { m } ,$ ，then considering the term $k = m - 1$ in the infinite series,extracting from it the term in ${ \pmb u } ^ { m } ;$ ,and so on. (As an aside, compare Exercise 1.5.13. We have stumbled on the generating function of $\{ U _ { n } ( { \pmb x } / 2 ) \} .$ Therefore the coefficient of $\pmb { u } ^ { n }$ in the expansion $F ( u , x / 2 )$ is, in view of (1.106) and (1.107),

$$
T _ { n } \left( \frac { x } { 2 } \right) = \sum _ { k = 0 } ^ { [ ( n - 1 ) / 2 ] } ( - 1 ) ^ { k } \left[ \binom { n - k } { k } - \frac { 1 } { 2 } \binom { n - 1 - k } { k } \right] x ^ { n - 2 k } + \cos \frac { n \pi } { 2 } ,
$$

and since this equality holds for $\boldsymbol { x } \in \boldsymbol { I }$ , it holds for all $\mathbf { \boldsymbol { x } } ;$ but

$$
{ \binom { n - k } { k } } - { \frac { 1 } { 2 } } { \binom { n - 1 - k } { k } } = { \frac { 1 } { 2 } } { \frac { n - k } { k } } { \binom { n - k } { k } } ,
$$

and so replacing $_ x$ with $_ { 2 x }$ in (1.108) enables us to recover (1.96).

Note that, if we put $\boldsymbol { x } = \cos { \theta }$ and put $P _ { u } ( \theta ) = 2 F ( u , \cos \theta ) - 1$ ,then (1.105) yields

$$
P _ { u } ( \theta ) = \frac { 1 - u ^ { 2 } } { 1 - 2 u \cos \theta + u ^ { 2 } } = 1 + 2 \sum _ { n = 1 } ^ { \infty } u ^ { n } \cos n \theta .
$$

The generating function, $P _ { u } ( \theta ) ,$ ， is called the Poisson kernel and plays an important role in function theory (See Bak and Newman [1], for example).

# 4. Least Squares

We show next that if

$$
p ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n - 1 } x ^ { n - 1 } + x ^ { n } , \qquad n > 0
$$

then

$$
\int _ { - 1 } ^ { 1 } p ^ { 2 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } \geqslant \int _ { - 1 } ^ { 1 } \widetilde { T } _ { n } ^ { 2 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 2 ^ { 1 - 2 n } \pi
$$

with equality only if $p = \widetilde { T } _ { n }$ ; that is to say, among allpolynomials of degree n having leading coefficient 1 the normalized Chebyshev polynomial has the least integral of its square with respect to the weight function $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$

To prove (1.109) we write $p ( x ) = b _ { 0 } T _ { 0 } ( x ) + \cdots + b _ { n } T _ { n } ( x ) ,$ where (cf. Exercise 1.2.6) $b _ { n } = 2 ^ { - ( n - 1 ) }$ ,and consider

$$
\begin{array} { c } { { \displaystyle { \int _ { - 1 } ^ { 1 } \left( \tilde { T } _ { n } ( x ) - p ( x ) \right) ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \int _ { - 1 } ^ { 1 } \tilde { T } _ { n } ^ { 2 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } + \int _ { - 1 } ^ { 1 } p ^ { 2 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } } } \\ { { - 2 \displaystyle { \int _ { - 1 } ^ { 1 } \left( b _ { 0 } + b _ { 1 } T _ { 1 } ( x ) + \cdots + b _ { n } T _ { n } ( x ) \right) \tilde { T } _ { n } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } . \qquad ( 1 . 1 1 \eqno { ( 1 . 1 7 ) } } } \end{array}
$$

But the orthogonality relationship (1.89) implies that the·last term on the right-hand side of (1.110) is equal to

$$
- 2 \int _ { - 1 } ^ { 1 } \widetilde { T } _ { n } ^ { 2 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } .
$$

Moreover, the left-hand side of(1.11O) is nonnegative (since it is the integral of a nonnegative integrand) and zero if and only if $p = \widetilde { T } _ { n }$ . Equation (1.109) follows at once, the value of the minimal integral following from (1.89b).

# 5. Numerical Integration

Numerical integration is approximation of the definite integral by finite sums. A typical numerical integration formula involves approximating

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x
$$

by

$$
\sum _ { i = 1 } ^ { n } A _ { i } ^ { ( n ) } f ( x _ { i } ^ { ( n ) } )
$$

for all $f$ continuous on I. One criterion of the goodness of the approximation (1.112) to (1.111) is to require that (1.112) be equal to (1.111) for $f \in \mathcal { P } _ { k }$ and $\pmb { k }$ as large as possible. A reason for adopting this criterion is that, according to the Weierstrass approximation theorem (Theorem 1.4), every continuous function on $\pmb { I }$ can be uniformly approximated,arbitrarily closely，by polynomials.

In order to integrate every $f \in \mathcal { P } _ { k }$ exactly by means of (1.112) it suffices to choose the ${ A } _ { i } ^ { ( n ) }$ and ${ \pmb x } _ { i } ^ { ( n ) }$ in (1.112) to satisfy

$$
\sum _ { i = 1 } ^ { n } \ A _ { i } ^ { ( n ) } ( x _ { i } ^ { ( n ) } ) ^ { j } = \int _ { - 1 } ^ { 1 } x ^ { j } d x , \qquad j = 0 , 1 , . . . , k .
$$

We have 2n unknowns in the system of $k + 1$ equations (1.113). Therefore the largest $\pmb { k }$ for which we can generally expect to solve this system is $k = 2 n - 1 ;$ hence we can expect to integrate exactly all $f \in \mathcal { P } _ { 2 n - 1 }$ ,at most, by suitable choice of nodes and coefficients in (1.112).

The choice of the zeros of the Chebyshev polynomials as nodes in (1.112) leads to an optimal numerical integration formula, not, however, for (1.111) but for

$$
\int _ { - 1 } ^ { 1 } { \frac { f ( x ) } { \sqrt { 1 - x ^ { 2 } } } } d x .
$$

We proceed next to produce this formula. Suppose that $\pmb { p } \in \mathcal { P } _ { 2 n - 1 }$ ； then the Lagrange interpolating polynomial to $\pmb { p }$ at the zeros of $T _ { n } ( x )$ is

$$
L _ { n - 1 } ( p , T ; x ) = \sum _ { j = 1 } ^ { n } \frac { p ( \xi _ { j } ) T _ { n } ( x ) } { T _ { n } ^ { \prime } ( \xi _ { j } ) ( x - \xi _ { j } ) } .
$$

Since $p ( x ) - L _ { n - 1 } ( x ) = 0$ for $\pmb { x } = \xi _ { 1 } , \ldots , \xi _ { n }$ ， we can write

$$
p ( x ) - L _ { n - 1 } ( x ) = T _ { n } ( x ) r ( x ) ,
$$

where $\boldsymbol { r } ( \boldsymbol { x } ) \in \mathcal { P } _ { n - 1 }$ . In view of Exercise 1.2.6 and the orthogonality relationships (1.89a)

$$
\int _ { - 1 } ^ { 1 } T _ { n } ( x ) r ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0 ,
$$

and so (1.116) implies

$$
\int _ { - 1 } ^ { 1 } p ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( p , T ; x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } ,
$$

but, if we evaluate the integral on the right-hand side of (1.117) in view of (1.115), we obtain

$$
\int _ { - 1 } ^ { 1 } \frac { p ( x ) } { \sqrt { 1 - x ^ { 2 } } } d x = \sum _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( n ) } p ( \xi _ { j } ^ { ( n ) } ) ,
$$

where

$$
\lambda _ { j } ^ { ( n ) } = \frac { 1 } { T _ { n } ^ { \prime } ( \xi _ { j } ^ { ( n ) } ) } \int _ { - 1 } ^ { 1 } \frac { T _ { n } ( x ) } { ( x - \xi _ { j } ^ { ( n ) } ) } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } .
$$

In other words, the numerical integration formula

$$
\sum _ { j = 1 } ^ { n } \lambda _ { j } ^ { ( n ) } f ( \xi _ { j } ^ { ( n ) } ) ,
$$

where $\lambda _ { j } ^ { ( n ) }$ is defined in (1.119),evaluates the integral (1.114) exactly if $f \in \mathscr { P } _ { 2 n - 1 }$ .Formula (1.120) is simply the integral with respect to the weight function $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ of $L _ { n - 1 } ( f , T ; x )$

·The formula analogous to (1.12O) for (1.111) is due to Gauss and called Gauss's quadrature formula (quadrature being a synonym of numerical integration). It is derived by using the zeros of the set of polynomials orthogonal on $\pmb { I }$ with weight function $w ( x ) = 1$ , the Legendre polynomials, in place of the zeros of the Chebyshev polynomials in (1.115). The reader is once again referred to Szego [1] for details. Formula (1.120) is sometimes called the Gauss-Chebyshev quadrature formula.

Formula (1.120) cannot evaluate (1.114) exactly for all $f \in \mathcal { P } _ { 2 n } .$ forif $f ( x ) = T _ { n } ^ { 2 } ( x ) \in \mathcal { P } _ { n }$ then (1.114) is positive and (1.120) is zero. Indeed, there is no formula

$$
\sum _ { i = 1 } ^ { n } c _ { i } f ( x _ { i } ) , \qquad c _ { i } \ne 0 , i = 1 , . . . , n ,
$$

that evaluates (1.114) exactly for $f \in \mathcal { P } _ { m }$ with $m \geqslant 2 n - 1$ other than (1.120), for if there were put $\omega ( x ) = ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } )$ Say $\mathbf { \Delta } _ { \mathbf { x } _ { k } }$ is not one of the $\xi _ { j } ^ { ( n ) }$ Consider

$$
f ( x ) = { \frac { \omega ( x ) T _ { n } ( x ) } { x - x _ { k } } } ;
$$

then $f \in \mathscr { P } _ { 2 n - 1 }$ ,(1.120) is zero,and therefore (1.114) is also, but (1.121) yields the value $c _ { k } \omega ^ { \prime } ( x _ { k } ) T _ { n } ( x _ { k } ) \neq 0 .$ Thus, possibly after renumbering, $x _ { j } = \xi _ { j } ^ { ( n ) } , j = 1 ,$ $\cdots , n .$ Finally, putting $f ( x ) = T _ { n } ( x ) / ( x - \xi _ { j } )$ in (1.121) and (1.120) yields

$$
c _ { j } = \lambda _ { j } ^ { ( n ) } = \frac { 1 } { T _ { n } ^ { \prime } ( \xi _ { j } ) } \int _ { - 1 } ^ { 1 } \frac { T _ { n } ( x ) } { x - \xi _ { j } } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } .
$$

We want to show next that (1.119) can be considerably simplified. Indeed

$$
\lambda _ { j } ^ { ( n ) } = \frac { \pi } { n } , \qquad j = 1 , \ldots , n ,
$$

so that (1.120) has the particularly simple form

$$
\frac { \pi } { n } \sum _ { j = 1 } ^ { n } f ( \xi _ { j } ^ { ( n ) } ) .
$$

To prove (1.122) we put $\boldsymbol { y } = \boldsymbol { \xi } _ { i }$ in (1.102), which then becomes

$$
\sum _ { j = 0 } ^ { n } T _ { j } ( x ) T _ { j } ( \xi _ { i } ) = - \frac { 1 } { 2 } T _ { n + 1 } ( \xi _ { i } ) \frac { T _ { n } ( x ) } { x - \xi _ { i } } .
$$

If we now multiply both sides of this identity by $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ and then integrate over $I _ { : }$ ，we obtain, in view of the orthogonality relationships,

$$
\frac { \pi } { 2 } = - { \textstyle \frac { 1 } { 2 } } T _ { n + 1 } ( \xi _ { i } ) T _ { n } ^ { \prime } ( \xi _ { i } ) \lambda _ { i } ^ { ( n ) } .
$$

Equations (1.122) now follow from Exercises 1.2.3 and 1.2.7.

We observe, finally, that the approximation (1.123) to (1.114) converges to (1.114) as ${ \pmb n }  \infty$ ,for

$$
{ \frac { \pi } { n } } \sum _ { j = 1 } ^ { n } ~ f ( \xi _ { j } ^ { ( n ) } ) = { \frac { \pi } { n } } \sum _ { j = 1 } ^ { n } ~ f { \biggl ( } \cos \left( 2 j - 1 \right) { \frac { \pi } { 2 n } } { \biggr ) } ,
$$

and since $f ( x )$ is continuous on $I _ { : }$ ，the right-hand side of this equality converges to

$$
\int _ { 0 } ^ { \pi } f ( \cos \theta ) d \theta = \int _ { - 1 } ^ { 1 } { \frac { f ( x ) } { \sqrt { 1 - x ^ { 2 } } } } d x
$$

as ${ \pmb n }  \infty$ ·

# EXERCISES 1.5.20-1.5.25

1.5.20. Equations (1.122) are equivalent to

$$
\frac { \pi } { n } = \int _ { - 1 } ^ { 1 } l _ { j , n } ( T ; x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } }
$$

(the $l _ { j , n } ( T ; x )$ are the fundamental polynomials of Lagrange interpolation at the zeros of the Chebyshev polynomials). Show that

$$
\int _ { - 1 } ^ { 1 } l _ { j , n } ( T ; x ) l _ { k , n } ( T ; x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0 , j \neq k ; j , k = 1 , \dots , n .
$$

# 1.5.21. Show that

$$
\frac { \pi } { n } = \int _ { - 1 } ^ { 1 } [ l _ { j , n } ( T ; x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } , \qquad j = 1 , \ldots , n .
$$

Hint. Substitute $p ( x ) = [ l _ { j , n } ( T ; x ) ] ^ { 2 } \in \mathcal { P } _ { 2 n - 1 }$ in (1.118). Note the remarkable result implied by (1.124)and (1.125). Also summing both sides of(1.125)on j from 1 to $\pmb { n }$ gives

$$
\int _ { - 1 } ^ { 1 } \sum _ { j = 1 } ^ { n } [ l _ { j , n } ( T ; x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \pi ,
$$

which should be compared to Exercise 1.4.9.

1.5.22. Generalization of Exercise 1.5.20. Prove that if $\pmb { k }$ is even and $\boldsymbol { n } ( 1 ) , \ldots , \boldsymbol { n } ( k )$ are distinct integers satisfying $1 \leqslant n ( i ) \leqslant n$ then

$$
\int _ { - 1 } ^ { 1 } l _ { n ( 1 ) , n } ( T ; x ) l _ { n ( 2 ) , n } ( T ; x ) \cdot \cdot \cdot l _ { n ( k ) , n } ( T ; x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0 .
$$

Hint. $l _ { n ( 1 ) } ( x ) \cdot \cdot \cdot l _ { n ( k ) } ( x ) = c ( T _ { n } ( x ) ) ^ { k - 1 } T _ { n } ( x ) / [ ( x - \xi _ { n ( 1 ) } ) \cdot \cdot \cdot ( x - \xi _ { n ( k ) } ) ]$ andrecall Exercise 1.2.12.

1.5.23. If $\pmb { n } ( 1 ) , . . . , \pmb { n } ( \pmb { m } )$ are distinct integers that satisfy $1 \leqslant n ( i ) \leqslant n ,$ show that

$$
\int _ { - 1 } ^ { 1 } { \mathfrak { h } } _ { n ( 1 ) } ( x ) \cdots { \mathfrak { h } } _ { n ( m ) } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = 0 ,
$$

where the ${ \mathfrak { h } } _ { n ( i ) }$ .are defined in (1.72). However, also show that

$$
\int _ { - 1 } ^ { 1 } h _ { i } ( x ) h _ { k } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } \neq 0 ,
$$

where the $h _ { j }$ are defined in (1.71).

1.5.24. Suppose $f ( x )$ is continuous on $\pmb { I }$ and $W _ { 2 n - 1 }$ is the Hermite interpolating polynomial defined by

$$
\begin{array} { l c r } { { W _ { 2 n - 1 } ( \xi _ { j } ) = f ( \xi _ { j } ) , \qquad j = 1 , \ldots , n , } } \\ { { \nonumber } } \\ { { W _ { 2 n - 1 } ^ { \prime } ( \xi _ { j } ) = y _ { j } ^ { \prime } , \qquad j = 1 , \ldots , n , } } \end{array}
$$

where the $y _ { j } ^ { \prime } , j = 1 , . . . , n ,$ are any given real numbers. Show that

$$
\operatorname * { l i m } _ { n  \infty } \int _ { - 1 } ^ { 1 } W _ { 2 n - 1 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \int _ { - 1 } ^ { 1 } \frac { f ( x ) } { \sqrt { 1 - x ^ { 2 } } } d x .
$$

1.5.25. If $F ( \theta ) = f ( \cos \pi \theta ) = f ( x )$ satisfies $F ^ { \prime \prime } ( \theta ) \geqslant 0$ and $F ^ { \prime \prime } ( \theta ) \geqslant 0$ for $0 \leqslant \theta \leqslant 1$ ,show that the Gauss-Chebyshev quadrature formulas increase monotonically to (1.114) as $\pmb { n }$ increases.

Any $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ has a“Chebyshev expansion,” i.e., it can be written as

$$
p ( x ) = { \frac { A _ { 0 } } { 2 } } + A _ { 1 } T _ { 1 } ( x ) + \cdots + A _ { n } T _ { n } ( x ) .
$$

The coefficients $A _ { 0 } , A _ { 1 } , \ldots , A _ { n }$ are easily determined. We multiply both sides of (1.126) by $T _ { m } ( x ) ( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ and integrate the resulting equality to obtain

$$
\int _ { - 1 } ^ { 1 } p ( x ) T _ { m } ( x ) { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } = \sum _ { k = 0 } ^ { n } A _ { k } \int _ { - 1 } ^ { 1 } T _ { k } ( x ) T _ { m } ( x ) { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } . \dagger
$$

The orthogonality relationship (1.89) now yields

$$
A _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } p ( x ) T _ { k } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } , \qquad k = 0 , . . . , n ,
$$

as the formula for the coeffcients in (1.126).(It was to avoid singling out the case $k = 0$ that we took the first term in (1.126) to be $A _ { 0 } / 2 . )$ Let us, for example, obtain the Chebyshev expansion (1.126) for $L _ { n - 1 } ( f , T ; x ) \in { \mathcal { P } } _ { n - 1 }$ Suppose that

$$
{ \cal L } _ { n - 1 } ( f , T ; x ) = \sum _ { m = 0 } ^ { n - 1 } \alpha _ { m } T _ { m } ( x ) ,
$$

then

$$
\alpha _ { m } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( x ) T _ { m } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } ;
$$

but $L _ { n - 1 } ( x ) T _ { m } ( x ) \in \mathcal { P } _ { 2 n - 1 }$ ,hence (1.118) applies and we obtain

$$
\alpha _ { m } = \frac { 2 } { n } \sum _ { j = 1 } ^ { n } L _ { n - 1 } ( \xi _ { j } ) T _ { m } ( \xi _ { j } )
$$

or

$$
\alpha _ { m } = \frac { 2 } { n } \sum _ { j = 1 } ^ { n } f ( \xi _ { j } ) T _ { m } ( \xi _ { j } ) , \qquad m = 0 , \dots , n - 1 .
$$

In particular, if $f ( \xi _ { k } ) = 1$ and $f ( \xi _ { i } ) = 0 , \ i \neq k ,$ then $L _ { n - 1 } ( f , T ; x ) =$ $l _ { k , n } ( T , x ) ,$ , and we obtain

$$
l _ { k , n } ( T ; x ) = l _ { k } ( x ) = \frac { 2 } { n } \sum _ { m = 0 } ^ { n - 1 } T _ { m } ( \xi _ { k } ) T _ { m } ( x ) .
$$

†The notation ${ \pmb { \Sigma } } ^ { \prime }$ is defined following (1.102).

The expression (1.130) has some remarkable consequences. In the preceding section we proved that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( f , T ; x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \int _ { - 1 } ^ { 1 } \frac { f ( x ) } { \sqrt { 1 - x ^ { 2 } } } d x
$$

for $f ( x )$ continuous on $I .$ .The integral appearing on the left-hand side of (1.131) is precisely (1.123) and so we had a particularly simple numerical integration formula for (1.114). We wish to show next that

$$
\int _ { - 1 } ^ { 1 } L _ { n - 1 } ( f , T ; x ) d x = \sum _ { i = 1 } ^ { n } f ( \xi _ { i } ) \int _ { - 1 } ^ { 1 } l _ { i } ( x ) d x
$$

is an effective numerical integration formula for

$$
\int _ { - 1 } ^ { 1 } f ( x ) d x
$$

in the sense that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( f , T ; x ) d x = \int _ { - 1 } ^ { 1 } f ( x ) d x .
$$

# Theorem 1.6. If

$$
\mu _ { i } = \mu _ { i } ^ { ( n ) } = \int _ { - 1 } ^ { 1 } l _ { i , n } ( T , x ) d x ,
$$

then, if $f ( x )$ is continuous on $I _ { \mathrm { - } }$ ，

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k \mathop { = } 1 } ^ { n } \mu _ { i } ^ { ( n ) } f ( \xi _ { j } ^ { ( n ) } ) = \int _ { - 1 } ^ { 1 } f ( x ) d x .
$$

Proof. We first establish that $\mu _ { i } > 0 , i = 1 , . . . , n .$

$$
\begin{array} { l } { \displaystyle \mu _ { i } = \int _ { 0 } ^ { \pi } l _ { i } ( \cos \theta ) \sin \theta d \theta } \\ { \displaystyle \quad = \frac { 1 } { n } \sum _ { m = 0 } ^ { n - 1 } \left( 2 \int _ { 0 } ^ { \pi } \sin \theta \cos m \theta d \theta \right) \cos m \theta _ { i } , } \end{array}
$$

where we have used the trigonometric form of (1.130). Now

$$
\begin{array}{c} { \begin{array} { r l } { { 2 } } & { 2 { \Biggl \{ } { \underset { 0 } { \uparrow } } \sin \theta \cos m \theta d \theta = { \Biggr \int } _ { 0 } ^ { \pi } ( \sin ( m + 1 ) \theta - \sin ( m - 1 ) \theta ) d \theta } \\ & { \quad = { \Biggl \{ } _ { \displaystyle - 2 \left( { \frac { 1 } { m - 1 } } - { \frac { 1 } { m + 1 } } \right) , \quad { \Biggl . } \quad m \operatorname { e v e n } ( m > 0 ) , } \\ & { \quad { \Biggl . } } \\ { 4 , \quad \quad \quad \quad \quad \quad \quad m = 0 . } \end{array} } } \end{array} 
$$

Therefore

$$
\begin{array} { l } { \displaystyle \mu _ { i } = \frac { 2 } { n } \Biggl [ 1 - ( 1 - \frac { 1 } { 3 } ) \cos 2 \theta _ { i } - ( \frac { 1 } { 3 } - \frac { 1 } { 5 } ) \cos 4 \theta _ { i } } \\ { \displaystyle \qquad - \dots - \biggl ( \frac { 1 } { m - 1 } - \frac { 1 } { m + 1 } \biggr ) \cos m \theta _ { i } - \dots - \biggl ( \frac { 1 } { k - 1 } - \frac { 1 } { k + 1 } \biggr ) \cos k \theta _ { i } \Biggr ] . } \end{array}
$$

where $k = n - 1$ for odd $\pmb { n }$ and $k = n - 2$ for even $\pmb { n } ;$ but cos $m \theta _ { i } \leqslant 1$ ,hence

$$
\begin{array} { c } { { \mu _ { i } \geqslant \displaystyle \frac { 2 } { n } \bigg [ 1 - ( 1 - \frac { 1 } { 3 } ) - ( \frac { 1 } { 3 } - \frac { 1 } { 5 } ) - \cdots - \left( \displaystyle \frac { 1 } { m - 1 } - \frac { 1 } { m + 1 } \right) - \cdots } } \\ { { - \left( \displaystyle \frac { 1 } { k - 1 } - \displaystyle \frac { 1 } { k + 1 } \right) \bigg ] \geqslant \displaystyle \frac { 2 } { n } \displaystyle \frac { 1 } { k + 1 } \geqslant \displaystyle \frac { 2 } { n ^ { 2 } } > 0 , } } \end{array}
$$

and the positivity of $\pmb { \mu _ { i } }$ ， $i = 1 , \ldots , n ,$ is established.

Suppose now that $p ( { \boldsymbol { x } } )$ is a polynomial, say $\pmb { p } \in \mathcal { P } _ { \pmb { k } }$ ; then

$$
L _ { n } ( p , T ; x ) = p ( x ) , \qquad n \geqslant k
$$

and so

$$
\int _ { - 1 } ^ { 1 } L _ { n } ( p , T ; x ) d x = \int _ { - 1 } ^ { 1 } p ( x ) d x , \qquad n \geqslant k , k = 1 , \ldots .
$$

Thus the theorem is proved for polynomial $f ( x ) ,$ without recourse to the positivity of the $\pmb { \mu _ { i } }$

If $f ( x )$ is continuous on $I _ { : }$ ，then, according to the Weierstrass approximation theorem (Theorem 1.4), given any $\pmb \varepsilon > \mathbf 0$ , we can find a polynomial $p ( { \boldsymbol { x } } )$ such that

$$
f ( x ) = p ( x ) + \delta ( x )
$$

with

$$
| \delta ( x ) | < \varepsilon , \qquad x \in I .
$$

Equation (1.135) implies that

$$
\int _ { - 1 } ^ { 1 } L _ { n - 1 } ( f , T ; x ) d x = \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( p , T ; x ) d x + \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( \delta , T ; x ) d x .
$$

Now

$$
\int _ { - 1 } ^ { 1 } L _ { n - 1 } ( \delta , T ; x ) d x = \sum _ { i = 1 } ^ { n } \mu _ { i } \delta ( \xi _ { i } ) ; .
$$

hence

$$
\left| \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( \delta , T ; x ) d x \right| \leqslant \sum _ { i = 1 } ^ { n } | \mu _ { i } | | \delta ( \xi _ { i } ) | < \varepsilon \sum _ { i = 1 } ^ { n } \mu _ { i } ,
$$

in view of (1.136) and the positivity of the $\mu _ { i }$ but

$$
\sum _ { i = 1 } ^ { n } \mu _ { i } = \sum _ { i = 1 } ^ { n } \int _ { - 1 } ^ { 1 } l _ { i } ( x ) d x = \int _ { - 1 } ^ { 1 } \left( \sum _ { i = 1 } ^ { n } l _ { i } ( x ) \right) d x = 2 ,
$$

where we make use of Exercise 1.3.1. Therefore

$$
- 2 \varepsilon < \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( \delta , T ; x ) d x < 2 \varepsilon ,
$$

whereas integration of (1.135) implies that

$$
\int _ { - 1 } ^ { 1 } p ( x ) d x = \int _ { - 1 } ^ { 1 } f ( x ) d x - \int _ { - 1 } ^ { 1 } \delta ( x ) d x ,
$$

where

$$
- 2 \varepsilon < \int _ { - 1 } ^ { 1 } \delta ( x ) d x < 2 \varepsilon .
$$

If we now restrict $\pmb { n }$ to be greater than $N$ , the degree of $p ( { \boldsymbol { x } } ) ,$ (1.137) yields

$$
\begin{array} { r l } {  { \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( f , T ; x ) d x = \int _ { - 1 } ^ { 1 } p ( x ) d x + \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( \delta , T ; x ) d x } } \\ & { = \int _ { - 1 } ^ { 1 } f ( x ) d x - \int _ { - 1 } ^ { 1 } \delta ( x ) d x + \int _ { - 1 } ^ { 1 } L _ { n - 1 } ( \delta , T ; x ) d x . } \end{array}
$$