(2.2.33) holds for any ordering of the rotations in Givens QR factorization. Actual errors grow even more slowly.

Two plane rotations $G _ { i j }$ and $G _ { k l }$ are said to be disjoint if the integers $i , j , k , l$ are disjoint. Disjoint rotations commute and can be performed in parallel. To increase the efciency of Givens QR factorizations, the rotations can be ordered into groups of disjoint operations. An ordering suggested by Gentleman [451,1975] is illustrated as follows for a $6 \times 5$ matrix:

$$
\left[ { \begin{array} { c c c c c c } { \times } & { \times } & { \times } & { \times } & { \times } \\ { 1 } & { \times } & { \times } & { \times } & { \times } \\ { 2 } & { 3 } & { \times } & { \times } & { \times } \\ { 3 } & { 4 } & { 5 } & { \times } & { \times } \\ { 4 } & { 5 } & { 6 } & { \times } & { \times } \\ { 5 } & { 6 } & { 7 } & { 8 } & { \times } \end{array} } \right] .
$$

Here an integer $k$ in position $( i , j )$ denotes that the corresponding element is eliminated in step $k$ . Note that all elements in a group are disjoint. For a matrix $A \in \mathbb { R } ^ { m \times n }$ with $m > n$ ， $m + n - 2$ stages are needed.

# 2.2.3 - Least Squares by Householder QR

Since orthogonal transformations preserve the Euclidean length, the QR factorization is an ideal tool for solving linear least squares problems.

Theorem 2.2.5. Let $A \in \mathbb { R } ^ { m \times n }$ ， $\operatorname { r a n k } ( A ) = n$ have the QR factorization

$$
A = Q \left( { R \atop 0 } \right) .
$$

Then the unique solution $x$ $\dot { \mathbf { \xi } } t o \operatorname* { m i n } _ { x } \parallel A x - b \parallel _ { 2 }$ and the corresponding residual vector $r = b - A x$ are given by the solution of the upper triangular system $R x = d _ { 1 }$ ,where

$$
\begin{array} { r } { \left( \begin{array} { l } { d _ { 1 } } \\ { d _ { 2 } } \end{array} \right) = Q ^ { T } b , \qquad r = Q \left( \begin{array} { l } { 0 } \\ { d _ { 2 } } \end{array} \right) . } \end{array}
$$

The norm of the residual $r = b - A x$ is $\| r \| _ { 2 } = \| d _ { 2 } \| _ { 2 }$

Proof. Since $Q$ is orthogonal, we have

$$
\| r \| _ { 2 } ^ { 2 } = \left\| Q ^ { T } ( b - A x ) \right\| _ { 2 } ^ { 2 } = \left\| { \binom { d _ { 1 } } { d _ { 2 } } } - { \binom { R x } { 0 } } \right\| _ { 2 } ^ { 2 } = \| d _ { 1 } - R x \| _ { 2 } ^ { 2 } + \| d _ { 2 } \| _ { 2 } ^ { 2 } .
$$

Clearly $\| \boldsymbol { r } \| _ { 2 } ^ { 2 }$ is minimized by taking $R x \ = \ d _ { 1 }$ . From the orthogonality of $Q$ it follows that $b = A x + r = Q d = Q _ { 1 } d _ { 1 } + Q _ { 2 } d _ { 2 }$ . Since $Q _ { 1 } d _ { 1 } = Q _ { 1 } R x = A x$ , it follows that $r = Q _ { 2 } d _ { 2 }$ and $\| r \| _ { 2 } = \| d _ { 2 } \| _ { 2 }$ □

Golub [487,1965l gives an algorithm using pivoted Householder QR factorization. The factor $Q$ is not explicitly formed but implicitly defined as $Q = H _ { 1 } H _ { 2 } \cdot \cdot \cdot H _ { n }$ ：

$$
\left( \begin{array} { l } { { d _ { 1 } } } \\ { { d _ { 2 } } } \end{array} \right) = H _ { n } \cdot \cdot \cdot H _ { 2 } H _ { 1 } b , \qquad r = H _ { 1 } H _ { 2 } \cdot \cdot \cdot H _ { n } \left( \begin{array} { l } { { 0 } } \\ { { d _ { 2 } } } \end{array} \right) .
$$

An ALGOL implementation of Golub's least squares algorithm is given in Businger and Golub [193, $\mathbf { 1 9 6 5 } ]$ . This later appeared in Wilkinson and Reinsch [1123,1971].

Householder QR factorization requires $2 n ^ { 2 } ( m - n / 3 )$ flops, and computing $Q ^ { T } b$ and solving $R x \ : = \ : d _ { 1 }$ require a further $4 m n - n ^ { 2 }$ flops.If one wants not only $\| r \| _ { 2 }$ but also $r$ ，another $4 n m - 2 n ^ { 2 }$ flops are needed. This can be compared to the method of normal equations, which requires $( m n ^ { 2 } + n ^ { 3 } / 3 )$ flops for the factorization and $2 ( n m + n ^ { 2 } )$ flops for each right-hand side. For $m = n$ this is about the same as for the Householder QR method, but for $m \gg n$ the Householder method is roughly twice as expensive.

In the following algorithm the QR factorization is applied to the extended matrix $( A b )$

$$
\left( \begin{array} { c c } { { A } } & { { b } } \end{array} \right) = Q \left( \begin{array} { c c } { { R } } & { { d _ { 1 } } } \\ { { 0 } } & { { \rho e _ { 1 } } } \end{array} \right) , \quad Q = H _ { 1 } \cdot \cdot \cdot H _ { n } H _ { n + 1 } .
$$

Then $R x = d _ { 1 }$ and the residual and its norm are given by

$$
r = H _ { 1 } \cdot \cdot \cdot H _ { n } H _ { n + 1 } \left( { 0 \atop \rho e _ { 1 } } \right) , \qquad \| r \| _ { 2 } = \rho \geq 0 .
$$

# Algorithm 2.2.5 (Least Squares Solution by Householder QR).

function $\mathrm { [ x , r , r h o ] ~ = ~ h o u s e l s ( A , b ) ; }$ $\%$ HOUSELS computes the solution ${ \tt x }$ ，the residual $\%$ r and rho $= \mathrm { ~ | ~ | ~ r \mid ~ | ~ } _ { - } 2$ to the full-rank linear $\%$ least squares problem min $| \mathbf { \nabla } | \operatorname { A x } \ - \ \operatorname { b } | \mathbf { \nabla } | \mathbf { \mu } _ { - } 2$ ， $\%$ $\begin{array} { r l } & { [ \mathbf { m } , \mathbf { n } ] \quad \mathrm { ~ e ~ s i z e ~ ( } A \boldsymbol { ) } ; \quad \forall \quad \mathrm { ~ \vec { n } ~ \mathbf { \tau } _ { \mathrm { n } } ~ > ~ \mathbf { n } ~ } } \\ & { [ \boldsymbol { \nabla } , \mathbf { S } , \mathbf { b } \in \mathrm { f a } ] \quad \mathrm { ~ n o u s e q r ~ ( } \mathrm { ~ I A } , \mathrm { ~ b } ] ; } \\ & { \mathrm { ~ R } \quad \mathrm { ~ e ~ \mathbf { \sigma } _ { \mathrm { S } } ~ > ( 1 : , n , 1 : n ) ~ } ; } \\ & { \mathrm { ~ R } \quad = \mathrm { ~ S } \left( 1 : \mathbf { n } , \mathbf { \sigma } _ { \mathrm { M } } + 1 \right) ; } \\ & { \mathrm { ~ x ~ = ~ R } \mathrm { \times d } ! ; } \\ & { \mathrm { ~ r h o } \quad = \mathrm { ~ a b s ~ ( S ( \mathbf { n } + 1 , \mathbf { n } + 1 ) ) ~ } ; } \\ & { \mathrm { ~ \sigma ~ r e r o ~ s e r o ~ s ( \sigma , 1 ) ~ } ; } \\ & { \mathrm { ~ \boldsymbol { r } ~ \mathbf { \sigma } _ { \mathrm { n } } ~ > ~ \mathbf { r h o } ~ : } } \\ & { \mathrm { ~ f o r ~ \sigma ~ k ~ = ~ \mathbf { n } + 1 : - 1 : 1 ~ } } \\ & { \mathrm { ~ \boldsymbol { c } ~ \mathbf { \sigma } _ { \mathrm { n } } ~ < \mathbf { b e t a } ~ ( \mathbf { \sigma } _ { \mathrm { M } } ~ > ~ \mathbf { \sigma } _ { \mathrm { c r } } ( \mathbf { \sigma } _ { \mathrm { k } } ; \mathbf { n } ) ~ ; } } \\ &  \quad \mathrm { ~ \boldsymbol { r } ~ \mathbf { \sigma } _ { \mathrm { ( } \mathrm { S } } , \mathbf { \sigma } _ { \mathrm { M } } ) ~ = ~ \mathbf { r } ~ ( \mathbf { k } : \mathbf { n } ) ~ \sigma ~ < \mathbf { \sigma } _ { \mathrm { c r } } ( \mathbf { \sigma } _ { \mathrm { M } } ; \mathbf { n } ) . } \end{array}$ end   
end

The Householder algorithm for least squares problems is normwise backward stable. Theorem 2.2.3 can be extended to give the following columnwise backward error bounds. Essentially the same result holds for Givens QR factorization.

Theorem 2.2.6. Suppose that the full-rank least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ ， $m \geq n$ is solved by Householder QR factorization. Then the computed solution $\hat { x }$ is the exact least squares solution to a slightly perturbed problem

$$
\operatorname* { m i n } _ { x } \| ( A + \delta A ) x - ( b + \delta b ) \| _ { 2 } ,
$$

where $\| \delta \boldsymbol { a } _ { j } \| _ { 2 } \leq n \gamma _ { m n } \| \boldsymbol { a } _ { j } \| _ { 2 } , j = 1 , \ldots , n ,$ and $\| \delta \boldsymbol { b } \| _ { 2 } \leq \gamma _ { m n } \| \boldsymbol { b } \| _ { 2 }$

Proof. See Higham [623, 2002, Theorem 20.3].

In some applications it is important that the computed residual vector $\bar { r }$ be accurately orthogonal to $\mathcal { R } ( A )$ . The backward stability of Householder QR means that the residual computed

from (2.2.40) satisfies

$$
( A + E ) ^ { T } \bar { r } = 0 , \quad \| E \| _ { 2 } \leq c \mathbf { u } \| A \| _ { 2 } ,
$$

for some constant $c = c ( m , n )$ . Hence $A ^ { T } \bar { r } = - E ^ { T } \bar { r }$ and

$$
\| A ^ { T } \bar { r } \| _ { 2 } \leq c \mathbf { u } \| \bar { r } \| _ { 2 } \| A \| _ { 2 } .
$$

Now assume that the residual is computed instead from $\widetilde { \boldsymbol { r } } = f l ( \boldsymbol { b } - f l ( \boldsymbol { A } \boldsymbol { x } ) )$ , where $x$ is the exact least squares solution. Then $A ^ { T } r = 0$ ,and the error analysis for (1.4.11) for inner products gives $| A ^ { T } \tilde { r } | < \gamma _ { n + 1 } | A ^ { T } | ( | b | + | A | | x | )$ . It follows that

$$
\begin{array} { r } { \| A ^ { T } \widetilde { r } \| _ { 2 } \leq n ^ { 1 / 2 } \gamma _ { n + 1 } \| A \| _ { 2 } ( \| b \| _ { 2 } + n ^ { 1 / 2 } \| A \| _ { 2 } \| x \| _ { 2 } ) . } \end{array}
$$

This bound is much weaker than the bound (2.2.42) valid for the Householder QR method, particularly when $\lVert \bar { r } \rVert _ { 2 } \ll \lVert b \rVert _ { 2 }$

Let $A ^ { T } y = c$ be an underdetermined linear system, where $A \in \mathbb { R } ^ { m \times n }$ has full row rank $n$ Then the least-norm solution $y \in \mathbb { R } ^ { m }$ can be computed from the Householder QR factorization of $A$ as follows. We have $A ^ { T } = \left( R ^ { T } \quad 0 \right) Q ^ { T }$ and

$$
A y = ( R ^ { T } 0 ) z = c , \quad z = Q ^ { T } y = { \binom { z _ { 1 } } { z _ { 2 } } } .
$$

Since $\| y \| _ { 2 } = \| z \| _ { 2 }$ , the problem is reduced to $\operatorname* { m i n } \| z _ { 1 } \| _ { 2 }$ subject to $R ^ { T } z _ { 1 } = c$ Clearly the least-norm solution is obtained by setting $z _ { 2 } = 0$ ,and

$$
R ^ { T } z _ { 1 } = c , \qquad y = Q \left( { z _ { 1 } \atop 0 } \right) .
$$

The resulting Householder QR algorithm (2.2.44) is backward stable.

Theorem 2.2.7.Assume that the least-norm solution of $A ^ { T } y = c$ is computed by Householder QR factorization of $A \in \mathbb { R } ^ { m \times n }$ ， $\operatorname { r a n k } ( A ) = n$ Then the computed solution $\hat { x }$ is the exact least-norm solution to a slightly perturbed system $( A + \delta A ) ^ { T } y = ( c + \delta c )$ ，where

$$
\| \delta \boldsymbol { a } _ { j } \| _ { F } \leq n \gamma _ { m n } \| \boldsymbol { a } _ { j } \| _ { F } , \quad j = 1 , \ldots , n , \qquad \| \delta \boldsymbol { c } \| _ { 2 } \leq \gamma _ { m n } \| \boldsymbol { c } \| _ { 2 } .
$$

Proof. See Higham [623, 20o2,Theorem 21.4]. (This result from 2002 was first published here; see Notes and References at the end of Chapter 21.) □

When $\operatorname { r a n k } ( A ) = n$ ,the pseudoinverses of $A$ and $A ^ { T }$ can be expressed in terms of the QR factorization as

$$
A ^ { \dagger } = R ^ { - 1 } Q _ { 1 } ^ { T } , \qquad ( A ^ { T } ) ^ { \dagger } = Q _ { 1 } R ^ { - T } .
$$

The Householder QR algorithms for the least squares and minimum norm problems are special cases of a general QR algorithm for solving the augmented system

$$
{ \left( \begin{array} { l l } { I } & { A } \\ { A ^ { T } } & { 0 } \end{array} \right) } { \left( \begin{array} { l } { y } \\ { x } \end{array} \right) } = { \left( \begin{array} { l } { b } \\ { c } \end{array} \right) } , \quad b \in \mathbb { R } ^ { m } , \quad c \in \mathbb { R } ^ { n } ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ ， $\operatorname { r a n k } ( A ) = n$ . From the QR factorization of $A$ we obtain

$$
y + Q \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) x = b , \qquad ( R ^ { T } \quad 0 ) Q ^ { T } y = c .
$$

Multiplying the first equation by $Q ^ { T }$ and the second by $R ^ { - T }$ , we get

$$
Q ^ { T } y + \left( \begin{array} { l } { R } \\ { 0 } \end{array} \right) x = Q ^ { T } b , \qquad \left( \begin{array} { l l } { I _ { n } } & { 0 } \end{array} \right) Q ^ { T } y = R ^ { - T } c .
$$

The second equation can be used to eliminate the first $n$ components of $Q ^ { T } y$ in the first equation to solve for $x$ . The last $m - n$ components $d _ { 2 }$ of $Q ^ { T } y$ are obtained from the last $m - n$ equations in the first equation. The resulting QR algorithm for solving the augmented system (2.2.46) is summarized below.

Algorithm 2.2.6 (Augmented System Solution by Householder QR). Compute the House-holder QR factorization of $A \in \mathbb { R } ^ { m \times n }$ ， $\operatorname { r a n k } ( A ) = n$ ,and

$$
\begin{array} { c c } { { z = R ^ { - T } c , } } & { { d = \left( \begin{array} { c } { { d _ { 1 } } } \\ { { d _ { 2 } } } \end{array} \right) = Q ^ { T } b , } } \\ { { x = R ^ { - 1 } ( d _ { 1 } - z ) , } } & { { y = Q \left( \begin{array} { c } { { z } } \\ { { d _ { 2 } } } \end{array} \right) . } } \end{array}
$$

The algorithm requires triangular solves with $R$ and $R ^ { T }$ and multiplications of vectors with $Q$ and $Q ^ { T }$ for a total of $8 m n - 2 n ^ { 2 }$ flops. Higham [618,1991] gives a componentwise error analysis of this algorithm, which is of importance in the analysis of iterative refinement of least squares solution; see Section 2.5.3.

Lemma 2.2.8 (Higham 1991). Let $A \in \mathbb { R } ^ { m \times n }$ ， $\operatorname { r a n k } ( A ) = n$ ， and suppose the augmented system is solved by the algorithm in (2.2.47)-(2.2.48) using Householder or Givens QR factorization. Then the computed $\bar { x }$ and $\bar { y }$ satisfy

$$
\left( { \begin{array} { c c } { I } & { A + E _ { 1 } } \\ { ( A + E _ { 2 } ) ^ { T } } & { 0 } \end{array} } \right) \left( { \begin{array} { c } { { \bar { y } } } \\ { { \bar { x } } } \end{array} } \right) = \left( { \begin{array} { l } { b + e _ { 1 } } \\ { c + e _ { 2 } } \end{array} } \right) ,
$$

where

$$
\begin{array} { r l } & { | E _ { i } | \leq \mu _ { m , n } G | A | , \quad i = 1 , 2 , } \\ & { | e _ { 1 } | \leq \mu _ { m , 1 } ( H _ { 1 } | b | + H _ { 2 } | \bar { y } | ) , \qquad | e _ { 2 } | \leq \mu _ { m , 1 } | A ^ { T } | H _ { 3 } | \bar { y } | , } \end{array}
$$

$$
\begin{array} { r l r } & { \| G \| _ { 2 } \leq 3 m n ( 1 + \theta _ { m , n } ) , \quad } & { \| H _ { 1 } \| \leq 3 m ^ { 3 / 2 } ( 1 + \theta _ { m , 1 } ) , } \\ & { \| H _ { 2 } \| \leq 5 m ^ { 3 / 2 } ( 1 + \theta _ { m , 1 } ) , \quad } & { \| H _ { 2 } \| \leq 7 m ^ { 3 / 2 } \mu _ { m , 1 } ( 1 + \theta _ { m , 1 } ) , } \\ & { \theta _ { m , n } = \displaystyle \frac { 2 \mu _ { m , n } ( m ( n - 1 ) ) ^ { 1 / 2 } } { 1 - 2 \mu _ { m , n } ( m ( n - 1 ) ) ^ { 1 / 2 } } , } \end{array}
$$

where $\gamma _ { n } = n \mathbf { u } / ( 1 - n \mathbf { u } )$ and $\mu _ { m , n } = \gamma _ { a m + b n + c }$

# 2.2.4 - Gram-Schmidt QR factorization

The earliest orthogonalization methods for solving least squares problems used Gram-Schmidt orthogonalization,where an orthonormal matrix $Q \in \mathbb { R } ^ { m \times m }$ is formed explicitly as a linear combination of the columns of $A$ . Gram-Schmidt orthogonalization is a well-known standard topic in elementary linear algebra textbooks. If used correctly, this has excellent stability proper-ties. Unfortunately, incorrect descriptions are still found in textbooks and elsewhere, particularly in statistics.

Gram-Schmidt orthogonalization is a process that, from a linearly independent sequence $\{ x _ { n } \}$ of members of a finite or infinite inner-product space $s$ ,forms an orthogonal sequence $\left\{ q _ { n } \right\}$ as

$$
q _ { 1 } = x _ { 1 } , \qquad q _ { n } = x _ { n } - \sum _ { k = 1 } ^ { n - 1 } { \frac { \langle q _ { k } , x _ { n } \rangle } { \| q _ { k } \| ^ { 2 } } } q _ { k } ,
$$

where $\langle \cdot , \cdot \rangle$ denotes the inner product. By construction, $\langle q _ { j } , q _ { k } \rangle = 0$ ， $j \neq k$ , and span $( q _ { 1 } , \dots , q _ { k } )$ $= \operatorname { s p a n } \left( x _ { 1 } , \ldots , x _ { k } \right)$ ， $k \geq 1$ .Replacing each $q _ { n }$ by $q _ { n } / \lVert q _ { n } \rVert$ gives an orthonormal sequence. Having an orthogonal basis for this nested sequence of subspaces simplifies many operations.

Given $A = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } ) \in \mathbb { R } ^ { m \times n }$ with linearly independent columns, the Gram-Schmidt process computes a matrix factorization

$$
A = Q R = ( q _ { 1 } , q _ { 2 } , \ldots , q _ { n } ) \left( \begin{array} { r r r r } { { r _ { 1 1 } } } & { { r _ { 1 2 } } } & { { \ldots } } & { { r _ { 1 n } } } \\ { { } } & { { r _ { 2 2 } } } & { { \ldots } } & { { r _ { 2 n } } } \\ { { } } & { { \ddots } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { r _ { n n } } } \end{array} \right) ,
$$

such that $Q = ( q _ { 1 } , q _ { 2 } , \ldots , q _ { n } ) \in \mathbb { R } ^ { m \times n }$ is orthonormal and $R \in \mathbb { R } ^ { n \times n }$ upper triangular. The difference between Gram-Schmidt and Householder QR factorizations has been aptly formulated by Trefethen and Bau [1068,1997,p.70]: Gram-Schmidt is triangular orthogonalization, whereas Householder is orthogonal triangularization.

The Classical Gram-Schmidt (CGS) algorithm applied to $A = \left( a _ { 1 } , \ldots , a _ { n } \right)$ proceeds in $n$ steps, $k = 1 , \ldots , n$ . In step $k$ the vector $a _ { k }$ is orthogonalized against $Q _ { k - 1 } = \left( q _ { 1 } , \ldots , q _ { k - 1 } \right)$ ， giving

$$
\widehat { \boldsymbol { a } } _ { k } = \big ( I - Q _ { k - 1 } Q _ { k - 1 } ^ { T } \big ) \boldsymbol { a } _ { k } = \boldsymbol { a } _ { k } - Q _ { k - 1 } \boldsymbol { r } _ { k } , \quad \boldsymbol { r } _ { k } = Q _ { k - 1 } ^ { T } \boldsymbol { a } _ { k } .
$$

Then $q _ { k }$ is obtained by normalizing $\widehat { a } _ { k } \colon r _ { k k } = \| \widehat { a } _ { k } \| _ { 2 } , q _ { k } = \widehat { a } _ { k } / r _ { k k }$ . Note that if $a _ { 1 } , \ldots , a _ { k }$ are linearly independent, then $r _ { k k } > 0$

# Algorithm 2.2.7 (Classical Gram-Schmidt).

function $\left[ { \tt Q } , { \tt R } \right] \ = \ \tt c \tt g \tt s \left( { \tt A } \right)$ ； $\%$ CGS computes the thin $\mathbb { Q R }$ factorization of A $\%$ by Classical Gram--Schmidt $\%$ 1 $\mathrm { [ m , n ] ~ = ~ \ s i z e ( A ) : }$ ${ \sf Q } =$ zeros(m,n)； R = zeros(n); ${ \mathfrak { q } } \mathbf { k } \ = \ \mathtt { A } ( : , \mathbf { k } )$ for $\mathtt { k } \ = \ 1 { : } \mathtt { n }$ if $\texttt { k } > \texttt { 1 }$ $\begin{array} { r l } & { \mathtt { R } ( 1 { : } \mathrm { k } { - } 1 , \mathrm { k } ) \ = \ \mathtt { Q } ( : , 1 { : } \mathrm { k } { - } 1 ) \ { : } \mathrm { * { q } } \mathrm { k } ; } \\ & { \mathtt { q } \mathrm { k } \ = \ \mathtt { q } \mathrm { k } - \ \mathtt { Q } ( : , 1 { : } \mathrm { k } { - } 1 ) { * } \mathrm { R } ( 1 { : } \mathrm { k } { - } 1 , \mathrm { k } ) ; } \end{array}$ end $\begin{array} { r l } { { \sf R } \left( { \bf k } , { \bf k } \right) } & { = { \sf n o r m } \left( { \sf q } { \bf k } \right) ; } \\ { { \sf q } \left( : , { \bf k } \right) } & { = { \sf q } { \bf k } / { \sf R } \left( { \bf k } , { \bf k } \right) ; } \end{array}$ end end

In step $k$ of CGS the first $k - 1$ elements of the $k$ th column of $R$ are computed. CGS is therefore called a columnwise or left-looking algorithm. The main work in CGS is performed in two matrix-vector products. By omitting the normalization of $a _ { k }$ ,a square-root-free CGS algorithm can be obtained. This gives a factorization $A = Q R$ ，where $\hat { R }$ is unit upper triangular and $Q ^ { T } Q = D$ ，a positive diagonal matrix. The CGS algorithm requires approximately $2 m n ^ { 2 }$ flops. This is $2 n ^ { 3 } / 3$ flops more than required for Householder QR.

The modified Gram-Schmidt (MGS） algorithm is a slightly different way to carry out Gram-Schmidt orthogonalization. As soon as a new column $q _ { k }$ has been computed,all remaining columns are orthogonalized against it. This determines the $k$ th row of $R$ .Hence MGS is a row-oriented or right-looking algorithm.At the start of step $k$ the matrix $A = A ^ { ( 1 ) }$ has been transformed into

$$
( Q _ { k - 1 } \quad A ^ { ( k ) } ) = \big ( q _ { 1 } , \dots , q _ { k - 1 } , a _ { k } ^ { ( k ) } , \dots , a _ { n } ^ { ( k ) } \big ) ,
$$

were the columns n $A ^ { ( k ) }$ are orthgonal to $Q _ { k - 1 }$ . Normalizing he etor $a _ { k } ^ { ( k ) }$ gives

$$
r _ { k k } = \| a _ { k } ^ { ( k ) } \| _ { 2 } , \quad q _ { k } = a _ { k } ^ { ( k ) } / r _ { k k } .
$$

$a _ { j } ^ { ( k ) } , j = k , \dots , n$ is orthogonalied to $q _ { k }$

$$
a _ { j } ^ { ( k + 1 ) } = ( I - q _ { k } q _ { k } ^ { T } ) a _ { j } ^ { ( k ) } = a _ { j } ^ { ( k ) } - r _ { k j } q _ { k } , \quad r _ { k j } = q _ { k } ^ { T } a _ { j } ^ { ( k ) } .
$$

This determines the remaining elements in the $k$ th row of $R$

# Algorithm 2.2.8 (Modified Gram-Schmidt).

function $\left[ { \mathbb Q } , { \mathbb R } \right] \ = \ \mathrm { m g } { \mathbf s } \left( { \mathbb A } \right)$ ； $\%$ Computes the thin $\mathbb { Q R }$ factorization of A $\%$ by rowwise modified Gram--Schmidt. %- $\mathrm { [ m , n ] \ = \ s i z e \left( A \right) }$ ； ${ \sf \sf \sf \sf \sf \sf \sf } \left( \sf \sf \sf \Psi \right) \sf = \sf \sf \sf \sf \sf \sf \sf A $ ； $\mathrm { ~ \textsf ~ { ~ R ~ } ~ } =$ zeros(n); for $\mathtt { k } \ = \ 1 { : } \mathtt { n }$ $\begin{array} { r l } & { \mathrm {  ~ \gamma ~ } _ { \mathrm { { A } } } ^ { \mathrm { { \tiny ~ \scriptstyle ~ \mathscr ~ { ~ x ~ } ~ } } } = \mathrm { {  ~ \pi ~ } } _ { \mathrm { { n } } } \mathrm { { o r m } } \left( \mathrm { { q k } } \right) ; } \\ & { \mathrm {  ~ \gamma ~ } _ { \mathrm { { Q } } } ^ { \mathrm { { \tiny ~ \scriptstyle ~ \vec ~ { k ~ } ~ } } } \mathrm { { \Sigma } } _ { \mathrm { { { B } } } } ^ { \mathrm { { \tiny ~ \vec ~ { ~ x ~ } ~ } } } = \mathrm { { \Lambda } } _ { \mathrm { { { Q } } } } \left( \mathrm { { \dot { \Sigma } } } , \mathrm { { k } } \right) / \mathrm { { R } } \left( \mathrm { { k } } , \mathrm { { k } } \right) ; } \\ & { \mathrm { \ q } _ { \mathrm { { E } } } ^ { \mathrm { { \tiny ~ \vec ~ { ~ } } } } = \mathrm { { \Lambda } } _ { \mathrm { { { { Q } } } } } ^ { \mathrm { { \tiny ~ \vec ~ { ~ k ~ } } } } ; } \\ & { \mathrm { \ i f ~ { \vec ~ { ~ k ~ } } ~ } \mathrm { { \Sigma } } ^ { \mathrm { { \tiny ~ \vec ~ { ~ k ~ } } } } \mathrm { { \Sigma } } ^ { \mathrm { { \tiny ~ \vec ~ { ~ x ~ } ~ } } } } \\ & { \mathrm { \ q } \left( \mathrm { { \bf \Sigma } } , \mathrm { { k } } + 1 : \mathrm { { n } } \right) \ = \ \mathrm { { q } } \left( \mathrm { { \dot { \Sigma } } } , \mathrm { { k } } + 1 : \mathrm { { n } } \right) \ - \ \mathrm { { q } } \mathrm { { k } } { * \mathrm { R } } \left( \mathrm { { k } } , \mathrm { { k } } + 1 : \mathrm { { n } } \right) ; } \end{array}$ end end

Note that in MGS the orthogonalization of $a _ { k }$ is carried out as the product

$$
a _ { k } ^ { ( k ) } = ( I - q _ { k - 1 } q _ { k - 1 } ^ { T } ) \cdot \cdot \cdot ( I - q _ { 1 } q _ { 1 } ^ { T } ) a _ { k } .
$$

This can becomparedto the expression a) )=(I-Qk-1QT-1)ak used inCGS.Ifq1,.., qk-1 are exactly orthonormal, these two expressions are equivalent. However, this will not be the case in finite-precision arithmetic,and MGS is not numerically equivalent to CGS for $n > 2$

As described above,MGS is a rowwise or right-looking algorithm.In applications where the columns of $A$ are generated one at a time, or when MGS is applied to an additional right-hand side $b$ of a least squares problem, a columnwise (or left-looking) version of MGS must be used. In columnwise MGS, the same arithmetic operations as are performed as in rowwise MGS,and only the temporal sequence of the operations is different. Then rounding errors are the same,and the two versions of MGS produce exactly the same numerical results. The difference between

CGS and MGS is subtle and has often gone unnoticed or been misunderstood. Wilkinson [1122, 1971, p. 559] writes“Iused the modified process for many years without even explicitly noticing that I was not performing the classcal algorithm.’ Columnwise versions of MGS have been used by Schwarz,Rutishauser,and Stiefel [978,1968]; see also Gander [437,198o] and Longley [757, 1981].

# Algorithm 2.2.9 (Columnwise MGS).

function $\left[ { \sf q } , { \sf R } \right] = \mathrm { m } { \sf g } { \sf s } { \sf c } \left( { \sf A } \right)$ ； $\%$ Computes the thin $\mathbb { Q R }$ factorization of A $\%$ by columnwise modified Gram--Schmidt % $\mathrm { [ m , n ] \ = \ s i z e \left( A \right) }$ ； ${ \sf Q } =$ zeros(m,n)； R = zeros(n); for $\mathtt { k } \ = \ 1 { : } \mathtt { n }$ $\mathfrak { q k } \ = \ \mathtt { A } ( : , \mathtt { k } )$ ； for $\dot { \mathrm { ~ \scriptsize ~ i ~ } } = \mathrm { ~ \scriptsize ~ 1 : ~ k - 1 ~ }$ $\begin{array} { r l } { \mathtt { R } ( \mathtt { i } , \mathtt { k } ) } & { = \mathtt { Q } ( : , \mathtt { i } ) \ ^ { * } \mathtt { q } \mathtt { k } ; } \\ { \mathtt { A } ( : , \mathtt { k } ) } & { = \mathtt { A } ( : , \mathtt { k } ) \ \mathtt { \Omega } - \ \mathtt { Q } ( : , \mathtt { i } ) * \mathtt { R } ( \mathtt { i } , \mathtt { k } ) ; } \end{array}$ end $\begin{array} { r l } { { \sf R } \left( { \bf k } , { \bf k } \right) } & { = { \sf n o r m } \left( { \sf q } { \bf k } \right) ; } \\ { { \sf q } \left( : , { \bf k } \right) } & { = { \sf q } { \bf k } / { \sf R } \left( { \bf k } , { \bf k } \right) ; } \end{array}$ end   
end

In CGS and rowwise MGS algorithms virtually all operations can be implemented as matrixvector operations. These versions can be made to execute more eficiently than columnwise MGS,which uses vector operations. They also offer more scope for parallel implementations. These aspects are important in deciding which variant should be used in a particular application.

Rice [926,1g66] was the first to establish the superior stability properties of MGS.Both CGS and MGS can be shown to accurately reproduce $A$ ，

$$
A + E _ { 1 } = \bar { Q } \bar { R } , \quad \| E _ { 1 } \| _ { 2 } < c _ { 1 } \mathbf { u } \| A \| _ { 2 } ,
$$

where $c _ { 1 } = c _ { 1 } ( m , n )$ is a small constant.

Rounding errors will occur when the orthogonal projections onto previous vectors $q _ { i }$ are subtracted. These errors will propagate to later stages of the algorithm and cause a (sometimes severe) loss of orthogonality in the computed $Q$ .However, as shown by Bjorck[125,1g67], for MGS the loss of orthogonality can be bounded by a factor proportional to $\kappa ( A )$

Theorem 2.2.9. Let $\bar { Q }$ denote the orthogonal factor computed by the MGS algorithm. Then, provided that $c _ { 2 } \kappa _ { 2 } ( A ) \mathbf { u } < 1$ ，there is a constant $c _ { 2 } = c _ { 2 } ( m , n )$ such that

$$
\left\| I - \bar { Q } ^ { T } \bar { Q } \right\| _ { 2 } \leq \frac { c _ { 2 } \kappa _ { 2 } ( A ) \mathbf { u } } { 1 - c _ { 2 } \kappa _ { 2 } ( A ) \mathbf { u } } .
$$

The loss of orthogonality in CGS can be much more severe. Gander [437,198o] points out that even Cholesky QR factorization often gives better orthogonality than CGS. For the standard version of CGS,not even a bound proportional to $\kappa ( A ) ^ { 2 }$ holds unless a slightly altered "Pythagorean variant” of CGS is used, in which the diagonal entry $r _ { k k }$ is computed as

$$
r _ { k k } = ( s _ { k } ^ { 2 } - p _ { k } ^ { 2 } ) ^ { 1 / 2 } = ( s _ { k } - p _ { k } ) ^ { 1 / 2 } ( s _ { k } + p _ { k } ) ^ { 1 / 2 } ,
$$

where $s _ { k } = \| a _ { k } \| _ { 2 }$ and $p _ { k } = ( r _ { 1 k } ^ { 2 } + \cdot \cdot \cdot + r _ { k - 1 , k } ^ { 2 } ) ^ { 1 / 2 }$ .For hisvrant,Smoktunowiczarlow, and Langou [1006, 2oo6] were able to prove the upper bound

$$
\| I - \bar { Q _ { 1 } } ^ { T } \bar { Q _ { 1 } } \| _ { 2 } \leq c _ { 2 } ( m , n ) \kappa _ { 2 } ( A ) ^ { 2 } .
$$

Example 2.2.10. To ilustrate the difference in loss of orthogonality of MGS and CGS,we use a matrix $A \in \mathbb { R } ^ { 5 0 \times 1 0 }$ with singular values $\sigma _ { i } = 1 0 ^ { - i + 1 }$ ， $i = 1 { : } 1 0$ generated by computing

$$
A = U D V ^ { T } , \quad D = \mathrm { d i a g } ( 1 , 1 0 ^ { - 1 } , \ldots , 1 0 ^ { - 9 } ) .
$$

Here $U$ and $V$ are random orthonormal matrices from the Haar distribution generated by an algorithm of Stewart [1O19,198o] that uses products of Householder matrices with randomly chosen Householder vectors． Table 2.2.1 shows $\kappa ( A _ { k } )$ ， $A _ { k } \ = \ ( a _ { 1 } , \ldots , a _ { k } )$ ，and the loss of orthogonality in CGS and MGS as measured by $\lVert I _ { k } - Q _ { k } ^ { T } Q _ { k } \rVert _ { 2 }$ for $k = 1 , \ldots , 1 0$ . As expected, the loss of orthogonality in the computed factor $Q$ for MGS is proportional to $\kappa ( A _ { k } )$ . For CGS the loss is much worse. CGS is therefore often used with reorthogonalization; see Section 2.2.7.

Table 2.2.1. Condition number and loss of orthogonality in CGS and MGS.   

<table><tr><td>k</td><td>K(Ak)</td><td>Ik-QTQcll2</td><td>|Ik -QMQmll2</td></tr><tr><td>1</td><td>1.000e+00</td><td>1.110e-16</td><td>1.110e-16</td></tr><tr><td>2</td><td>1.335e+01</td><td>2.880e-16</td><td>2.880e-16</td></tr><tr><td>3</td><td>1.676e+02</td><td>7.295e-15</td><td>8.108e-15</td></tr><tr><td>4</td><td>1.126e+03</td><td>2.835e-13</td><td>4.411e-14</td></tr><tr><td>5</td><td>4.853e+05</td><td>1.973e-09</td><td>2.911e-11</td></tr><tr><td>6</td><td>5.070e+05</td><td>5.951e-08</td><td>3.087e-11</td></tr><tr><td>7</td><td>1.713e+06</td><td>2.002e-07</td><td>1.084e-10</td></tr><tr><td>8</td><td>1.158e+07</td><td>1.682e-04</td><td>6.367e-10</td></tr><tr><td>9</td><td>1.013e+08</td><td>3.330e-02</td><td>8.779e-09</td></tr><tr><td>10</td><td>1.000e+09</td><td>5.446e-01</td><td>4.563e-08</td></tr></table>

It is important to note that all Gram-Schmidt algorithms are invariant under column scalings, Let $D > 0$ be a diagonal matrix. Then the Gram-Schmidt algorithms applied to the scaled matrix $\widetilde { A } = A D$ will yield the factors $\widetilde Q = Q$ and ${ \widetilde { R } = R D }$ .This is true also in floating-point arithmetic,provided that the entries of $D$ are powers of two so that the scaling is done without error. From the invariance under column scaling it follows that $\kappa _ { 2 } ( A )$ in (2.2.56) can be replaced by

$$
{ \widetilde { \kappa } } _ { 2 } = \operatorname* { m i n } _ { D \in { \mathcal { D } } } \kappa _ { 2 } ( A D ) ,
$$

where $\mathcal { D }$ is the set of all positive diagonal matrices. Scaling $A$ so that all column norms in $A$ are equal will approximately minimize $\kappa _ { 2 } ( A D )$ ; see Theorem .1.5.

# Notes and references

The history of Gram-Schmidt orthogonalization is surveyed by Leon, Bjorck, and Gander [733, 2013].What is now called the “classical" Gram-Schmidt (CGS) algorithm appeared in Schmidt [971,1907],[972,19o8] in the context of solving linear systems with infinitely many unknowns. Schmidt remarked that his formulas were similar to those given earlier by J. P. Gram [525,1883] in a paper on series expansions of real functions using least squares. Gram used the “modified" Gram-Schmidt (MGS) algorithm for orthogonalizing a sequence of functions and applied the results to applications involving integral equations. Gram was influenced by the work of Chebyshev, and his original orthogonalization procedure was applied to orthogonal polynomials.

