# 242 General form of linear multistep methods

Even though Adams methods are amongst the most commonly used classes of linear multistep methods, they are very specialized in that the dependence of $y _ { n }$ on previously computed values ignores $y _ { n - 1 }$ , $y _ { n - 2 }$ , $\cdot \cdot \cdot$ , $y _ { n - k }$ . The general form of the method includes additional terms to take these into account. It thus has the form

$$
\begin{array} { c } { y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ { + h \big ( \beta _ { 0 } f ( x _ { n } , y _ { n } ) + \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) } \\ { + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) \big ) . } \end{array}
$$

It is customary to characterize this method by polynomials whose coefficients are the numbers $\alpha _ { 1 }$ , $\alpha _ { 2 }$ , . . . , $\alpha _ { k }$ , $\beta _ { 0 }$ , $\beta _ { 1 }$ , $\beta _ { 2 }$ , $\cdot \cdot \cdot$ , $\beta _ { k }$ . The standard terminology is to use polynomials $\rho ( z )$ and $\sigma ( z )$ defined by

$$
\begin{array} { l } { \rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } , } \\ { \sigma ( z ) = \beta _ { 0 } z ^ { k } + \beta _ { 1 } z ^ { k - 1 } + \beta _ { 2 } z ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } . } \end{array}
$$

The style we are adopting in this book makes it more convenient to use a slightly different pair of polynomials,

$$
\begin{array} { l } { \alpha ( z ) = 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } z ^ { k } , } \\ { \beta ( z ) = \beta _ { 0 } + \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { k } z ^ { k } . } \end{array}
$$

Of course, it really makes little difference whether we use $( \rho , \sigma )$ or $[ \alpha , \beta ]$ t o characterize a method because, once the value of $k$ is known, we can move between them by the relations

$$
\alpha ( z ) = z ^ { k } \rho \Big ( \frac { 1 } { z } \Big ) , \beta ( z ) = z ^ { k } \sigma \Big ( \frac { 1 } { z } \Big ) , \rho ( z ) = z ^ { k } \alpha \Big ( \frac { 1 } { z } \Big ) , \sigma ( z ) = z ^ { k } \beta \Big ( \frac { 1 } { z } \Big ) .
$$

For all eligible $\alpha$ polynomials, $\alpha ( 0 ) = 1$ , and for Adams methods, $\alpha ( z ) = 1 - z$ . Using the $[ \alpha , \beta ]$ representation, we can distinguish Adams–Bashforth from Adams–Moulton by the fact that $\beta ( 0 ) = 0$ for the Bashforth variety.
