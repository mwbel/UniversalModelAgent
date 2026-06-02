# 502 Runge–Kutta methods as general linear methods

Since Runge–Kutta methods have a single input, it is usually convenient to represent them, as general linear methods, with $r = 1$ . Assuming the input vector is an approximation to $y ( x _ { n - 1 } )$ , it is only necessary to write $U = { \bf 1 }$ , $V = 1$ , write $B$ as the single row $b ^ { \prime }$ of the Runge–Kutta tableau and, finally, identify $A$ with the $s \times s$ matrix of the same name also in this tableau.

A very conventional and well-known example is the classical fourth order method

$$
\begin{array}{c} { \begin{array} { r l } & { { \begin{array} { l } { 0 } \\ { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } \\ { 1 } \end{array} } } \\ & { { \begin{array} { r l } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } } \end{array} }  \\ & { { \begin{array} { r l } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } { \begin{array} { r l } { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \end{array} } } \end{array} 
$$

which, in general linear formulation, is represented by the partitioned matrix

$$
\left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } \end{array} \right] .
$$

A more interesting example is the Lobatto IIIA method for which the straightforward representation, with $s \ = \ 3$ and $r ~ = ~ 1$ , is misleading. The reason is that the method has the ‘FSAL property’ in the sense that the final stage evaluated in a step is identical with the first stage of the following step. It therefore becomes possible, and even appropriate, to use a representation with $s = r = 2$ which expresses, quite explicitly, that the FSAL property holds. This representation would be

<table><tr><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>1</td><td>NA</td></tr></table>

$$
\left[ { \frac { \frac { 1 } { 3 } } { 3 } } \quad - { \frac { 1 } { 1 2 } } \quad \left| { 1 \frac { 5 } { 1 2 } } \right. \right] ,
$$

and the input quantities are supposed to be approximations to

$$
y _ { 1 } ^ { [ n - 1 ] } \approx y ( x _ { n - 1 } ) , \quad y _ { 2 } ^ { [ n - 1 ] } \approx h y ^ { \prime } ( x _ { n - 1 } ) .
$$

Finally, we consider a Runge–Kutta method introduced in Subsection 322, with tableau

As we pointed out when the method was introduced, it can be implemented as a two-value method by replacing the computation of the second stage derivative by a quantity already computed in the previous step. The method is now not equivalent to any Runge–Kutta method but, as a general linear method, it has coefficient matrix

<table><tr><td>0 3 -2</td><td>0 0 2</td><td>0 0 0</td><td>1 0 1 1 4</td></tr><tr><td>1</td><td>2</td><td>1</td><td>1 1 1 0</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>1</td><td>0</td><td>0 0</td></tr></table>