The earliest linkage of the names Gram and Schmidt to describe the orthonormalization process appears to be in a paper by Wong [1130,1935]. A process similar to MGS had already been used by Laplace [721,18i6] for solving a least squares problem; see Farebrother [396, 1988] and Langou [720,2oog]. However,Laplace seems not to have recognized the crucial role of orthogonality. Bienaymé [118,1853] developed a similar process related to an interpolation algorithm of Cauchy [212,1837] that forms the basis of Thiele's theory of linear estimation.

# 2.2.5 - MGS as a Householder Method

The results in Theorem 2.2.9 on the stability of MGS are quite satisfactory but fall short of proving backward stability.A surprising observation due to Charles Sheffeld is that the MGS algorithm can be interpreted as Householder QR factorization applied to the matrix $A \in \mathbb { R } ^ { m \times n }$ augmented with a square matrix of zero elements on top. This is not only true in theory but also holds numerically in the presence of rounding errors.We now outline this relationship in more detail. We denote the augmented QR factorization by

$$
\widetilde { A } \equiv \left( { O _ { n } } \right) = P \left( { \begin{array} { l } { { \widetilde { R } } } \\ { { 0 } } \end{array} } \right) = \left( { P _ { 1 1 } } \quad { P _ { 1 2 } } \right) \left( { \begin{array} { l } { { \widetilde { R } } } \\ { { 0 } } \end{array} } \right) ,
$$

where $P \in \mathbb { R } ^ { ( n + m ) \times ( n + m ) }$ and $P _ { 1 1 } \in \mathbb { R } ^ { n \times n }$ ．Recall that the Householder transformation $P a = e _ { 1 } \rho$ uses

$$
P = I - 2 { v v } ^ { T } / \| v \| _ { 2 } ^ { 2 } , \quad v = a - e _ { 1 } \rho , \quad \rho = \pm \| a \| _ { 2 }
$$

$\scriptstyle { \mathcal { C } } k$ is the $k$ th column of the unit matrix). If (2.2.6O) is obtained using Householder transformations, then

$$
P ^ { T } = P _ { n } \cdot \cdot \cdot P _ { 2 } P _ { 1 } , \qquad P _ { k } = I - 2 \hat { v } _ { k } \hat { v } _ { k } ^ { T } / \| \hat { v } _ { k } \| _ { 2 } ^ { 2 } , \qquad k = 1 : n ,
$$

where the vectors $\hat { v } _ { k }$ are as described below.From MGS applied to $A ^ { ( 1 ) } = A$ ， $r _ { 1 1 } = \| a _ { 1 } ^ { ( 1 ) } \| _ { 2 }$ and a $a _ { 1 } ^ { ( 1 ) } = q _ { 1 } ^ { \prime } = q _ { 1 } r _ { 1 1 }$ . Thus,for the first Householder transformation applied to the augmented matrix,

$$
\begin{array} { r l r } & { \widetilde { A } ^ { ( 1 ) } \equiv \left( \begin{array} { c } { O _ { n } } \\ { A ^ { ( 1 ) } } \end{array} \right) , \quad } & { \widetilde { a } _ { 1 } ^ { ( 1 ) } = \left( \begin{array} { c } { 0 } \\ { a _ { 1 } ^ { ( 1 ) } } \end{array} \right) , } \\ & { } & \\ & { \hat { v } _ { 1 } ^ { ( 1 ) } \equiv \left( \begin{array} { c } { - e _ { 1 } r _ { 1 1 } } \\ { q _ { 1 } ^ { \prime } } \end{array} \right) = r _ { 1 1 } v _ { 1 } , \quad } & { v _ { 1 } = \left( \begin{array} { c } { - e _ { 1 } } \\ { q _ { 1 } } \end{array} \right) } \end{array}
$$

(and since there can be no cancellation, we take $r _ { k k } \ge 0$ ). But $\| v _ { 1 } \| _ { 2 } ^ { 2 } = 2$ , giving

$$
P _ { 1 } = I - 2 \hat { v } _ { 1 } \hat { v } _ { 1 } ^ { T } / \| \hat { v } _ { 1 } \| _ { 2 } ^ { 2 } = I - 2 v _ { 1 } v _ { 1 } ^ { T } / \| v _ { 1 } \| _ { 2 } ^ { 2 } = I - v _ { 1 } v _ { 1 } ^ { T }
$$

and

$$
P _ { 1 } \widetilde { a } _ { j } ^ { ( 1 ) } = \widetilde { a } _ { j } ^ { ( 1 ) } - v _ { 1 } v _ { 1 } ^ { T } \widetilde { a } _ { j } ^ { ( 1 ) } = \left( { \small \begin{array} { c } { 0 } \\ { a _ { j } ^ { ( 1 ) } } \end{array} } \right) - \left( { \small \begin{array} { c } { - e _ { 1 } } \\ { q _ { 1 } } \end{array} } \right) q _ { 1 } ^ { T } a _ { j } ^ { ( 1 ) } = \left( { \small \begin{array} { c } { e _ { 1 } r _ { 1 j } } \\ { a _ { j } ^ { ( 2 ) } } \end{array} } \right) ,
$$

SO

$$
P _ { 1 } \widetilde { A } ^ { ( 1 ) } = \left( \begin{array} { c c c c c } { { r _ { 1 1 } } } & { { r _ { 1 2 } } } & { { \cdots } } & { { r _ { 1 n } } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { a _ { 2 } ^ { ( 2 ) } } } & { { \cdots } } & { { a _ { n } ^ { ( 2 ) } } } \end{array} \right) ,
$$

where these values are clearly numerically the same as in the first step of MGS on $A$ . The next Householder transformation produces thesecond rowof $R$ and $a _ { 3 } ^ { ( 3 ) } , \ldots , a _ { n } ^ { ( 3 ) }$ , just as in MGS. We have

$$
{ \widetilde Q } ^ { T } \left( \begin{array} { c } { { 0 } } \\ { { A } } \end{array} \right) = \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) , \quad { \widetilde Q } ^ { T } = { \widetilde H } _ { n } \cdot \cdot \cdot { \widetilde H } _ { 2 } { \widetilde H } _ { 1 } ,
$$

where $\widetilde { H } _ { k } = I - 2 \hat { v } _ { k } \hat { v } _ { k } ^ { T } / \| \hat { v } _ { k } \| _ { 2 } ^ { 2 }$ ， $k = 1 : n$ ,are Householder reflectors. Because of the special structure of the augmented matrix, the Householder vectors $v _ { k }$ have the form

$$
\hat { \boldsymbol { v } } _ { k } = \left( \begin{array} { c } { - r _ { k k } \boldsymbol { e } _ { k } } \\ { \hat { \boldsymbol { q } } _ { k } } \end{array} \right) , \quad r _ { k k } = \| \hat { \boldsymbol { q } } _ { k } \| _ { 2 } ,
$$

where $e _ { k }$ denotes the $k$ th unit vector,and the sign is chosen so that $R$ has a positive diagonal. With $q _ { k } = \hat { q } _ { k } / r _ { k k }$ it follows that

$$
\widetilde { H } _ { k } = I - v _ { k } v _ { k } ^ { T } , \quad v _ { k } = \left( \begin{array} { c } { - e _ { k } } \\ { q _ { k } } \end{array} \right) , \quad \| v _ { k } \| _ { 2 } ^ { 2 } = 2 .
$$

Initially the first $n$ rows are empty. Hence, the scalar products of $v _ { k }$ with later columns will only involve $q _ { k }$ ,and as is easily verified, the quantities $r _ { k j }$ and $q _ { k }$ are numerically the same as in the MGS method. It follows that Householder QR is numerically equivalent to MGS applied to $A$ From the backward stability of Householder QR we have the following result.

Theorem 2.2.11._There exists an exactly orthonormal matrix $\hat { Q } _ { 1 } \in \mathbb { R } ^ { m \times n }$ such that for the computed matrix $\bar { R }$ in MGS it holds that

$$
\begin{array} { r } { A + E = \hat { Q } _ { 1 } \bar { R } , \quad \| \widetilde { E } \| _ { 2 } \leq c _ { 3 } { \mathbf u } \| A \| _ { 2 } , } \end{array}
$$

where $c _ { 3 } \equiv c _ { 2 } ( m , n )$ is a modest constant depending on $m$ and $n$

A consequence of this result is that the factor $\bar { R }$ computed by MGS is as good as the triangular factor obtained by using Householder or Givens QR.The result can be sharpened to show that $\bar { R }$ is the exact triangular QR factor of a matrix near $A$ in the columnwise sense; see Higham [623, 2002, Theorem 19.13].

For a matrix $Q _ { 1 } = ( q _ { 1 } , \ldots , q _ { n } ) $ with any sequence $q _ { 1 } , \ldots , q _ { n }$ of unit 2-norm vectors, the matrix $P = P _ { 1 } P _ { 2 } \cdot \cdot \cdot P _ { n }$ ,with

$$
P _ { k } = I - v _ { k } v _ { k } ^ { T } , \quad v _ { k } ^ { T } = ( - e _ { k } ^ { T } , q _ { k } ^ { T } ) ,
$$

has a very special structure. The following result holds without recourse to the MGS connection. As shown by Paige [862, 2oog] it can be used to simplify the error analysis of several other algorithms.

Theorem 2.2.12. Let $Q _ { 1 } = ( q _ { 1 } , \dots , q _ { n } ) \in \mathbb { R } ^ { m \times n }$ ， $\| q _ { k } \| _ { 2 } = 1$ $k = 1 : n$ , and define

$$
M _ { k } = I - q _ { k } q _ { k } ^ { T } , \qquad P _ { k } = I - v _ { k } v _ { k } ^ { T } , \quad v _ { k } = \binom { - e _ { k } } { q _ { k } } \in \mathbb { R } ^ { m + n } .
$$

Then

$$
P = P _ { 1 } P _ { 2 } \cdots P _ { n } = { \binom { P _ { 1 1 } } { Q _ { 1 } ( I - P _ { 1 1 } ) } } I - Q _ { 1 } ( I - P _ { 1 1 } ) Q _ { 1 } ^ { T } \quad )
$$

$$
\mathbf { \Psi } = \left( \begin{array} { c c c c c c } { 0 } & { q _ { 1 } ^ { T } q _ { 2 } } & { q _ { 1 } ^ { T } M _ { 2 } q _ { 3 } } & { \cdots } & { q _ { 1 } ^ { T } M _ { 2 } M _ { 3 } \cdots \cdot M _ { n - 1 } q _ { n } } \\ { 0 } & { 0 } & { q _ { 2 } ^ { T } q _ { 3 } } & { \cdots } & { q _ { 2 } ^ { T } M _ { 3 } M _ { 4 } \cdots M _ { n - 1 } q _ { n } } \\ { \vdots } & { \vdots } & { \vdots } & { \cdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { q _ { n - 1 } ^ { T } q _ { n } } & { q _ { n - 1 } ^ { T } M _ { n } } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { q _ { n } ^ { T } } \\ { q _ { 1 } } & { M _ { 1 } q _ { 2 } } & { M _ { 1 } M _ { 2 } q _ { 3 } } & { \cdots } & { M _ { 1 } M _ { 2 } \cdots M _ { n - 1 } q _ { n } } & { M _ { 1 } M _ { 2 } \cdots M _ { n } } \end{array} \right)
$$

The matrix $P$ is orthogonal and depends only on $Q _ { 1 }$ and the strictly upper triangular matrix $P _ { 1 1 }$ $P _ { 1 1 } = 0$ if and only if $Q _ { 1 } ^ { T } Q _ { 1 }$ is diagonal, and then

$$
P = \left( \begin{array} { c c } { { 0 } } & { { Q _ { 1 } ^ { T } } } \\ { { Q _ { 1 } } } & { { I - Q _ { 1 } Q _ { 1 } ^ { T } } } \end{array} \right) .
$$

Proof. See Bjorck and Paige [149,1992, Theorem 4.1].

# 2.2.6 - Least Squares Problems by MGS

Let $A = Q _ { 1 } R$ be the MGS QR factorization of $A \in \mathbb { R } ^ { m \times n }$ ， $\operatorname { r a n k } ( A ) = n$ . We first remark that to solve the least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ by forming $z = Q _ { 1 } ^ { T } b$ and then solving $R x = z$ is not a stable way to proceed.Unfortunately, this method is stillfound in some textbooks.A backward stable algorithm for computing $x$ is obtained by instead treating the right-hand side $b$ as an extra column of $A$ and applying MGS to the extended matrix

$$
\left( A \quad b \right) = \left( Q _ { 1 } \quad q _ { n + 1 } \right) \left( \begin{array} { c c } { { R } } & { { z } } \\ { { 0 } } & { { \rho } } \end{array} \right) .
$$

We can then express the residual as

$$
\begin{array} { c }  r = b - A x = ( A \begin{array} { c c } { { \displaystyle ( - x ) ( \begin{array} { c c } { { \displaystyle - x } } \\ { { 1 } } \end{array} ) = ( Q _ { 1 } } } & { { \displaystyle q _ { n + 1 } ) ( \begin{array} { c c } { { \displaystyle R } } & { { \displaystyle z } } \\ { { 0 } } & { { \rho } } \end{array} ) ( \begin{array} { c } { { \displaystyle - x } } \\ { { 1 } } \end{array} ) } } \\ { { = Q _ { 1 } ( z - R x ) + \rho q _ { n + 1 } , \quad \| q _ { n + 1 } \| _ { 2 } = 1 . } } \end{array} \end{array}
$$

If $q _ { n + 1 } \neq 0$ and is orthogonal to $Q _ { 1 }$ , it follows that $\| A x - b \| _ { 2 }$ is minimized when

$$
R x = \rho q _ { n + 1 } , \qquad s = \| r \| _ { 2 } = \rho .
$$

No assumption about the orthogonality of $Q _ { 1 }$ is needed for this to be true. However, if $\rho \ll \| b \| _ { 2 }$ ， then $q _ { n + 1 }$ fails to be accurately orthogonal to $\mathcal { R } ( A )$ . A backward stable $r$ is obtained by adding a reorthogonalization step,where the computed $r$ orthogonalized against $q _ { n } , \ldots , q _ { 2 } , q _ { 1 }$ in this order. The proof of backward stability of this algorithm for computing $x$ and $r$ is by no means obvious.It folows by noting that it is numerically equivalent to solvig

$$
\operatorname* { m i n } _ { x } \left\| \left( { \begin{array} { l } { 0 } \\ { A } \end{array} } \right) x - \left( { \begin{array} { l } { 0 } \\ { b } \end{array} } \right) \right\| _ { 2 }
$$

by Householder QR.Applying the Householder transformations to the right-hand side in (2.2.70) gives

$$
\binom { d } { e } = H _ { n } \cdot \cdot \cdot H _ { 1 } \binom { 0 } { b } .
$$

An implementation is given below.

# Algorithm 2.2.10 (Linear Least Squares by MGS).

function $\mathrm { [ x , r ] \ = \ m g s 2 s \mathrm { q } ( A , b ) }$ ； $\%$ Computes x and ${ \bf { r } } ~ = ~ { \bf { b } } ~ - ~ { \bf { A } } { \bf { x } }$ for the least $\%$ squares problem $\mathrm { m i n } \_ \mathbf { x } | \ | \textbf { b } \_ \mathrm { A x } | \ | \ \_ 2$ %- $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ size(A); $\left[ { \mathbb Q } , { \mathbb R } \right] \ = \ \mathfrak { m } \mathfrak { g } \mathfrak { s } \left( \mathbb A \right)$ ； d = zeros(n,1); for $\mathtt { k } \ = \ 1 { : } \mathtt { n }$ $\begin{array} { r l } & { \mathrm { d \left( \mathbf { k } \right) \ = \ 0 \left( : \Gamma , \mathbf { k } \right) \mathrm { \Sigma } ^ { \prime } \ast \mathbf { b } ; } } \\ & { \mathrm { ~ \mathbf { b } ~ = ~ \mathbf { b } _ \alpha - \nabla \ d \left( \mathbf { k } \right) \ast \mathbf { Q } \left( : \Gamma , \mathbf { k } \right) ; } } \end{array}$ end $\begin{array} { r l } & { \mathbf { x _ { \lambda } } = \mathbf { \nabla } \mathsf { R } \backslash \mathrm { d } ; \mathrm { ~  ~ { ~ \mathbf ~ { ~ r ~ } ~ } = ~ b ~ } ; } \\ & { \mathbf { f } \circ \mathbf { r } \mathrm { ~  ~ { ~ \mathbf ~ { ~ k ~ } ~ } = ~ \mathbf { ~ n } : - 1 : 1 ~ } } \\ & { \mathbf { r _ { \lambda } } = \textbf { r _ { \lambda } } - \mathbf { \nabla } \left( \mathsf { Q } \left( : , \mathbf { k } \right) : \ast \mathbf { r } \right) \ast \mathsf { Q } \left( : , \mathbf { k } \right) ; } \end{array}$ end

The equivalence between MGS and Householder QR factorization can also be used to obtain a backward stable algorithm for computing the minimum norm solution of an underdetermined linear system,

$$
\operatorname* { m i n } \| y \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A ^ { T } y = c ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ $\operatorname { r a n k } ( A ) = n$ ; see Bjorck [134,1994l. Consider now using Householder QR factorization to solve the equivalent least-norm problem

$$
\operatorname* { m i n } \left\| { \left( \begin{array} { l } { w } \\ { y } \end{array} \right) } \right\| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } \left( { \mathrm { ~ 0 ~ } } \quad A ^ { T } \right) { \left( \begin{array} { l } { w } \\ { y } \end{array} \right) } = c .
$$

If we solve $R ^ { T } z = c$ for $z = ( \zeta _ { 1 } , \ldots , \zeta _ { n } ) ^ { T }$ , then $y$ is obtained from

$$
{ \binom { w } { y } } = H _ { 1 } \cdot \cdot \cdot H _ { n } { \binom { z } { 0 } } .
$$

From the special form of the matrices $H _ { k }$ , this leads to the following algorithm: Set $y ^ { ( n ) } = 0$ and

$$
y ^ { ( k - 1 ) } = y ^ { ( k ) } - ( \omega _ { k } - \zeta _ { k } ) q _ { k } , \quad \omega _ { k } = q _ { k } ^ { T } y ^ { ( k ) } , \quad k = n , \ldots , 1 .
$$

Then the least-norm solution is $y = y ^ { ( 0 ) }$ . The quantities $\omega _ { k }$ compensate for the lack of orthogonality of $Q _ { 1 }$ . If $Q _ { 1 }$ is exactly orthogonal, they are zero.

# Algorithm 2.2.11 (Least-Norm Solution by MGS).

function y = mgsmnr(A,c); $\%$ Computes the least-norm solution y $\%$ of the linear system $\mathbb { A } ^ { \prime } \ast \mathbb { y } \ = \ \mathbb { c }$ %-- $\mathrm { [ m , n ] ~ = ~ \ s i z e ( A ) : }$ $\left[ { \mathbb Q } , { \mathbb R } \right] \ = \ \mathfrak { m } \mathfrak { g } \mathfrak { s } \left( \mathbb A \right)$ $\mathrm { ~ z ~ } = \ \mathrm { R } ^ { \prime } \setminus \mathrm { c }$ ； y = zeros(n,1); for $\texttt { k } = \texttt { n : - 1 : 1 }$ omega = Q(:,k)'\*y; y = y + (z(k）- omega)\*Q(:,k); end   
end

Algorithms 2.2.10 and 2.2.11 are columnwise backward stable in the same sense as the corresponding Householder QR factorizations; see Theorem 2.2.6 and Theorem 2.2.7, respectively.

The backward stable algorithm (2.2.47)-(2.2.48) using Householder QR factorization for solving the augmented system

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { y } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { b } } \\ { { c } } \end{array} \right) ,
$$

where $A \in \mathbb { R } ^ { m \times n }$ ，with $\operatorname { r a n k } ( A ) = n$ was given in Section 2.2.3. The interpretation of MGS as a Householder method shows the strong backward stability property of the following MGS algorithm for solving augmented systems; see Bjorck and Paige [150,1994l.

# Algorithm 2.2.12 (Augmented System Solution by MGS).

Compute MGS factorization $A = Q _ { 1 } R \in \mathbb { R } ^ { m \times n }$ , where $Q _ { 1 } = ( q _ { 1 } , \dots , q _ { n } )$

1. Solve $R ^ { T } z = c$ for $z = ( \zeta _ { 1 } , \ldots , \zeta _ { n } ) .$

2. Set $b ^ { ( 1 ) } = b$ and compute $d = ( \delta _ { 1 } , \ldots , \delta _ { n } )$ as

$$
\delta _ { k } = q _ { k } ^ { T } b ^ { ( k ) } , \quad b ^ { ( k + 1 ) } = b ^ { ( k ) } - \delta _ { k } q _ { k } \quad k = 1 : n .
$$

3. Set $y ^ { ( n ) } = b ^ { ( n + 1 ) }$ and compute $y = y ^ { ( 0 ) }$ by

$$
\omega _ { k } = q _ { k } ^ { T } y ^ { ( k ) } , \quad y ^ { ( k - 1 ) } = y ^ { ( k ) } - ( \omega _ { k } - \zeta _ { k } ) q _ { k } , \quad k = n : ( - 1 ) : 1 .
$$

4. Solve $\ R x = d - z$ for $x$

Algorithm 2.2.12 requires $8 m n + 2 n ^ { 2 }$ flops and generalizes the previous two algorithms. It is easily verified that if $c = 0$ ,it reduces to Algorithm 2.2.10,and if $b = 0$ ，it reduces to Algorithm 2.2.11. The stability of the MGS algorithm for solving augmented systems is analyzed by Bjorck and Paige [150,1994].

# 2.2.7 - Reorthogonalization

As shown in Section 2.2.4,the loss of orthogonality in the computed $Q _ { 1 } \ = \ ( q _ { 1 } , . . . , q _ { n } )$ as measured by $\lVert I - Q _ { 1 } ^ { T } Q _ { 1 } \rVert _ { 2 }$ is proportional to $\kappa ( A )$ for MGS and to $\kappa ( A ) ^ { 2 }$ for a variant of CGS.

In many applications it is essential that the computed vectors be orthogonal to working accuracy. In the orthogonal basis problem $A$ is given, and we want to find $Q _ { 1 }$ and $R$ such that

$$
\| I - Q _ { 1 } ^ { T } Q _ { 1 } \| \leq c _ { 1 } ( m , n ) \mathbf { u } , \qquad \| A - Q _ { 1 } R \| \leq c _ { 2 } ( m , n ) \mathbf { u } ,
$$

for modest constants $c _ { 1 } ( m , n )$ and $c _ { 2 } ( m , n )$ . One important application of reorthogonalization is subspace projection methods for solving eigenvalue problems.

To study the loss of orthogonalization in an elementary orthogonalization step, let $A =$ $( a _ { 1 } , a _ { 2 } ) \ \in \ \mathbb { R } ^ { m \times n }$ be_two given linearly independent unit vectors. Let $q _ { 1 } ~ = ~ a _ { 1 }$ and $q _ { 2 } ^ { \prime } \ =$ $a _ { 2 } \mathrm { ~ - ~ } r _ { 1 2 } q _ { 1 }$ ， $r _ { 1 2 } = q _ { 1 } ^ { T } a _ { 2 }$ , be the exact results. The corresponding quantities in floating-point arithmetic are

$$
\begin{array} { r } { \overline { { r } } _ { 1 2 } = f l ( q _ { 1 } ^ { T } a _ { 2 } ) , \qquad \overline { { q } } _ { 2 } ^ { \prime } = f l ( a _ { 2 } - f l ( \overline { { r } } _ { 1 2 } q _ { 1 } ) ) . } \end{array}
$$

The errors can be bounded by (see Section 1.4.2)

$$
\lvert \overline { { r } } _ { 1 2 } - r _ { 1 2 } \rvert < m \mathbf { u } , \qquad \lvert \lvert \overline { { q } } _ { 2 } ^ { \prime } - q _ { 2 } ^ { \prime } \rvert \rvert _ { 2 } < ( m + 2 ) \mathbf { u } \lvert \overline { { r } } _ { 1 2 } \rvert < ( m + 2 ) \mathbf { u } .
$$

It follows that $| q _ { 1 } ^ { T } \bar { q } _ { 2 } ^ { \prime } | = | q _ { 1 } ^ { T } ( \overline { { { q } } } _ { 2 } ^ { \prime } - q _ { 2 } ^ { \prime } ) | < ( m + 2 ) \mathbf { u }$ giving

$$
| q _ { 1 } ^ { T } \overline { { { q } } } _ { 2 } ^ { \prime } | / \| \overline { { { q } } } _ { 2 } ^ { \prime } \| _ { 2 } < \gamma _ { m + 2 } / \overline { { { r } } } _ { 2 2 } , \quad \bar { r } _ { 2 2 } = \| \overline { { { q } } } _ { 2 } ^ { \prime } \| _ { 2 } .
$$

(The errors in the normalization are negligible.） This shows that loss of orthogonality results when cancellation occurs in the computation of $\overline { { q } } _ { 2 } ^ { \prime }$ . This is the case when $r _ { 2 2 } = \sin ( \phi )$ is small, where $\phi$ is the angle between $a _ { 1 }$ and $a _ { 2 }$ . Then the orthogonalization can be repeated:

$$
\delta \overline { { { r } } } _ { 1 2 } = f l ( q _ { 1 } ^ { T } \overline { { { q } } } _ { 2 } ^ { \prime } ) , \qquad \overline { { { q } } } _ { 2 } ^ { \prime } : = f l ( \overline { { { q } } } _ { 2 } ^ { \prime } - f l ( \overline { { { r } } } _ { 1 2 } q _ { 1 } ) ) .
$$

Often such a reorthogonalization is carried out whenever

$$
\overline { { r } } _ { 2 2 } = \| \overline { { q } } _ { 2 } ^ { \prime } \| _ { 2 } \leq \alpha \| a _ { 2 } \| _ { 2 }
$$

for some parameter $\alpha$ , typically chosen in the range $0 . 1 \leq \alpha \leq 1 / \sqrt { 2 }$ . If cancellation occurs again, the reorthogonalization is repeated. In unpublished notes, Kahan showed that provided $A$ has full numerical rank,“twice is enough,” i.e., two reorthogonalizations always suffce. This result is made more precise by Parlett [884,1998], who showed that

$$
\begin{array} { r } { \| \hat { q } _ { 2 } ^ { \prime } - q _ { 2 } ^ { \prime } \| _ { 2 } \leq ( 1 + \alpha ) \mathbf { u } \| a _ { 2 } \| _ { 2 } , \qquad | q _ { 1 } ^ { T } \hat { q } _ { 2 } ^ { \prime } | \leq \mathbf { u } \alpha ^ { - 1 } \| \hat { q } _ { 2 } ^ { \prime } \| _ { 2 } . } \end{array}
$$

Hence for $\alpha = 0 . 5$ the computed vector $\hat { q } _ { 2 } ^ { \prime }$ is orthogonal to machine precision. For smaller values of $\alpha$ , reorthogonalization wil occur less frequently,and then the bound (2.2.79) on orthogonality is less satisfactory.

For $A = ( a _ { 1 } , \ldots , a _ { n } ) $ ， $n \ > \ 2$ ， selective reorthogonalization is used in a similar way. In step $k$ ， $k = 2 , \ldots , n$ ，CGS or MGS is applied to make $a _ { k }$ orthogonal to an orthonormal $Q _ { 1 } = \left( q _ { 1 } , \dotsc , q _ { k - 1 } \right)$ ， giving a computed vector $\bar { q } _ { k } ^ { \prime }$ .The vector $\bar { q } _ { k } ^ { \prime }$ is accepted provided $\bar { r } _ { k k } = \| \bar { q } _ { k } ^ { \prime } \| _ { 2 } > \alpha \| a _ { k } \| _ { 2 }$ . Otherwise, $\bar { q } _ { k } ^ { \prime }$ is reorthogonalized against $Q _ { 1 }$ .Rutishauser [951,1970] performs reorthogonalization when at least one decimal digit of accuracy has been lost due to cancellation. This corresponds to selective reorthogonalization with $\alpha = 0 . 1$ .Hoffmann [637, $\mathrm { 1 9 8 9 } ]$ reports extensive numerical tests with iterated reorthogonalization for CGS and MGS for a range of values of $\alpha = 1 / 2 , 0 . 1 , . . . , 1 0 ^ { - 1 0 }$ . The tests show that $\alpha = 0 . 5$ makes $Q _ { 1 }$ orthogonal to full working precision after one reorthogonalization.Moreover, with $\alpha = 0 . 5$ ,CGS performs as well as MGS.

Daniel et al. [285,1976] recommend using $\alpha = 1 / \sqrt { 2 }$ .Under certain technical assumptions, they show that provided $A$ has full numerical rank, iterated reorthogonalization converges to a sufficient level of orthogonality. If failure occurs in step $k$ , one option is to not generate a new vector $q _ { k }$ in this step,set $r _ { k k } = 0$ ，and proceed to the next column. This will generate a QR factorization where,after a suitable permutation of columns, $Q$ is $m \times ( n - p )$ and $R$ is $( n - p ) \times n$ upper trapezoidal with nonzero diagonal entries. This factorization can be used to compute the pseudoinverse solution to a least squares problem.

If full orthogonality is desired, the simplest option is to always perform one reorthogonalization, ie,tecolumectors $a _ { k } ^ { ( 0 ) } = a _ { k }$ ， $k \geq 2$ in $A$ are orthogonalized twice against the computed basis vectors $Q _ { k - 1 } = ( q _ { 1 } , \dots , q _ { k - 1 } )$ ：

$$
\begin{array} { r } { \boldsymbol a _ { k } ^ { ( i ) } = ( I - Q _ { k - 1 } Q _ { k - 1 } ^ { T } ) \boldsymbol a _ { k } ^ { ( i - 1 ) } = \boldsymbol a _ { k } ^ { ( i - 1 ) } - Q _ { k - 1 } ( Q _ { k - 1 } ^ { T } \boldsymbol a _ { k } ^ { ( i - 1 ) } ) , \quad i = 1 , 2 . } \end{array}
$$

The newbasisveor isthenivenas $q _ { k } = a _ { k } ^ { ( 2 ) } / \lVert a _ { k } ^ { ( 2 ) } \rVert _ { 2 }$

# Algorithm 2.2.13 (CGS2).

function $\left[ { \tt Q } , { \tt R } \right] = \tt { c g s 2 } \left( { \tt A } \right)$ ； $\%$ CGS2 computes the compact $\mathbb { Q R }$ factorization of A $\%$ using CGS with one step of reorthogonalization. %--- $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ size(A); ${ \sf \sf \sf \sf \sf \sf \sf } \left( \sf \sf \sf \Psi \right) \sf = \sf \sf \sf \sf \sf \sf \sf A $ ； $\mathrm { ~ \textsf ~ { ~ R ~ } ~ } =$ zeros(n) ; ${ \tt R } \left( 1 , 1 \right) \ = \ { \tt n o r m } \left( { \tt G } \left( : , 1 \right) \right) ;$ $\mathfrak { q } \left( : , 1 \right) \ = \ \mathfrak { q } \left( : , 1 \right) / \mathtt { R } \left( 1 , 1 \right) ;$ for $\mathtt { k } \ = \ 2 : \mathtt { n }$ for $\mathrm { ~ i ~ } = \mathrm { ~ 1 : 2 ~ }$ $\begin{array} { l } { { \mathrm {  ~ { \cal ~ V } ~ } = \mathrm {  ~ { \cal ~ Q } ~ } ( : , 1 : \mathrm { k } - 1 ) \mathrm {  ~ { \sf ~ * } ~ } \mathrm {  ~ { \sf ~ Q } ~ } ( : , \mathrm { k } ) \mathrm {  ~ { \sf ~ ; } ~ } } } \\ { { \mathrm {  ~ { \cal ~ Q } ~ } ( : , \mathrm { k } ) = \mathrm {  ~ { \cal ~ Q } ~ } ( : , \mathrm { k } ) - \mathrm {  ~ { \cal ~ Q } ~ } ( : , 1 : \mathrm { k } - 1 ) \mathrm {  ~ { \sf ~ * } ~ } \mathrm {  ~ { \cal ~ V } ~ } ; } } \\ { { \mathrm {  ~ { \cal ~ R } ~ } ( 1 : \mathrm { k } - 1 , \mathrm { k } ) = \mathrm {  ~ { \cal ~ R } ~ } ( 1 : \mathrm { k } - 1 , \mathrm { k } ) + \mathrm {  ~ { \cal ~ V } ~ } ; } } \end{array}$ end $\begin{array} { r l } { { \tt R } ( \tt k , \tt k ) } & { = { \tt \tt { n o r m } } \left( \tt { 0 } \left( : \tau , \tt k \right) \right) ; } \\ { { \tt Q } ( : \theta , \tt k ) } & { = { \tt { Q } } ( : \theta , \tt k ) / { \tt R } \left( \tt k , \tt k \right) ; } \end{array}$ end   
end

The corrections to the elements in $R$ are in general small and may be omitted. However, Gander [437,198o] has shown that including them will give a slightly lower error in the com-puted residual $A - Q R$ . A scheme MGS2 similar to CGS2 can be employed for the columnwise MGS algorithm. This has the same operation count as CGS2,and both produce basis vectors with orthogonality close to unit roundoff level. For MGS2 the inner loop is a vector operation, whereas in CGS2 it is a matrix-vector operation. Hence MGS2 executes slower than CGS2, which therefore usually is the preferred choice.

Giraud and Langou [479, 2oo2] analyze a different version of MGS2. Let the initial factorization $A = Q _ { 1 } R$ be computed by rowwise MGS. MGS is then applied a second time to the computed $Q _ { 1 }$ to give $Q _ { 1 } = \widetilde { Q } _ { 1 } \widetilde { R }$ . Combining this and the first factorizations yields the corrected factorization

$$
A = \widetilde Q _ { 1 } \widehat R , \quad \widehat R = \widetilde R R .
$$

This algorithm can be proved to work under weaker assumptions than those for CGS2. From the analysis of MGS by Bjorck [125,1967l and Bjorck and Paige [149,1992], Giraud and Langou get the following result.

Lemma 2.2.13. Assume that $A \in \mathbb { R } ^ { m \times n }$ $n \leq m$ ， satisfies $c \mathbf { u } \kappa ( A ) \leq 0 . 1$ ，where

$$
c = 1 8 . 5 3 n ^ { 3 / 2 } , \qquad 2 . 1 2 ( m + 1 ) \mathbf { u } \leq 0 . 0 1 .
$$

Then for the factorization $A = Q _ { 1 } R$ computed by MGS, it holds that $\kappa ( Q _ { 1 } ) \leq 1 . 3$

From this lemma it can be deduced that $Q _ { 1 }$ satisfies

$$
\lVert I - \widetilde { Q } _ { 1 } ^ { T } \widetilde { Q } _ { 1 } \rVert _ { 2 } \leq 1 . 7 1 c \kappa ( \widetilde { Q } _ { 1 } ) \mathbf { u } < 4 0 . 5 2 \mathbf { u } n ^ { 3 / 2 } .
$$

Hence $\widetilde { Q } _ { 1 }$ is orthonormal to machine precision.

# Notes and references

Roundoff error analyses for CGS with reorthogonalization are given by Abdelmalek [4,1971] and Kielbasinski [692,1974]. Giraud, Graton,and Langou [478, 2oo4] propose an a posteriori reorthogonalization technique for MGS based on a rank- $k$ update of the computed vectors.The level of orthogonality of the set of vectors gets better when $k$ increases and eventually reaches machine-precision level.

Ruhe [940,1983] considers iterated reorthogonalization of $a _ { k }$ against vectors $\begin{array} { r l } { Q _ { 1 } } & { { } = } \end{array}$ $( q _ { 1 } , \dots , q _ { k - 1 } )$ that are not accurately orthogonal. He shows that this gives $q _ { k } = a _ { k } - Q _ { 1 } r _ { k }$ ， where $r _ { k }$ satisfes the least squares problem

$$
Q _ { 1 } ^ { T } Q _ { 1 } r _ { k } = Q _ { 1 } ^ { T } a _ { k } .
$$

Iterated CGS corresponds to the Jacobi,and iterated MGS corresponds to the Gauss-Seidel iterative method for solving this system; see Section 6.1.4.

# 2.3 - Rank-Deficient Least Squares Problems

# 2.3.1 - Semidefinite Cholesky Factorization

If the columns of $A \in \mathbb { R } ^ { m \times n }$ are linearly dependent, $\operatorname { r a n k } ( A ) = r < n$ ，and the matrix of normal equations $C = A ^ { T } A$ is positive semidefinite. In this case the Cholesky factor $R$ must have $n - r$ zero diagonal elements. By using symmetric pivoting in the factorization, these zero elements can be made to appear last.

Theorem 2.3.1. Let $C = A ^ { T } A \in \mathbb { R } ^ { n \times n }$ be a symmetric positive semidefinite matrix of rank $r < n$ .Then there is a permutation $P$ such that $P ^ { T } C P$ has a unique Cholesky factorization of the form

$$
\begin{array} { r } { P ^ { T } A ^ { T } A P = R ^ { T } R , \quad R = \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) , } \end{array}
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ is upper triangular with positive diagonal elements.

Proof. The proof is constructive. The algorithm takes $C ^ { ( 1 ) } = A ^ { T } A$ and computes a sequence of matrices

$$
C ^ { ( k ) } = ( c _ { i j } ^ { ( k ) } ) = \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { S ^ { ( k ) } } } \end{array} \right) , \quad k = 1 , 2 , \ldots .
$$

At the start of step $k$ we select the maximum diagonal element of $C ^ { ( k ) }$ ，

$$
s _ { p } = \operatorname* { m a x } _ { k \leq i \leq n } c _ { i i } ^ { ( k ) } ,
$$

and interchange rows and columns $p$ and $k$ to bring this into pivot position.This pivot must be positive for $k < r$ ,because otherwise $S ^ { ( k ) } = 0$ ，which implies that $\operatorname { r a n k } ( C ) < r$ .Next, the elements in the permuted $C ^ { ( k ) }$ are transformed according to

$$
\begin{array} { r l } & { r _ { k k } = \sqrt { c _ { k k } ^ { ( k ) } } , \qquad r _ { k j } = c _ { k j } ^ { ( k ) } / r _ { k k } , \quad j = k + 1 : n , } \\ & { c _ { i j } ^ { ( k + 1 ) } = c _ { i j } ^ { ( k ) } - r _ { k i } r _ { k j } ^ { T } , \quad i , j = k + 1 : n . } \end{array}
$$

This is equivalent to subtracting a symmetric rank-one matrix $r _ { j } r _ { j } ^ { T }$ from $C ^ { ( k ) }$ , where $r _ { j } = e _ { j } ^ { T } R$ is the $j$ th row of $R$ .The algorithm stops when $k = r + 1$ .Then all diagonal elements are zero, which implies that $C ^ { ( r + 1 ) } = 0$ □

Since all reduced matrices $C ^ { ( k ) }$ are symmetric positive semidefinite, their maximum elements lie on the diagonal. Hence,the pivot selection in the outer product Cholesky algorithm described above is equivalent to complete pivoting. The algorithm produces a matrix $R$ whose diagonal elements in $R$ form a nonincreasing sequence $r _ { 1 1 } \geq r _ { 2 2 } \geq \cdot \cdot \cdot \geq r _ { n n }$ Indeed, the stronger inequalities

$$
r _ { k k } ^ { 2 } \geq \sum _ { i = k } ^ { j } r _ { i j } ^ { 2 } , \quad j = k + 1 , \ldots , n , \quad k = 1 : r ,
$$

are true; see Section 2.3.3.

Rounding errors can cause negative elements to appear on the diagonal in the Cholesky algorithm even when $C$ is positive semidefinite. Similarly, the computed reduced matrix will in general be nonzero after $r$ steps even when ${ \mathrm { r a n k } } ( C ) = r$ . This raises the question of when to terminate the Cholesky factorization of a semidefinite matrix. One possibility is to stop when

