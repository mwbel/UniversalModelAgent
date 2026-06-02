# 395 Solving the implicit equations

For stiff problems, the methods of choice are implicit. We discuss some aspects of the technical problem of evaluating the stages of an implicit Runge–Kutta method. For a one-stage method, the evaluation technique is also similar for backward difference methods and for Runge–Kutta and general linear methods that have a lower triangular coefficient matrix.

For these simple methods, the algebraic question takes the form

$$
Y - h \gamma f ( X , Y ) = U ,
$$

where $X$ and $U$ are known. Let $J ( X , Y )$ denote the Jacobian matrix with elements given by

$$
J ( X , Y ) _ { i j } = \frac { \partial f _ { i } } { \partial y _ { j } } ( X , Y ) , \qquad i , j , = 1 , 2 , \ldots , N .
$$

A full Newton scheme would start with the use of a predictor to obtain a first approximation to $Y$ . Denote this by $Y ^ { \left[ 0 \right] }$ and update it with a sequence of approximations $Y ^ { \left\lfloor i \right\rfloor }$ , $i = 1 , 2 , \dots$ , given by

$$
Y ^ { [ i ] } = Y ^ { [ i - 1 ] } - \Delta ,
$$

where

$$
( I - h \gamma J ( X , Y ^ { [ i - 1 ] } ) ) \Delta = Y ^ { [ i - 1 ] } - h \gamma f ( X , Y ^ { [ i - 1 ] } ) - U .
$$

Although the full scheme has the advantage of quadratic convergence, it is usually not adopted in practice. The reason is the excessive cost of evaluating the Jacobian $J$ and of carrying out the LU factorization of the matrix $I - h \gamma J$ . The Newton scheme can be modified in various ways to reduce this cost. First, the re-evaluation of $J$ after each iteration can be dispensed with. Instead the scheme (395b) can be replaced by

$$
( I - h \gamma J ( X , Y ^ { [ 0 ] } ) ) \Delta = Y ^ { [ i - 1 ] } - h \gamma f ( X , Y ^ { [ i - 1 ] } ) - U ,
$$

and for many problems this is almost as effective as the full Newton method. Even if more iterations are required, the additional cost is often less than the saving in $J$ evaluations and LU factorizations.

Secondly, in the case of diagonally implicit methods, it is usually possible to evaluate $J$ only once per step, for example at the start of the first stage. Assuming the Jacobian is sufficiently slowly varying, this can be almost as effective as evaluating the Jacobian once for each stage.

The third, and most extreme, of the Jacobian update schemes is the use of the same approximation over not just one step but over many steps. A typical algorithm signals the need to re-evaluate $J$ only when the rate of convergence is sufficiently slow as to justify this expenditure of resources to achieve an overall improvement. When $J$ is maintained at a constant value over many steps, we have to ask the further question about when $I \mathrm { ~ - ~ } h \gamma J$ should be refactorized. Assuming that $\gamma$ is unchanged, any change in $h$ will affect the convergence by using a factorization of this matrix which is based not only on an incorrect value of $J$ , but on what may be a vastly different value of $h$ .

It may be possible to delay the refactorization process by introducing a ‘relaxation factor’ into the iteration scheme. That is, when $\Delta$ has been computed in a generalized form of (395b), the update takes the form

$$
Y ^ { [ i ] } = Y ^ { [ i - 1 ] } - \theta \Delta ,
$$

where $\theta$ is a suitably chosen scalar factor. To analyse how this works, suppose for simplicity that $J$ is constant but that $h$ has changed from $\overline { { h } }$ at the time the factorization took place to $r { \bar { h } }$ at the time a generalized Newton step is being carried out. As a further simplification, assume that $f ( x , y ) = J y + V$ and that we are exploring the behaviour in a direction along along an eigenvector corresponding to an eigenvalue $\lambda$ . Write $z = \overline { { h } } \gamma \lambda$ . Under these assumptions the iteration scheme effectively seeks a solution to an equation of the form

$$
\eta - r z \eta = a ,
$$

with solution $\eta = \eta ^ { * } = a / ( 1 - r )$ , using an iteration scheme which replaces $\eta ^ { * } + \epsilon$ by $\eta ^ { * } + \phi ( z ) \epsilon$ , where

$$
\phi ( z ) = 1 - \theta \frac { 1 - r z } { 1 - z } .
$$

Convergence will depend on the magnitude of $\phi ( z )$ for all $z$ that are likely to arise. Values of $z$ near zero correspond to non-stiff components of the problem, and values of $z$ with large magnitude in the left half-plane correspond to stiff components. Hence, it seems desirable to choose $\theta$ to minimize $| \phi ( z ) |$ for $z$ in the left half-plane. The value that achieves this is

