# 357 Non-linear stability

The second generalization of A-stability we consider is the assumption that, even though the function $f$ is non-linear, it satisfies the condition that

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 ,
$$

where $\langle \cdot \rangle$ denotes a semi-inner product, with corresponding semi-norm defined by

$$
| \boldsymbol { u } | = \langle \boldsymbol { u } , \boldsymbol { u } \rangle ^ { 1 / 2 } .
$$

The reason for our interest in the assumption (357a) is that if there are two solutions $y$ and $z$ to the same differential equations, but with possibly different initial values, then the norm difference of $y$ and $z$ satisfies the bound

$$
| y ( x ) - z ( x ) | \leq | y ( x _ { 0 } ) - z ( x _ { 0 } ) | ,
$$

because

$$
{ \frac { d } { d x } } | y ( x ) - z ( x ) | ^ { 2 } = 2 \langle f ( y ( x ) ) - f ( z ( x ) ) , y ( x ) - z ( x ) \rangle \leq 0 .
$$

The corresponding property for a Runge–Kutta method would be that the sequences of computed solutions satisfy

$$
| y _ { n } - z _ { n } | \leq | y _ { n - 1 } - z _ { n - 1 } | .
$$

It would equally be possible to use a simpler type of test problem, such as $Y ^ { \prime } ( x ) = F ( Y ( x ) )$ , where

$$
\begin{array} { r } { \langle \langle g ( U ) , U \rangle \rangle \leq 0 , } \end{array}
$$

because (357a) can be expressed using (357c). If $\langle \cdot \rangle$ is the semi-inner product on $\mathbb { R } ^ { N }$ used in (357a), with $| \cdot |$ the corresponding semi-norm, then we can define a quasi-inner product $\langle \langle \cdot \rangle \rangle$ on $\mathbb { R } ^ { 2 N }$ , with corresponding norm $\| \cdot \|$ , by the formula

$$
\left. \left. \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] , \left[ \begin{array} { l } { \widetilde { u } } \\ { \widetilde { v } } \end{array} \right] \right. \right. = \langle u , \widetilde { u } \rangle - \langle u , \widetilde { v } \rangle - \langle v , \widetilde { u } \rangle + \langle v , \widetilde { v } \rangle .
$$

The semi-norms defined from these quasi-inner products are related by

$$
\left\| \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] \right\| = \langle \langle u - v , u - v \rangle \rangle = | u - v | ^ { 2 } ,
$$

and we can write the condition (357a) in the form

$$
\left. \left. G \left( { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right]}  \right) , { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } \right. \right. \leq 0 ,
$$

where $G$ is defined by

$$
G \left( { \left[ \begin{array} { l } { u } \\ { v } \end{array} \right] } \right) = { \left[ \begin{array} { l } { f ( u ) } \\ { f ( v ) } \end{array} \right] } .
$$

Furthermore, the requirement on a numerical method (357b) can be written in the form

$$
\| Y _ { n } \| \leq \| Y _ { n - 1 } \| .
$$

Hence we lose no generality in using a test problem which satisfies (357c) rather than the formally more complicated condition (357a). We therefore adopt this requirement, but revert to the more conventional notation of using $\langle \cdot \rangle$ for a standard semi-inner product with $\| \cdot \|$ the corresponding norm.

Even though we have simplified the notation in one way, it is appropriate to generalize it in another. We really need to avoid the use of autonomous problems because of the intimate relationship that will be found between ANstability and the type of non-linear stability we are discussing here. When Definition 357A was first introduced, it was referred to as ‘B-stability’, because it is one step more stringent than A-stability. In the non-autonomous form in which it seems to be a more useful concept, a more natural name is BNstability.

Definition 357A A Runge–Kutta $( A , b ^ { \intercal } , c )$ is ‘BN-stable’ if for any initial value problem

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

satisfying the condition

$$
\langle f ( x , u ) , u \rangle \leq 0 ,
$$

the sequence of computed solutions satisfies

$$
\left\| y _ { n } \right\| \leq \left\| y _ { n - 1 } \right\| .
$$

The crucial result is that for an irreducible non-confluent method, ANstability and BN-stability are equivalent. Because of the fundamental importance of the necessary and sufficient conditions for a Runge–Kutta method to have either, and therefore both, of these properties, we formalize these conditions:

Definition 357B A Runge–Kutta method $( A , b ^ { \prime } , c )$ is ‘algebraically stable’ if $b _ { i } > 0$ , for $i = 1 , 2 , \dots , s$ , and if the matrix $M$ , given by

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top } ,
$$

is positive semi-definite.

We now show the sufficiency of this property.

Theorem 357C If a Runge–Kutta method is algebraically stable then it is BN-stable.

Proof. Let $F _ { i } = f ( x _ { n - 1 } + h c _ { i } , Y _ { i } )$ . We note that if $M$ given by (357d) is positive semi-definite, then there exist vectors $v _ { l } \in \mathbb { R } ^ { s }$ , $l = 1 , 2 , \ldots , \overline { { s } } \leq s$ , such that