$$
\operatorname* { m a x } _ { k \leq i \leq n } c _ { i i } ^ { ( k ) } \leq 0
$$

and set $\operatorname { r a n k } ( C ) = k - 1$ . But this may cause unnecessary work in eliminating negligible elements. Taking computational cost into consideration, we recommend the stopping criterion

$$
\operatorname* { m a x } _ { k \leq i \leq n } a _ { i i } ^ { ( k ) } \leq c _ { n } \mathbf { u } r _ { 1 1 } ^ { 2 } ,
$$

where $c _ { n }$ is a modest constant; see also Higham [623, 2oo2, Sect.10.3.2]. Perturbation theory and error analysis for the Cholesky decomposition of semidefinite matrices are developed by Higham [617,1990].

In the rank-deficient case, the permuted normal equations become

$$
\begin{array} { r } { R ^ { T } R \widetilde { x } = \widetilde { d } , \quad x = P \widetilde { x } , \quad \widetilde { d } = P ^ { T } ( A ^ { T } b ) . } \end{array}
$$

With $z = R \widetilde { x }$ ,we obtain

$$
\begin{array} { r } { R ^ { T } z = \left( \begin{array} { l } { R _ { 1 1 } ^ { T } } \\ { R _ { 1 2 } ^ { T } } \end{array} \right) z = \left( \begin{array} { l } { \widetilde { d } _ { 1 } } \\ { \widetilde { d } _ { 2 } } \end{array} \right) , } \end{array}
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ is nonsingular. The triangular system $R _ { 1 1 } ^ { T } z = \widetilde { d } _ { 1 }$ determines $z \in \mathbb { R } ^ { r }$ . From

$$
R _ { 1 1 } \widetilde { x } _ { 1 } = z - R _ { 1 2 } \widetilde { x } _ { 2 } ,
$$

where $\begin{array} { r l } { \widetilde { x } = \left( \widetilde { x } _ { 1 } ^ { T } } & { { } \widetilde { x } _ { 2 } ^ { T } \right) ^ { T } } \end{array}$ ， we can determine $\widetilde { x } _ { 1 }$ for an arbitrarily chosen $\widetilde { x } _ { 2 }$ . This expresses the fact that a consistent singular system has an infinite number of solutions. Finally, the permutations are undone to obtain $x = P \widetilde { x }$

Setting $\widetilde { x } _ { 2 } = 0$ we get a basic solution $x _ { b }$ with only $r = { \mathrm { r a n k } } ( A )$ nonzero components in $x$ ,corresponding to the first $r$ columns in $A P$ . This is relevant when a good least squares fit of $b$ using as few variables as possible is desired. The pseudoinverse solution $x ^ { \dagger }$ that minimizes $\| x \| _ { 2 } = \| \widetilde { x } \| _ { 2 }$ is obtained from the full-rank least squares problem

$$
\operatorname* { m i n } _ { x _ { 2 } } \left\| \left( { \begin{array} { c } { S } \\ { - I _ { n - r } } \end{array} } \right) x _ { 2 } - \left( { \begin{array} { c } { x _ { b } } \\ { 0 } \end{array} } \right) \right\| _ { 2 } , \quad S = R _ { 1 1 } ^ { - 1 } R _ { 1 2 } .
$$

The basic solution $x _ { b }$ can be computed in about $r ^ { 2 } ( n - r )$ flops. Note that $S$ can overwrite $R _ { 1 2 }$ Then $x _ { 2 }$ can be computed from the normal equations,

$$
( S ^ { T } S + I _ { n - r } ) x _ { 2 } = S ^ { T } x _ { b } ,
$$

using a Cholesky factorization of $( S ^ { T } S + I _ { n - r } )$ . When $x _ { 2 }$ has been determined, we have $x _ { 1 } =$ $x _ { b } - S x _ { 2 }$ . This method requires about $r ( n - r ) ^ { 2 } + { \textstyle { \frac { 1 } { 3 } } } ( n - r ) ^ { 3 }$ flops and has been further studied by Deuflhard and Sautter [319,198o].

# 2.3.2- Rank-Deficient QR Factorization

We now show that there is a column permutation $P$ such that in the QR factorization of $A P$ the zero diagonal elements appear last.

Theorem 2.3.2. Given $A \in R ^ { m \times n }$ with $\operatorname { \dot { \operatorname { a n k } } } ( A ) = r < n ,$ there is a permutation matrix $P$ and an orthogonal matrix $Q \in \mathbb { R } ^ { m \times n }$ ，such that

$$
A P = Q \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { 0 } } \end{array} \right) \} r \qquad 
$$

where $R _ { 1 1 } \in R ^ { r \times r }$ is upper triangular with positive diagonal elements.

Proof. Since $\operatorname { r a n k } ( A ) = r$ ， we can always choose a permutation matrix $P$ such that $A P =$ $\left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right)$ , where $A _ { 1 } \in R ^ { m \times r }$ has linearly independent columns. The QR factorization

$$
\begin{array} { r } { Q ^ { T } A _ { 1 } = \left( \begin{array} { c } { R _ { 1 1 } } \\ { 0 } \end{array} \right) , \quad Q = \left( \begin{array} { c c } { Q _ { 1 } } & { Q _ { 2 } } \end{array} \right) } \end{array}
$$

uniquely determines $Q _ { 1 } \in \mathbb { R } ^ { m \times r }$ and $R _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ with positive diagonal elements. Then

$$
Q ^ { T } A P = ( Q ^ { T } A _ { 1 } \quad Q ^ { T } A _ { 2 } ) = \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right)
$$

has rank $r$ .Here $R _ { 2 2 } = 0$ , because $R$ cannot have more than $r$ linearly independent rows. Hence the factorization must have the form (2.3.5). □

From (2.3.5) and orthogonal invariance it folows that the least squares problem $\operatorname* { m i n } _ { x } \| A x -$ $b \Vert _ { 2 }$ is equivalent to

$$
\operatorname* { m i n } _ { x } \left\| \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c } { \widetilde { x } _ { 1 } } \\ { \widetilde { x } _ { 2 } } \end{array} \right) - \left( \begin{array} { c } { d _ { 1 } } \\ { d _ { 2 } } \end{array} \right) \right\| _ { 2 } ,
$$

where $d = Q ^ { T } b$ and ${ \widetilde { x } } = P x$ are partitioned conformally. The general solution of (2.3.6) is given by $x = P \left( { \widetilde { x } } _ { 1 } \right)$ , where

$$
R _ { 1 1 } \widetilde { x } _ { 1 } = d _ { 1 } - R _ { 1 2 } z ,
$$

and $z = \widetilde { x } _ { 2 }$ can be chosen arbitrarily. For $z = 0$ ,we obtain a basic least squares solution

$$
x = P \left( { \begin{array} { c } { \widetilde { x } _ { b } } \\ { 0 } \end{array} } \right) , \quad \widetilde { x } _ { b } = R _ { 1 1 } ^ { - 1 } d _ { 1 } ,
$$

with at most $r = { \mathrm { r a n k } } ( A )$ nonzero components. The general solution is given by

$$
x = P \left( \begin{array} { c } { { \widetilde { x } _ { b } - S z } } \\ { { z } } \end{array} \right) , \quad S = R _ { 1 1 } ^ { - 1 } R _ { 1 2 } .
$$

Here $S$ can be computed in about $r ^ { 2 } ( n - r )$ flops by solving the matrix equation $R _ { 1 1 } S = R _ { 1 2 }$ using back-substitution.

A general approach to resolve rank-deficiency is to seek the solution to the least squares problem

$$
\operatorname* { m i n } _ { x \in S } \| B x \| _ { 2 } , \quad S = \{ x \mid \operatorname* { m i n } _ { x } \| A x - b \| _ { 2 } \} .
$$

Here $B$ can be chosen so that $\| B x \| _ { 2 }$ is a measure of the smoothness of $x$ . Substituting the general solution (2.3.7), we find that (2.3.10) is equivalent to

$$
\operatorname* { m i n } _ { z } \left\| B \left( \begin{array} { c } { S } \\ { - I _ { n - r } } \end{array} \right) z - B \left( \begin{array} { c } { \widetilde { x } _ { b } } \\ { 0 } \end{array} \right) \right\| _ { 2 } .
$$

This is a least squares problem of dimension $\boldsymbol { r } \times ( \boldsymbol { n } - \boldsymbol { r } )$ that can be solved by QR factorization in about $2 r ( n - r ) ^ { 2 }$ flops. In particular, taking $B = I$ minimizes

$$
\| x \| _ { 2 } ^ { 2 } = \| S z \| _ { 2 } ^ { 2 } + \| z \| _ { 2 } ^ { 2 }
$$

and gives the pseudoinverse solution. It is easily verified that

$$
\begin{array} { r } { \mathcal { N } ( A P ) = \mathcal { R } \left( \begin{array} { c } { S } \\ { - I _ { n - r } } \end{array} \right) } \end{array}
$$

is a (nonorthonormal) basis for $\mathcal { N } ( A P )$ . QR factorization gives an orthonormal basis for $\mathcal { N } ( A P )$ Note that the unique pseudoinverse solution orthogonal to $\mathcal { N } ( A P )$ equals the residual of the least squares problem (2.3.11) with $B = I$ ，

$$
\widetilde { x } ^ { \dagger } = \binom { \widetilde { x } _ { b } } { 0 } - \binom { S } { - I _ { n - r } } z .
$$

Notice that it has the form of the basic solution minus a correction in the nullspace of $A P$ . Any particular solution can be substituted for $z$ in (2.3.11).

# 2.3.3 - Pivoted QR Factorization

For many applications it is preferable to use a column pivoted QR factorization (QRP)

$$
A P = Q R , \quad A \in \mathbb { R } ^ { m \times n } ,
$$

in which the pivot column at step $k$ is chosen to maximize the diagonal element $r _ { k k }$ . We first show how to implement this strategy for MGS.Assume that after $\left( k - 1 \right)$ steps the nonpivotal columns have been transformed according to

$$
a _ { j } ^ { ( k ) } = a _ { j } - \sum _ { i = 1 } ^ { k - 1 } r _ { i j } q _ { i } , \quad j = k , \ldots , n ,
$$

where aj is orthogonal to ${ \mathcal { R } } ( A _ { k - 1 } ) = \operatorname { s p a n } \left\{ q _ { 1 } , \dots , q _ { k - 1 } \right\}$ . Hence in the $k$ th step we should determine $p$ ,so that

$$
\| a _ { p } ^ { ( k ) } \| _ { 2 } ^ { 2 } = \operatorname* { m a x } _ { k \leq j \leq n } \| a _ { j } ^ { ( k ) } \| _ { 2 } ^ { 2 } ,
$$

and interchange columns $k$ and $p$ .This is equivalent to choosing at the $k$ th step a pivot column with largest distance to the subspace $\mathcal { R } ( A _ { k - 1 } ) = \operatorname { s p a n } \left( a _ { c _ { 1 } } , \dots , a _ { c _ { k - 1 } } \right)$ ，where $A _ { k - 1 }$ is the submatrix formed by the columns corresponding to the first $k - 1$ selected pivots. We note that for this pivot strategy to be relevant it is essential that the columns of $A$ be well scaled.

Golub [487,1965l gave an implementation of the same pivoting strategy for Householder QR. Assume that after $k$ steps of pivoted QR factorization the reduced matrix is

$$
\left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { A ^ { ( k ) } } } \end{array} \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ is square upper triangular and $A ^ { ( k ) } = ( a _ { 1 } ^ { ( k ) } , \dots , a _ { n } ^ { ( k ) } )$ .Let $p$ be the smallest index such that

$$
s _ { p } ^ { ( k ) } \geq s _ { j } ^ { ( k ) } , \quad s _ { j } ^ { ( k ) } = \| a _ { j } ^ { ( k ) } \| _ { 2 } ^ { 2 } , \quad j = k + 1 , \ldots , n ,
$$

where a are the columns of the submatrix $A ^ { ( k ) }$ . Then before the next step, columns $k + 1$ and $p$ in $A ^ { ( k ) }$ are interchanged. The pivot column maximizes

$$
s _ { j } ^ { ( k ) } = \operatorname* { m i n } _ { y } \| A ^ { ( k ) } y - a _ { j } ^ { ( k ) } \| _ { 2 } ^ { 2 } , \quad j = k , \ldots , n .
$$

The quantities $s _ { j } ^ { ( k ) }$ is necessary to avoid numerical cancellation.

With the column pivoting strategy described above,the diagonal elements in $R$ will form a nonincreasing sequence $r _ { 1 1 } \ge r _ { 2 2 } \ge \dots \ge r _ { r r }$ .It is not difficult to show that, in fact, the diagonal elements in $R$ satisfy the stronger inequalities

$$
r _ { k k } ^ { 2 } \geq \sum _ { i = k } ^ { j } r _ { i j } ^ { 2 } , \quad j = k + 1 , \ldots , n , \quad k = 1 : r .
$$

This implies that if $r _ { k k } = 0$ , then $r _ { i j } = 0 , i , j \ge k$ . In particular,

$$
| r _ { 1 1 } | = \operatorname * { m a x } _ { 1 \leq j \leq n } \{ | e _ { 1 } ^ { T } R e _ { 1 } | \ | \ A P _ { 1 , j } = Q R \} ,
$$

where $P _ { 1 , j }$ is he perutationatrix tatiterhangesouand $j$ Then $\| A \| _ { F } ^ { 2 } \le n r _ { 1 1 } ^ { 2 }$ which yields upper and lower bounds for $\sigma _ { 1 } ( A )$ ，

$$
| r _ { 1 1 } | \leq \sigma _ { 1 } ( A ) \leq { \sqrt { n } } | r _ { 1 1 } | .
$$

If the column norms $\| a _ { j } ^ { ( k ) } \| _ { 2 }$ are recomputed at each stage of MGS,this will increase the operation count of the QR factorization by $50 \%$ . Since these quantities are invariant under orthogonal transformations, this overhead can be reduced to $O ( m n )$ operations by using the recursion

$$
\| a _ { j } ^ { ( k + 1 ) } \| _ { 2 } ^ { 2 } = \| a _ { j } ^ { ( k ) } \| _ { 2 } ^ { 2 } - r _ { k j } ^ { 2 } , \quad j = k + 1 , \ldots , n ,
$$

to update these values.To avoid numerical problems $s _ { j } ^ { ( k + 1 ) }$ should be recomputedfrom scratch wheneveteba $\| a _ { j } ^ { ( k + 1 ) } \| _ { 2 } \leq \| a _ { j } ^ { ( k ) } \| _ { 2 } / \sqrt { 2 }$

If a diagonal element $r _ { k k }$ in QRP vanishes, it follows from (2.3.18) that $r _ { i j } = 0 , i , j \ge k$ Assume that at an intermediate stage of QRP the new diagonal element satisfies $r _ { k + 1 , k + 1 } \leq \delta$ for some small $\delta$ .Then by (2.3.18),

$$
\| A ^ { ( k ) } \| _ { F } \le ( n - k ) ^ { 1 / 2 } \delta ,
$$

and setting $A ^ { ( k ) } = 0$ corresponds to a perturbation $E _ { k }$ of $A$ ，such that $A + E _ { k }$ has rank- $k$ and $\| E _ { k } \| _ { F } \le ( n - k ) ^ { 1 / 2 } \delta$ .The matrix

$$
\hat { A } = Q _ { 1 } \left( R _ { 1 1 } \quad R _ { 1 2 } \right) P ^ { T } , \quad Q = \left( Q _ { 1 } \quad Q _ { 2 } \right) ,
$$

obtained by neglecting $R _ { 2 2 }$ , is the best rank- $k$ approximation to $A$ that differs from $A P$ only in the last $n - k$ columns. In particular, with $k = n - 1$ we obtain $\| A - { \hat { A } } \| _ { F } = r _ { n n }$

Example 2.3.3. The following example by Kahan [680,1966] shows that QR factorization with standard pivoting can fail to reveal near singularity of a matrix.The matrix

$$
A _ { n } = \mathrm { d i a g } ( 1 , s , \ldots , s ^ { n - 1 } ) \left( \begin{array} { c c c c c } { 1 } & { - c } & { - c } & { \ldots } & { - c } \\ & { 1 } & { - c } & { \ldots } & { - c } \\ & & { 1 } & { \ddots } & { \vdots } \\ & & & { \ddots } & { - c } \\ & & & & { 1 } \end{array} \right) , \quad 0 \leq c \leq 1 ,
$$

where $s ^ { 2 } + c ^ { 2 } = 1$ , is already in upper triangular form. Because the inequalities (2.3.18) hold, $A _ { n }$ is invariant under QR factorization with column pivoting.4 For $n = 1 0 0$ and $c = 0 . 2$ the two smallest singular values are $\sigma _ { n } = 3 . 6 7 8 1 \cdot 1 0 ^ { - 9 }$ and $\sigma _ { n - 1 } = 0 . 1 4 8 2$ . However, the two smallest diagonal elements of $R _ { n }$ are $r _ { n - 1 , n - 1 } = s ^ { n - 2 } = 0 . 1 2 9 9$ and $r _ { n n } = s ^ { n - 1 } = 0 . 1 3 2 6$ ,and the near singularity of $A _ { n }$ is not revealed.

The column pivoting strategy described is independent of the right-hand side $b$ and may not be the most appropriate for solving a given least squares problem. For example, suppose $b$ is a multiple of a column in $A$ . With standard pivoting this may not be detected until the full QR factorization has been computed. An alternative strategy is to select the pivot column in step $k + 1$ as the column for which the current residual norm $\| b - A x ^ { ( k ) } \| _ { 2 }$ is maximally reduced. For MGS this is achieved by choosing as pivot the column $a _ { p }$ that makes the smallest acute angle with $r ^ { ( k ) }$ . Hence, with $\gamma _ { j } ^ { ( k ) } = ( a _ { j } ^ { ( k ) } ) ^ { T } r ^ { ( k ) }$ a()Tr(k),thecolumn ischosen tomaximize

$$
( \gamma _ { j } ^ { ( k ) } ) ^ { 2 } / \| a _ { j } ^ { ( k ) } \| _ { 2 } ^ { 2 } .
$$

This quantity is important in statistical applications, such as stepwise variable regression.

The criterion $r _ { k + 1 , k + 1 } \ \leq \ \delta$ is commonly used for terminating the pivoted QR algorithm. However, it can greatly overestimate the numerical rank of $A$ .Faddeev,Kublanovskaya,and Faddeeva [391,1968] proved the inequality

$$
\sigma _ { n } \geq \frac { 3 | r _ { n n } | } { \sqrt { 4 ^ { n } + 6 n - 1 } } \geq 2 ^ { 1 - n } | r _ { n n } | .
$$

This shows $\sigma _ { n }$ can be much smaller than $\left| \boldsymbol { r } _ { n n } \right|$ for moderately large values of $n$ .Example 2.3.3 shows that the bound in (2.3.24) can almost be attained.

Stewart [1023,1984] shows that better bounds for $\sigma _ { n }$ can be found from QR factorization using so-called reverse column pivoting. This determines the permutation $P _ { 1 , j }$ so that

$$
| r _ { n n } | = \operatorname* { m i n } _ { 1 \leq j \leq n } \{ | e _ { n } ^ { T } R e _ { n } | \ | \ A P _ { 1 , j } = Q R \} .
$$

Then it holds that

$$
( 1 / { \sqrt { n } } ) | r _ { n n } | \leq \sigma _ { n } ( A ) \leq | r _ { n n } | .
$$

Setting $r _ { n n } = 0$ makes $R$ singular. Hence the upper bound (2.3.25) follows from (1.3.21). As shown by Chandrasekaran and Ipsen [231,1994l), reverse pivoting on $R$ is equivalent to using standard pivoting on $R ^ { - T }$

# 2.3.4 - Complete Orthogonal Decompositions

The QR factorization of a rank-deficient matrix $A \in \mathbb { R } ^ { m \times n }$ is

$$
A P = ( Q _ { 1 } \quad Q _ { 2 } ) \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

where $R _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ ， $r \ < \ n$ , is nonsingular. Here $Q _ { 1 }$ and $Q _ { 2 }$ give orthogonal bases for $\mathcal { R } ( A )$ and $\mathcal { N } ( A ^ { T } )$ . This factorization is less useful for applications that need a basis for ${ \mathcal { N } } ( A )$ .The elements in $R _ { 1 2 }$ can be annihilated by postmultiplying $R$ by a sequence of Householder reflectors

$$
\left( R _ { 1 1 } \quad R _ { 1 2 } \right) { \cal H } _ { k } \cdot \cdot \cdot { \cal H } _ { 1 } = \left( \widetilde { R } \quad 0 \right) , \quad { \cal H } _ { j } = I - \gamma _ { j } ^ { - 1 } u _ { j } u _ { j } ^ { T } ,
$$

$j = r , r - 1 , \ldots , 1$ ，where $u _ { j }$ has nonzero elements only in positions $j , r + 1 , \ldots , n$ . This is equivalent to a QL factorization of the transpose of the triangular factor $R$ ，

$$
\left( \begin{array} { c c } { { R _ { 1 1 } ^ { T } } } & { { 0 } } \\ { { R _ { 1 2 } ^ { T } } } & { { 0 } } \end{array} \right) = \hat { \cal Q } \left( \begin{array} { c c } { { \widetilde R ^ { T } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) ,
$$

and requires $2 r ^ { 2 } ( n - r )$ flops. The first two steps in the reduction are shown below for $n = 6$ ， $r = 4$

$$
H _ { 4 } \left[ \begin{array} { l l l l l } { \times } & & & \\ { \times } & { \times } & & \\ { \times } & { \times } & { \times } & \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } \end{array} \right] \quad \Rightarrow \quad H _ { 3 } \left[ \begin{array} { l l l l } { \times } & & & \\ { \times } & { \times } & & \\ { \times } & { \times } & { \times } & \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \otimes } \end{array} \right] \quad \Rightarrow \quad H _ { 2 } \left[ \begin{array} { l l l l } { \times } & & & \\ { \times } & { \times } & & \\ { \times } & { \times } & { \times } & \\ { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \otimes } & { \otimes } \end{array} \right] , \quad \cdot \cdot . . , .
$$

# This gives a complete orthogonal decomposition of the form

$$
A P = Q \left( \begin{array} { c c } { { \widetilde { R } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) V ^ { T } , \quad V = H _ { 1 } \cdot \cdot \cdot H _ { k } .
$$

This decomposition, first described by Hanson and Lawson [589,1969], gives an explicit orthogonal basis for the range and nullspace of $A$ ,and a representation for the pseudoinverse.It can be updated efficiently when $A$ is subject to a change of low rank; see Section 3.3.

Theorem 2.3.4. Assume that we have a complete orthogonal decomposition (2.3.27) of $A$ Then if $V = \left( \begin{array} { l l } { { V _ { 1 } } } & { { V _ { 2 } } } \end{array} \right)$ ， $P V _ { 2 }$ is an orthogonal basis for the nullspace of dimension $( n - r )$ of $A$ Furthermore,the pseudoinverse of $A$ is

$$
\begin{array} { r } { A ^ { \dagger } = P V \left( \begin{array} { c c } { R ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } \end{array} \right) Q ^ { T } , } \end{array}
$$

and $x ^ { \dagger } = P V _ { 1 } R ^ { - 1 } Q _ { 1 } ^ { T } b$ is the pseudoinverse solution of the problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$

Proof. It is immediately verified that $A P V _ { 2 } = 0$ ，and a dimensional argument shows that $P V _ { 2 }$ spans the nullspace of $A$ . The expression for the pseudoinverse follows by verifying the Penrose conditions. □

For matrices $A \in \mathbb { R } ^ { m \times n }$ that are only close to being rank-deficient with $r \ < \ n$ ，Stewart [1025,1992] introduced the URV decomposition. This has the form

$$
\begin{array} { r } { A P = U \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { R _ { 2 2 } } \end{array} \right) V ^ { T } , \quad R _ { 1 1 } \in \mathbb { R } ^ { r \times r } , } \end{array}
$$

with $U = \left( U _ { 1 } \quad U _ { 2 } \right)$ and $V = \left( \begin{array} { l l } { V _ { 1 } } & { V _ { 2 } } \end{array} \right)$ orthogonal. If the singular values of $A$ are

$$
\sigma _ { 1 } \geq \sigma _ { 2 } \geq \cdot \cdot \cdot \geq \sigma _ { r } \gg \sigma _ { r + 1 } \geq \cdot \cdot \cdot \geq \sigma _ { n } ,
$$

then the decomposition (2.3.29) is said to be rank-revealing if

$$
\sigma _ { k } ( R _ { 1 1 } ) \geq \sigma _ { r } / c , \qquad \left( \| R _ { 1 2 } \| _ { F } ^ { 2 } + \| R _ { 2 2 } \| _ { F } ^ { 2 } \right) ^ { 1 / 2 } \leq c \sigma _ { r + 1 } ,
$$

and $c$ is bounded by a low-degree polynomial in $r$ and $n$ .For $\Pi = I$ ,it follows from (2.3.29) that

$$
\| A V _ { 2 } \| _ { 2 } = \left\| \left( { \binom { R _ { 1 2 } } { R _ { 2 2 } } } \right) \right\| _ { F } \leq c \sigma _ { r + 1 } .
$$

Hence $V _ { 2 }$ is an orthogonal basis for the approximate nullspace of $A$ . The URV decomposition is useful in applications, such as subspace tracking in signal processing, where it is desirable to compute an approximate nullspace and also update the basis as rows are added or deleted from $A$

The rank-revealing process of Chan starts from a pivoted QR factorization and determines a vector $w$ such that $\| R w \| _ { 2 }$ is small. Then a sequence of plane rotations is determined such that

$$
Q ^ { T } w _ { n } = G _ { n - 1 , n } ^ { T } \cdot \cdot \cdot G _ { 1 2 } ^ { T } w _ { n } = \| w _ { n } \| _ { 2 } e _ { n } .
$$

Next, an orthogonal matrix $P$ such that $P ^ { T } R Q \ = \ P ^ { T } G _ { 1 2 } \ldots , G _ { n - 1 , n }$ is upper triangular is determined. When $G _ { j - 1 , j }$ is applied, a nonzero element is introduced just below the diagonal of $R$ . To restore the triangular from, a left rotation can be used:

$$
{ \begin{array} { c c c c } { { \downarrow } } & { { \downarrow } } & { { \downarrow } } & { { \downarrow } } \\ { { \left( { \begin{array} { l l l l } { r } } & { r } & { r } & { r } \\ { + } & { r } & { r } & { r } \\ { 0 } & { 0 } & { r } & { r } \\ { 0 } & { 0 } & { 0 } & { r } \end{array} \right)}  } & { \Rightarrow } & { { \left( \begin{array} { l l l l } { r } & { r } & { r } & { r } \\ { \oplus } & { r } & { r } & { r } \\ { 0 } & { 0 } & { r } & { r } \\ { 0 } & { 0 } & { 0 } & { r } \end{array} \right) } } & { \Rightarrow } & { { \left( \begin{array} { l l l l } { r } & { r } & { r } & { r } \\ { 0 } & { r } & { r } & { r } \\ { 0 } & { + } & { r } & { r } \\ { 0 } & { 0 } & { 0 } & { r } \end{array} \right) } } \end{array} }
$$

$$
\begin{array} { r l } & { \to \left( \begin{array} { l l l l } { r } & { r } & { r } & { r } \\ { 0 } & { r } & { r } & { r } \\ { 0 } & { \oplus } & { r } & { r } \\ { 0 } & { 0 } & { 0 } & { r } \end{array} \right) \Rightarrow \quad \left( \begin{array} { l l l l } { r } & { r } & { r } & { r } \\ { 0 } & { r } & { r } & { r } \\ { 0 } & { 0 } & { r } & { r } \\ { 0 } & { 0 } & { + } & { r } \end{array} \right) \Rightarrow \quad \to \left( \begin{array} { l l l l } { r } & { r } & { r } & { e } \\ { 0 } & { r } & { r } & { e } \\ { 0 } & { 0 } & { r } & { e } \\ { 0 } & { 0 } & { \oplus } & { e } \end{array} \right) . } \end{array}
$$

This process requires $O ( n ^ { 2 } )$ multiplications. We now have

$$
\begin{array} { r } { P ^ { T } R w _ { n } = ( P ^ { T } R Q ) ( Q ^ { T } w _ { n } ) = \| w _ { n } \| _ { 2 } { \widetilde { R } } e _ { n } . } \end{array}
$$

As $P$ is orthogonal it follows that if $\| R w _ { n } \| _ { 2 } < | r _ { n n } |$ ,then $\| \widetilde { R } e _ { n } \| _ { 2 } < \delta / \| w _ { n } \| _ { 2 }$ . This bounds the norm for the last column of the transformed matrix $\widetilde { R }$ If $| r _ { n - 1 , n - 1 } |$ is small, this defation can be continued on the principal submatrix of order $n - 1$ of $\widetilde { R }$

Stewart [1026,1993l has suggested a refinement process for the URV decomposition (2.3.29), which reduces the size of the block $R _ { 1 2 }$ and increases the accuracy in the nullspace approximation. It can be viewed as one step of the zero-shift QR algorithm (7.1.19),and can be iterated, and will converge quickly if there is a large relative gap between the singular values $\sigma _ { k }$ and $\sigma _ { k + 1 }$ Alternatively one can work with the corresponding decomposition of lower triangular form, the rank-revealing ULV decomposition

$$
A = U \left( \begin{array} { c c } { { L _ { 1 1 } } } & { { 0 } } \\ { { L _ { 2 1 } } } & { { L _ { 2 2 } } } \end{array} \right) V ^ { T } .
$$

For this decomposition with the partitioning $V = ( V _ { 1 } \quad V _ { 2 } ) , \| A V _ { 2 } \| _ { 2 } = \| L _ { 2 2 } \| _ { F }$ . Hence the size of $\| L _ { 2 1 } \| _ { F }$ does not adversely affect the nulspace approximation.

Suppose we have a rank-revealing factorization

$$
A P = Q \left( \begin{array} { c c } { { L _ { 1 1 } } } & { { 0 } } \\ { { L _ { 2 1 } } } & { { L _ { 2 2 } } } \end{array} \right) ,
$$

where $L _ { 1 1 }$ and $L _ { 2 2 }$ are lower triangular and $\sigma _ { k } ( L _ { 1 1 } ) \geq \sigma _ { k } / c$ and $\| L _ { 2 2 } \| _ { 2 } \le c \sigma _ { k + 1 }$ for some constant $c$ .(Such a factorization can be obtained from a rank-revealing QR factorization by reversing the rows and columns of the $R$ -factor.） Then a rank-revealing ULV decomposition can be obtained by a similar procedure as shown above for the URV decomposition. Suppose we have a vector $w$ such that $\Vert \boldsymbol { w } ^ { T } L \Vert _ { 2 }$ is small. Then,as before, $w$ is first reduced to the unit vector $e _ { n }$ ：

$$
Q ^ { T } w _ { n } = G _ { n - 1 , n } ^ { T } \cdot \cdot \cdot G _ { 1 2 } ^ { T } w _ { n } = \| w _ { n } \| _ { 2 } e _ { n } .
$$

The sequence of plane rotations are then applied to $L$ from the left, and extra rotations from the right are used to preserve the lower triangular form.

# Notes and references

The use of URV and QR factorizations for solving rank-deficient least squares problems is treated by Foster [428,2oo3]. Foster and Kommu [426, 2oo6] use a truncated pivoted QR factorization, where the rank of the trailing diagonal block is estimated by a condition estimator. For problems of low rank it is an order of magnitude faster than the LAPACK routine xGELSY, which is based on a complete orthogonal decomposition. Symmetric rank-revealing decompositions are studied by Hansen and Yalamov [586, 2001].

# 2.3.5 - Rank-Revealing QR Factorizations

As seen from examples in the previous section, QR factorization with standard column pivoting may fail to reveal the rank-deficiency of nearly singular matrices.The following definition makes precise what would be desirable in this case.

Definition 2.3.5. Let $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ , be a given matrix, and let $\Pi _ { k }$ be a permutation. Then the QR factorization

$$
A \Pi _ { k } = Q R = Q \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right) \} k _ { \qquad - k } ~ , ~ 1 \leq k < n ,
$$

is said to be a rank-revealing QR (RRQR) factorization if

$$
\sigma _ { k } ( R _ { 1 1 } ) \geq \sigma _ { k } ( A ) / c , \qquad \sigma _ { 1 } ( R _ { 2 2 } ) \leq c \sigma _ { k + 1 } ( A ) ,
$$

where $c = c ( k , n ) > 0$ is bounded by a low-degree polynomial in $k$ and $n$

From the interlacing property of the singular values (Theorem 1.3.5) it follows that

$$
\sigma _ { k } ( A ) \geq \sigma _ { k } ( R _ { 1 1 } ) , \qquad \sigma _ { k + 1 } ( A ) \leq \sigma _ { 1 } ( R _ { 2 2 } ) .
$$

The permutation $\Pi$ should be chosen so that the smallest singular value of the $k$ first columns of $A _ { 1 }$ is maximized and the largest singular value of $A _ { 2 }$ is minimized. Note that an exhaustive search is not feasible because this has combinatorial complexity. It can be shown that an RRQR factorization always exists.

Theorem 2.3.6. Let $A \in \mathbb { R } ^ { m \times n }$ $( m \geq n )$ , and let $k$ be a given integer $0 < k < n$ Then there is a permutation matrix $\Pi _ { k }$ that gives an RRQR factorization (2.3.32) with

$$
c = \sqrt { k ( n - k ) + 1 } .
$$

Proof. See Hong and Pan 638,1992,Theorem 2.2].

As pointed out by Stewart [1024,1992] the sense in which the RRQR algorithms are rankrevealing is different from that of the SVD. Given $A \in \mathbb { R } ^ { m \times n }$ and a value $k < n$ they produce a permutation $\Pi$ that reveals if there is a gap between $\sigma _ { k }$ and $\sigma _ { k + 1 }$ . For a different value of $k$ the permutation may change.

Golub,Klema,and Stewart [496,1976] (see also Golub and Van Loan [512,1996, Sect. 12.2]) note that the selection of $\Pi$ in an RRQR factorization is related to the column subset selection problem of determining a subset $A _ { 1 }$ of $k \ < \ n$ columns in $A \in \mathbb { R } ^ { m \times n }$ such that $\lVert A - ( A _ { 1 } \bar { A } _ { 1 } ^ { \dagger } ) A \rVert _ { 2 }$ is minimized over all possible choices. This is closely related to the selection of a subset of rows of the matrix of right singular vectors of $A$ corresponding to small singular values,as explained in the following theorem.

Theorem 2.3.7. Let $A = U \Sigma V ^ { T }$ be the SVD of $A$ and set $V = \left( \begin{array} { l l } { V _ { 1 } } & { V _ { 2 } } \end{array} \right)$ and $\Pi = \left( \Pi _ { 1 } \quad \Pi _ { 2 } \right)$ ， where $V _ { 1 } , \Pi _ { 1 } \ \in \mathbb { R } ^ { n \times k }$ . Hence, $V _ { 2 }$ is the matrix of right singular vectors corresponding to the $n - k$ smallest singular values. Let

$$
\begin{array} { r } { A \Pi = Q R \in \mathbb { R } ^ { m \times n } , \quad R = \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { R _ { 2 2 } } \end{array} \right) , } \end{array}
$$

$R _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ ， $1 \leq k < n$ , be the QR factorization of $A \Pi$ Then

$$
\sigma _ { \operatorname* { m i n } } ( R _ { 1 1 } ) \geq c \sigma _ { k } ( A ) , \qquad \sigma _ { \operatorname* { m a x } } ( R _ { 2 2 } ) \leq \frac { 1 } { c } \sigma _ { k + 1 } ( A ) ,
$$

where $c = \sigma _ { \operatorname* { m i n } } ( \Pi _ { 1 } ^ { T } V _ { 1 } ) = \sigma _ { \operatorname* { m i n } } ( \Pi _ { 2 } ^ { T } V _ { 2 } ) .$

Proof. See Hong and Pan [638,1992, Theorem 1.5]. The equality (2.3.37) follows by applying the CS decomposition (see Section 1.2.4) to the orthogonal matrix

$$
\Pi ^ { T } V = \left( \begin{array} { c c } { { \Pi _ { 1 } ^ { T } V _ { 1 } } } & { { \Pi _ { 1 } ^ { T } V _ { 2 } } } \\ { { \Pi _ { 2 } ^ { T } V _ { 1 } } } & { { \Pi _ { 2 } ^ { T } V _ { 2 } } } \end{array} \right) .
$$

Here the matrix $V _ { 2 }$ of right singular vectors can be replaced by any orthonormal basis for the column space of $V _ { 2 }$ □

This theorem says that $A \Pi = Q R$ is an RRQR factorization if the permutation matrix $\Pi$ is such that $\sigma _ { \mathrm { m i n } } ( \Pi _ { 2 } ^ { T } V _ { 2 } )$ is maximum. At the same time, $\sigma _ { \mathrm { m i n } } ( \Pi _ { 1 } ^ { T } V _ { 1 } )$ will attain its maximum.

It remains to obtain a sufficiently sharp lower bound for $c$ When $k = n - 1$ ,this is easily done. Let $v _ { n }$ be the right singular vector corresponding to $\sigma _ { n }$ . Since $\| v _ { n } \| _ { 2 } = 1$ , it follows that $\| v _ { n } \| _ { \infty } \geq 1 / { \sqrt { n } }$ . Hence, taking $\Pi$ to be the permutation matrix that permutes the maximum element in $v _ { n }$ to the last position guarantees that (2.3.37) holds with $c = { \sqrt { n } }$

Algorithms for computing an RRQR factorization based on computing the SVD of $A$ are usually not practical. If the SVD is known, this is already sufficient for most purposes.

Example 2.3.8. Let $R _ { n }$ ， $n = 1 0 0$ , be the Kahan matrix in Example 2.3.3. The largest element in the right singular vector $v _ { n }$ corresponding to $\sigma _ { n }$ is $v _ { 1 , n } = 0 . 5 5 3$ ， whereas the element $v _ { n , n } =$ $1 . 6 0 \cdot 1 0 ^ { - 8 }$ is very small. Therefore, we perform a cyclical shift of the columns in $R _ { n }$ that puts the first column last, i.e., in the order $2 , 3 , \ldots , n , 1$ ，

$$
H _ { n } = R _ { n } \Pi = \mathrm { d i a g } ( 1 , s , \ldots , s ^ { n - 1 } ) \left( \begin{array} { c c c c c } { - c } & { - c } & { \ldots } & { - c } & { 1 } \\ { 1 } & { - c } & { \ldots } & { - c } & { 0 } \\ & { 1 } & { \ddots } & { \vdots } & { \vdots } \\ & & { \ddots } & { - c } & { 0 } \\ & & & { 1 } & { 0 } \end{array} \right) .
$$

The matrix $H _ { n }$ has Hessenberg form and can be retriangularized in less than $2 n ^ { 2 }$ flops using updating techniques.Hence the total cost of this factorization is only slightly larger than that for the standard QR factorization. In the new $R$ -factor $\bar { R }$ the last diagonal element $\begin{array} { l l } { \bar { r } _ { n , n } } & { = } \end{array}$ $6 . 6 5 4 \cdot 1 0 ^ { - 9 }$ is of the same order of magnitude as the smallest singular value $3 . 6 7 8 \cdot 1 0 ^ { - 9 }$ Furthermore, $\bar { r } _ { n - 1 , n - 1 } = 0 . 1 6 2 3 6$ Hence $\bar { R }$ is rank-revealing.

