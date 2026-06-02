# 541 The types of DIMSIM methods

‘Diagonally implicit multistage integration methods’ (DIMSIMs) were introduced in Butcher (1995a). A DIMSIM is loosely defined as a method in which the four integers $p$ (the order), $q$ (the stage order), $r$ (the number of data vectors passed between steps) and $s$ (the number of stages) are all approximately equal. To be a DIMSIM, a method must also have a diagonally implicit structure. This means that the $s \times s$ matrix $A$ has the form

$$
A = \left[ \begin{array} { c c c c c } { { \lambda } } & { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { \lambda } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { \lambda } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { a _ { s 1 } } } & { { a _ { s 2 } } } & { { a _ { s 3 } } } & { { \cdots } } & { { \lambda } } \end{array} \right] ,
$$

where $\lambda \geq 0$ . The rationale for this restriction on this coefficient matrix is that the stages can be computed sequentially, or in parallel if the lower triangular part of $A$ is zero. This will lead to a considerable saving over a method in which $A$ has a general implicit structure. For Runge–Kutta methods, where $r = 1$ , this sort of method is referred to as explicit if $\lambda = 0$ or as diagonally implicit (DIRK, or as singly diagonally implicit or SDIRK) if $\lambda > 0$ ; see Subsection 361.

Types of DIMSIM and related methods   

<table><tr><td>Type</td><td colspan="4"></td><td>Application</td><td></td><td>1Architecture</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>：</td><td>0</td><td></td><td></td></tr><tr><td></td><td>a21</td><td>0</td><td>0</td><td>：</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>a31</td><td>a32</td><td>0</td><td>：</td><td>0</td><td>Non-stiff</td><td>Sequential</td></tr><tr><td></td><td>：</td><td>：</td><td>：</td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td>as1</td><td>as2</td><td>as3</td><td>：</td><td>0 1</td><td></td><td></td></tr><tr><td></td><td>入</td><td>0</td><td>0</td><td>：：</td><td>0 1</td><td></td><td></td></tr><tr><td></td><td>a21</td><td>入</td><td>0</td><td>：</td><td>0</td><td></td><td></td></tr><tr><td>2</td><td>a31</td><td>a32</td><td>入</td><td>：</td><td>0</td><td>Stiff</td><td>Sequential</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>：</td><td>：</td><td>：</td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td>as1</td><td>as2</td><td>as3</td><td>：</td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>：…</td><td>0</td><td></td><td></td></tr><tr><td>3</td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td>Non-stiff</td><td>Parallel</td></tr><tr><td></td><td>：</td><td>：</td><td></td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>：</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>：.</td><td>0</td><td></td><td></td></tr><tr><td></td><td>入</td><td>0</td><td>0</td><td>：：</td><td>0</td><td></td><td></td></tr><tr><td></td><td>0</td><td>入</td><td>0</td><td></td><td>0</td><td></td><td></td></tr><tr><td>4</td><td>0</td><td>0</td><td>入</td><td></td><td>0</td><td>Stiff</td><td>Parallel</td></tr><tr><td></td><td></td><td>：</td><td>：</td><td></td><td>：</td><td></td><td></td></tr><tr><td></td><td>：</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td></td><td>入</td><td></td><td></td></tr></table>

While these Runge–Kutta methods suffer from the disadvantages associated with low stage order, there is no such difficulty associated with general linear methods.

For non-stiff problems, it is advantageous to choose $\lambda = 0$ , whereas for stiff problems, it is necessary that $\lambda > 0$ , if A-stability is to be achieved. Furthermore, as we have already remarked, parallel evaluation of the stages is only possible if $A$ is a diagonal matrix; specifically, this would be the zero matrix in the non-stiff case. From these considerations, we introduce the ‘types’ of a DIMSIM method, and we retain this terminology for methods with a similar structure.

The four types, together with their main characteristics, are shown in Table 541(I). The aim in DIMSIM methods has been to find methods in which $p$ , $q$ , $r$ and $s$ are equal, or approximately equal, and at the same time to choose $V$ as a simple matrix, for example a matrix with rank 1.

If $p = q$ , it is a simple matter to write down conditions for this order and stage order. We have the following result:

Theorem 541A A method

$$
\textstyle \left[ { \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} } \right] ,
$$

has order and stage order $p$ if and only if there exists a function

$$
\phi : \mathbb { C } \to \mathbb { C } ^ { r } ,
$$

analytic in a neighbourhood of $0$ , such that

$$
\begin{array} { r } { \exp ( c z ) = z A \exp ( c z ) + U \phi ( z ) + O ( z ^ { p + 1 } ) , } \\ { \exp ( z ) \phi ( z ) = z B \exp ( c z ) + V \phi ( z ) + O ( z ^ { p + 1 } ) , } \end{array}
$$

where $\exp ( c z )$ denotes the vector in $\mathbb { C } ^ { s }$ for which component $i$ is equal to $\exp ( c _ { i } z )$ .

