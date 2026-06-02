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

![](images/dc40860ae2d24e735cd7f53fff3b397a867c6fb666e0f67c77843a5dc69b6da6.jpg)  
Figure 1.1. A function to be approximated.

![](images/4a97e856122ac3dd94086b4462e638957f717257228bacb08742766bb83503b6.jpg)  
Figure 1.2. Some data to be approximated.

![](images/8c49b53b047be022ce5822c9df836873f9528e06570e8a3e236dc107817ba928.jpg)  
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

![](images/db364ccd1837a9f69728b8949d889110f05c2e7660277dfb47a12520588475af.jpg)  
Figure 1.4. An approximation problem in ${ \mathcal { R } } ^ { 2 }$

![](images/94e3a375c5fa7d2291968fd1f304832df65ec7f7d79671368cb90851afe30316.jpg)  
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