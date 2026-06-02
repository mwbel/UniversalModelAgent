# 358 BN-stability of collocation methods

In the case of methods satisfying the collocation conditions

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \qquad \quad \quad i , k = 1 , 2 , \ldots , s , } } \\ { { \displaystyle \quad \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , \qquad \quad \quad k = 1 , 2 , \ldots , s , } } \end{array}
$$

a congruence transformation of $M$ , using the Vandermonde matrix

$$
V = { \left[ \begin{array} { l l l l l } { \mathbf { 1 } } & { c } & { c ^ { 2 } } & { \cdots } & { c ^ { s - 1 } } \end{array} \right] } ,
$$

where powers of $c$ are interpreted in a componentwise manner, leads to considerable simplification. Denote

$$
\epsilon _ { k } = \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } - \frac { 1 } { k } , \qquad k = 1 , 2 , \ldots , 2 s ,
$$

so that $\epsilon _ { 1 } = \epsilon _ { 2 } = \cdot \cdot \cdot = \epsilon _ { s } = 0$ . Calculate the $( k , l )$ element of $V ^ { \prime } M V$ . This has the value

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 1 } ^ { s } c _ { i } ^ { k - 1 } \sum _ { j = 1 } ^ { s } c _ { j } ^ { l - 1 } \big ( b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } \big ) } & { } \\ { = \displaystyle \sum _ { i = 1 } ^ { s } \frac { 1 } { l } b _ { i } c _ { i } ^ { k + l - 1 } + \sum _ { j = 1 } ^ { s } \frac { 1 } { k } b _ { j } c _ { j } ^ { k + l - 1 } - \frac { 1 } { k l } } & { } \\ { } & { = \displaystyle \frac { 1 } { l ( k + l ) } + \frac { 1 } { l } \epsilon _ { k + l } + \frac { 1 } { k ( k + l ) } + \frac { 1 } { k } \epsilon _ { k + l } - \frac { 1 } { k l } } \\ { } & { = \displaystyle \frac { k + l } { k l } \epsilon _ { k + l } . } \end{array}
$$

Thus,

$$
{ \boldsymbol { r } } ^ { \mathsf { T } } M V = { \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { { \frac { s + 1 } { s } } \epsilon _ { s + 1 } } \\ & { 0 } & { 0 } & { \cdots } & { { \frac { s + 1 } { 2 ( s - 1 ) } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 2 s } } \epsilon _ { s + 2 } } \\ & { 0 } & { 0 } & { \cdots } & { { \frac { s + 2 } { 3 ( s - 1 ) } } \epsilon _ { s + 2 } } & { { \frac { s + 3 } { 3 s } } \epsilon _ { s + 3 } } \\ & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ & & { { \frac { s + 1 } { 2 ( s - 1 ) } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 3 ( s - 1 ) } } \epsilon _ { s + 2 } } & { \cdots } & { { \frac { 2 s - 2 } { ( s - 1 ) ^ { 2 } } } \epsilon _ { 2 s - 2 } } & { { \frac { 2 s - 1 } { s ( s - 1 ) } } \epsilon _ { 2 s - 1 } } \\ & { { \frac { s + 1 } { s } } \epsilon _ { s + 1 } } & { { \frac { s + 2 } { 2 s } } \epsilon _ { s + 2 } } & { { \frac { s + 3 } { 3 s } } \epsilon _ { s + 3 } } & { \cdots } & { { \frac { 2 s - 1 } { s ( s - 1 ) } } \epsilon _ { 2 s - 1 } } & { { \frac { 2 s } { s ^ { 2 } } } \epsilon _ { 2 s } } \end{array} \right] } .
$$

A symmetric positive semi-definite matrix cannot have a zero diagonal element unless all the elements on the same row and column are also zero. Hence, we deduce that $\epsilon _ { i } = 0$ for $i = s + 1 , s + 2 , \ldots , 2 s - 1$ . Thus, the only way for $M$ to be positive semi-definite is that

$$
V ^ { \top } M V = \frac { 2 s } { s ^ { 2 } } \epsilon _ { 2 s } e _ { s } e _ { s } ^ { \top }
$$

and that

$$
\epsilon _ { 2 s } \geq 0 .
$$

Combining these remarks with a criterion for (358a), we state:

Theorem 358A A collocation Runge–Kutta method is algebraically stable if and only if the abscissae are zeros of a polynomial of the form

$$
\begin{array} { r } { P _ { s } ^ { * } - \theta P _ { s - 1 } ^ { * } , } \end{array}
$$

where $\theta \geq 0$ .

Proof. Because $\epsilon _ { i } = 0$ for $i = 1 , 2 , \ldots , 2 s - 1$ , it follows that

$$
\int _ { 0 } ^ { 1 } P ( x ) \phi ( x ) d x = 0 ,
$$

where $\phi ( x )$ is a polynomial of degree $s$ , with positive leading coefficient and zeros $c _ { 1 }$ , $c _ { 2 }$ , . . . , $c _ { s }$ and $P$ is any polynomial of degree not exceeding $s - 2$ . Furthermore, if $P$ is a polynomial of degree $s - 1$ and positive leading coefficient, the integral in (358c) has the same sign as $- \epsilon _ { 2 s }$ . Because of the orthogonality of $\phi$ and polynomials of degree less than $s - 1$ , $\phi$ is a positive constant multiple of (358b). Apart from a positive factor, we can now evaluate the integral in (358c), with $P ( x ) = P _ { s - 1 } ^ { * } ( x )$ ,

$$
\int _ { 0 } ^ { 1 } P _ { s - 1 } ^ { * } ( x ) ( P _ { s } ^ { * } ( x ) - \theta P _ { s - 1 } ^ { * } ( x ) ) d x = - \theta \int _ { 0 } ^ { 1 } P _ { s - 1 } ^ { * } ( x ) ^ { 2 } d x ,
$$

which has the opposite sign to $\theta$ .

A consequence of this result is that both Gauss and Radau IIA methods are algebraically stable. Many other methods used for the solution of stiff problems have stage order lower than $s$ and are therefore not collocation methods. A general characterization of algebraic stable methods is found by using a transformation based not on the Vandermonde matrix $V$ , but on a generalized Vandermonde matrix based on the polynomials that are essentially the same as $P _ { i } ^ { * }$ , for $i = 0 , 1 , 2 , \ldots , s - 1$ .
