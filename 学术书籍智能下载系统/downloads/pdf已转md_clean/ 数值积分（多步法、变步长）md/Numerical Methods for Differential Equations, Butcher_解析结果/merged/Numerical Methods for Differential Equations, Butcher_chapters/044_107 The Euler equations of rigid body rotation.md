# 107 The Euler equations of rigid body rotation

For a rigid body on which no moments are acting, the three components of angular velocity, in terms of the principal directions of inertia fixed in the

body, satisfy the Euler equations:

$$
\begin{array} { r } { I _ { 1 } \cfrac { d w _ { 1 } } { d t } = ( I _ { 2 } - I _ { 3 } ) w _ { 2 } w _ { 3 } , } \\ { I _ { 2 } \cfrac { d w _ { 2 } } { d t } = ( I _ { 3 } - I _ { 1 } ) w _ { 3 } w _ { 1 } , } \\ { I _ { 3 } \cfrac { d w _ { 3 } } { d t } = ( I _ { 1 } - I _ { 2 } ) w _ { 1 } w _ { 2 } , } \end{array}
$$

where the ‘principal moments of inertia’ $I _ { 1 }$ , $I _ { 2 }$ and $I _ { 3 }$ are positive. Denote the kinetic energy by $\scriptstyle { \frac { 1 } { 2 } } E$ and the squared norm of the angular momentum by $F$ . That is,

$$
\begin{array} { r } { E = I _ { 1 } w _ { 1 } ^ { 2 } + I _ { 2 } w _ { 2 } ^ { 2 } + I _ { 3 } w _ { 3 } ^ { 2 } , } \\ { F = I _ { 1 } ^ { 2 } w _ { 1 } ^ { 2 } + I _ { 2 } ^ { 2 } w _ { 2 } ^ { 2 } + I _ { 3 } ^ { 2 } w _ { 3 } ^ { 2 } . } \end{array}
$$

Differentiate these expressions and substitute in $d w _ { i } / d t$ , $i = 1 , 2 , 3$ , to obtain a zero result in each case. Hence, $E$ and $F ^ { \dagger }$ are invariants of the solution to (107a). This observation provides useful tests on numerical methods for this problem because there is in general no reason why these invariants should be maintained in a numerical approximation.

# Exercises 10

10.1 You are given the initial value problem

$$
u ^ { \prime \prime \prime } ( x ) - 3 u ^ { \prime \prime } ( x ) + 2 u ( x ) u ^ { \prime } ( x ) = 0 , \quad u ( 1 ) = 2 , u ^ { \prime } ( 1 ) = - 1 , u ^ { \prime \prime } ( 1 ) = 4 .
$$

Show how to reformulate this problem in the form

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ .

10.2 You are given the non-autonomous initial value problem

$$
\begin{array} { l l } { { u ^ { \prime } = x u + x ^ { 2 } v , } } & { { u ( 0 ) = 3 , } } \\ { { v ^ { \prime } = u - v + 2 x w , } } & { { v ( 0 ) = 2 , } } \\ { { w ^ { \prime } = u + \displaystyle \frac { v } { 1 + x } , } } & { { w ( 0 ) = 5 . } } \end{array}
$$

Show how to write this as an autonomous problem.

10.3 The matrix

$$
A = ( N - 1 ) ^ { 2 } \left[ \begin{array} { c c c c c c c } { - 1 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 1 } & { - 2 } & { 1 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { - 2 } & { \cdots } & { 0 } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 2 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } & { - 1 } \end{array} \right]
$$

arises in the numerical solution of the heat equation, but with Neumann boundary conditions. Find the eigenvalues of $A$ .

10.4 Calculate the period of an orbit of the Lotka–Volterra problem which passes through the point $( 3 , 2 )$ .
