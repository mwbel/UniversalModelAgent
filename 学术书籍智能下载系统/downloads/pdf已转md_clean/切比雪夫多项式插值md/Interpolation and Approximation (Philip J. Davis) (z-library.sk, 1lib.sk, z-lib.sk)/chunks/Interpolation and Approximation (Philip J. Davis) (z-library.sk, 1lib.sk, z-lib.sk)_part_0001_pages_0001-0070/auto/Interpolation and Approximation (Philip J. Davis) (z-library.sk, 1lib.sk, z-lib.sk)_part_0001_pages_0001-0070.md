![](images/60228d5f7a3b0c2cff0122b8fb773acc260fd079602b54968341ad75ec1deb13.jpg)

# Philip J. Davis INTERPOLATION & APPROXIMATION

# INTERPOLATION AND

# APPROXIMATION

PHILIP J. DAVIS

Brown University

# DOVER PUBLICATIONS,INC. NEW YORK

Copyright $\circledcirc$ 1963 by Philip J.Davis. Copyright $\circledcirc$ 1975 by Philip j.Davis. Ali rights reserved under Pan American and International Copyright Conventions.

Published in Canada by General Publishing Company，Ltd., 30 Lesmill Road,Don Mills,Toronto, Ontario.

Published in the United Kingdom by Constable and Company, Ltd., 10 Orange Street,London WC 2.

This Dover edition,first published in l975,is an unabridged republication，with niinor corrections, of the work originally issued by the Blaisdell Publishing Company,a Division of Ginn and Company, Waltham，Massachusetts，in l963.A new Preface (with bibliography) has been prepared by the author especially for the Dover edition.

International Standard Book Number:O-486-62495-1   
Library of Congress Catalog Card Number:75-2568

Manufactured in the United States of America Dover Publications,Inc. 180 Varick Street New York,N.Y.10014

To the Memory of my Father and Mother   
FRANK DAVIS and ANNIE DAVIS   
In the play between content and form,   
they sought a middle road.

# This page intentionally left blank

# Preface to the Dover Edition

This edition,apart from minor corrections,is identical with the fourth printing of the book originally published by Blaisdell Publishing Company (later:Xerox College).

In the fifteen years since the preparation of the original manuscript the field of interpolation and approximation has flourished greatly. Perhaps several dozens of subtopics hardly mentioned in this book have been developed to the point where each is now a separate discipline in its own right.

Granted a copious reservoir of animal energy,it might indeed have been possible to update the present work so as to take notice of some of the significant recent achievements.But I think that the present work, limited as it is, has a scope and a point of view which remain of importance.

For the reader who wishes to pursue some of the recent developments, I append here a list of books which cover a wide variety of topics.

Ahlberg,J.H.，Nilson,E.N.,and Walsh,J.L.,The Theory of Splines and Their Applications,Academic Press,N.Y.,1967.   
Bézier，P.,Numerical Control:Math.and Applications,Wiley & Sons, N. Y., 1972.   
Butzer,P.L.,and Nessel, R.J.,Fourier Analysis and Approximation, Birkhaiiser Verlag,Basel,1971.   
Cheney，E.W.,Introduction to Approximation Theory，McGraw-Hill, N.Y., 1966.   
Davis, P.J.,and Rabinowitz,P., Numerical Integration,Academic Press, N.Y., 1975.   
Forest，A.R.，“On Coons’and Other Methods for the Representation of Curved Surfaces,’ Computer Graphics and Image Processing,Vol. I,1972, pp. 341-359.   
Freud,G.,Orthogonal Polynomials,Pergamon Press,Oxford,1971.   
Goldstein,A.A., Constructive Real Analysis,Harper & Row,N.Y.,1967.   
Karlin,S.,and Studden,W.,Tschebyscheff Systems with Applications in Analysis and Statistics,Interscience,1966.   
Laurent,P.J.,Approximation et Optimisation, Hermann, Paris,1972.   
Lorentz，G.G.， Approximation of Functions. Holt, Rinehart and Winston,N.Y.,1966.   
Luke,Y.L., The Special Functions and Their Approximation,Academic Press,N.Y.,1969.   
Meinardus,G.，Approximation of Functions: Theory and Numerical Methods,Springer,N.Y.,1967.   
Nachbin, L., Elements of Approximation Theory,Van Nostrand, N.Y., 1967.   
Olver,F. W.J.，Asymptotics and Special Functions,Academic Press, N.Y., 1974.   
Rice,J.R., The Approximation of Functions,Addison-Wesley,Reading, Mass.,Vol.I: 1964,Vol.II: 1969.   
Rivlin,T.J.,An Introduction to the Approximation of Functions,Blaisdell,Waltham,Mass.,1969.   
Sard,A., Linear Approximation,Am. Math. Soc., Providence,R.I., Math. Surveys,No.9,1963.   
Schoenberg,I.J.,Cardinal Spline Interpolation, Society for Industrial and Applied Mathematics,Philadelphia,1973.   
Shapiro,H. S.，Smoothing and Approximation，Van Nostrand,N.Y., 1969. ,Topics in Approximation Theory,Springer,N.Y.,1971.   
Singer,I.,Best Approximation in Normed Linear Spaces by Elements of Linear Subspaces,Grund.Math.Wissen, Springer,N.Y.,1970.   
Talbot,A.(ed.)，Approximation Theory，Academic Press,N.Y.,1970.   
Todd,J.，Introduction to the Constructive Theory of Functions,Birkhaiser Verlag,Basel,1963.   
Wermer,John, Banach Algebras and Several Complex Variables, Markham,Chicago,1971.   
Werner, H.， Vorlesung über Approximationstheorie, Lecture Notes in Mathematics,Vol.14, Springer,N.Y.1966.

# Foreword

During the past few decades,the subject of interpolation and approximation has not been overly popular in American universities.Neglected in favor of more abstract theories,it has been taught only where some staff member has actively engaged in research in the field.This has resulted in a scarcity of English language books at the intermediate level. Since the development of high speed computing machinery,the flame of interest in interpolation and approximation has burned brighter,and the realization that portions of the theory are best presented through functional analysis has added additional fuel to the flame.It has been my intention,therefore,to prepare a book which would be at the level of students who have had some real variable, some complex variable,some linear algebra,and, perhaps,a bit of integration theory.The book would merge,insofar as possble,the real and the complex, the concrete and the abstract,and would provide a place for general results of these previous courses to find application and to pass in review.

A one semester course can be based on Chapters 2,3,4,6,7,and 8.The problems,on the whole,are simple,and are intended to secure the material presented rather than to extend the coverage of the book.The illustrative examples are an integral part of the text,but a number of them lack complete details and can be used as additional problems.

The fields of interpolation and approximation have been cultivated for centuries.The amount of information available is truly staggering.Take, for instance,the subject of orthogonal polynomials.Abibliography prepared in the late l93O's contains several hundred pages of references,and the topic continues to grow.I have had to anthologize.I have sought breadth rather than depth,and have tried to display a variety of analytical techniques.To some extent,I have been guided by what I consider “useful.”Accordingly, I have developed neither the calculus of finite differences,nor $L ^ { p }$ spaces $( p \neq 2 , \infty )$ , nor approximation on infinite sets,for in my work with computation,I have rarely dealt with these things.On the other hand,I am aware that utility cannot be made into a principle of selection for a mathematics book.It comes down to this: I have included the topics that have caught my imagination.I hope that the selection will introduce the student to some of the best and encourage the scholar to seek the rest.

A word is in order on the portions of the book that are devoted to functional analysis. This subject is generally presented with spectral theory as its culmination.Here，the elementary geometric portions are developed for ultimate application to approximation theory.This is by no means new.In 1930,Dunham Jackson ended his book on the theory of approximation with a chapter on the geometry of function space,and over the years,more and more emphasis has been given to functional analysis.At its best, functional analysis unifes many seemingly diverse situations in a wonderful way and is a genuine principle of research. At its worst, it is a scintillating wrapper that provides attractive packages,and camouflages with glamorous language the fact that their content may be small or may have been originally obtained in the drab workshops of hard analysis.Perhaps functional analysis is analogous to Cartesian geometry which put an end to the synthetic drudgery of Apollonius though the major theorems on conics are Greek. Though the welding of functional analysis to conventional analysis has produced an imperfect seam that is visible in practically every chapter of this book,I believe that functional analysis is a good way to present many of the topics, and that it can and should be introduced at an early stage of a student's career.

This book derives froni several teaching experiences. In the Spring of 1957 and again in the Spring of l959,I presented a series of lectures on approximation theory to the members of training programs in Numerical Analysis that were held at the National Bureau of Standards in Washington, D.C.under the sponsorship of the National Science Foundation.In 1959,I gave a course in interpolation and approximation at the Harvard Summer School,and have given shorter courses in special computer programs at Wayne University and the University of Pennsylvania.Out of these varied experiences and out of a day to day exposure to live computation in the Applied Mathematics Division of the National Bureau of Standards,the plan of the present book emerged. The liberal policy of the National Bureau of Standards,encouraging study,research,and writing has enabled me to carry this plan to fruition.The following chapters were prepared at the Bureau:5,and 9-14.

My debt to various works is clear,but I must single out Gontcharoff, Natanson,Szego,and Walsh for special mention.My debt to my teachers should be made more explicit.My concern with these matters extends back to dissertation days when Ralph P. Boas interested me in interpolatory function theory.The lectures of Stefan Bergman opened my eyes to the beauty of orthogonal functions and the kernel function.The lectures and subsequent work with J.L.Walsh deepened my interest in problems in the complex plane.I had the pleasure of knowing and working with Michael Fekete in the last years of his life.A wonderful man of that wonderful school of Hungarian mathematicians, his single-minded insistence on simplicity and elegance made an immediate impression on me.

To discharge my debt to my colleagues,I must thank Dr. Oved Shisha for his kind attentions to this book. I have profited greatly from many discussions with him and from his detailed criticism of the manuscript.

From students (may their number increase)I have learned that though mathematics proceeds from false starts and bungling,it is presented backwards,as a fait accompli.This may provide clean copy and heighten the dramatic effect,but it taxes the understanding.There are many places in this book where the masters of analysis work their magic.How did they happen to get such and such an idea? This question has been asked me over and over by students just beyond the advanced calculus stage.It can rarely be answered,but one should say: tackle the problem yourself and you may learn.The road to understanding is rough;to smooth it too much denies the reality of creative genius.

Thanks go to Ellen Rigby who helped me with the figures and to Richard Strafella for various tasks with the manuscript.These were done as part of their Antioch College plan of quarters devoted to work.

PHILIP J.DAVIS Washington,D.C. Fall,1961

# This page intentionally left blank

# Contents

# CHAPTER I·INTRODUCTION

1.1 Determinants 1   
1.2 Solution of Linear Systems of Equations 2   
1.3 Linear Vector Spaces 3   
1.4 The Hierarchy ofFunctions 4   
1.5 Functions Satisfying a Lipschitz Condition 8   
1.6 Differentiable Functions 8   
1.7 Infinitely Differentiable Functions 11   
1.8 Functions Analytic on the Line 12   
1.9 Functions Analytic ina Region 12   
1.10 Entire Functions 15   
1.11 Polynomials 15   
1.12 Linear Functionals and the Algebraic Conjugate Space 16   
1.13 Some Assorted Facts 19

# CHAPTER II·INTERPOLATION

2.1 Polynomial Interpolation 24   
2.2 The General Problem of Finite Interpolation 26   
2.3 Systems Possessing the Interpolation Property 27   
2.4 Unisolvence 31   
2.5 Representation Theorems:The Lagrange Formula 33   
2.6 Representation Theorems:The Newton Formula 39   
2.7 Successive Differences 50

# CHAPTER III ·REMAINDER THEORY

3.1 The Cauchy Remainder for Polynomial Interpolation 56   
3.2 Convex Functions 58   
3.3 Best Real Error Estimates；The Tschebyscheff Polynomials 60   
3.4 Divided Differences and Mean Values 64   
3.5 Interpolation at Coincident Points 66   
3.6 Analytic Functions:Remainder for Polynomial Interpolation 67   
3.7 Peano's Theorem and Its Consequences 69   
3.8 Interpolation in Linear Spaces；General Remainder Theorem 75

# CHAPTER IV·CONVERGENCE THEOREMS FOR INTERPOLATORY PROCESSES

4.1 Approximation by Means of Interpolation 78   
4.2 Triangular Interpolation Schemes 79   
4.3 A Convergence Theorem for Bounded Triangular Schemes 81   
4.4Lemniscates and Interpolation 83

CHAPTER V· SOME PROBLEMS OF INFINITE INTERPOLATION

5.1 Characteristics of Such Problems 95   
5.2 Guichard's Theorem 96   
5.3 A Second Approach:Infinite Systems of Linear Equations in   
Infinitely Many Unknowns 97   
5.4Applications of Polya's Theorem 102

# CHAPTER VI · UNIFORM APPROXIMATION

6.1 The Weierstrass Approximation Theorem 107   
6.2 The Bernstein Polynomials 108   
6.3 Simultaneous Approximation of Functions and Derivatives 112   
6.4 Approximation by Interpolation:Fejer's Proof 118   
6.5 Simultaneous Interpolation and Approximation 121   
6.6 Generalizations of the Weierstrass Theorem 122

# CHAPTER VII · BEST APPROXIMATION

7.1 What is Best Approximation? 128   
7.2 Normed Linear Spaces 129   
7.3 Convex Sets 134   
7.4 The Fundamental Problem of Linear Approximation 136   
7.5 Uniqueness of Best Approximation 140   
7.6 Best Uniform (Tschebyscheff）Approximation of Continuous   
Functions 146   
7.7Best Approximation by Nonlinear Families 152

# CHAPTER VIII · LEAST SQUARE APPROXIMATION

8.1Inner Product Spaces 158

8.2Angle Geometry for Inner Product Spaces 161

8.3Orthonormal Systems 163

8.4Fourier (or Orthogonal) Expansions 169

8.5Minimum Properties of Fourier Expansions 171

8.6 The Normal Equations 175

8.7Gram Matrices and Determinants 176

8Further Properties of the Gram Determinant 184

8.9Closure and Its Consequences 188   
8.10 Further Geometrical Properties of Complete Inner Product Spaces195

# CHAPTER IX ·HILBERT SPACE

9.1 Introduction 201   
9.2 Three Hilbert Spaces 203   
9.3 Bounded Linear Functionals in Normed Linear Spaces and in Hilbert Spaces 214   
9.4 Linear Varieties and Hyperplanes； Interpolation and Approximation in Hilbert Space 225

CHAPTER X · ORTHOGONAL POLYNOMIALS

10.1General Properties of Real Orthogonal Polynomials 234   
10.2 Complex Orthogonal Polynomials 239   
10.3The Special Function Theory of the Jacobi Polynomials 246

CHAPTER XI · THE THEORY OF CLOSURE AND COMPLETENESS

l1.1 The Fundamental Theorem of Closure and Completeness 257   
11.2 Completeness of the Powers and Trigonometric Systems for   
$L ^ { 2 } [ a , b ]$ 265   
11.3 The Müntz Closure Theorem 267   
11.4 Closure Theorems for Classes of Analytic Functions 273   
11.5Closure Theorems for Normed Linear Spaces 281

# CHAPTER XII · EXPANSION THEOREMS FOR ORTHOGONAL FUNCTIONS

12.1 The Historical Fourier Series 290   
12.2 Fejér's Theoryof Fourier Series 299   
12.3 Fourier Series of Periodic Analytic Functions 305   
12.4 Convergence of the Legendre Series for Analytic Functions 308   
12.5 Complex Orthogonal Expansions 314   
12.6 Reproducing Kernel Functions 316

CHAPTER XIII · DEGREE OF APPROXIMATION

13.1 The Measure of Best Approximation 328

13.2 Degree of Approximation with Some Square Norms 333

13.3Degree of Approximation with Uniform Norm 334

CHAPTER XIV · APPROXIMATION OF LINEAR FUNCTIONALS

14.1 Rules and Their Determination 341   
14.2 The Gauss-Jacobi Theory of Approximate Integration 342   
14.3Norms of Functionals as Error Estimates 345   
14.4Weak\* Convergence 346

363

Short Guide to Orthogonal Polynomials Table of the Tschebyscheff Polynomials Table of the Legendre Polynomials

BIBLIOGRAPHY 373

# INTERPOLATION

AND

# APPROXIMATION

# This page intentionally left blank

# CHAPTER I

# Introduction

This chapter contains material from algebra and analysis that will be of use in the later portions of the book.It is presented here for ready reference and for review.The reader is assumed to be familiar with some of the theorems.Other theorems may be less familiar and their proofs have been given.Though $L ^ { p }$ spaces are mentioned in Theorem l.4.0,they do not reappear until Chapter VII,and only the elementary portions of measure and integration theory are used.

1.1 Determinants. Let $\boldsymbol { v } _ { i }$ designate the $\pmb { n }$ -tuple of numbers $( a _ { i 1 } , a _ { i 2 } ,$ $\cdots , a _ { i n } )$ . For a constant $\pmb { \alpha }$ , we shall mean by $\alpha v _ { i }$ the $\pmb { n }$ -tuple $( \alpha a _ { i 1 } , \alpha a _ { i 2 } , \ldots ,$ ${ \alpha } a _ { i n } )$ ，while by $\pmb { v } _ { i } + \pmb { v } _ { j }$ ，we shall mean the $\pmb { n }$ -tuple $( a _ { i 1 } + a _ { j 1 }$ ， ${ a _ { i } } _ { 2 } + { a _ { j } } _ { 2 } ,$ ：, ${ a } _ { i n } + { a } _ { j n } )$ .The letters $e _ { 1 } , \ldots , e _ { n }$ will designate the unit $\pmb { n }$ -tuples (1,0,0, $\ldots , 0 )$ ， $( 0 , 1 , 0 , \ldots , 0 ) , \ldots , ( 0 , 0 , 0 , \ldots , 1 ) .$ ，The function of the $\pmb { n } ^ { 2 }$ variables $\pmb { a } _ { i j }$ $( i , j = 1 , 2 , \ldots , n )$ , known as the determinant of those quantities, is generally written

$$
D = { \left| \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} \right| } = | a _ { i j } | = D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { n } ) .
$$

The determinant is completely characterized by the following three properties

$$
\begin{array} { l } { { D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { i } , \ldots , v _ { n } ) = D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { i } + v _ { j } , \ldots , v _ { n } ) } } \\ { { ( i \neq j ) \ ( \mathrm { I n v a r i a n c e } ) . } } \\ { { D ( v _ { 1 } , v _ { 2 } , \ldots , \alpha v _ { i } , \ldots , v _ { n } ) = \alpha D ( v _ { 1 } , v _ { 2 } , \ldots , v _ { i } , \ldots , v _ { n } ) } } \end{array}
$$

$$
D ( e _ { 1 } , e _ { 2 } , \ldots , e _ { n } ) = 1 { \mathrm { ( N o r m a l i z a t i o n ) } } .
$$

The whole of determinant theory can be built up from this starting point and is related to the theory of the volume of an $\pmb { n }$ -dimensional parallelotope.

Given an $\pmb { n }$ by $\pmb { n }$ matrix $A = ( a _ { i j } )$ ，the determinant associated with this matrix is designated by $| A |$ or det $\pmb { A }$ .If from the array $\pmb { A }$ we delete the ith row and the jth column,a certain $( n - 1 )$ by $( n - 1 )$ submatrix $A _ { i j }$ will remain.The determinant associated with this submatrix is known as the minor of the element $\pmb { a } _ { i j }$ .The quantity $( - 1 ) ^ { i + j } \left| A _ { i j } \right|$ is the cofactor of $\boldsymbol { a } _ { i j } .$ For the cofactor we write $A _ { i j } { } ^ { * }$ .The following rules of computation for determinants are fundamental.

(a) $| { \cal A } | = | { \cal A } ^ { \prime } |$ ， $A ^ { \prime } =$ transpose of $A = ( a _ { j i } )$   
(b) If two rows (or columns) of $\pmb { A }$ are interchanged, producing a matrix $\scriptstyle A _ { 1 }$ ，then $| A | = - | A _ { 1 } |$   
（c） If two rows (or columns) of $\pmb { A }$ are identical,then $| { \cal A } | = 0$   
(d) If a row (or column), $\pmb { v }$ of $\pmb { A }$ is replaced by kv producing a matrix $\scriptstyle A _ { 1 }$ ,then $| A _ { 1 } | = k \left| A \right|$   
(e) If a scalar multiple $k v _ { i }$ of the ith row (or column) is added to the jth row (or column) $\boldsymbol { v } _ { j }$ ， $( i \neq j )$ and （ the matrix $A _ { 1 }$ results, then $| { \cal A } | = | { \cal A } _ { 1 } |$

(f) A determinant may be evaluated in terms of cofactors :

$$
\begin{array} { r l } { { | { \cal A } | = \displaystyle \sum _ { i = 1 } ^ { n } a _ { i j } A _ { i j } { } ^ { * } } } & { { \quad 1 \le j \le n } } \\ { { } } & { { } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } a _ { i j } A _ { i j } { } ^ { * } } } & { { \quad 1 \le i \le n . } } \end{array}
$$

The expansion (f) is of considerable utility for it reduces an $\textit { \textbf { n } } \times \textit { \textbf { n } }$ determinant to a sum of $\pmb { n }$ determinants of order $\pmb { n } - \pmb { 1 }$ . Coupled with the elementary equation $| a _ { \mathbf { 1 1 } } | = a _ { \mathbf { 1 1 } }$ ,it contains within it a recursive definition of a determinant.The complete expansion of a determinant in terms of the matrix elements is less useful theoretically and hardly at all numerically.

1.2 Solution of Linear Systems of Equations. Consider the system of $\pmb { n }$ linear equations in $\pmb { n }$ unknowns $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$

$$
\sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = b _ { i } \qquad ( i = 1 , 2 , . . . , n ) .
$$

