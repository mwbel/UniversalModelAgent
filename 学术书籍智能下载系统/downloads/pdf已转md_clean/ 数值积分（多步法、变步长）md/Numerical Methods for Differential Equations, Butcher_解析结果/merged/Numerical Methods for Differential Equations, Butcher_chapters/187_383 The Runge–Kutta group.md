# 383 The Runge–Kutta group

While the group of equivalent classes of Runge–Kutta methods is conceptually very simple, it is difficult to use for detailed manipulations. We turn to a second group that is closely related to it, but which has a more convenient representation.

Let $G _ { 1 }$ denote the set of functions on $T$ , the rooted trees, to the real numbers. We define a binary relation on $G _ { 1 }$ that makes it a group. It is convenient to widen the scope of our discussion by making use of forests. By a ‘forest’, we mean a set of vertices $V$ and a set of edges $E$ such that each edge is an ordered pair of members of $V$ under the restrictions that each vertex appears as the second member of at most one edge. If $[ v _ { 1 } , v _ { 2 } ]$ , $[ v _ { 2 } , v _ { 3 } ]$ , $\cdot \cdot ,$ $[ v _ { n - 1 } , v _ { n } ]$ are edges, we write $v _ { 1 } < v _ { n }$ . We will require this relation to be a partial ordering.

Suppose that $V$ and $E$ can be partitioned as $V ~ = ~ V _ { 1 } \cup V _ { 2 } \cup \dots \cup V _ { k }$ , $E = E _ { 1 } \cup E _ { 2 } \cup \cdot \cdot \cdot \cup E _ { k }$ , where each of $( V _ { i } , E _ { i } )$ , $i = 1 , 2 , \ldots , k$ , is connected and is therefore a rooted tree. A function $\alpha : T  \mathbb { R }$ can be extended multiplicatively to a function on the set of all forests by defining

$$
\alpha { \big ( } ( V , E ) { \big ) } = \prod _ { i = 1 } ^ { k } \alpha { \big ( } ( V _ { i } , E _ { i } ) { \big ) } .
$$

If $( V , E )$ is a forest and $\hat { V }$ is a subset of $V$ , then the sub-forest induced by $\hat { V }$ is the forest $( \widehat { V } , \widehat { E } )$ , where $\widehat { E }$ is the intersection of $\hat { V } \times \hat { V }$ and $E$ . A special

case is when a sub-forest $( \widehat { V } , \widehat { E } )$ satisfies the requirement that for any two vertices $u , v$ of $E$ such that $u < v$ and $v \in \widehat { E }$ , $u$ is also a member of $\widehat { E }$ . In this case we write

$$
( { \widehat { V } } , { \widehat { E } } ) \triangleleft ( V , E ) .
$$

From now on we write forests by single letters $Q$ , $R$ , $S$ , and interpret $R \triangleleft S$ accordingly. If $R \triangleleft S$ then $S \backslash R$ will denote the forest induced by the difference of the vertex sets of $S$ and $R$ , respectively.

We can now define a product of two multiplicative mappings of forests to real numbers. If $\alpha$ and $\beta$ are two such mappings, then we write

$$
( \alpha \beta ) ( S ) = \sum _ { R \diamond S } \alpha ( S \setminus R ) \beta ( R ) .
$$

We need to verify that $\alpha \beta$ is multiplicative if the same is true for $\alpha$ and $\beta$ .

Lemma 383A Let $\alpha$ and $\beta$ be multiplicative mappings from the forests to the real numbers. Then $\alpha \beta$ is multiplicative.

Proof. It will be sufficient to consider the value of $( \alpha \beta ) ( S )$ , where $S = S _ { 1 } \cup S _ { 2 }$ . Each $R \triangleleft S$ can be written as $R = R _ { 1 } \cup R _ { 2 }$ , where $R _ { 1 } \triangleleft S _ { 1 }$ and $R _ { 2 } \triangleleft S _ { 2 }$ . We now have

$$
\begin{array} { l } { { ( \alpha \beta ) ( S ) = \displaystyle \sum _ { R \ll S } \alpha ( S \setminus R ) \beta ( R ) } } \\ { { \ = \displaystyle \sum _ { R _ { 1 } \leqslant S _ { 1 } } \alpha ( S _ { 1 } \setminus R _ { 1 } ) \beta ( R _ { 1 } ) \sum _ { R _ { 2 } \leqslant S _ { 2 } } \alpha ( S _ { 2 } \setminus R _ { 2 } ) \beta ( R _ { 2 } ) } } \\ { { \ = ( \alpha \beta ) ( S _ { 1 } ) ( \alpha \beta ) ( S _ { 2 } ) . } } \end{array}
$$

We next show that the product we have defined is associative.

Lemma 383B Let $\alpha$ , $\beta$ and $\gamma$ be multiplicative mappings from forests to reals. Then

$$
( \alpha \beta ) \gamma = \alpha ( \beta \gamma ) .
$$

Proof. If $Q \triangleleft R \triangleleft S$ then $( R \setminus Q ) \triangleleft ( S \setminus Q )$ . Hence, we find

$$
\begin{array} { r l } { ( ( \alpha \beta ) \gamma ) ( S ) = \displaystyle \sum _ { Q + \delta } ( \alpha \beta ) ( S \setminus Q ) \gamma ( Q ) } \\ { = \displaystyle \sum _ { Q + S } \sum _ { ( R \backslash Q ) \leqslant ( S \backslash Q ) } \alpha ( ( S \setminus Q ) \setminus ( R \setminus Q ) ) \beta ( R \setminus Q ) \gamma ( Q ) } \\ { = \displaystyle \sum _ { Q + R R \cap Q \leqslant ( S \setminus R ) \beta ( R \setminus Q ) \gamma ( Q ) } } \\ { = \displaystyle \sum _ { R \neq S } \alpha ( S \setminus R ) ( \beta \gamma ) ( R ) } \\ { = \displaystyle \sum _ { R \neq S } \alpha ( S \setminus R ) ( \beta \gamma ) ( R ) } \\ { = ( \alpha ( \beta \gamma ) ) ( S ) . } \end{array}
$$

