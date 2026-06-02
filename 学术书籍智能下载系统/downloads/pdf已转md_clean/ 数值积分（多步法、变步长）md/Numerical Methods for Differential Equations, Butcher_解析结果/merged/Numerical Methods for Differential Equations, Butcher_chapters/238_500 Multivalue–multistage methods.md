# 500 Multivalue–multistage methods

The systematic computation of an approximation to the solution of an initial value problem usually involves just two operations: evaluation of the function $f$ defining the differential equation and the forming of linear combinations of previously computed vectors. In the case of implicit methods, further complications arise, but these can also be brought into the same general linear formulation.

We consider methods in which a collection of vectors forms the input at the beginning of a step, and a similar collection is passed on as output from the current step and as input into the following step. Thus the method is a multivalue method, and we write $r$ for the number of quantities processed in this way. In the computations that take place in forming the output quantities, there are assumed to be $s$ approximations to the solution at points near the current time step for which the function $f$ needs to be evaluated. As for Runge–Kutta methods, these are known as stages and we have an $s$ -stage or, in general, multistage method.

The intricate set of connections between these quantities make up what is known as a general linear method. Following Burrage and Butcher (1980), we represent the method by four matrices which we will generally denote by $A$ , $U$ , $B$ and $V$ . These can be written together as a partitioned $( s + r ) \times ( s + r )$ matrix

$$
\left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] .
$$

The input vectors available at step $n$ will be denoted by $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ , $y _ { 2 } ^ { \lfloor n - 1 \rfloor }$ , y[n−1] r . During the computations which constitute the step, stage values Y1, $Y _ { 2 }$ , . . . , $Y _ { s }$ , are computed and derivative values $F _ { i } = f ( Y _ { i } )$ , $i = 1 , 2 , \dots , s$ , are computed in terms of these. Finally, the output values are computed and, because these will constitute the input at step $n + 1$ , they will be denoted by $y _ { i } ^ { \lfloor n \rfloor }$ , $i = 1 , 2 , \dots , r$ . The relationships between these quantities are defined in terms of the elements of $A$ , $U$ , $B$ and $V$ by the equations

$$
\begin{array} { c } { { Y _ { i } = \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } h F _ { j } + \sum _ { j = 1 } ^ { r } u _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , s , } } \\ { { y _ { i } ^ { [ n ] } = \displaystyle \sum _ { j = 1 } ^ { s } b _ { i j } h F _ { j } + \sum _ { j = 1 } ^ { r } v _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , r . } } \end{array}
$$

It will be convenient to use a more concise notation, and we start by defining vectors $\boldsymbol { Y } , \boldsymbol { F } \in \mathbb { R } ^ { s N }$ and $y ^ { \lfloor n - 1 \rfloor } , y ^ { \lfloor n \rfloor } \in \mathbb { R } ^ { r N }$ as follows:

$$
\begin{array} { r } { Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad F = \left[ \begin{array} { c } { F _ { 1 } } \\ { F _ { 2 } } \\ { \vdots } \\ { F _ { s } } \end{array} \right] , \quad y ^ { [ n - 1 ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n - 1 ] } } \\ { y _ { 2 } ^ { [ n - 1 ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n - 1 ] } } \end{array} \right] , \quad y ^ { [ n ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n ] } } \\ { y _ { 2 } ^ { [ n ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n ] } } \end{array} \right] . } \end{array}
$$

Using these supervectors, it is possible to write (500a) and (500b) in the form

$$
\left[ \begin{array} { c } { Y } \\ { y ^ { [ n ] } } \end{array} \right] = \left[ \begin{array} { c c } { A \otimes I _ { N } } & { U \otimes I _ { N } } \\ { B \otimes I _ { N } } & { V \otimes I _ { N } } \end{array} \right] \left[ \begin{array} { c } { h F } \\ { y ^ { [ n - 1 ] } } \end{array} \right] .
$$

In this formulation, $I _ { N }$ denotes the $N \times N$ unit matrix and the Kronecker product is given by

$$
A \otimes I _ { N } = \left[ \begin{array} { c c c c } { a _ { 1 1 } I _ { N } } & { a _ { 1 2 } I _ { N } } & { \cdot \cdot \cdot } & { a _ { 1 s } I _ { N } } \\ { a _ { 2 1 } I _ { N } } & { a _ { 2 2 } I _ { N } } & { \cdot \cdot \cdot } & { a _ { 2 s } I _ { N } } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { a _ { s 1 } I _ { N } } & { a _ { s 2 } I _ { N } } & { \cdot \cdot \cdot } & { a _ { s s } I _ { N } } \end{array} \right] .
$$

When there is no possibility of confusion, we simplify the notation by replacing

$$
\left[ \begin{array} { l l } { A \otimes I _ { N } } & { U \otimes I _ { N } } \\ { B \otimes I _ { N } } & { V \otimes I _ { N } } \end{array} \right] \quad \mathrm { b y } \quad \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] .
$$

In Subsections 502–505, we illustrate these ideas by showing how some known methods, as well as some new methods, can be formulated in this manner. First, however, we will discuss the possibility of transforming a given method into one using a different arrangement of the data passed from step to step.
