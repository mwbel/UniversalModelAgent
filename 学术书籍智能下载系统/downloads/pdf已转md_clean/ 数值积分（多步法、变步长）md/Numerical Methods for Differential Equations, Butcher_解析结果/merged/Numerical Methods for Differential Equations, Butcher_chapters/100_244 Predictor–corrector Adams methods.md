# 244 Predictor–corrector Adams methods

Continuing the discussion of Adams–Bashforth and Adams–Moulton methods from Subsection 241, we present in tabular form the coefficients of these methods for orders as high as 8. In the Adams–Bashforth case this means presenting the methods as far as $k = 8$ and in the Moulton case as far as $k = 7$ .

Along with the coefficients of the methods, the value is given of the error constants. For example, in the case of the Adams–Bashforth method with order 2 we can write

$$
y ( x _ { n } ) = y ( x _ { n - 1 } ) + h \big ( { \textstyle \frac { 3 } { 2 } } y ^ { \prime } ( x _ { n - 1 } ) - { \textstyle \frac { 1 } { 2 } } y ^ { \prime } ( x _ { n - 2 } ) \big ) + C h ^ { 3 } y ^ { ( 3 ) } ( x _ { n } ) + O ( h ^ { 4 } ) ,
$$

Coefficients and error constants for Adams–Bashforth methods   

<table><tr><td>k</td><td>β1</td><td></td><td></td><td>ββββ5</td><td></td><td></td><td>βββ8</td><td></td><td></td></tr><tr><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>24</td><td>59 24</td><td>中</td><td>3</td><td></td><td></td><td></td><td></td><td>251 720</td></tr><tr><td>5</td><td>1901 720</td><td>1387 360</td><td>109 30</td><td>637 360</td><td>251 720</td><td></td><td></td><td></td><td>95 288</td></tr><tr><td>6</td><td>4277 1440</td><td>2641 480</td><td>4991 720</td><td>3649 720</td><td>959 480</td><td>95 288</td><td></td><td></td><td>19087 60480</td></tr><tr><td>7</td><td>198721 60480</td><td>18637 2520</td><td>235183 20160</td><td>10754 945</td><td>135713 20160</td><td>5603 2520</td><td>19087 60480</td><td></td><td>5257 17280</td></tr><tr><td>8</td><td>16083 4480</td><td>1152169 120960</td><td>242653 13440</td><td>296053 13440</td><td>2102243 120960</td><td>115747 13440</td><td>32863 13440</td><td>5257 17280</td><td>1070017 3628800</td></tr></table>

Coefficients and error constants for Adams–Moulton methods   

<table><tr><td>k</td><td>β</td><td>β1</td><td></td><td>ββ</td><td></td><td>β4β5</td><td></td><td>ββ</td><td>C</td></tr><tr><td>0</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>1</td><td></td><td>D</td><td></td><td></td><td></td><td></td><td></td><td></td><td>12</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>3</td><td>#</td><td></td><td>12524</td><td></td><td></td><td></td><td></td><td></td><td>24 19</td></tr><tr><td>4</td><td>251</td><td>24 323</td><td>11</td><td>五</td><td>19</td><td></td><td></td><td></td><td>720 3</td></tr><tr><td>5</td><td>720 95</td><td>360 1427</td><td>30 133</td><td>360 241</td><td>720 173</td><td>3</td><td></td><td></td><td>160 863</td></tr><tr><td>6</td><td>288 19087</td><td>1440 2713</td><td>240 15487</td><td>720 586</td><td>1440 6737</td><td>160 263</td><td>863</td><td></td><td>60480 275</td></tr><tr><td></td><td>60480</td><td>2520</td><td>20160</td><td>945</td><td>20160</td><td>2520</td><td>60480</td><td></td><td>24192</td></tr><tr><td>7</td><td>5257 17280</td><td>139849 120960</td><td>4511 4480</td><td>123133 120960</td><td>88547 120960</td><td>1537 4480</td><td>11351 120960</td><td>275 24192</td><td>33953 3628800</td></tr></table>

where the error constant is equal to $\begin{array} { r } { C = \frac { 5 } { 1 2 } } \end{array}$ . The values for the Adams– Bashforth methods are given in Table 244(I) and for the Adams–Moulton methods in Table 244(II).

The Adams methods are usually implemented in ‘predictor–corrector’ form. That is, a preliminary calculation is carried out using the Bashforth form of the method. The approximate solution at a new step value is then used to evaluate an approximation to the derivative value at the new point. This derivative approximation is then used in the Moulton formula in place of the derivative at the new point. There are many alternatives as to what is done next, and we will describe just one of them. Let $y _ { n } ^ { * }$ denote the approximation to $y ( x _ { n } )$ found during the Bashforth part of the step calculation and $y _ { n }$ the improved approximation found in the Moulton part of the step. Temporarily denote by $\beta _ { i } ^ { * }$ the value of $\beta _ { i }$ in the Bashforth formula so that $\beta _ { i }$ will denote only the Moulton coefficient. The value of $k$ corresponding to the Bashforth formula will be denoted here by $k ^ { * }$ . Usually $k$ and $k ^ { * }$ are related by $k ^ { * } = k + 1$ so that both formulae have the same order $p = k + 1$ .

In the Bashforth stage of the calculation we compute

$$
y _ { n } ^ { * } = y _ { n - 1 } + h \sum _ { i = 1 } ^ { k ^ { * } } \beta _ { i } ^ { * } f ( x _ { n - i } , y _ { n - i } ) ,
$$

and in the Moulton stage

$$
y _ { n } = y _ { n - 1 } + h \beta _ { 0 } f ( x _ { n } , y _ { n } ^ { * } ) + h \sum _ { i = 1 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ) .
$$

Methods of this type are referred to as ‘predictor–corrector’ methods because the overall computation in a step consists of a preliminary prediction of the answer followed by a correction of this first predicted value. The use of (244a) and (244b) requires two calculations of the function $f$ in each step of the computation. Such a scheme is referred to as being in ‘predict–evaluate– correct–evaluate’ or ‘PECE’ mode. An alternative scheme in which the second evaluation is never performed is said to be in ‘predict–evaluate–correct’ or ‘PEC’ mode. In this mode, every occurrence of $f ( x _ { n - i } , y _ { n - i } )$ would need to be replaced by $f ( x _ { n - i } , y _ { n - i } ^ { * } )$ , and would represent the value of a derivative evaluated in a previous step but based on the predicted approximation to $y ( x _ { n - i } )$ in that step. Thus, (244a) and (244b) would be replaced by

$$
y _ { n } ^ { * } = y _ { n - 1 } + h \sum _ { i = 1 } ^ { k ^ { * } } \beta _ { i } ^ { * } f ( x _ { n - i } , y _ { n - i } ^ { * } )
$$

and

$$
y _ { n } = y _ { n - 1 } + h \beta _ { 0 } f ( x _ { n } , y _ { n } ^ { * } ) + h \sum _ { i = 1 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ^ { * } ) .
$$

In addition to PEC and PECE modes it is also possible to have PECEC and PECECE and, more generally $\mathrm { P ( E C ) } ^ { k }$ and $\mathrm { P ( E C ) } ^ { k } \mathrm { E }$ , modes, in which corrections and evaluations are done repeatedly. Using this same type of terminology, $\mathrm { P ( E C ) ^ { \infty } }$ indicates iteration to convergence.
