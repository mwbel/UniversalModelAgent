$$
\begin{array} { r } { L U \mathbf { x } = L \mathbf { y } = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 3 } & { 4 } & { 1 } & { 0 } \\ { - 1 } & { - 3 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \end{array} \right] = \left[ \begin{array} { c } { 8 } \\ { 7 } \\ { 1 4 } \\ { - 7 } \end{array} \right] . } \end{array}
$$

This system is solved for $\mathbf { y }$ by a simple forward-substitution process:

$$
\begin{array} { r l } { y _ { 1 } = 8 ; } & { { } } \\ { 2 y _ { 1 } + y _ { 2 } = 7 , } & { { } \mathrm { ~ s o ~ } y _ { 2 } = 7 - 2 y _ { 1 } = - 9 ; } \\ { 3 y _ { 1 } + 4 y _ { 2 } + y _ { 3 } = 1 4 , } & { { } \mathrm { ~ s o ~ } y _ { 3 } = 1 4 - 3 y _ { 1 } - 4 y _ { 3 } = 2 6 ; } \\ { - y _ { 1 } - 3 y _ { 2 } + y _ { 4 } = - 7 , } & { { } \mathrm { ~ s o ~ } y _ { 4 } = - 7 + y _ { 1 } + 3 y _ { 2 } = - 2 6 . } \end{array}
$$

We then solve $U \mathbf { x } = \mathbf { y }$ for $\mathbf { x }$ , the solution of the original system; that is,

$$
\left[ { \begin{array} { r r r r r } { 1 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { - 1 } & { - 1 } & { - 5 } \\ { 0 } & { 0 } & { 3 } & { 1 3 } \\ { 0 } & { 0 } & { 0 } & { - 1 3 } \end{array} } \right] \left[ { \begin{array} { r r r r } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \\ { x _ { 4 } } \end{array} } \right] = \left[ { \begin{array} { r r r r } & { 8 } \\ { - 9 } \\ { 2 6 } \\ { - 2 6 } \end{array} } \right] .
$$

Using backward substitution we obtain $x _ { 4 } = 2 , x _ { 3 } = 0 , x _ { 2 } = - 1 , x _ { 1 } = 3 .$

The factorization used in Example 1 is called Doolittle's method and requires that 1's be on the diagonal of L,which results in the factorization described in Theorem 6.17. In Section 6.6,we consider Crout's method,a factorization which requires that 1's be on the diagonal elements of $U$ , and Choleski's method, which requires that $l _ { i i } = u _ { i i }$ , for each $i$ ·

A general procedure for factoring matrices into a product of triangular matrices is contained in Algorithm 6.4. Although new matrices L and U are constructed,the generated values can replace the corresponding entries of A that are no longer needed.

Algorithm 6.4 permits either the diagonal of L or the diagonal of U to be specified.

# LU Factorization

To factor the $n \times n$ matrix $A = ( a _ { i j } )$ into the product of the lower-triangular matrix $L =$ (lij) and the upper-triangular matrix U = (uij); that is, A = LU, where the main diagonal of either $L$ or $U$ consists of all ones:

INPUT dimension $\pmb { n }$ ; the entries $a _ { i j }$ ， $1 \leq i , j \leq n$ of $A$ ; the diagonal $l _ { 1 1 } = \ldots = l _ { n n } = 1$ of $L$ or the diagonal $u _ { 1 1 } = \cdot \cdot \cdot = u _ { n n } = 1$ of $U$

OUTPUT the entries $l _ { i j } , 1 \le j \le i , 1 \le i \le n$ of $L$ and the entries, $u _ { i j } , i \ \leq \ j \ \leq \ n$ ， $1 \leq i \leq n$ of $U$

Step 1 Select $l _ { 1 1 }$ and $u _ { 1 1 }$ satisfying $l _ { 1 1 } u _ { 1 1 } = a _ { 1 1 }$ If $l _ { 1 1 } u _ { 1 1 } = 0$ then OUTPUT('Factorization impossible'); STOP.

Step 2 For $\begin{array} { r l } { j = 2 , \dots , n \mathrm { s e t } u _ { 1 j } = a _ { 1 j } / l _ { 1 1 } ; } & { { } ( F i r s t r o w o f U . ) } \\ { l _ { j 1 } = a _ { j 1 } / u _ { 1 1 } . } & { { } ( F i r s t c o l u m n o f L . ) } \end{array}$

Step3For $i = 2 , \ldots , n - 1$ do Steps 4 and 5.

Step 4 Select $l _ { i i }$ and $u _ { i i }$ satisfying $\begin{array} { r } { l _ { i i } u _ { i i } = a _ { i i } - \sum _ { k = 1 } ^ { i - 1 } l _ { i k } u _ { k i } } \end{array}$ If $l _ { i i } u _ { i i } = 0$ then OUTPUT('Factorization impossible); STOP.

Step 5For $j = i + 1 , \ldots , n$

$$
\begin{array} { r l } & { \mathsf { s e t } u _ { i j } = \frac { 1 } { l _ { i i } } \bigg [ a _ { i j } - \sum _ { k = 1 } ^ { i - 1 } l _ { i k } u _ { k j } \bigg ] ; \quad ( i t h r o w o f U . ) } \\ & { \qquad l _ { j i } = \frac { 1 } { u _ { i i } } \bigg [ a _ { j i } - \sum _ { k = 1 } ^ { i - 1 } l _ { j k } u _ { k i } \bigg ] . \quad ( i t h c o l u m n o f L . ) } \end{array}
$$

Step 6 Select $l _ { n n }$ and $u _ { n n }$ stisfying $\begin{array} { r } { l _ { n n } u _ { n n } = a _ { n n } - \sum _ { k = 1 } ^ { n - 1 } l _ { n k } u _ { k n } } \end{array}$

(Note: 1f ${ { l } _ { n n } } { { u } _ { n n } } = 0$ then $A = L U$ but $A$ is singular.)

Step 7OUTPUT $( l _ { i j }$ for $j = 1$ ，..， $i$ and $i = 1 , \ldots , n )$ ； OUTPUT $\left( { { u } _ { i j } } \right.$ for $j = i , \ldots , n$ and $i = 1 , \ldots , n )$ ； STOP.

Once the matrix factorization is complete,the solution to a linear system of the form $A \mathbf { x } = L U \mathbf { x } = \mathbf { b }$ is found by first letting $\mathbf { y } = U \mathbf { x }$ and solving $L \mathbf { y } = \mathbf { b }$ for y. Since $L$ is lower triangular, we have

$$
y _ { 1 } = \frac { b _ { 1 } } { l _ { 1 1 } } ,
$$

and, for each $i = 2 , 3 , \dots , n$

$$
y _ { i } = \frac { 1 } { l _ { i i } } \left[ b _ { i } - \sum _ { j = 1 } ^ { i - 1 } l _ { i j } y _ { j } \right] .
$$

After $\mathbf { y }$ isfoundyisio $U \mathbf { x } = \mathbf { y }$ is solved for $\mathbf { X }$ by backward substitution using the equations

$$
x _ { n } = { \frac { y _ { n } } { u _ { n n } } } \quad { \mathrm { a n d } } \quad x _ { i } = { \frac { 1 } { u _ { i i } } } \left[ y _ { i } - \sum _ { j = i + 1 } ^ { n } u _ { i j } x _ { j } \right] .
$$

In the previous discussion we assumed that $A \mathbf { x } = \mathbf { b }$ can be solved using Gaussian elimination without row interchanges.From a practical standpoint,this factorization is useful only when row interchanges are not required to control the roundoff error resulting from the use of finite-digit arithmetic. Fortunately, many systems we encounter when using approximation methods are of this type,but we will now consider the modifications that must be made when row interchanges are required.We begin the discussion with the introduction of a class of matrices that are used to rearrange, or permute, rows of a given matrix.

An $n \times n$ permutation matrix $P$ is obtained by rearranging the rows of $I _ { n }$ , the identity matrix. This gives a matrix with precisely one nonzero entry in each row and in each column, and each nonzero entry is a 1.

The matrix

$$
P = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }
$$

is a $3 \times 3$ permutation matrix. For any $3 \times 3$ matrix $A$ , multiplying on the left by $P$ has the effect of interchanging the second and third rows of $A$ ：

$$
P A = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] } = { \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \end{array} \right] } .
$$

Similarly, multiplying $A$ on the right by $P$ interchanges the second and third columns of $A$

Two useful properties of permutation matrices relate to Gaussan elimination, the first of which is ilustrated in the previous example. Suppose $k _ { 1 } , \ldots , k _ { n }$ is a permutation of the integers $1 , \ldots , n$ and the permutation matrix $P = ( p _ { i j } )$ is defined by

$$
p _ { i j } = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } j = k _ { i } , } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Then

(i） $P A$ permutes the rows of $A$ ; that is,

$$
P A = \left[ \begin{array} { c c c c } { a _ { k _ { 1 } 1 } } & { a _ { k _ { 1 } 2 } } & { \cdot \cdot \cdot } & { a _ { k _ { 1 } n } } \\ { a _ { k _ { 2 } 1 } } & { a _ { k _ { 2 } 2 } } & { \cdot \cdot \cdot } & { a _ { k _ { 2 } n } } \\ { \vdots } & { \vdots } & { \cdot } & { \vdots } \\ { a _ { k _ { n } 1 } } & { a _ { k _ { n } 2 } } & { \cdot \cdot } & { a _ { k _ { n } n } } \end{array} \right] .
$$

(i） $P ^ { - 1 }$ exists and $P ^ { - 1 } = P ^ { t }$

At the end of Section 6.4 we saw that for any nonsingular matrix $A$ , the linear system $A \mathbf { x } = \mathbf { b }$ can be solved by Gaussian elimination, with the possibility of row interchanges. If we knew the row interchanges that were required to solve the system by Gaussian elimination, we could arrange the original equations in an order that would ensure that no row interchanges are needed. Hence there is a rearrangement of the equations in the system that permits Gaussian elimination to proceed without row interchanges. This implies that for any nonsingular matrix $A$ , a permutation matrix $P$ exists for which the system

$$
P A \mathbf { x } = P \mathbf { b }
$$

can be solved without row interchanges. But this matrix $P A$ can be factored into

$$
P A = L U ,
$$

where $L$ is lower triangular and $U$ is upper triangular. Since $P ^ { - 1 } = P ^ { t }$ ， we have the factorization

$$
A = P ^ { - 1 } L U = ( P ^ { t } L ) U . \ .
$$

The matrix $U$ is still upper triangular, but $P ^ { t } L$ is not lower triangular unless $P = I$

# EXAMPLE 3

Since $a _ { 1 1 } = 0$ , the matrix

$$
A = \left[ { \begin{array} { r r r r } { 0 } & { 1 } & { - 1 } & { 1 } \\ { 1 } & { 1 } & { - 1 } & { 2 } \\ { - 1 } & { - 1 } & { 1 } & { 0 } \\ { 1 } & { 2 } & { 0 } & { 2 } \end{array} } \right]
$$

does not have an $L U$ factorization. However,using therowinterchange $( E _ { 1 } ) \  \ ( E _ { 2 } )$ ， followed by $( E _ { 3 } + E _ { 1 } )  E _ { 3 }$ and $( E _ { 4 } - E _ { 1 } )  E _ { 4 }$ ,produces

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 1 } & { - 1 } & { 2 } \\ { 0 } & { 1 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { 1 } & { 0 } \end{array} \right] } ~ .
$$

Then the row interchange $( E _ { 3 } )  ( E _ { 4 } )$ , followed by $( E _ { 3 } - E _ { 2 } )  E _ { 3 }$ , gives the matrix

$$
U = \left[ { \begin{array} { r r r r } { 1 } & { 1 } & { - 1 } & { 2 } \\ { 0 } & { 1 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 2 } \end{array} } \right] .
$$

The permutation matrix associated with the row interchanges $( E _ { 1 } )  ( E _ { 2 } )$ and $( E _ { 3 } ) $ $( E _ { 4 } )$ is

$$
P = { \left[ \begin{array} { l l l l } { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} \right] } ~ .
$$

Gaussian elimination can be performed on $P A$ without row interchanges to give the $L U$ factorization of $P A$ ，

$$
P A = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 1 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { - 1 } & { 2 } \\ { 0 } & { 1 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 2 } \end{array} \right] } = L U .
$$

So

$$
A = P ^ { - 1 } L U = ( P ^ { t } L ) U = \left[ { \begin{array} { r r r r } { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 1 } & { 0 } \end{array} } \right] \left[ { \begin{array} { r r r r } { 1 } & { 1 } & { - 1 } & { 2 } \\ { 0 } & { 1 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 2 } \end{array} } \right] .
$$

Maple has the command LUdecomp to compute a factorization of the form $A = P L U$ of the matrix A. If the matrix A has been created, the function call $> \mathrm { U } : = \mathrm { L U d e c o m p } \left( \mathrm { A } , \mathrm { P } = ^ { \prime } \mathrm { G } ^ { \prime } , \mathrm { L } = ^ { \prime } \mathrm { H } ^ { \prime } \right) ;$ returns the upper triangular matrix $U$ as the value of the function and returns the lower triangular matrix $L$ in $H$ and the permutation matrix $P$ in $G$

# Exercise set 6.5

1．Solve the following linear systems:

a. $[ { \begin{array} { r r r } { 1 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 0 } & { 1 } \end{array} }  [ { \begin{array} { r r r } { 2 } & { 3 } & { - 1 } \\ { 0 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { 3 } \end{array} } ] [ { \begin{array} { r r r } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} } ] = [ { \begin{array} { r r r } { 2 } \\ { - 1 } \\ { 1 } \end{array} } ]$ ${ \begin{array} { r l } { \mathbf { b . } } & { { } { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } \\ { 3 } & { 2 } & { - 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { - 1 } \\ { 3 } \\ { 0 } \end{array} \right] } } \end{array} }$

2. Consider the following matrices. Find the permutation matrix $P$ so that $P A$ can be factored into the product $L U$ ，where $L$ is lower triangular with $\mathbf { \nabla } _ { 1 } \mathfrak { s }$ on its diagonal and $U$ is upper triangular for these matrices.

