# 365 Effective order and DESIRE methods

An alternative way of forcing singly implicit methods to be more appropriate for practical computation is to generalize the order conditions. This has to be done without lowering achievable accuracy, and the use of effective order is indicated. Effective order is discussed in a general setting in Subsection 389 but, for methods with high stage order, a simpler analysis is possible.

Suppose that the quantities passed from one step to the next are not necessarily intended to be highly accurate approximations to the exact solution, but rather to modified quantities related to the exact result by weighted Taylor series. For example, the input to step $_ { n }$ might be an approximation to

$$
y ( x _ { n - 1 } ) + \alpha _ { 1 } h y ^ { \prime } ( x _ { n - 1 } ) + \alpha _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + \cdot \cdot \cdot + \alpha _ { p } h ^ { p } y ^ { ( p ) } ( y _ { n - 1 } ) .
$$

We could regard a numerical method, which produces an output equal to

$$
y _ { n } = y ( x _ { n } ) + \alpha _ { 1 } h y ^ { \prime } ( x _ { n } ) + \alpha _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot + \alpha _ { p } h ^ { p } y ^ { ( p ) } ( y _ { n } ) + O ( h ^ { p + 1 } ) ,
$$

as a satisfactory alternative to a method of classical order $p$ .

We explore this idea through the example of the effective order generalization of the L-stable order 2 singly implicit method with the tableau (363g). For this method, the abscissae are necessarily equal to $3 - 2 { \sqrt { 2 } }$ and $^ { 1 }$ , which are quite satisfactory for computation. However, we consider other choices, because in the more complicated cases with $s = p > 2$ , at least one of the abscissae is outside the interval $[ 0 , 1 ]$ , for A-stability.

If the method is required to have only effective order 2, then we can assume that the incoming and outgoing approximations are equal to

