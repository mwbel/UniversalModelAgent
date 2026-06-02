# 44 Order and Stability Barriers

440 Survey of barrier results

It is a simple matter to construct a linear $k$ -step method with order $2 k$ . This can be done, for example, by finding coefficients $A _ { j }$ , $B _ { j }$ , $j = 0 , 1 , \ldots , k$ , such that

$$
{ \frac { 1 } { z ^ { 2 } ( z + 1 ) ^ { 2 } ( z + 2 ) ^ { 2 } \cdots ( z + k ) ^ { 2 } } } = \sum _ { j = 0 } ^ { k } { \frac { A _ { j } } { z + j } } + \sum _ { j = 0 } ^ { k } { \frac { B _ { j } } { ( z + j ) ^ { 2 } } }
$$

and then defining

$$
\alpha _ { j } = - { \frac { A _ { j } } { A _ { 0 } } } , \quad j = 1 , 2 , \ldots , k , \qquad \beta _ { j } = { \frac { B _ { j } } { A _ { 0 } } } , \quad j = 0 , 1 , \ldots , k .
$$

To justify this remark, consider the contour integral

$$
{ \frac { 1 } { 2 \pi i } } \oint _ { C } { \frac { \phi ( z ) d z } { \prod _ { j = 0 } ^ { k } ( z + j ) ^ { 2 } } } = \sum _ { j = 0 } ^ { k } { \frac { 1 } { 2 \pi i } } \oint _ { C } \phi ( z ) \left( { \frac { A _ { j } } { z + j } } + { \frac { B _ { j } } { ( z + j ) ^ { 2 } } } \right) d z ,
$$

where the contour $C$ consists of a counter-clockwise circle of radius $R > k$ and centre at the origin and $\phi$ is a polynomial of degree not exceeding $2 k$ . By

taking $R$ large the value of the integral can be estimated by $O ( R ^ { - 1 } )$ ; because it is constant, it must be zero. On the other hand, the terms in the partial fraction representation of the integral are

$$
\sum _ { j = 0 } ^ { k } \left( A _ { j } \phi ( - j ) + B _ { j } \phi ^ { \prime } ( - j ) \right) .
$$

For example, if $k = 3$ , we have

$$
\begin{array} { r c l } { \displaystyle { \frac { 1 } { z ^ { 2 } ( z + 1 ) ^ { 2 } ( z + 2 ) ^ { 2 } } = - \frac { 1 1 } { 1 0 8 } \frac { 1 } { z } - \frac { 1 } { 4 } \frac { 1 } { z + 1 } + \frac { 1 } { 4 } \frac { 1 } { z + 2 } + \frac { 1 1 } { 1 0 8 } \frac { 1 } { z + 3 } } } \\ { \displaystyle { + \frac { 1 } { 3 6 } \frac { 1 } { z ^ { 2 } } + \frac { 1 } { 4 } \frac { 1 } { ( z + 1 ) ^ { 2 } } + \frac { 1 } { 4 } \frac { 1 } { ( z + 2 ) ^ { 2 } } + \frac { 1 } { 3 6 } \frac { 1 } { ( z + 3 ) ^ { 2 } } , } } \end{array}
$$

leading to the values

$$
\alpha _ { 1 } = - \frac { 2 7 } { 1 1 } , \quad \alpha _ { 2 } = \frac { 2 7 } { 1 1 } , \quad \alpha _ { 3 } = 1 ,
$$

so that the method is unstable.

This is an example of a result found by Dahlquist (1956), that order $p$ is impossible for a convergent method unless $p \leq k + 1$ if $k$ is odd, and $p \leq k + 2$ if $k$ is even.

With the recognition of the importance of stiffness came the property of A-stability (Dahlquist, 1963). It has been shown, also by Dahlquist, for Astable linear multistep methods that $p$ cannot exceed 2. This result is known as the second Dahlquist barrier, in contrast to the result about the order of a convergent $k$ -step method, which is usually referred to as the first Dahlquist barrier.