$$
\begin{array} { c c } { { A = \left[ \begin{array} { c c c } { { 1 } } & { { 2 } } & { { - 1 } } \\ { { 2 } } & { { 4 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { - 1 } } \end{array} \right] ~ } } & { { ~ \bf b . } } & { { ~ A = \left[ \begin{array} { c c c } { { 0 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 2 } } & { { - 1 } } \\ { { 1 } } & { { - 1 } } & { { 1 } } \end{array} \right] ~ } } \\ { { A = \left[ \begin{array} { c c c } { { 1 } } & { { 1 } } & { { - 1 } } & { { 0 } } \\ { { 1 } } & { { 1 } } & { { 4 } } & { { 3 } } \\ { { 2 } } & { { - 1 } } & { { 2 } } & { { 4 } } \\ { { 2 } } & { { - 1 } } & { { 2 } } & { { 3 } } \end{array} \right] ~ } } & { { ~ \bf d . } } & { { ~ A = \left[ \begin{array} { c c c } { { 0 } } & { { 1 } } & { { 1 } } & { { 2 } } \\ { { 0 } } & { { 1 } } & { { 1 } } & { { - 1 } } \\ { { 1 } } & { { 2 } } & { { - 1 } } & { { 3 } } \\ { { 1 } } & { { 1 } } & { { 2 } } & { { 0 } } \end{array} \right] ~ } } \end{array}
$$

3.Factor the following matrices into the $L U$ decomposition using the $L U$ Factorization Algorithm with ${ l } _ { i i } = 1$ for all $i$

8 $\cdot \quad { \left[ \begin{array} { l l l } { 2 } & { - 1 } & { 1 } \\ { 3 } & { 3 } & { 9 } \\ { 3 } & { 3 } & { 5 } \end{array} \right] }$ $\mathbf { b } . \quad \left[ \begin{array} { r r r } { 1 . 0 1 2 } & { - 2 . 1 3 2 } & { 3 . 1 0 4 } \\ { - 2 . 1 3 2 } & { 4 . 9 0 6 } & { - 7 . 0 1 3 } \\ { 3 . 1 0 4 } & { - 7 . 0 1 3 } & { 0 . 0 1 4 } \end{array} \right]$   
c. $\left[ { \begin{array} { r r r r r } { 2 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { 1 . 5 } & { 0 } & { 0 } \\ { 0 } & { - 3 } & { 0 . 5 } & { 0 } \\ { 2 } & { - 2 } & { 1 } & { 1 } \end{array} } \right]$ 2.1756 4.0231 -2.1732 5.1967 --4.0231 6.0000 0 1.1973   
d --1.0000 -5.2107 1.1111 0 6.0235 7.0000 0 -4.1561

4. Modify the LU Factorization Algorithm so that it can be used to solve a linear system,and then solve the following linear systems.

a. $\begin{array} { l } { { 2 x _ { 1 } - x _ { 2 } + x _ { 3 } = - 1 } } \\ { { 3 x _ { 1 } + 3 x _ { 2 } + 9 x _ { 3 } = 0 , } } \\ { { 3 x _ { 1 } + 3 x _ { 2 } + 5 x _ { 3 } = 4 . } } \end{array}$ b. $1 . 0 1 2 x _ { 1 } - 2 . 1 3 2 x _ { 2 } + 3 . 1 0 4 x _ { 3 } = 1 . 9 8 4 ,$ $- 2 . 1 3 2 x _ { 1 } + 4 . 0 9 6 x _ { 2 } - 7 . 0 1 3 x _ { 3 } = - 5 . 0 4 9 ,$ $3 . 1 0 4 x _ { 1 } - 7 . 0 1 3 x _ { 2 } + 0 . 0 1 4 x _ { 3 } = - 3 . 8 9 5 .$

$$
\begin{array} { r l r } { 2 x _ { 1 } } & { \mathrm { ~ } } & { = 3 , } \\ { x _ { 1 } + 1 . 5 x _ { 2 } } & { = 4 . 5 , } \\ { - } & { 3 x _ { 2 } + 0 . 5 x _ { 3 } } & { = - 6 . 6 , } \\ { 2 x _ { 1 } - } & { 2 x _ { 2 } + } & { x _ { 3 } + x _ { 4 } = 0 . 8 . } \end{array}
$$

$$
\begin{array} { r } { 2 . 1 7 5 6 x _ { 1 } + 4 . 0 2 3 1 x _ { 2 } - 2 . 1 7 3 2 x _ { 3 } + 5 . 1 9 6 7 x _ { 4 } = 1 7 . 1 0 2 , } \\ { - 4 . 0 2 3 1 x _ { 1 } + 6 . 0 0 0 0 x _ { 2 } \qquad + 1 . 1 9 7 3 x _ { 4 } = - 6 . 1 5 9 3 , } \\ { - 1 . 0 0 0 0 x _ { 1 } - 5 . 2 1 0 7 x _ { 2 } + 1 . 1 1 1 1 x _ { 3 } \qquad = 3 . 0 0 0 4 , } \\ { 6 . 0 2 3 5 x _ { 1 } + 7 . 0 0 0 0 x _ { 2 } \qquad - 4 . 1 5 6 1 x _ { 4 } = 0 . 0 0 0 0 . } \end{array}
$$

5.Obtain factorizations of the form $A = P ^ { t } L U$ for the following matrices.

$$
{ \begin{array} { r l } { 1 . } & { A = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 3 } \\ { 1 } & { 1 } & { - 1 } \\ { 0 } & { - 1 } & { . 1 } \end{array} \right] } } \\ { . } & { A = { \left[ \begin{array} { l l l l } { 1 } & { - 2 } & { 3 } & { 0 } \\ { 3 } & { - 6 } & { 9 } & { 3 } \\ { 2 } & { 1 } & { 4 } & { 1 } \\ { 1 } & { - 2 } & { 2 } & { - 2 } \end{array} \right] } } \end{array} } \qquad \mathbf { { b . } } \quad { \begin{array} { l l } { A = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { - 1 } \\ { 1 } & { 2 } & { 3 } \\ { 2 } & { - 1 } & { 4 } \end{array} \right] } } \\ { 1 . } & { 1 } & { 2 } \end{array} }
$$

6. Suppose $A = P ^ { t } L U$ ，where $P$ is a permutation matrix, $L$ is a lower-triangular matrix with ones on the diagonal, and $U$ is an upper-triangular matrix.

a.Count the number of operations needed to compute $P ^ { t } L U$ for a given matrix A. $\mathbf { b } _ { \bullet }$ Show that if $P$ contains $k$ row interchanges, then

$$
\begin{array} { r } { \operatorname* { d e t } P = \operatorname* { d e t } P ^ { t } = ( - 1 ) ^ { k } . } \end{array}
$$

c. Use det $A { \mathrm { ~ } } = \operatorname* { d e t } P ^ { t }$ det $L$ det $U = ( - 1 ) ^ { k }$ det $v$ to count the number of operations for determining det A by factoring.

d. Compute det $\pmb { A }$ and count the number of operations when

$$
A = \left[ { \begin{array} { r r r r r r r } { 0 } & { 2 } & { 1 } & { 4 } & { - 1 } & { 3 } \\ { 1 } & { 2 } & { - 1 } & { 3 } & { 4 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { - 1 } & { 2 } & { - 1 } \\ { 2 } & { 3 } & { - 4 } & { 2 } & { 0 } & { 5 } \\ { 1 } & { 1 } & { 1 } & { 3 } & { 0 } & { 2 } \\ { - 1 } & { - 1 } & { 2 } & { - 1 } & { 2 } & { 0 } \end{array} } \right] .
$$

7.a. Show that the $L U$ Factorization Algorithm requires ${ \scriptstyle { \frac { 1 } { 3 } } n ^ { 3 } - { \frac { 1 } { 3 } } n }$ multiplications/divisions and ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 1 } { 2 } } } n ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } n$ additions/subtractions.

b.Show that solving $\mathbf { \vec { \mathcal { L } } \vec { y } } = \mathbf { \vec { b } }$ ，where $L$ is a lower-triangular matrix with $l _ { i i } = 1$ for all $i$ ， requires ${ \frac { 1 } { 2 } } n ^ { 2 } - { \frac { 1 } { 2 } } n$ multiplications/divisions and ${ \scriptstyle { \frac { 1 } { 2 } } } n ^ { 2 } - { \scriptstyle { \frac { 1 } { 2 } } } n$ additions/subtractions.

c. Show that solving $\pmb { A } \mathbf { x }  \mathbf { b }$ by first factoring $\pmb { A }$ into $A = L U$ and then solving $L \mathbf { y } = \mathbf { b }$ and $U \mathbf { x } = \mathbf { y }$ requires the same number of operations as the Gaussian Elimination Algorithm 6.1.   
d. Count the number of operations required to solve $m$ linear systems $A \mathbf { x } ^ { ( k ) } = \mathbf { b } ^ { ( k ) }$ for $k = 1 , \ldots , m$ by first factoring $\pmb { A }$ and then using the method of part (c) $m$ times.

# 6.6 Special Types of Matrices

We will now turn atention to two classes of matrices for which Gaussian elimination can be performed efectively without row interchanges.The first class is described in the following definition.

# Definition 6.18

The $n \times n$ matrix $A$ is said to be strictly diagonally dominant when

$$
\left| a _ { i i } \right| > \sum _ { { j = 1 } , \atop { j \neq i } } ^ { n } \left| a _ { i j } \right|
$$

holds for each $i = 1 , 2 , \dots , n$

# EXAMPLE 1

Consider the matrices

$$
A = { \left[ \begin{array} { l l l } { 7 } & { 2 } & { 0 } \\ { 3 } & { 5 } & { - 1 } \\ { 0 } & { 5 } & { - 6 } \end{array} \right] } \quad { \mathrm { ~ a n d ~ } } \quad B = { \left[ \begin{array} { l l l } { 6 } & { 4 } & { - 3 } \\ { 4 } & { - 2 } & { 0 } \\ { - 3 } & { 0 } & { 1 } \end{array} \right] } .
$$

The nonsymmetric matrix $A$ is strictly diagonally dominant since $| 7 | > | 2 | + | 0 | , | 5 | >$ $| 3 | + | - 1 |$ ,and $| - 6 | > | 0 | + | 5 |$ . The symmetric matrix $B$ is not strictly diagonally dominant because,for example,in the first row the absolute value of the diagonal element is $| 6 | <$ $| 4 | + | - 3 | = 7$ . It is interesting to note that $A ^ { t }$ is not strictly diagonally dominant, nor, of course, is $B ^ { t } = B$ .

The following theorem was used in Section 3.4 to ensure that there are unique solutions to the linear systems needed to determine cubic spline interpolants.

# Theorem 6.19

A strictly diagonally dominant matrix A is nonsingular. Moreover, in this case, Gaussian elimination can be performed on any linear system of the form $\pmb { A } \mathbf { x } = \mathbf { b }$ to obtain its unique solution without row or column interchanges,and the computations will be stable with respect to the growth of roundoff errors.

Proof We first use proof by contradiction to show that $A$ is nonsingular. Consider the linear system described by $\pmb { A } \mathbf { x } = \pmb { 0 }$ ,and suppose that a nonzero solution $\mathbf { x } = ( x _ { i } )$ to this system exists. Let $k$ be an index for which

$$
0 < | x _ { k } | = \operatorname* { m a x } _ { 1 \leq j \leq n } | x _ { j } | .
$$

Since $\textstyle \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = 0$ for each $i = 1 , 2 , \dots , n$ , we have, when $i = k$

$$
a _ { k k } x _ { k } = - \sum _ { j = 1 , \atop j \not = k } ^ { n } a _ { k j } x _ { j } .
$$

This implies that

$$
| a _ { k k } | | x _ { k } | \leq \sum _ { j = 1 , \atop j \neq k } ^ { n } | a _ { k j } | | x _ { j } | ,
$$

or

$$
| a _ { k k } | \leq \sum _ { { j = 1 } , \atop { j \neq k } } ^ { n } | a _ { k j } | { \frac { | x _ { j } | } { | x _ { k } | } } \leq \sum _ { { j = 1 } , \atop { j \neq k } } ^ { n } | a _ { k j } | .
$$

This inequality contradicts the strict diagonal dominance of $A$ . Consequently, the only solution to $\pmb { A } \mathbf { x } = \pmb { \mathbb { 0 } }$ is $\mathbf { x } = \mathbf { 0 }$ ,a condition shown in Theorem 6.16 to be equivalent to the nonsingularity of $A$ ·

To prove that Gaussian elimination can be performed without row interchanges, we will show that each of the matrices $A ^ { ( 2 ) } , A ^ { ( 3 ) } , \ldots , A ^ { ( n ) }$ generated by the Gaussian elimination process (and described in Section 6.5) is strictly diagonally dominant.

Since $A$ is strictly diagonally dominant, $a _ { 1 1 } \neq 0$ and $A ^ { ( 2 ) }$ can be formed. Thus, for each $i = 2 , 3 , \dots , n .$ ，

$$
a _ { i j } ^ { ( 2 ) } = a _ { i j } ^ { ( 1 ) } - \frac { a _ { 1 j } ^ { ( 1 ) } a _ { i 1 } ^ { ( 1 ) } } { a _ { 1 1 } ^ { ( 1 ) } } , \quad \mathrm { f o r } \quad 2 \leq j \leq n .
$$

Since a(2) $a _ { i 1 } ^ { ( 2 ) } = 0$ ，

