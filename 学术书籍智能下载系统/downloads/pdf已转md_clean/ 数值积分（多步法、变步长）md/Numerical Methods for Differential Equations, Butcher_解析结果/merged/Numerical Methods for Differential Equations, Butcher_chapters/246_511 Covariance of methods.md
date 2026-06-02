# 511 Covariance of methods

Assume the interpretation of a method is agreed to, at least in terms of the choice of the preconsistency vector. We want to ensure that numerical approximations are transformed appropriately by a shift of origin. Consider the two initial value problems

$$
\begin{array} { r l r l } & { \boldsymbol { y } ^ { \prime } ( \boldsymbol { x } ) = f ( \boldsymbol { y } ( \boldsymbol { x } ) ) , } & & { \boldsymbol { y } ( x _ { 0 } ) = y _ { 0 } , } \\ & { \boldsymbol { z } ^ { \prime } ( \boldsymbol { x } ) = f ( \boldsymbol { z } ( \boldsymbol { x } ) - \boldsymbol { \eta } ) , } & & { \boldsymbol { z } ( x _ { 0 } ) = y _ { 0 } + \boldsymbol { \eta } , } \end{array}
$$

where $\eta \in \mathbb { R } ^ { N }$ is arbitrary. If (511a) has a solution, then (511b) also has a solution, which is identical to the former solution except that each point on the trajectory is translated by $\eta$ . If the solution is required at some $\overline { { x } } > x _ { 0 }$ , then the solution to (511a) at this point can be found by subtracting $\eta$ from the solution of (511b).

When each of these problems is solved by a numerical method, it is natural to expect that the numerical approximations should undergo the same covariance rule as for the exact solution. This means that in a single step of a method $( A , U , B , V )$ , interpreted as having a preconsistency vector $u$ , we want to be able to shift component $i$ of $y ^ { [ 0 ] }$ by $u _ { i } \eta$ , for all $i = 1 , 2 , \dots , r$ , and be assured that component $i$ of $y ^ { [ 1 ] }$ is also shifted by the same amount. At the same time the internal approximations (the stage values) should be shifted by $\eta$ . Of course no shift will take place to the stage derivatives.

The idea of covariance is illustrated in Figure 511(i). For an initial value problem $( f , y _ { 0 } )$ as given by (511a), the operation $\nu$ represents the computation of a numerical approximation to the solution on an interval $[ x _ { 0 } , { \overline { { x } } } ]$ , or at a single value of $x$ . Furthermore, $\sigma$ represents a shift of coordinates by a specific vector $\eta$ , as in the transformation to the problem (511b). Covariance is just the statement that the diagram in Figure 511(i) commutes, that is, that $\sigma \circ \nu = \nu \circ \sigma$ . The diagonal arrow representing these equal composed functions corresponds to the operation of solving the problem and then shifting coordinates, or else shifting first and then solving.

The covariance of the output values is equivalent to (510a) and the covariance of the stage values is equivalent to (510b). We have no interest in methods that are not covariant even though it is possible to construct artificial methods which do not have this property but can still yield satisfactory numerical results.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/b2580a2d7e659c1a9ddbfac42031cd27cecd59487aa604e169006e0b0c7535d3.jpg)  
A commutative diagram for covariance