To obtain a sharp lower bound for $c$ in (2.3.36) when $k > 1$ is more difficult. Recall that the volume of a matrix $\boldsymbol { X } \in \mathbb { R } ^ { m \times k }$ ， $m \geq k$ , is definedas the productof its singular values:

$$
\operatorname { v o l } \left( X \right) = | \operatorname* { d e t } ( X ) | = \sigma _ { 1 } ( X ) \cdots \sigma _ { k } ( X ) .
$$

Hong and Pan [638,1992] show that selecting a permutation $\Pi ~ = ~ \left( \Pi _ { 1 } ~ \Pi _ { 2 } \right)$ such that vol $( \Pi _ { 2 } ^ { T } V _ { 2 } )$ is maximum among all possible $( n - k )$ by $( n - k )$ submatrices in $V _ { 2 }$ is sufficient to give an RRQR factorization.

Lemma 2.3.9. Let the unit vector $v$ ， $\| v \| _ { 2 } = 1$ be such that $\| A v \| _ { 2 } = \epsilon .$ Let II be a permutation such that if $w = \Pi ^ { T } v$ ，then $| z _ { n } | ~ = ~ \| w \| _ { \infty }$ . Then, in the QR factorization of AII we have $| r _ { n n } | \leq n ^ { 1 / 2 } \epsilon .$

Proof. Since $| z _ { n } | = \| w \| _ { \infty }$ and $\| v \| _ { 2 } = \| w \| _ { 2 } = 1$ , it follows that $| z _ { n } | \geq n ^ { - 1 / 2 }$ . Furthermore,

$$
Q ^ { T } A v = Q ^ { T } A \Pi ( \Pi ^ { T } v ) = R w ,
$$

where the last component of $R w$ is $r _ { n n } z _ { n }$ . Therefore, $\epsilon = | | A v | | _ { 2 } = | | Q ^ { T } A w | | _ { 2 } = | | R w | | _ { 2 } \geq$ $\left| r _ { n n } z _ { n } \right|$ , from which the result follows. □

Chan [224,1987l gives a more efficient approach for the special case $k = n - 1$ ,based on inverse iteration. Let $A \Pi _ { G } = Q R$ be an initial QR factorization using standard pivoting. Then

$$
( A ^ { T } A ) ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T } ,
$$

for which the dominating eigenvalue is $\sigma _ { 1 } ^ { - 2 }$ . Each step then requires $2 n ^ { 2 }$ flops for the solution of the two triangular systems

$$
R ^ { T } y ^ { ( k ) } = w ^ { ( k - 1 ) } , \qquad R w ^ { ( k ) } = y ^ { ( k ) } .
$$

By a few steps of inverse iteration, an approximation to $\sigma _ { n }$ and the corresponding singular vector $v _ { n }$ are obtained. From this a permutation matrix $\Pi$ is determined as in Lemma 2.3.9.An RRQR factorization of $R \Pi = { \bar { Q } } { \bar { R } }$ can then be computed using updating techniques as in Example 2.3.8.

The above one-dimensional technique can be extended to the case when the approximate nullspace is larger than one by applying it repeatedly to smaller and smaller leading blocks of $R$ as described in Algorithm 2.3.1.

# Algorithm 2.3.1 (Chan's RRQR).

Rrctom $A \Pi = Q \left( { R \atop 0 } \right)$

For $k = n , n - 1 , \ldots d o$

1. Partition

$$
R = \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right) \Sigma \Sigma _ { k - k }
$$

and determine $\delta _ { k } = \sigma _ { \operatorname* { m i n } } ( R _ { 1 1 } )$ and the corresponding right singular vector $w _ { k }$

2. If $\delta _ { k } > \tau$ (a user tolerance), then set $\operatorname { \cdot a n k } ( A ) = k$ and finish.

3. Determine a permutation matrix $P$ such that $\begin{array} { r } { | ( P ^ { T } w _ { k } ) _ { k } | = \| P ^ { T } w _ { k } \| _ { \infty } . } \end{array}$

4. Compute the QR factorization $R _ { 1 1 } P = \widetilde Q \widetilde R _ { 1 1 }$ and update

$$
\Pi : = \Pi \left( \begin{array} { c c } { { P } } & { { 0 } } \\ { { 0 } } & { { I _ { n - k } } } \end{array} \right) , \quad Q : = Q \left( \begin{array} { c c } { { \widetilde Q } } & { { 0 } } \\ { { 0 } } & { { I _ { n - k } } } \end{array} \right) , \quad R : = \left( \begin{array} { c c } { { \widetilde R _ { 1 1 } } } & { { \widetilde Q ^ { T } R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right) .
$$

5. Assign $\left( \begin{array} { c } { { w _ { k } } } \\ { { 0 } } \end{array} \right)$ to the kth column of $W$ and update

$$
W = \left( \begin{array} { c } { { W _ { 1 } } } \\ { { W _ { 2 } } } \end{array} \right) : = \left( \begin{array} { c c } { { P ^ { T } } } & { { 0 } } \\ { { 0 } } & { { I _ { n - k } } } \end{array} \right) W ,
$$

where $W _ { 2 }$ is upper triangular and nonsingular.

A similar algorithm was proposed independently by Foster [424,1986]. The main difference between the two algorithms is that Foster's algorithm only produces a factorization for a subset of the columns of the original matrix.

By the interlacing property of singular values (Theorem 1.2.9) it follows that the $\delta _ { i }$ are nonincreasing and that the singular values $\sigma _ { i }$ of $A$ satisfy $\delta _ { i } \leq \sigma _ { i }$ ， $k + 1 \leq i \leq n$ . Chan [224,1987] proves the following upper and lower bounds.

Theorem 2.3.10. Let $R _ { 2 2 } ^ { ( i ) }$ and $W _ { 2 } ^ { ( i ) }$ denoteteoebo $( n - i +$ $1 ) \times ( n - i + 1 )$ of $R _ { 2 2 }$ and $W _ { 2 }$ ，respectively. Let $\delta _ { i }$ denote the smallest singular value of the leading principal $i \times i$ submatrices of $R$ Then,for $i = k + 1 : n$ ，

$$
\frac { \sigma _ { i } } { \sqrt { n - i + 1 } \| ( W _ { 2 } ^ { ( i ) } ) ^ { - 1 } \| _ { 2 } } \le \delta _ { i } \le \sigma _ { i } \le \| R _ { 2 2 } ^ { ( i ) } \| _ { 2 } \le \sigma _ { i } \sqrt { n - i + 1 } \| ( W _ { 2 } ^ { ( i ) } ) ^ { - 1 } \| _ { 2 } .
$$

Hence, $\| R _ { 2 2 } ^ { ( i ) } \| _ { 2 }$ are easilycomputable upper bounds for $\sigma _ { i }$ .Further, theoutermost bounds in the theorem show that if $\lVert ( W _ { 2 } ^ { ( i ) } ) ^ { - 1 } \rVert _ { 2 }$ is not large, then $\delta _ { i }$ and $\| R _ { 2 2 } ^ { ( i ) } \| _ { 2 }$ are guaranteed to be tight bounds,and hence the factorization will have revealed the rank.The matrix $W$ determined

by the RRQR algorithm satisfies

$$
\| A \Pi W \| _ { 2 } ^ { 2 } \leq \| A \Pi W \| _ { F } ^ { 2 } = \sum _ { i = k + 1 } ^ { n } \delta _ { i } ^ { 2 } .
$$

Therefore, ${ \mathcal { R } } ( \Pi W )$ in the RRQR algorithm is a good approximation to the numerical nullspace $\mathcal { N } _ { k } ( A )$ . A more accurate and orthogonal basis for $\mathcal { N } _ { k } ( A )$ can be determined by simultaneous inverse iteration with $R ^ { T } R$ starting with $W$ .If $R$ has zero or nearly zero diagonal elements, a small multiple of the machine unit is substituted. The use of RRQR factorizations for computing truncated SVD solutions is discussed by Chan and Hansen [227,1990].

If the matrix $A$ has low rank rather than low rank-deficiency, it is more efcient to build up the rank-revealing QR factorization from estimates of singular vectors corresponding to the large singular values. Such algorithms are described by Chan and Hansen [229,1994]. Chandrasekaran and Ipsen [231, 1994] show that many previously suggested pivoting strategies form a hierarchy of greedy algorithms. They give an algorithm called Hybrid-II that is guaranteed to find an RRQR factorization that satisfies (2.3.33). Their algorithm works by alternately applying standard and Stewart's reverse column pivoting to the leading and trailing diagonal blocks of the initial QR factorization

$$
\begin{array} { r } { A = Q R = Q \left( \begin{array} { c c } { R _ { 1 1 } } & { R _ { 1 2 } } \\ { 0 } & { R _ { 2 2 } } \end{array} \right) , \quad R _ { 1 1 } \in \mathbb { R } ^ { k \times k } . } \end{array}
$$

It keeps interchanging the“most dependent” of the first $k$ columns with one of the last $n - k$ columns,and interchanging the“most independent’ of the last $n - k$ columns with one of the first $k$ columns, as long as $\operatorname* { d e t } ( R _ { 1 1 } )$ strictly increases. This stops after a finite number of steps. In the worst case the work is exponential in $n$ ,but in practice usually only a few refactorizations are needed.

Pan and Tang [875,1999l give an RRQR algorithm that uses a similar type of cyclic pivotig. Given $A \in \mathbb { R } ^ { m \times n }$ $m \geq n$ ,let $\Pi _ { i , j }$ be the permutation matrix such that $A \Pi _ { i , j }$ interchanges columns $i$ and $j$ of $A$ .They define the pivoted magnitude $\eta ( A )$ of $A$ to be the maximum magnitude of $r _ { 1 1 }$ in the QR factorizations of $A \Pi _ { 1 , j }$ ， $1 \leq j \leq n$ ,i.e.,

$$
\eta ( A ) = \operatorname* { m a x } _ { 1 \leq j \leq n } \{ | r _ { 1 1 } | \ | \ A \Pi _ { 1 , j } = Q R \} .
$$

Clearly, it holds that

$$
\eta ( A ) = \operatorname* { m a x } _ { 1 \leq j \leq n } \| A e _ { j } \| _ { 2 } .
$$

Similarly, they define the reverse pivoted magnitude $\tau ( A )$ to be the minimum magnitude of $\left| \boldsymbol { r } _ { n n } \right|$ in the QR factorizations of $A \Pi _ { j , n }$ ， $1 \leq j \leq n$ If $A$ is nonsingular, then as shown by Stewart [1023,1984],

$$
\tau ( A ) = 1 / \operatorname* { m a x } _ { 1 \leq j \leq n } \| e _ { j } ^ { T } A ^ { - 1 } \| _ { 2 } .
$$

In the following, two related submatrices of $R$ in the partitioned QR factorization (2.3.39) are important: $\overline { { R } } _ { 1 1 }$ ,the $( k + 1 ) \times ( k + 1 )$ leading principal submatrix, and $\overline { { R } } _ { 2 2 }$ ,the $( n - k +$ $1 ) \times ( n - k + 1 )$ trailing principal submatrix. Pan and Tang consider the QR factorizations

$$
A \Pi _ { j , k } = Q ^ { ( j ) } R ^ { ( j ) } , \quad j = 1 , \ldots , k ,
$$

and show that f $| r _ { k k } ^ { ( j ) } | \ = \ \eta ( \overline { { { R } } } _ { 2 2 } ^ { ( j ) } )$ then he factoirainisa $k$ rank-revealin fatoiain i.e.,the inequalities (2.3.33) are satisfied.

The following algorithm is less expensive than Hybrid-IIby avoiding reverse pivoting.

# Algorithm 2.3.2 (Pan and Tang's RRQR Algorithm 1).

Compute the QR factorization $A \Pi$ with standard pivoting. Set $i = k - 1$ ，and while $i \neq 0$ ， do

1. Compute $R$ -factor $R \Pi _ { i , k }$

2. If $| r _ { k k } | \geq \eta ( \overline { { R } } _ { 2 2 } )$ ,then set $i = i - 1$ Otherwise, perform an exchange as folows. Find $\ell$ such that

$$
\eta ( \bar { R } _ { 2 2 } ) = \| ( r _ { k , \ell } , r _ { k + 1 , \ell } , \ldots , r _ { n , \ell } ) \| _ { 2 } .
$$

3. Compute $R$ -factor $R \Pi _ { k , \ell ; }$ and set $\Pi = \Pi \Pi _ { k , \ell }$ and $i = k - 1$

It can be shown that whenever an exchange takes place in step 2, the determinant of $R _ { 1 1 }$ will strictly increase in magnitude. Therefore an exchange can happen only a finite number of times. After the last exchange,at most $k - 1$ iterations can take place. Hence the algorithm must terminate.

For the RRQR factorization a basis for the numerical nullspace is given by $\mathcal { R } ( \mathcal { W } )$ , where

$$
W = \left( \begin{array} { c } { { - R _ { 1 1 } ^ { - 1 } R _ { 1 2 } } } \\ { { I _ { n - r } } } \end{array} \right) .
$$

If the norm of $R _ { 1 1 } ^ { - 1 } R _ { 1 2 }$ is large,this cannot be stably evaluated. Gu and Eisenstat [549,1996] call an RRQR factorization strong if,apart from (2.3.33) being satisfied,it holds that

$$
\left| ( R _ { 1 1 } ^ { - 1 } R _ { 1 2 } ) _ { i j } \right| \leq c _ { 2 } ( k , n )
$$

for $1 \leq i \leq k$ and $1 \leq j \leq n - k$ ，where $c _ { 2 }$ is bounded by a low-degree polynomial in $k$ and $n$ .This condition suffices to make $\mathcal { R } ( \mathcal { W } )$ an approximate nullspace of $A$ with a small residual independent of the condition number of $R _ { 1 1 }$ . They give a modification of the Hybrid-II algorithm that computes both $k$ and a strong RRQR factorization.

# $2 . 4 ~ \AA$ Methods Based on LU Factorization

# 2.4.1 - The Peters-Wilkinson Method

Standard algorithms for solving square nonsymmetric linear systems are usually based on an LU factorization of $A$ ,and many efcient implementations are available for both sparse and dense systems. Let minx $\| A x - b \| _ { 2 }$ ， $A \in \mathbb { R } ^ { m \times n }$ of $\operatorname { r a n k } ( A ) = n < m$ ,be an overdetermined least squares problem. The method of Peters and Wilkinson [892,197o] starts by computing an LU factorization with complete pivoting,

$$
\Pi _ { 1 } A \Pi _ { 2 } = { \binom { A _ { 1 } } { A _ { 2 } } } = L U = { \binom { L _ { 1 } } { L _ { 2 } } } U ,
$$

where $\boldsymbol { L } \in \mathbb { R } ^ { m \times n }$ is unit lower trapezoidal and $U \in \mathbb { R } ^ { n \times n }$ is upper triangular and nonsingular. $\Pi _ { 1 }$ and $\Pi _ { 2 }$ are permutation matrices reflecting the row and column interchanges. With this factorization the least squares problem becomes

$$
\operatorname* { m i n } _ { y } \| L y - \Pi _ { 1 } b \| _ { 2 } , \quad U \Pi _ { 2 } ^ { T } x = y .
$$

If complete pivoting is used, then all elements in $L$ are bounded by one in modulus.This ensures that $L$ is well-conditioned,and any ill-conditioningin $A$ will be reflected in $U$ . Hence, squaring

the condition number is avoided,and without substantial loss of accuracy, the first subproblem in (2.4.2) can be solved using the normal equations

$$
L ^ { T } L y = L ^ { T } \Pi _ { 1 } b .
$$

The solution $x$ is then obtained from $U \Pi _ { 2 } ^ { T } x = y$ by back-substitution. The Peters-Wilkinson method is particularly suitable for solving weighted least squares problems.

Computing the factorization (2.4.1） requires $m n ^ { 2 } - n ^ { 3 } / 3$ flops.Forming the symmetric matrix $L ^ { T } L$ requires $m n ^ { 2 } - n / 3$ flops,and computing its Cholesky factorization needs $n ^ { 3 } / 3$ flops. Neglecting terms of order $n ^ { 2 }$ ,the total arithmetic cost to compute the least squares solution by the Peters-Wilkinson method is $2 m n ^ { 2 } - n ^ { 3 } / 3$ flops. This is always more than that needed for the method of normal equations applied to the original system, which requires $m n ^ { 2 } + n ^ { 3 } / 3$ flops.Sautter [967,1978] gives a detailed analysis of stability and rounding errors of the LU factorization with complete pivoting.

Example 2.4.1. The following ill-conditioned matrix and its normal matrix is considered by Noble [832,1976]:

$$
A = \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { 1 + \epsilon } } \\ { { 1 } } & { { 1 - \epsilon } } \end{array} \right) , \qquad A ^ { T } A = 3 \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { 1 + 2 \epsilon ^ { 2 } / 3 } } \end{array} \right) .
$$

If $\epsilon \leq \sqrt { \mathbf { u } }$ ，then in floating-point computation, $f l ( 1 + 2 \epsilon ^ { 2 } / 3 ) = 1$ ，and the computed matrix $A ^ { T } A$ is numerically singular. However,in the LU factorization

$$
A = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } \end{array} \right) \left( \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 0 } } & { { \epsilon } } \end{array} \right) \equiv L U ,
$$

$L$ is orthonormal, and the pseudoinverse can be stably computed as

$$
\begin{array} { r l } & { A ^ { \dagger } = U ^ { - 1 } ( L ^ { T } L ) ^ { - 1 } L ^ { T } = \left( \begin{array} { c c } { 1 } & { - \epsilon ^ { - 1 } } \\ { 0 } & { \epsilon ^ { - 1 } } \end{array} \right) \left( \begin{array} { c c } { 1 / 3 } & { 0 } \\ { 0 } & { 1 / 2 } \end{array} \right) \left( \begin{array} { c c } { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { - 1 } \end{array} \right) } \\ & { \qquad = \frac { 1 } { 6 } \left( \begin{array} { c c } { 2 } & { 2 - 3 \epsilon ^ { - 1 } } & { 2 + 3 \epsilon ^ { - 1 } } \\ { 0 } & { 3 \epsilon ^ { - 1 } } & { - 3 \epsilon ^ { - 1 } } \end{array} \right) . } \end{array}
$$

A similar method can be developed for solving the underdetermined problem

$$
\operatorname* { m i n } \| y \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A ^ { T } y = c ,
$$

where $\operatorname { r a n k } ( A ^ { T } ) = n < m$ . From (2.4.1) we have $A ^ { T } y = \Pi _ { 2 } ( L U ) ^ { T } \Pi _ { 1 } y$ Hence, with $z = \Pi _ { 1 } y$ problem (2.4.4) can be written as

$$
\operatorname* { m i n } \| z \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } L ^ { T } z = d ,
$$

where $d$ is obtained from the lower triangular system $U ^ { T } d = \Pi _ { 2 } ^ { T } c$ Problem (2.4.5) is wellconditioned and can be solved using the normal equations of the second kind:

$$
L ^ { T } L z = d , \qquad y = \Pi _ { 1 } ^ { T } ( L z ) .
$$

LU factorization with complete pivoting is slow, and when $A$ has full column rank, it is usually sufficient to use partial pivoting. An atractive alternative is to use a method that, in terms of efficiency and accuracy, lies between partial and complete pivoting; see Foster [425, 1997].Rook pivoting was introduced by Neal and Poole [824,1992]. The name is chosen because the pivot search resembles the movement of the rook piece in chess.A pivot element is chosen that is the largest in both its row and column. One starts by finding the element of maximum magnitude in the first column. If this also is of maximum magnitude in its row, it is accepted as pivot. Otherwise, the element of maximum magnitude in this row is determined and compared with other elements in its column, etc.

The Peters-Wilkinson method works also for problems where $A$ is rank-deficient. Then, after deleting zero rows in $U$ and the corresponding columns in $L$ ,the LU factorization yields a unit lower trapezoidal factor $\boldsymbol { L } \in \mathbb { R } ^ { m \times r }$ and an upper triangular factor $U \in \mathbb { R } ^ { r \times n }$ of full rank. For example, if $m = 6$ ， $n = 4$ ,and $r = 3$ ,then (in exact computation) the factors obtained after $r$ elimination steps have the form

$$
L = \left( \begin{array} { c c c } { { 1 } } & { { } } & { { } } \\ { { l _ { 2 1 } } } & { { 1 } } & { { } } \\ { { l _ { 3 1 } } } & { { l _ { 3 2 } } } & { { 1 } } \\ { { l _ { 4 1 } } } & { { l _ { 4 2 } } } & { { l _ { 4 3 } } } \\ { { l _ { 5 1 } } } & { { l _ { 5 2 } } } & { { l _ { 5 3 } } } \\ { { l _ { 6 1 } } } & { { l _ { 6 2 } } } & { { l _ { 6 3 } } } \end{array} \right) , \qquad U = \left( \begin{array} { c c c } { { u _ { 1 1 } } } & { { u _ { 1 2 } } } & { { u _ { 1 3 } } } & { { u _ { 1 4 } } } \\ { { } } & { { u _ { 2 2 } } } & { { u _ { 2 3 } } } & { { u _ { 2 4 } } } \\ { { } } & { { } } & { { u _ { 3 3 } } } & { { u _ { 3 4 } } } \end{array} \right) ;
$$

see Section 2.4.3. A problem that remains is how to determine the rank $r$ reliably.

# 2.4.2 - Nearly Square Least Squares Problems

Many applications lead to linear systems $A x = b$ that are nearly square, i.e., the number of rows in $A$ is almost equal to the number of columns. One example is the simulation of multibody systems,such as robot arms or satellites; see Cardenal,Duff,and Jiménez [2O8,1998].For such problems substantial savings in operations and storage may be achieved by an algebraic reformulation of the Peters-Wilkinson method.

Let $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ ， $\operatorname { r a n k } ( A ) = n$ , be a nearly square least squares problem, $p = m - n$ ， $0 < p \ll n$ .LU factorization gives the subproblem $\operatorname* { m i n } _ { y } \| L y - b \| _ { 2 }$ With $z = L _ { 1 } y$ ， $u = z - b _ { 1 }$ ， the transformed subproblem becomes

$$
\operatorname* { m i n } _ { z } \left\| \left( \begin{array} { c } { { I _ { n } } } \\ { { C } } \end{array} \right) u - \left( \begin{array} { c } { { 0 } } \\ { { b _ { 2 } - C b _ { 1 } } } \end{array} \right) \right\| _ { 2 } ,
$$

where $C = L _ { 2 } L _ { 1 } ^ { - 1 } \in \mathbb { R } ^ { p \times n }$ . The normal equations are

$$
( I _ { n } + C ^ { T } C ) u = C ^ { T } ( b _ { 2 } - C b _ { 1 } ) .
$$

The useful identity

$$
( I _ { n } + C ^ { T } C ) ^ { - 1 } C ^ { T } = C ^ { T } ( I _ { p } + C C ^ { T } ) ^ { - 1 }
$$

can be proved by multiplying with $\left( I _ { n } + C ^ { T } C \right)$ from the left and using $( C ^ { T } C ) C = C ^ { T } ( C C ^ { T } )$ It follows that the solution to (2.4.7) can be written $u = C ^ { T } v$ ,where

$$
( I _ { p } + C C ^ { T } ) v = b _ { 2 } - C b _ { 1 } .
$$

This only requires the inversion of a matrix of size $p \times p$ . The resulting algorithm is summarized below.

1. Compute te factoriraion $\begin{array} { r } { \widetilde { A } = \Pi _ { 1 } A \Pi _ { 2 } = \left( { L _ { 1 } } \atop { L _ { 2 } } \right) U . } \end{array}$

2. Compute $C$ by solving $L _ { 1 } ^ { T } C = L _ { 2 } ^ { T }$ 3. Form and solve $( I _ { p } + C C ^ { T } ) v = b _ { 2 } - C b _ { 1 } .$

4. Form and solve $L _ { 1 } y = b _ { 1 } + C ^ { T } v$ and $U x = y$

Neglecting higher order terms in $p$ ,the initial LU factorization requires $m n ^ { 2 } - n ^ { 3 } / 3$ flops and computing $C$ requires $p n ^ { 2 }$ flops. Forming and solving the normal equations for $v$ takes about $n p ^ { 2 }$ flops. Finally, solving the triangular systems $L _ { 1 } y = C ^ { T } v + b _ { 1 }$ and $U x = y$ takes $2 n ^ { 2 }$ flops. For $p \ll n$ the total arithmetic cost $m n ^ { 2 } - n ^ { 3 } / 3 + p n ^ { 2 }$ is lower than that required by the normal equations.

Equation (2.4.9) is the normal equation for the problem

$$
\operatorname* { m i n } _ { \widetilde { y } _ { 2 } } \left\| \left( \begin{array} { c } { { I _ { p } } } \\ { { C ^ { T } } } \end{array} \right) v - \left( \begin{array} { c } { { b _ { 2 } } } \\ { { - b _ { 1 } } } \end{array} \right) \right\| _ { 2 }
$$

and can be solved by a QR factorization of size $( p + n ) \times p$

The least-norm problem

$$
\operatorname* { m i n } \| y \| _ { 2 } { \mathrm { ~ s u b j e c t ~ t o ~ } } A ^ { T } y = c
$$

can be treated similarly. f $A = L U$ $L = { \binom { L _ { 1 } } { L _ { 2 } } }$ ,then

$$
\begin{array} { r } { y _ { 1 } + { C ^ { T } } y _ { 2 } = L _ { 1 } ^ { - T } { U ^ { - T } } c = d , \quad C = L _ { 2 } L _ { 1 } ^ { - 1 } , \quad y = \left( \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \end{array} \right) . } \end{array}
$$

This shows that $y _ { 2 }$ is the solution to the damped least squares problem of full rank,

$$
\operatorname* { m i n } _ { y _ { 2 } } \left\| \left( { C ^ { T } \atop I _ { p } } \right) y _ { 2 } - \left( { d \atop 0 } \right) \right\| _ { 2 } .
$$

The normal equations are $( C C ^ { T } + I _ { p } ) y _ { 2 } = C f .$ . The algorithm can be summarized as follows:

1. Comput ge $\begin{array} { r } { \widetilde { A } = \Pi _ { 1 } A \Pi _ { 2 } = \left( { L _ { 1 } } \atop { L _ { 2 } } \right) U . } \end{array}$

2. Solve $L _ { 1 } ^ { T } C = L _ { 2 } ^ { T }$ and $U _ { 1 } ^ { T } L _ { 1 } ^ { T } d = c$ for $C$ and $d$

3. Form and solve the normal equations $( C C ^ { T } + I _ { p } ) y _ { 2 } = C d .$

4. Compute $y _ { 1 } = - C ^ { T } y _ { 2 }$

Cardenal, Duff,and Jiménez [2O8,19g8] derive similar formulas for quasi-square least squares problems by using the augmented system formulation. They implement and test the new methods using both dense LU routines from LAPACK and the sparse LU solver MA48 from the Harwell Software Library (HSL). Tests carried out confirm that the new method is much faster than either the normal equations or the original Peters-Wilkinson method. Furthermore,their sparse implementation outperformed the dense solvers on problems as small as a few hundred equations.

An alternative suggested by Tewarson [1058,1968] is to solve the least squares subproblem $\mathrm { m i n } _ { y } \parallel L y - \Pi _ { 1 } b \parallel _ { 2 }$ in (2.4.2) by an orthogonal reduction of the trapezoidal matrix $L$ to lower triangular form:

$$
Q \left( \begin{array} { c } { { L _ { 1 } } } \\ { { L _ { 2 } } } \end{array} \right) = \left( \begin{array} { c } { { \bar { L } } } \\ { { 0 } } \end{array} \right) , \qquad Q \Pi _ { 1 } b = \left( \begin{array} { c } { { c _ { 1 } } } \\ { { c _ { 2 } } } \end{array} \right) .
$$

Such an algorithm is given by Cline [253,1973]. The lower trapezoidal structure in $\bar { L }$ is pre-served by taking $Q$ as a product of Householder reflectors,

$$
Q = P _ { 1 } \cdot \cdot \cdot P _ { n - 1 } P _ { n } ,
$$

where $P _ { k }$ is chosen to zero the elements $\ell _ { n + 1 , k } , \dots , l _ { m , k }$ This reduction requires $2 n ^ { 2 } ( m -$ $n$ ） flops.The least squares solution is then obtained in $2 n ^ { 3 } / 3$ flops from the lower triangular system $\bar { L } y = c _ { 1 }$ . Cline's algorithm is very efficient for least squares problems that are slightly overdetermined, i.e., $p = m - n \ll n$ . The total number of flops required for computing the least squares solution is about ${ \frac { 2 } { 3 } } n ^ { 3 } + 3 p n ^ { 2 }$ . This is fewer than needed for the method of normal equations if $p \leq n / 3$ For $p \leq 2 n / 3$ it is also more efficient than using the Householder QR factorization of $A$

Plemmons [897,1974l solves the least squares subproblem (2.4.2) by MGS. The trapezoidal structure in $L$ is preserved by applying MGS in reverse order from the last to the first column of $L$ 、This method requires a total of ${ \textstyle { \frac { 4 } { 3 } } } n ^ { 3 } + 3 p n ^ { 2 }$ flops, which is slightly more than needed for Cline's algorithm. Similar orthogonalization methods for the underdetermined case ( $m < n )$ are given by Cline and Plemmons [258,1976].

# Notes and references

The use of LU factorization in least squares algorithms was proposed by Ben-Israel and Wersan [102,1963], Tewarson [1058,1968],and Noble [831,196g]. Bjorck and Duff [139,1980] use a slightly modified version of the Peters-Wilkinson method for solving sparse least squares problems and discuss extensions of the method to handle linear constraints.

# 2.4.3 - Rank-Revealing LU Factorizations

If Gaussian elimination with complete pivoting is applied in exact arithmetic to $A \in \mathbb { R } ^ { m \times n }$ ， $m \geq n$ ,and $\operatorname { r a n k } ( A ) = k < n$ ,this yields after $k$ steps a factorization

$$
\begin{array} { r } { \bar { A } = \Pi _ { 1 } A \Pi _ { 2 } = \left( \begin{array} { c c } { L _ { 1 1 } } & { 0 } \\ { L _ { 2 1 } } & { I _ { m - k } } \end{array} \right) \left( \begin{array} { c c } { U _ { 1 1 } } & { U _ { 2 1 } } \\ { 0 } & { U _ { 2 2 } } \end{array} \right) , } \end{array}
$$

where $L _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ is unit lower unit triangular, $U _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ is upper triangular, and $U _ { 2 2 } = 0$ Hence the rank of the matrix is revealed. However, when $A$ is nearly rank-deficient, then even with complete pivoting, $\| U _ { 2 2 } \|$ may not be small, as shown by the following example by Peters and Wilkinson [892,197o]. For the upper triangular Wilkinson matrix

$$
W = \left( \begin{array} { c c c c c } { 1 } & { - 1 } & { - 1 } & { \cdots } & { - 1 } \\ & { 1 } & { - 1 } & { \cdots } & { - 1 } \\ & & { \ddots } & { \cdots } & { \vdots } \\ & & & { 1 } & { - 1 } \\ & & & & { 1 } \end{array} \right) \in \mathbb { R } ^ { n \times n } ,
$$

the smallest singular value of $W$ is of size $2 ^ { - ( n - 2 ) }$ ,although no diagonal elementis small.

For matrices having only one smal singular value, Chan [223,1984] shows that there always exists a permutation such that the near-rank-deficiency is revealed by LU factorization. Further-more,these permutations are related to the size of elements in $A ^ { - 1 }$ .Let $A \in \mathbb { R } ^ { m \times n }$ have the SVD

$$
A = U \Sigma V ^ { T } = \sum _ { i = 1 } ^ { n } \sigma _ { i } u _ { i } v _ { i } ^ { T } ,
$$

and assume that $\sigma _ { n - 1 } \gg \sigma _ { n } > 0$ ，Then the last term $\sigma _ { n } ^ { - 1 } v _ { n } u _ { n } ^ { T }$ in the pseudoinverse $A ^ { \dagger } =$ $\textstyle \sum _ { i = 1 } ^ { n } \sigma _ { i } ^ { - 1 } v _ { i } u _ { i } ^ { T }$ will dominate.Let $i , j$ be indices corresponding to the maximum value of $| ( u _ { n } ) _ { i } ( v _ { n } ) _ { j } |$ .Then permuting $a _ { i j }$ to the $( n , n )$ th position will produce a rank-revealing LU (RRLU) factorization with $u _ { n n } = \overset { \^ } { 2 } \overset { - } { - } \overset { ( n - 2 ) } { \approx } \sigma _ { n } ( A )$ For the matrix $W$ in (2.4.13), the largest element of the inverse

$$
W ^ { - 1 } = \left( \begin{array} { c c c c c } { { 1 } } & { { 1 } } & { { 2 } } & { { \ddots } } & { { 2 ^ { n - 2 } } } \\ { { } } & { { 1 } } & { { 1 } } & { { \ddots } } & { { 2 ^ { n - 3 } } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { } } & { { 1 } } \end{array} \right) \in \mathbb { R } ^ { n \times n }
$$

is in the $( 1 , n )$ th position. Hence a rank-revealing LU factorization should be obtained by permuting element $( n , 1 )$ to position $( n , n )$ .Switching the first and last columns of $R$ gives $R \Pi _ { 1 , n } = L U$ ,where $u _ { n n } = 2 ^ { - ( n - 2 ) }$

Chan suggests the following algorithm. Compute a pivoted LU factorization of $A$ ,and then use inverse iteration to find approximate singular vectors $u _ { n }$ and $v _ { n }$ . Determine $( i , j )$ so that $\vert ( u _ { n } ) _ { i } ( v _ { n } ) _ { j } \vert$ is maximal, permute element $a _ { j i }$ to the $( n , n )$ th position, and recompute the LU factorization with a pivoting strategy that is restricted to permuting only the first $n - 1$ rows and columns.The cost of this algorithm is at most two LU factorizations and a few back solves.

For the general case,where $A$ may have several small singular values, the existence of a rank-revealing LU (RRLU) factorization is proved by Pan [873, 2ooo,Theorem 1.2].

Theorem 2.4.2. Let $A \in \mathbb { R } ^ { n \times n }$ have singular values $\sigma _ { 1 } \geq \cdot \cdot \cdot \geq \sigma _ { n } \geq 0 .$ Then for any given $k$ ， $1 \leq k < n$ ,there exist permutations $\Pi _ { 1 }$ and $\Pi _ { 2 }$ such that in the factorization (2.4.12), $L _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ is unit lower triangular, $U _ { 1 1 } \in \mathbb { R } ^ { k \times k }$ is upper triangular, and

$$
\begin{array} { r l } & { \sigma _ { \operatorname* { m i n } } ( U _ { 1 1 } ) \geq \sigma _ { k } / ( k ( n - k ) + 1 ) , } \\ & { \sigma _ { \operatorname* { m a x } } ( U _ { 2 2 } ) \leq ( k ( n - k ) + 1 ) \sigma _ { k + 1 } . } \end{array}
$$

The bounds established in (2.4.14) and (2.4.15) are strikingly similar to the bounds established in Theorem 2.3.6 for rank-revealing QR factorizations.If $\| U _ { 2 2 } \| _ { 2 }$ is sufficiently small, then a rank- $k$ approximation of $A$ is

$$
A = \Pi _ { 1 } ^ { T } \left( { \begin{array} { l } { L _ { 1 1 } } \\ { L _ { 2 1 } } \end{array} } \right) \left( U _ { 1 1 } \quad U _ { 2 1 } \right) \Pi _ { 2 } ^ { T } .
$$

In addition to the generalized LU factorization (2.4.12) we introduce the block LU factorization

$$
\bar { A } = \left( \begin{array} { c c } { { I _ { k } } } & { { 0 } } \\ { { \bar { A } _ { 2 1 } \bar { A } _ { 1 1 } ^ { - 1 } } } & { { I _ { n - k } } } \end{array} \right) \left( \begin{array} { c c } { { \bar { A } _ { 1 1 } } } & { { \bar { A } _ { 1 2 } } } \\ { { 0 } } & { { S } } \end{array} \right) ,
$$

where $S = \bar { A } _ { 2 2 } - \bar { A } _ { 2 1 } \bar { A } _ { 1 1 } ^ { - 1 } \bar { A } _ { 1 2 }$ is the Schur complement.

f $\bar { A } _ { 1 1 } = L _ { 1 1 } U _ { 1 1 }$ is nonsingular, a rank $k$ approximation of $\bar { A }$ is

$$
\bar { A } = \left( \begin{array} { l } { \bar { A } _ { 1 1 } } \\ { \bar { A } _ { 2 1 } } \end{array} \right) \bar { A } _ { 1 1 } ^ { - 1 } \left( \begin{array} { l l } { \bar { A } _ { 1 1 } } & { \bar { A } _ { 1 2 } } \end{array} \right) .
$$

If $k$ is small, this approximation preserves a large part of $A$ .When $A$ is large and sparse this can give large savings of memory and arithmetic. Goreinov, Tyrtyshnikov, and Zamarashkin [519, 1997] cal this a pseudoskeleton approximation. They derive tighter bounds using an approach that relies heavily on information from the SVD.

Pan [873, 2ooo] used the concept of local maximum volume and showed how this could be used to find a pivoting strategy that works for finding both RRLU and RRQR factorizations; see Section 2.4.3.

Definition 2.4.3. Let $B$ be a submatrix of $A \in \mathbb { R } ^ { m \times n }$ formed by any $k$ columns (rows) of $A$ Then $B$ is said to have local maximum volume $i f$

$$
\operatorname { v o l } \left( B \right) = \sigma _ { 1 } ( B ) \cdot \cdot \cdot \sigma _ { n } ( B ) \geq \operatorname { v o l } \left( B ^ { \prime } \right)
$$

for any $B ^ { \prime }$ obtained by replacing one column $( r o w )$ of $B$ with a column (row) of $A$ not in $B$

Note that to determine if $B$ has a local maximum volume, it is only necessary to compare its volume with the volumes of $k ( n - k )$ neighboring submatrices that differ from $B$ in exactly one column (row). In floating-point computations, (2.4.17) should be replaced by $\mathrm { v o l } \left( B \right) \geq$ $\operatorname { v o l } \left( B ^ { \prime } \right) / \mu$ ，where $\mu > 1$ is a fudge factor.

Lemma 2.4.4. Let $A = { \binom { A _ { 1 } } { A _ { 2 } } } \in \mathbb { R } ^ { n \times k }$ ,where $A _ { 1 } \in \mathbb { R } ^ { k \times k }$ ， $n > k$ Then

$$
\| A _ { 2 } A _ { 1 } ^ { - 1 } \| _ { 2 } \le \sqrt { k ( n - k ) + 1 }
$$

provided $\operatorname { v o l } \left( A _ { 1 } \right)$ is a local maximum in $A$

Proof. Let $M = ( m _ { i j } ) = A _ { 2 } A _ { 1 } ^ { - 1 }$ so that $\left( \begin{array} { c } { { I } } \\ { { M } } \end{array} \right) A _ { 1 } = \left( \begin{array} { c } { { A _ { 1 } } } \\ { { A _ { 2 } } } \end{array} \right)$ Since the submatrix $A _ { 1 }$ has maximum local volume in $A$ , it follows that $I$ has maximum local volume in $\left( \begin{array} { c } { { I } } \\ { { M } } \end{array} \right)$ For any $m _ { i j } \neq 0$ , interchange row $i$ of $M$ with row $j$ in $I$ .Denote the new matrix by $\left( \begin{array} { c } { { I ^ { \prime } } } \\ { { M ^ { \prime } } } \end{array} \right)$ Then $\begin{array} { r l r } { \mathrm { v o l } \left( I ^ { \prime } \right) } & { { } \le } & { \mathrm { v o l } \left( I \right) } \end{array}$ ，which implies that $| m _ { i j } | \le 1$ Finally, $\| M \| _ { 2 } ~ \leq ~ \| M \| _ { F } ~ \leq$ $\sqrt { k ( n - k ) }$ □

From this lemma we obtain the following result.

Lemma 2.4.5. Let $A = { \binom { A _ { 1 } } { A _ { 2 } } } \in \mathbb { R } ^ { n \times k }$ ,where $A _ { 1 } \in \mathbb { R } ^ { k \times k }$ ， $n > k$ Then

$$
\sigma _ { \operatorname* { m i n } } ( A _ { 1 } ) \geq \sigma _ { k } ( A ) / \sqrt { k ( n - k ) + 1 }
$$

provided $\operatorname { v o l } \left( A _ { 1 } \right)$ is a local maximum in $A$

Proof. Assume that the QR factorization of $A$ is $A \ = \ Q R$ ，where $Q \ = \ \left( { { Q } _ { 1 } } \right)$ Since $\operatorname { v o l } \left( Q _ { 1 } \right) \operatorname { v o l } \left( R \right) = \operatorname { v o l } \left( A _ { 1 } \right)$ , it follows that $\mathrm { v o l } \left( Q _ { 1 } \right)$ is a local maximum in $Q$

To find a rank- $k$ ， $1 \leq k < n$ ,RRLU factorization of $A \in \mathbb { R } ^ { n \times n }$ one first selects a subset of $k$ columns with local maximum volume in $A$ and then a subset of $k$ rows with local maximum volume in the selected $k$ columns.Pan [873,2ooo] gives two algorithms.Algorithm 1 selects an $m \times m$ submatrix of a matrix $A \in \mathbb { R } ^ { m \times n }$ ,with $\operatorname { r a n k } ( A ) = m < n$ . It starts by computing the LU factorization with partial pivoting

$$
\Pi _ { 1 } A \Pi _ { 2 } = L U = L \left( U _ { 1 } \quad U _ { 2 } \right) ,
$$

where $\Pi _ { 1 } = I$ and $\left| u _ { k k } \right| \ge \left| u _ { k j } \right|$ ， $k < j \leq n$ . This is followed by a block pivoting phase in which column $j$ of $U _ { 1 } , j = m - 1 , \ldots , 1$ , is permuted to the last position in $U _ { 1 }$ , and the permuted $U _ { 1 }$ is retriangularized by Gaussian elimination. If the updated matrix fails to satisfy the condition

$$
| u _ { m m } | \geq \operatorname* { m a x } _ { 1 \leq j \leq n } | u _ { m j } | ,
$$

a column interchange between $U _ { 1 }$ and $U _ { 2 }$ is performed to restore condition (2.4.20).Whenever such an interchange takes place the procedure of permuting every column in $U _ { 1 }$ to the last is repeated. When a complete block pivoting phase has been performed without violating condition (2.4.20), the product $L U _ { 1 }$ has maximum local volume in $A$ , and the algorithm stops.

If the interchanges in the block pivoting phase are done by a cyclic shift, the permuted matrix $U _ { 1 }$ will have Hessenberg form. For example, for $m = 5$ ,permuting columns 2 and 5 produces a matrix with structure

$$
\begin{array} { r } { \begin{array} { c c c c c c } { x } & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { } \\ & & { \times } & { \times } & { } \\ & & & { \times } & { \times } \end{array} . } \end{array}
$$

For stability reasons,row pivoting should be employed in the retriangularization. A complete block pivoting without column interchanges between $U _ { 1 }$ and $U _ { 2 }$ requires about $m ^ { 2 } n - ( 1 / 3 ) m ^ { 3 }$ flops. This algorithm is faster than the corresponding QR approach even without an explicit $Q$

The second algorithm of Pan selects $k < \mathrm { m i n } \{ m , n \}$ columns from $A \in \mathbb { R } ^ { m \times n }$ by com-puting a rank-revealing Cholesky factorization. It is initialized with an uncompleted Cholesky factorization with diagonal pivoting of $A ^ { T } A$ .Like Algorithm 1 it uses block pivoting to find a symmetric permutation such that the leading principal submatrix of order $k$ has local maximum volume. Combined with Algorithm 1 this yields an algorithm for finding an RRLU factorization.

# Notes and references

Hwang,Lin,and Yang 652,1992] were the first to consider RRLU factorizations with numerical rank-deficiency $p > 1$ .However, their bounds may increase faster than exponentially. Improved bounds are given in Hwang,Lin,and Pierce [651,1997]. Miranian and Gu [796, 20o3] study strong rank-revealing LU factorizations for which the elements of $W _ { l } = L _ { 2 1 } L _ { 1 1 } ^ { - 1 }$ and $W _ { r } =$ $U _ { 1 1 } ^ { - 1 } U _ { 1 2 }$ are bounded by some slow growing polynomial in $k , m$ ,and $n$

# 2.4.4 - Elimination Methods for Augmented Systems

If $\operatorname { r a n k } ( A ) \ = \ n$ ， the least squares problem $\operatorname* { m i n } _ { x } \| b - A x \| _ { 2 }$ is equivalent to the symmetric indefinite augmented system

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { r } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { b } } \\ { { 0 } } \end{array} \right) .
$$