$$
\begin{array} { r l } { \frac { 1 } { \sqrt { 2 } } \sum _ { j = 1 } ^ { N } a _ { j } ^ { ( k ) } \Big ( 1 - \sum _ { j = 1 } ^ { N } a _ { j } ^ { ( k ) } - \frac { a _ { j } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \Big ) } & { = } \\ & { \leq \frac { 1 } { \sqrt { 2 } } \sum _ { k = 1 } ^ { N } a _ { j } ^ { ( k ) } - \frac { a _ { j } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \frac { 1 } { a _ { j } ^ { ( k ) } } \Bigg ( 1 - \sum _ { j = 1 } ^ { N } a _ { j } ^ { ( k ) } \frac { a _ { j } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \Bigg ) } \\ & { \leq \frac { 1 } { \sqrt { 2 } } \sum _ { k = 1 } ^ { N } a _ { j } ^ { ( k ) } + \frac { a _ { j } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \frac { 1 } { a _ { j } ^ { ( k ) } } } \\ & { \leq \mu _ { 0 } ^ { ( k ) } ( 1 - \Delta _ { \Delta } ^ { ( k ) } ) - \frac { \mu _ { 0 } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \frac { 1 } { a _ { j } ^ { ( k ) } } \frac { \sum _ { l = 1 } ^ { N } a _ { l } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } } \\ & { < \omega _ { 0 } ^ { ( k ) } ( 1 - \Delta _ { \Delta } ^ { ( k ) } ) + \frac { \mu _ { 0 } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \frac { 1 } { a _ { j } ^ { ( k ) } } \frac { \sum _ { l = 1 } ^ { N } a _ { l } ^ { ( k ) } } { a _ { l } ^ { ( k ) } } } \\ &  =  \omega _ { 0 } ^ { ( k ) } - \frac { \mu _ { 0 } ^ { ( k ) } a _ { j } ^ { ( k ) } } { a _ { j } ^ { ( k ) } } \frac { 1 } { a _ { j } ^ { ( k ) } } ( \frac { \Delta _ { \Delta } ^ { ( k ) } }  \Delta _  \ \end{array}
$$

This establishes the strict diagonal dominance for rows 2,...,n. Since the first row of $A ^ { ( 2 ) }$ and $A$ are the same, $A ^ { ( 2 ) }$ is strictly diagonally dominant.

This process is continued inductively until the upper-triangular and strictly diagonally dominant $A ^ { ( n ) }$ is obtained. This implies that all the diagonal elements are nonzero,so Gaussian elimination can be performed without row interchanges.

The demonstration of stability for this procedure can be found in [We].

The next special class of matrices is called positive definite.

Definition 6.20 A matrix $A$ is positive definite if it is symmetric and if $\mathbf { x } ^ { t } A \mathbf { x } > 0$ for every $\pmb { n }$ -dimensional vector $\mathbf { x } \neq \mathbf { 0 }$ ■

Not all authors require symmetry of a positive definite matrix. For example, Golub and Van Loan [GV],a standard reference in matrix methods, requires only that $\mathbf { x } ^ { t } A \mathbf { x } > 0$ for each $\mathbf { x } \neq \mathbf { 0 }$ . Matrices we call positive definite are called symmetric positive definite in [GV]. Keep this discrepancy in mind if you are using material from other sources.

To be precise,Definition 6.20 should specify that the $1 \times 1$ matrix generated by the operation $\mathbf { x } ^ { t } A \mathbf { x }$ has a positive value for its only entry since the operation is performed as follows:

$$
\mathbf { x } ^ { t } A \mathbf { x } = [ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ] \left[ { \begin{array} { c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \cdots } & { a _ { 2 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n n } } \end{array} } \right] \left[ { \begin{array} { c } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} } \right]
$$

$$
= [ x _ { 1 } , x _ { 2 } , \dotsc , x _ { n } ] { \left[ \begin{array} { l } { \sum _ { j = 1 } ^ { n } a _ { 1 j } x _ { j } } \\ { \sum _ { j = 1 } ^ { n } a _ { 2 j } x _ { j } } \\ { \qquad \vdots } \\ { \sum _ { j = 1 } ^ { n } a _ { n j } x _ { j } } \end{array} \right] } = \left[ \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } a _ { i j } x _ { i } x _ { j } \right] .
$$

# EXAMPlE 2

The matrix

$$
A = \left[ { \begin{array} { r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} } \right]
$$

is positive definite,for suppose $\mathbf { x }$ is any three-dimensional column vector. Then

$$
\begin{array} { r l r } & { } & { \mathbf { x } ^ { t } A \mathbf { x } = [ x _ { 1 } , x _ { 2 } , x _ { 3 } ] \left[ \begin{array} { r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} \right] \left[ \begin{array} { r } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } \\ & { } & { = [ x _ { 1 } , x _ { 2 } , x _ { 3 } ] \left[ \begin{array} { r r r } { 2 x _ { 1 } } & { - } & { x _ { 2 } } \\ { - x _ { 1 } } & { + } & { 2 x _ { 2 } } & { - } \\ { - x _ { 2 } } & { + } & { 2 x _ { 3 } } \end{array} \right] } \\ & { } & { = 2 x _ { 1 } ^ { 2 } - 2 x _ { 1 } x _ { 2 } + 2 x _ { 2 } ^ { 2 } - 2 x _ { 2 } x _ { 3 } + 2 x _ { 3 } ^ { 2 } . } \end{array}
$$

Rearranging the terms gives

$$
\begin{array} { c } { { \bf x ^ { \prime } { \cal A } { \bf x } = x _ { 1 } ^ { 2 } + ( x _ { 1 } ^ { 2 } - 2 x _ { 1 } x _ { 2 } + x _ { 2 } ^ { 2 } ) + ( x _ { 2 } ^ { 2 } - 2 x _ { 2 } x _ { 3 } + x _ { 3 } ^ { 2 } ) + x _ { 3 } ^ { 2 } } } \\ { { { } } } \\ { { = x _ { 1 } ^ { 2 } + ( x _ { 1 } - x _ { 2 } ) ^ { 2 } + ( x _ { 2 } - x _ { 3 } ) ^ { 2 } + x _ { 3 } ^ { 2 } } } \end{array}
$$

and

$$
x _ { 1 } ^ { 2 } + ( x _ { 1 } - x _ { 2 } ) ^ { 2 } + ( x _ { 2 } - x _ { 3 } ) ^ { 2 } + x _ { 3 } ^ { 2 } > 0 ,
$$

uniess $x _ { 1 } = x _ { 2 } = x _ { 3 } = 0$

It should be clear from Example 2 that using the definition to determine whether a matrix is positive definite can be difficult. Fortunately, there are more easily verified criteria, which are presented in Chapter 9, for identifying members of this important class. The next result provides some conditions that can be used to eliminate certain matrices from consideration.

Theorem 6.21 If $A$ is an $n \times n$ positive definite matrix, then a.A is nonsingular; b $a _ { i i } > 0$ , for each $i = 1 , 2 , \dots , n ;$ $\begin{array} { r } { \operatorname* { m a x } _ { 1 \leq k , j \leq n } | a _ { k j } | \leq \operatorname* { m a x } _ { 1 \leq i \leq n } | a _ { i i } | ; } \end{array}$ d. $( a _ { i j } ) ^ { 2 } < a _ { i i } a _ { j j }$ , for each $i \neq j$

# Proof

a.If $\mathbf { x }$ satisfies $A \mathbf { x } = \mathbf { 0 }$ ,then $\mathbf { x } ^ { t } A \mathbf { x } = 0$ Since $\pmb { A }$ is positive definite,this implies $\mathbf { x } = \mathbf { 0 }$ . Consequently, $\pmb { A } \mathbf { x } = \pmb { \mathbb { 0 } }$ has only the zero solution, and $A$ is nonsingular.

b. For a given $i$ ,let $\mathbf { x } = ( x _ { j } )$ be defined by $x _ { i } = 1$ and $x _ { j } = 0$ ,if $j \neq i$ . Since $\mathbf { x } \neq \mathbf { 0 }$ ，

$$
0 < \mathbf { x } ^ { \prime } A \mathbf { x } = a _ { i i } .
$$

c.For $k \neq j$ ,define $\mathbf { x } = ( x _ { i } )$ by

$$
x _ { i } = \left\{ { \begin{array} { l l } { 0 , } & { { \mathrm { i f ~ } } i \neq j { \mathrm { ~ a n d ~ } } i \neq k , } \\ { 1 , } & { { \mathrm { i f ~ } } i = j , } \\ { - 1 , } & { { \mathrm { i f ~ } } i = k . } \end{array} } \right.
$$

Since $\mathbf { x } \neq \mathbf { 0 }$ ，

$$
0 < \mathbf { x } ^ { t } A \mathbf { x } = a _ { j j } + a _ { k k } - a _ { j k } - a _ { k j } .
$$

But $A ^ { t } = A$ ，s $) a _ { j k } = a _ { k j }$ and

$$
2 a _ { k j } < a _ { j j } + a _ { k k } .
$$

Now define ${ \bf z } = ( z _ { i } )$ by

$$
z _ { i } = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { i f } } i \neq j { \mathrm { ~ a n d } } i \neq k , } \\ { 1 , } & { { \mathrm { i f } } i = j { \mathrm { ~ o r ~ } } i = k . } \end{array} \right. }
$$

Then ${ \pmb z } ^ { t } A { \pmb z } > 0$ ,so

$$
- 2 a _ { k j } < a _ { k k } + a _ { j j } .
$$

Equations (6.10) and (6.11) imply that for each $k \neq j$ ，

$$
| a _ { k j } | < \frac { a _ { k k } + a _ { j j } } { 2 } \leq \operatorname* { m a x } _ { 1 \leq i \leq n } | a _ { i i } | , \quad \mathrm { s o } \quad \operatorname* { m a x } _ { 1 \leq k , j \leq n } | a _ { k j } | \leq \operatorname* { m a x } _ { 1 \leq i \leq n } | a _ { i i } | .
$$

d.For $i \neq j$ ,define ${ \bf x } = ( x _ { k } )$ by

$$
x _ { k } = \left\{ { \begin{array} { l l } { 0 , } & { { \mathrm { i f ~ } } k \neq j { \mathrm { ~ a n d ~ } } k \neq i , } \\ { \alpha , } & { { \mathrm { i f ~ } } k = i , } \\ { 1 , } & { { \mathrm { i f ~ } } k = j , } \end{array} } \right.
$$

where $\alpha$ represents an arbitrary real number. Since $\mathbf { x } \neq \mathbf { 0 }$ ，

$$
0 < { \bf x } ^ { t } A { \bf x } = a _ { i i } \alpha ^ { 2 } + 2 a _ { i j } \alpha + a _ { j j } .
$$

As a quadratic polynomial in $\pmb { \alpha }$ with no real roots, the discriminant of $P ( \alpha ) =$ $a _ { i i } \alpha ^ { 2 } + 2 a _ { i j } \alpha + a _ { j j }$ must be negative. Thus,

$$
4 a _ { i j } ^ { 2 } - 4 a _ { i i } a _ { j j } < 0 \quad \mathrm { a n d } \quad a _ { i j } ^ { 2 } < a _ { i i } a _ { j j } .
$$

Although Theorem 6.21 provides some important conditions that must be true of positive definite matrices,it does not ensure that a matrix satisfying these conditions is positive definite.

The following notion will be used to provide a necessary and sufficient condition.

lefinition 6.22A leading principal submatrix of a matrix A is a matrix of the form

$$
A _ { k } = \left[ \begin{array} { c c c c } { a _ { 1 1 } } & { a _ { 1 2 } } & { \ldots } & { a _ { 1 k } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \ldots } & { a _ { 2 k } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { a _ { k 1 } } & { a _ { k 2 } } & { \ldots } & { a _ { k k } } \end{array} \right] ,
$$

for some $1 \leq k \leq n$ ，

A proof of the following result can be found in [Stew1, p. 250].

# Theorem 6.23

A symmetric matrix $A$ is positive definite if and only if each of its leading principal submatrices has a positive determinant. ■

# EXAMPLE 3

In Example 2 we used the definition to show that the symmetric matrix

$$
A = \left[ { \begin{array} { r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} } \right]
$$

is positive definite.To confirm this using Theorem 6.23 note that

$$
\operatorname* { d e t } A _ { 2 } = \operatorname* { d e t } { \left[ { \begin{array} { r r } { 2 } & { - 1 } \\ { - 1 } & { 2 } \end{array} } \right] } = 4 - 1 = 3 > 0 ,
$$

and

$$
\operatorname* { d e t } A _ { 3 } = \operatorname* { d e t } { \left[ \begin{array} { r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } \\ { 0 } & { - 1 } & { 2 } \end{array} \right] } = 2 \operatorname* { d e t } { \left[ \begin{array} { r r } { 2 } & { - 1 } \\ { - 1 } & { 2 } \end{array} \right] } - ( - 1 ) \operatorname* { d e t } { \left[ \begin{array} { r r } { - 1 } & { - 1 } \\ { 0 } & { 2 } \end{array} \right] }
$$

$$
= 2 ( 4 - 1 ) + ( - 2 + 0 ) = 4 > 0 .
$$

The Maple command >definite(A,positive_def);

returns true or false as an indication of positive definiteness. Consistent with our definition, symmetry is required for a true result.

The next result extends part (a) of Theorem 6.21 and parallels the strictly diagonally dominant results presented in Theorem 6.19.We will not give a proof of this theorem since it requires introducing terminology and results that are not needed for any other purpose. The development and proof can be found in [We, pp. 120 ff].

# Theorem 6.24

The symmetric matrix A is positive definite if and only if Gaussian elimination without row interchanges can be performed on the linear system $\mathbf { A } \mathbf { x } = \mathbf { b }$ with all pivot elements positive. Moreover, in this case,the computations are stable with respect to the growth of roundoff errors. ■

Some interesting facts that are uncovered in constructing the proof of Theorem 6.24 are presented in the following corollaries.

# Corollary 6.25

The matrix $A$ is positive definite if and only if $A$ can be factored in the form $L D L ^ { t }$ , where $L$ is lower triangular with 1's on its diagonal and $D$ is a diagonal matrix with positive diagonal entries.

# Corollary 6.26

The matrix A is positive definite if and only if A can be factored in the form $L L ^ { t }$ , where $L$ is lower triangular with nonzero diagonal entries. ■

The matrix $L$ in Corollary 6.26 is not the same as the matrix in Corollary 6.25.A relationship between them is presented in Exercise 26.

Algorithm 6.5 is based on the $L U$ Factorization Algorithm 6.4 and obtains the $L D L ^ { t }$ factorization described in Corollary 6.25.

# LDL' Factorization

To factor the positive definite $n \times n$ matrix $\pmb { A }$ into the form $L D L ^ { t }$ ， where $L$ is a lower triangular matrix with 1's along the diagonal and $D$ is a diagonal matrix with positive entries on the diagonal:

INPUTthe dimension $\pmb { n }$ ; entries $a _ { i j }$ ,for $1 \leq i , j \leq n$ of $A$

OUTPUT the entries $l _ { i j }$ ,for $1 \le j < i$ and $1 \leq i \leq n$ of $L$ ,and $d _ { i }$ ,for $1 \leq i \leq n$ of $D$

Step 1 For $i = 1 , \ldots , n$ do Steps 2-4.

Step 2 For $j = 1 , \dots , i - 1$ ,set $v _ { j } = l _ { i j } d _ { j }$ ·

Step 3 Set $\begin{array} { r } { d _ { i } = a _ { i i } - \sum _ { j = 1 } ^ { i - 1 } l _ { i j } \boldsymbol { v } _ { j } } \end{array}$

Step 4 For $\begin{array} { r } { \cdot \ j = i + 1 , \ldots , n \ \mathrm { s e t } l _ { j i } = ( a _ { j i } - \sum _ { k = 1 } ^ { i - 1 } l _ { j k } v _ { k } ) / d _ { i } . } \end{array}$

Step5OUTPUT $( l _ { i j }$ for $j = 1 , \dots , i - 1 \mathrm { a n d } i = 1 , \dots , n )$ OUTPUT $( d _ { i }$ for $i = 1 , \ldots , n )$ ； STOP.

Corollary 6.25 has a counterpart when $A$ is symmetric but not necessarily positive definite. This result is widely applied since symmetric matrices are common and easily recognized.

# Corollary 6.27

Let A be a symmetric $n \times n$ matrix for which Gaussian elimination can be applied without $A$ $L D L ^ { t }$ $L$ $D$ $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { n n } ^ { ( n ) }$

Algorithm 6.5 is easily modified to factor the symmetric matrices described in Corollary 6.27. It simply requires adding a check to ensure that the diagonal elements are nonzero. Choleski's Algorithm 6.6 produces the $L L ^ { t }$ factorization described in Corollary 6.26.

# Choleski's

To factor the positive definite $n \times n$ matrix $\pmb { A }$ into $L L ^ { t }$ ，where $L$ is lower triangular:

INPUT the dimension $n$ ; entries $a _ { i j }$ ,for $1 \leq i$ ， $j \le n$ of $A$

OUTPUT the entries $l _ { i j }$ ,for $1 \le j \le i$ and $1 \leq i \leq n$ of $L$ . (The entries of $U = L ^ { t }$ are$u _ { i j } = l _ { j i }$ ， $f o r i \leq j \leq n$ and $1 \leq i \leq n .$ ）

Step 1 Set $l _ { 1 1 } = \sqrt { a _ { 1 1 } }$

Step 2 For $j = 2 , \ldots , n , \sec l _ { j 1 } = a _ { j 1 } / l _ { 1 1 } .$

Step 3 For $i = 2 , \ldots , n - 1$ do Steps 4 and 5.

$$
\begin{array} { r } { { \sf S t e p 4 } \quad { \sf S e t } l _ { i i } = \Big ( a _ { i i } - \sum _ { k = 1 } ^ { i - 1 } l _ { i k } ^ { 2 } \Big ) ^ { 1 / 2 } . } \end{array}
$$

Step 5For $j = i + 1 , \ldots , n$

Step 6 Set $\begin{array} { r } { l _ { n n } = \left( a _ { n n } - \sum _ { k = 1 } ^ { n - 1 } l _ { n k } ^ { 2 } \right) ^ { 1 / 2 } } \end{array}$

Step 7OUTPUT $( l _ { i j }$ for $j = 1 , \dots , i$ and $i = 1 , \ldots , n )$ ； STOP.

The Choleski factorization of A is computed in Maple using the statement >L:=cholesky(A);

# EXAMPLE 4

The matrix

$$
A = \left[ { \begin{array} { r r r } { 4 } & { - 1 } & { 1 } \\ { - 1 } & { 4 . 2 5 } & { 2 . 7 5 } \\ { 1 } & { 2 . 7 5 } & { 3 . 5 } \end{array} } \right]
$$

is positive definite. The factorization LDL' of A given in Algorithm 6.5 is

$$
A = L D L ^ { t } = \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { - 0 . 2 5 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 7 5 } & { 1 } \end{array} \right] \left[ \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 4 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { l l l } { 1 } & { - 0 . 2 5 } & { 0 . 2 5 } \\ { 0 } & { 1 } & { 0 . 7 5 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] .
$$

and Choleski's Algorithm 6.6 produces the factorization

$$
A = L L ^ { t } = { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { - 0 . 5 } & { 2 } & { 0 } \\ { 0 . 5 } & { 1 . 5 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { 2 } & { - 0 . 5 } & { 0 . 5 } \\ { 0 } & { 2 } & { 1 . 5 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } .
$$

The $L D L ^ { t }$ factorization described in Algorithm 6.5 requires $n ^ { 3 } / 6 + n ^ { 2 } - 7 n / 6$ multiplications/divisions and n³/6 -n/6 additions/subtractions. The LL' Choleski factorization of a positive definite matrix requires only n³/6 + n²/2 - 2n/3 multiplications/divisions and n³/6 -n/6 additions/subtractions. The computational advantage of Choleski's factorization is misleading, however, since it requires extracting n square roots. However, the number of operations required for computing the n square roots is a linear factor of n and will decrease in significance as $\pmb { n }$ increases.

Algorithm 6.5 provides a stable method for factoring a positive definite matrix into the form A = LDL',but it must be modified to solve the linear system Ax = b. To do this, we delete the STOP statement from Step 5 in the algorithm and add the following steps to solve the lower triangular system $L \mathbf { y } = \mathbf { b }$ ：

Step 6 Set $y _ { 1 } = b _ { 1 }$

$$
\begin{array} { r } { { \cal S t e p 7 } \quad \mathrm { F o r } i = 2 , \dots , n \mathrm { \ s e t \ y } _ { i } = b _ { i } - \sum _ { j = 1 } ^ { i - 1 } l _ { i j } y _ { j } . } \end{array}
$$

The linear system $D \mathbf { z } = \mathbf { y }$ can then be solved by

$$
{ \mathit { S t e p } } \ \delta { \mathrm {  ~ \ F o r ~ } } i = 1 , \ldots , n { \mathrm { \ s e t ~ } } z _ { i } = y _ { i } / d _ { i } .
$$

Finally, the upper-triangular system $L ^ { t } \mathbf { X } = \mathbf { Z }$ is solved with the steps given by

Step 9 Set $x _ { n } = z _ { n }$

Step 10 $\begin{array} { r } { \mathrm { F o r } i = n - 1 , \ldots , 1 \mathrm { ~ s e t } x _ { i } = z _ { i } - \sum _ { j = i + 1 } ^ { n } l _ { j i } x _ { j } . } \end{array}$

Step 11 OUTPUT ( $\cdot \boldsymbol { x } _ { i }$ for $i = 1 , \ldots , n )$ ； STOP.

The additional operations required to solve the linear system are shown in Table 6.3.

# Table 6.3

<table><tr><td>Step</td><td>Multiplications/Divisions</td><td>Additions/Subtractions</td></tr><tr><td>6</td><td>0</td><td>0</td></tr><tr><td>7</td><td>n(n-1)/2</td><td>n(n -1)/2</td></tr><tr><td>8</td><td>n</td><td>0</td></tr><tr><td>9</td><td>0</td><td>0</td></tr><tr><td>10</td><td>n(n-1)/2</td><td>n(n-1)/2</td></tr><tr><td>Total</td><td>n2</td><td>n²-n</td></tr></table>

If the Choleski factorization given in Algorithm 6.6 is preferred,the additional steps for solving the system $\pmb { A } \mathbf { x } = \mathbf { b }$ are as follows. First delete the STOP statement from Step 7. Then add

Step 8 Set $y _ { 1 } = b _ { 1 } / l _ { 1 1 }$   
Step 9 $\begin{array} { r } { \mathrm { F o r } i = 2 , \dots , n \mathrm { ~ s e t ~ } y _ { i } = \left( b _ { i } - \sum _ { j = 1 } ^ { i - 1 } l _ { i j } y _ { j } \right) \bigg / l _ { i i } . } \end{array}$   
Step 10 Set $x _ { n } = y _ { n } / l _ { n n }$   
Step 11 Fo $\begin{array} { r } { \mathrm { ~ r ~ } i = n - 1 , \dotsc , 1 \dotsc , 1 \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc \dotsc . } \end{array} ,$ Step 12 OUTPUT $( x _ { i } ~ \mathrm { f o r } ~ i = 1 , \dots , n )$ ；   
STOP.

Steps 8-12 require $n ^ { 2 } + n$ multiplications/divisions and $n ^ { 2 } - n$ additions/ subtractions.

The last class of matrices considered are calld band matrices. In most applications the band matrices are also strictly diagonally dominant or positive definite.

An $n \times n$ matrix is called a band matrix if integers $p$ and $q$ ,with $1 < p , q < n$ ,exist with the property that $a _ { i j } = 0$ whenever $i + p \le j$ or $j + q \le i$ . The bandwidth of a band matrix is defined as $w = p + q - 1$ ·

For example, the matrix

$$
A = \left[ { \begin{array} { r r r } { 7 } & { 2 } & { 0 } \\ { 3 } & { 5 } & { - 1 } \\ { 0 } & { - 5 } & { - 6 } \end{array} } \right]
$$

is a band matrix with $p = q = 2$ and bandwidth $2 + 2 - 1 = 3$

The definition of band matrix forces those matrices to concentrate all their nonzero entries about the diagonal. Two special cases of band matrices that occur frequently have $p = q = 2$ and $p = q = 4$

Matrices of bandwidth 3, occurring when $p = q = 2$ ， are called tridiagonal since they have the form

$$
A = \left[ \begin{array} { l l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { 0 { : } \cdots { } } & { \cdots { } } & { \cdots { } } & { \cdots { } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } & { \ddots } & { } & { \vdots } \\ { 0 } & { a _ { 3 2 } } & { a _ { 3 3 } } & { a _ { 3 4 } } & { \ddots } & { } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { } \\ { \vdots } & { \qquad \ddots } & { \ddots } & { \ddots } & { \ddots } & { } \\ { \vdots } & { \qquad \ddots } & { \ddots } & { \ddots } & { \ddots } & { a _ { n - 1 , n } } \\ { \vdots } & { \qquad \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } \\ { 0 } & { \cdots } & { \cdots } & { \cdots } & { \ddots } & { a _ { n , n - 1 } } & { \ddots } \end{array} \right] .
$$

Tridiagonal matrices are also considered in Chapter 11 in connection with the study of piecewise linear approximations to boundary-value problems. The case of $p = q = 4$ will be used for the solution of boundary-value problems when the approximating functions assume the form of cubic splines.

The factorization algorithms can be simplified considerably in the case of band matrices because a large number of zeros appear in these matrices in regular patterns. It is particularly interesting to observe the form the Crout or Doolittle method assumes in this case.

To illustrate the situation, suppose a tridiagonal matrix A can be factored into the triangular matrices $L$ and $U$ . Since $A$ has only $( 3 n \textrm { -- } 2 )$ nonzero entries,there are only $( 3 n - 2 )$ conditions to be applied to determine the entries of $L$ and $U$ , provided, of course, that the zero entries of $A$ are also obtained. Suppose that the matrices can be found in the form

$$
L = \left[ \begin{array} { l l l l } { l _ { 1 1 } } & { 0 ; \cdots } & { \cdots } & { \cdots } & { \cdots } \\ { l _ { 2 1 } } & { l _ { 2 2 } } & { \vdots } & { \vdots } \\ { 0 } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { 0 } & { \cdots } & { \ddots } & { l _ { n , n - 1 } } & { l _ { n n } } \end{array} \right] \quad \mathrm { a n d } \quad U = \left[ \begin{array} { l l l l } { 1 } & { u _ { 1 2 } } & { 0 ; \cdots } & { \cdots } & { \cdots } \\ { 0 } & { 1 } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } \\ { \partial } & { \cdots } & { \cdots } & { \ddots } & { 1 } \end{array} \right] .
$$

There are $( 2 n - 1 )$ undetermined entries of $L$ and $( n - 1 )$ undetermined entries of $U$ , which totals the number of condition, $( 3 n - 2 )$ . The O entries of $A$ are obtained automatically.

The multiplication involved with $A = L U$ gives,in addition to the O entries,

$$
\begin{array} { r } { \begin{array} { r l } & { a _ { 1 1 } = l _ { 1 1 } ; } \\ & { a _ { i , i - 1 } = l _ { i , i - 1 } , \quad \mathrm { f o r } \operatorname { e a c h } i = 2 , 3 , \ldots , n ; } \\ & { \quad a _ { i i } = l _ { i , i - 1 } u _ { i - 1 , i } + l _ { i i } , \quad \mathrm { f o r } \operatorname { e a c h } i = 2 , 3 , \ldots , n ; } \end{array} } \end{array}
$$

and

$$
a _ { i , i + 1 } = l _ { i i } u _ { i , i + 1 } , \quad { \mathrm { f o r } } \operatorname { e a c h } i = 1 , 2 , \dots , n - 1 .
$$

A solution to this system is found by first using Eq. (6.12) to obtain allthe nonzero off-diagonal terms in $L$ and then using Eqs.(6.13） and (6.14) to alternately obtain the remainder of the entries in $U$ and $L$ . These can be stored in the corresponding entries of $A$

Algorithm 6.7 solves an $n \times n$ system of linear equations whose coefficient matrix is tridiagonal. This algorithm requires only $( 5 n - 4 )$ multiplications/divisions and $( 3 n - 3 )$ additions/subtractions. Consequently, it has considerable computational advantage over the methods that do not consider the tridiagonality of the matrix.

# Crout Factorization for Tridiagonal Linear Systems

To solve the $n \times n$ linear system

$$
\begin{array} { c c c c } { { E _ { 1 } : } } & { { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } } } & { { = } } & { { a _ { 1 , n + 1 } , } } \\ { { E _ { 2 } : } } & { { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + a _ { 2 3 } x _ { 3 } } } & { { = } } & { { a _ { 2 , n + 1 } , } } \\ { { } } & { { } } & { { \vdots } } & { { \vdots } } \\ { { E _ { n - 1 } : } } & { { a _ { n - 1 , n - 2 } x _ { n - 2 } + a _ { n - 1 , n - 1 } x _ { n - 1 } + a _ { n - 1 , n } x _ { n } = a _ { n - 1 , n + 1 } , } } & { { } } \\ { { E _ { n } : } } & { { } } & { { a _ { n , n - 1 } x _ { n - 1 } } } & { { + a _ { n n } x _ { n } } } & { { = a _ { n , n + 1 } , } } \end{array}
$$

which is assumed to have a unique solution:

INPUT the dimension $\pmb { n }$ ; the entries of $\pmb { A }$

OUTPUT the solution $x _ { 1 } , \ldots , x _ { n }$

(Steps 1-3 set up and solve $\pmb { L } \pmb { z = } \mathbf { b } ,$ ）

Step 1 Set $l _ { 1 1 } = a _ { 1 1 }$ ；$\begin{array} { l } { { u _ { 1 2 } = a _ { 1 2 } / l _ { 1 1 } ; } } \\ { { z _ { 1 } = a _ { 1 , n + 1 } / l _ { 1 1 } . } } \end{array}$

Step2 Fori=2,...,n-1s

$$
\begin{array} { r l } & { \mathsf { s e t } l _ { i , i - 1 } = a _ { i , i - 1 } ; ~ ( i t h ~ r o w ~ o f L . ) } \\ & { ~ l _ { i i } = a _ { i i } - l _ { i , i - 1 } u _ { i - 1 , i } ; } \\ & { ~ u _ { i , i + 1 } = a _ { i , i + 1 } / l _ { i i } ; ~ ( ( i + 1 ) t h ~ c o l u m n ~ o f U . ) } \\ & { ~ z _ { i } = ( a _ { i , n + 1 } - l _ { i , i - 1 } z _ { i - 1 } ) / l _ { i i } . } \end{array}
$$

Step 3 Set $l _ { n , n - 1 } = a _ { n , n - 1 }$ ; (nth row of L.)

$$
\begin{array} { l } { { l _ { n n } = a _ { n n } - l _ { n , n - 1 } u _ { n - 1 , n } . } } \\ { { z _ { n } = ( a _ { n , n + 1 } - l _ { n , n - 1 } z _ { n - 1 } ) / l _ { n n } . } } \end{array}
$$

(Steps 4 and 5 solve $U \mathbf { X } = \mathbf { L } .$ ）

Step 4 Set $x _ { n } = z _ { n }$

Step 5 Fori = n - 1,..,1 set $x _ { i } = z _ { i } - u _ { i , i + 1 } x _ { i + 1 }$

Step 6OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ； STOP.

To ilustrate the procedure fortridiagonal matrices,considerthetridiagonal systemof equations

$$
\begin{array} { r l r } & { } & { 2 x _ { 1 } - x _ { 2 } \qquad = 1 , } \\ & { } & { - x _ { 1 } + 2 x _ { 2 } - x _ { 3 } \qquad = 0 , } \\ & { } & { - x _ { 2 } + 2 x _ { 3 } - x _ { 4 } = 0 , } \\ & { } & { - x _ { 3 } + 2 x _ { 4 } = 1 , } \end{array}
$$

whose augmented matrix is

$$
\left[ { \begin{array} { r r r r r r } { 2 } & { - 1 } & { 0 } & { 0 } & { \vdots } & { 1 } \\ { - 1 } & { 2 } & { - 1 } & { 0 } & { \vdots } & { 0 } \\ { 0 } & { - 1 } & { 2 } & { - 1 } & { \vdots } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { 2 } & { \vdots } & { 1 } \end{array} } \right] .
$$

The Crout Factorization Algorithm produces the factorization

$$
\left[ { \begin{array} { r r r r r } { 2 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 2 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 2 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { 2 } \end{array} } \right] = \left[ { \begin{array} { r r r r } { 2 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { { \frac { 3 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { { \frac { 4 } { 3 } } } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { { \frac { 5 } { 4 } } } \end{array} } \right] \left[ { \begin{array} { r r r r } { 1 } & { - { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 1 } & { - { \frac { 2 } { 3 } } } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - { \frac { 3 } { 4 } } } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right] = L U .
$$

Solving the system $L \mathbf { z } = \mathbf { b }$ gives $\begin{array} { r } { \mathbf { z } = \left( \frac { 1 } { 2 } , \frac { 1 } { 3 } , \frac { 1 } { 4 } , 1 \right) ^ { t } } \end{array}$ , and the solution of $U \mathbf { x } = \mathbf { z }$ is ${ \bf x } =$ $( 1 , 1 , 1 , 1 ) ^ { t }$

The Crout Factorization Algorithm can be applied whenever $l _ { i i } \neq 0$ for each $i =$ $1 , 2 , \ldots , n$ .Two conditions, either of which ensure that this is true,are that the coeficient matrix of the system is positive definite or that it is strictly diagonally dominant. An additional condition that ensures this algorithm can be applied is given in the next theorem, whose proof is discussed in Exercise 22.

# Theorem 6.29

Suppose that $A = ( a _ { i j } )$ is tridiagonal with $a _ { i , i - 1 } a _ { i , i + 1 } \neq 0$ ,for each $i = 2 , 3 , \ldots , n - 1$ .If $| a _ { 1 1 } | > | a _ { 1 2 } |$ ， $\lvert a _ { i i } \rvert \geq \lvert a _ { i , i - 1 } \rvert + \lvert a _ { i , i + 1 } \rvert$ , for each $i = 2 , 3 , \ldots , n - 1$ , and $\left| a _ { n n } \right| > \left| a _ { n , n - 1 } \right| .$ ， then $A$ is nonsingular and the values of $l _ { i i }$ described in the Crout Factorization Algorithm are nonzero for each $i = 1 , 2 , \dots , n$ ■

# ExErcIse Set 6.6

1. Determine which ofthe following matrices are (i) symmetric,(ii)singular,(ii)strictly diagonally dominant, (iv) positive definite.

$\begin{array} { r l } { \mathfrak { a } . \ } & { { } \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 3 } \end{array} \right] } \\ { \mathfrak { c } . \ } & { { } \left[ \begin{array} { l l l } { 2 } & { 1 } & { 0 } \\ { 0 } & { 3 } & { 0 } \\ { 1 } & { 0 } & { 4 } \end{array} \right] } \end{array}$ $\begin{array} { r l } { \mathbf { b } . } & { { } \left[ \begin{array} { l l } { - 2 } & { 1 } \\ { 1 } & { - 3 } \end{array} \right] } \\ { \mathbf { d } . } & { { } \left[ \begin{array} { l l l } { 2 } & { 1 } & { 0 } \\ { 0 } & { 3 } & { 2 } \\ { 1 } & { 2 } & { 4 } \end{array} \right] } \end{array}$

$\begin{array} { r l } { \mathrm { e . } \quad } & { { } \left[ \begin{array} { c c c } { 4 } & { 2 } & { 6 } \\ { 3 } & { 0 } & { 7 } \\ { - 2 } & { - 1 } & { - 3 } \end{array} \right] } \end{array}$ $\begin{array} { r l } { \mathbf { f } . } & { { } \left[ { \begin{array} { r r r r } { 2 } & { - 1 } & { 0 } \\ { - 1 } & { 4 } & { 2 } \\ { 0 } & { 2 } & { 2 } \end{array} } \right] } \\ { \mathbf { h } . } & { { } \left[ { \begin{array} { r r r r } { 2 } & { 3 } & { 1 } & { 2 } \\ { - 2 } & { 4 } & { - 1 } & { 5 } \\ { 3 } & { 7 } & { 1 . 5 } & { 1 } \\ { 6 } & { - 9 } & { 3 } & { 7 } \end{array} } \right] } \end{array}$ $\mathbf { g } . \quad \left[ \begin{array} { l l l l } { 4 } & { 0 } & { 0 } & { 0 } \\ { 6 } & { 7 } & { 0 } & { 0 } \\ { 9 } & { 1 1 } & { 1 } & { 0 } \\ { 5 } & { 4 } & { 1 } & { 1 } \end{array} \right]$

2. Use the $L D L ^ { t }$ Factorization Algorithm to find a factorizaton of the form $A = L D L ^ { \prime }$ for the following matrices:

$$
\begin{array} { c c } { { A = \left[ \begin{array} { c c c } { { 2 } } & { { - 1 } } & { { 0 } } \\ { { - 1 } } & { { 2 } } & { { - 1 } } \\ { { 0 } } & { { - 1 } } & { { 2 } } \end{array} \right] } } & { { \qquad \mathbf { b . } \quad A = \left[ \begin{array} { c c c } { { 4 } } & { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { 3 } } & { { - 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } & { { 2 } } & { { 0 } } \\ { { 1 } } & { { 1 } } & { { 0 } } & { { 2 } } \end{array} \right] } } \\ { { A = \left[ \begin{array} { c c c } { { 4 } } & { { 1 } } & { { - 1 } } & { { 0 } } \\ { { 1 } } & { { 3 } } & { { - 1 } } & { { 0 } } \\ { { - 1 } } & { { - 1 } } & { { 5 } } & { { 2 } } \\ { { 0 } } & { { 0 } } & { { 2 } } & { { 4 } } \end{array} \right] } } & { { \qquad \mathbf { d . } \quad A = \left[ \begin{array} { c c c } { { 6 } } & { { 2 } } & { { 1 } } & { { - 1 } } \\ { { 2 } } & { { 4 } } & { { 1 } } & { { 0 } } \\ { { 1 } } & { { 1 } } & { { 4 } } & { { - 1 } } \\ { { - 1 } } & { { 0 } } & { { - 1 } } & { { 3 } } \end{array} \right] } } \end{array}
$$

3.Use Choleski's Algorithm to find a factorization of the form $A = L L ^ { t }$ for the matrices in Exercise 2.

4. Modify the $L D L ^ { t }$ Factorization Algorithm as suggested in the text so that it can be used to solve linear systems. Use the modified algorithm to solve the following linear systems.

a. $\begin{array} { c c } { { 2 x _ { 1 } - x _ { 2 } } } & { { = 3 , } } \\ { { } } & { { - x _ { 1 } + 2 x _ { 2 } - x _ { 3 } = - 3 , } } \\ { { } } & { { - \ x _ { 2 } + 2 x _ { 3 } = 1 . } } \end{array}$ b. $\begin{array} { r l } { { 4 } x _ { 1 } + } & { x _ { 2 } + } & { x _ { 3 } + } \\ { } & { x _ { 1 } + 3 x _ { 2 } - } & { x _ { 3 } + } \\ { } & { x _ { 1 } - } & { x _ { 2 } + 2 x _ { 3 } \qquad = 0 , } \\ { } & { x _ { 1 } + } & { x _ { 2 } \qquad + 2 x _ { 4 } = 0 . 5 . } \end{array}$

$$
\begin{array} { r l } { { 4 } x _ { 1 } + ~ x _ { 2 } - ~ x _ { 3 } ~ } & { { } = 7 , } \\ { ~ x _ { 1 } + 3 x _ { 2 } - ~ x _ { 3 } ~ } & { { } = 8 , } \\ { { } - x _ { 1 } - ~ x _ { 2 } + 5 x _ { 3 } + 2 x _ { 4 } = - 4 , } & { { } } \\ { { } 2 x _ { 3 } + 4 x _ { 4 } = 6 . } & { { } \quad - x _ { 1 } ~ - ~ x _ { 3 } + 3 x _ { 4 } = - 2 . } \end{array}
$$

5. Modify Choleski's Algorithm as suggested in the text so that it can be used to solve linear systems,and use the modified algorithm to solve the linear systems in Exercise 4.

6.Use Crout factorization for tridiagonal systems to solve the folowing linear systems.

a. ${ \begin{array} { r l } { x _ { 1 } - } & { x _ { 2 } \qquad = 0 , } \\ { - 2 x _ { 1 } + 4 x _ { 2 } - 2 x _ { 3 } = - 1 , } \\ { - } & { x _ { 2 } + 2 x _ { 3 } = 1 . 5 . } \end{array} }$ b $\begin{array} { c } { 3 x _ { 1 } + { \ x } _ { 2 } \qquad = - 1 , } \\ { 2 x _ { 1 } + 4 x _ { 2 } + { \ x } _ { 3 } = 7 , } \\ { 2 x _ { 2 } + 5 x _ { 3 } = 9 . } \end{array}$ c. $\begin{array} { c c } { { 2 x _ { 1 } - x _ { 2 } } } & { { = 3 , } } \\ { { } } & { { - x _ { 1 } + 2 x _ { 2 } - x _ { 3 } = - 3 , } } \\ { { } } & { { } } \\ { { - } } & { { x _ { 2 } + 2 x _ { 3 } = 1 . } } \end{array}$

$$
\begin{array} { r l r } { 0 . 5 x _ { 1 } + 0 . 2 5 x _ { 2 } } & { } & { = 0 . 3 5 , } \\ { 0 . 3 5 x _ { 1 } + \ 0 . 8 x _ { 2 } + 0 . 4 x _ { 3 } } & { = 0 . 7 7 , } \\ { 0 . 2 5 x _ { 2 } + } & { } & { x _ { 3 } + 0 . 5 x _ { 4 } = - 0 . 5 , } \\ & { } & { x _ { 3 } - \ 2 x _ { 4 } = - 2 . 2 5 . } \end{array}
$$

7.Let $A$ be the $1 0 \times 1 0$ tridiagonal matrix given by $a _ { i i } = 2 , a _ { i , i + 1 } = a _ { i , i - 1 } = - 1$ ,for each $i = 2 , \ldots , 9$ , and $a _ { 1 1 } = a _ { 1 0 , 1 0 } = 2$ ， $a _ { \mathrm { 1 2 } } = a _ { \mathrm { 1 0 , 9 } } = - 1$ Let $\mathbf { b }$ be the ten-dimensional column vector given by $b _ { 1 } = b _ { 1 0 } = 1$ and $b _ { i } = 0$ ,for each $i = 2 , 3 , \dots , 9$ Solve $A \mathbf { x } = \mathbf { b }$ using the Crout factorization for tridiagonal systems.

8. Modify the $L D L ^ { t }$ factorization to factor a symmetric matrix A. [Note: The factorization may not always be possible.] Apply the new algorithm to the following matrices:

a. $A = { \left[ \begin{array} { r r r } { 3 } & { - 3 } & { 6 } \\ { - 3 } & { 2 } & { - 7 } \\ { 6 } & { - 7 } & { 1 3 } \end{array} \right] }$ $\mathbf { b . } \quad A = \left[ { \begin{array} { r r r } { 3 } & { - 6 } & { 9 } \\ { - 6 } & { 1 4 } & { - 2 0 } \\ { 9 } & { - 2 0 } & { 2 9 } \end{array} } \right]$   
c. $A = \left[ { \begin{array} { r r r r } { - 1 } & { 2 } & { 0 } & { 1 } \\ { 2 } & { - 3 } & { 2 } & { - 1 } \\ { 0 } & { 2 } & { 5 } & { 6 } \\ { 1 } & { - 1 } & { 6 } & { 1 2 } \end{array} } \right]$ $\mathbf { d . } \quad A = \left[ { \begin{array} { r r r r r } { 2 } & { - 2 } & { 4 } & { - 4 } \\ { - 2 } & { 3 } & { - 4 } & { 5 } \\ { 4 } & { - 4 } & { 1 0 } & { - 1 0 } \\ { - 4 } & { 5 } & { - 1 0 } & { 1 4 } \end{array} } \right]$

9.Which of the symmetric matrices in Exercise 8 are positive definite?

10.Find $\pmb { \alpha }$ so that $A = { \left[ \begin{array} { l l l } { \alpha } & { 1 } & { - 1 } \\ { 1 } & { 2 } & { 1 } \\ { - 1 } & { 1 } & { 4 } \end{array} \right] } { \mathrm { i s ~ p o s i t i v e ~ d e f i n i t e } } .$

11.Find $\alpha$ so that $A = \left[ { \begin{array} { r r r } { 2 } & { \alpha } & { - 1 } \\ { \alpha } & { 2 } & { 1 } \\ { - 1 } & { 1 } & { 4 } \end{array} } \right]$ is positive definite.

12.Find $\pmb { \alpha }$ and $\beta > 0$ so that the matrix

$$
A = { \left[ \begin{array} { l l l } { 4 } & { \alpha } & { 1 } \\ { 2 \beta } & { 5 } & { 4 } \\ { \beta } & { 2 } & { \alpha } \end{array} \right] }
$$

is strictly diagonally dominant.

13.Find $\alpha > 0$ and $\beta > 0$ so that the matrix

$$
A = { \left[ \begin{array} { l l l } { 3 } & { 2 } & { \beta } \\ { \alpha } & { 5 } & { \beta } \\ { 2 } & { 1 } & { \alpha } \end{array} \right] }
$$

is strictly diagonally dominant.

14.Suppose that $A$ and $B$ are strictly diagonally dominant $n \times n$ matrices.

a. Is -A strictly diagonally dominant? b. Is $A ^ { t }$ strictly diagonally dominant? c. Is $A + B$ strictly diagonally dominant? d. Is $A ^ { 2 }$ strictly diagonally dominant? e. Is $A - B$ strictly diagonally dominant?

15.Suppose that A and B are positive definite n × n matrices.

$\mathbf { a } _ { \mathbf { \delta } }$ Is -A positive definite? $\mathbf { \delta } _ { \mathbf { b } _ { \mathbf { \delta } } }$ Is $A ^ { t }$ positive definite? $\pmb { \mathbb { c } } _ { \pmb { \imath } }$ Is $A + B$ positive definite? $\mathbf { d } .$ Is $A ^ { 2 }$ positive definite? $\clubsuit .$ Is $A - B$ positive definite?

16.Let

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 1 } \\ { - 1 } & { 1 } & { \alpha } \end{array} } \right] .
$$

Find all values of $\pmb { \alpha }$ for which

a. A is singular.   
$\mathbf { { b } } .$ A is strictly diagonally dominant.   
c. A is symmetric.   
d. $\pmb { A }$ is positive definite.

17.Let

$$
A = \left[ { \begin{array} { l l l } { \alpha } & { 1 } & { 0 } \\ { \beta } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 2 } \end{array} } \right] .
$$

Find all values of $\pmb { \alpha }$ and $\beta$ for which

a. A is singular.   
b. $\pmb { A }$ is strictly diagonally dominant.   
c. A is symmetric.   
d. A is positive definite.

18.Suppose A and B commute, that is,AB = BA. Must A' and B' also commute?

19.Construct a matrix A that is nonsymmetric but for which xf Ax > O for all x / 0.

20. Show that Gaussian elimination can be performed on A without row interchanges if and only if all leading principal submatrices of A are nonsingular. [Hint: Partition each matrix in the equation

$$
\boldsymbol { A } ^ { ( k ) } = \boldsymbol { M } ^ { ( k - 1 ) } \boldsymbol { M } ^ { ( k - 2 ) } \cdot \cdot \cdot \boldsymbol { M } ^ { ( 1 ) } \boldsymbol { A }
$$

vertically between the kth and (k+1)st columns and horizontally between the kth and (k +1)st rows (see Exercise 10 of Section 6.3). Show that the nonsingularity of the leading principal submatrix of $\pmb { A }$ is equivalent to $a _ { k , k } ^ { ( k ) } \neq 0 . ]$ 1

21. Tridiagonal matrices are usually labeled by using the notation

$$
A = { \left[ \begin{array} { l l l l } { a _ { 1 } } & { c _ { 1 } } & { 0 { : } \cdots \cdots \cdot 0 } \\ { b _ { 2 } } & { a _ { 2 } } & { c _ { 2 } } & { \ddots } \\ { 0 } & { . } & { b _ { 3 } } & { . } \\ { \vdots } & { . } & { . } & { . } \\ { { \dot { 0 } } } & { . . . . } & { . } & { . } \end{array} \right] }
$$

to emphasize that it is not necessary to consider all the matrix entries. Rewrite the Crout Factorization Algorithm using this notation,and change the notation of the lij and uij in a similar manner.

22.Prove Theorem 6.29.[Hint: Show that $\left| u _ { i , i + 1 } \right| < 1$ , for each $i = 1 , 2 , \dots , n - 1$ ,and that $| l _ { i i } | > 0$ , for each $i = 1 , 2 , \dots , n$ . Deduce that det $A = \operatorname* { d e t } L \cdot \operatorname* { d e t } U \neq 0 . ]$

23. Suppose $V = 5 . 5$ volts in the lead example of this chapter. By reordering the equations, a tridiagonal linear system can be formed. Use the Crout Factorization Algorithm to find the solution of the modified system.

24.Construct the operation count for solving an $n \times n$ linear system using the Crout Factorization Algorithm.

25.In a paper by Dom and Burdick [DoB], it is reported that the average wing length that resulted from mating three mutant varieties of fruit flies (Drosophila melanogaster) can be expressed in the symmetric matrix form

$$
\begin{array} { r } { A = \left[ \begin{array} { c c c } { 1 . 5 9 } & { 1 . 6 9 } & { 2 . 1 3 } \\ { 1 . 6 9 } & { 1 . 3 1 } & { 1 . 7 2 } \\ { 2 . 1 3 } & { 1 . 7 2 } & { 1 . 8 5 } \end{array} \right] , } \end{array}
$$

where $a _ { i j }$ denotes the average wing length of an offspring resulting from the mating of a male of type $i$ with a female of type $j$

a. What physical significance is associated with the symmetry of this matrix? b.Is this matrix positive definite? If so, prove it; if not, find a nonzero vector $\mathbf { X }$ for which $\mathbf { x } ^ { t } A \mathbf { x } \leq 0$

26. Suppose that the positive definite matrix A has the Cholesky factorization $A = L L ^ { t }$ and also the factorization $\dot { \boldsymbol { A } } = \hat { L } \boldsymbol { D } \hat { L } ^ { t }$ ，where $D$ is the diagonal matrix with positive diagonal entries $d _ { 1 1 } , d _ { 2 2 } , \ldots , d _ { n n }$ .Let $D ^ { 1 / 2 }$ be the diagonal matrix with diagonal entries $\sqrt { d _ { 1 1 } } , \sqrt { d _ { 2 2 } } , . . . , \sqrt { d _ { n n } }$

a.Show that D = D1/2 D1/2. b.Show that $L = \hat { L } D ^ { 1 / 2 }$

# 6.7 Survey of Methods and Software

In this chapter we have looked at direct methods for solving linear systems. A linear system consists of $\pmb { n }$ equations in $\pmb { n }$ unknowns expressed in matrix notation as $A \mathbf { x } = \mathbf { b }$ . These techniques use a finite sequence of arithmetic operations to determine the exact solution of the system subject only to roundoff error. We found that the linear system $A \mathbf { x } = \mathbf { b }$ has a unique solution if and only if $A ^ { - 1 }$ exists, which is equivalent to det $A \neq 0$ . The solution of the linear system is the vector $\mathbf { x } = A ^ { - 1 } \mathbf { b }$

Pivoting techniques were introduced to minimize the effects of roundoff error, which can dominate the solution when using direct methods. We studied partial pivoting,scaled partial pivoting, and total pivoting. We recommend the partial or scaled partial pivoting methods for most problems since these decrease the effects of roundoff error without adding much extra computation. Total pivoting should be used if roundoff error is sus-pected to be large. In Section 7.4 we willsee some procedures for estimating this roundoff error.

Gaussian elimination with minor modifications was shown to yield a factorization of the matrix $\pmb { A }$ into $L U$ , where $L$ is lower triangular with 1's on the diagonal and $U$ is upper triangular. This process is called Doolitle factorization. Not all nonsingular matrices can be factored this way,but a permutation of the rows will always give a factorization of the form $P A = L U$ ，where $P$ is the permutation matrix used to rearrange the rows of $A$ The advantage of the factorization is that the work is reduced when solving linear systems $\pmb { A } \mathbf { x } = \mathbf { b }$ with the same coefficient matrix $A$ and different vectors b.

Factorizations take a simpler form when the matrix $A$ is positive definite.For example, the Choleski factorization has the form $A = L L ^ { t }$ ,where $L$ is lower triangular. A symmetric matrix that has an LU factorization can also be factored in the form $A = L D L ^ { t }$ ，where $D$ is diagonal and $L$ is lower triangular with 1's on the diagonal. With these factorizations, manipulations involving $A$ can be simplified. If $A$ is tridiagonal, the $L U$ factorization takes a particularly simple form,with $U$ having 1's on the main diagonal and Os elsewhere, except on the diagonal immediately above the main diagonal. In addition, $L$ has its only nonzero entries on the main diagonal and one diagonal below.

The direct methods are the methods of choice for most linear systems. For tridiagonal, banded,and positive definite matrices,the special methods are recommended. For the general case, Gaussian elimination or $L U$ factorization methods, which allow pivoting,are recommended.In these cases,the effects of roundof error should be monitored.In Section 7.4 we discuss estimating errors in direct methods.

Large linear systems with primarily O entries occurring in regular patterns can be solved efficiently using an iterative procedure such as those discussed in Chapter 7. Sys-tems of this type arise naturally, for example, when finite-difference techniques are used to solve boundary-value problems,a common application in the numerical solution of partialdifferential equations.

It can be very difficult to solve a large linear system that has primarily nonzero entries or one where the O entries are not in a predictable pattern.The matrix associated with the system can be placed in secondary storage in partitioned form and portions read into main memory only as needed for calculation. Methods that require secondary storage can be either iterative or direct, but they generally require techniques from the fields of data structures and graph theory. The reader is referred to [BuR] and [RW] for a discussion of the current techniques.

The software for matrix operations and the direct solution of linear systems implemented in IMSL and NAG is based on LAPACK,a subroutine package in the public domain. There is excellent documentation available with it and from the books written about it. We will focus on several of the subroutines that are available in all three sources.

Accompanying LAPACK is a set of lower-level operations called Basic Linear Algebra Subprograms (BLAS). Level 1 of BLAS generally consists of vector-vector operations with input data and operation counts of $O ( n )$ . Level 2 consists of the matrix-vector opera-tions with input data and operation counts of $O ( n ^ { 2 } )$ . Level 3 consists of the matrix-matrix operations with input data and operation counts of $O ( n ^ { 3 } )$ . For example, in Level 1, the sub-routine SCOPY overwrites a vector y with a vector $\mathbf { x }$ ; SSCAL computes a scalar $a$ times a vector x; SAXPY adds a scalar $\pmb { a }$ times a vector $\pmb { \mathrm { x } }$ to a vector y $( \mathbf { y } = \mathbf { a } \cdot \mathbf { x } + \mathbf { y } )$ ; SDOT computes the inner, or scalar, product of two vectors; SNRM2 computes the Euclidean norm of a vector by a method similar to that discussed in Section 1.4; and ISAMAX computes the index of the vector component that gives the maximum absolute value of all the com-ponents. In Level 2, SGEMV computes the product of a matrix and a vector and in Level 3, SGEMM computes the product of a matrix and a matrix.

The subroutines in LAPACK for solving linear systems first factor the matrix $A$ . The factorization depends on the type of matrix in the following way:

1. General matrix $P A = L U$ ；   
2.Positive definite matrix $A = L L ^ { t }$ ；   
3. Symmetric matrix $A = L D L ^ { t }$   
4.Tridiagonal matrix $A = L U$ (in banded form).

The subroutine STRTRS solves a triangular linear system when the matrix is either upper or lower triangular.

The subroutine SGETRF factors $P A$ into $L U$ as a preliminary operation to the subroutine SGETRS,which then computes the solution to $A \mathbf { x } = \mathbf { b }$ . The subroutine SGETRI is used to construct the inverse of a matrix $A$ and to calculate the determinant of $A$ once $A$ has been factored via SGETRF.

The Choleski factorization of a positive definite matrix $A$ is obtained with the subroutine SPOTRF. The linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ can then be solved using the subroutine SPOTRS. Inverses and determinants of positive definite matrices,given the Choleski factorization, can be computed using SPOTRI. If $A$ is symmetric, the $L D L ^ { t }$ factorization is found using SSYTRF. Linear systems can then be solved using SSYTRS. If inverses or determinants are desired, SSYTRI can be used.

Many of the subroutines in LINPACK, and its successor LAPACK, can be implemented using MATLAB. A nonsingular matrix $A$ is factored using the command

$$
{ \begin{array} { r l } { [ L , U , P ] = l u ( A ) } \end{array} } 
$$

into the form $P A = L U$ , where $P$ is the permutation matrix defined by performing partial pivoting to solve a linear system involving $A$ . If the nonsingular matrix $A$ and the vector b have been defined in MATLAB, the command

$$
x = A \backslash b
$$

solves the linear system by first using the $P A = L U$ factoring command. Then it solves the lower-triangular system ${ \cal L } { \bf z } = { \bf b }$ for $\mathbf { z }$ using its command,

$$
z = L \backslash b
$$

This is followed by a solution to the upper-triangular system $U { \bf x } = { \bf z }$ using the command

$$
x = U \backslash z
$$

Other MATLAB commands include computing the inverse, transpose, and determinant of matrix $A$ by issuing the commands $i n v ( A ) , A ^ { \prime }$ , and det $( A )$ , respectively.

The IMSL Library includes counterparts to almost all the LAPACK subroutines and some extensions as wel. They are named with regard to the tasks tey perform as follows:

1. The first three letters of the name are used.

a. LSL: solves a linear system b. LFT: factors a coefficient matrix c. LFS: solves a linear system given factors from LFT d. LFD: calculates the determinants of given factors e. LIN: computes the inverse of given factors

2. The last two letters determine the type of matrix involved.

a. RG: real, general b. RT: real triangular c. DS: real positive definite d. SF: real symmetric e. RB: real banded

For example, the routine LFTDS factors a real positive definite matrix.

The NAG Library has many subroutines for direct methods of solving linear systems similar to those in LAPACK and IMSL. For example, the subroutine FO4AEF solves linear systems using Crout factorization. The subroutine FO4ATF solves a single linear system using Crout factorization,as in FO4AEF. The subroutine FO4EAF solves a single linear system where the matrix is real and tridiagonal, and FO4ASF solves a system when the matrix is real and positive definite. Inverse matrices can be computed by FO7AJF after using FO7ADF for an arbitrary real matrix and by FO1ABF if the matrix is positive definite.A determinant can be computed using FO3AAF.Factorizations can be obtained using F07ADF for the $L U$ factorization of a real matrix and using FO1LEF for a tridiagonal matrix.Linear systems can then be solved using FO7AEF. Choleski's factorization of a positive definite matrix can be obtained using FO7FDF,and a linear system can then be solved using FO7FEF. The NAG library also includes the lower-level matrix-vector manipulations.

Further information on the numerical solution of linear systems and matrices can be found in Golub and Van Loan [GV], Forsythe and Moler [FM], and Stewart [Stew1]. The use of direct techniques for solving large sparse systems is discussed in detail in George and Liu [GL] and in Pissanetzky [Pi]. Coleman and Van Loan [CV] consider the use of BLAS, LINPACK, and MATLAB.

# Iterative Techniques in Matrix Algebra

■.

bridge design, the individual members of the truss are connected with rotatable pin joints that permit forces to be transferred from one member of the truss to another. The accompanying figure shows a truss that is held stationary at the lower left endpoint $\textcircled{1}$ , is permitted to move horizontally at the lower right endpoint $\textcircled{4}$ ,and has pin joints at $\textcircled{1} , \textcircled{ 2 } , \textcircled{ 3 }$ ,and $\textcircled{4}$ A load of 10,000 newtons $( \mathbf { N } )$ is placed at the joint $\textcircled{3}$ , and the forces on the members of the truss have magnitudes given by $f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 }$ ,and $f _ { 5 } ,$ , as shown. The stationary support member has both a horizontal force ${ \pmb F } _ { 1 }$ and a vertical force $\pmb { F _ { 2 } } ,$ , but the movable support member has only the vertical force ${ \pmb F } _ { 3 }$ ·

![](images/abe6d0bbced409c39900b478849c131190a1969667d011697fa29c053fd6af31.jpg)

If the truss is in static equilibrium, the forces at each joint must add to the zero vector, so the sum of the horizontal and vertical components of the forces at each joint must be 0. This produces the system of liear equations shown in the accompanying table. An $\yen 8$ matrix describing this system has 46 zero entries and only 18 nonzero entries. Matrices with a high percentage of zero entries are called sparse and are often solved using iterative, rather than direct, techniques. The iterative solution to this system is considered in Exercise 18 of Section 7.3.

![](images/796040671f59d5976e15f6391c4ea1170711c7c746b5345690c459aa05b44a12.jpg)

<table><tr><td>Joint</td><td>Horizontal Component</td><td>Vertical Component</td></tr><tr><td>①</td><td>-F1+√fi+f=0</td><td>f-F2=0</td></tr><tr><td>?</td><td>-f+fA=0</td><td>-f-fs+fa=0</td></tr><tr><td>③</td><td>-f+ fs= 0</td><td>f-10,000 = 0</td></tr><tr><td>④</td><td>-fA-fs=0</td><td>2f4-F3=0</td></tr></table>

The methods presented in Chapter 6 used direct techniques to solve a system of $n \times n$ linear equations.of the form $\pmb { A } \mathbf { x } = \mathbf { b }$ . In this chapter, we present iterative methods to solve a system of this type.

# 7.1 Norms of Vectors and Matrices

In Chapter 2 we described iterative techniques for finding roots of equations of the form $f ( x ) = 0$ . An initial approximation (or approximations) was found,and new approximations were then determined based on how wel the previous approximations satisfied the equation. To discuss iterative methods for solving linear systems,we first need to be able to measure the distance between $\pmb { n }$ -dimensional column vectors to determine whether a sequence of vectors converges to a solution of the system. In actuality, this measure is also needed when the solution is obtained by the direct methods presented in Chapter 6. Those methods required a large number of arithmetic operations,and using finite-digit arithmetic leads only to an approximation to an actual solution of the system.

Let $\mathbb { R } ^ { n }$ denote the set of all $\pmb { n }$ -dimensional column vectors with real-number coeffcients. To define a distance in $\mathbb { R } ^ { n }$ we use the notion of a norm.

# Definition 7.1

A vector norm on $\mathbb { R } ^ { n }$ is a function, $\| \cdot \|$ ,from $\mathbb { R } ^ { n }$ into $\mathbb { R }$ with the following properties:

(i） $\left\| \mathbf { x } \right\| \geq 0 { \mathrm { ~ f o r ~ a l l ~ } } \mathbf { x } \in \mathbb { R } ^ { n } ,$ (ii） $\| \mathbf { x } \| = 0$ if and only if $\mathbf { x } = \mathbf { 0 }$ ， (i) $\| \alpha \mathbf { x } \| = | \alpha | \| \mathbf { x } \|$ for all $\alpha \in \mathbb { R }$ and $\mathbf { x } \in \mathbb { R } ^ { n }$ ， (iv） $\| \mathbf { x } + \mathbf { y } \| \leq \| \mathbf { x } \| + \| \mathbf { y } \|$ for all x $\mathbf { \Delta } _ { : , \textbf { y } \in \mathbb { R } ^ { n } }$

We will need only two specific norms on $\mathbb { R } ^ { n }$ , although a third norm on $\mathbb { R } ^ { n }$ is presented in Exercise 2.

Since vectors in $\mathbb { R } ^ { n }$ are column vectors,it is convenient to use the transpose notation presented in Section 6.3 when a vector is represented in terms of its components. For example, the vector

$$
\mathbf { x } = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] }
$$

will be written $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ ·

# Definition 7.2

The $l _ { 2 }$ and $l _ { \infty }$ norms for the vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ are defined by

$$
\| { \mathbf { x } } \| _ { 2 } = \left\{ \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \right\} ^ { 1 / 2 } \quad { \mathrm { a n d } } \quad \| { \mathbf { x } } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } | x _ { i } | .
$$

The $l _ { 2 }$ norm is called the Euclidean norm of the vector $\pmb { \mathrm { x } }$ since it represents the usual notion of distance from the origin in case $\mathbf { x }$ is in $\mathbb { R } ^ { 1 } \equiv \mathbb { R } , \mathbb { R } ^ { 2 }$ ,or ${ \mathbb { R } } ^ { 3 }$ . For example, the $l _ { 2 }$ norm of the vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t }$ gives the length of the straight line joining the points (0,0,0) and $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ . Figure 7.1 shows the boundary of those vectors in $\mathbb { R } ^ { 2 }$ and $\mathbb { R } ^ { 3 }$ that have $l _ { 2 }$ norm less than 1.Figure 7.2 is a similar illustration for the ${ l } _ { \infty }$ norm.

![](images/486ed58bfe705f3c1b8cff6ef1ce1b012ecd231392a01787c52438a987444183.jpg)  
Figure 7.1

![](images/6cdcd9eec07c96d0771ff0d12dbc9a8e1a2175bba2c58e99c7d6383f43be2e39.jpg)  
Figure 7.2

# EXAMPlE 1

The vector $\mathbf { x } = ( - 1 , 1 , - 2 ) ^ { t }$ in ${ \mathbb { R } } ^ { 3 }$ has norms

$$
\| \mathbf { x } \| _ { 2 } = { \sqrt { ( - 1 ) ^ { 2 } + ( 1 ) ^ { 2 } + ( - 2 ) ^ { 2 } } } = { \sqrt { 6 } }
$$

and

$$
\| \mathbf { x } \| _ { \infty } = \operatorname* { m a x } \{ | - 1 | , | 1 | , | - 2 | \} = 2 .
$$

It is easy to show that the properties in Definition 7.1 hold for the $l _ { \infty }$ norm since they follow from similar results for absolute values.For example,if $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ and $\mathbf { y } = ( y _ { 1 } , y _ { 2 } , \ldots , y _ { n } ) ^ { t }$ ,then

$$
\mathbf { y } \| _ { \infty } = \underset { 1 \leq i \leq n } { \operatorname* { m a x } } \left| x _ { i } + y _ { i } \right| \leq \underset { 1 \leq i \leq n } { \operatorname* { m a x } } \left( | x _ { i } | + | y _ { i } | \right) \leq \underset { 1 \leq i \leq n } { \operatorname* { m a x } } \left| x _ { i } \right| + \underset { 1 \leq i \leq n } { \operatorname* { m a x } } \left| y _ { i } \right| = \| \mathbf { x } \| _ { \infty } + \| \mathbf { y } \| _ { \infty }
$$

To show that

$$
\| \mathbf { x } + \mathbf { y } \| _ { 2 } \leq \| \mathbf { x } \| _ { 2 } + \| \mathbf { y } \| _ { 2 } , \quad { \mathrm { f o r ~ e a c h ~ } } \mathbf { x } , \mathbf { y } \in \mathbb { R } _ { n } ,
$$

we need a famous inequality.

# Theorem 7.3

# (Cauchy-Buniakowsky-Schwarz Inequality for Sums)

For each $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ and $\mathbf { y } = ( y _ { 1 } , y _ { 2 } , \dots , y _ { n } ) ^ { t } \ \mathrm { i }$ n $\mathbb { R } ^ { n }$ ，

$$
\mathbf { x } ^ { t } \mathbf { y } = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq { \biggl \{ } \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } { \biggr \} } ^ { 1 / 2 } { \biggl \{ } \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } { \biggr \} } ^ { 1 / 2 } = \| \mathbf { x } \| \cdot \| \mathbf { y } \| .
$$

Proof If $\mathbf y = \mathbf 0$ or $\mathbf { x } = \mathbf { 0 }$ ,the result is immediate since both sides of the inequality are zero.

Suppose $\textbf { y } \neq \textbf { 0 }$ and $\mathbf { x } \neq \mathbf { 0 }$ .For each $\lambda \in \mathbb { R }$ ，

$$
0 \leq | | \mathbf { x } - \lambda \mathbf { y } | | _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { n } ( x _ { i } - \lambda y _ { i } ) ^ { 2 } = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } - 2 \lambda \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } + \lambda ^ { 2 } \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } ,
$$

and

$$
2 \lambda \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } + \lambda ^ { 2 } \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| \mathbf { y } \| _ { 2 } ^ { 2 } .
$$

Since $\| \mathbf { x } \| _ { 2 } > 0$ and $\| \mathbf { y } \| _ { 2 } > 0$ , we can let $\lambda = \| \mathbf { x } \| _ { 2 } / \| \mathbf { y } \| _ { 2 }$ to give

$$
\left( 2 \frac { \| \mathbf { x } \| _ { 2 } } { \| \mathbf { y } \| _ { 2 } } \right) \left( \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \right) \leq \| \mathbf { x } \| _ { 2 } ^ { 2 } + \frac { \| \mathbf { x } \| _ { 2 } ^ { 2 } } { \| \mathbf { y } \| _ { 2 } ^ { 2 } } \| \mathbf { y } \| _ { 2 } ^ { 2 } = 2 \| \mathbf { x } \| _ { 2 } ^ { 2 } ,
$$

so

$$
2 \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq 2 \| \mathbf { x } \| _ { 2 } ^ { 2 } { \frac { \| \mathbf { y } \| _ { 2 } } { \| \mathbf { x } \| _ { 2 } } } = 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } .
$$

Thus,

$$
\mathbf { x } ^ { t } \mathbf { y } = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } = { \bigg \{ } \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } { \bigg \} } ^ { 1 / 2 } { \bigg \{ } \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } { \bigg \} } ^ { 1 / 2 } .
$$

