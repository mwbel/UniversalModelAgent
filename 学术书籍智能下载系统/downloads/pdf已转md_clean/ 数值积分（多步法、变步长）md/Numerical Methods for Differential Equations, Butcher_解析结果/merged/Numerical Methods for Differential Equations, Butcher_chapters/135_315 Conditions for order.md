# 315 Conditions for order

Now that we have expressions for the Taylor expansions of the exact solution, and also of the computed solution, we have all we need to find conditions for order. If the exact solution has Taylor series given by (311d) and the approximate solution has Taylor series given by (313e), then we need only compare these term by term to arrive at the principal result on the order of Runge–Kutta methods.

Theorem 315A A Runge–Kutta method with elementary weights

$$
\Phi : T  \mathbb { R } ,
$$

has order $p$ if and only if

$$
\Phi ( t ) = { \frac { 1 } { \gamma ( t ) } } , { \mathrm { ~ } } f o r { \mathrm { ~ } } a l l \ t \in T { \mathrm { ~ } } s u c h { \mathrm { ~ } } t h a t r ( t ) \leq p .
$$

Proof. The coefficient of $F ( t ) ( y _ { 0 } ) h ^ { r ( t ) }$ in (313e) is $\begin{array} { r } { \frac { 1 } { \sigma ( t ) } \Phi ( t ) } \end{array}$ , compared with the coefficient in (311d), which is $\frac { 1 } { \sigma ( t ) \gamma ( t ) }$ . Equate these coefficients and we obtain (315a). $\boxed { \begin{array} { r l } \end{array} }$
