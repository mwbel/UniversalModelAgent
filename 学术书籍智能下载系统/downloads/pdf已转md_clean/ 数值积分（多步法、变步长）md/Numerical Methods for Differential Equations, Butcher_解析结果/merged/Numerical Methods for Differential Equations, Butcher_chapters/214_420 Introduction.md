# 420 Introduction

The result computed in a step is generally not exact, even if we ignore any errors introduced in previous steps. However, once a significant departure from the exact solution has occurred, we are in effect solving a different problem. Hence, a proper analysis of error takes account of errors generated locally, and also the accumulated effect of errors generated in previous steps. We present a simplified discussion of this phenomenon in this subsection, and discuss the limitations of this discussion in Subsection 421.

Suppose a sequence of approximations

$$
\begin{array} { c } { y _ { 1 } \approx y ( x _ { 1 } ) , } \\ { y _ { 2 } \approx y ( x _ { 2 } ) , } \\ { \vdots \qquad \vdots } \\ { y _ { n - 1 } \approx y ( x _ { n - 1 } ) , } \end{array}
$$

has been computed, and we are now computing step $n$ . If, for the moment, we ignore errors in previous steps, the value of $y _ { n }$ can be evaluated using a Taylor expansion where, for implicit methods, we need to take account of the fact that $f ( y _ { n } )$ is also being calculated. We have

$$
\begin{array} { l } { y ( x _ { n } ) - y _ { n } - h \beta _ { 0 } ( f ( y ( x _ { n } ) ) - f ( y _ { n } ) ) } \\ { \displaystyle = y ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x _ { n - i } ) - h \sum _ { i = 0 } ^ { k } \beta _ { i } y ^ { \prime } ( x _ { n - 1 } ) , } \end{array}
$$

which is equal to

$$
C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) .
$$

In this informal discussion, we not only ignore the term $O ( h ^ { p + 2 } )$ but also treat the value of $h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n - i } )$ as constant. This is justified in a local sense. That is, if we confine ourselves to a finite sequence of steps preceding step $n$ , then the variation in values of this quantity will also be $O ( h ^ { p + 2 } )$ , and we ignore such quantities. Furthermore, if

$$
y ( x _ { n } ) - y _ { n } - h \beta _ { 0 } ( f ( y ( x _ { n } ) ) - f ( y _ { n } ) ) \approx C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) ,
$$

then the assumption that $f$ satisfies a Lipschitz condition will imply that

$$
y ( x _ { n } ) - y _ { n } \approx C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } )
$$

and that

$$
h ( f ( y ( x _ { n } ) ) - f ( y _ { n } ) ) = O ( h ^ { p + 2 } ) .
$$

With the contributions of terms of this type thrown into the $O ( h ^ { p + 2 } )$ category, and hence capable of being ignored from the calculation, we can write a difference equation for the error in step $n$ , which will be written as $\epsilon _ { n } = y ( x _ { n } ) - y _ { n }$ , in the form

$$
\epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } = K h ^ { p + 1 } ,
$$

where $K$ is a representative value of $C _ { p + 1 } { \boldsymbol { y } } ^ { ( p + 1 ) }$

For a stable consistent method, the solution of this equation takes the form

$$
\epsilon _ { n } = - \alpha ^ { \prime } ( 1 ) ^ { - 1 } h ^ { p + 1 } n K + \sum _ { i = 1 } ^ { k } \eta _ { i } \lambda _ { i } ^ { n } ,
$$

where the coefficients $\eta _ { i }$ , $i = 1 , 2 , \ldots , k$ , depend on initial values and $\lambda _ { i }$ , $i = 1 , 2 , \ldots , k$ , are the solutions to the polynomial equation $\alpha ( \lambda ^ { - 1 } ) = 0$ .

The factor $- \alpha ^ { \prime } ( 1 ) ^ { - 1 }$ that occurs in (420a) can be written in a variety of forms, and we have

$$
- \alpha ^ { \prime } ( 1 ) = \rho ^ { \prime } ( 1 ) = \beta ( 1 ) = \sigma ( 1 ) = \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } .
$$

The value of $- C \alpha ^ { \prime } ( 1 ) ^ { - 1 }$ is known as the ‘error constant’ for the method and represents the factor by which $h ^ { p + 1 } y ^ { ( p + 1 ) }$ must be multiplied to give the contribution from each step to the accumulated error. Since the method is assumed to be stable, the terms of the form $\eta _ { i } \lambda _ { i } ^ { n }$ can be disregarded compared with the linearly growing term $- \alpha ^ { \prime } ( 1 ) ^ { - 1 } h ^ { p + 1 } n K$ . If the integration is carried out to a specific output value $\scriptstyle { \overline { { x } } }$ , and $n$ steps are taken to achieve this result, then $h n = \overline { { x } } - x _ { 0 }$ . In this case we can make a further simplification and write the accumulated error as approximately

$$
- ( \overline { { x } } - x _ { 0 } ) \alpha ^ { \prime } ( 1 ) ^ { - 1 } h ^ { p } C y ^ { ( p + 1 ) } ( \overline { { x } } ) .
$$

In the next subsection, these ideas will be discussed further.
