# 261 Pseudo Runge–Kutta methods

The paper by Byrne and Lambert suggests a generalization of Runge– Kutta methods in which stage derivatives computed in earlier steps are used alongside stage derivatives found in the current step, to compute the output value in the step. The stages themselves are evaluated in exactly the same way as for a Runge–Kutta method. We consider the case where the derivatives found only in the immediately previous step are used. Denote these by $F _ { i } ^ { [ n - 1 ] }$ , $i = 1 , 2 , \dots , s$ , so that the derivatives evaluated in the current step, $n$ , are $F _ { i } ^ { \left[ n \right] }$ , $i = 1 , 2 , \dots , s$ .

The defining equations for a single step of the method will now be

$$
\begin{array} { c } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } ^ { [ n ] } , } } \\ { { \displaystyle F _ { i } ^ { [ n ] } = f ( x _ { n - 1 } + h c _ { i } , Y _ { i } ) , } } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + h \left( \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } ^ { [ n ] } + \sum _ { i = 1 } ^ { s } \overline { { { b } } } _ { i } F _ { i } ^ { [ n - 1 ] } \right) . } } \end{array}
$$

We consider a single example of a pseudo Runge–Kutta method in which there are $s = 3$ stages and the order is $p = 4$ . The coefficients are given by the tableau

<table><tr><td rowspan=1 colspan=1>011</td><td rowspan=1 colspan=1>1      4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>11      112</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1      1       1124</td></tr></table>

where the additional vector contains the $\overline { { b ^ { \intercal } } }$ components.

Characteristic handicaps with this sort of method are starting and changing stepsize. Starting in this case can be accomplished by taking the first step with the classical Runge–Kutta method but inserting an additional stage $Y _ { 5 }$ , with the role of Y (1)3 , to provide, along with $Y _ { 2 } ^ { ( 2 ) } = Y _ { 2 }$ , the derivatives in step 1 required to complete step 2. Thus the starting step is based on the Runge– Kutta method

<table><tr><td rowspan=1 colspan=1>1</td><td></td></tr><tr><td rowspan=1 colspan=1>1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1    1  1  1  0</td></tr></table>

These methods, known also as hybrid methods or modified linear multistep methods, generalize linear multistep methods, interpreted as predictor– corrector pairs, by inserting one or more additional predictors, typically at offstep points. Although many examples of these a single example for which the off-step point is $\frac { 8 } { 1 5 }$ thods are known, we give justof the way through the step. That is, the first predictor computes an approximation to $\begin{array} { r l } { y ( x _ { n - 1 } + \frac { 8 } { 1 5 } h ) = } \end{array}$ $\textstyle y ( x _ { n } - { \frac { 7 } { 1 5 } } h )$ . We denote this first predicted value by the symbol $\scriptstyle { \mathcal { Y } } _ { n - 7 / 1 5 }$ and the corresponding derivative by $\begin{array} { r } { \dddot { f } _ { n - 7 / 1 5 } = f ( x _ { n } - \frac { 7 } { 1 5 } h , \widetilde { y } _ { n - 7 / 1 5 } ) } \end{array}$ . Similarly, the second predictor, which gives an initial approximation to $y ( x _ { n } )$ , will be denoted by $\widetilde { y } _ { n }$ and the corresponding derivative by $\widetilde { f } _ { n } ~ = ~ f ( x _ { n } , \widetilde { y } _ { n } )$ . This notation is in contrast to $y _ { n }$ and $f _ { n }$ , which denote the corrected step approximation to $y ( x _ { n } )$ and the corresponding derivative $f ( x _ { n } , y _ { n } )$ , respectively. The relationships between these quantities are

$$
\begin{array} { r l r } {  { \widetilde { y } _ { n - 7 / 1 5 } = - \frac { 5 2 9 } { 3 3 7 5 } y _ { n - 1 } + \frac { 3 9 0 4 } { 3 3 7 5 } y _ { n - 2 } + h ( \frac { 4 2 3 2 } { 3 3 7 5 } f _ { n - 1 } + \frac { 1 4 7 2 } { 3 3 7 5 } f _ { n - 2 } ) , } } \\ & { } & \\ & { } & { \widetilde { y } _ { n } = \frac { 1 5 2 } { 2 5 } y _ { n - 1 } - \frac { 1 2 7 } { 2 5 } y _ { n - 2 } + h ( \frac { 1 8 9 } { 9 2 } \widetilde { f } _ { n - 7 / 1 5 } - \frac { 4 1 9 } { 1 0 0 } f _ { n - 1 } - \frac { 1 1 1 8 } { 5 7 5 } f _ { n - 2 } ) , } \\ & { } & \\ & { } & { y _ { n } = y _ { n - 1 } + h ( \frac { 2 5 } { 1 6 8 } \widetilde { f } _ { n } + \frac { 3 3 7 5 } { 5 1 5 2 } \widetilde { f } _ { n - 7 / 1 5 } + \frac { 1 9 } { 9 6 } f _ { n - 1 } - \frac { 1 } { 5 5 2 } f _ { n - 2 } ) . \qquad } \end{array}
$$
