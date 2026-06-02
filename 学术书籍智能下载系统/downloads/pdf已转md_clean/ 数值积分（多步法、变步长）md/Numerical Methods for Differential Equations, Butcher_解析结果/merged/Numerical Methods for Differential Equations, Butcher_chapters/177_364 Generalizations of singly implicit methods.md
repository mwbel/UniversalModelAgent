# 364 Generalizations of singly implicit methods

In an attempt to improve the performance of existing singly implicit methods, Butcher and Cash (1990) considered the possibility of adding additional diagonally implicit stages. For example, if $s ~ = ~ p + 1$ is chosen, then the coefficient matrix has the form

$$
\begin{array} { r } { A = \left[ \begin{array} { c c } { \lambda \widehat { A } } & { 0 } \\ { b ^ { \top } } & { \lambda } \end{array} \right] , } \end{array}
$$

where $\widehat { A }$ is the matrix

$$
{ \widehat { A } } = T ( I - J ) T ^ { - 1 } .
$$

An appropriate choice of $\lambda$ is made by balancing various considerations. The first of these is good stability, and the second is a low error constant. Minor considerations would be convenience, the avoidance of coefficients with abnormally large magnitudes or with negative signs, where possible, and a preference for methods in which the $c _ { i }$ lie in $[ 0 , 1 ]$ . We illustrate these ideas for the case $p = 2$ and $s = 3$ , for which the general form for a method would be

<table><tr><td>入(2-√2) 入(2+√2)</td><td colspan="3">入(1-√2) 入(1+√②)</td><td>&gt;(1-√2) 入(1+1√②)</td><td>0 0</td></tr><tr><td rowspan="3">1</td><td>2+3√2_ λ(1+√2) 4</td><td>2 2 8</td><td>2-3√2_(1-√2) 4</td><td>3 2</td><td rowspan="3">入 入</td></tr><tr><td>2+3√2</td><td>入(1+√2)</td><td>2-3√2</td><td></td></tr><tr><td>4</td><td>2 2 8</td><td>4</td><td>入(1-√2) 点 + 2</td></tr></table>

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0005_pages_0281-0350/auto/images/c0b1581105a7e8352a8baf7e761a8469c17426adeb496aeaacbfbe83a5eded4e.jpg)  
Error constant $C ( \lambda )$ for $\lambda \in [ 0 . 1 , 0 . 5 ]$

The only choice available is the value of $\lambda$ , and we consider the consequence of making various choices for this number. The first criterion is that the method should be A-stable, and we analyse this by calculating the stability function

$$
R ( z ) = \frac { N ( z ) } { D ( z ) } = \frac { 1 + ( 1 - 3 \lambda ) z + ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } ) z ^ { 2 } } { ( 1 - \lambda z ) ^ { 3 } }
$$

and the E-polynomial

$$
\begin{array} { r } { E ( y ) = | D ( i y ) | ^ { 2 } - | N ( i y ) | ^ { 2 } = \Big ( 3 \lambda ^ { 4 } - \big ( \frac { 1 } { 2 } - 3 \lambda + 3 \lambda ^ { 2 } \big ) ^ { 2 } \Big ) y ^ { 4 } + \lambda ^ { 6 } y ^ { 6 } . } \end{array}
$$

For A-stability, the coefficient of $y ^ { 4 }$ must be non-negative. The condition for this is that

$$
\frac { 3 - { \sqrt { 3 + 2 { \sqrt { 3 } } } } } { 2 ( 3 - { \sqrt { 3 } } ) } \leq \lambda \leq \frac { 3 + { \sqrt { 3 + 2 { \sqrt { 3 } } } } } { 2 ( 3 - { \sqrt { 3 } } ) } ,
$$

or that $\lambda$ lies in the interval [0.180425, 2.185600]. The error constant $C ( \lambda )$ , defined by $\exp ( z ) - R ( z ) = C ( \lambda ) z ^ { 3 } + O ( z ^ { 4 } )$ , is found to be

$$
C ( \lambda ) = \frac { 1 } { 6 } - \frac { 3 } { 2 } \lambda + 3 \lambda ^ { 2 } - \lambda ^ { 3 } ,
$$

and takes on values for $\lambda \in [ 0 . 1 , 0 . 5 ]$ , as shown in Figure 364(i).

The value of $b _ { 1 }$ is positive for $\lambda > 0 . 1 2 5 4 4 1$ . Furthermore $b _ { 2 }$ is positive for $\lambda < 0 . 3 6 4 3 3 5$ . Since $b _ { 1 } + b _ { 2 } + \lambda = 1$ , we obtain moderately sized values of all components of $b ^ { \top }$ if $\lambda \in [ 0 . 1 2 5 4 4 1 , 0 . 3 6 4 3 3 5$ ]. The requirement that $c _ { 1 }$ and $c _ { 2 }$ lie in $( 0 , 1 )$ is satisfied if $\lambda < ( 2 - \sqrt { 2 } ) ^ { - 1 } \approx 0 . 2 9 2 8 9 3$ . Leaving aside the question of convenience, we should perhaps choose $\lambda \approx 0 . 1 8 0 4 2 5$ so that the error constant is small, the method is A-stable, and the other minor considerations are all satisfied. Convenience might suggest an alternative value $\textstyle \lambda = { \frac { 1 } { 5 } }$ .
