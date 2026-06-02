# 211 Local truncation error

In a single step of the Euler method, the computed result, $y _ { 0 } + h f ( x _ { 0 } , y _ { 0 } )$ , differs from the exact answer by

$$
y ( x _ { 0 } + h ) - y ( x _ { 0 } ) - h f ( x _ { 0 } , y ( x _ { 0 } ) ) = y ( x _ { 0 } + h ) - y ( x _ { 0 } ) - h y ^ { \prime } ( x _ { 0 } ) .
$$

Assuming $y$ has continuous first and second derivatives, this can be written in the form

$$
h ^ { 2 } \int _ { 0 } ^ { 1 } ( 1 - s ) y ^ { \prime \prime } ( x _ { 0 } + h s ) d s .
$$

For $i ~ = ~ 1 , 2 , \ldots , N$ , component $i$ can be written, using the mean value theorem, as ${ \scriptstyle { \frac { 1 } { 2 } } } h ^ { 2 }$ times component $i$ of $y ^ { \prime \prime } ( x _ { 0 } + h s ^ { * } )$ , where $s ^ { * }$ is in the interval $( 0 , 1 )$ . Another way of writing the error, assuming that third derivatives also exist and are bounded, is

$$
{ \frac { 1 } { 2 } } h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) + { \cal O } ( h ^ { 3 } ) .
$$

This form of the error estimate is quite convenient for interpreting numerically produced results, because if $h$ is sufficiently small, the local error will appear to behave like a constant vector multiplied by $h ^ { 2 }$ . It is also useful for determining how stepsize control should be managed.
