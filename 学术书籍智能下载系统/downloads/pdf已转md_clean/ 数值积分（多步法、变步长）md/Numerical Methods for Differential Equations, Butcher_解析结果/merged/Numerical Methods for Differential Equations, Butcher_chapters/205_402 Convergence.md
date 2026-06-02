# 402 Convergence

We consider the approximation of $y ( { \overline { { x } } } )$ by a linear multistep method, with $h = ( \overline { { x } } - x _ { 0 } ) / m$ , using initial values

$$
\begin{array} { l } { { y _ { 0 } } = \phi _ { 0 } { \left( y ( { x _ { 0 } } ) , h \right) } , } \\ { { y _ { 1 } } = \phi _ { 1 } { \left( y ( { x _ { 0 } } ) , h \right) } , } \\ { { \mathrm { ~ } } } \\ { { \vdots \qquad \vdots } } \\ { { y _ { k - 1 } } = \phi _ { k - 1 } { \left( y ( { x _ { 0 } } ) , h \right) } . } \end{array}
$$

After the initial values have been evaluated, the values of $y _ { n }$ , for $n =$ $k , k + 1 , \ldots , m$ , are found in turn, using the linear $k$ -step method $[ \alpha , \beta ]$ . It is assumed that for $i = 1 , 2 , \ldots , k - 1$ ,

$$
\left\| \phi _ { i } \left( y ( x _ { 0 } ) , h \right) - y ( x _ { 0 } ) \right\| \to 0 , \quad { \mathrm { ~ a s ~ } } h \to 0 .
$$

Definition 402A Consider a linear multistep method used with a starting method as described in the previous discussion. Let $Y _ { m }$ denote the approximation to $y ( { \overline { { x } } } )$ found using $_ { T I l }$ steps with $h = ( \overline { { x } } - x _ { 0 } ) / m$ . The function $f$ is assumed to be continuous and to satisfy a Lipschitz condition in its second variable. The linear multistep method is said to be ‘convergent’ if, for any such initial value problem,

$$
\| Y _ { m } - y ( { \overline { { x } } } ) \| \to 0 , \ a s \ m \to \infty .
$$
