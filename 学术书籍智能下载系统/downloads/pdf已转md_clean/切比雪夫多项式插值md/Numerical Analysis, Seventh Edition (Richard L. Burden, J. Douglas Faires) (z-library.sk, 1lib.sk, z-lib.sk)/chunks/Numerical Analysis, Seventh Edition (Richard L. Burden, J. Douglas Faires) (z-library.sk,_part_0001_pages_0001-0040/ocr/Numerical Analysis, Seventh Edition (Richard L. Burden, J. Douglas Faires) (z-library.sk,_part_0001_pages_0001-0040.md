# Preface

# About the Text

We have developed this material for a sequence of courses on the theory and application of numerical approximation techniques. The text is designed primarily for junior-level mathematics,science,and engineering majors who have completed at least the first year of the standard college calculus sequence. Familiarity with the fundamentals of matrix algebra and differential equations is also useful, but adequate introductory material on these topics is presented in the text so that those courses need not be prerequisites.

Previous editions of Numerical Analysis have been used in a wide variety of situations. In some cases, the mathematical analysis underlying the development of approximation techniques was emphasized rather than the methods themselves; in others,the emphasis was reversed. The book has also been used as the core reference for courses at the beginning graduate level in engineering and computer science programs,and in first-year courses in introductory analysis offered at international universities.We have tried to adapt the book to fit these diverse users without compromising our original purpose:

To give an introduction to modern approximation techniques; to explain how, why, and when they can be expected to work; and to provide a firm basis for future study of numerical analysis and scientific computing.

The book contains suficient material for a full year of study, but we expect many readers to use the text only for a single-term course. In such a course, students learn to identify the types of problems that require numerical techniques for their solution and see examples of the error propagation that can occur when numerical methods are applied. They accurately approximate the solutions of problems that cannot be solved exactly and learn techniques for estimating error bounds for the approximations.The remainder of the text serves as a reference for methods that are not considered in the course.Either the full-year or single-course treatment is consistent with the aims of the text.

Virtually every concept in the text is illustrated by example, and this edition contains more than 2,Ooo class-tested exercises ranging from elementary applications of methods and algorithms to generalizations and extensions of the theory. In addition, the exercise sets include many applied problems from diverse areas of engineering,as well as from the physical, computer, biological,and social sciences. The applications chosen demonstrate concisely how numerical methods can be,and often must be,applied in real-life situations.

A number of software packages have been developed to produce symbolic mathematical computations. Predominant among them in the academic environment are Derive@, Maple@,and Mathematica@. Student versions of these software packages are available at reasonable prices for most common computer systems. Although there are significant differences among the packages, both in performance and price,all can perform standard algebra and calculus operations. Having a symbolic computation package available can be very useful in the study of approximation techniques. The results in most of our examples and exercises have been generated using problems for which exact values can be determined, since this permits the performance of the approximation method to be monitored. Exact solutions can often be obtained quite easily using symbolic computation. In addition, for many numerical techniques the error analysis requires bounding a higher ordinary or partial derivative of a function, which can be a tedious task and one that is not particularly instructive once the techniques of calculus have been mastered. Derivatives can be quickly obtained symbolically, and a litle insight often permits a symbolic computation to aid in the bounding process as well.

We have chosen Maple as our standard package because of its wide distribution, but Derive or Mathematica can be substituted with only minor modifications.Examples and exercises have been added whenever we felt that a computer algebra system would be of significant benefit, and we have discussed the approximation methods that Maple employs when it is unable to solve a problem exactly.

The seventh edition includes two new major sections. The Preconditioned Conjugate Gradient method has been added to Chapter 7 to provide a more complete treatment of the numerical solution to systems of linear equations. It is presented as an iterative approximation technique for solving positive definite linear systems. In this form, it is particularly useful for approximating the solution to large sparse systems.

In Chapter 10 we have added a section on Homotopy and Continuation methods. These methods provide a distinctly different technique for approximating the solutions to nonlinear systems of equations, one that has attracted a great deal of attention recently.

We have also added extensive listings of Maple code throughout the book, since reviewers found this feature useful in the sixth edition. We have updated all the Maple code to Release 6, the version that will be current by the time the book is printed. Those familiar with our past editions will find that virtually every page has been improved in some way. All the references have.been updated and revised, and new exercises have been added. We hope you will find these changes beneficial to the teaching and study of numerical anal-ysis; most have been motivated by changes in the presentation of the material to our own students.

Another important modification in this edition is a web site at

# http://www.as.ysu.edu/\~faires/Numerical-Analysis/

On this web site we will place updated programs as the software changes and post responses to comments made by users of the book. We can also add new material that might be included in subsequent editions in the form of PDF files that users can download. Our hope is that this will extend the life of the seventh edition while keeping the material in the book up to date.

# Algorithms

As in previous editions, we give a detailed, structured algorithm without program listing for each method in the text. The algorithms are in a form that can be coded, even by those with limited programming experience.

This edition includes a disk containing programs for solutions to representative exercises using the algorithms. The programs for each algorithm are written in Fortran, Pascal, and C. In addition, we have coded the programs using Maple and Mathematica, as well as in MATLAB, a computer software package that is widely used for linear algebra applications. This should ensure that a set of programs is available for most common computing systems.

A Student Study Guide is available with this edition that illustrates the calls required for these programs, which is useful for those with limited programming experience. The study guide also contains worked-out solutions to many of the problems.

Brooks/Cole can provide instructors with an Instructor's Manual that provides answers and solutions to allthe exercises in the book. Computation results in the Instructor's Manual were regenerated for this edition, using the programs on the disk to ensure compatibility among the various programming systems.

The algorithms in the text lead to programs that give correct results for the examples and exercises in the text, but no attempt was made to write general-purpose professional software.Specifically,the algorithms are not always written in a form that leads to the most efficient program in terms of either time or storage requirements. When a conflict occurred between writing an extremely efficient algorithm and writing a slightly different one that better illustrates the important features of the method, the latter path was invariably taken.

The CD on the inside back cover of the book contains programs for all the algorithms in the book, in numerous formats,as wellas samples of the Student Study Guide for the book in both the PostScript@ (PS) and the Adobe@ Portable Document (PDF) formats.

For each algoithm there is a C, Fortran, Maple,Mathematica, MATLAB,and Pascal program, and for some of these systems there are multiple programs that depend on the particular version of the software that is being run. Every program is illustrated with a sample problem that is closely correlated to the text. This permits the program to be run initially in the language of your choice to see the form of the input and output. The pro-grams can then be modified for other problems by making minor changes.The form of the input and output are, as nearly as possible, the same in each of the programming systems. This permits an instructor using the programs to discuss them generically, without regard to the particular programming system an individual student uses.

The programs are designed to run on a minimally configured computer. All that is re-quired is a computer running MS-DOS@, Windows@,or the Macintosh@ operating system. You will, however, need appropriate software,such as a compiler for Pascal, Fortran, and C,or one of the computer algebra systems (Maple, Mathematica, and MATLAB). There are six subdirectories on the disk, one for each of the computer languages and the accompanying data files.

All of the programs are given as ASCI files or worksheets. They can be altered using any editor or word processor that creates a standard ASCI fle. (These are also commonly called “Text Only”files.)

Extensive README files are included with the program files so that the peculiarities of the various programming systems can be individually addressed. The README files are presented both in ASCII format and as PDF files.As new software is developed, the algorithms will be updated and placed on the web site for the book.

Numerical Analysis is designed to allow instructors flexibility in the choice of topics,as well as in the level of theoretical rigor and in the emphasis on applications. In line with these aims,we provide detailed references for the results that are not demonstrated in the text and for the applications that are used to indicate the practical importance of the methods.The text references cited are those most likely to be available in college libraries and have been updated to reflect the most recent edition at the time this book was placed into production. We also include quotations from original research papers when we feel this material is accessible to our intended audience.

The following flowchart indicates chapter prerequisites. The only deviation from this chart is described in the footnote at the bottom of the first page of Section 3.4. Most of the possible sequences that can be generated from this chart have been taught by the authors at Youngstown State University.

![](images/53986f7524756f4e9ce0f7c3a6eac7703b67badac1c7afda312dae10c1576fc2.jpg)

# Acknowledgments

We feel most fortunate to have had so many of our students and collagues communicate with us regarding their impressions of earlier editions of this book. All of these comments are taken very seriously; we have tried to include allthe suggestions that are in line with the philosophy of the book,and are extremely grateful to all those that have taken the time to contact us and inform us of improvements we can make in subsequent versions.

We would particularly like to thank the following, whose efforts we greatly appreciate.

Glen Granzow, Idaho State University   
Jose Miguel, Universidad Peruana Cayetano Heredia, Lima, Peru   
John M. Neuberger, Northern Arizona University   
L. G. de Pillis, Harvey Mudd College

We want especially to thank our friend and former student Jim Baglama of Ball State University. Jim agreed to be an extensive reviewer for this edition and was particularly helpful in updating our survey sections and references to software. It is most gratifying to see one's students move through the profession.

Also moving through his profession,but in a completly different manner,is our Editor and Publisher Gary Ostedt. Gary has been an outstanding manager of our projects and a good personal friend.We will very much miss his direction and assistance,and would like to take this opportunity to wish him all the best in his upcoming retirement from Brooks/Cole.

As has been our practice in past editions of the book,we have used student help at Youngstown State University in preparing the seventh edition. Our able assistant for this edition was Laurie Marinelli，,whom we thank for all her work. We would also like to express gratitude to our colleagues on the faculty and administration of Youngstown State University for providing us the opportunity and facilities to complete this project.

Finally, we would like to thank all those who have used and adopted the various edi-tions of Numerical Analysis over the years. It has been wonderful to hear from so many students,and new faculty,who used our book for their first exposure to the study of numerical methods.We hope this edition continues the trend and adds to the enjoyment of students studying numerical analysis. If you have any suggestions for improvements that can be incorporated into future editions of the book, we would be grateful for your com-ments. We can be contacted by electronic mail at the addresses listed below.

Richard L.Burden burden @math.ysu.edu

J. Douglas Faires faires @math.ysu.edu

![](images/45e6ab13c563012d045fc62777e55ef42e2039ef44c0f034b4d308278b436cd6.jpg)

# Contents

# 1 Mathematical Preliminaries1

1.1 Review of Calculus 2   
1.2 Roundoff Errors and Computer Arithmetic18   
1.3 Algorithms and Convergence31   
1.4 Numerical Software 40

# 2 Solutions of Equations in One Variable 47

2.1 The Bisection Method 48   
2.2 Fixed-Point Iteration55   
2.3 Newton's Method 66   
2.4 Error Analysis for Iterative Methods78   
2.5 Accelerating Convergence86   
2.6 Zeros of Polynomials and Muller's Method91   
2.7 Survey of Methods and Software 101

# 3 Interpolation and Polynomial Approximation 104

3.1 Interpolation and the Lagrange Polynomial107   
3.2 Divided Differences 122   
3.3 Hermite Interpolation 133   
3.4 Cubic Spline Interpolation 141   
3.5 Parametric Curves156   
3.6 Survey of Methods and Software163

# 4 Numerical Differentiation and Integration166

4.1 Numerical Differentiation 167   
4.2 Richardson's Extrapolation178   
4.3 Elements of Numerical Integration 186   
4.4 Composite Numerical Integration 196   
4.5 Romberg Integration 207   
4.6 Adaptive Quadrature Methods 213   
4.7 Gaussian Quadrature 220   
4.8 Multiple Integrals 227   
4.9 Improper Integrals 241   
4.10 Survey of Methods and Software 247

# 5 Initial-Value Problems for Ordinary Differential Equations 249

5.1 The Elementary Theory of Initial-Value Problems251   
5.2 Euler's Method 256   
5.3 Higher-Order Taylor Methods 266   
5.4 Runge-Kutta Methods 272   
5.5 Error Control and the Runge-Kutta-Fehlberg Method 282   
5.6 Multistep Methods 289   
5.7 Variable Step-Size Multistep Methods301   
5.8 Extrapolation Methods 307   
5.9 Higher-Order Equations and Systems of Differential Equations313   
5.10 Stability 324   
5.11 Stiff Differential Equations334   
5.12 Survey of Methods and Software 342

# 6 Direct Mysteods for Solving

6.1 Linear Systems of Equations 345   
6.2 Pivoting Strategies 359   
6.3 Linear Algebra and Matrix Inversion 370   
6.4 The Determinant of a Matrix 383   
6.5 Matrix Factorization 388   
6.6 Special Types of Matrices398   
6.7 Survey of Methods and Software 413

# 7 Iterative Techniques in Matrix Algebra 417

7.1 Norms of Vectors and Matrices418   
7.2 Eigenvalues and Eigenvectors430   
7.3 Iterative Techniques for Solving Linear Systems437   
7.4 Error Bounds and Iterative Refinement 454   
7.5 The Conjugate Gradient Method 465   
7.6 Survey of Methods and Software 481

# 8 Approximation Theory 483

8.1 Discrete Least Squares Approximation 484   
8.2 Orthogonal Polynomials and Least Squares Approximation498   
8.3 Chebyshev Polynomials and Economization of Power Series507   
8.4 Rational Function Approximation 517   
8.5 Trigonometric Polynomial Approximation 529   
8.6 Fast Fourier Transforms537   
8.7 Survey of Methods and Software 548

# 9 Approximating Eigenvalues550

9.1 Linear Algebra and Eigenvalues 551   
9.2 The Power Method 560   
9.3 Householder's Method 577   
9.4 The QR Algorithm 585   
9.5 Survey of Methods and Software597

# 10 Numerical Solutions of Nonlinear Systems of Equations 600

10.1 Fixed Points for Functions of Several Variables602   
10.2 Newton's Method 611   
10.3 Quasi-Newton Methods  620   
10.4 Steepest Descent Techniques628   
10.5 Homotopy and Continuation Methods635   
10.6 Survey of Methods and Software643

# 11 Boundary-Value Problems for Ordinary Differential Equations 645

11.1 The Linear Shooting Method 646   
11.2 The Shooting Method for Nonlinear Problems653   
11.3 Finite-Difference Methods for Linear Problems660   
11.4 Finite-Difference Methods for Nonlinear Problems667   
11.5 The Rayleigh-Ritz Method 672   
11.6 Survey of Methods and Software 688

# 12 Numerical Solutions to Partial Differential Equations691

12.1 Elliptic Partial Differential Equations694   
12.2 Parabolic Partial Differential Equations704   
12.3 Hyperbolic Partial Differential Equations718   
12.4 An Introduction to the Finite-Element Method 726   
12.5 Survey of Methods and Software741

# Bibliography 743

# Answers to Selected Exercises 753

Index 831

CHAPTER

# 1

# Mathematical Preliminaries

IN beginning chemistry courses, we see the ideal gas law,

$$
P V = N R T ,
$$

which relates the pressure P, volume V, temperature T, and number of moles N of an “ideal" gas. In this equation, R is a constant that depends on the measurement system.

Suppose two experiments are conducted to test this law, using the same gas in each case. In the first experiment,

$$
\begin{array} { l l } { { P = 1 . 0 0 \mathrm { a t m } , } } & { { V = 0 . 1 0 0 \mathrm { m } ^ { 3 } , } } \\ { { { } } } & { { { } } } \\ { { N = 0 . 0 0 4 2 0 \mathrm { m o l } , } } & { { R = 0 . 0 8 2 0 6 . } } \end{array}
$$

The ideal gas law predicts the temperature of the gas to be

$$
T = { \frac { P V } { N R } } = { \frac { ( 1 . 0 0 ) ( 0 . 1 0 0 ) } { ( 0 . 0 0 4 2 0 ) ( 0 . 0 8 2 0 6 ) } } = 2 9 0 . 1 5 \mathrm { K } = 1 7 ^ { \circ } \mathbf { C } .
$$

When we measure the temperature of the gas, we find that the true tem-perature is ${ \bf 1 5 ^ { \circ } C } .$

![](images/a44d6879a1013dd8479076f8ca7881de9b45d66b215a7a7672af55709620c7fa.jpg)

![](images/ecb6f6c9170bc5bc3fad6dd0158e2b77a6288c52ca876de37d38d30a9bada1bf.jpg)

We then repeat the experiment using the same values of $\pmb R$ and $N$ ， but increase the pressure by a factor of two and reduce the volume by the same factor. Since the product $\pmb { P V }$ remains the same, the predicted temperature is still $\bf { 1 7 ^ { \circ } C }$ , but we find that the actual temperature of the gas is now $\mathbf { 1 9 ^ { \circ } C }$ ·

Clearly, the ideal gas law is suspect, but before concluding that the law is invalid in this situation, we should examine the data to see whether the error can be attributed to the experimental results. If so, we might be able to determine how much more accurate our experimental results would need to be to ensure that an error of this magnitude could not occur.

Analysis of the error involved in calculations is an important topic in numerical analysis and is introduced in Section 1.2. This particular application is considered in Exercise 28 of that section.

This chapter contains a short review of those topics from elementary single-variabie calculus that will be needed in later chapters, together with an introduction to convergence, error analysis, and the machine representation of numbers.

# 1.1 Review of Calculus

The concepts of limit and continuity of a function are fundamental to the study of calculus.

# Definition 1.1

A function $f$ defined on a set $X$ of real numbers has the limit $L$ at $\pmb { x _ { 0 } }$ , written

$$
\operatorname* { l i m } _ { x \to x _ { 0 } } f ( x ) = L ,
$$

if, given any real number $\epsilon > 0$ ,there exists a real number $\delta > 0$ such that $| f ( x ) - L | < \epsilon ,$ whenever $x \in X$ and $0 < | { \boldsymbol { x } } - { \boldsymbol { x } } _ { 0 } | < \delta$ . (See Figure 1.1.)

# Definition 1.2

Let $f$ be a function defined on a set $X$ of real numbers and $x _ { 0 } \in X$ . Then $f$ is continuous at $x _ { 0 }$ if

$$
\operatorname * { l i m } _ { x \to x _ { 0 } } f ( x ) = f ( x _ { 0 } ) .
$$

The function $f$ is continuous on the set $X$ if it is continuous at each number in $\pmb { X }$

![](images/e9241bf09ce4199b6ad7bee9d54f36053488ea3d6f74d354239b354bbca62268.jpg)  
Figure 1.1

$C ( X )$ denotes the set of allfunctions that are continuous on $X$ . When $X$ is an interval of the real line,the parentheses in this notation are omitted. For example,the set of all functions continuous on the closed interval $[ a , b ]$ is denoted $C [ a , b ]$

The limit of a sequence of real or complex numbers is defined in a similar manner.

# Definition 1.3

Let $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ be an infinite sequence ofreal orcomplex numbers.The sequence $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ has the limit $\pmb { x }$ (converges to $\pmb { x }$ ) if, for any $\epsilon > 0$ ,there exists a positive integer $N ( \epsilon )$ such that $| x _ { n } - x | < \epsilon$ , whenever $n > N ( \epsilon )$ . The notation

$$
\operatorname* { l i m } _ { n \to \infty } x _ { n } = x , \quad { \mathrm { o r } } \quad x _ { n } \to x \quad { \mathrm { a s } } \quad n \to \infty ,
$$

means that the sequence $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ converges to $x$

The following theorem relates the concepts of convergence and continuity.

# Theorem 1.4

If $f$ is a function defined on a set $X$ of real numbers and $x _ { 0 } ~ \in ~ X$ , then the following statements are equivalent:

a. $f$ is continuous at $\pmb { x _ { 0 } }$ ； b.If $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ is any sequence in $\pmb { X }$ converging to $x _ { 0 }$ , then $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f ( x _ { n } ) = f ( x _ { 0 } ) } \end{array}$

The functions we consider when discussing numerical methods are assumed to be continuous since this is a minimal requirement for predictable behavior. Functions that are not continuous can skip over points of interest, which can cause diffculties when attempting to approximate a solution to a problem. More sophisticated assumptions about a function generally lead to better approximation results. For example, a function with a smooth graph willnormally behave more predictably than one with numerous jagged features.The smoothness condition relies on the concept of the derivative.

# Definition 1.5

Let $f$ be a function defined in an open interval containing $x _ { 0 }$ . The function $f$ is differentiable at $x _ { 0 }$ if

$$
f ^ { \prime } ( x _ { 0 } ) = \operatorname* { l i m } _ { x \to x _ { 0 } } { \frac { f ( x ) - f ( x _ { 0 } ) } { x - x _ { 0 } } }
$$

exists. The number $f ^ { \prime } ( x _ { 0 } )$ is called the derivative of $f$ at $x _ { 0 }$ . A function that has a derivative at each number in a set $\pmb { X }$ is differentiable on $X$

The derivative of $f$ at $x _ { 0 }$ is the slope of the tangent line to the graph of $f$ at $( x _ { 0 } , f ( x _ { 0 } ) )$ ， as shown in Figure 1.2.

![](images/de96346942bb899f8998d6e25174c2849b2b586d9c556e38238aea6d027bfd58.jpg)  
Figure 1.2

If the function $f$ is differentiable at $\pmb { x _ { 0 } }$ ,then $f$ is continuous at $x _ { 0 }$ ·

The set of all functions that have $\pmb { n }$ continuous derivatives on $X$ is denoted $C ^ { n } ( X )$ , and the set of functions that have derivatives of all orders on $\pmb { X }$ is denoted $C ^ { \infty } ( X )$ .Polynomial, rational, trigonometric, exponential, and logarithmic functions are in $C ^ { \infty } ( X )$ ，where $X$ consists of all numbers for which the functions are defined. When $\pmb { X }$ is an interval of the real line, we will again omit the parentheses in this notation.

The next theorems are of fundamental importance in deriving methods for error estimation. The proofs of these theorems and the other unreferenced results in this section can be found in any standard calculus text.

# Theorem 1.7

# (Rolle's Theorem)

Suppose $f \in C [ a , b ]$ and $f$ is differentiable on $( a , b )$ .If $f ( a ) = f ( b )$ , then a number $c$ in $( a , b )$ exists with $f ^ { \prime } ( c ) = 0$ . (See Figure 1.3.)

![](images/139b37428ac06dd923a3de3971f71afdf90c0d2a2345d25e8c752a5f75a953f2.jpg)  
Figure 1.3

# Theorem 1.8

# (Mean Value Theorem)

If $f \in C [ a , b ]$ and $f$ is differentiable on $( a , b )$ , then a number $c$ in $( a , b )$ exists with

$$
f ^ { \prime } ( c ) = { \frac { f ( b ) - f ( a ) } { b - a } } .
$$

![](images/a4123ef7d7579829c05ddb624dd1574a4f06d2fc0a74b27ceff6427cfbf075d2.jpg)  
Figure 1.4

# Theorem 1.9

# (Extreme Value Theorem)

If $f \in C [ a , b ]$ ，then $c _ { 1 } , c _ { 2 } \in [ a , b ]$ exist with $f ( c _ { 1 } ) \leq f ( x ) \leq f ( c _ { 2 } )$ ,for all $x \in \{ a , b \}$ In addition, if $f$ is differentiable on $( a , b )$ , then the numbers $c _ { 1 }$ and $c _ { 2 }$ occur either at the endpoints of $[ a , b ]$ or where $f ^ { \prime }$ is zero. (See Figure 1.5.)

As mentioned in the preface, we willuse the computeralgebra system Maple whenever appropriate. Computer algebra systems are particularly useful for symbolic differentiation and ploting graphs. Both techniques are illstrated in Example 1.

![](images/c760d92e1258d1a85640c8a077f44b5315693536be8bbf2276bad4ee660aaa08.jpg)  
Figure 1.5

Find $\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$ for

$$
f ( x ) = 5 \cos 2 x - 2 x \sin 2 x
$$

on the intervals [1,2] and [0.5,1].

We first ilustrate the graphing capabilities of Maple. To access the graphing package, enter the command

>with(plots);

The commands within the package are then displayed. We define $f$ by entering

$$
> \pounds : = { \mathsf { \Omega } } 5 * \mathsf { c o s } \left( 2 * \ x \right) - 2 * \ x * \mathsf { s i n } \left( 2 * \ x \right) ;
$$

The response from Maple is

$$
f : = 5 \cos ( 2 x ) - 2 x \sin ( 2 x )
$$

To graph $f$ on the interval [0.5, 2], use the command

>plot(f,x=0.5..2);

The graph appears as shown in Figure 1.6,and we can determine the coordinates of any point of the graph by moving the mouse pointer to the desired point and clicking the left mouse button. This technique can be used to estimate axis intercepts and extrema of functions.

We complete the example using the Extreme Value Theorem. First, consider the interval [1,2].To obtain the first derivative $g = f ^ { \prime }$ ,enter

Maple gives

$$
g : = - 1 2 \sin ( 2 x ) - 4 x \cos ( 2 x )
$$

![](images/c633fe879a693be5e421ca49a8c42b991844557a21766731bd8269518b1e387f.jpg)  
Figure 1.6

We can then solve $g ( x ) = 0$ ,for $1 \leq x \leq 2$ , with the command

>fsolve $( \mathbf { g } , \mathbf { x } , 1 \ldots 2 )$ ；

obtaining 1.358229874,and compute f(1.358229874) using

>evalf(subs( $x = 1$ .358229874,f));

Since $f ( 1 ) = - 3 . 8 9 9 3 2 9 0 3 7$ and $f ( 2 ) = - 0 . 2 4 1 0 0 8 1 2 4$ ， we have, for the interval [1,2], a maximum value of $f ( 2 ) = - 0 . 2 4 1 0 0 8 1 2 4$ as illustrated in Figure 1.7, and a

![](images/882c482baae6a533eb388c65cf7437eb38b8426757f1ae12509eb2bdc7f97563.jpg)  
Figure 1.7

minimum of approximately $f ( 1 . 3 5 8 2 2 9 8 7 4 ) = - 5 . 6 7 5 3 0 1 3 3 8 . \mathrm { H e n c e } ,$

$$
\operatorname* { m a x } _ { 1 \leq x \leq 2 } | 5 \cos 2 x - 2 x \sin 2 x | \approx | f ( 1 . 3 5 8 2 2 9 8 7 4 ) | = 5 . 6 7 5 3 0 1 3 3 8 .
$$

If we try to solve $g ( x ) = 0$ ,for $0 . 5 \leq x \leq 1$ , we find that when we enter >fsolve(g,x,0.5..1);

Maple responds with

$$
\mathrm { f s o l v e } ( - 1 2 \sin ( 2 x ) - 4 x \cos ( 2 x ) , x , . 5 . 1 )
$$

which indicates that Maple could not find a solution in [0.5,1].If you graph $g$ , you will see that there is no solution in this interval, and the maximum occurs at an endpoint. Hence, $f ^ { \prime }$ is never O in [0.5,1],as shown in Figure 1.8,and, since $f ( 0 . 5 ) = 1 . 8 6 0 0 4 0 5 4 5$ and $f ( 1 ) = - 3 . 8 9 9 3 2 9 0 3 7$ ,we have

$$
\operatorname* { m a x } _ { 0 . 5 \le x \le 1 } | 5 \cos 2 x - 2 x \sin 2 x | = | f ( 1 ) | = 3 . 8 9 9 3 2 9 0 3 7 .
$$

![](images/636a43bec9592f6dd820b81c101fec77d91405656bf6e227c0d651c216a11c62.jpg)  
Figure 1.8

The other basic concept of calculus that willbe used extensively is the Riemann integral.

Ition 1.10The Riemann integral of the function $f$ on the interval $[ a , b ]$ is the following limit, provided it exists:

$$
\int _ { a } ^ { b } f ( x ) d x = \operatorname* { l i m } _ { \operatorname* { m a x } \Delta x _ { i } \to 0 } \sum _ { i = 1 } ^ { n } f ( z _ { i } ) \Delta x _ { i } ,
$$

where the numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ satisfy $a = x _ { 0 } \leq x _ { 1 } \leq \cdots \leq x _ { n } = b$ ，and where $\Delta x _ { i } = x _ { i } - x _ { i - 1 }$ , for each $i = 1 , 2 , \dots , n$ ,and $z _ { i }$ is arbitrarily chosen in the interval $\{ x _ { i - 1 } , x _ { i } \}$

Every continuous function $f$ on $[ a , b ]$ is Riemann integrable on $[ a , b ]$ . This permits us to choose, for computational convenience, the points $x _ { i }$ to be equally spaced in $[ a , b ]$ ， and for each $i = 1 , 2 , \ldots , n$ ,to choose $z _ { i } = x _ { i }$ . In this case,

$$
\int _ { a } ^ { b } f ( x ) d x = \operatorname* { l i m } _ { n \to \infty } { \frac { b - a } { n } } \sum _ { i = 1 } ^ { n } f ( x _ { i } ) ,
$$

where the numbers shown in Figure 1.9 as $x _ { i }$ are $x _ { i } = a + i ( b - a ) / n$

![](images/d9378d4b25f0751896da88c5d1c67a9926ac9d8dd9e2ab338e7f5b1d41784d0d.jpg)  
Figure 1.9

Two other results wil be needed in our study of numerical analysis. The first is a generalization of the usual Mean Value Theorem for Integrals.

# (Weighted Mean Value Theorem for Integrals)

Suppose $f \in C [ a , b ]$ , the Riemann integral of $\pmb { g }$ exists on $[ a , b ]$ ,and $g ( x )$ does not change sign on $[ a , b ]$ . Then there exists a number $\pmb { c }$ in $( a , b )$ with

$$
\int _ { a } ^ { b } f ( x ) g ( x ) d x = f ( c ) \int _ { a } ^ { b } g ( x ) d x .
$$

When $g ( x ) \equiv 1$ ,Theorem 1.11 is the usual Mean Value Theorem for Integrals. It gives the average value of the function $f$ over the interval $[ a , b ]$ as

$$
f ( c ) = { \frac { 1 } { b - a } } \int _ { a } ^ { b } f ( x ) d x .
$$

![](images/633699caf5bc310d3debdd61f4b309f0e98e1a7010f0980db7ae75ef05053203.jpg)  
Figure 1.10

The proof of Theorem 1.11 is not generally given in a basic calculus course but can be found in most analysis texts (see,for example,[Fu, p. 162]).

The other theorem we will need that is not generally presented in a basic calculus course is derived by applying Rolle's Theorem successively to $f , \ f ^ { \prime }$ ,..., and, finally, to $f ^ { ( n - 1 ) }$ .

# Theorem 1.12

# (Generalized Rolle's Theorem)

Suppose $f \in C \{ a , b \}$ is $\pmb { n }$ times differentiable on $( a , b )$ .If $f ( x )$ is zero at the $n + 1$ distinct numbers $\pmb { x _ { 0 } }$ ，.， $x _ { n }$ in $[ a , b ]$ , then a number $c$ in $( a , b )$ exists with $f ^ { ( n ) } ( c ) = 0$ ■

The next theorem is the Intermediate Value Theorem. Although its statement seems reasonable, the proof is beyond the scope of the usual calculus course. It can, however, be found in most analysis texts (see,for example,[Fu, p. 67]).

# Theorem 1.13

# (Intermediate Value Theorem)

f $f \in C [ a , b ]$ and $\pmb { K }$ is any number between $f ( a )$ and $f ( b )$ , then there exists a number $c$ in $( a , b )$ for which $f ( c ) = K$

Figure 1.11 shows one choice for the number that is guaranteed by the Intermediate Value Theorem. In this example there are two other possibilities.

![](images/2a9831638a6cb5d81c837bba309288daebeb717f7272e6f9d93d2c77df375bb6.jpg)  
Figure 1.11

# EXAMPLE 2

To show that $x ^ { 5 } - 2 x ^ { 3 } + 3 x ^ { 2 } - 1 = 0$ has a solutionin the interal [O,1],cosider $f ( x ) =$ $x ^ { 5 } - 2 x ^ { 3 } + 3 x ^ { 2 } - 1$ . Since

$$
f ( 0 ) = - 1 < 0 < 1 = f ( 1 )
$$

and $f$ is continuous,the Intermediate Value Theorem implies that a number $x$ exists with $0 < x < 1$ ,for which $x ^ { 5 } - 2 x ^ { 3 } + 3 x ^ { 2 } - 1 = 0$

As seen in Example 2,the Intermediate Value Theorem is used to determine when solutions to certain problems exist. It does not, however, give an eficient means for finding these solutions. This topic is considered in Chapter 2.

The final theorem in this review from calculus describes the Taylor polynomials. These polynomials are used extensively in numerical analysis.

# Theorem 1.14 (Taylor's Theorem)

Suppose $f \in C ^ { n } [ a , b ]$ ,that $f ^ { ( n + 1 ) }$ exists on $[ a , b ]$ ,and $x _ { 0 } \in [ a , b ]$ . For every $x \in [ a , b ]$ ， there exists a number $\xi ( x )$ between $x _ { 0 }$ and $x$ with

$$
f ( x ) = P _ { n } ( x ) + R _ { n } ( x ) ,
$$

where

$$
{ \begin{array} { l } { P _ { n } ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + { \frac { f ^ { \prime \prime } ( x _ { 0 } ) } { 2 ! } } ( x - x _ { 0 } ) ^ { 2 } + \cdot \cdot \cdot + { \frac { f ^ { ( n ) } ( x _ { 0 } ) } { n ! } } ( x - x _ { 0 } ) ^ { n } } \\ { \displaystyle \qquad = \sum _ { k = 0 } ^ { n } { \frac { f ^ { ( k ) } ( x _ { 0 } ) } { k ! } } ( x - x _ { 0 } ) ^ { k } } \end{array} }
$$

and

$$
R _ { n } ( x ) = { \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } } ( x - x _ { 0 } ) ^ { n + 1 } .
$$

