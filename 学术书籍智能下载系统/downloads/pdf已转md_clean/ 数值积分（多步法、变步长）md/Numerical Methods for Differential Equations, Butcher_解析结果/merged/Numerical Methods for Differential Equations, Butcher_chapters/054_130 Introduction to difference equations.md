# 130 Introduction to difference equations

While differential equations deal with functions of a continuous variable, difference equations deal with functions of a discrete variable. Instead of a formula for the derivative of a function written in terms of the function itself, we have to consider sequences for which each member is related in some specific way to its immediate predecessor or several of its most recent predecessors. Thus we may write

$$
x _ { n } = \phi _ { n } ( x _ { n - 1 } , x _ { n - 2 } , \ldots , x _ { n - k } ) ,
$$

where $k$ is the ‘order’ of this difference equation. This equation, in which $x _ { n }$ depends on $k$ previous values, can be recast in a vector setting in which members of the sequence lie not in $\mathbb { R }$ but in $\mathbb { R } ^ { k }$ , and depend only on one previous value. Thus if

$$
X _ { n } = \left[ \begin{array} { c } { { x _ { n } } } \\ { { x _ { n - 1 } } } \\ { { \vdots } } \\ { { x _ { n - k + 1 } } } \end{array} \right] ,
$$

then

$$
X _ { n } = \Phi _ { n } ( X _ { n - 1 } ) = \left[ \begin{array} { c } { \phi _ { n } ( x _ { n - 1 } , x _ { n - 2 } , \ldots , x _ { n - k } ) } \\ { x _ { n - 1 } } \\ { x _ { n - 2 } } \\ { \vdots } \\ { x _ { n - k + 1 } } \end{array} \right] .
$$

Just as for differential equations, we can use either formulation as we please.
