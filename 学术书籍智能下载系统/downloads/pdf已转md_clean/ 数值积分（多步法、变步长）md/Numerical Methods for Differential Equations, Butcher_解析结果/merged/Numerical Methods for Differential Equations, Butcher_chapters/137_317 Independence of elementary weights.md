# 317 Independence of elementary weights

We show in Subsection 324 that, given a positive integer $p$ , there exists an integer $s$ such that there is a Runge–Kutta method with $s$ stages with order $p$ . We now present a more general result on the independence of the elementary weights but without a specific value of $s$ given.

Theorem 317A Given a finite subset $T _ { 0 }$ , of $T$ and a mapping $\phi : T _ { 0 }  \mathbb { R }$ , there exists a Runge–Kutta method such that the elementary weights satisfy

$$
\Phi ( t ) = \phi ( t ) , \qquad f o r \ a l l \ t \in T _ { 0 } .
$$

Proof. Let $\# T _ { 0 } = n$ . The set of possible values that can be taken by the vector of $\Phi ( t )$ values, for all $t \in T _ { 0 }$ , is a vector space. To see why this is the case, consider Runge–Kutta methods given by the tableaux

$$
{ \frac { c \left| \ A \right. } { \left| \ b ^ { \mathsf { T } } \right. } } \qquad { \mathrm { a n d } } \qquad { \frac { \overline { { c } } } { \overline { { b } } ^ { \mathsf { T } } } } \qquad { \frac { \overline { { A } } } { \overline { { b } } ^ { \mathsf { T } } } }
$$

with $s$ and $\overline { { s } }$ stages, respectively. If the elementary weight functions for these two Runge–Kutta methods are $\Phi$ and $\overline { { \Phi } }$ , then the method given by the tableau

$$
\frac { c } { c } \left| \begin{array} { c c } { { A } } & { { 0 } } \\ { { 0 } } & { { \overline { { { A } } } } } \\ { { \theta b ^ { \intercal } } } & { { \overline { { { \theta } } } \overline { { { b } } } ^ { \intercal } } } \end{array} \right.
$$

has elementary weight function $\theta \Phi + { \overline { { \theta \Phi } } }$ . Let $V \subset \mathbb { R } ^ { n }$ denote this vector space. We complete the proof by showing that $V = \mathbb { R } ^ { n } .$ If this were not the case, there would exist a non-zero function $\psi : T _ { 0 } \to \mathbb { R }$ such that $\begin{array} { r } { \sum _ { t \in T _ { 0 } } \psi ( t ) \Phi ( t ) = 0 } \end{array}$ , for all Runge–Kutta methods. Because every coefficient in a Runge–Kutta tableau can be multiplied by an arbitrary scalar $\theta$ to give a new method for which $\Phi ( t )$ is replaced by $\theta ^ { r ( t ) } \Phi ( t )$ , we may assume that every non-zero value of $\psi$ corresponds to trees with the same order $k$ . This is impossible for $k = 1$ , because in this case there is only a single tree $\tau$ . Suppose the impossibility of this has been proved for all orders less than $k$ , but that there exist trees Kutta methods with $t _ { 1 }$ , $t _ { 2 }$ , . . . , $t _ { m }$ , each of order $\psi ( t _ { i } ) \neq 0$ $k$ , such that , for $i = 1 , 2 , \dots , m$ $\textstyle \sum _ { i = 1 } ^ { m } \psi ( t _ { i } ) \Phi ( t _ { i } ) = 0$ . Write $t _ { i } = [ t _ { i 1 } ^ { l _ { i 1 } } t _ { i 2 } ^ { l _ { i 2 } } \cdot \cdot \cdot ]$ , for all Runge– , for $i = 1 , 2 , \dots , m$ . Let $\hat { t }$ denote a tree appearing amongst the $t _ { i j }$ which does not occur with the same exponent in each of the $t _ { i }$ . Construct an $s$ -stage Runge–Kutta method

$$
\frac { c \mid A } { b ^ { \intercal } }
$$

for which each of $\Phi ( t _ { i j } ) = 1$ , except for $\Phi ( \hat { t } ) = \theta$ . Define second Runge–Kutta tableau with $s + 1$ stages of the form

$$
{ \frac { c \ \boxed { A } \ 0 } { 1 \ \boxed { b ^ { \intercal } } \ 0 } } \ .
$$

If $q _ { i }$ is the exponent of $\hat { t }$ in $t _ { i }$ , then it follows that

$$
\sum _ { i = 1 } ^ { m } \psi ( t _ { i } ) \theta ^ { q _ { i } } = 0 .
$$

Since $\theta$ can take any value and since $q _ { i }$ is not constant, it is not possible that $\psi$ is never zero. 
