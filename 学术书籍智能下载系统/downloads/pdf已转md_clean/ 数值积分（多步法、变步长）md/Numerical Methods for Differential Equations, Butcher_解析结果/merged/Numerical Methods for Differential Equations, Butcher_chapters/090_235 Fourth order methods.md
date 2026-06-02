# 235 Fourth order methods

Write the order conditions presented in the previous subsection, in the special case $s = 4$ , assuming, because the method will be explicit, that $a _ { i j } = 0$ unless $i > j$ . This yields the conditions

$$
\begin{array} { r } { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } \\ { b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = 1 , } \\ { b _ { 3 } c _ { 2 } + b _ { 4 } c _ { 3 } + b _ { 4 } c _ { 4 } = 1 , } \\ { b _ { 2 } c _ { 3 } + b _ { 3 } c _ { 4 } = 1 , } \\ { b _ { 5 } c _ { 3 } \alpha _ { 2 } c _ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 3 } + b _ { 4 } c _ { 4 } = 1 , } \\ { b _ { 5 } c _ { 3 } \alpha _ { 2 } c _ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 3 } + b _ { 4 } c _ { 4 } \alpha _ { 3 } c _ { 4 } = 1 , } \\ { b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 6 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } ^ { 2 } - \frac { 1 } { 4 } , } \\ { b _ { 6 } c _ { 3 } \alpha _ { 2 } c _ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } + b _ { 6 } c _ { 4 } \alpha _ { 4 } c _ { 3 } = 1 , } \\ { b _ { 5 } c _ { 3 } \alpha _ { 2 } c _ { 2 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 4 } c _ { 3 } = \frac { 1 } { 1 2 } } \\ { b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } ^ { 2 } + b _ { 4 } c _ { 4 } \alpha _ { 2 } c _ { 2 } = \frac { 1 } { 2 } . } \end{array}
$$

That $c _ { 4 } = 1$ can be shown, by solving for $b _ { 2 }$ , $b _ { 3 }$ and $b _ { 4 }$ , from equations (235b), (235c) and (235e); by then solving for $a _ { 3 2 }$ , $a _ { 4 2 }$ and $a _ { 4 3 }$ from (235d), (235f) and (235g); and then by substituting into (235h). Many solutions and families of solutions are known to these conditions; the following are two examples:

<table><tr><td rowspan="2">RK41 :</td><td>0 G</td><td>1 0 1 0 0</td><td>1</td><td rowspan="2">1</td></tr><tr><td></td><td>1</td><td>1 1</td></tr><tr><td rowspan="2">RK42 :</td><td>1</td><td>1 1 1 -2</td><td>2</td><td></td></tr><tr><td></td><td>1</td><td>0</td><td>2 16</td></tr></table>
