# 504 Some known unconventional methods

Amongst the methods that do not fit under the conventional Runge–Kutta or linear multistep headings, we consider the cyclic composite methods of Donelson and Hansen (1971), the pseudo Runge–Kutta methods of Byrne and Lambert (1966) and the hybrid methods of Gragg and Stetter (1964), Butcher (1965) and Gear (1965). We illustrate, by examples, how methods of these types can be cast in general linear form.

To overcome the limitations of linear multistep methods imposed by the conflicting demands of order and stability, Donelson and Hansen proposed a procedure in which two or more linear multistep methods are used in rotation over successive steps. Write the constituent methods as $( \alpha ^ { ( 1 ) } , \beta ^ { ( 1 ) } )$ , $( \alpha ^ { ( 2 ) } , \beta ^ { ( 2 ) } ) , . .$ . , $( \alpha ^ { ( m ) } , \beta ^ { ( m ) } )$ , so that the formula for computing $y _ { n }$ will be

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } ^ { ( j ) } y _ { n - i } + \sum _ { i = 0 } ^ { k } \beta _ { i } ^ { ( j ) } h f ( x _ { n - i } , y _ { n - i } ) ,
$$

where $j \in \{ 1 , 2 , \dots , m \}$ is chosen so that $n - j$ is a multiple of $m$ .

The step value $-$ that is the maximum of the degrees of $\alpha ^ { ( j ) }$ and $\beta ^ { ( j ) } \textrm { - }$ may vary amongst the $m$ constituent methods, but they can be assumed to have a common value $k$ equal to the maximum over all the basic methods. We illustrate these ideas in the case $k = 3$ , $m = 2$ . As a consequence of the Dahlquist barrier, order $p = 5$ with $k = 3$ is inconsistent with stability and therefore convergence. Consider the following two linear multistep methods:

$$
\begin{array} { r l } & { [ \alpha ^ { ( 1 ) } ( z ) , \beta ^ { ( 1 ) } ( z ) ] = [ 1 + \frac { 8 } { 1 1 } z - \frac { 1 9 } { 1 1 } z ^ { 2 } , \frac { 1 0 } { 3 3 } + \frac { 1 9 } { 1 1 } z + \frac { 8 } { 1 1 } z ^ { 2 } - \frac { 1 } { 3 3 } z ^ { 3 } ] , } \\ & { [ \alpha ^ { ( 2 ) } ( z ) , \beta ^ { ( 2 ) } ( z ) ] = [ 1 - \frac { 4 4 9 } { 2 4 0 } z - \frac { 1 9 } { 3 0 } z ^ { 2 } + \frac { 3 6 1 } { 2 4 0 } z ^ { 3 } , \frac { 2 5 1 } { 7 2 0 } + \frac { 1 9 } { 3 0 } z - \frac { 4 4 9 } { 2 4 0 } z ^ { 2 } - \frac { 3 5 } { 7 2 } z ^ { 3 } ] . } \end{array}
$$

Each of these has order 5 and is, of course, unstable. To combine them, used alternately, into a single step of a general linear method, it is convenient to regard $h$ as the stepsize for the complete cycle of two steps. We denote the incoming approximations as $y _ { n - 3 / 2 }$ , $y _ { n - 1 }$ , $h f _ { n - 2 }$ , $h f _ { n - 3 / 2 }$ and $h f _ { n - 1 } .$ The first half-step, relating $y _ { n - 1 / 2 }$ and $h f _ { n - 1 / 2 }$ to the input quantities, gives

$$
\begin{array} { r } { y _ { n - \frac { 1 } { 2 } } = \frac { 5 } { 3 3 } h f _ { n - \frac { 1 } { 2 } } + \frac { 1 9 } { 1 1 } y _ { n - \frac { 3 } { 2 } } - \frac { 8 } { 1 1 } y _ { n - 1 } - \frac { 1 } { 6 6 } h f _ { n - 2 } + \frac { 4 } { 1 1 } h f _ { n - \frac { 3 } { 2 } } + \frac { 1 9 } { 2 2 } h f _ { n - 1 } . } \end{array}
$$

Substitute this into the corresponding formula for $y _ { n }$ and we find

$$
\begin{array} { r } { y _ { n } = \frac { 4 7 5 3 } { 7 9 2 0 } h f _ { n - \frac { 1 } { 2 } } + \frac { 2 5 1 } { 1 4 4 0 } h f _ { n } + \frac { 1 9 } { 1 1 } y _ { n - \frac { 3 } { 2 } } - \frac { 8 } { 1 1 } y _ { n - 1 } \qquad } \\ { - \frac { 4 4 9 } { 1 5 8 4 0 } h f _ { n - 2 } + \frac { 3 4 6 3 } { 7 9 2 0 } h f _ { n - \frac { 3 } { 2 } } + \frac { 4 4 9 } { 6 6 0 } h f _ { n - 1 } . } \end{array}
$$

Translating these formulae into the $( A , U , B , V )$ formulation gives

