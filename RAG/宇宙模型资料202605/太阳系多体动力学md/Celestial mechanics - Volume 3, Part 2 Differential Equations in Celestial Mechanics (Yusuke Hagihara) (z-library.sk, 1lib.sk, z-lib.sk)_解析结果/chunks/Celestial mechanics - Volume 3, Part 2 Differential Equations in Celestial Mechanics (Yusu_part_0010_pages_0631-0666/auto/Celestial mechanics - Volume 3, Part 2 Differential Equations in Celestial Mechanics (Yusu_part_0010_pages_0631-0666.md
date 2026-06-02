maintain the stability of the origin $x = 0$ we use a compensating mechanism, i.e.,a control (Section 16.6).Let $\xi$ be a scalar parameter and $\xi = 0$ be a state of no control. The new equations of motion corresponding to the linearized system ${ \dot { y } } = A y$ from $\dot { y } = Y ( y , t )$ are

$$
x \equiv \dot { y } = A y + \xi b , \dot { \xi } = f ( \sigma ) , \sigma = c ^ { T } y - r \pounds ,
$$

where $b , c$ are $_ n$ -vectors and $r$ a scalar, $\pmb { \sigma }$ is introduced as an intermediate, $f ( \sigma )$ is the characteristic of the servomechanism,and $c ^ { T }$ is the transposed matrix of $\pmb { c }$ .We assume that $\sigma f ( \sigma ) > 0$ for $\sigma \neq 0$ ， $f ( 0 ) = 0$ ，where $f ( 0 )$ is continuous and $\int ^ { \pm \infty } f ( \sigma ) d \sigma = + \infty$

A Liapounov function $V ( { \dot { y } } , t ) \equiv V ( \dot { x , \sigma } )$ ， such that

$$
\dot { V } = \frac { \partial V } { \partial t } + Y { \cdot } \operatorname { g r a d } V ,
$$

is needed in this case in the form

$$
V ( x , \sigma ) = x ^ { T } \cdot B x + \int _ { 0 } ^ { \sigma } f ( \sigma ) d \sigma , \qquad B > 0 , \qquad B ^ { T } = B ,
$$

with the symmetric matrix $\pmb { B }$ . This is positive-definite over the whole space $( x , \sigma )$ , except for $V ( 0 , 0 ) = 0$ and $V$ and its first partial derivatives are continuous throughout the whole space. Moreover $V$ is the sum of two terms: the first term,which is positive for all $x \neq 0$ ，and the second term,which is positive for all $\sigma \neq 0$ .Hence the sum can only vanish if $x = 0$ ， $\sigma = 0$ ,and is positive otherwise. Our assumption on $f ( \sigma )$ also imply that $V ( x , \sigma ) \to \infty$ as $\| { \boldsymbol { x } } \| ^ { 2 } + \sigma ^ { 2 } \to \infty$

By means of (190) we find

$$
\begin{array} { r l } & { \dot { V } ( x , \sigma ) = \dot { x } ^ { T } B x + x ^ { T } B \dot { x } + f ( \sigma ) \dot { \sigma } = x ^ { T } ( A ^ { T } B + B A ) x - r f ^ { 2 } ( \sigma ) } \\ & { \qquad + \ 2 f ( \sigma ) \{ \frac { 1 } { 2 } ( b ^ { T } B x + x ^ { T } B b ) + \frac { 1 } { 2 } c ^ { T } x \} } \end{array}
$$

Since the transposed matrix $B ^ { T } = B$ ， we have

$$
b ^ { T } B x + x ^ { T } B b = 2 b ^ { T } B x = 2 ( B b ) ^ { T } \cdot x .
$$

Put

$$
A ^ { r } B + B A = - C ;
$$

then

$$
C ^ { T } = - ( A ^ { T } B + B A ) ^ { T } = - ( B A + A ^ { T } B ) = C .
$$

Hence $C$ is the matrix of a quadratic form,and we obtain

$$
\dot { V } = - x ^ { T } C x - r f ^ { 2 } ( \sigma ) + 2 f ( \sigma ) ( B b + { \textstyle { \frac { 1 } { 2 } } } c ) ^ { T } x .
$$

Thus $\dot { V }$ is a quadratic form in $x _ { 1 } , \ldots , x _ { n }$ , and in $f ( \sigma )$ . By the theorem just quoted this should be negative-definite for complete stability.

It can be shown that $\pmb { B }$ determines $C$ uniquely. We consider the converse.

Let $\lambda _ { 1 } , \ldots , \lambda _ { n }$ be the characteristic roots of $\pmb { A }$ ， each repeated as often as its multiplicity in the characteristic equation.It can be shown that if every sum $\lambda _ { j } + \lambda _ { k } \neq 0$ ,then the symmetric matrix $\pmb { B }$ is uniquely determined by the symmetric matrix $C$ .Thus(192) is a one-to-one relation between the two matrices.

If $\pmb { A }$ is stable, then $\lambda _ { j } + \lambda _ { k } \neq 0$ ，and we have

$$
b _ { i k } = b _ { k i } , \qquad \sum _ { k } ( a _ { h i } b _ { h k } + a _ { h k } b _ { h i } ) = - c _ { i k } \qquad ( i \equiv k ) ,
$$

where $\boldsymbol { b } _ { i k } , a _ { i k }$ are the elements of the matrices $B , A$ respectively.This relation is unaltered by any nonsingular transformation of the coordinates.

Assume that $\pmb { A }$ is stable.It can be proved that if $C$ is positive, then the unique solution $\pmb { B }$ of (194)，which exists，is likewise positive (LaSalle and Lefschetz, 1961 ;Lefschetz, 1949).

Take any matrix $C > 0$ and let $B > 0$ be the unique symmetric matrix solution of (192),and form $V ( x , \sigma )$ ； then $V ( x , \sigma )$ is positivedefinite for all $( x , \sigma )$ . The derivative $\dot { V }$ is a quadratic form in $x , f ( \sigma )$ To have $- \dot { V } > 0$ for all $x , f$ we must satisfy the well-known $n + 1$ determinantal inequalities of Sylvester (Section 16.3). Since $C > 0$ the first $_ n$ are already fulfilled. There remains the last one

$$
\left| { \begin{array} { c c } { C } & { - ( B b + { \frac { 1 } { 2 } } c ) } \\ { - ( B b + { \frac { 1 } { 2 } } c ) ^ { T } } & { r } \end{array} } \right| > 0 .
$$

It is the necessary and sufficient condition for $- \dot { V } > 0$ for all $x$ and with $f ( \sigma ) \neq 0$ Since $| C ^ { - 1 } | = | C | ^ { - 1 } > 0$ ，the determinant of the matrix $\binom { C ^ { - 1 } } { 0 } \binom { 0 } { 1 }$ isposive. Hencehedeteinantofteproductfthse two matrices

$$
\binom { I } { - ( B b + \frac { 1 } { 2 } c ) } \quad \begin{array} { c } { { - C ^ { - 1 } ( B b + \frac { 1 } { 2 } c ) } } \\ { { r } } \end{array}
$$

is,except for a positive factor, the same as in (195). Accordingly (195) is equivalent to

$$
r > ( B b + \textstyle { \frac { 1 } { 2 } } c ) ^ { \tau } C ^ { - 1 } ( B b + \textstyle { \frac { 1 } { 2 } } c ) .
$$

La Salle showed that this inequality implies that $r > - c ^ { \tau } A ^ { - 1 } b$ and therefore that

$$
r + c ^ { T } A ^ { - 1 } b \neq 0 .
$$

The inequality (196) is our fundamental control inequality. By the above theorem it implies the complete stability of the control system for all allowable functions $f ( \sigma )$

Since $C > 0$ we see that $C ^ { - 1 } > 0$ . Consequently the right-hand member of (196) is nonnegative,and this fundamental inequality implies that $r > 0$ .The control effciency should increase with $r _ { : }$ as this means moving away from the situation where $\dot { V }$ ceases to be negative-definite,and so to augment the efficiency of the control mechanism. The extent to which this is true requires investigation.

For example, let the characteristic roots be $- \mu _ { 1 } , \ldots , - \mu _ { n }$ ，where the $\mu$ are all distinct and positive. Choose $x$ such that $A = - D$ ， $D =$ diag $( \mu _ { 1 } , \ldots , \mu _ { n } )$ ； then the nonperturbed system (190) becomes

$$
\dot { x } = - D x + f ( \sigma ) b , \qquad \dot { \sigma } = c ^ { T } x - r f ( \sigma ) .
$$

The equations (194) become

$$
b _ { k i } = b _ { i k } , \qquad ( \lambda _ { i } + \lambda _ { k } ) b _ { i k } = - c _ { i k } \qquad ( i \geq k ) .
$$

Choose

$$
C = \operatorname { d i a g } { ( d _ { 1 } , \ldots , d _ { n } ) } ,
$$

where every $d _ { s } > 0$ . Then

$$
C ^ { - 1 } = \operatorname { d i a g } \Big ( \frac { 1 } { d _ { 1 } } , \ldots , \frac { 1 } { d _ { n } } \Big ) , \qquad B = \operatorname { d i a g } \Big ( \frac { d _ { 1 } } { 2 \mu _ { 1 } } , \ldots , \frac { d _ { n } } { 2 \mu _ { n } } \Big ) ,
$$

$$
( B b ) ^ { \tau } = \frac { 1 } { 2 } \left( \frac { b _ { 1 } d _ { 1 } } { \mu _ { 1 } } , \dots , \frac { b _ { n } d _ { n } } { \mu _ { n } } \right) ,
$$

and (196) becomes

$$
r > \sum _ { h } \frac { 1 } { 4 d _ { h } } \left( \frac { b _ { h } d _ { h } } { \mu _ { h } } + c _ { h } \right) ^ { 2 } = \sum _ { h } \frac { 1 } { 4 } \left( \frac { b _ { h } e _ { h } } { \mu _ { h } } + \frac { c _ { h } } { e _ { h } } \right) ^ { 2 } ,
$$

$$
\begin{array} { r } { e _ { h } = \sqrt { d _ { h } } > 0 . } \end{array}
$$

The minimum of the sum as a function of $e _ { h }$ occurs when each parenthesis squared assumes its least value. At first, suppose that $b _ { h }$ and $c _ { h }$ are of the same sign, for example, $b _ { h } , c _ { h } > 0$ 、The hth parenthesis is the sum of two terms with constant product. Hence its extremum occurs when the two terms are equal or when $e _ { h } ^ { 2 } = \mu _ { h } c _ { h } / b _ { h }$ . For $b _ { h } c _ { h }$ $< 0$ the squared parenthesis can assume its smallest value,which is zero.Hence

$$
r > \sum _ { h } \frac { \varepsilon _ { h } b _ { h } c _ { h } } { \mu _ { h } } ,
$$

where $\varepsilon _ { h } = 1$ if $b _ { h } c _ { h } > 0$ ,and $\varepsilon _ { h } = 0$ otherwise. This gives the lower bound for the value of $r$

If some,but not all, of the characteristic roots of $\pmb { A }$ are zero, then we consider instead of (190)

$$
\frac { d u } { d t } = A u + \xi b , \frac { d z } { d t } = \xi d , \frac { d \xi } { d t } = f ( \sigma ) ,
$$

$$
\boldsymbol { \sigma } = c ^ { T } \boldsymbol { u } + 2 e ^ { T } \boldsymbol { z } - r \boldsymbol { \xi } ,
$$

where $y , d , e$ are $p$ -vectors.By introducing $x = d u / d t = A u + \xi b _ { \mathrm { ~ \normalfont ~ + ~ } }$ ， $y = d z / d t = \xi c$ we can show that the stability relations are unaltered if the inequality (197) holds,and the new system is

$$
\frac { d x } { d t } = A x + f ( \sigma ) b , \frac { d y } { d t } = f ( \sigma ) d , \frac { d \sigma } { d t } = c ^ { T } x + 2 e ^ { T } y - r f ( \sigma
$$

where $y , d , e$ are $p$ -vectors. We look for a Liapounov function

$$
V ( x , y , \sigma ) = y ^ { T } \cdot M y + \left\{ x ^ { T } \cdot B x + \int _ { 0 } ^ { \sigma } f ( \sigma ) \ d \sigma \right\} , \qquad M > 0 ,
$$

which is positive-definite for the whole space. Hence the stability character can be judged by Liapounov's theorems (Section 16.3).

Geiss and Abbate (1967) developed a procedure for computing the optimal quadratic estimate of the domain of attraction of an equilibrium solution of a quasi-linear differential equation, such as

$$
{ \frac { d x } { d t } } = A x + f ( x ) , \qquad f ( 0 ) = 0 ,
$$

where $\pmb { A }$ is stable.The quadratic Liapounov function $V ( x ) = x ^ { \tau } P ( x _ { \mathrm { . } }$ $P > 0$ ，hasas its derivative

$$
\dot { V } ( x ) = - x ^ { T } Q x + 2 x ^ { T } P f ( x ) , \qquad - Q = A ^ { T } P + P A .
$$

If $Q$ is chosen to be positive-definite, then $P$ is positive-definite,and accordingly $\dot { V }$ is negative in the domain

$$
D \colon \left( x \colon { \frac { \| f ( x ) \| } { \| x \| } } < { \frac { \lambda ^ { \operatorname* { m i n } } ( Q ) } { 2 \lambda ^ { \operatorname* { m a x } } ( P ) } } \right) ,
$$

where $\lambda ^ { \tt m i n } ( Q )$ and $\lambda ^ { \tt m a x } ( P )$ are the minimum eigenvalue of $Q$ and the maximum eigenvalue of $P$ ，respectively. The domain of attraction of the null solution $x ( t ) = 0$ of (198) is estimated,as in the foregoing, by

$$
\Omega _ { l } \colon ( x \mathbin { : } V ( x ) < l , \dot { V } ( x ) < 0 ) .
$$

The last estimate is obtained by defining the set $\boldsymbol { \varepsilon }$ as

$$
E \colon ( x ; { \dot { V } } ( x ) = 0 , x \neq 0 )
$$

and by changing $\iota$ to

$$
l = \operatorname* { m i n } _ { x \in E } V ( x ) .
$$

Then the optimal choice of $\boldsymbol { Q }$ ， which is denoted by $Q ^ { \circ }$ ， from the set of all positive-definite $n \times n$ matrices is defined by

$$
J ( Q ^ { 0 } ) = \operatorname* { m a x } _ { Q > 0 } J ( Q ) ,
$$

where

$$
J ( Q ) = \rho ^ { n / 2 } \biggl [ \prod _ { i = 1 } ^ { n } \lambda _ { i } ( P ) \biggr ] ^ { - 1 / 2 } = \Bigl ( \frac { l ^ { n } } { \mathrm { d e t } P } \Bigr ) ^ { 1 / 2 } .
$$

This definition of $Q ^ { \mathfrak { o } }$ was shown by Geiss and Abbate to yield the best estimate in terms of the enclosed volume of the domain of attraction under the constraint that $V ( x )$ should be a positive-definite quadratic form.

They proceeded in four steps.

The first step:It is known (Frazer,Duncan,and Collar,1938; Gantmacher,1959) that all real symmetric matrices are orthogonally similar to a diagonal matrix and that all positive-definite matrices are orthogonally similar to a diagonal matrix with positive diagonal element such as

$$
\Lambda = { \mathrm { d i a g } } \{ \lambda _ { 1 } , . ~ . ~ . ~ , \lambda _ { n } \} , \qquad \lambda _ { i } > 0 \qquad ( i = 1 , 2 , . ~ . ~ . , n ) ,
$$

and the parametrization (Sections 4.14-4.15) of all positive-definite matrices $\boldsymbol { Q }$ is reduced to the parametrization of the group of orthogonal matrices $s$ such as

$$
Q = S ^ { T } A S , \qquad S ^ { T } S = I .
$$

According to Murnaghan (1962) the parametrization of the group of $n \times n$ orthogonal matrices (Section 16.13) $s$ is accomplished by the factorization

$$
S = D _ { 1 } \bigg ( \prod _ { k = 1 } ^ { n - 1 } S _ { n - k } \bigg ) , \qquad D _ { 1 } = \mathrm { d i a g } \{ 1 , \dots , 1 , \pm 1 \} ,
$$

$$
S _ { k } = \left\{ \prod _ { l = k + 1 } ^ { n - 1 } S _ { k l } ( \theta _ { \mu } ) \right\} \{ S _ { k n } ( \phi _ { k } ) \} , \qquad S _ { k l } ( \theta _ { \mu } ) = U _ { k l } ( \theta _ { \mu } , 0 ) ,
$$

$$
\mu = { \frac { ( 2 n - k - 2 ) ( k - 1 ) } { 2 } } + n - l .
$$

If we restrict $s$ to be a rotation matrix, then the number of parameters is $n ( n + 1 ) / 2$

The second step is to solve the Liapounov equation (199),where $\pmb { P }$ and $Q$ are $n \times n$ symmetric matrices and $\pmb { A }$ is a stable $n \times n$ matrix:Assume that $( \lambda - \lambda _ { i } ) ^ { \alpha _ { i } } ( i = 1 , 2 , \ldots , r ; \alpha _ { 1 } + \cdot \cdot \cdot + \alpha _ { r } = n )$ are the elementary divisors of $\pmb { A }$ ； then there exist matrices $U , V$ such that $\pmb { A } = \pmb { U } ^ { - 1 } \tilde { \pmb { A } } _ { 1 } \pmb { U }$ ， $A ^ { \tau } = V ^ { - 1 } \tilde { A } _ { 1 } V$ ，where $\tilde { A } _ { 1 }$ is the Jordan normal form for $\pmb { A }$ (Frazer,Duncan,and Collar,1938；Gantmacher,1958, 1959, 1959a), i.e.,

$$
\begin{array} { c } { { \tilde { A } = \mathrm { d i a g } \{ \lambda _ { 1 } I _ { \alpha _ { 1 } } + N _ { \alpha _ { 1 } } , \dots , \lambda _ { r } I _ { \alpha _ { r } } + N _ { \alpha _ { r } } \} , } } \\ { { I _ { \alpha _ { \mu } } = ( \delta _ { i j } ) \qquad ( i , j = 1 , \dots , \alpha _ { \mu } ) , } } \\ { { N _ { \alpha _ { \mu } } = ( \delta _ { i + 1 , j } ) \qquad ( i , j = 1 , \dots , \alpha _ { \mu } ) , } } \end{array}
$$

and $\delta _ { i j }$ is the Kronecker delta. Then the Liapounov equation becomes

$$
\tilde { A } _ { 1 } Y + Y \tilde { A } _ { 1 } = - D ,
$$

where

$$
Y = V P U ^ { - 1 } , ~ D = V Q U ^ { - 1 } .
$$

The solution is

$$
Y _ { i j } = - \sum _ { n = 0 } ^ { \alpha _ { i } + \alpha _ { j } - 2 } ( \lambda _ { i } + \lambda _ { j } ) ^ { - ( n + 1 ) } ( - 1 ) ^ { n } \sum _ { \sigma + \tau = n } ^ { } \frac { n ! } { ( n - \tau ) ! \tau ! } N _ { \alpha _ { i } } ^ { \sigma } D _ { i j } N _ { \sigma } ^ { \tau }
$$

where $Y _ { i j } , D _ { i j }$ are the $( i , j )$ th elements of the matrices $\boldsymbol { Y } , \boldsymbol { D }$ ， respectively. We have finally

$$
P = V ^ { - 1 } Y U .
$$

Since $\pmb { A }$ is stable,all $\lambda _ { i }$ have negative real parts and $\lambda _ { i } + \lambda _ { j } \neq 0$ $( i , j = 1 , \ldots , r )$

The third step is to compute $ { l }$ and $Q ^ { \circ }$ by means of (200) and (201). We have two constraints that $x \in E$ ,i.e., $x$ is such that ${ \dot { V } } ( x ) = 0$ and $x \neq 0$ ，and that $\boldsymbol { Q }$ is positive-definite.We use Courant's device for penalty functions (Courant, 1943).A penalty function formulation of the present problem $l = \operatorname* { m i n } _ { x \neq 0 } V ( x )$ on ${ \dot { V } } ( x ) = 0$ is

$$
l = \operatorname * { m i n } _ { x } \left[ V ( x ) + k _ { 1 } ^ { 2 } \dot { V } ^ { 2 } ( x ) g ( x ) \right] ,
$$

or

$$
l = \operatorname* { m i n } _ { x } \left[ V ( x ) + \dot { k } _ { 1 } ^ { 2 } \dot { V } ^ { 2 } ( x ) + { k } _ { 2 } ^ { 2 } h ( x ) \right] ,
$$

where $\dot { V } ^ { 2 } ( x )$ is the penalty associated with not meeting the constraint

${ \dot { V } } ( x ) = 0$ and $g ( x )$ 0r $h ( x )$ is designed to penalize the choices of $x$ close to or equal to zero, e.g.,

$$
h ( x ) = { \frac { 1 + \| x \| ^ { 2 m } } { \| x \| ^ { 2 m } } } \qquad ( m = 1 , 2 , . . . ) .
$$

By parametrization, the equation (201) can be written

$$
J ( Q ^ { 0 } ) = \operatorname* { m a x } _ { \tiny { \begin{array} { c } { { \lambda _ { ( i  Q ) > 0 } } \\ { { - \pi \leq \phi _ { k } \subset \pi } } \\ { { - \pi / 2 \leq \theta _ { j } \leq \pi / 2 } } \end{array} } } } { J ( Q ) } = \operatorname* { m a x } _ { \tiny { \begin{array} { c } { { \lambda _ { ( i Q ) > 0 } } } \\ { { - \pi \leq \phi _ { k } \leq \pi } } \\ { { \pi / 2 \leq \theta _ { j } \leq \pi / 2 } } \end{array} } } \bigg ( \frac { l ^ { n } } { \operatorname* { d e t } P } \bigg ) ^ { 1 / 2 } .
$$

The _penalty function formulation of the corresponding minimum problem is

$$
J ^ { - 1 } ( Q ^ { 0 } ) = \operatorname * { m i n } _ { \lambda _ { j } , \phi _ { k ^ { \prime } } , \theta _ { j ^ { \prime } } } \left\{ \left( \frac { \operatorname * { d e t } P } { l ^ { n } } \right) ^ { 1 / 2 } + k _ { 3 } ^ { 2 } G ( \lambda _ { 1 } , \ldots , \lambda _ { n } ) \right\} ,
$$

where

$$
\begin{array} { r l } & { \phi _ { k } = - \pi + \phi _ { k } ^ { \prime } \bmod 2 \pi , \qquad - \infty < \phi _ { k } ^ { \prime } < \infty , } \\ & { \theta _ { j } = \frac { 1 } { 2 } ( - \pi + \theta _ { j } ^ { \prime } \bmod 2 \pi ) , \qquad - \infty < \theta _ { j } ^ { \prime } < \infty , } \\ & { G ( \lambda _ { 1 } , \ldots , \lambda _ { n } ) = \left\{ 1 \qquad \begin{array} { l l } { \lambda _ { i } \le \varepsilon \quad } & { ( i = 1 , \ldots , n ) , } \\ { 0 \quad } & { \lambda _ { i } > \varepsilon \quad } & { ( i = 1 , \ldots , n ) . } \end{array} \right. } \end{array}
$$

The constants $k _ { 1 } , k _ { 2 } , k _ { 3 }$ are chosen large enough to ensure meeting the respective constraints to the required accuracies,and $\varepsilon$ is chosen to define a forbidden neighborhood of zero.

The fourth step is to compute numerically the solutions of (200), (201)by means of (202),(203).To find the minimum over all $x$ of $\boldsymbol { \mathscr { f } } ( \boldsymbol { x } )$ ，where $x ^ { T } = ( x _ { 1 } , \ldots , x _ { n } )$ and where $\boldsymbol { \mathsf { f } } ( \boldsymbol { x } )$ is a scalar function,we choose an initial point $x _ { 0 }$ and an arbitrary $n \times n$ positive-definite symmetric matrix $H _ { \mathfrak { o } }$ ，and let

$$
{ \boldsymbol { s } } _ { k } = - H _ { k } { \boldsymbol { f } } _ { k } , \qquad { \boldsymbol { f } } _ { k } = { \Bigl ( } { \frac { \partial f } { \partial x _ { 1 } } } , \ldots , { \frac { \partial f } { \partial x _ { n } } } { \Bigr ) } ^ { T } ,
$$

and find $\alpha _ { k } > 0$ such that $f ( x _ { k } + \alpha _ { k } s _ { k } )$ is a minimum with respect to $\alpha _ { k }$ .Put

$$
x _ { k + 1 } = x _ { k } + \alpha _ { k } s _ { k }
$$

and compute $f ( x _ { k + 1 } )$ and $f ^ { \prime } ( x _ { k + 1 } )$ . We calculate $H _ { k + 1 }$ by

$$
H _ { k + 1 } = H _ { k } + A _ { k } + B _ { k } , \qquad y _ { k } = f _ { k + 1 } ^ { \prime } - f _ { k } ^ { \prime } ,
$$

$$
A _ { k } = ( s _ { k } ^ { T } y _ { k } ) ^ { - 1 } \alpha _ { k } s _ { k } s _ { k } ^ { T } , \qquad B _ { k } = - ( y _ { k } ^ { T } H _ { k } y _ { k } ) ^ { - 1 } H _ { k } y _ { k } y _ { k } ^ { T } H _ { k } .
$$

The process is repeated until

$$
\| x _ { k + 1 } - x _ { k } \| < \varepsilon , \qquad 0 < \varepsilon \ll 1
$$

(Pontryagin，Voltyanskii，Gamkrelidze， and Mischenko，1961;Hestenes，1966；Sworder, 1966； Leitmann, 1965,1967； Bellman,1967, 1971, 1973).

It is known that the Kepler motion is unstable in Liapounov's sense if time is used as the independent variable.Baumgarte (1972) succeeded in bringing the modified Kepler motion stable,by using the variable $s$ such that $d t = r d s$ as the independent variable and adding as control to the equations of motion a supplementary term:

$$
\frac { 1 } { 2 } \left( \frac { r ^ { \prime 2 } } { r ^ { 2 } } + \phi ^ { \prime 2 } \right) - \frac { K ^ { 2 } } { r } + h = 0 ,
$$

where $^ { h }$ is the energy constant and $\kappa$ the gravitational parameter such that

$$
\ddot { r } - r \dot { \phi } ^ { 2 } + \frac { K ^ { 2 } } { r ^ { 2 } } = 0 ,
$$

and a prime means a differentiation with respect to $\pmb { s }$ ，and a dot with respect to t.

Recently stability,called stochastic stability in contrast to deterministic stability,and control theory，of stochastic diferential equations, for example, for noise of electric circuit systems as a random process or for diffusion with random distribution of particle velocity，are discussed (Kushner，1967,1971；Astrom，1970；Curtain，1972; Wedig, 1972). Stochastic process and random process are synonyms and cover practically all the theory of probability from coin tossing to harmonic analysis (Feller,195O).In practice the term stochastic process is used mostly when a time parameter is introduced. Random walks (Section 27.4) and Markov chains (Sections 26.22-26.24) are examples of stochastic processes where changes can occur only at fixed times.

# 16.22STABILITY OF RIGID-BODY ROTATION

Stabilities of free rotation of a rigid body about its principal axes of least and greatest moments of inertia are well-known. Vinti (1969, 1969a,197O) derived the stabilities directly from the constancy of the kinetic energy and of the square of the angular momentum.

Let $A < B < C$ be the moments of inertia about the principal axes, $I _ { A } , I _ { B }$ and $I _ { c }$ be unit vectors attached to those axes and let $\omega _ { 1 } , \omega _ { 2 }$ and $\omega _ { 3 }$ be the respective components of the angular velocity about those axes. Consider the 3-dimensional $\pmb { \omega }$ -space. There is general Liapounov stability of rotational equilibrium at $\omega = \omega _ { 0 }$ if there exists a $\delta \leq \varepsilon$ such that, when $\omega _ { 0 }$ is changed by $\delta \omega _ { i }$ the resulting $\omega ( t )$ always satisfies $| \omega ( t ) - \omega _ { 0 } | < \varepsilon$ for $| \delta \omega _ { i } | < \delta .$ .When $\delta \omega _ { i }$ is restricted to the component perpendicular to the initial angular velocity $\omega _ { 0 }$ without speeding up or slowing down the main component, then the stability is called restricted by Vinti. When all three components of the initial angular velocity are changed then there is general stability.Thus,since $( \omega _ { 0 } , 0 , 0 )$ is an equilibrium point,any motion in the neighborhood is stable if there exists a $\delta \leq \varepsilon$ such that $( \omega _ { 1 } - \omega _ { 0 } ) ^ { 2 } + \omega _ { 2 } ^ { 2 } + \omega _ { 3 } ^ { 2 } < \varepsilon ^ { 2 }$ whenever $( \omega _ { 1 0 } - \omega _ { 0 } ) ^ { 2 }$ $+ \ \omega _ { 2 0 } ^ { 2 } + \omega _ { 3 0 } ^ { 2 } < \delta ^ { 2 }$ ，where $\omega _ { i 0 }$ $( i = 1 , 2 , 3 )$ denotes the initial value of $\omega _ { i }$ . From the constancy of the kinetic energy of rotation $2 T = A \omega _ { 1 } ^ { 2 }$ $+ \ B \omega _ { 2 } ^ { 2 } + \ C \omega _ { 3 } ^ { 2 }$ ， and the angular momentum $L = I _ { A } A \omega _ { 1 } + I _ { B } B \omega _ { 2 } +$ $I _ { c } C \omega _ { 3 }$ Vinti obtained

$$
\delta = \varepsilon F _ { 1 } ^ { - 1 } , \qquad F _ { 1 } ^ { 2 } = 1 + \frac { C } { A } \frac { C - B } { B - A } + \frac { C } { B } \frac { C - A } { B - A } ,
$$

as a sufficient condition for restricted stability of a free rotation about $I _ { c }$ , except for the case $A = B$ ； and similarly

$$
F _ { \mathrm { 3 } } ^ { \mathrm { 2 } } = 1 + { \frac { B } { C } } { \frac { B - A } { C - A } } + { \frac { B } { A } } { \frac { C - B } { C - A } } + { \frac { A } { C } } { \frac { B - A } { C - B } } + { \frac { A } { B } } { \frac { C - A } { C - B } }
$$

for restricted stability about $\boldsymbol { I } _ { A }$ . Instability of a free rotation about the intermediate axis $I _ { B }$ cannot be derived from the constancy of $L ^ { 2 }$ and $T$ . Neither can we derive a necessary condition.

For general stability Vinti concluded that, for arbitrarily small $\varepsilon$ ， the $\omega$ -point always remains inside the sphere of radius $\varepsilon < | \omega _ { \bar { \kappa } 0 } |$ with center $( \omega _ { 0 } , 0 , 0 )$ for $k = 1$ or $( 0 , 0 , \omega _ { 0 } )$ for $k = 3$ if it lies initially inside a like-centered sphere of radius $\delta = \varepsilon ( 1 + F _ { \varepsilon } ) ^ { - 1 }$ $( k = 1 , 3 )$ .

Vinti showed that this also leads to sufficient conditions for the rotational stability of almost-spherical bodies of various shapes,prolate or oblate.It may be pertinent in designing spheres to be used in currently planned experiments to test general relativity by observing the rate of precession of a rotating sphere in orbit about the earth (see, Section 8.25).

Roberson (1968),and Longman, and Roberson (1969) discussed the stability of gravity-gradient gyroscopic satellites by using Liapounov's direct method,and classified the equilibria of orbiting gyrostats into five separate categories.Let $\xi _ { 3 }$ be the unit vector in the direction of the geocentric vertical, $\boldsymbol { \xi } _ { 2 }$ normal to the plane of the circular orbit with the positive sense of the orbital angular velocity vector, and $\pmb { \xi } _ { 1 }$ forward along the tangent to the orbit. These are called the orbiting reference frame. The five categories are :

(i) The principal axes of the body aligned in any way with $\pm \xi _ { 1 } .$ ， $\pm \xi _ { 2 } .$ and $\pm \hat { \xi } _ { 3 }$ . The internal angular momentum must be along that axis aligned with $\pm \xi _ { 2 }$ (ii) A principal axis of the body aligned with $\pm \xi _ { 1 }$ , the other body axes not aligned with $\pm \xi _ { 2 } , \pm \xi _ { 3 }$ . The internal angular momentum must be in the plane perpendicular to $\hat { \xi } _ { 1 }$ (iii) A principal axis of the body aligned with $\pm \hat { \xi } _ { 3 }$ ,the other body axes not aligned with $\pm \xi _ { 1 } , \pm \xi _ { 2 }$ . The internal angular momentum must be in the plane perpendicular to $\xi _ { 3 }$ (iv) The axis of intermediate moment of inertia in the orbital plane and none of the principal axes aligned with an axis of the $\xi$ -frame. (v) None of the principal axes in any of the planes: the $\xi _ { 1 } - \xi _ { 2 }$ plane, the $\xi _ { 1 } - \xi _ { 3 }$ plane, or the $\xi _ { 2 } - \xi _ { 3 }$ plane.

These define a complete set of all possible equilibria. There are no cases (iv) and (v) for symmetric satellites.

Longman (1971） discussed the gravity-gradient stabilization of gyrostat satellites with the internal angular momentum vector (or rotor axis） aligned with the $\pm \hat { \xi } _ { 2 }$ , or in the principal planes,as in the case (i),(ii),and (ii). For those configurations for which the rotor axis is aligned with a principal axis there exists a continuum of equilibrium orientations at one and only one rotor speed. The stability was discussed by Anchev (1966).When the rotor axis is moved away from a principal axis,as in the cases (iv) and (v), in such a way that it is contained in a plane formed by two principal axes,it is shown that the continuum disappears and we have a new set of eight equilibrium orientations.Longman studied the stability of these orientations using the Hamiltonian as a Liapounov testing function. For properly chosen inertia ratios of the satellite some of these orientations are stable,and might be used in future gravity-gradient stabilized satellites.

Concerning the attitude behavior of artificial earth satellites, Breakwell and Pringle (1965） studied the resonant gravity-gradient perturbations of the attitude librations of a nonspinning satelite in a nearly circular orbit, Kane and Shippy (1963) discussed the attitude stability of a triaxial satellite in a circular orbit spinning about a principal axis normal to the orbital plane，Meirovitch and Wallace (1967) treated the normalized difference of the transverse inertias as a small quantity and carried out the formal asymptotic expansions, Fitzpatrick and Crenshaw (1968) discussed the gravity-gradient effects on the general rapid rotational motion of a uniaxial satellite, Torzhevskii (1968） considered the behavior near resonance for a satellite differing slightly from an axially symmetric satellite，and Holland and Sperling (1969; Section 8.6) averaged the gravity-gradient torque equation to obtain the long-term changes in the rotational angular momentum vector for any tumbling satellite.

Hitzl and Breakwell (1971) discussed the resonant and nonresonant gravity-gradient perturbations of the attitude motion of a tumbling triaxial satellite.The center of mass of the satellite is considered to be in an elliptic orbit about a spherical planet and to be tumbling at a frequency much greater than the orbital rate.A canonical form for the solution of the torque-free motion of a rigid body was taken as the nonperturbed motion of the satelite. Representing the gravitygradient perturbing torque in terms of a perturbing Hamiltonian， the long-term changes in the rotational motion were derived. Far from resonance they showed that there is no long-period change in the magnitude of the rotational angular momentum and rotational energy and that the rotational angular momentum vector precesses around the orbital angular momentum vector. At resonance, however,a loworder commensurability exists between the polhode frequency and the tumbling frequency.Near resonance there may be small long-period fluctuations in the rotational energy and angular momentum magni-tude,and moreover the precessional angular momentum vector about the orbital angular momentum vector contains substantial long-period contributions superimposed on the nonresonant precession rate. By averaging certain long-period elliptic functions the mean value near resonance for the precession of the rotational angular momentum vector is obtained in terms of the initial conditions.

Hitzl (1972) again discussed the resonant attitude instabilities for a symmetric satellite in a circular orbit. Resonance in circular orbit occurs if there is a low-order commensurability between the coupled rol-yaw attitude frequencies. The only perturbative effect of an artificial satellite is that due to the so-called gravity-gradient torque.He assumed that the symmetry axis of the satellite is almost aligned with the orbit normal.His approach was to expand the Hamiltonian describing the perturbed attitude motion in a power series and then to remove the rapid attitude oscillations by averaging. Close to a resonant state there is a near commensurability between the frequencies of the two normal modes for the coupled roll-yaw motion，which is called internal resonance.Then it is seen that the long-term perturbations can become large near a resonance.Hitzl also discussed the effect of elliptic orbital motion on the long-term behavior of the satellite symmetry axis.Then resonance occurs when there is a near commensurability between the attitude frequencies and the mean orbital rate. This is called external resonance.He took the moment of inertia ratio $r$ and the angular momentum $\iota$ along the nonsymmetrical axis as two parameters. The linearized stability in the Thomson plane of $( l , r )$ is shown in two regions : the Lagrange region, where the Hamiltonian is positive-definite,and the Delp region,where the Hamiltonian is indefinite but corresponds to a maximum potential energy.Denote the two frequencies of this linearized motion by $\omega _ { 1 }$ and $\omega _ { 2 }$ . Hitzl considered the resonant case $\omega _ { 2 } = 3 \omega _ { 1 }$ . He confirmed the resonance-induced instabilities by direct numerical integration.He showed that the nonlinear oscillations near resonance are substantially different in the Lagrange to that in the Delp region of the parameter space,and that near the region $\omega _ { 2 } = 3 \omega _ { 1 }$ for the Lagrange region there are long-period oscillations caused by an interchange of energy between the two normal modes but in the Delp region there is a simultaneous growth or decay of both modal energies.Large resonance growth of both modes is shown to be possible in the Delp region along the two sections of the internal resonance line where $1 . 0 5 \leq r \leq 1 . 0 8$ . Thus Liapounov stability does not exist in the Delp region. The two unstable sections have the limits $- 1 . 7 4 3 < l < - 1 . 5 6 7$ and $0 . 3 8 5 < l < 0 . 9 4 9$

Kane and Marsh (1971) analyzed the problem of attitude motion of the smallest body of axial symmetry for the restricted three-body problem,in which the symmetry axis is normal to the orbital plane, and examined the stability of attitude motion of the small body near the equilibrium points.They showed that the stability is essentially the same when the body moves on a circular orbit about a fixed particle,which case was studied by Thomson (1962),but when the body occupies one of the straight-line equilibrium points the difference between the three-body problem and the two-body problem can be pronounced, particularly when the body lies at $L _ { 2 }$

Hughes and Fung (1971) then discussed the Liapounov stability of a spinning satellite which has a central rigid body and long flexible tubular appendages called booms nominally in the spin plane.It is known, from the major-axis theorem in the presence of damping, that of the three pure-spin solutions of the equations of motion only spin around the major inertia axis is stable.Hughes and Fung showed that the major-axis condition is a necessary but not a sufficient condition for stability. The stability is studied through the diferential equations for first-order perturbation about a pure spin around the axis perpendicular to the plane of the booms.They used a modified Hamiltonian as the Liapounov function,and showed that if the central rigid body is itself in a major-axis spin then the addition of booms does not destabilize it. They derived necessary conditions for stability and demonstrated that flexible booms can be used to stabilize an unstable central body.

Zipse (1971） showed that the gross attitude deviation of spinstabilized axially symmetric probes which move along elliptic solar orbits,such as the solar probe Helios, is small.

Kinoshita (1972) studied the stationary motions of a system of two rigid bodies,one spherical and the other triaxial,and the stability. The stationary solution in which the principal axis with the maximum inertial momentum is perpendicular to the orbital plane and the axis with the minimum inertial momentum points towards the sphere is shown to be secularly stable, i.e.,the total mechanical potential is in the absolute minimum. The stationary motion in which the principal axis with the medium inertial momentum is perpendicular to the orbital plane is unstable.

Zhuravlev (1972) discussed the stability of the equilibrium points in the problem of motion of a mass point in the neighborhood of a rotating triaxial ellipsoid in the strict sense.The equations of motion admit particular solutions in a rotating coordinate system.Four relative equilibrium points correspond to these solutions. The equilibrium points are on the plane of an equatorial section on the continuation of its major and minor axes.The points on the minor axis are stable in the first approximation in Liapounov's sense and those on the major axis'are unstable.There is a critical case in the stability theory when a first approximation is not suffcient to solve a stability problem. It has been shown that the stable points in the first approximation are unstable if the frequencies $\lambda _ { 1 }$ and $\lambda _ { 2 }$ of a linear system are rational and satisfy a resonance condition $\lambda _ { 1 } = 2 \lambda _ { 2 }$ or $\lambda _ { 1 } = 3 \lambda _ { 2 }$ . Zhuravlev considered the equilibrium points of systems whose base frequencies satisfy other resonance conditions or do not at all satisfy resonance conditions and showed that the equilibrium points of the ellipsoids whose form and dynamical characteristics are close to those of the planets are stable.

Kinoshita (1972a） studied the first-order perturbation from the Keplerian motion by the Lie transform method (Sections 9.29,10.44). He showed that the precessional motion of the plane normal to the angular momentum vector of the triaxial rigid body is synchronized with the motion of the node of the orbital plane,and that when the triaxial body is oblate the motion is retrograde.The sidereal mean motion is larger than that of the nonperturbed Keplerian motion and the mean motion of the rotation along the figure axis is smaller than that of the nonperturbed rotational motion.

Nikolayev (1972） studied the stability conditions of the libration points of the triaxial ellipsoid under constant perturbations by calculating in asymptotic series form the characteristic exponents of the system of six linear first-order differential equations with nearly periodic coefficients.

Sperling (1972） discussed the following type of rotations. The satellite spins about an axis fixed in the orbit frame ;the satellite need not be symmetric,the spin not uniform，and the spin axis not a principal axis of inertia.An orbit frame has its origin at the center of mass of the satellite and rotates with the satellite's orbital angular speed such that one axis always points towards the central body and another axis is orthogonal to the space-fixed orbit plane. Lagrange's 24 solutions are in the case with the satellite resting in the orbit frame and with the principal axes of inertia lined up with the axes of the orbit frame.Another type of motion with spin about a principal axis orthogonal to the orbit plane is known. Pringle （1964） discovered cases of a satelite spinning uniformly about a principal axis of inertia such that the spin axis rests in the orbit frame,and the satellite is symmetric with respect to the spin axis. Sperling's result for the above general case is that the cases of Lagrange and Pringle and the spin about a principal axis of inertia orthogonal to the orbit plane are essentially the only ones possible. The only further motions Sperling found are cases of uniform spin of a two-dimensional, but not necessarily symmetric,satellite about certain axes that are orthogonal to the plane containing the body and to the orbit of the satellite about the central body.

Pringle (1973) studied the coupled vibration-rotation motion of a satellite using a canonical perturbation theory based on Lie transform method (Sections 9.29 and 10.44). Short-period oscillating terms are removed from the Hamiltonian. The transformed damping forces exhibit coupling directly to the rotational variables which determine the body wobble motion attenuation. Resonance effects and instabilities were seen to limit the effectiveness of such damping. Pringle used canonical rotation parameters which provide a unified treatment of all rotation-vibration problems.Attitude singularities are easily handled with simple canonical changes of variables. Jump phenomena are exhibited in the case of resonance between vibration and rotation.

Recently Zhuravlev (1973） studied the stability of the libration points of a rotating triaxial ellipsoid in a degenerate case, i.e.，when the Gaussian of the Hamiltonian is zero,using Birkhoff's transformation (Section 21.1),on the basis of the Kolmogorov-Arnold stability criterion (Section 21.17).

# REFERENCES

Abraham, R. 1967Foundations of Mechanics, Benjamin, New York.   
Adamov, N. 1935Recueil Math., 42, 651.   
Ahlfors, L. V., and Sario, L. 1960Riemann Surfaces,Princeton University Press,Princeton, N.J.   
Almkvist, G. 1966 Pacific J. Math.,16,383.   
Anchev, A. A. 1966 Kosmicheskie Issledovania, 4,192.   
Andronov, A., and Witt, A. 1933 Phys. Z. Sov. Union,4,606.   
Antosiewicz, H. A. 1958Contribution to the Theory of Nonlinear Oscillations, IV,S. Lefschetz,ed.,141,Princeton University Press,Princeton, N.J.   
Arnold, V. I. 1965 Dokl. Akad. Nauk SSSR,162, no. 5. Translated in Soviet Math. (Dokl.), 6, 773. 1965a Compt. Rend., 261, 17.   
Artemiev, N. A. 1938 Compositio Math.,6,78.   
Astrom, K. J. 1970 Introduction to Stochastic Control Theory，Academic Press, New York.   
Atkinson, F. V. 1958 Annals of Math., 68, 690.   
Banach, S. 1932 Théorie des Opérations Linéaires,Z Subwencji Funduszu Kultury Narodowej, Warszawa.   
Baumgarte, J. 1972 Celestial Mech.,5,490.   
Bellman, R. 1953 Stability Theoryof Differential Equations,McGraw Hill,New York. 1971 Introduction to the Mathematical Theory of Control Processes,Academic Press,New York. 1973 Methods of Nonlinear Analysis,I,Academic Press,New York.   
Duaua, IN. r., auu Szego, U. r. 1970Stability Theory of Dynamical Systems, Springer, Berlin.   
Bieberbach,L. 1953" Theorie der gewohnlichen Differentialgleichungen, Springer, Berlin.   
Birkhoff, G. D. 1927Dynamical Systems, Am. Math. Soc., New York.   
Bodewig,E. 1956Matrix Calculus, North-Holland, Amsterdam.   
Bohl, P. 1893 Dissertation,Tartu,published as Uber die Darstellung der Funktionen einer Variabeln durch trigonometrische Reihen mit mehreren einer Variabeln proportionalen Argumenten, C. Mattiesen,Tartu. 1904 J.reine angew. Math.,127,179. 1906 Ibid.,131,268. 1907 Z.Math. Physik., 54,381. 1910 Bull. Soc. Math. France,38,5. 1917 Acta Math., 40,321.   
Bourbaki, N. 1953 Espaces Vectoriels Topologiques,I, Hermann, Paris. 1955 Ibid., II.   
Brayton, R.K., and Miranker, W.L. 1964 Arch. Ratl. Mech. Anal., 17,358.   
Brayton, R.K.,and Moser, J. 1964 Quart. J. Appl. Math., 22, 9,81.   
Breakwell, J.V., and Pringle, R. 1965Proc.Internatl. Astronaut. Congress,Athens, 305.   
Cameron, R. H. 1938 Acta Math., 69,21.   
Cesari, L. 1959 Asymptotic Behavior and Stability Problems in Ordinary Differential Equations,Springer,Berlin.   
Cetaev, N. G. 1934 Dokl.Akad.Nauk SSSR,2,529. 1961 The Stability of Motion,Pergamon, Oxford.   
Cherry, T. M. 1928 Proc. London Math. Soc., 27,151.   
Chevalley, C. 1946 Theory of Lie Groups,I, Princeton University Press, Princeton, N. J.   
Coppel, W. A. 1965 Stability and Asymptotic Behavior of Differential Equations, Heath, Boston. 1967 Ann. Mat. pura appl., 76, 27.   
Cotton, E. 1911 Ann. Ecole Norm. Sup., ser. 3,28, 473. 1972Stability of Stochastic Dynamical Systems, Springer, Berlin.   
Dalecki, Iu. L., and Krein, M. G. 1972 Stability of Solutions of Differential Equations in Banach Space, Transl. in Am. Math. Soc., New York.   
Dearman, C. C., and Le May, A. R. 1966 Mathematiche Methoden der Himmelsmechanik und Astronautik，Berichte einer Tagung des Mathematischen Forschungs-Instituts Oberwolfach,E.Stiefel,ed.，Bibliographisches Institut, Mannheim.   
Delsarte, J. 1932 Les Groupes des Transformations Linéaires dans l'Espace de Hilbert,Gauthier-Villars,Paris.   
Deysach, L. G., and Sell, G. R. 1965 Michigan Math. J., 12, 87.   
Diliberto, S. P. 1950 Contributions to the Theory of Nonlinear Oscillations, S. Lefschetz, ed.,1,Princeton University Press,Princeton, N.J.   
Dunford, N.,and Schwartz, J.T. 1958Linear Operators,Part I,General Theory,Interscience,New York.   
Erugin, N. P. 1966 Linear Systems of Ordinary Differential Equations with Periodic and Quasi-Periodic Coefficients,Translated from Russian，Academic Press,New York.   
Feller, W. 1950An Introduction to Probability Theory and its Appl:cations, I, Wiley,New York.   
Fink,A. M., and Seifert, G. 1969J. Differential Eqs., 5,307.   
Fitzpatrick, P. M.,and Crenshaw, J. W. 1968 J. Am. Inst. Aeronaut. Astronaut., 6, 2140.   
Fomin, S. 1950 Ukrain. Mat. Zhur.,2, 25. Translated in Am. Math. Soc. Transl.,ser. 2, no. 61, 1.   
Fomin, V. N. 1965 Dokl.Akad.Nauk SSSR,163，no.4，830． Translated in Soviet Math. (Dokl.),6, 1037.   
Frazer,R. A., Duncan,W.J., and Collar,A. R. 1938Elementary Matrices， Cambridge University Press, London.   
Gantmacher, F.R. 1958Matrizenrechnung,I,Akademie-Verlag, Berlin. 1959Ibid., II. 1959a The Theory of Matrices,I,Chelsea,New York.   
Gantmacher, F.R.,and Krein,M.G. 1960 Oszillationsmatrizen, Oszillationskerne und kleine Schwingungen mechanischer Systeme,Akademie-Verlag, Berlin. 190/ Grurnnun Res. Depi. Rep. RE-zo∠, Aeiu-Asuvuyuaumus Lab.,Marshall Space Flight Center,Huntsville,Alabama.   
Gelfand, I. M.,and Lidskii, V. B. 1955Usp.Mat.Nauk SSSR,10,3. Translated in Am.Math. Soc. Transl., ser.1,5,242,1962.   
Ghizzeti, A. 1963 Mem. Accad. Naz. Lincei, ser. 8,7, 17.   
Gottschalk,W.,and Hedlund, G. 1955Topological Dynamics, Am. Math. Soc., New York.   
Haacke,W. 1952 Math. Z., 56, 65; 57, 34.   
Hadamard, J. 1897 J. Math. pures appl., ser. 5, 3, 331. 1898Ibid., 4, 27.   
Hagihara, Y. 1970 Theories of Equilibrium Figures of a Rotating Homogeneous Fluid Mass, National Aeronautics and Space Administration, Washington, D.C.   
Hahn, W. 1959 Theorie und Anwendung der direkten Methode von Ljapounov,Springer,Berlin.   
Hale, J. K. 1963 Oscillations in Nonlinear Systems,McGraw Hill, New York. 1963a Contr.Dif.Eqs.,1,401. 1964 Arch. Ratl. Mech. Anal., 15,289. 1965J.Differential Eqs., 1,452.   
Halkin, H. 1964 Arch. Ratl. Mech. Anal., 17, 272. 1964a J. Math. Anal. Appl., 7, 272. 1964b J. Analyse Math., 12, 1. 1965J. Math. Anal.Appl.,10,325.   
Harasahal, V. H. 1961 Dokl. Akad. Nauk SSSR, 139,313. Translated in Soviet Math. (Dokl.), 2,940. 1962 Ibid.,146, 1290. Translated in Soviet Math (Dokl.),3,1506.   
Hestenes, M.R. 1966 Calculus of Variations and Optimal Control Theory， Wiley New York.   
Hitzl, D. L. 1972 Celestial Mech., 5, 433.   
Hitzl,D. L.,and Breakwell, J.V. 1971 Celestial Mech., 3, 346.   
Holland, R.L., and Sperling, H.J. 1969Astron.J.,74,490.   
Horn, J. 1906 J. reine angew. Math.,131, 224.   
Hughes, P. C., and Fung, J. C. 1971 Celestial Mech., 4,295.

Cambridge, Mass. Hurwitz, A. 1895 Math. Annalen, 46, 273. Ince, E. L. 1927Ordinary Differential Equations, Longmans, London. Infante, E. F. 1967 Differential Equations and Dynamical Systems, J.K.Hale and J.P.LaSale, eds., 309, Academic Press, New York. Ingwerson, D. R. 1961IRE Trans.on Automatic Control, AC-6, no. 2, 199. Jacobson, N. 1935 Proc. Natl. Acad. Sci. US, 21, 667. 1937Annals of Math., 38,484. Kane,T.R., and Marsh, E.L. 1971 Celestial Mech., 4, 78. Kane, T. R., and Shippy, D. J. 1963J. Astronaut. Sci., 10, 114. Kantorovich, L. V., and Akimov, G. P. 1964 Functional Analysis in Normed Space,Pergamon, London. Karstens, H. 1901 Ueber gewisse asymptotische Losungen der Differentialgleichungen der analytischen Mechanik,Dissertation, Berlin. Kato, J. 1971 Japan-United States Seminar on Ordinary Differential and Functional Equations，M. Urabe,ed., 54, Springer-Verlag, Berlin. Kato, J.,and Yoshizawa, T. 1970Funkcialaj Ekvacioj,12,233. Kato, T. 1956 Comm. Pure Appl. Math., 9,479. Kelley, J.L., Namioka, I.,et al. 1963 Linear Topological Spaces, van Nostrand, Princeton, N. J. Kinoshita, H. 1972 Pub. Astron. Soc. Japan, 24, 409. 1972a Ibid.,24,423. Klein F. 1894Uber lineare Differentialgleichungen zweiter Ordnung (mimeographed). Kneser, A. 1895 J. reine angew. Math., 115, 308. 1897Ibid.,118, 186. Kolesov, Iu. S. 1969 Dokl.Akad.Nauk SSSR,188,1234. Translated in Soviet Math. (Dokl.),10, 1290. Kothe, G. 1960Topologische Lineare Räume,Springer-Verlag, Berlin. Krasnoselskii, M.A.

Krasovskii, N. N. 1963Stability of Motion，Application of Liapounov's Second Method to Differential Systems and Equations with Delay, Stanford University Press,Stanford,Calif.   
Krein, M. G. 1950 Dokl. Akad. Nauk SSSR, 73,445. 1972 Linear Differential Equations in Banach Space, Am. Math. Soc., New York.   
Kudaev, M. B. 1962 Dokl. Akad.Nauk SSSR,147,1285.Translated in Soviet Math. (Dokl.), 3,1802.   
Kushner, H. J. 1967 Stochastic Stability and Control,Academic Press,New York. 1971 Introduction to Stochastic. Control Theory，Holt,Rinehart and Winston,New York.   
Langer, R. E. 1949 Trans. Am. Math. Soc., 67,461.   
La Salle, J. P. 1957 Annals of Math., 65, 571. 1967 Differential Equations and Dynamical Systems, J.K.Hale and J.P. La Sall, eds., 277. Academic Press, New York. 1968 J. Differential Eqs., 4, 57.   
La Salle,J., and Lefschetz, S. 1961 Stability by Liapounov's Direct Method with Applications, Academic Press, New York.   
Lefschetz, S. 1949Lectures on Differential Equations,Princeton University Press,Princeton, N.J. 1958 Bol. Soc.Mat. Mex.,3,25.   
Leitman, G., ed. 1965 Stability of Nonlinear Control Systems,Academic Press, New York. 1967 Topics in Optimization,Academic Press, New York.   
Lettenmeyer, F. 1929 Sitzber. bayer.Akad. Wiss.,Minchen,Math.-Naturw.Abt., 1929,201.   
Liapounov, A. 1907 Mém. Acad. Sci. Saint-Pétersbourg, 13, no. 2,1. 1949 Probleme Géneral de la Stabilite du Mouvement,Princeton University Press,Princeton, N.J. Previously printed in Comm. Soc.Math. Kharkow，1892. Reprinted in Ann. Fac. Sci. Toulouse,ser.2,9, 203,1907；and in Sobranie Sochineni, II, 7,Akad. Nauk SSSR, 1956. 1966 Stability of Motion,with contribution by V.A.Pliss and introduction by V.P. Basov,Academic Press,New York.   
Likins, P. W., and Roberson, R. E. 1971 Celestial Mech., 3,491.

1955Annals of Math., 69,1. 1960 Math. Z., 73, 45. Lillo, J. C., and Seifert, G. 1956Z. angew. Math. Phys., 7, 238. Liu, R. W., and Leake, R. J. 1967 Differential Equations and Dynamical Systems, J. K. Hale and J.P.La Salle,eds., 333, Academic Press, New York. Loewy， A. 1918 Math. Annalen, 78,1. Longman, R. W. 1971 Celestial Mech., 3, 169. Longman, R. W.， and Roberson, R. E. 1969J. Astronaut. Sci.,16,49. Malkin, I. G. 1938 Mat. Sbornik SSSR,3(45).47. Translated in Am. Math. Soc. Transl.,no. 41 (1951) and ser.1,5,175 (1962). 1942 Prikl.Mat.Mekh., 6, 411. Translated in Am. Math. Soc. Transl.,no.38 (1951) and ser. 1,5, 242 (1962). 1944 Ibid.,8,241. Translated in Am. Math.Soc. Transl.,no.8 (1950） and ser.1,5,291(1962). 1952 Theory of Stability of Motion, Transl.，AEC-tr-3352, U.S. Department of Commerce, Washington, D.C. Markus, L. 1955 Math. Z., 62, 310. Massera, J. L. 1949 Annals of Math., 50, 705. Massera, J. L., and Schaffer, J.J. 1958 Annals of Math., 67,517. 1959 Ibid.,69, 88. 1959a Ibid.,69,535. 1966 Linear Differential Equations and Function Spaces,Academic Press, New York. Meirovitch,L., and Wallace, F.B. 1967 J. Astronaut. Sci.,14, 123. Miller, R. K. 1965 J. Differential Eqs.,1, 337. 1965a Ibid.,3,293. Moisseiev, N. 1936 Math. Annalen,113,452. 1936a Dokl. Akad.Nauk SSSR,10, 165. 1936b Ibid.,10,215. 1937 Math.Z.,42, 513. 1937a Dokl. Akad. Nauk SSSR,16,291. Moser, J. 1958 Comm. Pure Appl. Math., 11, 257. Moustakhichev, K.. 1968 Byull. Inst. Teor. Astron. (Akad. Nauk SSSR),11,453. Murnaghan, F. D.

Murray, F.H. 1925 Am. J. Math.,47,25. 1926 Trans. Am. Math. Soc., 28, 74, 109.   
Nagai, R. 1972 Rep. Tokyo Astron. Obs.,16,1 (Japanese).   
Nakajima, F. 1971 Japan-United States Seminar on Ordinary Differential and Functional Equations,M. Urabe,ed., 293,Springer-Verlag, Berlin.   
Nemytskii, V. V. 1949 Usp.Mat.Nauk SSSR,4,no.6, (34),91. Translated in Am. Math. Soc. Transl., no.103 (1954) and ser.1,5,414 (1962).   
Nemytski, V. V. and Stepanov, V. V. 1960Qualitative Theory of Differential Equations,Princeton University Press, Princeton, N.J.   
Newell, H. E. 1942 Duke Math. J.,9, 249; 10, 705.   
Nikolayev, S. I. 1972Byull. Inst. Teor. Astron.(Akad. Nauk SSSR),13,215.   
Olszewski, J. 1971 Celestial Mech., 4, 3.   
Perron, O. 1913 J. reine angew. Math., 142, 254; 143, 25. 1928 Math. Z., 29, 129. 1929 J. reine angew. Math., 161,41. 1930 Math. Z., 31, 748. 1930a Ibid.,32,465. 1930b Ibid.,32,703. 1937 Math. Annalen,113,292.   
Picard, E. 1908 Traité d'Analyse,III,2nd ed.,Gauthier-Villars,Paris.   
Pliss, V. A. 1964 Dokl.Akad.Nauk SSSR，154，1044. Translated in Soviet Math. (Dokl.), 5, 247. 1966 Nonlocal Problems of the Theory of Oscillations,Academic Press, New York.   
Poincaré,H. 1879 Sur les Propriérés des Fonctions définies par les Equations aux Différences Partielles，These,Paris. Reprinted in Oeuvres,I, XLIX, Gauthier-Villars,Paris,1928. 1885 J. Math. pures appl., ser.4,1, 167. Reprinted in Oeuvres,I, 90, Gauthier-Villars,Paris,1928. 1886 Ibid.,ser.4, 2,151. Reprinted in Oeuvres,I,167. 1892 Les Méthodes Nouvelles de la Mécanique Céleste, I,Gauthier-Villars, Paris. 1899 Ibid., III. 1912 Rendiconti Cir. Mat. Palermo,33, 375. Reprinted in Oeuvres,   
Pontryagin, L. 1939 Topological Groups， Princeton University Press,Princeton, N.J.   
Pontryagin, L. C., Voltyanski, V. G., Gamkrelidze,R. V., and Mischenko, E.F. 1961 Matematicheskaia Teoria Optimalinikh Prochessov，Gosudarstvennoe Izd. Fisiko-Matematicheskoi Literaturi, Moskwa.   
Pringle, R. 1964 AIAAJ,2,908. 1973 Celestial Mech., 7, 495.   
Puri, N. N., and Ku, Y. H. 1963J. Franklin Inst., 276,349.   
Puri, N. N., and Weygandt, C. N. 1963 1bid.,276, 365.   
Razumikhin, B. S. 1956Prikl.Mat.Mekh.SSSR,20,500.   
Reid, W. T. 1951 Duke Math. J.,18,41.   
Riesz, F., and Nagy, B. Sz. 1955Functional Analysis, Ungar, New York.   
Roberson, R. E. 1968 J. Astronaut. Sci., 15,242.   
Roseau, M. 1966Vibrations nonlinéaires et Théorie de la Stabilité,Springer, Berlin.   
Routh, E. J. 1877 A Treatise on the Stability of a given State of Motion, Macmillan, London. 1884 A Treatise on the Dynamics of a System of Rigid Bodies,4th ed.,Macmillan,London. 1905 Ibid.,I, 6th ed.,Macmillan, London.   
Schaefer, H. H. 1971Topological Vector Spaces, Springer, Berlin.   
Schauder, I. 1930 Studia Math., 2,183.   
Schmeidler, W. 1965 Linear Operators in Hilbert Space，Academic Press,New York.   
Schultz, D. G., and Gibson, J.E. 1962 Trans. AlEE on Automatic Control,81, part 2,203.   
Segal, M. 1964 Comm. Pure Appl. Math., 17,401.   
Seifert, G. 1955 Z.angew.Math. Phys.,6,239. 1958 Annals of Math., 67, 83. 1959 Ibid., 69, 75. 1960 Proc. Am. Math. Soc., 11, 429. 1966 J. Differential Eqs., 2, 305.

1968 J. Math. Anal. Appl.,21,136.

\~0 Berlin.   
Sell, G. R. 1967 Trans. Am. Math. Soc.,127, 246,263. 1971 Topological Dynamics and Ordinary Differential Equations, Van Nostrand,odon.   
Shtokalo, I. Z. 1961 Linear Differential Equations with Variable Coefficients (Criteria of Stability and Instability of their Solutions),Gordon Breach,New York.   
Smale, S. 1967 Bull.Am. Math. Soc., 73,747.   
Sobolev, S. L. 1963 Applications of Functional Analysis in Mathematical Physics, Am.Math.Soc., translated from Russian.   
Soulé, J. L. 1967Opérations Linéaires dans l'Espace D'Hilbert,Gordon Breach, New York.   
Sperling, H. J. 1972 Celestial Mech., 6, 278.   
Stone, M. H. 1932 Linear Transformations in Hilbert Space, Am. Math. Soc., New York.   
Sugiyama, S. 1971 Japan-United States Seminar on Ordinary Differential and Functional Equations，M. Urabe,ed.,1, Springer-Verlag, Berlin.   
Sworder, D. 1966 Optimal Adaptive Control Systems， Academic Press, New York.   
Thomson, W. T. 1962 J. Astronaut. Sci., 9, 31.   
Torzhevskii, A.P. 1968 Kosmicheskie Issledovania, 6, 47.   
Ura, T., and Kimura, I. 1964Proc. Japan Acad.,40, 703. Vinti, J. P. 1969 Celestial Mech., 1, 59. 1969a Measurement Systems Laboratory,RE-58,MIT Press, Cambridge,Mass. 1970 Periodic Orbits,Stability and Resonance,259,G.E. O.Giacaglia,ed.,Reidel,Dordrecht,Holland. Volterra, V. 1910 Lecons sur les Equations Intégrales et les Equations Intégro-Difféerentielles,Gauthier-Villars,Paris. Volterra, V.,and Péres,J. 1936Théorie Générale des Fonctionnelles,Gauthier-Villars, Paris.   
Von Neumann, J. 1950 Functional Operators, II, Princeton University Press, Princeton, N.J.   
Wedig, W. 1972 Proc.IUTAM Symposium on Stability of Stochastic Dynamical Systems, Springer,Berlin.   
Weyl, H. 1939 The Classical Groups, Princeton University Press, Princeton, N.J.   
Wiman, A. 1936 Acta Math., 66, 121.   
Wintner, A. 1947The Analytical Foundations of Celestial Mechanics, Princeton University Press, Princeton, N.J.   
Yabubovic, V. A. 1951 Dokl. Akad. Nauk SSSR,78, 221.   
Yorke, J. A. 1970 J.Differential Eqs.,7, 189.   
Yoshizawa, T. 1955 Mem. Coll. Sci. Univ. Kyoto, ser. A, 29,27. 1959 Funkcialaj Ekvacioj,2, 95. 1960 Mem. Coll. Sci. Univ. Kyoto, ser. A, 33,301. 1960a Arch. Ratl. Mech. Anal., 6,409. 1963 Contr. Diff. Eqs.,1,37i;2, 407. 1964 Arch. Ratl. Mech. Anal., 17, 148. 1966 Stability Theory by Liapounov's Second Method, Math.Soc. Japan, Tokyo. 1968 J.Differential Eqs.,4,121. 1969 Studies in Appl. Math., 5, 166. 1971 Japan-United States Seminar on Ordinary Differential and Functional Equations,M. Urabe,ed.，29,Springer-Verlag, Berlin.   
Yosida, K. 1966Functional Analysis， Springer, Berlin.   
Zhuravlev, S. G. 1972 Celestial Mech., 6, 255. 1973 Ibid., 8, 75.   
Zipse, H. W. 1971 Celestial Mech.,4,329.   
Zubov, V. I. 1964 Methods of A. M. Lyapunov and their Applications, Noordhoff, Groningen.

# Retrospect of Volume III

The differential equations in celestial mechanics, the perturbation theory and the lunar theory including the theory of Saturn's rings,are finally reduced to a differential equation of the second order with periodic coefficients,such as Lindstedt's or Hill's equation.Hill's equation is a generalization of the Mathieu equation in mathematical physics. The solution of the Mathieu equation is discussed in detail, together with Hill's equation. The solutions are derived rigorously in convergent series. Linear differential equations of similar form with quasi-periodic or almost periodic coefficients are solved in a rigorous manner.

However, if we transform back to the coordinates and momenta of the planetary or lunar problem the series are not uniformly convergent according to Bruns and Poincaré. The series,although not uniformly convergent, can represent the solution for a limited time interval when truncated at a term of magnitude within the accuracy of observations. This circumstance was called semi-convergent by Poincaré.

The proof of non-uniform convergence is fully discussed with the extension by Petersson and Wintner. Various methods for elevating the degree of formal convergence are treated. Mechanism are discussed.

The degree of accuracy of such semi-convergent expressions can be estimated in the Krylov-Bogoliubov method of averaging or possibly in the Ritz-Galerkin method,but is not yet known for the methods of Lagrange, Delaunay， von Zeipel, Lindstedt, Gyldén, or

Hill, that were described in Volume II. Littlewood proposed an order estimation of asymptotic solutions. Diliberto showed the asymptotic existence of a periodic surface with an application to the motion of an earth satellite. Whittaker found an adelphic integral in a certain problem in the neighborhood of an equilibrium. Contopoulos and his colleagues discussed a third integral,which is not uniformly convergent,of the motion in the galactic gravitational field or in the threebody problem by numerical computation.

The form of general solution of the planetary or the three-body problem has been studied by Newcomb,Lindstedt, Gyldén,von Zeipel, Poincaré,and Cherry,entirely disregarding the question of the convergence. The form of such a formal solution is a trigonometric series with arguments proportional to time and with coefficients arranged in powers of small parameters. If such a series be uniformly convergent then it would represent a quasi-periodic or almost periodic function. The existence of such quasi-periodic solutions under a certain condition was proved by Kolmogorov, Arnold, and Moser, as will be discussed in Volume IV.

The stability of an equilibrium is discussed in detail in Chapter 16 according to Liapounov, Bohl, and Perron. The question is whether the stability character may be modified when higher-order terms are taken into account.

The rigorous solution of the three-body problem of periodic character or asymptotic to periodic solutions will be discussed in Volume IV. The existence of the solution for the three-body problem will be rigorously proved in detail in Volume V. The singularities of the differential equations will be discussed in detail. Also the topological theory of the solution curves and the manifold of motion, i.e., the existence and behavior of periodicity and ergodicity,will be discussed in Volume V.

The author cordially expresses his gratitude for the grants from the Department of Education of the Japanese government for publication and from the National Aeronautics and Space Administration in Washington, D.C. for editing by Mr. R. Tanner of the Goddard Space Flight Center and Mr. Ed. Agro of the MIT Press.

The author is also thankful to Dr. Y. Kozai for reading the second and later proofs while the author was sick in hospital.

# Index

Note.Pages 1-503 will be found in Part 1; pages 505-1154, in Part 2.

abnormal series,511   
absolutely continuous,1104   
addition theorem of matrizants,205   
additive group,1097   
adelphic integral, 624-638   
adelphic transformation,626   
adiabatic invariant, 670   
adjacent, 966   
adjoint, 1100   
adjoint equation,113   
adjoint group,202   
adjoint space,1103   
algebra,1100   
algebraic number,777   
almost-normal coordinate,349   
almost periodic differential equations,   
697-754   
almost periodic orbit, 647   
almost periodic type, 747-754   
$\pmb { \alpha }$ -limit point, 943   
Andoyer's theory on the form of in  
tegrals,536-538   
approximately similar,1096   
associated Mathieu functions,132   
asymptotic integrals of Littlewood,   
878-899   
asymptotic representation, 505-523   
asymptotic series,508   
asymptotic solution,848,1025-1029   
asymptotic solution of the Mathieu   
equation, 123-140   
asymptotic stability，933   
asymptotically stable,921,944   
attraction,1126   
automorphism,1097   
averaging,330   
averaging method,327-405   
averaging operator,328   
Baire class,769-772   
Baire function, 772   
Baker's matrix method,199-207   
application of-,207-270   
Banach space,1102   
base，1100   
Bendixon's theorem,302   
bifurcation equation,365   
Bohlin's method,41-50   
Bohlin's series,594-602,864-874   
Bohlin's theory,567-616,583-593,   
602-616   
Bohl's theorems,978-1000   
Borel series,763-769   
boundary,1100   
bounded variation,811   
Brillouin-Wentzel-Kramers method,   
120   
Brouwer's fixed-point theorem,1104   
Bruns's method, 72-80   
Bruns's proof of convergence,779-781   
canonical form of finite equations of   
Lie group,201   
Cantor's solution,767   
Cassini's and Encke's divisions,185-   
199   
Cauchy sequence, 764,1101   
center-focus,965   
uai puu,   
Cetaev's theorem, 929   
characteristic equation,3   
characteristic exponent, 97,110,1083,   
characteristic index,1124   
characteristic number,413,910-921   
characteristic roots,1048   
Charlier's comment, 791-796   
circular product, 23   
class of trajectory,696   
closed linear manifold,1098   
closed set,723,763   
closure,764   
commutative group,1097   
compact,763,1101   
complete,764,1102   
complete stability,1126   
completely continuous,1122   
completely exponentially unstable,952   
completely unstable, 936,1046   
completeness theorem of Fourier   
series,812   
component, 764   
condensation,766   
condensation-point, 764   
conditionally compact, 1100   
conditionally stable,906,1047   
confluence,1110   
confluent hypergeometric function,   
112,136   
conjugate,810   
conjugate space,1103   
conjugation,1097   
connected,764   
constant of the mean,1090   
continued fraction, 773-774   
continuous,765   
continuum,764   
control, 1126-1135   
convergence of Hill's determinant,   
21-26   
convex,964,1104   
coset,1097   
Cotton's integral equation,1037-1046   
covering,1101   
critical inclination,366   
decomposable solution, 751   
decrescent 938   
definite function, 922   
degenerate nodal point, 965   
degenerate normal, 411   
degree, 827   
dense,764,1102   
derived set, 763   
diffeomorphism,1101   
difference equations,686   
Diliberto's theory,461-472   
Dini's criterion, 814   
Diophantine approximation, 779   
direct sum,1099   
Dirichlet criterion,814   
discontinuous,765   
discontinuous recurrent, 297   
discriminant, 146   
divergence of Bohlin's series,861-863   
divergence of Lindstedt's series,856-   
861   
domain, 764   
Du Bois-Reymond theorem,813   
dual space,1103   
Duffing's problem,290   
dynamical system, 942-954   
eigenfunction, 99   
eigenvalue, 99   
electron motion in a magnetron, 258-   
270   
elevation of the degree of formal con  
vergence,827-847   
elliptic cylinder function,81,99   
elliptic invariant point, 4   
elliptic trajectory,965   
embedding,1103   
equation for variation,16   
equi-asymptotically stable, 935   
equicontinuous,1103   
equilibrium figure,152-163   
equilibrium position,1030-1037   
equivalent, 775,1103   
ergodic,638,905   
error estimate,356-363   
error estimate of averaging method,   
334-341   
essentially divergent, 774   
even instability,16   
everywhere dense,764   
existence and uniqueness of a periodic   
surface,431-434   
exponentially stable,952   
external resonance,1139   
Faa de Bruno operator,310   
factor group,1097   
field,1097   
fixed-point property,1104   
fixed-point theorem,296,341   
Floquet's theorem,1-10   
fluctuation, 771   
form of the integral,505-507   
formal stability in the three-body prob  
lem,472-480   
formally analytic function,473   
formally convergent, 519,827-841   
Fréchet space,1102   
Fuchs's theory,81   
functional,1099   
fundamental determinant, 973   
fundamental set,1098   
general stability，1136   
generalized Liapounov function,965   
generator,751   
genus,147   
genus （geschlecht）of an entire func  
tion, 518   
global,935,936   
gravitational dilution factor,177   
Green's theorem,39   
grouping of terms,841-848   
Gylden's method,50-65   
Gyldén's probability theorem,781-791   
Hadamard's theorem,26-32   
Hale-Cesari theory,363-375   
Hankel function,125   
Harzer's method, 88-90   
Haupt's theorem,148   
Hausdorff space,1101   
Heine-Borel's covering theorem, 764   
heteroclinic, 674   
heuristic method,59   
Hilbert space,1104   
Hill's argument, 852-856   
Hill's equation,1-32,10-21,110-123,   
207-214   
Hill's infinite determinant,13   
homeomorphic,410   
homeomorphism,1101   
homomorphic,1097   
homotopic,1116   
hull, 764   
Hurwitz's theorem, 931   
hyperbolic-cylinder function,104   
hyperbolic invariant point,4   
hyperbolic trajectory,965   
ideal resonance,612   
idempotent operator,1099   
identity operator,1098   
image,1097   
index of inertia,1125   
index of rotation,1108   
integral equations of Volterra's t   
1037   
integral surface,643   
integrating operator, 328   
internal resonance,1139   
invariant, 1097   
invariant curve,643   
invariant point,638   
invariant set,942   
inverse,1097   
involution,1100   
irregular integral, 507-519   
isolated set,764   
isolating integral, 638   
isometric isomorphism,1103   
isometrically equivalent,1103   
isomorphism,1097   
Jacobi identity，2   
Jordan criterion,814   
jump arcs,306   
kinematic similarity,1083-1096   
Kowalewski's theory,155   
Krasovskii's theorem,952   
Kronecker's theorem，234   
Kruskal's method,492-495   
Krylov-Bogoliubov method,283-295,   
310-327

lacunary series,813   
Lagrange's theorem, 928   
Laguerre's theorem,147   
λ-family of periodic two-surface,408   
Lamé function,80   
Laplace transform,511   
last geometric theorem of Poincaré, 297   
Lebesgue integral, 772   
left ideal,1100   
Liapounov function,905,927   
Liapounov stability,905-978   
Liapounov's direct method, 921-933   
Liapounov's frst theorem for stability, 922   
Liapounov's first theorem on instability，926   
Liapounov's function, 954-973   
Liapounov's second theorem on instability，927   
Liapounov's second theorem on stability，925   
Liapounov's theorems, 933-942

Lie's theory of finite continuous   
groups,200   
limit characteristic numbers,413   
limit cycle,291   
limit-deviation,967   
limit-deviation gradient,967   
limited function,910,922   
limiting point,763   
Lindemann's discussion,80-83   
Lindstedt equation, 33-96,215   
Lindstedt's method, 33-41   
Lindstedt's theory, 530-538,567-578   
linear functional, 1099   
linear operators,1097-1105   
linear space,1098   
linear topological space,1102   
Liouville-Green factor,134   
Liouville's number, 773-779   
Littlewood's theorems,878-883   
locally convex,1104   
logarithmic normal series,511   
Malkin's theorem, 1127   
mapping,1097   
Mathieu equation,96-152,214-217   
Mathieu function, 99   
Mathieu function of the first kind,102   
Mathieu function of the second kind,   
102   
matrix method,207-217,222-227   
matrix method of integration,199-270   
matrizant,204   
Maxwell's theory,163-173   
measurable, 770   
measurable B, 771   
mechanism of divergence,864-874   
Mellin function,136   
method of steepest descent,136,137   
metric,942,1101   
metric space,1101   
metrizable,1101   
minor, 751   
Mittag-Leffler's star region,203   
modulus, 724   
modulus of continuity,812   
modulus of instability,16   
monodromy group,1106   
monodromy matrix,3   
multiplication operator, 420   
multiplicator,739   
multiplier,1106   
natural homomorphism,1099   
negative-semi-definite, 937   
neighborhood,763   
Newcomb's theory on the form of   
integrals,523-530   
nilpotent,1099   
non-conditionally convergent, 775   
non-essentially divergent,774   
nonuniform convergence, 779-796,   
816-825   
norm,942,1102   
normal,411,1089   
normal coordinate,349   
normal determinant,23   
normal function,723-728   
normal integral, 511,512   
normal series,511   
normal space,1101   
normal system,912   
normed linear space,942   
normed space,1102   
nowhere dense,764,1102   
nucleus, 764   
null set, 1100   
null space,1100   
number of zeropoints,140-152   
$\pmb { \omega }$ -limit point,943   
open set, 763   
order number,1061   
ordinary periodic solution,625   
oscillation theorem,145

parabolic trajectory,965   
Parseval's formula,812   
partially degenerate normal system, 412   
penalty function,1133   
perfect,764   
periodic q-surface,410   
periodic solution and asymptotic solution,848-852   
periodic solutions for satellite motion (Diliberto's theory),461-472   
periodic solutions of the earth satellite problem,363-375   
periodic surface,405-415   
periodic surface applied to satellite motion,434-447   
periodic surface method, 405-488   
periodic two-surface,450   
permanent surface,413   
Perron's generalization,1066-1083   
Perron's order number,1060-1066   
Perron's stability criterion,1046-1096   
perturbation,906

Petersson's refinement, 796-804   
Picart's method, 90-96   
piecewise discontinuous,813   
place,700,1015   
Poincaré's formulation   
of Bohlin's theory,583-593   
of Lindstedt's theory,567-578   
Poincaré's inequality, 155   
Poincaré's theory on the form of in  
tegrals,551-567   
Poincare's transformation, 551-563   
Poincaré-von Zeipel method,310-327   
point-set measurable B,771   
pointwise discontinuous,771   
positive-semi-definite,937   
power of continuum,764   
pregnant behavior,952   
primary solution,748   
product-set,763   
projection,1099   
properly uniformly convergent, 765   
pseudo-solution, 751

qualitative properties of satellite orbits, 480-488   
quasi-periodic,696   
quasi-periodic function, 685, 697-716, 1000-1013

range,1097   
rank of the differential equation,516   
Rayleigh's equation,290   
reduced determinant, 21   
reduced fraction,773   
reducible,1083   
reducible system,916   
reduction principle,964   
regular arc,306   
regular family,674   
regular space,1101   
regular system,914   
related equation,707   
relation to asymptotic solutions, 875-   
878   
relative topology，1100   
resonance domain,261   
Rhea,227-231   
Riemann's function, 767   
Riesz-Fischer theorem,812   
right ideal,1099   
rigid-body rotation,1135-1142   
ring,1097   
ring-form equilibrium figures,152-163   
Ritz-Galerkin method,488-492   
Roche limit,184   
rotation number,302,668   
Rouche's theorem,357   
saddle point, 965   
satellite motion, 351-356-,375   
Saturn's ring,163-199,217-222   
Saturn's satellites,252-258   
scalar,1105   
Schauder's theorem,1104   
secular constant, 714-715   
secular perturbation of higher degree,   
231-247   
secular term,506   
semi-convergent series,519-523   
semi-resonance,264   
separable,764,1102   
servomechanism, 1128   
simply connected region,203   
singular coordinate,1013   
singular periodic solution,626   
spectrum,99   
stability, 905-910   
stability domain,1105   
stability in abstract space,1122-1126   
stability probability,936,967   
stable,16,906,1122   
stable coordinate,1013-1025   
stable focal point, 965   
stable nodal point, 965   
stable under disturbances,941   
standard form,328   
Stieltjes's discussion,84-88   
stochastic process,1135   
stochastic stability,1135   
Stormer problem,118   
strong characteristic exponent, 1090   
strongly stable, 936,1105-1122   
structure constant, 200   
subharmonic,296   
subring,1099   
successive consequent, 638,773   
sum-set, 763   
surface transformation, 638   
symplectic matrix,1109   
system with slow variation,375-405   
theory of libration,222-227   
third integral, 638-674   
Thome's normal series,516   
Tisserand's method, 66-72   
Tisserand's theory on the form of in  
tegrals,536   
topological group,1102   
topological space,1100   
topology，1100   
total variation,1100   
totalization,823   
totally discontinuous,771   
totally stable,941   
trajectory, 942,943   
transcendental number,777   
transformation $\boldsymbol { \tau }$ of a periodic surface   
into itself,415-430   
translational operator,420   
triangular matrix,1083   
trigonometric series,810-856   
Trojan asteroid,247-252   
truncated sum,812   
truncated trigonometrical polynomial,   
490   
twist mapping,485   
two-sided ideal,1100   
two-variable expansion procedure,322   
uneven instability,16   
uniform asymptotic stability,933   
uniformly asymptotically stable,935,   
944   
uniformly asymptotically stable glob  
ally,936   
uniformly attracting,944   
uniformly bounded,819   
uniformly continuous, 765,1102   
uniformly stable,934   
uniformly stable globally,935   
uniqueness theorem of Fourier series,   
813   
unstable,16,906   
unstable coordinate,1013   
unstable focal point, 965   
unstable nodal point, 965   
Van der Pol's equation,290,295-310   
vanishing function,910   
Vessiot's transformation,563-567   
Von Zeipel's theory on the form of   
integrals,538-551

weakly simple,413   
weakly stable,1122   
weakly uniformly asymptotically stable, 941   
Weierstrassian approximation theorem, 812   
Whittaker's method,96-99   
Whittaker's theory on the form of integrals,616-697   
Wintner's discussion, 804-810

zero operator,1098   
zone of instability, 674   
Zubov's theorem, 946

global and strong stability,kinematic/ similarity and order numbers,are introduced,even stability in abstract space is stated.

The following Volumes are on the periodic and quasi-periodic solutions and on the topology of the three-body problem.

![](images/c2f714a703b1bf5e04a3a2227f8ed65bc0cfe6fe55e6c040e04843e93507be89.jpg)