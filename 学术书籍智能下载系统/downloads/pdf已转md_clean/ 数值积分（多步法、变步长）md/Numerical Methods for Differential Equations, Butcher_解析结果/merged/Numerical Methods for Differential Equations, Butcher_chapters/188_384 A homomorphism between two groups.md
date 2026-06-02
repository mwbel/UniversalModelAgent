# 384 A homomorphism between two groups

We show that the groups introduced in Subsections 382 and 383 are related in such a way that the former is isomorphic to a subgroup of the latter. The mapping between elements of the group that provides this homomorphism maps an equivalence class of Runge–Kutta methods to the function on $T$ to $\mathbb { R }$ defined by the elementary weights associated with a representative member of the class. We need to establish that products in the first group are preserved in the second. This means that if $m$ and $\widehat { m }$ are Runge–Kutta methods and $\Phi : T  \mathbb { R }$ and $\widehat \Phi : T  \mathbb { R }$ are the elementary weight functions for $m$ and $\widehat { m }$ , respectively, then $\Phi \widehat \Phi$ is the elementary weight function associated with $m \widehat { m }$ .

Theorem 384A Let $\Phi : T  \mathbb { R }$ be the elementary weight function associated with $( A , b ^ { \prime } , c )$ and $\widehat \Phi : T \to \mathbb { R }$ the elementary weight function associated with $( \widehat { A } , \widehat { b } ^ { \intercal } , \widehat { c } )$ . Let $\widetilde { \Phi } : T  \mathbb { R }$ denote the elementary weight function for the product method as represented by (382a). Then

$$
{ \widetilde { \Phi } } = \Phi { \widehat { \Phi } } .
$$

Proof. Denote the $( s + { \widehat { s } } )$ -stage composite coefficient matrices by $( \widetilde { A } , \widetilde { b } ^ { \intercal } , \widetilde { c } )$ with the elements of $\ddot { A }$ and $\widetilde { b } ^ { \intercal }$ given by

$$
\begin{array} { r l } & { \widetilde { a } _ { i j } = \left\{ \begin{array} { l l } { a _ { i j } , } & { i \leq s , j \leq s , } \\ { 0 , } & { i \leq s , j > s , } \\ { b _ { j } , } & { i > s , j \leq s , } \\ { \widehat { a } _ { i - s , j - s } , } & { i > s , j > s . } \end{array} \right. } \\ & { \widetilde { b } _ { i } = \left\{ \begin{array} { l l } { b _ { i } , } & { i \leq s , } \\ { \widehat { b } _ { i - s } , } & { i > s . } \end{array} \right. } \end{array}
$$

For a tree $t$ , such that $r ( t ) = n$ , represented by the vertex–edge pair $( V , E )$ , with root $\rho \in V$ , write the elementary weight $ { \widetilde { \Phi } } ( t )$ in the form

$$
\widetilde { \Phi } ( t ) = \sum _ { i \in I } \widetilde { b } _ { i ( \rho ) } \prod _ { ( v , w ) \in E } \widetilde { a } _ { i ( v ) , i ( w ) } .
$$

In this expression, $I$ is the set of all mappings from $V$ to the set $\{ 1 , 2 , \ldots , { \widetilde { s } } \}$ and, for $i \in I$ and $v \in V$ , $i ( v )$ denotes the value to which the vertex $v$ maps.

If $v \ < \ w$ and $i ( v ) \leq s < i ( w )$ then the corresponding term in (384a) is zero. Hence, we sum only over $I ^ { \prime }$ defined as the subset of $I$ from which such $i$ are omitted. For any $i \in I ^ { \prime }$ , define $R \triangleleft S = ( V , E )$ such that all the vertices associated with $R$ map into $\{ s + 1 , s + 2 , \ldots , s + \widehat { s } \}$ . Collect together all $i \in I ^ { \prime }$ which share a common $R$ so that (384a) can be written in the form

$$
\widetilde { \Phi } ( t ) = \sum _ { R \leqslant S } \sum _ { i \in I _ { R } } \widetilde { b } _ { i ( \rho ) } \prod _ { ( v , w ) \in E } \widetilde { a } _ { i ( v ) , i ( w ) } .
$$

For each $R$ , the terms in the sum have total value $\Phi ( S \setminus R ) { \widehat { \Phi } } ( R )$ , and the result follows. $\sqcup$
