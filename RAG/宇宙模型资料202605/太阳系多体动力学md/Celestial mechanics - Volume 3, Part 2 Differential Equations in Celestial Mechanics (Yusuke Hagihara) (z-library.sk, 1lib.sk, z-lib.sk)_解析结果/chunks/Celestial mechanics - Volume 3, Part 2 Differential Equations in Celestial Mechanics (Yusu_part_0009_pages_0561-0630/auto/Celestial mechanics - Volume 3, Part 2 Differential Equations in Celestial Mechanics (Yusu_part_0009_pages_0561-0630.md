This is contradictory to (156). Therefore $\beta$ is equal to $\Re ( \rho _ { l } )$ with a certain index l. The first part of Theorem 11 is thus established.

Theorem 12: If the functions $\phi _ { s }$ of the differential system

$$
\frac { d x _ { s } } { d t } = \rho _ { s } x _ { s } + \phi _ { s } ( x _ { 1 } , \ldots , x _ { n } , t ) \qquad ( s = 1 , \ldots , n ) ,
$$

satisfy the conditions (A） and (B),and if $\Re ( \rho _ { 1 } ) > \Re ( \rho _ { 2 } ) > \cdots >$ $\Re ( \rho _ { n } )$ ，then for each solution $x _ { s }$ for which

$$
\operatorname* { l i m } _ { t \to \infty } x _ { 1 } = 0 , \dots , \operatorname* { l i m } _ { t \to \infty } x _ { n } = 0
$$

there is an index $\mathbf { \xi } _ { l }$ such that

$$
\begin{array} { r l } & { \underset { t  \infty } { \operatorname* { l i m } } ( \frac { x _ { s } } { x _ { l } } ) = 0 \qquad \mathrm { f o r } \qquad s \neq l , } \\ & { \underset { t  \infty } { \operatorname* { l i m } } ( \frac { 1 } { x _ { l } } \frac { d x _ { l } } { d t } ) = \rho _ { l } , \qquad \Re ( \rho _ { l } ) \leq 0 . } \end{array}
$$

If the functions $\phi _ { s }$ satisfy also the condition (C),then conversely there exists a solution of this nature corresponding to an index $\imath$ for which $\Re ( \rho _ { l } ) < 0$ ，and such solutions for $l \geq j$ form a family with just $n -$ $j + 1$ arbitrary constants.

Choose a fixed number $c > 0$ such that

$$
\Re ( \rho _ { s } ) - c > \Re ( \rho _ { s + 1 } ) + c \qquad ( s = 1 , \ldots , n - 1 ) .
$$

Since the $\phi _ { s }$ satisfy the condition (B),we have

$$
| \phi _ { s } | \leq { \frac { c \varepsilon } { 2 n } } \left( | x _ { 1 } | + \cdot \cdot \cdot + | x _ { n } | \right) ,
$$

or

$$
\sum _ { s = 1 } ^ { n } | x _ { s } \phi _ { s } | \leq \frac { c \varepsilon } { 2 n } ( | x _ { 1 } | + \cdot \cdot \cdot + | x _ { n } | ) ^ { 2 } \leq \frac { c \varepsilon } { 2 } \sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } .
$$

Assume $l > 1$ and put

$$
\sum _ { s = 1 } ^ { l - 1 } | x _ { s } | ^ { 2 } = \Phi ( t ) , \qquad \sum _ { s = l } ^ { n } | x _ { s } | ^ { 2 } = \Psi ( t ) ,
$$

then from the given differential equations we obtain after computation

$$
\frac { 1 } { 2 } \frac { d } { d t } [ \Phi ( t ) - \varepsilon \Psi ( t ) ] \geq [ \Re ( \rho _ { \rho - 1 } ) - c ] [ \Phi ( t ) - \varepsilon \Psi ( t ) ] .
$$

Hence

$$
\exp \left\{ - 2 [ \Re ( \rho _ { l - 1 } ) - c ] t \right\} \cdot \left[ \Phi ( t ) - \Psi ( t ) \right]
$$

increases monotonically for $t \geq T _ { \varepsilon }$ ， but this cannot be positive for $t \geq T _ { \varepsilon }$ ， as can be seen by reasoning similar to the proof of Theorem 11. Thus we have $\Phi ( t ) \leq \varepsilon \Psi ( t )$ for $t \geq T _ { \varepsilon }$ . Since $\Phi ( t )$ and $\Psi ( t )$ cannot vanish simultaneously by Theorem 2,we have

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { \Phi ( t ) } { \Psi ( t ) } } = 0 ,
$$

or

$$
\operatorname* { l i m } _ { t \to \infty } \frac { | x _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { l - 1 } | ^ { 2 } } { | x _ { l } | ^ { 2 } + \cdot \cdot \cdot + | x _ { n } | ^ { 2 } } = 0 \qquad \mathrm { i f } \qquad l > 1 .
$$

Assume $l < n$ and put

$$
\sum _ { s = l + 1 } ^ { n } | x _ { s } | ^ { 2 } = \Omega ( t ) ,
$$

then from the differential equations and (159) we obtain

$$
\frac { 1 } { 2 } \frac { d } { d t } [ \varepsilon | x _ { l } | ^ { 2 } - \Omega ( t ) ] \geq [ \Re ( \rho _ { l } ) - c ] [ \varepsilon | x _ { l } | ^ { 2 } - \Omega ( t ) ]
$$

fort≥T≥T..

Hence

$$
\mathrm { e x p } \left\{ - 2 [ \Re ( \rho _ { l } ) - c ] t \right\} \cdot [ \varepsilon | x _ { l } | ^ { 2 } - \Omega ( t ) ]
$$

increases monotonically for $t \geq T _ { \varepsilon } ^ { \prime }$ . We have

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { | x _ { l + 1 } | ^ { 2 } + \mathbf { \cdots } + | x _ { n } | ^ { 2 } } { | x _ { l } | ^ { 2 } } } = 0 \qquad { \mathrm { i f } } \qquad l < n .
$$

Thus for any value of $\imath$ we have (Perron,1913)

$$
\operatorname* { l i m } _ { t  \infty } { \frac { x _ { s } } { x _ { l } } } = 0 \qquad ( s \neq l ) .
$$

By the condition (B) we obtain,from the Ith differential equation,

$$
\displaystyle \operatorname* { l i m } _ { t \to \infty } \frac { 1 } { x _ { t } } \frac { d x _ { t } } { d t } = \rho _ { t } + \operatorname* { l i m } _ { t \to \infty } \left( \frac { \phi _ { l } ( x _ { 1 } , \ldots , x _ { n } , t ) } { | x _ { 1 } | + \cdot \cdot \cdot + | x _ { n } | } \frac { | x _ { 1 } | + \cdot \cdot \cdot + | x _ { n } | } { x _ { l } } \right) = \rho ,
$$

Perron (1929) then applied the theory to

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } [ a _ { s i } + \phi _ { i s } ( t ) ] x _ { i } \qquad ( s = 1 , \ldots , n ) .
$$

16.15PERRON'S ORDER NUMBER OF DIFFERENTIAL EQUATIONS

Consider the diferential equations

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } f _ { s i } ( t ) x _ { i } \qquad ( s = 1 , \ldots , n ) ,
$$

where the $f _ { s i } ( t )$ are bounded, $| f _ { s i } ( t ) | \le c$ ．Multiplying（160） by the conjugate complex $\bar { \boldsymbol { x } } _ { s }$ , we.obtain

$$
\frac { 1 } { 2 } \frac { d } { d t } | x _ { s } | ^ { 2 } = \Re \Big ( \bar { x } _ { s } \frac { d x _ { s } } { d t } \Big ) \leq | x _ { s } | \sum _ { i = 1 } ^ { n } c | x _ { i } | \leq c \sum _ { i = 1 } ^ { n } \frac { | x _ { s } | ^ { 2 } + | x _ { i } | ^ { 2 } } { 2 } ,
$$

and

$$
{ \frac { 1 } { 2 } } { \frac { d } { d t } } | x _ { s } | ^ { 2 } \equiv - | x _ { s } | \sum _ { i = 1 } ^ { n } c | x _ { i } | \equiv - c \sum _ { i = 1 } ^ { n } { \frac { | x _ { s } | ^ { 2 } + | x _ { i } | ^ { 2 } } { 2 } } .
$$

Put

$$
\sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } = \phi ( t ) ;
$$

then

$$
\frac { 1 } { 2 } { \phi } ^ { \prime } ( t ) \left\{ \mathop { = } ^ { \le n c { \phi } ( t ) } , \right.
$$

Similarly,

$$
\frac { d } { d t } \left[ \phi ( t ) e ^ { - 2 \pi c t } \right] \leq 0 , \frac { 1 } { 2 } \left[ \phi ( t ) e ^ { 2 \pi c t } \right] \geq 0 .
$$

Thus we get

$$
\phi ( t ) e ^ { - 2 \pi c t } \leq \phi ( 0 ) , ~ \phi ( t ) e ^ { 2 \pi c t } \geq \phi ( 0 ) ,
$$

or

$$
- 2 n c \equiv \operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \log \phi ( t ) \equiv \operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \log \phi ( t ) \equiv 2 n c ,
$$

or

$$
2 \gamma \equiv \operatorname* { l i m } _ { t  \infty } \frac { 1 } { t } \log \phi ( t ) \begin{array} { l } { \{ \equiv 2 n c ,  } \\ {  \geq - 2 n c . } \end{array} 
$$

It can be seen that there are at most $\pmb { n }$ distinct possible values of $\gamma$ . Suppose that there were $n + . 1$ distinct values of $\gamma \colon \gamma _ { 1 } < \gamma _ { 2 } < \cdots$ $< \gamma _ { n + 1 }$ . Let $\boldsymbol { x } _ { s } = \boldsymbol { x } _ { s , \lambda }$ be a solution with $\gamma = \gamma _ { 2 }$ ; then

$$
\operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \log \operatorname* { m a x } _ { s = 1 } ^ { \infty } | x _ { s , \cdot } | = \gamma _ { \imath } ~ ( \lambda = 1 , \ldots , n + 1 ) .
$$

There should be a linear homogeneous relation among $n + 1$ solutions $x _ { s , 1 } , \ldots , x _ { s , n + 1 }$ ，such as

$$
C _ { 1 } x _ { s , 1 } + C _ { 2 } x _ { s , 2 } + \cdot \cdot \cdot + C _ { n + 1 } x _ { s , n + 1 } = 0 \qquad ( s = 1 , \ldots , n ) .
$$

Let $C _ { p + 1 }$ be the last nonzero coefficient, $p + 1 > 1$ . Then $C _ { p + 1 } = - 1$ and

$$
x _ { s , p + 1 } = \sum _ { \lambda = 1 } ^ { p } C _ { \lambda } x _ { s , \lambda } \qquad ( s = 1 , \ldots , n ) .
$$

From these relations we should have with a suffciently small positive $\varepsilon$

$$
\operatorname* { m a x } _ { s = 1 } ^ { n } | x _ { s , \lambda } | < \exp \left\{ ( \gamma _ { \lambda } + c ) t \right\} \leq \exp \left\{ ( \gamma _ { p } + \varepsilon ) t \right\}
$$

for all sufficiently large t. Then we should have

$$
\operatorname* { m a x } _ { s = 1 } ^ { n } | x _ { s , p + 1 } | \leq \sum _ { \lambda = 1 } ^ { p } | C _ { \lambda } | \exp \left\{ ( \gamma _ { p } + \varepsilon ) t \right\}
$$

for all sufficiently large t. Hence

$$
\gamma _ { p + 1 } = \operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \log \operatorname* { m a x } _ { s = 1 } ^ { n } | x _ { s , p + 1 } | \leq \gamma _ { p } + \varepsilon ,
$$

or $\gamma _ { p + 1 } \leqq \gamma _ { p }$ ， which is contrary to our construction.

A number $\gamma _ { \lambda }$ such as

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { 1 } { t } } \log \sum _ { s = 1 } ^ { n } | x _ { s } | = \gamma _ { \lambda }
$$

is called the order number (Ordnungszahl) of the solution $x _ { s }$ (Perron, 1930).

The order number of a linear combination of a finite number of solutions, whose order numbers are $\leq \gamma _ { \lambda }$ ,is also $\leq r _ { 2 }$

Let $e _ { 1 }$ be the number of linearly independent solutions whose order numbers are the smallest possible, i.e., $\gamma _ { 1 }$ ，among the linear independent solutions and their linear combinations.Let $e _ { 1 } + e _ { 2 }$ be the number of linearly independent solutions whose order numbers are equal to either $\gamma _ { 1 }$ or $\gamma _ { 2 }$ , and so forth. Thus $e _ { \lambda }$ is the multiplicity of $\gamma _ { \lambda }$ ， and $e _ { 1 } + \cdots + e _ { n } = n$

Theorem 1: The number of the order numbers of linear differential equations (16O) is just equal to $_ n$ if the multiplicity is properly counted.

Theorem 2: Let $\gamma _ { 1 } , \ldots , \gamma _ { n }$ be the order numbers of the differential equations (16O)； then we have the estimate

$$
\sum _ { s = 1 } ^ { n } \tau _ { s } \geq \operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } \sum _ { \lambda = 1 } ^ { n } \Re ( f _ { \lambda \lambda } ( \tau ) ) \ d \tau .
$$

In fact, we have for an arbitrary positive number $\varepsilon$

$$
\left| x _ { s , { \lambda } } \right| < \exp \left\{ \left( \gamma _ { \lambda } + \frac { \varepsilon } { n } \right) t \right\} .
$$

The determinant is

$$
X = \| x _ { s , \ i } \| < n ! \exp \bigg \{ \bigg ( \sum _ { \lambda = 1 } ^ { n } r _ { \lambda } + \varepsilon \bigg ) t \bigg \} .
$$

Hence

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { 1 } { t } } \log | X | \leq \sum _ { \lambda = 1 } ^ { n } \gamma _ { \lambda } .
$$

On the other hand,since

$$
X = a \exp \left\{ \int _ { 0 } ^ { t } \sum _ { \lambda = 1 } ^ { n } f _ { \lambda \lambda } ( \tau ) d \tau \right\} \qquad ( a = \mathrm { c o n s t a n t } ) ,
$$

we obtain

$$
\operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \log | X | = \varlimsup _ { t \to \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } \sum _ { \lambda = 1 } ^ { n } \Re ( f _ { \lambda \lambda } ( \tau ) ) \ d \tau .
$$

Thus the theorem is established.

Consider an adjoint system (Section 3.8) to the system (160):

$$
\frac { d y _ { s } } { d t } = - \sum _ { i = 1 } ^ { n } f _ { i s } ( t ) y _ { i } \qquad ( s = 1 , \ldots , n ) .
$$

Theorem 3: Let the order numbers of the system (160) be $\left( \Gamma \right)$ ： $\gamma _ { 1 } \leq \gamma _ { 2 } \leq \cdot \cdot \cdot \leqq r _ { n }$ ，and those of (160a) be $( \Delta ) \colon \delta _ { 1 } \leq \delta _ { 2 } \leq \cdot \cdot \cdot \leq \delta _ { n } ,$ then we have always $\gamma _ { s } + \delta _ { s } \geq 0$ $( s = 1 , \ldots , n )$

In fact, we have

$$
\frac { d X } { d t } = F X , \qquad F = \| f _ { s i } ( t ) \| , \qquad X = \| x _ { s , i } \| ,
$$

and

$$
\frac { d Y } { d t } = - Y F , \qquad Y = | | y _ { s i } | | ;
$$

accordingly

$$
Y { \frac { d X } { d t } } + { \frac { d Y } { d t } } X = 0 .
$$

The integral is

$$
Y X = C , \quad \quad C = \| c _ { i j } \| = { \mathrm { c o n s t a n t } } ,
$$

or

$$
\sum _ { s = 1 } ^ { n } y _ { \lambda s } x _ { s \mu } = c _ { \lambda \mu } \qquad ( \lambda , \mu = 1 , \ldots , n ) .
$$

Since by the definition of order numbers we have

$$
| x _ { s , \lambda } | \leq \exp { \{ ( \gamma _ { \lambda } + \varepsilon ) t \} } , \qquad | y _ { \lambda , s } | < \exp { \{ ( \delta _ { \lambda } + \varepsilon ) t \} } ,
$$

we obtain

$$
| c _ { \lambda \lambda } | \equiv \sum _ { s = 1 } ^ { n } | y _ { \lambda , s } x _ { s , \lambda } | \equiv n \exp { \{ ( \gamma _ { \lambda } + \delta _ { \lambda } + 2 \varepsilon ) t \} } .
$$

Hence $\gamma _ { \lambda } + \delta _ { \lambda } \geq 0$ if $c _ { \scriptscriptstyle { \lambda \lambda } } \neq 0$ ·

Let

$$
X A = X ^ { * } , \qquad A = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { } & { } & { 0 } \\ { a _ { 2 1 } } & { 1 } & { } & { } & { 0 } \\ { \cdots } & { } & { } & { } & { } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { 1 } \end{array} \right] } ,
$$

where the $a _ { s \lambda }$ are arbitrary constants for $s > \lambda$ . Then the elements $\boldsymbol { x } _ { s 2 } ^ { * }$ of $X ^ { * }$ form the fundamental system of solutions of (160).We have

$$
B Y = Y ^ { * } , \qquad B = \left[ \begin{array} { l l l l } { 1 } & { 0 } & { \cdots } & { 0 } \\ { b _ { \scriptscriptstyle 2 1 } } & { 1 } & { } & { 0 } \\ { \cdots } & { } & { } \\ { b _ { \scriptscriptstyle n 1 } } & { b _ { \scriptscriptstyle n 2 } } & { \cdots } & { 1 } \end{array} \right] ,
$$

where the $b _ { \scriptscriptstyle { 2 s } }$ are arbitrary constants for $\lambda > s$ .The elements $y _ { \lambda s } ^ { * }$ of $\ b { Y } ^ { * }$ form the fundamental system of solutions of (160a).

From $X ^ { * } = X A$ ， $Y ^ { * } = B Y$ we obtain $Y ^ { * } X ^ { * } = B Y X A = B C A$ $= C ^ { * }$ ，or

$$
\begin{array}{c} \begin{array} { r l } & { \begin{array} { c c c c c } { 0 } \\ { 0 } \\ { 0 } \\ { \left[ c _ { 2 1 } \right]} & { c _ { 2 2 } } & { c _ { 2 n } } \\ { c _ { 1 } - } \\ { c _ { n 1 } } & { c _ { n 2 } } & { c _ { n n } } \end{array}  \left[ \begin{array} { c c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { 1 } & { 0 } & { 0 } \\ { \cdots } & { } & { } & { } \\ { \cdots } & { } & { } & { } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { 1 } \end{array} \right] } \end{array}  \\ & { \begin{array} { r l } & { \begin{array} { r l } { \left[ c _ { 1 1 } ^ { \ast } \right]} & { c _ { 1 2 } ^ { \ast } } & { c _ { 1 n } ^ { \ast } } \\ { c _ { 2 1 } ^ { \ast } } & { c _ { 2 2 } ^ { \ast } } & { c _ { 2 n } ^ { \ast } } \\ { \cdots } & { } & { } & { \ddots } \\ { c _ { n 1 } ^ { \ast } } & { c _ { n 2 } ^ { \ast } } & { c _ { n 1 } ^ { \ast } } \end{array}  } \end{array} } \\ & { = \left[ \begin{array} { c c c c } { c _ { 1 1 } ^ { \ast } } & { c _ { 2 1 } ^ { \ast } } & { c _ { 2 n } ^ { \ast } } \\ { \cdots } & { } & { } & { } \\ { c _ { n 1 } ^ { \ast } } & { c _ { n 2 } ^ { \ast } } & { c _ { n 2 } ^ { \ast } } \end{array} \right] . } \end{array}
$$

We can see that it is possible to choose $a _ { \scriptscriptstyle \mu k } , b _ { \scriptscriptstyle \ k \lambda }$ so that all $c _ { \kappa k } ^ { * }$ are nonzero.

If the $f _ { s i } ( t )$ are all constant, then $\gamma _ { s } + \delta _ { s } = 0$ and the order numbers of the systems (160) and (160a) are equal and of opposite sign. More generally we have

Theorem 4: The relation $\gamma _ { s } + \delta _ { s } \geq 0$ in Theorem 3 is replaced by $\gamma _ { s } + \delta _ { s } = 0$ if and only if the limit

$$
\operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } \sum _ { \lambda = 1 } ^ { n } \Re ( f _ { \lambda \lambda } ( \tau ) ) \ d \tau
$$

exists and is equal to $\sum { \mathfrak { z } } _ { = 1 } ^ { n } \gamma _ { \mathfrak { s } }$

Consider a system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } [ f _ { s i } ( t ) + \phi _ { s i } ( t ) ] x _ { i } \qquad ( s = 1 , \ldots , n ) ,
$$

beside the system (160),where the $\phi _ { s i } ( t )$ tend to zero for sufficiently large values of $t \geq t _ { 0 }$ .Then all solutions of (160b) tend to the solutions of (160) for $t \to \infty$ . The order numbers of the two systems are equal. This is true for $n = 1$ , but not always so for $n > 1$

Let the order numbers of the system (160b) be $\gamma _ { 1 } ^ { \prime } \leq \gamma _ { 2 } ^ { \prime } \leqq \cdot \cdots \leqq \gamma _ { n } ^ { \prime }$ . If for any positive ε a positive $\delta$ can be chosen so that for $| \phi _ { s i } ( t ) | \leq \delta ;$ at least for large values of $t$ we have $| \gamma _ { \ast } ^ { \prime } - \gamma _ { \ast } | \leq \varepsilon$ ，then the number $\gamma _ { k }$ is said to be unstable. If $\gamma _ { k }$ is stable,then $\gamma _ { k } ^ { \prime } = \gamma _ { k }$ follows from $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } \phi _ { s i } ( t ) = 0 } \end{array}$

Thus a small change in the coefficients yields a large change in the order numbers. Perron (1930) made estimates of the order numbers.

Theorem 5: If the coefficients of the differential equations (160) satisfy

$$
\Re ( f _ { 1 1 } ( t ) ) \geq P ( t ) + 2 ( n - 1 ) Q ( t ) ,
$$

$$
P ( t ) = \operatorname* { m a x } _ { \lambda = 2 } ^ { n } \Re ( f _ { \lambda \lambda } ( t ) ) , \qquad Q ( t ) = \operatorname* { m a x } _ { s \neq i } | f _ { s i } ( t ) |
$$

for sufficiently large values of $t \left( t \geq \mathbf { } t _ { 0 } \right)$ , then the largest order numbei $\gamma$ is contained between the limits

$$
\begin{array} { r }  \gamma \{ \begin{array} { l l }  \displaystyle \leq \frac { \displaystyle \operatorname* { l i m } _ { t  \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } [ \Re ( f _ { 1 1 } ( \tau ) ) + ( n - 1 ) Q ( \tau ) ] d \tau , } \\ { \displaystyle \geq \frac { \displaystyle \operatorname* { l i m } _ { t  \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } [ \Re ( f _ { 1 1 } ( \tau ) ) - ( n - 1 ) Q ( \tau ) ] d \tau . } \end{array}  } \end{array}
$$

Theorem 6: If the coeffcients of the differential equations (160) satisfy

$$
\begin{array} { r l r } & { \underset { t  \infty } { \operatorname* { l i m } } f _ { s i } ( t ) = 0 } & { ( s \neq i ) , } \\ & { \underset { ( ) \times ( f _ { 1 1 } ( t ) ) } { \operatorname* { s u p } } \cong \Re ( f _ { \lambda \lambda } ( t ) ) + c } & { ( c > 0 ) , } \end{array}
$$

for $t \geq t _ { 0 } ( \lambda = 2 , . . . , n )$ , then the largest order number is stable and is equal to

$$
\operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } \Re ( f _ { 1 1 } ( \tau ) ) \ d \tau .
$$

In fact, from the differential equations we obtain

$$
\begin{array} { r l r } {  { \frac { 1 } { 2 } \frac { d } { d t } | x _ { s } | ^ { 2 } = \sum _ { i = 1 } ^ { n } \Re ( f _ { s i } ( t ) \bar { x } _ { s } x _ { i } ) } } \\ & { } & { \quad \le \Re ( f _ { s s } ( t ) ) | x _ { s } | ^ { 2 } + Q ( t ) \sum _ { i ( i \ne s ) } \frac { 1 } { 2 } \{ | x _ { s } | ^ { 2 } + | x _ { i } | ^ { 2 } \} , } \end{array}
$$

or by the assumption of Theorem 5

$$
\frac { 1 } { 2 } \frac { d } { d t } \sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } \leq \Re ( f _ { 1 1 } ( t ) ) \sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } + ( n - 1 ) Q ( t ) \sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } ,
$$

or

$$
\begin{array} { r l r } {  { \frac { 1 } { 2 } \frac { d } { d t } \bigg ( | x _ { 1 } | ^ { 2 } - \sum _ { s = 2 } ^ { n } | x _ { s } | ^ { 2 } \bigg ) } } \\ & { } & { \geq [ \Re ( f _ { 1 1 } ( t ) ) - ( n - 1 ) Q ( t ) ] \bigg ( | x _ { 1 } | ^ { 2 } - \sum _ { s = 2 } ^ { n } | x _ { s } | ^ { 2 } \bigg ) . } \end{array}
$$

From these relations it follows that

$$
\sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } \exp \left\{ - 2 \int _ { 0 } ^ { t } \left[ \Re ( f _ { 1 1 } ( \tau ) ) + ( n - 1 ) Q ( \tau ) \right] d \tau \right\}
$$

decreases monotonically, and

$$
\left( | x _ { 1 } | ^ { 2 } - \sum _ { s = 2 } ^ { n } | x _ { s } | ^ { 2 } \right) \exp \left\{ - 2 \int _ { 0 } ^ { t } \left[ \Re ( f _ { 1 1 } ( \tau ) ) - ( n - 1 ) Q ( \tau ) \right] d \tau \right\}
$$

increases monotonically. Hence, if we so choose the initial value that $\scriptstyle | x _ { 1 } | ^ { 2 } - \sum _ { 1 } ^ { n } = 2 \displaystyle | x _ { s } | ^ { 2 }$ is positive for $t = t _ { 0 }$ ,then the solution is positive and

$$
\varlimsup _ {  \infty } \frac { 1 } { t } \log [ | x _ { 1 } | ^ { 2 } - \sum _ { s = 2 } ^ { n } | x _ { s } | ^ { 2 } ] \equiv \varlimsup _ { t  \infty } \frac { 2 } { t } \int _ { 0 } ^ { t } [ \Re ( f _ { 1 1 } ( \tau ) ) - ( n - 1 ) Q ( \tau ) ]
$$

or

$$
\varlimsup _ { t \to \infty } \frac { 1 } { t } \log \sum _ { s = 1 } ^ { n } | x _ { s } | ^ { 2 } \equiv \varlimsup _ { t \to \infty } \frac { 2 } { t } \int _ { 0 } ^ { t } \left[ \Re ( f _ { 1 1 } ( \tau ) ) - ( n - 1 ) Q ( \tau ) \right] d \tau .
$$

Theorem 7:If the coefficients of (160) satisfy

$$
\begin{array} { c c } { \underset { t  \infty } { \operatorname* { l i m } } f _ { s i } ( t ) = 0 } & { ( s \neq i ) , } \\ { \ncong \mathrm { ~ } } & { } \\ { \Re [ f _ { s - 1 , s - 1 } ( i ) - f _ { s s } ( t ) ] \geq c > 0 } & { ( t \geq t _ { 0 } ; s = 2 , \dots , n ) , } \end{array}
$$

and if we put

$$
\operatorname* { l i m } _ { t \to \infty } \frac { 1 } { t } \int _ { 0 } ^ { t } \Re ( f _ { s s } ( \tau ) ) d \tau = \gamma _ { s } \qquad ( s = 1 , \ldots , n ) ,
$$

then the order numbers are $\gamma _ { 1 } , \ldots , \gamma _ { n }$

# 16.16PERRON'S GENERALIZATION

Perron (1930b) generalized the discussion of stability to the differential system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } f _ { s i } ( t ) x _ { i } + \phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) \quad ( s = 1 , \ldots , n ) ,
$$

where the $f _ { s i } ( t )$ are arbitrary continuous and bounded functions of $t$ The question is whether the results obtained for the system in which $\begin{array} { r } { f _ { s i } ( t ) = a _ { s i } = } \end{array}$ constant $( s , i = 1 , 2 , \ldots , n )$ can be transferred to the more general system (161). Perron's answer was in the negative. Perron added as the hypothesis that the system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } f _ { s i } ( t ) x _ { i } + \psi _ { s } ( t ) ( s = 1 , 2 , . . . , n )
$$

admits always at least one bounded solution for arbitrary continuous bounded functions $\psi _ { s } ( t )$ . Whether (16la) admits always a bounded solution is known from the behavior of the homogeneous system (161) with $\phi _ { s } \equiv 0$ (Section 16.14).

The negative answer comes from the example

$$
\frac { d x _ { 1 } } { d t } = - a x _ { 1 } , \frac { d x _ { 2 } } { d t } = ( \sin \log t + \cos \log t - 2 a ) x _ { 2 } ,
$$

which admits general integrals

$$
x _ { 1 } = C _ { 1 } e ^ { - a t } , \qquad x _ { 2 } = C _ { 2 } \exp { \{ ( \sin \log t - 2 a ) t \} } .
$$

If $2 a < 1$ , then the single-parameter solution with $C _ { 2 } = 0$ has only the property that

$$
\operatorname* { l i m } _ { t \to \infty } \left( | x _ { 1 } | + | x _ { 2 } | \right) = 0 , \operatorname* { l i m } _ { t \to \infty } \frac { | x _ { 1 } | + | x _ { 2 } | } { e ^ { - c t } } = 0
$$

for $c < a$ If $2 a > 1$ ，then these limit relations hold only if $c < \operatorname* { m i n } { ( a , 2 a - 1 ) }$

The perturbed system

$$
\frac { d x _ { 1 } } { d t } = - a x _ { 1 } , \frac { d x _ { 2 } } { d t } = ( \sin \log t + \cos \log t - 2 a ) x _ { 2 } + x _ { 1 } ^ { 2 }
$$

admits solutions $x _ { 2 }$ which converge to zero for $t \to \infty$ when $2 a < 1$ There is no solution satisfying the above limit relations.When $2 a > 1$ the solutions $x _ { 2 }$ tend to zero for $t \to \infty$ only when $C _ { 1 } = 0$

First, Perron discussed the stability character of a special system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) x _ { i } + \omega _ { s } ( t ) \qquad ( s = 1 , \ldots , n ) ,
$$

where the $g _ { s i } ( t )$ are equal to zero for $s \geq i$ ，that is,the elements below the principal diagonal of the matrix formed by $g _ { s i } ( t )$ are zero.Thus the first $\pmb { s }$ equations contain only the first $\pmb { s }$ unknown variables $x _ { i }$ ·

Theorem $\boldsymbol { \mathit { 1 } }$ :For the case in which the $g _ { s i } ( t ) , 1 \leq i \leq s \leq n _ { \cdot }$ are continuous and bounded for $t \geq 0$ the necessary and sufficient condition,for the system (162) to admit at least one bounded solution for any choice of the continuous and bounded functions $\omega _ { s } ( t )$ , is that the functions $g _ { s i } ( t )$ should satisfy the conditions with

$$
\int _ { 0 } ^ { t } g _ { s s } ( \tau ) d \tau = G _ { s } ( t ) ,
$$

and that for any indices $s = 1 , 2 , \ldots , n$ ，either

(A)exp $\{ G _ { s } ( t ) \}$ and

