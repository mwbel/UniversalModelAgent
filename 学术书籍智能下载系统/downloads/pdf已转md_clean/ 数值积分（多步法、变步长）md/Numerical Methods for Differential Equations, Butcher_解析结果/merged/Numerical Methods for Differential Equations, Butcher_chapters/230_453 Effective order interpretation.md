# 453 Effective order interpretation

The concept of effective order, introduced in Subsections 365 and 389, gives an alternative interpretation of the relationship between the computed approximation and the exact solution.

Define the function $\gamma ( z )$ by

$$
\gamma ( z ) = \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } \exp ( - i z ) \bigg ) ^ { - 1 } = \gamma _ { 0 } + \gamma _ { 1 } z + \gamma _ { 2 } z ^ { 2 } + \cdots ,
$$

where $\gamma _ { 0 } = 1$ , and the starting approximation by

$$
S ( y ) ( x ) = \sum _ { i = 0 } ^ { p } \gamma _ { i } h ^ { i } y ^ { ( i ) } ( x ) ,
$$

assuming the linear multistep method $\lfloor \alpha , \beta \rfloor$ has order $p$ . Write ${ \widehat { y } } ( x ) = S ( y ) ( x )$ . We then have

$$
\widehat { y } ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } \widehat { y } ( x _ { n - i } ) = h \sum _ { i = 1 } ^ { k } \beta _ { i } f \biggr ( x _ { n } , \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } \widehat { y } ( x _ { n - i } ) \biggr ) + O ( h ^ { p + 1 } ) .
$$