$$
\theta = { \frac { 2 } { 1 + r } } .
$$

For fully implicit Runge–Kutta methods, the problem of evaluating the stages becomes much more complicated and potentially more costly. For a method with coefficient matrix $A$ , we need to consider all stages at the same time. Let $Y$ denote the $s N$ -dimensional vector made up from $Y _ { 1 }$ , $Y _ { 2 }$ , . . . , $Y _ { s }$ . Furthermore the approximation sequence will be written as $Y ^ { \left[ j \right] }$ , $j = 0 , 1 , \ldots$ , each also made up from $s$ subvectors, and $\Delta$ will denote a vector in $\mathbb { R } ^ { s N }$ made up from the subtrahends in each of the $s$ components in iteration $i$ . Thus

$$
\begin{array} { r } { Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad Y ^ { [ i ] } = \left[ \begin{array} { c } { Y _ { 1 } ^ { [ i ] } } \\ { Y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { Y _ { s } ^ { [ i ] } } \end{array} \right] , \quad \Delta = \left[ \begin{array} { c } { \Delta _ { 1 } } \\ { \Delta _ { 2 } } \\ { \vdots } \\ { \Delta _ { s } } \end{array} \right] = \left[ \begin{array} { c } { Y _ { 1 } ^ { [ i - 1 ] } - Y _ { 1 } ^ { [ i ] } } \\ { Y _ { 2 } ^ { [ i - 1 ] } - Y _ { 2 } ^ { [ i ] } } \\ { \vdots } \\ { Y _ { s } ^ { [ i - 1 ] } - Y _ { s } ^ { [ i ] } } \end{array} \right] . } \end{array}
$$

In place of (395a), the algebraic equations to solve in a step take the form

$$
Y - h A \otimes f ( X , Y ) = U \in \mathbb { R } ^ { s N } .
$$

Note that $f ( X , Y )$ denotes a vector in $\mathbb { R } ^ { s N }$ made up from subvectors of the form $f ( X _ { j } , Y _ { j } )$ , $j = 1 , 2 , \dots , s$ . The iteration scheme consists of solving the equations

$$
\Delta _ { j } - h \sum _ { k = 1 } ^ { s } a _ { j k } J \bigl ( X _ { k } , Y _ { k } ^ { [ i ] } \bigr ) \Delta _ { k } = Y _ { j } - h \sum _ { k = 1 } ^ { s } a _ { j k } f \bigl ( X _ { k } , Y _ { k } ^ { [ i ] } \bigr ) - U _ { i } ,
$$

and then carrying out the update $Y _ { j } ^ { [ i ] } = Y _ { j } ^ { [ i - 1 ] } - \Delta _ { j }$ , $j = 1 , 2 , \dots , s$ . If it is assumed that Jacobians are evaluated only once per step, or even less frequently, then we can write (395c) in the simplified form

$$
( I _ { s } \otimes I _ { N } - h A \otimes J ) \Delta = Y ^ { [ i - 1 ] } - h A \otimes F ^ { [ i - 1 ] } - U ,
$$

where $F ^ { [ i - 1 ] }$ is the vector with $k$ th subvector equal to $f \big ( X _ { k } , Y _ { k } ^ { \lfloor i - 1 \rfloor } \big )$ . Here $J$ is a single approximation to the $n \times n$ Jacobian matrix. One of the advantages of using a single $J$ approximation is the fact that it is possible to operate, for example, with similarity transformations, on the coefficient matrix $A$ and $J$ independently.

If no such transformation is carried out, the computational costs can become very severe. The LU factorization of the matrix on the left-hand side of (395d) requires a number of operations proportional to $s ^ { 3 } N ^ { 3 }$ , compared with just $N ^ { 3 }$ if $s = 1$ . However, if $A = T ^ { - 1 } \widehat { A } T$ , where $\widehat { A }$ has a structure close to diagonal, then the cost reduces to something like $s N ^ { 3 }$ .

# Exercises 39

39.1 An implicit Runge–Kutta method is to be implemented for the solution of non-stiff problems using functional iteration to solve the nonlinear equations. How should the stepsize be selected?

39.2 A Runge–Kutta method of order $p$ is used over an interval of length $X$ . Suppose that for a subinterval of length $( 1 - \theta ) X$ the error in a step of length $h$ is $C h ^ { p + 1 }$ , and for the remaining distance $\theta X$ the error is $\alpha C h ^ { 5 }$ . Assume that a large number $N$ of steps are performed, of which $( 1 - \phi ) N$ are in the first subinterval and $\phi N$ are in the second subinterval. Determine the value of $\phi$ which will minimize the total error committed in the integration.

39.3 Compare the result found in Exercise 39.2 with the result that would be obtained from an ‘error per unit step’ argument.