With this result we see that for each $\mathbf { x } , \mathbf { y } \in \mathbb { R } ^ { n }$ ，

$$
+ \mathbf { y } \| _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { n } ( x _ { i } + y _ { i } ) ^ { 2 } = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } + 2 \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } + \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } \leq \| \mathbf { x } \| _ { 2 } ^ { 2 } + 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } + \| \mathbf { y } \| _ { 2 } ^ { 2 } ,
$$

which gives the final norm property

$$
\| \mathbf { x } + \mathbf { y } \| _ { 2 } \leq \left( \| \mathbf { x } \| _ { 2 } ^ { 2 } + 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } + \| \mathbf { y } \| _ { 2 } ^ { 2 } \right) ^ { 1 / 2 } = \| \mathbf { x } \| _ { 2 } + \| \mathbf { y } \| _ { 2 } .
$$

Since the norm of a vector gives a measure for the distance between an arbitrary vector and the zero vector, the distance between two vectors is defined as the norm of the difference of the vectors.

# Definition 7.4

$\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) ^ { t }$ and $\mathbf { y } = ( y _ { 1 } , y _ { 2 } , \ldots , y _ { n } ) ^ { t }$ are vectors in $\mathbb { R } ^ { n }$ ,the $l _ { 2 }$ and $l _ { \infty }$ distances between $\pmb { \mathrm { x } }$ and $\mathbf { y }$ are defined by