Here $P _ { n } ( x )$ is called the nth Taylor polynomial for $f$ about $x _ { 0 }$ ,and $R _ { n } ( x )$ is called the remainder term (or truncation error) associated with $P _ { n } ( x )$ . The infinite series obtained by taking the limit of $P _ { n } ( x )$ as $n  \infty$ is called the Taylor series for $f$ about $x _ { 0 }$ . In the case $x _ { 0 } = 0$ , the Taylor polynomial is often called a Maclaurin polynomial, and the Taylor series is called a Maclaurin series.

The term truncation error refers to the error involved in using atruncated, or fiite, summation to approximate the sum of an infinite series.

Determine (a) the second and (b) the third Taylor polynomials for $f ( x ) = \cos x$ about $x _ { 0 } = 0$ ,and use these polynomials to approximate cos(0.01). (c) Use the third Taylor polynomial anditsremander term toapproximate $\begin{array} { r } { \int _ { 0 } ^ { 0 . 1 } \cos x \ d x } \end{array}$

Since $f \in C ^ { \infty } ( \mathbb { R } )$ , Taylor's Theorem can be applied for any $n \geq 0$ Also,

$$
f ^ { \prime } ( x ) = - \sin x , ~ f ^ { \prime \prime } ( x ) = - \cos x , ~ f ^ { \prime \prime } ( x ) = \sin x \quad \mathrm { a n d } \quad f ^ { ( 4 ) } ( x ) = \cos x ,
$$