Eliminating $y$ using Gaussian elimination without pivoting gives the reduced upper block trian-gular system

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { 0 } } & { { - A ^ { T } A } } \end{array} \right) \left( \begin{array} { c } { { y } } \\ { { x } } \end{array} \right) = \left( \begin{array} { c } { { b } } \\ { { - A ^ { T } b } } \end{array} \right) .
$$

Hence this choice of pivots just leads to the normal equations. To get a more stable method, it is necessary to choose pivots outside the block $I$

Introducing the scaled residual vector $s = \alpha ^ { - 1 } r$ gives the augmented system

$$
\left( \begin{array} { c c } { { \alpha I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { \alpha ^ { - 1 } r } } \\ { { x } } \end{array} \right) = \left( \begin{array} { c } { { b } } \\ { { 0 } } \end{array} \right) \quad \Longleftrightarrow \quad M _ { \alpha } z _ { \alpha } = d _ { \alpha } ,
$$

where we assume that $0 \leq \alpha \leq \| A \| _ { 2 } = \sigma _ { 1 } ( A )$ .The scaling parameter $\alpha$ will affect the conditioning of $M _ { \alpha }$ as well as the choice of pivots and thereby the accuracy of the computed solution. For sufficiently small values of $\alpha$ ，pivots will not be chosen from the $( 1 , 1 )$ block. However,mixing the unknowns $x$ and $r$ does not make sense physically, because they have different physical units and may be on vastly different scales numerically.

For a general symmetric indefinite matrix $M$ ，astable symmetric indefinite factorization $\Pi M \Pi ^ { T } = { \cal L } D { \cal L } ^ { T }$ with $D$ diagonal always exists if $2 \times 2$ symmetric blocks in $D$ are allowed. A pivoting scheme due to Bunch and Kaufman [187,1977] guarantees control of element growth without requiring too much searching. The symmetry constraint allows row and column permutations to bring any diagonal element $d _ { 1 } = b _ { r r }$ or any $2 \times 2$ submatrix of the form

$$
\left( \begin{array} { l l } { b _ { r r } } & { b _ { r s } } \\ { b _ { s r } } & { b _ { s s } } \end{array} \right) \quad ( b _ { r s } = b _ { s r } )
$$

to the pivot position. Taking a $2 \times 2$ submatrix as a pivot is equivalent to a double step of Gaussian elimination and pivoting first on $b _ { r s }$ and then on $b _ { s r }$ . Such a double step preserves symmetry, and only elements on and below the main diagonal of the reduced matrix need to be computed. Ultimately,a factorization $A = L D L ^ { T }$ is obtained where $D$ is block diagonal with a mixture of $1 \times 1$ and $2 \times 2$ blocks. $L$ is unit lower triangular with $\ell _ { k + 1 , k } = 0$ when $B ^ { ( k ) }$ is reduced by a $2 \times 2$ pivot.The Bunch-Kaufman strategy is to search until two columns $r$ and $s$ are found for which the common element $b _ { r s }$ bounds in modulus the other off-diagonal elements in the $r$ and $s$ columns.Then either a $2 \times 2$ pivot on these two columns or a $1 \times 1$ pivot with the largest in modulus of the two diagonal elements is taken,according to the test

$$
\operatorname* { m a x } ( | b _ { r r } | , | b _ { s s } | ) \geq \rho | b _ { r s } | , \quad \rho = ( \sqrt { 1 } 7 + 1 ) / 8 \approx 0 . 6 4 0 4 .
$$

The number $\rho$ has been chosen to minimize the growth per stage of elements of $B$ ,allowing for the fact that two stages are taken by a $2 \times 2$ pivot. With this choice, element growth is bounded by $g _ { n } \leq ( 1 + 1 / \rho ) ^ { n - 1 } < ( 2 . 5 7 ) ^ { n - 1 }$ . This bound can be compared to the bound $2 ^ { n - 1 }$ that holds for Gaussian elimination with partial pivoting.

The above bound for element growth can be achieved with fewer comparisons using a strategy due to Bunch and Kaufman. Let $\lambda = \left| b _ { r 1 } \right| = \operatorname* { m a x } _ { 2 \leq i \leq n } \left| b _ { i 1 } \right|$ be the off-diagonal element of largest magnitude in the first column. If $\left| b _ { 1 1 } \right| \geq \rho \lambda$ ,take $b _ { 1 1 }$ as a pivot. Otherwise,determine the largest off-diagonal element in column $r$ ：

$$
\sigma = \operatorname* { m a x } _ { 1 \leq i \leq n } | b _ { i r } | , \quad i \neq r .
$$

If $| b _ { 1 1 } | \ge \rho \lambda ^ { 2 } / \sigma$ , again take $b _ { 1 1 }$ as a pivot; else if $\left| b _ { r r } \right| \geq \rho \sigma$ ,take $b _ { r r }$ as a pivot. Otherwise, take the $2 \times 2$ pivot corresponding to the off-diagonal element $b _ { 1 r }$ . Note that at most two columns need

to be searched in each step,and at most $n ^ { 2 }$ comparisons are needed in all. When the factorization $M = L D L ^ { T }$ has been obtained, the solution of $M z = d$ is obtained in the three steps

$$
\begin{array} { r } { L v = d , \quad D w = v , \quad L ^ { T } z = w . } \end{array}
$$

It has been shown by Higham [621,1997] that for stability it is necessary to solve the $2 \times 2$ systems arising in $D w = v$ using partial pivoting or the explicit $2 \times 2$ inverse. The proof of this is nontrivial and makes use of the special relations satisfied by the elements of the $2 \times 2$ pivots in the Bunch-Kaufman pivoting scheme.

Bunch-Kaufman pivoting does not in general give a stable method for the least squares problem, because perturbations introduced by roundof do not respect the structure of the augmented system.For the scaled system (2.4.21) with a sufficiently small value of $\alpha$ the Bunch-Kaufman scheme will introduce $2 \times 2$ pivots of the form

$$
\left( \begin{array} { c c } { { \alpha } } & { { a _ { 1 r } } } \\ { { a _ { 1 r } } } & { { 0 } } \end{array} \right) ,
$$

which may improve the stability. This raises the question of the optimal choice of $\alpha$ for stability. The eigenvalues $\lambda$ of $M _ { \alpha }$ can be expressed in terms of the singular values $\sigma _ { i }$ ， $i = 1 , \ldots , n$ of $A$ ; see Bjorck [124,1967]. If $M _ { \alpha } z = \lambda z$ ， $\boldsymbol { z } = ( s , x ) ^ { T } \neq \boldsymbol { 0 }$ ,then

$$
\alpha s + A x = \lambda s , \qquad A ^ { T } s = \lambda x ,
$$

or, eliminating $s , \alpha \lambda x + A ^ { T } A x = \lambda ^ { 2 } x .$ Hence if $x \neq 0$ ,then $x$ is an eigenvector and $\left( \lambda ^ { 2 } - \alpha \lambda \right)$ an eigenvalue of $A ^ { T } A$ .On the other hand, $x = 0$ implies that $A ^ { T } s = 0$ ， $\alpha s = \lambda s$ ， $s \neq 0$ It follows that the $m + n$ eigenvalues of $M _ { \alpha }$ are

$$
\lambda = { \left\{ \begin{array} { l l } { \alpha / 2 \pm { \sqrt { \alpha ^ { 2 } / 4 + \sigma _ { i } ^ { 2 } } } , } & { i = 1 , \ldots , n , } \\ { \alpha } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

If $\operatorname { r a n k } ( A ) = r \leq n$ ，then the eigenvalue $\alpha$ has multiplicity $( m - r )$ , and O is an eigenvalue of _multiplicity $( n - r )$ .From this it is easily deduced that if $\sigma _ { n } > 0$ ，then $\mathrm { m i n } _ { \alpha } \kappa _ { 2 } ( M _ { \alpha } ) \approx$ ${ \sqrt { 2 } } \kappa _ { 2 } ( A )$ is attained for $\alpha = \tilde { \alpha } = 2 ^ { - 1 / 2 } \sigma _ { n } \dot { ( } A )$ . Therefore, $\tilde { \alpha }$ (or $\sigma _ { n }$ ） can be used as a nearly optimal scaling factor in the augmented system method. Minimizing $\kappa _ { 2 } ( M _ { \alpha } )$ will minimize the forward bound for the error in $z _ { \alpha }$ ，

$$
\| \bar { z } _ { \alpha } - z _ { \alpha } \| _ { 2 } \leq \frac { \epsilon \kappa ( M _ { \alpha } ) } { 1 - \epsilon \kappa ( M _ { \alpha } ) } \| z _ { \alpha } \| _ { 2 } , \qquad z _ { \alpha } = \binom { \alpha ^ { - 1 } r } { x } .
$$

However, $\alpha$ also influences the norm in which the error is measured.

Pivoting and stability in the augmented system method is studied by Bjorck [133,1992]. A more refined error analysis is given here that separately minimizes bounds for the errors in $\bar { x }$ and $\bar { y }$ . It is shown that the errors in the computed solution satisfy the upper bounds

$$
\begin{array} { r } { \left( \begin{array} { c } { \| \bar { r } - r \| _ { 2 } } \\ { \| \bar { x } - x \| _ { 2 } } \end{array} \right) \leq c g \mathbf { u } f ( \alpha ) \left( \begin{array} { c } { \sigma _ { 1 } ( A ) } \\ { \kappa _ { 2 } ( A ) } \end{array} \right) , } \end{array}
$$

where $c$ is a low-degree polynomial, $g$ the growth factor, and

$$
f ( \alpha ) = \left( 1 + \frac { \alpha } { \sigma _ { n } } \right) \left( \frac { 1 } { \alpha } \| r \| _ { 2 } + \| x \| _ { 2 } \right) .
$$

If $x \neq 0$ then $f ( \alpha )$ is minimized for $\alpha = \alpha _ { \mathrm { o p t } } = \left( \sigma _ { n } \| r \| _ { 2 } / \| x \| _ { 2 } \right) ^ { 1 / 2 }$ . The corresponding minimum value of $f ( \alpha )$ is

$$
f _ { \mathrm { m i n } } = \biggl ( 1 + \frac { \alpha _ { \mathrm { o p t } } } { \sigma _ { n } } \biggr ) ^ { 2 } \| x \| _ { 2 } = \biggl ( 1 + \frac { \sigma _ { n } } { \alpha _ { \mathrm { o p t } } } \biggr ) ^ { 2 } \sigma _ { n } ^ { - 1 } \| r \| _ { 2 } .
$$

Taking $\alpha = \sigma _ { n }$ we find

$$
f ( \sigma _ { n } ) = 2 \biggl ( \frac { 1 } { \sigma _ { n } } \| r \| _ { 2 } + \| x \| _ { 2 } \biggr ) \leq 2 f _ { \operatorname* { m i n } } ,
$$

i.e., using $\alpha = \sigma _ { n }$ will at most double the error bound.

We recall that an acceptable-error stable algorithm is defined as one that gives a solution for which the size of the error is never significantly greater than the error bound obtained from a tight perturbation analysis. It can be shown that the augmented system method is acceptableerror stable with both $\alpha = \sigma _ { n }$ and $\alpha = \alpha _ { \mathrm { o p t } }$

# $\pm . 5 .$ Estimating Condition Numbers and Errors

# 2.5.1 - Condition Estimators

The perturbation bounds for the least squares solution $x$ given in Section 1.3.4 depend critically on the condition number $\kappa _ { 2 } ( A ) = \sigma _ { 1 } ( A ) / \sigma _ { n } ( A )$ . If the QR factorization $A = Q R$ is known then we have

$$
\kappa ( A ) = \kappa ( R ) \leq \| R \| _ { F } \| R ^ { - 1 } \| _ { F } .
$$

But computing $R ^ { - 1 }$ takes $n ^ { 3 } / 3$ flops, which usually is too expensive. Combining the estimates (2.3.20) and (2.3.25) we obtain the lower bound

$$
\kappa ( A ) = \sigma _ { 1 } ( R ) / \sigma _ { n } ( R ) \geq | r _ { 1 1 } / r _ { n n } | .
$$

Empirical evidence suggests that, provided column pivoting has been used in the QR factorization,it is very rare for the bound in(2.5.1) to differ much from $\kappa ( A )$ .In extensive tests on randomly generated test matrices,the bound usually underestimated the true condition number by a factor of only 2-3 and never by more than 10. However,as shown by Example 2.3.3, the bound (2.5.1) can still be a considerable underestimate of $\kappa ( A )$

Improved estimates of $\kappa ( R )$ can be computed in only $O ( n ^ { 2 } )$ flops by using inverse iteration. Let the singular values of $A$ be $\sigma _ { i }$ ， $i = 1 , \ldots , n$ ，where $\sigma _ { n } < \sigma _ { i }$ ， $i \neq n$ .Then the dominating eigenvalue $\bar { \sigma } _ { 1 } ^ { - 2 }$ of the matrix

$$
C = ( A ^ { T } A ) ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 }
$$

can be computed by applying the power method to $( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }$ . In each step, two triangular linear systems

$$
R ^ { T } y ^ { ( k ) } = z ^ { ( k - 1 ) } , \qquad R z ^ { ( k ) } = y ^ { ( k ) } , \quad k = 1 , 2 , \ldots ,
$$

are solved, which requires $2 n ^ { 2 }$ flops. After normalization, $z ^ { ( k ) }$ will converge totherightsingular vector $v _ { n }$ corresponding to an eigenvalue,and

$$
\begin{array} { r } { \sigma _ { 1 } ^ { - 2 } = v _ { 1 } ^ { T } R ^ { - T } R ^ { - 1 } v _ { 1 } = \| R ^ { - 1 } v _ { 1 } \| _ { 2 } ^ { 2 } . } \end{array}
$$

Example 2.5.1. Failure to detect near-rank-deficiency of $A$ even in the (unusual) case when this is not revealed by a small diagonal element in $R$ can lead to a meaningless solution of very large norm. Inverse iteration will often prevent that. For example, the $n \times n$ upper triangular Wilkinson matrix

$$
W = \left( \begin{array} { c c c c c } { { 1 } } & { { - 1 } } & { { \cdots } } & { { - 1 } } & { { - 1 } } \\ { { } } & { { 1 } } & { { \cdots } } & { { - 1 } } & { { - 1 } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { \vdots } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - 1 } } \\ { { } } & { { } } & { { } } & { { } } & { { 1 } } \end{array} \right)
$$

has numerical rank n - 1 when n is large. Ifn = 5O and W is perturbed by changing the 50,1 entry to $- 2 ^ { - 4 8 }$ , the new matrix $\hat { W }$ will be exactly singular. The smallest singular value of $W$ is bounded by

$$
\sigma _ { 5 0 } \le \| { \cal W } - \hat { { \cal W } } \| _ { { \cal F } } = 2 ^ { - 4 8 } \approx 7 . 1 0 5 \cdot 1 0 ^ { - 1 5 } .
$$

The next smallest singular value is $\sigma _ { 4 9 } \approx 1 . 5$ , so there is a well-defined gap between $\sigma _ { 4 9 }$ and $\sigma _ { 5 0 }$ But in the QR factorization $R = W$ and gives no indication of the numerical rank-deficiency. (If column interchanges are employed, the diagonal elements in $R$ indicate rank 49.) Doing a single inverse iteration on $W ^ { T } W$ using the MATLAB script

$$
\begin{array} { r l } & { \texttt { n } = \texttt { 5 0 } ; \quad \texttt { W } = \texttt { e y e } ( \mathrm { n } ) \ \texttt { - } \ \mathrm { t r i u } ( \mathrm { o n e s } \left( \mathrm { n } , \mathrm { n } \right) , 1 ) ; } \\ & { \texttt { z } = \mathrm { o n e s } \left( \mathrm { n } , 1 \right) ; \quad \texttt { x } = \texttt { W } \backslash \left( \texttt { W } ^ { \prime } \backslash \boldsymbol { z } \right) ; } \\ & { \texttt { s } = \texttt { 1 } / \mathrm { s q r t } \left( \mathrm { m a x } \left( \mathrm { a b s } \left( \mathrm { x } \right) \right) \right) ; } \end{array}
$$

gives an approximate smallest singular value $s = 1 . 9 3 2 3 { \cdot } 1 0 ^ { - 1 5 }$ . A second inverse iteration gives a value of 2.3666.10-30.

The condition estimator given by A. K. Cline et al. [256,1979],often referred to as the LINPACK condition estimator, proceeds as follows:

1. Choose a vector $d$ such that $\| y \| / \| d \|$ is large, where $R ^ { T } y = d$

2. Solve $R z = y$ , and estimate $\lVert R ^ { - 1 } \rVert \approx \lVert z \rVert / \lVert y \rVert \le \lVert R ^ { - 1 } \rVert .$

This is equivalent to one step of the power method with $( A ^ { T } A ) ^ { - 1 }$ .Let $R = U \Sigma V ^ { T }$ be the SVD of $R$ .Expanding $d$ in terms of the right singular vectors $V$ gives

$$
d = \sum _ { i = 1 } ^ { n } \alpha _ { i } v _ { i } , \quad y = \sum _ { i = 1 } ^ { n } ( \alpha _ { i } / \sigma _ { i } ) u _ { i } , \quad z = \sum _ { i = 1 } ^ { n } ( \alpha _ { i } / \sigma _ { i } ^ { 2 } ) v _ { i } .
$$

Hence provided $\alpha _ { n }$ , the component of $d$ along $v _ { n }$ , is not very small, the vector $z$ is likely to be dominated by its component of $v _ { n }$ ,and

$$
\sigma _ { n } ^ { - 1 } \approx \| z \| _ { 2 } / \| y \| _ { 2 }
$$

will usually be a good estimate of $\sigma _ { n } ^ { - 1 }$ . In the LINPACK algorithm the 1-norm is used for normalization． The vector $d$ is chosen as $d = ( \pm 1 , \pm 1 , \dots , \pm 1 ) ^ { T }$ ， where the sign of $d _ { j }$ is determined adaptively; see A. K. Cline et al. [256,1979].

In practice the LINPACK algorithm performs very reliably and produces good order of mag-nitude estimates; see Higham [612, $\mathrm { 1 9 8 7 } ]$ . However, examples of parametrized matrices can be constructed for which the LINPACK estimate can underestimate the true condition number by an arbitrarily large factor. In a modification to the LINPACK condition estimator, O'Leary [837, $1 9 8 0 ]$ suggests that $\lVert R ^ { - 1 } \rVert _ { 1 }$ be estimated by

$$
\operatorname* { m a x } { \big \{ } \| y \| _ { \infty } / \| d \| _ { \infty } , \| z \| _ { 1 } / \| y \| _ { 1 } { \big \} } ,
$$

This makes use of information from the first step,which can improve the estimate.Another generalization, due to A. K. Cline, Conn,and Van Loan [255,1982],of the LINPACK algorithm incorporates a“look-behind" technique. This allows for the possbility of modifying previously chosen $d _ { j }$ 's. It gives an algorithm for the 2-norm that requires about $1 0 n ^ { 2 }$ flops.

Boyd [173,1974] devised a method for_computing a lower bound for an arbitrary Holder norm $\| B \| _ { p }$ , assuming only that $B x$ and $B ^ { T } x$ can be computed for arbitrary vectors $x$ In the following, $p \geq 1$ and $q \geq 1$ are such that $1 / p + 1 / q = 1$ Then $\| \cdot \| _ { q }$ is the dual norm to $\| \cdot \| _ { p }$ and the Holder inequality

$$
| x ^ { T } y | \leq \| x \| _ { p } \| y \| _ { q }
$$

holds. In the algorithm, ${ \mathrm { d u a l } } _ { p } ( x )$ is any vector $y$ of unit $\ell _ { q }$ -norm such that equality holds for $x$ and $y$ in the Holder inequality. A derivation of Boyd's algorithm is given by Higham [623, 2002, Sect. 15.2]. When $p = q = 2$ ，Boyd's algorithm reduces to the usual power method applied to $B ^ { T } B$

For the $\ell _ { 1 }$ -norm the algorithm was derived independently by Hager [560,1984]. In this case the dual norm is the $\ell _ { \infty }$ -norm. Since $\| B \| _ { \infty } = \| B ^ { T } \| _ { 1 }$ ,this algorithm can be used also to estimate the infinity norm.Hager's algorithm is based on convex optimization and uses the observation that $\| B \| _ { 1 }$ is the maximal value of the convex function

$$
f ( x ) = \| B x \| _ { 1 } = \sum _ { i = 1 } ^ { n } | y _ { i } | , \quad y = B x ,
$$

over the convex set $S = \{ x \in \mathbb { R } ^ { n } \mid \| x \| _ { 1 } \leq 1 \}$ . From convexity results it follows that the maximum is attained at one of the vertices $e _ { j }$ ， $j = 1 , \dotsc , n$ of $S$ .From this observation Hager derives an algorithm for finding a local maximum that with high probability is also the global maximum.

# Algorithm 2.5.1 (Hager's Norm Estimator).

Given a matrix $B \in \mathbb { R } ^ { n \times n }$ this algorithm computes $y = B x$ such that $\gamma = \| y \| _ { 1 } / \| x \| _ { 1 } \leq$ $\| B \| _ { 1 }$ Let $e = ( 1 , 1 , \ldots , 1 ) ^ { T }$ ， $e _ { j }$ be the jth unit vector, and $\xi = \mathrm { s i g n } ( y )$ where $\xi _ { i } ~ = ~ \pm 1$ according to whether $y _ { i } \geq 0$ or $y _ { i } < 0$

$$
x = n ^ { - 1 } e ;
$$

$$
\begin{array} { r l } & { y = B x ; \quad \xi = \mathrm { s i g n } ( y ) ; } \\ & { z = B ^ { T } \xi ; } \\ & { \mathrm { i f ~ } \| z \| _ { \infty } \leq z ^ { T } x } \\ & { \qquad \gamma = \| y \| _ { 1 } ; \mathrm { b r e a k } } \end{array}
$$

$$
\mathrm { s e t } x = e _ { j } ; \mathrm { w h e r e } | z _ { j } | = \| z \| _ { \infty } ;
$$

The algorithm tries to maximize $f ( x ) = \| B x \| _ { 1 }$ subject to $\| x \| _ { 1 } = 1$ . The vector $z$ computed at each step can be shown to be a subgradient of $f$ at $x$ .From convexity properties,

$$
f ( \pm e _ { j } ) \geq f ( x ) + z ^ { T } ( \pm e _ { j } - x ) , \qquad j = 1 , \ldots , n .
$$

Hence if $| z _ { j } | > z ^ { T } x$ for some $j$ ,then $f$ can be increased by moving from $x$ to the vertex $e _ { j }$ of $S$ If, however, $\| z \| _ { \infty } \leq z ^ { T } x$ ,and if $y _ { j } \ne 0$ for all $j$ ,then $x$ can be shown to be a local maximum point for $f$ over $S$

Higham [617, 199o] reports on experience in using Hager's algorithm. The estimates produced are generally sharper than those produced by the LINPACK estimator. Its results are frequently exact, usually good $( \gamma \geq 0 . 1 \| B \| _ { 1 } )$ ,but sometimes poor. The algorithm almost always converges after at most four iterations,and Higham recommends that between two and five iterations be used. The average cost for estimating $\| R \| _ { 1 }$ of a triangular matrix $R$ is in practice around $6 n ^ { 2 }$ flops.

An important feature of Hager's norm estimator is that to estimate $\lVert B ^ { - 1 } \rVert _ { 1 }$ we only need to be able to solve linear systems $B y = x$ and $B ^ { T } z = \xi$ . This feature makes it useful for estimating the componentwise error bounds given in Section 1.3.4. For the least squares problem the bound (1.3.56) can be written in the form $\| \delta x \| _ { \infty } \leq \omega { \mathrm { ~ c o n d } } ( A , b ) \| x \| _ { \infty }$ ,where

$$
\operatorname { c o n d } ( A , b ) \leq \left( \| | A ^ { \dagger } | g _ { 1 } \| _ { \infty } + \| | A ^ { T } A ) ^ { - 1 } | g _ { 2 } \| _ { \infty } \right) / \| x \| _ { \infty }
$$

and

$$
g _ { 1 } = | A | | x | + | b | , g _ { 2 } = | A | ^ { T } | r | .
$$

Hager's algorithm gives an inexpensive and reliable estimate of cond $( A , b )$ . The key idea is to note that all terms in (2.5.5) are of the form $\| | B | g \| _ { \infty }$ ,where $g > 0$ .Following Arioli, Demmel, and Duff [33,1989],we take $G = \arg \left( g \right)$ . Then using $g \ = \ G e$ and the properties of the $\ell _ { \infty }$ -norm, we have

$$
\begin{array} { r } { \| | B | g \| _ { \infty } = \| | B | G e \| _ { \infty } = \| B G \| _ { \infty } = \| | B G | e \| _ { \infty } = \| B G \| _ { \infty } . } \end{array}
$$

Hence Hager's algorithm can be applied to estimate $\| | B | g \| _ { \infty }$ provided matrix-vector products $B G x$ and $G ^ { T } B ^ { T } y$ can be computed efficiently. To estimate cond $( A , b )$ we need to be able to compute matrix-vector products of the forms ${ \overset { \cdot } { A ^ { \dag } x } } , ( A ^ { \dag } ) ^ { T } y$ ,and $( A ^ { T } A ) ^ { - 1 } x$ . This can be done efficiently if a QR factorization of $A$ is known.

# Notes and references

A survey of condition estimators is given by Higham [612,1987]. Fortran 77 codes by Higham [614,1988] implementing Hager's condition estimator for the 1-norm of a real or complex matrix are included in LAPACK; see Anderson et al.[26,1995]. Further details and comments on the algorithm are found in Hager [560,1984] and Higham [616,1990].

# 2.5.2 - A Posteriori Estimation of Errors

Let $\bar { x }$ be an approximate solution of a linear least squares problem $\mathrm { m i n } _ { x } \| A x - b \| _ { 2 }$ .If $\bar { x }$ is an exact solution of the perturbed problem

$$
\operatorname* { m i n } _ { x } \| ( A + E ) x - b \| _ { 2 }
$$

for some $E$ ，then $\| E \| _ { 2 }$ is called the backward error of $\bar { x }$ If $\| E \| _ { 2 }$ is small compared to the uncertainty in the data $A$ , then the solution $\bar { x }$ can be said to be as good as the data warrants. The forward error $\lVert x - { \bar { x } } \rVert$ can be estimated using the perturbation bounds given in Section 1.3.3.

In general, $\bar { x }$ solves (2.5.7) for an infinite number of perturbations $E$ .The optimal backward error for a given $\bar { x }$ is defined as

$$
\begin{array} { r } { \mu ( \bar { x } ) = \operatorname* { m i n } \| E \| _ { F } \mathrm { ~ s u b j e c t ~ t o ~ } \| ( A + E ) \bar { x } - b \| _ { 2 } = \operatorname* { m i n } . } \end{array}
$$

To find a good estimate of $\mu ( \bar { x } )$ is important, e.g.,for deciding when to stop an iterative solution method. For a consistent linear system $A x = b$ .Rigal and Gaches [928,1g67] showed that the optimal backward error $E$ is given by the rank-one perturbation

$$
E _ { 0 } = \bar { r } \bar { x } ^ { T } / \| \bar { x } \| _ { 2 } ^ { 2 } = \bar { r } \bar { x } ^ { \dag } , \quad \bar { r } = b - A \bar { x } .
$$

Furthermore, $\| E _ { 0 } \| _ { 2 } = \| E _ { 0 } \| _ { F } = \| { \bar { r } } \| _ { 2 } / \| { \bar { x } } \| _ { 2 }$

Finding the optimal backward error for a general least squares problem is more difficult. Stewart [1018,1977,Theorem 3.1] gives two simple upper bounds for $\mu ( \bar { x } )$

Theorem 2.5.2. Let x be an approximate solution to the least squares problem $\operatorname* { m i n } _ { x }$ $\| A x - b \| _ { 2 }$ Assume that the corresponding residual $\bar { r } = b - A \bar { x } \neq 0$ Then $\bar { x }$ exactly solves $\operatorname* { m i n } _ { x } \| b - ( A +$ $E _ { i } ) x \| _ { 2 }$ ,where

$$
E _ { 1 } = \frac { ( \bar { r } - r ) \bar { x } ^ { T } } { \| \bar { x } \| _ { 2 } ^ { 2 } } , \qquad E _ { 2 } = - \frac { \bar { r } \bar { r } ^ { T } A } { \| \bar { r } \| _ { 2 } ^ { 2 } } = - \bar { r } \bar { r } ^ { \dagger } ,
$$

and $r = b - A x$ is the residual corresponding to the exact solution $x$ The norms of these perturbations are

$$
\| E _ { 1 } \| _ { 2 } = \frac { \sqrt { \| \bar { r } \| _ { 2 } ^ { 2 } - \| r \| _ { 2 } ^ { 2 } } } { \| \bar { x } \| _ { 2 } } \leq \frac { \| \bar { r } \| _ { 2 } } { \| \bar { x } \| _ { 2 } } , \qquad \| E _ { 2 } \| _ { 2 } = \frac { \| A ^ { T } \bar { r } \| _ { 2 } } { \| \bar { r } \| _ { 2 } } .
$$

Proof. The result for $E _ { 2 }$ is proved by showing that $\bar { x }$ satisfies the normal equations $( A + E _ { 2 } ) ^ { T } ( b -$ $( A + E _ { 2 } ) \bar { x } = 0$ . Note that $\bar { r } ^ { \dagger } = \bar { r } ^ { T } / \| \bar { r } \| _ { 2 }$ is the pseudoinverse of $\bar { r }$ and that $\bar { r } \bar { r } ^ { \dagger }$ is an orthogonal projector. From $A + E _ { 2 } = ( I - \bar { r } \bar { r } ^ { \dag } ) A$ and $A { \bar { x } } = b - { \bar { r } }$ ,we obtain

$$
b - ( A + E _ { 2 } ) \bar { x } = b - ( I - \bar { r } \bar { r } ^ { \dagger } ) ( b - \bar { r } ) = \bar { r } \bar { r } ^ { \dagger } b .
$$

Hence the normal equations become $A ^ { T } ( I - \bar { r } \bar { r } ^ { \dagger } ) \bar { r } \bar { r } ^ { \dagger } b = 0$ .The proof for $E _ { 1 }$ may be found in Stewart [1017,1977,Theorem 5.3]. □

In Theorem $2 . 5 . 2 \parallel E _ { 1 } \parallel _ { 2 }$ is small when $\bar { r }$ is almost equal to the residual $r$ of the exact solution. $\| E _ { 2 } \| _ { 2 }$ is small when $\bar { r }$ is almost orthogonal to the column space of $A$ .However, these are just upper bounds, and $\mu ( \bar { x } )$ can be much smaller than either $\| E _ { 1 } \| _ { 2 }$ or $\| E _ { 2 } \| _ { 2 }$

An exact expression for $\mu ( \bar { x } )$ was found by Waldén, Karlsson, and Sun [1096,1995] by characterizing the set $\mathcal { E }$ of all possible perturbations $E$ . Their result is summarized in the following theorem; see also Higham [623,2002,pp. 404-405].

Theorem 2.5.3. Let $\bar { r } = b - A \bar { x } \neq 0$ and $\eta = \| \bar { r } \| _ { 2 } / \| \bar { x } \| _ { 2 }$ . Then the optimal backward error in the Frobenius norm is

$$
\mu ( \bar { x } ) \equiv \operatorname* { m i n } _ { E \in \mathcal { E } } \| E \| _ { F } = \operatorname* { m i n } \big ( \eta , \sigma _ { \operatorname* { m i n } } \left( A , B \right) \big ) ,
$$

where $B = \eta ( I - \bar { r } \bar { r } ^ { \dagger } )$

Computing the smallest singular value of the matrix $( A , B ) \in \mathbb { R } ^ { m \times ( m + n }$ is too expensive for most practical purposes. Karlsson and Walden [685,1997] proposed an estimate of $\tilde { \mu }$ that can be computed more cheaply. This makes use of a regularized projection of the residual $\bar { r } = b - A \bar { x }$ The Karlsson-Waldén (KW) estimate can be expressed as $\widetilde { \mu } = \| K y \| _ { 2 } / \| \bar { x } \| _ { 2 }$ , where $y$ solves the least squares problem

$$
\operatorname* { m i n } _ { y } \| K y - v \| _ { 2 } , \quad K = \left( { A \atop \eta I } \right) , \quad v = \left( { \bar { r } } \atop 0 \right) .
$$

If the compact QR factorization of $K = Q R$ of $K$ is known, $\widetilde { \mu } = \| Q ^ { T } v \| _ { 2 } / \| \bar { x } \| _ { 2 }$ can be computed in $O ( m n )$ operations.

Numerical experiments by Grcar, Saunders,and Su [532, 2oo7] indicate that the KW estimate is very near the true optimal backward error and can be used safely in practice. This was confirmed by Gratton, Jiranek,and Titley-Peloquin [528, 2o12], who proved the lower and upper bounds

$$
1 \leq \frac { \mu } { \tilde { \mu } } \leq \sqrt { 2 - \left( \| r \| _ { 2 } / \| \bar { r } \| _ { 2 } \right) } \leq \sqrt { 2 } .
$$

The ratio tends to 1 as $\| { \bar { r } } \| _ { 2 } \to \| r \| _ { 2 }$

The following MATLAB script can be used to compute the KW estimate (2.5.13) by sparse QR factorization without storing $Q$

$$
\begin{array} { l } { { { [ \mathrm { m } , { \bf n } ] } ~ = ~ \mathrm { s i z e } \left( \mathrm { A } \right) ; ~ { \mathrm {  ~ { \vec { r } ~ - ~ \vec { b } ~ - ~ \vec { \cal { A } } * x } ; ~ } } } } \\ { { { \mathrm { n o r m ~ \vec { \mu } ~ - ~ \vec { \mu } ~ n o r m } \left( \mathrm { x } \right) ; ~ \mathrm {  ~ \vec { \Lambda } ~ \ e t a ~ = ~ \ n o r m } \left( \mathrm { r } \right) / \mathrm { n o r m } \ : ; } } } \\ { { { \mathrm {  ~ { \vec { p } ~ - ~ \vec { \mu } ~ n o l d } \left( \mathrm { A } \right) ~ } } ; } } \\  { { \mathrm {  ~ { \vec { \cal { K } } ~ - ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \nu } ~ \ e t a ^ { * } \mathrm { s g e y e y e } \left( n \right) } { \mathrm {  ~ { \vec { \mu } ~ \cdot ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ } } } } } } \\  { { \mathrm {  ~ { \vec { \nu } ~ - ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \mu } ~ \ z e r o s } \left( \mathrm { n } , 1 \right) } { \mathrm {  ~ { \vec { \mu } ~ \cdot ~ \vec { \nu } ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ \ \vec { \nu } ~ \ \vec { \mu } ~ \vec { \nu } ~ } } } } } \\  { { { \mathrm { [ \vec { \Lambda } ~ \vec { \mu } ~ \mathrm { , ~ \vec { \nu } ~ \vec { \mu } ~ \vec { \nu } ~ \vec { \mu } ~ = ~ \ n o r m } \left( \mathrm { c } \right) / \mathrm { n o r m } \ : } } } } \end{array}
$$

Methods for computing the KW estimate are given by Malyshev and Sadkane [770, 2001]. Optimal backward error bounds for problems with multiple right-hand sides are given by Sun [1050,1996],while bounds for underdetermined systems are derived in Sun and Sun [1051, 1997].The extension of backward error bounds to constrained least squares problems is discussed by Cox and Higham [271,1999].

The optimal componentwise backward error of $\bar { x }$ is the smallest $\omega \ge 0$ such that $\bar { x }$ exactly minimizes $\| ( A + E ) \bar { x } - ( b + f ) \| _ { 2 }$ ,and

$$
| E | \leq \omega | A | , \quad | f | \leq \omega | b | ,
$$

where the inequalities are to be interpreted componentwise. For a consistent linear system $b \in$ $\mathcal { R } ( A )$ , Oettli and Prager [835,1964] proved the explicit expression

$$
\omega = \operatorname* { m a x } _ { 1 \leq i \leq n } \frac { \lvert A \bar { x } - b \rvert _ { i } } { ( \lvert A \rvert \lvert \bar { x } \rvert + \lvert b \rvert ) _ { i } } .
$$

Here $0 / 0$ should be interpreted as O,and $\zeta / 0$ $\zeta \neq 0 ,$ ）as infinity. (The latter case means that no finite $\omega$ satisfying (2.5.16) exists.) Together with the perturbation result (1.3.49), (2.5.16) can be used to compute an a posteriori bound on the error in a given approximate solution $\bar { x }$

In Section 1.3.4 we obtained perturbation bounds for the least squares problem subject to componentwise perturbations. However, no expression for the optimal componentwise backward error is known. Following Bjorck [132,1991],we apply the Oettli-Prager bound to the augmented system(1.1.19),where no perturbations in the diagonal blocks of $M$ or in the zero vector in the right-hand side are allowed. However, we allow for different perturbations of the blocks $A$ and $A ^ { T }$ ,as this does not increase the forward error bounds (1.3.55) and (1.3.56).

Hence for an a posteriori error analysis, it makes sense to define the pseudocomponentwise backward error of a computed solution ${ \bar { x } } , { \bar { r } }$ to be the smallest nonnegative number $\omega$ such that

$$
| \delta A _ { i } | \le \omega | A | , \quad i = 1 , 2 , \qquad | \delta b | \le \omega | b | ,
$$

and

$$
\left( { \cal I } _ { { \cal A } ^ { T } + \delta { \cal A } _ { 2 } } \right. \left. \begin{array} { c } { { A + \delta { \cal A } _ { 1 } } } \\ { { 0 } } \end{array} \right) \left( \begin{array} { c } { { \bar { r } } } \\ { { \bar { x } } } \end{array} \right) = \left( \begin{array} { c } { { b + \delta b } } \\ { { 0 } } \end{array} \right) .
$$

Note that this allows the two blocks of $A$ in the augmented system to be perturbed differently and hence does not directly correspond to perturbing the data of the least squares problem. From the result of Oettli and Prager, this backward error for a computed solution $\bar { r }$ and $\bar { x }$ becomes $\omega ( \bar { r } , \bar { x } ) = \operatorname* { m a x } ( \omega _ { 1 } , \omega _ { 2 } )$ ,where

$$
\omega _ { 1 } = \operatorname* { m a x } _ { 1 \leq i \leq m } \frac { | b - ( \bar { r } + A \bar { x } ) | _ { i } } { ( | A | | \bar { x } | + | b | ) _ { i } } , \quad \omega _ { 2 } = \operatorname* { m a x } _ { 1 \leq i \leq n } \frac { | A ^ { T } \bar { r } | _ { i } } { ( | A ^ { T } | | \bar { r } | ) _ { i } } .
$$

If we only have a computed $\bar { x }$ ,it may be feasible to define ${ \bar { r } } = b - A { \bar { x } }$ and apply the result above.With this choice we have $\omega _ { 1 } = 0$ (exactly),and hence

$$
\omega ( \bar { r } , \bar { x } ) = \omega _ { 2 } = \operatorname* { m a x } _ { 1 \leq i \leq n } \frac { \vert A ^ { T } ( b - A \bar { x } ) \vert _ { i } } { ( \vert A ^ { T } \vert \vert b - A \bar { x } \vert ) _ { i } } .
$$

If the columns of $A$ and $b$ are scaled, the class of perturbations scales in the same way. Hence $\omega$ is invariant under row and column scaling of $A$ .A bound for the forward error $\| { \bar { x } } - x \| _ { 2 }$ can be obtained in terms of $\omega$ ,which potentially is much smaller than the standard forward error bound involving $\kappa _ { 2 } ( A )$

In the case of a nearly consistent least squares problem, $f l ( b - A { \bar { x } } )$ will mainly consist of roundoff and will not be accurately orthogonal to the range of $A$ .Hence although $\bar { x }$ may have a small relative backward error, $\omega _ { 2 }$ may not be small. This illustrates a fundamental problem in computing the backward error: for $\bar { x }$ to have a small backward error it is sufficient that either $( b - A { \bar { x } } )$ or $A ^ { T } ( b - A { \bar { x } } )$ is small, but neither of these conditions is necessary.

# 2.5.3 - Iterative Refinement

Mixed-precision iterative refinement (IR) is a process used for improving the accuracy of a given approximate solution $x$ to a linear system $A x = b$ .Typically the initial approximation is computed using an LU factorization of $A$ computed in working precision of $A$ .Next the residual $b - A x$ is computed in a higher precision, the correction equation $A d = r$ is solved, and an updated solution $x + d$ is formed.If necessary, the refinement step is repeated. In classical mixed-precision IR,arithmetic in two different precisions is: the working precision $\mathbf { u } _ { 1 }$ ,in which the data and solution are stored,and a higher precision $\mathbf { u } _ { 2 } \leq \mathbf { u } _ { 1 }$ used for computing residuals.

# Algorithm 2.5.2 (Iterative Refinement).

Solve $A x _ { 0 } = b$ in precision $\mathbf { u } _ { 1 }$ using some factorization of $A$

for s = 0,1,2,...,compute $r _ { s } = b - A x _ { s }$ ； in precision $\mathbf { u } _ { 2 }$ round $r _ { s }$ to precision $\mathbf { u } _ { 1 }$ solve $A \delta x _ { s } = r _ { s }$ ； in precision u1$x _ { s + 1 } = x _ { s } + \delta x _ { s }$ ； in precision u1  
end;

The process is stopped when $\delta x _ { s } / \| x _ { s } \|$ no longer shows a steady decrease.

The factorization of $A$ used for computing the initial approximation can also be used for solving the correction equations.Therefore the cost of each refinement step is quite small. Note that while the computed solution initially improves with each iteration, this is usually not reflected in a corresponding decrease in the norm of the residual, which typically stays about the same.

On many early computers,inner products could be cheaply accumulated at twice the working precision,and IR was used with $\mathbf { u } _ { 2 } = \mathbf { u } _ { 1 } ^ { 2 }$ . This traditional version of IR was analyzed for fixedpoint arithmetic by Wilkinson [1118,1963] and for floating-point arithmetic by Moler [799, 1967].A more recent error analysis is found in Higham [623, 2Oo2, Chapter 12]. As long as $A$ is not too ill-conditioned so that the initial solution has a relative error $\| x - x _ { 0 } \| / \| x _ { 0 } \| = \eta$ ， $\eta < 1$ ， IR behaves roughly as follows. The relative error is decreased by a factor of about $\eta$ with each step of refinement until a stage is reached at which the solution is correct to working precision u.

Since most problems involve inexact input data, obtaining a highly accurate solution may not seem to be justified. Even so,IR offers a useful estimate of the accuracy and reliability of a computed solution. The correction $\delta _ { 1 }$ also gives a good estimate of the sensitivity of the solution to small relative perturbations of order u in the data $A$ and $b$ .Furthermore,there are applications where an accurate solution of very ill-conditioned equations is warranted; see Ma et al.[765, 2017].

Mixed-precision IR was first applied to least squares problems by Businger and Golub [193, 1965]. In their algorithm the QR factorization of $A$ is used to compute $x _ { 0 }$ and solve for the corrections $\delta { x _ { s } }$ . The iterations proceeds as follows.

f $\begin{array} { r } { \begin{array} { r l } & { \mathrm { o r } s = 0 , 1 , 2 , . . . } \\ & { \mathrm { c o m p u t e } r _ { s } = b - A x _ { s } ; \mathrm { i n p r e c i s i o n } { \bf u } _ { 2 } . } \\ & { \mathrm { s o l v e } \displaystyle \operatorname* { m i n } _ { \delta x _ { s } } \| A \delta x _ { s } - r _ { s } \| _ { 2 } ; \mathrm { i n p r e c i s i o n } { \bf u } _ { 1 } . } \\ & { \left. x _ { s + 1 } = x _ { s } + \delta x _ { s } ; \mathrm { i n p r e c i s i o n } { \bf u } _ { 1 } . \right. } \end{array} } \end{array}$ end

This works well for small-residual problems, but otherwise it may fail to give solutions correct to working precision.

To remedy this it is necessary to simultaneously refine both the solution $x$ and the residual $r$ by applying IR to the augmented system for the least squares problem. Let $x _ { s }$ and $r _ { s }$ be the current approximations. In Bjorck [124,1967] the new approximations are taken to be

$$
x _ { s + 1 } = x _ { s } + \delta x _ { s } , \qquad r _ { s + 1 } = r _ { s } + \delta r _ { s } ,
$$

where the corrections are computed in precision $\mathbf { u } _ { 1 }$ from the augmented system

$$
\left( \begin{array} { c c } { { I } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { \delta r _ { s } } } \\ { { \delta x _ { s } } } \end{array} \right) = \left( \begin{array} { c } { { f _ { s } } } \\ { { g _ { s } } } \end{array} \right) .
$$

Here the residuals

$$
f _ { s } = b - r _ { s } - A x _ { s } , \qquad g _ { s } = - A ^ { T } r _ { s }
$$

are computed in precision $\mathbf { u } _ { 2 }$ and rounded to precision $\mathbf { u } _ { 1 }$ . The system (2.5.19) can be solved stably using Algorithm 2.2.6:

$$
\begin{array} { r l } & { z _ { s } = R ^ { - T } g _ { s } , \qquad \left( \begin{array} { l } { d _ { s } } \\ { e _ { s } } \end{array} \right) = Q ^ { T } f _ { s } , } \\ & { \delta r _ { s } = Q \left( \begin{array} { l } { z _ { s } } \\ { e _ { s } } \end{array} \right) , \qquad \delta x _ { s } = R ^ { - 1 } ( d _ { s } - z _ { s } ) . } \end{array}
$$

Alternatively,an MGS QR factorization and Algorithm 2.2.12 can be used.An implementation that uses Householder QR is given by Bjorck and Golub [143,1967].

# Algorithm 2.5.3 (IR of Augmented System Solution).

$$
\mathrm { s e t } \ x _ { 0 } = 0 ; \ r _ { 0 } = 0 ;
$$

$$
\begin{array} { r l } & { f _ { s } = b - r _ { s } - A x _ { s } ; ~ g _ { s } = c - A ^ { T } r _ { s } ; ~ \mathrm { i n } \mathrm { p r e c i s i o n } \mathrm { \bf u } _ { 2 } } \\ & { \mathrm { s o l v e } \mathrm { f o r } \delta r _ { s } , \delta x _ { s } ; ~ \mathrm { i n } \mathrm { p r e c i s i o n } \mathrm { \bf u } _ { 1 } } \\ & { x _ { s + 1 } = x _ { s } + \delta x _ { s } ; } \\ & { r _ { s + 1 } = r _ { s } + \delta r _ { s } ; } \end{array}
$$

end

This algorithm requires $8 m n - 2 n ^ { 2 }$ flops in working precision for computing the QR factorization. Computing the residual takes 4mn flops in extended precision. The initial rate of convergence can be shown to be linear with rate

$$
\rho = c _ { 1 } \mathbf { u } \kappa ^ { \prime } , \quad \kappa ^ { \prime } = \operatorname* { m i n } _ { D > 0 } \kappa _ { 2 } ( A D ) ,
$$

where $c _ { 1 }$ is of modest size. Note that this rate is achieved without actually carrying out the scaling of $A$ by the optimal $D$ . This rate is similar to that for the linear system case,even though the conditioning of the least squares problem includes a term proportional to $\kappa ^ { 2 } ( A )$ for large-residual problems.

Example 2.5.4 (See Bjorck and Golub [143,1967l). To illustrate the method of iterative refinement we consider the linear least squares problem where $A$ is the last six columns of the inverse of the Hilbert matrix $H _ { 8 } \in R ^ { 8 \times 8 }$ , which has elements

$$
h _ { i j } = 1 / ( i + j - 1 ) , \quad 1 \leq i , j \leq 8 .
$$

Two right-hand sides $b _ { 1 }$ and $b _ { 2 }$ are chosen so that the exact solution is

$$
x = ( 1 / 3 , 1 / 4 , 1 / 5 , 1 / 6 , 1 / 7 , 1 / 8 ) ^ { T } .
$$

For $b = b _ { 1 }$ the system $A x = b$ is consistent; for $b = b _ { 2 }$ the norm of the residual $r = b - A x$ is $1 . 0 4 \cdot 1 0 ^ { 7 }$ . Hence, for $b _ { 2 }$ the term proportional to $\kappa ^ { 2 } ( A )$ in the perturbation bound dominates.

The refinement algorithm was run on a computer with a single precision unit roundoff ${ \bf u } =$ $1 . 4 6 \cdot 1 0 ^ { - 1 1 }$ . The correction equation was solved using Householder QR factorization. Double precision accumulation of inner products was used for calculating the residuals,but otherwise all computations were performed in single precision.We give below the first component of the successive approximations $x ^ { ( s ) } , r ^ { ( s ) } s = \bar { 1 } , \bar { 2 } , 3 , \ldots ,$ for right-hand sides $b _ { 1 }$ (left) and $b _ { 2 }$ (right).

$$
\begin{array} { r l r } { x _ { 1 } ^ { ( s ) } = } & { 3 . 3 3 3 2 3 2 5 2 6 9 \cdot 1 0 ^ { - 1 } } & { x _ { 1 } ^ { ( s ) } = } & { 5 . 5 6 2 3 9 0 1 5 4 7 \cdot 1 0 ^ { + 1 } } \\ & { 3 . 3 3 3 3 3 3 3 3 5 2 4 7 \cdot 1 0 ^ { - 1 } } & { 3 . 3 7 7 7 7 1 8 0 6 0 \cdot 1 0 ^ { - 1 } } \\ & { 3 . 3 3 3 3 3 3 3 3 3 3 4 \cdot 1 0 ^ { - 1 } } & { 3 . 3 3 3 1 1 5 7 9 0 8 \cdot 1 0 ^ { - 1 } } \\ & { 3 . 3 3 3 3 3 3 3 3 3 3 3 4 \cdot 1 0 ^ { - 1 } } & { 3 . 3 3 3 3 3 3 3 3 3 1 7 \cdot 1 0 ^ { - 1 } } \\ { r _ { 1 } ^ { ( s ) } = } & { 9 . 3 2 6 2 6 2 4 3 0 3 \cdot 1 0 ^ { - 5 } } & { r _ { 1 } ^ { ( s ) } = } & { 2 . 8 0 1 3 0 ~ 6 8 8 6 4 \cdot 1 0 ^ { 6 } } \\ & { 5 . 0 5 1 1 4 0 3 4 1 6 \cdot 1 0 ^ { - 7 } } & { 2 . 7 9 9 9 9 9 9 8 2 4 8 \cdot 1 0 ^ { 6 } } \\ & { 3 . 6 5 2 1 7 7 1 7 1 8 \cdot 1 0 ^ { - 1 1 } } & { 2 . 7 9 9 9 9 9 9 5 \cdot 1 0 ^ { 6 } } \\ & { - 1 . 9 5 3 0 0 7 0 1 7 4 \cdot 1 0 ^ { - 1 3 } } & { 2 . 8 0 0 0 0 0 0 0 0 0 0 \cdot 1 0 ^ { 6 } } \end{array}
$$

A gain of almost three digits accuracy per step in the approximations to $x _ { 1 }$ and $r _ { 1 }$ is achieved for both right-hand sides $b _ { 1 }$ and $b _ { 2 }$ . This is consistent with the estimate (2.5.22) because

$$
\kappa ( A ) = 5 . 0 3 \cdot 1 0 ^ { 8 } , \quad u \kappa ( A ) = 5 . 8 4 \cdot 1 0 ^ { - 3 } .
$$

For the right-hand side $b _ { 1 }$ the approximation $x _ { 1 } ^ { ( 4 ) }$ is correct tofullfxed precisn.Itistin to note that for the right-hand side $b _ { 2 }$ the effect of the error term proportional to $u \kappa ^ { 2 } ( A )$ is evident in that the computed solution $x _ { 1 } ^ { ( 1 ) }$ is in error by a factr of $1 0 ^ { 3 }$ .However, $x _ { 1 } ^ { ( 4 ) }$ has eight correct digits, and $r _ { 1 } ^ { ( 4 ) }$ is close to the true value $2 . 8 \cdot 1 0 ^ { 6 }$

Wampler [1099,1979] gives two Fortran subroutines L2A and L2B using MGS with iterative refinement for solving weighted least squares problems. These are based on the ALGOL programs in Bjorck [126,1968] and were found to provide the best accuracy in a comparative evaluation at the National Bureau of Standards; see Wampler [1098,197o]. Demmel et al. [308, 2009] developed a portable and parallel implementation of the Bjorck-Golub IR algorithm for least squares solutions that uses extended precision.

Most descriptions of IR stress the importance of computing the residuals in higher precision. However, fixed-precision IR with residuals computed in working precision ( $\mathbf { u } _ { 2 } = \mathbf { u } _ { 1 } $ ）can also be beneficial. Jankowski and Wozniakowksi [663,1977] show that any linear equation solver can be made backward stable by IR in fixed precision as long as the solver is not too unstable and $A$ not too ill-conditioned. If the product of cond $( A ) = \parallel | A ^ { - 1 } | | A | \parallel _ { 2 }$ and the measure of ill-scaling

$$
\sigma ( A , x ) = { \frac { \operatorname* { m a x } _ { i } ( | A | | x | ) _ { i } } { \operatorname* { m i n } _ { i } ( | A | | x | ) _ { i } } }
$$

is not too large,Skeel [1Oo0l,198o] proves that LU factorization with partial pivoting combined with one step of fixed-precision IR becomes stable in a strong sense. Higham [618,1991] extends Skeel's analysis to show that for any solver that is not too unstable,one step of fixed-precision IR suffices to achieve a solution with a componentwise relative backward error $\omega < \gamma _ { n + 1 } \mathbf { u } _ { 1 }$ .In particular, this result applies to solving linear systems by QR factorization.

Higham [618,1991] studies fixed-precision IR for linear systems and least squares problems of QR factorization methods.He shows that the componentwise backward error $\omega ( \bar { r } , \bar { x } ) =$ $\operatorname* { m a x } ( \omega _ { 1 } , \omega _ { 2 } )$ in (2.5.18) eventually becomes small,although it may take more than one iteration. In particular, IR mitigates the effect of poor row scaling.

If $f _ { s }$ and $g _ { s }$ in Algorithm 2.5.3 are evaluated in precision $\mathbf { u } _ { 1 }$ ， then the resulting roundoff errors become more important.A standard backward error analysis shows that

$$
\bar { f } = b - \delta b - ( A + \delta A _ { 1 } ) \bar { x } - ( I + \delta I ) \bar { r } , \qquad \bar { g } = - ( A + \delta A _ { 2 } ) ^ { T } \bar { r } ,
$$

where $\delta I$ is diagonal. Hence, the roundoff errors are equivalent to small componentwise perturbations in the nonzero blocks of the augmented matrix,

$$
\begin{array} { r l } & { | \delta A _ { 1 } | \le 1 . 0 6 ( n + 3 ) \mathbf { u } | A | , \quad | \delta b | \le 1 . 0 6 \mathbf { u } | b | , } \\ & { | \delta A _ { 2 } | \le 1 . 0 6 ( m + 2 ) \mathbf { u } | A | , \quad | \delta I | \le \mathbf { u } I , } \end{array}
$$

where the inequalities are to be interpreted componentwise. It follows that the computed residuals $\bar { f }$ and $\bar { g }$ are the exact residuals corresponding to the perturbed system

$$
\left( \begin{array} { c } { \bar { f } } \\ { \bar { g } } \end{array} \right) = \left( \begin{array} { c } { b + \delta b } \\ { 0 } \end{array} \right) - \left( \begin{array} { c c } { I + \delta I } & { A + \delta A _ { 1 } } \\ { ( A + \delta A _ { 2 } ) ^ { T } } & { 0 } \end{array} \right) \left( \begin{array} { c } { \bar { r } } \\ { \bar { x } } \end{array} \right) ,
$$

where the perturbations satisfy the componentwise bounds derived above. A perturbation $\lvert \delta I \rvert$ can be considered as a small perturbation in the weights of the rows of $A x - b$ .Roundoff errors also occur in solving equations (2.5.20-(2.5.21). However, if the refinement converges,then the roundoff errors in the solution of the final corrections are negligible.

Recently, graphics processing units (GPUs) have been introduced that perform extremely fast half precision matrix-matrix multiplication accumulated in single IEEE half precision format (see Section 1.4). This has caused a renewed interest in multiprecision algorithms for applications such as weather forecasting and machine learning. A survey of linear algebra in mixed precision is given by Higham and Mary [627, 2022].

Carson and Higham [2O9,2o18] develop a three-precision iterative refinement algorithm for solving linear equations.This uses a complete LU factorization in half IEEE precision $( \mathbf { u } = 4 . 9 \times$ $1 0 ^ { - 4 } )$ , single precision as working precision,and double precision for computing residuals. The remaining computations are performed in working precision, and allresults are stored in working precision. A rounding error analysis shows that this obtains fullsingle-precision accuracy as long as $\kappa ( A ) \leq 1 0 ^ { 4 }$ . With lower working precision the likelihood increases that the system being solved is too il-conditioned.The authors show that in these cases an improvement is obtained by using a two-stage iterative refinement approach where the correction equation is solved by GMRES preconditioned by LU factorization (see Section 6.4.5). For the resulting GMRES-IR algorithm the above condition can be weakened to $\kappa ( A ) \leq 1 0 ^ { 8 }$

Carson,Higham,and Pranesh [210, 2o2o] develop an analogous three-precision iterative refinement algorithm called GMRES-LSIR for least squares problems. It uses the QR factorization of $A$ computed in half IEEE precision. The correction is solved by GMRES applied to the augmented system using a preconditioner based on Algorithm 2.2.6 and the computed QR factor-ization. For a wide range of problems this yields backward and forward errors for the augmented system correct to working precision.

# Notes and references

Kielbasinski [693,1981] studies a version of IR with variable precision called binary-cascade IR (BCIR) in which several steps of IR are performed for solving a linear system with prescribed relative accuracy. At each step the process uses the lowest sufficient precision for evaluating the residuals.A BCIR process for solving least squares problems is developed by Gluchowska and Smoktunowicz [481,199o]. Iterative refinement of solutions has many applications to sparse linear systems and sparse least squares problems. Arioli, Demmel,and Duff [33,1989] adapt Skeel's analysis of fixed-precision IR to the problem of solving sparse linear systems with sparse backward error. The use of a fixed-precision IR for sparse least squares problems is studied by Arioli,Duff,and de Rijk [36,198g]. They note that IR can regain a loss of accuracy caused by bad scaling of the augmented system.

# 2.5.4 - The Corrected Seminormal Equations

The seminormal equations (SNE) for the least squares problem $\operatorname* { m i n } _ { x } \| A x - b \| _ { 2 }$ are

$$
\begin{array} { r } { R ^ { T } R x = c , \quad c = A ^ { T } b . } \end{array}
$$

In floating-point arithmetic the roundoff errors in computing $c$ can be bounded by $\| \delta c \| _ { 2 } ~ \leq$ $m \mathbf { u } \| A \| _ { 2 } \| b \| _ { 2 }$ .The error leads to a resulting perturbation $\delta x$ in the solution of (2.5.26) such that

$$
\begin{array} { r } { \| \delta \boldsymbol { x } \| _ { 2 } \leq m \mathbf { u } \kappa ( \boldsymbol { A } ) ^ { 2 } \| \boldsymbol { b } \| _ { 2 } / \| \boldsymbol { A } \| _ { 2 } . } \end{array}
$$

It will be of similar size whether $R$ comes from a QR factorization of $A$ or from a Cholesky factorization of $A ^ { T } A$ .This error term can be damped by performing a few steps of IR in fixed precision:

# Algorithm 2.5.4 (IR for Seminormal Equations).

$$
\begin{array} { r l } & { r _ { s } = b - A x _ { s } , } \\ & { \mathrm { s o l v e } \ R ^ { T } ( R \delta x _ { s } ) = A ^ { T } r _ { s } , } \\ & { x _ { s + 1 } = x _ { s } + \delta x _ { s } . } \end{array}
$$

end

Each step of refinement requires matrix-vector multiplication with $A$ and $A ^ { T }$ and the solution of two triangular systems.With $R$ from a QR factorization the convergence of this iteration is linear with a rate that can be shown to be approximately

$$
\rho = c u \kappa ^ { \prime } ( A ) , \quad \kappa ^ { \prime } = \operatorname* { m i n } _ { D > 0 } \kappa ( A D ) ;
$$

see Bjorck [130,1987]. Note that this holds without actually performing the optimum column scaling. When $R$ comes from a Cholesky factorization the rate achieved is much worse: only $\bar { \rho } = c u \kappa ^ { \prime } ( A ) ^ { 2 }$ . Even then, a good final accuracy can be achieved for a large class of problems by performing several steps of IR.

In the method of corrected seminormal equations (CSNE),a corrected solution $x _ { c }$ is computed by doing just one step of refinement of the SNE solution $\bar { x }$ : Compute the residual $\bar { r } = f l ( b - A \bar { x } )$ and solve

$$
\begin{array} { r } { R ^ { T } R \delta x = A ^ { T } \bar { r } , \quad x _ { c } = \bar { x } + \delta x . } \end{array}
$$

Assuming that $R$ comes from a backward stable Householder QR or MGS factorization, the computed $R$ is the exact $R$ -factor of a perturbed matrix,

$$
A + E , \quad \| E \| _ { F } \leq c _ { 1 } \mathbf { u } \| A \| _ { F } ,
$$

where $c _ { 1 }$ is a small constant depending on $m$ and $n$ . From this property the following error bound for the corrected solution $x _ { c }$ can be shown; see Bjorck [130,1987, Theorem 3.2].

Theorem 2.5.5. Let $\hat { x } _ { c }$ be the computed CSNE solution using $R$ from Householder QR or MGS of $A$ f $\rho \equiv c _ { 1 } n ^ { 1 / 2 } { \bf u } \kappa ( A ) < 1$ ，then neglecting higher order terms in $\mathbf { u } \kappa ( A )$ ， the following error estimate holds:

$$
\| x - \bar { x } _ { c } \| _ { 2 } \leq m n ^ { 1 / 2 } \mathbf { u } \kappa \bigg ( \| x \| _ { 2 } + \kappa \frac { \| r \| _ { 2 } } { \| A \| _ { 2 } } \bigg ) + \sigma \mathbf { u } \kappa \bigg ( c _ { 2 } \| x \| _ { 2 } + n ^ { 1 / 2 } m \frac { \| b \| _ { 2 } } { \| A \| _ { 2 } } \bigg ) ,
$$

where $\kappa = \kappa ( A )$ ， $\boldsymbol { \sigma } = c _ { 3 } \mathbf { u } \kappa \boldsymbol { \kappa } ^ { \prime }$ ， $c _ { 3 } \leq 2 n ^ { 1 / 2 } ( c _ { 1 } + 2 n + m / 2 )$ ,and $c _ { 1 }$ and $c _ { 2 }$ are small constants depending on $m$ and $n$

If $\sigma = c _ { 3 } \mathbf { u } \kappa \kappa ^ { \prime } < 1$ ,the error bound for the CSNE solution is no worse than the error bound for a backward stable method. This condition is usually satisfied in practical applications and is roughly equivalent to requiring that $\bar { x }$ from the seminormal equation have at least one correct digit.

An important application of CSNE is to sparse least squares problems. In the QR factorization of a sparse matrix $A$ ,the factor $Q$ often can be much less sparse that the factor $R$ ； see Gilbert, $\mathrm { N g }$ ,and Peyton [470,1997]. Therefore $Q$ is not saved, which creates a difficulty if additional right-hand sides $b$ have to be treated. With CSNE,recomputing the QR factorization can be avoided.

Example 2.5.6. Consider a sequence of least squares problems constructed as follows. Let $A$ be the first five columns of the inverse Hilbert matrix $H _ { 6 } ^ { - 1 }$ of order six. This matrix is moderately ill-conditioned: $\kappa _ { 2 } ( A ) = 4 . 7 0 \times 1 0 ^ { 6 }$ Let $x = ( 1 , \bar { 1 } / 2 , 1 / 3 , 1 / 4 , 1 / 5 ) ^ { T }$ ,and let $b = A x$ be a consistent right-hand side.Let $h$ satisfy $A ^ { T } h = 0$ and $\kappa _ { 2 } ( A ) \| h \| _ { 2 } / ( \| A \| _ { 2 } \| x \| _ { 2 } ) = 3 . 7 2 \times 1 0 ^ { 3 }$ Consider a sequence of right-hand sides $A x + 1 0 ^ { k } h$ ， $k = 0 , 1 , 2$ ,with increasing residual norm. For these problems it holds that $\sigma = c _ { 3 } \mathbf { u } \kappa \kappa ^ { \prime } \ll 1$

Table 2.5.1 shows the average number of correct significant decimal digits of four solution methods: Normal equations (NE), SNE, QR,and CSNE. As predicted by the error analysis, SNE gives only about the same accuracy as NE. On the other hand, CSNE is better than QR.

Table 2.5.1. Average number of correct significant decimal digits.   

<table><tr><td>Right-hand side</td><td>NE</td><td>SNE</td><td>QR</td><td>CSNE</td></tr><tr><td>b</td><td>3.541</td><td>3.308</td><td>6.208</td><td>7.744</td></tr><tr><td>b+h</td><td>3.423</td><td>4.801</td><td>6.232</td><td>8.103</td></tr><tr><td>b+10h</td><td>4.357</td><td>3.797</td><td>6.567</td><td>7.861</td></tr><tr><td>b+100h</td><td>4.575</td><td>4.241</td><td>5.142</td><td>5.814</td></tr></table>

For more ill-conditioned problems, several refinement steps may be needed. Let $x _ { p }$ be the computed solution after $p$ refinement steps.With $R$ from QR the error initially behaves as $\lVert x -$ $x _ { s } \| \sim c _ { 1 } u \kappa \kappa ^ { \prime } ( c _ { 1 } \mathbf { u } \kappa ^ { \prime } ) ^ { p }$ If $c _ { 1 } \approx 1$ and $\kappa ^ { \prime } = \kappa$ ,an acceptable-error stable level is achieved in $p$ steps if κ(A) <u-p/(p+1).

# 2.6 - Blocked Algorithms and Subroutine Libraries

# 2.6.1- Blocked QR Factorization

A key strategy for obtaining high performance in new algorithms is to group together and reorder scalar and matrix-vector operations into matrix-matrix operations.Such blocked algorithms have the same stability properties as their scalar counterparts but reduced communication. Consider Householder QR of the partitioned matrix $A = \left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right) \in \mathbb { R } ^ { m \times n }$ ，where $A _ { 1 } \in \mathbb { R } ^ { m \times n _ { 1 } }$ .In the first step we compute

$$
A _ { 1 } = Q _ { 1 } \left( \binom { R _ { 1 1 } } { 0 } , \quad Q _ { 1 } = P _ { 1 } P _ { 2 } \cdot \cdot \cdot P _ { n _ { 1 } } \in \mathbb { R } ^ { m \times m } , \right.
$$

where $P _ { i } = I - \tau _ { i } u _ { i } u _ { i } ^ { T }$ ， $i = 1 , \ldots , n _ { 1 }$ ,are Householder reflections. Next, these transformations are applied to the trailing matrix $A _ { 2 } \in \mathbb { R } ^ { m \times n _ { 2 } }$ ：

$$
\begin{array} { r l r } { Q _ { 1 } ^ { T } A _ { 2 } = \left( { R } _ { 1 2 } \right) , } & { { } } & { Q _ { 1 } ^ { T } = P _ { n _ { 1 } } \cdot \cdot \cdot P _ { 2 } P _ { 1 } . } \end{array}
$$

To achieve beter performance, this sequence of rank-one updates can be aggregated into one update of rank $p$

A stable compact representation of a product of Householder matrices is given by Bischof and Van Loan [123,1987]. Here we describe a more storage-efficient version due to Schreiber and Van Loan [975,1989]. Let

$$
Q _ { i } = I - U _ { i } T _ { i } U _ { i } ^ { T } , \quad i = 1 , 2 ,
$$

where $U _ { i } \in \mathbb { R } ^ { m \times n _ { i } }$ and $T _ { i } \in \mathbb { R } ^ { n _ { i } \times n _ { i } }$ are upper triangular. Then $Q = Q _ { 1 } Q _ { 2 } = ( I - U T U ^ { T } )$ ， where

$$
U = \left( U _ { 1 } \quad U _ { 2 } \right) , \qquad T = \left( \begin{array} { c c } { { T _ { 1 } } } & { { - T _ { 1 } U _ { 1 } ^ { T } U _ { 2 } T _ { 2 } } } \\ { { 0 } } & { { T _ { 2 } } } \end{array} \right) .
$$

Note that $U$ is formed by concatenation,but forming the off-diagonal block of the upper trian-gular matrix $T$ requires extra operations. In the special case when $n _ { 1 } = k , n _ { 2 } = 1 , U _ { 2 } = u$ and $T _ { 2 } = \tau$ ,(2.6.3) becomes

$$
U = \left( U _ { 1 } \quad u \right) , \qquad T = \left( \begin{array} { c c } { { T _ { 1 } } } & { { - \tau T _ { 1 } ( U _ { 1 } ^ { T } u ) } } \\ { { 0 } } & { { \tau } } \end{array} \right) .
$$

The blocked Householder QR algorithm of $A \ = \ ( A _ { 1 } \ A _ { 2 } )$ starts by computing the QR factorization of $A _ { 1 } \in \mathbb { R } ^ { m \times n _ { 1 } }$ , where $n _ { 1 } \ll n$ . Starting with $T = \tau _ { 1 }$ ， $U = u _ { 1 }$ and using (2.6.4) recursively, $T _ { n _ { 1 } }$ and $U _ { n _ { 1 } }$ are generated so that

$$
Q _ { 1 } ^ { T } = P _ { n _ { 1 } } \cdot \cdot \cdot P _ { 2 } P _ { 1 } = I - U _ { n _ { 1 } } ^ { T } T _ { n _ { 1 } } ^ { T } U _ { n _ { 1 } } .
$$

This requires about $n _ { 1 } ^ { 2 } ( m + n _ { 1 } / 3 )$ flops. The trailing matrix $A _ { 2 }$ can then be updated by matrixmatrix operations as

$$
\begin{array} { r } { Q _ { 1 } ^ { T } A _ { 2 } = A _ { 2 } - U _ { n _ { 1 } } ( T _ { n _ { 1 } } ^ { T } ( U _ { n _ { 1 } } ^ { T } A _ { 2 } ) ) = { \binom { R _ { 1 2 } } { B } } , \quad R _ { 1 2 } \in \mathbb { R } ^ { n _ { 1 } \times ( n - n _ { 1 } ) } } \end{array}
$$

in about $n _ { 1 } n _ { 2 } ( 2 m + n _ { 1 } )$ flops. Next, $B$ is partitioned as $B = \left( \begin{array} { c c } { B _ { 1 } } & { B _ { 2 } } \end{array} \right)$ .Proceeding as before, the QR factorization $B _ { 1 } = Q _ { 1 } R _ { 2 2 }$ is computed and $B _ { 2 }$ is updated. All remaining steps are similar. The process terminates when the columns of $A$ are exhausted.Note that the size of the successive blocks can be chosen dynamically and need not be fixed in advance. The optimal choice of block sizes depends on characteristics of the computer. This block Householder QR algorithm has the same stability as the scalar algorithm and can be shown to be backward stable.

Consider now a block Householder QR factorization for a fixed uniform partitioning $A =$ $( A _ { 1 } , A _ { 2 } , \ldots , A _ { N } )$ ,where $N = n / p$ For $k = 0 , \ldots , N - 1$ ,do:

1. Compute the Householder QR factorization of a matrix of size $( m - k p ) \times p$

2. Update the upper triangular matrix $T \in \mathbb { R } ^ { k p \times k p }$ in the WY representation.

3. Apply the update to the trailing blocks matrix of size $( m - k p ) \times ( n - k p )$

The QR factorization in step l requires a total of less than $2 N m p ^ { 2 } = 2 m n p$ flops. The operation count of step 2 is of similar magnitude. Since the total number of flops for the Householder QR factorization of $A \in \mathbb { R } ^ { m \times n }$ must be greater than $2 n ^ { 2 } ( m - n / 3 )$ flops, all but a fraction of $n / p = 1 / N$ of the operations are spent in the matrix operations of the updating.

The block Householder QR algorithm described above is right-looking,i.e., in step $k$ the full trailing submatrix of size $( m - k p ) \times ( n - k p )$ is updated. For $p = 1$ it reduces to the standard Householder QR algorithm. The data referenced can instead be reduced by using a left-looking algorithm that in step $k$ applies all previous Householder transformations to the next block of size $( n - k p ) \times p$ of the trailing matrix.

A blocked form of MGS QR can easily be constructed as follws; see Bjorck [134,1994l. Let $A = \left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right)$ and

$$
A _ { 1 } = Q _ { 1 } R _ { 1 1 } \in \mathbb { R } ^ { m \times k } , \quad Q _ { 1 } = ( q _ { 1 } , \dots , q _ { k } ) ,
$$

be the MGS factorization of $A _ { 1 }$ ，where $q _ { i } ^ { T } q _ { j } = 1$ ， $i = j$ . Due to rounding errors, there will be a loss of orthogonality so that $q _ { i } ^ { T } q _ { j } \neq 0$ ， $i \neq j$ . In the next step, the trailing block $A _ { 2 }$ is transformed as

$$
B = P _ { k } ^ { T } A _ { 2 } , \quad P _ { k } = ( I - q _ { 1 } q _ { 1 } ^ { T } ) \cdot \cdot \cdot ( I - q _ { k } q _ { k } ^ { T } ) ,
$$

where $P _ { k }$ is a product of elementary orthogonal projectors. To perform this updating eficiently, $P _ { k }$ can be expressed in the form

$$
P _ { k } = I - Q _ { k } T _ { k } Q _ { k } ^ { T } , \qquad Q _ { k } = ( q _ { 1 } , \dots , q _ { k } ) ,
$$

where $T _ { k } \in \mathbb { R } ^ { k \times k }$ is a unit upper riangular matrix.To form $T _ { k }$ recursively, set $T _ { 1 } = 1 , Q _ { 1 } = q _ { 1 }$ and for $i = 2 , \ldots , k$ ,compute

$$
Q _ { i } = ( Q _ { i - 1 } , q _ { i } ) , \qquad L _ { i } = \left( \begin{array} { c c } { { T _ { i - 1 } } } & { { l _ { i } } } \\ { { 0 } } & { { 1 } } \end{array} \right) , \quad l _ { i } = - T _ { i - 1 } ( Q _ { i - 1 } ^ { T } q _ { i } ) .
$$

The update in (2.6.7) can then be written in terms of matrix operations as

$$
B = ( I - Q _ { k } ^ { T } T _ { k } ^ { T } Q _ { k } ) A _ { 2 } = A _ { 2 } - Q _ { k } ^ { T } ( T _ { k } ^ { T } ( Q _ { k } A _ { 2 } ) ) .
$$

This update requires $2 ( n - k ) k ( m + p / 4 )$ flops. When $k \ll n$ this is the main work in the first step.In the next step, $B$ is partitioned as $B = \left( B _ { 1 } \quad B _ { 2 } \right)$ ,and the MGS QR factorization of $B _ { 1 }$ is computed, etc. The resulting block MGS algorithm has the same stability as the scalar MGS algorithm and can be used to solve least squares problems in a backward stable way.

The following result (Bjorck [125,1967,Lemma 5.1])can be used to improve the effciency of column-oriented MGS orthogonalization.

Lemma 2.6.1. Given $Q _ { k } = ( q _ { 1 } , \ldots , q _ { k } )$ ,with $\| q _ { j } \| _ { 2 } = 1$ $j = 1 , \dots , k ,$ define $\widetilde { Q } _ { k } = ( \widetilde { q } _ { 1 } , \dots , \widetilde { q } _ { k } )$ recursively by $\widetilde { q } _ { 1 } = q _ { 1 }$ ， $\widetilde { q } _ { k } = P _ { k - 1 } q _ { k }$ ， $P _ { k - 1 } = ( \bar { I } - q _ { 1 } q _ { 1 } ^ { T } ) \cdot \cdot \cdot ( I - q _ { k - 1 } q _ { k - 1 } ^ { T } )$ .Then

$$
P _ { k } = I - \widetilde Q _ { k } Q _ { k } ^ { T } , \quad Q _ { k } = \widetilde Q _ { k } ( I + L _ { k } ^ { T } ) ,
$$

where $L _ { k } \in \mathbb { R } ^ { k \times k }$ is a strictly lower triangular corection matrix with elements $l _ { i j } = q _ { i } ^ { T } q _ { j }$ ， $i > j$

Proof. The lemma is trivially true for $k = 1$ . From the definition of $\widetilde { q } _ { k }$ we have

$$
{ P } _ { k } = { P } _ { k - 1 } ( I - q _ { k } q _ { k } ^ { T } ) = { P } _ { k - 1 } - { P } _ { k - 1 } q _ { k } q _ { k } ^ { T } = { P } _ { k - 1 } - \widetilde { q } _ { k } q _ { k } ^ { T } .
$$

Assume that (2.6.11) holds for $k - 1$ . Then $\widetilde { q } _ { k } = \big ( I - \widetilde { Q } _ { k - 1 } Q _ { k - 1 } ^ { T } \big ) q _ { k }$ or, equivalently,

$$
q _ { k } = \widetilde { q } _ { k } + ( q _ { k } ^ { T } q _ { k - 1 } ) \widetilde { q } _ { k - 1 } + \cdot \cdot \cdot + ( q _ { j } ^ { T } q _ { 1 } ) \widetilde { q } _ { 1 } .
$$

But this is the $k$ th column of $Q _ { k } = \widetilde { Q } _ { k } ( I + L _ { k } ^ { T } )$

From Lemma 2.6.1 it follows that

$$
P _ { k } ^ { T } = I - Q _ { k } ( I + L _ { k } ) ^ { - 1 } Q _ { k } ^ { T } .
$$

Hence the orthogonalization of $a _ { k }$ against $q _ { 1 } , \ldots , q _ { k - 1 }$ in MGS can be written as

$$
P _ { k - 1 } ^ { T } a _ { k } = ( I - Q _ { k - 1 } { \widetilde Q } _ { k - 1 } ^ { T } ) a _ { k } , \quad { \widetilde Q } _ { k - 1 } ^ { T } = ( I + L _ { k - 1 } ) ^ { - 1 } Q _ { k - 1 } ^ { T } .
$$

Comparing (2.6.8) and (2.6.13) gives the identity $T _ { k - 1 } = ( I - L _ { k - 1 } ) ^ { - 1 }$ . A similar lower triangular inverse is used by Walker [1097,1988] to obtain a blocked Householder algorithm. A summary of the compact WY and inverse compact WY for Householder and MGS transformations and a version of blocked MGS based on (2.6.13) are given by Swirydowicz et al.[1054, 2020].

Several other block Gram-Schmidt algorithms have been suggested. Jalby and Philippe [662, 1991] study a block Gram-Schmidt algorithm in which MGS is used to orthogonalize inside the blocks,and the trailing matrix is updated as in CGS by multiplication with $( I - Q _ { k } Q _ { k } ^ { T } )$ . The stability of this algorithm is shown to lie between that of MGS and CGS.The computed matrix $\hat { Q }$ satisfies

$$
\| I - \hat { Q } ^ { T } \hat { Q } \| _ { 2 } \leq \rho \mathbf { u } \operatorname* { m a x } _ { k } \kappa ( W _ { k } ) \kappa ( A ) ,
$$

where $W _ { k }$ ， $k = 1 , \ldots , N$ ，are the successive panel matrices. The accuracy can be improved significantly by reorthogonalization of the trailing matrix.

A more challenging problem is the orthogonal basis problem for computing $Q _ { 1 }$ and $R$ that satisfy

$$
\begin{array} { r } { \| I - Q _ { 1 } ^ { T } Q _ { 1 } \| \leq c _ { 1 } ( m , n ) \mathbf { u } , \qquad \| A - Q _ { 1 } R \| \leq c _ { 2 } ( m , n ) \| A \| \mathbf { u } , } \end{array}
$$

where $A \in \mathbb { R } ^ { m \times n }$ ，and $c _ { 1 } ( m , n )$ and $c _ { 2 } ( m , n )$ are modest constants. Stewart [1031, 2008] develops a left-looking Gram-Schmidt algorithm with $A$ partitioned into blocks of columns. Each block is successively orthogonalized and incorporated into $Q$ ．In order to maintai full orthogonality in $Q$ ,reorthogonalization is used in all Gram-Schmidt steps.A feature of the algorithm is that it can handle numerical rank-deficiencies in $A$ ，A similar block algorithm based on CGS2, together with an error analysis that improves some previously given bounds, is given by Barlow and Smoktunowicz [76, 2013].

# Notes and references

Puglisi [906,1992] gives an improved version of the WY representation of products of Householder reflections,which is richer in matrix-matrix operations; see also Joffrain et al. [674, 2006]. Bischof and Quintana-Orti [121,122,1998], use a windowed version of column pivoting aided by an incremental condition estimator (ICE) to develop an efficient block algorithm for computing an RRQR factorization. Columns found to be nearly linearly dependent of previously chosen columns are permuted to the end of the matrix. Numerical tests show that this pivoting strategy usually correctly identifies the rank of $A$ and generates a well-conditioned matrix $R$

Oliveira et al. [842, 2ooo] analyze pipelined implementations of QR factorization using different partitioning schemes, including block and block-cyclic columnwise schemes. A parallel implementation of CGS with reorthogonalization is given by Hernandez,Roman,and Tomas [605,2oo6]. Rounding error analysis of mixed-precision block Householder algorithms is given by Yang,Fox,and Sanders [1138,2o2o]. Carson et al.[211, 2022] survey block Gram-Schmidt algorithms and their stability properties.

# 2.6.2 - Recursive Cholesky and QR Factorization

A special class of block partitioned algorithms uses a recursive blocking. This improves data locality and can execute efciently also on multicore computers. The Cholesky factorization for a symmetric positive definite matrix $A$ partitioned in $2 \times 2$ blocks has the form

$$
\left( \begin{array} { c c } { { A _ { 1 1 } } } & { { A _ { 1 2 } } } \\ { { A _ { 1 2 } ^ { T } } } & { { A _ { 2 2 } } } \end{array} \right) = \left( \begin{array} { c c } { { R _ { 1 1 } ^ { T } } } & { { 0 } } \\ { { R _ { 1 2 } ^ { T } } } & { { R _ { 2 2 } ^ { T } } } \end{array} \right) \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right) ,
$$

where $R _ { 1 1 }$ and $R _ { 2 2 }$ are upper triangular matrices. Equating both sides gives the matrix equations

$$
R _ { 1 1 } ^ { T } R _ { 1 1 } = A _ { 1 1 } , \qquad R _ { 1 1 } ^ { T } R _ { 1 2 } = A _ { 1 2 } , \qquad R _ { 2 2 } ^ { T } R _ { 2 2 } = A _ { 2 2 } - R _ { 1 2 } ^ { T } R _ { 1 2 }
$$

for computing the blocks in $R$ and leads to the following algorithm.

1. Compute the Cholesky factorization $A _ { 1 1 } = R _ { 1 1 } ^ { T } R _ { 1 1 }$   
2. Solve the lower triangular system $R _ { 1 1 } ^ { T } R _ { 1 2 } = A _ { 1 2 }$ for $R _ { 1 2 }$   
3.Form the Schur complement $S _ { 2 2 } = A _ { 2 2 } - R _ { 1 2 } ^ { T } R _ { 1 2 }$ and compute its Cholesky factorization $S _ { 2 2 } = R _ { 2 2 } ^ { T } R _ { 2 2 }$

The Cholesky algorithm in the MATLAB program following computes the two required Cholesky factorizations of size $n _ { 1 } \times n _ { 1 }$ and $n _ { 2 } \times n _ { 2 }$ by recursive calls. The recursion is stopped and a standard Cholesky routine used if $n \leq n m i n$

# Algorithm 2.6.1 (Recursive Cholesky Factorization).

function $\mathrm { ~ L ~ } =$ rchol(C,nmin) $\%$ RCHOL computes the Cholesky factorization $\%$ of C using a divide and conquer method $\%$ - $[ \mathtt { n } , \mathtt { n } ] \ = \ \mathtt { s i z e } ( \mathtt { C } )$ ； if n $< =$ nmin，L = chol(C); else $\begin{array} { l }  { \mathrm { { n 1 } ~ = ~ f 1 { \mathrm { o o r } } \left( n / 2 \right) ; ~ \mathrm { { n 2 } ~ = ~ \mathrm { { n - n 1 } ; } } } } \\ { { \mathrm { { j 1 } ~ = ~ 1 : n 1 ; ~ { \dot { j } } 2 ~ = ~ \mathrm { { n 1 + 1 : n } } ; } } } \end{array}$ % Recursive call $\mathrm { L 1 1 ~ = ~ \ r c h o l { \left( C ( j 1 , j 1 ) , n m i n \right) } ; }$ % Triangular solve $\begin{array} { r c l } { \operatorname { L } 2 1 } & { = } & { \left( \operatorname { L } 1 1 \backslash \mathbf { C } \left( \mathrm { j } 1 , \mathrm { j } 2 \right) \right) \ : ; } \end{array}$ $\%$ Recursive call $\begin{array} { r c l } { { \mathrm { L 2 2 } } } & { { = } } & { { \mathrm { r c h o 1 ( C ( j 2 , j 2 ) \_ - \Delta L 2 1 * L 2 1 ^ { \circ } , n m i n ) ; } } } \\ { { \mathrm { L } } } & { { = } } & { { \left[ \mathrm { L 1 1 , \ z e r o s ( n 1 , n 2 ) ; \Delta L 2 1 , \ L 2 2 } \right] ; } } \end{array}$ end   
end

The parameter nmin may be tuned according to architecture characteristics. If $n m i n = 1$ ， the algorithm is a purely recursive algorithm，and $\begin{array} { r l } { \mathrm { ~ L ~ } } & { { } = } \end{array}$ sqrt(C） can be substituted for $\begin{array} { r l } { \mathrm { ~ L ~ } } & { { } = } \end{array}$ chol(C).All remaining work is done in triangular solves and matrix multiplication. At level $i$ ， $2 ^ { i }$ calls to matrix-matrix operations are made. In going from level $i$ to $i + 1$ , the number of such calls doubles,and each problem size is halved. Hence the number of flops done at each level goes down in a geometric progression by a factor of 4. Because the total number of flops must remain the same,a large part of the calculations are made at low levels. Since the flop rate goes down with the problem size,the computation time does not quite go down by the factor $1 / 4$ , but for large problems this has lite efect on the total efficiency.

To develop a recursive QR algorithm, $A$ is partitioned as $A = \left( \begin{array} { l l } { A _ { 1 } } & { A _ { 2 } } \end{array} \right)$ , where $A _ { 1 }$ consists of the first $\lfloor n / 2 \rfloor$ columns of $A$ . Assume that the QR factorization of $A _ { 1 }$ has been computed and $A _ { 2 }$ updated as follows:

$$
\begin{array} { r } { Q _ { 1 } ^ { T } A _ { 1 } = \left( \begin{array} { c } { R _ { 1 1 } } \\ { 0 } \end{array} \right) , \qquad Q _ { 1 } ^ { T } A _ { 2 } = Q _ { 1 } ^ { T } \left( \begin{array} { c } { A _ { 1 2 } } \\ { A _ { 2 2 } } \end{array} \right) = \left( \begin{array} { c } { R _ { 1 2 } } \\ { B } \end{array} \right) . } \end{array}
$$

To obtain the QR factorization of $A$ ，

$$
A = \left( Q _ { 1 } \quad Q _ { 2 } \right) \left( \begin{array} { c c } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } \\ { { 0 } } & { { R _ { 2 2 } } } \end{array} \right) ,
$$

it remains to compute the QR factorization of $B = \left( \begin{array} { c c } { B _ { 1 } } & { B _ { 2 } } \end{array} \right)$ giving $Q _ { 2 }$ and $R _ { 2 2 }$

Algorithm 2.6.2 uses recursive calls to perform the CGS QR factorization. If $n < n m i n$ ， where nmin $\geq 1$ is a user-selected parameter, a standard scalar CGS routine is used. If nmin $=$ 1, this can be replaced by settig $\overset { \vartriangle } { \boldsymbol { R } } = ( \boldsymbol { A } ^ { T } \boldsymbol { A } ) ^ { 1 / 2 }$ and $Q = A / R$

# Algorithm 2.6.2 (Recursive CGS Factorization).

function $\left[ \mathbb { Q } , \mathbb { R } \right] ~ = ~ \operatorname { r c g s } \left( \mathbb { A } , \operatorname { n m i n } \right)$ $\%$ RCGS computes the CGS $\mathbb { Q R }$ factorization $\%$ of A using a divide and conquer method %--- $\mathrm { [ m , n ] \ = \ s i z e \left( A \right) }$ if n $< =$ nmin $\left[ { \mathbb Q } , { \mathbb R } \right] \ = \ \mathsf { c g s } \left( \mathsf { A } \right)$ ； else ${ \mathrm { \Large ~ n ~ 1 ~ } } = { \mathrm { \Large ~ f ~ } } { \mathrm { \large ~ 1 ~ o ~ o ~ r ~ } } ( { \mathrm { \bf { n } } } / 2 ) ; { \mathrm { \Large ~ n } } 2 = { \mathrm { \bf ~ n } } - { \mathrm { \bf { n } } } 1 ;$ $\%$ Recursive call $\begin{array} { l } { { \left[ \mathbb { Q } 1 , \mathbb { R } 1 1 \right] \ = \ \operatorname { r c g s } \left( \mathbb { A } \left( : , 1 : \mathrm { n } 1 \right) , \mathrm { n m i n } \right) } } \\ { { \mathrm { R } 1 2 \ = \ \mathbb { Q } 1 ^ { , } \ \ast \ \mathbb { A } \left( : , \mathrm { n } 1 + 1 : \mathrm { n } \right) ; } } \end{array}$ % Recursive call $\begin{array} { l } { { \left[ \mathbb { Q } 2 , \mathrm { R } 2 2 \right] \ = \ \mathrm { r c g s } \left( \mathrm { A } \left( : , \mathrm { n } 1 + 1 : \mathrm { n } \right) \ - \ \mathrm { \mathbb { Q } } 1 * \mathrm { R } 1 2 , \mathrm { n } \mathrm { m i n } \right) ; } } \\ { { \mathbb { Q } \ = \ \left[ \mathbb { Q } 1 \ , \ \mathrm { \mathbb { Q } } 2 \right] \ ; } } \\ { { \mathrm { R } \ = \ \left[ \mathrm { R } 1 1 , \ \mathrm { R } 1 2 ; \ \mathrm { z e r o s } \left( \mathrm { n } 2 , \mathrm { n } 1 \right) , \mathrm { R } 2 2 \right] ; } } \end{array}$ end   
end

Algorithm 2.6.3 below performs a recursive QR factorization of $A \in \mathbb { C } ^ { m \times n }$ $m \geq n )$ . The matrix $Q = I - U T U ^ { T }$ is given in aggregated form, where $U \in \mathbb { C } ^ { m \times n }$ is unit lower trapezoidal and $T \in \mathbb { C } ^ { n \times n }$ is upper triangular. The function houseg(a） generates a Householder reflector $P = I \mp \tau u u ^ { T }$ such that $P a = \sigma e _ { 1 }$ ， $\sigma = - \mathrm { s i g n } \left( a _ { 1 } \right) \| a \| _ { 2 }$

# Algorithm 2.6.3 (Recursive Householder QR Factorization).

function [U,T,R] $=$ recqr(A) $\%$ RECQR computes recursively the $\mathbb { Q R }$ factorization $\%$ of the m by n matrix A $\mathrm { ~ ( ~ m ~ } > = \mathrm { ~ n ~ ) ~ }$ .Output is the $\%$ n by n R and $\sf { Q } \ = \ \left( \ I \mathrm { ~ \ - ~ } \ U T U ^ { \Omega } \right)$ in aggregated form. $\%$ 1- $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ size(A); if $\texttt { n } = = \texttt { 1 }$ ，[U,T,R] $=$ houseg(A); else $\begin{array} { l } { { \mathrm { n } 1 ~ = ~ \mathrm { f } \mathrm { { } } 1 { \circ } { \circ } \mathrm { { r } } \left( \mathrm { { n } } / 2 \right) ; } } \\   \mathrm { { } } \mathrm { n } 2 ~ = ~ \mathrm { { } } \mathrm { { n } } ~ - ~ \mathrm { { } } \mathrm { { n } } 1 ; ~ \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm  { } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { } \mathrm { { } } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm   \end{array}$ $\%$ Recursive call [U1,T1,R1] $=$ recqr(A(1:m,1:n1)); $\begin{array} { r l r } { \mathrm { ~ \mathsf { B } ~ } = } & { { } \mathrm { A } \left( \mathrm { 1 } : \mathrm { m } , \mathrm { j } : \mathrm { n } \right) \mathrm { ~ \mathsf { \Omega } ~ } - } & { { } \left( \mathrm { U } \mathrm { 1 } * \mathrm { T } \mathrm { 1 } ^ { \prime } \right) * \left( \mathrm { U } \mathrm { 1 } ^ { \prime } * \mathrm { A } \left( \mathrm { 1 } : \mathrm { m } , \mathrm { j } : \mathrm { n } \right) \right) ; } \end{array}$ $\%$ Recursive call ${ \begin{array} { l } { { \mathrm { [ U 2 ~ , T 2 , R 2 ] ~ = ~ { r e c q r } ( B \left( j : m , 1 : n 2 \right) ) ~ ; } } } \\ { { \mathrm { ~ R ~ = ~ { \left[ R 1 , ~ B \left( 1 : n 1 , 1 : n 2 \right) ~ ; ~ { \theta ~ z e r o s } \left( n - n 1 , n 1 \right) , ~ R 2 \right] } ~ ; } } } \\ { { \mathrm { ~ U 2 ~ = ~ { \left[ z e r o s \left( n 1 , n 2 \right) ~ ; ~ { \theta U 2 } \right] } ~ ; } } } \\ { { \mathrm { ~ U ~ = ~ { \left[ U 1 , ~ U 2 \right] } ~ ; } } } \\ { { \mathrm { ~ T ~ = ~ { \left[ T 1 , ~ - T 1 * \left( U 1 ^ \prime * U 2 \right) * T 2 ; ~ { \theta z e r o s } \left( n 2 , n 1 \right) , ~ T 2 \right] } ~ ; } } } \end{array} }$ end   
end

A disadvantage of this algorithm is the overhead in storage and operations caused by the $T$ matrices.At the end of the recursive QR factorization a $T$ -matrix of size $n \times n$ is formed and stored. This can be avoided by using a hybrid of the partitioned and recursive algorithms, where the recursive QR algorithm is only used to factorize the blocks in the partitioned algorithm; see Elmroth and Gustavson [385, 2004].

# Notes and references

O'Leary and Whitman [841,199o] analyze algorithms for Householder and MGS QR factoriza-tions on distributed MIMD machines using rowwise partitioning schemes. Gunter and Van de Geijn [553, 2oo5l present parallel algorithms for QR factorizations.A recursive algorithm for Cholesky factorization of a matrix in packed storage format is given in Andersen, Wasniewski, and Gustavson [23, 2oo1]. An incremental parallel QR factorization code is given by Baboulin et al. [49, 2oog]. Algorithms for QR factorization for multicore architectures are developed by Buttari et al.[196,20o8], Buttari [195,2013],and Yeralan et al.[1139,2017]. Communication avoiding rank-revealing QR factorizations are developed by Demmel et al. [3O5,2o15]. Recent developments in hardware and software for large-scale accelerated multicores are surveyed by Abdelfattah et al. [2, 2o16]. The impact of hardware developments on subroutines for computing the SVD is surveyed by Dongarra et al. [323, 2018].

# 2.6.3 - BLAS and Linear Algebra Libraries

The core of most applications in scientifc computing are subroutines implementing algorithms for matrix computations such as LU, QR,and SVD factorizations. To be efficient, these have to be continuously adapted as computer architectures change. The first collection of high quality software for linear algebra appeared in 1971 in the Handbook by Wilkinson and Reinsch [1123, 1971]. It contained eleven subroutines written in ALGOL 6O for linear systems,linear least squares,and linear programming and eighteen routines for eigenvalue problems.

EISPACK is a collection of Fortran 77 subroutines for computing eigenvalues and/or eigen-vectors of several different classes of matrices as wellas the SVD; see Smith et al.[1OO5,1976] and Garbow et al. [441,1977]. The subroutines are primarily based on a collection of ALGOL procedures in the Handbook mentioned above,although some were updated to increase reliability and accuracy.

In 1979 a set of standard routines called BLAS (Basic Linear Algebra Subprograms) were introduced to perform frequently occurring operations； see Lawson et al. [728,1979l. These included operations such as scalar product $\beta : = x ^ { T } y$ (Sdot), vector sums $y : = \alpha x + y$ (Saxpy), scaling $y \ : = \ : \alpha x$ (Sscal),and Euclidean norm $\beta = \| x \| _ { 2 }$ (Snrm2). Both single- and doubleprecision real and complex operations were provided. BLAS leads to shorter and clearer code and aids portability. Furthermore, machine-independent optimization can be obtained by using tuned BLAS provided by manufacturers.

LINPACK is a collection of Fortran subroutines using BLAS that analyzes and solves linear equations and linear least squares problems. It solves systems whose matrices are general, banded,symmetric positive definite and indefinite, triangular, or tridiagonal. It uses QR and SVD for solving least squares problems. These subroutines were developed from scratch and include several innovations; see Dongarra et al. [322,1979].

While successful for vector-processing machines, Level 1 BLAS were found to be unsatisfactory for the cache-based machines introduced in the 198Os. This brought about the development of Level 2 BLAS that involve operations with one matrix and one or several vectors, e.g.,

$$
\scriptstyle y : = \alpha A x + \beta y ,
$$

where $A$ is a matrix, $T$ is an upper or lower triangular matrix, and $x$ and $y$ are vectors; see Dongarra et al. [325,326,1988]． Level 2 BLAS involve $O ( m n )$ data,where $m \times n$ is the dimension of the matrix involved, and the same number of arithmetic operations.

When RISC-type microprocessors were introduced,Level 2 BLAS failed to achieve adequate performance,due to a delay in geting data to the arithmetic processors. In Level 3 BLAS, introduced in 1990,the vectors in Level 2 BLAS are replaced by matrices. Some typical Level 3 BLAS are

$$
\begin{array} { l } { { C : = \alpha A B + \beta C , } } \\ { { C : = \alpha A ^ { T } B + \beta C , } } \\ { { C : = \alpha A B ^ { T } + \beta C , } } \\ { { B : = \alpha T B , } } \\ { { B : = \alpha T ^ { - 1 } B . } } \end{array}
$$

For $n \times n$ matrices,Level 3 BLAS use $O ( n ^ { 2 } )$ data but perform $O ( n ^ { 3 } )$ arithmetic operations. This gives a surface-to-volume effect for the ratio of data movement to operations and avoids excessive data movements between different parts of the memory hierarchy. Level 3 BLAS can achieve close to optimal performance on a large variety of computer architectures and makes it possible to write portable high-performance linear algebra software.Formal definitions for

Level 3 BLAS were published in 2001; see Blackford et al.[155,20o2]. Vendor-supplied highly effcient machine-specific implementations of BLAS libraries are available,such as Intel Math Kernel Library (MKL), IBM Scientific Subroutine Library (ESSL),and the open-source BLAS libraries OpenBLAS and ATLAS.

The kernel in the Level 3 BLAS that gets closest to peak performance is the matrix-matrix multiply routine GEMM.Typically, it will achieve over $90 \%$ of peak on matrices of order greater than a few hundred. The bulk of the computation of other Level 3 BLAS such as symmetric matrix-matrix multiply (SYMM), triangular matrix-matrix multiply (TRMM),and symmetric rank- $k$ update (SYRK), can be expressed as calls to GEMM; see Kägstrom, Ling, and Van Loan [679,1998].

The LAPACK library [27,1999], first released in 1992, was designed to supersede and inte-grate LINPACK and EISPACK. The subroutines in LAPACK were restructured to achieve greater effciency on both vector processors and shared-memory multiprocessors. LAPACK was incor-porated into MATLAB in the year 2Ooo. LAPACK is continually improved and updated and available from http://www.netlib.org/lapack/. Different versions and releases are listed there as well as information on related projects. A number of parallel BLAS libraries can be used in LAPACK to take advantage of common techniques for shared-memory parallelization such as pThreads or OpenMP.

The last decade has been marked by the proliferation of multicore processors and hardware accelerators that present new challenges in algorithm design. On such machines,costs for communication,i.e., moving data between different levels of memory hierarchies and processors,can exceed arithmetic costs by orders of magnitude; see Graham, Snir, and Patterson [524, 2004]. This gap between computing power and memory bandwidth keeps increasing; see Abdelfatta et al.[1, 2o21]. A key to high efficiency is locality of reference, which requires splitting opera-tions into carefully sequenced tasks that operate on small portions of data. Iterative refinement is exploited by Dongarra and his coworkers for accelerating multicore computing; see Abdelfatta et al. [2, 2016].

There are two costs associated with communication: bandwidth cost (proportional to the amount of data moved) and latency cost (proportional to the number of messages in which these data are sent). Ballard et al. [65, 2o11] prove bounds on the minimum amount of communication needed for a wide variety of matrix factorizations including Cholesky and QR factorizations. These lower bounds generalize earlier bounds by Irony,Toledo,and Tiskin [657,2oo4] for matrix products. New linear algebra algorithms with reduced communication costs are discussed and examples given that attain these lower bounds.

ScaLAPACK is an extension of LAPACK designed to run effciently on newer MIMD distributed memory architectures； see Choi et al.[243,1996] and Blackford et al.[154,1997]. ScaLAPACK builds on distributed memory versions of paralel BLAS (PBLAS) and on a set of Basic Linear Algebra Communication Subprograms (BLACS) for executing communication tasks. This makes the top level code of ScaLAPACK look quite similar to the LAPACK code. Matrices are arranged in a two-dimensional block-cyclic layout using a prescribed block size. New implementations of algorithms are available via the open-source libraries PLASMA and MAGMA; see Agullo et al. [10, 2009].

Chapter 3

# Generalized and Constrained Least Squares

# 3.1 - Generalized Least Squares Problems 3.1.1 - Generalized Least Squares

Many applications of least squares involve a general Gauss-Markov linear model

$$
A x + \epsilon = b , \qquad \mathcal { V } ( \epsilon ) = \sigma ^ { 2 } V ,
$$

with Hermitian positive definite error covariance matrix $V \neq I$ Then the following result holds.

Theorem 3.1.1. Consider a Gauss-Markov linear model $A x = b + e$ with $A \in \mathbb { C } ^ { m \times n }$ of $\operatorname { r a n k } ( A ) = n$ and symmetric positive definite error covariance matrix $\mathcal { V } ( e ) = \sigma ^ { 2 } V \in \mathbb { C } ^ { m \times m } ,$ Then the best unbiased linear estimate of $x$ is the solution of the generalized least squares (GLS) problem

$$
\operatorname* { m i n } _ { x } { ( b - A x ) ^ { H } V ^ { - 1 } ( b - A x ) } .
$$

The solution $\widehat { x }$ satisfies the generalized normal equations

$$
A ^ { H } V ^ { - 1 } A x = A ^ { H } V ^ { - 1 } b
$$

or, equivalently,the orthogonality condition $A ^ { H } V ^ { - 1 } r = 0$ ,where $r = b - A x$

The covariance matrix of the estimate of $x$ is

$$
\begin{array} { r } { \mathcal { V } ( \widehat { \boldsymbol { x } } ) = \sigma ^ { 2 } ( \boldsymbol { A } ^ { H } \boldsymbol { V } ^ { - 1 } \boldsymbol { A } ) ^ { - 1 } \in \mathbb { R } ^ { m \times m } , } \end{array}
$$

and an unbiased estimate of $\sigma ^ { 2 }$ is

$$
s ^ { 2 } = { \widehat { r } } ^ { H } V ^ { - 1 } { \widehat { r } } / ( m - n ) , \quad { \widehat { r } } = b - A { \widehat { x } } .
$$

Proof. Since $V$ is positive definite, the Cholesky factorization $V = L L ^ { H }$ exists. Then $A ^ { H } V ^ { - 1 } A$ $= ( \overset { \cdot } { L } ^ { - 1 } A ) ^ { H } L ^ { - 1 } \overset { \cdot } { A }$ ,and problem (3.1.2) can be reformulated as

$$
\operatorname* { m i n } _ { x } \| L ^ { - 1 } ( A x - b ) \| _ { 2 } .
$$

This is a standard least squares problem $\operatorname* { m i n } _ { x } \| \widetilde { A } x - \widetilde { b } \|$ , where $\stackrel { \sim } { A } = L ^ { - 1 } A$ and $\widetilde { b } = L ^ { - 1 } b$ The proof now follows by replacing $A$ and $b$ in Theorem 1.1.4 with $\widetilde { A }$ and $\widetilde { b }$ □

In the following we assume that $A , b$ and $V$ are real． The GLS problem can be solved by first computing $V = L L ^ { T }$ and then solving $L { \widetilde { A } } = A$ and $L { \widetilde { b } } = b$ . The normal equations $\bar { \tilde { A } } { } ^ { T } \tilde { A } x = \tilde { A } { } ^ { T } \tilde { b }$ are formed and solved by Cholesky factorization. Alternatively, using the QR factorization

$$
L ^ { - 1 } A = Q \left( \begin{array} { c } { { R } } \\ { { 0 } } \end{array} \right) , \quad Q = \left( Q _ { 1 } \quad Q _ { 2 } \right) ,
$$

we get the solution $x = R ^ { - 1 } Q _ { 1 } ^ { T } L ^ { - 1 } b$

Computing the Cholesky factorization $V ~ = ~ L L ^ { T }$ requires about $m ^ { 3 } / 3$ flops for a dense matrix $V$ .Forming $\stackrel { \sim } { A } = L ^ { - 1 } A$ and $\widetilde { b } = L ^ { - 1 } b$ requires a further $m ^ { 2 } ( n + 1 )$ flops. This may be prohibitive unless $V$ has a favorable structure.When $V$ is a banded matrix with small bandwidth $w$ ,the work in the Cholesky factorization is only about $m w ( w + 3 )$ flops.Frequently $V$ is diagonal. Such weighted least squares problems are treated in Section 3.2.1.

For a consistent linear system $A ^ { T } y = c$ of full row rank, the generalized least-norm (GLN) problem is

$$
\operatorname* { m i n } _ { y } y ^ { T } V y { \mathrm { ~ s u b j e c t ~ t o ~ } } A ^ { T } y = c .
$$

The corresponding generalized normal equations of the second kind are

$$
A ^ { T } V ^ { - 1 } A z = c , \quad y = V ^ { - 1 } A z .
$$

If $V = L L ^ { T }$ is the Cholesky factorization, then $y ^ { T } V y = \| L ^ { T } y \| _ { 2 } ^ { 2 }$ Hence problem (3.1.8) is equivalent to seeking the minimum $\ell _ { 2 }$ -norm solution of the system $\widetilde { A } ^ { T } \widetilde { y } = c$ ,where

$$
\widetilde { A } = L ^ { - 1 } A , \qquad \widetilde { y } = L ^ { T } y .
$$

Alternatively, using the QR factorization (3.1.7) gives

$$
\begin{array} { r } { y = L ^ { - T } Q _ { 1 } ( R ^ { - T } c ) . } \end{array}
$$

Problems GLS and GLN are special cases of the generalized augmented system

$$
M \left( \begin{array} { l } { { y } } \\ { { x } } \end{array} \right) \equiv \left( \begin{array} { l l } { { V } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { y } } \\ { { x } } \end{array} \right) = \left( \begin{array} { l } { { b } } \\ { { c } } \end{array} \right) .
$$

This system is nonsingular if and only if $\operatorname { r a n k } ( A ) = n$ and

$$
{ \mathcal { N } } ( V ) \cap { \mathcal { N } } ( A ^ { T } ) = \{ 0 \} .
$$

If $V$ is positive definite,then by Sylvester's law of inertia (see Horn and Johnson $[ 6 3 9 , 1 9 8 5 ] \rangle$ it follows that the matrix $M \in \bar { \mathbb { R } } ^ { ( m + n ) \times ( m + n ) }$ of system (3.1.11) has $m$ positive and $n$ negative eigenvalues.For this reason,(3.1.11) is called a saddle point system. Eliminating $y$ in (3.1.11) gives the generalized normal equations for $x$ ，

$$
A ^ { T } V ^ { - 1 } A x = A ^ { T } V ^ { - 1 } b - c .
$$

Such systems represent the equilibrium of a physical system and occur in many applications; see Strang [1043,1988].

Theorem 3.1.2. If $A \in \mathbb { R } ^ { m \times n }$ has full column rank and $V \in \mathbb { R } ^ { m \times m }$ is symmetric positive defnite, the augmented system (3.1.11) is nonsingular and gives the first-order optimality conditions for the generalized least squares problem

$$
\operatorname* { m i n } _ { x \in \mathbb { R } ^ { n } } { \frac { 1 } { 2 } } r ^ { T } V ^ { - 1 } r + c ^ { T } x , \quad r = b - A x ,
$$

and for the dual equality-constrained quadratic programming problem

$$
\operatorname* { m i n } _ { y \in \mathbb { R } ^ { m } } \frac { 1 } { 2 } y ^ { T } V y - b ^ { T } y \ s u b j e c t \ t o \ A ^ { T } y = c .
$$

Proof. System (3.1.11) can be obtained by differentiating (3.1.13). This gives $A ^ { T } V ^ { - 1 } ( b { - } A x ) =$ $c$ ,where $V y = b - A x$ . It can also be obtained by differentiating the Lagrangian

$$
L ( x , y ) = { \frac { 1 } { 2 } } y ^ { T } V y - b ^ { T } y + x ^ { T } ( A ^ { T } y - c )
$$

for (3.1.14) and equating to zero. Here $x$ is the vector of Lagrange multipliers.If $c = 0$ in (3.1.13), then $x$ is the GLS solution of (1.1.2). If $b = 0$ in (3.1.14), $y$ is the GLS solution with minimum weighted norm $\| y \| _ { V } = ( y ^ { T } V y ) ^ { 1 / 2 }$ of the consistent underdetermined linear system $A ^ { T } y = c$ □

It follows that any algorithm for solving the GLS problem (3.1.13) is valid also for the quadratic programming problem (3.1.14) and vice versa. An explicit expression for the inverse of augmented matrix $M$ is obtained from the Schur-Banachiewicz formula (3.3.6),

$$
M ^ { - 1 } = \left( \begin{array} { c c } { { V } } & { { A } } \\ { { A ^ { T } } } & { { 0 } } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { { V ^ { - 1 } ( I - P ) } } & { { V ^ { - 1 } A S ^ { - 1 } } } \\ { { S ^ { - 1 } A ^ { T } V ^ { - 1 } } } & { { - S ^ { - 1 } } } \end{array} \right) ,
$$

where

$$
S = A ^ { T } V ^ { - 1 } A , \qquad P = A S ^ { - 1 } ( V ^ { - 1 } A ) ^ { T } .
$$

In terms of the QR factorization (3.1.7), the inverse is

$$
M ^ { - 1 } = \left( \begin{array} { c c } { { L ^ { - T } Q _ { 2 } Q _ { 2 } ^ { T } L ^ { - 1 } } } & { { L ^ { - T } Q _ { 1 } R ^ { - T } } } \\ { { R ^ { - 1 } Q _ { 1 } ^ { T } L ^ { - 1 } } } & { { - R ^ { - 1 } R ^ { - T } } } \end{array} \right) .
$$

The solution of the augmented system (3.1.11) becomes $y = L ^ { - T } u$ ， $x = R ^ { - 1 } v$ ,where

$$
\binom { u } { v } = \binom { Q _ { 2 } Q _ { 2 } ^ { T } } { Q _ { 1 } ^ { T } } - I \biggr ) \bigg ( \frac { B ^ { - 1 } b } { R ^ { - T } c } \bigg ) .
$$

# Notes and references

In constrained optimization the augmented system is called the Karush-Kuhn-Tucker (KKT) system. Such systems arise in a wide variety of applications and are often large. Numerous solution methods,both direct and iterative, have been suggested. An excellent survey is given by Benzi, Golub,and Liesen [1O8,2oo5]. Solution methods for augmented systems where the (1,1)-block is indefinite are developed by Golub and Greif [491,2003].

# 3.1.2 - Oblique Projectors

A matrix $P \in \mathbb { R } ^ { m \times m }$ that satisfies $P ^ { 2 } = P$ and $P ^ { T } \neq P$ is an obliqueprojector.Itsplits any vector $b \in \mathbb { R } ^ { m }$ into a sum $b = P b + ( I - P ) b$ ，

$$
P b \in \mathcal { R } ( P ) , \quad ( I - P ) b = \mathcal { N } ( P ) ^ { \perp } .
$$

Consider first the two-dimensional case. Let $u$ and $v$ be unit vectors in $\mathbb { R } ^ { 2 }$ such that $\cos \theta =$ $v ^ { T } u > 0$ Then

$$
P = u ( v ^ { T } u ) ^ { - 1 } v ^ { T } = \frac { 1 } { \cos \theta } u v ^ { T }
$$

is the oblique projector onto $u$ along the orthogonal complement of $v$ .Similarly, $\begin{array} { r l } { P ^ { T } } & { { } = } \end{array}$ $\boldsymbol { v } ( \boldsymbol { u } ^ { T } \boldsymbol { v } ) ^ { - 1 } \bar { \boldsymbol { u } ^ { T } }$ is the oblique projector onto $v$ along the orthogonal complement of $u$ If $u = v$ ， then $P$ is an orthogonal projector and $\cos \theta \ = \ 1$ .When $v$ is almost orthogonal to $u$ ，then $\| P \| _ { 2 } = 1 / \cos \theta$ becomes large.

It is easily verified that if $V \neq I$ is positive definite, the matrix in (3.1.16),

$$
P = A ( A ^ { T } V ^ { - 1 } A ) ^ { - 1 } ( V ^ { - 1 } A ) ^ { T } ,
$$

is an oblique projector onto $\mathcal { R } ( A )$ along the orthogonal complement to ${ \mathcal { N } } ( V ^ { - 1 } A ) ^ { \perp }$

Theorem 3.1.3. Let $\mathcal { X }$ and $\mathcal { V }$ be two complementary subspaces in $\mathbb { C } ^ { n }$ ，

$$
\mathcal { X } \cap \mathcal { y } = 0 , \qquad \mathcal { X } \cup \mathcal { y } = \mathbb { C } ^ { n } .
$$

Let $U _ { 1 }$ and $V _ { 1 }$ be orthonormal matrices such that $\mathcal { R } ( U _ { 1 } ) = \mathcal { X }$ and $\mathcal { R } ( V _ { 1 } ) = \mathcal { V } ^ { \perp }$ ，where $y \bot$ is the orthogonal complement of $\mathcal { V }$ 、Then the oblique projector onto $\mathcal { X }$ along $\mathcal { V }$ is

$$
P _ { \mathcal { X } , \mathcal { Y } } = U _ { 1 } ( V _ { 1 } ^ { T } U _ { 1 } ) ^ { - 1 } V _ { 1 } ^ { T } .
$$

Similarly, let $U _ { 2 }$ and $V _ { 2 }$ be orthonormal matrices such that ${ \mathcal { X } } ^ { \bot } = { \mathcal { R } } ( U _ { 2 } )$ and $\mathcal { Y } = \mathcal { R } ( V _ { 2 } )$ .Then $P y , x = V _ { 2 } ( U _ { 2 } ^ { T } V _ { 2 } ) ^ { - 1 } U _ { 2 } ^ { T }$ and

$$
P \chi _ { , y } + P _ { y , \chi } = I , \qquad P _ { \chi , y } ^ { T } = P _ { y ^ { \perp } , \chi ^ { \perp } } .
$$

Proof. We have $P _ { \mathcal { X } , \mathcal { Y } } ^ { 2 } = U _ { 1 } ( V _ { 1 } ^ { T } U _ { 1 } ) ^ { - 1 } V _ { 1 } ^ { T } U _ { 1 } ( V _ { 1 } ^ { T } U _ { 1 } ) ^ { - 1 } V _ { 1 } ^ { T } = P _ { \mathcal { X } , \mathcal { Y } }$ This shows that $P _ { \mathcal { X } , \mathcal { Y } }$ is a projector onto $\mathcal { X }$ Similarly, $P y , x = V _ { 2 } ( U _ { 2 } ^ { T } V _ { 2 } ) ^ { - 1 } U _ { 2 } ^ { T }$ is the projector onto $\mathcal { V }$ To prove the first identity in (3.1.22), we first note that the assumption implies $V _ { 1 } ^ { T } V _ { 2 } = 0$ and $U _ { 2 } ^ { T } U _ { 1 } = 0$ . Then

$$
\begin{array} { r l } & { P _ { \mathcal { X } , \mathcal { Y } } + P _ { \mathcal { Y } , \mathcal { X } } = U _ { 1 } ( V _ { 1 } ^ { T } U _ { 1 } ) ^ { - 1 } V _ { 1 } ^ { T } + V _ { 2 } ( U _ { 2 } ^ { T } V _ { 2 } ) ^ { - 1 } U _ { 2 } ^ { T } } \\ & { \qquad = \left( U _ { 1 } , V _ { 1 } \right) \left( \left( V _ { 2 } \quad U _ { 2 } \right) ^ { T } \left( U _ { 1 } ^ { T } \quad V _ { 1 } \right) \right) ^ { - 1 } \left( V _ { 2 } \quad U _ { 2 } \right) ^ { T } } \\ & { \qquad = \left( U _ { 1 } \quad V _ { 1 } \right) \left( U _ { 1 } \quad V _ { 1 } \right) ^ { - 1 } \left( V _ { 2 } , \quad U _ { 2 } \right) ^ { - T } \left( V _ { 2 } \quad U _ { 2 } \right) ^ { T } = I . } \end{array}
$$

Thesecondidetfollos freeprso $P _ { x , y } ^ { T } = V _ { 1 } ( U _ { 1 } ^ { T } V _ { 1 } ) ^ { - 1 } U _ { 1 } ^ { T }$

If $P$ is an orthogonal projector, then

$$
\| P v \| _ { 2 } = \| Q _ { 1 } ^ { T } v \| _ { 2 } \leq \| v \| _ { 2 } ~ \forall ~ v \in \mathbb { C } ^ { n } ,
$$

where equality holds for all vectors in $\mathcal { R } ( P )$ . It follows that $\| \cal P \| _ { 2 } = 1$ .The converse is also true; a projector $P$ is an orthogonal projector only if (3.1.23) holds. The spectral norm of an oblique projector can be exactly computed.

Lemma 3.1.4. Let $P \in \mathbb { R } ^ { n \times n }$ be an oblique projector. Then

$$
\| P \| _ { 2 } = \| I - P \| _ { 2 } = 1 / c , \quad c = \cos { \theta _ { \mathrm { m a x } } ( V _ { 1 } ^ { T } U _ { 1 } ) } ,
$$

where $\theta _ { \mathrm { m a x } }$ is the largest principal angle between $\mathcal { R } ( P )$ and $\mathcal { N } ( P ) ^ { \perp }$

Proof. See Wedin [1110,1985,Lemma 5.1] or Stewart [1032, 2011].

# Notes and references

An excellent introduction to oblique projectors and their representations is given by Wedin [1110, $\mathrm { 1 9 8 5 } ]$ .Afriat [9,1957l gives an exposition of orthogonal and oblique projectors. Relations between orthogonal and oblique projectors are studied in Greville [537,1974l and Cerny [215, 2009]. Numerical properties of oblique projectors are treated by Stewart [1032, 2o11]. Szyld [1055,2oo6] surveys different proofs of the equality $\| P \| = \| I - P \|$ for norms of oblique projectors in Hilbert spaces.

# 3.1.3 - Eliptic MGS and Householder Methods

For a given symmetric positive definite matrix $G$ ，

$$
( x , y ) _ { G } : = y ^ { T } G x , \qquad \| x \| _ { G } = ( x ^ { T } G x ) ^ { 1 / 2 }
$$

defines a scalar product and the corresponding norm. Since the unit ball $\{ x \mid \| x \| _ { G } \leq 1 \}$ is an ellipsoid, $\| \cdot \| _ { G }$ is called an eliptic norm. A generalized Cauchy-Schwarz inequality holds:

$$
| ( x , y ) _ { G } | \leq \| x \| _ { G } \| y \| _ { G } .
$$

Two vectors $x$ and $y$ are said to be $G$ -orthogonal if $( x , y ) _ { G } = 0$ ,and a matrix $Q \in \mathbb { R } ^ { m \times n }$ is $G$ -orthonormal if $Q ^ { T } G Q = I$

If $A = ( a _ { 1 } , \dots , a _ { n } ) \in R ^ { m \times n }$ has full column rank, then an elliptic modified Gram-Schmidt (MGS) algorithm can be used to compute a $G$ orthonormal matrix $Q _ { 1 } = ( q _ { 1 } , \ldots , q _ { n } ) $ and an upper triangular matrix $R$ such that

$$
A = Q _ { 1 } R , \quad Q _ { 1 } ^ { T } G Q _ { 1 } = I _ { n } .
$$

An elementary elliptic projector has the form

$$
\boldsymbol { P } = ( \boldsymbol { I } - \boldsymbol { q } \boldsymbol { q } ^ { T } \boldsymbol { G } ) , \quad \boldsymbol { q } ^ { T } \boldsymbol { G } \boldsymbol { q } = 1
$$

and satisfies $P ^ { 2 } = I - 2 q q ^ { T } G + q ( q ^ { T } G q ) q ^ { T } G = P$ It is easily verified that for any vector $a$ ， $q ^ { T } G ( P a ) = 0$ ,i.e., $P a$ is $G$ -orthogonal to $q$ .Note that $P$ is not symmetric and therefore is an oblique projector; see Section 3.1.2. Furthermore,

$$
G ^ { 1 / 2 } { \cal P } G ^ { - 1 / 2 } = I - \tilde { q } \tilde { q } ^ { T } , \quad \tilde { q } = G ^ { 1 / 2 } q
$$

is an orthogonal projector.

The following row-oriented MGS algorithm computes the factorization (3.1.27).

# Algorithm 3.1.1 (Row-Oriented Elliptic MGS).

function $[ \mathsf { Q } , \mathsf { R } ] \ = \ \mathsf { e m g } \mathsf { s } \left( \mathsf { A } , \mathsf { G } \right)$ ； $\%$ Computes the thin $\mathbb { Q R }$ factorization $\%$ by row-oriented elliptic MGS. $\%$ 1 fo $[ { \mathfrak { m } } , { \mathfrak { n } } ] \ =$ ${ \begin{array} { r l } & { { \mathrm { , ~ n _ { \ell } ~ = ~ s _ { 1 } z e ~ ( } \kappa _ { I } , { \mathrm {  ~ { \scriptstyle ~ n _ { \ell } ~ } } } ) } \quad { \mathrm { , ~ } } \quad { \mathrm { ~ } } = { \mathrm { ~ z e r o s ~ ( n _ { \ell } , n _ { \ell } ) ~ } } ; } \\ & { { \mathrm { ~ r ~ } } { \mathrm { ~ k _ { \ell } ~ = ~ 1 ~ } } : { \mathrm { ~ n _ { \ell } ~ } } } \\ & { { \mathrm { ~ q k _ { \ell } ~ = ~ 0 ~ ( : ~ , ~ k _ \ell ) ~ } } \quad { \mathrm { ~ p k ~ = ~ G * q k _ { \ell } ~ } } ; } \\ & { { \mathrm { ~ R ( k , k _ \ell ) ~ = ~ s _ { \ell } q r t ~ ( p \cdot * q k _ \ell ) ~ } } ; } \\ & { { \mathrm { ~ q k _ { \ell } ~ = ~ q k / R ( k , k _ \ell ) ~ } } \quad { \mathrm { ~ q ( : ~ , ~ k _ \ell ) ~ = ~ q k _ \ell ~ } } ; } \\ & { { \mathrm { ~ p k _ { \ell } ~ = ~ p k / R ( k , k _ \ell ) ~ } } ; } \\ & { { \mathrm { ~ f o r ~ } } { \mathrm { ~ j ~ } } = { \mathrm { ~ k _ { \ell } + 1 : n _ \ell ~ } } } \\ & { { \mathrm { ~ R ( k , j ) ~ = ~ p k ' * q ( : ~ , ~ j ) ~ } } ; } \\ & { { \mathrm { ~ \{ ~ \{ ~ \} ~ } = ~ q ( : ~ , ~ j ) ~ = ~ q ( : ~ , ~ j ) ~ - ~ R ( k , j ) * q k _ { \ell } } } ; } \end{array} $ size(A)； R = zeros(n,n); end end   
end

In addition to the $2 m n ^ { 2 }$ flops for the standard MGS algorithms, elliptic MGS requires $2 m ^ { 2 } n$ flops for $n$ matrix-vector products with $G$ .If $m \gg n$ ,these operations can dominate the overall arithmetic cost. If a factorization $G = B ^ { T } B \in \mathbb { R } ^ { m \times m }$ is known, then

$$
\| x \| _ { G } = ( x ^ { H } B ^ { T } B x ) ^ { 1 / 2 } = \| B x \| _ { 2 } ,
$$

and the operations with $G$ can be replaced by operations with $B$ and $B ^ { T }$ ． A column-oriented MGS using the minimal number $n$ matrix-vector products requires storing $n$ auxiliary vectors $p _ { k } = G q _ { k }$ ， $k = 1 , \dots , n$

# Algorithm 3.1.2 (Column-Oriented Eliptic MGS).

function ${ [ } \mathsf { Q } , \mathsf { R } \mathsf { ] } \ = \ \mathsf { e m g s c } \left( \mathsf { A } , \mathsf { G } \right)$ $\%$ Computes the thin $\mathbb { Q R }$ factorization $\%$ by column-oriented elliptic MGS $\%$ - $[ \mathrm { m } , \mathrm { n } ] = \mathrm { s i } \mathsf { z e } \left( \mathrm { A } \right) ; \quad \mathrm { Q } = \mathrm { A } ;$ $\mathrm { ~ \textsf ~ { ~ R ~ } ~ } =$ zeros $( \mathtt { n } , \mathtt { n } )$ ； for $\mathtt { k } \ = \ 1 { : } \mathtt { n }$ for $\dot { \mathrm { ~ \scriptsize ~ i ~ } } = \mathrm { ~ \scriptsize ~ 1 : ~ k - 1 ~ }$ $\begin{array} { r l } { \mathrm { R } ( \mathrm { i } , \mathrm { k } ) } & { = \mathrm {  ~ p ~ } ( \mathrm { i } ) \mathrm {  ~ \cdot ~ } \sf { s } Q \left( \mathrm { : \nabla } , \mathrm { k } \right) ; } \\ { \mathrm { Q } ( \mathrm { : \nabla } , \mathrm { k } ) } & { = \mathrm {  ~ Q \left( \mathrm { : \nabla } , \mathrm { k } \right) ~ } - \mathrm {  ~ \cal ~ R } ( \mathrm { i } , \mathrm { k } ) \mathrm {  ~ \cdot ~ } \sf { Q } \left( \mathrm { : \nabla } , \mathrm { i } \right) ; } \end{array}$ end $\begin{array} { r l } { \mathrm { p } \left( \mathrm { k } \right) } & { = \mathrm { G } { * } \mathrm { Q } \left( : , \mathrm { k } \right) ; } \\ { \mathrm { R } \left( \mathrm { k } , \mathrm { k } \right) } & { = \mathrm { s q r t } \left( \mathrm { p } \left( \mathrm { k } \right) { * } \mathrm { Q } \left( : , \mathrm { k } \right) \right) ; } \\ { \mathrm { Q } \left( : , \mathrm { k } \right) } & { = \mathrm { Q } \left( : , \mathrm { k } \right) / \mathrm { R } \left( \mathrm { k } , \mathrm { k } \right) ; } \\ { \mathrm { p } \left( \mathrm { k } \right) } & { = \mathrm { \ p } \left( \mathrm { k } \right) / \mathrm { R } \left( \mathrm { k } : , \mathrm { k } \right) ; } \end{array}$ end   
end

The GLS problem (3.1.2) or, equivalently, $\operatorname* { m i n } _ { x } \| b - A x \| _ { G }$ ， $G = V ^ { - 1 }$ , can be solved by an elliptic MGS QR factorization. If applied to the extended matrix $( A b )$ ，this gives the

factorization

$$
\left( A \quad b \right) = \left( Q _ { 1 } \quad q _ { n + 1 } \right) \left( \begin{array} { c c } { { R } } & { { z } } \\ { { 0 } } & { { \rho } } \end{array} \right) .
$$

It follows that $A x \textrm { -- } b = Q _ { 1 } ( R x \textrm { -- } z ) \textrm { -- } \rho q _ { n + 1 }$ ，where $q _ { n + 1 }$ is $G$ -orthogonal to $Q _ { 1 }$ Hence $\| b - A x \| _ { G }$ is minimized when $R x = z$ ,and the solution and residual are obtained from

$$
R x = z , \qquad r = b - A x = \rho q _ { n + 1 } .
$$

Extra right-hand sides can be treated later by updating the factorization $A = Q _ { 1 } R$ using the column-oriented version of elliptic MGS.

Gulliksson and Wedin [551,1992] develop an elliptic Householder QR factorization. An elliptic Householder reflection has the form

$$
H = ( I - \beta u u ^ { T } G ) , \quad \beta = 2 / ( u ^ { T } G u ) ;
$$

cf. the elementary projection operator (3.1.28). The product of an elliptic Householder reflection $H$ with a vector $a$ is given by

$$
H a = ( I - \beta u u ^ { T } G ) a = a - \beta ( u ^ { T } G a ) u .
$$

It is easily verified that $H ^ { 2 } = I$ and hence $H ^ { - 1 } = H$ However, $H$ is neither symmetric nor $G$ -orthogonal, but

$$
G ^ { 1 / 2 } H G ^ { - 1 / 2 } = I - \beta \tilde { u } \tilde { u } ^ { T } , \quad \tilde { u } = G ^ { 1 / 2 } u
$$

is an orthogonal reflection. It is easily verified that

$$
H ^ { T } G H = ( I - \beta G u u ^ { T } ) G ( I - \beta u u ^ { T } G ) = G .
$$

Such matrices are called $G$ -invariant. Clearly, the unit matrix $I$ is $G$ -invariant,and a product of $G$ -invariant matrices $H = H _ { 1 } H _ { 2 } \cdot \cdot \cdot H _ { n }$ is again $G$ -invariant. This property characterizes transformations that leave the $G$ -norm invariant:

$$
\| H x \| _ { G } ^ { 2 } = ( H x ) ^ { T } G H x = x ^ { T } G x = \| x \| _ { G } .
$$

Hence, $\mathrm { m i n } _ { x } \| A x - b \| _ { G }$ and $\operatorname* { m i n } _ { x } \| H ( A x - b ) \| _ { G }$ have the same solution.

To develop a Householder QR algorithm for solving $\operatorname* { m i n } _ { x } \| A x - b \| _ { G }$ ， we construct a sequence of generalized reflections $H _ { i }$ such that

$$
H _ { n } \cdot \cdot \cdot H _ { 1 } ( A x - b ) = { \binom { R } { 0 } } x - { \binom { c _ { 1 } } { c _ { 2 } } } ,
$$

where $R$ is upper triangular and nonsingular. Then an equivalent problem is $\operatorname* { m i n } _ { x } \| R x - c _ { 1 } \| _ { G }$ with solution $x = R ^ { - 1 } c _ { 1 }$ ． As in the standard Householder method, this only requires that we construct a generalized Householder reflection $H$ that maps a given vector $a$ onto a multiple of the unit vector $e _ { 1 }$ ：

$$
H a = a - \beta ( u ^ { T } G a ) u = \pm \sigma e _ { 1 } .
$$

By the invariance of the $G$ -norm,

$$
\sigma \| e _ { 1 } \| _ { G } = \| a \| _ { G } , \quad \| e _ { 1 } \| _ { G } = ( e _ { 1 } ^ { T } G e _ { 1 } ) ^ { 1 / 2 } ,
$$

and from (3.1.34) we have $u = a \mp \sigma e _ { 1 }$ . Hence $\beta = 2 / ( u ^ { T } G u )$ , where

$$
u ^ { T } G u = ( a \mp \sigma e _ { 1 } ) ^ { T } G ( a \mp \sigma e _ { 1 } ) = 2 ( \| a \| _ { G } ^ { 2 } \mp \sigma a ^ { T } G e _ { 1 } ) .
$$

For stability, the sign should be chosen to maximize $u ^ { T } G u$

# Notes and references

Gram-Schmidt orthogonalization in elliptic norms is analyzed by Thomas and Zahar [1059, 1991],[1060,1992]. The numerical stability of such algorithms is studied by Rozloznik et al. [938,2012]. Imakura and Yamamoto [656,2o19] compare different variants of eliptic MGS with respect to efficiency and accuracy.

# 3.1.4 - Generalized QR Factorization

If the covariance matrix is given in factored form

$$
V = B B ^ { T } , \quad B \in \mathbb { R } ^ { m \times p } , \quad p \leq m ,
$$

the GLS problem $\begin{array} { r } { \operatorname* { m i n } _ { x } ( b - A x ) ^ { T } V ^ { - 1 } ( b - A x ) } \end{array}$ can be reformulated as a standard least squares problem $\begin{array} { r } { \operatorname* { m i n } _ { x } \| B ^ { - 1 } A x - B ^ { - 1 } b \| _ { 2 } } \end{array}$ .However, when $B$ is ill-conditioned, computing $\stackrel { \sim } { A } = B ^ { - 1 } A$ and $\widetilde { b } = B ^ { - 1 } b$ may lead to a loss of accuracy. Paige [858, 853,1979l avoids this by using the equivalent formulation

$$
\operatorname* { m i n } _ { v , x } \| v \| _ { 2 } ^ { 2 } \quad { \mathrm { s u b j e c t ~ t o } } \quad A x + B v = b .
$$

Paige's method can handle rank-deficiency in both $A$ and $V$ , but for simplicity we assume in the following that $A$ has full column rank $n$ and $V$ is positive definite. Paige's method starts by computing the QR factorization of $A$ and applies $Q ^ { T }$ to $b$ and $B$ ：

$$
Q ^ { T } \left( A \quad b \right) = \left( \begin{array} { c c } { { R } } & { { c _ { 1 } } } \\ { { 0 } } & { { c _ { 2 } } } \end{array} \right) \} \quad m - n ^ { } , \quad Q ^ { T } B = \left( \begin{array} { c c } { { C _ { 1 } } } \\ { { C _ { 2 } } } \end{array} \right) \} \quad m - n ^ { } .
$$

The constraint in (3.1.36)can then be written in partitioned form

$$
\left( { \begin{array} { c } { C _ { 1 } } \\ { C _ { 2 } } \end{array} } \right) v + \left( { \begin{array} { c } { R } \\ { 0 } \end{array} } \right) x = \left( { \begin{array} { c } { c _ { 1 } } \\ { c _ { 2 } } \end{array} } \right) .
$$

For any vector $v \in R ^ { m }$ ， $x$ can always be determined so that the first block of these equations is satisfied. Next, an orthogonal matrix $P \in R ^ { m \times m }$ is determined such that

$$
P ^ { T } C _ { 2 } ^ { T } = \left( \begin{array} { c } { { 0 } } \\ { { S ^ { T } } } \end{array} \right) \Bigr \} \quad \quad n \quad \quad \quad \quad \quad
$$

and $S$ is upper triangular. By the nonsingularity of $B$ it follows that $C _ { 2 }$ will have linearly independent rows,and hence $S$ will be nonsingular. (Note that after rows and columns are reversed, (3.1.39) is just the QR factorization of $C _ { 2 } ^ { T }$ .） Now, the second set of constraints in (3.1.38) becomes

$$
S u _ { 2 } = c _ { 2 } , \quad \mathrm { w h e r e } \quad P ^ { T } \boldsymbol { v } = \boldsymbol { u } = \left( \begin{array} { c } { u _ { 1 } } \\ { u _ { 2 } } \end{array} \right) \left. \begin{array} { c c } { \right\} } & { \boldsymbol { n } } \\  \left. \begin{array} { c c } { \boldsymbol { m } - \boldsymbol { n } ^ { 2 } } \end{array} \right. . \end{array}
$$

Since $P$ is orthogonal, $\| v \| _ { 2 } = \| u \| _ { 2 }$ . Hence the minimum in (3.1.36)is achieved by taking

$$
u _ { 1 } = 0 , \quad u _ { 2 } = S ^ { - 1 } c _ { 2 } , \quad v = P _ { 2 } u _ { 2 } ,
$$

where $P = \left( P _ { 1 } \ : P _ { 2 } \right)$ . Finally, $x$ is obtained by solving the triangular system $R x = c _ { 1 } - C _ { 1 } v$ in (3.1.38). It can be shown that this gives an unbiased estimate of $x$ for the model (3.1.36) with covariance matrix $\sigma ^ { 2 } B ^ { T } B$ ,where

$$
B = L R ^ { - T } , \quad L = P _ { 1 } ^ { T } C _ { 1 } .
$$

Paige's algorithm requires a total of about $4 m ^ { 3 } / 3 + 2 m ^ { 2 } n$ flops. If $m \gg n$ ,the work in the QR factorization of $C _ { 2 }$ dominates.Paige [858,1979l gives a perturbation analysis for the generalized least squares problem (3.1.6) by using the formulation (3.1.36). An error analysis shows that the algorithm is stable.The algorithm can be generalized in a straightforward way to rank-deficient $A$ and $B$ .

If $B$ has been obtained from the Cholesky factorization of $V$ , it is advantageous to carry out the two QR factorizations in (3.1.37) and (3.1.39) together, maintaining the lower triangular form throughout by a careful sequencing of the plane rotations.When there are several problems of the form (3.1.36) with constant $A$ but variable $B$ ,the QR factorization of $A$ can be computed once and for all. When $m = n$ this reduces the work for solving an additional problem from $( 1 0 / 3 ) n ^ { 3 }$ to $2 n ^ { 3 }$

When computing the QR factorization of the product $C = B A$ or quotient $C = A B ^ { - 1 } =$ $Q R$ the explicit formation of $C$ should be avoided in order to obtain backward stable results. The generalized QR factorization (GQR) of a pair of matrices $A \in \mathbb { R } ^ { m \times n }$ and $\boldsymbol { B } \in \mathbb { R } ^ { m \times p }$ ,introduced by Hammarling [564,1987], is useful for solving generalized equality constrained least squares problems and in the preprocessing stage for computing the generalized SVD (GSVD). When $B$ is nonsingular, GQR implicitly computes

$$
C = B ^ { - 1 } A = Q R , \qquad A \in \mathbb { R } ^ { m \times n } , \qquad B \in \mathbb { R } ^ { m \times m }
$$

without forming $C$ ． The GQR is defined for any matrices $A$ and $B$ with the same number of rows. In the general case the construction of the GQR proceeds in two steps. A rank-revealing QR factorization of $A$ is first computed,

$$
\begin{array} { r }  Q ^ { T } A \Pi = \left( \begin{array} { c c } { U _ { 1 1 } } & { U _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) \begin{array} { l r } { \left. \right\} \boldsymbol { r } \\ { \left. \boldsymbol { \it  m } - \boldsymbol { r } \cdot \nabla \right. } \end{array} } \end{array}
$$

where $Q$ is orthogonal, $\Pi$ is a permutation matrix, and $U _ { 1 1 } \in \mathbb { R } ^ { r \times r }$ is upper triangular and nonsingular. Then $Q ^ { T }$ is applied to $B$ ：

$$
\begin{array} { r }  Q ^ { T } B = \left( \begin{array} { l } { B _ { 1 } } \\ { B _ { 2 } } \end{array} \right) \begin{array} { l } { \} r } \\ { \} \end{array} } \end{array}
$$

Next, an orthogonal matrix $\tilde { Q }$ is constructed so that

$$
Q ^ { T } B \tilde { Q } = R = \left( \begin{array} { l l l } { { R _ { 1 1 } } } & { { R _ { 1 2 } } } & { { 0 } } \\ { { 0 } } & { { R _ { 2 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) \} q \qquad _ { j q \mathrm { ~ - ~ } t } , \tilde { Q } = ( Q _ { 1 } \quad Q _ { 2 } \quad Q _ { 3 } ) ,
$$

where $\mathrm { r a n k } ( B _ { 2 } ) = q , t = r + q , R _ { 1 1 } \in \mathbb { R } ^ { r \times k _ { 1 } }$ and $R _ { 2 2 } \in \mathbb { R } ^ { ( n - q ) \times k _ { 2 } }$ are upper trapezoidal, and $\mathrm { r a n k } ( R _ { 1 1 } ) = k _ { 1 }$ ， $\mathrm { r a n k } ( R _ { 2 2 } ) = k _ { 2 }$ .If $\operatorname { r a n k } ( B ) = p$ ,there will be no zero columns. Note that row interchanges can be performed on the block $B _ { 2 }$ if $Q$ is modified accordingly.

If $B$ is square ( $\mathrm { \Delta } p = m \mathrm { \Delta }$ and nonsingular, then so is $R$ ,and from (3.1.43)-(3.1.44) we have

$$
\tilde { Q } ^ { T } ( B ^ { - 1 } A ) \Pi = \left( { \cal R } _ { 1 1 } ^ { - 1 } U \right) = S , \qquad U = \left( U _ { 1 1 } \quad U _ { 1 2 } \right) ,
$$

which is the QR factorization of $B ^ { - 1 } A \Pi$ . Even in this case one should avoid computing $S$ because in most applications it is not needed,and it is usually more effective to use $R _ { 1 1 }$ and $U$ separately. Another advantage of keeping $R _ { 1 1 }$ and $U$ is that the corresponding decompositions (3.1.43)-(3.1.44) can be updated by the standard methods when columns or rows of $A$ and $B$ are added or deleted. Even when $S$ is defined by (3.1.45) it cannot generally be updated in a stable way.

When $B$ is singular or not square, the GQR can be defined as the QR factorization of $B ^ { \dagger } A$ ， where $B ^ { \dagger }$ denotes the pseudoinverse of $B$ . However, as pointed out by Paige [861,199o], this does not produce the algebraically correct solution for many applications.

The product QR factorization (PQR) of $A \in \mathbb { R } ^ { m \times n }$ and $B \in \mathbb { R } ^ { m \times p }$ can be computed in a similar manner. We use (3.1.43) as the first step and replace (3.1.44) by

$$
\begin{array} { r }  Q ^ { T } B \tilde { Q } = \left( \begin{array} { c c c } { L _ { 1 1 } } & { 0 } & { 0 } \\ { L _ { 2 1 } } & { L _ { 2 2 } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) \xrightarrow [ ] { \} r _ { \bigotimes } , \quad \widetilde { Q } = ( Q _ { 1 } } & { Q _ { 2 } \quad Q _ { 3 } ) , } \end{array}
$$

where $L _ { 1 1 } \in \mathbb { R } ^ { q \times r _ { 1 } }$ ， $L _ { 2 2 } \in \mathbb { R } ^ { ( n - q ) \times r _ { 2 } }$ and $\mathrm { r a n k } ( L _ { 1 1 } ) = r _ { 1 }$ ， $\mathrm { r a n k } ( L _ { 2 2 } ) = r _ { 2 }$ . This gives the PQR because

$$
\widetilde { Q } ^ { T } B ^ { T } A = \left( { { L } _ { 1 1 } ^ { T } } U \right) = \left( { { L } ^ { T } } \right) ,
$$

with $L ^ { T } \in \mathbb { R } ^ { r _ { 1 } \times n }$ upper trapezoidal. Again, one should avoid computing $L ^ { T }$ because it is not needed in most applications,and more accurate methods are usually obtained if $L _ { 1 1 }$ and $U$ are kept separate.(A trivial example is the case when $B = A$ ）

The GQR factorization is given by

$$
A = Q R , \qquad B = Q T Z ,
$$

where $Q \in \mathbb { R } ^ { m \times m }$ and $Z \in \mathbb { R } ^ { p \times p }$ are orthogonal, and $R$ and $T$ have one of the forms

$$
\begin{array} { r } { R = \left( \begin{array} { c } { R _ { 1 1 } } \\ { 0 } \end{array} \right) \quad ( m \geq n ) , \qquad R = ( R _ { 1 1 } \quad R _ { 1 2 } ) \quad ( m < n ) } \end{array}
$$

and

$$
T = \bigl ( 0 \quad T _ { 1 2 } \bigr ) \quad ( m \leq p ) , \qquad T = \biggl ( \begin{array} { l } { { T _ { 1 1 } } } \\ { { T _ { 2 1 } } } \end{array} \biggr ) \quad ( m > p ) .
$$

If $B$ is square and nonsingular, GQR implicitly gives the QR factorization of $B ^ { - 1 } A$ . There is a similar generalized RQ factorization related to the QR factorization of $A B ^ { - 1 }$ . These generalized decompositions and their applications are discussed in Anderson, Bai, and Dongarra [25,1992].

# 3.1.5 - Generalized SVD

The generalized SVD(GSVD) is a generalization of the SVD to a pair of matrices $A$ and $B$ with the same number of columns (or rows).For $B = I$ the GSVD reduces to the SVD of $A$ The GSVD was introduced by Van Loan [1O79,1976], who used it to analyze matrix pencils $A ^ { T } A - \lambda B ^ { T } B$ . Paige and Saunders [856,1981] extended the GSVD and gave it a computationally more reliable form.

The GSVD is closely related to the CS decomposition defined in Section 1.2.4. To see this, let the QR factorization of the matrix $M$ be

$$
M = \left( { \begin{array} { c } { A } \\ { B } \end{array} } \right) = \left( { \begin{array} { c } { Q _ { 1 1 } } \\ { Q _ { 2 1 } } \end{array} } \right) R ,
$$

where the matrices are partitioned conformally. For simplicity,assume that both $A$ and $B$ are square matrices and that $\operatorname { r a n k } ( M ) = n$ . These assumptions are satisfied in many applications. From the CS decomposition in Section 1.2.4 it follows that

$$
\binom { A } { B } = \binom { U _ { 1 } C V ^ { T } R } { U _ { 2 } S V ^ { T } R } ,
$$

where $C = \operatorname* { d i a g } \left( c _ { 1 } , \ldots , c _ { n } \right)$ ， $S = \operatorname { d i a g } \left( s _ { 1 } , \ldots , s _ { n } \right)$ ,and $C ^ { 2 } + S ^ { 2 } = I _ { n }$ . This is essentially the GSVD of the matrix pair $( A , B )$

Theorem 3.1.5 (Generalized SVD). Let $( A , B )$ with $A \in \mathbb { R } ^ { m \times n }$ and $B \in \mathbb { R } ^ { p \times n }$ be a given matrix pair with $M = \left( A ^ { T } B ^ { T } \right) ^ { T }$ and 1 $\operatorname { \dot { a n k } } ( M ) = k$ Then there exist orthogonal matrices $U \in \mathbb { R } ^ { m \times m }$ ， $V \in \mathbb { R } ^ { p \times p }$ ， $Q \in \mathbb { R } ^ { n \times n }$ ,and $W \in \mathbb { R } ^ { k \times k }$ such that

$$
A Q = U \Sigma _ { A } \left( Z \quad 0 \right) , \qquad B Q = V \Sigma _ { B } \left( Z \quad 0 \right) ,
$$

where the nonzero singular values of $Z = W ^ { T } R$ equal those of $M$ and $R \in \mathbb { R } ^ { k \times k }$ is upper triangular. Moreover,

$$
\Sigma _ { A } = \left( \begin{array} { l l l } { { I _ { A } } } & { { } } & { { } } \\ { { } } & { { D _ { A } } } & { { } } \\ { { } } & { { } } & { { O _ { A } } } \end{array} \right) \begin{array} { l }  { \} r } \\ { { \nmid s } } \\ { { \nmid m - r - s } } \end{array} , \Sigma _ { B } = \left( \begin{array} { l l l } { { O _ { B } } } & { { } } & { { } } \\ { { } } & { { D _ { B } } } & { { } } \\ { { } } & { { } } & { { I _ { B } } } \end{array} \right) \begin{array} { l } { { \nmid m - k - r } } \\ { { \nmid s } } \\ { { \nmid k - r - s } } \end{array} .
$$

are diagonal matrices,

$$
\begin{array} { r l } & { D _ { A } = \mathrm { d i a g } \left( \alpha _ { r + 1 } , \ldots , \alpha _ { r + s } \right) , \quad 1 > \alpha _ { r + 1 } \geq \cdot \cdot \cdot \geq \alpha _ { r + s } , } \\ & { D _ { B } = \mathrm { d i a g } \left( \beta _ { r + 1 } , \ldots , \beta _ { r + s } \right) , \quad 0 < \beta _ { r + 1 } \leq \cdot \cdot \cdot \leq \beta _ { r + s } , } \end{array}
$$

and $\alpha _ { i } ^ { 2 } + \beta _ { i } ^ { 2 } = 1$ ， $i = r + 1 , \ldots , r + s$ Furthermore, $I _ { A }$ and $I _ { B }$ are square unit matrices, and $O _ { A } \in \mathbb { R } ^ { ( m - r - s ) \times ( k - r - s ) }$ and $O _ { B } \in \mathbb { R } ^ { ( m - k - r ) \times r }$ are zero matrices with possibly no rows or no columns.

Proof. See Paige and Saunders [856,1981].

Note that in (3.1.51) the column partitionings of $\Sigma _ { A }$ and $\Sigma _ { B }$ are the same. We can define $k$ nontrivial singular value pairs $( \alpha _ { i } , \beta _ { i } )$ of $( A , B )$ ，where $\alpha _ { i } = 1 , \beta _ { i } = 0 , i = 1 , \ldots , r .$ and $\alpha _ { i } = 0$ ， $\beta _ { i } = 1$ ， $i = r + s + 1 , \ldots , k$ . Perturbation theory for generalized singular values by Sun [1047, 1983] and Li [742,1993] shows that as in the SVD, $\alpha _ { i }$ and $\beta _ { i }$ are well-conditioned with respect to perturbations of $A$ and $B$

The GSVD algorithm of Bai and Demmel [59,1993] requires about $2 m n ^ { 2 } + 1 5 n ^ { 3 }$ flops.It uses a preprocessing step for reducing $A$ and $B$ to upper triangular form and gives a new stable and accurate $2 \times 2$ triangular GSVD algorithm. Another approach by Bai and Zha [63,1993] starts by extracting a regular pair $( A , B )$ ,with $A$ and $B$ upper triangular and $B$ nonsingular.

A satisfying aspect of the formulation of GSVD in Theorem 3.1.5 is that $A$ and $B$ are treated identically,and no assumptions are made on the dimension and rank of $A$ and $B$ For many applications this generality is not needed,and the following simplified form similar to that in Van Loan [1079,1976] can be used.

Corollary 3.1.6. Let $\left( \begin{array} { l l } { A } & { B } \end{array} \right)$ with $A \in \mathbb { R } ^ { m \times n }$ and $B \in \mathbb { R } ^ { p \times n }$ be a given matrix pair with $m \ \geq \ n \ \geq \ p$ and $\operatorname { r a n k } ( M ) = n$ ，where $M = \left( \begin{array} { c c } { { A ^ { T } } } & { { B ^ { T } } } \end{array} \right) ^ { T }$ . Then there exist orthogonal matrices $U \in \mathbb { R } ^ { m \times m }$ ， $V \in \mathbb { R } ^ { p \times p }$ and a nonsingular matrix $Z \in \mathbb { R } ^ { n \times n }$ with singular values equal to those of $M$ ，such that

$$
A = U \left( D _ { A } \quad 0 \right) Z , \qquad B = V \left( \begin{array} { c c } { { D _ { B } } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right) Z ,
$$

where $D _ { A } = \operatorname { d i a g } \left( \alpha _ { 1 } , \ldots , \alpha _ { n } \right)$ $\alpha _ { n } ) , D _ { B } = \mathrm { d i a g } ( \beta _ { 1 } , \ldots , \beta _ { p } ) , \alpha _ { i } ^ { 2 } + \beta _ { i } ^ { 2 } = 1 , i = 1 , \ldots , p ,$ and

$$
0 < \alpha _ { 1 } \leq \cdot \cdot \cdot \leq \alpha _ { n } \leq 1 , \qquad 1 \geq \beta _ { 1 } \geq \cdot \cdot \cdot \geq \beta _ { p } > 0 .
$$

The generalized singular values of $( A , B )$ are the ratios $\sigma _ { i } = \alpha _ { i } / \beta _ { i }$ . Setting $W = Z ^ { - 1 } =$ $( w _ { 1 } , \ldots , w _ { k } )$ , we get from (3.1.53)

$$
A w _ { i } = \alpha _ { i } u _ { i } , \quad i = 1 , \ldots , n , \qquad B w _ { i } = \beta _ { i } v _ { i } , \quad i = 1 , \ldots , p ,
$$