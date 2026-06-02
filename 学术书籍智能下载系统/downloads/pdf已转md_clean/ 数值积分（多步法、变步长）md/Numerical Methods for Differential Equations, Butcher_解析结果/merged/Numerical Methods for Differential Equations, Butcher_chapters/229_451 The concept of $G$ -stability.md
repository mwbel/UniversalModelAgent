# 451 The concept of $G$ -stability

We recall the non-linear stability property introduced in Subsection 357. The corresponding property for one-leg methods was introduced in Dahlquist (1976) and given the name G-stability. For convenience, we consider applications only to autonomous problems

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) ,
$$

and we assume that the dissipativity property holds in the sense that solution values lie in an $N$ -dimensional inner-product space, and that

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 ,
$$

for all $u , v \in \mathbb { R } ^ { N }$ .

For Runge–Kutta methods, in the study of the non-linear stability property applicable to those methods, in Subsection 357, it was possible to use the norm $\| u \| = \sqrt { \langle u , u \rangle }$ to measure the drift between two approximately equal numerical approximations that takes place in step $n$ . However, for linear $k$ - step methods, each of the $k$ subvectors making up the current state vector of each approximate solution has to be taken into account. Hence, we need to construct a suitable norm on the vector space RkN .

For $U \in \mathbb { R } ^ { k N }$ , write $U _ { i }$ , $i = 1 , 2 , \ldots , k$ , for subvectors in $\mathbb { R } ^ { N }$ . That is,

$$
\begin{array} { r } { \boldsymbol { U } = \left[ \begin{array} { c } { \boldsymbol { U } _ { 1 } } \\ { \boldsymbol { U } _ { 2 } } \\ { \vdots } \\ { \boldsymbol { U } _ { k } } \end{array} \right] . } \end{array}
$$

If $U , V \in \mathbb { R } ^ { k N }$ then, given a positive definite symmetric $k \times k$ matrix $G$ , we can define an inner product $\langle \cdot \rangle _ { G }$ by

$$
\langle U , V \rangle _ { G } = \sum _ { i , j = 1 } ^ { k } g _ { i j } \langle U _ { i } , V _ { j } \rangle ,
$$

with corresponding norm

$$
\| U \| _ { G } = \sqrt { \sum _ { i , j = 1 } ^ { k } g _ { i j } \langle U _ { i } , U _ { j } \rangle } .
$$

The aim of G-stability is to discover, for a given one-leg method, if $G$ exists so that, for a problem satisfying (451b),

$$
\left\| Y ^ { ( n ) } - Z ^ { ( n ) } \right\| _ { G } ^ { 2 } - \left\| Y ^ { ( n - 1 ) } - Z ^ { ( n - 1 ) } \right\| _ { G } ^ { 2 }
$$

cannot be positive, where

$$
Y ^ { ( n ) } = \left[ \begin{array} { c } { { y _ { n } } } \\ { { y _ { n - 1 } } } \\ { { y _ { n - 2 } } } \\ { { \vdots } } \\ { { y _ { n - k + 1 } } } \end{array} \right] , \qquad Z ^ { ( n ) } = \left[ \begin{array} { c } { { z _ { n } } } \\ { { z _ { n - 1 } } } \\ { { z _ { n - 2 } } } \\ { { \vdots } } \\ { { z _ { n - k + 1 } } } \end{array} \right] ,
$$

and the $y$ and $z$ sequences are numerical approximations corresponding to two different solutions to (451a).

The only inequality at our disposal that could be used to ensure that (451c) is not positive is the dissipativity requirement applied to the only evaluations of $f$ that take place in the step. That is, we can use the fact that

$$
\bigg \langle f \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } y _ { n - i } \bigg ) - f \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } z _ { n - i } \bigg ) , \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } ( y _ { n - i } - z _ { n - i } ) \bigg \rangle \leq 0 .
$$

Because

$$
y _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } = { \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) } ^ { - 1 } f \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } y _ { n - i } \bigg ) ,
$$

with a similar formula for the $z$ sequence, it follows that

$$
\left. y _ { n } - z _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } ( y _ { n - i } - z _ { n - i } ) , \sum _ { i = 0 } ^ { k } \beta _ { i } ( y _ { n - i } - z _ { n - i } ) \right. \leq 0 ,
$$

and this will imply that (451c) has the correct sign if $G$ can be selected so that the $( k + 1 ) \times ( k + 1 )$ matrix $M$ is positive semi-definite, where

$$
\boldsymbol { M } = \alpha \beta ^ { \intercal } + \beta \alpha ^ { \intercal } - \left[ \begin{array} { c c } { G } & { 0 } \\ { 0 } & { 0 } \end{array} \right] + \left[ \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { G } \end{array} \right] ,
$$

where, in this context, $\alpha$ and $\beta$ are the vectors

$$
\alpha = \left[ \begin{array} { c } { 1 } \\ { - \alpha _ { 1 } } \\ { - \alpha _ { 2 } } \\ { \vdots } \\ { - \alpha _ { k } } \end{array} \right] , \qquad \beta = \left[ \begin{array} { c } { \beta _ { 0 } } \\ { \beta _ { 1 } } \\ { \beta _ { 2 } } \\ { \vdots } \\ { \beta _ { k } } \end{array} \right] .
$$