$$
f ( 0 ) = 1 , \ f ^ { \prime } ( 0 ) = 0 , \ f ^ { \prime \prime } ( 0 ) = - 1 \quad \mathrm { a n d } \quad f ^ { \prime \prime \prime } ( 0 ) = 0 .
$$

a. For ${ n = 2 }$ and $x _ { 0 } = 0$ ,we have

$$
\cos x = 1 - { \frac { 1 } { 2 } } x ^ { 2 } + { \frac { 1 } { 6 } } x ^ { 3 } \sin \xi ( x ) ,
$$

where $\xi ( x )$ is a number between O and $\pmb { x }$ . (See Figure 1.12.)

![](images/a18fdd37361a34f5468cf7b3295accb4bc1d01a1c86b502d95f98e16830255ef.jpg)  
Figure 1.12

With ${ x = 0 . 0 1 }$ ,the Taylor polynomial and remainder term are

$$
\begin{array} { c } { { \cos 0 . 0 1 = 1 - { \displaystyle \frac { 1 } { 2 } } ( 0 . 0 1 ) ^ { 2 } + { \displaystyle \frac { 1 } { 6 } } ( 0 . 0 1 ) ^ { 3 } \sin \xi ( x ) } } \\ { { = 0 . 9 9 9 9 5 + 0 . 1 \overline { { 6 } } \times 1 0 ^ { - 6 } \sin \xi ( x ) , } } \end{array}
$$

where $0 < \xi ( x ) < 0 . 0 1$ . (The bar over the 6 in O.16 is used to indicate that this digit repeats indefinitely.） Since $| \sin \xi ( x ) | < 1$ for all $\pmb { x }$ , we have

$$
| \cos { 0 . 0 1 } - 0 . 9 9 9 9 5 | \le 0 . 1 \overline { { 6 } } \times 1 0 ^ { - 6 } ,
$$

so the approximation O.99995 matches at least the first five digits of cos O.01,and

$$
\begin{array} { r l } & { 0 . 9 9 9 9 4 8 3 < 0 . 9 9 9 9 5 - 1 . { \overline { { 6 } } } \times 1 0 ^ { - 6 } \leq \cos 0 . 0 1 \leq 0 . 9 9 9 9 5 + 1 . { \overline { { 6 } } } \times 1 0 ^ { - 6 } } \\ & { \qquad < 0 . 9 9 9 9 5 1 7 . } \end{array}
$$

The error bound is much larger than the actual error. This is due in part to the poor bound we used for $| \sin \xi ( x ) |$ . It can be shown that for all values of $x$ ， we have $| \sin x | \leq | x |$ . Since $0 \le \xi < 0 . 0 1$ ， we could have used the fact that $| \sin \xi ( x ) | \le 0 . 0 1$ in the error formula, producing the bound $0 . 1 \overline { { 6 } } \times 1 0 ^ { - 8 }$

b. Since $f ^ { \prime \prime \prime } ( 0 ) = 0$ , the third Taylor polynomial with remainder term about $x _ { 0 } = 0$ is

$$
\cos x = 1 - \frac { 1 } { 2 } x ^ { 2 } + \frac { 1 } { 2 4 } x ^ { 4 } \cos \tilde { \xi } ( x ) ,
$$

where $\mathbf { 0 < \tilde { \xi } } ( x ) < 0 . 0 1$ . The approximating polynomial remains the same, and the approximation is still 0.99995,but we now have a much better accuracy assurance. Since $| \cos \tilde { \xi } ( x ) \} \le 1$ for all $\pmb { x }$ , we have

$$
\left| \frac { 1 } { 2 4 } x ^ { 4 } \cos { \xi } ( x ) \right| \le \frac { 1 } { 2 4 } ( 0 . 0 1 ) ^ { 4 } ( 1 ) \approx 4 . 2 \times 1 0 ^ { - 1 0 } .
$$

So

$$
| \cos 0 . 0 1 - 0 . 9 9 9 9 5 | \le 4 . 2 \times 1 0 ^ { - 1 0 } ,
$$

and

$$
\begin{array} { r l } { 0 . 9 9 9 9 4 9 9 9 9 5 8 = 0 . 9 9 9 9 9 5 - 4 . 2 \times 1 0 ^ { - 1 0 } } & { } \\ { \leq \cos 0 . 0 1 \leq 0 . 9 9 9 9 5 + 4 . 2 \times 1 0 ^ { - 1 0 } = 0 . 9 9 9 9 5 0 0 0 4 2 . } & { } \end{array}
$$

The first two parts of this example illustrate the two objectives of numerical analysis.The first is to find an approximation, which the Taylor polynomials in both parts provide. The second is to determine the accuracy of the approximation. In this case, the third Taylor polynomial was much more informative than the second, even though both polynomials gave the same approximation.

c.Using the third Taylor polynomial gives

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 0 . 1 } \cos { x } d x = \int _ { 0 } ^ { 0 . 1 } \left( 1 - \frac 1 2 x ^ { 2 } \right) d x + \frac 1 { 2 4 } \int _ { 0 } ^ { 0 . 1 } x ^ { 4 } \cos { \tilde { \xi } } ( x ) d x } \\ { \displaystyle \qquad = \left[ x - \frac 1 6 x ^ { 3 } \right] _ { 0 } ^ { 0 . 1 } + \frac 1 { 2 4 } \int _ { 0 } ^ { 0 . 1 } x ^ { 4 } \cos { \tilde { \xi } } ( x ) d x } \\ { \displaystyle \qquad = 0 . 1 - \frac 1 6 ( 0 . 1 ) ^ { 3 } + \frac 1 { 2 4 } \int _ { 0 } ^ { 0 . 1 } x ^ { 4 } \cos { \tilde { \xi } } ( x ) d x . } \end{array}
$$

Therefore,

$$
\int _ { 0 } ^ { 0 . 1 } \cos { x } d x \approx 0 . 1 - { \frac { 1 } { 6 } } ( 0 . 1 ) ^ { 3 } = 0 . 0 9 9 8 { \overline { { 3 } } } .
$$

A bound for the error in this approximation is determined from the integral of the Taylor remainder term and the fact that $| \cos \tilde { \xi } ( x ) | \le 1$ for all $\pmb { x }$ ：

$$
\begin{array} { r l r } & { } & { \displaystyle \frac { 1 } { 2 4 } \bigg | \int _ { 0 } ^ { 0 . 1 } x ^ { 4 } \cos { \tilde { \xi } ( x ) } d x \bigg | \le \frac { 1 } { 2 4 } \int _ { 0 } ^ { 0 . 1 } x ^ { 4 } | \cos { \tilde { \xi } ( x ) } | d x } \\ & { } & { \displaystyle \qquad \le \frac { 1 } { 2 4 } \int _ { 0 } ^ { 0 . 1 } x ^ { 4 } d x = 8 . { \overline { { 3 } } } \times 1 0 ^ { - 8 } . } \end{array}
$$

Since the true value of this integral is

$$
\int _ { 0 } ^ { 0 . 1 } \cos { x } d x = \sin { x } \bigg ] _ { 0 } ^ { 0 . 1 } = \sin { 0 . 1 } \approx 0 . 0 9 9 8 3 3 4 1 7 ,
$$

the actual error for this approximation is $8 . 3 3 2 \times 1 0 ^ { - 8 }$ ,which is within the error bound.