Proof. Assume that (541a) and (541b) are satisfied and that the components of $\phi ( z )$ have Taylor series

$$
\phi _ { i } ( z ) = \sum _ { j = 0 } ^ { p } \alpha _ { i j } z ^ { j } + O ( z ^ { p + 1 } ) .
$$

Furthermore, suppose starting method $i$ is chosen to give the output

$$
\sum _ { j = 0 } ^ { p } \alpha _ { i j } h ^ { j } y ^ { ( j ) } ( x _ { 0 } ) + O ( h ^ { p + 1 } ) ,
$$

where $y$ denotes the exact solution agreeing with a given initial value at $x _ { 0 }$ Using this starting method, consider the value of

$$
y ( x _ { 0 } + h c _ { k } ) - h \sum _ { i = 1 } ^ { s } a _ { k i } y ^ { \prime } ( x _ { 0 } + h c _ { i } ) - \sum _ { i = 1 } ^ { r } U _ { k i } \sum _ { j = 0 } ^ { p } \alpha _ { i j } h ^ { j } y ^ { ( j ) } ( x _ { 0 } ) .
$$

If this is $O ( h ^ { p + 1 } )$ then it will follow that $Y _ { k } - y ( x _ { 0 } + h c _ { k } ) = O ( h ^ { p + 1 } )$ . Expand (541c) about $x _ { 0 }$ , and it is seen that the coefficient of $h ^ { j } y ^ { ( j ) } ( x _ { 0 } )$ is

$$
{ \frac { 1 } { j ! } } c _ { k } ^ { j } - \sum _ { i = 1 } ^ { s } a _ { k i } { \frac { 1 } { ( j - 1 ) ! } } c _ { i } ^ { j - 1 } - \sum _ { i = 1 } ^ { r } U _ { k i } \alpha _ { i j } .
$$

However, this is exactly the same as the coefficient of $z ^ { j }$ in the Taylor expansion of the difference of the two sides of (541a). Given that the order

of the stages is $p$ , and therefore that $h f ( Y _ { i } ) = h y ^ { \prime } ( x _ { 0 } + h c _ { i } ) + O ( h ^ { p + 1 } )$ , we can carry out a similar analysis of the condition for the $k$ th output vector to equal

$$
\sum _ { j = 0 } ^ { p } \alpha _ { k j } h ^ { j } y ^ { [ j ] } ( x _ { 0 } + h ) + O ( h ^ { p + 1 } ) .
$$

Carry out a Taylor expansion about $x _ { 0 }$ and we find that (541d) can be written as

$$
\sum _ { j = 0 } ^ { p } \sum _ { i = j } ^ { p } \alpha _ { k j } \frac { 1 } { ( i - j ) ! } h ^ { i } y ^ { ( i ) } ( x _ { 0 } ) + O ( h ^ { p + 1 } ) .
$$

The coefficient of $h ^ { i }$ in (541e) is identical to the coefficient of $z ^ { i }$ in $\exp ( z ) \phi _ { k } ( z )$ . Hence, combining this with the terms

$$
\sum _ { i = 1 } ^ { s } b _ { k i } \frac { 1 } { ( j - 1 ) ! } c _ { i } ^ { j - 1 } + \sum _ { i = 1 } ^ { r } V _ { k i } \alpha _ { i j } ,
$$

we find (541b).

To prove necessity, use the definition of order given by (532e) and (532f) and evaluate the two sides of each of these equations for the sequence of trees $t _ { 0 } = \emptyset$ , $t _ { 1 } = \tau$ , $t _ { 2 } = [ t _ { 1 } ]$ , $\cdot \cdot \cdot$ , $t _ { p } = [ t _ { p - 1 } ]$ . Use the values of $\alpha _ { i j }$ given by

$$
\alpha _ { i j } = \xi _ { i } ( t _ { j } ) ,
$$

so that

$$
( E \xi _ { i } ) ( t _ { j } ) = \sum _ { k = 0 } ^ { j } \frac { 1 } { k ! } \xi _ { i } ( t _ { j - k } ) ,
$$

which is the coefficient of $z ^ { j }$ in $\textstyle \exp ( z ) \sum _ { k = 0 } ^ { p } \alpha _ { i k } z ^ { k }$ . We also note that

$$
\eta _ { i } ( t _ { j } ) = \frac { 1 } { j ! } c _ { i } ^ { j } , \qquad ( \eta _ { i } D ) ( t _ { j } ) = \frac { 1 } { ( j - 1 ) ! } c _ { i } ^ { j - 1 } ,
$$

which are, respectively, the $z ^ { j }$ coefficients in $\exp ( c _ { i } z )$ and in $z \exp ( c _ { i } z )$ . Write $\phi ( z )$ as the vector-valued function with $i$ th component equal to $\scriptstyle \sum _ { k = 0 } ^ { p } \alpha _ { i k } z ^ { k }$ , and we verify that coefficients of all powers of $z$ up to $z ^ { p }$ agree in the two sides of (541a) and (541b). 
