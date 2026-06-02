# 135 The arithmetic-geometric mean

Let $a _ { 0 }$ and $b _ { 0 }$ be real numbers chosen so that $0 < b _ { 0 } < a _ { 0 }$ , and define the sequence of $( a _ { n } , b _ { n } )$ pairs by the formulae

$$
\begin{array} { l c r } { { a _ { n } = \frac { 1 } { 2 } ( a _ { n - 1 } + b _ { n - 1 } ) , } } & { { } } & { { n = 1 , 2 , \ldots . . . } } \\ { { b _ { n } = \sqrt { a _ { n - 1 } b _ { n - 1 } } , } } & { { } } & { { } } \end{array}
$$

We can verify (i) that $b _ { n - 1 } < b _ { n } < a _ { n } < a _ { n - 1 }$ for all $n \geq 1$ and (ii) that the sequence $a _ { 0 } - b _ { 0 }$ , $a _ { 1 } - b _ { 1 }$ , $a _ { 2 } - b _ { 2 } , \dots$ converges to zero. The truth of (i) follows from elementary properties of arithmetic and geometric means. Furthermore, (ii) can be proved from the identity

$$
a _ { n } - b _ { n } = { \frac { ( a _ { n - 1 } - b _ { n - 1 } ) ^ { 2 } } { 2 { \bigl ( } { \sqrt { a _ { n - 1 } } } + { \sqrt { b _ { n - 1 } } } { \bigr ) } ^ { 2 } } } .
$$

The common limit of the $a _ { n }$ and $b _ { n }$ sequences is known as the ‘arithmeticgeometric mean’ of $a _ { 0 }$ and $b _ { 0 }$ . We present a single application.

The quantities

$$
\begin{array} { l } { { F ( a , b ) = \displaystyle \int _ { 0 } ^ { \pi / 2 } \left( a ^ { 2 } \cos ^ { 2 } ( \theta ) + b ^ { 2 } \sin ^ { 2 } ( \theta ) \right) ^ { - 1 / 2 } d \theta , } } \\ { { E ( a , b ) = \displaystyle \int _ { 0 } ^ { \pi / 2 } \left( a ^ { 2 } \cos ^ { 2 } ( \theta ) + b ^ { 2 } \sin ^ { 2 } ( \theta ) \right) ^ { 1 / 2 } d \theta , } } \end{array}
$$

are known as ‘complete elliptic integrals’ of the first and second kind, respectively. The value of $4 E ( a , b )$ is the length of the circumference of the ellipse

$$
{ \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } = 1 .
$$

Use $a _ { 0 } = a$ and $b _ { 0 } = b$ as starting values for the computation of the sequences defined by (135a), and denote by $a _ { \infty }$ the arithmetic-geometric mean of $a _ { 0 }$ and $b _ { 0 }$ . Then it can be shown that

$$
F ( a _ { 0 } , b _ { 0 } ) = F ( a _ { 1 } , b _ { 1 } ) ,
$$

and therefore that

$$
F ( a _ { 0 } , b _ { 0 } ) = F ( a _ { \infty } , a _ { \infty } ) = \frac { \pi } { 2 a _ { \infty } } .
$$

The value of $E ( a _ { 0 } , b _ { 0 } )$ can also be found from the sequences that lead to the arithmetic-geometric mean. In fact

$$
E ( a _ { 0 } , b _ { 0 } ) = \frac { \pi } { 2 a _ { \infty } } \left( a _ { 0 } ^ { 2 } - 2 a _ { 1 } ( a _ { 0 } - a _ { 1 } ) - 4 a _ { 2 } ( a _ { 1 } - a _ { 2 } ) - 8 a _ { 3 } ( a _ { 2 } - a _ { 3 } ) - \cdot \cdot \cdot \right) .
$$

# Exercises 13

13.1 Write the difference equation given by (134e) in the form

$$
z _ { n } = \phi ( z _ { n - 1 } ) ,
$$

with $z _ { 0 }$ a given initial value.

13.2 Write the difference equation system

$$
\begin{array} { r l r } { \boldsymbol { u } _ { n } = \boldsymbol { u } _ { n - 1 } + \boldsymbol { v } _ { n - 1 } , } & { { } } & { \boldsymbol { u } _ { 0 } = 2 , } \\ { \boldsymbol { v } _ { n } = 2 \boldsymbol { u } _ { n - 1 } + \boldsymbol { v } _ { n - 1 } ^ { 2 } , } & { { } } & { \boldsymbol { v } _ { 0 } = 1 , } \end{array}
$$

in the form $y _ { n } = \phi ( y _ { n - 1 } , y _ { n - 2 } )$ , with $y _ { 0 }$ and $y _ { 1 }$ given initial values.

13.3 Use the formula for the error in linear interpolation together with the solution to (133c) to verify the order of convergence of (134e).

13.4 Calculate $\sqrt { 2 }$ by applying the Newton method to the equation

$$
2 x ^ { - 2 } - 1 = 0 .
$$

13.5 Calculate the value of $\sqrt { 3 }$ by applying the secant method to

$$
x ^ { 2 } - 3 = 0 .
$$

13.6 Calculate the circumference of the ellipse

$$
{ \frac { x ^ { 2 } } { 9 } } + { \frac { y ^ { 2 } } { 4 } } = 1 ,
$$

using the arithmetic-geometric mean.
