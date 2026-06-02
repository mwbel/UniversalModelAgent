# 372 Order conditions

Given rooted trees $t$ , $u$ and a symplectic Runge–Kutta method, we consider the relationship between the elementary weights $\phi ( t u ) , \phi ( u t ) , \phi ( t ) , \phi ( u )$ . Write

$$
\Phi ( t ) = \sum _ { i = 1 } b _ { i } \phi _ { i } , \quad \Phi ( u ) = \sum _ { i = 1 } b _ { i } \psi _ { i } .
$$

Then we find

$$
\begin{array} { l } { \displaystyle \Phi ( t u ) = \sum _ { i , j = 1 } ^ { s } b _ { i } \phi _ { i } a _ { i j } \psi _ { j } , } \\ { \displaystyle \Phi ( u t ) = \sum _ { i , j = 1 } ^ { s } b _ { j } \psi _ { j } a _ { j i } \phi _ { i } , } \end{array}
$$

so that

$$
\begin{array} { l } { \displaystyle \Phi ( t u ) + \Phi ( u t ) = \sum _ { i , j = 1 } ^ { s } ( b _ { i } a _ { i j } + b _ { j } a _ { j i } ) \phi _ { i } \psi _ { j } } \\ { \displaystyle \qquad = \sum _ { i , j = 1 } ^ { s } ( b _ { i } b _ { j } ) \phi _ { i } \psi _ { j } } \\ { \displaystyle \qquad = \Phi ( t ) \Phi ( u ) . } \end{array}
$$

Assuming the order conditions $\Phi ( t ) = 1 / \gamma ( t )$ and $\Phi ( u ) = 1 / \gamma ( u )$ are satisfied, then

$$
\Phi ( t u ) - \frac { 1 } { \gamma ( t u ) } + \Phi ( u t ) - \frac { 1 } { \gamma ( u t ) } = 0 .
$$

Using this fact, we can prove the following theorem:

Theorem 372A Let $( A , b ^ { \prime } , c )$ be a symplectic Runge–Kutta method. The method has order $p$ if and only if for each non-superfluous tree and any vertex in this tree as root, $\Phi ( t ) = 1 / \gamma ( t )$ , where $t$ is the rooted tree with this vertex.

Proof. We need only to prove the sufficiency of this criterion. If two rooted trees belong to the same tree but have vertices $v _ { 0 }$ , $\widehat { v }$ say, then there is a sequence of vertices $v _ { 0 }$ , $v _ { 1 }$ , $\cdot \cdot \cdot$ , $v _ { m } = \widehat { v }$ , such that $v _ { i - 1 }$ and $v _ { i }$ are adjacent for $i = 1 , 2 , \dots , m$ . This mean that rooted trees $t , u$ exist such that $t u$ is the rooted tree with root $v _ { i - 1 }$ and $u t$ is the rooted tree with root $v _ { i }$ . We are implicitly using induction on the order of trees and hence we can assume that $\Phi ( t ) = 1 / \gamma ( t )$ and $\Phi ( u ) = 1 / \gamma ( u )$ . Hence, if one of the order conditions for the trees $t u$ and $u t$ is satisfied, then the other is. By working along the chain of possible roots $v _ { 0 } , v _ { 1 } , \ldots , v _ { m }$ , we see that the order condition associated with the root $v _ { 0 }$ is equivalent to the condition for $\widehat { v }$ . In the case of superfluous trees, one choice of adjacent vertices would imply that $t = u$ . Hence, (372a) is equivalent to $2 \Phi ( t t ) = 2 / \gamma ( t t )$ so that the order condition associated with $t t$ is satisfied and all rooted trees belonging to the same tree are also satisfied.

The first experiment uses the simple pendulum based on the Hamiltonian $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ and initial value $\left( p , q \right) = \left( 1 , 0 \right)$ . The amplitude is found to be $\pi / 3 \approx 1 . 0 4 7 1 9 8$ and the period to be approximately 6.743001. Numerical solutions, displayed in Figure 373(i), were found using the Euler, implicit Euler and the implicit mid-point rule methods. Only the last of these is symplectic and its behaviour reflects this. That is, like the exact solution which is also shown, the area of the initial set remains unchanged, even though its shape is distorted.

The second experiment is based on problem (122c), which evolves on the unit sphere $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1$ . The value of $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 }$ is calculated by the Euler method, the implicit Euler method and the implicit mid-point rule method. Only the last of these is symplectic. The computed results are shown in Figure 373(ii). In each case a stepsize $h = 0 . 1$ was used. Although results are shown for only 500 time steps, the actual experiment was extended much further. There is no perceptible deviation from $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } + y _ { 3 } ^ { 2 } = 1$ for the first million steps.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0005_pages_0281-0350/auto/images/83a6e1ff135a200883a79c61d1e2a5fd54639e36ae4148227af8a545daa4bdd1.jpg)  
Solutions of the Hamiltonian problem $H ( p , q ) = p ^ { 2 } / 2 - \cos ( q )$ . Left: Euler method (grey) and implicit Euler method (white). Right: exact solution (grey) and implicit mid-point method (white). The underlying image depicts the takahe Porphyrio hochstetteri, rediscovered in 1948 after many years of presumed extinction.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0005_pages_0281-0350/auto/images/49ea0f5ff0444cf6688a2b9cb532cb3bfd5aa23c33b768de46a5533e41ed7d97.jpg)  
Experiments for problem (122c). The computed value of $\| y _ { n } \| ^ { 2 }$ is shown after $n = 1 , 2 , \ldots$ , steps.

# Exercises 37

37.1 Do two-stage symplectic Runge–Kutta methods exist which have order 3 but not order 4?

37.2 Do three-stage order 3 symplectic Runge–Kutta methods exist for which $A$ is lower triangular?