THEOREM 1.2.1 (Cramer's Rule).If $| A | = | a _ { i j } | \neq 0$ ,then (1.2.1) possesses a unique solution given by

$$
x _ { r } = { \frac { \displaystyle \sum _ { i = 1 } ^ { n } A _ { i r } { } ^ { * } b _ { i } } { | A | } } \qquad r = 1 , 2 , \ldots , n .
$$

THEOREM 1.2.2 (The Alternative Theorem). The homogeneous system

$$
\sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = 0 \qquad ( i = 1 , 2 , . . . , n )
$$

possesses a non-trivial solution (i.e., $\pmb { a }$ solution other than $x _ { 1 } = x _ { 2 } = \cdots =$ $\begin{array} { r } { x _ { n } = 0 \quad } { } \end{array}$ if and only if $| { \cal A } | = 0$ If for $\pmb { a }$ fixed $A = ( a _ { i j } )$ there are solutions to the non-homogeneous system (1.2.i) for every selection of the quantities $\boldsymbol { b } _ { i }$ then $| A | \neq 0$ and the homogeneous system has only the trivial solution.

1.3 Linear Vector Spaces. It will be useful to formulate many questions of interpolation and approximation theory within an abstract framework.The notion of a linear vector space over a field $\pmb { F }$ is therefore a basic one.

DEFINITioN l.3.l. A linear vector space (or a linear space) $\pmb { X }$ is a set of elements (or vectors) $\boldsymbol { \mathscr { x } } , \boldsymbol { \mathscr { y } } , \ldots$ ,for which two types of operation are possible. Any two elementsx, $y \in X$ determine a unique element $\pmb { x } + \pmb { y } \in \pmb { X }$ as their sum.Each element $\pmb { x } \in \pmb { X }$ and each scalar $\pmb { \alpha }$ ofa given field $\pmb { F }$ determine a unique element $\pmb { \alpha } \pmb { x } \in \pmb { X }$ as a scalar product.Vector sums and scalar products are required to obey the following laws.

(a) ${ \pmb x } + { \pmb y } = { \pmb y } + { \pmb x } .$   
(b) ${ \pmb x } + ( { \pmb y } + { \pmb z } ) = ( { \pmb x } + { \pmb y } ) + { \pmb z } .$   
(c） There exists a unique element $\mathbf { 0 } \in X$ such that $\pmb { x } + \pmb { 0 } = \pmb { x }$ for all $\pmb { x } \in \pmb { X }$   
(d) To each ${ \pmb x } \in { \pmb X }$ there exists a unique inverse - $_ { \pmb { x } }$ such that ${ \pmb x } + ( - { \pmb x } ) = 0$   
(e) $\alpha ( \beta x ) = ( \alpha \beta ) x$ for all $\alpha , \beta \in F , x \in X$   
(f) $\alpha ( { \pmb x } + { \pmb y } ) = \alpha { \pmb x } + \alpha { \pmb y } .$   
（g） $( \alpha + \beta ) x = \alpha x + \beta x$   
(h) $\mathbf { l } ( { \pmb x } ) = { \pmb x }$

Couditions (a)-(d) are frequently summed up by saying that the elements of $\pmb { X }$ form an Abelian group under addition.The element O is called the zero vector.

In this book,the underlying field $\pmb { F }$ of scalars will be either (l) the feld of real numbers,or (2) the feld of complex numbers.We can,therefore, speak either of a real or a.complex linear vector space.

DEFINITIoN 1.3.2. An expression of the form

$$
\alpha _ { 1 } x _ { 1 } + \alpha _ { 2 } x _ { 2 } + \cdots + \alpha _ { n } x _ { n } ; \alpha _ { i } \in I , x _ { i } \in X
$$

is called a linear combination of the $_ { \ast }$ s.

DEFINITioN 1.3.3. A finite set of vectors $x _ { 1 } , \ldots , x _ { n }$ is linearlydependent if we can find constants (i.e., scalars) $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n } ;$ ，not all zero such that $\alpha _ { 1 } x _ { 1 } + \alpha _ { 2 } x _ { 2 } + \cdot \cdot \cdot + \alpha _ { n } x _ { n } = 0$ .If such is not the case,the vectors are calledindependent.

DEFINITION 1.3.4． Let $\pmb { n }$ be a positive integer. Suppose that we can find $\pmb { n }$ vectors $x _ { 1 } , x _ { 2 } , \ldots .$ ， $x _ { n } \in X$ which are independent while every $n + 1$ vectors are dependent.Then $\pmb { X }$ is said to be a linear space of dimension $\pmb { n }$ If no such $_ { n }$ exists,then $\pmb { X }$ is called an infinite dimensional space.

DEFINITIoN l.3.5. A set of elements $x _ { 1 } , x _ { 2 } , \ldots$ , is said to be a basis for $\pmb { X }$ if the $x _ { i }$ are independent and if every $x \in X$ can be expressed (uniquely) as a linear combination of the $x _ { i }$

THEOREM 1.3.1． $\pmb { X }$ has finite dimensionnif and only if it has a basis of $\pmb { n }$ elements.If $\pmb { X }$ has dimension n any $\mathscr { n }$ independent elementsconstitute $\pmb { a }$ basis.

Ex.1．The Real, $_ n$ -dimensional,Cartesianpace $\scriptstyle { R _ { n } }$ .This consists of vectors $_ x$ which are $_ n$ -tuples of real numbers: ${ \boldsymbol { x } } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . Let $y = ( y _ { 1 } , y _ { 2 } , \dotsc , y _ { n } )$ be a second vector.( $x$ and $_ y$ are considered equal if and only if $x _ { i } = y _ { i } , i =$ $1 , 2 , \ldots , n .$ ）Vector addition is defined by

$$
x + y = ( x _ { 1 } + y _ { 1 } , x _ { 2 } + y _ { 2 } , . . . , x _ { n } + y _ { n } ) .
$$

Scalar multiplication is defined by $\alpha x = ( \alpha x _ { 1 } , \alpha x _ { 2 } , \ldots , \alpha x _ { n } )$ .We set $0 \ \simeq$ $( \mathbf { 0 } , 0 , \ldots , \mathbf { 0 } )$ and $- x = ( - x _ { 1 } , - x _ { 2 } , . ~ . ~ . ~ , - x _ { n } )$ .The $_ n$ vectors, $\boldsymbol { e } _ { 1 } = ( 1 , 0 , \dots , 0 )$ ， $e _ { 2 } = ( 0 , 1 , . ~ . ~ . ~ , 0 ) , . ~ . ~ . ~ , e _ { n } = ( 0 , 0 , . ~ . ~ . ~ , 1 )$ ,known as unit vectors,are independent.

Ex.2. The Complex, $_ n$ -dimensional,Cartesian pace $C _ { n }$ .This consists of $_ { n }$ tuples of complex numbers: $( z _ { 1 } , z _ { 2 } , \ldots , z _ { n } )$ .The laws of combination are as in Ex. 1.

Ex.3.Linear Spaces of Functions.In this example,a function,considered asa whole,is thought of as constituting an element ofa space.Let $\pmb { S }$ designate a point set lying on the real axis.Consider the totality of real-valued functions with domain $\boldsymbol { s }$ .Call this totality $_ { T }$ $\Gamma . { \bf F o r } f , g \in T$ ,define their sum $f + g$ by means of

$$
( f + g ) ( x ) = f ( x ) + g ( x ) , x \in S .
$$

Define a scalar product by means of

$$
( \alpha f ) ( x ) \ = \alpha f ( x ) , x \in S .
$$

Let the zero vector be the function of $\pmb { T }$ that vanishes identically.Let $- f$ designate the function defined by

$$
( - f ) ( x ) \ = \ - f ( x ) , x \in S .
$$

With these definitions, $\pmb { T }$ is a linear vector space.If $\boldsymbol { s }$ contains more than a finite number of points, $\pmb { T }$ is of infinite dimension.

1.4 The Hierarchy of Functions. Our dealings will be almost exclusively with functions of a single real or complex variable.We shall work with finite intervals in the real case and bounded sets in the complex case. The deeper analytical properties of interpolation and approximation depend to a great extent on what may be called “the degree of smoothness”of the function approximated.In order of increasing smoothness,we shall deal with: $L ^ { p }$ functions,bounded functions,continuous functions,functions satisfying a Lipschitz condition,differentiable functions, $\pmb { n }$ -times differentiable functions,infinitely differentiable functions,analytic functions,entire functions,polynomials of restricted degree,constants.It will become apparent in subsequent chapters that the processes of interpolation and approximation become stronger when applied to functions further down this list.We shall now define these classes of functions and recall some basic facts about them.

DEFINITION 1.4.0. Let $\pmb { p } > 0$ .The class of functions $f ( x )$ which are measurable and for which $| f ( x ) | ^ { p }$ is integrable over $[ a , b ]$ is known as $L ^ { p } [ \pmb { a } , \pmb { b } ]$ If $\pmb { p } = 1$ , the class is designated by $L [ \boldsymbol { a } , \boldsymbol { b } ]$

THEOREM 1.4.0. (a) $L ^ { p } [ { \pmb { a } } , { \pmb { b } } ]$ is $^ { \pmb { a } }$ linear space. (b) If $f \in L [ a , b ]$ ，then $f \geq 0$ and $\int _ { a } ^ { b } f ( x ) d x = 0$ imply $f = 0$ almost everywhere. (c) If $f \in L [ a , b ]$ ， then $g ( x ) = \int _ { a } ^ { x } f ( x ) d x$ is continuous. (d) $1 f - \infty < a < b < \infty$ ，then $f \in L ^ { p } [ a , b ] , p ^ { \prime } < p$ ,implies $f \in L ^ { p \prime } [ a , b ]$ (e) $I f f \in L ^ { p } [ a , b ]$ with $\pmb { \mathscr { p } } \geq 1$ , we can find an absolutely continuous function $g ( x )$ such that $\int _ { a } ^ { b } | f ( x ) - g ( x ) | ^ { p } d x \leq \varepsilon$ for arbitrary $\varepsilon > 0$

For these results,the reader is referred to standard texts on integration theory.

Let $s$ denote a point set in $\scriptstyle { R _ { n } }$ or in the complex plane and $P$ a point in that set. Though Definitions 1.4.l-l.9.l are meaningful for complex valued functions of a real variable,we shall generally deal with real valued functions whenever $\boldsymbol { s }$ is in $\scriptstyle { R _ { n } }$

DEFINITION l.4.1． A function $f$ is bounded on $\boldsymbol { s }$ if there exists a constant $M$ such that

$$
| f ( P ) | \leq M { \mathrm { ~ f o r ~ a l l ~ } } P \in S .
$$

If no such constant exists,the function is said to be unbounded on $s$ .The class of functions which are bounded on $\boldsymbol { s }$ will be designated by $B ( S ) . ~ B ( S )$ is a lincar space.

Ex.1．The function $y = \sin x ^ { 2 }$ is bounded on $- \infty < x < \infty$

Ex.2．The Gamma function $y = \Gamma ( x )$ is unbounded on the interval $0 < x \le 1$ ， and on the interval $1 \leq x < \infty$ ·

Ex.3.If $[ a , b ]$ is a finite interval, $f \in B [ a , b ]$ and measurable there implies $f \in L ^ { p } [ a , b ]$ for all $\pmb { \mathscr { p } } > \pmb { 0 }$

DEFINITION 1.4.2． Let the function $f$ be defined on the set $\pmb { S }$ It is continuous at a point $P _ { 0 }$ of $\pmb { S }$ if

$$
\operatorname* { l i m } _ { n \to \infty } f ( P _ { n } ) = f ( P _ { 0 } )
$$

whenever $P _ { n } \to P _ { 0 }$ ， $P _ { n } \in { \mathcal { S } }$ If $f$ is defined on an interval $[ \pmb { a } , \pmb { b } ]$ and is continuous at ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ ,then given an $\varepsilon > 0$ ,we can find a $\pmb { \delta }$ such that

$$
| f ( x ) - f ( x _ { 0 } ) | \leq \varepsilon
$$

for all $| x - x _ { 0 } | \leq \delta$ in $[ a , b ]$ .The $\pmb { \delta }$ will depend upon $f , \pmb { x _ { 0 } } ,$ and $\varepsilon$ The class of functions continuous on $I \colon [ a , b ]$ will be designated by $C [ \pmb { a } , \pmb { b } ]$ .It is a linear space.

It may occur that for a given $f$ and ε we can find a $\pmb { \delta }$ for which (1.4.3) holds independently of $\pmb { x _ { 0 } }$ 、This leads to the notion of uniform continuity.

DEFINITION 1.4.3． A function $f$ is uniformly continuous over a set $\pmb { S }$ if given an $\varepsilon > 0$ ,we can find a $\pmb { \delta }$ such that

$$
| f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq \varepsilon
$$

for all $| x _ { 1 } - x _ { 2 } | \leq \delta ; x _ { 1 } , x _ { 2 } \in S$

I one important case,the lotions of continuity and uniform continuity coincide:

THEOREM l.4.1. A function which is continuous on a compact (i.e.,closed and bounded) point set is uniformly continuous there.

Ex.1．The function $A ( x ) = \left| x \right|$ is continuous on $- \infty < x < \infty$

Ex.2．The function $f ( x ) = ( 1 + e ^ { 1 / x } ) ^ { - 1 }$ is discontinuous at $\pmb { x } = \pmb { 0 }$ however ${ f ( 0 ) }$ may be defined,for $\operatorname* { l i m } _ { x \to 0 ^ { + } } f ( x ) = 0$ while $\operatorname* { l i m } _ { x \to 0 ^ { - } } f ( x ) \ = \ 1$ .It is continuous elsewhere.

Ex.3．The function $f ( x ) = { \frac { 1 } { x } }$ is continuous on the open interval $( \mathbf { 0 } , \textstyle { \frac { 1 } { 2 } } )$ but is not uniformly continuous there.

Ex.4. The function $f ( x ) = { \frac { 1 } { 1 + x ^ { 2 } } }$ is uniformly continuous over the whole   
line $- \infty < x < \infty$ ,for we have

$$
\left| \frac { 1 } { 1 + { x _ { 1 } } ^ { 2 } } - \frac { 1 } { 1 + { x _ { 2 } } ^ { 2 } } \right| = \frac { | { x _ { 2 } } ^ { 2 } - { x _ { 1 } } ^ { 2 } | } { ( 1 + { x _ { 1 } } ^ { 2 } ) ( 1 + { x _ { 2 } } ^ { 2 } ) } \le | { x _ { 2 } } - { x _ { 1 } } | \frac { ( | { x _ { 1 } } | + | { x _ { 2 } } | ) } { ( 1 + { x _ { 1 } } ^ { 2 } ) ( 1 + { x _ { 2 } } ^ { 2 } ) } .
$$

Inasmuch as

$$
{ \frac { | x _ { 1 } | } { 1 + { x _ { 1 } } ^ { 2 } } } \leq { \frac { 1 } { 2 } } , { \frac { | x _ { 1 } | + | x _ { 2 } | } { ( 1 + { x _ { 1 } } ^ { 2 } ) ( 1 + { x _ { 2 } } ^ { 2 } ) } } \leq 1 .
$$

Thus,

THEOREM 1.4.2 (First Mean Value Theorem for Integrals).

$L e t f , g \in C [ a , b ]$ . Suppose moreover that ${ \pmb g } \ge { \pmb 0 }$ there. Then,

$$
\int _ { a } ^ { b } f ( x ) g ( x ) \ d x = f ( \xi ) { \int _ { a } ^ { b } g ( x ) \ d x }
$$

for some ${ \pmb \xi }$ with $a \le \xi \le b$ The theorem is also true if ${ \pmb g } \in { \pmb L } [ { \pmb a } , { \pmb b } ]$ ， $g \geq 0$ a.e. It is occasionally useful to have inforination about the best $\pmb { \varepsilon }$ which goes with a given $\pmb { \delta }$ in the definition of uniform continuity.

DEFINITION 1.4.4． Let $f ( x )$ be defined on an interval $\pmb { I }$ Set

$$
w ( \delta ; f ) = w ( \delta ) = \operatorname* { s u p } | f ( x _ { 1 } ) - f ( x _ { 2 } ) |
$$

where the sup is taken over all pairs ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } } \in I$ for which $| x _ { 1 } - x _ { 2 } | \leq \delta$ The function $w ( \delta )$ (which depends on $f$ )is called the modulus of continuity of $f$ on $\pmb { I }$

$$
f ( x ) = x ^ { 2 } , I = ( 0 , 1 ) , w ( \delta ) = 2 \delta - \delta ^ { 2 } .
$$

Ex. 6. $f ( x ) = \frac { 1 } { x } , I = ( 0 , 1 ) , w ( \delta ) = + \infty .$

Ex. 7. $f ( x ) = \sin \frac { 1 } { x } , I = ( 0 , 1 ) , w ( \delta ) \equiv 2 .$

THEOREM 1.4.3．Let $f ( x ) \in C [ a , b ]$ The modulus of continuity has the following properties

$$
{ \pmb w } ( { \bf 0 } ) = { \bf 0 }
$$

$$
w ( \delta _ { 1 } + \delta _ { 2 } ) \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } ) \ ( S u b a d d i t i v i t y )
$$

$$
w ( n \delta ) \leq n w ( \delta ) .
$$

Moreover, $w ( \delta ) \in C [ 0 , b - a ]$ ·

Proof:(l.4.7) is obvious. Since $| x _ { 1 } - x _ { 2 } | \le \delta _ { 1 }$ implies $| x _ { 1 } - x _ { 2 } | \leq \delta _ { 2 } ,$ the corresponding sup cannot decrease,and (1.4.8) follows. To prove (l.4.9),observe that if $0 \le x _ { 2 } - x _ { 1 } \le \delta _ { 1 }$ ,then $| f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq w ( \delta _ { 1 } ) \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } )$ On the other hand,if $\delta _ { 1 } < x _ { 2 } - x _ { 1 } \le \delta _ { 1 } + \delta _ { 2 } ,$ then $\pmb { x _ { 1 } } + \pmb { \delta _ { 1 } } < \pmb { x _ { 2 } }$ and $x _ { 2 } - ( x _ { 1 } + \delta _ { 1 } ) < \delta _ { 2 }$ But,

$$
\begin{array} { r } { | f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq | f ( x _ { 1 } ) - f ( x _ { 1 } + \delta _ { 1 } ) | + | f ( x _ { 1 } + \delta _ { 1 } ) - f ( x _ { 2 } ) | } \\ { \leq w ( \delta _ { 1 } ) + w ( x _ { 2 } - ( x _ { 1 } + \delta _ { 1 } ) ) \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } ) . } \end{array}
$$

Therefore, $w ( \delta _ { 1 } + \delta _ { 2 } ) = \operatorname* { s u p } _ { \substack { 0 \leq x _ { 2 } - x _ { 1 } \leq \delta _ { 1 } + \delta _ { 2 } } } | f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq w ( \delta _ { 1 } ) + w ( \delta _ { 2 } ) .$ (1.4.10) follows immediately from (1.4.9)by induction. From (l.4.8 and 9), $0 \le w ( \delta + \delta _ { 1 } ) - w ( \delta ) \le w ( \delta _ { 1 } )$ Now， by Theorem 1.4.1, $\operatorname* { l i m } _ { \delta _ { 1 } \to 0 } \ w ( \delta _ { 1 } ) = 0$ and hence $\pmb { w }$ is continuous at $\delta$

# 1.5 Functions Satisfying a Lipschitz Condition

DEFINITION 1.5.1． Let $f ( x )$ be defined on an interval $\boldsymbol { \mathit { I } }$ and suppose we can find two positive constants $M$ and $\pmb { \alpha }$ such that

$$
| f ( x _ { 1 } ) - f ( x _ { 2 } ) | \leq M | x _ { 1 } - x _ { 2 } | ^ { \alpha } { \mathrm { ~ f o r ~ a l l ~ } } x _ { 1 } , x _ { 2 } \in I .
$$

Then $f$ is said to satisfy a Lipschitz Condition of order $\pmb { \alpha }$ .The class of such functions will be designated by Lip $\pmb { \alpha }$ .When it is useful to put the constant $\pmb { M }$ in evidence, one writes $\operatorname { L i p } _ { M } \alpha$ ·

THEOREM 1.5.1． Lip $\pmb { \alpha }$ is a linear space. If $f \in \operatorname { L i p } \alpha$ on $\boldsymbol { \mathit { I } }$ ，then $f$ is continuous；indeed，uniformly continuous on $\pmb { I }$ If $f \in \operatorname { L i p } \alpha$ with $\alpha > 1$ then $f = c o n s t a _ { i }$ nt.If $f \in \operatorname { L i p } \alpha$ ,it may fail to be differentiable,but if it possesses $^ { \pmb { a } }$ derivative satisfying $| f ^ { \prime } ( x ) | \leq M$ then $f \in \operatorname { L i p } _ { M } 1$ .If $\alpha < \beta$ then Lip ${ \pmb { \alpha } } = \mathbf { L i p } \beta$ The conditions $f \in \operatorname { L i p } _ { M } \alpha$ and $w ( \delta ) \leq M \delta ^ { \alpha }$ are equivalent.

Ex.1.Let $0 ~ < \alpha < 1$ Let $x > 0 , h > 0$ .Then ${ \frac { d } { d x } } \left[ ( x + h ) ^ { \alpha } - x ^ { \alpha } \right] =$ $\alpha [ ( x + h ) ^ { \alpha - 1 } - x ^ { \alpha - 1 } ] < 0$ Therefore $( x + h ) ^ { \alpha } - x ^ { \alpha }$ is decreasing for all $x \ge 0$ and hence $( x + h ) ^ { \alpha } - x ^ { \alpha } \leq h ^ { \alpha }$ ，This means that $x ^ { \alpha } \in$ Lip $\pmb { \alpha }$ on any positive interval.

# 1.6 Differentiable Functions

DEFINITION 1.6.1．Let $f ( x )$ be defined on an interval $\boldsymbol { \mathit { I } }$ It is said to be differentiableat a point $x _ { 0 } \in I$ if the following limit exists

$$
\operatorname* { l i m } _ { x \to x _ { 0 } } { \frac { f ( x ) - f ( x _ { 0 } ) } { x - x _ { 0 } } } = f ^ { \prime } ( x _ { 0 } ) .
$$

If $x _ { \mathbf { 0 } }$ is an end point of $\boldsymbol { \mathit { I } }$ then the limit in (1.6.l) is replaced by an appropriate one-sided limit.The function $f ( x )$ is differentiable on $\boldsymbol { \mathit { I } }$ if it is differentiable at each point of $\boldsymbol { I }$

Ex.1. $A ( x ) = \left| x \right|$ is differentiable at all $x \neq 0$ At $x = 0$ it possesses right and left hand derivatives $\operatorname* { l i m } _ { x \to 0 ^ { + } } , \operatorname* { l i m } _ { x \to 0 ^ { - } } \frac { A ( x ) - A ( 0 ) } { x - 0 }$

Ex. 2. $S ( x ) = \left\{ { \begin{array} { l l } { 0 \quad } & { x \leq 0 } \\ { 1 \quad } & { x > 0 } \end{array} } \right.$ is discontinuous at $x = 0$ and is not differentiable there.Elsewhere it is differentiable.

Ex. 3. $f ( x ) = x ^ { \frac { 1 } { 3 } }$ .Though continuous at ${ \pmb x } = { \bf 0 } , { \pmb f } ( { \pmb x } )$ fails to be differentiable there.It is sometimes convenient to write $f ^ { \prime } ( 0 ) = + \infty$

For differentiable functions,we have Rolle's Theorem and the Mean Value Theorem :

THEOREM 1.6.1 (Rolle). $L e t f ( x ) \in C [ a , b ]$ and be differentiable at each point of $( a , b )$ .If $f ( a ) = f ( b )$ then thereisa point ${ \pmb x } = { \pmb \xi }$ with $a < \xi < b$ for which $f ^ { \prime } ( \pmb { \xi } ) = 0$

THEOREM 1.6.2． Let $f ( x ) \in C [ a , b ]$ be differentiable at each point of $( a , b )$ Then we can find a ${ \pmb \xi }$ with $a < \xi < b$ such that

$$
f ( b ) = f ( a ) + ( b - a ) f ^ { \prime } ( \xi ) .
$$

If $f$ is differentiable at each point of $\pmb { I }$ ,its derivative $f ^ { \prime } ( x )$ may exhibit a wide variety of smoothness properties.A particularly noteworthy case is where $f ^ { \prime } ( x )$ is itself continuous on $\boldsymbol { \mathit { I } }$ .The class of functions that have a continuous derivative on $[ a , b ]$ is designated by $\scriptstyle C ^ { 1 } [ a , b ]$ .More generally,

DEFINITION 1.6.2. If $f ( x )$ is $\pmb { n }$ times differentiable on $[ \pmb { a } , \pmb { b } ]$ and if $f ^ { ( n ) } ( x )$ is itself continuous on $[ \pmb { a } , \pmb { b } ]$ ，we shall write $f ( x ) \in C ^ { n } [ a , b ]$

$C ^ { n } [ \pmb { a } , \pmb { b } ]$ is a linear space of functions.

Ex.4.Let

$$
f ( x ) = { \left\{ \begin{array} { l l } { x ^ { k } \quad } & { x \geq 0 } \\ { 0 \quad } & { x < 0 . } \end{array} \right. }
$$

Then, $f \in C ^ { k - 1 }$ on $- \infty < x < \infty$ .But $f \notin C ^ { k }$ on any interval containing the origin.

Ex.5.Let $f ( x ) = | x | ^ { \frac { 5 } { 2 } }$ .Then $f \in C ^ { 2 }$ ，but $f \not \in C ^ { 3 }$ on any interval containing the origin.

For functions having higher derivatives we have the following generalized Rolle's Theorem.

THEOREM 1.6.3． Let $n \geq 2$ Suppose that $\pmb { f } \in C [ \pmb { a } , \pmb { b } ]$ and let $f ^ { ( n - 1 ) } ( x )$ exist at each point of $( a , b )$ . Suppose that $f ( x _ { 1 } ) = f ( x _ { 2 } ) = \cdot \cdot \cdot = f ( x _ { n } ) = 0$ for $a \leq x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { n } \leq b $ Then there is $\pmb { a }$ point ${ \pmb \xi }$ ， $x _ { 1 } < \xi < x _ { n }$ such that $j ^ { ( n - 1 ) } ( \xi ) = 0$

Proof: We give the proof for $n = 3$ .The general case is similar. Let $f ( x _ { 1 } ) = f ( x _ { 2 } ) = f ( x _ { 3 } ) = 0$ Since $f$ is differentiable in $x _ { 1 } < x < x _ { 3 }$ we can find $\pmb { \xi _ { 1 } }$ and ${ \pmb { \xi _ { 2 } } }$ such that $x _ { 1 } < \xi _ { 1 } < x _ { 2 } < \xi _ { 2 } < x _ { 3 }$ and $f ^ { \prime } ( \pmb { \xi } _ { 1 } ) = 0$ ， $f ^ { \prime } ( \pmb { \xi } _ { 2 } ) = \mathbf { 0 }$

Since $f ^ { \prime \prime }$ also exists,a second application of Rolle's Theorem yields a $\pmb { \xi } ,$ $\xi _ { 1 } < \xi < \xi _ { 2 }$ with $f ^ { ( 2 ) } ( \xi ) = 0$

Taylor's Theorem with the exact remainder and the various expressions for the remainder involving higher derivatives constitute generalizations of the Mean Value Theorem.

THEOREM 1.6.4. Let $f ( x ) \in C ^ { n + 1 } [ a , b ]$ and let ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ . Then for all

$$
\begin{array} { c } { { a \leq x \leq b , f ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + { \displaystyle \frac { f ^ { \prime \prime } ( x _ { 0 } ) } { 2 ! } } ( x - x _ { 0 } ) ^ { 2 } + \cdot \cdot \cdot } } \\ { { + { \displaystyle \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } } ( x - x _ { 0 } ) ^ { n } + { \displaystyle \frac { 1 } { n ! } } { \displaystyle \int _ { x _ { 0 } } ^ { x } } f ^ { ( n + 1 ) } ( t ) ( x - t ) ^ { n } d t . } } \end{array}
$$

THEOREM 1.6.5．Let $f ( x ) \in C ^ { n } [ a , b ]$ and let $f ^ { ( n + 1 ) } ( x )$ exist in $( a , b )$ . Then there isa ${ \pmb \xi }$ with $a < \xi < b$ such that

$$
\begin{array} { c } { { f ( b ) = f ( a ) + f ^ { \prime } ( a ) ( b - a ) + \displaystyle { \frac { f ^ { \prime } ( a ) } { 2 ! } } ( b - a ) ^ { 2 } + \cdots } } \\ { { + \displaystyle { \frac { f ^ { ( n ) } ( a ) } { n ! } } ( b - a ) ^ { n } + \displaystyle { \frac { f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } ( b - a ) ^ { n + 1 } . } } \end{array}
$$

A form of the remainder theorem (sometimes referred to as Young's form) is useful on occasion.

THEOREM 1.6.6． Let $f ( x )$ be $\pm 1$ times differentiable at ${ \pmb x } = { \pmb x } _ { \pmb 0 }$ Then,

$$
\begin{array} { c } { { f ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + \displaystyle \cdots + \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } ~ ( x - x _ { 0 } ) ^ { n } } } \\ { { + \displaystyle \frac { ( x - x _ { 0 } ) ^ { n + 1 } } { ( n + 1 ) ! } \left[ f ^ { ( n + 1 ) } ( x _ { 0 } ) + \varepsilon ( x ) \right] } } \end{array}
$$

where

$$
\operatorname* { l i m } _ { x \to x _ { 0 } } \varepsilon ( x ) = 0 .
$$

Proof: Set

$$
R ( x ) = f ( x ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) - \cdot \cdot \cdot - { \frac { ( x - x _ { 0 } ) ^ { n + 1 } } { ( n + 1 ) ! } } f ^ { ( n + 1 ) } ( x _ { 0 } ) .
$$

Then (l.6.5) is equivalent to showing that $\operatorname* { l i m } _ { x \to x _ { 0 } } { \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } } = 0$ = 0.By differentiating,we find that

$$
R ( x _ { 0 } ) = R ^ { \prime } ( x _ { 0 } ) = \cdot \cdot \cdot = R ^ { ( n + 1 ) } ( x _ { 0 } ) = 0 .
$$

Let $\varepsilon > 0$ . The functions

$$
P ( x ) = R ( x ) + \varepsilon ( x - x _ { 0 } ) ^ { n + 1 } , Q ( x ) = R ( x ) - \varepsilon ( x - x _ { 0 } ) ^ { n + 1 }
$$

are $\pmb { n } + \pmb { 1 }$ times differentiable at ${ x } = { x } _ { 0 }$ .Moreover, $P ^ { ( k ) } ( x _ { 0 } ) = 0 , Q ^ { ( k ) } ( x _ { 0 } ) = 0$ $k = 0 , 1 , \ldots , n$ ,while $P ^ { ( n + 1 ) } ( x _ { 0 } ) = \varepsilon ( n + 1 ) ! > 0$ ，

$$
Q ^ { ( n + 1 ) } ( x _ { 0 } ) = - ( n + 1 ) ! \varepsilon < 0 .
$$

This implies that $P ( { \pmb x } )$ increases monotonically in some interval $( \pmb { x _ { 0 } } , \pmb { x _ { 0 } } + \delta )$ while $Q ( x )$ decreases monotonically in $( x _ { 0 } , \ x _ { 0 } + \delta )$ Therefore，for $_ { \pmb { x } }$ in $( x _ { 0 } , x _ { 0 } + \delta )$ ，

$$
\begin{array} { l l l l l l } { R ( x ) + \varepsilon ( x - x _ { 0 } ) ^ { n + 1 } > 0 } \\ { R ( x ) - \varepsilon ( x - x _ { 0 } ) ^ { n + 1 } < 0 . } \end{array}
$$

Therefore,

$$
- \varepsilon < \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } < \varepsilon .
$$

