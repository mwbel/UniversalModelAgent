# Chapter 7. Symplectic Runge–Kutta Methods

In this chapter we consider symplectic Runge–Kutta (R–K) method.

# 7.1 Multistage Symplectic Runge–Kutta Method

Now we study Multistage Symplectic Runge–Kutta Method. A key feature of the R–K method is using the linear combination of the first-order derivatives of the numerical solution of differential equations to achieve the higher-order approximation.

# 7.1.1 Definition and Properties of Symplectic R–K Method

Consider the following Hamiltonian system:

$$
\begin{array} { l } { \frac { \mathrm { d } p _ { i } } { \mathrm { d } t } = - \frac { \partial H } { \partial q _ { i } } , } \\ { \frac { \mathrm { d } q _ { i } } { \mathrm { d } t } = \frac { \partial H } { \partial p _ { i } } , \qquad i = 1 , 2 , \cdots , n , } \end{array}
$$

where $H = H ( p _ { 1 } , \cdot \cdot \cdot , p _ { n } , q _ { 1 } , \cdot \cdot \cdot , q _ { n } )$ is a Hamiltonian function independent of $t$ . For $t$ -dependent Hamiltonian (e.g., nonautonomous system), we can introduce two new variables and transform the system into another one which has (1.1) $\mathrm { f o r m } ^ { [ \mathrm { Q i n 9 6 } , \mathrm { G o n 9 6 } ] }$ . In order to facilitate the expression, we denote

$$
\boldsymbol { z } = \left[ \begin{array} { c } { p _ { 1 } } \\ { \vdots } \\ { p _ { n } } \\ { q _ { 1 } } \\ { \vdots } \\ { q _ { n } } \end{array} \right] = \left[ \begin{array} { c } { z _ { 1 } } \\ { \vdots } \\ { z _ { n } } \\ { z _ { n + 1 } } \\ { \vdots } \\ { z _ { 2 n } } \end{array} \right] , \quad \boldsymbol { H } _ { \boldsymbol { z } } = \left[ \begin{array} { c } { H _ { z _ { 1 } } } \\ { \vdots } \\ { H _ { z _ { n } } } \\ { \vdots } \\ { H _ { z _ { 2 n } } } \end{array} \right] ,
$$

$$
J = J _ { 2 n } = \left[ \begin{array} { c c } { { O } } & { { I _ { n } } } \\ { { - I _ { n } } } & { { O } } \end{array} \right] , \quad J ^ { \prime } = J ^ { - 1 } = - J ,
$$

where $I _ { n }$ is $n \times n$ identity matrix, $J$ is a standard symplectic matrix. Using this notation, we can rewrite Equation (1.1) into

$$
\frac { \mathrm { d } \boldsymbol { z } } { \mathrm { d } t } = \boldsymbol { J } ^ { - 1 } \boldsymbol { H } _ { \boldsymbol { z } } ,
$$

or

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = J ^ { - 1 } H _ { z } = f ( z ) .
$$

The $s$ -stage R–K method for (1.3) has the following form:

$$
\begin{array} { l } { { \displaystyle z ^ { k + 1 } = z ^ { k } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Y _ { i } ) } , } \\ { { \displaystyle Y _ { i } = z ^ { k } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ) } , \quad 1 \leq i \leq s , } \end{array}
$$

where $h = t _ { k + 1 } - t _ { k } ( k \geq 0 ) , b _ { i } , a _ { i j } ( i , j = 1 , 2 , \cdots , s )$ are real parameters. The properties of a $\mathbf { R - K }$ method (consistency, accuracy, and stability, etc.) are determined completely by these parameters. In scheme (1.4), if $j \geq i$ $( 1 \leq i \leq s )$ ), $a _ { i j } = 0$ , then all $Y _ { i }$

$$
Y _ { i } = z ^ { k } + h \sum _ { j = 1 } ^ { i - 1 } a _ { i j } f ( Y _ { j } ) + a _ { i i } f ( Y _ { i } ) , \quad 1 \leq i \leq s ,
$$

can be computed in an explicit way from $Y _ { 1 } , Y _ { 2 } , \cdots , Y _ { i - 1 }$ . Such scheme is therefore called explicit $\mathbf { R - K }$ scheme. In scheme (1.4), when $j > i$ $\mathit { \Theta } ^ { \prime } 1 \leq i < s )$ , $a _ { i j } = 0$ , and has certain $a _ { i i } \neq 0$ in the diagonal line $1 \leq i \leq s \}$ ), the scheme is called semiimplicit scheme. Each $Y _ { i }$ may defined implicitly by a $2 n$ -dimensional equation. The importance of semi-implicit methods is that the computation of $Y _ { 1 } , Y _ { 2 } , \cdots , Y _ { i - 1 }$ can be carried out in sequence as $s$ system of $2 n$ algebraic equation rather than as one system of $s \times 2 n$ equations. Sometimes we referred this scheme as diagonal implicit. If the method is neither explicit, nor diagonally implicit, and is just called implicit, then all $Y _ { i }$ must be computed simultaneously. Explicit methods are much easier to apply than implicit ones. On the other hand implicit methods possess good stability properties.

Butcher in[But87] proposed the so-called Butcher-array which provides a condensed representation of the R–K method (1.4),

<table><tr><td>C</td><td>A</td></tr><tr><td></td><td>6T</td></tr></table>

where $c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } ( i = 1 , 2 , \cdot \cdot \cdot , s )$ . Thus, a $s$ -stage $\mathbf { R - K }$ method is determined completely by the mathmatical tableau (1.6). Therefore this kind of expression is often called the Butcher tableau (or form).

We regard a single-step difference scheme as a transition mapping from time $t _ { k }$ to $t _ { k + 1 }$ .

Definition 1.1. A symplectic R–K method is a R–K method whose transitional transformation of (1.4), i.e., Jacobian matrix $\frac { \partial z ^ { k + 1 } } { \partial z ^ { k } }$ is symplectic.

Definition 1.2. An $s$ -stage R–K method is said to satisfy simplifying condition if

$$
\begin{array} { r l r l } & { B ( \boldsymbol { p } ) : \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } = \frac { 1 } { k } , } & & { k = 1 ( 1 ) \boldsymbol { p } , } \\ & { C ( \eta ) : \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { c _ { i } ^ { k } } { k } , } & & { k = 1 ( 1 ) \eta , } \\ & { D ( \zeta ) : \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 } a _ { i j } = \frac { b _ { j } ( 1 - c _ { j } ^ { k } ) } { k } , } & & { j = 1 ( 1 ) s , \quad k = 1 ( 1 ) \zeta , } \end{array}
$$

where $A$ is $s \times s$ matrix, $b$ and $c$ are $s \times 1$ vectors of weights and abscissae, respectively.

In 1964 Butcher proved the following fundamental theorem $[ \mathrm { B u t 8 7 } ]$ :

Theorem 1.3. If the coefficients $A , b , c$ of a $R$ –K method satisfy $B ( p ) , C ( \eta ) , D ( \zeta )$ $( p \leq \eta + \zeta + 1$ , and $p \leq 2 \eta + 2 )$ , then the $R$ –K method is of order $p ^ { [ \mathrm { H N W 9 3 } ] }$ .

$\mathbf { R - K }$ method is based on high order quadrature rule. Thus one can derive a R–K method of order $s$ for any set of distinct abscissas $c _ { i } \left( i = 1 , \cdots , s \right)$ . A high order can be obtained for the following special sets of abscissas:

$1 ^ { \circ }$ Using shifted zeros of the Gauss–Legendre polynomial to obtain $c _ { i }$ and condition $C ( s )$ of Definition 1.2 to obtain the Gauss–Legendre method.

$2 ^ { \circ }$ Using zeros of Radau polynomial: (1) $\begin{array} { r l } & { \frac { \mathrm { d } ^ { s - 1 } } { \mathrm { d } x ^ { s - 1 } } \big ( x ^ { s } ( x - 1 ) ^ { s - 1 } \big ) \ ( \mathrm { l e f t \ R a d a u } ) , } \\ & { \frac { \mathrm { d } ^ { s - 1 } } { \mathrm { d } x ^ { s - 1 } } \big ( x ^ { s - 1 } ( x - 1 ) ^ { s } \big ) \ ( \mathrm { r i g h t \ R a d a u } ) , } \end{array}$ (2)

with condition $D ( s )$ of Definition 1.2 to obtain Radau I A method, or with condition $C ( s )$ to obtain Radau $\mathrm { I I }$ A method.

$3 ^ { \circ }$ Using zeros of Lobatto polynomial

$$
{ \frac { \mathrm { d } ^ { s - 2 } } { \mathrm { d } x ^ { s - 2 } } } \left( x ^ { s - 1 } ( x - 1 ) ^ { s - 1 } \right)
$$

with coefficients $b _ { i }$ satisfying condition $1 . 2 B ( 2 s - 2 )$ to obtain

(1) Lobatto III A if $a _ { i j }$ is determined by $C ( s )$ ; (2) Lobatto III B if $D ( s )$ is satisfied; (3) Lobatto III C if $a _ { i 1 } = b _ { 1 }$ , $\forall \ i = 1 , \cdots , s$ , and the rest of $a _ { i j }$ is determined by $C ( s - 1 )$ .

Radau I A:

![](images/7633cbf776275e1b5360ad6883469ea9b827a1b96a90b763bdb03c1a8a0690de.jpg)

Radau II A:

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr></table>

<table><tr><td>1</td><td>5</td><td>1 12</td></tr><tr><td>1</td><td>3 4</td><td>1</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>3-4</td><td>4</td></tr></table>

Lobatto III A:

<table><tr><td>0</td><td>0 0</td></tr><tr><td>1</td><td>1 1</td></tr><tr><td></td><td>1-2 1</td></tr></table>

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>5</td><td></td><td>1</td></tr><tr><td>1</td><td>24</td><td>13</td><td>24</td></tr><tr><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>23</td><td>1</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1</td><td>2</td><td>1</td></tr></table>

Lobatto III B:

<table><tr><td>0</td><td>1 0</td></tr><tr><td>1</td><td>1 0</td></tr><tr><td></td><td>1 1</td></tr></table>

<table><tr><td>0</td><td>1</td><td>1 0</td></tr><tr><td>1</td><td>1</td><td>1 0</td></tr><tr><td></td><td></td><td></td></tr><tr><td>1</td><td>1</td><td>56 0</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>1 2-3</td><td>1</td></tr></table>

Lobatto III C:

<table><tr><td colspan="4"></td><td></td><td></td></tr><tr><td rowspan="4">0</td><td></td><td></td><td>1</td><td>1 一</td><td>1</td></tr><tr><td>1</td><td>1-2 一</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>5</td><td>1</td></tr><tr><td></td><td>1</td><td>1</td><td>12</td><td>12</td></tr><tr><td rowspan="3">1</td><td>1</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>1</td><td>23</td><td>1</td></tr><tr><td></td><td></td><td>6</td><td></td><td>6</td></tr><tr><td rowspan="4"></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td>2</td><td>1</td></tr><tr><td></td><td></td><td>1</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

We present a table of these conditions for methods which are based on high order quadrature rule, see Table 1.1.

Table 1.1. The simplified conditions for $s$ -stage method based on high order quadrature rule   

<table><tr><td>method</td><td>simplified</td><td>condition</td><td>order of accuracy</td><td>Padé approx</td></tr><tr><td>Gauss-Legendre</td><td>B(2s) C(s)</td><td>D(s)</td><td>2s</td><td>(s,s)</td></tr><tr><td>Radau I A</td><td>B(2s -1) C(s-1)</td><td>D(s)</td><td>2s-1</td><td>(s-1,s)</td></tr><tr><td>Radau II A</td><td>B(2s-1) C(s)</td><td>D(s-1)</td><td>2s-1</td><td>(s-1,s)</td></tr><tr><td>Lobatto III A</td><td>B(2s-2) C(s)</td><td>D(s-2)</td><td>2s-2</td><td>(s-1,s-1)</td></tr><tr><td>Lobatto II B</td><td>B(2s-2) C(s-2)</td><td>D(s)</td><td>2s-2</td><td>(s-1,s-1)</td></tr><tr><td>Lobatto III C</td><td>B(2s-2) C(s-1)</td><td>D(s-1)</td><td>2s-2</td><td>(s-2,s)</td></tr></table>

# 7.1.2 Symplectic Conditions for R–K Method

In this subsection a sufficient condition for $\mathbf { R - K }$ method to be symplectic is given. Let $B = \mathrm { d i a g } [ b _ { 1 } , b _ { 2 } , \cdot \cdot \cdot , b _ { s } ]$ be a diagonal matrix, $M = B A + A ^ { \prime } B - b b ^ { \prime }$ . The following condition was first proposed by Sanz-Serna during his visit to China[SS88] .

Theorem 1.4. If $M = 0$ , then an $s$ -stage $R$ –K method (1.4) is symplectic[SS88,Las88,Sur88] .

Proof. Here we give our own proof $[ 0 Z 9 2 \mathrm { a } ]$ . To prove the scheme (1.4) is symplectic when $M = 0$ , we only need to verify the Jacobian matrix is symplectic. From the scheme (1.4) we have

$$
\begin{array} { r l r } & { \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } = I + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \mathbb { D } f ( Y _ { i } ) \frac { \partial Y _ { i } } { \partial z ^ { k } } , } & \\ & { \frac { \partial Y _ { i } } { \partial z ^ { k } } = I + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } \mathbb { D } f ( Y _ { j } ) \frac { \partial Y _ { j } } { \partial z ^ { k } } , } & { 1 \leq i \leq s , } \end{array}
$$

where $\ Ḋ \mathrm Ḋ f Ḍ Ḍ$ is the derivative of function $f$ .

Denote $D _ { i } = \operatorname { D } f ( Y _ { i } ) , { \frac { \partial Y _ { i } } { \partial z ^ { k } } } = X _ { i } ( i = 1 , 2 , \cdots , s )$ , and let $f = J ^ { - 1 } H _ { z }$ , then

$$
J D _ { i } + D _ { i } ^ { \prime } J = 0 ,
$$

and

$$
\begin{array} { r l } { \left( \displaystyle \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } \right) ^ { \prime } J \displaystyle \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } } & { = \ J + h \left( \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } D _ { i } X _ { i } \right) ^ { \prime } J + h . J \left( \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } D _ { i } X _ { i } \right) } \\ & { \quad + \left( h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } D _ { i } X _ { i } \right) ^ { \prime } J \left( \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } D _ { i } X _ { i } \right) } \\ & { = \ J + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } \left[ ( D _ { i } X _ { i } ) ^ { \prime } J + J D _ { i } X _ { i } \right] } \\ & { \quad + h ^ { 2 } \left( \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } D _ { i } X _ { i } \right) ^ { \prime } J \left( \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } D _ { i } X _ { i } \right) . } \end{array}
$$

It follows from (1.8)

$$
\begin{array} { l } { { ( D _ { i } X _ { i } ) ^ { \prime } J X _ { i } = ( D _ { i } X _ { i } ) ^ { \prime } J + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } ( D _ { i } X _ { i } ) ^ { \prime } J D _ { j } X _ { j } , } } \\ { { \ } } \\ { { ( X _ { i } ) ^ { \prime } J D _ { i } X _ { i } = J D _ { i } X _ { i } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } ( D _ { j } X _ { j } ) ^ { \prime } J D _ { i } X _ { i } . } } \end{array}
$$

Using Equation (1.9), we obtain

$$
\begin{array} { r l } { \left( \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } \right) ^ { \prime } J \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } } & { = \ J + \left( \boldsymbol { h } \underset { \underset { i = 1 } { \overset { s } { \prod } } b _ { i } J _ { i } A _ { i } } { \overset { s } { \prod } } J _ { i } \left( \underset { s = 1 } { \overset { s } { \prod } } b _ { i } J _ { i } , X _ { i } \right) \right. ^ { \prime } J _ { i } \left( \underset { s = 1 } { \overset { s } { \prod } } b _ { i } J _ { i } , X _ { i } \right) } \\ & { \qquad \left. + \boldsymbol { h } \underset { \underset { i = 1 } { \overset { s } { \prod } } b _ { i } } { \overset { s } { \prod } } [ X _ { i } ^ { \prime } , J _ { i } ^ { \prime } , X _ { i } + X _ { i } ^ { \prime } , J _ { i } ^ { \prime } , X _ { i } ] \right. } \\ & { - \boldsymbol { h } \underset { \underset { i = 1 } { \overset { s } { \prod } } b _ { i } } { \overset { s } { \prod } } \left[ \underset { j = 1 } { \overset { s } { \prod } } a _ { i j } ( D _ { i } \boldsymbol { \bar { X } } _ { i } ) ^ { \prime } J \boldsymbol { D } _ { j } X _ { j } \right. } \\ & { \qquad \left. + \boldsymbol { h } \underset { \underset { i = 1 } { \overset { s } { \prod } } a _ { i j } ( D _ { i } \boldsymbol { \bar { X } } _ { i } ) ^ { \prime } J \boldsymbol { D } _ { i } X _ { j } } { \overset { s } { \prod } } \right] } \\ & { = \ J + \boldsymbol { h } ^ { 2 } \underset { \underset { i = 1 } { \overset { s } { \prod } } b _ { i } } { \overset { s } { \prod } } ( b _ { i } J _ { i } - b _ { i } a _ { i } ) - b _ { i } a _ { i } b _ { i } J _ { i } ( D _ { i } \boldsymbol { \bar { X } } _ { i } ) ^ { \prime } J \boldsymbol { D } _ { j } X _ { i } . } \end{array}
$$

It is easy to see that if $M = 0$ , then

$$
\left( \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } \right) ^ { \prime } J \frac { \partial z ^ { k + 1 } } { \partial z ^ { k } } = J ,
$$

i.e., the Jacobian matrix of transitional mapping $\frac { \partial z ^ { k + 1 } } { \partial z ^ { k } }$ is symplectic.

Remark 1.5. If $\mathbf { R - K }$ method is non-reducible, then condition $M = 0$ is also necessary.

From subsection 7.1.1 we know that a $\mathbf { R - K }$ method is determined completely by the coefficients $c _ { i } , a _ { i j } , b _ { i }$ $( i , j = 1 , \cdots , s )$ . Now we introduce the Gauss–Legendre method: let $c _ { i }$ $( i = 1 , \cdots , s )$ be zeros of shifted Legendre polynomial $Q _ { s } ( x )$ , where the Legendre polynomials are defined as

$$
\begin{array} { l } { { P _ { s } ( x ) = \displaystyle \frac { 1 } { 2 ^ { s } s ! } \frac { \mathrm { d } ^ { s } } { \mathrm { d } x ^ { s } } \{ ( x ^ { 2 } - 1 ) ^ { s } \} , } } \\ { { Q _ { s } ( x ) = P _ { s } \left( x - \displaystyle \frac { 1 } { 2 } \right) . } } \end{array}
$$

Let this method satisfy simplified conditions $B ( s )$ and $C ( s )$ . Solve equations $\sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { k - 1 }$ $= { \frac { 1 } { k } } \left( 1 \leq k \leq s \right) { \mathrm { f o r ~ } } b _ { i } \ ( i = 1 , \cdots , s ) { \mathrm { , ~ a n d ~ s o l v e ~ e q u a t i o n s } } \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = { \frac { 1 } { k } } c _ { i } ^ { k } \left( 1 + { \frac { 1 } { 2 } } { \frac { s } { \alpha { \mathrm { , ~ i ~ } } s } } \right) ,$ ≤ $k \leq s , 1 \leq i \leq s )$ ) for $a _ { i j }$ $( i , j = 1 , \cdots , s )$ . Then the scheme determined by $b _ { i }$ and $a _ { i j }$ is the only R–K method that has achieved $2 s$ -order of accuracy. We listed Butcher’s tableau for $s \leq 2$ as follows

$s = 1$ :

<table><tr><td>1</td><td>1 2</td></tr><tr><td></td><td>1</td></tr></table>

$s = 2$ :

<table><tr><td>3-√3</td><td>1-4</td><td>3-2√3</td></tr><tr><td>6</td><td></td><td>12</td></tr><tr><td>3+√3</td><td>3+2√3</td><td>1</td></tr><tr><td>6</td><td>12</td><td>4</td></tr><tr><td></td><td>1</td><td>1</td></tr><tr><td></td><td></td><td></td></tr></table>

It is easy to see that $s = 1$ is exactly the case of the Euler centered scheme:

$$
z ^ { k + 1 } = z ^ { k } + h f \left( { \frac { 1 } { 2 } } ( z ^ { k } + z ^ { k + 1 } ) \right) .
$$

It is not difficult to verify that both schemes (1.12) and (1.13) satisfy the conditions $M = 0$ , and hence are symplectic. Furthermore, we have the following conclusions:

Theorem 1.6. An $s$ -stage Gauss–Legendre method is a symplectic scheme with $2 s$ - order of accuracy.

Proof. Since the scheme satisfies conditions $D ( s ) , C ( s ) , B ( 2 s )$ , i.e.,

$$
\begin{array} { r l r } {  { \sum _ { i = 1 } ^ { s } b _ { i } a _ { i j } c _ { i } ^ { l - 1 } \ = \ \frac { 1 } { l } b _ { j } ( 1 - c _ { j } ^ { l } ) = \frac { 1 } { l } b _ { j } - \frac { 1 } { l } b _ { j } c _ { j } ^ { l } } } \\ & { } & \\ & { } & { = \ \sum _ { i = 1 } ^ { s } b _ { i } b _ { j } c _ { i } ^ { l - 1 } - \sum _ { i = 1 } ^ { s } b _ { j } a _ { j i } c _ { i } ^ { l - 1 } , } \end{array}
$$

which results in

$$
\sum _ { i = 1 } ^ { s } ( b _ { i } a _ { i j } + b _ { j } a _ { j i } - b _ { i } b _ { j } ) c _ { i } ^ { l - 1 } = 0 , \quad l , j = 1 , 2 , \cdots , s .
$$

Since $c _ { 1 } , c _ { 2 } , \cdots , c _ { s }$ are not equal mutually, we obtain $M = 0$ .

# 7.1.3 Diagonally Implicit Symplectic R–K Method

In this subsection, we will give some diagonal symplectic $\mathbf { R - K }$ formulas. These schemes not only have advantages with regards to computational convenience and good stability, but also are symplectic.

Let us consider a diagonally $s$ -stage implicit R–K method that satisfies $M = 0$ . Without loss of generality we assume that $b _ { i } \neq 0$ $( i = 1 , 2 , \cdots , s )$ ). Because of the condition $M = 0$ , we have

$$
b _ { i } b _ { j } - b _ { i } a _ { i j } - b _ { j } a _ { j i } = 0 , \quad i , j = 1 , 2 , \cdot \cdot \cdot , s .
$$

If $b _ { k } = 0$ , then $b _ { i } a _ { i k } = 0 ( i = 1 , 2 , \cdot \cdot , s )$ , the method is equivalent to a method with fewer stages.

The following theorem is first proposed by the authors, sees the literature $[ \mathrm { Q Z 9 2 a } , \mathrm { S A 9 1 } ]$

Theorem 1.7. If an $s$ -stage diagonally implicit method satisfies $M = 0$ , then we can write the method in the following form:

$$
c _ { i } = \sum _ { j = 1 } ^ { i } b _ { j - 1 } + { \frac { b _ { i } } { 2 } } ( i = 1 , \cdots , s , b _ { 0 } = 0 ) .
$$

Proof. Since the scheme is diagonally implicit, $a _ { i j } = 0 \ : ( j > i )$ ; to satisfy $M = 0$ , we have $b _ { i } b _ { j } - b _ { i } a _ { i j } - b _ { j } a _ { j i } = 0$ $( i , j = 1 , 2 , \cdots , s )$ , which results in

$$
a _ { i j } = b _ { j } , \quad a _ { i i } = { \frac { b _ { i } } { 2 } } , \quad i = 1 , \cdots , s , \quad i > j .
$$

The theorem is proved.

Corollary 1.8. Explicit R–K method with any order does not satisfy condition $M = 0$

Remark 1.9. Tableau (1.16) Cooper[Coo87] has discussed the condition (1.15) and constructed a method of family (1.16) with $s = 3$ and order 3.

Below we give diagonally implicit symplectic $\mathbf { R - K }$ methods for $s \leq 3$ : $s = 1$ :

<table><tr><td>1</td><td>1 2</td></tr><tr><td></td><td>1</td></tr></table>

$s = 2$ :

<table><tr><td>1</td><td>4 0</td></tr><tr><td>4</td><td>1 41</td></tr><tr><td></td><td></td></tr><tr><td></td><td>1 1</td></tr></table>

$s = 3$ :

<table><tr><td>1 a</td><td></td><td></td><td></td><td></td></tr><tr><td>3-2 a</td><td>a</td><td>1 a</td><td></td><td></td></tr><tr><td>1 十 a</td><td>a</td><td>a</td><td>1</td><td>a</td></tr><tr><td></td><td>a</td><td>a</td><td>1-2a</td><td></td></tr></table>

where $a = 1 . 3 5 1 2 0 7$ , which is a real root of polynomial $6 x ^ { 3 } - 1 2 x ^ { 2 } + 6 x - 1 { } ^ { [ \mathrm { C o o 8 7 } ] }$ .   
The above three schemes have accuracy $o ( \Delta t ^ { 2 } ) , o ( \Delta t ^ { 2 } ) , o ( \Delta t ^ { 3 } )$ respectively.

Corollary 1.10. If $s = 3$ , and the elements in Butcher tableau are taken in symmetrical version $( a _ { 1 1 } = a _ { 3 3 }$ ).

Then this scheme has 4th-order accuracy.

In Chapter 8 we will see that this is a typical example that using Euler centered scheme and multiplication extrapolation to achieve 4th order accuracy.

Now we consider $s = 4$ , Butcher tableau can be represented as follows:

We expect this method to have 4th-order accuracy. According to Taylor expansion, the coefficients in the method must satisfy the system of equations:

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } = 1 , } \\ & { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } = \frac { 1 } { 2 } , } \\ & { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } = \frac { 1 } { 3 } , } \\ & { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 2 } = \frac { 1 } { 3 } , } \\ & { \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { i j } c _ { j } = \frac { 1 } { 6 } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { 3 } = \frac { 1 } { 4 } } , } \\ { { \displaystyle \sum _ { i , j = 1 \atop i , j = 1 } ^ { s } b _ { i } c _ { i } a _ { i j } c _ { j } = \frac { 1 } { 8 } } , } \\ { { \displaystyle \sum _ { i , j = 1 } ^ { s } b _ { i } a _ { i j } c _ { j } ^ { 2 } = \frac { 1 } { 1 2 } } , } \\ { { \displaystyle \sum _ { i , j , k = 1 } ^ { s } b _ { i } a _ { i j } a _ { j k } c _ { k } = \frac { 1 } { 2 4 } } } \end{array}
$$

Now we have 8 equations with 4 unknowns. Luckily we find a set of solutions using computer, which is

$$
\begin{array} { l l } { { b _ { 1 } = - 2 . 7 0 3 0 9 4 1 2 , } } & { { b _ { 2 } = - 0 . 5 3 6 5 2 7 0 8 , } } \\ { { { } } } & { { { } } } \\ { { b _ { 3 } = 2 . 3 7 8 9 3 9 3 1 , } } & { { b _ { 4 } = 1 . 8 6 0 6 8 1 8 8 5 6 . } } \end{array}
$$

Perhaps we can reduce the equations to the form of 4 equations with 4 unknowns and s   
get the exact solution. For an example, using $\sum _ { i = 1 } ^ { \cdot } b _ { i } = 1 , b _ { i } b _ { j } - b _ { i } a _ { i j } = 0 ( i , j =$   
$1 , 2 , \cdots , s )$ , we have $\sum _ { = 1 , j = 1 } ^ { s } b _ { i } a _ { i , j } \ = \ \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } \ = \ \frac { 1 } { 2 }$ So we can remove Equation i   
(1.23) from the system. In an implementation of this $\mathbf { R - K }$ method, we rewrite it in the   
following form:

$$
\begin{array} { l } { { Y _ { 1 } = z ^ { k } + \frac { b _ { 1 } h } { 2 } f ( Y _ { 1 } ) , } } \\ { { \ } } \\ { { Y _ { 2 } = 2 Y _ { 1 } - z ^ { k } + \frac { b _ { 2 } h } { 2 } f ( Y _ { 2 } ) , } } \\ { { \ } } \\ { { Y _ { 3 } = 2 Y _ { 2 } - ( 2 Y _ { 1 } - z ^ { k } ) + \frac { b _ { 3 } h } { 2 } f ( Y _ { 3 } ) , } } \\ { { \ } } \\ { { Y _ { 4 } = 2 Y _ { 3 } - ( 2 Y _ { 2 } - 2 Y _ { 1 } + z ^ { k } ) + \frac { b _ { 4 } h } { 2 } f ( Y _ { 4 } ) , } } \\ { { \ } } \\ { { z ^ { k + 1 } = 2 Y _ { 4 } - ( 2 Y _ { 3 } - 2 Y _ { 2 } + 2 Y _ { 1 } - z ^ { k } ) . } } \end{array}
$$

Corollary 1.11. This scheme (1.30) can be obtained by applying the implicit midpoint scheme over 4 steps of length $b _ { 1 } h , b _ { 2 } h , b _ { 3 } h , b _ { 4 } h .$ . It has 4-th order accuracy.

Let

$$
\begin{array} { l } { { z ^ { \frac { 1 } { 4 } } = z ^ { 0 } + b _ { 1 } h f \Big ( \frac { z ^ { \frac { 1 } { 4 } } + z ^ { 0 } } { 2 } \Big ) , } } \\ { { z ^ { \frac { 2 } { 4 } } = z ^ { \frac { 1 } { 4 } } + b _ { 2 } h f \Big ( \frac { z ^ { \frac { 2 } { 4 } } + z ^ { \frac { 1 } { 4 } } } { 2 } \Big ) , } } \\ { { z ^ { \frac { 3 } { 4 } } = z ^ { \frac { 2 } { 4 } } + b _ { 3 } h f \Big ( \frac { z ^ { \frac { 3 } { 4 } } + z ^ { \frac { 2 } { 4 } } } { 2 } \Big ) , } } \\ { { z ^ { 1 } = z ^ { \frac { 3 } { 4 } } + b _ { 4 } h f \Big ( \frac { z ^ { 1 } + z ^ { \frac { 3 } { 4 } } } { 2 } \Big ) , } } \end{array}
$$

Rewrite it in the following form:

$$
\begin{array} { r l r } & { } & { \frac { z ^ { \frac { 3 } { 4 } } + z ^ { 0 } } { 2 } = z ^ { 0 } + \frac { b _ { 1 } } { 2 } h f \left( \frac { z ^ { \frac { 1 } { 4 } } + z ^ { 0 } } { 2 } \right) , } \\ & { } & { \frac { z ^ { \frac { 2 } { 4 } } + z ^ { \frac { 1 } { 4 } } } { 2 } = z ^ { \frac { 1 } { 4 } } + \frac { b _ { 2 } } { 2 } h f \left( \frac { z ^ { \frac { 2 } { 4 } } + z ^ { \frac { 1 } { 4 } } } { 2 } \right) , } \\ & { } & { \frac { z ^ { \frac { 3 } { 4 } } + z ^ { \frac { 2 } { 4 } } } { 2 } = z ^ { \frac { 2 } { 4 } } + \frac { b _ { 3 } } { 2 } h f \left( \frac { z ^ { \frac { 3 } { 4 } } + z ^ { \frac { 2 } { 4 } } } { 2 } \right) , } \\ & { } & { \frac { z ^ { \frac { 3 } { 4 } } + z ^ { \frac { 3 } { 4 } } } { 2 } = z ^ { \frac { 3 } { 4 } } + \frac { b _ { 4 } } { 2 } h f \left( \frac { z ^ { 1 } + z ^ { \frac { 3 } { 4 } } } { 2 } \right) . } \end{array}
$$

Let

$$
\begin{array} { l l } { { \displaystyle { \frac { z ^ { 0 } + z ^ { \frac { 1 } { 4 } } } { 2 } } = Y _ { 1 } , } } & { { \displaystyle { \frac { z ^ { \frac { 1 } { 4 } } + z ^ { \frac { 2 } { 4 } } } { 2 } } = Y _ { 2 } , } } \\ { { \displaystyle { \frac { z ^ { \frac { 2 } { 4 } } + z ^ { \frac { 3 } { 4 } } } { 2 } } = Y _ { 3 } , } } & { { \displaystyle { \frac { z ^ { \frac { 3 } { 4 } } + z ^ { 1 } } { 2 } } = Y _ { 4 } , } } \end{array}
$$

then (1.32) becomes scheme (1.30).

There are similar results for $s \leq 3$ . More detail can be seen later in Section 8.1. All schemes proposed in this section can be applied to general ODE’s as well.

Exercise 1.12. Does there exist 5-stage diagonally implicit R–K method with 5thorder accuracy?

# 7.1.4 Rooted Tree Theory

# 1. High order derivatives and rooted tree theory

The basic method to construct the numerical scheme for ordinary differential equations is Taylor expansion. If only a single (scalar) equation is considered, Taylor expansion can be used in studying the convergence, compatibility, and order conditions for $\mathbf { R - K }$ methods. However, if the system of differential equations are considered, Taylor expansion is intractable. Consider system of ODE’s:

$$
\dot { y } = f ( y ) , \quad y ( 0 ) = \eta , \quad f : { \mathbf R } ^ { m }  { \mathbf R } ^ { m } , \quad m > 1 .
$$

For brevity, let $m = 2$ , and $y = ( ^ { 1 } y , ^ { 2 } y ) ^ { \prime } , f = ( ^ { 1 } f , ^ { 2 } f ) ^ { \prime }$ , introduce the following notations

$$
{ } ^ { i } f _ { j } : = \frac { \partial ^ { i } f } { \partial ( { } ^ { j } y ) } , \quad { } ^ { i } f _ { j k } : = \frac { \partial ^ { 2 } ( { } ^ { i } f ) } { \partial ( { } ^ { j } y ) \partial ( { } ^ { k } y ) } ,
$$

we have

$$
\begin{array} { l l } { { { } ^ { 1 } y ^ { ( 1 ) } = { } ^ { 1 } f , } } & { { { } ^ { 2 } y ^ { ( 1 ) } = { } ^ { 2 } f , } } \\ { { { } ^ { 1 } y ^ { ( 2 ) } = { } ^ { 1 } f _ { 1 } ( { } ^ { 1 } f ) + { } ^ { 1 } f _ { 2 } ( { } ^ { 2 } f ) , } } & { { { } ^ { 2 } y ^ { ( 2 ) } = { } ^ { 2 } f _ { 1 } ( { } ^ { 1 } f ) + { } ^ { 2 } f _ { 2 } ( { } ^ { 2 } f ) . } } \end{array}
$$

Using matrix and vector symbols, we have

$$
y ^ { ( 2 ) } = { \left[ \begin{array} { l l } { ^ { 1 } f _ { 1 } } & { ^ { 1 } f _ { 2 } } \\ { } & { } \\ { ^ { 2 } f _ { 1 } } & { ^ { 2 } f _ { 2 } } \end{array} \right] } f .
$$

The second order derivative can be expressed via Jacobian matrix. However, the third-order derivative $y ^ { ( 3 ) }$ , can no longer be expressed via matrix and vector symbol, not to mention the higher order derivative. This has motivated people to study the structure of the Taylor expansion of high order derivatives and search for a better symbol to simplify the Taylor expansion of high order derivatives. Then the rooted tree theory[But87,Lam91,HNW93,SSC94] (With the tree roots skill to express high order derivative) emerged. Take $y ^ { ( 3 ) }$ as an example:

$$
\begin{array} { r l } { ^ { 1 } y ^ { ( 3 ) } \ = \ ^ { 1 } f _ { 1 1 } ( ^ { 1 } f ) ^ { 2 } + ^ { 1 } f _ { 1 2 } ( ^ { 1 } f ) ( ^ { 2 } f ) + ^ { 1 } f _ { 1 } \big ( ^ { 1 } f _ { 1 } ( ^ { 1 } f ) + ^ { 1 } f _ { 2 } ( ^ { 2 } f ) \big ) } \\ & { \quad + ^ { 1 } f _ { 2 1 } ( ^ { 2 } f ) ( ^ { 1 } f ) + ^ { 1 } f _ { 2 2 } ( ^ { 2 } f ) ^ { 2 } + ^ { 1 } f _ { 2 } \big ( ^ { 2 } f _ { 1 } ( ^ { 1 } f ) + ^ { 2 } f _ { 2 } ( ^ { 2 } f ) \big ) , } \\ { ^ { 2 } y ^ { ( 3 ) } \ = \ ^ { 2 } f _ { 1 1 } ( ^ { 1 } f ) ^ { 2 } + ^ { 2 } f _ { 1 2 } ( ^ { 1 } f ) ( ^ { 2 } f ) + ^ { 2 } f _ { 1 } \big ( ^ { 1 } f _ { 1 } ( ^ { 1 } f ) + ^ { 1 } f _ { 2 } ( ^ { 2 } f ) \big ) } \\ & { \quad + ^ { 2 } f _ { 2 1 } ( ^ { 2 } f ) ( ^ { 1 } f ) + ^ { 2 } f _ { 2 2 } ( ^ { 2 } f ) ^ { 2 } + ^ { 2 } f _ { 2 } \big ( ^ { 2 } f _ { 1 } ( ^ { 1 } f ) + ^ { 2 } f _ { 2 } ( ^ { 2 } f ) \big ) . } \end{array}
$$

Definition 1.13. Let $z$ , $f ( z ) \in \mathbf { R } ^ { m }$ , $f ^ { ( M ) } ( z )$ be the $M$ -th Frechet derivatives of $f$ . It is an operator on $\mathbf { R } ^ { m } \times \mathbf { R } ^ { m } \times \cdot \cdot \cdot \times \mathbf { R } ^ { m }$ ( $M$ times), and is linear in each operand,

$$
\begin{array} { l } { { \displaystyle f ^ { ( M ) } ( z ) ( K _ { 1 } , K _ { 2 } , \cdots , K _ { M } ) } } \\ { { \displaystyle \quad = \sum _ { i = 1 } ^ { m } \sum _ { j _ { 1 } = 1 } ^ { m } \sum _ { j _ { 2 } = 1 } ^ { m } \cdots \sum _ { j _ { M } = 1 } ^ { m } { } ^ { i } f _ { j _ { 1 } j _ { 2 } \cdots j _ { M } } { } ^ { j _ { 1 } } K _ { 1 } ^ { j _ { 2 } } K _ { 2 } \ldots { } ^ { j _ { M } } K _ { M } \cdot e _ { i } , } } \end{array}
$$

where $z$ is the argument, $K _ { 1 } , K _ { 2 } , \cdots , K _ { M }$ operands, and

$$
\begin{array} { l } { { \displaystyle K _ { t } ~ = ~ \left( { ^ 1 } K _ { t } , { ^ 2 } K _ { t } , \cdot \cdot \cdot , { ^ m } K _ { t } \right) ^ { \mathrm { T } } \in { \bf R } ^ { m } , \quad t = 1 , 2 , \cdot \cdot \cdot , M , } } \\ { { \displaystyle i \ f _ { j _ { 1 } j _ { 2 } \cdots j _ { M } } ~ = ~ \frac { \partial ^ { M } } { \partial ( ^ { j _ { 1 } } z ) \partial ( ^ { j _ { 2 } } z ) \cdot \cdot \cdot \cdot \partial ( ^ { j _ { M } } z ) } i f ( z ) } } \end{array}
$$

and

$$
e _ { i } = [ 0 , 0 , \cdots , 0 , \underbrace { 1 } _ { i } , 0 , \cdots , 0 ] ^ { \mathrm { T } } \in \mathbf { R } ^ { m } .
$$

We have the following comments:

(1) The value of $f ^ { ( \bar { M } ) } ( z ) ( \cdots )$ is a vector in $\mathbf { R } ^ { m }$ . (2) Repeated subscripts are permitted in (1.37), so that all possible partial derivatives of order $M$ are involved. Thus, if $M = 3 , m = 2$ , the following partial derivatives will appear:

$$
\begin{array} { r l r } & { { } ^ { i } f _ { 1 1 1 } = \displaystyle \frac { \partial ^ { 3 } ( { } ^ { i } f ) } { \partial ( { } ^ { 1 } z ) ^ { 3 } } ; \quad { } ^ { i } f _ { 1 1 2 } = { } ^ { i } f _ { 1 2 1 } = { } ^ { i } f _ { 2 1 1 } = \displaystyle \frac { \partial ^ { 3 } ( { } ^ { i } f ) } { \partial ( { } ^ { 1 } z ) ^ { 2 } \partial ( { } ^ { 2 } z ) } , } & \\ & { { } ^ { i } f _ { 1 2 2 } = { } ^ { i } f _ { 2 1 2 } = { } ^ { i } f _ { 2 2 1 } = \displaystyle \frac { \partial ^ { 3 } ( { } ^ { i } f ) } { \partial ( { } ^ { 1 } z ) \partial ( { } ^ { 2 } z ) ^ { 2 } } , \quad { } ^ { i } f _ { 2 2 2 } = \displaystyle \frac { \partial ^ { 3 } ( { } ^ { i } f ) } { \partial ( { } ^ { 2 } z ) ^ { 3 } } , } & \end{array} \quad i = 1 , 2 .
$$

(3) The argument $z$ simply denotes the vector with respect to whose component we are performing the partial differentiations.

(4) An $M$ times Frechet derivatives has $M$ operands. This is an important property to note.

Take $m = 2$ , we have

Case $M = 1$

$$
\begin{array} { l l l } { { f ^ { ( 1 ) } ( z ) ( K _ { 1 } ) ~ = ~ \displaystyle \sum _ { i = 1 } ^ { 2 } \sum _ { j _ { 1 } = 1 } ^ { 2 } i f _ { j _ { 1 } } ( { } ^ { j _ { 1 } } K _ { 1 } ) e _ { i } } }  \\ { { ~ = ~ \displaystyle \left[ \begin{array} { l } { { 1 f _ { 1 } ( { } ^ { 1 } K _ { 1 } ) + { } ^ { 1 } f _ { 2 } ( { } ^ { 2 } K _ { 1 } ) } } \\ { { 2 f _ { 1 } ( { } ^ { 1 } K _ { 1 } ) + { } ^ { 2 } f _ { 2 } ( { } ^ { 2 } K _ { 1 } ) } } \end{array} \right] , } } \end{array}
$$

where

$$
^ i f _ { 1 } = \frac { \partial ( ^ { i } f ) } { \partial ( ^ { 1 } z ) } , ^ { i } f _ { 2 } = \frac { \partial ( ^ { i } f ) } { \partial ( ^ { 2 } z ) } , i = 1 , 2 .
$$

Replace $z$ with $y$ , and $K _ { 1 }$ with $f$ , (1.39) becomes

$$
f ^ { ( 1 ) } ( y ) ( f ( y ) ) = { \left[ \begin{array} { l } { ^ { 1 } f _ { 1 } ( ^ { 1 } f ) + ^ { 1 } f _ { 2 } ( ^ { 2 } f ) } \\ { ^ { 2 } f _ { 1 } ( ^ { 1 } f ) + ^ { 2 } f _ { 2 } ( ^ { 2 } f ) } \end{array} \right] } = y ^ { ( 2 ) } .
$$

(1.40) can be briefly denoted as

$$
y ^ { ( 2 ) } = f ^ { ( 1 ) } ( f ) .
$$

Case $M = 2$

$$
\begin{array} { l } { { \displaystyle f ^ { ( 2 ) } ( z ) ( K _ { 1 } , K _ { 2 } ) = \sum _ { i = 1 } ^ { 2 } \sum _ { j _ { 1 } = 1 } ^ { 2 } \sum _ { j _ { 2 } = 1 } ^ { 2 } i f _ { j _ { 1 } j _ { 2 } } ( { } ^ { j _ { 1 } } K _ { 1 } ) ( { } ^ { j _ { 2 } } K _ { 2 } ) e _ { i } } } \\ { { \displaystyle = \left[ \begin{array} { l } { { } ^ { 1 } f _ { 1 1 } ( { } ^ { 1 } K _ { 1 } ) ( { } ^ { 1 } K _ { 2 } ) + { } ^ { 1 } f _ { 1 2 } ( { } ^ { 1 } K _ { 1 } ) ( { } ^ { 2 } K _ { 2 } ) + { } ^ { 1 } f _ { 2 1 } ( { } ^ { 2 } K _ { 1 } ) ( { } ^ { 1 } K _ { 2 } ) + { } ^ { 1 } f _ { 2 2 } ( { } ^ { 2 } K _ { 1 } ) ( { } ^ { 2 } K _ { 2 } ) } \\ { { } ^ { 2 } f _ { 1 1 } ( { } ^ { 1 } K _ { 1 } ) ( { } ^ { 1 } K _ { 2 } ) + { } ^ { 2 } f _ { 1 2 } ( { } ^ { 1 } K _ { 1 } ) ( { } ^ { 2 } K _ { 2 } ) + { } ^ { 2 } f _ { 2 1 } ( { } ^ { 2 } K _ { 1 } ) ( { } ^ { 1 } K _ { 2 } ) + { } ^ { 2 } f _ { 2 2 } ( { } ^ { 2 } K _ { 1 } ) ( { } ^ { 2 } K _ { 2 } ) } \end{array} \right] . } } \end{array}
$$

Use $y$ to replace $z$ , and let $K _ { 1 } = K _ { 2 } = f$ , we obtain

$$
f ^ { ( 2 ) } ( y ) ( f ( y ) , f ( y ) ) = \left[ \begin{array} { l } { 1 f _ { 1 1 } ( 1 f ) ^ { 2 } + 2 ( ^ { 1 } f _ { 1 2 } ) ( ^ { 1 } f ) ( ^ { 2 } f ) + ^ { 1 } f _ { 2 2 } ( ^ { 2 } f ) ^ { 2 } } \\ { 2 f _ { 1 1 } ( ^ { 1 } f ) ^ { 2 } + 2 ( ^ { 2 } f _ { 1 2 } ) ( ^ { 1 } f ) ( ^ { 2 } f ) + ^ { 2 } f _ { 2 2 } ( ^ { 2 } f ) ^ { 2 } } \end{array} \right] ,
$$

which is only part of the right side of (1.36), but not all. The absent terms are

$$
\left[ { \begin{array} { c } { 1 f _ { 1 } \big ( ^ { 1 } f _ { 1 } \big ( ^ { 1 } f \big ) + ^ { 1 } f _ { 2 } \big ( ^ { 2 } f \big ) \big ) + ^ { 1 } f _ { 2 } \big ( ^ { 2 } f _ { 1 } \big ( ^ { 1 } f \big ) + ^ { 2 } f _ { 2 } \big ( ^ { 2 } f \big ) \big ) } \\ { 2 f _ { 1 } \big ( ^ { 1 } f _ { 1 } \big ( ^ { 1 } f \big ) + ^ { 1 } f _ { 2 } \big ( ^ { 2 } f \big ) \big ) + ^ { 2 } f _ { 2 } \big ( ^ { 2 } f _ { 1 } \big ( ^ { 1 } f \big ) + ^ { 2 } f _ { 2 } \big ( ^ { 2 } f \big ) \big ) } \end{array} } \right] .
$$

Now if we replace the operand $f ( y )$ with $f ^ { ( 1 ) } ( y ) ( f ( y ) )$ in (1.40), the result is exactly (1.43). Hence, shortening the notation as in (1.41), (1.36) can be written as

$$
y ^ { ( 3 ) } = f ^ { ( 2 ) } ( f , f ) + f ^ { ( 1 ) } ( f ^ { ( 1 ) } ( f ) ) .
$$

Thus we have seen that $y ^ { ( 2 ) }$ is a single Frecht derivative of order 1, and that $y ^ { ( 3 ) }$ is a linear combination of Frecht derivatives of order 1 and 2. In general, $y ^ { ( p ) }$ turns out to be a linear combination of Frecht derivatives of order up to $p - 1$ . The components in such linear combination are called elementary differentials.

Definition 1.14. The elementary differential $F _ { s } : \mathbf { R } ^ { m }  \mathbf { R } ^ { m }$ of $f$ , and their order are defined respectively by

$1 ^ { \circ }$ $f$ is only elementary differential of order 1, and $2 ^ { \circ }$ if $F _ { s } \left( s = 1 , 2 , \cdots , M \right)$ are elementary differential of order $r _ { s }$ , then the Frecht derivative

$$
F ^ { ( M ) } ( F _ { 1 } , F _ { 2 } , \cdots , F _ { M } ) ,
$$

is an elementary of order

$$
1 + \sum _ { s = 1 } ^ { M } r _ { s } .
$$

Remark 1.15. We have following:

$1 ^ { \circ }$ The elementary differential $F _ { 1 } , F _ { 2 } , \cdots , F _ { M }$ appearing as operands in (1.45) need not be distinct.

$2 ^ { \circ }$

$$
\{ F _ { 1 } , F _ { 2 } , \cdot \cdot \cdot , F _ { M } \} : f ^ { ( M ) } ( F _ { 1 } , F _ { 2 } , \cdot \cdot \cdot , F _ { M } ) .
$$

$3 ^ { \circ }$ The order of the elementary differential (1.47) is, by (1.46), the sum of the orders of the elementary differentials plus 1, i.e., $1 + \sum _ { s = 1 } ^ { M } r _ { s }$ , where 1 is “for the brackets”.

Order 1 has only one elementary differential, i.e., $f$

Order 2 has only one elementary differential, i.e., $f ^ { ( 1 ) } ( f ) = \{ f \}$

Order 3 has two elementary differentials, i.e.,

$M = 2 \Longrightarrow$ operand $f$ , $f \Longrightarrow$ elementary differential $\{ f ^ { 2 } \}$ , $M = 1 \Longrightarrow$ operand $f ^ { ( 1 ) } ( f ) = \{ f \} \Longrightarrow$ elementary differential $\{ \{ f \} \} = \{ _ { 2 } f \} _ { 2 }$ .

Order 4 has four elementary differentials, i.e.,

M = 3 =⇒ operand $f , f , f \implies$ elementary differential $\{ f ^ { 3 } \}$ , $M = 2 \implies$ operand $f , \{ f \} \implies$ elementary differential $\{ f \{ f \} _ { 2 } ( \equiv \{ _ { 2 } f \} f )$ , M = 1 = operand $\left\{ f ^ { 2 } \right\} \quad \Longrightarrow$ elementary differential $\{ { _ { 2 } f ^ { 2 } } \} _ { 2 }$ , operand $\{ _ { 2 } f \} _ { 2 } \implies$ elementary differential $\{ _ { 3 } f \} _ { 3 }$ .

# 2. Labeled graph

Let $n$ be a positive integer. A labeled $n$ -graph $g$ is a pair $\{ V , E \}$ formed by a set $V$ collection with card $( V ) = n$ , and a set $E$ of unordered pairs $( v , w )$ as a collection of elements, of which $v , w$ are point of the set $V$ , and $v \neq w$ . Therefore $g$ may be empty. $V$ and $E$ elements are known as the vertices and edges respectively. Two vertices $v , w$ is said to be the adjacent if $( v , w ) \in E$ . Fig. 1.1 shows labeled graph for $n = 2 , 3 , 4$ .

![](images/ac475a9a81a6df063454f1f8fe9d26ef2d682328904f519400510628df4e3382.jpg)  
Fig. 1.1. Labeled graph for $n = 2 , 3 , 4$

A graph can have many different types of label. However for the same graph, there exists a isomorphic mapping $\chi$ between two different labels. For an example, for one of the graphs in Fig. 1.1, depicted also in Fig. 1.2, we can take two types of label, as shown in Fig. 1.3.

![](images/c64200f6eeb9ee6412029d39b5e8f9e47415f9967c415386f48ad22f76eaac1e.jpg)

![](images/bd022a0fa90e4147fa39a01244ac85baa287891b2da506656fff708d5bb432cd.jpg)  
Fig. 1.2. Labeled of graph 4   
Fig. 1.3. 2 kind labeled of graph

We take mapping $\chi$ to be

$$
\chi : i \longrightarrow m , \quad j \longrightarrow n , \quad k \longrightarrow p , \quad l \longrightarrow q ,
$$

i.e.,

$$
\chi : V _ { 1 } \longrightarrow V _ { 2 } , V _ { 1 } = \{ i , j , k , l \} , V _ { 2 } = \{ m , n , p , q \} ,
$$

then

$$
\begin{array} { r l } { \chi : \quad } & { ( i , j ) \longrightarrow ( m , n ) , } \\ & { ( j , k ) \longrightarrow ( n , p ) , } \\ & { ( k , l ) \longrightarrow ( p , q ) , } \end{array}
$$

i.e.,

$$
\begin{array} { r l } { \chi : \quad } & { E _ { 1 } \longrightarrow E _ { 2 } , } \\ & { E _ { 1 } = \{ ( i , j ) , ( j , k ) , ( k , l ) \} , } \\ & { E _ { 2 } = \{ ( m , n ) , ( n , p ) , ( p , q ) \} . } \end{array}
$$

Therefore $\chi : L g _ { 1 } \to L g _ { 2 }$ , where $L g _ { 1 } = \{ V _ { 1 } , E _ { 1 } \}$ , $L g _ { 2 } = \{ V _ { 2 } , E _ { 2 } \}$ are two different labels in Fig. 1.3. In fact, if there exists a isomorphic mapping between two labels $g _ { 1 } , g _ { 2 }$ , they can be regarded as two types of labels for the same tree. Therefore a graph is an equivalent class, which consists of a variety of different labeled graphs corresponding to different types of label. These labeled graphs are equivalent, i.e., there exists an isomorphic mapping between them.

# 3. Relationship between rooted tree and elementary differential

Next we can see that there is a 1 to 1 correspondence between elementary and trees.

(1) Let $f$ be the unique elementary differential of order 1. Then $f$ corresponds to the unique tree of order 1, which consists of a single vertex.

(2) If the elementary differential $F _ { s }$ of order $r _ { s }$ $( s ~ = ~ 1 , 2 , \cdots , M )$ corresponds to trees $t _ { s }$ of order $r _ { s }$ $( s = 1 , 2 , \cdots , M )$ , then the elementary differential $\{ F _ { 1 } , F _ { 2 } , \cdots , F _ { M } \}$ of order $1 + \sum _ { 1 } ^ { M } r _ { s }$ corresponds to the tree of order $1 + \sum _ { s = 1 } ^ { M } r _ { s } ,$ obtained by grafting the $M$ trees $F _ { s }$ ( $\mathbf { \sigma } _ { s } = 1 , 2 , \cdots , M )$ onto a new root.

Example 1.16. If

$$
 \begin{array} { r l } & { { \boldsymbol { F } } _ { 1 } \sim { { t } _ { 1 } } ^ { \circ } \setminus { { \begin{array} { l } { P _ { , } } \\ { P _ { , } } \end{array} } } , { \boldsymbol { F } } _ { 2 } \sim { { t } _ { 2 } } = { \begin{array} { l } { P _ { , } } \\ { P _ { , } } \end{array} } , { \boldsymbol { F } } _ { 3 } \sim { { t } _ { 3 } } = { \begin{array} { l } { \ P _ { , } } \\ { { \begin{array} { l } { { \mathrm { t h e n } } } \\ { { \mathrm { ~ } } } \end{array} } } \\ { \{ \begin{array} { r l r l } { P _ { 1 } , F _ { 2 } , F _ { 3 } \} \sim { \small { \operatorname { \mathbb { V } } } \widehat { \left( { \begin{array} { l } { P _ { 2 } } \\ { \dots } \end{array} } \right) } } } \end{array} } } \end{array} } \end{array}
$$

We need a notation to represent trees similar to the notation for elementary differential. All trees can be labeled with combination of the symbol of $\tau$ for the unique tree of order 1 (consisting of a single node) and the symbol $[ \cdots ]$ , meaning we have grafted the trees appearing between the brackets onto a new root. We shall denote $n$ copies of tree t1 by t n1 , [[[···[ktimes by $[ \boldsymbol { \mathbf { \rho } } _ { k }$ , and $\operatorname * { l } _ { k \mathrm { t i m e s } }$ by $] _ { k }$ . For example

$$
t _ { 1 } = [ \tau ] = \mathscr { J } ,
$$

$$
\begin{array} { r c l } { { } } & { { } } & { { t _ { 2 } = [ \tau [ \tau ] ] ( \phantom { } - [ [ \tau ] \tau ] ) = [ \tau [ \tau ] _ { 2 } = \stackrel { \circ } { \sim } \phantom { } ] \ , } } \\ { { } } & { { } } & { { t _ { 3 } = [ t _ { 1 } , t _ { 2 } ^ { 2 } ] = [ [ \tau ] [ \tau [ \tau ] ] , [ \tau [ \tau ] ] ] \phantom { } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { = [ 2 \tau ] [ \tau [ \tau ] _ { 2 } [ \tau [ \tau ] _ { 3 } = \stackrel { \circ } { \sim } ] \ _ { \mathrm { { o } } } ^ { \mathrm { { q } } } \stackrel { \circ } { \sim } \phantom { \ } ] \ . } } \end{array}
$$

Definition 1.17. The order $r ( t )$ , symmetry $\sigma ( t )$ ◦and density (tree factorial) $\gamma ( t )$ are defined by

$$
\begin{array} { r l } & { r ( \tau ) = \sigma ( \tau ) = \gamma ( \tau ) = 1 , \quad \mathrm { a n d } } \\ & { r \big ( [ t _ { 1 } ^ { n _ { 1 } } t _ { 2 } ^ { n _ { 2 } } \cdot \cdot \cdot ] \big ) = 1 + n _ { 1 } r ( t _ { 1 } ) + n _ { 2 } r ( t _ { 2 } ) + \cdot \cdot \cdot , \quad \mathrm { ( n u m b e r ~ o f ~ v e r t i c e s ) } } \\ & { \sigma \big ( [ t _ { 1 } ^ { n _ { 1 } } t _ { 2 } ^ { n _ { 2 } } \cdot \cdot \cdot ] \big ) = n _ { 1 } ! n _ { 2 } ! \cdot \cdot \cdot \big ( \sigma ( t _ { 1 } ) \big ) ^ { n _ { 1 } } \left( \sigma ( t _ { 2 } ) \right) ^ { n _ { 2 } } \cdot \cdot \cdot , } \\ & { \gamma \big ( [ t _ { 1 } ^ { n _ { 1 } } t _ { 2 } ^ { n _ { 2 } } \cdot \cdot \cdot ] \big ) = r \big ( [ t _ { 1 } ^ { n _ { 1 } } t _ { 2 } ^ { n _ { 2 } } \cdot \cdot \cdot ] \big ) \left( \gamma ( t _ { 1 } ) \right) ^ { n _ { 1 } } \left( \gamma ( t _ { 2 } ) \right) ^ { n _ { 2 } } \cdot \cdot \cdot . } \end{array}
$$

Let $\alpha ( t )$ (tree multiplicity) be the number of essentially different ways of labeling the vertices of the tree $t$ with the integers $1 , 2 , \cdots , r ( t )$ such that labels are monotone increase. Essentially different labeling is illustrated in the following examples:

$$
\mathbf { p l e 1 . 1 8 . } \ t _ { 1 } = [ \tau ^ { 3 } ] = \big \{ \tau ^ { 3 } , \rho , \mathrm { i t s \ l a b e l i n g \ t r e e s \ a r e } ^ { 2 } \big \} \overset { 3 } { \underset { 1 } { \sim } } \big \{ \tau ^ { 4 } \big \} ^ { 2 } \big \& { \mathrm { a n d } } ^ { 4 } \big \mathrm { \Large ~ \left. \sum _ { \ell } ^ { 2 } \right. ^ { 3 } , }
$$

are not regarded as essentially different labelings, hence $\alpha ( t _ { 1 } ) = 1$ .

Q 4 4 Example 1.19. $t _ { 2 } = [ \tau [ \tau ] ] = \stackrel { \circ } { \sim } \stackrel { \circ }$ , its labeling trees are ◦ 2 ◦ 3 , ◦ 3 2 3 ◦ 4 ◦ 2 and are regarded as essentially different labelings, and $\alpha ( t _ { 2 } ) = 3$ .

From above, we have a easy way of computing $\alpha ( t )$ , namely

$$
\alpha ( t ) = \frac { r ( t ) ! } { \sigma ( t ) \gamma ( t ) } .
$$

# 4. Order conditions for multi-stage R–K method

Definition 1.20. The function $F$ is defined on the set $T$ of all trees by

$$
\begin{array} { c } { F ( \tau ) = f , } \\ { \begin{array} { c } { F ( t _ { 1 } , t _ { 2 } , \cdot \cdot \cdot , t _ { M } ] ) = \{ F ( t _ { 1 } ) , F ( t _ { 2 } ) , \cdot \cdot \cdot , F ( t _ { M } ) \} . } \end{array} } \end{array}
$$

The proof of the following two theorems was established by Butcher in 1987 [But87] .

Theorem 1.21. Let $\dot { y } = f ( y ) , f : \mathbf { R } ^ { m }  \mathbf { R } ^ { m }$ , then

$$
y ^ { ( q ) } = \sum _ { r ( t ) = q } \alpha ( t ) F ( t ) ,
$$

where $F ( t )$ is defined by (1.49), and $\alpha ( t )$ by (1.48).

Below let us apply this theorem for $p \leq 4$ to obtain $y ^ { ( q ) }$

$$
\begin{array} { l } { { y ^ { ( 2 ) } = \{ f \} , } } \\ { { y ^ { ( 3 ) } = \{ f ^ { 2 } \} + \{ { 2 f } \} _ { 2 } , } } \\ { { y ^ { ( 4 ) } = \{ f ^ { 3 } \} + 3 \{ f \{ f \} _ { 2 } + \{ _ { 2 } f ^ { 2 } \} _ { 2 } + \{ _ { 3 } f \} _ { 3 } . } }  \end{array}
$$

Let us define the right side of Equation (1.4) to be $y _ { n } ( h )$ , which is then expanded as a Taylor series about $h = 0$ ,

$$
y ( x _ { n + 1 } ) = y ( x _ { n } ) + h y ^ { ( 1 ) } ( x _ { n } ) + { \frac { 1 } { 2 } } h ^ { 2 } y ^ { ( 2 ) } ( x _ { n } ) + \cdots ,
$$

where

$$
\left. { \frac { \mathrm { d } ^ { q } } { \mathrm { d } h ^ { q } } } y _ { n } ( h ) \right| _ { h = 0 } = \sum _ { r ( t ) = q } \alpha ( t ) \gamma ( t ) \phi ( t ) F ( t ) .
$$

We first slightly modify the notation in Butcher array of $a$ . Let $a _ { s + 1 , i } ~ = ~ b _ { i }$ $( i =$ $1 , 2 , \cdots , s )$ , we get the following Table 1.2.

Definition 1.22. $1 ^ { \circ }$ For $i = 1 , 2 , \cdots , s , s + 1$ , define the function of $\phi _ { i }$ on the set $T$ of all trees by:

$$
\begin{array} { l } { \displaystyle \phi _ { i } ( \tau ) = \sum _ { j = 1 } ^ { s } a _ { i j } , } \\ { \displaystyle \phi _ { i } \big ( [ t _ { 1 } , t _ { 2 } , \cdot \cdot \cdot , t _ { M } ] \big ) = \sum _ { j = 1 } ^ { s } a _ { i j } \phi _ { j } \big ( t _ { 1 } \big ) \phi _ { j } \big ( t _ { 2 } \big ) \cdot \cdot \cdot \phi _ { j } \big ( t _ { M } \big ) . } \end{array}
$$

$2 ^ { \circ }$ define ${ { \phi } } ( t ) = { { \phi } _ { s + 1 } } ( t )$ .

Table 1.2. Tree and elementary differential up to 4   

<table><tr><td rowspan=1 colspan=1>tree</td><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>F(t)               r(t)σ(t)γ(t)α(t)i(t),i=1,.·,s</td><td rowspan=1 colspan=4>r(t)σ(t)γ(t)α(t)i(t),i=1,.·,s</td><td rowspan=1 colspan=1>（(t)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>f               1111</td><td rowspan=1 colspan=4>∑aij(=ci)j</td><td rowspan=1 colspan=1>Mbii</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>{f}=f&#x27;f           2121L</td><td rowspan=1 colspan=4>MaijCjL</td><td rowspan=1 colspan=1>Mbicii</td></tr><tr><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>[72][[]]</td><td rowspan=1 colspan=1>{f²}=f&quot;(f,f)    3231∑aijc²{2f}2= f&#x27;f&#x27;f      3161∑au∑</td><td rowspan=1 colspan=4>j3161∑au∑ajkCkj     k</td><td rowspan=1 colspan=1>£CbiciMbiaijCjij</td></tr><tr><td rowspan=4 colspan=1>99P。0</td><td rowspan=4 colspan=1>[73]</td><td rowspan=4 colspan=1>{f³}=f&quot;(f,f,f） 4 6 4 1[t[r]]{f{f}2=f&quot;(f,f&#x27;f)4 1 8 3∑[t²]{2f²}2=f&#x27;f&quot;（f,f）4 2 121∑ai∑[[]]{3f}3=f&#x27;f&#x27;f&#x27;f</td><td rowspan=1 colspan=1>M</td><td rowspan=2 colspan=3>aijc</td><td rowspan=4 colspan=1>£biciMbiCiaijCjij∑biaijc²ijjk</td></tr><tr><td rowspan=1 colspan=1>j</td></tr><tr><td rowspan=1 colspan=1>></td><td rowspan=1 colspan=2>aijCjMajkCk</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M</td></tr><tr><td rowspan=1 colspan=4>aijCjMajkCkj       kCajkej     k4 1 24 1∑aij∑ajk∑aknCn∑biaijajκCkj     k     n</td></tr></table>

Remark 1.23. Functions $\phi _ { i }$ has representations on the set $T$

$$
\begin{array} { l l } { \displaystyle \phi _ { i } ( \tau ) = \sum _ { j } a _ { i j } = c _ { i } , } & { \forall i = 1 , 2 , \cdots , s , } \\ { \displaystyle \phi ( \tau ) = \sum _ { j } a _ { s + 1 , j } = \sum _ { j } b _ { j } = \sum _ { i } b _ { i } , } & { } \\ { \displaystyle \phi _ { i } ( [ \tau ] ) = \sum _ { j } a _ { i j } \phi _ { j } ( \tau ) = \sum _ { j } a _ { i j } c _ { j } , } & { \forall i = 1 , 2 , \cdots , s , } \\ { \displaystyle \phi ( [ \tau ] ) = \sum _ { j } a _ { s + 1 , q } c _ { j } = \sum _ { j } b _ { j } c _ { j } = \sum _ { i } b _ { i } c _ { i } , } & { } \\ { \displaystyle \phi _ { i } ( [ [ \tau ] ) ) = \sum _ { j } a _ { j } \phi _ { i } ( [ \tau ] ) = \sum _ { j } a _ { j } \sum _ { k } a _ { j } c _ { k } , } & { \forall i = 1 , 2 , \cdots , s , } \\ { \displaystyle \phi ( [ [ \tau ] ) ) = \sum _ { j } a _ { s + 1 , j } \sum _ { k } a _ { j k } c _ { k } = \sum _ { j k } b _ { i } a _ { k } c _ { k } , } & { \forall i = 1 , 2 , \cdots , s , } \\ { \displaystyle \phi ( [ [ \tau ] ) ) = \sum _ { j } a _ { s + 1 , j } \sum _ { k } a _ { j k } c _ { k } = \sum _ { j k } b _ { i } a _ { j k } c _ { k } = \sum _ { i j } b _ { i } a _ { i j } c _ { j } . } & { } \end{array}
$$

Theorem 1.24. R–K method has order $p _ { i }$ , if

$$
\phi ( t ) = \sum _ { i } b _ { i } \phi _ { i } = \frac { 1 } { \gamma ( t ) } , \quad \forall r ( t ) \leq p , \quad t \in T ,
$$

and does not hold for some tree of order $p + 1$

From Table 1.3, we then obtain the following number of orders trees (see Table 1.4).

Table 1.3. Number of trees up to order 10   

<table><tr><td rowspan=1 colspan=1>order p</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1> number of trees Tp</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>48</td><td rowspan=1 colspan=1>115</td><td rowspan=1 colspan=1>286</td><td rowspan=1 colspan=1>719</td></tr></table>

Table 1.4. Number of conditions up to order 10   

<table><tr><td rowspan=1 colspan=1>order p</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>number of conditions</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>486</td><td rowspan=1 colspan=1>1205</td></tr></table>

Number of order conditions for Multi-stage $\mathbf { R - K }$ up to order 10, can be seen in the following Table 1.4.

# 7.1.5 Simplified Conditions for Symplectic R–K Method

There are four types of trees, which can be defined as follows[SA91] :

(1) A labeled $n$ -tree $\lambda \tau$ is a labeled $n$ -graph $\{ V , E \}$ , such that for any pair of distinct vertices $v$ and $w$ , there exists a unique path that joins $v$ and $w$ .

(2) Two labeled $n$ -trees $\{ V _ { 1 } , E _ { 1 } \}$ , $\{ V _ { 2 } , E _ { 2 } \}$ are said to be isomorphic, if a bijection of $V _ { 1 }$ onto $V _ { 2 }$ exists that transforms edges in $E _ { 1 }$ into edges in $E _ { 2 }$ , vertices $V _ { 1 }$ into $V _ { 2 }$ . $n$ -trees $\tau$ is an equivalence class that consists of labeled $n$ -trees isomorphic to it. Each of the labeled $n$ -trees that represent $\tau$ is called a labeling of $\tau$ .

(3) A rooted labeled $n$ -tree $\rho \lambda \tau$ is a labeled $n$ -tree, in which one of the vertices $r$ , called the root, has been highlighted. The vertices adjacent to the root are called the sons of the root. The sons of the remaining vertices are defined in an obvious recursive way. In fact, when some point is defined as root, the tree becomes a directed graph, i.e., any edge $( v , w )$ in set $E$ has a direction to represent the relationship between father and son. Let $T$ be a mapping from son to father. Since any point $v$ has a path to the root, e.g. $v = v _ { 0 } , v _ { 1 } , \cdots , v _ { m } = r ,$ $r$ may be obtained through the sequential action of $T$ on $v$ . Therefore a direction can be defined from $v$ to $r$ , and the entire root also become oriented.

(4) Two labeled $n$ -trees $\{ V _ { 1 } , E _ { 1 } , r _ { 1 } \}$ , $\{ V _ { 2 } , E _ { 2 } , r _ { 2 } \}$ are said to be root isomorphic, if a bijection of $V _ { 1 }$ onto $V _ { 2 }$ exists that transforms edges in $E _ { 1 }$ onto $E _ { 2 }$ and maps $r _ { 1 }$ onto $r _ { 2 }$ . A rooted $n$ -trees $\rho \tau$ is an equivalence class that comprises of a the rooted labeled $n$ -tree and all rooted labeled $n$ -trees root-isomorphic to it. Fig. 1.4 is an example of rooted tree.

Fig. 1.5 shows that there is only one unlabeled 3-tree for $n = 3$ , $\tau _ { 3 1 }$ , which represents three different labeled trees denoted by $( A , B , C )$ . Each labeled tree represents three rooted labeled trees denoted by lower case letter $( a , b , \cdot \cdot \cdot )$ . The 9 rooted labeled trees can be classified into two rooted trees $\rho \tau _ { 3 1 }$ , $\rho \tau _ { 3 2 }$ . The tree $\tau _ { 3 1 }$ at the last row can be considered as the result of the identification of $\rho \tau _ { 3 1 }$ with $\rho \tau _ { 3 2 }$ . In general, trees can be considered to be equivalent classes of rooted trees, because a root isomorphism is an isomorphism. For each rooted tree $\rho \tau$ , we denote $\alpha ( \rho \tau )$ as the number of the monotonic rooted labeled trees. The latter only allow so called monotonic rooted labelings where each vertex is labeled using an integer number $( \leq n )$ smaller than all its sons.

![](images/70a74b2a795d43de6dc297d1bf7ee4ded1db64ea0f3526b6c3fa5cfb23dce0c1.jpg)  
Fig. 1.4. A rooted tree

Unless otherwise specified, it is assumed that the set of vertices of a labeled $n$ graph is always $\{ 1 , 2 , \cdots , n \}$ . In order to clarify the above four types of trees, we use Fig. 1.5 to illustrate.

![](images/7fe05a0bb1ce00c6cfa116709126ea0425349e8b92351e626e18e28b58dc6a59.jpg)  
Fig. 1.5. The 3-tree, labeled 3-trees $( A ) - ( C )$ , rooted labeled 3-tree $( a ) - ( i )$ , and rooted 3-tree

![](images/a01693258485fb6b374b4b768a27d3d3dc4aa5851d9c6ef0713d31dbc8c62035.jpg)  
Fig. 1.6. Rooted $n$ -tree $( n { = } 1 , 2 )$

![](images/8caa0bad06e68779049093ec7aee98f829fcdc7e027d458d57ae2be4f1b22eb5.jpg)  
Fig. 1.7. Rooted $n$ -tree $( n { = } 3 , 4 )$

![](images/11706dd9f24db8dd382220dcd33fe437faec84ef73b02f50cfc02e7f2c9caf87.jpg)  
Fig. 1.8. 4 rooted tree in Lemma 1.25

Superfluous trees. Let $\tau$ be an $n$ -tree and choose one of its labelings $\lambda \tau$ . This labeling gives rise to $n$ different rooted labeled trees $\rho \lambda \tau _ { 1 } , \cdots , \rho \lambda \tau _ { n }$ , where $\rho \lambda \tau _ { i }$ has its root at the integer $i$ $( 1 \leq i \leq n )$ . If for each edge $( i , j )$ in $\lambda \tau$ , $\rho \tau _ { i }$ and $\rho \tau _ { j }$ represent different rooted trees; then $\tau$ is called non-superfluous. Consider the 3-tree $\tau _ { 3 1 }$ in

Fig.1.5. When choosing the labeled 3-tree $A$ , we see that for the edge 1-2, choosing 1 as the root leads to $\rho \tau _ { 3 1 }$ , and choosing 2 as the root leads to $\rho \tau _ { 3 2 }$ . For the edge 2-3, choosing 2 as the root leads to $\rho \tau _ { 3 2 }$ , and choosing 2 as the root leads to $\rho \tau _ { 3 1 }$ . Therefore $\tau _ { 3 1 }$ is non-superfluous. One the other hand the 4-tree with labeling is superfluous (see Fig. 1.6 and 1.7), since changing the root from 2 to the adjacent 3 does not result in

• • • •1 2 3 4

In order to simplify the order conditions for symplectic R–K,we need some lemmas. Before introducing the lemmas, let us first look at Fig. 1.8: 4-rooted tree.

Look at first rooted tree $\rho \tau _ { i }$ (i.e., root at $i$ ) and rooted tree $\rho \tau _ { j }$ . The root of the rooted trees $\rho \tau _ { I } , \rho \tau _ { J }$ in Fig. 1.8 is at vertex $i$ and $j$ , they are removed edge joining $i$ and $j$ in the top left-hand corner graph.

Lemma 1.25. With the above notations

$1 ^ { \circ }$

$$
\frac { 1 } { \gamma ( \rho \tau _ { i } ) } + \frac { 1 } { \gamma ( \rho \tau _ { j } ) } = \frac { 1 } { \gamma ( \rho \tau _ { I } ) } \cdot \frac { 1 } { \gamma ( \rho \tau _ { J } ) } .
$$

$2 ^ { \circ }$ For the symplectic $R – K$ method, weighted coefficients of elementary differential satisfy

$$
\phi ( \rho \tau _ { i } ) + \phi ( \rho \tau _ { j } ) = \phi ( \rho \tau _ { I } ) \phi ( \rho \tau _ { J } ) .
$$

$3 ^ { \circ }$ For order $\geq ( r - 1 )$ , symplectic R–K method,

$$
\phi ( \rho \tau _ { i } ) + \phi ( \rho \tau _ { j } ) = \frac { 1 } { \gamma ( \rho \tau _ { i } ) } + \frac { 1 } { \gamma ( \rho \tau _ { j } ) } .
$$

Therefore $\rho \tau _ { i }$ order conditions hold iff order conditions of $\rho \tau _ { j }$ hold.

Proof. By the definition of $\gamma$ , we have

$$
\begin{array} { l } { { \gamma ( \rho \tau _ { i } ) = r \gamma ( \rho \tau _ { J } ) \displaystyle \frac { \gamma ( \rho \tau _ { I } ) } { r ( \rho \tau _ { I } ) } , } } \\ { { \gamma ( \rho \tau _ { j } ) = r \gamma ( \rho \tau _ { I } ) \displaystyle \frac { \gamma ( \rho \tau _ { J } ) } { r ( \rho \tau _ { J } ) } , } } \end{array}
$$

where $r ( \rho \tau _ { I } )$ and $r ( \rho \tau _ { J } )$ are the orders of $\rho \tau _ { I }$ and $\rho \tau _ { J }$ . Then, insert $r ( \rho \tau _ { I } )$ in formula (1.57) and $r ( \rho \tau _ { J } )$ in formula (1.58) into $r ( \rho \tau _ { I } ) \substack { + r ( \rho \tau _ { J } ) = r }$ to obtain (1.54). Rewrite the left side of formula (1.55) into

$$
\phi ( \rho \tau _ { i } ) + \phi ( \rho \tau _ { j } ) = \sum _ { i j \cdots } b _ { i } a _ { i j } \prod + \sum _ { i j \cdots } b _ { j } a _ { i j } \prod ,
$$

where $\prod$ represents a product of $r - 2$ factors $a _ { k l }$ . Equality (1.55) can be obtained using order condition (1.15) of the symplectic R–K method. -

Example 1.26. See the simple examples below. From Fig. 1.8 we have

$$
\begin{array} { l } { { \phi ( \rho \tau ^ { v } ) = \displaystyle \sum _ { v w 1 \cdots 4 } b _ { i _ { v } } a _ { i _ { v } i _ { w } } a _ { i _ { v } i _ { 1 } } a _ { i _ { v } i _ { 2 } } a _ { i _ { w } i _ { 3 } } a _ { i _ { w } i _ { 4 } } , } } \\ { { \phi ( \rho \tau ^ { w } ) = \displaystyle \sum _ { v w 1 \cdots 4 } b _ { i _ { w } } a _ { i _ { w } i _ { v } } a _ { i _ { w } i _ { 3 } } a _ { i _ { w } i _ { 4 } } a _ { i _ { v } i _ { 1 } } a _ { i _ { v } i _ { 2 } } . } } \end{array}
$$

From Fig.1.8 we have

$$
\phi ( \rho \tau _ { v } ) = \sum _ { v 1 2 } b _ { i v } a _ { i _ { v } i _ { 1 } } a _ { i _ { v } i _ { 2 } } ,
$$

$$
\phi ( \rho \tau _ { w } ) = \sum _ { w 3 4 } b _ { i _ { w } } a _ { i _ { w } i _ { 3 } } a _ { i _ { 3 } i _ { 4 } } .
$$

![](images/2ddfff7884675461ec071133b47358227dc0868f3d96cbc38b535cdd0b20f6e7.jpg)

Theorem 1.27. [SA91] Assume that a symplectic $R – K$ method satisfies the order conditions for order $\geq ( r - 1 )$ with ( $\dot { r } \geq 2 \dot { }$ ). Then, to ensure that the method to have order $\geq r$ , it is sufficient that, for each non-superfluous tree $\tau$ with $r$ vertices, there is one rooted tree ρτ associated with $\tau$ for which

$$
\phi ( \rho \tau ) = { \frac { 1 } { \gamma ( \rho \tau ) } } .
$$

Proof. Choose first a non-superfluous tree $\tau$ . Assume that condition (1.60) is satisfied for a suitable rooted tree $\rho \tau _ { i }$ of $\tau$ . From the Lemma 1.25 we choose $j$ as any of the vertices adjacent to $i$ . By condition (1.56), the order condition (1.60) is also satisfied for $\rho \tau _ { j }$ . Since any two vertices of a tree can be joined through a chain of pairwise adjacent vertices, the iteration of this argument leads to the conclusion that the method satisfies the order conditions that arise from any rooted tree in $\tau$ . In the case of a superfluous tree $\tau$ , by definition, it is possible to choose adjacent vertices $i , j$ , such that $\rho \tau _ { i }$ and $\rho \tau _ { j }$ are in fact the same rooted tree. Then condition (1.56) shows that (1.60) holds for the rooted tree $\rho \tau _ { i }$ . Therefore (1.60) holds for all rooted tree in $\tau$ . $\blacktriangle$

Example 1.28. For $r = 2$ , there is only one tree $\tau _ { 2 1 }$ , this is a superfluous tree.

Example 1.29. For $r \ : = \ : 3$ , there is again only one tree $\tau _ { 3 1 }$ . It has two rooted trees $\rho \tau _ { 3 1 }$ , $\rho \tau _ { 3 2 }$ . Hence the order conditions become

$$
\sum _ { i , j , k = 1 } ^ { 3 } b _ { i } a _ { i j } a _ { i k } = \frac { 1 } { 3 } , \quad \mathrm { o r } \quad \sum _ { i , j , k = 1 } ^ { 3 } b _ { i } a _ { i j } a _ { j k } = \frac { 1 } { 6 } .
$$

Example 1.30. For $r \ = \ 4$ , there is only one non-superfluous tree $\tau _ { 4 2 }$ . We impose either the order conditions for $\rho \tau _ { 4 3 }$ or the order conditions for $\rho \tau _ { 4 4 }$ .

We see that for symplectic $\mathbf { R - K }$ methods it is sufficient to obtain the order conditions only for non-superfluous trees rather than every rooted trees. The reduction in the number of order conditions is given in Table 1.5. Comparison order conditions between symplectic R–K (R–K–N) method.

Table 1.5. Order conditions between symplectic R–K (R–K–N) method   

<table><tr><td>Order</td><td>R-K method</td><td>symp.R-K method</td><td>R-K-Nmethod</td><td>symp.R-K-Nmethod</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td></tr><tr><td>3</td><td>4</td><td>2</td><td>4</td><td>4</td></tr><tr><td>4</td><td>8</td><td>3</td><td>7</td><td>6</td></tr><tr><td>5</td><td>17</td><td>6</td><td>13</td><td>10</td></tr><tr><td>6</td><td>37</td><td>10</td><td>23</td><td>15</td></tr><tr><td>7</td><td>85</td><td>21</td><td>43</td><td>25</td></tr><tr><td>8</td><td>200</td><td>40</td><td>79</td><td>39</td></tr></table>

Example 1.31. For diagonally symplectic $\mathbf { R - K }$ method, see tableau (1.16).

If $r = 3$ , according to Theorem 1.27 and Table 1.5, symplectic $\mathbf { R - K }$ method has only two conditions. One condition is for $r = 1$ ,

$$
b _ { 1 } + b _ { 2 } + b _ { 3 } = 1 .
$$

another condition is for $r \ = \ 3$ , which has only one non-superfluous tree with two rooted trees, $\rho \tau _ { 3 1 } , \rho \tau _ { 3 2 }$ . Choose one of them

$$
r ( \rho \tau _ { 3 1 } ) \phi ( \rho \tau _ { 3 1 } ) = 1 , \quad \sum _ { i = 1 } ^ { 3 } b _ { i } c _ { i } ^ { 2 } = \frac { 1 } { 3 } ,
$$

After simplifying, we obtain

$$
b _ { 1 } ^ { 3 } + b _ { 2 } ^ { 3 } + b _ { 3 } ^ { 3 } = 0 .
$$

Since we have two equations with three unknowns, one of which can be freely chosen, for example:

$$
b _ { 1 } = b _ { 3 } = { \frac { 1 } { 2 - { \sqrt [ { 3 } ] { 3 } } } } , \quad b _ { 2 } = { \frac { - { \sqrt [ { 3 } ] { 2 } } } { 2 - { \sqrt [ { 3 } ] { 3 } } } } \quad \sec { ( 1 . 2 0 ) } .
$$

# 7.2 Symplectic P–R–K Method

In this section we study symplectic Partitioned–Runge–Kutta method(P–R–K method).

# 7.2.1 P–R–K Method

In this subsection we focus on a class of special Hamiltonian system i.e., separable systems:

$$
H ( p , q ) = u ( p ) + v ( q ) .
$$

Its corresponding Hamiltonian equations are

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \mathrm { d } p } { \mathrm { d } t } = - v _ { q } ( q ) = f ( q ) , } \\ { \displaystyle \frac { \mathrm { d } q } { \mathrm { d } t } = u _ { p } ( p ) = g ( p ) . } \end{array} \right.
$$

Let us suppose that the component $p$ of the first set of system (2.2) are integrated by an $\mathbf { R - K }$ method and the component $q$ in second part of system are integrated with a different $\mathbf { R - K }$ method. The overall scheme is called a Partitioned– Runge–Kutta method, or shortly called P–R–K method. It can be specified by two Butcher tableaux:

$$
{ \begin{array} { c } { c _ { 1 } { | \begin{array} { l l l l l l l l l } { a _ { 1 1 } } & { \cdots } & { a _ { 1 s } } & & & & & { C _ { 1 } { | \begin{array} { l l l l l l l } { A _ { 1 1 } } & { \cdots } & { A _ { 1 s } } & & \\ { \vdots } & { \ddots } & { \vdots } & & & & { \vdots } \\ { a _ { s 1 } } & { \cdots } & { a _ { s s } } & & & & & { C _ { s } { | \begin{array} { l l l l l l l } { \vdots } & { \ddots } & { } & { \vdots } & \\ { B _ { 1 } } & { \cdots } & { A _ { s s } } & { } & { } \end{array} | } } \\ { b _ { 1 } } & { \cdots } & { b _ { s } } & & & & { } & & { B _ { 1 } \quad \cdots } & { B _ { s } } \end{array} } } \end{array} | } } } \\ { { \frac { c _ { s } { | \begin{array} { l l l l l l l l l l } { a _ { 1 } } & { \cdots } & { \cdots } & { a _ { s s } } & { } & & & { C _ { s } { | \begin{array} { l l l l l l l l } { A _ { 3 1 } } & { \cdots } & { A _ { s s } } & { } \\ { b _ { 1 } } & { \cdots } & { \cdots } & { b _ { s } } & { } \end{array} | } } } } { b _ { 1 } } } } \end{array}  { \mathrm { ~ } }  \frac { ; } { \begin{array} { l l l l l l l l } { a _ { 1 } } & { \cdots } & { a _ { 1 s } } & { } & & & { C _ { 1 } { | \begin{array} { l l l l l l l } { a _ { 2 } } & { \cdots } & { a _ { 1 s } } & { } \\ { \vdots } & { \vdots } & { \ddots } & { } & { \vdots } \\ { a _ { s } } & { \cdots } & { a _ { s s } } & { } & { } & & { C _ { s } { | \begin{array} { l l l l l l } { a _ { 2 } } & { \cdots } & { a _ { 1 s } } & { } \\ { b _ { 1 } } & { \cdots } & { b _ { s } } & { } \end{array} | } } } \end{array} } } \end{array} \end{array}
$$

The application of (2.3) to the system (2.2) results in

$$
\left\{ \begin{array} { l l } { \displaystyle P _ { i } = p ^ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Q _ { j } ) , } \\ { \displaystyle Q _ { i } = q ^ { n } + h \sum _ { j = 1 } ^ { s } A _ { i j } g ( P _ { j } ) , } \\ { \displaystyle p ^ { n + 1 } = p ^ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Q _ { i } ) , } \\ { \displaystyle q ^ { n + 1 } = q ^ { n } + h \sum _ { i = 1 } ^ { s } B _ { i } g ( P _ { i } ) . } \end{array} \right. \quad i = 1 , \cdots , s ,
$$

These tableaux are coefficients of P–R–K method.

Theorem 2.1. If coefficients of P–R– $K$ (2.4) satisfies the following conditions:

$$
M = b _ { i } A _ { i j } + B _ { j } a _ { j i } - b _ { i } B _ { j } = 0 , \quad i , j = 1 , \cdot \cdot \cdot , s
$$

then this P–R–K method is symplectic[AS93,Sur90,Sun93b,SSM92] .

Proof. Let

$$
K _ { i } = f ( Q _ { i } ) , \quad l _ { i } = g ( P _ { i } ) ,
$$

and

$$
\begin{array} { c } { { d p ^ { n + 1 } \wedge { \bf d } q ^ { n + 1 } - { \bf d } p ^ { n } \wedge { \bf d } q ^ { n } } } \\ { { = } } \\ { { { \displaystyle h \sum _ { i = 1 } ^ { s } \left( b _ { i } { \bf d } K _ { i } \wedge { \bf d } Q _ { i } + B _ { i } { \bf d } P _ { i } \wedge { \bf d } l _ { i } \right) } } } \\ { { { } } } \\ { { { \displaystyle ~ - h ^ { 2 } \sum _ { i , j = 1 } ^ { s } \left( b _ { i } A _ { i j } + B _ { j } a _ { j i } - b _ { i } B _ { j } \right) { \bf d } K _ { i } \wedge { \bf d } l _ { j } . } } } \end{array}
$$

Note that the first term on the right side of Equation (2.7) is

$$
\begin{array} { l } { b _ { i } \mathbf { d } K _ { i } \wedge \mathbf { d } Q _ { i } + B _ { i } \mathbf { d } P _ { i } \wedge \mathbf { d } l _ { i } } \\ { = \displaystyle \sum _ { i , j = 1 } ^ { s } - v _ { q q } \mathbf { d } Q _ { i } \wedge \mathbf { d } Q _ { j } + u _ { p p } \mathbf { d } P _ { i } \wedge \mathbf { d } P _ { j } = 0 . } \end{array}
$$

In order to satisfy the equality (2.5), it is sufficient to make

$$
b _ { i } A _ { i j } + B _ { j } a _ { j i } - b _ { i } B _ { j } = 0 .
$$

Therefore, the theorem is completed.

$W$ -transformation (defined below) proposed by Hairer and Wanner in 1981 has the intention of simplifying the order condition $C ( \cdot )$ and $D ( \cdot )$ , as well as their relationship. Through the $W$ - transformation, it is easy to construct higher order $\mathbf { R - K }$ method $[ \bar { \mathrm { H w } } 8 1 ]$ . Let us suppose polynomials $p _ { i }$ $0 \leq i \leq ( s - 1 ) )$ , are orthogonal to the following inner product

$$
( p , q ) = \sum _ { i = 1 } ^ { s } b _ { i } p ( c _ { i } ) q ( c _ { i } ) ,
$$

introducing matrix

$$
W = \left[ \begin{array} { c c c c } { { p _ { 0 } ( c _ { 1 } ) } } & { { p _ { 1 } ( c _ { 1 } ) } } & { { \cdots } } & { { p _ { s - 1 } ( c _ { 1 } ) } } \\ { { p _ { 0 } ( c _ { 2 } ) } } & { { p _ { 1 } ( c _ { 2 } ) } } & { { \cdots } } & { { p _ { s - 1 } ( c _ { 2 } ) } } \\ { { \cdots } } & { { \cdots } } & { { \cdots } } & { { \cdots } } \\ { { p _ { 0 } ( c _ { s } ) } } & { { p _ { 1 } ( c _ { s } ) } } & { { \cdots } } & { { p _ { s - 1 } ( c _ { s } ) } } \end{array} \right] ,
$$

by the orthogonality of $p _ { i } ( i = 1 , \cdots , s - 1 )$ , we have

$$
W ^ { \mathrm { T } } B W = I .
$$

We take $p _ { k } ( x )$ as a standard shifted Legendre polynomial, defined by

$$
p _ { k } ( x ) = \sqrt { 2 k + 1 } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { k + i } \Big ( \begin{array} { c } { { k } } \\ { { i } } \end{array} \Big ) \Big ( \begin{array} { c } { { k + i } } \\ { { i } } \end{array} \Big ) x ^ { i } , \quad k = 0 , 1 , \cdots , s - 1 .
$$

For an $s$ -stage $\mathbf { R - K }$ method $( A , b , c )$ , let $X = W ^ { - 1 } A W = W ^ { \mathrm { T } } B A W$ , then for the high order $\mathbf { R - K }$ method based on the high order quadrature formula their transformation matrix X is given by Table 2.1[Sun93a,Sun94,Sun95] .

Table 2.1. Matrix $X$ form   

<table><tr><td>method</td><td>Xs,s-1</td><td>Xs-1,s</td><td>Xs,s</td><td>symplectic</td></tr><tr><td>Gauss</td><td>s-1</td><td>-s-1</td><td>0</td><td>yes</td></tr><tr><td>Lobatto III A</td><td>ss-1u</td><td>0</td><td>0</td><td>no</td></tr><tr><td>Lobatto III B</td><td>0</td><td>-ss-1u</td><td>0 u²</td><td>no</td></tr><tr><td>Lobatto III C</td><td>ss-1u</td><td>-s-1u</td><td>2(2s -1)</td><td>no</td></tr><tr><td>Lobatto III S</td><td>gs-1u0</td><td>-gs-1ug</td><td>0</td><td>yes</td></tr><tr><td>Radau IA</td><td>s-1</td><td>-s-1</td><td>1 4s-2</td><td>no</td></tr><tr><td>Radau II A</td><td>ss-1</td><td>-s-1</td><td>1 4s-2</td><td>no</td></tr><tr><td>Radau I B</td><td>ms-1</td><td>-s-1</td><td>0</td><td>yes</td></tr><tr><td>Radau I B</td><td>ms-1</td><td>-s-1</td><td>0</td><td>yes</td></tr></table>

For the Gauss–Legendre method

$$
\begin{array} { r } { X _ { G L } = \left[ \begin{array} { c c c c c c } { \frac { 1 } { 2 } } & { - \xi _ { 1 } } & & & & & \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } & & & & { o } \\ & { \xi _ { 2 } } & { \ddots } & { \ddots } & & \\ & & { \ddots } & { \ddots } & { \ddots } & \\ & & & { \ddots } & { \ddots } & { - \xi _ { s - 1 } } \\ { O } & & & & { \xi _ { s - 1 } } & { 0 } \end{array} \right] , } \end{array}
$$

where $\xi _ { k } = \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } \big ( k = 0 , 1 , \cdots , s - 1 \big ) .$ .

Corollary 2.2. If coefficients of $P { - } R { - } K$ method satisfy $b _ { i } \ = \ B _ { i }$ , $c _ { i } = C _ { i } , c _ { i }$ and $b _ { i } \neq 0 ( i = 1 , \cdots , s )$ , and

$$
W ^ { \mathrm { T } } \overline { { { M } } } W = X + \overline { { { X } } } ^ { \mathrm { T } } - e _ { 1 } e _ { 1 } ^ { \mathrm { T } } ,
$$

then $P { - } R { - } K$ method is symplectic.

Corollary 2.3. $( \mathrm { S u n } ) ^ { [ \mathrm { S u n } 9 3 \mathrm { b } ] }$ Given a $s$ -stage $R – K$ method and its coefficients $( A , b , c )$ . If the coefficients $c _ { i } , b _ { i } \neq 0 ( i = 1 , \cdots , s )$ satisfy order conditions of $R – K$ method $B ( p ) , ~ C ( \eta )$ and $D ( \zeta )$ , then the $P { - } R { - } K$ method produced by the coefficient of aij , a¯ij = bj 1 − ajib  , $b _ { i } , \ c _ { i }$ is symplectic with order $r = \operatorname* { m i n } \left( p , 2 \eta + 2 , 2 \zeta + \right.$ 2, $\eta + \zeta + 1 )$ .

Corollary 2.4. Method of Radau IA has order $2 s - 1$ , by Corollary 2.3, method of Radau IA and Radau $I \overline { { A } }$ is symplectic with order $2 s - 1$ .

Example 2.5. P–R–K method with first order accuracy Radau IA–I A

$$
\begin{array}{c} { \frac { 0 } { | \begin{array} { l l l l l l l l } { 1 } & { } & { } & { 0 } & { | } & { 0 } & { } & { } & { | } & { { \frac { 1 } { 2 } } | } \\ { 1 } & { } & { } & { } & { } & { 1 } & { } & { } & { } \end{array} | } } \end{array}  \Longrightarrow \quad { \frac { | \begin{array} { l l l l l l l l l l l } { { \frac { 1 } { 2 } } } & { } & { } & { } & { } & { } & { } & { } & { } \\ { 1 } & { } & { } & { } & { } & { } & { } & { } & { } \end{array} | } }
$$

Example 2.6. P–R–K method with third order accuracy Radau I A – IA   

<table><tr><td rowspan=2 colspan=1>02</td><td rowspan=1 colspan=3>1      1        04</td><td rowspan=1 colspan=3>0    0</td><td rowspan=1 colspan=1>1      1</td></tr><tr><td rowspan=1 colspan=1>54    12</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>1    13    3</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>324     8</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1    3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4    3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1-4     4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1     4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4    4</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr></table>

Corollary 2.7. Constructs symplectic P–R–K method Radau II A – Radau II A with the similar method.

Example 2.8. P–R–K method with first order accuracy Radau II A – Radau II A

<table><tr><td>1</td><td>1 1</td><td>0</td><td>1 2</td></tr><tr><td></td><td>1</td><td>1</td><td>1</td></tr></table>

Example 2.9. P–R–K method with third order accuracy Radau II A – Radau II A   

<table><tr><td rowspan=2 colspan=1>11</td><td rowspan=1 colspan=1>5       112      12</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1   0</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>38      1247     18     8</td></tr><tr><td rowspan=1 colspan=1>3      14      4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1    0</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>4   4</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>4     1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4      4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Corollary 2.10. Using same method constructed symplectic $P { - } R { - } K$ method Lobatto III $C - I I I \overline { { C } }$ with $2 s - 2$ order accuracy.

Example 2.11. Symplectic P–R–K Lobatto III C–III C method with 2 order accuracy, its coefficients are

$$
\frac { 1 } { \frac { 1 } { 2 } \frac { 1 } { \frac { 1 } { 2 } } } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } } \frac { 0 } { \frac { 1 } { 2 } } \frac { 0 } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } } \frac { 1 } { \frac { 1 } { 2 } }
$$

Example 2.12. Symplectic P–R–K Lobatto III $\mathrm { C } - \mathrm { I I I } \overline { { \mathrm { C } } }$ method, its coefficients are

$$
\begin{array}{c} { \begin{array} { r c } { 0 } \\ { { \left| \begin{array} { l l l l l l l } { { \frac { 1 } { 6 } } } & { - { \frac { 1 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { { \frac { 5 } { 1 2 } } } & { - { \frac { 1 } { 1 2 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 1 2 } } } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } & { { \frac { 1 } { 6 } } } \end{array} \right| } } \end{array} }   & { { \Longrightarrow } } & { { { \frac { { \left| \begin{array} { l l l l l l } { { \frac { 1 } { 1 2 } } } & { - { \frac { 1 } { 6 } } } & { { \frac { 1 } { 1 2 } } } & { 0 } \\ { { \frac { 5 } { 2 4 } } } & { { \frac { 4 } { 1 2 } } } & { - { \frac { 1 } { 2 4 } } } & { 0 } \\ { { \frac { 1 } { 1 2 } } } & { { \frac { 5 } { 6 } } } & { { \frac { 1 } { 1 2 } } } & { 0 } \\ { { \frac { 1 } { 6 } } } & { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 6 } } } & { 0 } \end{array} \right| } } } } \end{array} }
$$

Corollary 2.13. The $s$ -stage $P { - } R { - } K$ Lobatto III $A$ –III $B$ method is symplectic with $2 s - 2$ order accuracy.

Example 2.14. Symplectic P–R–K Lobatto III A–III B method, its coefficients are

<table><tr><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>14</td><td>0</td><td></td></tr><tr><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1-4</td><td></td></tr><tr><td></td><td></td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td></td><td>1 1</td><td></td></tr><tr><td></td><td>0 0</td><td>0</td><td></td><td>1</td><td>1</td><td>0</td><td>1</td><td>1 12</td><td>0</td></tr><tr><td></td><td></td><td>1</td><td></td><td>1-61-6</td><td></td><td>0</td><td></td><td></td><td>1</td></tr><tr><td>长</td><td>3</td><td>24</td><td></td><td></td><td>1</td><td></td><td>16</td><td>13</td><td>48</td></tr><tr><td></td><td></td><td>1</td><td></td><td></td><td>5</td><td>0</td><td>1</td><td>2</td><td>1</td></tr><tr><td></td><td></td><td>6</td><td></td><td></td><td>6</td><td></td><td></td><td>12</td><td>12</td></tr><tr><td></td><td>1</td><td>2-3</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td></tr><tr><td></td><td></td><td></td><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

With the help of symplectic conditions of P–R–K methods, we can construct symplectic $\mathbf { R - K }$ method. We have the following corollary:

Corollary 2.15. $[ \mathrm { S u n } ] ^ { [ \mathrm { S u n } 0 0 ] }$ The s-stage $R$ –K method with coefficients $a _ { i j } ^ { * } = \frac { 1 } { 2 } ( a _ { i j } +$ $A _ { i j }$ ), $b _ { i } ^ { * } = b _ { i } = B _ { i }$ and $c _ { i } ^ { * } = c _ { i }$ are symplectic and at least satisfy $B ( p ) , C ( \xi )$ and $D ( \xi )$ , i.e., order

$$
r = \operatorname* { m i n } ( p , 2 \xi + 1 ) , \quad w h e r e \quad \xi = \operatorname* { m i n } \big ( \eta , \zeta \big ) .
$$

Example 2.16. If we take the coefficients in Example 2.14, we know that the right of the table is a special case of 2-order accuracy of $\mathbf { R - K }$ methods of Lobatto III S i.e., $\sigma = \frac { 1 } { 2 }$ situation of literature [Chi97] , see Table 2.1 .

# 7.2.2 Symplified Order Conditions of Explicit Symplectic R–K Method

The following $s$ -stage scheme is well-known[ZQ95b]

$$
\begin{array} { l } { { p _ { i } ~ = ~ p _ { i - 1 } + c _ { i } h f ( q _ { i - 1 } ) , } } \\ { { q _ { i } ~ = ~ q _ { i - 1 } + d _ { i } h g ( p _ { i } ) , ~ i = 1 , 2 , \cdots , s , } } \end{array}
$$

where $f = - v _ { q } ( q ) , g = u _ { p } ( p )$ . We can regard $f , g$ as a function of ${ z } = ( p , q )$ , for $f$ $( \mathrm { o r } g )$ with the $p$ (or $q$ ) variables of coefficient 0, i.e., $f ( q , 0 \cdot p )$ (or $g ( p , 0 \cdot q )$ . In order to facilitate the writing in a unified form, we make:

$$
p = y _ { a } , \quad q = y _ { b } , \quad f = f _ { a } , \quad g = f _ { b } , \quad y _ { a , 0 } = p _ { 0 } , \quad y _ { b , 0 } = q _ { 0 } ,
$$

and $y _ { a , 1 } = p _ { s - 1 }$ , $y _ { b , 1 } = q _ { s - 1 }$ , then Equation (2.8) is transformed into an $s$ -stage P–R–K form:

$$
\begin{array} { l } { { q _ { 1 , a } = y _ { a , 0 } = p _ { 0 } , } } \\ { { q _ { 1 , b } = y _ { b , 0 } = q _ { 0 } , } } \\ { { \displaystyle { q _ { 2 , a } = y _ { a , 0 } + c _ { 1 } \tau _ { f a } ( q _ { 0 } ) = y _ { a , 0 } + c _ { 1 } h f _ { a } ( g _ { 1 , b } ) = p _ { 1 } , } } } \\ { { g _ { 2 , b } = y _ { b , 0 } + d _ { 1 } \tau f _ { b } ( p _ { 1 } ) = y _ { b , 0 } + d _ { 1 } h f _ { b } ( g _ { 2 , a } ) = q _ { 1 } , } } \\ { { \displaystyle ~ \vdots ~ } } \\ { { g _ { s , a } = y _ { a , 0 } + h \sum _ { j = 1 } ^ { s - 1 } c _ { j } f _ { a } ( g _ { j , b } ) = p _ { s - 1 } , } } \\ { { \displaystyle ~ { \frac { s - 1 } { \rho _ { 1 } \rho _ { b } = y _ { b , 0 } + h \sum _ { j = 1 } ^ { s - 1 } d _ { j } f _ { b } ( g _ { j + 1 , a } ) = q _ { s - 1 } } } . } } \end{array}
$$

(2.9) is equivalent to

$$
\begin{array} { l } { g _ { i , a } = y _ { a , 0 } + h \displaystyle \sum _ { j = 1 } ^ { i - 1 } c _ { j } f _ { a } ( g _ { j , b } ) , } \\ { g _ { i , b } = y _ { b , 0 } + h \displaystyle \sum _ { j = 1 } ^ { i - 1 } d _ { j } f _ { b } ( g _ { j + 1 , a } ) , \quad i = 2 , \cdots , s , } \\ { y _ { a , 1 } = y _ { a , 0 } + h \displaystyle \sum _ { j = 1 } ^ { s - 1 } c _ { j } f _ { a } ( g _ { j , b } ) , } \\ { y _ { b , 1 } = y _ { b , 0 } + h \displaystyle \sum _ { j = 1 } ^ { s - 1 } d _ { j } f _ { b } ( g _ { j + 1 , a } ) . } \end{array}
$$

And (2.2) can be rewritten with new variables as

$$
\left[ \begin{array} { l } { \dot { y } _ { a } } \\ { \dot { y } _ { b } } \end{array} \right] = \left[ \begin{array} { l } { f _ { a } ( y _ { b } ) } \\ { f _ { b } ( y _ { a } ) } \end{array} \right] .
$$

Let

$$
\begin{array} { l l l l l } { { a _ { 1 } = c _ { 1 } , } } & { { a _ { 2 } = c _ { 2 } , } } & { { \cdots \cdot \cdot , } } & { { a _ { s - 1 } = c _ { s - 1 } , } } & { { a _ { s } = 0 , } } \\ { { b _ { 1 } = 0 , } } & { { b _ { 2 } = d _ { 1 } , } } & { { \cdots \cdot , } } & { { b _ { s - 1 } = d _ { s - 2 } , } } & { { b _ { s } = d _ { s - 1 } , } } \end{array}
$$

then schemes (2.10) now become

$$
\begin{array} { l } { { \displaystyle { { \mathcal { I } } _ { i , a } } = y _ { a , 0 } + h \displaystyle \sum _ { j = 1 } ^ { i - 1 } { a _ { j } f _ { a } ( g _ { j , b } ) } = y _ { a , 0 } + h \displaystyle \sum _ { j = 1 } ^ { i - 1 } { a _ { j } R _ { j , a } } , } } \\ { { \displaystyle { { \mathcal { I } } _ { i , b } } = y _ { b , 0 } + h \displaystyle \sum _ { j = 1 } ^ { i } { d _ { j } f _ { b } ( g _ { j , a } ) } = y _ { b , 0 } + \displaystyle \sum _ { j = 1 } ^ { i } { b _ { j } R _ { j , b } } , \quad i = 2 , \cdots , s , } } \\ { { \displaystyle y _ { a , 1 } = y _ { a , 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } { a _ { j } R _ { j , a } } , } } \\ { { \displaystyle y _ { b , 1 } = y _ { b , 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } R _ { j , b } } . } \end{array}
$$

Where

$$
R _ { i , a } = f _ { a } ( g _ { i , b } ) , \quad R _ { i , b } = f _ { b } ( g _ { i , a } ) .
$$

Now, we just need to study the order conditions of scheme (2.13) when $a _ { s } = b _ { 1 } = 0$ . Notice that $a _ { s } = b _ { 1 } = 0$ is necessary for (2.13) to be canonical and is also crucial for simplifying order conditions, as we will see later.

A $P$ -graph (denoted by $P G$ ) is a special graph which satisfies the following conditions: (i) its vertices are divided into two classes: “white” $\circ$ “black” $\bullet$ , sometimes instead “meagre” and “fat”. (ii) the two adjacent vertices of a $P G$ cannot be of the same class. If we give the vertices of PG an arbitrary set of labels, we get a label $P -$ - graph, and we say $P$ -graph $\in \ P G$ . Two labeled $P$ -graphs are said to be isomorphic labeled $P$ -graphs if they are just two different labelings of the same $P$ -graph.

A simple path joins a pair of vertices $v$ and $w$ , $v \neq w$ , and is a sequence of pairwise distinct vertices $v = v _ { 0 } , v _ { 1 } , \cdot \cdot \cdot , v _ { n - 1 } = w$ , where $v _ { i } \neq v _ { i - 1 }$ , $( v _ { i - 1 } , v _ { i } ) \in E$ . Fig. 2.1 shows an example of a simple path of $v$ and $w$ for $n = 4$ .

![](images/f7abf17ed6f5b92f5ced881629af7284ce5a01b38a9f13158e5247057bda7272.jpg)  
Fig. 2.1. A simple path of $v$ and $w$ black $\bullet$ and white $^ { \circ }$ , for $\scriptstyle n = 4$

(1) The definition of a $P$ -tree $P \tau$ , a labeled $P$ -tree (denoted by $\lambda P \tau$ ), a rooted labeled $P$ -tree $\rho \lambda P \tau$ of the same order $n$ are just as that of tree $\tau$ , labeled by tree $\lambda \tau$ , rooted tree $\rho \tau$ , and rooted labeled tree $\rho \lambda \tau$ , where the general graph is substituted by the $P$ -graph.

(2) We define the isomorphism of two labeled $P$ -trees below. Generally tree’s isomorphism and the $P$ -tree’s isomorphism are all in accordance with the type of labeling used. This has been described before. Here we give the precise definition for a $P$ -tree.

Two labeled $P$ -trees $\{ V _ { 1 } , E _ { 1 } \}$ and $\{ V _ { 2 } , E _ { 2 } \}$ are called isomorphism, if the order of these tree is the same, and there exists a bijection mapping $\chi$ , from $V _ { 1 }$ to $V _ { 2 }$ and $E _ { 1 }$ to $E _ { 2 }$ satisfies

$$
K ( \chi ( v _ { 1 } ) ) = K ( v _ { 1 } ) ,
$$

where $v _ { 1 } \in V _ { 1 }$ , and

$$
K ( v ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { f o r ~ } } v { \mathrm { ~ b l a c k } } , } \\ { 0 , } & { { \mathrm { f o r ~ } } v { \mathrm { ~ w h i t e } } . } \end{array} \right. }
$$

A $P$ -tree ( $\stackrel { \cdot } { n }$ order) is the equivalent of such a class, it consists of a labeled $P$ -tree and all of its isomorphism. We use [HNW93] the $P$ -series and tree method to derive the order condition of Equation (2.13) below. We first introduce some definitions and notations.

(3) Two rooted labeled $P$ -trees with same order, $\{ V _ { 1 } , E _ { 1 } , r _ { 1 } \}$ and $\{ V _ { 2 } , E _ { 2 } , r _ { 2 } \}$ (where $r _ { i }$ $( i = 1 , 2 )$ denoted rooted label), are called rooted isomorphism if there exists a $\chi$ that satisfies the condition of (2), and $\chi ( r _ { 1 } ) = r _ { 2 }$ holds.

A rooted $P$ -tree, denoted by $\rho P \tau$ , is an equivalence class which contains a labeled $P$ -tree and all of its isomorphic $P$ -trees. We denote $\rho P \tau _ { a } ( \rho P \tau _ { b } )$ as $\rho P \tau$ with white (black) root, and $\rho \lambda P \tau$ as rooted labeled $P$ -tree, which is obtained by adding label to $\rho P \tau$ . Thus $\rho \lambda P \tau \in \rho P \tau$ .

We denote by $\rho P \tau _ { a }$ (resp. $\rho P \tau _ { b }$ ) for a rooted $P$ -tree $\rho P \tau$ that has a white (resp. black) root. If we give the vertices of a rooted $P$ -tree $\rho P \tau$ such a set of labels so that the label of a father vertex is always smaller than that of its sons, we then get a monotonically labeled rooted $P$ -tree ${ \cal M } \rho \lambda { \cal P } \tau$ . We denote by $\alpha ( \rho P \tau )$ the number of possible different monotonic labelings of $\rho P \tau$ when the labels are chosen from the set $A _ { q } = \left\{ \begin{array} { l l } { \begin{array} { r l r } \end{array} } \end{array} \right.$ the first $q$ letters of $i < j < k < l < \cdot \cdot \cdot \}$ , where $q$ is the order of $\rho P \tau$ .

The set of all rooted trees of order $n$ with a white (resp. black) root is denoted by $T P _ { n } ^ { a }$ (resp. $T P _ { n . } ^ { b }$ ). Let us denote by $\lambda P \tau _ { n } ^ { a }$ (resp. $\lambda P \tau _ { n } ^ { b } )$ ) the set of all rooted labeled $P$ -trees of order $n$ with a white (resp. black) root vertex, and $M \lambda P \tau _ { n } ^ { a }$ (resp. $M \lambda P \tau _ { n } ^ { b } ,$ ) the set of all monotonically labeled $P$ -tree of order $n$ with a white (resp. black) root vertex when the labels are chose from the set $A _ { n }$ .

(4) The density $\gamma ( \rho \lambda \tau )$ of a rooted $P$ -tree $\rho \lambda \tau$ is defined recursively as

$$
\gamma ( \rho \lambda \tau ) = r ( \rho \lambda \tau ) \gamma ( \rho \lambda \tau ^ { 1 } ) \cdot \cdot \cdot \gamma ( \rho \lambda \tau ^ { m } ) ,
$$

where $r ( \rho \lambda \tau )$ is order of $\rho \lambda \tau$ , and $\rho \lambda \tau ^ { 1 } , \cdot \cdot \cdot , \rho \lambda \tau ^ { m }$ are the sub-trees which arise when the root of $\rho \lambda \tau$ is moved from the tree. The density of rooted $P$ -tree $\rho P \tau$ is calculated by regarding them as general rooted tree neglecting the difference between with the black and white vertices .

(5) Let $\rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m }$ be rooted $P$ -tree. We denote by $\rho P \tau = { } _ { a } [ \rho P \tau ^ { 1 } , \cdot \cdot \cdot ,$ $\rho P \tau ^ { m } ]$ the unique rooted $P$ -tree that arises when the roots of $\rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m }$ are all attached to a white root vertex. Similarly denote it by $\mathsf { \Phi } _ { b } [ \rho P \tau ^ { 1 } , \cdots , \rho P \tau ^ { m } ]$ when the root of the $P$ -tree is black. We say $\rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m }$ are sub-trees of $\rho P \tau$ . We further denote the rooted $P$ -tree of order 1, which has a white (resp.black) root vertex by $t _ { a } ( \mathrm { r e s p . } t _ { b } )$ .

(6) (2.11) is defined recursively as:

$$
\begin{array} { r c l } { { } } & { { } } & { { F ( t _ { a } ) ( y ) ~ = ~ f _ { a } ( y ) , ~ { \cal F } ( t _ { b } ) ( y ) = f _ { b } ( y ) , } } \\ { { } } & { { } } & { { F ( \rho P \tau ) ( y ) ~ = ~ { \frac { \partial ^ { m } f _ { w ( \rho P t ) } ( y ) } { \partial y _ { w ( \rho P \tau ^ { 1 } ) } \cdot \cdot \cdot \partial y _ { w ( \rho P \tau ^ { m } ) } } } \big ( F ( \rho P \tau ^ { 1 } ) ( y ) \cdot \cdot \cdot F ( \rho P \tau ^ { m } ) ( y ) \big ) , } } \end{array}
$$

where $\boldsymbol { y } = \left( y _ { a } , y _ { b } \right)$ , and $\rho P \tau = { } _ { a } [ \rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m } ]$ or $\rho P \tau = { } _ { b } [ \rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m } ]$ , and $w ( \rho P \tau )$ is defined by:

$$
w ( \rho P \tau ) = \left\{ \begin{array} { l l } { a , } & { \mathrm { i f ~ } \rho P \tau \mathrm { ~ a t t a c h e d ~ t o ~ a ~ w h i t e ~ r o o t ~ v e r t e x } , } \\ { b , } & { \mathrm { i f ~ } \rho P \tau \mathrm { ~ a t t a c h e d ~ t o ~ a ~ b l a c k ~ r o o t ~ v e r t e x } . } \end{array} \right.
$$

We see that $F ( \rho P \tau )$ is independent of labeling. Here, and in the remainder of this book, in order to avoid sums and unnecessary indices, we assume that $y _ { a }$ and $y _ { b }$ are scalar quantities , and $f _ { a } , f _ { b }$ scalar functions. All subsequent formulas remain valid for vectors if the derivatives are interpreted as multi-linear mapping.

Lemma 2.17. The derivatives of the exact solution of (2.11) satisfy:

$$
\begin{array} { l } { { \displaystyle y _ { a } ^ { ( a ) } = \sum _ { \rho \lambda P \tau \in M \lambda T P _ { q } ^ { \alpha } } F ( \rho \lambda P \tau ) ( y _ { a } , y _ { b } ) = \sum _ { \rho P \tau \in T P _ { q } ^ { \alpha } } \alpha ( \rho P \tau ) F ( \rho P \tau ) ( y _ { a } , y _ { b } ) , } } \\ { { \displaystyle y _ { b } ^ { ( a ) } = \sum _ { \rho \lambda P \tau \in M \lambda T P _ { q } ^ { b } } F ( \rho \lambda P \tau ) ( y _ { a } , y _ { b } ) = \sum _ { \rho P \tau \in T P _ { q } ^ { b } } \alpha ( \rho P \tau ) F ( \rho P \tau ) ( y _ { a } , y _ { b } ) , } } \end{array}
$$

where $q = 1 , 2 , \cdots$ .

It is convenient to introduce two new rooted $P$ -trees of order 0: $\varnothing _ { a }$ and $\varnothing _ { b }$ . The corresponding elementary differential are $F ( \varnothing _ { a } ) = y _ { a }$ , $F ( \emptyset _ { b } ) = y _ { b }$ .

We further set

$$
\begin{array} { l } { { T P ^ { a } = \emptyset _ { a } \cup T P _ { 1 } ^ { a } \cup T P _ { 2 } ^ { a } \cup \dots , } } \\ { { T P ^ { b } = \emptyset _ { b } \cup T P _ { 1 } ^ { b } \cup T P _ { 2 } ^ { b } \cup \dots , } } \\ { { \lambda T P ^ { a } = \emptyset _ { a } \cup \lambda T P _ { 1 } ^ { a } \cup \lambda T P _ { 2 } ^ { a } \cup \dots , } } \\ { { \lambda T P ^ { b } = \emptyset _ { b } \cup \lambda T P _ { 1 } ^ { b } \cup \lambda T P _ { 2 } ^ { b } \cup \dots , } } \\ { { M \lambda T P ^ { a } = \emptyset _ { a } \cup M \lambda T P _ { 1 } ^ { a } \cup M \lambda T P _ { 2 } ^ { a } \cup \dots , } } \\ { { M \lambda T P ^ { b } = \emptyset _ { b } \cup M \lambda T P _ { 1 } ^ { b } \cup M \lambda T P _ { 2 } ^ { b } \cup \dots . } } \end{array}
$$

$p$ -series: let $c ( \emptyset _ { a } ) , c ( \emptyset _ { b } ) , c ( t _ { a } ) , c ( t _ { b } ) , \cdot \cdot \cdot$ be real coefficients defined for all $P$ - trees, $c : T P ^ { a } \cup T P ^ { b }  \mathbf { R }$ . The series $p ( c , y ) = ( p _ { a } ( c , y ) , p _ { b } ( c , y ) )$ is defined as

$$
\begin{array} { r l } { p _ { a } ( c , y ) } & { = \displaystyle \sum _ { \rho \lambda P \tau \in M \lambda T P ^ { a } } \frac { h ^ { r ( \rho \lambda P \tau ) } } { r ( \rho \lambda P \tau ) ! } c ^ { ( \rho \lambda P \tau ) } F ( \rho \lambda P \tau ) ( y ) } \\ & { = \displaystyle \sum _ { \rho P \tau \in T P ^ { a } } \alpha ( \rho P \tau ) \frac { h ^ { r ( \rho \lambda P \tau ) } } { ( \rho \lambda P \tau ) ! } c ^ { ( \rho \lambda P \tau ) } F ( \rho \lambda P \tau ) ( y ) , } \\ { p _ { b } ( c , y ) } & { = \displaystyle \sum _ { \rho \lambda P \tau \in M \lambda T P ^ { b } } \frac { h ^ { r ( \rho \lambda P \tau ) } } { ( \rho \lambda P \tau ) ! } c ^ { ( \rho \lambda P \tau ) } F ( \rho \lambda P \tau ) ( y ) } \\ & { = \displaystyle \sum _ { \rho P \tau \in T P ^ { b } } \alpha ( \rho P \tau ) \frac { h ^ { r ( \rho \lambda P \tau ) } } { r ( \rho \lambda P \tau ) ! } c ^ { ( \rho \lambda P \tau ) } F ( \rho \lambda P \tau ) ( y ) . } \end{array}
$$

Notice that $c$ is defined on $T P ^ { a } \cup T P ^ { b }$ , and for any labelings of $\rho P \tau$ (especially for monotonic labeling $\rho \lambda P \tau )$ , we have $c ( \rho \lambda P \tau ) = c ( \rho P \tau )$ . Lemma 2.17 states simply that the exact solution is a $p$ -series,

$$
{ { \left( { { y } _ { a } } ( t _ { 0 } + h ) , { { y } _ { b } } ( t _ { 0 } + h ) \right) } ^ { \mathrm { T } } } = p { { \left( { Y } , { { y } _ { a } } ( t _ { 0 } ) , { { y } _ { b } } ( t _ { 0 } ) \right) } } ,
$$

where $Y ( \rho P \tau ) = 1$ for all rooted $P$ -trees $\rho P \tau$ . The following theorem is from the book[HNW93] .

Theorem 2.18. Let $c : T P ^ { a } \cup T P ^ { b }  \mathbf { R } ,$ , be a sequence of coefficients such that $c ( \emptyset _ { a } ) = c ( \emptyset _ { b } ) = 1$ . Then

$$
h { \left[ \begin{array} { l } { f _ { a } { \big ( } p ( c , ( y _ { a } , y _ { b } ) ) { \big ) } } \\ { f _ { b } { \big ( } p ( c , ( y _ { a } , y _ { b } ) ) { \big ) } } \end{array} \right] } = p { \big ( } c ^ { \mathrm { T } } , ( y _ { a } , y _ { b } ) { \big ) } ,
$$

with

$$
\begin{array} { r l } & { c ^ { \mathrm { T } } ( \varnothing _ { a } ) = c ^ { \mathrm { T } } ( \varnothing _ { b } ) = 0 , \quad c ^ { \mathrm { T } } ( t _ { a } ) = c ^ { \mathrm { T } } ( t _ { b } ) = 1 , } \\ & { c ^ { \mathrm { T } } ( \rho P \tau ) = r ( \rho P \tau ) c ( \rho P \tau ^ { 1 } ) \cdot \cdot \cdot c ( \rho P \tau ^ { m } ) , } \\ & { \rho P \tau = _ { a } [ \rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m } ] , \quad o r \quad \rho P \tau = _ { b } [ \rho P \tau ^ { 1 } , \cdot \cdot \cdot , \rho P \tau ^ { m } ] . } \end{array}
$$

Let

$$
\left\{ \begin{array} { l l } { R _ { i , a } = p _ { a } \big ( K _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \big ) , } & \\ { R _ { i , b } = p _ { b } \big ( K _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \big ) , } & \\ { g _ { i , a } = p _ { a } \big ( G _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \big ) , } & \\ { g _ { i , b } = p _ { b } \big ( G _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \big ) , } & \end{array} \right. \quad i = 1 , \cdots , s ,
$$

where $K _ { i } ( i = 1 , \cdots , s ) : T P ^ { a } \cup T P ^ { b }  \mathbf { R }$ $\cdot \cdot , s ) : T P ^ { a } \cup T P ^ { b } \to \mathbf { R } , G _ { i } \left( i = 1 , \cdot \cdot \cdot , s \right) : T P ^ { a } \cup T P ^ { b } \to \mathbf { R }$ are two sets of $p$ -series. From (2.10), we have $G _ { i } ( \emptyset _ { a } ) = G _ { i } ( \emptyset _ { b } ) = 1$ . Hence, From (2.14), we have

$$
\begin{array} { r l r } { \Big ( K _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } & { = } & { \left[ \begin{array} { l } { p _ { a } \Big ( K _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } \\ { p _ { b } \Big ( K _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } \end{array} \right] = \left[ \begin{array} { l } { R _ { i , a } } \\ { R _ { i , b } } \end{array} \right] = h \left[ \begin{array} { l } { f _ { a } ( g _ { i , b } ) } \\ { f _ { b } ( g _ { i , a } ) } \end{array} \right] } \\ & { = } & { h \left[ \begin{array} { l } { f _ { a } \Big ( p _ { b } \Big ( G _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) \Big ) } \\ { f _ { b } \Big ( p _ { a } \Big ( G _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) \Big ) } \end{array} \right] = h \left[ \begin{array} { l } { f _ { a } \Big ( p \Big ( G _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) \Big ) } \\ { f _ { b } \Big ( p \Big ( G _ { i \mathrm { , ~ } } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) \Big ) } \end{array} \right] } \\ & { = } & { p \Big ( G _ { i \mathrm { , ~ } } ^ { \prime } ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) . } \end{array}
$$

Then from Theorem 2.18, we get

$$
K _ { i } = G _ { i } ^ { \prime } , \quad \forall i = 1 , \cdot \cdot \cdot , s .
$$

But from (2.13), we have

$$
\begin{array} { r l } { p \Big ( G _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } &  = \begin{array} { l } { \displaystyle \left[ \begin{array} { l } { p _ { a } \Big ( G _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } \\ { p _ { b } \Big ( G _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } \end{array} \right] = \left[ \begin{array} { l } { y _ { a , 0 } + h \sum _ { j = 1 } ^ { i - 1 } a _ { j } R _ { j , a } } \\ { y _ { b , 0 } + h \sum _ { j = 1 } ^ { i } b _ { j } R _ { j , b } } \end{array} \right] } \\ & { = \begin{array} { l } { \displaystyle \left[ \begin{array} { l } { y _ { a , 0 } + h \sum _ { j = 1 } ^ { i - 1 } a _ { j } p _ { a } \Big ( K _ { j } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } \\ { y _ { b , 0 } + h \sum _ { j = 1 } ^ { i } b _ { j } p _ { b } \Big ( K _ { j } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) } \end{array} \right] . } \end{array} } \end{array} \end{array}
$$

Thus:

$$
\begin{array} { l l } { \displaystyle { G _ { i } ( \rho P \tau _ { a } ) = \sum _ { j = 1 } ^ { i - 1 } a _ { j } K _ { j } ( \rho P \tau _ { a } ) , } } & { } \\ { \displaystyle { \quad \forall r ( \rho P \tau ) \geq 1 . } } \\ { \displaystyle { G _ { i } ( \rho P \tau _ { b } ) = \sum _ { j = 1 } ^ { i } b _ { j } K _ { j } ( \rho P \tau _ { b } ) , } } \end{array}
$$

From (2.13), we also have

$$
\begin{array} { l } { { \displaystyle y _ { a , 1 } = y _ { a , 0 } + h \sum _ { i = 1 } ^ { s } p _ { a } \Big ( K _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) , } } \\ { { \displaystyle y _ { b , 1 } = y _ { b , 0 } + h \sum _ { i = 1 } ^ { s } p _ { b } \Big ( K _ { i } , ( y _ { a , 0 } , y _ { b , 0 } ) \Big ) . } } \end{array}
$$

Comparing the numerical solution obtained from (2.13) and the exact solution from (2.11), we get the order condition for scheme (2.13).

Theorem 2.19. Scheme (2.13) is $p$ -order accuracy iff its coefficients $a _ { i } , b _ { i }$ satisfy:

$$
\left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { s } a _ { i } K _ { i } ( \rho P \tau _ { a } ) = 1 , } & { \quad 1 \leq r ( \rho P \tau _ { a } ) \leq p , } \\ { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } K _ { i } ( \rho P \tau _ { b } ) = 1 , } & { \quad 1 \leq r ( \rho P \tau _ { b } ) \leq p , } \end{array} \right.
$$

where $K _ { i } ( i = 1 , \cdots , s ,$ ) are defined recursively by

$$
\left\{ \begin{array} { l l } { \displaystyle K _ { i } = G _ { i } ^ { \prime } , } \\ { \displaystyle G _ { i } ( \emptyset _ { a } ) = G _ { i } ( \emptyset _ { b } ) = 1 , } \\ { \displaystyle G _ { i } ( \rho P \tau _ { a } ) = \sum _ { j = 1 } ^ { i - 1 } a _ { j } K _ { j } ( \rho P \tau _ { a } ) , \quad } & { \displaystyle r ( \rho P \tau _ { a } ) , r ( \rho P \tau _ { b } ) \geq 1 . } \\ { \displaystyle G _ { i } ( \rho P \tau _ { b } ) = \sum _ { j = 1 } ^ { i } b _ { j } K _ { j } ( \rho P \tau _ { b } ) , } \end{array} \right.
$$

From the first and second equations of (2.23) we know $K _ { i } ( \emptyset _ { a } ) ~ = ~ K _ { i } ( \emptyset _ { b } ) ~ =$ 0, $~ K _ { i } ( t _ { a } ) ~ = ~ K _ { i } ( t _ { b } ) ~ = ~ 1$ , from the last two equations of (2.23) we can obtain $G _ { i } ( t _ { a } ) , G _ { i } ( t _ { b } )$ . Repeating this procedure, we can obtain $K _ { i } ( \rho P \tau _ { a } ) , K _ { i } ( \rho P \tau _ { b } )$ , by $P$ - tree order from low to high.

Next we rewrite equations (2.23) into more intuitive forms. From (2.23), we have

$$
\left\{ \begin{array} { l l } { \displaystyle K _ { i } ( \rho P \tau _ { a } ) = r ( \rho P \tau _ { a } ) \left( \sum _ { j = 1 } ^ { i } b _ { j } K _ { j } ( \rho P \tau _ { b } ^ { 1 } ) \right) \cdots \left( \sum _ { j = 1 } ^ { i } b _ { j } K _ { j } ( \rho P \tau _ { b } ^ { m _ { 1 } } ) \right) , } & \\ { \displaystyle K _ { i } ( \rho P \tau _ { b } ) = r ( \rho P \tau _ { b } ) \left( \sum _ { j = 1 } ^ { i - 1 } a _ { j } K _ { j } ( \rho P \tau _ { a } ^ { 1 } ) \right) \cdots \left( \sum _ { j = 1 } ^ { i - 1 } a _ { j } K _ { j } ( \rho P \tau _ { a } ^ { m _ { 2 } } ) \right) , } & \end{array} \right. ~ i = 2 , 3 , \cdots , s
$$

where

$$
\begin{array} { l } { \rho P \tau _ { a } = { } _ { a } [ \rho P \tau _ { b } ^ { 1 } , \cdot \cdot \cdot , \rho P \tau _ { b } ^ { m _ { 1 } } ] , } \\ { \rho P \tau _ { b } = { } _ { b } [ \rho P \tau _ { a } ^ { 1 } , \cdot \cdot \cdot , \rho P \tau _ { a } ^ { m _ { 2 } } ] . } \end{array}
$$

We now define elementary weight $\phi ( \rho P \tau )$ for a rooted $P$ -tree. Choose any labeling $\rho \lambda P \tau$ for $\rho P \tau$ ; without loss of generality we choose a monotonic one with labels $i < j < k < l < \cdots$ , where the rooted labeling is $i$ . Then $\phi$ can be obtained recursively (Note the difference of solving for $\phi$ between the original tree and its subtree)

$$
\left\{ \begin{array} { l l } { \displaystyle \phi ( \rho P \tau _ { a } ) = \sum _ { i = 1 } ^ { s - 1 } a _ { i } \big ( \phi ( \rho P \tau _ { b } ^ { 1 } ) , \cdots , \phi ( \rho P \tau _ { b } ^ { m _ { 1 } } ) \big ) , } \\ { \displaystyle \phi ( \rho P \tau _ { b } ) = \sum _ { i = 1 } ^ { s } b _ { i } \big ( \phi ( \rho P \tau _ { a } ^ { 1 } ) , \cdots , \phi ( \rho P \tau _ { a } ^ { m _ { 2 } } ) \big ) , } \\ { \displaystyle \phi ( \emptyset _ { a } ) = \phi ( \emptyset _ { b } ) = 1 , } \end{array} \right. \quad r ( \rho P \tau _ { a } ) , r ( \rho P \tau _ { b } ) \geq 1 ,
$$

where $\rho P \tau _ { a } , \rho P \tau _ { b }$ and (2.25) are the same. Here, notice that $i$ is the root of $\rho P \tau _ { a }$ or $\rho P \tau _ { b }$ , and $s$ is the label for an imaginary father vertex to the root $i$ . The summation is always with respect to subscripts of the son’s vertex, from 1 adds to the father vertex or it reduces by 1. Now $s$ is order of scheme (2.13). We are doing this only for ease of the recursive definition; otherwise vertex $i$ has no father vertex and the summation superscript cannot be determined. Regarding the subtrees of $\rho P \tau _ { a } , \rho P \tau _ { b }$ , the father vertex for their root labeling is $i$ . It is not necessary to add an extra father vertex. So the weight for a $p$ -tree as the original tree is different from the weight as another subset tree. By (2.26) we can see that the elementary weight of a tree $\phi$ is not related to its labeling as long as the imaginary father of maintaining root label is always the order of the scheme (2.13).

Theorem 2.20. [AS93,ZQ95b,SSC94] Order conditions in Theorem 2.19 are equivalent to

$$
\phi ( \rho P \tau ) = \frac { 1 } { \gamma ( \rho P \tau ) } , \quad \forall \rho P \tau \in T P ^ { a } \cup T P ^ { b } , \quad r ( \rho P \tau ) \leq p .
$$

Proof. We just need to prove

$$
\left\{ \begin{array} { l l } { \displaystyle { \phi ( \rho P \lambda \tau _ { a } ) \gamma ( \rho \lambda P \tau _ { b } ) = \sum _ { j = 1 } ^ { s - 1 } a _ { j } K _ { j } ( \rho P \tau _ { a } ) } , } \\ { \displaystyle { \phi ( \rho \lambda P \tau _ { b } ) \gamma ( \rho \lambda P \tau _ { a } ) = \sum _ { j = 1 } ^ { s } b _ { j } K _ { j } ( \rho \lambda P \tau _ { b } ) } . } \end{array} \right.
$$

From (2.23), we have

$$
\left\{ \begin{array} { l l } { \displaystyle K _ { i } \left( \rho \lambda P \tau _ { a } \right) = r ( \rho \lambda P \tau _ { a } ) \left( \displaystyle \sum _ { j _ { 1 } = 1 } ^ { i } b _ { j _ { 1 } } K _ { j _ { 1 } } ( \rho \lambda P \tau _ { b } ^ { 1 } ) \right) \cdot \cdot \cdot \left( \displaystyle \sum _ { j _ { m _ { 1 } } = 1 } ^ { i } b _ { j _ { m _ { 1 } } } K _ { j _ { m _ { 1 } } } ( \rho \lambda P \tau _ { b } ^ { m _ { 1 } } ) \right) , } \\ { \displaystyle K _ { i } \left( \rho \lambda P \tau _ { b } \right) = r ( \rho \lambda P \tau _ { b } ) \left( \displaystyle \sum _ { j _ { 1 } = 1 } ^ { i - 1 } a _ { j _ { m _ { 2 } } } K _ { j _ { m _ { 2 } } } ( \rho \lambda P \tau _ { a } ^ { 1 } ) \right) \cdot \cdot \cdot \left( \displaystyle \sum _ { j _ { m _ { 2 } } = 1 } ^ { i - 1 } a _ { j _ { m _ { 2 } } } K _ { j _ { m _ { 2 } } } ( \rho \lambda P \tau _ { a } ^ { m _ { 2 } } ) \right) , } \end{array} \right.
$$

where $i = 2 , 3 , \cdots , s$ , and

$$
\begin{array} { r l } & { \rho \lambda P \tau _ { a } = \mathsf { \Pi } _ { a } [ \rho P \tau _ { b } ^ { 1 } , \cdots , \rho \lambda P \tau _ { b } ^ { m _ { 1 } } ] , } \\ & { \rho \lambda P \tau _ { b } = \mathsf { \Pi } _ { b } [ \rho \lambda P \tau _ { a } ^ { 1 } , \cdots , \rho \lambda P \tau _ { a } ^ { m _ { 2 } } ] , } \end{array}
$$

while $j _ { 1 } , \cdots , j _ { m _ { 1 } }$ and $j _ { 1 } , \cdots , j _ { m _ { 2 } }$ are the labels of the roots of $\rho \lambda P \tau _ { b } ^ { 1 } , \cdot \cdot \cdot , \rho \lambda P \tau _ { b } ^ { m _ { 1 } }$ and $\lambda P \tau _ { a } ^ { 1 } , \cdot \cdot \cdot , \rho \lambda P \tau _ { a } ^ { m _ { 2 } }$ respectively. Due to

$$
\begin{array} { r l } { \le . \mathsf { o f } ( 2 . 2 8 ) } & { \iff \left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { s - 1 } a _ { i } r ( \rho \lambda P \tau _ { a } ) \Bigg ( \displaystyle \sum _ { j _ { 1 } = 1 } ^ { i } b _ { j _ { 1 } } K _ { j _ { 1 } } ( \rho \lambda P \tau _ { b } ^ { 1 } ) \Bigg ) \cdots \Bigg ( \displaystyle \sum _ { j _ { m _ { 1 } } = 1 } ^ { i } b _ { j _ { m _ { 1 } } } K _ { j _ { m _ { 1 } } } ( \rho \lambda P \tau _ { b } ^ { m _ { 1 } } ) \Bigg ) , } \\ { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } r ( \rho \lambda P \tau _ { b } ) \Bigg ( \displaystyle \sum _ { j _ { 1 } = 1 } ^ { i - 1 } a _ { j _ { 1 } } K _ { j _ { 1 } } ( \rho \lambda P \tau _ { a } ^ { 1 } ) \Bigg ) \cdots \Bigg ( \displaystyle \sum _ { j _ { m _ { 2 } } = 1 } ^ { i - 1 } a _ { j _ { m _ { 2 } } } K _ { j _ { m _ { 2 } } } ( \rho \lambda P \tau _ { a } ^ { m _ { 2 } } ) \Bigg ) , } \end{array} \right. } \\ { \le . \mathsf { o f } \left( 2 . 2 8 \right) } & { \iff \left\{ \begin{array} { l l } { \displaystyle \sum _ { i = 1 } ^ { s - 1 } a _ { i } r ( \rho \lambda P \tau _ { a } ) \Bigg ( \phi ( \rho \lambda P \tau _ { b } ^ { 1 } ) \gamma ( \rho \lambda P \tau _ { b } ^ { 1 } ) \Bigg ) \cdots \Bigg ( \phi ( \rho \lambda P \tau _ { b } ^ { m _ { 1 } } ) \gamma ( \rho \lambda P \tau _ { b } ^ { m _ { 1 } } ) \Bigg ) , } \\ { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } r ( \rho \lambda P \tau _ { b } ) \Big ( \phi ( \rho \lambda P \tau _ { a } ^ { 1 } ) \gamma ( \rho \lambda P \tau _ { a } ^ { 1 } ) \Big ) \cdots \Bigg ( \phi ( \rho \lambda P \tau _ { a } ^ { m _ { 2 } } ) \gamma ( \rho \lambda P \tau _ { a } ^ { m _ { 2 } } ) \Bigg ) , } \end{array} \right. } \end{array}
$$

so we have to prove

$$
\phi ( \rho \lambda P \tau _ { b } ^ { l } ) \gamma ( \rho \lambda P \tau _ { b } ^ { l } ) = \sum _ { j _ { n } = 1 } ^ { i } b _ { j _ { n } } K _ { j _ { n } } ( \rho P \tau _ { b } ^ { l } ) \quad \mathrm { f o r } \quad n = 1 , \cdots , m _ { 1 } ,
$$

and

$$
\phi ( \rho P \tau _ { a } ^ { l } ) \gamma ( \rho P \tau _ { a } ^ { l } ) = \sum _ { j _ { n } = 1 } ^ { i - 1 } a _ { j _ { n } } K _ { j _ { n } } ( \rho P \tau _ { a } ^ { l } ) \quad \mathrm { f o r } \quad n = 1 , \cdots , m _ { 2 } .
$$

Continue this process and finally we see it is enough to prove

$$
\phi ( t _ { a } ) \gamma ( t _ { a } ) = \sum _ { l = 1 } ^ { f ( l ) - 1 } a _ { l } K _ { l } ( t _ { a } ) , \quad \phi ( t _ { b } ) \gamma ( t _ { b } ) = \sum _ { l = 1 } ^ { f ( l ) - 1 } b _ { l } K _ { l } ( t _ { b } ) ,
$$

where $l$ is the label of $t _ { a }$ or $t _ { b }$ and $f ( l )$ is the label of the father. Since

$$
\begin{array} { l } { { \phi ( t _ { a } ) \gamma ( t _ { a } ) = \displaystyle \sum _ { l = 1 } ^ { f ( l ) - 1 } a _ { l } \cdot 1 = \sum _ { l = 1 } ^ { f ( l ) - 1 } a _ { l } \cdot K _ { l } ( t _ { a } ) = \sum _ { l = 1 } ^ { f ( l ) - 1 } a _ { l } , } } \\ { { \phi ( t _ { b } ) \gamma ( t _ { b } ) = \displaystyle \sum _ { l = 1 } ^ { f ( l ) } b _ { l } \cdot 1 = \sum _ { l = 1 } ^ { f ( l ) } b _ { l } \cdot K _ { l } ( t _ { b } ) = \sum _ { l = 1 } ^ { f ( l ) } b _ { l } , } } \end{array}
$$

and

$$
K _ { l } ( t _ { a } ) = 1 , \quad K _ { l } ( t _ { b } ) = 1 .
$$

The theorem is proved.

Let $P \tau$ be a tree of order $p$ $\left( p \geq 2 \right)$ ) $P$ -tree. Choose any label to obtain $\lambda P \tau$ . Let $v$ and $w$ be two adjacent vertices. We consider four rooted $P$ -tree . Denote $\rho P \tau ^ { v }$ (resp. $\rho P \tau ^ { w } )$ as the rooted $P$ -tree obtained by regarding the vertex $v$ (resp.w) as the root of $\rho P \tau$ . Denote $\rho P \tau _ { v }$ (resp. ${ \rho } P \tau _ { w } )$ the rooted $P$ -tree, which arises when the edge $( v , w )$ is deleted from $P \tau$ and has the root $v$ (resp. $w$ ). Without loss of generality, let $v$ be white, and $w$ be black.

Theorem 2.21. [AS93,ZQ95b,SSC94] With the above notations, we have:

Proof. By the definition of $\gamma$ , we have

$$
\begin{array} { r } { \gamma ( \rho P \tau ^ { v } ) = n \gamma ( \rho P \tau _ { w } ) \frac { \gamma ( \rho P \tau _ { v } ) } { r ( \rho P \tau _ { v } ) } , } \\ { \gamma ( \rho P \tau ^ { w } ) = n \gamma ( \rho P \tau _ { v } ) \frac { \gamma ( \rho P \tau _ { w } ) } { r ( \rho P \tau _ { w } ) } . } \end{array}
$$

Due to $r ( \rho P \tau _ { v } ) + r ( \rho P \tau _ { w } ) = n$ , therefore

$$
\begin{array} { r c l } { { \displaystyle \frac { 1 } { \gamma ( \rho P \tau ^ { \upsilon } ) } + \frac { 1 } { \gamma ( \rho P \tau ^ { \upsilon } ) } ~ = ~ \frac { r ( \rho P \tau _ { \upsilon } ) } { n \gamma ( \rho P \tau _ { \upsilon } ) \gamma ( \rho P \tau _ { \upsilon } ) } + \frac { r ( \rho P \tau _ { w } ) } { n \gamma ( \rho P \tau _ { w } ) \gamma ( \rho P \tau _ { \upsilon } ) } } } \\ { { ~ } } & { { = ~ \frac { 1 } { \gamma ( \rho P \tau _ { w } ) \gamma ( \rho P \tau _ { v } ) } . } } \end{array}
$$

i.e., $1 ^ { \circ }$

Also has

$$
\begin{array} { r c l } { { \displaystyle \phi ( \rho P \tau ^ { v } ) } } & { { = } } & { { \displaystyle \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } \sum _ { i _ { w } = 1 } ^ { i _ { v } } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } } } \\ { { \displaystyle \phi ( \rho P \tau ^ { w } ) } } & { { = } } & { { \displaystyle \sum _ { i _ { w } = 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } \sum _ { i _ { v } = 1 } ^ { i _ { w } - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } , } } \end{array}
$$

where $\prod _ { 1 } ^ { i _ { v } } \left( \operatorname { r e s p . } \prod _ { 2 } ^ { i _ { w } } \right)$ is the product of all $\phi ( \rho P \tau ^ { v } )$ resp. $\phi ( \rho P \tau ^ { w } ) )$ , while

$$
\rho \lambda P \tau _ { a } = _ { a } [ \rho P \tau _ { b } ^ { 1 } , \cdot \cdot \cdot , \rho \lambda P \tau _ { b } ^ { m _ { 1 } } ] , \quad \rho \lambda P \tau _ { b } = _ { b } [ \rho \lambda P \tau _ { a } ^ { 1 } , \cdot \cdot \cdot , \rho \lambda P \tau _ { a } ^ { m _ { 2 } } ] ,
$$

and $i _ { v } , i _ { w }$ are labels of $v$ and $w$ respectively. $\prod _ { 1 } ^ { i _ { v } } \left( \operatorname { r e s p . } \prod _ { 2 } ^ { i _ { w } } \right)$ varies only according to $i _ { v }$ , (resp. $i _ { w . }$ ), therefore

$$
\phi ( \rho P \tau _ { v } ) = \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } , \quad \phi ( \rho P \tau _ { w } ) = \sum _ { i _ { w } = 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } ,
$$

then

$$
\begin{array} { r c l } { \displaystyle \phi ( \rho P \tau _ { v } ) \phi ( \rho P \tau _ { w } ) } & { = } & { \displaystyle \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } \sum _ { i _ { w } = 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } } \\ & { = } & { \displaystyle \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } \Big ( \sum _ { i _ { w } = 1 } ^ { i _ { v } } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } + \sum _ { i _ { w } = i _ { v } + 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } \Big ) } \\ & { = } & { \displaystyle \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } \sum _ { i _ { w } = 1 } ^ { i _ { v } } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } + \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } \sum _ { i _ { w } = i _ { v } + 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } . } \end{array}
$$

After manipulation, we can get

$$
\begin{array} { r l r } {  { \sum _ { i _ { v } = 1 } ^ { s - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } \sum _ { i _ { w } = i _ { v } + 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } \ = \ \sum _ { i _ { w } = 2 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } \sum _ { i _ { v } = 1 } ^ { i _ { w } - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } } } \\ & { } & { \ = \ \sum _ { i _ { w } = 1 } ^ { s } b _ { i _ { w } } \prod _ { 2 } ^ { i _ { w } } \sum _ { i _ { v } = 1 } ^ { i _ { w } - 1 } a _ { i _ { v } } \prod _ { 1 } ^ { i _ { v } } , \quad b _ { 1 } = 0 . } \end{array}
$$

From this, $2 ^ { \circ }$ holds.

Corollary 2.22. Let scheme (2.13) be at least $( p - 1 )$ -order, where $p \geq 2$ , then order conditions

$$
\phi ( \rho P \tau ^ { v } ) = \frac { 1 } { \gamma ( \rho P \tau ^ { v } ) }
$$

satisfies, iff

$$
\phi ( \rho P \tau ^ { w } ) = \frac { 1 } { \gamma ( \rho P \tau ^ { w } ) } .
$$

Proof. Because scheme (2.13) is at least $( p - 1 )$ -order, by Theorem 2.20, we know the following two relations hold:

$$
\phi ( \rho P \tau ^ { v } ) = { \frac { 1 } { \gamma ( \rho P \tau _ { v } ) } } , \quad \phi ( \rho P \tau ^ { w } ) = { \frac { 1 } { \gamma ( \rho P \tau _ { w } ) } } .
$$

By Theorem 2.21, we have

$$
\phi ( \rho P \tau ^ { v } ) + \phi ( \rho P \tau ^ { w } ) = \frac { 1 } { \gamma ( \rho P \tau ^ { v } ) } + \frac { 1 } { \gamma ( \rho P \tau ^ { w } ) } .
$$

The corollary is obviously established.

So far we draw the following conclusion for this section:

Theorem 2.23. [AS93,ZQ95b,SSC94] Symplectic scheme (2.13) $( a _ { s } = b _ { 1 } = 0 ) \quad$ ) is of $p$ - order, if and only if any of $P$ -tree $p \tau$ , $r ( p \tau ) \leq p$ there is a rooted $P$ -tree $\rho P \tau \in p \tau$ , such that

$$
\phi ( \rho P \tau ) = \frac { 1 } { \gamma ( \rho P \tau ) } .
$$

Proof. By Corollary 2.22, we know that any two kinds of rooted label method of the $P \tau$ lead to equivalent conditions. Therefore, we only need to take one of them to get the order conditions.

By Theorem 2.23, we simplify the order conditions. Originally, every rooted $P$ - tree has a corresponding order condition. Now every $P$ -tree, no matter how different the root is chosen, has a corresponding order condition. For the case of 4-order, the number of order conditions reduces from 16 to 8, and the corresponding 8 $P$ -trees are as follows:

![](images/31c617b6acdb2c028db322ead77be123d29783feab1845303dfb5fc60bf9c05d.jpg)  
Fig. 2.2. 8 P-trees

Finally, according to Theorem 2.23, we can simplify the order conditions for P–R–K method, which is given in Table 2.2. Calvo and Hairer[CH95] further reduce the number of independent condition in P–R–K method. See Table 2.3. For general Hamiltonian, the corresponding values are given by Table 2.4 which is obtained by Mirua[Mur97] .

Table 2.2. Order conditions P–R–K method and Symplectic P–R–K method for separable case   

<table><tr><td rowspan=1 colspan=1>Order</td><td rowspan=1 colspan=1>P-R-K method</td><td rowspan=1 colspan=1>Symplectic P-R-K method</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>8</td><td rowspan=6 colspan=1>5814244688</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>34</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>74</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>170</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>400</td></tr></table>

Table 2.3. Further reduction in Order conditions for P–R–K method in separable case   

<table><tr><td>Order</td><td>P-R-K method</td><td>Symp.P-R-K method</td><td>expl. Symp.P-R-K method</td></tr><tr><td>1</td><td>2</td><td>1</td><td>1</td></tr><tr><td>2</td><td>2</td><td>1</td><td>1</td></tr><tr><td>3</td><td>4</td><td>2</td><td>2</td></tr><tr><td>4</td><td>8</td><td>3</td><td>3</td></tr><tr><td>5</td><td>18</td><td>6</td><td>6</td></tr><tr><td>6</td><td>40</td><td>10</td><td>9</td></tr><tr><td>7</td><td>96</td><td>22</td><td>18</td></tr><tr><td>8</td><td>230</td><td>42</td><td>30</td></tr></table>

Table 2.4. Order conditions P–R–K method and Symplectic P–R–K method for general case   

<table><tr><td rowspan=1 colspan=1>Order</td><td rowspan=1 colspan=1>P-R-K method</td><td rowspan=1 colspan=1>Symplectic P-R-K method</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>52</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>214</td><td rowspan=4 colspan=1>27913501376</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>916</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>4116</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>18996</td></tr></table>

# 7.3 Symplectic R–K–N Method

Symplectic Runge–Kutta–Nystrom method is abbreviated as symplectic R–K–N method. ¨ The main purpose of this section is to develop and simplify the order conditions for R– $\mathrm { K } { - } \mathrm { N }$ methods, while the simplified order conditions for canonical R–K–N methods, which are applied to special kind of ODE’s, are also obtained here. Then, using the simplified order condition , we construct some 5 stage, fifth-order symplectic R–K–N schemes.

# 7.3.1 Order Conditions for Symplectic R–K–N Method

We consider a special kind of second order ODE’s:

$$
{ \ddot { y } } ^ { J } = f ^ { J } ( y ^ { 1 } , y ^ { 2 } , \cdot \cdot \cdot , y ^ { n } ) , \quad J = 1 , \cdot \cdot \cdot , n , \quad ( y ^ { 1 } , \cdot \cdot \cdot , y ^ { n } ) \in \mathbf { R } ^ { n } .
$$

We can transform (3.1) into a system of first order ODE’s

$$
\left[ \begin{array} { c } { \dot { y } } \\ { \ddot { y } } \end{array} \right] = \left[ \begin{array} { c } { \dot { y } } \\ { f ( y ) } \end{array} \right] ,
$$

by adding another group of variables $\dot { y } ^ { J } \left( J = 1 , \cdots , n \right)$ . Since canonical difference schemes are meaningful only to Hamiltonian systems, we assume that (3.2) can be written as

$$
\left[ \begin{array} { c c } { \dot { y } } \\ { \ddot { y } } \end{array} \right] = \left[ \begin{array} { c c } { \frac { \partial H ( y , \dot { y } ) } { \partial \dot { y } } } \\ { - \frac { \partial H ( y , \dot { y } ) } { \partial { y } } } \end{array} \right] ,
$$

where $H ( y , \dot { y } )$ is scalar function that satisfies

$$
\left\{ \begin{array} { l l } { \displaystyle \frac { \partial H ( y , \dot { y } ) } { \partial \dot { y } } = \dot { y } , } \\ { \displaystyle - \frac { \partial H ( y , \dot { y } ) } { \partial y } = f ( y ) . } \end{array} \right.
$$

So $H$ must be in the form $\begin{array} { r } { H = \frac 1 2 { \dot { y } } ^ { \mathrm { T } } { \dot { y } } - u ( y ) , \frac { \partial u } { \partial y } = f ( y ) \ } \end{array}$ . Therefore only when $f ( g )$ is a gradient of some scalar function, its symplectic algorithm is meaningful. A general $s$ -stage R–K–N method can be written as

$$
\left\{ \begin{array} { l l } { \displaystyle g _ { i } = y _ { 0 } + c _ { i } h { \dot { y } } _ { 0 } + h ^ { 2 } \sum _ { j = 1 } ^ { s } a _ { i j } f ( g _ { j } ) , \quad i = 1 , \cdots , n , } \\ { \displaystyle y _ { 1 } = y _ { 0 } + h { \dot { y } } _ { 0 } + h ^ { 2 } \sum _ { j = 1 } ^ { s } { \overline { { b _ { j } } } } f ( g _ { j } ) , } \\ { \displaystyle { \dot { y } } _ { 1 } = { \dot { y } } _ { 0 } + h \sum _ { j = 1 } ^ { s } b _ { j } f ( g _ { j } ) . } \end{array} \right.
$$

The corresponding Butcher tableau is

$$
\begin{array} { r } { \frac { c _ { 1 } } { c _ { 2 } } ~ \left| \begin{array} { l l l } { a _ { 1 1 } } & { \cdots } & { a _ { 1 s } } \\ { a _ { 2 1 } } & { \cdots } & { a _ { 2 s } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { a _ { s 1 } } & { \cdots } & { a _ { s s } } \\ { \overline { { b _ { 1 } } } } & { \cdots } & { \overline { { b _ { s } } } } \\ { b _ { 1 } } & { \cdots } & { b _ { s } } \end{array} \right| } \end{array}
$$

Theorem 3.1. If the coefficients of scheme (3.4) satisfy

$$
\begin{array} { r l r } & { \overline { { b _ { j } } } = b _ { j } \big ( 1 - c _ { j } \big ) , } & { 1 \leq j \leq s , } \\ & { b _ { i } a _ { i j } - b _ { j } a _ { j i } + \overline { { b } } _ { i } b _ { j } - b _ { i } \overline { { b } } _ { j } = 0 , } & { 1 \leq i , j \leq s , } \end{array}
$$

then scheme is symplectic[Sur90,Sur89,CS93,ZQ93] .

Proof. The proof of Theorem 3.1 can be find in $[ \mathrm { S u r 8 9 } , \mathrm { O S 9 2 } ]$ . Here, we only point out that under conditions (3.5), (3.6) are equivalent to

$$
b _ { i } a _ { i j } - b _ { j } a _ { j i } + b _ { i } b _ { j } ( c _ { j } - c _ { i } ) = 0 , \quad 1 \leq i , j \leq s .
$$

Therefore, the theorem is completed.

Similar to Section 7.1, we first introduce some necessary definitions and notations, and then derive order conditions. Some definitions of Section 7.1 can still be used. Here we only introduce some special definitions and notations.

(1) $S$ -graph. A $S$ -graph, denoted as $S { - } g$ , is a special $P$ -graph where any two adjacent vertices belong to different categories: “ white (meagre)” or “ black (fat)”. The Labeled $S$ -graph has a definition similar to the labeled $P$ -graph.

(2) $S$ -tree. A $S$ -tree, denoted as $S \tau$ , has a definition similar to the $P$ -tree of 7.2: replacing the $P$ -graph in the definition of original $P$ -tree with $S$ -graph gives the definition of $S$ -tree. The definition of labeled $S$ - tree, $\lambda S \tau$ , rooted $S$ -tree, $\rho S \tau$ , rooted labeled $S$ -tree, $\rho \lambda S \tau$ , and isomorphic labeled $S$ -trees, root-isomorphic labeled $S$ -tree are defined using the same method as we have used to define $P$ -trees, labeled $P$ -trees, etc. We should point out that in this section, we just consider $S$ -trees with “ black” root vertices. So when we refer to rooted $S$ -tree, we mean that its $S$ -tree has a “ black” root. Moreover, order $r$ , density $\gamma$ also has similar definition as mentioned in Section 7.1. But the elementary weight definition is completely different, which we will redefine subsequently.

Definition 3.2. We define the elementary weight $\phi ( \rho \lambda S \tau )$ corresponding to a rooted labeled $S$ -tree. At first, for convenience, we assume $\rho \lambda S \tau$ is monotonically labeled. Later, we will see this is unnecessary. In the remainder of this section, without specification, the labels of the vertices are always $j < k < l < m < \cdots$ . For a monotonic labeling, the label of the root is $j$ . Then $\phi ( \rho \lambda S \tau )$ is a sum over the labels of all fat vertices of $\rho \lambda s \tau$ , the general term of the sum is a product of

$1 ^ { \circ }$ $b _ { j }$ ( $j$ is a rooted vertex). $2 ^ { \circ }$ $a _ { k l }$ , if the fat vertex $k$ is connected via a meagre son with another fat vertex $l$ . $3 ^ { \circ }$ $c _ { k } ^ { m }$ , if the fat vertex $k$ has $m$ meagre end-vertices as its sons, where an endvertex is the vertex which has no son.

We see that, for two different rooted labeled $S$ -trees: $\rho \lambda S \tau ^ { 1 }$ and $\rho \lambda S \tau ^ { 2 }$ , we have $\phi ( \rho \lambda S \tau ^ { 1 } ) = \phi ( \rho \lambda S \tau ^ { 2 } )$ . Thus, the choosing of the monotonic labeling is unnecessary.

For example, for k• $\begin{array} { c } { { \bullet } } \\ { { k ^ { \bullet } \bullet \bullet ^ { \bullet } } } \\ { { \rho \lambda S \tau ^ { 1 } } } \end{array}$ and $\begin{array} { c } { { m \pmb { \mathscr { Q } } ^ { j } } _ { k } } \\ { { \rho \lambda S \tau ^ { 2 } } } \end{array}$ , we have $\phi ( \rho \lambda S \tau ^ { 1 } ) = \sum _ { j , m } b _ { j } c _ { j } a _ { j m } = \sum _ { j , k } b _ { k } a _ { k j } c _ { k } = \phi ( \rho \lambda S \tau ^ { 2 } ) = \phi ( \rho S \tau ) .$

Because $\rho \lambda S \tau ^ { 1 }$ and $\rho \lambda S \tau ^ { 2 }$ are rooted isomorphism, they belong to a rooted tree $\rho S \tau$

+ . Therefore, they form an equivalence class. The following theorem can be seen in the literature [HNW93] . We omit the proof here.

Theorem 3.3. P-K-N method (3.4) is order of p iff:

$$
\phi ^ { \prime } ( \rho S \tau ) = \frac { 1 } { \gamma ( \rho S \tau ) ( r ( \rho S \tau ) + 1 ) } , f o r r o o t e d S \ – t r e e \rho \lambda S \tau , r ( \rho S \tau ) \le ( p - 1 ) .
$$

The explanation for $\phi ^ { \prime } ( \rho S \tau )$ is similar to that of $\phi ( \rho S \tau )$ , which only needs to substitute $b _ { j }$ in $\phi ( \rho S \tau )$ (suppose $j$ is the label of rooted tree, corresponding to a certain label choosing) by $\bar { b } _ { j }$ . Because $\phi$ and $\phi ^ { \prime }$ is independent of the chosen label, (3.8) and (3.9) can take any of the labels to calculate.

We find that (3.8) and (3.9) are not independent under symplectic conditions.

Theorem 3.4. Under symplectic condition (3.5), order condition (3.8) implies condition (3.9)[ZQ95b] .

Proof. Let $\rho S \tau$ be $\leq p - 1$ order $S$ -tree, and let $\rho S u$ be such a rooted $S$ -tree with $r ( \rho S \tau ) + 1$ order that is obtained from $\rho S \tau$ rooted tree by attaching a new branch with a meagre vertex to the root of $\tau$ . Therefore from definition of $\phi$ , we have

$$
\phi ( \rho S u ) = \sum _ { j } b _ { j } c _ { j } \sum \prod , \quad \phi ( \rho S \tau ) = \sum _ { j } b _ { j } \sum \prod ,
$$

where we assume that $\rho S \tau$ and $\rho S u$ have monotonic labels $j < k < l < \cdots$ Then for $\rho S u$ , apart from the added root of the meagre leaf node, the remaining vertices have the same labeling as $\rho S \tau$ , and $\displaystyle \sum$ is a sum for all non-fat root vertices, and $\prod$ is a product of $a _ { i j }$ and $c _ { i }$ that are contained in $\rho S \tau$ and $\rho S u$ . From the definition of $\phi$ , we have

$$
\gamma ( \rho S u ) = \frac { ( r ( \rho S \tau ) + 1 ) \gamma ( \rho S \tau ) } { r ( \rho S \tau ) } ,
$$

therefore,

$$
\begin{array} { l } { \phi ^ { \prime } ( \rho S \tau ) ~ = ~ \displaystyle \sum _ { j } \bar { b } _ { j } \sum \prod = \displaystyle \sum _ { j } b _ { j } ( 1 - c _ { j } ) \sum \prod } \\ { ~ = ~ \displaystyle \sum _ { j } b _ { j } \sum \prod - \displaystyle \sum _ { j } b _ { j } c _ { j } \sum \prod = \phi ( \rho S \tau ) - \phi ( \rho S u ) } \\ { ~ = ~ \displaystyle \frac { 1 } { \gamma ( \rho S \tau ) } - \frac { 1 } { \gamma ( \rho S u ) } = \frac { 1 } { ( r ( \rho S \tau ) + 1 ) \gamma ( \rho S \tau ) } . } \end{array}
$$

Since the formula(3.8) is held for $\leq \textit { p }$ -order $S$ -tree and (3.9) is held only for $\leq p - 1$ -order $S$ -tree, the order of the tree obtained by adding a leaf node to any $\leq p - 1$ -order tree on the root must be $\leq p$ and (3.8) must be satisfied. Therefore the final equal sign in (3.10) holds. Thus we reach the conclusion of this section. -

Theorem 3.5. R–K–N method (3.4) is symplectic, and is of $p$ -order iff:

$$
\begin{array} { r l r } & { b _ { i } a _ { i j } - b _ { j } a _ { j i } + b _ { i } b _ { j } ( c _ { j } - c _ { i } ) = 0 , } & { 1 \leq i , j \leq s , } \\ & { \bar { b } _ { i } = b _ { i } ( 1 - c _ { i } ) , } & { 1 \leq i \leq s , } \\ & { \phi ( \rho S \tau ) = \displaystyle \frac { 1 } { \gamma ( \rho S \tau ) } } & { f o r r o o t e d S \ – t r e e \rho S \tau , \ r ( \rho S \tau ) \leq p . } \end{array}
$$

Note that the conditions we have given here are necessary and sufficient. However some conditions of (3.13) are still redundant, which means some conditions are mutually equivalent. We will see more details about this in Section 7.4.

# 7.3.2 The 3-Stage and 4-th order Symplectic R–K–N Method

For convenience, we construct only explicit schemes here[QZ91] . Suppose the parameters $a _ { i j }$ of a $\mathrm { R - K - N }$ method to be a matrix $A$

$$
A = \left[ \begin{array} { c c c c c } { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s , s - 1 } } & { 0 } \end{array} \right] .
$$

By the symmetry of Equations (3.11) in Theorem 3.5, we have

$$
b _ { i } a _ { i j } - b _ { j } a _ { j i } + b _ { i } b _ { j } ( c _ { j } - c _ { i } ) = 0 \Longleftrightarrow b _ { j } a _ { j i } - b _ { i } a _ { i j } + b _ { j } b _ { i } ( c _ { i } - c _ { j } ) = 0 ,
$$

hence Equations (3.11) can be simplified into

$$
b _ { i } a _ { i j } - b _ { j } a _ { j i } + b _ { i } b _ { j } ( c _ { j } - c _ { i } ) = 0 , \quad 1 \leq j < i \leq s .
$$

Since when $j < i , a _ { j i } = 0$ , the above formula can be written as

$$
b _ { i } a _ { i j } + b _ { i } b _ { j } ( c _ { j } - c _ { i } ) = 0 , \quad 1 \leq j < i \leq s .
$$

For conditions of 3-stage of 3rd-order R–K–N method, we get equations for parameters :

$$
\left\{ \begin{array} { l l } { b _ { 2 } a _ { 2 1 } + b _ { 2 } b _ { 1 } ( c _ { 1 } - c _ { 2 } ) = 0 , } \\ { b _ { 3 } a _ { 3 1 } + b _ { 3 } b _ { 1 } ( c _ { 1 } - c _ { 3 } ) = 0 , } \\ { b _ { 3 } a _ { 3 2 } + b _ { 3 } b _ { 2 } ( c _ { 2 } - c _ { 3 } ) = 0 , } \\ { b _ { 1 } + b _ { 2 } + b _ { 3 } = 1 , } \\ { b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \frac { 1 } { 2 } , } \\ { b _ { 1 } c _ { 1 } ^ { 2 } + b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } = \frac { 1 } { 3 } , } \\ { b _ { 2 } a _ { 2 1 } + b _ { 3 } a _ { 3 1 } + b _ { 3 } a _ { 3 2 } = \frac { 1 } { 6 } , } \end{array} \right.
$$

and

$$
\overline { { b _ { i } } } = b _ { i } ( 1 - c _ { i } ) , \quad i = 1 , 2 , 3 .
$$

Direct verification shows

$$
\begin{array} { l } { { A = \left[ \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 0 } } \\ { { { \displaystyle { \frac { 7 } { 3 6 } } } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - { \displaystyle { \frac { 1 } { 2 } } } } } & { { 0 } } \end{array} \right] , } } \\ { { b _ { 1 } = { \displaystyle { \frac { 7 } { 2 4 } } } , \quad b _ { 2 } = { \displaystyle { \frac { 3 } { 4 } } } , \quad b _ { 3 } = - { \displaystyle { \frac { 1 } { 2 4 } } } , \quad c _ { 1 } = c _ { 3 } = 0 , \quad c _ { 2 } = { \displaystyle { \frac { 2 } { 3 } } } } } \end{array}
$$

is a set of solutions for system (3.14).

The number of order conditions becomes 7 for a scheme of order 4. In addition, if the scheme is of 3-stage, there are 3 equations for canonicity. Therefore we have a total of 10 equations with 9 unknown variables (systems (3.14) plus parameters ${ \bar { b } } _ { i }$ $( i = 1 , 2 , 3 )$ ). So we first construct a 4-stage scheme of 4th order, which requires 13 equations with 14 variables:

A 3-stage symplectic scheme needs to satisfy the following 6 conditions

$$
\begin{array} { l } { { b _ { 2 } a _ { 2 1 } + b _ { 2 } b _ { 1 } ( c _ { 1 } - c _ { 2 } ) = 0 , } } \\ { { b _ { 3 } a _ { 3 1 } + b _ { 3 } b _ { 1 } ( c _ { 1 } - c _ { 3 } ) = 0 , } } \\ { { b _ { 3 } a _ { 3 2 } + b _ { 3 } b _ { 2 } ( c _ { 2 } - c _ { 3 } ) = 0 , } } \\ { { b _ { 4 } a _ { 4 1 } + b _ { 4 } b _ { 1 } ( c _ { 1 } - c _ { 4 } ) = 0 , } } \\ { { b _ { 4 } a _ { 4 2 } + b _ { 4 } b _ { 2 } ( c _ { 2 } - c _ { 4 } ) = 0 , } } \\ { { b _ { 4 } a _ { 4 3 } + b _ { 4 } b _ { 3 } ( c _ { 3 } - c _ { 4 } ) = 0 , } } \end{array}
$$

and equations that satisfy 4th-order conditions are as follows:

$$
\begin{array} { r l } & { b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } \\ & { b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } + b _ { 4 } c _ { 4 } = \frac { 1 } { 2 } , } \\ & { b _ { 1 } c _ { 1 } ^ { 2 } + b _ { 2 } c _ { 2 } ^ { 2 } + b _ { 3 } c _ { 3 } ^ { 2 } + b _ { 4 } c _ { 4 } ^ { 2 } = \frac { 1 } { 3 } , } \\ & { b _ { 2 } a _ { 2 1 } + b _ { 3 } a _ { 3 1 } + b _ { 3 } a _ { 3 2 } + b _ { 4 } a _ { 4 1 } + b _ { 4 } a _ { 4 2 } + b _ { 4 } a _ { 4 3 } = \frac { 1 } { 6 } , } \\ & { b _ { 1 } c _ { 1 } ^ { 3 } + b _ { 2 } c _ { 2 } ^ { 3 } + b _ { 3 } c _ { 3 } ^ { 3 } + b _ { 4 } c _ { 4 } ^ { 3 } = \frac { 1 } { 4 } , } \\ & { b _ { 2 } c _ { 2 } a _ { 2 1 } + b _ { 3 } c _ { 3 } a _ { 3 1 } + b _ { 3 } c _ { 3 } a _ { 3 2 } + b _ { 4 } c _ { 4 } a _ { 4 1 } + b _ { 4 } c _ { 4 } a _ { 4 2 } + b _ { 4 } c _ { 4 } a _ { 4 3 } = \frac { 1 } { 8 } , } \\ & { b _ { 2 } a _ { 2 1 } c _ { 1 } + b _ { 3 } a _ { 3 1 } c _ { 1 } + b _ { 3 } a _ { 3 2 } c _ { 2 } + b _ { 4 } a _ { 4 1 } c _ { 1 } + b _ { 4 } a _ { 4 2 } c _ { 2 } + b _ { 4 } a _ { 4 3 } c _ { 3 } = \frac { 1 } { 2 4 } . } \end{array}
$$

Set $c _ { 4 } = 0$ , we have

$$
\begin{array} { r l } & { b _ { 2 } a _ { 2 1 } + b _ { 2 } b _ { 1 } ( c _ { 1 } - c _ { 2 } ) = 0 , } \\ & { b _ { 3 } a _ { 3 1 } + b _ { 3 } b _ { 1 } ( c _ { 1 } - c _ { 3 } ) = 0 , } \\ & { b _ { 3 } a _ { 3 2 } + b _ { 3 } b _ { 2 } ( c _ { 2 } - c _ { 3 } ) = 0 , } \\ & { b _ { 4 } a _ { 4 1 } + b _ { 4 } b _ { 1 } c _ { 1 } = 0 , } \end{array}
$$

$$
\begin{array} { r l } & { \gamma _ { 1 } ^ { \mathrm { o f } } 4 ^ { \mathrm { o f } } 4 ^ { \mathrm { o f } } 2 ^ { \mathrm { o f } } 2 ^ { \mathrm { o f } } 2 = 0 , } \\ & { \beta _ { 1 } 4 ^ { \mathrm { o f } } 4 6 _ { 3 } + \beta _ { 1 } \hbar ^ { \mathrm { o f } } 8 0 = 0 , } \\ & { \hbar _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = 1 , } \\ & { b _ { 1 } c _ { 1 } + b _ { 2 } c _ { 2 } + b _ { 3 } c _ { 3 } = \frac { 1 } { 2 } , } \\ & { b _ { 1 } c _ { 1 } ^ { \mathrm { o f } } + b _ { 2 } c _ { 2 } ^ { \mathrm { o f } } + b _ { 3 } c _ { 3 } ^ { \mathrm { o f } } = \frac { 1 } { 3 } , } \\ & { b _ { 2 } c _ { 2 } ^ { \mathrm { o f } } 1 + b _ { 3 } c _ { 3 } ^ { \mathrm { o f } } 3 + b _ { 3 } c _ { 3 } ^ { \mathrm { o f } } = \frac { 1 } { 3 } , } \\ & { b _ { 2 } c _ { 3 } + b _ { 3 } c _ { 3 } ( 1 + b _ { 3 } c _ { 3 } + 1 ) c _ { 4 } \alpha _ { 1 1 } + b _ { 4 } \alpha _ { 2 2 } + b _ { 4 } \alpha _ { 5 3 } = \frac { 1 } { 6 } , } \\ & { b _ { 1 } c _ { 1 } ^ { \mathrm { o f } } 4 ^ { \mathrm { o f } } 6 2 c _ { 2 } ^ { \mathrm { o f } } + b _ { 6 } c _ { 3 } ^ { \mathrm { o f } } = \frac { 1 } { 4 } , } \\ & { b _ { 2 } c _ { 2 } \alpha _ { 2 1 } + b _ { 4 } c _ { 3 } \alpha _ { 1 1 } + b _ { 5 } c _ { 4 } \alpha _ { 2 2 } - \frac { 1 } { 8 } , } \\ & { b _ { 2 } c _ { 2 } \alpha _ { 2 1 } + b _ { 3 } c _ { 3 } \alpha _ { 1 2 } + b _ { 3 } c _ { 3 } \alpha _ { 2 2 } + b _ { 4 } \alpha _ { 1 1 } c _ { 1 } + b _ { 4 } \alpha _ { 2 2 } c _ { 2 } + b _ { 4 } \alpha _ { 1 3 } c _ { 3 } = \frac { 1 } { 2 4 } . } \end{array}
$$

We obtain a set of numerical solutions of $( 3 . 1 6 ) - ( 3 . 2 8 )$

$$
\begin{array} { r l r l } & { a _ { 2 1 } = 0 . 2 2 3 2 8 9 6 \mathrm { E } - 0 1 , } & & { a _ { 3 1 } = 0 . 2 8 2 2 9 7 7 \mathrm { E } - 0 8 , } \\ & { a _ { 3 2 } = 0 . 2 8 8 6 7 5 3 , } & & { a _ { 4 1 } = 0 . 3 0 5 3 7 8 9 \mathrm { E } - 0 1 , } \\ & { a _ { 4 2 } = - 0 . 1 0 5 7 3 4 2 , } & & { a _ { 4 3 } = - 0 . 4 2 5 1 1 3 7 , } \\ & { b _ { 1 } = - 0 . 3 8 6 7 4 9 1 \mathrm { E } - 0 1 , } & & { b _ { 2 } = 0 . 5 0 0 0 0 3 , } \\ & { b _ { 3 } = 0 . 5 3 8 6 7 4 6 , } & & { b _ { 4 } = - 0 . 9 1 2 9 7 6 7 \mathrm { E } - 0 7 , } \\ & { c _ { 1 } = 0 . 7 8 8 6 7 5 3 , } & & { c _ { 2 } = 0 . 2 1 1 3 2 4 9 , } \\ & { c _ { 3 } = 0 . 7 8 8 6 7 5 2 . } \end{array}
$$

Guessing from these numerical solutions, we obtain

$$
a _ { 3 1 } = 0 , \quad b _ { 2 } = \frac { 1 } { 2 } , \quad b _ { 3 } = \frac { 1 } { 2 } - b _ { 1 } , \quad b _ { 4 } = 0 , \quad c _ { 1 } = c _ { 3 } , \quad c _ { 2 } = 1 - c _ { 1 } .
$$

Inserting them into (3.16) – (3.28), we have

$$
\begin{array} { r l } & { \mathfrak { h } \iff \omega _ { 2 1 } + b _ { 1 } ( 2 \mathfrak { c } _ { 1 } - 1 ) = 0 , } \\ & { \circ ) \iff 0 = 0 , } \\ & { \emptyset \iff \left( \frac { 1 } { 2 } - b _ { 1 } \right) a _ { 3 2 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) \frac { 1 } { 2 } ( 1 - 2 \mathfrak { c } _ { 1 } ) = 0 , } \\ & { \emptyset , ( 3 2 0 ) , ( 3 2 2 ) , ( 3 . 3 2 2 ) , ( 3 . 2 3 ) \iff 0 = 0 , \quad \mathrm { o r } \quad 1 = 1 , } \\ & { \emptyset \implies \frac { 1 } { 2 } c _ { 1 } ^ { \circ } + \frac { 1 } { 2 } ( 1 - \mathfrak { c } _ { 1 } ) ^ { 2 } = \frac { 1 } { 3 } , } \\ & { \emptyset \implies \frac { 1 } { 2 } a _ { 2 1 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) a _ { 3 2 } = \frac { 1 } { 6 } , } \\ & { \emptyset \implies c _ { 1 } ^ { \circ } - \mathrm { c } _ { 1 } + \frac { 1 } { 6 } = 0 , } \\ & { \emptyset \implies \frac { 1 } { 2 } ( 1 - \mathfrak { c } _ { 1 } ) a _ { 2 1 } + \mathrm { c } _ { 1 } a _ { 3 2 } \left( \frac { 1 } { 2 } - b _ { 1 } \right) = \frac { 1 } { 8 } , } \\ & { \emptyset \implies \frac { 1 } { 2 } a _ { 2 1 } c _ { 1 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) a _ { 3 2 } ( 1 - \mathfrak { c } _ { 1 } ) = \frac { 1 } { 2 4 } . } \end{array}
$$


<!-- chunk 0006: pages 351-420 -->
So we obtain a system of equations of the variables $a _ { 2 1 } , a _ { 3 2 } , b _ { 1 } , c _ { 1 }$

$$
\begin{array} { l } { { a _ { 2 1 } + b _ { 1 } ( 2 c _ { 1 } - 1 ) = 0 , } } \\ { { \left( \frac { 1 } { 2 } - b _ { 1 } \right) a _ { 3 2 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) \frac { 1 } { 2 } ( 1 - 2 c _ { 1 } ) = 0 , } } \\ { { \frac { 1 } { 2 } c _ { 1 } ^ { 2 } + \frac { 1 } { 2 } ( 1 - c _ { 1 } ) ^ { 2 } = \frac { 1 } { 3 } , } } \\ { { \frac { 1 } { 2 } a _ { 2 1 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) a _ { 3 2 } = \frac { 1 } { 6 } , } } \\ { { \frac { 1 } { 2 } ( 1 - c _ { 1 } ) a _ { 2 1 } + c _ { 1 } a _ { 3 1 } \left( \frac { 1 } { 2 } - b _ { 1 } \right) = \frac { 1 } { 8 } , } } \\ { { \frac { 1 } { 2 } a _ { 2 1 } c _ { 1 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) a _ { 3 2 } ( 1 - c _ { 1 } ) = \frac { 1 } { 2 4 } . } } \end{array}
$$

From (3.31), we have $c _ { 1 } ^ { 2 } - c _ { 1 } + \frac { 1 } { 6 } = 0$ , which leads to $c _ { 1 } = { \frac { 3 + { \sqrt { 3 } } } { 6 } }$  or $c _ { 1 } = { \frac { 3 - { \sqrt { 3 } } } { 6 } } \bigg )$ . Suppose $b _ { 1 } \neq \frac 1 2$ , from (3.30) we obtain

$$
a _ { 3 2 } = \frac 1 2 ( 2 c _ { 1 } - 1 ) ,
$$

$a _ { 3 2 } = { \frac { \sqrt { 3 } } { 6 } } ($ $a _ { 3 2 } = - { \frac { \sqrt { 3 } } { 6 } } )$

$$
\frac { 1 } { 2 } a _ { 2 1 } + \left( \frac { 1 } { 2 } - b _ { 1 } \right) \times \frac { 1 } { 2 } ( 2 c _ { 1 } - 1 ) = \frac { 1 } { 6 } .
$$

Adding (3.36) and (3.29) together, we find

$$
2 a _ { 2 1 } = { \frac { 1 } { 3 } } - { \frac { 1 } { 2 } } ( 2 c _ { 1 } - 1 ) , \quad \mathrm { i . e . , } \quad a _ { 2 1 } = { \frac { 2 - { \sqrt { 3 } } } { 1 2 } } \quad \left( \mathrm { o r } \quad { \frac { 2 + { \sqrt { 3 } } } { 1 2 } } \right) .
$$

From (3.29), we obtain $b _ { 1 } = \frac { 3 - 2 \sqrt { 3 } } { 1 2 } \bigg ( \mathrm { o r } \frac { 3 + 2 \sqrt { 3 } } { 1 2 } \bigg )$ Therefore, we have reason to speculate that

$$
a _ { 2 1 } = { \frac { 2 - { \sqrt { 3 } } } { 1 2 } } , \quad a _ { 3 2 } = { \frac { \sqrt { 3 } } { 6 } } , \quad b _ { 1 } = { \frac { 3 - 2 { \sqrt { 3 } } } { 1 2 } } , \quad c _ { 1 } = { \frac { 3 + { \sqrt { 3 } } } { 6 } }
$$

and

$$
a _ { 2 1 } = { \frac { 2 + { \sqrt { 3 } } } { 1 2 } } , \quad a _ { 3 2 } = - { \frac { \sqrt { 3 } } { 6 } } , \quad b _ { 1 } = { \frac { 3 + 2 { \sqrt { 3 } } } { 1 2 } } , \quad c _ { 1 } = { \frac { 3 - { \sqrt { 3 } } } { 6 } }
$$

are two sets of solutions of $( 3 . 2 9 ) - ( 3 . 3 4 )$ . Direct verification shows that they are indeed solutions of the equations of (3.16) – (3.28). Thus we obtain two sets of analytic solutions of the original equations of system (3.16) – (3.28).

Solution 1 ${ \mathrm { : } } \quad a _ { 2 1 } = { \frac { 2 - { \sqrt { 3 } } } { 1 2 } } , \ a _ { 3 1 } = 0 , \ a _ { 3 2 } = { \frac { \sqrt { 3 } } { 6 } } , \ a _ { 4 1 } , \ a _ { 4 2 } , \ a _ { 4 3 } { \mathrm { ~ a r b i t r a r y } } .$

$$
\begin{array} { l l l } { { b _ { 1 } = \displaystyle \frac { 3 - 2 \sqrt { 3 } } { 1 2 } , \quad } } & { { b _ { 2 } = \displaystyle \frac { 1 } { 2 } , \quad } } & { { b _ { 3 } = \displaystyle \frac { 3 + 2 \sqrt { 3 } } { 1 2 } , \quad } } & { { b _ { 4 } = 0 , } } \\ { { c _ { 1 } = \displaystyle \frac { 3 + \sqrt { 3 } } { 6 } , \quad } } & { { c _ { 2 } = \displaystyle \frac { 3 - \sqrt { 3 } } { 6 } , \quad } } & { { c _ { 3 } = \displaystyle \frac { 3 + \sqrt { 3 } } { 6 } , \quad } } & { { c _ { 4 } = 0 . } } \end{array}
$$

Solution 2: $a _ { 2 1 } = \frac { 2 + \sqrt { 3 } } { 1 2 }$ , a31 = 0, a32 = √3 6 $a _ { 4 1 }$ , $a _ { 4 2 }$ , $a _ { 3 2 }$ arbitrary.

$$
\begin{array} { l l l l } { { b _ { 1 } = { \frac { 3 + 2 \sqrt { 3 } } { 1 2 } } , } } & { { \quad b _ { 2 } = { \frac { 1 } { 2 } } , } } & { { \quad b _ { 3 } = { \frac { 3 - 2 \sqrt { 3 } } { 1 2 } } , } } & { { \quad b _ { 4 } = 0 , } } \\ { { c _ { 1 } = { \frac { 3 - \sqrt { 3 } } { 6 } } , } } & { { \quad c _ { 2 } = { \frac { 3 + \sqrt { 3 } } { 6 } } , } } & { { \quad c _ { 3 } = { \frac { 3 - \sqrt { 3 } } { 6 } } , } } & { { \quad c _ { 4 } = 0 . } } \end{array}
$$

Since $b _ { 4 } = c _ { 4 } = 0$ , and $\bar { b } _ { 4 } = b _ { 4 } ( 1 - c _ { 4 } ) = 0$ in the two solutions, we obtain two 3-stage symplectic explicit R–K–N method of order 4. They are

<table><tr><td colspan="2">Scheme1: Ci</td><td colspan="2"></td></tr><tr><td>3+√3</td><td colspan="3">aij</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3-√3 6</td><td>2-√3</td><td>0</td><td>0</td></tr><tr><td>3+√3</td><td>12</td><td>V</td><td>0</td></tr><tr><td>6</td><td>0</td><td>6</td><td></td></tr><tr><td>bi</td><td>5-3√3 24</td><td>3+√3 12</td><td>1+√3</td></tr><tr><td rowspan="3">bi Scheme 2:</td><td>3-2√3</td><td></td><td>24 3+2√3</td></tr><tr><td>12</td><td>1</td><td>12</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Ci</td><td></td><td>aij</td><td></td></tr><tr><td>3-√3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>6 3+√3</td><td></td><td></td><td></td></tr><tr><td>6</td><td>2+√3 12</td><td>0</td><td>0</td></tr><tr><td>3-√3</td><td></td><td>V3</td><td></td></tr><tr><td>6</td><td>0</td><td>6</td><td>0</td></tr><tr><td>bi</td><td>5+3√3</td><td>3-√3</td><td>1-√3</td></tr><tr><td rowspan="2">bi</td><td>24 3+2√3</td><td>12</td><td>24 3-2√3</td></tr><tr><td>12</td><td>1</td><td>12</td></tr></table>

Remark 3.6. We can obtain the required solutions easily by solving only the first 6 equations from the simplified order conditions of symplectic R–K–N.

# 7.3.3 Symplified Order Conditions for Symplectic R–K–N Method

In subsection 7.3.1, we have a preliminary briefing of symplified order conditions for the symplectic R–K–N methods. In this section, we will simplify them further. The key is to make full use of symplectic conditions [ZQ95b] .

Let $S \tau$ be an $S$ -tree of order $n \geq 3$ . It has at least two fat vertices. Let $\lambda S \tau$ be a labeling. Let $v$ and $w$ be two fat vertices connected via a meagre vertex $u$ . For order $\leq ~ 2$ $S$ -tree, the root $S$ -trees contains only one the first-order and one the secondorder. Therefore there are no such issues that the order conditions for the trees with the same order are related to each other. We consider six rooted $S$ -trees. Let us denote $\rho S \tau ^ { v }$ (resp. $\rho S \tau ^ { w } )$ ) as the rooted $S$ -tree obtained by regarding the vertex $v$ (resp. $w$ ) as the root of $S \tau$ . Let us denote $\rho S \tau ^ { v u }$ (resp. $\rho S \tau ^ { w u } )$ as the rooted $S$ -tree with root $v$ (resp. $w$ ) that arises when the edge $( u , w ) ( \mathbf { r e s p . } ( v , u ) )$ is deleted from $s \tau$ . Let us denote $\rho S \tau _ { v }$ and $\rho S \tau _ { w }$ as the rooted $S$ -tree with root $v$ and $w$ respectively which arise when edges, $( u , v )$ and $( u , w )$ are deleted from $S \tau$ . Fig. 3.1 shows the rooted trees of Theorem 3.7.

![](images/fe3fc3ad6808d838839c2503a7e2f32624013bacb4ccd5d5fe0a6b283446c2a3.jpg)  
Fig. 3.1. Rooted $S$ -trees

Theorem 3.7. With the above notations, we have:

$$
1 ^ { \circ } \quad \frac { 1 } { \gamma ( \rho S \tau ^ { \circ } ) } - \frac { 1 } { \gamma ( \rho S \tau ^ { w } ) } = \frac { 1 } { \gamma ( \rho S \tau ^ { v u } ) \gamma ( \rho S \tau _ { w } ) } - \frac { 1 } { \gamma ( \rho S \tau ^ { w u } ) \gamma ( \rho S \tau _ { v } ) } .
$$

And if the R–K–N method (3.4) satisfies (3.7), then,

$$
\begin{array} { r l } { { 2 ^ { \circ } } } & { \phi ( \rho S \tau ^ { v } ) - \phi ( \rho S \tau ^ { w } ) = \phi ( \rho S \tau ^ { v u } ) \phi ( \rho S \tau _ { w } ) - \phi ( \rho S \tau ^ { w u } ) \phi ( \rho S \tau _ { v } ) . } \end{array}
$$

Proof. Let

$$
r ( \rho S \tau _ { v } ) = x , \quad r ( \rho S \tau _ { w } ) = \dot { y } , \quad n = r ( S \tau ) = x + y + 1 .
$$

By definition of $\gamma$ , we have

$$
\begin{array} { l } { { \gamma ( \rho S \tau ^ { v } ) = n \prod _ { 1 } ( x + 1 ) \gamma ( \rho S \tau _ { w } ) , } } \\ { { \gamma ( \rho S \tau ^ { w } ) = n \prod _ { 2 } ( y + 1 ) \gamma ( \rho S \tau _ { v } ) , } } \end{array}
$$

where $\prod _ { 1 } \left( \prod _ { 2 } \right)$ denotes the product of $\gamma ( \tau _ { 1 } ) ( \gamma ( \tau _ { 2 } ) )$ of the sub-trees, $\tau _ { i }$ which arise when $v$ (resp. $w$ ) is chopped from $\rho S \tau _ { v }$ (resp. $\rho S \tau _ { w }$ ). Notice that $\gamma$ is calculated as

the general tree $\tau$ , with the difference between the black and white vertices neglected. Then from (3.37), we have

$$
{ \frac { 1 } { \gamma ( \rho S \tau ^ { v } ) } } - { \frac { 1 } { \gamma ( \rho S \tau ^ { w } ) } } = { \frac { n } { n } } \left( { \frac { { 2 ( y + 1 ) \gamma ( \rho S \tau _ { v } ) } - { _ { 1 } ( x + 1 ) \gamma ( \rho S \tau _ { w } ) } } { { _ { 1 } ( x + 1 ) \gamma ( \rho S \tau _ { v } ) } _ { 2 } ( y + 1 ) \gamma ( \rho S \tau _ { w } ) } } \right) .
$$

Because

$$
\gamma ( \rho S \tau ^ { v u } ) = ( x + 1 ) \prod _ { 1 } , \gamma ( \rho S \tau ^ { w u } ) = ( y + 1 ) \prod _ { 2 } ,
$$

and

$$
\gamma ( \rho S \tau _ { v } ) = x \prod _ { 1 } , \gamma ( \rho S \tau _ { w } ) = y \prod _ { 2 } ,
$$

we have

$$
\begin{array} { r c l } { \displaystyle \frac { 1 } { \gamma ( \rho S \tau ^ { v } ) } - \frac { 1 } { \gamma ( \rho S \tau ^ { w } ) } } & { = } & { \displaystyle \frac { n } { n } \left( \frac { \prod ( y + 1 ) \gamma ( \rho S \tau _ { v } ) - \prod ( x + 1 ) \gamma ( \rho S \tau _ { w } ) } { \gamma ( \rho S \tau ^ { v u } ) \gamma ( \rho S \tau ^ { w u } ) \gamma ( \rho S \tau _ { v } ) \gamma ( \rho S \tau _ { w } ) } \right) } \\ & { = } & { \displaystyle \frac { 1 } { n } \left( \frac { \prod } { \gamma ( \rho S \tau ^ { v u } ) \gamma ( \rho S \tau ^ { w u } ) \gamma ( \rho S \tau _ { v } ) \gamma ( \rho S \tau _ { w } ) } \right) . } \end{array}
$$

However,

$$
\begin{array} { r l } & { \frac { 1 } { \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) } - \frac { 1 } { \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) } } \\ { = \ } & { \frac { \alpha ( \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) - \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) ) } { n ( \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) ) } } \\ & { \frac { 1 } { \alpha } ( \prod ( \{ \rho ( S \cdot 1 ) \} \prod _ { s = 1 } ^ { \infty } \exp ( \exp ( \exp ( \exp ( \nu S \cdot \mathbf { x } ^ { - 1 } ) ) ) )  } \\ { = \ } & { \frac { 1 } { \alpha ( \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) ) } } \\ & {  \frac { 1 } { \alpha ( \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) - ( \alpha \cdot 1 ) \gamma ) } ) } \\ { = \ } & { \frac { 1 } { \alpha ( \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) ) } } \\ { = \ } &  \frac { 1 } { \alpha } ( \frac { \prod ( \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) }  \gamma ( \rho S \cdot \mathbf { x } ^ { - 1 } ) \gamma (  \end{array}
$$

Thus, we get $1 ^ { \circ }$ .

By definition of $\phi$ , we have

$$
\left\{ \begin{array} { l l } { \displaystyle \phi ( \rho S \tau ^ { v u } ) = \sum _ { i _ { v } } b _ { i _ { v } } c _ { i _ { v } } \prod ^ { v } , } & { \quad \phi ( \rho S \tau _ { v } ) = \sum _ { i _ { v } } b _ { i _ { v } } \prod ^ { v } , } \\ { \displaystyle \phi ( \rho S \tau ^ { w u } ) = \sum _ { i _ { w } } b _ { i _ { w } } c _ { i _ { w } } \prod ^ { w } , } & { \quad \phi ( \rho S \tau _ { w } ) = \sum _ { i _ { w } } b _ { i _ { w } } \prod ^ { w } , } \end{array} \right.
$$

and

$$
\left\{ \begin{array} { l } { \displaystyle \phi ( \rho S \tau ^ { v } ) = \sum _ { i _ { v } } b _ { i _ { v } } \sum _ { i _ { v } } a _ { i _ { v } i _ { w } } \left( \prod _ { \rho } ^ { v } \prod _ { i } ^ { w } \right) , } \\ { \displaystyle \phi ( \rho S \tau ^ { w } ) = \sum _ { i _ { w } } b _ { i _ { w } } \sum _ { i _ { w } } a _ { i _ { w } i _ { v } } \left( \prod _ { \rho } ^ { v } \prod _ { i } ^ { w } \right) , } \end{array} \right.
$$

where $\prod ^ { v } \bigl ( \prod ^ { w } \bigr )$ denotes part of $\phi ( \rho S \tau ^ { v } ) ( \mathbf { r e s p . } \phi ( \rho S \tau ^ { w } )$ , which is the sum over black vertices of $\bar { \rho S \tau _ { v } } ( \rho S \tau _ { w } )$ . From symplectic order condition (3.11), we have

$$
\begin{array} { r l } { \phi ( \rho S \tau ^ { w } ) - \phi ( \rho S \tau ^ { w } ) } & { = \displaystyle \sum _ { i _ { v } , i _ { w } } ( b _ { i _ { v } } a _ { i _ { v } i _ { w } } - b _ { i _ { w } } a _ { i _ { w } i _ { v } } ) \prod _ { \ell = 1 } ^ { w } \prod } \\ & { = \displaystyle \sum _ { i _ { v } , i _ { w } } b _ { i _ { v } } b _ { i _ { w } } ( c _ { i _ { v } } - c _ { i _ { w } } ) \prod _ { \ell = 1 } ^ { v } \prod } \\ & { = \displaystyle \sum _ { i _ { v } } b _ { i _ { v } } c _ { i _ { v } } \prod _ { \ell = 1 } ^ { v } \sum _ { i _ { w } } b _ { i _ { w } } \prod } \\ & { \quad - \displaystyle \sum _ { i _ { v } } b _ { i _ { w } } c _ { i _ { w } } \prod _ { \ell = 1 } ^ { w } \sum _ { i _ { v } } b _ { i _ { w } } \prod } \\ & { = \displaystyle \phi ( \rho S \tau ^ { w } ) \phi ( \rho S \tau _ { w } ) - \phi ( \rho S \tau ^ { w \prime } ) \tilde { \rho } ( \rho S \tau _ { v } ) . } \end{array}
$$

Thus, the second part $2 ^ { \circ }$ of Theorem 3.7 is held. The following corollary is trivial.

Corollary 3.8. Suppose that the $R { - } K { - } N$ method (3.4) satisfying (3.7), has order at least $n - 1$ , with $n \geq 3 .$ . If $\rho S \tau ^ { v }$ and $\rho S \tau ^ { w }$ are different rooted $S$ -trees of order $n$ , then the order condition is the same as given in Theorem 3.7.

$$
\phi ( \rho S \tau ^ { v } ) = \frac { 1 } { \gamma ( \rho S \tau ^ { v } ) }
$$

holds, iff

$$
\phi ( \rho S \tau ^ { w } ) = \frac { 1 } { \gamma ( \rho S \tau ^ { w } ) }
$$

is satisfied.

Proof. Because R–K–N method (3.4) is of at least $n - 1$ -order, by Theorem 3.5, we have

$$
\phi ( \rho S \tau ^ { v u } ) = \frac { 1 } { \gamma ( \rho S \tau ^ { v u } ) } , \quad \phi ( \rho S \tau ^ { w u } ) = \frac { 1 } { \gamma ( \rho S \tau ^ { w u } ) } ,
$$

and

$$
\phi ( \rho S \tau _ { v } ) = \frac { 1 } { \gamma ( \rho S \tau _ { v } ) } , \quad \phi ( \rho S \tau _ { w } ) = \frac { 1 } { \gamma ( \rho S \tau _ { w } ) } ,
$$

similarly by Theorem 3.1, corollary is proved.

So we have the conclusion of this subsection.

Theorem 3.9. [SSC94,ZQ95b] A R–K–N method (3.4) that satisfies symplectic conditions is order of $p _ { ; }$ , iff for every $S$ -tree $S \tau$ there exists a rooted $S$ -tree $\rho S \tau ^ { v }$ which arises when a black vertex v of $S \tau$ is lifted as the root, such that

$$
\phi ( \rho S \tau ) = \frac { 1 } { \gamma ( \rho S \tau ) } .
$$

Proof. By Corollary 3.8 we know that any two different methods of choosing the corresponding root have equivalent order conditions. Hence the theorem is proved. -

As an application of Theorem 3.9, we consider the explicit $\mathrm { R - K - N }$ method, i.e., $a _ { i j } = 0$ , for $j > i$ $( i , j = 1 , 2 , \cdot \cdot , s )$ , and the non-redundant case, i.e., $b _ { i } \neq 0$ ( $i =$ $1 , 2 , \cdots , s )$ , see [OS92] . Then, we have $a _ { i j } = b _ { j } ( c _ { i } - c _ { j } )$ , for $i \geq j$ , $( i , j = 1 , 2 , \cdots , s )$ . So we obtain the following corollary.

Corollary 3.10. Non-redundant $R { - } K { - } N$ method (3.4) is explicit symplectic and of order $p _ { : }$ , iff:

$1 ^ { \circ }$ $a _ { i j } = b _ { j } ( c _ { i } - c _ { j } )$ , $1 \leq j < i \leq s .$ $2 ^ { \circ }$ $\bar { b } _ { j } = b _ { j } ( 1 - c _ { j } )$ , $1 \le j \le s$ .

$3 ^ { \circ }$ For every $S$ -tree $s \tau$ , there exist a rooted $S$ -tree $\rho S \tau ^ { v }$ , which arises when a black vertex v of sτ is lifted as the root, such that:

$$
\phi ( \rho S \tau ) = \frac { 1 } { \gamma ( \rho S \tau ) } .
$$

To obtain a 5-stage fifth order non-redundant symplectic explicit R–K–N method, the following equations are satisfied:

$$
\begin{array} { l l } { { a _ { i j } = b _ { j } \bigl ( c _ { i } - c _ { j } \bigr ) , } } & { { 1 \leq j < i \leq s , } } \\ { { \bar { b } _ { j } = b _ { j } \bigl ( 1 - c _ { j } \bigr ) , } } & { { 1 \leq j \leq s , } } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { 5 } b _ { j } = 1 } , } \\ { { \displaystyle \sum _ { j = 1 } ^ { 5 } b _ { j } c _ { j } = \frac 1 2 , } } \end{array}
$$

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \leq x ^ { 2 } - \frac { 3 } { 3 } x ^ { 2 } - \frac { 3 } { 5 } x ^ { 3 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } + \frac { 3 } { 5 } x ^ { 3 } - \frac { 3 } { 5 } x ^ { 5 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } + \frac { 3 } { 5 } x ^ { 4 } - \frac { 3 } { 5 } x ^ { 5 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } - \frac { 3 } { 5 } x ^ { 2 } - \frac { 1 } { 5 } x ^ { 3 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } - \frac { 1 } { 5 } x ^ { 5 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 5 } - \frac { 1 } { 5 } x ^ { 3 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } - \frac { 3 } { 5 } x ^ { 5 } - \frac { 3 } { 5 } x } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } - \frac { 3 } { 5 } x ^ { 5 } } \\ & { \leq \frac { 1 } { 2 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } - \frac { 3 } { 5 } x ^ { 3 } } \\ & { \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } + \frac { 3 } { 5 } x ^ { 4 } } \\ & { \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 2 } } \\ & { \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } - \frac { 3 } { 5 } x ^ { 2 } } \\ & { \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } } \\ & { \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } - \frac { 3 } { 5 } x ^ { 3 } } \\ & { \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } } \\ &  \leq \frac { 3 } { 5 } \leq x ^ { 3 } \leq \frac { 3 } { 5 } x ^ { 3 } \end{array}
$$

Replacing $a _ { i j }$ of system equations $( 3 . 4 4 ) - ( 3 . 5 3 )$ by (3.42), we get a system of 10 equations for parameters $b _ { i } , c _ { i } ( i = 1 , \cdots , 5 )$ . Every order condition of system (3.44) − (3.53) corresponds to the $S$ -trees of the same number in Fig. 3.2.

![](images/0736e0d61574d7d4923411aabb2f81ab87d534b454227576e0a8e99ce7a5800c.jpg)  
Fig. 3.2. Rooted $S$ -trees corresponding to order condition (3.44) – (3.53)

For the sake of convenience, we choose monotonic labelings for trees in Fig. 3.2. We obtain the Equations (3.46). In the following list we provide four sets of numerical solutions, whose laws are yet to be studied further.

<table><tr><td>i</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="2">1{</td><td>bi</td><td>0.396826</td><td>-0.824374</td><td>0.204203</td><td>1.002182</td><td>0.221161</td></tr><tr><td>Ci</td><td>0.961729</td><td>0.866475</td><td>0.127049</td><td>0.754358</td><td>0.229296</td></tr><tr><td rowspan="3">2{</td><td>bi</td><td>0.221160</td><td>1.002182</td><td>0.204203</td><td>-0.824375</td><td>0.396827</td></tr><tr><td>Ci</td><td>0.770703</td><td>0.245641</td><td>0.872950</td><td>0.133524</td><td>0.038270</td></tr><tr><td>bi</td><td>-1.670799</td><td>1.221431</td><td>0.088495</td><td>0.959970</td><td>0.400902</td></tr><tr><td rowspan="3">3{ 4{</td><td>Ci</td><td>0.694313</td><td>0.637071</td><td>-0.020556</td><td>0.795861</td><td>0.301165</td></tr><tr><td>bi</td><td>0.400902</td><td>0.959969</td><td>0.088495</td><td>1.221434</td><td></td></tr><tr><td>Ci</td><td>0.698834</td><td>0.204138</td><td>1.020556</td><td>0.362928</td><td>-1.670802 0.305086</td></tr></table>

Remark 3.11. R–K, P–R–K, and R–K–N methods have corresponding order conditions. The order conditions for symplectic R–K, symplectic P–R–K, and symplectic $\mathrm { R - K - N }$ method can be simplified using symplectic conditions. The order conditions for order 1 to 8 have already been listed in Table 1.4. Calvo and Hairer[CH95] further reduce the number of independent condition in R–K–N method. See Table 3.1.

Table 3.1. Order conditions R–K–N method and Symplectic R–K–N method for general case   

<table><tr><td rowspan=1 colspan=2>Order</td><td rowspan=1 colspan=1>R-K-N method</td><td rowspan=1 colspan=1>Symplectic R-K-Nmethod</td></tr><tr><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>1</td><td rowspan=4 colspan=1>12245</td></tr><tr><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>36</td></tr><tr><td rowspan=1 colspan=2>6</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=2>7</td><td rowspan=1 colspan=1>20</td><td rowspan=2 colspan=1>1014</td></tr><tr><td rowspan=1 colspan=2>8</td><td rowspan=1 colspan=1>36</td></tr></table>

# 7.4 Formal Energy for Symplectic R–K Method

The energy $H ( z )$ of a Hamiltonian system is also an invariant of the system. However, under normal circumstances, no symplectic scheme can preserve all the original Hamilton energy $\left[ \mathrm { F e n 9 8 a } \right]$ . On the other hand, any symplectic scheme preserves a formal Hamiltonian energy, which approaches the original Hamiltonian energy with the precision of numerical scheme. The calculation of formal energy can be done in many ways. First, we have obtained a complete method in theory to obtain the formal energy of a symplectic difference scheme constructed by generating function $[ \mathrm { F e n 9 8 a } ]$ . Yoshida [Yos90] uses Lie series of BCH Formula to determine the formal energy of separable Hamiltonian. What is insufficient is that the existing formal energy computational methods for symplectic R–K method mostly use Poincare lemma, and then use the ´ quadrature method. Although theoretically primary function (total differential) does exist, obtaining the primary function through the integral is not that easy. Therefore, we attempt to calculate the formal energy of a symplectic R–K method in a easy way that does not need the integral and also does not need any differentiation.

# 7.4.1 Modified Equation

Consider the numerical solution of ODEs

$$
\dot { z } = f ( z ) , \quad z \in \mathbf { R } ^ { n } .
$$

The R–K method for Equation (4.1) is defined as follows:

$$
\begin{array} { l } { { \displaystyle k _ { i } = f \bigg ( z _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } k _ { j } \bigg ) } , } \\ { { \displaystyle z _ { 1 } = z _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } k _ { i } } . } \end{array}
$$

Since the fundamental work of Butcher, numerical solution $z _ { 1 }$ can be written as (suppose $f$ is sufficiently differentiable):

$$
z _ { 1 } = z _ { 0 } + \sum _ { t \in T } \frac { h ^ { r ( t ) } } { r ( t ) ! } \alpha ( t ) \left( \gamma ( t ) \sum _ { i = 1 } ^ { s } b _ { i } \phi _ { i } ( t ) \right) F ( t ) ( z _ { 0 } ) .
$$

Definition 4.1. $\mathrm { [ H a i 9 4 ] }$ Let $t$ be a rooted tree. A partition of $t$ into $k$ subtrees $\{ s _ { 1 } , \ldots , s _ { k } \}$ is a set $S$ , consisting of $k - 1$ branches of $t$ such that the trees $s _ { 1 } , \ldots , s _ { k }$ are obtained when the branches of $S$ are removed from $t$ . Such a partition is denoted by $( t , S )$ . We further denote $\alpha ( t , S )$ as the number of possible monotonic labelings of $t$ such that the vertices of the subtrees $s _ { j }$ are labeled consecutively.

Example 4.2. All partitions of $t = [ [ \tau ] , [ \tau ] ]$ , $t$ into $k$ subtrees with the numbers $\alpha ( t , S )$ :

![](images/b68bb2a003e82ef71d933859b932791e488cea4a0df365d9e58122866cd8eeee.jpg)

Suppose a numerical method can be expressed as a formal series

$$
z _ { 1 } = z _ { 0 } + \sum _ { t \in T } \frac { h ^ { r ( t ) } } { r ( t ) ! } \alpha ( t ) a ( t ) F ( t ) ( z _ { 0 } ) ,
$$

Table 4.1. Relation between coefficients $a ( t )$ and $b ( t )$ (1)   

<table><tr><td>t=·</td><td>= b() a（)</td></tr><tr><td>t=！</td><td>a（/）= b（/）+b(0)²</td></tr><tr><td>t=Y</td><td>a（） =b(）+2b（/）6(0）+b(0)²</td></tr><tr><td>t=</td><td>(&gt;） a（&gt;）+3b（/）b(.）+b(0)³ a</td></tr></table>

where $a : T  \mathbf { R }$ is an arbitrary function. Such a series is called a $B$ -series. If function $f ( z )$ is only $N .$ -times continuously differentiable, then the series (4.5) has to be interpreted as a finite sum over $t \in T$ with $( r ( t ) \leq N )$ .

Theorem 4.3. $\mathrm { [ H a i 9 4 ] }$ Let $a : T  \mathbf { R }$ be an arbitrary mapping, and the right side of equation (4.1) $f ( z )$ is $N$ -times continuously differentiable. The numerical solution given by (4.5) satisfies

$$
z _ { 1 } = \widetilde { z } ( t _ { 0 } + h ) + O ( h ^ { N + 1 } ) .
$$

Here, $\widetilde { z } ( t )$ is the exact solution of the modified equation:

$$
\widetilde { \dot { z } } = \sum _ { r ( t ) \leq N } \frac { h ^ { r ( t ) - 1 } } { r ( t ) ! } \alpha ( t ) b ( t ) F ( t ) ( \widetilde { z } ) ,
$$

where the coefficients $b ( t )$ can be defined recursively by:

$$
a ( t ) = \sum _ { k = 1 } ^ { r ( t ) } \frac { 1 } { k ! } \sum _ { ( t , S ) } \Big ( \operatorname { \delta } _ { r \left( s _ { 1 } \right) , \cdots , r \left( s _ { k } \right) } ^ { r ( t ) } \Big ) \frac { \alpha ( t , S ) } { \alpha ( t ) } b ( s _ { 1 } ) \cdots b ( s _ { k } ) .
$$

The second sum in (4.8) is over all partitions of $t$ into $k$ subtrees $\{ s _ { 1 } , \cdots , s _ { k } \}$

By (4.8), we can define relation between coefficients $a ( t )$ and $b ( t )$ , See Table 4.1 to Table 4.4[LQ01] .

According to Table 4.1 – Table 4.4, we can determine modified equation for R–K equation (up to 5 orders, it is clear that as long as the order continues to add 6, 7-order tree · · · equation can be modified to any order).

Remark 4.4. If numerical method is symmetrical (or time-reversible), then when $r ( t )$ is even, $b ( t ) = 0$ .

Remark 4.5. If numerical method is $p$ -order, in other words when $r ( t ) \leq p , a ( t ) =$ 1; then, if $2 \leq r ( t ) \leq p , \ b ( \bullet ) = 1 , \ b ( t ) = 0$ ; if $r ( t ) = p + 1$ , $b ( t ) = a ( t ) - 1$ .

$$
\begin{array} { r l } & { c ( \sqrt { \gamma } ) = \nu ( \sqrt { \gamma } ) + 2 \alpha ( \epsilon ) \nu ( \sqrt { \gamma } ) + 2 \alpha ( \epsilon ) ^ { 2 } \lambda ( \epsilon ) ^ { 2 } + \lambda ( \epsilon ) ^ { 3 } } \\ & { - \big ( \sqrt { \gamma } \big ) - \nu \big ( \sqrt { \gamma } \big ) \big ( \frac { \lambda } { 2 } \lambda ( \epsilon ) \big ( \sqrt { \gamma } \big ) \big ) ^ { 2 } \frac { 2 \lambda ( \epsilon ) } { 3 } \big ( \lambda ( \epsilon ) \big ( \sqrt { \gamma } \big ) \big ) \times [ 1 ] \gamma } \\ & { \qquad + \frac { 1 0 } { 3 } \nu ( \epsilon ) ^ { 3 } \nu ( \hat { \gamma } ) + 2 \alpha ( \epsilon ) ^ { 4 } } \\ & { - \big ( \Upsilon ^ { \prime } \big ) - \nu \big ( \Upsilon ^ { \prime } \big ) + \alpha ( \epsilon ) \nu ( \sqrt { \gamma } ) + 2 \alpha ( \epsilon ) \nu ( \bigtriangleup ) } \\ & { \qquad + \alpha ( \epsilon ) \alpha ( \epsilon ) ^ { 3 } \big ( \lambda ( \epsilon ) ^ { 4 } \big ) } \\ & { - \big ( \big ( \sum _ { j \in J } \big ) - \nu \big ( \sum _ { j \in J } \big ) + \alpha ( \epsilon ) ^ { 2 } \big ) + \alpha ( \epsilon ) ^ { 2 } } \\ & { \qquad + \beta ( \epsilon ) ^ { 3 } \alpha ( \epsilon ) ^ { 4 } - \nu ( \epsilon ) ^ { 4 } } \\ & { \qquad + \beta ( \epsilon ) ^ { 3 } \alpha ( \epsilon ) ^ { 4 } \big ) + \alpha ( \epsilon ) ^ { 4 } } \end{array}
$$

$$
z _ { n + 1 } = z _ { n } + h f \Big ( \frac { z _ { n } + z _ { n + 1 } } { 2 } \Big ) .
$$

Modified equation can be defined1

$$
\begin{array} { r c l } { { \widetilde { \dot { z } } ~ = } } & { { f ( \widetilde { z } ) - \displaystyle \frac { h ^ { 2 } } { 2 4 } \Big [ f ^ { ( 2 ) } ( f , f ) - 2 f ^ { ( 1 ) } f ^ { ( 1 ) } f \Big ] + \displaystyle \frac { h ^ { 4 } } { 1 2 0 } \Big [ \frac { 7 } { 4 8 } f ^ { ( 4 ) } ( f , f , f , f ) } } \\ { { } } & { { } } & { { \displaystyle + \frac { 1 } { 4 } f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f ) - \displaystyle \frac { 1 } { 4 } f ^ { ( 2 ) } \big ( f , f ^ { ( 2 ) } ( f , f ) \big ) - \frac { 3 } { 2 } f ^ { ( 2 ) } \big ( f , f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ) } } \\ { { } } & { { } } & { { \displaystyle + \frac { 3 } { 4 } f ^ { ( 2 ) } \big ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f \big ) - \displaystyle \frac { 7 } { 1 2 } f ^ { ( 1 ) } f ^ { ( 3 ) } ( f , f , f ) - \displaystyle \frac { 1 } { 2 } f ^ { ( 1 ) } f ^ { ( 2 ) } \big ( f , f ^ { ( 1 ) } f \big ) } } \\ { { } } & { { } } & { { \displaystyle + \frac { 1 } { 4 } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } \big ( f , f \big ) + \displaystyle \frac { 3 } { 2 } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] + O ( h ^ { 6 } ) . } } \end{array}
$$

Example 4.7. 2-stage Gauss–Legendre method [HNW93] :

$$
\begin{array} { l } { { \iota = \sqrt [ 4 ] { \pi } \Bigg | a \big ( \textstyle { \begin{array} { l } { \Psi } \\ { \Psi } \end{array} } \big ) = b \big ( \textstyle { \begin{array} { l } { \Psi } \\ { \Psi } \end{array} } \big ) + \frac { 5 } { 2 } b ( \bullet ) b \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) + \frac { 1 0 } { 3 } b ( \bullet ) ^ { 2 } b ( \textstyle { \mathsf { Y } } ^ { * } ) } } \\ { { \qquad + \frac { 5 } { 2 } b ( \bullet ) ^ { 3 } b ( \underline { { \ell } } ^ { \prime } ) + b ( \bullet ) ^ { 5 } } } \\ { { \iota = \mathbb { Y } } \Bigg | a \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) = b \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) + \frac { 5 } { 2 } b ( \bullet ) b \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) + \frac { 5 } { 2 } b ( \bullet ) b \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) + \frac { 1 0 } { 3 } b ( \bullet ) ^ { 2 } b \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) }  \\ { { \qquad + \frac { 1 0 } { 3 } b ( \bullet ) ^ { 2 } b \big ( \textstyle { \mathsf { Y } } ^ { * } \big ) + 5 b ( \bullet ) ^ { 3 } b ( \textstyle { \mathsf { Z } } ^ { * } ) + b ( \bullet ) ^ { 5 } } } \end{array}
$$

$$
t = \sum _ { i = 0 } ^ { \infty } | a ( \sum _ { j = 0 } ^ { \infty } ) = b ( \sum _ { i = 0 } ^ { \infty } ) + 5 b ( \bullet ) b ( \sum _ { j = 0 } ^ { \infty } ) + 1 0 b ( \sum _ { i = 0 } ^ { \infty } ) b ( \sum _ { j = 1 } ^ { \infty } ) + 1 0 b ( \bullet ) ^ { 2 } b ( \sum _ { i = 0 } ^ { \infty } )
$$

$$
+ 1 5 b ( \bullet ) b ( \bullet ) ^ { 2 } + 1 0 b ( \bullet ) ^ { 3 } b ( \bullet ) ^ { 5 } + b ( \bullet ) ^ { 5 }
$$

$$
 \begin{array} { l l l } { { \frac { 1 } { 2 } } - { \frac { \sqrt { 3 } } { 6 } } { | \begin{array} { l l l } { ~ { \frac { 1 } { 4 } } ~ } & { { \frac { 1 } { 4 } } - { \frac { \sqrt { 3 } } { 6 } } } \\ { { \frac { 1 } { 2 } } + { \frac { \sqrt { 3 } } { 6 } } { | \frac { 1 } { 4 } + { \frac { \sqrt { 3 } } { 6 } } ~ } & { ~ { \frac { 1 } { 4 } } } \\ { ~ { \frac { 1 } { 2 } } ~ } & { ~ { \frac { 1 } { 2 } } } \end{array} | } } \end{array} }
$$

Modified equation is defined2

$$
\begin{array} { r c l } { { \displaystyle \widetilde { \dot { z } } ( t ) ~ = } } & { { \displaystyle f ( \widetilde { z } ) - \frac { 3 7 h ^ { 4 } } { 8 8 4 0 } \big [ f ^ { ( 4 ) } ( f , f , f , f ) - 4 f ^ { ( 1 ) } f ^ { ( 3 ) } ( f , f , f ) \big ] - \frac { h ^ { 4 } } { 7 2 0 } \big [ f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f ^ { ( 1 ) } ) } } \\ { { } } & { { } } & { { \displaystyle - f ^ { ( 2 ) } \big ( f , f ^ { ( 2 ) } ( f , f ) \big ) - 2 f ^ { ( 1 ) } \big ( f ^ { ( 2 ) } f , f ^ { ( 1 ) } f \big ) + f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ) \big ] } } \\ { { } } & { { } } & { { \displaystyle - \frac { 3 7 h ^ { 4 } } { 2 8 8 0 } \big [ f ^ { ( 2 ) } \big ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f \big ) - 2 f ^ { ( 2 ) } \big ( f , f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ) + 2 f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] } } \\ { { } } & { { } } & { { \displaystyle + O ( h ^ { 6 } ) . } } \end{array}
$$

Example 4.8. 2-order diagonal implicit R–K method: Modified equation:

$$
\begin{array} { r l } & { \quad \quad ( \frac { 1 } { 2 } \kappa \frac { \partial \kappa } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } } \\ &  = \frac { \kappa _ { i } ( \frac { 1 } { 2 } \kappa ) _ { i } ( \frac { 1 } { 2 } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } } \\ &  \quad + \frac { \kappa _ { i } ( \frac { 1 } { 2 } \kappa ) _ { i } ( \frac { 1 } { 2 } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } } \\ &  = \frac  \kappa _ { i } ( \frac { 1 } { 2 } \kappa ) _ { i } ( \frac { 1 } { 2 } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 } { \partial \tau } ) _ { i } ( \frac { 1 } { \partial \tau } ) _ { j } ( \frac { 1 }  \ \end{array}
$$

$$
\begin{array} { r l } { \tilde { \dot { z } } ( t ) = } & { f ( \tilde { z } ) - \cfrac { h ^ { 2 } } { 9 6 } \big [ f ^ { ( 2 ) } ( f , f ) - 2 f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] - \cfrac { 1 7 h ^ { 4 } } { 1 0 2 4 0 } \big [ f ^ { ( 4 ) } ( f , f , f , f ) } \\ & { - 4 f ^ { ( 1 ) } f ^ { ( 3 ) } ( f , f , f ) \big ] - \cfrac { 1 3 h ^ { 4 } } { 2 5 6 0 } \big [ f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f ) - f ^ { ( 2 ) } ( f , f ^ { ( 2 ) } ( f , f ) ) } \\ & { - 2 f ^ { ( 1 ) } ( f ^ { ( 2 ) } f , f ^ { ( 1 ) } f ) + f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ) \big ] - \cfrac { h ^ { 4 } } { 2 5 6 0 } \big [ f ^ { ( 2 ) } ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f ) } \\ & { - 2 f ^ { ( 2 ) } \big ( f , f ^ { ( 1 ) } f ^ { ( 1 ) } + 2 f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 1 ) } f \big ] + O ( h ^ { 6 } ) . } \end{array}
$$

<table><tr><td>1-43-4</td><td>1 0 4 1 1</td></tr><tr><td>1 2</td><td>2 4 1 2</td></tr></table>

# 7.4.2 Formal Energy for Symplectic R–K Method

Let $T$ be a set of all rooted trees. On set $T$ we define a relation $\sim$ , as follows:

$1 ^ { \circ }$ $t \sim t$ .   
$2 ^ { \circ }$ $u \circ v \sim v \circ u$ .   
$3 ^ { \circ }$ If $u _ { 1 } \circ v _ { 1 } \sim u _ { 2 } \circ v _ { 2 } , u _ { 2 } \circ v _ { 2 } \sim u _ { 3 } \circ v _ { 3 }$ , then $u _ { 1 } \circ v _ { 1 } \sim u _ { 3 } \circ v _ { 3 }$

Where $u \circ v$ and $v \circ u$ is defined by

if $\boldsymbol { u } = [ u _ { 1 } , \cdot \cdot \cdot , u _ { m } ] , \boldsymbol { v } = [ v _ { 1 } , \cdot \cdot \cdot , v _ { m } ]$ , then

$$
u \circ v = [ u _ { 1 } , \cdots , u _ { m } , v ] , \quad v \circ u = [ v _ { 1 } , \cdots , v _ { m } , u ] .
$$

Obviously $^ { 6 6 } \sim ~ $ expresses an equivalent relation. Using this equivalent relation to classify the root tree collection $T$ , we can obtain a quotient space, denoted by $T E$ . Then we may construct another set $T \widetilde { E }$ , which is obtained by filtering every equivalent class of $T E$ . The filtering rule is as follows: if $\bar { t } \in T E$ , then $\bar { t }$ is a rooted tree’s subset class. We sort the element of $\bar { t }$ according to $\sigma ( t )$ , and choose $t$ so that $\sigma ( t )$ is the biggest. In general, such $t$ is not unique and we can choose any one of them. For each element in the $T \widetilde { E }$ we define a quasi elementary differential

$$
F ^ { * } ( t ) = f ^ { ( m - 1 ) } \bigl ( F ( t _ { 1 } ) , F ( t _ { 2 } ) , \cdot \cdot \cdot , F ( t _ { m } ) \bigr ) .
$$

The reason why we call (4.9) quasi elementary differential is because under normal circumstances, elementary differential has been defined as:

$$
F ( t ) = f ^ { ( m ) } \bigl ( F ( t _ { 1 } ) , F ( t _ { 2 } ) , \cdot \cdot \cdot , F ( t _ { m } ) \bigr ) ,
$$

where $f ^ { ( m ) } ( K _ { 1 } , K _ { 2 } , \cdot \cdot \cdot , K _ { m } )$ is $m$ -order Frechet derivative.

Here, we regard $f ^ { ( m - 1 ) } ( K _ { 1 } , K _ { 2 } , \cdot \cdot \cdot , K _ { m } )$ as a formal definition. Obviously, when $f$ is a differential of some function, $f ^ { ( m - 1 ) } ( K _ { 1 } , K _ { 2 } , \cdot \cdot \cdot , K _ { m } )$ will become $m$ - order Frechet derivative of its primary function. For example, $t = [ \tau , \tau , \tau , \tau ]$ , $F ^ { * } [ t ] =$ $f ^ { ( 3 ) } ( f , f , f , f )$ . Let $f = J H _ { z } $ , then $F ^ { * } ( t )$ becomes $J H ^ { ( 4 ) } ( J H _ { z } , J H _ { z } , J H _ { z } , J H _ { z } )$ , which is obviously a fourth-order Frechet derivative. We use $\mathcal { L }$ to express this mapping, namely

$$
\begin{array} { r l } { \mathcal { L } : } & { f ^ { ( m - 1 ) } ( K _ { 1 } ( f ) , K _ { 2 } ( f ) , \cdot \cdot \cdot , K _ { m } ( f ) ) } \\ & { \longmapsto J H ^ { ( m ) } ( K _ { 1 } ( J H _ { z } ) , K _ { 2 } ( J H _ { z } ) , \cdot \cdot \cdot , K _ { m } ( J H _ { z } ) ) . } \end{array}
$$

Obviously, $\mathcal { L }$ is a 1 to 1 mapping. From now on, we will always use $\mathcal { L }$ to express this mapping unless it is specified otherwise. We will no longer differentiate $F ^ { * } ( t )$ with $\mathcal { L } ( F ^ { \ast } ( t ) )$ . The operation of $F ^ { * } ( t )$ is always thought as operation of $\mathcal { L } ( F ^ { \ast } ( t ) )$ .

Lemma 4.9. Let $( A , b )$ be a symplectic R–K method, $a ( t ) = \gamma ( t ) \sum _ { j = 1 } ^ { s } b _ { j } \phi _ { j } ( t ) ,$ , then:

$$
\frac { a ( u \circ v ) } { \gamma ( u \circ v ) } + \frac { a ( v \circ u ) } { \gamma ( v \circ u ) } = \frac { a ( u ) } { \gamma ( u ) } \cdot \frac { a ( v ) } { \gamma ( v ) } , \quad u , v \in T P .
$$

Proof. [CS94] .

Lemma 4.10. Let $\widetilde { H } ( z , h )$ be the formal energy of symplectic $R – K$ method $( A , b )$ , then the corresponding modified equation is (possible differ by an arbitrary constant):

$$
\widetilde { \dot { z } } = \widetilde { f } ( \widetilde { z } ) = J \widetilde { H } _ { \widetilde { z } } .
$$

Conversely, if modified equation of symplectic $\mathbf { R - K }$ the method $( A , b )$ are $\widetilde { f } ( \widetilde { z } )$ , then we have

$$
\widetilde { H } _ { z } = - J \widetilde { f } ( z ) .
$$

Proof. Note that both the modified equation and the formal energy can be obtained essentially via series expansion, Lemma 4.10 is obvious. -

Lemma 4.11. Let $( A , b )$ be a symplectic $R$ –K method, $a ( t ) = \gamma ( t ) \sum _ { j = 1 } ^ { s } b _ { j } \phi _ { j } ( t ) ,$ , then:

$$
\frac { b ( u \circ v ) } { \gamma ( u \circ v ) } + \frac { b ( v \circ u ) } { \gamma ( v \circ u ) } = 0 , \quad u , v \in T P , \quad u \neq v ,
$$

where $b ( t )$ is determined recursively by (4.8).

Proof. Using the method that proves Lemma 10 in literature $\mathrm { [ H a i 9 4 ] }$ and modifying it slightly will complete the proof. We leave out its detail here. -

Remark 4.12. By (4.13) and relation $\alpha ( t ) \gamma ( t ) \sigma ( t ) = r ( t )$ we obtain

$$
\frac { \alpha ( u \circ v ) b ( u \circ v ) } { \alpha ( v \circ u ) b ( v \circ u ) } + \frac { \sigma ( v \circ u ) } { \sigma ( u \circ v ) } = 0 .
$$

We now need another coefficient $\nu ( t )$ related to rooted tree. Note first that the rooted trees $u \circ v$ and $v \circ u$ represent an identical unrooted tree with different root, i.e., selecting the other vertex of $u \circ v$ as root leads to tree $v \circ u$ . Thus, in an equivalent class, it can always transform one rooted tree to another by selecting a different root. Take $\bar { t } \in T E$ , then $\bar { t }$ is one equivalent class of rooted tree collection ( $\mathbf { \chi } _ { t }$ represents the element). Let $u \in \bar { t }$ , then $u$ can be obtained by selecting some vertex of $t$ as the root node. We denote $\nu ( u )$ as number of vertices of $t$ which may be selected.

Example 4.13. $t = [ \tau , \tau , [ \tau ] ]$ , then $\bar { t } = \{ t _ { 1 } , t _ { 2 } , t _ { 3 } , t _ { 4 } \}$ , where

$$
\begin{array} { l } { { { \bf { \Delta } } ^ { \mathrm { p r e }  { \bf { \bar { t } } } , { \bf { \Delta } } , { \bf { \Sigma } } ^ { \ast } } - [ { \bf { \bar { t } } } , { \bf { \Sigma } } ^ { \prime } , { \bf { \Sigma } } ^ { \prime } ] { \bf { \Delta } } ^ { \mathrm { m a x } } { \bf { \Sigma } } ^ { \ast } - [ { \bf { \bar { t } } } 1 , { \bf { \Sigma } } ^ { \prime } 2 , { \bf { \Sigma } } ^ { \nu _ { 3 } } , { \bf { \Sigma } } ^ { \nu _ { 4 } } 2 , { \bf { \Sigma } } ^ { \mathrm { w a x } } { \bf { \Sigma } } ^ { \mathrm { c } } } } \\ { { \bf { \Sigma } } _ { 1 } = { \bf { \Sigma } } ^ { \ast } \dot { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } _ { 2 } { \bf { \Sigma } } _ { 2 } { \bf { \Sigma } } = { \bf { \bar { \Sigma } } } ^ { \ast } { \bf { \bar { \Sigma } } } ^ { \ast } { \bf { \Sigma } } _ { 3 } { \bf { \Sigma } } _ { 4 } { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } _ { 3 } { \bf { \Sigma } } _ { 4 } = { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } _ { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } _ { 4 } = { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } _ { \bf { \Sigma } } ^ { \ast } { \bf { \Sigma } } _ { \bf { \Sigma } } . }  \end{array}
$$

We have

$$
\nu ( t _ { 1 } ) = 1 , \quad \nu ( t _ { 2 } ) = 1 , \quad \nu ( t _ { 3 } ) = 1 , \quad \nu ( t _ { 4 } ) = 2 .
$$

Then, the following relation for $\nu ( t )$ is hold

$$
\nu ( u \circ v ) \cdot \sigma ( u \circ v ) = \nu ( v \circ u ) \cdot \sigma ( v \circ u ) .
$$

Lemma 4.14. Let rooted tree $u \ne v$ , then

$$
F ^ { * } ( u \circ v ) = - F ^ { * } ( v \circ u ) .
$$

Proof. $F ^ { \ast } ( u \circ v ) = J J ^ { - 1 } F ( u ) J J ^ { - 1 } F ( v )$ . Let $\alpha = J ^ { - 1 } F ( u ) , \beta = J ^ { - 1 } F ( v )$ , where $F ( u ) , F ( v )$ are elementary differentials. If $u = [ u _ { 1 } , u _ { 2 } , \cdot \cdot \cdot , u _ { m } ]$ , then

$$
F ( u ) = f ^ { ( m ) } \bigl ( F ( u _ { 1 } ) , F ( u _ { 2 } ) , \cdot \cdot \cdot , F ( u _ { m } ) \bigr ) ,
$$

where $f = J H _ { z }$ , and $F ( v )$ is similar to $F ( u )$ .

By properties of elementary differential (multilinear mapping), $\alpha , \beta$ are $2 n$ -dimensional vectors, and

$$
F ^ { * } ( u \circ v ) = J ( \alpha , J \beta ) = J \alpha ^ { \mathrm { T } } J \beta = - J \beta ^ { \mathrm { T } } J \alpha = - F ^ { * } ( v \circ u ) .
$$

Therefore, the lemma is completed.

Lemma 4.15. Let $t ^ { * } \in T \widetilde E$ , then

$$
\alpha ( t ^ { * } ) b ( t ^ { * } ) \nabla F ^ { * } ( t ^ { * } ) = \sum _ { t \in t ^ { * } } \alpha ( t ) b ( t ) F ( t ) .
$$

Proof. First the right side of (4.17) is uniquely determined, and on the left side the selection of $t ^ { * }$ may not necessarily be unique. Therefore, it is required to prove that (4.17) the left side of the formula is independent of selection of $t ^ { * }$ . We explain it as follows: given $t ^ { * 1 } \in \overline { { t ^ { * } } }$ , such that $\sigma ( t ^ { * } ) = \sigma ( t ^ { * 1 } )$ , then there exists a series of $u \circ v$ , such that

$$
t ^ { * } = u _ { 1 } \circ v _ { 1 } \sim v _ { 1 } \circ u _ { 1 } = u _ { 2 } \circ v _ { 2 } \sim v _ { 2 } \circ u _ { 2 } = \cdot \cdot \cdot \sim u _ { m } \circ v _ { m } = t ^ { * 1 } .
$$

Let $m = 2$ , i.e., $t ^ { * } = u _ { 1 } \circ v _ { 1 }$ , $t ^ { * 1 } = v _ { 1 } \circ u _ { 1 }$ , then by (4.14)

$$
\alpha ( t ^ { * } ) b ( t ^ { * } ) = - \alpha ( t ^ { * 1 } ) b ( \mathbf { \Phi } ^ { * 1 } ) ,
$$

and by Lemma 4.14

$$
F ^ { * } ( u \circ v ) = - F ^ { * } ( v \circ u ) \Longrightarrow \nabla F ^ { * } ( u \circ v ) = - \nabla F ^ { * } ( v \circ u ) ,
$$

therefore

$$
\alpha ( t ^ { * } ) b ( t ^ { * } ) \nabla F ^ { * } ( t ^ { * } ) = \alpha ( t ^ { * 1 } ) b ( t ^ { * 1 } ) \nabla F ^ { * } ( t ^ { * 1 } ) .
$$

For $m > 2$ , $t ^ { * 1 }$ must be a node of (4.18), (4.19) is also held.

Next, $\nabla F ^ { * } ( t ^ { * } )$ must be a linear combination of basic differentials in the same class, i.e.,

$$
\nabla F ^ { * } ( t ^ { * } ) = \sum _ { t \in t ^ { * } } \beta ( t ) F ( t ) .
$$

Consider a special case:

$$
t ^ { * } = \begin{array} { l } { l } \\ { \overline { { \mathbf { \Gamma } } } } \end{array} \overset { \bullet } { \underset { i } { \longrightarrow } } \overset { \bullet } { \underset { i } { \longrightarrow } } j
$$

$$
F ^ { * } ( t ^ { * } ) = f ^ { ( 2 ) } ( f , f , f ^ { ( 1 ) } f ) .
$$

The differentiation of $F ^ { * } ( t ^ { * } )$ can be seen as a following process: first differentiate w.r.t. the root node one time, obtain $f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f )$ , and then differentiate w.r.t. each vertex one time, i.e., add 1 to each vertex superscript and then move it in front of its father along with its substance, continue moving until it reaches the front of root node. In this process, according to (4.4), every move accompanies a change in sign. Using the above example, differentiating w.r.t. the point $i , j , k , l , m$ respectively, we obtain

$$
\begin{array} { r l } { m } & { \longrightarrow - f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ) , \qquad l \longrightarrow - f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ) , } \\ { j } & { \longrightarrow - f ^ { ( 2 ) } ( f , f ^ { ( 2 ) } ( f , f ) ) , \qquad k \longrightarrow f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ) . } \end{array}
$$

Thus, we get:

$$
\begin{array} { r c l } { { \nabla F ^ { * } ( t ^ { * } ) ~ = ~ f ^ { ( 3 ) } ( f , f , f ^ { ( 1 ) } f ) - 2 f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ^ { ( 1 ) } f ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - f ^ { ( 2 ) } ( f , f ^ { ( 2 ) } ( f , f ) ) + f ^ { ( 1 ) } f ^ { ( 1 ) } f ^ { ( 2 ) } ( f , f ) . } } \end{array}
$$

It is easy to see,

$$
\beta ( t ) = \pm \frac { \nu ( t ) } { \nu ( t ^ { * } ) } ,
$$

where $^ { 6 6 } \pm \ v r$ is selected using the following rule: if $d ( \cdot )$ expresses the distance between the vertex to the root node, i.e., the least number of vertices passed from this vertex to the root node along the connection between vertices (including initial point and root node), then sign $( \beta ( t ) ) = ( - 1 ) ^ { d ( t ) }$ . Using the above example

$$
d ( i ) = 0 , \quad d ( m ) = d ( l ) = d ( j ) = 1 , \quad d ( k ) = 2 .
$$

By sig $\begin{array} { r } { \mathrm { ~ 1 ~ } ( b ( u \circ v ) ) = - \mathrm { s i g n } \left( b ( v \circ u ) \right) } \end{array}$ , we have

$$
( - 1 ) ^ { d ( t ) } = \frac { \mathrm { s i g n } \left( b ( t ) \right) } { \mathrm { s i g n } \left( b ( t ^ { \ast } ) \right) } ,
$$

therefore:

$$
\nabla F ^ { * } ( t ^ { * } ) = \sum _ { t \in \bar { t ^ { * } } } \frac { \alpha ( t ) b ( t ) } { \alpha ( t ^ { * } ) b ( t ^ { * } ) } F ( t ) .
$$

Thus, we get

$$
\alpha ( t ^ { * } ) b ( t ^ { * } ) \nabla F ^ { * } ( t ^ { * } ) = \sum _ { t \in \hat { t ^ { * } } } \alpha ( t ) b ( t ) F ( t ) .
$$

Therefore, the lemma is completed.

With the above results, we describe the main result of this section $\mathrm { [ H a i 9 4 ] }$ .

Theorem 4.16. Given a $R – K$ method $( A , b ) , A = ( a _ { i j } ) _ { s \times s } , b = ( b _ { 1 } , b _ { 2 } , \cdot \cdot \cdot , b _ { s } ) ^ { \prime }$ , its formal energy is

$$
\widetilde { H } ( z , h ) = - J \sum _ { \rho ( t ) \leq N } \frac { h ^ { \rho ( t ) - 1 } } { \rho ( t ) ! } \alpha ( t ) b ( t ) F ^ { * } ( t ) , \quad t \in T \widetilde { E } ,
$$

where $b ( t )$ is determined by $a ( t )$ (According to Table 4.1 to Table 4.4), i.e.,

$$
a ( t ) = \gamma ( t ) \sum _ { j = 1 } ^ { s } b _ { j } \phi _ { j } ( t ) .
$$

Proof. Let the modified equation be

$$
\widetilde { \dot { z } } = \sum _ { t \in T P } \frac { h ^ { r ( t ) - 1 } } { r ( t ) ! } \alpha ( t ) b ( t ) F ( t ) ( \widetilde { z } ) ,
$$

then

$$
\begin{array} { r c l } { { \widetilde { \dot { z } } } } & { { = } } & { { \displaystyle \sum _ { t ^ { * } \in T \widetilde { E } } \frac { h ^ { r ( t ^ { * } ) - 1 } } { r ( t ^ { * } ) ! } \sum _ { t \in \dot { t ^ { * } } } \alpha ( t ) b ( t ) F ( t ) ( \widetilde { z } ) } } \\ { { } } & { { = } } & { { \displaystyle \sum _ { t ^ { * } \in T \widetilde { E } } \frac { h ^ { r ( t ^ { * } ) - 1 } } { r ( t ^ { * } ) ! } \alpha ( t ^ { * } ) b ( t ^ { * } ) \nabla F ^ { * } ( t ^ { * } ) . } } \end{array}
$$

By Lemma 4.10

$$
\widetilde { H } _ { z } = - J \sum _ { t ^ { * } \in T \widetilde { E } } \frac { h ^ { r ( t ^ { * } ) - 1 } } { r ( t ^ { * } ) ! } \alpha ( t ^ { * } ) b ( t ^ { * } ) \nabla F ^ { * } ( t ^ { * } ) ,
$$

which leads to (differ by an arbitrary constant)

$$
\widetilde { H } ( z , h ) = - J \sum _ { t ^ { * } \in T \widetilde { E } } \frac { h ^ { r ( t ^ { * } ) - 1 } } { r ( t ^ { * } ) ! } \alpha ( t ^ { * } ) b ( t ^ { * } ) F ^ { * } ( t ^ { * } ) .
$$

The theorem is proved.

Remark 4.17. Literature $\left[ \mathrm { T a n 9 4 } \right]$ pointed out that each item of series expansion of formal energy of symplectic $\mathbf { R - K }$ scheme has 1 to 1 corresponding relationship with unrooted trees collection. This theorem specifically indicates this 1 to 1 correspondences.

Finally we sum up the method to construct the formal energy of a symplectic R–K method: given a symplectic R–K method $( A , b , c )$ , let $a ( t ) = \gamma ( t ) \sum _ { j } b _ { j } \phi _ { j } ( t )$ . Then according to Table 4.1 to Table 4.4 identify the corresponding $b ( t )$ to each rooted tree in $T \widetilde { E }$ . Using (4.20), we can directly write the formal energy. Without loss of generality, in practice we can choose

$$
T { \tilde { E } } = \{ \bullet , \forall , \forall , \forall , \ P \bullet \cdot \ \dot { \Psi } , \ U _ { \rho } , \dots \} .
$$

If we know the order of method or the method are time reversible (symmetrical), then according to Remark 4.4 and Remark 4.5 many calculations can be left out.

Example 4.18. Centered Euler scheme

$$
z _ { n + 1 } = z _ { n } + h f \Big ( \frac { z _ { n } + z _ { n + 1 } } { 2 } \Big ) .
$$

Its formal energy $\left[ \mathrm { T a n 9 4 } \right]$

$$
\begin{array} { r l } { \widetilde { H } ( z , h ) = } & { H ( z ) + \displaystyle \frac { h ^ { 2 } } { 2 4 } J f ^ { ( 2 ) } ( f , f ) - \frac { 7 h ^ { 4 } } { 5 7 6 0 } J f ^ { ( 3 ) } ( f , f , f , f ) } \\ & { - \displaystyle \frac { h ^ { 4 } } { 4 8 0 } J f ^ { ( 2 ) } ( f , f , f ^ { ( 1 ) } f ) - \frac { h ^ { 4 } } { 1 6 0 } J f ^ { ( 2 ) } ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f ) + O ( h ^ { 6 } ) . } \end{array}
$$

Example 4.19. Gauss–Legendre method

$$
\begin{array}{c} { \frac { { \frac { 1 } { 2 } } - { \frac { \sqrt { 3 } } { 6 } } } { \frac { 1 } { 2 } + { \frac { \sqrt { 3 } } { 6 } } } } \quad \quad { \frac { \frac { 1 } { 4 } } { \frac { 1 } { 4 } + { \frac { \sqrt { 3 } } { 6 } } } } \quad \quad { \frac { { \frac { 1 } { 4 } } - { \frac { \sqrt { 3 } } { 6 } } } { \frac { 1 } { 2 } } } \quad \quad \quad \quad { \frac { 1 } { 6 } } \quad  \\ { \quad \quad \quad { \frac { 1 } { 2 } } \quad \quad \quad \quad { \frac { 1 } { 2 } } \quad \quad \quad \quad { \frac { 1 } { 2 } } \quad } \end{array} 
$$

Its formal energy:

$$
\begin{array} { r c l } { { { \widetilde { H } ( z , h ) \ = } } } & { { { \displaystyle H ( z ) + \frac { 3 7 h ^ { 4 } } { 8 8 4 0 } } J f ^ { ( 3 ) } ( f , f , f , f ) + \frac { h ^ { 4 } } { 7 2 0 } J f ^ { ( 2 ) } ( f , f , f ^ { ( 1 ) } f ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \displaystyle \frac { 3 7 h ^ { 4 } } { 2 8 8 0 } J f ^ { ( 1 ) } ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f ) + { \cal O } ( h ^ { 6 } ) . } } \end{array}
$$

Example 4.20. Diagonal implicit $\mathbf { R - K }$ method

<table><tr><td>A</td><td>1 0 1 1</td></tr><tr><td></td><td>2 4 1 1 2 2</td></tr></table>

Its formal energy

$$
\begin{array} { r c l } { { { \widetilde { H } ( z , h ) } } } & { { = } } & { { H ( z ) + \displaystyle \frac { h ^ { 2 } } { 9 6 } J f ^ { ( 1 ) } ( f , f ) + \displaystyle \frac { 1 7 h ^ { 4 } } { 1 0 2 4 0 } J f ^ { ( 3 ) } ( f , f , f , f ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \displaystyle \frac { 1 3 h ^ { 4 } } { 2 5 6 0 } J f ^ { ( 2 ) } ( f , f , f ^ { ( 1 ) } f ) + \displaystyle \frac { h ^ { 4 } } { 2 5 6 0 } J f ^ { ( 1 ) } ( f ^ { ( 1 ) } f , f ^ { ( 1 ) } f ) + { \cal O } ( h ^ { 6 } ) . } } \end{array}
$$

# 7.5 Definition of $\mathbf { } a ( t )$ and $b ( t )$

We consider following schemes.

# 7.5.1 Centered Euler Scheme

$$
a ( \bullet ) = 1 \qquad a ( \bullet ) = 1 \qquad b ( \bullet ) = 1 \qquad b ( \bullet ) = 1 \qquad b ( \bullet ) = 0
$$

$$
a ( { \begin{array} { c c } { \bullet } \\ { \bullet } \end{array} } ^ { \bullet } ) = { \frac { 3 } { 4 } } \qquad a ( { \begin{array} { c c } { \bullet } \\ { \bullet } \end{array} } ) = { \frac { 3 } { 2 } } \qquad b ( { \begin{array} { c c } { \bullet } \\ { \bullet } \end{array} } ^ { \bullet } ) = - { \frac { 1 } { 4 } } \qquad b ( { \begin{array} { c c } { \bullet } \\ { \bullet } \end{array} } ) = { \frac { 1 } { 2 } }
$$

$$
( \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c } { { \dot { \mathbb { V } } } ^ { \bullet } ) = \frac { 1 } { 2 } } & { } & { } & { } & { } & { a ( \bullet \bullet \bullet ) } & { } & { } & { b ( \bullet \bullet \bullet b \bullet b ) } & { } & { } & { } & { b ( \bullet \bullet \bullet b \bullet ) } & { = 0 } \end{array}
$$

$$
a \left( \begin{array} { c } { { \bullet } } \\ { { \bullet } } \end{array} \right) = \frac { 3 } { 2 } a \left( \begin{array} { c } { { \bullet } } \\ { { \bullet } } \end{array} \right) = 3 b \left( \begin{array} { c } { { \bullet } } \\ { { \bullet } } \end{array} \right) = 0 b \left( \begin{array} { c } { { \bullet } } \\ { { \bullet } } \end{array} \right) = 0
$$

![](images/ff931d73fbbf67b249cf8a3673c5a228080b6a2034079c905221e9b97b55e236.jpg)

$$
a ( \bullet \bullet \bullet ) = \frac { 1 5 } { 1 6 } \qquad a ( \bullet \bullet ) = \frac { 1 5 } { 8 } \qquad b ( \bullet \bullet \bullet ) = - \frac { 1 } { 1 6 } \qquad b ( \bullet \bullet \bullet ) = - \frac { 3 } { 8 }
$$

$$
\begin{array} { l l l l } { { a \displaystyle { \binom { 1 } { 4 } } = \frac { 5 } { 4 } } } & { { a \displaystyle { \binom { 1 } { 2 } } = \frac { 5 } { 4 } } } & { { b \displaystyle { \binom { 1 } { 4 } } = \frac { 1 } { 4 } } } & { { b \displaystyle { \binom { 1 } { 2 } } = - \frac { 7 } { 1 2 } } } \\ { { } } & { { } } & { { } } \\ { { a \displaystyle { \binom { 1 } { 2 } } = \frac { 5 } { 2 } } } & { { a \displaystyle { \binom { 1 } { 2 } } = \frac { 1 5 } { 4 } } } & { { b \displaystyle { \binom { 1 } { 2 } } = - \frac { 1 } { 6 } } } & { { b \displaystyle { \binom { 3 } { 4 } } = \frac { 1 } { 4 } } } \\ { { } } & { { } } & { { } } \\ { { a \displaystyle { \binom { 1 5 } { 4 } } = \frac { 1 5 } { 2 } } } & { { b \displaystyle { \binom { 1 } { 4 } } = \frac { 3 } { 2 } } } & { { } } \end{array}
$$

# 7.5.2 Gauss–Legendre Method

<table><tr><td>1</td><td>V3 6</td><td>1</td><td>1-4</td><td>V3 6</td></tr><tr><td rowspan="2">1 +</td><td>V3</td><td>V</td><td></td><td></td></tr><tr><td>6</td><td>1-4 + 6</td><td>1</td><td></td></tr><tr><td colspan="2"></td><td>1</td><td>1</td><td></td></tr></table>

$\begin{array} { l c l l } { { a ( \bullet ) = 1 } } & { { \qquad a ( \bullet ^ { \bullet } ) = 1 } } & { { \qquad b ( \bullet ) = 1 } } & { { \qquad b ( \bullet ^ { \bullet } ) = 0 } } \\ { { a ( \bigtriangledown ^ { * } ) = 1 } } & { { \qquad a ( \bigtriangleup ^ { * } ) = 1 } } & { { \qquad b ( \bigtriangledown ^ { * } ) = 0 } } & { { \qquad b ( \bigtriangledown ^ { * } ) = 0 } } \\ { { } } & { { } } & { { } } \\ { { a ( \bigtriangleup ^ { * } ) = 1 } } & { { \qquad a \big ( \bigtriangledown ^ { * } \big ) = 1 } } & { { \qquad b ( \bigtriangledown ^ { * } ) = 0 } } & { { \qquad b \big ( \bigtriangledown ^ { * } \big ) = 0 } } \end{array}$ $a ( \bullet \bullet ) ^ { \bullet } ) = 1 \qquad a ( \bullet \bullet ) = 1 \qquad b ( \bullet \bullet ) ^ { \bullet } ) = 0 \qquad b ( \bullet \bullet ) = 0$ $a ( \bullet , \dot { \zeta } ) = \frac { 3 5 } { 7 2 } a ( \bullet \dot { \zeta } ) = \frac { 3 5 } { 3 6 } b ( \bullet \dot { \zeta } ) = - \frac { 3 7 } { 7 2 } b ( \bullet \dot { \zeta } ) = - \frac { 1 } { 3 6 }$ $a ( \cdot \cdot , \cdot ) = \frac { 3 5 } { 7 2 }$ $b \Big ( \frac { 9 } { 9 } \Big ) = - \frac { 3 7 } { 7 2 }$

# 7.5.3 Diagonal Implicit R–K Method

<table><tr><td>1</td><td>1 4 0 1 1</td></tr><tr><td></td><td>2 4</td></tr><tr><td></td><td>1 1 2 2</td></tr></table>

$$
\begin{array} { l l l l } { a ( \bullet ) = 1 } & { a ( \bullet ) = 1 } & { b ( \bullet ) = 1 } & { b ( \bullet ) = 0 } \\ { a ( \bullet ^ { * } ) = \frac { 1 5 } { 1 6 } } & { a \big ( \bullet ^ { * } ) = \frac { 9 } { 8 } } & { b \big ( \bullet ^ { * } \big ) = - \frac { 1 } { 1 6 } } & { b \big ( \bullet ^ { * } \big ) = \frac { 1 } { 8 } } \\ { a ( \mathring { \mathbb { Y } } ) = \frac { 1 } { 2 } } & { a \big ( \overset { \bullet } { \underset {  } { \big { \big \wedge } } } \big ) = 1 } & { b \big ( \overset { \bullet } { \underset {  } { \big { \big \wedge } } } \big ) = 0 } & { b \big ( \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = 0 } \\ { a \big ( \bullet \overset { \bullet } { \underset {  } { \big { \big \wedge } } } \big ) = \frac { 3 } { 2 } } & { a \big ( \bullet \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = 3 } & { b \big ( \bullet \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = 0 } & { b \big ( \bullet \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = 0 } \\ { a \big ( \bullet \overset { \bullet } { \underset {  } { \big { \big \wedge } } } \big ) = \frac { 2 0 5 } { 2 5 6 } } & { a \big ( \bullet \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = \frac { 1 1 5 } { 1 2 8 } } & { b \big ( \bullet \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = - \frac { 5 1 } { 2 5 6 } } & { b \big ( \bullet \overset { \bullet } { \underset {  } { \big \wedge } } \big ) = - \frac { 1 3 } { 1 2 } } \end{array}
$$

$$
a ( \cdot \cdot \cdot ) = \frac { 6 5 } { 6 4 }
$$

$$
b \big ( \big < \big > \big ) = - \frac { 1 } { 6 4 }
$$

# 7.6 Multistep Symplectic Method

We present in this section Multistep method for Hamiltonian system.

# 7.6.1 Linear Multistep Method

Consider the autonomous ODEs on $\mathbf { R } ^ { n }$

$$
\frac { \mathrm { d } z } { \mathrm { d } t } = a ( z ) ,
$$

where $z = ( z _ { 1 } , \cdots , z _ { n } )$ and $a ( z ) = ( a _ { 1 } ( z ) , \cdots , a _ { n } ( z ) )$ is a smooth vector field on $\mathbf { R } ^ { n }$ . For Equations (6.1) we define a linear $m$ step method (LMM) in standard form by

$$
\sum _ { j = 0 } ^ { m } \alpha _ { j } z _ { j } = \tau \sum _ { j = 0 } ^ { m } \beta _ { j } Q _ { j } ,
$$

where $\alpha _ { j }$ and $\beta _ { j }$ are constants subject to the conditions

$$
\alpha _ { m } = 1 , \quad | \alpha _ { 0 } | + | \beta _ { 0 } | \neq 0 .
$$

If $m = 1$ , we call (6.2) a single step method. Otherwise, we call it a multi-step method. The linearity means that the right hand of (6.2) linearly depends on the value of $a ( z )$ on integral points. For compatibility of (6.2) with Equation (6.1), it must be of at least order one and thus satisfies

$$
\begin{array} { l } { \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { m } = 0 ; } \\ { \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { m } = \displaystyle \sum _ { j = 0 } ^ { m } j \alpha _ { j } \neq 0 . } \end{array}
$$

LMM method (6.2) has two characteristic polynomials

$$
\xi ( \lambda ) = \sum _ { i = 0 } ^ { m } \alpha _ { i } \lambda ^ { i } , \quad \sigma ( \lambda ) = \sum _ { i = 0 } ^ { m } \beta _ { i } \lambda ^ { i } .
$$

Equation (6.2) can be written as

$$
\xi ( E ) = \tau a ( \sigma ( E ) y _ { n } ) .
$$

In next subsection, we propose a new definition for symplectic multi-step methods. This new definition differs from the old ones given for the single step method. It is defined directly on $M$ which corresponds to the $m$ step scheme defined on $M$ , while the old definitions are given by defining a corresponding one step method on $M \times M \times \cdots \times M = M ^ { m }$ with a set of new variables. The new definition introduces a step transition operator $g : M \to M$ . Under our new definition, the leap-frog method is symplectic only for linear Hamiltonian systems. The transition operator $g$ will be constructed via continued fractions and rational approximation.

# 7.6.2 Symplectic LMM for Linear Hamiltonian Systems

First we consider a linear Hamiltonian system

$$
{ \frac { \mathrm { d } z } { \mathrm { d } t } } = a z ,
$$

where $a$ is an infinitesimal $2 n \times 2 n$ symplectic matrix $a \in s p ( 2 n )$ . Its phase flow is $z ( t ) = \exp { ( t a ) } z _ { 0 }$ . The LMM for (6.5) is

$$
\alpha _ { m } z _ { m } + \cdot \cdot \cdot + \alpha _ { 1 } z _ { 1 } + \alpha _ { 0 } z _ { 0 } = \tau a ( \beta _ { m } z _ { m } + \cdot \cdot \cdot + \beta _ { 1 } z _ { 1 } + \beta _ { 0 } z _ { 0 } ) .
$$

Our goal is to find a matrix $g$ , i.e., a linear transformation $g : \mathbf { R } ^ { 2 n } \to \mathbf { R } ^ { 2 n }$ which can satisfy (6.6)

$$
\alpha _ { m } g ^ { m } ( z _ { 0 } ) + \cdot \cdot \cdot + \alpha _ { 1 } g ( z _ { 0 } ) + \alpha _ { 0 } z _ { 0 } = \tau a \big ( \beta _ { m } g ^ { m } ( z _ { 0 } ) + \cdot \cdot \cdot + \beta _ { 1 } g ( z _ { 0 } ) + \beta _ { 0 } z _ { 0 } \big ) .
$$

Such a map $g$ exists for sufficiently small $\tau$ and can be represented by continued fractions and rational approximations. We call this transformation step transition operator[Fen98b] .

Definition 6.1. If $g$ is a symplectic transformation, then its corresponding LMM (6.6) is symplectic (we simply call the method SLMM).

From (6.7), we have

$$
\tau a = \frac { \alpha _ { 0 } I + \alpha _ { 1 } g ^ { 1 } + \cdot \cdot \cdot + \alpha _ { m } g ^ { m } } { \beta _ { 0 } I + \beta _ { 1 } g ^ { 1 } + \cdot \cdot \cdot + \beta _ { m } g ^ { m } } .
$$

The characteristic equation for LMM is

$$
\xi ( \lambda ) = \tau \mu \sigma ( \lambda ) ,
$$

where $\mu$ is the eigenvalue of the infinitesimal symplectic matrix $a$ and $\lambda$ is the eigenvalue of $g$ .

Let

$$
\psi ( \lambda ) = \frac { \xi ( \lambda ) } { \sigma ( \lambda ) } ,
$$

then (6.9) can be written as

$$
\tau \mu = \psi ( \lambda ) .
$$

Its inverse function is

$$
\lambda = \phi ( \tau \mu ) .
$$

To study the symplecticity of the LMM, one only needs to study the properties of functions $\phi$ and $\psi$ . We will see that if $\phi$ is of the exponential form or $\psi$ is of logarithmic form, the corresponding LMM is symplectic. We first study the properties of the exponential functions and logarithmic functions.

# Explike and loglike functions

First we describe the properties of exponential functions:

$$
\begin{array} { l } { \displaystyle \exp { ( x ) } | _ { x = 0 } = 1 . \qquad } \\ { \displaystyle \frac { \mathrm { d } } { \mathrm { d } x } \exp { ( x ) } | _ { x = 0 } = 1 . \qquad } \\ { \displaystyle \exp { ( x + y ) } = \exp { ( x ) } \cdot \exp { ( y ) } . } \end{array}
$$

If we substitute $y$ with $- x$ , we have

$$
\exp \left( x \right) \exp \left( - x \right) = 1 .
$$

Definition 6.2. If a function $\phi ( x )$ satisfies $\phi ( 0 ) = 1 , \phi ^ { \prime } ( 0 ) = 1$ and $\phi ( x ) \phi ( - x ) = 1$ , we call this function an explike function.

It is well known that the inverse function of an exponential function is a logarithmic function $x  \log ( x )$ . It has the following properties:

(1) log $x | _ { x = 1 } = 0$ ; (2) $\frac { \mathrm { d } } { \mathrm { d } x } \log x | _ { x = 1 } = 1 ;$ (3) $\log x y = \log x + \log y .$

If we take $y = { \frac { 1 } { x } }$ , we get

$$
\log x + \log { \frac { 1 } { x } } = 0 .
$$

Definition 6.3. If a function $\psi$ satisfies $\psi ( 1 ) = 0 , \psi ^ { \prime } ( 1 ) = 1$ , and

$$
\psi ( x ) + \psi \left( { \frac { 1 } { x } } \right) = 0 ,
$$

we call it a loglike function.

Obviously, polynomials can not be explike functions or loglike functions, so we try to find explike and loglike functions in the form of rational functions.

Theorem 6.4. [Fen98b] LMM is symplectic for linear Hamiltonian systems iff its step transition operator $g = \phi ( \tau a )$ is explike, i.e., $\phi ( \mu ) \cdot \phi ( - \mu ) = 1$ , $\phi ( 0 ) = 1$ , $\phi ^ { \prime } ( 0 ) = 1$ .

Theorem 6.5. [Fen98b] LMM is symplectic for linear Hamiltonian systems iff $\psi ( \lambda ) =$ $\frac { \xi ( \lambda ) } { \sigma ( \lambda ) }$ is $a$ loglike function, i.e., $\psi ( \lambda ) + \psi \Big ( \frac { 1 } { \lambda } \Big ) = 0 , \psi ( 1 ) = 0 , \psi ^ { \prime } ( 1 ) = 1 .$

Proof. From Theorem 6.4, we have $\phi ( \mu ) \phi ( - \mu ) = 1$ , so $\lambda = \phi ( \mu )$ , ${ \frac { 1 } { \lambda } } = \phi ( - \mu )$ . The inverse function of $\phi$ satisfies $\psi ( \lambda ) = \mu$ , $\psi \left( { \frac { 1 } { \lambda } } \right) = - \mu$ , i.e., $\psi ( \lambda ) + \psi \left( { \frac { 1 } { \lambda } } \right) = 0 .$ , $\psi ( 1 ) = 0 , \psi ^ { \prime } ( 1 ) = 1$ follows from consistency condition (1), (2).

On the other side, if $\psi ( \lambda ) = - \psi \left( \frac { 1 } { \lambda } \right)$ , let $\psi ( \lambda ) = \mu$ , then its inverse function is $\phi ( \mu ) = \lambda$ and $\phi ( - \mu ) = \frac { 1 } { \lambda }$ , we then have $\phi ( \mu ) \cdot \phi ( - \mu ) = 1$ .

Theorem 6.6. If $\xi ( \lambda )$ is a antisymmetric polynomial, $\sigma ( \lambda )$ is $a$ symmetric one, then $\psi ( \lambda ) = { \frac { \xi ( \lambda ) } { \sigma ( \lambda ) } }$ , satisfies

$$
\psi ( 1 ) = 0 , \psi \left( { \frac { 1 } { \lambda } } \right) + \psi ( \lambda ) = 0 .
$$

Proof. Since

$$
\begin{array} { l } { { \displaystyle \bar { \xi } ( \lambda ) = \lambda ^ { m } \xi \Big ( \frac { 1 } { \lambda } \Big ) = \sum _ { i = 0 } ^ { m } a _ { m - i } \lambda ^ { i } = - \sum _ { i = 1 } ^ { m } a _ { i } \lambda ^ { i } = - \xi ( \lambda ) , } } \\ { { \displaystyle \overline { { \sigma } } ( \lambda ) = \lambda ^ { m } \sigma \Big ( \frac { 1 } { \lambda } \Big ) = \sum _ { i = 0 } ^ { m } \beta _ { m - i } \lambda ^ { i } = \sum _ { i = 1 } ^ { m } \beta _ { i } \lambda ^ { i } = \sigma ( \lambda ) , } } \\ { { \displaystyle \psi ( \lambda ) = \frac { \xi ( \lambda ) } { \sigma ( \lambda ) } , \quad \psi \Big ( \frac { 1 } { \lambda } \Big ) = \frac { \xi \Big ( \frac { 1 } { \lambda } \Big ) } { \sigma \Big ( \frac { 1 } { \lambda } \Big ) } = \frac { \lambda ^ { m } \xi \Big ( \frac { 1 } { \lambda } \Big ) } { \lambda ^ { m } \sigma \Big ( \frac { 1 } { \lambda } \Big ) } = \frac { - \xi ( \lambda ) } { \sigma ( \lambda ) } , } } \end{array}
$$

we obtain $\lambda ) + \psi \Big ( \frac { 1 } { \lambda } \Big ) = 0 . \operatorname { N o w } \xi ( 1 ) = \sum _ { k = 0 } ^ { m } \alpha _ { k } = 0 , \sigma ( 1 ) = \sum _ { k = 0 } ^ { m } \beta _ { k } \neq 0 ,$ , then $\psi ( 1 ) = \frac { \xi ( 1 ) } { \sigma ( 1 ) } = 0 .$

Corollary 6.7. If above generating polynomial is consistent with $O D E ( 6 . 1 )$ , then $\psi ( \lambda )$ is loglike function, i.e., $\psi \left( { \frac { 1 } { \lambda } } \right) + \psi ( \lambda ) = 0$ , $\psi ( 1 ) = 0$ , $\dot { \psi } ( 1 ) = 1$ .

Proof. $\psi ^ { \prime } ( 1 ) = \frac { \dot { \xi } \sigma - \dot { \xi } \xi } { \sigma ^ { 2 } } = \frac { \dot { \xi } ( 1 ) } { \sigma ( 1 ) } = 1$ . This condition is just consistence condition. -

Theorem 6.8. Let $\psi ( \lambda ) = { \frac { \xi ( \lambda ) } { \sigma ( \lambda ) } }$ irreducible loglike function, then $\xi ( \lambda )$ is an antisymmetric polynomial while $\sigma ( \lambda )$ is a symmetric one.

Proof. We write formally

$$
\begin{array} { l } { { \xi ( \lambda ) = \alpha _ { m } \lambda ^ { m } + \alpha _ { m - 1 } \lambda ^ { m - 1 } + \cdot \cdot \cdot + \alpha _ { 1 } \lambda + \alpha _ { 0 } , } } \\ { { \nonumber } } \\ { { \sigma ( \lambda ) = \beta _ { m } \lambda ^ { m } + \beta _ { m - 1 } \lambda ^ { m - 1 } + \cdot \cdot \cdot + \beta _ { 1 } \lambda + \beta _ { 0 } . } } \end{array}
$$

If $\deg \xi ( \lambda ) = p < m$ , set $a _ { i } = 0$ for $i > p$ ; if $\deg \sigma ( \lambda ) = q < m$ , set $\beta _ { i } = 0$ for $i > q . \psi ( 1 ) = 0 \Rightarrow \xi ( 1 ) = 0$ , since otherwise, if $\xi ( 1 ) \neq 0$ , then $\psi ( 1 ) = { \frac { \xi ( 1 ) } { \sigma ( 1 ) } } \neq 0$ Now $\xi ( 1 ) = 0 \Leftrightarrow \sigma ( 1 ) \neq 0$ , since otherwise $\xi ( 1 ) = \sigma ( 1 ) \Rightarrow \xi ( \lambda ) .$ , $\sigma ( \lambda )$ would have common factor. So we have

$$
\begin{array} { c } { { \displaystyle \xi ( 1 ) = \sum _ { k = 0 } ^ { m } \alpha _ { k } = \sum _ { k = 0 } ^ { p } \alpha _ { k } = 0 , } } \\ { { \displaystyle \sigma ( 1 ) = \sum _ { k = 0 } ^ { m } \beta _ { k } = \sum _ { k = 0 } ^ { q } \beta _ { k } \neq 0 . } } \end{array}
$$

If $m = \deg \xi = p$ , then $\begin{array} { r } { a _ { m } = a _ { p } \neq 0 . } \end{array}$ . If $m = \deg \sigma = q$ , then $\beta _ { m } = \beta _ { p } \neq 0$

$$
\psi \left( \frac { 1 } { \lambda } \right) = \frac { \xi \left( \displaystyle \frac { 1 } { \lambda } \right) } { \sigma \left( \displaystyle \frac { 1 } { \lambda } \right) } = \frac { \lambda ^ { m } \xi \left( \displaystyle \frac { 1 } { \lambda } \right) } { \lambda ^ { m } \sigma \left( \displaystyle \frac { 1 } { \lambda } \right) } = \frac { \bar { \xi } ( \lambda ) } { \overline { { \sigma } } ( \lambda ) } .
$$

Since $\psi ( \lambda ) + \psi \left( { \frac { 1 } { \lambda } } \right) = 0$ , we have

$$
\begin{array} { r c l } { { \displaystyle \frac { \xi ( \lambda ) } { \sigma ( \lambda ) } = - \frac { \overline { { { \xi } } } ( \lambda ) } { \overline { { { \sigma } } } ( \lambda ) } \longleftrightarrow \xi ( \lambda ) \overline { { { \sigma } } } ( \lambda ) = - \overline { { { \xi } } } ( \lambda ) \sigma ( \lambda ) } } \\ { { \displaystyle \implies \xi ( \lambda ) \vert \overline { { { \xi } } } ( \lambda ) \sigma ( \lambda ) \mathrm { a n d } \sigma ( \lambda ) \vert \overline { { { \sigma } } } ( \lambda ) \xi ( \lambda ) . } } \end{array}
$$

Since $\xi ( \lambda ) , ~ \sigma ( \lambda )$ have no common factor, then $\xi ( \lambda ) | \overline { { { \xi } } } ( \lambda ) , ~ \sigma ( \lambda ) | \overline { { { \sigma } } } ( \lambda )$ . If $\begin{array} { r l } { m } & { { } = } \end{array}$ $\deg \xi ( \lambda ) \Rightarrow \deg \overline { { \xi } } \leq \deg \xi \Rightarrow \exists c$ ,

$$
\xi ( \lambda ) = c \overline { { { \xi } } } ( \lambda ) \Longrightarrow \sigma ( \lambda ) = - c \overline { { { \sigma } } } ( \lambda ) .
$$

Since $\alpha _ { m } \neq 0 \Rightarrow \alpha _ { m } \lambda ^ { m } + \alpha _ { m - 1 } \lambda ^ { m - 1 } + \cdot \cdot \cdot + \alpha _ { 0 } = c ( \alpha _ { m } + \cdot \cdot \cdot + \alpha _ { 0 } w ^ { n } ) \Rightarrow \alpha _ { m } =$ $c \alpha _ { 0 }$ $, \alpha _ { 0 } = c \alpha _ { m } \Leftrightarrow \alpha _ { m } = c ^ { 2 } \alpha _ { m }$ , therefore $c ^ { 2 } = 1 , c = \pm 1$ . Suppose $c = + 1$ , then

$\sigma ( \lambda ) = - \bar { \sigma } ( \lambda ) , \mathrm { a n d } \sum _ { k = 0 } ^ { m } \beta _ { k } = \sigma ( 1 ) , \mathrm { t h e n } - \bar { \sigma } ( 1 ) = \sigma ( 1 ) \Leftrightarrow \sigma ( 1 ) = 0 ,$ which leads to a contradiction with the assumption $\sigma ( 1 ) \neq 0$ . Therefore $c = - 1$ , i.e.,

$$
\begin{array} { l l l l } { { \xi ( \lambda ) = - \tilde { \xi } ( \lambda ) , \quad } } & { { \alpha _ { j } = - \alpha _ { m - j } , \quad } } & { { j = 0 , 1 , \cdot \cdot \cdot , m , } } \\ { { \sigma ( \lambda ) = \tilde { \sigma } ( \lambda ) , \quad } } & { { \beta _ { j } = \beta _ { m - j } , \quad } } & { { j = 0 , 1 , \cdot \cdot \cdot , m . } } \end{array}
$$

The theorem is proved.

The proof for the case $m = \deg \sigma ( \lambda )$ proceeds in exactly the same manner as above.

# 7.6.3 Rational Approximations to Exp and Log Function

# 1. Leap-frog scheme

We first study a simple example:

$$
z _ { 2 } = z _ { 0 } + 2 \tau a z _ { 1 } .
$$

Let $z _ { 1 } = c z _ { 0 }$ , then $z _ { 0 } = c ^ { - 1 } z _ { 1 }$ , insert this equation into (6.16),we get

$$
z _ { 2 } = 2 \tau a z _ { 1 } + { \frac { 1 } { c } } z _ { 1 } = \left( 2 \tau a + { \frac { 1 } { c } } \right) z _ { 1 } = d _ { 1 } z _ { 1 } , \qquad z _ { 1 } = { \frac { 1 } { 2 \tau a + { \frac { 1 } { c } } } } z _ { 2 } = { \frac { z _ { 2 } } { d _ { 1 } } } ,
$$

$$
z _ { 3 } = z _ { 1 } + 2 \tau a z _ { 2 } = \left( 2 \tau a + \frac { 1 } { 2 \tau a + \displaystyle \frac { 1 } { c } } \right) z _ { 2 } = d _ { 2 } z _ { 2 } , \quad z _ { 2 } = \displaystyle \frac { 1 } { 2 \tau a + \displaystyle \frac { 1 } { 2 \tau a + \displaystyle \frac { 1 } { c } } } z _ { 3 } ,
$$

$$
z _ { 4 } = \left( 2 \tau a + { \frac { 1 } { 2 \tau a + { \frac { 1 } { 2 \tau a + { \frac { 1 } { c } } } } } } \right) = d _ { 4 } z _ { 3 } , \quad \cdot \cdot \cdot .
$$

Where $d _ { k }$ can be written in the form of continued fractions

$$
\begin{array} { l } { { d _ { k } = 2 \tau a + \displaystyle \frac 1 { 2 \tau a } + \displaystyle \frac 1 { 2 \tau a } + \cdot \cdot \cdot + \displaystyle \frac 1 { 2 \tau a } + \cdot \cdot \cdot \cdot } } \\ { { \displaystyle \operatorname* { l i m } _ { k \to \infty } \mathrm { d } _ { k } = g = \tau a + \sqrt { 1 + ( \tau a ) ^ { 2 } } . } } \end{array} ,
$$

We assume the transition operator of Leap-frog to be $g$ , from (6.16) we have

$$
g ^ { 2 } - 1 = 2 \tau a g ,
$$

now we have $g = \tau a \pm \sqrt { 1 + ( \tau a ) ^ { 2 } }$ . Here only sign $^ +$ is meaningful, thus $g \ : = \ :$ $\tau a + \sqrt { 1 + ( \tau a ) ^ { 2 } }$ which is just the limit of continued fraction (6.17). It is easy to verify that $g$ is explike, i.e., $g ( \mu ) g ( - \mu ) = 1$ . So the Leap-frog scheme is symplectic for linear Hamiltonian systems according to our new definition.

# 2. Exponential function

$$
\exp ( z ) = 1 + \sum _ { k = 1 } ^ { \infty } { \frac { z ^ { k } } { k ! } } .
$$

We have Lagrange’s continued function

$$
{ \begin{array} { l } { \displaystyle \exp \left( z \right) ~ = ~ 1 + { \frac { z } { 1 + { \cfrac { - z } { 2 + \ddots + + } } } } { \cfrac { z } { 2 n - 1 } } + { \cfrac { - z } { 2 + \cdot \cdot \cdot } } } \\ { ~ = ~ b _ { 0 } + { \cfrac { a _ { 1 } } { b _ { 1 } } } + { \cfrac { a _ { 2 } } { b _ { 2 } } } + \cdot \cdot \cdot + { \cfrac { a _ { 2 n - 1 } } { b _ { 2 n - 1 } } } + { \cfrac { a _ { 2 n } } { b _ { 2 n } } } + \cdot \cdot \cdot } \end{array} } ,
$$

where

$$
\begin{array} { l l } { { a _ { 1 } = z , \ a _ { 2 } = - z , \ \cdots , \ a _ { 2 n - 1 } = z , \ a _ { 2 n } = - z , } } & { { \ n \geq 1 , } } \\ { { b _ { 0 } = 1 , \ b _ { 1 } = 1 , \ b _ { 2 } = 2 , \ \cdots , \ b _ { 2 n - 1 } = 2 n - 1 , \ b _ { 2 n } = 2 , } } & { { \ n \geq 1 , } } \end{array}
$$

and Euler’s contract expansion

$$
\begin{array} { r c l } { \displaystyle \exp \left( z \right) } & { = } & { 1 + \displaystyle \frac { 2 z } { 2 - z } \frac { z ^ { 2 } } { 6 } + \cdot \cdot \cdot + \overline { { { 2 ( 2 n - 1 ) } } } + \cdot \cdot \cdot } \\ { \displaystyle } & { = } & { { \cal B } _ { 0 } + \displaystyle \frac { A _ { 1 } } { B _ { 1 } } + \frac { A _ { 2 } } { B _ { 2 } } + \cdot \cdot \cdot + \overline { { { B _ { n } } } } + \cdot \cdot \cdot } \end{array}
$$

where

$$
\begin{array} { r l r } & { A _ { 1 } = 2 z , \ A _ { 2 } = z ^ { 2 } , \cdots , \ A _ { n } = z ^ { 2 } , } & { \quad n \ge 2 , } \\ & { B _ { 0 } = 1 , \ B _ { 1 } = 2 - z , \ B _ { 2 } = 6 , \ \cdots , \ B _ { n } = 2 ( 2 n - 1 ) , } & { \quad n \ge 2 . } \end{array}
$$

We have

$$
\begin{array} { l l l } { { \displaystyle { \frac { P _ { 0 } } { Q _ { 0 } } } = \frac { p _ { 0 } } { q _ { 0 } } = 1 , } } & { { \displaystyle { \frac { p _ { 1 } } { q _ { 1 } } } = \frac { 1 + z } { 1 } , } } & { { \displaystyle { \frac { p _ { 2 } } { q _ { 2 } } } = \frac { P _ { 1 } } { Q _ { 1 } } = \frac { 2 + z } { 2 - z } , } } \\ { { \displaystyle { \frac { p _ { 3 } } { q _ { 3 } } } = \frac { 6 + 4 z + z ^ { 2 } } { 6 - 2 z } , } } & { { \displaystyle { \frac { p _ { 4 } } { q _ { 4 } } } = \frac { P _ { 2 } } { Q _ { 2 } } = \frac { 1 2 + 6 z + z ^ { 2 } } { 1 2 - 6 z + z ^ { 2 } } + \cdots . } } \end{array}
$$

In general $p _ { 2 n - 1 } ( z )$ is a polynomial of degree $n , q _ { 2 n - 1 }$ is a polynomial of degree $n { - } 1$ , so $\frac { p _ { 2 n - 1 } } { q _ { 2 n - 1 } }$ is not explike. While $p _ { 2 n } = P _ { n } ( x )$ , $q _ { 2 n } = Q _ { n } ( x )$ are both polynomials of degree $n$ and from the recursions

$$
\begin{array} { l l l } { { P _ { 0 } = 1 , \quad } } & { { P _ { 1 } = 2 + z , \quad } } & { { P _ { n } = z ^ { 2 } P _ { n - 2 } + 2 ( 2 n - 1 ) P _ { n - 1 } , } } \\ { { Q _ { 0 } = 1 , \quad } } & { { Q _ { 1 } = 2 - z , \quad } } & { { Q _ { n } = z ^ { 2 } Q _ { n - 2 } + 2 ( 2 n - 1 ) Q _ { n - 1 } . } } \end{array}
$$

It’s easy to see that for $n = 0 , 1 , \cdots$ ,

$$
Q _ { n } ( z ) = P _ { n } ( - z ) , \quad P _ { n } ( 0 ) > 0 .
$$

So the rational function

$$
\phi _ { n } ( z ) = { \frac { P _ { n } ( z ) } { Q _ { n } ( z ) } } = { \frac { P _ { n } ( z ) } { P _ { n } ( - z ) } }
$$

is explike and

$$
\phi _ { n } ( z ) - \exp ( z ) = o ( | z | ^ { 2 n + 1 } ) ,
$$

where

$$
P _ { 0 } = 1 , \quad P _ { 1 } = 2 + z , \quad P _ { n } ( z ) = z ^ { 2 } P _ { n - 2 } ( z ) + 2 ( 2 n - 1 ) P _ { n - 1 } ( z ) , \quad n \geq 2 .
$$

This is just the diagonal Pade approximation. ´

# 3. Logarithmic function

$$
\log w = \sum _ { k = 1 } ^ { \infty } { \frac { ( w - 1 ) ^ { k } } { k w ^ { k } } } ,
$$

we have the Lagrange’s continued fraction

$$
\begin{array} { r c l } { { \log w } } & { { = } } & { { \displaystyle \frac { w - 1 } { 1 } + \frac { w - 1 } { 2 } + \frac { w - 1 } { 3 } + \frac { 2 ( w - 1 ) } { 2 } + \ldots + \frac { ( n - 1 ) ( w - 1 ) } { 2 n - 1 } + \frac { n ( w - 1 ) } { 2 } + \ldots } } \\ { { } } & { { = } } & { { \displaystyle \frac { a _ { 1 } } { b _ { 1 } } + \frac { a _ { 2 } } { b _ { 2 } } \frac { a _ { 3 } } { + b _ { 3 } } \frac { a _ { 4 } } { b _ { 4 } } + \ldots + \frac { a _ { 2 n - 1 } } { b _ { 2 n - 1 } } \frac { a _ { 2 n } } { b _ { 2 n } } + \ldots , } } \end{array} ( 6 .
$$

where

$$
\begin{array} { r l } & { a _ { 1 } = w - 1 , \quad a _ { 2 } = w - 1 , \quad a _ { 3 } = w - 1 , \quad a _ { 4 } = 2 ( w - 1 ) , \quad \cdots , } \\ & { b _ { 0 } = 0 , \quad b _ { 1 } = 1 , \quad b _ { 2 } = 2 , \quad b _ { 3 } = 3 , \quad b _ { 4 } = 2 , \quad \cdots , } \end{array}
$$

and

$$
\begin{array} { l l l } { { a _ { 2 n - 1 } = ( n - 1 ) ( w - 1 ) , } } & { { a _ { 2 n } = n ( w - 1 ) , } } & { { n \geq 2 , } } \\ { { b _ { 2 n - 1 } = 2 n - 1 , } } & { { b _ { 2 n } = 2 , } } & { { n \geq 2 , } } \end{array}
$$

and the Euler’s contracted expansion

$$
\begin{array} { r l r } { \log w } & { = } & { \displaystyle { \frac { 2 ( w - 1 ) } { w + 1 } } \displaystyle { \frac { 2 ( w - 1 ) } { - 6 ( w + 1 ) - } \frac { \big ( 2 \times 2 ( w - 1 ) \big ) ^ { 2 } } { 2 . 5 ( w + 1 ) } } - \cdots - \frac { \Big ( 2 ( n - 1 ) ( w - 1 ) \Big ) ^ { 2 } } { 2 ( 2 n - 1 ) ( w + 1 ) } } \\ & { } & { \displaystyle \phantom { \frac { 1 } { ( w + 1 ) } } = \displaystyle { \frac { A _ { 1 } } { B _ { 1 } } } \displaystyle { \frac { A _ { 2 } } { B _ { 2 } } } \displaystyle { \frac { A _ { 3 } } { B _ { 3 } + \cdots + } \frac { A _ { n } } { B _ { n } } } + \cdots \quad ( 6 . 5 ( w + 1 ) ) ^ { 2 } } \end{array}
$$

where

$$
\begin{array} { r l r l } & { A _ { 1 } = 2 ( w - 1 ) , \quad A _ { 2 } = - 2 ( w - 1 ) , \ : \cdots , A _ { n } = - ( 2 ( n - 1 ) ( w - 1 ) ) ^ { 2 } , } & & { n \geq 3 , } \\ & { B _ { 0 } = 0 , \ : B _ { 1 } = w + 1 , \ : B _ { 2 } = 6 ( w + 1 ) , \ : \cdots , \ : B _ { n } = 2 ( 2 n - 1 ) ( w + 1 ) , } & & { n \geq 2 . } \end{array}
$$

The following can be obtained by recursion

$$
\begin{array} { r l } & { \frac { P _ { 0 } } { Q _ { 0 } } = \frac { p _ { 0 } } { q _ { 0 } } = 0 , \quad \frac { p _ { 1 } } { q _ { 1 } } = w - 1 , \quad \frac { p _ { 2 } } { q _ { 2 } } = \frac { P _ { 1 } } { Q _ { 1 } } = \frac { 2 ( w - 1 ) } { w + 1 } , } \\ & { \frac { p _ { 3 } } { q _ { 3 } } = \frac { w ^ { 2 } + 4 w - 5 } { 4 w + 2 } , \quad \frac { p _ { 4 } } { q _ { 4 } } = \frac { P _ { 2 } } { Q _ { 2 } } = \frac { 3 ( w ^ { 2 } - 1 ) } { w ^ { 2 } + 4 w + 1 } . } \end{array}
$$

In general

$$
\begin{array} { r } { \frac { p _ { 2 n - 1 } ( w ) } { q _ { 2 n - 1 } ( w ) } - \log { ( w ) } = O \left( | w - 1 | ^ { 2 n } \right) , \quad \frac { p _ { 2 n } ( w ) } { q _ { 2 n } ( w ) } - \log { ( w ) } = O \left( | w - 1 | ^ { 2 n + 1 } \right) . } \end{array}
$$

The rational function $\frac { p _ { 2 n - 1 } ( w ) } { q _ { 2 n - 1 } ( w ) }$ approximates log w only by odd order 2n − 1, it does not reach the even order $2 n$ , and is not loglike. However

$$
R _ { n } = \psi _ { n } ( w ) = { \frac { p _ { 2 n } ( w ) } { q _ { 2 n } ( w ) } } = { \frac { P _ { n } ( w ) } { Q _ { n } ( w ) } }
$$

is a loglike function. In fact, by recursion, it’s easy to see that

$$
\begin{array} { l } { \displaystyle P _ { n } ( w ) = - w ^ { n } P _ { n } \bigg ( \frac { 1 } { w } \bigg ) , } \\ { \displaystyle Q _ { n } ( w ) = w ^ { n } Q _ { n } \bigg ( \frac { 1 } { w } \bigg ) , } \end{array}
$$

and $\forall n$ , $Q _ { n } ( 1 ) \neq 0 .$ We also have

$$
\begin{array} { l l l } { { P _ { 0 } = 0 , } } & { { P _ { 1 } ( w ) = 2 ( w - 1 ) , } } & { { P _ { 2 } ( w ) = 3 ( w ^ { 2 } - 1 ) , } } \\ { { Q _ { 0 } = 1 , } } & { { Q _ { 1 } ( w ) = w + 1 , } } & { { Q _ { 2 } ( w ) = w ^ { 2 } + 4 w + 1 , } } \end{array}
$$

and for $n \geq 3$

$$
\begin{array} { l l } { P _ { n } ( w ) = - ( 2 ( n - 1 ) ( w - 1 ) ^ { 2 } P _ { n - 2 } ( w ) + 2 ( 2 n - 1 ) ( w - 1 ) P _ { n - 2 } ( w ) ) , } \\ { Q _ { n } ( w ) = - ( ( 2 n - 1 ) ( w - 1 ) ^ { 2 } Q _ { n - 2 } ( w ) + 2 ( 2 n - 1 ) ( w - 1 ) Q _ { n - 2 } ( w ) ) . } \end{array}
$$

So we see $R _ { 1 } ( \lambda )$ is just the Euler midpoint rule and $R _ { 2 } ( \lambda ) = \frac { 3 ( \lambda ^ { 2 } - 1 ) } { \lambda ^ { 2 } + 4 \lambda + 1 }$ is just the Simpson scheme.

Conclusion: The odd truncation of the continued fraction of the Lagrange’s approximation to $\exp ( x )$ and $\log \left( x \right)$ is neither explike nor loglike, while the even truncation is explike and loglike. The truncation of the continued fraction obtained from Euler’s contracted expansion is explike and loglike.

# 4. Obreschkoff formula

Another rational approximation to a given function is the Obreschkoff formula[Obr40] :

$$
\begin{array} { r l r } { { \displaystyle R _ { m , n } ( x ) } } & { { = } } & { { \displaystyle \sum _ { k = 0 } ^ { n } \frac { \mathrm { C } _ { n } ^ { k } } { \mathrm { C } _ { m + n } ^ { k } k ! } ( x _ { 0 } - x ) ^ { k } f ^ { ( k ) } ( x ) - \sum _ { k = 0 } ^ { m } \frac { \mathrm { C } _ { m } ^ { k } } { \mathrm { C } _ { m + n } ^ { k } k ! } ( x - x _ { 0 } ) ^ { k } f ^ { ( k ) } ( x _ { 0 } ) } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { ( m + n ) ! } \int _ { x _ { 0 } } ^ { x } ( x - t ) ^ { m } ( x _ { 0 } - t ) ^ { n } f ^ { m + n + 1 } ( t ) \mathrm { d } t . } } \end{array}
$$

(1) Take $f ( x ) = \mathbf { e } ^ { x } , x _ { 0 } = 0$ , we obtain Pade approximation ´ $\exp ( x ) \doteq R _ { m , n } ( x )$ . If $m = n$ , we obtain Pade approximation ´ $R _ { m , m } ( x )$ .

(2) Take $f ( x ) = \log ( x ) , x _ { 0 } = 1$ , we obtain $\log ( x ) \doteq R _ { m , n } ( x )$ . If $m = n$ , we obtain loglike function $R _ { m } ( x )$ ,

$$
R _ { m } ( \lambda ) = \frac { 1 } { \lambda ^ { m } } \sum _ { k = 1 } ^ { m } \frac { { \bf C } _ { m } ^ { k } } { { \bf C } _ { 2 m } ^ { k } k } ( \lambda - 1 ) ^ { k } ( \lambda ^ { m - k } + ( - 1 ) ^ { k - 1 } \lambda ^ { m } ) ,
$$

i.e.,

$$
R _ { m } ( \lambda ) + R _ { m } \left( \frac { 1 } { \lambda } \right) = 0 .
$$

We have

$$
\begin{array} { l } { { R _ { m } ( \lambda ) - \log { ( \lambda ) } = O \left( | \lambda | ^ { 2 m + 1 } \right) , } } \\ { { R _ { 1 } = \displaystyle \frac { \lambda ^ { 2 } - 1 } { 2 \lambda } , } } \\ { { R _ { 2 } = \displaystyle \frac { 1 } { 1 2 \lambda ^ { 2 } } ( - \lambda ^ { 4 } + 8 \lambda ^ { 3 } - 8 \lambda + 1 ) , } } \\ { { R _ { 3 } = \displaystyle \frac { 1 } { 6 0 \lambda ^ { 3 } } ( \lambda ^ { 6 } - 9 \lambda ^ { 5 } + 4 5 \lambda ^ { 4 } - 4 5 \lambda ^ { 2 } + 9 \lambda - 1 ) , } } \\ { { . . . } } \end{array}
$$

where $R _ { 1 } ( \lambda )$ is just the leap-frog scheme.

# 5. Nonexistence of SLMM for Nonlinear Hamiltonian Systems (Tang Theorem)

For nonlinear Hamiltonian systems, there exists no symplectic LMM. When equation (6.1) is nonlinear, how to define a symplectic LMM? The answer is to find the step-transition operator $g : \mathbf { R } ^ { n }  \mathbf { R } ^ { n }$ , let

$$
{ \begin{array} { r l } & { z = g ^ { 0 } ( z ) , } \\ & { z _ { 1 } = g ( x ) , } \\ & { z _ { 2 } = g ( g ( z ) ) = g \circ g ( z ) = g ^ { 2 } ( z ) , } \\ & { \quad \vdots } \\ & { z _ { n } = g ( g ( \cdot \cdot ( g ( z ) ) \cdot \cdot \cdot ) ) = g \circ g \circ \cdot \cdot \cdot \circ g \circ ( z ) = g ^ { n } ( z ) , } \end{array} }
$$

we get from (6.2)

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } g ^ { i } ( z ) = \tau \sum _ { i = 0 } ^ { n } \beta _ { i } f \circ g ^ { i } ( z ) .
$$

It’s easy to prove that if LMM (6.33) is consistent with Equation (6.1), then for smooth $f$ and sufficiently small step-size $\tau$ , the operator $g$ defined by (6.32) exists and it can be represented as a power series in $\tau$ and with first term equal to identity. Consider a case where Equation (6.1) is a Hamiltonian system, i.e., $\boldsymbol { a } ( z ) = J \nabla H ( z )$ , we have the following definition.

Definition 6.9. LMM is symplectic if the transition operator $g$ defined by (6.32) is symplectic for all $H ( z )$ and all step-size $\tau$ , i.e.,

$$
g _ { * } ^ { \mathrm { T } } J g _ { * } ( z ) = J .
$$

This definition is a completely different criterion that can include the symplectic condition for one-step methods in the usual sense. But Tang $\mathrm { i n } ^ { [ \mathrm { T a n 9 3 a } ] }$ has proved that nonlinear multistep method can satisfy such a strict criterion. Numerical experiments of $\mathrm { L i } ^ { [ \mathrm { F e n 9 2 b } ] }$ show that the explicit 3-level centered method (Leap-frog method) is symplectic for linear Hamiltonian systems $H = \frac { 1 } { 2 } ( p ^ { 2 } + 4 q ^ { 2 } )$ (see Fig. 0.2 in introduction of this book) but is non-symplectic for nonlinear Hamiltonian systems $H = { \frac { 1 } { 2 } } ( p ^ { 2 } + q ^ { 2 } ) + { \frac { 2 } { 3 } } q ^ { 4 }$ + 23 q4 (see Fig. 0.3 (a,b,c) in introduction of this book).

# Bibliography

[AS93] L. Abia and J.M. Sanz-Serna: Partitioned Runge–Kutta methods for separable Hamiltonian problems. Math. Comp., 60:617–634, (1993).   
[But87] J.C. Butcher: The Numerical Analysis of Ordinary Differential Equations. John Wiley, Chichester, (1987).   
[CH95] M.P. Calvo and E. Hairer: Further reduction in the number of independent order conditions for symplectic, explicit partitioned Runge-Kutta and Runge–Kutta–Nystrom methods. ¨ Appl. Numer. Math., 18:107–114, (1995).   
[Chi97] S. A. Chin: Symplectic integrators from composite operator factorization. Physics Letters A, 226:344–348, (1997).   
[Coo87] G. J. Cooper: Stability of Runge–Kutta methods for trajectory problems. IMA J. Numer. Anal., 7:1–13, (1987).   
[CS93] M.P. Calvo and J.M. Sanz-Serna: High-order symplectic Runge-Kutta-Nystrom meth- ¨ ods. SIAM J. Sci. Comput., 114:1237–1252, (1993).   
[CS94] M.P. Calvo and J.M. Sanz-Serna: Canonical B-Series. Numer. Math., 67:161–175, (1994).   
[DV84] K. Dekker and J.G. Verwer: Stability of Runge-Kutta Methods for Stiff Initial Value Problems. North-Holland, Amsterdam, (1984).   
[Fen65] K. Feng: Difference schemes based on variational principle. J. of Appl. and Comput. Math.in Chinese, 2(4):238–262, (1965).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen86a] K. Feng: Canonical Difference Schemes for Hamiltonian Canonical Differential Equations. In International Workshop on Applied Differential Equations (Beijing, 1985), pages 59–73. World Sci. Publishing, Singapore, (1986).   
[Fen86b] K. Feng: Difference schemes for Hamiltonian formalism and symplectic geometry. J. Comput. Math., 4:279–289, (1986).   
[Fen86c] K. Feng: Symplectic geometry and numerical methods in fluid dynamics. In F.G. Zhuang and Y.L. Zhu, editors, Tenth International Conference on Numerical Methods in Fluid Dynamics, Lecture Notes in Physics, pages 1–7. Springer, Berlin, (1986).   
[Fen91] K. Feng: The Hamiltonian Way for Computing Hamiltonian Dynamics. In R. Spigler, editor, Applied and Industrial Mathematics, pages 17–35. Kluwer, The Netherlands, (1991).   
[Fen92a] K. Feng: Formal power series and numerical methods for differential equations. In T. Chan and Z.C. Shi, editors, International conf. on scientific computation, pages 28–35. World Scientific, Singapore, (1992).   
[Fen92b] K. Feng: How to compute property Newton’s equation of motion. In L. A. Ying, B.Y. Guo, and I. Gladwell, editors, Proc of 2nd Conf. on Numerical Method for PDE’s, pages 15–22.World Scientific, Singapore, (1992). Also see Collected Works of Feng Kang. Volume I, II. National Defence Industry Press, Beijing, (1995).   
[Fen93a] K. Feng: Formal dynamical systems and numerical algorithms. In K. Feng and Z.C Shi, editors, International conf. on computation of differential equationsand dynamical systems, pages 1–10. World Scientific, Singapore, (1993).   
[Fen93b] K. Feng: Symplectic, contact and volume preserving algorithms. In Z.C. Shi and T. Ushijima, editors, Proc.1st China-Japan conf. on computation of differential equationsand dynamical systems, pages 1–28. World Scientific, Singapore, (1993).   
[Fen95] K. Feng: Collected Works of Feng Kang. volume I,II. National Defence Industry Press, Beijing, (1995).   
[Fen98a] K. Feng: The calculus of generating functions and the formal energy for Hamiltonian systems. J. Comput. Math., 16:481–498, (1998).   
[Fen98b] K. Feng: The step-transition operator for multi-step methods of ODEs. J. Comput. Math., 16(3), (1998).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FQ91a] K. Feng and M.Z. Qin: Hamiltonian Algorithms for Hamiltonian Dynamical Systems. Progr. Natur. Sci., 1(2):105–116, (1991).   
[FQ91b] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FQ03] K. Feng and M. Q. Qin: Symplectic Algorithms for Hamiltonian Systems. Zhejiang Science and Technology Publishing House, Hangzhou, in Chinese, First edition, (2003).   
[FW91a] K. Feng and D.L. Wang: A note on conservation laws of symplectic difference schemes for Hamiltonian systems. J. Comput. Math., 9(3):229–237, (1991).   
[FW91b] K. Feng and D.L. Wang: Symplectic difference schemes for Hamiltonian systems in general symplectic structure. J. Comput. Math., 9(1):86–96, (1991).   
[FW94] K. Feng and D.L. Wang: Dynamical systems and geometric construction of algorithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS Vol 163, pages 1–32. AMS, (1994).   
[FW98] K. Feng and D.L. Wang: On variation of schemes by Euler. J. Comput. Math., 16:97– 106, (1998).   
[FWQ90] K. Feng, H.M. Wu, and M.Z. Qin: Symplectic difference schemes for linear Hamiltonian canonical systems. J. Comput. Math., 8(4):371–380, (1990).   
[FWQW89] K. Feng, H.M. Wu, M.Z. Qin and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[Ge88] Z. Ge: Symplectic geometry and its application in numerical analysis. PhD thesis, Computer Center, CAS, (1988).   
[Ge90] Z. Ge: Generating functions, Hamilton–Jacobi equations and symplectic groupoids on Poisson manifolds. Indiana Univ. Math. J., 39:859, (1990).   
[Ge91] Z. Ge: Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, (1991).   
[Ge95] Z. Ge: Symplectic integrators for Hamiltonian systems. In W. Cai et al., editor, Numerical Methods in Applied Sciences, pages 97–108, Science Press, New York, (1995).   
[Gon96] O. Gonzalez: Time integration and discrete Hamiltonian systems. J. Nonlinear. Sci., 6:449–467, (1996).   
[Hai94] E. Hairer: Backward analysis of numerical integrators and symplectic methods. Annals of Numer. Math., 1:107–132, (1994).   
[Hai97b] E. Hairer: Variable time step integration with symplectic methods. Appl. Numer. Math., 25:219–227, (1997).   
[Hai99] E. Hairer: Backward error analysis for multistep methods. Numer. Math., 84:199–232, (1999).   
[Hai00] E. Hairer: Symmetric projection methods for differential equations on manifolds. BIT, 40:726–734, (2000).   
[Hai01] E. Hairer: Geometric integration of ordinary differential equations on manifolds. BIT, 41:996–1007, (2001).   
[Hai03] E. Hairer: Global modified Hamiltonian for constrained symplectic integrators. Numer. Math., 95:325–336, (2003). & Sons, Inc., New York, Second edition, (1962).   
[HL97a] E. Hairer and P. Leone: Order barriers for symplectic multi-value methods. In D.F. Grifysis, D.F.Higham, and G.A. Watson, editors, Numerical Analysis 1997 Proc.of the 17- th Dundee Biennial Conference,June 24-27, 1997, Pitman Reserch Notes in math. series 380, pages 133–149, (1997).   
[HL97b] E. Hairer and Ch. Lubich: The life-span of backward error analysis for numerical integrators. Numer. Math., 76:441–462, (1997).   
[HL97c] M. Hochbruck and Ch. Lubich: On Krylov subspace approximations to the matrix exponential operator. SIAM J. Numer. Anal., 34(5), (1997).   
[HL97d] W. Huang and B. Leimkuhler: The adaptive Verlet method. SIAM J. Sci. Comput., 18(1):239, (1997).   
[HL99a] E. Hairer and Ch. Lubich: Invariant tori of dissipatively perturbed Hamiltonian systems under symplectic discretization. Appl. Numer. Math., 29:57–71, (1999).   
[HL99b] M. Hochbruck and Ch. Lubich: Exponential integrators for quantum-classical molecular dynamics. BIT, 39:620–645, (1999).   
[HL00a] E. Hairer and P. Leone: Some properties of symplectic Runge–Kutta methods. New Zealand J. of Math., 29:169–175, (2000).   
[HL00b] E. Hairer and Ch. Lubich: Energy conservation by Stormer-type numerical inte- ¨ grators. In G.F. Griffiths and G.A. Watson, editors, In Numerical Analysis 1999, pages 169–190. CRC Press LLC, (2000).   
[HL00c] E. Hairer and Ch. Lubich: Long-time energy conservation of numerical methods for oscillatory differential equations. SIAM J. Numer. Anal., 38:414–441, (2000).   
[HL00d] J. L. Hong and Y. Liu: Symplectic integration of linear discontinues Hamiltonian systems. Neural Parallel Sci Comput., 8:317–325, (2000).   
[HL03] M. Hochbruck and C. Lubich: On magnus integrators for time-dependent Schrodinger ¨ equations. SIAM J. Numer. Anal., 41:945–963, (2003).   
[HL04a] E. Hairer and C. Lubich: symmetric multistep methods over long times. Numer. Math., 97:699–723, (2004).   
[HLR01] T. Holder, B. Leimkuhler, and S. Reich: Explicit variable step-size and timereversible integration. Appl. Numer. Math., 39:367–377, (2001).   
[HLS98] M. Hochbruck, C. Lubich, and H. Selhofer: Exponential integrators for large systems of differential equations. SIAM J. Sci. Comput., 19(5):1552–1574, (1998).   
[HLW02] E. Hairer, Ch. Lubich, and G. Wanner: Geometric Numerical Integration. Number 31 in Springer Series in Computational Mathematics. Springer-Verlag, (2002).   
[HLW03] E. Hairer, C. Lubich and G. Wanner: Geometric integration illustrated by the Stormer-Verlet method. ¨ Acta Numerica, pages 399–450, (2003).   
[HM04] P. Hydon and E.L. Mansfield: A variational complex for difference equations. Foundations of Computational Mathematics, 4:187–217, (2004).   
[HMM95] P. Hut, J. Makino and S. McMillan: Building a better leapfrog. Astrophys. J., 443:L93–L96, (1995).   
[HMSS93] E. Hairer, A. Murua and J.M. Sanz-Serna: The non-existence of symplectic multiderivative Runge–Kutta methods. Preprint, (1993).   
[HNW93] E. Hairer, S. P. Nørsett, and G. Wanner: Solving Ordinary Differential Equations I, Nonstiff Problems. Springer-Verlag, Second revised edition, (1993).   
[HOS99] D.J. Hardy, D.I. Okunbor, and R.D. Skeel: Symplectic variable step size integration for $n$ -body problems. Appl. Numer. Math., 29:19–30, (1999).   
[HS81] W. H. Hundsdorfer and M. N. Spijker: A note on B-stability of Runge–Kutta methods. Numer. Math., 36:319–331, (1981).   
[HS94] A. R. Humphries and A. M. Stuart: Runge-Kutta methods for dissipative and gradient dynamical systems. SIAM J. Numer. Anal., 31(5):1452–1485, (1994).   
[HS97a] E. Hairer and D. Stoffer: Reversible long-term integration with variable stepsizes. SIAM J. Sci. Comput., 18:257–269, (1997).   
[HS05] E. Hairer and G. Soderlind: Explicit time reversible adaptive step size control. ¨ SIAM J. Sci. Comput., 26:1838–1851, (2005).   
[HW74] E. Hairer and G. Wanner: On the Butcher group and general multivalue methods. Computing, 13:1–15, (1974).   
[HW81] E. Hairer and G. Wanner: Algebraically stable and implementable Runge–Kutta methods of high order. SIAM J. Numer. Anal., 18:1098–1108, (1981).   
[HW91] E. Hairer and G. Wanner: Solving Ordinary Differential Equations II, Stiff and Differential-Algebraic Problems. Springer, Berlin, (1991).   
[HW94] E. Hairer and G. Wanner: Symplectic Runge-Kutta methods with real eigenvalues. BIT, 34:310–312, (1994).   
[HW96] E. Hairer and G. Wanner: Solving Ordinary Differential Equations II. Stiff and Differential-Algebraic Problems, 2nd edition, Springer Series in Computational Mathematics 14. Springer-Verlag Berlin, Second edition, (1996).   
[IA88] T. Itoh and K. Abe: Hamiltonian-conserving discrete canonical equations based on variational difference quotients. J. of Comp. Phys., 76:85–102, (1988).   
[Jay96] L. O. Jay: Symplectic partitioned Runge–Kutta methods for constrained Hamiltonian systems. SIAM J. Numer. Anal., 33:368–387, (1996).   
[Jay97] L. O. Jay: Lagrangian integration with symplectic methods. Technical Report AH-PCRC Preprint 97-009, University of Minnesota, (1997).   
[Jay99] L. O. Jay: Structure preservation for constrained dynamics with super partitioned additive Runge–Kutta methods. SIAM J. Sci. Comput., 20(2):416–446, (1999).   
[Jim94] S. Jime´nez: Derivation of the discrete conservation laws for a family of finite difference schemes. Applied Mathematics and Computation, 64:13–45, (1994).   
[JL06] Z. Jia and B. Leimkuhler: Geometric integrators for multiple time-scale simulation. J. Phys. A: Math. Gen., 39:5379–5403, (2006).   
[Kar96a] B. Karasozen: Comparison of reversible integrators for a Hamiltonian in normal ¨ form. In E. Kreuzer and O. Mahrenholz, editors, Proceedings of the Third International Congress on Industrial and Applied Mathematics, ICIAM 95, Issue 4: Applied Sciences, especially Mechanics (Minisymposia), pages 563–566, (1996).   
[Kar96b] B. Karasozen: Composite integrators for Bi-Hamiltonian systems. ¨ Comp. & Math. with Applic., 32:79–86, (1996).   
[Kar96c] B. Karasozen: Numerical Studies on a Bi-Hamiltonian H ¨ enon-Heiles System. Tech- ´ nical Report No 133, Middle East Technical University, Department of Mathematics, Ankara, Turkey, (1996).   
[Kar97] B. Karasozen: Reflexive methods for dynamical systems with conserved quantities. ¨ Technical Report Nr. 1897, Technische Hochschule Darmstadt, FB Mathematik, (1997).   
[KHL08] L. H. Kong, J. L. Hong, and R. X. Liu: Long-term numerical simulation of the interaction between a neutron field and meson field by a symplectic-preserving scheme. J. Phys. A: Math. Theor., 41:255207, (2008).   
[Kir86] U. Kirchgraber: Multi-step methods are essentially one-step methods. Numer. Math., 48:85–90, (1986).   
[Lam91] J.D. Lambert: Numerical Methods for Ordinary Differential Equations, The Initial Value Problem. Wiley, Chichester, (1991).   
[Las88] F.M. Lasagni: Canonical Runge–Kutta methods. Z. Angew. Math. Phys., 39:952–953, (1988).   
[LDJW00] Y.X. Li, P. Z. Ding, M. X. Jin, and C. X. Wu: Computing classical trajectories of model molecule $A _ { 2 } B$ by symplectic algorithm. Chemical Journal of Chinese Universities, 15(8):1181–1186, (2000).   
[Lei99] B. J. Leimkuhler: Reversible adaptive regularization: Perturbed Kepler motion and classical atomic trajectories. Phil. Trans. Royal Soc. A, 357:1101, (1999).   
[Leo00] P. Leone: Symplecticity and Symmetry of General Integration Methods. These, Section \` de Mathematiques, Universit ´ e de Gen ´ eve, Second edition, (2000). \`   
[LP96] B. J. Leimkuhler and G. W. Patrick: A symplectic integrator for Riemannian manifolds. J. Nonlinear. Sci., 6(4):367–384, (1996). of matrix differential systems on quadratic groups. Appl. Numer. Math., 36:35–55, (2001).   
[LQ01] H. W. Li and M. Z. Qin: On the formal energy of symplectic R–K method. Math. Num. Sinica, 23:75–92, (2001).   
[LQHD07] X.S. Liu, Y.Y. Qi, J. F. He, and P. Z. Ding: Recent progress in symplectic algorithms for use in quantum systems. Communications in Computational Physics, 2(1):1–53, (2007).   
[LR94a] B. Leimkuhler and S. Reich: Symplectic integration of constrained Hamiltonian systems. Math. Comp., 63:589–605, (1994).   
[LR05] B. Leimkuhler and S. Reich: Simulating Hamiltonian Dynamics. Cambridge University Press, Cambridge, First edition, (2005).   
[LvV97] B. J. Leimkuhler and E. S. van Vleck: Orthosymplectic integration of linear Hamiltonian systems. Numer. Math., 77:269–282, (1997).   
[LW76] J. D. Lambert and I. A. Watson: Symmetric multistep methods for periodic initial value problems. J. Inst. Maths. Applics., 18:189–202, (1976).   
[LYC06] H. Liu, J.H. Yuan, J.B. Chen, H. Shou, and Y.M. Li: Theory of large-step depth extrapolation. Chinese journal Geophys., 49(6):1779–1793, (2006).   
[McL95c] R. I. McLachlan: On the numerical integration of ODE’s by symmetric composition methods. SIAM J. Numer. Anal., 16:151–168, (1995).   
[McL95d] R. I. McLachlan: On the numerical integration of ordinary differential equations by symmetric composition methods. SIAM J. Sci. Comput., 16:151–168, (1995).   
[McL96] R. I. McLachlan: More on Symplectic Correctors. In Jerrold E. Marsden, George W. Patrick, and William F. Shadwick, editors, Integration Algorithms and Classical Mechanics, volume 10 of Fields Institute Communications. Fields Institute, American Mathematical Society, July (1996).   
[McL02] R. McLachlan: Splitting methods. Acta Numerica, 11:341–434, (2002).   
[Mie89] S. Miesbach: Symplektische Phasenfluß approximation zur Numerischen Integration Kanonischer Differentialgleichungen. Master’s thesis, Technische Universitat M¨ unchen, ¨ (1989).   
[MP92] S. Miesbach and H.J. Pesch: Symplectic phase flow approximation for the numerical integration of canonical systems. Numer. Math., 61:501–521, (1992).   
[MPQ04] R.I. McLachlan, M. Perlmutter, and G.R.W. Quispel: On the nonlinear stability of symplectic integrators. BIT, 44:99–117, (2004).   
[MQ98a] R. I. McLachlan and G. R. W. Quispel: Generating functions for dynamical systems with symmetries, integrals, and differential invariants. Physica D, 112:298–309, (1998).   
[MQ98b] R.I. McLachlan and G.R.W. Quispel: Numerical integrators that preserve symmetries and reversing symmetries. SIAM J. Numer. Anal., 35:586–599, (1998).   
[MQ02] R. I. McLachlan and G. R. W. Quispel: Splitting methods. Acta Numerica, 11:341– 434, (2002).   
[MQ03] R.I. McLachlan and G.R.W. Quispel: Geometric integration of conservative polynomial ODEs. Appl. Numer. Math., 45:411–418, (2003).   
[MQ04] D.I. McLaren and G.R.W. Quispel: Integral-preserving integrators. J. Phys. A: Math. Gen., 37:L489–L495, (2004).   
[MQR98] R. I. McLachlan, G. R. W. Quispel, and N. Robidoux: A unified approach to Hamiltonian systems, Poisson systems, gradient systems, and systems with Lyapunov functions and/or first integrals. Physical Review Letters, 81:2399–2403, (1998).   
[MQR99] R. I. McLachlan, G. R. W. Quispel, and N. Robidoux: Geometric integration using discrete gradients. Phil. Trans. Royal Soc. A, 357:1021–1046, (1999).   
[MQT98] R. I. McLachlan, G. R. W. Quispel, and G. S. Turner: Numerical integrators that preserve symmetries and reversing symmetries. SIAM J. Numer. Anal., 35(2):586–599, (1998).   
[MS95c] R. I. McLachlan and C. Scovel: Equivariant constrained symplectic integration. J. Nonlinear. Sci., 5:233–256, (1995).   
[MS96] R. I. McLachlan and C. Scovel: A Survey of Open Problems in Symplectic Integration. In J. E. Mardsen, G. W. Patrick, and W. F. Shadwick, editors, Integration Algorithms and Classical Mechanics, pages 151–180. American Mathematical Society, (1996).   
[Mur97] A. Murua: On order conditions for partitioned symplectic methods. SIAM J. Numer. Anal., 34:2204–2211, (1997).   
[Mur99] A. Murua: Formal series and numerical integrators, part I: Systems of odes and symplectic integrators. Appl. Numer. Math., 29:221–251, (1999).   
[Obr40] N. Obreschkoff: Neue Quadraturformeln. Abhandlungen pro¨ß Klasse Acad Wiss Mathnatuwiss, 1–20.(1940).   
[Oku93] D. Okunbor: Variable step size does not harm second-order integrators for Hamiltonian systems. J. Comput. Appl. Math, 47:273–279, (1993).   
[Oku95] E. I. Okunbor: Energy conserving, Liouville, and symplectic integrators. J. of Comp. Phys., 120(2):375–378, (1995).   
[OS92] D. Okunbor and R.D. Skeel: Explicit canonical methods for Hamiltonian systems. Math. Comp., 59:439–455, (1992).   
[QD97] G. R. W. Quispel and C. Dyt: Solving ODE’s numerically while preserving symmetries, Hamiltonian structure, phase space volume, or first integrals. In A. Sydow, editor, Proceedings of the 15th IMACS World Congress, pages 601–607. Wissenschaft & Technik, Berlin, (1997).   
[Qin87] M. Z. Qin: A symplectic schemes for the Hamiltonian equations. J. Comput. Math., 5:203–209, (1987).   
[Qin89] M. Z. Qin: Cononical difference scheme for the Hamiltonian equation. Mathematical Methodsand in the Applied Sciences, 11:543–557, (1989).   
[Qin90] M. Z. Qin: Multi-stage symplectic schemes of two kinds of Hamiltonian systems of wave equations. Computers Math. Applic., 19:51–62, (1990).   
[Qin96] M. Z. Qin: Symplectic difference schemes for nonautonomous Hamiltonian systemes. Acta Applicandae Mathematicae, 12(3):309–321, (1996).   
[Qin97a] M. Z. Qin: A symplectic schemes for the PDE’s. AMS/IP studies in Advanced Mathemateics, 5:349–354, (1997).   
[QT90a] G. D. Quinlan and S. Tremaine: Symmetric multistep methods for the numerical integration of planetary orbits. Astron. J., 100:1694–1700, (1990).   
[QT90b] G.D. Quinlan and S. Tremaine: Symmetric multistep methods for the numerical integration of planetary orbits. Astron. J., 100:1694–1700, (1990).   
[QT96] G. R. W. Quispel and G. S. Turner: Discrete gradient methods for solving ODE’s numerically while preserving a first integral. Physics Letters A, 29:L341–L349, (1996).   
[QWZ91] M. Z. Qin, D. L. Wang, and M. Q. Zhang: Explicit symplectic difference schemes for separable Hamiltonian systems. J. Comput. Math., 9(3):211–221, (1991).   
[QZ90a] M. Z. Qin and M. Q. Zhang: Explicit Runge-Kutta-like schemes to solve certain quantum operator equations of motion. J. Stat. Phys., 60(5/6):839–843, (1990).   
[QZ91] M. Z. Qin and W. J. Zhu: Canonical Runge-Kutta-Nystro¨m(RKN) methods for second order ode’s. Computers Math. Applic., 22:85–95, (1991).   
[QZ92a] M. Z. Qin and M. Q. Zhang: Symplectic Runge-Kutta Schemes for Hamiltonian System. J. Comput. Math., Supplementary Issue: pages 205–215, (1992).   
[QZ92b] M. Z. Qin and W. J. Zhu: Construction of higher order symplectic schemes by composition. Computing, 47:309–321, (1992).   
[QZ94] M. Z. Qin and W. J. Zhu: Multiplicative extrapolatio method for constructing higher order schemes for ODE’s. J. Comput. Math., 12:352–356, (1994).   
[QZZ95] M. Z. Qin, W. J. Zhu, and M. Q. Zhang: Construction of symplectic of a three stage difference scheme for ODE’s. J. Comput. Math., 13:206–210, (1995).   
[Rei94a] S. Reich: Momentum conserving symplectic integrators. Physica D, 76:375–383, (1994).   
[Rei95c] S. Reich: Smoothed dynamics of highly oscillatory Hamiltonian systems. Physica D, 89:28–42, (1995).   
[Rei96a] S. Reich: Enhancing energy conserving methods. BIT, 1:122–134, (1996). methods. SIAM J. Numer. Anal., 33:475–491, (1996).   
[Rei96c] S. Reich: Symplectic Methods for Conservative Multibody Systems. In J. E. Mardsen, G. W. Patrick, and W. F. Shadwick, editors, Integration Algorithms and Classical Mechanics, pages 181–192. American Mathematical Society, (1996).   
[Rei97] S. Reich: On higher-order semi-explicit symplectic partitioned Runge–Kutta methods for constrained Hamiltonian systems. Numer. Math., 76(2):249–263, (1997).   
[Rei99] S. Reich: Backward error analysis for numerical integrators. SIAM J. Numer. Anal., 36:475–491, (1999).   
[Rut83] R. Ruth: A canonical integration technique. IEEE Trans. Nucl. Sci., 30:26–69, (1983).   
[SA91] J.M. Sanz-Serna and L. Abia: Order conditions for canonical Runge-Kutta schemes. SIAM J. Numer. Anal., 28:1081–1096, (1991).   
[SS88] J. M. Sanz-Serna: Runge–Kutta schemes for Hamiltonian systems. BIT, 28:877–883, (1988).   
[SSC94] J. M. Sanz-Serna and M. P. Calvo: Numerical Hamiltonian Problems. AMMC 7. Chapman & Hall, (1994).   
[SSM92] S. Saito, H. Sugiura, and T. Mitsui: Family of symplectic implicit Runge-Kutta formulae. BIT, 32:539–543, (1992).   
[SSM92b] S. Saito, H. Sugiura, and T. Mitsui: Butcher’s simplifying assumption for symplectic integrators. BIT, 32:345–349, (1992).   
[Sto93b] D.M. Stoffer: Variable step size destabilizes the Stormer/leap-frog/Verlet method. ¨ BIT, 33:172–175, (1993).   
[Sto95] D. Stoffer: Variable steps for reversible integration methods. Computing, 55:1–22, (1995).   
[Sto97] D. Stoffer: On the Qualitative Behaviour of Symplectic Integrators Part I: Perturbed Linear Systems. Numer. Math., 77(4):535–548, (1997).   
[Sto98a] D. Stoffer: On the gualitative behavior of symplectic integrator. II: Integrable systems. J. of Math. Anal. and Applic., 217:501–520, (1998).   
[Sto98b] D. Stoffer: On the qualitative behaviour of symplectic integrators. III: Perturbed integrable systems. J. of Math. Anal. and Appl., 217:521–545, (1998).   
[Sun93a] G. Sun: Construction of high order symplectic Runge-Kutta methods. J. Comput. Math., 11(3):250–260, (1993).   
[Sun93b] G. Sun: Symplectic partitioned Runge–Kutta methods. J. Comput. Math., 11:365– 372, (1993).   
[Sun94] G. Sun: Characterization and construction of linear symplectic R–K methods. J. Comput. Math., 12(2):101–112, (1994).   
[Sun95] G. Sun: Construction of high order symplectic Partitioned–Runge–Kutta methods. J. Comput. Math., 13(1):40–50, (1995).   
[Sun00] G. Sun: A simple way constructing symplectic Runge–Kutta methods. J. Comput. Math., 18:61–68, (2000).   
[Sur88] Y.B. Suris: On the conservation of the symplectic structure in the numerical solution of Hamiltonian systems(in Russian), In: Numerical Solution of Ordinary Differential Equations, ed. S.S. Filippov, Keldysh Institute of Applied Mathematics. USSR Academy of Sciences, Moscow, Second edition, (1988).   
[Sur89] Y.B. Suris: The canoniwhen integrating the systems $\begin{array} { r } { \ddot { x } = - \frac { \partial U } { \partial x } } \end{array}$ ppings generated by Runge–Kutta type methods. U.S.S.R. Comput. Maths. Math. Phys., 29:138–   
[Sur90] Y.B. Suris: Hamiltonian methods of Runge–Kutta type and their variational interpretation. Math. Model., 2:78–87, in Russian, (1990).   
[Tan93a] Y. F. Tang: The symplecticity of multi-step methods. Computers Math. Applic., 25:83–90, (1993).   
[Tan93b] Y. F. Tang: The necessary condition for Runge–Kutta schemes to be symplectic for Hamiltonian systems. Computers Math. Applic., 26:13–20, (1993).   
[Tan94] Y. F. Tang: Formal energy of a symplectic scheme for Hamiltonian systems and its applications. Computers Math. Applic., 27:31–39, (1994).   
[Vog56] R. de Vogelaere: Methods of integration which preserve the contact transformation property of the Hamiltonian equations. Report No. 4, Dept. Math., Univ. of Notre Dame, Notre Dame, Ind., Second edition, (1956).   
[Wan91a] D. L. Wang: Semi-discrete Fourier spectral approximations of infinite dimensional Hamiltonian systems and conservations laws. Computers Math. Applic., 21:63–75, (1991).   
[Wan91b] D. L. Wang: Symplectic difference schemes for Hamiltonian systems on Poisson manifolds. J. Comput. Math., 9(2):115–124, (1991).   
[Wan91c] D. L. Wang: Poisson difference schemes for Hamiltonian systems on Poisson manifolds. J. Comput. Math., 9:115–124, (1991).   
[Wan93] D. L. Wang: Decomposition vector fields and composition of algorithms. In Proceedings of International Conference on computation of differential equations and dynamical systems, Beijing, 1993. World Scientific, (1993).   
[Wan94] D. L. Wang: Some acpects of Hamiltonian systems and symplectic defference methods. Physica D, 73:1–16, (1994).   
[Yos90] H. Yoshida: Conserved quantities of symplectic integrators for Hamiltonian systems. Preprint, (1990).   
[ZQ93a] M. Q. Zhang and M. Z. Qin: Explicit symplectic schemes to solve vortex systems. Comp. & Math. with Applic., 26(5):51, (1993).   
[ZQ93b] W. Zhu and M. Qin: Applicatin of higer order self-adjoint schemes of PDE’s. Computers Math. Applic.,26(3):15–26, (1993).   
[ZQ93c] W. Zhu and M. Qin: Constructing higer order schemes by formal power series. Computers Math. Applic.,25(12):31–38, (1993).   
[ZQ93] W. Zhu and M. Qin: Order conditionof two kinds of canonical difference schemes. Computers Math. Applic., 25(6):61–74, (1993).   
[ZQ94] W. Zhu and M. Qin: Poisson schemes for Hamiltonian systems on Poisson manifolds. Computers Math. Applic., 27:7–16, (1994).   
[ZQ95a] W. Zhu and M. Qin: Reply to “comment on Poisson schemes for Hamiltonian systems on Poisson manifolds”. Computers Math. Applic., 29(7):1, (1995).   
[ZQ95b] W. Zhu and M. Qin: Simplified order conditions of some canonical difference schemes. J. Comput. Math., 13(1):1–19, (1995).   
[ZS75] K. Zare and V. Szebehely: Time transformations in the extended phase-space. Celest. Mech., 11:469–482, (1975).   
[ZS95] M. Q. Zhang and R. D. Skeel: Symplectic integrators and the conservation of angular momentum. J. Comput. Chem., 16:365–369, (1995).   
[ZS97] M. Q. Zhang and R. D. Skeel: Cheap implicit symplectic integrators. Appl. Numer. Math., 25(2):297, (1997).   
[ZW99] H. P. Zhu and J. K. Wu: Generalized canonical transformations and symplectic algorithm of the autonomous Birkhoffian systems. Progr. Natur. Sci., 9:820–828, (1999).   
[ZzT96] W. Zhu, X. zhao, and Y Tang: Numerical methods with a high order of accuracy applied in the quantum system. J. Chem. Phys., 104(6):2275–2286, (1996).
