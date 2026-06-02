# 131 A linear problem

Consider the difference equation

$$
y _ { n } = 3 y _ { n - 1 } - 2 y _ { n - 2 } + C \theta ^ { n } ,
$$

where $C$ and $\theta$ are constants. We do not specify an initial value, but aim instead to find the family of all solutions. As a first step, we look at the special case in which $C = 0$ . In this case, the equation becomes linear in the sense that known solutions can be combined by linear combinations. The simplified equation in matrix–vector form is

$$
\left[ \begin{array} { c } { y _ { n } } \\ { y _ { n - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { 3 } & { - 2 } \\ { 1 } & { 0 } \end{array} \right] \left[ \begin{array} { c } { y _ { n - 1 } } \\ { y _ { n - 2 } } \end{array} \right] ,
$$

which can be rewritten as

$$
\left[ \begin{array} { c } { y _ { n } - y _ { n - 1 } } \\ { - y _ { n } + 2 y _ { n - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { 2 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { y _ { n - 1 } - y _ { n - 2 } } \\ { - y _ { n - 1 } + 2 y _ { n - 2 } } \end{array} \right] ,
$$

with solution defined by

$$
\begin{array} { c } { { y _ { n } - y _ { n - 1 } = A 2 ^ { n - 1 } , } } \\ { { - y _ { n } + 2 y _ { n - 1 } = B , } } \end{array}
$$

for constants $A$ and $B$ . By eliminating $y _ { n - 1 }$ , we find

$$
y _ { n } = A 2 ^ { n } + B
$$

for the general solution. The fact that this combines powers of $2$ and $^ { 1 }$ , the eigenvalues of the matrix

$$
\left[ { \begin{array} { r r } { 3 } & { - 2 } \\ { 1 } & { 0 } \end{array} } \right] ,
$$

suggests that we can look for solutions for the original formulation in the form $\lambda ^ { n }$ without transforming to the matrix–vector formulation. Substitute this trial solution into (131a), with $C = 0$ , and we find, apart from a factor $\lambda ^ { n - 2 }$ , that the condition on $\lambda$ is

$$
\lambda ^ { 2 } - 3 \lambda + 2 = 0 .
$$

This is the characteristic polynomial of the matrix (131b), but it can be read off immediately from the coefficients in (131a).

To find the general solution to (131a), if $C \neq 0$ , it is easy to see that we only need to find one special solution to which we can add the terms $A 2 ^ { n } + B$ to obtain all possible solutions. A special solution is easily found, if $\theta \neq 1$ and $\theta \neq 2$ , in the form

$$
y _ { n } = \frac { C \theta ^ { n + 2 } } { ( \theta - 1 ) ( \theta - 2 ) } .
$$

This type of special solution is not available if $\theta$ equals either $^ { 1 }$ or 2. In these cases a special solution can be found as a multiple of $_ { n }$ or $n 2 ^ { { n } }$ , respectively. Combining these cases, we write the general solution as

$$
y _ { n } = { \left\{ \begin{array} { l l } { A 2 ^ { n } + B - C n , } & { \theta = 1 , } \\ { A 2 ^ { n } + B + 2 C n 2 ^ { n } , } & { \theta = 2 , } \\ { A 2 ^ { n } + B + { \frac { C \theta ^ { 2 } } { ( \theta - 1 ) ( \theta - 2 ) } } \theta ^ { n } , } & { \theta \neq 1 , \theta \neq 2 . } \end{array} \right. }
$$

132 The Fibonacci difference equation

The initial value difference equation

$$
y _ { n } = y _ { n - 1 } + y _ { n - 2 } , \qquad y _ { 0 } = 0 , \quad y _ { 1 } = 1 ,
$$

is famous because of the mathematical, biological and even numerological significance attached to the solution values

$$
1 , 2 , 3 , 5 , 8 , 1 3 , 2 1 , 3 4 , 5 5 , 8 9 , 1 4 4 , \ldots .
$$

To find the general solution, solve the polynomial equation

$$
\lambda ^ { 2 } - \lambda - 1 = 0 ,
$$

to find the terms $\lambda _ { 1 } ^ { n }$ and $\lambda _ { 2 } ^ { n }$ , where

$$
\begin{array} { r } { \lambda _ { 1 } = \frac { 1 + \sqrt { 5 } } { 2 } , \quad \lambda _ { 2 } = \frac { 1 - \sqrt { 5 } } { 2 } = - \lambda _ { 1 } ^ { - 1 } . } \end{array}
$$

To find the coefficients $A$ and $B$ in the general solution

$$
\begin{array} { r } { y _ { n } = A \left( \frac { 1 + \sqrt { 5 } } { 2 } \right) ^ { n } + B \left( - \frac { 1 + \sqrt { 5 } } { 2 } \right) ^ { - n } , } \end{array}
$$

substitute $n = 0$ and $n = 1$ , to find $A = - B = 5 ^ { - 1 / 2 }$ , and therefore the specific solution to the initial value problem (132a),

$$
\begin{array} { r } { y _ { n } = \frac { 1 } { \sqrt { 5 } } \bigg ( \Big ( \frac { 1 + \sqrt { 5 } } { 2 } \Big ) ^ { n } - \Big ( - \frac { 1 + \sqrt { 5 } } { 2 } \Big ) ^ { - n } \bigg ) . } \end{array}
$$