$$
\exp \left\{ G _ { s } ( t ) \right\} \cdot \int _ { 0 } ^ { t } \left| \exp \left\{ - G _ { s } ( \tau ) \right\} \right| d \tau
$$

be both bounded, or

(B)exp $\{ G _ { s } ( t ) \}$ be unbounded but

$$
\exp \left\{ G _ { s } ( t ) \right\} \cdot \int _ { 0 } ^ { t } \left| \exp \left\{ - G _ { s } ( \tau ) \right\} \right| d \tau
$$

be existing and bounded.

Theorem 2: If the system (162) admits at least one bounded solution for any choice of the continuous bounded functions $\omega _ { s } ( t )$ ,i.e., if the conditions of Theorem 1 are satisfied, then for each bounded solution of the homogeneous system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) x _ { i } \qquad ( s = 1 , \ldots , n )
$$

the relation

$$
\operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } ^ { n } | x _ { i } ( t ) | = 0
$$

holds.

For the proof of these two theorems Perron referred to the Preparatory Theorem: If $G ( t )$ is continuous for $t \geq 0$ and if

$$
e ^ { G ( t ) } , \qquad e ^ { G ( t ) } \int _ { 0 } ^ { t } \left| e ^ { - G ( \tau ) } \right| d \tau
$$

are bounded, then

$$
\operatorname* { l i m } _ { t  \infty } e ^ { G ( t ) } = 0 .
$$

In fact, we have

$$
L _ { 2 } \geq | e ^ { G ( t ) } | \int _ { 0 } ^ { t } \frac { d \tau } { L _ { 1 } } = | e ^ { G ( t ) } | \frac { t } { L _ { 1 } } ,
$$

where

$$
L _ { 1 } \geq \vert e ^ { G ( t ) } \vert , \qquad L _ { 2 } \geq \vert e ^ { G ( t ) } \vert \int _ { 0 } ^ { t } \vert e ^ { - G ( \tau ) } \vert d \tau .
$$

Hence

$$
\begin{array} { r } { \left| e ^ { G ( t ) } \right| \leqq L _ { 1 } L _ { 2 } / t . } \end{array}
$$

Theorems 1 and 2 are proved by induction. It can be seen that the theorems are true for $n = 1$ . Suppose that the theorems are true for $n - 1$ . The nth equation of (162) is

$$
\frac { d x _ { n } } { d t } = g _ { n n } ( t ) x _ { n } + \sum _ { i = 1 } ^ { n - 1 } g _ { n i } ( t ) x _ { i } + \omega _ { n } ( t ) .
$$

We have

$$
\begin{array} { r l r } {  { x _ { n } = \exp { \{ G _ { n } ( t ) \} } \cdot \bigg ( c _ { n } + \int _ { 0 } ^ { t } [ \sum _ { i = 1 } ^ { n - 1 } g _ { n i } ( \tau ) x _ { i } ( \tau ) + \omega _ { n } ( \tau ) ] } } \\ & { } & { \times \exp { \{ - G _ { n } ( \tau ) \} } \cdot d \tau \bigg ) , } \end{array}
$$

$$
\begin{array} { r } { c _ { n } = x _ { n } ( 0 ) . } \end{array}
$$

If we put $\omega _ { 1 } ( t ) = \cdots = \omega _ { n - 1 } ( t ) = 0 \mathrm { , }$ ， then we get

$$
\operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } ^ { n - 1 } | x _ { i } ( t ) | = 0 .
$$

Choose $\omega _ { n } ( t )$ so that $\omega _ { n } ( t ) = \vert \exp \left\{ - G _ { n } ( t ) \right\} \vert / [ \exp \left\{ - G _ { n } ( t ) \right\} ]$ ; then the solution $x _ { n }$ is

$$
\begin{array} { r l r } & { } & { x _ { n } = \exp { \{ G _ { n } ( t ) \} } \cdot \Big ( c _ { n } + \displaystyle \int _ { 0 } ^ { t } [ 1 + H ( \tau ) ] | \exp { \{ - G _ { n } ( \tau ) \} } | d \tau \Big ) , } \\ & { } & { H ( t ) = \displaystyle \sum _ { i = 1 } ^ { n - 1 } g _ { n i } ( t ) x _ { i } ( t ) \frac { \exp { \{ - G _ { n } ( t ) \} } } { | \exp { \{ - G _ { n } ( t ) \} } | } . } \end{array}
$$

We see that

$$
\operatorname* { l i m } _ { t  \infty } H ( t ) = 0 .
$$

Hence for the existence of a bounded solution with bounded $e ^ { G ( t ) }$ the function

$$
\exp \left\{ { \cal G } _ { n } ( t ) \right\} \cdot \int _ { 0 } ^ { t } | \exp \left\{ - { \cal G } _ { n } ( \tau ) \right\} | d \tau
$$

should be bounded. If exp $\{ G _ { \pi } ( t ) \}$ is unbounded, then the solution $x _ { n }$ should be

$$
- \exp { \{ G _ { n } ( t ) \} } \cdot \int _ { \tau } ^ { \infty } | 1 + H ( \tau ) | \cdot | \exp { \{ - G _ { n } ( \tau ) \} } | d \tau
$$

for a definite choice of $c _ { n }$ . The boundedness and existence of this function are equivalent to those of

$$
\exp \left\{ G _ { n } ( t ) \right\} \cdot \int _ { t } ^ { \infty } | \exp \left\{ - G _ { n } ( \tau ) \right\} | d \tau .
$$

Thus the boundedness of this latter function is necessary. It is easily shown to be also sufficient if we refer to the preparatory theorem.

Theorem 3: If the conditions of Theorem 1 are satisfed, then in the general bounded solution of the system (162) the number of arbitrary constants is equal to the number of the indices $\pmb { s }$ for which the condition (A） is satisfied.The initial values $x _ { s } ( 0 ) = c _ { s }$ can be arbitrarily chosen so that their index s satisfies the condition (A).If the condition (A) is satisfed for all indices $\pmb { S }$ ，then all solutions are bounded. If the condition (B) is satisfied for all indices $s$ ，then there is only a single bounded solution.

Theorem 4: If,among the conditions of Theorem 1, the $k$ indices $\pmb { s }$ satisfy the condition (A） and the remaining $n - k$ indices $\pmb { s }$ satisfy the condition (B),then the linear homogeneous system (162） with $\omega _ { 1 } ( t ) = \cdots = \omega _ { n } ( t ) = 0$ admits just $k$ linearly independent bounded solutions $( k = 0 , 1 , \ldots , n )$ . When $k = 0$ there is no bounded solution except the trivial solution $x _ { s } ( t ) = 0$

Next consider the differential system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) x _ { i } + \chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) \qquad ( s = 1 , \ldots , n ) ,
$$

where the $\chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ are continuous and bounded in the domain: $t \geq 0 , x _ { j }$ arbitrary $( j = 1 , \ldots , n )$

Theorem 5: Let $g _ { s i } ( t ) \left( 1 \leq i \leq s \leq n \right)$ be continuous and bounded for $t \geq 0$ .The necessary and sufficient condition for the differential system (163) with any arbitrary functions $\chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ of the above nature to admit only bounded solutions is that the functions

$$
\exp { \{ G _ { s } ( t ) \} } \cdot \int _ { 0 } ^ { t } \left| \exp { \{ - G _ { s } ( \tau ) \} } \right| d \tau \qquad ( s = 1 , \ldots , n ) ,
$$

with

$$
G _ { s } ( t ) = \int _ { 0 } ^ { t } g _ { s s } ( \tau ) d \tau ,
$$

should be bounded.

If this condition is satisfied and if the ${ \pmb \chi } _ { \pmb s }$ satisfy further conditions

$$
| \chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) | \leq \gamma \sum _ { i = 1 } ^ { n } | x _ { i } | \qquad ( s = 1 , \ldots , n )
$$

in the domain $t \geq 0 , | x _ { j } | \leq a ( j = 1 , \ldots , n )$ ，where $\boldsymbol { \gamma }$ is a sufficiently small constant depending on $^ { a }$ and $g _ { s \ell } ( t )$ ，then for any interval in which the initial values $x _ { s } ( 0 )$ are sufficiently small in absolute values, we should have $| x _ { s } ( t ) | \leq a$ and

$$
\operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } ^ { n } | x _ { i } ( t ) | = 0 .
$$

Theorem 6: Let $g _ { s i } ( t ) \left( 1 \leq i \leq s \leq n \right)$ and $\chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ $( s =$ $1 , \ldots , n )$ be continuous in the domain $t \geq 0 , | x _ { \lambda } | \leq b \alpha ^ { n - \lambda } ( \lambda = 1 , 2 ,$ $\cdots , n )$ ，and suppose that

$$
| g _ { s i } ( t ) | \le K , \qquad | \exp \left\{ G _ { s } ( t ) \right\} | \le L _ { 1 } ,
$$

where, since $G _ { s } ( 0 ) = 0$ ,we have $L _ { 1 } \equiv 0$ ，and that

$$
| \exp \left\{ G _ { s } ( t ) \right\} | \cdot \int _ { 0 } ^ { t } | \exp \left\{ - G _ { s } ( \tau ) \right\} | d \tau \leq L _ { 2 } ,
$$

$$
| \chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) | \equiv { \frac { K b \alpha ^ { n } } { 1 - \alpha } } ,
$$

with

$$
\int _ { 0 } ^ { t } g _ { s s } ( \tau ) d \tau = G _ { s } ( t ) ,
$$

where $b , \alpha , K , L _ { 1 } , L _ { 2 }$ are positive constants such that

$$
\alpha < 1 , \qquad \frac { K L _ { 2 } \alpha } { 1 - \alpha } < 1 .
$$

If $\pmb { c }$ is a positive number such that

$$
\frac { c } { b } L _ { 1 } + \frac { K L _ { 2 } \alpha } { 1 - \alpha } = \vartheta < 1 ,
$$

namely, $c < \vartheta b < b$ because $L _ { 1 } \gtrapprox 0$ , then any solution of the differential system(163) with the initial values $x _ { s } ( 0 )$ ， such that

$$
| x _ { s } ( 0 ) | \equiv c \alpha ^ { n - s } \qquad ( s = 1 , \ldots , n ) ,
$$

continues to exist for $t \geq 0$ and satisfies

$$
| x _ { s } ( t ) | < b \alpha ^ { n - s } \qquad ( s = 1 , \ldots , n ) .
$$

If the functions ${ \tt X } \tt { s }$ satisfy the additional conditions

$$
| \chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) | \leq { \frac { 1 } { n } } { \frac { K } { 1 - \alpha } } \sum _ { i = 1 } ^ { n } \alpha ^ { i } | x _ { i } | \qquad ( s = 1 , \ldots , n ) ,
$$

.then we have further

$$
\operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } ^ { n } | x _ { i } ( t ) | = 0 .
$$

In fact, the system (163) is written

$$
\begin{array}{c} \frac { d x _ { s } } { d t } = g _ { s s } x _ { s } + \sum _ { i = 1 } ^ { s - 1 } g _ { s i } x _ { i } + \chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) \qquad \\ { ( s = 1 , \ldots , n ) , \qquad } \end{array}
$$

which admits the solution

$$
x _ { s } ( t ) = \exp { \{ G _ { s } ( t ) \} } \cdot \Big [ x _ { s } ( 0 ) + \int _ { 0 } ^ { t } \Phi _ { s } ( \tau ) \exp { \{ - G _ { s } ( \tau ) \} } \cdot d \tau ] ,
$$

$$
\Phi _ { s } ( \tau ) = \sum _ { i = 1 } ^ { s - 1 } g _ { s i } ( \tau ) x _ { i } ( \tau ) + \chi _ { s } ( \tau , x _ { 1 } ( \tau ) , \dots , x _ { n } ( \tau ) ) .
$$

By (167) and $c > b$ , the inequalities (168) hold at least for sufficiently small $\pmb { t } .$ ,and we have

$$
\begin{array} { r l } & { \bigg | \displaystyle \sum _ { i = 1 } ^ { s - 1 } a _ { s i } ( t ) x _ { i } ( t ) + \chi _ { s } ( t , x _ { 1 } ( t ) , \dots , x _ { n } ( t ) ) \bigg | } \\ & { \qquad \displaystyle \leq \sum _ { i = 1 } ^ { s - 1 } K b \alpha ^ { n - i } + \frac { K b \alpha ^ { n } } { 1 - \alpha } = \frac { K b \alpha } { 1 - \alpha } \alpha ^ { n - s } . } \end{array}
$$

From(171） we derive the estimate

$$
| x _ { s } ( t ) | \leq c \alpha ^ { n - s } L _ { 1 } + \frac { K b \alpha } { 1 - \alpha } \alpha ^ { n - s } L _ { 2 } = \vartheta b \alpha ^ { n - s } .
$$

Hence, as far as (168) is true, a sharper inequality

$$
| x _ { s } ( t ) | \leq \vartheta b \alpha ^ { n - s }
$$

holds.Accordingly,the solution ${ \boldsymbol { x } } _ { s } ( t )$ can be continued up to an arbitrarily large value of $t ,$ where $| x _ { s } ( t ) | \leq \vartheta b \alpha ^ { n - s }$ .Thus the first part of the theorem is established.

Let $\pmb { B }$ be defined by

$$
\operatorname* { l i m } _ { t \to \infty } | x _ { s } ( t ) | < B \alpha ^ { n - s } \qquad ( s = 1 , 2 , \ldots , n ) .
$$

If the $\pmb { \chi } _ { s }$ satisfy (169), then $| x _ { s } ( t ) | < B \alpha ^ { n - s } ( s = 1 , \ldots , n )$ and

$$
| \chi _ { s } ( t , x _ { 1 } , . . . , x _ { n } ) | < { \frac { 1 } { n } } { \frac { K } { 1 - \alpha } } \sum _ { i = 1 } ^ { n } \alpha ^ { i } B \alpha ^ { n - s } = { \frac { K B \alpha ^ { n } } { 1 - \alpha } }
$$

for $t \geq t _ { 0 }$ . In (171) we divide the integral between O and $\pmb { t }$ into two integrals,between O and $t _ { 0 }$ and between $t _ { 0 }$ and $\pmb { t }$ .The first integral is a constant $\ b { A } _ { s }$ . The second integral can be estimated by (172） and (173).From (171) we obtain

$$
| x _ { s } ( t ) | \leq | \exp \{ G _ { s } ( t ) \} | { \cdot } | x _ { s } ( 0 ) + A _ { s } | + \frac { K L _ { 2 } \alpha } { 1 - \alpha } B \alpha ^ { n - s } .
$$

By the preparatory theorem and the hypothesis of Theorem 6, we have

$$
\operatorname* { l i m } _ { t \to \infty } \left[ \exp \left\{ G _ { s } ( t ) \right\} \right] = 0 .
$$

From the foregoing inequality and (172) we obtain

$$
\operatorname* { l i m } _ { t \to \infty } | x _ { s } ( t ) | \leq { \frac { K L _ { 2 } \alpha } { 1 - \alpha } } B \alpha ^ { n - s } < \vartheta B \alpha ^ { n - s } .
$$

Repeating this process, we find the inequality

$$
\operatorname* { l i m } _ { t \to \infty } | x _ { s } ( t ) | < \vartheta ^ { k } B \alpha ^ { n - s }
$$

for an arbitrarily large $k$ . Thus we conclude that $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } x _ { s } ( t ) = 0 } \end{array}$

Theorem 7: In the differential system (163) let the functions $\chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ $( s = 1 , \ldots , n )$ be continuous in the domain $t \geq 0$ ， $| x _ { \lambda } | \equiv b \alpha ^ { n - 1 } \left( \lambda = 1 , 2 , \ldots , n \right)$ and satisfy

$$
| g _ { s i } ( t ) | \leq K , \qquad | \chi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) | \leq { \frac { K b \alpha ^ { n } } { 1 - \alpha } } ,
$$

$$
| \chi _ { s } ( t , x _ { 1 } , \dots , x _ { n } ) - \chi _ { s } ( t , x _ { 1 } ^ { * } , \dots , x _ { n } ^ { * } ) | \leq \frac { 1 } { n } \frac { K } { 1 - \alpha } \sum _ { i = 1 } ^ { n } \alpha ^ { i } | x _ { i } - x _ { i } ^ { * }
$$

Furthermore,suppose that for each single index $\nu$ we have either

$$
\begin{array} { l } { | \exp \left\{ G _ { s } ( t ) \right\} | \leq L _ { 1 } , } \\ { | \exp \left\{ G _ { s } ( t ) \right\} | \cdot { \displaystyle \int _ { 0 } ^ { t } } | \exp \left\{ - G _ { s } ( \tau ) \right\} | d \tau \leq L _ { 2 } ; } \end{array}
$$

or

$| \exp \left\{ G _ { s } ( t ) \right\} |$ unbounded,

$$
| \exp \left\{ G _ { s } ( t ) \right\} | \cdot \int _ { t } ^ { \infty } | \exp \left\{ - G _ { s } ( \tau ) \right\} | d \tau \leq L _ { 2 } .
$$

Denote an index of the first kind by $s _ { A }$ , and one of the second kind by $s _ { B }$ .Let $b , \alpha , K , L _ { 1 } , L _ { 2 }$ be positive constants such that

$$
\alpha < 1 , \qquad \frac { K L _ { 2 } \alpha } { 1 - \alpha } < 1 .
$$

Let $^ c$ be a positive number $c \leq b$ ， such that,if there exists at least one index $s _ { A }$ among the indices $\pmb { s }$ ,we have

$$
\frac { c } { b } L _ { 1 } + \frac { K L _ { 2 } \alpha } { 1 - \alpha } \cong 1 ;
$$

then the given differential system (163） admits at least a bounded solution，and indeed,if an arbitrary $x _ { s } ( 0 ) = c _ { s }$ is given for each $s = s _ { A }$ in the domain $\vert c _ { s } \vert \le c \alpha ^ { n - s }$ ， there exists just one solution that continues to be bounded $| x _ { s } ( t ) | \leq b \alpha ^ { n - s }$ for all $\pmb { s }$

If for all $s$ we have further $\gamma _ { s } ( t , 0 , \ldots , 0 ) = 0$ ,then there still holds for the solution the relation

$$
\operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } ^ { n } | x _ { i } ( t ) | = 0 .
$$

After all these preparations we show that the original general system (161) can be reduced to this specialized system (163).

Theorem 8: Let the functions $f _ { s i } ( t ) \left( s , i = 1 , \ldots , n \right)$ be continuous and bounded for $t \geq 0$ . Then the necessary and sufficient condition for the differential system (161)

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } f _ { s i } ( t ) x _ { i } + \phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) \qquad ( s = 1 , \ldots , n ) ,
$$

for any arbitrary choice of the functions $\phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ that are continuous and bounded in the domain $t \geq 0$ ， $x _ { \lambda }$ arbitrary $( \lambda = 1 , \ldots , n )$ to admit only bounded solutions is that the linear system (161a)

$$
{ \frac { d x _ { s } } { d t } } = \sum _ { i = 1 } ^ { n } f _ { s i } ( t ) x _ { i } + \psi _ { s } ( t ) \qquad ( s = 1 , \ldots , n )
$$

should always admit only bounded solutions for arbitrary continuous bounded $\psi _ { s } ( t )$

If this condition is satisfied and if $\phi _ { s }$ in the domain $t \geq 0 , | x _ { \lambda } | \leq a$ $( \lambda = 1 , \ldots , n )$ satisfies additional conditions

$$
| \phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) | \leq \gamma \sum _ { i = 1 } ^ { n } | x _ { i } | \qquad ( s = 1 , \ldots , n ) ,
$$

where $\boldsymbol { \gamma }$ is a sufficiently small constant depending only on $^ { a }$ and $f _ { s i } ( t )$ ， then each solution whose initial values $x _ { s } ( 0 )$ are sufficiently small in absolute values satisfies

$$
| x _ { s } ( t ) | \leq a \qquad ( s = 1 , \ldots , n ) , \qquad \operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } ^ { n } | x _ { i } ( t ) | = 0 .
$$

Before entering on the proof of Theorem 8 we present three auxiliary theorems.

Auxiliary Theorem $\boldsymbol { \mathit { 1 } }$ :A bounded matrix $F$ can be transformed by a bounded matrix $P$ with bounded reciprocal $P ^ { - 1 }$ and bounded derivative $\dot { P }$ to a bounded matrix

$$
( P F + \dot { P } ) P ^ { - 1 } = G ,
$$

which is of reduced triangular form, i.e.,whose $( \lambda , \mu ) { \mathrm { t h } }$ element is zero for $\lambda < \mu$ ,i.e.，whose elements below the principal diagonal are zero (Perron,1930a ；Gantmacher and Krein,1960).

Auxiliary Theorem 2: The matrix $\pmb { P }$ in Auxiliary Theorem 1 can be chosen so that the diagonal elements $g _ { \lambda \lambda }$ of the reduced matrix $G$ are real. If the elements of the given matrix $F$ are all real,then we can arrange matters so that all elements of $\pmb { P }$ and consequently all elements of $G$ are real.

In fact, $G$ is equal to $( P F + { \dot { P } } ) P ^ { - 1 }$ ； accordingly, $G = \dot { Q } Q ^ { - 1 }$ . The matrix $\boldsymbol { Q }$ is of reduced form and its diagonal elements $q _ { \lambda \lambda }$ are real. Hence $g _ { \lambda \lambda } = \dot { q } _ { \lambda \lambda } / q _ { \lambda \lambda }$ are real. Also, if the $f _ { \mu \nu }$ are all real, then the $p _ { \lambda \nu }$ ， by definition,are real.

Auxiliary Theorem 3: For any matrix $G$ satisfying all the requirements of Auxiliary Theorem 1, the real part of the integral

$$
\int _ { 0 } ^ { t } \left[ \sum _ { \nu = 1 } ^ { n } g _ { \nu \nu } ( \tau ) - \sum _ { \nu = 1 } ^ { n } f _ { \nu \nu } ( \tau ) \right] d \tau
$$

is bounded.

Now let us return to the proof of Theorem 8.

Denote by $\pmb { F }$ the matrix formed of $f _ { i , j } ( t )$ ；then there is a bounded matrix $\pmb { P }$ formed of $p _ { i j } ( t )$ such that the bounded reciprocal $P ^ { - 1 }$ and the bounded derivative $\dot { P }$ are such that the bounded matrix $( P F + { \dot { P } } ) Q$ $= G$ ，whose elements $g _ { i j } ( t )$ are zero for $i > j _ { : }$ ，is of the reduced triangular form (Section 16.17).

If we introduce new variables $y _ { 1 } , \ldots , y _ { n }$ by

$$
\begin{array} { l l } { { y _ { s } = \displaystyle \sum _ { i = 1 } ^ { n } p _ { s i } ( t ) x _ { i } ~ } } & { { ~ ( s = 1 , \ldots , n ) , } } \\ { { { } } } & { { { } } } \\ { { x _ { s } = \displaystyle \sum _ { i = 1 } ^ { n } q _ { s i } ( t ) y _ { i } ~ } } & { { ~ ( s = 1 , \ldots , n ) , } } \end{array}
$$

then the differential system (I) is transformed to

$$
\frac { d y _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) y _ { i } + \chi _ { s } ( t , y _ { 1 } , . . . , y _ { n } ) ,
$$

where

$$
\begin{array} { l } { \displaystyle _ { \langle s } ( t , y _ { 1 } , \dots , y _ { n } ) = \sum _ { i = 1 } ^ { n } p _ { s i } ( t ) \phi _ { i } ( t , x _ { 1 } , \dots , x _ { n } ) , } \\ { \displaystyle _ { \langle s } ( t , y _ { 1 } , \dots , y _ { n } ) = \sum _ { i = 1 } ^ { n } q _ { s i } ( t ) \chi _ { i } ( t , y _ { 1 } , \dots , y _ { n } ) \qquad ( s = 1 , \dots , n ) } \end{array}
$$

Similarly (II) is transformed to

$$
\frac { d y _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) y _ { i } + \omega _ { s } ( t ) \qquad ( s = 1 , \ldots , n ) ,
$$

where

$$
\begin{array} { l l } { \omega _ { s } ( t ) = \displaystyle \sum _ { i = 1 } ^ { n } p _ { s i } ( t ) \psi _ { i } ( t ) , } \\ { \psi _ { s } ( t ) = \displaystyle \sum _ { i = 1 } ^ { n } q _ { s i } ( t ) \omega _ { i } ( t ) \quad } & { ( s = 1 , \ldots , n ) . } \end{array}
$$

The requirement that (I) admits only bounded solutions for arbitrary continuous and bounded $\phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ is equivalent to the requirement that (Ia) admits only bounded solutions for arbitrary continuous and bounded $\chi _ { s } ( t , y _ { 1 } , \ldots , y _ { n } )$ . The latter requirement is fulfilled if and only if

$$
\exp { \{ G _ { s } ( t ) \} } \cdot \int _ { 0 } ^ { t } \vert \exp { \{ - G _ { s } ( \tau ) \} } \vert d \tau \qquad ( s = 1 , \ldots , n ) ,
$$

where

$$
G _ { s } ( t ) = \int _ { 0 } ^ { t } g _ { s s } ( \tau ) d \tau ,
$$

are bounded by Theorem 5.By Theorem 3, this is the necessary and sufficient condition for the linearized system (Ia) to admit only bounded solutions for any arbitrary continuous and bounded $\omega _ { s } ( t )$ Hence it is equivalent to the condition that the system (II) admits only bounded solutions for any arbitrary continuous and bounded $\psi _ { s } ( t )$

Theorem 9: Let the functions ${ { f } _ { s i } } ( t ) ( s , i = 1 , \ldots , n )$ and $\phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ $( s = 1 , \ldots , n )$ be continuous and bounded in the domain $t \geq 0 , | x _ { \lambda } | \leq a \left( \lambda = 1 , \ldots , n \right)$ . In particular, let $\mathbf { \ } f _ { s i } ( t )$ be such that the linear homogeneous system (II) admits always at least a bounded solution for any arbitrary continuous and bounded functions $\psi _ { s } ( t )$ and that the homogeneous system

$$
\frac { d x _ { s } } { d t } = \sum _ { i = 1 } ^ { n } f _ { s i } ( t ) x _ { i } \qquad ( s = 1 , \ldots , n )
$$

admits just $k \left( k \geq 0 , k \leq n \right)$ linearly independent bounded solutions. If the functions $\phi _ { s }$ in this case satisfy

$$
| \phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) | \equiv \gamma _ { 1 } \qquad ( s = 1 , \ldots , n ) ,
$$

$$
| \phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) - \phi _ { s } ( t , x _ { 1 } ^ { * } , \ldots , x _ { n } ^ { * } ) | \leq { \gamma } _ { 2 } \sum _ { i = 1 } ^ { n } | x _ { i } - x _ { i } ^ { * } |
$$

where $\gamma _ { 1 } , \gamma _ { 2 }$ are sufficiently small positive constants dependings only on $\pmb { a }$ and $ { f _ { s i } } ( t )$ ，then solutions of (I) for which $| x _ { s } ( t ) | \leq a$ continue to hold form a family of just $k$ arbitrary constants,and indeed the $k$ linearly independent combinations of the initial values

$$
\sum _ { i = 1 } ^ { n } A _ { \varepsilon i } x _ { i } ( 0 ) = \alpha _ { \varepsilon } \qquad ( \kappa = 1 , \ldots , k )
$$

can be arbitrarily chosen in a sufficiently small domain $| \alpha _ { \varepsilon } | \leq c _ { \varepsilon } .$ so that the solution is uniquely determined.

In addition to this,if $\phi _ { s } ( t , 0 , \ldots , 0 ) = 0$ for all $\pmb { s }$ ， then we have for these solutions

$$
\operatorname* { l i m } _ { t \to \infty } \sum _ { i = 1 } | x _ { i } ( t ) | = 0 .
$$

Proof: By the linear substitution (174) the differential systems (I), (II), (III) are transformed respectively to

$$
\frac { d y _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) y _ { i } + \chi _ { s } ( t , y _ { 1 } , . . . , y _ { n } ) ,
$$

$$
\frac { d y _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) y _ { i } + \omega _ { s } ( t ) ,
$$

$$
\frac { d y _ { s } } { d t } = \sum _ { i = 1 } ^ { s } g _ { s i } ( t ) y _ { i } \qquad ( s = 1 , \ldots , n ) ,
$$

where $\chi _ { s } , \omega _ { s }$ are given in the proof of Theorem 8. The hypothesis in Theorem 9 is equivalent to the requirement that (IIa) admit only bounded solutions for any arbitrary bounded $\omega _ { s } ( t )$ or to the requirement that (IIIa) admit just $k$ linearly independent bounded solutions. By Theorem 4 we have

$$
\begin{array} { r l } & { \exp \left\{ G _ { s } ( t ) \right\} \qquad \mathrm { b o u n d e d , } } \\ & { \exp \left\{ G _ { s } ( t ) \right\} \cdot \displaystyle \int _ { 0 } ^ { t } | \exp \left\{ - G _ { s } ( \tau ) \right\} | d \tau \qquad \mathrm { t } } \end{array}
$$

for just $k$ indices $\pmb { s }$ ; and

$$
\begin{array} { l } { { \displaystyle \exp \left\{ G _ { s } ( t ) \right\} \qquad \mathrm { u n b o u n d e d } , } } \\ { { \displaystyle \exp \left\{ G _ { s } ( t ) \right\} \cdot \int _ { t } ^ { \infty } \left| \exp \left\{ - G _ { s } ( \tau ) \right\} \right| d \tau } } \end{array}
$$

for the remaining $n - k$ indices $\pmb { s }$ .By the substitution (174） the domain $( \mathbf { D } ^ { \prime } ) \colon | x _ { \lambda } | \leq a ( \lambda = 1 , \ldots , n )$ is transformed to a domain (D) for $y _ { \lambda }$ which vary with $\pmb { t } .$ If $_ { \alpha }$ lies between O and 1,then the domain (D) contains a domain $( \mathbf { D } _ { 1 } ) \colon | y _ { \boldsymbol { \imath } } | \le b _ { 0 } \alpha ^ { n - \lambda } \left( \lambda = 1 , \ldots , n \right)$ as a subdomain.On the other hand, the domain $\mathbf { \eta } ^ { ( \mathbf { D } ) }$ is contained in a domain $( \mathrm { D } _ { 2 } ) \colon | y _ { \lambda } | \le b _ { 1 } \alpha ^ { n - \lambda } \left( \lambda = 1 , \ldots , n \right)$ ，which is independent of $t _ { i }$ ，where we choose $\alpha$ in order to apply Theorem 7 so that

$$
\alpha < 1 , \qquad \frac { K L _ { 2 } \alpha } { 1 - \alpha } < 1 ,
$$

where $K , L _ { 2 }$ are the upper bounds, depending only on $g _ { s i } ( t )$ and finally on $f _ { s i } ( t )$ . Hence $f _ { s i } ( t )$ is conditioned only by the choice of $\alpha$ . The constants $b _ { 0 } , b _ { 1 } , b _ { 0 } \cong b _ { 1 }$ in the above inequalities depend only on $\pmb { a }$ and $f _ { s i } ( t )$ . The functions ${ \pmb \chi } _ { \pmb s }$ are given as continuous at first only in the domain $\mathbf { \eta } ^ { ( \mathbf { D } ) }$ . In order to continue analytically the given functions $\phi _ { s }$ to the domain $\left( \mathbf { D } _ { 2 } \right)$ beyond the boundary of the domain $\mathbf { ( D ^ { \prime } ) }$ ，we refer to

$$
\phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } ) = \phi _ { s } ( t , \vartheta _ { 1 } x _ { 1 } , \ldots , \vartheta _ { n } x _ { n } ) ,
$$