$$
M = \sum _ { l = 1 } ^ { \overline { { s } } } \mu _ { l } \mu _ { l } ^ { \intercal } .
$$

This means that a quadratic form can be written as the sum of squares as follows:

$$
\xi ^ { \mathsf { T } } M \xi = \sum _ { l = 1 } ^ { \overline { { s } } } ( \mu _ { l } ^ { \mathsf { T } } \xi ) ^ { 2 } .
$$

Furthermore, a quadratic form of inner products

$$
\sum _ { i , j = 1 } ^ { s } m _ { i j } \langle U _ { i } , U _ { j } \rangle
$$

is equal to

$$
\sum _ { l = 1 } ^ { \overline { { s } } } \Big \| \sum _ { i = 1 } ^ { s } \mu _ { l i } U _ { i } \Big \| ^ { 2 } ,
$$

and cannot be negative. We show that

$$
\| y _ { n } \| - \| y _ { n - 1 } \| ^ { 2 } = 2 h \sum _ { i = 1 } ^ { s } b _ { i } \langle Y _ { i } , F _ { i } \rangle - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } m _ { i j } \langle F _ { i } , F _ { j } \rangle ,
$$

so that the result will follow. To prove (357e), we use the equations

$$
\begin{array} { l } { { \displaystyle Y _ { i } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } a _ { i j } F _ { j } } , } \\ { { \displaystyle Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) F _ { j } } , } \end{array}
$$

which hold for $i = 1 , 2 , \dots , s$ . In each case, form the quasi-inner product with $F _ { i }$ , and we find

$$
\begin{array} { l } { { \langle Y _ { i } , F _ { i } \rangle = \langle y _ { n - 1 } , F _ { i } \rangle + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } \langle F _ { i } , F _ { j } \rangle , } } \\ { { } } \\ { { \langle Y _ { i } , F _ { i } \rangle = \langle y _ { n } , F _ { i } \rangle + h \displaystyle \sum _ { j = 1 } ^ { s } ( a _ { i j } - b _ { j } ) \langle F _ { i } , F _ { j } \rangle . } } \end{array}
$$

Hence,

$$
\begin{array} { c } { { 2 h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \big \langle Y _ { i } , F _ { i } \big \rangle = \Big \langle y _ { n } + y _ { n - 1 } , h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } \Big \rangle } } \\ { { = h ^ { 2 } \displaystyle \sum _ { i , j = 1 } ^ { s } ( 2 b _ { i } a _ { i j } - b _ { i } b _ { j } ) \big \langle F _ { i } , F _ { j } \big \rangle . } } \end{array}
$$

Substitute $y _ { n }$ and $y _ { n - 1 }$ from (357f) and (357g) and rearrange to deduce (357e).

Our final aim in this discussion of non-autonomous and non-linear stability is to show that BN-stability implies AN-stability. This will give the satisfactory conclusion that algebraic stability is equivalent to each of these concepts.

Because we have formulated BN-stability in terms of a quasi-inner product over the real numbers, we first need to see how (356a) can be expressed in a suitable form. Write the real and imaginary parts of $q ( x )$ as $\alpha ( x )$ and $\beta ( x )$ , respectively. Also write $y ( x ) = \xi ( x ) + i \eta ( x )$ and write $\zeta ( x )$ for the function with values in $\mathbb { R } ^ { 2 }$ whose components are $\xi ( x )$ and $\eta ( x )$ , respectively.

Thus, because

$$
\begin{array} { c } { { y ^ { \prime } ( x ) = ( \alpha ( x ) + i \beta ( x ) ) ( \xi ( x ) + i \eta ( x ) ) } } \\ { { { } } } \\ { { { } = ( \alpha ( x ) \xi ( x ) - \beta ( x ) \eta ( x ) ) + i ( \beta ( x ) \xi ( x ) + \alpha ( x ) \eta ( x ) ) , } } \end{array}
$$

we can write

$$
\zeta ^ { \prime } ( x ) = Q \zeta ,
$$

where

$$
Q = \left[ \begin{array} { c c } { { \alpha ( x ) } } & { { - \beta ( x ) } } \\ { { \beta ( x ) } } & { { \alpha ( x ) } } \end{array} \right] .
$$

Using the usual inner product we now have the dissipativity property

$$
\begin{array} { r } { \langle Q v , v \rangle = \alpha \| v \| ^ { 2 } \leq 0 , } \end{array}
$$

if $\alpha \leq 0$

What we have found is that the test problem for AN-stability is an instance of the test problem for BN-stability. This means that we can complete the chain of equivalences interconnecting AN-stability, BN-stability and algebraic stability. The formal statement of the final step is as follows:

Theorem 357D If an irreducible non-confluent Runge–Kutta method is BNstable, then it is AN-stable.