Since ε is arbitrary,(l.6.8) implies that $\operatorname* { l i m } _ { x \to x _ { 0 } + } { \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } } = 0$ =0.A similar argument shows that $\operatorname* { l i m } _ { x \to x _ { 0 } - } { \frac { R ( x ) } { ( x - x _ { 0 } ) ^ { n + 1 } } } = 0$ ,and the proof is complete.

# 1.7Infinitely Differentiable Functions

DEFINITION 1.7.1．If $f ( x ) \in C ^ { n } [ a , b ]$ for $n = 0 , 1 , 2 , \ldots$ ,then $f$ is called infinitelydifferentiablein $[ a , b ]$ . We shall write $C ^ { \infty } [ \pmb { a } , \pmb { b } ]$ for the class of such functions.

Ex. 1. $f ( x ) = x ^ { 2 }$ is infinitely differentiable on $- \infty < x < \infty$

Ex. 2. $f ( x ) = { \frac { 1 } { 1 + x ^ { 2 } } }$ is infinitely differentiable on $- \infty < x < \infty$

Ex. 3. $f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { \cos n x } { n ^ { \log n } } }$ is infitly diferetiable on $- \infty < x < \infty$ For since $| \cos n x | \le 1$ and $\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { \log n } } } < \infty$ ,the original series converges absolutely and uniformly. Since moreover,for any integer ： $p \ge 0 \sum _ { n = 1 } ^ { \infty } \frac { n ^ { p } } { n ^ { \mathrm { l o g } n } } < \infty$ ，the differentiated series of all orders converge uniformly and hence represent the respective derivatives of $f ( x )$

The functions of class $C ^ { \infty } [ { \pmb { a } } , { \pmb { b } } ]$ form a linear space.

If $f \in C ^ { \infty } [ a , b ]$ and ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ we may form the Taylor expansion

$$
f ( x ) \sim \sum _ { k = 0 } ^ { \infty } { \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } } ( x - x _ { 0 } ) ^ { n } .
$$

For a given $_ { \pmb { x } }$ this series may or may not converge. If it converges, it may or may not converge to $f ( x )$ . The famous function that displays this

behavior is

$$
f ( x ) = e ^ { - x ^ { - 2 } } , \quad x \neq 0 ; \quad f ( 0 ) = 0 .
$$

This function is in $C ^ { \infty } ( - \infty , \infty )$ and

$$
f ^ { ( n ) } ( 0 ) = 0 \qquad n = 0 , 1 , 2 , . . . .
$$

With $x _ { \mathbf { 0 } } = 0$ ，(1.7.1） converges to O for every $_ x$ .There are an infinity of functions of class $C ^ { \infty }$ for which (1.7,3) holds.If (1.7.1) converges to $f ( x )$ over an interval,we are led to the notion of an analytic function.

# 1.8 Functions Analytic on the Line

DEFINITION 1.8.1． Let $f ( x )$ be defined on $[ a , b ]$ and assume that at each point $x _ { \pmb 0 } \in [ \pmb { a } , \pmb { b } ]$ there is a power series expression of $f ( x )$ valid in some interval:

$$
f ( x ) = a _ { 0 } + a _ { 1 } ( x - x _ { 0 } ) + a _ { 2 } ( x - x _ { 0 } ) ^ { 2 } + \cdots , | x - x _ { 0 } | < p ( x _ { 0 } ) .
$$

Then $f ( x )$ is said to be analytic on the interval. We write $f ( x ) \in A [ a , b ] .$

$$
f ( x ) = [ ( x ) ( x - 1 ) ] ^ { - \frac { 1 } { 2 } } \in A [ \varepsilon , 1 - \varepsilon ] , 0 < \varepsilon < 1 - \varepsilon .
$$

Ex. 2. $f ( x ) = \int _ { 0 } ^ { x } e ^ { t ^ { 2 } } d t$ is analytic over theentire line $- \infty < x < \infty$

Ex.3. $A ( x ) = \left| x \right|$ is not analytic over an interval containing $x = 0$ inits interior.But it is“piece-wise”analytic.

THEOREM 1.8.1. $A [ { \pmb a } , { \pmb b } ]$ is $\pmb { a }$ linear space. If $f ( x ) \in A [ a , b ]$ then

$$
f ( x ) \in C ^ { \infty } [ a , b ] .
$$

The constants ${ \pmb a } _ { \pmb n }$ of (1.8.1) are

$$
a _ { n } = { \frac { 1 } { n ! } } f ^ { ( n ) } ( x _ { 0 } ) \qquad n = 0 , 1 , . . . .
$$

It does not follow conversely that if $f \in C ^ { \infty } [ a , b ]$ then $f \in A [ a , b ]$ This is demonstrated by the example (1.7.2).Another example is $f ( x ) = \sum _ { k = 1 } ^ { \infty } { \frac { \cos n x } { n ^ { \log n } } }$ which,as we have seen,is infinitely differentiable on $- \infty < x < \infty$ and of period $2 \pi$ .The ideas of Theorem l2.3.2 will show that $f ( x ) \not \in A [ - \pi , \pi ]$

# 1.9 Functions Analytic in a Region

DEFINITION 1.9.1． Let $\boldsymbol { R }$ be a region of the complex plane and let $f ( z )$ be a single valued function of the complex variable $\boldsymbol { z }$ defined in $\pmb { R }$ If $z _ { 0 } \in R , f ( z )$ is said to be analytic at ${ \boldsymbol { z } } _ { \mathbf { 0 } }$ (or regular at ${ z _ { \mathbf { 0 } } }$ ）if it has a representation of

the form

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

valid in some neighborhood of $z _ { 0 } \colon | z - z _ { 0 } | < p ( z _ { 0 } )$ .If $z _ { \mathbf { 0 } } = \infty$ , we require an expansion of the form

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { - n } , | z | > p .
$$

A function is analytic (or regular) in $\pmb { R }$ if it is analytic at each point of $\pmb { R }$ We shall write $A ( R )$ for the class of such functions. $A ( R )$ is a linear space.

Ex.1.The function f(z) = $f ( z ) = { \frac { 1 } { 1 + z ^ { 2 } } }$ is analytic in any region not containing the points $z ~ = ~ \pm i$

Ex.2.The function $f ( z ) \ = \int _ { 0 } ^ { z } e ^ { t ^ { 2 } } \ d t$ is analytic inanyregionnot cotaining $z = \infty$ ·

Ex.3.A branch of the function $f ( z ) = ( z ( z \ : - \ : 1 ) ) ^ { \frac { 1 } { 2 } }$ may be selected that is regular in any rectangle $0 < \varepsilon \le x \le 1 - \varepsilon$ ， $- R \leq y \leq R$

The relationship between functions analytic on a line and functions analytic in a region is given by the following theorem.

THEOREM 1.9.1． Let $f ( x ) \in A [ a , b ]$ . Then we can fnd a region $\pmb { R }$ containing $[ a , b ]$ into which $f ( x )$ can be continued analytically such that $f ( z ) \in A ( R )$

Proof: For each point $x _ { \mathbf { 0 } } \in [ a , b ]$ there is a quantity $\pmb { \mathscr { p } } ( \pmb { x _ { 0 } } )$ and an expansion

$$
f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( x - x _ { 0 } ) ^ { n } { \mathrm { ~ v a l i d ~ i n ~ } } | x - x _ { 0 } | < p ( x _ { 0 } ) .
$$

When $_ { x }$ is replaced by $z = x + i y$ ，(1.9.3)defines an analytic continuation of $f ( x )$ into the circle $| z - x _ { 0 } | < p ( x _ { 0 } )$ Let $\pmb { x _ { 0 } }$ run through the interval $[ a , b ]$ .The circles $| z - x _ { 0 } | < p ( x _ { 0 } )$ cover $[ a , b ]$ .Let $\pmb { R }$ be the union of these circles. $\pmb { R }$ is an open set and is arcwise connected. For if p, $q \in R$ ，join $\pmb { p }$ to $x _ { 1 }$ and $\pmb q$ to ${ \pmb x } _ { \mathbf { 2 } } ^ { }$ ,the centers of their respective circles.Then the arc $p x _ { 1 } x _ { 2 } q$ lies in $\boldsymbol { R } , \boldsymbol { R }$ is therefore a region and $f ( x )$ can be continued analytically into it.

![](images/9956dcce49eec34f1a2b804e6707edc66dce61f94316b987947dce8994726e14.jpg)  
Figure 1.9.1.

Cauchy's Theorem is a basic tool in complex analysis.

THEOREM 1.9.2． Let $\pmb { R }$ be $^ { \pmb { a } }$ simply connected region and let $f ( z ) \in A ( R )$ Let $z _ { \mathbf { 0 } }$ lie in $\pmb { R }$ and suppose that $c$ is $^ { \pmb { a } }$ simple,closed,rectifiable curve which lies in $\pmb { R }$ and which goes around ${ z _ { 0 } }$ in the positive sense. Then

$$
f ^ { ( n ) } ( z _ { 0 } ) = { \frac { n ! } { 2 \pi i } } \int _ { C } { \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { n + 1 } } } d z .
$$

Whenever the Cauchy integral formula is employed,it will be understood that $c$ satisfies the above conditions.

Analytic functions may be completely characterized by the growth of their derivatives,and this provides a second approach independent of power series.

THEOREM 1.9.3 (Pringsheim).Let $f ( x ) \in C ^ { \infty } [ a , b ]$ $\pmb { A }$ necessary and suffcient condition that $f \in A [ a , b ]$ is that there exist $\pmb { a }$ constant $r > 0$ such that

$$
| f ^ { ( n ) } ( x ) | \leq r ^ { n } n ! \quad a \leq x \leq b , \quad n = 0 , 1 , . . . .
$$

Proof: Sufficiency. Let $\pmb { x _ { 0 } }$ be a fixed point in $[ a , b ]$ and suppose that (1.9.5) holds. By Theorem 1.6.5 we have for ${ \pmb x } \in [ { \pmb a } , { \pmb b } ]$ ，

$$
f ( x ) = \sum _ { k = 0 } ^ { n - 1 } { \frac { f ^ { ( k ) } ( x _ { 0 } ) } { k ! } } ( x - x _ { 0 } ) ^ { k } + { \frac { f ^ { ( n ) } ( \xi ) } { n ! } } ( x - x _ { 0 } ) ^ { n } .
$$

This holds for all $\pmb { n }$ ,and $\xi = \xi ( n , x )$ is between $_ { \pmb { x } }$ and $\pmb { x _ { 0 } }$ In view of (1.9.5),

$$
\left| { \frac { f ^ { ( n ) } ( \xi ) } { n ! } } ( x - x _ { 0 } ) ^ { n } \right| \leq r ^ { n } | x - x _ { 0 } | ^ { n } ,
$$

so that if $| x - x _ { 0 } | < \frac { 1 } { r }$ ,the remainder in (1.9.6)willconverge to 0.The function $f$ possesses a power series expansion valid in a neighborhood of $\pmb { x _ { 0 } }$ This means that $f \in A [ a , b ]$ . Necessity. If $f \in A [ a , b ]$ ，then by Theorem 1.9.1,we can find a simply connected region $\pmb { R }$ containing $[ a , b ]$ in which $f$ is analytic. Let $\boldsymbol { c }$ be a curve surrounding $[ \pmb { a } , \pmb { b } ]$ and lying in $\pmb { R }$ .Then,for ${ \pmb x } _ { \pmb 0 } \in [ { \pmb a } , { \pmb b } ]$ ,we have from (1.9.4),

$$
\vert f ^ { ( n ) } ( x _ { 0 } ) \vert \leq { \frac { n ! } { 2 \pi } } \int _ { C } { \frac { \vert f ( z ) \vert } { \vert z - x _ { 0 } \vert ^ { n + 1 } } } d s .
$$

If $L ( C )$ denotes the length of $c$ and $\pmb { \delta }$ is the minimum distance from $c$ to $[ a , b ]$ ，then

$$
| f ^ { ( n ) } ( x ) | \leq { \frac { \operatorname* { m a x } _ { z \in C } \left| f ( z ) \right| L ( C ) n ! } { 2 \pi \delta ^ { n + 1 } } } = { \frac { M n ! } { \delta ^ { n } } } , a \leq x \leq b
$$

where $M$ is a constant independent of $\pmb { n }$ . It is now clear that we can find an $\boldsymbol { r }$ that makes (1.9.5) true.

Ex.4.Suppose $f \in A [ - 1 , 1 ]$ .It is impossible to have $f ^ { ( n ) } ( 0 ) = ( n ! ) ^ { 2 }$ For then, $\begin{array} { r } { ( n ! ) ^ { 2 } \leq r ^ { n } n ! } \end{array}$ ， $\textbf { \em n } = \textbf { 0 }$ ,1,....But,by Stirling's Theorem, $\tilde { \mathcal { V } } _ { n !  \mathrm { ~ \infty ~ } } ^ { - }$ so that we cannot find such an $\boldsymbol { r }$

On the other hand,if $f$ is analytic only in the semi-open interval $0 < x \le 1$ but is in $C ^ { \infty } [ 0 , 1 ]$ ，we may very well have $f ^ { ( n ) } ( 0 ) = ( n ! ) ^ { 2 }$ A theorem to this effect is developed in Chapter $\mathbf { v }$

Of great importance is the class of functions that are analytic in a circle $C _ { r } \colon | z | < r$ ，Here we have the fundamental theorem of Cauchy-Hadamard.

THEOREM 1.9.4．Let $f ( z ) \in A ( C _ { r } )$ but $\not \in A ( C _ { r ^ { \prime } } )$ if $r ^ { \prime } > r$ This holds if and only if

$$
r ^ { - 1 } = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { \infty } \left| { \frac { f ^ { ( n ) } ( 0 ) } { n ! } } \right| ^ { 1 / n }
$$

THEOREM 1.9.5 (Maximum Principle). Let $f ( z )$ be analytic in a region $\pmb { R }$ and not be constant there.Let $z _ { \mathbf { 0 } }$ lie in $\boldsymbol { R }$ .Then in any neighborhood of $z _ { \mathbf { 0 } }$ there exists $^ { \pmb { a } }$ point $z _ { 1 }$ where $| f ( z _ { 1 } ) | > | f ( z _ { 0 } ) |$ If $f ( z _ { 0 } ) \neq 0$ ,then in any neighborhood of $z _ { \mathbf { 0 } }$ there is $\pmb { a }$ point $z _ { 2 }$ where $| f ( z _ { 2 } ) | < | f ( z _ { 0 } ) |$

# 1.10 Entire Functions

DEFINITION 1.10.l． A function $f ( x )$ is called entire ifit has a representation of the form

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k } \quad \mathrm { \ v a l i d ~ f o r ~ } | z | < \infty .
$$

We shall designate this class of functions by $\pmb { \cal E } , \pmb { \cal E }$ is a linear space.

Ex.1. Some examples of entire functions are

THEOREM 1.10.1． The function $f ( z ) = \sum _ { k = 0 } ^ { \infty } a _ { k } z ^ { k }$ is entire if and only if

$$
\operatorname* { l i m } _ { n  \infty } | a _ { n } | ^ { 1 / n } = 0 .
$$

Proof: This follows from (1.9.9).

# 1.11 Polynomials

DEFINITIoN 1.1l.1． By a polynomial of degree $\pmb { n }$ is meant a function of the form

$$
p _ { n } ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdots + a _ { n } , a _ { 0 } \neq 0 .
$$

The class of polynomials of degree $\leq n$ will be designated by $\mathcal { P } _ { n }$

One might distinguish between the classes of polynomials with real coeffcients and with complex coefficients.It will usually be clear from the context which class we are dealing with and separate notations will not be introduced.

$\mathcal { P } _ { n }$ is a linear space.

The following basic facts about polynomials should be recaled.

THEOREM 1.l1.l (Fundamental Theorem of Algebra).If $\pmb { n } \geq 1$ , a polynomial of degree n possesses a complex root.

THEOREm l.l1.2 (Factorization Theorem).If $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( z )$ is a polynomial of degree $\pmb { n }$ then we may find $\pmb { n }$ complex numbers $z _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ such that

$$
\begin{array} { c } { \qquad \nu _ { n } ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { n } } \\ { \qquad \equiv a _ { 0 } ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) \quad ( a _ { 0 } \ne 0 } \end{array}
$$

The quantities $z _ { i }$ need not be distinct.If there are $r \leq n$ distinct roots $z _ { 1 } , z _ { 2 } , \ldots , z _ { r } ;$ ，then for appropriate positive integers $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { r } ,$ satisfying $\alpha _ { 1 } + \alpha _ { 2 } + \cdots + \alpha _ { r } = n$ ,we have

$$
p _ { n } ( z ) = a _ { 0 } ( z - z _ { 1 } ) ^ { \alpha _ { 1 } } ( z - z _ { 2 } ) ^ { \alpha _ { 2 } } \cdot \cdot \cdot ( z - z _ { r } ) ^ { \alpha _ { r } } .
$$

The ${ \pmb { \alpha } } _ { i }$ are uniquely determined and the zero $z _ { i }$ is known as an ${ \pmb { \alpha } } _ { i }$ fold zero. We have

$$
p _ { n } ( z _ { i } ) = { p _ { n } } ^ { \prime } ( z _ { i } ) = \dots = p _ { n } ^ { ( \alpha _ { i } - 1 ) } ( z _ { i } ) = 0 , p _ { n } ^ { ( \alpha _ { i } ) } ( z _ { i } ) \neq 0 .
$$

Conversely,these derivative conditions imply the above factorization.

THEOREM 1.11.3 (Uniqueness).If $f ( z ) \in \mathcal { P } _ { n }$ and $f$ vanishes at more than n distinct points then it vanishes identically.

Proof: Let the degree of $f$ be $k \leq n$ .By Theorem 1.11.2,

$$
f ( z ) = a _ { 0 } ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { k } ) .
$$

By hypothesis,we can find a point $z ^ { * } \neq z _ { 1 } , z _ { 2 } , \ldots , z _ { k }$ such that $f ( z ^ { * } ) = 0$ Then, $0 = a _ { 0 } ( z ^ { * } - z _ { 1 } ) \cdot \cdot \cdot ( z ^ { * } - z _ { k } )$ so that ${ a _ { \mathbf { 0 } } } = 0$ .This implies that

$$
f ( z ) \equiv 0 .
$$

1.12 Linear Functionals and the Algebraic Conjugate Space. In many problems,we must associate a number with a function extracted from a given class of functions.For instance,to each function $f ( x )$ that has a continuous derivative on $[ a , b ]$ ，we may want to associate the number $\int _ { a } ^ { b } ( 1 + [ f ^ { \prime } ( x ) ] ^ { 2 } ) ^ { \frac { 1 } { 2 } } d x$ .To each function $\pmb { f } ( \pmb { x } , y )$ that is twice continuously differentiable over a closed bounded region $\pmb { B }$ ，we may have to form the number $\iint _ { B } { \left( \frac { \partial f } { \partial x } \right) ^ { 2 } } + \left( \frac { \partial f } { \partial y } \right) ^ { 2 } d x d y$ or even more simply, $f ( x _ { 0 } , y _ { 0 } )$ where $( x _ { 0 } , y _ { 0 } ) \in B$ .Such an association is known as a functional.An important restriction is that the association behave linearly,and this leads to the following definition.

DEFINITION 1.12.1． Let $X$ be a linear vector space and to each $_ x$ let there be associated a unique real (or complex) number designated by $\scriptstyle { L ( x ) }$ If for : $\mathfrak { e } , \mathfrak { y } \in X$ and for all real (or complex) $\alpha , \beta$ we have

$$
L ( \alpha x + \beta y ) = \alpha L ( x ) + \beta L ( y ) ,
$$

then $L$ is called a linear functional over $X$

Ex. 1. $X = C [ a , b ]$ . The elements of $x$ are functions $f ( x )$

$$
L ( f ) = \int _ { a } ^ { b } f ( x ) d x \quad { \mathrm { o r } } \quad L ( f ) = \int _ { a } ^ { b } x ^ { 2 } f ( x ) d x .
$$

$$
\begin{array} { r l } & { X = C ^ { 2 } [ a , b ] . \ L ( f ) \ = f ^ { \prime \prime } ( a ) + f ^ { \prime } ( b ) \ - f \bigg ( \frac { a \ + \ b } { 2 } \bigg ) . } \\ & { X \ = A [ a , b ] . \ L ( f ) \ = \displaystyle \int _ { a } ^ { b } f ( x ) \ d x \ - \sum _ { i = 1 } ^ { n } a _ { i } f ( x _ { i } ) , a \ \leq x _ { i } \ \leq b . } \end{array}
$$

Ex. 4. $X = A ( R )$ where $\scriptstyle { R }$ is a region of the complex plane. Let $C$ bea rectifiable curve lying in $\scriptstyle { R }$

$$
L ( f ) = \int _ { C } f ( z ) d z .
$$

Ex.5. ${ \ X = R _ { n } . \ x = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) }$ .Let $a _ { 1 } , \ldots , a _ { n }$ be fixed constants and set

$$
L ( x ) = \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } .
$$

Interpolation theory is concerned with reconstructing functions on the basis of certain functional information assumed known.In many cases,the functionals are linear.

Functionals can be added to one another and scalar products can be formed. If,for instance, $f \in C ^ { 1 } [ a , b ]$ and

$$
L _ { 1 } ( f ) = \int _ { a } ^ { b } f ( x ) d x \quad { \mathrm { a n d } } \quad L _ { 2 } ( f ) = f ^ { \prime } \left( { \frac { a + b } { 2 } } \right) ,
$$

we can identify the functional

$$
L ( f ) = \alpha { \int _ { a } ^ { b } } f ( x ) d x + \beta f ^ { \prime } { \left( \frac { a + b } { 2 } \right) }
$$

with the expression $\alpha L _ { 1 } + \beta L _ { 2 } . L$ is itself a linear functional. These observations form the basis for the following definition.

DEFINITION 1.12.2． Let $\pmb { X }$ be a given linear space and let $L _ { 1 }$ and $L _ { 2 }$ be two linear functionals defined on $X$ . The sum of $L _ { 1 }$ and $L _ { 2 }$ and the scalar product of $\pmb { \alpha }$ and $L _ { 1 }$ are defined by

$$
\begin{array} { c } { { ( L _ { 1 } + L _ { 2 } ) ( x ) = L _ { 1 } ( x ) + L _ { 2 } ( x ) , x \in X } } \\ { { ( \alpha L _ { 1 } ) ( x ) = \alpha L _ { 1 } ( x ) . } } \end{array}
$$

It is a simple matter to show that the set of all linear functionals defined on $\pmb { X }$ combined by the above rules constitute a second linear space.

DEFINITION 1.12.3． Let $\pmb { X }$ be a given linear space.The set of linear functionals defined on $\pmb { X }$ and combined by (l.l2.2) forms a linear space called the algebraic conjugate space of $\pmb { X }$ and denoted by $x ^ { * }$

$x ^ { * }$ ，then，has elements that are linear functionals.We can speak of linear combinations, linear inderendence,dimension,bases,etc.,for linear functionals.

Ex.6. $X = C [ a , b ]$ .Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be $_ n$ distinct points lying in $[ a , b ]$ · Let $L _ { k } ( f ) = f ( x _ { k } )$ for $f \in X$ .Then $L _ { 1 } , L _ { 2 } , \ldots , L _ { n }$ are independent in $x ^ { * }$ .For otherwise,for constants $a _ { \mathbf { 1 } } , \ldots , a _ { n }$ not all zero, $a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdot \cdot \cdot + a _ { n } L _ { n } = 0$ (the O functional).Thus,for all $f \in C [ a , b ]$ $a _ { 1 } f ( x _ { 1 } ) + a _ { 2 } f ( x _ { 2 } ) + \cdot \cdot \cdot + a _ { n } f ( x _ { n } ) = 0$ . This is impossible.For if $a _ { k } \neq 0$ ，we may find a continuous function for which $f ( x _ { k } ) = 1 , f ( x _ { i } ) = 0 , i \neq k$ .This leads to the contradiction $a _ { k } = 0$

Ex. 7. $X = { \pmb { \mathscr P } } _ { n - 2 } [ a , b ]$ . The above $_ n$ functionals are linearly dependent.This isa consequence of the Lagrange interpolation formula in Chapter II.

THEOREM 1.12.1．If $\pmb { X }$ has dimension $\pmb { n }$ then $X ^ { * }$ has dimension n also.

Proof: Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ be a basis ( $\mathbf { \lambda } _ { n }$ independent elements).Then for any ${ \pmb x } \in { \pmb X }$ ， $x = a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n }$ in a unique way. Therefore, $L ( x ) = a _ { 1 } L ( x _ { 1 } ) + \cdot \cdot \cdot + a _ { n } L ( x _ { n } )$ .For any $\pmb { x } \in \pmb { X }$ set

$$
\begin{array} { l } { { L _ { 1 } ( x ) = a _ { 1 } } } \\ { { \ } } \\ { { L _ { 2 } ( x ) = a _ { 2 } } } \\ { { \ } } \\ { { . } } \\ { { \ . } } \\ { { L _ { n } ( x ) = a _ { n } . } } \end{array}
$$

$L _ { i }$ are linear functionals defned on $\pmb { X }$ ，They are independent,for,if not, we would have $\beta _ { 1 } L _ { 1 } + \beta _ { 2 } L _ { 2 } + \cdots + \beta _ { n } L _ { n } = 0$ with some $\beta _ { j } \neq 0$ .Then,

$$
\beta _ { 1 } L _ { 1 } ( x _ { j } ) + \beta _ { 2 } L _ { 2 } ( x _ { j } ) + \cdot \cdot \cdot + \beta _ { j } L _ { j } ( x _ { j } ) + \cdot \cdot \cdot + \beta _ { n } L _ { n } ( x _ { j } ) = 0 ( x _ { j } ) = 0 .
$$

