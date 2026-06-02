# 503 Linear multistep methods as general linear methods

For a linear $k$ -step method $[ \alpha , \beta ]$ of the special form $\alpha ( z ) = 1 - z$ , the natural way of writing this as a general linear method is to choose $r = k + 1$ , $s = 1$ and the input approximations as

$$
y ^ { [ n - 1 ] } \approx \left[ \begin{array} { c } { y ( x _ { n - 1 } ) } \\ { h y ^ { \prime } ( x _ { n - 1 } ) } \\ { h y ^ { \prime } ( x _ { n - 2 } ) } \\ { \cdots } \\ { h y ^ { \prime } ( x _ { n - k } ) } \end{array} \right] .
$$

The matrix representing the method now becomes

$$
{ [ \begin{array} { l l l l l l l } { \beta _ { 0 } | } & { 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } } & { \beta _ { k } } \\ { \beta _ { 0 } | } & { 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } } & { \beta _ { k } } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} ] } .
$$

Because y[1 $y _ { 1 } ^ { \lfloor n - 1 \rfloor }$ and $y _ { k + 1 } ^ { [ n - 1 ] }$ occur in the combination $y _ { 1 } ^ { [ n - 1 ] } + \beta _ { k } y _ { k + 1 } ^ { [ n - 1 ] }$ in each of the two places where these quantities are used, we might try to simplify the method by transforming using the matrix

$$
T = { \left[ \begin{array} { l l l l l l } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { \beta _ { k } } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] } ~ .
$$

The transformed coefficient matrices become

$$
[ \begin{array} { l l l l l l l l } { A } & { U T ^ { - 1 } } \\ { T B } & { T V T ^ { - 1 } } \end{array} ] = [ \begin{array} { l l l l l l l l } { \beta _ { 0 } | 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } } & { 0 } \\ { \beta _ { 0 } | 1 } & { \beta _ { 1 } } & { \beta _ { 2 } } & { \beta _ { 3 } } & { \cdots } & { \beta _ { k - 1 } + \beta _ { k } } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} ] ,
$$

and we see that it is possible to reduce $r$ from $k + 1$ to $k$ , because the $( k + 1 ) \mathrm { t h }$ input vector is never used in the calculation.

The well-known technique of implementing an implicit linear multistep method by combining it with a related explicit method to form a predictor– corrector pair fits easily into a general linear formulation. Consider, for example, the PECE method based on the third order Adams Bashforth and Adams–Moulton predictor–corrector pair. Denote the predicted approximation by $y _ { n } ^ { * }$ and the corrected value by $y _ { n }$ . We then have

$$
\begin{array} { l } { { y _ { n } ^ { * } = y _ { n - 1 } + { \displaystyle \frac { 2 3 } { 1 2 } } h f ( x _ { n - 1 } , y _ { n - 1 } ) - { \displaystyle \frac { 4 } { 3 } } h f ( x _ { n - 2 } , y _ { n - 2 } ) + { \displaystyle \frac { 5 } { 1 2 } } h f ( x _ { n - 3 } , y _ { n - 3 } ) , } } \\ { { y _ { n } = y _ { n - 1 } + { \displaystyle \frac { 5 } { 1 2 } } h f ( x _ { n } , y _ { n } ^ { * } ) + { \displaystyle \frac { 2 } { 3 } } h f ( x _ { n - 1 } , y _ { n - 1 } ) - { \displaystyle \frac { 1 } { 1 2 } } h f ( x _ { n - 2 } , y _ { n - 2 } ) . } } \end{array}
$$

As a two-stage general linear method, we write $Y _ { 1 } ~ = ~ y _ { n } ^ { * }$ and $Y _ { 2 } ~ = ~ y _ { n }$ . The $r \ = \ 4$ input approximations are the values of $y _ { n - 1 }$ , $h f ( x _ { n - 1 } , y _ { n - 1 } )$ , $h f ( x _ { n - 2 } , y _ { n - 2 } )$ and $h f ( x _ { n - 3 } , y _ { n - 3 } )$ . The $( s + r ) \times ( s + r )$ coefficient matrix is now

$$
[ \begin{array} { c c } { 0 } & { 0 } \\ { \frac { 5 } { 1 2 } } & { 0 } \\ { \frac { 5 } { 1 2 } } & { 0 } \\ { 0 } & { 1 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} ] \begin{array} { c c c } { 1 } & { \frac { 2 3 } { 1 2 } } & { - \frac { 4 } { 3 } } \\ { 1 } & { \frac { 2 } { 3 } } & { - \frac { 1 } { 1 2 } } \\ { \frac { 2 } { 3 } } & { - \frac { 1 } { 1 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} ] .
$$

The one-leg methods, introduced by Dahlquist (1976) as counterparts of linear multistep methods, have their own natural representations as general linear methods. For the method characterized by the polynomial pair $[ \alpha ( z ) , \beta ( z ) ]$ , the corresponding one-leg method computes a single stage value $Y$ , with stage derivative $F ^ { \dagger }$ , using the formula

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } + { \biggl ( } \sum _ { i = 0 } ^ { k } \beta _ { i } { \biggr ) } h F ,
$$

where

$$
Y = \frac { \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n - i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } .
$$

This does not fit into the standard representation for general linear methods but it achieves this format when $Y$ and $y _ { n }$ are separated out from the two expressions (503b) and (503c). We find

$$
\begin{array} { l } { { \displaystyle Y = \beta _ { 0 } h F + \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) ^ { - 1 } \sum _ { i = 1 } ^ { k } ( \beta _ { 0 } \alpha _ { i } + \beta _ { i } ) y _ { n - i } } , } \\ { { \displaystyle y _ { n } = \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) h F + \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } } . } \end{array}
$$

As a general linear method, it has the form

$$
[ \begin{array} { c }  \frac { \beta _ { 0 } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } | \begin{array} { c c c c c c } { \gamma _ { 1 } } & { \gamma _ { 2 } } & { \gamma _ { 3 } } & { \cdots } & { \gamma _ { k - 1 } } & { \gamma _ { k } } \\ { \alpha _ { 1 } } & { \alpha _ { 2 } } & { \alpha _ { 3 } } & { \cdots } & { \alpha _ { k - 1 } } & { \alpha _ { k } } \\ { 0 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} ] , \end{array}
$$

where

$$
\gamma _ { i } = \bigg ( \sum _ { j = 0 } ^ { k } \beta _ { j } \bigg ) ^ { - 1 } \big ( \beta _ { 0 } \alpha _ { i } + \beta _ { i } \big ) , \qquad i = 1 , 2 , \ldots , k .
$$
