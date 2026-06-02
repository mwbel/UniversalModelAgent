# 532 Algebraic analysis of order

Associated with each of the components of the vector of starting methods is a member of the algebra $G$ introduced in Subsection 385. Denote $\xi _ { i }$ , $i = 1 , 2 , \ldots , r$ , as the member corresponding to $S _ { i }$ . That is, $\xi _ { i }$ is defined by

$$
\begin{array} { l } { { \displaystyle \xi _ { i } ( \emptyset ) = b _ { 0 } ^ { ( i ) } , } } \\ { { \displaystyle \xi _ { i } ( t ) = \Phi ^ { ( i ) } ( t ) , \quad t \in T , } } \end{array}
$$

where the elementary weight $\Phi ^ { ( i ) } ( t )$ is defined from the tableau (530a). Associate $\eta _ { i } \in G _ { 1 }$ with stage $i = 1 , 2 , \dots , s$ , and define this recursively by

$$
\eta _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } \eta _ { j } D + \sum _ { j = 1 } ^ { r } U _ { i j } \xi _ { j } .
$$

Having computed $\eta _ { i }$ and $\eta _ { i } D$ , $i = 1 , 2 , \dots , s$ , we are now in a position to compute the members of $G$ representing the output approximations. These are given by

$$
\sum _ { j = 1 } ^ { s } b _ { i j } \eta _ { j } D + \sum _ { j = 1 } ^ { r } V _ { i j } \xi _ { j } , \qquad i = 1 , 2 , \ldots , r .
$$

If the method is of order $p$ , this will correspond to $E \xi _ { i }$ , within $H _ { p }$ . Hence, we may write the algebraic counterpart to the fact that the method $M$ is of order $p$ , relative to the starting method $S$ , as

$$
E \xi _ { i } = \sum _ { j = 1 } ^ { s } b _ { i j } \eta _ { j } D + \sum _ { j = 1 } ^ { r } V _ { i j } \xi _ { j } , \qquad \mathrm { i n ~ } G / H _ { p } , i = 1 , 2 , \ldots , r .
$$

Because (532b) represents a Taylor expansion, the expression

$$
E \xi _ { i } - \sum _ { j = 1 } ^ { s } b _ { i j } \eta _ { j } D - \sum _ { j = 1 } ^ { r } V _ { i j } \xi _ { j } , \qquad i = 1 , 2 , \ldots , r ,
$$

represents the amount by which $y _ { i } ^ { \left[ n \right] }$ falls short of the value that would be found if there were no truncation error. Hence, (532d) is closely related to the local truncation error in approximation $i$ .

Before attempting to examine this in more detail, we introduce a vector notation which makes it possible to simplify the way formulae such as (532a) and (532c) are expressed. The vector counterparts are

$$
\begin{array} { r } { \eta = A \eta D + U \xi , } \\ { E \xi = B \eta D + V \xi , } \end{array}
$$

where these formulae are to be interpreted in the space $G / H _ { p }$ . That is, the two sides of (532e) and of (532f) are to be equal when evaluated for all $t \in T ^ { \# }$ such that $r ( t ) \leq p$ .

Theorem 532A Let $M = ( A , U , B , V )$ denote a general linear method and let $\xi$ denote the algebraic representation of a starting method $S$ . Assume that (532e) and (532f) hold in $G / H _ { p }$ . Denote

$$
\epsilon = E \xi - B \eta D - V \xi , \qquad i n \ : G .
$$

Then the Taylor expansion of $S ( y ( x _ { 0 } + h ) ) - M ( S ( y ( x _ { 0 } ) ) )$ is

$$
\sum _ { r ( t ) > p } \frac { \epsilon ( t ) } { \sigma ( t ) } h ^ { r ( t ) } F ( t ) ( y ( x _ { 0 } ) ) .
$$

Proof. We consider a single step from initial data given at $x _ { 0 }$ and consider the Taylor expansion of various expressions about $x _ { 0 }$ . The input approximation, computed by $S$ , has Taylor series represented by $\xi$ . Suppose the Taylor expansions for the stage values are represented by $\eta$ so that the stage derivatives will be represented by $\eta D$ and these will be related by (532e). The Taylor expansion for the output approximations is represented by $B \eta D + V \xi$ , and this will agree with the Taylor expansion of $S ( y ( x _ { 0 } + h ) )$ up to $h ^ { p }$ terms if (532f) holds. The difference from the target value of $S ( y ( x _ { 0 } + h ) )$ is given by (532g). $\boxed { \begin{array} { r l } \end{array} }$