But $L _ { i } ( x _ { j } ) = \delta _ { i j } = { \Big \{ } _ { 0 { \mathrm { ~ i f ~ } } i \neq j } ^ { 1 { \mathrm { ~ i f ~ } } i = j } { \Big . }$ so that we obtain $\beta _ { j } = 0$ ，a contradiction.

This shows that the dimension of $X ^ { * }$ is at least $\mathscr { n }$ .We next show it is at most $\pmb { n }$

Suppose we have $n + 1$ functionals, $L _ { 1 } , L _ { 2 } , \dots , L _ { n + 1 }$ .Consider the $n + 1$ $\pmb { n }$ -tuples

$$
[ L _ { i } ( x _ { 1 } ) , L _ { i } ( x _ { 2 } ) , \ldots , L _ { i } ( x _ { n } ) ] , \qquad i = 1 , 2 , \ldots , n + 1 .
$$

Since $\scriptstyle { R _ { n } }$ (or $C _ { n } )$ is of dimension $\pmb { n }$ ，these $\pmb { n }$ -tuples cannot be independent. Hence we can find numbers $\alpha _ { 1 } , \ldots , \alpha _ { n + 1 }$ not all zero such that

$$
\begin{array} { r l } & { \alpha _ { 1 } [ L _ { 1 } ( x _ { 1 } ) , \textrm { . . . , } L _ { 1 } ( x _ { n } ) ] + \cdot \cdot \cdot + \alpha _ { n + 1 } [ L _ { n + 1 } ( x _ { 1 } ) , \textrm { . . . , } L _ { n + 1 } ( x _ { n } ) ] } \\ & { \phantom { = } \quad \quad \quad \quad \quad \quad \quad \quad \quad = 0 = [ 0 , 0 , \textrm { . . . , } 0 ] . } \end{array}
$$

Therefore

$$
( \alpha _ { 1 } L _ { 1 } + \cdot \cdot \cdot + \alpha _ { n + 1 } L _ { n + 1 } ) ( x _ { i } ) = 0 , ~ \mathrm { f o r } ~ i = 1 , 2 , \ldots , n .
$$

By taking linear combinations,

$$
( \alpha _ { 1 } L _ { 1 } + \cdot \cdot \cdot + \alpha _ { n + 1 } L _ { n + 1 } ) ( x ) = 0 \quad \mathrm { f o r } \quad x \in X .
$$

Therefore $L _ { 1 } , \ldots , L _ { n + 1 }$ must be dependent and the dimension of $X ^ { * }$ is at most,and hence,precisely $\pmb { n }$

This theorem tells us that over a space $\pmb { X }$ of dimension $\pmb { n }$ any linear functional can be expressed as a linear combination of $\pmb { n }$ fixed independent linear functionals.

1.13 Some Assorted Facts. Two special conformal maps.

A.

$$
w = \textstyle \frac { 1 } { 2 } ( z + z ^ { - 1 } ) .
$$

Set $w = u + i v$ and $z = \rho e ^ { i \theta }$ . The exterior of the unit circle, $| z | > 1$ ,is mapped conformally onto the $\pmb { w }$ -plane with the interval $- 1 \leq u \leq 1$ deleted. The image of the point $( \rho \cos \theta , \rho \sin \theta )$ is the point

$$
( \ddagger ( \rho + \rho ^ { - 1 } ) \cos \theta , \ddagger ( \rho - \rho ^ { - 1 } ) \sin \theta ) .
$$

The circle $| z | = \rho > 1$ maps onto the ellipse

$$
\begin{array} { r } { u = \frac { 1 } { 2 } ( \rho + \rho ^ { - 1 } ) \cos \theta , v = \frac { 1 } { 2 } ( \rho - \rho ^ { - 1 } ) \sin \theta , 0 \leq \theta \leq 2 \pi . } \end{array}
$$

![](images/5b8220bf9fd249008fb2fad681ffd0c5ca92f29d92d82e932c0a515423a44738.jpg)  
Figure 1.13.1.

DEFINITIoN 1.13.1.The ellipse (1.13.2) will be designated by $\mathcal { E } _ { \rho }$ ， $( \pmb { \rho } > 1 )$ The semi-axes of $\mathcal { E } _ { \rho }$ are, respectively

$$
\begin{array} { c } { { { \pmb a } = \frac { 1 } { 2 } ( { \pmb \rho } + { \pmb \rho } ^ { - 1 } ) } } \\ { { { \pmb b } = \frac { 1 } { 2 } ( { \pmb \rho } - { \pmb \rho } ^ { - 1 } ) } } \end{array}
$$

and hence

The foci of $\mathcal { E } _ { \rho }$ are at $u = \pm 1$ so that $\mathcal { E } _ { \rho } ^ { \mathcal { ( } { ) } } , \rho > 1$ ,forms a confocal family of ellipses. The image of the unit circle under (l.l3.l） is the interval $- 1 \leq u \leq 1$ traced from l to $^ { - 1 }$ ,thence back to l.

When $z$ is solved for $\pmb { w }$ ，we obtain

$$
z = w + \sqrt { w ^ { 2 } - 1 } .
$$

For values of $z$ outside the unit circle,that branch of the root must be taken which leads to $z ( \infty ) = \infty$

![](images/821f5db0deaccd0d5c99059a8c981d56037a6c6d7a24e3ee264397dc23e11256.jpg)  
Figure 1.13.2 The Family $\mathbf { \boldsymbol { \mathcal { E } } } _ { \rho } ^ { \varphi }$ of Confocal Ellipses.

B.

$$
z = \cos w = \cos ( u + i v ) = \cos u \cosh v - i \sin u \sinh v .
$$

Let $\pmb { R }$ be the rectangle in the $\pmb { w }$ plane with vertices at $w = \sigma { i }$ ， $\sigma i + \pi ,$ $- \sigma i + \pi , - \sigma i . \ R$ is mapped onto the ellipse d ${ \mathfrak { s } } _ { \mathfrak { p } } , \ \pmb { \rho } = { \mathfrak { e } } ^ { \pmb { \sigma } }$ ，with the two intervals $[ 1 , { \pmb a } ] , [ - { \pmb a } , - 1 ]$ ， $a = \cosh \sigma$ ，deleted.As a point w traces out the vertical sides of $\pmb { R }$ ，the image point $\boldsymbol { z }$ traces each of these two intervals twice.

![](images/7762de965342e8b7605ea108b5b95b4c77982ee5608e43634d5dc7a903280ac6.jpg)  
Figure 1.13.3.

Zorn's Lemma. Today,a mathematics book without this lemma would be like an l8th century gentleman without his sword.

DEFINITION 1.13.2. A partial ordering of a set $X$ is a binary relation between elements designated by $^ { \ast } \leq ^ { \ast }$ and such that

$$
\begin{array} { l l l } { x \leq y , } & { y \leq z } & { \mathrm { i m p l i e s } } & { x \leq z } \\ { } & { } & { x \leq x } \\ { x \leq y , } & { y \leq x } & { \mathrm { i m p l i e s } } & { x = y . } \end{array}
$$

If in addition for auy $x , y \in X$ it is true that either

$$
x \leq y \quad { \mathrm { o r } } \quad y \leq x ,
$$

the set is called totally ordered (or,simply ordered).

If $\pmb { A }$ is a subset of a partially ordered set,and if an element $z$ satisfies

$$
x \leq z \quad { \mathrm { f o r ~ a l l } } \quad x \in A ,
$$

then $_ z$ is called an upper bound for $\pmb { A }$

If $z$ is an element of a partially ordered set $X$ such that no element $x \in X$ ， $x \neq z$ satisfies

$$
z \leq x
$$

then $\boldsymbol { z }$ is called a maximal element of $X$

THEOREM 1.13.1 (ZORN's LEMMA). Let $X$ be $^ { a }$ partially ordered set and suppose that every totally ordered subset of $X$ has an upper bound in X.Then $X$ has a maximal element.

Zorn's Lemma is known to be equivalent to the Axiom of Choice.

# NOTES ON CHAPTER I

1.1Determinant theory developed from the point of view of $\mathscr { n }$ -dimensional volume can be found in Schreier and Sperner [1], Chapter II.

1.4 For a discussion of when a function $w ( \delta )$ can be a modulus of continuity see Tieman [l],p.109.

1.7For more on infinitely differentiable functions,see Boas [4], pp.   
150-156.

1.10 An up-to-date account of the theory of entire functions is given in Boas [3].

1.12 For the algebraic conjugate space, see, e.g.，Taylor [3], pp.34-35.

1.13 Zorn's Lemma is discussed in Halmos [2],p. 62.

# PROBLEMS

1. For what values of $^ { a }$ and $^ { b }$ are the curves $y = a x ^ { b }$ bounded on [0,1]?

2.For what values of a andbare the curves y =x² +ax +b bounded on[-1,1]？

3.Show that $\frac { 1 } { x }$ sin x and $x \sin { \frac { 1 } { x } }$ (properly defined at $x = 0$ ）are continuous over any finite interval.

4.Show that $\begin{array} { r } { y = e ^ { - x } } \end{array}$ is uniformly continuous over the infinite interval

$$
0 \leq x < \infty .
$$

5.Let $f \in C [ a , b ]$ .Use the first mean value theorem to show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } f \left( x \right) \left| \sin n x \right| d x = \operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } f \left( x \right) \left| \cos n x \right| d x = { \frac { 2 } { \pi } } \int _ { a } ^ { b } f \left( x \right) d x . \ \mathrm { ( F e ] } \dot { \epsilon } \mathrm { r } ) .
$$

6. Compute $w ( f ; \delta )$ for $f ( x ) = \sin { x }$ on $- \infty < x < \infty$ ·

7. Compute $w ( f ; \delta )$ for $f ( x ) = x ^ { 2 } - 3 x + 1$ on $- 1 \leq x \leq 1$

8.Let $f ( x ) \in C ^ { 1 } [ a , b ]$ and let $f ^ { \prime } ( x )$ be increasing and positive.Find $w ( \delta )$

9.Let $f ( z )$ be analytic in $| z | \leq 1$ .Show that $w ( f ; \delta ) \leq M \delta$ for some $\pmb { M }$ Generalize.

10.Let $f ( x )$ be periodic and integrable. Define the moving average of $f$ by means of

$$
f _ { h } ( x ) = { \frac { 1 } { 2 h } } \int _ { x - h } ^ { x + h } f \left( t \right) d t .
$$

Prove: 1. $f _ { h } ( x )$ is periodic. 2.If $f \left( x \right) \in C ^ { n }$ then $f _ { h } ( x ) \in C ^ { n + 1 }$ 3. $w ( f _ { h } ; \delta ) \le w ( f ; \delta )$ and hence $f _ { h }$ is“smoother”than $f$ 4. If $f$ is sufficiently smooth, $( f _ { h } ( x ) ) ^ { \prime } = ( f ^ { \prime } ) _ { h }$

11. Let $f ( x )$ ， $g ( x ) \in \operatorname { L i p } \alpha$ on $[ a , b ]$ . Then the same is true of $f ( x ) \ g ( x )$

12. Does $x ^ { \alpha } \log x , \alpha > 0$ ，satisfy a Lipschitz condition on [0,1]?

13. If

$$
f ( x ) \in C ^ { 2 } [ a , b ] ,
$$

then

$$
( a ~ - b ) { f ^ { \prime } ( x ) } ~ = f ( a ) ~ - ~ f ( b ) ~ + ~ { \textstyle { \frac { 1 } { 2 } } } ( b ~ - x ) ^ { 2 } f ^ { \prime \prime } ( \xi _ { 1 } ) ~ - ~ { \textstyle { \frac { 1 } { 2 } } } ( a ~ - x ) ^ { 2 } f ^ { \prime \prime } ( \xi _ { 2 } )
$$

for $x \in ( a , b ) , a \mathit { \Theta } < \xi _ { 2 } < x , x \mathit { \Theta } < \xi _ { 1 } < b$

14.Use the last result to show that

$$
M _ { 1 } \leq \frac { 2 M _ { 0 } } { h } + \frac { 1 } { 2 } M _ { 2 } h
$$

where $M _ { i } = \operatorname* { m a x } _ { a \leq x \leq b } | f ^ { ( i ) } ( x ) |$ and $h = b - a$ . (Hadamard)

15. $\operatorname { I f } \operatorname* { l i m } _ { h \to 0 } { \frac { f ( x + h ) - 2 f ( x ) + f ( x - h ) } { h ^ { 2 } } }$ exists, $f ( x )$ is said to have a second Riemann derivative at $_ { x }$ .Use Theorem 1.6.6 to show that if $f ^ { \prime \prime } ( x )$ exists then the above limit exists and equals it. Show,however,that there are many functions that do not have a second derivative at $_ { x }$ but have a second Riemann derivative.

16. Let $f \in C ^ { 1 } [ a , b ]$ and let $f ^ { \prime \prime } ( x )$ exist at each point of $( a , b )$ . Suppose $f ( a ) =$ $f ^ { \prime } ( a ) = 0$ and $f ( b ) = 0$ ．Then there isa point ${ \pmb \xi }$ ， $a < \xi < b$ with $f ^ { \prime \prime } ( \pmb { \xi } ) = \mathbf { 0 }$ Generalize to functions having higher order zeros at $\pmb { k }$ points.

17. If $\operatorname* { l i m } _ { x \to \infty } f ( x ) = a$ and $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime \prime \prime } ( x ) = 0$ prove that $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime } ( x ) = 0$ and $\operatorname* { l i m } _ { x \to \infty } f ^ { \prime \prime } ( x ) = 0$

18.Let $f ( x ) , g ( x ) \in C ^ { \infty } [ a , b ]$ and $a \leq x _ { 0 } \leq b$ If $f ^ { ( n ) } ( x _ { 0 } ) = 0$ ,n = 0,1,2,..., then ${ \frac { d ^ { n } } { d x ^ { n } } } ( f ( x ) g ( x ) ) | _ { x _ { 0 } } = 0 , n = 0 , 1 , . . . . .$

19.1 $\sum \limits _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } , \sum \limits _ { n = 0 } ^ { \infty } b _ { n } z ^ { n }$ are algin $| z | < 1$ soi $\sum _ { n = 0 } ^ { \infty } a _ { n } b _ { n } z ^ { n }$

20.Use Theorem 1.9.3 to show that is in $A [ a , b ]$ for any $0 < a < b < \infty$

21. Show directly that $e ^ { e ^ { \pmb { x } } }$ satisfies the conditions of Theorem 1.9.3 on [0,1].

22. Make use of Theorem 1.10.l to show that $f ( z ) = \int _ { 0 } ^ { z } e ^ { t ^ { 2 } } d t$ is entire.

23.If $f ( z )$ is entire and satisfies $| f ( z ) | \geq m | z | ^ { n }$ for all $| z | > r$ ，then $\pmb { f }$ is a polynomial and its degree is at least $_ { n }$

24. Let $f \in \mathcal { P } _ { 2 }$ and suppose that $\pmb { f } ( a ) = \pmb { f } ^ { \prime } ( a ) = 0 , \pmb { f } ( b ) = 0 \textnormal { \pmb { b } } \neq a$ . Then $\pmb { f } \equiv \mathbf { 0 }$ In general, if $f \in \mathcal { P } _ { n }$ and has roots of total multiplicity $> n$ ,then $\pmb { f } \equiv 0$

25. Prove that $\mathbf { 2 } ^ { x }$ can coincide with a polynomial at only a finite number of points.Is this true when $_ { x }$ is replaced by $z ?$

26.Let $f \in A ( - \infty , \infty )$ and f(𝑘)(x)>0k=0,1,....Then $f ( x )$ cannot coincide with a polynomial infinitely often. Generalize.

27. If $f ( x )$ is a polynomial, then lim $f ^ { ( n ) } ( x ) = 0$ for all $_ { \pmb { x } }$ .Is the converse true? n→8

28.The spaces $C ^ { n } [ a , b ] , C ^ { \infty } [ a , b ] , A [ a , b ] , A ( R ) , .$ $\pmb { \cal E }$ are all infinite dimensional.

29. ${ \mathcal { P } } _ { n }$ defined on $[ a , b ]$ has dimension $n + 1$ .What about $\mathcal { P } _ { n }$ defined on a set $\pmb { S }$ consisting of $\pmb { k }$ points?

30.Let $A _ { r }$ designate the set of functions that are analytic in $| z | < r$ but in no disc $| z | < r ^ { \prime }$ with $r ^ { \prime } > r$ Is $A _ { r }$ a linear space?

31. Let $_ { x }$ be the space of all functions that are analytic in $| z | < R$ and have $| z | = R$ as a natural boundary. Is $\pmb { N }$ a linear space?

# CHAPTER II

# Interpolation

2.1 Polynomial Interpolation. This whole book can be regarded as a theme and variation on two theorems:an interpolation theorem of great antiquity and Weierstrass’approximation theorem of l885.The simple theorem of polynomial interpolation upon which much practical numerical analysis rests says,in effect,that a straight line can be passed through two points,a parabola through three,a cubic through four,and so on.

![](images/da8587d3ab9a4eeab60c56ef4567b8491dbfefcb7dce108ec54e6e30e8b058dd.jpg)  
Figure 2.1.1. Polynomial Interpolation.

THEOREM 2.1.1. Given $n + 1$ distinct (real or complex) points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ and $n + 1$ (real or complex) values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ There exists $^ { a }$ unique polynomial $\pmb { p } _ { n } ( z ) \in \mathcal { P } _ { n }$ for which

$$
p _ { n } ( z _ { i } ) = w _ { i } \qquad i = 0 , 1 , . . . , n .
$$

Proof:Set up a polynomial $a _ { 0 } + a _ { 1 } z + \cdots + a _ { n } z ^ { n }$ with $n + 1$ undetermined coefficients $a _ { i }$ ，The conditions (2.1.l) lead to the system of $n + 1$ linear equations in the ${ \bf { \em a } } _ { \imath }$ ：

$$
a _ { \pm } + a _ { 1 } z _ { i } + \cdot \cdot \cdot + a _ { n } z _ { \iota } { } ^ { n } = w _ { i } \qquad i = 0 , \ldots , n .
$$

The determinant of the system is the Vandermonde determinant formed

from $z _ { 0 } , \ldots , z _ { n }$ ：

$$
V ( z _ { 0 } , z _ { 1 } , \ldots , z _ { n } ) = \left| \begin{array} { c c c c c } { { 1 } } & { { z _ { 0 } } } & { { z _ { 0 } ^ { \ 2 } \cdot \cdot \cdot z _ { 0 } ^ { \ n } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { z _ { 1 } } } & { { z _ { 1 } ^ { \ 2 } \cdot \cdot \cdot z _ { 1 } ^ { \ n } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { 1 } } & { { z _ { n } } } & { { z _ { n } ^ { \ 2 } \cdot \cdot \cdot z _ { n } ^ { \ n } } } \end{array} \right| .
$$

To evaluate $V$ ,we may proceed as follows. Consider the function

$$
V ( z ) = V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z ) = \left| \begin{array} { c c } { { 1 } } & { { z _ { 0 } ~ ^ { . . . ~ } z _ { 0 } ^ { n } } } \\ { { . } } & { { . } } \\ { { . } } & { { . } } \\ { { . } } & { { . } } \\ { { 1 } } & { { z _ { n - 1 } ~ ^ { . . . ~ } z _ { n - 1 } ^ { n } } } \\ { { 1 } } & { { z ~ ^ { . . . ~ } z ^ { n } } } \end{array} \right| .
$$

$V ( z )$ is obviously in $\mathcal { P } _ { n }$ Furthermore it vanishes at $z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 }$ for inserting these values in place of $_ z$ yields two identical rows in the determinant. Thus,

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z ) = A ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } )
$$

where $\pmb { A }$ depends only on $z _ { 0 } , z _ { 1 } , \dotsc , z _ { n - 1 }$ . To evaluate $\pmb { A }$ ,expand the determinant in (2.1.4) by minors of its last row.We then see that the coefficient of $z ^ { n }$ is $V ( z _ { 0 } , \dots , z _ { n - 1 } )$ . Thus, we have

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z ) = V ( z _ { 0 } , . . . , z _ { n - 1 } ) ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } )
$$

and hence we have the recursion formula

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n - 1 } , z _ { n } ) = V ( z _ { 0 } , . . . , z _ { n - 1 } ) ( z _ { n } - z _ { 0 } ) ( z _ { n } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { n } - z _ { n - 1 } ) .
$$

Since $V ( z _ { 0 } , z _ { 1 } ) = z _ { 1 } - z _ { 0 }$ ,we have from (2.1.7),

$$
V ( z _ { 0 } , z _ { 1 } , z _ { 2 } ) = ( z _ { 1 } - z _ { 0 } ) ( z _ { 2 } - z _ { 0 } ) ( z _ { 2 } - z _ { 1 } )
$$

and by multiple applications of (2.1.7),

$$
V ( z _ { 0 } , z _ { 1 } , . . . , z _ { n } ) = \prod _ { i > j } ^ { n } ( z _ { i } - z _ { j } ) .
$$

By assumption, the points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ are distinct.Therefore $V \neq 0$ There is consequently a unique solution to the system (2.1.2).

Here is a second proof that contains a useful line of reasoning.Consider the system (2.1.2).If,when the right-hand side is O $( w _ { i } = 0 )$ ，the system possesses only the trivial zero solution，Theorem 1.2.2 tells us that its determinant does not vanish.Hence for an arbitrary right-hand side there is one and only one solution.Now a zero right-hand side to (2.l.2) means that $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( z )$ vanishes at $n + 1$ distinct points. By Theorem 1.11.3, $a _ { k } = 0 , k =$ $0 , 1 , \ldots , n$ 、The homogeneous equation possesses only the trivial solution and the rest follows.

2.2 The General Problem of Finite Interpolation. In Theorem 2.1.1 we have reconstructed a polynomial $\in \mathcal { P } _ { \pmb { n } }$ on the basis of $\pm 1$ values. Can we do it on the basis of $n + 1$ arbitrary pieces of linear information? Can we do it for functions other than polynomials? These questions lead to the following general problem.

Let $\pmb { X }$ be a linear space of dimension $\pmb { n }$ and let $L _ { 1 } , L _ { 2 } , \ldots , L _ { n }$ be $\pmb { n }$ given linear functionals defined on $\pmb { X }$ .For a given set of values $w _ { 1 } , w _ { 2 } , \ldots , w _ { n } ,$ can we find an element of $\pmb { X }$ ,say $_ { \pmb { x } }$ ，such that

$$
L _ { i } ( x ) = w _ { i } \qquad i = 1 , 2 , \ldots , n !
$$

The answer is yes if the $\scriptstyle { L _ { i } }$ are independent in $X ^ { * }$ ·

LEMMA 2.2.1. Let $\pmb { X }$ have dimension $\pmb { n }$ .If $x _ { 1 } , \ldots , x _ { n }$ are independent in $\pmb { X }$ and $L _ { 1 } , \ldots , L _ { n }$ are independent in $X ^ { * }$ then

$$
| L _ { i } ( x _ { j } ) | \neq 0 .
$$

Conversely， if either $x _ { 1 } , \ldots , x _ { n }$ or $L _ { 1 } , \ldots , L _ { n }$ are independent and (2.2.2) holds then the other set is also independent.

Proof: Suppose that $| L _ { i } ( x _ { j } ) | = 0$ .Then also $| L _ { j } ( x _ { i } ) | = 0$ The system

$$
\begin{array} { l } { { a _ { 1 } L _ { 1 } ( x _ { 1 } ) + a _ { 2 } L _ { 2 } ( x _ { 1 } ) + \cdots + a _ { n } L _ { n } ( x _ { 1 } ) = 0 } } \\ { { \ . } } \\ { { . } } \\ { { . } } \\ { { . } } \\ { { a , L _ { 1 } ( x _ { \infty } ) + a , L _ { 2 } ( x _ { \infty } ) + \cdots + a , L _ { \mathit { \Pi } } ( x _ { \infty } ) = 0 } } \end{array}
$$

would have a nontrivial solution $a _ { 1 } , \ldots , a _ { n }$

Then,

$$
( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdot \cdot \cdot + a _ { n } L _ { n } ) ( x _ { i } ) = 0 \qquad i = 1 , 2 , \ldots , n .
$$

Since ${ \pmb x _ { 1 } , \dotsb \cdot \dotsb , \pmb x _ { n } }$ form a basis for $\pmb { X }$ ，

$$
( a _ { 1 } L _ { 1 } + a _ { 2 } L _ { 2 } + \cdots + a _ { n } L _ { n } ) ( x ) = 0 \qquad x \in X
$$

and hence $a _ { 1 } L _ { 1 } + \cdots + a _ { n } L _ { n } = 0$

Therefore, $L _ { 1 } , \ldots , L _ { n }$ are dependent contrary to our assumption.

To show the converse,we may trace the argument backwards.

THEOREM 2.2.2. Let a linear space $\pmb { X }$ have dimension n and let $L _ { 1 } , L _ { 2 } , \ldots$ ， $L _ { n }$ be $\pmb { n }$ elements of $x ^ { * }$ .The interpolation problem (2.2.l) possesses a solution for arbitrary values $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ if and only if the $L _ { i }$ are independent in $X ^ { * }$ The solution will be unique.

Proof:In this generality，the theorem is nothing but a rewording of Theorem 1.2.2. If the $\mathbf { } L _ { i }$ are independent and if $x _ { 1 } , \ldots , x _ { n }$ are independent, then $| L _ { i } ( x _ { j } ) | \neq 0$ by Lemma 2.2.1.Hence the system

$$
L _ { i } ( a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) = w _ { i } ~ i = 1 , 2 , \ldots , n
$$

Qr

$$
a _ { 1 } L _ { i } ( x _ { 1 } ) + a _ { 2 } L _ { i } ( x _ { 2 } ) + \cdot \cdot \cdot + a _ { n } L _ { i } ( x _ { n } ) = w _ { i }
$$