$$
\vartheta _ { i } = \left\{ { \begin{array} { l l } { 1 \qquad { \mathrm { f o r } } \qquad | x _ { i } | \leq a , } \\ { a / | x _ { i } | \qquad { \mathrm { f o r } } \qquad | x _ { i } | > a . } \end{array} } \right.
$$

It can be seen that the functions $\phi _ { s }$ thus continued analytically are everywhere continuous.The inequalities (175),which hold for the first domain $( \mathbf { D ^ { \prime } } )$ ，are true also for the domain $( \mathbf { D } _ { 2 } )$ . The functions $\phi _ { s } ( t , x _ { 1 } , \ldots , x _ { n } )$ and $\chi _ { s } ( t , y _ { 1 } , \ldots , y _ { n } )$ are continuous in the domain $( \mathbf { D } _ { 2 } )$ . In the domain $\mathbf { \eta } ^ { ( \mathbf { D } ) }$ these functions coincide with the original ${ \pmb \chi } _ { s }$ If $\gamma _ { 1 } , \gamma _ { 2 }$ are chosen sufficiently small, then we have

$$
| \chi _ { s } ( t , y _ { 1 } , . . . , y _ { n } ) | \equiv \frac { K b _ { 0 } \alpha ^ { n } } { 1 - \alpha } ,
$$

$$
| \chi _ { s } ( t , y _ { 1 } , \dots , y _ { n } ) - \chi _ { s } ( t , y _ { 1 } ^ { * } , \dots , y _ { n } ^ { * } ) | \leq { \frac { 1 } { n } } { \frac { K } { 1 - \alpha } } \sum _ { i = 1 } ^ { n } \alpha ^ { i } | y _ { i } - y _ { } |
$$

Thus Theorem 7 can be applied to (Ia) either in the domain $\left( \mathbf { D } _ { 2 } \right)$ or in the domain $\mathbf { ( D _ { 1 } ) }$ . When $y _ { s } ( 0 )$ are given arbitrarily for $k$ indices $s = s _ { A }$ in a sufficiently small domain $| y _ { s } ( 0 ) | \le c \alpha ^ { n - s }$ ，where $^ c$ is sufficiently small, then the system (Ia) admits just one solution $y _ { s }$ ， which remains as $| y _ { s } ( t ) | \leq b _ { 0 } \alpha ^ { n - s }$ ，where the initial condition $y _ { s } ( 0 ) =$ $\scriptstyle \sum _ { i = 1 } ^ { n } p _ { s i } ( 0 ) x _ { i } ( 0 )$ can be arbitrarily given for $k$ indices $s = s _ { A }$ in the domain

$$
\left| \sum _ { i = 1 } ^ { n } p _ { s i } ( 0 ) x _ { i } ( 0 ) \right| \leq c \alpha ^ { n - s } .
$$

Thus Theorem 9 is established except for the part，which follows immediately from the last part of Theorem 7.

Lettenmeyer (1929) studied the asymptotic behavior of the solution for $t \to + \infty$ of the system of differential equations

$$
\frac { d x _ { i } } { d t } = f ( t ) \cdot \sum _ { k = 1 } ^ { n } a _ { i k } x _ { k } + \phi _ { i } ( x _ { 1 } , \ldots , x _ { n } , t ) \qquad ( i = 1 , 2 , \ldots , n ) ,
$$

where the $a _ { i k }$ are constants not all zero, $f ( t )$ is defined and real in a certain domain $\mathfrak { B }$ of $x _ { i }$ and for all $t \geq t _ { 0 }$ ，such that $f ( t ) \geq 0$ for all $t \geq t _ { 0 }$ and that $F ( t ) = \int f ( t ) d t \to \infty$ as $t \to + \infty$ , and where the $\phi _ { i }$ satisfy

$$
| \phi _ { i } | \leq \varepsilon f ( t ) \cdot \sum _ { k = 1 } ^ { n } | x _ { k } |
$$

for all $t \geq T _ { \varepsilon }$ and for all $x _ { i }$ in the partial domain $\mathfrak { B } _ { \mathfrak { e } } \subset \mathfrak { B }$ By a matrix transformation the system is reduced to

$$
\frac { d y _ { i } } { d t } = \rho _ { i } f y _ { i } + \sum _ { k = 1 ( k \neq i ) } ^ { n } c _ { i k } f y _ { k } + \psi _ { i } ( y _ { 1 } , . . . , y _ { n } , t ) \qquad ( i = 1 , 2 , . .
$$

$$
\psi _ { i } = \sum _ { k } b _ { i k } ^ { \prime } \phi _ { k } ,
$$

where $| \psi _ { i } | \leq \varepsilon f \cdot \sum _ { k } | y _ { k } |$ for all $t \geq T _ { \varepsilon }$ and for all systems $( y _ { k } )$ of the transformed domain $\mathfrak { B } _ { \epsilon } ^ { * }$ of $\mathfrak { B } _ { \mathfrak { s } }$ ，and where the $\rho _ { i } ( i = 1 , \ldots , n )$ are the characteristic roots of $( a _ { i k } )$ . The matrix $( a _ { i j } )$ is transformed to the canonical form

$$
( b _ { i k } ) ^ { - 1 } ( a _ { i k } ^ { \prime } ) ( b _ { i k } ) = \left[ \begin{array} { l l l } { \rho _ { 1 } } & { } & { } \\ { } & { \rho _ { 2 } } & { c _ { i j } } \\ { } & { \cdot } & { } \\ { 0 } & { } & { \rho _ { n } } \end{array} \right] ,
$$

where $( a _ { i k } ^ { \prime } )$ is obtained by the simultaneous exchange of two columns and two rows from $( a _ { i k } )$ ，and $( b _ { i k } ^ { \prime } ) = ( b _ { i k } ) ^ { - 1 }$

Lettenmeyer, after the fashion of Perron, proved the existence of

$$
\operatorname* { l i m } _ { t \to \infty } { \left[ { \log \sum _ { i = 1 } ^ { n } | x _ { i } | } { \Big / } { \int f ( t ) d t } \right] } ,
$$

which are equal to $\Re ( \rho _ { \nu } ) , 1 \le \nu \le n$ ，The solution $( x _ { i } )$ is then said to belong to the characteristic roots with equal real parts $\Re ( \rho _ { * } )$ .If $\pmb { p }$ of the characteristic roots have real parts $\Re ( \rho _ { \nu } )$ ， then there exists also the limit

$$
\operatorname* { l i m } _ { t \to \infty } \left[ \log \sum _ { i = m + 1 } ^ { m + p } | x _ { i } | \bigg / \int f ( t ) d t \right] = \Re ( \rho _ { \nu } ) .
$$

Let $\Re ( \rho _ { 1 } ) \geq \Re ( \rho _ { 2 } ) \geq \cdot \cdot \cdot \geq \Re ( \rho _ { m } )$ ,and $\rho _ { m + 1 } , \ldots , \rho _ { m + p }$ be the characteristic roots with equal real parts $\rho _ { m + 1 }$ .If the original system is transformed to the second form so that the $\displaystyle { \big | c _ { i k } \big | }$ are sufficiently small, then we have,for the solutions belonging to this group of characteristic roots,

$$
\operatorname * { l i m } _ { t \to \infty } \left[ y _ { j } ^ { 2 } \Bigg / \sum _ { i = m + 1 } ^ { m + p } | y _ { i } | ^ { 2 } \right] = 0 , \operatorname * { l i m } _ { t \to \infty } \left[ y _ { j } \Bigg / \sum _ { i = m + 1 } ^ { m + p } | y _ { i } | \right] = 0
$$

for all $j$ excluding $m + 1 \leq j \leq m + p$

If the characteristic root $\rho _ { \nu }$ has its real part different from that of any other characteristic root, then the components $x _ { i }$ are divided into two groups $x _ { \alpha }$ and $x _ { \beta }$ ,in which at least one $x _ { i }$ belongs to the group $x _ { \alpha }$ but the group $x _ { \beta }$ may be dropped. The grouping can be found from the solutions $e _ { 1 } , e _ { 2 } , \ldots , e _ { n } \neq 0 , 0 , \ldots , 0$ of the linear equations of rank $n - 1$ ：

$$
\begin{array} { r l } & { ( a _ { 1 1 } - \rho _ { \circ } ) e _ { 1 } + a _ { 1 2 } e _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } e _ { n } = 0 , } \\ & { a _ { 2 1 } e _ { 1 } + ( a _ { 2 2 } - \rho _ { \circ } ) e _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } e _ { n } = 0 , } \\ & { \cdot \cdot \cdot } \\ & { a _ { n 1 } e _ { 1 } + a _ { n 2 } e _ { 2 } + \cdot \cdot \cdot + ( a _ { n n } - \rho _ { \circ } ) e _ { n } = 0 , } \end{array}
$$

in which those with the index $i$ such that $e _ { i } \neq 0$ belong to $x _ { \alpha }$ and the remaining ones to $x _ { _ { \beta } }$ . The values $e _ { i }$ and the grouping are the same for all solutions belonging to $\rho _ { \nu }$ and independent of $\phi _ { t }$

Consider the system

$$
\frac { d ^ { n } x } { d t ^ { n } } + [ a _ { 1 } f ( t ) + \chi _ { 1 } ( t ) ] \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } + [ a _ { 2 } f ( t ) + \chi _ { 2 } ( t ) ] \frac { d ^ { n - 2 } x } { d t ^ { n - 2 } } + \cdot \cdot \cdot
$$

where $f ( t )$ is defined for $t \geq t _ { 0 }$ and $f ( t )  + \infty$ as $t \to + \infty$ ， such that the function $F ( t ) = \int f ( t ) d t$ exists, and where the $\chi _ { \nu } ( t ) \ ( \nu = 1 , 2 , \ldots , n )$ are defined for $t \geq t _ { 0 }$ and $\chi _ { \nu } ( t ) / f ( t ) = 0$ as $t \to + \infty$ ，and $\Re ( a _ { 1 } ) \neq 0$ Such a system is said to be of the first type.If the solution exists for $t \geq t _ { 0 }$ and does not vanish identically from a certain point on，then there exists the limit

$$
\operatorname* { l i m } _ { t \to \infty } \left\{ \left[ \log \left( | x | + \left| { \frac { d x } { d t } } \right| + \cdots + \left| { \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } } \right) \right] \right/ \left( \int f ( t ) d t \right) \right\}
$$

For the solution belonging to $- \pmb { a } _ { 1 }$ the derivative $d ^ { n - 1 } x / d t ^ { n - 1 }$ does not vanish for any $t$ and

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { t \to \infty } \Big \{ \Big [ \log \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } \Big ] \bigg / \bigg ( \int f ( t ) d t \bigg ) \Big \} = - a _ { 1 } , } \\ { \displaystyle \operatorname* { l i m } _ { t \to \infty } \Big [ \frac { d ^ { j } x } { d t ^ { j } } \Big / \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } \Big ] = 0 \qquad ( j = 0 , 1 , \ldots , n - 2 ) . } \end{array}
$$

The system

$$
\frac { d ^ { n } x } { d t ^ { n } } + [ a _ { 1 } + \chi _ { 1 } ( t ) ] \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } + \cdot \cdot \cdot + [ a _ { n } + \chi _ { n } ( t ) ] x = 0 ,
$$

where the ${ \chi _ { \nu } ( t ) }$ are defined for $t \geq t _ { 0 }$ ， $x _ { 0 } ( t )  0$ as $t  + \infty \ ( \nu = 1 ,$ $2 , \ldots , n )$ , is said to be of the second type, which has been studied by Poincaré and Perron. For any solution that exists for $t \geq t _ { 0 }$ and does not vanish identically from a certain point on there exists

$$
\operatorname* { l i m } _ { t \to \infty } \left\{ \left[ \log \Big ( | x | + \Big | \frac { d x } { d t } \Big | + \cdot \cdot \cdot + \Big | \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } \Big | \Big ) \right] \Big / { t } \right\} = \Re ( \rho _ { \ast } )
$$

$$
( 1 \leq \nu \leq n ) .
$$

If a solution belongs to a characteristic root $\rho _ { \nu }$ whose real part is not equal to that of any other characteristic root, then $x$ does not vanish and

$$
\operatorname* { l i m } _ { t \to \infty } \left[ { \frac { \log x } { t } } \right] = \rho _ { \nu } , \qquad \operatorname* { l i m } _ { t \to \infty } \left[ { \frac { d ^ { j } x / d t ^ { j } } { x } } \right] = \rho _ { \nu } ^ { j } \qquad ( j = 1 , \ldots , n ) .
$$

$\rho _ { \nu } \neq 0$ ，then $d x / d t , . . . , d ^ { n - 1 } x / d t ^ { n - 1 }$ are different from zero, and

$$
\operatorname* { l i m } _ { t \to \infty } \left\{ { \frac { \log \left( { \cal d } ^ { j } x / { \cal d } t ^ { j } \right) } { t } } \right\} = \rho _ { \nu } ( j = 1 , \cdot \cdot . . , n ) .
$$

For any solution belonging to the characteristic root $\rho _ { \nu }$ ，whose real part is equal to the real part of just $p$ characteristic roots, we have

$$
\operatorname* { l i m } _ { t \to \infty } \left\{ \left[ \log \left( | x | + \left| { \frac { d x } { d t } } \right| + \cdot \cdot \cdot + \left| { \frac { d ^ { p - 1 } x } { d t ^ { p - 1 } } } \right| \right) \right] \Big / t \right\} = \Re ( \rho _ { \circ } ) .
$$

Let the $p$ characteristic roots be $\sigma _ { 1 } , \ldots , \sigma _ { p }$ and

$$
\begin{array} { c } { { s _ { 1 } = \sigma _ { 1 } + \cdot \cdot \cdot + \sigma _ { p } , \qquad s _ { 2 } = \sigma _ { 1 } \sigma _ { 2 } + \cdot \cdot \cdot + \sigma _ { p - 1 } \sigma _ { p } , } } \\ { { \ldots , \qquad s _ { p } = \sigma _ { 1 } \sigma _ { 2 } \cdot \cdot \cdot \sigma _ { p } ; } } \end{array}
$$

then

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { { \frac { d ^ { p } x } { d t ^ { p } } } - s _ { 1 } { \frac { d ^ { p - 1 } x } { d t ^ { p - 1 } } } + s _ { 2 } { \frac { d ^ { p - 2 } x } { d t ^ { p - 2 } } } + \cdot \cdot \cdot + ( - 1 ) ^ { p } s _ { p } x } { | x | + \left| { \frac { d x } { d t } } \right| + \cdot \cdot \cdot + \left| { \frac { d ^ { p - 1 } x } { d t ^ { p - 1 } } } \right| } } = 0 ,
$$

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { { \cfrac { d ^ { p + 1 } x } { d t ^ { p + 1 } } } - s _ { 1 } { \cfrac { d ^ { p } x } { d t ^ { p } } } + s _ { 2 } { \cfrac { d ^ { p - 1 } x } { d t ^ { p - 1 } } } + \cdot \cdot \cdot + ( - 1 ) ^ { p } s _ { p } { \cfrac { d x } { d t } } } { | x | + \left| { \cfrac { d x } { d t } } \right| + \cdot \cdot \cdot + \left| { \cfrac { d ^ { p - 1 } x } { d t ^ { p - 1 } } } \right| } } = 0 ,
$$

$$
\operatorname* { l i m } _ { t \to \infty } { \frac { { \frac { d ^ { n } x } { d t ^ { n } } } - s _ { 1 } { \frac { d ^ { n - 1 } x } { d t ^ { n - 1 } } } + s _ { 2 } { \frac { d ^ { n - 2 } x } { d t ^ { n - 2 } } } + \cdot \cdot \cdot + ( - 1 ) ^ { p } s _ { p } { \frac { d ^ { n - p } x } { d t ^ { n - p } } } } { | x | + \left| { \frac { d x } { d t } } \right| + \cdot \cdot \cdot + \left| { \frac { d ^ { p - 1 } x } { d t ^ { p - 1 } } } \right| } } = 0 .
$$

Haacke (1952) discussed the stability problem for a system of linear differential equations of the second order with periodic coefficients depending on a parameter 𝜆. Suppose that this system admits 2n independent solutions that are bounded for suffciently large values of 𝜆. Such a system can be transformed to a system of first-order equations that represents the solutions asymptotically with regard to λ in the form of formal series in reciprocal powers of ,as was shown by Perron (1937)，Langer (1949)，and by Newell (1942） in the complex domain.

# 16.17KINEMATIC SIMILARITY

Since Perron (1930a； see also 1913) introduced the idea of kinematic similarity of matrices in the theory of stability, Loewy (1918) and Jacobson (1935,1937) extended the idea，and Jacobson defined pseudo-linear transformations, similarity，reducibility，and decomposability of matrices. An extension to differential equations with almost periodic coeffcients (Section 14.19) has been studied by Cameron (1938) and Lillo (1955；Sections 14.24-14.28).When a given matrix can be transformed to a matrix whose elements below the principal diagonal are all zero,it is called reducible and the reduced form a triangular matrix (Gantmacher, 1958,1959,1959a; Gantmacher and Krein,1960).Diliberto (1950) improved the idea of Perron (Section 13.17). The relation between the characteristic exponents of Perron and the classical stability theory is clarified by the idea of kinematic similarity developed by Markus (1955).

Let $M _ { n }$ be the set of all $n \times n$ matrices whose elements are complexvalued functions of a real variable $t$ ，continuous and bounded for $0 \leq t < \infty$ .For $\pmb { A }$ ， $B \in M _ { n }$ we say that $A \sim B$ ,i.e., $\pmb { A }$ is kinematically similar to $\pmb { B }$ in the terminology of Markus (1955)，if there exists a matrix $P$ with $P , P ^ { - 1 }$ and ${ \dot { P } } \in M _ { n }$ such that $- P ^ { - 1 } [ \dot { P } - A P ] = B$ for all $0 \leq t < \infty$

Let ${ \dot { X } } = A X$ ，where $\pmb { { \cal A } } \in { \pmb { { \cal M } } } _ { n }$ . For each nonzero solution vector $X _ { \alpha } ( t )$ we define a characteristic exponent of $\pmb { A }$ by

$$
\operatorname* { l i m } _ { t \to \infty } \left[ t ^ { - 1 } \log | X _ { \alpha } ( t ) | \right] = \lambda _ { \alpha } .
$$

Perron (1930； Section 16.14) showed that the $\lambda _ { \alpha }$ are bounded and there are at most distinct characteristic exponents of $\pmb { A }$ , and that every matrix in $M _ { n }$ is kinematically equivalent to a triangular matrix (1930a ; Section 16.16).For such a solution vector $X ( t )$ with characteristic exponent $\lambda$ ，we define a type of $\pmb { A }$ as

$$
\nu ( \lambda , X ( t ) ) = \nu ( \lambda ) = \operatorname* { l i m } _ { t \to \infty } \frac { \log | X ( t ) e ^ { - \lambda t } | } { \log t } .
$$

The set of all solution vectors of ${ \dot { X } } = A X$ with characteristic exponents $\lambda \leq \lambda _ { i }$ $( i = 1 , 2 , \ldots , k )$ forms a linear space (see Section 16.18) called $E ( \lambda _ { i } )$ . Moreover $E ( \lambda _ { i - 1 } )$ is properly included in $E ( \lambda _ { i } )$ and we adopt the convention $E ( \lambda _ { 0 } ) = 0$ . If for any two solution vectors in the set the difference $E ( \lambda _ { i } ) \ : - \ : E ( \lambda _ { i - 1 } )$ differs only by a solution in $E ( \lambda _ { i - 1 } )$ , then the type is the same.Thus we can define the type of a coset in the factor space (Section 16.18) $E ( \lambda _ { i } ) / E ( \lambda _ { i - 1 } )$ ，taking the identity coset to have zero type. The collection of cosets of $E ( \lambda _ { i } ) / E ( \lambda _ { i - 1 } )$ of the type $\nu \not \equiv \nu _ { i j }$ is a linear subspace of $E ( \lambda _ { i } ) / E ( \lambda _ { i - 1 } )$ called $T ( \lambda _ { i } , \nu _ { i j } )$ . We agree that $T ( \lambda _ { i } , \nu _ { i 0 } ) = 0$

Let $\lambda _ { 1 } < \lambda _ { 2 } < \cdots < \lambda _ { k }$ be the distinct characteristic exponents of $\pmb { A } \in M _ { n }$ with corresponding types $\nu _ { 1 1 } < \nu _ { 1 2 } < \cdot \cdot \cdot , \nu _ { 2 1 } < \nu _ { 2 2 } < \cdot \cdot \cdot , \cdot \cdot ,$ $\nu _ { k 1 } < \nu _ { k 2 } < \cdots$ The multiplicity of $\lambda _ { i } ( i = 1 , 2 , \ldots , k )$ is $m ( \lambda _ { i } ) =$ dim $[ E ( \lambda _ { i } ) / E ( \lambda _ { i - 1 } ) ]$ . The multiplicity of $\nu _ { i j }$ is

$$
m ( \nu _ { i j } ) = \dim \frac { T ( \lambda _ { i } , \nu _ { i j } ) } { T ( \lambda _ { i } , \nu _ { i , j - 1 } ) } .
$$

Theorem $\boldsymbol { \mathit { 1 } }$ :The characteristic exponents $\lambda _ { i }$ of $\pmb { { \cal A } } \in { \cal M } _ { n }$ , their types $\nu _ { i j }$ ，and the multiplicities $m ( \lambda _ { i } )$ and $m ( \nu _ { i j } )$ are invariants of kinematic similarity.

We consider a nonsingular coordinate change $Y = P ^ { - 1 } X$ with $P \in M _ { n }$ ，and examine the geometry of the solution curve $X ( t )$ . The transformed equation, i.e., the equation with the same solution curve in $E _ { c } ^ { n }$ ，an $_ n$ -dimensional compact Euclidean space,is $\dot { Y } = B Y$ ， $\pmb { B } =$ $- P ^ { - 1 } [ \dot { P } - A P ]$ . Hence the relation $A \sim B$ holds if and only if $\pmb { A }$ and $\pmb { B }$ are the coefficients of the same differential system referred to two coordinate systems in $E _ { c } ^ { n }$ .If $Y = P _ { 0 } ^ { - 1 } X$ ，where $P _ { 0 }$ is a constant matrix, then we have $- P _ { \circ } ^ { - 1 } [ \dot { P } _ { 0 } - A P _ { 0 } ] = P _ { 0 } ^ { - 1 } A P _ { \circ } = B$ . An algebraic relation of similarity,which is called static similarity,isa special case of kinematic similarity.

The relation $- P ^ { - 1 } [ \dot { P } - A P ] = B$ defines the kinematic similarity $A \sim B$ . We consider the solution space for ${ \dot { X } } = A X$ which is isomorphic (Section 16.18) to the solution space for $\dot { Y } = B Y$ . Since the matrices $P$ and $P ^ { - 1 }$ are both in $M _ { n }$ ， the corresponding solutions $X ( t )$ and $Y ( t )$ are of the same type with the same characteristic exponents. Hence $\lambda _ { i } , \nu _ { i j } , m ( \lambda _ { i } ) , m ( \nu _ { j i } )$ are the same for $\pmb { A }$ and $\pmb { B }$ .owing to isomorphism (Section 16.18).

Any constant $n \times n$ matrix $\scriptstyle A _ { 0 }$ isstatically，and accordingly, kinematically similar to the Weierstrass-Jordan or Jordan matrix (Bodewig,1956；Gantmacher,1958,1959,1959a；Gantmacher and Krein,1960) $A _ { J } = \mathrm { d i a g }$ $\left\{ A _ { 1 } , A _ { 2 } , \ldots , A _ { k } \right\}$ ，where each square block $A _ { i } =$ diag $\{ A _ { i 1 } , \dotsc , A _ { i p _ { i } } \}$ $( i = 1 , 2 , \dots , k )$ and

$$
A _ { i r } = \left( \begin{array} { c c c c } { { \lambda _ { i } } } & { { 1 } } & { { \dots } } & { { 0 } } \\ { { } } & { { \lambda _ { i } } } & { { 1 } } & { { \dots } } & { { 0 } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } \\ { { } } & { { } } & { { } } & { { 1 } } \\ { { 0 } } & { { } } & { { } } & { { \ddots } } \end{array} \right)
$$

A Jordan matrix $\scriptstyle A _ { \sigma }$ that is statically similar to $\scriptstyle A _ { 0 }$ is unique (Section 1.21).We arrange an order of the blocks $\boldsymbol { A } _ { i r }$ down the principal diagonal of $A _ { J }$ ，for example,by increasing at first $| \lambda _ { i } |$ ，next arg $\lambda _ { i }$ ， and last, dim $\pmb { A } _ { i r }$ . We introduce real Jordan matrices as the canonical form for a subclass of $M _ { n }$ , including constant and periodic matrices.

Lemma: If there are two real constant Jordan matrices such as $A _ { J } \sim B _ { J }$ ，then $A _ { J } = B _ { J }$

In fact,by Theorem 1 the invariants $\lambda _ { i } , \nu _ { i j } , m ( \lambda _ { i } ) , m ( \nu _ { i j } )$ characterize a real Jordan matrix. The roots characterizing $A _ { J }$ are $\lambda _ { i }$ . Hence dim $A _ { i } = m ( \lambda _ { i } )$ . But $A _ { i } = \operatorname { d i a g } \left\{ A _ { i 1 } , \dotsc , A _ { i p _ { i } } \right\}$ ，and the dimension of the block $\pmb { A } _ { i r }$ $( r = 1 , 2 , \ldots , p )$ is determined by the type $\nu _ { i j }$ , because the number of the blocks $A _ { i r }$ of dimension $\geq \nu _ { i j } + 1$ is $m ( \nu _ { i j } )$ . Thus the total structure of $A _ { J }$ is determined by $\lambda _ { i } , \nu _ { i j } , m ( \lambda _ { i } ) , m ( \nu _ { i j } )$ ：

Theorem 2: For the subclass of matrices in $M _ { n }$ that are kinematically similar to constant matrices the invariants consisting of characteristic exponents $\lambda _ { i }$ ， type $\nu _ { i j }$ ，and their multiplicities $m ( \lambda _ { i } )$ and $m ( \nu _ { i j } )$ form a complete set of invariants.Also, if $A \sim C$ for $\pmb { { \cal A } } \in { \cal M } _ { n }$ ， and $C$ is a constant matrix, then there exists a unique real constant Jordan matrix $A _ { J } \sim A$ which displays the invariants of $\pmb { A }$

The foregoing lemma shows the uniqueness of $A _ { J }$ .From the existence of $A _ { J }$ it follows that the above invariants form the complete set.In order to show the existence of $A _ { J }$ it is sufficient to prove that a complex Jordan matrix $C$ is kinematically similar to a real Jordan matrix. In fact, it is sufficient to show that each elementary divisor group (Bodewig,1956) is of the form

$$
C _ { i j } = \left[ \begin{array} { l l l l } { \lambda } & { 1 } & { \cdots } & { 0 } \\ & { \lambda } & { 1 } & { \cdots } & { 0 } \\ & & { \cdot } & { \cdot } & \\ & & & { \cdot } & { 1 } \\ { 0 } & & & & { \cdot } & \end{array} \right] \sim \left[ \begin{array} { l l l l } { \xi } & { 1 } & { \cdots } & { 0 } \\ & { \xi } & { 1 } & { \cdots } & { 0 } \\ & & { \cdot } & { \cdot } \\ & & & { \cdot } & { 1 } \\ { 0 } & & & { \cdot } & { \xi } \end{array} \right] = A _ { i j }
$$

$$
( \lambda = \xi + \sqrt { - 1 } \eta ) .
$$

We define

$$
\Pi _ { i j } = \exp { \{ \sqrt { - 1 } \eta t \} } \cdot \left( { { \ O } ^ { 1 } } \cdot { { \ O } ^ { 0 } } \right)
$$

and by calculation we find that

$$
- \Pi _ { i j } ^ { - 1 } ( \dot { \Pi } _ { i j } - { C } _ { i j } \Pi _ { i j } ) = A _ { i j } .
$$

Thus we obtain the unique canonical form $A _ { J }$ for $\pmb { A }$ by eliminating the imaginary parts of the characteristic exponents of $C$ ，which is a complex Jordan matrix $C \sim A$ . For example, if $\pmb { A }$ is a periodic matrix, we obtain its characteristic exponents as the characteristic roots of a unique real Jordan matrix $A _ { J } \sim A$

Corollary: If $A \sim C$ over the real field,where $\pmb { { \cal A } } \in { \cal M } _ { n }$ and $C$ is a constant matrix, then $A \sim A _ { J }$ over the real field.

In fact,assuming that $C$ is a classical normal form for a real matrix, we discuss

$$
\begin{array} { r } { C _ { i j } ^ { R } = \left[ \begin{array} { l l l l } { \Lambda _ { i } } & { I _ { 2 } } & { \dots } & { 0 } \\ & { \Lambda _ { i } ^ { \cdot } } & & \\ & { \Lambda _ { \cdot } } & { \cdot } & \\ & & & { \cdot } & \\ & & & { \cdot } & { I _ { 2 } } \\ { 0 } & & & & { \Lambda _ { i } } \end{array} \right] , } \end{array}
$$

$$
\Lambda _ { i } = { \left( \begin{array} { l l } { 0 } & { 1 } \\ { - c _ { i } } & { - b _ { i } } \end{array} \right) } , \quad I _ { 2 } = { \left( \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } .
$$

The corresponding elementary divisor is a power $A _ { i } = { \textstyle { \frac { 1 } { 2 } } } ( 4 c _ { i } - b _ { i } ^ { 2 } ) ^ { 1 / 2 }$ $> 0$ of $( x ^ { 2 } + b _ { i } x + c _ { i } )$ . Put

$$
\mathrm { ~  ~ \Gamma ~ } _ { i } ^ { \prime } = \binom { \cos \Delta _ { i } t } { - ( b _ { i } / 2 ) \cos \Delta _ { i } t - \Delta _ { i } \sin \Delta _ { i } t } \mathrm { ~  ~ \Gamma ~ } _ { - } ^ { \prime } ( b _ { i } / 2 ) \sin \Delta _ { i } t + \Delta _ { i } \cos \Delta _ { i } t \big / \mathrm { ~  ~ \Gamma ~ }
$$

$$
\Pi _ { i } = \mathbb { d i a g } \{ \Pi _ { i } ^ { \prime } , \ldots , \Pi _ { i } ^ { \prime } \} ,
$$

then the $\Pi _ { i }$ are of the same dimension as the $C _ { i j } ^ { R }$ . We compute $- \Pi _ { i } ^ { - 1 } ( \dot { \Pi } _ { i } - C _ { i j } ^ { R } \Pi _ { i } )$ ， which is statically similar to diag $\{ A _ { i j } , A _ { i j } \}$ ，

$$
A _ { i j } = \left[ \begin{array} { c c c c } { - ( b _ { i } / 2 ) } & { 1 } & { \cdots } & { 0 } \\ { - ( b _ { i } / 2 ) } & { 1 } & { \cdots } & { 0 } \\ { \phantom { - } } & { \cdot } & { \cdot } & { \phantom { - } } \\ { \phantom { - } } & { \cdot } & { \cdot } & { 1 } \\ { 0 } & { \phantom { - } } & { \cdot } & { \phantom { - } } \end{array} \right] .
$$

Hence we have $A \sim A _ { 0 }$ over the real field.

Theorem 3: Let $A \sim A _ { J }$ where $\pmb { { \cal A } } \in { \cal M } _ { n }$ and $A _ { J }$ is its real constant Jordan form.Then there exists a diagonal matrix $D \in M _ { n }$ such that $A \sim D$ if and only if $A _ { J }$ is diagonal.

It is sufficient to prove that $A \sim D$ implies that $A _ { J }$ is diagonalized. Let us suppose the opposite.Consider a special case

$$
A _ { J } = \left\{ { \begin{array} { l l l l } { \lambda } & { 1 } & { \cdots } & { 0 } \\ & { \lambda } & { 1 } & { \cdots } & { 0 } \\ & & { \cdot } & { \cdot } & { \cdot } \\ & & & { \cdot } & { 1 } \\ { 0 } & & & { \cdot } & { \lambda } \end{array} } \right\} ,
$$

in which $A _ { J }$ consists of only one elementary block, $P = ( p _ { i j } ) , D =$ diag $\{ d _ { 1 } , \ldots , d _ { n } \}$ . Then from $\dot { P } = A _ { J } P - P D$ we obtain

$$
\begin{array} { r l r } & { = \lambda p _ { 1 1 } + p _ { 2 1 } - p _ { 1 1 } d _ { 1 } , } & { \dot { p } _ { 1 2 } = \lambda p _ { 1 2 } + p _ { 2 2 } - p _ { 1 2 } d _ { 2 } , \qquad \cdots , } \\ & { } & { \dot { p } _ { 1 n } = \lambda p _ { 1 n } + p _ { 2 n } - p _ { 1 n } d _ { n } , } \\ & { = \lambda p _ { 2 1 } + p _ { 3 1 } - p _ { 2 1 } d _ { 1 } , } & { \dot { p } _ { 2 2 } = \lambda p _ { 2 2 } + p _ { 3 2 } - p _ { 2 2 } d _ { 2 } , \qquad \cdots , } \\ & { } & { \dot { p } _ { 2 n } = \lambda p _ { 2 n } + p _ { 3 n } - p _ { 2 n } d _ { n } , } \end{array}
$$

$$
\dot { p } _ { n 1 } = \lambda p _ { n 1 } - p _ { n 1 } d _ { 1 } , \qquad \cdot \cdot \cdot , \qquad \dot { p } _ { n n } = \lambda p _ { n n } - p _ { n n } d _ { n } .
$$

If $d _ { 1 } = \lambda$ ，then ${ \dot { p } } _ { n 1 } = 0$ and $p _ { n 1 } = c _ { n 1 }$ ， a constant. But in that case we have $\dot { p } _ { n - 1 , 1 } = \lambda p _ { n - 1 , 1 } + p _ { n , 1 } - p _ { n - 1 , 1 } d _ { 1 } = c _ { n , 1 } $ $p _ { n - 1 , 1 } = c _ { n 1 } t +$ $c _ { n - 1 , 1 }$ . Since all the $p _ { i j } ( t )$ are bounded,we should have $p _ { n 1 } = 0$ If $d _ { 1 } \not \equiv \lambda$ ，then we should have

$$
p _ { n 1 } = c _ { n 1 } \exp \left\{ \int _ { 0 } ^ { t } ( \lambda - d _ { 1 } ) \ d s \right\}
$$

and

$$
\ L _ { n - 1 , 1 } = c _ { n 1 } t \exp \left\{ \int _ { 0 } ^ { t } \left( \lambda - d _ { 1 } \right) d s \right\} + c _ { n 1 } c _ { n - 1 , 1 } \exp \left\{ \int _ { 0 } ^ { t } \left( \lambda - d _ { 1 } \right) d s \right\} ,
$$

where

$$
\int _ { 0 } ^ { t } \left( \lambda - d _ { 1 } \right) d s \to - \infty
$$

But then we should have $p _ { n 1 } \to 0$ as $t \to \infty$ . Hence $\begin{array} { r } { \operatorname* { l i m } _ { t  \infty } p _ { n 1 } ( t ) = 0 } \end{array}$

With these preparations on the kinematic similarity of matrices we study the stability of a nonlinear differential system.

Consider

$$
\frac { d u _ { s } } { d t } = f _ { s } ( u ) \qquad ( s = 1 , \ldots , n ) ,
$$

where the $f _ { s } ( u )$ are real-valued functions of class $C ^ { \prime \prime }$ in a region $o$ of an Euclidean space $E ^ { n }$ . Let $u _ { s } = \phi _ { s } ( t )$ be a solution in a bounded subregion $\kappa$ ，where ${ \bar { \kappa } } \subset O$ for all $0 \leq t < \infty$ . Let us study the Liapounov stability of this solution.

Suppose that a nearby solution $u ( t )$ lying in $K \subset O$ for $0 \leq t < t _ { 1 }$ $< \infty$ differs from the base solution $\phi _ { s } ( t )$ by $x _ { s } ( t ) = u _ { s } ( t ) - \phi _ { s } ( t )$ .The difference satisfies

$$
\frac { d x _ { s } } { d t } = \sum _ { j } \frac { \partial f _ { s } } { \partial u _ { j } } \left[ \phi ( t ) \right] x _ { j } + \sum _ { j , k } \frac { \partial ^ { 2 } f _ { s } } { \partial u _ { j } \partial u _ { k } } \left[ \phi ( t ) + \varepsilon ( t ) \right] x _ { j } x _ { k } ,
$$

where $\phi ( t ) + \varepsilon ( t )$ is a point on the segment connecting $\phi ( t )$ and $u ( t )$ Thus we get

$$
\frac { d x _ { s } } { d t } = \sum _ { j } J _ { j } ^ { s } ( t ) x _ { j } + \sum _ { j , k } B _ { j k } ^ { s } ( t ) x _ { j } x _ { k } ,
$$

where $\mathbf { \boldsymbol { J } } ( t ) , \mathbf { \boldsymbol { B } } ( t )$ are continuous and bounded in $0 \leq t < t _ { 2 } \leq t _ { 1 }$ We seek the condition on $\mathbf { } J ( t )$ that every solution $x ( t )$ with a sufficiently small initial value $| x ( 0 ) |$ is defined in $0 \leq t < \infty$ and approaches the origin as $t \to \infty$ . In such a case the solution $\phi ( t )$ of the nonlinear system is called stable.It should be noticed that the conjecture，that if the characteristic exponents of $\boldsymbol { J } ( t )$ are negative then the solution $\phi ( t )$ of the nonlinear system is stable,is false (Perron,1930b).

Theorem 4: Let

$$
\frac { d x _ { s } } { d t } = \sum _ { j } J _ { j } ^ { s } ( t ) x _ { j } + F _ { s } ( t , x ) \qquad ( s = 1 , \ldots , n ) ,
$$

where $J ( t ) \in M _ { n }$ and $F ( t , x ) \in C ^ { \prime }$ for $0 \leq t < \infty$ and $| x | < \varepsilon$ for $\varepsilon > 0$ Also assume that

$$
\operatorname* { l i m } _ { | x | \to 0 } { \frac { | F ( t , x ) | } { | x | } } = 0
$$

uniformly in $0 \leq t < \infty$ and that $\boldsymbol { J } ( t )$ is kinematically similar to a constant matrix and has negative characteristic exponents. Then there exists a $\delta > 0$ such that if $| x ( 0 ) | < \delta$ the solution $x ( t )$ is defined for all $0 \leq t < \infty$ with $| x ( t ) | < \varepsilon$ ，and furthermore $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } | x ( t ) | = 0 } \end{array}$

