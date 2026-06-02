# 263 General linear methods

To obtain a general formulation of methods that possess the multivalue attributes of linear multistep methods, as well as the multistage attributes of Runge–Kutta methods, general linear methods were introduced by the present author (Butcher, 1966). However, the formulation we present, while formally different, is equivalent in terms of the range of methods it can represent, and was introduced in Burrage and Butcher (1980).

Suppose that $r$ quantities are passed from step to step. At the start of step $n$ , these will be denoted by $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ , $y _ { 2 } ^ { [ n - 1 ] }$ , . , y[n−1] r , and after the step is completed, thstep will be $y _ { 1 } ^ { [ n ] }$ or, $y _ { 2 } ^ { [ n ] }$ onding, . . . , $y _ { r } ^ { \lfloor n \rfloor }$ antities available for use in the subsequen. During the computation of the step, $s$ stage values $Y _ { 1 }$ , $Y _ { 2 }$ , $\cdot \cdot \cdot$ , $Y _ { s }$ are computed, along with the corresponding stage derivatives $F _ { 1 }$ , $F _ { 2 }$ , $\cdot \cdot \cdot$ , $F _ { s }$ . For convenience of notation, we can create supervectors containing either $r$ or $s$ subvectors as follows:

$$
\begin{array} { r } { y ^ { [ n - 1 ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n - 1 ] } } \\ { y _ { 2 } ^ { [ n - 1 ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n - 1 ] } } \end{array} \right] , \quad y ^ { [ n ] } = \left[ \begin{array} { c } { y _ { 1 } ^ { [ n ] } } \\ { y _ { 2 } ^ { [ n ] } } \\ { \vdots } \\ { y _ { r } ^ { [ n ] } } \end{array} \right] , \quad Y = \left[ \begin{array} { c } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] , \quad F = \left[ \begin{array} { c } { F _ { 1 } } \\ { F _ { 2 } } \\ { \vdots } \\ { F _ { s } } \end{array} \right] . } \end{array}
$$

Just as for Runge–Kutta methods, the stages are computed making use of linear combinations of the stage derivatives but, since there are now a collection of input approximations, further linear combinations are needed to express the dependence on this input information. Similarly, the output quantities depend linearly on both the stage derivatives and the input quantities. All in all, four matrices are required to express all the details of these computations, and we denote these by $A = [ a _ { i j } ] _ { s , s }$ , $U = \left[ u _ { i j } \right] _ { s , r }$ , $B = [ b _ { i j } ] _ { r , s }$ and $V = [ v _ { i j } ] _ { r , r }$ .

The formulae for the stage values and the output values are

$$
\begin{array} { r } { Y _ { i } = \displaystyle \sum _ { j = 1 } ^ { s } h a _ { i j } F _ { j } + \sum _ { j = 1 } ^ { r } u _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , s , } \\ { y _ { i } ^ { [ n ] } = \displaystyle \sum _ { j = 1 } ^ { s } h b _ { i j } F _ { j } + \sum _ { j = 1 } ^ { r } v _ { i j } y _ { j } ^ { [ n - 1 ] } , \quad i = 1 , 2 , \ldots , r , } \end{array}
$$

or, using Kronecker product notation for an $N$ -dimensional problem,

$$
\begin{array} { r } { Y = h ( A \otimes I _ { N } ) F + ( U \otimes I _ { N } ) y ^ { [ n - 1 ] } , } \\ { y ^ { [ n ] } = h ( B \otimes I _ { N } ) F + ( V \otimes I _ { N } ) y ^ { [ n - 1 ] } . } \end{array}
$$

We devote Chapter 5 to a detailed study of general linear methods but, for the present, we illustrate the all-encompassing nature of the methods included in this family by presenting a number of sample methods written in this terminology.

In each case, the coefficients of the general linear formulation are presented in the $( s + r ) \times ( s + r )$ partitioned matrix

$$
\textstyle \left[ { \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} } \right] .
$$

The Euler method and implicit Euler methods are, respectively,

$$
\left[ { \frac { 0 \left| 1 \right| } { 1 \left| 1 \right] } } \right] \quad { \mathrm { a n d } } \quad \left[ { \frac { 1 \left| 1 \right| } { 1 \left| 1 \right| } } \right] .
$$

