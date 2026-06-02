# 514 The necessity of consistency

By selecting a specific differential equation, as in Subsection 513, we can prove that for covariant methods, consistency is necessary.

Theorem 514A Let $( A , U , B , V )$ denote a convergent method which is, moreover, covariant with preconsistency vector $u$ . Then there exists a vector $v \in \mathbb { R } ^ { r }$ , such that (510c) holds.

Proof. Consider the initial value problem

$$
y ^ { \prime } ( x ) = 1 , \qquad y ( 0 ) = 0 ,
$$

with constant starting values $\phi ( h ) ~ = ~ 0$ and $\begin{array} { r l } { \overline { { x } } } & { { } = ~ 1 } \end{array}$ . The sequence of approximations, when $n$ steps are to be taken with $h = 1 / n$ , is given by

$$
y ^ { [ i ] } = \frac { 1 } { n } B \mathbf { 1 } + V y ^ { [ i - 1 ] } , \qquad i = 1 , 2 , \ldots , n .
$$

This means that the error vector, after the $n$ steps have been completed, is given by

$$
\begin{array} { c } { { y ^ { [ n ] } - u = \displaystyle \frac { 1 } { n } \left( I + V + V ^ { 2 } + \cdots + V ^ { n - 1 } \right) B \mathbf { 1 } - u } } \\ { { \displaystyle = \displaystyle \frac { 1 } { n } \left( I + V + V ^ { 2 } + \cdots + V ^ { n - 1 } \right) ( B \mathbf { 1 } - u ) . } } \end{array}
$$

Because $V$ has bounded powers, it can be written in the form

$$
V = S ^ { - 1 } \left[ \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { W } } \end{array} \right] S ,
$$

where $I$ is $\widetilde { r } \times \widetilde { r }$ for $\widetilde r \le r$ and $W$ is power-bounded and is such that $1 \not \in \sigma ( W )$ This means that

$$
y ^ { [ n ] } - u = S ^ { - 1 } \left[ \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { \frac { 1 } { n } ( I - W ) ^ { - 1 } ( I - W ^ { n } ) } } \end{array} \right] S ( B { \bf 1 } - u ) ,
$$

whose limit as $n \longrightarrow \infty$ is

$$
\begin{array} { r } { S ^ { - 1 } \left[ \begin{array} { l l } { I } & { 0 } \\ { 0 } & { 0 } \end{array} \right] S ( B \mathbf { 1 } - u ) . } \end{array}
$$

If $y ^ { \lfloor n \rfloor } - u$ is to converge to $0$ as $n \longrightarrow \infty$ , then $S ( B \mathbf { 1 } - u )$ has only zero in its first $\widetilde { r }$ components. Write this vector in the form

$$
\begin{array} { c } { S ( B \mathbf { 1 } - u ) = \left[ \begin{array} { c } { 0 } \\ { \left( I - W \right) \widetilde v } \end{array} \right] } \\ { = \left( I - \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { W } \end{array} \right] \right) S v } \\ { = S ( I - V ) v , } \end{array}
$$

where

$$
v = S ^ { - 1 } \left[ \begin{array} { l } { 0 } \\ { \widetilde { v } } \end{array} \right] .
$$

Thus $B { \bf 1 } + V v = u + v$ .