possesses a solution $a _ { 1 } , \ldots , a _ { n }$ and the element $\sum _ { i = 1 } ^ { n } a _ { i } x _ { i }$ solves the inter-  
polation problem.Conversely，if the problem (2.2.l） has a solution for arbitrary $w _ { i }$ ,then (2.2.3) has a solution for arbitrary $w _ { i }$ .By Theorem 1.2.2, this implies that $| L _ { \ i } ( x _ { j } ) | \neq 0$ and hence by Lemma 2.2.1, the $L _ { i }$ are independent.

The determinant $| L _ { i } ( x _ { j } ) |$ is a generalized Gram determinant (cf. Chapter 8.7)and its nonvanishing is synonomous with the possibility of solution of the interpolation problem.We may speak of independent systems of functionals as having the“interpolation property.’In the next section,we shall study some spaces and functionals for which the interpolation problem can be solved.But before passing to it,we should rid ourselves of the naive hope that an interpolation problem can always be solved providing the number of parameters equals the number of conditions.

Ex.1.Let $x$ designate the set of functions of the form $a _ { 0 } + a _ { 2 } x ^ { 2 }$ defined on [-1,1]. $x$ has dimension 2. If $L _ { 1 } ( f ) = f ( x _ { 1 } )$ and $L _ { 2 } ( f ) = f ( x _ { 2 } ) , - 1 \leq x _ { 1 } , x _ { 2 } \leq 1$ then the generalized Gram determinant for the independent elements 1, $x ^ { 2 }$ is

$$
\left| \begin{array} { c c } { { 1 } } & { { { x _ { 1 } } ^ { 2 } } } \\ { { } } & { { } } \\ { { 1 } } & { { { x _ { 2 } } ^ { 2 } } } \end{array} \right| = ( x _ { 2 } - x _ { 1 } ) ( x _ { 2 } + x _ { 1 } ) .
$$

This vanishes if $x _ { 1 } = x _ { 2 }$ or $x _ { 1 } = - x _ { 2 }$ In these cases $L _ { 1 }$ and $\scriptstyle L _ { 2 }$ are not independent.The frst case would be excluded trivially,but the second tells us that we cannot force the even functions $a _ { 0 } + a _ { 2 } x ^ { 2 }$ to take on arbitrary values at distinct points.

Ex.2. The strength of Theorem 2.1.1 is brought out by noting that it cannot be extended as it stands to polynomial interpolation in several variables.Let the powers in two real variables be listed as follows: $p _ { \mathbf { 0 } } ( x , y ) = 1$ ， $p _ { 1 } ( x , y ) = x$ ， $p _ { 2 } ( x , y ) = y ;$ $p _ { 3 } ( x , y ) = x ^ { 2 }$ ， $p _ { 4 } ( x , y ) = x y$ ， $p _ { 5 } ( x , y ) = y ^ { 2 }$ ， $p _ { 6 } ( x , y ) = x ^ { 3 }$ .... It is not always possible,having been given $_ n$ arbitrary distinct points $( x _ { i } , y _ { i } )$ ，to find a linear combination of $p _ { 0 } , \ldots , p _ { n - 1 }$ that takes on preassigned values at these points.

2.3 Systems Possessing the Interpolation Property. Many spaces offunctions and related systems of independent functionals are known and have been studied in detail. We shall list some of the more common ones.

Ex.1. (Interpolation at discrete points)

$$
X = { \mathcal { P } } _ { n } . \quad L _ { 0 } ( f ) = f ( z _ { 0 } ) , L _ { 1 } ( f ) = f ( z _ { 1 } ) , . . . , L _ { n } ( f ) = f ( z _ { n } ) .
$$

We assume that $z _ { i } \neq z _ { j } , i \neq j$

Ex.2． (Taylor interpolation)

$$
X = { \mathcal { P } } _ { n } . \quad L _ { 0 } ( f ) = f ( z _ { 0 } ) , L _ { 1 } ( f ) = f ^ { \prime } ( z _ { 0 } ) , . . . , L _ { n } ( f ) = f ^ { ( n ) } ( z _ { 0 } ) .
$$

Ex.3. (Abel-Gontscharoff Interpolation)

$$
X = \mathcal { P } _ { n } . \quad L _ { 0 } ( { f } ) = f ( z _ { 0 } ) , L _ { 1 } ( { f } ) = f ^ { \prime } ( z _ { 1 } ) , L _ { 2 } ( { f } ) = f ^ { \prime \prime } ( z _ { 2 } ) , \dots , L _ { n } ( { f } ) = f ^ { ( n ) } ( z _ { n } ) .
$$

Ex.4.(Lidstone Interpolation)

$$
\begin{array} { r l } { X = \mathcal { P } _ { 2 n + 1 } . } & { L _ { 1 } ( f ) = f ( z _ { 0 } ) , L _ { 2 } ( f ) = f ( z _ { 1 } ) } \\ & { L _ { 3 } ( f ) = f ^ { \prime \prime } ( z _ { 0 } ) , L _ { 4 } ( f ) = f ^ { \prime \prime } ( z _ { 1 } ) } \\ & { . } \\ & { . } \end{array}
$$

$$
L _ { 2 n + 1 } ( f ) = f ^ { ( 2 n ) } ( z _ { 0 } ) , L _ { 2 n + 2 } ( f ) = f ^ { ( 2 n ) } ( z _ { 1 } ) , ( z _ { 0 } \ne z _ { 1 } ) .
$$

Ex.5. (Simple Hermite or Osculatory Interpolation)

$$
\begin{array} { r l r } { X = \mathcal { P } _ { 2 n - 1 } . } & { } & { L _ { 1 } ( f ) = f ( z _ { 1 } ) , L _ { 2 } ( f ) = f ^ { \prime } ( z _ { 1 } ) } \\ & { } & { L _ { 3 } ( f ) = f ( z _ { 2 } ) , L _ { 4 } ( f ) = f ^ { \prime } ( z _ { 2 } ) } \\ & { } & { . } \\ & { } & { . } \end{array}
$$

$$
L _ { 2 n - 1 } ( f ) = f ( z _ { n } ) , L _ { 2 n } ( f ) = f ^ { \prime } ( z _ { n } ) , ( z _ { i } \ne z _ { j } , i \ne j ) .
$$

Ex.6． (Full Hermite Interpolation) $\boldsymbol { X } = \mathcal { P } _ { N }$ ，To avoid indexing difficulties,we list the functional information employed without using the symbol $L$ ·

$$
\begin{array} { l } { f ( z _ { n } ) , f ^ { \prime } ( z _ { n } ) , \ldots , f ^ { ( m _ { n } ) } ( z _ { n } ) } \\ { \quad ( z _ { i } \ne z _ { j } , N = m _ { 0 } + m _ { 1 } + \cdot \cdot \cdot + m _ { n } + n ) . } \end{array}
$$

Ex.7． (Generalized Taylor Interpolation) $x$ consists of the linear combinations of the $n + 1$ linearly independent functions $\varphi _ { \bf 0 } ( z ) , \varphi _ { \bf 1 } ( z ) , \ldots , \varphi _ { n } ( z )$ that are analytic at $z _ { \mathbf { 0 } }$

$$
\begin{array} { r l } & { L _ { \bf 0 } ( f ) = f ( z _ { \bf 0 } ) , L _ { \bf 1 } ( f ) = f ^ { \prime } ( z _ { \bf 0 } ) , \ldots , } \\ & { } \\ & { L _ { \bf n } ( f ) = f ^ { ( n ) } ( z _ { \bf 0 } ) . } \end{array}
$$

$$
\vert \varphi _ { i } ^ { ( j ) } ( z _ { 0 } ) \vert \neq 0 .
$$

Ex.8． (Trigonometric Interpolation)

A linear combination of 1,cos $_ x$ ...,cos $_ { n x }$ ，sin $_ x$ sin $\mathbf { 2 } x$ ....,sin nx is known as a trigonometric polynomial of degree $\leq n$ . The corresponding linear space will be designated by $\mathcal { T } _ { n }$ .It has dimension $2 n \mathrm { ~ + ~ } 1$

$$
\begin{array} { r l } { X = \mathcal { T } _ { n } . \ } & { L _ { 0 } ( f ) = f ( x _ { 0 } ) , L _ { 1 } ( f ) = f ( x _ { 1 } ) , . . . , L _ { 2 n } ( f ) = f ( x _ { 2 n } ) , } \\ & { - \pi \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { 2 n } < \pi . } \end{array}
$$

Ex.9． (Fourier Series)

$$
\begin{array} { r l } { X = \mathcal { T } _ { n } . \quad L _ { 2 k } ( f ) = \displaystyle \int _ { - \pi } ^ { \pi } f ( x ) \cos k x d x , k = 0 , 1 , \ldots , n . } & { } \\ { L _ { 2 k - 1 } ( f ) = \displaystyle \int _ { - \pi } ^ { \pi } f ( x ) \sin k x d x , k = 1 , 2 , \ldots , n . } & { } \end{array}
$$

Before demonstrating that these functionals are independent over the respective spaces,a few remarks are in order.Ex.1 is,of course,Theorem 2.1.1.Exs.1,2,5 are special cases of Ex. 6. Ex.2 is a special case of Ex.7 if we select $\varphi _ { k } ( z ) = z ^ { k }$ .Ex.9 is not generally thought of as an interpolation process since the usual interpolatory processes make use of point data.But it—and indeed all orthogonal expansions-fit into the present pattern,and so we have listed it here.

The most direct way to show that the interpolation problem formed from these examples has a solution is to exhibit the solution explicitly.For some of the examples,we shall do this in subsequent sections.But it suffces to show that the generalized Gram determinant does not vanish,(2.2.2),or to apply the Alternative Theorem 1.2.2 directly.

Ex.6.We shall show that if $\mathcal { P } \in \mathcal { P } _ { N }$ and satisfies

$$
\begin{array} { r l r } { \ } & { } & { p ( z _ { 0 } ) = 0 , p ^ { \prime } ( z _ { 0 } ) = 0 , \ldots , p ^ { m _ { 0 } } ( z _ { 0 } ) = 0 } \\ { \ } & { } & { p ( z _ { 1 } ) = 0 , p ^ { \prime } ( z _ { 1 } ) = 0 , \ldots , p ^ { m _ { 1 } } ( z _ { 1 } ) = 0 } \\ { \ } & { } & { \cdot } \\ { \ } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \ } & { } & { p ( z _ { , n } ) = 0 , p ^ { \prime } ( z _ { n } ) = 0 , \ldots , p ^ { m _ { n } } ( z _ { n } ) = 0 } \end{array}
$$

where $N = m _ { 0 } + m _ { 1 } + \cdot \cdot \cdot + m _ { n } + n$ ，then $\mathscr { p }$ must vanish identically.By the Factorization Theorem,if $\pmb { p }$ satisfies all conditions of (2.3.1) with the exception of the last, i.e., $p ^ { m _ { n } } ( z _ { n } ) = 0$ ,then we must have

$$
p ( z ) = A ( z ) ( z - z _ { 0 } ) ^ { m _ { 0 } + 1 } ( z - z _ { 1 } ) ^ { m _ { 1 } + 1 } \cdot \cdot \cdot ( z - z _ { n - 1 } ) ^ { m _ { n - 1 } + 1 } ( z - z _ { n } ) ^ { m _ { n } } ,
$$

A(z) = polynomial.

By examining the degree of this product, it appears that $A =$ constant. Since, moreover,

$$
p ^ { ( m _ { n } ) } ( z _ { n } ) = A ( m _ { n } ) ! ( z _ { n } - z _ { 0 } ) ^ { m _ { 0 } + 1 } \cdot \cdot \cdot ( z _ { n } - z _ { n - 1 } ) ^ { m _ { n - 1 } + 1 } = 0
$$

and ${ \pmb z } _ { i } \neq { \pmb z } _ { j } , \ i \neq j ,$ ，we have $ { \textbf { A } } = 0$ and therefore ${ \boldsymbol { \mathscr { p } } } \equiv 0$ ．The homogeneous interpolation problem has the zero solution only and hence the nonhomogeneous problem possesses a unique solution.

Ex.3. The generalized Gram determinant is

$$
\scriptstyle { \begin{array} { l } { { \begin{array} { l l l l l } { \scriptstyle 1 } & { \ z _ { 0 } } & { \ z _ { 0 } ^ { \ 2 } \cdot \cdot \cdot \ z _ { 0 } ^ { n } } \\ { \scriptstyle 0 } & { \ 1 } & { \ 2 z _ { 1 } \cdot \cdot \cdot n z _ { 1 } ^ { n - 1 } } \\ { \scriptstyle 0 } & { \ 0 } & { \ 2 \ \cdot \cdot \cdot \ n ( n - 1 ) z _ { 2 } ^ { n - 2 } } \\ { \scriptstyle \cdot } & { \ } & { \ \cdot } \\ { \scriptstyle \cdot } & { \ } & { \ \cdot } \\ { \scriptstyle \cdot } & { \ } & { \ \cdot } \\ { \scriptstyle 0 } & { \ 0 } & { \ 0 } & { \ \cdot \cdot \ n ! } \end{array} } } \end{array} } = 1 ! \ \ 2 ! \cdot \cdot \cdot n ! \ \neq 0 .
$$

Ex.4.Let $\boldsymbol { p } \in \mathscr { P } _ { 2 n + 1 }$ .If $p ^ { ( 2 j ) } ( z _ { 0 } ) = 0$ for $j = 0 , 1 , \ldots , n$ ，then by Theorem 1.6.4， $p ( z ) = a _ { 1 } ( z - z _ { 0 } ) + a _ { 3 } ( z - z _ { 0 } ) ^ { 3 } + \cdot \cdot \cdot + a _ { 2 n + 1 } ( z - z _ { 0 } ) ^ { 2 n + 1 }$ Ifnow, $p ^ { ( 2 n ) } ( z _ { 1 } ) = 0$ then $a _ { 2 n + 1 } = 0$ and $p ^ { ( 2 j ) } ( z _ { 1 } ) = 0 , j = n \ - 1 , n \ - \ 2 , . \ . \ . \ , 0$ implies, by recurrence,that the remaining coefficients are O.The homogeneous problem possesses the O solution only,and so the nonhomogeneous problem has a solution and it is unique.

As far as Ex.7 is concerned,no proof is required,for condition (2.2.2) has been built into the hypothesis.In this example,the crucial determinant reduces to the Wronskian of the functions $\phi _ { 0 } , \ldots , \phi _ { n }$ and we postulate that it does not vanish at ${ \pmb z _ { 0 } }$

Ex.8. The crucial determinant here is

$$
\begin{array} { r } { G = \left[ \begin{array} { l l l l l l l } { 1 . \cos x _ { 0 } } & { \sin x _ { 0 } } & { \cos 2 x _ { 0 } } & { \sin 2 x _ { 0 } } & { \cdot \cdot \cdot \cos n x _ { 0 } } & { \sin n x _ { 0 } } \\ { 1 } & { \cos x _ { 1 } } & { \sin x _ { 1 } } & { \cos 2 x _ { 1 } } & { \sin 2 x _ { 1 } } & { \cdot \cdot \cdot } & { \cos n x _ { 1 } } & { \sin n x _ { 1 } } \\ { . } & { } & { } & { } & { \cdot } & { } \\ { . } & { } & { } & { } & { \cdot } & { } \\ { . } & { } & { } & { } & { } & { \cdot } \\ { 1 } & { \cos x _ { 2 n } } & { \sin x _ { 2 n } } & { \cos 2 x _ { 2 n } } & { \sin 2 x _ { 2 n } } & { \cdot \cdot \cdot } & { \cos n x _ { 2 n } } & { \sin n x _ { 2 n } } \end{array} \right] . } \end{array}
$$

To evaluate $G$ we reduce its elements to complex form. Multiply the 3rd, 5th,... columns by $\mathbf { \chi } _ { i } ^ { \star }$ and add them respectively to the 2nd,4th,...columns.We obtain

$$
G \ = \ | 1 e ^ { i x _ { j } } \sin x _ { j } e ^ { 2 i x _ { j } } \sin 2 x _ { j } . . . e ^ { n i x _ { j } } \sin n x _ { j } | .
$$

Multiply the 3rd, 5th,...columns by $- 2 i$ and to them add the 2nd, 4th,...

columns respectively:

$$
( - 2 i ) ^ { n } G = | 1 e ^ { i x _ { j } } e ^ { - i x _ { j } } e ^ { 2 i x _ { j } } e ^ { - 2 i x _ { j } } . \cdot \cdot \cdot e ^ { n i x _ { j } } e ^ { - n i x _ { j } } | .
$$

Interchange the columns:

$$
( - 1 ) ^ { n ( n + 1 ) } ( - 2 i ) ^ { n } G = \big | e ^ { - n i x _ { j } } e ^ { - ( n - 1 ) i x _ { j } } \cdot \cdot \cdot 1 \cdot \cdot e ^ { ( n - 1 ) i x _ { j } } e ^ { n i x _ { j } } \big | .
$$

Multiply the jth row by $e ^ { n i x _ { j } } , j = 0 , . . . , 2 n$ ：

$$
e ^ { n i ( x _ { o } + x _ { 1 } + \cdots + x _ { 2 n } ) } ( - 1 ) ^ { n ( n + 1 ) } ( - 2 i ) ^ { n } { \cal G } = | 1 e ^ { i x _ { j } } e ^ { 2 i x _ { j } } \cdots e ^ { 2 n i x _ { j } } | .
$$

The determinant in the last line is a Vandermonde. Hence from (2.1.8),

$$
e ^ { n i ( x _ { 0 } + x _ { 1 } + \cdots + x _ { 2 n } ) } ( - 1 ) ^ { n ( n + 1 ) } ( - 2 i ) ^ { n } { \cal G } \ = \ \prod _ { j > k } ^ { 2 n } \ ( e ^ { i x _ { j } } - e ^ { i x _ { k } } ) .
$$

In view of the conditions on the $x _ { j } , e ^ { i x _ { j } } \neq e ^ { i x _ { k } } , j \neq k _ { \mathrm { ; } }$ and so $G \neq 0$

Ex.9.In view of the orthogonality of the sines and cosines (Chap. 8.3, Ex.3),the crucial determinant has positive quantities on the main diagonal and O's elsewhere and hence does not vanish.

2.4 Unisolvence. Let the functions $f _ { 1 } ( x ) , f _ { 2 } ( x ) , \ldots , f _ { n } ( x )$ be defined on an interval $\pmb { I }$ Given $\pmb { n }$ distinct points $x _ { 1 } , \dotsc , x _ { n } \in I$ and $\pmb { n }$ values $w _ { 1 } , . . . ,$ $w _ { n }$ ,we will be able to solve uniquely the interpolation problem

$$
\sum _ { i = 0 } ^ { n } a _ { i } f _ { i } ( x _ { j } ) = w _ { j } \qquad j = 1 , 2 , \ldots , n
$$

if and only if

$$
| f _ { i } ( x _ { j } ) | \neq 0 .
$$

DEFINITION 2.4.1． A system of $\pmb { n }$ functions $f _ { 1 } , \ldots , f _ { n }$ defined on a point set $s$ is called unisolvent on $\pmb { S }$ if (2.4.2) holds for every selection of $\pmb { n }$ distinct points lying in $\pmb { S }$

Pointwise interpolation can always be carried out uniquely with a unisolvent system.

It follows that $f _ { 1 } , \ldots , f _ { n }$ is unisolvent on $\pmb { S }$ if and only if the only linear combination of the $f ^ { ; }$ sthat vanishes on $\pmb { n }$ distinct points of $\pmb { S }$ vanishes identically.

Ex.1．The system 1, $\pmb { x ^ { 2 } }$ is unisolvent on [0,1] but not on[-1,1].

Ex. 2. The system $1 , x , x ^ { 2 } , \ldots , x ^ { n }$ is unisolvent over any interval $[ a , b ]$ ·

Ex.3.Suppose that ${ \pmb w } ( { \pmb x } )$ does not vanish on $[ a , b ]$ . Then

$$
w ( x ) , x w ( x ) , x ^ { 2 } w ( x ) , \textrm { . . . , } x ^ { n } w ( x )
$$

is unisolvent on $[ a , b ]$

Ex. 4. The system of complex powers $1 , z , z ^ { 2 } , \ldots , z ^ { n }$ is unisolvent over any region.

Ex.5. The trigonometric system

1, cos $_ { \pmb { x } }$ cos $\mathbf { 2 } x$ ...,cos $_ { n x }$ ,sin $_ x$ sin $\pmb { 2 x }$ ....,sin nx

is unisolvent on $- \pi \leq x < \pi$

Ex.6.Let $\pmb { a } _ { i }$ be distinct values not in $[ \pmb { a } , \pmb { b } ]$ .Then the system

$$
{ \frac { 1 } { x \ + a _ { 1 } } } , { \frac { 1 } { x \ + a _ { 2 } } } , \ \ldots \ , { \frac { 1 } { x \ + a _ { n } } }
$$

is unisolvent in $[ a , b ]$ .For we shall prove in Chap.I1.3 that

$$
\left| { \frac { 1 } { x _ { i } + a _ { j } } } \right| = \prod _ { i > j } ^ { n } ( x _ { i } - x _ { j } ) ( a _ { i } - a _ { j } ) \left/ \prod _ { i , j = 1 } ^ { n } ( x _ { i } + a _ { j } ) . \right.
$$

As far as functions of one variable are concerned,unisolvent systems are reasonably plentiful.In several dimensions,the situation is vastly different. We have already had a hint of this in 2.2,Ex.2 where we noticed that the fundamental theorem of polynomial interpolation does not go over directly to several variables.

THEOREM 2.4.1 (Haar).Let $s$ be a point set in a Euclidean space of $\pmb { n }$ dimension, $\scriptstyle { R _ { n } }$ ， $\mathscr { n } \geq 2$ Suppose that $s$ contains an interior point $\pmb { p }$ Let $f _ { 1 } , f _ { 2 } , \ldots , f _ { n } ( n > 1 )$ be defined on $\pmb { S }$ and continuous in $^ { \pmb { a } }$ neighborhood of $\pmb { p }$ Then this set of functions cannot be unisolvent on $\pmb { S }$

Proof: Let $\boldsymbol { U }$ be a ball with center at $\pmb { p }$ and contained in $\pmb { S }$ and sufficiently small so that the $f _ { i }$ are continuous in $\boldsymbol { U }$ .Select $\pmb { n }$ distinct points $p _ { 1 } , p _ { 2 } , \ldots ,$ ${ \pmb { p } } _ { \pmb { n } } \in U$ .We may assume that $| f _ { i } ( p _ { j } ) | \neq 0$ ,for otherwise the system is surely not unisolvent.Hold the points $p _ { 3 } , p _ { 4 } , \ldots , p _ { n }$ fixed. Now move the points ${ \pmb p _ { 1 } }$ and ${ \pmb p _ { \mathbf { 2 } } }$ continuously through $\boldsymbol { U }$ in such a manner that the positions of $\pmb { p _ { 1 } }$ and ${ \pmb p _ { 2 } }$ are interchanged. Since $\boldsymbol { U }$ has dimension $\geq 2$ ,it is clear that this can be carried out in such a manner that $\pmb { p _ { 1 } }$ and ${ \pmb p _ { \mathbf { 2 } } }$ coincide neither with one another nor with the remaining points.In this way we induce an interchange of two columns of the determinant $| f _ { i } ( \pmb { p } _ { j } ) |$ .Its sign therefore changes. Since the functions are continuous,there must be some intermediate position of ${ \pmb p _ { 1 } }$ and ${ \pmb p _ { 2 } }$ for which the value of the determinant is zero.

In order to carry out this argument,it is not necessary to have an interior point.It suffices if the set $\pmb { S }$ contains a “ramification point;” that is to say, a point $\pmb { p }$ at which three arcs meet.Then by a process of“train switching" we may carry out the same argument.It is surprising that unisolvence has this topological aspect.

![](images/30f2974ac4d256836f919bd8c0932cff177349e83a8c57d6b1be990b79bc06e2.jpg)  
Figure 2.4.1.

2.5 Representation Theorems: The Lagrange Formula. Let $z _ { \mathbf { 0 } } ,$ $z _ { 1 } , \ldots , z _ { n }$ be distinct and introduce the following polynomials of degree $\pmb { n }$

$$
l _ { k } ( z ) = { \frac { ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { k - 1 } ) ( z - z _ { k + 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) } { ( z _ { k } - z _ { 0 } ) ( z _ { k } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { n } ) } } ,
$$

It is clear that

$$
l _ { k } ( z _ { j } ) = \delta _ { k j } = { \binom { 0 { \mathrm { ~ i f ~ } } k \neq j } { 1 { \mathrm { ~ i f ~ } } k = j } } .
$$

For given values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ ，the polynomial

$$
p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } w _ { k } l _ { k } ( z )
$$

is in $\mathcal { P } _ { \pmb { n } }$ and takes on these values at the points $z _ { i }$

$$
p _ { n } ( z _ { k } ) = w _ { k } \qquad k = 0 , 1 , \ldots , n .
$$

Formula (2.5.3) is the Lagrange Interpolation Formula. Since the interpolation problem (2.5.4) has a unique solution,all other representations of the solution must, upon rearrangement of terms, coincide with the Lagrange polynomial.

An alternate form is useful.Introduce

$$
w ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) .
$$

Then,

$$
w ^ { \prime } ( z _ { k } ) = ( z _ { k } - z _ { 0 } ) ( z _ { k } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { n } )
$$

and hence from (2.5.1),

$$
l _ { k } ( z ) = \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } .
$$

The formula (2.5.3) becomes

$$
p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } w _ { k } \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } .
$$

The polynomials $l _ { k } ( z )$ are called the fundamental polynomials for pointwise interpolation.

The numbers $w _ { i }$ are frequently the values of some function $f ( z )$ at the points $z _ { i }$ ： $w _ { i } = f ( z _ { i } )$ . The polynomial $\scriptstyle { \pmb { p } } _ { \pmb { n } } ( z )$ given by (2.5.8) and formed with these w's coincides with the function $f ( z )$ at the points $z _ { 0 } , z _ { 1 } , \ldots , z _ { n } .$ That is,if

$$
p _ { n } ( z ) = \sum _ { k = 0 } ^ { n } f ( z _ { k } ) l _ { k } ( z ) = \sum _ { k = 0 } ^ { n } f ( z _ { k } ) { \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } } ,
$$

then

$$
p _ { n } ( z _ { k } ) = f ( z _ { k } ) \qquad k = 0 , 1 , \ldots , n .
$$

DEFINITIon 2.5.1. We shall designate the unique polynomial of class $\mathcal { P } _ { n }$ that coincides with $f$ at $z _ { 0 } , \ldots , z _ { n }$ by $p _ { n } ( f ; z )$

Suppose that $q ( z ) \in \mathcal { P } _ { n }$ .Then $\pmb q$ is uniquely determined by the $n + 1$ values $q ( z _ { i } ) , i = 0 , \ldots , n$ .Hence we must have

$$
p _ { n } ( q ; z ) \equiv q ( z ) .
$$

Now take $q ( z ) = ( z - u ) ^ { j }$ ， $j = 0 , 1 , \ldots , n$ and regard $\textbf { \em u }$ as an independent variable.From (2.5.1l) and (2.5.9),

$$
( z - u ) ^ { j } = \sum _ { k = 0 } ^ { n } ( z _ { k } - u ) ^ { j } l _ { k } ( z ) \qquad j = 0 , 1 , \ldots , n
$$

