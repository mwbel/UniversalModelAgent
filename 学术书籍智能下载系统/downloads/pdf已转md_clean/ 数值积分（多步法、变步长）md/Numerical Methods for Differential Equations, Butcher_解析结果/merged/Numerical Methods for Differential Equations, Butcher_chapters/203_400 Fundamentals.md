# 400 Fundamentals

This chapter, devoted entirely to the analysis of linear multistep methods, follows on from the introduction to these methods presented in Section 24. We use the notation and ideas introduced there, but attempt to fill in missing details. In particular, we show in the present section how the concepts of consistency, stability and convergence are interrelated and give more of a theoretical justification for the concept of ‘order’. This analysis depends heavily on the use of difference equations, especially on the conditions for the solution of a linear difference equation to be bounded. For a difference equation,

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } ,
$$

we recall that all solutions are bounded if and only if the polynomial

$$
z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k }
$$

has all its zeros in the closed unit disc and all multiple zeros in the interior of this disc.

The direct applicability of this result to a linear multistep method $[ \alpha , \beta ]$ , in which the approximate solution at $x _ { n }$ is computed by

$$
\begin{array} { r l } & { y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ & { \qquad + \beta _ { 0 } h f ( x _ { n } , y _ { n } ) + \beta _ { 1 } h f ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + \beta _ { k } h f ( x _ { n - k } , y _ { n - k } ) , } \end{array}
$$

is clear. We wish to be able to solve a wide variety of initial value problems in a reliable manner, and amongst the problems for which we need good answers is certainly the simple problem for which $f ( x , y ) = 0$ . In this case the solution approximations are related by (400a), and stable behaviour for this problem becomes essential. It is a remarkable fact that convergence hinges on this stability result alone, as well as on consistency requirements.

As in Section 24 we write the method as $[ \alpha , \beta ]$ , where

$$
\begin{array} { l } { \alpha ( z ) = 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } z ^ { k } , } \\ { \beta ( z ) = \beta _ { 0 } + \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { k } z ^ { k } , } \end{array}
$$

or in the more traditional formulation as $( \rho , \sigma )$ , where

$$
\begin{array} { l } { \rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } , } \\ { \quad } \\ { \sigma ( z ) = \beta _ { 0 } z ^ { k } + \beta _ { 1 } z ^ { k - 1 } + \beta _ { 2 } z ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } . } \end{array}
$$
