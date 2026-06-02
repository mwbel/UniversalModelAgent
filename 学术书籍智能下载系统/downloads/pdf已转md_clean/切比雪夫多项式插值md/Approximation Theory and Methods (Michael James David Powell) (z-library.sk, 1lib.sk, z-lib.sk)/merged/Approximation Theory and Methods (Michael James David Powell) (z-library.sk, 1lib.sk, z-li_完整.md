<!-- source: Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-lib.sk).pdf -->

<!-- pdf_type: normal; pages: 351; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
M.J.D.POWELL   
Approximation   
theory and   
methods   
M. J. D. POWELL   
John Humphrey Plummer Professor of Applied Numerical Analysis   
University of Cambridge

Approximation theory and methods

# CAMBRIDGE UNIVERSITY PRESS

Cambridge New York Port ChesterMelbourneSydney

Published by the Press Syndicate of the University of Cambridge The Pitt Building, Trumpington Street, Cambridge CB2 1RP 40 West 20th Street,New York,NY l0011,USA 10 Stamford Road, Oakleigh,Melbourne 3l66,Australia

$^ { © }$ Cambridge University Press 1981

First published 1981   
Reprinted 1988,1991

Printed in the United States of America

British Library cataloguing in publication data

Powell,MJD   
Approximation theory and methods. 1.Approximation theory   
1. Title   
511'.4 QA221   
ISBN 0 521 22472 1 hard covers ISBNO 521295149 paperback

# Preface

# lThe approximation problem and existence of best approximations 1

1.1 Examples of approximation problems 1

1.2 Approximation in a metric space 3

1.3 Approximation in a normed linear space 5

1.4 The $L _ { p } .$ -norms 6

1.5 A geometric view of best approximations 9

# 2 The uniqueness of best approximations 13

2.1 Convexity conditions 13   
2.2 Conditions for the uniqueness of the best approximation 14   
2.3 The continuity of best approximation operators 16   
2.4 The 1-,2- and o-norms 17

# 3Approximation operators and some approximating functions

3.1 Approximation operators 22   
3.2 Lebesgue constants 24   
3.3 Polynomial approximations to differentiable functions 25   
3.4 Piecewise polynomial approximations 28

4Polynomial interpolation 33

4.1 The Lagrange interpolation formula 33   
4.2 The error in polynomial interpolation 35   
4.3 The Chebyshev interpolation points 37   
4.4 The norm of the Lagrange interpolation operator 41

5Divided differences 46

5.1 Basic properties.of divided differences 46

5.2 Newton's interpolation method 48

Contents vi

5.3 The recurrence relation for divided differences 49   
5.4 Discussion of formulae for polynomial interpolation 51   
5.5 Hermite interpolation 53

# 6The uniform convergence of polynomial approximations 6

6.1 The Weierstrass theorem 61   
6.2 Monotone operators 62   
6.3 The Bernstein operator 65   
6.4 The derivatives of the Bernstein approximations 67

# 7The theory of minimax approximation 72

7.1 Introduction to minimax approximation 72   
7.2 The reduction of the error of a trial approximation 74   
7.3 The characterization theorem and the Haar condition 76   
7.4 Uniqueness and bounds on the minimax error 79

8The exchange algorithm 85

8.1 Summary of the exchange algorithm 85

8.2 Adjustment of the reference 87

8.3 An example of the iterations of the exchange algorithm 88

8.4 Applications of Chebyshev polynomials to minimax approximation 90

8.5 Minimax approximation on a discrete point set 92

# 9The convergence of the exchange algorithm 97

9.1 The increase in the levelled reference error 97   
9.2 Proof of convergence 99   
9.3 Properties of the point that is brought into reference 102   
9.4 Second-order convergence 105

# 10Rational approximation by the exchange algorithm 111

10.1 Best minimax rational approximation 111   
10.2 The best approximation on a reference 113   
10.3 Some convergence properties of the exchange algorithm 116   
10.4 Methods based on linear programming 118

# 11 Least squares approximation 123

11.1 The general form of a linear least squares calculation 123   
11.2 The least squares characterization theorem 125   
11.3 Methods of calculation 126   
11.4 The recurrence relation for orthogonal polynomials 131

Contents vii

12Properties of orthogonal polynomials 136

12.1 Elementary properties 136   
12.2 Gaussian quadrature 138   
12.3 The characterization of orthogonal polynomials 141   
12.4 The operator $\scriptstyle { R _ { n } }$ 143

13 Approximation to periodic functions 150

13.1 Trigonometric polynomials 150   
13.2 The Fourier series operator $S _ { n }$ 152   
13.3 The discrete Fourier series operator 156   
13.4 Fast Fourier transforms 158

# 14 The theory of best $\pmb { L _ { 1 } }$ approximation 164

14.1 Introduction to best $L _ { 1 }$ approximation 164   
14.2 The characterization theorem 165   
14.3 Consequences of the Haar condition 169   
14.4 The $L _ { 1 }$ interpolation points for algebraic polynomials 172

# 15An example of $\pmb { L _ { 1 } }$ approximation and the discrete case 17'

15.1 A useful example of $L _ { 1 }$ approximation 177   
15.2 Jackson's first theorem 179   
15.3 Discrete $L _ { 1 }$ approximation 181   
15.4 Linear programming methods 183

# 16The order of convergence of polynomial approximations

16.1 Approximations to non-differentiable functions 189   
16.2 The Dini-Lipschitz theorem 192   
16.3 Some bounds that depend on higher derivatives 194   
16.4 Extensions to algebraic polynomials 195

# 17 The uniform boundedness theorem 200

17.1 Preliminary results 200   
17.2 Tests for uniform convergence 202   
17.3 Application to trigonometric polynomials 204   
17.4 Application to algebraic polynomials 208

# 18Interpolation by piecewise polynomials 212

18.1 Local interpolation methods 212   
18.2 Cubic spline interpolation 215   
18.3 End conditions for cubic spline interpolation 219   
18.4 Interpolating splines of other degrees 221

Contents vii

19B-splines 227

19.1 The parameters of a spline function 227   
19.2 The form of $\pmb { B }$ -splines 229   
19.3 $\pmb { B }$ -splines as basis functions 231   
19.4 A recurrence relation for $\pmb { B }$ -splines 234   
19.5 The Schoenberg-Whitney theorem 236

# 20 Convergence properties of spline approximations 241

20.1 Uniform convergence 241   
20.2 The order of convergence when $f$ is differentiable 243   
20.3 Local spline interpolation 246   
20.4 Cubic splines with constant knot spacing 248

# 21Knot positions and the calculation of spline approximations

21.1 The distribution of knots at a singularity 254   
21.2 Interpolation for general knots 257   
21.3 The approximation of functions to prescribed accuracy 261

# 22 The Peano kernel theorem

268

22.1 The error of a formula for the solution of differential equations

22.2 The Peano kernel theorem 270

22.3 Application to divided differences and to polynomial interpolation

22.4 Application to cubic spline interpolation 277

23 Natural and perfect splines 283

23.1 A variational problem 283   
23.2 Properties of natural splines 285   
23.3 Perfect splines 290

:4Optimal interpolation 298

24.1 The optimal interpolation problem 298   
$2 4 . 2 \ { \cal L } _ { 1 }$ approximation by $\pmb { B }$ -splines 301   
24.3 Properties of optimal interpolation 307   
Appendix A The Haar condition 313   
Appendix B Related work and references 317   
Index 333

There are several reasons for studying approximation theory and methods, ranging from a need to represent functions in computer calculations to an interest in the mathematics of the subject. Although approximation algorithms are used throughout the sciences and in many industrial and commercial fields, some of the theory has become highly specialized and abstract.Work in numerical analysis and in mathematical software is one of the main links between these two extremes, for its purpose is to provide computer users with efficient programs for general approximation calculations, in order that useful advances in the subject can be applied. This book presents the view of a numerical analyst, who enjoys the theory,and who is keenly interested in its importance to practical computer calculations. It is based on a course of twenty-four lectures,given to third-year mathematics undergraduates at the University of Cambridge.There is really far too much material for such a course, but it is possible to speak coherently on each chapter for about one hour, and to include proofs of most of the main theorems. The prerequisites are an introduction to linear spaces and operators and an intermediate course on analysis, but complex variable theory is not required.

Spline functions have transformed approximation techniques and theory during the last fifteen years. Not only are they convenient and suitable for computer calculations, but also they provide optimal theoretical solutions to the estimation of functions from limited data. Therefore seven chapters are given to spline approximations. The classical theory of best approximations from linear spaces with respect to the minimax,least squares and $L _ { 1 }$ -norms is also studied, and algorithms are described and analysed for the calculation of these approximations. Interpolation is considered also,and the accuracy of interpolation and other linear operators is related to the accuracy of optimal algorithms. Special attention is given to polynomial functions,and there is one chapter on rational functions, but, due to the constraints of twenty-four lectures, the approximation of functions of several variables is not included. Also there are no computer listings,and little attention is given to the consequences of the rounding errors of computer arithmetic. All theorems are proved,and the reader will find that the subject provides a wide range of techniques of proof. Some material is included in order to demonstrate these techniques,for example the analysis of the convergence of the exchange algorithm for calculating the best minimax approximation to a continuous function. Several of the proofs are new. In particular, the uniform boundedness theorem is established in a way that does not require any ideas that are more advanced than Cauchy sequences and completeness.Less functional analysis is used than in other books on approximation theory，and normally functions are assumed to be continuous,in order to simplify the presentation.Exercises are included with each chapter which support and extend the text.All references to related work are given in an appendix.

It is a pleasure to acknowledge the excellent opportunities I have received for research and study in the Department of Applied Mathematics and Theoretical Physics at the University of Cambridge since 1976, and before that at the Atomic Energy Research Establishment, Harwell. My interest in approximation theory began at Harwell, stimulated by the enthusiasm of Alan Curtis,and strengthened by Pat Gaffney，who developed some of the theory that is reported in Chapter 24. I began to write this book in the summer of 1978 at the University of Victoria, Canada,and I am grateful for the facilities of their Department of Mathematics, for the encouragement of Ian Barrodale and Frank Roberts,and for financial support from grants A5251 and A7143 of the National Research Council of Canada. At Cambridge David Carter of King's College kindly studied drafts of the chapters and offered helpful comments. The manuscript was typed most expertly by Judy Roberts, Hazel Felton,Margaret Harrison and Paula Lister. I wish to express special thanks to Hazel for her assistance and patience when I was redrafting the text. My wife,Caroline, not only showed sympathetic understanding at home during the time when I worked long hours to complete the manuscript, but also she assisted with the figures.This work is dedicated to Caroline.

Pembroke College, Cambridge January 1980

# The approximation problem and existence of best approximations

# 1.1 Examples of approximation problems

A simple example of an approximation problem is to draw a straight line that fits the curve shown in Figure 1.1. Alternatively we may require a straight line fit to the data shown in Figure 1.2. Three possible fits to the discrete data are shown in Figure 1.3,and it seems that lines $\pmb { B }$ and $c$ are better than line $\pmb { A }$ . Whether $\pmb { B }$ or $c$ is preferable depends on our confidence in the highest data point, and to choose between the two straight lines we require a measure of the quality of the trial approxima-tions. These examples show the three main ingredients of an approximation calculation, which are as follows: (1) A function, or some data, or more generally a member of a set, that is to be approximated. We call it $f .$ (2) A set, $\mathscr { A }$ say,of approximations,which in the case of the given examples is the set of all straight lines. (3) A means of selecting an approximation from $\scriptstyle { \mathcal { A } } .$

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0001_pages_0001-0070/auto/images/dc40860ae2d24e735cd7f53fff3b397a867c6fb666e0f67c77843a5dc69b6da6.jpg)  
Figure 1.1. A function to be approximated.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0001_pages_0001-0070/auto/images/4a97e856122ac3dd94086b4462e638957f717257228bacb08742766bb83503b6.jpg)  
Figure 1.2. Some data to be approximated.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0001_pages_0001-0070/auto/images/8c49b53b047be022ce5822c9df836873f9528e06570e8a3e236dc107817ba928.jpg)  
Figure 1.3. Three straight-line fits to the data of Figure 1.2.

Approximation problems of this type arise frequently. For instance we may estimate the solution of a differential equation by a function of a certain simple form that depends on adjustable parameters,where the measure of goodness of the approximation is a scalar quantity that is derived from the residual that occurs when the approximating function is substituted into the differential equation. Another example comes from the choice of components in electrical circuits.The function $f$ may be the required response from the circuit， and the range of available components gives a set $\mathscr { A }$ of attainable responses. We have to approximate $f$ by a member of $\mathcal { A } ,$ , and we require a criterion that selects suitable components. Moreover， in computer calculations of mathematical functions, the mathematical function is usually approximated by one that is easy to compute.

Many closely related questions are of interest also. Given $f$ and $\mathcal { A } ,$ we may wish to know whether any member of $\mathscr { A }$ satisfies a fixed tolerance condition, and, if suitable approximations exist, we may be willing to accept any one. It is often useful to develop methods for selecting a member of $\pmb { \mathcal { A } }$ such that the error of the chosen approximation is always within a certain factor of the least error that can be achieved.It may be possible to increase the size of $\mathscr { A }$ if necessary, for example $\pmb { \mathcal { A } }$ may be a linear space of polynomials of any fixed degree,and we may wish to predict the improvement in the best approximation that comes from enlarging $\pmb { \mathcal { A } }$ by increasing the degree.At the planning stage of a numerical method we may know only that $f$ will be a member of a set $\mathcal { B } _ { : }$ ,in which case it is relevant to discover how well any member of $\mathcal { B }$ can be approximated from ${ \mathcal { A } } .$ Further, given $\mathcal { B }$ , it may be valuable to compare the suitability of two different sets of approximating functions, $\mathcal { A } _ { 0 }$ and $\mathcal { A } _ { 1 }$ . Numerical methods for the calculation of approximating functions are required. This book presents much of the basic theory and algorithms that are relevant to these questions,and the material is selected and described in a way that is intended to help the reader to develop suitable techniques for himself.

# 1.2 Approximation in a metric space

The framework of metric spaces provides a general way of measuring the goodness of an approximation, because one of the basic properties of a metric space is that it has a distance function. Specifically, the distance function $d ( x , y )$ of a metric space $\mathcal { B }$ is a real-valued function, that is defined for all pairs of points $( x , y )$ in $\mathcal { B }$ ,and that has the following properties. If $x \neq y$ ,then $d ( x , y )$ is positive and is equal to $d ( y , x )$ .If $\ b x = \ b y$ ， then the value of $d ( x , y )$ is zero. The triangle inequality

$$
d ( x , y ) \leqslant d ( x , z ) + d ( z , y )
$$

must hold, where $x , y$ and $z$ are any three points in $\mathcal { B }$

In most approximation problems there exists a suitable metric space that contains both $f$ and the set of approximations ${ \mathcal { A } } .$ .Then it is natural to decide that $\pmb { a } _ { 0 } \in \mathcal { A }$ is a better approximation than $\pmb { a } _ { 1 } \in \mathcal { A }$ if the inequality

$$
d ( a _ { 0 } , f ) < d ( a _ { 1 } , f )
$$

is satisfied. We define $\ b { a } ^ { * } \in \mathcal { A }$ to be a best approximation if the condition

$$
d ( a ^ { \ast } , f ) \leq d ( a , f )
$$

holds for all ${ \pmb a } \in \mathcal { A } .$

The metric space should be chosen so that it provides a measure of the error of each trial approximation. For example, in the problem of fitting the data of Figure 1.2 by a straight line, we approximate a set of points $\{ ( x _ { i } , y _ { i } ) ; i = 1 , 2 , 3 , 4 , 5 \}$ by a function of the form

$$
p ( x ) = c _ { 0 } + c _ { 1 } x ,
$$

where $c _ { 0 }$ and $\pmb { c _ { 1 } }$ are scalar coefficients. Because we are interested in only five values of $\pmb { x } ,$ ，the most convenient space is $\mathcal { R } ^ { s }$ . The fact that $p ( { \pmb x } )$ depends on two parameters is not relevant to the choice of metric space. We measure the goodness of the approximation (1.4) as the distance, according to the metric we have chosen, from the vector of function values $\{ p ( x _ { i } ) ; i = 1 , 2 , 3 , 4 , 5 \}$ to the data values $\{ y _ { i } ; i = 1 , 2 , 3 , 4 , 5 \}$

It may be important to know whether or not a best approximation exists. One reason is that many methods of calculation are derived from properties that are obtained by a best approximation. The following theorem shows existence in the case when $\mathcal { A }$ is compact.

# Theorem 1.1

If $\mathscr { A }$ is a compact set in a metric space $\mathcal { B }$ ,then,for every $f$ in $\mathcal { B }$ ， there exists an element $\pmb { a } ^ { * } \in \mathcal { A }$ ，such that condition (1.3） holds for all $\pmb { a } \in \mathcal { A }$

Proof. Let $d ^ { * }$ be the quantity

$$
d ^ { * } = \operatorname* { i n f } _ { a \in { \mathcal { A } } } d ( a , f ) .
$$

If there exists $a ^ { * }$ in $\mathscr { A }$ such that this bound on the distance is achieved, then there is nothing to prove. Otherwise there is a sequence $\{ a _ { i } ; i =$ $1 , 2 , \ldots \}$ of points in $\pmb { \mathcal { A } }$ which gives the limit

$$
\operatorname* { l i m } _ { i \to \infty } d ( a _ { i } , f ) = d ^ { \ast } .
$$

By compactness the sequence has at least one limit point in $\mathcal { A } , a ^ { + }$ say. Expression (1.6) and the definition of $a ^ { + }$ imply that, for any $\pmb \varepsilon > 0$ ,there exists an integer $\pmb { k }$ such that the inequalities

$$
d ( a _ { k } , f ) < d ^ { \ast } + { \textstyle \frac { 1 } { 2 } } \varepsilon
$$

and

$$
d ( a _ { k } , a ^ { + } ) < \frac { 1 } { 2 } \varepsilon
$$

are obtained. Hence the triangle inequality (1.1) provides the bound

$$
\begin{array} { c } { { d ( a ^ { + } , f ) \leqslant d ( a ^ { + } , a _ { k } ) + d ( a _ { k } , f ) } } \\ { { < d ^ { * } + \varepsilon . } } \end{array}
$$

Because $\pmb \varepsilon$ can be arbitrarily small, the distance $d ( a ^ { + } , f )$ is not greater than $d ^ { * }$ . Therefore $a ^ { + }$ is a best approximation.□

When $\pmb { \mathcal { A } }$ is not compact it is easy to find examples to show that best approximations may not exist. For instance, let $\mathcal { B }$ be the Euclidean space $\mathcal { R } ^ { 2 }$ and let $\pmb { \mathcal { A } }$ be the set of points that are strictly inside the unit circle. There is no best approximation to any point of $\mathcal { B }$ that is outside or on the unit circle.

# 1.3 Approximation in a normed linear space

The properties of metric spaces are not sufficiently strong for most of our work, so it is assumed that $\pmb { \mathcal { A } }$ and $f$ are contained in a normed linear space, which we call $\mathcal { B }$ also when we want to refer to it. The norm is a real-valued function $\| { \boldsymbol { x } } \|$ that is defined for all $\boldsymbol { x } \in \mathcal { B } ,$ Its properties are such that the function

$$
d ( x , y ) = \| x - y \|
$$

is suitable as a distance function. Therefore,by letting $z$ be zero in expression(1.1) and by reversing the sign of $\boldsymbol { y }$ , we may deduce the triangle inequality

$$
\| x + y \| \leq \| x \| + \| y \| .
$$

Moreover, the norm must satisfy the homogeneity condition

$$
\| \lambda x \| = \left| \lambda \right| \| x \|
$$

for all $x \in { \mathcal { B } }$ and for all scalars $\pmb { \lambda }$

The specialization from metric spaces to normed linear spaces does not exclude any of the approximation problems that we will consider. Therefore mostly we use the distance function (1.1O). It occurs naturally in the approximation calculations that are of practical interest, and it allows the existence of a best approximation to be proved when $\pmb { \mathcal { A } }$ is a linear space.

# Theorem 1.2

If $\mathscr { A }$ is a finite-dimensional linear space in a normed linear space ${ \mathcal { B } } .$ ，then,for every $f \in { \mathcal { B } } ,$ ，there exists an element of $\mathscr { A }$ that is a best approximation from $\mathscr { A }$ to $f .$

Proof. Let the subset $\mathcal { A } _ { 0 }$ contain the elements of $\pmb { \mathcal { A } }$ that satisfy the condition

$$
\left\| a \right\| \leqslant 2 \left\| f \right\| .
$$

It is compact because it is .a closed and bounded subset of a finitedimensional space. It is not empty: for example it contains the zero element. Therefore,by Theorem 1.1, there is a best approximation from $\mathcal { A } _ { 0 }$ to $f$ which we call $a _ { 0 } ^ { * }$ .By definition the inequality

$$
\| a - f \| \geqslant \| a _ { 0 } ^ { * } - f \| , \qquad a \in \mathcal { A } _ { 0 } ,
$$

holds.Alternatively,if the element $^ { a }$ is in $\mathscr { A }$ but is not in $\mathcal { A } _ { 0 }$ then, because condition (1.13) is not obtained we have the bound

$$
\begin{array} { r l } & { \| a - f \| \geqslant \| a \| { - } \| f \| } \\ & { ~ > \| f \| } \\ & { ~ \geqslant \| a _ { 0 } ^ { * } - f \| , } \end{array}
$$

where the last line makes further use of the fact that the zero element is in $\scriptstyle { \mathcal { A } } _ { 0 }$ .Hence expression (1.14) is satisfied for all $^ { a }$ in $\scriptstyle { \mathcal { A } } ,$ ， which proves that $a _ { 0 } ^ { * }$ is a best approximation.□

# 1.4 The $\mathbf { L } _ { p }$ -norms

In most of the approximation problems that we consider, $f$ and $\pmb { \mathcal { A } }$ are in the space ${ \mathcal { C } } [ a \ b ] ,$ ，which is the set of continuous real-valued functions that are defined on the interval $[ a , b ]$ of the real line. Occasion-ally we turn to discrete problems, where $f$ and $\mathscr { A }$ are in ${ \mathcal { R } } ^ { m }$ ,which is the set of real $^ { m }$ -component vectors. Both of these spaces are linear and we have a choice of norms.

We study the three norms that are used most frequently, namely the $L _ { p }$ -norms in the cases when $p = 1$ ,2 and $\infty$ . For finite $\pmb { p }$ the $L _ { p }$ -norm in

$\mathcal { C } [ \alpha , b ]$ is defined to have the value

$$
\| f \| _ { p } = { \biggl [ } \int _ { a } ^ { b } | f ( x ) | ^ { p } ~ \mathrm { d } x { \biggr ] } ^ { 1 / p } , \qquad 1 \leqslant p < \infty ,
$$

and in ${ \mathcal { R } } ^ { m }$ it has the value

$$
\| f \| _ { p } = { \biggl [ } \sum _ { i = 1 } ^ { m } | y _ { i } | ^ { p } { \biggr ] } ^ { 1 / p } , \qquad 1 \leqslant p < \infty ,
$$

where $\{ y _ { i } ; i = 1 , 2 , \dots , m \}$ are the components of $f .$ The $\infty$ -norms are the expressions

$$
\| f \| _ { \infty } = \operatorname* { m a x } _ { a \leqslant x \leqslant b } \left| f ( x ) \right|
$$

and

$$
\| f \| _ { \infty } = \underset { 1 \leqslant i \leqslant m } { \mathbf { m a x } } \left| y _ { i } \right|
$$

respectively.

There are excellent reasons for giving our attention to the 1-,2- and $\infty .$ -norms.The 1-norm is the least used of the three,but it has one remarkable property that makes it highly suitable for fitting to discrete data in the case when it is possible that there may be some gross errors in the data due to blunders. It is that the magnitude of a blunder makes no difference to the final approximation. This statement will be made clear in Chapter 14.Further,we find later that an understanding of the conditions that are obtained by best approximations in the 1-norm is necessary to analyse some error expressions that occur in the approximation of functionals.

The 2-norm,or perhaps a weighted 2-norm of the form

$$
\| f \| _ { 2 } = \left[ \int _ { a } ^ { b } w ( x ) | f ( x ) | ^ { 2 } { \mathrm { d } } x \right] ^ { \frac { 1 } { 2 } } ,
$$

where $w$ is a fixed positive function,occurs naturally in theoretical studies of Hilbert spaces. The practical reasons for considering the 2-norm are even stronger. Statistical considerations show that it is the most appropriate choice for data fitting when the errors in the data have a normal distribution. Moreover, when $\mathscr { A }$ is a linear space, the calculation of the best approximation in the 2-norm reduces to a system of linear equations,which allows highly efficient algorithms to be developed. Often the 2-norm is preferred because it is known that the best approximation calculation is straightforward to solve.

The $\infty$ -norm provides the foundation of much of approximation theory, for our next theorem shows that, if we succeed in finding an approximation $\pmb { a } \in \mathcal { A }$ such that the o-norm distance function $\pmb { d } ( f , \pmb { a } )$ is small, then the 2-norm and 1-norm distance functions are small also. However, an example that follows the theorem shows that the converse statement may not be true.A practical reason for using the $\infty \cdot$ -norm is that， when in computer calculations a complicated mathematical function, $f$ say, is estimated by one that is easy to calculate, $\pmb { p }$ say, then it is usually necessary to ensure that the greatest value of the error function $\{ | f ( x ) - p ( x ) | ; a \leqslant x \leqslant b \}$ is less than a fixed amount, which is just the required accuracy of the approximation. In other words we have.a condition on the norm $\| f - p \| _ { \infty }$

# Theorem 1.3

For all $^ e$ in ${ \mathcal { C } } [ a , b ]$ the inequalities

$$
\| e \| _ { 1 } \leqslant ( b - a ) ^ { \frac { 1 } { 2 } } \| e \| _ { 2 } \leqslant ( b - a ) \| e \| _ { \infty }
$$

hold.

Proof. The Cauchy-Schwarz inequality provides the bound

$$
\begin{array} { l } { \displaystyle \| e \| _ { 1 } = \int _ { a } ^ { b } \left| e \left( x \right) \right| \left| 1 \right| \mathrm { d } x } \\ { \displaystyle \leqslant \left[ \int _ { a } ^ { b } \left| e \left( x \right) \right| ^ { 2 } \mathrm { d } x \right] ^ { \frac { 1 } { 2 } } \left[ \int _ { a } ^ { b } \mathrm { d } x \right] ^ { \frac { 1 } { 2 } } } \\ { \displaystyle = ( b - a ) ^ { \frac { 1 } { 2 } } \| e \| _ { 2 } , } \end{array}
$$

which is the first part of the required result. Moreover, by replacing an integrand by its maximum value, we obtain the inequality

$$
\begin{array} { l } { \displaystyle \| e \| _ { 2 } = \Big [ \int _ { a } ^ { b } \big | e ( x ) \big | ^ { 2 } \mathrm { d } x \Big ] ^ { \frac { 1 } { 2 } } } \\ { \displaystyle \qquad \leqslant \Big [ \int _ { a } ^ { b } \| e \| _ { \infty } ^ { 2 } \mathrm { d } x \Big ] ^ { \frac { 1 } { 2 } } } \\ { \displaystyle \qquad = ( b - a ) ^ { \frac { 1 } { 2 } } \big \| e \big \| _ { \infty } , } \end{array}
$$

which completes the proof of the theorem.

It is interesting to consider the statement of Theorem 1.3, when $^ e$ is the error in approximating the constant function $\{ f ( x ) = 1 ; 0 \leqslant x \leqslant 1 \}$ by $\{ x ^ { \lambda } ; 0 \leqslant x \leqslant 1 \}$ ，where $\lambda$ is a positive parameter. Straightforward calculation shows that the norms have the values

$$
\begin{array} { l } { \| e \| _ { 1 } = \lambda / ( \lambda + 1 ) , } \\ { \| e \| _ { 2 } = [ 2 \lambda ^ { 2 } / ( \lambda + 1 ) ( 2 \lambda + 1 ) ] ^ { \frac { 1 } { 2 } } , } \end{array}
$$

and

$$
\| e \| _ { \infty } = 1 .
$$

We see that, if $\lambda$ becomes arbitrarily small, then $\| e \| _ { 1 }$ and $\left\| e \right\| _ { 2 }$ tend to zero,but $\| e \| _ { \infty }$ remains at one.Hence it is not always possible to reduce the $\infty$ -norm of an error function by making smallits 2-norm or its 1-norm. In order to develop algorithms that give approximations with small errors in the 1-, 2- and $\infty$ -norms,we just have to ensure that the algorithm is suitable for the $\infty$ -norm.

The $\infty$ -norm is sometimes called the uniform or minimax norm, and the 2-norm is sometimes called the least squares or Euclidean norm.

# 1.5 A geometric view of best approximations

In the case when $f$ and $\mathscr { A }$ are contained in a normed linear space $\mathcal { B }$ , and when we require a best approximation from $\mathscr { A }$ to $f ,$ it is sometimes helpful to think of the balls of different radii whose centres are at $f .$ The ball of radius $r$ is defined to be the set

$$
\mathcal { N } ( f , r ) \equiv \{ g \colon \| g - f \| \leqslant r , g \in \mathcal { B } \} .
$$

It follows that, if $r _ { 1 } > r _ { 0 } .$ ,then $\mathcal { N } ( f , r _ { 0 } ) \subset \mathcal { N } ( f , r _ { 1 } )$ Hence,if $f \notin { \mathcal { A } } ,$ and if $r$ is allowed to increase from zero there exists a scalar, $r ^ { * }$ say, such that, for $r > r ^ { * }$ ， there are points of $\mathcal { A }$ that are in $\mathcal { N } ( f , r )$ ，but, for $r < r ^ { * }$ ，the intersection of $\mathcal { N } ( f , r )$ and $\mathscr { A }$ is empty. The value of $r ^ { * }$ is equal to expression (1.5),and we know from Theorem 1.2 that, if $\mathcal { A }$ is a finitedimensional linear space, then the equation

$$
r ^ { * } = \operatorname* { i n f } _ { a \in { \mathcal { A } } } \left\| f - a \right\| = \left\| f - a ^ { * } \right\|
$$

is obtained for a point $a ^ { * }$ in $\mathcal { A }$

For example, suppose that $\mathcal { B }$ is the two-dimensional Euclidean space $\mathcal { R } ^ { 2 }$ ， and that we are using the 2-norm. Let $f$ be the point whose components are (2,1), and let $\mathscr { A }$ be the linear space of vectors

$$
{ \mathcal { A } } = \{ ( \lambda , \lambda ) ; - \infty < \lambda < \infty \} ,
$$

where $\lambda$ is a real parameter. Figure 1.4 shows the set $\mathscr { A }$ and the three balls, centre $f ,$ whose radii are $\scriptstyle { \frac { 1 } { 2 } }$ ， $\scriptstyle { \sqrt { \frac { 1 } { 2 } } }$ and 1. If we imagine that the value of $r$ is allowed to increase from zero, we see that the best approximation is the point where the ball of radius $\scriptstyle { \sqrt { \frac { 1 } { 2 } } }$ touches $\mathcal { A } .$

The shapes of balls in two-dimensional space for the 1-,2- and $\infty \cdot$ -norms are interesting, because they indicate some of the implications of the choice of norm. The boundaries of the three unit balls centred on the origin are shown in Figure 1.5.We note that,if the 2-norm is replaced by the 1-norm in Figure 1.4,and if the radius of the ball centred at $f$ is again allowed to increase from zero, then we find that many points of $\pmb { \mathcal { A } }$ are best approximations to $f .$ The question of the uniqueness of best approximations is considered in the next chapter.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0001_pages_0001-0070/auto/images/db364ccd1837a9f69728b8949d889110f05c2e7660277dfb47a12520588475af.jpg)  
Figure 1.4. An approximation problem in ${ \mathcal { R } } ^ { 2 }$

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0001_pages_0001-0070/auto/images/94e3a375c5fa7d2291968fd1f304832df65ec7f7d79671368cb90851afe30316.jpg)  
Figure 1.5. The unit bals of the 1-,2- and o-norms.

# 1 Exercises

1.1 Let $\scriptstyle { \mathcal { A } } _ { 0 }$ be a compact set and $\pmb { \mathcal { A } } _ { 1 }$ be a finite-dimensional linear space in a normed linear space ${ \mathcal { B } } .$ ，Prove that there exists $\pmb { a } _ { 0 } ^ { * }$ in $\scriptstyle { \mathcal { A } } _ { 0 }$ and $a _ { 1 } ^ { * }$ in $\mathcal { A } _ { 1 }$ such that the inequality

$$
\begin{array} { r } { \| \boldsymbol { a } _ { 0 } ^ { * } - \boldsymbol { a } _ { 1 } ^ { * } \| \leqslant \| \boldsymbol { a } _ { 0 } - \boldsymbol { a } _ { 1 } \| , \qquad \boldsymbol { a } _ { 0 } \in \mathcal { A } _ { 0 } , \qquad \boldsymbol { a } _ { 1 } \in \mathcal { A } _ { 1 } , } \end{array}
$$

is satisfied.

1.2 Let $\mathcal { B }$ be the set of bounded regions in two-dimensional space, whose shapes can be cut from a piece of flat card. For any pair of elements $\{ x , y \}$ of $\mathcal { B }$ ,let the number $d ( x , y )$ be the area of the union of $\pmb { x }$ and $y$ minus the area of the intersection of $\pmb { x }$ and $\pmb { y }$ Show that $d ( x , y )$ satisfies the axioms of a distance function.Let $\mathscr { A }$ be the set of triangular regions in two-dimensional space. Prove that every element of $\mathcal { B }$ has a best approximation in $\pmb { \mathcal { A } }$ with respect to the distance function $d ( x , y )$ ·

1.3 Let $\mathscr { A }$ be the set of straight lines in three-dimensional Euclidean space $\mathcal { R } ^ { 3 }$ . For any point $\pmb { x }$ in $\mathcal { R } ^ { 3 }$ and for any line $\pmb { a }$ in $\mathcal { A } ,$ let $d ( x , a )$ be the Euclidean distance from the point to the line.Let $\mathcal { S }$ be a set that contains a finite number of points of $\mathcal { R } ^ { 3 }$ .Prove that there exists an element $a ^ { * }$ in $\mathscr { A }$ that satisfies the inequality

$$
\operatorname* { m a x } _ { s \in \mathcal { S } } d ( a ^ { \ast } , s ) \leqslant \operatorname* { m a x } _ { s \in \mathcal { S } } d ( a , s ) , \qquad a \in \mathcal { A } .
$$

1.4 Prove that expression (1.16) satisfies the axioms of a norm in $\mathcal { C } [ \alpha , b ] ,$ when $p = 1$ ,2 and 4.

1.5 Let $\mathscr { A }$ be the set of real continuous functions on the interval $[ a , b ]$ that are composed of straight line segments.Hence $\pmb { \mathcal { A } }$ is a subspace of $\mathcal { C } [ \alpha , b ]$ .Prove that, for any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ and for any positive number $\pmb \varepsilon$ ， there exists an element $^ { a }$ in $\pmb { \mathcal { A } }$ such that $\| f - \pmb { a } \| _ { \infty }$ is less than $\pmb \varepsilon$ ,where the $\infty$ -norm is defined by equation (1.18). It follows that in general there is not a best approximation from $\pmb { \mathcal { A } }$ to $f$ with respect to the $\infty$ -norm.

1.6 Let $\left\| f \right\| _ { 1 }$ and $\| f \| _ { 2 }$ be the 1-norm and 2-norm respectively of a function $f$ in $\mathcal { C } [ \alpha , b ]$ . Construct an example to show that the ratio $\left\| f \right\| _ { 2 } / \left\| f \right\| _ { 1 }$ can be arbitrarily large.

1.7 What point of the plane $3 x + 2 y + z - 6 = 0$ in three-dimensional space is closest to the origin when distance is measured by each of the following three norms: (1) the 1-norm, (ii) the 2-norm,and (iii) the $\infty$ -norm.

1.8 The set $\mathscr { A }$ is composed of the functions $f$ in $\mathcal { C } [ 0 , 1 ]$ that have the form

$$
f ( x ) = ( c _ { 0 } + c _ { 1 } x ) / ( c _ { 2 } + c _ { 3 } x ) , \qquad 0 \leqslant x \leqslant 1 ,
$$

where $c _ { 0 } , \ c _ { 1 } , \ c _ { 2 }$ and $\pmb { c _ { 3 } }$ are real coefficients such that the denominator $\{ c _ { 2 } + c _ { 3 } x ; 0 \leqslant x \leqslant 1 \}$ is strictly positive.Let $\mathcal { S }$ be a set of points from [0,1],and let $f$ be a function in $\mathcal { C } [ 0 , 1 ]$ . Show that sometimes there is no element $a ^ { * }$ in $\mathscr { A }$ that satisfies the condition

$$
\operatorname* { m a x } _ { x \in \mathcal { S } } \big | f ( x ) - a ^ { * } ( x ) \big | \leqslant \operatorname* { m a x } _ { x \in \mathcal { S } } \big | f ( x ) - a ( x ) \big | , \qquad a \in \mathcal { A } .
$$

1.9 Let $\mathscr { A }$ be the set that is defined in Exercise 1.8. Prove that every function $f$ in $\mathcal { C } [ 0 , 1 ]$ has a best approximation in $\scriptstyle { \mathcal { A } }$ , with respect to the $\infty$ -norm distance function.

1.10 Let $\mathscr { A }$ be a finite-dimensional linear subspace of $\mathcal { C } [ 0 , 1 ]$ let $f$ be any function from $\mathcal { C } [ 0 , 1 ] ,$ , and,for all positive integers $\pmb { p }$ ,let $a _ { p }$ be an element of $\mathcal { A }$ that minimizes the $\pmb { p }$ -norm

$$
\| f - a \| _ { p } = \bigg [ \int _ { 0 } ^ { 1 } | f ( x ) - a ( x ) | ^ { p } \mathrm { d } x \bigg ] ^ { 1 / p } , \qquad a \in \mathcal { A } .
$$

Investigate whether the sequence of functions $\{ a _ { p } ; p =$ $1 , 2 , 3 , \ldots \}$ converges to a function that is the best approximation from $\mathscr { A }$ to $f$ with respect to the $\infty$ -norm. This sequence gives ‘Polya's algorithm'.

#

# The uniqueness of best approximations

# 2.1 Convexity conditions

In order to approximate a point or a function $f$ by an element of a set $\scriptstyle { \mathcal { A } } ,$ it is usual to choose conditions that define a particular approximation.Best approximation with respect to an appropriate distance function is often suitable, but sometimes there are several best approximations. Some general conditions for uniqueness are given in this chapter, that depend on the convexity of the distance function and the convexity of the set $\mathcal { A } .$ Hence it is shown that in many important cases the best approximation is unique,including best approximation with respect to the 2-norm when $\mathscr { A }$ is a linear space.We find, however, that, if the 1-norm or $\infty$ -norm is used, then stronger conditions are required on $\mathcal { A }$ in order to ensure uniqueness.

The set $\mathcal { S }$ of a linear space is convex if, for all $\pmb { s } _ { 0 }$ and ${ \pmb S } _ { 1 }$ in ${ \mathcal { S } } ,$ the points $\{ \theta s _ { 0 } + ( 1 - \theta ) s _ { 1 }$ ； $0 < \theta < 1 \}$ are also in ${ \mathcal { S } } .$ The set is strictly convex if, for all $s _ { 0 } \neq s _ { 1 }$ , the points $\{ \theta s _ { 0 } + ( 1 - \theta ) s _ { 1 }$ $0 < \theta < 1 \}$ are interior points of $\mathcal { S } .$ Thus, it is not possible for the boundary of a strictly convex set to contain a segment of a straight line.The nature of the ideas that are studied in this chapter is suggested by considering the uniqueness of the best approximation if the circles in Figure 1.4 are replaced by balls that are derived from some other norm.Our next theorem shows that these balls are convex sets.

# Theorem 2.1

Let $\mathcal { B }$ be a normed linear space. Then, for any $f \in { \mathcal { B } }$ and for any $r > 0$ , the ball

$$
\mathcal { N } ( f , r ) = \{ { x } { : \| { x - f } \| } { \leqslant } r , { x } { \in } \mathcal { B } \}
$$

is convex.

Proof. Let $\scriptstyle { \pmb { x } } _ { 0 }$ and $x _ { 1 }$ be in $\mathcal { N } ( f , r )$ . Then the axioms of a norm and the definition (2.1) give the bound

$$
\begin{array} { r l } { \left\| { \theta x _ { 0 } + ( 1 - \theta ) x _ { 1 } - f } \right\| \leqslant \left\| { \theta x _ { 0 } - \theta f } \right\| + \left\| { ( 1 - \theta ) x _ { 1 } - ( 1 - \theta ) f } \right\| } & { } \\ { = \left| { \theta } \right| \left\| { x _ { 0 } - f } \right\| + \left| { 1 - \theta } \right| \left\| { x _ { 1 } - f } \right\| } & { } \\ { \leqslant r \{ \left| { \theta } \right| + \left| { 1 - \theta } \right| \} } & { } \\ { = r , 0 < \theta < 1 , } \end{array}
$$

which is the required convexity condition.

It is now easy to prove one of the basic properties of best approximations，which depends on the convexity of the set of approximating functions. This convexity condition holds,of course, when $\mathscr { A }$ is a linear space.

# Theorem 2.2

Let $\mathscr { A }$ be a convex set in a normed linear space $\mathcal { B }$ , and let $f$ be any point of $\mathcal { B }$ such that there exists a best approximation from $\mathscr { A }$ to $f .$ Then the set of best approximations is convex.

Proof. Let $h ^ { * }$ be the error of the best approximation

$$
h ^ { * } = \operatorname* { m i n } _ { a \in { \mathcal { A } } } \| a - f \| .
$$

The set of best approximations is the intersection of $\mathscr { A }$ and the ball $\mathcal { N } ( f , h ^ { * } )$ . The theorem follows from the fact that the intersection of two convex sets is convex.□

The uniqueness theorems of the next section require either $\boldsymbol { \mathcal { A } }$ or the norm of the linear space $\mathcal { B }$ to be strictly convex. The norm is defined to be strictly convex if and only if the unit ball centred on the origin, namely ${ \mathcal { N } } ( 0 , 1 )$ , is strictly convex. Because the general ball (2.1) can be obtained from ${ \mathcal { N } } ( 0 , 1 )$ by translation and magnification, strict convexity of the norm implies that the set (2.1) is strictly convex for any $f$ and $r .$

# 2.2 Conditions for uniqueness of the best approximation

The two uniqueness theorems that are given below are selfevident if one takes the geometric view of best approximation that is described in Section 1.5.We recall that a ball with centre $f$ is allowed to grow until it touches the set $\mathscr { A }$ of approximating functions,and then the radius of the ball has the value (2.3).The two theorems state that there is only one point of contact between $\mathscr { A }$ and $\mathcal { N } ( f , h ^ { * } )$ , if the boundary of either $\mathscr { A }$ or $\mathcal { N } ( f , h ^ { * } )$ is curved,and if both sets are convex.

# Theorem 2.3

Let $\mathscr { A }$ be a compact and strictly convex set in a normed linear space $\mathcal { B }$ Then,for all $f \in { \mathcal { B } }$ ,there is just one best approximation from $\pmb { \mathcal { A } }$ to $f .$

Proof. Theorem 1.1 shows that there is a best approximation. We continue to let $h ^ { * }$ be the error (2.3). Suppose that $\pmb { s _ { 0 } }$ and ${ \pmb S } _ { 1 }$ are different best approximations from $\mathscr { A }$ to $f .$ Because the triangle inequality for norms gives the condition

$$
\begin{array} { r } { \| \frac { 1 } { 2 } ( s _ { 0 } + s _ { 1 } ) - f \| \leqslant \frac { 1 } { 2 } \| s _ { 0 } - f \| + \frac { 1 } { 2 } \| s _ { 1 } - f \| , } \end{array}
$$

and because $\mathscr { A }$ is convex, it follows that $\textstyle { \frac { 1 } { 2 } } ( s _ { 0 } + s _ { 1 } )$ is also a best approximation,and therefore it satisfies the equation

$$
\left\| { \frac { 1 } { 2 } } { \big ( } s _ { 0 } + s _ { 1 } { \big ) } - f \right\| = h ^ { * } .
$$

We let $\pmb { \lambda }$ be the largest number in the interval $0 \leqslant \lambda \leqslant 1$ such that the point

$$
s = { \scriptstyle { \frac { 1 } { 2 } } } ( s _ { 0 } + s _ { 1 } ) + \lambda \left[ f - { \frac { 1 } { 2 } } ( s _ { 0 } + s _ { 1 } ) \right]
$$

is in $\mathcal { A } .$ The value of $\lambda$ is well-defined because $\mathcal { A }$ is compact. Expressions (2.5) and (2.6) imply the equation

$$
\left\| s - f \right\| = ( 1 - \lambda ) h ^ { * } .
$$

However, $h ^ { * }$ is positive because otherwise $\scriptstyle s _ { 0 } = f = s _ { 1 }$ ,and $\lambda$ is positive because the strict convexity of $\mathscr { A }$ implies that $\textstyle { \frac { 1 } { 2 } } ( s _ { 0 } + s _ { 1 } )$ is an interior point of $\mathcal { A } .$ It therefore follows from equation (2.7) that $\| s - f \|$ is less than $h ^ { * }$ This contradiction proves the theorem.□

# Theorem 2.4

Let $\mathscr { A }$ be a convex set in a normed linear space $\mathscr { B }$ ,whose norm is strictly convex. Then, for all $f \in { \mathcal { B } } _ { \mathrm { : } }$ , there is at most one best approximation from $\mathscr { A }$ to $f .$

Proof. Suppose that $\pmb { s } _ { 0 }$ and ${ \pmb S } _ { 1 }$ are different best approximations from $\pmb { \mathcal { A } }$ to $f .$ Because the strict convexity of the norm implies that the set $\mathcal { N } ( f , h ^ { * } )$ is strictly convex, the point $\textstyle { \frac { 1 } { 2 } } ( s _ { 0 } + s _ { 1 } )$ is an interior point of $\mathcal { N } ( f , h ^ { * } )$ ,which is the condition

$$
\left\| { \frac { 1 } { 2 } } { \big ( } s _ { 0 } + s _ { 1 } { \big ) } - f \right\| < h ^ { * } .
$$

This is a contradiction, however, because $\begin{array} { r } { \frac { 1 } { 2 } ( s _ { 0 } + s _ { 1 } ) \in \mathcal { A } . } \end{array}$ The theorem is proved.□

Theorem 2.4 is much more useful to us than Theorem 2.3, because our sets of approximating functions are finite-dimensional linear subspaces.

Therefore it is important to know whether the norm of $\mathcal { B }$ is strictly convex. It is proved in Section 2.4 that the 2-norms in ${ \mathcal { C } } [ a , b ]$ and in ${ \mathcal { R } } ^ { n }$ are strictly convex, but that the 1- and $\infty$ -norms are not. In fact all the $p$ -norms are strictly convex for $1 < p < \infty$

# 2.3 The continuity of best approximation operators

When there is a unique best approximation from $\mathscr { A }$ to $f$ for all $f \in { \mathcal { B } }$ ， we can regard the best approximation as a function of $f .$ Hence there is a best approximation operator from $\mathcal { B }$ to $\mathcal { A } ,$ which we call $X ,$ and which, incidentally, must be a projection.It is shown in this section that often the operator $\pmb { X }$ is continuous. This result is important to computer calculations,because,if it does not hold, then the effect of computer rounding errors in the definition of $f$ may cause substantial changes to the calculated approximation.

# Theorem 2.5

Let $\mathscr { A }$ be a compact set in a metric space $\mathcal { B }$ , such that for every $f$ in $\mathcal { B }$ there is only one best approximation in $\mathcal { A }$ ， $X ( f )$ say. Then the operator $X ,$ ,defined by the best approximation condition, is continuous.

Proof.If the theorem is false, there exists a sequence of points $\{ f _ { i } ; i =$ $1 , 2 , 3 , \ldots \}$ in $\mathcal { B }$ that converges to a limit, $f$ say, such that the sequence $\{ X ( f _ { i } ) ; \ i = 1 , 2 , 3 , . . . \}$ in $\mathscr { A }$ fails to converge to $X ( f )$ . Therefore, by compactness, the second sequence has a limit point, $a ^ { * }$ say, that is in $\mathscr { A }$ but that is not equal to $X ( f )$ . It suffices to show that both $a ^ { * }$ and $X ( f )$ are best approximations to $f ,$ for then we have a contradiction that proves the theorem.

Therefore we consider the distance $d ( a ^ { * } , f )$ ， and, by applying the triangle inequality (1.1) twice, we deduce the bound

$$
d ( a ^ { \ast } , f ) \leq d ( a ^ { \ast } , X ( f _ { i } ) ) + d ( X ( f _ { i } ) , f _ { i } ) + d ( f _ { i } , f ) .
$$

Moreover, the definition of $X ( f _ { i } )$ gives the relation

$$
\begin{array} { l } { { d ( X ( f _ { i } ) , f _ { i } ) \leqslant d ( X ( f ) , f _ { i } ) } } \\ { { \qquad \leqslant d ( X ( f ) , f ) + d ( f , f _ { i } ) , } } \end{array}
$$

where the last line makes use of the triangle inequality again. Now, for any $\pmb \varepsilon > 0$ , there exists $i$ such that the conditions

$$
d ( a ^ { * } , X ( f _ { i } ) ) \leqslant \frac { 1 } { 3 } \varepsilon
$$

and

$$
\begin{array} { r } { d ( f _ { i } , f ) \leqslant \frac { 1 } { 3 } \varepsilon } \end{array}
$$

hold. It follows from expressions (2.9) and (2.10) that the bound

$$
d ( a ^ { \ast } , f ) \leq d ( X ( f ) , f ) + \varepsilon
$$

is obtained. Since $\pmb \varepsilon$ can be arbitrarily small, $a ^ { * }$ is a best approximation from $\scriptstyle { \mathcal { A } }$ to $f ,$ which is the required contradiction.□

By applying the technique that is used in the proof of Theorem 1.2, it can be shown that the following theorem is true also. The proof is left as an exercise.

# Theorem 2.6

If $\mathscr { A }$ is a finite-dimensional linear space in a normed linear space ${ \mathcal { B } } .$ ， such that for every $f$ in $\mathcal { B }$ there is only one best approximation in $\scriptstyle { \mathcal { A } }$ ， $X ( f )$ say,then the operator $X ,$ ，defined by the best approximation condition, is continuous.□

The last theorem is directly relevant to the approximation problems that are studied in later chapters. Note that it provides additional motivation for giving attention to the uniqueness of best approximations.

# 2.4 The 1-, 2- and o-norms

The method that we use to prove that the 2-norm is strictly convex in $\mathcal { C } [ \alpha , b ]$ and ${ \mathcal { R } } ^ { n }$ makes use of scalar products. It is well known that the scalar product of $y$ and $z$ in ${ \mathcal { R } } ^ { n }$ has the value

$$
( y , z ) = \sum _ { i = 1 } ^ { n } y _ { i } z _ { i } ,
$$

and in $\mathcal { C } [ \alpha , b ]$ the scalar product of the functions $f$ and $\pmb { g }$ is the expression

$$
( f , g ) = \int _ { a } ^ { b } f ( x ) g ( x ) \mathrm { d } x .
$$

It is important to note that $( f , f )$ is equal to $\| \ b { f } \| _ { 2 } ^ { 2 }$ Further, the identity

$$
\left\| f + g \right\| _ { 2 } ^ { 2 } = \left\| f \right\| _ { 2 } ^ { 2 } + 2 ( f , g ) + \left\| g \right\| _ { 2 } ^ { 2 }
$$

is obtained, either when $f$ and $\pmb { g }$ are in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ,or when they are in ${ \mathcal { R } } ^ { n }$ .In fact it holds for all Hilbert spaces, but, if the reader has not met Hilbert spaces before, it is sufficient for him to recognise that equation (2.16) is valid both for ${ \mathcal { C } } [ a , b ]$ and for ${ \mathcal { R } } ^ { n }$ . We note also that the scalar product $( f , g )$ is linear in $f$ and in $\pmb { g }$

# Theorem 2.7

The 2-norm of the linear space $\mathcal { B }$ is strictly convex when $\mathcal { B }$ is either ${ \mathcal { C } } [ a , b ]$ or ${ \mathcal { R } } ^ { n }$

Proof. We let $f$ and $\pmb { g }$ be any two distinct points of $\mathscr { B }$ such that $\| f \| _ { 2 } = \| g \| _ { 2 } = 1$ . It is sufficient to prove that the bound

$$
\| \pmb { \theta } f + ( 1 - \theta ) \pmb { g } \| _ { 2 } < 1
$$

is satisfied for all $0 < \theta < 1$ . The identity

$$
\begin{array} { r l } & { \| \theta f + ( 1 - \theta ) g \| _ { 2 } ^ { 2 } + \theta ( 1 - \theta ) \| f - g \| _ { 2 } ^ { 2 } } \\ & { \quad = \theta ^ { 2 } + 2 \theta ( 1 - \theta ) ( f , g ) + ( 1 - \theta ) ^ { 2 } + \theta ( 1 - \theta ) [ 1 - 2 ( f , g ) + 1 ] } \\ & { \quad = 1 , } \end{array}
$$

which holds for all values of $\pmb \theta .$ ， gives the required inequality (2.17).[

It has been stated already that the 1-and $\infty \cdot$ -norms in $\mathcal { C } [ \alpha , b ]$ and in ${ \mathcal { R } } ^ { n }$ are not strictly convex, and now this statement is proved. We also wish to find out whether best approximations from linear subspaces are always unique. If we prove first that the norms are not strictly convex, then Theorem 2.4 does not answer the uniqueness question. If instead, however, we can demonstrate that a best approximation from a linear subspace of a normed linear space is not unique, then we may deduce from Theorem 2.4 that the norm is not strictly convex. We give examples of this kind. In each one there is a linear subspace $\pmb { \mathcal { A } }$ and a point $f$ such that the best approximation from $\pmb { \mathcal { A } }$ to $f$ is not unique, where $\pmb { \mathcal { A } }$ and $f$ are contained in either $\mathcal { C } [ \alpha , b ]$ or in ${ \mathcal { R } } ^ { n }$ ，and where the accuracy of the approximation is measured either by the 1-norm or by the $\infty \cdot$ -norm.

When the 1-norm is used in $\mathcal { C } [ - 1$ ,1], we let $f$ be the constant function whose value is one,and we let $\pmb { \mathcal { A } }$ be the one-dimensional linear space that contains all functions of the form

$$
a ( x ) = \lambda x , \qquad - 1 \leqslant x \leqslant 1 ,
$$

where $\pmb { \lambda }$ is a parameter. It is straightforward to derive the equation

$$
\operatorname* { m i n } _ { a \in \mathcal { A } } \int _ { - 1 } ^ { 1 } \left| f ( x ) - a ( x ) \right| \mathrm { d } x = 2 ,
$$

and to show that the minimum value is obtained when $\pmb { \lambda }$ is in the range $- 1 \leqslant \lambda \leqslant 1$ . Hence the best approximation is not unique.

This example for the 1-norm is extended to ${ \mathcal { R } } ^ { n }$ $( n \geqslant 2 )$ by dividing the interval [-1,1] by the points $- 1 = x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { n } = 1$ ，which are equally spaced

$$
x _ { i + 1 } - x _ { i } = 2 / ( n - 1 ) , \qquad i = 1 , 2 , \ldots , n - 1 .
$$

We evaluate the function $f$ that we had before at these points to give a vector $f \in \mathcal { R } ^ { n }$ .Moreover, corresponding to equation (2.19), we let ${ \pmb a } \in$ ${ \mathcal { A } } \subset { \mathcal { R } } ^ { n }$ be the vector whose components have the values

$$
a _ { i } = \lambda x _ { i } , \qquad i = 1 , 2 , \ldots , n ,
$$

where $\pmb { \lambda }$ is still a parameter. Now, instead of equation (2.20), we find the expression

$$
\operatorname* { m i n } _ { a \in \mathcal { A } } \sum _ { i = 1 } ^ { n } \left| f _ { i } - a _ { i } \right| = n ,
$$

and again the minimum value is obtained for all values of $\pmb { \lambda }$ in the range $- 1 \leqslant \lambda \leqslant 1$

For the $\infty$ -norm in $\mathcal { C } [ - 1 , 1 ]$ ,we again let $f$ be the constant function whose value is one, but now we let $\pmb { \mathcal { A } }$ be the one-dimensional linear space that contains functions of the form

$$
a ( x ) = \lambda ( 1 + x ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

We deduce the equation

$$
\operatorname* { m i n } _ { a \in \mathcal { A } } \| f - a \| _ { \infty } = 1 ,
$$

and we find that the function (2.24) is a best approximation if and only if $\pmb { \lambda }$ satisfies the condition

$$
0 \leqslant \lambda \leqslant 1 .
$$

Hence we have non-uniqueness once more. We extend the example to ${ \mathcal { R } } ^ { n }$ in the way described in the previous paragraph.The components of $f \in \mathcal { R } ^ { n }$ are the same as before, but, because of equation (2.24), the components of $\pmb { a } \in \mathcal { A }$ have the values

$$
a _ { i } = \lambda ( 1 + x _ { i } ) , \qquad i = 1 , 2 , \ldots , n ,
$$

instead of the values (2.22). The range of values of $\pmb { \lambda }$ that give a best approximation from $\pmb { \mathcal { A } }$ to $f$ is still the range (2.26).

The reader is advised to draw figures that show the non-uniqueness of the best approximation in these four examples. It should be noted also that the examples illustrate the usefulness of Theorem 2.2.

In many important cases, in particular when the normed linear space is $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ,when the norm is either the 1-norm or the $\infty$ -norm,and when $\pmb { \mathcal { A } }$ is the space $\mathcal { P } _ { n }$ of algebraic polynomials of degree at most $\pmb { n }$ , then the best approximation is unique for all $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .This statement is proved later. The purpose of the examples, therefore, is to show that, if $\pmb { \mathcal { A } }$ is a linear subspace of a normed linear space,whose norm is not strictly convex, then the uniqueness of best approximations depends on properties of $\pmb { \mathcal { A } }$ and $f .$

# 2 Exercises

2.1 Let $\pmb { \mathcal { A } }$ be a closed, bounded convex set of a linear space $\mathcal { B }$ ,such that the zero element is an interior point of $\mathcal { A } ,$ ,and such that if $f \in \mathcal A$ then $- f \in { \mathcal { A } } .$ ，Show that the following definition of Ill satisfies the axioms of a norm. If $f$ is the zero element we let $\left\| f \right\| = 0$ ,and otherwise we let $\| f \|$ be the smallest positive number such that $f / \| f \|$ is in the set $\mathcal { A }$

2.2 Prove Theorem 2.6.

2.3 Prove that the norm

$$
\| f \| _ { 4 } = { \biggl [ } \int _ { a } ^ { b } | f ( x ) | ^ { 4 } \ \mathrm { d } x { \biggr ] } ^ { \frac { 1 } { 4 } } , \qquad f \in { \mathcal { C } } [ a , b ] ,
$$

is strictly convex.

2.4 Let $\mathcal { A }$ be the set $\{ a : \| a \| _ { 2 } \leqslant 1 \}$ in the two-dimensional space $\mathcal { R } ^ { 2 }$ ， but let the $\infty$ -norm be used as a distance function. Draw a diagram to show the best approximation in $\mathscr { A }$ to a general point in $\mathcal { R } ^ { 2 }$ . Verify that the best approximation operator from $\mathcal { R } ^ { 2 }$ to $\mathcal { A }$ is continuous.

2.5 Let $\mathcal { B }$ be a linear space that has a strictly convex norm,and that is such that the unit ball $\mathcal { A } = \{ a : \| a \| \leqslant 1 \}$ is compact. For any $f \in { \mathcal { B } }$ ， let $X ( f )$ be the best approximation from $\mathcal { A }$ to $f .$ Show that, if $> 1$ , then $X ( f )$ is the point $f / \| f \|$ . Hence prove that the operator $\boldsymbol { X }$ satisfies the continuity condition

$$
\begin{array} { r } { \| { \cal { X } } ( f _ { 1 } ) - { \cal { X } } ( f _ { 2 } ) \| \leqslant 2 \| f _ { 1 } - f _ { 2 } \| , } \end{array}
$$

where $f _ { 1 }$ and $f _ { 2 }$ are any two points of $\mathscr { B }$

2.6 By considering the approximation of the function $\{ f ( x ) = x$ ； $- \pi \leqslant x \leqslant \pi \}$ by a multiple of $\{ \sin ^ { 2 } x ; - \pi \leqslant x \leqslant \pi \}$ , show that the norm

$$
\| f \| = \int _ { - \pi } ^ { \pi } { \bigl | } f ( x ) { \bigr | } \mathrm { d } x + \operatorname* { m a x } _ { - \pi \leq x \leq \pi } { \bigl | } f ( x ) { \bigr | } , \qquad f \in \mathcal { C } [ - \pi , \pi ] ,
$$

is not strictly convex.

2.7 Let the set $\mathscr { A }$ in $\mathcal { C } [ - 1 , 1 ]$ contain the continuous functions that are each composed of one or two straight line segments. Show that there is more than one best approximation from $\mathscr { A }$ to the function $\{ f ( x ) = x ^ { 3 } ; - 1 \leqslant x \leqslant 1 \}$ ， with respect to the oo-norm.

Find a plane in $\mathcal { R } ^ { 3 }$ that has several closest points to the origin with respect to the 1-norm,and that also has several closest points to the origin with respect to the $\infty$ -norm.

2.9 Investigate the following hypothesis. If $\mathscr { A }$ is a compact set in a normed linear space $\mathcal { B }$ ,and if $\mathscr { A }$ is not convex, then there exists a point $f$ in $\mathcal { B }$ that has more than one best approximation in $\pmb { \mathcal { A } } .$

2.10 Let $\mathscr { A }$ be a compact and strictly convex set in a normed linear space ${ \mathcal { B } } .$ For any $\pmb { a }$ in $\mathcal { A } ,$ let $\mathcal { S } ( a )$ be the set of points in $\mathscr { B }$ such that $\pmb { s }$ is in $\mathcal { S } ( a )$ if and only if $^ { a }$ is the best approximation from $\pmb { \mathcal { A } }$ to s. Investigate general conditions that ensure that the set $\mathcal { S } ( a )$ is convex.

# Approximation operators and some approximating functions

# 3.1 Approximation operators

We continue to let $\pmb { \mathcal { A } }$ be a set of approximating functions in a normed linear space ${ \mathcal { B } } .$ . It was noted in Section 2.3 that if,for every $f$ in $\mathscr { B }$ ， there is a unique best approximation from $\pmb { \mathcal { A } }$ to $f , X ( f )$ say, then we may regard $\pmb { X }$ as an operator from $\mathscr { B }$ to ${ \mathcal { A } } .$ . We now take the more general point of view that $\pmb { X }$ is an approximation operator if it is any mapping from $\mathscr { B }$ to $\mathcal { A } .$

Nearly all numerical methods for calculating approximations are approximation operators. It is only necessary for the method to select a unique element of $\mathscr { A }$ as an approximation to any $f$ in $\mathcal { B }$ . We make this remark because it is helpful sometimes to relate some fundamental properties of operators to algorithms.

For example, some of the work of Chapter 17 concerns algorithms that possess the projection property. Therefore we note that the operator $\pmb { X }$ is defined to be a projection if the equation

$$
X [ X ( f ) ] = X ( f ) , \qquad f \in { \mathcal { B } } ,
$$

is satisfied. Hence a sufficient condition for $\pmb { X }$ to be a projection is the equation

$$
X ( a ) = a , \qquad a \in { \mathcal { A } } .
$$

Most of the approximation methods that are considered in this book do satisfy condition (3.2)，but an important exception is the Bernstein operator，which is discussed in Chapter 6.Sometimes $X ( f )$ is written as $X f .$

The idea of a linear operator is also well known; namely, we define $\pmb { X }$ to be linear if the equation

$$
X ( \lambda f ) = \lambda X ( f )
$$

holds for all $f \in { \mathcal { B } }$ ,where $\pmb { \lambda }$ is any real number,and if the equation

$$
X ( f + g ) = X ( f ) + X ( g )
$$

is obtained for all $f \in { \mathcal { B } }$ and for all $g \in \mathcal { B }$ .Usually, when $\pmb { X }$ is linear and when $\mathscr { A }$ is a finite-dimensional linear space, the calculation of $X ( f )$ reduces to the solution of a system of linear equations. For example, we find in Chapter 11 that this case occurs when $X ( f )$ is the best approximation to $f$ with respect to the 2-norm. However, if $X ( f )$ is the best approximation in the 1-norm or $\infty$ -norm, then $\pmb { X }$ is hardly ever a linear operator.

Also we make frequent use of the norm of an approximation operator. The norm of $\pmb { X }$ is written as $\| X \| ,$ , and it is the smallest real number such that the inequality

$$
\| X ( f ) \| \leqslant \| X \| \| f \|
$$

holds for all $f \in { \mathcal { B } }$ . The notation $\| X \| _ { p }$ indicates that $\| X \|$ is derived from $\| f \| _ { p }$

An example of an approximation operator that is useful because it is easy to apply is as follows. Let $\mathcal { B }$ be the space $\mathcal { C } [ 0 , 1 ]$ of real-valued functions that are continuous on [O, 1],and let $\mathscr { A }$ be the linear space $\mathcal { P } _ { 1 }$ of all real polynomials of degree at most one. Then, in order that the calculation of an approximation to a function $f$ in $\mathcal { B }$ depends on only two function evaluations,we let $p$ be the polynomial in $\mathscr { A }$ that satisfies the interpolation conditions

$$
\left. \begin{array} { c } { { p ( 0 ) = f ( 0 ) } } \\ { { p ( 1 ) = f ( 1 ) } } \end{array} \right\} .
$$

Thus $p = X ( f )$ ,where $\pmb { X }$ is a linear projection operator from $\mathscr { B }$ to $\mathcal { A }$

In order to define the norm of this operator we choose a norm for the space $\mathcal { C } [ 0 , 1 ]$ .However, if the 2-norm

$$
\| f \| _ { 2 } = \left\{ \int _ { 0 } ^ { 1 } { [ f ( x ) ] ^ { 2 } } \mathrm { d } x \right\} ^ { \frac { 1 } { 2 } } , \qquad f \in { \mathcal { C } } [ 0 , 1 ] ,
$$

is used, we find that the operator $\pmb { X }$ is unbounded, because it is possible for $\| X f \| _ { 2 }$ to be one when $\left\| f \right\| _ { 2 }$ is arbitrarily small It is therefore necessary to prefer the $\infty$ -norm

$$
\| f \| _ { \infty } = \operatorname* { m a x } _ { 0 \leqslant x \leqslant 1 } | f ( x ) | , \qquad f \in \mathcal { C } [ 0 , 1 ] ,
$$

when considering approximation operators that are defined by

interpolation conditions. In this case, because $\pmb { p }$ is in $\mathcal { P } _ { 1 }$ ,equation (3.6) implies the inequality

$$
\begin{array} { r l } & { \| X ( f ) \| = \| p \| } \\ & { \qquad = \operatorname* { m a x } \left[ | p ( 0 ) | , | p ( 1 ) | \right] } \\ & { \qquad = \operatorname* { m a x } \left[ | f ( 0 ) | , | f ( 1 ) | \right] } \\ & { \qquad \leqslant \| f \| , \qquad f \in \mathcal { C } [ 0 , 1 ] . } \end{array}
$$

Hence the value of $\| X \|$ is at most one. Because the function $\{ f ( x ) = 1 ; 0 \leqslant$ $x \leqslant 1 \}$ shows that $\| X \|$ is at least one, it follows that the norm of the approximation operator is equal to one. The norms of several other operators are calculated later, and the work of the next section gives one reason why they are important.

# 3.2 Lebesgue constants

The norm of an approximation operator is sometimes called the Lebesgue constant of the operator. In particular this term is used when one compares the error of a calculated approximation with the smallest error that can be achieved. The next theorem shows that the value of the norm is of direct relevance to this comparison.

# Theorem 3.1

Let $\mathscr { A }$ be a finite-dimensional linear subspace of a normed linear space $\mathcal { B }$ ,and let $\pmb { X }$ be a linear operator from $\mathcal { B }$ to $\scriptstyle { \mathcal { A } }$ that satisfies the projection condition (3.2). For any $f$ in $\mathcal { B }$ ,let $d ^ { * }$ be the least distance

$$
d ^ { * } = \operatorname* { m i n } _ { a \in { \mathcal { A } } } \left\| f - a \right\|
$$

from $f$ to an element of ${ \mathcal { A } } .$ Then the error of the approximation $X ( f )$ satisfies the bound

$$
\left\| f - X ( f ) \right\| \leqslant [ 1 + \| X \| ] d ^ { * } .
$$

Proof. Let $p ^ { * }$ be a best approximation from $\mathscr { A }$ to $f ,$ which is shown to exist by Theorem 1.2. The projection condition (3.2) and the linearity of $X$ give the equation

$$
f - X ( f ) = ( f - p ^ { * } ) - X ( f - p ^ { * } ) .
$$

It follows from the triangle inequality for norms, and from the definitions of $\| X \|$ and $p ^ { * }$ , that the bound

$$
\begin{array} { r l } & { \| f - X ( f ) \| \leqslant \| f - p ^ { * } \| + \| X ( f - p ^ { * } ) \| } \\ & { \qquad \leqslant [ 1 + \| X \| ] \| f - p ^ { * } \| } \\ & { \qquad = [ 1 + \| X \| ] d ^ { * } } \end{array}
$$

is obtained, which is the required result.

If we apply this theorem to the example given in Section 3.1, where $p = X ( f )$ is the linear polynomial that satisfies the conditions (3.6), then we find the bound

$$
\left\| f - X ( f ) \right\| _ { \infty } \leqslant 2 \displaystyle \operatorname* { m i n } _ { p \in { \mathcal P } _ { 1 } } \left\| f - p \right\| _ { \infty } .
$$

Hence the maximum error of .the approximation from $\mathcal { P } _ { 1 }$ to $f$ that is defined by the interpolation conditions (3.6) is never more than twice the least maximum error that can be achieved.Results of this kind often show that the extra work of calculating best approximations is not worthwhile.

If the interpolation method (3.6) is applied to the function

$$
f ( x ) = x ^ { 2 } , \qquad 0 \leqslant x \leqslant 1 ,
$$

then the calculated approximation is the polynomial $\{ p ( x ) = x ; 0 \leqslant x \leqslant$ 1},while the approximation that minimizes the $\infty$ -norm of the error is the function $\{ p ^ { * } ( x ) = x - { \frac { 1 } { 8 } }$ ， $0 \leqslant x \leqslant 1 \}$ . This example shows that expression (3.11) can be satisfied as an equality.

One useful application of Theorem 3.1 is to the case when one requires a polynomial approximation $\pmb { p }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the condition

$$
\| f - p _ { 1 } \| _ { \infty } \leqslant \varepsilon ,
$$

where $\pmb \varepsilon$ is a given positive number. The degree of the polynomial is not specified, but it should not be much larger than necessary. Let $\mathscr { A }$ be the space $\mathcal { P } _ { n }$ of polynomials of degree at most $\pmb { n }$ ，and let $\pmb { X }$ be a linear operator from $\mathcal { C } [ a , b ]$ to $\mathscr { A }$ that satisfies condition (3.2). If $X ( f )$ is calculated,and if it is found that at a point of the range $[ a , b ]$ the modulus of the error function $[ f - X ( f ) ]$ is larger than $[ 1 + \| X \| _ { \infty } ] \varepsilon$ ,then it follows from Theorem 3.1 that the degree of $p$ must exceed $\pmb { n }$ .Hence it is possible sometimes to derive useful information about best approximations from simple algorithms.Therefore,when we consider practical algorithms that are linear projections, we usually give some attention to the norm of the approximation operator.

# 3.3 Polynomial approximations to differentiable functions

Much of the work of this book is given to approximation by polynomials. One could try to justify this specialization by the wellknown Weierstrass theorem. It is proved in Chapter 6,and it states that, for any $f$ in $\mathcal { C } [ a , b ]$ and for anv $\pmb \varepsilon > 0$ ,there exists an algebraic polynomial $\pmb { p }$ that satisfies the condition

$$
\| f - p \| _ { \infty } \leqslant \varepsilon .
$$

Sometimes, however, the degree of $\pmb { p }$ has to be so large that the polynomial is not a useful approximation in practice.Therefore there are other reasons for giving so much attention to polynomials. One is that polynomials show nicely the properties of best approximations in the 1-, 2- and $\infty$ -norms that help the numerical methods of calculation. Moreover, the theoretical work of the subject provides several techniques of analysis that can be used sometimes in new applications. One of these techniques is shown in this section, because it is instructive to compare it with the use that was made of equation (3.12) in the proof of Theorem 3.1. The result that is obtained shows that the adequacy of polynomial approximations depends on the differentiability properties of the function that is being approximated.

In order to give this result, we introduce some more notation,and we accept some assertions that are proved later. We take from Chapter 7 the statement that the best approximation in the $\infty$ -norm from the space $\mathcal { P } _ { n }$ to any function $f$ in ${ \mathcal { C } } [ a , b ]$ is unique. We let $X _ { n }$ be the best approximation operator,and we define $d _ { n } ^ { * } ( f )$ to be the least maximum error

$$
d _ { n } ^ { * } \left( f \right) = \left\| f - X _ { n } ( f ) \right\| _ { \infty } , \qquad f \in \mathcal { C } [ a , b ] .
$$

We take from Chapter 16 the statement that there exists a constant $\pmb { c }$ such that, if $f$ is any continuously differentiable function on $[ a , b ] ,$ then the inequality

$$
d _ { n } ^ { * } ( f ) \leqslant \left( { \frac { c } { n } } \right) \| f ^ { \prime } \| _ { \infty }
$$

is satisfied for all positive integers $\pmb { n }$ . We let $\mathcal { C } ^ { ( k ) } [ a , b ]$ be the linear space of real-valued functions on $[ a , b ]$ that have continuous kth derivatives. The result is as follows.

# Theorem 3.2

Condition (3.19) implies that,if the function $f$ is in $\mathcal { C } ^ { ( k ) } [ a , b ]$ and if $\begin{array} { r } { n \geqslant k , } \end{array}$ ,then the distance $d _ { n } ^ { * } ( f )$ satisfies the bound

$$
d _ { n } ^ { * } ( f ) \leqslant \frac { ( n - k ) ! c ^ { k } } { n ! } \| f ^ { ( k ) } \| _ { \infty } .
$$

Proof. By hypothesis, Theorem 3.2 holds when $k = 1$ . The method of proof is inductive. Therefore we suppose that the theorem is true when $\pmb { k }$ is replaced by $( k - 1 )$ , and we prove it is true for $\pmb { k }$

Because ${ \boldsymbol { n } } \geqslant { \boldsymbol { k } }$ implies $( n - 1 ) \geqslant ( k - 1 )$ ， we may apply the inductive. hypothesis to the function $f ^ { \prime }$ ，which is in $\mathcal { C } ^ { ( k - 1 ) } [ a , b ] ,$ to obtain the condition

$$
d _ { n - 1 } ^ { * } ( f ^ { \prime } ) \leqslant \frac { ( n - k ) ! c ^ { k - 1 } } { ( n - 1 ) ! } \| f ^ { ( k ) } \| _ { \infty } .
$$

We let $\pmb q$ be an indefinite integral of the best approximation from $\mathcal { P } _ { n - 1 }$ to $f ^ { \prime }$ . It follows from expression (3.19) that the inequality

$$
\begin{array} { r } { d _ { n } ^ { * } ( f - q ) \leqslant ( c / n ) \| f ^ { \prime } - q ^ { \prime } \| _ { \infty } } \\ { = ( c / n ) d _ { n - 1 } ^ { * } ( f ^ { \prime } ) } \end{array}
$$

is satisfied, where the last line depends on the definition of $\pmb q$ . The result that we use that is similar to equation (3.12) is the identity

$$
\operatorname* { m i n } _ { p \in \mathcal { P } _ { n } } \| f - p \| _ { \infty } = \operatorname* { m i n } _ { p \in \mathcal { P } _ { n } } \| f - q - p \| _ { \infty } ,
$$

which holds because $q$ is in the linear space $\mathcal { P } _ { n }$ . This identity is the equation

$$
d _ { n } ^ { * } ( f ) = d _ { n } ^ { * } ( f - q ) .
$$

The proof of the theorem is a straightforward consequence of expressions (3.21),(3.22) and (3.24).□

Expressions (3.19) and (3.20) are useful because, when $f$ is a continuously differentiable function from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，they provide bounds on the rate of convergence of the sequence $\left\{ X _ { n } ( f ) ; n = 0 , 1 , 2 , \ldots \right\}$ to $f ,$ where $X _ { n }$ is the best minimax approximation operator. It is interesting to investigate how closely the bounds are satisfied in some particular cases. Therefore some values of $d _ { n } ^ { * } ( f )$ are given in Table 3.1 for the two functions $f$ that are obtained by letting $\pmb { k }$ have the values 1 and 3 in the definition

$$
f ( x ) = \left| x \right| ^ { k } , \qquad - 1 \leqslant x \leqslant 1 .
$$

The table suggests that, as $n \to \infty$ , the error $\left\| f - X _ { n } ( f ) \right\|$ converges like ${ ( 1 / n ) } ^ { k }$ , which is the rate of convergence of the bound (3.20) when $f$ is in $\mathcal { C } ^ { ( k ) } [ - 1 , 1 ]$ . Because the trial functions are in $\mathcal { C } ^ { ( k ) } [ - 1 , 1 ]$ , except for the kth derivative discontinuity at $\boldsymbol { x } = \mathbf { 0 }$ ，Theorem 3.2 seems to be quite realistic.This statement can be made more definite because, by applying a technique that is described in Chapter 16,it can be proved that inequality (3.20) is satisfied without change to the constant $^ c$ , if the derivative $f ^ { ( k ) }$ is a piecewise continuous function， provided that the number of discontinuities is finite.

Table 3.1. Some values of $d _ { n } ^ { * } ( f )$ when $f ( x ) = \left| x \right| ^ { k }$   

<table><tr><td>n k=1</td><td>k=3</td></tr><tr><td>2 0.125 00</td><td>0.074 07</td></tr><tr><td>4 0.067 62</td><td>0.00888</td></tr><tr><td>8 0.034 69</td><td>0.001 14</td></tr><tr><td>16 0.017 47</td><td>0.000 14</td></tr></table>

This discussion shows that, if a very accurate approximation is required to a function $f ,$ then usually it is not appropriate to let the approximating function be a single polynomial, unless high derivatives of $f$ exist. Even when $f$ is infinitely differentiable, then polynomial approximations may not be suitable. One reason is that the only polynomials $p ( x )$ that remain bounded when $x \to \infty$ are constant functions.Therefore, if the function shown in Figure 1.1 is approximated closely by a polynomial, there is a strong natural tendency for the approximation to diverge rapidly to an unbounded value when the variable $x$ is outside the range $[ a , b ]$ . It may be difficult to suppress this tendency inside the range of $x$

Rational approximations, therefore,are preferred to polynomials almost exclusively in the computer subroutines that calculate standard mathematical functions, such as sines, exponentials and arc-tangents. In rational approximation, the set $\mathscr { A }$ depends on two non-negative integers $^ { m }$ and $\pmb { n }$ ,for it is composed of functions of the form

$$
r ( x ) = p ( x ) / q ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $\pmb { p } \in \mathcal { P } _ { m }$ and $q \in \mathcal P _ { n }$ . Hence $\mathscr { A }$ is not a linear space,and the algorithms for obtaining rational approximations are not linear operators. Some methods of calculation are described briefly in Chapter 10.

The question whether to give further attention to rationals was considered carefully when this book was planned. Because it was decided to concentrate on the cases when $\mathscr { A }$ is a finite-dimensional linear space, we emphasise now that rational approximations are usually far superior to polynomials,in terms of the number of coefficients that are required in order to provide sufficient accuracy. Further information can be found in the references.

# 3.4 Piecewise polynomial approximations

Consider the problem of deciding on an approximation, s say, in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,to a function $f ,$ given only the function values

$$
f ( x _ { i } ) = y _ { i } , \qquad i = 1 , 2 , \ldots , m ,
$$

where the abscissae of the data are in ascending order

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b .
$$

Often a suitable approach to this problem is to imagine that the data are plotted, and that $\pmb { s }$ is defined by drawing a smooth curve through the data points. One advantage of this method is that it allows much flexibility. For example, if $f$ is composed of a sequence of peaks that are separated by a flat background, then each peak can be plotted separately. However, suppose that instead we let $\pmb { s }$ be an analytic function.Then this flexibility is lost, because,by analytic continuation, the form of $\pmb { S }$ in any part of the range $[ a , b ]$ determines the whole of the approximating function. It is inefficient, therefore, to restrict $\pmb { s }$ to a single polynomial or rational form in approximation algorithms that are intended for general use.Instead, most of the flexibility of the graphical method can be obtained by letting s be a piecewise polynomial function.

An example of a piecewise polynomial approximation that occurs frequently is linear interpolation in a table of function values.Given the data (3.27), where $x _ { 1 } = a$ and $x _ { m } = b$ ,the function $\pmb { s }$ is defined on each of the intervals $\{ [ x _ { i } , x _ { i + 1 } ] ; i = 1 , 2 , \dots , m - 1 \}$ by the equation

$$
s ( x ) = { \frac { ( x _ { i + 1 } - x ) f ( x _ { i } ) + ( x - x _ { i } ) f ( x _ { i + 1 } ) } { ( x _ { i + 1 } - x _ { i } ) } } , \qquad x _ { i } \leqslant x \leqslant x _ { i + 1 } .
$$

Hence $\pmb { s }$ is composed of a sequence of straight line segments that are joined so that $\pmb { s }$ is continuous. If the smoothness of $f$ varies greatly on $[ a , b ] ,$ ，then it is usually advantageous to concentrate the data points where the curvature of $f$ is large.

We define $\pmb { s }$ to be a continuous piecewise polynomial of degree $k$ ,if it is in ${ \mathcal { C } } [ a , b ]$ ，and if there exist points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ ， satisfying the conditions

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi \ldots < \xi _ { n } = b ,
$$

such that $\pmb { s }$ is a polynomial of degree at most $k$ on each of the intervals $\{ [ \xi _ { i - 1 } , \xi _ { i } ] ; i = 1 , 2 , . . . , n \}$ .We define $\pmb { s }$ to be a spline function of degree $k$ if,in addition to being a continuous polynomial of degree $k$ , it is in the space $\mathcal { C } ^ { ( k - 1 ) } [ a , b ]$ . In this case the points $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ are called knots. We use the notation $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ for the linear space of spline functions of degree $k$ that have these knots.We note that each member of the space has the form

$$
s ( x ) = \sum _ { j = 0 } ^ { k } c _ { j } x ^ { j } + \frac { 1 } { k ! } \sum _ { j = 1 } ^ { n - 1 } d _ { j } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where the subscript $\cdot _ { + } ,$ has the meaning

$$
( x - \xi _ { j } ) _ { + } = \operatorname* { m a x } { [ 0 , x - \xi _ { j } ] } ,
$$

and where the parameters $\{ c _ { j } ; j = 0 , 1 , \ldots , k \}$ and $\{ d _ { j } ; j = 1 , 2 , \dots , n - 1 \}$ distinguish the different members of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . Hence the dimension of the space is $( n + k )$ . We find later, however, that the form (3.31) of a spline function is less suitable for numerical calculation than one that is recommended in Chapter 19.When a spline is obtained from the data(3.27) there is no need for the knots $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ to be a subset of the abscissae $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$

There are several reasons for giving attention to spline functions. If one requires an approximating function $\pmb { s }$ that is in $\mathcal { C } ^ { ( j ) } [ a , b ]$ and that is more flexible than an analytic function, then the simplest kind of function to handle in computer calculations is a spline of degree $( j + 1 )$ . If one requires an approximating function that is a piecewise polynomial of degree $k _ { \ast }$ ,then an advantage of using a spline is to provide a high order of derivative continuity. Thus some of the freedom in $\pmb { s }$ is fixed automatically,which can be important if there is a limited amount of data to determine the approximating function. Moreover, we find in Chapters 22-24 that splines occur naturally in the analysis of many approximation methods.

In order to keep the properties that are obtained when the set of approximating functions is a linear space, we suppose that the parameters $k$ and $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ are given. Often in practice the value of $k$ is three.Larger values provide more smoothness in the approximating function, but they reduce the amount of flexibility. The question of accuracy is also important to the choice of $k$ Specifically, if $f$ is a fixed function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ ,and if the value of $\pmb { n }$ and the distribution of the knots is variable, then the equation

$$
\operatorname* { m i n } _ { s \in \mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } ) } \left\| \boldsymbol { f } - \boldsymbol { s } \right\| = O ( h ^ { k + 1 } )
$$

is satisfied,where $h$ is the greatest interval between knots

$$
h = \operatorname* { m a x } _ { 1 \leqslant i \leqslant n } \big | \xi _ { i } - \xi _ { i - 1 } \big | .
$$

A proof of this result is given in Chapter 20. Expression (3.33), however, conceals one of the main properties of spline approximation, which is that it is usually advantageous to concentrate the knots where $f$ varies most rapidly.

Splines of degree three are called cubic splines. They are used often in practice for approximations to functions and data, because they usually provide a suitable balance between flexibility and accuracy,and because reliable algorithms are available for calculating them. Some of these algorithms choose the knot positions automatically. One of these methods is described in Chapter 21,and references to other algorithms are given in Appendix B.

# 3 Exercises

3.1 Every linear operator $\pmb { X }$ from ${ \mathcal { R } } ^ { n }$ to ${ \mathcal { R } } ^ { n }$ can be written in the form

$$
[ X f ] _ { i } = \sum _ { j = 1 } ^ { n } \bar { X } _ { i j } [ f ] _ { j } , \qquad f \in \mathcal { R } ^ { n } ,
$$

where $\bar { X }$ is an $\pmb { n } \times \pmb { n }$ matrix,and where the notation $[ f ] _ { i }$ means the ith component of the element $f$ in ${ \mathcal { R } } ^ { n }$ Express $\| X \| _ { 1 } , \| X \| _ { 2 }$ and $\| X \| _ { \infty }$ in terms of the elements of $\bar { X } .$

3.2 For any $f$ in $\mathcal { C } [ a , b ]$ ,let $X f$ be the function

$$
( X f ) ( x ) = \int _ { a } ^ { b } K ( x , y ) f ( y ) \mathrm { d } y , \qquad a \leqslant x \leqslant b ,
$$

where $\{ K ( x , y ) ; a \leqslant x \leqslant b , a \leqslant y \leqslant b \}$ isa given continuous function of two variables. Express $\| X \| _ { \infty }$ in terms of $\kappa ,$ and investigate whether, if $\| \mathbf { X } \| _ { \infty } = 1$ and $X f = f ,$ then $f$ is a constant function.

3.3 In Exercise 3.2 let $[ a , b ]$ be the interval[-1,1],and let $\kappa$ be the function

$$
K ( x , y ) = { \scriptstyle { \frac { 1 } { 2 } } } ( 1 + 3 x y ) , \qquad - 1 \leqslant x \leqslant 1 , \qquad - 1 \leqslant y \leqslant 1 .
$$

Prove that the operator $\pmb { X }$ is a projection from $\mathcal { C } [ - 1 , 1 ]$ to the space $\mathcal { P } _ { 1 }$ of linear polynomials,and that $\| X \| _ { \infty }$ has the value ${ \frac { 5 } { 3 } } .$

3.4 For any $f$ in $\mathcal { C } [ 0 , 1 ]$ let $X f$ be the function

$$
( X f ) ( x ) = 2 \int _ { 0 } ^ { \frac { 1 } { 2 } } f ( t ) \mathrm { d } t + ( x - { \textstyle \frac { 1 } { 4 } } ) [ f ( 1 ) - f ( 0 ) ] , \qquad 0 \leqslant x \leqslant 1 .
$$

Prove that the bound

$$
\left\| { f - X f } \right\| _ { \infty } \leqslant 3 \frac { 1 } { 2 } \| { f - p } \| _ { \infty }
$$

is satisfied, where $p$ is any approximation to $f$ from the space $\mathcal { P } _ { 1 }$ of linear polynomials.

3.5 Investigate whether the inequality of Exercise 3.4 can be satisfied as an equation.

3.6 Show that the estimate

$$
f ( 3 ) \approx - { \textstyle \frac { 1 } { 2 } } f ( 0 ) + f ( 1 ) + { \textstyle \frac { 1 } { 2 } } f ( 4 )
$$

is exact if $f$ is a quadratic polynomial. For a particular $f$ in $\mathcal { C } [ 0 , 4 ]$ it is found that the error of the estimate is O.15.Prove that the inequality

$$
\operatorname* { m i n } _ { p \in \mathcal { P } _ { 2 } } \operatorname* { m a x } _ { 0 \leqslant x \leqslant 4 } \left| f ( x ) - p ( x ) \right| \geqslant 0 . 0 5
$$

holds.

3.7 We use the notation of Theorem 3.2. For any positive integer $k$ let the numbers $\{ c ( k , n ) ; n \geq k \}$ satisfy the condition

$$
d _ { n } ^ { * } ( f ) \leqslant c ( k , n ) \| f ^ { ( k ) } \| _ { \infty } , \qquad f \in \mathcal { C } ^ { ( k ) } [ a , b ] .
$$

Prove that, if $n \geqslant 2 k$ ,then the bound

$$
d _ { n } ^ { * } ( f ) \leqslant c ( k , n ) c ( k , n - k ) \| f ^ { ( 2 k ) } \| _ { \infty } , \qquad f \in \mathcal { C } ^ { ( 2 k ) } [ a , b ] ,
$$

is obtained. Hence deduce a relation between $d _ { n } ^ { * } ( f )$ and $\| f ^ { ( 2 k ) } \| _ { \infty }$ from expression (3.20).

3.8 Let $\mathscr { A }$ be the set of quadratic splines in $\mathcal { C } [ - 1 , 1 ]$ that have at most two knots in the open interval $( - 1 , 1 )$ ，and let $f$ be the function $\{ f ( x ) = | x | ; - 1 \leqslant x \leqslant 1 \}$ . Show that there exists $\pmb { s }$ in $\mathcal { A }$ such that $\| f - s \| _ { \infty }$ is less than any given positive number, but that no member of $\mathscr { A }$ satisfies the condition $\| f - s \| _ { \infty } = 0$

3.9 Let $\pmb { s }$ be the cubic spline function

$$
s ( x ) = x ^ { 3 } - 4 ( x - 1 ) _ { + } ^ { 3 } + 6 ( x - 2 ) _ { + } ^ { 3 } - 4 ( x - 3 ) _ { + } ^ { 3 } + ( x - 4 ) _ { + } ^ { 3 } ,
$$

$$
0 \leqslant x \leqslant 1 0 0 .
$$

Show that $\pmb { s }$ is identically zero if $x \geqslant 4$ , but that severe cancellation occurs if $s ( 1 0 0 )$ is evaluated from the definition of $\pmb { s }$

3.10Let $\mathcal { A }$ be the set of piecewise functions of the form

$$
\begin{array} { r } { s _ { \lambda } ( x ) = \left\{ \begin{array} { l l } { 0 , } & { 0 \leqslant x \leqslant \lambda , } \\ { 1 , } & { \lambda < x \leqslant 1 , } \end{array} \right. } \end{array}
$$

where $\lambda$ is a parameter from the interval [O,1], and let $f$ be a function in $\mathcal { C } [ 0 , 1 ]$ Show that, if $\pmb { S } _ { \pmb { \lambda } }$ is a best $\mathbf { { { L } } _ { 1 } }$ approximation from $\mathscr { A }$ to $f ,$ then $\lambda = 0$ ,or $\lambda = 1$ ,or $\begin{array} { r } { f ( \lambda ) = \frac { 1 } { 2 } } \end{array}$ Find an $f$ in $\mathcal { C } [ 0 , 1 ]$ that has exactly two best $L _ { 1 }$ approximations in $\mathcal { A }$

# Polynomial interpolation

# 4.1 The Lagrange interpolation formula

If one decides to approximate a function $f \in { \mathcal { C } } [ a , b ]$ by a polynomial

$$
p ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } x ^ { i } , \qquad a \leqslant x \leqslant b ,
$$

one has the problem of specifying the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$ The most straightforward method is to calculate the value of $f$ at $( n + 1 )$ distinct points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ of $[ a , b ]$ ，and to satisfy the equations

$$
p ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , n .
$$

We note that there are as many conditions as coefficients,and the following theorem shows that they determine $p \in \mathcal P _ { n }$ uniquely.

# Theorem 4.1

Let $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ be any set of $( n + 1 )$ distinct points in $[ a , b ] ,$ and let $f \in \mathcal { C } [ a , b ]$ .Then there is exactly one polynomial $p \in \mathcal P _ { n }$ that satisfies the equations (4.2).

Proof. For $k = 0 , 1 , \ldots , n .$ let $l _ { k }$ be the function

$$
l _ { k } ( x ) = \prod _ { \stackrel { j = 0 } { j \ne k } } ^ { n } ( x - x _ { j } ) / ( x _ { k } - x _ { j } ) , \quad a \leqslant x \leqslant b .
$$

We note that $l _ { k } \in \mathcal { P } _ { n }$ and that the equations

$$
l _ { k } ( x _ { i } ) = \delta _ { k i } , \qquad i = 0 , 1 , \ldots , n ,
$$

hold, where $\delta _ { k i }$ has the value

$$
\delta _ { k i } = \left\{ { \begin{array} { l l l } { 1 , } & { } & { k = i , } \\ { 0 , } & { } & { k \neq i . } \end{array} } \right.
$$

It follows that the function

$$
p = \sum _ { k = 0 } ^ { n } f ( x _ { k } ) l _ { k }
$$

is in $\mathcal { P } _ { n }$ and it satisfies the required interpolation conditions (4.2). To show uniqueness,suppose that the equations (4.2) are satisfied by both $p \in \mathcal P _ { n }$ and $q \in \mathcal { P } _ { n }$ . Then the difference $( p - q )$ is in $\mathcal { P } _ { n }$ and it has roots at the points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ .However, a polynomial of degree at most $_ n$ that has $( n + 1 )$ distinct roots is identically zero.Therefore $p$ is equal to $q$ □

The numerical value of the interpolating polynomial $p ( x )$ for any fixed $x$ in $[ a , b ]$ can be calculated by first computing the numbers (4.3) for $k = 0 , 1 , \ldots , n .$ , and then by substituting them in the equation

$$
p ( x ) = \sum _ { k = 0 } ^ { n } f ( x _ { k } ) l _ { k } ( x ) .
$$

This method is called the Lagrange interpolation formula. There are many other algorithms for calculating $p ( x )$ that are equivalent in exact arithmetic. They differ, however,in the accuracy that is obtained in the presence of computer rounding errors,and in the amount of work that is done when they are applied. One of the most successful algorithms, which is called Newton's interpolation method, is described in the next chapter.

The uniqueness property, proved in Theorem 4.1, allows us to regard the interpolation process as an operator from $\mathcal { C } [ a , b ]$ to $\mathcal { P } _ { n }$ ，which depends on the choice of the fixed points $\{ x _ { i } ; i = 0 , ~ 1 , \dotsc , n \}$ . The operator is a projection because,if $f \in \mathcal P _ { n }$ ， then we may satisfy the interpolation conditions (4.2) by making $p$ equal to $f .$ Moreover, because the functions $l _ { k }$ $( k = 0 , 1 , \ldots , n )$ are independent of $f ,$ equation (4.6) shows that the operator is linear. Therefore we may apply Theorem 3.1, and we find in Section 4.4 that it gives some interesting results.

When the function values $\{ f ( x _ { i } ) ; i = 0 , 1 , \dots , n \}$ cannot be obtained exactly, it may be important to know the contribution'that their errors make to the calculated polynomial $p$ .Equation (4.6) answers this question directly,for, if the true function value $f ( x _ { k } )$ is replaced by the approximation $\{ f ( x _ { k } ) + \varepsilon _ { k } \}$ for $k = 0 , 1 , \ldots , n$ , we see that the change to $p$ is the expression $\sum \pmb { \varepsilon } _ { k } l _ { k }$

The Lagrange interpolation formula provides some algebraic relations that are useful in later work. They come from our remark that the interpolation process is a projection operator. In particular, for $0 \leqslant i \leqslant n$ ， we let $f$ be the function

$$
f ( x ) = x ^ { i } , \qquad a \leqslant x \leqslant b ,
$$

in order to obtain from expression (4.7) the equation

$$
\sum _ { k = 0 } ^ { n } x _ { k } ^ { i } l _ { k } ( x ) = x ^ { i } , \qquad a \leqslant x \leqslant b .
$$

The value $i = 0$ gives the identity

$$
\sum _ { k = 0 } ^ { n } l _ { k } ( x ) = 1 , \qquad a \leqslant x \leqslant b ,
$$

which is useful for checking the numbers $\left\{ l _ { k } ( x ) ; k = 0 , 1 , \ldots , n \right\}$ when the Lagrange interpolation method is applied. Moreover, by substituting the definition (4.3) in equation (4.9),and then by considering the coeficient of $x ^ { n }$ ,we find the identity

$$
\sum _ { k = 0 } ^ { n } \frac { x _ { k } ^ { i } } { \displaystyle \prod _ { j = 0 \atop j \ne k } ^ { n } \left( x _ { k } - x _ { j } \right) } = \delta _ { i n } , \qquad i = 0 , 1 , \dots , n .
$$

# 4.2 The error in polynomial interpolation

We use the notation $^ e$ for the error function of an approximation, and in this chapter it has the value

$$
e ( x ) = f ( x ) - p ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $\pmb { p }$ is the polynomial in ${ \mathcal { P } } _ { n }$ that satisfies the interpolation conditions (4.2). It should be clear that, if we change $f$ by adding to it an element of $\mathcal { P } _ { n }$ ， then the interpolation process automatically adds the same element to $\pmb { p }$ ，which leaves $_ e$ unchanged. Expressions for the error should show this property. It is therefore appropriate, when $f \in { \mathcal { C } } ^ { ( n + 1 ) } [ a , b ] .$ to state $^ e$ in terms of the derivative $f ^ { ( n + 1 ) }$ ,which is doneinour next theorem.

# Theorem 4.2

For any set of distinct interpolation points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ in $[ a , b ]$ and for any $f \in { \mathcal { C } } ^ { ( n + 1 ) } [ a , b ] ,$ let $\pmb { p }$ be the element of $\mathcal { P } _ { n }$ that satisfies the equations (4.2). Then,for any $\pmb { x }$ in $[ a , b ] ,$ ,the error (4.12) has the value

$$
e \left( x \right) = \frac { 1 } { \left( n + 1 \right) ! } \prod _ { j = 0 } ^ { n } \left( x - x _ { j } \right) f ^ { ( n + 1 ) } ( \xi ) ,
$$

where $\pmb { \xi }$ is a point of $[ a , b ]$ that depends on $\pmb { x }$

Proof. Two methods are used in this book to express errors in terms of derivatives. One is to apply the Taylor series expansion,and the other one is to use Rolle's theorem several times. Rolle's theorem states that, if a continuously differentiable function is zero at two points, then its deriva-tive is zero at an intermediate point. By using this result inductively, we deduce that, if afunction $g \in { \mathcal { C } } ^ { ( n + 1 ) } [ a , b ]$ is zero at $( n + 2 )$ distinct points of $[ a , b ] ,$ then its $( n + 1 ) \operatorname { t h }$ derivative has at least one zero in $[ a , b ]$ .The present proof depends on this fact.

We note frst that, if $x$ is in the point set $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ ，then equation (4.13) holds, because both sides of the equation are equal to zero. Otherwise we define the function $\pmb { g }$ by the equation

$$
g ( t ) = f ( t ) - p ( t ) - e ( x ) \prod _ { i = 0 } ^ { n } { \frac { ( t - x _ { i } ) } { ( x - x _ { i } ) } } , \qquad a \leqslant t \leqslant b ,
$$

and it is important to note that $t$ is the variable, the value of $x$ being fixed. We see that $g \in { \mathcal { C } } ^ { ( n + 1 ) } [ a , b ] ,$ and that $g ( t )$ is zero both when $t = x$ and when $t$ is in the point set $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ ，Therefore there exists a point $\pmb { \xi }$ in $[ a , b ]$ at which the equation

$$
{ \pmb g } ^ { ( n + 1 ) } ( { \pmb \xi } ) = { \bf 0 }
$$

is satisfied. By substituting the definition (4.14) in this equation, and by rearranging terms, we find the required result (4.13).□

A helpful way of remembering this result is to let $f$ be the function

$$
f ( x ) = x ^ { n + 1 } , \qquad a \leqslant x \leqslant b .
$$

In this case the error function is the polynomial

$$
e ( x ) = x ^ { n + 1 } - p ( x ) , \qquad a \leqslant x \leqslant b ,
$$

and,because the error is zero at the interpolation points $\{ x _ { i } ; i =$ $0 , 1 , \ldots , n \} , e ( x )$ must be a multiple of the product

$$
\prod _ { j = 0 } ^ { n } { \big ( } x - x _ { j } { \big ) } .
$$

The multiplying factor is the term $f ^ { ( n + 1 ) } ( \xi )$ times a constant, which has to have the value $1 / ( n + 1 ) !$ , in order that the coefficient of $x ^ { n + 1 }$ in $e ( x )$ is equal to one, as required by equation (4.17).

Some applications of Theorem 4.2 are as follows. If a bound on $\| f ^ { ( n + 1 ) } \| _ { \infty }$ is known,then expression (4.13) gives a bound on the error of polynomial interpolation.Similarly，an estimate of the term $f ^ { ( n + 1 ) } ( \pmb { \xi } )$ provides an estimate of the interpolation error, which is discussed further in the next chapter. Moreover, Theorem 4.2 is useful sometimes when one wishes to compare polynomial interpolation with some other linear approximation operator that is exact for $f \in \mathcal { P } _ { n }$ . If the error of the alternative operatoris expressed in terms of $f ^ { ( n + 1 ) }$ , then equation (4.13) helps to show which approximation method is more accurate.

# 4.3 The Chebyshev interpolation points

This section concerns the choice of the interpolation points $\left\{ x _ { i } ; i = 0 , 1 , \ldots , n \right\}$ 、Most of the conclusions are obtained by applying polynomial interpolation to a particular function $f ,$ known as Runge's example.It is the function

$$
f ( x ) = 1 / ( 1 + x ^ { 2 } ) , \qquad - 5 \leqslant x \leqslant 5 .
$$

Because most of the variation in $f$ Occurs in the middle of the range $- 5 \leqslant x \leqslant 5$ ,the discussion given in Section 3.3 shows that it is not really suitable to approximate $f$ by a single polynomial. We have to choose a polynomial of very high degree if we wish to achieve high accuracy. Therefore the example serves quite well to show the kinds of difficulty that can occur in polynomial interpolation. In particular, we find that the positions of the interpolation points $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ are important when $_ n$ is large.

If the nterpolation points are spaced uniformly

$$
x _ { i } = - 5 + 1 0 i / n , \qquad i = 0 , 1 , \dots , n ,
$$

then the size of the error function (4.12) near the ends of the range $- 5 \leqslant x \leqslant 5$ is interesting. We let $x _ { n - { \frac { 1 } { 2 } } }$ be the point

$$
x _ { n - \frac { 1 } { 2 } } = 5 - 5 / n ,
$$

which is the mid-point of the last interval between interpolation points. The value of $p ( x _ { n - \frac { 1 } { 2 } } )$ was found by Lagrange interpolation for $\pmb { n } =$ 2,4,...,20,and the results are shown in Table 4.1. We see that the error almost doubles in magnitude each time $_ n$ is increased by two. Therefore it is futile to try to improve the accuracy of the approximation by increasing the value of $_ n$

Table 4.1. The dependence of $e ( x _ { n - \frac { 1 } { 2 } } )$ on n in Runge's example   

<table><tr><td>n</td><td>f(xn-2)</td><td>p(xn-2)</td><td>e(xn-2)</td></tr><tr><td>2</td><td>0.137931</td><td>0.759 615</td><td>-0.621 684</td></tr><tr><td>4</td><td>0.066 390</td><td>-0.356 826</td><td>0.423 216</td></tr><tr><td>6</td><td>0.054 463</td><td>0.607 879</td><td>-0.553 416</td></tr><tr><td>8</td><td>0.049 651</td><td>-0.831 017</td><td>0.880 668</td></tr><tr><td>10</td><td>0.047 059</td><td>1.578 721</td><td>--1.531 662</td></tr><tr><td>12</td><td>0.045 440</td><td>-2.755 000</td><td>2.800 440</td></tr><tr><td>14</td><td>0.044 334</td><td>5.332 743</td><td>-5.288 409</td></tr><tr><td>16</td><td>0.043 530</td><td>-10.173 867</td><td>10.217 397</td></tr><tr><td>18</td><td>0.042 920</td><td>20.123 671</td><td>-20.080 751</td></tr><tr><td>20</td><td>0.042 440</td><td>-39.952 449</td><td>39.994 889</td></tr></table>

The reason for the large values of $e ( x )$ shown in Table 4.1 can be found from the form of the error function when $n = 2 0$ .Values of this function are given in Table 4.2 at the points that are midway between the interpolation points in $0 \leqslant x \leqslant 5$ . Negative values of $\pmb { x }$ are omitted because $f$ and $\pmb { p }$ are both even functions of $\pmb { x }$ .The function (4.18), which is called prod $( x )$ , is also tabulated. The most important feature of the table is that the very rapid increase in the tabulated values of $e ( x )$ also occurs in the tabulated values of prod $\mathbf { \Psi } ( x )$ . Indeed the ratio $e ( x ) / { \mathfrak { p r o d } } ( x )$ is almost constant.

It follows, therefore, that in this example the dependence on $\pmb { x }$ of the term $f ^ { ( n + 1 ) } ( \pmb { \xi } )$ in equation (4.13) does not make much difference to the form of $e ( x )$ . A good practical strategy is to assume that this property remains true if the positions of the interpolation points $\{ x _ { i } ; i =$ $0 , 1 , \ldots , n \}$ are altered. Therefore we wish to find interpolation points that do not give large variations in the heights of the peaks of prod $( x )$ . By bunching interpolation points near the ends of the range, the very large peaks of prod $\mathbf { \Psi } ( { \pmb x } )$ can be reduced, at the expense of increasing the heights of the small peaks near the centre of the range $- 5 \leqslant x \leqslant 5$ . The interpolation points that equalize the peak heights are called the Chebyshev interpolation points,and they are found by making use of ‘Chebyshev polynomials'.

For the range $- 1 \leqslant x \leqslant 1$ ,the Chebyshev polynomial of degree $_ { n }$ is the function $T _ { n }$ that satisfies the equation

$$
T _ { n } ( \cos \theta ) = \cos { ( n \theta ) } ,
$$

Table 4.2. An example of equally spaced interpolation points $( n = 2 0 )$   

<table><tr><td>X</td><td>f(x)</td><td>p(x)</td><td>e(x)</td><td>prod(x)</td></tr><tr><td>0.25</td><td>0.941 176</td><td>0.942 490</td><td>-0.001314</td><td>2.05×106</td></tr><tr><td>0.75</td><td>0.640 000</td><td>0.636 755</td><td>0.003 245</td><td>-2.48×106</td></tr><tr><td>1.25</td><td>0.390 244</td><td>0.395 093</td><td>-0.004 849</td><td>3.64×106</td></tr><tr><td>1.75</td><td>0.246 154</td><td>0.238 446</td><td>0.007 708</td><td>-6.56×106</td></tr><tr><td>2.25</td><td>0.164 948</td><td>0.179 763</td><td>-0.014 814</td><td>1.46×107</td></tr><tr><td>2.75</td><td>0.116 788</td><td>0.080 660</td><td>0.036128</td><td>-4.12×107</td></tr><tr><td>3.25</td><td>0.086 486</td><td>0.202 423</td><td>-0.115 936</td><td>1.51×108</td></tr><tr><td>3.75</td><td>0.066 390</td><td>-0.447 052</td><td>0.513442</td><td>-7.56×108</td></tr><tr><td>4.25</td><td>0.052 459</td><td>3.454 958</td><td>-3.402 499</td><td>5.59×109</td></tr><tr><td>4.75</td><td>0.042 440</td><td>-39.952 449</td><td>39.994 889</td><td>-7.27×1010</td></tr></table>

which is equivalent to the equation

$$
T _ { n } ( x ) = \cos { ( n \cos ^ { - 1 } x ) } , \qquad - 1 \leqslant x \leqslant 1 .
$$

An easy way of imagining $T _ { n } ( x )$ as a function of $\pmb { x }$ is to expand cos $( n \theta )$ in powers of cos $\pmb \theta _ { i }$ , and to write $\pmb { x }$ in place of cos $\pmb \theta .$ Hence $T _ { n } \in \mathcal { P } _ { n } ,$ ,and the identity

$$
\cos \left[ ( n + 1 ) \theta \right] + \cos \left[ ( n - 1 ) \theta \right] = 2 \cos \theta \cos \left( n \theta \right)
$$

gives the recurrence relation

$$
T _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

Chebyshev polynomials have many applications in approximation theory,and they are useful now because the heights of the peaks of the function

$$
T _ { n } ( x ) = \cos { ( n \theta ) } , \qquad x = \cos { \theta } ,
$$

are all equal to one. We can force prod $( x )$ to be a multiple of $T _ { n + 1 } ( x )$ by letting the interpolation points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ be the roots of the polynomial $T _ { n + 1 }$ , which gives the points

$$
x _ { i } = \cos \bigg \{ \frac { [ 2 ( n - i ) + 1 ] \pi } { 2 ( n + 1 ) } \bigg \} , \qquad i = 0 , 1 , \ldots , n .
$$

In order to adapt these values to a general range $a \leqslant x \leqslant b$ we introduce real parameters $\pmb { \lambda }$ and $\pmb { \mu }$ ,and we define the points

$$
x _ { i } = \lambda + \mu \cos \Big \{ \frac { [ 2 ( n - i ) + 1 ] \pi } { 2 ( n + 1 ) } \Big \} , \qquad i = 0 , 1 , \ldots , n ,
$$

to be Chebyshev interpolation points.By construction they have the property that the magnitudes of the peaks of the polynomial (4.18) are all equal,which helps usually to reduce the greatest value of the error function (4.13), provided that $\pmb { x _ { 0 } }$ is close to $\pmb { a }$ and $x _ { n }$ is close to $\pmb { b }$ . We really want to choose the interpolation points in a way that makes the expression

$$
\operatorname* { m a x } _ { a \leqslant x \leqslant b } \left| { \mathrm { p r o d } } \left( x \right) \right|
$$

small.A theorem in Chapter 7 shows that this expression is minimized over all sets $\left\{ x _ { i } ; i = 0 , 1 , \ldots , n \right\}$ if $\pmb { \lambda }$ and $\pmb { \mu }$ have the values

$$
\left. \begin{array} { c } { { \lambda = \frac 1 2 ( a + b ) } } \\ { { \mu = \frac 1 2 ( b - a ) } } \end{array} \right\}
$$

in equation (4.28).

In order to show that the use of Chebshev interpolation points can improve on the accuracy that is shown in Table 4.2,we let $\{ x _ { i } ; i =$ $0 , 1 , \ldots , n \}$ have the values (4.28), where $\pmb { n } = 2 0$ and where $\pmb { \lambda }$ and $\pmb { \mu }$ are such that $x _ { 0 } = - 5$ and $x _ { 2 0 } = 5$ . The Lagrange interpolation method was applied again to Runge's function (4.19). Table 4.3 shows the errors of interpolation at the positive values of $x$ where |prod $\left( x \right) \ !$ is greatest. We find that the greatest value of $\left| e ( x ) \right|$ is smaller than in Table 4.2 by a factor of over two thousand, and the cost of this gain is that the small errors near the centre of the range $- 5 \leqslant x \leqslant 5$ are increased by about a factor of five.Now all the variations in the tabulated values of $e ( x )$ are due to the term $f ^ { ( n + 1 ) } ( \xi )$ in equation (4.13).

It is also of interest to note the improvement over Table 4.1 that can be obtained by using Chebyshev interpolation points. Therefore, for $n = 2$ ， $4 , \ldots , 2 0$ ，we let the set $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ be defined by equation (4.28), where,as in the last paragraph, the values of $\pmb { \lambda }$ and $\pmb { \mu }$ are such that $x _ { 0 } = - 5$ and $x _ { n } = 5$ . Thus an interpolating polynomial $\pmb { p } \in \mathcal { P } _ { n }$ is obtained for each n. By applying Lagrange interpolation for several values of $x$ ,the maximum value of $\vert e ( x ) \vert$ was calculated. The values of $x$ that maximize the error function and the corresponding values of $f , p$ and $\pmb { e }$ are shown in Table 4.4. We see that the use of Chebyshev interpolation points is so much better than equally spaced ones, that now the accuracy of the approximation improves when $\pmb { n }$ is increased.

Table 4.3. An example of Chebyshev interpolation points $( n = 2 0 )$   

<table><tr><td>x</td><td>f(x)</td><td>p(x)</td><td>e(x)</td></tr><tr><td>0.374 698</td><td>0.876 886</td><td>0.887 135</td><td>-0.010 249</td></tr><tr><td>1.115 724</td><td>0.445 466</td><td>0.429 963</td><td>0.015 503</td></tr><tr><td>1.831 827</td><td>0.229 590</td><td>0.242 708</td><td>-0.013 119</td></tr><tr><td>2.507 010</td><td>0.137 266</td><td>0.126 532</td><td>0.010 734</td></tr><tr><td>3.126190</td><td>0.092 824</td><td>0.101 876</td><td>-0.009 052</td></tr><tr><td>3.675 537</td><td>0.068 920</td><td>0.061018</td><td>0.007 902</td></tr><tr><td>4.142 778</td><td>0.055 058</td><td>0.062 173</td><td>-0.007115</td></tr><tr><td>4.517 476</td><td>0.046 712</td><td>0.040 130</td><td>0.006 582</td></tr><tr><td>4.791 261</td><td>0.041 743</td><td>0.047 981</td><td>-0.006238</td></tr><tr><td>4.958 018</td><td>0.039 090</td><td>0.033 045</td><td>0.006 045</td></tr></table>

Table 4.4. The maximum error when Chebyshev interpolation points are used   

<table><tr><td>n</td><td>x</td><td>f(x)</td><td>p(x)</td><td>e(x)</td></tr><tr><td>2</td><td>2.024 604</td><td>0.196116</td><td>0.842 345</td><td>-0.646 229</td></tr><tr><td>4</td><td>1.393 399</td><td>0.339 765</td><td>0.761 908</td><td>-0.442 143</td></tr><tr><td>6</td><td>1.097 876</td><td>0.453 447</td><td>0.727 637</td><td>-0.274 191</td></tr><tr><td>8</td><td>0.912 455</td><td>0.545 680</td><td>0.721 700</td><td>-0.176 020</td></tr><tr><td>10</td><td>0.781 995</td><td>0.620 534</td><td>0.732 455</td><td>-0.111 921</td></tr><tr><td>12</td><td>0.684167</td><td>0.681 159</td><td>0.751878</td><td>-0.070 718</td></tr><tr><td>14</td><td>1.526988</td><td>0.300 148</td><td>0.252 887</td><td>0.047 260</td></tr><tr><td>16</td><td>1.356 570</td><td>0.352 078</td><td>0.319 037</td><td>0.033 040</td></tr><tr><td>18</td><td>1.221 054</td><td>0.401 449</td><td>0.378 684</td><td>0.022 765</td></tr><tr><td>20</td><td>1.110 623</td><td>0.447 731</td><td>0.432 224</td><td>0.015 507</td></tr></table>

# 4.4 The norm of the Lagrange interpolation operator

Theorem 3.1 provides an excellent reason for studying the norm of the Lagrange interpolation operator. We use the $\infty$ -norm for the elements of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ ，we assume that the set of interpolation points $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ has been chosen and,for each $f$ in $\mathcal { C } [ a , b ]$ ,we let $X ( f )$ be the element of $\mathcal { P } _ { n }$ that is defined by the conditions (4.2). The value of $\| \pmb { X } \|$ is the subject of our next theorem.

# Theorem 4.3

The norm of the Lagrange interpolation operator has the value

$$
\left\| { \mathbfcal { X } } \right\| = \operatorname* { m a x } _ { a \leqslant x \leqslant b } \sum _ { k = 0 } ^ { n } \big | l _ { k } ( x ) \big | ,
$$

where the functions $\{ l _ { k } ; k = 0 , 1 , \ldots , n \}$ are defined by equation (4.3).

Proof. The definition of a norm and equation (4.6) give the identity

$$
\begin{array} { l } { | X | = \displaystyle \operatorname* { s u p } _ { \| f \| < 1 } \| X ( f ) \| } \\ { = \displaystyle \operatorname* { s u p } _ { \| f \| \geq 1 } \operatorname* { m a x } _ { \alpha \leq x \leq b } \bigg | \displaystyle \sum _ { k = 0 } ^ { n } f ( x _ { k } ) l _ { k } ( x ) \bigg | } \\ { = \displaystyle \operatorname* { m a x } _ { \alpha \leq x \leq b } \displaystyle \operatorname* { s u p } _ { \kappa = 0 } \bigg | \displaystyle \sum _ { k = 0 } ^ { n } f ( x _ { k } ) l _ { k } ( x ) \bigg | } \\ { = \displaystyle \operatorname* { m a x } _ { \alpha \leq x \leq b } \displaystyle \sum _ { k = 0 } ^ { n } | l _ { k } ( x ) | , } \end{array}
$$

which is the required result.

We note that the method of proof is to treat the supremum over $f$ in equation (4.32) before the maximum over $x$ .Often expressions for norms are suprema of maxima,and it is usually helpful, especially in the case of interpolation operators, to take account of the conditions on $f$ before maximizing over $\pmb { x }$

Theorem 3.1 states that the error $\left\| f - X ( f ) \right\|$ is within the factor $[ 1 + \| X \| ]$ of the least error

$$
d ^ { * } ( f ) = \operatorname* { m i n } _ { { p \in { \mathcal { P } } _ { n } } } \left\| f - { p } \right\|
$$

that can be achieved by approximating $f$ by a member of $\mathcal { P } _ { n }$ Hence we obtain from Tables 4.2 and 4.4 a lower bound on $\| X \| ,$ where $\pmb { X }$ is the interpolation operator in the case when $\pmb { n } = 2 0$ and the interpolation points have the equally spaced values (4.2O). Because Table 4.4 shows that 0.015 507 is an upper bound on $d ^ { * } ( f )$ , it follows from Theorem 3.1 and Table 4.2 that the inequality

$$
\left\| X \right\| \geqslant ( 3 9 . 9 9 4 8 8 9 / 0 . 0 1 5 5 0 7 ) - 1
$$

holds.Hence $\| { \pmb X } \|$ is rather large,and in fact it is equal to 10 986.71, which was calculated by evaluating the function on the right-hand side of equation (4.31） for several values of $\pmb { x }$ .Table 4.5 gives $\| X \|$ for $n =$ 2,4,...,20 for the interpolation points (4.20). It also gives the value of $\| X \|$ for the Chebyshev interpolation points (4.28) that are relevant to Table 4.4, where $\pmb { \lambda }$ and $\pmb { \mu }$ are such that $x _ { 0 } = - 5$ and $x _ { n } = 5$

Table 4.5 shows clearly that, if the choice of interpolation points is independent of $f ,$ and if $\pmb { n }$ is large, then it is safer to use Chebyshev points instead of equally spaced ones. Indeed, if $\pmb { n } = 2 0$ and if Chebyshev points are preferred, then it follows from Theorem 3.1 that, for all $f \in \mathcal { C } [ - 5 , 5 ] ,$ the maximum error of the interpolating polynomial is within the factor 3.48 of the least maximum error that can be achieved. However, if the interpolation points are equally spaced, then the form of the error function shown in Table 4.2 is typical, where the maximum error is much larger than necessary. Moreover，another good practical reason for keeping $\| X \|$ small is that it makes the calculated polynomial less sensitive to errors in the data.

Table 4.5. The norms of some interpolation operators   

<table><tr><td>n</td><td>Equally spaced points</td><td>Chebyshev points</td></tr><tr><td>2</td><td>1.25</td><td>1.25</td></tr><tr><td>4</td><td>2.21</td><td>1.57</td></tr><tr><td>6</td><td>4.55</td><td>1.78</td></tr><tr><td>8</td><td>10.95</td><td>1.94</td></tr><tr><td>10</td><td>29.90</td><td>2.07</td></tr><tr><td>12</td><td>89.32</td><td>2.17</td></tr><tr><td>14</td><td>283.21</td><td>2.27</td></tr><tr><td>16</td><td>934.53</td><td>2.34</td></tr><tr><td>18</td><td>3171.37</td><td>2.42</td></tr><tr><td>20</td><td>10 986.71</td><td>2.48</td></tr><tr><td colspan="3"></td></tr></table>

The results in Table 4.5 are not special to the range $- 5 \leqslant x \leqslant 5$ ， because a general linear transformation of the form

$$
x  \alpha x + \beta , \qquad \alpha > 0 ,
$$

where $_ \alpha$ and $\beta$ are real parameters,which changes $[ a , b ]$ to $[ \alpha a + \beta ,$ $\alpha b + \beta ]$ and $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ to $\left\{ \alpha x _ { i } + \beta ; i = 0 , 1 , \ldots , n \right\}$ ，does not alter the value of $\| X \|$ . The reason is that this transformation just introduces the factor $\alpha ^ { n }$ into the numerator and denominator of the definition (4.3） and these factors cancel each other.Hence the transformation stretches or contracts the graphs of $l _ { k }$ $( k = 0 , 1 , \ldots , n )$ in the $x$ -direction, but it leaves them unaltered in the $y$ -direction. Thus the value of expression (4.31) does not change,and identities like equation (4.10) are preserved.

# 4 Exercises

4.1 Let $p$ be the cubic polynomial that interpolates the function values $f ( 0 ) , f ( 1 ) , f ( 2 )$ and $f ( 3 )$ . Express $p ( 6 )$ in terms of these function values,and verify that your formula is correct when $f$ is the function $\{ f ( x ) = ( x - 3 ) ^ { 3 }$ ； $0 \leqslant x \leqslant 6 \}$ . What is the uncertainty in the value of $p ( 6 )$ , if the uncertainty in each function value is $\pm \varepsilon ?$

4.2 Let $f \in { \mathcal { C } } ^ { ( 2 ) } [ 0 , 1 ]$ , and let the function value $f ( x )$ be estimated by linear interpolation to two of the three values $\begin{array} { r } { f ( 0 . 0 ) = 0 . 0 , } \end{array}$ $f ( 0 . 7 ) = 0 . 7$ and $f ( 1 . 0 ) = 0 . 1$ .Show that, if Theorem 4.2 is used to express the error in terms of $f ^ { \prime \prime }$ ,then,in order to minimize the multiplying factor in the error estimate, it is best to interpolate to $\textstyle f ( 0 . 0 )$ and $f ( 0 . 7 )$ if $0 \leqslant x < 0 . 5$ , but it is best to use $f ( 0 . 7 )$ and $f ( 1 . 0 )$ if $0 . 5 < x \leqslant 1 . 0$ .Deduce that $f ( 0 . 5 )$ satisfies the condition

$$
1 . 1 - 0 . 0 5 \| f ^ { ( 2 ) } \| _ { \infty } \leqslant f ( 0 . 5 ) \leqslant 0 . 5 + 0 . 0 5 \| f ^ { ( 2 ) } \| _ { \infty } ,
$$

and hence obtain a lower bound on $\| f ^ { ( 2 ) } \| _ { \infty }$

Piecewise polynomial approximations ${ \pmb p } _ { 1 }$ and $\pmb { p } _ { 2 }$ to the function $\{ f ( x ) = \cos x ; 0 \leqslant x \leqslant \pi \}$ are defined in the following way. Positive integers $\pmb { n } _ { 1 }$ and $_ { n _ { 2 } }$ are chosen, where $_ { n _ { 2 } }$ is even. The function ${ p } _ { 1 }$ is composed of straight line segments that join at the points $\{ x = k \pi / n _ { 1 } ; k = 1 , 2 , \ldots , n _ { 1 } - 1 \}$ ,and its parameters are defined by the conditions $\{ p _ { 1 } ( k \pi / n _ { 1 } ) = f ( k \pi / n _ { 1 } ) ; k = 0 , 1 , \ldots , n _ { 1 } \}$ .The function ${ \pmb p } _ { 2 }$ is composed of quadratic polynomial segments that join at the points $\{ x = k \pi / n _ { 2 }$ ； $k = 2 , 4 , 6 , \dots , n _ { 2 } - 2 \}$ and its parameters are defined by the conditions $\{ p _ { 2 } ( k \pi / n _ { 2 } ) = f ( k \pi / n _ { 2 } )$

$k = 0 , 1 , \ldots , n _ { 2 } \}$ . Estimate the smallest values of $\pmb { n } _ { 1 }$ and $_ { n _ { 2 } }$ that make the errors $\| f - p _ { 1 } \| _ { \infty }$ and $\| f - p _ { 2 } \| _ { \infty }$ less than ${ { 1 0 } ^ { - 6 } }$

4.4 Let $f \in { \mathcal { C } } ^ { ( 2 n ) } [ 0 , 1 ]$ ,and let $\pmb { p }$ be a polynomial of degree $( 2 n - 1 )$ that satisfies the equations

$$
\begin{array} { c c } { { p ^ { ( k ) } ( 0 ) = f ^ { ( k ) } ( 0 ) \Big \} , } } & { { \quad k = 0 , 1 , . . . , n - 1 . } } \\ { { p ^ { ( k ) } ( 1 ) = f ^ { ( k ) } ( 1 ) } } \end{array}
$$

Prove that, for every $x$ in [0,1], there exists $\pmb { \xi }$ in [0,1], such that the error of the polynomial approximation has the value

$$
f ( x ) - p ( x ) = { \frac { x ^ { n } ( x - 1 ) ^ { n } } { ( 2 n ) ! } } f ^ { ( 2 n ) } ( \xi ) .
$$

4.5 Show that, if the Chebyshev interpolation points (4.27) are used instead of the equally spaced points $\{ x _ { i } = ( 2 i - n ) / n$ ； $i =$ $0 , 1 , \ldots , n \}$ ， then the greatest distance between interpolation points is multiplied by a factor that is less than $\scriptstyle { \frac { 1 } { 2 } } \pi$ Show, however, that the Chebyshev points have the property that the ratio of the largest to the smallest intervals between interpolation points is greater than $( n + 1 ) / \pi$

4.6 For any $f$ in $\mathcal { C } [ 0 , 3 ]$ let $X f$ be the function of the form

$$
( X f ) ( x ) = c _ { 0 } + c _ { 1 } x + c _ { 3 } x ^ { 3 } , \qquad 0 \leqslant x \leqslant 3 ,
$$

whose coefficients $c _ { 0 } , c _ { 1 }$ and $\boldsymbol { c } _ { 3 }$ are defined by the interpolation conditions $( X f ) ( 0 ) = f ( 0 )$ ， $( X f ) ( 2 ) = f ( 2 )$ and $( X f ) ( 3 ) = f ( 3 )$ Deduce that $\| X \| _ { \infty }$ has the value $( 1 + 3 2 / 4 5 \sqrt { 3 } )$

4.7 Let $M ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n } )$ be the $\infty$ -norm of the Lagrange interpolation operator from the space $\mathcal { C } [ \alpha , b ]$ to $\mathcal { P } _ { n }$ ，where the interpolation points have the values $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ .Prove that, if the interpolation points are changed continuously so that two of them tend to be equal, then $M ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n } )$ tends to infinity.

.8 Suppose that one has to calculate $p ( { \pmb x } )$ from equations (4.7) and (4.3) for many million values of $\pmb { x }$ ,where $_ n$ is about twenty. Show that, by calculating in advance some auxiliary quantities that depend on the data points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ and the function values $\{ f ( x _ { i } ) ; i = 0 , 1 , \dots , n \}$ ， the number of computer operations in each evaluation of $p ( x )$ can be reduced to a small multiple of $\pmb { n }$

4.9 Consider the problem of calculating the coefficients $\{ \alpha _ { i } ; i =$ $0 , 1 , \ldots , m \}$ and $\{ \beta _ { i } ; i = 0 , 1 , \ldots , n \}$ of the rational function

$$
r ( x ) = \frac { \alpha _ { 0 } + \alpha _ { 1 } x + . . . + \alpha _ { m } x ^ { m } } { \beta _ { 0 } + \beta _ { 1 } x + . . . + \beta _ { n } x ^ { n } } , \qquad a \leqslant x \leqslant b ,
$$

so that the interpolation conditions

$$
r ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , m + n ,
$$

are satisfied, where $\{ x _ { i } ; i = 0 , 1 , \ldots , m + n \}$ is a set of distinct points in $[ a , b ]$ ，and where the function values $\{ f ( x _ { i } ) ; i =$ $0 , 1 , \ldots , m + n \}$ are given. Show that suitable coefficients can be found usually by solving a square system of linear equations, but that sometimes the linear equations have no adequate solution.

4.10Sketch the graph of the function

$$
\sum _ { k = 0 } ^ { n } \big | l _ { k } ( x ) \big | , \qquad a \leqslant x \leqslant b ,
$$

that occurs in equation (4.31). Consider the problem of placing the interpolation points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ in a way that minimizes $\| X \|$ .Show that it is suitable to let $x _ { 0 }$ and $x _ { n }$ have the values $\pmb { a }$ and $^ { b }$ respectively. Investigate the position(s) of the other point(s) when $n = 2$ and when ${ n = 3 }$ .

# Divided differences

# 5.1 Basic properties of divided differences

Let $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ be any $( n + 1 )$ distinct points of $[ a , b ] ,$ and let $f$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ . The coefficient of $x ^ { n }$ in the polynomial $p \in \mathcal P _ { n }$ that satisfies the interpolation conditions

$$
p ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , n ,
$$

is defined to be a divided difference of order $_ n$ , and we use the notation $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ]$ for its value. We note that the order of a divided difference is one less than the number of arguments in the expression $f [ . { \cdot } , . , . . . , . ]$ Hence $f [ x _ { 0 } ]$ is a divided difference of order zero, which, by definition,has the value $f ( x _ { 0 } )$ . Moreover, when $n \geqslant 1$ ， it follows from equations (4.3) and (4.6) that the equation

$$
f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ] = \sum _ { k = 0 } ^ { n } { \frac { f ( x _ { k } ) } { \prod _ { j = 0 } ^ { n } \left( x _ { k } - x _ { j } \right) } }
$$

is satisfied. We see that the divided difference is linear in the function values $\{ f ( x _ { i } ) ; i = 0 , 1 , \dots , n \}$ ，but formula (5.2) is not the best way of calculating the value of $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ]$ . A better method is described in Section 5.3.

Divided differences have several uses. They are applied in this chapter to provide a good method of polynomial interpolation. They are used in Chapter 19 to generate a convenient basis of the space of splines $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ， which was mentioned in Section 3.4. Other applications include checking values of a tabulated function for errors,and the automatic adjustment of‘order' and step-length in the numerical solution of differential equations.

It is often convenient to think of the divided differeice $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ]$ as a value of the nth derivative of the function $f$ divided by the factor $n !$ The following theorem justifies this point of view.

# Theorem 5.1

Let $f \in { \mathcal { C } } ^ { ( n ) } [ a , b ]$ and let $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ be a set of distinct points in $[ a , b ]$ . Then there exists a point $\xi ,$ in the smallest interval that contains the points $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ ,at which the equation

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } ] = f ^ { ( n ) } ( \xi ) / n !
$$

is satisfied.

Proof. Let $e$ be the error function

$$
e ( x ) { = } f ( x ) { - } p \dot { ( x ) } , \qquad a { \leqslant } x { \leqslant } b ,
$$

where $\pmb { p } \in \mathcal { P } _ { n }$ is defined by the interpolation conditions (5.1). We note that $e$ is in $\mathcal { C } ^ { ( n ) } [ a , b ] .$ ,and that $e ( x )$ is zero when $x$ is in the point set $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ .Therefore, by applying Rolle's theorem inductively, we find that $e ^ { ( n ) } ( \xi )$ is zero, where $\xi$ is a point in the range that is given in the statement of the theorem. Hence the equation

$$
p ^ { ( n ) } ( \xi ) = f ^ { ( n ) } ( \xi )
$$

is obtained, so the required result (5.3) follows from the definition of the divided difference.□

This theorem is an important part of the standard method of checking tabulated values of a function for errors. Suppose that the function $f \in { \mathcal { C } } ^ { ( n ) } [ a , b ]$ is given on the point set $\{ x _ { i } ; i = 0 , 1 , \dots , m \}$ ，where $_ m$ is much larger than $\pmb { n }$ ,and where the points are in ascending order

$$
a \leqslant x _ { 0 } < x _ { 1 } < . ~ . ~ . < x _ { m } \leqslant b .
$$

Then the sequence $\{ f [ x _ { j } , x _ { j + 1 } , \dots , x _ { j + n } ] ; j = 0 , 1 , \dots , m - n \}$ may be calculated, using the method described in Section 5.3.Theorem 5.1 shows that,in exact arithmetic, the terms of the sequence are values of the function $\{ f ^ { ( n ) } ( x ) / n ! ; a \leqslant x \leqslant b \}$ in each of the intervals $\{ [ x _ { j } , x _ { j + n } ] ; j =$ $0 , 1 , \ldots , m - n \}$ . Therefore,if the data points $\{ x _ { i } ; i = 0 , 1 , \ldots , m \}$ are closely spaced, we may expect the sequence of divided differences to vary slowly. In this case,however, the denominators of expression (5.2) are small. Hence any errors in the function values are magnified by amounts that can easily be calculated. It is usual to attribute unsmooth changes in the terms of the sequence $\{ f [ x _ { j } , x _ { j + 1 } , \dots , x _ { j + n } ] ; j = 0 , 1 , \dots , m - n \}$ to errors in the tabulated function values,which provides a procedure for estimating the size of the errors.

# 5.2 Newton's interpolation method

Suppose that one has to estimate the function value $f ( x )$ from a large number of data $\{ f ( x _ { i } ) ; i = 0 , 1 , \ldots , m \}$ ,where $x$ is a fixed point. It is usually poor to fit a polynomial of degree $^ m$ to all the data, but it may be suitable to apply polynomial interpolation to a subset of the given function values, in which case the question arises of choosing which data to use.A suitable procedure can be obtained from the remark that, if ${ p _ { n } }$ is the polynomial in $\mathcal { P } _ { n }$ that interpolates the function values $\{ f ( x _ { i } ) ; i =$ $0 , 1 , \ldots , n \}$ ,and if $n < m$ ,then Theorems 4.2 and 5.1 suggest the error estimate

$$
f ( x ) - p _ { n } ( x ) \approx \left\{ \prod _ { j = 0 } ^ { n } { ( x - x _ { j } ) } \right\} f [ x _ { 0 } , x _ { 1 } , . . . , x _ { n + 1 } ] .
$$

Because it is sensible to prefer data points that are close to $x$ itis convenient to label the data points so that the differences $\{ | x - x _ { i } | ; i =$ $0 , 1 , \ldots , m \}$ increase monotonically. The procedure for choosing $_ n$ is to consider the error estimate (5.7) for $n = 0 , 1 , \ldots , ( m - 1 )$ .One should not necessarily prefer the value of $_ n$ that gives the smallest error estimate, because expression (5.7) can be small by chance.Instead one should seek the value of $_ n$ at which the trend in the error estimates is least. What usually happens is that at first the accuracy of the interpolation method improves,but one reaches a stage where the additional data is so remote from $x$ that it is not helpful to use extra function values.

Even if the value of $\pmb { n }$ is known in advance, there are advantages in calculating the polynomials $\{ p _ { k } ; k = 0 , 1 , \ldots , n \}$ in sequence, where ${ p } _ { k }$ is the polynomial in $\mathcal { P } _ { k }$ that is defined by the interpolation conditions

$$
p _ { k } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , k .
$$

The main advantage is the subject of the next theorem, and it is that one can calculate $p _ { k + 1 } ( x )$ from $p _ { k } ( x )$ by adding on the estimate of the error $\{ f ( x ) - p ( x ) \}$ that is obtained by replacing $_ n$ by $\pmb { k }$ in expression (5.7).

# Theorem 5.2

Let ${ p } _ { k }$ be the polynomial in $\mathcal { P } _ { k }$ that is defined by the interpolation conditions (5.8). Then the function

$$
p _ { k + 1 } ( x ) = p _ { k } ( x ) + \bigg \{ \prod _ { j = 0 } ^ { k } { ( x - x _ { j } ) \bigg \} } f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ] , \qquad a \leqslant x \leqslant b ,
$$

is the polynomial in $\mathcal { P } _ { k + 1 }$ that satisfies the conditions

$$
p _ { k + 1 } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , k + 1 .
$$

Proof. Let $p _ { k + 1 }$ be defined by equation (5.9),and let $q$ be the polynomial in $\mathcal { P } _ { k + 1 }$ that interpolates the function values $\{ f ( x _ { i } ) ; i = 0 , 1 , \dots , k + 1 \}$ Equations (5.8) and (5.9) imply the identities

$$
q ( x _ { i } ) - p _ { k + 1 } ( x _ { i } ) = 0 , \qquad i = 0 , 1 , \ldots , k .
$$

Moreover,the definition of the divided difference $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ]$ implies that the function $\{ q ( x ) - p _ { k + 1 } ( x ) ; a \leqslant x \leqslant b \}$ is in $\mathcal { P } _ { k }$ . It follows from expression (5.11） that the difference $\{ q ( x ) - p _ { k + 1 } ( x ) ; a \leqslant x \leqslant b \}$ is identically zero,which proves the theorem.□

By applying the theorem inductively,we obtain the definition

$$
\begin{array} { r l } & { p _ { n } ( x ) = f ( x _ { 0 } ) + ( x - x _ { 0 } ) f [ x _ { 0 } , x _ { 1 } ] + ( x - x _ { 0 } ) ( x - x _ { 1 } ) f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ] } \\ & { \qquad + \ldots + \left\{ \displaystyle \prod _ { j = 0 } ^ { n - 1 } ( x - x _ { j } ) \right\} f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ] , \quad a \leqslant x \leqslant b , } \end{array}
$$

of the polynomial in $\mathcal { P } _ { n }$ that satisfies the interpolation conditions (5.1). This form of the interpolating polynomial is called ‘Newton's interpolation method', and it is useful for several reasons. For example, we find in Section 5.4 that the effects of computer rounding errors when the formula is used in practice are less damaging than the effects that occur when the Lagrange interpolation method is applied. It is important to notice that the numbers $\{ x _ { i } ; i = 0 , 1 , \dotsc , n \}$ need not be in ascending order.A good method of calculating the divided differences of expression (5.12) is described in the next section.

# 5.3 The recurrence relation for divided differences

The standard procedure for calculating the divided differences of Newton's interpolation formula (5.12) requires the evaluation of all the terms in the tableau

$$
\begin{array} { r l } & { f [ x _ { 0 } ] } \\ & { f [ x _ { 0 } , x _ { 1 } ] } \\ & { f [ x _ { 1 } ] } \\ & { f [ x _ { 1 } , x _ { 2 } ] } \\ & { f [ x _ { 1 } , x _ { 2 } ] } \\ & { f [ x _ { 2 } ] } \\ & { \vdots \quad \qquad \vdots } \\ & { f [ x _ { n - 1 } , x _ { n - 1 } , x _ { n } ] \cdot ^ { \cdot } } \\ & { \vdots \quad f [ x _ { n - 1 } , x _ { n } ] } \\ & { f [ x _ { n } ] } \end{array}
$$

The first column is composed of the given function values $\{ f ( x _ { i } ) ; i =$ $0 , 1 , \ldots , n \}$ , and the remaining columns are calculated in sequence, using the formula that is given in the next theorem.

# Theorem 5.3

The divided difference $f [ x _ { j } , x _ { j + 1 } , \dotsc , x _ { j + k + 1 } ]$ of order $( k + 1 )$ is related to the divided differences $f [ x _ { j } , x _ { j + 1 } , \dotsc , x _ { j + k } ]$ and $f [ x _ { j + 1 } , x _ { j + 2 } , \dotsc , x _ { j + k + 1 } ]$ of order $k$ by the equation

$$
f [ x _ { j } , x _ { j + 1 } , \dots , x _ { j + k + 1 } ] = { \frac { f [ x _ { j + 1 } , \dots , x _ { j + k + 1 } ] - f [ x _ { j } , \dots , x _ { j + k } ] } { ( x _ { j + k + 1 } - x _ { j } ) } } .
$$

Proof. Let ${ p } _ { k }$ be the polynomial in $\mathcal { P } _ { k }$ that interpolates the function values $\{ f ( x _ { i } ) ; i = j , j + 1 , \ldots , j + k \} ,$ and let $\pmb q _ { k }$ be the polynomial in $\mathcal { P } _ { k }$ that interpolates the function values $\{ f ( x _ { i } ) ; i = j + 1 , j + 2 , \ldots , j + k + 1 \}$ Then it is straightforward to verify that the function

$$
p _ { k + 1 } ( x ) = \frac { ( x - x _ { j } ) q _ { k } ( x ) + ( x _ { j + k + 1 } - x ) p _ { k } ( x ) } { ( x _ { j + k + 1 } - x _ { j } ) } , \qquad a \leqslant x \leqslant b ,
$$

is in $\mathcal { P } _ { k + 1 }$ ,and it satisfies the conditions

$$
p _ { k + 1 } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = j , j + 1 , . . . . , j + k + 1 .
$$

Hence the divided difference $f [ x _ { j } , x _ { j + 1 } , \dotsc , x _ { j + k + 1 } ]$ is the coefficient of $x ^ { k + 1 }$ in thepolynomial (5.15).Because $f [ x _ { j } , x _ { j + 1 } , \dotsc , x _ { j + k } ]$ is the coefficient of $x ^ { k }$ in ${ p } _ { k }$ ，and because $f [ x _ { j + 1 } , x _ { j + 2 } , \dotsc , x _ { j + k + 1 } ]$ is the coefficient of $x ^ { k }$ in $\pmb q _ { k }$ ,it follows that equation (5.14) is satisfied.□

The theorem shows that the calculation of each entry in the second and subsequent columns of the tableau (5.13) requires only two subtractions and one division. Hence the number of computer operations to obtain the divided differences for Newton's interpolation formula is of order $n ^ { 2 }$

The recurrence relation (5.14) was used to calculate the divided differences of the function

$$
f ( x ) = 1 0 \mathrm { e } ^ { - 3 x } , \qquad 0 \leqslant x \leqslant 2 ,
$$

tabulated on the point set {1.60,1.63,1.70,1.76,1.80}. The results are shown in Tables 5.1 and 5.2. All data and all calculated numbers were rounded to a fixed precision before they were recorded and used for subsequent calculation.The difference between the tables is that in Table 5.1 the precision is six decimal places,but in Table 5.2 it is only five decimal places.We note the large change in the fourth divided difference that is caused by the change in accuracy, which shows the care that has to be given to the accuracy of the data and the precision of the computer arithmetic, if one uses divided differences to estimate derivatives.

# 5.4 Discussion of formulae for polynomial interpolation

Often there are several ways of carrying out a computer calculation that would give identical results in exact arithmetic. The numerical analyst studies the effect of computer rounding errors, which is often a major part of the development of a successful algorithm.In this book,however, much more attention is given to the theoretical questions that are relevant to approximation methods,assuming that computer arithmetic is exact. Therefore, we show now that the consequences of limited precision arithmetic are important also, by giving this question some attention in the case of polynomial interpolation.

Three methods of interpolation are compared. Two of these have been described already, namely the Lagrange formula and Newton's method, and the third one is to evaluate the coeficients $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$ ,in order that $p ( { \pmb x } )$ may be calculated from the formula

Table 5.1. Some divided differences in six-decimal arithmetic   

<table><tr><td>xi</td><td>f(xi)</td><td>Order 1</td><td>Order 2</td><td>Order 3</td><td>Order 4</td></tr><tr><td>1.60</td><td>0.082 297</td><td>-0.236 100</td><td></td><td></td><td></td></tr><tr><td>1.63</td><td>0.075 214</td><td>-0.203 529</td><td>0.325 710</td><td>-0.297 900</td><td></td></tr><tr><td>1.70</td><td>0.060 967</td><td>-0.167 383</td><td>0.278 046</td><td>-0.257 153</td><td>0.203 735</td></tr><tr><td>1.76</td><td>0.050 924</td><td>-0.143 950</td><td>0.234 330</td><td></td><td></td></tr><tr><td>1.80</td><td>0.045 166</td><td></td><td></td><td></td><td></td></tr></table>

Table 5.2. Some divided differences in five-decimal arithmetic   

<table><tr><td>xi</td><td>f(xi)</td><td>Order 1</td><td>Order 2</td><td>Order 3</td><td>Order 4</td></tr><tr><td>1.60</td><td>0.082 30</td><td>-0.236 33</td><td></td><td></td><td></td></tr><tr><td>1.63</td><td>0.075 21</td><td></td><td>0.329 00</td><td>-0.328 87</td><td></td></tr><tr><td>1.70</td><td>0.060 97</td><td>-0.203 43</td><td>0.276 38</td><td></td><td>0.500 80</td></tr><tr><td>1.76</td><td>0.050 92</td><td>-0.167 50</td><td>0.237 50</td><td>-0.228 71</td><td></td></tr><tr><td>1.80</td><td>0.045 17</td><td>-0.143 75</td><td></td><td></td><td></td></tr></table>

$$
p ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } x ^ { i } , \qquad a \leqslant x \leqslant b ,
$$

for any value of $x$ .Thus a polynomial approximation to $f$ is defined in three ways,and we ask first whether they satisfy accurately the interpolation conditions (5.1).

In the case of the Lagrange formula, when $x$ is the interpolation point $x _ { i } , 0 \leqslant i \leqslant n$ ,then the definition (4.3） makes $l _ { k } ( x )$ zero for $k \neq i ,$ and it makes $l _ { i } ( { \pmb x } )$ equal to or very close to the value one on a floating point computer. Hence good accuracy in the interpolation conditions is obtained from equation (4.7). The situation is less clear for Newton's formula (5.12),except when $\pmb { x } = \pmb { x } _ { 0 }$ ,because the function values do not occur explicitly in the equation that defines $p ( { \pmb x } )$ . Instead the formula is dependent on the accuracy of the calculated divided differences.A comparison of Tables 5.1 and 5.2 suggests at first that this accuracy may be poor, but if,for example, we take the divided differences from the top line of Table 5.2,and if we let $x = 1 . 8 0$ in equation (5.12), then exact arithmetic gives the value

$$
p ( 1 . 8 0 ) = 0 . 0 4 5 1 6 9 9 5 0 8 ,
$$

which agrees very well with the data value O.O45 17. The reason for the good precision in the interpolation conditions is due to the cancellation that occurs when differences are calculated. Because of it, the number of digits that are needed to retain the information that is present in the original table of function values becomes less as each new column of differences is formed. Hence, the effect of working to a fixed number of digits is that more and more guard digits are introduced, whose values are ill-defined, but they prevent loss of information during the calculation. Exercise 5.4 helps to make the point clear,for it shows that the whole of Table 5.2 can be recovered to high accuracy from the data in its leading diagonal.

The situation is rather different, however, if $p ( { \pmb x } )$ is obtained from equation (5.18). Again the function values do not occur explicitly, and now the accuracy to which the interpolation conditions (5.1） hold depends on the errors in the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$ .In the case of the data of Table 5.2,for example, it is appropriate to calculate the coefficients to at least five decimals accuracy, and to this precision $\pmb { p }$ is the polynomial

$$
\begin{array} { c } { { p ( x ) = 6 . 7 0 0 9 8 - 1 3 . 3 6 0 2 1 x + 1 0 . 3 8 5 6 0 x ^ { 2 } } } \\ { { - 3 . 6 9 2 4 1 x ^ { 3 } + 0 . 5 0 2 7 2 x ^ { 4 } . } } \end{array}
$$

However, because computers use floating point arithmetic,it is inconsistent to allow seven decimals of accuracy in the coefficients $\{ c _ { i } ; i =$ $0 , 1 , \ldots , n \}$ ,when making comparisons with a calculation that is accurate to only five decimals. Therefore we may have to accept the approximation

$$
\begin{array} { c } { p ( x ) = 6 . 7 0 1 0 - 1 3 . 3 6 0 x + 1 0 . 3 8 6 x ^ { 2 } } \\ { - 3 . 6 9 2 4 x ^ { 3 } + 0 . 5 0 2 7 2 x ^ { 4 } } \end{array}
$$

instead of expression (5.20). This less accurate approximation gives the value

$$
\begin{array} { r } { p ( 1 . 8 ) = 0 . 0 4 6 9 2 , } \end{array}
$$

which shows a large error in the interpolation conditions. It is generally better, therefore, to use Newton's formula, unless one knows in advance that the computer arithmetic is so accurate that one can obtain suitable values of the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$

A consideration that is important sometimes is the magnitude of the discontinuities that occur in the approximating function $\{ p ( x ) ; a \leqslant x \leqslant b \}$ due to the discrete nature of computer arithmetic. We consider this question in the frequently occurring case when $f$ is so smooth that the successive terms of Newton's formula (5.12) decrease rapidly in magnitude.In this case,if we change the variable $x$ continuously, then computer rounding errors introduce discontinuities into the polynomial (5.12), whose magnitude is about $\left| f ( \boldsymbol { x } _ { 0 } ) \right|$ times the relative precision of the computer arithmetic.However,because the terms of the sum (4.7) of the Lagrange formula are calculated separately, we find in this case that the magnitude of the discontinuities is approximately the relative precision times the largest of the numbers $\{ | f ( x _ { k } ) l _ { k } ( x ) | ; k = 0 , 1 , \dots , n \}$ Hence, in the cases when the factor $\big | l _ { k } ( x ) \big |$ is much larger than one, an advantage of using Newton's method instead of the Lagrange formula is that one usually obtains smaller discontinuities in the calculated interpolating polynomial.

# 5.5 Hermite interpolation

It happens sometimes that, in addition to the function values on the right-hand side of equation (5.1), some values of the derivative of $f$

are known also. The general Hermite interpolation problem is to calculate $\pmb { p } \in \mathcal { P } _ { n }$ that satisfies the conditions

$$
p ^ { ( j ) } ( x _ { i } ) = f ^ { ( j ) } ( x _ { i } ) , \qquad j = 0 , 1 , \ldots , l _ { i } , \qquad i = 0 , 1 , \ldots , m ,
$$

where the number of coefficients of $\pmb { p }$ is equal to the number of data, which implies that $_ n$ is defined by the equation

$$
n + 1 = \sum _ { i = 0 } ^ { m } { \bigl ( } l _ { i } + 1 { \bigr ) } .
$$

We find in this section that $\pmb { p }$ can be obtained from an interesting extension of Newton's interpolation method, but first it is proved that the data on the right-hand side of equation (5.23) does define the required polynomial uniquely.

# Theorem 5.4

Let $\{ x _ { i } ; i = 0 , 1 , \ldots , m \}$ be a set of distinct points from $a \leqslant x \leqslant b$ ， and let the real numbers $\{ f ^ { ( j ) } ( x _ { i } ) ; j = 0 , 1 , \ldots , l _ { i } ; i = 0 , 1 , \ldots , m \}$ be given.Then there is just one polynomial $\pmb { p }$ in $\mathcal { P } _ { n }$ that satisfies the equations (5.23), where the value of $\pmb { n }$ is defined by equation (5.24).

Proof. The frst part of the proof is a highly useful general method for demonstrating the uniqueness of an approximation from a linear space. We parameterize the approximating functions by choosing a basis of the linear space,and in the present case every member of $\mathcal { P } _ { n }$ can be expressed in the form

$$
p ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } x ^ { i } , \qquad a \leqslant x \leqslant b .
$$

Because the number of conditions on $\pmb { p }$ is equal to the number of parameters, the required coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy a square system of linear equations. It is therefore sufficient to prove that the matrix of the system is non-singular.An equivalent condition is that, if we set the right-hand sides of the equations to zero, then they are satisfied only if all the parameters are zero.Hence it suffices to prove that, if all the data values are zero, then $\pmb { p }$ is identically zero.

We find that,when the data are zero, then $p$ is a multiple of the polynomial

$$
\prod _ { i = 0 } ^ { m } \ ( x - x _ { i } ) ^ { l _ { i } + 1 } , \qquad a \leqslant x \leqslant b .
$$

Because this polynomial includes the term $x ^ { n + 1 }$ , the multiplying factor must be zero.Hence $p$ is identically zero.□

We note that Theorem 4.1 can be deduced as a corollary of Theorem 5.4. We note also that the proof of Theorem 5.4 depends on the condition that, if the derivative value $f ^ { ( k ) } ( x _ { i } )$ occurs in the data, then the values $\{ f ^ { ( j ) } ( x _ { i } ) ; j = 0 , 1 , \ldots , k - 1 \}$ are given also. The divided difference method for calculating $p$ makes further use of this condition.

In order to describe this method, we change the notation for the data points in the following way. We replace the set $\{ x _ { i } ; i = 0 , 1 , \dots , m \}$ by the set $\{ x _ { 0 } , x _ { 0 } , \dotsc , x _ { 0 } , x _ { 1 } , x _ { 1 } , \dotsc , x _ { 1 } , \dotsc , x _ { m } , x _ { m } , \dotsc , x _ { m } \}$ ，where，for $i =$ $0 , 1 , \ldots , m$ ,the number $\pmb { \chi } _ { i }$ occurs $( l _ { i } + 1 )$ times. We renumber the indices of the terms in the new set so that its elements are $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ Hence the repeated terms in the new set indicate which derivatives are given as data, and we have returned to the case where there are $( n + 1 )$ data points.

We now try to apply Newton's interpolation formula (5.12) to our data. The only difficulty occurs in the calculation of the divided differences,due to the fact that the recurrence relation (5.14) gives zero divided by zero if $x _ { j + k + 1 } = x _ { j } .$ However, Theorem 5.1 provides a solution to this problem, for it shows that if $x _ { j } = x _ { j + 1 } = \dotsc = x _ { j + k + 1 }$ , then it is appropriate to make the definition

$$
f [ x _ { j } , x _ { j + 1 } , \ldots , x _ { j + k + 1 } ] = f ^ { ( k + 1 ) } ( x _ { j } ) / ( k + 1 ) ! ,
$$

which is very convenient because the right-hand side is available as data. Thus all the terms in the table of divided differences (5.13) can be found, either from equation (5.14) or from equation (5.27), provided that the repeated terms in the set $\left\{ x _ { i } ; i = 0 , 1 , \ldots , n \right\}$ are grouped together. Hence formula (5.12) can still be used.

For example, we calculate the polynomial of degree four that satisfes the conditions

$$
\left. \begin{array} { r l } { p ( 1 . 6 ) = } & { { 0 . 0 8 2 2 9 7 } } \\ { p ^ { \prime } ( 1 . 6 ) = - { 0 . 2 4 6 8 9 2 } } \\ { p ( 1 . 7 ) = } & { { 0 . 0 6 0 9 6 7 } } \\ { p ( 1 . 8 ) = } & { { 0 . 0 4 5 1 6 6 } } \\ { p ^ { \prime } ( 1 . 8 ) = - { 0 . 1 3 5 4 9 7 } } \end{array} \right\}
$$

The data are obtained from the function (5.17). The tableau of divided differences is shown in Table 5.3,where the first and last entries in the column of first-order differences are data.The remainder of this column and the higher order terms are calculated by using the recurrence relation (5.14). Hence Newton's method gives the polynomial

$$
\begin{array} { c } { { p ( x ) = 0 . 0 8 2 \ 2 9 7 - 0 . 2 4 6 \ 8 9 2 ( x - 1 . 6 ) + 0 . 3 3 5 \ 9 2 0 ( x - 1 . 6 ) ^ { 2 } } } \\ { { - 0 . 2 9 7 \ 3 5 0 ( x - 1 . 6 ) ^ { 2 } ( x - 1 . 7 ) } } \\ { { + 0 . 2 0 3 \ 7 5 0 ( x - 1 . 6 ) ^ { 2 } ( x - 1 . 7 ) ( x - 1 . 8 ) . } } \end{array}
$$

It is easy to verify that the conditions (5.28) are satisfied. The final theorem of this chapter proves that the given extension of Newton's method is suitable generally for calculating the polynomial in $\mathcal { P } _ { n }$ that is defined by the conditions (5.23).

# Theorem 5.5

Let the function value $f ( x )$ be given at the points $\{ x _ { i } ; i =$ $0 , 1 , \ldots , n \}$ ，and,if $\pmb { \chi } _ { i }$ occurs $( k + 1 )$ times in the point set, let the derivatives $\{ f ^ { ( j ) } ( x _ { i } ) ; j = 1 , 2 , \dots , k \}$ be given also. Let any repeated terms in the set $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ be grouped together, and let $p _ { n } \in \mathcal { P } _ { n }$ be the polynomial that is calculated by the extension of Newton's method that has just been described. Then the polynomial ${ p _ { n } }$ interpolates the data.

Proof. Because Theorem 5.4 states that there is exactly one polynomial, $p ^ { * }$ say, that interpolates the data, and because the definition of ${ p _ { n } }$ is unchanged if $f$ is replaced by $p ^ { * }$ , we assume without loss of generality that $f$ is in $\mathcal { P } _ { n }$ . Therefore we have to prove that ${ p _ { n } }$ is equal to $f .$ For any small positive number $\pmb \varepsilon$ ，we let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a set of distinct points that satisfies the conditions $\{ | \xi _ { i } - x _ { i } | \leqslant \varepsilon ; i = 0 , 1 , \dots , n \}$ ，and we apply Newton's method to calculate the polynomial in $\mathcal { P } _ { n }$ that interpolates the function values $\left\{ f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n \right\}$ ， which is straightforward because the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ are distinct. Because this polynomial must be $f$ itself, the identity

Table 5.3.A divided difference table that includes derivative values   

<table><tr><td>xi</td><td>f(xi)</td><td>Order 1</td><td>Order 2</td><td>Order 3</td><td>Order 4</td></tr><tr><td>1.60</td><td>0.082 297</td><td>-0.246 892</td><td></td><td></td><td></td></tr><tr><td>1.60</td><td>0.082 297</td><td>-0.213 300</td><td>0.335 920</td><td>-0.297 350</td><td></td></tr><tr><td>1.70</td><td>0.060 967</td><td>-0.158 010</td><td>0.276 450</td><td>-0.256 600</td><td>0.203 750</td></tr><tr><td>1.80</td><td>0.045 166</td><td>-0.135 497</td><td>0.225 130</td><td></td><td></td></tr><tr><td>1.80</td><td>0.045 166</td><td></td><td></td><td></td><td></td></tr></table>

$$
\begin{array} { l } { f ( x ) = f ( \xi _ { 0 } ) + ( x - \xi _ { 0 } ) f [ \xi _ { 0 } , \xi _ { 1 } ] + ( x - \xi _ { 0 } ) ( x - \xi _ { 1 } ) f [ \xi _ { 0 } , \xi _ { 1 } , \xi _ { 2 } ] } \\ { \displaystyle + \ldots + \left\{ \prod _ { j = 0 } ^ { n - 1 } \ ( x - \xi _ { j } ) \right\} f [ \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } ] } \end{array}
$$

is satisfied. We compare this calculation with the definition of ${ \pmb p } _ { \pmb n }$ that is given in the statement of the theorem.In particular we compare the two tables of divided differences that are formed.

In the table that is used to calculate $p _ { n }$ ,the first column contains the function values $\{ f ( x _ { i } ) ; i = 0 , 1 , \ldots , n \}$ ,and in the other table it contains the numbers $\left\{ f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n \right\}$ .Moreover, if equation (5.27) is used in the calculation of ${ \pmb p } _ { \pmb n }$ ,then the entry $f ^ { ( k + 1 ) } ( x _ { j } ) / ( k + 1 ) !$ occurs in one divided difference table,and the corresponding entry in the other table is the expression $f [ \xi _ { j } , \xi _ { j + 1 } , \ldots , \xi _ { j + k + 1 } ] ,$ which,by Theorem 5.1,has the value $f ^ { ( k + 1 ) } ( \xi ) / ( k + 1 ) !$ , where $\pmb { \xi }$ is in the shortest interval that contains the points $\{ \xi _ { i } ; i = j , j + 1 , \ldots , j + k + 1 \}$ .Therefore $\pmb { \xi }$ is in the interval $[ x _ { j } - \varepsilon , x _ { j } + \varepsilon ]$ ，Hence,by choosing $\pmb \varepsilon$ to be sufficiently small, one can achieve arbitrarily close agreement between the entries in the two divided difference tables that correspond directly to the data that determine ${ p _ { n } }$ All remaining entries are defined by the recurrence relation (5.14). Each recurrence relation that is used has a non-zero denominator,and the denominator $( \pmb { \xi } _ { j + k + 1 } - \pmb { \xi } _ { j } )$ can be made arbitrarily close to $( { \pmb x } _ { j + k + 1 } - { \pmb x } _ { j } )$ by choosing $\pmb \varepsilon$ to be sufficiently small. Hence arbitrarily close agreement can be obtained between the two complete tables. Therefore,for any value of $\pmb { x } ,$ ，and for any positive number $\delta ,$ ，there exists $\pmb \varepsilon > 0$ such that the difference $\left| f ( x ) - p _ { n } ( x ) \right|$ between expressions (5.30) and (5.12) is less than $\pmb { \delta } .$ ，However,both $f ( x )$ and $p _ { n } ( x )$ are independent of $\pmb \varepsilon$ . Therefore the polynomials $f$ and ${ \pmb p } _ { \pmb n }$ are the same.□

# 5 Exercises

5.1 Form the table of divided differences of the function values $f ( - 2 ) = 3 . 2 8 ,$ ， $f ( - 1 ) = 1 7 . 3 6$ ， $f ( 2 ) = 1 4 . 9 6 ,$ ， $f ( 3 ) = 1 9 . 2 8$ and $f ( 4 ) = 3 6 . 1 6 .$ .Verify that Newton's interpolation method is in agreement with the given vale of $f ( 4 )$ ·

5.2 Deduce from equation (5.12) that $p ^ { \prime } ( x _ { 0 } )$ has the value

$$
\begin{array} { r } { p ^ { \prime } ( x _ { 0 } ) = f [ x _ { 0 } , x _ { 1 } ] + ( x _ { 0 } - x _ { 1 } ) f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ] + \dots } \\  + \left\{ \begin{array} { l l } { \displaystyle \prod _ { j = 1 } ^ { n - 1 } \ ( x _ { 0 } - x _ { j } ) \right\} f [ x _ { 0 } , x _ { 1 } , \dots , x _ { n } ] . } \end{array} \end{array}
$$

Hence obtain $p ^ { \prime } ( 2 )$ from the divided difference table of Exercise 5.1,where $\pmb { p }$ is the polynomial in $\mathcal { P } _ { 4 }$ that interpolates the data of that exercise. Note that, if $\scriptstyle x _ { 0 } = 2$ ， $x _ { 1 } = 3$ ， $x _ { 2 } = 4$ ， $x _ { 3 } = - 1$ and $x _ { 4 } = - 2$ , then all the divided differences that occur in the expression for $p ^ { \prime } ( 2 )$ have been calculated already. Check the value of $p ^ { \prime } ( 2 )$ by repeating the calculation for a different ordering of the data points.

5.3 If the data points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ have the equally spaced values $\{ x _ { i } = x _ { 0 } + i h ; i = 0 , 1 , \dots , n \}$ ,where $\boldsymbol { h }$ is a constant, then equation(5.2) impliesthatthe divideddifference $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ]$ takes the value

$$
h ^ { - n } \sum _ { k = 0 } ^ { n } ( - 1 ) ^ { n - k } { \frac { 1 } { k ! ( n - k ) ! } } f ( x _ { k } ) .
$$

Verify that this statement is consistent with the recurrence relation of Theorem 5.3.

5.4 Given the column of data points $\{ x _ { i } \}$ and the first entry in each of the other columns of Table 5.2,calculate the remaining ten entries in the table.

5.5 By following the procedure described in Section 5.5,that requires the construction of a divided difference table,obtain an expression for the polynomial in ${ \mathcal { P } } _ { 4 }$ that interpolates the function values $f ( 0 )$ and $f ( 1 )$ and the derivative values $f ^ { \prime } ( 0 ) , f ^ { \prime \prime } ( 0 )$ and $f ^ { \prime } ( 1 )$ . Check that your calculation is correct by leting $f$ be the function $\{ f ( x ) = ( x + 1 ) ^ { 4 }$ ； $0 \leqslant x \leqslant 1 \}$

5.6 Let $f \in { \mathcal { C } } ^ { ( 1 ) } [ a , b ] .$ ，and let the function values $\{ f ( x _ { i } ) ; i =$ $0 , 1 , \ldots , n \}$ and the derivative value $f ^ { \prime } ( \zeta )$ be given. Prove that there is a unique polynomial, $p$ say,in $\mathscr { P } _ { n + 1 }$ that satisfies the conditions $\{ p ( x _ { i } ) = f ( x _ { i } ) ; i = 0 , 1 , . . . , n \}$ and $p ^ { \prime } ( \zeta ) = f ^ { \prime } ( \zeta )$ ,unless $q ^ { \prime } ( \zeta )$ is zero, where $\pmb q$ is the polynomial

$$
q ( x ) = \prod _ { i = 0 } ^ { n } { \big ( } x - x _ { i } { \big ) } , \qquad a \leqslant x \leqslant b .
$$

Use Rolle's theorem to deduce that $q ^ { \prime } ( \zeta )$ is non-zero if $\pmb { \zeta }$ is in the set $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$

5.7 Let $f$ be a function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ , whose kth derivative increases strictly monotonically. Let the points $\{ x _ { i } ; i = 0 , 1 , \dots , m \}$ satisfy the conditions

$$
a \leqslant x _ { 0 } < x _ { 1 } < . ~ . ~ . < x _ { m } \leqslant b ,
$$

where the integer $^ { m }$ is greater than $\pmb { k }$ . Prove that the sequence of divided differences $\{ f [ x _ { j } , x _ { j + 1 } , \dots , x _ { j + k } ] ; j = 0 , 1 , \dots , m - k \}$ increases strictly monotonically.

When a table of differences is formed from the function values $\{ f ( x _ { i } ) ; i = 0 , 1 , \dots , n \}$ ， and when the data points are equally spaced, the denominator of the recurrence relation (5.14） is independent of $j .$ Therefore, in order to avoid a division for each value of $j ,$ it is convenient to take account of the denominator by a normalizing factor that multiplies a complete column of differences. Hence form the first-，second- and third-order differences of the data

$$
( 0 . 2 ) = 0 . 2 4 9 \ 1 2 6 \quad f ( 0 . 6 ) = 0 . 8 6 2 \ 5 6 9 \quad f ( 1 . 0 ) = 1 . 6 3 0 \ 4 3 5 .
$$

$$
f ( 0 . 3 ) = 0 . 3 8 8 0 6 2 f ( 0 . 7 ) = 1 . 0 4 0 0 2 3
$$

The data contain two errors that are indicated by the behaviour of the differences. Find and correct these errors.

5.9 Given $f$ and $\pmb { g }$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，let $h$ be the product $\{ h ( x ) =$ $f ( x ) g ( x ) ; a \leqslant x \leqslant b \}$ . Prove by induction the formula for the divided difference of a product

$$
h [ x _ { 0 } , x _ { 1 } , \ldots , x _ { n } ] = \sum _ { j = 0 } ^ { n } f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { j } ] g ( x _ { j } , x _ { j + 1 } , \ldots , x _ { n } ] .
$$

5.10 An extension of equation (5.15) provides a method of solution of the rational interpolation problem of Exercise 4.9.It depends on the assumption,which is not always true, that the required and some intermediate rational functions are well defined by interpolation conditions. For $a \leqslant x \leqslant b$ we let $r ( j , k , l , x ) =$ $p ( j , k , l , x ) / q ( j , k , l , x )$ be the value at $x$ of the rational function that satisfies the equations

$$
r ( j , k , l , x _ { i } ) = f ( x _ { i } ) , i = j , j + 1 , . . . , j + k + l ,
$$

where $\{ p ( j , k , l , x ) ; a \leqslant x \leqslant b \}$ and $\{ q ( j , k , l , x ) ; a \leqslant x \leqslant b \}$ are polynomials in $\mathcal { P } _ { k }$ and $\mathcal { P } _ { l }$ respectively. The extension of expression (5.15) is that both $r ( j , k + 1 , l , x )$ and $r ( j , k , l + 1 , x )$ have the form

$$
\frac { \left( x - x _ { j } \right) p \left( j + 1 , k , l , x \right) + c \left( x _ { j + k + l + 1 } - x \right) p \left( j , k , l , x \right) } { \left( x - x _ { j } \right) q \left( j + 1 , k , l , x \right) + c \left( x _ { j + k + l + 1 } - x \right) q \left( j , k , l , x \right) } ,
$$

where $^ c$ is a constant, whose value is chosen to give the required degree of the numerator or denominator. Let $\pmb { \chi } _ { i }$ equal $i$ for $i = 0$


<!-- chunk 0002: pages 71-140 -->
1, 2, 3, 4, and let $f$ have the values $f ( 0 ) = 0$ ， $f ( 1 ) = 1$ ， $f ( 2 ) = 3$ ， $f ( 3 ) = 4$ and $f ( 4 ) = 4$ .First calculate the polynomials $\{ r ( j , 2 , 0 , x )$ ， $0 \leqslant x \leqslant 4$ ； $j = 0 , 1 , 2 \}$ ,and then obtain the rational function $\{ r ( 0 , 2 , 2 , x ) ; 0 \leqslant x \leqslant 4 \}$ that interpolates the data by applying the given extension of equation (5.15) three times.

# The uniform convergence of polynomial approximations

# 6.1 The Weierstrass theorem

In Chapter 4 the approximation of the function

$$
f ( x ) = 1 / ( 1 + x ^ { 2 } ) , \qquad - 5 \leqslant x \leqslant 5 ,
$$

by polynomials of various degrees was considered. Each polynomial was calculated by Lagrange interpolation,and we found that, for equally spaced interpolation points,increasing the degree of the polynomial makes the accuracy of the approximation worse. For the Chebyshev interpolation points,however, Table 4.4 suggests that the calculated polynomial approximations converge uniformly to the function (6.1). It is interesting to ask whether there are functions in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that are so awkward that, even if Chebyshev interpolation points are used, the Lagrange interpolation method for polynomials of higher and higher degree gives a sequence of approximations that fails to converge uniformly. It is proved in Chapter 17 that such awkward functions do exist.

Suppose，however， that instead of defining each polynomial by Lagrange interpolation,we use some other method of calculation.Can we then generate a sequence of polynomial approximations to any function $f \in \mathcal { C } [ a , b ]$ such that uniform convergence is obtained. It is shown in Section 6.3 that the Bernstein approximation method is suit-able. Hence we obtain a constructive proof of the following well-known theorem.

# Theorem 6.1 (Weierstrass)

For any $f \in \mathcal { C } [ a , b ]$ and for any $\pmb \varepsilon > 0$ ,there exists an algebraic polynomial of the form

$$
p ( x ) = c _ { 0 } + c _ { 1 } x + . . . + c _ { n } x ^ { n } , \qquad a \leqslant x \leqslant b ,
$$

such that the bound

$$
\| f - p \| _ { \infty } \leqslant \varepsilon
$$

is satisfied.

Proof. The work of the next two sections provides a proof of this theorem.□

# 6.2 Monotone operators

Our method of proof of Theorem 6.1 depends on an interesting and remarkable property of monotone operators,which is explained in this section. The operator $\pmb { L }$ from $\mathcal { C } [ a , b ]$ to $\mathcal { C } [ a , b ]$ is defined to be monotone if it satisfies the following condition. Let $f$ and $\pmb { g }$ be any two functions in $\mathcal { C } [ a , b ]$ ， such that the inequality

$$
f ( x ) \geqslant g ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is obtained. Then the functions $L f$ and $L g$ must satisfy the condition

$$
( L f ) ( x ) \geqslant ( L g ) ( x ) , \qquad a \leqslant x \leqslant b .
$$

We note that, if $L$ is a linear operator, then the monotonicity condition is equivalent to the following simpler form. For allnon-negative functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ ,the function $L f$ must be non-negative also.

Monotone operators are useful to us because,given an infinite sequence of linear monotone operators, $\{ L _ { i } ; i = 0 , 1 , 2 , \ldots \}$ say, each one being from ${ \mathcal { C } } [ a , b ]$ to $\mathcal { C } [ a , b ] .$ ，there is a very simple test to discover whether or not the sequence of functions $\{ L _ { i } f ; i = 0 , 1 , 2 , \ldots \}$ converges uniformly to $f$ for all $f$ in $\mathcal { C } [ a , b ]$ .This test is the subject of our next theorem,and it is applied in Section 6.3 to the Bernstein operators in order to establish the Weierstrass theorem.

# Theorem 6.2

Let $\{ L _ { i } ; i = 0 , 1 , 2 , \ldots \}$ be a sequence of linear monotone operators from $\mathcal { C } [ a , b ]$ to $\mathcal { C } [ a , b ]$ .Then, if the sequence $\{ L _ { i } f ; i = 0 , 1 , 2 , \ldots \}$ converges uniformly to $f$ for the functions

$$
f ( x ) = x ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where $\dot { k } = 0$ ，1 or 2, then the sequence $\{ L _ { i } f ; i = 0 , 1 , 2 , . . . \}$ convergesuniformly to $f$ for all $f$ in $\mathcal { C } [ a , b ]$

Proof. The method of proof of the theorem is indicated in Figure 6.1. We let $\pmb { \xi }$ be any fixed point of $[ a , b ] ,$ we let $\pmb { q _ { \mathrm { \pmb { u } } } }$ be a quadratic function that is wholly above $f ,$ and we let $\pmb q _ { 1 }$ be a quadratic function that is wholly below $f ,$ where these functions are such that the difference $ { \boldsymbol { q } } _ { \mathrm { u } } ( \pmb { \xi } ) -  { \boldsymbol { q } } _ { \mathrm { l } } ( \pmb { \xi } )$ is small. The operator $L _ { n }$ is applied to the functions $q _ { \mathrm { u } } , f$ and $\pmb { q } _ { 1 }$ . Because, by hypothesis,the sequence $\{ L _ { i } f ; i = 0 , 1 , 2 , \ldots \}$ converges to $f$ when $f$ is a quadratic function, we can ensure that $L _ { n } q _ { \mathrm { { u } } }$ and $L _ { n } q _ { 1 }$ are very close to $\pmb { q _ { \mathrm { u } } }$ and $\pmb q _ { 1 }$ respectively by choosing a large value of $\pmb { n }$ .Moreover，the monotonicity of the operator $L _ { n }$ ensures that the function $L _ { n } f$ is bounded below by $L _ { n } q _ { 1 }$ and is bounded above by $L _ { n } q _ { \mathrm { { u } } }$ . Hence $( L _ { n } f ) ( \xi )$ must be close to $f ( \xi )$ . Thus the limit

$$
\operatorname* { l i m } _ { n  \infty } ( L _ { n } f ) ( \xi ) = f ( \xi )
$$

is proved for any fixed $\pmb { \xi }$ in $[ a , b ]$ . The details of the method of proof of equation (6.7), which are given below,establish the uniform convergence condition

$$
\operatorname* { l i m } _ { n \to \infty } \| f - L _ { n } f \| _ { \infty } = 0 ,
$$

which is stronger than the pointwise result (6.7).

Given $f \in { \mathcal { C } } [ a , b ] ,$ we let $\pmb \varepsilon$ be any positive number,and we choose $\pmb { \delta } > 0$ such that, if $\left| x _ { 1 } - x _ { 2 } \right| \leqslant \delta _ { \cdot }$ ，then the bound

$$
\left| f ( x _ { 1 } ) - f ( x _ { 2 } ) \right| \leqslant \varepsilon ,
$$

is obtained. Next we let $\pmb { \xi }$ be any fixed point of $[ a , b ] ,$ , and we note that $\pmb { \delta }$ is

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0002_pages_0071-0140/auto/images/8c4cb92aa8c3e1115d3f8c80a848755c314dc67ff3630f1dc4c8072250fe062a.jpg)  
Figure 6.1. The proof of the monotone operator theorem.

independent of $\xi .$ The quadratic functions $\pmb q _ { \mathbf { u } }$ and $\pmb { q } _ { 1 }$ are defined by the equations

$$
\begin{array} { r l } & { q _ { \mathbf { u } } ( x ) = f ( \xi ) + \varepsilon + 2 \| f \| _ { \infty } ( x - \xi ) ^ { 2 } / \delta ^ { 2 } \big ] , \quad a \leqslant x \leqslant b . } \\ & { \ q _ { 1 } ( x ) = f ( \xi ) - \varepsilon - 2 \| f \| _ { \infty } ( x - \xi ) ^ { 2 } / \delta ^ { 2 } \big \} , } \end{array}
$$

It follows from condition (6.9) that the inequality

$$
q _ { \mathrm { u } } ( x ) { \geq } f ( x )
$$

holds when $\vert x - \xi \vert \leqslant \delta$ ，Moreover, this inequality is also obtained when $| x - \xi | > \delta$ because of the definition of $\| f \| _ { \infty }$ . Similarly the condition

$$
q _ { 1 } ( x ) \leqslant f ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is satisfied also. Therefore the monotonicity of the operators gives the bounds

$$
( L _ { n } q _ { 1 } ) ( x ) \leqslant ( L _ { n } f ) ( x ) \leqslant ( L _ { n } q _ { \mathsf { u } } ) ( x ) , \qquad a \leqslant x \leqslant b ,
$$

for all non-negative integers $\pmb { n }$

In order to ensure that $\pmb { n }$ is large enough to prove the theorem, we express the functions $\pmb { q _ { \mathrm { u } } }$ and $\pmb q _ { 1 }$ as linear combinations of the polynomials ${ p } _ { 0 } , { p } _ { 1 }$ and $_ { p _ { 2 } }$ ,which are defined by the equation

$$
p _ { k } ( x ) = x ^ { k } , \qquad a \leqslant x \leqslant b .
$$

The definitions (6.10) give expressions of the form

$$
\begin{array} { r } { q _ { \mathbf { u } } = c _ { 0 } ( \pmb { \xi } ) p _ { 0 } + c _ { 1 } ( \pmb { \xi } ) p _ { 1 } + c _ { 2 } ( \pmb { \xi } ) p _ { 2 } } \\ { q _ { 1 } = c _ { 3 } ( \pmb { \xi } ) p _ { 0 } + c _ { 4 } ( \pmb { \xi } ) p _ { 1 } + c _ { 5 } ( \pmb { \xi } ) p _ { 2 } \} , } \end{array}
$$

and there exists a number $M ,$ that depends on $\delta , \varepsilon$ and $f$ but not on $\xi ,$ such that the bounds

$$
\left| c _ { i } ( \xi ) \right| \leqslant M , \qquad i = 0 , 1 , \ldots , 5 ,
$$

are obtained. By hypothesis, we can let $\pmb { N }$ be an integer such that the conditions

$$
\begin{array} { r } { \| p _ { k } - L _ { n } p _ { k } \| _ { \infty } \leqslant \varepsilon / M , \qquad k = 0 , 1 , 2 , } \end{array}
$$

hold for all $\begin{array} { r } { n \geqslant N . } \end{array}$ It is important to note that $\pmb { N }$ is also independent of $\xi .$ Inequality (6.17) is useful to us because,by combining it with expressions (6.15) and (6.16),and by using both the linearity of the operator $L _ { n }$ and the triangle inequality for norms,we deduce the bounds

$$
\begin{array} { c } { \| q _ { \mathrm { u } } - L _ { n } q _ { \mathrm { u } } \| _ { \infty } \leqslant 3 \varepsilon } \\ { \| q _ { \mathrm { l } } - L _ { n } q _ { \mathrm { l } } \| _ { \infty } \leqslant 3 \varepsilon } \end{array} \biggr \} .
$$

Expressions (6.13),(6.18) and (6.10) are applied in sequence to give the bound

$$
\begin{array} { r } { ( L _ { n } f ) ( \xi ) \leqslant ( L _ { n } q _ { \mathrm { u } } ) ( \xi ) } \\ { \leqslant q _ { \mathrm { u } } ( \xi ) + 3 \varepsilon } \\ { = f ( \xi ) + 4 \varepsilon . } \end{array}
$$

Similarly, by making use of $\pmb q _ { 1 }$ instead of $\pmb { q _ { \mathrm { u } } }$ , we deduce the inequality

$$
( L _ { n } f ) ( \xi ) \geqslant f ( \xi ) - 4 \varepsilon .
$$

We write expressions (6.19) and (6.20) in the form

$$
\left| f ( \xi ) - ( L _ { n } f ) ( \xi ) \right| \leqslant 4 \varepsilon , \qquad n \geqslant N .
$$

Because $\pmb { N }$ and $\pmb \varepsilon$ are independent of $\xi ,$ it follows that the stronger condition

$$
\| f - L _ { n } f \| _ { \infty } \leqslant 4 \varepsilon , \qquad n \geqslant N ,
$$

also holds. We recall that our proof has established the existence of $\pmb { N }$ for any positive $\pmb \varepsilon$ . Therefore the required limit (6.8) is obtained for any $f$ in $\mathcal { C } [ \alpha , b ]$ □

# 6.3 The Bernstein operator

The Bernstein operator $B _ { n }$ is from ${ \mathcal { C } } [ a , b ]$ to the subspace $\mathcal { P } _ { n }$ of polynomials of degree $\pmb { n }$ ,and it is defined for all positive integral values of $\pmb { n }$ . In the case when the range $[ a , b ]$ is the interval[0,1], it is specified by the equation

$$
( B _ { n } f ) ( x ) = \sum _ { k = 0 } ^ { n } { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } f ( k / n ) , \qquad 0 \leqslant x \leqslant 1 .
$$

In order to simplify notation, we assume for the rest of this chapter that the range of the variable is $0 \leqslant x \leqslant 1$ .

The Bernstein approximation (6.23) is similar to the Lagrange polynomial approximation (4.7) in two ways. Both approximation operators are linear,and in both cases the polynomial approximation that is chosen from $\mathcal { P } _ { n }$ depends just on the value of $f$ at $( n + 1 )$ discrete points of $[ a , b ]$

However, unlike Lagrange interpolation, the approximation $B _ { n } f$ may not equal $f$ when $f$ is in ${ \mathcal P } _ { n }$ .For example, suppose that $f$ is the polynomial in $\mathcal { P } _ { n }$ that takes the value one at $x = k / n$ and that is zero at the points $\{ x = j / n ; j = 0 , 1 , \ldots , n ; j \neq k \}$ Then $( B _ { n } f ) ( x )$ is a multiple of $x ^ { k } ( 1 -$ $\pmb { x } ) ^ { n - k }$ ，which is positive at thepoints $\{ x = j / n ; j = 1 , 2 , . . . , n - 1 \}$ The main advantage of Bernstein approximation over Lagrange interpolation is given in the next theorem.

# Theorem 6.3

For all functions $f$ in $\mathcal { C } [ 0 , 1 ] ,$ , the sequence $\{ B _ { n } f ; n = 1 , 2 , 3 , . . . \}$ converges uniformly to $f ,$ where $B _ { n }$ is defined by equation (6.23).

Proof. The definition (6.23) shows that $B _ { n }$ is a linear operator. It shows also that, if $f ( x )$ is non-negative for $0 \leqslant x \leqslant 1$ ， then $( B _ { n } f ) ( x )$ is nonnegative for $0 \leqslant x \leqslant 1$ . Hence $B _ { n }$ is both linear and monotone. It follows from Theorem 6.2 that we need only establish that the limit

$$
\operatorname* { l i m } _ { n \to \infty } \| B _ { n } f - f \| _ { \infty } = 0
$$

is obtained when $f$ is a quadratic polynomial. Therefor, for $j = 0 , 1 , 2$ ， we consider the error of the Bernstein approximation to the function

$$
f ( x ) = x ^ { j } , \qquad 0 \leqslant x \leqslant 1 .
$$

For $j = 0$ ，we find for all $_ n$ that $B _ { n } f$ is equal to $f$ by the binomial theorem. When $j = 1$ , the definition of $B _ { n }$ gives the equation

$$
\begin{array} { l } { ( B _ { n } f ) ( x ) = \displaystyle \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } \frac k n } \\ { = \displaystyle \sum _ { k = 1 } ^ { n } \frac { ( n - 1 ) ! } { ( k - 1 ) ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } } \\ { = x \displaystyle \sum _ { k = 0 } ^ { n - 1 } \frac { ( n - 1 ) ! } { k ! ( n - 1 - k ) ! } x ^ { k } ( 1 - x ) ^ { n - 1 - k } . } \end{array}
$$

Hence again $B _ { n } f$ is equal to $f$ by the binomial theorem. To continue the proof we make use of the identity

$$
\sum _ { k = 0 } ^ { n } { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } { \bigg ( } { \frac { k } { n } } { \bigg ) } ^ { 2 } = { \frac { n - 1 } { n } } x ^ { 2 } + { \frac { 1 } { n } } x ,
$$

which is straightforward to establish. For the case when $j = 2$ in equation (6.25), it gives the value

$$
\| B _ { n } f - f \| _ { \infty } = \operatorname* { m a x } _ { 0 \leqslant x \leqslant 1 } \left| { \frac { n - 1 } { n } } x ^ { 2 } + { \frac { 1 } { n } } x - x ^ { 2 } \right| = { \frac { 1 } { 4 n } } ,
$$

and it is important to note that the right-hand side tends to zero as $_ n$ tends to infinity. Hence the limit (6.24) is achieved for all $f \in \mathcal { P } _ { 2 }$ ，which completes the proof of the theorem.□

It follows from this theorem that,for any $f \in \mathcal { C } [ 0 , 1 ]$ and for any $\pmb \varepsilon > 0$ ， there exists $_ n$ such that the inequality

$$
\| f - B _ { n } f \| _ { \infty } \leqslant \varepsilon
$$

holds.Hence condition (6.3） can be satisfied by letting $\begin{array} { r } { p = B _ { n } f , } \end{array}$ which proves the Weierstrass theorem in the case when $[ a , b ]$ is [0, 1].

The general case,when $[ a , b ]$ may be different from [0,1],does not introduce any extra difficulties if one thinks geometrically. Imagine a function $f$ from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，that we wish to approximate to accuracy $\pmb \varepsilon$ ， plotted on graph paper. We may redefine the units on the $\pmb { x }$ -axis by a linear transformation, so that the range of interest becomes [O, 1],and we leave the plotted graph of $f$ unchanged. We apply the Bernstein operator (6.23) to the plotted function of the new variable,choosing $\pmb { n }$ to be so large that the approximation is accurate to $\pmb \varepsilon$ .We then draw the graph of the calculated approximation, and we must find that no error in the $\boldsymbol { y }$ -direction exceeds $\pmb \varepsilon$ . There are now two plotted curves. We leave them unchanged and revert to the original labelling on the $\pmb { x }$ -axis. Hence we find an approximating function that completes the proof of Theorem 3.1.

The Bernstein operator is seldom applied in practice, because the rate of convergence of $B _ { n } f$ to $f$ is usually too slow to be useful. For example, equation (6.28) shows that, in order to approximate the function $f ( x ) = x ^ { 2 }$ on [0,1] to accuracy $1 0 ^ { - 4 }$ , it is necessary to let $n = 2 5 0 0$ .However, equation (6.23) has an important application to automatic design. Here one takes advantage of the fact that the function values $\{ f ( k / n )$ ； $k =$ $0 , 1 , \ldots , n \}$ that occur on the right-hand side of the equation define $B _ { n } f$ Moreover, for any polynomial $p \in \mathcal { P } _ { n }$ ，there exist function values such that $B _ { n } f$ is equal to $p$ 、Hence the numbers $\{ f ( k / n ) ; k = 0 , 1 , . . . , n \}$ provide a parameterization of the elements of ${ \mathcal { P } } _ { n }$ .It is advantageous in design to try different polynomials by altering these parameters, because the changes to $B _ { n } f$ that occur when the parameters are adjusted separately are smooth peaked functions that one can easily become accustomed to in interactive computing.

# 6.4 The derivatives of the Bernstein approximations

The Bernstein operator possesses another property which is as remarkable as the uniform convergence result that is given in Theorem 6.3. It is that, if $f$ is in $\mathcal { C } ^ { ( k ) } [ 0 , 1 ]$ , which means that $f$ has a continuous kth derivative, then, not only does $B _ { n } f$ converge uniformly to $f ,$ but also the derivatives of $B _ { n } f$ converge uniformly to the derivatives of $f ,$ for all orders of derivative up to and including $k$ . We prove this result in the case when $k = 1$ .

# Theorem 6.4

Let $f$ be a continuously differentiable function in $\mathcal { C } [ 0 , 1 ]$ .Then the limit

$$
\operatorname* { l i m } _ { n \to \infty } \| f ^ { \prime } - ( B _ { n } f ) ^ { \prime } \| _ { \infty } = 0
$$

is obtained, where $B _ { n }$ is the Bernstein operator.

Proof. By applying Theorem 6.3 to the function $f ^ { \prime }$ ， we see that the sequence $\{ B _ { n } ( f ^ { \prime } ) ; n = 1 , 2 , 3 , . . . \}$ converges uniformly to $f ^ { \prime }$ . It is therefore sufficient to prove that the limit

$$
\operatorname* { l i m } _ { n  \infty } \| B _ { n } ( f ^ { \prime } ) - ( B _ { n + 1 } f ) ^ { \prime } \| _ { \infty } = 0
$$

is obtained. One of the subscripts is chosen to be $n + 1$ in order to help the algebra that follows.

Values of the function $( B _ { n + 1 } f ) ^ { \prime }$ can be found by differentiating the right-hand side of the definition (6.23). This is done below,and then the calculated expression is rearranged by using the divided difference nota-tion of Chapter 5,followed by an application of Theorem 5.1. Hence we obtain the equation

$$
\begin{array} { r l r } { ( B _ { n + 1 } f ) ^ { \prime } ( x ) = \displaystyle \sum _ { k = 0 } ^ { n + 1 } \frac { ( n + 1 ) ! } { ( k - 1 ) ! ( n + 1 - k ) ! } x ^ { k - 1 } ( 1 - x ) ^ { n + 1 - k } f \Bigl ( \frac { k } { n + 1 } \Bigr ) } \\ & { } & { \qquad - \displaystyle \sum _ { k = 0 } ^ { n } \frac { ( n + 1 ) ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f \Bigl ( \frac { k } { n + 1 } \Bigr ) } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { n } \frac { ( n + 1 ) ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } \Bigl \{ f \Bigl ( \frac { k + 1 } { n + 1 } \Bigr ) - f \Bigl ( \frac { k } { n + 1 } \Bigr ) \Bigr \} } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f \Bigl [ \frac { k } { n + 1 } , \frac { k + 1 } { n + 1 } \Bigr ] } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f \Bigl [ \frac { k } { n + 1 } , \frac { k } { n + 1 } \Bigr ] } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f ( \xi _ { k } ) , \qquad ( 6 . 3 ; } \end{array}
$$

where $\xi _ { k }$ is in the interval

$$
\frac { k } { n + 1 } \leqslant \xi _ { k } \leqslant \frac { k + 1 } { n + 1 } , \qquad k = 0 , 1 , \ldots , n .
$$

By using the definition (6.23) again, it follows that the modulus of the

value of the function $[ B _ { n } ( f ^ { \prime } ) - ( B _ { n + 1 } f ) ^ { \prime } ]$ at the point $x$ is bounded by the expression

$$
\begin{array} { r l r } & { } & { \bigg | \displaystyle \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } \bigg [ f ^ { \prime } \Big ( \frac { k } { n } \Big ) - f ^ { \prime } ( \xi _ { k } ) \bigg ] \bigg | } \\ & { } & { \displaystyle \leqslant \operatorname* { m a x } _ { k = 0 , 1 , \dots , n } \bigg | f ^ { \prime } \Big ( \frac { k } { n } \Big ) - f ^ { \prime } ( \xi _ { k } ) \bigg | \leqslant \omega \Big ( \frac { 1 } { n + 1 } \Big ) , } \end{array}
$$

where $\pmb { \omega }$ is the modulus of continuity of the function $f ^ { \prime }$ . The last inequality is obtained from the fact that $k / n$ ,like $\xi _ { k }$ , is in the interval $[ k / ( n + 1 )$ ， $( k + 1 ) / ( n + 1 ) ]$ . Because this last inequality is independent of $\pmb { x }$ ,we have established the condition

$$
\| B _ { n } ( f ^ { \prime } ) - ( B _ { n + 1 } f ) ^ { \prime } \| _ { \infty } \leqslant \omega \Big ( \frac { 1 } { n + 1 } \Big ) .
$$

Therefore the limit (6.31) is proved.□

It is worth noting that the middle line of equation (6.32) implies that, if the function $f$ increases strictly monotonically, then the polynomial $B _ { n + 1 } f$ also increases strictly monotonically. The Bernstein method is excellent for providing a polynomial approximation that preserves any smooth qualitative properties of the function that is being approximated. It is also useful for obtaining a differentiable approximation to a non-differentiable function, and for some other smoothing applications.

# 6 Exercises

6.1 For any $f \in \mathcal { C } [ a , b ]$ ,let $X f$ be the linear polynomial that inter-polates $f ( x _ { 0 } )$ and $f ( x _ { 1 } )$ ,where $x _ { 0 }$ and $\pmb { x } _ { 1 }$ are fixed points of $[ a , b ]$ such that $\pmb { x } _ { 0 } < \pmb { x } _ { 1 }$ . Prove that the operator $\pmb { X }$ is monotone if and only if $\scriptstyle x _ { 0 } = a$ and $x _ { 1 } = b$

6.2 By using the identity

$$
k ^ { 2 } = ( k - 1 ) ( k - 2 ) + 3 ( k - 1 ) + 1 ,
$$

prove that the Bernstein approximation to the function $\{ f ( { \pmb x } ) =$ $x ^ { 3 } ; 0 \leqslant x \leqslant 1 \}$ is the polynomial

$$
p ( x ) = { \frac { ( n - 1 ) ( n - 2 ) } { n ^ { 2 } } } x ^ { 3 } + { \frac { 3 ( n - 1 ) } { n ^ { 2 } } } x ^ { 2 } + { \frac { 1 } { n ^ { 2 } } } x , \qquad 0 \leqslant x \leqslant 1 .
$$

Note that the method of calculation can be generalized to show that, if $f \in \mathcal P _ { r }$ and if $n > r ,$ ,then the approximation $B _ { n } f$ is also in $\mathcal { P } _ { r }$

6.3 Let ${ \pmb p } = { \pmb B } _ { 6 } f ,$ where $B _ { n } f$ is the Bernstein approximation (6.23) to a function $f$ in $\mathcal { C } [ 0 , 1 ]$ .Express the function values $\{ p ( j / 6 ) ; j =$ $0 , 1 , \ldots , 6 \}$ as linear combinations of the numbers $\{ f ( j / 6 )$ ；

$j = 0 , 1 , \ldots , 6 \}$ .Hence show that, if $p$ is the polynomial in ${ \mathcal { P } } _ { 6 }$ that satisfies the conditions $p ( { \frac { 1 } { 2 } } ) = 1$ and $\{ p ( j / 6 ) = 0$ ； $j = 0$ ,1,2,4,5, $6 \}$ ，then $f$ takes the values $f ( 0 ) = f ( 1 ) = 0 .$ $\textstyle f ( { \frac { 1 } { 6 } } ) = f ( { \frac { 5 } { 6 } } ) = 2 0 / 3$ ， $f ( \scriptstyle { \frac { 1 } { 3 } } ) = f ( \frac { 2 } { 3 } ) = - 3 0 8 / 1 5$ and $f ( \scriptstyle { \frac { 1 } { 2 } } ) = 3 0$

6.4 Let $\pmb { n }$ and $\boldsymbol { r }$ be positive integers, where $n \geqslant r ,$ let $f$ be a function in $\mathcal { C } ^ { ( r ) } [ 0 , 1 ] ,$ and let $p _ { n } = B _ { n } f$ be the Bernstein polynomial (6.23). By expressing the derivative $p _ { n } ^ { ( r ) } ( 0 )$ as a linear combination of the function values $\{ f ( k / n ) ; k = 0 , 1 , \ldots , r \}$ ,prove that the equation

$$
p _ { n } ^ { ( r ) } ( 0 ) = \frac { n ! } { n ^ { r } ( n - r ) ! } f ^ { ( r ) } ( \xi )
$$

is satisfied, where $\xi$ is in the interval $[ 0 , r / n ]$ .Deduce that $\smash { p _ { n } ^ { ( r ) } }$ （0） tends to $f ^ { ( r ) } ( 0 )$ as $_ n$ tends to infinity.

Prove that the error at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ of the Bernstein approximation $B _ { n } f$ to the function $\{ f ( x ) = | x - { \frac { 1 } { 2 } } |$ ； $0 \leqslant x \leqslant 1 \}$ is of order of magnitude $n ^ { - \frac { 1 } { 2 } }$

6.6 Consider the function

$$
\phi _ { n k } ( x ) = { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } , \qquad 0 \leqslant x \leqslant 1 ,
$$

that occurs in the definition of the approximation (6.23). Investigate its properties, giving particular attention to the case when $_ n$ is large.You should find that $\phi _ { n k }$ has one peak at $x = k / n$ ， and that the width of the peak becomes narrower as $\pmb { n }$ tends to infinity. Let $\xi$ and $\pmb { \eta }$ be any two fixed points of [O,1], where $\xi$ is rational, and let the ratio $\phi _ { n k } ( \eta ) / \phi _ { n k } ( \xi )$ be calculated for an infinite sequence of pairs $( k , n )$ such that $\xi = k / n$ .Prove that the ratio tends to zero.

6.7 Let $L _ { n }$ be a linear monotone operator from $\mathcal { C } [ 0 , 1 ]$ to $\mathcal { C } [ 0 , 1 ] ,$ ， where $L _ { n } f$ depends only on the function values $\{ f ( k / n )$ ； $k =$ $0 , 1 , \ldots , n \}$ ,and let $L _ { n }$ have the property that, if $f \in { \mathcal { C } } ^ { ( 2 ) } [ 0 , 1 ] ,$ then the bound

$$
\| f - L _ { n } f \| _ { \infty } \leqslant c \| f ^ { \prime \prime } \| _ { \infty }
$$

is satisfied, where the number $c$ is independent of $f .$ By consider-ing a quadratic function that is positive on most of the range [0,1], show that $c$ is not less than $1 / 8 n ^ { 2 }$ .Further, show that the value $c = 1 / 8 n ^ { 2 }$ can be achieved by letting $L _ { n } f$ be a piecewise linear function.

6.8 By applying the technique that is used to prove Theorem 6.2, show that, if $f \in { \mathcal { C } } ^ { ( 2 ) } [ 0 , 1 ] ,$ , then the error of the approximation (6.23) satisfies the bound

$$
\| f - B _ { n } f \| _ { \infty } \leqslant [ 1 / 8 n ] \| f ^ { \prime \prime } \| _ { \infty } .
$$

Note that this bound holds as an equation when $f$ is the function $\{ f ( x ) = x ^ { 2 } ; 0 \leqslant x \leqslant 1 \} .$

9 By extending the proof of Theorem 6.4 show that, if $f \in$ $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ] ,$ ， then the limit

$$
\operatorname* { l i m } _ { n \to \infty } \| f ^ { \prime \prime } - ( B _ { n } f ) ^ { \prime \prime } \| _ { \infty } = 0
$$

is obtained.

6.10 Let $\{ f ( x , y ) ; 0 \leqslant x \leqslant 1 ; 0 \leqslant y \leqslant 1 \}$ be a continuous function of two variables,and let the function $B _ { n } f$ be obtained by applying the Bernstein approximation method to each of the variables of $f .$ Therefore $( B _ { n } f ) ( x , y )$ has the value

$$
\sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } { \frac { ( n ! ) ^ { 2 } } { j ! ( n - j ) ! k ! ( n - k ) ! } } x ^ { j } ( 1 - x ) ^ { n - j } y ^ { k } ( 1 - y ) ^ { n - k } f { \biggl ( } { \frac { j } { n } } , { \frac { k } { n } } { \biggr ) } ,
$$

where $0 \leqslant x \leqslant 1$ and $0 \leqslant y \leqslant 1$ . Prove that the infinite sequence $\{ B _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$

# 7

# The theory of minimax approximation

# 7.1 Introduction to minimax approximation

We recall from Chapter 1 that the best minimax approximation from a set $\mathcal { A }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ is the element of $\mathscr { A }$ that minimizes the expression

$$
\| f - p \| _ { \infty } = \operatorname* { m a x } _ { a \leqslant x \leqslant b } { \big | } f ( x ) - p ( x ) { \big | } , \qquad p \in { \mathcal { A } } .
$$

In this chapter we study the conditions that are satisfied by a best approximation， when $\mathscr { A }$ is a linear space. We note that they take a particularly simple form if $\mathscr { A }$ is the space $\mathcal { P } _ { n }$ of algebraic polynomials of degree at most $_ n$ . In fact this form is obtained in the more general case when $\mathscr { A }$ satisfies the‘Haar condition',which is defined in Section 7.3.In Section 7.4 some further useful properties of best minimax approximations are proved in the case when the Haar condition is obtained, including the result that the best approximation is unique. The Haar condition also provides an excellent method for calculating best approximations,called the exchange algorithm, which is described in Chapter 8 and analysed in Chapter 9.

The theory that is developed for the case when $\mathscr { A }$ is any finitedimensional linear space comes from asking the following question. Let $p ^ { * }$ be a trial approximation from $\mathcal { A }$ to $f .$ Can we find a change to $p ^ { * }$ that reduces the maximum error of the trial approximation? In other words, we seek an element $p$ in $\mathcal { A }$ such that the inequality

$$
\| f - ( p ^ { * } + \theta p ) \| _ { \infty } < \| f - p ^ { * } \| _ { \infty }
$$

is satisfied for some value of the scalar parameter $\pmb \theta$ .Figure 7.1 gives an example to explain this point of view.

In the figure the function $f ,$ which is shown in each of the four parts, is to be approximated by a straight line,so $\mathcal { A }$ is the space $\mathcal { P } _ { 1 }$ . Three trial approximaticns,namely $p _ { 1 } ^ { * } , p _ { 2 } ^ { * }$ and $\pmb { p } _ { 3 } ^ { * }$ , are shown. The vertical lines in the figure indicate where the error function of each approximation takes its maximum value. We see that the straight line $p _ { 1 } ^ { * }$ is not optimal, because the maximum error is reduced if the line is raised. The straight line $\pmb { p } _ { 2 } ^ { * }$ is not optimal either, because the maximum error can be reduced by rotating the line in a counter-clockwise direction. The straight line $\pmb { p } _ { 3 } ^ { * }$ ， however, is the best approximation from $\mathcal { P } _ { 1 }$ to $f .$ We find in Section 7.3 that the characteristic property of a best straight line approximation is that the maximum error is achieved at three points of $[ a , b ]$ with alternating sign.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0002_pages_0071-0140/auto/images/e8705c55ae5be159ffc0b5ae19e8b58bb26dfe47637ac706b6e15d1d8fef3adf.jpg)  
Figure 7.1. Minimax approximation by a straight line.

Figure 7.1 suggests that, to discover if a trial approximation is optimal, one only need consider the extreme values of the error function $\{ f ( x ) -$ $p ^ { * } ( x )$ ； $a \leqslant x \leqslant b \}$ . This remark is made rigorous in the next section. It follows that we can find a function, $\pmb { g }$ say, to add to the function of Figure 7.1,such that the best approximation is unchanged,but the best approximation from $\mathcal { P } _ { 1 }$ to $\pmb { g }$ is not the zero function. This remark is important, because it shows that in general a best minimax operator from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ to $\mathcal { A }$ is not a linear operator. Therefore the algorithms for calculating best approximations are iterative procedures.

# 7.2 The reduction of the error of a trial approximation

We let $p ^ { * }$ be a trial approximation from $\mathcal { A }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ , and we try to improve the approximation by satisfying condition (7.2). The set of points at which the error function

$$
e ^ { * } ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

takes its extreme values is important, and we call it $\mathcal { Z } _ { \mathbf { M } }$ This set is characterized by the condition

$$
\begin{array} { r } { \big | e ^ { * } ( x ) \big | = \big \| e ^ { * } \big \| _ { \infty } , \qquad x \in \mathcal { Z } _ { \bf M } . } \end{array}
$$

We suppose first that $p ^ { * }$ is not optimal. We let $( p ^ { * } + \theta p )$ be a best approximation. Hence the reduction (7.2) is obtained, and the points in $\mathcal { Z } _ { \mathbf { M } }$ satisfy the inequality

$$
| e ^ { * } ( x ) - \theta p ( x ) | < | e ^ { * } ( x ) | , \qquad x \in \mathcal { Z } _ { \mathsf { M } } .
$$

We assume without loss of generality that $\pmb \theta$ is positive.Therefore expression (7.5) shows that, if $\pmb { x }$ is in $\mathcal { L } _ { \mathbf { M } } .$ ,then the sign of $e ^ { * } ( x )$ is the same as the sign of $p ( { \pmb x } )$ . It follows that $p ^ { * }$ is a best minimax approximation from $\mathscr { A }$ to $f$ if there is no function $p$ in $\mathscr { A }$ that satisfies the condition

$$
[ f ( x ) - p ^ { * } ( x ) ] p ( x ) > 0 , \qquad x \in \mathcal { Z } _ { \bf M } .
$$

In the remainder of this section the converse result is proved, namely that, if inequality (7.6) holds for some $p$ in $\scriptstyle { \mathcal { A } }$ , then there exists a positive value of $\pmb \theta$ that gives the reduction (7.2).

Because of the way in which the exchange algorithm works，we generalize the problem of minimizing $\| f - p \| _ { \infty } ,$ ，to the problem of

minimizing the expression

$$
\operatorname* { m a x } _ { x \in \mathcal { X } } | f ( x ) - p ( x ) | , \qquad p \in \mathcal { A } ,
$$

where $\mathcal { Z }$ is any closed subset of $[ a , b ]$ , which may be $[ a , b ]$ itself, but in the exchange algorithm the set $\mathcal { X }$ is composed of a finite number of points. The next theorem allows $\mathcal { Z }$ to be general.

# Theorem 7.1

Let $\mathscr { A }$ be a linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ let $f$ be any function in $\mathcal { C } [ a , b ] ,$ let $\mathcal { Z }$ be any closed subset of $[ a , b ]$ let $p ^ { * }$ be any element of $\scriptstyle { \mathcal { A } } ,$ ， and let $\mathcal { Z } _ { \mathbf { M } }$ be the set of points of $\mathcal { Z }$ at which the error $\{ | f ( x ) - p ^ { * } ( x ) |$ ； $x \in$ $\mathcal { Z } \}$ takes its maximum value.Then $p ^ { * }$ is an element of $\mathscr { A }$ that minimizes expression (7.7) if and only if there is no function $p$ in $\pmb { \mathcal { A } }$ that satisfies condition (7.6).

Proof. The remarks made in the first paragraph of this section prove the ‘if’ part of the theorem，when $\mathcal { Z }$ is the whole interval $[ a , b ]$ It is straightforward to extend these remarks to the case when $\mathcal { Z }$ is a subset of $[ a , b ]$ .Therefore, it remains to show that, if condition (7.6) is obtained, then the inequality

$$
\operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) - \theta p ( x ) \right| < \operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) \right|
$$

holds for some value of $\pmb \theta _ { : }$ ，where $e ^ { * }$ is the error function (7.3).

We let $\pmb \theta$ be positive,and we must ensure that it is not too large.For example, if we improve the approximation $p _ { 1 } ^ { * }$ in Figure 7.1 by raising the straight line approximation, then we must be careful not to raise it too far. In order to avoid detailed consideration of the size of $p$ when we find a suitable value of $\pmb \theta$ , we assume without loss of generality that the condition

$$
| p ( x ) | \leqslant 1 , \qquad a \leqslant x \leqslant b ,
$$

holds. We have to give particular care to any values of $\pmb { x }$ for which the signs of $e ^ { * } ( x )$ and $p ( x )$ are opposite. Therefore the set $\mathcal { Z } _ { 0 }$ is defined to contain the elements $\pmb { x }$ that satisfy the condition

$$
p ( x ) e ^ { * } ( x ) \leqslant 0 , \qquad x \in { \mathcal { Z } } .
$$

Because this set is closed, and because $\mathcal { Z } _ { 0 }$ and $\mathcal { Z } _ { \mathbf { M } }$ have no points in common, the number

$$
d = \operatorname* { m a x } _ { x \in \mathcal { X } _ { 0 } } \left| e ^ { * } ( x ) \right|
$$

satisfies the bound

$$
d < \operatorname* { m a x } _ { x \in \mathcal { X } } | e ^ { * } ( x ) | .
$$

If $\mathcal { X } _ { 0 }$ is empty, we define $^ d$ to be zero. We prove that inequality (7.8) is obtained when $\pmb \theta$ has the positive value

$$
\begin{array} { r } { \theta = \frac { 1 } { 2 } [ \underset { x \in \mathcal { X } } { \operatorname* { m a x } } \left| e ^ { * } ( x ) \right| - d ] . } \end{array}
$$

Because the set $\mathcal { Z }$ is closed, we may let $\xi$ be an element of $\mathcal { X }$ that satisfies the equation

$$
\left| e ^ { * } ( \xi ) - \theta p ( \xi ) \right| = \operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) - \theta p ( x ) \right| .
$$

If $\xi$ is in $\mathcal { X } _ { 0 }$ , the bound

$$
\operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) - \theta p ( x ) \right| = \left| e ^ { * } ( \xi ) \right| + \left| \theta p ( \xi ) \right| \leqslant d + \theta
$$

is obtained, where the last term depends on expressions (7.11) and (7.9). Hence condition (7.8) follows from inequality (7.12) and equation (7.13). Alternatively, when $\xi$ is not in $\mathcal { X } _ { 0 }$ ,the signs of the terms $e ^ { * } ( \xi )$ and $p ( \xi )$ are the same, which gives the strict inequality

$$
\left| e ^ { * } ( \xi ) - \theta p ( \xi ) \right| < \operatorname* { m a x } { [ | e ^ { * } ( \xi ) | , | \theta p ( \xi ) | ] } .
$$

Again it follows that condition (7.8) is satisfied. The proof of the theorem is complete.□

This theorem justifies the remark, made in Section 7.1, that, to find out if a trial approximation is optimal, one only need consider the extreme values of the error function. Specifically, one should ask if condition (7.6) holds for some function $\pmb { p }$ in $\mathcal { A }$

# 7.3 The characterization theorem and the Haar condition

If the set $\boldsymbol { \mathcal { A } }$ of approximating functions is the space $\mathcal { P } _ { n }$ of algebraic polynomials of degree at most $\pmb { n }$ ， then it is rather easy to test whether condition (7.6) can be.obtained. We make use of the fact that a function in $\mathcal { P } _ { n }$ has at most $_ n$ sign changes. Therefore,if the error function $[ f ( x ) - p ^ { * } ( x ) ]$ changes sign more than $\pmb { n }$ times as $x$ ranges over $\mathcal { L } _ { \mathbf { M } } ,$ ,then $p ^ { * }$ is a best approximation. Conversely, if the number of sign changes does not exceed $_ n$ , then we can choose the zeros of a polynomial in ${ \mathcal { P } } _ { n }$ so that condition (7.6) is satisfied. This result is usually called the minimax characterization theorem, and it is stated formally below.

It is useful to express the theorem in a form that applies to a class of functions that includes polynomials as a special case. The usual way of defining this class is to identify the properties of polynomials that are used in the proof of the characterization theorem. They are the following two conditions:

(1) If an element of $\mathcal { P } _ { n }$ has more than $\pmb { n }$ zeros, then it is identically zero.

(2) Let $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ be any set of distinct points in the open interval $( a , b )$ ,where $k \leqslant n$ .There exists an element of ${ \mathcal P _ { n } }$ that changes sign at these points,and that has no other zeros. Moreover, there is a function in ${ \mathcal { P } } _ { n }$ that has no zeros in $[ a , b ]$

The following two properties of polynomials are required later:

(3) If a function in $\mathcal { P } _ { n }$ ,that is not identically zero, has j zeros,and if $\pmb { k }$ of these zeros are interior points of $[ a , b ]$ at which the function does not change sign, then the number $( j + k )$ is not greater than $_ n$   
(4) Let $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ be any set of distinct points in $[ a , b ] ,$ and let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be any basis of $\mathcal { P } _ { n }$ . Then the $( n + 1 ) \times$ $( n + 1 )$ matrix whose elements have the values $\{ \phi _ { i } ( \pmb { \xi } _ { j } )$ ； $i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is non-singular.

An $( n + 1 )$ -dimensional linear subspace $\pmb { \mathcal { A } }$ of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ is said to satisfy the‘Haar condition’ if these four statements remain true when $\mathcal { P } _ { n }$ is replaced by the set $\mathcal { A }$ Equivalently,any basis of $\mathscr { A }$ is called a ‘Chebyshev set'. Spaces that satisfy the Haar condition are studied in Appendix A. It is proved that properties (1), (3) and (4) are equivalent, and that these properties imply condition (2). It is usual to define the Haar condition in terms of the first property. Thus $\pmb { \mathcal { A } }$ satisfies the Haar condition if and only if,for every non-zero $p$ in $\mathcal { A } ,$ ， the number of roots of the equation $\{ p ( x ) = 0$ ； $a \leqslant x \leqslant b \}$ is less than the dimension of $\mathcal { A }$

# Theorem 7.2 (Characterization Theorem)

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \alpha , b ]$ that satisfies the Haar condition,and let $f$ be any function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .Then $p ^ { * }$ is the best minimax approximation from $\mathscr { A }$ to $f ,$ if and only if there exist $( n + 2 )$ points $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \ldots , n + 1 \}$ ,such that the conditions

$$
\begin{array} { r l } & { a \leqslant \xi _ { 0 } ^ { * } < \xi _ { 1 } ^ { * } < \ldots < \xi _ { n + 1 } ^ { * } \leqslant b , } \\ & { \left| f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) \right| = \left\| f - p ^ { * } \right\| _ { \infty } , \qquad i = 0 , 1 , \ldots , n + 1 , } \end{array}
$$

and

$$
f ( \xi _ { i + 1 } ^ { * } ) - p ^ { * } ( \xi _ { i + 1 } ^ { * } ) = - [ f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) ] , \qquad i = 0 , 1 , \dots , n ,
$$

are obtained.

Proof. We let $\mathcal { Z }$ be the interval $[ a , b ]$ in Theorem 7.1. The present theorem is proved in the way that is described in the first paragraph of this section, by making use of the properties (1) and (2) that are stated above, which hold when $\pmb { \mathcal { A } }$ satisfies the Haar condition.□

One important application of this theorem is to prove the minimum property of Chebyshev polynomials. We recall from equation (4.26) that the Chebyshev polynomial $T _ { n }$ is the polynomial of degree $_ n$ that is defined on the interval [-1,1] by the equation

$$
T _ { n } ( x ) = \cos { ( n \theta ) } , \qquad x = \cos { \theta } , \qquad 0 \leqslant \theta \leqslant \pi .
$$

The minimum property is sufficiently useful to be stated as a theorem.

# Theorem 7.3

Let the range of $_ { x }$ be[-1,1],and let $\pmb { n }$ be any positive integer. The polynomial $( { \frac { 1 } { 2 } } ) ^ { n - 1 } T _ { n }$ is the member of $\mathcal { P } _ { n }$ whose $\infty$ -norm is least, subject to the condition that the coefficient of $x ^ { n }$ is equal to one.

Proof. One way of identifying the required polynomial is to seek the values of the coeffcients $\{ c _ { i } ; i = 0 , 1 , \ldots , n - 1 \}$ that minimize the expression

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \left. x ^ { n } + \sum _ { i = 0 } ^ { n - 1 } c _ { i } x ^ { i } \right. .
$$

We see that this approach is equivalent to finding the best approximation from $\scriptstyle { \mathcal { P } } _ { n - 1 }$ to the function $\{ x ^ { n } ; - 1 \leqslant x \leqslant 1 \}$ . It follows from Theorem 7.2 that $( { \frac { 1 } { 2 } } ) ^ { n - 1 } T _ { n }$ is the required polynomial, if the coefficientof $x ^ { n }$ is one, and if there exist points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ in $[ - 1 , 1 ]$ ,arranged in ascending order, such that the equations

$$
T _ { n } ( \xi _ { i } ) = ( - 1 ) ^ { n - i } \big \| T _ { n } \big \| _ { \infty } , \qquad i = 0 , 1 , \ldots , n ,
$$

hold. The recurrence relation (4.25) implies that the coefficient of $x ^ { n }$ is correct. Moreover,the definition (7.2O) shows that equation (7.22） is satisfied if we let each $\xi _ { i }$ have the value cos $[ ( n - i ) \pi / n ]$ .The theorem is proved.□

The main reason for letting $\mathcal { Z }$ be any closed subset of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ in the statement of Theorem 7.1, is that the exchange algorithm requires the case when $\mathcal { Z }$ contains just $( n + 2 )$ points. In descriptions of the exchange algorithm it is usual to call such a set of points a ‘reference'.We use this term also,and we let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be the points of the reference. We assume that always these points are in ascending order

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < \ldots < \xi _ { n + 1 } \leqslant b .
$$

The following corollary of Theorem 7.1 is used on every iteration of the exchange algorithm.

# Theorem 7.4

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a reference, and let $f$ be any function in $\mathcal { C } [ \alpha , b ]$ Then $p ^ { * }$ is the function in $\mathscr { A }$ that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } | f ( \xi _ { i } ) - p ( \xi _ { i } ) | , \qquad p \in \mathcal { A } ,
$$

if and only if the equations

$$
f ( \xi _ { i + 1 } ) - p ^ { * } ( \xi _ { i + 1 } ) = - [ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ] , \qquad i = 0 , 1 , \dots , n ,
$$

are satisfied.

Proof. We follow the method of proof of Theorem 7.2,except that we let $\mathcal { Z }$ be the point set $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ ，instead of the interval $[ a , b ]$ □

The function $p ^ { * }$ that minimizes expression (7.24) may be calculated from the equations (7.25). It is usual to let $\pmb { h }$ be the value of $[ f ( \xi _ { 0 } ) -$ $\begin{array} { r } { p ^ { \ast } ( \xi _ { 0 } ) ] , } \end{array}$ and to choose a basis of $\mathcal { A } , \{ \phi _ { j } ; j = 0 , 1 , \dots , n \}$ say. It follows that the coefficients of the function

$$
p ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

satisfy the equations

$$
f ( \xi _ { i } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( \xi _ { i } ) = ( - 1 ) ^ { i } h , \qquad i = 0 , 1 , \dots , n + 1 ,
$$

which is a linear system in the unknowns $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ and $\pmb { h }$ Because Theorem 7.4 shows that these equations have a solution for all functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，the matrix of the system is non-singular. Hence only one element of $\mathscr { A }$ minimizes expression (7.24). A more general and more useful method of proving uniqueness is given in the next section.

# 7.4 Uniqueness and bounds on the minimax error

Suppose that the conditions of Theorem 7.2 hold, that $p ^ { * }$ and $q ^ { * }$ are both best minimax approximations from $\mathscr { A }$ to $f ,$ and that conditions (7.17),(7.18) and (7.19) are satisfied. We let $r ^ { * }$ be the function $( q ^ { * } - p ^ { * } )$ ， and we consider the numbers

$$
\begin{array} { r } { r ^ { * } ( \xi _ { i } ^ { * } ) = [ f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) ] - [ f ( \xi _ { i } ^ { * } ) - q ^ { * } ( \xi _ { i } ^ { * } ) ] , \smallskip } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

Because $\| f - q ^ { * } \| _ { \infty }$ and $\| f - p ^ { * } \| _ { \infty }$ are equal, it follows from equation (7.18)

that either $r ^ { * } ( \xi _ { i } ^ { * } )$ is zero,or its sign is the same as the sign of $[ f ( \xi _ { i } ^ { * } ) -$ $p ^ { * } ( \xi _ { i } ^ { * } ) ]$ .Hence equation (7.19) provides information about the signs of the terms of the sequence $\{ r ^ { * } ( \xi _ { i } ^ { * } ) ; i = 0 , 1 , \dots , n + 1 \}$ . It can be deduced from this information that $r ^ { * }$ is identically zero. Hence the best minimax approximation from $\mathscr { A }$ to $f$ is unique. The method of proving that $r ^ { * }$ is identically zero is a general one that has several applications. Therefore it is stated in the following theorem.

# Theorem 7.5

Let $r$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ;$ and let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a reference, such that the conditions

$$
( - 1 ) ^ { i } r ( \xi _ { i } ) \geqslant 0 , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

are satisfied. Then $r$ has at least $( n + 1 )$ zeros in $[ a , b ] ,$ provided that any double zero is counted twice, where a double zero is a zero that is strictly inside $[ a , b ] ,$ at which $r$ does not change sign.

Proof. Let $\mathscr { F }$ and $\mathscr { J }$ be the sets

$$
\begin{array} { r l } { \mathcal { G } = \{ i \colon r ( \xi _ { i } ) \neq 0 , \quad } & { { } i = 0 , 1 , \ldots , n + 1 \} } \\ { \mathcal { J } = \{ j \colon r ( \xi _ { j } ) = 0 , \quad } & { { } j = 0 , 1 , \ldots , n + 1 \} } \end{array} ,
$$

and let $n ( { \mathcal { F } } )$ and $n ( { \mathcal { F } } )$ be the number of elements in each set.The theorem is trivial if $n ( { \mathcal { F } } )$ is zero or one. Otherwise we consider the number of zeros in the interval $[ \xi _ { k } , \xi _ { l } ] ,$ where $k$ and $\iota$ are both in $\pmb { \mathcal { F } }$ ,and where no other element of $\mathscr { F }$ is in the range $[ k , l ]$ Condition (7.29) implies that the numbers $r ( \xi _ { k } )$ and $r ( \xi _ { l } )$ have the same sign if $( l - k )$ is even,and they have opposite signs if $( l - k )$ is odd.Hence the number of zeros of $r$ in the interval $[ \xi _ { k } , \xi _ { l } ]$ is at least one more than the number of points of the set $\{ \xi _ { j } ; j \in \mathcal { J } \}$ that are in this interval, provided that any double zero is counted twice. Because the number of pairs $[ \xi _ { k } , \xi _ { l } ]$ that have this property is $[ n ( { \mathcal { I } } ) - 1 ]$ , it follows that the total number of zeros of $r$ in $[ a , b ]$ is at least $[ n ( { \mathcal { I } } ) + n ( { \mathcal { J } } ) - 1 ] ,$ ，which is the required result.□

Hence we obtain the uniqueness theorem for best approximation in the 8-norm.

# Theorem 7.6

Let $\boldsymbol { \mathcal { A } }$ be a linear subspace of $\mathcal { C } [ a , b ]$ that satisfies the Haar condition.Then, for any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，there is just one best minimax approximation from $\mathscr { A }$ to $f .$

Proof. The remarks in the first paragraph of this section and Theorem 7.5 imply that, if $p ^ { * }$ and $q ^ { * }$ are both best approximations, then the function $( p ^ { * } - q ^ { * } )$ has at least $( n + 1 )$ zeros in $[ a , b ] ,$ provided that any double zero is counted twice. It follows from property (3) of Section 7.3, which is obtained when the Haar condition is satisfied, that the functions $p ^ { * }$ and $q ^ { * }$ are the same.□

Another interesting property of the Haar condition，which is the subject of Exercise 7.9, is that, if $\mathscr { A }$ is any finite-dimensional linear subspace of $\mathcal { C } [ \alpha , b ]$ that does not satisfy the Haar condition, then there are functions $f$ in $\mathcal { C } [ \alpha , b ]$ that have several best approximations in $\mathcal { A } .$

Theorem 7.5 is also useful for obtaining lower bounds on the least value of expression (7.1). Suppose that an iterative method for calculating a best approximation produces a trial approximation $p ^ { * }$ ,and that the conditions (7.17),(7.18) and (7.19) are almost satisfied. Then we usually have available a reference $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ ,such that the signs of the terms $\{ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n + 1 \}$ alternate.In this case the following theorem applies.

# Theorem 7.7

Let the conditions of Theorem 7.2 hold, let $p ^ { * }$ be any element of $\mathcal { A } ,$ and let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a reference, such that the condition

$$
\begin{array} { r } { \mathrm { s i g n } [ f ( \xi _ { i + 1 } ) - p ^ { * } ( \xi _ { i + 1 } ) ] = - \mathrm { s i g n } [ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ] , \smallskip } \\ { i = 0 , 1 , \ldots , n , } \end{array}
$$

is satisfied. Then the inequalities

$$
\begin{array} { r l } { \underset { i = 0 , 1 , \ldots , n + 1 } { \operatorname* { m i n } } \left| f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) \right| \leqslant \underset { p \in \mathcal { A } } { \operatorname* { m i n } } \underset { i = 0 , 1 , \ldots , n + 1 } { \operatorname* { m a x } } \left| f ( \xi _ { i } ) - p ( \xi _ { i } ) \right| } & { } \\ { \leqslant \underset { p \in \mathcal { A } } { \operatorname* { m i n } } \left\| f - p \right\| _ { \infty } } & { } \\ { } & { \leqslant \left\| f - p ^ { * } \right\| _ { \infty } } \end{array}
$$

are obtained. Moreover, the first inequality is strict unless all the numbers $\{ | f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) | ; i = 0 , 1 , \ldots , n + 1 \}$ are equal.

Proof. The third inequality of expression(7.32) holds because $p ^ { * }$ is in $\scriptstyle { \mathcal { A } } ,$ ， and the second one holds because the reference is a subset of $[ a , b ]$ .In order to prove the first inequality, we suppose that there exists a function $q ^ { * }$ in $\pmb { \mathcal { A } }$ that satisfies the condition

$$
\operatorname* { m i n } _ { i = 0 , 1 , \dots , n + 1 } | f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) | \geqslant \operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } | f ( \xi _ { i } ) - q ^ { * } ( \xi _ { i } ) | .
$$

If $q ^ { * }$ is equal to $p ^ { * }$ ，, then expression (7.33） shows that the numbers $\{ | f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) | ; i = 0 , 1 , \ldots , n + 1 \}$ are all the same.Thus the first part of condition (7.32) can hold as an equation. Alternatively, let us suppose that $p ^ { * }$ is not equal to $q ^ { * }$ , but that inequality (7.33) is satisfied.As in the first paragraph of this section, we let $r ^ { * }$ be the function $( q ^ { * } - p ^ { * } )$ . Because condition (7.33） implies that the numbers (7.28) have the same sign properties as before,we deduce from Theorem 7.5 and from the Haar condition that the functions $p ^ { * }$ and $q ^ { * }$ are the same,which is a contradiction. The theorem is proved.□

It is useful to note that, if $p ^ { * }$ is the best minimax approximation from $\pmb { \mathcal { A } }$ to $f ,$ and if the reference in the statement of the last theorem is the set of points $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \dots , n + 1 \}$ that occurs in conditions (7.17),(7.18) and (7.19),then all the inequalities of expression (7.32) are satisfied as equations.

# 7 Exercises

7.1 For any $f$ in $\mathcal { C } [ \alpha , b ]$ ,let $X ( f )$ be the best minimax approximation in $\mathcal { P } _ { n }$ to $f .$ Construct an example to show that the operator $\pmb { X }$ is not linear.

7.2 Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \alpha , b ] .$ let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a basis of $\scriptstyle { \mathcal { A } }$ ,let $p ^ { * }$ be a best approximation from $\pmb { \mathcal { A } }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,and let $\mathcal { Z } _ { \mathbf { M } }$ be the set that is defined by equations (7.3) and (7.4). Prove that, if $\mathcal { Z } _ { \mathbf { M } }$ contains just the discrete points $\left\{ \xi _ { j } ; j = 1 , 2 , \ldots , r \right\}$ ,and if $\pmb { H }$ is the $( n +$ $1 ) \times r$ -dimensional matrix whose elements have the values $\{ \phi _ { i } ( \xi _ { j } ) ; i = 0 , 1 , \ldots , n ; j = 1 , 2 , \ldots , r \}$ ,then the rank of $\pmb { H }$ is less than $r$

7.3 Let $\pmb { \mathcal { A } }$ be a finite-dimensional linear subspace of $\mathcal { C } [ \alpha , b ]$ ,let $p ^ { * }$ be a trial approximation from $\pmb { \mathcal { A } }$ to a function $f$ in $\mathcal { C } [ \alpha , b ]$ ,and let $\mathcal { Z } _ { \mathbf { M } }$ be the set that is defined by equations (7.3) and (7.4). Prove that $p ^ { * }$ is a best approximation from $\mathscr { A }$ to $f ,$ if there exist points $\left\{ \xi _ { j } ; j = 1 , 2 , \ldots , r \right\}$ in $\mathcal { Z } _ { \mathbf { M } }$ and non-zero multipliers $\{ \sigma _ { j } ; j =$ $1 , 2 , \ldots , r \}$ , such that, for all functions $\phi$ in $\scriptstyle { \mathcal { A } } ,$ ， the equation

$$
\sum _ { j = 1 } ^ { r } \sigma _ { j } \phi ( \xi _ { j } ) = 0
$$

holds,and such that the sign conditions

$$
\sigma _ { j } [ f ( \xi _ { j } ) - p ^ { * } ( \xi _ { j } ) ] \geqslant 0 , \qquad j = 1 , 2 , \ldots , r ,
$$

are satisfied.

7.4 Let $\pmb { n }$ be a positive integer, and let $\mathscr { A }$ be the linear space of dimension $( 2 n + 1 )$ that is spanned by the trigonometric functions $\left\{ \cos { \left( j x \right) } , - \pi + \varepsilon \leqslant x \leqslant \pi - \varepsilon ; j = 0 , 1 , \ldots , n \right\}$ and $\left\{ \sin { ( j x ) } , - \pi + \varepsilon \leqslant x \leqslant \pi - \varepsilon ; j = 1 , 2 , \ldots , n \right\} .$ ，where $\pmb \varepsilon$ isa constant from the interval $[ 0 , \pi )$ . Prove that $\pmb { \mathcal { A } }$ satisfies the Haar condition if $\pmb \varepsilon$ is positive.By considering the case when $\pmb \varepsilon$ is zero, show that conditions (1) and (2） of Section 7.3 are not equivalent.

Calculate the best approximation to the function $\{ f ( x ) = \left| x + { \frac { 1 } { 2 } } \right|$ ；   
$- 1 \leqslant x \leqslant 1 \}$ by a quadratic polynomial.

7.6 Let the conditions of Theorem 7.6 be satisfied. Prove the theorem by showing that, if $q ^ { * }$ and $r ^ { * }$ are best approximations from $\mathscr { A }$ to a function $f$ in $\mathcal { C } [ a , b ] ,$ and if $\pmb { \xi }$ is any solution of the equation $\left| f ( \xi ) - p ^ { * } ( \xi ) \right| = \| f - p ^ { * } \| _ { \infty } ,$ ，where $p ^ { * }$ is the approximation $^ { \frac { 1 } { 2 } } ( q ^ { * } + r ^ { * } )$ ,then $q ^ { * } ( \xi )$ is equal to $r ^ { * } ( \pmb { \xi } )$

7.7 Let $\mathscr { A }$ be the space $\mathcal { P } _ { 2 }$ ,let $f$ be the function $\{ f ( x ) = x ^ { 3 }$ ； $0 \leqslant x \leqslant 1 \}$ ， and let the points $\{ \xi _ { i } ; i = 0 , 1 , 2 , 3 \}$ have the values ${ \xi _ { 0 } } = 0 . 0$ ， $\xi _ { 1 } = 0 . 3$ ， $\xi _ { 2 } = 0 . 8$ and $\xi _ { 3 } = 1 . 0$ . Calculate the polynomial $p ^ { * }$ that minimizes expression (7.24).Hence the first line of expression (7.32） is satisfied as an equation. Calculate all the terms of inequality (7.32)，using Theorem 7.3 to obtain the least maximum error $d ^ { * } = \operatorname* { m i n } \left\{ \| f - p \| _ { \infty } ; p \in \mathcal { A } \right\}$ .You should find that expression (7.32） gives close upper and lower bounds on $d ^ { * }$ .

7.8 Show that the three-dimensional linear space $\mathscr { A }$ that is spanned bythefunctions $\{ \phi _ { 0 } ( { \pmb x } ) = 1$ ； $\scriptstyle - { \frac { 1 } { 6 } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ ， $\begin{array} { r } { \{ \phi _ { 1 } ( { \pmb x } ) = } \end{array}$ cos $( 2 x )$ ； $\scriptstyle - { \frac { 1 } { 6 } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ and $\left\{ \phi _ { 2 } ( x ) = \sin \left( 3 x \right) \right.$ ； $\scriptstyle - { \frac { 1 } { 6 } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ satisfies the Haar condition. It is sufficient to prove that property (4) of Section 7.3 is obtained. Show also that there is no function in $\mathscr { A }$ that is zero at the left-hand end of the range, $- \frac { 1 } { 6 } \pi ,$ and that has no other zeros. It is most unusual for a space that satisfies the Haar condition to have this property.

Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that does not satisfy the Haar condition. By using condition (4) of Section 7.3 and Exercise 7.3,show that there exists $f$ in ${ \mathcal { C } } [ a , b ]$ and a best approximation $p ^ { * }$ from $\mathscr { A }$ to $f ,$ such that the set ${ \mathcal { Z } } _ { \mathbf { M } } = \{ x : | f ( x ) - p ^ { * } ( x ) | = \| f - p ^ { * } \| _ { \infty } \}$ contains fewer than $( n + 2 )$ points. Let $\bar { p }$ be a non-zero function in $\mathscr { A }$ that is zero at the points of $\mathcal { Z } _ { \mathbf { M } }$ .By modifying $f$ if necessary, deduce from Exercise 7.3 that it is possible for $( p ^ { * } + \theta \bar { p } )$ to be a best approximation from $\mathscr { A }$ to $f$ for a range of values of the number $\pmb \theta _ { \mathrm { i } }$ , which proves that not every element of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ has a best minimax approximation in $\mathcal { A } .$

7.10 In a discrete minimax calculation the numbers $\{ f _ { i } ; i =$ $1 , 2 , \ldots , m \}$ and $\{ \phi _ { i j } ; i = 1 , 2 , \ldots , m ; j = 0 , 1 , \ldots , n \}$ are given, andone requiresthe values ofthe parameters $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ that minimize the expression

$$
\operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \bigg | f _ { i } - \sum _ { j = 0 } ^ { n } \phi _ { i j } \lambda _ { j } \bigg | .
$$

Investigate the relevance of the theory of this chapter to this calculation. Hence show that the least value of the expression max $: [ \left. 2 - 4 \lambda _ { 1 } - 5 \lambda _ { 2 } \right. , \left. 3 - 5 \lambda _ { 1 } - 6 \lambda _ { 2 } \right. , \left. 4 - 6 \lambda _ { 1 } - 8 \lambda _ { 2 } \right. ]$ is equal to $\scriptstyle { \frac { 2 } { 7 } }$

# The exchange algorithm

# 8.1 Summary of the exchange algorithm

Let $f$ be a function in ${ \mathcal { C } } [ a , b ] ,$ and let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition.The exchange algorithm calculates the element of $\mathscr { A }$ that minimizes the maximum error

$$
\| f - p \| _ { \infty } = \operatorname* { m a x } _ { a \leqslant x \leqslant b } | f ( x ) - p ( x ) | , \qquad p \in \mathcal { A } .
$$

Instead of trying to reduce the error of each trial approximation, the algorithm adjusts a reference $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ , so that it converges to a point set $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \dots , n + 1 \}$ ， that satisfies the conditions of Theorem 7.2. The adjustments are made by an iterative procedure.

In order to begin the calculation,an initial reference is chosen.It can be any set of points that satisfies the condition

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < \ldots < \xi _ { n + 1 } \leqslant b ,
$$

but a particular choice that is suitable when $\mathscr { A }$ is the space $\mathcal { P } _ { n }$ is given in Section 8.4. At the start of each iteration a reference is available that is different from the references of all previous iterations.The calculations of each iteration are as follows.

We let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be the reference at the start of an iteration. First the function $p$ in $\mathscr { A }$ that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } \big | f ( \xi _ { i } ) - p ( \xi _ { i } ) \big | , \qquad p \in \mathcal { A } ,
$$

is calculated. Theorem 7.4 shows that the coefficients of $p$ may be found by solving the linear system of equations

$$
f ( \xi _ { i } ) - p ( \xi _ { i } ) = ( - 1 ) ^ { i } h , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

where,as in equation (7.27), $\pmb { h }$ is also defined by the linear system. It follows from Theorem 7.7 that the bounds

$$
\lvert h \rvert \leqslant \lVert f - p ^ { * } \rVert _ { \infty } \leqslant \lVert f - p \rVert _ { \infty }
$$

are satisfied, where $p ^ { * }$ is the required best approximation from $\mathcal { A }$ to $f .$ In order to make use of the right-hand bound,and in order to obtain a suitable change to the reference, the error function

$$
e ( x ) = f ( x ) - p ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is considered.

A typical error function in the case ${ n = 3 }$ is shown in Figure 8.1. We see that equation (8.4) is satisfied,and that consequently $_ e$ has at least $_ { n }$ turning points. The positions of the extrema,which are called $\eta _ { 1 } , \eta _ { 2 }$ and $\pmb { \eta _ { 3 } }$ in the figure,are estimated by evaluating the error function at several points of $[ a , b ]$ . It is necessary in practice to obtain these points automa-tically in an effcient way. Suitable methods are based on local quadratic fits to the error function,but we assume that the abscissae of the extrema can be found exactly. We let $\pmb { \eta }$ be a point that satisfes the equation

$$
\left| f ( \eta ) - p ( \eta ) \right| = \| f - p \| _ { \infty } .
$$

The calculation finishes if the difference

$$
\delta = \left| f ( \eta ) - p ( \eta ) \right| - \left| h \right|
$$

is sufficiently small, because inequality (8.5) implies the bound

$$
\| f - p \| _ { \infty } \leqslant \| f - p ^ { * } \| _ { \infty } + \delta .
$$

Otherwise the reference is changed in order to begin another iteration. In the ‘one-point exchange algorithm’ the new reference, $\begin{array} { r } { \{ \xi _ { i } ^ { + } ; i = 0 , } \end{array}$ $1 , \ldots , n + 1 \}$ say, contains $\pmb { \eta }$ and $( n + 1 )$ of the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots ,$ $n + 1 \}$ ，which are specified in the next section. The most important property of the change of reference is that the quantity $| h |$ ,which is called the levelled reference error, increases strictly monotonically from iteration to iteration.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0002_pages_0071-0140/auto/images/fb41900dda36b867e87768be799afa864668b8f2c9a49d2ee3648a81681ddf6a.jpg)  
Figure 8.1. An error function of the exchange algorithm.

Because it is convenient to regard the levelled reference error as a function of the reference, we use the notation

$$
h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } ) = | h | .
$$

It is helpful to take the point of view that the purpose of the change of reference is to increase the value of $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ .Because expres-sion (8.8) is small only if the levelled reference error is close to the bound $\| f - p ^ { * } \| _ { \infty }$ ofinequality (8.5)， it is advantageous to make $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ as large as possible. Thus the exchange algorithm is a method of solving a maximization problem,where the variables are the points of the reference. The structure of $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ ,however, is such that it is inefficient to use one of the superlinearly convergent algorithms that are available in subroutine libraries for general maximization calculations.

# 8.2 Adjustment of the reference

As in the previous section,we consider an iteration of the exchange algorithm that calculates a function $p$ in $\mathscr { A }$ by solving the equations (8.4),and that changes the reference from $\{ \xi _ { i } ; i = 0 , 1 , \ldots ,$ $n + 1 \}$ to $\{ \xi _ { i } ^ { + } ; i = 0 , 1 , \ldots , n + 1 \}$ . The method of choosing the new reference depends on Theorem 7.7,for it states conditions that imply the increase

$$
h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \ldots , \xi _ { n + 1 } ^ { + } ) > h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )
$$

in the levelled reference error. The theorem shows that it is sufficient if the conditions

$$
\begin{array} { r l } & { \mathsf { s i g n } \left[ f ( \xi _ { i + 1 } ^ { + } ) - p ( \xi _ { i + 1 } ^ { + } ) \right] } \\ & { \quad = - \mathsf { s i g n } \left[ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right] , \qquad i = 0 , 1 , \ldots , n , } \end{array}
$$

and

$$
\begin{array} { r } { \big | f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \big | \geqslant \big | h \big | , \qquad i = 0 , 1 , \ldots , n + 1 , } \end{array}
$$

are satisfied, provided that at least one of the numbers $\{ \vert f ( \pmb { \xi } _ { i } ^ { + } ) - p ( \pmb { \xi } _ { i } ^ { + } ) \vert$ ； $i = 0 , 1 , \ldots , n + 1 \}$ is greater than $| h |$ .Hence,several ways of obtaining an increase in the levelled reference error are suggested by Figure 8.1.

One method is to let each point of the new reference be an extremum of the error function (8.6). In this case the error curve of Figure 8.1 gives the reference $\left\{ \xi _ { 0 } , \eta _ { 1 } , \eta _ { 2 } , \eta _ { 3 } , \xi _ { 4 } \right\}$ ， and we note that conditions (8.12） and (8.13)are obtained. Methods that can change every reference point on every iteration are usually more efficient than the one-point exchange algorithm, in the sense that fewer iterations are required to reduce the number (8.8) to less than a prescribed tolerance.We give our attention, however, to the one-point method, because it is interesting to discover the way in which it achieves a fast rate of convergence.An advantage of the one-point method is that the work of solving the equations (8.4) may be reduced, by using techniques for updating matrix factorizations.

In the one-point exchange algorithm, we let $\xi _ { q }$ be the point that leaves the old reference to make room for $\pmb { \eta }$ .For example,in Figure 8.1,because $\pmb { \eta _ { 1 } }$ is the solution of equation (8.7),we let $q = 1$ , in order that the new reference is the set $\left\{ \xi _ { 0 } , \eta _ { 1 } , \xi _ { 2 } , \xi _ { 3 } , \xi _ { 4 } \right\}$ .No other choice of $q$ allows condition (8.12) to be satisfed. Provided that $| h |$ is positive, it is true generally that condition (8.12) and the value of $\pmb { \eta }$ determine the point that leaves the reference uniquely. The case when $| h |$ is zero can occur only on the first iteration,and then any value of $\pmb q$ gives the increase (8.11).

When $| h |$ is positive,and when $\pmb { \eta }$ is inside the interval $[ \xi _ { 0 } , \xi _ { n + 1 } ] ,$ the value of $\pmb q$ is such that the signs of $[ f ( \eta ) - p ( \eta ) ]$ and $[ f ( \pmb { \xi } _ { q } ) - p ( \pmb { \xi } _ { q } ) ]$ are the same,and no point of the old reference is between $\xi _ { q }$ and $\pmb { \eta }$ .When $\pmb { \eta } < \pmb { \xi } _ { 0 }$ ， then $\xi _ { q }$ is either $\pmb { \xi _ { 0 } }$ or $\xi _ { n + 1 }$ . We let $q$ be zero if the signs of $[ f ( \eta ) - p ( \eta ) ]$ and $[ f ( \pmb { \xi } _ { 0 } ) - p ( \pmb { \xi } _ { 0 } ) ]$ are the same, otherwise it is necessary to let $q$ be $( n + 1 )$ .A similar rule determines the value of $q$ when $\pmb { \eta }$ is greater than $\xi _ { n + 1 }$ ·

The description of the one-point exchange algorithm is now complete. An example of its use is given in the next section,and some of its convergence properties are studied in Chapter 9.

# 8.3 An example of the iterations of the exchange algorithm

In order to show the convergence properties of the one-point exchange algorithm, this section describes the numerical results that are obtained when $\mathcal { A }$ is the two-dimensional linear space of functions of the form

$$
p ( x ) = \lambda _ { 0 } x + \lambda _ { 1 } x ^ { 2 } , \qquad 0 \leqslant x \leqslant \pi / 2 ,
$$

when $f$ is the function

$$
f ( x ) = \sin x , \qquad 0 \leqslant x \leqslant \pi / 2 ,
$$

and when the reference of the first iteration contains the points {0.5,1.0, $\pi / 2 \}$ .Because $p ( 0 )$ is equal to $f ( 0 )$ for all values of the coefficients $\lambda _ { 0 }$ and $\lambda _ { 1 }$ ,the first point of the reference is positive throughout the calculation. Because the only extrema of the error $\{ f ( { \pmb x } ) - { \pmb p } ( { \pmb x } ) _ { \pmb \mathrm { \| } }$ $0 \leqslant x \leqslant \pi / 2 \}$ occur near $\xi _ { 0 }$ and $\xi _ { 1 }$ , the point $\pi / 2$ never leaves the reference.Hence the error function shown in Figure 8.2 is typical, and we let $\pmb { \eta _ { 0 } }$ and $\pmb { \eta } _ { 1 }$ be the abscissae of its turning points. Therefore,if another iteration is required, its reference is either $\{ \eta _ { 0 } , \xi _ { 1 } , \xi _ { 2 } \}$ or $\{ \xi _ { 0 } , \eta _ { 1 } , \xi _ { 2 } \}$ ，where the one that is chosen depends on which is the larger of the numbers $\left| e ( \eta _ { 0 } ) \right|$ and $\left| e ( \eta _ { 1 } ) \right|$

Tables 8.1 and 8.2 give the levelled reference errors and the extrema that occur on the first five iterations. We note that the levelled reference errors increase strictly monotonically and that the values of $\| f - p \| _ { \infty }$ decrease monotonically. Both these sequences seem to be converging rapidly to the same limit. Hence inequality (8.5） provides excellent bounds on the least maximum error. For example,after only three iterations,we find that the bounds

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0002_pages_0071-0140/auto/images/370b9bf3720c651e41bd93622b727169f9fccbb19f1d97ad749fac8799cc9706.jpg)  
Figure 8.2. An error function of the example of Section 8.3.

Table 8.1. The references of the example of Section 8.3   

<table><tr><td>Iteration</td><td>50</td><td>51</td><td>5</td><td>h(50,51,52）</td></tr><tr><td>1</td><td>0.500 000</td><td>1.000 000</td><td>1.570 796</td><td>0.013 998 30</td></tr><tr><td>2</td><td>0.298 938</td><td>1.000 000</td><td>1.570 796</td><td>0.016 978 02</td></tr><tr><td>3</td><td>0.298 938</td><td>1.104 968</td><td>1.570 796</td><td>0.017 482 78</td></tr><tr><td>4</td><td>0.283880</td><td>1.104 968</td><td>1.570 796</td><td>0.017 501 65</td></tr><tr><td>5</td><td>0.283 880</td><td>1.106 124</td><td>1.570 796</td><td>0.017 501 72</td></tr></table>

Table 8.2. The extrema of the error function of the example of Section 8.3   

<table><tr><td>Iteration</td><td>no</td><td>e(no)</td><td>n1</td><td>e(n1)</td></tr><tr><td>1</td><td>0.298 938</td><td>-0.019 659 29</td><td>1.133 035</td><td>0.016 193 66</td></tr><tr><td>2</td><td>0.279 792</td><td>-0.017 039 99</td><td>1.104 968</td><td>0.018 391 16</td></tr><tr><td>3</td><td>0.283 880</td><td>-0.017 521 06</td><td>1.106 316</td><td>0.017 483 03</td></tr><tr><td>4</td><td>0.283 733</td><td>-0.017 501 66</td><td>1.106 124</td><td>0.017 501 83</td></tr><tr><td>5</td><td>0.283 733</td><td>-0.017 501 72</td><td>1.106 124</td><td>0.017 501 72</td></tr></table>

$$
0 . 0 1 7 4 8 2 7 8 \leqslant \left\| f - p ^ { * } \right\| \leqslant 0 . 0 1 7 5 2 1 0 6
$$

are satisfied. Further, the maximum error of the approximation that is calculated on the fifth iteration agrees with the least maximum error to eight decimal places.It is highly satisfactory to obtain this accuracy in so few iterations.

Another interesting feature of the tables is that the abscissae $\pmb { \eta _ { 0 } }$ and $\pmb { \eta } _ { 1 }$ of the extrema of the error function are rather insensitive to the changes that are made to the points of the reference. It is proved in the next chapter that this property holds generally,and that it provides the fast rate of convergence.

We note also that the set $\pmb { \mathcal { A } }$ of the example does not satisfy the Haar condition, because many members of $\mathscr { A }$ have two zeros in the range $[ 0 , \pi / 2 ]$ .One of these zeros is always at $\scriptstyle x = 0$ .Hence the Haar condition is obtained on the range $[ \alpha , \pi / 2 ]$ ，where $\pmb { \alpha }$ is any fixed positive number that is less than $\pi / 2$ . It does not matter in this example that the Haar condition is not obtained. In general, however,before applying the exchange algorithm, one should check that $\mathscr { A }$ satisfies the Haar condition, because it is important to the remark that equation (8.4) defines the function $p$ that minimizes expression (8.3).

# 8.4 Applications of Chebyshev polynomials to minimax approximation

A very nice property of the exchange algorithm, which is proved in Chapter 9,is that, if the Haar condition holds,then convergence is obtained from any initial reference.However, some initial references are better than others,if one wishes to avoid the calculation of approximations whose errors are much larger than necessary. The problem of choosing a good initial reference is similar to the problem of choosing good interpolation points,which was considered in Chapter 4.When $\mathscr { A }$ is the space $\mathcal { P } _ { n }$ ，a suitable initial reference can be obtained from the properties of Chebyshev polynomials. Specifically,if the range of $x$ is [-1,1], we let the points of the initial reference have the values

$$
\xi _ { i } = \cos { [ ( n + 1 - i ) \pi / ( n + 1 ) ] } , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

because this choice has the following property.

# Theorem 8.1

Let $f \in \mathcal { C } [ - 1 , 1 ]$ ,and let $\pmb { p } \in \mathcal { P } _ { n }$ be the approximation to $f$ that is calculated by an iteration of the exchange algorithm, where the reference contains the points (8.17). If $f$ is a polynomial of degree $( n + 1 )$ ,then $p$ is the best minimax approximation from ${ \mathcal P _ { n } }$ to $f .$

Proof. Equation (8.17) and the definition of the Chebyshev polynomial $T _ { n + 1 }$ imply the values

$$
T _ { n + 1 } ( \xi _ { i } ) = ( - 1 ) ^ { n + 1 - i } , \qquad i = 0 , 1 , \dots , n + 1 .
$$

Because $( f - p )$ is in $\mathcal { P } _ { n + 1 }$ , it follows from equation (8.4) that the error function $\left( f - p \right)$ is a multiple of $T _ { n + 1 }$ .Therefore,by the Characterization Theorem 7.2, $p$ is the best approximation from $\mathcal { P } _ { n }$ to $f .$ □

Theorem 8.1 is useful, not only when $f$ is in $\mathcal { P } _ { n + 1 }$ , but also when $f$ is infinitely differentiable,and its Taylor series

$$
f ( x ) = \sum _ { j = 0 } ^ { \infty } \frac { x ^ { j } } { j ! } f ^ { ( j ) } ( 0 ) , \qquad - 1 \leqslant x \leqslant 1 ,
$$

is rapidly convergent. In this case it happens often that the error of the best approximation from $\mathcal { P } _ { n }$ to $f$ is dominated by the error that comes from the term $x ^ { n + 1 } f ^ { ( n + 1 ) } ( 0 ) / ( n + 1 ) !$ . Theorem 8.1 shows that the reference (8.17) makes this contribution to the error as small as possible. Moreover,by regarding the calculation of $\pmb { p }$ in Theorem 8.1 as a linear operator from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ ,and by finding the norm of this operator, it follows from Theorem 3.1 that the ratio of $\| f - p \|$ to the least maximum error is bounded by a small multiple of ln $\pmb { n }$ ，for all functions $f$ in $\mathcal { C } [ - 1 , 1 ]$

The reference points (8.17） are appropriate only for the interval [-1,1]. For the general range $[ a , b ] ,$ , it is helpful to recall the discussion, given in Section 6.3,of suitable changes to the Bernstein operator when [0,1] is replaced by $[ a , b ]$ .We again think of $[ a , b ]$ as an interval on the $x$ -axis of the graph of the function $\{ f ( x ) ; a \leqslant x \leqslant b \}$ ,and now we apply a linear transformation to the variable, so that this interval can be relabelled as[-1,1]. The points (8.17) are suitable for the new range of $\pmb { x }$ If we express them in terms of the original variable we have the values

$$
\begin{array} { c } { { \xi _ { i } = \frac { 1 } { 2 } ( a + b ) + \frac { 1 } { 2 } ( b - a ) \cos \Big [ \frac { ( n + 1 - i ) \pi } { ( n + 1 ) } \Big ] , } } \\ { { i = 0 , 1 , \dots , n + 1 , } } \end{array}
$$

which is therefore a suitable reference for the general range $[ a , b ]$ ,when $\pmb { \mathcal { A } }$ is the space $\mathcal { P } _ { n }$

Another application of Chebyshev polynomials to minimax approximation is that they provide a technique that is called ‘telescoping'. In order to describe it, we suppose that we have an approximation

$$
\bar { p } ( x ) = \bar { c } _ { 0 } + \bar { c } _ { 1 } x + . . . + \bar { c } _ { n + 1 } x ^ { n + 1 } , \qquad - 1 \leqslant x \leqslant 1 ,
$$

from $\mathcal { P } _ { n + 1 }$ to a function $\mathsf { \Omega } _ { | f \mathbf { i n } } \mathcal { C } [ - 1 , 1 ] ,$ , but that there is a possibility that an approximation from $\mathcal { P } _ { n }$ may be sufficiently accurate. For instance,we may have the bound

$$
\left\| f - { \bar { p } } \right\| \leqslant { \bar { \varepsilon } } ,
$$

but we may be able to accept any approximation $p$ that satisfies the condition

$$
\| f - p \| \leqslant \varepsilon ,
$$

where $\pmb \varepsilon$ is greater than $\pmb { \bar { \varepsilon } }$ It follows from the triangle inequality for norms that $p$ is an adequate approximation if the bound

$$
\left\| p - { \bar { p } } \right\| \leqslant \varepsilon - { \bar { \varepsilon } }
$$

is obtained.This inequality is useful because it gives some freedom in the approximating function that does not depend on $f .$ In particular we ask whether it allows $p$ to be in $\mathcal { P } _ { n }$ .Theorem 7.3 shows that the answer is affirmative if and only if the condition

$$
\begin{array} { r } { \big | \bar { c } _ { n + 1 } \big | ( \frac { 1 } { 2 } ) ^ { n } \big | \big | T _ { n + 1 } \big | \big | \leqslant \varepsilon - \bar { \varepsilon } } \end{array}
$$

holds.Therefore, because the norm of $T _ { n + 1 }$ is one, it is appropriate to test the inequality

$$
\left| { \bar { c } } _ { n + 1 } \right| \leqslant 2 ^ { n } ( \varepsilon - { \bar { \varepsilon } } ) .
$$

If it is satisfed, then $\bar { p }$ may be replaced by the approximation

$$
p = \bar { p } - \bar { c } _ { n + 1 } \bigl ( \frac 1 2 \bigr ) ^ { n } T _ { n + 1 } ,
$$

which is in $\mathcal { P } _ { n }$ . Hence we obtain the bound

$$
\| f - p \| \leqslant \bar { \varepsilon } + ( \frac { 1 } { 2 } ) ^ { n } \bigl | \bar { c } _ { n + 1 } \bigr | ,
$$

which may allow the procedure to be repeated to give a sufficiently accurate approximation in $\mathcal { P } _ { n - 1 }$

# 8.5 Minimax approximation on a discrete point set

It happens sometimes that it is not possible or not convenient to calculate the function $f$ in $\mathcal { C } [ \alpha , b ]$ ,that is to be approximated,at any point of the range $[ a , b ]$ Instead $f$ may be known on a set of points $\{ x _ { i } ; i =$ $1 , 2 , \ldots , m \}$ ,that are in ascending order

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b .
$$

In this case the function $p$ in $\mathscr { A }$ that minimizes the discrete maximum error

$$
\operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \big | f ( x _ { i } ) - p ( x _ { i } ) \big | , \qquad p \in \mathcal { A } ,
$$

may be required. If $\mathscr { A }$ is a linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, and if $^ { m }$ is greater than the dimension of $\mathcal { A } _ { : }$ , then the exchange algorithm is an excellent procedure for calculating this approximation. We let each reference be a subset of $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ On each iteration the equations (8.4) are solved to define the trial approximation $p$ .Instead of expression (8.5),the bounds

$$
\left| h \right| \leqslant \operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \left| f ( x _ { i } ) - p ^ { * } ( x _ { i } ) \right| \leqslant \operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \left| f ( x _ { i } ) - p ( x _ { i } ) \right|
$$

hold, where $p ^ { * }$ is still the required approximation. Now the point that is brought into the reference is an element of the set $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ that satisfies the equation

$$
\left| f ( \eta ) - p ( \eta ) \right| = \operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \left| f ( x _ { i } ) - p ( x _ { i } ) \right| ,
$$

instead of equation (8.7). The procedure for changing the reference is the same as before.

One advantage of the calculation in the discrete case is that it is much easier to prove convergence.

# Theorem 8.2

Let $\mathcal { A }$ be a finite-dimensional subspace of $\mathcal { C } [ a , b ]$ that satisfies the Haar condition. Let $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ be a set of distinct points from $[ a , b ] ,$ ，where $^ { m }$ is not less than the dimension of $\mathcal { A } .$ For any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ , let the one-point exchange algorithm be applied to calculate the element of $\mathscr { A }$ that minimizes expression (8.3O). Then the required approximation to $f$ is obtained in a finite number of iterations.

Proof. The calculation ends if both parts of expression (8.31） are satisfied as equations. Otherwise the procedure for changing the reference causes the levelled reference errors to increase strictly monotonically.The number of different levelled reference errors is at most the number of different references,but this number is finite.Therefore the calculation of the algorithm is a finite process.□

It would not be sensible to obtain from the theorem an upper bound on the number of iterations of the algorithm, because the bound would be very pessimistic. Instead, the main value of the theorem is to show that the exchange algorithm terminates in an important special case, provided that one takes suitable precautions against the effects of computer rounding errors.

Because there is a need sometimes to solve minimax approximation calculations when $\mathcal { A }$ does not satisfy the Haar condition, it is useful to note that, in the discrete case, the calculation can be expressed as a linear programming problem. We let $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ be a basis of $\mathcal { A }$ ,and we express a general element of $\mathcal { A }$ in the form

$$
p = \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } .
$$

The least value of expression (8.30) is the smallest real number $\pmb \theta$ that satisfies the conditions

$$
- \theta \leqslant f ( x _ { i } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( x _ { i } ) \leqslant \theta , \qquad i = 1 , 2 , \ldots , m ,
$$

for some values of the coefficients $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ . Therefore the variables of the linear programming calculation are $\pmb \theta$ and $\{ \lambda _ { j } ; ~ j =$ $0 , 1 , \ldots , n \}$ ，the objective function is $\pmb \theta$ ，and the constraints are the conditions (8.34).The final values of the variables $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ are the coefficients of the function in $\mathcal { A }$ that minimizes expression (8.30).

Basically the one-point exchange algorithm is a standard linear pro-gramming procedure for solving the dual version of the linear programming calculation that has just been mentioned. However, the Haar condition is useful, because it allows the point that leaves the reference to be found from the sign properties of the current error function,which gives a geometric point of view of the algorithm. Several advantages are lost if one supposes instead that minimax approximation is a special case of linear programming. In particular it is less easy to make use of the fact that the functions $f$ and $p$ are in $\mathcal { C } [ \alpha , b ] .$ ，which is important to the convergence theory of the next chapter.

# 8 Exercises

8.1 Let the exchange algorithm be applied to calculate the best approximation from $\mathcal { P } _ { n }$ to a function $f$ in ${ \mathcal { C } } [ a , b ]$ . Prove that the levelled reference error (8.10) is the modulus of the divided difference $f [ \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } ]$ multiplied by a number that is independent of $f .$ In particular, show that when $n = 1$ the levelled reference error is the expression

8.2 The exchange algorithm is applied to calculate the best approximation from $\mathcal { P } _ { 1 }$ to a convex function in $\mathcal { C } [ \alpha , b ]$ .(The function $f$ is convex if, for any $\scriptstyle x _ { 0 }$ and $x _ { 1 }$ in $[ a , b ]$ and any $\pmb \theta$ in [0,1], the inequality

$$
f ( \theta x _ { 0 } + [ 1 - \theta ] \dot { x } _ { 1 } ) \leqslant \theta f ( x _ { 0 } ) + ( 1 - \theta ) f ( x _ { 1 } )
$$

is satisfied.) Show that, if the initial reference includes the points ${ \pmb \xi } _ { 0 } = { \pmb a }$ and $\pmb { \xi } _ { 2 } = \pmb { b }$ ,then at most two iterations are required.

Show that the best approximation from $\mathcal { P } _ { 2 }$ to the function $\{ f ( x ) = 1 4 4 / ( x + 2 )$ ； $0 \leqslant x \leqslant 6 \}$ is the quadratic $\{ p ^ { * } ( x ) = 6 9 -$ $2 0 x + 2 x ^ { 2 }$ ； $0 \leqslant x \leqslant 6 \}$ , and that the extreme values of the error function occur at the points $\xi _ { 0 } ^ { * } = 0$ ， $\pmb { \xi } _ { 1 } ^ { * } = 1$ ， $\pmb { \xi } _ { 2 } ^ { * } = 4$ and $\pmb { \xi } _ { 3 } ^ { \ast } = 6$ Let the exchange algorithm be used to calculate $p ^ { * }$ , and let the reference points of an iteration have the values ${ \xi _ { 0 } } = 0$ ， $\xi _ { 1 } = 1 + \alpha _ { : }$ ， $\pmb { \xi } _ { 2 } = 4 + \pmb { \beta }$ ， $\xi _ { 3 } = 6$ .Prove that, if $\pmb { \alpha }$ and $\beta$ are so small that one can neglect terms of order $\alpha ^ { 2 } , \alpha \beta$ and $\beta ^ { 2 }$ , then the function $\{ p ( { \pmb x } )$ ； $0 \leqslant x \leqslant 6 \}$ that satisfies equation (8.4) is equal to $p ^ { * }$

8.4 Let the iterations of the one-point exchange algorithm calculate the sequence of approximations $\{ p _ { k } ; ~ k = 1 , 2 , 3 , . . . \}$ from a linear space $\mathscr { A }$ to a function $f$ in $\mathcal { C } [ \alpha , b ]$ . Construct an example to show that the errors {b $^ { \mathsf { c } } - p _ { k } \| _ { \infty }$ ； $k = 1 , 2 , 3 , \ldots \}$ do not always decrease monotonically.

8.5 Let $_ n$ be a non-negative integer. Show that the definition of the approximation $p$ to $f$ in Theorem 8.1 can be regarded as a linear operator from $\mathcal { C } [ - 1$ ,1] to ${ \mathcal { P } } _ { n }$ . Show also that, when $\pmb { n } = 2$ ,the ∞-norm of this operator has the value $\frac { 5 } { 3 }$

3.6 A polynomial approximation $\{ p ( x ) ; - 1 \leqslant x \leqslant 1 \}$ to the function $\{ f ( x ) = \ln \left( 1 + { \frac { 1 } { 2 } } x \right)$ ； $- 1 \leqslant x \leqslant 1 \}$ is required that satisfies the condition $\| f - p \| _ { \infty } { \leqslant } 0 . 0 1$ . One method of calculation is to take sufficient terms in the Taylor series expansion of $f$ about $\boldsymbol { x } = 0$ ， and then to reduce the degree of the polynomial by the telescoping procedure that is described in Section 8.4. Show that this method gives a polynomial of degree three.

8.7 Apply the discrete version of the one-point exchange algorithm to calculate the best approximation from $\mathcal { P } _ { 1 }$ to the following seven function values: $f ( 0 ) = 0 . 3$ ， $f ( 1 ) = 4 . 2$ ， $f ( 2 ) = 0 . 1$ ， $f ( 3 ) =$ 3.4, $f ( 4 ) = 5 . 7 , f ( 5 ) = 4 . 9$ ,and $f ( 6 ) = 5 . 7$ . Let the initial reference be the set of points $\{ 0 , 3 , 6 \}$

8.8 Let $\mathscr { A }$ be a linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, and let the one-point exchange algorithm be applied to calculate the best approximation from $\mathscr { A }$ to a function $f$ in $\mathcal { C } [ \alpha , b ]$ Let $p _ { k }$ and $p _ { k + 1 }$ be the approximations to $f$ that are calculated by any two consecutive iterations of the algorithm, and let $\xi$ be any point that is in the references of both iterations. Prove that the differences $[ f ( \pmb { \xi } ) - p _ { k } ( \pmb { \xi } ) ]$ and $[ f ( \pmb { \xi } ) - p _ { \pmb { k } + 1 } ( \pmb { \xi } ) ]$ have the same sign.

Find an extension to the one-point exchange algorithm for the following calculation. Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the Haar condition, let $\{ \zeta _ { i } ; i =$ $1 , 2 , \ldots , l \}$ be fixed points in $[ a , b ]$ where $1 \leqslant l \leqslant n$ ,and let $f$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ . Calculate the elenient of $\mathcal { A }$ that minimizes the error { $\| f - p \| _ { \infty } ; p \in \mathcal { A } \}$ subject to the interpolation conditions $\{ p ( \zeta _ { i } ) = f ( \zeta _ { i } ) ; i = 1 , 2 , . . . , l \}$ .One difficulty in the extension is finding a suitable rule for the change of reference.It is helpful to preserve the sign properties that are the subject of Exercise 8.8.

8.10 Investigate the following extension to the exchange algorithm for the case when $\mathcal { A }$ is an $( n + 1 )$ -dimensional subspace of ${ \mathcal { C } } [ a , b ]$ that need not satisfy the Haar condition. Let each reference contain $( n + 3 )$ points.Given the reference $\left\{ \xi _ { i } ; i = 0 , 1 , \ldots , \right.$ $n + 2 \}$ ,let $p _ { k }$ be the function in $\mathcal { A }$ that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 2 } \big | f ( \xi _ { i } ) - p ( \xi _ { i } ) \big | , \qquad p \in \mathcal { A } .
$$

Let $\xi _ { q }$ be the point such that ${ p } _ { k }$ also minimizes this expression when the range of $i$ excludes the value $i = q$ .The reference for the next iteration is obtained by replacing $\xi _ { q }$ by a number $\pmb { \eta }$ that satisfies the equation $\left| f ( \eta ) - p _ { k } ( \eta ) \right| = \| f - p _ { k } \| _ { \infty }$ . Because bounds of the form (8.5) are still valid, the procedure continues until the bounds show that sufficient accuracy is obtained.

# The convergence of the exchange algorithm

# 9.1 The increase in the levelled reference error

The method of proof of Theorem 8.2 depends so strongly on the fact that the number of different references is finite in the discrete case, that it is not useful for analysing the convergence properties of the one-point exchange algorithm that is described in Sections 8.1 and 8.2, where the purpose of the calculation is to obtain the element of $\mathscr { A }$ that minimizes the maximum value of the error function on the interval $a \leqslant x \leqslant b$ .We begin the analysis of the continuous case by finding an expression for the increase in the levelled reference error. This work gives an alternative proof of part of Theorem 7.7.

The levelled reference error is defined by the equations (8.4),but these equations also include the unknown coeficients of the approximation $p$ In order to remove this dependence, we let $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ be a basis of $\mathcal { A } ,$ ，and we eliminate the coefficients $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ from the equations

$$
f ( \xi _ { i } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( \xi _ { i } ) = ( - 1 ) ^ { i } h , \qquad i = 0 , 1 , \dots , n + 1 .
$$

Because there are $( n + 2 )$ points in a reference, there exist multipliers $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \} ,$ , not all zero, that satisfy the conditions

$$
\sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } \phi _ { j } ( \xi _ { i } ) = 0 , \qquad j = 0 , 1 , \ldots , n .
$$

Hence $h$ is defined by the equation

$$
\sum _ { i = 0 } ^ { n + 1 } ( - 1 ) ^ { i } \sigma _ { i } h = \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } f ( \xi _ { i } ) .
$$

We require the properties of the numbers $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ that are given in the next theorem.

# Theorem 9.1

Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the Haar condition, let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a set of points from $[ a , b ]$ that are in ascending order

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < \ldots < \xi _ { n + 1 } \leqslant b ,
$$

and let $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a set of real multipliers,that are not all zero,and that satisfy the equation

$$
\sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } p ( \xi _ { i } ) = 0 ,
$$

for all functions $p$ in $\mathcal { A }$ . Then every multiplier is non-zero,and their signs alternate.

Proof. Let $k$ be an integer in $[ 0 , n ]$ .Because of the fourth property of linear spaces that satisfy the Haar condition, given in Section 7.3,we may let $\pmb { p }$ be the element of $\mathscr { A }$ that is defined by the interpolation conditions

$$
p \left( \xi _ { i } \right) = 0 , \qquad i = 0 , 1 , \ldots , n + 1 , \qquad i \neq k , \qquad i \neq k + 1 ,
$$

and

$$
p ( \xi _ { k } ) = 1 .
$$

It follows from condition (1) of Section 7.3 that equation (9.6) gives all the zeros of the function $p$ Hence $p ( \xi _ { k + 1 } )$ is positive. Because the choice of $p$ and equation (9.5) imply the identity

$$
\sigma _ { k } + \sigma _ { k + 1 } p ( \xi _ { k + 1 } ) = 0 ,
$$

it follows that either $\pmb { \sigma } _ { \pmb { k } }$ and $\pmb { \sigma } _ { k + 1 }$ are both zero,or they are both non-zero and their signs are opposite. This statement holds for $k = 0 , 1 , \ldots , n$ Therefore the theorem is true.□

We deduce from the theorem and from equation (9.3) that the levelled reference error has the value

$$
\begin{array} { l } { { \displaystyle h \left( \xi _ { 0 } , \xi _ { 1 } , \dots , \xi _ { n + 1 } \right) = \Biggl \vert \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } f ( \xi _ { i } ) \Biggl \vert \Biggl / \sum _ { i = 0 } ^ { n + 1 } \left. \sigma _ { i } \right. } } \\ { { \displaystyle \qquad = \Biggl \vert \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } \lbrack f ( \xi _ { i } ) - p ( \xi _ { i } ) \rbrack \Biggl \vert \Biggl / \sum _ { i = 0 } ^ { n + 1 } \left. \sigma _ { i } \right. } , } \end{array}
$$

where the last line depends on equation (9.5). Suitable values of the multipliers $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ may be obtained from the co-factors of the matrix of the equations (9.2). We make the definition

$$
\begin{array} { l } { { \sigma _ { i } = ( - 1 ) ^ { i } \operatorname* { d e t } \left[ \Phi ( \xi _ { 0 } , \xi _ { 1 } , \dots , \xi _ { i - 1 } , \xi _ { i + 1 } , \dots , \xi _ { n + 1 } ) \right] , } } \\ { { \qquad i = 0 , 1 , \dots , n + 1 , } } \end{array}
$$

where $\Phi ( \zeta _ { 0 } , \zeta _ { 1 } , \ldots , \zeta _ { n } )$ is the square matrix whose elements are the numbers $\{ \phi _ { j } ( \zeta _ { i } ) ; i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ .The fourth property of Section 7.3 states that each $\pmb { \sigma _ { i } }$ is non-zero. Thus the first line of equation (9.9) expresses the levelled reference error in a way that is independent of $p$

In order to relate $h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \ldots , \xi _ { n + 1 } ^ { + } )$ to $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ , where we are using the notation of Section 8.1, we let $\{ \sigma _ { i } ^ { + } ; i = 0 , 1 , \ldots , n + 1 \}$ be the numbers that are obtained by replacing the old reference points by the new reference points in the definition (9.1O). Therefore equation (9.9) gives the value

$$
h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \ldots , \xi _ { n + 1 } ^ { + } ) = \overbrace { \vphantom { \int _ { 0 } ^ { 0 } } \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } ^ { + } \left[ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right] } ^ { \left| \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } ^ { + } \left[ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right] \right| } ,
$$

where $p$ is any element of $\mathcal { A }$ We let $p$ be the approximation that is defined by equation (8.4),and we recall that the new reference satisfies the sign conditions (8.12). It follows from Theorem 9.1 that the numerator of expression (9.11) has the value

$$
\sum _ { i = 0 } ^ { n + 1 } \big | \sigma _ { i } ^ { + } [ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) ] \big | .
$$

Now, in the one-point exchange algorithm, $\left| f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right|$ is equal to $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ ,unless $\xi _ { i } ^ { + }$ is the point $\pmb { \eta }$ that satisfies equation (8.7), in which case $\left| f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right|$ is equal to $\| f - p \|$ . We let $\xi _ { r } ^ { + }$ be the point of the new reference that is equal to $\pmb { \eta }$ .Hence the new levelled reference error is the expression

$$
\begin{array} { l } { { \displaystyle h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \dots , \xi _ { n + 1 } ^ { + } ) } \ ~ } \\ { { \displaystyle h ( \xi _ { 0 } , \xi _ { 1 } , \dots , \xi _ { n + 1 } ) \sum _ { i = 0 \atop i \neq r } ^ { n + 1 } \left| { \boldsymbol \sigma } _ { i } ^ { + } \right| + \left\| { \boldsymbol f } - { \boldsymbol p } \right\| \left| { \boldsymbol \sigma } _ { r } ^ { + } \right| } \ ~ } \\ { { \displaystyle ~ = \frac { h + r } { \sum _ { i = 0 } ^ { n + 1 } \left| { \boldsymbol \sigma } _ { i } ^ { + } \right| } } . } \end{array}
$$

This result provides the alternative proof of the statement that the levelled reference errors increase, if the calculation of the exchange algorithm continues because the right-hand side of expression (8.5) is greater than the left-hand side.

# 9.2 Proof of convergence

It is straightforward to deduce from equation (9.13) that the functions $p$ in $\mathcal { A } ,$ ， that are calculated by the iterations of the exchange algorithm, converge to the best minimax approximation from $\mathscr { A }$ to $f ,$ provided that each $\left| \sigma _ { r } ^ { + } \right|$ is bounded away from zero. This condition is satisfied, but in order to prove it we require the technical result that is given in the next theorem.

# Theorem 9.2

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the Haar condition,and,for any $f$ in $\mathcal { C } [ a , b ] .$ , let the one-point exchange algorithm be applied to calculate the best approximation from $\mathscr { A }$ to $f .$ Then，for any initial reference $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ ，there exists a positive number $\pmb { \delta }$ ,such that on each iteration the points of the reference satisfy the bounds

$$
\xi _ { i + 1 } - \xi _ { i } \geqslant \delta , \qquad i = 0 , 1 , \ldots , n .
$$

Proof. The method that is used to change the reference ensures that the points of each reference are distinct. Therefore it is sufficient to rule out the possibility that, for a subsequence of references, two points tend to become coincident. We suppose that this happens and deduce a contradiction. Because all references are in a closed and bounded subset of $\mathcal { R } ^ { n + 2 }$ ，the hypothesis implies that there is a subsequence of the subsequence that converges to a set $\{ \bar { \xi } _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ that contains at most $( n + 1 )$ distinct points.

Let $\left| h _ { k } \right|$ be the levelled reference error of the kth iteration. Although $\lvert h _ { 1 } \rvert \mathrm { m a y }$ be zero,it follows from inequality (8.11) that $\left| h _ { 2 } \right|$ is positive, and that the sequence $\{ | h _ { k } | ; k = 1 , 2 , 3 , . . . \}$ increases strictly monotonically. The contradiction that is obtained from the set $\{ \bar { \xi } _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ is that a large value of $k$ exists, such that $\left| h _ { k } \right|$ is less than $\left| h _ { 2 } \right|$

Because the Haar condition implies that there is a function in $\mathcal { A }$ that interpolates $f$ at any $( n + 1 )$ points of $[ a , b ] ,$ we may let $\bar { p }$ be a function in $\mathcal { A }$ that satisfies the equations

$$
\bar { p } ( \bar { \xi } _ { i } ) = f ( \bar { \xi } _ { i } ) , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

It is important to note that $\bar { p }$ does not depend on the iteration number. Because $f$ and $\bar { p }$ are both in $\mathcal { C } [ \alpha , b ] .$ ,there exists a positive number $\pmb \varepsilon$ such that the inequality

$$
\left| ( f - { \bar { p } } ) ( x _ { 2 } ) - ( f - { \bar { p } } ) ( x _ { 1 } ) \right| < \left| h _ { 2 } \right|
$$

holds, where $x _ { 1 }$ and $x _ { 2 }$ are any two points of $[ a , b ]$ that satisfy the bound

$$
\left| x _ { 1 } - x _ { 2 } \right| < \varepsilon .
$$

We let $\pmb { k }$ be the number of an iteration whose reference satisfies the conditions

$$
\left| \xi _ { i } - { \bar { \xi } } _ { i } \right| < \varepsilon , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

Therefore, we may let $x _ { 1 } = \xi _ { i }$ and $x _ { 2 } = \bar { \xi } _ { i }$ in expression (9.16), which, because of equation (9.15), gives the inequality

$$
| f ( \xi _ { i } ) - \bar { p } ( \xi _ { i } ) | < | h _ { 2 } | , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

It follows that the bound

$$
\operatorname* { m i n } _ { p \in \mathcal { A } } \operatorname* { m a x } _ { i = 0 , 1 , \ldots , n + 1 } \left| f ( \xi _ { i } ) - p ( \xi _ { i } ) \right| < \left| h _ { 2 } \right|
$$

is obtained. The required contradiction is a consequence of the fact that the left-hand side of this expression is the definition of $\left| h _ { k } \right|$ □

In order to prove that $\left| \sigma _ { r } ^ { + } \right|$ is bounded away from zero, we let $\pmb { \delta }$ be the number that is mentioned in the statement of Theorem 9.2,and we let $\mathcal { Z } = \left\{ { z } \right\}$ be the subset of vectors in $\mathcal { R } ^ { n + 1 }$ whose components, $\{ \zeta _ { i } ; i =$ $0 , 1 , \ldots , n \}$ say, satisfy the conditions

$$
a \leqslant \zeta _ { 0 } \leqslant \zeta _ { 1 } \leqslant . ~ . ~ \leqslant \zeta _ { n } \leqslant b ,
$$

and

$$
\zeta _ { i } \cdots \zeta _ { i - 1 } \geqslant \delta , \qquad i = 1 , 2 , \ldots , n .
$$

Because $\mathcal { Z }$ is compact,and because the functions in $\mathscr { A }$ are continuous, the expression

$$
\begin{array} { r l r } { \big \vert \mathbf { d e t } \Phi ( \zeta _ { 0 } , \zeta _ { 1 } , \ldots , \zeta _ { n } ) \big \vert , } & { { } } & { z \in \mathcal { Z } , } \end{array}
$$

achieves its minimum value, $^ { m }$ say, where $\Phi$ is defined immediately after equation (9.1O). It follows from the fourth property of Section 7.3 and from Theorem 9.2, that the inequality

$$
| \sigma _ { i } | \geqslant m > 0 , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

is satisfied on every iteration. Moreover, the definition (9.10) implies a constant upper bound of the form

$$
\left| \sigma _ { i } \right| \leqslant M , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

We are now ready to use equation (9.13) to deduce the convergence of the exchange algorithm.

# Theorem 9.3

Let the conditions of Theorem 9.2 be satisfied,and let $p _ { k }$ be the function in $\mathscr { A }$ that is calculated by the kth iteration of the exchange algorithm. Then the sequence $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$ converges to the best minimax approximation from $\pmb { \mathcal { A } }$ to $f , p ^ { * }$ say.

Proof. Expressons (9.13),(9.24) and (9.25) imply the relation

$$
\left| h _ { k + 1 } \right| \geqslant \frac { ( n + 1 ) M \vert h _ { k } \vert + m \| f - p _ { k } \| } { ( n + 1 ) M + m } .
$$

Subtracting $\left| h _ { k } \right|$ from each side gives the bound

$$
\left| h _ { k + 1 } \right| - \left| h _ { k } \right| \geqslant \frac { m } { ( n + 1 ) M + m } \left[ \left\| f - p _ { k } \right\| - \left| h _ { k } \right| \right] .
$$

The sequence $\{ | h _ { k } | ; k = 1 , 2 , 3 , . . . \}$ increases monotonically and is bounded above by the condition

$$
\left| h _ { k } \right| \leqslant \left\| f - p ^ { * } \right\| \leqslant \left\| f - p _ { k } \right\| .
$$

Therefore the left-hand side of expression (9.27) tends to zero.Because inequality (9.28) shows that $[ \| f - p _ { k } \| - | h _ { k } | ]$ is non-negative,it follows that the right-hand side of expression (9.27) also tends to zero. Thus, using inequality (9.28) once more,we find the limit

$$
\operatorname* { l i m } _ { k \to \infty } \| f - p _ { k } \| = \| f - p ^ { * } \| .
$$

Hence the functions $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$ are bounded,and therefore they remain in a compact subset of $\mathcal { A }$ ，Therefore the sequence $\{ p _ { k } ; k =$ $1 , 2 , 3 , \ldots 3$ has at least one limit point. Equation (9.29) shows that each limit point is a best approximation, while Theorem 7.6 states that the best approximation is unique. It follows,by using compactness again, that the sequence $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$ converges to $p ^ { * }$ .□

# 9.3 Properties of the point that is brought into the reference

There are many examples in numerical analysis of procedures that always converge, but whose rate of convergence is so slow that the procedure is hardly ever useful. The calculation of Section 8.3, however, shows that the exchange algorithm can perform very well. The work of the next two sections explains the excellent convergence properties of the one-point exchange algorithm，assuming some differentiability and regularity properties that are often achieved in practice.

We continue to let $p ^ { * }$ be the best approximation to $f$ in $\mathcal { C } [ a , b ]$ from an $( n + 1 )$ -dimensional linear space $\mathcal { A }$ that satisfies the Haar condition. We assume that the maximum value of the modulus of the error function

$$
e ^ { * } ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

occurs at only $( n + 2 )$ points of $[ a , b ]$ , namely $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \dots , n + 1 \}$ . We assume that all functions are twice continuously differentiable. If $\boldsymbol { \xi } _ { 0 } ^ { * }$ is at $^ { a }$ ,we require the first derivative $e ^ { * \prime } ( a )$ to be non-zero, and, if $\xi _ { n + 1 } ^ { * }$ is at $^ { b }$ ，

we require $e ^ { * \prime } ( b )$ to be non-zero. For all other points in the set $\{ \xi _ { i } ^ { * } ; i =$ $0 , 1 , \ldots , n + 1 \nmid$ ， we require the second derivative $e ^ { * \prime \prime } ( \xi _ { i } ^ { * } )$ to be nonzero.

We let $\{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \} , \left| h _ { k } \right|$ and $p _ { k }$ be the reference points, the levelled reference error and the calculated approximation of the kth iteration of the exchange algorithm. Therefore the equations

$$
| f ( \xi _ { i k } ) - p _ { k } ( \xi _ { i k } ) | = | h _ { k } | , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

are satisfied. Theorem 9.3 shows that,as $k$ tends to infinity, $p _ { k }$ and $\left| h _ { k } \right|$ tend to $p ^ { * }$ and $\| f - p ^ { * } \|$ respectively,and Theorem 9.2 states that the points of each reference stay apart.It follows from the first assumption of the previous paragraph and from equation (9.31) that the sequence of references $[ \{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \}$ ； $k = 1 , 2 , 3 , \ldots ]$ converges to the set $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \ldots , n + 1 \}$ . The following theorem gives some properties of the way in which each reference is changed. These properties are used in Section 9.4 to bound the rate of convergence of the sequence of approximations $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$

# Theorem 9.4

Given the assumptions and using the notation that are stated in the previous two paragraphs, there exists an integer $\pmb { K }$ and a constant $c$ such that the following conditions are obtained for all $k \geqslant K .$ Let $\xi _ { q k + 1 } =$ $\eta$ be the point that is brought into the reference by the kth iteration of the exchange algorithm. If $\xi _ { q } ^ { * }$ is one of the end points of the interval $[ a , b ] .$ ， then $\xi _ { q k + 1 }$ is equal to ${ \xi } _ { q } ^ { * }$ . Otherwise the bound

$$
\left| \xi _ { q } ^ { * } - \xi _ { q k + 1 } \right| \leqslant c \left\| p ^ { * } - p _ { k } \right\|
$$

is satisfied.

Proof. Because the sequence of references converges to $\{ \xi _ { i } ^ { * } ; i =$ $0 , 1 , \ldots , n + 1 \}$ , we may choose $\pmb { K }$ so that, for all $k \geqslant K ,$ ，the point that leaves the reference of the kth iteration to make room for $\xi _ { q k + 1 } = \eta$ is the point $\xi _ { q k }$ .Further,if $e ^ { * \prime } ( a )$ is non-zero, we may also require $\pmb { K }$ to satisfy the condition that,for all $k \geqslant K ,$ ,there are no stationary points of the error function $\{ e _ { k } ( x ) = f ( x ) - p _ { k } ( x )$ $a \leqslant x \leqslant b \}$ in a small fixed neighbourhood of $^ a$ Hence, if $\xi _ { q } ^ { * } = a$ ,then the point $\xi _ { q k + 1 }$ is equal to ${ \xi } _ { q } ^ { * }$ for sufficiently large $k$ ，A similar result holds if $\xi _ { q } ^ { * } = b$ In all other cases $\xi _ { q k + 1 }$ is the abscissa of an extreme point of the error function $e _ { k }$ , that is close to ${ \xi } _ { q } ^ { * }$ when $k$ is large.It remains to prove that in this case condition (9.32) is obtained.

The conditions of the theorem imply that there exist positive constants $\pmb \varepsilon$ and $^ d$ such that, if $\pmb { \xi } _ { q } ^ { * }$ is one of the points $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \ldots , n + 1 \}$ at which $e ^ { * }$ is stationary, then the inequality

$$
\begin{array} { r } { | e ^ { * \prime \prime } ( x ) | \geqslant d , \qquad \xi _ { q } ^ { * } - \varepsilon \leqslant x \leqslant \xi _ { q } ^ { * } + \varepsilon , } \end{array}
$$

holds. We increase $\kappa$ if necessary so that, for $k \geq K$ ， the point $\xi _ { q k + 1 }$ is always in the interval $[ \xi _ { q } ^ { * } - \varepsilon , \xi _ { q } ^ { * } + \varepsilon ]$ . Therefore, because $e ^ { * \prime } ( \xi _ { q } ^ { * } )$ is zero, expression (9.33) gives the bound

$$
\left| e ^ { * \prime } ( \xi _ { q k + 1 } ) \right| \geqslant d | \xi _ { q } ^ { * } - \xi _ { q k + 1 } | .
$$

The definitions of $\xi _ { q k + 1 } , e ^ { * }$ and $e _ { k }$ imply that the left-hand side of this inequality has the value

$$
\left| e ^ { \ast \prime } ( \xi _ { q k + 1 } ) - e _ { k } ^ { \prime } ( \xi _ { q k + 1 } ) \right| = \big | p ^ { \ast \prime } ( \xi _ { q k + 1 } ) - p _ { k } ^ { \prime } ( \xi _ { q k + 1 } ) \big | .
$$

Hence the condition

$$
\big | \xi _ { q } ^ { * } - \xi _ { q k + 1 } \big | \leqslant ( 1 / d ) \big | \big | p ^ { * \prime } - p _ { k } ^ { \prime } \big | \big |
$$

is satisfied. Because $\pmb { \mathcal { A } }$ is a finite-dimensional linear space, there exists a constant $\pmb { D }$ such that the inequality

$$
\| p ^ { \prime } \| { \leqslant } D \| p \| , \qquad p \in { \mathcal { A } } ,
$$

holds. It follows from condition (9.36) that the theorem is true, where $^ { c }$ is the number $\scriptstyle { D / d }$ □

In order to apply the theorem,it is necessary to relate the difference $( p ^ { * } - p _ { k } )$ to the positions of the reference points $\{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \}$ The following result is suitable.

# Theorem 9.5

There exists a constant $\bar { c }$ such that the inequality

$$
\left\| p ^ { * } - p _ { k } \right\| \leqslant \bar { c } \operatorname* { m a x } _ { i = 0 , 1 , \ldots , n + 1 } \left| e ^ { * } ( \xi _ { i } ^ { * } ) - e ^ { * } ( \xi _ { i k } ) \right|
$$

is satisfied, where the notation is defined earlier in this section.

Proof. We let $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ be a basis of $\scriptstyle { \mathcal { A } }$ we express $p ^ { * }$ and ${ p } _ { k }$ in the form

$$
\begin{array} { l l } { { p ^ { * } ( x ) = \displaystyle \sum _ { j = 0 } ^ { n } \lambda _ { j } ^ { * } \phi _ { j } ( x ) , } } & { { \quad a \leqslant x \leqslant b } } \\ { { } } & { { } } \\ { { p _ { k } ( x ) = \displaystyle \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( x ) , } } & { { \quad a \leqslant x \leqslant b } } \end{array} \biggr \} ,
$$

and we recall that the numbers $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ and $h _ { k }$ are defined by the equations

$$
f ( \xi _ { i k } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( \xi _ { i k } ) = ( - 1 ) ^ { i } h _ { k } , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

The matrix of this system is bounded away from singularity for allvalues of $k$ , because,due to the definition (9.10),the modulus of the determinant of the matrix has the value

$$
\left| \sum _ { i = 0 } ^ { n + 1 } { ( - 1 ) ^ { i } \sigma _ { i } } \right| = \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| \geqslant ( n + 2 ) m ,
$$

where the last two steps depend on Theorem 9.1 and inequality (9.24). Therefore,if we define the numbers $\{ \alpha _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ by the equations

$$
\alpha _ { i } - \sum _ { j = 0 } ^ { n } { \bf \Phi } ( \lambda _ { j } - \lambda _ { j } ^ { * } ) \phi _ { j } ( \xi _ { i k } ) = { \bf \Phi } ( - 1 ) ^ { i } ( h _ { k } - h ^ { * } ) , \qquad i = 0 , 1 , \dots , n + 1 ,
$$

where $h ^ { * }$ is the minimax error of the approximation $p ^ { * }$ that satisfies the conditions

$$
f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) = ( - 1 ) ^ { i } h ^ { * } , \qquad i = 0 , 1 , \dots , n + 1 ,
$$

and if we take the point of view that the system (9.42) is used to express the differences $\{ \lambda _ { j } - \lambda _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ and $( h _ { k } - h ^ { * } )$ in terms of the numbers $\{ \alpha _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ , it follows that the bound

$$
\operatorname* { m a x } _ { j = 0 , 1 , \dots , n } \left| \lambda _ { j } - \lambda _ { j } ^ { * } \right| \leqslant \bar { d } \operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } \left| \alpha _ { i } \right|
$$

is satisfied for some constant $\bar { d } .$ Equation (9.39), (9.40),(9.42) and (9.43) imply that $\pmb { \alpha } _ { i }$ has the vaiue

$$
\begin{array} { l } { { \alpha _ { i } = f ( \xi _ { i k } ) - p ^ { * } ( \xi _ { i k } ) - ( - 1 ) ^ { i } h ^ { * } } } \\ { { \mathrm { } = e ^ { * } ( \xi _ { i k } ) - e ^ { * } ( \xi _ { i } ^ { * } ) , \qquad i = 0 , 1 , \dots , n + 1 , } } \end{array}
$$

and expression (9.39) gives the bound

$$
\| p ^ { * } - p _ { k } \| _ { \infty } \leqslant \sum _ { j = 0 } ^ { n } \left| \lambda _ { j } - \lambda _ { j } ^ { * } \right| \| \phi _ { j } \| _ { \infty } .
$$

Therefore,inequality (9.38) is a consequence of condition (9.44), where $\bar { c }$ has the value

$$
\bar { c } = \bar { d } \sum _ { j = 0 } ^ { n } \| \phi _ { j } \| _ { \infty } .
$$

The theorem is proved.

# 9.4 Second-order convergence

In order to prove that the one-point exchange algorithm has a second-order rate of convergence,we note that Theorem 9.4 and the form of $e ^ { * }$ imply that, for $k \geqslant K ,$ ，the difference $\left| e ^ { * } ( \xi _ { q } ^ { * } ) - e ^ { * } ( \xi _ { q k + 1 } ) \right|$ is bounded above by a multiple of $\| p ^ { * } - p _ { k } \| ^ { 2 }$ . Thus,for sufficiently large $k$ ， each iteration reduces one of the terms that occurs on the right-hand side of inequality (9.38). Because each iteration changes only one reference point,as many as $( n + 2 )$ iterations may be necessary to make a substantial improvement to the calculated approximations. Even then a better approximation need not be obtained, because of the remote possibility that at the beginning of the sequence of iterations the calculated approximation is equal to $p ^ { * }$ , but this situation is not recognized because the reference is wrong. Therefore it is not possible to prove that the sequence $\{ \| p ^ { * } - p _ { k } \|$ ； $k = 1 , 2 , 3 , \ldots \}$ converges to zero in a regular way. Instead, the following theorem gives a useful property of the changes that are made to the references.

# Theorem 9.6

Let the conditions of Theorem 9.4 be satisfed. There exists an integer $\kappa$ and a constant $\beta$ such that the sequence $\left\{ \rho _ { k } ; k = K , K + 1 , \ldots \right\}$ converges monotonically to zero, and such that the inequality

$$
\rho _ { k + n + 2 } \leqslant \beta \rho _ { k } ^ { 2 } , \qquad k \geqslant K ,
$$

is satisfied, where $\rho _ { k }$ is the expression

$$
\rho _ { k } = \operatorname* { m a x } _ { i = 0 , 1 , \ldots , n + 1 } \big | e ^ { * } ( \xi _ { i } ^ { * } ) - e ^ { * } ( \xi _ { i k } ) \big | .
$$

Proof. The discussion that is given immediately before Theorem 9.4 shows that the sequence $\{ \rho _ { k } ; k = K , K + 1 , \ldots \}$ converges to zero. In order to prove that the sequence is monotonic, we let $K , c$ and $\bar { c }$ have the values that are given in Theorems 9.4 and 9.5,and we increase $\pmb { K }$ if necessary so that the bound

$$
( c \bar { c } ) ^ { 2 } \rho _ { k } \| e ^ { * \prime \prime } \| _ { \infty } \leqslant 2 , \qquad k \geqslant K ,
$$

is obtained. The definition (9.49) implies the relation

$$
\rho _ { k + 1 } \leqslant \operatorname* { m a x } { [ \rho _ { k } , | e ^ { * } ( \xi _ { q } ^ { * } ) - e ^ { * } ( \xi _ { q k + 1 } ) | ] } ,
$$

where $\xi _ { q k + 1 }$ is still the point that is brought into the reference by the kth iteration of the exchange algorithm.Therefore, if ${ \xi } _ { q } ^ { * }$ is an end point of the interval $[ a , b ]$ ，the condition $\rho _ { k + 1 } \leqslant \rho _ { k }$ is an immediate consequence of Theorem 9.4. Otherwise,we use the Taylor series expansion of the function $\{ e ^ { * } ( x ) ; a \leqslant x \leqslant b \}$ about the point $x = \xi _ { q } ^ { * }$ to deduce the inequality

$$
\begin{array} { r l } & { \| e ^ { * } ( \xi _ { q } ^ { * } ) - e ^ { * } ( \xi _ { q k + 1 } ) \| \leqslant \frac { 1 } { 2 } ( \xi _ { q } ^ { * } - \xi _ { q k + 1 } ) ^ { 2 } \| e ^ { * \prime \prime } \| _ { \infty } } \\ & { \qquad \leqslant \frac { 1 } { 2 } c ^ { 2 } \| p ^ { * } - p _ { k } \| ^ { 2 } \| e ^ { * \prime \prime } \| _ { \infty } } \\ & { \qquad \leqslant \frac { 1 } { 2 } ( c \bar { c } ) ^ { 2 } \rho _ { k } ^ { 2 } \| e ^ { * \prime \prime } \| _ { \infty } } \\ & { \qquad \leqslant \rho _ { k } , } \end{array}
$$

Therefore the sequence $\{ \rho _ { k } ; k = K , K + 1 , \ldots \}$ does decrease monotonically.

In order to establish inequality (9.48), we let $k$ be an integer that is not less than $\kappa$ ，and we let $q ( j )$ be the index of the point that leaves the reference $\{ \xi _ { i j } ; i = 0 , 1 , \ldots , n + 1 \}$ on the $j _ { \mathbf { \ L } } ( \mathbf { h }$ iteration. Because the set $\{ q ( j ) ; j = k , k + 1 , \ldots , k + n + 2 \}$ contains $( n + 3 )$ terms,and because at most $( n + 2 )$ of these terms are different, we let $\boldsymbol { r }$ and $\pmb { s }$ be integers that satisfy the conditions $k \leqslant r < s \leqslant k + n + 2$ and $q ( r ) = q ( s ) = t ,$ ,say,and we reduce $\pmb { s }$ if necessary so that the integer $t$ does not occur in the set $\{ q ( j ) ; j = r + 1 , r + 2 , \ldots , s - 1 \}$ .The point $\xi _ { t } ^ { * }$ is not equal to $^ { a }$ or $^ { b }$ ， because,if it were, then Theorem 9.4 would imply that the sth iteration would fail to change the reference.

We consider the difference $( \xi _ { t s + 1 } - \xi _ { t s } )$ ，which is the change to a reference point on the sth iteration. Because $\xi _ { t s }$ is equal to $\xi _ { t r + 1 }$ ,expressions (9.32), (9.38) and (9.49) give the bound

$$
\begin{array} { r l } & { \left| { \xi _ { t s + 1 } - \xi _ { t s } } \right| \leqslant c [ \| p ^ { * } - p _ { s } \| + \| p ^ { * } - p _ { r } \| ] } \\ & { \qquad \leqslant c \bar { c } ( \rho _ { s } + \rho _ { r } ) } \\ & { \qquad \leqslant 2 c \bar { c } \rho _ { k } . } \end{array}
$$

We make use of the fact that $\xi _ { t s + 1 }$ is the abscissa of an extremum of the error function $\{ e _ { s } ( x ) = f ( x ) - p _ { s } ( x )$ ； $a \leqslant x \leqslant b \}$ to deduce the inequality

$$
\begin{array} { r } { \big | e _ { s } ( \xi _ { t s + 1 } ) - e _ { s } ( \xi _ { t s } ) \big | \leqslant \frac { 1 } { 2 } \bar { \beta } \big | \xi _ { t s + 1 } - \xi _ { t s } \big | ^ { 2 } , } \end{array}
$$

where $\bar { \beta }$ is a constant upper bound on the norms $\{ \| e _ { j } ^ { \prime \prime } \| _ { \infty } ; j \geqslant K \}$ . Because of the sign conditions that are satisfied when the exchange algorithm adjusts a reference, the equation

$$
| e _ { s } ( \xi _ { t s + 1 } ) - e _ { s } ( \xi _ { t s } ) | . = \| e _ { s } \| _ { \infty } - | h _ { s } |
$$

holds, and we recall that $\| e _ { s } \| _ { \infty }$ is an upper bound on the least maximum error $\| e ^ { * } \| _ { \infty }$ . Therefore, expressions (9.53), (9.54) and (9.55) imply the relation

$$
\big \| e ^ { * } \big \| _ { \infty } - \big | h _ { s } \big | \leqslant 2 \bar { \beta } ( c \bar { c } \rho _ { k } ) ^ { 2 } .
$$

The final part of the proof depends on the value of $\left| h _ { s } \right|$ that can be obtained from equation (9.9), when $\pmb { p }$ is the polynomial $p ^ { * }$ . By increasing $\pmb { K }$ if necessary, so that for all $\pmb { s } \geqslant \pmb { K }$ and for $i = 0 , 1 , \ldots , n + 1$ ,the signs of $e ^ { * } ( \xi _ { i s } )$ and $e ^ { * } ( \xi _ { i } ^ { * } )$ are the same, we find the value

$$
\begin{array} { l } { { \displaystyle \left| h _ { s } \right| = \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| \left| e ^ { * } ( \xi _ { i s } ) \right| \bigg / \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| } } \\ { { \displaystyle ~ = \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| [ \left| e ^ { * } ( \xi _ { i } ^ { * } ) \right| - \left| e ^ { * } ( \xi _ { i } ^ { * } ) - e ^ { * } ( \xi _ { i s } ) \right| ] \bigg / \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| } } \\ { { \displaystyle ~ \leqslant \left\| e ^ { * } \right\| _ { \infty } - \rho _ { s } m / [ ( n + 1 ) M + m ] } , } \end{array}
$$

where the second line depends on the properties of $e ^ { * }$ ,and where the last line depends on the definition (9.49) and on the bounds (9.24) and(9.25). Because expressons (9.56) and (9.57) imply the inequality

$$
\rho _ { s } \leqslant 2 [ ( n + 1 ) M + m ] \bar { \beta } ( c \bar { c } \rho _ { k } ) ^ { 2 } / m ,
$$

and because the sequence $\{ \rho _ { k } ; k = K , K + 1 , \ldots \}$ decreases monotonically, the theorem is proved.□

Theorems 9.5 and 9.6 show that the differences $\{ \| p ^ { * } - p _ { k } \|$ ； $k = K ,$ $\kappa +$ $1 , \ldots . \}$ are less than the corresponding terms of the sequence $\{ \bar { c } \rho _ { k } ; k =$ $K , K + 1 , \ldots \} ,$ . which converges to zero monotonically at an $( n + 2 )$ -step quadratic rate. This is about the strongest result that can be expected from an algorithm that changes only one reference point on each iteration, and it explains the rate of convergence that is achieved.

# 9 Exercises

9.1 Let the exchange algorithm be used to calculate the best approximation to the function $\{ f ( x ) = x ^ { 2 }$ ； $0 \leqslant x \leqslant 1 \}$ by a multiple of the function $\{ p ( x ) = x ; 0 \leqslant x \leqslant 1 \}$ . Let $\xi _ { 0 1 }$ be any interior point of the interval [0,1] and let $\xi _ { 1 1 } = 1$ ,where $\left\{ \xi _ { 0 k } , \xi _ { 1 k } \right\}$ is the reference of the kth iteration. Prove that $\xi _ { 1 k } = 1$ for all values of $k$ ,and that the sequence $\{ \xi _ { 0 k } ; k = 1 , 2 , 3 , . . . \}$ converges to the limit $\xi _ { 0 } ^ { * } =$ $\sqrt { 2 } - 1$ at a quadratic rate, which means that there is a constant $^ { c }$ such that the condition

$$
\begin{array} { r } { \big | \xi _ { 0 k + 1 } - \xi ^ { * } \big | \leqslant c \big | \xi _ { 0 k } - \xi ^ { * } \big | ^ { 2 } , \qquad k = 1 , 2 , 3 , \ldots , } \end{array}
$$

is satisfied.

9.2 Let $f$ be a function in $\mathcal { C } ^ { ( n + 1 ) } [ a , b ] ,$ let $\mathscr { A }$ be the space ${ \mathcal { P } } _ { n }$ , and let $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ be the levelled reference error that is defined in Section 8.1. Deduce from Theorem 4.2 that there exists a constant $^ c$ such that the bound

$$
h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } ) \leqslant c \operatorname* { m i n } _ { i = 0 , 1 , \ldots , n } \big | \xi _ { i + 1 } - \xi _ { i } \big | \big \| f ^ { ( n + 1 ) } \big \| _ { \infty }
$$

is obtained, which provides an easy proof of Theorem 9.2 in this special case.

9.3 Deduce from the proof of Theorem 9.3 that there exists a constant $\pmb \theta$ in the open interval (O,1) such that the inequality

$$
[ \left\| { f - p ^ { * } } \right\| - | h _ { k + 1 } | ] \leqslant \theta [ \left\| { f - p ^ { * } } \right\| - | h _ { k } | ]
$$

holds on every iteration of the one-point exchange algorithm.

9.4 Let $\mathscr { A }$ be a finite-dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, and let $f$ be any function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$

Prove that there exists a positive number $^ { c }$ such that the inequality

$$
\| f - p \| _ { \infty } - \| f - p ^ { * } \| _ { \infty } \geqslant c \| p - p ^ { * } \| _ { \infty }
$$

is satisfied for all $\pmb { p }$ in $\mathcal { A }$ ,where $p ^ { * }$ is the best approximation from $\mathcal { A }$ to $f .$

Section 8.2 mentions several procedures for changing the reference of the exchange algorithm on each iteration.Let the version be used that adjusts every reference point to a local extremum of the error function $\{ f ( x ) - p ( x ) ; a \leqslant x \leqslant b \}$ , subject to the conditions (8.12) and (8.13),and where one of the points of the new reference is a solution $\pmb { \eta }$ of equation (8.7). Prove that, if the conditions of Theorem 9.4 are satisfied, then this version of the exchange algorithm gives the quadratic rate of convergence

$$
\| p ^ { * } - p _ { k + 1 } \| \leqslant \mu \| p ^ { * } - p _ { k } \| ^ { 2 } , \qquad k = 1 , 2 , 3 , \ldots ,
$$

where $\pmb { \mu }$ is a constant.

9.6 Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ,and let $f$ be a function in ${ \mathcal { C } } [ a , b ]$ . Let $[ \{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \}$ ； $k =$ $1 , 2 , 3 , \ldots ]$ be an infinite sequence of references such that the numbers

$$
\big | h _ { k } \big | = \operatorname* { m i n } _ { p \in \mathcal { A } } \operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } \big | f ( \xi _ { i k } ) - p ( \xi _ { i k } ) \big | , \qquad k = 1 , 2 , 3 , \dots ,
$$

increase strictly monotonically. By considering the case when $\mathscr { A }$ is the two-dimensional space that is spanned by the functions $\{ \phi _ { 0 } ( x ) = x ; 0 \leqslant x \leqslant 2 \}$ and $\displaystyle \{ \phi _ { 1 } ( x ) = \mathbf { e } ^ { x }$ ； $0 \leqslant x \leqslant 2 \}$ ，and when $f$ is the function $\{ f ( x ) = x ^ { 2 }$ ； $0 \leqslant x \leqslant 2 \}$ ，show that, if $\mathcal { A }$ does not satisfy the Haar condition, then the differences $[ \{ \xi _ { i + 1 k } - \xi _ { i k } ; i =$ $0 , 1 , \ldots , n \}$ ； $k = 1 , 2 , 3 , \ldots ]$ may not be bounded away from zero.

9.7

In order to avoid consideration of the whole of the error function $\{ f ( x ) - p ( x ) ; a \leqslant x \leqslant b \}$ ，there is a version of the one-point exchange algorithm in which the point that leaves the reference is specified at the beginning of each iteration.Let this point be $\xi _ { q }$ The new reference point is found usually by searching from $\xi _ { q }$ in the direction that causes the error $\left| f ( x ) - p ( x ) \right|$ to increase,until an extreme value of the error function is found. Let the conditions of Theorem 9.2 be satisfied, except that this version of the exchange algorithm is used. Let $\mathscr { A }$ and $f$ be such that each error function has exactly $\pmb { n }$ extrema in the open interval $( a , b )$ . Let $\xi _ { 0 } = a$ and $\xi _ { n + 1 } = b$ throughout the calculation,and let the sequence of values of $\pmb q$ be a cyclic sequence of the integers $\left\{ 1 , 2 , \ldots , n \right\}$ .Hence each new reference point is used for exactly $_ n$ iterations. Prove that the calculated approximations converge to the best minimax approximation from $\mathscr { A }$ to $f .$

8 Let the conditions of Theorem 9.4 be satisfied.If an optimization algorithm is applied to maximize the levelled reference error $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ ，thenthesecondderivativesof $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ with respect to the reference points are important, excluding any reference points that become fixed at $^ { a }$ or $^ { b }$ By letting $\boldsymbol { p } = \boldsymbol { p } ^ { * }$ in equation (9.9), in order to express $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ in terms of the differences $\{ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ; i =$ $0 , 1 , \ldots , n + 1 \}$ ， prove that the important off-diagonal terms of the second derivative matrix all tend to zero.

).9 In practice it is inefficient to try to calculate extrema of functions exactly. Therefore investigate some useful ways of relaxing the condition (8.7) on the point that is brought into the reference by each iteration of the one-point exchange algorithm. It is advantageous if the proposed methods preserve the convergence theorems of this chapter.

9.10 Let the conditions of Theorem 9.4 be satisfied, except that in a neighbourhood of one interior reference point, $\pmb { \xi } _ { l } ^ { \ast }$ say, the error function of the best approximation satisfies the equation $\begin{array} { r } { \big | e ^ { * } ( x ) \big | = \big | e ^ { * } ( \xi _ { l } ^ { * } ) \big | - \big | x - \xi _ { l } ^ { * } \big | ^ { \alpha } , } \end{array}$ where $_ { \pmb { \alpha } }$ is a constant in the range (O,2),and where the singularity is due entirely to the function $f .$ Investigate the effect of the singularity on the rate of convergence of the one-point exchange algorithm.

# Rational approximation by the exchange algorithm

# 10.1 Best minimax rational approximation

It is noted in Chapter 3 that polynomials are not suitable for approximating a function of the form shown in Figure 1.1, because no polynomial that is slowly varying when $| x |$ is large can include naturally a sharp peak near the centre of the range of the variable.However,it is easy to obtain this kind of behaviour by letting the approximating function have the form

$$
r ( x ) = p _ { m } ( x ) / q _ { n } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $p _ { m } ( x )$ and $q _ { n } ( x )$ are polynomials of degrees $_ { m }$ and $_ n$ respectively. If in the case of Figure 1.1 it is known that the slope of the function to be approximated tends to a constant non-zero value when $x$ becomes large, then it is appropriate to let $m = n + 1$

We use the notation $\{ a _ { i } ; i = 0 , 1 , \dots , m \}$ and $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ for the coefficients of $p _ { m } ( x )$ and $q _ { n } ( x )$ . Thus the function (10.1） is the expression

$$
r ( x ) = \frac { a _ { 0 } + a _ { 1 } x + \ldots + a _ { m } x ^ { m } } { b _ { 0 } + b _ { 1 } x + \ldots + b _ { n } x ^ { n } } , \qquad a \leqslant x \leqslant b .
$$

Because $r ( x )$ remains unchanged if $p ( x )$ and $q ( x )$ are replaced by $c p ( x )$ and $c q ( x )$ ，where $c$ is any non-zero constant, the parameters of $r$ provide $( m + n + 1 )$ degrees of freedom. It is therefore appropriate to compare the approximation (1o.2） with a polynomial approximation from $\mathscr { P } _ { m + n }$ For example, if $f$ is the exponential function $\{ e ^ { x } ; - 1 \leqslant x \leqslant 1 \}$ ， then the least maximum error of an approximation from ${ \mathcal { P } } _ { 4 }$ is 0.000 547, but the least maximum error of a rational approximation when $m = n = 2$ is only O.Ooo O87. This gain in accuracy is remarkable,because the exponential function is not particularly well suited to approximation by a rational function. In many other cases much greater improvements are achieved.

We let $\mathcal { A } _ { m n }$ be the set of rational functions of the form (10.2). Because it is not a linear space, the calculation of rational approximations is harder than the calculation of polynomial approximations. There is, however, a useful extension of the exchange algorithm that does not require much extra work.As in the polynomial case, a sequence of approximations is found, that is expected to converge to the rational function that minimizes the greatest value of the error function. References are still used, each reference being a set of points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , m + n + 1 \}$ that satisfies the conditions

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < . . . < \xi _ { m + n + 1 } \leqslant b .
$$

For each trial reference the approximating function, $r _ { k }$ say, that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \ldots , m + n + 1 } | f ( \xi _ { i } ) - r ( \xi _ { i } ) | , \qquad r \in \bar { \mathcal { A } } _ { m n } ,
$$

is calculated, where $k$ is the iteration number,and where $\bar { \mathcal { A } } _ { m n }$ is the subset of $\mathcal { A } _ { m n }$ whose elements satisfy the condition that they are bounded in $[ a , b ]$ . In the one-point exchange algorithm,one point of the reference is replaced by a solution $\pmb { \eta }$ of the equation

$$
\left| f ( \pmb { \eta } ) - r _ { k } ( \pmb { \eta } ) \right| = \| f - r _ { k } \| ,
$$

where the point that leaves the reference is selected in the way that is described in Chapter 8. Then another iteration is begun.

The following theorem gives the equations that are used for the calculation of $r _ { k }$

# Theorem 10.1

Let $\bar { \mathcal { A } } _ { m n }$ be the set of rational functions of the form (10.2), whose denominators have no zeros in $[ a , b ] ,$ let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , m + n + 1 \}$ be a reference that satisfies the conditions (1O.3),and let $f$ be in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .If $r _ { k }$ is in $\mathcal { \bar { A } } _ { m n }$ ,and if the equations

$$
r _ { k } ( \xi _ { i } ) + ( - 1 ) ^ { i } h _ { k } = f ( \xi _ { i } ) , \qquad i = 0 , 1 , \ldots , m + n + 1 ,
$$

hold for some constant $h _ { k } ,$ then $r _ { k }$ is the element of $\mathcal { \bar { A } } _ { m n }$ that minimizes expression (10.4).

Proof. Because expression (10.4) has the value $\left| h _ { k } \right|$ when $r$ is equal to $r _ { k }$ ， it is sufficient to show that, if $\bar { r }$ is a function in $\mathcal { \bar { A } } _ { m n }$ that satisfies the condition

$$
\operatorname* { m a x } _ { i = 0 , 1 , \ldots , m + n + 1 } | f ( \xi _ { i } ) - \bar { r } ( \xi _ { i } ) | \leqslant | h _ { k } | ,
$$

then $\tilde { r }$ is equal to $r _ { k }$ .Expressions (10.6) and (10.7) imply that each of the terms $\{ [ f ( \xi _ { i } ) - r _ { k } ( \xi _ { i } ) ] - [ f ( \xi _ { i } ) - \bar { r } ( \xi _ { i } ) ] ; ~ i = 0 , ~ 1 , \ldots , m + n + 1 \}$ is either zero or has the sign of $( - 1 ) ^ { i } h _ { k }$ . It follows from Theorem 7.5 that the function $\left( \hat { r } - r _ { k } \right)$ has at least $( m + n + 1 )$ zeros in $[ a , b ]$ .However, we may express this function as the ratio of two polynomials,where the degree of the numerator is at most $( m + n )$ . Therefore $\bar { r }$ is equal to $r _ { k }$ □

If the conditions of Theorem 10.1 hold,and if $r ^ { * }$ is a best approximation from $\bar { \mathcal { A } } _ { m n }$ to $f ,$ then it follows from Theorem 10.1 and from the definition of a best approximation that the bounds

$$
\left| h _ { k } \right| \leqslant \left\| f - r ^ { * } \right\| \leqslant \left\| f - r _ { k } \right\|
$$

are satisfied. Thus,again the exchange algorithm provides upper and lower bounds on the least maximum error. Expression (10.8) shows also that $r _ { k }$ is the required approximation if $\left\| f - r _ { k } \right\|$ is equal to $\left| h _ { k } \right|$ ，which provides a sufficient condition for a best approximation that is analogous to the Characterization Theorem 7.2.

Because only one chapter of this book is given to the study of rational approximations, we leave many interesting questions open. For example, we do not even prove that for each $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ there is a best approximation from $\bar { \mathcal { A } } _ { m n }$ . In fact a best approximation always exists,and it is unique except for common factors that may occur in its numerator and denominator. These factors may depend on $x$ For example, if $f$ is the constant function whose value is one, then expression (1O.1） is a best rational approximation from $\boldsymbol { \bar { \mathcal { A } } } _ { m n } ,$ ，provided that the polynomials $p _ { m }$ and $q _ { n }$ are the same and have no roots in $[ a , b ]$

Section 10.2 considers the calculation of $r _ { k }$ and $h _ { k }$ by solving the equations (10.6). In Section 10.3 the convergence of the exchange algorithm is studied,and we find that the algorithm may fail. Therefore a more reliable method for calculating best rational approximations is mentioned briefly at the end of the chapter.

# 10.2 The best approximation on a reference

We let the coefficients of the required approximation $r _ { k }$ be $\{ a _ { j } ; j = 0 , 1 , \ldots , m \}$ and $\{ b _ { j } ; j = 0 , 1 , \ldots , n \}$ as in expression (10.2). We ensure that $r _ { k }$ is in $\bar { \mathcal { A } } _ { m n }$ by satisfying the condition

$$
b _ { 0 } + b _ { 1 } x + \ldots + b _ { n } x ^ { n } > 0 , \qquad a \leqslant x \leqslant b .
$$

Therefore the system (10.6) is equivalent to the equations

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 0 } ^ { m } a _ { j } \xi _ { i } ^ { j } = \left[ f ( \xi _ { i } ) - ( - 1 ) ^ { i } h _ { k } \right] \sum _ { j = 0 } ^ { n } b _ { j } \xi _ { i } ^ { j } , } } \\ { { \ i = 0 , 1 , \dots , m + n + 1 . } } \end{array}
$$

They are not linear because not only the coefficients of $r _ { k }$ but also the value of $h _ { k }$ are to be determined.

The usual way of solving these equations begins by eliminating the coefficients $\{ a _ { j } ; j = 0 , 1 , \ldots , m \}$ by making use of the identities

$$
\sum _ { i = 0 } ^ { m + n + 1 } \xi _ { i } ^ { l } \prod _ { \stackrel { j = 0 } { j \neq i } } ^ { m + n + 1 } \frac 1 { ( \xi _ { j } - \xi _ { i } ) } = 0 , \qquad l = 0 , 1 , \ldots , m + n ,
$$

which are a consequence of equation (4.11). Thus expression (10.10) provides the equations

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 0 } ^ { m + n + 1 } \big [ f ( \xi _ { i } ) - ( - 1 ) ^ { i } h _ { k } \big ] \bigg [ \sum _ { j = 0 } ^ { n } b _ { j } \xi _ { i } ^ { j + l } \bigg ] } & { } \\ { \displaystyle \qquad \times \bigg [ \prod _ { j = 0 } ^ { m + n + 1 } \frac { 1 } { ( \xi _ { j } - \xi _ { i } ) } \bigg ] = 0 , \qquad l = 0 , 1 , \dots , n , } \end{array}
$$

which we write in matrix form

$$
A { \bf b } - h _ { k } B { \bf b } = 0 ,
$$

where $\mathbf { b }$ is the vector whose components are the coefficients $\{ b _ { j }$ ； $j = 0 , 1 , \ldots , n \}$ ,and where $\pmb { A }$ and $\pmb { B }$ are square matrices whose elements have the values

$$
A _ { l j } = \sum _ { i = 0 } ^ { m + n + 1 } f ( \xi _ { i } ) \xi _ { i } ^ { j + l } \bigg [ \prod _ { s = 0 \atop s \ne i } ^ { m + n + 1 } \frac { 1 } { ( \xi _ { s } - \xi _ { i } ) } \bigg ]
$$

and

$$
B _ { l j } = \sum _ { i = 0 } ^ { m + n + 1 } { ( - 1 ) ^ { i } \xi _ { i } ^ { j + l } \left[ \prod _ { \stackrel { s = 0 } { s \neq i } } ^ { m + n + 1 } { \frac { 1 } { ( \xi _ { s } - \xi _ { i } ) } } \right] } ,
$$

for $l = 0 , 1 , \ldots , n$ and $j = 0 , 1 , \ldots , n$

A non-zero vector b satisfies equation (10.13) if and only if the matrix $\left( A - h _ { k } B \right)$ is singular. Therefore the only values of $h _ { k }$ that are allowed by the system (10.6) are solutions of the generalized eigenvalue problem

$$
\operatorname* { d e t } ( A - h _ { k } B ) = 0 .
$$

Expressions (10.14) and (10.15） show that the matrices $\pmb { A }$ and $\pmb { B }$ are symmetric. Moreover the following condition is obtained.

# Theorem 10.2 The matrix $\pmb { B }$ is positive definite.

Proof. We let c be any vector in $\mathcal { R } ^ { n + 1 }$ that is not identically zero. It is sufficient to prove that the inequality

$$
\mathbf { c } ^ { \mathrm { { T } } } B \mathbf { c } > 0
$$

is satisfied. We let $\pmb { u }$ be the polynomial

$$
u ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } x ^ { i } , \qquad a \leqslant x \leqslant b ,
$$

and we note that not all of the numbers $\{ u ( \xi _ { i } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ are zero, even if $m = 0$ ·

The definition of $\pmb { B }$ and expression (10.3) give the equation

$$
\begin{array} { l } { { \displaystyle { \bf c } ^ { \bf T } B { \bf c } = \sum _ { l = 0 } ^ { n } \sum _ { j = 0 } ^ { n } c _ { l } c _ { j } \sum _ { i = 0 } ^ { m + n + 1 } \left( - 1 \right) ^ { i } \xi _ { i } ^ { j + l } \prod _ { s = 0 } ^ { m + n + 1 } \frac { 1 } { ( \xi _ { s } - \xi _ { i } ) } } } \\ { ~ } \\ { { \displaystyle ~ = \sum _ { i = 0 } ^ { m + n + 1 } \sum _ { l = 0 } ^ { n } \sum _ { j = 0 } ^ { n } \sum _ { \ell = 0 } ^ { n } \left( c _ { l } \xi _ { i } ^ { l } \right) \left( c _ { j } \xi _ { i } ^ { j } \right) \prod _ { s = 0 } ^ { m + n + 1 } \frac { 1 } { \left| \xi _ { s } - \xi _ { i } \right| } } } \\ { { \displaystyle ~ = \sum _ { i = 0 } ^ { m + n + 1 } \left[ u \left( \xi _ { i } \right) \right] ^ { 2 } \sum _ { \scriptstyle s = 0 } ^ { m + n + 1 } \frac { 1 } { \left| \xi _ { s } - \xi _ { i } \right| } } . } \end{array}
$$

Therefore the theorem is true.

The theorem implies that the matrix $\pmb { B }$ has a square root $B ^ { \frac { 1 } { 2 } }$ ,which is real, symmetric and non-singular. Therefore we may express equation (10.16) in the form

$$
( B ^ { - \frac { 1 } { 2 } } A B ^ { - \frac { 1 } { 2 } } - h _ { k } I ) = 0 .
$$

Because the matrix $B ^ { - \frac { 1 } { 2 } } A B ^ { - \frac { 1 } { 2 } }$ is symmetric, it follows that all values of $h _ { k }$ that satisfy condition (1O.16) are real, and the number of different roots of this equation is at most $( n + 1 )$ . For each of these roots a non-zero vector $\mathbf { b }$ can be found that satisfies equation (1O.13),and then the coefficients $\{ a _ { j } ; j = 0 , \ 1 , \dots , m \}$ are defined uniquely by the system (10.10).

Several different rational approximations may be generated in this way, but only one of them can satisfy inequality (1O.9). To prove this statement we let $r _ { k }$ and $\bar { r }$ be two approximations that are obtained from the solutions $h _ { k }$ and $\bar { h }$ of equation (10.16). It follows from the equations (10.6),and from the similar equations that define F, that the numbers $\{ r _ { k } ( \xi _ { i } ) - \bar { r } ( \xi _ { i } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ are all zero or their signs alternate. Therefore,if both $r _ { k }$ and $\tilde { r }$ have no singularities in $[ a , b ]$ ， then the difference $( r _ { k } - { \bar { r } } )$ has at least $( m + n + 1 )$ zeros. Hence $r _ { k }$ is equal to $\bar { r } .$

In order to reduce the time that is spent by the exchange algorithm on calculating approximations that fail to satisfy condition (10.9),it is helpful to carry forward from the previous iteration the number $h _ { k - 1 }$ ，because usually it is a good initial estimate of the required root of equation (10.16). One of the exercises at the end of this chapter shows that the required root is not necessarily the one of least modulus.

# 10.3 Some convergence properties of the exchange algorithm

Many of the convergence properties of the exchange algorithm in the rational case are similar to the ones that are obtained when $\mathcal { A }$ isa linear space that satisfies the Haar condition. In particular our next theorem shows that the levelled reference errors $\left\{ \left| h _ { k } \right| ; k = 1 , 2 , 3 , . . . \right\}$ increase strictly monotonically.

# Theorem 10.3

Let the approximation $r _ { k }$ and the number $h _ { k }$ satisfy the conditions of Theorem 10.1, where $f$ is a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ;$ let $e _ { k }$ be the error function

$$
e _ { k } ( x ) = f ( x ) - r _ { k } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

and let the points $\{ \xi _ { i } ^ { + } ; i = 0 , 1 , \ldots , m + n + 1 \}$ of the reference that is calculated for the $( k + 1 ) \mathrm { t h }$ iteration satisfy the following three conditions: $( a )$ they are in ascending order

$$
a \leqslant \xi _ { 0 } ^ { + } < \xi _ { 1 } ^ { + } < . . . < \xi _ { m + n + 1 } ^ { + } \leqslant b ;
$$

$( b )$ the inequalities

$$
\big | e _ { k } ( \xi _ { i } ^ { + } ) \big | \geqslant \big | h _ { k } \big | , \qquad i = 0 , 1 , \ldots , m + n + 1 ,
$$

hold and at least one of them is strict; and $( c )$ the signs of the numbers $\{ e _ { k } ( \xi _ { i } ^ { + } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ alternate. Let the number $h _ { k + 1 }$ and the approximation $r _ { k + 1 }$ from $\bar { \mathcal { A } } _ { m n }$ be defined by the equations

$$
r _ { k + 1 } ( \xi _ { i } ^ { + } ) + ( - 1 ) ^ { i } h _ { k + 1 } = f ( \xi _ { i } ^ { + } ) , \qquad i = 0 , 1 , \dots , m + n + 1 .
$$

Then the inequality

$$
\left| h _ { k + 1 } \right| > \left| h _ { k } \right|
$$

is satisfied.

Proof. Suppose that condition (10.25) is not obtained. Then expressions (10.23) and (10.24) imply the bounds

$$
\big | e _ { k + 1 } ( \xi _ { i } ^ { + } ) \big | \leqslant \big | e _ { k } ( \xi _ { i } ^ { + } ) \big | , \qquad i = 0 , 1 , \ldots , m + n + 1 ,
$$

where $e _ { k + 1 }$ is the error function

$$
e _ { k + 1 } ( x ) = f ( x ) - r _ { k + 1 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

We consider the sequence $\{ e _ { k } ( \xi _ { i } ^ { + } ) - e _ { k + 1 } ( \xi _ { i } ^ { + } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ It follows from expression (10.26)，from Theorem 7.5,and from the definitions (10.21) and (10.27),that the function $\left( r _ { k + 1 } - r _ { k } \right)$ has at least $( m + n + 1 )$ zeros in $[ a , b ]$ .Therefore the functions $r _ { k + 1 }$ and $r _ { k }$ are the same. In particular, for $i = 0 , 1 , \ldots , m + n + 1$ , the error $\big | e _ { k } \big ( \xi _ { i } ^ { + } \big ) \big |$ is equal to $\left| e _ { k + 1 } ( \xi _ { i } ^ { + } ) \right|$ . Hence, because one of the conditions (10.23) is satisfied as a strict inequality,it follows from equation (10.24) that the increase (10.25) is obtained. This conclusion contradicts the hypothesis that is made at the beginning of the proof. Therefore the theorem is true.□

This theorem allows us to extend Theorem 8.2 to the rational case, provided that on each iteration a solution of the equations (10.6) can be calculated that satisfies condition (1O.9). Hence we find that, if the interval $a \leqslant x \leqslant b$ is replaced by a set of discrete points, then the strategy of forcing the levelled reference error to increase on each iteration can provide the best approximation. Usually satisfactory convergence is obtained in the continuous case also.

However, we noted earlier that the exchange algorithm fails occasion-ally. The form of the failure is that sometimes none of the values of $h _ { k }$ that solve equation (1O.16) gives an approximating function that satisfies condition (10.9). Its cause is closely related to the fact that, if the function

$$
r ^ { * } ( x ) = p ^ { * } ( x ) / q ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is the best approximation to a function $f \mathrm { f r o m } \ { \mathcal { C } } [ a , b ] ,$ , then sometimes the number of different values of $\pmb { x }$ that satisfy the equation

$$
\left| f ( x ) - r ^ { * } ( x ) \right| = \left\| f - r ^ { * } \right\|
$$

is less than $( m + n + 2 )$ . This case occurs only if the best approximation is ‘defective', which means that the actual degree of $p ^ { * }$ is less than $^ { m }$ and the actual degree of $q ^ { * }$ is less than $\pmb { n }$ ·

For example, suppose that $m = n = 2$ , and that the rational function

$$
r ^ { * } ( x ) = \frac { a _ { 0 } + a _ { 1 } x } { b _ { 0 } + b _ { 1 } x } , \qquad a \leqslant x \leqslant b ,
$$

is bounded. Let $f$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ such that equation (10.29) holds for only five values of $x , \{ \xi _ { i } ; i = 0$ ,1,2,3,4} say,where the signs of the numbers $\{ f ( \xi _ { i } ) - r ^ { * } ( \xi _ { i } ) ; i = 0 , 1 , 2 , 3 , 4 \}$ alternate. We claim that $r ^ { \ast }$ is a best approximation to $f .$ To prove this statement we suppose that F is even better. The method of proof of Theorem 10.1 implies that $( r ^ { * } - { \bar { r } } )$ is the ratio of two cubic polynomials that has four zeros. Hence $\bar { r } = r ^ { * }$ ,which confirms that $r ^ { * }$ is a best approximation.

In order to show that the exchange algorithm can break down, we let $m = n = 1$ , we let the reference contain the four points $\{ - 4 , - 1 , 1 , 4 \}$ ,and we choose a function $f$ that has the values $f ( - 4 ) = 0 , f ( - 1 ) = 1 , f ( 1 ) = 1$ and $f ( 4 ) = 0$ .This data has been chosen because the function $r$ in $\boldsymbol { \bar { \mathcal { A } } } _ { 1 1 }$ that minimizes expression (10.4) is the constant function

$$
\begin{array} { r } { r ( x ) = \frac { 1 } { 2 } , \qquad a \leqslant x \leqslant b . } \end{array}
$$

Therefore the conditions (10.6） are not obtained. The solutions of equation (10.16) are the values $h _ { k } = - 0 . 4$ and $h _ { k } = 0 . 4$ .They give the rational approximations $( 1 . 6 - 0 . 2 x ) / ( 2 - x )$ and $( 1 . 6 + 0 . 2 x ) / ( 2 + x ) .$ ， which satisfy the equations (10.6). However, both approximations are unacceptable because they contain singularities in the range of $x$

Some computer programs that apply the exchange algorithm do not abandon the calculation when this kind of difficulty occurs. Instead they may try different references or they may reduce the values of $^ { m }$ or $_ n$ However, there may not be a computer program of this kind that treats all cases successfully.

# 10.4 Methods based on linear programming

Many of the difficulties that occur sometimes, when the exchange algorithm is used to calculate the best rational approximation to a function $f$ in $\mathcal { C } [ a , b ] ,$ ，are due to the fact that the system of equations (10.6) is not linear in the unknowns.However, if we let $h$ be an estimate of the least maximum error, then the problem of finding out whether the estimate is too low or too high can be reduced to a set of linear conditions. Specifically,there is an approximation of the form (10.2) that satisfies the bound

$$
| f ( x ) - r ( x ) | \leqslant h , \qquad a \leqslant x \leqslant b ,
$$

if and only if there exist values of the coefficients $\{ a _ { i } ; i = 0 , 1 , \ldots , m \}$ and $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ such that the inequalities

$$
q ( x ) > 0 , \qquad a \leqslant x \leqslant b ,
$$

and

$$
\begin{array} { l l } { { p ( x ) - f ( x ) q ( x ) \leqslant h q ( x ) } } \\ { { f ( x ) q ( x ) - p ( x ) \leqslant h q ( x ) } } \end{array} \quad \quad x \in X ,
$$

are obtained, where $\boldsymbol { x }$ is the range of $x$ ，and where $p$ and $q$ are the numerator and denominator of $r .$ Because $r$ is unchanged if $p$ and $q$ are multiplied by a constant, we may replace expression (10.33) by the condition

$$
q ( x ) \geq \delta , \qquad x \in X ,
$$

where $\pmb { \delta }$ is any positive constant.

The notation $\pmb { X }$ is used for the range of $x$ , because,in order to apply linear programming methods, it is usual to replace the range $a \leqslant x \leqslant b$ by a set of discrete points. We suppose that this has been done. Then calculating whether an approximation $p / q$ satisfies conditions (10.34) and (10.35） is a standard linear programming procedure. Many trial values of $\pmb { h }$ may be used, and they can be made to converge to the least maximum error by a bracketing and bisection procedure.Whenever $h$ exceeds the least maximum error, the linear programming calculation gives feasible coefficients for $p$ and $\pmb q .$ provided that the discretization of $\pmb { X }$ in condition (10.35) does not cause inequality (10.33) to fail.

This procedure has the property that, even if $\pmb { h }$ is much larger than necessary, then it is usual for several of the conditions (10.34) to be satisfied as equations. It would be better, however, if the maximum error of the calculated approximation $p / q$ were less than $\pmb { h }$ A way of achieving this useful property is to replace expression (10.34) by the conditions

$$
\begin{array} { r l } & { p ( x ) - f ( x ) q ( x ) \leqslant h q ( x ) + \varepsilon } \\ & { f ( x ) q ( x ) - p ( x ) \leqslant h q ( x ) + \varepsilon } \end{array} \quad \quad x \in X ,
$$

where $\pmb \varepsilon$ is an extra variable. Moreover, the overall scaling of $\pmb { p }$ and $\pmb q$ is fixed by the equation

$$
b _ { 0 } + b _ { 1 } \zeta + b _ { 2 } \zeta ^ { 2 } + . . . + b _ { n } \zeta ^ { n } = 1 ,
$$

where $\pmb { \zeta }$ is any fixed point of $X ,$ the value $\zeta = 0$ being a common choice. For each trial value of $\pmb { h }$ the variable $\pmb \varepsilon$ is minimized,subject to the conditions (10.36) and (10.37) on the variables $\{ a _ { i } ; i = 0 , 1 , \ldots , m \} ,$ $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ and $\pmb \varepsilon$ , which is still a linear programming calculation.

It is usual to omit condition (10.35) from this calculation,and to choose $h$ to be greater than the least maximum error.In this case the final value of $\pmb \varepsilon$ is negative.Hence condition (1O.35） is unnecessary，because expression (10.36) implies that $q ( x )$ is positive for all $x \in X .$ If the calculated value of $\pmb \varepsilon$ is zero, then usually $p / q$ is the best approximation, but very occasionally there are difficulties due to $p ( { \pmb x } )$ and $q ( x )$ both being zero for a value of $x$ in $X .$ If $\pmb \varepsilon$ is positive, then the conditions (10.34) and (10.35） are inconsistent, so $h$ is less than the least maximum error. Equation (10.37） is important because,if it is left out,and if the conditions (1O.36) are satisfied for a negative value of $\pmb \varepsilon$ ,then $\pmb \varepsilon$ can be made arbitrarily large and negative by scaling all the variables of the linear programming calculation by a sufficiently large positive constant. Hence the purpose of condition (10.37) is to ensure that $\pmb \varepsilon$ is bounded below.

The introduction of $\pmb \varepsilon$ gives an iterative method for adjusting $\pmb { h }$ A high value of $\pmb { h }$ is required at the start of the first iteration. Then $p , q$ and $\pmb \varepsilon$ are calculated by solving the linear programming problem that has just been described. The value of $\pmb { h }$ is replaced by the maximum error of the current approximation $p / q$ . Then a new iteration is begun. It can be shown that the calculated values of $\pmb { h }$ converge to the least maximum error from above.This method is called the ‘differential correction algorithm'.

A simple device provides a large reduction in the number of iterations that are required by this procedure.It is to replace the conditions (10.36) of the linear programming calculation by the inequalities

$$
\begin{array} { r l } & { p ( x ) - f ( x ) q ( x ) \leqslant h q ( x ) + \varepsilon \bar { q } ( x ) } \\ & { f ( x ) q ( x ) - p ( x ) \leqslant h q ( x ) + \varepsilon \bar { q } ( x ) } \end{array} \biggr \} , \qquad x \in X ,
$$

where $\bar { q } ( { \pmb x } )$ is a positive function that is an estimate of the denominator of the best approximation. On the first iteration we let $\bar { q } ( { \pmb x } )$ be the constant function whose value is one, but on later iterations it is the denominator of the approximation that gave the current value of $\pmb { h } .$ .Some fundamental questions on the convergence of this method are still open in the case when the range of $x$ is the interval $[ a , b ]$

# 10 Exercises

10.1 Let $f$ be a function in $\mathcal { C } [ a , b ] ,$ and let $r ^ { * } = p ^ { * } / q ^ { * }$ and $\bar { r } = \bar { p } / \bar { q }$ be functions in $\mathcal { \bar { A } } _ { m n }$ that satisfy the condition $\left\| \boldsymbol { f } - \boldsymbol { \bar { r } } \right\| _ { \infty } < \| \boldsymbol { f } - \boldsymbol { r } ^ { * } \| _ { \infty } ,$ where $q ^ { * } ( x )$ and $\bar { q } ( x )$ are positive for all $\pmb { x }$ in $[ a , b ]$ .Let $r$ be the rational function $\{ [ p ^ { * } ( x ) + \theta \bar { p } ( x ) ] / [ q ^ { * } ( x ) + \theta \bar { q } ( x ) ] ;$ $a \leqslant x \leqslant b \}$ ， where $\pmb \theta$ is a positive number. Prove that the inequality $\| f - r \| _ { \infty } <$ $\| f - r ^ { * } \| _ { \infty }$ is satisfied. Allowing $\pmb \theta$ to change continuously gives a set of rational approximations that is useful to some theoretical work.

10.2 Let $r ^ { * }$ be an approximation from $\bar { \mathcal { A } } _ { m n }$ to a function $f$ in $\mathcal { C } [ a , b ] ,$ and let $\mathcal { Z } _ { \mathbf { M } }$ be the set of points $\{ x : | f ( x ) - r ^ { * } ( x ) | = \| f - r ^ { * } \| _ { \infty } ;$ $a \leqslant x \leqslant b $ .Prove that, if $\bar { r }$ is a function in $\mathcal { \bar { A } } _ { m n }$ that satisfies the sign conditions

$$
\begin{array} { r } { \big [ f ( x ) - r ^ { * } ( x ) \big ] \big [ \bar { r } ( x ) - r ^ { * } ( x ) \big ] > 0 , \qquad x \in \mathcal { Z } _ { \mathsf { M } } , } \end{array}
$$

then there exists a positive number $\pmb \theta$ such that the approximation $r ,$ defined in Exercise 10.1,gives the reduction $\| f - r \| _ { \infty } <$ $\| f - r ^ { * } \| _ { \infty }$ in the error function. Thus Theorem 7.1 can be extended to rational approximation.

10.3 Let $f$ be a function in $\mathcal { C } [ 0 , 6 ]$ that takes the values $f ( \xi _ { 0 } ) = f ( 0 ) =$ 0.0, $f ( \xi _ { 1 } ) = f ( 2 ) = 1 . 0$ ， $f ( \xi _ { 2 } ) = f ( 5 ) = 1 . 6 $ and $f ( \xi _ { 3 } ) = f ( 6 ) = 2 . 0$ Calculate and plot the two functions in the set $\mathcal { A } _ { 1 1 }$ that satisfy the equations (10.10).

10.4 Prove that the function $\{ r ^ { * } ( x ) = { \frac { 3 } { 4 } } x$ ； $- 1 \leqslant x \leqslant 1 \}$ is the best approximation to $\{ f ( x ) = x ^ { 3 }$ ； $- 1 \leqslant x \leqslant 1 \}$ from the set $\vec { \mathcal { A } } _ { 2 1 }$ ,but that it is not the best approximation from the set $\displaystyle \overline { { \mathcal { A } } } _ { 1 2 }$

10.5 Prove that,if in the iteration that is described in the last paragraph of this chapter, the function $\bar { q }$ is the denominator of a best approximation, and $\pmb { h }$ is any real number that is greater than the least maximum error, then the iteration calculates directly a function $p / q$ that is a best approximation.

10.6 Let $r ^ { * } = p ^ { * } / q ^ { * }$ be a function in $\mathcal { \bar { A } } _ { m n }$ such that the only common factors of $p ^ { * }$ and $q ^ { * }$ are constants,and let the defect $\pmb { d }$ be the smaller of the integers $\left\{ m - \right.$ (actual degree of $p ^ { * }$ ， $n -$ (actual degree of $q ^ { * } ) \}$ .Prove that, if $\left\{ \xi _ { i } ; \ : i = 1 , 2 , \ldots , k \right\}$ is any set of distinct points in $( a , b )$ ,where $k \leqslant m + n - d$ ， then there exists a function $\bar { r }$ in $\bar { \mathcal { A } } _ { m n }$ such that the only zeros of the function $( { \bar { r } } - r ^ { * } )$ are simple zeros at the points $\{ \xi _ { i } ; i = 1 , 2 , \ldots , k \}$ .Hence deduce from Exercise 10.2 a characterization theorem for minimax rational approximation that is analogous to Theorem 7.2.

10.7 Let $f$ be a function that takes the values $f ( \xi _ { 0 } ) = f ( 0 . 0 ) = 1 2$ ， $f ( \xi _ { 1 } ) = f ( 1 ) = 8 ,$ $f ( \xi _ { 2 } ) = f ( 2 ) = - 1 2$ ，and $f ( \xi _ { 3 } ) = f ( 3 ) = - 7$ . Calculate the two functions in the set $\mathcal { A } _ { 1 1 }$ that satisfy the equations (10.10). Note that the function that does not have a singularity in the interval [O,3] is derived from the solution $h _ { k }$ of equation (10.16) that has the larger modulus.

10.8 Investigate the calculation of the function in $\mathcal { \bar { A } } _ { 1 1 }$ that minimizes expression (10.4),where the data have the form $f ( \xi _ { 0 } ) = f ( - 4 ) =$ $\varepsilon _ { 0 } , f ( \xi _ { 1 } ) = f ( - 1 ) = 1 + \varepsilon _ { 1 }$ ， $f ( \xi _ { 2 } ) = f ( 1 ) = 1 + \varepsilon _ { 2 } .$ ,and $f ( \xi _ { 3 } ) = f ( 4 ) =$ $\pmb { \varepsilon _ { 3 } }$ ， and where the moduli of the numbers $\{ \varepsilon _ { i } ; i = 0 , 1 , 2 , 3 \}$ are very small.

10.9 Let $f \in { \mathcal { C } } [ a , b ] .$ let $\pmb { X }$ be a set of discrete points from $[ a , b ] ,$ and let $r ^ { * } = p ^ { * } / q ^ { * }$ be a best approximation from $\mathcal { A } _ { m n }$ to $f$ on $X ,$ subject to the conditions $\{ q ^ { * } ( x ) > 0 ; x \in X \}$ and $q ^ { * } ( \zeta ) = 1$ ,where $\pmb { \zeta }$ is a point of $\boldsymbol { x }$ .Let the version of the differential correction algorithm that depends on condition (10.36) be applied to calculate $r ^ { * }$ ，where $\pmb { h }$ is chosen and adjusted in the way that is described in Section 10.5. Prove that on each iteration the calculated value of $\pmb \varepsilon$ satisfies the bound

$$
\varepsilon \leqslant - ( h - \| f - r ^ { * } \| ) \operatorname* { m i n } _ { x \in X } q ^ { * } ( x ) .
$$

Hence show that, if the normalization condition (10.37) keeps the variables $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ bounded throughout the calculation, then the sequence of values of $h$ converges to $\| f - r ^ { * } \|$

10.10Prove that, if the points $\{ \xi _ { i } ; i = 0 , 1 , 2 , 3 \}$ are in ascending order, and if the function values $\left\{ f ( \xi _ { i } ) ; i = 0 , 1 , 2 , 3 \right\}$ increase strictly monotonically, then one of the solutions $r _ { k }$ in the set $\mathcal { A } _ { 1 1 }$ to the equations (1O.6) has no singularities in the range $[ \xi _ { 0 } , \xi _ { 3 } ] _ { : }$ ,and the other solution has a singularity in the interval $( \xi _ { 1 } , \xi _ { 2 } )$ .

# 11

# Least squares approximation

# 11.1 The general form of a linear least squares calculation

Given a set $\boldsymbol { \mathscr { A } }$ of approximating functions that is a subset of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ， and given a fixed positive function $\{ w ( x ) ; a \leqslant x \leqslant b \} ,$ ，which we call a‘weight function',we define the element $p ^ { * }$ of $\mathscr { A }$ to be a best weighted least squares approximation from $\mathscr { A }$ to $f ,$ if $p ^ { * }$ minimizes the expression

$$
\int _ { a } ^ { b } w ( x ) [ f ( x ) - p ( x ) ] ^ { 2 } \mathrm { d } x , \qquad p \in \mathcal { A } .
$$

Often $\scriptstyle { \mathcal { A } }$ is a finite-dimensional linear space. We study the conditions that $p ^ { * }$ must satisfy in this case, and we find that there are some fast numerical methods for calculating $p ^ { * }$

It is convenient to express the properties that are obtained by $p ^ { * }$ in terms of scalar products. For each $f$ and $\pmb { g }$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ we let $( f , g )$ be the scalar product

$$
( f , g ) = \int _ { a } ^ { b } w ( x ) f ( x ) g ( x ) \mathrm { d } x ,
$$

which satisfies all the conditions that are stated in the frst paragraph of Section 2.4. Therefore we introduce the norm

$$
\| f \| = ( f , f ) ^ { \frac { 1 } { 2 } } , \qquad f \in { \mathcal { C } } [ a , b ] ,
$$

and, in accordance with the ideas of Chapter 1, we define the distance from $f$ to $\pmb { g }$ to be $\| f - g \|$ . Hence expression (11.1) is the square of the distance

$$
\| f - p \| = ( f - p , f - p ) ^ { \frac { 1 } { 2 } } , \qquad p \in \mathcal { A } .
$$

Therefore the required approximation $p ^ { * }$ is a ‘best' approximation from $\mathscr { A }$ to $f .$ It follows from Theorem 1.2 that, if $\pmb { \mathcal { A } }$ is a finite-dimensional linear space, then a best approximation exists. Further, because the method of proof of Theorem 2.7 shows that the norm (11.3) is strictly convex, it follows from Theorem 2.4 that only one function in $\mathscr { A }$ minimizes expression (11.1).

One of the main advantages of the scalar product notation is that the theory that is developed applies,not only to continuous least squares approximation problems, but also to discrete ones.Discrete calculations occur, for example, when one requires an approximation to a function $f$ in ${ \mathcal { C } } [ a , b ]$ ,but, instead of being able to calculate $f ( x )$ for any $x$ in $a \leqslant x \leqslant b$ ， one can only measure the value of $f ( x )$ ，where the measuring process includes a random error.Let the values of $\pmb { x }$ at which the measurements are taken be $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ ,let $y _ { j }$ be the measured value of $f ( x _ { j } )$ ， and let the variance of the measurement be $1 / w _ { j } .$ If $\mathcal { A } _ { 0 }$ is the set of approximating functions,and if the random errors have a normal distribution, then it is appropriate for statistical reasons to seek the function $p _ { 0 } ^ { * }$ in $\mathcal { A } _ { 0 }$ that minimizes the weighted sum of squares

$$
\sum _ { j = 1 } ^ { m } w _ { j } [ y _ { j } - p _ { 0 } ( x _ { j } ) ] ^ { 2 } , \qquad p _ { 0 } \in \mathcal { A } _ { 0 } .
$$

It happens often that one minimizes this expression even when the distribution of data errors is not normal, because the numerical methods for calculating $\boldsymbol { p } _ { 0 } ^ { * }$ are easy to apply when $\mathcal { A } _ { 0 }$ is a linear space.

We wish to introduce scalar products in such a way that expression (11.5) is analogous to the square of the distance (11.4). However, the definition

$$
( f , g ) = \sum _ { j = 1 } ^ { m } w _ { j } f ( x _ { j } ) g ( x _ { j } )
$$

is unacceptable,because in this case expression (11.3) fails to satisfy the axioms of a norm,due to the fact that $( f , f )$ is zero for some functions $f$ that are not identically zero.Instead we take note of the fact that the data $\{ y _ { j } ; j = 1 , 2 , \dots , m \}$ define a vector $y$ in $\mathcal { R } ^ { m }$ .For each ${ p } _ { 0 }$ in $\scriptstyle { \mathcal { A } } _ { 0 }$ ,we let $X ( p _ { 0 } )$ be the vector in ${ \mathcal { R } } ^ { m }$ whose components have the values $\{ p _ { 0 } ( x _ { j } ) ; j =$ $1 , 2 , \ldots , m \}$ , and we let $\mathcal { A }$ be the set $\{ X ( p _ { 0 } ) ; p _ { 0 } \in \mathcal { A } _ { 0 } \}$ ,which is a subset of ${ \mathcal { R } } ^ { m }$ .Calculating the function $p _ { 0 } ^ { * }$ in $\mathcal { A } _ { 0 }$ that minimizes expression (11.5) is equivalent to obtaining the vector $p ^ { * }$ in $\mathscr { A }$ that gives the least value of the sum of squares

$$
\sum _ { j = 1 } ^ { m } w _ { j } \big [ y _ { j } - p _ { j } \big ] ^ { 2 } , \qquad p \in \mathcal { A } ,
$$

where $\{ p _ { j } ; j = 1 , 2 , \ldots , m \}$ are the components of $p$ . We can now let the scalar product $( u , v )$ have the value

$$
( u , v ) = \sum _ { j = 1 } ^ { m } w _ { j } u _ { j } v _ { j }
$$

for any vectors $\pmb { u }$ and $v$ in ${ \mathcal { R } } ^ { m }$ ， and we let $\left\| u \right\|$ be $( u , u ) ^ { \frac { 1 } { 2 } }$ . Hence the calculation of $p ^ { * }$ becomes a best approximation problem,where we require to minimize the distance

$$
\| y - p \| = ( y - p , y - p ) ^ { \frac { 1 } { 2 } } , \qquad p \in \mathcal { A } .
$$

In the usual case when $\mathcal { A } _ { 0 }$ is a linear subspace of $\mathcal { C } [ a , b ] .$ then $\mathscr { A }$ is a finite-dimensional linear subspace of ${ \mathcal { R } } ^ { m }$ .Hence Theorems 1.2 and 2.4 imply that a unique element of $\mathcal { A }$ minimizes expression (11.9).

Because expressions(11.4) and (11.9) are both distances in a Hilbert space,and because some highly useful properties are satisfied when the set of approximating functions is a linear space,we study the following problem.Let $\mathscr { A }$ be a finite-dimensional linear subspace of a Hilbert space ${ \mathcal { B } } .$ For any $f$ in $\mathcal { B }$ ,calculate the best approximation from $\mathscr { A }$ to $f .$

# 11.2 The least squares characterization theorem

The following characterization theorem shows that the solution to the problem that is stated in the last paragraph may be regarded as an orthogonal projection onto the set of approximating functions, where the elements $f$ and $\pmb { g }$ of a Hilbert space are defined to be orthogonal if the scalar product $( f , g )$ is zero.

# Theorem 11.1

Let $\mathscr { A }$ be a linear subspace of a Hilbert space $\mathcal { B }$ , and let $f$ be any element of $\mathcal { B }$ . The point $p ^ { * }$ in $\mathscr { A }$ is the best approximation from $\mathscr { A }$ to $f$ if and only if the error $e ^ { * } { = } f { - } p ^ { * }$ satisfies the orthogonality conditions

$$
( e ^ { * } , p ) = 0 , \qquad p \in \mathcal { A } .
$$

Proof. Suppose first that $( e ^ { * } , p )$ is non-zero for some $p$ in $\mathcal { A } .$ .Then the square of the distance from $( p ^ { * } + \lambda p )$ to $f$ is the expression

$$
\left\| f - p ^ { * } - \lambda p \right\| ^ { 2 } = \left\| f - p ^ { * } \right\| ^ { 2 } - 2 \lambda \left( e ^ { * } , p \right) + \lambda ^ { 2 } \left\| p \right\| ^ { 2 } ,
$$

where $\pmb { \lambda }$ is a real parameter. The value of $\pmb { \lambda }$ that minimizes expression (11.11) is not equal to zero. Therefore $p ^ { * }$ is not the best approximation from $\mathscr { A }$ to $f .$

Conversely, suppose that $( e ^ { * } , p )$ is zero for all $\pmb { p }$ in $\mathcal { A } .$ Let $q ^ { * }$ be any element of $\mathcal { A }$ ，From the properties of scalar products we deduce the equation

$$
\begin{array} { r l } & { \| f - q ^ { * } \| ^ { 2 } - \| f - p ^ { * } \| ^ { 2 } } \\ & { \quad = \| q ^ { * } \| ^ { 2 } - \| p ^ { * } \| ^ { 2 } - 2 ( f , q ^ { * } ) + 2 ( f , p ^ { * } ) } \\ & { \quad = \| q ^ { * } - p ^ { * } \| ^ { 2 } + 2 ( f - p ^ { * } , p ^ { * } - q ^ { * } ) . } \end{array}
$$

The last term is zero by hypothesis. Hence we obtain the bound

$$
\begin{array} { c } { \| f - q ^ { * } \| ^ { 2 } = \| f - p ^ { * } \| ^ { 2 } + \| q ^ { * } - p ^ { * } \| ^ { 2 } } \\ { \geqslant \| f - p ^ { * } \| ^ { 2 } , } \end{array}
$$

which holds for all $q ^ { * }$ in ${ \mathcal { A } } .$ Therefore $p ^ { * }$ is the best approximation.

Figure 11.1 presents a geometric view of this theorem. The point $p ^ { * }$ is the best approximation from ${ \mathcal { A } } \tan f .$ The point $q ^ { * }$ is any other point of $\mathcal { A }$ The orthogonality condition is shown by the standard symbol for a right-angle. Moreover, the first line of expression (11.13） states that Pythagoras's Theorem is obtained by the points of Figure 11.1, namely the square of the distance from $f$ to $q ^ { * }$ is equal to the square of the distance from $f$ to $p ^ { * }$ plus the square of the distance from $q ^ { * }$ to $p ^ { * }$ ·

Expression (11.13) is useful in two other ways. It provides an alter-native proof of the uniqueness of the best approximation,for it shows that $\| f - q ^ { * } \|$ is larger than $\| f - p ^ { * } \|$ if $q ^ { * }$ is not equal to $p ^ { * }$ . Secondly, by letting $q ^ { * }$ be the zero element, we obtain the equation

$$
\| f \| ^ { 2 } { \cdot } = \| p ^ { * } \| ^ { 2 } + \| f - p ^ { * } \| ^ { 2 } .
$$

Some interesting consequences of this equation are found later.

# 11.3 Methods of calculation

In order to calculate a best least squares approximation from a linear space $\mathcal { A } _ { : }$ , we choose a set of functions, $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ say, that span $\mathcal { A } .$ . Often a set of basis functions is present in the definition of $\mathcal { A } .$ We continue to let $p ^ { * }$ be the best approximation. Therefore we require the values of the coefficients $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ in the expression

$$
p ^ { * } = \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } .
$$

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0002_pages_0071-0140/auto/images/0c50b4b75d7ea9b87fd6f8e727e26a92e7541240a4a1080991f48f47380cc4a3.jpg)  
Figure 11.1. A geometric view of the least squares characterization theorem.

We suppose that the elements $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ are linearly independent, which is equivalent to supposing that the dimension of $\mathcal { A }$ is $( n + 1 )$ ， in order that the problem of determining these coefficients has a unique solution. Because every element of $\mathscr { A }$ is a linear combination of the basis elements,it follows from Theorem 11.1 that expression (11.15) is the best approximation from $\mathscr { A }$ to $f$ if and only if the conditions

$$
\left( \phi _ { i } , f - \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } \right) = 0 , \qquad i = 0 , 1 , \ldots , n ,
$$

are satisfied. They can be written in the form

$$
\sum _ { j = 0 } ^ { n } \big ( \phi _ { i } , \phi _ { j } \big ) c _ { j } ^ { * } = \big ( \phi _ { i } , f \big ) , \qquad i = 0 , 1 , \dots , n .
$$

Thus we obtain a square system of linear equations in the required coefficients, that are called the ‘normal equations’ of the least squares calculation.

The normal equations may also be derived by expressing a general element of $\mathscr { A }$ in the form

$$
p = \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ,
$$

where $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$ is a set of real parameters. Their values have to be chosen to minimize the expression

$$
( f - p , f - p ) = ( f , f ) - 2 \sum _ { i = 0 } ^ { n } c _ { i } ( \phi _ { i } , f ) + \sum _ { i = 0 } ^ { n } \sum _ { j = 0 } ^ { n } c _ { i } c _ { j } ( \phi _ { i } , \phi _ { j } ) .
$$

Therefore, for $i = 0 , 1 , \ldots , n$ ， the derivative of this expression with respect to $c _ { i }$ must be zero.These conditions are just the normal equations.

We note that the matrix of the system (11.17) is symmetric.Further, if $\{ z _ { i } ; i = 0 , 1 , \ldots , n \}$ is a set of real parameters, the identity

$$
\sum _ { i \mathop { = } 0 } ^ { n } \sum _ { j \mathop { = } 0 } ^ { n } z _ { i } z _ { j } ( \phi _ { i } , \phi _ { j } ) = \biggl ( \sum _ { i \mathop { = } 0 } ^ { n } z _ { i } \phi _ { i } , \sum _ { j \mathop { = } 0 } ^ { n } z _ { j } \phi _ { j } \biggl )
$$

holds. Because the right-hand side is the square of $\big \| \sum z _ { i } \phi _ { i } \big \|$ , it is zero only if all the parameters are zero. Hence the matrix of the system (11.17) is positive definite. Therefore there are many good numerical procedures for solving the normal equations. The technique of calculating the required coefficients $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ from the normal equations suggests itself. Often this is an excellent method, but sometimes it causes unnecessary loss of accuracy.

For example, suppose that we have to approximate a function $f$ in $\mathcal { C } [ 1 , 3 ]$ by a linear function

$$
p ^ { * } ( x ) = c _ { 0 } ^ { * } + c _ { 1 } ^ { * } x , \qquad 1 \leqslant x \leqslant 3 ,
$$

and that we are given measured values of f on the point set {xi =i; i = 1,2,3}.Let the data be y1 = 2.0≈f(1.0),y2=2.8≈f(2.0),and y3=4.2 = f(3.0),where the variances of the measurements are 1/M, 0.1 and 0.1 respectively. In order to demonstrate the way in which accuracy can be lost, we let M be much larger than ten. The normal equations are the system

$$
{ \binom { M + 2 0 } { M + 5 0 } } M + 5 0 \atop { M + 1 3 0 } { \binom { c _ { 0 } ^ { * } } { c _ { 1 } ^ { * } } } = { \binom { 2 M + 7 0 } { 2 M + 1 8 2 } } ,
$$

which has the solution

$$
\begin{array} { l } { { c _ { 0 } ^ { * } = 0 . 9 6 M / ( M + 2 ) } } \\ { { c _ { 1 } ^ { * } = ( 1 . 0 4 M + 2 . 8 ) / ( M + 2 ) } } \end{array} \biggr \} .
$$

We note that there is no cancellation in expression (11.23), even if $M$ is large.In this case the values of $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ are such that the difference $\left[ p ^ { * } ( 1 . 0 ) - y _ { 1 } \right]$ is small,and the remaining degree of freedom in the coeffcients is fixed by the other two measurements of $f .$ However, to take an extreme case, suppose that $M$ has the value ${ 1 0 } ^ { 9 }$ , and that we try to obtain $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ from the system (11.22),on a computer whose relative accuracy is only six decimals.When the matrix elements of the normal equations are formed, their values are dominated so strongly by $M$ that the important information in the measurements $y _ { 2 }$ and $y _ { 3 }$ is lost. Hence it is not possible to obtain accurate values of $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ from the calculated normal equations by any numerical procedure.

One reason for the loss of precision is that high relative accuracy in the matrix elements of the normal equations need not provide similar accuracy in the required solution $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ .However, similar accuracy is always obtained if the system (11.17) is diagonal. Therefore many successful methods for solving linear least squares problems are based on choosing the functions $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ so that the conditions

$$
( \phi _ { i } , \phi _ { j } ) = 0 , \qquad i \neq j .
$$

are satisfied,in order that the matrix of the normal equations is diagonal. In this case we say that the basis functions are orthogonal. When $\mathscr { A }$ is the space ${ \mathcal { P } } _ { n }$ of algebraic polynomials,a useful technique for generating orthogonal basis functions is by means of a three-term recurrence relation,which is described in the next section.

In the example that gives the system (11.22), is a subspace of $\mathcal { R } ^ { 3 }$ ,and its basis vectors have the components

$$
\phi _ { 0 } = { \binom { 1 } { 1 } } \quad { \mathrm { a n d } } \quad \phi _ { 1 } = { \binom { 1 } { 2 } } .
$$

One way of making the basis vectors orthogonal is to replace $\phi _ { 1 }$ by the vector

$$
\begin{array} { r } { \bar { \phi } _ { 1 } = \phi _ { 1 } - \alpha \phi _ { 0 } , } \end{array}
$$

where $_ { \pmb { \alpha } }$ has the value $( M + 5 0 ) / ( M + 2 0 )$ . In this case the coefficients of the required least squares approximation

$$
p ^ { * } = \bar { c } _ { 0 } \phi _ { 0 } + \bar { c } _ { 1 } \bar { \phi } _ { 1 }
$$

satisfy the diagonal normal equations

$$
\left( { { \cal M } + 2 0 \atop 5 0 } \right) _ { M + 2 0 } ^ { \cal ( 0 ) } { \left( { { \overline { { c } } } _ { 0 } } \right) } = \left( { 2 { \cal M } + 7 0 \atop 5 2 M + 1 4 0 } \right) ,
$$

which gives the values

$$
\begin{array} { l } { \bar { c } _ { 0 } = ( 2 M + 7 0 ) / ( M + 2 0 ) } \\ { \bar { c } _ { 1 } = ( 1 . 0 4 M + 2 . 8 ) / ( M + 2 ) } \end{array} \biggr \} .
$$

Of course this calculation is equivalent to the earlier one in exact arithmetic. However, if we let $M = 1 0 ^ { 9 }$ again,and if the calculation is carried out on a six-decimal floating point computer, then we avoid the serious loss of accuracy that occurred before.

In general the use of orthogonal basis functions is recommended, because it happens frequently that information is lost when the normal equations are constructed. The form of the best least squares approxima-tion when the basis functions are orthogonal is suficiently important to be stated as a theorem.

# Theorem 11.2

Let $\mathcal { A }$ be a linear subspace of a Hilbert space $\mathcal { B }$ that is spanned by the basis functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ . If the orthogonality condition (11.24) is satisfied,then,for any $f$ in $\mathcal { B }$ ,the best approximation from $\mathscr { A }$ to $f$ is the function

$$
p ^ { * } = \sum _ { j = 0 } ^ { n } \frac { ( \phi _ { j } , f ) } { \| \phi _ { j } \| ^ { 2 } } \phi _ { j } .
$$


<!-- chunk 0003: pages 141-210 -->
Proof. Equations (11.17) and (11.24) imply that the coefficients of the required approximation (11.15) have the values

$$
{ c } _ { i } ^ { * } = ( \phi _ { i } , f ) / \| \phi _ { i } \| ^ { 2 } , \qquad i = 0 , 1 , \ldots , n ,
$$

which proves the theorem.□

Often the space $\mathcal { A }$ is defined by a sequence of independent basis functions $\{ \psi _ { i } ; i = 0 , 1 , \ldots , n \}$ , say.For example, if $\mathcal { A }$ is the space $\mathcal { P } _ { n }$ ,then $\psi _ { i }$ may be the function $\{ \psi _ { i } ( x ) = x ^ { i }$ ； $a \leqslant x \leqslant b \}$ . For $i = 0 , 1 , \ldots , n$ ,we let $\mathcal { A } _ { i }$ be the linear space that is spanned by the functions $\{ \psi _ { j } ; j = 0 , 1 , \ldots , i \}$ ， in order to describe a general method for choosing an orthogonal basis of $\mathcal { A }$

We let $\phi _ { 0 }$ be the function $\psi _ { 0 }$ .For $i \geqslant 1$ we let $\bar { \psi _ { i } }$ be any member of $\mathcal { A } _ { i }$ that is not in $\mathcal { A } _ { i - 1 }$ , and we let $q _ { i } ^ { * }$ be the best approximation from $\mathcal { A } _ { i - 1 }$ to ${ \bar { \psi } } _ { i } .$ We define $\phi _ { i }$ by the equation

$$
\phi _ { i } = { \bar { \psi } } _ { i } - q _ { i } ^ { * } .
$$

Because Theorem 11.1 states that $\phi _ { i }$ is orthogonal to all elements of $\mathcal { A } _ { i - 1 }$ ， the condition

$$
( \phi _ { i } , \phi _ { j } ) = 0 , \qquad j < i ,
$$

is satisfied.Hence the functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ , that are obtained from this construction,are an orthogonal basis of $\mathcal { A }$

This construction is particularly useful if we are given an element $f$ and an infinite sequence of functions $\{ \psi _ { i } ; i = 0 , 1 , 2 , \ldots \}$ in a Hilbert space $\mathcal { B }$ ， and we wish to make the error $\| f - p \|$ less than a prescribed accuracy $\pmb { \delta }$ ， where $p$ is a linear combination of the first $( n + 1 )$ terms of the sequence, and where the value of $\pmb { n }$ is not known in advance,because it is to be the smallest integer that is allowed by the required accuracy. The main advantage of the construction is that the definition of the orthogonal functions $\{ \phi _ { i } ; i = 0 , 1 , 2 , \ldots \}$ does not depend on $\pmb { n }$ . Hence the coefficients (11.31） are also independent of $\pmb { n }$ .For $i = 0 , 1 , 2 , \dots$ ，we define $p _ { i } ^ { * }$ to be the function

$$
p _ { i } ^ { * } = \sum _ { j = 0 } ^ { i } \frac { ( \phi _ { j } , f ) } { \| \phi _ { j } \| ^ { 2 } } \phi _ { j } .
$$

Because Theorem 11.2 shows that this function is the best approximation to $f$ from the linear space $\mathcal { A } _ { i }$ that is spanned by the functions $\{ \psi _ { j } ; j =$ $0 , 1 , \ldots , i \}$ ，we require $_ n$ to be the least integer that satisfies the condition

$$
\left\| f - { p _ { n } ^ { * } } \right\| \leqslant \delta .
$$

In fact it is not necessary to calculate each of the approximations (11.34),because equation (11.14) implies that expression (11.35) is equivalent to the inequality

$$
\| p _ { n } ^ { * } \| ^ { 2 } \geqslant \| f \| ^ { 2 } - \delta ^ { 2 } .
$$

Therefore we have only to choose $_ n$ so that $\| p _ { n } ^ { * } \|$ is sufficiently large. Because the orthogonality conditions and the definition (11.34) imply the equation

$$
\big \| p _ { n } ^ { * } \big \| ^ { 2 } = \sum _ { j = 0 } ^ { n } { \big ( } \phi _ { j } , f { \big ) } ^ { 2 } / \big \| \phi _ { j } \big \| ^ { 2 } ,
$$

it follows that the required value of $_ n$ can be calculated by summing the terms $\{ ( \phi _ { j } , f ) ^ { 2 } / \| \phi _ { j } \| ^ { 2 } ; j = 0 , 1 , 2 , . . . \} ,$ ， until the bound

$$
\sum _ { j = 0 } ^ { n } \frac { \left( \phi _ { j } , f \right) ^ { 2 } } { \left\| \phi _ { j } \right\| ^ { 2 } } { \geqslant } \| f \| ^ { 2 } - \delta ^ { 2 }
$$

is satisfied.

# 11.4 The recurrence relation for orthogonal polynomials

An important special case of least squares approximation is when the set of approximating functions $\boldsymbol { \mathscr { A } }$ is the linear space $\mathcal { P } _ { n }$ of all polynomials of degree at most $_ n$ . In the case of approximation on a point set, where the scalar product has the value (11.6), we take the point of view that ‘polynomial' means the vector that is obtained by evaluating the polynomial at the discrete points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ .This point of view is tenable when the number of different discrete points is greater than $_ n$ ， so we assume that this condition is satisfied,in order that the work of this section is relevant to both continuous and discrete least squares approximations.

Orthogonal polynomials can be constructed by the method that is described immediately after Theorem 11.2, where the basis functions are $\{ \psi _ { i } ( x ) = x ^ { i } ; i = 0 , 1 , \ldots , n \}$ . A version of this construction, that comes from a particular choice of the function $\bar { \psi _ { i } }$ in equation (11.32), is highly useful in practice, because it gives the following three-term recurrence relation.

# Theorem 11.3

Let $\scriptstyle \phi _ { 0 }$ be the constant function

$$
\phi _ { 0 } ( x ) = 1 , \qquad a \leqslant x \leqslant b .
$$

For $j \equiv 0$ ,let $\alpha _ { j }$ be the scalar

$$
\alpha _ { j } = ( \phi _ { j } , x \phi _ { j } ) / \big \| \phi _ { j } \big \| ^ { 2 } ,
$$

where $x \phi _ { j }$ is the polynomial $\{ x \phi _ { j } ( x ) ; a \leqslant x \leqslant b \}$ .Let $\phi _ { 1 }$ be the linear function

$$
\phi _ { 1 } ( x ) = ( x - \alpha _ { 0 } ) \phi _ { 0 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

For $j \geqslant 1$ ,let $\beta _ { j }$ be the scalar

$$
\beta _ { j } = \mathopen { } \mathclose \bgroup \left\| \phi _ { j } \aftergroup \egroup \right\| ^ { 2 } / \mathopen { } \mathclose \bgroup \left\| \phi _ { j - 1 } \aftergroup \egroup \right\| ^ { 2 } ,
$$

and let $\phi _ { j + 1 }$ be defined by the three-term recurrence relation

$$
\phi _ { j + 1 } ( x ) = ( x - \alpha _ { j } ) \phi _ { j } ( x ) - \beta _ { j } \phi _ { j - 1 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Then, for each $j ,$ , the function $\phi _ { j }$ is a polynomial of degree $j ,$ the coefficient of $x ^ { j }$ being unity. Moreover, the polynomials $\{ \phi _ { j } ; j = 0 , 1 , 2 , \ldots \}$ are orthogonal.

Proof. The first statement of the theorem is an immediate consequence of the definitions (11.39), (11.41) and (11.43). To establish the orthogonality conditions, we show that the definitions (11.41) and (11.43) are equivalent to the construction (11.32) where $\bar { \psi _ { i } }$ is the polynomial $x \phi _ { i - 1 }$ · Because we proceed by induction, we assume that the functions $\left\{ \phi _ { i } ; i = \right.$ $0 , 1 , \ldots , j \}$ ，defined in the statement of the theorem,are orthogonal. Therefore, by applying Theorem 11.2 to equation (11.32),it follows that the polynomial

$$
\phi _ { j + 1 } ( x ) = x \phi _ { j } ( x ) - \sum _ { i = 0 } ^ { j } \frac { \left( \phi _ { i } , x \phi _ { j } \right) } { \left\| \phi _ { i } \right\| ^ { 2 } } \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is orthogonal to $\{ \phi _ { i } ; i = 0 , 1 , \ldots , j \}$ . The definition of $\pmb { \alpha _ { 0 } }$ shows that this equation is equivalent to expression (11.41) when $j = 0$ .Hence it remains to prove that the functions (11.43) and (11.44) are the same when $j \geqslant 1$

Therefore we consider the terms under the summation sign of expression (11.44). When $i = j$ we find the term $\alpha _ { j } \phi _ { j } ( x )$ ， which is present in equation (11.43). When $i \leqslant j - 2$ , we make use of the relation

$$
\begin{array} { c } { { ( \phi _ { i } , x \phi _ { j } ) = ( x \phi _ { i } , \phi _ { j } ) } } \\ { { { } } } \\ { { = 0 , } } \end{array}
$$

which holds because $\phi _ { j }$ is orthogonal to every polynomial in $\mathscr { P } _ { j - 1 }$ . Hence it is correct that $\phi _ { i } ( x )$ is absent from equation (11.43) for $i \leqslant j - 2$ .The remaining term of the sum depends on the identity

$$
\begin{array} { r l } {  { ( \phi _ { j - 1 } , x \phi _ { j } ) = ( x \phi _ { j - 1 } , \phi _ { j } ) } } \\ & { = ( \phi _ { j } , \phi _ { j } ) + ( x \phi _ { j - 1 } - \phi _ { j } , \phi _ { j } ) } \\ & { = \| \phi _ { j } \| ^ { 2 } , } \end{array}
$$

which holds because $( x \phi _ { j - 1 } - \phi _ { j } )$ isin $\boldsymbol { \mathcal { P } } _ { j - 1 }$ . It follows that equation

(11.43) contains the correct multiple of $\phi _ { j - 1 }$ , which completes the proof that expressions (11.43) and (11.44) are equivalent.□

When this theorem is applied in practice,to obtain the best polynomial approximation to an element $f$ of a Hilbert space, it is usual to calculate the coefficient

$$
c _ { j } ^ { \ast } = ( \phi _ { j } , f ) / \| \phi _ { j } \| ^ { 2 }
$$

immediately after $\phi _ { j }$ is determined. At the end of the fitting procedure, it is suffcient to provide the values of the parameters $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ $\{ \alpha _ { j } ; j = 0 , 1 , \ldots , n - 1 \}$ and $\{ \beta _ { j } ; j = 1 , 2 , \ldots , n - 1 \}$ .Therefore the storage space that holds $\phi _ { j - 1 }$ may be re-used by $\phi _ { j + 1 }$ when formula (11.43) is applied,which is important sometimes in discrete calculations that have very many data. After the polynomial approximation is found, it may be necessary to calculate its value at several general points of the range $a \leqslant x \leqslant b$ .For each value of $\pmb { x } .$ ,the numbers $\{ \phi _ { j } ( x ) ; j = 0 , 1 , \ldots , n \}$ are obtained in sequence from the three-term recurrence relation, and then $p ^ { * } ( x )$ is determined by the equation

$$
p ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } ( x ) .
$$

# 11 Exercises

11.1 Let $\mathscr { A }$ be a finite-dimensional linear subspace of a Hilbert space $\mathcal { B }$ ,and,for any $f$ in ${ \mathcal { B } } _ { : }$ let $X ( f )$ be the best approximation in $\pmb { \mathcal { A } }$ to $f ,$ with respect to the 2-norm that is induced by the scalar product. Prove that $\pmb { X }$ is a linear operator, that it is a projection, and that $\| X \| _ { 2 } = 1$ .

11.2 Let $f \in \mathcal { C } [ - 5 , 5 ]$ ，and let $\mathscr { A }$ be the linear space of dimension seven that contains all even polynomials in $\mathcal { P } _ { 1 2 }$ . Show that there are many elements of $\mathscr { A }$ that minimize the expression

$$
\sum _ { j = - 5 } ^ { 5 } \big [ f ( j ) - p ( j ) \big ] ^ { 2 } , \qquad p \in \mathcal { A } ,
$$

but that there is only one optimal set of function values $\{ p ( j )$ ； $j = - 5 , - 4 , \dots , 5 \}$

11.3 Let $f$ be the function $\{ f ( x ) = x ^ { 2 } ; 0 \leqslant x \leqslant 1 \}$ , and let $\{ p ^ { * } ( x ) = c _ { 0 } ^ { * } +$ $c _ { 1 } ^ { * } x ; 0 \leqslant x \leqslant 1 \}$ be the linear polynomial that minimizes the integral

$$
\int _ { 0 } ^ { 1 } \left[ f ( x ) - p ( x ) \right] ^ { 2 } \mathrm { d } x , \qquad p \in \mathcal { P } _ { 1 } .
$$

Calculate the coefficients $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ from the normal equations (11.17),and verify that $p ^ { * }$ satisfies equation (11.14).

11.4 Suppose that one has to use a computer to calculate the coefficients $c _ { 0 }$ and $c _ { 1 }$ that minimize the sum of squares of residuals of the inconsistent linear equations

$$
\begin{array} { c } { ( 1 + \varepsilon ) c _ { 0 } + 2 c _ { 1 } = 5 + 2 \varepsilon } \\ { \ } \\ { 2 c _ { 0 } + ( 4 + \varepsilon ) c _ { 1 } = 1 0 - \varepsilon } \\ { \ } \\ { \varepsilon c _ { 0 } = 3 \varepsilon } \\ { \ } \\ { \varepsilon c _ { 1 } = \varepsilon . } \end{array}
$$

Suppose also that the constant $\pmb \varepsilon$ is so small that $\varepsilon ^ { 2 }$ is less than the relative accuracy of the computer arithmetic. Show that, if the normal equations are formed, then the matrix of the system can be exactly singular,but, if one makes the substitution $c _ { 0 } =$ $\bar { c } _ { 0 } - 2 c _ { 1 }$ in order to work with $\bar { c } _ { 0 }$ and $c _ { 1 }$ instead of with $c _ { 0 }$ and $c _ { 1 }$ ， then it is possible to achieve moderate accuracy.

11.5 Use the three-term recurrence relation of Theorem 11.3 to calculate the polynomials $\{ \phi _ { k } \in \mathcal { P } _ { k } ; k = 0 , 1 , 2 , 3 \}$ that are orthogonal on the point set $\{ 0 , 1 , 3 \}$ ，which means that they satisfy the conditions

$$
\phi _ { j } ( 0 ) \phi _ { k } ( 0 ) + \phi _ { j } ( 1 ) \phi _ { k } ( 1 ) + \phi _ { j } ( 3 ) \phi _ { k } ( 3 ) = 0 , \qquad j \neq k .
$$

You should find that the cubic polynomial $\phi _ { 3 }$ is zero on the point set $\{ 0 , 1 , 3 \}$

11.6 For any $f$ in $\mathcal { C } [ \alpha , b ]$ let $X ( f )$ be the linear polynomial that minimizes the expression

$$
\int _ { a } ^ { b } [ f ( x ) - p ( x ) ] ^ { 2 } { \mathrm { d } } x , \qquad p \in { \mathcal { P } } _ { 1 } .
$$

Prove that, if the $\infty$ -norm is used in $\mathcal { C } [ \alpha , b ]$ ,then the norm of the operator $X$ has the value $\| \boldsymbol { X } \| _ { \infty } = \frac { 5 } { 3 }$

11.7 For $i = 0 , 1 , 2 , 3$ ，let $\phi _ { i }$ be the function that is obtained by drawing straight lines between the function values $\{ \phi _ { i } ( j ) =$ $\delta _ { i j } ; j = 0 , 1 , 2 , 3 \}$ . Thus $\{ \phi _ { i } ; i = 0 , 1 , 2 , 3 \}$ is a basis of the space of linear splines that is called $\mathcal { S } ( 1 , 0 , 1 , 2 , 3 )$ in Section 3.4. Let $f$ be the piecewise constant function $\{ f ( x ) = 1$ ， $0 \leqslant x \leqslant 1$ ； $f ( x ) = 0$ ， $1 < x \leqslant 3 \}$ . Use the normal equations (11.17) to calculate the coefficients $\{ c _ { i } ^ { * } ; i = 0 , 1 , 2 , 3 \}$ that minimize the integral

$$
\int _ { 0 } ^ { 3 } \left[ f ( x ) - \sum _ { i = 0 } ^ { 3 } c _ { i } ^ { * } \phi _ { i } ( x ) \right] ^ { 2 } \mathrm { d } x .
$$

Plot the function $\{ \sum c _ { i } ^ { * } \phi _ { i } ( x ) ; 0 \leqslant x \leqslant 3 \}$

11.8 Let $f$ be the function $\{ f ( x ) = 2 x - 1 ; 0 \leqslant x \leqslant 1 \}$ . Find the smallest value of $_ n$ such that a function of the form

$$
p ( x ) = \sum _ { k = 0 } ^ { n } c _ { k } \cos { ( k \pi x ) } , \qquad 0 \leqslant x \leqslant 1 ,
$$

satisfies the condition

$$
\int _ { 0 } ^ { 1 } [ f ( x ) - p ( x ) ] ^ { 2 } ~ \mathrm { d } x < 1 0 ^ { - 4 } .
$$

11.9 Given the values $T _ { 0 } ( x )$ and $T _ { 1 } ( x )$ of the first two Chebyshev polynomials, the recurrence relation

$$
T _ { k + 1 } ( x ) = 2 x T _ { k } ( x ) - T _ { k - 1 } ( x ) , \qquad k = 1 , 2 , 3 , \ldots ,
$$

is applied to calculate $T _ { n } ( x )$ where $_ n$ is large.Show that,if $T _ { 0 } ( x )$ and $T _ { 1 } ( x )$ are exact, but if every arithmetic operation can cause an absolute error of $\pm \eta$ ,then the error in $T _ { n } ( x )$ when $x = 1$ is at most $\scriptstyle { \frac { 3 } { 2 } } \eta n ( n - 1 )$ . Investigate whether larger errors can occur for any other value of $x$ in the interval $[ - 1 , 1 ]$

11.10 Let $\mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 2 }$ be finite-dimensional linear subspaces of a Hilbert space $\mathcal { B }$ ，and let $X _ { 1 }$ and $X _ { 2 }$ be the linear projection operators from $\mathcal { B }$ to $\mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 2 }$ respectively, that give the best approximations in these spaces with respect to the norm of the Hilbert space. For any $f _ { 1 }$ in $\mathcal { B }$ ，let the sequence $\{ f _ { k }$ ； $k = 1 , 2 , 3 , \ldots \}$ be defined by the equation $\{ f _ { k + 1 } = X _ { 2 } ( X _ { 1 } f _ { k } ) ; k =$ $1 , 2 , 3 , \ldots \}$ . Prove that the sequence converges to the best approximation to $f _ { 1 }$ in the intersection of the spaces $\mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 2 }$

# 12

# Properties of orthogonal polynomials

# 12.1 Elementary properties

Orthogonal polynomials have several uses in addition to the method of calculating least squares approximations that has just been described.For example, we find in Section 12.2 that they are important to the construction of some efficient formulae for the numerical calculation of integrals. First, however, some of their elementary properties are established.Unless it is stated otherwise,it is assumed that each orthogonal polynomial is defined on the range $a \leqslant x \leqslant b$ .However,by taking the point of view that is mentioned at the beginning of Section 11.4, it follows that some of the results of this chapter are also valid in the case when the range of $x$ is a set of discrete points.

# Theorem 12.1

Let $\mathcal { B }$ be a Hilbert space that contains the subspace $\mathcal { P } _ { n }$ of algebraic polynomials of degree $\pmb { n }$ .Let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a sequence of non-zero polynomials,where each $\phi _ { i }$ is in $\mathcal { P } _ { i } ,$ and where the orthogonality conditions

$$
( \phi _ { i } , \phi _ { j } ) = 0 , \qquad i \neq j ,
$$

hold (Theorem 11.3 shows that these conditions can be satisfied). Then the functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ are linearly independent. Moreover, if $\psi _ { k }$ is any polynomial in $\mathcal { P } _ { k }$ that is orthogonal to the elements of $\mathcal { P } _ { k - 1 }$ ， where $k$ is any integer from $[ 1 , n ]$ ,then the equation

$$
\psi _ { k } ( x ) = c \phi _ { k } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is obtained for some constant $^ { c }$

Proof. To prove the first part of the theorem, we have to show that, if the scalars $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy the equation

$$
\sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } = 0 ,
$$

where O is the zero function, then they are all equal to zero. Because expression (12.3) implies the equations

$$
\sum _ { i = 0 } ^ { n } \lambda _ { i } ( \phi _ { j } , \phi _ { i } ) = 0 , \qquad j = 0 , 1 , \ldots , n ,
$$

and because $( \phi _ { j } , \phi _ { j } )$ is positive if $\phi _ { j }$ is a non-zero function, it follows from the orthogonality conditions (12.1） that the coefficients $\begin{array} { r l } { \{ \lambda _ { j } ; ~ j = } \end{array}$ $0 , 1 , \ldots , n \}$ are zero,which is the first required result.

This result is useful to the second part of the theorem, because it shows that the functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , k \}$ are a basis of $\mathcal { P } _ { k }$ . Therefore we may express $\psi _ { k }$ in the form

$$
\psi _ { k } = \sum _ { i = 0 } ^ { k } \mu _ { i } \phi _ { i } ,
$$

which gives the equations

$$
( \phi _ { j } , \psi _ { k } ) = \sum _ { i = 0 } ^ { k } \mu _ { i } ( \phi _ { j } , \phi _ { i } ) , \qquad j = 0 , 1 , \ldots , k - 1 .
$$

Hence condition (12.1) and the orthogonality properties of $\psi _ { k }$ imply that the parameters $\{ \mu _ { j } ; j = 0 , 1 , \ldots , k - 1 \}$ are zero. It follows from expression (12.5) that equation (12.2) is satisfied, where $^ c$ is equal to $\pmb { \mu _ { k } }$ □

Another elementary property of orthogonal polynomials, that is required in the next section, is as follows.

# Theorem 12.2

Let. $\phi _ { k }$ be a non-zero polynomial that is in $\mathcal { P } _ { k } ,$ ，and that is orthogonal to the elements of $\mathcal { P } _ { k - 1 }$ . Then $\phi _ { k }$ has exactly $k$ real and distinct zeros in the open interval $a < x < b$

Proof. Let $r$ be the number of sign changes of the function $\{ \phi _ { k } ( x )$ ； $a \leqslant x \leqslant b \}$ . There is a non-zero polynomial in $\mathcal { P } _ { r } , \psi _ { r }$ say,such that the inequality

$$
\phi _ { k } ( x ) \psi _ { r } ( x ) \geqslant 0 , \qquad a \leqslant x \leqslant b ,
$$

holds, the product $\phi _ { k } ( x ) \psi _ { r } ( x )$ being zero if and only if $\pmb { x }$ is a zero of $\phi _ { k }$ .It follows from the definition (11.2) of the scalar product that $\left( \phi _ { k } , \psi _ { r } \right)$ is positive. Therefore, because of the orthogonality properties of $\phi _ { k } , r$ is not less than $k$ .Hence $\phi _ { k }$ has at least $k$ distinct zeros in the open interval $a < x < b$ .The number of zeros cannot exceed $k$ because $\phi _ { k }$ is a non-zero element of $\mathcal { P } _ { k }$ .Therefore the theorem is true.□

The extension of this result to the discrete case is not difficult, but it is different from the other extensions that have been made in a fundamental way. In all other theorems it does not matter if the approximating function is known only on the set $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ ，where the scalar product has the value (11.6),but now we use the fact that polynomials are defined for all values of the variable $x$ .In the statement of the discrete version of Theorem 12.2 we require $k < m$ ，and we let $[ a , b ]$ be any interval that contains the points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ . The proof of the theorem is unchanged,and $\psi _ { r }$ is still constructed so that inequality (12.7) holds for all $x$ in $[ a , b ]$ . It follows that the $k$ real roots of the polynomial $\phi _ { k }$ are usually not in the point set $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ ,but they are in the shortest interval that contains the data points.

Theorem 12.1 shows that all functions $\phi _ { k }$ that satisfy the conditions of Theorem 12.2 are the same,except for a scaling factor. Therefore, the roots of $\phi _ { k }$ depend only on the integer $k$ and the definition of the scalar product.

# 12.2 Gaussian quadrature

Many formulae for approximating definite integrals have the form

$$
\int _ { a } ^ { b } w ( x ) f ( x ) \mathrm { d } x \approx \sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } ) ,
$$

where $\{ w ( x ) ; a \leqslant x \leqslant b \}$ is a fixed positive weight function, where $f$ is in $\mathcal { C } [ \alpha , b ] .$ ,where $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ is a set of real coefficients,and where the abscissae are in ascending order

$$
a \leqslant x _ { 0 } < x _ { 1 } < . ~ . ~ . < x _ { k } \leqslant b .
$$

Hence the integral is estimated from $( k + 1 )$ point evaluations of $f .$ One of the most useful methods for choosing the parameters $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ and $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ is to force the condition that equation (12.8) is exact when $f$ is in a suitable linear subspace $\mathscr { A }$ of ${ \mathcal { C } } [ a , b ]$

For example, if the points $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ are given, then we may obtain the coeffcients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ by letting $\mathscr { A }$ be the space $\mathcal { P } _ { k }$ · We recall from Chapter 4 that, when $f$ is in $\mathcal { P } _ { k }$ , it can be expressed in the form

$$
f ( x ) = \sum _ { i = 0 } ^ { k } l _ { i } ( x ) f ( x _ { i } ) , \qquad a \leqslant x \leqslant b ,
$$

where $\{ l _ { i } ( x ) ; a \leqslant x \leqslant b \}$ is the cardinal function (4.3). It follows from the properties of cardinal functions that the two sides of expression (12.8) are equal when $c _ { i }$ has the value

$$
c _ { i } = \int _ { a } ^ { b } w ( x ) l _ { i } ( x ) \mathrm { d } x , \qquad i = 0 , 1 , \dots , k .
$$

Any other choice of $c _ { i }$ causes an error in the approximation (12.8) when $f$ is the cardinal polynomial $\{ l _ { i } ( x ) ; a \leqslant x \leqslant b \}$

Gaussian quadrature formulae extend this idea, for their parameter values $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ and $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ are such that the approximation (12.8) is exact when $f$ is in $\mathscr { P } _ { 2 k + 1 }$ . The abscissae $\{ x _ { i } ; i =$ $0 , 1 , \ldots , k \}$ may be calculated by satisfying a system of non-linear equations,but the purpose of this section is to show that they are the zeros of an orthogonal polynomial.

# Theorem 12.3

Let the points $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ in the quadrature formula (12.8) be the zeros of a polynomial $\phi _ { k + 1 }$ of degree $( k + 1 )$ that satisfies the orthogonality conditions

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k + 1 } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { P } _ { k } ,
$$

where $\{ w ( x ) ; a \leqslant x \leqslant b \}$ is any integrable function. Let the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ have the values (12.11), where $l _ { i }$ is defined by equation (4.3). Then the approximation (12.8) is exact when $f$ is any polynomial in $\mathscr { P } _ { 2 k + 1 }$

Proof. If $f$ is in $\mathscr { P } _ { 2 k + 1 }$ , it may be expressed in the form

$$
f ( x ) = p ( x ) \phi _ { k + 1 } ( x ) + q ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $\phi _ { k + 1 }$ is given in the statement of the theorem,and where $p$ and $q$ are in $\mathcal { P } _ { k }$ . Because $\phi _ { k + 1 }$ is orthogonal to $p$ ,we have the equation

$$
\int _ { a } ^ { b } w ( x ) f ( x ) \mathrm { d } x = \int _ { a } ^ { b } w ( x ) q ( x ) \mathrm { d } x .
$$

Because the abscissae $\left\{ x _ { i } ; i = 0 , 1 , \ldots , k \right\}$ are zeros of $\phi _ { k + 1 }$ , the identity

$$
\sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } ) = \sum _ { i = 0 } ^ { k } c _ { i } q ( x _ { i } )
$$

is satisfed.Because $\pmb q$ isin $\mathcal { P } _ { k }$ ，it follows from the definition of the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ that the right-hand sides of expressions (12.14) and (12.15) are equal. Therefore the left-hand sides are equal, which is the required result.□

When formula (12.8) is applied,it is usual for some errors to be present in the function values {f(xi); i = O,1,...,k}, due, for example,to the rounding errors of computer arithmetic. It is therefore advantageous if the sum

$$
\| c \| _ { 1 } = \sum _ { i = 0 } ^ { k } { \big | } c _ { i } { \big | }
$$

is small. However,in order that equation (12.8) is exact when $f$ is a constant function,it is necessary to satisfy the equation

$$
\int _ { a } ^ { b } w ( x ) \mathop { } \mathrm { d } x = \sum _ { i = 0 } ^ { k } c _ { i } .
$$

Therefore expression (12.16） is least if and only if the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ all have the same sign. Our next theorem shows that Gaussian quadrature formulae give this useful property.

# Theorem 12.4

If the approximation (12.8) is exact for allfunctions $f$ in $\mathscr { P } _ { 2 k + 1 }$ ， and if $w$ is positive, then each of the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ is positive.

Proof. If we let $f$ be the polynomial

$$
f ( x ) = [ l _ { i } ( x ) ] ^ { 2 } , \qquad a \leqslant x \leqslant b ,
$$

where $l _ { i }$ is the cardinal function (4.3),then the left-hand side of expression (12.8) is positive,and the right-hand side is equal to $c _ { i } .$ Because $f$ is in $\mathscr { P } _ { 2 k + 1 }$ , it follows that $c _ { i }$ is positive.□

Gaussian quadrature formulae are not very convenient for adaptive numerical integration procedures, where the user specifies the accuracy that he requires in the calculated estimate of his integral. In these procedures the error of each approximation to the integral is estimated automatically,and the method of integration is refined until it seems that the required accuracy is achieved.In Gaussian quadrature formulae the positions of the abscissae $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ make it difficult to use previously calculated values of the integrand after each refinement process. Despite this disadvantage, Gaussan methods are found in many automatic integration algorithms.Moreover, if the integrand takes so long to calculate that one has to manage with not more than about four terms in the sum (12.8), then frequently a Gaussian formula is the best one to apply. Thus there is another reason for continuing the study of orthogonal polynomials.

# 12.3 The characterization of orthogonal polynomials

The recurrence relation of Theorem 11.3 is not always the most convenient method for calculating orthogonal polynomials. Some other highly useful techniques come from the following characterization theorem.

# Theorem 12.5

Let $\{ w ( x ) ; a \leqslant x \leqslant b \}$ be any continuous function. The function $\phi _ { k + 1 }$ in $\mathcal { C } [ a , b ]$ satisfies the orthogonality conditions

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k + 1 } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { P } _ { k } ,
$$

if and only if there exists a $( k + 1 )$ - times differentiable function $\{ u ( x ) ; a \leqslant$ $x \leqslant b \}$ that satisfies the equations

$$
w ( x ) \phi _ { k + 1 } ( x ) = u ^ { ( k + 1 ) } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

and

$$
u ^ { ( i ) } ( a ) = u ^ { ( i ) } ( b ) = 0 , \qquad i = 0 , 1 , \ldots , k .
$$

Proof. If equations (12.20) and (12.21) hold, then integration by parts gives the identity

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k + 1 } ( x ) p ( x ) \mathrm { d } x = ( - 1 ) ^ { k + 1 } \int _ { a } ^ { b } u ( x ) p ^ { ( k + 1 ) } ( x ) \mathrm { d } x .
$$

Therefore, because of the term $p ^ { ( k + 1 ) } ( x )$ ,the orthogonalitycondition (12.19) is obtained when $p$ is in $\mathcal { P } _ { k }$

Conversely,when equation (12.19) is satisfied, we let $\pmb { u }$ be defined by expression (12.20), where the constants of integration are chosen to give the values

$$
u ^ { ( i ) } ( a ) = 0 , \qquad i = 0 , 1 , \ldots , k .
$$

Expression (12.20) is substituted in the integral (12.19).For each integer j in $[ 0 , k ] ,$ we let ${ \pmb p } = { \pmb p } _ { j }$ be the polynomial

$$
p _ { j } ( x ) = ( b - x ) ^ { j } , \qquad a \leqslant x \leqslant b ,
$$

and we apply integration by parts $( j + 1 )$ times to the left-hand side of expression (12.19). Thus we obtain the equation

$$
\begin{array} { l } { { [ ( - 1 ) ^ { j } u ^ { ( k - j ) } ( x ) p _ { j } ^ { ( j ) } ( x ) ] _ { a } ^ { b } } } \\ { { \displaystyle \quad + ( - 1 ) ^ { j + 1 } \int _ { a } ^ { b } u ^ { ( k - j ) } ( x ) p _ { j } ^ { ( j + 1 ) } ( x ) \mathrm { d } x = 0 . } } \end{array}
$$

Because $p _ { j } ^ { ( j + 1 ) }$ is zero,i follows that ${ \pmb u } ^ { ( k - j ) } ( { \pmb b } )$ is zero for $j = 0 , 1 , \ldots , k ,$ which completes the proof of the theorem.□

In order to apply this theorem to generate orthogonal polynomials, it is necessary to identify a function $\pmb { u }$ ,satisfying the conditions(12.21),such that the function $\phi _ { k + 1 }$ ,defined by equation (12.2O), is a polynomial of degree $( k + 1 )$ . There is no automatic method of identification,but in many important cases the required function $\pmb { u }$ is easy to recognize. For example, if we satisfy the equations (12.21) by leting $\pmb { u }$ be the function

$$
u ( x ) = ( x - a ) ^ { k + 1 } ( x - b ) ^ { k + 1 } , \qquad a \leqslant x \leqslant b ,
$$

then it follows that $\phi _ { k + 1 }$ is in $\mathcal { P } _ { k + 1 }$ when the weight function w is constant. In other words the polynomials

$$
\phi _ { j } ( x ) = \frac { d ^ { j } } { d x ^ { j } } [ ( x - a ) ^ { j } ( x - b ) ^ { j } ] , \qquad j = 0 , 1 , 2 , \ldots ,
$$

satisfy the orthogonality conditions

$$
\int _ { a } ^ { b } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x = 0 , \qquad i \neq j .
$$

Many of the families of orthogonal polynomials that have been given special names can be obtained from Theorem 12.5.Each family is characterized by a weight function $\{ w ( x ) ; a \leqslant x \leqslant b \}$ . For example, if $\pmb { \alpha }$ and $\beta$ are real constants that are both greater than minus one, then the polynomials $\{ \phi _ { j } ; j = 0 , 1 , 2 , \ldots \}$ that satisfy the orthogonality conditions

$$
\int _ { - 1 } ^ { 1 } { ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x } = 0 , \qquad i \neq j ,
$$

are called Jacobi polynomials.In this case we require the function (12.20) to be a polynomial of degree $( k + 1 )$ multiplied by the weight function $\{ ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } ; - 1 \leqslant x \leqslant 1 \}$ . Therefore we let $\pmb { u }$ be the function

$$
u ( x ) = ( 1 - x ) ^ { \alpha + k + 1 } ( 1 + x ) ^ { \beta + k + 1 } , \qquad - 1 \leqslant x \leqslant 1 .
$$

Because condition (12.21） is satisfied, it follows that the Jacobi polynomials are defined by the equation

$$
\begin{array} { r } { \phi _ { j } ( x ) = ( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } \displaystyle \frac { \mathrm { d } ^ { j } } { \mathrm { d } x ^ { j } } \left[ ( 1 - x ) ^ { \alpha + j } ( 1 + x ) ^ { \beta + j } \right] , } \\ { j = 0 , 1 , 2 , \ldots , } \end{array}
$$

which is called Rodrigue's formula.

In the special case when the range of $x$ is[-1,1] and when $\alpha = \beta = 0$ ， the Jacobi polynomials are called the Legendre polynomials. If instead, for this range of $x _ { i }$ we let $\alpha = \beta = - \frac { 1 } { 2 }$ ，then we obtain the Chebyshev polynomials, that we met for the first time in Chapter 4.Further attention is given to the Chebyshev polynomials in the next section, because they provide least squares approximation operators that are important to the work of Chapter 17.

We may allow the range of $\pmb { x }$ to be infinite in Theorem 12.5, provided that the integral (12.19) is well defined. For example,because it is necessary sometimes to integrate functions that decay exponentially, there is a need for Gaussian quadrature formulae of the type

$$
\int _ { 0 } ^ { \infty } \mathrm { e } ^ { - x } f ( x ) \mathrm { d } x \approx \sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } ) .
$$

Therefore, in order to make use of Theorem 12.3,we seek polynomials $\{ \phi _ { j } \in \mathcal { P } _ { i } ; j = 0 , 1 , 2 , . . . \}$ that satisfy the conditions

$$
\int _ { 0 } ^ { \infty } \mathrm { e } ^ { - x } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x = 0 , \qquad i \ne j ,
$$

which are called Laguerre polynomials. If $\pmb { u }$ is the function

$$
u \left( x \right) = \mathrm { e } ^ { - x } x ^ { k + 1 } , \qquad 0 \leqslant x < \infty ,
$$

in Theorem 12.5, then the conditions (12.21） are obtained,and the function $\phi _ { k + 1 }$ ，defined by equation (12.20)，is in $\mathcal { P } _ { k + 1 }$ .Hence the Laguerre polynomials have the values

$$
\phi _ { j } ( x ) = \mathtt { e } ^ { x } { \frac { \mathrm { d } ^ { j } } { \mathrm { d } x ^ { j } } } ( \mathtt { e } ^ { - x } x ^ { j } ) , \qquad j = 0 , 1 , 2 , \ldots . . . .
$$

Similarly, the Hermite polynomials

$$
\phi _ { j } ( x ) = { \bf e } ^ { x ^ { 2 } } { \frac { { \bf d } ^ { j } } { { \bf d } x ^ { j } } } ( { \bf e } ^ { - x ^ { 2 } } ) , \qquad j = 0 , 1 , 2 , \ldots ,
$$

obey the orthogonality conditions

$$
\int _ { - \infty } ^ { \infty } \mathbf { e } ^ { - x ^ { 2 } } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x = 0 , \qquad i \neq j .
$$

It is possible to deduce from each of the expressions (12.31), (12.35) and (12.36) that each family of orthogonal polynomials satisfies a three term recurrence relation. Thus,in these three cases, algebraic expressions can be found for the coefficients $\{ \alpha _ { j } ; ~ j = 0 , 1 , 2 , \ldots \}$ and $\{ \beta _ { j } ; j =$ $1 , 2 , 3 , \ldots \}$ that occur in Theorem 11.3.

# 12.4 The operator $\pmb { R _ { n } }$

The operator $\scriptstyle { R _ { n } }$ is a linear projection from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ .For each $f$ in $\mathcal { C } [ - 1 , 1 ] , R _ { n } f$ is defined to be the element of ${ \mathcal { P } } _ { n }$ that minimizes the expression

$$
\int _ { - 1 } ^ { 1 } { ( 1 - x ^ { 2 } ) ^ { - \frac { 1 } { 2 } } [ f ( x ) - p ( x ) ] ^ { 2 } \mathrm { d } x } , \qquad p \in \mathscr { P } _ { n } .
$$

Therefore Theorem 11.2 shows that $\scriptstyle R _ { n } f$ is the function

$$
R _ { n } f = \sum _ { j = 0 } ^ { n } { \frac { ( \phi _ { j } , f ) } { \| \phi _ { j } \| ^ { 2 } } } \phi _ { j } ,
$$

where the scalar product has the value

$$
( \phi _ { j } , f ) = \int _ { - 1 } ^ { 1 } \big ( 1 - x ^ { 2 } \big ) ^ { - \frac { 1 } { 2 } } \phi _ { j } ( x ) f ( x ) \ : \mathrm { d } x ,
$$

provided that the polynomials $\left\{ \phi _ { j } \in \mathcal { P } _ { j } ; j = 0 , 1 , \ldots , n \right\}$ are mutually orthogonal. Three properties of $\scriptstyle { R _ { n } }$ that are proved later are that its norm is quite small, it is closely related to Fourier approximation, and, if $f$ is in $\mathcal { P } _ { n + 1 }$ ，then $\scriptstyle R _ { n } f$ is the best minimax approximation from $\mathcal { P } _ { n }$ to $f .$ The calculation of $\scriptstyle { R _ { n } f }$ is helped by the fact that the functions $\{ \phi _ { j } ; j =$ $0 , 1 , \ldots , n \}$ in equation (12.39) are Chebyshev polynomials,which is established in the next theorem.

# Theorem 12.6

The Chebyshev polynomials

$$
T _ { j } ( x ) = \cos { ( j \theta ) } , \qquad x = \cos { \theta } ,
$$

satisfy the orthogonality conditions

$$
\int _ { - 1 } ^ { 1 } { ( 1 - x ^ { 2 } ) ^ { - { \frac { 1 } { 2 } } } T _ { j } ( x ) T _ { k } ( x ) } \mathrm { d } x = 0 , \qquad j \neq k .
$$

Prcof. By letting $\scriptstyle { \pmb { x } } = \cos { \pmb { \theta } }$ in the integral (12.42),it follows that the integral has the value

$$
{ \begin{array} { r l } & { { \displaystyle \int _ { 0 } ^ { \pi } \cos \left( j \theta \right) \cos \left( k \theta \right) \mathrm { d } \theta } } \\ & { \quad = { \frac { 1 } { 2 } } \displaystyle \int _ { 0 } ^ { \pi } \left\{ \cos \left[ ( j + k ) \theta \right] + \cos \left[ ( j - k ) \theta \right] \right\} \mathrm { d } \theta } \\ & { \quad = 0 , \quad \quad j \neq k , } \end{array} }
$$

which is the required result.□

It is now straightforward to deduce that $\scriptstyle R _ { n } f$ is the best minimax approximation from $\mathcal { P } _ { n }$ to $f$ when $f$ is a polynomial of degree $( n + 1 )$ .In this case the error function $\left( f - R _ { n } f \right)$ is in $\mathscr { P } _ { n + 1 }$ and, by Theorem 11.1, it is orthogonal to all elements of $\mathcal { P } _ { n }$ .Hence,by Theorem 12.1,it is a multiple of a polynomial that is independent of $f .$ Theorem 12.6 shows that we may let this fixed polynomial be $T _ { n + 1 }$ . Therefore the approximation $\scriptstyle { R _ { n } f }$ satisfies the characterization condition, given in Theorem 7.2,for the best minimax approximation from $\mathcal { P } _ { n }$ to $f .$

When we claimed that the norm of the operator $\scriptstyle { R _ { n } }$ is quite small, we did not have in mind the operator norm that is induced by the definition

$$
\left\| f \right\| = ( f , f ) ^ { \frac 1 2 } , \qquad f \in \mathcal { C } [ - 1 , 1 ] ,
$$

where the scalar product has the value (12.4O). This case is rather uninteresting, because equation (11.14) and the fact that $\scriptstyle { R _ { n } }$ is a projection imply that $\left\| R _ { n } \right\|$ is one. Instead, the following theorem gives the value of $\left\| R _ { n } \right\|$ that is induced by the maximum norm

$$
\| f \| _ { \infty } = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | f ( x ) | , \qquad f \in { \mathcal { C } } [ - 1 , 1 ] .
$$

# Theorem 12.7

The norm of the operator $\scriptstyle { R _ { n } }$ has the value

$$
\begin{array} { l } { \displaystyle \| R _ { n } \| _ { \infty } = \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } \left| \frac { \sin { \big [ ( n + \frac { 1 } { 2 } ) \theta \big ] } } { \sin { ( \frac { 1 } { 2 } \theta ) } } \right| \mathrm { d } \theta } \\ { \displaystyle \quad = \frac { 1 } { 2 n + 1 } + \frac { 2 } { \pi } \sum _ { j = 1 } ^ { n } \frac { 1 } { j } \tan { \left( \frac { j \pi } { 2 n + 1 } \right) } , } \end{array}
$$

with respect to the $\infty$ -norm (12.45).

Proof. Not all of the steps of the proof are given explicitly, because the details are rather tedious.First we let the functions $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ in the definition (12.39) be the Chebyshev polynomials $\{ T _ { j } ; j = 0 , 1 , \dots , n \}$ We make the change of variable $\scriptstyle { \pmb { x } } = \cos { \pmb { \theta } }$ in the integrals that occur, and we calculate the denominators of expression (12.39) analytically. Thus, for all values of $t$ in $[ 0 , \pi ] ,$ . we obtain the equation

$$
\begin{array} { r } { ( R _ { n } f ) ( \cos t ) = \displaystyle \frac { 2 } { \pi } \sum _ { j = 0 } ^ { n } \int _ { \theta = 0 } ^ { \pi } \cos \big ( j \theta \big ) f ( \cos \theta ) \mathrm { d } \theta \cos ( j t ) } \\ { = \displaystyle \frac { 2 } { \pi } \int _ { \theta = 0 } ^ { \pi } f ( \cos \theta ) \sum _ { j = 0 } ^ { n } \cos \big ( j \theta \big ) \cos \big ( j t \big ) \mathrm { d } \theta , } \end{array}
$$

where the prime on the summation sign indicates that the first term is halved. The required value of $\| R _ { n } \|$ is the least upper bound on expression (12.47） subject to the conditions $0 \leqslant t \leqslant \pi$ and $\| f \| _ { \infty } \leqslant 1$ By taking the supremum over $f ,$ we deduce the value

$$
\left\| R _ { n } \right\| = \operatorname* { m a x } _ { t } \frac { 2 } { \pi } \int _ { \theta = 0 } ^ { \pi } \bigg | \sum _ { j = 0 } ^ { n } \cos \left( j \theta \right) \cos \left( j t \right) \bigg | \ \mathrm { d } \theta .
$$

We express the product cos $( j \pmb \theta )$ cos $\left( j t \right)$ in terms of cos $[ j ( \pmb \theta + t ) ]$ and

cos $[ j ( \pmb \theta - \pmb t ) ] ,$ , and we extend the range of integration. Hence we obtain the bound

$$
\begin{array} { l } { \displaystyle \| R _ { n } \| \leqslant \operatorname* { m a x } _ { t } \frac { 1 } { 2 \pi } \int _ { \theta = - \pi } ^ { \pi } \left\{ \left| \sum _ { j = 0 } ^ { n } \cos \left[ j ( \theta + t ) \right] \right| \right. } \\ { \displaystyle \left. + \left| \sum _ { j = 0 } ^ { n } \cos \left[ j ( \theta - t ) \right] \right| \right\} \mathrm { d } \theta . } \end{array}
$$

By periodicity the right-hand side of this inequality is independent of $t .$ Therefore, because expressions (12.48) and (12.49) are equal when $\pmb { t = 0 }$ ， we have the identity

$$
\left\| R _ { n } \right\| = \frac { 2 } { \pi } \int _ { \theta = 0 } ^ { \pi } \left| \sum _ { j = 0 } ^ { n } \cos \left( j \theta \right) \right| \mathrm { d } \theta .
$$

The first part of expression (12.46) now follows from the elementary equation

$$
\sum _ { j = 0 } ^ { n } \cos { ( j \theta ) } = \textstyle { \frac { 1 } { 2 } } \sin { [ ( n + \textstyle { \frac { 1 } { 2 } } ) \theta ] } / \sin { ( \textstyle { \frac { 1 } { 2 } } \theta ) } .
$$

We see that this result implies that the zeros of the integrand (2.50) occur when $\pmb \theta$ has the values

$$
\theta _ { k } = k \pi / ( n + \textstyle { \frac { 1 } { 2 } } ) , \qquad k = 0 , 1 , \ldots , n .
$$

We let $\theta _ { n + 1 } = \pi ;$ , in order to obtain from equation (12.50) the expression

$$
\left\| R _ { n } \right\| = { \frac { 2 } { \pi } } \sum _ { k = 0 } ^ { n } \left( - 1 \right) ^ { k } \int _ { \theta _ { k } } ^ { \theta _ { k + 1 } } \sum _ { j = 0 } ^ { n } \cos \left( j \theta \right) \mathbf { d } \theta .
$$

Thus, by analytic integration, by exchanging the orders of summation, and by giving special attention to the contribution from $j = 0$ , the equation

$$
\begin{array} { r l r } & { } & { \left\| { \cal R } _ { n } \right\| = \displaystyle \frac { 1 } { 2 n + 1 } + \sum _ { j = 1 } ^ { n } \frac { 2 } { j \pi } \sum _ { k = 0 } ^ { n } \left( - 1 \right) ^ { k } \left[ \sin \left( j \theta \right) \right] _ { \theta _ { k } } ^ { \theta _ { k + 1 } } } \\ & { } & { = \displaystyle \frac { 1 } { 2 n + 1 } + \sum _ { j = 1 } ^ { n } \frac { 4 } { j \pi } \sum _ { k = 1 } ^ { n } \left( - 1 \right) ^ { k + 1 } \sin \left( \frac { j k \pi } { n + \frac { 1 } { 2 } } \right) } \end{array}
$$

is satisfied. By expressing the sine terms of this equation as imaginary parts of exponential functions, one can deduce the identity

$$
\sum _ { k = 1 } ^ { n } { \bigl ( } - 1 { \bigr ) } ^ { k + 1 } \sin { \biggl ( } { \frac { j k \pi } { n + { \frac { 1 } { 2 } } } } { \biggr ) } = { \frac { 1 } { 2 } } \tan { \biggl ( } { \frac { j \pi } { 2 n + 1 } } { \biggr ) } .
$$

Therefore the last line of expression (12.46) is implied by equation (12.54).□

Some values of $\| R _ { n } \|$ were calculated from equation (12.46). They are given in Table 12.1.They are so similar to the norms that are listed in the last column of Table 4.5, that the norms do not provide a good reason for preferring the operator $\scriptstyle { R _ { n } }$ to an interpolation method for calculating a polynomial approximation to a function $f .$ The main reason for our interest in the values of $\| R _ { n } \|$ is given in Chapter 17.

# 12 Exercises

12.1 Let $\{ \phi _ { j } \in \mathcal { P } _ { j } ; j = 0 , 1 , 2 , . . . \}$ be a sequence of orthogonal polynomials,and let $\{ \xi _ { j k } ; \ k = 1 , 2 , \ldots , j \}$ be the zeros of $\phi _ { j } .$ By considering equation (11.43） when $\{ x = \xi _ { j k }$ ； $k = 1 , 2 , \ldots , j \} _ { }$ ， prove by induction that, for all positive integers $j ,$ there is a zero of $\phi _ { j }$ in each of the intervals $\{ ( \pmb { \xi } _ { j + 1 } \pmb { \mathrm { \varepsilon } } _ { k } , \pmb { \xi } _ { j + 1 } \pmb { \mathrm { \varepsilon } } _ { k + 1 } )$ ； $k = 1 , 2 , \ldots , j \}$ ·

12.2 Calculate the coefficients $\boldsymbol { w } _ { 0 } , \boldsymbol { w } _ { 1 } , \boldsymbol { x } _ { 0 }$ and $\pmb { x } _ { 1 }$ that make the approximation

$$
\int _ { 0 } ^ { 1 } x f ( x ) \mathrm { d } x \approx w _ { 0 } f ( x _ { 0 } ) + w _ { 1 } f ( x _ { 1 } )
$$

exact when $f$ is any cubic polynomial. Verify your solution by letting $f$ be a general cubic polynomial.

12.3 Let $f$ be a function in $\mathcal { C } ^ { ( 2 k + 2 ) } [ a , b ] ,$ , and let the approximation (12.8) be a Gaussian quadrature formula.Therefore the error of the approximation is unchanged if a polynomial $\pmb { p }$ of degree $( 2 k + 1 )$ is subtracted from $f .$ By letting $\pmb { p }$ be the function in $\mathscr { P } _ { 2 k + 1 }$ that satisfies the conditions $\{ p ( x _ { i } ) = f ( x _ { i } )$ ； $i = 0 , 1 , \ldots , k \}$ and $\{ p ^ { \prime } ( x _ { i } ) = f ^ { \prime } ( x _ { i } )$ ； $i = 0 , 1 , \ldots , k \}$ ，and by using an extension of Theorem 4.2, prove that the error has the value

$$
\int _ { a } ^ { b } w ( x ) \prod _ { j = 0 } ^ { k } \left( x - x _ { j } \right) ^ { 2 } \mathrm { d } x f ^ { ( 2 k + 2 ) } ( \xi ) / ( 2 k + 2 ) ! ,
$$

where $\pmb { \xi }$ is a point of $[ a , b ]$

12.4 Use equation (12.36) to generate the first six Hermite polynomials,and verify that they satisfy a three-term recurrence relation of the form that is given in Theorem 11.3.

Table 12.1. Some values of $\| R _ { n } \|$   

<table><tr><td>R.l n</td><td></td><td>n Rl</td></tr><tr><td>2</td><td>1.6422</td><td>12 2.2940</td></tr><tr><td>4</td><td>1.8801</td><td>14 2.3542</td></tr><tr><td>6</td><td>2.0290</td><td>16 2.4065</td></tr><tr><td>8</td><td>2.1377</td><td>18 2.4529</td></tr><tr><td>10</td><td>2.2234</td><td>20 2.4945</td></tr></table>

12.5 Let $\bar { p }$ be a function in $\mathcal { P } _ { k }$ ,and let $\pmb { n }$ be an integer in the range $[ 0 , k - 1 ]$ . Let the telescoping procedure of Section 8.4 be applied $( k - n )$ times to derive from $\bar { p }$ a polynomial $\pmb { p }$ in ${ \mathcal P _ { n } }$ . Prove that $p$ is the function $\pmb { R _ { n } } \bar { p }$ ，where the operator $\scriptstyle { R _ { n } }$ is defined in Section 12.4.

12.6 For any $f$ in $\mathcal { C } [ - 1 , 1 ]$ ,let $L _ { n } f$ be the polynomial in ${ \mathcal { P } } _ { n }$ that interpolates $f$ at the Chebyshev points (4.27). Given that the largest value of the sum

$$
\sum _ { k = 0 } ^ { n } { \big | } l _ { k } ( x ) { \big | } , \qquad - 1 \leqslant x \leqslant 1 ,
$$

occurs when $x = - 1$ and 1, where $l _ { k }$ is the cardinal function (4.3), deduce that the $\infty$ -norm of the operator $L _ { n }$ has the value

$$
\| L _ { n } \| _ { \infty } = { \frac { 1 } { n + 1 } } \sum _ { j = 0 } ^ { n } \tan \left[ { \frac { ( j + { \frac { 1 } { 2 } } ) \pi } { 2 ( n + 1 ) } } \right] .
$$

12.7 Let $\{ \phi _ { j } \in \mathcal { P } _ { j } ; j = 0 , 1 , 2 , . . . \}$ be a sequence of polynomials that are orthogonal with respect to a positive integrable weight function $\{ w ( x )$ ； $a \leqslant x \leqslant b \}$ ，and let $\{ \xi _ { j k } ; k = 1 , 2 , \ldots , j \}$ be the zeros of $\phi _ { j }$ .Deduce from the theory of Gaussian quadrature that, if $\pmb { p }$ is in $\mathcal { P } _ { j } ,$ then the inequality

$$
\int _ { a } ^ { b } { \left[ p ( x ) \right] ^ { 2 } } w ( x ) \mathrm { d } x \leqslant \int _ { a } ^ { b } w ( x ) \mathrm { d } x \operatorname* { m a x } _ { 1 \leqslant k \leqslant j + 1 } { \left[ p ( \xi _ { j + 1 } _ { k } ) \right] ^ { 2 } }
$$

is satisfied. For any function $f$ in ${ \mathcal { C } } [ a , b ] ,$ let $p _ { j } ^ { * }$ be the best minimax approximation from $\mathcal { P } _ { j }$ to $f ,$ let $L f$ be the element of $\mathcal { P } _ { j }$ that interpolates $f$ at the zeros of $\phi _ { j + 1 }$ ，and let $p$ be the polynomial $( p _ { j } ^ { * } - L _ { j } f )$ . Thus,using the triangle inequality

$$
\| f - L _ { j } f \| _ { 2 } \leqslant \| f - p _ { j } ^ { * } \| _ { 2 } + \| p \| _ { 2 } ,
$$

obtain the‘Erdos Turan theorem'

$$
\operatorname* { l i m } _ { j \to \infty } \int _ { a } ^ { b } { \left[ f ( x ) - ( L _ { j } f ) ( x ) \right] ^ { 2 } } w ( x ) \mathrm { d } x = 0 .
$$

12.8 Let $[ a , b ]$ be the interval $[ - 1 , \ 1 ] ,$ and let $w$ be the function $\{ w ( x ) = x ^ { 2 }$ ； $- 1 \leqslant x \leqslant 1 \}$ . Prove that,if $\pmb { k }$ is even, then the function

$$
\phi _ { k + 1 } ( x ) = { \frac { 1 } { x ^ { 2 } } } { \frac { \mathrm { d } ^ { k + 1 } } { \mathrm { d } x ^ { k + 1 } } } [ ( 1 - x ^ { 2 } ) ^ { k + 1 } ( 1 + x ^ { 2 } ) ] , \qquad - 1 \leqslant x \leqslant 1 ,
$$

is in $\mathcal { P } _ { k + 1 }$ ,and satisfies the orthogonality condition (12.19).Find a similar definition of a polynomial $\phi _ { k + 1 }$ that satisfies equation

(12.19)when $\pmb { k }$ is odd. Check that your definition is correct when $k = 3$

12.9Prove that the Legendre polynomials

$$
\phi _ { j } ( x ) = { \frac { \mathbf { d } ^ { j } } { \mathbf { d } x ^ { j } } } [ ( x ^ { 2 } - 1 ) ^ { j } ] , \qquad - 1 \leqslant x \leqslant 1 , \qquad j = 0 , 1 , 2 , \ldots ,
$$

satisfy the three-term recurrence relation

$$
\phi _ { j + 1 } ( x ) = ( 4 j + 2 ) x \phi _ { j } ( x ) - 4 j ^ { 2 } \phi _ { j - 1 } ( x ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

A good method of solution comes from expressing each term in the form

The middle term has this form, because the Leibniz formula for calculating the jth derivative of a product gives the identity

$$
\frac { \mathrm { d } ^ { j - 1 } } { \mathrm { d } x ^ { j - 1 } } \left\{ \frac { \mathrm { d } } { \mathrm { d } x } \left[ x ( x ^ { 2 } - 1 ) ^ { j } \right] \right\} = x \phi _ { j } ( x ) + j \frac { \mathrm { d } ^ { j - 1 } } { \mathrm { d } x ^ { j - 1 } } [ ( x ^ { 2 } - 1 ) ^ { j } ] .
$$

12.10Prove that the Legendre polynomials, defined in Exercise 12.9, satisfy the equation

$$
( x ^ { 2 } - 1 ) \phi _ { j } ^ { \prime } ( x ) = j x \phi _ { j } ( x ) - 2 j ^ { 2 } \phi _ { j - 1 } ( x ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

A convenient expression for the term $( x ^ { 2 } - 1 ) \phi _ { j } ^ { \prime } ( x )$ can be obtained by regarding the right-hand side of the definition

$$
\phi _ { j + 1 } ( x ) = { \frac { \mathrm { d } ^ { j + 1 } } { \mathrm { d } x ^ { j + 1 } } } [ ( x ^ { 2 } - 1 ) ^ { j + 1 } ]
$$

as the $( j + 1 ) \operatorname { t h }$ derivative of the product $( x ^ { 2 } - 1 ) \times ( x ^ { 2 } - 1 ) ^ { j } .$ Investigate extensions of the formulae of this exercise and the previous one to the Jacobi polynomials that are defined in Section 12.3.

# 13

# Approximation to periodic functions

# 13.1 Trigonometric polynomials

In many branches of science and engineering, periodic functions occur naturally,and there is a need to estimate periodic functions from measured data.Because the variable $x$ may be scaled if necessary,we assume that the functions $f$ that occur are in the space $\mathcal { C } _ { 2 \pi } ,$ which is the set of all continuous functions from ${ \mathcal { R } } ^ { 1 }$ to $\mathcal { R } ^ { 1 }$ that satisfy the periodicity condition

$$
f ( x + 2 \pi ) = f ( x ) , \qquad - \infty < x < \infty .
$$

In approximation calculations the set $\mathcal { A }$ of approximating functions is composed usually of functions of the form

$$
q \left( x \right) = \frac { 1 } { 2 } a _ { 0 } + \sum _ { j = 1 } ^ { n } \left[ a _ { j } \cos \left( j x \right) + b _ { j } \sin \left( j x \right) \right] , \qquad -
$$

where $\{ a _ { j } ; j = 0 , 1 , \ldots , n \}$ and $\{ b _ { j } ; j = 1 , 2 , \ldots , n \}$ are real parameters. If $\pmb { n }$ is fixed, then $\mathcal { A }$ is a linear subspace of $\mathcal { C } _ { 2 \pi }$ of dimension $( 2 n + 1 )$ ,which we denote by ${ \mathcal { Q } } _ { n }$ . It is called the space of trigonometric polynomials of degree $\pmb { n }$ . The actual degree of the trigonometric polynomial (13.2) is the greatest integer $j$ such that at least one of the coefficients $a _ { j }$ and $b _ { j }$ is non-zero.

It is important to note that, if $j$ and $k$ are non-negative integers whose sum is not greater than $\pmb { n }$ ,then the function $\left\{ \cos ^ { \mathrm { i } } x \sin ^ { \mathrm { k } } x ; - \infty < x < \infty \right\}$ is in ${ \mathcal { Q } } _ { n }$ Thus,if $\pmb { p }$ isin ${ \mathcal { Q } } _ { m }$ and $\pmb q$ is in $\mathcal { Q } _ { n }$ ，then the product function $\{ p ( x ) q ( x ) ; - \infty < x < \infty \}$ is in $\mathcal { Q } _ { m + n }$ . We note also that the zero function is the only element of ${ \mathcal { Q } } _ { n }$ that has more than $_ { 2 n }$ zeros in the interval $[ 0 , 2 \pi )$

It is usual to calculate an approximation from ${ \mathcal { Q } } _ { n }$ to $f$ by a least squares algorithm. The main methods that are used are studied in this chapter.

First,however, it is proved that,by choosing $\pmb { n }$ to be sufficiently large, it is possible to approximate any continuous periodic function to arbitrarily high accuracy by a trigonometric polynomial.

# Theorem 13.1

For any $f$ in $\mathcal { C } _ { 2 \pi }$ and for any $\pmb \varepsilon > 0$ ,there exists a polynomial of the form (13.2) that satisfies the condition

$$
\| f - q \| _ { \infty } \leqslant \varepsilon ,
$$

where $_ n$ is a finite integer.

Proof. The function $f$ is the sum of the even and odd functions $f _ { 1 }$ and $f _ { 2 }$ that are defined by the equations

$$
\begin{array} { r l } { f _ { 1 } ( x ) = \frac { 1 } { 2 } [ f ( x ) + f ( - x ) ] , } & { \quad - \infty < x < \infty } \\ { f _ { 2 } ( x ) = \frac { 1 } { 2 } [ f ( x ) - f ( - x ) ] , } & { \quad - \infty < x < \infty } \end{array} \biggr \} .
$$

We show that $f _ { 1 }$ can be approximated to accuracy $\scriptstyle { \frac { 1 } { 4 } } \varepsilon$ and that $f _ { 2 }$ can be approximated to accuracy $\scriptstyle { \frac { 3 } { 4 } } \varepsilon$ .Thus inequality (13.3) is satisfied when $q$ is the sum of the two approximations.

In order to find a suitable approximation to $f _ { 1 }$ , we let ${ \pmb g } _ { 1 }$ be the function

$$
g _ { 1 } ( \cos x ) = f _ { 1 } ( x ) , \qquad 0 \leqslant x \leqslant \pi ,
$$

which is in $\mathcal { C } [ - 1 , 1 ]$ . Hence,by Theorem 6.1, there is an algebraic polynomial ${ p } _ { 1 }$ that satisfies the condition

$$
\begin{array} { r } { \big | g _ { 1 } ( t ) - p _ { 1 } ( t ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad - 1 \leqslant t \leqslant 1 . } \end{array}
$$

It follows that the inequality

$$
\begin{array} { r } { \big | g _ { 1 } ( \cos x ) - p _ { 1 } ( \cos x ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad 0 \leqslant x \leqslant \pi , } \end{array}
$$

holds. We define the function $\{ q _ { 1 } ( x ) ; - \infty < x < \infty \}$ to be the trigonometric polynomial $\{ p _ { 1 } ( \cos x ) ; - \infty < x < \infty \}$ .Hence the required bound

$$
\| f _ { 1 } - q _ { 1 } \| _ { \infty } \leqslant \frac { 1 } { 4 } \varepsilon
$$

is a consequence of expressions (13.5) and (13.7),and the fact that $f _ { 1 }$ and $\pmb q _ { 1 }$ are even functions in $\mathcal { C } _ { 2 \pi } .$

In order to obtain a suitable approximation to $f _ { 2 }$ we note that the values $f _ { 2 } ( 0 )$ and $f _ { 2 } ( \pmb { \pi } )$ are both zero.We let $x _ { 0 }$ be the largest number in the interval $[ 0 , { \frac { 1 } { 2 } } \pi ]$ such that the inequality

$$
\begin{array} { r } { \big | f _ { 2 } ( x ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad 0 \leqslant x \leqslant x _ { 0 } , } \end{array}
$$

is satisfied,and we let $x _ { 1 }$ be the smallest number in $[ \tilde { \frac { 1 } { 2 } \pi } , \pi ]$ that is allowed by the condition

$$
\begin{array} { r } { \big | f _ { 2 } ( x ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad x _ { 1 } \leqslant x \leqslant \pi . } \end{array}
$$

Further, $f _ { 3 }$ is the even function in $\mathcal { C } _ { 2 \pi }$ that takes the values

$$
f _ { 3 } ( x ) = \left\{ \begin{array} { l l } { f _ { 2 } ( x _ { 0 } ) / \sin x _ { 0 } , } & { 0 \leqslant x \leqslant x _ { 0 } , } \\ { f _ { 2 } ( x ) / \sin x , } & { x _ { 0 } \leqslant x \leqslant x _ { 1 } , } \\ { f _ { 2 } ( x _ { 1 } ) / \sin x _ { 1 } , } & { x _ { 1 } \leqslant x \leqslant \pi , } \end{array} \right.
$$

on $[ 0 , \pi ]$ .By applying to $f _ { 3 }$ the method that was used to approximate $f _ { 1 }$ ,it follows that there is an even trigonometric polynomial, $\pmb { q _ { 3 } }$ say, such that the inequality

$$
\| f _ { 3 } - q _ { 3 } \| _ { \infty } \leqslant \frac { 1 } { 4 } \varepsilon
$$

holds.We show that the function $\{ q _ { 2 } ( x ) = \sin x q _ { 3 } ( x ) ; - \infty < x < \infty \}$ is a sufficiently accurate approximation to $f _ { 2 }$ . When $\pmb { x }$ is in $[ 0 , x _ { 0 } ]$ we have the bound

$$
\begin{array} { r l } & { \left| f _ { 2 } ( x ) - q _ { 2 } ( x ) \right| = \left| f _ { 2 } ( x ) - \sin x q _ { 3 } ( x ) \right| } \\ & { \qquad \leqslant \left| f _ { 2 } ( x ) \right| + \left| \sin x f _ { 3 } ( x ) \right| + \sin x \left| f _ { 3 } ( x ) - q _ { 3 } ( x ) \right| } \\ & { \qquad \leqslant \frac { 3 } { 4 } \varepsilon , } \end{array}
$$

where the last line depends on the definitions of $x _ { 0 } , f _ { 3 }$ and $\pmb { q } _ { 3 }$ . Similarly this bound is satisfied when $\pmb { x }$ is in $[ x _ { 1 } , \pi ]$ .Moreover, when $x$ is in $[ x _ { 0 } , x _ { 1 } ] ,$ the inequality

$$
\begin{array} { l } { { \left| f _ { 2 } ( x ) - q _ { 2 } ( x ) \right| = \sin { x } \left| f _ { 3 } ( x ) - q _ { 3 } ( x ) \right| } } \\ { { \leqslant \frac { 1 } { 4 } \varepsilon } } \end{array}
$$

holds. Because these remarks give the condition

$$
\big | f _ { 2 } ( x ) - q _ { 2 } ( x ) \big | \leqslant \frac { 3 } { 4 } \varepsilon , \qquad 0 \leqslant x \leqslant \pi ,
$$

the required bound

$$
\| f _ { 2 } - q _ { 2 } \| _ { \infty } \leqslant \frac { 3 } { 4 } \varepsilon
$$

follows from the fact that $f _ { 2 }$ and $q _ { 2 }$ are both odd functions in $\mathcal { C } _ { 2 \pi }$ The theorem is proved.□

# 13.2 The Fourier series operator $\pmb { S _ { n } }$

$S _ { n }$ is an operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ . For each $f$ in $\mathcal { C } _ { 2 \pi }$ ,the function $s _ { n } f$ is defined to be the trigonometric polynomial that minimizes the least squares distance function

$$
d ( f , q ) = \left[ \int _ { - \pi } ^ { \pi } \{ f ( x ) - q ( x ) \} ^ { 2 } \mathrm { d } x \right] ^ { \frac { 1 } { 2 } } , \qquad q \in { \mathcal { Q } } _ { n } .
$$

Therefore $S _ { n }$ is a linear projection. It has several interesting theoretical properties.For example, it is proved in Chapter 17 that $\| \boldsymbol { S _ { n } } \| _ { \infty }$ is less than or equal to the norm of any other linear projection from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that leaves functions in ${ \mathcal { Q } } _ { n }$ unchanged. Moreover,almost all of the usual algorithms for calculating trigonometric approximations are derived from $\pmb { S _ { n } }$

In order to apply the results of Chapter 11 to $\pmb { S _ { n } }$ we let $( f , g )$ be the scalar product

$$
( f , g ) = \int _ { - \pi } ^ { \pi } f ( x ) g ( x ) \mathrm { d } x ,
$$

for all functions $f$ and $\pmb { g }$ in $\mathcal { C } _ { 2 \pi } ,$ which is consistent with the distance function (13.17). We note that the orthogonality conditions

$$
\left. { \begin{array} { l } { \displaystyle \int _ { - \pi } ^ { \pi } \cos \left( j x \right) \cos \left( k x \right) \mathrm { d } x = 0 , \quad \ j \neq k } \\ { \displaystyle \int _ { - \pi } ^ { \pi } \sin \left( j x \right) \sin \left( k x \right) \mathrm { d } x = 0 , \quad \ j \neq k } \\ { \displaystyle \int _ { - \pi } ^ { \pi } \cos \left( j k \right) \sin \left( k x \right) \mathrm { d } x = 0 } \end{array} } \right\} ,
$$

are satisfied, where $j$ and $\pmb { k }$ are any non-negative integers, which give the following expressions for the coefficients of the trigonometric polynomial $\textstyle S _ { n } f .$

# Theorem 13.2

The trigonometric polynomial (13.2） minimizes the distance function (13.17) if and only if the coefficients have the values

and

$$
a _ { j } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( \theta ) \cos \left( j \theta \right) \mathrm { d } \theta , \qquad j = 0 , 1 , \ldots , n ,
$$

$$
b _ { j } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( \theta ) \sin \left( j \theta \right) \mathrm { d } \theta , \qquad j = 1 , 2 , \ldots , n .
$$

Proof. The orthogonality conditions (13.19) and Theorem 11.2 imply that the required coefficients satisfy the equations

and

$$
\begin{array} { r l } & { \frac { 1 } { 2 } a _ { 0 } = ( f , \cos { \{ 0 . \} } ) / ( \cos { \{ 0 . \} } , \cos { \{ 0 . \} } ) , } \\ & { a _ { j } = ( f , \cos { \{ j . \} } ) / ( \cos { \{ j . \} } , \cos { \{ j . \} } ) , \quad \ j = 1 , 2 , \ldots , n , } \end{array}
$$

$$
b _ { j } = ( f , \sin \{ j . \} ) / ( \sin \{ j . \} , \sin \{ j . \} ) , \qquad j = 1 , 2 , \ldots , n ,
$$

where cos $\{ j . \}$ and sin $\{ j . \}$ are the functions $\{ \cos { ( j x ) } ; - \infty < x < \infty \}$ and $\{ \sin { ( j x ) } ; - \infty < x < \infty \}$ respectively. The values (13.20) and (13.21) follow from the definition of the scalar product, where each denominator is integrated analytically.□

Because Theorem 13.1 implies that the least value of expression (13.17) tends to zero as $^ { n }$ tends to infinity, one expects the sequence of trigonometric polynomials $\{ S _ { n } f ; n = 1 , 2 , 3 , . . . \}$ to converge uniformly to $f ,$ except perhaps in some pathological cases. However, the convergence properties are not shown well by Theorem 13.2. Therefore another expression for $s _ { n }$ is derived that shows explicitly the relation between $s _ { n } f$ and $f _ { - }$

# Theorem 13.3

The value of $s _ { n } f$ at the point $\pmb { x }$ is the expression

$$
( S _ { n } f ) ( x ) = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } { \frac { \sin \left[ ( n + { \frac { 1 } { 2 } } ) \theta \right] } { 2 \sin \left( { \frac { 1 } { 2 } } \theta \right) } } f ( x + \theta ) \mathrm { d } \theta .
$$

Proof. By substituting the values (13.20) and(13.21) in equation (13.2), and by reversing the order of integration and summation, we deduce the identity

$$
\begin{array} { r l } { ( S _ { n } f ) ( x ) = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left\{ \frac { 1 } { 2 } + \displaystyle \sum _ { j = 1 } ^ { n } \left[ \cos { ( j x ) } \cos { ( j \theta ) } \right. \right. } & { { } } \\ { \displaystyle \left. \left. + \sin { ( j x ) } \sin { ( j \theta ) } \right] \right\} f ( \theta ) \mathrm { d } \theta } \\ { \displaystyle } & { { } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left\{ \frac { 1 } { 2 } + \displaystyle \sum _ { j = 1 } ^ { n } \cos { [ j ( \theta - x ) ] } \right\} f ( \theta ) \mathrm { d } \theta } \\ { \displaystyle } & { { } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left[ \frac { 1 } { 2 } + \displaystyle \sum _ { j = 1 } ^ { n } \cos { ( j \theta ) } \right] f ( x + \theta ) \mathrm { d } \theta } \\ { \displaystyle } & { { } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \frac { \sin { [ ( n + \frac { 1 } { 2 } ) \theta ] } } { 2 \sin { ( \frac { 1 } { 2 } \theta ) } } f ( x + \theta ) \mathrm { d } \theta , } \end{array}
$$

where in the fourth line we have changed the variable of integration by the addition of the parameter $\pmb { x }$ , and where the last line depends on equation (12.51). This is the required result.□

It is interesting to consider equation (13.25) when $\pmb { n }$ tends to infinity. If $_ \pmb { \alpha }$ and $\beta$ are any two fixed points of the range $[ - \pi , \pi ]$ ,and if the interval $[ \alpha , \beta ]$ does not contain zero, then the rapid periodic oscillations of the function $\{ \sin { [ ( n + \frac { 1 } { 2 } ) \theta ] } ; - \pi \leqslant \theta \leqslant \pi \}$ cause the integral

$$
{ \frac { 1 } { \pi } } \int _ { \alpha } ^ { \beta } \sin \left[ ( n + { \frac { 1 } { 2 } } ) \theta \right] { \frac { f ( x + \theta ) } { 2 \sin \left( { \frac { 1 } { 2 } } \theta \right) } } \mathrm { d } \theta
$$

to tend to zero. It follows that $( S _ { n } f ) ( x )$ tends to be dominated by the behaviour of $\left\{ f ( x + \theta ) ; - \pi \leqslant \theta \leqslant \pi \right\}$ when $| \pmb \theta |$ is small. It therefore seems plausible that the limit as $\pmb { n }$ tends to infinity of expression (13.25) is unchanged if $f ( x + \theta )$ is replaced by $f ( x )$ . When this suggestion is valid, then it is easy to deduce that $\{ ( S _ { n } f ) ( x ) ; n = 1 , 2 , 3 , . . . \}$ converges to $f ( x )$ ， but it is shown in Chapter 17 that there exist functions $f$ in $\mathcal { C } _ { 2 \pi }$ such that the sequence of maximum errors $\{ \| f - S _ { n } f \| _ { \infty }$ ； $n = 1 , 2 , 3 , \ldots \}$ fails to tend to zero. In Chapter 16, however, it is proved that $\{ S _ { n } f ; n = 1 , 2 , 3 , . . . \}$ does converge uniformly to $f ,$ provided that some mild smoothness conditions are satisfied.

We may use Theorem 13.3 to obtain the value of $\| \pmb { S _ { n } } \| _ { \infty }$ . Expression (13.25) shows that, if $f$ is in $\mathcal { C } _ { 2 \pi }$ and if $\| f \| _ { \infty }$ is not greater than one, then the least upper bound on $| ( S _ { n } f ) ( x ) |$ has the value

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \left| { \frac { \sin { [ ( n + { \frac { 1 } { 2 } } ) \theta ] } } { 2 \sin { ( { \frac { 1 } { 2 } } \theta ) } } } \right| { \bf d } \theta .
$$

Because this expression is independent of $\pmb { x }$ , it must be equal to $\| \boldsymbol { S _ { n } } \| _ { \infty }$ It follows from Theorem 12.7 that the equation

$$
\| S _ { n } \| _ { \infty } = \| R _ { n } \| _ { \infty } , \qquad n = 1 , 2 , 3 , \ldots ,
$$

is satisfied. Therefore Theorem 3.1 and Table 12.1 imply that when $n = 2 0$ , for example, the error $\| S _ { 2 0 } f - f \| _ { \infty }$ is within the factor 3.4945 of the least maximum error that can be achieved when $f$ is approximated by a trigonometric polynomial of degree twenty. Results of this kind help to justify the attention that is given to the approximation operator ${ \pmb S } _ { n }$ ·

The coefficients (13.20) and (13.21) of the trigonometric polynomial $s _ { n } f$ have some useful properties. We see that ${ \pmb a } _ { j }$ and $b _ { j }$ are independent of $\pmb { n }$ . We derive some other properties from the equation

$$
\| f - S _ { n } f \| _ { 2 } ^ { 2 } + \| S _ { n } f \| _ { 2 } ^ { 2 } = \| f \| _ { 2 } ^ { 2 } ,
$$

which is a special case of equation (11.14). Because analytic integration and the orthogonality conditions (13.19) imply that the 2-norm of the function (13.2) has the value

$$
\| q \| _ { 2 } = { \biggl [ } { \textstyle \frac { 1 } { 2 } } \pi a _ { 0 } ^ { 2 } + \pi ~ \sum _ { j = 1 } ^ { n } ~ ( a _ { j } ^ { 2 } + b _ { j } ^ { 2 } ) { \biggr ] } ^ { \frac { 1 } { 2 } } ,
$$

it follows from equation (13.30) that the coefficients (13.20) and (13.21) satisfy the condition

$$
{ \scriptstyle { \frac { 1 } { 2 } } } \pi a _ { 0 } ^ { 2 } + \pi \sum _ { j = 1 } ^ { n } ( a _ { j } ^ { 2 } + b _ { j } ^ { 2 } ) \leqslant \int _ { - \pi } ^ { \pi } [ f ( x ) ] ^ { 2 } { \mathrm { d } } x ,
$$

which is known as ‘Bessel's inequality'. Hence the sequences $\{ a _ { j } ; j =$ $0 , 1 , 2 , \ldots \}$ and $\{ b _ { j } ; j = 1 , 2 , 3 , . . . \}$ tend to zero. Further, the difference between the two sides of expression (13.32) is a measure of the accuracy of the approximation $s _ { n } f$ to $f ,$ because equation (13.30) shows that the difference is equal to $\| f - S _ { n } f \| _ { 2 } ^ { 2 }$ . Theorem 13.1 and the definition of $\pmb { S } _ { n }$ imply that the sequence { $\left\| f - S _ { n } f \right\| _ { 2 }$ ； $n = 1 , 2 , 3 , \ldots \}$ converges to zero. Therefore inequality (13.32) becomes an equality in the limit as $\pmb { n }$ tends to infinity.

# 13.3 The discrete Fourier series operator

It happens often in practice that, instead of knowing the value of $f ( x )$ for all $\pmb { x }$ in $[ - \pi , \pi ] ,$ ，the function is given on only a discrete set of points. Even when $f ( x )$ can be calculated for any $x _ { i }$ , it may be necessary to make numerical approximations to the integrals (13.20) and (13.21). Therefore,in this section, we consider the important problem of obtaining an approximation from ${ \mathcal { Q } } _ { n }$ to a function $f$ in $\mathcal { C } _ { 2 \pi } ,$ using only the equally spaced function values

$$
f { \left( \frac { 2 \pi k } { N } \right) } , \qquad k = 0 , 1 , \dots , N - 1 .
$$

By periodicity the value of $f ( 2 \pi k / N )$ is known for all integral values of $k$ · There is no loss of generality in supposing that $f ( 0 )$ is available, because,if we are given the function values

$$
f { \left( \frac { 2 \pi k } { N } + \alpha \right) } , \qquad k = 0 , 1 , \ldots , N - 1 ,
$$

for some constant $_ \alpha$ ,then the change of variable $\pmb \theta = \pmb x - \pmb \alpha$ can be made. The data (13.34） are suitable for the approximation of the function $\{ f ( \theta + \alpha ) ; - \infty < \theta < \infty \}$ ，which gives a trigonometric polynomial in $\pmb \theta .$ Hence the approximation is also trigonometric polynomial in $x$

The‘discrete Fourier series approximation' from $\mathcal { Q } _ { n }$ to the function $f$ is obtained from the data (13.33). It has the form (13.2)，where the coefficients $\{ a _ { j } ; j = 0 , 1 , \ldots , n \}$ and $\{ b _ { j } ; j = 1 , 2 , \ldots , n \}$ are defined by replacing the integrals of expressions (13.20) and (13.21) by estimates of the form

$$
\frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } g ( \theta ) \mathrm { d } \theta \approx \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } g \Big ( \frac { 2 \pi k } { N } \Big ) .
$$

Hence the coefficients have the values

$$
a _ { j } = \frac 2 N \sum _ { k = 0 } ^ { N - 1 } f \bigg ( \frac { 2 \pi k } N \bigg ) \cos \bigg ( \frac { 2 \pi j k } N \bigg ) , \qquad j = 0 , 1 , \ldots , n ,
$$

and

$$
b _ { j } = \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } f \bigg ( \frac { 2 \pi k } { N } \bigg ) \sin \bigg ( \frac { 2 \pi j k } { N } \bigg ) , \qquad j = 1 , 2 , \ldots , n .
$$

Section 13.4 describes a way of organizing the calculation of these coefficients,so that they can all be found in only of order $N \log _ { 2 } N$ operations,provided that $N$ is a power of two. The technique is so successful that it is applied frequently for very large values of $\pmb { N }$ and $_ n$ The next theorem shows that the estimate (13.35) has some remarkably strong properties.

# Theorem 13.4

If $_ { g }$ is the function $\{ \cos { \left( j \theta \right) } ; - \infty < \theta < \infty \}$ , where $j$ is any integer that is not a positive or negative integral multiple of $N ,$ orif $\pmb { g }$ is the function $\{ \sin { ( j \theta ) } ; - \infty < \theta < \infty \}$ ，where $j$ is any integer, then the approximation (13.35) is exact.

Proof. It is clear that the estimate (13.35) is exact when $\pmb { g }$ is a constant function. In all other cases that are given in the statement of the theorem, the left-hand side of the estimate is zero, and adding or subtracting a multiple of $\pmb { N }$ to the integer $j$ does not alter the terms of the sum (13.35). Hence it is sufficient to establish the equations

$$
\sum _ { k = 0 } ^ { N - 1 } \cos \left( \frac { 2 \pi j k } { N } \right) = 0 , \qquad j = 1 , 2 , \ldots , N - 1 ,
$$

and

$$
\sum _ { k = 0 } ^ { N - 1 } \sin \left( { \frac { 2 \pi j k } { N } } \right) = 0 , \qquad j = 1 , 2 , \ldots , N .
$$

Expression (13.38) holds,because, by substituting $\theta { = } 2 \pi j / N$ and $\pmb { n } = \pmb { N }$ in equation (12.51), we find the identity

$$
\begin{array} { c } { { \frac { 1 } { 2 } + \displaystyle \sum _ { k = 0 } ^ { N - 1 } \cos \left( \displaystyle \frac { 2 \pi j k } { N } \right) = \frac { 1 } { 2 } \sin \left[ ( 2 N + 1 ) \pi j / N \right] / \sin \left( \pi j / N \right) } } \\ { { \frac { 1 } { 2 } { } + \displaystyle \sum _ { j = 1 } ^ { N - 1 } \sum _ { j = 1 , 2 , . . . , N - 1 . } } } \end{array}
$$

Expression (13.39) follows from the symmetry properties of the sine function.□

Another method that suggests itself, for calculating an approximation from ${ \mathcal { Q } } _ { n }$ to a function $f$ in $\mathcal { C } _ { 2 \pi }$ from the function values (13.33), is to minimize the sum of squares

$$
\sum _ { k = 0 } ^ { N - 1 } \bigg [ f \bigg ( \frac { 2 \pi k } { N } \bigg ) - q \bigg ( \frac { 2 \pi k } { N } \bigg ) \bigg ] ^ { 2 } , \qquad q \in \mathcal { Q } _ { n } .
$$

In this case it is appropriate to define the scalar product

$$
( f , g ) = \sum _ { k = 0 } ^ { N - 1 } f \biggl ( \frac { 2 \pi k } { N } \biggr ) g \biggl ( \frac { 2 \pi k } { N } \biggr ) ,
$$

between periodic functions that are defined on the point set $\{ 2 \pi j / N ; j$ integral}. Minimizing expression (13.41） determines the coeffcients of $\pmb q$ uniquely only if the number of coefficients does not exceed the number of data. Therefore we assume that the inequality

$$
\scriptstyle n < { \frac { 1 } { 2 } } N
$$

is satisfied. Because expressions (13.38) and (13.39) imply the orthogonality conditions

$$
\left. \begin{array} { l l } { { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \cos \left( \frac { 2 \pi j k } N \right) \cos \left( \frac { 2 \pi l k } N \right) = 0 , } } & { { j \neq l } } \\ { { } } & { { } } \\ { { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \sin \left( \frac { 2 \pi j k } N \right) \sin \left( \frac { 2 \pi l k } N \right) = 0 , } } & { { j \neq l } } \\ { { } } & { { } } \\ { { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \cos \left( \frac { 2 \pi j k } N \right) \sin \left( \frac { 2 \pi l k } N \right) = 0 } } & { { } } \end{array} \right\} ,
$$

when the integers $j$ and $\iota$ are in the interval $[ 0 , { \scriptstyle { \frac { 1 } { 2 } } } N - { \scriptstyle { \frac { 1 } { 2 } } } ] ,$ , it is straightforward to obtain from Theorem 11.2 the function in ${ \mathcal { Q } } _ { n }$ that minimizes expression (13.41). We find that its coefficients have the values (13.36) and (13.37). Therefore this method of calculating $\pmb q$ is equivalent to the discrete Fourier series method. Hence，if $\begin{array} { r } { n < \frac { 1 } { 2 } N , } \end{array}$ then the discrete Fourier series operator is a projection, and it maps functions in ${ \mathcal { Q } } _ { n }$ into themselves. However, these projection properties are not obtained if $\begin{array} { r } { n \geqslant \frac { 1 } { 2 } N . } \end{array}$

# 13.4 Fast Fourier transforms

In this section we consider the calculation of the coefficients (13.36) and (13.37), when $N$ is a power of two, and when the value of $\pmb { n }$ is close to ${ \scriptstyle { \frac { 1 } { 2 } } } N .$ If each sum is evaluated separately, then the number of computer operations is of order $N ^ { 2 }$ ,but we can do better. For example, consider the two coefficients $a _ { j }$ and $\begin{array} { r } { a _ { 2 } ^ { \perp } N { _ { - } } j { * } } \end{array}$ Because the second coefficient has the value

$$
a _ { \scriptscriptstyle { 2 N - j } } = \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } f \bigg ( \frac { 2 \pi k } { N } \bigg ) ( - 1 ) ^ { k } \cos \bigg ( \frac { 2 \pi j k } { N } \bigg ) ,
$$

it follows that, if we sum separately over the odd and the even values of $\pmb { k }$ in expression (13.36), then we can obtain both $a _ { j }$ and $\alpha _ { 2 } ^ { 1 } N { - } j$ using little more work than the calculation of $a _ { j }$ alone. The FFT (fast Fourier transform) method is a development of this remark.

In order to describe it, we let $a [ m , \alpha , j ]$ and $b [ m , \alpha , j ]$ be the sums

$$
a [ m , \alpha , j ] = \frac { 2 } { m } \sum _ { k = 0 } ^ { m - 1 } f \Big ( \frac { 2 \pi k } { m } + \alpha \Big ) \cos \Big ( \frac { 2 \pi j k } { m } \Big )
$$

and

$$
b [ m , \alpha , j ] = \frac { 2 } { m } \sum _ { k = 0 } ^ { m - 1 } f \Big ( \frac { 2 \pi k } { m } + \alpha \Big ) \sin \Big ( \frac { 2 \pi j k } { m } \Big ) .
$$

They are useful because only a smal amount of work is required to obtain $a [ 2 m , \alpha , j ]$ and $b [ 2 m , \alpha , j ]$ from the numbers $a [ m , \alpha , j ] , a [ m , \alpha +$ $\pi / m , j ] , \ b [ m , \alpha , j ]$ and $b [ m , \alpha + \pi / m , j ]$ ， and because they are the required coefficients when $m = N$ and $\alpha = 0$ . The value of $a [ 2 m , \alpha , j ]$ is defined by the equation

$$
\begin{array} { r l } { \alpha [ 2 m , \alpha , j ] = \displaystyle \frac { 1 } { m } \sum _ { k = 0 } ^ { 2 m - 1 } f \left( \frac { \pi k } { m } + \alpha \right) \cos { \left( \frac { \pi j k } { m } \right) } } & { } \\ { = \displaystyle \frac { 1 } { m } \sum _ { k = 0 } ^ { m - 1 } f \left( \frac { 2 \pi k } { m } + \alpha \right) \cos { \left( \frac { 2 \pi j k } { m } \right) } } & { } \\ { + \displaystyle \frac { 1 } { m } \sum _ { k = 0 } ^ { m - 1 } f \left( \frac { 2 \pi k } { m } + \frac { \pi } { m } + \alpha \right) \cos { \left( \frac { 2 \pi j k } { m } + \frac { \pi j } { m } \right) } } & { } \\ { = \frac { 1 } { 2 } \alpha [ m , \alpha , j ] + \frac { 1 } { 2 } \cos { \left( \frac { \pi j } { m } \right) } \alpha [ m , \alpha + \pi / m , j ] } & { } \\ { ~ - \frac { 1 } { 2 } \sin { \left( \frac { \pi j } { m } \right) } b [ m , \alpha + \pi / m , j ] . } & { } \end{array}
$$

Similarly the identity

$$
\begin{array} { l } { { b [ 2 m , \alpha , j ] = \frac { 1 } { 2 } b [ m , \alpha , j ] + \frac { 1 } { 2 } \sin \Big ( \displaystyle \frac { \pi j } { m } \Big ) a [ m , \alpha + \pi / m , j ] } } \\ { { \phantom { b } } } \\ { { \phantom { b } + \frac { 1 } { 2 } \cos \Big ( \displaystyle \frac { \pi j } { m } \Big ) b [ m , \alpha + \pi / m , j ] } } \end{array}
$$

is satisfied, which is used to evaluate $b [ 2 m , \alpha , j ]$ . It is important to note that the definitions (13.46) and (13.47) imply the equations

$$
\begin{array} { l }  { a [ m , \alpha , j ] = a [ m , \alpha , m - j ] \atop b [ m , \alpha , j ] = - b [ m , \alpha , m - j ] \Big \} , } \end{array}
$$

and that $b [ m , \alpha , j ]$ is zero when $j = { \textstyle \frac { 1 } { 2 } } m$

The FFT method begins by setting the numbers

$$
a [ 1 , \alpha , 0 ] = 2 f ( \alpha ) ,
$$

where the values of $_ { \pmb { \alpha } }$ are the numbers in the set $\scriptstyle \{ 2 \pi k / N , k =$ $0 , 1 , \ldots , N - 1 \}$ . Then an iterative process is applied, where each itera-tion depends on the value of $^ { m }$ ,which initially has the value one.At the beginning of each iteration the numbers $\{ a [ m , \alpha , j ]$ ； $\scriptstyle 0 \leqslant j \leqslant { \frac { 1 } { 2 } } m \}$ and $\{ b [ m , \alpha , j ] ; 0 < j < \frac { 1 } { 2 } m \}$ are available,where the second set is empty until $m \geqslant 4$ , and where the range of $_ \alpha$ is the set $\left\{ 2 \pi k / N ; k = 0 , 1 , \ldots \right.$ ，

$N / m - 1 \}$ . The iteration uses equations (13.48), (13.49) and (13.50) to calculate the coefficients $\{ a [ 2 m , \alpha , j ] ; 0 \leqslant j \leqslant m \}$ and $\{ b [ 2 m , \alpha , j ] ; 0 < j <$ $m \}$ ,where the new range of $_ { \pmb { \alpha } }$ is the set $\{ 2 \pi k / N ; k = 0 , 1 , \ldots , N / 2 m - 1 \}$ Because the term $( \alpha + \pi / m )$ occurs in the formulae (13.48) and (13.49), all the data that are available at the beginning of the iteration are necessary. All terms that are not available explicitly as data are either zero or are obtained from equation (13.5O).At the end of the iteration the value of $^ { m }$ is multiplied by two and is tested. If the new value is less than $N ,$ then a new iteration is begun. Otherwise,when $m = N ,$ all the required values of the coefficients are found.Because the number of computer operations of each iteration of this process is of order $N ,$ ,the total work of the FFT method is only of order $N \log _ { 2 } N .$

The FFT method can be extended to the case when $\pmb { N }$ has the value

$$
N = r _ { 1 } r _ { 2 } \ldots r _ { t } ,
$$

where the terms $\{ r _ { s } ; s = 1 , 2 , \ldots , t \}$ are any integers that are greater than one. Then $t$ iterations of a process are applied, each iteration being similar to the one that is described in the previous paragraph. Initially the parameters (13.51) are set as before,and $^ { m }$ is equal to one. The later values of $^ { m }$ are defined by multiplying $^ { m }$ by $\boldsymbol { r } _ { s }$ at the end of each iteration, where $\pmb { s }$ is the number of the iteration. At the start of the sth iteration, the numbers $\{ a [ m , \alpha , j ] ; 0 \leqslant j \leqslant \frac { 1 } { 2 } m \}$ and $\{ b [ m , \alpha , j ] ; 0 < j < \frac { 1 } { 2 } m \}$ are known, where,as before,the range of $_ { \pmb { \alpha } }$ is the set $\scriptstyle \{ 2 \pi k / N $ ； $k = 0 , 1 , \ldots ,$ $N / m - 1 \}$ . The iteration calculates the terms $\{ a [ r _ { s } m , \alpha , j ] ; 0 \leqslant j \leqslant \frac { 1 } { 2 } r _ { s } m \}$ and $\{ b [ r _ { s } m , \alpha , j ] ; 0 < j < \frac { 1 } { 2 } r _ { s } m \}$ ，where the new range of $_ { \pmb { \alpha } }$ is the set $\left\{ 2 \pi k / N ; k = 0 , 1 , \ldots , N / ( r _ { s } m ) - 1 \right\}$ . Hence,after $t$ iterations, the required coefficients are found.

In order to calculate $a [ r m , \alpha , j ]$ and $b [ r m , \alpha , j ]$ , we replace $^ { m }$ by rm in the definitions (13.46) and (13.47).The sums over $k$ are split into $r$ parts, where in each part the value of $k$ (modulo $r$ ） is constant.Thus we find expressions for $a [ r m , \alpha , j ]$ and $b [ r m , \alpha , j ] ,$ in terms of $a [ m , \alpha + 2 \pi l / r m , j ]$ and $b [ m , \alpha + 2 \pi l / r m , j ]$ where $l$ takes the values $l = 0 , 1 , \ldots , ( r - 1 ) ,$ ， which are suitable for the change to the range of $\pmb { \alpha }$ that is made by the iteration. Because the greatest new value of $j$ is $\scriptstyle { \frac { 1 } { 2 } } r _ { s } m$ , it happens sometimes that $j$ exceeds $_ { m }$ ， It is therefore important to note that the definitions (13.46) and (13.47), not only provide the equations (13.50), but also they give the identities

$$
\begin{array} { c } { { a \left[ m , \alpha , j + m \right] = a \left[ m , \alpha , j \right] } } \\ { { b \left[ m , \alpha , j + m \right] = b \left[ m , \alpha , j \right] } } \end{array} \biggr \} .
$$

It is helpful to work through a simple example,in order to verify that all the formulae that are needed by the general FFT method have been mentioned.

# 13 Exercises

.1 Let $j$ and $\pmb { n }$ be positive integers such that $j \leqslant 2 n$ .Show that there is a non-zero function in ${ \mathcal { Q } } _ { n }$ that has zeros at any $j$ distinct points of the interval $[ 0 , 2 \pi )$ . A convenient method is to express the required function as the product of functions from $\mathcal { Q } _ { 1 }$ .Hence develop a procedure, that is analogous to Lagrange interpolation, for calculating the function $q$ in ${ \mathcal { Q } } _ { n }$ that satisfies the conditions $\{ q ( \xi _ { i } ) = f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , 2 n \}$ where the function values $\{ f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , 2 n \}$ are given,and where the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , 2 n \}$ are all different and are all in $[ 0 , 2 \pi )$ · Further, prove that no non-zero element of ${ \mathcal { Q } } _ { n }$ has more than $_ { 2 n }$ zeros in $[ 0 , 2 \pi )$

13.2Let $f$ be the odd function in $\mathcal { C } _ { 2 \pi }$ that satisfies the equation

$$
f ( x ) = 1 - ( 4 / \pi ^ { 2 } ) ( x - { \textstyle \frac { 1 } { 2 } } \pi ) ^ { 2 } , \qquad 0 \leqslant x \leqslant \pi .
$$

Calculate the Fourier series approximation to $f ,$ and deduce the identity

$$
1 + ( { \textstyle { \frac { 1 } { 3 } } } ) ^ { 6 } + ( { \textstyle { \frac { 1 } { 5 } } } ) ^ { 6 } + ( { \textstyle { \frac { 1 } { 7 } } } ) ^ { 6 } + \dots = \pi ^ { 6 } / 9 6 0
$$

from Bessel's inequality.

13.3 Let $_ n$ be a fixed positive integer, let $\bar { \pmb { S } } [ n , N ]$ be the linear operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that is equivalent to the discrete Fourier method of Section 13.3,and let $f$ be any function in $\mathcal { C } _ { 2 \pi }$ .Prove that the limit

$$
\operatorname* { l i m } _ { N  \infty } \| \bar { S } [ n , N ] f - S _ { n } f \| _ { \infty } = 0
$$

is obtained, where $s _ { n }$ is the Fourier series operator that is defined in Section 13.2.

13.4 Given the function values $f ( 0 ) = 0 . 2 , f ( \textstyle { \frac { 1 } { 2 } } \pi ) = 0 . 2 5 , f ( \pi ) = 1 . 0$ and $f ( 1 _ { 2 } ^ { \frac { 1 } { 2 } } \pi ) = 0 . 5$ ，use the discrete Fourier method to obtain an approximation to $f$ of the form

$$
\begin{array} { r } { q ( x ) = \frac { 1 } { 2 } a _ { 0 } + a _ { 1 } \cos x + b _ { 1 } \sin x + a _ { 2 } \cos ( 2 x ) , \qquad - \infty < x < \infty . } \end{array}
$$

Let $\bar { \pmb q }$ be the function

$$
\bar { q } ( x ) = { \textstyle \frac { 1 } { 2 } } a _ { 0 } + a _ { 1 } \cos x + b _ { 1 } \sin x + { \textstyle \frac { 1 } { 2 } } a _ { 2 } \cos ( 2 x ) , \qquad - \infty < x <
$$

Explain why $\bar { q }$ interpolates the data but $q$ does not.

13.5 Let $\bar { \pmb { S } } [ \pmb { n } , \pmb { N } ]$ be the operator that is defined in Exercise 13.3, and let $\pmb { D } _ { \pmb { \lambda } }$ be the operator from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { C } _ { 2 \pi }$ such that, for any $f$ in $\mathcal { C } _ { 2 \pi } , D _ { \lambda } f$ is the function

$$
( D _ { \lambda } f ) ( x ) = f ( x + \lambda ) , \qquad - \infty < x < \infty .
$$

Prove that $\bar { \cal S } [ n , 2 N ]$ is the operator

$$
\bar { S } [ n , 2 N ] = { \textstyle \frac { 1 } { 2 } } \{ \bar { S } [ n , N ] + D _ { - \pi / N } \bar { S } [ n , N ] D _ { \pi / N } \} .
$$

Relate this equation to the FFT method.

13.6 Apply the FFT method to calculate an approximation in $\mathcal { Q } _ { 3 }$ to the data

$$
\begin{array} { l l l } { { f ( 0 ) } } & { { = - 0 . 1 1 2 1 7 8 } } & { { f ( \pi ) \quad \quad = - 0 . 3 2 1 4 1 2 } } \\ { { f ( \pi / 4 ) } } & { { = \quad 1 . 0 7 9 6 5 9 } } & { { f ( 5 \pi / 4 ) = - 0 . 5 2 8 1 1 3 } } \\ { { f ( \pi / 2 ) } } & { { = \phantom { - } 2 . 1 7 2 6 6 7 } } & { { f ( 3 \pi / 2 ) = - 0 . 5 6 2 3 2 6 } } \\ { { f ( 3 \pi / 4 ) = } } & { { 0 . 3 7 6 6 0 7 } } & { { f ( 7 \pi / 4 ) = - 0 . 4 6 6 2 6 1 , } } \end{array}
$$

using the results of the previous two exercises to check your calculation.

13.7 State and prove a characterization theorem for the best minimax approximation from ${ \mathcal { Q } } _ { n }$ to a function $f$ in $\mathcal { C } _ { 2 \pi } ,$ that is analogous to Theorem 7.2.

13.8Let $f$ be a function in $\mathcal { C } _ { 2 \pi }$ that takes the values

$$
f ( x ) = \lvert x - \xi \rvert , \qquad \xi - \varepsilon \leqslant x \leqslant \xi + \varepsilon ,
$$

where $\pmb { \xi }$ is a fixed number, and where $\pmb \varepsilon$ is a positive constant that is much less than $\pmb { \pi }$ 、Prove that the limit

$$
\operatorname* { l i m } _ { n  \infty } { ( S _ { n } f ) ( \xi ) = f ( \xi ) }
$$

is obtained, and that, if $f$ satisfies the Lipschitz condition

$$
\left| f ( x _ { 1 } ) - f ( x _ { 0 } ) \right| \leqslant L \left| x _ { 1 } - x _ { 0 } \right|
$$

for all real numbers $\scriptstyle x _ { 0 }$ and $x _ { 1 }$ ,where $L$ is a constant, then the difference $\left| f ( \xi ) - ( S _ { n } f ) ( \xi ) \right|$ is of order $1 / n$

3.9 Deduce from Exercises 13.3 and 13.5 that the inequality $\| { \bar { S } } [ n , N ] \| _ { \infty } \geqslant \| S _ { n } \| _ { \infty }$ is satisfied.

13.10Prove the analogy of Theorem 6.2 for trigonometric approximation, namely that, if $\left\{ G _ { k } ; k = 1 , 2 , 3 , . . . \right\}$ is a sequence of linear monotone operators from $\mathcal { C } _ { 2 \pi }$ to $\ell _ { 2 \pi }$ ，then the sequence $\{ G _ { k } f ; k = 1 , 2 , 3 , . . . \}$ converges uniformly to $f$ for all $f$ in $\mathcal { C } _ { 2 \pi }$ if and only if it converges uniformly for the functions $\{ f ( x ) =$

# Exercises

$1 ; - \infty < x < \infty \} , \quad \{ f ( x ) = \cos x ; - \infty < x < \infty \} ,$ and $\{ f ( x ) =$ sin $x ; - \infty < x < \infty \}$ . By establishing that the Fejer operator

$$
G _ { k } = \frac { 1 } { k } \left[ S _ { 0 } + S _ { 1 } + \ldots + S _ { k - 1 } \right]
$$

is monotone, where $s _ { n }$ is still the Fourier series operator, deduce another proof of Theorem 13.1.

# 14

# The theory of best $\pmb { L _ { 1 } }$ approximation

# 14.1 Introduction to best $\pmb { L _ { 1 } }$ approximation

In Chapter 1 we noted that a best $L _ { 1 }$ approximation from a subset $\mathscr { A }$ of $\mathcal { C } [ a , b ]$ to a function $f$ in $\mathcal { C } [ a , b ]$ is an element of $\mathcal { A }$ that minimizes the expression

$$
\| f - p \| _ { 1 } = \int _ { a } ^ { b } { \bigl | } f ( x ) - p ( x ) { \bigr | } \mathrm { d } x , \qquad p \in { \mathcal { A } } .
$$

The theory that is given in this chapter is for the frequently occurring case when $\mathcal { A }$ is a linear space. Necessary and sufficient conditions for the function $p ^ { * }$ in $\mathcal { A }$ to be a best $L _ { 1 }$ approximation to $f$ are given in the next section. They have the interesting property that all the dependence on $f$ is contained in the sign function

$$
s ^ { * } ( x ) = \left\{ \begin{array} { l l } { - 1 , } & { f ( x ) < p ^ { * } ( x ) } \\ { 0 , } & { f ( x ) = p ^ { * } ( x ) } \\ { 1 , } & { f ( x ) > p ^ { * } ( x ) , } \end{array} \right. \quad a \leqslant x \leqslant b .
$$

It follows,therefore, that if $p ^ { * }$ is a best approximation to $f ,$ and if $f$ is changed in any way that leaves the sign function (14.2) unaltered, then $p ^ { * }$ remains a best approximation to $f .$ A similar result holds in the discrete case,where we require the function in $\mathscr { A }$ that minimizes the expression

$$
\sum _ { t = 1 } ^ { m } \big | f ( x _ { t } ) - p ( x _ { t } ) \big | , \qquad p \in \mathcal { A } ,
$$

where $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ is a set of data points in $[ a , b ]$ . This property explains the statement, made in Chapter 1, that, if there are a few gross errors in the data $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ ,then the magnitudes of these errors make no difference to the final approximation.

In order to introduce the characterization theorem,we consider first the approximation of a strictly monotonic function $f$ in ${ \mathcal { C } } [ a , b ]$ by a constant function $p$ ,where the value of the constant is to be determined. Thus $\mathscr { A }$ is a linear space of dimension one. The value of expression (14.1), when $p$ is the function $\{ p ( x ) = f ( \xi )$ ； $a \leqslant x \leqslant b \}$ , is the total area of the shaded regions of Figure 14.1. We require the value of $\pmb { \xi }$ that minimizes this area. The figure shows that, if we replace $p$ by the function $\{ p ( { \pmb x } ) =$ $f ( \xi ) + \varepsilon \mathrm { ~ ; ~ } a \leqslant x \leqslant b \}$ ,where $\pmb \varepsilon$ is small, then the change to the area of the left-hand shaded region is approximately ${ \pmb \varepsilon } \left( { \pmb \xi } - { \pmb a } \right)$ ,and the change to the area of the other shaded region is approximately $- \varepsilon ( b - \xi )$ , which gives a total change of about $2 \varepsilon \left( \xi - \textstyle { \frac { 1 } { 2 } } [ a + b ] \right)$ . Therefore, if $\begin{array} { r } { \xi < \frac { 1 } { 2 } [ a + b ] . } \end{array}$ we can reduce $\| f - p \| _ { 1 }$ by letting $\pmb \varepsilon$ be positive, and, if $\begin{array} { r } { \xi > \frac { 1 } { 2 } [ a + b ] , } \end{array}$ , there exists a negative value of $\pmb \varepsilon$ that reduces the error. It follows that the required approximation is the constant function $\{ p ( x ) = f ( { \textstyle \frac { 1 } { 2 } } [ a + b ] )$ ； $a \leqslant x \leqslant b \}$ This approximation is optimal because the measures of the sets $\{ x \colon f ( x ) <$ $p ( { \pmb x } ) \}$ and $\{ x \colon f ( x ) > p ( x ) \}$ are equal. Thus we have an example of a condition for a best approximation that depends just on the sign of the error function.

Another useful property of this example is that, if we know in advance that $f$ is monotonic, then the calculation of $f ( x )$ at the single point $x = { \textstyle { \frac { 1 } { 2 } } } ( a + b )$ provides all the data that are needed to determine the best approximation. It is shown in Section 14.3 that this property generalizes to the case when $\mathcal { A }$ satisfies the Haar condition.

# 14.2 The characterization theorem

The following theorem gives the basic necessary and sufficient condition for the function $p ^ { * }$ to be a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$ It is an extension of the example of the last section. It includes a condition

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0003_pages_0141-0210/auto/images/1bda995631250fd4f271c669fe9b9b0b7427b156eb3323bedd9932b0fb200738.jpg)  
Figure 14.1. The value of $\| f - p \| _ { 1 }$

on the set of zeros of the function $\{ f ( x ) - p ^ { * } ( x )$ ； $a \leqslant x \leqslant b $ ,that fails only in pathological cases.

# Theorem 14.1

Let $\mathscr { A }$ be a linear subspace of $\mathcal { C } [ a , b ]$ . Let $f$ be any function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,and let $p ^ { * }$ be any element of $\mathcal { A } ,$ ， such that the set

$$
{ \mathcal { L } } = \{ x : f ( x ) = p ^ { * } ( x ) , a \leqslant x \leqslant b \}
$$

is either empty or is composed of a finite number of intervals and discrete points. Then $p ^ { * }$ is a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f ,$ if and only if the inequality

$$
{ \biggl | } \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x { \biggr | } \leqslant \int _ { { \mathcal { Z } } } \left| p ( x ) \right| \mathrm { d } x
$$

is satisfied for all $p$ in $\scriptstyle { \mathcal { A } } ,$ where $s ^ { * }$ is the function (14.2).

Proof. If condition (14.5) does not hold for all functions $p$ in $\mathcal { A } .$ we let $p$ be an element of $\mathscr { A }$ such that the number

$$
\eta = \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x - \int _ { \mathcal { Z } } \left| p ( x ) \right| \mathrm { d } x
$$

is positive,and such that the normalization condition

$$
\| p \| _ { \infty } = 1
$$

holds. We prove that $p ^ { * }$ is not a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f$ by showing that, if the number $\pmb \theta$ is suficiently small and positive,then the inequality

$$
\| f - ( p ^ { * } + \theta p ) \| _ { 1 } < \| f - p ^ { * } \| _ { 1 }
$$

is obtained. The upper bound on $\pmb \theta$ depends on the set

$$
\mathcal { Z } _ { \theta } = \{ x : 0 < \left| f ( x ) - p ^ { * } ( x ) \right| \leqslant \theta , a \leqslant x \leqslant b \} .
$$

We require $\pmb \theta$ to be so small that the condition

$$
\int _ { \mathcal { X } _ { \theta } } \mathrm { d } x < \frac { 1 } { 2 } \eta
$$

is satisfied,which is possible because of the restrictions on $\mathcal { Z }$ that are given in the statement of the theorem.We let $\mathcal { X } _ { \mathbf { R } }$ be the set that contains the points of $[ a , b ]$ that are neither in $\mathcal { Z }$ nor in $\mathcal { Z } _ { \pmb { \theta } }$ .Inequality(14.8） is proved by dividing the range of integration in the definition

$$
\| f - ( p ^ { * } + \theta p ) \| _ { 1 } = \int _ { a } ^ { b } { \bigl | } f ( x ) - p ^ { * } ( x ) - \theta p ( x ) { \bigr | } \mathrm { d } x
$$

into the three parts $\mathcal { X } , \mathcal { X } _ { \theta }$ and $\mathcal { L } _ { \mathbf { R } }$ . The definition (14.4) gives the identity

$$
\begin{array} { r } { \mathopen { } \mathclose \bgroup \left| f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \aftergroup \egroup \right| = \theta \mathopen { } \mathclose \bgroup \left| p ( x ) \aftergroup \egroup \right| , \qquad x \in \mathcal { L } , } \end{array}
$$

condition (14.7) provides the bound

$$
\begin{array} { r l } & { \left| f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \right| \leqslant \left| f ( x ) - p ^ { * } ( x ) \right| + \theta \left| p ( x ) \right| } \\ & { \quad \leqslant \left| f ( x ) - p ^ { * } ( x ) \right| + \theta [ 2 - s ^ { * } ( x ) p ( x ) ] , \qquad x \in \mathcal { Z } _ { \theta } , } \end{array}
$$

and equations (14.7) and (14.9) imply that, when $x$ is in $\mathcal { Z } _ { \mathbf { R } }$ ,the sign of $\{ f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \}$ is the same as the sign of $\{ f ( x ) - p ^ { * } ( x ) \}$ ,which gives the relation

$$
{ \big | } f ( x ) - p ^ { * } ( x ) - \theta p ( x ) { \big | } = { \big | } f ( x ) - p ^ { * } ( x ) { \big | } - \theta s ^ { * } ( x ) p ( x ) , \qquad x \in \mathcal { X } _ { \mathbf { R } } .
$$

Therefore it follows from equations (14.2) and (14.11) that the condition

$$
\begin{array} { l } { \displaystyle \left\| f - ( p ^ { * } + \theta p ) \right\| _ { 1 } \leqslant \left\| f - p ^ { * } \right\| _ { 1 } + \theta \displaystyle \int _ { \mathcal { X } } \left| p ( x ) \right| \mathrm { d } x - \theta \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x } \\ { \displaystyle \qquad + 2 \theta \displaystyle \int _ { \mathcal { X } _ { \theta } } \mathrm { d } x } \end{array}
$$

is obtained. Inequality (14.8) is now a consequence of expressions (4.6) and (14.1O),which proves the first half of the theorem.

To prove the second part of the theorem, we let $\pmb q$ be a general element of $\mathcal { A } _ { : }$ we let $p$ be the function $( p ^ { * } - q )$ , which is also in $\mathcal { A } ,$ and we deduce from inequality (14.5） that the distance $\| f - q \| _ { 1 }$ is not less than the distance $\| f - p ^ { * } \| _ { 1 }$ . Specifically, from expressions (14.2),(14.4) and (14.5) we obtain the relation

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } \left| f ( x ) - q ( x ) \right| \mathrm { d } x \geqslant \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) [ f ( x ) - q ( x ) ] \mathrm { d } x + \displaystyle \int _ { x } | f ( x ) - q ( x ) | \mathrm { d } x } \\ { \displaystyle = \int _ { a } ^ { b } s ^ { * } ( x ) [ f ( x ) - p ^ { * } ( x ) ] \mathrm { d } x + \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) [ p ^ { * } ( x ) - q ( x ) ] \mathrm { d } x } \\ { \displaystyle \quad + \displaystyle \int _ { x } | p ^ { * } ( x ) - q ( x ) | \mathrm { d } x } \\ { \displaystyle = \| f - p ^ { * } \| _ { 1 } + \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x + \displaystyle \int _ { x } | p ( x ) | \mathrm { d } x } \\ { \displaystyle \geqslant \| f - p ^ { * } \| _ { 1 } , } \end{array}
$$

where the first line depends on the property $\{ s ^ { * } ( x ) = 0 , x \in \mathcal { X } \}$ .Because this inequality shows that $q$ is not a better $L _ { 1 }$ approximation than $p ^ { * }$ ,the theorem is proved.□

Frequently the set $\mathcal { Z } ,$ ,defined by equation (14.4),contains only a finite number of discrete points. In this case, because the right-hand side of

expression (14.5) is zero, $p ^ { * }$ is a best $\scriptstyle { L _ { 1 } }$ approximation from $\mathcal { A }$ to $f$ if and only if the condition

$$
( s ^ { * } , p ) = 0 , \qquad p \in \mathcal { A } ,
$$

holds,where $s ^ { * }$ is the function (14.2),and where $( s ^ { * } , p )$ is the scalar product

$$
( s ^ { * } , p ) = \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x .
$$

Scalar products are mentioned, because it is interesting to compare a best approximation in the 1-norm with the best approximation in the 2-norm. We recall from Theorem 11.1 that the condition for $p ^ { * }$ to be the function in $\mathscr { A }$ that minimizes the expression

$$
\| f - p \| _ { 2 } = { \bigg [ } \int _ { a } ^ { b } { \left[ f ( x ) - p ( x ) \right] ^ { 2 } } \mathrm { d } x { \bigg ] } ^ { \frac { 1 } { 2 } } , \qquad p \in { \mathcal { A } } ,
$$

is the equation

$$
( f - p ^ { * } , p ) = 0 , \qquad p \in \mathcal { A } .
$$

Therefore,to minimize the 2-norm of the error,we require the error function to be orthogonal to every element of $\mathcal { A } _ { : }$ ，but, to minimize the 1-norm of the error,it is the sign function (14.2) that has to be orthogonal to every element of $\mathscr { A }$

The reason for the similarity between these characterization theorems is that expressions (14.1) and(14.19) are both special cases of the $q$ -norm error

$$
\| f - p \| _ { q } = { \biggl [ } \int _ { a } ^ { b } { \bigl | } f ( x ) - p ( x ) { \bigr | } ^ { q } ~ \mathrm { d } x { \biggr ] } ^ { 1 / q } , \qquad p \in { \mathcal { A } } ,
$$

where $\pmb q$ is a real constant that is not less than one.In order to develop this remark, we let $p ^ { * }$ be an element of $\mathcal { A }$ that minimizes expression (14.21), we let $p$ be any element of $\mathcal { A } _ { : }$ , and we let $\phi$ be the function

$$
\phi \left( \theta \right) = \int _ { a } ^ { b } \left| f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \right| ^ { q } \mathrm { d } x , \qquad - \infty < \theta < \infty .
$$

It follows that $\phi ( \theta )$ is least when $\pmb \theta$ is zero. Therefore, if $\phi$ is differentiable, the term $\phi ^ { \prime } ( 0 )$ must be zero. This derivative can be calculated when $q$ is greater than one.Hence we obtain the condition

$$
\int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) | f ( x ) - p ^ { * } ( x ) | ^ { q - 1 } \mathrm { d } x = 0 , \qquad p \in \mathcal { A } ,
$$

on $p ^ { * }$ ， where $s ^ { * }$ is the function (14.2). We note that, when $q = 2$ , this condition is the same as equation (14.20). Moreover, if we let $q$ tend to one,then the conditions (14.17) and (14.23) on $p ^ { * }$ become the same. Thus the similarity between the characterization theorems 11.1 and 14.1 is explained.

Two uses of Theorem 14.1 are as follows. The proof of the first part of the theorem provides a constructive method for obtaining an approximation from $\mathcal { A }$ to $f$ that is better than $p ^ { * }$ if condition (14.5） is not satisfied. Secondly, the theorem can be used sometimes to calculate the best approximation directly. For example, in the approximation problem that is shown in Figure 14.1, the required approximation is the function $\{ p ^ { * } ( x ) = f ( { \textstyle \frac { 1 } { 2 } } [ a + b ] )$ ； $a \leqslant x \leqslant b \}$ ，because then the sign function (14.2) satisfies the characterization condition (14.5).

# 14.3 Consequences of the Haar condition

As in the case of minimax approximation,one can say much more about the best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f ,$ if the linear space $\mathcal { A }$ satisfies the Haar condition. We refer to the properties (1)-(4)of the Haar condition that are stated in the second paragraph of Section 7.3.First we prove a theorem on the number of zeros of the error function of a best $L _ { 1 }$ approximation, that is applied in two ways.It helps to show that the best approximation is unique. Moreover, it is used to generalize our earlier remark, that the best $L _ { 1 }$ approximation can be calculated sometimes by interpolation at points of the range $[ a , b ] ,$ that are independent of the function that is being approximated.

# Theorem 14.2

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition,and let $f$ be any function in $\mathcal { C } [ a , b ]$ .If $p ^ { * }$ is a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f ,$ and if the number of zeros of the error function

$$
e ^ { * } ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is finite, then $e ^ { * }$ changes sign at least $( n + 1 )$ times.

Proof. Suppose that $e ^ { * }$ has a finite number of zeros,and that it changes sign fewer than $( n + 1 )$ times. Then,by property (2) of Section 7.3, there exists a function $\pmb { p }$ in $\mathcal { A } _ { : }$ ,such that the product $s ^ { * } ( x ) p ( x )$ is positive for all values of $x$ in $[ a , b ]$ ,except for the zeros of $e ^ { * }$ , where $s ^ { * }$ is the function (14.2). Hence the integral (14.18) is positive,but the right-hand side of expression (14.5) is zero,because $\mathcal { Z }$ has measure zero.Therefore $p ^ { * }$ fails to satisfy the characterization theorem 14.1. This contradiction proves the theorem.□

One application of this theorem is to show that the best $L _ { 1 }$ approximation is unique when the Haar condition is satisfied.

# Theorem 14.3

Let $\mathscr { A }$ be a linear subspace of $\mathcal { C } [ a , b ]$ that satisfies the Haar condition. Then, for any $f$ in $\mathcal { C } [ a , b ]$ ,there is just one best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$

Proof. Let $q ^ { * }$ and $r ^ { * }$ be best $L _ { 1 }$ approximations from $\mathcal { A }$ to $f ,$ and let $p ^ { * }$ be the function $\scriptstyle { \frac { 1 } { 2 } } ( q ^ { * } + r ^ { * } )$ . We consider the inequality

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } \left| f ( x ) - p ^ { * } ( x ) \right| \mathrm { d } x = \int _ { a } ^ { b } \left| \frac { 1 } { 2 } [ f ( x ) - q ^ { * } ( x ) ] + \frac { 1 } { 2 } [ f ( x ) - r ^ { * } ( x ) ] \right| \mathrm { d } x } \\ { \displaystyle \qquad \leqslant \frac { 1 } { 2 } \int _ { a } ^ { b } \left| f ( x ) - q ^ { * } ( x ) \right| \mathrm { d } x + \frac { 1 } { 2 } \int _ { a } ^ { b } \left| f ( x ) - r ^ { * } ( x ) \right| \mathrm { d } x , \qquad ( 1 4 ) \mathrm { d } x , } \end{array}
$$

which depends on the definition of the modulus of a number.Because the right-hand side is the least distance from $\mathcal { A }$ to $f ,$ and because $p ^ { * }$ is in $\mathcal { A } ,$ this inequality is satisfied as an equation. Therefore, because allfunctions are in ${ \mathcal { C } } [ a , b ]$ , the identity

$$
{ \big | } f ( x ) - p ^ { * } ( x ) { \big | } = { \textstyle { \frac { 1 } { 2 } } } { \big | } f ( x ) - q ^ { * } ( x ) { \big | } + { \textstyle { \frac { 1 } { 2 } } } { \big | } f ( x ) - r ^ { * } ( x ) { \big | }
$$

holds for all $x$ in $[ a , b ]$ .In particular,when $f ( x )$ is equal to $p ^ { * } ( x )$ ,then both $q ^ { * } ( x )$ and $r ^ { * } ( x )$ must be equal to $f ( x )$ . It follows from Theorem 14.2 that the function $\{ q ^ { * } ( x ) - r ^ { * } ( x )$ ； $a \leqslant x \leqslant b \}$ has at least $( n + 1 )$ zeros. Therefore the Haar condition implies that the functions $q ^ { * }$ and $r ^ { * }$ are the same.□

Most algorithms for calculating best $L _ { 1 }$ approximations aim to find the zeros of the error function. Often the number of zeros is exactly $( n + 1 )$ ， where $( n + 1 )$ is the dimension of $\mathcal { A } .$ .For example, this case occurs if $\mathcal { A }$ is the space $\mathcal { P } _ { n }$ if $f$ is in $\mathcal { C } ^ { ( n + 1 ) } [ a , b ] .$ and if the derivative $f ^ { ( n + 1 ) } ( x )$ is positive for all $x$ in $[ a , b ]$ . Therefore the following theorem is useful.

# Theorem 14.4

Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition,and let $f$ be a function in $\mathcal { C } [ a , b ]$ such that the error function (14.24) has exactly $( n + 1 )$ zeros, where $p ^ { * }$ is the best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$ . Then the positions of the zeros do not depend on $f .$

Proof. Let $s ^ { * }$ be the function (14.2),and let the zeros of the error function $\{ f ( x ) - p ^ { * } ( x ) ; a \leqslant x \leqslant b \}$ be at the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ .Let $\pmb { g }$ be a function in $\mathcal { C } [ a , b ]$ such that the error function

$$
d ^ { * } ( x ) = g ( x ) - q ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

also has exactly $( n + 1 )$ zeros, where $q ^ { * }$ is the best $L _ { 1 }$ approximation from $\mathcal { A }$ to ${ \pmb g }$ . Let these zeros be at the points $\{ \eta _ { i } ; i = 0 , 1 , \ldots , n \}$ ,and let $t ^ { * }$ be the function

$$
t ^ { * } ( x ) = \left\{ \begin{array} { c c } { - 1 , } & { g ( x ) < q ^ { * } ( x ) } \\ { 0 , } & { g ( x ) = q ^ { * } ( x ) } \\ { 1 , } & { g ( x ) > q ^ { * } ( x ) , } \end{array} \right. \quad a \leqslant x \leqslant b .
$$

We have to show that the sets $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ and $\{ \eta _ { i } ; i = 0 , 1 , \ldots , n \}$ are the same. The method of proof depends on the Haar condition, and on the fact that Theorem 14.1 gives the equations

$$
\int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x = \int _ { a } ^ { b } t ^ { * } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { A } .
$$

We also require two consequences of Theorem 14.2, namely that the error functions (14.24) and (14.27) both change sign at their zeros,and that $e ^ { * } ( a )$ and $d ^ { * } ( a )$ are both non-zero.

We assume without loss of generality that $\xi _ { 0 } \leqslant \eta _ { 0 }$ ,and that the signs of $e ^ { * } ( a )$ and $d ^ { * } ( a )$ are the same. Because of property (2) of Section 7.3, we may let $\pmb { p }$ be a function in $\mathcal { A }$ that changes sign at the points $\{ \xi _ { i } ; i =$ $1 , 2 , \ldots , n \}$ ,and that has no other zeros.We choose the overall sign of $p$ so that the signs of $p ( a )$ and $e ^ { * } ( a )$ are opposite. We consider the equation

$$
\int _ { a } ^ { b } [ s ^ { * } ( x ) - t ^ { * } ( x ) ] p ( x ) \mathrm { d } x = 0 ,
$$

which follows from condition (14.29). The sign of the integrand is important. Our assumptions imply that $[ s ^ { * } ( x ) - t ^ { * } ( x ) ]$ is zero when $\pmb { x }$ is in the interval $[ a , \xi _ { 0 } )$ . Further, in the range $( \xi _ { 0 } , b ]$ ,the product $s ^ { * } ( x ) p ( x )$ is positive,except on a set of measure zero,namely the poit set $\{ \xi _ { i }$ ； $i = 1 , 2 , \ldots , n \}$ .Moreover,the definitions (14.2) and (14.28) show that,if $s ^ { * } ( x ) p ( x )$ is positive, then the product $[ s ^ { * } ( x ) - t ^ { * } ( x ) ] p ( x )$ is non-negative. By combining all these remarks, we deduce that the inequality

$$
[ s ^ { * } ( x ) - t ^ { * } ( x ) ] p ( x ) \geqslant 0 , \qquad a \leqslant x \leqslant b ,
$$

is satisfied. It follows from equation (14.30) that the function $\{ \pmb { s } ^ { * } ( \pmb { x } ) -$ $t ^ { * } ( x )$ ； $a \leqslant x \leqslant b $ is zero almost everywhere. Therefore the sets $\{ \xi _ { i }$ ； $i = 0 , 1 , \ldots , n \}$ and $\{ \eta _ { i } ; i = 0 , 1 , \ldots , n \}$ are the same.□

This theorem provides the main method for calculating best $\mathbf { { { L } } _ { 1 } }$ approximations to continuous functions. One begins by assuming that the error function will change sign only $( n + 1 )$ times. In this case, because the zeros of the error function are independent of $f ,$ they may be found by detailed consideration of $\mathcal { A } .$ An approximation from $\mathscr { A }$ to $f$ is calculated by interpolation at these zeros,and then a check is made to find out if its error function satisfies the assumption. If the assumption holds, then the required approximation has been found.Otherwise a more elaborate approximation algorithm is necessary, for example a linear programming method of the type that is described in Section 15.4. The interpolation points for the case when $\mathcal { A }$ is the space ${ \mathcal P _ { n } }$ are given in the next section. Some applications of this method are given in Chapters 15 and 24.

# 14.4 The $\pmb { L _ { 1 } }$ interpolation points for algebraic polynomials

In order to apply the algorithm for calculating best $L _ { 1 }$ approximations, that is described in the previous paragraph, it is necessary to identify the interpolation points that are the subject of Theorem 14.4. The interpolation points for the important special case when $\mathcal { A }$ is the space $\mathcal { P } _ { n }$ are given in the next theorem.

# Theorem 14.5

Let the conditions of Theorem 14.4 be satisfied, where $\mathscr { A }$ is the space $\mathcal { P } _ { n } ,$ ,and where $[ a , b ]$ is the interval [-1,1]. Then the zeros of the error function

$$
e ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad - 1 \leqslant x \leqslant 1 ,
$$

have the values

$$
\xi _ { i } = \cos \bigg [ \frac { ( n + 1 - i ) \pi } { n + 2 } \bigg ] , \qquad i = 0 , 1 , \ldots , n .
$$

Proof. Theorem 14.2 implies that the error function (14.32) changes sign at its zeros. Therefore, because of the characterization theorem 14.1, it is sufficient to prove that the equation

$$
\int _ { - 1 } ^ { 1 } s ^ { * } ( x ) p ( x ) \mathrm { d } x = 0
$$

holds for all polynomials $p$ in $\mathcal { P } _ { n }$ where $s ^ { * }$ is the sign function

$$
s ^ { * } ( x ) = \left\{ \begin{array} { l l } { 1 , } & { - 1 < x < \xi _ { 0 } } \\ { ( - 1 ) ^ { i } , } & { \xi _ { i - 1 } < x < \xi _ { i } , \quad \quad i = 1 , 2 , \ldots , n , } \\ { ( - 1 ) ^ { n + 1 } , } & { \xi _ { n } < x < 1 } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

The numbers $s ^ { * } ( - 1 )$ and $s ^ { * } ( 1 )$ are defined to be zero,in order that the function

$$
\sigma ( \theta ) = s ^ { * } ( \cos \theta ) , \qquad 0 \leqslant \theta \leqslant \pi ,
$$

satisfes some periodicity conditions. We extend $\sigma$ to the infinite range by defining $\left\{ \sigma ( - \theta ) = - \sigma ( \theta ) ; 0 \leqslant \theta \leqslant \pi \right\}$ ,and by letting $\pmb { \sigma }$ be a $2 \pi$ -periodic function. It follows from equations (14.33) and (14.35) that the graph of $\{ \sigma ( \theta ) ; \ - \infty < \theta < \infty \}$ is a square wave that changes sign when $\pmb \theta$ is any integral multiple of $\pi / ( n + 2 )$ .Hence the condition

$$
\sigma \bigg ( \theta + \frac { \pi } { n + 2 } \bigg ) = - \sigma ( \theta ) , \qquad - \infty < \theta < \infty ,
$$

is obtained.

It will be shown that, if the change of variables $\left\{ x = \cos \theta ; 0 \leqslant \theta \leqslant \pi \right\}$ is made in the integral (14.34), then condition (14.37) enables equation (14.34) to be proved when $p$ is any one of the Chebyshev polynomials

$$
T _ { j } ( x ) = \cos { ( j \cos ^ { - 1 } x ) } , \qquad - 1 \leqslant x \leqslant 1 , \qquad j = 0 , 1 , \ldots , n .
$$

Because these polynomials are a basis of $\mathcal { P } _ { n }$ , we complete the proof of the theorem by establishing the equations

$$
\int _ { - 1 } ^ { 1 } s ^ { * } ( x ) T _ { j } ( x ) \mathrm { d } x = 0 , \qquad j = 0 , 1 , \dots , n .
$$

The identity

$$
\begin{array} { l } { \displaystyle \int _ { - 1 } ^ { 1 } s ^ { * } ( x ) T _ { i } ( x ) \mathrm { d } x = \int _ { 0 } ^ { \pi } s ^ { * } ( \cos \theta ) \cos \left( j \theta \right) \sin \theta \mathrm { d } \theta } \\ { = \frac { 1 } { 2 } \displaystyle \int _ { 0 } ^ { \pi } \sigma ( \theta ) \{ \sin \left[ ( j + 1 ) \theta \right] - \sin \left[ ( j - 1 ) \theta \right] \} \mathrm { d } \theta } \\ { = \frac { 1 } { 4 } \displaystyle \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \{ \sin \left[ ( j + 1 ) \theta \right] - \sin \left[ ( j - 1 ) \theta \right] \} \mathrm { d } \theta } \end{array}
$$

is satisfied, where the last line depends on the fact that $\pmb { \sigma }$ is an odd function. Therefore it is sufficient to show that the integrals

$$
I _ { k } = \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \sin \left( k \theta \right) \mathrm { d } \theta , \qquad k = 0 , 1 , \ldots , n + 1 ,
$$

are zero.We use the periodicity of the integrand of $I _ { k }$ ，then condition (14.37),and then the fact that $\pmb { \sigma }$ is odd, to deduce the equation

$$
\begin{array} { l } { { I _ { k } = \displaystyle { \int _ { - \pi } ^ { \pi } \sigma \Big ( \theta + \frac { \pi } { n + 2 } \Big ) \sin \left[ k \Big ( \theta + \frac { \pi } { n + 2 } \Big ) \right] \mathrm { d } \theta } } } \\ { { \displaystyle { \quad = - \cos \left( \frac { k \pi } { n + 2 } \right) \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \sin \left( k \theta \right) \mathrm { d } \theta } } } \\ { { \displaystyle { \qquad - \sin \left( \frac { k \pi } { n + 2 } \right) \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \cos \left( k \theta \right) \mathrm { d } \theta } } } \\ { { \displaystyle { \quad = - \cos \left( \frac { k \pi } { n + 2 } \right) I _ { k } , \qquad k = 0 , 1 , \dots , n + 1 . } } } \end{array}
$$

Because the factor $- \cos { [ k \pi / ( n + 2 ) ] }$ is not equal to one, it follows that $I _ { k }$ is zero,which gives the required result.□

We note that the points (14.33) are the abscissae of the extrema of the Chebyshev polynomial $T _ { n + 2 }$ . We note also that the extension of Theorem 14.5,to the case when the range of the variable is $[ a , b ] ,$ is that the zeros of the error function occur at the points

$$
\xi _ { i } = \textstyle { \frac { 1 } { 2 } } ( a + b ) + \textstyle { \frac { 1 } { 2 } } ( b - a ) \cos { \left[ \frac { ( n + 1 - i ) \pi } { n + 2 } \right] } , \qquad i = 0 , 1 , \ldots , n .
$$

Therefore the polynomial in $\mathcal { P } _ { n }$ that minimizes the $L _ { 1 }$ error

$$
\int _ { a } ^ { b } \left| f ( x ) - p ( x ) \right| \mathrm { d } x , \qquad p \in \mathcal { P } _ { n } ,
$$

may be calculated by satisfying the conditions $\{ p ( \xi _ { i } ) = f ( \xi _ { i } ) ; \ i = 0 , 1 ,$ $\cdots , n \}$ ， provided that the error function of the resultant approximation changes sign just at the interpolation points.

# 14 Exercises

14.1 Find the best $L _ { 1 }$ approximation to the function $\{ f ( x ) = x ^ { 3 }$ ； $1 \leqslant$ $x \leqslant 2 \}$ by a multiple of the quadratic polynomial $\{ p ( x ) = x ^ { 2 }$ ； $1 \leqslant x \leqslant 2 \}$ in the following two different ways. Firstly calculate the integral

$$
\eta ( a ) = \int _ { 1 } ^ { 2 } \left| x ^ { 3 } - a x ^ { 2 } \right| \mathrm { d } x
$$

analytically,and obtain the required value of $^ { a }$ from the equation $\eta ^ { \prime } ( a ) = 0$ . Secondly calculate the number $^ { b }$ such that the integral of the function $\{ x ^ { 2 } \sin { ( b - x ) } ; 1 \leqslant x \leqslant 2 \}$ is zero. You should find that $b = a$

14.2 Let $\mathcal { A }$ be the three-dimensional linear space of functions in $\mathcal { C } [ - 1 , 1 ]$ that are composed of two straight line segments that join at $x = 0$ .In other words $\mathcal { A }$ is the space of splines of degree one that have only one interior knot,at the point $x = 0$ . Calculate the element of $\mathcal { A }$ that minimizes the integral

$$
\int _ { - 1 } ^ { 1 } \left| x ^ { 2 } - p ( x ) \right| \mathrm { d } x , \qquad p \in \mathcal { A } .
$$

14.3 Let $\mathscr { A }$ be the one-dimensional linear space that contains al multiples of the function $\{ p ( x ) = x - c ; - 1 \leqslant x \leqslant 1 \}$ where $^ { c }$ is a constant. Prove that,if $^ { c }$ is non-zero, then each function in $\mathcal { C } [ - 1 , 1 ]$ has only one best $L _ { 1 }$ approximation in $\mathcal { A }$

14.4 Let $\mathscr { A }$ be the two-dimensional linear subspace of $\mathcal { C } [ 0 , 1 ]$ that is spanned by the functions $\{ \phi _ { 0 } ( x ) = 1$ ； $0 \leqslant x \leqslant 1 \}$ and $\smash { \{ \phi _ { 1 } ( x ) = x ^ { 2 } \} }$ ； $0 \leqslant x \leqslant 1 \}$ . Calculate the points $\xi _ { 0 }$ and $\xi _ { 1 }$ such that, if $p ^ { * } \in \mathcal A ,$ if $f \in { \mathcal { C } } [ 0 , 1 ] .$ ,and if the error function $e ^ { * } { = } f { - } p ^ { * }$ changes sign just at the points $\xi _ { 0 }$ and $\xi _ { 1 }$ , then $p ^ { * }$ is the best $L _ { 1 }$ approximation to $f$ from $\mathcal { A }$ 、Hence show that the least value of the integral

$$
\int _ { 0 } ^ { 1 } \left| x - p ( x ) \right| \mathrm { d } x , \qquad p \in \mathcal { A } ,
$$

is equal to $\scriptstyle { \frac { 1 } { 4 } } ( { \sqrt { 5 } } - 2 )$

14.5 Let $\mathscr { A }$ be the set of monic polynomials in $\mathcal { P } _ { n + 1 }$ ， which means that the coefficient of $x ^ { n + 1 }$ is one,and let the range of the variable be[-1,1].Deduce from Theorem 14.5 that the norm $\{ \| p \| _ { 1 } ; p \in \mathcal { A } \}$ is least when $p$ is the function $\{ p ( x ) = T _ { n + 2 } ^ { \prime } ( x ) / [ 2 ^ { n + 1 } ( n + 2 ) ]$ $- 1 \leqslant x \leqslant 1 \}$ . Hence obtain the bound

$$
\| p \| _ { 1 } \geqslant 2 ^ { - n } , \qquad p \in { \mathcal { A } } ,
$$

and verify that it is correct by applying Theorem 14.5 directly in the case when $n = 1$

14.6 Let $f$ be a function in $\mathcal { C } [ - 1 , 1 ]$ that is identically zero on the intervals $[ - 1 , - c ]$ and $[ c , 1 ] ,$ , but that is positive on the interval $( - c , c )$ ，where $\pmb { c }$ is a positive constant. Prove that the zero function is a best $L _ { 1 }$ approximation from $\mathcal { P } _ { 2 }$ to $f$ if and only if $c \leqslant { \frac { 1 } { 4 } } ( { \sqrt { 5 - 1 } } )$

14.7 Let $p ^ { * }$ be the linear function $\{ p ^ { * } ( x ) = x ; - 1 \leqslant x \leqslant 1 \}$ ,and let $f$ be a function in $\mathcal { C } [ - 1 , 1 ]$ ，such that the error $\{ e ^ { * } ( x ) = f ( x ) -$ $p ^ { * } ( x )$ ； $- 1 \leqslant x \leqslant 1 \}$ changes sign just at the points $x = 0$ and $\pm 1 / \sqrt { 2 }$ . It follows from Theorem 14.5 that $p ^ { * }$ is the best $L _ { 1 }$ approximation to $f$ from $\mathcal { P } _ { 2 }$ .By choosing a suitable $f ,$ show that $p ^ { * }$ need not be a best $L _ { 1 }$ approximation to $f$ from the space of rational functions that is called $\boldsymbol { \bar { \mathcal { A } } } _ { 1 1 }$ in Exercise 10.1.

14.8 Let $\mathscr { A }$ be a finite-dimensional linear subspace of $\mathcal { C } ^ { ( 1 ) } [ a , b ]$ that satisfies the Haar condition， let $f$ be any fixed function in $\mathcal { C } ^ { ( 1 ) } [ a , b ] ,$ and let $p ^ { * }$ be the best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$ Prove that there exist positive constants $^ c$ and $^ d$ such that the inequality

$$
\| f - p \| _ { 1 } \geqslant \| f - p ^ { * } \| _ { 1 } + \operatorname* { m i n } { [ c \| p - p ^ { * } \| _ { 1 } ^ { 2 } , d \| p - p ^ { * } \| _ { 1 } ] }
$$

is satisfied for all $p \in { \mathcal { A } } .$ Show, however, that this condition need not be obtained if the function $f$ is continuous but not differentiable.

14.9 Let $q ^ { * }$ be the best $L _ { 1 }$ approximation from the space $\mathcal { Q } _ { n }$ of trigonometric polynomials to a function $f$ in $\mathcal { C } _ { 2 \pi }$ 、Show that the error function $( f - q ^ { * } )$ has at least $( 2 n + 2 )$ zeros in the interval $[ 0 , 2 \pi )$ . Further, show that, if the number of zeros in this interval is equal to $( 2 n + 2 )$ , then the spacing between adjacent zeros is constant.

14.10 Let the linear subspace $\mathscr { A }$ of $\mathcal { C } [ a , b ]$ be composed of splines of degree one whose knots are fixed. Prove that each function in $\mathcal { C } [ a , b ]$ has only one best $L _ { 1 }$ approximation in $\mathcal { A } .$

# An application of $\pmb { L _ { 1 } }$ approximation and the discrete case

# 15.1 A useful example of $\pmb { L _ { 1 } }$ approximation

A particular $L _ { 1 }$ approximation problem is solved in this section, in order to demonstrate the method of calculation when the number of sign changes of the error function is equal to the dimension of $\scriptstyle { \mathcal { A } } ,$ and in order to provide a result that is required in Section 15.2. The problem is to calculate the value of the expression

$$
\operatorname* { m i n } _ { b _ { 1 } , b _ { 2 } , \ldots , b _ { n } } \int _ { 0 } ^ { \pi } \left| x - \sum _ { k = 1 } ^ { n } b _ { k } \sin { ( k x ) } \right| \mathrm { d } x ,
$$

where the quantities $\left\{ b _ { k } ; k = 1 , 2 , \ldots , n \right\}$ are real parameters. We see that it is equivalent to finding the best $L _ { 1 }$ approximation to the function $\left\{ f ( x ) = x ; 0 \leqslant x \leqslant \pi \right\}$ from the $\pmb { n }$ -dimensional linear space $\mathcal { A } ,$ ，that is spanned by the functions $\left\{ \phi _ { k } ( x ) = \sin { ( k x ) } ; 0 \leqslant x \leqslant \pi ; k = 1 , 2 , \ldots , n \right\}$

We take the optimistic view that this problem can be solved by the procedure that is described at the end of Section 14.3.Therefore we seek points $\left\{ \xi _ { i } ; i = 1 , 2 , \ldots , n \right\}$ ,satisfying the conditions

$$
0 < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } < \pi ,
$$

such that the equation

$$
\int _ { 0 } ^ { \pi } s ^ { * } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { A } ,
$$

holds, where $\pmb { s } ^ { * }$ is the sign function

$$
s ^ { * } ( x ) = \left\{ \begin{array} { l l } { 1 , } & { 0 < x < \xi _ { 1 } } \\ { ( - 1 ) ^ { i } , } & { \xi _ { i } < x < \xi _ { i + 1 } , } \\ { ( - 1 ) ^ { n } , } & { \xi _ { n } < x < \pi . } \end{array} \right. \quad i = 1 , 2 , \ldots , n - 1
$$

Because the integrals (14.41) are zero,it is suitable to replace $\pmb { n }$ by $( n - 1 )$

in the definition of $\pmb { \sigma } _ { : }$ ， given in the proof of Theorem 14.5,and to let $\{ s ^ { * } ( x ) ; 0 \leqslant x \leqslant \pi \}$ be the function $\{ \sigma ( \theta ) ; 0 \leqslant \theta \leqslant \pi \}$ .Thus the values

$$
\xi _ { i } = i \pi / ( n + 1 ) , \qquad i = 1 , 2 , \ldots , n ,
$$

cause equation (15.3) to be satisfied.It follows that, if $p ^ { * }$ is an element of $\mathcal { A }$ that is defined by the interpolation conditions

$$
p ^ { * } ( \xi _ { i } ) = f ( \xi _ { i } ) = \xi _ { i } , \qquad i = 1 , 2 , \ldots , n ,
$$

and if the error function

$$
e ^ { * } ( x ) = x - p ^ { * } ( x ) , \qquad 0 \leqslant x \leqslant \pi ,
$$

has no other zeros in the open interval $( 0 , \pi )$ , where a double zero at any $\xi _ { i }$ would count as an extra zero,then $p ^ { * }$ is the approximation that provides the least value of expression (15.1).

In order to prove that the equations (15.6) have a solution, we recall, from the proof of Theorem 5.4, that it is sufficient to show that the zero function is the only element of $\mathscr { A }$ that vanishes at the interpolation points. If this condition is not satisfied, then an odd trigonometric polynomial of degree $\pmb { n }$ has $_ n$ zeros in the interval $( 0 , \pi )$ ,and therefore it has $( 2 n + 1 )$ zeros in $( - \pi , \pi )$ ，which is a contradiction. Hence the equation (15.6) defines $p ^ { * }$ uniquely. We now consider the number of zeros of the function (15.7).

We see that the first derivative of $e ^ { * }$ is an even trigonometric polynomial of degree at most $\pmb { n }$ .Therefore it is zero at not more than $\pmb { n }$ points of the open interval $( 0 , \pi )$ . Hence the error function itself has at most $( n + 1 )$ zeros in the closed interval $[ 0 , \pi ]$ .We know already, however, that $e ^ { * }$ is zero at the interpolation points and at $\scriptstyle x = 0$ . Therefore there are no extra zeros.It follows that the coefficients of the function $p ^ { * }$ in $\mathcal { A } ,$ , that is defined by the interpolation conditions (15.6),are the values of the parameters $\{ b _ { i } ; i = 1 , 2 , \ldots , n \}$ ,that minimize expression (15.1).

Next we make the very useful observation that there is no need to calculate the coefficients of $p ^ { * }$ .The reason is that equation(15.3),and the definitions of $\{ s ^ { * } ( x ) ; 0 \leqslant x \leqslant \pi \}$ and the interpolation points,give the identity

$$
\begin{array} { r l } & { \displaystyle \int _ { 0 } ^ { \pi } \left| x - p ^ { * } ( x ) \right| \mathrm { d } x = \left| \displaystyle \int _ { 0 } ^ { \pi } s ^ { * } ( x ) \big [ x - p ^ { * } ( x ) \big ] \mathrm { d } x \right| } \\ & { \quad \quad \quad = \displaystyle \left| \displaystyle \int _ { 0 } ^ { \pi } s ^ { * } ( x ) x \mathrm { d } x \right| . } \end{array}
$$

Therefore expression (15.1) has the value

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { \pi } \left. x - p ^ { * } ( x ) \right. \mathrm { d } x = \left. \sum _ { j = 0 } ^ { n } \left( - 1 \right) ^ { j } \int _ { j \pi / ( n + 1 ) } ^ { ( j + 1 ) \pi / ( n + 1 ) } x \mathrm { d } x \right. } \\ { \displaystyle \qquad = \pi ^ { 2 } / 2 ( n + 1 ) , } \end{array}
$$

which is the required result. This example shows that the interpolation procedure for calculating best $L _ { 1 }$ approximations can be used sometimes when $\mathcal { A }$ does not satisfy the Haar condition.

# 15.2 Jackson's first theorem

Equation (15.9) is important to the following question. Let $f$ be any function in $\mathcal { C } _ { 2 \pi }$ that is continuously differentiable; find the smallest number $c ( n )$ that satisfies the condition

$$
\operatorname* { m i n } _ { q \in \mathcal { Q } _ { n } } \| f - q \| _ { \infty } \leqslant c \left( n \right) \| f ^ { \prime } \| _ { \infty } ,
$$

and that is independent of $f ,$ where ${ \mathcal { Q } } _ { n }$ is the space of trigonometric polynomials of degree at most $\pmb { n }$ . In this section it is proved that $c ( n )$ has the value $\pmb { \pi } / 2 ( \pmb { n } + 1 )$ , which is ‘Jackson's first theorem'.We note that, if it is necessary to approximate $f$ by a trigonometric polynomial to given accuracy,and if the norm $\| f ^ { \prime } \| _ { \infty }$ is known, then the theorem gives an upper bound on the least value of $n$ that may be used. Usually, however, this upper bound is so high that it is of no practical value.Two reasons for studying Jackson's first theorem are that it shows a way of relating errors in function approximation to derivatives,and it is the basis of the work of the next chapter.

In order to relate $f$ to $f ^ { \prime }$ , when $f$ is in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) } ,$ we make use of the formula

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( \theta ) \operatorname { d } \theta + { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \theta f ^ { \prime } ( \theta + x + \pi ) \operatorname { d } \theta ,
$$

which may be verified by integration by parts. We require also the fact that, if $\pmb { g }$ is any function in $\mathcal { C } _ { 2 \pi } ,$ and if $q$ is any element of ${ \mathcal { Q } } _ { n }$ ,then the function

$$
\psi ( x ) = \int _ { - \pi } ^ { \pi } q ( \theta ) g ( \theta + x ) \mathrm { d } \theta , \qquad - \infty < x < \infty ,
$$

is also in ${ \mathcal { Q } } _ { n }$ . This statement holds because periodicity gives the equation

$$
\psi ( x ) = \int _ { - \pi } ^ { \pi } q ( \theta - x ) g ( \theta ) { \bf d } \theta ,
$$

and because $q ( \pmb \theta - \pmb x )$ may be expressed in the form

$$
q ( \theta - x ) = \frac { 1 } { 2 } a _ { 0 } ( \theta ) + \sum _ { j = 1 } ^ { n } a _ { j } ( \theta ) \cos { ( j x ) } + b _ { j } ( \theta ) \sin { ( j x ) } .
$$

In the proof of Jackson's theorem, which is given below, we let $\pmb { g }$ be the function

$$
g ( x ) = f ^ { \prime } ( x + \pi ) , \qquad - \infty < x < \infty .
$$

# Theorem 15.1 (Jackson I)

For allfunctions $f$ in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ and for all non-negative integers $\pmb { n }$ ,the inequality

$$
\operatorname* { m i n } _ { q \in { \mathcal { Q } } _ { n } } \| f - q \| _ { \infty } \leqslant { \frac { \pi } { 2 ( n + 1 ) } } \| f ^ { \prime } \| _ { \infty }
$$

is satisfied, where ${ \mathcal { Q } } _ { n }$ is the linear space of trigonometric polynomials of degree at most $\pmb { n }$

Proof. We express $f$ in the form (15.11). Because the first integral in this expression is independent of $\pmb { x } .$ ，and because the space ${ \mathcal { Q } } _ { n }$ includes constant functions, we just have to consider trigonometric approximations to the function

$$
{ \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \theta f ^ { \prime } ( \theta + x + \pi ) \mathrm { d } \theta , \qquad - \infty < x < \infty .
$$

Therefore,by using the remark that expression (15.12) is a trigonometric polynomial, we obtain the bound

$$
\begin{array} { r l } & { \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \left\| f - q \right\| _ { \infty } \leqslant \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \underset { x } { \operatorname* { m a x } } \left| \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \left[ \theta - q \left( \theta \right) \right] f ^ { \prime } \left( \theta + x + \pi \right) \mathrm { d } \theta \right| } \\ & { \quad \quad \quad \leqslant \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \left| \theta - q \left( \theta \right) \right| \mathrm { d } \theta \left\| f ^ { \prime } \right\| _ { \infty } , \quad \quad \quad \left( 1 \right) } \end{array}
$$

where the last line is elementary. Because the work of Section 15.1 gives the equation

$$
\operatorname* { m i n } _ { q \in \mathcal { Q } _ { n } } \int _ { - \pi } ^ { \pi } \left. \theta - q ( \theta ) \right. { \bf d } \theta = \frac { \pi ^ { 2 } } { \left( n + 1 \right) } ,
$$

it follows that Theorem 15.1 is true.

The factor $\pmb { \pi } / 2 ( \pmb { n } + 1 )$ that occurs in inequality (15.16) cannot be decreased. In order to prove this statement, we consider a function $f$ in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ that takes the values

$$
f ( j \pi / [ n + 1 ] ) = ( - 1 ) ^ { j } , \qquad j = 0 , \pm 1 , \pm 2 , \ldots .
$$

For any $\pmb \varepsilon > 0$ , it is possible to choose $f$ so that it also satisfies the condition

$$
\| f ^ { \prime } \| _ { \infty } { \leqslant } 2 ( n + 1 ) ( 1 + \varepsilon ) / \pi .
$$

We let $q ^ { * }$ be a best approximation from ${ \mathcal { Q } } _ { n }$ to $f .$ If the distance $\| f - q ^ { * } \| _ { \infty }$ is less than one,then equation (15.20) implies that the sign of $q ^ { * } ( j \pi / [ n + 1 ] )$ is the same as the sign of $( - 1 ) ^ { j }$ .Hence $q ^ { * }$ has a zero in each of the intervals $\{ [ ( j - 1 ) \pi / ( n + 1 ) , j \pi / ( n + 1 ) ] ; j = 1 , 2 , \ldots , 2 n + 2 \} ,$ .which is not possible because $q ^ { * }$ is in ${ \mathcal { Q } } _ { n }$ . It follows that the inequality

$$
\begin{array} { r l } { \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \| f - q \| _ { \infty } \geqslant 1 } & { } \\ { \geqslant \frac { \pi } { 2 ( n + 1 ) ( 1 + \varepsilon ) } \| f ^ { \prime } \| _ { \infty } } & { } \end{array}
$$

is satisfied. Therefore, because $\pmb \varepsilon$ can be arbitrarily small, Jackson's first theorem gives the least value of $c ( n )$ , that is independent of $f ,$ and that is such that inequality (15.1O） holds for all continuously differentiable functions in $\mathcal { C } _ { 2 \pi }$

# 15.3 Discrete $\pmb { L _ { 1 } }$ approximation

In data-fitting calculations,where the element of $\mathscr { A }$ that minimizes expression (14.3) is required, there is a characterization theorem that is similar to Theorem 14.1. It is stated in a form that allows different weights to be given to the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$

# Theorem 15.2

Let the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ ,and fixed positive weights $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ be given. Let $\mathscr { A }$ be a linear space of functions that are defined on the point set $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ Let $p ^ { * }$ be any element of $\scriptstyle { \mathcal { A } } ,$ let $\mathcal { Z }$ contain the points of $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ that satisfy the condition

$$
p ^ { * } ( x _ { t } ) = f ( x _ { t } ) ,
$$

and let $s ^ { * }$ be the sign function

$$
\begin{array} { r } { s ^ { * } ( x _ { t } ) = \left\{ \begin{array} { l l } { 1 , } & { f ( x _ { t } ) > p ^ { * } ( x _ { t } ) } \\ { 0 , } & { f ( x _ { t } ) = p ^ { * } ( x _ { t } ) } \\ { - 1 , } & { f ( x _ { t } ) < p ^ { * } ( x _ { t } ) , } \end{array} \right. \quad t = 1 , 2 , \ldots , m . } \end{array}
$$

Then $p ^ { * }$ is a function in $\mathcal { A }$ that minimizes the expression

$$
\sum _ { t = 1 } ^ { m }  w _ { t } | f ( x _ { t } ) - p ( x _ { t } ) | , \quad \quad p \in \mathcal { A } ,
$$

if and only if the inequality

$$
\biggl | \sum _ { t = 1 } ^ { m } w _ { t } s ^ { * } ( x _ { t } ) p ( x _ { t } ) \biggr | \leqslant \sum _ { x _ { t } \in \mathcal { Z } } w _ { t } \bigl | p ( x _ { t } ) \bigr |
$$

holds for all $p$ in $\mathscr { A }$

Proof. The method of proof is similar to the proof of Theorem 14.1. If condition (15.26) is not satisfied,we consider replacing the approximation $p ^ { * }$ by $( p ^ { * } + \theta p )$ , where $| \pmb \theta |$ is so small that, if $\scriptstyle { \pmb { x } } _ { t }$ is not in $\mathcal { Z } ,$ , the sign of $\{ f ( x _ { t } ) - p ^ { * } ( x _ { t } ) - \theta p ( x _ { t } ) \}$ is the same as the sign of $s ^ { * } ( x _ { t } )$ . It follows that the replacement changes the value of expression (15.25) by the amount

$$
- \theta \sum _ { t = 1 } ^ { m } w _ { t } s ^ { * } ( x _ { t } ) p ( x _ { t } ) + \theta \sum _ { x _ { t } \in \mathcal { X } } w _ { t } \big | p ( x _ { t } ) \big | .
$$

Therefore, if the left-hand side of expression (15.26) is larger than the right-hand side,one may choose the sign of $\pmb \theta$ so that $( p ^ { * } + \theta p )$ is a better approximation than $p ^ { * }$

Conversely,if condition (15.26) is obtained for all $p$ in $\mathcal { A } _ { : }$ ， then, by replacing the integrals in expression (14.15) by weighted sums, it follows that $p ^ { * }$ is a best discrete $L _ { 1 }$ approximation to the data.□

The following theorem shows that there is a function $p ^ { * }$ in $\mathcal { A }$ that minimizes expression (15.25),and that is such that the set $\mathcal { Z }$ of Theorem 15.2 contains at least $( n + 1 )$ points, where $( n + 1 )$ is the dimension of $\mathscr { A }$ Therefore many algorithms for calculating best discrete $L _ { 1 }$ approximations seek a set $\mathcal { Z }$ that allows an optimal function $p ^ { * }$ to be obtained by interpolation.

# Theorem 15.3

Let the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ and fixed positive weights $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ be given. Let $\mathcal { A }$ be a linear subspace of ${ \mathcal { R } } ^ { m }$ ， where the components of each vector $p$ in $\mathcal { A }$ have the values $\{ p ( x _ { t } ) ; t =$ $1 , 2 , \ldots , m \}$ . Then there exists an element $p ^ { * }$ in $\{ \mathcal { A } ,$ ，that minimizes expression (15.25),and that has the property that the zero vector is the only element $p$ in $\mathcal { A }$ that satisfies the conditions $\{ p ( x _ { t } ) = 0 ; x _ { t } \in \mathcal { X } \}$ ,where the set $\mathcal { Z }$ is defined in Theorem 15.2.

Proo0f.  Let $p ^ { * }$ be a best weighted $L _ { 1 }$ approximation from $\mathcal { A }$ to the data, but suppose that there exists a non-zero element $q$ in $\mathcal { A }$ that satisfies the condition

$$
q ( x _ { t } ) = 0 , \qquad x _ { t } \in \mathcal { X } .
$$

We consider the function

$$
\psi ( \theta ) = \sum _ { t = 1 } ^ { m } w _ { t } \big | f ( x _ { t } ) - p ^ { * } ( x _ { t } ) - \theta q ( x _ { t } ) \big | , \qquad - \infty < \theta < \infty ,
$$

where $\pmb \theta$ is a real variable. It is a continuous, piecewise linear function of $\theta _ { \mathrm { i } }$ that tends to infinity when $| \theta |$ becomes large,and that takes its least value when $\pmb \theta$ is zero, because $p ^ { * }$ is a best approximation. Moreover, equation (15.28) implies that two different line segments of $\psi$ do not join at $\pmb \theta = 0$ Therefore $\psi$ is constant in a neighbourhood of $\pmb \theta = 0$ If $\pmb \theta$ is increased from zero, then $\psi ( \theta )$ remains constant until a value of $\pmb \theta$ is reached that satisfies the conditions

$$
\left. { \begin{array} { l } { f ( x _ { t } ) - p ^ { * } ( x _ { t } ) - \theta q ( x _ { t } ) = 0 } \\ { q ( x _ { t } ) \neq 0 } \end{array} } \right\}
$$

for some value of $t .$ Let this value of $\pmb \theta$ be ${ \bar { \theta } } .$ Because $\psi ( { \overline { { \theta } } } )$ is equal to $\psi ( 0 )$ ， the function $( p ^ { * } + { \bar { \theta } } q )$ is another best weighted $L _ { 1 }$ approximation from $\mathscr { A }$ to the data. Equation (15.28) implies that the residuals $\{ f ( x _ { t } ) -$ $( p ^ { * } + \bar { \theta } q ) ( x _ { t } ) ; x _ { t } \in \mathcal { Z } \}$ are zero.Further,another zero residual is obtained from the first line of expression (15.30). Hence our construction increases the number of zeros of a best approximation. Because the construction can be applied recursively,it follows that the theorem is true.□

This theorem shows that the calculation of a best discrete $L _ { 1 }$ approximation can be regarded as a search for suitable interpolation points in the set of data points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ . A systematic method of searching is needed,and also it is necessary to test whether a trial set of interpolation points gives a best approximation.The condition (15.26) is not suitable in practice,because it has to be satisfied for every element of ${ \mathcal { A } } .$ All of these problems can be solved quite routinely, because the complete calculation is a linear programming problem.

# 15.4 Linear programming methods

In order to show that the best discrete $L _ { 1 }$ approximation calculation is a linear programming problem, we let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a basis of the space $\mathcal { A }$ of approximations,and we write the expression (15.25), whose least value is required, in the form

$$
\sum _ { t = 1 } ^ { m }  w _ { t } | f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) | ,
$$

where the parameters $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ are some of the variables of the linear programming calculation.We also introduce two new variables for each data point,which we call $\{ u _ { t } ; t = 1 , 2 , \ldots , m \}$ and $\{ v _ { t } ; t = 1 , 2$ ， $\dots , m \}$ . They have to satisfy both the non-negativity conditions

$$
\begin{array} { r } { u _ { t } \geqslant 0 } \\ { v _ { t } \geqslant 0 } \end{array} , \qquad t = 1 , 2 , \ldots , m ,
$$

and the bounds

$$
- v _ { t } \leqslant f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) \leqslant u _ { t } , \qquad t = 1 , 2 , \ldots , m .
$$

Therefore,if, for any values of the coefficients $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ ,the variables $\pmb { u } _ { t }$ and $v _ { t }$ are chosen to minimize the sum $\left( u _ { t } + v _ { t } \right)$ ， then the equation

$$
u _ { t } + v _ { t } = \left| f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) \right|
$$

is satisfied. It follows that we require the least value of the expression

$$
\sum _ { t = 1 } ^ { m } w _ { t } ( u _ { t } + v _ { t } ) ,
$$

subject to the constraints (15.32） and (15.33) on the values of the variables $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \} , \{ u _ { t } ; t = 1 , 2 , \ldots , m \}$ and $\{ v _ { t } ; t = 1 , 2 ,$ $\cdots , m \}$ ,which is a linear programming calculation.

Because the use of a general linear programming procedure is less efficient than one that is adapted to the calculation of the last paragraph,it is helpful to think of the linear programming method geometrically. The constraints define a convex polyhedron of feasible points in the space of the variables,and there is a solution to the calculation at a vertex of the polyhedron. The characteristic properties of a vertex are that it is feasible, and it is on the boundary of as many linearly independent constraints as there are variables, namely $( 2 m + n + 1 )$ . Because each of the variables $\{ u _ { t } ; t = 1 , 2 , \ldots , m \}$ and $\{ v _ { t } ; t = 1 , 2 , \ldots , m \}$ has to occur in at least one of the independent constraints, the equations

$$
\begin{array} { l } { { u _ { t } = \displaystyle \operatorname* { m a x } \left[ 0 , f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) \right] \Bigg \} } } \\ { { v _ { t } = \displaystyle \operatorname* { m a x } \left[ 0 , \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) - f ( x _ { t } ) \right] \Bigg ) , } } \end{array} \quad t = 1 , 2 , \ldots , m ,
$$

are satisfied at every vertex.The remaining $( n + 1 )$ constraints that hold as equations have the form

$$
f ( x _ { t } ) = \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) , \qquad t \in \mathcal { T } ,
$$

where $\mathcal { T }$ is a subset of the integers $\left\{ 1 , 2 , \ldots , m \right\}$ . Because $\mathcal { T }$ contains $( n + 1 )$ elements,and because the constraints that define a vertex are linearly independent, we have another explanation of Theorem 15.3.

At the beginning of an iteration of the simplex method for solving a linear programming calculation, the variables are set to the coordinates of a vertex of the polyhedron. If it is not possible to reduce the function (15.35) by moving along one of the edges of the polyhedron that meet at the vertex, then the current values of the variables $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ are the ones that minimize the function (15.31). Thus there is a test for optimality which is more useful than condition (15.26),because it depends on a finite number of inequalities.

An edge of the polyhedron is defined to be in the intersection of the boundaries of $( 2 m + n )$ linearly independent constraints. One way of generating an edge from a vertex is to give up one of the conditions (15.36),but these edges are irrelevant because they always lead to increases in the objective function (15.35).Therefore we have to consider only edges that satisfy expression (15.36),and that are defined by $\pmb { n }$ independent equations from the system (15.37). We let $\mathcal { T } _ { \mathtt { E } }$ be the set of indices of the independent equations. Hence $\mathcal { T } _ { \mathtt { E } }$ is a subset of $\mathcal { T } .$ Except for a constant scaling factor， there is a unique non-trivial solution $\{ \bar { \lambda } _ { i } ; i = 0 , 1 , \ldots , n \}$ to the conditions

$$
\sum _ { i = 0 } ^ { n } \bar { \lambda } _ { i } \phi _ { i } ( x _ { t } ) = 0 , \qquad t \in \mathcal { T } _ { \mathsf { E } } .
$$

If $\{ \lambda _ { i } = \hat { \lambda } _ { i } ; i = 0 , 1 , \ldots , n \}$ is the solution of the system (15.37), then, at a general point on the edge, the equations $\left\{ \lambda _ { i } = \hat { \lambda } _ { i } + \alpha \bar { \lambda } _ { i } \right.$ ； $i = 0 , 1 , \ldots , n \}$ are obtained,where $\pmb { \alpha }$ is a real parameter. Moreover,the objective function (15.35) has the value

$$
\psi ( \alpha ) = \sum _ { t = 1 } ^ { m } w _ { t } \bigg | f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } ( \hat { \lambda } _ { i } + \alpha \bar { \lambda } _ { i } ) \phi _ { i } ( x _ { t } ) \bigg | .
$$

Suppose that, at the vertex where equations (15.36) and(15.37) hold, it is found that the objective function is reduced if a move is made along the edge that is defined by equations (15.36) and (15.38). The far end of the edge in the $( 2 m + n + 1 )$ -dimensional space of the variables is reached when one of the terms $\{ f ( x _ { t } ) - \sum \lambda _ { i } \phi _ { i } ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ in expression (15.36) changes sign.At this point the term that changes sign is zero. Hence another interpolation condition of the form (15.37) is satisfied, which implies that the point is another vertex of the polyhedron. A standard linear programming procedure would have to begin a new iteration at this vertex. However, because our purpose is to make the function (15.31) as smallas possible, it is sensible to continue to change $_ { \alpha }$ until the function (15.39) reaches its least value. Hence we are searching along a locus that is composed of straight line segments in the space of the variables.Because the optimal point on the locus is also a vertex of the polyhedron of feasible points,all other features of the standard simplex method can be retained. The technique of choosing $\pmb { \alpha }$ to minimize expression (15.39) on every iteration can provide large gains in effciency, especially when the linear programming calculation is obtained by discretizing the continuous problem that is studied in Chapter 14.

One reason for discretizing a continuous problem is that it may not be possible to minimize expression (14.1) by the method that is described at the end of Section 14.3, because the error function of the best approximation may have too many zeros.A standard technique in this case is to apply a linear programming procedure to minimize the sum (15.31) instead,where the weights $\{ w _ { t } ; t = 1 , 2 , \dots , m \}$ and the data points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ are chosen so that expression (15.31) is an adequate approximation to the integral (14.1). It is not appropriate to use a high order integration formula, because the integrand has first derivative discontinuities,and because the discretization forces $( n + 1 )$ zeros of the final error function $\left\{ f ( x ) - p ( x ) ; a \leqslant x \leqslant b \right\}$ to be in the point set $\{ x _ { t } ; t =$ $1 , 2 , \ldots , m \}$ . Therefore usually $_ m$ has to be large.

An extension of this linear programming method provides a useful algorithm that can be applied directly to the minimization of the continuous $L _ { 1 }$ distance function (14.1). It comes from the remark that, in the linear programming procedure,expression (15.39) can be replaced by the integral

$$
\int _ { a } ^ { b } \Big | f ( x ) - \sum _ { i = 0 } ^ { n } \big ( \hat { \lambda } _ { i } - \alpha \bar { \lambda } _ { i } \big ) \phi _ { i } ( x ) \Big | \mathrm { d } x ,
$$

in order to determine the value of $\pmb { \alpha }$ that is most appropriate to the continuous calculation. Each iteration begins with a trial approximation, $\pmb { \hat { p } }$ say, to $f ,$ that has the property that the set

$$
{ \mathcal { L } } = \{ x : f ( x ) = { \hat { p } } ( x ) ; a \leqslant x \leqslant b \}
$$

contains at least $\pmb { n }$ points.A subset $\mathcal { L } _ { \mathrm { E } }$ is chosen that is composed of exactly $\pmb { n }$ points of $\mathscr { Z }$ and $\bar { p }$ is defined to be a non-zero function in $\mathscr { A }$ that satisfies the equations $\{ \bar { p } ( x ) = 0 ; x \in \mathcal { X } _ { \mathrm { E } } \}$ .The iteration replaces $\pmb { \hat { p } }$ by $\left( \hat { p } + \alpha \bar { p } \right)$ ，where $\pmb { \alpha }$ has the value that minimizes the norm $\| f - \hat { p } - \alpha \bar { p } \| _ { 1 }$ ， which is equal to expression (15.4O). Then another iteration is begun. Most of the details are taken from the linear programming method that has been described already, but an important difference is the need to evaluate integrals. It is therefore worth noting that, because the calculation of $_ \alpha$ is itself an $L _ { 1 }$ approximation problem, the required value depends only on integrals of $\bar { p }$ and on the sign properties of the error function $\left( f - \hat { p } - \alpha \bar { p } \right)$ . Exercise 15.6 gives an example of the use of this algorithm.

# 15 Exercises

15.1Let $f$ be the function in $\mathcal { C } _ { 2 \pi }$ that takes the values $\{ f ( x ) = x$

$- { \scriptstyle { \frac { 1 } { 2 } } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ and $\{ f ( x ) = \pi - x ; { \frac { 1 } { 2 } } \pi \leqslant x \leqslant { \frac { 3 } { 2 } } \pi \}$ . Prove that the equation

$$
\operatorname* { m i n } _ { q \in { \mathcal { Q } } _ { 1 } } \int _ { 0 } ^ { 2 \pi } { \big | } f ( x ) - q ( x ) { \big | } \mathrm { d } x = \pi ^ { 2 } / 1 8
$$

is satisfied.

15.2 Deduce directly from expressions (15.18) and (15.19) that the term ${ \frac { 1 } { 2 } } \pi / ( n + 1 )$ that occurs in inequality (15.16) is optimal.

15.3 Let $\mathscr { A }$ be any linear space of functions that are defined on the point set $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ ,where the dimension of $\mathscr { A }$ is less than m. Prove that there exist function values $\{ f ( x _ { t } ) ; t = 1 , 2 ,$ $\cdots , m \}$ and positive weights $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ such that more than one element of $\mathscr { A }$ minimizes expression (15.25). Construct an example of non-uniqueness of best discrete $L _ { 1 }$ approximations in the case when $\mathscr { A }$ is the space $\mathcal { P } _ { 2 }$

15.4 The polynomial $\{ p ( x ) = 1 6 x - { x ^ { 2 } } ; 1 \leqslant x \leqslant 8 \}$ is one of several functions in $\mathcal { P } _ { 3 }$ that minimizes the expression

$$
\sum _ { i = 1 } ^ { 8 } \ w _ { i } \vert f ( x _ { i } ) - p ( x _ { i } ) \vert , \qquad p \in \mathcal { P } _ { 3 } ,
$$

where the data have the values $w _ { 1 } = w _ { 8 } = 1$ ， $w _ { 3 } = w _ { 6 } = w _ { 7 } = 2$ ， $w _ { 2 } = w _ { 4 } = w _ { 5 } = 3 ,$ $f ( 1 ) = 1 5$ ， $f ( 2 ) = 3 1$ ， $f ( 3 ) = 3 9$ ， $f ( 4 ) \dot { = } 4 6$ ， $f ( 5 ) = 5 8$ ， $f ( 6 ) = 6 0$ ， $f ( 7 ) = 6 2$ ，and $f ( 8 ) = 6 4$ . Find another function in $\mathcal { P } _ { 3 }$ that minimizes this expression.

15.5 The best $L _ { 1 }$ approximation in $\mathcal { P } _ { 1 }$ is required to the data $f ( 0 ) =$ $^ { - 3 5 }$ ， $f ( 1 ) = - 5 6$ ， $f ( 2 ) = 0$ ， $f ( 3 ) = - 1 6 ,$ ， $f ( 4 ) = - 3$ ， $f ( 5 ) = 4$ ， $f ( 6 ) = 1 0$ ， $f ( 7 ) = 5 3$ and $f ( 8 ) = 6 9$ ，where all the weights are equal to one.Calculate it by the method that is described in Section 15.4,where on the first iteration the only point of the set $\{ \boldsymbol { x } _ { t } ; t \in \mathcal { T } _ { \mathtt { E } } \}$ is $\scriptstyle x = 0$

15.6 Let the algorithm that is described in the last paragraph of Section 15.4 be applied to calculate the best $L _ { 1 }$ approximation from $\mathcal { P } _ { 1 }$ to the function $\{ f ( x ) = x ^ { 2 } ; - 1 \leqslant x \leqslant 1 \}$ Investigate the rate at which the zeros of the error function $\left( f - \hat { p } \right)$ converge to the points $\pm \frac { 1 } { 2 }$ that are given by Theorem 14.5.You should find that, if an iteration adjusts a zero to $\left( { \frac { 1 } { 2 } } + \varepsilon \right)$ ,where $\pmb \varepsilon$ is small, then, when the zero is adjusted again two iterations later, the difference between its new value and $\textstyle { \frac { 1 } { 2 } }$ is of order $\pmb { \varepsilon } ^ { 4 }$

15.7 Theorem 15.3 does not have an analogue in the continuous case. Prove this remark by finding a finite-dimensional linear subspace $\mathscr { A }$ of $\mathcal { C } [ a , b ] ,$ and a function $f$ in $\mathcal { C } [ a , b ]$ , such that every best $L _ { 1 }$ approximation from $\mathscr { A }$ to $f$ has fewer than $( n + 1 )$ zeros,where $( n + 1 )$ is the dimension of $\pmb { \mathcal { A } }$

15.8Let the function values $\{ f ( x _ { i } ) = f ( i ) ; i = 0 , 1 , 2 , 3 , 4 \}$ be given, and let $p ^ { * }$ be a polynomial in $\mathcal { P } _ { 2 }$ that minimizes the expression

$$
\sum _ { i = 0 } ^ { 4 } | f ( i ) - p ( i ) | , \qquad p \in \mathscr { P } _ { 2 } .
$$

Prove that $p ^ { * } ( 0 )$ and $p ^ { * } ( 4 )$ are equal to $f ( 0 )$ and $f ( 4 )$ respectively.

15.9 Let $\boldsymbol { \bar { \mathcal { A } } } _ { 0 , 1 }$ be the set of functions in $\mathcal { C } [ - 1 , 4 ]$ that have the form $\{ \alpha / ( 1 + \beta x ) ; - 1 \leqslant x \leqslant 4 \}$ ，where $\pmb { \alpha }$ and $\beta$ are real parameters.

Calculate the function $p ^ { * }$ that minimizes the weighted sum

$$
\begin{array} { r } { \big \vert 9 - p ( - 1 ) \big \vert + M \big \vert 8 - p ( 0 ) \big \vert + \big \vert 4 - p ( 4 ) \big \vert , \qquad p \in \bar { \mathcal { A } } _ { 0 , 1 } , } \end{array}
$$

where the weight $M$ is so large that the condition $p ^ { * } ( 0 ) = 8$ is obtained. The purpose of this exercise is to show that Theorem 15.3 does not extend to rational approximation on a discrete point set.

15.10Investigate the convergence properties of the algorithm that is described in the last paragraph of Section 15.4, in the case when the choice of $\mathcal { Z } _ { \mathrm { E } }$ is governed by the rule that no point shall remain in $\mathcal { L } _ { \mathrm { E } }$ for more than $_ n$ iterations. You may assume that all functions are continuously differentiable,that $\mathscr { A }$ satisfies the Haar condition,and that every error function that is calculated has exactly $( n + 1 )$ zeros.

# The order of convergence of polynomial approximations

# 16.1 Approximations to non-differentiable functions

In the first three sections of this chapter we consider the error of the best minimax approximation from ${ \mathcal { Q } } _ { n }$ 'to a function $f$ in $\mathcal { C } _ { 2 \pi } .$ Specifically we study the dependence on $\pmb { n }$ of the number

$$
\operatorname* { m i n } _ { q \in { \mathcal { Q } } _ { n } } \| f - q \| _ { \infty } = E _ { n } ( f ) ,
$$

say. Section 16.4 extends the work to best minimax approximations from $\mathcal { P } _ { n }$ to functions in $\mathcal { C } [ - 1 , 1 ]$ .Most of the theory depends on the bound

$$
E _ { n } ( f ) \leqslant \frac { \pi } { 2 ( n + 1 ) } \| f ^ { \prime } \| _ { \infty } , \qquad f \in \mathcal { C } _ { 2 \pi } ^ { ( 1 ) } ,
$$

which is given in Theorem 15.1. The purpose of this section is to show that, by elementary analysis, one can deduce from inequality (16.2) some bounds on $E _ { n } ( f )$ ,that hold when $f$ is non-differentiable.

The technique that is used depends on a differentiable function that is close to $f .$ We let $\pmb { \delta }$ be a small positive number, and we let $\phi$ be the function

$$
\phi \left( x \right) = { \frac { 1 } { 2 \delta } } \int _ { x - \delta } ^ { x + \delta } f ( \theta ) { \mathrm { d } } \theta , \qquad - \infty < x < \infty ,
$$

which is in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ for any $f$ in $\mathcal { C } _ { 2 \pi }$ . The derivative of $\phi$ has the value

$$
\phi ^ { \prime } ( x ) = { \frac { 1 } { 2 \delta } } [ f ( x + \delta ) - f ( x - \delta ) ] , \qquad - \infty < x < \infty ,
$$

and $\phi$ tends to $f$ if $\pmb { \delta }$ tends to zero. The proof of the following theorem depends on both of these properties.

Theorem 16.1 (Jackson II)

Let $f$ be a function in $\mathcal { C } _ { 2 \pi }$ that satisfies the Lipschitz condition

$$
\big | f ( x _ { 1 } ) - f ( x _ { 0 } ) \big | \leqslant M | x _ { 1 } - x _ { 0 } | ,
$$

for all real numbers $x _ { 1 }$ and $x _ { 0 }$ ，where $M$ is a constant. Then expression (16.1) is bounded by the inequality

$$
E _ { n } ( f ) \leqslant \pi M / 2 ( n + 1 ) .
$$

Proof. For every function $\phi$ in $\mathcal { C } _ { 2 \pi }$ the inequality

$$
\begin{array} { r l } & { { E } _ { n } ( f ) \leqslant \| f - q ^ { * } \| _ { \infty } } \\ & { \qquad \leqslant \| f - \phi \| _ { \infty } + \| \phi - q ^ { * } \| _ { \infty } } \\ & { \qquad = \| f - \phi \| _ { \infty } + { E } _ { n } ( \phi ) } \end{array}
$$

is satisfied, where $q ^ { * }$ is the best approximation from ${ \mathcal { Q } } _ { n }$ to $\phi$ . We let $\phi$ be the function (16.3). Therefore condition (16.5) gives the bound

$$
\begin{array} { l } { \displaystyle \| f - \phi \| _ { \infty } = \operatorname* { m a x } _ { \boldsymbol { x } } \frac { 1 } { 2 \delta } \left| \int _ { \boldsymbol { x } - \delta } ^ { \boldsymbol { x } + \delta } f ( \boldsymbol { x } ) - f ( \theta ) \mathrm { d } \theta \right| } \\ { \displaystyle \leqslant \operatorname* { m a x } _ { \boldsymbol { x } } \frac { M } { 2 \delta } \int _ { \boldsymbol { x } - \delta } ^ { \boldsymbol { x } + \delta } \left| \boldsymbol { x } - \theta \right| \mathrm { d } \theta } \\ { \displaystyle = \frac { 1 } { 2 } M \delta . } \end{array}
$$

Moreover expressions (16.4) and (16.5) imply the inequality

$$
\| \phi ^ { \prime } \| _ { \infty } \leqslant M .
$$

Therefore,if we replace $f$ by $\phi$ in condition (16.2), it follows from inequalities (16.7) and (16.8) that the bound

$$
\begin{array} { r } { E _ { n } ( f ) \leqslant \frac { 1 } { 2 } M \delta + \pi M / 2 ( n + 1 ) } \end{array}
$$

is satisfied. Because $\pmb { \delta }$ can be arbitrarily small, the required result (16.6) is implied by expression (16.10).□

Expression (16.2) also implies a bound on $E _ { n } ( f )$ ,when $f$ is a continuous function that does not satisfy a Lipschitz condition.

Theorem 16.2 (Jackson III) For every function $f$ in $\mathcal { C } _ { 2 \pi } ,$ the inequality

$$
E _ { n } ( f ) \leqslant \frac { 3 } { 2 } \omega \left( \frac { \pi } { n + 1 } \right)
$$

is obtained, where $\pmb { \omega }$ is the modulus of continuity of $f$

Proof. We again substitute the function (16.3) in expression (16.7). Instead of inequality (16.8), however, we have the bound

$$
\begin{array} { l } { \displaystyle \| f - \phi \| _ { \infty } = \underset { \displaystyle x } { \mathrm { m a x } } \frac { 1 } { 2 \delta } \left| \int _ { x - \delta } ^ { x + \delta } f ( x ) - f ( \theta ) \mathrm { d } \theta \right| } \\ { \displaystyle \leqslant \operatorname* { m a x } _ { \displaystyle x } \frac { 1 } { 2 \delta } \int _ { x - \delta } ^ { x + \delta } \omega \big ( | x - \theta | \big ) \mathrm { d } \theta } \\ { \displaystyle \leqslant \omega \big ( \delta \big ) . } \end{array}
$$

Moreover, because equation (16.4) implies the condition

$$
\begin{array} { c } { { \| \phi ^ { \prime } \| _ { \infty } \leqslant \omega \left( 2 \delta \right) / 2 \delta } } \\ { { \leqslant \omega \left( \delta \right) / \delta , } } \end{array}
$$

where the last line is an elementary property of the modulus of continuity, expression (16.2) gives the bound

$$
E _ { n } ( \phi ) { \leqslant } \frac { \pi } { 2 ( n + 1 ) \delta } { \omega } ( \delta ) .
$$

It follows from condition (16.7) that the inequality

$$
E _ { n } ( f ) \leqslant \biggl [ 1 + \frac { \pi } { 2 ( n + 1 ) \delta } \biggr ] \omega ( \delta )
$$

is satisfied.Therefore,to complete the proof of the theorem,it is sufficient to let $\delta$ have the value $\pi / ( n + 1 )$ .□

We note that inequality (16.11) gives a proof of Theorem 13.1, for it shows that $E _ { n } ( f )$ tends to zero as $_ n$ tends to infinity. Further,extending inequality (16.11） to approximation by algebraic polynomials,which is done in Theorem 16.5，gives another proof of the Weierstrass Theorem 6.1.

In fact inequality (16.11) remains true if the constant $\textstyle { \frac { 3 } { 2 } }$ is replaced by the value one. The following example shows that the parameters $c _ { 1 }$ and $c _ { 2 }$ in the bound

$$
E _ { n } ( f ) \leqslant c _ { 1 } \omega ( c _ { 2 } \pi / [ n + 1 ] ) , \qquad f \in \mathcal { C } _ { 2 \pi } ,
$$

cannot both be less than one.

Let $c _ { 2 }$ be from $( { \textstyle { \frac { 1 } { 2 } } } , 1 )$ ,let $\varepsilon$ have the value

$$
\varepsilon = ( 1 - c _ { 2 } ) \pi / ( n + 1 ) ,
$$

and let $\dot { f }$ be a function in $\mathcal { C } _ { 2 \pi }$ that satisfies the following conditions. For each integer $j , f$ does not change sign on the interval $[ j \pi / ( n + 1 ) - { \textstyle { \frac { 1 } { 2 } } } \pmb { \varepsilon } .$ ， $j \pi / { \left( n + 1 \right) } + { \textstyle \frac { 1 } { 2 } } \varepsilon ] _ { \cdot }$ and $f$ is zero on the interval $[ j \pi / ( n + 1 ) + { \textstyle \frac { 1 } { 2 } } \varepsilon .$ ， $( j + 1 )$ $\pi / ( n + 1 ) { - } \frac { 1 } { 2 } \varepsilon ]$ .The equations

$$
\| f \| _ { \infty } = 1
$$

and

$$
f ( j \pi / [ n + 1 ] ) = ( - 1 ) ^ { j } , \qquad j = 0 , \pm 1 , \pm 2 , . . . ,
$$

hold.A suitable function is shown in Figure 16.1. Expressions (16.18) and (16.19) imply that the zero function is a best approximation from ${ \mathcal { Q } } _ { n }$ to $f ,$ because otherwise a best approximation would change sign $( 2 n + 2 )$ times in $[ 0 , 2 \pi ]$ . Hence $E _ { n } ( f )$ is equal to one. Moreover, Figure 16.1 shows that $\pmb { \omega } ( \pmb { \pi } / [ n + 1 ] - \pmb { \varepsilon } )$ is also equal to one. Therefore substituting the value (16.17) gives the equation

$$
E _ { n } ( f ) = \omega ( c _ { 2 } \pi / [ n + 1 ] ) .
$$

Thus, if $c _ { 2 } < 1$ in inequality (16.16), then $\pmb { c } _ { 1 }$ is not less than one.

# 16.2 The Dini-Lipschitz theorem

The Dini-Lipschitz theorem identifies a quite general class of functions $f$ in $\mathcal { C } _ { 2 \pi } ,$ such that $\pmb { S _ { n } f }$ converges uniformly to $f$ as $\pmb { n }$ tends to infinity, where $S _ { n }$ is the Fourier series operator that is defined in Section 13.2. Because the method of proof depends on Theorem 3.1, we require an upper bound on $\| \pmb { S _ { n } } \|$ .Therefore we recall from Section 13.2 that the norm has the value

$$
\left\| S _ { n } \right\| = { \frac { 1 } { \pi } } \int _ { 0 } ^ { \pi } \left| { \frac { \sin \left[ ( n + { \frac { 1 } { 2 } } ) \theta \right] } { \sin \left( { \frac { 1 } { 2 } } \theta \right) } } \right| \mathrm { d } \theta .
$$

The integrand is bounded above by $( 2 n + 1 )$ and by ${ \pmb \pi } / \theta ;$ ，where the first bound is a consequence of equation (12.51),and where the second bound follows from the elementary inequality

$$
\sin \left( { \textstyle { \frac { 1 } { 2 } } } \theta \right) \geqslant \theta / \pi , \qquad 0 \leqslant \theta \leqslant \pi .
$$

Therefore the relation

$$
\begin{array} { c } { { \displaystyle { \left\| S _ { n } \right\| \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { \mu } \left( 2 n + 1 \right) \mathbf { d } \theta + \frac { 1 } { \pi } \int _ { \mu } ^ { \pi } \frac { \pi } { \theta } \mathbf { d } \theta } } } \\ { { = ( 2 n + 1 ) \mu / \pi + \ln \pi - \ln \mu } } \end{array}
$$

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0003_pages_0141-0210/auto/images/fd21cd815769caf8b379af7daf1b42928ac306846085bfb923382bad6c09b9bb.jpg)  
Figure 16.1. A function that satisfes equation (16.20).

is satisfied for all $\pmb { \mu }$ in $( 0 , \pi )$ . In particular, the value $\pmb { \mu } = \pi / ( 2 n + 1 )$ gives the bound

$$
\left\| S _ { n } \right\| \leqslant 1 + \ln { \left( 2 n + 1 \right) } ,
$$

which is sufficient to prove the following theorem.

Theorem 16.3 (Dini-Lipschitz)

If $f$ is any function in $\mathcal { C } _ { 2 \pi }$ whose modulus of continuity satisfies the condition

$$
\operatorname * { l i m } _ { \delta  0 } | \omega ( \delta ) \ln \delta | = 0 ,
$$

then the sequence of Fourier series approximations $\{ S _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$

Proof. By applying Theorem 3.1, then Theorem 16.2,and then expression (16.24),we deduce the bound

$$
\begin{array} { l } { \displaystyle \| f - S _ { n } f \| _ { \infty } \leqslant [ 1 + \| S _ { n } \| ] E _ { n } ( f ) } \\ { \displaystyle \leqslant \frac { 3 } { 2 } [ 1 + \| S _ { n } \| ] \omega \Big ( \frac { \pi } { n + 1 } \Big ) } \\ { \displaystyle \leqslant \frac { 3 } { 2 } [ 2 + \ln { ( 2 n + 1 ) } ] \omega \Big ( \frac { \pi } { n + 1 } \Big ) . } \end{array}
$$

Because the elementary inequality

$$
\ln { \left( 2 n + 1 \right) } < \ln { \left( 2 \pi \right) } + \left| \ln { \left( \frac { \pi } { n + 1 } \right) } \right|
$$

and condition (16.25) imply that the right-hand side of expression (16.26) tends to zero as $_ n$ tends to infinity, it follows that the theorem is true.□

One reason why the theorem is useful is that it is often easy to show that a continuous function satisfies condition (16.25). However, condition (16.25) is not necessary for the uniform convergence of the Fourier series. It is not possible to strengthen the theorem by improving the bound (16.24), because $\| S _ { n } \|$ is bounded below by a multiple of ln n. Specifically, equation (16.21) and elementary arithmetic give the inequality

$$
\begin{array} { l } { \displaystyle \| S _ { n } \| > \frac { 2 } { \pi } \sum _ { j = 1 } ^ { n } \int _ { ( j - 1 ) \pi / ( n + \frac { 1 } { 2 } ) } ^ { j \pi / ( n + \frac { 1 } { 2 } ) } \left| \frac { \sin { \left[ ( n + \frac { 1 } { 2 } ) \theta \right] } } { \theta } \right| \mathrm { d } \theta } \\ { \displaystyle > \frac { 2 } { \pi } \sum _ { j = 1 } ^ { n } \frac { n + \frac { 1 } { 2 } } { j \pi } \int _ { ( j - 1 ) \pi / ( n + \frac { 1 } { 2 } ) } ^ { j \pi / ( n + \frac { 1 } { 2 } ) } \left| \sin { \left[ ( n + \frac { 1 } { 2 } ) \theta \right] } \right| \mathrm { d } \theta } \\ { \displaystyle = ( 4 / \pi ^ { 2 } ) \sum _ { j = 1 } ^ { n } \frac { 1 } { j } } \\ { \displaystyle > ( 4 / \pi ^ { 2 } ) \ln { ( n + 1 ) } , } \end{array}
$$

which is important to the work of the next chapter.

# 16.3 Some bounds that depend on higher derivatives

It is interesting that Theorems 16.1 and 16.2 apply to Lipschitz continuous and to continuous functions,because they are derived from an inequality, namely expression (16.2), that is valid when $f$ is continuously differentiable.In this section we move in the other direction,for, given that $f$ can be differentiated more than once,we deduce a bound on $E _ { n } ( f )$ that is stronger than expression (16.2). Our main result is analogous to Theorem 3.2, but it is a little more difficult to prove, because, if $r$ is a trigonometric polynomial, then the indefinite integral of $r$ is also a trigonometric polynomial only if the constant term of $r$ is zero.

Theorem 16.4 (Jackson IV)

If the function $f$ is in the space $\mathcal { C } _ { 2 \pi } ^ { ( k ) }$ ， then the error of the best approximation from ${ \mathcal { Q } } _ { n }$ to $f$ satisfies the condition

$$
E _ { n } ( f ) \leqslant { \bigg ( } { \frac { \pi } { 2 n + 2 } } { \bigg ) } ^ { k } \| f ^ { ( k ) } \| _ { \infty } .
$$

Proof. First we establish the bound

$$
E _ { n } ( f ) \leqslant \frac { \pi } { 2 n + 2 } \| f ^ { \prime } - r \| _ { \infty } ,
$$

where $r$ is any function in ${ \mathcal { Q } } _ { n }$ ,and then the proof is completed by induction on $k$ .We obtain inequality (16.30) by extending the proof of Theorem 15.1. If $f ^ { \prime }$ is replaced by $( f ^ { \prime } - r )$ in the second integral of equation (15.11), the right-hand side of this equation is changed by the amount

$$
- \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \theta r \left( \theta + x + \pi \right) { \bf d } \theta = \phi ( x ) ,
$$

say. We may express $r ( \theta + x + \pi )$ in terms of cos $( j \pmb { \theta } )$ ,sin $( j \pmb \theta )$ ,cos $( j x )$ and sin $( j x )$ ，for $j = 0 , 1 , \ldots , n$ , and we may integrate over $\pmb \theta$ analytically, which shows that the function $\{ \phi ( x ) , - \infty < x < \infty \}$ is in ${ \mathcal { Q } } _ { n }$ . It follows from equation (15.11),and from the fact that the first term on the right-hand side of this equation is a constant, that $E _ { n } ( f )$ is equal to the maximum error of the best approximation from ${ \mathcal { Q } } _ { n }$ to the function

$$
\frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \theta [ f ^ { \prime } ( \theta + x + \pi ) - r ( \theta + x + \pi ) ] \mathrm { d } \theta , \qquad - \infty < x < \infty ,
$$

where $r$ is any element of ${ \mathcal { Q } } _ { n }$ .Hence inequality (15.18) remains valid if $f ^ { \prime }$ is replaced by $( f ^ { \prime } - r )$ . Therefore the required condition (16.30） is a consequence of expression (15.19).

To begin the inductive part of the proof, we suppose that inequality (16.29)is satisfied when $k$ is replaced by $( k - 1 )$ . It follows from expression (16.3O) and from the inductive hypothesis that the bound

$$
\begin{array} { c } { { E _ { n } ( f ) \displaystyle \leqslant \frac { \pi } { 2 n + 2 } \displaystyle \operatorname* { m i n } _ { r \in \mathcal { Q } _ { n } } \| f ^ { \prime } - r \| _ { \infty } } } \\ { { \displaystyle = \frac { \pi } { 2 n + 2 } E _ { n } ( f ^ { \prime } ) } } \\ { { \displaystyle \leqslant \left( \frac { \pi } { 2 n + 2 } \right) ^ { k } \| f ^ { ( k ) } \| _ { \infty } } } \end{array}
$$

is obtained, which is the general step of the inductive argument. Because Theorem 15.1 states that inequality(16.29) holds when $k = 1$ ,the proof is complete.□

One fundamental difference between Theorems 3.2 and 16.4 is that Theorem 16.4 does not require the condition $k \leqslant n$ It is therefore interesting to consider the consequences of inequality (16.29) when $k$ is larger than $_ n$ .For example, if $f$ is an infinitely differentiable function whose derivatives are bounded, if we let $n = 1$ ,and if we take the limit of inequality (16.29) as $\pmb { k }$ tends to infinity, then it follows that $E _ { 1 } ( f )$ is zero. Thus the function $f$ is in the space $\mathcal { Q } _ { 1 }$ , which can also be proved from the fact that the derivatives of the Fourier series expansion of $f$ are equal to the derivatives of $f .$ The more usual application of Theorem 16.4, however, is when a bound on $\| f ^ { ( k ) } \| _ { \infty }$ is known,and a trigonometric polynomial approximation to $f$ is required,whose maximum error does not exceed a given tolerance.Inequality (16.29) provides a value of $n$ such that a trigonometric polynomial from ${ \mathcal { Q } } _ { n }$ is suitable.

# 16.4 Extensions to algebraic polynomials

In this section we deduce from Theorems 16.1 and 16.2 some useful bounds on the least maximum error

$$
d _ { n } ^ { \ast } \left( g \right) = \operatorname* { m i n } _ { p \in \mathscr { P } _ { n } } \left\| g - p \right\| _ { \infty } ,
$$

where $\pmb { g }$ is a function in $\mathcal { C } [ - 1 , 1 ]$ . It is necessary to relate approximation by algebraic polynomials to best approximation by trigonometric polynomials.The following technique is used,which is similar to one that occurs in the proof of Theorem 13.1.

Given $_ g$ in $\mathcal { C } [ - 1 , 1 ]$ , we let $f$ be the function in $\mathcal { C } _ { 2 \pi }$ that is defined by the equation

$$
f ( x ) = g ( \cos x ) , \qquad - \infty < x < \infty .
$$

We let $q ^ { * }$ be an approximation to $f$ from ${ \mathcal { Q } } _ { n }$ that satisfies the condition

$$
E _ { n } ( f ) = \| f - q ^ { * } \| _ { \infty } .
$$

Because $f$ is an even function, it follows that $q ^ { * }$ is also even, but the theory that has been given does not include a proof of this statement. Instead we note that, if $\{ q ^ { * } ( x ) ; - \infty < x < \infty \}$ is not even, then $\{ q ^ { * } ( - x )$ ； $- \infty < x <$ $\infty \}$ and hence $\scriptstyle { \frac { 1 } { 2 } } [ q ^ { * } ( x ) + q ^ { * } ( - x ) ] ; \ - \infty < x < \infty \}$ are also best approxima-tions from ${ \mathcal { Q } } _ { n }$ to $f .$ Therefore,in the hypothetical case when there is some freedom in $q ^ { * }$ , we can choose $q ^ { * }$ to be an even function, which gives an expansion of the form

$$
q ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } c _ { j } ( \cos x ) ^ { j } , \qquad - \infty < x < \infty ,
$$

where each $c _ { j }$ is a real coeficient. Therefore the algebraic polynomial

$$
p ^ { * } ( t ) = \sum _ { j = 0 } ^ { n } c _ { j } t ^ { j } , \qquad - 1 \leqslant t \leqslant 1 ,
$$

satisfies the equation

$$
q ^ { * } ( x ) = p ^ { * } ( \cos x ) , \qquad - \infty < x < \infty .
$$

It follows from equations (16.34), (16.35), (16.36) and (16.39) that the inequality

$$
\begin{array} { r l } & { d _ { n } ^ { * } \left( g \right) \leqslant \left\| g - p ^ { * } \right\| _ { \infty } } \\ & { \qquad = \underset { - \infty < x < \infty } { \operatorname* { m a x } } \left| f ( x ) - q ^ { * } ( x ) \right| } \\ & { \qquad = E _ { n } ( f ) } \end{array}
$$

is obtained. In fact this inequality is satisfied as an equation for all $_ { g }$ in $\mathcal { C } [ - 1 , 1 ]$ . It is important to the proof of the following theorem.

Theorem 16.5 (Jackson V)

For all functions $_ { g }$ in $\mathcal { C } [ - 1 , 1 ] ,$ ,the least maximum error (16.34) satisfies the bound

$$
d _ { n } ^ { \ast } \left( g \right) \leqslant \frac { 3 } { 2 } \omega _ { g } \biggl ( \frac { \pi } { n + 1 } \biggr ) ,
$$

where $\omega _ { g }$ is the modulus of continuity of $\pmb { g }$ 、Further,if the Lipschitz condition

$$
\big | g ( t _ { 1 } ) - g ( t _ { 0 } ) \big | \leqslant M _ { g } \big | t _ { 1 } - t _ { 0 } \big |
$$

holds for all $t _ { 0 }$ and $t _ { 1 }$ in[−1,1], then $d _ { n } ^ { * } ( g )$ is bounded by the inequality

$$
d _ { n } ^ { \ast } \left( g \right) \leqslant \pi M _ { g } / 2 ( n + 1 ) .
$$

Proof. The bound (16.41) is a corollary of Theorem 16.2 and condition (16.40), provided that the inequality

$$
\omega _ { f } \Big ( \frac { \pi } { n + 1 } \Big ) \leqslant \omega _ { g } \Big ( \frac { \pi } { n + 1 } \Big )
$$

is obtained, where $\omega _ { f }$ is the modulus of continuity of the function (16.35). In order to establish this inequality we require the elementary relation

$$
\begin{array} { r } { \left| \cos \theta _ { 1 } - \cos \theta _ { 0 } \right| \leqslant \left| \theta _ { 1 } - \theta _ { 0 } \right| . } \end{array}
$$

Thus the bound

$$
\begin{array} { r l } & { \omega _ { g } \Bigg ( \displaystyle \frac { \pi } { n + 1 } \Bigg ) = \underset { | \theta _ { 1 } - \theta _ { 0 } | \in \pi / ( n + 1 ) } { \operatorname* { m a x } } \left| g ( \theta _ { 1 } ) - g ( \theta _ { 0 } ) \right| } \\ & { \qquad \geqslant \underset { | \theta _ { 1 } - \theta _ { 0 } | \in \pi / ( n + 1 ) } { \operatorname* { m a x } } \left| g ( \cos \theta _ { 1 } ) - g ( \cos \theta _ { 0 } ) \right| } \\ & { \qquad = \underset { | \theta _ { 1 } - \theta _ { 0 } | \in \pi / ( n + 1 ) } { \operatorname* { m a x } } \left| f ( \theta _ { 1 } ) - f ( \theta _ { 0 } ) \right| } \\ & { \qquad = \omega _ { f } \Bigg ( \frac { \pi } { n + 1 } \Bigg ) } \end{array}
$$

is satisfied, where $f$ is the function (16.35). Therefore the first part of the theorem is true.

In order to prove the second part, we note that inequality (16.42) and the method of proof of inequality (16.44) imply the relation

$$
\begin{array} { r } { \left| f ( x _ { 1 } ) - f ( x _ { 0 } ) \right| \leqslant \omega _ { f } ( \left| x _ { 1 } - x _ { 0 } \right| ) } \\ { \leqslant \omega _ { g } ( \left| x _ { 1 } - x _ { 0 } \right| ) } \\ { \leqslant M _ { g } \left| x _ { 1 } - x _ { 0 } \right| . } \end{array}
$$

Therefore condition (16.43) is a consequence of the bound (16.40) and Theorem 16.1.□

One important corollary of the theorem is the extension of Theorem 15.1 to algebraic polynomials. Because the Lipschitz condition

$$
\big | g ( t _ { 1 } ) - g ( t _ { 0 } ) \big | \leqslant \| g ^ { \prime } \| _ { \infty } \big | t _ { 1 } - t _ { 0 } \big |
$$

is satisfied if $\pmb { g }$ is in $\mathcal { C } ^ { ( 1 ) } [ - 1 , 1 ]$ , expression (16.43) implies the bound

$$
d _ { n } ^ { \ast } \left( g \right) \leqslant \frac { \pi } { 2 ( n + 1 ) } \| g ^ { \prime } \| _ { \infty } .
$$

Therefore inequality (3.19） is valid. Specifically, if the range $[ a , b ]$ is $[ - 1 , 1 ] .$ , we may let $^ c$ have the value ${ \scriptstyle { \frac { 1 } { 2 } } } \pi .$ It follows from Theorem 3.2 that the condition

$$
d _ { n } ^ { * } ( g ) \leqslant \frac { ( n - k ) ! { ( \frac { 1 } { 2 } \pi ) } ^ { k } } { n ! } \| g ^ { ( k ) } \| _ { \infty } , \qquad n \geqslant k ,
$$

is obtained by all functions $\pmb { g }$ in the space $\mathcal { C } ^ { ( k ) } [ - 1 , 1 ]$

We consider whether a bound that is stronger than inequality (16.50) can be found by applying the method of proof of Theorem 16.5 to the bound (16.29). First we let $k = 2$ .Expressions (16.40) and (16.29) imply the relation

$$
d _ { n } ^ { * } \left( g \right) \leqslant \left( \frac { \pi } { 2 n + 2 } \right) ^ { 2 } \left\| f ^ { \prime \prime } \right\| _ { \infty } ,
$$

where $f$ is still the function (16.35). Hence, in order to deduce a condition of the form (16.50), it is necessary to bound $\| f ^ { \prime \prime } \| _ { \infty }$ by a multiple of $\| g ^ { \prime \prime } \| _ { \infty }$ Here the method breaks down, however. For example, if $\pmb { g }$ is the function $\left\{ g ( x ) = x ; - 1 \leqslant x \leqslant 1 \right\}$ ,then $\| g ^ { \prime \prime } \| _ { \infty }$ is zero but $\| f ^ { \prime \prime } \| _ { \infty }$ is one.Therefore the close relation between minimax approximation by trigonometric and algebraic polynomials,which is shown in Theorem 16.5,does not extend to bounds that depend on higher derivatives.

# 16 Exercises

16.1 Find values of $_ n$ such that $E _ { n } ( f )$ is less than $1 0 ^ { - 4 }$ for each of the following three functions $f$ :(i) the function defined in Exercise 15.1,(ii) the function defined in Exercise 13.2,and (ii) a function in $\mathcal { C } _ { 2 \pi }$ that is infinitely differentiable and that satisfies the condition $\| f ^ { ( k ) } \| _ { \infty } \leqslant 1 0 ^ { k }$ , for all positive integers $k$

16.2 Let $c _ { 2 } ( n )$ be a number such that the condition ${ \cal E } _ { n } ( \phi ) \leqslant$ $\phi$ $c _ { 2 } ( n ) \| \phi ^ { \prime \prime } \| _ { \infty }$ beuo163) is satisfied, where $\phi$ is any function in $f$ is anyfunction in $\mathcal { C } _ { 2 \pi } ^ { ( 2 ) }$ Byletting $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ then $E _ { n } ( f )$ is bounded by the inequality $\begin{array} { r } { E _ { n } ( f ) \leqslant [ 2 c _ { 2 } ( n ) ] ^ { \frac { 1 } { 2 } } \| f ^ { \prime } \| _ { \infty } . } \end{array}$

16.3Give an example to show that the value of $c _ { 2 } ( n )$ in the inequality

$$
E _ { n } ( \phi ) \leqslant c _ { 2 } ( n ) \| \phi ^ { \prime \prime } \| _ { \infty } , \qquad \phi \in \mathcal { C } _ { 2 \pi } ^ { ( 2 ) } ,
$$

is at least $\pi ^ { 2 } / [ 8 ( n + 1 ) ^ { 2 } ]$

16.4 Let $f$ be a function in $\mathcal { C } ^ { ( 1 ) } [ 0 , 1 ]$ and let $B _ { n } f$ be the Bernstein approximation (6.23). Deduce from the equation

$$
( f - B _ { n } f ) ( x ) = \sum _ { k = 0 } ^ { n } { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } { \biggl [ } f ( x ) - f { \biggl ( } { \frac { k } { n } } { \biggr ) } { \biggr ] }
$$

that, when $n = 2$ , the inequality

$$
\| f - B _ { 2 } f \| _ { \infty } \leqslant \frac { 8 } { 2 7 } \| f ^ { \prime } \| _ { \infty }
$$

is satisfied. Compare the bound (16.5O) in the case when $k = 1$ and $n = 2$ ， after allowing for the change to the range of the variable.

16.5 By following the method of proof of Theorem 3.2,obtain from condition （16.49）a bound on $d _ { n } ^ { * } ( g )$ that is stronger than inequality (16.5O),and that is valid when $n = k - 1$ .Deduce from Theorems 4.2 and 7.3 that the least number $c ( n )$ that satisfies the inequality

$$
d _ { n } ^ { * } \left( g \right) \leqslant c \left( n \right) \| g ^ { ( n + 1 ) } \| _ { \infty } , \qquad g \in \mathcal { C } ^ { ( n + 1 ) } [ - 1 , 1 ] ,
$$

has the value $c ( n ) = 1 / 2 ^ { n } ( n + 1 ) !$

16.6 By showing that the function $\{ p ( x ) = \sin { ( n x ) } / { n } ; - \infty < x < \infty \}$ is the element of ${ \mathcal { Q } } _ { n }$ whose minimax norm is least subject to the condition $p ^ { \prime } ( 0 ) = 1$ ， prove that the inequality $\| p ^ { ( k ) } \| _ { \infty } \leqslant n ^ { k } \| p \| _ { \infty }$ holds for all trigonometric polynomials $p$ in $\mathcal { Q } _ { n }$

16.7 Let $f$ be a function in $\mathcal { C } _ { 2 \pi }$ that has the form $\{ f ( x ) = | x | ^ { \frac { 1 } { 2 } } \}$ in a neighbourhood of the origin. Deduce from Exercise 16.6 that $E _ { n } ( f )$ is bounded below by a multiple of $\left( n ^ { 2 } \| f \| _ { \infty } \right) ^ { - 1 / 3 }$ . Compare the bound that is given by Theorem 16.2.

16.8 Theorem 16.4 shows that the constant $c _ { 2 } ( n )$ of Exercise 16.2 may be given the value $[ { \pmb \pi } / ( 2 n + 2 ) ] ^ { 2 }$ . Deduce from the proofs of Theorems 15.1 and 16.4 that smaller values of $c _ { 2 } ( n )$ exist, giving attention to the conditions on $f ^ { \prime }$ that make $E _ { n } ( f ^ { \prime } )$ close to $[ { \pi } / { ( 2 n + 2 ) } ] \| f ^ { \prime \prime } \| _ { \infty }$

16.9Prove that the inequality

$$
E _ { n } ( f ) \leqslant { \biggl [ } 1 + { \frac { ( 2 n + 2 ) ^ { 2 } c _ { 2 } ( n ) } { 2 \pi ^ { 2 } } } { \biggr ] } \omega { \biggl ( } { \frac { \pi } { n + 1 } } { \biggr ) }
$$

is satisfied, for all functions $f$ in $\mathcal { C } _ { 2 \pi }$ where $c _ { 2 } ( n )$ is the constant of Exercise 16.2.A suitable method is to replace $\phi$ in the proof of Theorem 16.2 by the function

$$
\phi ( x ) = \int _ { - \delta } ^ { \delta } f ( x + \theta ) ( \delta - | \theta | ) { \mathrm d } \theta / \delta ^ { 2 } , \qquad - \infty < x < \infty .
$$

Hence Exercise 16.8 implies that the constant $\frac { 3 } { 2 }$ in the statement of Theorem 16.2 is not optimal.

16.10By considering a case when the best minimax approximation in $\mathcal { P } _ { 2 }$ to a function $\pmb { g }$ in $\mathcal { C } [ - 1 , 1 ]$ is the zero function, show that, if $^ { c }$ is a constant that satisfies the condition

$$
d _ { n } ^ { * } ( g ) \leqslant c \| g ^ { \prime } \| _ { \infty } , \qquad g \in { \mathcal { C } } ^ { ( 1 ) } [ - 1 , 1 ] ,
$$

then $c$ is not less than $\textstyle { \frac { 1 } { 3 } }$ .Further,by considering a case when the best approximation is a straight line, show that the lower bound on $^ { c }$ can be increased to $( 6 - 4 \sqrt { 2 } )$


<!-- chunk 0004: pages 211-280 -->
# 17

# The uniform boundedness theorem

# 17.1 Preliminary results

If an approximation to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ is required to high accuracy, then it is usual to calculate a sequence of approximations $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ ,until the accuracy is achieved. Therefore it may be helpful to know whether the sequence converges uniformly to $f .$ The uniform boundedness theorem gives one of the most useful methods for answering this question.A simple version of it is proved in Section 17.2, which implies that, if the operators $\left\{ X _ { n } ; n = 0 , 1 , 2 , \ldots \right\}$ are linear, then uniform convergence is obtained for all functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,only if the sequence of norms $\{ \| X _ { n } \|$ ； $n = 0 , 1 , 2 , \ldots \}$ is bounded. Because expressions (13.29) and (16.28) give the inequality

$$
\| R _ { n } \| _ { \infty } > ( 4 / \pi ^ { 2 } ) \ln { ( n + 1 ) } ,
$$

it follows,for example, that there exists $f$ in $\mathcal { C } [ - 1 , 1 ]$ such that the sequence of approximations $\{ R _ { n } f ; n = 0 , 1 , 2 , . . . \}$ fails to converge to $f .$ Moreover, because the work of Section 17.2 applies also to the approximation of functions in $\mathcal { C } _ { 2 \pi } ,$ the bound (16.28) implies that there exist continuous periodic functions whose Fourier series approximations do not converge uniformly.

Therefore Section 17.3 addresses the question whether there is a sequence of operators $\left\{ X _ { n } ; n = 0 , 1 , 2 , . . . \right\}$ for calculating approximations to functions in $\mathcal { C } _ { 2 \pi }$ ，that is more suitable than the Fourier series sequence $\{ S _ { n } ; n = 0 , 1 , 2 , \ldots \}$ .We find the remarkable result that, if $X _ { n }$ is linear, if $X _ { n } f$ is in ${ \mathcal { Q } } _ { n }$ for all $f ,$ and if the projection condition

$$
X _ { n } f = f , \qquad f \in { \mathcal { Q } } _ { n } ,
$$

is satisfied, then the norm $\| X _ { n } \| _ { \infty }$ cannot be less than $\| \pmb { S _ { n } } \| _ { \infty }$ .Hence, in order to obtain uniform convergence, it is necessary to give up the projection condition, or to give up the linearity of the operator. A similar conclusion is reached for approximation by algebraic polynomials in Section 17.4. The main theory of the chapter requires the definitions and elementary results that are mentioned below.

In order to prove the uniform boundedness theorem we make use of ‘Cauchy sequences’ and ‘complete’ normed linear spaces.We note, therefore, that the sequence $\{ f _ { i } ; i = 0 , 1 , 2 , . . . \}$ is a Cauchy sequence if, for any $\pmb \varepsilon > 0$ ,there exists an integer $N$ such that the difference $\| f _ { i } - f _ { j } \|$ is less than $\pmb \varepsilon$ for all $i \geq N$ and $j \geq N .$ Further,a normed linear space is complete if every Cauchy sequence is convergent. In particular, the space $\mathcal { C } [ a , b ]$ is complete when the norm is the $\infty$ -norm,which allows Theorem 17.2 to be applied to $\mathcal { C } [ a , b ]$

We also make use of ‘fundamental sets'. The set $\{ f _ { i } ; i = 0 , 1 , 2 , . . . \}$ in a normed linear space $\mathcal { B }$ is called fundamental if,for any $f$ in $\mathcal { B }$ and any $\pmb \varepsilon > 0$ , there exist an integer $k$ and coefficients $\{ a _ { i } ; i = 0 , 1 , \ldots , k \}$ such that the element

$$
\phi = \sum _ { i = 0 } ^ { k } a _ { i } f _ { i }
$$

satisfies the condition

$$
\left\| f - \phi \right\| < \varepsilon .
$$

For example, the set of polynomials $\{ f _ { i } ( x ) = x ^ { i } ; a \leqslant x \leqslant b ; i = 0 , 1 , 2 , . . . \}$ is fundamental in $\mathcal { C } [ a , b ]$

One application of fundamental sets is to show that two bounded linear operators, $L _ { 1 }$ and $L _ { 2 }$ say, from $\mathscr { B }$ to $\mathcal { B }$ are equal. Clearly, if $\{ f _ { i } ; i =$ $0 , 1 , 2 , \ldots \}$ is a fundamental set, then the operators are equal only if the equations

$$
L _ { 1 } f _ { i } = L _ { 2 } f _ { i } , \qquad i = 0 , 1 , 2 , \ldots ,
$$

are satisfied. The following argument gives the useful result that the conditions (17.5) are sufficient for the operators to be the same.

Suppose that the equations (17.5） hold, but that $L _ { 1 }$ and $\mathbf { { { L } } } _ { 2 }$ are different. Then there exists $f$ in $\mathcal { B }$ such that $L _ { 1 } f$ is not equal to $L _ { 2 } f .$ We let $\pmb \varepsilon$ be the positive number

$$
\varepsilon = \big \| L _ { 1 } f - L _ { 2 } f \big \| / [ \big \| L _ { 1 } \big \| + \big \| L _ { 2 } \big \| ] ,
$$

and we let expression (17.3) be an element of $\mathcal { B }$ that satisfies the bound (17.4). The properties of norms,the linearity of the operators,and

condition (17.5) imply the relation

$$
\begin{array} { r l } & { \left\| L _ { 1 } f - L _ { 2 } f \right\| = \left\| L _ { 1 } ( f - \phi ) - L _ { 2 } ( f - \phi ) \right\| } \\ & { \qquad \leqslant [ \left\| L _ { 1 } \right\| + \left\| L _ { 2 } \right\| ] \| f - \phi \| } \\ & { \qquad < \varepsilon [ \left\| L _ { 1 } \right\| + \left\| L _ { 2 } \right\| ] , } \end{array}
$$

but this relation contradicts the definition (17.6). Therefore the equations (17.5)are suitable for showing that two operators are equal.

# 17.2 Tests for uniform convergence

The two theorems of this section are useful for testing whether a sequence of linear operators $\left\{ X _ { n } ; n = 0 , 1 , 2 , \ldots \right\}$ from $\mathcal { B }$ to $\mathcal { B }$ has the property that $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges to $f$ for all $f$ in $\mathscr { B }$

# Theorem 17.1

Let $\{ f _ { i } ; i = 0 , 1 , 2 , . . . \}$ be a fundamental set in a normed linear space $\mathcal { B }$ ,and let $\left\{ X _ { n } ; n = 0 , 1 , 2 , . . . \right\}$ be a sequence of bounded linear operators from $\mathcal { B }$ to $\mathcal { B }$ .The equations

$$
\operatorname* { l i m } _ { n \to \infty } \big \| f _ { i } - X _ { n } f _ { i } \big \| = 0 , \qquad i = 0 , 1 , 2 , \ldots ,
$$

are necessary and sufficient conditions for the sequence $\{ X _ { n } f ; n =$ $0 , 1 , 2 , \ldots \}$ to converge to $f$ for all $f$ in $\mathscr { B }$

Proof. Clearly the equations are necessary. To prove that they are sufficient, we let $f$ be a general element of $\mathcal { B }$ . The definition of a fundamental set implies that, for any $\varepsilon > 0$ ,there exists a function of the form (17.3) that satisfies the condition

$$
\begin{array} { r } { \left\| f - \phi \right\| \leqslant \frac { 1 } { 2 } \varepsilon / ( M + 1 ) , } \end{array}
$$

where $M$ is a fixed upper bound on the norms $\left\{ \left\| X _ { n } \right\| ; n = 0 , 1 , 2 , \ldots \right\}$ Further, equation (17.8) implies that there is an integer $N ,$ such that the coefficients of expression (17.3) satisfy the bound

$$
\begin{array} { r } { \| f _ { i } - X _ { n } f _ { i } \| \leqslant \frac { 1 } { 2 } \varepsilon \bigg / \underset { j = 0 } { \overset { k } { \sum } } | a _ { j } | , \qquad i = 0 , 1 , \dots , k , } \end{array}
$$

for all $n \geqslant N .$ It follows from the properties of norms,and from the linearity of the operators, that the inequality

$$
\begin{array} { l } { \displaystyle \| f - X _ { n } f \| \leqslant \| ( f - \phi ) - X _ { n } ( f - \phi ) \| + \| \phi - X _ { n } \phi \| } \\ { \displaystyle \leqslant ( M + 1 ) \| f - \phi \| + \| \sum _ { i = 0 } ^ { k } a _ { i } ( f _ { i } - X _ { n } f _ { i } ) \| } \\ { \displaystyle \leqslant ( M + 1 ) \| f - \phi \| + \sum _ { i = 0 } ^ { k } \left| a _ { i } \right| \| f _ { i } - X _ { n } f _ { i } \| } \\ { \displaystyle \leqslant \varepsilon , \qquad n \geqslant N , } \end{array}
$$

is satisfied, which completes the proof of the theorem.

Because many algorithms for calculating spline approximations are bounded linear operators,Theorem 17.1 is useful to the work of the last seven chapters.The next theorem shows that, if the norms $\{ \Vert X _ { n } \Vert$ ； $n =$ $0 , 1 , 2 , \ldots \}$ are unbounded, then there is an unequivocal answer to the convergence question of this section.

# Theorem 17.2 (uniform boundedness)

Let $\mathcal { B }$ be a complete normed linear space,and let $\{ X _ { n } ; n =$ $0 , 1 , 2 , \ldots \}$ be a sequence of linear operators from $\mathcal { B }$ to $\mathcal { B }$ If the sequence of norms $\{ \Vert X _ { n } \Vert$ ； $n = 0 , 1 , 2 , \ldots \}$ is unbounded, then there exists an element, $f ^ { * }$ say, in $\mathcal { B }$ ，such that the sequence $\{ X _ { n } f ^ { * } ; n = 0 , 1 , 2 , . . . \}$ diverges.

Proof. Because it is sufficient to show that a subsequence of $\{ X _ { n } f ^ { * } ; n = { }$ $0 , 1 , 2 , \ldots \}$ diverges,we may work with a subset of the sequence of operators. We may choose operators whose norms diverge at an arbitrarily fast rate. Therefore we assume, without loss of generality, that the conditions

$$
\| X _ { n } \| \geqslant ( 2 0 n ) 4 ^ { n } , \qquad n = 0 , 1 , 2 , \ldots ,
$$

are satisfied. The method of proof is to use these conditions to construct a Cauchy sequence $\{ f _ { k } ; k = 0 , 1 , 2 , \ldots \} ,$ ，whose limit $f ^ { * }$ is such that the numbers $\left\{ \left\| X _ { n } f ^ { * } \right\| ; n = 0 , 1 , 2 , . . . \right\}$ diverge.

The terms of the Cauchy sequence depend on elements $\{ \phi _ { n } ; n =$ $0 , 1 , 2 , \ldots \}$ of $\mathcal { B }$ that satisfy the conditions

$$
\begin{array} { l } { \displaystyle \| \phi _ { n } \| = 1 } \\ { \displaystyle \| X _ { n } \phi _ { n } \| \geqslant 0 . 8 \| X _ { n } \| } \end{array} \} , \quad n = 0 , 1 , 2 , \ldots .
$$

The definition of $\| X _ { n } \|$ implies that these elements exist. We let $f _ { 0 } = \phi _ { 0 }$ ， and, for $k \geqslant 1 , f _ { k }$ has the form

$$
f _ { k } = \Big \{ \begin{array} { l l } { \mathrm { e i t h e r } f _ { k - 1 } } \\ { \mathrm { o r } f _ { k - 1 } + ( \frac 3 4 ) ( \frac 1 4 ) ^ { k } \phi _ { k } , } \end{array}
$$

where the choice depends on $\| X _ { k } f _ { k - 1 } \|$ and will be made precise later. In all cases expression (17.14) implies that for $j > k$ the bound

$$
\| f _ { j } - f _ { k } \| \leqslant \sum _ { i = k + 1 } ^ { j } \ ( \frac { 3 } { 4 } ) ( \frac { 1 } { 4 } ) ^ { i } \| \phi _ { i } \| < ( \frac { 1 } { 4 } ) ^ { k + 1 }
$$

is obtained. Therefore $\left\{ f _ { k } ; k = 0 , 1 , 2 , \ldots \right\}$ is a Cauchy sequence, and its limit $f ^ { * }$ satisfies the condition

$$
\begin{array} { r } { \left\| f ^ { * } - f _ { k } \right\| \leqslant ( \frac { 1 } { 4 } ) ^ { k + 1 } , \qquad k = 0 , 1 , 2 , \ldots , } \end{array}
$$

which gives the inequality

$$
\begin{array} { r l } {  { \big \| X _ { n } f ^ { * } \big \| \geqslant \big \| X _ { n } f _ { n } \big \| - \big \| X _ { n } ( f ^ { * } - f _ { n } ) \big \| } } \\ & { \geqslant \big \| X _ { n } f _ { n } \big \| - \big ( \frac { 1 } { 4 } \big ) ^ { n + 1 } \big \| X _ { n } \big \| . } \end{array}
$$

It follows that the relation

$$
\begin{array} { r } { \| X _ { k } f _ { k } \| \geqslant k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| , \qquad k = 0 , 1 , 2 , \ldots , } \end{array}
$$

would imply the divergence of the sequence $\{ X _ { n } f ^ { * } ; n = 0 , 1 , 2 , . . . \}$ .We complete the proof of the theorem by showing that the choice (17.14) allows condition (17.18) to be satisfied.

The value of $f _ { 0 }$ is such that condition (17.18) holds when $k = 0$ ,but this case is unimportant. For $k \geqslant 1$ we let $f _ { k } = f _ { k - 1 }$ if this choice satisfies inequality (17.18). Otherwise,when the bound

$$
\| X _ { k } f _ { k - 1 } \| < k + ( \frac 1 4 ) ^ { k + 1 } \| X _ { k } \|
$$

is obtained, $f _ { k }$ is defined by the second line of expression (17.14). Hence the triangle inequality for norms, expressions (17.13) and (17.19), and the bound (17.12) give the relation

$$
\begin{array} { r l } & { \| X _ { k } f _ { k } \| \geqslant \| ( \frac { 3 } { 4 } ) ^ { \iota } ( \frac { 1 } { 4 } ) ^ { k } X _ { k } \phi _ { k } \| - \| X _ { k } f _ { k - 1 } \| } \\ & { \qquad > 0 . 6 ( \frac { 1 } { 4 } ) ^ { k } \| X _ { k } \| - [ k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| ] } \\ & { \qquad = [ k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| ] + [ 0 . 1 ( \frac { 1 } { 4 } ) ^ { k } \| X _ { k } \| - 2 k ] } \\ & { \qquad \geqslant k + ( \frac { 1 } { 4 } ) ^ { k + 1 } \| X _ { k } \| , } \end{array}
$$

which establishes expression (17.18). Therefore,for reasons given already, the sequence $\{ X _ { n } f ^ { * } ; n = 0 , 1 , 2 , . . . \}$ diverges,where $f ^ { * }$ is an element of the complete linear space $\mathcal { B }$ □

Because the spaces $\mathcal { C } [ a , b ]$ and $\mathcal { C } _ { 2 \pi }$ are complete,and because the bound (17.1) applies to both $\| R _ { n } \| _ { \infty }$ and $\| \boldsymbol { S _ { n } } \| _ { \infty }$ ,the theorem proves two of the statements that are made in the first paragraph of this chapter, namely that there exists $f$ in $\mathcal { C } [ - 1 , 1 ]$ such that $\{ R _ { n } f ; n = 0 , 1 , 2 , . . . \}$ diverges, and there exists $f$ in $\mathcal { C } _ { 2 \pi }$ such that $\left\{ S _ { n } f ; n = 0 , 1 , 2 , \ldots \right\}$ diverges.These remarks, however, should not deter one from using the operators $\scriptstyle { R _ { n } }$ and $\pmb { S _ { n } }$ ,because the rate of divergence

$$
\left\| R _ { n } \right\| = \left\| S _ { n } \right\| \sim \ln n
$$

is slow, and in any case divergence cannot occur when $f$ is differentiable. From a practical point of view it is more important to keep in mind that it is unusual to calculate polynomial approximations of high degree.

# 17.3 Application to trigonometric polynomials

In this section we prove the result, mentioned in Section 17.1, that, if $L$ is a bounded linear operator from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { Q } _ { n }$ ，and if the

projection condition

$$
L f = f , \qquad f \in { \mathcal { Q } } _ { n } ,
$$

is satisfied, then $\| \pmb { L } \| _ { \infty }$ is bounded below by $\| \pmb { S _ { n } } \| _ { \infty }$ . The method of proof depends on the displacement operator $\pmb { D } _ { \pmb { \lambda } }$ from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { C } _ { 2 \pi }$ that is defined by the equation

$$
( D _ { \lambda } f ) ( x ) = f ( x + \lambda ) , \qquad - \infty < x < \infty ,
$$

where $\pmb { \lambda }$ is any real parameter, and where $f$ is any function in $\mathcal { C } _ { 2 \pi }$ It also depends on the operator

$$
G = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } D _ { - \lambda } L D _ { \lambda } \mathrm { d } \lambda .
$$

Before beginning the proof of the main result, the meaning of this integral is explained.

For any $f$ in $\mathcal { C } _ { 2 \pi } ,$ we let $f _ { \lambda }$ be the function

$$
f _ { \lambda } = D _ { - \lambda } L D _ { \lambda } f ,
$$

which is also in $\mathcal { C } _ { 2 \pi }$ .For any fixed value of the variable $\pmb { x }$ , we regard $f _ { \lambda } ( x )$ as a function of $\lambda$ .Equation (17.24) means that $G f$ is the function

$$
( G f ) ( x ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f _ { \lambda } ( x ) \mathrm { d } \lambda , \qquad - \infty < x < \infty ,
$$

which is a valid definition, because the following discussion shows that $f _ { \lambda } ( x )$ is a continuous function of $\lambda$

It is straightforward to prove that $D _ { \lambda } f$ depends continuously on $\lambda$ Specifically, because the definition (17.23) implies the equation

$$
( D _ { \mu } f - D _ { \lambda } f ) ( x ) = f ( x + \mu ) - f ( x + \lambda ) , \qquad - \infty < x < \infty ,
$$

we have the bound

$$
\| D _ { \mu } f - D _ { \lambda } f \| _ { \infty } \leqslant \omega _ { f } ( | \mu - \lambda | ) ,
$$

where $\omega _ { f }$ is the modulus of continuity of $f .$ Thus the inequality

$$
\| L D _ { \mu } f - L D _ { \lambda } f \| _ { \infty } \leqslant \| L \| \omega _ { f } ( | \mu - \lambda | )
$$

is satisfied, which shows that the function $L D _ { \lambda } f$ also depends continuously on $\lambda$

To continue the discussion we require the result that the family of functions $\{ L D _ { \lambda } f ; 0 \leqslant \lambda \leqslant 2 \pi \}$ is uniformly continuous.This result holds because the dependence on $\pmb { \lambda }$ is continuous, because the range of $\pmb { \lambda }$ is compact, because each function in the family is continuous in the variable $\pmb { x } ,$ ，and because,due to periodicity,it is sufficient to establish uniform continuity when $x$ is restricted to the compact interval $0 \leqslant x \leqslant 4 \pi$ We let $\omega ^ { * }$ be the modulus of continuity of the family. Therefore,if we replace $f$ by $L D _ { \nu } f$ in expression (17.28), we find that the bound

$$
\begin{array} { r } { \| D _ { \mu } L D _ { \nu } f - D _ { \lambda } L D _ { \nu } f \| \leqslant \omega ^ { * } ( | \mu - \lambda | ) } \end{array}
$$

is obtained for all values of the parameters $\mu , \lambda$ and $\pmb { \nu }$ Moreover expression (17.29),and the fact that the norm of a displacement operator is one,give the condition

$$
\| D _ { - \mu } L D _ { \mu } f - D _ { - \mu } L D _ { \lambda } f \| \leqslant \| L \| \omega _ { f } ( | \mu - \lambda | ) .
$$

We deduce from the last two inequalities and from the definition (17.25) that the relation

$$
\begin{array} { c } { { \left\| f _ { \mu } - f _ { \lambda } \right\| \leqslant \left\| f _ { \mu } - D _ { - \mu } L D _ { \lambda } f \right\| + \left\| D _ { - \mu } L D _ { \lambda } f - f _ { \lambda } \right\| } } \\ { { \leqslant \left\| L \right\| \omega _ { f } ( \left| \mu - \lambda \right| ) + \omega ^ { * } ( \left| \mu - \lambda \right| ) } } \end{array}
$$

holds, which completes the demonstration that $f _ { \lambda }$ is a continuous function of $\lambda$

We note also that the function $G f$ is in $\mathcal { C } _ { 2 \pi }$ ,because it is an average of functions that are in $\mathcal { C } _ { 2 \pi }$ . We are now ready to prove the relation between $\| L \| _ { \infty }$ and $\| S _ { n } \| _ { \infty }$

# Theorem 17.3

If $L$ is any bounded linear operator from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { Q } _ { n }$ ,that satisfies the projection condition (17.22), then $\| L \| _ { \infty }$ is bounded below by $\| S _ { n } \| _ { \infty }$

Proof. The key to the proof is that,for every operator $L$ that satisfies the conditions of the theorem, the equation

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } D _ { - \lambda } L D _ { \lambda } { \mathrm { ~ d } } \lambda = S _ { n }
$$

is obtained. In order to establish this equation, we recall from Section 17.1 that it is sufficient to prove that the conditions

$$
G f _ { i } = S _ { n } f _ { i } , \qquad i = 0 , 1 , 2 , \ldots ,
$$

hold,where we are using the notation (17.24),and where $\{ f _ { i } ; i =$ $0 , 1 , 2 , \ldots \}$ is any fundamental set in $\mathcal { C } _ { 2 \pi }$ .Theorem 13.1 shows that,in the notation of equations (13.22)-(13.24), the functions $\{ \cos \{ j . \} ; j =$ $0 , 1 , 2 , \ldots \}$ and $\{ \sin \{ j . \} ; j = 1 , 2 , 3 , . . . \}$ together form a fundamental set. Therefore we prove that equation (17.34) is satisfied for each of these functions. We recall from Section 13.2 that the operator $S _ { n }$ gives the equations

$$
S _ { n } f _ { i } = f _ { i } , \qquad f _ { i } \in \mathcal { Q } _ { n } ,
$$

and

$$
\begin{array} { l l } { S _ { n } \cos { \{ j . \} } = 0 } \\ { S _ { n } \sin { \{ j . \} } = 0 } \end{array} \} , \quad \quad j > n ,
$$

which we compare with the equations that are obtained by applying $\pmb { G }$ to the functions in the fundamental set.

When $f _ { i }$ is in $\mathcal { Q } _ { n } ,$ , then $D _ { \lambda } f _ { i }$ is also in ${ \mathcal { Q } } _ { n }$ .Hence the projection condition (17.22) and the definition (17.23) of the displacement operator imply the identity

$$
D _ { - \lambda } L D _ { \lambda } f _ { i } = D _ { - \lambda } D _ { \lambda } f _ { i } = f _ { i } , \qquad f _ { i } \in \mathcal { Q } _ { n } .
$$

It follows that $G f _ { i }$ is equal to expression (17.35).

Next we consider $\pmb { G }$ cos $\{ j . \}$ when $j > n$ . We require the equation

$$
D _ { \lambda } \cos \{ j . \} = \cos ( j \lambda ) \cos \{ j . \} - \sin ( j \lambda ) \sin \{ j . \} ,
$$

and we require the fact that $L$ cos $\{ j . \}$ and $L$ sin $\{ j . \}$ can be expressed in the form

$$
\begin{array} { r } { L \cos \left\{ j . \right\} = \underset { k = 0 } { \overset { n } { \sum } } \left[ a _ { j k } \cos \left\{ k . \right\} + b _ { j k } \sin \left\{ k . \right\} \right] } \\ { L \sin \left\{ j . \right\} = \underset { k = 0 } { \overset { n } { \sum } } \left[ \alpha _ { j k } \cos \left\{ k . \right\} + \beta _ { j k } \sin \left\{ k . \right\} \right] . } \end{array}
$$

Hence we can write $L D _ { \lambda }$ cos $\{ j . \}$ in terms of the basis functions of $\mathcal { Q } _ { n }$ .An obvious continuation of this procedure gives $D _ { - \lambda } L D _ { \lambda }$ cos $\{ j . \}$ in terms of the same basis functions,and we obtain $\pmb { G }$ cos $\{ j . \}$ by integrating this expression over $\pmb { \lambda }$ . Every term of this integral includes a factor of the form

$$
\int _ { 0 } ^ { 2 \pi } \left[ \cos \left( k \lambda \right) \mathrm { o r } \sin \left( k \lambda \right) \right] \times \left[ \cos \left( j \lambda \right) \mathrm { o r } \sin \left( j \lambda \right) \right] \mathrm { d } \lambda .
$$

Because $\pmb { k }$ is in the interval $[ 0 , n ] .$ ,and because $j$ is greater than $\pmb { n }$ ,each of these factors is zero. It follows that $G \cos \left\{ j . \right\}$ is equal to $S _ { n }$ cos $\{ j . \}$ A similar argument gives the equation

$$
G \sin \{ j . \} = S _ { n } \sin \{ j . \} , \qquad j > n ,
$$

which completes the proof that the operators $_ G$ and $S _ { n }$ are the same.

The required lower bound on $\| L \|$ is a consequence of equation (17.33), the properties of norms, and the fact that $\| D _ { \lambda } \|$ is one. By extending the triangle inequality for norms to integrals, it follows from equation (17.33) that the inequality

$$
\lVert S _ { n } \rVert { \leqslant } { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \left. { D _ { - \lambda } L D _ { \lambda } } \right. \mathbf { d } \lambda
$$

is satisfied. The integrand is bounded above by the relation

$$
\| D _ { - \lambda } L D _ { \lambda } \| \leqslant \| D _ { - \lambda } \| \| L \| \| D _ { \lambda } \| = \| L \| .
$$

Therefore $\| \pmb { S _ { n } } \|$ is a lower bound on $\| \pmb { L } \|$

This theorem gives an excellent reason for taking the point of view that $S _ { n }$ is the best of the linear projection operators from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$

# 17.4 Application to algebraic polynomials

An interesting question is to seek the linear operator $L$ from $\mathcal { C } [ \alpha , b ]$ to $\mathcal { P } _ { n }$ that satisfies the projection condition

$$
L f = f , \qquad f \in { \mathcal { P } } _ { n } ,
$$

and whose norm $\| L \| _ { \infty }$ is as small as possible. Equation (17.44) implies the bound

$$
\| L \| _ { \infty } \geqslant 1 ,
$$

which can hold as an equation when $n = 1$ . Specifically, it is shown in Section 3.1 that, if $L f$ is the function in $\mathcal { P } _ { 1 }$ that is defined by the interpolation conditions

$$
\left. \begin{array} { c } { { \left( L f \right) \left( a \right) = f \left( a \right) } } \\ { { \left( L f \right) \left( b \right) = f \left( b \right) } } \end{array} \right\} ,
$$

then $\| L \| _ { \infty }$ is equal to one. It follows that $\| R _ { n } \|$ is not a lower bound on $\| \pmb { L } \|$ The least value of $\| L \|$ for general $\pmb { n }$ is unknown,but the next theorem gives a useful condition that depends on $\| R _ { n } \|$

# Theorem 17.4

If $L$ is any bounded linear operator from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ ,that satisfies the projection condition (17.44), then the inequality

$$
\| L \| \geqslant \frac { 1 } { 2 } \| R _ { 0 } + R _ { n } \|
$$

holds.

Proof. Because the proof has much in common with the proof of Theorem 17.3, some of the details are omitted.Instead of the displacement operator $\pmb { D } _ { \pmb { \lambda } }$ ， it is helpful to employ an average of two displacements. Therefore the operator $H _ { \lambda }$ is defined by the equation

$$
\begin{array} { r } { ( H _ { \lambda } f ) ( \cos { \theta } ) = \frac { 1 } { 2 } \{ f ( \cos { [ \theta + \lambda ] } ) + f ( \cos { [ \theta - \lambda ] } ) \} , \qquad 0 \leqslant \theta \leqslant \pi . } \end{array}
$$

It should be clear that $H _ { \lambda } f$ is in $\mathcal { C } [ - 1 , 1 ]$ for every $f$ in $\mathcal { C } [ - 1 , 1 ]$ , and that, if $f$ is in $\mathcal { P } _ { n }$ ,then $H _ { \lambda } f$ is also in $\mathcal { P } _ { n }$ . We take for granted that the operator

$$
G = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } H _ { \lambda } L H _ { \lambda } \mathrm { d } \lambda
$$

is well defined. The key equation in the present proof is the identity

$$
{ \cal G } = { \cal R } _ { 0 } + { \cal R } _ { n } ,
$$

and, to establish it,we make use of the fundamental set $\{ T _ { j } ; j = 0$ ， $1 , 2 , \ldots \} ,$ where $T _ { j }$ is still the Chebyshev polynomial

$$
T _ { j } ( \cos \theta ) = \cos { ( j \theta ) } , \qquad 0 \leqslant \theta \leqslant \pi .
$$

Therefore we recall from Section 12.4 that $\scriptstyle { R _ { n } }$ gives the functions

$$
R _ { n } T _ { j } = \Big \{ { T _ { j } } , \qquad j \in n ,
$$

Moreover, it is important to note that the definition (17.48) implies the relation

$$
H _ { \lambda } T _ { j } = \cos { ( j \lambda ) } T _ { j }
$$

for each scalar $\pmb { \lambda }$ .Hence $G T _ { j }$ and $( R _ { 0 } + R _ { n } ) T _ { j }$ are the same if $j \leqslant n$ ,which depends on the projection condition (17.44). The term $\scriptstyle { R _ { 0 } }$ allows for the fact that the integral of the function $\left\{ \cos ^ { 2 } { \left( j \lambda \right) } ; 0 \leqslant \lambda \leqslant 2 \pi \right\}$ when $j = 0$ is twice the value that occurs when $j$ is a positive integer. When $j > n$ ，we may express $L H _ { \lambda } T _ { j }$ in the form

$$
L H _ { \lambda } T _ { j } = \cos { ( j \lambda ) } \sum _ { k = 0 } ^ { n } a _ { j k } T _ { k } ,
$$

where the coefficients $\{ a _ { j k } ; k = 0 , 1 , \ldots , n \}$ are independent of $\lambda$ . Therefore the equation

$$
H _ { \lambda } L H _ { \lambda } T _ { j } = \sum _ { k = 0 } ^ { n } a _ { j k } \cos { ( j \lambda ) } \cos { ( k \lambda ) } T _ { k }
$$

is satisfied. Because the integral over $\pmb { \lambda }$ of each term of the sum is zero, we find the identity

$$
\begin{array} { l } { { G T _ { j } = 0 } } \\ { { \qquad = ( R _ { 0 } + R _ { n } ) T _ { j } , \qquad j > n , } } \end{array}
$$

which completes the proof of expression (17.50).

Because $\| H _ { \lambda } ^ { \cdot } \|$ is one,equations (17.49) and (17.50) give the bound

$$
\begin{array} { l } { \displaystyle \| R _ { 0 } + R _ { n } \| \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \| { \cal H } _ { \lambda } { \cal L } { \cal H } _ { \lambda } \| \mathrm { d } \lambda } \\ { \displaystyle \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } \| { \cal H } _ { \lambda } \| ^ { 2 } \| { \cal L } \| \mathrm { d } \lambda } \\ { \displaystyle = 2 \| { \cal L } \| , } \end{array}
$$

which is the required result.□

By combining this theorem with inequality (17.1),we find that $\| L \| _ { \infty }$ is bounded below by the inequality

$$
\begin{array} { r } { \| L \| _ { \infty } > ( 2 / \pi ^ { 2 } ) \ln { ( n + 1 ) } - \frac { 1 } { 2 } . } \end{array}
$$

It follows from Theorem 17.2 that the sequence $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ does not converge uniformly to $f$ for all $f$ in $\mathcal { C } [ - 1 , 1 ] ,$ if each $X _ { n }$ is any linear operator from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ that leaves polynomials of degree $\pmb { n }$ unchanged. However，we recall from Section 6.3 that the Bernstein operators (6.23) give uniform convergence.Perhaps it would be useful to investigate algorithms for calculating polynomial approximations that have bounded norms, that are linear,and that are more accurate than the Bernstein method when $f$ can be differentiated more than once.

# 17 Exercises

17.1 Prove that the space ${ \mathcal { C } } [ a , b ]$ is complete with respect to the 8-norm.

17.2 Let $\{ \xi _ { i } ; i = 2 , 3 , 4 , . . . \}$ be an infinite sequence of numbers in the interval $[ a , b ]$ ,such that every point of $[ a , b ]$ is a limit point of the sequence. Prove that the functions $\{ \phi _ { 0 } ( x ) = 1$ ； $a \leqslant x \leqslant b $ ， $\{ \phi _ { 1 } ( x ) = x$ ； $a \leqslant x \leqslant b \}$ and $\{ \phi _ { i } ( x ) = \left| x - \xi _ { i } \right|$ ； $a \leqslant x \leqslant b$ ； $i = 2 , 3$ ， $4 , \ldots . \}$ are a fundamental set in $\mathcal { C } [ a , b ]$

17.3 Let $\mathcal { B }$ be the space $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ of periodic functions with continuous first derivatives. The Fourier series operators $\{ S _ { n } ; n = 0 , 1$ ， $2 , \ldots \} \operatorname* { m a p } \mathcal { B }$ into $\mathcal { B }$ and the sequence of norms $\smash { \{ \| S _ { n } \| _ { \infty } ; n = 0 , 1 \} }$ ， $2 , \ldots . \}$ diverges.Nevertheless,Theorem 15.1 shows that the sequence of functions $\left\{ S _ { n } f ; n = 0 , 1 , 2 , \ldots \right\}$ converges uniformly to $f$ for all $f$ in $\mathcal { B }$ .Explain why there is not a conflict with the uniform boundedness theorem 17.2.

17.4 Calculate the right-hand side of inequality (17.47) in the case when $n = 1$ . You should find,of course, that it is not greater than one.

17.5Prove that the operator $\pmb { G }$ of equation (17.49) is well defined.

17.6 For every positive integer $\pmb { n }$ ,let $\{ \xi _ { n i } ; i = 0 , 1 , \ldots , 2 n \}$ be a set of distinct points of $[ a , b ] ,$ ，arranged in ascending order,and such that $\xi _ { n 0 } = a$ and $\xi _ { n 2 n } = b$ .For any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ;$ ,the function $X _ { n } f$ is defined to be the piecewise quadratic polynomial that is a single quadratic on each of the intervals $\{ [ \xi _ { n i } , \xi _ { n i + 2 } ]$ ； $i = 0 , 2 , \ldots ,$ $2 n - 2 \}$ ， and that interpolates the function values $\{ f ( \xi _ { n i } ) ; i = 0 \}$ $1 , \ldots , 2 n \}$ . Find necessary and sufficient conditions on the points $[ \{ \xi _ { n i } ; i = 0 , 1 , \ldots , 2 n \}$ ； $n = 1 , 2 , 3 , \ldots ]$ for the sequence $\{ X _ { n } f$ $n = 1 , 2 , 3 , \ldots \}$ to converge uniformly to $f$ for all $f$ in ${ \mathcal { C } } [ a , b ]$

17.7 Prove that the powers $\{ \phi _ { k } ( x ) = x ^ { k } ; - 1 \leqslant x \leqslant 1 ; k = 0 , 2 , 3 ,$ 4,...},excluding the linear function $\{ \phi _ { 1 } ( x ) = x ; - 1 \leqslant x \leqslant 1 \} .$ ， are a fundamental set in $\mathcal { C } [ - 1 , 1 ]$ ，but that the Chebyshev polynomials $\{ T _ { k } ; k = 0 , 2 , 3 , 4 , \ldots \}$ ，excluding the linear term, are not a fundamental set in $\mathcal { C } [ - 1 , 1 ]$

17.8 Let $\{ L _ { n } ; n = 0 , 1 , 2 , \ldots \}$ be a sequence of linear operators from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { C } [ - 1 , 1 ]$ such that, for every $f$ in $\mathcal { C } [ - 1 , 1 ] ,$ the sequence of functions $\{ L _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$ Let $X _ { n }$ be the operator

$$
X _ { n } = \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } H _ { \lambda } L _ { n } H _ { \lambda } \mathrm { d } \lambda - R _ { 0 } ,
$$

where $H _ { \lambda }$ and $\scriptstyle { R _ { 0 } }$ occur in the proof of Theorem 17.4. Prove that, for every $f$ in $\mathcal { C } [ - 1 , 1 ] ,$ , the sequence $\{ X _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$ Note that $L _ { n }$ need not be a projection.

17.9 Construct a linear operator $\pmb { L }$ from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { 2 }$ ，satisfying the projection condition (17.44),whose norm $\| L \| _ { \infty }$ is as small as you can make it. By letting $L$ have the form $\scriptstyle { \frac { 1 } { 2 } } ( L _ { \lambda } + L _ { \mu } )$ ,where,for any $f$ in $\mathcal { C } [ - 1 , 1 ] , L _ { \lambda } f$ is the quadratic polynomial that interpolates the function values $\{ f ( - \lambda ) , f ( 0 ) , f ( \lambda ) \}$ ,it is possible for $\| L \| _ { \infty }$ to be less than $\textstyle { \frac { 5 } { 4 } }$

17.10 Let $\bar { \pmb { S } } [ \pmb { n } , \pmb { N } ]$ be the operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that corresponds to the discrete Fourier series method of Section 13.3.Let $L$ be any linear operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that satisfies the projection condition (17.22) and that has the property that,for any $f$ in $\mathcal { C } _ { 2 \pi } ,$ the function $L f$ depends only on the function values $\{ f ( 2 \pi j / N ) ; j = 0 , 1 , \ldots , N - 1 \}$ . Prove that, if $\begin{array} { r } { n < \frac { 1 } { 2 } N , } \end{array}$ then $\| L \| _ { \infty }$ is bounded below by $\| \bar { \pmb { S } } [ n , N ] \| _ { \infty }$

# Interpolation by piecewise polynomials

# 18.1 Local interpolation methods

We have noted several disadvantages of polynomial approximations. In Chapter 3,for example,it is pointed out that they are not well suited to the approximation of the function shown in Figure 1.1, because, if $\{ p ( x ) ; - \infty < x < \infty \}$ is a polynomial whose degree is non-zero, then $\left| p ( x ) \right|$ becomes unbounded as $| x |$ tends to infinity. It is noted also that it can be highly inefficient to use an analytic function to represent a function that is not analytic. Therefore it happens often that, in order to obtain sufficient accuracy by a polynomial approximation, it is necessary to let the degree of the polynomial be high.In this case there may not be sufficient data to determine all the coefficients properly, the effort of calculating the polynomial is increased,and the tendencies towards unboundedness are exacerbated. Really polynomials are quite inappropriate for general use as approximating functions. Because piecewise polynomials are much more successful in practice, they are studied in the next four chapters.

We use the notation $\{ s ( x ) ; a \leqslant x \leqslant b \}$ for a piecewise polynomial. In this chapter $\pmb { s }$ is defined by the interpolation equations

$$
s ( x _ { j } ) = f ( x _ { j } ) , \qquad j = 1 , 2 , \ldots , m ,
$$

where the function values $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ are given, and where the data points satisfy the conditions

$$
a = x _ { 1 } < x _ { 2 } < \ldots < x _ { m } = b .
$$

This section is concerned with interpolation methods that have the property that, for any fixed $x$ ,the function value $\pmb { s } ( \pmb { x } )$ depends on only a few of the data, whose abscissae are close to $\pmb { x }$

The most frequently used method of this type, namely piecewise linear interpolation, has been mentioned already in Section 3.4.In each of the intervals $\{ x _ { j } \leqslant x \leqslant x _ { j + 1 } ; j = 1 , 2 , \ldots , m - 1 \} , s ( x )$ is defined by the formula

$$
s \left( x \right) = f ( x _ { j } ) + \frac { x - x _ { j } } { x _ { j + 1 } - x _ { j } } \left[ f ( x _ { j + 1 } ) - f ( x _ { j } ) \right] ,
$$

which is equivalent to equation (3.29). The main advantages of the method are that $\{ s ( x ) ; a \leqslant x \leqslant b \}$ adapts itself easily to the form of $\{ f ( x )$ ； $a \leqslant x \leqslant b \}$ ,and that the error $ \| f - s \| _ { \infty }$ can be controlled directly by the spacing between data points.However, in order to achieve a prescribed accuracy,piecewise linear interpolation usually requires far more data than some higher order methods.

We consider two higher order methods that are quite useful. Both of them define $\pmb { S }$ to be a cubic polynomial, $s _ { j }$ say,on each of the intervals $\{ x _ { j } \leqslant x \leqslant x _ { j + 1 } ; \ j = 1 , 2 , \ldots , m - 1 \}$ .Therefore there are two degrees of freedom in $s _ { j }$ after equation (18.1) is satisfied. In the first method $s _ { j }$ is defined by interpolating two more function values. If $2 \leqslant j \leqslant m - 2$ ,these values are $f ( x _ { j - 1 } )$ and $f ( x _ { j + 2 } )$ ,but, if $j = 1$ or $m - 1$ , they are $f ( x _ { 3 } )$ and $f ( x _ { 4 } )$ or $f ( x _ { m - 3 } )$ and $f ( x _ { m - 2 } )$ respectively. In the other method the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ are given or are calculated at the beginning of the interpolation procedure. For example, if $3 \leqslant j \leqslant m - 2$ , we may let $\pmb { s } ^ { \prime } ( \pmb { x } _ { j } )$ be the derivative at $x _ { j }$ of the quartic polynomial that interpolates the five function values $\{ f ( x _ { k } ) ; k = j - 2 , j - 1 , j , j + 1 , j + 2 \}$ . The derivatives $\pmb { s } ^ { \prime } ( \pmb { x } _ { j } )$ and $\pmb { s } ^ { \prime } ( \pmb { x } _ { j + 1 } )$ fix the two degrees of freedom in $s _ { j }$ for each $j .$ Hence $s _ { j } ( x )$ is the cubic polynomial

$$
s _ { j } ( x ) = f ( x _ { j } ) + s ^ { \prime } ( x _ { j } ) ( x - x _ { j } ) + c _ { 2 } ( x - x _ { j } ) ^ { 2 } + c _ { 3 } ( x - x _ { j } ) ^ { 3 } ,
$$

where the coefficients have the values

$$
c _ { 2 } = \frac { 3 [ f ( x _ { j + 1 } ) - f ( x _ { j } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } } - \frac { 2 s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) } { x _ { j + 1 } - x _ { j } }
$$

and

$$
c _ { 3 } = \frac { 2 [ f ( x _ { j } ) - f ( x _ { j + 1 } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 3 } } + \frac { s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } } .
$$

It should be clear that each of the three interpolation methods that have been mentioned gives a function $\{ s ( x ) ; a \leqslant x \leqslant b \}$ that is continuous, but only the last method makes the first derivative $\{ s ^ { \prime } ( x ) ; a \leqslant x \leqslant b \}$ continuous also.

In order to compare the accuracy of the first two methods, in the case when $f$ has a continuous fourth derivative, we refer to the expression for the error of polynomial interpolation that is stated in Theorem 4.2. If $\pmb { s }$ is the cubic polynomial that interpolates the data $\{ f ( x _ { j - 1 } ) , f ( x _ { j } ) , f ( x _ { j + 1 } ) \}$ $f ( x _ { j + 2 } ) \}$ ,and if $x$ is in the interval $[ x _ { j - 1 } , x _ { j + 2 } ]$ ,then the theorem gives the bound

$$
\begin{array} { r } { \big \vert f ( x ) - s ( x ) \big \vert \leqslant \frac { 1 } { 2 4 } \displaystyle \prod _ { i = j - 1 } ^ { j + 2 } \big \vert x - x _ { i } \big \vert \operatorname* { m a x } _ { x _ { j - 1 } \leqslant \xi \leqslant x _ { j + 2 } } \big \vert f ^ { ( 4 ) } ( \xi ) \big \vert . } \end{array}
$$

This inequality suggests that doubling the number of data can improve the accuracy by a factor of sixteen, but the corresponding result for the interpolation formula (18.3) is that there is only a fourfold increase in accuracy. Therefore piecewise linear interpolation is normally less efficient. In the third method the values of the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j =$ $1 , 2 , \ldots , m \}$ can usually be chosen so that this method gives the best accuracy,which is demonstrated in Exercise 18.1.However, if $f$ is not in $\mathcal { C } ^ { ( 4 ) } [ a , b ] .$ then piecewise inear interpolationmay be preferable,especially if the spacing between data points is irregular.

Because all of these interpolation methods depend linearly on the data, each one can be expressed in the form

$$
s ( x ) = \sum _ { k = 1 } ^ { m } l _ { k } ( x ) f ( x _ { k } ) , \quad a \leqslant x \leqslant b ,
$$

where $l _ { k }$ is a ‘cardinal function’ that depends on the positions of the data points,but that is independent of the given function values.As in equation (4.4), the cardinal functions satisfy the equations

$$
l _ { k } ( x _ { j } ) = \delta _ { k j } ,
$$

in order that the interpolation conditions (18.1) hold.If the interpolation method is‘local'，then $l _ { k } ( x )$ is non-zero only if $x$ is close to $x _ { k }$ A convenient way of obtaining $l _ { k }$ is to apply the interpolation procedure to the data $\{ f ( x _ { j } ) = \delta _ { k j } ; j = 1 , 2 , \ldots , m \}$ .The results of this calculation for the three interpolation methods of this section are shown in Figure 18.1, where $k$ is remote from the ends of the interval $[ 1 , m ]$ ,and where the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ for the last method are obtained in the way that is suggested before equation (18.4).It is clear that only the last method makes $\{ \boldsymbol { s } ^ { \prime } ( \boldsymbol { x } )$ ； $a \leqslant x \leqslant b $ continuous for general data $\{ f ( x _ { j } )$ ； $j = 1 , 2 , \dots , m \}$

The figure suggests that there are many ways of choosing cardinal functions so that equation (18.8) gives a tolerable approximation to $\{ f ( x )$ ； $a \leqslant x \leqslant b $ . The ideal properties for a cardinal function are that it is non-zero over only a small part of the range $[ a , b ] .$ ,it is smooth, the form of $\pmb { S }$ is convenient for computer calculations, $\| l _ { k } \| _ { \infty }$ is not much larger than one,and, if $f$ can be differentiated many times, then the error $\| f - s \| _ { \infty }$ of the approximation (18.8） is small. A good way of achieving the last condition is to ensure that the error is zero when $f$ is a polynomial of suitable order, but the last two conditions can conflict when the spacing between data points is highly irregular.These comments assume that equation (18.9) is satisfied,but we find in Chapter 2O that it can be advantageous to work with an approximation of the form (18.8) that does not interpolate the data $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$

# 18.2 Cubic spline interpolation

Cubic spline functions are now used widely in computer calculations for the approximation of continuous functions of one variable. We recall from Chapter 3 that a cubic spline $\{ s ( x ) ; a \leqslant x \leqslant b \}$ is composed of cubic polynomial pieces, that are joined so that the second derivative $\{ s ^ { \prime \prime } ( x ) ; a \leqslant x \leqslant b \}$ is continuous. In Sections 18.2 and 18.3 we consider interpolation by cubic splines to the data $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ ，when the cubic polynomial pieces meet at the data points. We continue to assume that condition (18.2） is satisfied. Because it is convenient to calculate the value of the spline from expression (18.4) when $x$ is in the interval $[ x _ { j } , x _ { j + 1 } ] _ { 2 }$ ，we study methods for obtaining the derivative values $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ from the data. One important difference between cubic spline interpolation and the methods that are described in the last section is that, if $\pmb { s }$ is a cubic spline, then each of the pieces of $\pmb { s }$ usually depends on all the data.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0004_pages_0211-0280/auto/images/5fe051391afc26fd13a87eda269882fdd16561f7e0e778acfcd46b5c09f1f6d1.jpg)  
Figure 18.1. Cardinal functions for three local interpolation methods.

The condition that $s ^ { \prime \prime }$ is continuous at the data points $\{ x _ { k } ; ~ k = 2$ $3 , \ldots , m - 1 \}$ gives equations that have to be satisfied by the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ . In order to derive these equations,we note that expression (18.4) implies the value

$$
\begin{array} { l } { s ^ { \prime \prime } ( x _ { j + 1 } ) = 2 c _ { 2 } + 6 c _ { 3 } ( x _ { j + 1 } - x _ { j } ) \qquad } \\ { \quad = \frac { 6 \left[ f ( x _ { j } ) - f ( x _ { j + 1 } ) \right] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } } + \frac { 2 s ^ { \prime } ( x _ { j } ) + 4 s ^ { \prime } ( x _ { j + 1 } ) } { \left( x _ { j + 1 } - x _ { j } \right) } , } \end{array}
$$

which, if $j \leqslant m - 2$ ,has to agree with the second derivative at $x _ { j + 1 }$ of the cubic polynomial that is equal to $\pmb { s }$ on the interval $[ x _ { j + 1 } , \ x _ { j + 2 } ]$ An expression for this polynomial can be obtained by replacing $j$ by $( j + 1 )$ in equations (18.4), (18.5) and (18.6). Hence the relation

$$
\begin{array} { l } { \displaystyle \frac { s ^ { \prime } ( x _ { k - 1 } ) + 2 s ^ { \prime } ( x _ { k } ) } { ( x _ { k } - x _ { k - 1 } ) } + \frac { 2 s ^ { \prime } ( x _ { k } ) + s ^ { \prime } ( x _ { k + 1 } ) } { ( x _ { k + 1 } - x _ { k } ) } } \\ { \displaystyle = \frac { 3 [ f ( x _ { k } ) - f ( x _ { k - 1 } ) ] } { \left( x _ { k } - x _ { k - 1 } \right) ^ { 2 } } + \frac { 3 [ f ( x _ { k + 1 } ) - f ( x _ { k } ) ] } { \left( x _ { k + 1 } - x _ { k } \right) ^ { 2 } } } \end{array}
$$

is the condition for second derivative continuity at $x _ { k }$ .Because we give special attention to the case when the spacing between data points is constant

$$
x _ { j + 1 } - x _ { j } = h , \qquad j = 1 , 2 , \ldots , m - 1 ,
$$

we note that in this case expression (18.11) simplies to the form

$$
s ^ { \prime } ( x _ { k - 1 } ) + 4 s ^ { \prime } ( x _ { k } ) + s ^ { \prime } ( x _ { k + 1 } ) = 3 [ f ( x _ { k + 1 } ) - f ( x _ { k - 1 } ) ] / h .
$$

One method, that is sometimes recommended, for fixing the two degrees of freedom that remain in the derivatives $\{ s ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ ， after equation (18.11） is satisfied for $k = 2 , 3 , \ldots , m - 1$ , is to use a separate preliminary procedure to calculate or to estimate $\pmb { s } ^ { \prime } ( \pmb { x } _ { 1 } )$ and $s ^ { \prime } ( x _ { m } )$ . In this case the second derivative continuity conditions give a tridiagonal system of linear equations in the unknowns $\lbrace s ^ { \prime } ( x _ { j } ) ; j =$ $2 , 3 , \ldots , m - 1 \}$ ， which can be solved easily because it is diagonally dominant. Several other methods for fixing the two degrees of freedom are mentioned in the next section.

In the remainder of this section we consider cubic spline interpolation, when there are an infinite number of uniformly spaced data points

$$
x _ { j } = j h , \qquad j = 0 , \pm 1 , \pm 2 , . . . .
$$

This case is studied because it is easy to analyse,and because the cardinal

functions of the interpolation procedure help one to understand some of the main properties of spline approximation. We may express $\pmb { s }$ in the form

$$
s ( x ) = \sum _ { j = - \infty } ^ { \infty } l _ { j } ( x ) f ( x _ { j } ) , \qquad - \infty < x < \infty ,
$$

where each $l _ { j }$ is a cardinal spline function that satisfies the equations

$$
l _ { j } ( x _ { k } ) = \delta _ { j k } , \qquad k = 0 , \pm 1 , \pm 2 , . . . .
$$

Because the range of the variable $x$ is infinite,there is the possibility that $l _ { j }$ is unbounded,which would be unacceptable, because then the approximation (18.15） would be highly sensitive to the function value $f ( x _ { j } )$ .Fortunately it happens that the two degrees of freedom that occur in cubic spline interpolation, when the number of data points is finite,can be used in just one way to make $\{ l _ { j } ( x ) ; - \infty < x < \infty \}$ bounded when the data points have the values (18.14). The derivatives $\{ l _ { j } ^ { \prime } ( x _ { k } ) ; k = 0 , \pm 1 , \pm 2 , . . . \}$ of the bounded cardinal spline are found in the following way.

The second derivative continuity conditions that correspond to equation (18.13) have the form

$$
\begin{array} { r l r } {  { l _ { j } ^ { \prime } ( x _ { k - 1 } ) + 4 l _ { j } ^ { \prime } ( x _ { k } ) + l _ { j } ^ { \prime } ( x _ { k + 1 } ) } } \\ & { } & { = 3 [ \delta _ { j k + 1 } - \delta _ { j k - 1 } ] / h , \qquad k = 0 , \pm 1 , \pm 2 , \ldots . } \end{array}
$$

It is important to note that the right-hand side is zero if $k \geqslant j + 2$ It follows from the theory of recurrence relations that the conditions

$$
l _ { j } ^ { \prime } ( x _ { k } ) = \alpha ( - 2 + \sqrt { 3 } ) ^ { k - j } + \beta ( - 2 - \sqrt { 3 } ) ^ { k - j } , \qquad k \geqslant j + 1 ,
$$

hold, where $_ \alpha$ and $\beta$ are constants, and where $( - 2 \pm { \sqrt { 3 } } )$ are the roots of the quadratic equation

$$
1 + 4 \theta + \theta ^ { 2 } = 0 .
$$

In order that $\{ l _ { j } ( x ) ; - \infty < x < \infty \}$ is bounded, the value of $\beta$ must be zero. Similarly, because the right-hand side of expression (18.17) is zero for $k \leqslant j - 2$ ,the conditions

$$
l _ { j } ^ { \prime } ( x _ { k } ) = \gamma ( - 2 + \sqrt { 3 } ) ^ { j - k } , \qquad k \leqslant j - 1 ,
$$

must hold also, where $\gamma$ is another constant. The numbers $\alpha , \gamma$ and $l _ { j } ^ { \prime } ( x _ { j } )$ are determined uniquely by giving $k$ the values $j - 1 , ~ j$ and $j + 1$ in equation (18.17). Hence the bounded cardinal spline $l _ { j }$ has the derivatives

$$
\begin{array} { r } { l _ { j } ^ { \prime } ( x _ { k } ) = \left\{ \begin{array} { c c } { - 3 ( - 2 + \sqrt { 3 } ) ^ { j - k } / h , } & { \quad k < j } \\ { 0 , } & { \quad k = j } \\ { 3 ( - 2 + \sqrt { 3 } ) ^ { k - j } / h , } & { \quad k > j . } \end{array} \right. } \end{array}
$$

This cardinal function is shown in Figure 18.2. It is an oscillatory function that decays exponentially by the factor $( { \sqrt { 3 - 2 } } )$ per data point as $x$ moves away from $x _ { j } .$ It follows from equation (18.15) that, if $x$ is not a data point, then $s ( x )$ depends on all the function values $\{ f ( x _ { j } ) ; j = 0 , \pm 1 \}$ $\pm 2 , \ldots . \}$ ，but the contribution from $f ( x _ { j } )$ to $\pmb { s } ( \pmb { x } )$ is usually negligible when ${ \left| x - x _ { j } \right| } / h$ is large.

It is easy to calculate the $\infty$ -norm of the interpolation algorithm (18.15) when expression (18.21) gives the derivatives of the cardinal functions. Because each interval between data points is similar, the norm has the value

$$
\begin{array} { r l } { \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } \ \operatorname* { m a x } _ { \| f \| _ { \infty } \leq 1 } \ \Big | _ { j = - \infty } l _ { j } ( x ) f ( x _ { j } ) \Big | } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } \ \sum _ { j = - \infty } ^ { \infty } | l _ { j } ( x ) | } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } \ \sum _ { j = 0 } ^ { \infty } \ ( - 1 ) ^ { i } [ l _ { - j } ( x ) + l _ { j + 1 } ( x ) ] } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } p ( x ) , } \\ { = \displaystyle \operatorname* { m a x } _ { 0 \leq x \leq h } p ( x ) , } \end{array}
$$

say, where the third line of this equation depends on the sign properties of the cardinalfunction that are shown in Figure 18.2.The function $\{ p ( { \pmb x } )$ ； $0 \leqslant x \leqslant h \}$ is a cubic polynomial that is defined by the equations

$$
p ( 0 ) = p ( h ) = 1
$$

and

$$
\begin{array} { r } { p ^ { \prime } ( 0 ) = - p ^ { \prime } ( h ) = \underset { k = - \infty } { \overset { \infty } { \sum } } \left| l _ { j } ^ { \prime } ( x _ { k } ) \right| } \\ { = 3 ( \sqrt { 3 } - 1 ) / h . } \end{array}
$$

Hence the $\infty$ -norm has the value $p ( \frac { 1 } { 2 } h ) = ( 1 + 3 \surd 3 ) / 4 \approx 1 . 5 5$ ，which is remarkably small. Therefore cubic spline interpolation to equally spaced

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0004_pages_0211-0280/auto/images/0fa59eac8d7112b6387a665724b8aa21310c03173cc38c539aacfd7b8dc11989.jpg)  
Figure 18.2.A cubic spline cardinal function.

data on the whole real line is a reliable procedure.It is analysed further in Section 22.4.

# 18.3 End conditions for cubic spline interpolation

It has been noted that, if $\{ s ( x ) ; a \leqslant x \leqslant b \}$ is a cubic spline that has knots at the points $\{ x _ { j } ; j = 2 , 3 , \ldots , m - 1 \}$ , and that satisfes the interpolation conditions (18.1), then there are two degrees of freedom in s.A change in the method that fixes this freedom alters $\pmb { s }$ by a spline, $\sigma$ say, that is zero at all the interpolation points. Therefore,if the data points are equally spaced, then equation (18.13) implies the conditions

$$
\sigma ^ { \prime } ( x _ { k - 1 } ) + 4 \sigma ^ { \prime } ( x _ { k } ) + \sigma ^ { \prime } ( x _ { k + 1 } ) = 0 , \qquad k = 2 , 3 , \ldots , m - 1 .
$$

It follows that, if $\bar { s }$ is any particular cubic spline that interpolates the data, then the general interpolating spline has the derivative values

$$
\begin{array} { c } { { s ^ { \prime } ( x _ { j } ) = \bar { s } ^ { \prime } ( x _ { j } ) + \alpha ( - 2 + \sqrt { 3 } ) ^ { j - 1 } + \beta ( - 2 + \sqrt { 3 } ) ^ { m - j } , } } \\ { { j = 1 , 2 , \ldots , m , } } \end{array}
$$

where $\pmb { \alpha }$ and $\beta$ are constants. This section considers procedures that define the values of $\pmb { \alpha }$ and $\beta$

Expression (18.26) shows that the influence of $_ \alpha$ is strongest at the left-hand end of the range $[ a , b ] ,$ ，while the influence of $\beta$ is strongest at the right-hand end. Therefore, in order that $\pmb { s }$ depends stably on the procedure that fixes $_ { \pmb { \alpha } }$ and $\beta$ ,it is necessary to impose a condition on $\pmb { s }$ at each end of the range. Normally this remark is also true in the general case when the distribution of data points is irregular. Therefore, obtaining the values of $\pmb { s } ^ { \prime } ( \pmb { a } )$ and $s ^ { \prime } ( b )$ from a preliminary calculation,which is suggested in the last section, is a suitable method for determining the free parameters of $\pmb { s }$

A different procedure that is used sometimes is to set $s ^ { \prime \prime } ( a ) = s ^ { \prime \prime } ( b ) = 0$ ， which makes s a ‘natural spline'. Natural splines have some interesting theoretical properties that are studied in Chapter 23,but in practice they are often poor approximating functions, because they waste the accuracy that can be achieved when $f$ is in $\mathcal { C } ^ { ( 4 ) } [ a , b ]$ .When $f ^ { \prime \prime } ( a )$ and $f ^ { \prime \prime } ( b )$ are both non-zero, the error $\| f - s \| _ { \infty }$ of a natural spline approximation is bounded below by a multiple of max ${ \left[ { \left( { { x } _ { 2 } } - { x } _ { 1 } \right) ^ { 2 } } \right. }$ ， $\left( x _ { m } - x _ { m - 1 } \right) ^ { 2 } ] ,$ instead of being of fourth order in the spacing between the data points. It is better to choose two suitable properties that would be obtained by a good spline approximation when $f$ is a polynomial of degree at least three,and to force $\pmb { s }$ to have these properties.

For example, if $f$ is a cubic polynomial, then $\pmb { s }$ is equal to $f$ only if $\pmb { s } ^ { \prime \prime \prime }$ is continuous throughout $[ a , b ]$ . Therefore the property that $\pmb { s }$ can equal a general cubic polynomial is preserved if $_ { \alpha }$ and $\beta$ ,in equation (18.26),are defined by requiring any two of the third derivative discontinuities

$$
d _ { j } = s ^ { \prime \prime \prime } ( x _ { j } + ) - s ^ { \prime \prime } ( x _ { j } - ) , \qquad j = 2 , 3 , \ldots , m - 1 ,
$$

to be zero. Equations (18.4) and (18.6) show that $d _ { j }$ has the value

$$
d _ { j } = \frac { 1 2 [ f ( x _ { j } ) - f ( x _ { j + 1 } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 3 } } + \frac { 6 [ s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) ] } { \left( x _ { j + 1 } - x _ { j } \right) ^ { 2 } }
$$

$$
- \frac { 1 2 [ f ( x _ { j - 1 } ) - f ( x _ { j } ) ] } { \left( x _ { j } - x _ { j - 1 } \right) ^ { 3 } } - \frac { 6 [ s ^ { \prime } ( x _ { j - 1 } ) + s ^ { \prime } ( x _ { j } ) ] } { \left( x _ { j } - x _ { j - 1 } \right) ^ { 2 } } .
$$

A good method for determining $\pmb { s }$ is to set $d _ { 2 } = d _ { m - 1 } = 0$ ,in addition to satisfying condition (18.11) for $k = 2 , 3 , \ldots , m - 1$ .Hence the required derivatives $\{ \pmb { s } ^ { \prime } ( \pmb { x } _ { j } )$ $; j = 1 , 2 , \ldots , m \}$ are defined by a square system of linear equations,that is easy to solve, because it is almost tridiagonal and almost diagonally dominant. Another technique for fixing the values of the parameters $_ { \alpha }$ and $\beta$ is to set $d _ { 2 } = d _ { 3 }$ and $d _ { m - 2 } = d _ { m - 1 } ,$ . It has the strong advantage that it minimizes the error $ \| f - s \| _ { \infty }$ when the spacing between data points is uniform and $f$ is any quartic polynomial.

Two important and related questions,which we consider in the case when the data points have the constant spacing (18.12),are the effect that the data $\{ f ( x _ { j } ) ; j = 1 , 2 , \ldots , m \}$ have on the parameters $_ { \alpha }$ and $\beta$ ,and the effect that $_ { \pmb { \alpha } }$ and $\beta$ have on the spline $\{ s ( x ) ; a \leqslant x \leqslant b \}$ In order that the values of $_ { \alpha }$ and $\beta$ are unambiguous,it is necessary to choose a particular function $\tilde { s }$ in equation (18.26). Because of the nice properties that are obtained by the interpolating spline (18.15) when the cardinal functions have the form shown in Figure 18.2,we define $\bar { s }$ in the following way. We continue the uniform spacing of data points along the whole real line,and we assign fixed values to $f ( x _ { j } )$ at the new data points. For instance,these function values may be set to zero,if it is not important to preserve continuity in the extension of $f .$ We let $\bar { s }$ be the part of the function (18.15) that is relevant to the range $[ a , b ]$

The two conditions on $\{ s ( x ) ; a \leqslant x \leqslant b \}$ that fix the parameters $\pmb { \alpha }$ and $\beta$ give these parameters non-zero values only if the required conditions on $\pmb { s }$ are not obtained by s. The equation

$$
{ \bar { s } } ( x ) = \sum _ { j = - \infty } ^ { \infty } l _ { j } ( x ) f ( x _ { j } ) , \qquad a \leqslant x \leqslant b ,
$$

shows directly the contribution from $f ( x _ { j } )$ to $\bar { s } ( \boldsymbol { x } )$ ，and we note the presence of the scaling factor $l _ { j } ( x )$ . Therefore,in the usual case when $\pmb { \alpha }$ and $\beta$ depend on the form of $\bar { s }$ near the ends of the range $[ a , b ] ,$ , it follows from Figure 18.2 and equation (18.21),that the contribution from $f ( x _ { j } )$ to $\pmb { \alpha }$ or $\beta$ includes the factor $( 2 - { \sqrt { 3 } } ) ^ { j }$ or $( 2 - \sqrt { 3 } ) ^ { m - j }$ .Hence the values of $\pmb { \alpha }$ and $\beta$ depend mainly on the data that are near the ends of the interval $[ a , b ]$ . Moreover,equation (18.26) shows that the effect of the end conditions on $s ( x )$ decays exponentially if $x$ is moved towards the centre of the range $[ a , b ]$

These remarks suggest that, when $x$ is well inside the interval $[ a , b ] ,$ then it is usually adequate to regard $s ( x )$ as the value of a cubic spline that interpolates $f$ on the infinite range $- \infty < x < \infty$ . Thus one can obtain useful error estimates,and one can study the behaviour of the error as $h$ tends to zero,in a way that avoids the complications that come from the choice of end conditions.

# 18.4 Interpolating splines of other degrees

In most of this section we consider interpolation by quadratic splines.It is possible to satisfy the conditions (18.1） by letting $\pmb { s }$ be a quadratic polynomial on each of the intervals $\{ [ x _ { j } , x _ { j + 1 } ]$ ； $j = 1 , 2 , \dots ,$ $m - 1 \}$ ，where the joins of the quadratic pieces are such that the frst derivative $\{ s ^ { \prime } ( x ) ; a \leqslant x \leqslant b \}$ is continuous. This procedure, however, has some severe disadvantages. In particular, the following example shows that there are difficulties in adapting the distribution of data points to the form of $f .$

We let $f$ be the continuous function

$$
f ( x ) = \left\{ { \begin{array} { l l } { 0 , \qquad - 1 \leqslant x \leqslant 0 } \\ { x , \qquad 0 \leqslant x \leqslant 1 . } \end{array} } \right.
$$

We suppose that the number of data points $^ m$ is given,and that we are free to choose the positions of the data points, subject to the conditions

$$
- 1 = x _ { 1 } < x _ { 2 } < \ldots < x _ { m } = 1 ,
$$

and subject to the restriction that one of the data points, $x _ { n }$ say, is at zero. If $\pmb { s }$ is to be a quadratic spline that satisfies the conditions of the previous paragraph, we find that, because $x _ { n }$ is zero,it is not possible to make the error $\| f - s \| _ { \infty }$ very small by clustering the data points near the first derivative discontinuity of $f ,$ even though $f$ is equal to a single segment of a quadratic spline on each side of the discontinuity. In order to reach this conclusion we note that, because $\pmb { s }$ is a quadratic function on each of the intervals $\{ [ x _ { j } , x _ { j + 1 } ] ; j = 1 , 2 , \dots , m - 1 \}$ , the equations

$$
\begin{array} { r } { \frac { 1 } { 2 } [ s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) ] = [ s ( x _ { j + 1 } ) - s ( x _ { j } ) ] / ( x _ { j + 1 } - x _ { j } ) , \qquad } \\ { j = 1 , 2 , \ldots , m - 1 , } \end{array}
$$

are satisfied. Thus expressions (18.1) and (18.30) give the conditions

$$
\begin{array} { r } { \frac 1 2 [ s ^ { \prime } ( x _ { j } ) + s ^ { \prime } ( x _ { j + 1 } ) ] = \left\{ \begin{array} { l l } { 0 , } & { \quad j < n } \\ { 1 , } & { \quad j \geq n , } \end{array} \right. } \end{array}
$$

which imply the identities

$$
s ^ { \prime } ( x _ { j + 2 } ) = s ^ { \prime } ( x _ { j } ) , \qquad j \neq n - 1 .
$$

In particular, the derivatives $\{ s ^ { \prime } ( x _ { n } ) , s ^ { \prime } ( x _ { n \pm 2 } ) , s ^ { \prime } ( x _ { n \pm 4 } ) , . . . \}$ are all equal. It follows that $\pmb { S }$ cannot adapt itself efficiently to the slopes of both of the straight line sections of $f .$ The difficulty is due to the fact that the cardinal functions of quadratic spline interpolation do not usually become small when $x$ is remote from the data point at which the cardinal function is equal to one. For example, Figure 18.3 shows a symmetric cardinal function, where the distribution of data points is uniform.

However, there is a way of making quadratic spline interpolation a flexible procedure.It is to position the knots of $\pmb { s }$ midway between the data points.We study this technique in the case when the range of $\boldsymbol { x }$ is the whole real line,and when the data points have the equally spaced values $\{ x _ { j } = j h ; j = 0 , \pm 1 , \pm 2 , . . . \} .$ As in Section 3.4, the notation

$$
\xi _ { j } = \textstyle { \frac { 1 } { 2 } } ( x _ { j } + x _ { j + 1 } ) , \qquad j = 0 , \pm 1 , \pm 2 , . . . ,
$$

is used for the knots of the spline.Because $s ( x _ { j } )$ is equal to $f ( x _ { j } )$ ,and because $x _ { j }$ is the mid-point of the interval $[ \xi _ { j - 1 } , \xi _ { j } ] _ { : }$ ,the quadratic function $\{ s _ { j } ( x ) = s ( x ) ; \xi _ { j - 1 } \leqslant x \leqslant \xi _ { j } \}$ is the expression

$$
\begin{array} { l } { { s _ { j } ( x ) = f ( x _ { j } ) + ( x - x _ { j } ) [ s ( \xi _ { j } ) - s ( \xi _ { j - 1 } ) ] / h } } \\ { { \qquad + 2 ( x - x _ { j } ) ^ { 2 } [ s ( \xi _ { j } ) - 2 f ( x _ { j } ) + s ( \xi _ { j - 1 } ) ] / h ^ { 2 } . } } \end{array}
$$

Therefore,in order to define $\{ s ( x ) ; \ - \infty < x < \infty \}$ ，it is convenient to calculate the function values $\{ s ( \xi _ { j } ) ; j = 0 , \pm 1 , \pm 2 , . . . \}$ . The first deriva-

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0004_pages_0211-0280/auto/images/895015c4c4e8e6131f7f395b556056e720fc43f4518cdc8ff272f186818b2abc.jpg)  
Figure 18.3.A quadratic cardinal function whose knots are at the data points.

tive continuity condition $s _ { j } ^ { \prime } ( \pmb { \xi } _ { j } ) = s _ { j + 1 } ^ { \prime } \left( \pmb { \xi } _ { j } \right)$ and equation (18.36) imply that the recurrence relations

$$
\begin{array} { c } { { s ( \xi _ { k - 1 } ) + 6 s ( \xi _ { k } ) + s ( \xi _ { k + 1 } ) = 4 [ f ( x _ { k } ) + f ( x _ { k + 1 } ) ] , } } \\ { { { } } } \\ { { k = 0 , \pm 1 , \pm 2 , . . . , } } \end{array}
$$

are obtained. Therefore the cardinal function $l _ { j } ,$ that satisfies equation (18.16) at the interpolation points,also satisfies the conditions

$$
\begin{array} { c } { { l _ { j } ( \xi _ { k - 1 } ) + 6 l _ { j } ( \xi _ { k } ) + l _ { j } ( \xi _ { k + 1 } ) = 4 [ \delta _ { j k } + \delta _ { j k + 1 } ] , } } \\ { { { } } } \\ { { k = 0 , \pm 1 , \pm 2 , . . . . . } } \end{array}
$$

As in Section 18.2 there is only one bounded solution to this system, which is that the cardinal function takes the values

$$
l _ { j } ( \pmb { \xi } _ { k } ) = \Big \{ \begin{array} { l l } { ( 2 - \sqrt { 2 } ) ( 2 \sqrt { 2 } - 3 ) ^ { j - 1 - k } , \qquad k \leqslant j - 1 } \\ { ( 2 - \sqrt { 2 } ) ( 2 \sqrt { 2 } - 3 ) ^ { k - j } , \qquad k \geqslant j , } \end{array}
$$

at the knots. Hence $l _ { j }$ has the form that is shown in Figure 18.4. The localization properties are even better than those of the cardinal function of Figure 18.2, because the exponential decay factor $| 2 { \sqrt { 2 - 3 } } |$ is less than $| { \sqrt { 3 - 2 } } |$ . Therefore quadratic spline interpolation is a very useful procedure, if the knots are placed between the data points.

When there are a finite number of data points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ ,and when $\pmb { s }$ is an interpolating quadratic spline, then the knot positions

$$
\xi _ { j } = \textstyle { \frac { 1 } { 2 } } ( x _ { j } + x _ { j + 1 } ) , \qquad j = 2 , 3 , \ldots , m - 2 ,
$$

are usually suitable. Because there are no knots in the intervals $[ x _ { 1 } , x _ { 2 } ]$ and $[ x _ { m - 1 } , x _ { m } ] ,$ ， the number of parameters of the spline is equal to the number of data. The Schoenberg-Whitney theorem,which is proved in Section 19.5, shows that the interpolation conditions (18.1) determine the parameters uniquely. Hence the knots (18.40) take up the degrees of freedom in the quadratic spline that correspond to the end conditions that are discussed in Section 18.3.This approximation method is usually successful in practice.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0004_pages_0211-0280/auto/images/23ef7f6df6162b5db8ebee92731f12362d9672a0f042de4c006fafaffa309298.jpg)  
Figure 18.4. A quadratic cardinal function whose knots are midway between the data points.

Interpolation by splines of degree greater than three is rare. One of the main reasons is that increasing the degree of a spline normally makes the localization properties less good, because the tails of the cardinal functions decay at a slower exponential rate.Another reason is that there are many computer programs available for interpolation by cubic splines. However,splines of greater degree can be very useful when high accuracy is required. The work of the next chapter is sufficiently general to provide a suitable method of calculation.

# 18 Exercises

18.1 Let the data points of the interpolation procedures of Section 18.1 have the equally spaced values $\{ x _ { j } = j h ; j = 1 , 2 , \ldots , m \}$ Calculate the values of the cardinal functions of Figure 18.1 at the points that are midway between the interpolation points. Hence, for each of the three interpolation procedures, identify the coefficients $\{ c _ { k j } ; j = 1 , 2 , \dots , m \}$ of the equation

$$
s ( x _ { k } + { \textstyle \frac 1 2 } h ) = \sum _ { j = 1 } ^ { m } c _ { k j } f ( x _ { j } ) ,
$$

where $\pmb { s }$ is the interpolating function,and where $k$ is remote from the ends of the interval $[ 1 , m ]$ . Thus compare the accuracy of the three interpolation methods when $f$ is a quartic polynomial.

18.2 Show that both of the piecewise cubic interpolation procedures of Section 18.1 have the property that, depending on the distribution of the data points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ ,the $\infty$ -norm of the interpolation operator can be arbitrarily large.

18.3 Let the data points $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ be equally spaced, let $f$ be a quartic polynomial, and let $\pmb { s }$ be the cubic spline,whose knots are at the data points, that satisfies the interpolation equations (18.1) and the end conditions $d _ { 2 } = d _ { 3 }$ and $d _ { m - 2 } = d _ { m - 1 }$ ， where $d _ { j }$ is the third derivative discontinuity (18.27). Prove that the equations $\{ s ^ { \prime } ( x _ { j } ) = f ^ { \prime } ( x _ { j } ) ; j = 1 , 2 , . . . , m \}$ are obtained, and that the third derivative discontinuities of $\pmb { s }$ have the constant values

$$
d _ { j } = h f ^ { ( 4 ) } ( x _ { j } ) , \qquad j = 2 , 3 , \ldots , m - 1 ,
$$

where $h$ is the spacing between data points.

18.4 Let $\pmb { s }$ be a cubic spline that satisfies the interpolation conditions (18.1), where the knots of $s$ are at the data points,and where the data points are equally spaced. If the function values $f ( \frac { 1 } { 2 } { \ [ x _ { 1 } + }$ $x _ { 2 } ] ) = f ( x _ { 1 { \frac { 1 } { 2 } } } )$ and $f ( { \frac { 1 } { 2 } } [ x _ { 2 } + x _ { 3 } ] ) = f ( x _ { 2 { \frac { 1 } { 2 } } } )$ are known, then two useful methods for fixing one of the degrees of freedom in $\pmb { s }$ are as follows.In one method $\pmb { s } ^ { \prime } ( \pmb { x } _ { 2 } )$ is made equal to the first derivative at $x _ { 2 }$ of the polynomial in ${ \mathcal { P } } _ { 4 }$ that interpolates the function values $\{ f ( x _ { j } ) ; j = 1 , 1 _ { 2 } ^ { \scriptscriptstyle 1 } , 2 , 2 _ { 2 } ^ { \scriptscriptstyle 1 } , 3 \} .$ ，and in the other method the equation

$$
f ( x _ { 2 _ { 2 } ^ { 1 } } ) - s ( x _ { 2 _ { 2 } ^ { 1 } } ) = f ( x _ { 1 _ { 2 } ^ { 1 } } ) - s ( x _ { 1 _ { 2 } ^ { 1 } } )
$$

is satisfied. Prove that these methods are equivalent.

18.5 For any $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $X f$ be the quadratic spline that has knots at the points $\{ \xi _ { j } = ( j + \textstyle { \frac { 1 } { 2 } } ) h ; j = 0$ ，±1，±2,...},and that interpolates the function values $\{ f ( j h ) ; ~ j = 0 , ~ \pm 1 , ~ \pm 2 , . ~ . . \} .$ where $h$ is a positive constant. Prove that the $\infty$ -norm of $X$ has the value $\| X \| _ { \infty } = { \sqrt { 2 } }$

18.6 For any $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $\pmb { s }$ be a cubic spline that is defined by equation (18.15),where the data points have the values (18.14), and where each function $\{ l _ { j } ( x ) ; ~ - \infty < x < \infty \}$ satisfies the cardinality conditions (18.16). Show that, if $\pmb { s }$ is allowed to have knots not only at the data points $\{ j h ; j = 0 , \pm 1 , \pm 2 , . . . \}$ but also at the mid-points $\{ ( j + \textstyle { \frac { 1 } { 2 } } ) h ; j = 0 , \pm 1 , \pm 2 , . . . \} .$ ,then it is possible for each $l _ { j }$ to be non-zero only on the interval $( x _ { j } - 3 h , x _ { j } + 3 h )$ ， and for $\pmb { S }$ to be equal to $f$ when $f$ is any cubic polynomial.

18.7 Let $\{ s ( x ) ; 0 \leqslant x < \infty \}$ be a non-zero cubic spline function that has knots at the points $\{ x _ { j } = \mu ^ { j } ; j = 0 , 1 , 2 , . . . \}$ ,and that is zero at every knot, where $\pmb { \mu }$ is a constant that is not less than one.Prove that it is possible for the derivatives $\{ | s ^ { \prime } ( x _ { j } ) | ; j = 0 , 1 , 2 , . . . \}$ to be bounded for any value of $\pmb { \mu }$ ,but that it is possible for $\pmb { s }$ to be bounded only if $\mu \leqslant \frac { 1 } { 2 } ( 3 + \sqrt { 5 } )$

18.8 For any bounded function $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $\pmb { S }$ be the spline function (18.15),where each cardinal function has the form that is shown in Figure 18.2,and where the spacing between data points, $h$ ,that is given in equation (18.14),is a parameter.Prove that,as $h$ tends to zero, $\pmb { s }$ converges uniformly to $f .$

18.9 Let $f$ be a cubic polynomial, and let s be the quadratic spline with knots at the points (18.40) that interpolates the function values $\{ f ( x _ { j } ) ; \ j = 1 , 2 , \ldots , m \}$ ，where the spacing between the data points $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ is constant. Sketch the form of the error function $\{ f ( { \pmb x } ) - { \pmb s } ( { \pmb x } )$ ； $x _ { 1 } \leqslant x \leqslant x _ { m } \}$ .Propose an algorithm for quadratic spline interpolation that does not cause an increase in the error function near the ends of the range $[ x _ { 1 } , x _ { m } ]$ when $f$ is a cubic polynomial.

18.10 Given two sets of data points $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ and $\{ y _ { k } ; k =$ $1 , 2 , \ldots , n \}$ that satisfy conditions (18.2） and the inequalities $a = y _ { 1 } < y _ { 2 } < . ~ . ~ . < y _ { n } = b$ ,an algorithm is chosen for cubic spline interpolation on each set of points.Let the cardinal functions of the algorithms be $\{ l _ { j } ( x ) ; a \leqslant x \leqslant b ; j = 1 , 2 , . . . m \}$ and $\{ \lambda _ { k } ( y )$ ； $a \leqslant y \leqslant b ; k = 1 , 2 , \ldots , n \Bigr \}$ . For any function $\{ f ( x , y )$ ； $a \leqslant x \leqslant b$ ； $a \leqslant y \leqslant b \}$ of two variables, the approximation

$$
s ( x , y ) = \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { n } l _ { j } ( x ) \lambda _ { k } ( y ) f ( x _ { j } , y _ { k } ) , \qquad a \leqslant x \leqslant b , \qquad a \leqslant y \leqslant b ,
$$

is called a ‘bicubic spline’ approximation to $f .$ Investigate its properties, giving particular attention to the accuracy of the method when $f$ is differentiable,and to procedures for calculating the value of $\pmb { s } ( \pmb { x } , \pmb { y } )$ for any $x$ and $y$ directly from the data $\{ f ( x _ { j } , y _ { k } ) ; j = 1 , 2 , . . . m ; k = 1 , 2 , . . . , n \}$

#

# B-splines

# 19.1 The parameters of a spline function

Most of the results of this chapter and of Chapter 2O apply to general spline functions, that are not necessarily defined by interpolation conditions. As in Section 3.4,we let $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ be the linear space of splines of degree $k$ ,whose knots are $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ .The range of the variable is still the interval $[ a , b ] ,$ ,and it is assumed that the conditions

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } = b
$$

are satisfied. Sometimes the name of the space is shortened to $\mathcal { S }$ Equation (3.31) states that each function in this space can be expressed in the form

$$
s ( x ) = \sum _ { j = 0 } ^ { k } c _ { j } x ^ { j } + \frac { 1 } { k ! } \sum _ { j = 1 } ^ { n - 1 } d _ { j } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where $\{ c _ { j } ; j = 0 , 1 , \ldots , k \} \quad { \mathrm { a n d } } \quad \{ d _ { j } ; j = 1 , 2 , \ldots , n - 1 \}$ arereal parameters. Therefore the dimension of the space is $( k + n )$ . The main purpose of this chapter is to describe a general method for defining an element of $\mathcal { S }$ that is highly convenient for computer calculations.

First an example is given to show that it can be quite unsuitable to specify a spline by the values of the coefficients $\{ c _ { j } ; j = 0 , 1 , \ldots , k \}$ and $\{ d _ { j } ; j = 1 , 2 , \dots , n - 1 \}$ . We let $\pmb { s }$ be the piecewise cubic polynomial, whose knots are the integers $\{ \xi _ { j } = j ; j = 0 , 1 , \ldots , n \}$ ,that is defined by the equations

$$
\left. \begin{array} { l } { { s ( \xi _ { j } ) = 0 } } \\ { { s ^ { \prime } ( \xi _ { j } ) = ( \sqrt { 3 - 2 } ) ^ { j } } } \end{array} \right\} , \qquad j = 0 , 1 , \ldots , n .
$$

It is a cubic spline because it is a multiple of the tail of the cardinal

function that is given in Figure 18.2.Therefore,there is an expression for $\pmb { s }$ of the form (19.2),which is the function

$$
s ( x ) = x - \sqrt { 3 x ^ { 2 } + ( \sqrt { 3 } - 1 ) x ^ { 3 } + 2 \sqrt { 3 \sum _ { j = 1 } ^ { n - 1 } ( \sqrt { 3 - 2 } ) ^ { j } ( x - j ) _ { + } ^ { 3 } } } ,
$$

If we calculate $s ( 1 0 . 5 )$ , for example, from this equation, then the third term contributes the number $( \sqrt { 3 - 1 } ) ( 1 0 . 5 ) ^ { 3 } \approx 8 4 7$ ，but, because $s ( x )$ decreases exponentially as $x$ is increased by whole integers, the actual value of $s ( 1 0 . 5 )$ is $( \sqrt { 3 } - 2 ) ^ { 1 0 } s ( 0 . 5 ) \approx 3 . 0 2 \times { 1 0 } ^ { - 7 }$ . Hence nine decimal digits are lost in cancellation if expression (19.4) is evaluated. Excellent accuracy can be obtained, however, from the data (19.3). Therefore it is better to work with the function and derivative values $\{ s ( \pmb { \xi } _ { j } ) ; j = 0 \}$ ， $1 , \ldots , n \}$ and $\{ s ^ { \prime } ( \xi _ { j } ) ; j = 0 , 1 , \ldots , n \}$ ， instead of with the coefficients $\{ c _ { j } ; j = 0 , 1 , \ldots , k \}$ and $\{ d _ { j } ; j = 1 , 2 , \dots , n - 1 \}$ ·

There are disadvantages,however, in defining $\pmb { s }$ by function and derivative values when $\dot { \kappa } = 3$ . In particular， the second derivative continuity conditions are artificial, and, if $_ n$ is large,then the number of parameters that specify an element of $\mathcal { S }$ is almost twice the dimension of ${ \mathcal { S } } .$ Therefore, except in a few special cases such as interpolation to $f$ at the knots of $\pmb { S }$ , there are more unknowns than necessary in the calculation of a particular cubic spline from data, which can increase greatly the length of the calculation. Further, for larger values of $k$ , it would be necessary to take account of higher derivatives, for instance $\{ s ^ { \prime \prime } ( \xi _ { j } ) ; j = 0 , 1 , \ldots , n \}$ ， which would make the disadvantages worse.

In order that the number of parameters of $\pmb { s }$ is the same as the dimen-sion of $\mathcal { S } ,$ , we may choose any fixed basis of $\mathcal { S } , \{ \phi _ { j } ; j = 1 , 2 , \dotsc , k + n \} \mathtt { s a } _ { \mathrm { { + } } }$ y， and we express $\pmb { S }$ in the form

$$
s ( x ) = \sum _ { j = 1 } ^ { k + n } \lambda _ { j } \phi _ { j } ( x ) , \qquad a \leqslant x \leqslant b .
$$

The coefficients $\left\{ \lambda _ { j } ; j = 1 , 2 , \ldots , k + n \right\}$ are the parameters that characterize ${ \pmb S } .$ .The example (19.4） shows that the basis functions $\{ \phi _ { j } ( x ) =$ $( x - \xi _ { j } ) _ { + } ^ { k }$ ， $a \leqslant x \leqslant b ; j = 1 , 2 , \ldots , n - 1 \}$ and $\{ \phi _ { j } ( { \pmb x } ) = { \pmb x } ^ { j - n }$ ， $a \leqslant x \leqslant b ; j =$ $n , n + 1 , \ldots , n + k \}$ can give severe difficulties in practice, but many other choices of basis can be made. We find that a basis of $^ { \bullet } B$ -splines’ is particularly suitable, not only because it prevents severe loss of accuracy due to cancellation, but also because it reduces the amount of calculation, and it helps the convergence analysis of Chapter 20.

# 19.2 The form of $\pmb { B }$ -splines

One way of introducing $\pmb { B }$ -splines is to address the question of choosing the basis functions $\{ \phi _ { j } ; j = 1 , 2 , \ldots , k + n \}$ in expression (19.5), so that each function $\{ \phi _ { j } ( \pmb { x } )$ ； $a \leqslant x \leqslant b \}$ is identically zero over a large part of the range $a \leqslant x \leqslant b$ .Therefore we consider the problem of finding an element of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is zero on the intervals $[ \xi _ { 0 } , \xi _ { p } ]$ and $[ \xi _ { q } , \xi _ { n } ]$ ,but that is non-zero on $( \xi _ { p } , \xi _ { q } \cdot )$ , where $0 < p < q < n$ f $\pmb { s }$ is such a function it can be expressed in the form

$$
s ( x ) = \sum _ { j = p } ^ { q } d _ { j } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where the parameters $d _ { j }$ have to satisfy the condition

$$
\sum _ { j = p } ^ { q } d _ { j } ( x - \xi _ { j } ) ^ { k } = 0 , \qquad \xi _ { q } \leqslant x \leqslant b .
$$

It follows that the equations

$$
\sum _ { j = p } ^ { q } d _ { j } \xi _ { j } ^ { i } = 0 , \qquad i = 0 , 1 , \dots , k ,
$$

must hold. These equations have a non-zero solution if $q \geq p + k + 1$ ， because then the number of coefficients $\{ d _ { j } \}$ is greater than the number of equations. The identity (4.11） shows that， if $q = p + k + 1$ ，then the coefficients

$$
d _ { j } = \prod _ { \stackrel { i = p } { i \neq j } } ^ { p + k + 1 } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } , \qquad j = p , p + 1 , \ldots , p + k + 1 ,
$$

are suitable. We note that the sign of expression (19.9) is such that $d _ { p }$ is positive. The spline function

$$
B _ { p } ( x ) = \sum _ { j = p } ^ { p + k + 1 } \prod _ { \stackrel { i = p } { i \neq j } } ^ { p + k + 1 } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } { \Big ] } ( x - \xi _ { j } ) _ { + } ^ { k } , \qquad - \infty < x < \infty ,
$$

is called a $^ { \ell } B \cdot$ spline'. The subscript $p$ on $B _ { p } ( { \boldsymbol { x } } )$ denotes that $B _ { p } ( { \boldsymbol { x } } )$ is non-zero only if $x$ is in the interval $( \xi _ { p } , \xi _ { p + k + 1 } )$

Figure 19.1 shows $\pmb { B }$ -splines of degrees one, two and three when the spacing between knots is constant. We note that the value of each spline is positive,except where it is constrained to be zero.The following theorem proves that this property is obtained by all $\pmb { B }$ -splines,and it gives a useful condition on the number of zeros of some other spline functions.

# Theorem 19.1

Let $\pmb { S }$ be a function in the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ，that is identically zero on the intervals $[ \xi _ { 0 } , \xi _ { p } ] \mathrm { a n d } [ \xi _ { q } , \xi _ { n } ] ,$ and that has $r$ zeros in the open interval $( \xi _ { p } , \xi _ { q } )$ ，where $p$ and $q$ are integers that satisfy the condition $0 < p < q < n$ ,and where $r$ is finite.Then the number of zeros is bounded by the inequality

$$
r \leqslant q - ( p + k + 1 ) .
$$

Proof. When $\pmb { s }$ is composed of straight line segments, then it has at most one zero in each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = p , p + 1 , \ldots , q - 1 \}$ Because $s ( \xi _ { p } )$ and $s ( \xi _ { q } )$ are both zero, it follows that the total number of zeros in the open interval $( \xi _ { p } , \xi _ { q } )$ is at most $( q - p - 2 )$ . Therefore the theorem is true when $k = 1$

In order to treat larger values of $k$ ,we require an upper bound on the number of sign changes of a linear spline, $\pmb { \sigma }$ say,that is in the space $\mathcal { S } ( 1 , \xi _ { p } , \xi _ { p + 1 } , . . . , \xi _ { q } )$ ，and that is zero at $\xi _ { p }$ and $\xi _ { q } .$ ，Because no sign changes can occur in the intervals $[ \xi _ { p } , \xi _ { p + 1 } ]$ and $[ \xi _ { q - 1 } , \xi _ { q } ] ,$ ，and because each of the other intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = p + 1 , p + 2 , \ldots , q - 2 \}$ contributes at most one sign change,the total number of sign changes is also bounded above by $( q - p - 2 )$ . An important difference between this result and the one given in the previous paragraph is that some of the linear sections of $\pmb { \sigma }$ are allowed to be identically zero.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0004_pages_0211-0280/auto/images/58591ea408dbeb92ecc1a8bc6b049440802bb1d669ceabe56961c13fb50bd775.jpg)  
Figure 19.1. $B$ -splines of degrees one, two and three.

To complete the proof of the theorem for $k \geqslant 2$ ，we let $\pmb { \sigma }$ be the function $\{ s ^ { ( k - 1 ) } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { q } \}$ and we do some counting. Since, by definition, the function $s$ has $r$ zeros in $( \xi _ { p } , \xi _ { q } )$ , and since $s ( \xi _ { p } )$ and $s ( \xi _ { q } )$ are both zero, the first derivative $\{ s ^ { \prime } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { q } \}$ changes sign at least $( r + 1 )$ times. If $k \geqslant 3$ ,we consider next the second derivative $\{  { s } ^ { \prime \prime } (  { \boldsymbol { { x } } } ) ;  { \boldsymbol { \xi } } _ { p } \leqslant$ $x \leqslant \xi _ { q } \}$ . Because $s ^ { \prime } ( \xi _ { p } )$ and $s ^ { \prime } ( \xi _ { q } )$ are both zero,the number of sign changes of the second derivative is at least one more than the number of sign changes of the first derivative.Hence $s ^ { \prime \prime }$ changes sign at least $( r + 2 )$ times. If $k \geqslant 4$ , we continue this argument inductively. It follows that, for all $k \geqslant 2$ ,the function $\{ \sigma ( x ) = s ^ { ( k - 1 ) } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { q } \}$ changes sign at least $\left( r + k - 1 \right)$ times. Combining this statement with the result of the previous paragraph gives the inequality

$$
( r + k - 1 ) \leqslant ( q - p - 2 ) .
$$

Therefore the theorem is true.

The theorem implies that $q$ cannot be less than $\left( p + k + 1 \right)$ . Moreover, the proof of the theorem shows that,if $\pmb { s }$ is the $B$ -spline (19.10), then, not only is $r$ equal to zero, but also all the inequalities that lead to condition (19.12）are satisfied as equations.Hence,for $j = 0 , 1 , \ldots , k - 1$ ，the derivative $\{ B _ { p } ^ { ( j ) } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { p + k + 1 } \}$ changes sign exactly $j$ times. Therefore Schoenberg made the highly descriptive remark that $^ { \bullet } B$ -splines are bell-shaped'.

# 19.3 $\pmb { B }$ -splines as basis functions

The fact that the $B$ -spline (19.1O) is non-zero only in the interval $[ \xi _ { p } , \xi _ { p + k + 1 } ]$ can be very useful in practical computer calculations. Therefore we seek a basis of the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is composed of $\pmb { B }$ -splines.We include the functions $\{ B _ { p } ; p = 0 , 1 , \dotsc , n - k - 1 \}$ in the basis,because they are linearly independent and they are all in ${ \mathcal { S } } .$ The dimension of the space that is spanned by these functions, however,is $( n - k )$ ,while the dimension of $\mathcal { S }$ is $( n + k )$ .Therefore another $_ { 2 k }$ basis functions are required.A convenient way of choosing them so that they are also $B$ -splines is to introduce some extra knots outside the interval $[ a , b ]$ .Specifically，, we let $\{ \xi _ { j } ; j = - k , - k + 1 , \ldots , - 1 \}$ and $\{ \xi _ { j } ; j = n + 1$ ， $n + 2 , \ldots , n + k \}$ be any points on the real line that satisfy the conditions

$$
\begin{array} { r l } & { \xi _ { - k } < \xi _ { - k + 1 } < . . . < \xi _ { - 1 } < \xi _ { 0 } = a } \\ & { b = \xi _ { n } < \xi _ { n + 1 } < \xi _ { n + 2 } < . . . < \xi _ { n + k } } \end{array} \biggr \} .
$$

For example, we may set $\{ \xi _ { j } = \xi _ { 0 } + j ( \xi _ { 1 } - \xi _ { 0 } ) ; j = - 1 , - 2 , \ldots , - k \}$ and $\{ \xi _ { j } = \xi _ { n } + ( j - n ) ( \xi _ { n } - \xi _ { n - 1 } ) ; j = n + 1 , n + 2 , \ldots , n + k \} .$ . We now define $B _ { p }$ by equation(19.10) for p = -k,-k +1,...,n -1, but we make use of the function value $B _ { p } ( x )$ only if $x$ is in the interval $[ a , b ]$ .Hence the total number of $B$ -splines is equal to the dimension of $\mathcal { S } .$ The following theorem shows that every element of $\mathcal { S }$ can be expressed in the form

$$
s ( x ) = \sum _ { j = - k } ^ { n - 1 } \lambda _ { j } B _ { j } ( x ) , \qquad a \leqslant x \leqslant b .
$$

# Theorem 19.2

Let the points $\{ \xi _ { j } ; j = - k , - k + 1 , \ldots , n + k \}$ satisfy conditions (19.1）and (19.13)，and let $\scriptstyle B _ { p }$ be defined by equation (19.10) for $p = - k , - k + 1 , \ldots , n - 1 .$ Then the functions $\{ B _ { p } ( x ) , a \leqslant x \leqslant b ; p = - k ,$ $- k + 1 , \ldots , n - 1 \}$ are a basis of the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$

Proof. The definition (19.1O) implies that each of the functions $\{ B _ { p } ( x )$ $, a \leqslant x \leqslant b ; p = - k , - k + 1 , . . . , n - 1 \}$ isin $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ， and we have noted already that the number of functions is equal to the dimension of ${ \mathcal { S } } .$ It is therefore sufficient to show that the functions are linearly independent. We follow the normal method of proof, which is to show that, if the spline

$$
s ( x ) = \sum _ { p = - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x ) \cdot
$$

is zero on $a \leqslant x \leqslant b$ ，then all the coefficients $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots \right.$ ， $n - 1 \}$ are zero.

Let $\xi _ { - k - 1 }$ be any real number that is less than $\xi _ { - k }$ . We consider the spline $\{ s ( x ) ; \xi _ { - k - 1 } \leqslant x \leqslant \xi _ { 1 } \}$ ，where $s ( x )$ has the value (19.15). The definition (19.10) implies $\{ s ( x ) = 0 ; \xi _ { - k - 1 } \leqslant x \leqslant \xi _ { - k } \}$ .Therefore,if $s ( x )$ is also zero for $\xi _ { 0 } \leqslant x \leqslant \xi _ { 1 }$ , it follows from the remark,made immediately after the proof of Theorem 19.1, that $\pmb { s }$ is identically zero on $[ \xi _ { - k - 1 } , \xi _ { 1 } ]$ Hence it is sufficient to show that the condition $\{ s ( \boldsymbol { x } ) = 0$ ； $\xi _ { - k } \leqslant x \leqslant b \}$ implies $\left\{ \lambda _ { p } = 0 ; p = - k , - k + 1 , \ldots , n - 1 \right\}$

Alternatively we may prove the equivalent result that, if any of the numbers $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ are non-zero, then $s$ is not identically zero on $[ \xi _ { - k } , b ]$ .We let $q$ be the smallest integer such that $\lambda _ { q }$ is non-zero. It follows from the definitions (19.10) and (19.15) that the equation

$$
\begin{array} { r } { s ( x ) = \lambda _ { q } B _ { q } ( x ) , \qquad \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } , } \end{array}
$$

is satisfied. Hence $s ( x )$ is non-zero for $\xi _ { q } < x \leqslant \xi _ { q + 1 }$ , which completes the proof of the theorem.□

In order to demonstrate the way in which a $\pmb { B }$ -spline basis can be used, we consider the problem of expressing the cardinal function of Figure 18.2 in the form

$$
l _ { j } ( x ) = \sum _ { p = - \infty } ^ { \infty } \lambda _ { p } B _ { p } ( x ) , \qquad - \infty < x < \infty .
$$

Because the knots are the points $\{ \xi _ { i } = i h ; i = 0 , \pm 1 , \pm 2 , \ldots \} ,$ ,the $\pmb { B }$ -spline $\scriptstyle B _ { p }$ is the function

$$
\begin{array} { c } { { B _ { p } ( x ) = \displaystyle \frac { 1 } { 2 4 h ^ { 4 } } [ ( x - \xi _ { p } ) _ { + } ^ { 3 } - 4 ( x - \xi _ { p + 1 } ) _ { + } ^ { 3 } + 6 ( x - \xi _ { p + 2 } ) _ { + } ^ { 3 } } } \\ { { - 4 ( x - \xi _ { p + 3 } ) _ { + } ^ { 3 } + ( x - \xi _ { p + 4 } ) _ { + } ^ { 3 } ] , ~ - \infty < x < \infty . } } \end{array}
$$

In particular the equations

$$
\left. \begin{array} { l } { B _ { p } ( \xi _ { p + 1 } ) = 1 / \left( 2 4 h \right) } \\ { B _ { p } ( \xi _ { p + 2 } ) = 1 / ( 6 h ) } \\ { B _ { p } ( \xi _ { p + 3 } ) = 1 / \left( 2 4 h \right) } \end{array} \right\}
$$

are satisfied.Because $\scriptstyle B _ { p }$ is zero at all the other knots, it follows from equation (19.17) that $l _ { j } ( \pmb { \xi } _ { i } )$ has the value

$$
l _ { j } ( \xi _ { i } ) = [ \lambda _ { i - 1 } + 4 \lambda _ { i - 2 } + \lambda _ { i - 3 } ] / 2 4 h .
$$

Therefore the cardinality conditions $\{ l _ { j } ( \pmb { \xi } _ { i } ) = \delta _ { i j } ; i = 0 , \pm 1 , \pm 2 , . . . \}$ give the equations

$$
\lambda _ { i - 1 } + 4 \lambda _ { i - 2 } + \lambda _ { i - 3 } = 2 4 h \delta _ { i j } , \qquad i = 0 , \pm 1 , \pm 2 , \ldots .
$$

This recurrence relation has just one bounded solution, namely the values

$$
\lambda _ { p } = 4 \sqrt { 3 ( \sqrt { 3 } - 2 ) ^ { | j - 2 - p | } } h , \qquad p = 0 , \pm 1 , \pm 2 , . . . ,
$$

which are the required coefficients of expression (19.17). Two advantages of using $\pmb { B }$ -splines are that the method of calculating cardinal functions can be extended easily to splines of higher degree,and, for any $x ,$ the number of non-zero terms in the sum (19.17) or (19.14) is finite.

It is interesting also to express the function (19.4) in terms of $\pmb { B }$ -splines. Therefore we introduce extra knots at the points $\{ \xi _ { j } = j ; j = - 3$ ， $- 2 , \ : - 1 , \ : n + 1 , \ : n + 2 , \ : n + 3 \}$ .Because the shape of the spline (19.4) is the same as the tail of the cardinal function (19.17),the required expression has the form

$$
s ( x ) = \alpha \sum _ { p = - 3 } ^ { n - 1 } ( \sqrt { 3 - 2 } ) ^ { p } B _ { p } ( x ) , \qquad 0 \leqslant x \leqslant n ,
$$

where $_ { \pmb { \alpha } }$ is a constant. Equation (19.18) and the property $s ^ { \prime } ( 0 ) = 1$ give the value $\scriptstyle \alpha = { \frac { 4 } { 3 } } ( 7 { \sqrt { 3 - 1 2 } } )$ .If $s ( 1 0 . 5 )$ is calculated numerically from expression (19.23), then a small number is found, because of the factor $( { \sqrt { 3 - 2 } } ) ^ { p }$ and because the first non-zero term of the sum occurs when $p = 7$ . Hence the $B$ -spline basis avoids the very serious cancellation that occurs when equation (19.4) is used to evaluate $s ( 1 0 . 5 )$

# 19.4 A recurrence relation for $\pmb { { \cal B } }$ -splines

In many algorithms for approximation and data fitting it is necessary to calculate the values of $\pmb { B }$ -splines for several values of the variable $x$ . One possible method is to calculate directly the expression

$$
B _ { p } ^ { k } ( x ) = \sum _ { j = p } ^ { p + k + 1 } \bigg [ \prod _ { \stackrel { i = p } { i \ne j } } ^ { p + k + 1 } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } \bigg ] ( x - \xi _ { j } ) _ { + } ^ { k } ,
$$

which is the same as equation (19.1O),except that the superscript $k$ on the left-hand side shows the degree of the $\pmb { B }$ -spline explicitly. If one allows for the fact that the term in square brackets is independent of $x$ ,then this method is quite suitable, unless $x$ is very close to $\xi _ { p + k + 1 }$ . The difficulty in this case is that $B _ { p } ^ { k } ( x )$ should tend to zero as $x$ tends to $\xi _ { p + k + 1 }$ , butformula (19.24) relies on cancellation to give this property. It would be better to make use of the fact that $B _ { p } ^ { k } ( x )$ is a multiple of $( x - \xi _ { p + k + 1 } ) ^ { k }$ when $x$ is in the interval $[ \xi _ { p + k } , \xi _ { p + k + 1 } ]$ 、A procedure that is efficient in all cases is described in this section. It depends on the following recurrence relation.

# Theorem 19.3

Let $k$ be an integer that is greater than one, and let $\{ \xi _ { j } ; j = p ;$ $p + 1 , \ldots , p + k + 1 \}$ be a set of distinct real numbers, which we assume are in ascending order. Then the function (19.24) satisfies the equation

$$
B _ { p } ^ { k } ( x ) = \frac { ( x - \xi _ { p } ) B _ { p } ^ { k - 1 } ( x ) + ( \xi _ { p + k + 1 } - x ) B _ { p + 1 } ^ { k - 1 } ( x ) } { ( \xi _ { p + k + 1 } - \xi _ { p } ) } ,
$$

for all real values of $x$

Proof. Let $s ( x )$ be the right-hand side of expression (19.25).The function $\{ s ( x ) ; - \infty < x < \infty \}$ is composed of polynomial pieces, each of degree at most $k$ ，that are joined at the knots $\left\{ \xi _ { j } ; \ j = p , p + 1 , \ldots , \right.$ $p + k + 1 \}$ . By the definition of a $\pmb { B }$ -spline,this function is identically zero for $x \leqslant \xi _ { p }$ and $x \geqslant \xi _ { p + k + 1 }$ . When $x$ is in the interval $[ \xi _ { p } , \xi _ { p + 1 } ] ,$ ，the definition (19.24) implies the identity

$$
\boldsymbol { B } _ { p } ^ { k } ( \boldsymbol { x } ) = \frac { ( \boldsymbol { x } - \boldsymbol { \xi } _ { p } ) } { ( \boldsymbol { \xi } _ { p + k + 1 } - \boldsymbol { \xi } _ { p } ) } \boldsymbol { B } _ { p } ^ { k - 1 } ( \boldsymbol { x } ) ,
$$

and $B _ { p + 1 } ^ { k - 1 } \left( x \right)$ is zero. Therefore the equation $\{ s ( x ) = B _ { p } ^ { k } ( x ) ; \xi _ { p } \leqslant x \leqslant \xi _ { p + 1 } \}$ is satisfied. In order to prove that the conditions $\{ s ( x ) = B _ { p } ^ { k } ( x )$ ； $\xi _ { j } \leqslant x \leqslant$ $\xi _ { j + 1 } ; j = p _ { , } + 1 , p + 2 , \ldots , p + k \}$ hold also, it is sufficient to show that the change in $\pmb { s }$ at the knots $\{ \xi _ { j } ; j = p + 1 , p + 2 , \ldots , p + k \}$ agrees with the change that is given in equation (19.24). This result is obtained by straightforward algebra from the definitions of $B _ { p } ^ { k - 1 } ( x ) , B _ { p + 1 } ^ { k - 1 } ( x )$ and $\pmb { s } ( \pmb { x } )$ . When $j$ is in $[ p + 1 , p + k ]$ ，we find that the change in $\pmb { s }$ at $\xi _ { j }$ is the polynomial $( x - \xi _ { j } ) ^ { k - 1 } / ( \xi _ { p + k + 1 } - \xi _ { p } )$ multiplied by the factor

$$
\begin{array} { l } { { ( x - \xi _ { p } ) \overset { p \ \not \mapsto k } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } + ( \xi _ { p + k + 1 } - x ) \overset { p + k + 1 } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { i } ) } } } \\ { { \ } } \\ { { = [ ( x - \xi _ { p } ) ( \xi _ { p + k + 1 } - \xi _ { i } ) + ( \xi _ { p + k + 1 } - x ) ( \xi _ { p } - \xi _ { i } ) ] \overset { p + k + 1 } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { j } ) } } } \\ { { \ } } \\ { { \ } } \\ { { = ( x - \xi _ { i } ) ( \xi _ { p + k + 1 } - \xi _ { p } ) \overset { p + k + 1 } { \underset { i \not \in p } { \prod } } \frac { 1 } { ( \xi _ { i } - \xi _ { i } ) } . } } \end{array}
$$

Hence the change in $\pmb { s }$ is the same as the change in ${ B } _ { p } ^ { k }$ ， which completes the proof of the theorem.□

Equation (19.25) is similar to the recurrence formula (5.14) for divided differences. Therefore a convenient method for calculating $B _ { p } ^ { k } ( x )$ for a fixed value of $x$ is to compute the columns of the tableau

in sequence. If $x$ is in the interval $[ \xi _ { i } , \xi _ { i + 1 } ] ,$ ,then the numbers in the first column have the values

$$
\left. \begin{array} { l } { { B _ { j } ^ { 1 } ( x ) = 0 , \qquad j \neq i - 1 , \qquad j \neq i } } \\ { { B _ { i - 1 } ^ { 1 } ( x ) = ( \xi _ { i + 1 } - x ) / [ ( \xi _ { i + 1 } - \xi _ { i - 1 } ) ( \xi _ { i + 1 } - \xi _ { i } ) ] \Bigg \} . } } \\ { { B _ { i } ^ { 1 } ( x ) = ( x - \xi _ { i } ) / [ ( \xi _ { i + 1 } - \xi _ { i } ) ( \xi _ { i + 2 } - \xi _ { i } ) ] } } \end{array} \right.
$$

The remaining entries in the table (19.28) are obtained from equation (19.25),which gives $B _ { p } ^ { k } ( x )$ in the final column. This procedure is highly suitable for numerical computation， because,except for differences between values of the variables, there is no cancellation. Moreover, it is easy to extend the table to provide $B _ { p } ^ { k } ( x )$ for a range of values of $p$

There are other relations between $\pmb { B }$ -splines and divided differences. One of them is so fundamental that it is used sometimes to introduce $B$ -splines. It comes from a property of the function

$$
f ( \xi ) = ( - 1 ) ^ { k + 1 } ( x - \xi ) _ { + } ^ { k } , \qquad - \infty < \xi < \infty ,
$$

where $x$ is any fixed number.We recall from Chapter 5 that the divided difference $f [ \xi _ { p } , \xi _ { p + 1 } , \ldots , \xi _ { p + { \dot { k } } + 1 } ]$ is the coefficient of $\xi ^ { k + 1 }$ in the polynomial of degree at most $k + 1$ that interpolates the function values $\{ f ( \xi _ { j } ) ; j = p , p + 1 , \ldots , p + k + 1 \}$ . Therefore,if we make the definition

$$
B _ { p } ^ { k } ( x ) = f [ \xi _ { p } , \xi _ { p + 1 } , . . . , \xi _ { p + k + 1 } ] ,
$$

it follows that $B _ { p } ^ { k } ( x )$ is zero when $x \leqslant \xi _ { p }$ and when $x ^ { \prime } \geq \xi _ { p + k + 1 }$ . Further, because the divided difference is a linear combination of the function values $\{ f ( \xi _ { j } ) ; j = p , p + 1 , \ldots , p + k + 1 \}$ ，the function $\{ B _ { p } ^ { k } ( x ) ; - \infty < x <$ $\infty \}$ is a spline of degree $k$ whose knots are the points $\{ \xi _ { j } ; j = p , p + 1 \}$ $\cdots , p + k + 1 \}$ . Hence ${ B } _ { p } ^ { k }$ isa $\pmb { B }$ -spline. An alternative and less interesting method of reaching this conclusion is to deduce from equations (5.2),(19.30) and (19.31) that $B _ { p } ^ { k } ( x )$ has the value

$$
B _ { p } ^ { k } ( x ) = \sum _ { j = p } ^ { p + k + 1 } \frac { ( - 1 ) ^ { k + 1 } ( x - \xi _ { j } ) _ { + } ^ { k } } { \underset { i = p } { \prod } ( \xi _ { j } - \xi _ { i } ) } ,
$$

which is equivalent to the definition (19.24).

There are some advantages in taking the point of view that $B _ { p } ^ { k } ( x )$ is the divided difference (19.31). In particular, a neat proof of Theorem 19.3 can be obtained by letting $\pmb { g }$ and $h$ be the functions

$$
\begin{array} { l } { { g ( \xi ) = ( \xi - x ) , \qquad - \infty < \xi < \infty , \nonumber } } \\ { { h ( \xi ) = ( - 1 ) ^ { k } ( x - \xi ) _ { + } ^ { k - 1 } , \qquad - \infty < \xi < \infty } } \end{array} \biggr \} ,
$$

and by calculating expression (19.31) from the product formula

$$
B _ { p } ^ { k } ( x ) = \sum _ { j = p } ^ { p + k + 1 } g [ \xi _ { p } , \xi _ { p + 1 } , \ldots , \xi _ { j } ] h [ \xi _ { j } , \xi _ { j + 1 } , \ldots , \xi _ { p + k + 1 } ] ,
$$

which is given in Exercise 5.9.

# 19.5 The Schoenberg-Whitney theorem

A convenient method for calculating an approximation from the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to the function $\{ f ( x ) ; a \leqslant x \leqslant b \}$ is to inter-

polate some function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , n + k \}$ . We let the interpolation points be in ascending order

$$
a \leqslant x _ { 1 } < x _ { 2 } < . . . < x _ { n + k } \leqslant b ,
$$

but there is no need for any of them to be at knot positions. Because the number of function values is equal to the dimension of ${ \mathcal { S } } ,$ it is important to ask whether there is just one element $\pmb { s }$ in $\mathcal { S }$ that satisfies the equations

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , n + k .
$$

We introduce extra knots outside the interval $[ a , b ] ,$ in order that every element of $\mathcal { S }$ can be expressed as a linear combination of the $\pmb { B }$ -splines $\{ B _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \}$ Useful necessary and sufficient conditions for $\pmb { s }$ to be unique are given in the following theorem.

# Theorem 19.4 (Schoenberg-Whitney)

Let the real numbers $\{ \xi _ { j } ; j = - k , - k + 1 , \ldots , n + k \}$ be in strictly ascending order,and,for $p = - k , - k + 1 , \ldots , n - 1$ ,let $\{ B _ { p } ( x ) ; - \infty < x <$ $\infty \}$ be defined by equation (19.10). Let the interpolation points $\{ x _ { i } ; i =$ $1 , 2 , \ldots , n + k \}$ also be in strictly ascending order.Then,for any function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , n + k \}$ , the equations

$$
\sum _ { p = - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , n + k ,
$$

have a unique solution $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ , if and only if all the numbers $\{ B _ { j - k - 1 } ( x _ { j } ) ; j = 1 , 2 , \ldots , n + k \}$ are non-zero.

Proof. Suppose that $B _ { j - k - 1 } ( x _ { j } )$ is zero.Then either the inequality $x _ { j } \leqslant \xi _ { j - k - 1 }$ or the inequality $x _ { j } \geqslant \xi _ { j }$ is satisfied.In the first case $B _ { p } ( { \boldsymbol { x } } )$ is zero if the conditions $p \geqslant j - k - 1$ and $x \leqslant x _ { j }$ both hold. It follows that the first $j$ of the equations (19.37) have the form

$$
\sum _ { p = - k } ^ { j - k - 2 } \lambda _ { p } B _ { p } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , j .
$$

Because these $j$ equations depend on only $( j - 1 )$ unknowns, they do not have a solutioh for a general right-hand side. Similarly, if $x _ { j } \geqslant \xi _ { j } ,$ then the last $( n + k + 1 - j )$ equations have the form

$$
\sum _ { p = j - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = j , j + 1 , \ldots , n + k ,
$$

so again the number of unknowns is insuffcient. Therefore the conditions

$$
B _ { j - k - 1 } ( x _ { j } ) \neq 0 , \qquad j = 1 , 2 , \ldots , n + k ,
$$

are necessary for the system (19.37) to have a solution for any $f .$

The equations (19.37) do not have a unique solution if and only if there exist parameters $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ ，that are not all zero, such that the function

$$
s ( x ) = \sum _ { p = - k } ^ { n - 1 } \lambda _ { p } B _ { p } ( x ) , \qquad - \infty < x < \infty ,
$$

satisfies the conditions

$$
s ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , n + k .
$$

In this case Theorem 19.2 states that the function (19.41) is not identically zero.Therefore,to prove the second half of the theorem,it is sufficient to show that conditions (19.40), (19.41) and (19.42) do not allow $\pmb { s }$ to be a non-zero spline function.

We suppose that these conditions hold, but that $\pmb { s }$ is non-zero. As $x$ ranges over the real line, there are some intervals,including $x \leqslant \xi _ { - k }$ and $x \geq \xi _ { n + k } ,$ on which $\pmb { s }$ is identically zero,but in other parts of the range the number of zeros of $\pmb { s }$ is finite. Therefore there are knots, $\xi _ { p }$ and $\xi _ { q } ,$ such that $\pmb { s }$ is identically zero on $[ \xi _ { p - 1 } , \xi _ { p } ]$ and $[ \xi _ { q } , \xi _ { q + 1 } ] ,$ ，while, in the open interval $( \xi _ { p } , \xi _ { q } )$ ， $\pmb { s }$ has only a finite number of zeros, $r$ say. It may be necessary to introduce two more artificial knots $\xi _ { - k - 1 }$ and $\xi _ { n + k + 1 }$ satisfying the conditions $\xi _ { - k - 1 } < \xi _ { - k }$ and $\xi _ { n + k + 1 } > \xi _ { n + k }$ .In any case,the proof of Theorem 19.1 shows that inequality (19.11) is obtained.However, the $\pmb { B }$ -splines $\{ B _ { j } ; j = p , p + 1 , \ldots , q - k - 1 \}$ take non-zero values only if the variable $x$ is in the interval $( \xi _ { p } , \xi _ { q } )$ . Therefore condition (19.40) implies that the points $\{ x _ { j + k + 1 } ; j = p , p + 1 , \dots , q - k - 1 \}$ are all in this interval. It follows from equation (19.42) that the number of zeros of $\pmb { s }$ in $( \xi _ { p } , \xi _ { q } )$ is at least $\left( q - p - k \right)$ ，which contradicts inequality (19.11). Therefore the theorem is true.□

The calculation of the spline $s$ in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that satisfies the equations (19.36) shows the usefulness of many of the results of this chapter. The Schoenberg-Whitney theorem makes it easy to check whether the equations have a solution.We may use the ideas of Section 19.3 to express $\pmb { s }$ as a linear combination of $\pmb { B }$ -splines. Therefore we have to calculate the parameters $\left\{ \lambda _ { p } ; p = - k , - k + 1 , \ldots , n - 1 \right\}$ that are defined by the system (19.37). This system is easy to solve,because the properties of $\pmb { B }$ -splines, given in Section 19.2,imply that, for each $i ,$ at most $( k + 1 )$ of the matrix elements $\{ B _ { p } ( x _ { i } ) ; p = - k , - k + 1 , \ldots , n - 1 \}$ are non-zero. The non-zero matrix elements can be obtained conveniently from the recurrence relation that is described in Section 19.4. Hence,after the knots of the spline and the points $\{ x _ { i } ; i = 1 , 2 , \ldots , n + k \}$ are chosen,it is straightforward to calculate spline approximations by interpolation.

# 19 Exercises

19.1 Let $V$ be a polyhedron in $\mathcal { R } ^ { k + 1 }$ that has $( k + 2 )$ vertices, for example a tetrahedron in $\mathcal { R } ^ { 3 }$ . Let d be a fixed non-zero vector in $\mathcal { R } ^ { k + 1 }$ ,and,foranyrealnumber $\theta _ { i }$ let $U ( \pmb \theta )$ be the linear manifold $\{ \mathbf { x } \colon \mathbf { x } ^ { \mathrm { T } } \mathbf { d } = \theta , \mathbf { x } \in \mathcal { R } ^ { k + 1 } \}$ , which is a slice of $\mathcal { R } ^ { k + 1 }$ that is orthogonal to the direction d. Let $s ( \theta )$ be the volume (or area) of the intersection of $U ( \pmb \theta )$ and $V .$ Prove that, if no linear manifold $U ( \theta )$ contains more than one vertex of the polyhedron, then the function $\{ s ( \theta ) ; - \infty < \theta < \infty \}$ is a $\pmb { B }$ -spline of degree $k$ ·

19.2 Let $k = 3$ ， $n = 1 0$ and $\{ \xi _ { j } = j ; j = - 3 , - 2 , \ldots , 1 3 \}$ in the statement of Theorem 19.2.Express the function $\{ f ( x ) = x ^ { 2 }$ ； $0 \leqslant x \leqslant$ $1 0 \}$ as a linear combination of the $\pmb { B }$ -splines $\{ B _ { p }$ ； $p = - 3$ ， $- 2 , \ldots , 9 \}$ .Check the calculation of the coefficients by evaluating your expression at $\begin{array} { r } { x = l + \frac { 1 } { 2 } , } \end{array}$ ,where $\iota$ is any integer in the range [0, 9].

19.3 Express the first derivative of the $\pmb { B }$ -spline (19.10) in terms of two $\pmb { B }$ -splines of degree $( k - 1 )$

19.4 Let ${ B } _ { p } ^ { k }$ be the $\pmb { B }$ -spline of degree $k$ whose knots have the values $\left\{ \xi _ { j } = j ; j = p , p + 1 , \ldots ; p + k + 1 \right\}$ ，Use the recurrence relation (19.25) to determine the value of the $\pmb { B }$ -spline at its knots for $k = 1 , 2 , 3 , \ldots , 7$ . A convenient check on your calculations is that the equation

$$
\sum _ { j = p + 1 } ^ { p + k } B _ { p } ^ { k } ( \xi _ { j } ) = 1 / ( k + 1 )
$$

should be satisfied, which is a consequence of Theorem 20.1.

9.5 Let $\pmb { n }$ be a positive integer, let $\pmb { \alpha }$ be a constant from the interval (0,1),and let the points $\{ \xi _ { j } \}$ and $\{ x _ { i } \}$ have the values $\{ \xi _ { j } = j ; j =$ $0 , 1 , \ldots , n \}$ ， $\left\{ x _ { i } = \alpha + i - 1 ; i = 1 , 2 , \ldots , n \right\}$ and $x _ { n + 1 } = n$ . Show that, for any function $f$ in $\textstyle \mathcal { C } [ 0 , n ] ,$ ,there is a linear spline in the space $\mathcal { S } ( 1 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that interpolates the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , n + 1 \}$ . Sketch the cardinal functions of the interpolation procedure. It should be clear that the $\infty$ -norm of the interpolation operator is large if $\pmb { \alpha }$ is near one, but that it is of moderate size if $\alpha < \frac { 1 } { 2 }$

19.6 Let $\pmb { s }$ be an approximation from the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ a , b ]$ ，where the knots satisfy the conditions (19.1). Prove that $\pmb { s }$ is a best minimax approximation from $\mathcal { S }$ to $f$ if and only if there exist integers $p$ and $q$ in $[ 0 , n ]$ and points $\{ \zeta _ { i } ; i = 0 , 1 , . . . , q - p + k \}$ such that the following conditions are obtained:

$$
\xi _ { p } \leqslant \zeta _ { 0 } < \zeta _ { 1 } < . . . < \zeta _ { q - p + k } \leqslant \xi _ { q } ,
$$

$$
| f ( \zeta _ { i } ) - s ( \zeta _ { i } ) | = \| f - s \| _ { \infty } , \qquad 0 \leqslant i \leqslant q - p + k ,
$$

$$
[ f ( \zeta _ { i } ) - s ( \zeta _ { i } ) ] = - [ f ( \zeta _ { i - 1 } ) - s ( \zeta _ { i - 1 } ) ] , \qquad 1 \leqslant i \leqslant q - p + k .
$$

19.7 Prove Theorem 19.3 by the method that is suggested in the last paragraph of Section 19.4.

19.8 Let ${ B } _ { p } ^ { k }$ be the spline function (19.10),where the superscript shows the degree of the spline,and where we allow $k$ to be any non-negative integer. Let $x$ be any point in the interval $( \xi _ { p } , \xi _ { p + k + 1 } ]$ ，and let the integer $q$ be defined by the condition $\xi _ { q } < x \leqslant \xi _ { q + 1 }$ . Prove that the indefinite integral of ${ B } _ { p } ^ { k }$ has the value

$$
\int _ { \xi _ { p } } ^ { x } B _ { p } ^ { k } ( \theta ) \mathrm { d } \theta = \frac { 1 } { k + 1 } \sum _ { j = 0 } ^ { q - p } \left( x - \xi _ { p + j } \right) B _ { p + j } ^ { k - j } ( x ) .
$$

This formula allows the integral to be calculated without any cancellation from the bottom entries of the columns of the tableau (19.28).

19.9 Let $k$ and $_ n$ be positive integers such that $( k + n )$ is even, and let the knots $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ of the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ satisfy inequality (19.1).Let $f$ be a function in $\mathcal { C } ^ { ( 1 ) } [ a , b ]$ and let $\{ x _ { i } ; i = 1 , 2 , \ldots , { \textstyle { \frac { 1 } { 2 } } } ( k + n ) \}$ be a set of distinct points in $[ a , b ]$ Obtain necessary and suffcient conditions on these points that imply that a unique spline in $\mathcal { S }$ is defined by the equations $\{ s ( x _ { i } ) = f ( x _ { i } ) , s ^ { \prime } ( x _ { i } ) = f ^ { \prime } ( x _ { i } ) ; i = 1 , 2 , \ldots , { \frac { 1 } { 2 } } ( k + n ) \}$

19.10 Let $\mathcal { S }$ be the space of quadratic splines that have the knots $\{ \xi _ { j } = j h ; j = 0 , \pm 1 , \pm 2 , \ldots \} ,$ ，let $f$ be a bounded function in $\mathcal { C } ( - \infty , \infty )$ ,and let the function

$$
s ( x ) = \sum _ { p = - \infty } ^ { \infty } \lambda _ { p } B _ { p } ( x ) , \qquad - \infty < x < \infty ,
$$

be the best least squares approximation from $\mathcal { S }$ to $f .$ Calculate the elements of the matrix of the normal equations.Hence deduce that there exist multipliers $\{ \mu _ { l } ; l = 0 , \pm 1 , \pm 2 , \ldots \}$ such that $\lambda _ { p }$ has the value

$$
\lambda _ { p } = \sum _ { l = - \infty } ^ { \infty } \mu _ { l } \int _ { \xi _ { p + l } } ^ { \xi _ { p + l + 3 } } B _ { p + l } ( x ) f ( x ) \mathrm { d } x , \qquad p = 0 , \pm 1 , \pm 2 , . . . ,
$$

and that the order of magnitude of $\left| \mu _ { l } \right|$ is $( 0 . 4 3 0 6 ) ^ { | l | } h$

# Convergence properties of spline approximations

# 20.1 Uniform convergence

If one requires a spline approximation from $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ , then it is useful sometimes to have bounds on the least maximum error

$$
d ^ { * } ( { \mathcal { S } } , f ) = \operatorname* { m i n } _ { s \in { \mathcal { S } } } \| f - s \| _ { \infty } .
$$

They are studied in this chapter, including the case when $f$ is differentiable. It is assumed that the numbers $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy the conditions

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } = b ,
$$

and we let $\boldsymbol { h }$ be the maximum interval between knots

$$
h = \operatorname* { m a x } _ { i = 1 , 2 , \ldots , n } ( \xi _ { i } - \xi _ { i - 1 } ) .
$$

The main purpose of this section is to derive the inequality

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant \omega ( { \frac { 1 } { 2 } } [ k + 1 ] h ) ,
$$

where $\pmb { \omega }$ is the modulus of continuity of $f .$ It follows that any continuous function can be approximated to arbitrarily high accuracy by a spline function of degree $k _ { : }$ ， provided that the spacing between knots is sufficiently small.

In order to express spline functions as linear combinations of $\pmb { B }$ - splines, we introduce extra knots that satisfy condition (19.13). Instead of using $\smash { B _ { p ; \mathrm { ~ \scriptsize ~ . ~ } } ^ { k } }$ ,however, it is more convenient to work with the function

$$
N _ { p } ^ { k } ( x ) \cdot = ( \xi _ { p + k + 1 } - \xi _ { p } ) \sum _ { { j = p \atop \prod _ { i = p } ^ { p + k + 1 } } \atop { i \ne j } } ^ { p + k + 1 } { \frac { ( x - \xi _ { j } ) _ { + } ^ { k } } { p + k + 1 } } , \qquad a \leqslant x \leqslant b ,
$$

which is just $B _ { p } ^ { k } ( x )$ multiplied by the factor $( \xi _ { p + k + 1 } - \xi _ { p } )$ . Therefore the splines $\{ N _ { p } ^ { k } ; p = - k , \ - k + 1 , \ldots , n - 1 \}$ are a basis of ${ \mathcal { S } } ,$ and $N _ { p } ^ { k } ( x )$ is non-zero only if $x$ is in the interval $( \xi _ { p } , \xi _ { p + k + 1 } )$ . It is important to notice also that Theorem 19.1 and equation (20.5) imply the condition

$$
N _ { p } ^ { k } ( x ) \geqslant 0 , \qquad a \leqslant x \leqslant b .
$$

Because the function $\{ s ( x ) = 1 ; a \leqslant x \leqslant b \}$ is in $\mathcal { S } ,$ it can be expressed in terms of the basis functions.The factor $( \xi _ { p + k + 1 } - \xi _ { k } )$ is present in equation (20.5) in order that this expression has the following simple form.

# Theorem 20.1

For all positive integers $k$ ， the functions $\{ N _ { p } ^ { k } ; p = - k , - k + 1 \}$ $\cdots , n - 1 \}$ satisfy the identity

$$
\sum _ { p = - k } ^ { n - 1 } N _ { p } ^ { k } \left( x \right) = 1 , \qquad a \leqslant x \leqslant b .
$$

Proof. Theorem 19.3 allows a proof by induction. By changing the notation from $\boldsymbol { B } _ { p } ^ { k }$ to $\boldsymbol { N } _ { p } ^ { k }$ in expression (19.25), we find that the equation

$$
N _ { p } ^ { k } \left( x \right) = \frac { \left( x - \xi _ { p } \right) } { \left( \xi _ { p + k } - \xi _ { p } \right) } N _ { p } ^ { k - 1 } \left( x \right) + \frac { \left( \xi _ { p + k + 1 } - x \right) } { \left( \xi _ { p + k + 1 } - \xi _ { p + 1 } \right) } N _ { p + 1 } ^ { k - 1 } \left( x \right)
$$

holds for $p = - k , - k + 1 , \ldots , n - 1$ .The two sides of this equation are summed over $\pmb { p }$ , and we make use of the identities $\{ N _ { - k } ^ { k - 1 } ( x ) = 0$ ； $a \leqslant x \leqslant$ $^  b \}$ and $\{ N _ { n } ^ { k - 1 } \left( x \right) = 0$ $a \leqslant x \leqslant b \}$ . Hence, for $k \geqslant 2$ , we find the relation

$$
\begin{array} { c } { { \displaystyle \sum _ { p = - k } ^ { n - 1 } N _ { p } ^ { k } \left( x \right) = \sum _ { p = - k } ^ { n - 1 } \frac { \left( x - \xi _ { p } \right) } { \left( \xi _ { p + k } - \xi _ { p } \right) } N _ { p } ^ { k - 1 } \left( x \right) } } \\ { { + \displaystyle \sum _ { p = - k + 1 } ^ { n } \frac { \left( \xi _ { p + k } - x \right) } { \left( \xi _ { p + k } - \xi _ { p } \right) } N _ { p } ^ { k - 1 } \left( x \right) } } \end{array}
$$

$$
\quad = \sum _ { p = - k + 1 } ^ { n - 1 } N _ { p } ^ { k - 1 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Therefore,if equation (20.7) holds for $k = 1$ ,then it is satisfied for all positive integers $k$ In the case $k = 1$ the function $\smash { N _ { p } ^ { k } ( x ) }$ is equal to ${ \cal B } _ { p } ^ { 1 } ( x )$ multiplied by $( \xi _ { p + 2 } - \xi _ { p } )$ . It follows from expression (19.29) that equation (20.7) is valid for $k = 1$ , which completes the proof.□

The following theorem shows that the properties of $\pmb { B }$ -splines and equation (20.7) provide an elementary proof of the useful bound (20.4).

# Theorem 20.2

For every function $f$ in $\mathcal { C } [ a , b ] .$ ,the least maximum error (20.1) satisfies condition (20.4).

Proof.It is suffcient to find an element $\pmb { s }$ in $\mathcal { S }$ such that the inequality

$$
\| f - s \| _ { \infty } \leqslant \omega ( { \frac { 1 } { 2 } } [ k + 1 ] h )
$$

is obtained. We let $\pmb { s }$ be the spline function

$$
s ( x ) = \sum _ { p = - k } ^ { n - 1 } f ( x _ { p } ) N _ { p } ^ { k } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $\scriptstyle { \mathfrak { x } } _ { p }$ is the number in the range $[ a , b ]$ that is closest to $\frac { 1 } { 2 } \big ( \xi _ { p } + \xi _ { p + k + 1 } \big )$ · Therefore $\scriptstyle { \pmb { x _ { p } } }$ is one of the three numbers $a , b$ and $\frac { 1 } { 2 } ( \xi _ { p } + \xi _ { p + k + 1 } )$ . Equations (20.7) and (20.11) imply the relation

$$
f ( x ) - s ( x ) = \sum _ { p = - k } ^ { n - 1 } { \bigl [ } f ( x ) - f ( x _ { p } ) { \bigr ] } N _ { p } ^ { k } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Because the term under the summation sign is non-zero only if $x$ is in the interval $( \xi _ { p } , \xi _ { p + k + 1 } )$ , the definitions of $x _ { p }$ and $h$ give the bound

$$
\begin{array} { r l } & { \big | f ( x ) - f ( x _ { p } ) \big | \big | N _ { p } ^ { k } ( x ) \big | \leqslant \omega \big ( \frac { 1 } { 2 } [ \xi _ { p + k + 1 } - \xi _ { p } ] \big ) \big | N _ { p } ^ { k } ( x ) \big | } \\ & { \qquad \leqslant \omega \big ( \frac { 1 } { 2 } [ k + 1 ] h \big ) \big | N _ { p } ^ { k } ( x ) \big | , \qquad a \leqslant x \leqslant b . } \end{array}
$$

It follows from expressions (20.12),(20.6) and (20.7) that the inequality

$$
\begin{array} { r l r } {  {  f ( x ) - s ( x )  \leqslant \omega ( \frac { 1 } { 2 } [ k + 1 ] h ) \sum _ { p = - k } ^ { n - 1 }  N _ { p } ^ { k } ( x )  } } \\ & { } & { = \omega ( \frac { 1 } { 2 } [ k + 1 ] h ) , \qquad a \leqslant x \leqslant b , } \end{array}
$$

is satisfied, which is the required result.[

This proof demonstrates that $B$ -splines are useful, not only for simplifying the numerical calculation of spline approximations, but also for theoretical analysis. Their properties imply that the function value $s ( x )$ ， defined by equation (20.11), is independent of $x _ { p } ,$ unless $\left| x - x _ { p } \right|$ is less than ${ \frac { 1 } { 2 } } [ k + 1 ] h$ .Therefore we have a spline approximation whose local properties are similar to those that are given by the interpolation procedures of Section 18.1. The spline function (20.11), however, does not satisfy any obvious interpolation conditions.

# 20.2 The order of convergence when $f$ is differentiable

It is proved in this section that, if $f$ is a differentiable function, then there are upper bounds on the least maximum error (20.1) of the form

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c h ^ { q } \ \| f ^ { ( j ) } \| _ { \infty } ,
$$

for certain positive integers $\pmb q$ and $j ,$ where $c$ is a number that is independent of $f$ and of the positions of the knots $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ ,and

where $h$ is still the maximum distance between adjacent knots. For example, if $f$ is in $\mathcal { C } ^ { ( 1 ) } [ a , b ] .$ , then expression (20.4) and the definition of the modulus of continuity give the bound

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant { \frac { 1 } { 2 } } ( k + 1 ) h \ \| f ^ { \prime } \| _ { \infty } .
$$

An advantage of this kind of bound is that it indicates the improvement in accuracy that can be obtained by increasing the number of knots. It is therefore advantageous if $q$ is as large as possible in expression (20.15). The following argument shows, however, that, even if $f$ can be differentiated more than $j$ times, then $\pmb q$ is equal to $j .$

Let $f$ be a function in $\mathcal { C } ^ { ( j ) } [ a , b ]$ such that $d ^ { * } ( \mathcal { S } , f )$ is positive. We make the change of variable $\{ \bar { x } = \alpha x$ ； $a \leqslant x \leqslant b $ ，where $\pmb { \alpha }$ is any positive constant. Let $\bar { f }$ be the function $\{ \bar { f } ( \bar { x } ) = f ( \bar { x } / \alpha )$ ； $\alpha a \leqslant \bar { x } \leqslant \alpha b \}$ ,let $\bar { \mathcal { S } }$ be the space $\mathcal { S } ( k , \alpha \xi _ { 0 } , \alpha \xi _ { 1 } , . . . , \alpha \xi _ { n } )$ , and let ${ \bar { s } } ^ { * }$ be a best approximation to $\bar { f }$ from ${ \mathcal { \bar { S } } } .$ We note that the function $\{ s ^ { * } ( x ) = \bar { s } ^ { * } ( \alpha x )$ ； $a \leqslant x \leqslant b \}$ is in $\mathcal { S } _ { \ast }$ Therefore the inequality

$$
\begin{array} { r } { d ^ { * } ( \mathcal { S } , f ) \leqslant \left\| f - s ^ { * } \right\| _ { \infty } } \\ { = \left\| \bar { f } - \bar { s } ^ { * } \right\| _ { \infty } } \\ { = d ^ { * } ( \bar { \mathcal { S } } , \bar { f } ) } \end{array}
$$

is satisfied, where the $\infty$ -norm is applied to two different spaces. We may apply condition (20.15) to $d ^ { * } ( { \bar { \mathcal { S } } } , { \bar { f } } )$ ,when $c$ is independent of $f$ and of the numbers $\left\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \right\}$ .Because the maximum distance between adjacent knots in the space $\mathcal { \bar { S } }$ is $\alpha h$ ,it follows from inequality (20.17) that the bound

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c \left( \alpha h \right) ^ { q } \left\| \bar { f } ^ { ( j ) } \right\| _ { \infty }
$$

is obtained. Therefore, because the definition of $\bar { f }$ implies that $\| \bar { f } ^ { ( j ) } \| _ { \infty }$ is equal to $\pmb { \alpha } ^ { - j } \| f ^ { ( j ) } \| _ { \infty }$ ,the relation

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c h ^ { q } \alpha ^ { q - j } \| f ^ { ( j ) } \| _ { \infty }
$$

holds for all positive values of $\pmb { \alpha }$ . However, the left-hand side of this expression is a positive number that is independent of $\pmb { \alpha }$ ,and,if $q$ is not equal to $j ,$ the right-hand side can be made arbitrarily small by choosing an extreme value of $_ \alpha$ .Hence,even if the restriction is relaxed that $q$ is to be an integer, $q$ cannot be different from $j$ in inequality (20.15).

Therefore, we would like $j$ to be as large as possible. Of course $j$ may not exceed the number of times $f$ can be differentiated, and also it cannot be larger than $( k + 1 )$ ,because inequality (20.15) has to hold in the special case when $f$ is the polynomial $\{ f ( x ) = x ^ { k + 1 }$ ； $a \leqslant x \leqslant b \}$ . Therefore the values of $j$ that are given in the following theorem are optimal. Another nice feature of the theorem is that the proof is elementary,although the spacing between knots is allowed to be irregular.

# Theorem 20.3

Let $k$ and $l$ be positive integers. For every function $f$ in $\mathcal { C } ^ { ( l ) } [ a , b ] ,$ and for every integer $j$ in the range [1, $\operatorname* { m i n } ( l , k + 1 ) ]$ ，the least maximum error (20.1) satisfies the condition

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant \frac { ( k + 1 ) ! } { ( k + 1 - j ) ! } ( \frac { 1 } { 2 } h ) ^ { j } \| f ^ { ( j ) } \| _ { \infty } .
$$

Proof. The proof is by induction,and it is similar to the proof of Theorem 3.2. For the general step of the induction we let the values of both $j$ and $k$ be greater than or equal to two,and we assume that condition (20.20) is satisfied if $j$ and $k$ are replaced by $( j - 1 )$ and $( k - 1 )$ This assumption implies the inequality

$$
\| f ^ { \prime } - \sigma \| _ { \infty } \leqslant \frac { k ! } { ( k + 1 - j ) ! } ( \frac { 1 } { 2 } h ) ^ { j - 1 } \| f ^ { ( j ) } \| _ { \infty } ,
$$

where $\pmb { \sigma }$ is a best approximation to $f ^ { \prime }$ from the space ${ \mathcal { S } } ( k - 1 ,$ $\xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . We let $\pmb { s }$ be an indefinite integral of $\pmb { \sigma } .$ ,and we let $s ^ { * }$ be a best approximation to $( f - s )$ from the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . Therefore inequalities (20.16) and (20.21) give the bound

$$
\begin{array} { r l } { \underset { a \leqslant x \leqslant b } { \operatorname* { m a x } } \left| f ( x ) - s ( x ) - s ^ { * } ( x ) \right| \leqslant \frac { 1 } { 2 } ( k + 1 ) h \left\| f ^ { \prime } - \sigma \right\| _ { \infty } } & { } \\ { \leqslant \frac { ( k + 1 ) ! } { ( k + 1 - j ) ! } ( \frac { 1 } { 2 } h ) ^ { j } \left\| f ^ { ( j ) } \right\| _ { \infty } . } \end{array}
$$

Because $( \pmb { \mathscr { s } } + \pmb { \mathscr { s } } ^ { * } )$ is in ${ \mathcal { S } } ,$ it follows that inequality (20.20) is satisfied. It remains to establish suitable conditions to begin the inductive argument.

When $j = 1$ ,we find that condition (20.2O) is the same as inequality (20.16),which is valid for $k \geqslant 1$ . It follows that the theorem is true if $k \geq j \geq 1$ . However, in order that the inductive argument can be applied also to the important special case when $j = k + 1$ ,we have to show that inequality (20.20) is valid when $k = 1$ and $j = 2$ . In this case we let $\pmb { s }$ be the function in $\mathcal { S } ( 1 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is defined by the interpolation conditions $\{ s ( \xi _ { i } ) = f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n \}$ .Because each piece of $\mathcal { S }$ is a linear function, it follows from Theorem 4.2 that, if $x$ is in the interval $[ \xi _ { i } , \xi _ { i + 1 } ] ,$ ，where $i$ is any integer from $[ 0 , n - 1 ] ,$ ，then the equation

$$
f ( x ) - s ( x ) = { \textstyle { \frac { 1 } { 2 } } } ( x - \xi _ { i } ) ( x - \xi _ { i + 1 } ) f ^ { \prime \prime } ( \xi )
$$

holds, where $\xi$ is a point in $[ \xi _ { i } , \xi _ { i + 1 } ]$ that depends on $x$ .Hence we deduce the inequality

$$
\begin{array} { r } { d ^ { * } ( \mathcal { S } , f ) \leqslant \| f - s \| _ { \infty } \leqslant \frac { 1 } { 8 } h ^ { 2 } \| f ^ { \prime \prime } \| _ { \infty } . } \end{array}
$$

Because this condition is stronger than expression (20.20), the proof of the theorem is complete.□

This theorem is useful because it indicates the order of magnitude of the error of a spline approximation when $h$ is small. We recall, however, from Chapter 3, that bounds of the form (20.2O) fail to show that it can be highly advantageous to adapt the distribution of knots to the form of $f .$

# 20.3 Local spline interpolation

If one is selecting a method to calculate an approximation from $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ a , b ] .$ ,one should ask if there are any sudden changes in the form of $f ,$ for example a derivative discontinuity. For many approximation algorithms, the effect of a discontinuity is to introduce a wave in the spline that decays in magnitude away from the discontinuity. However, if the spacing between knots is increased away from the discontinuity, then the rate of decay is usually diminished. In this kind of situation it can be helpful to select an approximation method that has the property that, if $\pmb { x }$ is any point of $[ a , b ]$ that is separated from the discontinuity by a certain number of knots, then the value of the spline at $x$ is independent of the discontinuity. The following interpolation method is suitable.

We choose $( k + 1 )$ different points in each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] \}$ $j = 0 , ( k + 1 ) , 2 ( k + 1 ) , \ldots , r ( k + 1 ) \} _ { \mathrm { { z } } }$ where $r$ is the greatest integer that satisfies the bound

$$
r ( k + 1 ) \leqslant n - 1 ,
$$

and,if the bound holds as a strict inequality,we also choose $[ n - 1 -$ $r ( k + 1 ) ]$ different points in $[ \xi _ { n - 1 } , \xi _ { n } ] ,$ ，where the last of the points is greater than $\xi _ { n - 1 }$ . Thus the total number of points is equal to $( n + k )$ ， which is the dimension of $\mathcal { S } .$ Therefore,because the conditions of Theorem 19.4 are satisfied, we may define $\pmb { s }$ to be the element of $\mathcal { S }$ that interpolates $f$ at the points. The main property of this procedure is that, on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , ( k + 1 ) , 2 ( k + 1 ) , \ldots , r ( k + 1 ) \} ,$ the number of interpolation points is such that the polynomial segment $\{ s ( x ) ; \xi _ { j } \leqslant x \leqslant \xi _ { j + 1 } \}$ is defined completely by the values of $f$ in the interval. Therefore there are no degrees of freedom that allow the form of $\pmb { s }$ in $[ a , \xi _ { j } )$ to be related to the form of $\pmb { s }$ in $( \xi _ { j + 1 } , b ]$ .Hence,if a perturbation to $\pmb { s }$ is generated by a discontinuity in $f ,$ then the effect of the perturbation cannot pass through any of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , ( k + 1 ) \}$ ， $2 ( k + 1 ) , \ldots , r ( k + 1 ) \}$ Thus,if $x$ is any point in $[ a , b ] ,$ ，then the value $\pmb { s } ( \pmb { x } )$ depends only on the form of $f$ in the interval $[ \operatorname* { m a x } \left( \xi _ { q - k } , a \right) ,$ ， min $( \pmb { \xi } _ { q + k + 1 } , \pmb { b } ) ]$ , where the integer $q$ is such that $x$ is in the range $[ \xi _ { q } , \xi _ { q + 1 } ]$

One reason for mentioning this interpolation procedure is that it can be used to derive bounds of the form (20.15), in a way that is more direct than the inductive proof of Theorem 20.3. The bounds are given in the following theorem.

# Theorem 20.4

Given the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ，let $( n + k )$ interpolation points be chosen in the way that has just been described,and let $L$ be the operator from $\mathcal { C } [ a , b ]$ to $\mathcal { S }$ such that, for any $f$ in $\ell [ a , b ] ,$ ,the function $L f$ is the spline that is defined by the interpolation conditions. If $f$ is in the space $\mathcal { C } ^ { ( j ) } [ a , b ] ,$ ，where $j$ is any integer in the range $[ 1 , k + 1 ]$ ，then the inequality

$$
d ^ { * } ( { \mathcal { S } } , f ) { \leqslant } \frac { 1 } { j ! } { \| L \| } _ { \infty } ( k + 1 ) ^ { j } h ^ { j } \| f ^ { ( j ) } \| _ { \infty }
$$

is satisfied.

Proof. It is sufficient to prove that $\| f - s \| _ { \infty }$ is bounded above by the right-hand side of expression (20.26), where $\pmb { s }$ is the spline $L f .$ We let $\pmb { \zeta }$ be any fixed point in $[ a , b ] ,$ , and we let $\phi$ be the polynomial

$$
\phi \left( x \right) = f ( \zeta ) + \frac { \left( x - \zeta \right) } { 1 ! } f ^ { \prime } ( \zeta ) + \ldots + \frac { \left( x - \zeta \right) ^ { j - 1 } } { ( j - 1 ) ! } f ^ { ( j - 1 ) } ( \zeta ) ,
$$

Because $\phi$ is in ${ \mathcal { S } } ,$ the spline $L \phi$ is the polynomial $\phi$ .Further, $\phi ( \zeta )$ is equal to $f ( \zeta )$ .Hence the error at $\pmb { \zeta }$ of the approximation $s = L f$ to $f$ has the value

$$
\begin{array} { r } { f ( \zeta ) - s ( \zeta ) = \phi ( \zeta ) - ( L f ) ( \zeta ) } \\ { = ( L \{ \phi - f \} ) ( \zeta ) . } \end{array}
$$

It is important to notice that the function $( \phi - f )$ takes very small values when the variable is near $\zeta ,$ and to recall that $( L \{ \phi - f \} ) ( \zeta )$ depends only on the form of $( \phi - f )$ in the interval

$$
[ a _ { \xi } , b _ { \zeta } ] = [ \operatorname* { m a x } \ ( \xi _ { q - k } , a ) , \operatorname* { m i n } \ ( \xi _ { q + k + 1 } , b ) ] ,
$$

where the integer $q$ is such that $\pmb { \zeta }$ is in the range $[ \xi _ { q } , \xi _ { q + 1 } ]$ . In order to

make use of these remarks, we note that the mean value theorem gives the bound

$$
{ \big | } f ( x ) - \phi ( x ) { \big | } \leqslant { \frac { 1 } { j ! } } { \big | } x - \zeta { \big | } ^ { j } \| f ^ { ( j ) } \| _ { \infty } , \qquad a \leqslant x \leqslant b .
$$

Therefore, if $\psi _ { \zeta }$ is the function in ${ \mathcal { C } } [ a , b ]$ that satisfes the equation

$$
\psi _ { \zeta } ( x ) = \phi ( x ) - f ( x ) , \qquad a _ { \zeta } \leqslant x \leqslant b _ { \zeta } ,
$$

and that is constant on each of the intervals $[ a , a _ { \zeta } ]$ and $[ b _ { \zeta } , b ] ,$ then the inequality

$$
\begin{array} { l } { \displaystyle \| \psi _ { \zeta } \| _ { \infty } \leqslant \frac { 1 } { j ! } \operatorname* { m a x } \left[ \left| \zeta - a _ { \zeta } \right| ^ { j } , \left| b _ { \zeta } - \zeta \right| ^ { j } \right] \| f ^ { ( j ) } \| _ { \infty } } \\ { \displaystyle \leqslant \frac { 1 } { j ! } \operatorname* { m a x } \left[ \left| \xi _ { q + 1 } - a _ { \zeta } \right| ^ { j } , \left| b _ { \zeta } - \xi _ { q } \right| ^ { j } \right] \| f ^ { ( j ) } \| _ { \infty } } \\ { \displaystyle \leqslant \frac { 1 } { j ! } \left( k + 1 \right) ^ { j } h ^ { i } \left\| f ^ { ( j ) } \right\| _ { \infty } } \end{array}
$$

holds,where the last line depends on the definitions (2O.3) and (20.29). Because expressions (20.31) and (20.32) imply the bound

$$
\begin{array} { r l r } {  { \big | ( L \{ \phi - f \} ) ( \zeta ) \big | = \big | ( L \psi _ { \zeta } ) ( \zeta ) \big | } } \\ & { } & { \leqslant \| L \| _ { \infty } \| \psi _ { \zeta } \| _ { \infty } } \\ & { } & { \leqslant \displaystyle \frac { 1 } { j ! } \| L \| _ { \infty } ( k + 1 ) ^ { j } h ^ { j } \| f ^ { ( j ) } \| _ { \infty } , } \end{array}
$$

and because the right-hand side of this inequality is independent of $\zeta ,$ it follows from equation (20.28) that the theorem is true.□

This theorem is less useful than Theorem 20.3,because the interpolation procedure is such that there is no upper bound on $\| L \| _ { \infty }$ that is independent of the knot positions $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ .Really the main value of the theorem is to show that it is possible to deduce bounds of the form (20.26) from equation (20.28),by letting $\phi$ be the function (20.27), provided that the operator $L$ has the property that, for any $\pmb { \zeta }$ in $[ a , b ]$ ,the function value $( L f ) ( \zeta )$ is independent of $f ( x )$ if $\left| x - \zeta \right|$ exceeds a constant multiple of $h$ .This technique is used again in the next section.

# 20.4 Cubic splines with constant knot spacing

There are several methods for calculating spline approximations with good localization properties that do not make use of interpolation conditions. A procedure is developed in this section for the special case when $k = 3$ and the knots satisfy condition (20.2) and the equation

$$
\xi _ { j } = \xi _ { 0 } + j h , \qquad j = - 3 , - 2 , \ldots , n + 3 .
$$

It shows another technique for spline approximation that obtains high order accuracy when $f$ is sufficiently differentiable.We assume that the function to be approximated is defined on the interval $[ a - 2 h , b + 2 h ] ,$ Because the $\pmb { B }$ -spline $\{ N _ { p } ^ { 3 } ( x ) ; - \infty < x < \infty \}$ is symmetric about the point $x = \xi _ { p + 2 }$ ,we let $\pmb { s _ { 0 } }$ ${ \bf \Gamma } _ { 0 } \left( = L _ { 0 } f , \right.$ ，say) be the spline function

$$
s _ { 0 } ( x ) = \sum _ { p = - 3 } ^ { n - 1 } f ( \xi _ { p + 2 } ) N _ { p } ^ { 3 } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

which is similar to the one that is used to prove Theorem 20.2.In order to apply the idea that is used to prove Theorem 20.4, we seek the greatest value of $j$ such that the equation

$$
\phi = L _ { 0 } \phi , \qquad \phi \in { \mathcal { P } } _ { j - 1 } ,
$$

is satisfied.

Because expression (19.18) implies the equations $N _ { p } ^ { 3 } ( \xi _ { p + 1 } ) =$ $\begin{array} { r } { N _ { p } ^ { 3 } \left( \xi _ { p + 3 } \right) = \frac { 1 } { 6 } } \end{array}$ and $\begin{array} { r } { N _ { p } ^ { 3 } \left( \xi _ { p + 2 } \right) = \frac { 2 } { 3 } , } \end{array}$ ,the spline (20.35) takes the values

$$
\begin{array} { r } { s _ { 0 } ( \xi _ { i } ) = \frac { 1 } { 6 } f ( \xi _ { i - 1 } ) + \frac { 2 } { 3 } f ( \xi _ { i } ) + \frac { 1 } { 6 } f ( \xi _ { i + 1 } ) , \qquad i = 0 , 1 , \dots , n , } \end{array}
$$

at the knots.Hence, if $f$ is in the space $\mathcal { P } _ { 1 }$ ,then ${ \pmb s } _ { 0 } ( { \pmb \xi } _ { i } )$ is equal to $f ( \xi _ { i } )$ ,but, if $f$ is a quadratic function, then the error

$$
\begin{array} { r } { f ( \xi _ { i } ) - s _ { 0 } ( \xi _ { i } ) = - \frac { 1 } { 6 } h ^ { 2 } f ^ { \prime \prime } ( \xi _ { i } ) , \qquad i = 0 , 1 , \dots , n , } \end{array}
$$

occurs. Similarly, the spline approximation

$$
s _ { 1 } ( x ) = \frac { 1 } { 2 } \sum _ { p = - 3 } ^ { n - 1 } \left[ f ( \xi _ { p + 1 } ) + f ( \xi _ { p + 3 } ) \right] N _ { p } ^ { 3 } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

has the value

$$
\begin{array} { r } { s _ { 1 } ( \xi _ { i } ) = \frac { 1 } { 1 2 } [ f ( \xi _ { i - 2 } ) + 4 f ( \xi _ { i - 1 } ) + 2 f ( \xi _ { i } ) + 4 f ( \xi _ { i + 1 } ) + f ( \xi _ { i + 2 } ) ] , } \end{array}
$$

which implies the error

$$
\begin{array} { r } { f ( \xi _ { i } ) - s _ { 1 } ( \xi _ { i } ) = - \frac { 2 } { 3 } h ^ { 2 } f ^ { \prime \prime } ( \xi _ { i } ) , \qquad i = 0 , 1 , \dots , n , } \end{array}
$$

when $f$ is in $\mathcal { P } _ { 2 }$ . The spline approximation that is studied in this section is obtained by forming the linear combination of $\pmb { s _ { 0 } }$ and $\pmb { S } _ { 1 }$ that eliminates the error terms (20.38) and (20.41).Hence it is the function

$$
\begin{array} { r } { s \left( x \right) = \displaystyle \sum _ { p = - 3 } ^ { n - 1 } \left[ - \frac { 1 } { 6 } f ( \xi _ { p + 1 } ) + \frac { 4 } { 3 } f ( \xi _ { p + 2 } ) - \frac { 1 } { 6 } f ( \xi _ { p + 3 } ) \right] N _ { p } ^ { 3 } \left( x \right) , } \\ { a \leqslant x \leqslant b . } \end{array}
$$

Because equations (20.38) and (20.41) are valid when $f$ is any cubic polynomial, the conditions

$$
f ( \xi _ { i } ) = s ( \xi _ { i } ) , \qquad i = 0 , 1 , \ldots , n , \qquad f \in \mathcal { P } _ { 3 } ,
$$

are obtained. Further,equations (19.18)and (20.42） imply that, for $i = 0 , 1 , \ldots , n$ ,the derivative $s ^ { \prime } ( \xi _ { i } )$ has the value

$$
s ^ { \prime } ( \xi _ { i } ) = \frac { 1 } { 1 2 h } \big [ f ( \xi _ { i - 2 } ) - 8 f ( \xi _ { i - 1 } ) + 8 f ( \xi _ { i + 1 } ) - f ( \xi _ { i + 2 } ) \big ] ,
$$

which is equal to $f ^ { \prime } ( \pmb { \xi } _ { i } )$ when $f$ is in $\mathcal { P } _ { 3 }$ . Hence the spline approximation (20.42) is equal to $f ,$ when $f$ is any cubic polynomial.

Therefore, if $f$ is in $\mathcal { C } ^ { ( 4 ) } [ a , b ] ,$ . we may apply the method of proof of Theorem 20.4 to obtain a bound on $d ^ { * } ( \mathcal { S } , f )$ in terms of $\| f ^ { ( 4 ) } \| _ { \infty }$ . To begin this analysis the definition of $f$ is extended to the interval $[ a - 2 h , b + 2 h ]$ in a way that does not increase $\| f ^ { ( 4 ) } \| _ { \infty }$ ，and an operator $L _ { i }$ ，from $\mathscr { C } [ a - 2 h , b + 2 h ]$ to ${ \mathcal { S } } ,$ is defined by the equation

$$
\begin{array} { r l } { { } } & { { \displaystyle { L f } = \sum _ { p = - 3 } ^ { n - 1 } \big [ - \frac { 1 } { 6 } f ( \xi _ { p + 1 } ) + \frac { 4 } { 3 } f ( \xi _ { p + 2 } ) . - \frac { 1 } { 6 } f ( \xi _ { p + 3 } ) \big ] N _ { p } ^ { 3 } } } \\ { { } } & { { = \displaystyle { \sum _ { p = - 3 } ^ { n - 1 } \lambda _ { p } ( f ) N _ { p } ^ { 3 } } , } } \end{array}
$$

say. We let $j = 4$ in expression (20.27),and we note that equation (20.28) is satisfied. Therefore we require an upper bound on $\left| ( L \{ \phi - f \} ) ( \zeta ) \right|$ that is independent of $\zeta .$

Equation (20.45), the properties of $\pmb { B }$ -splines and Theorem 20.1 imply the condition

$$
\begin{array} { r l } { | ( L \{ \phi - f \} ) ( \zeta ) | = \biggr | \displaystyle \sum _ { p = - 3 } ^ { n - 1 } \lambda _ { p } ( \phi - f ) N _ { p } ^ { 3 } ( \zeta ) \biggr | } & { } \\ { = \biggr | \displaystyle \sum _ { p = - q - 3 } ^ { q } \lambda _ { p } ( \phi - f ) N _ { p } ^ { 3 } ( \zeta ) \biggr | } & { } \\ { \leqslant \displaystyle \operatorname* { m a x } _ { q = 3 \in p \in q } \left| \lambda _ { p } ( \phi - f ) \right| \displaystyle \sum _ { p = - q - 3 } ^ { q } \left| N _ { p } ^ { 3 } ( \zeta ) \right| } \\ { = \displaystyle \operatorname* { m a x } _ { q = 3 \in p \in q } \left| \lambda _ { p } ( \phi - f ) \right| , } \end{array}
$$

where $\pmb q$ is still an integer such that $\zeta$ is in the range $[ \xi _ { q } , \xi _ { q + 1 } ]$ . There is no need to introduce a function that corresponds to the function $\psi _ { \zeta }$ in the proof of Theorem 20.4, because expressions (20.45) and (20.30) give the bound

$$
\begin{array} { c l } { { \displaystyle \left| \lambda _ { p } ( \phi - f ) \right| \leqslant \frac { 1 } { 6 } \big | ( f - \phi ) ( \xi _ { p + 1 } ) \big | + \frac { 4 } { 3 } \big | ( f - \phi ) ( \xi _ { p + 2 } ) \big | + \frac { 1 } { 6 } \big | ( f - \phi ) ( \xi _ { p + 3 } ) \big | } } \\ { { \displaystyle \leqslant \frac { \| f ^ { ( 4 ) } \| _ { \infty } } { 1 4 4 } [ \big | \xi _ { p + 1 } - \zeta \big | ^ { 4 } + 8 \big | \xi _ { p + 2 } - \zeta \big | ^ { 4 } + \big | \xi _ { p + 3 } - \zeta \big | ^ { 4 } ] . } } \end{array}
$$

When $p$ is in the interval $[ q - 3 , q ] ,$ ，then $\zeta$ is in the interval $[ \xi _ { p } , \xi _ { p + 4 } ]$ In

this case the greatest possible value of expression (20.47) occurs when $\left| \xi _ { p + 2 } - \zeta \right| = 2 h .$ It follows from equation (20.28)and condition (20.46) that the inequality

$$
| f ( \zeta ) - s ( \zeta ) | \leqslant \frac { 3 5 } { 2 4 } h ^ { 4 } \| f ^ { ( 4 ) } \| _ { \infty } , \qquad a \leqslant \zeta \leqslant b ,
$$

is satisfied, which is a slight improvement on the one that is obtained by setting $k = 3$ and $j = 4$ in Theorem 20.3.

The factor $\frac { 3 5 } { 2 4 }$ in condition (20.48) is much larger than necessary. Most of the loss of precision comes from the third line of expression (20.46), but some of the loss can be avoided by a different choice of $\phi$ For example, we let $\phi$ be the cubic polynomial that interpolates the function values $f ( \xi _ { q - 1 } ) , f ( \xi _ { q } ) , f ( \xi _ { q + 1 } )$ and $f ( \xi _ { q + 2 } )$ . In this case Theorem 4.2 gives the inequality

$$
\begin{array} { r } { \vert f ( x ) - \phi \left( x \right) \vert \leqslant \frac { 1 } { 2 4 } \bigg \vert \underset { j = q - 1 } { \overset { q + 2 } { \prod } } \left( x - \xi _ { j } \right) \bigg \vert \| f ^ { ( 4 ) } \| _ { \infty } , \qquad a \leqslant x \leqslant b , } \end{array}
$$

instead of expression (20.30). It follows that, instead of equation (20.28), the bound

$$
\begin{array} { r } { \left| f ( \zeta ) - s ( \zeta ) \right| \leqslant \left| \phi ( \zeta ) - ( L f ) ( \zeta ) \right| + \left| f ( \zeta ) - \phi ( \zeta ) \right| } \\ { \leqslant \left| ( L \{ \phi - f \} ) ( \zeta ) \right| + \frac { 3 } { 1 2 8 } h ^ { 4 } \left\| f ^ { ( 4 ) } \right\| _ { \infty } } \end{array}
$$

is satisfied, where the last line depends on the fact that $\pmb { \zeta }$ is in $[ \xi _ { q } , \xi _ { q + 1 } ]$ The relation (2O.46) is still valid, but there are substantial changes to expression (20.47) because the terms $\{ ( f - \phi ) ( \xi _ { j } ) ; q - 1 \leqslant j \leqslant q + 2 \}$ are all zero.Hence,when $p = q - 3$ , the definition of $\lambda _ { p }$ and inequality (20.49) imply the bound

$$
\begin{array} { r l } & { \left| \lambda _ { p } ( \phi - f ) \right| = \frac { 1 } { 6 } \big | ( f - \phi ) ( \xi _ { q - 2 } ) \big | } \\ & { \qquad \leqslant \frac { 1 } { 6 } h ^ { 4 } \left\| f ^ { ( 4 ) } \right\| _ { \infty } . } \end{array}
$$

This bound also holds when $\pmb { p } = \pmb { q }$ Similarly, if $p$ is equal to $q - 2$ or $q - 1$ ， then $\lambda _ { p } ( \phi - f )$ is zero.It follows from expressions (20.46) and (20.50) that the inequality

$$
\begin{array} { r } { \big | f ( \zeta ) - s ( \zeta ) \big | \leqslant \frac { 7 3 } { 3 8 4 } h ^ { 4 } \| f ^ { ( 4 ) } \| _ { \infty } , \qquad a \leqslant \zeta \leqslant b , } \end{array}
$$

is obtained, which is sharper than condition (20.48).

By being more ingenious in the choice of $\phi$ ，or by giving detailed attention to the third line of expression (20.46), it is possible to make a further reduction in the constant of inequality (20.52). However,by using a different procedure, the least possible value of this constant is found in Section 22.4.

# 20 Exercises

20.1 Let $k = 2$ ，let $f$ be a quadratic polynomial, and let $\pmb { s }$ be the quadratic spline (20.11),where $\{ \xi _ { j } = j h ; j = - 2 , - 1 , \ldots , n + 2 \}$ and $\{ x _ { p } = \frac { 1 } { 2 } ( \xi _ { p } + \xi _ { p + 3 } ) ; \ p = - 2 , \ - 1 , \ldots , n - 1 \}$ . Show that for every point $\pmb { x }$ in the interval $[ \xi _ { 0 } , \xi _ { n } ] ,$ ，the error $[ f ( { \pmb x } ) - { \pmb s } ( { \pmb x } ) ]$ is equal to the constant $- { \textstyle \frac { 1 } { 8 } } h ^ { 2 } f ^ { \prime \prime } ( x )$

20.2 Let $k$ be a fixed positive integer,and let $\beta$ be a constant such that the inequality

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant \omega \left( \beta h \right)
$$

holds for all functions $f$ in ${ \mathcal { C } } [ a , b ]$ and for all spaces of splines of degree $k$ whose knots satisfy the conditions (20.2),where $\pmb { \omega }$ is the modulus continuity of $f ,$ and where $^ { h }$ has the value (20.3). Prove that $\beta$ is not less than one.Hence Theorem 2O.2 gives the optimal value of $\beta$ when $k = 1$

20.3Prove that, if the bound

$$
d ^ { * } ( { \mathcal { S } } , f ) \leqslant c h ^ { j } \| f ^ { ( j ) } \| _ { \infty } , \quad f \in { \mathcal { C } } ^ { ( j ) } [ a , b ] ,
$$

is satisfied for all spaces $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ whose knots satisfy the condition

$$
\xi _ { i } - \xi _ { i - 1 } \geqslant \mu h , \qquad i = 1 , 2 , \ldots n ,
$$

where $\pmb { \mu }$ is a positive constant that is less than one, and where $h$ is the maximum knot spacing (20.3), then the inequality

$$
d ^ { * } ( \mathcal { S } , f ) \leqslant c \left( h / [ 1 - \mu ] \right) ^ { j } \| f ^ { ( j ) } \| _ { \infty }
$$

holds when there are no restrictions on the positions of the knots of $\mathcal { S }$

20.4 Let $f$ be a quartic polynomial, and let $\pmb { s }$ be the cubic spline in the space $\mathcal { S } ( 3 , 0 , 1 , 2 , 3 , 4 , 5 )$ that satisfies the interpolation conditions $\{ s ( { x } _ { i } ) = f ( { x } _ { i } )$ ； $i = 1 , 2 , 3 , \ldots , 8 \}$ ， where the interpolation points have the values $\begin{array} { r } { \{ x _ { i } = ( i - 1 ) / 3 , i = 1 , 2 , 3 , 4 ; x _ { i } = ( i + 7 ) / 3 , } \end{array}$ ， $i = 5 , 6 , 7 , 8 \}$ . Show that the error $[ f ( 2 \frac { 1 } { 2 } ) - s ( 2 \frac { 1 } { 2 } ) ]$ is equal to ${ \frac { 1 7 9 } { 1 0 3 6 8 } } f ^ { ( 4 ) } ( x )$ ndattdeii $\pmb { s }$ have the values ${ \textstyle \frac { 2 8 } { 2 7 } } f ^ { ( 4 ) } ( x ) , { \textstyle \frac { 2 6 } { 2 7 } } f ^ { ( 4 ) } ( x ) , { \textstyle \frac { 2 6 } { 2 7 } } f ^ { ( 4 ) } ( x )$ and ${ \textstyle \frac { 2 8 } { 2 7 } } f ^ { ( 4 ) } ( x )$

20.5 Obtain a bound on $\| f - s \| _ { \infty }$ that is stronger than condition (20.52) by substituting the conditions on $\begin{array} { r } { \{ \vert \lambda _ { p } ( \phi - f ) \vert ; q - 3 \leqslant p \leqslant q \} , } \end{array}$ that are given immediately before inequality (20.52), into the second line of expression (20.46).

20.6 Let the knots $\{ \xi _ { j } \}$ have the values (20.34),and let ${ \pmb S } _ { \pmb { \alpha } }$ be the cubic spline approximation

$$
s _ { \alpha } ( x ) = \sum _ { p = - 3 } ^ { n - 1 } \left[ f ( \xi _ { p + 2 } ) + \alpha f ^ { \prime \prime } ( \xi _ { p + 2 } ) \right] N _ { p } ^ { 3 } \left( x \right) , \qquad a \leqslant x \leqslant b ,
$$

to a function $f$ in $\mathcal { C } ^ { ( 4 ) } [ a - h , b + h ]$ .Calculate the value of $\pmb { \alpha }$ such that ${ \pmb S } _ { { \pmb \alpha } }$ is equal to $f$ when $f$ is a cubic polynomial. Hence find a bound on the error $\{ | f ( x ) - s ( x ) | ; a \leqslant x \leqslant b \}$ of the form (20.48).

).7 Investigate whether the inequality of Exercise 20.2 is valid when $k = 2$ and $\beta = 1$

Improve the bound of Theorem 20.4 by replacing the function (20.27) by a polynomial of degree $( j - 1 )$ that interpolates $f$ at suitable points of the interval (20.29).

20.9 Prove that the Chebyshev polynomial $T _ { k }$ maximizes the derivative $\{ \| p ^ { \prime } \| _ { \infty } ; p \in \mathcal { P } _ { k } \}$ subject to the condition $\| p \| _ { \infty } \leqslant 1$ , where the $\infty$ -norm applies to the interval [-1,1]. Hence deduce that the bound

$$
\operatorname* { m a x } _ { \xi _ { i - 1 } \le x \le \xi _ { i } } \big | p ( x ) \big | \geqslant \frac { ( \xi _ { i } - \xi _ { i - 1 } ) } { 2 k ^ { 2 } } \operatorname* { m a x } _ { \xi _ { i - 1 } \le x \le \xi _ { i } } \big | p ^ { \prime } ( x ) \big | , \qquad p \in \mathcal { P } _ { k } ,
$$

is satisfied. This condition is required for the next exercise.

20.10 Let $f$ be a function in $\mathcal { C } ^ { ( j ) } [ a , b ]$ ，and let $\pmb { s }$ be a spline in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that satisfies the condition

$$
\| \boldsymbol { f } - \boldsymbol { s } \| _ { \infty } \leqslant c h ^ { j } \| \boldsymbol { f } ^ { ( j ) } \| _ { \infty } ,
$$

where $k \geqslant j - 1 \geqslant 1$ ，where $^ c$ is a constant, and where $h$ is the maximum interval between knots. Prove that $ \| f ^ { \prime } - s ^ { \prime } \| _ { \infty }$ is bounded above by a constant multiple of the expression $h ^ { j } \parallel f ^ { ( j ) } \parallel _ { \infty } / \eta ,$ where $\pmb { \eta }$ is the smallest of the numbers $\{ \xi _ { i } - \xi _ { i - 1 } ; i = 1 , 2 , \ldots , n \}$ Note that it is helpful to use Exercise 20.9 to bound the difference $\left| f ^ { \prime } ( \zeta ) - s ^ { \prime } ( \zeta ) \right| = \left| \phi ^ { \prime } ( \zeta ) - s ^ { \prime } ( \zeta ) \right| ,$ where $\pmb { \zeta }$ is any point of the interval $[ \xi _ { i - 1 } , \xi _ { i } ] ,$ ,and where $\phi$ is the Taylor series approximation to $f$ at $\pmb { \zeta }$ of degree $( j - 1 )$

# Knot positions and the calculation of spline approximations

# 21.1 The distribution of knots at a singularity

A strong advantage of letting the knots of a spline approximation have the equally spaced values

$$
\xi _ { j } = \xi _ { 0 } + \left( j / n \right) ( \xi _ { n } - \xi _ { 0 } ) , \qquad j = 0 , 1 , \ldots , n ,
$$

is that,for any $x$ in $[ a , b ] ,$ ,one can find by one division and one integer part operation an index $j$ such that the condition $\xi _ { j } \leqslant x \leqslant \xi _ { j + 1 }$ is satisfied. It is often possible, however, to reduce greatly the total number of knots by giving up the condition that the spacing between knots is constant. In order to demonstrate this point, we consider the approximation of the function $\{ f ( x ) = x ^ { \frac { 1 } { 2 } }$ ； $0 \leqslant x \leqslant 1 \}$ by the piecewise linear function $\pmb { s }$ from the space $\mathcal { S } ( 1 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ (where ${ \xi _ { 0 } } = 0$ and $\xi _ { n } = 1$ ） that is defined by the interpolation conditions

$$
s ( \xi _ { i } ) = f ( \xi _ { i } ) , \qquad i = 0 , 1 , . . . , n .
$$

We consider the number of knots that are needed to provide the accuracy

$$
\| f - s \| _ { \infty } \leqslant \varepsilon ,
$$

where $\varepsilon$ is a small positive constant.

In each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , 1 , \dots , n - 1 \}$ , the error function satisfies the equation

$$
f ( x ) - s \left( x \right) = x ^ { \frac { 1 } { 2 } } - \frac { \xi _ { j } ^ { \frac { 1 } { 2 } } \left( \xi _ { j + 1 } - x \right) + \xi _ { j + 1 } ^ { \frac { 1 } { 2 } } \left( x - \xi _ { j } \right) } { \xi _ { j + 1 } - \xi _ { j } } , \qquad \xi _ { j } \leqslant x \leqslant \xi _ { j + 1 } .
$$

Therefore the maximum error on $[ \xi _ { j } , \xi _ { j + 1 } ]$ occurs at the point $x =$ $\begin{array} { r } { \frac { 1 } { 4 } ( \xi _ { j } ^ { \frac { 1 } { 2 } } + \xi _ { j + 1 } ^ { \frac { 1 } { 2 } } ) ^ { 2 } } \end{array}$ . Here the modulus of the error function has the value

$$
\begin{array} { r } { \frac { 1 } { 4 } \big ( \xi _ { j + 1 } ^ { \frac { 1 } { 3 } } - \xi _ { j } ^ { \frac { 1 } { 2 } } \big ) ^ { 2 } / ( \xi _ { j } ^ { \frac { 1 } { 2 } } + \xi _ { j + 1 } ^ { \frac { 1 } { 3 } } ) . } \end{array}
$$

If the knots are equally spaced, then this expression is greatest when $j = 0$

Hence $\| f - s \| _ { \infty }$ is equal to ${ \frac { 1 } { 4 } } n ^ { - { \frac { 1 } { 2 } } }$ . It follows that, in order to achieve the bound (21.3), the integer $_ n$ must not be less than $1 / { ( 4 \varepsilon ) } ^ { 2 }$

If there are no restrictions on the positions of the knots, however, then the values

$$
\xi _ { j } = ( j / n ) ^ { 4 } , \qquad j = 0 , 1 , \ldots , n ,
$$

are particularly suitable. In this case expression (21.5) gives the identity

$$
\operatorname* { m a x } _ { \xi _ { i } \le x \le \xi _ { i + 1 } } \big | f ( x ) - s ( x ) \big | = \frac { 1 } { 4 n ^ { 2 } } \frac { 4 j ^ { 2 } + 4 j + 1 } { 2 j ^ { 2 } + 2 j + 1 } .
$$

Because the right-hand side is bounded above by $1 / 2 { n } ^ { 2 }$ , the accuracy (21.3) is achieved if $_ n$ is not less than $( 2 \varepsilon ) ^ { - \frac { 1 } { 2 } }$ , which is a large improvement on the previous bound. For example, if $\varepsilon = 1 0 ^ { - 4 }$ ，then $n \geq 2 5 \times { 1 0 } ^ { 6 }$ when the knots are equally spaced,but the distribution (21.6) allows $n = 7 1$ . The reduction in the number of knots that can be made by adapting the knot positions to the form of $f$ is usually even greater when $\pmb { s }$ is a quadratic or a cubic spline.

It is interesting to compare the number of knots that are needed to approximate the functions $\{ f ( x ) = x ^ { \frac { 1 } { 2 } }$ ； $0 \leqslant x \leqslant 1 \}$ and $\{ f ( x ) = 2 x ^ { 2 }$ ； $0 \leqslant x \leqslant$ 1} to accuracy $\pmb \varepsilon$ by a linear spline.When $f$ is a quadratic polynomial it is best to use a constant knot spacing.Hence in both cases the fewest number of knots that is necessary to achieve the required accuracy is about $( 2 \varepsilon ) ^ { - { \frac { 1 } { 2 } } }$ , even though one function has a singularity and the other one is very smooth. It happens often that singularities in $f$ do not increase greatly the total number of knots, provided that careful attention is given to the knot positions.

One kind of singularity that can be fitted easily is a derivative discontinuity. We consider the case when $f ^ { ( q ) }$ is discontinuous at $\bar { x }$ where $q$ is an integer in the interval $[ 1 , k ]$ ,and where $\bar { x }$ is an interior point of the range $[ a , b ]$ .When $q = k .$ , then placing one of the knots $\left\{ \xi _ { i } ; i = 1 , 2 , \ldots , \right.$ $n - 1 \}$ at $\bar { x }$ allows the discontinuity to be fitted exactly， because the function

$$
\sigma ( x ) = ( x - \bar { x } ) _ { + } ^ { q } , \qquad a \leqslant x \leqslant b ,
$$

is in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ . When $q$ is less than $k$ ,then it is suitable to let $( k + 1 - q )$ of the knots $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ be close to $\bar { x } ,$ ,because the following theorem shows that in this way the function (21.8) can be approximated arbitrarily closely by an element of ${ \mathcal { S } } .$

# Theorem 21.1

Let $q$ be an integer in $[ 1 , k - 1 ]$ ,and let $\sigma$ be the function (21.8), where $\bar { x }$ is any fixed point in $( a , b )$ .For any $\varepsilon > 0$ , there exists a spline $\pmb { s }$ in

$\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that satisfies the inequality

$$
\| { \pmb \sigma } - { \pmb s } \| _ { \infty } \leqslant { \pmb \varepsilon } ,
$$

provided that the condition

$$
\left| { \bar { x } } - \xi _ { j } \right| \leqslant \varepsilon / [ q \ ( b - a ) ^ { q - 1 } ]
$$

holds for at least $( k + 1 - q )$ of the knots $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$

Proof. We let the knots $\{ \xi _ { i } ; j = p , p + 1 , \ldots , p + k - q \}$ satisfy condition (21.10),and we let $\pmb { s }$ be the function

$$
s ( x ) = \frac { ( - 1 ) ^ { k - q } ( k - q ) ! q ! } { k ! } \sum _ { { j = p \atop i = p } } ^ { p + k - q } \frac { ( x - \xi _ { j } ) _ { + } ^ { k } } { \underset { i = p } { \prod _ { j = k + 1 } ^ { p + k - q } } ( \xi _ { j } - \xi _ { i } ) } , \qquad a \leqslant x \leqslant b ,
$$

which is in $\mathcal { S } .$ Equation (5.2) shows that,for any fixed $x , s ( x )$ is the divided difference $g [ \xi _ { p } , \xi _ { p + 1 } , \ldots , \xi _ { p + k - q } ] _ { : }$ where $\pmb { g }$ is the function

$$
g ( \theta ) = ( - 1 ) ^ { k - q } [ ( k - q ) ! q ! / k ! ] ( x - \theta ) _ { + } ^ { k } , \qquad a \leqslant \theta \leqslant b .
$$

It follows from Theorem 5.1 that $s ( x )$ has the value

$$
\begin{array} { c } { { s ( x ) = \left[ 1 / ( k - q ) ! \right] g ^ { ( k - q ) } ( \xi ) } } \\ { { = ( x - \xi ) _ { + } ^ { q } , } } \end{array}
$$

where $\xi$ is in the interval $[ \xi _ { p } , \xi _ { p + k - q } ]$ and depends on $x$ .The remainder of the proof depends only on equations (21.8) and (21.13),and the fact that $\xi$ satisfies the condition

$$
{ \left| { \bar { x } - \xi } \right| } \leqslant \varepsilon / [ q \left( { b - a } \right) ^ { q - 1 } ] .
$$

If $q = 1$ ,then equations (21.8) and (21.13) imply the inequality

$$
\left| \sigma ( x ) - s ( x ) \right| \leqslant \left| { \bar { x } } - \xi \right| .
$$

When $q > 1$ ，the mean value theorem is applied to the function $\{ ( x - \theta ) _ { + } ^ { q }$ ； $a \leqslant \theta \leqslant b \}$ to deduce the equation

$$
\left| \sigma ( x ) - s ( x ) \right| = \left| { \bar { x } } - \xi \right| q ( x - \zeta ) _ { + } ^ { q - 1 } ,
$$

where $\pmb { \zeta }$ is between $\bar { x }$ and $\xi .$ The term $( x - \zeta ) _ { + } ^ { q - 1 }$ is bounded above by $( b - a ) ^ { q - 1 }$ . It follows from expressions (21.14), (21.15) and (21.16) that $\left| \sigma ( { \pmb x } ) - s ( { \pmb x } ) \right|$ does not exceed $\pmb { \varepsilon }$ .Because this statement holds for all $x$ in $[ a , b ] .$ ,the theorem is proved.□

In practice,instead of choosing the knots $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ in such a way that the function (21.8) can be approximated to high accuracy by an element of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ , it is more convenient to let the function (21.8) be in the set of.approximating functions. Therefore we extend the definition of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ in order to allow repeats in the set $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ . If the conditions

$$
a = \xi _ { 0 } \leqslant \xi _ { 1 } \leqslant \xi _ { 2 } \leqslant . ~ . ~ \leqslant \xi _ { n } = b
$$

hold,and if at least one of the inequalities is satisfied as an equation, then the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ is defined as follows. It is the space that is spanned by the functions $\{ x ^ { i } , a \leqslant x \leqslant b$ ； $i = 0 , 1 , \ldots , k \}$ and $\{ ( { \pmb x } - { \pmb \xi } _ { j } ) _ { + } ^ { i } .$ ， $a \leqslant x \leqslant b ; k + 1 - q ( j ) \leqslant i \leqslant k ; j = 1 , 2 , \ldots , n - 1 \}$ ,where $q ( j )$ is the minimum of $k$ and the number of times that the number $\xi _ { j }$ Occurs in the set $\{ \xi _ { p } ; p = 1 , 2 , \ldots , n - 1 \}$ .Most of the theory that is given in Chapters 19 and 20 applies to the extended definition of $\mathcal { S }$

# 21.2 Interpolation for general knots

In order that the results of the previous section are useful, there is a need for an algorithm that calculates an approximation from $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ to a function $f$ in $\mathcal { C } [ a , b ]$ ,without unnecessary loss of accuracy when the distribution of knots is highly irregular. Interpolation methods are often suitable,provided that the interpolation points $\{ x _ { i }$ ； $i = 1 , 2 , \ldots , n + k \}$ are selected carefully. The conditions of Theorem 19.4 must be satisfied,and then the equations

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , n + k ,
$$

define a unique element of $\mathcal { S }$ for each $f$ in $\mathcal { C } [ a , b ]$ . Thus the interpolation algorithm is a linear projection operator from ${ \mathcal { C } } [ a , b ]$ to ${ \mathcal { S } } .$ It follows from Theorem 3.1 that, if the norm of the interpolation operator is small, then the error of the calculated approximation is never much larger than necessary. Therefore we seek interpolation points that make the norm small.

If the splines are piecewise linear functions, then the norm of the interpolation procedure is one if the interpolation points are the knots. For $k \geqslant 2$ , it is usually suitable to include the values

$$
x _ { i } = \left( \xi _ { i - k } + \xi _ { i - k + 1 } + . . . + \xi _ { i - 1 } \right) / k , \qquad i = k , k + 1 , \ldots , n + 1 .
$$

The following theorem makes this statement definite in the case when $k = 2$ . We find later, however, that, if the interpolation points are specified before the knots are chosen, then it may not be possible to achieve a small norm.

# Theorem 21.2

For any $f$ in ${ \mathcal { C } } [ a , b ]$ ,let $s = L f$ be the quadratic spline in the space $\mathcal { S } ( 2 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is defined by the interpolation conditions

(21.18), where the knots are in ascending order

$$
a = \xi _ { 0 } < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } = b ,
$$

and where the interpolation points have the values

$$
\left. { \begin{array} { l } { x _ { 1 } = \xi _ { 0 } } \\ { x _ { i } = { \frac { 1 } { 2 } } ( \xi _ { i - 2 } + \xi _ { i - 1 } ) , \qquad i = 2 , 3 , \ldots , n + 1 } \\ { x _ { n + 2 } = \xi _ { n } } \end{array} } \right\} .
$$

Then the norm of the interpolation operator satisfies the bound

$$
\| L \| _ { \infty } \leqslant 2 .
$$

Proof. Let $s _ { j }$ be the quadratic function that is equal to $\pmb { s }$ on the interval $[ \xi _ { j } , \xi _ { j + 1 } ]$ .Because $x _ { j + 2 }$ is the mid-point of this interval, the quadratic can be expressed in terms of the function values $s ( \xi _ { j } ) , f ( x _ { j + 2 } )$ and $\pmb { s } ( \pmb { \xi } _ { j + 1 } )$ Hence the equations

$$
\begin{array} { r l } & { ( \xi _ { j + 1 } - \xi _ { j } ) s _ { j } ^ { \prime } ( \xi _ { j } ) = - 3 s ( \xi _ { j } ) + 4 f ( x _ { j + 2 } ) - s ( \xi _ { j + 1 } ) } \\ & { ( \xi _ { j + 1 } - \xi _ { j } ) s _ { j } ^ { \prime } ( \xi _ { j + 1 } ) = s ( \xi _ { j } ) - 4 f ( x _ { j + 2 } ) + 3 s ( \xi _ { j + 1 } ) } \end{array} \bigg \}
$$

are satisfied. Therefore the first derivative continuity conditions $\{ s _ { j } ^ { \prime } ( \xi _ { j + 1 } ) = s _ { j + 1 } ^ { \prime } ( \xi _ { j + 1 } ) ; j = 0 , 1 , \ldots , n - 2 \}$ give the recurrence relations

$$
\begin{array} { r l } & { s ( \xi _ { j } ) h _ { j + 1 } + 3 s ( \xi _ { j + 1 } ) [ h _ { j } + h _ { j + 1 } ] + s ( \xi _ { j + 2 } ) h _ { j } } \\ & { \quad = 4 f ( x _ { j + 2 } ) h _ { j + 1 } + 4 f ( x _ { j + 3 } ) h _ { j } , \qquad j = 0 , 1 , \ldots , n - 2 , } \end{array}
$$

where $h _ { j }$ is the length of the interval $[ \xi _ { j } , \xi _ { j + 1 } ]$ Let $M = \left| s ( \xi _ { q } ) \right|$ be the largest of the numbers $\{ | s ( \xi _ { j } ) | ; j = 0 , 1 , \ldots , n \}$ If $1 \leqslant q \leqslant n - 1$ ，then expression (21.24) implies the bound

$$
3 M ( h _ { q - 1 } + h _ { q } ) \leqslant ( 4 \| f \| _ { \infty } + M ) ( h _ { q - 1 } + h _ { q } ) ,
$$

which shows that $M$ is not greater than $2 \| f \| _ { \infty }$ . Alternatively, if $q$ is 0 or $_ n$ ， then the equation $s ( \xi _ { q } ) = f ( \xi _ { q } )$ holds. It follows that the inequalities

$$
| s ( \xi _ { j } ) | \leqslant 2 \| f \| _ { \infty } , \qquad j = 0 , 1 , \ldots , n ,
$$

are obtained. Moreover,equations (21.18) and (21.21) give the conditions

$$
\begin{array} { r } { \big | s \big ( \frac 1 2 [ \xi _ { j } + \xi _ { j + 1 } ] \big ) \big | \leqslant \| f \| _ { \infty } , \qquad j = 0 , 1 , \ldots , n - 1 . } \end{array}
$$

The required bound on $\| L \| _ { \infty }$ will be derived from the last two inequalities and the fact that $\pmb { s }$ is a quadratic function on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , 1 , \dots , n - 1 \}$

In order to simplify notation, we suppose that $\xi _ { j } = 0$ and $\xi _ { j + 1 } = 1$ . Then the Lagrange interpolation formula and expressions (21.26) and (21.27)

imply that, if $\textstyle 0 \leqslant x \leqslant { \frac { 1 } { 2 } }$ , the condition

$$
{ \begin{array} { r l r } & { | s ( x ) | = \left| 2 ( x - { \frac { 1 } { 2 } } ) ( x - 1 ) s ( 0 ) + 4 ( x - x ^ { 2 } ) s ( { \frac { 1 } { 2 } } ) + 2 ( x ^ { 2 } - { \frac { 1 } { 2 } } x ) s ( 1 ) \right| } \\ & { \qquad \leqslant 4 \| f \| _ { \infty } [ ( x - { \frac { 1 } { 2 } } ) ( x - 1 ) + ( x - x ^ { 2 } ) + ( { \frac { 1 } { 2 } } x - x ^ { 2 } ) ] } \\ & { \qquad } & { = 4 \| f \| _ { \infty } [ { \frac { 1 } { 2 } } - x ^ { 2 } ] \leqslant 2 \| f \| _ { \infty } \qquad ( 2 } \end{array} }
$$

is satisfed. Similarly this condition holds when $\textstyle { \frac { 1 } { 2 } } \leqslant x \leqslant 1$ . The same technique may be used to bound $\left| s ( x ) \right|$ on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = 0 , 1 , \dots , n - 1 \}$ .Hence $\| s \| _ { \infty }$ is not greater than $2 \| f \| _ { \infty }$ , which is the required result.□

Unfortunately there is no constant bound on $\| L \| _ { \infty }$ when $\pmb { s }$ is a quadratic spline,and when, instead of placing the interpolation points midway between the knots,the procedure of Section 18.4 is followed, which places the knots midway between the interpolation points. There is not even a constant upper bound on the norm of the interpolation operator if the knot positions are chosen to minimize the norm. This result is easy to prove if there are only three interpolation points,because then $\pmb { s }$ is just a quadratic polynomial. It is more interesting, however, to consider a case when the maximum distance between adjacent interpolation points can be made arbitrarily small. We find that it is still possible for the distribution of interpolation points to prevent a bounded norm.The demonstration depends on an elementary property of quadratic splines,which is proved in the following theorem, in order to separate it from the main argument.

# Theorem 21.3

Let $\pmb { s }$ be any quadratic spline,and let $( \alpha , \beta )$ be any interval of the real line that contains at most two knots. Then the inequality

$$
\operatorname* { m a x } _ { \alpha \leqslant x \leqslant \beta } \left| s \left( x \right) \right| \geqslant \frac { 1 } { 2 0 } ( \beta - \alpha ) \left| s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] ) \right|
$$

is satisfied.

Proof.If $\pmb { S }$ is a quadratic polynomial on the interval $[ u , v ]$ , then straightforward algebra shows that the bound

$$
\operatorname* { m a x } _ { u \leqslant x \leqslant v } \left| s ( x ) \right| \geqslant \frac { 1 } { 8 } ( v - u ) \operatorname* { m a x } \left[ \left| s ^ { \prime } ( u ) \right| , \left| s ^ { \prime } ( v ) \right| \right]
$$

holds in general, and that the bound

$$
\operatorname* { m a x } _ { u \leqslant x \leqslant v } \left| s ( x ) \right| \geqslant \frac { 1 } { 2 } ( v - u ) \operatorname* { m i n } \left[ \left| s ^ { \prime } ( u ) \right| , \left| s ^ { \prime } ( v ) \right| \right]
$$

is obtained in the particular case when the signs of the derivatives $\pmb { s } ^ { \prime } ( u )$ and $\pmb { s } ^ { \prime } ( \pmb { v } )$ are the same. If there is no knot in the interval $( \alpha , \frac { 1 } { 2 } [ \alpha + \beta ] )$ ,then expression (21.30) implies that inequality (21.29) is satisfied,with the factor $\scriptstyle { \frac { 1 } { 2 0 } }$ replaced by $\scriptstyle { \frac { 1 } { 1 6 } }$ .Similarly this inequality holds when there is no knot in the interval $( \frac { 1 } { 2 } [ \alpha + \beta ] , \beta )$ . Therefore it remains to consider the case when there are two knots in $( \alpha , \beta ) , \ \xi _ { j }$ and $\xi _ { j + 1 }$ say，such that $\xi _ { j } < \frac { 1 } { 2 } ( \alpha + \beta ) < \xi _ { j + 1 }$ .Because the derivative $\{ s ^ { \prime } ( x ) ; \xi _ { j } \leqslant x \leqslant \xi _ { j + 1 } \}$ is a linear function, we may assume without loss of generality that $\pmb { s } ^ { \prime } ( \pmb { \xi } _ { j + 1 } ) \geq$ $s ^ { \prime } ( { \scriptstyle { \frac { 1 } { 2 } } } [ \alpha + \beta ] )$ ,and that $s ^ { \prime } ( { \scriptstyle { \frac { 1 } { 2 } } } [ \alpha + \beta ] )$ is non-negative. It follows from expressions (21.30) and (21.31) that the bounds

$$
\begin{array} { r l } & { \underset { \xi _ { i + 1 } \leqslant x \leqslant \beta } { \operatorname* { m a x } } \left| s \left( x \right) \right| \geqslant \frac { 1 } { 8 } ( \beta - \xi _ { i + 1 } ) s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] ) } \\ & { \underset { \frac { 1 } { 2 } ( \alpha + \beta ) \leqslant x \leqslant \xi _ { j + 1 } } { \operatorname* { m a x } } \left| s \left( x \right) \right| \geqslant \frac { 1 } { 2 } ( \xi _ { j + 1 } - \frac { 1 } { 2 } [ \alpha + \beta ] ) s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] ) \Bigg ] } \end{array}
$$

are obtained. Because the greater right-hand side is least when $\xi _ { j + 1 } =$ $0 . 4 \alpha + 0 . 6 \beta$ , the inequality

$$
\operatorname* { m a x } _ { { \scriptstyle \frac { 1 } { 2 } } ( \alpha + \beta ) \leqslant x \leqslant \beta } \left| s ( x ) \right| \geqslant \frac { 1 } { 2 0 } ( \beta - \alpha ) \ s ^ { \prime } ( \frac { 1 } { 2 } [ \alpha + \beta ] )
$$

holds,which completes the proof of the theorem.

In order to show that, if $\pmb { s } = \pmb { L } ( f )$ is the spline in $\mathcal { S } ( 2 , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that is defined by the interpolation conditions (21.18), then $\| \pmb { L } \| _ { \infty }$ may be large, even if the knot positions are chosen carefully, we consider the case when the spacings between the interpolation points are the distances

$$
\begin{array} { r } { x _ { i + 1 } - x _ { i } = \left\{ \begin{array} { c c } { h , } & { i \mathrm { ~ o d d } , } \\ { \delta h , } & { i \mathrm { ~ e v e n } , } \end{array} \right. \quad \quad i = 1 , 2 , \ldots , n + 1 , } \end{array}
$$

where $h$ and $\delta$ are positive constants, and where $\pmb \delta$ is much smaller than one. It is sufficient to show that $\| \pmb { s } \| _ { \infty }$ is large when the data have the values $\{ f ( x _ { i } ) = ( - 1 ) ^ { i + 1 }$ ； $i = 1 , 2 , \ldots , n + 2 \}$ If $q$ is any even integer in the range $[ 2 , n ] ,$ , then the mean value theorem implies that there is a point $\pmb { \eta _ { q } }$ in the interval $\left( x _ { q } , x _ { q + 1 } \right)$ that satisfies the equation

$$
\begin{array} { c } { { s ^ { \prime } ( \eta _ { q } ) = [ s ( x _ { q + 1 } ) - s ( x _ { q } ) ] / ( x _ { q + 1 } - x _ { q } ) } } \\ { { { } } } \\ { { = 2 / ( \delta h ) . } } \end{array}
$$

Because the intervals $\{ ( \eta _ { q } - { \textstyle \frac { 1 } { 2 } } h , \eta _ { q } + { \textstyle \frac { 1 } { 2 } } h ) ; q = 2 , 4 , 6 , . . . \}$ are disjoint, and because the number of internal knots of the spline is only $( n - 1 )$ ，it follows that, when $_ n$ is large, there are fewer than three knots in several of the intervals $\{ ( \eta _ { q } - \frac { 1 } { 2 } h , \eta _ { q } + \frac { 1 } { 2 } h )$ ； $q = 2 , 4 , 6 , \ldots \}$ .We apply Theorem 21.3 to any one of them,where $( \alpha , \beta ) = ( \eta _ { q } - \textstyle \frac 1 2 h , \eta _ { q } + \textstyle \frac 1 2 h )$ . Hence equation (21.35) gives the bound

$$
\| s \| _ { \infty } \geqslant 1 / ( 1 0 \delta ) .
$$

This inequality holds for all choices of knots, and $\pmb { \delta }$ can be arbitrarily small. Therefore some distributions of interpolation points make it inevitable that the norm of the interpolation operator is large.Hence it is important sometimes to choose the positions of the knots before the positions of the interpolation points,and then Theorem 21.2 gives a convenient way of achieving a small norm.

# 21.3 The approximation of functions to prescribed accuracy

This section considers the problem of calculating automatically a cubic spline function $\pmb { s }$ that satisfies the condition

$$
\| f - s \| _ { \infty } \leqslant \varepsilon ,
$$

where $f$ is a given function in $\mathcal { C } [ a , b ]$ ,and where $\pmb \varepsilon$ is a given constant tolerance.One reason for this study is that, if a computer program requires the value $f ( x )$ for many thousand different values of $x$ ,and if each evaluation takes several seconds of computer time, then it is necessary to replace $f$ by an approximation that can be calculated easily. We let $\pmb { s }$ be a cubic spline approximation, because cubic splines give a good balance between smoothness and flexibility.

First we consider a spline whose knots are equally spaced

$$
\xi _ { j } = \xi _ { 0 } + j h , \qquad j = 0 , 1 , \ldots , n ,
$$

and that satisfies the interpolation conditions

$$
s ( \xi _ { j } ) = f ( \xi _ { j } ) , \qquad j = 0 , 1 , . . . , n .
$$

We suppose that the technique that fixes the two end conditions, discussed in Section 18.3,is such that,if $f$ is a quartic polynomial, then $s ^ { \prime } ( a )$ and $s ^ { \prime } ( b )$ are equal to $f ^ { \prime } ( a )$ and $f ^ { \prime } ( b )$ respectively.For example,Exercise 18.3 shows that it is sufficient to satisfy the equations $d _ { 1 } = d _ { 2 }$ and $d _ { n - 2 } = d _ { n - 1 }$ ,where $d _ { j }$ is the third derivative discontinuity

$$
d _ { j } = s ^ { \prime \prime \prime } ( \xi _ { j } + ) - s ^ { \prime \prime \prime } ( \xi _ { j } - ) , \qquad j = 1 , 2 , \ldots , n - 1 .
$$

If the number of knots of $\pmb { s }$ is to be chosen automatically, then it is necessary to predict whether the accuracy (21.37) is obtained.

In order to derive an error estimate, we follow an approach that is often successful. It is to analyse the error of the spline approximation when $f$ is a polynomial of the lowest degree that gives a non-zero error. Therefore we assume that $f$ is in ${ \mathcal { P } } _ { 4 }$ ,and we note that Exercise 18.3 implies the values

$$
\begin{array} { c c } { { s ( \xi _ { j } ) = f ( \xi _ { j } ) } } \\ { { s ^ { \prime } ( \xi _ { j } ) = f ^ { \prime } ( \xi _ { j } ) } } \end{array} \bigg \} , ~ j = 0 , 1 , . . . , n ,
$$

and

$$
d _ { j } = h f ^ { ( 4 ) } ( \xi ) , \qquad j = 1 , 2 , \dots , n - 1 ,
$$

where $\pmb { \xi }$ is any point of $[ a , b ]$ .Because the function $\{ f ( x ) - s ( x ) ; \xi _ { q } \leqslant x \leqslant$

$\xi _ { q + 1 } \big \}$ is a quartic polynomial, where $q$ is any integer in $[ 0 , n - 1 ]$ ,it follows from expressions (21.41) and (21.42) that the equation

$$
\begin{array} { r l } { f ( x ) - s ( x ) = \frac { 1 } { 2 4 } ( x - \xi _ { q } ) ^ { 2 } ( x - \xi _ { q + 1 } ) ^ { 2 } f ^ { ( 4 ) } ( \xi ) \ d t } \\ { = \displaystyle \frac { 1 } { 2 4 h } ( x - \xi _ { q } ) ^ { 2 } ( x - \xi _ { q + 1 } ) ^ { 2 } d _ { j } , \qquad \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } , } \end{array}
$$

is satisfied. Because the greatest error occurs at the point $\begin{array} { r } { { \pmb x } = \frac { 1 } { 2 } ( { \pmb \xi } _ { q } + { \pmb \xi } _ { q + 1 } ) } \end{array}$ it has the value

$$
\operatorname* { m a x } _ { \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } } | f ( x ) - s ( x ) | = \frac { h ^ { 3 } } { 3 8 4 } | d _ { j } | ,
$$

where $d _ { j }$ is any one of the third derivative discontinuities of $s$ , and where $f$ is a fourth degree polynomial.

The next stage of the derivation of the error estimate is to let $f$ be an infinitely differentiable function, and to consider the error of the spline approximation to the Taylor series expansion

$$
f ( x ) = \sum _ { i = 0 } ^ { \infty } { \frac { ( x - \xi ) ^ { i } } { i ! } } f ^ { ( i ) } ( \xi ) , \qquad a \leqslant x \leqslant b ,
$$

where $\xi$ is any fixed point of $[ a , b ]$ . Because the interpolation method for calculating the spline approximation is a linear operator, the error $( f - s )$ is the sum of the errors that occur when the separate terms of the Taylor series are approximated by splines. It is important to note that, because the cardinal function of Figure 18.2 decays exponentially, the error $\{ f ( \xi ) - s ( \xi )$ ； $a \leqslant \xi \leqslant b \}$ is dominated by the form of $\{ f ( x ) ; a \leqslant x \leqslant b \}$ in a neighbourhood of $\xi .$ Therefore,for sufficiently small $h _ { \ast }$ ,the error at $\xi$ is mostly due to the fourth derivative term of expression (21.45). A similar argument shows that, if $h$ is sufficiently small, and if $\xi _ { j }$ is close to $\xi ,$ ，then the main contribution to the third derivative discontinuity (21.40) also comes from the fourth derivative term of the Taylor series. By combining these remarks with equation (21.44),we obtain the error estimate

$$
\operatorname* { m a x } _ { \xi _ { q } \leqslant x \leqslant \xi _ { q + 1 } } { \big | } f ( x ) - s ( x ) { \big | } \approx { \frac { h ^ { 3 } } { 3 8 4 } } \operatorname* { m a x } { [ \big | } d _ { q } { \big | } , \big | d _ { q + 1 } { \big | } ] .
$$

It may be used for $q = 1 , 2 , \ldots , n - 2 .$ When $q = 0$ the term $\left| d _ { q } \right|$ is deleted from the right-hand side,and when $q = n - 1$ the term $| d _ { q + 1 } |$ is deleted, because $s$ does not have third derivative discontinuities at $\xi _ { 0 }$ and $\xi _ { n }$

The approximation (21.46) is usually adequate in practice,even when $f$ has some mild singularities. It is easy to calculate the right-hand side of the approximation from the parameters of $\pmb { S } ,$ . Because there are separate error estimates for each of the intervals $\{ [ \xi _ { q } , \xi _ { q + 1 } ] ; q = 0 , 1 , \ldots , n - 1 \}$ a computer program can find automatically when it is advantageous to give up the condition that the spacing between knots is constant.

The example of Section 21.1 shows that changes in knot spacing can give large gains in efficiency，but one loses the advantage that is mentioned in the opening sentence of this chapter, error control is more difficult when there are frequent changes of knot spacing,and also, if a sequence of trial approximations to $f$ is calculated, then it is more difficult to control the positions of interpolation points so that full use is made of all calculated values of $f ( x )$ . A successful compromise is to keep each knot spacing for several consecutive intervals,and to allow only halving and doubling where the knot spacing changes.Therefore we consider the case when the knots have the values

$$
\begin{array} { l } { { \xi _ { j } = \xi _ { r } + ( j - r ) h , \qquad j = 0 , 1 , \ldots , r } } \\ { { \qquad \xi _ { j } = \xi _ { r } + 2 ( j - r ) h , \qquad j = r , r + 1 , \ldots , n } } \end{array} \biggr \} ,
$$

where $\xi _ { r }$ is remote from the ends of the range $[ a , b ]$ . In particular, we ask whether the error estimate (21.46) is suitable if $q$ is close to $\boldsymbol { r }$

Because of the importance of the fourth order term of the Taylor series (21.45), we again let $f$ be a quartic polynomial, and we let $e = f - s$ be the error function of the spline approximation that is defined by interpolation at the knots (21.47).In order to analyse this error function, we compare it with $e _ { h }$ and $e _ { 2 h }$ ,which are the error functions that would be obtained if the spacing between knots were the constants $h$ and $^ { 2 h }$ respectively.The solid line of Figure 21.1 is the function $^ e$ ,and the dotted line is composed of the functions $\{ e _ { h } ( x ) ; \xi _ { r - 4 } \leqslant x \leqslant \xi _ { r } \}$ and $\{ e _ { 2 h } ( x ) ; \xi _ { r } \leqslant x \leqslant \xi _ { r + 3 } \}$ The differences $\{ e ( x ) - e _ { h } ( x ) ; x \leqslant \xi _ { r } \}$ and $\{ e ( x ) - e _ { 2 h } ( x ) ; x \ge \xi _ { r } \}$ are similar to the tails of the cardinal function of Figure 18.2.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0004_pages_0211-0280/auto/images/7fbda3a09f149a594656ab153164f92a6fba11718b20318935ebec7f3102747c.jpg)  
Figure 21.1. The effect on the error of a change in step-length.

Therefore,assuming that the effects from the ends of the range $[ a , b ]$ can be neglected, there exist parameters $\pmb { \lambda }$ and $\pmb { \mu }$ such that the equation

$$
e ( x ) = \left\{ \begin{array} { l l } { e _ { h } ( x ) + \lambda \ \sigma ( [ \xi _ { r } - x ] / h ) , \quad } & { x \leqslant \xi _ { r } } \\ { e _ { 2 h } ( x ) + \mu \ \sigma ( [ x - \xi _ { r } ] / 2 h ) , \quad } & { x \geqslant \xi _ { r } , } \end{array} \right.
$$

holds, where $\pmb { \sigma }$ is the function

$$
\sigma ( x ) = x - \sqrt { 3 { x } ^ { 2 } + ( \sqrt { 3 } - 1 ) { x } ^ { 3 } + 2 \sqrt { 3 } \sum _ { j = 1 , 2 , . . . } ( \sqrt { 3 } - 2 ) ^ { j } ( x - j ) _ { + } ^ { 3 } } ,
$$

that is studied in Section 19.1. Because $e ^ { \prime }$ and $e ^ { \prime \prime }$ are continuous at $\boldsymbol { x } = \boldsymbol { \xi } _ { r } ,$ the conditions $\mu = - 2 \lambda$ and

$$
{ \textstyle \frac { 1 } { 1 2 } } h ^ { 2 } f ^ { ( 4 ) } ( \xi ) - 2 \sqrt { 3 \lambda / h ^ { 2 } } = { \textstyle \frac { 1 } { 3 } } h ^ { 2 } f ^ { ( 4 ) } ( \xi ) - { \textstyle \frac { 1 } { 2 } } \sqrt { 3 \mu / h ^ { 2 } }
$$

are satisfied, where $f ^ { ( 4 ) } ( \xi )$ is the constant fourth derivative of $f .$ It follows that the parameters have the values

$$
\left. \begin{array} { l } { \displaystyle \lambda = - \frac { h ^ { 4 } } { 1 2 \sqrt { 3 } } f ^ { ( 4 ) } ( \xi ) } \\ { \displaystyle \mu = \frac { h ^ { 4 } } { 6 \sqrt { 3 } } f ^ { ( 4 ) } ( \xi ) } \end{array} \right\} .
$$

It is now straightforward to obtain from expression (21.48) the third derivative discontinuities of $\pmb { s }$ , and the maximum value of $| f - s |$ on each of the intervals $\{ [ \xi _ { j } , \xi _ { j + 1 } ] ; j = r - 4 , r - 3 , \ldots , r + 2 \}$ .These numbers are given in Table 21.1.

The table shows that the expression

$$
\operatorname* { m a x } _ { \xi _ { q } \le x \le \xi _ { q + 1 } } | f ( x ) - s ( x ) | \approx \frac { ( \xi _ { q + 1 } - \xi _ { q } ) ^ { 3 } } { 3 8 4 } \operatorname* { m a x } \left[ | d _ { q } | , \left| d _ { q + 1 } \right| \right]
$$

Table 21.1. Errors and derivative discontinuities at a change in knot spacing   

<table><tr><td>j di max |f(x)-s(x)l j≤x≤5j+1</td></tr><tr><td>1.0052hf(() 0.0028h4f（4）（） r-4</td></tr><tr><td>0.9808hf（4（） 0.0021h4f(） r-3</td></tr><tr><td>1.0718hf() 0.0047h4f4（) r-2</td></tr><tr><td>0.7321hf（（） 0.0060hf（（） r-1</td></tr><tr><td>1.6585hf(（) 0.0571h4f（）（） r</td></tr><tr><td>2.0670hf（） 0.0376h4f（） r+1</td></tr><tr><td>r+2 1.9821hf(） 0.0428h4f（4）() r+3 2.0048hf（(）</td></tr><tr><td></td></tr></table>

overestimates the error when $q = r - 3$ and $r + 1$ , and it underestimates the error when $q = r - 4 , r - 2 , r - 1$ ， $r$ and $r + 2$ ,by $7 \%$ ， $4 1 \%$ ， $2 8 \%$ ， $2 5 \%$ and 22% respectively. The discrepancies for q<r do not matter very much because they occur in errors that are much smaller then the errors when $q \geqslant r .$ The $2 \%$ discrepancy can usually be ignored,but a modification is needed when $q = r .$ The table suggests that the approximation

$$
\begin{array} { r l r } {  { \operatorname* { m a x } _ { k \to s \in \xi _ { r + 1 } } \big | f ( x ) - s ( x ) \big | } } \\ & { } & { \approx \frac { ( \xi _ { r + 1 } - \xi _ { r } ) ^ { 3 } } { 3 8 4 } \operatorname* { m a x } [ 1 . 6 5 | d _ { r } | , | d _ { r + 1 } | ] } \end{array}
$$

is suitable.Moreover,in order to avoid the possibility that the error estimate predicts incorrectly that the interval $[ \xi _ { r - 1 } , \xi _ { r } ]$ is too long, it is advisable to delete the term $| d _ { q + 1 } |$ from expression (21.52) when $q = r - 1$ .

These ideas give an automatic method of estimating the local error of an interpolating cubic spline approximation to a function $f ,$ provided that, where the knot spacing changes, it only halves or doubles,and provided that each new knot spacing is used for several consecutive intervals.The error estimate is usually adequate when $f$ is a general function,even though the analysis is based on the assumption that $f$ is a quartic polynomial. If it is applied to a trial cubic spline approximation, then the estimate indicates the parts of the range $[ a , b ]$ where the accuracy is insufficient. By reducing the knot spacing only in these parts of the range, the spacing between knots can be adapted automatically to the form of $f .$ Hence a general algorithm has been developed for solving the problem that is stated at the beginning of this section. The algorithm begins by calculating an interpolating cubic spline that has a few equally spaced knots in $[ a , b ]$ .This spline is the first of a sequence of trial approximations.If it is predicted that a trial approximation is not sufficiently accurate, then the knot spacing is halved where the error is too large,and a new trial spline is calculated. The procedure finishes when the error estimate indicates that the required accuracy is achieved. Two features that are worth including in the algorithm are to insert extra knots only in the parts of the range $[ a , b ]$ where it is predicted that the error of the current trial approximation is within one-sixteenth of its maximum value, and to allow for an effect that is shown in Figure 21.1, namely that in the interval $[ \xi _ { r } , \xi _ { r + 1 } ]$ the error given by the solid line is about 1.4 times larger than the error shown by the dashed line. This increase in error is due to the change in interval length at $\xi _ { r }$ . Many trial approximations can be saved sometimes by anticipating this effect when the algorithm chooses the intervals in which to place new knots.

# 21 Exercises

21.1 If a linear spline approximation $\pmb { s }$ to a function $f$ in $\mathcal { C } ^ { ( 2 ) } [ a , b ]$ satisfies the condition $\| f - s \| _ { \infty } \leqslant \varepsilon$ and if $\pmb { s }$ interpolates $f$ at the knots,then Theorem 4.2 shows that, in a neighbourhood of a point $x$ of $[ a , b ] _ { \mathrm { : } }$ ,the knot spacing $^ { h }$ is at most about $\left| 8 \varepsilon / f ^ { \prime \prime } ( x ) \right| ^ { \frac { 1 } { 2 } }$ . This remark suggests the density of knots that is needed to approximate a given function to prescribed accuracy. Hence estimate the minimum number of knots that are necessary to achieve the condition $\| f - s \| _ { \infty } \leqslant \varepsilon$ when $f$ is the function $\{ f ( x ) =$ $x ^ { \mu } ; 0 \leqslant x \leqslant 1 \}$ where the constant $\pmb { \mu }$ is greater than two. Show that, if the knot spacing has to be constant, then the number of knots increases by a factor of about ${ \scriptstyle { \frac { 1 } { 2 } } } \mu$

21.2 Apply the interpolation method of Theorem 21.2 to calculate a spline approximation from the space $\mathcal { S } ( 2 , 0 , \frac { 1 } { 6 4 } , \frac { 8 } { 6 4 } , \frac { 2 7 } { 6 4 } , 1 )$ to the function $\dot { \{ f ( x ) = x ^ { \frac { 3 } { 2 } } } $ ； $0 \leqslant x \leqslant 1 \}$ . You should find that the maximum error at a knot is equal to O.000 254.

21.3 Let $\mathcal { S } _ { \epsilon }$ be the space of cubic splines on the infinite range $( - \infty , \infty )$ that have knots at the points $\{ \xi _ { 3 j } = j h$ ， $\xi _ { 3 j - 1 } = j h - \varepsilon$ ， $\xi _ { 3 j + 1 } =$ $j h + \varepsilon ; j = 0 , \pm 1 , \pm 2 , . . . \} ,$ ，where $h$ is a positive constant, and where $\varepsilon$ is a positive parameter that is less than $^ { \frac { 1 } { 2 } h }$ For any $f$ in $\mathcal { C } ( - \infty , \infty )$ ,let $\pmb { S } _ { \epsilon }$ be the bounded spline in $\mathcal { S } _ { \epsilon }$ that interpolates $f$ at the points $\begin{array} { r } { \{ x _ { i } = \frac { 1 } { 3 } ( \xi _ { i - 1 } + \xi _ { i } + \xi _ { i + 1 } ) } \end{array}$ ； $i = 0 , \pm 1 , \pm 2 , \ldots \}$ Prove that, as $\varepsilon$ tends to zero, $\pmb { S } _ { \pmb { \epsilon } }$ tends to the function $s ^ { * }$ that, on each of the intervals $\{ [ j h , j h + h ] ; j = 0 , \pm 1 , \pm 2 , . . . \}$ ，is the cubic polynomial that is defined by the interpolation conditions $\{ s ^ { * } ( j h + { \textstyle \frac { 1 } { 3 } } l h ) = f ( j h + { \textstyle \frac { 1 } { 3 } } l h ) ; l = 0 , 1 , 2 , 3 \} .$

21.4 Let $\pmb { \mathscr { s } }$ be the cubic spline that interpolates the function $\{ f ( { \pmb x } ) =$ $| x | ; - \infty < x < \infty \}$ at the knots $\{ \xi _ { j } = j h ; j = 0 , \pm 1 , \pm 2 , \ldots \}$ Show that the error estimate (21.46) underestimates the error in the interval $[ \xi _ { 0 } , \xi _ { 1 } ]$ by a factor of about 7.4.

21.5 Let the knots of a cubic spline $\pmb { s }$ on $( - \infty , \infty )$ have the values $\{ \xi _ { j } = j h ; j \ge 0 \}$ and $\{ \xi _ { j } = j \eta h ; j \leqslant 0 \}$ ，where $\eta$ is a small positive constant. Prove that, if $\pmb { s }$ is the bounded spline that satisfies the cardinality conditions $\{ s ( \xi _ { j } ) = \delta _ { j 0 } ; j = 0 , \pm 1 , \pm 2 , . . . \} ,$ ， then there is no upper bound on $\| \pmb { s } \| _ { \infty }$ that is independent of $\pmb { \eta }$

21.6 Let $f$ be a function in $\mathcal { C } ^ { ( 2 ) } [ a , b ]$ such that the derivative $\{ f ^ { \prime \prime } ( x ) ; a \leqslant x \leqslant b \}$ has no zeros. For any small positive number $\varepsilon$ let $\pmb { s }$ be a linear spline with fewest knots that gives the accuracy $\| f - s \| _ { \infty } \leqslant \varepsilon$ ， subject to the condition that $\pmb { s }$ interpolates $f$ at its knots. Investigate the positions of the knots of s $\{ \xi _ { j } [ \varepsilon ] ; j =$ $0 , 1 , \dots , n [ \varepsilon ] \}$ say,in the limit as $\pmb \varepsilon$ tends to zero. You should find that asymptotically $\xi _ { j } [ \varepsilon ]$ has the value $\phi ( j / n [ \varepsilon ] )$ ，where $\left\{ \phi ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ is the monotonically increasing differentiable function that satisfies the equations $\phi ( 0 ) = a$ ， $\phi ( 1 ) = b$ ,and

$$
[ \phi ^ { \prime } ( \theta ) ] ^ { 2 } f ^ { \prime \prime } [ \phi \left( \theta \right) ] = \mathrm { c o n s t a n t } , \qquad 0 \leqslant \theta \leqslant 1 .
$$

21.7 Use Exercise 21.6 to explain why the knots (21.6) are particularly suitable for the approximation of the function $\{ f ( { \pmb x } ) =$ $x ^ { \frac { 1 } { 2 } }$ ； $0 \leqslant x \leqslant 1 \}$ by a linear spline. Similarly，find good knot positions for the approximation of the function $\{ f ( x ) = x ^ { \mu }$ ； $0 \leqslant x \leqslant 1 \}$ ,where $\pmb { \mu }$ is a constant in (O,1),and bound the number of knots that are needed to achieve a given accuracy.

21.8 Apply the method that gives the error estimate (21.46) to deduce that, if $\pmb { s }$ is a quadratic spline with equally spaced knots $\{ \xi _ { j } = j h \}$ ， that interpolates a function $f$ at the points that are midway between the knots, then the error estimate

$$
\operatorname* { m a x } _ { \xi _ { q } \le x \le \xi _ { q + 1 } } \big | f ( x ) - s ( x ) \big | \approx \frac { h ^ { 2 } } { 7 2 \sqrt { 3 } } \operatorname* { m a x } \left[ \big | d _ { q } \big | , \big | d _ { q + 1 } \big | \right]
$$

is appropriate, where $d _ { q }$ is the second derivative discontinuity of $\pmb { s }$ at $\xi _ { q }$

21.9 Let $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ be the space that is defned in the last paragraph of Section 21.1, where inequality (21.17) holds.Let $\pmb { s }$ be any fixed function in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ ,and let $\pmb \varepsilon$ be any pos-itive constant.Prove thatthereexists apositive number $\pmb { \delta }$ suchthat, if $\{ \eta _ { j } ; j = 0 , 1 , \dotsc , n \}$ is any set of numbers that satisfies the conditions $\{ \vert \eta _ { j } - \xi _ { j } \vert \leqslant \delta$ ； $j = 0 , 1 , \ldots , n \}$ and $a = \eta _ { 0 } < \eta _ { 1 } < \eta _ { 2 } < . ~ . ~ .$ $< \eta _ { n } = b$ ，then there is a function, $\pmb { \sigma }$ say，in the space $\mathcal { S } ( k , \eta _ { 0 } , \eta _ { 1 } , \dots , \eta _ { n } )$ such that $\| s - \sigma \| _ { \infty }$ is less than $\pmb \varepsilon$

21.10 Extend the definition of $\pmb { B }$ -splines and the four theorems of Chapter 19 to the case when $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ is the extended space of splines that is defined in the last paragraph of Section 21.1.

#

# The Peano kernel theorem

# 22.1 The error of a formula for the solution of differential equations

The Peano kernel theorem gives a general and highly useful technique for expressing the errors of approximations in terms of derivatives of the underlying function of the approximation. For example, let the coefficients $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ and the points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ be such that the quadrature rule

$$
\int _ { a } ^ { b } f ( x ) \mathrm { d } x \approx \sum _ { t = 1 } ^ { m } w _ { t } f ( x _ { t } )
$$

is exact when $f$ is in $\mathcal { P } _ { k }$ ，where the points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ are all in $[ a , b ]$ .The theorem defines a function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ , that is independent of $f ,$ such that the equation

$$
\int _ { a } ^ { b } f ( x ) \mathrm { d } x - \sum _ { t = 1 } ^ { m } w _ { t } f ( x _ { t } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta
$$

holds for all functions $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ . One useful consequence of this equation is that the error of the approximation (22.1) is bounded above by $c \| f ^ { ( k + 1 ) } \| _ { \infty }$ ,where $c$ is the number

$$
c = \int _ { a } ^ { b } \left| K ( \theta ) \right| \mathrm { d } \theta .
$$

Because $c$ is independent of $f ,$ it provides a convenient measure of the accuracy of formula (22.1), that may be useful to a comparison of integration methods.

In order to introduce the theorem，we consider the problem of expressing the error of the formula

$$
f ( x _ { t } + 2 h ) \approx f ( x _ { t } + h ) + h \big [ \frac { 3 } { 2 } f ^ { \prime } ( x _ { t } + h ) - \frac { 1 } { 2 } f ^ { \prime } ( x _ { t } ) \big ]
$$

in terms of the third derivative of $f .$ This formula is a standard technique for the step-by-step solution of ordinary differential equations. We solve the problem by making use of the Taylor series. In Section 22.2 the method of solution is generalized, which gives the Peano kernel theorem. The remainder of the chapter describes some applications of the theorem.

The simplest way of estimating the error

$$
L ( f ) = f ( x _ { t } + 2 h ) - f ( x _ { t } + h ) - h [ \frac { 3 } { 2 } f ^ { \prime } ( x _ { t } + h ) - \frac { 1 } { 2 } f ^ { \prime } ( x _ { t } ) ] ,
$$

when $f$ is suficiently differentiable, is to make the Taylor series approximations

$$
\left. { \begin{array} { l } { f ( x _ { t } + 2 h ) = f ( x _ { t } ) + 2 h f ^ { \prime } ( x _ { t } ) + 2 h ^ { 2 } f ^ { \prime \prime } ( x _ { t } ) + { \frac { 4 } { 3 } } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { t } ) + \dots } \\ { f ( x _ { t } + h ) = f ( x _ { t } ) + h f ^ { \prime } ( x _ { t } ) + { \frac { 1 } { 2 } } h ^ { 2 } f ^ { \prime \prime } ( x _ { t } ) + { \frac { 1 } { 6 } } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { t } ) + \dots } \\ { f ^ { \prime } ( x _ { t } + h ) = f ^ { \prime } ( x _ { t } ) + h f ^ { \prime \prime } ( x _ { t } ) + { \frac { 1 } { 2 } } h ^ { 2 } f ^ { \prime \prime \prime } ( x _ { t } ) + \dots } \end{array} } \right\} ,
$$

ignoring the higher order terms that are represented by‘...'.By substituting expression (22.6) in equation (22.5) we obtain the estimate

$$
\begin{array} { r } { L ( f ) \approx \frac { 5 } { 1 2 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { t } ) . } \end{array}
$$

It is better, however, to use the Taylor series with explicit remainder, because then the exact value of $L ( f )$ is found. We express $f ( x _ { t } + h )$ ,for example,in the form

$$
\begin{array} { l } { f ( x _ { t } + h ) = f ( x _ { t } ) + h f ^ { \prime } ( x _ { t } ) + \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { t } ) } \\ { \qquad + \frac { 1 } { 2 } \displaystyle \int _ { x _ { t } } ^ { x _ { t } + h } \left( x _ { t } + h - \theta \right) ^ { 2 } f ^ { \prime \prime \prime } ( \theta ) \ : \mathrm { d } \theta . } \end{array}
$$

Hence equation (22.5) implies the identity

$$
\begin{array} { r l } & { L ( f ) = \frac { 1 } { 2 } \displaystyle \int _ { x _ { t } } ^ { x _ { t } + 2 h } \left( x _ { t } + 2 h - \theta \right) ^ { 2 } f ^ { \prime \prime } ( \theta ) \mathrm { d } \theta } \\ & { \quad \quad \quad - \frac { 1 } { 2 } \displaystyle \int _ { x _ { t } } ^ { x _ { t } + h } \left( x _ { t } + h - \theta \right) ^ { 2 } f ^ { \prime \prime } ( \theta ) \mathrm { d } \theta } \\ & { \quad \quad \quad - \frac { 3 } { 2 } h \displaystyle \int _ { x _ { t } } ^ { x _ { t } + h } \left( x _ { t } + h - \theta \right) f ^ { \prime \prime } ( \theta ) \mathrm { d } \theta } \\ & { \quad \quad \quad = \displaystyle \int _ { x _ { t } } ^ { x _ { t } + 2 h } K ( \theta ) f ^ { \prime \prime \prime } ( \theta ) \mathrm { d } \theta , } \end{array}
$$

where $\pmb { K } ( \pmb \theta )$ has the value

$$
\begin{array} { r } { K ( \theta ) = \Big \{ \frac { 1 } { 2 } h \big ( \theta - x _ { t } \big ) , \qquad x _ { t } \leqslant \theta \leqslant x _ { t } + h } \\ { \frac 1 2 \big ( x _ { t } + 2 h - \theta \big ) ^ { 2 } , \qquad x _ { t } + h \leqslant \theta \leqslant x _ { t } + 2 h . } \end{array}
$$


<!-- chunk 0005: pages 281-350 -->
Because the function $\{ K ( \theta ) ; x _ { t } \leqslant \theta \leqslant x _ { t } + 2 h \}$ does not change sign, the mean value theorem gives the equation

$$
\begin{array} { c } { { { \displaystyle { \cal L } ( f ) = f ^ { \prime \prime \prime } ( \xi ) \int _ { x _ { t } } ^ { x _ { t } + 2 h } K ( \theta ) \mathrm { d } \theta } } } \\ { { { = \frac { 5 } { 1 2 } h ^ { 3 } f ^ { \prime \prime \prime } ( \xi ) , } } } \end{array}
$$

where $\xi$ is a point in the interval $[ x _ { t } , x _ { t } + 2 h ]$ .This result is stronger than the approximation (22.7).

# 22.2 The Peano kernel theorem

The notation $L ( f )$ is used in equation (22.5), because the righthand side is a linear functional of $f .$ We let $L$ be a general linear functional such that $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k }$ If $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ we write it in the form

$$
f ( x ) = \sum _ { j = 0 } ^ { k } { \frac { ( x - a ) ^ { j } } { j ! } } f ^ { ( j ) } ( a ) + { \frac { 1 } { k ! } } \int _ { a } ^ { x } { ( x - \theta ) ^ { k } } f ^ { ( k + 1 ) } ( \theta ) { \mathrm { d } } \theta ,
$$

$$
a \leqslant x \leqslant b .
$$

When $L$ is applied to this equation, the contribution from the sum on the right-hand side is zero. Hence $L f$ is expressed in terms of $f ^ { ( k + 1 ) }$

The Peano kernel theorem states a useful form of this construction. It depends on a function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ that is defined in the following way. For any value of $\pmb \theta _ { \mathrm { i } }$ ， which in fact need not be in $[ a , b ] ,$ we let $\bullet _ { \pmb { \theta } }$ be the function

$$
\begin{array} { r } { s _ { \theta } ( x ) = ( x - \theta ) _ { + } ^ { k } , \qquad a \leqslant x \leqslant b . } \end{array}
$$

The number $\pmb { K } ( \pmb \theta )$ is obtained by applying the operator $L$ to the function $s _ { \theta } / k !$ , which gives the value

$$
K ( \theta ) = { \frac { 1 } { k ! } } L ( s _ { \theta } ) , \qquad a \leqslant \theta \leqslant b .
$$

It is convenient to introduce a notation that allows expressions (22.13) and (22.14) to be combined. Therefore we write the equation

$$
K ( \theta ) = \frac { 1 } { k ! } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} , \qquad a \leqslant \theta \leqslant b ,
$$

where the notation $L _ { x } \{ \dots \}$ indicates that the expression in the braces is to be regarded as a function of $x$ on which $L$ operates.

Because it is sometimes useful to let $k = 0$ in equation (22.15),it may be necessary for $L ( f )$ to be defined when $f$ is in the space $\mathcal { V } [ a , b ] ,$ ，which is the space of real-valued functions on $[ a , b ]$ that are of bounded variation.

This condition is assumed in the next theorem, and it is assumed also that $L$ is bounded, which means that there is a constant $\| L \| _ { \infty }$ such that the inequality

$$
\begin{array} { r } { \left| L ( f ) \right| \leqslant \left\| L \right\| _ { \infty } \left\| f \right\| _ { \infty } , \qquad f \in \mathcal { V } [ a , b ] , } \end{array}
$$

holds, where $\| f \| _ { \infty }$ is the norm

$$
\| f \| _ { \infty } = \operatorname* { s u p } _ { a \leqslant x \leqslant b } { \big | } f ( x ) { \big | } , \qquad f \in { \mathcal { V } } [ a , b ] .
$$

These conditions on $L$ ，however，are too restrictive for general use, because they do not allow $L$ to depend on derivatives. Therefore another version of the Peano kernel theorem is given later.

# Theorem 22.1 (Peano kernel)

Let $k$ be any non-negative integer,and let $L$ be a bounded linear functional from $\mathcal { V } [ a , b ]$ to ${ \mathcal { R } } ^ { 1 }$ , such that $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k }$ ,and such that the function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ ，which is defined by equation (22.15), is of bounded variation.Then, f $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ , the functional $L ( f )$ has the value

$$
L ( f ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta .
$$

Proof.By applying $L$ to expression (22.12) we obtain the equation

$$
L ( f ) = { \frac { 1 } { k ! } } L _ { x } { \Big \{ } { \int _ { a } ^ { b } ( x - \theta ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta { \Big \} } } .
$$

Therefore it is sufficient to show that the operator $L _ { x }$ can be exchanged with the integration sign. The bounded variation conditions in the statement of the theorem, and also the fact that the variation of the function $\left\{ ( x - \theta ) _ { + } ^ { k } \right.$ ； $a \leqslant \theta \leqslant b \}$ is uniformly bounded for all $x$ in $[ a , b ] ,$ are needed in order to approximate integrals by Reimann sums. Thus,for any $\varepsilon > 0$ ，there exist points $\{ \theta _ { t } ; t = 1 , 2 , \ldots , m \}$ in $[ a , b ]$ such that the expression

$$
\bigg \vert \int _ { a } ^ { b } { ( x - \theta ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta } - \frac { ( b - a ) } { m } \sum _ { t = 1 } ^ { m } { ( x - \theta _ { t } ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta _ { t } ) } \bigg \vert = \eta ( x ) ,
$$

say, is less than $\pmb \varepsilon$ for all $x$ in $[ a , b ] ,$ , and such that the inequality

$$
\bigg | \displaystyle \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) { \bf d } \theta - \frac { ( b - a ) } { m } \sum _ { t = 1 } ^ { m } K ( \theta _ { t } ) f ^ { ( k + 1 ) } ( \theta _ { t } ) \bigg | \leqslant \varepsilon
$$

holds.Because the linearity of $L$ and the definition (22.15） give the identity

$$
\begin{array} { c } { { { \displaystyle { \cal L } _ { x } \bigg \{ \sum _ { t = 1 } ^ { m } ( x - \theta _ { t } ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta _ { t } ) \bigg \} = \sum _ { t = 1 } ^ { m } { \cal L } _ { x } \{ ( x - \theta _ { t } ) _ { + } ^ { k } \} f ^ { ( k + 1 ) } ( \theta _ { t } ) } } } \\ { { { = k ! \sum _ { t = 1 } ^ { m } K ( \theta _ { t } ) f ^ { ( k + 1 ) } ( \theta _ { t } ) , } } } \end{array}
$$

it follows from the accuracy of the Riemann sums that, if the equation

$$
L _ { x } { \Big \{ } \int _ { a } ^ { b } { ( x - \theta ) _ { + } ^ { k } f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta } { \Big \} } = k ! \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta
$$

is not satisfied, then the difference between the two sides is bounded by the number

$$
\left| L _ { x } \{ \eta ( x ) \} \right| + k ! \varepsilon \leqslant ( \| L \| _ { \infty } + k ! ) \varepsilon .
$$

Since $\pmb \varepsilon$ can be arbitrarily small, equation (22.23) is valid.It follows from expression (22.19) that $L ( f )$ does have the value (22.18),which is the required result.□

This theorem gives useful expressions for the errors of many inter-polation and integration procedures. We have noted, however, that if $L$ depends on some derivatives of $f ,$ which is the case in example (22.5),and which is usual when one analyses the local truncation errors of linear multistep methods for solving ordinary differential equations, then $L$ is nct bounded, nor is it a mapping from ${ \mathcal { W } } [ a , b ]$ to ${ \mathcal { R } } ^ { 1 }$ . A suitable extension to Theorem 22.1 can be obtained by expressing $L ( f )$ in terms of a derivative of $f .$ For example, we can write equation (22.5) in the form

$$
\begin{array} { l } { { \displaystyle { \cal L } ( f ) = \int _ { x _ { t } + h } ^ { x _ { t } + 2 h } f ^ { \prime } ( x ) \mathrm { d } x - h \big [ \frac { 3 } { 2 } f ^ { \prime } ( x _ { t } + h ) - \frac { 1 } { 2 } f ^ { \prime } ( x _ { t } ) \big ] } } \\ { { \displaystyle ~ = M ( f ^ { \prime } ) , } } \end{array}
$$

say. It is important to notice that the linear operator $M$ is bounded, even though $L$ is not. Therefore it is valid to replace $L$ by $M$ and $f$ by $f ^ { \prime }$ in the statement of Theorem 22.1.Thus $\begin{array} { r } { M ( f ^ { \prime } ) = L ( f ) } \end{array}$ can be expressed in terms of $f ^ { \prime \prime }$ ，where $f$ is any function in $\mathcal { C } ^ { ( 3 ) } [ a , b ]$

This technique applies generally to operators $L$ that have the form

$$
L ( f ) = M ( f ^ { ( j ) } ) , \qquad f \in \mathcal { V } ^ { ( j ) } [ a , b ] ,
$$

where $\mathcal { V } ^ { ( j ) } [ a , b ]$ is the linear space of functions whose jth derivatives are of bounded variation, and where $M$ is a bounded linear operator from $\mathcal { V } [ a , b ]$ to ${ \mathcal { R } } ^ { 1 }$ . The generalization is given in the following theorem.

# Theorem 22.2

Let $L$ be the operator (22.26), where $M$ satisfies the conditions that have just been stated,and let $k$ be any integer that is greater than or equal to $j .$ If $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k } ,$ ,and if the function (22.15) is of bounded variation, then,for all functions $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ ，the linear functional $L ( f )$ has the value that is given in Theorem 22.1.

Proof. Equations (22.15) and (22.26) give the relation

$$
\begin{array} { l } { { \displaystyle { K ( \theta ) = \frac { 1 } { k ! } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} } } } \\ { { \displaystyle { \ = \frac { 1 } { ( k - j ) ! } M _ { x } \{ ( x - \theta ) _ { + } ^ { k - j } \} , \qquad a \leqslant \theta \leqslant b . } } } \end{array}
$$

Because,by hypothesis, this function is of bounded variation,and because of the conditions that are satisfied by $M ,$ we may replace $L$ by $M , f$ $\boldsymbol { \mathsf { b y } } \boldsymbol { f } ^ { ( i ) }$ and $\pmb { k }$ by $( k - j )$ in the statement of Theorem 22.1. Hence we obtain the value

$$
M ( f ^ { ( j ) } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] .
$$

It follows from equation (22.26) that the theorem is true.□

The refinements of bounded variation and the differences between Theorems 22.1 and 22.2 are usually ignored in practice. The standard way of applying the Peano kernel theorem is to check first that $L$ is a linear operator, that $L ( f )$ is zero if $f$ is any polynomial of degree $k$ and that $L$ does not depend on any derivatives of degree greater than $\pmb { k }$ If these conditions hold, then $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ is calculated from equation (22.15). This function,which is called the ‘kernel function',is substituted into equation (22.18). Thus $L ( f )$ is expressed in terms of the derivative $\{ f ^ { ( k + 1 ) } ( \pmb { \theta } ) ; a \leqslant \pmb { \theta } \leqslant b \}$

There is a neat way of verifying that the condition

$$
L ( f ) = 0 , \qquad f \in \mathcal { P } _ { k } ,
$$

holds. It is the reason for the remark, made immediately before equation (22.13), that the value of $\pmb \theta$ need not be in the range $[ a , b ]$ .We consider the definition

$$
K ( \theta ) = \frac { 1 } { k ! } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} , \qquad - \infty < \theta < \infty .
$$

If $\theta < a$ , then the function $\left\{ ( { \pmb x } - { \pmb \theta } ) _ { + } ^ { k } \right.$ ； $a \leqslant x \leqslant b \}$ is in $\mathcal { P } _ { k } ,$ and, if $\pmb \theta > b$ ,then

it is the zero function. Hence the equations

$$
\left. \begin{array} { c } { { K ( \theta ) = 0 , \theta < a } } \\ { { K ( \theta ) = 0 , \theta > b } } \end{array} \right\}
$$

should be obtained. Because the space $\mathcal { P } _ { k }$ is spanned by the polynomials $\{ ( x - \theta _ { t } ) ^ { k } ; - \infty < x < \infty ; t = 0 , 1 , \ldots , k \}$ ,where $\left\{ \theta _ { t } ; t = 0 , 1 , \ldots , k \right\}$ is any set of distinct real numbers that are less than $^ { a }$ ,the first line of expression (22.31) is both a necessary and a sufficient condition for $L ( f )$ to be zero when $f$ is in $\mathcal { P } _ { k }$

When $k = 2$ ,and when $L$ is the functional (22.5), the definition (22.30) is the equation

$$
\begin{array} { r } { K ( \theta ) = \frac { 1 } { 2 } \{ ( x _ { t } + 2 h - \theta ) _ { + } ^ { 2 } - ( x _ { t } + h - \theta ) _ { + } ^ { 2 } \quad } \\ { - h [ 3 ( x _ { t } + h - \theta ) _ { + } - ( x _ { t } - \theta ) _ { + } ] \} , ~ - \infty < \theta < \infty . } \end{array}
$$

It is straightforward to verify that $\pmb { K } ( \pmb \theta )$ is zero when $\pmb \theta$ is less than $\boldsymbol { x } _ { t } .$ If $\pmb \theta$ is increased through the value $\pmb \theta = \pmb x _ { t } ,$ then the term $( x _ { t } - \theta ) _ { + }$ in expression (22.32) is the only one that causes a discontinuity in $\pmb { K } ( \pmb \theta )$ . This remark is useful, because it provides a convenient way of calculating the first line of equation (22.10).

# 22.3 Application to divided differences and to polynomial interpolation

Theorem 5.1 states that, if $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ , then the divided difference $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ]$ is equal to $f ^ { ( k + 1 ) } ( \xi ) / ( k + 1 ) !$ for some number $\xi .$ Hence $f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ]$ is zero when $f$ is in $\mathcal { P } _ { k }$ It follows from Theorem 22.1 that the following useful and interesting relation is obtained between divided differences and $\pmb { B }$ -splines.

# Theorem 22.3

f $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ and if $\{ x _ { i } ; i = 0 , 1 , \ldots , k + 1 \}$ is a set of distinct points in $[ a , b ] ,$ , then the equation

$$
f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k + 1 } ] { = } { \frac { 1 } { k ! } } \int _ { a } ^ { b } B ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta
$$

is satisfied, where $\pmb { B }$ is the $\pmb { B }$ -spline

$$
B ( \theta ) = \sum _ { i = 0 } ^ { k + 1 } \bigg \{ ( \theta - x _ { i } ) _ { + } ^ { k } \bigg / \prod _ { { j = 0 } \atop { j \ne i } } ^ { k + 1 } ( x _ { j } - x _ { i } ) \bigg \} , \qquad a \leqslant \theta \leqslant b .
$$

Proof. By equation (5.2) the divided difference is the expression

$$
\begin{array} { c } { { f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ] = \displaystyle \sum _ { i = 0 } ^ { k + 1 } \left\{ f ( x _ { i } ) \Biggl / \prod _ { j = 0 \atop j \ne i } ^ { k + 1 } ( x _ { i } - x _ { j } ) \right\} } } \\ { { = { \cal L } ( f ) , } } \end{array}
$$

say. Therefore,for any fixed and distinct points $\{ x _ { i } ; i = 0 , 1 , \ldots , k + 1 \}$ ， $L$ is a bounded linear operator from $\mathcal { V } [ a , b ]$ to $\mathcal { R } ^ { 1 }$ , and the function (22.15） is of bounded variation. It follows from Theorem 22.1 that equation (22.18) is satisfied, where $\pmb { K } ( \pmb \theta )$ has the value

$$
K ( \theta ) = { \frac { 1 } { k ! } } \sum _ { i = 0 } ^ { k + 1 } \Big \{ ( x _ { i } - \theta ) _ { + } ^ { k } \Big / \prod _ { j = 0 \atop j \neq i } ^ { k + 1 } ( x _ { i } - x _ { j } ) \Big \} , \qquad a \leqslant \theta \leqslant b .
$$

Equation (22.18) shows that the required relation (22.33) is valid if and only if the function (22.34) is equal to $k ! K .$ We substitute the identity

$$
\left( x _ { i } - \theta \right) _ { + } ^ { k } = \left( x _ { i } - \theta \right) ^ { k } + \left( - 1 \right) ^ { k + 1 } \left( \theta - x _ { i } \right) _ { + } ^ { k }
$$

into expression (22.36) for $i = 0 , 1 , \ldots , k + 1$ ， which gives the equation

$$
K ( \theta ) = \frac { 1 } { k ! } [ L _ { x } \{ \left( x - \theta \right) ^ { k } \} + B ( \theta ) ] , \qquad a \leqslant \theta \leqslant b .
$$

The term $L _ { x } \{ { ( x - \theta ) } ^ { k } \}$ is zero,because the function $\{ ( x - \theta ) ^ { k } ; a \leqslant x \leqslant b \}$ is in $\mathcal { P } _ { k }$ .Therefore the theorem is true.□

This theorem is more general than Theorem 5.1, because equation (22.33) does not depend on the unknown number $\xi .$ Further,Theorem 5.1 can be deduced from Theorem 22.3 in the following way. We recall that $B$ -splines are non-negative. Therefore,by applying the mean value theorem to equation (22.33), the relation

$$
f [ x _ { 0 } , x _ { 1 } , \ldots , x _ { k + 1 } ] { = } \frac { 1 } { k ! } { \biggl [ } \int _ { a } ^ { b } B ( \theta ) \mathrm { d } \theta { \biggl ] } f ^ { ( k + 1 ) } ( \xi )
$$

is obtained, where $\pmb { \xi }$ is in the interval $[ a , b ]$ .Because this relation holds in the particular case when $f$ is the polynomial $\{ f ( x ) = x ^ { k + 1 }$ ； $a \leqslant x \leqslant b $ ,and because of the original definition of a divided difference, the integral of the $\pmb { B }$ -spline has the value

$$
\int _ { a } ^ { b } B ( \theta ) { \bf d } \theta = 1 / ( k + 1 ) .
$$

Hence Theorem 5.1 is true.

Theorem 22.3 is also useful to the main subject of Chapters 23 and 24, which is the problem of obtaining good approximations from the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ when $^ { m }$ is large.For example, we may have to choose the weights $\{ w _ { t } ; t = 1 , 2 , \dots , m \}$ in formula (22.1),and it may be suitable to force the approximation to be exact only when $f$ is a polynomial of degree $k$ ,where $k$ is much smaller than $_ m$ . In this case a suitable technique,for taking up the freedom in the weights, is to apply the Peano kernel theorem to express the error of the approximation in terms of the derivative $\{ f ^ { ( k + 1 ) } ( \theta ) ; a \leqslant \theta \leqslant b \}$ ,and then to use the freedom to make the kernel function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ small. It is convenient to write the approximation (22.1) in the form

$$
\int _ { a } ^ { b } f ( x ) \mathrm { d } x \approx \sum _ { t = 1 } ^ { k + 1 } u _ { t } f ( x _ { t } ) + \sum _ { t = 1 } ^ { m - k - 1 } v _ { t } f [ x _ { t } , x _ { t + 1 } , \ldots , x _ { t + k + 1 } ] ,
$$

because then the freedom in the weights allows arbitrary values of the parameters $\{ v _ { t } ; t = 1 , 2 , \ldots , m - k - 1 \}$ .Theorem 22.3 shows the change to the kernel function that is caused by adjustments to the parameters $\{ v _ { t } ; t = 1 , 2 , \ldots , m - k - 1 \} .$

This theorem also gives an expression for the error of polynomial interpolation. As in Theorem 5.2,we let $\{ p _ { k } ( x )$ ； $a \leqslant x \leqslant b $ be the polynomial in $\mathcal { P } _ { k }$ that satisfies the interpolation conditions

$$
p _ { k } ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 0 , 1 , \ldots , k ,
$$

and we let $x _ { k + 1 }$ be any point of $[ a , b ]$ that is not in the set $\{ x _ { i } ; i = 0$ ， $1 , \ldots , k \}$ . Because Theorem 5.2 implies the equation

$$
f ( x _ { k + 1 } ) = p _ { k } ( x _ { k + 1 } ) + \bigg \{ \prod _ { j = 0 } ^ { k } { \left( x _ { k + 1 } - x _ { j } \right) } \bigg \} f [ x _ { 0 } , x _ { 1 } , \dots , x _ { k + 1 } ] ,
$$

it follows from Theorem 22.3 that the difference $\{ f ( x _ { k + 1 } ) - p _ { k } ( x _ { k + 1 } ) \}$ has the value

$$
\begin{array} { c } { { f ( x _ { k + 1 } ) - p _ { k } ( x _ { k + 1 } ) = \displaystyle \frac { 1 } { k ! } \bigg \{ \prod _ { j = 0 } ^ { k } \left( x _ { k + 1 } - x _ { j } \right) \bigg \} \displaystyle \int _ { a } ^ { b } B ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta } } \\ { { = \displaystyle \frac { 1 } { ( k + 1 ) ! } \bigg \{ \prod _ { j = 0 } ^ { k } \left( x _ { k + 1 } - x _ { j } \right) \bigg \} f ^ { ( k + 1 ) } ( \xi ) , } } \\ { { \xi \in [ a , b ] , \qquad ( 2 } } \end{array}
$$

where the last line depends on the condition $\{ B ( \pmb \theta ) \geq 0$ ； $a \leqslant \theta \leqslant b \}$ , on the mean value theorem,and on equation (22.4O). Both lines of this expression are useful,and we see that the second one is the same as the statement of Theorem 4.2.

It is important to note that often the linear functional $L$ and the value of $k$ are such that the kernel function $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ of equation (22.18) changes sign. For example, the possibility that $L ( f )$ is zero when $f$ is in $\mathcal { P } _ { k + 1 }$ does not impair the validity of Theorem 22.1. If this possibility occurs, and if we let $f$ be the function $\{ f ( x ) = x ^ { k + 1 }$ ； $a \leqslant x \leqslant b \}$ ,then equation (22.18) implies the identity

$$
\int _ { a } ^ { b } K ( \theta ) { \bf d } \theta = 0 .
$$

In general, therefore, one should not expect the equation

$$
L ( f ) = \int _ { a } ^ { b } K ( \theta ) \mathrm { d } \theta f ^ { ( k + 1 ) } ( \xi )
$$

to be satisfied for some value of $\xi$ in $[ a , b ]$

# 22.4 Application to cubic spline interpolation

In order to show the usefulness of the Peano kernel theorem, it is applied in this section to bound the error of a cubic spline approximation that is defined by interpolation. We consider the procedure,described in Section 18.2, where the knots of the spline have the values

$$
x _ { j } = j h , \qquad j = 0 , \pm 1 , \pm 2 , \ldots ,
$$

and where the interpolation conditions are the equations

$$
s ( x _ { j } ) = f ( x _ { j } ) , \qquad j = 0 , \pm 1 , \pm 2 , . . . .
$$

We recall that $\pmb { s }$ can be expressed in the form

$$
s ( x ) = \sum _ { j = - \infty } ^ { \infty } l _ { j } ( x ) f ( x _ { j } ) , \qquad - \infty < x < \infty ,
$$

where the cardinal spline $\{ l _ { j } ( x ) ; - \infty < x < \infty \}$ is symmetric about $\boldsymbol { x } = \boldsymbol { x } _ { j } ,$ and has the properties that are shown in Figure 18.2.In particular, the fact that the tails of the cardinal function reduce by the factor $( { \sqrt { 3 } } - 2 )$ per knot gives the conditions

$$
\begin{array} { r l r l } & { l _ { j } ( x - h ) = ( \sqrt { 3 } - 2 ) l _ { j } ( x ) , } & & { x \leqslant x _ { j - 1 } } \\ & { l _ { j } ( x + h ) = ( \sqrt { 3 } - 2 ) l _ { j } ( x ) , } & & { x \geqslant x _ { j + 1 } } \end{array} \bigg \} .
$$

Because the Peano kernel theorem concerns linear functionals,we study the error of the interpolation procedure for a particular value of the variable $\pmb { x } .$ .Therefore we let $L$ be the functional

$$
\begin{array} { l } { { \displaystyle { \cal L } ( f ) = f ( \xi ) - s ( \xi ) } } \\ { { \displaystyle ~ = f ( \xi ) - \sum _ { j = - \infty } ^ { \infty } l _ { j } ( \xi ) f ( x _ { j } ) , } } \end{array}
$$

where $\xi$ is a fixed real number,which, for convenience, is chosen in the interval $[ 0 , h ]$ . Although the range of the variable is infinite, it is assumed that the Peano kernel theorem can be applied.Hence, if $f$ is in $\mathcal { C } ^ { ( 4 ) } ( - \infty , \infty )$ , then the equation

$$
f ( \xi ) - s ( \xi ) = \int _ { - \infty } ^ { \infty } K ( \theta ) f ^ { ( 4 ) } ( \theta ) { \bf d } \theta
$$

is satisfied, where $\pmb { K }$ is the function

$$
K ( \theta ) = \frac { 1 } { 3 ! } \biggl [ ( \xi - \theta ) _ { + } ^ { 3 } - \sum _ { j = - \infty } ^ { \infty } l _ { j } ( \xi ) ( x _ { j } - \theta ) _ { + } ^ { 3 } \biggr ] , \qquad - \infty < \theta < \infty .
$$

We derive some properties of this kernel function,in order to obtain bounds on the error (22.52).

First it is proved that the form of $\{ K ( \theta ) ; - \infty < \theta < \infty \}$ is similar to the form of a cardinal function when $| \pmb \theta |$ is large.Because the behaviour of the cardinal functions that gives expression (22.50) also implies the equation

$$
l _ { j } ( \xi ) = ( \surd 3 - 2 ) l _ { j - 1 } ( \xi ) , \qquad j \geq 3 ,
$$

it follows from the definition (22.53) that, for $\pmb \theta \geqslant x _ { 1 }$ ,the relation

$$
\begin{array} { l } { { \displaystyle K ( \theta + h ) = - \frac { 1 } { 6 } \sum _ { j = 3 } ^ { \infty } l _ { j } ( \xi ) ( x _ { j } - \theta - h ) _ { + } ^ { 3 } } } \\ { { \displaystyle \quad = - \frac { 1 } { 6 } ( \surd 3 - 2 ) \sum _ { j = 3 } ^ { \infty } l _ { j - 1 } ( \xi ) ( x _ { j - 1 } - \theta ) _ { + } ^ { 3 } } } \\ { { \displaystyle \quad = ( \surd 3 - 2 ) K ( \theta ) } } \end{array}
$$

is obtained.A remarkable result can now be deduced from the fact that, if $p$ is any cubic polynomial, then the identity

$$
\begin{array} { c } { { 1 2 [ p ( x _ { j + 1 } ) - p ( x _ { j } ) ] = ( 6 + 2 \sqrt { 3 } ) h [ p ^ { \prime } ( x _ { j + 1 } ) - ( \sqrt { 3 } - 2 ) p ^ { \prime } ( x _ { j } ) ] } } \\ { { - ( \sqrt { 3 } + 1 ) h ^ { 2 } [ p ^ { \prime \prime } ( x _ { j + 1 } ) - ( \sqrt { 3 } - 2 ) p ^ { \prime \prime } ( x _ { j } ) ] } } \end{array}
$$

holds. We let $j$ be any positive integer, and we let $p$ be the polynomial $\left\{ K ( \theta ) \right.$ ； $x _ { j } \leqslant \theta \leqslant x _ { j + 1 } \}$ . Because equation (22.55） implies that the righthand side of expression (22.56) is zero, the numbers $K ( x _ { j } )$ and $\pmb { K } ( \pmb { x } _ { j + 1 } )$ are equal. However, condition (22.55) has to hold when $\theta = x _ { j } .$ Hence the equations

$$
K ( x _ { j } ) = 0 , \qquad j = 1 , 2 , 3 , \ldots ,
$$

Figure 22.1.A kernel function for cubic spline interpolation.

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0005_pages_0281-0350/auto/images/50f54a38e1151941cf9b02c59ec64e93fdd752637049dc340e23e98115b23cdb.jpg)

are satisfied. By symmetry, or by applying the technique that depends on expression (22.37) in the proof of Theorem 22.3,we also deduce the conditions $\{ K ( x _ { j } ) = 0 ; j = 0 , - 1 , - 2 , . . . \}$ and $\left\{ K ( \theta - h ) = ( \sqrt { 3 } - 2 ) K ( \theta ) \right.$ $\theta \leqslant x _ { 0 } \}$ . These properties are displayed in Figure 22.1, but the form of $\kappa$ in the interval $[ 0 , h ]$ requires further analysis.

Equation (22.53)and the figure imply that there exist parameters $\lambda , \mu$ and $^ d$ such that $\pmb { K }$ is the function

$$
K ( \theta ) = \left\{ \begin{array} { l l } { \lambda ~ \sigma ( - \theta / h ) , \qquad \theta \leqslant 0 } \\ { \mu ~ \sigma ( \theta / h ) + \frac { 1 } { 6 } ( \xi - \theta ) ^ { 3 } + \frac { 1 } { 6 } d ( h - \theta ) ^ { 3 } , \qquad 0 \leqslant \theta \leqslant \xi } \\ { \mu ~ \sigma ( \theta / h ) + \frac { 1 } { 6 } d ( h - \theta ) ^ { 3 } , \qquad \xi \leqslant \theta \leqslant h } \\ { \mu ~ \sigma ( \theta / h ) , \qquad \theta \geqslant h , } \end{array} \right.
$$

where $\{ \sigma ( x ) ; 0 \leqslant x < \infty \}$ is defined in equation (21.49). Because $\mathbf { \partial } \kappa , \mathbf { \partial } \kappa ^ { \prime }$ and $\pmb { K } ^ { \prime \prime }$ are continuous at $\pmb \theta = 0$ , it follows that the parameters have the values

$$
\left. \begin{array} { l } { d = - \xi ^ { 3 } / h ^ { 3 } } \\ { \lambda = \frac { 1 } { 1 2 } [ - \sqrt { 3 } \xi h ^ { 2 } + 3 \xi ^ { 2 } h - ( 3 - \sqrt { 3 } ) \xi ^ { 3 } ] } \\ { \mu = \frac { 1 } { 1 2 } [ \sqrt { 3 } \xi h ^ { 2 } + 3 \xi ^ { 2 } h - ( 3 + \sqrt { 3 } ) \xi ^ { 3 } ] } \end{array} \right\} .
$$

We note that, for all $\xi$ in $( 0 , h ) , \lambda$ is negative and $\pmb { \mu }$ is positive. Hence $\pmb { K } ( \pmb \theta )$ has the correct sign in Figure 22.1,except perhaps when $0 < \theta < h$ In this interval $\pmb { K } ( \pmb \theta )$ is positive, but there seems to be no short way of proving this statement. One method begins with the remark that, because $\pmb { K } ( 0 ) = 0$ ， $K ^ { \prime } ( 0 ) { > } 0$ and $K ^ { \prime \prime \prime } ( 0 + ) < 0$ ,there is at most one zero of $\pmb { K }$ in the interval $( 0 , \xi ]$ .Direct calculation gives $\pmb { K } ( \pmb { \xi } ) > 0 .$ Hence $\pmb { K }$ has no zeros in $( 0 , \xi ]$ ，Similarly there are no zeros in $[ \xi , h )$ ，which completes the justification of the signs that are shown in Figure 22.1.

It is now straightforward to calculate the integral

$$
I ( \xi ) = \int _ { - \infty } ^ { \infty } \left| K ( \theta ) \right| \mathrm { d } \theta , \qquad 0 \leqslant \xi \leqslant h ,
$$

in order to bound the error (22.52) by a multiple of $\| f ^ { ( 4 ) } \| _ { \infty }$ . Because the function (21.49) satisfies the equation

$$
\sigma ( x + 1 ) = ( \sqrt { 3 - 2 } ) \sigma ( x ) , \qquad x \geqslant 0 ,
$$

expression (22.58),Figure 22.1, and the definition of $\sigma$ give the value

$$
\begin{array} { l } { { \displaystyle I ( \xi ) = \left( \left| \lambda \right| + \left| \mu \right| \right) \Biggl [ \int _ { 0 } ^ { h } \sigma ( \theta / h ) \mathrm { d } \theta \Biggr ] \Biggl [ \sum _ { j = 0 } ^ { \infty } \left| \surd 3 - 2 \right| ^ { j } \Biggr ] } } \\ { { \displaystyle \qquad + \frac { 1 } { 6 } \int _ { 0 } ^ { \xi } \left( \xi - \theta \right) ^ { 3 } \mathrm { d } \theta + \frac { 1 } { 6 } d \int _ { 0 } ^ { h } \left( h - \theta \right) ^ { 3 } \mathrm { d } \theta } } \\ { { \displaystyle \qquad = \left( \left| \lambda \right| + \left| \mu \right| \right) \frac { 1 } { 1 2 } \sqrt { 3 } h + \frac { 1 } { 2 4 } ( \xi ^ { 4 } + d h ^ { 4 } ) . } } \end{array}
$$

It follows from equations (22.52) and (22.59) that the bound

$$
\begin{array} { r l } & { \left| f ( \xi ) - s ( \xi ) \right| \leqslant I ( \xi ) \left\| f ^ { ( 4 ) } \right\| _ { \infty } } \\ & { \qquad = \frac { 1 } { 2 4 } ( \xi ^ { 4 } - 2 \xi ^ { 3 } h + \xi h ^ { 3 } ) \left\| f ^ { ( 4 ) } \right\| _ { \infty } , \quad \quad 0 \leqslant \xi \leqslant h , } \end{array}
$$

is obtained. Therefore, because the right-hand side takes its maximum value when $\xi = { \textstyle \frac { 1 } { 2 } } h .$ ，and because all intervals between data points are similar,the error of the spline approximation is bounded by the inequality

$$
\| f - s \| _ { \infty } \leqslant \frac { 5 h ^ { 4 } } { 3 8 4 } \| f ^ { ( 4 ) } \| _ { \infty } .
$$

In order to check most of the work of this section, we let $f$ be a quartic polynomial, and we deduce the error $f ( \xi ) - s ( \xi )$ from equations (22.52), (22.58) and (22.59). Because $f ^ { ( 4 ) } ( x )$ is constant the equation

$$
f ( \xi ) - s ( \xi ) = J ( \xi ) f ^ { ( 4 ) } ( x ) , 0 \leqslant \xi \leqslant h ,
$$

is satisfied, where $\pmb { J } ( \pmb { \xi } )$ is the integral

$$
\begin{array} { l } { { \displaystyle { J ( \xi ) = ( \lambda + \mu ) \biggl [ \int _ { 0 } ^ { h } \sigma ( \theta / h ) \mathrm { d } \theta \biggl ] \biggl [ \sum _ { j = 0 } ^ { \infty } ( \sqrt { 3 - 2 } ) ^ { j } \biggr ] } } } \\ { { \displaystyle ~ + \frac { 1 } { 6 } \int _ { 0 } ^ { \xi } ( \xi - \theta ) ^ { 3 } \mathrm { d } \theta + \frac { 1 } { 6 } d \int _ { 0 } ^ { h } \left( h - \theta \right) ^ { 3 } \mathrm { d } \theta } }  \\ { { = ( \lambda + \mu ) \frac { 1 } { 1 2 } h + \frac { 1 } { 2 4 } ( \xi ^ { 4 } + d h ^ { 4 } ) } } \\ { { = \frac { 1 } { 2 4 } \xi ^ { 2 } ( \xi - h ) ^ { 2 } . } } \end{array}
$$

The check on the calculation is that we have verified the first line of expression (21.43).

Inequality (22.64) provides a substantial improvement on the bound (20.52), where $\mathcal { S }$ is the space of cubic splines whose knots are the points

$$
\xi _ { j } = \xi _ { 0 } + j h , \qquad j = 0 , 1 , \ldots , n ,
$$

and where $f$ is any function in $\mathcal { C } ^ { ( 4 ) } [ \xi _ { 0 } , \xi _ { n } ]$ .The analysis for the infinite range is applicable to this case, because we may extend $f$ to the infinite range in any way that does not increase $\| f ^ { ( 4 ) } \| _ { \infty }$ ,and we may let $\pmb { S }$ be the spline (22.49). The restriction of $\pmb { S }$ to the interval $[ \xi _ { 0 } , \xi _ { n } ]$ is an element of ${ \mathcal { S } } .$ Hence $d ^ { * } ( \mathcal { S } , f )$ is bounded above by $\| f - s \| _ { \infty }$ . It follows from inequality (22.64) that the constant in expression (20.52) can be reduced from $\frac { 7 3 } { 3 8 4 }$ t0 $\frac { 5 } { 3 8 4 }$

One unusual feature of the example of this section is that all the zeros of the kernel function (22.53) occur at points where a derivative of $\pmb { K }$ is discontinuous. In general, if equation (22.18) holds,and if one requires the value of the constant (22.3) in the bound

$$
{ \big | } L ( f ) { \big | } \leqslant c { \big | } { \big | } f ^ { ( k + 1 ) } { \big | } { \big | } _ { \infty } ,
$$

then it is necessary to find the values of $\pmb \theta$ at which $\left\{ K ( \theta ) ; a \leqslant \theta \leqslant b \right\}$ changes sign by solving a polynomial equation. Some examples are $\mathtt { \mathtt { s i v e n } }$ in the exercises.

# 22 Exercises

22.1Let $p ( { \scriptstyle { \frac { 1 } { 2 } } } ) = { \scriptstyle { \frac { 1 } { 2 } } } [ f ( 0 ) + f ( 1 ) ] .$ where $f$ is a function in $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ]$ .Find the smallest constants $c _ { 0 } , \ : c _ { 1 }$ and $c _ { 2 }$ such that the error bounds

$$
\begin{array} { r } { \big | f ( \frac { 1 } { 2 } ) - p ( \frac { 1 } { 2 } ) \big | \leqslant c _ { k } \big \| f ^ { ( k ) } \big \| _ { \infty } , \qquad k = 0 , 1 , 2 , } \end{array}
$$

are valid.

22.2 Let $f$ be any function in $\mathcal { C } ^ { ( 4 ) } [ 0 , 2 ]$ 、 Show that the error of Simpson's integration rule satisfies the equation

$$
\begin{array} { r } { \displaystyle \int _ { 0 } ^ { 2 } f ( x ) \mathrm { d } x - \frac { 1 } { 3 } [ f ( 0 ) + 4 f ( 1 ) + f ( 2 ) ] = - \frac { 1 } { 9 0 } f ^ { ( 4 ) } ( \xi ) , } \end{array}
$$

where $\xi$ is a point of the range [0,2].

22.3 Calculate the values of the coefficients $w _ { 0 } , w _ { 1 }$ and $w _ { 3 }$ such that the inequality

$$
\left| f ( 2 ) - \left[ w _ { 0 } f ( 0 ) + w _ { 1 } f ( 1 ) + w _ { 3 } f ( 3 ) \right] \right| \leqslant \mu \| f ^ { \prime \prime } \| _ { 2 }
$$

holds for all functions $f$ in $\mathscr { C } ^ { ( 2 ) } [ 0 , 3 ]$ , where the degree of freedom in the coefficients is used to minimize the constant $\pmb { \mu }$ . You should obtain the bound

$$
\begin{array} { r } { { \left| f ( 2 ) + \frac { 1 } { 4 } f ( 0 ) - \frac { 7 } { 8 } f ( 1 ) - \frac { 3 } { 8 } f ( 3 ) \right| \leqslant \sqrt { ( \frac { 5 } { 4 8 } ) } \left\| f ^ { \prime \prime } \right\| } _ { 2 } . } \end{array}
$$

22.4 Prove Theorem 22.3 by integrating the right-hand side of equation (22.33) by parts.

Show by an example that the constant $\frac { 5 } { 3 8 4 }$ in expression (22.64) cannot be reduced. There exists a suitable function $f$ that is zero at all the knots.

22.6 Let $f$ be a function in $\mathcal { C } ^ { ( 4 ) } [ 0 , 1 ]$ . Calculate the third derivative of the cubic polynomial $p$ that interpolates the data $\left\{ f ( 0 ) , f ^ { \prime } ( 0 ) \right.$ ， $f ( 1 ) , f ^ { \prime } ( 1 ) \}$ . Prove that the inequality

$$
\begin{array} { r } { \left| f ^ { \prime \prime \prime } ( \xi ) - p ^ { \prime \prime \prime } ( \xi ) \right| \leqslant ( \frac { 1 } { 2 } - \xi + 2 \xi ^ { 3 } - \xi ^ { 4 } ) \| f ^ { ( 4 ) } \| _ { \infty } } \end{array}
$$

is satisfied, where $\pmb { \xi }$ is any point in [O,1]. Find a function $f$ with a piecewise continuous fourth derivative for which this inequality holds as an equation.

22.7 Calculate the values of the parameters $w _ { 1 } , w _ { 2 } , w _ { 3 }$ and $w _ { 4 }$ that minimize the number $\pmb { \mu }$ in the bound

$$
\bigg \vert \int _ { 0 } ^ { 1 } f ( x ) \mathrm { d } x - w _ { 1 } f ( 0 ) - w _ { 2 } f ^ { \prime } ( 0 ) - w _ { 3 } f ( 1 ) - w _ { 4 } f ^ { \prime } ( 1 ) \bigg \vert \leqslant \mu \| f ^ { \prime \prime } \| _ { \infty } ,
$$

where $f$ is any function in $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ]$ . Show that the least value of $\pmb { \mu }$ is $\scriptstyle { \frac { 1 } { 3 2 } }$

22.8 Prove that the right-hand side of the final inequality of Exercise 22.3 can be replaced by the expression $\begin{array} { r } { \sqrt { \left( \frac { 5 } { 4 8 } \right) [ \| f ^ { \prime \prime } \| _ { 2 } ^ { 2 } - 9 ( f [ 0 , 1 , 3 ] ) ^ { 2 } ] ^ { \frac { 1 } { 2 } } } , } \end{array}$ which is a useful improvement because the divided difference $\textstyle f [ 0 , 1 , 3 ]$ can be calculated from the function values $f ( 0 ) , f ( 1 )$ and $f ( 3 )$ . One method of proof comes from expressing $f ^ { \prime \prime }$ in the form $f ^ { \prime \prime } ( \theta ) = \alpha B ( \theta ) + \{ f ^ { \prime \prime } ( \theta ) - \alpha B ( \theta ) \} , \qquad 0 \leqslant \theta \leqslant 3 ,$ where $\pmb { B }$ is the kernel function that occurs when Theorem 22.3 is used to express $f [ 0 , 1 , 3 ]$ in terms of $f ^ { \prime \prime }$ ,and where the multiplier $_ \alpha$ is such that the term in the braces is orthogonal to $f ^ { \prime \prime }$ . Verify that the two sides of the new inequality are equal when $f$ is the function $\{ f ( x ) = x ^ { 3 } - 3 ( x - 2 ) _ { + } ^ { 3 }$ ； $0 \leqslant x \leqslant 3 \}$ and explain why this happens.

22.9 Investigate the validity of the assumption, made immediately before equation (22.52), that the Peano kernel theorem can be applied when the range of the variable $x$ is infinite,given the condition that the derivatives of $f$ are bounded.

22.10 For any bounded function $f$ in $\mathcal { C } ^ { ( 3 ) } ( - \infty , \infty )$ ,let $\pmb { s }$ be the quadratic spline with knots at the points (18.35),that satisfies the interpolation conditions $\{ s ( x _ { j } ) = f ( x _ { j } ) = f ( j h )$ ； $\dot { \mathbf { \theta } } = 0 , \mathbf { \theta } \pm 1 , \mathbf { \eta } \pm 2$ ， .. .},and that is studied in Section 18.4. Prove that the value of the spline at a knot is bounded by the inequality

$$
\big | f ( \xi _ { i } ) - s ( \xi _ { i } ) \big | \mathrm { \leqslant } \frac { h ^ { 3 } } { 2 4 } \big \| f ^ { \prime \prime \prime } \big \| _ { \infty } .
$$

# 23

# Natural and perfect splines

# 23.1 A variational problem

A very early result in the study of spline approximations is that a cubic spline is the solution of the following variational problem. Given the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ in the interval $[ a , b ] ,$ satisfying the conditions

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b ,
$$

and given the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ ，calculate the function $\{ s ( x ) ; a \leqslant x \leqslant b \}$ that minimizes the integral

$$
\int _ { a } ^ { b } \left[ s ^ { \prime \prime } ( x ) \right] ^ { 2 } \mathrm { d } x ,
$$

subject to the interpolation equations

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , m .
$$

If one knows the solution to this problem in advance, then there is a short way of showing that one has the required function, which is given in the proof of Theorem 23.2.In this section, however, the solution is derived without foresight or intuition,because the method that is used has other applications.

We assume that $m > 2$ ,because otherwise the integral (23.2) can be made zero, by letting $\pmb { \mathscr { s } }$ be any straight line that interpolates the data. When $m > 2$ ， then it is necessary to identify the restrictions that the conditions (23.3） impose on the second derivative $\{ s ^ { \prime \prime } ( x ) ; a \leqslant x \leqslant b \}$ Because Theorem 22.3 shows that divided differences can be expressed in terms of derivatives, the equations

$$
s [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] = f [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] , \qquad p = 1 , 2 , \ldots , m - 2 ,
$$

which follow from condition (23.3)，are really constraints on $\pmb { s } ^ { \prime \prime }$ Specifically,applying the theorem to expression (23.4） gives the constraints

$$
\int _ { a } ^ { b } B _ { p } ( \theta ) s ^ { \prime \prime } ( \theta ) { \mathrm d } \theta = f [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] , \qquad p = 1 , 2 , \ldots , m - 2 ,
$$

where $\scriptstyle B _ { p }$ is the first degree $\pmb { B }$ -spline

$$
B _ { p } ( \theta ) = \sum _ { i = p } ^ { p + 2 } \bigg \{ ( \theta - x _ { i } ) _ { + } \bigg / \prod _ { \stackrel { j = p } { j \neq i } } ^ { p + 2 } ( x _ { j } - x _ { i } ) \bigg \} , \qquad a \leq \theta \leqslant b .
$$

Therefore we seek the function $\{ u ( x ) ; a \leqslant x \leqslant b \}$ that minimizes the integral

$$
I ( u ) = \int _ { a } ^ { b } \left[ u ( x ) \right] ^ { 2 } \mathrm { d } x ,
$$

subject to the conditions

$$
\int _ { a } ^ { b } B _ { p } ( \theta ) u ( \theta ) { \mathrm d } \theta = f [ x _ { p } , x _ { p + 1 } , x _ { p + 2 } ] , \qquad p = 1 , 2 , \ldots , m - 2 .
$$

If $\pmb { u }$ is not of the form

$$
u ( x ) = \sum _ { j = 1 } ^ { m - 2 } \lambda _ { j } B _ { j } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

then there is a function, $v$ say, that is orthogonal to the splines $\{ B _ { j } ; j =$ $1 , 2 , \ldots , m - 2 \}$ ，but that is not orthogonal to $\pmb { u }$ 、Hence the equations (23.8) hold if $\pmb { u }$ is replaced by $\left( u + \alpha v \right)$ , where $_ { \alpha }$ is any real number, but $_ \alpha$ can be chosen so that $I ( u + \alpha v )$ is less than $I ( u )$ . It follows that equation (23.9) is satisfied.

In order to calculate the values of the parameters $\left\{ \lambda _ { j } ; j = 1 , 2 , \ldots , \right.$ $m - 2 \}$ of expression (23.9),we note that the conditions (23.8) give a square system of linear equations in the parameters. If the matrix of the system is singular, then there exist numbers $\{ \mu _ { j } ; j = 1 , 2 , \ldots , m - 2 \}$ ,that are not al zero, such that the equations

$$
\int _ { a } ^ { b } B _ { p } ( \theta ) \bigg [ \sum _ { j = 1 } ^ { m - 2 } \mu _ { j } B _ { j } ( \theta ) \bigg ] { \mathrm { d } } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - 2 ,
$$

hold. These equations, however, imply the identity

$$
\int _ { a } ^ { b } \left[ \sum _ { j = 1 } ^ { m - 2 } \mu _ { j } B _ { j } ( \theta ) \right] ^ { 2 } \mathrm { d } \theta = 0 ,
$$

which contradicts Theorem 19.2. Therefore the parameters of the function (23.9) are defined by the constraints (23.8).

The function $\{ s ( x ) ; a \leqslant x \leqslant b \}$ is obtained by integrating $\{ u ( x )$ ； $a \leqslant x \leqslant$ $b \}$ twice,where the constants of integration are chosen so that $\pmb { s } ( \pmb { x } _ { 1 } )$ and $\pmb { s } ( \pmb { x } _ { 2 } )$ are equal to $f ( { \pmb x } _ { 1 } )$ and $f ( x _ { 2 } )$ respectively.By applying the conditions (23.4) in sequence, it follows that the equations $\{ s ( x _ { p + 2 } ) = f ( x _ { p + 2 } ) ; p = 1$ ， $2 , \ldots , m - 2 \}$ are obtained. Hence $\pmb { s }$ is the function, interpolating the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ ， that minimizes the integral (23.2). It is a cubic spline,because its second derivative is the continuous piecewise linear function (23.9). It is called a natural spline because it solves the variational problem of this section. The characteristic properties of natural cubic splines,which are implied by equation (23.9),are that their second derivatives are zero at $x _ { 1 }$ and $x _ { m }$ ,and that, if $x _ { 1 }$ and $x _ { m }$ are interior points of $[ a , b ] ,$ , then the cubic polynomial pieces degenerate to straight lines on each of the intervals $[ a , x _ { 1 } ]$ and $[ x _ { m } , b ]$

The degree of a natural spline is always odd. A spline $\pmb { s }$ of degree $( 2 k + 1 )$ on the interval $[ a , b ]$ is called a natural spline if it satisfies the conditions

$$
{ s } ^ { ( j ) } ( x _ { 1 } ) = { s } ^ { ( j ) } ( x _ { m } ) = 0 , \qquad k + 1 \leqslant j \leqslant 2 k ,
$$

where $x _ { 1 }$ and $x _ { m }$ are the extreme knots.Further, when $a < x _ { 1 }$ and when $x _ { m } < b$ ,then $\pmb { s }$ must be a polynomial of degree $k$ on the intervals $[ a , x _ { 1 } ]$ and $[ x _ { m } , b ]$ respectively.It is shown in the next section that natural splines give solutions to two variational problems.

If the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ satisfy condition (23.1),then the notation $\mathcal { S } _ { \mathrm { N } } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { m } )$ is used for the linear space of natural splines of degree $( 2 k + 1 )$ that have these points as knots: Sometimes we shorten the notation to $\mathcal { S } _ { \mathbf { N } }$ .It is proved in Theorem 23.1 that,if $m \geq k + 1$ , then the dimension of $\mathcal { S } _ { \mathbf { N } }$ is equal to $_ m$

# 23.2 Properties of natural splines

Natural spline approximations to functions are calculated by interpolation at the knots. The following theorem states that, except when $m \leqslant k$ ,the interpolation problem has a unique solution.

# Theorem 23.1

Let $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ be any set of real numbers that satisfy expression (23.1),and let $k$ be any integer in the range $[ 1 , m - 1 ]$ . Then, for any $f$ in $\mathcal { C } [ a , b ] ,$ ,there is exactly one function $\pmb { s }$ in the space $\mathcal { S } _ { \mathbf { N } } ( 2 k + 1 ,$ $x _ { 1 } , x _ { 2 } , \ldots , x _ { m } )$ that satisfies the interpolation conditions

$$
s ( x _ { i } ) = f ( x _ { i } ) , \qquad i = 1 , 2 , \ldots , m .
$$

Proof. If $\mathbf { \boldsymbol { a } } < \mathbf { \boldsymbol { x } } _ { 1 }$ , then the form of a natural spline on the interval $[ a , x _ { 1 } ]$ is defined uniquely by the form of the spline on $[ x _ { 1 } , x _ { 2 } ]$ A similar condition holds at the other end of the range $[ a , b ]$ . Therefore there is no loss of generality in assuming that $x _ { 1 } = a$ and $x _ { m } = b$ . It has been noted already that the dimension of the space $\mathcal { S } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . ~ , x _ { m } )$ of ordinary splines is equal to $( 2 k + m )$ . Natural splines, however,are splines that satisfy the linear homogeneous conditions (23.12)． Therefore the dimension of $\mathcal { S } _ { \mathrm { N } } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { m } )$ is not less than m. If the dimension exceeds $^ { m }$ ,then the equations

$$
\bar { s } ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , m , \ldots \quad \bar { s } \in \mathcal { S } _ { \mathrm { N } } ,
$$

have a non-trivial solution. Therefore we ask whether these equations imply that $\bar { s }$ is the zero function.

We evaluate the integral

$$
I ( \bar { s } ^ { ( k + 1 ) } ) = \int _ { x _ { 1 } } ^ { x _ { m } } \left[ \bar { s } ^ { ( k + 1 ) } ( x ) \right] ^ { 2 } \mathrm { d } x
$$

by parts. It follows from conditions (23.12),from the fact that $\bar { s } ^ { ( 2 k + 1 ) }$ is constant on each of the intervals $\{ ( x _ { i } , x _ { i + 1 } ) ; i = 1 , 2 , . . . , m - 1 \}$ ,and from equation (23.14), that the integral has the value

$$
\begin{array} { l } { { I ( \bar { s } ^ { ( k + 1 ) } ) = ( - 1 ) ^ { k } \displaystyle \int _ { x _ { 1 } } ^ { x _ { m } } \bar { s } ^ { \prime } ( x ) \bar { s } ^ { ( 2 k + 1 ) } ( x ) \mathrm { d } x } } \\ { { \qquad = ( - 1 ) ^ { k } \displaystyle \sum _ { i = 1 } ^ { m - 1 } \bar { s } ^ { ( 2 k + 1 ) } ( x _ { i } + ) \displaystyle \int _ { x _ { i } } ^ { x _ { i + 1 } } \bar { s } ^ { \prime } ( x ) \mathrm { d } x } } \\ { { \qquad = ( - 1 ) ^ { k } \displaystyle \sum _ { i = 1 } ^ { m - 1 } \bar { s } ^ { ( 2 k + 1 ) } ( x _ { i } + ) [ \bar { s } ( x _ { i + 1 } ) - \bar { s } ( x _ { i } ) ] } } \\ { { \qquad = 0 , } } \end{array}
$$

where $x _ { i } +$ is any point in the interval $\left( x _ { i } , x _ { i + 1 } \right)$ .Therefore,because $\bar { s } ^ { ( k + 1 ) }$ is a continuous function,equations (23.15)and (23.16) imply that s(k+1) is identically zero.Hence $\bar { s }$ isin $\mathcal { P } _ { k }$ ，but $\bar { s }$ also satisfies the conditions (23.14). Thus, because $m \geq k + 1 , \mathrm { { : } }$ $\bar { s }$ is the zero function, which completes the proof that the dimension of the space $\mathcal { S } _ { \mathrm { N } } ( 2 k + 1 , x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { m } )$ is equal to $^ { m }$

We now know that the number of conditions (23.13) on $\pmb { S }$ is equal to the dimension of $\mathcal { S } _ { \mathbf { N } }$ . It follows from the method of proof of Theorem 5.4 that these conditions define $\pmb { s }$ uniquely,unless the equations (23.14) have a non-trivial solution. Because we have shown already that $\bar { s }$ can only be the zero function, the theorem is proved.□

The next theorem shows that interpolating natural splines are the solution to the kind of variational problem that is studied in Section 23.1.

# Theorem 23.2

Let the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , m \}$ be given, and let $k$ be an integer in $[ 1 , m - 1 ]$ The function $\pmb { s }$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ that minimizes the integral

$$
\int _ { a } ^ { b } [ s ^ { ( k + 1 ) } ( x ) ] ^ { 2 } { \mathrm { d } } x ,
$$

subject to the interpolation conditions (23.13), is the natural spline that is defined in Theorem 23.1.

Proof. We let $\pmb { s }$ be the natural spline that is the subject of Theorem 23.1, and we let $\pmb { g }$ be any function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ that interpolates the data. Hence the equations

$$
g ( x _ { i } ) - s ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , m ,
$$

are satisfied. Because the definition of the 2-norm gives the identity

$$
\begin{array} { r } { \| g ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } = \big \| s ^ { ( k + 1 ) } \big \| _ { 2 } ^ { 2 } + \big \| g ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \big \| _ { 2 } ^ { 2 } + 2 \big ( g ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } , s ^ { ( k + 1 ) } \big ) , } \end{array}
$$

where the last term is twice the scalar product

$$
\int _ { a } ^ { b } \left[ g ^ { ( k + 1 ) } ( x ) - s ^ { ( k + 1 ) } ( x ) \right] s ^ { ( k + 1 ) } ( x ) \mathrm { d } x ,
$$

it is sufficient to show that this scalar product is zero. By applying integration by parts,by using the conditions

$$
s ^ { ( j ) } ( a ) = s ^ { ( j ) } ( b ) = 0 , \qquad k + 1 \leqslant j \leqslant 2 k ,
$$

which are obtained because $\pmb { s }$ is a natural spline,and by noting that $s ^ { ( 2 k + 1 ) } ( x )$ is zero if $x$ is in the interval $( a , x _ { 1 } )$ or $( x _ { m } , b )$ ,i folows that the integral (23.20) has the value

$$
( - 1 ) ^ { k } \int _ { x _ { 1 } } ^ { x _ { m } } \left[ g ^ { \prime } ( x ) - s ^ { \prime } ( x ) \right] s ^ { ( 2 k + 1 ) } ( x ) \mathrm { d } x .
$$

Therefore, because of condition (23.18), the method that gives the last three lines of expresson (23.16) implies also that the present integral is zero,which completes the proof of the theorem.□

One result that can be deduced from the proof is useful later. It is obtained from equation (23.19) and the fact that expression (23.20) is zero. It is that, if $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ and if $\pmb { s }$ is the natural spline that is defined in Theorem 23.1, then the identity

$$
\| f ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } = \| s ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } + \| f ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 }
$$

is satisfied.

The most remarkable property of natural splines is their relevance to an approximation problem that is mentioned in Section 22.3.In this problem a linear functional $L$ is estimated by the expression

$$
L ( f ) \approx \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) ,
$$

where the values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ are given,but the weights $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ have to be chosen. We recall that, if the estimate is to be exact when $f$ is in $\mathcal { P } _ { k }$ ,and if $^ { m }$ is much larger than $k$ ,then a suitable way of fixing the degrees of freedom in the weights is to minimize a norm of the kernel function

$$
K ( \theta ) = { \frac { 1 } { k ! } } { \bigg [ } L _ { x } \{ ( x - \theta ) _ { + } ^ { k } \} - \sum _ { i = 1 } ^ { m } w _ { i } ( x _ { i } - \theta ) _ { + } ^ { k } { \bigg ] } , \qquad a \leqslant \theta \leqslant b ,
$$

of the relation

$$
L ( f ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) { \mathrm { d } } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] .
$$

Natural splines give a direct and convenient method of calculating the approximation (23.24), when the weights $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ have the values that minimize the 2-norm

$$
\left\| K \right\| _ { 2 } = \bigg \{ \int _ { a } ^ { b } \left[ K \left( \theta \right) \right] ^ { 2 } \mathrm { d } \theta \bigg \} ^ { \frac { 1 } { 2 } } .
$$

The importance of natural splines to this calculation is shown usually by a detailed analysis of the conditions for the least value of $\| \pmb { K } \| _ { 2 }$ .However, because a similar analysis is given in Chapter 24,we prefer a different and much shorter approach, that depends on knowing that the required approximation to $L ( f )$ is $L ( s )$ , where $\pmb { s }$ is the natural spline that is defined in Theorem 23.1. This approximation does have the form (23.24), because,if the natural splines $\{ s _ { i } ; i = 1 , 2 , \ldots , m \}$ are the cardinal functions of the interpolation procedure of Theorem 23.1, then $\ b { L } ( s )$ is the expression

$$
\begin{array} { l } { { \displaystyle { \cal L } ( s ) = { \cal L } \bigg \{ \sum _ { i = 1 } ^ { m } f ( x _ { i } ) s _ { i } \bigg \} } } \\ { ~ } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } { \cal L } ( s _ { i } ) f ( x _ { i } ) } } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } \bar { w } _ { i } f ( x _ { i } ) } , } \end{array}
$$

say. We let $\{ { \bar { K } } ( \theta ) ; a \leqslant \theta \leqslant b \}$ be the kernel function that is obtained by seting $\left\{ w _ { i } = \bar { w } _ { i } ; i = 1 , 2 , \ldots , m \right\}$ in equation (23.25). The following theorem shows that $L ( s )$ is the required approximation.

# Theorem 23.3

Let $L$ be any linear functional from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ to $\mathcal { R } ^ { 1 }$ ,and let $\bar { K }$ be the kernel function that has just been defined.Let expression (23.24) be any approximation to $L ( f )$ ,that is exact when $f$ is in $\mathcal { P } _ { k }$ . Then the norm of the kernel function (23.25)is bounded below by the inequality

$$
\| { \bar { K } } \| _ { 2 } \leqslant \| K \| _ { 2 } .
$$

Proof. Equation (23.26) implies the bound

$$
\bigg | L ( f ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) \bigg | \leqslant \| K \| _ { 2 } \| f ^ { ( k + 1 ) } \| _ { 2 } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] .
$$

By replacing $f \operatorname { \bf { b y } } f - s ,$ where $\pmb { s }$ is defined in Theorem 23.1, we obtain the relation

$$
{ \biggl | } L ( f ) - L ( s ) - \sum _ { i = 1 } ^ { m } w _ { i } [ f ( x _ { i } ) - s ( x _ { i } ) ] { \biggr | } \leqslant \| K \| _ { 2 } \| f ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \| _ { 2 } .
$$

Because $\pmb { s }$ satisfies the interpolation conditions (23.13),and because equation (23.23） shows that $\| f ^ { ( k + 1 ) } - s ^ { ( k + 1 ) } \| _ { 2 }$ is bounded above by $\| f ^ { ( k + 1 ) } \| _ { 2 }$ ,it follows thattheinequality

$$
\begin{array} { r } { \big \vert L ( f ) - L ( s ) \big \vert \leqslant \big \| K \big \| _ { 2 } \big \| f ^ { ( k + 1 ) } \big \| _ { 2 } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] , } \end{array}
$$

is satisfied. The proof is completed by making a particular choice of $f ,$ namely a function $\bar { f }$ such that $\bar { f } ^ { ( k + 1 ) }$ is equal to $\bar { \kappa } .$ Hence expressions (23.28) and (23.32) give the relation

$$
\left| L ( { \bar { f } } ) - \sum _ { i = 1 } ^ { m } { \bar { w } } _ { i } { \bar { f } } ( x _ { i } ) \right| \leqslant \| K \| _ { 2 } \| { \bar { K } } \| _ { 2 } .
$$

Because the kernel function $\bar { K }$ is defined by the equation

$$
L ( f ) - \sum _ { i = 1 } ^ { m } { \bar { w } } _ { i } f ( x _ { i } ) = \int _ { a } ^ { b } { \bar { K } } ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] ,
$$

the choice of $\bar { f }$ implies the identity

$$
L ( \overline { { f } } ) - \sum _ { i = 1 } ^ { m } \bar { w } _ { i } \overline { { f } } ( x _ { i } ) = \| \bar { K } \| _ { 2 } ^ { 2 } .
$$

It follows from condition (23.33) that the theorem is true.[

If $c$ is any constant that can replace $\| \pmb { K } \| _ { 2 }$ in inequality (23.30), then $\| K \| _ { 2 }$ may be replaced by $^ c$ throughout the proof of the theorem. Therefore,for every set of weights $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ that allows an error bound of the form

$$
\bigg | L ( f ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) \bigg | \leqslant c \| f ^ { ( k + 1 ) } \| _ { 2 } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,
$$

the constant $^ { c }$ is not less than $\| \bar { K } \| _ { 2 }$ .Equation (23.34) shows that the least value $c = \| \bar { \pmb { K } } \| _ { 2 }$ is achieved when the weights have the values $\left\{ w _ { i } = \bar { w } _ { i } = \right.$ $L ( s _ { i } ) ; i = 1 , 2 , \ldots , m \}$ .Hence the approximation $\pmb { { \cal L } } ( \pmb { s } )$ to $L ( f )$ is the one that minimizes the constant $^ { c }$ of expression (23.36).

It is interesting that, if $L ( f )$ is the point function value $f ( \xi )$ ,where $\pmb { \xi }$ is any fixed point of $[ a , b ] ,$ ，then the estimate of $f ( \xi )$ that minimizes the right-hand side of expresson (23.36) is the same as the value at $\pmb { \xi }$ of the function that solves the variational problem of Theorem 23.2.The fact that these two different techniques give the same estimate of $f ( \xi )$ isa consequence of the dependence of the work of this section on the 2-norm of f(k+1）

# 23.3 Perfect splines

Perfect splines are obtained from a variational problem that is closely related to the one that is the subject of Theorem 23.2. The new variational problem is to calculate a function $\pmb { s }$ that minimizes $\big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ,$ subject to the interpolation conditions (23.3),where $m > k$ ,and where the abscissae of the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ satisfy expression (23.1). We consider this calculation,and we find that, at least on a part of the range $[ a , b ] , s$ is.a spline function of degree $( k + 1 )$

As in Section 23.1，divided differences are used to express the interpolationconditionsintermsof $\pmb { s } ^ { ( k + 1 ) }$ Therefore, leting $\{ z ( x ) = s ^ { ( k + 1 ) } ( x )$ ； $a \leqslant x \leqslant b \}$ ,the least value of the norm

$$
J ( z ) = \operatorname* { m a x } _ { a \leqslant x \leqslant b } { \left| z ( x ) \right| }
$$

is required, subject to the conditions

$$
\begin{array} { r l } {  { \int _ { a } ^ { b } B _ { p } ( \theta ) z ( \theta ) \mathrm { d } \theta = k ! f [ x _ { p } , x _ { p + 1 } , \ldots , x _ { p + k + 1 } ] } } \\ & { \quad = c _ { p } , \qquad p = 1 , 2 , \ldots , m - k - 1 , } \end{array}
$$

say,where $\scriptstyle B _ { p }$ is the $\pmb { B }$ -spline that has the form (19.1O) and the knots $\{ x _ { j } ; j = p , p + 1 , \ldots , p + k + 1 \}$ . Expressions (23.37） and (23.38) correspond to equations (23.7) and (23.8).

Because there is an unknown function to be found, and because the number of constraints is finite, it is useful to apply duality theory to the calculation of $z$ .We note, therefore, that the constraints (23.38) imply that, for all values of the multipliers $\{ \lambda _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ the inequality

$$
\begin{array} { r } { \displaystyle \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } c _ { p } = \int _ { a } ^ { b } \left[ \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) \right] z ( \theta ) \mathrm { d } \theta } \\ { \displaystyle \leqslant \left\| z \right\| _ { \infty } \int _ { a } ^ { b } \left. \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) \right. \mathrm { d } \theta } \end{array}
$$

must hold,which gives the bound

$$
\left\| z \right\| _ { \infty } \geqslant \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } c _ { p } \bigg / \int _ { a } ^ { b } \left| \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) \right| \mathrm { d } \theta .
$$

Because the calculation of $z$ is a continuous version of a linear programming problem, it follows from the duality that necessary and sufficient conditions for $z$ to be optimal are that the constraints (23.38) are satisfied,and that there exist values of the parameters $\begin{array} { r } { \left\{ \lambda _ { p } ; p = 1 \right. } \end{array}$ ， $2 , \ldots , m - k - 1 \}$ such that inequality (23.40) becomes an equation. In this case the two lines of expression (23.39) are equal. Therefore, provided that equation (23.38) holds, the condition that characterizes the optimal $z$ is that there is a function

$$
\eta ( \theta ) = \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

that is not identically zero, such that, if $\pmb \theta$ is any point of $[ a , b ]$ at which $\pmb { \eta } ( \pmb \theta )$ is non-zero, then $z ( \theta )$ has the value

$$
z \left( \theta \right) = \| z \| _ { \infty } \operatorname { s i g n } { \left[ \eta \left( \theta \right) \right] } .
$$

The following theorem gives a useful version of this result that depends on properties of $\pmb { B }$ -splines. In order to state the theorem, we require the definition of a ‘perfect spline'.

The function $\pmb { s }$ is a perfect spline of degree $( k + 1 )$ on the interval $[ a , b ] ,$ if it is a spline of degree $( k + 1 )$ ,and if the constant sections of $\pmb { s } ^ { ( k + 1 ) }$ all have the same absolute value. Thus the equation

$$
{ \big | } s ^ { ( k + 1 ) } ( x ) { \big | } = \| s ^ { ( k + 1 ) } \| _ { \infty } , \qquad a \leqslant x \leqslant b ,
$$

is satisfied, except perhaps at the knots of $\pmb { S } .$ If $\pmb { s }$ is a perfect spline of degree $( k + 1 )$ , we adopt the convention that a point of $[ a , b ]$ is a knot of $\pmb { s }$ ， onlifitistetfetedf $\pmb { s } ^ { ( k + 1 ) }$ actually changes sign at the point. It is convenient sometimes,for example in the statement of Theorem 23.4, to call an element of $\mathcal { P } _ { k + 1 }$ a perfect spline of degree $( k + 1 )$

# Theorem 23.4

Let the function values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ be given, where the abscissae satisfy condition (23.1),and let $k$ be an integer in $[ 1 , m - 2 ]$ Let $\pmb { \mathcal { A } }$ be the set of functions that have bounded $( k + 1 )$ th derivatives,and that interpolate the data. The function $\pmb { s }$ in $\mathscr { A }$ gives the least value of the derivative norm $\big \{ \big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ; \boldsymbol { s } \in \mathcal { A } \big \}$ ,if andonlyifthereexistdata points $x _ { q }$ and $x _ { r } ,$ such that $r - q \geqslant k + 1$ ,and such that,on the interval $[ x _ { q } , x _ { r } ] _ { : }$ sisa perfect spline of degree $( k + 1 )$ that satisfies the following two conditions. The equation

$$
\begin{array} { r } { \big | s ^ { ( k + 1 ) } ( x ) \big | = \big \| s ^ { ( k + 1 ) } \big \| _ { \infty } , \qquad x _ { q } < x < x _ { r } , } \end{array}
$$

holds,except perhaps at the knots of $\pmb { s }$ ,where the norm on the right-hand side refers to the whole interval $[ a , b ] ,$ and $\pmb { S }$ has at most $( r - q - k - 1 )$ knots in the range $( x _ { q } , x _ { r } )$

Proof. First we consider the case when $\pmb { s }$ minimizes $\big \{ \big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ; \boldsymbol { s } \in \mathcal { A } \big \}$ The function z = s(k+1) gives the least value of expression (23.37) subject to the constraints (23.38), because otherwise,if $\bar { z }$ is a solution to this optimization problem,then,by integrating $\bar { z } \ \left( k + 1 \right)$ times,as in the solution to the variational problem of Section 23.1, we obtain an element of $\mathscr { A }$ whose $( k + 1 ) \operatorname { t h }$ derivative is smaller than $s ^ { ( k + 1 ) }$ . It follows from the discussion at the beginning of this section that there is a function $\pmb { \eta }$ of the form (23.41), that is not identically zero, sich that, if $\pmb \theta$ is any point of $[ a , b ]$ at which $\pmb { \eta } ( \pmb \theta )$ is non-zero, then $z ( \theta )$ has the value (23.42). We let $x _ { 0 }$ and $x _ { m + 1 }$ be fixed points that are less than $x _ { 1 }$ and greater than $x _ { m }$ respectively,and, if necessary,we extend the definition (23.41） to the range $[ x _ { 0 } , x _ { m + 1 } ]$ .Hence there exist integers $\pmb q$ and $r$ in the interval $[ 1 , m ] ,$ such that $\pmb { \eta }$ has a finite number of zeros in the range $( x _ { q } , x _ { r } )$ ,but $\eta$ is identically zero on $[ x _ { q - 1 } , x _ { q } ]$ and $[ x _ { r } , x _ { r + 1 } ]$ .Because $z = s ^ { ( k + 1 ) }$ , it follows from equation (23.42) that $\pmb { s }$ is a perfect spline of degree $( k + 1 )$ on the interval $[ x _ { q } , x _ { r } ] ,$ ,and that condition (23.44) is satisfied, except perhaps at the knots of $\pmb { S } ,$ ，Further,by applying Theorem 19.1 to $\pmb { \eta }$ ，the condition $r \geq ( q + k + 1 )$ holds,and the number of zeros of $\pmb { \eta }$ in $( x _ { q } , x _ { r } )$ is at most $( r - q - k - 1 )$ .Equation (23.42) shows that these zeros are the only points at which z = s(k+1) can change sign. Hence $\pmb { \mathscr { s } }$ has at most $( r - q - k - 1 )$ knots in the range $( x _ { q } , x _ { r } )$ , which completes one of the two parts of the proof.

To prove the second part of the theorem, we let $\pmb { s }$ be an element of $\mathcal { A }$ ， that is a perfect spline of degree $( k + 1 )$ on the interval $[ x _ { q } , x _ { r } ] ,$ ，where $r - q \geqslant k + 1$ ，where equation (23.44） holds,and where $\pmb { s }$ has at most $( r - q - k - 1 )$ knots in $( x _ { q } , x _ { r } )$ . We have to show that $\big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty }$ is as small as possible.It follows from the remarks on duality, that are made before the statement of the theorem, that it is sufficient to find a non-zero function of the form (23.41), such that equation (23.42) is satisfied if $\pmb { \eta } ( \pmb \theta )$ is nonzero, where $z$ is still the derivative $\pmb { s } ^ { ( k + 1 ) }$ The relation $\left| z ( \theta ) \right| = \left\| z \right\| _ { \infty }$ that is required by condition (23.42) is obtained from expression (23.44) by choosing $\pmb { \eta }$ so that $\pmb { \eta } ( \pmb \theta )$ is non-zero only if $\pmb \theta$ is in the interval $( x _ { q } , x _ { r } )$ Therefore we have to show that the sign of $\eta ( \theta )$ can satisfy equation (23.42).

There is no loss of generality in increasing the integer $q$ and in decreasing the integer $r$ ,until the difference $( r - q )$ is as small as possible, subject to the condition $r - q \geqslant k + 1$ , and subject to the number of knots of $\pmb { s }$ in $( x _ { q } , x _ { r } )$ being not more than $( r - q - k - 1 )$ . We assume that this is done. The number of knots is equal to $( r - q - k - 1 )$ ,because otherwise a further reduction in $\left( r - q \right)$ can be made. If the number of knots is zero, then $\boldsymbol { s } ^ { ( k + 1 ) } = \boldsymbol { z }$ is constant on the interval $( x _ { q } , x _ { r } )$ . Therefore the required sign of $\pmb { \eta }$ can be obtained by letting $\pmb { \eta }$ be a non-zero multiple of the $\pmb { B }$ -spline $\left\{ B _ { q } ( \vartheta ) ; a \leqslant \theta \leqslant b \right\}$ ,which has the form (23.41).Because $\eta ( \theta )$ is zero when $\pmb \theta$ is not in $( x _ { q } , x _ { r } )$ , the theorem is proved in the special case when $r - q = k + 1$

When $( r - q - k - 1 )$ is positive, we let the knots of $\pmb { s }$ in $( x _ { q } , x _ { r } )$ have the values $\{ \xi _ { j } ; j = q , q + 1 , \ldots , r - k - 2 \}$ .Because the assumption that is made in the previous paragraph prevents an increase in $q$ to $( j + 1 )$ ,where $j$ is any one of the integers $\{ q , q + 1 , \dots , r - k - 2 \}$ ,the spline $\pmb { s }$ has at least $( r - j - k - 1 )$ knots in $\left( x _ { j + 1 } , x _ { r } \right)$ .Hence the inequality $\xi _ { j } > x _ { j + 1 }$ is satisfied. By giving similar consideration also to the possibility of decreasing $r _ { \mathrm { { : } } }$ it follows that the bounds

$$
x _ { j + 1 } < \xi _ { j } < x _ { j + k + 1 } , \qquad j = q , q + 1 , \ldots , r - k - 2 ,
$$

are obtained. We require a function of the form

$$
\eta ( \theta ) = \sum _ { p = q } ^ { r - k - 1 } \lambda _ { p } B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

that changes sign at the knots $\{ \xi _ { j } ; j = q , q + 1 , \ldots , r - k - 2 \}$ . Therefore it must satisfy the conditions

$$
\eta ( \xi _ { j } ) = 0 , \qquad j = q , q + 1 , \ldots , r - k - 2 ,
$$

where some or all of the parameters $\left\{ \lambda _ { p } ; p = q , q + 1 , \ldots , r - k - 1 \right\}$ are non-zero,which is possible because there are fewer conditions than parameters. Expression (23.45) is useful, for it implies that the knots $\{ \xi _ { j } ; j = q , q \ { \scriptscriptstyle \circ } \ i , \ldots , r - k - 2 \}$ are the only zeros of the function (23.46) in the interval $( x _ { q } , x _ { r } )$

In order to prove this statement, we suppose that $\pmb { \xi }$ is another zero, and we let $\{ \zeta _ { p } ; p = q , q + 1 , \ldots , r - k - 1 \}$ be the numbers $\pmb { \xi }$ and $\{ \xi _ { j } ; j = q ,$ $q + 1 , \ldots , r - k - 2 \}$ ，arranged in ascending order. It follows from expression (23.45） and from the form of $\pmb { B }$ -splines that the numbers $\{ B _ { p } ( \zeta _ { p } ) ; p = q , q + 1 , \ldots , r - k - 1 \}$ are all non-zero. Therefore Theorem 19.4 states that there is exactly one set of parameters $\{ \mu _ { p } ; p = q , q + 1$ ， $\ldots , r - k - 1 \}$ that satisfies the equations

$$
\sum _ { p = q } ^ { r - k - 1 } \mu _ { p } B _ { p } ( \zeta _ { j } ) = 0 , \qquad j = q , q + 1 , \ldots , r - k - 1 .
$$

This is a contradiction, because, in addition to the trivial solution $\{ \mu _ { p } =$ $0 ; p = q , q + 1 , \ldots , r - k - 1 \}$ ，the points $\{ \zeta _ { i } ; j = q , q + 1 , \ldots , r - k - 1 \}$ are all zeros of the function (23.46). Hence the zeros of $\pmb { \eta }$ in $( x _ { q } , x _ { r } )$ are just the points $\{ \xi _ { i } ; j = q , q + 1 , \ldots , r - k - 2 \}$

Finally, we have to show that $\pmb { \eta }$ changes sign at the zeros $\{ \xi _ { j } ; j = q , q + 1$ ， $\cdots , r - k - 2 \}$ . Because the work of the last paragraph rules out the possibility that $\pmb { \eta }$ is identically zero on a subinterval of $( x _ { q } , x _ { r } )$ ,and because $\pmb { \eta }$ has the form (23.46), the method of proof of Theorem 19.1 may be applied to $\pmb { \eta }$ on $[ x _ { q } , x _ { r } ]$ .Hence the total number of zeros inside the interval does not exceed $( r - q - k - 1 )$ ,even if zeros at which $\pmb { \eta }$ does not change sign are counted twice. It follows that the points $\{ \xi _ { j } ; j = q ,$ $q + 1 , \ldots , r - k - 2 \}$ are all simple zeros.Hence,in $( x _ { q } , x _ { r } )$ ，the sign changes of the function (23.46) occur at the same points as the sign changes of $\pmb { s } ^ { ( k + 1 ) }$ .Therefore,because $\pmb { \eta }$ is identically zero outside $( x _ { q } , x _ { r } )$ ， and because equation (23.44) is satisfied, it is possible to choose $\pmb { \eta }$ so that condition (23.42) is obtained for all values of $\pmb \theta$ in $[ a , b ]$ at which $\pmb { \eta } ( \pmb \theta )$ is non-zero.The theorem is proved.□

Although the variational problem of Theorem 23.2 always has a unique solution, there can be many functions $\pmb { s }$ in the set $\mathcal { A }$ of Theorem 23.4 that minimize $\big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty }$ . For example, if $k = 0$ , and if the data have the values that are shown by the small circles in Figure 23.1,then both the dashed and the solid lines of the figure minimize $\| s ^ { \prime } \| _ { \infty }$ ,where the two lines coincide between the third and fourth data points. The solid line shows the only perfect spline of degree one on the interval $[ x _ { 1 } , x _ { m } ] ;$ , that solves the variational problem and that has not more than $( m - 2 )$ krots.

More generally, if $k \geqslant 0$ ,if $m \geq k + 2$ ,and if condition (23.1) is satisfied, there is a perfect spline of degree $( k + 1 )$ on the full range $[ a , b ]$ ，that interpolates the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , m \}$ ,and that has not more than $( m - k - 2 )$ knots. Theorem 23.4 states that this perfect spline minimizes $\big \{ \big \| \boldsymbol { s } ^ { ( k + 1 ) } \big \| _ { \infty } ; s \in \mathcal { A } \big \}$ . References to proofs of the existence of the perfect spline are given in Appendix B.A condition for uniqueness is the subject ofExercise 23.10.

A strong disadvantage of using a perfect spline of degree $( k + 1 )$ to approximate a function $f$ in $\mathcal { C } [ a , b ]$ is that, if it is necessary for the $( k { + } 1 )$ th derivative of the spline to be large on a part of $[ a , b ] ,$ then, by the definition of a perfect spline, the derivative is large throughout the range. This disadvantage is shown in Figure 23.1. However， some of the theoretical properties of perfect splines are useful. In particular they give error bounds on the interpolation method that is considered in the next chapter.

# 23 Exercises

23.1 Prove that, if $f$ is a function in $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ]$ that has the values $f ( 0 ) = 0 , f ( \textstyle { \frac { 1 } { 2 } } ) = 1$ and $f ( 1 ) = 1$ , then the inequality

$$
\int _ { 0 } ^ { 1 } { [ f ^ { \prime \prime } ( x ) ] ^ { 2 } } \mathrm { d } x \geqslant 1 2
$$

holds.

23.2 Let the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy condition (19.1),and let $f$ be a function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ Prove that there is a spline, $s ^ { * }$ say， in the space $\mathcal { S } ( 2 k + 1 , \xi _ { 0 } , \xi _ { 1 } , . ~ . ~ . , \xi _ { n } )$ that satisfies the equations $\{ s ^ { * } ( \xi _ { i } ) = f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n \}$ $\{ s ^ { * ^ { ( j ) } } ( a ) = f ^ { ( j ) } ( a ) ; j = 1 , 2 , \ldots , k \} _ { \mathrm { \scriptsize {  } } }$ and $\{ s ^ { * ( j ) } ( b ) = f ^ { ( j ) } ( b ) ; j = 1 , 2 , \ldots , k \}$ Prove also that $s ^ { * }$ minimizes the integral

![](../chunks/Approximation Theory and Methods (Michael James David Powell) (z-library.sk, 1lib.sk, z-li_part_0005_pages_0281-0350/auto/images/9188c47b2308605878f1264b8ed58c6fb043d777d330d280efb0f25f4625ba64.jpg)  
Figure 23.1. Two solutions to a variational problem.

$$
\int _ { a } ^ { b } \left[ f ^ { ( k + 1 ) } ( x ) - s ^ { ( k + 1 ) } ( x ) \right] ^ { 2 } \mathrm { d } x , \qquad s \in \mathcal { S } ( 2 k + 1 , \xi _ { 0 } , \xi _ { 1 } , . . . , \xi _ { n } ) .
$$

23.3 Verify that the coefficients $w _ { 0 } , w _ { 1 }$ and $w _ { 3 }$ that solve Exercise 22.3 are such that $\left[ w _ { 0 } f ( 0 ) + w _ { 1 } f ( 1 ) + w _ { 3 } f ( 3 ) \right]$ is the value at $\scriptstyle x = 2$ of the natural cubic spline that interpolates $f ( 0 ) , f ( 1 )$ and $f ( 3 )$

23.4 Let $f$ be a function in $\mathcal { C } ^ { ( 3 ) } [ - 2 , 2 ]$ that has the values $f ( - 2 ) =$ $f ( - 1 ) = f ( 1 ) = f ( 2 ) = 0$ and $f ( 0 ) = 1$ . Show that the inequality $\| f ^ { \prime \prime \prime } \| _ { \infty } \geqslant 4 . 5$ is satisfied. If it is known also that $f ^ { \prime } ( - 2 ) = f ^ { \prime } ( 2 ) = 0 { \mathrm { . } }$ ， show that the lower bound on $\| f ^ { \prime \prime \prime } \| _ { \infty }$ may be increased to 6.425 ...,which is the number $( 2 3 1 + 9 \sqrt { 3 3 } ) / 4 4$

23.5 Let $m = 4$ and $k = 1$ in the statement of Theorem 23.4,and let $s ^ { * }$ be the function in $\mathcal { A }$ that minimizes $\big \{ \big \| \boldsymbol { s } ^ { \prime \prime } \big \| _ { \infty } ; s \in \mathcal { A } \big \}$ . Prove that the inequality

$$
{ \| s ^ { * } \prime \prime \| _ { \infty } } { \leqslant } 4 \operatorname* { m a x } { \{ \left| f [ x _ { 1 } , x _ { 2 } , x _ { 3 } ] \right| , \left| f [ x _ { 2 } , x _ { 3 } , x _ { 4 } ] \right| \} }
$$

holds,and that, if $f$ can be any function in $\mathcal { C } [ a , b ] ,$ ，then the constant 4 on the right-hand side cannot be replaced by a smaller number.

Calculate the function $\pmb { s }$ in $\mathcal { C } [ 0 , 2 ]$ that minimizes the integral

$$
\int _ { 0 } ^ { 2 } \{ [ s ^ { \prime \prime } ( x ) ] ^ { 2 } / ( 1 + x ) \} \mathrm { d } x ,
$$

subject to the conditions $s ( 0 ) = 0 , s ( 1 ) = 0$ and $s ( 2 ) = 1 6$ .You should find the piecewise polynomial

$$
s ( x ) = { \Big \{ } _ { 6 - 1 9 x + 1 2 x ^ { 2 } + 2 x ^ { 3 } - x ^ { 4 } , 1 \leqslant x \leqslant 2 . } ^ { - 3 x }  ^ { - 3 x } \qquad \leqslant x \leqslant 1 .
$$

23.7 Let $\pmb { \sigma }$ be the spline in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ that minimizes the integral

$$
\| g - s \| _ { 2 } ^ { 2 } = \int _ { a } ^ { b } \left[ g ( x ) - s ( x ) \right] ^ { 2 } \mathrm { d } x , \qquad s \in \mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } ) ,
$$

where inequality (19.1) holds,and where $\pmb { g }$ is any fixed function in $\mathcal { C } [ a , b ]$ .If $f$ is a $( k + 1 )$ -fold integral of $\pmb { g } .$ and if $s ^ { * }$ is the spline in $\mathcal { S } ( 2 k + 1 , \xi _ { 0 } , \xi _ { 1 } , . ~ . ~ . , \xi _ { n } )$ that is defined in Exercise 23.2, then $\pmb { \sigma }$ is equal to $\pmb { s } ^ { * ( k + 1 ) }$ . Prove that,if it isnot possible toreduce the error $\| g - \sigma \| _ { 2 }$ by altering the positions of the interior knots $\{ \xi _ { i } ; i = 1 , 2 , \ldots , n - 1 \}$ ,then,not only does $s ^ { * }$ satisfy the equations of Exercise 23.2，but also the derivative conditions $\{ s ^ { * } { } ^ { \prime } ( \xi _ { i } ) = f ^ { \prime } ( \xi _ { i } ) ; i = 1 , 2 , . . . , n - 1 \}$ are obtained.

23.8Let the points $\{ x _ { i } ; i = 0 , 1 , \ldots , n \}$ of the quadrature formula

$$
\int _ { x _ { 0 } } ^ { x _ { n } } f ( x ) { \mathrm { d } } x \approx \sum _ { i = 0 } ^ { n } w _ { i } f ( x _ { i } ) , \qquad f \in \mathcal { C } ^ { ( 2 ) } [ x _ { 0 } , x _ { n } ] ,
$$

satisfy the conditions $\{ x _ { i } = x _ { 0 } + i h ; i = 1 , 2 , \dots , n \}$ ，and let the weights $\{ w _ { i } ; i = 0 , 1 , \ldots , n \}$ have the values that minimize the multiple of $\left\| f ^ { \prime \prime } \right\| _ { 2 }$ that bounds the error of the quadrature formula. Show that $w _ { 0 } = w _ { n }$ ,and that the equations

$$
w _ { i } = h [ 1 + \beta ( \sqrt { 3 - 2 } ) ^ { i } + \beta ( \sqrt { 3 - 2 } ) ^ { n - i } ] , \qquad i = 1 , 2 , \ldots , n - 1 ,
$$

are obtained, where $\beta$ is a number that does not depend on $i ,$

23.9 Prove the necessary and sufficient conditions that are stated in the sentence that follows inequality (23.40).

.10Let the conditions of Theorem 23.4 be satisfied,and let $\bar { \mathcal { A } }$ be the set of perfect splines of degree $( k + 1 )$ on the full range $[ a , b ]$ ,that interpolate the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ ，and that have not more than $( m - k - 2 )$ knots. Let $\bar { s }$ be an element of $\{ { \bar { \alpha } } ,$ let $z$ be the derivative s(k+1), ，and let the function (23.41） have the property that equation (23.42) is satisfied for all points $\pmb \theta$ in $[ a , b ]$ at which $\eta ( \theta )$ is non-zero.Prove that,if $\pmb { \eta }$ has only a finite number of zeros in $[ a , b ] ,$ ,then $\bar { s }$ is the only element of $\boldsymbol { \bar { \mathcal { A } } } .$ Express this condition as a relation between the knots of $\bar { s }$ and the positions of the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ . Investigate relations between the knots of $\pmb { \bar { s } }$ and the data points that allow $\bar { \mathcal { A } }$ to contain more than one element.

# Optimal interpolation

# 24.1 The optimal interpolation problem

If one is given many values $\{ f ( x _ { i } ) ; i = 1 , 2 , \dots , m \}$ of a function $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ if it is known that $\| f ^ { ( k + 1 ) } \| _ { \infty }$ is not very large,and if an estimate of $f ( \xi )$ is required, where $\xi$ is any point of $[ a , b ] ,$ , then one may make an approximation of the form

$$
f ( \xi ) \approx \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) ,
$$

where the multipliers $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ are such that the approximation is exact when $f$ is in $\mathcal { P } _ { k }$ . In this case the Peano kernel theorem shows that there is a number $^ c$ ,that is independent of $f ,$ such that the bound

$$
\bigg | f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) \bigg | \leqslant c \big \| f ^ { ( k + 1 ) } \big \| _ { \infty } , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,
$$

is satisfied. When $m > k + 1$ ,there is some freedom in the values of the multipliers. If this freedom is used to minimize $^ c$ ，the approximation (24.1) is said to be ‘optimal'. We reserve the notation $\{ w _ { i } ( \pmb { \xi } ) ; i = 1$ ,2, $\cdots , m \}$ for the optimal multipliers, we let $s ( \xi )$ be the optimal estimate

$$
s ( \xi ) = \sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) f ( x _ { i } ) , \qquad a \leqslant \xi \leqslant b ,
$$

of $f ( \xi )$ ，and we let $c ( \xi )$ be the least value of $c$ 、We find later that the optimal multipliers are unique for each $\xi .$

Because the optimal interpolation procedure can be applied for all values of $\xi \mathrm { i n } [ a , b ] ,$ ,the function (24.3) can be regarded as an approximation to the function $\{ f ( x ) ; a \leqslant x \leqslant b \}$ .It is shown in Section 24.3 that this approximation is a spline of degree $k$ that has $( m - k - 1 )$ knots whose positions are independent of $f .$ It is highly satisfactory that $\pmb { s }$ is a spline of the lowest degree that is allowed by an error bound of the form (24.2).We recall,however, that natural splines that are obtained by minimizing the number $\boldsymbol { c } _ { 2 }$ in the bound

$$
{ \biggl | } f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) { \biggr | } \leqslant c _ { 2 } \| f ^ { ( k + 1 ) } \| _ { 2 }
$$

are less convenient, because they are of degree $( 2 k + 1 )$ ,and because their end conditions force errors to occur when $f$ is in $\mathscr { P } _ { 2 k + 1 }$ but not in $\mathcal { P } _ { k }$ ·

Another remark that we recall from Section 23.2 is that the minimization of $c _ { 2 }$ gives the same estimate of $f ( \xi )$ as the solution to the variational problem of Theorem 23.2.If an analogous result were true when $\| f ^ { ( k + 1 ) } \| _ { 2 }$ is replaced by $\| f ^ { ( k + 1 ) } \| _ { \infty }$ , then,by Theorem 23.4,the function (24.3) would be a perfect spline of degree $( k + 1 )$ on a subinterval of $[ a , b ] _ { \mathrm { : } }$ ，but the degree of $\pmb { s }$ is only $k$ .Nevertheless, the properties of perfect splines are important to optimal interpolation.In particular, it willbe shown that the function $\{ c ( \pmb { \xi } )$ ； $a \leqslant \xi \leqslant b \}$ is the modulus of a perfect spline of degree $( k + 1 )$

When $\pmb { \xi }$ is a variable whose range is $[ a , b ] ,$ ,then the functions $\{ w _ { i } ; i = 1$ ， $2 , \ldots , m \}$ in expression (24.3) are the cardinal functions of the optimal interpolation procedure. We have called $w _ { i } ( \xi )$ a multiplier, however, instead of a cardinal function, because, from now until the beginning of Section $2 4 . 3 , \xi$ is treated as a fixed point of $[ a , b ]$ .The main properties of optimal interpolation are derived from the following theorem.

# Theorem 24.1

Let the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ satisfy the conditions

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b ,
$$

let $\xi$ be any point of $[ a , b ] ,$ and let $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ be multipliers, such that the estimate (24.1) is exact when $f$ is in $\mathcal { P } _ { k }$ .Let $\pmb { K }$ be the kernel function

$$
K ( \theta ) = \frac { 1 } { k ! } \Bigl [ ( \xi - \theta ) _ { + } ^ { k } - \sum _ { i = 1 } ^ { m } w _ { i } ( x _ { i } - \theta ) _ { + } ^ { k } \Bigr ] , \qquad a \leqslant \theta \leqslant b .
$$

Then the multipliers have the values that minimize the constant $^ c$ in inequality (24.2),if and only if they minimize the norm

$$
\| K \| _ { 1 } = \int _ { a } ^ { b } \left| K ( \theta ) \right| \mathrm { d } \theta .
$$

Proof.Theorem 22.1 implies the equation

$$
f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } f ( x _ { i } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) { \mathrm { d } } \theta , \qquad f \in { \mathcal { C } } ^ { ( k + 1 ) } [ a , b ] .
$$

Hence,for any particular choice of the multipliers,the least constant $c$ in inequality (24.2) has the value (24.7). It follows that the problems of choosing the multipliers to minimize $c$ and to minimize $\left\| K \right\| _ { 1 }$ are equivalent.□

In order to minimize $\left\| K \right\| _ { 1 }$ , we make use of an idea that is given in Chapter 22. It is to express the approximation (24.1) in the form

$$
f ( \xi ) \approx \sum _ { i = 1 } ^ { k + 1 } u _ { i } f ( x _ { i } ) + \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } f [ x _ { p } , x _ { p + 1 } , \ldots , x _ { p + k + 1 } ] ,
$$

where $f [ x _ { p } , x _ { p + 1 } , \dotsc , x _ { p + k + 1 } ]$ is a divided difference. This approximation is exact when $f$ is in $\mathcal { P } _ { k }$ , if and only if the coefficients $\{ u _ { i } ; i = 1 , 2 , \ldots ,$ $k + 1 \}$ satisfy the condition

$$
f ( \xi ) = \sum _ { i = 1 } ^ { k + 1 } u _ { i } f ( x _ { i } ) , \qquad f \in \mathcal { P } _ { k } .
$$

Because the right-hand side of this condition can only be the value at $\xi$ of the polynomial in $\mathcal { P } _ { k }$ that interpolates the data $\{ f ( x _ { i } ) ; i = 1 , 2 , \ldots , k + 1 \} _ { } ,$ it follows that, as in equation (22.43),the identity

$$
f ( \xi ) - \sum _ { i = 1 } ^ { k + 1 } u _ { i } f ( x _ { i } ) = \bigg \{ \prod _ { i = 1 } ^ { k + 1 } { ( \xi - x _ { i } ) \bigg \} } f [ x _ { 1 } , x _ { 2 } , \ldots , x _ { k + 1 } , \xi ]
$$

holds for all functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .Therefore the error of the estimate (24.9) is the expression

$$
\begin{array} { r l r } {  { \bigg \{ \prod _ { i = 1 } ^ { k + 1 } ( \xi - x _ { i } ) \bigg \} f [ x _ { 1 } , x _ { 2 } , \dots , x _ { k + 1 } , \xi ] } } \\ & { } & { - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } f [ x _ { p } , x _ { p + 1 } , \dots , x _ { p + k + 1 } ] . } \end{array}
$$

Theorem 22.3 shows that, when $f$ is in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,$ this expression may be written in the form

$$
\frac { 1 } { k ! } \int _ { a } ^ { b } \bigg [ \bigg \{ \prod _ { i = 1 } ^ { k + 1 } \left( \xi - x _ { i } \right) \bigg \} B ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } B _ { p } ( \theta ) \bigg ] f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta ,
$$

where the knots of the $B$ -splines are the arguments of the corresponding divided differences.It follows from Theorem 24.1 that the approximation (24.9) is the optimal interpolation formula, if and only if the coefficients $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ minimize the norm

$$
\int _ { a } ^ { b } | { \Big \{ } \prod _ { i = 1 } ^ { k + 1 } { ( \xi - x _ { i } ) } { \Big \} } B ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } B _ { p } ( \theta ) { \Big | } \ \mathbf { d } \theta .
$$

Thus the optimal interpolation problem is equivalent to calculating the best $L _ { 1 }$ approximation to the function $\left\{ B ( \theta ) ; \ a \leqslant \theta \leqslant b \right\}$ by a linear combination of the $B$ -splines $\{ B _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \} .$

# $2 4 . 2 \ L _ { 1 }$ approximation by $\pmb { B }$ -splines

The main result of this section is that the required parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ in expression (24.14） are defined by the linear equations

$$
\sum _ { p = 1 } ^ { m - k - 1 } v _ { p } B _ { p } ( \xi _ { j } ) = \bigg \{ \prod _ { i = 1 } ^ { k + 1 } ( \xi - x _ { i } ) \bigg \} B ( \xi _ { j } ) , \qquad j = 1 , 2 , \ldots , m - k - 1 ,
$$

where the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are independent of $\xi .$ The result is a corollary of Theorem 14.4, but this theorem requires the set of approximating functions to be a Chebyshev set. Therefore it is necessary to show that the $B$ -splines $\{ B _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ are sufficiently close to a Chebyshev set for Theorem 14.4 to be useful.

# Theorem 24.2

Let $k$ and $_ { m }$ be positive integers such that $m > k + 1$ , let the points $\{ x _ { i } ; \ i = 1 , 2 , \dots , m \}$ satisfy condition (24.5)，and for $1 \leqslant p \leqslant$ $m - k - 1$ let $\scriptstyle B _ { p }$ be the $\pmb { B }$ -spline

$$
B _ { p } ( \theta ) = \sum _ { i = p } ^ { p + k + 1 } \bigg \{ ( \theta - x _ { i } ) _ { + } ^ { k } \bigg / \prod _ { \stackrel { j = p } { j \neq i } } ^ { p + k + 1 } ( x _ { j } - x _ { i } ) \bigg \} , \qquad a \leqslant \theta \leqslant b .
$$

For any $\varepsilon > 0$ ,there exists a Chebyshev set of functions $\{ \phi _ { p } ; p = 1 , 2 $ $\ldots , m - k - 1 \}$ such that the inequalities

$$
\| B _ { p } - \phi _ { p } \| _ { \infty } \leqslant \varepsilon , \qquad p = 1 , 2 , \ldots , m - k - 1 ,
$$

hold.

Pro0f. Let $q = m - k - 1$ , and let $\psi$ be the function

$$
\psi ( \alpha ) = M \mathrm { e } ^ { - \pi M ^ { 2 } \alpha ^ { 2 } } , \qquad - \infty < \alpha < \infty ,
$$

where $M$ is a parameter. For $p = 1 , 2 , \ldots , q ;$ we let $\phi _ { p }$ have the form

$$
\phi _ { p } ( \theta ) = \int _ { - \infty } ^ { \infty } \psi ( \alpha - \theta ) B _ { p } ( \alpha ) \mathrm { d } \alpha , \qquad a \leqslant \theta \leqslant b ,
$$

where $B _ { p } ( \alpha )$ is zero if $\pmb { \alpha }$ is outside $[ a , b ]$ .Because the area under the curve $\{ \psi ( \alpha ) ; - \infty < \alpha < \infty \}$ is one, because $\psi$ tends to a delta function as $M$ tends to infinity,and because the functions $\{ B _ { p } ; p = 1 , 2 , \ldots , q \}$ are continuous and bounded,we can choose $M$ to be so large that the conditions (24.17) are satisfied for any fixed positive value of $\pmb \varepsilon$ .Therefore it is sufficient to prove that the set $\{ \phi _ { p } ; p = 1 , 2 , \ldots , q \}$ is a Chebyshev set. We show that property (4) of Section 7.3 is obtained,which is that, if the numbers $\{ \theta _ { j } ; j = 1 , 2 , \ldots , q \}$ satisfy the inequalities

$$
a \leqslant \theta _ { 1 } < \theta _ { 2 } < . . . < \theta _ { q } \leqslant b ,
$$

then the $q \times q$ matrix $\pmb { A }$ ,whose elements have the values $A _ { p j } = \phi _ { p } ( \theta _ { j } )$ ,is non-singular.

Because $B _ { p } ( \alpha )$ is zero unless $_ \alpha$ is in the interval $( a , b )$ , the matrix $\pmb { A }$ has the form

$$
\begin{array}{c} \begin{array} { r l } {  \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 1 } - \theta _ { 1 } ) B _ { 1 } ( \alpha _ { 1 } ) \mathrm { d } \alpha _ { 1 }  } & { \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 2 } - \theta _ { 2 } ) B _ { 1 } ( \alpha _ { 2 } ) \mathrm { d } \alpha _ { 2 } . . . } \\ {  \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 1 } - \theta _ { 1 } ) B _ { 2 } ( \alpha _ { 1 } ) \mathrm { d } \alpha _ { 1 }  } & { \displaystyle \int _ { a } ^ { b } \psi ( \alpha _ { 2 } - \theta _ { 2 } ) B _ { 2 } ( \alpha _ { 2 } ) \mathrm { d } \alpha _ { 2 } . . . } \\ { \vdots } & { \vdots } \end{array} ) .  \end{array}
$$

We consider the value of its determinant. If all of the columns of $\pmb { A }$ are fixed except for the jth column, then the determinant is a linear functional of the jth column.It follows that the integral over $\alpha _ { j }$ can be taken outside the determinant, and this can be done for each $j .$ Hence we obtain the identity

$$
\operatorname* { d e t } A = \int _ { a } ^ { b } \cdot \cdot \cdot \int _ { a } ^ { b } \bigg \{ \prod _ { j = 1 } ^ { q } \psi ( \alpha _ { j } - \theta _ { j } ) \bigg \} \operatorname* { d e t } H \mathrm { d } \alpha _ { 1 }  \cdot \cdot \cdot \mathrm { d } \alpha _ { q } ,
$$

where $H$ is the $q \times q$ matrix whose elements are $H _ { p j } = B _ { p } ( \alpha _ { j } )$ .Because the numbers $\{ \psi ( \alpha _ { j } - \theta _ { j } ) ; j = 1 , 2 , \ldots , q \}$ are all positive,and because det $\pmb { H }$ is a continuous function of the variables $\{ \alpha _ { j } ; j = 1 , 2 , \ldots , q \}$ ,it is sufficient to prove that det $\pmb { H }$ is not identically zero and does not change sign in the range of integration of expression (24.22).

The matrix $H$ is similar to the one that occurs in the linear system of equations (19.37) of the Schoenberg-Whitney theorem. It follows from the proof of Theorem 19.4 that det $H ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { q } )$ is non-zero if and only if the numbers $\{ B _ { p } ( \alpha _ { p } )$ ； $p = 1 , 2 , \ldots , q \}$ are all positive. If det $H ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { q } )$ is positive, but det $H ( \beta _ { 1 } , \beta _ { 2 } , \dots , \beta _ { q } )$ is negative, then，by continuity， there exists a number $r$ in [O,1] such that det $H ( \gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { q } )$ is zero， where $\begin{array} { r } { \{ \gamma _ { p } = r \alpha _ { p } + ( 1 - r ) \beta _ { p } } \end{array}$ ； $p = 1$ ,2, $\cdots , q \}$ . However, because $B _ { p } ( \alpha _ { p } )$ and $B _ { p } ( \beta _ { p } )$ are both positive,and because $\scriptstyle B _ { p }$ is a $\pmb { B }$ -spline, the number $B _ { p } ( \gamma _ { p } )$ must also be positive for $p = 1 , 2 , \ldots , q ;$ ，which gives a contradiction. Hence det $\pmb { H }$ does not change sign in the range of the integral (24.22). The theorem is proved.□

In order to apply Theorem 14.4 to the minimization of expression (24.14), we let $\xi$ be a point of $[ a , b ]$ that is not in the set $\left\{ x _ { i } ; ~ i = \right.$

$1 , 2 , \ldots , m \}$ ，we let $M$ be a large number,we define the functions $\{ \phi _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ by equation (24.19), and we let $\phi$ be the function

$$
\phi \left( \theta \right) = \int _ { a } ^ { b } \psi ( \alpha - \theta ) ~ B \left( \alpha \right) \mathrm { d } \alpha , \qquad a \leqslant \theta \leqslant b .
$$

By inserting $\xi$ into the sequence $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ ，it follows from Theorem 24.2 that the linear space that is spanned by the functions $\phi$ and $\{ \phi _ { p } ; ~ p = 1 , 2 , \ldots , m - k - 1 \}$ satisfies the Haar condition. We deduce from Theorem 14.4 that there exist points $\{ \xi _ { j } ( M ) ; j = 1 , 2 , \ldots ,$ $m - k - 1 \}$ ,that are independent of $\xi ,$ such that a necessary and sufficient condition for the coeffcients $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ to minimize the norm

$$
\int _ { a } ^ { b } | { \Big \{ } \prod _ { i = 1 } ^ { k + 1 } { \big ( } \xi - x _ { i } { \big ) } { \Bigg \} } \phi ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } \phi _ { p } ( \theta ) { \Bigg | } \ \mathrm { d } \theta
$$

is that the interpolation conditions

$$
\sum _ { p = 1 } ^ { m - k - 1 } v _ { p } \phi _ { p } ( \xi _ { j } [ M ] ) = \bigg \{ \prod _ { i = 1 } ^ { k + 1 } ( \xi - x _ { i } ) \bigg \} \phi ( \xi _ { j } [ M ] ) ,
$$

$$
j = 1 , 2 , \ldots , m - k - 1 ,
$$

are satisfied. Because $\{ \phi _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ and $\phi$ tend to $\{ B _ { p } ; p =$ $1 , 2 , \ldots , m - k - 1 \}$ and $\pmb { B }$ respectively as $M$ tends to infinity, it seems to be appropriate to let the interpolation points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ of equation (24.15) be a limit of the set $\{ \xi _ { j } ( M ) ; j = 1 , 2 , \ldots , m - k - 1 \}$ as $M$ becomes large, where the inequalities

$$
a \leqslant \xi _ { 1 } ( M ) < \xi _ { 2 } ( M ) < \ldots < \xi _ { m - k - 1 } ( M ) \leqslant b
$$

hold.The remainder of this section shows that it is suitable to define the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ in this way. First it is proved that the matrix of the system of equations (24.15) is non-singular.

# Theorem 24.3

Let the conditions of Theorem 24.2 hold, let $\{ M _ { t } ; t = 1 , 2 , 3 , . . . \}$ be a monotonically increasing divergent sequence of positive real numbers,and let $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ be a limit of the sequence of sets $[ \{ \xi _ { j } ( M _ { t } ) ; j = 1 , 2 , \ldots , m - k - 1 \} ;$ $t = 1 , 2 , 3 , \ldots ] ,$ ,where the numbers $\{ \xi _ { j } ( M _ { t } ) ; j = 1 , 2 , \ldots , m - k - 1 \}$ have just been defined.Then the numbers $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are all different, and they satisfy the conditions

$$
x _ { j } < \xi _ { j } < x _ { j + k + 1 } , \qquad j = 1 , 2 , \ldots , m - k - 1 .
$$

Proof. Let $M$ be any positive number,for $1 \leqslant p \leqslant m - k - 1$ let $\phi _ { p }$ be the function (24.19),and let $z _ { M }$ be the sign function

$$
z _ { M } ( \theta ) = \left\{ \begin{array} { l l } { { 1 , ~ } } & { { a \leqslant \theta < \xi _ { 1 } ( M ) } } \\ { { ( - 1 ) ^ { j } , ~ } } & { { \xi _ { j } ( M ) < \theta < \xi _ { j + 1 } ( M ) , ~ 1 \leqslant j \leqslant m - k - 2 ~ } } \\ { { ( - 1 ) ^ { m - k - 1 } , ~ } } & { { \xi _ { m - k - 1 } ( M ) < \theta \leqslant b } } \\ { { 0 , ~ } } & { { \mathrm { o t h e r w i s e } . } } \end{array} \right.
$$

Theorems 14.1, 14.4 and 24.2 imply that the equations

$$
\int _ { a } ^ { b } z _ { M } ( \theta ) \phi _ { p } ( \theta ) { \mathrm { d } } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - k - 1 ,
$$

hold.By taking the limit as $M$ tends to infinity,it follows that the conditions

$$
\int _ { a } ^ { b } z ( \theta ) B _ { p } ( \theta ) { \mathrm { d } } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - k - 1 ,
$$

are obtained,where $z$ is the function

$$
z \left( \theta \right) = \left\{ \begin{array} { l l } { 1 , \qquad a \leqslant \theta < \xi _ { 1 } } \\ { ( - 1 ) ^ { i } , \qquad \xi _ { j } < \theta < \xi _ { j + 1 } , \qquad 1 \leqslant j \leqslant m - k - 2 } \\ { ( - 1 ) ^ { m - k - 1 } , \qquad \xi _ { m - k - 1 } < \theta \leqslant b } \\ { 0 , \qquad \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

We let $\sigma$ be a perfect spline of degree $( k + 1 )$ that satisfies the equation

$$
\sigma ^ { ( k + 1 ) } ( \theta ) = z ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

except perhaps when $\pmb \theta$ is in the set $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \} .$

The notation $z$ is chosen for the $( k + 1 ) \mathrm { t h }$ derivative of the perfect spline,in order to make use of the second half of the proof of Theorem 23.4. This proof shows that, if there are data points $x _ { q }$ and $x _ { r }$ such that $r - q \geqslant k + 1$ , and such that $\sigma$ has at most $( r - q - k - 1 )$ knots in the range $( x _ { q } , x _ { r } )$ , then there is a function of the form

$$
\eta ( \theta ) = \sum _ { p = q } ^ { r - k - 1 } \lambda _ { p } B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

that is not identically zero,and that has the property that equation (23.42) holds when $\pmb { \eta } ( \pmb \theta )$ is non-zero. Hence the inequality

$$
{ \int _ { a } ^ { b } z ( \theta ) \eta ( \theta ) \operatorname { d } \theta } = { \int _ { a } ^ { b } \left| \eta ( \theta ) \right| \operatorname { d } \theta }
$$

is obtained. This inequality, however, contradicts equations (24.30) and (24.33).Hence there is a relation between the knots of $\sigma$ and the positions of the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ ,which we find is sufficient to complete the proof.

Specifically, because of the possibility that $q = 1$ and $r = m$ , the spline $\sigma$ must have more than $( m - k - 2 )$ knots,which proves that the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are all different. Moreover, if there is an integer $j$ in the range[1, $m - k - 1 ]$ such that $\xi _ { j } \leqslant x _ { j } ,$ then letting $q = j$ and $r = m$ also gives a contradiction. Similarly，by letting $q = 1$ and $r =$ $j + k + 1$ , there is a contradiction if $\pmb { \xi } _ { j } \geq \pmb { x } _ { j + k + 1 }$ .Hence inequality (24.27) is satisfied. The proof is complete.□

We let the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ satisfy the conditions of Theorem 24.3.It follows from Theorem 19.4 that the system of equations (24.15) defines the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ uniquely. We have to show that these parameters are the ones that minimize $\| K \| _ { 1 }$ ， where $\kappa$ is the kernel function

$$
K ( \theta ) = \frac { 1 } { k ! } \biggl [ \Bigl \{ \prod _ { i = 1 } ^ { k + 1 } \left( \xi - x _ { i } \right) \Bigr \} B ( \theta ) - \sum _ { p = 1 } ^ { m - k - 1 } v _ { p } \ B _ { p } ( \theta ) \biggr ] , \qquad a \leqslant \theta
$$

Theorem 14.1 states that it is sufficient to prove that,for any values of the parameters $\{ \lambda _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ ,the function

$$
\eta ( \theta ) = \sum _ { p = 1 } ^ { m - k - 1 } \lambda _ { p } \ B _ { p } ( \theta ) , \qquad a \leqslant \theta \leqslant b ,
$$

satisfies the inequality

$$
\left| \int _ { a } ^ { b } t ( \theta ) \eta ( \theta ) { \bf d } \theta \right| \leqslant \int _ { \mathcal { Z } } \left| \eta ( \theta ) \right| { \bf d } \theta ,
$$

where $t$ is the sign function

$$
t ( \theta ) = \left\{ \begin{array} { r l } { 1 , \quad } & { { } K ( \theta ) > 0 } \\ { 0 , \quad } & { { } K ( \theta ) = 0 \quad } & { a \leqslant \theta \leqslant b , } \\ { - 1 , \quad } & { { } K ( \theta ) < 0 , } \end{array} \right.
$$

and where $\mathcal { Z }$ is the set

$$
{ \mathcal { L } } = \{ \theta colon K ( \theta ) = 0 , a \leqslant \theta \leqslant b \} .
$$

Inequality (24.37） is not a direct consequence of equation (24.30), because of the possibility that $\pmb { K }$ is identically zero on some subintervals of $[ a , b ]$ .We have to apply Theorem 19.1 again. Therefore we let $x _ { 0 }$ and $x _ { m + 1 }$ be fixed points such that the conditions

$$
\left. \begin{array} { l } { x _ { 0 } < \operatorname* { m i n } \left[ x _ { 1 } , \xi \right] } \\ { x _ { m + 1 } > \operatorname* { m a x } \left[ x _ { m } , \xi \right] } \end{array} \right\}
$$

hold,and if necessary we extend the range of $\pmb \theta$ in the definition (24.35) so that it includes the points $x _ { 0 }$ and $x _ { m + 1 }$ ·

The kernel function (24.35) is a spline of degree $k$ whose knots are $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ and $\xi ,$ and,due to equation (24.15),it has zeros at $\{ \xi _ { j }$ ； $j = 1 , 2 , \ldots , m - k - 1 \} .$ If $\pmb { p }$ and $q$ are integers such that $\pmb { K }$ is identically zero on $[ x _ { p - 1 } , x _ { p } ]$ and $[ x _ { q } , x _ { q + 1 } ]$ ,but if $\pmb { K }$ has a finite number of zeros in $( x _ { p } , x _ { q } )$ ,then condition (24.27) implies that the number of zeros in $( x _ { p } , x _ { q } )$ is not less than $( q - p - k )$ . It follows from Theorem 19.1 that $\kappa$ has at least $( q - p )$ knots in $( x _ { p } , x _ { q } )$ . Because only $( q - p - 1 )$ of the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ are in this interval, $\xi$ is also in $( x _ { p } , x _ { q } )$ . Therefore, either $\kappa$ is identically zero,which happens when $\xi$ is in the point set $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ , or there exist numbers $\pmb { \alpha }$ and $\beta$ in $[ a , b ]$ such that $\pmb { K }$ is non-zero only in $( \alpha , \beta )$ ,and in this interval the number of zeros of $\pmb { K }$ is finite.In the first case inequality (24.37) is satisfied because $\{ t ( \theta ) = 0$ ； $a \leqslant \theta \leqslant b \}$ , but the second case requires further consideration.

The only zeros of $\pmb { K }$ in the interval $( \alpha , \beta )$ are in the set $\{ \xi _ { j } ; j = 1$ ， $2 , \ldots , m - k - 1 \}$ ,and all these zeros are simple, because otherwise, by extending the argument of the previous paragraph that depends on Theorem 19.1,we find that $\pmb { K }$ has insufficient knots. It follows from the definitions (24.31） and (24.38) that either $\{ t ( \theta ) = z ( \theta )$ ； $\alpha < \theta < \beta \}$ or $\{ t ( \theta ) = - z ( \theta )$ ： $\alpha < \theta < \beta \}$ . Therefore, because $t$ is zero on $( a , \alpha )$ and $( \beta , b )$ , and because equations (24.30) and (24.36) imply the value

$$
\int _ { a } ^ { b } z \left( \theta \right) \eta \left( \theta \right) { \bf d } \theta = 0 ,
$$

the identity

$$
\begin{array} { l } { { \displaystyle { \left| \int _ { a } ^ { b } t ( \theta ) \eta ( \theta ) { \bf d } \theta \right| = \left| \int _ { \alpha } ^ { \beta } z ( \theta ) \eta ( \theta ) { \bf d } \theta \right| } } } \\ { { \displaystyle { \qquad = \left| \int _ { a } ^ { \alpha } z ( \theta ) \eta ( \theta ) { \bf d } \theta + \int _ { \beta } ^ { b } z ( \theta ) \eta ( \theta ) { \bf d } \theta \right| } } } \end{array}
$$

is satisfied. We note that the set (24.39) contains the intervals $( a , \alpha )$ and $( \beta , b )$ ,and that $\| z \| _ { \infty }$ is one. Hence inequality (24.37) is a consequence of equation (24.42). Therefore equation (24.15) does define the parameters of the optimal interpolation formula.

We require later that the definition (24.38), and the properties of $K , t$ and $z$ that are given in the previous two paragraphs, imply the equation

$$
\begin{array} { c } { \displaystyle \| { \boldsymbol { K } } \| _ { 1 } = \int _ { a } ^ { b } { \boldsymbol { K } } ( \theta ) t ( \theta ) { \mathrm { d } } \theta } \\ { \displaystyle = \left| \int _ { a } ^ { b } { \boldsymbol { K } } ( \theta ) z ( \theta ) { \mathrm { d } } \theta \right| . } \end{array}
$$

# 24.3 Properties of optimal interpolation

Instead of calculating the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ of the optimal interpolation formula from equation (24.15),and then obtaining the coefficients $\{ w _ { i } ( \xi ) ; i = 1 , 2 , \dots , m \}$ from the equivalence of the approximations (24.1) and (24.9), it is better to determine $\{ w _ { i } ( \xi )$ ； $i = 1 , 2 , \ldots , m \}$ directly from the properties that define the optimal values of $\{ u _ { i } ; i = 1 , 2 , \ldots , k + 1 \}$ and $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ .These properties are that equation (24.1O) must hold,and that the kernel function (24.35) is zero when $\{ \theta = \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ ,where the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are independent of $\xi .$ Because equation (24.10) states that the approximation (24.1) is exact when $f$ is in $\mathcal { P } _ { k } ,$ it is equivalent to the conditions

$$
\sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) x _ { i } ^ { r } = \xi ^ { r } , \qquad r = 0 , 1 , \ldots , k ,
$$

and, because expressions (24.6) and (24.35） must be the same, the relations that determine $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ are the equations

$$
\sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) ( x _ { i } - \xi _ { j } ) _ { + } ^ { k } = ( \xi - \xi _ { j } ) _ { + } ^ { k } , \qquad j = 1 , 2 , \ldots , \dot { m } - k - 1 .
$$

The formulae (24.44) and (24.45) give a square system of linear equations in the unknowns $\{ w _ { i } ( \xi ) ; \ i = 1 , 2 , \dots , m \}$ ，which is non-singular, because equivalent equations define $\{ u _ { i } ; i = 1 , 2 , \ldots , k + 1 \}$ and $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ uniquely. The matrix elements of the system are the numbers $\{ x _ { i } ^ { r } ; r = 0 , 1 , \ldots , k \}$ and $\left\{ \left( x _ { i } - \xi _ { j } \right) _ { + } ^ { k } \right.$ ； $j = 1 , 2 , \dots ,$ $m - k - 1 \}$ ,where $1 \leqslant i \leqslant m$ .They are mentioned explicitly, because it is important to notice that they are independent of $\xi .$ Therefore, if the system is multiplied by the inverse matrix, which is also independent of $\xi ,$ it follows that each of the coefficient functions $\{ w _ { i } ( \pmb { \xi } )$ ； $a \leqslant \xi \leqslant b$ ； $i = 1 , 2 , \dots , m \}$ is in the linear space that is spanned by $\{ \xi ^ { r } ; a \leqslant \xi \leqslant b$ ； $r = 0 , 1 , \ldots , k \}$ and $\{ ( \pmb { \xi } - \pmb { \xi } _ { j } ) _ { + } ^ { k }$ ； $a \leqslant \xi \leqslant b ; j = 1 , 2 , \ldots , m - k - 1 \} ,$ Thus, letting $\xi _ { 0 } = a$ and $\xi _ { m - k } = b$ ,the functions $\{ w _ { i } ; i = 1 , 2 , \dots , m \}$ are all in the space that we call $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { m - k } )$ . It follows that the optimal interpolating function (24.3) is also a spline of degree $k$ .Because there is no error in the optimal interpolation formula when $\pmb { \xi }$ is one of the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ ， the optimal interpolating function satisfies the conditions

$$
s ( \boldsymbol { x } _ { i } ) = f ( \boldsymbol { x } _ { i } ) , \qquad i = 1 , 2 , \ldots , m .
$$

The number of equations is equal to the dimension of $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { m - k } )$ ，Therefore, instead of calculating $\{ w _ { i } ( \pmb { \xi } ) ; i = 1$ ， $2 , \ldots , m \}$ in order to determine $\pmb { S } _ { \mathrm { i } }$ , one can calculate $\pmb { s }$ directly from the system (24.46), provided that the knots $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ are known. Because the indirect procedure defines $\pmb { s }$ uniquely, the equations (24.46) are non-singular. Alternatively, one can turn to Theorem 19.4 to check whether the equations have a solution. We find that the conditions on $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ ,that are required by Theorem 19.4,are equivalent to the ones that occur in Theorem 24.3.

In order to determine the knots of $\pmb { S } _ { 3 }$ ，we consider the conditions that they have to satisfy. Theorem 24.1 states that it is necessary and sufficient for the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ to have the property that, if the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ are defined by equation (24.15), then the norm (24.14) is minimized.It follows from the discussion that follows the proof of Theorem 24.3 that it is sufficient if the points $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ satisfy the bounds (24.27),and if equation (24.30) holds, where $z$ is the sign function (24.31). Moreover, Theorem 24.3 shows that such points exist. However, instead of calculating $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ directly from the non-linear equations that are implied by expressions (24.30) and (24.31), it is usually easier to seek a perfect spline $\pmb { \sigma }$ of degree $( k + 1 )$ whose knots are $\{ \xi _ { j } ; j = 1 , 2 , \ldots ,$ $m - k - 1 \}$ .The relation (24.32） between $\sigma$ and $z$ has to be satisfied, but this relation allows any polynomial from $\mathcal { P } _ { k }$ to be added to $\pmb { \sigma }$ Therefore we impose the conditions $\{ \pmb { \sigma } ( \pmb { x } _ { i } ) = 0$ ； $i = 1 , 2 , \ldots , k + 1 \}$ Hence,because equation (24.3O) implies that the divided differences $\{ \sigma [ x _ { p } , x _ { p + 1 } , \ldots , x _ { p + k + 1 } ]$ $p = 1 , 2 , \ldots , m - k - 1 \}$ are all zero, it follows that all the data points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ are zeros of $\pmb { \sigma }$ ，Thus the required knots $\{ \xi _ { j } ; j = 1 , 2 , \ldots , m - k - 1 \}$ of the optimal interpolating function (24.3) are the knots of a perfect spline $\pmb { \sigma }$ of degree $( k + 1 )$ that satisfies the equations

$$
\begin{array} { l } { \sigma ( x _ { i } ) = 0 , \qquad i = 1 , 2 , \ldots , m } \\ { \| { \boldsymbol { \sigma } } ^ { ( k + 1 ) } \| _ { \infty } = 1 } \end{array} \biggr \} .
$$

It'is particularly useful that the converse of the last remark is true. In other words, if $\sigma$ is a perfect spline of degree $( k + 1 )$ that has $( m - k - 1 )$ knots,and that satisfes condition (24.47)， then its knots $\{ \xi _ { j } ; ~ j = 1$ ， $2 , \ldots , m - k - 1 \}$ are suitable knots for the spline $\pmb { s }$ of the optimal interpolation procedure. In order to prove this statement it is sufficient to show that expressions (24.27) and (24.30) are valid, where $z$ and $\scriptstyle B _ { p }$ are the functions (24.31) and (24.16). The first line of equation (24.47) and Theorem 22.3 imply the identities

$$
\int _ { a } ^ { b } \sigma ^ { ( k + 1 ) } ( \theta ) B _ { p } ( \theta ) \mathrm { d } \theta = 0 , \qquad p = 1 , 2 , \ldots , m - k - 1 .
$$

Therefore,because the function (24.31) is a muliple of $\sigma ^ { ( k + 1 ) }$ , equation (24.30) is satisfied. It follows from the last two paragraphs of the proof of Theorem 24.3 that inequality (24.27) is also valid.

The next theorem summarises these properties of optimal interpolation,and it gives one new result.

# Theorem 24.4

Let $k$ and $_ m$ be positive integers such that $m \geq k + 1$ , let the points $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ satisfy condition (24.5),and let $\sigma$ be a perfect spline of degree $( k + 1 )$ on $[ a , b ]$ that has $( m - k - 1 )$ knots $\{ \xi _ { j } ; j = 1$ ， $2 , \ldots , m - k - 1 \}$ ，and that satisfies equation (24.47). If $f$ is any function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ ,then the interpolation conditions (24.46) define a unique approximation $\pmb { s }$ in $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \xi _ { 2 } , . ~ . ~ . , \xi _ { m - k - 1 } , \xi _ { m - k } )$ ，whose error is bounded by the inequality

$$
\big | f ( \xi ) - s ( \xi ) \big | \leqslant \big | \sigma ( \xi ) \big | \big \| f ^ { ( k + 1 ) } \big \| _ { \infty } , \qquad a \leqslant \xi \leqslant b ,
$$

where $\xi _ { 0 } = a$ and $\xi _ { m - k } = b$ .Further,if the parameters $\{ w _ { i } ; ~ i = 1 , 2 ,$ $\cdots , m \}$ and $^ c$ have any values such that condition (24.2） is valid for all $f$ in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ]$ then $^ c$ is not less than $| \sigma ( \xi ) |$

Proof. The only result that has not been proved already is that, if $\pmb { \xi }$ is any fixed point of $[ a , b ]$ ,then $\| K \| _ { 1 }$ is equal to $\left| \sigma ( \xi ) \right|$ ,where the kernelfunction $\pmb { K }$ is defined by the equation

$$
f ( \xi ) - \sum _ { i = 1 } ^ { m } w _ { i } ( \xi ) f ( x _ { i } ) = \int _ { a } ^ { b } K ( \theta ) f ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta , \qquad f \in \mathcal { C } ^ { ( k + 1 ) } [ a , b ] ,
$$

and where the notation (24.3） is used for the optimal interpolating function in order to show its dependence on $f .$ . We express $\| K \| _ { 1 }$ in terms of $\sigma$ .The sign function $z$ ,defined by equation (24.31), changes sign at the knots of $\pmb { \sigma } _ { : }$ ,and the absolute values of $z$ and $\sigma ^ { ( k + 1 ) }$ are equal to one almost everywhere. Therefore equation (24.43) gives the value

$$
\| K \| _ { 1 } = \left| \int _ { a } ^ { b } K ( \theta ) \sigma ^ { ( k + 1 ) } ( \theta ) \mathrm { d } \theta \right| .
$$

The proof is completed by obtaining an identity from equation (24.50) in the particular case when $f = \sigma .$ .The equation is valid in this case,even though g(k+1) is not continuous, because otherwise one can deduce a contradiction by letting $f$ be a function that satisfies the conditions $\{ f ( x _ { i } ) = \sigma ( x _ { i } ) ; i = 1 , 2 , . . . , m \} , f ($ $f ( \pmb { \xi } ) = \pmb { \sigma } ( \pmb { \xi } )$ and the inequality

$$
\left| \int _ { a } ^ { b } K \left( \theta \right) \left[ f ^ { ( k + 1 ) } ( \theta ) - \sigma ^ { ( k + 1 ) } ( \theta ) \right] \mathrm { d } \theta \right| < \varepsilon ,
$$

where $\varepsilon$ is a sufficiently small positive constant. Because the terms $\{ \sigma ( x _ { i } )$ ； $i = 1 , 2 , \ldots , m \}$ are all zero, substituting $f = \sigma$ in expression (24.50) gives the value

$$
\sigma ( \xi ) = \int _ { a } ^ { b } K ( \theta ) \sigma ^ { ( k + 1 ) } ( \theta ) { \bf d } \theta .
$$

It follows from equation (24.51) that the numbers $\| K \| _ { 1 }$ and $\left. \sigma ( \xi ) \right.$ are equal. The theorem is proved.□

Some examples on the use of the optimal interpolation procedure are given in the exercises. They show that the error bounds of optimal interpolation are not much smaller than those that are obtained by simpler algorithms. Therefore the value of the optimal interpolation method may be questioned. One good reason for studying optimal procedures is that they can indicate directly whether it is possible to make substantial improvements to more convenient algorithms. Moreover, the work of this chapter gives excellent theoretical support to the strong practical reasons for employing spline approximations in computer calculations.

# 24 Exercises

24.1 Let $\{ B _ { 1 } ( \theta ) ; 0 \leqslant \theta \leqslant 3 \}$ be the linear $B$ -spline of the form (24.16) that has knots at the points $\{ x _ { 1 } = 0 , x _ { 2 } = 1 , x _ { 3 } = 3 \}$ . Calculate the value of $\xi _ { 1 }$ that satisfies the equation

$$
\int _ { 0 } ^ { \xi _ { 1 } } B _ { 1 } ( \theta ) { \bf d } \theta = \int _ { \xi _ { 1 } } ^ { 3 } B _ { 1 } ( \theta ) { \bf d } \theta .
$$

Let $\{ \sigma ( \xi ) ; 0 \leqslant \xi \leqslant 3 \}$ be a perfect spline of degree two that has only one knot, and that has zeros at the points $\{ x _ { i } ; i = 1 , 2 , 3 \}$ Verify that the knot of $\pmb { \sigma }$ is at $\xi _ { 1 }$

24.2 Calculate from Theorem 24.4 and from Exercise 24.1 the numbers $w _ { 1 } , w _ { 2 } , w _ { 3 }$ and $c$ ,such that the value of $c$ is as small as possible in the inequality

$$
\big | f ( 2 ) - w _ { 1 } f ( 0 ) - w _ { 2 } f ( 1 ) - w _ { 3 } f ( 3 ) \big | \leqslant c \big \| f ^ { \prime \prime } \big \| _ { \infty } , \qquad f \in \mathcal { C } ^ { ( 2 ) } [ 0 , 3 ] .
$$

Compare the term on the right-hand side with the error expres-sion of Theorem 4.2 for the approximation $f ( 2 ) { \approx } \frac { 1 } { 2 } [ f ( 1 ) + f ( 3 ) ]$

24.3 Find the form of the optimal linear spline approximation to the function values $\{ f ( - 1 ) , f ( - 1 + \varepsilon ) , f ( 1 - \varepsilon ) , f ( 1 ) \}$ ，where $\varepsilon$ isa constant from the open interval $( 0 , \textstyle { \frac { 2 } { 3 } } )$ . Show that the $\infty$ -norm of the optimal interpolation operator has the value $[ - \frac { 1 } { 2 } + \varepsilon ^ { - 1 } ]$

24.4 Extend Theorem 24.4 to the case when the data points satisfy the condition

$$
a \leqslant x _ { 1 } \leqslant x _ { 2 } \leqslant \ldots \leqslant x _ { m } \leqslant b
$$

instead of inequality (24.5),assuming that no number is repeated more than $( k + 1 )$ times in the set $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ If repeats occur, then the conditions (24.46) on $\pmb { s }$ are replaced bythe equations $\begin{array} { r } { \{ s ^ { ( j ) } ( x _ { i } ) = f ^ { ( j ) } ( x _ { i } ) ; \quad j = 0 , 1 , \dots , r ( i ) - 1 , } \end{array}$ ： $i = 1 , 2 , \ldots , m \}$ ，where $\pmb { r } ( i )$ is the number of occurrences of the number $x _ { i }$ in the set of data points.

24.5 The values $f ( 0 ) , f ^ { \prime } ( 0 ) , f ^ { \prime \prime } ( 0 )$ and $f ( 1 )$ of a function $f$ in $\mathcal { C } ^ { ( 3 ) } [ 0 , 1 ]$ are given. For any $\pmb { \xi }$ in [0, 1], let $s ( \xi )$ be the estimate of $f ( \xi )$ that minimizes the value of $c ( \xi )$ in the error bound

$$
\left| f ( \xi ) - s \left( \xi \right) \right| < c \left( \xi \right) \left\| f ^ { \prime \prime \prime } \right\| _ { \infty } .
$$

Calculate the functions $\{ s ( \xi ) ; 0 \leqslant \xi \leqslant 1 \}$ and $\{ c ( \xi ) ; 0 \leqslant \xi \leqslant 1 \}$

24.6 Let $f$ be a function that is defined on the range $( - \infty , \infty )$ and that has a bounded and continuous fourth derivative,and let the function values $\{ f ( x _ { i } ) = f ( i h ) ; i = 0 , \pm 1 , \pm 2 , . . . \}$ be given, where $\pmb { h }$ is a positive constant. Let $\{ s ( \xi ) ; \ - \infty < \xi < \infty \}$ be the best estimate of $\{ f ( \xi ) ; - \infty < \xi < \infty \}$ that can be obtained from the data,in the sense that the multiple of $\| f ^ { ( 4 ) } \| _ { \infty }$ that bounds the error $\left| f ( \pmb { \xi } ) - s ( \pmb { \xi } ) \right|$ is minimized. Prove that $\pmb { s }$ is the cubic spline that has knots at the points $\{ x _ { i } = i h ; i = 0 , \pm 1 , \pm 2 , . . . \}$ and that interpolates $f$ at its knots. Obtain the analogous property of the quadratic spline interpolation procedure whose cardinal functions have the form that is shown in Figure 18.4.

Let the conditions of Exercise 24.6 be satisfied except that only the function values $\{ f ( x _ { i } ) = f ( i h ) ; \ i = 1 , 2 , . . . , m \}$ are given, where $m \geqslant 4$ . Hence the optimal interpolating function $\{ \pmb { s } ( \pmb { \xi } )$ $x _ { 1 } \leqslant \xi \leqslant x _ { m } \}$ is a cubic spline that has $( m - 4 )$ knots. Let $\bar { s }$ be the cubic spline in the space $\mathcal { S } ( 3 , x _ { 1 } , x _ { 2 } , \ldots , x _ { m } )$ that interpolates the data, and whose third derivative is continuous at $x _ { 2 }$ and at $x _ { m - 1 }$ .Let $\mathcal { S } _ { 0 }$ be the two-dimensional subspace of $\mathcal { S }$ that contains splines that are zero at the knots $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ . Let ${ \pmb S } _ { \pmb { \alpha } }$ and $s _ { \beta }$ be the elements of $\mathcal { S } _ { 0 }$ whose third derivative discontinuities at $\pmb { x } _ { 2 }$ and $x _ { m - 1 }$ are one and zero and zero and one respectively. By comparing $\pmb { s }$ and $\bar { s }$ with the cubic spline that is considered in Exercise 24.6, prove that there exists a number $\pmb { \mu }$ ,independent of $f , h$ and $^ { m }$ ,such that the bound

$\big | f ( \xi ) - \bar { s } ( \xi ) \big | \leqslant \{ \big | \sigma ( \xi ) \big | + \mu h [ \big | s _ { \alpha } ( \xi ) \big | + \big | s _ { \beta } ( \xi ) \big | ] \} \{ \big | f ^ { ( 4 ) } \big | \big | _ { \infty } , \quad \ x _ { 1 } \leqslant \xi \leqslant x _ { m } ,$ is satisfied,where $\pmb { \sigma }$ is defined in Theorem 24.4.

24.8 The argument that follows Theorem 24.3 proves that the equa-tions (24.15) define the parameters $\{ v _ { p } ; p = 1 , 2 , \ldots , m - k - 1 \}$ that minimize the norm (24.14). Another way of obtaining this result depends on the fact that the system (24.15) is the limit as $M$ tends to infinity of the system (24.25). Make this alternative argument rigorous.

24.9 Show that, except for an overall change of sign, there is only one perfect spline $\pmb { \sigma }$ that satisfies the conditions of Theorem 24.4. It is suitable to combine the method of proof of Theorem 14.4 with the orthogonality conditions (24.48).

24.10 Let $f$ be a function in $\mathcal { C } ^ { ( k + 1 ) } [ a , b ] .$ ,let the function values $\{ f ( x _ { i } )$ $i = 1 , 2 , \ldots , m \}$ be given, where $m \geq k + 1$ , and let $L$ be a linear functional. The approximation to $L f$ by a linear combination of the function values is required, such that the error of the approx-imation is bounded by the smallest possible multiple of $\| f ^ { ( k + 1 ) } \| _ { \infty }$ Investigate conditions on $L$ that imply that $L s$ is the required approximation to $L f ,$ where $\pmb { s }$ is the spline function that is defined in Theorem 24.4.

# APPENDIX A

# The Haar condition

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear space in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ In Section $\mathbf { 7 . 3 \ d }$ is defined to satisfy the Haar condition if the following property is obtained.

Condition $\mathbf { \Omega } ( \pmb { 1 } )$ If $\phi$ is any element of $\mathcal { A }$ that is not identically zero, then the number of roots of the equation $\{ \phi ( { \pmb x } ) = 0$ ； $a \leqslant x \leqslant b $ is less than $( n + 1 )$

The purpose of this appendix is to prove that the following three conditions are implied by Condition (1),and also that Condition (3) and Condition (4) are each equivalent to Condition (1).

Condition (2). If $\pmb { k }$ is any integer in $[ 1 , n ]$ and if $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ is any set of distinct points from the open interval $( a , b )$ ,then there exists an element of $\scriptstyle { \mathcal { A } }$ that changes sign at these points,and that has no other zeros.Moreover, there is a function in $\mathcal { A }$ that has no zeros in $[ a , b ]$

Condition $( { \pmb 3 } )$ If $\phi$ is any element of $\mathscr { A }$ that is not identically zero, if the number of roots of the equation $\{ \phi ( { \pmb x } ) = 0$ ； $a \leqslant x \leqslant b \}$ is equal to $j ,$ and if $\pmb { k }$ of these roots are interior points of $[ a , b ]$ at which $\phi$ does not change sign, then $( j + k )$ is less than $( n + 1 )$

Condition (4). If $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ is any basis of $\scriptstyle { \mathcal { A } } .$ and if $\{ \xi _ { i } ; j = 0 , 1 , \ldots , n \}$ is any set of $( n + 1 )$ distinct points in $[ a , b ] ,$ then the $( n + 1 ) \times ( n + 1 )$ matrix whose elements have the values $\{ \phi _ { i } ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is non-singular.

It is clear that Condition (3) implies Condition (1). First it is proved that Conditions (1) and (4) are equivalent.Secondly it is shown that Conditions (1) and (4) together imply Condition (3).Finally we deduce Condition (2)from Condition (3). The final stage depends on limits of sequences of functions.

The equivalence of Conditions $( { \pmb { 1 } } )$ and (4). Suppose that Condition (1) holds but Condition (4) fails. Then there exist $( n + 1 )$ distinct points $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ in $[ a , b ] ,$ ，such that the matrix $\{ \phi _ { i } ( \xi _ { j } ) ; i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is singular.

where $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ is a basis of $\mathcal { A } .$ Therefore there exist multipliers $\left\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \right\}$ ,that are not all zero,and that satisfy the equations

$$
\sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( \xi _ { j } ) = 0 , \qquad j = 0 , 1 , \ldots , n .
$$

It follows that the function

$$
\phi \left( x \right) = \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

has zeros at the points $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ ,but this conclusion contradicts Condition (1).

Conversely,if Condition (1) fails, then there is a function of the form (A.2) that is not identically zero,and that has zeros at the points $\{ \xi _ { i } ; j = 0 , 1 , \ldots , n \}$ say. Hence equation (A.1） is satisfied,which implies that the matrix $\{ \phi _ { i } ( \pmb { \xi } _ { i } ) ; i = 0 \}$ ， $1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is singular.Therefore there is also a contradiction if Condition (1） fails but Condition (4） holds,which completes the proof that Conditions (1) and (4) are equivalent.

Conditions $( { \pmb { 1 } } )$ and (4) imply Condition $( { \pmb 3 } )$ .It is sufficient to show a contradiction if Conditions (1） and (4） hold,but Condition (3） is not satisfied.When Condition (3) is not obtained,there is a function $\phi$ in $\mathscr { A }$ that is not identically zero, that has double zeros at the points $\{ \eta _ { i } ; i = 1 , 2 , \ldots , k \}$ and that has simple zeros at the points $\{ \eta _ { i } ; i = k + 1 , k + 2 , \ldots , j \} $ where $( j + k ) \geqslant ( n + 1 )$ ,and where a zero is said to be simple if it is a point at which $\phi$ changes sign,or if it is one of the ends of the range $[ a , b ]$ 、Because Condition (1） is contradicted if $j \geq ( n + 1 )$ ，we only consider the case when $j \leqslant n$ .Therefore there is at least one double zero.We let $\pmb \varepsilon$ be a positive number such that, for each integer $_ i$ in the range $1 \leqslant i \leqslant k .$ the function $\phi$ is zero at only one point of the interval $[ \eta _ { i } - \varepsilon , \eta _ { i } + \varepsilon ] ,$ namely the point $\eta _ { i } ,$ and we let $c _ { i }$ be any non-zero number whose sign is the same as the sign of the function $\phi$ on the interval $[ \eta _ { i } - \varepsilon , \eta _ { i } + \varepsilon ] .$ Further,we let $\{ \xi _ { t } ; t = 0 , 1 , \ldots , n \}$ be any set of distinct points of $[ a , b ]$ that includes the points $\left\{ \xi _ { t } = \eta _ { t + 1 } \right.$ ； $\scriptstyle t = 0$ ， $1 , \ldots , j - 1 \}$

Condition (4) implies that there is a unique element of $\mathcal { A } , \psi$ say, that is defined by the equations

$$
\psi ( \xi _ { t } ) = \left\{ { \begin{array} { l } { c _ { t + 1 } , \quad t = 0 , 1 , \ldots , k - 1 } \\ { 0 , \quad t = k , k + 1 , \ldots , n . } \end{array} } \right.
$$

We consider the function $\left\{ \phi ^ { * } ( x ) = \phi ( x ) - \theta \psi ( x ) ; a \leqslant x \leqslant b \right\}$ ，where $\pmb \theta$ is a small positive number that satisfies the inequalities

$$
\begin{array} { l } { { \theta { | \psi ( { { \eta } _ { i } } - \varepsilon ) | } < { | \phi ( { { \eta } _ { i } } - \varepsilon ) | } } } \\ { { \theta { | \psi ( { { \eta } _ { i } } + \varepsilon ) | } < { | \phi ( { { \eta } _ { i } } + \varepsilon ) | } } } \end{array}  , \qquad i = 1 , 2 , \ldots , k .
$$

By construction $\phi ^ { * }$ changes sign in each of the intervals $\{ ( \eta _ { i } - \varepsilon , \eta _ { i } ) ; i = 1$ ， $2 , \ldots , k \}$ and $\{ ( \eta _ { i } , \eta _ { i } + \varepsilon ) ; i = 1 , 2 , \dots , k \}$ ，and also it has zeros at the points $\{ \eta _ { i } ; i = k + 1 , k + 2 , \ldots , j \}$ .Hence it has at least $( j + k )$ zeros,which contradicts Condition (1). The proof that Condition (3) is a consequence of Conditions (1) and (4) is complete.

Proof that Condition (2) is satisfied. Let $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , n \}$ be any set of distinct points in $[ a , b ]$ .Because the dimension of $\scriptstyle { \mathcal { A } }$ is $( n + 1 )$ ,there exists a function $\psi$ in $\mathcal { A }$ that is not identically zero and that satisfies the equations

$$
\psi ( \zeta _ { j } ) = 0 , \qquad j = 1 , 2 , \ldots , n .
$$

It follows from Condition (3) that $\psi$ has no other zeros in $[ a , b ]$ ,and that it changes sign at those zeros that are interior points of $[ a , b ]$ .Therefore Condition (2) holds when $k = n$

When $k = n - 1$ , we let $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ be interior points of $[ a , b ] .$ and we let $\psi _ { a }$ and $\psi _ { b }$ be non-zero functions in $\mathscr { A }$ that have zeros at the points $\{ \zeta _ { i } ; j =$ $1 , 2 , \ldots , k \}$ and at one other point, namely $^ { a }$ and $^ { b }$ respectively. Condition (3) implies that the overall sign of $\psi _ { b }$ may be chosen to satisfy the inequality $\{ \psi _ { a } ( x ) \psi _ { b } ( x ) { \geq } 0$ ； $a \leqslant x \leqslant b $ .Hence the function $\psi = { \textstyle \frac { 1 } { 2 } } ( \psi _ { a } + \psi _ { b } )$ shows that Condition (2) is valid when $k = n - 1$

The method of proof for smaller values of $k$ depends on the following statement. If $k$ and $t$ are non-negative integers such that $k + 2 t = n$ and if $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ are distinct points of $[ a , b ]$ where all the points $\{ \eta _ { j } ; j = 1 , 2 , \dots , t \}$ are in the open interval $( a , b )$ ,then there exists a function $\psi$ in $\mathcal { A }$ that has simple zeros at $\left\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \right\}$ and that has double zeros at $\{ \eta _ { j } ; j = 1 , 2 , \dots , t \}$ . In order to prove it we let $\bar { \varepsilon }$ be a positive constant such that, for each integer $i$ in $[ 1 , t ] , \eta _ { i }$ is the only one of the points $\{ \zeta _ { j } ; j = 1$ ， $2 , \ldots , k \}$ $\cdot \cdot , k \} , \{ \eta _ { j } ; j = 1 , 2 , \dots , t \}$ ， $^ { a }$ and $^ { b }$ that are in the interval $\left[ \eta _ { i } - { \bar { \varepsilon } } , \ \eta _ { i } + { \bar { \varepsilon } } \right]$ Further,for any $\pmb \varepsilon$ in $( 0 , \bar { \varepsilon } )$ , we let $\psi _ { \epsilon }$ be a function in $\mathcal { A }$ that has zeros at the points $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ ， $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ and $\left\{ \eta _ { j } + \varepsilon ; j = 1 , 2 , \dots , t \right\}$ .This function is scaled so that the coefficients of the expression

$$
\psi _ { \varepsilon } ( x ) = \sum _ { i = 0 } ^ { n } \lambda _ { i } ( \varepsilon ) \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

satisfy the condition

$$
\sum _ { i \mathop { = } 0 } ^ { n } [ \lambda _ { i } ( \varepsilon ) ] ^ { 2 } = 1 ,
$$

where $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ is a basis of $\mathcal { A } .$ Because Condition (3) implies that all the zeros of $\psi _ { \varepsilon }$ are simple, the products $\{ \psi _ { \varepsilon } ( \eta _ { j } - \delta ) \psi _ { \varepsilon } ( \eta _ { j } + \delta ) ; j = 1 , 2 , \dots , t \}$ are all positive,where $\pmb { \delta }$ is any number in $( \varepsilon , \bar { \varepsilon } )$

We let $\{ \varepsilon _ { q } ; q = 1 , 2 , 3 , \ldots \}$ be a sequence of numbers from the interval $( 0 , \bar { \varepsilon } )$ that tends to zero. Condition (A.7) implies that the sequence of parameters $[ \{ \lambda _ { i } ( \pmb { \varepsilon } _ { q } ) ; i = 0 , 1 , . . . , n \}$ ； $q = 1$ ,2,3,.. .] has a limit point $\{ \lambda _ { i } ^ { * } ; i = 0 , 1 , \dots , n \}$ It will be shown that it is suitable to let $\psi$ be the function

$$
\psi ( x ) = \sum _ { i = 0 } ^ { n } \lambda _ { i } ^ { * } \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Equation (A.7) implies that $\psi$ is not the zero function. Moreover,the definition of each $\psi _ { \epsilon }$ implies that $\psi$ has zeros at the points $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and $\{ \eta _ { j } ; j =$ $1 , 2 , \ldots , t \}$ . It remains,therefore,to rule out the possibility that one or more of the points $\{ \eta _ { i } ; j = 1 , 2 , \dots , \ \}$ are simple zeros. If $\pmb { \eta _ { j } }$ is a simple zero,there exists $\pmb \delta$ in $( 0 , \bar { \varepsilon } )$ such that the product $[ \psi ( \eta _ { j } - \delta ) \psi ( \eta _ { j } + \delta ) ]$ is negative.However, we have noted already that the product $\left[ \psi _ { \varepsilon } ( \eta _ { j } - \delta ) \psi _ { \varepsilon } ( \eta _ { j } + \delta ) \right]$ is positive if $\pmb \varepsilon$ is less than $\delta$ ， so it is non-negative in the limit as $\pmb \varepsilon$ tends to zero. This contradiction completes the proof that the function (A.8) has the required zeros.

In order to show that Condition (2) holds when $n - k = 2 t$ is a positive even integer,we choose interior points $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ of $[ a , b ]$ that are different from the points $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and we let $\psi$ be a function in $\pmb { \mathcal { A } }$ that has the zeros that have just been considered.It is important to notice that, because of Condition (3), $\psi$ has no other zeros.Further we let $( \eta _ { j } ^ { + } ; j = 1 , 2 , \dots , t \}$ be a set of points in $( a , b )$ that has no points in common with the sets $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ and $\{ \eta _ { j } ; j = 1 , 2 , \ldots , t \}$ and we let $\psi ^ { + }$ be a function in $\pmb { \mathcal { A } }$ that has simple zeros at $\{ \zeta _ { j }$ ； $j = 1 , 2 , \dots , k \}$ and double zeros at $\{ \eta _ { j } ^ { + } ; j = 1 , 2 , \dots , t \}$ .This function also has no other zeros: Because both $\psi$ and $\psi ^ { + }$ change sign only at the points $\{ \zeta _ { j } ; j = 1$ ， $2 , \ldots , k \}$ ，either the function $( \psi - \psi ^ { + } )$ or the function $( \psi + \psi ^ { + } )$ proves that Condition (3) is obtained when $( n - k )$ is an even integer.

Alternatively, if $n - k = 2 t + 1$ is an odd integer,we follow the method of the last paragraph, except that we add the point $^ { a }$ to the set $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ before defining $\psi _ { : }$ and we add $^ { b }$ to the set $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ before defining $\psi ^ { + }$ .The remainder of the proof is as before.Because these techniques can be used even when $k = 0$ , it follows that the last statement of Condition (2) is valid.The proofs of the relations between Conditions (1), (2),(3) and (4) are now complete.

# APPENDIX B

# Related work and references

Many excellent books are published on approximation theory and methods. The general texts that are particularly valuable to the present work are the ones by Achieser [2],Cheney [35],Davis [50],Handscomb (ed.)[74],Hayes (ed.)[77], Hildebrand [78],Holland & Sahney [81],Lorentz [100],Rice [132] and [134], Rivlin [138] and Watson [161]. Detailed references and suggestions for further reading are given in this appendix.

Most of the theory in Chapter 1 is taken from Cheney[35] and from Rice [132]. If one prefers an introduction to approximation theory that shows the relations to functional analysis, then the paper by Buck [32] is recommended.We give further attention only in special cases to the interesting problem, mentioned at the end of Section 1.1,of investigating how well any member of $\mathcal { B }$ can be approximated from $\mathscr { A }$ ; a more general study of this problem is in Lorentz[1OO] and in Vitushkin [160]. The development of the Polya algorithm,which is the subject of Exercise 1.10, into a useful computational procedure is considered by Fletcher, Grant & Hebden [57].

In Chapter 2,as in Chapter 1,much of the basic theory is taken from Cheney [35].For a further study of convexity the book by Rockafellar [142] is recommended.Several excellent examples of the non-uniqueness of best approximation with respect to the 1- and the $\infty$ -norms are given by Watson [161]. An interesting case of Exercise 2.1, namely when $\mathcal { B }$ is the space ${ \mathcal { R } } ^ { n }$ and the unit ball $\{ f \colon \| f \| \leqslant 1$ ； $f \in { \mathcal { B } } \}$ is a polyhedron,is considered by Anderson & Osborne [5].

The point of view in Chapter 3 that approximation algorithms can be regarded as operators is treated well by Cheney [35],and more advanced work on this subject can be found in Cheney & Price [37]. Several references to applications of Theorem 3.1 are given later, including properties of polynomial approximation operators that are defined by interpolation conditions. A comparison of the advantages of preferring rational to polynomial approximations is made by Hastings [76]. There is now a vast literature on spline functions,including interesting books by Ahlberg,Nilson & Walsh [4],de Boor [26],Prenter[127] and Schultz[151]. For a short introduction to splines the papers by Birkhoff & de Boor [15]and by Greville [70] are recommended. An excellent summary of more advanced properties of spline functions is given by Schoenberg [149].

The theory of Lagrange interpolation, considered in Chapter 4, is in most text-books on numerical analysis; see Hildebrand [78],for instance.These books include also many properties of Chebyshev polynomials.A careful analysis of Runge's example (4.19) is given by Steffensen [155]. The norms of polynomial interpolation operators are used by Powell[121] to draw attention to some of the advantages of the Chebyshev interpolation points.Further properties of the Lebesgue function $\{ \Sigma | l _ { k } ( x ) |$ ; $a \leqslant x \leqslant b \}$ ,when the Chebyshev interpolation points are used,are derived by Brutman [31]. The solution to the problem of Exercise 4.10 was conjectured by Bernstein in 1931, but the conjecture was not proved until 1977,by de Boor & Pinkus [28] and by Kilgore [89] independently.

Because the divided difference theory and methods of Chapter 5 were used extensively for the construction of tables, some of the best accounts of this work are in the older numerical analysis text-books,such as Steffensen [155]. The use of divided differences to detect errors in equally spaced data is explained by Miller [115],and an extension to allow unequal spacing between data points is made by Blanch [16]. More recent applications of divided differences are included in our study of spline approximations.A comparison of methods of representing polynomials in terms of coefficients is given by Gautschi [64]; the criterion of the comparison has several other applications.An algorithm for the Hermite interpolation method of Section 5.5 is described by Krogh [93]. A particularly elegant solution to Exercise 5.9,on the divided difference of a product,is in the book by de Boor [26]. Further information on the rational interpolation problem of Exercise 5.10 can be found in Mayers [110], Meinguet [111] and Wuytack [165].

The method of proof of the Weierstrass theorem, given in Chapter 6, is taken from Cheney [35]. The advantages of the Bernstein approximation method in interactive computing are explained by Gordon & Riesenfeld [68]. The convergence of the derivatives of the Bernstein approximations to the derivatives of the function that is being approximated is proved by Davis [5O],and the variation diminishing properties of Bernstein approximations are studied by Schoenberg [143].Many further properties of Bernstein polynomials are given by Lorentz [99].

The theory of Chapter 7 on minimax approximations is similar to the treatment in Rice [132]. An alternative approach, which is preferred by Cheney [35], by Rivlin & Shapiro [141] and by Watson [161], makes use of the properties of convex hulls. This approach is based on a necessary and sufficient condition for best minimax approximation, given by Kirchberger [9o], that depends only on the extreme values of the error function. Therefore our remark, that one only need consider extreme values of the error function to decide whether an approximation is optimal, has been known for many years. For further information on Chebyshev systems the book by Karlin & Studden [85] is recommended. A paper by Stiefel [156] directed attention to the usefulness of the bounds of Theorem 7.7.An extension of the result of Exercise 7.2 to the case when $\mathscr { A }$ is not a linear space is given by Curtis & Powell [47]. A good discussion of non-uniqueness of best approximations when the linear space $\mathscr { A }$ does not satisfy the Haar condition, which is the subject of Exercise 7.9, is in Watson [161].

It is mentioned in Chapter 8 that there are several versions of the exchange algorithm. The version that we give most attention to,that exchanges only one point of the reference on each iteration,and that brings into the reference a point where the current error function takes its maximum value, is due to Stiefel[156]. Another one-point method,which is proposed by Curtis & Frank [49] for minimax approximation on a discrete point set, is to alter the points of the reference in rotation. The version that can alter all of the reference on each iteration is studied by Murnaghan & Wrench [116]. Methods for updating matrix factorizations, in order to reduce the work of solving the system (8.4) on every iteration,are reviewed by Gill, Golub,Murray & Saunders [65]. For further reading on telescoping,the book by Lanczos [95] is recommended.Moreover, the gain in accuracy that can be obtained by calculating directly the best polynomial approximation of degree m to a polynomial of degree $\pmb { n }$ ,where $m \leqslant n - 2$ ,instead of using the telescoping technique $( n - m )$ times,is considered by Clenshaw [38], Lam & Elliott [94] and Talbot [158]. In order to apply the work of Section 8.5, one may replace a continuous interval $[ a , b ]$ by a set of discrete points; the effect of this replacement on the best minimax approximation is studied by Chalmers [33],Dunham [51]and Rivlin & Cheney[140].The relations between the discrete exchange algorithm and linear programming are explained by Rabinowitz [129], and a Fortran subroutine that is suitable for discrete minimax approximation is given by Barrodale &.Phillips [9].

The proof of the convergence of the exchange algorithm, given in the first two sections of Chapter 9,is similar to the theory of Dunham [52]. The analysis of the rate of convergence of the one-point exchange algorithm is new, but the quadratic rate of convergence of the version of the exchange algorithm that can alter all the reference points on each iteration was established by Veidinger [159]. The zero off-diagonal elements of the final second derivative matrix of the levelled reference error, which are stated in Exercise 9.8,were found by Curtis & Powell [48]. The presence of these zero second derivatives is implied by the convergence rate of the one-point exchange algorithm.

The book by Achieser [2] is recommended for the basic theory of rational approximation that is omitted from Chapter 10. Many descriptions of the exchange algorithm for the calculation of minimax rational approximations have been published,for instance see Curtis [44] and Maehly[1O5], because both of these papers give attention to the practical dificulties of the algorithm.An Algol listing of the algorithm is given by Werner,Stoer& Bommas [162].A good solution to the problem of replacing the eigenvalue calculation (10.16） by a suitably accurate finite calculation is proposed by Curtis & Osborne [46]. Methods for determining whether a system of linear constraints is consistent, which are required by the elementary linear programming methods of Section 10.4,are reviewed by Wolfe [164]. The differential correction algorithm is due to Cheney & Loeb [36],and the advantages of expression (10.38) over expression (10.36) are shown by Barrodale,Powell & Roberts [10].A numerical comparison of several algorithms for minimax rational approximation is made by Lee & Roberts [98], but more recently a procedure has been proposed by Kaufman, Leeming & Taylor [86], that combines the advantages of the exchange and the differential correction methods.Some of the diffculties that arise,if one prefers best rational approximations with respect to the 1-norm or 2-norm,are explained by Barrodale [8] and by Fraser [60].

The basic material of Chapter 11 is in many books on approximation theory and on numerical analysis,for example see Cheney [35],Davis [5O],Lawson & Hanson [97] and Rice [132]. There are also many publications on the numerical solution of discrete linear least squares problems without forming the normal equations,in particular the paper by Golub[67] is recommended.The application of the three-term recurrence relation of Theorem 11.3 to data fitting by polynomials was proposed by Forsythe [58].

Most of the results of Chapter 12 are in Hildebrand [78],which is an excellent book for further reading on Gaussian quadrature and special families of orthogonal polynomials. More properties of orthogonal polynomials are given by Szego [157]. The practical dificulties of adaptive quadrature are discussed by de Boor [2O],and he gives a suitable algorithm for this calculation.The material of Section 12.4 is one of the main topics of books on Chebyshev polynomials,for instance see Fox& Parker[59],Rivlin [139] and Snyder[153].The behaviour of the coefficients of the expansion of $\textstyle R _ { n } f$ in terms of Chebyshev polynomials when $f$ is analytic is studied by Elliott [53],and the relations between $\textstyle R _ { n } f$ and the best minimax approximation from ${ \mathcal { P } } _ { n }$ to $f$ are considered by Clenshaw [38]. The expression for $\| L _ { n } \| _ { \infty }$ in Exercise 12.6 is derived by Powell [121],and the Erdos-Turan theorem, which is the subject of Exercise 12.7,is proved in Cheney [35]. The calculation of polynomials that are orthogonal with respect to some ‘non-classical' weight functions is studied by Price [128],who suggests a technique that is similar to the one that is mentioned in Exercise 12.8.

The work of Chapter 13 is in most text-books on approximation,for instance see Cheney[35]and Rice [132]. For further reading on the theory of the Fourier series operator the book by Lanczos [96] is recommended. Interest in the FFT method has been strong during the last fteen years,due to the wide range of applications that were stimulated by the fundamental paper of Cooley & Tukey [39]. There is a book on Fast Fourier Transforms by Brigham [3O],an error analysis of the main procedure is given by Ramos [130], recent developments for the case when the number of data is not a power of two are in Winograd[163],and extensions for vector computers are considered by Korn & Lambiotte [91].

Except for Rice [132] and Watson [161],approximation books give little attention to the theory of best $L _ { 1 }$ approximations. These two books, however, cover the theory of Chapter 14.Further, the characteristic property that best $L _ { 1 }$ approximations depend on the sign of the error function is shown well by Barrodale [7]. The calculation of best $L _ { 1 }$ approximations by interpolation to $f$ at points that are independent of $f ,$ .which is suggested at the end of Section 14.3, is not restricted to the case when $\mathscr { A }$ satisfies the Haar condition, because Hobby & Rice [79]show the existence of interpolation points that may be suitable when $\mathcal { A }$ is any finite-dimensional linear space.

The proof of Jackson's first theorem, given in the first two sections of Chapter 15,is taken from Cheney [35],and the theory of discrete $L _ { 1 }$ approximation is in Rice[132],for instance. The application of linear programming methods to the solution of discrete $L _ { 1 }$ calculations was proposed by Barrodale & Young[13],and it is now an active field of research. The geometric view of linear programming, taken in Section 15.4,can be found in Abdelmalek [1] and in Bloomfield & Steiger [17]. The linear programming test for optimality,which is composed of a finite number of linear inequalities, is expressed in terms of the original $\scriptstyle { L _ { 1 } }$ approximation problem by Powell & Roberts [126]. The by-passing of vertices, recommended in Section 15.4,is included in the algorithm of Barrodale & Roberts [11], which has since been extended to allow general linear constraints on the parameters of the approximating function [12]. This algorithm defines each trial approximation by interpolation conditions,but Bartels, Conn & Sinclair[14] prefer a technique that reduces the $L _ { 1 }$ error on each iteration without the restriction of moving from vertex to vertex of the feasible region. A solution to Exercise 15.7,on the number of zeros of a best $L _ { 1 }$ approximation in the continuous case,is in Ascher [6].

The material of Chapter 16 can all be found in Cheney [35]. The optimality of the constant $\pi / 2 ( n + 1 )$ in inequality (16.2) is due to Achieser & Krein [3] and to Favard [54]. It is shown by Korneicuk [92] that the constant $\scriptstyle { \frac { 3 } { 2 } }$ in the bound (16.11) can be reduced to one. Substantial improvements to expression (16.5O) are made by Fisher[55]; he considers the construction of the least number $c ( k , n )$ such that $d _ { n } ^ { * } ( g )$ is bounded above $c ( k , n ) \| g ^ { ( k ) } \| _ { \infty }$ ，and he finds that the optimal value depends on properties of perfect splines,which are considered in Chapter 23.The optimal value of $c ( k , n )$ when $k = n + 1$ ,which is the subject of Exercise 16.5,is given by Phillips [119] and by Riess & Johnson [137].

The elementary theory of the first section of Chapter 17 can be found in most text-books on analysis,but the proof of the uniform boundedness theorem in Section 17.2 is new. Theorems 17.3 and 17.4 are taken from Cheney [35], who states that the minimum norm property of the Fourier series operator is due to Lozinski [1O1]. The problem of finding the linear projection operator from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ to ${ \mathcal { P } } ^ { n }$ of least norm,which is suggested in Section 17.4,is considered briefly by Chalmers & Metcalf [34]. Because Theorems 17.2 and 17.4 imply that no prescribed interpolation method for calculating a sequence of polynomial approximations can give uniform convergence for all continuous functions, it is interesting that the Erdos-Turan theorem, stated in Exercise 12.7,shows that some interpolation methods give convergence in the 2-norm; similar convergence properties for other norms are studied by Nevai [118].

Due to the construction and the use of tables of function values,the methods of Section 18.1 are a smallsample from the techniques that are proposed in the older numerical analysis books for piecewise polynomial interpolation.Most of the material on spline functions in Chapter 18 can be found in de Boor [26]. The papers by Curtis [45] and Lucas [1O2] are also recommended for consideration of the two end-conditions of cubic spline interpolation. There are many publications on interpolation by splines of degree greater than three: for instance,in the case of equally spaced data,Richards [136] studies the norm of the interpolation operator,and Powell[123]draws attention to the deterioration of the localization properties.The unboundedness of the interpolation operator for unevenly spaced data points, mentioned in Exercise 18.2,is shown by Marsden [108] to apply also to cubic spline interpolation,but Kammerer & Reddien [83] prove that the accuracy of cubic spline interpolation is excellent, even for irregularly spaced data,when the approximand has a continuous fourth derivative.The bicubic splines of Exercise 18.10 are highly useful for surface approximation; many of their properties are studied by de Boor [18] and [26].

The theory of the first three sections of Chapter 19,on the properties of $\pmb { B } \mathrm { . }$ -splines and on the important idea of using them as a basis of a space of splie functions,is in Curry & Schoenberg [43]. A stronger form of Theorem 19.1,on the number of zeros of spline functions,is given by Schumaker [152]. The recurrence relation of Section 19.4 for the stable evaluation of $\pmb { B }$ -splines was proposed by de Boor [21] and Cox [40]; in later papers Cox [42] suggests another stable technique for the calculation of a linear combination of $\pmb { B }$ -splines,and de Boor [25] gives Fortran programs that calculate $\pmb { B } \mathrm { . }$ -splines and their derivatives. Theorem 19.4, on conditions for the solution of the general spline interpolation problem,is due to Schoenberg & Whitney[15O]. An algorithm for general spline interpolation is described by Cox [41],and de Boor [23] studies the norm of the general spline interpolation operator. The geometric interpretation of $\pmb { B }$ -splines, given in Exercise 19.1,was found by Curry & Schoenberg[43]. Rice[133] proves the theorem of Exercise 19.6 on the characterization of a best minimax approximation.The expression for the indefinite integral of a $\pmb { B }$ -spline that is stated in Exercise 19.8 is due to Gaffney[61].Exercise 19.10 shows some of the features of least squares spline approximations.There are several publications on this useful subject; for instance,the localization properties are studied by Powell[124] in the case when the knot spacing is constant, Reid [131] describes a way of organizing the calculation to take full advantage of the band matrices that come from the use of $\pmb { B }$ -splines,and de Boor [26] gives some computer programs.

So much has been published on the accuracy of spline approximations, that Chapter 2O gives only a small sample of the convergence theorems and the techniques of analysis.Many of our theorems have been proved in other ways.For example de Boor [19] uses divided differences to establish Theorem 20.1,and Marsden [107] strengthens Theorem 20.2 by applying Schoenberg's[147] ‘variation diminishing method'.This technique sets each variable $\scriptstyle { \pmb { x _ { p } } }$ in the definition (20.11) to the average of the non-trivial knots of $N _ { p }$ ,in order that $\pmb { s }$ is equal to $f$ for any $f$ in ${ \mathcal { P } } _ { 1 }$ ,see Marsden [1O6].Thus the accuracy and some variational properties of $\pmb { s }$ are similar to those of a Bernstein polynomial approximation to $f ,$ but $\pmb { \mathscr { s } }$ has the advantage that each $s ( x )$ depends only on the form of $f$ in a neighbourhood of $x .$ .Therefore Gordon & Riesenfeld [69] recommend the use of spline approximations in computer aided design.The method that is used in Section 20.2,to establish the order of convergence of best spline approximations when $f$ is differentiable,is taken from de Boor[19].For further reading on the construction and applications of local spline approximations, which are studied in Section 20.3, the papers by de Boor & Fix [27] and Lyche & Schumaker [103] are recommended. Substantial improvements to the error bounds of Section 20.4 are given in Chapter 22,and in Kammerer & Reddien [83] and Lucas [102].

The advantages of suiting the knot positions of spline approximations to singularities of the approximand,which are considered in Section 21.1,are shown well by Rice [135]. Moreover,Rice [134] explains clearly the behaviour of the functions in the space $\mathcal { S } ( k , \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n } )$ when the knots tend to coincide. Theorem 21.2,on the norm of a quadratic spline interpolation operator, is due to Marsden [1O9]. The adaptive method for the calculation of a cubic spline approximation,given in Section 21.3,is described by Curtis [45]. An algorithm that uses a similar disposition of knots is proposed by Powell [125] for least squares approximation to discrete data. An alternative to inserting knots near a singularity is to adjust the positions of a fixed number of knots; Jupp [82] considers the application of general optimization procedures to this calculation, and de Boor & Rice [29] present a tailored algorithm,where in both cases the least squares norm of the error function is minimized.Some theoretical properties of optimal knot positions in minimax and least squares approximation are given by Handscomb [75] and Powell[122] respectively.

Conditions for the validity of the Peano kernel theorem,which is studied in Chapter 22,are in Davis [50] for instance.Applications of this important theorem are plentiful in the numerical analysis literature; in particular the analysis of the accuracy of Bernstein polynomial approximation that is given by Stancu [154], and Kershaw's [88]results on estimating derivatives of a function by differentiating a spline approximation to the function,are both highly relevant to our studies. Theorem 22.3,stating that a $\pmb { B }$ -spline is the Peano kernel of a divided difference, is in Curry & Schoenberg [43]. The calculation of Section 22.4 is not new, the constant $\frac { 5 } { 3 8 4 }$ of expression (22.64) being derived by both Hall [71] and Schultz [151].An interesting generalization of a property that is shown in Figure 22.1 is proved by Hall & Meyer [73]; it is that the Peano kernel function of cubic spline interpolation changes sign at the data points even when the spacing of the data is irregular,provided that the knots of the spline remain at the data points.

Many publications are relevant to the work of Chapter 23.The solution of the variational problem of Section 23.1 is due to Holladay [8O],and it was generalized by Schoenberg [144] to give the properties of natural splines that are stated in Theorems 23.1 and 23.2. Theorem 23.3 is also due to Schoenberg [145], but a different approach to functional approximation by Golomb & Weinberger [66] had already established a similar result. This theorem is applied in many papers to calculate the weights of quadrature formulae; see Schoenberg[148] for a review of this field. The accuracy of natural spline interpolation is analysed by Schoenberg[146], but not making full use of the degrce of the spline at the ends of the range is a disadvantage.However,both Hall [72]and Kershaw [87] show that,for cubic spline interpolation to equi-spaced data, the disadvantage is negligible at any interior point of the range in the limit as the interval between data points tends to zero.The norm of the natural spline interpolation operator for general data points is studied by Neuman [117]. The fact that perfect splines solve the variational problem of Theorem 23.4 was proved by de Boor [22] and [24] and Karlin [84] independently,allowing for the Hermite interpolation case where suitable derivatives of $f$ are given if data points coincide.For further reading on perfect splines, including results on uniqueness,the papers by Fisher & Jerome [56], Karlin [84], McClure [104] and Pinkus [120] are recommended.

The optimal interpolation problem, that is studied in Chapter 24,was solved independently and differently by Gaffney & Powell [63] and by Micchelli,Rivlin & Winograd [114], but several properties of the solution were known already, see Meinguet [112] for instance.Most of the theory of Section 24.2 is in Karlin & Studden [85],including the relation between $\pmb { B }$ -splines and Chebyshev sets that is stated in Theorem 24.2. An algorithm that calculates the optimal interpolating function in the way that is suggested by Theorem 24.4 is given by Gaffney [62].

The uniqueness of the perfect spline $\pmb { \sigma } _ { : }$ ,stated in Exercise 24.9,is proved by Karlin [84] and by Micchelli [113].

# References

solutions of overdetermined linear equations', J. Approx. Theory, 11 (1974) 38-53.   
[2] N. I. Achieser, Theory of Approximation (1947), translation published by Ungar, New York (1956).   
[3] N. I. Achieser & M. G. Krein, ‘Best approximation of differentiable periodic functions by means of trigonometric sums',Doklady Akad. Nauk SSSR,15 (1937) 107-111.   
[4] J. H. Ahlberg,E. N. Nilson & J.L. Walsh, The Theory of Splines and their Applications, Academic Press,New York (1967).   
[5] D.H. Anderson & M. R. Osborne,‘Discrete linear approximation problems in polyhedral norms',Numer.Math.,26 (1976) 179-189.   
[6] U. Ascher,On the invariance of the interpolation points of the discrete $L _ { 1 }$ approximation',J. Approx. Theory,24 (1978) 83-91.   
[7] I. Barrodale,‘On computing best $L _ { 1 }$ approximations', in Approximation Theory,ed.A. Talbot, Academic Press,London (1970).   
[8] I. Barrodale,Best rational approximation and strict quasi-convexity', SIAM J. Numer. Anal.,10 (1973) 8-12.   
[9] I. Barrodale & C.Phillips,‘Solution of an overdetermined system of linear equations in the Chebyshev norm',ACM Trans.Math. Software,1(1975) 264-270.   
[10]I.Barrodale,M. J.D.Powell & F.D.K.Roberts，‘The differential correction algorithm for rational $L _ { \infty }$ approximation', SIAM J. Numer. Anal.,9 (1972) 493-504.   
[11] I. Barrodale & F.D. K. Roberts,‘An improved algorithm for discrete $L _ { 1 }$ linear approximation', SIAM J. Numer. Anal.,10 (1973) 839-848.   
[12] I. Barrodale & F.D.K. Roberts,‘An efficient algorithm for discrete $L _ { 1 }$ linear approximation with linear constraints', SIAM J. Numer. Anal., 15 (1978) 603-611.   
[13] I. Barrodale & A. Young,‘Algorithms for best $L _ { 1 }$ and $L _ { \infty }$ linear approximations on a discrete set, Numer. Math.,8 (1966) 295-306.   
[14] R.H. Bartels,A.R. Conn & J.W. Sinclair,‘Minimization techniques for piecewise differentiable functions: the $L _ { 1 }$ solution to an overdetermined linear system', SIAM J. Numer. Anal.,15 (1978) 224-241.   
[15] G.Birkhoff & C.de Boor,‘Piecewise polynomial interpolation and approximation', in Approximation of Functions,ed. H.L. Garabedian, Elsevier Publishing Co.,Amsterdam (1965).   
[16] G. Blanch,‘On modified divided differences I', Maths. of Comp.,8 (1954) 1-11.   
[17] P. Bloomfield & W. Steiger,‘Least absolute deviations curve-fitting', SIAM Stat. Comp., in press.   
[18] C. de Boor,‘Bicubic spline interpolation', J. of Maths.and Physics, 41 (1962) 212-218. (1968) 219-235.   
[20] C.deBoorOnwritinganautomaticintegrationalgorithm,inMatheatical Software, ed. J. R. Rice, Academic Press, New York (1971).   
[21] C. de Boor,‘On calculating with $B$ -splines', J. Approx. Theory,6 (1972) 50-62.   
[22] C.de Boor,'Aremark concerning perfect splines',Bull.Amer. Math.Soc., 80 (1974) 724-727.   
[23] C.de Boor,'On bounding spline interpolation’, J. Approx. Theory,14 (1975) 191-203.   
[24] C.de Boor,‘On "best" interpolation',J. Approx. Theory,16(1976) 28-42.   
[25] C. de Boor,‘Package for calculating with $\pmb { B }$ splines', SIAM J. Numer. Anal.,14 (1977) 441-472.   
[26] C.de Boor,A Practical Guide to Splines, Springer-Verlag, New York (1978).   
[27] C. de Boor & G.J. Fix,‘Spline approximation by quasi-interpolants', J. Approx. The0ry,8 (1973) 19-45.   
[28] C.de Boor & A. Pinkus,‘Proof of the conjectures of Bernstein and Erdos concerning the_optimal nodes for polynomial interpolation', J. Approx. Theory,24 (1978) 289-303.   
[29] C. de Boor & J. R. Rice,Least squares cubic spline approximation IIvariable knots'，Report No.CSD TR 21， Purdue University，Indiana (1968).   
[30] E.O. Brigham, The Fast Fourier Transform,Prentice-Hall, Englewood Cliffs, N.J. (1974).   
[31] L. Brutman,‘On the Lebesgue function for polynomial interpolation', SIAM J. Numer. Anal., 15 (1978) 694-704.   
[32] R. C. Buck,Linear spaces and approximation theory', in On Numerical Approximation,ed.R.E.Langer, University of Wisconsin Press, Madison (1959).   
[33] B.A.Chalmers,On the rate of convergence of discretization in Chebyshev approximation', SIAM J. Numer. Anal.,15 (1978) 612-617.   
[34] B.L. Chalmers & F. T. Metcalf,‘On the computation of minimal pro-jections from $\mathcal { C } [ 0 , 1 ]$ to $\mathcal { P } _ { n } [ 0 , 1 ] ^ { , }$ ,in Approximation Theory II, eds.G.G. Lorentz,C.K. Chui & L.L. Schumaker,Academic Press,New York (1976).   
[35] E.W.Cheney,Introduction to Approximation Theory, McGraw-Hil, New York (1966).   
[36] E.W. Cheney & H. L. Loeb,‘On rational Chebyshev approximation, Numer. Math.,4 (1962) 124-127.   
[37] E.W. Cheney & K. H. Price, Minimal projections', in Approximation Theory, ed. A. Talbot, Academic Press,London (1970).   
[38] C.W. Clenshaw,‘A comparison of "best" polynomial approximations witl. truncated Chebyshev series expansions', SIAMJ. Numer. Anal.,1·(1964) 26-37.   
[39] J. W. Cooley & J. W. Tukey,‘An algorithm for the machine calculation of complex Fourier series',Maths.of Comp.,19 (1965) 297-301.   
[40] M. G. Cox,‘The numerical evaluation of $B$ -splines'， J. Inst. Maths. Applics.,10 (1972) 134-149.   
[41] M. G.Cox,An algorithm for spline interpolation',J. Inst. Maths. Applics., 15 (1975) 95-108.   
[42] M. G. Cox,‘The numerical evaluation of a spline from its $\pmb { B }$ -spline representation',J. Inst. Maths.Applics.,21(1978) 135-143.   
[43] H. B. Curry & I. J. Schoenberg,‘On Polya frequency functions IV. The fundamental spline functions and their limits’,J.d'Analyse Math.,17 (1966) 71-107.   
[44] A. R. Curtis,‘Theory and calculation of best rational approximations',in Methods of Numerical Approximation, ed. D. C. Handscomb, Pergamon Press,Oxford (1966).   
[45] A. R. Curtis,‘The approximation of a function of one variable by cubic splines', in Numerical Approximation to Functions and Data, ed. J.G. Hayes,The Athlone Press,London (1970).   
[46] A.R. Curtis & M. R. Osborne,‘The construction of minimax rational approximations to functions', Computer Journal,9 (1966) 286-293.   
[47] A. R. Curtis & M. J. D. Powell,‘Necessary conditions for a minimax approximation', Computer Journal,8 (1966) 358-361.   
[48] A.R. Curtis & M. J. D. Powell, On the convergence of exchange algorithms for calculating minimax approximations', Computer Journal, 9 (1966) 78-80.   
[49] P.C. Curtis & W.L. Frank,‘An algorithm for the determination of the polynomial of best minimax approximation to a function defined on a finite point set',J.Assoc. Comp.Mach.,6 (1959) 395-404.   
[50] P.J. Davis,Interpolation and Approximation, Blaisdell Publishing Co., Waltham,Mass. (1963).   
[51] C. B. Dunham,‘Efficiency of Chebyshev approximation on finite subsets', J. Assoc. Comp. Mach.,21 (1974) 311-313.   
[52] C. B. Dunham,‘Convergence of Stiefel's exchange method on an infinite set', SIAM J. Numer. Anal.,11(1974) 729-731.   
[53] D.Elliott,‘The evaluation and estimation of the coefficients in the Chebyshev series expansion of a function’, Maths. of Comp.,18 (1964) 274-284.   
[54] J.Favard, Sur les meilleurs proceédés d'approximation de certaines classes de fonctions par des polynomes trigonometriques'， Bull. des Sciences Math.,61 (1937) 209-224.   
[55] S.D. Fisher,‘Best approximation by polynomials', J. Approx. Theory,21 (1977)43-59.   
[56] S.D.Fisher & J.W. Jerome,‘Perfect spline solutions to $L _ { \infty }$ extremal problems', J. Approx. Theory,12(1974) 78-90.   
[57] R. Fletcher, J.A. Grant & M. D. Hebden, Linear minimax approximation as the limit of best $L _ { p }$ -approximation', SIAM J. Numer. Anal.,11 (1974) 123-136.   
[58] G.E. Forsythe,‘Generation and use of orthogonal polynomials for data fitting with a digital computer', SIAM Journal, 5 (1957) 74-88.   
[Jy」 L. rux & 1. D. raikei, Cnevysnev rolynomiuis in vumericul Analysis, Oxford University Press,London (1968).   
[60] W.Fraser,‘Examples of best discrete $L _ { 1 }$ and $L _ { 2 }$ rational approximations', J. Approx. The0ry,27 (1979) 249-253.   
[61] P.W. Gafney,The calculation of indefinite integrals of $B ^ { \prime }$ -splines', J. Inst. Maths. Applics.,17 (1976) 37-41.   
[62] P. W. Gaffney,To compute the optimal interpolation formula', Maths. of Comp., 32 (1978) 763-777.   
[63] P.W. Gaffney & M. J.D.Powell,‘Optimal interpolation', in Numerical Analysis Dundee 1975,Lecture Notes in Mathematics No. 506, ed. G. A. Watson, Springer-Verlag, Berlin (1976).   
[64] W. Gautschi, The condition of polynomials in power form', Maths. of Comp., 33 (1979) 343-352.   
[65] P. E. Gill, G.H. Golub,W. Murray & M. A. Saunders,‘Methods for modifying matrix factorizations',Maths.of Comp.,28 (1974) 505-535.   
[66] M. Golomb & H. F. Weinberger,‘Optimal approximation and error bounds', in On Numerical Approximation, ed.R.E.Langer,University of Wisconsin Press,Madison (1959).   
[67] G. H. Golub,‘Numerical methods for solving linear least squares problems',Numer. Math.,7 (1965) 206-216.   
[68] W. J. Gordon & R.F. Riesenfeld,‘Bernstein-Bézier methods for the computer-aided design of free-form curves and surfaces', J. Assoc. Comp. Mach.,21 (1974) 293-310.   
[69] W. J. Gordon & R.F. Riesenfeld,‘B-spline curves and surfaces', in Computer Aided Geometric Design, eds. R.E. Barnhill& R.F.Riesenfeld, Academic Press, New York (1974).   
[70] T. N. E. Greville,Introduction to spline functions', in Theory and Applications of Spline Functions, ed. T. N. E. Greville, Academic Press, New York (1969).   
[71] C. A. Hall :On error bounds for spline iterpolation’, J. Approx. Theory,1 (1968)209-218.   
[72] C. A. Hall,‘Natural cubic and bicubic spline interpolation’, SIAM J. Numer. Anal.,10 (1973) 1055-1060.   
[73] C. A. Hall & W. W. Meyer,‘Optimal error bounds for cubic spline interpolation',J. Approx. Theory,16 (1976) 105-122.   
[74] D. C. Handscomb (ed.), Methods of Numerical Approximation, Pergamon Press,Oxford (1966).   
[75] D. C. Handscomb,‘Characterization of best spline approximations with free knots', in Approximation Theory, ed. A. Talbot, Academic Press, London (1970).   
[76] C. Hastings,Approximations for Digital Computers, Princeton University Press, Princeton (1955).   
[77] J. G. Hayes (ed.), Numerical Approximation to Functions and Data, The Athlone Press,London (1970).   
[78] F. B. Hildebrand,Introduction to Numerical Analysis,McGraw-Hill, New York (1956).   
[/y」C. K. nuvvy & J.K. rice,A imuent piuvie m $L _ { 1 }$ approxiauon,rroc. Amer. Math. Soc.,16 (1965) 665-670.   
[80] J. C. Holladay,‘A smoothest curve approximation', Maths. of Comp., 11 (1957) 233-243.   
[81] A.S. B. Holland & B. N. Sahney, The General Problem of Approximation and Spline Functions, Krieger Publishing Co., Huntington, N.Y. (1979).   
[82] D.L. B. Jupp,‘Approximation to data by splines with free knots', SIAMJ. Numer. Anal.,15 (1978) 328-343.   
[83] W.J. Kammerer & G. W. Reddien,‘Local convergence of smooth cubic spline interpolates', SIAM J. Numer. Anal.,9 (1972) 687-694.   
[84] S. Karlin,‘Interpolation properties of generalized perfect splines and the solutions of certain extremal problems', Trans. Amer. Math. Soc. 206 (1975) 25-66.   
[85] S. Karlin & W.J. Studden, Tchebyscheff Systems: with Applications in Analysis and Statistics, Interscience,New York (1966).   
[86] E.H. Kaufman, D.L. Leeming & G.D. Taylor,‘A combined Remes - differential correction algorithm for rational approximation', Maths. of Comp.,32 (1978) 233-242.   
[87] D. Kershaw,'A note on the convergence of interpolatory cubic splines', SIAMJ. Numer. Anal., 8 (1971) 67-74.   
[88] D. Kershaw,The orders of approximation of the first derivative of cubic splines at the knots,Maths. of Comp.,26 (1972) 191-198.   
[89] T. A. Kilgore, A characterization of the Lagrange interpolating pro-jection with minimal Tchebycheff norm', J. Approx. Theory,24 (1978) 273-288.   
[90] P. Kirchberger，'Uber Tchebychefsche annaherungsmethoden'， Math. Ann., 57 (1903) 509-540.   
[91] D.G. Korn & J.L.Lambiotte,Computing the Fast Fourier Transform on a vector computer',Maths.of Comp., 33 (1979) 977-992.   
[92] N.P. Korneichuk, The exact constant in D. Jackson's theorem on best uniform approximation of continuous periodic functions',Doklady Akad. Nauk SSSR,145 (1962) 514-515.   
[93] F. T. Krogh,‘Eficient algorithms for polynomial interpolation and numerical differentiation', Maths. of Comp., 24 (1970) 185-190.   
[94] B.Lam & D.Ellott, Onaconjectureof C. W.Clenshaw',SIAMJ. Numer. Anal.,9 (1972) 44-52.   
[95] C.Lanczos, Applied Analysis，Prentice-Hall, Englewood Clifs，N.J. (1956).   
[96] C.Lanczos,Discourse on Fourier Series,Oliver & Boyd,Edinburgh (1966).   
[97] C.L.Lawson & R.J. Hanson, Solving Least Squares Problems, Prentice-Hall,Englewood Cliffs,N.J. (1974).   
[98] C.M.Lee & F.D. K. Roberts, A comparison of algorithms for rational $L _ { \infty }$ approximation', Maths.of Comp.,27 (1973) 111-121.   
[99] G. G.Lorentz,Bernstein Polynomials, University of Toronto Press, Toronto (1953).   
100] G. G. Lorentz, Approximation of Functions, Holt, Rinehart & Winston, New York (1966).   
[101] S. M. Lozinski, ‘On a class of linear operators', Doklady Akad. Nauk SSSR,61 (1948) 193-196.   
[102] T. R. Lucas,‘Error bounds for interpolating cubic splines under various end conditions', SIAM J. Numer. Anal.,11 (1974) 569-584.   
[103] T. Lyche & L. L. Schumaker,‘Local spline approximation methods',J. Approx.The0ry,15 (1975) 294-325.   
[104] D. E. McClure,‘Perfect spline solutions of $L _ { \infty }$ extremal problems by control methods',J. Approx. Theory,15 (1975) 226-242.   
[105]H.J. Maehly,‘Methods for fiting rational approximations,Parts II and III',J. Assoc. Comp. Mach.,10 (1963) 257-277.   
[106] M. J. Marsden,‘An identity for spline functions with applications_to variation-diminishing spline approximation',J.Approx. Theory,3 (1970) 7-49.   
[107] M. J. Marsden,‘On uniform spline approximation', J. Approx. Theory, 6 (1972) 249-253.   
[108] M. J. Marsden,‘Cubic spline interpolation of continuous functions, J. Approx. The0ry,10 (1974) 103-111.   
[109]M.J.Marsden,Quadraticspline interpolation',Bull.Amer.Math.Soc,80 (1974) 903-906.   
[110] D.F. Mayers,‘Interpolation by rational functions',in Methods of Numerical Approximation,ed.D.C.Handscomb,Pergamon Press,Oxford (1966).   
[111] J. Meinguet,‘On the solubility of the Cauchy interpolation problem', in Approximation Theory,ed.A. Talbot,Academic Press, London (1970).   
[112] J. Meinguet,Optimal approximation and interpolation in normedspaces', in Numerical Approximation to Functions and Data,ed. J. G. Hayes, The Athlone Press,London (1970).   
[113] C. A. Micchelli, 'Best $\mathbf { { { L } } _ { 1 } }$ approximation by weak Chebyshev systems and the uniqueness of interpolating perfect splines', J. Approx. Theory, 19 (1977) 1-14.   
[114] C. A. Miccheli, T. J. Rivlin & S. Winograd, The optimal recovery of smooth functions',Numer. Math., 26 (1976) 191-200.   
[115] J. C.P.Miller,Checking by differences I', Maths. of Comp.,4 (1950) 3-11.   
[116] F. D. Murnaghan & J. W. Wrench, The determination of the Chebyshev approximating polynomial for a differentiable function', Maths. of Comp., 13 (1959) 185-193.   
[117] E. Neuman,Bounds for the norm of certain spline projections',J. Approx. Theory,27 (1979) 135-145.   
[118] G. P. NevaiMean convergence of Lagrange interpolation,I',J. Approx. Theory,18 (1976) 363-377.   
[119]G.M.Phillips，‘Estimate of the maximum error in best polynomial approximations',Computer Journal,11(1968) 110-111.   
[120] A. Pinkus,‘Some extremal properties of perfect splines and the pointwise Landau problem on the finite interval',J. Approx. Theory,23 (1978) 37-64.   
[121] M. J. D. Powell, On the maximum errors of polynomial approximations defined by interpolation and by least squares criteria', Computer Journal,9 (1967) 404-407. Mathematik, Differentialgleichungen, Approximationstheorie, Birkhauser Verlag,Basel (1968).   
[123] M. J. D. Powell, A comparison of spline approximations with classical interpolation methods', in Proceedings IFIP Congress,Edinburgh,1968, North-Holland,Amsterdam (1969).   
[124]M. J. D. Powell,‘The local dependence of least squares cubic splines', SIAM J. Numer. Anal.,6 (1969) 398-413.   
[125] M. J. D. Powell,‘Curve fiting by splines in one variable', in Numerical Approximation to Functions and Data, ed.J.G. Hayes,The Athlone Press, London (1970).   
[126] M. J. D. Powell & F.D.K. Roberts,A discrete characterization theorem for the discrete $L _ { 1 }$ linear approximation problem', J. Approx. Theory, in press.   
[127] P. M. Prenter,Splines and Variational Methods, John Wiley & Sons Inc., New York (1975).   
[128]T.E. Price,‘Orthogonal polynomials for nonclasical weight functions, SIAMJ. Numer. Anal.,16 (1979) 999-1006.   
[129] P.Rabinowitz,'Applicationsof linear programming to numerical analysis', SIAM Review,10 (1968) 121-159.   
[130] G. U. Ramos,Roundoff error analysis of the Fast Fourier Transform', Maths. of Comp.,25 (1971) 757-768.   
[131] J. K. Reid,‘A note on the least squares solution of a band system of linear equations by Householder reductions',Computer Journal,1o (1967) 188-189.   
[132] J. R. Rice, The Approximation of Functions: vol.1, Linear Theory, Addison-Wesley Publishing Co., Reading,Mass. (1964).   
[133] J. R. Rice,‘Characterization of Chebyshev approximations by splines', SIAM J. Numer. Anal., 4 (1967) 557-565.   
[134] J. R. Rice, The Approximation of Functions: vol. 2, Nonlinear and Multivariate Theory,Addison-Wesley Publishing Co.,Reading,Mass. (1969).   
[135] J. R. Rice,‘On the degree of convergence of nonlinear spline approximation',in Approximation with Special Emphasis on Spline Functions,ed. I. J. Schoenberg, Academic Press, New York (1969).   
[136] F. Richards,The Lebesgue constants for cardinal spline interpolation', J. Approx. Theory,14 (1975) 83-92.   
[137]R.D.Riess &L.W.Johnson,Errors ininterpolatingfunctions atthezeros of $T _ { n + 1 } ( x ) ^ { \prime }$ , SIAM J. Numer. Anal., 11 (1974) 244-253.   
[138] T.J. Rivlin,An Introduction to the Approximation of Functions, Blaisdell Publishing Co., Waltham, Mass. (1969).   
[139] T. J. Rivlin, The Chebyshev Polynomials,John Wiley & Sons Inc., New York (1974).   
[140] T.J. Rivlin& E. W. Cheney,‘A comparison of uniform approximations on an interval and a finite subset thereof', SIAM J. Numer. Anal., 3 (1966) 311-320.   
[141] T. J. Rivlin & H. S. Shapiro,‘A unified approach to certain problems of approximation and minimization', SIAM Journal, 9 (1961) 670-699.

[142] R.T.Rockafellar, Convex Analysis,Princeton University Press,Princeton (1970).

[143] I.J.Schoenberg,‘On variation diminishing approximation methods, in $o _ { n }$ Numerical Approximation, ed. R.E. Langer, University of Wisconsin Press, Madison (1959).   
[144] I. J. Schoenberg,‘On interpolation by spline functions and its minimal properties', in On Approximation Theory,eds. P.L. Butzer & J. Korevaar, Birkhäuser Verlag, Stuttgart (1964).   
[145] I.J.Schoenberg,‘Spline interpolation and best quadrature formulae',Bull. Amer. Math. Soc.,70 (1964) 143-148.   
[146] I. J. Schoenberg,‘Spline interpolation and the higher derivatives', Proc. Nat. Acad. Sci. U.S.A.,51 (1964) 24-28.   
[147] I. J. Schoenberg,‘On spline functions', in Inequalities, ed. O. Shisha, Academic Press,New York (1967).   
[148] I. J. Schoenberg,‘Monosplines and quadrature formulae', in Theory and Applications of Spline Functions, ed. T.N. E. Greville, Academic Press, New York (1969).   
[149] I. J. Schoenberg, Cardinal Spline Interpolation, Regional Conference Series in Applied Mathematics No.12, SIAM,Philadelphia (1973).   
[150] I. J. Schoenberg & A.Whitney,‘On Polya frequency functions, II. The positivity of translation determinants with an application to the inter-polation problem by spline curves', Trans. Amer. Math. Soc.,74 (1953) 246-259.   
[151] M. H. Schultz, Spline Analysis, Prentice-Hall, Englewood Cliffs,N.J. (1973).   
[152] L. L. Schumaker,‘Zeros of spline functions and applications', J. Approx. Theory,18 (1976) 152-168.   
[153] M.A.Snyder, Chebyshev Methods in Numerical Approximation,Prentice-Hall,Englewood Cliffs,N.J. (1966).   
[154] D.D. Stancu,Evaluation of the remainder term in approximation formulas by Bernstein polynomials',Maths. of Comp.,17 (1963) 270-278.   
[155] J. F. Steffensen, Interpolation,Chelsea Publishing Co., New York (1927).   
[156] E.L. Stiefel,‘Numerical methods of Tchebychef approximation', in On Numerical Approximation,ed.R.E. Langer, University of Wisconsin Press, Madison (1959).   
[157] G. Szego, Orthogonal Polynomials,Amer. Math. Soc. Colloquium Publications,No.23 (1939).   
[158] A. Talbot,The uniform approximation of polynomials by polynomials of lower degree', J. Approx. Theory,17 (1976) 254-279.   
[159] L. Veidinger,On the numerical determination of the best approximations in the Chebyshev sense', Numer. Math.,2 (1960) 99-105.   
[160] A.G. Vitushkin, Theory of the Transmission and Processing of Information (transl.), Pergamon Press, Oxford (1961).   
[161] G.A. Watson,Approximation Theory and Numerical Methods,John Wiley & Sons,Chichester (1980).   
[162] H. Werner,J. Stoer & W. Bommas,‘Rational Chebyshev approximation', Numer. Math.,10 (1967) 289-306.   
[163] S.Winograd,‘On computing the discrete Fourier transform',Maths. of Comp.,32 (1978) 175-199.   
[164] P.Wolfe, The composite simplex algorithm', SIAM Review,7 (1965) 42-54.   
[165] L.Wuytack,‘On some aspects of the rational interpolation problem', SIAMJ. Numer. Anal.,11 (1974) 52-60.

# algebraic polynomial, see polynomial

$\pmb { B }$ -splines basis of space of splines 231-4 calculation of values and recurrence relation 234-6 definite integral 275 definition 229 derivation by divided differences 236 Haar condition 301-2 in analysis of optimal interpolation 300-6 in analysis of perfect splines 290-4 indefinite integral 240 in minimization of $\left\| s ^ { \prime \prime } \right\| _ { 2 }$ subject to interpolation conditions 283-5 in proof of uniform convergence of spline approximation 241-3 non-negativity conditions 229-31 Peano kernel of divided difference 274-6,283-5,290-1,300   
basis functions in least squares calculations 126-31, 240 in polynomial approximation 33,51-3, 131-3 in spline approximation 29-30, 227-8, 231-4   
Bernstein approximation 65-9   
Bessel's inequality 155   
best approximation characterization,see characterization theorems continuity of operator 16-17 definition and existence 4-6 geometric view 9-11 uniqueness of solution 14-16   
bicubic splines 226   
bounds,see error bounds and norm of operator   
cardinal functions in analysis of Gaussian quadrature 138-40 piecewise polynomial interpolation 214-15 polynomial interpolation 33-5 spline interpolation 216-19,222-3   
characterization theorems for $L _ { 1 }$ approximation 165-9,181-2 least squares approximation 125-6,296 minimax approximation 75-7,79,112- 13,120-1,239-40 orthogonal polynomials 141   
Chebyshev interpolation points 39-41   
Chebyshev polynomials definition and recurrence relation 38-9, 142 in telescoping 92 in the Chebyshev least squares operator $R _ { n }$ 144-5 minimal property 78 orthogonality conditions 144   
Chebyshev set,see Haar condition   
continuity_of best approximation operator 16-17   
convergence,see also order of convergence and uniform convergence of Fourier series 155-6,193 of the differential correction algorithm 120-2 of the exchange algorithm 93,101-2, 105-8, 116-17   
convexity 13-19   
cubic polynomial defined by Hermite interpolation 213   
cubic spline,see spline approximation by Bernstein derivative 67-9 approximation by spline derivative 253 conditions in Hermite interpolation 53-7 discontinuities of spline functions 220, 224,261-5 minimal property of natural spline 283- 5,287-90 minimal property of perfect spline 292-5 relation to divided difference 47   
difference,see divided difference   
diferential correction algorithm 119-22   
Dini-Lipschitz theorem 193   
discrete approximation by a rational function 112-13,117-20 by a trigonometric polynomial 156-61 by the exchange algorithm 92-4,117 in the $L _ { 1 }$ -norm 18-19,181-6 in the least squares norm 124-5,133, 157-8 in the minimax norm 19,79,92-4, 112-13,118-20 linear programming methods,see lineal programming to continuous problems 118-19,156, 186   
distance function 4-5,11   
divided difference checking of tables 47,59 definition 46 derivation of $\pmb { B }$ -splines 236 expression from the Peano kernel theorem 274-6,283-5,290-1,300 for Newton's interpolation method 48-9 of equi-spaced data 59 of product 59,236 recurrence relation 49-51 relation to derivative 47 when there are repeated arguments 55-7   
eigenvalue problem in rational exchange algorithm 113-15   
end conditions in spline interpolation 216,219-21,223-5,285   
equivalence of operators 201-2   
Erdos-Turan theorem 148   
error bounds,see also order of convergence for linear projection operators 24-5 in cubic spline interpolation 277-81 in optimal interpolation 309-10 I uc canang aiguiiu o1-, ov,v, 113   
error estimates in cubic spline interpolation 261-5   
error expressions derived by the Peano kernel theorem 268,276-82 for Gaussian quadrature 147 for polynomial interpolation 35-6,276 in the exchange algorithm,see levelled reference error   
Euclidean,see least squares   
exchange algorithm,see also levelled reference error adjustment of reference 87-8,93,112 bounds on the minimax error 81-2, 86, 90,113 description 85-8,93,112-15 initial reference 85,90-1 in the discrete case 92-4,117 in the rational case 112-18 minimax approximation on a reference 79,85-6,112-13 numerical example 88-90 proof of convergence 93,101-2, 116-17 rate of convergence 105-8 separation of reference points 100-1   
existence of best approximations 4-6 minimax rational approximations 12, 113   
extended space of spline functions 255-7   
fast Fourier transform 158-61   
Fejer operator 162-3   
first derivative recurrence relation of cubic spline 216   
Fourier series Bessel's inequality 155 convergence properties 155-6,193 Dini-Lipschitz theorem 193 fast Fourier transform 158-61 in the continuous case 152-6 in the discrete case 156-8 minimal property of norm 206-8 norms and their bounds 155,192-3   
Gaussian quadrature derivation 138-9 error expression 147 positive coefficients 140   
geometric view of linear programming 184-6 norms and best approximation 9-11   
Haar condition definition and properties 76-7,313-16 in analysis of the exchange algorithm 98-108 in $L _ { 1 }$ approximation 169-72,175 in minimax approximation 77,79-82, 90 of space of $\pmb { B }$ -splines 301-2   
Hermite interpolation by a cubic polynomial 213 an extension of Newton's method 53-7   
Hermite polynomials 143   
Hilbert space 17,123-6   
ill-conditioning of a spline basis 227-8 of normal equations 127-8,134   
increase in levelled reference error 87, 97-9, 116-17   
integrals and integration, see quadrature   
interpolation by a piecewise polynomial 29,212-15 by a polynomial,see polynomial interpolation by a rational function 44-5,59-60 bya spline,see spline interpolation by a trigonometric polynomial 161 cardinal functions 33-5,214-19,222-3 optimal, see optimal interpolation points for $L _ { 1 }$ approximation 170-4, 301-6   
Jackson's theorems extension to algebraic polynomials 195-8 for a continuous function 189-93, 196-7 for a differentiable function 179-81, 197-8 fora highly differentiable function 194- 5,197-8 for a Lipschitz continuous function 190, 196-7   
Jacobi polynomials 142   
kernel functions Fejer kernel 162-3 Fourier series kernel 154-5 Peano kernel 270-4   
knots of spline functions algorithm for choosing them automatically 261-6 change of spacing in cubic spline interpolation 263-5 coincident knots 255-7 definition 29-30 extra knots for $\pmb { B }$ -spline basis231-4 fitting to a singularity 254-7,266-7 in best least squares approximation 296 in optimal interpolation 308-9 in perfect spline interpolation 294-5 in quadratic spline interpolation 221-4, 257-61 relation to zeros of spline 230-1,237- 8,293-4,306   
$L _ { 1 }$ approximation byalgebraic polynomials172-4 by linear combination of $\pmb { B }$ -splines 300-6 by trigonometric polynomials 176 characterization theorems 165-9, 181-2 definition of $L _ { 1 }$ -norm 6-7,164 example for proof of Jackson's theorem 177-9 interpolation points 170-4,301-6 in the discrete case 18-19,181-6 methods of calculation 171-2,177-9, 183-6 non-uniqueness of best approximation 18-19,187 relation to least squares approximation 168 uniqueness of best approximation 170, 175 when the Haar condition holds 169-72, 175   
$L _ { 2 }$ approximation,see least squares approximation   
$L _ { \infty }$ approximation, see minimax approximation   
$L _ { p }$ approximation condition for best approximation 168-9 definition of norm 6-7 uniqueness of best approximation 16   
Lagrange interpolation description 33-5 discussion of stability 52-3   
Laguerre polynomials 143   
least maximum approximation,see minimax approximation   
least squares approximation basis functions 126-31,240 by algebraic polynomials 131-3 by spline functions 240,296 by the Chebyshev operator $\scriptstyle { R _ { n } }$ 143-7 by trigonometric polynomials 152-61 characterization theorem 125-6 definition of norm 6-7,123-5 Erdos-Turan theorem 148 in the discrete case 124-5,133,157-8   
least squares approximation (cont.) methods of calculation 126-33,158-61 normal equations 127-9 uniqueness of best apprjximation 17- 18,123-4,126   
Lebesgue constants and functions 24-5, 41-3,218-19   
Legendre polynomials 142,149   
levelled reference error bounds on its value 81-2 definition 87 diagonal second derivative matrix 110 explicit expression and its multipliers 97-9,101 in analysis of exchange algorithm 101-2 in rational approximation 112-17 methods of calculation 85-6,113-15 monotonic increase 87,97-9,116-17   
linear programming duality 94,291 for $\scriptstyle { L _ { 1 } }$ approximation 183-6 for minimax approximation 94,118-20 for rational approximation 118-20 geometric view 184-6 to derive minimal property of perfect spline 291   
local spline approximation bya combination of $\pmb { B }$ -splines 243, 248-51 by interpolation 225,246-8   
metric space 3-5,16   
minimal properties of Chebyshev polynomials 78 natural splines 287-90 perfect splines 290-5 the norm of $s _ { n }$ 206-8   
minimax approximation by algebraic polynomials 26-8,76-9 byrational functions 111-21 by spline functions 239-40 by trigonometric polynomials 162,196 characterization theorems 75-7,79, 112-13,120-1,239-40 definition of norm 7,72 in the discrete case 19,79,92-4,112- 13,118-20 methods of calculation 12,85-8, 92-4, 112-15,118-20 non-uniqueness of best approximation 18-19,83 on a reference 79,85-6,112-13 uniqueness of best approximation 79- 81,108-9,113 when Haar condition holds 77,79-82, 90   
monotone operator 62-5,162-3   
multivariate approximation 71,226   
natural spline definition 285 interpolation conditions 219,285-6 minimal properties 287-90   
Newton's method for polynomial interpolation description 48-51 discussion of stability 52-3 extension to Hermite interpolation 53-7   
non-uniqueness of best approximations 11 best $\scriptstyle { L _ { 1 } }$ approximations 18-19,187 best minimax approximations 19,83   
normal equations in least squares calculations 127-9   
normed linear space 5-6,9-11,13-15, 17-19   
norm of operator definition 23 for polynomial interpolation 23-4, 41-3 for spline interpolation 218-19,225, 257-9 in the error bound that depends on the least maximum error 24 in the uniform boundedness theorem 203-4 values and bounds for $\| R _ { n } \|$ and $\| \pmb { S _ { n } } \|$ 145-7, 155,192-3   
norm of space definition 5 geometric view 9-11 relation between norms 7-9,11 strictly convex norm 14-19 the $\scriptstyle { L _ { 1 } }$ -norm6-7,18-19,164 the $L _ { p }$ norm 6-7,16 the least squares norm 6-7,17-18, 123-5 the minimax norm 7,18-19,72   
numerical integration,see quadrature   
one-point exchange algorithm,see exchange algorithm   
operator best approximation operators 16-17 equivalence of operators 201-2 linear operators 22-3 monotone operators 62-5, 162-3 norm,see norm of operator projection operators 22-5,206-10 the Bernstein operator 65-9 the Chebyshev least squares operator $\scriptstyle { R _ { n } }$ 143-7,155,208-9   
operator (cont.) the discrete Fourier series operator 156-8 the Fejer operator 162-3 the Fourier series operator $s _ { n }$ 152-6, 192-3,206-8   
optimal interpolation definition 298 derivation of interpolation formula 299-309 error bounds 309-10 knot positions 308-9 method of calculation 307-8   
order of convergence of polynomial approximation 26-8, 195-8 of spline approximation 30,241-6 of trigonometric approximation,see Jackson's theorems   
orthogonality definition 125 in least squares approximations 125-31 of algebraic polynomials 131-3,141-3 of Chebyshev polynomials 144 of trigonometric polynomials 153,158   
orthogonal polynomials characterization theorem 141 Chebyshev,see Chebyshev polynomials elementary theory 136-8 Hermite polynomials 143 in Gaussian quadrature 138-40 in least squares approximation 131-3 Jacobi polynomials 142 Laguerre polynomials 143 Legendre polynomials 142,149 properties of zeros 137-8,147 recurrence relation 131-3 Rodrigue's formula 142 approximation discussion of applications 28-9 interpolation procedures 29, 212-15   
Polya algorithm12   
polynomial approximation basis functions33,51-3,131-3 Bernstein operator 65-9 best in the $\pmb { L } _ { 1 }$ norm 166-7, 172-4 best in the least squares norm 125-6 131-3 best in the minimax norm 26-8,76-! by interpolation,see polynomial interpolation characterization theorems 77,125-6. 166-7 methods of calculation 34,48-51, 5s 6,65,85-8,92-3, 131-3, 174 order of convergence 26-8,195-8 orthogonality of polynomials 131-3, 141-4 telescoping 92, 148 trigonometric,see trigonometric polynomials uniform convergence 61-7, 196-7   
polynomial interpolation by a straight line 23-4, 29,213-14 cardinal functions 33-5 choice of interpolation points 37-41 effect of data errors 34 error expressions 35-6,276 Hermite interpolation 53-7 Lagrange formula 33-5, 52-3 Newton'smethod 48-57 norm of operator 41-3,208-10 to obtain convergence in the least squares norm 148 uniqueness of solution 33-4, 54-5   
product divided difference formula 59, 236   
projection operator 22-5,206-10   
quadratic spline interpolation 221-5, 257-61,282   
quadrature Gaussian 138-40,147 of $\pmb { B }$ -splines 240, 275 of trigonometric functions 156-7   
$\pmb { R _ { n } }$ operator (Chebyshev least squares) 143-7,155,208-9   
rational approximation by interpolation 44-5,59-60 comparison with polynomial approximation 28,111-12 diferential correction algorithm 119- exchange algorithm 112-18   
Peano kernel theorem description and proof 270-4 discussion and applications 268-70, 273-81 for cubic spline interpolation 277-81 for divided differences 274-5 for polynomial interpolation 276 minimization of the $L _ { 1 }$ -norm of the kernel 299-306 minimization of the least squares norm of the kernel 288-90   
perfect splines definition 291-2 error bound and knots for optimal interpolation 308-10 minimal property 292-4 uniqueness 294-5,297,312   
rational approximation(cont.) minimax approximation on areference 112-13 minimax theory 12,111-13,117, 120-1   
recurrence relation for B-splines 234-6 Chebyshev polynomials_39 divided differences 49-51 Legendre polynomials 149 orthogonal polynomials 131-3 spline interpolation 216,222-3,258   
reference,see exchange algorithm and levelled reference error   
Remes’algorithm,see exchange algorithm   
Rodrigue's formula 142   
Rolle's theorem 35-6,47   
Runge's example 37-41   
$s _ { n }$ operator (Fourier series) 152-6,192- 3,206-8   
scalar product 17,123-5,168   
Schoenberg-Whitney.theorem 223, 236-8,294,302,305   
sign alternation in minimax approximation 77,79,87-8,98,112   
spline approximation $\pmb { B }$ -splines, see $\pmb { B }$ -splines basis functions 29-30,227-8,231-4 best in the least squares norm 240,296 best in the minimax norm 239-40 bicubic splines 226 definition of a spline function 29-30 derivative discontinuities 220,224, 261-5 extended space of spline functions 255-7 interpolation,see spline interpolation knots,see knots of spline functions local methods 225,243,246-51 methods of calculation 215-16,220, 222-4,238-9,257,261-6,307-8 natural splines,see natural splines neara singularity 254-7 order of convergence 30,241-6 perfect splines,see perfect splines uniform convergence 241-3 zeros of spline functions 230-1   
spline interpolation by a cubic spline 215-21, 224,261-6, 277-81 by a natural spline 219,285-6 bya perfect spline 294-5 by a quadratic spline 221-5,257-61, 282 cardinal functions 216-19,222-3

end conditions 216,219-21,223-5, 285 error bounds 277-82,309-10 error estimates for cubic splines 261-5 general data points 236-9,259-61 localization properties 218, 220-4, 246-7 norm of operator 218-19,225,257-9 on an infinite range 216-19,221-3, 277-80 optimal, see optimal interpolation recurrence relations 216,222-3,258 Schoenberg-Whitney theorem 236-8 to surfaces 226 uniqueness of solution 216, 237-8, 285-6 strict convexity 13-19 surface approximation 71,226

Tchebycheff,see Chebyshev   
telescoping 92,148   
third derivative discontinuities of cubic splines 220,224,261-5   
three term recurrence relation for orthogonal polynomials 131-3   
trigonometric polynomials,see also Fourier series approximation to discrete data 156-61 best in the $L _ { 1 }$ -norm 176 best in the least squares norm 152-3, 157-8 best in the minimax norm 162,196 interpolation 161 methods of calculation 156-61 order of convergence,see Jackson's theorems orthogonality conditions 153,158 quadrature 156-7 relation to algebraic polynomials 151- 2,195-8 uniform convergence 151-2,162-3, 190-1 zeros of trigonometric polynomials 15c 161   
unicity,see uniqueness   
uniform approximation,see minimax approximation   
uniform boundedness theorem 203-4   
uniform convergence of Bernstein approximations 66 linear operators 202-4 monotone operators 62-5,162-3 polynomial approximations 61-7, 196-7   
uniform convergence of (cont.) spline approximations 241-3 trigonometric approximations 151-2, 162-3,190-1   
uniqueness of best approximations 13-17 best $\scriptstyle { L _ { 1 } }$ approximations 170,175 best least squares approximations 17- 18,123-4,126 best minimax approximations 79-81, 108-9,113 general spline interpolation 237-8 $\scriptstyle { L _ { 1 } }$ interpolation points 170-2 natural spline functions 285-6 orthogonal polynomials 136-7 perfect splines 294-5,297, 312 polynomial interpolation 33-4, 54-5   
variational problems minimal properties of natural splines 287-90 minimal property of perfect splines 290-5 minimization of $\left\| s ^ { \prime \prime } \right\| _ { 2 }$ subject to interpolation conditions 283-5   
Weierstrass theorem 25,61-2,66-7,191   
zeros of error function in best $\scriptstyle { L _ { 1 } }$ approximation 169-72,182-3 functions in a Chebyshev set 76-7, 313-16 orthogonal polynomials 137-8, 147 spline functions 230-1 trigonometric polynomials 150,161


<!-- chunk 0006: pages 351-351 -->
Most functions that occur in mathematics cannot be used directly in computer calculations. Instead they are approximated by manageable functions such as polynomialsand piecewise polynomials.The general theory of the subject and itsapplication to polynomial roimtionare ascal,utpecewiseplls have become far more useful during the last twenty years.Thus many important theoretical properties have been found recently and many new techniques for the automatic calculation of approximationsto prescribedaccuracy havebeen developed.

This book gives a thorough and coherent introduction to the theory that is the basis of current approximation methods.Professor Powell describes and analyses the main techniques of calculation supplying sufficient motivation throughout the book to make it accessible to scientists and engineers who require approximation methods for practical needs.Because the book is based ona course of lectures to third-year undergraduates in mathematics at CambridgeUiversity,suficientattention isgiven totryto makeit highly suitable asa mathematical textbook atundergraduateorpostgraduatelevel.

Also issued in hardcovers Coverdesigned by James Butler
