# 331 Richardson error estimates

Richardson extrapolation consists of calculating a result in a manner that depends on a small parameter, and for which the error in the calculation varies systematically as the parameter varies. By using a sequence of values of the parameter, much of the effect of the errors can be eliminated so that improved accuracy results. In numerical quadrature, for example, the method of Romberg (1955) is based on calculating an integral $\begin{array} { r } { I = \int _ { a } ^ { b } \phi ( x ) d x } \end{array}$ using the trapezoidal rule with a stepsize $h$ equal to an integer divisor of $b - a$ . For a single choice of $h$ , the result computed can be expanded by an asymptotic formula of the form

$$
T ( h ) = I + C _ { 1 } h ^ { 2 } + C _ { 2 } h ^ { 4 } + \cdot \cdot \cdot ,
$$

so that, using a sequence $\begin{array} { l l l } { { h } } & { { = } } & { { H , 2 ^ { - 1 } H , 2 ^ { - 2 } H , . . . . } } \end{array}$ , we arrive at the approximations $T _ { 0 } = T ( H )$ , $T _ { 1 } = T ( \textstyle { \frac { 1 } { 2 } } H )$ , $T _ { 2 } = T ( \textstyle { \frac { 1 } { 4 } } H ) _ { ; }$ . . . with expansions

$$
\begin{array} { c } { { T _ { 0 } = I + C _ { 1 } H ^ { 2 } + C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { T _ { 1 } = I + \frac { 1 } { 4 } C _ { 1 } H ^ { 2 } + \frac { 1 } { 1 6 } C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { T _ { 2 } = I + \frac { 1 } { 1 6 } C _ { 1 } H ^ { 2 } + \frac { 1 } { 2 5 6 } C _ { 2 } H ^ { 4 } + \cdots , } } \\ { { { } } } \\ { { \vdots } } \\ { { { } } } \end{array}
$$

By forming

$$
\begin{array} { l } { { \displaystyle T _ { 0 1 } = \frac { 4 } { 3 } T _ { 1 } - \frac { 1 } { 3 } T _ { 0 } } , } \\ { ~ } \\ { { \displaystyle T _ { 1 2 } = \frac { 4 } { 3 } T _ { 2 } - \frac { 1 } { 3 } T _ { 1 } } , } \\ { ~ } \\ { { \displaystyle \quad \vdots \qquad } } \end{array}
$$

we obtain an ‘improved’ sequence in which the $C _ { 1 } H ^ { 2 }$ terms are eliminated from the asymptotic expansions so that convergence towards the exact result $I$ is more rapid as terms in the sequence are calculated. Similarly, a second sequence of improved approximations can be found from

$$
\begin{array} { l } { { \displaystyle T _ { 0 1 2 } = \frac { 1 6 } { 1 5 } T _ { 1 2 } - \frac { 1 } { 1 5 } T _ { 0 1 } } , } \\ { { \displaystyle T _ { 1 2 3 } = \frac { 1 6 } { 1 5 } T _ { 2 3 } - \frac { 1 } { 1 5 } T _ { 1 2 } } , } \\ { { \displaystyle \quad \quad \quad \quad \quad \vdots } } \end{array}
$$

This idea has an application to Runge–Kutta methods for ordinary differential equations on the small scale of a single step, repeated with two steps and half the original value of $h$ . Let $y _ { n - 1 }$ denote an incoming approximation for $y ( x _ { n - 1 } )$ and $y _ { n }$ the solution computed as an approximation to $y ( x _ { n } ) = y ( x _ { n - 1 } + h )$ using a Runge–Kutta method with tableau

$$
\begin{array} { r } { \left. \begin{array} { c } { 0 } \\ { c _ { 2 } } \\ { c _ { 3 } } \\ { \vdots } \\ { c _ { s } } \end{array} \right| \overset { \phantom { = } } \longrightarrow \left| \begin{array} { c c c c c } { 0 } \\ { a _ { 2 1 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } \\ { \vdots } & { \vdots } & { \ddots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \ddots } & { a _ { s , s - 1 } } \\ { b _ { 1 } } & { b _ { 2 } } & { \ddots } & { b _ { s - 1 } } & { b _ { s } } \end{array} \right. . } \end{array}
$$

Repeating the calculation with $h$ replaced by ${ \frac { 1 } { 2 } } h$ but carrying out two steps, rather than only one, is equivalent to taking a single step with the original $h$ , but using the tableau

$$
\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & { } { } & \end{array}
$$

Denote the result computed by this $2 s$ -stage method by ${ \hat { y } } _ { n }$ , and note that if the local truncation error in $y _ { n }$ is $C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } )$ , so that

$$
y _ { n } = y ( x _ { n } ) - C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

then

$$
\widehat { y } _ { n } = y ( x _ { n } ) - 2 ^ { - p } C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

because the error in computing ${ \hat { y } } _ { n }$ is $2 ^ { - p - 1 } C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } )$ contributed from each of two steps.

From the difference of (331a) and (331b) we find

$$
\widehat { y } _ { n } - y _ { n } = ( 1 - 2 ^ { - p } ) C ( x _ { n } ) h ^ { p + 1 } + O ( h ^ { p + 2 } ) ,
$$

so that the local truncation error in $y _ { n }$ can be approximated by

$$
( 1 - 2 ^ { - p } ) ^ { - 1 } ( { \widehat { y } } _ { n } - y _ { n } ) .
$$

This seems like an expensive way of computing the error in the result computed using an $s$ -stage method, because the additional computations required for the estimation take twice as long as the result itself. However, the additional cost becomes more reasonable when we realize that it is not $y _ { n }$ but ${ \widehat { y } } _ { n }$ that should be propagated. The additional cost on this basis is something like $5 0 \%$ . Actually, it is slightly less than this because the calculation of the derivative of $y _ { n - 1 }$ is shared by each of the two methods, and needs to be carried out only once.
