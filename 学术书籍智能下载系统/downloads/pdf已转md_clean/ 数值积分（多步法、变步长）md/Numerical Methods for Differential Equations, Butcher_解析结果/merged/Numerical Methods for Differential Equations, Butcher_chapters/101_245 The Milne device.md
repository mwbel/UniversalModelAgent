# 245 The Milne device

A feature of predictor–corrector methods is that two approximations to $y ( x _ { n } )$ are found in each step and each of these possesses different error constants, even though they might have the same order $p$ . Denote the error constant for the Adams–Bashforth $p$ -step method, as given in Table 244(I), by $C _ { p } ^ { * }$ , and the corresponding error constant for the $( p - 1 )$ -step Adams–Moulton method, as given in Table 244(II), by $C _ { p - 1 }$ . This means that the error in $y _ { n } ^ { * }$ , assuming that previous step values are exact, is equal to

$$
y _ { n } ^ { * } = y ( x _ { n } ) - h ^ { p + 1 } C _ { p } ^ { * } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) .
$$

Of course, the previous values will not be exact, but we can interpret (245a) in the general case as the new error introduced into step $n$ . Similarly, we can interpret the corresponding formula for the error in the $( p - 1 )$ -step Adams– Moulton method as representing the error introduced into the corrected value of step $n$ . The formula for the Adams–Moulton method is

$$
y _ { n } = y ( x _ { n } ) - h ^ { p + 1 } C _ { p - 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) .
$$

By calculating the difference of the predicted and corrected approximations and multiplying by an appropriate factor, we can estimate the error in the corrected value. That is,

$$
y ( x _ { n } ) - y _ { n } \approx \frac { C _ { p - 1 } } { C _ { p - 1 } - C _ { p } ^ { * } } ( y _ { n } ^ { * } - y _ { n } ) .
$$

This device, credited to Milne (1926), is used in practical algorithms to estimate local truncation errors for stepsize control. In some modern implementations, the order of the predictor is one lower than that of the corrector, and the Milne device loses the natural significance that we have described. However, it is still found to be a useful tool for adapting a numerical computation to the behaviour of the solution.