The Runge–Kutta methods (232a) and (233f) and (235i) are, respectively,

$$
 { \begin{array} { c c } { \mathrm { ~ - } } & { 0 } & { 0 } \\ { \mathrm { ~ 1 } } & { 0 } & { 1 } \\ { \mathrm { ~ - } { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { | \begin{array} { c } { 1 } \\ { 1 } \\ { 1 } \end{array} ] } } \end{array} } \quad { \mathrm { a n d } } \quad [ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { \mathrm { ~ - } 1 } & { 2 } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} } |  \quad { \mathrm { a n d } } \quad [ { \begin{array} { c c c c } { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} } ] .
$$

The second order Adams–Bashforth and Adams–Moulton and PECE methods based on these are, respectively,

$$
[ \begin{array} { l l l } { 0 | 1 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { 0 | 1 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { 1 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} ] \quad \mathrm { a n d } \quad [ \frac { 1 } { \frac { 1 } { 2 } } | 1  1 ] \quad \mathrm { a n d } \quad [ \frac { 1 } { \frac { 1 } { 2 } } \begin{array} { l l l l } { 0 } & { 0 } & { | 1 } & { \frac { 3 } { 2 } } & { - \frac { 1 } { 2 } } \\ { \frac { 1 } { 2 } } & { 0 } & { | 1 } & { \frac { 1 } { 2 } } & { 0 } \\ { \frac { 1 } { 2 } } & { 0 } & { 1 } & { \frac { 1 } { 2 } } & { 0 } \\ { 0 } & { 1 } & { | 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } \end{array}  ] ,
$$

where for each of the Adams–Bashforth and PECE methods, the output quantities are approximations to $y ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } )$ and $h y ^ { \prime } ( x _ { n - 1 } )$ , respectively.

Finally, we re-present two methods derived in this section. The first is the pseudo Runge–Kutta method (261a), for which the general linear representation is

<table><tr><td rowspan=2 colspan=1>0    0  00  0</td><td rowspan=1 colspan=1>1  0    0      0</td></tr><tr><td rowspan=1 colspan=1>1  0    0      0</td></tr><tr><td rowspan=1 colspan=1> 0</td><td rowspan=1 colspan=1>1  0    0      0</td></tr><tr><td rowspan=1 colspan=1>12   1  4</td><td rowspan=1 colspan=1>1  1    1      412</td></tr><tr><td rowspan=1 colspan=1>1    0  0</td><td rowspan=1 colspan=1>0  0    0      0</td></tr><tr><td rowspan=1 colspan=1>0    1  0</td><td rowspan=1 colspan=1>0  0    0      0</td></tr><tr><td rowspan=1 colspan=1>0    0 1</td><td rowspan=1 colspan=1>0  0    0      0</td></tr></table>

The four output quantities for this method are the approximate solution found at the end of the step, together with $h$ multiplied by each of the three stage derivatives. The second of the two general linear methods, that do not fit into any of the classical families, is the method introduced in Subsection 262. Its general linear method coefficient matrix is

<table><tr><td>0 189 92 3375 5152</td><td>0 0 25</td><td>0 529 3375 0 152 25 0 1</td><td>3904 3375 127 25 0</td><td>4232 3375 419 100 19</td><td>1472 3375 1118 575 1</td></tr><tr><td>3375</td><td>168 25 0 168</td><td>1</td><td>0</td><td>96 19</td><td>552 1</td></tr><tr><td>5152 0</td><td>0 0</td><td>1</td><td>0</td><td>96 0</td><td>552</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td></td><td></td><td></td><td>0</td></tr><tr><td>0</td><td>0 0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>

For this method, the output quantities are given by $y _ { 1 } ^ { [ n ] } \approx y ( x _ { n } )$ , $y _ { 2 } ^ { [ n ] } \approx$ $y ( x _ { n - 1 } )$ , $y _ { 3 } ^ { [ n ] } \approx h y ^ { \prime } ( x _ { n } )$ and $y _ { 4 } ^ { \lfloor n \rfloor } \approx h y ^ { \prime } ( x _ { n - 1 } )$ .

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/8dff35cc11da4683e9c04024e751ac373f6803b26e372076b8e911de65602628.jpg)  
Comparison of Runge–Kutta with pseudo Runge–Kutta method
