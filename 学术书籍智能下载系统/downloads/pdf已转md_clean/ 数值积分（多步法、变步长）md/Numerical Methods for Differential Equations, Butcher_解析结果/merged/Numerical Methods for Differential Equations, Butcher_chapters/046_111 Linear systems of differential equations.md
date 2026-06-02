# 111 Linear systems of differential equations

Linear differential equations are important because of the availability of a superposition principle. That is, it is possible for a linear differential equation system to combine known solutions to construct new solutions. The standard form of a linear system is

$$
\frac { d y } { d x } = A ( x ) y + \phi ( x ) ,
$$

where $A ( x )$ is a possibly time-dependent linear operator. The corresponding ‘homogeneous’ system is

$$
{ \frac { d y } { d x } } = A ( x ) y .
$$

The superposition principle, which is trivial to verify, states that:

Theorem 111A If $\widehat { y }$ is a solution to (111a) and $y _ { 1 } , y _ { 2 } , \ldots , y _ { k }$ are solutions to (111b), then for any constants $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k }$ , the function $y$ given by

$$
\boldsymbol { y } ( \boldsymbol { x } ) = \boldsymbol { \widehat { y } } ( \boldsymbol { x } ) + \sum _ { i = 1 } ^ { k } \alpha _ { i } \boldsymbol { y } _ { i } ( \boldsymbol { x } ) ,
$$

is a solution to (111a).

The way this result is used is to attempt to find the solution which matches a given initial value, by combining known solutions.

Many linear problems are naturally formulated in the form of a single high order differential equation

$$
Y ^ { ( m ) } ( x ) - C _ { 1 } ( x ) Y ^ { ( m - 1 ) } ( x ) - C _ { 2 } ( x ) Y ^ { ( m - 2 ) } ( x ) - \cdot \cdot \cdot - C _ { m } ( x ) Y ( x ) = g ( x ) .
$$

By identifying $Y ( x ) = y _ { 1 } ( x ) , Y ^ { \prime } ( x ) = y _ { 2 } ( x ) , . . . , Y ^ { ( m - 1 ) } = y _ { m } ( x )$ , we can rewrite the system in the form

$$
\frac d { d x } \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \\ { \vdots } \\ { y _ { m } ( x ) } \end{array} \right] = A ( x ) \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \\ { \vdots } \\ { y _ { m } ( x ) } \end{array} \right] + \phi ( x ) ,
$$

where the ‘companion matrix’ $A ( x )$ and the ‘inhomogeneous term’ $\phi ( x )$ are given by

$$
\mathbf { \Psi } ( x ) = \left[ \begin{array} { c c c c c c } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } \\ { C _ { m } ( x ) } & { C _ { m - 1 } ( x ) } & { C _ { m - 2 } ( x ) } & { \cdots } & { C _ { 1 } ( x ) } \end{array} \right] , \quad \phi ( x ) = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { g ( x ) } \end{array} \right] .
$$

When $A ( x ) = A$ in (111b) is constant, then to each eigenvalue $\lambda$ of $A$ , with corresponding eigenvector $\boldsymbol { v }$ , there exists a solution given by

$$
y ( x ) = \exp ( \lambda x ) v .
$$

When a complete set of eigenvectors does not exist, but corresponding to $\lambda$ there is a chain of generalized eigenvectors

$$
A v _ { 1 } = \lambda v _ { 1 } + v , \quad A v _ { 2 } = \lambda v _ { 2 } + v _ { 1 } , \quad \ldots , \quad A v _ { k - 1 } = \lambda v _ { k - 1 } + v _ { k - 2 } ,
$$

then there is a chain of additional independent solutions to append to (111d):

$$
y _ { 1 } = x \exp ( \lambda x ) v _ { 1 } , \quad y _ { 2 } = x ^ { 2 } \exp ( \lambda x ) v _ { 2 } , \quad \ldots , \quad y _ { k - 1 } = x ^ { k - 1 } \exp ( \lambda x ) v _ { k - 1 } .
$$

In the special case in which $A$ is a companion matrix, so that the system is equivalent to a high order equation in a single variable, as in (111c), with $C _ { 1 } ( x ) = C _ { 1 } , C _ { 2 } ( x ) = C _ { 2 } , . . . , C _ { m } ( x ) = C _ { m }$ , each a constant, the characteristic polynomial of $A$ is

$$
P ( \lambda ) = \lambda ^ { m } - C _ { 1 } \lambda ^ { m - 1 } - C _ { 2 } \lambda ^ { m - 2 } - \cdot \cdot \cdot - C _ { m } = 0 .
$$

For this special case, $P ( \lambda )$ is also the minimal polynomial, and repeated zeros always correspond to incomplete eigenvector spaces and the need to use generalized eigenvectors. Also, in this special case, the eigenvector corresponding to $\lambda$ , together with the generalized eigenvectors if they exist, are

$$
\boldsymbol { \upsilon } = \left[ \begin{array} { c } { 1 } \\ { \lambda } \\ { \lambda ^ { 2 } } \\ { \vdots } \\ { \lambda ^ { m - 1 } } \end{array} \right] , \boldsymbol { v } _ { 1 } = \left[ \begin{array} { c } { 0 } \\ { 1 } \\ { 2 \lambda } \\ { \vdots } \\ { ( m - 1 ) \lambda ^ { m - 2 } } \end{array} \right] , \boldsymbol { v } _ { 2 } = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { 1 } \\ { \vdots } \\ { \frac { ( m - 1 ) ( m - 2 ) } { 2 } \lambda ^ { m - 3 } } \end{array} \right] , \boldsymbol { \ldots } . \boldsymbol { \ldots } .
$$
