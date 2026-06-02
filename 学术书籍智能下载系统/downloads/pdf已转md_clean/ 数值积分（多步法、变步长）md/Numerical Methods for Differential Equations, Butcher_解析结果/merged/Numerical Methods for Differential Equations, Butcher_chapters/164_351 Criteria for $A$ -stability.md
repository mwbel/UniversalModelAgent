# 351 Criteria for $A$ -stability

We first find an alternative expression for the rational function (350a).

Lemma 351A Let $( A , b , c )$ denote a Runge–Kutta method. Then its stability function is given by

$$
R ( z ) = \frac { \operatorname* { d e t } \left( I + z ( \mathbf { 1 } b ^ { \intercal } - A ) \right) } { \operatorname* { d e t } ( I - z A ) } .
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/690e3faa45b81170a17aa11fe62c25aaa19bbb6d6d05478e2f1d8e6565fb4688.jpg)  
Figure 350(i) $\mathrm { A } ( \alpha )$ stability region for the method (350c)

Proof. Because a rank 1 $s \times s$ matrix $u v ^ { \top }$ has characteristic polynomial $\operatorname* { d e t } ( I w - u v ^ { \intercal } ) = w ^ { s - 1 } ( w - v ^ { \intercal } u )$ , a matrix of the form $I + u v ^ { \prime }$ has characteristic polynomial $( w - 1 ) ^ { s - 1 } ( w - 1 - v ^ { \mathsf { I } } u )$ and determinant of the form $1 + v ^ { \intercal } u .$ Hence,

$$
\operatorname* { d e t } \left( I + z \mathbf { 1 } b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \right) = 1 + z b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \mathbf { 1 } = R ( z ) .
$$

We now note that

$$
I + z ( \mathbf { 1 } b ^ { \mathsf { T } } - A ) = \left( I + z \mathbf { 1 } b ^ { \mathsf { T } } ( I - z A ) ^ { - 1 } \right) ( I - z A ) ,
$$

so that

$$
\operatorname* { d e t } \left( I + z ( \mathbf { 1 } b ^ { \intercal } - A ) \right) = R ( z ) \operatorname* { d e t } ( I - z A ) .
$$

Now write the stability function of a Runge–Kutta method as the ratio of two polynomials

$$
R ( z ) = { \frac { N ( z ) } { D ( z ) } }
$$

and define the E-polynomial by

$$
E ( y ) = D ( i y ) D ( - i y ) - N ( i y ) N ( - i y ) .
$$

Theorem 351B A Runge–Kutta method with stability function $\begin{array} { r l } { R ( z ) } & { { } = } \end{array}$ $N ( z ) / D ( z )$ is A-stable if and only if (a) all poles of $R$ (that is, all zeros of $D$ ) are in the right half-plane and (b) $E ( y ) \ge 0$ , for all real $y$ .

Proof. The necessity of (a) follows from the fact that if $z ^ { * }$ is a pole then $\begin{array} { r } { \operatorname* { l i m } _ { z \to z ^ { * } } | R ( z ) | = \infty } \end{array}$ , and hence $| R ( z ) | > 1$ , for $z$ close enough to $z ^ { * }$ . The necessity of (b) follows from the fact that $E ( y ) < 0$ implies that $| R ( i y ) | > 1$ , so that $| R ( z ) | > 1$ for some $z = - \epsilon + i y$ in the left half-plane. Sufficiency of these conditions follows from the fact that (a) implies that $R$ is analytic in the left half-plane so that, by the maximum modulus principle, $| R ( z ) | > 1$ in this region implies $| R ( z ) | > 1$ on the imaginary axis, which contradicts (b). $\boxed { \begin{array} { r l } \end{array} }$
