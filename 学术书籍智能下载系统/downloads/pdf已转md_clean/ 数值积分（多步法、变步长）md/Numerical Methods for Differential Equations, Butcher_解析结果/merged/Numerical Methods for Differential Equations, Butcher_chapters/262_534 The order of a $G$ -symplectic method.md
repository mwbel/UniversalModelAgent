# 534 The order of a $G$ -symplectic method

A second example, for the method (525d), introduced as an example of a G-symplectic method, is amenable to a similar analysis.

Theorem 534A The following method has order 4 and stage order 2:

$$
\left[ { \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} } \right] = \left[ { \frac { - { \frac { 3 + { \sqrt { 3 } } } { 6 } } } { \frac { - { \frac { 3 + { \sqrt { 3 } } } { 3 } } } { 6 } } } &  \left| { \begin{array} { c c } { 1 } & { - { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { 1 } & { { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { - { \frac { 1 } { 2 } } } \end{array} } \right|  \begin{array} { c c } { 1 } & { - { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } \\ { 1 } & { { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} } \right] .
$$

Before verifying this result we need to specify the nature of the starting method $S$ and the values of the stage abscissae, $c _ { 1 }$ and $c _ { 2 }$ . From an initial point $( x _ { 0 } , y _ { 0 } )$ , the starting value is given by

$$
\begin{array} { l } { { y _ { 1 } ^ { [ 0 ] } = y _ { 0 } , } } \\ { { { } } } \\ { { y _ { 2 } ^ { [ 0 ] } = \frac { \sqrt { 3 } } { 1 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { 0 } ) - \frac { \sqrt { 3 } } { 1 0 8 } h ^ { 4 } y ^ { ( 4 ) } ( x _ { 0 } ) + \frac { 9 + 5 \sqrt { 3 } } { 2 1 6 } h ^ { 4 } \frac { \partial f } { \partial y } y ^ { ( 3 ) } ( x _ { 0 } ) , } } \end{array}
$$

and the abscissa vector is $\begin{array} { r } { c = \left[ \frac { 1 } { 2 } + \frac { 1 } { 6 } \sqrt { 3 } \quad \frac { 1 } { 2 } - \frac { 1 } { 6 } \sqrt { 3 } \right] ^ { 1 } . } \end{array}$

Proof. Write $\xi _ { 1 }$ , $\xi _ { 2 }$ as the representations of $y _ { 1 } ^ { \left[ 0 \right] }$ , $y _ { 2 } ^ { [ 0 ] }$ and $\eta _ { 1 }$ , $\eta _ { 2 }$ to represent the stages. The stages have to be found recursively and only the converged values are given in Table 534(I), which shows the sequence of quantities occurring in the calculation. The values given for $\widehat { \xi _ { i } }$ are identical to those for $E \xi _ { i }$ , $i = 1 , 2$ , verifying that the order is 4. Furthermore $\eta _ { i } ( t ) = E ^ { ( c _ { i } ) } ( t )$ , $i = 1 , 2$ , for $r ( t ) \leq 2$ , showing stage order 2. 

Calculations to verify order $p = 4$ for (534a)   

<table><tr><td>i</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8 ：</td></tr><tr><td>ti S1</td><td>D 1</td><td>· 0</td><td>： 0</td><td>? 0</td><td>、 0</td><td>Y 0</td><td>· 0</td><td>丫 0</td><td>0</td></tr><tr><td>S</td><td>0</td><td></td><td>品</td><td>0</td><td>0</td><td></td><td></td><td>3+3</td><td>3+3</td></tr><tr><td></td><td></td><td>0 3+3</td><td>12 2+√3</td><td>9+5√3</td><td>9+5√3</td><td>18 11+6√3</td><td>36 11+6√3</td><td>36 2+√3</td><td>72 2+3</td></tr><tr><td>m1</td><td>1</td><td>6</td><td>12</td><td>36 2+√3</td><td>72</td><td>36 11+6√3</td><td>72</td><td>36</td><td>72</td></tr><tr><td>n1D</td><td>0</td><td>1</td><td>3+√3 6</td><td>6</td><td>2+√3 12</td><td>36</td><td>11+6√3 72</td><td>9+5√3 36</td><td>9+5√3 72</td></tr><tr><td>m2</td><td>1</td><td>3-3 6</td><td>2-3 12</td><td>3+5√3 36</td><td>3+5√3 72</td><td>7+6√3 36</td><td>7+6V3 72</td><td>4+3√3 36</td><td>4+3√3 72</td></tr><tr><td>n2D</td><td>0</td><td>1</td><td>3-3 6</td><td>2-3 6</td><td>2-√3 12</td><td>9-5√3 36</td><td>9-53 72</td><td>3+5√3 36</td><td>3+5√3 72</td></tr><tr><td>S</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>12</td><td>24</td></tr><tr><td>S</td><td>0</td><td>0</td><td></td><td></td><td>12</td><td>36</td><td>72</td><td>3+4v3 36</td><td>3+4√3 72</td></tr></table>
