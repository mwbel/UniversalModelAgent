# 324 Order barriers

It is possible, as we have seen, to derive explicit methods with $s ~ = ~ p$ for $p = 1 , 2 , 3 , 4$ . These methods are optimal in the sense that $s ~ < ~ p$ is never possible and $p = 4$ is as high as it is possible to go with $s ~ = ~ p$ . We now formalize these remarks.

Theorem 324A If an explicit $s$ -stage Runge–Kutta method has order $p$ , then $s \geq p$ .

Proof. Let $t = [ [ \cdots [ t ] \cdot \cdot \cdot ] ]$ such that $r ( t ) = p > s$ . The order condition associated with this tree is $\Phi ( t ) = 1 / \gamma ( t )$ , where $\gamma ( t ) = p !$ and $\Phi ( t ) = b ^ { \mathsf { T } } A ^ { p - 1 } \mathbf { 1 }$ . Because $A$ is strictly lower triangular, $A ^ { p } = 0$ . Hence, the order condition becomes $0 = 1 / p !$ , which has no solution. 

Theorem 324B If an explicit $s$ -stage Runge–Kutta method has order $p \geq 5$ , then $s > p$ .

Proof. Assume $s = p$ . Evaluate the values of the following four expressions:

$$
\begin{array} { c } { { b ^ { \top } A ^ { p - 4 } ( C - c _ { 4 } I ) ( C - c _ { 2 } I ) c = \displaystyle { \frac { 6 } { p ! } } - \frac { 2 ( c _ { 2 } + c _ { 4 } ) } { ( p - 1 ) ! } + \frac { c _ { 2 } c _ { 4 } } { ( p - 2 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } ( C - c _ { 4 } I ) A c = \displaystyle { \frac { 3 } { p ! } } - \frac { c _ { 4 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } A ( C - c _ { 2 } I ) c = \displaystyle { \frac { 2 } { p ! } } - \frac { c _ { 2 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 4 } A ^ { 2 } c = \displaystyle { \frac { 1 } { p ! } } . } } \end{array}
$$

From the left-hand sides of these expressions we observe that (324a) $\times$ (324d) = (324b) $\times$ (324c). Evaluate the right-hand sides, and we find that

$$
\left( { \frac { 6 } { p ! } } - { \frac { 2 ( c _ { 2 } + c _ { 4 } ) } { ( p - 1 ) ! } } + { \frac { c _ { 2 } c _ { 4 } } { ( p - 2 ) ! } } \right) \left( { \frac { 1 } { p ! } } \right) = \left( { \frac { 3 } { p ! } } - { \frac { c _ { 4 } } { ( p - 1 ) ! } } \right) \left( { \frac { 2 } { p ! } } - { \frac { c _ { 2 } } { ( p - 1 ) ! } } \right) ,
$$

which simplifies to $c _ { 2 } ( c _ { 4 } - 1 ) = 0$

Now consider the four expressions

$$
\begin{array} { c } { { b ^ { \top } A ^ { p - 5 } ( C - c _ { 5 } I ) A ( C - c _ { 2 } I ) c = \displaystyle \frac { 8 } { p ! } - \frac { 3 c _ { 2 } + 2 c _ { 5 } } { ( p - 1 ) ! } + \frac { c _ { 2 } c _ { 5 } } { ( p - 2 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } ( C - c _ { 5 } I ) A ^ { 2 } c = \displaystyle \frac { 4 } { p ! } - \frac { c _ { 5 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } A ^ { 2 } ( C - c _ { 2 } I ) c = \displaystyle \frac { 2 } { p ! } - \frac { c _ { 2 } } { ( p - 1 ) ! } , } } \\ { { b ^ { \top } A ^ { p - 5 } A ^ { 3 } c = \displaystyle \frac { 1 } { p ! } . } } \end{array}
$$

Again we see that (324e) $\times$ (324h) = (324f) $\times$ (324g), so that evaluating the right-hand sides, we find

$$
\left( { \frac { 8 } { p ! } } - { \frac { 3 c _ { 2 } + 2 c _ { 5 } } { ( p - 1 ) ! } } + { \frac { c _ { 2 } c _ { 5 } } { ( p - 2 ) ! } } \right) \left( { \frac { 1 } { p ! } } \right) = \left( { \frac { 4 } { p ! } } - { \frac { c _ { 5 } } { ( p - 1 ) ! } } \right) \left( { \frac { 2 } { p ! } } - { \frac { c _ { 2 } } { ( p - 1 ) ! } } \right) ,
$$

leading to $c _ { 2 } ( c _ { 5 } - 1 ) = 0$ . Since we cannot have $c _ { 2 } = 0$ , it follows that $c _ { 4 } =$ $c _ { 5 } = 1$ . Now evaluate $b ^ { 1 } A ^ { p - 5 } ( C - e ) A ^ { 2 } c$ . This equals $( 4 - p ) / p !$ by the order conditions but, in contradiction to this, it equals zero because component number $i$ of $b ^ { 1 } A ^ { p - 5 }$ vanishes unless $i ~ \leq ~ 5$ . However, these components of $( C - e ) A ^ { 2 } c$ vanish. $\boxed { \begin{array} { r l } \end{array} }$

The bound $s - p \ge 1$ , which applies for $p \geq 5$ , is superseded for $p \geq 7$ by $s \mathrm { ~ - ~ } p \mathrm { ~ \geq ~ 2 ~ }$ . This is proved in Butcher (1965a). For $p \geq 8$ we have the stronger bound $s - p \ge 3$ (Butcher, 1985). It seems likely that the minimum value of $s - p$ rises steadily as $p$ increases further, but there are no published results dealing with higher orders. On the other hand, it is known, because of the construction of a specific method (Hairer, 1978), that $p = 1 0$ , $s = 1 7$ is possible.

That a sufficiently high $s$ can be found to achieve order $p$ follows immediately from Theorem 317A. We now derive an upper bound on the minimum value of such an $s$ . This is done by constructing methods with odd orders, or methods satisfying the generalization of odd orders introduced in Subsection 323. In the latter case, we then use the results of that subsection to extend the result to the next even order higher.

Theorem 324C For any positive integer $p$ , an explicit Runge–Kutta method exists with order $p$ and $s$ stages, where

$$
s = \left\{ \begin{array} { l l } { \frac { 3 p ^ { 2 } - 1 0 p + 2 4 } { 8 } , \qquad } & { p \ e v e n , } \\ { \frac { 3 p ^ { 2 } - 4 p + 9 } { 8 } , \qquad } & { p \ o d d . } \end{array} \right.
$$

Proof. We consider the case of $p$ odd, but allow for generalized order conditions. If $p = 1 + 2 m$ , we construct first an implicit Runge–Kutta method with $1 + m$ stages, using (case I) standard order conditions and (case II) generalized order conditions. For case I, the order condition associated with the tree $t$ is, as usual,

$$
\Phi ( t ) = \frac { 1 } { \gamma ( t ) } .
$$

In case II, this condition is replaced by

$$
\Phi ( t ) = \frac { 1 } { ( r ( t ) + 1 ) \gamma ( t ) } .
$$

For the implicit method, the abscissae are at the zeros of the polynomial

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { m } } { d x ^ { m } } x ^ { m + 1 } ( x - 1 ) ^ { m } , \mathrm { i n c a s e I , } } } \\ { { \displaystyle \frac { d ^ { m } } { d x ^ { m } } x ^ { m + 1 } ( x - 1 ) ^ { m + 1 } , \mathrm { i n c a s e I I , } } } \end{array}
$$

with the zero $x = 1$ omitted in case II. It is clear that $x = 0$ is a zero in both cases and that the remaining zeros are distinct and lie in the interval $\lfloor 0 , 1 \rfloor$ . Denote the positive zeros by $\xi _ { i }$ , $i = 1 , 2 , \dots , m$ . We now construct methods with abscissae chosen from the successive rows of the following table:

$$
\begin{array} { l l l l l l } { \mathrm { r o w ~ 0 } } & { 0 } & { 0 } & { } & { } & { } & { } \\ { \mathrm { r o w ~ 1 } } & { } & { \xi _ { 1 } } & { } & { } & { } & { } \\ { \mathrm { r o w ~ 2 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { } & { } & { } \\ { \mathrm { r o w ~ 3 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { } & { } & { } \\ & { } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { } & { } \\ { \mathrm { r o w ~ m ~ } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } & { } \\ { \mathrm { r o w ~ m + 1 } } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } & { } \\ & { } & { \vdots } & { \vdots } & { \vdots } & { } & { \vdots } & { } \\ { \mathrm { r o w ~ 2 } m } & { } & { } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \xi _ { 3 } } & { \cdots } & { \xi _ { m } } \end{array}
$$

where there are exactly $m + 1$ repetitions of the rows with $m$ members. The total number of stages will then be

$$
s = 1 + { \big ( } 1 + 2 + \cdot \cdot \cdot + ( m - 1 ) { \big ) } + ( m + 1 ) m = { \frac { 1 } { 2 } } ( 3 m ^ { 2 } + m + 2 ) .
$$

Having chosen $c = \left( \begin{array} { l l l l l l } { 0 } & { \xi _ { 1 } } & { \xi _ { 1 } } & { \xi _ { 2 } } & { \dots } & { \xi _ { m } } \end{array} \right) ^ { 1 }$ , we construct $b ^ { \scriptscriptstyle 1 }$ with all components zero except the first component and the final $m$ components. The non-zero components are chosen so that

$$
\begin{array} { l } { { b _ { 1 } + \displaystyle \sum _ { i = 1 } ^ { m } b _ { s - m + i } = \left\{ \begin{array} { l l } { { 1 , } } & { { \mathrm { ~ c a s e ~ I ~ } } } \\ { { \frac { 1 } { 2 } , } } & { { \mathrm { ~ c a s e ~ I I ~ } } } \end{array} \right. } } \\ { { \displaystyle \sum _ { i = 1 } ^ { m } b _ { s - m + i } \xi _ { i } ^ { k - 1 } = \left\{ \begin{array} { l l } { { \frac { 1 } { k } , } } & { { \mathrm { ~ c a s e ~ I ~ } } } \\ { { \frac { 1 } { k ( k + 1 ) } , } } & { { \mathrm { ~ c a s e ~ I I ~ } } } \end{array} \right\} , \quad k = 1 , 2 , \ldots , 2 m + 1 . } } \end{array}
$$

The possibility that the non-zero $b$ components can be found to satisfy these conditions follows from the theory of Gaussian quadrature. The final step in the construction of the method is choosing the elements of the matrix $A$ . For $i$ corresponding to a member of row $k$ for $k = 1 , 2 , \ldots , m$ , the only non-zero


<!-- chunk 0004: pages 211-280 -->
$a _ { i j }$ are for $j = 1$ and for $j$ corresponding to a member of row $k - 1$ . Thus, the quadrature formula associated with this row has the form

$$
\int _ { 0 } ^ { c _ { i } } \phi ( x ) d x \approx w _ { 0 } \phi ( 0 ) + \sum _ { j = 1 } ^ { k - 1 } w _ { j } \phi ( \xi _ { j } )
$$

and the coefficients are chosen to make this exact for $\phi$ a polynomial of degree $k - 1$ . For $i$ a member of row $k = m + 1 , m + 2 , \ldots , 2 m$ , the non-zero $a _ { i j }$ are found in a similar way based on the quadrature formula

$$
\int _ { 0 } ^ { c _ { i } } \phi ( x ) d x \approx w _ { 0 } \phi ( 0 ) + \sum _ { j = 1 } ^ { m } w _ { j } \phi ( \xi _ { j } ) .
$$

The method constructed in this way has order, or generalized order, respectively, equal to $p = 2 m + 1$ . To see this, let ${ \widetilde { Y } } _ { i }$ denote the approximation to $y ( x _ { n - 1 } + h \xi _ { i } )$ in stage $1 + i$ of the order $2 m + 1$ Radau I method (in case I) or the order $2 m + 2$ Lobatto method (in case II). It is easy to see that the stages corresponding to row $k$ approximate the $\widetilde { Y }$ quantities to within $O ( h ^ { k + 1 } )$ . Thus the full method has order $2 m + 1$ in case I and generalized order $2 m + 1$ in case II. Add one more stage to the case II methods, as in Theorem 323B, and we obtain order $p = 2 m + 2$ with $s = { \textstyle { \frac { 1 } { 2 } } } ( 3 m ^ { 2 } + m + 4 )$ stages compared with $p = 2 m + 1$ and $\begin{array} { r } { s = { \frac { 1 } { 2 } } ( 3 m ^ { 2 } + m + 2 ) } \end{array}$ stages in case I. This gives the result of the theorem. 
