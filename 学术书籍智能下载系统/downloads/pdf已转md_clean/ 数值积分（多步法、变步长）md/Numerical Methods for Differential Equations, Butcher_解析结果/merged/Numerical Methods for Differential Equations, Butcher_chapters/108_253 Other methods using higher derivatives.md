# 253 Other methods using higher derivatives

We consider the possibility of using higher derivative information at more than one step value. In particular, we consider two special schemes of the form

$$
\begin{array} { c } { { y _ { n } = y _ { n - 1 } + h \alpha _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + h ^ { 2 } \alpha _ { 2 } f _ { 2 } ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot } } \\ { { + h ^ { m } \alpha _ { m } f _ { m } ( x _ { n - 1 } , y _ { n - 1 } ) + h \beta _ { 1 } f ( x _ { n - 2 } , y _ { n - 2 } ) } } \\ { { + h ^ { 2 } \beta _ { 2 } f _ { 2 } ( x _ { n - 2 } , y _ { n - 2 } ) + \cdot \cdot \cdot + h ^ { m } \beta _ { m } f _ { m } ( x _ { n - 2 } , y _ { n - 2 } ) } } \end{array}
$$

and

$$
\begin{array} { c } { y _ { n } = y _ { n - 1 } + h \gamma _ { 1 } f ( x _ { n } , y _ { n } ) + h ^ { 2 } \gamma _ { 2 } f _ { 2 } ( x _ { n } , y _ { n } ) + \cdot \cdot \cdot } \\ { \qquad + h ^ { m } \gamma _ { m } f _ { m } ( x _ { n } , y _ { n } ) + h \delta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) } \\ { \qquad + h ^ { 2 } \delta _ { 2 } f _ { 2 } ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + h ^ { m } \delta _ { m } f _ { m } ( x _ { n - 1 } , y _ { n - 1 } ) . } \end{array}
$$

The scheme (253a) uses information already available before step $n$ is attempted. Thus it can be regarded as a generalization of an Adams–Bashforth method. In contrast, the scheme (253b) is fully implicit, and thus corresponds to an Adams–Moulton method. Using Taylor series analyses, conditions for order $2 m$ can readily be found. These are equivalent to the conditions


<!-- chunk 0003: pages 141-210 -->
$$
\begin{array} { c } { \exp ( z ) - ( 1 + \alpha _ { 1 } z + \alpha _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \alpha _ { m } z ^ { m } ) } \\ { - \left( \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { m } z ^ { m } \right) \exp ( - z ) = O ( z ^ { 2 m + 1 } ) } \end{array}
$$

and

$$
\begin{array} { c } { { \exp ( z ) ( 1 - \gamma _ { 1 } z - \gamma _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \gamma _ { m } z ^ { m } ) } } \\ { { - \ ( 1 + \delta _ { 1 } z + \delta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \delta _ { m } z ^ { m } ) = O ( z ^ { 2 m + 1 } ) . } } \end{array}
$$

Note that the rational function

$$
\frac { N ( z ) } { D ( z ) } = \frac { 1 + \delta _ { 1 } z + \delta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \delta _ { m } z ^ { m } } { 1 - \gamma _ { 1 } z - \gamma _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \gamma _ { m } z ^ { m } } ,
$$

is known as a Pad´e approximation to the exponential function. It is the unique rational function with degree $m$ in both numerator and denominator, which maximizes the order of approximation of $N ( z ) / D ( Z )$ to $\exp ( z )$ .

For easy reference, the coefficients $\alpha _ { i }$ , $\beta _ { i }$ , $\gamma _ { i }$ and $\delta _ { i }$ are shown in Tables 253(I) and 253(II) up to $m = 4$ .

An example of the use of the methods discussed here, in a predictor– corrector mode, will be presented in Subsection 255.
