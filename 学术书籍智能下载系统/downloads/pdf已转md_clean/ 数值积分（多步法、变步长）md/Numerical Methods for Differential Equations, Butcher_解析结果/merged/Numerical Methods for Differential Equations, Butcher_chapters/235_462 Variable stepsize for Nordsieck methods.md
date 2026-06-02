# 462 Variable stepsize for Nordsieck methods

The motivation we have presented for the choice of $\gamma _ { 1 }$ , $\gamma _ { 2 }$ , . . . in the formulation of Nordsieck methods was to require a certain matrix to have zero spectral radius. Denote the vector $\gamma$ and the matrix $V$ by

$$
\gamma = \left[ \begin{array} { c } { \gamma _ { 1 } } \\ { \gamma _ { 2 } } \\ { \vdots } \\ { \gamma _ { p } } \end{array} \right] , \quad \quad V = \left[ \begin{array} { c c c c c } { 1 } & { 2 } & { 3 } & { \cdots } & { p } \\ { 0 } & { 1 } & { 3 } & { \cdots } & { \frac { 1 } { 2 } p ( p - 1 ) } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { \frac { 1 } { 6 } p ( p - 1 ) ( p - 2 ) } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } \end{array} \right] ,
$$

and denote by $e _ { 1 } ^ { \mathsf { T } }$ the basis row vector $e _ { 1 } ^ { \mathsf { T } } = [ 1 \quad 0 \quad \cdot \cdot \quad 0 ]$ . The characteristic property of $\gamma$ is that the matrix

$$
( I - \gamma e _ { 1 } ^ { \mathsf { T } } ) V
$$

has zero spectral radius. When variable stepsize is introduced, the matrix in (462a) is multiplied by $D ( r ) = \mathrm { d i a g } ( r , r ^ { 2 } , r ^ { 3 } , \ldots , r ^ { p } )$ and, as we have seen, if $\gamma$ is chosen on the basis of constant $h$ , there is a deterioration in stable behaviour. We consider the alternative of choosing $\gamma$ as a function of $r$ so that

$$
\rho ( D ( r ) ( I - \gamma e _ { 1 } ^ { \mathsf { T } } ) V ) = 0 .
$$

The value of $\gamma _ { 1 }$ still retains the value 1 but, in the only example we consider, $p = 3$ , it is found that

$$
\gamma _ { 2 } = \frac { 1 + 2 r } { 2 ( 1 + r ) } , \qquad \gamma _ { 3 } = \frac { r } { 3 ( 1 + r ) } ,
$$

and we have

$$
D ( r ) ( I - \gamma e _ { 1 } ^ { \intercal } ) V = \left[ \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { - \frac { r ^ { 3 } } { 1 + r } } & { \frac { 3 r ^ { 2 } } { 2 ( 1 + r ) } } \\ { 0 } & { - \frac { 2 r ^ { 4 } } { 3 ( 1 + r ) } } & { \frac { r ^ { 3 } } { 2 ( 1 + r ) } } \end{array} \right] .
$$

It is obvious that this matrix is power-bounded for all positive values of $r$ . However, if a sequence of $n$ steps is carried out with stepsize changes $r _ { 1 }$ , $r _ { 2 }$ , . . . , $r _ { n }$ then the product of matrices of the form given by (462b) for these values of $r$ to be analysed to determine stability. The spectral radius of such a product is found to be

$$
\frac { | r _ { 1 } - r _ { n } | r _ { 1 } ^ { 2 } } { 1 + r _ { 1 } } \cdot \frac { | r _ { 2 } - r _ { 1 } | r _ { 2 } ^ { 2 } } { 1 + r _ { 2 } } \cdot \frac { | r _ { 3 } - r _ { 2 } | r _ { 3 } ^ { 2 } } { 1 + r _ { 3 } } \cdot \cdot \cdot \frac { | r _ { n } - r _ { n - 1 } | r _ { n } ^ { 2 } } { 1 + r _ { n } } ,
$$

and this will be bounded by 1 as long as $r _ { i } \in [ 0 , r ^ { \star } ]$ , where $r ^ { \star }$ has the property that

$$
\frac { r _ { 1 } r _ { 2 } | r _ { 2 } - r _ { 1 } | } { \sqrt { ( 1 + r _ { 1 } ) ( 1 + r _ { 2 } ) } } \leq 1 , \quad \mathrm { w h e n e v e r ~ } r _ { 1 } , r _ { 2 } \in [ 0 , r ^ { \star } ] .
$$

It is found after some calculations that stability, in the sense of this discussion, is achieved if $r ^ { \star } \approx 2 . 1 5 9 5 4 5 4 3$ .
