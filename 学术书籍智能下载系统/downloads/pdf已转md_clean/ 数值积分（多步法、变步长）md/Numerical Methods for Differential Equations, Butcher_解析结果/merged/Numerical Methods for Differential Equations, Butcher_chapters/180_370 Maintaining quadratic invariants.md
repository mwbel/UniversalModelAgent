# 370 Maintaining quadratic invariants

We recall Definition 357B in which the matrix $M$ plays a role, where the elements of $M$ are

$$
\begin{array} { r } { m _ { i j } = b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } . } \end{array}
$$

Now consider a problem for which

$$
y ^ { \mathsf { T } } Q f ( y ) = 0 ,
$$

for all $y$ . It is assumed that $Q$ is a symmetric matrix so that (370b) is equivalent to the statement that $y ( x ) ^ { 1 } Q y ( x )$ is invariant.

We want to characterize Runge–Kutta methods with the property that $y _ { n } ^ { \mathsf { T } } Q y _ { n }$ is invariant with $n$ so that the the numerical solution preserves the conservation law possessed by the problem. If the input to step $1$ is $y _ { 0 }$ , then the output will be

$$
y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } , 
$$

where the stage derivatives are $F _ { i } = f ( Y _ { i } )$ , with

$$
Y _ { i } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } .
$$

From (370b) it follows that

$$
\boldsymbol { F } _ { i } ^ { \intercal } \boldsymbol { Q y _ { 0 } } = - h \sum _ { j = 1 } ^ { s } a _ { i j } \boldsymbol { F } _ { i } ^ { \intercal } \boldsymbol { Q F } _ { j } .
$$

Use (370c) to calculate $y _ { 1 } ^ { \mathsf { T } } Q y _ { 1 }$ and substitute from (370d) to obtain the result

$$
y _ { 1 } ^ { \mathsf { T } } Q y _ { 1 } = y _ { 0 } ^ { \mathsf { T } } Q y _ { 0 } - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } m _ { i j } F _ { i } ^ { \mathsf { T } } Q F _ { j } ,
$$

with $m _ { i j }$ given by (370a).

Thus $M ~ = ~ 0$ implies that quadratic invariants are preserved and, in particular, that symplectic behaviour is maintained. Accordingly, we have the following definition:

Definition 370A A Runge–Kutta method $( A , b ^ { \prime } , c )$ is symplectic if

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top }
$$

is the zero matrix.

The property expressed by Definition 370A was first found by Cooper (1987) and, as a characteristic of symplectic methods, by Lasagni (1988), Sanz-Serna (1988) and Suris (1988).