In fact, let $Y { = } P ^ { - 1 } X$ ，or $\scriptstyle y _ { s } = \sum _ { j } \rho _ { j } ^ { s } x _ { j }$ or $\begin{array} { r } { x _ { s } { = } \sum _ { j } p _ { j } ^ { s } y _ { j } } \end{array}$ be the coordinate change,and let $P$ ，such that $P , P ^ { - 1 }$ ， ${ \dot { P } } \in M _ { n }$ and $- P ^ { - 1 } [ \dot { P } - J P ]$ $= C$ ,be a real constant Jordan matrix whose characteristic exponents are negative. The transformed system is

$$
\frac { d y _ { s } } { d t } = \sum _ { j } C _ { j } ^ { s } y _ { j } + \sum _ { j } \rho _ { j } ^ { s } ( t ) F _ { j } ( t , p _ { m } ^ { e } y _ { m } ) ,
$$

where $\begin{array} { r } { G _ { s } ( t , y ^ { e } ) = \sum _ { j } \rho _ { j } ^ { s } ( t ) F _ { j } ( t , p _ { m } ^ { e } y _ { m } ) } \end{array}$ is supposed to be of class $C ^ { \prime }$ such that $| y | < \varepsilon _ { 1 } = \varepsilon / A$ in $0 \leq t < \infty$ . Since $0 < \alpha < | \rho ( t ) | < A$ for $\scriptstyle t \geq 0$ ，we have

$$
\operatorname* { l i m } _ { | y | \to 0 } \frac { | G ( A , y ) | } { | y | } = \operatorname* { l i m } _ { | x | \to \infty } \frac { | \rho _ { j } ^ { s } ( t ) F _ { j } ( t , x ) | } { | \rho _ { j } ^ { s } ( t ) x _ { j } | } = 0 .
$$

By the standard theorem we see that there exists a $\delta _ { \mathrm { 1 } } > 0$ such that $| y ( t ) | < \varepsilon$ for $0 \leq t < \infty$ and $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } | y ( t ) | = 0 } \end{array}$ ，that is, $| x ( 0 ) | < \delta _ { 1 } \alpha$ $= \delta$ $\delta , | x ( t ) | < \varepsilon _ { 1 } A = \varepsilon$ for all $0 \leq t < \infty$ ，and $\begin{array} { r } { \operatorname* { l i m } _ { t  \infty } | x ( t ) | = 0 } \end{array}$

The characteristic exponents are estimated by

Theorem 5: Let $\pmb { { \cal A } } \in { \cal M } _ { n }$ commute with $\int _ { 0 } ^ { t } A ( s ) \ d s$ for each $0 \leq t$ $< \infty$ . Assume that $\begin{array} { r } { A = A _ { p } + A _ { 0 } } \end{array}$ ，where $\scriptstyle A _ { 0 }$ is constant and commutes with both $\pmb { A }$ and $\int _ { 0 } ^ { t } A ( s ) \ d s$ . Suppose that $\int _ { 0 } ^ { 1 } A _ { p } ( s ) d s \in M _ { n }$ Then $\pmb { A }$ $\sim A _ { 0 }$ and $A _ { 0 } = \operatorname* { l i m } _ { t \to \infty } { \biggl [ } t ^ { - 1 } \int _ { 0 } ^ { t } A ( s ) \ d s { \biggr ] } .$

Corolary: Let $\pmb { { \cal A } } \in { \cal M } _ { n }$ be almost periodic and let $\pmb { A }$ $4 , \int _ { 0 } ^ { t } A \ d s _ { ; }$ and $\pmb { A } _ { 0 }$ all commute for any $t$ in $0 \leq t < \infty$ where

$$
A _ { 0 } = \operatorname* { l i m } _ { t \to \infty } { \biggl [ } t ^ { - 1 } \int _ { 0 } ^ { t } A ( s ) \ d s { \biggr ] } .
$$

If $\int _ { 0 } ^ { t } \left( A - A _ { 0 } \right) d s \in M _ { n }$ then $A \sim A _ { \mathfrak { o } }$ .Moreover,the transformation matrix $\pmb { P }$ is almost periodic.

Corollary: Let $\pmb { { \cal A } } \in { \cal M } _ { n }$ be almost periodic and commute with $\int _ { 0 } ^ { t } A \ d s$ for any $t$ in $0 \leq t < \infty$ . Assume that $\pmb { A }$ is an absolutely con-vergent Fourier series whose characteristic exponents are bounded below by a nonzero constant. Then $A \sim A _ { 0 } = 0$ by an almost periodic matrix $P$

A matrix is called normal if $A A ^ { * } = A ^ { * } A$ ,that is,if it is statically similar to a complex diagonal matrix by a unitary transformation (Section 1.21； Frazer, Duncan,and Collar,1938).

Theorem 6: Let $\pmb { { \cal A } } \in { \cal M } _ { n }$ be normal for each fxed $t$ in $0 \leq t < \infty$ Let $M ( t )$ be the maximum of the real parts of the characteristic roots of $\mathbf { \nabla } A ( t )$ ，and $m ( t )$ be the minimum of these real parts.Then

$$
\varlimsup _ { t  \infty } [ t ^ { - 1 } \int _ { 0 } ^ { t } m ( s ) \ d s ] \leq \lambda _ { i } \leq \varlimsup _ { t  \infty } [ t ^ { - 1 } \int _ { 0 } ^ { t } M ( s ) \ d s ] ,
$$

where the $\lambda _ { i }$ are the characteristic exponents of $\pmb { A }$

Corollary: Let $\pmb { { \cal A } } \in { \cal M } _ { n }$ be normal for each fixed $t \geq 0$ and let $\pmb { A }$ be almost periodic or have period $T > 0$ .Then $M ( t )$ and $m ( t )$ are also almost periodic or have period $T$ ，respectively，and

$$
\operatorname* { l i m } _ { t \to \infty } \left[ t ^ { - 1 } \int _ { 0 } ^ { t } m ( s ) ~ d s \right] \leq \lambda _ { i } \leq \operatorname* { l i m } _ { t \to \infty } \left[ t ^ { - 1 } \int _ { 0 } ^ { t } M ( s ) ~ d s \right] .
$$

Lillo (1955,1960) considered an inequality

$$
\left| \int _ { t _ { 0 } } ^ { t _ { 0 } + T ( \varepsilon ) + \sigma } \left[ a ( t ) - \lambda \right] d t \right| \leq \varepsilon [ T ( \varepsilon ) + \sigma ]
$$

for all $\sigma \geq 0$ and

$$
\left| \int _ { t _ { 0 } } ^ { t _ { 0 } + t } \left[ a ( s ) - \lambda \right] d s \right| < M ( \varepsilon ) + \varepsilon t
$$

for all $t \geq 0$ ，where $M [ a ( t ) ] = \lambda$ is the mean value of a continuous function $a ( t )$ in $0 \leq t < \infty$ ，and $T ( \varepsilon ) , M ( \varepsilon )$ are called the constants of the mean with initial time $t _ { 0 }$ .A continuous function $a ( t )$ has a property $\pmb { A }$ with mean value $\lambda$ if for every $\mu > 0$ there exists a constant $M ( \mu )$ such that

$$
\left| \int _ { s } ^ { t } \left[ a ( \tau ) - \lambda \right] d \tau \right| < M ( \mu ) + \mu | t - s |
$$

for all $0 \leq t , s \leq \infty$ . The norm, written $\| A ( t _ { k } ) \|$ ， cf a constant $n \times n$ matrix is $\begin{array} { r } { \| A ( t _ { k } ) \| = \sum _ { i , j } | a _ { i j } ( t _ { k } ) | } \end{array}$ ，and the norm $\| A \|$ of a variable matrix $\pmb { \mathscr { A } } ( t ) , t \in R$ ,is $\| A \| = { \mathrm { 1 . u . b . } } _ { t \in R } \left\| A ( t ) \right\|$ .Denote the jth column of a matrix $A ( t )$ by $\left[ \boldsymbol { A } ( t ) \right] _ { j }$ and the $k$ th row by $[ A ( t ) ] ^ { k }$ ·

If the solution $x ( t )$ of

$$
\frac { d x } { d t } = [ A ( t ) + B ( t ) ] x ,
$$

where $\mathbf { \nabla } A ( t ) , B ( t )$ are continuous and uniformly bounded functions in $0 \leq t < \infty$ ，satisfies

$$
\operatorname* { l i m } _ { t \to \infty } \left[ { \frac { \log \| x ( t ) \| } { t } } \right] = \lambda ,
$$

then $x ( t )$ is said to have the characteristic exponent λ. If

$$
\operatorname* { l i m } _ { t \to \infty } \left[ { \frac { \log \| x ( t ) \| } { t } } \right] = \lambda ,
$$

then $[ x ( t ) ] = \lambda$ is said to have the strong characteristic exponent λ.

Let $\lambda _ { 1 } < \lambda _ { 2 } < \cdots < \lambda _ { k }$ be distinct characteristic exponents,C.E. $[ x ( t ) ]$ . Let $e _ { 1 }$ be the number of linearly independent solutions such as C.E. $[ x ( t ) ] = \lambda _ { 1 }$ .The sum $\textstyle \sum _ { i = 1 } ^ { s } e _ { i }$ is the number of linearly independent solutions such as C.E. $[ x ( t ) ] = \lambda _ { s }$ ,and $e _ { i }$ is called the multiplicity of $\lambda _ { i }$ ，written C.E. $[ \lambda _ { 1 } , \ldots , \lambda _ { n } ]$

As has been shown, the differential system

$$
\frac { d y } { d t } = B ( t ) y , \qquad B ( t ) \in M _ { n }
$$

is equivalent to

$$
\frac { d x } { d t } = A ( t ) x , \qquad A ( t ) \in M _ { n } .
$$

Lemma $\boldsymbol { \mathit { 1 } }$ :Suppose that $\delta _ { i } = \lambda _ { n } - \lambda _ { n - i } > 0$ ； then， given $0 < \varepsilon _ { 1 }$ $< \delta _ { 1 } / 4$ , there exists an integer $k > 2$ such that when $\varepsilon _ { n - j } = \varepsilon _ { 1 } / k ^ { n - j }$ $( j = 0 , \ldots , n - 2 )$ and $a _ { i } = ( \delta _ { i } + \varepsilon _ { n } ) / ( \delta _ { n } - \varepsilon _ { n } - \varepsilon _ { i + 1 } )$ ，we have $\prod _ { i = 1 } ^ { n - 1 } a _ { i } < b$

Lemma 2: If

