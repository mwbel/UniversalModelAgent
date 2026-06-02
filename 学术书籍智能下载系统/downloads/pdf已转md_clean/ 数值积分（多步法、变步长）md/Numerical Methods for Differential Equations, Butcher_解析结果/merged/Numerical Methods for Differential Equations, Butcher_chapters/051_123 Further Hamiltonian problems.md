# 123 Further Hamiltonian problems

In the Hamiltonian formulation of classical mechanics, generalized coordinates $q _ { 1 }$ , $q _ { 2 }$ , . . . , $q _ { N }$ and generalized momenta $p _ { 1 }$ , $p _ { 2 }$ , $\cdot \cdot \cdot$ , $p _ { N }$ are used to represent the state of a mechanical system. The equations of motion are defined in terms

of a ‘Hamiltonian’ function $H ( p _ { 1 } , p _ { 2 } , \ldots , p _ { N } , q _ { 1 } , q _ { 2 } , \ldots , q _ { N } )$ by the equations

$$
\begin{array} { l } { { \displaystyle p _ { i } ^ { \prime } = - \frac { \partial H } { \partial q _ { i } } , } } \\ { { \displaystyle q _ { i } ^ { \prime } = \frac { \partial H } { \partial p _ { i } } . } } \end{array}
$$

Write $y ( x )$ as a vector variable, made up from $N$ momenta followed by the $N$ coordinates. That is,

$$
\begin{array} { r } { y _ { i } = \left\{ \begin{array} { l l } { p _ { i } , \quad \quad \quad 1 \leq i \leq N , } \\ { q _ { i - N } , \quad N + 1 \leq i \leq 2 N . } \end{array} \right. } \end{array}
$$

With the understanding that $H$ is regarded as a function of $y$ , the differential equations can be written in the form $y ^ { \prime } = f ( y )$ , where

$$
\boldsymbol { f } ( \boldsymbol { y } ) = \boldsymbol { J } \boldsymbol { \nabla } ( \boldsymbol { H } ) , \qquad \boldsymbol { J } = \left[ \begin{array} { l l } { 0 } & { - \boldsymbol { I } } \\ { \boldsymbol { I } } & { \ 0 } \end{array} \right] ,
$$

in which $I$ is the $N \times N$ unit matrix.

Theorem 123A $H ( y ( x ) )$ is invariant.

Proof. Calculate $\partial H / \partial y$ to obtain the result

The Jacobian of this problem is equal to

$$
\frac { \partial } { \partial y } f ( y ) = \frac { \partial } { \partial y } \left( J \nabla ( H ) \right) = J W ( y ) ,
$$

where $W$ is the ‘Wronskian’ matrix defined as the $2 N \times 2 N$ matrix with $( i , j )$ element equal to $\partial ^ { 2 } H / \partial y _ { i } \partial y _ { j }$ .

If the initial value $y _ { 0 } = y ( x _ { 0 } )$ is perturbed by a small number $\epsilon$ multiplied by a fixed vector $v _ { 0 }$ , then, to within $O ( \epsilon ^ { 2 } )$ , the solution is modified by $\epsilon v + O ( \epsilon ^ { 2 } )$ where

$$
v ^ { \prime } ( x ) = \frac { \partial f } { \partial y } v ( x ) = J W ( y ) v ( x ) .
$$

For two such perturbations $u$ and $\boldsymbol { v }$ , it is interesting to consider the value of the scalar $u ^ { \intercal } J v$ .

This satisfies the differential equation

$$
\frac { d } { d x } u ^ { \top } J v = u ^ { \top } J J W v + ( J W u ) ^ { \top } J v = - u ^ { \top } W v + u ^ { \top } W v = 0 .
$$

Hence we have:

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/dadda48945c747f8d40cffb4f8c1d188edcdbf33b3e86a65ad2e5edd43f4de68.jpg)  
Illustration of symplectic behaviour for $H ( p , q ) = p ^ { 2 } / 2 + q ^ { 2 } / 2$ (left) and $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ (right). The underlying image depicts the North Island brown kiwi, Apteryx mantelli.

# Theorem 123B $u ^ { \intercal } J v$ is invariant with time.

In the special case of a two-dimensional Hamiltonian problem, the value of $\left( \epsilon u \right) ^ { \prime } J ( \epsilon v )$ can be interpreted as the area of the infinitesimal parallelogram with sides in the directions $u$ and $v$ . As the solution evolves, $u$ and $v$ might change, but the area $u ^ { \prime } J v$ remains invariant. This is illustrated in Figure 123(i) for the two problems $H ( p , q ) = p ^ { 2 } / 2 + q ^ { 2 } / 2$ and $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ respectively.
