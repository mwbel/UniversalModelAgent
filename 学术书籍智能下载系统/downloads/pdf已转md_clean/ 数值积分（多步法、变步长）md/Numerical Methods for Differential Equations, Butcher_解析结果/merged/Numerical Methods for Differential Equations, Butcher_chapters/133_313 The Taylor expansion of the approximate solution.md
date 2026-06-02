# 313 The Taylor expansion of the approximate solution

We show that the result output by a Runge–Kutta methods is exactly the same as (311d), except that the factor $\gamma ( t ) ^ { - 1 }$ is replaced by $\Phi ( t )$ . We first establish a preliminary result.

Lemma 313A Let $k = 1 , 2 , \ldots ,$ . If

$$
Y _ { i } = y _ { 0 } + \sum _ { r ( t ) \leq k - 1 } { \frac { 1 } { \sigma ( t ) } } \Phi _ { i } ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { k } ) ,
$$

then

$$
h f ( Y _ { i } ) = \sum _ { r ( t ) \leq k } \frac { 1 } { \sigma ( t ) } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { k + 1 } ) .
$$

Proof. Use Lemma 310B. The coefficient of $\sigma ( t ) ^ { - 1 } F ( t ) ( y _ { 0 } ) h ^ { r ( t ) }$ in $h f ( Y _ { i } )$ is $\textstyle \prod _ { j = 1 } ^ { n } \Phi _ { i } ( t _ { j } )$ , where $t = \left\lfloor t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } \right\rfloor$ . $\boxed { \begin{array} { r l } \end{array} }$

We are now in a position to derive the formal Taylor expansion for the computed solution. The proof we give for this result is for a general Runge– Kutta method that may be implicit. In the case of an explicit method, the iterations used in the proof can be replaced by a sequence of expansions for $Y _ { 1 }$ , for $h f ( Y _ { 1 } )$ , for $Y _ { 2 }$ , for $h f ( Y _ { 2 } )$ , and so on until we reach $Y _ { s }$ , $h f ( Y _ { s } )$ and finally $y _ { 1 }$ .

Theorem 313B The Taylor expansions for the stages, stage derivatives and output result for a Runge–Kutta method are

$$
\begin{array} { c } { { Y _ { i } = y _ { 0 } + \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } \Phi _ { i } ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) , i = 1 , 2 , \ldots , s , } } \\ { { \displaystyle h f ( Y _ { i } ) = \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) , i = 1 , 2 , \ldots , s , } } \\ { { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { r ( t ) \leq n } \displaystyle \frac { 1 } { \sigma ( t ) } \Phi ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + { \cal O } ( h ^ { n + 1 } ) . } } \end{array}
$$

Proof. In a preliminary part of the proof, we consider the sequence of approximations to $Y _ { i }$ given by

$$
\begin{array} { l l } { { { \displaystyle Y _ { i } ^ { [ 0 ] } = y _ { 0 } } , } } & { { i = 1 , 2 , \ldots , s , } } \\ { { { \displaystyle Y _ { i } ^ { [ k ] } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f \left( Y _ { j } ^ { [ k - 1 ] } \right) , \ } } } & { { i = 1 , 2 , \ldots , s . } } \end{array}
$$

We prove by induction that Y [n]i agrees with the expression given for $Y _ { i }$ to within $O ( h ^ { n + 1 } ) .$ For $n = 0$ this is clear. For $n > 0$ , suppose it has been proved for $n$ replaced by $n - 1$ . From Lemma 313A with $k = n - 1$ and $Y _ { i }$ replaced by $Y _ { i } ^ { \lfloor n - 1 \rfloor }$ , we see that

$$
k f ( Y _ { i } ^ { [ n - 1 ] } ) = \sum _ { r ( t ) \leq n } { \frac { 1 } { \sigma ( t ) } } ( \Phi _ { i } D ) ( t ) h ^ { r ( t ) } F ( t ) ( y _ { 0 } ) + O ( h ^ { n + 1 } ) , \quad i = 1 , 2 , \ldots , s .
$$

Calculate Y [n]i using (313c) and the preliminary result follows. Assume $h$ tly to mall to guarantee convergence of the sequenceand (313c) follows. Finally, (313d) follows from $( Y _ { i } ^ { [ 0 ] } , Y _ { i } ^ { [ 1 ] } , Y _ { i } ^ { [ 2 ] } , \dots )$ $Y _ { i }$ Lemma 313A and (313e) from (312d). 