We could also use a CAS in Example 3. Using Maple, we define $f$ by

$> \mathbf { f } : = \mathsf { c o s } \left( \mathbf { x } \right)$ ；

Maple allows us to place multiple statements on a line and to use a colon to suppress Maple responses. For example, we obtain the third Taylor polynomial with

$$
> { \bf s } 3 : = \sf t a y l o r ( \bf f _ { \alpha } , x = 0 , \bf 4 ) : \mathrm { ~ } p 3 : = c o n v e r t { \bf ( s 3 , p o l y n o m ) : }
$$

The first part computes the Taylor series with four terms (degree 3） and remainder ex-panded about $x _ { 0 } = 0$ . The second part converts the series s3 to the polynomial $p 3$ by dropping the remainder. To obtain 11 decimal digits of display we enter

and evaluate f(0.01), $P _ { 3 } ( 0 . 0 1 )$ ,and $| f ( 0 . 0 1 ) - P _ { 3 } ( 0 . 0 1 ) |$ with

$$
\begin{array} { r l } & { \mathrm { > y 1 : = e v a l f \left( s u b s \left( x = 0 . 0 1 , f \right) \right) ; } } \\ & { \mathrm { > y 2 : = e v a l f \left( s u b s \left( x = 0 . 0 1 , p 3 \right) \right) ; } } \\ & { \mathrm { > e r r : = a b s \left( y 1 - y 2 \right) ; } } \end{array}
$$

This produces $y _ { 1 } = f ( 0 . 0 1 ) = 0 . 9 9 9 9 5 0 0 0 0 4 2 .$ $y _ { 2 } = P _ { 3 } ( 0 . 0 1 ) = 0 . 9 9 9 9 5 0 0 0 0 0 0$ and $| f ( 0 . 0 1 ) - P _ { 3 } ( 0 . 0 1 ) | = . 4 2 \times 1 0 ^ { - 9 }$

To obtain a graph similar to Figure 1.12, enter

$$
> \mathtt { p l o t } ( \{ \ \mathtt { f } \ , \mathtt { p } \mathtt { 3 } \ \} \mathtt { j } , \mathtt { x } ^ { \mathtt { s } - \mathtt { P i } } \cdot \mathtt { P i } ) \ ;
$$

The commands for the integrals are

$$
\begin{array} { r l } & { \mathrm { > q 1 : = i n t \left( f _ \varepsilon , x = 0 . ~ . 0 . 1 \right) ; } } \\ & { \mathrm { > q 2 : = i n t \left( p 3 , x = 0 . ~ . 0 . 1 \right) ; } } \\ & { \mathrm { > e r r : = a b s \left( q 1 - q 2 \right) ; } } \end{array}
$$

which give the values

$$
q _ { 1 } = \int _ { 0 } ^ { 0 . 1 } f ( x ) d x = 0 . 0 9 9 8 3 3 4 1 6 6 4 7 \quad { \mathrm { a n d } } \quad q _ { 2 } = \int _ { 0 } ^ { 0 . 1 } P _ { 3 } ( x ) d x = 0 . 0 9 9 8 3 3 3 3
$$

with error $0 . 8 3 3 1 4 \times 1 0 ^ { - 7 }$ .

Parts (a) and (b) of the example show how two techniques can produce the same approximation but have differing accuracy assurances. Remember that determining approximations is only part of our objective. An equally important part is to determine at least a bound for the accuracy of the approximation.

# ExERcIse Set 1.1

1.Show that the following equations have at least one solution in the given intervals.

a. $x \cos x - 2 x ^ { 2 } + 3 x - 1 = 0 ,$ ，[0.2,0.3] and [1.2,1.3] b. $( x - 2 ) ^ { 2 } - \ln { x } = 0 ,$ [1,2] and $[ e , 4 ]$ c. $2 x \cos ( 2 x ) - ( x - 2 ) ^ { 2 } = 0 ,$ [2,3] and [3,4] d. $x \mathrm { ~ - ~ } ( \ln x ) ^ { x } = 0 , \quad [ 4 , 5 ]$

2.Find intervals containing solutions to the following equations.

$$
\begin{array} { l } { x - 3 ^ { - x } = 0 } \\ { 4 x ^ { 2 } - e ^ { x } = 0 } \\ { x ^ { 3 } - 2 x ^ { 2 } - 4 x + 3 = 0 } \\ { x ^ { 3 } + 4 . 0 0 1 x ^ { 2 } + 4 . 0 0 2 x + 1 . 1 0 1 = 0 } \end{array}
$$

3.Show that $f ^ { \prime } ( x )$ is O at least once in the given intervals.

$$
\begin{array} { l } { f ( x ) = 1 - e ^ { x } + ( e - 1 ) \sin ( ( \pi / 2 ) x ) , \quad [ } \\ { f ( x ) = ( x - 1 ) \tan x + x \sin \pi x , \quad [ 0 , 1 ] } \\ { f ( x ) = x \sin \pi x - ( x - 2 ) \ln x , \quad [ 1 , 2 ] } \\ { f ( x ) = ( x - 2 ) \sin x \ln ( x + 2 ) , \quad [ - 1 , 3 ] } \end{array}
$$

4.Find $\operatorname* { m a x } _ { a \leq x \leq b } | f ( x ) |$ for the following functions and intervals.

$$
\begin{array} { l } { f ( x ) = ( 2 - e ^ { x } + 2 x ) / 3 , \quad [ 0 , 1 ] } \\ { f ( x ) = ( 4 x - 3 ) / ( x ^ { 2 } - 2 x ) , \quad [ 0 . 5 , 1 ] } \\ { f ( x ) = 2 x \cos ( 2 x ) - ( x - 2 ) ^ { 2 } , \quad [ 2 , 4 ] } \\ { f ( x ) = 1 + e ^ { - \cos ( x - 1 ) } , \quad [ 1 , 2 ] } \end{array}
$$

5. Use the Intermediate Value Theorem and Rolle's Theorem to show that the graph of $f ( x ) =$ $x ^ { 3 } + 2 x + k$ crosses the $\pmb { x }$ -axis exactly once, regardless of the value of the constant $k$

6. Suppose $f \in C [ a , b ]$ and $f ^ { \prime } ( x )$ exists on $( a , b )$ . Show that if $f ^ { \prime } ( x ) \neq 0$ for all $x$ in $( a , b )$ ， then there can exist at most one number $p$ in $[ a , b ]$ with $f ( p ) = 0$

7.Let $f ( x ) = x ^ { 3 }$

a. Find the second Taylor polynomial $P _ { 2 } ( x )$ about $x _ { 0 } = 0$   
$\mathbf { { b } } .$ Find ${ \pmb R } _ { 2 } ( { \bf 0 . 5 } )$ and the actual error in using ${ \cal P } _ { 2 } ( 0 . 5 )$ to approximate $f ( 0 . 5 )$ $\pmb { \mathfrak { c } } _ { \bullet }$ Repeat part (a) using $x _ { 0 } = 1$   
d. Repeat part (b) using the polynomial from part (c).

8. Find the third Taylorpolynomial $P _ { 3 } ( x )$ for the function $f ( x ) = { \sqrt { x + 1 } }$ about $x _ { 0 } = 0$ .Ap proximate $\sqrt { 0 . 5 } \mathrm { ~ , ~ } \sqrt { 0 . 7 5 } \mathrm { , ~ } \sqrt { 1 . 2 5 }$ ,and $\sqrt { 1 . 5 }$ using $P _ { 3 } ( x )$ ,and find the actual errors.

9.Find the second Taylor polynomial $P _ { 2 } ( x )$ for the function $f ( x ) = e ^ { x } \cos x$ about $x _ { 0 } = 0$

a. Use $P _ { 2 } ( 0 . 5 )$ to approximate $f ( 0 . 5 )$ . Find an upper bound for error $| f ( 0 . 5 ) - P _ { 2 } ( 0 . 5 )$ using the error formula, and compare it to the actual error.   
b. Find a bound for the error $| f ( { \pmb x } ) - { \pmb P } _ { 2 } ( { \pmb x } ) |$ in using $P _ { 2 } ( x )$ to approximate $f ( x )$ on the interval [0, 1].   
c. Approximate $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x$ using $\begin{array} { r } { \int _ { 0 } ^ { 1 } P _ { 2 } ( x ) d x } \end{array}$   
d. Find an upper bound for the error in (c) using $\textstyle \int _ { 0 } ^ { 1 } | R _ { 2 } ( x ) \ d x |$ , and compare the bound to the actual error.

10.Repeat Exercise 9 using $x _ { 0 } = \pi / 6$

11:Find the third Taylor polynomial $P _ { 3 } ( x )$ for the function $f ( x ) = ( x - 1 ) \ln$ $\pmb { x }$ about $x _ { 0 } = 1$ ：

a. Use $P _ { 3 } ( 0 . 5 )$ to approximate $f ( 0 . 5 )$ .Find an upper bound for error $| f ( 0 . 5 ) - P _ { 3 } ( 0 . 5 )$ using the error formula, and compare it to the actual error.   
b. Find a bound for the error $| f ( { \pmb x } ) - P _ { 3 } ( { \pmb x } ) |$ in using $P _ { 3 } ( x )$ to approximate $f ( x )$ on the interval [0.5, 1.5].   
c. Approximate $\int _ { 0 . 5 } ^ { 1 . 5 } f ( x ) d x$ using $\begin{array} { r } { \int _ { 0 . 5 } ^ { 1 . 5 } P _ { 3 } ( x ) d x } \end{array}$   
d. Find an upper bound for the error in (c) using $\begin{array} { r } { \int _ { 0 . 5 } ^ { 1 . 5 } \left| R _ { 3 } ( x ) d x \right| } \end{array}$ , and compare the bound to the actual error.

12.Let $f ( x ) = 2 x \cos ( 2 x ) - ( x - 2 ) ^ { 2 }$ and $x _ { 0 } = 0$

a. Find the third Taylor polynomial $P _ { 3 } ( x )$ , and use it to approximate $f ( 0 . 4 )$   
$\mathbf { b } .$ Use the error formula in Taylor's Theorem to find an upper bound for the error $\mid f ( 0 . 4 ) $ $P _ { 3 } ( 0 . 4 ) |$ . Compute the actual error.   
$\pmb { \mathbb { c } } _ { \pmb { \cdot } }$ Find the fourth Taylor polynomial $P _ { 4 } ( x )$ , and use it to approximate $\pmb { f } ( \mathbf { 0 . 4 } )$   
d. Use the error formula in Taylor's Theorem to find an upper bound for the error $\mid f ( 0 . 4 ) -$ $P _ { 4 } ( 0 . 4 ) !$ . Compute the actual error.

13.Find the fourth Taylor polynomial $P _ { 4 } ( x )$ for the function $f ( x ) = x e ^ { x ^ { 2 } }$ about $x _ { 0 } = 0 .$

a. Find an upper bound for $| f ( x ) - P _ { 4 } ( x ) |$ ,for $0 \leq x \leq 0 . 4$ $\big .$ Approximate $\begin{array} { r } { \int _ { 0 } ^ { 0 . 4 } f ( x ) d x } \end{array}$ using $\begin{array} { r } { \int _ { 0 } ^ { 0 . 4 } P _ { 4 } ( x ) d x } \end{array}$ c. Find an upper bound fortheeror in $( \mathbf { b } )$ using $\int _ { 0 } ^ { 0 . 4 } p _ { 4 } ( x ) d x$ d. Approximate $f ^ { \prime } ( 0 . 2 )$ using $P _ { 4 } ^ { \prime } ( 0 . 2 )$ ,and find the error.

14.Use the error term of a Taylor polynomial to estimate the error involved in using sin $x \approx x$ to approximate sin $1 ^ { \circ }$

15.Use a Taylor polynomial about $\pi / 4$ to approximate cos $4 2 ^ { \circ }$ to an accuracy of $1 0 ^ { - 6 }$

16.Let $f ( x ) = e ^ { x / 2 } \sin ( x / 3 )$ . Use Maple to determine the following. a.The third Maclaurin polynomial $P _ { 3 } ( x )$ · b. $f ^ { ( 4 ) } ( x )$ and a bound for the error $| f ( { \pmb x } ) - P _ { 3 } ( { \pmb x } ) |$ on [0, 1].

17.Let $f ( x ) = \ln ( x ^ { 2 } + 2 )$ . Use Maple to determine the following.

a. The Taylor polynomial ${ P } _ { 3 } ( x )$ for $f$ expanded about $x _ { 0 } = 1$ $\mathbf { b } .$ The maximum error $| f ( { \pmb x } ) - P _ { 3 } ( { \pmb x } ) |$ ,for $0 \leq x \leq 1$ ， c. The Maclaurin polynomial $\tilde { P } _ { 3 } ( x )$ for $f$ d. The maximum error $\vert f ( x ) - \tilde { P } _ { 3 } ( x ) \vert$ ,for $0 \leq x \leq 1$ ${ \pmb { \ell } } _ { \bullet }$ Does $P _ { 3 } ( 0 )$ approximate $f ( 0 )$ better than $\tilde { P } _ { 3 } ( 1 )$ approximates $f ( 1 ) \smash { ? }$

18.Let $f ( x ) = ( 1 - x ) ^ { - 1 }$ and $x _ { 0 } = 0$ .Find thenth Taylor polynomial $P _ { n } ( x )$ for $f ( x )$ about $x _ { 0 }$ Find a value of $\pmb { n }$ necessary for $P _ { n } ( x )$ to approximate $f ( x )$ to within $1 0 ^ { - 6 }$ on [0, 0.5].

19.Let $f ( x ) = e ^ { x }$ and $x _ { 0 } = 0$ .Find the nth Taylor polynomial $P _ { n } ( x )$ for $f ( x )$ about $x _ { 0 }$ . Find a value of $\pmb { n }$ necessary for $\smash { P _ { n } ( x ) }$ to approximate $f ( x )$ to within $1 0 ^ { - 6 }$ on [0, 0.5].

20．Find the nth Maclaurin polynomial $\pmb { P _ { n } } ( \pmb { x } )$ for $f ( x ) = \arctan x$

21．The polynomial $\begin{array} { r } { P _ { 2 } ( x ) = 1 - \frac { 1 } { 2 } x ^ { 2 } } \end{array}$ is to be used to approximate $f ( x ) = \cos x$ in $[ - \frac { 1 } { 2 } , \frac { 1 } { 2 } ]$ . Find a bound for the maximum error.

22. The nth Taylor polynomial for a function $f$ at $\pmb { x _ { 0 } }$ is sometimes referred to as the polynomial of degree at most n that “best" approximates $f$ near $\yen 0$ · a. Explain why this description is accurate. $\mathbf { b } _ { \bullet }$ Find the quadratic polynomial that best approximates a function $f$ near $x _ { 0 } = 1$ if the tangent line at $x _ { 0 } = 1$ has equation $y = 4 x - 1$ ,and if $f ^ { \prime \prime } ( 1 ) = 6$

23.A Maclaurin polynomial for $e ^ { x }$ is used to give the approximation 2.5 to $^ e$ . The error bound in this approximation is established to be $\begin{array} { r } { E = \frac 1 6 } \end{array}$ .Find a bound for the error in $\pmb { \cal E }$ 、

24. The error function defined by

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } \int _ { 0 } ^ { x } e ^ { - t ^ { 2 } } d t
$$

gives the probability that any one of a series of trials willie within $x$ units of the mean, assuming that the trials have a normal distribution with mean O and standard deviation $\sqrt { 2 } / 2$ . This integral cannot be evaluated in terms of elementary functions, so an approximating technique must be used.

a. Integrate the Maclaurin series for $e ^ { - x ^ { 2 } }$ to show that

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } \sum _ { k = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { k } x ^ { 2 k + 1 } } { ( 2 k + 1 ) k ! } } .
$$

