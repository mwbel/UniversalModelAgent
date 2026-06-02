# 133 Three quadratic problems

We consider the solutions to the problems

$$
\begin{array} { l } { y _ { n } = y _ { n - 1 } ^ { 2 } , } \\ { y _ { n } = y _ { n - 1 } ^ { 2 } - 2 , } \\ { y _ { n } = y _ { n - 1 } y _ { n - 2 } . } \end{array}
$$

If $z _ { n } = \ln ( y _ { n } )$ in (133a), then $z _ { n } = 2 z _ { n - 1 }$ with solution $z _ { n } = 2 ^ { n } z _ { 0 }$ . Hence, the general solution to (133a) is

$$
y _ { n } = y _ { 0 } ^ { 2 ^ { n } } .
$$

To solve (133b), substitute $y _ { n } = z _ { n } + z _ { n } ^ { - 1 }$ , so that

$$
z _ { n } + \frac { 1 } { z _ { n } } = z _ { n - 1 } ^ { 2 } + \frac { 1 } { z _ { n - 1 } ^ { 2 } } ,
$$

and this is satisfied by any solution to $z _ { n } = z _ { n - 1 } ^ { 2 }$ . Hence, using the known solution of (133a), we find

$$
y _ { n } = z _ { 0 } ^ { 2 ^ { n } } + z _ { 0 } ^ { - 2 ^ { n } } ,
$$

where $z _ { 0 }$ is one of the solutions to the equation

$$
z _ { 0 } + { \frac { 1 } { z _ { 0 } } } = y _ { 0 } .
$$

Finally, to solve (133c), substitute $z _ { n } = \ln ( y _ { n } )$ , and we find that

$$
z _ { n } = z _ { n - 1 } + z _ { n - 2 } .
$$

The general solution to this is found from the Fibonacci equation, so that substituting back in terms of $y _ { n }$ , we find

$$
y _ { n } = A ^ { \left( { \frac { 1 } { 2 } } ( 1 + { \sqrt { 5 } } ) \right) ^ { n } } \cdot B ^ { \left( { \frac { 1 } { 2 } } ( 1 - { \sqrt { 5 } } ) \right) ^ { n } } ,
$$

with $A$ and $B$ determined from the initial values.