holding identically in $\textit { \textbf { z } }$ and $\textbf { \em u }$

By selecting $u = z$ we obtain

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 0 } ^ { n } l _ { k } ( z ) \equiv 1 } } \\ { { \sum _ { k = 0 } ^ { n } ( z _ { k } - z ) ^ { j } l _ { k } ( z ) \equiv 0 , j = 1 , 2 , . . . , n . } } \end{array}
$$

The $\pm 1$ identities (2.5.l3) are the Cauchy relations for the fundamental polynomials $l _ { k } ( z )$

The importance of the fundamental polynomials lies in the identity (2.5.2) and the resulting simple explicit solution (2.5.9) of the interpolation problem.If we set

$$
L _ { 0 } ( f ) = f ( z _ { 0 } ) , \ L _ { 1 } ( f ) = f ( z _ { 1 } ) , \ldots , L _ { n } ( f ) = f ( z _ { n } ) ,
$$

then (2.5.2) can be written as

$$
\begin{array} { r } { L _ { i } ( l _ { j } ) = \delta _ { i j } . } \end{array}
$$

In anticipation of certain geometric developments in Chapter VII, we willsay that the polynomials $l _ { i } ( z )$ and the functionals $L _ { i }$ are biorthonormal. For a given set of independent functionals,we can always find a related biorthonormal set of polynomials.Indeed,we have the following generalization of Lagrange's formula.

THEOREM 2.5.1. Let $\pmb { X }$ be $^ { \pmb { a } }$ linear space of dimension $\pmb { n }$ Let $L _ { 1 } , L _ { 2 } , \dots ,$ $L _ { n }$ be $\pmb { n }$ independent functionals in $X ^ { * }$ .Then,there are determined uniquely $\pmb { n }$ independent elements of $X , x _ { 1 } { ^ * } , x _ { 2 } { ^ * } , \dotsb , x _ { n } { ^ * }$ such that

$$
L _ { i } ( x _ { j } { } ^ { * } ) = \delta _ { i j } .
$$

For any ${ \boldsymbol { x } } \in X$ we have

$$
{ \pmb x } = \sum _ { i = 1 } ^ { n } L _ { i } ( { \pmb x } ) x _ { i } ^ { \ast } .
$$

For every choice of $w _ { 1 } , \ldots , w _ { n } $ the element

$$
{ \pmb x } = \sum _ { i = 1 } ^ { n } w _ { i } { x _ { i } } ^ { * }
$$

is the unique solution of the interpolation problem

$$
L _ { i } ( x ) = w _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

Pro0f: Let $x _ { 1 } , \ldots , x _ { n }$ be a basis for $\pmb { X }$ .By Lemma 2.2.1, $| L _ { i } ( x _ { j } ) | \neq 0$ If we set ${ x _ { j } } ^ { * } = a _ { j 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { j n } x _ { n }$ ，then this determinant condition guarantees that the system (2.5.15) can be solved for $\pmb { a } _ { j _ { i } }$ to produce a set of elements ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ .By Theorem 2.2.2,the solution to the interpolation problem (2.5.15) is unique,for each $j$ ，and by Lemma 2.2.1,the ${ \pmb x } _ { i } ^ { * }$ are independent.

Denote $\stackrel { \mathrm { \scriptsize ~ . ~ . ~ } } { y } = \sum _ { i = 1 } ^ { n } { L _ { i } ( x ) { x _ { i } } ^ { * } }$ . Then $L _ { j } ( y ) = \sum _ { i = 1 } ^ { n } L _ { i } ( x ) L _ { j } ( x _ { i } { ^ { * } } )$ . Hence,by (2.5.15), $L _ { j } ( y ) = L _ { j } ( x ) , j = 1 , 2 , . . . , n$ 、Again,since interpolation with the $\pmb { n }$ conditions $L _ { i }$ is unique, $y = x$ and this establishes (2.5.16). Equation (2.5.18) is established similarly.

In this theorem and throughout the remainder of the book an asterisk $( ^ { * } )$ will be applied to the symbol of an element whenever the element is one of a biorthonormal or an orthonormal set. (Cf.Def. 8.3.1.) An asterisk on the symbol of a space will be used to denote the conjugate space. (Cf.Def.1.12.3.)

The solution to the interpolation problem (2.5.lS)can be given in determinantal form.

THEOREM 2.5.2. Let the hypotheses of Theorem 2.5.1 hold and let $\pmb { x } _ { 1 } , \ldots , .$ ${ \pmb x } _ { \pmb n }$ be $^ { \pmb { a } }$ basis for $\pmb { X }$ .If $w _ { 1 } , \ldots , w _ { n }$ are arbitrary numbers then the element

$$
x = - { \frac { 1 } { G } } { \left| \begin{array} { l l l l l } { 0 } & { x _ { 1 } } & { x _ { 2 } } & { \cdots } & { x _ { n } } \\ { w _ { 1 } } & { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) \cdots L _ { 1 } ( x _ { n } ) } \\ { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } \\ { . } & { . } & { . } & { . } \\ { w _ { n } } & { L _ { n } ( x _ { 1 } ) } & { L _ { n } ( x _ { 2 } ) \ldots L _ { n } ( x _ { n } ) } \end{array} \right| }
$$

satisfies $L _ { i } ( x ) = w _ { i } , i = 1 , 2 , \ldots , n .$

Proof:It is clear that $_ { \pmb { x } }$ is a linear combination of $x _ { 1 } , \ldots , x _ { n }$ and hence is in $X$ .Furthermore,we have

$$
\begin{array} { r } { L _ { j } ( x ) = - \frac { 1 } { G } \left| \begin{array} { c c c c } { 0 } & { L _ { j } ( x _ { 1 } ) } & { L _ { j } ( x _ { 2 } ) } & { \cdots \cdot L _ { j } ( x _ { n } ) } \\ { w _ { 1 } } & { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) \cdots L _ { 1 } ( x _ { n } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { w _ { j } } & { L _ { j } ( x _ { 1 } ) } & { L _ { j } ( x _ { 2 } ) } & { \cdots \cdot L _ { j } ( x _ { n } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { w _ { n } } & { L _ { n } ( x _ { 1 } ) } & { L _ { n } ( x _ { 2 } ) \cdots L _ { n } ( x _ { n } ) } \end{array} \right| . } \end{array}
$$

Expand this determinant by minors of the lst column. The minor of each nonzero element,with the exception of $w _ { j }$ ,is O,for it contains two identical rows. The cofactor of $w _ { j }$ is $- G$ Hence, $L _ { j } ( x ) = w _ { j } , j = 1 , 2 , . . . , n .$

Ex.1． (Taylor Interpolation)

The polynomials ${ \frac { z ^ { n } } { n ! } } , n = 0 , 1 , \ldots$ ，and the functionals $L _ { n } ( f ) = f ^ { ( n ) } ( 0 ) , n =$ $0 , 1 , \ldots$ ,are biorthonormal.

![](images/82f1acd77e80c7445a6cd1a4048876ea493678f965acec9286c4173030da73d9.jpg)  
Figure 2.5.1 Osculatory Interpolation at Two Points

$$
p ( x ) = \textstyle { \frac { 3 } { 4 } } - \frac { 1 } { 4 } x ^ { 2 } , \qquad f ( x ) = \frac { 1 } { 1 + x ^ { 2 } }
$$

$$
\begin{array} { r l } { p ( + 1 ) = f ( + 1 ) , \quad } & { { } p ^ { \prime } ( + 1 ) = f ^ { \prime } ( + 1 ) } \\ { p ( - 1 ) = f ( - 1 ) , \quad } & { { } p ^ { \prime } ( - 1 ) = f ^ { \prime } ( - 1 ) . } \end{array}
$$

Ex.2. (Osculatory Interpolation)

$$
w ( z ) = ( z - z _ { 1 } ) ( z - z _ { 2 } ) \cdot \cdot \cdot ( z - z _ { n } ) , l _ { k } ( z ) = \frac { w ( z ) } { ( z - z _ { k } ) w ^ { \prime } ( z _ { k } ) } .
$$

The polynomials $\left[ 1 - \frac { w ^ { \prime \prime } ( z _ { k } ) } { w ^ { \prime } ( z _ { k } ) } ( z - z _ { k } ) \right] { l _ { k } } ^ { 2 } ( z ) , ( z - z _ { k } ) { l _ { k } } ^ { 2 } ( z )$ of degree $2 n \mathrm { ~ - ~ } 1$ and the functionals

$$
L _ { k } ( f ) = f ( z _ { k } ) , M _ { k } ( f ) = f ^ { \prime } ( z _ { k } ) , \qquad k = 1 , 2 , \ldots , n
$$

are biorthonormal.

The resulting expansion of type (2.5.17) is, therefore,

$$
p _ { 2 n - 1 } ( z ) = \sum _ { k = 1 } ^ { n } w _ { k } \left[ 1 - \frac { w ^ { \prime \prime } ( z _ { k } ) } { w ^ { \prime } ( z _ { k } ) } ( z - z _ { k } ) \right] { l _ { k } } ^ { 2 } ( z ) + \sum _ { k = 1 } ^ { n } { w _ { k } } ^ { \prime } ( z - z _ { k } ) { l _ { k } } ^ { 2 } ( z ) ,
$$

and produces the unique element of $\mathscr { P } _ { 2 n - 1 }$ which solves the “osculatory” interpolation problem

$$
\begin{array} { c c } { { p ( z _ { k } ) = w _ { k } } } & { { } } \\ { { { } } } & { { { } } } \\ { { p ^ { \prime } ( z _ { k } ) = w _ { k } { } ^ { \prime } } } & { { { } } } \end{array} \quad k = 1 , 2 , . . . , n .
$$

Ex.3． (Two Point Taylor Interpolation) Let $^ { a }$ and $^ { b }$ be distinct points.The polynomial

$$
\begin{array} { c } { { \displaystyle p _ { 2 n - 1 } ( z ) ~ = ~ ( z ~ - ~ a ) ^ { n } \sum _ { k = 0 } ^ { 1 } \frac { B _ { k } ( z ~ - ~ b ) ^ { k } } { k ! } ~ + ~ ( z ~ - ~ b ) ^ { n } \sum _ { k = 0 } ^ { n - 1 } \frac { A _ { k } ( z ~ - ~ a ) ^ { k } } { k ! } ~ } } \\ { { { } ~ } } \\ { { { \cal A } _ { k } ~ { = } ~ { \displaystyle \frac { d ^ { k } } { d z ^ { k } } } \biggl [ \frac { f ( z ) } { ( z ~ - ~ b ) ^ { n } } \biggr ] _ { z = a } } } \\ { { { } ~ } } \\ { { { \cal B } _ { k } ~ { = } ~ { \displaystyle \frac { d ^ { k } } { d z ^ { k } } } \biggl [ \frac { f ( z ) } { ( z ~ - ~ a ) ^ { n } } \biggr ] _ { z = b } } } \end{array}
$$

is the unique solution in $\mathscr { P } _ { 2 n - 1 }$ of the interpolation problem

$$
\begin{array} { r l } & { p _ { 2 n - 1 } ( a ) = f ( a ) , p _ { 2 n - 1 } ^ { \prime } ( a ) = f ^ { \prime } ( a ) , \ldots , p _ { 2 n - 1 } ^ { ( n - 1 ) } ( a ) = f ^ { ( n - 1 ) } ( a ) \ } \\ & { p _ { 2 n - 1 } ( b ) = f ( b ) , p _ { 2 n - 1 } ^ { \prime } ( b ) = f ^ { \prime } ( b ) , \ldots , p _ { 2 n - 1 } ^ { ( n - 1 ) } ( b ) = f ^ { ( n - 1 ) } ( b ) . } \end{array}
$$

Ex.4． Exs.1,2,3 are,of course,special cases of the general Hermite interpolation problem. (Cf.Ex.6, 2.3.) Let $z _ { 1 } , z _ { 2 } , \ldots , z _ { n }$ be $\pmb { n }$ distinct points, $\alpha _ { 1 } , \ldots , \alpha _ { n }$ be $\pmb { n }$ integers $\geq 1$ and $N = \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { n } - 1$ Set $w ( z ) = \prod _ { i = 1 } ^ { n } ( z - z _ { i } ) ^ { \alpha _ { i } }$ and

$$
l _ { i k } ( z ) \ : = \ : w ( z ) \ : \frac { ( z \ : - \ : z _ { i } ) ^ { k - \alpha _ { i } } } { k ! } \ : \frac { d ^ { ( \alpha _ { i } - k - 1 ) } } { d z ^ { ( \alpha _ { i } - k - 1 ) } } \biggl [ \frac { ( z \ : - \ : z _ { i } ) ^ { \alpha _ { i } } } { w ( z ) } \biggr ] _ { z = z _ { i } } ,
$$

$$
p _ { N } ( z ) = \sum _ { i = 1 } ^ { n } r _ { i } l _ { i { \bf 0 } } ( z ) + \sum _ { i = 1 } ^ { n } r _ { i } \cdot l _ { i { \bf 1 } } ( z ) + \cdot \cdot \cdot + \sum _ { i = 1 } ^ { n } r _ { i } ^ { ( \alpha _ { i } - 1 ) } l _ { i { \alpha _ { i } } - 1 } ( z )
$$

is the unique member of ${ \mathcal P } _ { N }$ for which

$$
\begin{array} { l l } { { p _ { N } ( z _ { 1 } ) = r _ { 1 } , p ^ { \prime } { } _ { N } ( z _ { 1 } ) = r _ { 1 } { } ^ { \prime } , \cdot \cdot \cdot , p _ { N } ^ { ( \alpha _ { 1 } - 1 ) } ( z _ { 1 } ) = r _ { 1 } ^ { ( \alpha _ { 1 } - 1 ) } } } \\ { { . } } \\ { { . } } \\ { { . } } \end{array}
$$

$$
p _ { N } ( z _ { n } ) = r _ { n } , p ^ { \prime } N ( z _ { n } ) = r _ { n } { ' } , . . . , p _ { N } ^ { ( \alpha _ { n } - 1 ) } ( z _ { n } ) = r _ { n } ^ { ( \alpha _ { n } - 1 ) } .
$$

Ex.5.Given the $2 n \mathrm { ~ + ~ } 1$ points

$$
- \pi \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { 2 n } < \pi .
$$

Construct the functions $t _ { j } ( x ) = \prod _ { { k = 0 } \atop { k \ne j } } ^ { 2 n } \sin { \frac { 1 } { 2 } } ( x - x _ { k } ) \left/ \prod _ { { k = 0 } \atop { k \ne j } } ^ { 2 n } \sin { \frac { 1 } { 2 } } ( x _ { j } - x _ { k } ) , \right. \  j = 0 ,$ $1 , \ldots , 2 n$ .If $L _ { j } ( f ) = f ( x _ { j } )$ ,then $t _ { j }$ and $L _ { j }$ are biorthonormal.

Each function $t _ { j } ( x )$ is a linear combination of l, cos $_ { x }$ ....,cos $_ { n x }$ ,sin $x , \ldots$ ， sin nx and hence is an element of $\mathcal { T } _ { \pmb { n } }$

To show this,observe that the numerator of $t _ { j }$ is the product of ${ \bf 2 } n$ factors of the form sin ${ \mathfrak { z } } ( x - x _ { k } ) = \alpha e ^ { i x / 2 } + \beta e ^ { - i x / 2 }$ for appropriate constants $\pmb { \alpha }$ and $\beta$ The product is therefore of the form $\sum _ { \mathrm { ~ : ~ } = \mathrm { ~ - ~ } n } ^ { n } c _ { k } e ^ { i k x }$ ，and is a combination of the required form.The function

$$
T ( x ) = \sum _ { k = 0 } ^ { 2 n } w _ { k } t _ { k } ( x )
$$

is therefore an element of $\mathcal { T } _ { n }$ and is the unique solution of the interpolation problem $T ( x _ { k } ) = w _ { k } , k = 0 , 1 , \ldots , 2 n$ Formula (2.5.28) is known as the Gauss formula of trigonometric interpolation.

Ex.6.Given $\textbf { \em n } + \textbf { 1 }$ distinct points

$$
0 \leq x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < \pi .
$$

$$
C _ { j } ( x ) = \prod _ { { k = 0 } \atop { k \neq j } } ^ { n } ( \cos x - \cos x _ { k } ) \left/ \prod _ { { k = 0 } \atop { k \neq j } } ^ { n } ( \cos x _ { j } - \cos x _ { k } ) \right. .
$$

Then $\boldsymbol { C } _ { j }$ is a cosine polynomial of order $\leq n$ (i.e.,a function of the form $\sum _ { k = 0 } ^ { n } a _ { k } \cos k x )$ for which $C _ { j } ( x _ { k } ) = \delta _ { j k }$ Given $n + 1$ distinct values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ there is a unique cosine polynomial of order $\leq n , C ( x )$ ,for which $C ( x _ { k } ) = w _ { k } , k = 0 ;$ $1 , \ldots , n$ .It is

$$
C ( x ) = \sum _ { k = 0 } ^ { n } w _ { k } C _ { k } ( x ) .
$$

Ex. 7. Given $^ { \pmb { \mathscr { n } } }$ distinct points $0 < x _ { 1 } < \cdot \cdot \cdot < x _ { n } < \pi ,$ Set

$$
\displaystyle { S _ { j } ( x ) = \sin x \prod _ { \stackrel { k = 1 } { k \neq j } } ^ { n } ( \cos x - \cos x _ { k } ) \left/ \prod _ { \stackrel { k = 1 } { k \neq j } } ^ { n } ( \cos x _ { j } - \cos x _ { k } ) \right. } 
$$

Then ${ \pmb S } _ { j } ( { \pmb x } )$ is a sine polynomial of order $\leq n$ for which $S _ { j } ( x _ { k } ) = \delta _ { j k }$ Given $\pmb { n }$ distinct values $w _ { 1 } , w _ { 2 } , \ldots , w _ { n }$ ，there is a unique sine polynomial of order $\leq n , S ( x )$ ,for which $S ( x _ { k } ) = w _ { k }$ and it is

$$
S ( x ) = \sum _ { k = 1 } ^ { n } w _ { k } S _ { k } ( x ) .
$$

Ex.8.Let $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ be $\boldsymbol { n } + \boldsymbol { 1 }$ distinct real (or complex） points. Let $w _ { 0 } , w _ { 1 } , \ldots , w _ { m }$ be a second such set of $m + 1$ points.Set

$$
\begin{array} { r } { P ( z ) = ( z - z _ { 0 } ) \cdot \cdot \cdot ( z - z _ { n } ) , \phantom { . . . } } \\ { Q ( w ) = ( w - w _ { 0 } ) \cdot \cdot \cdot ( w - w _ { m } ) , } \\ { P _ { j } ( z ) = P ( z ) / ( z - z _ { j } ) , \phantom { . . . } } \\ { Q _ { k } ( w ) = Q ( w ) / ( w - w _ { k } ) . \phantom { . . } } \end{array}
$$

The $( m \mathrm { ~ + ~ } 1 ) ( n \mathrm { ~ + ~ } 1 )$ polynomials

$$
l _ { j k } ( z , w ) = \frac { P _ { j } ( z ) Q _ { k } ( w ) } { P _ { j } ( z _ { j } ) Q _ { k } ( w _ { k } ) }
$$

satisfy

$$
l _ { j k } ( z _ { r } , w _ { s } ) = \delta _ { j r } \delta _ { k s } .
$$

Hence

$$
p ( z , w ) = \sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { m } \mu _ { j k } l _ { j k } ( z , w )
$$

is a polynomial of degree $\leq m n$ which satisfies the $( m + 1 ) ( n + 1 )$ interpolation conditions

$$
\begin{array} { l l } { { } } & { { j = 0 , 1 , . . . , n } } \\ { { p ( z _ { j } , w _ { k } ) = \mu _ { j k } } } & { { } } \\ { { } } & { { k = 0 , 1 , . . . , m . } } \end{array}
$$

Formula (2.5.35) may be regarded as the generalization of the Lagrange formula to two dimensions.Extensions to any number of variables willfollow ina similar fashion.It shows that by taking a suffciently large number of powers of several variables polynomial interpolation can be achieved.

2.6 Representation Theorems: The Newton Formula. The Lagrange formula (2.5.3) or (2.5.l7) has one drawback. If we desire to pass from a space of dimension $\pmb { n }$ to a space of one higher dimension,we must determine an entirely new set of elements $y _ { 1 } { ^ { * } } , y _ { 2 } { ^ { * } } , \dots , y _ { n + 1 } { ^ { * } }$ that are not related in a simple fashion to the old set $x _ { 1 } { } ^ { * } , x _ { 2 } { } ^ { * } , \ldots , x _ { n } { } ^ { * }$ .A representation of Newton gets around this diffculty by taking linear combinations of both the basis elements ${ \pmb x _ { 1 } } , { \pmb x _ { 2 } } , \ldots .$ ，and the prescribed functionalg $L _ { 1 } , L _ { 2 } , \dotsb .$ We shall first study this representation in the case of polynomial interpolation.

Let $z _ { 0 } , \ldots , z _ { n }$ be $n + 1$ distinct points and form the $n + 1$ independent Newton polynomials

$$
1 , \ z - z _ { 0 } , \ ( z - z _ { 0 } ) ( z - z _ { 1 } ) , \ \ldots , ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } ) .
$$

For given values $w _ { 0 } , w _ { 1 } , \ldots , w _ { n }$ there is a unique member of $\mathcal { P } _ { n }$ for which $p ( z _ { i } ) = w _ { i } , i = 0 , 1 , . ~ . ~ . ~ , n$ .Let us see if we can represent it in the form

$$
\begin{array} { c } { p ( z ) = a _ { 0 } + a _ { 1 } ( z - z _ { 0 } ) + a _ { 2 } ( z - z _ { 0 } ) ( z - z _ { 1 } ) + \cdots } \\ { + a _ { n } ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n - 1 } ) . } \end{array}
$$

To determine the constants ${ \pmb a } _ { i }$ set $z = z _ { 0 } , \ z = z _ { 1 } , \ . \ . \ .$ ， successively， and solve the resulting linear equations:

$$
\begin{array} { r l } & { a _ { 0 } = w _ { 0 } } \\ & { a _ { 1 } = \displaystyle \frac { w _ { 1 } - w _ { 0 } } { z _ { 1 } - z _ { 0 } } } \\ & { a _ { 2 } = \displaystyle \frac { 1 } { z _ { 2 } - z _ { 1 } } \Big ( \displaystyle \frac { w _ { 2 } - w _ { 0 } } { z _ { 2 } - z _ { 0 } } - \displaystyle \frac { w _ { 1 } - w _ { 0 } } { z _ { 1 } - z _ { 0 } } \Big ) . } \\ & { . } \\ & { . } \end{array}
$$

Note that for a fixed set of points $z _ { 0 } , \ldots , z _ { n }$ ，each $\pmb { a } _ { i }$ is a certain linear combination of the ${ \boldsymbol { w } } _ { i }$ ,and that,furthermore, ${ \pmb { a } } _ { \mathbf { 0 } }$ involves only ${ \pmb w } _ { \mathbf 0 }$ and ${ z _ { 0 } } ; { a _ { 1 } }$ involves only $w _ { 0 } , w _ { 1 } , z _ { 0 } , z _ { 1 } ; a _ { 2 }$ involves only $w _ { 0 } , w _ { 1 } , w _ { 2 } , z _ { 0 } , z _ { 1 } , z _ { 2 }$ etc.

DEFINITION 2.6.1. The constant $\pmb { a _ { j } }$ is called the divided difference of the jth order of $w _ { 0 } , w _ { 1 } , \dotsc , w _ { j }$ with respect to $z _ { 0 } , z _ { 1 } , \dots , z _ { j } . \ i$ $\mathit { \Pi } _ { I t }$ is designated by

$$
a _ { j } = [ w _ { 0 } , w _ { 1 } , \ldots , w _ { j } ] .
$$

A compact formula for ${ \pmb a } _ { j }$ can be found by comparing (2.6.l) with the Lagrange formula (2.5.8) with which it must coincide.The coefficient of $z ^ { n }$ in (2.6.1) is fore, ${ \pmb a } _ { \pmb n }$ . The coefficient of $z ^ { n }$ in (2.5.8) is seen to be $\sum _ { k = 0 } ^ { n } { \frac { w _ { k } } { w ^ { \prime } ( z _ { k } ) } }$ . There-

$$
a _ { n } = [ w _ { 0 } , w _ { 1 } , \ldots , w _ { n } ] = \sum _ { k = 0 } ^ { n } \frac { w _ { k } } { w ^ { \prime } ( z _ { k } ) }
$$

where $w ( z ) = w _ { n } ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } ) .$ Thus, again, from (2.6.4),

$$
\begin{array} { l } { \displaystyle a _ { 1 } = \frac { w _ { 0 } } { z _ { 0 } - z _ { 1 } } + \frac { w _ { 1 } } { z _ { 1 } - z _ { 0 } } } \\ { \displaystyle a _ { 2 } = \frac { w _ { 0 } } { ( z _ { 0 } - z _ { 1 } ) ( z _ { 0 } - z _ { 2 } ) } + \frac { w _ { 1 } } { ( z _ { 1 } - z _ { 0 } ) ( z _ { 1 } - z _ { 2 } ) } + \frac { w _ { 2 } } { ( z _ { 2 } - z _ { 0 } ) ( z _ { 2 } - z _ { 1 } ) } } \end{array}
$$

If the $w _ { i }$ are taken as the value of a function $f$ at $z _ { i } \colon f ( z _ { i } ) = w _ { i } ,$ ，then we may combine (2.6.l) and (2.6.3) to obtain

$$
p _ { n } ( f ; z ) = \sum _ { k = 0 } ^ { n } [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , \ldots , f ( z _ { k } ) ] ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { k - 1 } ) .
$$

$$
{ \pmb w } _ { - { \bf 1 } } ( { \pmb z } ) \equiv { \bf 1 } .
$$

This form of the interpolating polynomial is the fnite Newton series for a function $f ( z )$

With $z _ { 0 } , z _ { 1 } , \ldots , z _ { n }$ fixed, introduce the linear functionals

$$
L _ { 0 } ( f ) = f ( z _ { 0 } )
$$

$$
\begin{array} { c } { { L _ { 1 } ( f ) = \displaystyle { \frac { f ( z _ { 0 } ) } { z _ { 0 } - z _ { 1 } } } + \displaystyle { \frac { f ( z _ { 1 } ) } { z _ { 1 } - z _ { 0 } } } } } \\ { { . } } \\ { { . } } \\ { { . } } \end{array}
$$