Let $m _ { i j }$ , $i , j ~ = ~ 0 , 1 , 2 , \ldots , k$ , denote the elements of $M$ . For any vector $U \in \mathbb { R } ^ { ( k + 1 ) N }$ , the fact that $M$ is positive semi-definite implies that

$$
\sum _ { i , j = 0 } ^ { k } m _ { i j } \langle U _ { i } , U _ { j } \rangle \geq 0 .
$$

Choose the vector

$$
U = \left[ \begin{array} { c } { y _ { n } - z _ { n } } \\ { y _ { n - 1 } - z _ { n - 1 } } \\ { y _ { n - 2 } - z _ { n - 2 } } \\ { \vdots } \\ { y _ { n - k + 1 } - z _ { n - k + 1 } } \\ { y _ { n - k } - z _ { n - k } } \end{array} \right] ,
$$

and we have the identity

$$
\begin{array} { r l } {  { \sum _ { i , j = 0 } ^ { k } m _ { i j } \langle y _ { n - i } - z _ { n - i } , y _ { n - j } - z _ { n - j } \rangle } \quad } & { } \\ & { = 2 \Big \langle y _ { n } - z _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \big ( y _ { n - i } - z _ { n - i } \big ) , \displaystyle \sum _ { i = 0 } ^ { k } \beta _ { i } \big ( y _ { n - i } - z _ { n - i } \big ) \Big \rangle } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad + \big \| Y ^ { ( n - 1 ) } - Z ^ { ( n - 1 ) } \big \| _ { G } ^ { 2 } - \big \| Y ^ { ( n ) } - Z ^ { ( n ) } \big \| _ { G } ^ { 2 } . } \end{array}
$$

If the left-hand side is non-negative, and the first term on the right is nonpositive, it follows that

$$
\| Y ^ { ( n ) } - Z ^ { ( n ) } \| _ { G } \leq \| Y ^ { ( n - 1 ) } - Z ^ { ( n - 1 ) } \| _ { G } .
$$

The positive semi-definiteness of $M$ was recognized by Dahlquist (1976) as just the right condition to identify methods that behave stably for the type of non-linear problem we are considering. Accordingly we state the following definition:

Definition 451A A one-leg method $\lfloor \alpha , \beta \rfloor$ is ‘ $G$ -stable’ if M given by (451e) is positive semi-definite.

We present the example of the BDF2 method with

$$
[ \alpha ( z ) , \beta ( z ) ] = \Big ( 1 - \frac { 4 } { 3 } z + \frac { 1 } { 3 } z ^ { 2 } , \frac { 2 } { 3 } \Big ) .
$$

Write

$$
G = { \left[ \begin{array} { l l } { g _ { 1 1 } } & { g _ { 1 2 } } \\ { g _ { 1 2 } } & { g _ { 2 2 } } \end{array} \right] }
$$

and we find

$$
M = \left[ \begin{array} { c c c } { { \frac 4 3 - g _ { 1 1 } } } & { { - \frac 8 9 - g _ { 1 2 } } } & { { \frac 2 9 } } \\ { { - \frac 8 9 - g _ { 1 2 } } } & { { g _ { 1 1 } - g _ { 2 2 } } } & { { g _ { 1 2 } } } \\ { { \frac 2 9 } } & { { g _ { 1 2 } } } & { { g _ { 2 2 } } } \end{array} \right] ,
$$

which is positive semi-definite if and only if $G$ is the positive definite matrix

$$
G = \left[ \begin{array} { r r } { { \frac { 1 0 } { 9 } } } & { { - \frac { 4 } { 9 } } } \\ { { - \frac { 4 } { 9 } } } & { { \frac { 2 } { 9 } } } \end{array} \right] .
$$

452 Transformations relating one-leg and linear multistep methods

Denote the point at which the derivative is calculated in step $n$ of a one-leg method by ${ \hat { y } } _ { n }$ . Also denote the corresponding $x$ argument as ${ \widehat { x } } _ { n }$ . Hence, we have

$$
\begin{array} { l } { \displaystyle \widehat { x } _ { n } = x _ { n } - \frac { \sum _ { i = 0 } ^ { k } i \beta _ { i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } h , } \\ { \displaystyle \widehat { y } _ { n } = \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) ^ { - 1 } \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n - i } , } \\ { \displaystyle y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { n - i } y _ { n - i } + \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) f ( \widehat { x } _ { n } , \widehat { y } _ { n } ) . } \end{array}
$$

Form a linear combination of ${ \widehat { y } } _ { n - i }$ , $i = 0 , 1 , \ldots , k$ , given by (452b), based on the coefficients in the $\alpha$ polynomial, and note that the operators $\alpha ( E ^ { - 1 } )$ and $\beta ( E ^ { - 1 } )$ are commutative. We have

$$
{ \widehat { y } } _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } { \widehat { y } } _ { n - i } = h \sum _ { i = 1 } ^ { k } \beta _ { i } f ( { \widehat { x } } _ { n } , { \widehat { y } } _ { n } ) .
$$

The relationship between the $y$ and $\hat { y }$ sequences given by (452b) and (452d) was suggested by Dahlquist (1976) as an indication that stability questions for a linear multistep method can be replaced by similar questions for the corresponding one-leg method.
