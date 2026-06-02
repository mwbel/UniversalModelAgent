# 361 Diagonally implicit Runge–Kutta methods

Because of the excessive cost in evaluating the stages in a fully implicit Runge– Kutta method, we consider the so-called ‘diagonally implicit Runge–Kutta’ or DIRK methods (Alexander, 1977). For these methods, the coefficient matrix $A$ has a lower triangular structure with equal elements on the diagonal. Note that sometimes these methods are referred to as ‘singly diagonally implicit’ or SDIRK, with DIRK methods not necessarily having equal diagonals. Earlier names for methods in this general class are semi-implicit Runge–Kutta methods (Butcher, 1965)and semi-explicit (Nørsett, 1974).

The advantage of these methods is that the stages can be evaluated sequentially rather than as one great implicit system. We consider here the derivation of some low order members of this class with a brief analysis of their stability regions.

To obtain order 2 with two stages, consider the tableau

$$
\frac { \lambda } { \left| \begin{array} { c c c } { \lambda } & { 0 } & { } \\ { c _ { 2 } - \lambda } & { \lambda } & { } \\ { b _ { 1 } } & { b _ { 2 } } \end{array} \right. } .
$$

The order conditions are

$$
\begin{array} { r } { b _ { 1 } + b _ { 2 } = 1 , } \\ { b _ { 1 } \lambda + b _ { 2 } c _ { 2 } = \frac { 1 } { 2 } , } \end{array}
$$

with solution $\begin{array} { r } { b _ { 1 } = \frac { 2 c _ { 2 } - 1 } { 2 ( c _ { 2 } - \lambda ) } } \end{array}$ , $\begin{array} { r } { b _ { 2 } = \frac { 1 - 2 \lambda } { 2 ( c _ { 2 } - \lambda ) } } \end{array}$ . The method is A-stable if $\lambda \geq \frac { 1 } { 4 }$ and L-stable if $\lambda = 1 \pm \textstyle { \frac { 1 } { 2 } } { \sqrt { 2 } }$ . A particularly attractive choice is $c _ { 2 } = 1 , \lambda = 1 - { \textstyle \frac { 1 } { 2 } } \sqrt { 2 }$ , for which the tableau is

$$
\frac { 1 - \frac 1 2 \sqrt 2 } { 1 } \left| \begin{array} { c c } { 1 - \frac 1 2 \sqrt { 2 } } & { 0 } \\ { \frac 1 2 \sqrt { 2 } } & { 1 - \frac 1 2 \sqrt { 2 } } \\ { \frac 1 2 \sqrt { 2 } } & { 1 - \frac 1 2 \sqrt { 2 } } \end{array} \right. .
$$

For $s = p = 3$ , the stability function is given by

$$
R ( z ) = \frac { 1 + ( 1 - 3 \lambda ) z + ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } ) z ^ { 2 } + ( \frac { 1 } { 6 } - \frac { 3 } { 2 } \lambda + 3 \lambda ^ { 2 } - \lambda ^ { 3 } ) z ^ { 3 } } { ( 1 - \lambda z ) ^ { 3 } }
$$

and the E-polynomial is found to be

$$
\mathrm {  ~ \psi ~ } ( y ) = \biggl ( \frac { 1 } { 1 2 } - \lambda + 3 \lambda ^ { 2 } - 2 \lambda ^ { 3 } \biggr ) y ^ { 4 } + \biggl ( - \frac { 1 } { 3 6 } + \frac { \lambda } { 2 } - \frac { 1 3 \lambda ^ { 2 } } { 4 } + \frac { 2 8 \lambda ^ { 3 } } { 3 } - 1 2 \lambda ^ { 4 } + 6 \lambda ^ { 5 } \biggr ) y ^ { 6 } .
$$

For $E ( y ) \ge 0$ , for all $y > 0$ , it is necessary and sufficient for A-stability that $\lambda \in [ \textstyle { \frac { 1 } { 3 } } , \widetilde { \lambda } ]$ , where $\tilde { \lambda } \approx 1 . 0 6 8 5 7 9 0 2 1 3$ is a zero of the coefficient of $y ^ { 4 }$ in $E ( y )$ . For

L-stability there is only one possible choice in this interval: $\lambda \approx 0 . 4 3 5 8 6 6 5 2 1 5$ , a zero of the coefficient of $z ^ { 3 }$ in the numerator of $R ( z )$ . Assuming $\lambda$ is chosen as this value, a possible choice for the remaining coefficients is given by the tableau

<table><tr><td rowspan=1 colspan=1>入(1+λ)1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4（-6)²+16λ-1）(6λ²-20λ+5）λ</td></tr></table>
