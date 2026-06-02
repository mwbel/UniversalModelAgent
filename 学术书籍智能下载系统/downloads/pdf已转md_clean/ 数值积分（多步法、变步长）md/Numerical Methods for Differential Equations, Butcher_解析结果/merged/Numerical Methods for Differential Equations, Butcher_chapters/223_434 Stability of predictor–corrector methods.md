# 434 Stability of predictor–corrector methods

We consider examples of PEC and PECE methods. For the PEC method based on second order Adams–Bashforth as predictor and Adams–Moulton as corrector, we have the following equations for the predicted and corrected values:

$$
\begin{array} { l } { { y _ { n } ^ { * } = y _ { n - 1 } + \displaystyle \frac { 3 } { 2 } h f _ { n - 1 } ^ { * } - \displaystyle \frac { 1 } { 2 } h f _ { n - 2 } ^ { * } , } } \\ { { y _ { n } = y _ { n - 1 } + \displaystyle \frac { 1 } { 2 } h f _ { n } ^ { * } + \displaystyle \frac { 1 } { 2 } h f _ { n - 1 } ^ { * } . } } \end{array}
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/ee04c8a3dee460a681acb16f7c1aacb063907f1bfc23ccb2ee30f36ef0985915.jpg)  
Stability regions for Adams–Moulton methods (solid lines) and PEC methods (dashed lines)

Superficially, this system describes two sequences, the $y$ and the $y ^ { * }$ which develop together. However, it is only the $y ^ { * }$ sequence that has derivative values associated with it. Hence, the $y$ sequence can conveniently be eliminated from consideration. Replace $n$ by $n + 1$ in (434a), and we find

$$
y _ { n + 1 } ^ { * } = y _ { n } + { \frac { 3 } { 2 } } h f _ { n } ^ { * } - { \frac { 1 } { 2 } } h f _ { n - 1 } ^ { * } .
$$

Add (434b) to this equation and subtract (434a), and we find

$$
y _ { n + 1 } ^ { * } = y _ { n } ^ { * } + 2 h f _ { n } ^ { * } - { \frac { 3 } { 2 } } h f _ { n - 1 } ^ { * } + { \frac { 1 } { 2 } } h f _ { n - 2 } ^ { * } .
$$

Apart from the actual values of the coefficients, this resembles an Adams– Bashforth method, and its stability region can be found in a similar way. If $\beta ^ { * }$ and $\beta$ are the respective generating polynomials for an order $p$ Adams– Bashforth method and the corresponding Adams–Moulton method, then the general form of the generating polynomial for $y ^ { * }$ in a PEC method is equal to $\widehat { \beta }$ , where

$$
\widehat { \beta } ( z ) = \beta ^ { \ast } ( z ) + \beta _ { 0 } z ( 1 - z ) ^ { p } .
$$

The value of $\beta _ { 0 }$ could be replaced by any value we wish without sacrificing the order $p$ . In fact, it could be replaced by the value of $( - 1 ) ^ { p } \beta _ { p + 1 } ^ { * }$ so that the method would actually be of order $p + 1$ . It would in this case be precisely the order $p + 1$ Adams–Bashforth method. Another advantage of pushing the order up one unit rather than accepting the standard PEC result, is that the stability region seems to be less desirable for PEC methods. This is illustrated in Figure 434(i), where the boundaries of some of these regions are shown.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/8f04aebd1d960629206629689f80e8d1360d55beeb650d1887cf2744ee99c32e.jpg)  
Stability regions for PECE methods with $q = p$ (solid lines) and $q = p - 1$ methods (dashed lines). In each case $p$ is attached to the curves

PECE methods are more interesting because two derivatives are computed in each step. Thus they are in reality two-stage general linear methods. From the stability point of view, they can be analysed by eliminating $y _ { n } ^ { * }$ so that the method

$$
\begin{array} { l } { { \displaystyle y _ { n } ^ { * } = y _ { n - 1 } + h \sum _ { i = 1 } ^ { k } \beta _ { i } ^ { * } f _ { n - i } } , } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + h \beta _ { 0 } f _ { n } ^ { * } + h \sum _ { i = 1 } ^ { k } \beta _ { i } f _ { n - i } } } \end{array}
$$

yields the difference equation

$$
y _ { n } = ( 1 + ( \beta _ { 0 } + \beta _ { 1 } ) z + \beta _ { 0 } \beta _ { 1 } ^ { * } z ^ { 2 } ) y _ { n - 1 } + \sum _ { i = 2 } ^ { k } ( \beta _ { i } z + \beta _ { 0 } \beta _ { i } ^ { * } z ^ { 2 } ) y _ { n - i } .
$$

Note that the step $k$ may be higher for the predictor than for the corrector but we assume that, if this is the case, sufficient zero values are added to the sequence of $\beta _ { i }$ values to make the two $k$ values effectively equal. In practice there are two options. Either both the predictor and corrector have the same order $p$ , in which case $k = p$ for the predictor and $k = p - 1$ for the corrector; or $k = p - 1$ for both predictor and corrector; in this case the predictor has order only $p - 1$ . The boundaries of the stability regions are shown in Figure 434(ii) for each of these cases.

The relatively more generous stability regions for the PECE methods, when compared with PEC methods, for $p ~ > ~ 1$ are regarded as constituting a significant advantage in carrying out a final evaluation in implementations of predictor–corrector methods. Similar comparisons apparently favour PECECE over PECE methods.

# Exercises 43

43.1 Use the Schur criterion to show that all zeros of the polynomial $7 z ^ { 3 } - 1 1 z ^ { 2 } + 5 z + 1$ lie in the unit disc.

43.2 Use the Schur criterion to show that not all zeros of the polynomial $7 z ^ { 3 } - 1 1 z ^ { 2 } + 6 z + 1$ lie in the unit disc.

43.3 Determine whether or not all zeros of the polynomial $7 z ^ { 3 } - 1 1 z ^ { 2 } + ( 5 +$ $i ) z + 1$ lie in the unit disc.

43.4 Find the stability regions for the PEC and PECE methods based on the fourth order Adams–Bashforth and Adams–Moulton methods.