$$
\| \mathbf { x } - \mathbf { y } \| _ { 2 } = \left\{ \sum _ { i = 1 } ^ { n } ( x _ { i } - y _ { i } ) ^ { 2 } \right\} ^ { 1 / 2 } \quad { \mathrm { a n d } } \quad \| \mathbf { x } - \mathbf { y } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } | x _ { i } - y _ { i } | .
$$

# EXAMPLE 2 The linear system

$$
\begin{array} { c } { 3 . 3 3 3 0 x _ { 1 } + 1 5 9 2 0 x _ { 2 } - 1 0 . 3 3 3 x _ { 3 } = 1 5 9 1 3 , } \\ { } \\ { 2 . 2 2 2 0 x _ { 1 } + 1 6 . 7 1 0 x _ { 2 } + 9 . 6 1 2 0 x _ { 3 } = 2 8 . 5 4 4 , } \\ { 1 . 5 6 1 1 x _ { 1 } + 5 . \dot { 1 7 } 9 1 x _ { 2 } + 1 . 6 8 5 2 x _ { 3 } = 8 . 4 2 5 4 } \end{array}
$$

has solution $( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ^ { t } = ( 1 , 1 , 1 ) ^ { t }$ . If Gaussian elimination is performed in five-digit rounding arithmetic using maximal column pivoting (Algorithm 6.2), the solution obtained is

$$
\tilde { \mathbf { x } } = ( \tilde { x } _ { 1 } , \tilde { x } _ { 2 } , \tilde { x } _ { 3 } ) ^ { t } = ( 1 . 2 0 0 1 , 0 . 9 9 9 9 1 , 0 . 9 2 5 3 8 ) ^ { t } .
$$

Measurements of $\mathbf { x } - \tilde { \mathbf { x } }$ are given by

$$
\begin{array} { c } { { \| { \bf x } - \tilde { \bf x } \| _ { \infty } = \operatorname* { m a x } \{ | 1 - 1 . 2 0 0 1 | , | 1 - 0 . 9 9 9 9 1 | , | 1 - 0 . 9 2 5 3 8 | \} } } \\ { { { } } } \\ { { = \operatorname* { m a x } \{ 0 . 2 0 0 1 , 0 . 0 0 0 0 9 , 0 . 0 7 4 6 2 \} = 0 . 2 0 0 1 } } \end{array}
$$

and

$$
\begin{array} { r } { \| \mathbf { x } - \tilde { \mathbf { x } } \| _ { 2 } = \left[ ( 1 - 1 . 2 0 0 1 ) ^ { 2 } + ( 1 - 0 . 9 9 9 9 1 ) ^ { 2 } + ( 1 - 0 . 9 2 5 3 8 ) ^ { 2 } \right] ^ { 1 / 2 } } \\ { = [ ( 0 . 2 0 0 1 ) ^ { 2 } + ( 0 . 0 0 0 0 9 ) ^ { 2 } + ( 0 . 0 7 4 6 2 ) ^ { 2 } ] ^ { 1 / 2 } = 0 . 2 1 3 5 6 . } \end{array}
$$

Although the components $\tilde { x } _ { 2 }$ and $\tilde { x } _ { 3 }$ are good approximations to $x _ { 2 }$ and $x _ { 3 }$ , the component $\tilde { x } _ { 1 }$ is a poor approximation to $x _ { 1 }$ , and $| x _ { 1 } - \tilde { x } _ { 1 } |$ dominates the norms.

The concept of distance in $\mathbb { R } ^ { n }$ is also used to define a limit of a sequence of vectors in this space.

# Definition 7.5

A sequence $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 1 } ^ { \infty }$ of vectors in $\mathbb { R } ^ { n }$ is said to converge to $\mathbf { x }$ with respect to the norm $\| \cdot \|$ if, given any $\varepsilon > 0$ ,there exists an integer $N ( \varepsilon )$ such that