$$
| \psi _ { 1 } ( t ) | \left\{ \begin{array} { l l } { \leq \exp \left\{ \lambda _ { n } t - \varepsilon _ { 1 } t _ { 0 } + M ( t - t _ { 0 } ) \right\} \quad } & { \mathrm { f o r } \quad \quad t \geq t _ { 0 } , } \\ { \leq \exp \left\{ \lambda _ { n } t + \varepsilon _ { n } t _ { 0 } \right\} \quad } & { \mathrm { f o r } \quad \quad t \leq t _ { 0 } , } \end{array} \right.
$$

$$
\left| a _ { i j } \right| < M , \left| \int _ { 0 } ^ { t } a _ { i i } ( \tau ) d \tau - \lambda _ { i } t \right| \leq \left\{ \begin{array} { l l } { \varepsilon _ { n } t \quad } & { \mathrm { ~ f o r ~ } \quad \quad t \geq t _ { 0 } , } \\ { \varepsilon _ { n } t _ { 0 } \quad } & { \mathrm { ~ f o r ~ } \quad 0 \leq t \leq t _ { 0 } } \end{array} \right.
$$

and

$$
\psi _ { i 1 } ( h ) = \int _ { 0 } ^ { h } \exp \left\{ \int _ { 0 } ^ { h } a _ { i i } ( \tau ) d \tau \right\} \cdot a _ { i \pi } ( s ) \psi _ { 1 } ( s ) d s ,
$$

then

$$
| \psi _ { i 1 } ( h ) | \leq \frac { 2 M } { \delta _ { n - i } } \exp \left\{ \lambda _ { n } h - \varepsilon _ { 2 } h \right\} \qquad \mathrm { f o r } \qquad \varepsilon _ { 1 } t _ { 0 } \leq h \leq b t _ { 0 } .
$$

Lemma 3: If

$$
\begin{array} { r } { \psi _ { i j } ( h ) = \displaystyle \int _ { 0 } ^ { h } \exp \left\{ \int _ { 0 } ^ { h } a _ { i i } ( \tau ) ~ d \tau \right\} \cdot a _ { i n - j + 1 } ( s ) \psi _ { j } ( s ) ~ d s , } \end{array}
$$

$$
| \psi _ { j } ( s ) | \le \left\{ \begin{array} { l l } { H \exp \left\{ - \varepsilon _ { j } s + \lambda _ { n } s \right\} \quad } & { \mathrm { f o r } \quad \quad t _ { j } \leq s \leq b t _ { 0 } , } \\ { \exp \left\{ \varepsilon _ { n } t + \lambda _ { n } s \right\} \quad } & { \mathrm { f o r } \quad \quad 0 \leq s \leq t _ { j } , } \end{array} \right.
$$

$$
\left| \int _ { 0 } ^ { \tau } a _ { i i } ( \tau ) d \tau - \lambda _ { j } l \right| \le \left\{ \begin{array} { l l } { \varepsilon _ { n } l \quad } & { \mathrm { ~ f o r ~ } \quad \quad t _ { j } \leq l , } \\ { \varepsilon _ { n } t _ { j } \quad } & { \mathrm { ~ f o r ~ } \quad 0 \leq l \leq t _ { j } , } \end{array} \right.
$$

$$
[ \delta _ { n - j } + \varepsilon _ { n } / ( \delta _ { n - i } - 2 \varepsilon _ { n } - \varepsilon _ { j + 1 } ) ] t _ { j } \leq h \leq b t _ { 0 } ,
$$

then

$$
| \psi _ { i j } ( h ) | \leq M \biggl ( \frac { 1 } { \delta _ { n - i } } + \frac { H } { \delta _ { n - i } - \varepsilon _ { j } } \biggr ) \exp { \{ \lambda _ { n } h - \varepsilon _ { i + 1 } h \} } .
$$

These three lemmas can be proved by direct computation.

Theorem 7: If for the solution vector $X ( t , x )$ of (163) the strong C.E. $( [ X ( t , 0 ) ] _ { i } ) = \lambda _ { i } ( i = 1 , . . . , n )$ ，and

$$
\lambda _ { i } < \lambda _ { i + 1 } \qquad ( i = 1 , \ldots , n - 1 ) ,
$$

then $M [ a _ { i i } ( t ) ] = \lambda _ { i } ( i = 1 , . . . , n )$

The theorem is valid for $n = 1$ . We prove it by induction. Assume that the theorem is true for $n - 1$ . For any $\varepsilon _ { n } > 0$ there exists a $T ( \varepsilon _ { n } , 0 )$ such that

$$
\begin{array} { r } { \exp \left\{ \lambda _ { i } t - \varepsilon _ { n } t \right\} \subseteq \| [ X ( t , 0 ) ] _ { i } \| \leq \exp \big \{ \lambda _ { i } t + \varepsilon _ { n } t \big \} , } \end{array}
$$

for $t \leq T ( \varepsilon _ { n } , 0 ) ( i = 1 , 2 , . . . , n - 1 )$ . Also we have

$$
\left| \int _ { 0 } ^ { t } a _ { i i } ( \tau ) d \tau - \lambda _ { i } t \right| \le \left| { \varepsilon } _ { n } { T } ( \varepsilon _ { n } , 0 ) \mathrm { f o r } 1 \equiv { T } ( \varepsilon _ { n } , 0 ) , \right.
$$

We must show that for a given $\delta _ { 1 } / 4 > \varepsilon _ { 1 } > 0$ there exists a $\overline { { T } } ( \varepsilon _ { 1 } , 0 )$ such that

$$
\left| \int _ { 0 } ^ { \varepsilon } a _ { n \pi } ( \tau ) \ d \tau - \lambda _ { n } t \right| \leq \varepsilon _ { 1 } t \qquad { \mathrm { f o r } } \qquad t \geq { \overline { { T } } } ( \varepsilon _ { 1 } , 0 ) .
$$

From(179) we obtain

$$
\left\{ \int _ { 0 } ^ { t } a _ { n n } ( \tau ) d \tau \right\} \ = \ | [ X _ { n } ( t , 0 ) ] _ { n } | \ \leq \| [ X ( t , 0 ) ] _ { n } \| < \exp \left\{ \lambda _ { n } t + \varepsilon _ { n } t \right\}
$$

for $t \geq T ( \varepsilon _ { n } , 0 )$ . By taking the logarithm we obtain

$$
\int _ { 0 } ^ { t } a _ { n n } ( \tau ) d \tau - \lambda t \leq \varepsilon _ { n } t \qquad \mathrm { f o r } \qquad t > T ( \varepsilon _ { n } , 0 ) .
$$

For any $\varepsilon _ { 1 } > 0$ and

$$
t \geq \operatorname* { m a x } \left[ T \Bigl ( \frac { \varepsilon _ { n } } { 2 } , 0 \Bigr ) , 4 \log \left( \sum _ { i = 1 } ^ { n } \frac { K _ { i } } { \varepsilon _ { n } } \right) \right] = R
$$

we can see that

$$
\int _ { 0 } ^ { t } a _ { n n } ( \tau ) ~ d \tau - \lambda t \geq - \varepsilon _ { 1 } t ,
$$

where $\pmb { \varepsilon } _ { 1 } , \pmb { \varepsilon } _ { 2 }$ are related by Lemma 1, and the $K _ { i }$ are defined by

$$
K _ { 1 } = 1 , \qquad K _ { j } = { \frac { 2 M } { \tilde { \partial } _ { j - 1 } } } + M \sum _ { i = 2 } ^ { j - 1 } \left( { \frac { 1 } { \tilde { \partial } _ { i - 1 } } } + { \frac { K _ { i } } { \tilde { \partial } _ { j - 1 } - \varepsilon _ { i } } } \right)
$$

for 2≤j≤n.

In fact,assume that there were a $t _ { 0 } \geq R$ such that

$$
\int _ { 0 } ^ { t _ { 0 } } a _ { n n } ( \tau ) d \tau < \lambda _ { 0 } t _ { 0 } - \varepsilon _ { 1 } t _ { 0 } .
$$

Then from (179) we should obtain

$$
\begin{array} { l } { 1 \le \left. [ X ( t , 0 ) ] _ { \pi } \right. \exp \left\{ - \lambda _ { \pi } t + \frac { \varepsilon _ { n } } { 2 } t \right\} } \\ { = \displaystyle \sum _ { j = 1 } ^ { n } \left. [ X _ { j } ( t ) ] _ { \pi } \right. \exp \left\{ \left( - \lambda _ { \pi } + \frac { \varepsilon _ { n } } { 2 } \right) t \right\} } \end{array}
$$

for $t \geq R \geq T ( \varepsilon _ { n } / 2 , 0 )$ . As a consequence of (182) we should have

$$
\int _ { 0 } ^ { t } a _ { n n } ( \tau ) d \tau < \lambda _ { n } t - \varepsilon _ { n } t _ { 0 } + ( t - t _ { 0 } ) M \qquad \mathrm { f o r } \qquad t \ge t _ { 0 } .
$$

By Lemmas 2 and 3 there would be inequalities

$$
| [ X _ { n - j + 1 } ( h ) ] | \leq K _ { j } \exp \left\{ \lambda _ { n } h - \varepsilon _ { j } h \right\}
$$

for any $h$ such that

$$
\left( \sum _ { i = 1 } ^ { n - 1 } a _ { i } \right) t _ { 0 } \leq h \leq b t _ { 0 } .
$$

By Lemma 1 this set of values would be non-void. By (181) and (182) an $h > R$ would exist such that

$$
\begin{array} { l } { { 1 \equiv \displaystyle \sum _ { j = 1 } ^ { n } K _ { j } \exp \left\{ \left( - \varepsilon _ { j } + \frac { \varepsilon _ { n } } { 2 } \right) h \right\} \equiv \displaystyle \sum _ { j = 1 } ^ { n } K _ { j } \exp \left\{ \left( - \frac { \varepsilon _ { n } } { 2 } \right) h \right\} } } \\ { { \mathrm { } \leq \displaystyle \sum _ { j = 1 } ^ { n } \exp \left\{ \left( - \frac { \varepsilon _ { n } } { 2 } \right) R \right\} \leq \displaystyle \frac { 1 } { 2 } . } } \end{array}
$$

This is contradictory. Hence we obtain Theorem 7 if we put $\overline { { T } } ( \varepsilon , 0 ) = R$

The solutions $X ( t , t _ { 0 } )$ for $0 \leq t _ { 0 } < \infty$ form a single-parameter family of fundamental solutions of (i63).Denote this family by $F ( s )$ We have $F ( t _ { 0 } ) = X ( t , t _ { 0 } )$ for $0 \leq s < \infty$ . The function $F ( s )$ has the set of strong characteristic exponents $[ \lambda _ { 1 } , \ldots , \lambda _ { n } ]$ uniformly with respect to $s$ if for any $s > 0$ there exists a $\pmb { T } ( \pmb \varepsilon )$ such that

$$
\frac { | \log | | [ X ( t + s , s ) ] _ { i } | | - \lambda _ { i } t | } { t } < \varepsilon
$$

for all $t \geq T ( \varepsilon )$ independently of $\pmb { s }$

Theorem 8: If the diagonal terms $a _ { 1 1 } ( t ) , \ldots , a _ { n n } ( t )$ possess the distinct mean values $\lambda _ { 1 } , \ldots , \lambda _ { n }$ , then the system (178) possesses strong characteristic exponents $[ \lambda _ { 1 } , \ldots , \lambda _ { n } ]$

This is equivalent to the statement that the system (163) admits $_ n$ independent solutions $\psi _ { i } ( t )$ such that for any $\varepsilon > 0$ there exist $m$ and $M$ having the property that

$$
m \exp \left\{ \lambda _ { i } t - \varepsilon t \right\} \leq \| \psi _ { i } ( t ) \| \leq M \exp \left\{ \lambda _ { i } t + \varepsilon t \right\} \qquad ( i = 1 , \dots , n
$$

where, with the mean value $\lambda _ { i }$ of $a _ { i i } ( t )$ ，

$$
\bar { S } _ { i } = \{ l ; l \leq i ; \lambda _ { l } > \lambda _ { i } \} , ~ S _ { i } = \{ l ; l \leq i , l \not \in \bar { S } _ { i } \} .
$$

Let $\psi _ { i k } ( t )$ be the kth component of the vector $\psi _ { i } ( t )$ . Define the components of $\psi _ { i } ( t )$ as follows ;

$$
\begin{array} { r l } & { \boldsymbol { \gamma } _ { i , k } ( t ) = 0 \quad ( k \geq i ) , } \\ & { \boldsymbol { r } _ { i , i } ( t ) = \exp \{ \displaystyle \int _ { 0 } ^ { t } a _ { i i } ( s ) d s \} , } \\ & { \boldsymbol { r } _ { i , k } ( t ) = \{ \displaystyle \int _ { 0 } ^ { t } \exp \{ \displaystyle \int _ { s } ^ { t } a _ { k k } ( s ) d s \} \cdot \sum _ { l = n } ^ { k + 1 } \psi _ { l , i } ( s ) a _ { k l } ( s ) d s \quad \quad ( k \in S _ { i } ) ,  } \\ & {  \boldsymbol { r } _ { i , k } ( t ) = \{ \displaystyle \int _ { - \infty } ^ { t } \exp \{ \displaystyle \int _ { s } ^ { t } a _ { k k } ( \sigma ) d \sigma \} \cdot \sum _ { l = n } ^ { k + 1 } \psi _ { l , i } ( s ) a _ { k l } ( s ) d s \quad \quad ( k \in \bar { S } _ { i } ) .  } \end{array}
$$

The theorem is true for $n = 1$ .Assume that it is true for $n - 1$ Then it is sufficient to show that for any $\varepsilon > 0$ there is an $M ( \mathfrak { s } )$ such that $| \psi _ { l , n } ( t ) | \leq M ( \varepsilon )$ exp $\{ \lambda _ { n } t + \varepsilon t \}$ for $t \geq 0$ Take $\eta > 0$ for $\lambda _ { n } - \lambda _ { 1 }$ $> 0$ such that $4 \eta < \mathrm { m i n } \left( \varepsilon , \lambda _ { n } - \lambda _ { 1 } \right)$ ，but for $\lambda _ { n } - \lambda _ { 1 } \leq 0$ such that $4 \eta < \varepsilon$ . Then,since $a _ { j j } ( t )$ has the mean value $\lambda _ { j }$ ，there is an $M ( \eta )$ such that

$$
\left| \int _ { 0 } ^ { t } a _ { j j } ( \tau ) d \tau - \lambda _ { n } t \right| < \eta t + \log M ( \eta ) \qquad ( j = 1 , \ldots , n ) ,
$$

$$
\sum _ { l = 2 } ^ { n } \vert \psi _ { l n } ( s ) \vert \cdot \vert a _ { n l } ( s ) \vert \leq M ( \eta ) \ \exp \ \{ \lambda _ { n } t + \eta t \} .
$$

According to whether $n \in { \overline { { S } } } _ { 1 }$ or $n \in S _ { 1 }$ we derive the following bounds for $\vert \psi _ { 1 n } ( t ) \vert$ .For $n \in \overline { S } _ { 1 }$ ，

$$
\begin{array} { c l l } { | \psi _ { 1 n } ( t ) | \displaystyle \equiv \int _ { \infty } ^ { t } M \exp { \left\{ \lambda ( t - s ) + 2 \eta s \right\} } \cdot M ( \eta ) \exp { \left\{ \lambda _ { n } s + \eta s \right\} } \cdot d s } & { } & { } \\ { \leq \displaystyle \frac { \exp { \left\{ \lambda _ { n } t + 3 \eta t \right\} } M ^ { 2 } ( \eta ) } { \eta } \leq \displaystyle \frac { M ^ { 2 } \exp { \left\{ \lambda _ { n } t + \varepsilon t \right\} } } { \eta } , } & { } \end{array}
$$

or for $n \in S _ { 1 }$ ，

$$
\begin{array} { l } { \displaystyle | \psi _ { 1 n } ( t ) | \leq \int _ { 0 } ^ { t } { M ( \eta ) \exp \left\{ \lambda _ { 1 } ( t - s ) + 2 \eta t \right\} \cdot M ( \eta ) \exp \left\{ \lambda _ { n } s + \eta s \right\} \cdot d } } \\ { \displaystyle \qquad \leq \frac { M ^ { 2 } ( \eta ) \exp \left\{ 3 \eta t + \lambda _ { n } t \right\} } { \eta } \leq \frac { M ^ { 2 } ( \eta ) \exp \left\{ \lambda _ { n } t + \varepsilon t \right\} } { \eta } . } \end{array}
$$

Consider the stability of the solution of the equation

$$
\frac { d x } { d t } = [ D + B ( t ) ] x + f ( t , x ) ,
$$

where (i) $\| f ( t , x _ { 1 } ) - f ( t , x _ { 2 } ) \| = 0 \left( \| x _ { 1 } - x _ { 2 } \| \right)$ when $\| x _ { 1 } \| , \| x _ { 2 } \|$ tend to zero,(ii) D= diag $( d _ { \scriptscriptstyle { 1 1 } } , \ldots , d _ { \scriptscriptstyle { n n } } )$ $( d _ { 1 1 } \leq d _ { 2 2 } \leqq \cdot \cdot \cdot \leq d _ { n n } )$ ， $d _ { \kappa k } < 0$ ， and (ii) if $\begin{array} { r } { \delta = \operatorname* { m i n } _ { \substack { d _ { i } \neq d _ { j j } } } | d _ { i } - d _ { j j } | } \end{array}$ ，then $\| B ( t ) \| < \delta / ( 1 6 n )$

Theorem 9: For $t = 0$ there exists in the $x \cdot$ -space a real $k \mathrm { . }$ dimensional manifold $S _ { k }$ containing the origin such that any solution $\phi$ of (183)with $\phi ( 0 )$ on the manifold $S _ { \kappa }$ tends to zero at an exponential rate of at least $d _ { \boldsymbol { k } \boldsymbol { k } } + ( \delta / 2 )$ .Moreover, the manifold $S _ { k }$ is differentiable if $\partial f / \partial x _ { i }$ exists and is continuous for $i = 1 , \ldots , n$ and $t \geq 0$

Let $j$ be the smallest integer such that $d _ { j + 1 , j + 1 } > d _ { k , k }$ and put

$$
\begin{array} { l } { { U _ { 1 } ( t ) = \mathrm { d i a g } \left[ \mathrm { e x p } \left( { d _ { 1 1 } } { t } \right) , \ldots , \mathrm { e x p } \left( { d _ { j j } } { t } \right) , 0 , \ldots , 0 \right] , } } \\ { { U _ { 2 } ( t ) = \mathrm { e x p } \left( { D t } \right) - { U _ { 1 } ( t ) } . } } \end{array}
$$

Consider $\boldsymbol { a } = ( a _ { 1 } , \ldots , a _ { k } , 0 , \ldots , 0 )$ ； then there exists a $\gamma > 0$ such that for $\| a \| < \gamma$ we may define a continuous vector-valued function $\boldsymbol { \vartheta } ( t , a )$ such that $\vartheta _ { i } ( 0 , a ) = a _ { i } \left( i \leq k \right)$ ， and the remaining components $\vartheta _ { i } ( 0 , a ) = y _ { i }$ ， $i > k$ ，define the desired $k \mathrm { . }$ -dimensional manifold.We have

$$
\begin{array} { c l c r } { { \displaystyle \vartheta ( t , a ) = U _ { 1 } ( t ) a + \displaystyle \int _ { 0 } ^ { t } U _ { 1 } ( t - s ) g ( s , \vartheta ( s , a ) ) \ d s } } \\ { { \displaystyle - \displaystyle \int _ { t } ^ { \infty } U _ { 2 } ( t - s ) g ( s , \vartheta ( s , a ) ) \ d s , } } \end{array}
$$

$$
g ( s , \vartheta ( s , a ) ) = B ( s ) \vartheta ( s , a ) + f ( s , \vartheta ( s , a ) ) .
$$

Choose $\gamma _ { 1 } > 0$ so that for $\| \vartheta ^ { i } ( s , a ) \| < \gamma _ { 1 } \left( i = 1 , \ldots , n \right)$ we have

$$
\lVert g ( s , \vartheta ^ { 1 } ( s , a ) ) - g ( s , \vartheta ^ { 2 } ( s , a ) ) \rVert \leq \frac { \delta } { 8 n } \lVert \vartheta ^ { 1 } ( s , a ) - \vartheta ^ { 2 } ( s , a ) \rVert .
$$

By the conditions (i) and (ii) this is possible.Put $\gamma = \gamma _ { 1 } / 2$ and solve (169) by successive approximation with $\mathcal { S } ^ { 0 } ( t , a ) = 0$ . Then we get

$$
\lVert \vartheta ^ { l + 1 } ( t , a ) - \vartheta ^ { l } ( t , a ) \rVert \leq \lVert a \rVert \exp \left\{ \left( d _ { k k } + \frac { \delta } { 2 } \right) t \right\} \bigg / 4 \iota .
$$

We see the existence of the solution $\boldsymbol { \vartheta } ( t , a )$ of (184) such that

$$
\lVert \vartheta ( t , a ) \rVert \equiv 2 \gamma \exp \left\{ \left( d _ { k k } + \frac { \delta } { 2 } \right) t \right\} .
$$

The convergence of $\vartheta ( 0 , a )$ follows from the uniform convergence and continuity of $\vartheta ^ { l } ( 0 , a )$

Theorem $_ { I 0 }$ :The conclusions of Theorem 9 hold when the condition (i) following the equation (183) is replaced by the weaker condition that $f ( t , x ) = 0 \left( \left\| x \right\| \right)$ as $\| { \boldsymbol x } \| \to 0$

Definition: The matrix $\pmb { { \cal A } } ( t ) \in { \cal M } _ { n }$ is said to be approximately similar to $\boldsymbol { B } ( t ) \in M _ { n }$ ，and written $A \approx B$ ，if，given any $\varepsilon \in 0$ ，there exists a $\boldsymbol { P } ( \varepsilon , t )$ such that $P ( \varepsilon , t ) , P ^ { - 1 } ( \varepsilon , t ) , \dot { P } ( \varepsilon , t ) \in M _ { n }$ and

$$
\| P ^ { - 1 } ( - \dot { P } + A ( t ) P ) - B ( t ) \| < \varepsilon .
$$

Approximate similarity has the following properties :

(i) The relation of approximate similarity is transitive and reflexive. (ii) The set of all matrices in $M _ { n }$ to which $\pmb { A } ( t )$ is approximately similar,written $E ( A )$ , is a closed set. (iii) For any $\pmb { A } \in \pmb { M } _ { n }$ the set $E ( A )$ contains at least one diagonal matrix. (iv）If $E ( A )$ contains a diagonal matrix of constant terms $\lambda _ { 1 } , . . . ,$ $\lambda _ { n }$ ，not necessarily distinct,then the system ${ \dot { \mathbf { x } } } = A ( t ) { \boldsymbol { x } }$ possesses the strong characteristic exponents $[ \lambda _ { 1 } , \ldots , \lambda _ { n } ]$ (v) By Perron's classical example, there exist $A , B \in M _ { n }$ such that $A \approx B$ and the systems $\dot { { \boldsymbol { x } } } = { \boldsymbol { A } } ( t ) { \boldsymbol { x } }$ and $\dot { y } = B ( t ) y$ possess different sets of characteristic exponents. (vi) Every constant matrix $\pmb { A }$ is approximately similar to a constant diagonal matrix where the diagonal terms are the real parts of the characteristic roots of det $| A - \lambda I |$ (vii)Every periodic matrix $P ( t )$ is approximately similar to a constant diagonal matrix where the diagonal terms are just the characteristic exponents of the system ${ \dot { x } } = P ( t ) x$

# TOPOLOGY OF THE STABILITY DOMAIN

# 16.18LINEAR OPERATORS

The statement $f \colon A \to B$ means that $f$ is a function whose domain is $\pmb { A }$ ，and whose range is contained in $\pmb { B }$ ; i.e., for every $a \in A$ ，the function $f$ assigns an element $f ( a ) \in B$ .If $f \colon A \to B$ and $g \colon B \to C$ ， then the mapping $g f \colon A \to C$ is defined by $( g f ) ( a ) = g ( f ( a ) )$ for $a \in A$ . If $f \colon A \to B$ and $C \subseteq A$ ，the symbol $f ( C )$ is used for the set of all elements of the form $f ( c )$ where $c \in C$ .If $f \colon A \to B$ and $\boldsymbol { D } \subseteq B$ ，then $f ^ { - 1 } ( D )$ is defined as $\{ x \colon x \in A , f ( x ) \in D \}$ ，which means that the set of $x$ such that $x \in A$ ， $f ( x ) \in D$ . The set $f ( C )$ is called the image of $C$ and the set $f ^ { - 1 } ( D )$ the inverse image of $D$ .If $f \colon A \to A$ and $C \subseteq A$ ，then $c$ is said to be invariant under $f$ for $f ( c ) \subseteq C$ . The function $f$ is said to map $\pmb { A }$ onto $B$ if $f ( A ) = B$ and into $\pmb { B }$ if $f ( A ) \subseteq B$

A group is a set $G$ together with a mapping $\mu \colon G \times G \to G$ ，called multiplication $\mu ( a , b ) = a b$ ,which has the properties (i) $a ( b c ) = ( a b ) c$ ， $a , b , c \in G$ ； (ii) there is an element $e$ in $G$ ，called the identity of $G$ such that $a e = e a = a$ for every $^ a$ in $G$ ； and (ii) to each $^ a$ in $G$ there corresponds an element $a ^ { - 1 }$ called the inverse of $^ { a }$ (Section 4.2),such that $a a ^ { - 1 } = a ^ { - 1 } a = e$ .A commutative group is a group in which the combination law $a b = b a$ holds.In a commutative group the binary operation $\mu$ is written $\mu ( a , b ) = a + b$ and is called addition.The group is then called an additive group.

A mapping $h \colon A \to B$ between groups $\pmb { A }$ and $\pmb { B }$ is called homomorphic if $h ( a , b ) = h ( a ) h ( b )$ . A one-to-one homomorphism is called an isomorphism.If $h \colon A \to B$ is an isomorphism and if $h ( A ) = B$ ， then $\pmb { A }$ and $\pmb { B }$ are said to be isomorphic,or $\pmb { A }$ is said to be isomorphic to $\pmb { B }$ . An isomorphism of a group $G$ to itself is an automorphism of $G$ .If $a \in G$ ， then the transformation $h _ { \alpha } \colon G \to G$ defined by $h _ { a } ( x ) =$ $a ^ { - 1 } x a$ is an automorphism of $G$ and is called the conjugation of $G$ by $^ a$ . A subgroup $\pmb { A }$ of a group $G$ is called invariant in $G$ if $x ^ { - 1 } A x = A$ for every $x$ in $G$ . The cosets,that is,sets of the form $\boldsymbol { A x }$ or $x A$ ，of an invariant subgroup $\pmb { A }$ form a group under the operation $( A x ) ( A y )$ $= A x y$ . This group of cosets of $\pmb { A }$ is called the factor group of $G$ by $\pmb { A }$ and denoted by $G / A$ .If $\pmb { A }$ is Abelian，then every subgroup is invariant.

A ring is an additive group $\pmb R$ together with a mapping $r \colon R \times R$ $ R$ which has the properties : (i) $( a b ) c = a ( b c )$ ； (ii) $a ( b + c ) = a b$ $+ \ b c$ ； and (iii) $( b + c ) a = b a + c a$ ，where the binary operation $r$ is written $r ( a , b ) = a b$ and is called multiplication.A field is a commutative ring in which the nonzero elements form a group under multiplication. The unit of this group in a field is written as 1 instead of $^ e$ (Sections 4.2, 4.26, 4.27, 4.28, 4.29).

A linear vector space, linear space,or vector space over a field $\Phi$ is an additive group $\mathfrak { X }$ together with an operation $m \colon \Phi \times { \mathfrak { X } } \to { \mathfrak { X } }$ written as $m ( { \boldsymbol { \alpha } } , x ) = \alpha x$ ，which satisfies the conditions

$$
\begin{array} { r l r l } & { \alpha ( x + y ) = \alpha x + \alpha y , } & & { \alpha \in \Phi , } \\ & { ( \alpha + \beta ) x = \alpha x + \beta y , } & & { \alpha , \beta \in \Phi , } & & { x \in \mathfrak { X } , } \\ & { \alpha ( \beta x ) = ( \alpha \beta ) x , } & & { \alpha , \beta \in \Phi , } & & { x \in \mathfrak { X } , } \\ & { 1 x = x , } & & { x \in \mathfrak { X } . } \end{array}
$$

(Bourbaki, 1953, 1955; Riesz and Nagy, 1955 ; Kothe, 1960； Kelley,Namioka et al., 1963； Berge,1963； Kantorovich and Akimov, 1964;Yosida,1966；Schaefer,1971).

A vector is an element of a vector space.A scalar is an element of the coefficient feld $\Phi$ . A sum $\alpha x + \beta y + \cdot \cdot \cdot + \gamma z$ where $\alpha , \beta , \ldots , \gamma$ are scalars is called a linear combination of the vectors $x , y , \ldots , z .$ The subspace spanned by a given set $\boldsymbol { \varepsilon }$ is the set of all linear combinations of elements of $\boldsymbol { \varepsilon }$ . The subspace spanned by a set $\pmb { B }$ in a linear space $\mathfrak { X }$ is denoted by sp $\left( B \right)$ .If $\mathfrak { X }$ is a linear topological space,the closure of sp $( B )$ denoted by ${ \overline { { \mathtt { s p } } } } \left( B \right)$ is called the closed linear manifold spanned by $B$ .Note, sp $( B )$ is a linear space. If sp $( B ) = { \mathfrak { X } }$ ， then the set $\pmb { B }$ is called fundamental.

A function $_ T$ is said to be a linear operator or a linear transformation if its domain and range are linear spaces over the same field $\Phi$ ， and if $T ( x + y ) = T x + T y$ ， $T ( \alpha x ) = \alpha T x$ for every $\alpha \in \Phi$ and for every pair $x , y$ of vectors in the domain of $_ { T }$ . Thus a linear transformation on a linear space $\mathfrak { X }$ is a homomorphism on the additive group $\mathfrak { X }$ which commutes with the operations of multiplication by scalars. If $T \colon { \mathfrak { X } }  { \mathfrak { Y } }$ and $U \colon { \mathfrak { V } } \to { \mathfrak { Z } }$ are linear transformations,and ,,3 are linear spaces over the same field $\Phi$ ， then the product ${ \pmb U } { \pmb T }$ ， defined by $( U T ) x = U ( T x )$ , is a linear transformation which maps $\mathfrak { X }$ into 8. If $_ T$ is a linear operator on $\mathfrak { X }$ to $\mathfrak { X }$ ，it is said to be a linear operator in $\mathfrak { X }$ . For such operators the symbol $T ^ { 2 }$ is used for $_ { T T }$ ，and, inductively, $T ^ { n }$ for $_ { T ^ { n - 1 } T }$ . The symbol $\pmb { I }$ is used for the identity operator, $I x = x$ ，and $o$ for the zero operator, $O x = O$ If $P ( \lambda ) =$ $\alpha _ { 0 } + \alpha _ { 1 } \lambda + \dotsb + \alpha _ { n } \lambda ^ { n }$ is a polynomial, then the symbol $P ( T )$ is used for the operator $\alpha _ { 0 } I + \alpha _ { 1 } T + \cdot \cdot \cdot + \alpha _ { n } T ^ { n }$ .If $T , U$ are both linear on $\mathfrak { X }$ to the linear space $\mathfrak { V }$ ， then the sum $T + U$ ，defined as $( T + U ) x$ $= T x + U x .$ is also linear on $\mathfrak { X }$ to $\mathfrak { Y }$ .If $_ T$ is linear and $\alpha$ is a scalar, the operation $_ { \alpha T }$ defined by $( \alpha T ) x = \alpha ( T x )$ is also linear. If $\mathfrak { X }$ and 9 are linear spaces over the same field $\Phi$ , the set of all linear operators from $\mathfrak { X }$ to $\mathfrak { Y }$ is a linear space over $\Phi$ under the operations $T + U$ and $_ { \alpha T }$ If ${ \mathfrak { X } } = { \mathfrak { Y } }$ ， this set is also a ring under the operations $T + U$ and TU.A linear operator $\boldsymbol { \varepsilon }$ in $\mathfrak { X }$ is said to be a projection or a projection in $\mathfrak { X }$ if $E ^ { 2 } = E$ . A projection is sometimes called an idempotent operator.An element in $x$ in a ring is called idempotent if $x ^ { 2 } = x$ and nilpotent if $x ^ { n } = 0$ for some positive integer $_ n$ .If $\mathfrak { X }$ is a vector space, if $A \subseteq { \mathfrak { X } }$ ，and if $\alpha$ is a scalar,then the symbol $\alpha A$ is written for the set of elements of the form $_ { \alpha x }$ with $x$ in $\pmb { A }$ .If $A , B \subseteq { \mathfrak { X } }$ and $x \in { \mathfrak { X } }$ ， then, since $\mathfrak { X }$ is an additive group,the symbols $A + B$ ， $A - B$ ，and $x + A$ have already been assigned definite meanings.The vector space $\mathfrak { X }$ is said to be the direct sum of the vector spaces ${ \mathfrak { M } } _ { i } ( i = 1 , 2 , \dots , n )$ ； symbolically $\mathfrak { X } = \mathfrak { M } _ { i } \oplus \dots \oplus \mathfrak { M } _ { n }$ ,if the spaces ${ \mathfrak { M } } _ { i }$ are subspaces of $\mathfrak { X }$ with the property that every $x$ in $\mathfrak { X }$ has a unique representation (Section 4.29) $x = m _ { 1 } + \cdots + m _ { n }$ with $m _ { i } \in \mathfrak { M } _ { i }$ $( i = 1 , 2 , \ldots , n )$ The map $E _ { i } \colon \mathfrak { X } \longrightarrow \mathfrak { M } _ { i }$ ， given by the equation $E _ { i } x = m _ { i }$ ， is a projection of $\mathfrak { X }$ onto ${ \mathfrak { M } } _ { i }$

If $\mathfrak { X } _ { 1 } , \ldots , \mathfrak { X } _ { n }$ are vector spaces over the field $\Phi$ ， the set $\mathfrak { X } = \mathfrak { X } _ { 1 } \times$ $\mathfrak { X } _ { 2 } \times \cdots \times \mathfrak { X } _ { n }$ is a vector space under the operations defined by the equations

$$
\begin{array} { c } { { [ x _ { 1 } , \ldots , x _ { n } ] + [ y _ { 1 } , \ldots , y _ { n } ] = [ x _ { 1 } + y _ { 1 } , \ldots , x _ { n } + y _ { n } ] , } } \\ { { { } } } \\ { { \alpha [ x _ { 1 } , \ldots , x _ { n } ] = [ \alpha x _ { 1 } , \ldots , \alpha x _ { n } ] . } } \end{array}
$$

The space $\mathfrak { X }$ is the direct sum of the spaces ${ \mathfrak { M } } _ { i }$ ，where ${ \mathfrak { M } } _ { i }$ is the set of those vectors $[ x _ { 1 } , \ldots , x _ { n } ]$ in $\mathfrak { X }$ with $x _ { j } = 0$ for $j \neq i$ . Since there is a one-to-one linear map between the spaces ${ \mathfrak { M } } _ { i }$ and $\mathfrak { X } _ { i }$ ，the space $\mathfrak { X }$ is often called the direct sum of the spaces $\mathfrak { X } _ { 1 } , \ldots , \mathfrak { X } _ { n }$

If $\mathfrak { M }$ is a subspace of the vector space $\mathfrak { X }$ over the field $\Phi$ , the factor space $\mathfrak { X } / \mathfrak { M }$ is the set of cosets of $\mathfrak { M }$ , i.e.,the set of sets of the form $x + { \mathfrak { M } }$ with $x \in { \mathfrak { X } }$ . The algebraic operations in $\mathfrak { X } / \mathfrak { M }$ are defined by

$$
\begin{array} { r l } & { \mathfrak { H } ) + ( y + \mathfrak { M } ) = ( x + y ) + \mathfrak { M } , \qquad x , y \in \mathfrak { X } , } \\ & { \alpha ( x + \mathfrak { M } ) = \alpha x + \mathfrak { M } , \qquad \alpha \in \Phi , \qquad x \in \mathfrak { X } . } \end{array}
$$

With these operations the factor space ${ \mathfrak { X } } / { \mathfrak { M } }$ is a linear vector space. The mapping of $\mathfrak { X }$ onto $\mathfrak { X } / \mathfrak { M }$ ， defined by $x  x + \mathfrak { M }$ ，is called the natural homomorphism of $\mathfrak { X }$ onto ${ \mathfrak { X } } / { \mathfrak { M } }$ . It is a linear transformation. A linear functional is a linear transformation whose range is in the coefficient field (Section 15.10).

If $\pmb R$ is a ring then a subset $R _ { 1 } \subseteq R$ is called a subring if the elements in $\pmb { R } _ { 1 }$ form a ring under the operations defined in $\pmb R$ . A subring $\pmb { I }$ of $\pmb R$ is called a right ideal of $\pmb R$ if it is such that $I x \subseteq I$ ， $x \in R$ and $( 0 ) \neq ( I ) \neq R$ .The definition of left ideal is similar. If $\pmb { I }$ is both a right and a left ideal of $\pmb R$ it is a two-sided ideal.

A set $\boldsymbol { \cal X }$ is said to be an algebra over a field $\Phi$ ，if $X$ is a ring (Section 2.5) as well as a vector space over $\Phi$ and if $\alpha ( x y ) = ( \alpha x ) y$ $= x ( \alpha y )$ where $x , y \in X$ ， $\alpha \in \Phi$ ． A right [left, two-sided] ideal in an algebra is a right [left,two-sided] ideal in the ring sense which is also closed under multiplication by scalars.If $\Phi$ is the field of complex numbers and if in the algebra $X$ there is a single-valued map $x \to x ^ { * }$ with $( x + y ) ^ { * } = x ^ { * } + y ^ { * }$ ， $( \lambda x ) ^ { * } = { \bar { \lambda } } x ^ { * }$ ， $( x ^ { * } ) ^ { * } = x .$ ， $( x y ) ^ { * } = y ^ { * } x ^ { * }$ ， then we say that $X$ is an algebra with involution and $x ^ { * }$ is called the adjoint of $x$ (Sections 4.5, 4.27).

An arbitrary given set function $\mu$ can be used to define a nonnegative set function $v ( \mu )$ called the total variation of $\mu$ (Sections 2.1, 15.9). The set function $v ( \mu )$ is defined so as to be equal to $\mu$ if $\mu$ itself is nonnegative,to be additive if $\mu$ is additive,and to be bounded if $\mu$ is bounded. Let $\mu$ be a set function defined on the field $\scriptstyle \sum$ of subsets of a set $s$ .Then for every $\boldsymbol { \varepsilon }$ in $\scriptstyle \sum$ the total variation of $\pmb { \mu }$ on $\boldsymbol { \varepsilon }$ ， denoted by $v ( \mu , E )$ , is defined as sup $\scriptstyle \sum _ { i = 1 } ^ { n } | f ( E _ { i } ) |$ where the supremum is taken over all finite sequences $\{ E _ { i } \}$ of disjoint sets in $\displaystyle \sum$ with $E _ { i } \subseteqq$ $\boldsymbol { \varepsilon }$ .If $\mu$ is nonnegative and additive then $v ( \mu , E ) = \mu ( E )$ .A set is a null set if and only if it is a subset of some measurable set $\boldsymbol { \varepsilon }$ such that $v ( \mu , E ) = 0$ .Similarly a null space is defined.

A family $\pmb { \tau }$ of subsets of a set $\pmb { X }$ is called a topology in $X$ if $\tau$ contains the void set ${ \mathfrak { g } }$ ，the set $X$ , the union of every one of its subfamilies,and the intersection of every one of the finite subfamilies. The pair $( X , \tau )$ is called a topological space；but sometimes,if $\boldsymbol { \tau }$ is understood, we refer to $X$ as a topological space.A family $\beta$ of subsets of $\boldsymbol { \cal X }$ is said to be a base for the topology if $\beta \subseteq \tau$ and if every set in $\tau$ is the union of some subfamily of $\beta$

The closure $\bar { A }$ of a set $\pmb { A }$ is the intersection (Section 2.1） of all closed sets containing $\pmb { A }$ . The set of points in $\bar { A }$ and not in the interior of $\pmb { A }$ is called the boundary of $\pmb { A }$ . If $Y \subseteq X$ and $\boldsymbol { \tau }$ is a topology for $X$ ，then the topology $\tau _ { Y } = \{ A : A = B \cap Y , B \in \tau \}$ is called the natural relative topology of $\boldsymbol { Y }$ generated by $\boldsymbol { \tau }$ . A subset of $X$ is called conditionally compact if its closure is compact (Section 15.1) in its relative topology (Section 2.1).

If $( X , \tau )$ and $( Y , \tau _ { 1 } )$ are topological spaces,and $f \colon X \to Y$ ，then $f$ is continuous if $f ^ { - 1 } ( A ) \in \tau$ for every $\pmb { A }$ in $\tau _ { 1 }$ . In other words, a mapping between topological spaces is continuous if the inverse image of every open set is open.The function $f$ is said to be continuous at the point $x$ if to every neighborhood $U$ of $f ( x )$ there corresponds a neighborhood

$V$ of $x$ with $f ( V ) \subseteq U$ If $f$ is a continuous one-to-one map of $\pmb { X }$ onto $\pmb { Y }$ and if the inverse function $f ^ { - 1 }$ is also continuous, then $f$ is called a homeomorphism or a topological isomorphism,and the spaces $\boldsymbol { \cal X }$ and $\pmb { Y }$ are said to be homeomorphic. If $f$ and $f ^ { - 1 }$ admit derivatives up to an infinite order, then the homeomorphism is called a diffeomorphism.

A topological space $X$ is a Hausdorff space if it has the properties (a) and (b) listed below. It is a regular space if it has the properties (a) and (c),a normal space if it has the properties (a) and (d): (a) Sets consisting of single points are closed. (b) For every pair of distinct points $x$ and $y$ ， there are disjoint neighborhoods of $x$ and $_ { y }$ (c) For every closed set $\pmb { A }$ ， and every $x \notin A$ ， there are disjoint neighborhoods of $\pmb { A }$ and $x$ (d) For every pair of disjoint closed sets $\pmb { A }$ and $\pmb { B }$ ，there are disjoint neighborhoods of $\pmb { A }$ and $\pmb { B }$

Two sets are disjoint if their intersection or product is void.

A covering of a set $\pmb { A }$ in a topological space $X$ is a family of open sets whose union contains $\pmb { A }$ . The space $X$ is said to be compact (Sections 2.1,15.1) if every covering of $\boldsymbol { \cal X }$ contains a finite subset that is also a covering.A compact Hausdorff space is normal.

Let $X$ be a set and let $\rho$ be a real function on $X \times X$ such that (i) $\rho ( x , y ) \geq 0$ (ii) $\rho ( x , y ) = 0$ if and only if $x = y$ ，(iii) $\rho ( x , y ) = \rho ( y , x )$ ， and (iv) $\rho ( x , y ) \cong \rho ( x , z ) + \rho ( z , y )$ . Then $\rho$ is called a metric. Sets of the form $S ( x , \varepsilon ) = \{ y ; \rho ( x , y ) < \varepsilon \}$ are called spheres in $X$ . The sphere $S ( x , \varepsilon )$ has $x$ for a center and $\varepsilon$ for a radius. The metric topology in $\boldsymbol { X }$ is the smallest topology containing the spheres. The set $X$ with its metric topology is called a metric space. If $\boldsymbol { \cal X }$ is a topological space such that there exists a metric whose topology is the same as the original topology，we say that $X$ is metrizable. If $\pmb { A }$ and $\pmb { B }$ are subsets of a metric space, let

$$
\rho ( A , B ) = \operatorname* { i n f } _ { a \in A , b \in B } \rho ( a , b ) .
$$

If $\pmb { A }$ is a subset of a metric space, the $\varepsilon \cdot$ -neighborhood of $\pmb { A }$ is the set $S ( A , \varepsilon ) = \{ x ; \rho ( A , x ) < \varepsilon \}$ . The diameter of a set $\pmb { A }$ ， denoted by $\delta ( A )$ ， is the number $\textstyle \operatorname* { s u p } _ { a , b \in A } \rho ( a , b )$ . A metric space is normal.

A sequence $\left\{ a _ { n } \right\}$ in a topological space is said to converge to a point $\pmb { a }$ in the space if every neighborhood of $^ { a }$ contains all but a finite number of points $a _ { n }$ ，that is, $a _ { n } \to a$ or $\scriptstyle \operatorname* { l i m } _ { n \to \infty } a _ { n } = a$ . A sequence $\left\{ a _ { n } \right\}$ is said to converge if $a _ { n } \to a$ for some $^ { a }$ . A sequence $\left\{ a _ { n } \right\}$ ina metric space is a Cauchy sequence if $\begin{array} { r } { \operatorname* { l i m } _ { m , n  \infty } \rho ( a _ { m } , a _ { n } ) = 0 } \end{array}$ .If every Cauchy sequence is convergent, then a metric space is said to be complete.A set is called dense in a topological space $X$ ,if its closure is $X$ . It is said to be nowhere dense if its closure does not contain any open set.A space is separable if it contains a denumerable dense set. (Section 2.1).

A mapping $f \colon X \to Y$ between metric spaces is said to be uniformly continuous on $X$ , if to every $\varepsilon > 0$ there corresponds a $\delta > 0$ such that $\rho ( x , x ^ { \prime } ) < \delta$ implies $\rho [ f ( x ) , f ( x ^ { \prime } ) ] < \varepsilon$ Let $X$ and $\pmb { Y }$ be metric spaces, and $Y$ be complete. If $f \colon A \to Y$ is uniformly continuous on the dense subset $\pmb { A }$ of $X$ ，then $f$ has a unique continuous extension $g \colon X \to Y$ . This unique extension is uniformly continuous on $X$ If $f \colon X \to Y$ is a continuous mapping between metric spaces,and if $X$ is compact, then $f$ is uniformly continuous.

A group $G$ is said to be a topological group if (i) $G$ is a Hausdorff space,and (i) the mapping $( x , y ) \to x y ^ { - 1 }$ of $G \times G$ into $G$ is continuous.A linear space $\mathfrak { X }$ is said to be a linear topological space if $\mathfrak { X }$ is a commutative topological group under addition, and if the mapping $( \alpha , x ) \to \alpha x$ of $\Phi \times { \mathfrak { X } }$ into $\mathfrak { X }$ is continuous.

A Fréchet space,or an $\pmb { F }$ -space,or a space of type $\pmb { F }$ ，is a linear space $\mathfrak { X }$ which is also a metric space such that: (i) the metric $\rho$ in $\mathfrak { X }$ is invariant, i.e., $\rho ( x , y ) = \rho ( x - y , 0 )$ ， (ii) the mapping $( \alpha , x ) \to \alpha x$ of $\Phi \times { \mathfrak { X } } \to { \mathfrak { X } }$ is continuous in $\alpha$ for each $x$ ，and continuous in $x$ for each $_ { \alpha }$ ,and (ii) the metric space $\mathfrak { X }$ is complete. The symbol $\| { \boldsymbol { x } } \|$ , called the norm of $x$ , is written for $\rho ( x , 0 )$ . We see that $\rho ( x , y ) \cong \rho ( x , z ) \ + \quad$ $\rho ( z , y )$ and $\rho ( x , y ) = 0$ if and only if $x = y$ ,and that $\rho ( x , y ) = \rho ( y , x )$ are equivalent to the properties $\| x + y \| \leq \| x \| + \| y \| , \| x \| = 0$ if and only if $x = 0$ and $\| - x \| = \| x \|$ . Thus an $\pmb { F }$ -space is a linear space on which there is a nonnegative function $\| x \|$ with these latter three properties and where,in addition, the properties (ii) and (ii) hold with reference to the metric function $\rho$ defined by $\rho ( x , y ) = \| x - y \|$ .For each $^ { a }$ in the set $\pmb { A }$ , let $T _ { \alpha }$ be a continuous linear map of an $F$ -space $\mathfrak { X }$ into an ${ \pmb F } .$ -space 9.If for each $x$ in $\mathfrak { X }$ the set $\{ T _ { \alpha } x ; a \in A \}$ is bounded, then $\begin{array} { r } { \operatorname* { l i m } _ { x \to 0 } T _ { \alpha } x = 0 } \end{array}$ uniformly for $a \in A$ .An ${ \pmb F } .$ -space is a linear topological space.A linear mapping of one ${ \pmb F }$ -space into another is continuous if and only if it maps bounded sets into bounded sets.

A linear space $\mathfrak { X }$ is a normed linear space or a normed space,if to each $x \in { \mathfrak { X } }$ there corresponds a real number $\| { \boldsymbol { x } } \|$ called the norm of $x$ satisfying (i) $\| 0 \| = 0 ; \| x \| > 0$ ， $x \neq 0$ ； (ii) $\| x + y \| \leq \| x \| + \| y \|$ ， ） $\mathfrak { c } , \mathfrak { y } \in \mathfrak { X }$ ; and (ii) $\| \alpha x \| = \| \alpha \| \cdot \| x \|$ ， $\alpha \in \Phi$ ， $x \in { \mathfrak { X } }$ . The zero element is called the origin of $\mathfrak { X }$ ,and the closed unit sphere is the set $\{ x : \| x \| \leq 1 \}$ A complete normed linear space,a space of type $B$ ，ora $\pmb { B }$ -space or a Banach space, is a normed linear space that is complete in its norm topology． A $B .$ -space is an ${ \pmb F } .$ -space in which the identity $\| \alpha x \| =$ $\| \alpha \| \cdot \| x \|$ is satisfied. This terminology will be used in future chapters.

The bound or norm of a linear map between normed linear space is $\mathsf { s u p } _ { \left| x \right| \leq 1 } \left\| T x \right\|$ ，denoted by $\| T \|$ . A linear map between normed linear spaces is continuous if and only if it is bounded. Let ${ \mathfrak { X } } , { \mathfrak { Y } }$ be $\pmb { B } .$ -spaces and $\{ T _ { \mathfrak { n } } \}$ a sequence of bounded linear operators on $\mathfrak { X }$ to $\mathfrak { Y }$ . Then the limit $\begin{array} { r } { T x = \operatorname* { l i m } _ { n \to \infty } T _ { n } x } \end{array}$ exists for every $x$ in $\mathfrak { X }$ if and only if (i) the limit $_ { T x }$ exists for every $x$ in a fundamental set, and (ii) for each $x$ in $\mathfrak { X }$ the supremum $\mathsf { s u p } _ { n } \| T _ { n } x \| < \infty$ ，i.e.，the least upper bound，is bounded. When the limit $_ { T x }$ exists for each $x$ in $\mathfrak { X }$ ， the operator $T$ is bounded and $\begin{array} { r } { \Vert T \Vert < \operatorname* { l i m } \operatorname* { i n f } _ { n  \infty } \Vert T _ { n } \Vert \leq \mathsf { s u p } _ { n } \Vert T _ { n } \Vert < \infty } \end{array}$

If $\mathfrak { X }$ and $\mathfrak { V }$ are linear topological spaces， then the symbol $B ( { \mathfrak { X } } , { \mathfrak { Y } } )$ is used for the linear space of all linear continuous maps of $\mathfrak { X }$ into $\mathfrak { Y }$ . The linear space ${ \mathfrak { X } } ^ { * }$ , denoted by $B ( { \mathfrak { X } } , \Phi )$ , is called the conjugate space, adjoint space,or dual space of $\mathfrak { X }$ . The elements of $\mathfrak { X } ^ { * }$ are the continuous linear functionals on $\Phi$ (Section 15.9).

If $\mathfrak { X }$ and $\mathfrak { Y }$ are normed linear spaces, and if $\mathfrak { Y }$ is complete, then the linear space $B ( { \mathfrak { X } } , { \mathfrak { Y } } )$ with the norm just defined is a $B$ -space.

Let a real function $p$ on the real linear space $\mathfrak { X }$ satisfy

$$
\begin{array} { c } { { p ( x + y ) \leq p ( x ) + p ( y ) , \qquad p ( \alpha x ) = \alpha p ( x ) ; } } \\ { { \alpha \geq 0 , \qquad x , y \in \mathfrak { X } . } } \end{array}
$$

Let $f$ be a real linear functional on a subspace $\mathfrak { V }$ of $\mathfrak { X }$ with $f ( x ) \leq p ( x )$ ， $x \in \mathfrak { Y }$ . Then there is a real linear functional $F$ on $\mathfrak { X }$ for which $F ( x ) =$ $f ( x ) , x \in { \mathfrak { V } } ; F ( x ) \leq p ( x ) , x \in { \mathfrak { X } }$

An isomorphism between two normed linear spaces $\mathfrak { X }$ and $\mathfrak { Y }$ isa one-to-one continuous linear map $T : { \mathfrak { X } } \to { \mathfrak { Y } }$ with $T { \mathfrak { X } } = { \mathfrak { Y } }$ . When such an isomorphism exists,the spaces $\mathfrak { X }$ and $\mathfrak { V }$ are called equivalent. An isometric isomorphism between two normed linear spaces $\mathfrak { X }$ and $\mathfrak { V }$ is an isomorphism $T$ between $\mathfrak { X }$ and $\mathfrak { Y }$ for which $\| T x \| = \| x \|$ . When such a $_ { T }$ exists,the spaces are said to be isometrically equivalent,or isometrically isomorphic.Let $\mathfrak { X }$ be a normed linear space and $\mathfrak { X } ^ { \ast \ast }$ the conjugate of the $\pmb { B }$ -space ${ \mathfrak { X } } ^ { * }$ . The mapping $\kappa \colon x \to { \hat { x } }$ of $\mathfrak { X }$ into ${ \mathfrak { X } } ^ { * * }$ , defined by ${ \hat { x } } x ^ { * } = x ^ { * } x$ for $x ^ { * }$ in $\mathfrak { X } ^ { * }$ , is called the natural embedding of $\mathfrak { X }$ into $\mathfrak { X } ^ { * * }$ . The range of $\kappa$ is denoted by $\boldsymbol { \hat { \mathfrak { X } } }$ . The natural embedding of a normed linear space $\mathfrak { X }$ into its second conjugate is an isometric isomorphism between $\mathfrak { X }$ and $\boldsymbol { \hat { \mathfrak { X } } }$

A subset $K \subseteq C ( S )$ is said to be equicontinuous if to every $\varepsilon > 0$ and every $s \in S$ there corresponds a neighborhood $N = N ( s )$ of $\pmb { s }$ with

$$
\operatorname* { s u p } _ { f \in K , t \in N } \| f ( s ) - f ( t ) \| < \varepsilon .
$$

Let $s$ be compact, then a set in $C ( S )$ is conditionally compact if and only if it is bounded and equicontinuous.

A set $C$ in a linear space is said to be convex if $\alpha x + ( 1 - \alpha ) y \in C$ whenever $x , y \in C$ and $0 \leq \alpha \leq 1$ .Let $C$ be a convex subset of $E ^ { k }$ ， a $k$ -dimensional Euclidean space,and $M$ be a function defined on $C$ and having values that are either real numbers or $+ \infty$ . We call $M$ convex if for any $u , v \in C$ we have

$$
M [ \alpha u + ( 1 - \alpha ) v ] \leq \alpha M ( u ) + ( 1 - \alpha ) M ( v )
$$

whenever $0 \leq \alpha \leq 1$

A topological space $R$ is said to have the fixed-point property (Sections 25.1-25.9; Poincaré,1912) if for every continuous mapping $T \colon R \to R$ there exists a $p \in R$ with $p = T ( p )$ .Brouwer's fixed-point theorem states that the closed unit sphere of $E ^ { n }$ has the fixed-point property (Section 25.4). A linear topological space is said to be locally convex if it possesses a base for its topology consisting of convex sets. A compact convex subset of a locally convex linear topological space has the fixed-point property. This is called Schauder's theorem (Dunford and Schwartz, 1958). Kolesov (1969) discussed the stability in connection with Schauder's theorem.

A space $B V ( I )$ is defined for an interval $\pmb { I }$ and consists of all scalar functions on $\pmb { I }$ that are of bounded variation (Section 2.1).A function $f \in B V ( I )$ is said to be absolutely continuous if for each $\varepsilon > 0$ there exists a $\delta > 0$ such that

$$
\sum _ { i = 1 } ^ { n } \| f ( b _ { i } ) - f ( a _ { i } ) \| < \varepsilon
$$

wherever $( a _ { i } , b _ { i } ) ( i = 1 , 2 , \dots , n )$ are nonoverlapping subintervals of $\pmb { I }$ with $\textstyle \sum _ { i = 1 } ^ { n } \| b _ { i } - a _ { i } \| < \delta$ .The space $A C ( I )$ is defined for an interval $\pmb { I }$ and consists of all absolutely continuous functions on $\pmb { I }$

A Hilbert space is a linear vector space $\mathfrak { L }$ over the field $\Phi$ of complex numbers, together with a complex function $( \cdot , \cdot )$ defined on $\mathcal { \tilde { V } } \times \mathcal { \tilde { Q } }$ by the following properties :

$( x , x ) = 0$ if and only if $x = 0$ ； $( x , x ) \geq 0 , \quad x \in \mathfrak { H } ;$ (ii) (iv) $\begin{array} { r l } & { ( x + y , z ) = ( x , \bar { z } ) + ( y , z ) , \quad x , y , z \in \mathfrak { S } ; } \\ & { ( \alpha x , y ) = \alpha ( x , y ) , \quad \alpha \in \Phi , \quad x , y \in \mathfrak { S } ; } \\ & { ( x \mathbin { \lrcorner } \smile \omega , \lrcorner \bullet 1 . } \end{array}$ (v) $( x , y ) = ( y , x )$ ； (vi）If $x _ { n } \in \mathfrak { H } \left( n = 1 , 2 , \ldots \right)$ , and if $\begin{array} { r } { \operatorname* { l i m } _ { n , m  \infty } ( x _ { n } - x _ { m } , x _ { n } - x _ { m } ) } \end{array}$ $= 0$ , then there is an $x$ in $\mathfrak { S }$ with $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } ( x _ { n } - x , x _ { n } - x ) = 0 } \end{array}$

The function $( x , y )$ is called the scalar or inner product of $x$ and $y$ in $\mathfrak { S }$ . The norm in $\mathfrak { L }$ is $\| { \boldsymbol x } \| = ( x , x ) ^ { 1 / 2 }$ .

A Hilbert space is a complex Banach space，and $\| ( x , y ) \| \leqq \| x \|$ $\cdot \| y \| , x , y \in \tilde { \mathcal { Q } }$ (Stone,1932；Delsarte,1932；von Neumann，1950; Schmeidler, 1965 ; Soulé,1967; for topological problems of the theory of dynamical systems see Nemytskii， 1949,and Nemytskii and Stepanov,1960； Sell, 1971).

# 16.19STRONG STABILITY

Consider a canonical system of equations in matrix notation (Sections 1.18-1.19; Sell,1971)

$$
\frac { d Y } { d t } = I H ( t ) Y , \qquad I = { \left( \begin{array} { l l } { 0 } & { I _ { n } } \\ { - I _ { n } } & { 0 } \end{array} \right) } ,
$$

$$
H = \sum _ { i , j = 1 } ^ { 2 n } h _ { i j } ( t ) y _ { i } y _ { j } , \qquad Y = ( y _ { 1 } , \dots , y _ { 2 n } ) ,
$$

where $h _ { i j } ( t ) = h _ { j i } ( t )$ are piecewise continuous real functions with common period $\pmb { \omega }$ . A canonical system is called strongly stable if it is stable and if there exists an $\varepsilon > 0$ such that, for any real symmetric matrix $\tilde { H } ( t )$ with piecewise continuous elements satisfying

$$
\tilde { H } ( t + \omega ) = \tilde { H } ( t ) , \qquad \| \tilde { H } ( t ) - H ( t ) \| < \varepsilon ,
$$

where $\parallel \parallel$ denotes the norm,all solutions of (185） are bounded for $t \to \infty$ . Strongly stable canonical systems form an open set in the set of all canonical systems (compare Section 16.4). Consider two strongly stable canonical systems

$$
\frac { d Y _ { 1 } } { d t } = I H _ { 1 } ( t ) Y _ { 1 } , ~ \frac { d Y _ { 2 } } { d t } = I H _ { 2 } ( t ) Y _ { 2 } ,
$$

such that either can be deformed into the other by continuous variation of the coefficients without violating the strong stability. Our problem is to find the conditions under which there exists a sequence of symmetric matrices $H ( t , \nu )$ ，subject to $H ( t + \omega , \nu ) = H ( t , \nu )$ ，and piecewise continuous in $t$ and $\nu$ ， such that the system

$$
\frac { d Y } { d t } = I H ( t , \nu ) Y
$$

is strongly stable for all $0 \leq \nu \leq 1$ , and such that $H ( t , 0 ) = H _ { 1 } ( t )$ ， $H ( t , 1 ) = H _ { 2 } ( t )$ . Such systems are said to belong to the same stability domain.We discuss the necessary and sufficient conditions for the matrices of solutions of canonical systems to belong to one stability domain,and accordingly study the structure of the stability domain (Krein,1950; Yakubovic,1951; Gelfand and Lidskii,1955).

We normalize the solutions such that $Y ( 0 ) = E _ { 2 n }$ . Since all coefficients of (185) have the common period $\omega$ ,we have

$$
Y ( t + n \omega ) = Y ( t ) Y ^ { n } ( \omega ) \qquad ( n = 1 , 2 , \ldots ) ,
$$

where the elements of the matrix $Y ( t )$ are bounded in $0 \leq t \leq \omega$ In order to have stability it is necessary that all elements of $Y ^ { n } ( \omega )$ should be bounded for $n \to \infty$ or that all roots of the characteristic polynomial of $Y ( \omega )$ should have unit modulus and all elementary divisors (Frazer,Duncan，and Collar,1938） of $Y ( \omega )$ should be linear, i.e., that $Y ( \omega )$ should be reducible to diagonal form.This condition, however, is not sufficient for strong stability.

The transformations for the fundamental system of solutions of a linear differential equation of Fuchsian type (Section 3.7) to be transformed,when the path of integration makes circuits around any of the singularities, form a group called the monodromy group $Y ( \omega )$ such that $Y ( t + \omega ) = Y ( t ) Y ( \omega )$ (Klein,1894; Bieberbach,1953；Wintner, 1947；Section 12.1). The matrix $Y ( \omega )$ is a monodromy matrix for the monodromy group of (185).We call the roots of the characteristic equation the multipliers for short.Krasnoselskii (1963) gave a method of computing the multipliers of a monodromy matrix.

Consider

$$
\frac { d Y } { d t } = I H ( t ) Y + \lambda I Q ( t ) Y ,
$$

where $\pmb { H }$ and $Q$ are real symmetric matrices with the common period $\omega , Q ( t )$ is a positive-definite matrix,and λ is a parameter. Krein (1950) discussed the behavior of the multipliers for complex values of . He proved the lemma that, if the parameter ^ is displaced from the real axis to the upper half of the complex plane, then $_ n$ multipliers of the system appear inside the unit circle and the remaining $_ n$ multipliers outside the unit circle,while none of the multipliers remains on the unit circle.The first $n$ multipliers are said to be of the frst kind and the second $\pmb { n }$ multipliers of the second kind.

Otherwise,by fixing a non-real value $\lambda = \lambda _ { 0 } \left( \mathfrak { F } \lambda _ { 0 } > 0 \right)$ ，we should assume that the monodromy matrix had an eigenvalue $\rho _ { 0 }$ of unit modulus and denote by $f _ { 0 }$ the corresponding eigenvector. Then $y _ { 0 } ( t )$ $= Y ( t ) f _ { 0 }$ would satisfy (186), giving

$$
\frac { d y _ { 0 } } { d t } = I H ( t ) y _ { 0 } + \lambda _ { 0 } I Q ( t ) y _ { 0 } .
$$

With the increment $\omega$ of $t$ the value of $y _ { 0 } ( t )$ would be multiplied by $\rho _ { 0 }$ ,because $y _ { 0 } ( t + \omega ) = Y ( t + \omega ) f _ { 0 } = Y ( t ) Y ( \omega ) f _ { 0 } = \rho _ { 0 } Y ( t ) f _ { 0 } = \rho _ { 0 } y _ { 0 } ( t )$ From these two equations we could regard $y _ { 0 } ( t )$ as the solution of the boundary value problem of (186a) with the boundary condition $y _ { 0 } ( \omega )$ $= \rho _ { 0 } y _ { 0 } ( 0 )$ ，and $\lambda _ { 0 }$ as the eigenvalue corresponding to this solution. If $| \rho _ { 0 } | = 1$ , then the boundary value problem would be self-adjoint and should have real eigenvalues. This is contradictory. Hence no multiplier can be found on the unit circle for $\mathfrak { I } \lambda \ne 0$ . Since a multiplier appears in pairs with its reciprocal, the lemma is proved.

If a canonical system possesses a repeated multiplier on the unit circle, then there occur two cases : the multipliers leave in the complex plane in the same sense or in the opposite sense from the circumference as ² shifts to the non-real region.The repeated multiplier is then said to be of the like type and of the unlike type respectively. Krein (1950) proved that, if a stable canonical system does not have repeated multipliers of the unlike type,then it is strongly stable.

![](images/36beb41f8bccd8828cae4a0f1971cb4dfed8ed8d4a8a8906fb1fe12638151c1d.jpg)  
Figure 16.1

In fact, suppose that there were at a point $\pmb { A }$ (Figure 16.1） of the unit circle a repeated multiplier which for $\lambda = 0$ were of the like type of (186),and that the multiplier would be displaced from the unit circle by some deformation of $H ( t )$ . We give $\lambda$ a complex value with sufficiently small modulus on the upper half-plane.All multipliers would move within the unit circle. Through the above deformation of $H ( t )$ and displacement of 𝜆 from the upper half-plane to zero,the multiplier could not be displaced to the opposite side of the circumference.Hence it is impossible for a stable repeated multiplier of the like type to remain on the unit circle for any sufficiently small deformation of $H ( t )$

Krein showed the converse that if a stable system (185) has repeated multipliers of the unlike type then they can be displaced from the unit circle by an arbitrary small deformation of the matrix $\pmb { H } ( t )$ ,accordingly the necessary and sufficient condition for strong stability is that a stable canonical system is strongly stable if and only if among the multipliers there is none that is repeated and of the unlike type.

From the condition of strong stability we can indicate the whole series of canonical systems belonging to distinct stability domains.

As will be shown，all multipliers of the monodromy matrix of a strongly stable system are non-real and the multipliers of the first and second kind are distributed symmetrically with respect to the real axis on the unit circle.Consider two strongly stable systems with coefficient matrices $H _ { 1 } ( t )$ and $H _ { 2 } ( t )$ ,respectively.It can be shown that the two systems belong to distinct stability regions.In fact, the particular type does not change as the multipliers move continuously on the unit circle,and the continuous deformation $H _ { 1 } ( t )$ to $H _ { 2 } ( t )$ on the unit circle would produce the coincidence of multipliers of the unlike type,which contradicts the condition of strong stability.Hence the necessary condition for two systems to belong to one stability domain is that the two systems should enjoy a conformal distribution of multipliers of the first and second kinds on the unit circle,that is,the ordering of the signs of the multipliers of the first and second kind in the counter-clockwise transit on the upper semicircle should coincide for the two systems,where repeated multipliers are counted in the number of times equal to the multiplicity. There are $2 ^ { n }$ possible types of distribution of multipliers of the first and second kind on the unit circle.

Theorem 1: Each stability domain of a canonical system with $_ { 2 n }$ equations of the form (185) is determined by one of the $2 ^ { n }$ possible types of relative distribution of multipliers on the unit circle,and,in addition,by an integer $N$ , the serial number of the stability domain $( - \infty < N < + \infty )$ .The integer $N$ is called the index of rotation of the system.If two strongly stable systems with conformal distribution of multipliers on the unit circle have the same index of rotation $N$ ， then either system can be continuously deformed to the other in the corresponding stability domain.

The proof is outlined step by step in the following.Consider the solution matrix $\mathbf { } Y ( t )$ of a canonical system normalized to $Y ( 0 ) = E _ { 2 n }$ A matrix $Y ( t )$ satisfies，with the transposed matrix $\mathbf { Y } ^ { T }$ ，

$$
Y ^ { T } ( t ) I Y ( t ) = I
$$

for all $\pmb { t }$ .In fact,by the use of $d Y / d t = I H ( t ) Y , d Y ^ { T } / d t = Y ^ { T } H ^ { T } I ^ { T }$ we have

$$
\frac { d } { d t } \left[ Y ^ { T } ( t ) I Y ( t ) \right] = Y ^ { T } ( t ) H ( t ) Y ( t ) - Y ^ { T } ( t ) H ( t ) Y ( t ) = 0 ,
$$

because $H ^ { T } ( t ) = H ( t )$ ， $I ^ { T } = I ^ { - 1 }$ ， $I ^ { 2 } = - E _ { 2 n }$ ，where $I ^ { \tau } = ( \bar { I } ^ { \tau } ) ^ { \tau }$ with the conjugate complex $\bar { I }$ of $\pmb { I }$ is a Hermitian matrix (Section 1.21; Frazer,Duncan and Collar,1938).

Matrices $\mathbf { } Y ( t )$ satisfying (187) or $I Y I ^ { - 1 } = ( Y ^ { T } ) ^ { - 1 } = ( Y ^ { - 1 } ) ^ { T }$ in a real field (Abraham,1967),or $\overline { { Y } } ^ { T } I Y = I$ in a complex field (Weyl,1939), are called symplectic (the definition in Section 1.21 is in error). They form a group under multiplication.Hence the solution matrices $\mathbf { } Y ( t )$ normalized to $Y ( 0 ) = E _ { 2 n }$ constitute the curves in the group of real symplectic matrices $\{ Y \}$ . In a real field we have det $\left. I \right. = 1$ ,det $\| Y \|$ $= 1$ .If $\gimel$ is an eigenvalue of a symplectic matrix $\boldsymbol { Y }$ ，such that $Y f =$ $\lambda f$ ，then each of $1 / \lambda , \bar { \lambda } , 1 / \bar { \lambda }$ is an eigenvalue with the same multiplicity as $\lambda$ ，where $\bar { \lambda }$ denotes the conjugate complex of . Whereas an orthogonal group (see later） consists of all transformations leaving invariant a nondegenerate symmetric bilinear form (scalar product), a symplectic group is the set of all linear transformations under which a given nondegenerate skew-symmetric bilinear form $[ x y ]$ remains unaltered (Sections 4.22, 21.13).

Lemma $\boldsymbol { \mathit { 1 } }$ :Every curve $Y ( t )$ in the group of real symplectic matrices in $0 \leq t \leq \omega$ possessing a piecewise continuous derivative satisfies a matrix equation of the form (185) in the interval $[ 0 , \omega ]$

Consider two curves $Y _ { \imath } ( t ) , Y _ { \imath } ( t )$ with common starting point $ { \boldsymbol { Y } } _ { 1 } ( 0 )$ $= Y _ { 2 } ( 0 ) = E _ { 2 n }$ out of the group $\{ Y \}$ ,which have piecewise continuous derivatives.It can be shown that if and only if there exists in the group $\{ Y \}$ a deformation $Y ( t , \nu )$ $( 0 \leq t \leq \omega$ ， $0 \leq \nu \leq 1 _ { \cdot }$ ）such that $Y ( t , 0 ) = Y _ { 1 } ( t )$ ， $Y ( t , 1 ) = Y _ { 2 } ( t )$ ， $Y ( 0 , \nu ) = E _ { 2 n }$ ，the derivative $d Y ( t , \nu ) / d t$ exists, is piecewise continuous in $\pmb { t } _ { : }$ ，and continuous in $\pmb { \nu }$ ， and if the curve $Y ( t , \nu )$ for each fixed $\pmb { \nu }$ corresponds to a strongly stable system,then the systems of differential equations for $Y _ { \scriptscriptstyle 1 } ( t ) , Y _ { \scriptscriptstyle 2 } ( t )$ belong to the same stability domain.Hence the question whether a curve belongs to a strongly stable system can be answered by examining the character of the end of the curve.

Any stable-type matrix can be reduced to diagonal form,and the eigenvalues are of unit modulus.Let $\scriptstyle { Y _ { 0 } }$ be such a real symplectic matrix. Let $f _ { 1 } , \ldots , f _ { 2 n }$ be a system of linearly independent eigenvectors of $\scriptstyle { Y _ { 0 } }$ . We can show that the eigenvectors $f _ { s _ { 1 } }$ and $f _ { s _ { 2 } }$ corresponding to distinct eigenvalues are $\scriptstyle I .$ orthogonal, i.e., $( I f _ { s _ { 1 } } , f _ { s _ { 2 } } ) = 0$ In fact, the eigenvalues $\rho _ { s _ { 1 } }$ and $\rho _ { s _ { 2 } }$ are distinct and of unit modulus $\rho _ { s } , \overline { { \rho } } _ { s _ { 2 } } \neq 1$ ； the relation

$$
\begin{array} { r } { ( I f _ { s _ { 1 } } , f _ { s _ { 2 } } ) = ( Y _ { 0 } ^ { T } I Y _ { 0 } f _ { s _ { 1 } } , f _ { s _ { 2 } } ) = ( I Y _ { 0 } f _ { s _ { 1 } } , Y _ { 0 } f _ { s _ { 2 } } ) } \\ { = ( I \rho _ { s _ { 1 } } f _ { s _ { 1 } } , \rho _ { s _ { 2 } } f _ { s _ { 2 } } ) = \rho _ { s _ { 1 } } \bar { \rho } _ { s _ { 2 } } ( I f _ { s _ { 1 } } , f _ { s _ { 2 } } ) } \end{array}
$$

gives the result. If $\rho _ { \circ }$ is a nonrepeated eigenvalue of the symplectic matrix $Y _ { \mathfrak { o } }$ and $f _ { 0 }$ ， the corresponding eigenvector, then we have $( I f _ { 0 } , f _ { 0 } )$ $\neq 0$ and $( I f _ { 0 } , f _ { 0 } )$ is pure imaginary，since $\pmb { I }$ is skew-symmetric by (185).

Put $J = - { \sqrt { - 1 } } I$ ； then it can be shown that the multiplier $\rho _ { 0 }$ moves inside the unit circle as the parameter $\gimel$ moves on the upper half-plane if $( J f , f ) = - \sqrt { - 1 } \ : ( I f , f ) \ : > \ : 0 \ :$ ，and that $\rho _ { 0 }$ is a multiplier of the second kind if $( J f , f ) < 0$ Thus,if $\rho$ is a nonrepeated multiplier, its type is determined by the sign of the quadratic form $( J f , f )$ ，where $f$ is the eigenvector corresponding to the eigenvalue $\rho$ of the monodromy matrix.

Suppose that $\rho _ { 0 }$ is the eigenvalue of $\scriptstyle { Y _ { 0 } }$ of multiplicity $r$ ,and choose the basis $f _ { 1 } , f _ { 2 } , \ldots , f _ { r }$ in the corresponding eigen-subspace. Put

$$
\begin{array}{c} \begin{array} { c c c c } { { { \cal L } _ { \beta _ { 0 } } \equiv ( ( J f _ { \imath } , f _ { \imath } ) ) } } & { { } } & { { } } & { { ( \nu , \mu = 1 , 2 , . . . , r ) } } \\ { { \mathrm { } } } & { { } } & { { } } & { { } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { ( J f _ { \imath } , f _ { \imath } ) } } & { { } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } & { { \mathrm { } } } \end{array} \quad   & { { \begin{array} { c } { { ( \jmath f _ { \tau } , f _ { \imath } ) } } \\ { { ( J f _ { \tau } , f _ { \imath } ) } } \\ { { ( J f _ { \tau } , f _ { \imath } ) } } \\ { { \mathrm { } } } \\ { { \mathrm { } } } \\ { { \mathrm { } } } \end{array} } ) , }  \end{array}
$$

which is nonsingular since the columns are linearly independent.Let the number of the positive eigenvalues of $\scriptstyle L _ { \beta _ { 0 } }$ be $r ^ { \prime }$ and that of the negative be $r ^ { \prime \prime } \left( r ^ { \prime } + r ^ { \prime \prime } = r \right)$ . The numbers $r ^ { \prime } , r ^ { \prime \prime }$ are independent of the choice of the basis in the eigen-subspace.As λ moves in the upper half-plane, the $r ^ { \prime }$ multipliers move toward the inside of the unit circle and $r ^ { \prime \prime }$ multipliers move away from the unit circle,which means that $\pmb { \rho }$ is the point of confluence of the $r ^ { \prime }$ multipliers of the first kind and the $r ^ { \prime \prime }$ multipliers of the second kind.In order that $\scriptstyle \mathbf { Y } _ { 0 }$ have no repeated multipliers of the unlike type it is necessary that all matrices of type $L _ { \beta }$ should be sign-definite,i.e.，each of the multipliers should have eigenvalues of one sign only,where multipliers of the first kind correspond to the positive-definite matrices $L _ { \beta }$ ，and multipliers of the second kind to negative-definite matrices $L _ { \beta }$ . Hence the real symplectic matrix $\boldsymbol { Y }$ is a matrix of the stable type if and only if it is reducible to diagonal form,all its proper values are of unit modulus,and the

Hermitian quadratic form $( J h , h )$ is definite on every eigen-subspace of the matrix $Y$ (Section 1.21).

Thus in order that two matrices of the stable type can be deformed one to the other through matrices of the stable type it is necessary that the two matrices have conformal distribution of multipliers of the first and second kind on the unit circle.Otherwise confluence of multipliers of the unlike type should occur during the continuous deformation.

Lemma 2: The symplectic matrix $\boldsymbol { Y }$ is a matrix of the stable type if and only if it can be represented in the form $Y = G R G ^ { - 1 }$ ，where $G$ and $\pmb R$ are real symplectic matrices,and

$$
R = \binom { \cos { \theta } } { - \sin { \theta } } \quad \cos { \theta } \Big ) ,
$$

where $\theta$ is a real diagonal matrix of order $_ n$ ， whose diagonal elements$\theta _ { 1 } , \ldots , \theta _ { n }$ satisfy $| \theta _ { s } | < \pi$ $( s = 1 , 2 , \ldots , n )$ ，and $\theta _ { s ^ { \prime } } \neq \theta _ { s ^ { \prime \prime } }$ $( 1 \leq s ^ { \prime }$ ，$s ^ { \prime \prime } \leqq n )$ ：

From the orthogonality of $\boldsymbol { Y }$ and $R$ follows the reducibility to diagonal form of $Y$ ， since the eigenvalues are all of modulus unity. It can be shown that the Hermitian form $( J h , h )$ is definite on the eigen-subspace of the matrix $\pmb { Y }$ . In fact,the quadratic form $( J h , h )$ conserves its value if we apply the symplectic matrix $G$ ，that is,

$$
( J G h , G h ) = G ^ { T } ( J G h , h ) = ( J h , h ) .
$$

The eigen-subspaces of $\pmb { Y }$ and $\pmb R$ corresponding to the same eigenvalue are connected by a linear transformation defined by $G$ ，since $\mathbf { \nabla } \mathbf { Y } =$ $G R G ^ { - 1 }$

Denoting the unit vector by

$$
\begin{array} { r l r } { e _ { 1 } = ( 1 , 0 , \ldots , 0 ) , \ } & { { } \ e _ { 2 } = ( 0 , 1 , \ldots , 0 ) , \ } & { } \\ { \phantom { e _ { 1 } = } \cdot \cdot \cdot , \ } & { { } \ e _ { 2 n } = ( 0 , 0 , \ldots , 1 ) , \ } & { } \end{array}
$$

and writing

$$
m _ { s } = \frac { e _ { s } + \sqrt { - 1 } \ e _ { s + n } } { \sqrt { 2 } } , m _ { - s } = \frac { e _ { s } - \sqrt { - 1 } \ e _ { s + n } } { \sqrt { 2 } }
$$

$$
( s = 1 , \ldots , n ) ,
$$

we see that the vectors $m _ { s } , m _ { - s } \left( s = 1 , 2 , . . . , n \right)$ form an orthogonal system of the eigenvectors of the matrix $\pmb R$ with the eigenvalues

$$
s = \exp \{ \sqrt { - 1 } \theta _ { s } \} , \rho _ { - s } = \exp \{ - \sqrt { - 1 } \theta _ { s } \} ( s = 1 , \ldots , n ) ,
$$

where

$$
R m _ { s } = \exp \left\{ \sqrt { - 1 } \theta _ { s } \right\} \cdot m _ { s } , \qquad R m _ { - s } = \exp \left\{ - \sqrt { - 1 } \theta _ { s } \right\} \cdot m _ { - s } ,
$$

$$
( m _ { s } , m _ { s } ) = 1 , \qquad ( m _ { - s } , m _ { - s } ) = 1 \qquad ( s = 1 , \ldots , n ) ,
$$

$$
( m _ { s ^ { \prime } } , m _ { s ^ { \prime \prime } } ) = 0 \qquad ( s ^ { \prime } \ne s ^ { \prime \prime } , - n \le s ^ { \prime } , s ^ { \prime \prime } \le n )
$$

The matrix $\pmb { I }$ is of the above form of $\pmb R$ and $I m _ { s } = \sqrt { - 1 } \ m _ { s } , I m _ { - s } =$ $- \sqrt { - 1 } \ m _ { - s }$ for $\theta _ { s } = \pi / 2$ $( s = 1 , \ldots , n )$

These vectors $m _ { s _ { 1 } } , \ldots , m _ { s } ,$ constitute the basis of the eigen-subspace of $R$ corresponding to the eigenvalue $\pmb { \rho }$ ，where $s _ { 1 } , s _ { 2 } , \ldots , s _ { r }$ are all of the same sign. Assume that $s _ { 1 } , \ldots , s _ { r } > 0$ Suppose that

$$
h = \sum _ { j = 1 } ^ { r } \alpha _ { j } m _ { s } \neq 0 ;
$$

then we get

$$
I h = \sum _ { j = 1 } ^ { r } \alpha _ { j } I m _ { j } = \sqrt { - 1 } h ,
$$

and accordingly

$$
( J h , h ) = - \sqrt { - 1 } \left( I h , h \right) = ( h , h ) > 0 .
$$

Hence $( J h , h )$ is positive-definite on the eigen-subspace corresponding to the eigenvectors with positive indices,and the numbers

$$
\exp \left\{ \sqrt { - 1 } \theta _ { s } \right\} \qquad ( s = 1 , \dots , n ) ,
$$

are multipliers of the first kind.

Conversely，suppose that $\boldsymbol { Y }$ is a matrix of the stable type and reducible to a diagonal form with all its eigenvalues on the unit circle, otherwise we could find a real eigenvector $f \neq 0$ corresponding to the eigenvalue not on the unit circle, so that we should have $( J f , f ) =$ $- { \sqrt { - 1 } } \left( I f , f \right) = 0$ Let $\rho$ be an eigenvalue with multiplicity $r$ of the matrix $\mathbf { \Delta } \mathbf { Y }$ . Then $( J h , h )$ is positive-definite in the corresponding eigen-subspace In this subspace we consider a basis of $r$ vectors $f _ { s _ { 1 } } , \ldots , f _ { s _ { \tau } }$ so chosen that

$$
( J f _ { s _ { i } } , f _ { s _ { j } } ) = 0 \qquad ( i \ne j ) , \qquad ( J f _ { s _ { i } } , f _ { s _ { j } } ) = 1 \qquad ( i = j ; 0 \le i , j
$$

because of the Hermitian and positive-definite character of the quadratic form $( J h , h )$

If $\pmb { Y }$ is real, the number $\overline { { \rho } }$ is also an eigenvalue of $\boldsymbol { Y }$ . The vectors ${ { f } _ { - s _ { 1 } } } = { { \bar { f } } _ { s _ { 1 } } } , { { f } _ { - s _ { 2 } } } = { { \bar { f } } _ { s _ { 2 } } } , . . . , { { f } _ { - s _ { r } } } = { { \bar { f } } _ { s _ { r } } }$ form a basis in the corresponding subspace,and are $\pmb { I }$ -orthogonal,as can be seen from the construction.

If the eigenvalues of $\boldsymbol { Y }$ corresponding to a pair of conjugate complex eigenvalues are normalized, then we obtain a system of $2 n$ linearly independent eigenvectors $f _ { 1 } , f _ { 2 } , . . . , f _ { n } , f _ { - 1 } , . . . , f _ { - n }$ ，for which

$$
( J f _ { s ^ { \prime } } , f _ { s ^ { \prime \prime } } ) = 0 \qquad ( s ^ { \prime } \ne s ^ { \prime \prime } ; - n \le s ^ { \prime } , s ^ { \prime \prime } \le n ) ,
$$

$$
( J f _ { s } , f _ { s } ) = 1 , \qquad ( J f _ { - s } , f _ { - s } ) = - 1 \qquad ( s = 1 , \ldots , n ) ,
$$

where eigenvalues with the indices of opposite sign are complex conjugate. We write the $2 n$ eigenvalues corresponding to these $2 n$ eigenvectors as

$$
\begin{array} { r l } & { \exp { \{ \sqrt { - 1 } \theta _ { 1 } \} } , \cdot \cdot \cdot , \exp { \{ \sqrt { - 1 } \theta _ { n } \} } , } \\ & { \exp { \{ - \sqrt { - 1 } \theta _ { 1 } \} } , \cdot \cdot \cdot , \exp { \{ - \sqrt { - 1 } \theta _ { n } \} } , } \end{array}
$$

in which a multiple eigenvalue of multiplicity $r$ is repeated $r$ times. The first $_ n$ eigenvalues are the multipliers of the first kind and the last $_ n$ are of the second kind. Choose $| \theta _ { s } | < \pi$ so that $\theta _ { s } , \neq \theta _ { s } , ,$ $( s ^ { \prime } , s ^ { \prime \prime } =$ $1 , \ldots , n )$ . Consider a system of real vectors defined by

$$
g _ { s } = \frac { f _ { s } + f _ { - s } } { \sqrt 2 } , g _ { s + n } = \frac { f _ { s } - f _ { - s } } { \sqrt { - 1 } \sqrt 2 } .
$$

Apart from the constant factors,the vectors $g _ { s }$ and $g _ { s + \pi }$ coincide with the real and imaginary parts of $f _ { s }$ ，respectively. Taking the real and imaginary parts of $Y f _ { s } = \exp { \{ \sqrt { - 1 } \theta _ { s } \} } \cdot f _ { s }$ ，we obtain

$$
Y g _ { s } = \cos \theta _ { s } \cdot g _ { s } - \sin \theta _ { s } \cdot g _ { s + n } , ~ Y g _ { s + n } = \sin \theta _ { s } \cdot g _ { s } + \cos \theta _ { s }
$$

Let $G$ be a matrix with the column $g _ { 1 } , \ldots , g _ { 2 n }$ . Then this last pair of equations can be writen $Y G = G R$ ，where $\pmb R$ is the matrix given in the foregoing discussion.The matrix $G$ is nonsingular, since the vectors $g _ { 1 } , \ldots , g _ { 2 n }$ are linearly independent.We obtain $Y = G R G ^ { - 1 }$ . It can be shown that $G$ is symplectic, because

$$
( I g _ { s ^ { \prime } } , g _ { s ^ { \prime \prime } } ) = 0 \qquad ( | s ^ { \prime } - s ^ { \prime \prime } | \neq n ; s ^ { \prime } , s ^ { \prime \prime } = 1 , \ldots , 2 n ) ,
$$

$$
\begin{array} { c }  { \tiny { \ : \begin{array} { l } { { ( \vert s ^ { \prime } - s ^ { \prime \prime } \vert \neq n ; s ^ { \prime } , s ^ { \prime \prime } = 1 , \ldots , 2 } } \\ { { ( g _ { s } , I g _ { s + n } ) = 1 , \qquad ( g _ { s + n } , I g _ { s } ) = - 1 , } } \end{array} } } \end{array}
$$

which are equivalent to $G ^ { T } I G = I$

Thus Lemma 2 is established.

Lemma 2 implies the sufficiency of the condition for the conformal distribution of the multipliers (Ahlfors and Sario,196O)． In fact, let $Y _ { 1 } = G _ { 1 } R _ { 1 } G _ { 1 } ^ { - 1 }$ ， $Y _ { 2 } = G _ { 2 } R _ { 2 } G _ { 2 } ^ { - 1 }$ be of such a nature.Because of the conformal distribution we can deform $R _ { 1 }$ to $\boldsymbol { R } _ { 2 }$ so that no confluence of multipliers of the unlike type occurs on the unit circle, along any curve connecting these matrices in the group of real symplectic matrices. The deformed matrix remains of the stable type during this deformation process.

Now consider the deformation of curves in the group of real symplectic matrices. In the group of real symplectic matrices not every pair of curves with common end-points can be deformed into coincidence continuously.

Lemma 3: The group of real symplectic matrices is homeomorphic to the topological product of the circumference of a circle and a simply connected topological space.

Proof:In general a matrix such that $Y ^ { T } = Y ^ { - 1 }$ is called orthogonal (Weyl,1939). Two vectors $x , y$ in a topological space $\mathfrak { S }$ are said to be orthogonal if the bilinear form $( x , y ) = 0$ . Two manifolds $\mathfrak { M }$ and $\mathfrak { N }$ in $\mathfrak { S }$ are orthogonal if $( { \mathfrak { M } } , { \mathfrak { N } } ) = 0$ A linear operator $E$ in $\mathfrak { L }$ is called an orthogonal projection if the manifolds $\pmb { E } \widetilde { \pmb { \mathcal { Q } } }$ and $( I - E ) \xi$ are orthogonal.

With a positive-definite matrix S and an orthogonal matrix $U$ a real symplectic matrix $\boldsymbol { Y }$ , if it is nonsingular,can be uniquely represented by the polar form (Section 1.21) $Y = S U$ ，where $s$ and $\boldsymbol { U }$ depend continuously on $\pmb { Y }$ . We extend this idea in four steps,based on the general theory of semisimple Lie groups (Sections 4.28 and 4.29).

(i) The matrices $s$ and $U$ are symplectic.In fact, in the relation $Y = I ^ { - 1 } ( Y ^ { T } ) ^ { - 1 } I ;$ ，which is equivalent to $Y ^ { T } I Y = I$ ，we replace $Y =$ $s U$ and obtain $Y = I ^ { - 1 } ( S ^ { T } ) ^ { - 1 } I \cdot I ^ { - 1 } ( U ^ { T } ) ^ { - 1 } I$ Since $s$ is symplectic and positive-definite and $\pmb { I }$ is orthogonal, $I ^ { - 1 } ( S ^ { T } ) ^ { - 1 } I = I ^ { T } S ^ { - 1 } I$ is symmetric (Section 16.20) and positive-definite.Moreover $I ^ { - 1 } ( U ^ { T } ) ^ { - 1 } I$ is orthogonal．Hence,by putting $S = I ^ { - 1 } ( S ^ { T } ) ^ { - 1 } I$ ， $U = I ^ { - 1 } ( U ^ { T } ) ^ { - 1 } I .$ ，we find the polar representation $Y = S U$

(ii)The set $\{ S \}$ of symmetric，positive-definite and symplectic matrices of order $_ { 2 n }$ is homeomorphic to an $n ( n + 1 )$ -dimensional Euclidean space. In fact, every symmetric positive-definite matrix $s$ can be represented uniquely by $S = e ^ { A }$ ，where $\pmb { A }$ is a real symmetric matrix

$$
e ^ { A } = E _ { 2 n } + A + { \frac { A ^ { 2 } } { 2 ! } } + { \frac { A ^ { 3 } } { 3 ! } } + \cdots .
$$

The relation $S = e ^ { A }$ establishes the homeomorphic correspondence (see Chapter 24) between positive-definite symmetric matrices of order $_ n$ and all symmetric matrices of order $\pmb { n }$ (Chevalley，1946；Section 4.29). From $e ^ { A } = I ^ { - 1 } ( e ^ { A } ) ^ { - 1 } I = I ^ { - 1 } e ^ { - A } I = e ^ { - I ^ { - 1 } A I }$ we obtain $e ^ { A } = { \begin{array} { l } { \begin{array} { r l r } \end{array} } \end{array} }$ $e ^ { - I ^ { - 1 } A I }$ or $A = - I ^ { - 1 } A I$ ,i.e., $\pmb { A }$ is symplectic.On the other hand,if $A = - I ^ { - 1 } A I _ { \mathrm { { i } } }$ ，then the matrix $e ^ { A }$ belongs to the set $\{ S \}$ . Thus the set $\{ S \}$ is homeomorphic to all real symmetric matrices $\{ A \}$ ·

Write $\pmb { A }$ in the form

$$
A = { \binom { a _ { 1 } } { a _ { 3 } } } ,
$$

where $a _ { 1 } , a _ { 2 } , a _ { 3 } , a _ { 4 }$ are square matrices of order $_ n$ .From the condition $A = - I ^ { - 1 } A I$ we obtain $a _ { 1 } = - a _ { 4 }$ ， $a _ { 2 } = a _ { 3 }$ . Since $\pmb { A }$ is symmetric, we have $a _ { 1 } ^ { \tau } = a _ { 1 }$ ， $a _ { 2 } ^ { \tau } = a _ { 3 }$ .Hence $\pmb { A }$ should be given by

$$
A = { \binom { a _ { 1 } } { a _ { 2 } } } , \quad { \underline { { a _ { 2 } } } } \rangle ,
$$

where $a _ { 1 } , a _ { 2 }$ are symmetric matrices of order $_ n$ . Such a set of matrices can be shown to be homeomorphic to an $n ( n + 1 )$ -dimensional Euclidean space,if we take the elements on and above the principal diagonal as coordinates.

(iii) The group $\{ U \}$ of real symplectic orthogonal matrices of order $_ { 2 n }$ is homeomorphic to the group $\{ w \}$ of complex unitary matrices of order $_ n$ (Section 1.21).

In fact,from the relation $U ^ { T } I U = I , U U ^ { T } = E _ { 2 n }$ we derive $U I =$ IU. Writing

$$
U = { \binom { u _ { 1 } } { u _ { 3 } } } ,
$$

we obtain $u _ { 1 } = u _ { 4 }$ ， $u _ { 2 } = - u _ { 3 }$ . Thus any symplectic orthogonal matrix $\pmb { U }$ can be written

$$
U = \binom { u _ { 1 } \quad u _ { 2 } } { - u _ { 2 } \quad u _ { 1 } } .
$$

We have from $U U ^ { T } = E _ { 2 n }$ ,by direct multiplication,

$$
u _ { 1 } u _ { 1 } ^ { T } + u _ { 2 } u _ { 2 } ^ { T } = E _ { 2 n } , \qquad u _ { 1 } u _ { 2 } ^ { T } - u _ { 2 } u _ { 1 } ^ { T } = 0 ,
$$

or

$$
( u _ { 1 } + \sqrt { - 1 } u _ { 2 } ) ( u _ { 1 } + \sqrt { - 1 } u _ { 2 } ) ^ { T } = E _ { n } .
$$

Hence $\pmb { u } _ { 1 }$ and $\pmb { u } _ { 2 }$ determine $\ b { U }$ .The matrix $w = u _ { 1 } + \sqrt { - 1 } u _ { 2 }$ of order $\pmb { n }$ is unitary. If we associate $w$ with every symplectic orthogonal matrix $\pmb { U }$ ，we find the required homeomorphism.

Let $U ^ { ( 1 ) }  w ^ { ( 1 ) }$ ， $U ^ { ( 2 ) }  { \pmb w } ^ { ( 2 ) }$ be the homeomorphism,and write ${ \pmb U } ^ { ( 1 ) }$ ， $U ^ { ( 2 ) }$ in the form

$$
U = \left( \begin{array} { r r } { { u _ { 1 } } } & { { u _ { 2 } } } \\ { { - u _ { 2 } } } & { { u _ { 1 } } } \end{array} \right) ;
$$

then

$$
U ^ { ( 1 ) } U ^ { ( 2 ) } = \binom { u _ { 1 } ^ { ( 1 ) } u _ { 1 } ^ { ( 2 ) } - u _ { 2 } ^ { ( 1 ) } u _ { 2 } ^ { ( 2 ) } } { - u _ { 1 } ^ { ( 1 ) } u _ { 2 } ^ { ( 2 ) } - u _ { 2 } ^ { ( 1 ) } u _ { 1 } ^ { ( 2 ) } } . \quad \cdot u _ { 1 } ^ { ( 1 ) } u _ { 2 } ^ { ( 2 ) } + u _ { 2 } ^ { ( 1 ) } u _ { 1 } ^ { ( 2 ) } \Biggr ) .
$$

On the other hand,we have

$$
\begin{array} { r l r } {  { \boldsymbol { w } ^ { ( 1 ) } \boldsymbol { w } ^ { ( 2 ) } = ( u _ { 1 } ^ { ( 1 ) } + \sqrt { - 1 } \ u _ { 2 } ^ { ( 1 ) } ) ( u _ { 1 } ^ { ( 2 ) } + \sqrt { - 1 } \ u _ { 2 } ^ { ( 2 ) } ) } } \\ & { } & { = u _ { 1 } ^ { ( 1 ) } u _ { 1 } ^ { ( 2 ) } - u _ { 2 } ^ { ( 1 ) } u _ { 2 } ^ { ( 2 ) } + \sqrt { - 1 } ( u _ { 1 } ^ { ( 1 ) } u _ { 2 } ^ { ( 2 ) } + u _ { 2 } ^ { ( 1 ) } u _ { 1 } ^ { ( 2 ) } ) . } \end{array}
$$

Hence the unity matrix $E _ { n }$ of the group $\{ w \}$ corresponds to the unity $E _ { 2 n }$ of the group $\{ U \}$ . Thus the groups $\{ U \}$ and $\{ w \}$ are isomorphic.

(iv) A group of complex unitary matrices can be decomposed into the topological product of the circumference of a circle and the group of unitary unimodular matrices.

In fact, for a unitary matrix $w$ we write det $\| w \| = \exp { \{ \sqrt { - 1 } \ \psi I ^ { T } \} } .$

$$
v = \left[ { \begin{array} { r r } { e ^ { \sqrt { - 1 } \nu } } & { 0 } \\ { 1 } & { . } \\ { \phantom { \sqrt { - 1 } } } & { . } \\ { 0 } & { \phantom { \sqrt { - 1 } } } & { 1 } \end{array} } \right] , \qquad w = v ( v ^ { - 1 } w ) .
$$

The group $\{ v \}$ is homeomorphic to the circumference of a circle. The matrix $v ^ { - 1 } w$ is unimodular.

After these preparations we come to the proof of Lemma 3. As is already known (Weyl,1939),unitary unimodular matrices form a simply connected topological group.We have seen that the group of real symplectic matrices of order $_ n$ is decomposed into the topological product of a group of unitary unimodular matrices of order $_ n$ and an $n ( n + 1 )$ -dimensional Euclidean space. Since the topological product of two simply connected spaces is simply connected, the first group is simply connected,and Lemma 3 is established.

We look for the condition under which two curves $Y _ { 1 } ( t ) , Y _ { 2 } ( t ) , 0 \leq$ $t \leq \omega$ ，with common ends $Y _ { 1 } ( 0 ) = Y _ { 2 } ( 0 ) = E _ { 2 n }$ ， $Y _ { 1 } ( \omega ) = Y _ { 2 } ( \omega )$ are homotopic, i.e., can be continuously deformed to each other with the two ends fixed. Two continuous curves are said to be homotopic if they can be brought into coincidence by continuous deformation (Section 24.17).By Lemma 3, to each real symplectic matrix $\pmb { Y }$ there corresponds a fully determined point, the projection of the matrix $\pmb { Y }$ on a circle,whose location is given by the determinant of the matrix w on the unit circle of the complex plane. The projections on the unit circle of the matrix curves $Y _ { 1 } ( t )$ and $Y _ { 2 } ( t )$ form two continuous curves with common ends. If the projections are homotopic, the continuous deformation can be set up by Lemma 3 if we bring together those projections in the simply connected topological space where any two curves are homotopic (Pontryagin,1939).Thus, in order that $\mathbf { \boldsymbol { Y } } _ { 1 } ( t )$ and $Y _ { \imath } ( t )$ shall be continuously deformable with the ends fixed it is necessary and sufficient that these projections of the circle should be of such a nature.

In order to write the condition explicitly，let ${ \pmb w } _ { 1 } ( t )$ ， ${ \pmb w } _ { 2 } ( t )$ be the curves corresponding to $Y _ { 1 } ( t ) , Y _ { 2 } ( t )$ respectively in the group of unitary matrices； then the condition for those curves to be homotopic is expressed by

$$
\arg \operatorname* { d e t } w _ { 1 } ( t ) | _ { 0 } ^ { \omega } = \arg \operatorname* { d e t } w _ { 2 } ( t ) | _ { 0 } ^ { \omega } ,
$$

where arg det $w ( t ) _ { \mid _ { 0 } } ^ { \mid \omega }$ denotes the change of argument of the complexvalued function det $w ( t )$ due to the variation of the real parameter $\pmb { t }$ from 0 to $\omega$

We obtain the expresson for the argument by representing the curve $\mathbf { } Y ( t )$ in polar form $Y ( t ) = S ( t ) U ( t )$ and introducing a unitary matrix $M$ (Section 1.21) such that

$$
M ^ { T } U M = { \binom { w } { 0 } } , { \LARGE \ d } , \qquad w = u _ { 1 } + { \sqrt { - 1 } } u _ { 2 } ,
$$

$$
M = \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c } { { E _ { n } } } & { { E _ { n } } } \\ { { \sqrt { - 1 } E _ { n } } } & { { - \sqrt { - 1 } E _ { n } } } \end{array} \right) .
$$

Then we get

$$
M ^ { T } Y ( t ) M = [ M ^ { T } S ( t ) M ] [ M ^ { T } U ( t ) M ] .
$$

Let $z ( t )$ be the upper diagonal minor of order $_ n$ of the matrix $M ^ { T } Y ( t ) M$ ; then

$$
z ( t ) = ( ( Y ( t ) m _ { j } , m _ { i } ) ) \qquad ( 1 \leq i , j \leq n ) ,
$$

where the $m _ { i }$ are given in the foregoing discussion. By using the above representation in the box diagonal form of $M ^ { T } U ( t ) M$ ，we see that $z ( t ) = s _ { n } ( t ) \cdot w ( t )$ ，where $s _ { n } ( t )$ is the upper diagonal minor of the positive-definite Hermitian matrix $M ^ { T } S ( t ) M$ .The determinant of $s _ { n } ( t )$ ， $0 \leq t \leq \omega$ ,is real and nonzero.Hence

$$
{ \mathrm { . } } { \mathit { z } } ( t ) { \mathit { \check { \mathbf { \rho } } } } _ { 0 } ^ { \omega } = { \arg \operatorname* { d e t } } { w ( t ) { \mathit { \check { \mathbf { \rho } } } } _ { 0 } ^ { \omega } } .
$$

Lemma 4: Two continuous curves $Y _ { \imath } ( \tau )$ and $Y _ { \mathfrak { z } } ( \tau )$ $( 0 \leq \tau \leq 1 )$ ， with common end-points $Y _ { 1 } ( 0 ) = Y _ { 2 } ( 0 )$ ， $ { Y _ { \mathrm { 1 } } } ( 1 ) =  { Y _ { \mathrm { 2 } } } ( 1 )$ ,lying entirely in a connected component of the matrices of the stable type，can always be continuously deformed one to the other.

By Lemma 2 the matrices $\boldsymbol { Y } _ { 1 } ( \tau )$ and $Y _ { \imath } ( \tau )$ can be expressed

$$
Y _ { 1 } ( \tau ) = G _ { 1 } ( \tau ) R _ { 1 } ( \tau ) G _ { 1 } ^ { - 1 } ( \tau ) , \qquad Y _ { 2 } ( \tau ) = G _ { 2 } ( \tau ) R _ { 2 } ( \tau ) G _ { 2 } ^ { - 1 } ( \tau )
$$

for a fixed value of $\tau$ ，where $R _ { 1 } ( \tau ) , R _ { 2 } ( \tau )$ are symplectic orthogonal matrices of the form in Lemma 2 and $G _ { 1 } ( \tau ) , G _ { 2 } ( \tau )$ are symplectic matrices. Also, $\pmb { R } ( \tau )$ and $G ( \tau )$ depend continuously on $\pmb { \tau }$ and can be so chosen that

$$
\begin{array} { r l } { R _ { 1 } ( 0 ) = R _ { 2 } ( 0 ) , } & { { } \quad R _ { 1 } ( 1 ) = R _ { 2 } ( 1 ) ; } \\ { G _ { 1 } ( 0 ) = G _ { 2 } ( 0 ) , } & { { } \quad G _ { 1 } ( 1 ) = G _ { 2 } ( 1 ) . } \end{array}
$$

It can be shown that the curves $R _ { 1 } ( \tau ) , R _ { 2 } ( \tau )$ are homotopic,because the multipliers of $Y _ { \imath } ( \tau )$ and $Y _ { \mathfrak { z } } ( \tau )$ for $0 \leq \tau \leq 1$ describe paths which do not go from one half-plane to the other on the unit circle and the paths described by the multipliers that coincide in pairs at $\tau = 0$ and $\tau = 1$ can be continuously deformed and brought into coincidence. Then we seek to deform the curve $G _ { 1 } ( \tau )$ to the curve $G _ { \imath } ( \tau )$ .The matrices $G ( \tau )$ in $Y = G R G ^ { - 1 }$ can be determined to within right multiplication by a matrix commuting with $\boldsymbol { R } ( \tau )$ .Hence the condition for homotopicity is that

$$
\arg \operatorname* { d e t } w _ { 1 } ( \tau ) \big | _ { 0 } ^ { 1 } = \arg \operatorname* { d e t } w _ { 2 } ( t ) \big | _ { 0 } ^ { 1 } ,
$$

where if necessary one of the curves is multiplied by a matrix commuting with $R ( \tau )$ . In fact, suppose that

$$
w _ { 1 } ( \tau ) | _ { 0 } ^ { 1 } = \mathrm { a r g } \operatorname * { d e t } w _ { 2 } ( \tau ) | _ { 0 } ^ { 1 } + \Delta , \qquad \Delta = 2 \pi m ,
$$

where m is an integer. Writing $G _ { 2 } ( \tau ) = S _ { 2 } ( \tau ) U _ { 2 } ( \tau )$ we introduce an orthogonal symplectic matrix

$$
N ( \tau ) = \left( \begin{array} { c c c c c c } { { \cos \tau 2 \pi m } } & { { 0 \ldots 0 } } & { { \sin \tau 2 \pi m } } & { { 0 \ldots 0 } } \\ { { 0 } } & { { 1 \ldots 0 } } & { { 0 } } & { { 0 \ldots 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } \\ { { 0 } } & { { 0 \ldots 1 } } & { { 0 } } & { { 0 \ldots 0 } } & { { 0 } } \\ { { - \sin \tau 2 \pi m } } & { { 0 \ldots 0 } } & { { \cos \tau 2 \pi m } } & { { 0 \ldots 0 } } \\ { { 0 } } & { { 0 \ldots 0 } } & { { 0 } } & { { 1 \ldots 0 } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } \\ { { 0 } } & { { 0 \ldots 0 } } & { { 0 } } & { { 0 } } & { { \ldots 1 } } \end{array} \right) .
$$

Now $N ( \tau )$ commutes with $R _ { 2 } ( \tau )$ . The condition for the curves $G _ { 1 } ( \tau )$ ， $\tilde { G } _ { 2 } ( \tau ) = G _ { 2 } ( \tau ) N ( \tau )$ to be homotopic is satisfied. The orthogonal part of $\tilde { G } _ { \scriptscriptstyle 2 } ( \tau )$ is equal to $U _ { \imath } ( \tau ) N ( \tau )$ in the polar representation $Y = s U$ ， and,by the isomorphism $U  w$ ， corresponds to the unitary.matrix $\tilde { w } _ { 2 } ( \tau ) = w _ { 2 } ( \tau ) w _ { N } ( \tau )$ ，where $w _ { N } ( \tau )$ is a matrix of the form of $v$ in the step (iv) of Lemma 3 with $\psi = \tau 2 \pi m$ . Since

we have

It is easily shown that $G _ { 1 } ^ { - 1 } ( \tau )$ is continuously deformable to $G _ { 2 } ^ { - 1 } ( \tau )$ since $G _ { 1 } ^ { - 1 } ( \tau ) = I ^ { - 1 } G _ { 1 } ^ { T } ( \tau ) I$ by symplectic condition.Thus Lemma 4 is established.

Consider a set of curves $\left[ Y _ { \alpha } ( t ) \right]$ $( 0 \leq { t } \leq \omega )$ ， $Y _ { \alpha } ( 0 ) = E _ { 2 n }$ in the group $\{ Y \}$ ， which have piecewise continuous derivatives and satisfy the conditions: (a) the ends of all curves lie in a connected component of the matrices of the stable type,and (b) after the ends of any two curves have been brought into coincidence, the homotopic condition

$$
\arg \operatorname* { d e t } w _ { 1 } ( t ) | _ { 0 } ^ { \omega } = \arg \operatorname* { d e t } w _ { 2 } ( t ) | _ { 0 } ^ { \omega }
$$

holds.

Take any curve $Y ( t )$ belonging to the stability domain $\left[ Y _ { \alpha } ( t ) \right]$ whose ends are $Y ( \omega ) = G R G ^ { - 1 }$ ， together with the curve $Y _ { g } ( t )$ defined by $Y _ { g } ( t ) = G ^ { - 1 } Y ( t ) G$ Then $Y _ { g } ( t )$ belongs to the set $ { [ Y _ { \alpha } ( t ) ] }$ . In fact, we have $Y _ { g } ( 0 ) = E _ { 2 n }$ ， $Y _ { g } ( \omega ) = G ^ { - 1 } Y ( \omega ) G = R$ ，and the end of $Y _ { g } ( t )$ has the same type of distribution of multipliers as the ends of the curves $ { [ Y _ { \alpha } ( t ) ] }$ ,i.e., those of the stable type. When the matrix $G$ is deformed to the unit matrix, the curve $Y _ { g } ( t )$ coincides with $Y ( t )$ ，where the end-points of the deformed curve are assumed not to leave the component of the matrices of the stable type.

We join the ends of the curve $Y _ { g } ( t )$ to the beginning,i.e.， to the matrix $E _ { 2 n }$ ,by means of the continuous curves defined by the orthogonal symplectic matrix $R$

$$
R = { \binom { \cos { ( 1 - \tau ) } \theta } { - \sin { ( 1 - \tau ) } \theta } } \quad \sin { ( 1 - \tau ) } \theta \quad \quad ( 0 \leq \tau \leq 1 ) .
$$

Since $\theta _ { s ^ { \prime } } \neq \theta _ { s ^ { \prime \prime } } , 1 \leq s ^ { \prime } , s ^ { \prime \prime } \leq n$ in Lemma 2,all points of the curve $R ( \tau )$ except the end-point, belong to the component of the matrix of the stable type.By joining the end and the beginning of the curve $\boldsymbol { Y } _ { g } ( t )$ by means of the matrix $R ( \tau )$ ，we obtain a closed curve.The change corresponding to this curve of the argument of the determinant of the unitary matrix $w$ is compounded by arg det $w _ { g } ( t ) \big \vert _ { 0 } ^ { \omega }$ and arg $R ( \tau ) \big | _ { 0 } ^ { 1 }$ The curve is closed.Accordingly the integer $N$ such that

$$
\frac { 1 } { 2 \pi } [ \arg \operatorname* { d e t } w _ { g } ( t ) | _ { \mathfrak { o } } ^ { \omega } + \arg R ( \tau ) | _ { \mathfrak { o } } ^ { 1 } ] = N
$$

is associated with the given stability domain $ { [ Y _ { \alpha } ( t ) ] }$ . The index of

rotation $N$ does not depend on the choice of the curve $Y ( t )$ out of the set $ { [ Y _ { \alpha } ( t ) ] }$

Since to the matrix $R ( \tau )$ there corresponds the unitary matrix

$$
\begin{array} { r } { \mathsf { o s } \left( 1 - \tau \right) \theta + \sqrt { - 1 } \sin \left( 1 - \tau \right) \theta = \exp \big \{ \sqrt { - 1 } \left( 1 - \tau \right) \theta \big \} , } \end{array}
$$

where $\theta$ is a diagonal matrix with the diagonal elements $\theta _ { 1 } , \ldots , \theta _ { n }$ ， the principal values of the first kind of $Y ( \omega )$ , it follows that

$$
\begin{array} { l } { { \displaystyle R ( \tau ) \big | _ { 0 } ^ { 1 } = \arg \operatorname* { d e t } \exp \left\{ \sqrt { - 1 } ( 1 - \tau ) \theta \right\} \big | _ { 0 } ^ { 1 } } } \\ { { \displaystyle ~ = \arg \prod _ { s = 1 } ^ { n } \exp \left\{ \sqrt { - 1 } \theta _ { s } ( 1 - \tau ) \right\} \big | _ { 0 } ^ { 1 } = - \sum _ { s = 1 } ^ { n } \theta _ { s } . } } \end{array}
$$

From(188)we obtain

arg det $w _ { g } ( t ) | _ { 0 } ^ { \omega } = \arg \operatorname* { d e t } z ( t ) | _ { 0 } ^ { \omega } ,$

$$
z ( t ) = ( ( Y _ { g } ( t ) m _ { j } , m _ { i } ) ) \qquad ( 1 \leq i , j \leq n ) ,
$$

where $Y _ { g } ( t ) = G ^ { - 1 } Y ( t ) G$ Since $G$ is symplectic, $G ^ { - 1 } = I ^ { - 1 } G ^ { T } I$ Hence

$$
\begin{array} { l } { ( Y _ { g } ( t ) m _ { j } , m _ { i } ) = ( G ^ { - 1 } Y ( t ) G m _ { j } , m _ { i } ) \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } } \\ { = ( I ^ { - 1 } G ^ { T } I Y G m _ { j } , m _ { i } ) = ( I Y G m _ { j } , m _ { i } ) . } \end{array}
$$

Since $I m _ { i } = \sqrt { - 1 } m _ { i }$ , this reduces to

$$
( Y _ { g } ( t ) m _ { j } , m _ { i } ) = ( - \sqrt { - 1 } \ I Y ( t ) G m _ { j } , m _ { i } ) = ( J Y ( t ) G m _ { j } , m _ { i } ) .
$$

The vectors $G m _ { s } = f _ { s } ( s = 1 , \dots , n )$ are the eigenvectors of $Y ( \omega )$ corresponding to the multipliers of the first kind,as can be seen from

$$
Y ( \omega ) f _ { s } = \exp { \{ \sqrt { - 1 } \ \theta _ { s } \} } { \cdot } G m _ { s } = \exp { \{ \sqrt { - 1 } \ \theta _ { s } \} } { \cdot } f _ { s } ,
$$

derived from $Y ( \omega ) f _ { s } = G R G ^ { - 1 } m _ { s } = G R m _ { s }$ and

$$
R m _ { s } = \exp \left\{ \sqrt { - 1 } \theta _ { s } \right\} \cdot m _ { s } .
$$

Hence

$$
z ( t ) = ( J Y ( t ) f _ { j } , f _ { i } ) \qquad ( 1 \leq i , j \leq n ) .
$$

Consider a curve $\tilde { Y } ( t )$ $( 0 \leq { t } \leq \omega )$ with $\tilde { Y } ( 0 ) = E _ { 2 n }$ ， and suppose that the end matrix $\tilde { Y } ( \omega )$ lies on the same component as the ends of the curve $ { [ Y _ { \alpha } ( t ) ] }$ . If the equation (188) holds for $\tilde { Y } ( t )$ with the same integer $N$ ，then the condition of homotopicity is satisfied after the end-points of $\tilde { Y } ( t )$ are brought into coincidence with the end-points of a curve of the set $ { [ Y _ { \alpha } ( t ) ] }$ . Thus the curve $\tilde { Y } ( t )$ belongs to the stability domain $[ Y _ { \alpha } ( t ) ]$ .Hence the integer $N$ determines the stability domain $ { [ Y _ { \alpha } ( t ) ] }$ together with the type of distribution of the multipliers.

We obtain the following result :

Theorem 2: Let there be given the solution matrix $Y ( t ) \left( 0 \leq t \leq \omega \right)$ of a strongly stable system，normalized by a condition at zero $\boldsymbol { Y } ( 0 )$ $= E _ { 2 n }$ . We choose an arbitrary basis $h _ { 1 } , h _ { 2 } , \ldots , h _ { n }$ in the subspace spanned by the eigenvectors of the monodromy matrix $Y ( \omega )$ that correspond to multipliers of the first kind,and set up the matrix

$$
z ( t ) = ( J Y ( t ) h _ { j } , h _ { i } ) \qquad ( 1 \leq i , j \leq n ) .
$$

Then the number of the regions to which the given system belongs is found from

$$
N = \frac { 1 } { 2 \pi } \left[ \arg \operatorname* { d e t } z ( t ) | _ { 0 } ^ { \omega } - \sum _ { s = 1 } ^ { \pi } \theta _ { s } \right] ,
$$

where the $\theta _ { s }$ are the principal values of the arguments of the multipliers of the first kind.

Yakubovic (1951） gave an example for $n = 1$ by discussing the criterion of stability of canonical systems of two differential equations with periodic coefficients.He showed that a group of second-order symplectic matrices is homeomorphic to the interior of a torus. By polar factorization $Y = S U$ we obtain

$$
Y = { \binom { S _ { 1 1 } } { S _ { 2 1 } } } \quad S _ { 1 2 } \Biggr ) \Biggl ( \begin{array} { r c l } { { \cos \psi } } & { { \sin \psi } } \\ { { - \sin \psi } } & { { \cos \psi } } \end{array} \Biggr )
$$

with $s _ { 1 1 } s _ { 2 2 } - s _ { 1 2 } ^ { 2 } = I , s _ { 2 2 } > 0$ . The elements of the symmetric positivedefinite matrix $s$ are

$$
\begin{array} { r l r } & { s _ { 1 1 } = \cosh \tau + \sinh \tau \cdot \cos \sigma , } & { s _ { 2 2 } = \cosh \tau - \sinh \tau \cdot \cos \sigma , } \\ & { } & { s _ { 1 2 } = s _ { 2 1 } = \sinh \tau \cdot \sin \sigma \quad ( 0 \leq \sigma \leq 2 \pi , 0 \leq \tau \leq \infty ) . } \end{array}
$$

A point on the surface of a torus is represented by the parameters $\psi , \sigma , \tau _ { : }$ ，where $\phi = \psi , \theta = \sigma , \gamma = \operatorname { t a n h } ^ { 2 } \tau$ ，The matrices of the stable type are determined by $2 | \cos \psi | \cosh \tau < 2$

Segal (1964) discussed the symmetric case in detail by means of a different technique from that of Gelfand and Lidskii for Hamiltonian systems.Let $d = ( T ( t ) , Y ( t ) )$ be a pair of real $n \times n$ matrices,where $\textstyle T ( t )$ is continuous and periodic with period $\omega$ and $Y ( t )$ satisfies

$$
\frac { d } { d t } Y = T Y , \qquad Y ( 0 ) = I .
$$

Segal called $d$ a differential equation and wrote the set of such pairs by $D ( \omega )$ . We have

$$
\begin{array} { r } { Y ( t + n \omega ) = Y ( t ) Y ( n \omega ) = Y ( t ) [ Y ( \omega ) ] ^ { n } . } \end{array}
$$

The power-boundedness of $Y ( \omega )$ ， if we transform $Y ( \omega )$ into the Jordan canonical form,holds if and only if $Y ( \omega )$ satisfies the condition that all its eigenvalues have absolute values less than or equal to unity, and that the eigenvalues with absolute values equal to unity are all proper. Segal called $Y ( \omega )$ the monodromy matrix of $^ d$ If $Y ( \omega )$ is power-bounded, then $d$ is called stable. If $d$ is stable and if there exists a $\tilde { d } = ( \tilde { \cal T } , \tilde { \cal Y } )$ in $D ( \omega )$ such that $\tilde { d }$ is not stable,and if max $| \tilde { T } - T |$ $< k$ for all $t$ in $[ 0 , \omega ]$ ，then $d$ is called weakly stable.If $^ d$ is stable but not weakly stable, $d$ is called strongly stable (see also Section 23.10).

# 16.20 STABILITY IN ABSTRACT SPACE

Let $\pmb { H }$ be a Hilbert space or a Banach space in general. A linear transformation $_ T$ on $\pmb { H }$ to $\pmb { H }$ is said to be completely continuous according to $\mathbf { F }$ .Riesz (Vollstetig,Schauder,1930; totalement continu, Banach，1932） if it transforms the unit sphere $\{ x ; | x | \leq 1 \}$ into a compact subset of $\pmb { H }$ (Section 15.1)； in other words, if the transformed sequence $\{ T x _ { n } \}$ of any bounded sequence $\{ x _ { n } \}$ of points in $\pmb { H }$ contains a convergent subsequence (Reid，1951). A completely continuous transformation $_ T$ is bounded, that is, $\lVert \boldsymbol { T } \rVert \equiv 1 . \mathrm { u . b . } | \boldsymbol { T } \boldsymbol { x } |$ on $\{ x ; | x | \leq 1 \}$ is finite. Let $( x , y ) , x , y \in H$ ,be a bilinear form (Section 16.19).If $\boldsymbol { T }$ is a bounded linear transformation on $\pmb { H }$ to $\pmb { H }$ ,and $( T x , y ) = ( x , T y )$ ， we say that $_ { T }$ is symmetric. For a symmetric transformation the quadratic form $( T x , x )$ is real and is said to be nonnegative if $( T x , x )$ $\geq 0$ for every $x$ in $\pmb { H }$ . For an arbitrary bounded linear transformation $_ T$ the adjoint $T ^ { * }$ is determined by $T ^ { * } = x T x ^ { - 1 }$ for $x \in H$ ，or by the definitive identity $( T x , y ) = ( x , T ^ { * } y )$ . A completely continuous transformation has the properties that for each $k > 0$ there are at most a finite number of eigenvalues $\lambda$ ，such that $T x = \lambda x$ ，satisfying $| \lambda | \geq k$ ， and that, if λ is nonzero and is not an eigenvalue of $_ T$ ，then $\lambda I - T$ has a unique bounded reciprocal $R ( \lambda ) = ( 1 / \lambda ) [ I - Q ( \lambda ) ]$ ，where $\boldsymbol Q ( \lambda )$ is completely continuous.

S. Fomin (195O) studied dynamical systems in function space and V.N.Fomin (1965) considered an operator differential equation with distributed parameter in a separable Hilbert space (Section 16.18)

$$
\sqrt { - 1 } \frac { d } { d t } F x = [ I + \mathfrak { H } ( \tau ) ] x , \qquad \tau = \theta t ,
$$

with the numerical parameter $\theta$ characterizing the perturbation frequency,where $F$ is a self-adjoint operator such that $F = x F x ^ { - 1 }$ ， $x \in H$ ， completely continuous in $\pmb { H }$ and with inverse $F ^ { - 1 }$ ， and the $2 \pi$ -periodic symmetric operator $\mathfrak { H } ( \tau )$ is subordinate to the operator $\pmb { F } ^ { - 1 }$ in the sense that the operator function $F ^ { - 1 } \mathfrak { S } ( \tau )$ is uniformly continuous in the interval $[ 0 , 2 \pi ]$ and that it has a uniformly continuous derivative $d [ F ^ { - 1 } \mathfrak { H } ( \tau ) ] / d \tau$ . By the solution of this equation we mean any continuous function $x ( t )$ such that the function $F x ( t )$ has a strong derivative for almost all $t \in [ 0 , 2 \pi / \theta ]$ and that it satisfies the equation for those values of $t$ .It can be seen that for any $x _ { 0 } \in H$ there exists a unique solution $x ( t )$ which is determined by the condition $x ( 0 ) = x _ { 0 }$ . V. N. Fomin proved the following theorem.

Theorem 1: The operator solution $X ( t )$ of the above Hamiltonian operator equation,specified in terms of the solution $x ( t )$ by the formula $x ( t ) = X ( t ) x ( 0 )$ can be represented by $X ( t ) = U ( t ) + V ( t )$ ，where the operator $U ( t )$ is unitary for any $\pmb { t }$ and $V ( t )$ is completely continuous for any $t$

The proof is based on the circumstance that the operator function $S ( t ) X ( t ) S ^ { - 1 } ( t )$ satisfies an equation not much different from a Schrodinger equation in wave mechanics if $[ I + \mathfrak { H } ( \tau ) ]$ is positivedefinite for all $\tau \in [ 0 , 2 \pi ]$ and if $S ( t )$ is the root of the operator $[ I + \mathfrak { H } ( \theta t ) ]$ . The spectrum (Sections 1.19 and 16.19) of the monodromy operator $X ( 2 \pi \theta ^ { - 1 } )$ consists only of isolated eigenvalues of a finite multiplicity.The computation of such isolated eigenvalues by means of the perturbation theory is reduced to finding the eigenvalues of the self-adjoint operator disturbed by a bounded operator.

Let $_ D$ be a linear set of functions that are $2 \pi \cdot$ -periodic and continuously differentiable,such that the values of these functions and their derivatives belong to the domain of definition of $F ^ { - 1 }$ and are transformed by this operator into continuous functions.We define on the set $_ D$ the scalar product by

$$
[ x , y ] = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } \left[ F ^ { - 1 } x ( \tau ) , F ^ { - 1 } ( y ) \right] d \tau .
$$

The complement of the set $D$ in the metric generated by this scalar product is denoted by $L _ { 2 }$ in the separable Hilbert space. The operator $\tilde { \pmb { S } } _ { 0 }$ generated by the differential expression

$$
\tilde { S } _ { \circ } = \sqrt { - 1 } \frac { d } { d \tau } - \frac { 1 } { \theta } F ^ { - 1 }
$$

on the set $D$ is symmetric,and its closure $S _ { \mathfrak { o } }$ consists of self-adjoint operators in $L _ { 2 }$ . By the definition of $\mathfrak { H } ( \tau )$ , the operator generated by

$$
S _ { 1 } y = - { \frac { 1 } { \theta } } [ F ^ { - 1 } \tilde { \mathcal { Q } } ( \tau ) ] ^ { * } y ( \tau )
$$

is defined everywhere in $L _ { 2 }$ and bounded, where $T ^ { * }$ denotes the adjoint operator of $_ T$ such that $T ^ { * } A = A T$

V.N. Fomin proved that if $\lambda$ is the eigenvalue of the operator $S _ { 0 } + S _ { 1 }$ ，then exp $\{ 2 \pi \sqrt { - 1 } \lambda \}$ is the eigenvalue of the operator $X ( 2 \pi \theta ^ { - 1 } )$ .Conversely，if $\rho$ is an eigenvalue of $X ( 2 \pi \theta ^ { - 1 } )$ ，then $( 2 \pi \sqrt { - 1 } ) ^ { - 1 } \log \rho$ is an eigenvalue of $S _ { 0 } + S _ { 1 }$ . If exp $\{ 2 \pi \sqrt { - 1 } \lambda \}$ belongs to the regularity domain of $X ( 2 \pi \theta ^ { - 1 } )$ in any branch of the logarithm, then the point $\lambda + k$ $k$ an integer） belongs to the regularity domain of $S _ { 0 } + S _ { 1 }$ .The number $\alpha = \sqrt { - 1 } \lambda$ is called the characteristic index of the given operator equation.

Let $\lambda _ { 0 }$ be an arbitrary fixed point of the complex plane,and Ω be a set of points $\lambda$ on the real axis such that $| \lambda - \lambda _ { 0 } | > \delta$ ，where $\delta > 0$ Denote by $E _ { \lambda }$ the spectralfamilyof the operator $S _ { \mathfrak { o } }$ and $P _ { \bar { \circ } } = \int d E _ { \imath }$ The operator $S _ { 0 } - \lambda _ { 0 } I$ is_the bounded inverse in the subspace $\pmb { P } _ { \pmb { \imath } } \pmb { L } _ { 2 }$ ， which is written $( S _ { 0 } - \lambda _ { 0 } I ) ^ { - 1 } P _ { \bar { o } }$ (Sections 20.1 and 26.13).

V.N. Fomin showed that, in order that a number $\lambda$ satisfying the condition $\delta ^ { - 1 } \| ( \lambda - \lambda _ { 0 } ) I - S _ { 1 } \| \ll 1$ be an eigenvalue of the operator $S _ { 0 } + S _ { 1 }$ ,it is necessary and suffcient that this number should be an eigenvalue of the operator $\Phi ( \delta , \lambda , \lambda _ { 0 } )$ generated in the subspace $( I - P _ { \bar { o } } ) L _ { 2 }$ by a matrix with elements

$$
\begin{array} { r l } & { \Phi _ { k l } ( \delta , \lambda , \lambda _ { 0 } ) = [ ( S _ { 0 } + S _ { 1 } ) x _ { l } , y _ { k } ] } \\ & { \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } - [ S _ { 1 } ( I + ( S _ { 0 } + \lambda _ { 0 } I ) ^ { - 1 } P _ { \delta } \{ S _ { 1 } - ( \lambda - \lambda _ { 0 } ) I \} ) ^ { - 1 } } \\ & { \phantom { x x x x x x x x x x x x x x x x x x x x } \times ( S _ { 0 } - \lambda _ { 0 } I ) ^ { - 1 } P _ { \delta } S _ { 1 } x _ { l } , x _ { k } ] , } \end{array}
$$

where $\{ x _ { k } \}$ $( k = 1 , 2 , \ldots , \infty )$ is an orthonormalized base in the subspace $( I - P _ { \bar { o } } ) L _ { 2 }$

Almkvist (1966) discussed the stability of the solution of

$$
{ \frac { d u } { d t } } = A ( t ) u ( t ) \qquad ( t \geq 0 )
$$

in a separable Hilbert space,by assuming that $\mathbf { \nabla } \_ { A \left( t \right) }$ is periodic with period unity and symmetric,and showed that there exists a continuous constant invertible operator $Q$ such that

$$
A ( t ) ^ { * } = - Q \cdot A ( t ) \cdot Q ^ { - 1 }
$$

for all $t \geq 0$ ，with reference to the perturbation technique for $\mathbf { \nabla } A ( t )$ $= A _ { 0 } ( t ) + B ( t )$ ，where $A _ { 0 } ( t )$ is compact and anti-Hermitian for all $t$ Denoting the solution operator of ${ d u } / { d t } = A _ { 0 } ( t ) u ( t )$ by $U _ { \mathfrak { o } }$ ，Almkvist proved that the differential equation is stable if $B ( t )$ satisfies a certain smallness condition involving the distribution of the eigenvalues of $U _ { \mathfrak { o } } ( 1 )$ and the action of $B ( t )$ on these eigenvalues. The result can be applied to the second-order equation $y ^ { \prime \prime } + C ( t ) y = 0$ with self-adjoint $C ( t )$ for all $t$

Kato (1956) considered a linear differential equation in Banach space (Section 20.8).Ura and Kimura (1964) studied the stability in the topological dynamics of Gottschalk and Hedlund (1955) on the basis of Zubov's condition for the stability of a closed invariant set (Daleckii and Krein,1972；Krein,1972；see also Section 23.10 and Smale, 1967).

It is well known that Poincaré (1899) assimilated the motion defined by the solution of a Hamiltonian system as represented by the flow of incompressible fluid.Arnold (1965,1965a) gave conditions for nonlinear stability of stationary flows of an ideal fluid on the basis of Liapounov stability. Suppose that $x _ { 0 }$ is a state of conditional maximum or minimum and that the extremum is nondegenerate,i.e.，the quadratic form $d ^ { 2 } H = d ^ { 2 } E + \lambda _ { 1 } d ^ { 2 } F _ { 1 } + \cdot \cdot \cdot + \lambda _ { k } d ^ { 2 } F _ { k }$ is nondegenerate in the subspace $d F _ { 1 } = 0 , \dots , d F _ { k } = 0$ ；then the position of equilibrium $x _ { 0 }$ is stable.If the linear real system $\dot { \boldsymbol { x } } = A \boldsymbol { x }$ has as a first integral the nondegenerate quadratic form $( B x , x )$ ， then the set of the eigenvalues $\lambda$ of the operator $\pmb { A }$ is symmetric, taking account of the multiplicity，with respect to the real and imaginary axes，and the number of points 𝜆 that lie strictly in the left half-plane $\Re \lambda < 0$ does not exceed the smallest of the indices of inertia $\nu _ { + } , \nu _ { - }$ of the quadratic form $( B x , x )$ -where an index of inertia means the number of positive (or negative) squared terms when the quadratic form is transformed into the sum of squares.

Let $M$ be a real analytic,oriented,compact,and connected Riemannian manifold of three dimensions.Let $a , b$ be two felds of analytic tangent vectors to $M$ such that div $a = 0$ ,div $b = 0$ . Suppose that the first Betti number (see Section 24.9) is zero.Arnold (1965b) proved the

Theorem 2: If the vector felds $^ { a }$ and $^ { b }$ of divergence zero commute, i.e., $[ a , b ] = 0$ ，and are not everywhere collinear，i.e., $a \cap b \not \equiv 0$ ，then almost all trajectories of the field $^ { a }$ are closed or everywhere dense on the analytic tori $T ^ { 2 }$ immersed in $M$ .The other trajectories form an analytic and compact subset of $M$

This theorem is also true if $M$ is a boundary variety with analytic boundary $M ^ { B }$ ，and the field $a$ is tangential to $M ^ { B }$

Let $v$ be the velocity field of the stationary flow of a perfect fuid in $_ D$ ，where $v , D , D ^ { B }$ are real analytic. If $v$ is not collinear with the rotation vector anywhere, then almost all lines of flow are closed or everywhere dense on the analytic real tori immersed in $_ D$ ，and the other lines of flow form an analytic and compact subset of $_ D$ ·

# 16.21APPLICATION TO CONTROLS

Consider an autonomous system

$$
\frac { d x } { d t } = X ( x ) , \qquad X ( 0 ) = 0
$$

around the null solution $x = 0$ where the $X$ are continuous in a domain $G$ of the $x$ -space and satisfy a Lipschitz condition in every closed bounded subregion ${ \overline { { G } } } _ { \mathfrak { s } } \subset G$ ，and also where

$$
\operatorname* { l i m } _ { t \to \infty } x ( x _ { 0 } , t _ { 0 } , t ) = 0 , \qquad x ( x _ { 0 } , t _ { 0 } , t ) \in \Gamma , \qquad t \geq t _ { 0 } ,
$$

for all values of the initial point $x _ { 0 }$ lying in $G _ { \delta }$ ，where $\Gamma \in G$ is given in advance ； then the region $G _ { \delta }$ of the $x$ -space is said to lie in the region of attraction of the point $x = 0$ if the nonperturbed motion is asymptotically stable in the sense of Liapounov (Section 16.3).

Let $\Gamma$ be a region contained in $G$ and containing the point $x = 0$ If the differential equations of the perturbed motion admit a Liapounov function $V$ such that

(i) $V$ is positive-definite in $\mathbf { \Gamma } ^ { \Gamma }$ ， (ii) $V$ admits an infinitely small upper bound in $\Gamma$ ， (i) $\dot { V }$ is negative-definite in $\Gamma$ ， (iv） there are bounded regions $G _ { \delta } , H _ { 0 } , G _ { \delta } \subset H _ { 0 } , { \overline { { H } } } _ { 0 } \subset T$ ， such that the superior bound of $V ( x _ { 1 } , \dots , x _ { n } , t )$ on the boundary of $G _ { \delta }$ for $0 \leq t < \infty$ is smaller than the inferior bound of $V ( x _ { 1 } , \dots , x _ { n } , t )$ on the boundary of $H _ { 0 }$ for $0 < t < \infty$ . Then the nonperturbed motion $x = 0$ is asymptotically stable and the region $G _ { \delta }$ lies in the region of attraction of the point $x = 0$ (Krasovskii, 1963).

When the whole space is the region of asymptotic stability，we say that we have complete stability.In linearized systems the stability is always complete,while it is only in nonlinear systems that it may fail to be complete.

Let $V ( x )$ be a scalar function with continuous first partial derivatives,and $\Omega _ { l }$ be the region where $V ( x ) < l$ 、Assume that $\Omega _ { l }$ is bounded and that within $\Omega _ { \imath }$ the condition $\mathbf { \rho } ( \mathbf { a } ) \colon V ( x ) > 0$ for $x \neq 0$ ，and the condition $( { \mathfrak { b } } ) \colon { \dot { V } } ( x ) \leq 0$ ，are fulfilled.Let $\pmb R$ be the set of all points within $\Omega _ { \iota }$ where $\dot { V } ( x ) = 0$ and $M$ be the largest invariant set in $\pmb R$ Then every solution $x ( t )$ in $\Omega _ { l }$ tends to $M$ as $t \to + \infty$ . An invariant set is characterized by the property that if a point $x _ { 0 }$ of $G$ isin $G$ ， then its whole path starting at $x _ { 0 }$ lies in $G$ for $- \infty < t < + \infty$ .A closed path is an invariant set.

The condition (b) can be replaced by the condition $( \mathsf { b } ^ { * } ) \colon \dot { V } ( x ) < 0$ for all $x \neq 0$ in $\Omega _ { l }$ ; then the origin is asymptotically stable and every solution in $\Omega _ { l }$ tends to the origin as $t \to + \infty$ ·

Let $V ( x )$ be a scalar function with continuous first partial derivatives for all $x$ . Suppose that $V ( x ) > 0$ for all $x \neq 0$ and ${ \dot { V } } ( x ) \leq 0$ Let $\boldsymbol { \varepsilon }$ be the locus $\dot { V } = 0$ and $M$ be the largest invariant set contained in $\boldsymbol { \varepsilon }$ .Then all solutions bounded for $t > 0$ tend to $M$ as $t \to + \infty$ Furthermore suppose that (i) $V ( x ) > 0$ for $x \neq 0$ ，(ii) $\dot { V } < 0$ for $x \neq 0$ and (iii) $V ( t )  \infty$ as $\| { \boldsymbol x } \| \to \infty$ . Then the system ${ \dot { x } } = X ( x )$ ， $X ( 0 ) = 0$ ,is completely stable.

These are suffcient conditions for complete stability but not necessary.

For nonautonomous system we have Malkin's theorem (Malkin, 1952). Consider a disturbed system

$$
\frac { d x } { d t } = X ( x , t ) ,
$$

and the modified perturbed system

$$
\frac { d x } { d t } = X ( x , t ) + R ( x , t ) .
$$

Suppose that there exist for the perturbed system (19O) a Liapounov function $V ( x , t )$ such that it behaves as required by Liapounov's asymptotic stability theorem (Section 16.3) in the basic region $\Omega ( A ) \colon \| x \| < A$ and for all $t \geq 0$ ，that is，there exist three positivedefinite functions ${ \cal W } ( x ) , { \cal W } _ { 1 } ( x ) , { \cal W } _ { 2 } ( x )$ such that in $\Omega ( A )$ and for $t \geq 0$ we have $W _ { 1 } ( x ) \geq V ( x , t ) \geq W ( x )$ ， ${ \dot { V } } ( x , t ) \leqq - W _ { 2 } ( x )$ . Suppose in addition that in $\Omega ( A )$ all partial derivatives $\partial V / \partial x _ { s }$ are bounded for $t \geq 0$ , i.e., there exists an $M > 0$ such that in $\Omega ( A )$

$$
\left| { \frac { \partial V } { \partial x _ { s } } } \right| \leq M , \qquad ( s = 1 , 2 , \ldots , n ; t \geq 0 ) .
$$

Then the origin has such a kind of stability that, given any number $\varepsilon$ $0 < \varepsilon < A$ ， there correspond to it two numbers $0 < \eta _ { 1 } ( \varepsilon )$ ， $0 < \eta _ { 2 } ( \varepsilon )$ so that if $\| x ( 0 ) \| < \eta _ { 1 } ( \varepsilon ) , \| R ( x , t ) \| < \eta _ { 2 } ( \varepsilon )$ for all $\| x \| < \varepsilon$ and $t \geq 0$ then $\| { \boldsymbol { x } } ( t ) \| < \varepsilon$ for all $t \geq 0$

Suppose that the characteristic roots of the real square matrix $\pmb { A }$ all have negative real parts ; then we call the system stable. In order to