$$
{ \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = { \left[ \begin{array} { l l l l l l l l } { { \frac { 5 } { 3 3 } } } & { 0 } & { 0 } & { { \frac { 1 9 } { 1 1 } } } & { - { \frac { 8 } { 1 1 } } } & { - { \frac { 1 } { 6 6 } } } & { { \frac { 4 } { 1 1 } } } & { { \frac { 1 9 } { 2 2 } } } \\ { { \frac { 4 7 9 5 3 } { 7 9 2 0 } } } & { { \frac { 2 5 1 } { 1 4 4 0 } } } & { { \frac { 1 9 } { 1 1 } } } & { - { \frac { 8 } { 1 1 } } } & { - { \frac { 4 4 9 } { 1 5 8 4 0 } } } & { { \frac { 3 4 6 3 } { 7 9 2 0 } } } & { { \frac { 4 4 9 } { 6 6 0 } } } \\ { { \frac { 5 } { 3 3 } } } & { 0 } & { { \frac { 1 9 } { 1 9 } } } & { - { \frac { 8 } { 1 1 } } } & { - { \frac { 1 } { 6 6 } } } & { { \frac { 1 } { 4 1 } } } & { { \frac { 1 9 } { 1 2 } } } \\ { { \frac { 4 7 5 3 } { 7 9 2 0 } } } & { { \frac { 2 5 1 } { 1 4 4 0 } } } & { { \frac { 1 9 } { 1 1 } } } & { - { \frac { 1 } { 1 1 } } } & { - { \frac { 4 4 9 } { 1 5 8 4 0 } } } & { { \frac { 3 4 6 3 } { 7 9 2 0 } } } & { { \frac { 4 4 9 } { 6 6 0 } } } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } .
$$

This formulation can be simplified, in the sense that $r$ can be reduced, and we have, for example, the following alternative coefficient matrices:

<table><tr><td rowspan="5">A U = B V</td><td>5 33 4753</td><td>0 251</td><td rowspan="5">1</td><td>1 66 449</td><td>4 1 3463</td><td>19 22 449</td></tr><tr><td>7920</td><td>1440</td><td>1 15840</td><td>7920</td><td>660</td></tr><tr><td>173 990</td><td>251 1980</td><td>1 1 180</td><td>307 990</td><td>329 330</td></tr><tr><td>0</td><td>0</td><td>0 0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Because of the natural way in which we have written this particular composite cyclic pair in general linear form, and then rewritten it, using equally simple operations, into a less recognizable form, an obvious question arises. The question is whether it might have been more appropriate to use the general linear formulation from the start, and then explore the existence of suitable methods that have no connection with linear multistep methods.

We now turn to pseudo Runge–Kutta methods. Consider the method given by (261a). Even though four input values are used in step $h F _ { 2 } ^ { [ n - 1 ] }$ and $h F _ { 3 } ^ { \lfloor n - 1 \rfloor }$ ), this can be effectively reduced to $n$ tw $( y _ { n - 1 } , h F _ { 1 } ^ { [ n - 1 ] }$ ecause, in , addition to $y _ { n - 1 }$ , only the combination $\begin{array} { r } { \frac { 1 } { 1 2 } h F _ { 1 } ^ { [ n - 1 ] } - \frac { 1 } { 3 } h F _ { 2 } ^ { [ n - 1 ] } - \frac { 1 } { 4 } h F _ { 3 } ^ { [ n - 1 ] } } \end{array}$ is actually used. This means that a quantity of this form, but with $n - 1$ replaced by $n$ , has to be computed in step $n$ for use in the following step. The $( 3 + 2 ) \times ( 3 + 2 )$ matrix representing this method is

$$
\left[ { \begin{array} { r r r r r r } { 0 } & { 0 } & { 0 } & { { \left| \begin{array} { l l } { 1 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { - { \frac { 1 } { 3 } } } & { { \frac { 4 } { 3 } } } & { 0 } \end{array} \right|}  } & { 1 } & { 0 } \\ { { \frac { 1 1 } { 1 2 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 4 } } } & { 1 } & { 1 } \\ { { \frac { 1 } { 1 2 } } } & { - { \frac { 1 } { 3 } } } & { - { \frac { 1 } { 4 } } } & { 0 } & { 0 } \end{array} } \right] .
$$

For a seventh order method taken from Butcher (1965), the solution at the end of the step is approximated using ‘predictors’ at $x _ { n } - { \textstyle { \frac { 1 } { 2 } } } h$ and at $x _ { n }$ , in preparation for a final ‘corrector’ value, also at $x _ { n }$ . The input quantities correspond to solution approximations y[n−1]1 ≈ y(xn 1), y[n−1]2 ≈ y(xn 2) and y[n−1]3 ≈ y(xn−3), and the corresponding scaled derivative approximations y[n−1] ≈ hy- (xn 1), y[n −1]5 ≈ hy- (xn 2) and y[n6 −1] ≈ hy- (xn 3). The general linear representation is

<table><tr><td>0 384</td><td>0</td><td>0</td><td>225 128</td><td>200 128</td><td>153 128 212</td><td>225 128 1395</td><td>300 128</td><td>45 128</td></tr><tr><td>155 2304</td><td>0 465</td><td>0</td><td>540 128 783</td><td>297 31 135</td><td>31 31</td><td>155 135</td><td>2130 155 495</td><td>309 155</td></tr><tr><td>3085</td><td>3085</td><td>0</td><td>617</td><td>617</td><td>617</td><td>3085</td><td>3085</td><td>39 3085</td></tr><tr><td>2304 3085</td><td>465 3085</td><td>0</td><td>783 617</td><td>135 617</td><td>31 617</td><td>135 3085</td><td>495 3085</td><td>39</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3085 0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td></td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>0</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr></table>
