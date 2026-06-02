# 318 Local truncation error

The conditions for order give guarantees that the Taylor expansions of the exact and computed solutions agree up to terms in $h ^ { p }$ . Obtaining an understanding of the respective terms in $h ^ { p + 1 }$ is regarded as a key to deriving methods that not only have a specific order, but also have a small truncation error. Because the number of terms of this order rises rapidly as $p$ increases, it is extremely difficult to know how this sort of optimality should be arrived at. Picking out just the terms of order $p + 1$ , we can write the local truncation error in a single step as

$$
h ^ { p + 1 } \sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) } \left( \frac { 1 } { \gamma ( t ) } - \Phi ( t ) \right) F ( t ) ( y _ { 0 } ) + O ( h ^ { p + 2 } ) .
$$

Since we are interested in asymptotic behaviour, that is, limiting behaviour for $h$ small, we do not devote much attention to the term $O ( h ^ { p + 2 } )$ . The coefficient of $h ^ { p + 1 }$ in (318a) is bounded in magnitude by

$$
\sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot \| F ( t ) ( y _ { 0 } ) \| ,
$$

and this should somehow be made small. There is simply no general rule interrelating the magnitudes of the various elementary differentials, and some assumptions need to be made.

expression fo The first approach that can be considered is to compare, term by term, the r 1(p+1)! y(p+1)(x0), which is proportional to the local truncation error coefficient for linear multistep methods or for implicit Runge–Kutta methods of collocation type. The coefficient in this expression, corresponding to $t$ , is

$$
{ \frac { 1 } { \sigma ( t ) \gamma ( t ) } } ,
$$

so that the corresponding multiplier to yield the corresponding term in (318b) is

$$
| \gamma ( t ) \Phi ( t ) - 1 | .
$$

Hence, we can bound (318b) by

$$
\operatorname* { m a x } _ { r ( t ) = p + 1 } | \gamma ( t ) \Phi ( t ) - 1 | \sum _ { r ( t ) = p + 1 } \frac { 1 } { \sigma ( t ) \gamma ( t ) } \cdot \| F ( t ) ( y _ { 0 } ) \|
$$

and hence, it might be desirable to minimize

$$
\operatorname* { m a x } _ { r ( t ) = p + 1 } | \gamma ( t ) \Phi ( t ) - 1 |
$$

in seeking an efficient method.

Another approach would be to assume a bound $M$ on $\| f \|$ , a bound $L$ on the linear operator $\| f ^ { \prime } \|$ , and further bounds to make up the sequence

$$
\begin{array} { r l } & { \| f \| \leq M , } \\ & { \| f ^ { \prime \prime } \| \leq L , } \\ & { \| f ^ { \prime \prime } \| \leq \frac { L ^ { 2 } } { M } , } \\ & { \| f ^ { \prime \prime \prime } \| \leq \frac { L ^ { 3 } } { M ^ { 2 } } , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad  \end{array}
$$

This will mean that for any tree of order $p + 1$ , $\| F ( t ) ( y _ { 0 } ) \| \le L ^ { p } M$ and that

$$
\sum _ { \substack { \cdot ( t ) = p + 1 } } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot \| F ( t ) ( y _ { 0 } ) \| \leq \sum _ { \substack { r ( t ) = p + 1 } } \frac { 1 } { \sigma ( t ) } \left| \Phi ( t ) - \frac { 1 } { \gamma ( t ) } \right| \cdot L ^ { p } M .
$$

In studying the behaviour of a particular method of order $p$ when used to solve a particular initial value problem, we wish to assume that the local truncation error is bounded asymptotically by some constant multiplied by $h ^ { p + 1 }$ . This assumption will hinge on smoothness of the solution and the differentiability, sufficiently many times, of $f$ .