b.The error function can also be expressed in the form

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } e ^ { - x ^ { 2 } } \sum _ { k = 0 } ^ { \infty } { \frac { 2 ^ { k } x ^ { 2 k + 1 } } { 1 \cdot 3 \cdot 5 \cdot \cdots ( 2 k + 1 ) } } .
$$

Verify that the two series agree for $k = 1 , 2 , 3$ ,and 4. [Hint: Use the Maclaurin series for $e ^ { - x ^ { 2 } }$

c. Use the series in part (a) to approximate $\tt e r f ( 1 )$ to within $1 0 ^ { - 7 }$ d.Use the same number of terms as in part (c)to approximate erf(1) with the series in part (b).

e.Explain why difficulties occur using the series in part (b) to approximate $\mathsf { e r f } ( x )$

25.A function $f : [ a , b ]  \mathbb { R }$ is said to satisfy a Lipschitz condition with Lipschitz constant $L$ on $[ a , b ]$ if, for every $x , y \in [ a , b ]$ ， we have $| f ( x ) - f ( y ) | \leq L | x - y |$ a. Show that if $f$ satisfies a Lipschitz condition with Lipschitz constant $L$ on an interval $\{ a , b \}$ ,then $f \in C [ a , b ]$ $\mathbf { b } _ { \bullet }$ Show that if $f$ has a derivative that is bounded on $[ a , b ]$ by $L$ ,then $f$ satisfies a Lipschitz condition with Lipschitz constant $L$ on $[ a , b ]$ c. Give an example of a function that is continuous on a closed interval but does not satisfy a Lipschitz condition on the interval.

26.Suppose $f \in C [ a , b ]$ ,that $x _ { 1 }$ and $\pmb { x _ { 2 } }$ are in $[ a , b ]$ , and that $c _ { 1 }$ and $c _ { 2 }$ are positive constants. Show that a number ${ \pmb \xi }$ exists between $x _ { 1 }$ and $\pmb { x _ { 2 } }$ with

$$
f ( \xi ) = \frac { c _ { 1 } f ( x _ { 1 } ) + c _ { 2 } f ( x _ { 2 } ) } { c _ { 1 } + c _ { 2 } } .
$$

27.Let $f \in C [ a , b ]$ , and let $p$ be in the open interval $( a , b )$ ·

a. Suppose $f ( p ) \neq 0$ . Show that a ${ \pmb \delta } > { \bf 0 }$ exists with $f ( x ) \neq 0$ ,for all $\pmb { x }$ in $[ p - \delta , p + \delta ]$ ， with $[ p - \delta , p + \delta ]$ a subset of $[ a , b ]$   
b. Suppose $f ( p ) = 0$ and $k > 0$ is given. Show that a $\delta > 0$ exists with $| f ( x ) | \leq k$ , for all $\pmb { x }$ in $[ p - \delta , p + \delta ]$ ,with $[ p - \delta , p + \delta ]$ a subset of $[ a , b ]$

# 1.2 Roundoff Errors and Computer Arithmetic

The arithmetic performed by a calculator or computer is different from the arithmetic in our algebra and calculus courses. From your past experience,you might expect that we always have as true statements such things as $2 + 2 = 4$ ， $4 \cdot 4 = 1 6$ ,and $( { \sqrt { 3 } } ) ^ { 2 } = 3$ .In standard computational arithmetic we will have the first two but not always the third. To understand why this is true we must explore the world of finite-digit arithmetic.

In our traditional mathematical world we permit numbers with an infinite number of digits.The arithmetic we use in this world defines $\sqrt { 3 }$ as that unique positive number that when multiplied by itself produces the integer 3. In the computational world, however, each representable number has only a fixed, finite number of digits. This means,for example, that only rational numbers-and not even all of these-can be represented exactly. Since $\sqrt { 3 }$ is not rational, it is given an approximate representation, one whose square will not be precisely 3,although it will likely be sufficiently close to 3 to be acceptable in most situations.In most cases, then, this machine arithmetic is satisfactory and passes without notice or concern,but at times problems arise because of this discrepancy.

Roundoff error is produced when a calculator or computer is used to perform realnumber calculations. It occurs because the arithmetic performed in a machine involves numbers with only a finite number of digits,with the result that calculations are performed with only approximate representations of the actual numbers. In a typical computer, only a relatively small subset of the real number system is used for the representation of all the real numbers. This subset contains only rational numbers, both positive and negative,and stores the fractional part, together with an exponential part.

In I985,the IEEE (Institute for Electrical and Electronic Engineers)published a report called Binary Floating Point Arithmetic Standard 754-1985.Formats were specified for single,double,and extended precisions,and these standards are generally followed by all microcomputer manufacturers using floating-point hardware.For example, the numerical coprocessor for PCs implements a 64-bit (binary digit) representation for a real number, called a long real. The first bit is a sign indicator, denoted $\pmb { \mathscr { s } }$ . This is followed by an 11-bit exponent, $c$ , called the characteristic, and a 52-bit binary fraction, $f$ , called the mantissa. The base for the exponent is 2.

Since 52 binary digits correspond to between 16 and 17 decimal digits, we can assume that a number represented in this system has at least 16 decimal digits of precision. The exponent of 11 binary digits gives a range of O to $2 ^ { 1 1 } - 1 = 2 0 4 7$ . However, using only positive integers for the exponent would not permit an adequate representation of numbers with small magnitude. To ensure that numbers with small magnitude are equally representable,1023 is subtracted from the characteristic, so the range of the exponent is actually from －1023 to 1024.

To save storage and provide a unique representation for each floating-point number, a normalization is imposed. Using this system gives a floating-point number of the form

$$
( - 1 ) ^ { s } 2 ^ { c - 1 0 2 3 } ( 1 + f ) .
$$

Consider for example, the machine number

The leftmost bit is zero,which indicates that the number is positive. The next 11 bits, 1000000oO11, giving the characteristic,are equivalent to the decimal number

$$
c = 1 \cdot 2 ^ { 1 0 } + 0 \cdot 2 ^ { 9 } + \cdot \cdot \cdot + 0 \cdot 2 ^ { 2 } + 1 \cdot 2 ^ { 1 } + 1 \cdot 2 ^ { 0 } = 1 0 2 4 + 2 + 1 = 1 0 2 7 .
$$

The exponential part of the number is,therefore, $2 ^ { 1 0 2 7 - 1 0 2 3 } = 2 ^ { 4 }$ . The final 52 bits specify that the mantissa is

$$
f = 1 \cdot \left( { \frac { 1 } { 2 } } \right) ^ { 1 } + 1 \cdot \left( { \frac { 1 } { 2 } } \right) ^ { 3 } + 1 \cdot \left( { \frac { 1 } { 2 } } \right) ^ { 4 } + 1 \cdot \left( { \frac { 1 } { 2 } } \right) ^ { 5 } + 1 \cdot \left( { \frac { 1 } { 2 } } \right) ^ { 8 } + 1 \cdot \left( { \frac { 1 } { 2 } } \right) ^ { 1 2 } .
$$

As a consequence,this machine number precisely represents the decimal number

$$
\begin{array} { c } { { ( - 1 ) ^ { s } 2 ^ { c - 1 0 2 3 } ( 1 + f ) = ( - 1 ) ^ { 0 } \cdot 2 ^ { 1 0 2 7 - 1 0 2 3 } \left( 1 + \displaystyle { \left( \frac { 1 } { 2 } + \frac { 1 } { 8 } + \frac { 1 } { 1 6 } + \frac { 1 } { 3 2 } + \frac { 1 } { 2 5 6 } + \frac { 1 } { 4 0 9 6 } \right) } \right) } } \\ { { = 2 7 . 5 6 6 4 0 6 2 5 , } } \end{array}
$$

However, the next smallest machine number is

0 10000000011 1011100100001111111111111111111111111111111111111111,

and the next largest machine number is

01000000001110111001000100000000000000000000000000000000000001.

This means that our original machine number represents not only 27.56640625,but also half of the real numbers that are between 27.56640625 and its two nearest machine-number neighbors.To be precise,it represents any real number in the interval

[27.5664062499999982236431605997495353221893310546875,

27.5664062500000017763568394002504646778106689453125).

The smallest normalized positive number that can be represented has all Os except for the rightmost bit of 1 and is equivalent to

$$
2 ^ { - 1 0 2 3 } \cdot ( 1 + 2 ^ { - 5 2 } ) \approx 1 0 ^ { - 3 0 8 } ,
$$

and the largest has a leading O followed by all 1s and is equivalent to

$$
2 ^ { 1 0 2 4 } \cdot ( 2 - 2 ^ { - 5 2 } ) \approx 1 0 ^ { 3 0 8 } .
$$

Numbers occurring in calculations that have a magnitude less than $2 ^ { - 1 0 2 3 } \cdot ( 1 + 2 ^ { - 5 2 } )$ result in underflow and are generally set to zero. Numbers greater than $2 ^ { 1 0 2 4 }$ · $( 2 - 2 ^ { - 5 2 } )$ result in overflow and typically cause the computations to halt.

The use of binary digits tends to conceal the computational diffculties that occur when a finite collection of machine numbers is used to represent all the real numbers. To examine these problems,we now assume,for simplicity,that machine numbers are represented in the normalized decimal floating-point form

$$
\pm 0 . d _ { 1 } d _ { 2 } \ldots d _ { k } \times 1 0 ^ { n } , \quad 1 \leq d _ { 1 } \leq 9 , \quad \mathrm { a n d } \quad 0 \leq d _ { i } \leq 9 ,
$$

for each $i = 2 , \ldots , k$ . Numbers of this form are called $k$ -digit decimal machine numbers.

Any positive real number within the numerical range of the machine can be normalized to the form

$$
y = 0 . d _ { 1 } d _ { 2 } \ldots d _ { k } d _ { k + 1 } d _ { k + 2 } \ldots \times 1 0 ^ { n } .
$$

The foating-point form of $y$ , denoted $f l ( y )$ , is obtained by terminating the mantissa of y at $k$ decimal digits. There are two ways of performing this termination. One method, called chopping,is to simply chop off the digits $d _ { k + 1 } d _ { k + 2 } \ldots$ . to obtain

$$
f l ( y ) = 0 . d _ { 1 } d _ { 2 } \ldots d _ { k } \times 1 0 ^ { n } .
$$

The other method, called rounding, adds $5 \times 1 0 ^ { n - ( k + 1 ) }$ to $y$ and then chops the result to obtain a number of the form

$$
f l ( y ) = 0 . \delta _ { 1 } \delta _ { 2 } \dots \delta _ { k } \times 1 0 ^ { n } .
$$

So, when rounding, if $d _ { k + 1 } \geq 5$ , we add 1 to $d _ { k }$ to obtain $f l ( y )$ ; that is, we round up. When $d _ { k + 1 } < 5$ ,we merely chop off all but the first $k$ digits; so we round down. If we round down, then $\delta _ { i } = d _ { i }$ ,for each $i = 1 , 2 , \ldots , k$ .However, if we round up,the digits might change.

The number $\pi$ has an infinite decimal expansion of the form π = 3.14159265... Written in normalized decimal form, we have

$$
\pi = 0 . 3 1 4 1 5 9 2 6 5 \ldots \times 1 0 ^ { 1 } .
$$

The floating-point form of $\pi$ using five-digit chopping is

$$
f l ( \pi ) = 0 . 3 1 4 1 5 \times 1 0 ^ { 1 } = 3 . 1 4 1 5 .
$$

Sincethesixthdigitoftedecialexpasioof $\pi$ is a 9, thefoating-pont formof $\pi$ using five-digit rounding is

$$
f l ( \pi ) = ( 0 . 3 1 4 1 5 + 0 . 0 0 0 0 1 ) \times 1 0 ^ { 1 } = 3 . 1 4 1 6 .
$$

The error that results from replacing a number with its foating-point form is called roundoff error (regardless of whether the rounding or chopping method is used). The following definition describes two methods for measuring approximation errors.

# Definition 1.15

If $p ^ { * }$ is an approximation to $p$ , the absolute error is $| p - p ^ { * } |$ , and the relative error is $\frac { | p - p ^ { * } | } { | p | }$ , provided that $p \neq 0$

Consider the absolute and relative errors in representing $p$ by $p ^ { * }$ in the following example.

a.If $p = 0 . 3 0 0 0 \times 1 0 ^ { 1 }$ and $p ^ { * } = 0 . 3 1 0 0 \times 1 0 ^ { 1 }$ ,the absolute error is O.1,and the relative error is $0 . 3 3 3 \overline { { 3 } } \times \bar { 1 0 } ^ { - 1 }$ ，

b.If $p = 0 . 3 0 0 0 \times 1 0 ^ { - 3 }$ and $p ^ { * } = 0 . 3 1 0 0 \times 1 0 ^ { - 3 }$ , the absolute error is $0 . 1 \times 1 0 ^ { - 4 }$ ， and the relative error is $0 . 3 3 3 \overline { { 3 } } \times 1 0 ^ { - 1 }$ ，   
c. f $p = 0 . 3 0 0 0 \times 1 0 ^ { 4 }$ and $p ^ { * } = 0 . 3 1 0 0 \times 1 0 ^ { 4 }$ , the absolute crror is $0 . 1 \times 1 0 ^ { 3 }$ , and the relative error is again $0 . 3 3 3 \overleftarrow { 3 } \times 1 0 ^ { - 1 }$

This example shows that the same relative error, $0 . 3 3 3 { \overline { { 3 } } } \times 1 0 ^ { - 1 }$ ， occurs for widely varying absolute errors. As a measure of accuracy, the absolute error can be misleading and the relative error more meaningful since the relative error takes into consideration the size of the value.

The following definition uses relative error to give a measure of significant digits of accuracy for an approximation.

# Definition 1.16

The number $p ^ { \ast }$ is said to approximate $p$ to $t$ significant digits (or figures) if $t$ is the largest nonnegative integer for which

$$
\frac { | p - p ^ { * } | } { | p | } < 5 \times 1 0 ^ { - t } .
$$

Table 1.1 illustrates the continuous nature of significant digits by listing,for the various values of $p$ , the least upper bound of $| p - p ^ { * } |$ , denoted max $| p - p ^ { * } |$ , when $p ^ { \ast }$ agrees with $p$ to four significant digits.

Table 1.1

<table><tr><td>p</td><td>0.1 0.5</td><td>100 1000</td><td>5000</td><td>9990 10000</td></tr><tr><td>max |p - p*|</td><td>0.00005 0.00025</td><td>0.05 0.5 2.5</td></tr><tr><td>4.995</td><td></td></tr><tr><td></td></tr><tr><td>5.</td></tr><tr><td></td></tr></table>

Returning to the machine representation of numbers, we see that the floating-point representation $f l ( y )$ for the number $y$ has the relative error

$$
\left| { \frac { y - f l ( y ) } { y } } \right| .
$$

if $k$ decimal digits and chopping are used for the machine representation of

$$
y = 0 . d _ { 1 } d _ { 2 } \ldots d _ { k } d _ { k + 1 } \ldots \times 1 0 ^ { n } ,
$$

then

$$
\begin{array} { r l r } {  {  \frac { y - f l ( y ) } { y }  =  \frac { 0 . d _ { 1 } d _ { 2 } \ldots d _ { k } d _ { k + 1 } \ldots \times 1 0 ^ { n } - 0 . d _ { 1 } d _ { 2 } \ldots d _ { k } \times 1 0 ^ { n } } { 0 . d _ { 1 } d _ { 2 } \ldots \times 1 0 ^ { n } }  } } \\ & { } & { =  \frac { 0 . d _ { k + 1 } d _ { k + 2 } \ldots \times 1 0 ^ { n - k } } { 0 . d _ { 1 } d _ { 2 } \ldots \times 1 0 ^ { n } }  =  \frac { 0 . d _ { k + 1 } d _ { k + 2 } \ldots } { 0 . d _ { 1 } d _ { 2 } \ldots }  \times 1 0 ^ { - k } . } \end{array}
$$

Since $d _ { 1 } \neq 0$ ,the minimal value of the denominator is O.1. The numerator is bounded above by 1. As a consequence,

$$
\left| { \frac { y - f l ( y ) } { y } } \right| \leq { \frac { 1 } { 0 . 1 } } \times 1 0 ^ { - k } = 1 0 ^ { - k + 1 } .
$$

In a similar manner, a bound for the relative error when using $k$ -digit rounding arithmetic is $0 . 5 \times 1 0 ^ { - k + 1 }$ . (See Exercise 24.)

Note that the bounds for the relative error using $k$ -digit arithmetic are independent of the number being represented. This result is due to the manner in which the machine numbers are distributed along the real line.Because of the exponential form of the characteristic,the same number of decimal machine numbers is used to represent each of the intervals [O.1,1],[1,10],and [10,100].In fact,within the limits of the machine,the number of decimal machine numbers in $[ 1 0 ^ { n } , 1 0 ^ { n + 1 } ]$ is constant for all integers $n$

In addition to inaccurate representation of numbers,the arithmetic performed in a com-puter is not exact.The arithmetic involves manipulating binary digits by various shifting, or logical, operations. Since the actual mechanics of these operations are not pertinent to this presentation, we shall devise our own approximation to computer arithmetic. Although our arithmetic will not give the exact picture, it suffices to explain the problems that occur. (For an explanation of the manipulations actually involved, the reader is urged to consult more technically oriented computer science texts,such as [Ma], Computer System Architecture.)

Assume that the floating-point representations $f l ( x )$ and $f l ( y )$ are given for the real numbers $x$ and $y$ and that the symbols $\oplus , \ominus , \otimes , \odot$ represent machine addition, subtraction,multiplication,and division operations,respectively. We will assume a finite-digit arithmetic given by

$$
\begin{array} { l l } { { x \oplus y = f l ( f l ( x ) + f l ( y ) ) , } } & { { x \otimes y = f l ( f l ( x ) \times f l ( y ) ) , } } \\ { { } } & { { } } \\ { { x \ominus y = f l ( f l ( x ) - f l ( y ) ) , } } & { { x \ominus y = f l ( f l ( x ) \div f l ( y ) ) . } } \end{array}
$$

This arithmetic corresponds to performing exact arithmetic on the floating-point repre-sentations of $x$ and $y$ and then converting the exact result to its finite-digit floating-point representation.

Rounding arithmetic is easily implemented in a CAS. The Maple command

>Digits: $= t$ ；

causes all arithmetic to be rounded to $t$ digits. For example, $f l ( f l ( x ) + f l ( y ) )$ is performed using $t$ -digit rounding arithmetic by

>evalf(evalf(x)+evalf(y));

Implementing $t$ -digit chopping arithmetic is more difcult and requires asequence of steps or a procedure. Exercise 27 explores this problem.

# EXAMPLE 3

Suppose that $\begin{array} { r } { x = { \frac { 5 } { 7 } } , y = \frac { 1 } { 3 } } \end{array}$ ,and that five-digit chopping is used for arithmetic calculations involving $x$ and $y$ . Table 1.2 lists the values of these computer-type operations on $f l ( x ) =$ $0 . 7 1 4 2 8 \times 1 0 ^ { 0 }$ and $f l ( y ) = 0 . 3 3 3 3 3 \times 1 0 ^ { 0 }$

# Table 1.2

<table><tr><td>Operation</td><td>Result</td><td>Actual value</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>xy</td><td>0.10476×10l</td><td>22/21</td><td>0.190 × 10-4</td><td>0.182 × 10-4</td></tr><tr><td>xΘy</td><td>0.38095×100</td><td>8/21</td><td>0.238 × 10-5</td><td>0.625× 10-5</td></tr><tr><td>x8y</td><td>0.23809 ×100</td><td>5/21</td><td>0.524× 10-5</td><td>0.220 × 10-4</td></tr><tr><td>yex</td><td>0.21428 × 10l</td><td>15/7</td><td>0.571 × 10-4</td><td>0.267 × 10-4</td></tr></table>

Since the maximum relative error for the operations in Example 3 is $0 . 2 6 7 \times 1 0 ^ { - 4 }$ ， the arithmetic produces satisfactory five-digit results. Suppose, however, that we also have $u = 0 . 7 1 4 2 5 1$ ， $\upsilon = 9 8 7 6 5 . 9$ ,and $w = 0 . 1 1 1 1 1 1 \times 1 0 ^ { - 4 }$ , so that $f l ( u ) = 0 . 7 1 4 2 5 \times 1 0 ^ { 0 }$ ， $f l ( v ) = 0 . 9 8 7 6 5 \times 1 0 ^ { 5 }$ ,and $f l ( w ) = 0 . 1 1 1 1 1 \times 1 0 ^ { - 4 }$ . (These numbers were chosen to illustrate some problems that can arise with finite-digit arithmetic.)

In Table 1.3, $x \ominus u$ results in a small absolute error but a large relative error. The subsequent division by the small number $w$ or multiplication by the large number $v$ magnifies the absolute error without modifying the relative error. The addition of the large and small numbers $u$ and $v$ produces large absolute error but not large relative error.

# Table 1.3

<table><tr><td>Operation</td><td>Result</td><td>Actual value</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>xΘu</td><td>0.30000 ×10-4</td><td>0.34714 × 10-4</td><td>0.471 × 10-5</td><td>0.136</td></tr><tr><td>(x Θu）w</td><td>0.29629 ×10&#x27;</td><td>0.34285×101</td><td>0.465</td><td>0.136</td></tr><tr><td>(xΘu）u</td><td>0.29629×101</td><td>0.34285×10l</td><td>0.465</td><td>0.136</td></tr><tr><td>uu</td><td>0.98765 × 105</td><td>0.98766 × 105</td><td>0.161×101</td><td>0.163×10-4</td></tr></table>

One of the most common error-producing calculations involves the cancellation of significant digits due to the subtraction of nearly equal numbers. Suppose two nearly equal numbers $x$ and $y$ ,with $x > y$ ,have the $k$ -digit representations

$$
f l ( x ) = 0 . d _ { 1 } d _ { 2 } \ldots d _ { p } \alpha _ { p + 1 } \alpha _ { p + 2 } \ldots \alpha _ { k } \times 1 0 ^ { n } ,
$$

and

$$
f l ( y ) = 0 . d _ { 1 } d _ { 2 } \ldots d _ { p } \beta _ { p + 1 } \beta _ { p + 2 } \ldots \beta _ { k } \times 1 0 ^ { n } .
$$

The floating-point form of $x - y$ is

$$
f l ( f l ( x ) - f l ( y ) ) = 0 . \sigma _ { p + 1 } \sigma _ { p + 2 } \ldots \sigma _ { k } \times 1 0 ^ { n - p } ,
$$

where

$$
0 . \sigma _ { p + 1 } \sigma _ { p + 2 } \ldots \sigma _ { k } = 0 . \alpha _ { p + 1 } \alpha _ { p + 2 } \ldots \alpha _ { k } - 0 . \beta _ { p + 1 } \beta _ { p + 2 } \ldots \beta _ { k } .
$$

The floating-point number used to represent $x - y$ has at most $k - p$ digits of significance. However, in most calculation devices, $x \mathrm { ~ - ~ } y$ will be assigned $k$ digits,with the last $p$ being either zero or randomly assigned. Any further calculations involving $x \ : - \ : y$ retain the problem of having only $k - p$ digits of significance, since a chain of calculations is no more accurate than its weakest portion.

If a finite-digit representation or calculation introduces an error, further enlargement of the error occurs when dividing by a number with small magnitude (or, equivalently, when multiplying by a number with large magnitude). Suppose, for example, that the number $z$ has the finite-digit approximation $z + \delta$ ， where the error $\delta$ is introduced by representation or by previous calculation. Suppose we now divide by $\varepsilon = 1 0 ^ { - n }$ ，where $n > 0$ .Then

$$
{ \frac { z } { \varepsilon } } \approx f l \left( { \frac { f l ( z ) } { f l ( \varepsilon ) } } \right) = ( z + \delta ) \times 1 0 ^ { n } .
$$

Thus,the absolute error in this approximation, $| \delta | \times 1 0 ^ { n }$ , is the original absolute error, $| \delta |$ ， multiplied by the factor $1 0 ^ { n }$ ·

# EXAMPLE 4

Let $p = 0 . 5 4 6 1 7$ and $q = 0 . 5 4 6 0 1$ . The exact value of $r = p - q$ is $r = 0 . 0 0 0 1 6$ Suppose the subtraction is performed using four-digit arithmetic. Rounding $p$ and $q$ to four digits gives $p ^ { * } = 0 . 5 4 6 2$ and $q ^ { * } = 0 . 5 4 6 0$ ,respectively, and $r ^ { * } = p ^ { * } - q ^ { * } = 0 . 0 0 0 2$ is the four-digit approximation to $r$ . Since

$$
\frac { | \boldsymbol { r } - \boldsymbol { r } ^ { * } | } { | \boldsymbol { r } | } = \frac { | 0 . 0 0 0 1 6 - 0 . 0 0 0 2 | } { | 0 . 0 0 0 1 6 | } = 0 . 2 5 ,
$$

the result has only one significant digit, whereas $p ^ { * }$ and $q ^ { * }$ were accurate to four and five significant digits, respectively.

If chopping is used to obtain the four digits,the four-digit approximations to $p , q$ , and $\boldsymbol { r }$ are $p ^ { * } = 0 . 5 4 6 1$ ， $q ^ { * } = 0 . 5 4 6 0$ , and $r ^ { * } = p ^ { * } - q ^ { * } = 0 . 0 0 0 1$ . This gives

$$
{ \frac { | \boldsymbol { r } - \boldsymbol { r } ^ { * } | } { | \boldsymbol { r } | } } = { \frac { | 0 . 0 0 0 1 6 - 0 . 0 0 0 1 | } { | 0 . 0 0 0 1 6 | } } = 0 . 3 7 5 ,
$$

which also results in only one significant digit of accuracy.

The loss of accuracy due to roundof error can often be avoided by a reformulation of the problem, as illustrated in the next example.

The quadratic formula states that the roots of $a x ^ { 2 } + b x + c = 0$ ,when $a \neq 0$ ,are

$$
x _ { 1 } = { \frac { - b + { \sqrt { b ^ { 2 } - 4 a c } } } { 2 a } } \quad { \mathrm { a n d } } \quad x _ { 2 } = { \frac { - b - { \sqrt { b ^ { 2 } - 4 a c } } } { 2 a } } .
$$

Using four-digit rounding arithmetic,consider this formula applied to the equation $x ^ { 2 } +$ $6 2 . 1 0 x + 1 = 0$ ，whose roots are approximately

$$
x _ { 1 } = - 0 . 0 1 6 1 0 7 2 3 \quad { \mathrm { a n d } } \quad x _ { 2 } = - 6 2 . 0 8 3 9 0 .
$$

In this equation, $b ^ { 2 }$ is much larger than $4 a c$ ，so the numerator in the calculation for $x _ { 1 }$ involves the subtraction of nearly equal numbers. Since

$$
{ \begin{array} { r l } & { { \sqrt { b ^ { 2 } - 4 a c } } = { \sqrt { ( 6 2 . 1 0 ) ^ { 2 } - ( 4 . 0 0 0 ) ( 1 . 0 0 0 ) ( 1 . 0 0 0 ) } } = { \sqrt { 3 8 5 6 . - 4 . 0 0 0 } } = { \sqrt { 3 8 5 2 . 0 0 } } } \\ & { \quad \quad = 6 2 . 0 6 , } \end{array} }
$$

we have

$$
f l ( x _ { 1 } ) = \frac { - 6 2 . 1 0 + 6 2 . 0 6 } { 2 . 0 0 0 } = \frac { - 0 . 0 4 0 0 0 } { 2 . 0 0 0 } = - 0 . 0 2 0 0 0 ,
$$

a poor approximation to $x _ { 1 } = - 0 . 0 1 6 1 1$ , with the large relative error

$$
\frac { | - 0 . 0 1 6 1 1 + 0 . 0 2 0 0 0 | } { | - 0 . 0 1 6 1 1 | } \approx 2 . 4 \times 1 0 ^ { - 1 } .
$$

On the other hand,the calculation for $x _ { 2 }$ involves the addition of the nearly equal numbers $- b$ and $- { \sqrt { b ^ { 2 } - 4 a c } }$ . This presents no problem since

$$
f l ( x _ { 2 } ) = \frac { - 6 2 . 1 0 - 6 2 . 0 6 } { 2 . 0 0 0 } = \frac { - 1 2 4 . 2 } { 2 . 0 0 0 } = - 6 2 . 1 0
$$

has the small relative error

$$
{ \frac { | - 6 2 . 0 8 + 6 2 . 1 0 | } { | - 6 2 . 0 8 | } } \approx 3 . 2 \times 1 0 ^ { - 4 } .
$$

To obtain a more accurate four-digit rounding approximation for $x _ { 1 }$ , we change the form of the quadratic formula by rationalizing the numerator:

$$
x _ { 1 } = \frac { - b + \sqrt { b ^ { 2 } - 4 a c } } { 2 a } \left( \frac { - b - \sqrt { b ^ { 2 } - 4 a c } } { - b - \sqrt { b ^ { 2 } - 4 a c } } \right) = \frac { b ^ { 2 } - ( b ^ { 2 } - 4 a c ) } { 2 a ( - b - \sqrt { b ^ { 2 } - 4 a c } ) } ,
$$

which simplifies to an alternate quadratic formula

$$
x _ { 1 } = \frac { - 2 c } { b + \sqrt { b ^ { 2 } - 4 a c } } .
$$

Using (1.2) gives

$$
f l ( x _ { \mathrm { i } } ) = \frac { - 2 . 0 0 0 } { 6 2 . 1 0 + 6 2 . 0 6 } = \frac { - 2 . 0 0 0 } { 1 2 4 . 2 } = - 0 . 0 1 6 1 0 ,
$$

which has the small relative error $6 . 2 \times 1 0 ^ { - 4 }$

The rationalization technique can also be applied to give the following alternative quadratic formula for $x _ { 2 }$ ：

$$
x _ { 2 } = \frac { - 2 c } { b - \sqrt { b ^ { 2 } - 4 a c } } .
$$

This is the form to use if $b$ is a negative number. In Example 5, however, the mistaken use of this formula for $x _ { 2 }$ would result in not only the subtraction of nearly equal numbers, but also the division by the small result of this subtraction. The inaccuracy that this combination produces,

$$
f l ( x _ { 2 } ) = { \frac { - 2 c } { b - { \sqrt { b ^ { 2 } - 4 a c } } } } = { \frac { - 2 . 0 0 0 } { 6 2 . 1 0 - 6 2 . 0 6 } } = { \frac { - 2 . 0 0 0 } { 0 . 0 4 0 0 0 } } = - 5 0 . 0 0 ,
$$

has the large relative error $1 . 9 \times 1 0 ^ { - 1 }$ .

Accuracy loss due to roundoff error can also be reduced by rearranging calculations, as shown in the next example.

# EXAMPLE 6

Evaluate $f ( x ) = x ^ { 3 } - 6 . 1 x ^ { 2 } + 3 . 2 x + 1 . 5$ at $x = 4 . 7 1$ using three-digit arithmetic.

Table 1.4 gives the intermediate results in the calculations. Carefully verify these re-sults to be sure that your notion of finite-digit arithmetic is correct. Note that the three-digit chopping values simply retain the leading three digits, with no rounding involved,and differ significantly from the three-digit rounding values.

# Table 1.4

<table><tr><td></td><td>x</td><td>x²</td><td>士</td><td>6.1x2</td><td>3.2x</td></tr><tr><td>Exact</td><td>4.71</td><td>22.1841</td><td>104.487111</td><td>135.32301</td><td>15.072</td></tr><tr><td>Three-digit (chopping)</td><td>4.71</td><td>22.1</td><td>104.</td><td>134.</td><td>15.0</td></tr><tr><td>Three-digit (rounding)</td><td>4.71</td><td>22.2</td><td>105.</td><td>135.</td><td>15.1</td></tr></table>

$$
f ( 4 . 7 1 ) = 1 0 4 . 4 8 7 1 1 1 - 1 3 5 . 3 2 3 0 1 + 1 5 . 0 7 2 + 1 . 5
$$

Three-digit (chopping): $f ( 4 . 7 1 ) = ( ( 1 0 4 . - 1 3 4 . ) + 1 5 . 0 ) + 1 . 5 = - 1 3 . 5 ;$

Three-digit (rounding): f(4.71) = ((105.- 135.) + 15.1) + 1.5 = -13.4.

The relative errors for the three-digit methods are

$$
\left| { \frac { - 1 4 . 2 6 3 8 9 9 + 1 3 . 5 } { - 1 4 . 2 6 3 8 9 9 } } \right| \approx 0 . 0 5 , \quad { \mathrm { f o r ~ c h o p p i n g } }
$$

and

$$
\left| { \frac { - 1 4 . 2 6 3 8 9 9 + 1 3 . 4 } { - 1 4 . 2 6 3 8 9 9 } } \right| \approx 0 . 0 6 , \quad { \mathrm { f o r ~ r o u n d i n g } } .
$$

As an alternative approach, $f ( x )$ can be written in a nested manner as

$$
f ( x ) = x ^ { 3 } - 6 . 1 x ^ { 2 } + 3 . 2 x + 1 . 5 = ( ( x - 6 . 1 ) x + 3 . 2 ) x + 1 . 5 .
$$

This gives

Three-c $\mathrm { l i g i t ~ ( c h o p p i n g ) } ; \quad f ( 4 . 7 1 ) = ( ( 4 . 7 1 - 6 . 1 ) 4 . 7 1 + 3 . 2 ) 4 . 7 1 + 1 . 5 = - 1 4 . 2$ and a three-digit rounding answer of -14.3. The new relative errors are

$$
\begin{array} { r l } { \mathrm { T h r e e - d i g i t } \left( \mathrm { c h o p p i n g } \right) : } & { \left| \frac { - 1 4 . 2 6 3 8 9 9 + 1 4 . 2 } { - 1 4 . 2 6 3 8 9 9 } \right| \approx 0 . 0 0 4 5 ; } \\ { \mathrm { T h r e e - d i g i t } \left( \mathrm { r o u n d i n g } \right) : } & { \left| \frac { - 1 4 . 2 6 3 8 9 9 + 1 4 . 3 } { - 1 4 . 2 6 3 8 9 9 } \right| \approx 0 . 0 0 2 5 . } \end{array}
$$

Nesting has reduced the relative error for the chopping approximation to less than $10 \%$ of that obtained initially. For the rounding approximation the improvement has been even more dramatic; the error in this case has been reduced by more than $95 \%$ · ■

Polynomials should always be expressed in nested form before performing an evaluation,because this form minimizes the number of arithmetic calculations.The decreased error in Example 6 is due to the reduction in computations from four multiplications and three additions to two multiplications and three additions. One way to reduce roundoff error is to reduce the number of error-producing computations.

# EXERCISE SET 1.2

1.Compute the absolute error and relative error in approximations of $p$ by $p ^ { * }$ · $\begin{array} { r l } { \mathbf { a } . } & { { } p = \pi , p ^ { * } = 2 2 / 7 } \\ { \mathbf { c } . } & { { } p = e , p ^ { * } = 2 . 7 1 8 } \end{array}$ $\begin{array} { r l } { \mathbf { b } _ { \cdot } } & { { } ~ p = \pi , p ^ { * } = 3 . 1 4 1 6 } \\ { \mathbf { d } _ { \cdot } } & { { } ~ p = { \sqrt { 2 } } , p ^ { * } = 1 . 4 1 4 } \end{array}$ e. $p = e ^ { 1 0 } , p ^ { * } = 2 2 0 0 0$ f.p = 10",p\*= 1400 g $p = 8 ! , p ^ { * } = 3 9 9 0 0$ $\begin{array} { r l } { \mathbf { h } . \ } & { { } p = 9 ! , p ^ { * } = \sqrt { 1 8 \pi } ( 9 / e ) ^ { 9 } } \end{array}$

2. Find the largest interval in which p\* must lie to approximate p with relative error at most 10-4 for each value of $p$

a. $\pi$ $\mathbf { b . } \_ e$ $\mathrm { ~ \bf ~ c ~ . ~ } \quad \sqrt { 2 } \quad \mathrm { ~ \bf ~ d . ~ } \quad \sqrt [ 3 ] { 7 }$

3. Suppose $p ^ { * }$ must approximate $p$ with relative error at most $1 0 ^ { - 3 }$ . Find the largest interval in which $p ^ { \ast }$ must lie for each value of $p$ ·

a.150 b.900 c.1500 d.90

4.Perform the following computations (i) exactly, (i)using three-digit chopping arithmetic,and (iii) using three-digit rounding arithmetic. (iv) Compute the relative errors in parts (ii） and (ii).

a. $\begin{array} { l } { { \frac { 4 } { 5 } + \frac { 1 } { 3 } } } \\ { { \left( \frac { 1 } { 3 } - \frac { 3 } { 1 1 } \right) + \frac { 3 } { 2 0 } } } \end{array}$ $\begin{array} { l l } { { \mathbf { b } . } } & { { \displaystyle \frac { 4 } { 5 } \cdot \frac { 1 } { 3 } } } \\ { { \mathbf { d } . } } & { { \displaystyle \left( \frac { 1 } { 3 } + \frac { 3 } { 1 1 } \right) - \frac { 3 } { 2 0 } } } \end{array}$   
c.

5. Use three-digit rounding arithmetic to perform the following calculations. Compute the absolute error and relative error with the exact value determined to at least five digits.

a. $1 3 3 + 0 . 9 2 1$ b. 133-0.499 c. (121 - 0.327)- 119 d. (121- 119)- 0.327 e. $\frac { \frac { 1 3 } { 1 4 } - \frac { 6 } { 7 } } { 2 e - 5 . 4 }$ $\begin{array} { r l } { \mathbf { f } . } & { { } - 1 0 \pi + 6 e - \frac { 3 } { 6 2 } } \\ { \mathbf { h } . } & { { } \frac { \pi - \frac { 2 2 } { 7 } } { \frac { 1 } { 1 7 } } } \end{array}$ g. $\left( { \frac { 2 } { 9 } } \right) \cdot \left( { \frac { 9 } { 7 } } \right)$

6.Repeat Exercise 5 using four-digit rounding arithmetic.

7.Repeat Exercise 5 using three-digit chopping arithmetic.

8.Repeat Exercise S using four-digit chopping arithmetic.

9.The first three nonzero terms of the Maclaurin series for the arctangent function are $x \textrm { -- }$ $( 1 / 3 ) x ^ { 3 } + ( 1 / 5 ) x ^ { 5 }$ . Compute the absolute error and relative error in the following approximations of $\pi$ using the polynomial in place of the arctangent:

： $4 \left[ \arctan \left( { \frac { 1 } { 2 } } \right) + \arctan \left( { \frac { 1 } { 3 } } \right) \right]$ ${ \bf b . } 1 6 \arctan \left( \frac { 1 } { 5 } \right) - 4 \arctan \left( \frac { 1 } { 2 3 9 } \right)$

10.The number $e$ can be defined by $\textstyle e = \sum _ { n = 0 } ^ { \infty } ( 1 / n ! )$ ， where $n ! = n ( n - 1 ) \cdot \cdot \cdot 2 \cdot 1$ for $n \neq 0$ and $0 ! = 1$ . Compute the absolute error and relative error in the following approximations of $e$ ：

a. $\sum _ { n = 0 } ^ { 5 } { \frac { 1 } { n ! } }$ $\mathbf { b } . \sum _ { n = 0 } ^ { 1 0 } { \frac { 1 } { n ! } }$

11.Let

$$
f ( x ) = { \frac { x \cos x - \sin x } { x - \sin x } } .
$$

a. Find $\scriptstyle \operatorname* { l i m } _ { x \to 0 } f ( x )$   
b. Use four-digit rounding arithmetic to evaluate $f ( 0 . 1 )$   
c. Replace each trigonometric function with its third Maclaurin polynomial,and repeat part (b).   
d. The actual value is $f ( 0 . 1 ) = - 1 . 9 9 8 9 9 9 9 8$ . Find the relative error for the values obtained in parts (b) and (c).

12.Let

$$
f ( x ) = { \frac { e ^ { x } - e ^ { - x } } { x } } .
$$

a. Find $\mathrm { l i m } _ { x \to 0 } ( e ^ { x } - e ^ { - x } ) / x$   
${ \bf { b } } .$ Use three-digit rounding arithmetic to evaluate $f ( 0 . 1 )$   
c. Replace each exponential function with its third Maclaurin polynomial, and repeat part (b).   
d. The actual value is $f ( 0 . 1 ) = 2 . 0 0 3 3 3 5 0 0 0$ . Find the relative error for the values obtained in parts (a) and (b).

$$
{ \begin{array} { r l r l } & { { \frac { 1 } { 3 } } x ^ { 2 } - { \cfrac { 1 2 3 } { 4 } } x + { \cfrac { 1 } { 6 } } = 0 } & & { \qquad \mathbf { b . } \quad { \frac { 1 } { 3 } } x ^ { 2 } + { \cfrac { 1 2 3 } { 4 } } x - { \cfrac { 1 } { 6 } } = 0 } \\ & { 1 . 0 0 2 x ^ { 2 } - 1 1 . 0 1 x + 0 . 0 1 2 6 5 = 0 } & & { \qquad \mathbf { d . } \quad 1 . 0 0 2 x ^ { 2 } + 1 1 . 0 1 x + 0 . 0 1 2 6 5 = 0 } \end{array} }
$$

14.Repeat Exercise 13 using four-digit chopping arithmetic.

15.Usethe 64-bit long real format tofind the decimal equivalentof the folowing floating-point machine numbers.

a. 0 10000001010 1001001100000000000000000000000000000000000000000000   
b. 1 10000001010 1001001100000000000000000000000000000000000000000000   
c. 0 01111111111 0101001100000000000000000000000000000000000000000000   
d. 0 01111111111 0101001100000000000000000000000000000000000000000001

16.Find the next largest and smallst machine numbers in decimal form for the numbers given in Exercise 15.

17. Suppose two points $( x _ { 0 } , y _ { 0 } )$ and $( x _ { 1 } , y _ { 1 } )$ are on a straight line with $y _ { 1 } \neq y _ { 0 }$ . Two formulas are available to find the $x$ -intercept of the line:

$$
x = { \frac { x _ { 0 } y _ { 1 } - x _ { 1 } y _ { 0 } } { y _ { 1 } - y _ { 0 } } } \quad { \mathrm { ~ a n d ~ } } \quad x = x _ { 0 } - { \frac { ( x _ { 1 } - x _ { 0 } ) y _ { 0 } } { y _ { 1 } - y _ { 0 } } } .
$$

a．Show that both formulas are algebraically correct.

b. Use the data $( x _ { 0 } , y _ { 0 } ) = ( 1 . 3 1 , 3 . 2 4 )$ and $( x _ { 1 } , y _ { 1 } ) = ( 1 . 9 3 , 4 . 7 6 )$ and three-digit rounding arithmetic to compute the $\pmb { x }$ -intercept both ways. Which method is better and why?

18. The Taylor polynomial of degree $\pmb { n }$ for $f ( x ) = e ^ { x }$ is $\scriptstyle \sum _ { i = 0 } ^ { n } ( x ^ { i } / i ! )$ . Use the Taylor polynomial of degree nine and three-digit chopping arithmetic to find an approximation to $e ^ { - 5 }$ by each of the following methods.

a. $e ^ { - 5 } \approx \sum _ { i = 0 } ^ { 9 } { \frac { ( - 5 ) ^ { i } } { i ! } } = \sum _ { i = 0 } ^ { 9 } { \frac { ( - 1 ) ^ { i } 5 ^ { i } } { i ! } }$ ${ \bf b } . \mathrm { ~ \ } e ^ { - 5 } = { \frac { 1 } { e ^ { 5 } } } \approx { \frac { 1 } { \sum _ { i = 0 } ^ { 9 } { \frac { 5 ^ { i } } { i ! } } } } .$ c. An approximate value of $e ^ { - 5 }$ Correct to three digits is $6 . 7 4 \times 1 0 ^ { - 3 }$ . Which formula, (a) or (b), gives the most accuracy, and why?

19. The two-by-two linear system

$$
\begin{array} { l } { { a x + b y = e , } } \\ { { } } \\ { { c x + d y = f , } } \end{array}
$$

where $a , b , c , d , e , f$ are given, can be solved for $\pmb { x }$ and $y$ as follows:

$$
\begin{array} { l } { d _ { 1 } = d - m b ; } \\ { f _ { 1 } = f - m e ; } \\ { y = \frac { f _ { 1 } } { d _ { 1 } } ; } \\ { x = \frac { ( e - b y ) } { a } . } \end{array}
$$

Solve the following linear systems using four-digit rounding arithmetic.

$$
\begin{array} { l } { { 1 . 1 3 0 x - 6 . 9 9 0 y = 1 4 . 2 0 \qquad \qquad \mathbf { b } . \quad 1 . 0 1 3 x - 6 . 0 9 9 y = 1 4 . 2 2 } } \\ { { 8 . 1 1 0 x + 1 2 . 2 0 y = - 0 . 1 3 7 0 \qquad \qquad \mathbf { d } . \quad - 1 8 . 1 1 x + 1 1 2 . 2 y = - 0 . 1 3 7 6 } } \end{array}
$$

20.Repeat Exercise 19 using four-digit chopping arithmetic.

21.a.Show that the polynomial nesting technique described in Example 6can also be applied to the evaluation of

$$
f ( x ) = 1 . 0 1 e ^ { 4 x } - 4 . 6 2 e ^ { 3 x } - 3 . 1 1 e ^ { 2 x } + 1 2 . 2 e ^ { x } - 1 . 9 9 .
$$

b. Use three-digit rounding arithmetic, the assumption that $e ^ { 1 . 5 3 } = 4 . 6 2$ , and the fact that $e ^ { n x } = ( e ^ { x } ) ^ { n }$ to evaluate $f ( 1 . 5 3 )$ as given in part (a).   
c. Redo the calculation in part (b) by first nesting the calculations.   
d. Compare the approximations in parts (b) and (c) to the true three-digit result $f ( 1 . 5 3 ) =$ $- 7 . 6 1$ ·

22.A rectangular parallelepiped has sides of length $3 \cos \mathbf { m }$ ， $4 \thinspace { \mathrm { c m } }$ ,and ${ \mathfrak { s } } \mathrm { c m }$ , measured to the nearest centimeter. What are the best upper and lower bounds for the volume of this parallelepiped? What are the best upper and lower bounds for the surface area?

23.Let $P _ { n } ( x )$ be the Maclaurin polynomial of degree $\pmb { n }$ for the arctangent function. Use Maple carrying 75 decimal digits to find the value of $\pmb { n }$ required to approximate $\pi$ to within $1 0 ^ { - 2 5 }$ using the following formulas.

$$
4 \left[ P _ { n } \left( { \frac { 1 } { 2 } } \right) + P _ { n } \left( { \frac { 1 } { 3 } } \right) \right] \qquad { \mathbf { b } } , \quad 1 6 P _ { n } \left( { \frac { 1 } { 5 } } \right) - 4 P _ { n } \left( { \frac { 1 } { 2 3 9 } } \right)
$$

24.Suppose that $f l ( \boldsymbol { y } )$ is a $k$ -digit rounding approximation to y. Show that

$$
\left| \frac { y - f l ( y ) } { y } \right| \leq 0 . 5 \times 1 0 ^ { - k + 1 } .
$$

[Hint: If $d _ { k + 1 } < 5$ ,then $f l ( y ) = 0 . d _ { 1 } d _ { 2 } \dots d _ { k } \times 1 0 ^ { n }$ .If $d _ { k + 1 } \geq 5$ ,then $f l ( y ) = 0 . d _ { 1 } d _ { 2 } \dots d _ { k } \times$ $1 0 ^ { n } + 1 0 ^ { n - k } .$ ]

25.The binomial coefficient

$$
{ \binom { m } { k } } = { \frac { m ! } { k ! \left( m - k \right) ! } }
$$

describes the number of ways of choosing a subset of $k$ objects from a set of m elements.

a.Suppose decimal machine numbers are of the form

$$
\pm 0 . d _ { 1 } d _ { 2 } d _ { 3 } d _ { 4 } \times 1 0 ^ { n } , \quad \mathrm { w i t h } 1 \leq d _ { 1 } \leq 9 , \ 0 \leq d _ { i } \leq 9 , i f i = 2 , 3 , 4 \quad \mathrm { a n d } \quad | n | \leq 1 5 .
$$

What is the largest value of $m$ for which the binomial coefficient $\binom { m } { k }$ can be computed for all $k$ by the definition without causing overflow?

b.Show that $\binom { m } { k }$ can also be computed by

$$
{ \binom { m } { k } } = \left( { \frac { m } { k } } \right) \left( { \frac { m - 1 } { k - 1 } } \right) \cdot \cdot \cdot \left( { \frac { m - k + 1 } { 1 } } \right) .
$$

c. What is the largest value of $m$ for which the binomial coefficient $\binom { m } { 3 }$ can be computed by the formula in part (b) without causing overflow?   
d. Use the equation in (b） and four-digit chopping arithmetic to compute the number of possible 5-card hands in a 52-card deck. Compute the actual and relative errors.

26.Let $f \in C [ a , b ]$ be a function whose derivative exists on $( a , b )$ . Suppose $f$ is to be evaluated at $\mathtt { \mathtt { x } _ { 0 } }$ in $( a , b )$ , but instead of computing the actual value $f ( x _ { 0 } )$ , the approximate value, $\tilde { f } ( \boldsymbol { x } _ { 0 } )$ ， is the actual value of $f$ at $x _ { 0 } + \epsilon$ ,that is, $\tilde { f } ( x _ { 0 } ) = f ( x _ { 0 } + \epsilon )$

a. Use the Mean Value Theorem to estimate the absolute error $| f ( x _ { 0 } ) - { \tilde { f } } ( x _ { 0 } ) |$ and the relative error $| f ( x _ { 0 } ) - \tilde { f } ( x _ { 0 } ) | / | f ( x _ { 0 } ) |$ , assuming $f ( x _ { 0 } ) \neq 0$   
b. If $\epsilon = 5 \times 1 0 ^ { - 6 }$ and $x _ { 0 } = 1$ ， find bounds for the absolute and relative errors for i $f ( x ) = e ^ { x }$ ii.f(x)= sin x   
c. Repeat part (b) with $\epsilon = ( 5 \times 1 0 ^ { - 6 } ) x _ { 0 }$ and $x _ { 0 } = 1 0$

27.The following Maple procedure chops a floating-point number $x$ to $t$ digits.

$\mathtt { c h o p : = p r o c ( x , t ) }$ ； if $\mathbf { \boldsymbol { x } } { = } 0$ then 0 else e:=trunc(evalf(logi0(abs(x)))); if e>0 then $\theta : = \theta + 1$ fi； x2:=evalf(trunc(x\*10^{)(t-e))\*10^{}(e-t)); fi   
end;

Verify the procedure works for the following values.

$$
\begin{array} { l l } { x = 1 2 4 . 0 3 1 , \ t = 5 } \\ { x = - 1 2 4 . 0 3 1 , \ t = 5 } \\ { x = 0 . 0 0 6 5 3 , \ t = 2 } \\ { x = - 0 . 0 0 6 5 3 , \ t = 2 } \end{array} \qquad \begin{array} { l l } { \mathbf { b . } } & { x = 1 2 4 . 0 3 6 , \ t = 5 } \\ { \mathbf { d . } } & { x = - 1 2 4 . 0 3 6 , \ t = 5 } \\ { \mathbf { f . } } & { x = 0 . 0 0 6 5 6 , \ t = 2 } \\ { \mathbf { h . } } & { x = - 0 . 0 0 6 5 6 , \ t = 2 } \end{array}
$$

28. The opening example to this chapter described a physical experiment involving the temperature of a gas under pressure. In this application, we were given $P = 1 . 0 0$ atm, $V = 0 . 1 0 0 \mathrm { m } ^ { 3 }$ $N = 0 . 0 0 4 2 0 \mathrm { m o l }$ ,and $R = 0 . 0 8 2 0 6$ . Solving for $T$ in the ideal gas law gives

$$
T = { \frac { P V } { N R } } = { \frac { \cdot ( 1 . 0 0 ) ( 0 . 1 0 0 ) } { ( 0 . 0 0 4 2 0 ) ( 0 . 0 8 2 0 6 ) } } = 2 9 0 . 1 5 \mathrm { K } = 1 7 ^ { \circ } \mathrm { C } .
$$

In the laboratory, it was found that $T$ was $1 5 \textdegree C$ under these conditions,and when the pressure was doubled and the volume halved, T was 19°C.Assume that the data are rounded values accurate to the places given,and show that both laboratory figures are within the bounds of accuracy for the ideal gas law.

# 1.3 Algorithms and Convergence

Throughout the text we will be examining approximation procedures, called algorithms, involving sequences of calculations. An algorithm is a procedure that describes,in an unambiguous manner, a finite sequence of steps to be performed in a specified order. The object of the algorithm is to implement a procedure to solve a problem or approximate a solution to the problem.

We use a pseudocode to describe the algorithms. This pseudocode specifies the form of the input to be supplied and the form of the desired output. Not all numerical procedures give satisfactory output for arbitrarily chosen input. As a consequence, a stopping technique independent of the numerical technique is incorporated into each algorithm to avoid infinite loops.

Two punctuation symbols are used in the algorithms:

A period (.) indicates the termination of a step, a semicolon (;) separates tasks within a step.

Indentation is used to indicate that groups of statements are to be treated as a single entity. Looping techniques in the algorithms are either counter-controlled,such as,

$$
\begin{array} { l l } { { \mathrm { F o r } } } & { { i = 1 , 2 , \dots , n } } \\ { { } } & { { } } \\ { { \mathrm { S e t } } } & { { x _ { i } = a _ { i } + i \cdot h } } \end{array}
$$

or condition-controlled, such as

To allow for conditional execution, we use the standard

If .. .then

or

If..then

else

constructions.

The steps in the algorithms follow the rules of structured program construction. They have been arranged so that there should be minimal diffculty translating pseudocode into any programming language suitable for scientific applications.

The algorithms are liberally laced with comments. These are written in italics and contained within parentheses to distinguish them from the algorithmic statements.

# EXAMPLE 1

An algorithm to compute

$$
\sum _ { i = 1 } ^ { N } x _ { 1 } + x _ { 2 } + \cdots + x _ { N } ,
$$