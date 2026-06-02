# 14 Difference Equation Theory

140 Linear difference equations

The standard form for linear difference equation systems is

$$
X _ { n } = A _ { n } X _ { n - 1 } + \phi _ { n } ,
$$

which becomes an initial value problem if the value of the initial vector $X _ { 0 }$ is specified. The corresponding system in which $\phi _ { n }$ is omitted is the ‘homogeneous part’.

Many linear difference equations are more naturally formulated as

$$
y _ { n } = \alpha _ { n 1 } y _ { n - 1 } + \alpha _ { n 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { n k } y _ { n - k } + \psi _ { n } ,
$$

but these are easily recast in the form (140a) by writing

$$
X _ { n } = \left[ \begin{array} { c } { { y _ { n } } } \\ { { y _ { n - 1 } } } \\ { { \vdots } } \\ { { y _ { n - k + 1 } } } \end{array} \right] , \quad A _ { n } = \left[ \begin{array} { c c c c } { { \alpha _ { n 1 } } } & { { \alpha _ { n 2 } } } & { { \cdots } } & { { \alpha _ { n k } } } \\ { { 1 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right] , \quad \phi _ { n } = \left[ \begin{array} { c } { { \psi _ { n } } } \\ { { 0 } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right] .
$$

To solve (140a) as an initial value problem, we need to use products of the form

$$
\prod _ { i = m } ^ { n } A _ { i } = A _ { n } A _ { n - 1 } \cdot \cdot \cdot A _ { m + 1 } A _ { m } .
$$

We have:

Theorem 140A The problem (140a), with initial value $X _ { 0 }$ given, has the unique solution

$$
y _ { n } = { \biggl ( } \prod _ { i = 1 } ^ { n } A _ { i } { \biggr ) } X _ { 0 } + \left( \prod _ { i = 2 } ^ { n } A _ { i } \right) \phi _ { 1 } + \left( \prod _ { i = 3 } ^ { n } A _ { i } \right) \phi _ { 2 } + \cdot \cdot \cdot + A _ { n } \phi _ { n - 1 } + \phi _ { n } .
$$

Proof. The result holds for $n = 0$ , and the general case follows by induction.
