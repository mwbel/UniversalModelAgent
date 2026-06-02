# 124 Further differential-algebraic problems

Consider the initial value problem

$$
\begin{array} { c } { { y ^ { \prime } = y + z , } } \\ { { \begin{array} { r l } \end{array} } } \\ { { 0 = z + z ^ { 3 } - y , } } \\ { { \begin{array} { r l } \end{array} } } \\ { { y ( 0 ) = 2 , \quad z ( 0 ) = 1 . } } \end{array}
$$

This is an index 1 problem, because a single differentiation of (124b) and a substitution from (124a) converts this to a differential equation system consisting of (124b) together with $z ^ { \prime } = ( y + z ) / ( 1 + 3 z ^ { 2 } )$ . However, this reduction does not do justice to the original formulation in the sense that a solution with slightly perturbed initial values has little to do with the original index 1 problem. This emphasizes the fact that initial conditions for the differential-algebraic equation formulation must be consistent with the algebraic constraint for it to be well-posed. A more appropriate reduction is to replace (124a) by $y ^ { \prime } = y + \phi ( y )$ , where $\phi ( y )$ is the real value of $z$ which satisfies (124b).

We next introduce an initial value problem comprising two differential equations and a single algebraic constraint:

$$
\begin{array} { c } { { y _ { 1 } ^ { \prime } = - \sin ( z ) , } } \\ { { y _ { 2 } ^ { \prime } = 2 \cos ( z ) - y _ { 1 } , } } \\ { { 0 = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } - 1 , } } \\ { { y _ { 1 } ( 0 ) = 1 , \quad y _ { 2 } ( 0 ) = 0 , \qquad z ( 0 ) = 0 . } } \end{array}
$$

An attempt to reduce this to an ordinary differential equation system by differentiating (124f) and substituting from (124d) and (124e), leads to a new algebraic constraint

$$
- y _ { 1 } \sin ( z ) + y _ { 2 } ( 2 \cos ( z ) - y _ { 1 } ) = 0 ,
$$

and it is clear that this will be satisfied by the solution to the original problem. However, this so-called ‘hidden constraint’ introduces a new complexity into this type of problem. That is, for initial values to be consistent, (124h) must be satisfied at the initial time. If, for example, the initial values $y _ { 1 } ( 0 ) = 1$ and $y _ { 2 } ( 0 ) = 0$ are retained, but the initial value $z ( 0 )$ is perturbed slightly, (124h) will not be satisfied and no genuine solution exists. But the hidden constraint, as the problem has actually been posed, is satisfied, and we can take the reduction towards an ordinary differential equation system to completion. Differentiate (124h) and substitute from (124d) and (124e) and we finally arrive at

$$
z ^ { \prime } ( \cos ^ { 2 } ( z ) + 2 \sin ^ { 2 } ( z ) ) = \sin ^ { 2 } ( z ) + y _ { 2 } \sin ( z ) + ( 2 \cos ( z ) - y _ { 1 } ) ^ { 2 } .
$$

Because two differentiation steps were required to reach this equation, the original system is referred to as an index 2 problem. In summary, the original index 2 problem, comprising (124d), (124e), (124f) has been reduced, first to an index 1 formulation (124d), (124e), (124h), and then to an ordinary differential equation system (124d), (124e), (124i).

# Exercises 12

12.1 Show that a problem of the form

$$
\begin{array} { l } { { u ^ { \prime } = - \alpha ^ { \prime } ( v ) \gamma ( u , v ) , } } \\ { { v ^ { \prime } = \beta ^ { \prime } ( u ) \gamma ( u , v ) , } } \end{array}
$$

satisfies the assumptions of (122a) with a suitable choice of $H ( u , v )$ .

12.2 Write the Lotka–Volterra equations (106a), (106b) in the form given in Exercise 12.1.