$$
\begin{array} { c } { { y _ { n - 1 } = y ( x _ { n - 1 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { p + 1 } ) , } } \\ { { y _ { n } = y ( x _ { n } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { n } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { n } ) + O ( h ^ { p + 1 } ) , } } \end{array}
$$

respectively. Suppose that the stage values are required to satisfy

$$
Y _ { 1 } = y ( x _ { n - 1 } + h c _ { 1 } ) + O ( h ^ { 3 } ) , \qquad Y _ { 2 } = y ( x _ { n - 1 } + h c _ { 2 } ) + O ( h ^ { 3 } ) ,
$$

with corresponding approximations for the stage derivatives. In deriving the order conditions, it can be assumed, without loss of generality, that $n = 1$ . The order conditions for the two stages and for the output approximation $y _ { n } = y _ { 1 }$ are

$$
\begin{array} { r l } & { y ( x _ { 0 } + h c _ { 1 } ) = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h \alpha _ { 1 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h \alpha _ { 1 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) , } \\ & { y ( x _ { 0 } + h c _ { 2 } ) = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h a _ { 2 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h a _ { 2 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) , } \\ & { y ( x _ { 1 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 1 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 1 } ) } \\ & { \qquad = y ( x _ { 0 } ) + h \alpha _ { 1 } y ^ { \prime } ( x _ { 0 } ) + h ^ { 2 } \alpha _ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) } \\ & { \qquad + h b _ { 1 } y ^ { \prime } ( x _ { 0 } + h c _ { 1 } ) + h b _ { 2 } y ^ { \prime } ( x _ { 0 } + h c _ { 2 } ) + O ( h ^ { 3 } ) . } \end{array}
$$

These can be converted into algebraic relations on the various free parameters by expanding by Taylor series about $x _ { 0 }$ and equating coefficients of $h y ^ { \prime } ( x _ { 0 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } )$ . This gives the conditions

$$
\begin{array} { c } { { c _ { 1 } = \alpha _ { 1 } + a _ { 1 1 } + a _ { 1 2 } , } } \\ { { { } } } \\ { { { \frac { 1 } { 2 } c _ { 1 } ^ { 2 } = \alpha _ { 2 } + a _ { 1 1 } c _ { 1 } + a _ { 1 2 } c _ { 2 } , } } } \\ { { { } } } \\ { { c _ { 2 } = \alpha _ { 1 } + a _ { 2 1 } + a _ { 2 2 } , } } \\ { { { } } } \\ { { { \frac { 1 } { 2 } c _ { 2 } ^ { 2 } = \alpha _ { 2 } + a _ { 2 1 } c _ { 1 } + a _ { 2 2 } c _ { 2 } , } } } \\ { { { } } } \\ { { { 1 + \alpha _ { 1 } = \alpha _ { 1 } + b _ { 1 } + b _ { 2 } , } } } \\ { { { { \frac { 1 } { 2 } + \alpha _ { 1 } + \alpha _ { 2 } = \alpha _ { 2 } + b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } . } } } } \end{array}
$$

Because of the single-implicitness condition $\sigma ( A ) = \{ \lambda \}$ , we also have

$$
\begin{array} { r } { a _ { 1 1 } + a _ { 2 2 } = 2 \lambda , } \\ { a _ { 1 1 } a _ { 2 2 } - a _ { 2 1 } a _ { 1 2 } = \lambda ^ { 2 } . } \end{array}
$$

Assuming that $c _ { 1 }$ and $c _ { 2 }$ are distinct, a solution to these equations always exists, and it leads to the values

$$
\begin{array} { r } { \alpha _ { 1 } = \frac 1 2 ( c _ { 1 } + c _ { 2 } ) - 2 \lambda , \quad \alpha _ { 2 } = \frac 1 2 c _ { 1 } c _ { 2 } - \lambda ( c _ { 1 } + c _ { 2 } ) + \lambda ^ { 2 } , } \end{array}
$$

together with the tableau

$$
\frac { c _ { 1 } \ { \boxed { \begin{array} { r l r l } { { c _ { 2 } } } & { { - \frac { c _ { 2 } - c _ { 1 } } { 2 } + \lambda + \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } & & { \lambda - \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } \end{array} } } } { \frac { \lambda } { c _ { 2 } } } } & { \frac { c _ { 2 } - c _ { 1 } } { 2 } + \lambda - \frac { \lambda ^ { 2 } } { c _ { 2 } - c _ { 1 } } } { \frac { \lambda } { c _ { 2 } } + \frac { 2 \lambda - \frac { 1 } { 2 } } { c _ { 2 } - c _ { 1 } } }  &  .
$$

In the special case $c ^ { \mathsf { T } } = [ 0 , 1 ]$ , with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ for L-stability, we find $\begin{array} { r } { \alpha _ { 1 } = \sqrt { 2 } - \frac { 3 } { 2 } } \end{array}$ and $\alpha _ { 2 } = \textstyle { \frac { 1 } { 2 } } ( 1 - { \sqrt { 2 } } )$ and the tableau

$$
{ \frac { 1 \left| { \begin{array} { l l } { { \frac { 1 } { 2 } } } ( 4 - 3 { \sqrt { 2 } } ) } & { { \frac { 1 } { 2 } } ( { \sqrt { 2 } } - 1 ) } \\ { { \frac { 1 } { 2 } } ( 5 - 3 { \sqrt { 2 } } ) } & { { \frac { 1 } { 2 } } { \sqrt { 2 } } } \end{array} \right.}  } { 2 - { \sqrt { 2 } } }  ~ .
$$

Combine the effective order idea with the diagonal extensions introduced in Subsection 364, and we obtain ‘DESIRE’ methods (diagonally extended by the example with implicit Runge–Kutta methods using effective order). These are exemplified $p = 2$ , $s = 3$ and $\textstyle \lambda = { \frac { 1 } { 5 } }$ . For this method, $\alpha _ { 1 } = - \frac { 3 } { 2 0 }$ $\begin{array} { r } { \alpha _ { 2 } = \frac { 1 } { 4 0 0 } } \end{array}$ and the coefficient tableau is

<table><tr><td>0</td><td>31 200</td><td>1 200</td><td>0</td></tr><tr><td rowspan="4"></td><td>81</td><td>49</td><td>0</td></tr><tr><td>200</td><td>200</td><td></td></tr><tr><td>71</td><td>119</td><td></td></tr><tr><td>200</td><td>200</td><td>1</td></tr><tr><td rowspan="2"></td><td>103</td><td>119</td><td>14</td></tr><tr><td>250</td><td>250</td><td>125</td></tr></table>

# Exercises 36

36.1 Derive the tableau for the two-stage order 2 diagonally implicit method satisfying (361a), (361b) with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ and $c _ { 2 } = 3 \lambda$ .

36.2 Rewrite the method in Exercise 36.1 so that the value of $Y _ { 1 }$ in step $n$ is the input and the value of $Y _ { 1 }$ in step $n + 1$ is the output.

36.3 Show that the method derived in Exercise 36.2 has stage order 2.

36.4 Derive a diagonally implicit method with $s = p = 3$ and with $\lambda = c _ { 2 } =$ $\textstyle { \frac { 1 } { 3 } }$ , $\begin{array} { r } { c _ { 2 } = \frac { 2 } { 3 } } \end{array}$ , $c _ { 3 } = 1$ .

36.5 Derive a diagonally implicit method with $s = p = 3$ , $\lambda = 1$ , $c _ { 2 } = { \textstyle { \frac { 1 } { 3 } } }$ , $c _ { 3 } = 1$ , $b _ { 1 } = 0$ .

36.6 Show that for an L-stable method of the type described in Subsection 364 with $p = 3$ , $s = 4$ , the minimum possible value of $\lambda$ is approximately 0.2278955169, a zero of the polynomial

$1 8 5 9 7 6 \lambda ^ { 1 2 } - 1 4 9 0 4 0 0 \lambda ^ { 1 1 } + 4 6 0 1 4 4 8 \lambda ^ { 1 0 } - 7 2 5 7 1 6 8 \lambda ^ { 9 } + 6 8 4 2 8 5 3 \lambda ^ { 8 }$ $- 4 1 8 1 7 6 0 \lambda ^ { 7 } + 1 7 2 4 2 5 6 \lambda ^ { 6 } - 4 8 7 2 9 6 \lambda ^ { 5 } + 9 4 1 7 6 \lambda ^ { 4 } - 1 2 1 9 2 \lambda ^ { 3 } + 1 0 0 8 \lambda ^ { 2 } - 4 8 \lambda + 1 . 0 0 0 9 4 1 6 \lambda ^ { 5 }$ .
