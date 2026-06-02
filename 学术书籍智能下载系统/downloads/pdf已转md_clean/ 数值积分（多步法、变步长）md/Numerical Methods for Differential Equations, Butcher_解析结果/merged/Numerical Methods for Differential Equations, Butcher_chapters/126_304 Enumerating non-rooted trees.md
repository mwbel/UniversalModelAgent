# 304 Enumerating non-rooted trees

Recall the generating function for the numbers of rooted trees of various orders

$$
\theta ( x ) = \theta _ { 1 } + \theta _ { 2 } x + \theta _ { 3 } x ^ { 2 } + \cdot \cdot \cdot ,
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0003_pages_0141-0210/auto/images/00dff3eda7dd4af2044d9dda13be2eec775a97d03ed67464fab4d9661e03a211.jpg)  
Trees with up to six vertices

where $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ are given in (302c). Also write

$$
\begin{array} { l } { { \phi ( x ) = \phi _ { 1 } + \phi _ { 2 } x + \phi _ { 3 } x ^ { 2 } + \cdots , } } \\ { { \psi ( x ) = \psi _ { 1 } + \psi _ { 2 } x + \psi _ { 3 } x ^ { 2 } + \cdots , } } \end{array}
$$

as the generating functions for the numbers of trees $\phi _ { i }$ of orders $i = 1 , 2 , \dots$ and the numbers of non-superfluous trees $\psi _ { i }$ . The meaning of ‘superfluous tree’ will become clear from the discussion which follows.

Given a tree, we can form a family of rooted trees by designating one of its vertices to be the root. We will refer to two such rooted trees as adjacent if the two roots are at the ends of the same edge in the underlying tree. For any particular vertex $\boldsymbol { v }$ , let $t = \left\lfloor t _ { 1 } , t _ { 2 } , \ldots , t _ { m } \right\rfloor$ and write $\phi ( v ) = \mathrm { m a x } _ { i = 1 } ^ { m } r ( t _ { i } )$ . There will be at most one vertex adjacent to $\boldsymbol { v }$ for which the value of $\phi$ is lower. However, for some trees with even order there will be two adjacent vertices for which the values of $\phi$ are each equal to $r ( t ) / 2$ . The 14 trees with up to six vertices are shown in Figure $\mathrm { 3 0 4 ( i ) }$ . The value of $\phi$ is attached to each vertex, with arrows showing the direction of decreasing $\phi$ . In the cases of two adjacent vertices $\boldsymbol { v }$ and $w$ with $\phi ( v ) = \phi ( w )$ , two arrows are shown meeting midway through the edge.

For a rooted tree formed from a tree by selecting a vertex as the root, we can move along an arrow to obtain a vertex with a lower value of $\phi$ . Thus we should subtract from the total number of rooted trees of a given order $n$ , the number of pairs or trees with unequal orders. This means subtracting the number of rooted trees of the form $t u$ , where $r ( t ) < r ( u )$ . In the case of trees where $n = 2 m$ is even, and for two adjacent vertices, the rooted trees $t u$ and ut occur, where $r ( t ) = r ( u )$ , we need to subtract half the number of such trees unless $t = u$ , in which case no subtraction is performed.

For a tree of order $\textit { n } = \ 2 m + 1$ , the number of trees will thus be $\begin{array} { r } { \theta _ { n } - \sum _ { i = 1 } ^ { m } \theta _ { i } \theta _ { n - i } } \end{array}$ , which is the coefficient of $x ^ { n - 1 }$ in

$$
\theta ( x ) - \frac { x } { 2 } \Bigl ( \theta ( x ) ^ { 2 } \mp \theta ( x ^ { 2 } ) \Bigr ) ,
$$

where the term involving $\theta ( x ^ { 2 } )$ does not actually contribute to this case of odd $n$ . In the case of even $n = 2 m$ , the number of trees will be

$$
\theta _ { n } - \sum _ { i = 1 } ^ { m - 1 } \theta _ { i } \theta _ { n - i } - \frac 1 2 \theta _ { m } ( \theta _ { m } \mp 1 ) ,
$$

where $\mp$ is interpreted as $^ -$ , and this is again equal to the coefficient of $x ^ { n - 1 }$ in (304a).

Counting non-superfluous trees is the same except that we need to subtract from the totals the number of trees of the form $t t$ , and this gives the same result as (304a) but with $\mp$ replaced by $^ +$ . Putting these results together we formally state:

Theorem 304A The generating functions for trees and non-superfluous trees are

$$
\begin{array} { c } { { \phi ( x ) = \theta ( x ) - \displaystyle \frac { x } { 2 } \Big ( \theta ( x ) ^ { 2 } - \theta ( x ^ { 2 } ) \Big ) , } } \\ { { \psi ( x ) = \theta ( x ) - \displaystyle \frac { x } { 2 } \Big ( \theta ( x ) ^ { 2 } + \theta ( x ^ { 2 } ) \Big ) . } } \end{array}
$$
