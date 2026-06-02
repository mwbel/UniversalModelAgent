# 141 Constant coefficients

We consider the solution of a linear difference equation with constant coefficients:

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } + \psi _ { n } .
$$

The solution is found in terms of the solution to the canonical problem in which the initial information is given in the form

$$
\begin{array} { r } { \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { - 1 } } \\ { \vdots } \\ { y _ { - k + 2 } } \\ { y _ { - k + 1 } } \end{array} \right] = \left[ \begin{array} { c } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { 0 } \end{array} \right] . } \end{array}
$$

Denote the solution to this problem at step $m$ by

$$
y _ { m } = \theta _ { m } , \qquad m = 0 , 1 , 2 , \ldots , n ,
$$

with $\theta _ { m } = 0$ for $m \ < \ 0$ . Given the difference equation (141a) with initial values $y _ { 0 } , y _ { 1 } , \ldots , y _ { k - 1 }$ , define linear combinations of this data by

$$
{ \left[ \begin{array} { l } { { \widetilde { y } } _ { k - 1 } } \\ { { \widetilde { y } } _ { k - 2 } } \\ { { \widetilde { y } } _ { k - 3 } } \\ { \vdots } \\ { { \widetilde { y } } _ { 1 } } \\ { { \widetilde { y } } _ { 0 } } \end{array} \right] } = { \left[ \begin{array} { l l l l l l } { 1 } & { \theta _ { 1 } } & { \theta _ { 2 } } & { \cdots } & { \theta _ { k - 2 } } & { \theta _ { k - 1 } } \\ { 0 } & { 1 } & { \theta _ { 1 } } & { \cdots } & { \theta _ { k - 3 } } & { \theta _ { k - 2 } } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { \theta _ { k - 4 } } & { \theta _ { k - 3 } } \\ { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { \theta _ { 1 } } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] } ^ { - 1 } { \left[ \begin{array} { l } { y _ { k - 1 } } \\ { y _ { k - 2 } } \\ { y _ { k - 3 } } \\ { \vdots } \\ { y _ { 1 } } \\ { y _ { 0 } } \end{array} \right] } .
$$

We are now in a position to write down the solution to (141a).

Theorem 141A Using the notation introduced in this subsection, the solution to (141a) with given initial values $y _ { 0 } , y _ { 1 } , \ldots , y _ { k - 1 }$ is given by

$$
y _ { n } = \sum _ { i = 0 } ^ { k - 1 } \theta _ { n - i } { \widetilde { y } } _ { i } + \sum _ { i = k } ^ { n } \theta _ { n - i } \psi _ { i } .
$$

Proof. Substitute $n = m$ , for $m = 0 , 1 , 2 , \ldots , k - 1$ , into (141c), and we obtain the value

$$
y _ { m } = \widetilde { y } _ { m } + \theta _ { 1 } \widetilde { y } _ { m - 1 } + \cdot \cdot \cdot + \theta _ { m } \widetilde { y } _ { 0 } , \quad m = 0 , 1 , 2 , \ldots , k - 1 .
$$

This is equal to $y _ { m }$ if (141b) holds. Add the contribution to the solution from each of $m = k , k + 1 , \ldots , n$ and the result follows. 
