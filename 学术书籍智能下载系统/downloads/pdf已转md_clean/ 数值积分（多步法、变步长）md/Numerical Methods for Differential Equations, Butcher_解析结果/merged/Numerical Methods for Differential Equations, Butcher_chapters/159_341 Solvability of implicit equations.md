# 341 Solvability of implicit equations

As we have remarked, explicit evaluation of the stages is not, in general, possible for an implicit Runge–Kutta method. However, under mild assumptions on the smoothness of the function $f$ it is easy to see that, for sufficiently small $h$ , the values of $Y _ { 1 }$ , $Y _ { 2 }$ , $\cdot \cdot \cdot$ , $Y _ { s }$ , and hence the output from a step, exist and are unique. Suppose that $f$ satisfies a Lipschitz condition

$$
\| f ( \eta ) - f ( \overline { { \eta } } ) \| \leq L \| \eta - \overline { { \eta } } \|
$$

and consider the stages in a step with size $h$ from initial value $y _ { 0 }$ . We can identify the values of $Y _ { i }$ , $i = 1 , 2 , \dots , s$ , as comprising the components of a vector in $\mathbb { R } ^ { s N }$ which is a fixed point of the mapping

$$
Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] \mapsto \phi ( Y ) = \left[ \begin{array} { c } { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { 1 i } f ( Y _ { i } ) } \\ { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { 2 i } f ( Y _ { i } ) } \\ { \vdots } \\ { y _ { 0 } + h \sum _ { i = 1 } ^ { s } a _ { s i } f ( Y _ { i } ) } \end{array} \right] .
$$

Define a metric on $\mathbb { R } ^ { s N }$ by the formula

$$
\rho ( Y , \overline { { Y } } ) = \operatorname* { m a x } _ { i = 1 } ^ { s } \| Y _ { i } - \overline { { Y } } _ { i } \| ,
$$

and estimate $\rho ( \phi ( Y ) , \phi ( { \overline { { Y } } } ) )$ as follows:

$$
\begin{array} { r l } { \displaystyle \rho ( \phi ( Y ) , \phi ( \overline { { Y } } ) ) = \underset { i = 1 } { \overset { s } { \operatorname* { m a x } } } \parallel \underset { j = 1 } { \overset { s } { \sum } } h a _ { i j } \parallel f ( Y _ { j } ) - \overline { { f } } ( Y _ { j } ) \parallel } & { } \\ { \displaystyle \leq | h | \underset { i = 1 } { \overset { s } { \operatorname* { m a x } } } \sum _ { j = 1 } ^ { s } | a _ { i j } | L \| Y _ { j } - \overline { { Y } } _ { j } \| } & { } \\ { \displaystyle \leq | h | L \| A \| _ { \infty } \underset { j = 1 } { \overset { s } { \operatorname* { m a x } } } \| Y _ { j } - \overline { { Y } } _ { j } \| } & { } \\ { \displaystyle \leq | h | L \| A \| _ { \infty } \rho ( Y , \overline { { Y } } ) , } \end{array}
$$

so that the conditions for the contraction mapping principle are satisfied as long as

$$
| h | \leq ( L \| A \| _ { \infty } ) ^ { - 1 } .
$$

In practice, this result is of little value, because implicit Runge–Kutta methods are usually used only for stiff problems for which $L$ is typically unreasonably large. In this case it is usually more efficient to use some variant of the Newton method. We discuss this question further in Subsection 360.
