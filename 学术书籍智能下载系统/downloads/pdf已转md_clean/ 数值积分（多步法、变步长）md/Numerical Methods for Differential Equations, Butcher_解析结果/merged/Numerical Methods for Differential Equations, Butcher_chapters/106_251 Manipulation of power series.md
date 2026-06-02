# 251 Manipulation of power series

We consider problems for which the components of the function $f$ are rational in $x$ and in the components of $y$ . This means that the terms occurring in (250a) can all be computed by the use of addition (and subtraction), multiplication and division.

We use power series with the $1 / i$ ! factor absorbed into the coefficient of $f _ { i } ( x _ { n - 1 } , y _ { n - 1 } )$ . Hence each component takes the form $a _ { 0 } + a _ { 1 } h + a _ { 2 } h ^ { 2 } + \cdot \cdot \cdot +$ $a _ { m } h ^ { m }$ . If a second such expansion, $b _ { 0 } + b _ { 1 } h + b _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + b _ { m } h ^ { m }$ , is added or subtracted, then we simply add or subtract corresponding coefficients. The product of two terms is found by expanding the formal product but truncating after the $h ^ { m }$ term. This means that the product of $a _ { 0 } + a _ { 1 } h + a _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + a _ { m } h ^ { m }$ and $b _ { 0 } + b _ { 1 } h + b _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + b _ { m } h ^ { m }$ would be $c _ { 0 } + c _ { 1 } h + c _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + c _ { m } h ^ { m }$ , where

$$
c _ { i } = \sum _ { j = 0 } ^ { i } a _ { i - j } b _ { j } , \qquad i = 0 , 1 , \ldots , m .
$$

The formula for the quotient

$$
a _ { 0 } + a _ { 1 } h + a _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + a _ { m } h ^ { m } \approx { \frac { c _ { 0 } + c _ { 1 } h + c _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + c _ { m } h ^ { m } } { b _ { 0 } + b _ { 1 } h + b _ { 2 } h ^ { 2 } + \cdot \cdot \cdot + b _ { m } h ^ { m } } }
$$

is found by reinterpreting the relationship between the $a _ { i }$ , $b _ { i }$ and $c _ { i }$ coefficients in (251a) to give

$$
a _ { i } = \left\{ \begin{array} { l l } { \frac { c _ { 0 } } { b _ { 0 } } , ~ i = 0 , } \\ { \frac { c _ { i } - \sum _ { j = 1 } ^ { i } a _ { i - j } b _ { j } } { b _ { 0 } } , ~ i = 1 , 2 , . . . , m . } \end{array} \right.
$$

Given a system of differential equations with dependent variables $y ^ { 1 }$ , $y ^ { 2 }$ , $\ldots , \ y ^ { N }$ , write the truncated power series for $y ^ { k } ( x _ { n - 1 } + h )$ in the form $y _ { 0 } ^ { k } + h y _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m } y _ { m } ^ { k }$ , $k = 1 , 2 , \ldots , N$ . Also denote the power series for component $k$ of $f ( x _ { n - 1 } , Y )$ by $f _ { 0 } ^ { k } + h f _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m } f _ { m } ^ { k }$ , where the vector $Y$ has its components substituted by the series $y _ { 0 } ^ { l } + h y _ { 1 } ^ { l } + \cdot \cdot \cdot + h ^ { m } y _ { m } ^ { l }$ , $l = 1 , 2 , \ldots , N$ .

We consider how to evaluate in turn the $y _ { i } ^ { k }$ coefficients for each $k \mathbf { \Sigma } =$ $1 , 2 , \ldots , N$ , with $i$ taking on values from $0$ to $m$ . For $i \ = \ 0$ , all the $y _ { i } ^ { k }$ are known from initial information at the start of the current step. For each value of $i > 0$ we already know the coefficients $y _ { j } ^ { k }$ for all $k$ and for all $j < i$ . It is thus possible to evaluate the $h ^ { i - 1 }$ terms in the components in the power series for $f ( x _ { n - 1 } + h , y _ { n - 1 } )$ . Writing the differential equation in the form

$$
\begin{array} { r } { \frac { d } { d h } ( y _ { 0 } ^ { k } + h y _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m } y _ { m } ^ { k } ) = y _ { 1 } ^ { k } + 2 h y _ { 2 } ^ { k } + \cdot \cdot \cdot + m h ^ { m - 1 } y _ { m } ^ { k } } \\ { = f _ { 0 } ^ { k } + h f _ { 1 } ^ { k } + \cdot \cdot \cdot + h ^ { m - 1 } f _ { m - 1 } ^ { k } , } \end{array}
$$

where the last term on the right-hand side has been deleted, we see that $y _ { i } ^ { k } = f _ { i - 1 } ^ { k } / i$ .

When we have reached $i = m$ , all the required coefficients are known at $x = x _ { n - 1 }$ , and it is possible to take the step to $x = x _ { n }$ .

This method of solution will be illustrated in the next subsection.
