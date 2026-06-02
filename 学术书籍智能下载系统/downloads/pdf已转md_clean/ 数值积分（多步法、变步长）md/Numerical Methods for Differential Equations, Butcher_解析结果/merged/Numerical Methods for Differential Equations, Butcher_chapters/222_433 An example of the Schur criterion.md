# 433 An example of the Schur criterion

We first recompute the stability region of the second order Adams–Bashforth method. We need to find for what values of the complex number $z$ the polynomial $a _ { 0 } w ^ { 2 } + a _ { 1 } w + a _ { 2 }$ has its zeros in the open unit disc, where

$$
a _ { 0 } = 1 , \qquad a _ { 1 } = - 1 - { \frac { 3 } { 2 } } z , \qquad a _ { 2 } = { \frac { z } { 2 } } .
$$

The condition $| a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } > 0$ is equivalent to

$$
| z | < 2 ,
$$

while the second condition $( | a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } ) ^ { 2 } - | \overline { { { a } } } _ { 0 } a _ { 1 } - a _ { 2 } \overline { { { a } } } _ { 1 } | ^ { 2 } > 0$ simplifies to

$$
\mathrm { R e } ( z ) ( 3 | z | ^ { 2 } - 4 ) < | z | ^ { 4 } .
$$

It is easy to verify that (433b) implies (433a). Thus, by plotting the points for which (433b) holds, we recover Figure $4 3 0 ( \mathrm { i } )$ .
