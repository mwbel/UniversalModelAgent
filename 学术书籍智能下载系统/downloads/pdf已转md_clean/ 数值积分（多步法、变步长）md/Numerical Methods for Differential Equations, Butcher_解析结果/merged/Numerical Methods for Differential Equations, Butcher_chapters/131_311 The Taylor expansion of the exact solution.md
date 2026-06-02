# 311 The Taylor expansion of the exact solution

We approach the question of the Taylor series of the exact solution from two points of view. In the first, we evaluate the Taylor coefficients by repeated differentiation, as we have illustrated in Subsection 310. In the second, we successively find Taylor series for the Picard iterates.

The central result in the first approach is an expression for the derivatives written in terms of labelled trees. Throughout the discussion it will be assumed, without further comment, that $y$ is a solution to $y ^ { \prime } ( x ) = f ( y ( x ) )$ and that $y$ is differentiable arbitrarily often. First, we need a formula for the derivative of a single elementary differential.

Lemma 311A Let $S = S _ { 0 } \cup \{ s \}$ be an ordered set, where every member of $S _ { 0 }$ is less than $s$ . Let $\mathbf { t }$ be a member of $T _ { S _ { 0 } } ^ { * }$ . Then

$$
{ \frac { d } { d x } } F ( | \mathbf { t } | ) ( y ( x ) )
$$

is the sum of $F ( | \mathbf { u } | ) ( y ( x ) )$ over all $\mathbf { u } \in T _ { S } ^ { * }$ such that the subtree formed by removing $s$ from the set of vertices is $\mathbf { t }$ .

Proof. If $S = \{ s _ { 0 } , s \}$ , then the result is equivalent to

$$
{ \frac { d } { d x } } f ( y ( x ) ) = f ^ { \prime } ( y ( x ) ) f ( y ( x ) ) .
$$

We now complete the proof by induction in the case $S = \{ s _ { 0 } \} \cup S _ { 1 } \cup S _ { 2 } \cup \cdot \cdot \cdot \cup$ $S _ { k } \cup \{ s \}$ , where $\left\{ s _ { 0 } \right\}$ , $S _ { 1 }$ , $S _ { 2 }$ , . . . , $S _ { k }$ , $\{ s \}$ are disjoint subsets of the ordered set $S$ . By the induction hypothesis, assume that the result of the lemma is true, when $S$ is replaced by $S _ { i }$ , $i = 1 , 2 , \ldots , k$ . If $\mathbf { t } \in T _ { S _ { 0 } } ^ { * }$ , then

$$
| \mathbf { t } | = [ \left| \mathbf { t } _ { 1 } \right| \left| \mathbf { t } _ { 2 } \right| \cdot \cdot \cdot \left| \mathbf { t } _ { k } \right| ] ,
$$

where $\mathbf { t } _ { i } \in T _ { S _ { i } } ^ { * }$ , $i = 1 , 2 , \ldots , k$ . Differentiate

$$
\begin{array} { r l } & { F ( | \mathbf { t } | ) ( y ( x ) ) } \\ & { \qquad = f ^ { ( k ) } ( y ( x ) ) \bigl ( F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , F ( | \mathbf { t } _ { 2 } | ) ( y ( x ) ) , \dots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) \bigr ) , } \end{array}
$$

to obtain

$$
Q _ { 0 } + Q _ { 1 } + Q _ { 2 } + \cdot \cdot \cdot + Q _ { k } ,
$$

where

$$
Q _ { 0 } = f ^ { ( k + 1 ) } ( y ( x ) ) { \big ( } F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , F ( | \mathbf { t } _ { 2 } | ) ( y ( x ) ) , \ldots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) , f ( y ( x ) ) { \big ) }
$$

and, for $i = 1 , 2 , \ldots , k$ ,

$$
Q _ { i } = f ^ { ( k ) } ( y ( x ) ) { \big ( } F ( | \mathbf { t } _ { 1 } | ) ( y ( x ) ) , \ldots , { \frac { d } { d x } } F ( | \mathbf { t } _ { i } | ) ( y ( x ) ) , \ldots , F ( | \mathbf { t } _ { k } | ) ( y ( x ) ) { \big ) } .
$$

The value of $Q _ { 0 }$ is

