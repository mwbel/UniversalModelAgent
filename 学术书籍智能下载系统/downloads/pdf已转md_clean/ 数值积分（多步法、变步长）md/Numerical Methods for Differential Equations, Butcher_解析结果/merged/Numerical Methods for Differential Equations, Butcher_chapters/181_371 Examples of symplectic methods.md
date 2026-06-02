# 371 Examples of symplectic methods

A method with a single stage is symplectic only if $2 b _ { 1 } a _ { 1 1 } - b _ { 1 } ^ { 2 } = 0$ . For consistency, that is order at least $^ { 1 }$ , $b _ { 1 } = 1$ and hence $\begin{array} { r } { c _ { 1 } = a _ { 1 1 } = \frac { 1 } { 2 } } \end{array}$ ; this is just the implicit mid-point rule. We can extend this in two ways: by either looking at methods where $A$ is lower triangular or looking at the methods with stage order $s$ .

For lower triangular methods we will assume that none of the $b _ { i }$ is zero. The diagonals can be found from $2 b _ { i } a _ { i i } = b _ { i } ^ { 2 }$ to be $\begin{array} { r } { a _ { i i } = \frac { 1 } { 2 } b _ { i } } \end{array}$ . For the elements of $A$ below the diagonal we have $b _ { i } a _ { i j } = b _ { i } b _ { j }$ so that $a _ { i j } = b _ { j }$ . This gives a tableau

$$
 \begin{array} { r l } { { \frac { 1 } { 2 } } b _ { 1 } } & { { | \begin{array} { l } { { \frac { 1 } { 2 } } b _ { 1 } } \\ { b _ { 1 } + { \frac { 1 } { 2 } } b _ { 2 } } \end{array}  } } &  { | \begin{array} { l l l l l } { { \frac { 1 } { 2 } } b _ { 1 } } & { } & { } & { } & { } \\ { b _ { 1 } } & { { \frac { 1 } { 2 } } b _ { 2 } } & { } & { } & { } \\ { b _ { 1 } } & { b _ { 2 } } & { { \frac { 1 } { 2 } } b _ { 3 } } & { } & { } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { } \\ { b _ { 1 } + \cdot \cdot + b _ { s - 1 } + { \frac { 1 } { 2 } } b _ { s } } & { { | \begin{array} { l l l l l l } { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { \cdot \cdot } & { { \frac { 1 } { 2 } } b _ { s } } \\ { b _ { 1 } } & { b _ { 2 } } & { b _ { 3 } } & { \cdot \cdot } & { b _ { s } } \end{array}  } } \end{array} } \end{array}
$$

This method is identical with $s$ steps of the mid-point rule with stepsizes $b _ { 1 } h$ , $b _ { 2 } h$ , $\cdot \cdot \cdot$ , $b _ { s } h$ .

For methods with order and stage order equal to $s$ , we have, in the notation of Subsection 358, $\epsilon _ { i } = 0$ for $i = s + 1$ , $s + 2$ , $\cdot \cdot \cdot$ , $2 s$ . This follows from the observation that $V ^ { \ I } M V = 0$ . Thus, in addition to $B ( s )$ , $B ( 2 s )$ holds. Hence, the abscissae of the method are the zeros of $P _ { s } ^ { * }$ and the method is the $s$ -stage Gauss method.