according to the scheme in (2.6.5). Then (2.6.6) becomes

$$
p _ { n } ( f ; z ) = \sum _ { k = 0 } ^ { n } L _ { k } ( f ) w _ { k - 1 } ( z ) .
$$

Since $w _ { j } ( z ) \in \mathcal { P } _ { n }$ if $0 \leq j \leq n - 1$ it follows that $w _ { j } ( z ) = p _ { n } ( w _ { j } ( z ) ; z )$ and hence

$$
w _ { j } ( z ) \equiv \sum _ { k = 0 } ^ { n } L _ { k } ( w _ { j } ( z ) ) w _ { k - 1 } ( z )
$$

By setting $j = 0 , 1 , 2 , \ldots ,$ in (2.6.9) successively we obtain

$$
L _ { k } ( w _ { j - 1 } ( z ) ) = \delta _ { k j } .
$$

Comparing the biorthogonality relationships (2.6.l0) and (2.5.l4) our introductory remarks become clear.Whereas $w _ { \boldsymbol { k } } ( z )$ depends only on the points $z _ { 0 } , \dotsc , z _ { k } , l _ { k } ( z ) = l _ { k , n } ( z )$ depends upon all the points $z _ { 0 } , \ldots , z _ { k } , \ldots , z _ { n }$ In the Lagrange representation，we add an additional point and increase the degree of the interpolating polynomial at the cost of changing all the fundamental polynomials.In the Newton representation,this can be accomplished by adding one more term. The Newton representation has a permanence property,and this is characteristic of Fourier series and other orthogonal and biorthogonal expansions.(See 8.5.) The price that is paid for the convenience of the permanence property is that the multipliers of the individual polynomials are no longer simple values at a point,but certain linear combinations of these values.

This type of biorthonormality and permanence can be obtained in a general setting.

THEOREM 2.6.1 (Biorthonormality Theorem or Generalized Newton Representation). Let $X$ be a linear space of infinite dimension. Let $x _ { 1 }$ ， $\pmb { x _ { 2 } } .$ be a sequence of elements of $X$ such that for each $n , x _ { 1 } , \ldots , x _ { n }$ are independent, Suppose,further,that $L _ { 1 } , L _ { 2 } , \ldots$ ，is $^ { a }$ sequence of linear functionals in $X ^ { * }$ such that for each $\pmb { n }$ the $\textit { \textbf { n } } \times \textit { \textbf { n } }$ determinant

$$
\vert L _ { i } ( x _ { j } ) \vert _ { i , j = 1 } ^ { n } \neq 0 .
$$

Then there is determined uniquely two triangular systems of constants $\pmb { a } _ { i j }$ $\boldsymbol { b } _ { i j }$ with $\pmb { a } _ { i i } \neq 0$ such that if

$$
\begin{array} { l l } { { { { L } _ { 1 } } ^ { * } = a _ { 1 1 } { L } _ { 1 } } } & { { { { x } _ { 1 } } ^ { * } = x _ { 1 } } } \\ { { { { L } _ { 2 } } ^ { * } = a _ { 2 1 } { L } _ { 1 } + a _ { 2 2 } { L } _ { 2 } } } & { { { { x } _ { 2 } } ^ { * } = b _ { 2 1 } { x } _ { 1 } + x _ { 2 } } } \\ { { { { L } _ { 3 } } ^ { * } = a _ { 3 1 } { L } _ { 1 } + a _ { 3 2 } { L } _ { 2 } + a _ { 3 3 } { L } _ { 3 } } } & { { { { x } _ { 3 } } ^ { * } = b _ { 3 1 } { x } _ { 1 } + b _ { 3 2 } { x } _ { 2 } + x _ { 3 } } } \\ { . } & { . } \\ { . } & { . } \\ { . } \end{array}
$$

we have

$$
{ L _ { i } } ^ { * } ( { x _ { j } } ^ { * } ) = { \delta } _ { i j } , ~ i , j = 1 , 2 , \cdots .
$$

Pro0f: We want $L _ { 1 } { } ^ { * } ( x _ { 1 } { } ^ { * } ) = 1$ . Therefore, $a _ { 1 1 } L _ { 1 } ( x _ { 1 } ) = 1$ or

$$
a _ { 1 1 } = ( L _ { 1 } ( x _ { 1 } ) ) ^ { - 1 } \neq 0 .
$$

The denominator does not vanish by (2.6.ll). We shall now carry out an inductive proof.Assume that we have already determined

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c } { a _ { 1 1 } } & & & & & & & & & & & & & & & & & & & & & & & & & & & & & \\ { a _ { 2 1 } } & { a _ { 2 2 } } & & & & & & { b _ { 2 1 } } & { 1 } & & & & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & { \cdot } & { \cdot } & & & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & { \cdot } & { \cdot } & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & { \cdot } & { \cdot } & & & & & & & & & \\ { \cdot } & { \cdot } & & & & & & { \cdot } & { \cdot } & & & & & & & & & \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdot \cdot \cdot \cdot } & { a _ { n n } } & & & & & { b _ { n 1 } } & { b _ { n 2 } } & { \cdot \cdot \cdot } & { b _ { n , n - 1 } } & { 1 } & & & & \end{array}
$$

with $a _ { 1 1 } a _ { 2 2 } \cdots a _ { n n } \neq 0$ and such that

$$
{ L _ { i } } ^ { * } ( x _ { j } { * } ) = { \delta } _ { i j } , ~ i , j = 1 , 2 , . ~ . ~ . ~ , n .
$$

We will show that we can obtain first $b _ { n + 1 , 1 } , b _ { n + 1 , 2 } , \dotsc , b _ { n + 1 , n } , 1$ and from a knowledge of these values can then obtain ${ \pmb { a } } _ { n + 1 , 1 }$ ， $a _ { n + 1 , 2 } , \ldots , a _ { n + 1 , n + 1 }$ with $a _ { n + 1 , n + 1 } \neq 0$ and such that

$$
{ L _ { i } } ^ { * } ( x _ { j } { } ^ { * } ) = \delta _ { i j } , \qquad i , j = 1 , 2 , \ldots , n + 1 .
$$

The conditions included in (2.6.l5) that are not already contained in (2.6.14) are

$$
\begin{array} { r l } { L _ { i } { * ( x _ { n + 1 } ^ { * } ) } = 0 } & { i = 1 , 2 , \ldots , n \quad \mathrm { a n d } } \\ { L _ { n + 1 } ^ { * } ( x _ { i } { * } ) = 0 } & { i = 1 , 2 , \ldots , n , } \\ { L _ { n + 1 } ^ { * } ( x _ { n + 1 } ^ { * } ) = 1 . } \end{array}
$$

The first $\pmb { n }$ equations in (2.6.l6) yield the system

$$
b _ { n + 1 , 1 } L _ { 1 } { } ^ { * } ( x _ { 1 } ) + b _ { n + 1 , 2 } L _ { 1 } { } ^ { * } ( x _ { 2 } ) + \cdot \cdot \cdot + b _ { n + 1 , n } L _ { 1 } { } ^ { * } ( x _ { n } ) = - L _ { 1 } { } ^ { * } ( x _ { n + 1 } )
$$

$$
b _ { n + 1 , 1 } L _ { n } { } ^ { * } ( x _ { 1 } ) + b _ { n + 1 , 2 } L _ { n } { } ^ { * } ( x _ { 2 } ) + \cdot \cdot \cdot + b _ { n + 1 , n } L _ { n } { } ^ { * } ( x _ { n } ) = - L _ { n } { } ^ { * } ( x _ { n + 1 } ) .
$$

This system has a unique solution providing $\vert { L } _ { i } { ^ { * } ( x _ { j } ) } \vert _ { i , j = 1 } ^ { n } \neq 0$ . But from Problem 19,Chapter II,

$$
| L _ { i } { ^ * } ( x _ { j } ) | = \left| { \begin{array} { l l l l } { a _ { 1 1 } } & { 0 } & { \cdots } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { 0 } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} } \right| \cdot | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n }
$$

$$
= a _ { 1 1 } a _ { 2 2 } \cdot \cdot \cdot a _ { n n } | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n } \neq 0 .
$$

Having determined the b's, or equivalently ${ \boldsymbol x } _ { n + 1 } ^ { * }$ , consider the second group of $\pm 1$ equations in (2.6.16). This yields

$$
\begin{array} { l } { { a _ { n + 1 , 1 } L _ { 1 } ( x _ { 1 } { * } ) + \dots + a _ { n + 1 , n + 1 } L _ { n + 1 } ( x _ { 1 } { * } ) = 0 } } \\ { { \mathrm { . } } } \\ { { \mathrm { . } } } \end{array}
$$

$$
\begin{array} { r } { a _ { n + 1 , 1 } L _ { 1 } ( x _ { n } { } ^ { * } ) + \cdots + a _ { n + 1 , n + 1 } L _ { n + 1 } ( x _ { n } { } ^ { * } ) = 0 } \\ { a _ { n + 1 , 1 } L _ { 1 } ( x _ { n + 1 } ^ { * } ) + \cdots + a _ { n + 1 , n + 1 } L _ { n + 1 } ( x _ { n + 1 } ^ { * } ) = 1 } \end{array}
$$

This system has a unique solution providing that

$$
| L _ { i } ( { x _ { j } } ^ { * } ) | _ { i , j = 1 } ^ { n + 1 } \neq 0 .
$$

But,again by Problem 19,

$$
| L _ { i } ( x _ { j } ^ { * } ) | _ { i , j = 1 } ^ { n + 1 } = \left| \begin{array} { l l l l } { 1 } & { 0 } & { \cdots } & { 0 } \\ { b _ { 2 1 } } & { 1 } & { \cdots } & { 0 } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { b _ { n + 1 , 1 } } & { b _ { n + 2 , 1 } } & { \cdots } & { 1 } \end{array} \right| \cdot | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n + 1 }
$$

$$
= | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n + 1 } \neq 0 .
$$

Furthermore, $a _ { n + 1 , n + 1 } = a _ { 1 1 } a _ { 2 2 } \cdot \cdot \cdot a _ { n n } | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n } / | L _ { i } ( x _ { j } ) | _ { i , j = 1 } ^ { n + 1 } \neq 0 .$ We observe finally that at no stage is there any arbitrariness in our determination of the constants and hence the solution is unique.

COROLLARY 2.6.2. Let $X _ { n }$ designate the subspace of $\pmb { X }$ spanned by $x _ { 1 } , \ldots ,$ $x _ { n }$ (i.e., the set of all linear combinations $a _ { 1 } x _ { 1 } + \cdots + a _ { n } x _ { n } )$ .If $x \in X _ { n }$ then

$$
\begin{array} { c } { { \displaystyle x = \sum _ { k = 1 } ^ { n } L _ { k } { } ^ { * } ( x ) x _ { k } { } ^ { * } . } } \\ { { \displaystyle = \sum _ { k = 1 } ^ { n } { L _ { k } { } ^ { * } ( x ) x _ { k } { } ^ { * } \mathrm { ~ t h e n ~ } L _ { j } { } ^ { * } ( y ) } = \sum _ { k = 1 } ^ { n } { L _ { k } { } ^ { * } ( x ) L _ { j } { } ^ { * } ( x _ { k } { } ^ { * } ) } = L _ { j } { } ^ { * } ( x ) } } \end{array}
$$

Proof: If by (2.6.13). Since $x _ { 1 } , \ldots , x _ { n }$ are independent,it follows from (2.6.l2） that ${ x _ { 1 } } ^ { * } , \ldots , { x _ { n } } ^ { * }$ are independent.Hence from (2.6.l3) and Lemma 2.2.l it follows that $L _ { 1 } , \ldots , L _ { n }$ and consequently $L _ { 1 } { } ^ { * } , \ldots , L _ { n } { } ^ { * }$ are independent. In view of this, $L _ { j } { * } ( y - x ) = 0 , j = 1 , 2 , \ldots , n$ implies $y = x$

For a given $x \in X$ ,the formal series

$$
x \sim \sum _ { k = 1 } ^ { \infty } L _ { k } { * ( x ) } { x _ { k } } ^ { * }
$$

is a biorthogonal expansion of the element $_ x$ .In particular cases,the relation of the series to $_ { x }$ has been the object of vast investigations.

It will help to grasp the difference between the biorthonormality of Lagrange type (2.5.l5) and that of Newton type (2.6.15) if each is expressed in the language of matrices.Let $G$ designate the matrix $( L _ { i } ( x _ { j } ) )$ . Let $\pmb { A }$ designate the matrix $( a _ { i j } )$ where the $\boldsymbol { a } _ { i j }$ are the quantities appearing in the proof of Theorem 2.5.1. $\boldsymbol { \mathit { I } }$ is the unit matrix. Then,(2.5.l5) may be expressed as

$$
G A ^ { \prime } = I , ~ A ^ { \prime } = \mathrm { t r a n s p o s e ~ o f } ~ A .
$$

On the other hand,if $\pmb { A }$ and $\pmb { B }$ designate the lower triangular matrices taken from the coefficient scheme of (2.6.l2) then

$$
A G B ^ { \prime } = I .
$$

Note that (2.6.19) is equivalent to

$$
\begin{array} { r } { G = A ^ { - 1 } ( B ^ { \prime } ) ^ { - 1 } . } \end{array}
$$

Now, $A ^ { - 1 }$ is a lower triangular matrix with non-zero elements on its·principal diagonal and $( B ^ { \prime } ) ^ { - 1 }$ is an upper triangular matrix with l's on its principal diagonal.(2.6.20) has a matrix formulation.A matrix ${ \cal { G } } = ( g _ { i j } )$ is said to be regularly arranged if none of its principal minors $\left( \mathrm { i . e . , } g _ { 1 1 } , \begin{array} { l } { { \left| \begin{array} { l l } { { g _ { 1 1 } } } & { { g _ { 1 2 } } } \\ { { g _ { 2 1 } } } & { { g _ { 2 2 } } } \end{array} \right| , . . . . } } \end{array} \right)$ vanishes. If $G$ is regularly arranged,then it can be expressed as the product of a lower triangular matrix by an upper triangular matrix with l's on its principal diagonal. This is known as an $_ { L U }$ -decomposition of $G$

The result of biorthogonalization can be expressed by means of determinants.

THEOREM 2.6.3. With the notation of the previous theorem,let

$$
G _ { r } = \vert L _ { \imath } ( x _ { j } ) \vert _ { i , j = 1 } ^ { r } .
$$

Then,

$$
x _ { j } \ast = { \frac { 1 } { G _ { j - 1 } } } { \left| \begin{array} { l l l l } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) } & { \cdots } & { L _ { 1 } ( x _ { j } ) } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { L _ { j - 1 } ( x _ { 1 } ) } & { L _ { j - 1 } ( x _ { 2 } ) } & { \cdots } & { L _ { j - 1 } ( x _ { j } ) } \\ { \quad x _ { 1 } } & { x _ { 2 } } & { \cdot \cdot \cdot } & { x _ { j } } \end{array} \right| }
$$

$$
L _ { j } * = \frac { 1 } { G _ { j } } \left| \begin{array} { c c c c c } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 2 } ( x _ { 1 } ) } & { \cdots } & { L _ { j } ( x _ { 1 } ) } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { L _ { 1 } ( x _ { j - 1 } ) } & { L _ { 2 } ( x _ { j - 1 } ) } & { \cdots } & { L _ { j } ( x _ { j - 1 } ) } \\ { L _ { 1 } } & { L _ { 2 } } & { \cdot \cdot } & { L _ { j } } \end{array} \right| .
$$

Proof:Expand these determinants according to the minors of the last row. We see that ${ x _ { j } } ^ { * }$ is a linear combination of $x _ { 1 } , x _ { 2 } , \dotsc , x _ { j }$ and $\boldsymbol { L _ { j } } ^ { * }$ is a linear combination of $L _ { 1 } , L _ { 2 } , \ldots , L _ { j }$ .Moreover the coefficient of $\boldsymbol { x } _ { j }$ in ${ x _ { j } } ^ { * }$ is 1. Fix a $j > 1$ .We shall show that ${ \cal L } _ { i } { } ^ { * } ( x _ { j } { } ^ { * } ) = 0$ for $i < j$ It suffices to show that $L _ { i } ( x _ { j } ^ { * } ) = 0$ for $i < j$ But

$$
L _ { i } ( x _ { j } * ) = { \frac { 1 } { G _ { j - 1 } } } { \left| \begin{array} { l l l l } { L _ { 1 } ( x _ { 1 } ) } & { L _ { 1 } ( x _ { 2 } ) } & { \cdot \cdot } & { L _ { 1 } ( x _ { j } ) } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } \\ { L _ { j - 1 } ( x _ { 1 } ) } & { L _ { j - 1 } ( x _ { 2 } ) } & { \cdot \cdot } & { L _ { j - 1 } ( x _ { j } ) } \\ { L _ { i } ( x _ { 1 } ) } & { L _ { i } ( x _ { 2 } ) } & { \cdot \cdot } & { L _ { i } ( x _ { j } ) } \end{array} \right| } = 0
$$

inasmuch as two rows are identical. Similarly,we can show that for fixed $i > 1$ ， ${ \cal L } _ { i } { } ^ { * } ( x _ { j } { } ^ { * } ) = 0$ for $j < i$ .It remains to show that ${ \cal L } _ { i } { } ^ { * } ( x _ { i } { } ^ { * } ) = 1$ Since $x _ { i } { ^ * } = b _ { i 1 } x _ { 1 } + b _ { i 2 } x _ { 2 } + \cdot \cdot \cdot + b _ { i , i - 1 } x _ { i - 1 } + x _ { i }$ it suffices to show that $L _ { i } { * ( x _ { i } ) } =$ 1.Now,from the second equation of (2.6.21), ${ L _ { i } } ^ { * } ( x _ { i } ) = { G _ { i } } / { G _ { i } } = 1$ The above biorthogonal representation is unique and the theorem follows.

We now give some examples of biorthogonal systems of the Newton type.

Ex.1． (Newton Polynomials). $x$ is the space of all polynomials in $\pmb { z }$ ，

$$
x _ { 1 } = 1 , x _ { 2 } = z , x _ { 3 } = z ^ { 2 } , \ldots , L _ { 1 } ( f ) = f ( z _ { 0 } ) , L _ { 2 } ( f ) = f ( z _ { 1 } ) , \ldots ,
$$

where ${ \pmb z } _ { i }$ are distinct points.Then,

$$
G _ { r } = \left| \begin{array} { c c c c c c } { 1 } & { z _ { 0 } } & { z _ { 0 } ^ { 2 } } & { \cdots } & { z _ { 0 } ^ { r - 1 } } \\ { \vdots } & { z _ { 1 } } & { z _ { 1 } ^ { 2 } } & { \ddots } & { z _ { 1 } ^ { r - 1 } } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { 1 } & { z _ { r - 1 } } & { z _ { r - 1 } ^ { 2 } } & { \cdot \cdot } & { z _ { r - 1 } ^ { r - 1 } } \end{array} \right| = \prod _ { i > j } ^ { r - 1 } ( z _ { i } - z _ { j } )
$$

$$
x _ { j } \sp * = { \frac { 1 } { G _ { j - 1 } } } \left| \begin{array} { c c c c c c } { { 1 } } & { { z _ { 0 } } } & { { z _ { 0 } \sp 2 } } & { { \cdots } } & { { z _ { 0 } \sp { j - 1 } } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { \cdot } } \\ { { 1 } } & { { z _ { j - 2 } } } & { { z _ { j - 2 } ^ { 2 } } } & { { \cdot \cdot \cdot } } & { { z _ { j - 2 } ^ { j - 1 } } } \\ { { 1 } } & { { z } } & { { z \sp 2 } } & { { \cdot \cdot \cdot } } & { { z ^ { j - 1 } } } \end{array} \right|
$$

This is a polynomial $q ( z )$ of degree $j - 1$ in $\pmb { z }$ .Now $q ( z _ { 0 } ) = q ( z _ { 1 } ) = \cdot \cdot \cdot = q ( z _ { j - 2 } ) = 0$ inasmuch as two rows are identical. Hence $x _ { j } { * } \ : = \ : ( z \ : - \ : z _ { 0 } ) ( z \ : - \ : z _ { 1 } ) \ : \cdot \ : \cdot ( z \ : - \ : z _ { j - 1 } )$ ， Corresponding to $\boldsymbol { L _ { j } } ^ { * }$ we have the divided differences of $f$ at the points $z _ { 0 } , z _ { 1 } , \dots z _ { \mathrm { ~ \tiny ~ ( ~ \cdot ~ ) ~ } }$ Formula (2.6.21) yields the representation

$$
\pmb { a _ { n } } = [ f ( z _ { 0 } ) , f ( z _ { 1 } ) , . . . , f ( z _ { n } ) ]
$$

$$
\begin{array} { r l } & { \mathbf { \Phi } _ { , J } : \langle \mathbf { \Phi } _ { 1 } | \boldsymbol { \cdot } , \boldsymbol { \cdot } , \boldsymbol { \cdot } , \boldsymbol { \cdot } , \boldsymbol { } , \boldsymbol { \cdot } , \boldsymbol { } , \boldsymbol { \cdot } , \boldsymbol { } \rangle } \\ & { = \left| \begin{array} { l l l l } { \mathbf { \Phi } _ { 1 } } & { \mathbf { \Phi } _ { 1 } } & { \dots } & { \mathbf { \Phi } _ { 1 } } \\ { \mathbf { \Phi } _ { z _ { 0 } } } & { \mathbf { \Phi } _ { z _ { 1 } } } & { \dots } & { \mathbf { \Phi } _ { z _ { n } } } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { z _ { 0 } ^ { n - 1 } } & { z _ { 1 } ^ { n - 1 } } & { \dots } & { z _ { n } ^ { n - 1 } } \\ { \mathbf { \Phi } _ { 2 } ^ { n } } & { \mathbf { \Phi } _ { 2 } ^ { n } } & { \dots } & { \mathbf { \Phi } _ { \tilde { n } } } \end{array} \right| \left| \begin{array} { l l l l l } { \mathbf { \Phi } _ { 1 } } & { \mathbf { \Phi } _ { 1 } } & { \dots } & { \mathbf { \Phi } _ { 1 } } \\ { \mathbf { \Phi } _ { z _ { 0 } } } & { \mathbf { \Phi } _ { z _ { 1 } } } & { \dots } & { \mathbf { \Phi } _ { z _ { n } } } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & { \cdot } \\ { z _ { 0 } ^ { n - 1 } } & { z _ { 1 } ^ { n - 1 } } & { \dots } & { z _ { n } ^ { n - 1 } } \\ { \mathbf { \Phi } _ { 2 } ^ { n } } & { \mathbf { \Phi } _ { z _ { 1 } } ^ { n } } & { \dots } & { z _ { n } ^ { n } } \end{array} \right| } \end{array}
$$

for divided differences.

Ex.2 (Abel-Gontscharoff Polynomials)． These polynomials, $Q _ { n } ( z )$ ,arise from biorthogonalizing the powers $1 , z , z ^ { 2 } , \ldots$ ，against the functionals $\pmb { L _ { 0 } } ( f ) =$ $f ( z _ { 0 } ) , L _ { 1 } ( f ) = f ^ { \prime } ( z _ { 1 } ) , L _ { 2 } ( f ) = f ^ { \prime } ( z _ { 2 } ) ,$ .... We have

$$
\scriptstyle G _ { \tau } = { \left| \begin{array} { l l l l l l } { 1 } & { z _ { 0 } } & { z _ { 0 } ^ { 0 } } & { \cdots } & & { z _ { 0 } ^ { \tau - 1 } } \\ { 0 } & { 1 } & { 2 z _ { 1 } } & { \cdots } & & { ( r - 1 ) z _ { 1 } ^ { \tau - 2 } } \\ { 0 } & { 0 } & { 2 } & { \cdots } & { ( r - 1 ) ( r - 2 ) z _ { 2 } ^ { \tau - 3 } } \\ { \cdot } & { \cdot } & & & { \cdot } \\ { \cdot } & { \cdot } & & & { \cdot } \\ { \cdot } & { \cdot } & & & { \cdot } \\ { 0 } & { 0 } & { \cdots } & { \cdot } & & { ( r - 1 ) ! } \end{array} \right| } = 1 ! \ 2 ! \ 3 ! \ \cdot \ \cdot \ \cdot ( r - 1 ) !
$$

$$
L _ { n } \mathbf { * } ( f ) = \frac { 1 } { G _ { n + 1 } } \left| \begin{array} { l l l l l l } { ~ 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { z _ { 0 } } & { ~ 1 } & { 0 } & { 0 } & { 0 } \\ { z _ { 0 } ^ { 2 } } & { ~ 2 z _ { 1 } } & { ~ 2 } & { ~ 0 } \\ { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } \\ { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } \\ { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } & { ~ \cdot } \\ { z _ { 0 } ^ { n - 1 } } & { ( n - 1 ) z _ { 1 } ^ { n - 2 } } & { ~ ( n - 1 ) ! } & { ~ 0 } \\ { ~ f ( z _ { 0 } ) } & { ~ f ^ { \prime } ( z _ { 1 } ) } & { ~ f ^ { ( n - 1 ) } ( z _ { n - 1 } ) } & { f ^ { ( n ) } ( z _ { n } ) } \end{array} \right| = \frac { f ^ { ( n ) } ( z _ { n } ) } { n ! }
$$

$$
\begin{array} { r } { Q _ { n } ( z ) \ = \frac { 1 } { G _ { n } } \left| \begin{array} { l l l l l l } { 1 } & { z _ { 0 } } & { z _ { 0 } ^ { 2 } } & { \cdots } & { z _ { 0 } ^ { n } } \\ { 0 } & { 1 } & { 2 z _ { 1 } } & { \cdots } & { n z _ { 1 } ^ { n - 1 } } \\ { 0 } & { 0 } & { 2 } & { \cdots } & { n ( n - 1 ) z _ { 2 } ^ { n - 2 } } \\ { \cdot } & { \cdot } & { \cdot } & & { \cdot } \\ { \cdot } & { \cdot } & { \cdot } & & & { \cdot } \\ { 1 } & { \cdot } & { \cdot } & & & { \cdot } \\ { 1 } & { z } & { z ^ { 2 } } & { \cdots } & { z ^ { n } } & \end{array} \right| } \end{array}
$$

Thus,in particular,we have

$$
\begin{array} { r l } & { Q _ { \bf 0 } ( z ) = 1 } \\ & { Q _ { \bf 1 } ( z ) = z - z _ { 0 } } \\ & { Q _ { \bf 2 } ( z ) = z ^ { 2 } - 2 z _ { 1 } z + z _ { 0 } ( 2 z _ { 1 } - z _ { 0 } ) . } \\ & { . } \\ & { . } \\ & { . } \end{array}
$$

The polynomials $Q _ { n } ( z )$ are the Abel-Gontscharoff polynomials. A more tractable representation can be found for $Q _ { n } ( z )$ in terms of iterated integration. Consider the $\pmb { n }$ -fold iterated integral

$$
T _ { n } ( z ) \ = n ! \int _ { z _ { 0 } } ^ { z } d z ^ { \prime } \int _ { z _ { 1 } } ^ { z ^ { \prime } } d z ^ { \prime \prime } \int _ { z _ { 2 } } ^ { z ^ { \prime } } d z ^ { \prime \prime \prime } \ \cdot \cdot \cdot \int _ { z _ { n - 1 } } ^ { z ^ { ( n - 1 ) } } d z ^ { ( n ) } , n \geq 1 .
$$

It is clear that $\scriptstyle { \pmb { T } } _ { \pmb { n } }$ is a polynomial of degree $\pmb { n }$ with leading coefficient 1.Furthermore, $T _ { n } ( z _ { 0 } ) = 0$ ,and by successive differentiation,

$$
\begin{array} { l } { { T _ { n } ^ { \prime } ( z _ { 1 } ) = 0 , \dots , \frac { T _ { n } ^ { ( n ) } ( z _ { n } ) } { n ! } = 1 , } } \\ { { \frac { T _ { n } ^ { ( r ) } ( z _ { r } ) } { r ! } = 0 \quad \mathrm { f o r } \quad r > n . } } \end{array}
$$

Thus,the biorthogonalityconditions hold for $\scriptstyle { T _ { n } }$ , and hence $T _ { n } \equiv Q _ { n }$

Ex.3 (Bernoulli Polynomials)．Let $\pmb { f } ( \pmb { z } )$ be analytic at ${ \boldsymbol { z } } = \mathbf { 0 }$ and assume that $f ( 0 ) \neq 0$ .ByLeibnitz'rule

$$
{ \frac { d ^ { n } } { d z ^ { n } } } \left( f ( z ) e ^ { s z } \right) = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } s ^ { k } e ^ { s z } f ^ { ( n - k ) } ( z ) .
$$

