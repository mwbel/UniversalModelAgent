# 36 Implementable Implicit Runge–Kutta Methods

360 Implementation of implicit Runge–Kutta methods

Because of the implicit nature of these methods, every step requires the solution of an algebraic system. For an $s$ -stage method with an $N$ -dimensional problem, there are $s N$ unknowns to evaluate and these satisfy $s N$ equations. If $f$ is nonlinear, then the large system of equations to be solved is also nonlinear. However, there are linear parts of it, and it may be possible to exploit this in their numerical solution. Let $A$ denote the coefficient matrix; then the stage values need to be computed as solutions to the system of equations

$$
\begin{array} { l } { { \displaystyle Y _ { 1 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { 1 j } f ( Y _ { j } ) } . } \\ { ~ } \\ { { \displaystyle Y _ { 2 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { 2 j } f ( Y _ { j } ) } . } \\ { { \displaystyle \quad \vdots \qquad } } \\ { { \displaystyle Y _ { s } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { s j } f ( Y _ { j } ) } . } \end{array}
$$

For an $N$ -dimensional differential equation system, this amounts to a system of $s N$ non-linear equations.

We consider how to solve these equations using a full Newton method. This requires going through the following steps:


<!-- chunk 0005: pages 281-350 -->
1. Compute approximations to $Y _ { 1 }$ , $Y _ { 2 }$ , . . . , $Y _ { s }$ using information available at the start of the step. Denote these ‘predicted’ values by $Y _ { i } ^ { [ 0 ] }$ , $i = 1 , 2 , \dots , s$ .

2. Carry out a sequence of iterations leading to approximations $Y _ { i } ^ { \left[ k \right] }$ , for $k = 1 , 2 , \dots$ , $i = 1 , 2 , \dots , s$ . These are given by the formulae

$$
Y _ { i } ^ { [ k ] } = Y _ { i } ^ { [ k - 1 ] } - \Delta _ { i } ,
$$

where

$$
\sum _ { j = 1 } ^ { s } m _ { i j } \Delta _ { j } = \phi _ { i } , \qquad i = 1 , 2 , \ldots , s ,
$$

with

$$
\phi _ { i } = Y _ { i } ^ { [ k - 1 ] } - y _ { n - 1 } - h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ^ { [ k - 1 ] } )
$$

and

$$
m _ { i j } = \delta _ { i j } I - h a _ { i j } f ^ { \prime } ( Y _ { j } ^ { [ k - 1 ] } ) .
$$

3. Test for convergence and terminate when each of $\lVert \Delta _ { 1 } \rVert$ , $| | \Delta _ { 2 } | |$ , . . . , $\| \Delta _ { s } \|$ are sufficiently small. Suppose that this happens in the computation of iteration $k$ .

4. Assign $Y _ { i } ^ { \left[ k \right] }$ to $Y _ { i }$ , for each $i = 1 , 2 , \dots , s$

In a practical calculation, it is usual to simplify this computation in various ways. Most importantly, the solution of (360a), preceded by the evaluation of the elements of $m _ { i j }$ which depend on $f ^ { \prime }$ evaluated at each stage and in each iteration, requires a large number of algebraic operations; these are to be avoided whenever possible.

A typical simplification is to replace the value of $f ^ { \prime } ( Y _ { j } ^ { [ k - 1 ] } )$ by a constant approximation to this Jacobian matrix. This approximation is maintained at a fixed value over every iteration and over each stage, and possibly over many steps. This means that the $s N \times s N$ matrix with elements built up from the submatrices $m _ { i j }$ can be replaced by a matrix of the form

$$
I _ { s } \otimes I _ { N } - h A \otimes J ,
$$

where $J$ is the Jacobian approximation. The cost, measured solely in terms of linear algebra costs, divides into two components. First, the factorization of the matrix (360b), carried out from time to time during the computation, costs a small multiple of $s ^ { 3 } N ^ { 3 }$ floating point operations. Secondly, the solution of (360a) costs a small multiple of $s ^ { 2 } N ^ { 2 }$ arithmetic operations per iteration.

It is the aim of the study of implementable methods to lower the factors $s ^ { 3 }$ in the occasional part of the cost and to lower the factor $s ^ { 2 }$ in the ‘per iteration’ part of the cost.
