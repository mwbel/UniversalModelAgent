# 410 Criteria for order

Given a linear multistep method $[ \alpha , \beta ]$ , we seek conditions on the coefficients in the polynomials $\alpha$ and $\beta$ that will guarantee that, locally, errors are $O ( h ^ { p + 1 } )$ . By this we mean that if starting values satisfy $y _ { i } = y ( x _ { i } ) + O ( h ^ { p + 1 } )$ , for $i = 0 , 1 , \ldots , k { - } 1$ , then this will imply that a similar estimate persists for $i \geq k$ . We emphasize that this is a local property in the sense that it cannot be used in a limiting case in which integration is carried to a fixed point $\overline { { x } } > x _ { 0 }$ , because the number of steps required to achieve this is approximately $( { \overline { { x } } } - x _ { 0 } ) / h$ , and this is unbounded as $h  0$ . To verify that $y _ { n } = y ( x _ { n } ) + O ( h ^ { p + 1 } )$ , assuming the same is true for the previous $k$ step values, it will be enough to estimate the value of

$$
y ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x _ { n - i } ) - \sum _ { i = 0 } ^ { k } \beta _ { i } h y ^ { \prime } ( x _ { n - i } )
$$

and to show that, under appropriate smoothness assumptions, it is $O ( h ^ { p + 1 } )$ . The smoothness assumptions will be that the problem under consideration has a solution with continuous derivatives up to order $p + 1$ . This will enable us to expand (410a) in a Taylor series

$$
\begin{array} { r l } & { C _ { 0 } y ( x _ { n } ) + C _ { 1 } h y ^ { \prime } ( x _ { n } ) + C _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot } \\ & { \qquad + C _ { p } h ^ { p } y ^ { ( p ) } ( x _ { n } ) + C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + \cdot \cdot \cdot } \end{array}
$$

and order $p$ will mean that $C _ { 0 } = C _ { 1 } = \cdot \cdot \cdot = C _ { p }$ . The value of $C _ { p + 1 }$ is closely related to the error constant and is non-zero unless the order is actually higher than $p$ .

Theorem 410A The constants $C _ { 0 } , C _ { 1 } , C _ { 2 } , \ldots$ . in (410b) are given by

$$
\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) ) = C _ { 0 } + C _ { 1 } z + C _ { 2 } z ^ { 2 } + \cdot \cdot \cdot .
$$

Proof. The coefficient of in the Taylor expansion of (410a) is equal to $\textstyle 1 - \sum _ { i = 1 } ^ { k } \alpha _ { i }$ , and this equals the constant term in the Taylor expansion of $\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) )$ . Now suppose that $j = 1 , 2 , \dots$ and calculate the coefficient of $y ^ { ( j ) } ( x _ { n } )$ in the Taylor expansion of (410a). This equals

$$
- \sum _ { i = 1 } ^ { k } \alpha _ { i } { \frac { ( - i ) ^ { j } } { j ! } } - \sum _ { i = 0 } ^ { k } \beta _ { i } { \frac { ( - i ) ^ { j - 1 } } { ( j - 1 ) ! } } ,
$$

where the coefficient of $\beta _ { 0 }$ is $^ { - 1 }$ if $j = 1$ and zero for $j > 1$ . This is identical to the coefficient of $z ^ { j }$ in the Taylor expansion of $\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) )$ .


<!-- chunk 0006: pages 351-420 -->
Altering the expression in (410c) slightly, we can state without proof a criterion for order:

Theorem 410B A linear multistep method $[ \alpha , \beta ]$ has order $p$ (or higher) if and only if

$$
\alpha ( \exp ( z ) ) + z \beta ( \exp ( z ) ) = O ( z ^ { p + 1 } ) .
$$

Because we have departed from the traditional $( \rho , \sigma )$ formulation for linear multistep methods, we restate this result in that standard notation:

Theorem 410C A linear multistep method $( \rho , \sigma )$ has order $p$ if and only if

$$
\rho ( \exp ( z ) ) - z \sigma ( \exp ( z ) ) = { \cal O } ( z ^ { p + 1 } ) .
$$

Return now to Theorem 410B and replace $\exp ( z )$ by $( 1 + z ) ^ { - 1 }$ . It is found that

$$
\alpha ( ( 1 + z ) ^ { - 1 } ) - \log ( 1 + z ) \beta ( ( 1 + z ) ^ { - 1 } ) = O ( z ^ { p + 1 } ) ,
$$

where $\log ( 1 + z )$ is defined only in $\{ z \in \mathbb { C } : | z | < 1 \}$ by its power series

$$
\log ( 1 + z ) = z - { \frac { 1 } { 2 } } z ^ { 2 } + { \frac { 1 } { 3 } } z ^ { 3 } - \cdot \cdot \cdot .
$$

Because both $\alpha ( 1 + z )$ and $\log ( 1 + z )$ vanish when $z = 0$ , it is possible to rearrange (410d) in the form given in the following result, which we present without further proof.

Theorem 410D A linear multistep formula $\lfloor \alpha , \beta \rfloor$ has order $p$ if and only if

$$
\frac { z } { \log ( 1 + z ) } \frac { \alpha ( 1 + z ) } { z } + \beta ( 1 + z ) = O ( z ^ { p } ) .
$$