$$
\| { \mathbf { x } } ^ { ( k ) } - { \mathbf { x } } \| < \varepsilon , \quad \mathrm { f o r ~ a l l } \ k \geq N ( \varepsilon ) .
$$

# Theorem 7.6

The sequence of vectors $\{ \mathbf { x } ^ { ( k ) } \}$ converges to $\mathbf { x }$ in $\mathbb { R } ^ { n }$ with respect to $\| \cdot \| _ { \infty }$ if and only if $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } \dot { x } _ { i } ^ { ( k ) } = x _ { i } } \end{array}$ , for each $i = 1 , 2 , \dots , n$

Proof Suppose $\{ \mathbf { x } ^ { ( k ) } \}$ converges to x with respect to $\| \cdot \| _ { \infty }$ . Given any $\varepsilon > 0$ , there exists an integer $N ( \varepsilon )$ such that for all $k \geq N ( \varepsilon )$ ，

$$
\operatorname* { m a x } _ { i = 1 , 2 , \ldots , n } | x _ { i } ^ { ( k ) } - x _ { i } | = \| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| _ { \infty } < \varepsilon .
$$

This result implies that $| x _ { i } ^ { ( k ) } - x _ { i } | < \varepsilon$ ,for each $i = 1 , 2 , \dots , n , \mathrm { s o } \operatorname* { l i m } _ { k \to \infty } x _ { i } ^ { ( k ) } = x _ { i }$ for each $i$ ，

