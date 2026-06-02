# 551 Inherent Runge–Kutta stability

In this subsection we discuss a special type of general linear method based on several assumptions on the form of the method. The original formulation for stiff methods was given in Butcher (2001) and for non-stiff methods in Wright (2002). In Butcher and Wright (2003) it was shown how these ans¨atze are interrelated and this led to the current formulation in Butcher and Wright (2003a).

Besides making use of doubly companion matrices, we also use the special $r \times r$ matrix $J$ and its transpose $K$ , where

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right] .
$$

For the special type of inherently RK stable general linear method we consider, $A$ has the diagonally implicit form

$$
A = \left[ \begin{array} { c c c c c } { { \lambda } } & { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { \lambda } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { \lambda } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { a _ { s 1 } } } & { { a _ { s 2 } } } & { { a _ { s 3 } } } & { { \cdots } } & { { \lambda } } \end{array} \right] ,
$$

with $\lambda \geq 0$ , and $V$ has the form

$$
V = \left[ \begin{array} { l l } { 1 } & { v ^ { \textsf { T } } } \\ { 0 } & { \dot { V } } \end{array} \right] ,
$$

where $\rho ( \dot { V } ) = 0$ , with $\rho$ denoting spectral radius. We assume that $p = q$ and that $s = r = p + 1$ . In some special cases, the last columns of $U$ and $V$ will vanish, thus making it possible for $r$ to be reduced to $r = p$ .

Definition 551A A general linear method $( A , U , B , V )$ is ‘inherently Runge– Kutta stable’ if $V$ is of the form (551a) and the two matrices

$$
B A - X B \qquad a n d \qquad B U - X V + V X
$$

are zero except for their first rows, where $X$ is some matrix.

The significance of this definition is expressed in the following.

Theorem 551B Let $( A , U , B , V )$ denote an inherently RK stable general linear method. Then the stability matrix

$$
M ( z ) = V + z B ( I - z A ) ^ { - 1 } U
$$

has only a single non-zero eigenvalue.

Proof. Calculate the matrix

$$
( I - z X ) M ( z ) ( I - z X ) ^ { - 1 } ,
$$

which has the same eigenvalues as $M ( z )$ . We use the notation $=$ to denote equality of two matrices, except for the first rows. Because $B A \equiv X B$ and $B U \equiv X V - V X$ , it follows that

$$
\begin{array} { l } { { ( I - z X ) B \equiv B ( I - z A ) , } } \\ { { ( I - z X ) V \equiv V ( I - z X ) - z B U , } } \end{array}
$$

so that

$$
( I - z X ) M ( z ) \equiv V ( I - z X ) .
$$

Hence $( I - z X ) M ( z ) ( I - z X ) ^ { - 1 }$ is identical to $V$ , except for the first row. Thus the eigenvalues of this matrix are its $( 1 , 1 )$ element together with the $p$ zero eigenvalues of $\dot { V }$ . 

Since we are adopting, as standard $r = p + 1$ and a stage order $q = p$ , it is possible to insist that the vector-valued function of $z$ , representing the input approximations, comprises a full basis for polynomials of degree $p$ . Thus, we will introduce the function $Z$ given by

$$
Z = \left[ \begin{array} { c } { { 1 } } \\ { { z } } \\ { { z ^ { 2 } } } \\ { { \vdots } } \\ { { z ^ { p } } } \end{array} \right] ,
$$

which represents the input vector

$$
y ^ { [ n - 1 ] } = \left[ \begin{array} { c } { y ( x _ { n - 1 } ) } \\ { h y ^ { \prime } ( x _ { n - 1 } ) } \\ { h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) } \\ { \vdots } \\ { h ^ { p } y ^ { ( p ) } ( x _ { n - 1 } ) } \end{array} \right] .
$$

This is identical, except for a simple rescaling by factorials, to the Nordsieck vector representation of input and output approximations, and it will be convenient to adopt this as standard.

Assuming that this standard choice is adopted, the order conditions are

$$
\begin{array} { r } { \exp ( c z ) = z A \exp ( c z ) + U Z + O ( z ^ { p + 1 } ) , } \\ { \exp ( z ) Z = z B \exp ( c z ) + V Z + O ( z ^ { p + 1 } ) . } \end{array}
$$

This result, and generalizations of it, make it possible to derive stiff methods of quite high orders. Furthermore, Wright (2003) has shown how it is possible to derive explicit methods suitable for non-stiff problems which satisfy the same requirements. Following some more details of the derivation of these methods, some example methods will be given.