Hence,

$$
{ \frac { d ^ { n } } { d z ^ { n } } } \left( f \left( z \right) e ^ { s z } \right) \left| _ { z = 0 } = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } s ^ { k } f ^ { ( n - k ) } ( 0 ) \right.
$$

is a polynomial of degree $_ n$ in $\pmb { \mathscr { s } }$ In particular, select $f ( z ) = { \frac { z } { e ^ { z } - 1 } }$ 1，a function that is analytic in $| z | < 2 \pi$ and $f ( 0 ) \neq 0$ .Hence,we may write

$$
\frac { z e ^ { s z } } { e ^ { z } - 1 } = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \left( \frac { z e ^ { s z } } { e ^ { z } - 1 } \right) _ { 0 } ^ { ( n ) } z ^ { n } = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } B _ { n } ( s ) z ^ { n }
$$

for certain polynomials $B _ { n } ( s )$ of degree $_ n$ .(2.6.31) is valid for $| z | < 2 \pi$ and can be shown to hold uniformly in $\pmb { \mathscr { s } }$ and $\pmb { z }$ provided $\pmb { \mathscr { s } }$ is confined to a closed bounded region and $_ z$ to a closed subset of $| z | < 2 \pi$ The polynomials $B _ { n } ( z )$ are the Bernoulli Polynomials. The generating function (2.6.3l） provides a convenient way to define them.Fora general $f ( z )$ ,the resulting polynomials $p _ { n } ( s )$ defined by

$$
f ( z ) e ^ { s z } \ : = \ : \sum _ { n = 0 } ^ { \infty } p _ { n } ( s ) z ^ { n }
$$

are known as Appel Polynomials.

Differentiating (2.6.31) $j$ times with respect to $s$ we obtain

$$
\frac { z ^ { j + 1 } e ^ { s z } } { e ^ { z } - 1 } = \sum _ { n = 0 } ^ { \infty } \frac { B _ { n } ^ { ( j ) } ( s ) z ^ { n } } { n ! } , \quad | z | < 2 \pi .
$$

Set $s = 0 , 1$ in (2.6.33),and subtract,

$$
z ^ { j + 1 } \Bigg ( \frac { e ^ { z } - 1 } { e ^ { z } - 1 } \Bigg ) \ = \sum _ { n = 0 } ^ { \infty } \frac { B _ { n } ^ { ( j ) } ( 1 ) - B _ { n } ^ { ( j ) } ( 0 ) } { n ! } z ^ { n } , | z | < 2 \pi , j = 0 , 1 , . . .
$$

By the uniqueness theorem for power series we must have

$$
\frac { B _ { j + 1 } ^ { ( j ) } ( 1 ) - B _ { j + 1 } ^ { ( j ) } ( 0 ) } { ( j + 1 ) ! } = 1 \quad \mathrm { w h i l e } \quad B _ { r } ^ { ( j ) } ( 1 ) - B _ { r } ^ { ( j ) } ( 0 ) = 0 , r \ne j + 1 .
$$

We see now that the polynomials ${ \cal B } _ { \bf 0 } ( x ) , { \cal B } _ { \bf 1 } ( x ) , \dots .$ and the functionals

$$
L _ { 0 } ( f ) = f ( 0 ) , L _ { 1 } ( f ) = f ( 1 ) - f ( 0 ) ,
$$

$$
L _ { 2 } ( f ) = \frac { f ( 1 ) - f ^ { \prime } ( 0 ) } { 2 ! } , L _ { 3 } ( f ) = \frac { f ^ { \prime \prime } ( 1 ) - f ^ { \prime \prime } ( 0 ) } { 3 ! } , \ldots ,
$$

form a biorthogonal set.

Ex.4 (Orthogonal Polynomials)． Though these polynomials will be treated in detail in Chapter $\mathbf { x }$ ,it is interesting to note how they fit in with Theorem 2.6.1 and Corollary 2.6.2.Let $X = C [ a , b ]$ .Let $w ( x )$ be a fixed positive weight function for which the integrals $\int _ { a } ^ { b } w ( x ) x ^ { n } d x , n = 0 , 1 , 2 , . . .$ ,all exist. Introduce the functionals $L _ { n } ( f ) \ = \int _ { a } ^ { b } w ( x ) x ^ { n } f ( x ) d x , n \ = \ 0 , 1 , 2 , . . . . .$ These are the weighted moments of $f$ .It will then be possible to biorthonormalize the powers $1 , x , x ^ { 2 } , \ldots ,$ against these functionals. (In Chapter VIII it will be shown that the determinant condition for this is fulfilled.)We then obtain $^ { \pmb { a } }$ sand $^ { b }$ s such that

$$
\begin{array} { c l c r } { { } } & { { } } & { { L _ { n } { } ^ { * } ( f ) = \displaystyle \int _ { a } ^ { b } w ( x ) ( a _ { n 0 } + a _ { n 1 } x + \cdot \cdot \cdot + a _ { n n } x ^ { n } ) f ( x ) d x } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle p _ { n } ( x ) = b _ { n 0 } + b _ { n 1 } x + \cdot \cdot \cdot + b _ { n n - 1 } x ^ { n - 1 } + x ^ { n } } } \\ { { } } & { { } } & { { L _ { n } { } ^ { * } ( p _ { j } ( x ) ) = \delta _ { n j } . } } \end{array}
$$

A glance at the determinants (2.6.21) shows that the a's and ó's in (2.6.35) are proportional. Indeed,since $L _ { i } ( x ^ { j } ) = \int _ { a } ^ { b } w ( x ) x ^ { i } x ^ { j } d x = L _ { j } ( x ^ { i } )$ ，the minors corre-sponding to elements $\boldsymbol { x } _ { i }$ and $\pmb { L _ { i } }$ are equal. After accounting for the factors $\scriptstyle Q _ { n - 1 }$ and $\scriptstyle { \pmb { G } } _ { n }$ infront of these determinants,we find

$$
L _ { n } { } ^ { * } ( f ) \ = \int _ { a } ^ { b } w ( x ) \ { \frac { G _ { n - 1 } } { G _ { n } } } p _ { n } ( x ) f ( x ) \ d x .
$$

If we now set

$$
p _ { n } { * } ( x ) = \sqrt { \frac { G _ { n - 1 } } { G _ { n } } } p _ { n } ( x )
$$

we shall have

$$
\begin{array} { l } { \displaystyle \sqrt { \frac { G _ { j - 1 } } { G _ { j } } } \sqrt { \frac { G _ { n } } { G _ { n - 1 } } } L _ { n } { } ^ { * } ( p _ { j } ) = \delta _ { n j } } \\ { \displaystyle = \int _ { a } ^ { b } w ( x ) \sqrt { \frac { G _ { n - 1 } } { G _ { n } } } p _ { n } ( x ) \sqrt { \frac { G _ { j - 1 } } { G _ { j } } } p _ { j } ( x ) d x } \\ { \displaystyle = \int _ { a } ^ { b } w ( x ) p _ { n } { } ^ { * } ( x ) p _ { j } { } ^ { * } ( x ) d x . } \end{array}
$$

The polynomials ${ { p } _ { n } } ^ { * }$ are called orthonormal over $[ a , b ]$ with respect to the weight $w ( x )$ .They are determined up to a factor of $\pm 1$ .(2.6.21) and (2.6.37) now give us the following determinant representation for the orthonormal polynomials

$$
\begin{array} { r } { p _ { n } \pmb { * } ( x ) = C _ { n } \left| \begin{array} { c c c c } { ( 1 , 1 ) } & { ( 1 , x ) } & { \cdots \cdot } & { ( 1 , x ^ { n } ) } \\ { ( x , 1 ) } & { ( x , x ) } & { \cdots \cdot } & { ( x , x ^ { n } ) } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { } & { \cdot } \\ { \cdot } & { } & { \cdot } \\ { ( x ^ { n - 1 } , 1 ) } & { ( x ^ { n - 1 } , x ) } & { \cdots \cdot } & { ( x ^ { n - 1 } , x ^ { n } ) } \\ { \phantom { \cdot } } & { } & { \cdot \cdot } & { x ^ { n } } \end{array} \right| } \end{array}
$$

where

$$
( x ^ { i } , x ^ { j } ) = \int _ { a } ^ { b } w ( x ) x ^ { i + j } d x
$$

and

with

$$
\begin{array} { l } { { C _ { n } = ( G _ { n } G _ { n - 1 } ) ^ { - \frac { 1 } { 2 } } \nonumber } } \\ { { G _ { n } = \left| ( x ^ { i } , x ^ { j } ) \right| _ { i , j = 0 } ^ { n } . } } \end{array}
$$

# 2.7Successive Differences

DEFINITIoN 2.7.1. Let there be given a sequence of values yo, Y1, .\*.. The differences of adjacent values are designated by

$$
\Delta y _ { k } = y _ { k + 1 } - y _ { k } , ~ k = 0 , 1 , \cdots .
$$

Higher diferences are defined similarly

$$
\Delta ^ { 2 } y _ { k } = \Delta ( \Delta y _ { k } ) = \Delta y _ { k + 1 } - \Delta y _ { k } = ( y _ { k + 2 } - y _ { k + 1 } ) - ( y _ { k + 1 } - y _ { k } ) .
$$

In general,

$$
\Delta ^ { n + 1 } y _ { k } = \Delta ( \Delta ^ { n } y _ { k } ) = \Delta ^ { n } y _ { k + 1 } - \Delta ^ { n } y _ { k } .
$$

We define $\Delta ^ { 0 } y _ { k } = y _ { k }$

THEOREM 2.7.1. We have

$$
\begin{array} { r l } & { \Delta ^ { 0 } y _ { k } = y _ { k } } \\ & { \Delta ^ { 1 } y _ { k } = y _ { k + 1 } - y _ { k } } \\ & { \Delta ^ { 2 } y _ { k } = y _ { k + 2 } - 2 y _ { k + 1 } + y _ { k } } \\ & { \Delta ^ { 3 } y _ { k } = y _ { k + 3 } - 3 y _ { k + 2 } + 3 y _ { k + 1 } - y _ { k } } \end{array}
$$

In general,

$$
\Delta ^ { n } y _ { k } = \sum _ { r = 0 } ^ { n } ( - 1 ) ^ { n - r } { \binom { n } { r } } y _ { k + r } , \quad { \binom { n } { r } } = { \frac { n ! } { r ! ( n - r ) ! } } .
$$

Proof: Formula (2.7.4) holds trivially for ${ \pmb n } = { \bf 0 }$ ，and this begins an inductive proof. Assume (2.7.4) true for $\pmb { n }$ Then,

$$
\begin{array} { r l } & { \Delta ^ { n + 1 } y _ { k } = \Delta ( \Delta ^ { n } y _ { k } ) = \Delta \Big ( \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \Big ( \underset { r } { \overset { n } { \sum } } y _ { k + r } \Big ) } \\ & { \qquad = \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \Big ( \underset { r } { \overset { n } { \sum } } \Big ) \Delta y _ { k + r } = \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \binom { n } { r } ( y _ { k + 1 + r } - y _ { k + r } ) } \\ & { \qquad = \underset { r = 1 } { \overset { n + 1 } { \sum } } ( - 1 ) ^ { n + 1 - r } \Big ( \underset { r = 1 } { \overset { n } { \binom { n } { r } } } y _ { k + r } - \underset { r = 0 } { \overset { n } { \sum } } ( - 1 ) ^ { n - r } \Big ( \underset { r } { \overset { n } { \sum } } \Big ) y _ { k + r } } \\ & { \qquad = \underset { r = 1 } { \overset { n } { \sum } } ( - 1 ) ^ { n + 1 - r } y _ { k + r } \Big [ \Big ( \underset { r = 1 } { \overset { n } { \sum } } \Big ) + \binom { n } { r } \Big ] + \binom { n } { n } y _ { k + n + 1 } - ( - 1 ) ^ { n } \binom { n } { 0 } y } \\ & { \qquad = \underset { r = 0 } { \overset { n + 1 } { \sum } } ( - 1 ) ^ { n + 1 - r } y _ { k + r } \Big ( \underset { r } { \overset { n } { \sum } } + 1 \Big ) . } \end{array}
$$

Thus,if the formula is true for $\pmb { n }$ ,it must be true for $n + 1$ ,and the induction is complete.

COROLLARY 2.7.2. For $\pmb { k } = \mathbf { 0 }$ we have

$$
\Delta ^ { n } y _ { 0 } = \sum _ { r = 0 } ^ { n } ( - 1 ) ^ { n - r } { \binom { n } { r } } y _ { r } .
$$

In the case of interpolation at abscissas $z _ { 0 } , z _ { 1 } , . . .$ , that are spaced evenly:

$$
z _ { 0 } = a , z _ { 1 } = a + h , z _ { 2 } = a + 2 h , . . . , z _ { n } = a + n h ,
$$

the divided differences may be given an elegant expression in terms of successive differences.If $w ( z ) = ( z - z _ { 0 } ) ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { n } )$ ,then

$$
w ^ { \prime } ( z _ { k } ) = ( z _ { k } - z _ { 0 } ) ( z _ { k } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { k - 1 } ) ( z _ { k } - z _ { k + 1 } ) \cdot \cdot \cdot ( z _ { k } - z _ { n } ) .
$$

Since $z _ { i } - z _ { j } = ( i - j ) h$ ，

$$
\begin{array} { c } { { w ^ { \prime } ( z _ { k } ) = ( k h ) ( k - 1 ) h \cdot \cdot \cdot ( h ) ( - h ) ( - 2 h ) \cdot \cdot \cdot ( - ( n - k ) h ) } } \\ { { = h ^ { n } k ! ( n - k ) ! ( - 1 ) ^ { n - k } . } } \end{array}
$$

Therefore from (2.6.4),

$$
{ \begin{array} { r l } & { a _ { n } = [ y _ { 0 } , y _ { 1 } , \dots , y _ { n } ] = \displaystyle \sum _ { k = 0 } ^ { n } { \frac { y _ { k } } { w ^ { \prime } ( z _ { k } ) } } } \\ & { \quad = \displaystyle \sum _ { k = 0 } ^ { n } { \frac { ( - 1 ) ^ { n - k } y _ { k } } { h ^ { n } k ! ( n - k ) ! } } = { \frac { 1 } { n ! h ^ { n } } } \sum _ { k = 0 } ^ { n } ( - 1 ) ^ { n - k } { \binom { n } { k } } y _ { k } } \\ & { \quad = \displaystyle { \frac { \Delta ^ { n } y _ { 0 } } { n ! h ^ { n } } } . } \end{array} }
$$

We can therefore prove the following theorem.

THEOREM 2.7.3. Let $\pmb { p } ( z )$ be the unique polynomial of $\mathcal { P } _ { n }$ that takes on the values $y _ { 0 } , y _ { 1 } , \ldots , y _ { n }$ at the $n + 1$ points $a , a + h , \ldots , a + n h$ . Then

$$
{ \begin{array} { r l } & { p _ { n } ( z ) = y _ { 0 } + { \cfrac { \Delta y _ { 0 } } { h } } ( z - a ) + { \cfrac { \Delta ^ { 2 } y _ { 0 } } { 2 ! h ^ { 2 } } } ( z - a ) ( z - a - h ) + \cdots } \\ & { \qquad + { \cfrac { 1 } { n ! h ^ { n } } } \Delta ^ { n } y _ { 0 } ( z - a ) ( z - a - h ) \cdot \cdot \cdot ( z - a - ( n - 1 ) h ) . } \end{array} }
$$

If $p _ { n } ( f ; z )$ interpolates to $f$ at $a , a + h , \ldots , a + n h$ then

$$
\begin{array} { l } { { p _ { n } ( f ; z ) = f ( a ) + \displaystyle \frac { \Delta f ( a ) } { h } ( z - a ) + \displaystyle \frac { 1 } { 2 ! h ^ { 2 } } \Delta ^ { 2 } f ( a ) ( z - a ) ( z - a - h ) + \cdots } } \\ { { \mathrm { } + \displaystyle \frac { 1 } { n ! h ^ { n } } \Delta ^ { n } f ( a ) ( z - a ) ( z - a - h ) \cdot \cdot \cdot ( z - a - ( n - 1 ) h ) . \quad ( 2 . 7 . 1 } } \end{array}
$$

We have written

$$
\begin{array} { l } { \Delta f ( a ) = f ( a + h ) - f ( a ) } \\ { \Delta ^ { 2 } f ( a ) = f ( a + 2 h ) - 2 f ( a + h ) + f ( a ) , \mathrm { { e t c . } } } \end{array}
$$

Formulas (2.7.9) and (2.7.10) are known as Newton's forward diffrence formulas.

If $f ( x )$ is defined at ${ \pmb a } , { \pmb a } + \hbar , { \pmb a } + 2 \hbar , . . . .$ ,the formal series

$$
f ( x ) \sim \sum _ { k = 0 } ^ { \infty } { \frac { \Delta ^ { k } f ( a ) } { k ! h ^ { k } } } ( z - a ) ( z - a - h ) \cdot \cdot \cdot ( z - a - ( k - 1 ) h )
$$

is called a Newton series for $f$

Ex.1. $\mathbf { I f } f ( x ) = x ^ { n }$ ,then $\Delta f ( x ) = n h x ^ { n - 1 } + \cdot \cdot \cdot .$ The first difference is therefore a polynomial of degree $n \mathrm { ~ - ~ } 1$ .Similarly,we find $\Delta ^ { n } x ^ { n } \ = n ! \ h ^ { n }$ and $\Delta ^ { p } x ^ { n } = 0$ for $\textit { \textbf { p } } > n$

Ex.2.If $f \left( x \right) = e ^ { \sigma x }$ then $\Delta f ( x ) = ( e ^ { \sigma h } - 1 ) \epsilon ^ { \sigma x }$ Iterating this, $\Delta ^ { n } f ( x ) =$ $( e ^ { \sigma h } - 1 ) ^ { n } e ^ { \sigma x }$

Ex.3.If $f \left( x \right) \in \mathcal { P } _ { n }$ then the series (2.7.12） converges to $f ( x )$ .From Ex. 1, the series reduces to a sum of $n + 1$ terms and,by Theorem 2.7.3,is that member of ${ \mathcal { P } } _ { n }$ which interpolates to $f$ at $a , a \ + \ h , \ . \ . \ . \ , a \ + \ n h$ By uniqueness,it must coincide with $f$

Ex.4．On the other hand,the function $f ( x ) = \sin \pi x$ has zeros at ${ \bf 0 } , { \bf \pm 1 }$ ， $\pm 2 , . . .$ ,so thatwith $a = 0 , h = 1 , \Delta ^ { k } f ( 0 ) \equiv 0$ .The series (2.7.12) is identically zero and does not represent $f ( x )$ over any interval.An entire function may still not be sufficiently restricted in its behavior to be represented by its Newton series.

# NOTES ON CHAPTER II

2.1The discussion of polynomial interpolation in Chapters II and II can be amplified by related material in any text on numerical analysis.Mention should be made also of the numerous practical articles of H.E.Salzer related to interpolation.

2.3Abel-Gontscharoff Interpolation:J.M.Whittaker [l],p.38；V.L. Gontscharoff [1]，pp.84-86.Lidstone Interpolation:D. V. Widder [3], R.P.Boas,Jr.[2].Hermite's Interpolation:A.A.Markoff[l]; Gontscharoff [l],p.64.Hermite's formulas are rediscovered and republished every few years.Generalized Taylor Interpolation:D.V.Widder[l],[2],I.M. Sheffer [l].Trigonometric Interpolation,A. Zygmund [l],Vol.II.

2.4For additional examples of unisolvent systems,see Polya and Szego [1],vol.II,pp.45-52.Further theory is presented in Achieser [l],p.67 et seq.and in Motzkin [l].References to recent work related to Haar's Theorem can be found in Buck [2].

2.5-2.6 General formulae of Lagrange and Newton type have been given implicitly and explicitly by many authors.For instance,see the articles by Widder and Shefer cited in 2.3. Also: W. E. Milne [1]. H. B. Curry [1] develops these notions and contains some further references.

Bernoulli Polynomials: N.E. Norlund [1].

Appel Polynomials: Boas and Buck [1], E. D. Rainville [1].

2.7For the algebraic side of differences,consult books on difference calculus such as Fort [l]. There are extensive studies of the convergence of interpolation series some of which are found in books:Norlund [1],Whittaker[l].A.O.Gelfand [1] has a noteworthy treatment of Newton series and allied questions.See also Buck[1].

# PROBLEMS

1. If $V ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ designates the Vandermonde determinant, show that $V ( 1 , 2 , 3 , . . . , n ) = 1 ! 2 ! 3 ! \cdot \cdot \cdot ( n - 1 ) !$

2. Can a parabola $\pmb { p }$ be found for which $\mathcal { p } ( 0 ) , \mathcal { p } ^ { \prime \prime } ( 0 ) , \mathcal { p } ^ { \prime \prime \prime } ( 0 )$ have preassigned values? For which $\int _ { - 1 } ^ { 1 } p ( x ) \ : d x , p ( 0 ) , p ^ { \prime } ( 0 ) \ :$ have preassigned values?

3.Construct a polynomial in $\mathscr { P } _ { 3 }$ for which $\begin{array} { r } { p ( 0 ) = 1 , p ( 1 ) = 3 , p ^ { \prime } ( - 1 ) = 4 , } \end{array}$ $p ^ { \prime \prime } ( 0 ) = 0$ .Is the answer unique?

4.Three points lie on a nonvertical line.What happens when you try to fit a parabola to them?A cubic?Formulate a general statement.

5.Show that wecan not alwaysfindafunctionoftheformf(x)= that passes through three points with distinct abscissas.

6.Is it possible to fit a curve of the form $f ( x ) = A + B e ^ { C x }$ to the data $f ( 0 ) = 0 , f ( 1 ) = 1 , f ( 2 ) = \frac { 1 } { 2 } ?$

7. $x$ consists of all functions of the form $a _ { 0 } + a _ { 1 } x + a _ { 2 } y + a _ { 3 } x ^ { 2 } + a _ { 4 } x y + a _ { 5 } y ^ { 2 }$ defined on $- 1 \leq x \leq 1$ ， $- 1 \le y \le 1$ .Find a basis for $x ^ { * }$ ·

8. Let $X = \mathcal { P } _ { n }$ considered on $0 \leq x \leq 1$ Let $0 < x _ { 0 } < \cdots < x _ { n } \leq 1$ Prove that $L _ { j } ( f ) = \int _ { 0 } ^ { x _ { j } } f ( t ) d t , j = 0 , 1 , . . . , n ,$ ，are independent over $x *$ ·

9.Select the constants $A , \ldots , E$ so that $\frac { A + B x + C x ^ { 2 } } { 1 + D x + E x ^ { 2 } }$ ：agrees with the Maclaurin series expansion of $e ^ { \mathfrak { X } }$ as far as $x ^ { 4 }$ .How close is the resulting rational function to $e ^ { \ast }$ over the interval $| x | \leq { \frac { 1 } { 1 0 } }$ ？

10. If $R ( x ) = { \frac { A + B x } { 1 + C x } }$ ， can the interpolation problem $R ( 0 ) = f ( 0 ) , R ^ { \prime } ( 0 ) =$ $f ^ { \prime } ( 0 ) , R ^ { \prime \prime } ( 0 ) = f ^ { \prime \prime } ( 0 )$ always be solved?What about a similar problem for rational functions of higher degree? The resulting rational functions are called the Padé Approximants to $f ( x )$

11. Let $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ be fixed．Let $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }$ and $p ( x _ { i } ) = y _ { i }$ Given an $\varepsilon > 0$ , we can find a $\pmb { \delta }$ such that $\left| y _ { i } \right| \le \delta$ implies $\left. a _ { i } \right. \leq \varepsilon$

12.Discuss the possibility of trigonometric interpolation with Taylor conditions.

13.Discuss the possibility of osculatory trigonometric interpolation.

14. Let $T ( x ) = a _ { 0 } + a _ { 1 } \cos x + b _ { 1 }$ sin $x + \cdots + a _ { n }$ cos ${ \pmb n } { \pmb x } + { \pmb b } _ { \pmb n }$ sin $_ { n x }$ Consider $e ^ { i n x } T ( x ) = P _ { 2 n } ( e ^ { i x } )$ and show that the number of real roots modulo $\pmb { 2 \pi }$ of $\pmb { T } ( \pmb { x } )$ ,each root counted with its multiplicity,is $\leq 2 n$ ·