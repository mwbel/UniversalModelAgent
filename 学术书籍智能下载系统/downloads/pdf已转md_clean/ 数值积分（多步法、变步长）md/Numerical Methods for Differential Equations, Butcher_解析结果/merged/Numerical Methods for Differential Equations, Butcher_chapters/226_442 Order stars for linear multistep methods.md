# 442 Order stars for linear multistep methods

In their historic paper, Wanner, Hairer and Nørsett (1978) introduced order stars on Riemann surfaces. Suppose that $\Phi ( w , z )$ is a polynomial function of two complex variables, $w \in W$ and $z \in Z$ . We assume that $Z = W = \mathbb { C }$ . The subset $R _ { \Phi }$ of $W \times Z$ defined by the relation $\Phi ( w , z ) = 0$ is a Riemann surface. Suppose that $\Phi$ has degree $r$ in $w$ and $s$ in $z$ . We may interpret $R$ as a mapping from the $Z$ plane which takes $z \in { Z }$ to the set of zeros of the equation $\Phi ( w , z ) = 0$ or as a mapping which takes $w \in W$ to the set of zeros of this same equation, but with $z$ now the unknown. The main interpretation will be that $\Phi ( w , z )$ is the characteristic polynomial $\operatorname* { d e t } ( w I - M ( z ) )$ of the stability matrix of a multivalue method. If this method has order $p$ then $\Phi ( \exp ( z ) , z ) = O ( z ^ { p + 1 } )$ . For ease of notation, we carry over concepts such as A-stability from multivalue methods, such as linear multistep methods, to the functions $\Phi$ used to characterize their stability.

Definition 442A The function $\Phi$ is $A$ -stable if $R _ { \Phi }$ has no intersection with the product set

$$
\{ w \in \mathbb { C } : | w | > 1 \} \times \{ z \in \mathbb { C } : \operatorname { R e } ( z ) \leq 0 \} .
$$

This definition is equivalent to the requirement that for any $z$ in the left half complex plane, all eigenvalues of the stability matrix are in the closed unit disc. Just as in the case of Runge–Kutta methods, for which the Riemann surface has only a single sheet, scaling the eigenvalues by $\exp ( - z )$ does not affect the behaviour on the imaginary axis or introduce or remove any poles.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/0d5fc24ca6cf5d995f03160f55bab594736148e18421141a0290f12ec0ea53b7.jpg)  
Order star for the second order BDF method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0006_pages_0351-0420/auto/images/42453fafe8af643434068c41b8d3e62c41328cb2941911853571121924744803.jpg)  
Order star for the third order BDF method

Hence we can consider a modified Riemann surface based on the function $\Phi ( w \exp ( z ) , z )$ . Just as for the Runge–Kutta case, one of the sheets, known as the ‘principal sheet’, behaves like $w = 1 + O ( z ^ { p + 1 } )$ and order stars appear.

We illustrate this by considering the case of the second order backward difference method, for which

$$
\Phi ( w \exp ( z ) , z ) = \left( 1 - \frac { 2 } { 3 } z \right) \exp ( 2 z ) w ^ { 2 } - \frac { 4 } { 3 } \exp ( z ) w + \frac { 1 } { 3 } ,
$$

and the third order backward difference method, for which

$$
{ \mathfrak { s } } ( w \exp ( z ) , z ) = \left( 1 - { \frac { 6 } { 1 1 } } z \right) \exp ( 3 z ) w ^ { 3 } - { \frac { 1 8 } { 1 1 } } \exp ( 2 z ) w ^ { 2 } + { \frac { 9 } { 1 1 } } \exp ( z ) w - { \frac { 2 } { 1 1 } } .
$$

For the second order case, shown in Figure 442(i), a pole at $\begin{array} { r } { z = \frac { 3 } { 2 } } \end{array}$ is marked, together with a branch point at $\begin{array} { r } { z = - \frac { 1 } { 2 } } \end{array}$ . Note that for $z \in ( \infty , - \frac { 1 } { 2 } )$ , the two roots of the equation $\Phi ( w \exp ( z ) , z ) = 0$ , for all $z$ in this real interval, have equal magnitudes. In this figure, light shading grey indicates that a region has exactly one of the sheets with magnitude greater than 1. A darker grey is used to indicate that both sheets have magnitudes greater than 1.

This method is A-stable, as we already know. This can be seen from the order star by noting that the only pole is in the right half-plane, and that the fingers do not intersect the imaginary axis. On the other hand, the third order method (Figure 442(ii)) is not A-stable because, in this case, the intersection of the imaginary axis with one the fingers is now not empty. Note that for the third order case, there is a single pole at $\begin{array} { r } { z = \frac { 1 1 } { 6 } } \end{array}$ and that three shades of grey are used to distinguish regions where one, two or three sheets have magnitudes greater than 1.

Although A-stable Runge–Kutta methods can have arbitrarily high orders, the order of A-stable linear multistep methods is restricted to 2. This was first proved using order stars (Wanner, Hairer and Nørsett, 1978), but we will use the closely related approach of order arrows (Butcher, 2002). These will be introduced in the Riemann surface case in the next subsection.
