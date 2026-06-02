# 513 The necessity of stability

Stability has the effect of guaranteeing that errors introduced in any step of a computation do not have disastrous effects on later steps. The necessity of this property is expressed in the following result:

Theorem 513A A general linear method $( A , U , B , V )$ is convergent only if it is stable.

Proof. Suppose, on the contrary, that $\left\{ \left\| V ^ { n } \right\| : n = 1 , 2 , 3 , \ldots \right\}$ is unbounded. This implies that there exists a sequence of vectors $w _ { 1 } , w _ { 2 } , w _ { 3 } , . . .$ such that $\| w _ { n } \| = 1$ , for all $n = 1 , 2 , 3 , \ldots$ , and such that the sequence $\{ \| V ^ { n } w _ { n } \| : n =$ $1 , 2 , 3 , \ldots \}$ is unbounded. Consider the solution of the initial value problem

$$
y ^ { \prime } ( x ) = 0 , \qquad y ( 0 ) = 0 ,
$$

using $( A , U , B , V )$ , where $n$ steps are taken with stepsize $h = 1 / n$ , so that the solution is approximated at $\overline { { x } } = 1$ . Irrespective of the choice of the vector $u$ in Definition 512A, the convergence of the method implies that the sequence of approximations converges to zero. For the approximation carried out with $n$ steps, use as the starting approximation

$$
\phi \Big ( \frac { 1 } { n } \Big ) = \frac { 1 } { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } w _ { n } .
$$

This converges to zero, because $\left\| \phi ( { 1 } / { n } ) \right\| = \left( { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } \right) ^ { - 1 }$ . The result, computed after $_ { n }$ steps, will then be

$$
V ^ { n } \phi \Big ( \frac { 1 } { n } \Big ) = \frac { 1 } { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } V ^ { n } w _ { n } ,
$$

with norm

$$
\left\| V ^ { n } \phi \Big ( \frac { 1 } { n } \Big ) \right\| = \frac { \| V ^ { n } w _ { n } \| } { \operatorname* { m a x } _ { i = 1 } ^ { n } \| V ^ { i } w _ { i } \| } .
$$

Because the sequence $n \mapsto \| V ^ { n } w _ { n } \|$ is unbounded, an infinite set of $n$ values will have the property that the maximum value of $\| V ^ { i } w _ { i } \|$ , for $i \ \leq \ n$ , will occur with $i = n$ . This means that (513a) has value 1 arbitrarily often, and hence is not convergent to zero as $n \longrightarrow \infty$ . $\sqcup$