Conversely, suppose that $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } x _ { i } ^ { ( k ) } = x _ { i } } \end{array}$ ， for every $i = 1 , 2 , \dots , n$ For a given $\varepsilon > 0$ ,let $N _ { i } ( \varepsilon )$ for each $i$ represent an integer with the property that

$$
| x _ { i } ^ { ( k ) } - x _ { i } | < \varepsilon ,
$$

whenever $k \geq N _ { i } ( \varepsilon )$

Define $N ( \varepsilon ) = \mathrm { m a x } _ { i = 1 , 2 , \dots , n } N _ { i } ( \varepsilon )$ If $k \geq N ( \varepsilon )$ , then

$$
\operatorname* { m a x } _ { i = 1 , 2 , \ldots , n } | x _ { i } ^ { ( k ) } - x _ { i } | = \| { \mathbf { x } } ^ { ( k ) } - { \mathbf { x } } \| _ { \infty } < \varepsilon .
$$

This implies that $\{ \mathbf { x } ^ { ( k ) } \}$ converges to $\mathbf { x }$ with respect to $\| \cdot \| _ { \infty }$

EXAMPLE 3 Let $\mathbf { X } ^ { ( k ) } \in \mathbb { R } ^ { 4 }$ be defined by

$$
\mathbf { x } ^ { ( k ) } = ( x _ { 1 } ^ { ( k ) } , x _ { 2 } ^ { ( k ) } , x _ { 3 } ^ { ( k ) } , x _ { 4 } ^ { ( k ) } ) ^ { t } = \left( 1 , 2 + { \frac { 1 } { k } } , { \frac { 3 } { k ^ { 2 } } } , e ^ { - k } \sin k \right) ^ { t } .
$$

Since $\scriptstyle \operatorname* { l i m } _ { k \to \infty } 1 = 1$ ， $\mathrm { l i m } _ { k \to \infty } ( 2 + 1 / k ) = 2$ ， $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } 3 / k ^ { 2 } = 0 } \end{array}$ and $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } e ^ { - k } \sin k = } \end{array}$ O,Theorem 7.6 implies that the sequence $\{ \mathbf { x } ^ { ( k ) } \}$ converges to $( 1 , 2 , 0 , 0 ) ^ { t }$ with respect to $1 1 \cdot 1 1 \infty$

To show directly that the sequence in Example 3 converges to $( 1 , 2 , 0 , 0 ) ^ { t }$ with respect to the $l _ { 2 }$ norm is quite complicated. It is easier to prove the next result and apply it to this special case.

# Theorem 7.7

For each $\mathbf { x } \in \mathbb { R } ^ { n }$

$$
\| \mathbf { x } \| _ { \infty } \leq \| \mathbf { x } \| _ { 2 } \leq { \sqrt { n } } \| \mathbf { x } \| _ { \infty } .
$$

Proof Let $x _ { j }$ be a coordinate of $\mathbf { x }$ such that $\| \mathbf { x } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } | x _ { i } | = | x _ { j } |$ . Then

$$
\| \mathbf { x } \| _ { \infty } ^ { 2 } = | x _ { j } | ^ { 2 } = x _ { j } ^ { 2 } \leq \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } ,
$$

so

$$
\| \mathbf { x } \| _ { \infty } \leq \| \mathbf { x } \| _ { 2 } ,
$$

and

$$
\| \mathbf { x } \| _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \leq \sum _ { i = 1 } ^ { n } x _ { j } ^ { 2 } = n x _ { j } ^ { 2 } = n | | \mathbf { x } | | _ { \infty } ^ { 2 } ,
$$

s0 $\| \mathbf { x } \| _ { 2 } \leq { \sqrt { n } } \| \mathbf { x } \| _ { \infty } .$

Figure 7.3 illustrates this result when $n = 2$

![](images/399e4bd095b93e65322e0966ddd2ac5ed7f5bbf8676052f2d0d11921970e6f66.jpg)  
Figure 73

In Example 3, we found that the sequence $\{ \mathbf { x } ^ { ( k ) } \}$ , defined by

$$
\mathbf { x } ^ { ( k ) } = \left( 1 , 2 + { \frac { 1 } { k } } , { \frac { 3 } { k ^ { 2 } } } , e ^ { - k } \sin k \right) ^ { t } ,
$$

converges to $\mathbf { x } = ( 1 , 2 , 0 , 0 ) ^ { t }$ with respect to $\| \cdot \| _ { \infty }$ . Given any $\varepsilon > 0$ , there exists an integer $N ( \varepsilon / 2 )$ with the property that

$$
\| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| _ { \infty } < \frac { \varepsilon } { 2 } ,
$$

whenever $k \geq N ( \varepsilon / 2 )$ . By Theorem 7.7, this implies that

$$
\| { \mathbf { x } } ^ { ( k ) } - { \mathbf { x } } \| _ { 2 } < \sqrt { 4 } \| { \mathbf { x } } ^ { ( k ) } - { \mathbf { x } } \| _ { \infty } < 2 ( \varepsilon / 2 ) = \varepsilon ,
$$

when $k \geq N ( \varepsilon / 2 )$ . So $\{ \mathbf { x } ^ { ( k ) } \}$ also converges to $\mathbf { x }$ with respect to $\| \cdot \| _ { 2 }$

It can be shown that all norms on $\mathbb { R } ^ { n }$ are equivalent with respect to convergence; that is,if $\| \cdot \|$ and $\| \cdot \| ^ { \prime }$ are any two norms on $\mathbb { R } ^ { n }$ and $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 1 } ^ { \infty }$ has the limit $\mathbf { x }$ with respect to $\| \cdot \|$ ,then $\{ \mathbf { x } ^ { ( k ) } \} _ { k = 1 } ^ { \infty }$ also has the limit $\pmb { \mathrm { x } }$ with respect to $\| \cdot \| ^ { \prime }$ . The proof of this fact for the general case can be found in [Or2, p.8]. The case for the norms $\| \cdot \| _ { 2 }$ and $\| \cdot \| _ { \infty }$ follows from Theorem 7.7.

In the subsequent sections of this and later chapters,we will need methods for determining the distance between $n \times n$ matrices. This again requires the use of a norm.

A matrix norm on the set of all $n \times n$ matrices is a real-valued function, $\| \cdot \|$ , defined on this set, satisfying for all $n \times n$ matrices $A$ and $B$ and all real numbers $\pmb { \alpha }$ ：

(i） $\| A \| \geq 0 ;$ (i） $\| A \| = 0$ , if and only if $\pmb { A }$ is $o$ ,the matrix with al O entries;

(ii） $\| \alpha A \| = | \alpha | \| A \| ;$ (iv） $\| A + B \| \leq \| A \| + \| B \| ;$ （v） $\| A B \| \leq \| A \| \| B \| .$

The distance between n × n matrices $A$ and $B$ with respect to this matrix norm is $\| A - B \|$

Although matrix norms can be obtained in various ways,the only norms we consider are.those that are natural consequences of the vector norms $l _ { 2 }$ and $l _ { \infty }$

The following theorem is not difficult to show, and its proof is left as Exercise 13.

Theorem 7.9

If $| | \cdot | |$ is a vector norm on $\mathbb { R } ^ { n }$ ,then

$$
\| A \| = \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| A \mathbf { x } \|
$$

is a matrix norm.

This is called the natural, or induced, matrix norm associated with the vector norm. In this text, all matrix norms will be assumed to be natural matrix norms unless specified otherwise.

For any $\mathbf { z } \neq \mathbf { 0 }$ , we have ${ \bf x } = { \bf z } / \| { \bf z } \|$ as a unit vector. Hence,

$$
\operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| A \mathbf { x } \| = \operatorname* { m a x } _ { \mathbf { z } \neq \mathbf { 0 } } \left\| A \left( { \frac { \mathbf { z } } { \| \mathbf { z } \| } } \right) \right\| = \operatorname* { m a x } _ { \mathbf { z } \neq \mathbf { 0 } } { \frac { \| A \mathbf { z } \| } { \| \mathbf { z } \| } } ,
$$

and we can alternatively write

$$
\left\| A \right\| = \operatorname* { m a x } _ { \mathbf { z } \neq 0 } { \frac { \| A \mathbf { z } \| } { \| \mathbf { z } \| } } .
$$

The following corollary to Theorem 7.9 follows from this representation of $\| A \|$

For any vector $\mathbf { z } \neq \mathbf { 0 }$ ,matrix $A$ , and any natural norm $\| \cdot \|$ ,we have

$$
\| A \mathbf { z } \| \leq \| A \| \cdot \| \mathbf { z } \| .
$$

The measure given to a matrix under a natural norm describes how the matrix stretches unit vectors relative to that norm. The maximum stretch is the norm of the matrix. The matrix norms we will consider have the forms

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { \infty } = 1 } \| A \mathbf { x } \| _ { \infty } , \quad \mathrm { t h e } l _ { \infty } \mathrm { n o r m } ,
$$

and

$$
\| A \| _ { 2 } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { 2 } = 1 } \| A \mathbf { x } \| _ { 2 } , \quad \mathrm { t h e } l _ { 2 } \operatorname { n o r m } .
$$

![](images/a6b1a1346069a81b57da24923d4c0637397cf5b76297a8133ece2234adcf1e2c.jpg)  
Figure 7.4

![](images/9f88ccff092df9c4d09b81f3304690de966a6c4ff8614e21d8ce1d1f9e7f0596.jpg)  
Figure 7.5

An illustration of these norms when $n = 2$ is shown in Figures 7.4 and 7.5.   
The $l _ { \infty }$ norm of a matrix can be easily computed from the entries of the matrix.

Theorem 7.11 If $A = ( a _ { i j } )$ is an $n \times n$ matrix, then

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

Proof First we show that $\begin{array} { r } { \| A \| _ { \infty } \leq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | } \end{array}$ .Let $\mathbf { x }$ be an $\pmb { n }$ -dimensional vector with $1 = \| \mathbf { x } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } | x _ { i } |$ . Since $\pmb { A } \pmb { \mathrm { x } }$ is also an $\pmb { n }$ -dimensional vector,

$$
\| A \mathbf { x } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } | ( A \mathbf { x } ) _ { i } | = \operatorname* { m a x } _ { 1 \leq i \leq n } \left| \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right| \leq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | \operatorname* { m a x } _ { 1 \leq j \leq n } | x _ { j } | .
$$

But $\operatorname* { m a x } _ { 1 \leq j \leq n } | x _ { j } | = \| { \mathbf { x } } \| _ { \infty } = 1$ ,s0

$$
\| A \mathbf { x } \| _ { \infty } \leq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

Consequently,

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { \infty } = 1 } \| A \mathbf { x } \| _ { \infty } \leq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

Now we will show the opposite inequality, that $\begin{array} { r } { \| A \| _ { \infty } \geq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | } \end{array}$ .Let $p$ be an integer with