We can now restrict multiplication to trees, and we note that associativity still remains. The semi-group that has been constructed on the set $G _ { 1 }$ is actually a group because we can construct both left and right inverses, α−1left and $\alpha _ { \mathrm { r i g h t } } ^ { - 1 }$ say, for any $\alpha \in G _ { 1 }$ , which must be equal because

$$
\alpha _ { \mathrm { l e f t } } ^ { - 1 } = \alpha _ { \mathrm { l e f t } } ^ { - 1 } \left( \alpha \alpha _ { \mathrm { r i g h t } } ^ { - 1 } \right) = \left( \alpha _ { \mathrm { l e f t } } ^ { - 1 } \alpha \right) \alpha _ { \mathrm { r i g h t } } ^ { - 1 } = \alpha _ { \mathrm { r i g h t } } ^ { - 1 } .
$$

Lemma 383C Given $\alpha \in G _ { 1 }$ , there exist a left inverse and a right inverse.

Proof. We show, by induction on the order of $t$ , that it is possible to construct $\beta$ such that $( \alpha \beta ) ( t ) = 0$ or $( \beta \alpha ) ( t ) = 0$ , for all $t \in T$ . Because $( \alpha \beta ) ( \tau ) = ( \beta \alpha ) ( \tau ) = \alpha ( \tau ) + \beta ( \tau )$ , the result is clear for order 1. Suppose the result has been proved for all trees of order less than that of $t \neq \tau$ ; then we note that

$$
( \alpha \beta ) ( t ) = \alpha ( t ) + \beta ( t ) + \phi ( t , \alpha , \beta )
$$

and

$$
( \beta \alpha ) ( t ) = \alpha ( t ) + \beta ( t ) + \phi ( t , \beta , \alpha ) ,
$$

where $\phi ( t , \alpha , \beta )$ involves the values of $\alpha$ and $\beta$ only for trees with orders less than $r ( t )$ . Hence, it is possible to assign a value to $\beta ( t )$ so that $( \alpha \beta ) ( t ) = 0$ or that $( \beta \alpha ) ( t ) = 0$ , respectively. Thus it is possible to construct $\beta$ as a left inverse or right inverse of $\alpha$ . 

Having established the existence of an inverse for any $\alpha \in G _ { 1 }$ , we find a convenient formula for $\alpha ^ { - 1 }$ . We write $S$ for a tree $t$ , written in the form $( V , E )$ , and ${ \mathcal { P } } ( S )$ for the set of all partitions of $S$ . This means that if $P \in { \mathcal { P } } ( S )$ , then $P$ is a forest formed by possibly removing some of the edges from $E$ . Another way of expressing this is that the components of $P$ are trees $( V _ { i } , E _ { i } )$ , for $i = 1 , 2 , \ldots , n$ , where $V$ is the union of $V _ { 1 }$ , $V _ { 2 }$ , $\cdot \cdot \cdot$ , $V _ { n }$ and each $E _ { i }$ is a subset of $E$ . The integer $n$ , denoting the number of components of $P$ , will be written as $\# P$ . We write $t _ { i }$ as the tree represented by $( V _ { i } , E _ { i } )$ .

Lemma 383D Given $\alpha \in G _ { 1 }$ and $t \in T$ , written in the form $( V , E )$ , then

$$
\alpha ^ { - 1 } ( t ) = \sum _ { P \in \mathcal { P } ( S ) } \prod _ { i = 1 } ^ { \# P } ( - \alpha ( t _ { i } ) ) .
$$

Proof. Construct a mapping $\beta \in G _ { 1 }$ equal to the right-hand side of (383b). We show that for any $t \in T$ , $( \alpha \beta ) ( t ) = 0$ so that $\alpha \beta = 1$ . Let $t = ( V , E )$ . For any partition $P$ with components $( V _ { i } , E _ { i } )$ , for $i = 1 , 2 , \ldots , n$ , we consider the set of possible combinations of $\{ 1 , 2 , \ldots , n \}$ , with the restriction that if $C$ is such a combination, then no edge $( v _ { 1 } , v _ { 2 } ) \in E$ exists with $v _ { 1 } \in V _ { i }$ and $v _ { 2 } \in V _ { j }$ , with $i$ and $j$ distinct members of $C$ . Let $\mathcal C ( P )$ denote the set of all such combinations of $P \in \mathcal { P } ( t )$ . Given $C \in P$ , denote by $\overline { { C } }$ the complement of $C$ in $P$ .

The value of $( \alpha \beta ) ( t )$ can be written in the form

$$
\sum _ { P \in \mathcal { P } ( t ) } \sum _ { C \in \mathcal { C } ( P ) } \prod _ { i \in C } \alpha ( t _ { i } ) ( - 1 ) ^ { \# \overline { { C } } } \prod _ { j \in \overline { { C } } } \alpha ( t _ { j } ) .
$$

For any particular partition $P$ , the total contribution is

$$
\sum _ { C \in \mathcal { C } ( P ) } ( - 1 ) ^ { n - \# C } \prod _ { i = 1 } ^ { \# P } \alpha ( t _ { i } ) .
$$

This is zero because $\begin{array} { r } { \sum _ { C \in { \mathcal { C } } ( P ) } ( - 1 ) ^ { n - \# C } = 0 } \end{array}$