$$
F ( \left[ \left. \mathbf { t } _ { 1 } \right. \left. \mathbf { t } _ { 2 } \right. \cdot \cdot \cdot \left. \mathbf { t } _ { k } \right. \left. \mathbf { t } _ { 0 } \right. \right] ) ( y ( x ) ) ,
$$

where $| \mathbf { t } _ { 0 } |$ is $\tau$ labelled with the single label $s$ . For $i = 1 , 2 , \ldots , k$ , the value of $Q _ { i }$ is the sum of all terms of the form (311a), with $F ( | \mathbf { t } _ { i } | ) ( y ( x ) )$ replaced by terms of the form $F ( | \mathbf { u } _ { i } | ) ( y ( x ) )$ , where $\mathbf { u } _ { i }$ is formed from $\mathbf { t } _ { i }$ by adding an additional leaf labelled by $s$ . The result of the lemma follows by combining all terms contributing to the derivative of (311a).

Theorem 311B Let $S$ denote a finite ordered set. Then

$$
y ^ { ( \# S ) } ( y _ { 0 } ) = \sum _ { \mathbf { t } \in T _ { S } } F ( | \mathbf { t } | ) ( y _ { 0 } ) .
$$

Proof. In the case $| \mathbf { t } | = \tau$ , the result is obvious. For the case $\# S > 1$ , apply Lemma 311A repeatedly by adding additional (and increasing) members to $S$ . 

We rewrite this result in terms of unlabelled trees, by noting that the number of times that a tree $t$ with order $\# S$ occurs as the unlabelled counterpart of a member of $T _ { S } ^ { * }$ , is exactly $\alpha ( t )$ .

# Theorem 311C

$$
y ^ { ( n ) } ( y ( x ) ) = \sum _ { t \in T _ { n } } \alpha ( t ) F ( t ) ( y ( x ) ) .
$$

The alternative approach to finding the Taylor coefficients is based on the Picard integral equation

$$
y ( x _ { 0 } + h \xi ) = y ( x _ { 0 } ) + h \int _ { 0 } ^ { \xi } f ( y ( x _ { 0 } + h \xi ) ) d \xi ,
$$

which, written in terms of Picard iterations, becomes

$$
y _ { n } ( x _ { 0 } + h \xi ) = y ( x _ { 0 } ) + h \int _ { 0 } ^ { \xi } f ( y _ { n - 1 } ( x _ { 0 } + h \xi ) ) d \xi ,
$$

where the initial iterate is given by

$$
y _ { 0 } ( x + h \xi ) = y ( x _ { 0 } ) .
$$

For $n = 1 , 2 , \ldots$ , we expand $y _ { n } ( x _ { 0 } + h \xi )$ for $\xi \in [ 0 , 1 ]$ , omitting terms that are $O ( h ^ { n + 1 } )$ .

Theorem 311D The Taylor expansion of $y _ { n }$ given by (311b) and (311c) is equal to

$$
y _ { n } = y ( x _ { 0 } ) + \sum _ { i = 1 } ^ { n } h ^ { i } \xi ^ { i } \sum _ { t \in T _ { i } } \frac { 1 } { \sigma ( t ) \gamma ( t ) } F ( t ) ( y ( x _ { 0 } ) ) + O ( h ^ { n + 1 } ) .
$$

Proof. The case $n = 0$ is obvious. We now use induction and suppose that (311d) is true with $n$ replaced by $n - 1$ . By Lemma 310B, with

$$
\theta ( t ) = \frac { 1 } { \gamma ( t ) } ,
$$

we have as the coefficient of $F ( t ) ( y ( x _ { 0 } ) ) h ^ { r ( t ) }$ , the expression

$$
\int _ { 0 } ^ { \xi } \frac { 1 } { \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) } \xi ^ { r ( t ) - 1 } { d \xi } = \frac { 1 } { r ( t ) \prod _ { i = 1 } ^ { k } \gamma ( t _ { i } ) } \xi ^ { r ( t ) } = \frac { 1 } { \gamma ( t ) } \xi ^ { r ( t ) } ,
$$

where $t = \left\lfloor t _ { 1 } t _ { 2 } \cdot \cdot \cdot t _ { k } \right\rfloor$ .