$$
\sum _ { j = 1 } ^ { n } | a _ { p j } | = \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ,
$$

and $\mathbf { x }$ be the vector with components

$$
x _ { j } = \left\{ { \begin{array} { r l } { 1 , } & { { \mathrm { i f } } \ a _ { p j } \geq 0 , } \\ { - 1 , } & { { \mathrm { i f } } \ a _ { p j } < 0 . } \end{array} } \right.
$$

Then $\| \mathbf { x } \| _ { \infty } = 1$ and $a _ { p j } x _ { j } = | a _ { p j } |$ , for all $j = 1 , 2 , \dots , n , s$ 60

$$
\| A \mathbf { x } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } \left| \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right| \geq \left| \sum _ { j = 1 } ^ { n } a _ { p j } x _ { j } \right| = \left| \sum _ { j = 1 } ^ { n } | a _ { p j } | \right| = \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

This result implies that

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { \infty } = 1 } \| A \mathbf { x } \| _ { \infty } \geq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ,
$$

which,together with Inequality (7.3), gives

$$
\| A \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 0 } & { 3 } & { - 1 } \\ { 5 } & { - 1 } & { 1 } \end{array} } \right] ,
$$

then

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 1 } ^ { 3 } | a _ { 1 j } | = | 1 | + | 2 | + | - 1 | = 4 , } } \\ { { \displaystyle \sum _ { j = 1 } ^ { 3 } | a _ { 2 j } | = | 0 | + | 3 | + | - 1 | = 4 , } } \end{array}
$$

and

$$
\sum _ { j = 1 } ^ { 3 } | a _ { 3 j } | = | 5 | + | - 1 | + | 1 | = 7 ;
$$

So

$$
\| A \| _ { \infty } = \operatorname* { m a x } \{ 4 , 4 , 7 \} = 7 .
$$

In the next section, we will discover an alternative method for finding the $l _ { 2 }$ norm of a matrix.

# Exercise set 7.1

1.Find $\| \mathbf { x } \| _ { \infty }$ and $\| \mathbf { x } \| _ { 2 }$ for the following vectors.

a. $\mathbf { x } = ( 3 , - 4 , 0 , \textstyle { \frac { 3 } { 2 } } ) ^ { t }$   
$\mathbf { b } _ { \bullet }$ $\mathbf { x } = ( 2 , 1 , - 3 , 4 ) ^ { t }$   
c. ${ \bf x } = ( \sin k , \cos k , 2 ^ { k } ) ^ { t }$ for a fixed positive integer $k$   
d. $\mathbf { x } = ( 4 / ( k + 1 ) , 2 / k ^ { 2 } , k ^ { 2 } e ^ { - k } ) ^ { t }$ for a fixed positive integer $k$

2.a.Verify that the function $\| \cdot \| _ { 1 }$ , defined on $\mathbb { R } ^ { n }$ by

$$
\| \mathbf { x } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } | ,
$$

is a norm on $\mathbb { R } ^ { n }$

b. Find $\| \mathbf { x } \| _ { 1 }$ for the vectors given in Exercise 1. $\pmb { \mathbb { c } } _ { \bullet }$ Prove that for all $\mathbf { z } \in \mathbb { R } ^ { n }$ ， $\| \mathbf { x } \| _ { 1 } \geq \| \mathbf { x } \| _ { 2 }$

3.Prove that the following sequences are convergent, and find their limits.

$$
\begin{array} { r l } & { \mathbf { x } ^ { ( k ) } = ( 1 / k , e ^ { 1 - k } , - 2 / k ^ { 2 } ) ^ { t } } \\ & { \mathbf { x } ^ { ( k ) } = \left( e ^ { - k } \cos k , k \sin ( 1 / k ) , 3 + k ^ { - 2 } \right) ^ { t } } \\ & { \mathbf { x } ^ { ( k ) } = ( k e ^ { - k ^ { 2 } } , ( \cos k ) / k , \sqrt { k ^ { 2 } + k } - k ) ^ { t } } \\ & { \mathbf { x } ^ { ( k ) } = ( e ^ { 1 / k } , ( k ^ { 2 } + 1 ) / ( 1 - k ^ { 2 } ) , ( 1 / k ^ { 2 } ) ( 1 + 3 + 5 + \cdots + ( 2 k - 1 ) ) ^ { t } } \end{array}
$$

4.Find $\| \cdot \| _ { \infty }$ for the following matrices.

$\mathbf { a } , \quad \left[ \begin{array} { l l } { 1 0 } & { \cdots } \\ { 0 } & { 1 } \end{array} \right]$ $\mathbf { b } . \quad \left[ \begin{array} { l l } { 1 0 } & { 0 } \\ { 1 5 } & { 1 } \end{array} \right]$

$\begin{array} { r l } { \mathbf { c } . } & { { } \left[ \begin{array} { l l l } { \ 2 } & { - 1 } & { \ 0 } \\ { - 1 } & { \ 2 } & { - 1 } \\ { \ 0 } & { - 1 } & { \ 2 } \end{array} \right] } \end{array}$ $\mathbf { d } . \quad \left[ { \begin{array} { r r r } { 4 } & { - 1 } & { 7 } \\ { - 1 } & { 4 } & { 0 } \\ { - 7 } & { 0 } & { 4 } \end{array} } \right]$

5.The following linear systems $A \mathbf { x } = \mathbf { b }$ have $\mathbf { x }$ as the actual solution and $\tilde { \bf x }$ as an approximate solution. Compute $\| { \bf x } - \tilde { { \bf x } } \| _ { \infty } \mathrm { a n d } \| \mathrm { } A \tilde { { \bf x } } - { \bf b } \| _ { \infty }$

$$
\begin{array} { r l } & { \frac { 1 } { 2 } x _ { 1 } + \frac { 1 } { 3 } x _ { 2 } = \frac { 1 } { 6 3 } , } \\ & { \frac { 1 } { 3 } x _ { 1 } + \frac { 1 } { 4 } x _ { 2 } = \frac { 1 } { 1 6 8 } , } \\ & { \mathbf { x } = \left( \frac { 1 } { 7 } , - \frac { 1 } { 6 } \right) ^ { t } , } \\ & { \tilde { \mathbf { x } } = ( 0 . 1 4 2 , - 0 . 1 6 6 ) ^ { t } . } \end{array}
$$

b. x1+2x+3x=1, $2 x _ { 1 } + 3 x _ { 2 } + 4 x _ { 3 } = - 1 ,$ $3 x _ { 1 } + 4 x _ { 2 } + 6 x _ { 3 } = 2 ,$ x = (0,-7,5)', $\tilde { \mathbf { x } } = ( - 0 . 3 3 , - 7 . 9 , 5 . 8 ) ^ { t } .$

c. $x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = 1 { \mathrm { . } }$ $2 x _ { 1 } + 3 x _ { 2 } + 4 x _ { 3 } = - 1 ,$ $3 x _ { 1 } + 4 x _ { 2 } + 6 x _ { 3 } = 2 ,$ X = (0,-7,5)', $\tilde { \mathbf { x } } = ( - 0 . 2 , - 7 . 5 , 5 . 4 ) ^ { t } .$ d. $0 . 0 4 x _ { 1 } + 0 . 0 1 x _ { 2 } - 0 . 0 1 x _ { 3 } = 0 . 0 6 ,$ $\begin{array} { r l } { 0 . 2 x _ { 1 } + } & { { } 0 . 5 x _ { 2 } - } & { 0 . 2 x _ { 3 } = 0 . 3 , } \\ { x _ { 1 } + } & { { } 2 x _ { 2 } + } & { 4 x _ { 3 } = 1 1 , } \end{array}$ $\begin{array} { r l } & { \mathbf { x } = ( 1 . 8 2 7 5 8 6 , 0 . 6 5 5 1 7 2 4 , 1 . 9 6 5 5 1 7 ) ^ { t } , } \\ & { \tilde { \mathbf { x } } = ( 1 . 8 , 0 . 6 4 , 1 . 9 ) ^ { t } . } \end{array}$

6.The matrix norm $\| \cdot \| _ { 1 }$ , defined by $\| A \| _ { 1 } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { 1 } = 1 } \| A \mathbf { x } \| _ { 1 }$ , can be computed using the formula

$$
\| A \| _ { 1 } = \operatorname* { m a x } _ { 1 \leq j \leq n } \sum _ { i = 1 } ^ { n } | a _ { i j } | ,
$$

where the vector norm $\| \cdot \| _ { 1 }$ is defined in Exercise 2.Find $\| \cdot \| _ { 1 }$ for the matrices in Exercise 4.

7．Show by example that $\| \cdot \| _ { \infty }$ ,defined by $\| A \| _ { \circledast } = \operatorname* { m a x } _ { 1 \leq i , j \leq n } | a _ { i j } | ,$ ,does not define a matrix norm.

8.Show that $\| \cdot \| _ { \mathfrak { D } }$ ,defined by

$$
\| A \| _ { \mathfrak { D } } = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ,
$$

is a matrix norm. Find $\| \cdot \| _ { \mathfrak { D } }$ for the matrices in Exercise 4.

9.a.The Frobenius norm (which is not a natural norm) is defined for an $n \times n$ matrix $A$ by

$$
\| A \| _ { F } = \left( \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) ^ { 1 / 2 } .
$$

Show that $\| \cdot \| _ { F }$ is a matrix norm.

b. Find $\| \cdot \| _ { F }$ for the matrices in Exercise 4. $\pmb { \mathrm { c } } _ { \pmb { \mathrm { \bullet } } }$ For any matrix $\pmb { A }$ ,show that $\| A \| _ { 2 } \leq \| A \| _ { F } \leq n ^ { 1 / 2 } \| A \| _ { 2 }$

10.In Exercise 9 the Frobenius norm of a matrix was defined. Show that for any $n \times n$ matrix A and vector $\mathbf { x }$ in $\mathbb { R } ^ { n }$ ， $\| A \mathbf { x } \| _ { 2 } \leq \| A \| _ { F } \| \mathbf { x } \| _ { 2 }$

11. Let $s$ be a positive definite $n \times n$ matrix. For any $\mathbf { x }$ in $\mathbb { R } ^ { n }$ define $\| { \bf x } \| = ( { \bf x } ^ { t } S { \bf x } ) ^ { 1 / 2 }$ . Show that this defines a norm on $\textstyle { \mathbb { R } } ^ { n }$ .[Hint: Use Choleski factorization of $s$ to show that $\mathbf { x } ^ { t } S \mathbf { y } = \mathbf { y } ^ { t } S \mathbf { x } \le$ $( \mathbf { x } ^ { t } S \mathbf { x } ) ^ { 1 / 2 } ( \mathbf { y } ^ { t } S \mathbf { y } ) ^ { 1 / 2 }$ ]

12.Let $S$ be a real and nonsingular matrix, and let $\| \cdot \|$ be any norm on $\mathbb { R } ^ { n }$ . Define $\vert \} \cdot $ by $\| \mathbf { x } \| ^ { \prime } = \| S \mathbf { x } \|$ . Show that $\| \cdot \| ^ { \prime }$ is also a norm on $\mathbb { R } ^ { n }$

13.Prove that if $\| \cdot \|$ is a vector norm on $\mathbb { R } ^ { n }$ , then $\| A \| = \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \left\| A \mathbf { x } \right\|$ is a matrix norm.

14. The following excerpt from the Mathematics Magazine $\{ S z \}$ gives an alternative way to prove the Cauchy-Buniakowsky-Schwarz Inequality.

a. Show that when $\mathbf { x } \neq \mathbf { 0 }$ and $\mathbf { y } \neq \mathbf { 0 }$ , we have

$$
{ \frac { \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } } { \left( \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } \right) ^ { 1 / 2 } } } = 1 - { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \left( { \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } - { \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \right) ^ { 2 } .
$$

b.Use the result in part (a) to show that

$$
\sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \left( \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } \right) ^ { 1 / 2 } .
$$

# 7.2 Eigenvalues and Eigenvectors

An $n \times m$ matrix can be considered as a function that uses matrix multiplication to take $m$ -dimensional vectors into $\pmb { n }$ -dimensional vectors. A square matrix $A$ takes the set of $n$ -dimensional vectors into itself. In this case,certain nonzero vectors $\mathbf { x }$ are parallel to $\pmb { A } \pmb { \mathrm { x } }$ ，which means that a constant $\lambda$ exists with $A \mathbf { x } \ = \ \lambda \mathbf { x }$ .For these vectors,we have $( A - \lambda I ) \mathbf { x } = \mathbf { 0 }$ . There is a close connection between these numbers $\lambda$ and the likelihood that an iterative method will converge. We will consider this connection in this section.

# Definition 7.12

f $A$ is a square matrix, the characteristic polynomial of $A$ is defined by

$$
p ( \lambda ) = \operatorname* { d e t } ( A - \lambda I ) .
$$

It is not difficult to show (see Exercise 7） that $p$ is an nth-degree polynomial and, consequently, has at most $\pmb { n }$ distinct zeros, some of which may be complex. If $\lambda$ is a zero of $p$ , then, since det $( A - \lambda I ) = 0$ ,Theorem 6.16 in Section 6.4 implies that the linear system defined by $( A - \lambda I ) \mathbf { x } = \mathbf { 0 }$ has a solution with $\mathbf { x } \neq \mathbf { 0 }$ . We wish to study the zeros of $p$ and the nonzero solutions corresponding to these systems.

f $p$ is the characteristic polynomial of the matrix $A$ ， the zeros of $p$ are eigenvalues, or characteristic values, of the matrix $\pmb { A }$ . If $\lambda$ is a eigenvalue of $A$ and $\textbf { x } \neq \pmb { \mathbb { 0 } }$ satisfies

$( A - \lambda I ) \mathbf { x } = \mathbf { 0 }$ ,then $\mathbf { x }$ is an eigenvector, or characteristic vector, of $A$ corresponding to the eigenvalue $\lambda$ ·

f $\pmb { \mathrm { x } }$ is an eigenvector associated with the eigenvalue $\lambda$ ，then $A \mathbf { x } = \lambda \mathbf { x }$ ,so the matrix $A$ takes the vector $\mathbf { x }$ into a scalar multiple of itself. If $\lambda$ is real and $\lambda > 1$ ，then $A$ has the effect of stretching $\mathbf { x }$ by a factor of $\lambda$ ,as illustrated in Figure 7.6(a). If $0 < \lambda < 1$ ， then $A$ shrinks $\mathbf { x }$ by a factor of $\lambda$ (see Figure 7.6(b)).When $\lambda < 0$ ,the effects are similar (see Figure 7.6(c) and (d)), although the direction of $\pmb { A } \pmb { \mathrm { x } }$ is reversed.

![](images/a18aa2a47b723d230990ec25cb4c8751eeb9040e6dfa1364a04886b72ea750f2.jpg)  
Figure 7.6

# EXAMPLE 1 Let

$$
A = \left[ { \begin{array} { r r r } { 1 } & { 0 } & { 2 } \\ { 0 } & { 1 } & { - 1 } \\ { - 1 } & { 1 } & { 1 } \end{array} } \right] .
$$

To compute the eigenvalues of $A$ , consider

$$
p ( \lambda ) = \operatorname * { d e t } ( A - \lambda I ) = \operatorname * { d e t } { \left[ \begin{array} { l l l } { 1 - \lambda } & { 0 } & { 2 } \\ { 0 } & { 1 - \lambda } & { - 1 } \\ { - 1 } & { 1 } & { 1 - \lambda } \end{array} \right] } = ( 1 - \lambda ) ( \lambda ^ { 2 } - 2 \lambda + 4 ) .
$$

The eigenvalues of $A$ are the solutions of $p ( \lambda ) = 0$ , which are $\lambda _ { 1 } = 1 , \lambda _ { 2 } = 1 + \sqrt { 3 } i$ ,and $\lambda _ { 3 } = \bar { 1 } - \sqrt { 3 } i$

An eigenvector $\mathbf { x }$ of $\pmb { A }$ associated with $\lambda _ { 1 }$ is a solution of the system $( A - \lambda _ { 1 } I ) \mathbf { x } = \mathbf { 0 }$ ：

$$
{ \left[ \begin{array} { l l l } { 0 } & { 0 } & { 2 } \\ { 0 } & { 0 } & { - 1 } \\ { - 1 } & { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } .
$$

Thus,

$$
2 x _ { 3 } = 0 , \quad - x _ { 3 } = 0 , \quad { \mathrm { a n d } } \quad - x _ { 1 } + x _ { 2 } = 0 ,
$$